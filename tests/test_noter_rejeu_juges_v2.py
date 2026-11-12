"""Rejeu de la cellule de juge redéfinie (GO-2026-10-29-04), v2, mode jouet : consigne (chaque critère porte son
échelle ; valeurs admises seules), lecture par probabilité restreinte aux valeurs admises suivies d'une fin de ligne
(valeurs exactes sur un modèle à bigrammes ; demi-point, valeur hors échelle et « 10 » non lus comme des entiers ;
espace non écrite comptée), lecture des branches par le cache égale à la lecture par passes complètes (modèle jouet),
garde d'encodage v2 et jetons terminaux (cas sain et artefacts, R5), génération bornée au bloc (égale à
`generer_lot` sans arrêt), gardes de configuration et de citation, chaîne jouet de bout en bout (génération du modèle
jouet, puis génération simulée par textes écrits), échéances, signal TERM, R12, lecture gelée."""
from __future__ import annotations

import hashlib
import json
import math
import subprocess
import time
from pathlib import Path
from types import SimpleNamespace

import pytest
import torch

from conftest import committer
from controle_ia import gardes
from controle_ia.environnements import lancer_pilote_a as lp
from controle_ia.environnements import noter_rejeu_juges_v1 as nrj
from controle_ia.environnements import noter_rejeu_juges_v2 as nrj2
from controle_ia.environnements.rubrique import CRITERES, lire_notes, points_max
from controle_ia.gardes import GardeArret
from controle_ia.harnais.episode import generer_lot
from controle_ia.harnais.modeles import modele_jouet
from controle_ia.manifeste import verifier_resultat
from controle_ia.scellement import empreinte, sceller
from test_noter_pilote_a import PILOTE
from test_noter_pilote_a import _config as _config_notations
from test_noter_rejeu_juges_v1 import (CTX, NOTATIONS, TokFusion, _i, _notations_artisanales, _reecrire,
                                       _tokeniseur_a_la_llama_3)
from test_pilote_a import FMT, TOK

NL = TOK.convert_tokens_to_ids("\n")
TERM = [NL]
NOTES = {"SPECIFICITY": 3, "COHERENCE": 2, "COVERAGE": 4, "FEASIBILITY": 1, "NOVELTY": 2, "RIGOR": 3, "BALANCE": 1,
         "RESULT_REASONING": 2, "REDUNDANCY_PENALTY": -1, "IRRELEVANCE_PENALTY": 0}


def _bloc(notes=None, echelle=True, brut=None):
    """Bloc des dix notes, forme à échelle (« NOM (lo to hi): v ») ou forme v1 ; `brut` remplace la valeur écrite de
    certains critères."""
    notes, brut = {**NOTES, **(notes or {})}, brut or {}
    lignes = []
    for nom, lo, hi in CRITERES:
        tete = f"{nom} ({lo} to {hi}):" if echelle else f"{nom}:"
        lignes.append(f"{tete} {brut.get(nom, notes[nom])}")
    return "\n".join(lignes)


COMPLET = _bloc()


# ---------------------------------------------------------------- modèle à bigrammes, avec un cache simulé

class FauxCache:
    """Cache simulé : une longueur, rognable par la fin (nombre négatif), comme `DynamicCache.crop`."""

    def __init__(self, n):
        self.n = n

    def get_seq_length(self):
        return self.n

    def crop(self, k):
        assert k < 0, "rognage par un nombre négatif seulement"
        self.n += k


class BigrammeCache(torch.nn.Module):
    """Logits du jeton suivant fonction du seul jeton courant (lois calculables à la main) ; rend un cache simulé."""

    def __init__(self, table):
        super().__init__()
        self.table = torch.nn.Parameter(table, requires_grad=False)

    def forward(self, input_ids, attention_mask=None, position_ids=None, use_cache=False, logits_to_keep=0,
                past_key_values=None, **_):
        lg = self.table[input_ids.to("cpu")]
        if isinstance(logits_to_keep, int):
            lg = lg[:, -logits_to_keep:] if logits_to_keep else lg
        else:
            lg = lg[:, logits_to_keep.to("cpu")]
        cache = None
        if use_cache:
            cache = past_key_values or FauxCache(0)
            cache.n += input_ids.shape[1]
        return SimpleNamespace(logits=lg, past_key_values=cache)


class SansCache(BigrammeCache):
    def forward(self, *a, **k):
        return SimpleNamespace(logits=super().forward(*a, **k).logits, past_key_values=None)


def _table(espace=None, moins=None, apres=None, deux_points=4.0):
    """Table de bigrammes : après « : », l'espace (logit `deux_points`) ; après l'espace, les chiffres et le signe ;
    après « - », le chiffre ; après chaque chiffre, la fin de ligne (logit 4 par défaut, `apres` pour changer)."""
    t = torch.full((len(TOK), len(TOK)), -8.0)
    t[_i(":"), _i(" ")] = deux_points
    for c, v in (espace or {"0": 3.0, "1": 1.0, "2": 1.0, "3": 2.0, "4": 1.0, "5": 0.0, "-": 2.0}).items():
        t[_i(" "), _i(c)] = v
    for c, v in (moins or {"1": 1.0, "2": 0.0}).items():
        t[_i("-"), _i(c)] = v
    for c in "012345":
        t[_i(c), NL] = 4.0
    for (c, d), v in (apres or {}).items():
        t[_i(c), _i(d)] = v
    return t


def _s(table, c):
    return torch.softmax(table[_i(c)], -1)


def _attendu(table, lo, hi):
    """Loi exacte d'une valeur écrite après « : » : espace, (signe), chiffre, puis fin de ligne (règle de la chaîne)."""
    p = {}
    for v in range(lo, hi + 1):
        x = float(_s(table, ":")[_i(" ")])
        x *= float(_s(table, " ")[_i("-")] * _s(table, "-")[_i(str(-v))]) if v < 0 else float(_s(table, " ")[_i(str(v))])
        p[v] = x * float(_s(table, str(abs(v)))[NL])
    masse = sum(p.values())
    return {v: x / masse for v, x in p.items()}, masse


def _lire(table, texte=COMPLET, complete=True, masse_min=0.5, modele=BigrammeCache):
    return nrj2.lire_par_probabilite_v2(modele(table), TOK, CTX, texte, CRITERES, complete, masse_min, TERM)


# ---------------------------------------------------------------- consigne

def test_consigne_chaque_critere_porte_son_echelle_et_valeurs_admises():
    c = nrj2.CONSIGNE_VERDICT_ECHELLES
    assert nrj2.EMPREINTE_CONSIGNE_V2 == hashlib.sha256(c.encode("utf-8")).hexdigest() != nrj.EMPREINTE_CONSIGNE
    lignes = c.splitlines()
    assert lignes[1:11] == [f"{n} ({lo} to {hi}): <integer>" for n, lo, hi in CRITERES]
    for m, (nom, lo, hi) in zip(nrj2._LIGNE_V2.finditer("\n".join(lignes[1:11])), CRITERES, strict=True):
        assert m["nom"] == nom and m["echelle"] == f"{lo} to {hi}"          # la ligne de consigne se lit comme un bloc
    assert "Only these values are allowed" in c and "No half points" in c and "outside the criterion's own scale" in c
    assert c.rstrip().endswith("After the tenth line, stop.")


# ---------------------------------------------------------------- lignes, bloc, lecture écrite stricte

def test_deux_formes_de_ligne_bloc_et_positions():
    for echelle in (True, False):
        texte = "Scores:\n" + _bloc(echelle=echelle) + "\nNow the analysis.\nSPECIFICITY (0 to 5): 5\n"
        bloc = nrj2.bloc_des_notes_v2(texte, CRITERES)
        assert bloc == "Scores:\n" + _bloc(echelle=echelle)
        assert nrj2.bloc_clos(texte, CRITERES) and not nrj2.bloc_clos(bloc, CRITERES)
        pos = nrj2.positions_des_valeurs_v2(bloc, CRITERES)
        assert all(bloc[pos[n]:pos[n] + len(str(v))] == str(v) for n, v in NOTES.items())
    assert nrj2.bloc_des_notes_v2(COMPLET.replace("NOVELTY", "NOVEL"), CRITERES) is None
    p = nrj2.positions_des_valeurs_v2(COMPLET.replace("RIGOR (0 to 4): 3", "RIGOR (0 to 4):  "), CRITERES)
    assert p["RIGOR"] is None
    assert nrj2.positions_des_valeurs_v2(COMPLET.replace("NOVELTY", "NOVEL"), CRITERES)["NOVELTY"] == "absent"


@pytest.mark.parametrize("brut, motif", [
    ("2.5", "valeur non admise"), ("3/5", "valeur non admise"), ("**3**", "valeur non admise"),
    ("3 (good)", "valeur non admise"), ("03", "non canonique"), ("6", "hors de [0, 5]"), ("+3", "valeur non admise"),
])
def test_lecture_ecrite_stricte_artefacts(brut, motif):
    e = nrj2.lecture_ecrite_v2(_bloc(brut={"SPECIFICITY": brut}), CRITERES)
    assert e["score"] is None and "SPECIFICITY" not in e["notes"]
    assert any(a.startswith("SPECIFICITY : ") and motif in a for a in e["anomalies"])


def test_lecture_ecrite_stricte_cas_sain():
    e = nrj2.lecture_ecrite_v2(_bloc(brut={"SPECIFICITY": "3 \t"}), CRITERES)
    assert e["notes"] == NOTES and e["anomalies"] == [] and e["lignes_a_echelle"] == 10
    assert e["score"] == lire_notes(_bloc(echelle=False)).score_sur_100()
    assert nrj2.lecture_ecrite_v2(_bloc(echelle=False), CRITERES)["lignes_a_echelle"] == 0
    hors = nrj2.lecture_ecrite_v2(_bloc(notes={"BALANCE": 4}), CRITERES)        # 4 sur [0, 3] : non admise
    assert hors["score"] is None and "BALANCE : 4 hors de [0, 3]" in hors["anomalies"]


# ---------------------------------------------------------------- lecture par probabilité, valeurs admises seules

def test_lecture_exacte_valeur_puis_fin_de_ligne():
    table = _table()
    r = _lire(table)
    total = 0.0
    for nom, lo, hi in CRITERES:
        loi, masse = _attendu(table, lo, hi)
        lu = r["criteres"][nom]
        assert all(math.isclose(lu["probabilites"][str(v)], p, rel_tol=1e-5) for v, p in loi.items())
        assert math.isclose(lu["masse"], masse, rel_tol=1e-5)
        assert all(math.isclose(lu["fin_de_ligne"][str(v)], float(_s(table, str(abs(v)))[NL]), rel_tol=1e-5)
                   for v in loi)
        total += lu["esperance"]
        c0 = COMPLET.rindex(f"{nom} (") + COMPLET[COMPLET.rindex(f"{nom} ("):].index(": ") + 2
        assert lu["position"] == len(CTX) + c0 and lu["prefixe"] == " " and lu["suite_commune"] == 1
    assert math.isclose(r["score"], 100 * max(0.0, total) / points_max(CRITERES), rel_tol=1e-6)
    assert r["motif"] is None
    # une passe principale, puis un prolongement du cache par valeur non écrite : 5+5+5+4+4+4+3+3+2+2 = 37
    assert r["passes"] == 1 + sum(hi - lo for _, lo, hi in CRITERES) == 38


def test_demi_point_non_lu_comme_entier():
    """« 2.5 » : le juge continue « 2 » par « . » ; v1 comptait « 2 » par son jeton de tête (score appuyé), v2 exige la
    fin de ligne après la valeur : la masse admise s'effondre, aucun score appuyé."""
    table = _table(espace={"0": -2.0, "1": -2.0, "2": 6.0, "3": -2.0, "4": -2.0, "5": -2.0, "-": -2.0},
                   apres={("2", "."): 8.0, ("2", "\n"): 0.0})
    texte = _bloc(brut={n: "2.5" for n, lo, hi in CRITERES if lo == 0})
    r = _lire(table, texte)
    assert r["score"] is None and "seuil d'appui" in r["motif"]
    assert r["criteres"]["COHERENCE"]["masse"] < 0.01 and r["criteres"]["COHERENCE"]["fin_de_ligne"]["2"] < 0.001
    v1 = nrj.lire_par_probabilite(BigrammeCache(table), TOK, CTX, _bloc(echelle=False, brut={"COHERENCE": "2.5"}),
                                  CRITERES, True, 0.5, TOK.pad_token_id)
    assert v1["criteres"]["COHERENCE"]["masse"] > 0.99                      # v1 : « 2 » de « 2.5 », jeton de tête
    sain = _table(espace={"0": -2.0, "1": -2.0, "2": 6.0, "3": -2.0, "4": -2.0, "5": -2.0, "-": -2.0})
    r = _lire(sain, _bloc(notes={n: 2 for n, lo, hi in CRITERES if lo == 0}), masse_min=0.0)
    assert r["criteres"]["COHERENCE"]["masse"] > 0.99                     # « 2 » suivi d'une fin de ligne : admis


def test_valeur_hors_echelle_et_dix_non_comptees():
    """« 4 » sur [0, 3] : hors des valeurs admises, masse sous le seuil. « 10 » sur [0, 5] : v1 lisait « 1 » par son jeton
    de tête ; v2 exige la fin de ligne après « 1 » : non compté."""
    hors = _table(espace={"0": -3.0, "1": -3.0, "2": -3.0, "3": -3.0, "4": 7.0, "5": -3.0, "-": -3.0})
    r = _lire(hors, _bloc(notes={"BALANCE": 4}))
    assert r["score"] is None and r["criteres"]["BALANCE"]["masse"] < 0.01
    assert r["criteres"]["SPECIFICITY"]["masse"] > 0.9                      # 4 est admis sur [0, 5]
    dix = _table(espace={"0": -3.0, "1": 7.0, "2": -3.0, "3": -3.0, "4": -3.0, "5": -3.0, "-": -3.0},
                 apres={("1", "0"): 9.0, ("1", "\n"): 0.0})
    texte = _bloc(brut={"SPECIFICITY": "10"})
    r = _lire(dix, texte)
    assert r["score"] is None and r["criteres"]["SPECIFICITY"]["masse"] < 0.01
    v1 = nrj.lire_par_probabilite(BigrammeCache(dix), TOK, CTX, _bloc(echelle=False, brut={"SPECIFICITY": "10"}),
                                  CRITERES, True, 0.5, TOK.pad_token_id)
    assert v1["criteres"]["SPECIFICITY"]["masse"] > 0.99


def test_espace_non_ecrite_comptee():
    """La probabilité des jetons communs à toutes les valeurs (l'espace après les deux-points) est comptée : un juge qui
    écrit autre chose après les deux-points (« ** », par exemple) n'a pas de score appuyé ; v1 lisait la loi des
    chiffres conditionnelle à une espace forcée."""
    table = _table(deux_points=-4.0)
    table[_i(":"), _i("*")] = 6.0
    r = _lire(table, _bloc(brut={"SPECIFICITY": "**3**"}))
    assert r["score"] is None and all(lu["masse"] < 0.01 for lu in r["criteres"].values())
    lu = r["criteres"]["SPECIFICITY"]
    assert lu["position"] == len(CTX) + COMPLET.index(": ") + 2           # décision au caractère « * » écrit
    assert _lire(table, masse_min=0.0)["score_sans_appui"] == pytest.approx(r["score_sans_appui"])


def test_fenetre_incomplete_critere_absent_valeur_absente_jamais_imputes():
    table = _table()
    r = _lire(table, COMPLET, complete=False)
    assert r["score"] is None and "fenêtre incomplète" in r["motif"] and r["passes"] == 0
    r = _lire(table, COMPLET.replace("NOVELTY (0 to 4): 2\n", ""))
    assert r["score"] is None and r["motif"] == "critère absent : NOVELTY" and r["passes"] == 0
    r = _lire(table, COMPLET.replace("RIGOR (0 to 4): 3", "RIGOR (0 to 4):"))
    assert r["score"] is None and r["motif"] == "valeur absente après le critère : RIGOR"


def test_forme_v1_lue_comme_la_forme_a_echelle():
    table = _table()
    a, b = _lire(table), _lire(table, _bloc(echelle=False))
    assert a["score"] == pytest.approx(b["score"]) and a["passes"] == b["passes"]
    assert all(a["criteres"][n]["masse"] == pytest.approx(b["criteres"][n]["masse"]) for n in NOTES)


def _reference_par_passes_completes(modele, tok, contexte, texte, terminaux):
    """Référence : pour chaque valeur, une passe complète sur contexte + bloc jusqu'au jeton de décision + suite de la
    valeur ; aucune réutilisation de cache."""
    car = nrj2.positions_des_valeurs_v2(texte, CRITERES)
    ids_rep, offs = nrj._encoder(tok, texte)
    sortie = {}
    for nom, lo, hi in CRITERES:
        k, prefixe = nrj.jeton_de_decision(texte, offs, car[nom])
        base = list(contexte) + ids_rep[:k]
        p = {}
        for v, c in nrj.candidats_de_valeur(tok, prefixe, lo, hi).items():
            with torch.no_grad():
                lg = modele(input_ids=torch.tensor([base + c]), use_cache=False).logits[0]
            lp = torch.log_softmax(lg.float(), -1)
            s = sum(float(lp[len(base) - 1 + t, c[t]]) for t in range(len(c)))
            p[v] = math.exp(s + float(torch.logsumexp(lp[len(base) - 1 + len(c), terminaux], 0)))
        sortie[nom] = p
    return sortie


def test_lecture_par_cache_egale_aux_passes_completes():
    """Modèle jouet de type Llama (vrai cache des clés et valeurs, rognage et prolongement) : la lecture v2 égale la
    référence par passes complètes, valeur par valeur, à 1e-4 près."""
    m = modele_jouet(11, len(TOK), couches=2, largeur=32, tetes=4, tetes_cle_valeur=2, intermediaire=64)
    texte = _bloc(brut={"COHERENCE": "2.5", "RIGOR": "**3**"})
    r = nrj2.lire_par_probabilite_v2(m, TOK, CTX, texte, CRITERES, True, 0.0, TERM)
    ref = _reference_par_passes_completes(m, TOK, CTX, texte, TERM)
    for nom, p in ref.items():
        lu = r["criteres"][nom]
        assert math.isclose(lu["masse"], sum(p.values()), rel_tol=1e-4)
        assert all(math.isclose(lu["probabilites"][str(v)], x / sum(p.values()), rel_tol=1e-4, abs_tol=1e-7)
                   for v, x in p.items())


def test_gardes_du_cache_cas_sain_et_artefacts():
    """Modèle sans cache : arrêt (aucun repli sur des passes complètes) ; rognage au-delà de la longueur, prolongement
    d'un cache d'une autre longueur : arrêt."""
    with pytest.raises(GardeArret, match="cache des clés et valeurs absent"):
        _lire(_table(), modele=SansCache)
    c = FauxCache(10)
    nrj2.rogner(c, 7)
    assert c.get_seq_length() == 7
    nrj2.rogner(c, 7)                                                       # même longueur : rien à rogner
    with pytest.raises(GardeArret, match="rognage à 8 impossible"):
        nrj2.rogner(c, 8)
    with pytest.raises(GardeArret, match="rognage à 0 impossible"):
        nrj2.rogner(c, 0)
    with pytest.raises(GardeArret, match="prolongement"):
        nrj2.prolonger(BigrammeCache(_table()), FauxCache(5), [1, 2], 4)
    lignes, c2 = nrj2.prolonger(BigrammeCache(_table()), FauxCache(4), [_i("2")], 4)
    assert c2.get_seq_length() == 5 and len(lignes) == 1
    with pytest.raises(GardeArret, match="sans jeton terminal"):
        nrj2.lire_par_probabilite_v2(BigrammeCache(_table()), TOK, CTX, COMPLET, CRITERES, True, 0.5, [])


# ---------------------------------------------------------------- jetons terminaux et garde d'encodage

class TokSansSaut:
    """Vocabulaire sans aucun jeton de fin de ligne (artefact)."""

    def __len__(self):
        return 3

    def batch_decode(self, lots, **_):
        return [["a", "b", " "][x[0]] for x in lots]


def test_jetons_terminaux_cas_sain_et_artefact():
    fins = FMT.fins
    t = nrj2.jetons_terminaux(TOK, fins)
    assert t == sorted({NL} | set(fins))
    llama = _tokeniseur_a_la_llama_3(rogner=False)
    tl = nrj2.jetons_terminaux(llama, set())
    assert llama.convert_tokens_to_ids("Ċ") in tl and all(set(llama.decode([i])) & {"\n", "\r"} for i in tl)
    with pytest.raises(GardeArret, match="aucun jeton de fin de ligne"):
        nrj2.jetons_terminaux(TokSansSaut(), set())
    assert nrj2.resume_terminaux(t) == nrj2.resume_terminaux(list(reversed(t)))


class TokCaracteres(TokFusion):
    """Un caractère par jeton (ceux de TOK), sans fusion ; `_apres` transforme la suite (artefacts ci-dessous)."""
    EN_PLUS = TokFusion.FUSION + 1

    def _decouper(self, s):
        return self._apres(s, [_i(c) for c in s], [(k, k + 1) for k in range(len(s))])

    def _apres(self, s, ids, offs):
        return ids, offs


class TokChiffreSaut(TokCaracteres):
    """« 3\\n » fondu en un seul jeton (artefact) : la valeur en contexte n'est plus la valeur à part."""

    def _apres(self, s, ids, offs):
        i, o, k = [], [], 0
        while k < len(ids):
            if k + 1 < len(ids) and ids[k] == _i("3") and ids[k + 1] == NL:
                i.append(self.EN_PLUS), o.append((offs[k][0], offs[k + 1][1]))
                k += 2
            else:
                i.append(ids[k]), o.append(offs[k])
                k += 1
        return i, o


class TokSautDouble(TokCaracteres):
    """Après un chiffre, « \\n » encodé en deux jetons (le saut, puis un jeton sans largeur) : la valeur est suivie
    d'un jeton terminal, mais pas d'un seul (artefact)."""

    def _apres(self, s, ids, offs):
        i, o = [], []
        for k, (x, off) in enumerate(zip(ids, offs)):
            i.append(x), o.append(off)
            if x == NL and k > 0 and s[k - 1].isdigit():
                i.append(self.EN_PLUS), o.append((off[1], off[1]))
        return i, o


def test_garde_d_encodage_v2_cas_sain_et_artefacts():
    sain = nrj2.controler_encodage_v2(TOK, "jouet", nrj2.jetons_terminaux(TOK, FMT.fins))
    assert sain["valeurs_controlees"] == 47 and sain["valeurs_controlees_v2"] == 94
    llama = _tokeniseur_a_la_llama_3(rogner=False)
    e = nrj2.controler_encodage_v2(llama, "reel", nrj2.jetons_terminaux(llama, set()))
    assert e["valeurs_controlees_v2"] == 94
    with pytest.raises(GardeArret, match="un seul jeton terminal"):            # « \n » en deux jetons
        nrj2.controler_encodage_v2(TokSautDouble(), "jouet", TERM)
    with pytest.raises(GardeArret, match="encodage de « SPECIFICITY: 3 »"):    # « 3\n » fondu : garde de v1
        nrj2.controler_encodage_v2(TokChiffreSaut(), "jouet", TERM)
    assert nrj2.controler_encodage_v2(TokCaracteres(), "jouet", TERM)["valeurs_controlees_v2"] == 94
    with pytest.raises(GardeArret, match="un seul jeton, terminal"):           # « \n » hors des terminaux
        nrj2.controler_encodage_v2(TOK, "jouet", [TOK.eos_token_id])
    with pytest.raises(GardeArret, match="aucun jeton terminal"):
        nrj2.controler_encodage_v2(TOK, "jouet", [])
    with pytest.raises(GardeArret, match="encodage de 'X: -1'"):               # garde de v1, toujours là
        nrj2.controler_encodage_v2(TokFusion(), "jouet", TERM)


# ---------------------------------------------------------------- génération bornée au bloc

def test_generer_lot_borne_egal_a_generer_lot_sans_arret():
    m = modele_jouet(5, len(TOK), couches=2, largeur=32, tetes=4, tetes_cle_valeur=2, intermediaire=64)
    contextes = [TOK.encode(s, add_special_tokens=False) for s in ("abc", "SPECIFICITY", "x")]
    fins = {TOK.eos_token_id}
    a, _ = generer_lot(m, contextes, 24, 1.0, [3, 4, 5], fins, TOK.pad_token_id)
    b, arrets = nrj2.generer_lot_borne(m, contextes, 24, 1.0, [3, 4, 5], fins, TOK.pad_token_id, {NL},
                                       lambda jetons: False)
    assert a == b and all(x in ("budget", "fin") for x in arrets)
    # arrêt à la première fin de ligne : chaque ligne est le début de sa ligne sans arrêt, mêmes tirages
    c, arrets = nrj2.generer_lot_borne(m, contextes, 24, 1.0, [3, 4, 5], fins, TOK.pad_token_id,
                                       set(range(len(TOK))), lambda jetons: True)
    assert all(len(x) == 1 and x == y[:1] for x, y in zip(c, a)) and set(arrets) <= {"bloc clos", "fin"}
    with pytest.raises(GardeArret, match="max_nouveaux"):
        nrj2.generer_lot_borne(m, contextes, 0, 1.0, [3, 4, 5], fins, TOK.pad_token_id, {NL}, lambda j: False)


def test_generer_lot_borne_s_arrete_au_bloc_clos():
    """Juge simulé déterministe qui répète le bloc : la ligne s'arrête au saut de ligne qui clôt le dixième critère
    (cause « bloc clos »), sans arrêt elle va au budget."""
    texte = COMPLET + "\n" + COMPLET
    ids = TOK.encode(texte, add_special_tokens=False)
    pos = {}

    class Script(torch.nn.Module):
        """Rend le jeton suivant du texte, selon la position (modèle simulé, sans aléa)."""

        def __init__(self):
            super().__init__()
            self.p = torch.nn.Parameter(torch.zeros(1), requires_grad=False)

        def forward(self, input_ids, position_ids=None, past_key_values=None, use_cache=False, **_):
            k = position_ids[0, -1].item() - pos["debut"] + 1
            lg = torch.full((1, 1, len(TOK)), -30.0)
            lg[0, 0, ids[k] if k < len(ids) else NL] = 30.0
            return SimpleNamespace(logits=lg, past_key_values=FauxCache(0))

    ctx = TOK.encode("Q", add_special_tokens=False)
    pos["debut"] = len(ctx)
    sauts = nrj2.jetons_de_saut(TOK)
    assert NL in sauts
    out, arrets = nrj2.generer_lot_borne(Script(), [ctx], 600, 1.0, [1], {TOK.eos_token_id}, TOK.pad_token_id, sauts,
                                         lambda j: nrj2.bloc_clos(TOK.decode(j), CRITERES))
    assert TOK.decode(out[0]) == COMPLET + "\n" and arrets == ["bloc clos"]
    out, arrets = nrj2.generer_lot_borne(Script(), [ctx], 64, 1.0, [1], {TOK.eos_token_id}, TOK.pad_token_id, sauts,
                                         lambda j: False)
    assert len(out[0]) == 64 and arrets == ["budget"]


# ---------------------------------------------------------------- chaîne jouet

def _phases(duree=300, juges=("jouet-8B", "jouet-3B")):
    return [{"juge": j, "variante": nrj2.VARIANTE, "duree_max_s": duree} for j in juges]


def _config(**changes):
    c = _config_notations()
    return {**{k: c[k] for k in nrj.CLES_EGALES_AUX_NOTATIONS}, "mode": "jouet", "run_notations": NOTATIONS,
            "phases": _phases(), "juge_decisif": "jouet-8B", "max_nouveaux_verdict": 64, "masse_min_appui": 0.0,
            "duree_globale_s": 1800, **changes}


def _fichiers(depot, run):
    return sorted(p.name for p in (depot / "diag" / run).glob("*.json"))


@pytest.mark.parametrize("changement, motif", [
    ({"phases": [{"juge": "jouet-8B", "variante": "verdict-d-abord", "duree_max_s": 9}]}, "variante 'verdict-d-abord'"),
    ({"phases": _phases()[::-1]}, "juge_decisif"),
    ({"juge_decisif": "jouet-9B"}, "juge_decisif"),
    ({"phases": _phases()[:1] * 2}, "phase en double"),
    ({"phases": [{"juge": "jouet-9B", "variante": nrj2.VARIANTE, "duree_max_s": 9}]}, "juge 'jouet-9B' inconnu"),
    ({"phases": _phases(duree=1801)}, "hors de"),
    ({"max_nouveaux_verdict": 32}, "max_nouveaux_verdict"),
    ({"masse_min_appui": 1.5}, "masse_min_appui"),
    ({"mode": "reel"}, "masse_min_appui 0.0 ≠ 0.5 au réel"),
    ({"duree_globale_s": 3601}, "duree_globale_s"),
    ({"variante_juge": "b*"}, "b0"),
    ({"max_nouveaux_suite": 8}, "clés inconnues"),
    ({"lot_juge": 0}, "lot_juge"),
])
def test_gardes_de_configuration_cas_sain_et_artefacts(changement, motif):
    with pytest.raises(GardeArret, match=motif):
        nrj2.exiger_config_rejeu_v2(_config(**changement))
    nrj2.exiger_config_rejeu_v2(_config())                                    # cas sain
    nrj2.exiger_config_rejeu_v2(_config(mode="reel", masse_min_appui=0.5))


def test_config_incomplete_reel_sans_fiche_ni_echeance(depot):
    with pytest.raises(GardeArret, match="incomplète"):
        nrj2.executer({k: v for k, v in _config().items() if k != "juge_decisif"}, depot, "20261029-110007-x", None,
                      "t.json")
    reel = _config(mode="reel", masse_min_appui=0.5)
    with pytest.raises(GardeArret, match="R1"):
        nrj2.executer(reel, depot, "20261029-110008-x", None, "t.json")
    with pytest.raises(GardeArret, match="sans échéance externe"):
        nrj2.executer(reel, depot, "20261029-110008-x", "prereg/fiche.md", "t.json")
    assert not (depot / "runs").exists()


def test_bout_en_bout_deux_juges_et_lecture(depot, monkeypatch, capsys):
    f = _notations_artisanales(depot, monkeypatch)
    capsys.readouterr()
    run = "20261029-110000-rejeu-v2-jouet"
    resume = nrj2.executer(_config(), depot, run, None, str(f), autoriser_depot_sale=True)
    assert [(p["juge"], p["statut"], p["decisive"]) for p in resume["phases"]] == [
        ("jouet-8B", "écrit", True), ("jouet-3B", "écrit", False)]
    assert resume["consigne_verdict_sha256"] == nrj2.EMPREINTE_CONSIGNE_V2 and resume["juge_decisif"] == "jouet-8B"
    assert {j: (e["valeurs_controlees"], e["valeurs_controlees_v2"]) for j, e in resume["encodage"].items()} == {
        "jouet-8B": (47, 94), "jouet-3B": (47, 94)}
    assert _fichiers(depot, run) == sorted([f"rejeu-jouet-{j}-{nrj2.VARIANTE}.json" for j in ("8B", "3B")]
                                           + ["resume.json"])
    assert _fichiers(depot, NOTATIONS) == ["notations-jouet-3B-decisives.json", "notations-jouet-8B-decisives.json",
                                           "resume.json"]                    # rien d'écrit chez les notations rejouées
    for j in ("jouet-8B", "jouet-3B"):
        r = verifier_resultat(depot, depot / "diag" / run / f"rejeu-{j}-{nrj2.VARIANTE}.json")["resultat"]
        assert len(r["notations"]) == 4 and r["consigne_verdict_sha256"] == nrj2.EMPREINTE_CONSIGNE_V2
        assert all(x["jetons_reponse"] <= 64 and x["arret_generation"] in ("fin", "bloc clos", "budget")
                   for x in r["notations"])
        assert sum(r["descriptifs"]["arrets_generation"].values()) == 4
    m = json.loads((depot / "runs" / run / "manifeste.json").read_text())
    mp = json.loads((depot / "runs" / PILOTE / "manifeste.json").read_text())
    assert {g["entropie"] for g in m["graines"].values()} == {next(iter(mp["graines"].values()))["entropie"]}
    assert sum(k.startswith(f"rejeu-v2/{nrj2.VARIANTE}/") for k in m["graines"]) == 8
    err = capsys.readouterr().err
    lignes = [x for x in err.splitlines() if x.startswith("PROGRES ")]
    assert lignes and "SPECIFICITY" not in err
    lecture = nrj2.lire_rejeu_v2(depot, run)
    assert lecture["source"] == "resume" and lecture["juge_decisif"] == "jouet-8B"
    c8, c3 = lecture["cellules"][f"jouet-8B/{nrj2.VARIANTE}"], lecture["cellules"][f"jouet-3B/{nrj2.VARIANTE}"]
    assert c8["role"] == "décisive" and c3["role"].startswith("descriptive")
    assert lecture["lecture_decisive"] == c8["lecture"] and c8["n"] == 4 and c8["textes"] == 2


# réponses simulées, par clé de notation : bloc complet à échelles ; demi-point ; préambule puis forme v1 ; bloc inachevé
SIMULEES = {"2506.00001v1/e0/passe-0": COMPLET + "\nJustification.",
            "2506.00001v1/e0/passe-1": _bloc(brut={"COHERENCE": "2.5"}),
            "2506.00002v1/e0/passe-0": "Scores:\n" + _bloc(echelle=False) + "\n",
            "2506.00002v1/e0/passe-1": "SPECIFICITY (0 to 5): 3\nCOHERENCE"}


def test_bout_en_bout_generation_simulee_lecture_par_le_cache(depot, monkeypatch):
    """Génération simulée (textes écrits, rendus en jetons) ; lecture par le modèle jouet et son vrai cache, dans la
    chaîne. Seuil d'appui nul (jouet) : les blocs complets ont un score lu ; le bloc inachevé n'en a pas."""
    f = _notations_artisanales(depot, monkeypatch)
    vus = []

    def simulee(modele, contextes, max_nouveaux, temperature, graines, fins, pad, declencheurs, arreter):
        sortie, arrets = [], []
        for _ in contextes:
            cle = cles.pop(0)
            ids = TOK.encode(SIMULEES[cle.split("/", 1)[1]], add_special_tokens=False)
            sortie.append(ids)
            arrets.append("bloc clos" if arreter(ids) else "budget")
            vus.append(cle)
        return sortie, arrets

    cles = []
    vrai = nrj2._verdict_echelles

    def verdict(modele, fmt, morceau, *a, **k):
        cles.extend(d["cle"] for d in morceau)
        return vrai(modele, fmt, morceau, *a, **k)

    monkeypatch.setattr(nrj2, "generer_lot_borne", simulee)
    monkeypatch.setattr(nrj2, "_verdict_echelles", verdict)
    run = "20261029-110001-rejeu-v2-jouet"
    nrj2.executer(_config(phases=_phases(juges=("jouet-8B",))), depot, run, None, str(f), autoriser_depot_sale=True)
    recs = verifier_resultat(depot, depot / "diag" / run / f"rejeu-jouet-8B-{nrj2.VARIANTE}.json")["resultat"]
    n = {r["cle"].split("/", 1)[1]: r for r in recs["notations"]}
    assert len(vus) == 4
    complet = n["2506.00001v1/e0/passe-0"]
    assert complet["bloc_complet"] and complet["proba"]["score"] is not None and complet["ecrit"]["notes"] == NOTES
    assert complet["ecrit"]["lignes_a_echelle"] == 10 and complet["proba"]["passes"] == 38
    demi = n["2506.00001v1/e0/passe-1"]
    assert demi["ecrit"]["score"] is None and demi["proba"]["score"] is not None       # seuil nul (jouet)
    assert "COHERENCE : valeur non admise ('2.5')" in demi["ecrit"]["anomalies"]
    v1 = n["2506.00002v1/e0/passe-0"]
    assert v1["ecrit"]["notes"] == NOTES and v1["ecrit"]["lignes_a_echelle"] == 0 and v1["arret_generation"] == "bloc clos"
    inacheve = n["2506.00002v1/e0/passe-1"]
    assert not inacheve["bloc_complet"] and inacheve["proba"]["motif"].startswith("fenêtre incomplète")
    c = nrj2.lire_rejeu_v2(depot, run)["cellules"][f"jouet-8B/{nrj2.VARIANTE}"]
    assert (c["n"], c["finis"], c["finis_ecrits"]) == (4, 3, 2) and c["lignes_a_echelle"] == 20
    assert c["arrets_generation"] == {"fin": 0, "bloc clos": 2, "budget": 2}


def test_echeance_de_phase_le_suivant_continue_et_r12(depot, monkeypatch):
    f = _notations_artisanales(depot, monkeypatch)
    run = "20261029-110002-rejeu-v2-jouet"
    phases = [{"juge": "jouet-8B", "variante": nrj2.VARIANTE, "duree_max_s": 1e-9},
              {"juge": "jouet-3B", "variante": nrj2.VARIANTE, "duree_max_s": 300}]
    resume = nrj2.executer(_config(phases=phases), depot, run, None, str(f), autoriser_depot_sale=True)
    assert [(p["statut"], p["lots_faits"]) for p in resume["phases"]] == [("échu", 0), ("écrit", 2)]
    assert _fichiers(depot, run) == [f"rejeu-jouet-3B-{nrj2.VARIANTE}.json", "resume.json"]          # tout ou rien
    lecture = nrj2.lire_rejeu_v2(depot, run)
    assert lecture["cellules"][f"jouet-8B/{nrj2.VARIANTE}"] == {"lecture": "non mesurée", "statut": "échu",
                                                                  "role": "décisive"}
    assert lecture["lecture_decisive"] == "non mesurée"
    with pytest.raises(GardeArret, match="R12"):
        nrj2.executer(_config(phases=phases), depot, run, None, str(f), autoriser_depot_sale=True)
    from controle_ia.manifeste import ecrire_resultat
    chemin_m = depot / "runs" / run / "manifeste.json"
    ecrire_resultat(depot, chemin_m, "lecture-rejeu-v2", lecture)
    with pytest.raises(GardeArret, match="R12"):
        ecrire_resultat(depot, chemin_m, "lecture-rejeu-v2", lecture)


def test_echeance_globale_et_externe_aucune_phase_ne_commence(depot, monkeypatch):
    f = _notations_artisanales(depot, monkeypatch)
    run = "20261029-110003-rejeu-v2-jouet"
    resume = nrj2.executer(_config(phases=_phases(duree=0.5), duree_globale_s=0.5), depot, run, None, str(f),
                           autoriser_depot_sale=True)
    assert {p["statut"] for p in resume["phases"]} == {"non-commencé"}
    assert _fichiers(depot, run) == ["resume.json"]
    run = "20261029-110004-rejeu-v2-jouet"
    resume = nrj2.executer(_config(), depot, run, None, str(f), autoriser_depot_sale=True,
                           echeance_externe=time.time() + 60)
    assert [p["statut"] for p in resume["phases"]] == ["non-commencé"] * 2
    assert resume["echeance"]["source"] == "externe" and 40 < resume["echeance"]["retenue_s"] <= 60
    with pytest.raises(GardeArret, match="déjà passée"):
        nrj2.executer(_config(), depot, "20261029-110005-x", None, str(f), autoriser_depot_sale=True,
                      echeance_externe=time.time() - 1)
    assert not (depot / "runs" / "20261029-110005-x").exists()


def test_signal_term_consigne_et_propage_puis_lecture(depot, monkeypatch):
    f = _notations_artisanales(depot, monkeypatch)
    vrai = nrj2._verdict_echelles

    def verdict(*a, **k):
        sortie = vrai(*a, **k)
        gardes.SIGNAL_TERM_RECU.append(15)           # signal avalé par une bibliothèque : drapeau seul
        return sortie

    monkeypatch.setattr(nrj2, "_verdict_echelles", verdict)
    run = "20261029-110006-rejeu-v2-jouet"
    with pytest.raises(GardeArret, match="signal TERM"):
        nrj2.executer(_config(), depot, run, None, str(f), autoriser_depot_sale=True)
    assert _fichiers(depot, run) == ["arret.json"]
    r = verifier_resultat(depot, depot / "diag" / run / "arret.json")["resultat"]
    assert r["etape"] == f"{nrj2.VARIANTE} par jouet-8B" and r["partiel"]["phases"][0]["lots_faits"] == 1
    c = nrj2.lire_rejeu_v2(depot, run)["cellules"]
    assert c[f"jouet-8B/{nrj2.VARIANTE}"] == {"lecture": "non mesurée (arrêt)", "statut": "arrêt pendant la phase",
                                              "role": "décisive"}
    assert c[f"jouet-3B/{nrj2.VARIANTE}"]["statut"] == "non atteinte"


def test_encodage_different_arrete_avant_toute_phase(depot, monkeypatch):
    f = _notations_artisanales(depot, monkeypatch)
    monkeypatch.setattr(nrj2, "jetons_terminaux", lambda tok, fins: [TOK.eos_token_id])
    run = "20261029-110009-rejeu-v2-jouet"
    with pytest.raises(GardeArret, match="un seul jeton, terminal"):
        nrj2.executer(_config(), depot, run, None, str(f), autoriser_depot_sale=True)
    r = verifier_resultat(depot, depot / "diag" / run / "arret.json")["resultat"]
    assert r["etape"] == "contrôle de l'encodage des valeurs" and r["partiel"]["phases"] == []


def test_memes_notations_que_v1_garde_d_alignement(depot, monkeypatch):
    """Mêmes 180 notations : la garde d'alignement de v1 (clé, empreinte de l'ensemble, nombre, lecture écrite refaite)
    s'applique ; une notation rejouée retirée arrête avant le manifeste."""
    f = _notations_artisanales(depot, monkeypatch)
    chemin = depot / "diag" / NOTATIONS / "notations-jouet-8B-decisives.json"
    _reecrire(chemin, lambda c: c["resultat"]["notations"].pop())
    with pytest.raises(GardeArret, match="3 notations rejouées, 4 attendues"):
        nrj2.executer(_config(), depot, "20261029-110010-x", None, str(f), autoriser_depot_sale=True)
    assert not (depot / "runs" / "20261029-110010-x").exists()


def _fiche(depot, config, f, entropie, commit, nom="fiche.md", remplacements=None, en_plus=()):
    (depot / "prereg").mkdir(exist_ok=True)
    p = depot / "prereg" / nom
    d = depot / "diag"
    valeurs = {"Commit du code d'analyse": commit,
               "Configuration du rejeu (empreinte canonique)": lp.empreinte_config(config),
               "Run du pilote rejoué": PILOTE, "Run des notations rejouées": NOTATIONS,
               "Manifeste des notations rejouées": empreinte(depot / "runs" / NOTATIONS / "manifeste.json"),
               "Notations rejouées du jouet-8B": empreinte(d / NOTATIONS / "notations-jouet-8B-decisives.json"),
               "Notations rejouées du jouet-3B": empreinte(d / NOTATIONS / "notations-jouet-3B-decisives.json"),
               "Épisodes du pilote rejoué": empreinte(d / PILOTE / "episodes.json"),
               "Consigne du verdict d'abord à échelles": nrj2.EMPREINTE_CONSIGNE_V2, "Tâches du pilote": empreinte(f),
               "Entropie": entropie, **(remplacements or {})}
    lignes = [f"- {k} : `{v}`" for k, v in valeurs.items() if v is not None] + list(en_plus)
    corps = ["# Fiche de test", "", *lignes, ""]
    for s in ("Hypothèse", "Prédiction chiffrée et signe attendu", "Métrique", "Seuil", "Plan d'analyse",
              "Critères de lecture gelés", "Liste d'arrêt"):
        corps += [f"## {s}", "", f"contenu {s}", ""]
    corps += ["## Contre-lecture", "", f"brouillon relu `{'a' * 64}`, rapport `{'b' * 64}`", ""]
    p.write_text("\n".join(corps), encoding="utf-8")
    sceller(p)
    return p


def test_gardes_de_citation_cas_sain_et_artefacts(depot, monkeypatch):
    f = _notations_artisanales(depot, monkeypatch)
    monkeypatch.setattr(nrj2, "exiger_code_importe_sous", lambda racine: None)
    commit = subprocess.run(["git", "-C", str(depot), "rev-parse", "HEAD"], capture_output=True, text=True,
                            check=True).stdout.strip()
    mp = json.loads((depot / "runs" / PILOTE / "manifeste.json").read_text())
    entropie = int(next(iter(mp["graines"].values()))["entropie"])
    c = _config(phases=_phases(duree=300, juges=("jouet-8B",)))
    sain = _fiche(depot, c, f, entropie, commit)
    cas = [(_fiche(depot, _config(), f, entropie, commit, "f-config.md"), "configuration"),
           (_fiche(depot, c, f, entropie + 1, commit, "f-entropie.md"), "entropie citée ≠ celle du pilote"),
           (_fiche(depot, c, f, entropie, commit, "f-consigne-v1.md",
                   remplacements={"Consigne du verdict d'abord à échelles": nrj.EMPREINTE_CONSIGNE}), "consigne"),
           (_fiche(depot, c, f, entropie, commit, "f-sans-consigne.md",
                   remplacements={"Consigne du verdict d'abord à échelles": None},
                   en_plus=(f"- Consigne du verdict d'abord : `{nrj2.EMPREINTE_CONSIGNE_V2}`",)), "consigne cité 0 fois"),
           (_fiche(depot, c, f, entropie, commit, "f-notations.md",
                   remplacements={"Notations rejouées du jouet-3B": "1" * 64}), "notations rejouées du jouet-3B"),
           (_fiche(depot, c, f, entropie, commit, "f-double.md",
                   en_plus=(f"- Run des notations rejouées : `{NOTATIONS}`",)), "cité 2 fois"),
           (_fiche(depot, c, f, entropie, commit, "f-taches.md", remplacements={"Tâches du pilote": "3" * 64}),
            "tâches")]
    committer(depot)
    for p, motif in cas:
        with pytest.raises(GardeArret, match=motif):
            nrj2.executer(c, depot, "20261029-110011-rejeu-v2-jouet", str(p), str(f))
        assert not (depot / "runs" / "20261029-110011-rejeu-v2-jouet").exists()
    resume = nrj2.executer(c, depot, "20261029-110012-rejeu-v2-jouet", str(sain), str(f), autoriser_depot_sale=True)
    assert resume["commit_cite"] == commit
    m = json.loads((depot / "runs" / "20261029-110012-rejeu-v2-jouet" / "manifeste.json").read_text())
    assert m["decisif"] and m["preenregistrement"]["chemin"] == "prereg/fiche.md"
    assert m["commande"] == nrj2.COMMANDE


def test_fonctions_de_v1_importees_sans_copie():
    """v2 importe de v1 tout ce qui ne change pas (R12 : v1 n'est pas modifié)."""
    for nom in ("candidats_de_valeur", "jeton_de_decision", "loi_renormalisee", "controler_encodage",
                "exiger_alignement", "charger_notations_rejouees", "exiger_egal_aux_notations", "lire_cellule",
                "_contexte_b0", "_derouler", "_non_mesuree"):
        assert getattr(nrj2, nom) is getattr(nrj, nom)
    assert nrj2.CITATIONS_V2["tâches"] is nrj.CITATIONS["tâches"]
    assert Path(nrj.__file__).name == "noter_rejeu_juges_v1.py"


# ---------------------------------------------------------------- contre-lecture R2 (CLR2-08) : gardes sans artefact
# Cinq essais du contre-lecteur (`outils/test_gardes_complementaires_v2.py` de la contre-lecture R2), versés tels quels,
# noms locaux au lieu du module importé.

class CacheMenteur(BigrammeCache):
    """Rend un cache d'une longueur fausse (un de plus)."""

    def forward(self, *a, **k):
        s = super().forward(*a, **k)
        if s.past_key_values is not None:
            s.past_key_values.n += 1
        return s


class LignesEnMoins(BigrammeCache):
    """Rend une ligne de logits de moins que demandé."""

    def forward(self, *a, **k):
        s = super().forward(*a, **k)
        return SimpleNamespace(logits=s.logits[:, :-1], past_key_values=s.past_key_values)


def test_passe_principale_cache_de_longueur_fausse_et_lignes_manquantes():
    _lire(_table())                                                     # cas sain
    with pytest.raises(GardeArret, match="longueur ≠ la suite"):
        _lire(_table(), modele=CacheMenteur)
    with pytest.raises(GardeArret, match="lignes rendues|demandées"):
        _lire(_table(), modele=LignesEnMoins)


def test_prolongement_longueur_rendue_fausse():
    nrj2.prolonger(BigrammeCache(_table()), FauxCache(4), [_i("2")], 4)                        # cas sain
    with pytest.raises(GardeArret, match="prolongement"):
        nrj2.prolonger(CacheMenteur(_table()), FauxCache(4), [_i("2")], 4)


def test_lecture_sans_contexte():
    with pytest.raises(GardeArret, match="sans contexte"):
        nrj2.lire_par_probabilite_v2(BigrammeCache(_table()), TOK, [], COMPLET, CRITERES, True, 0.5, TERM)


def test_generer_lot_borne_lot_vide_et_graines():
    m = BigrammeCache(_table())
    ctx = [TOK.encode("ab", add_special_tokens=False)]
    nrj2.generer_lot_borne(m, ctx, 2, 1.0, [1], {TOK.eos_token_id}, TOK.pad_token_id, {NL}, lambda j: False)
    for contextes, graines in (([], []), (ctx, [1, 2]), ([[]], [1])):
        with pytest.raises(GardeArret, match="lot vide"):
            nrj2.generer_lot_borne(m, contextes, 2, 1.0, graines, {TOK.eos_token_id}, TOK.pad_token_id,
                                   {NL}, lambda j: False)


def test_encodage_du_3b_recharge_different_arrete_avant_toute_phase(depot, monkeypatch):
    f = _notations_artisanales(depot, monkeypatch)
    vrai, appels = nrj2.controler_encodage_v2, []

    def change(tok, mode, terminaux, *a):
        sortie = dict(vrai(tok, mode, terminaux, *a))
        appels.append(1)
        if len(appels) > 2:                     # rechargement hors ligne du 3B : encodage différent (artefact)
            sortie["valeurs_controlees_v2"] = -1
        return sortie

    monkeypatch.setattr(nrj2, "controler_encodage_v2", change)
    run = "20261029-120000-rejeu-v2-jouet"
    with pytest.raises(GardeArret, match="encodage chargé hors ligne"):
        nrj2.executer(_config(), depot, run, None, str(f), autoriser_depot_sale=True)
    r = verifier_resultat(depot, depot / "diag" / run / "arret.json")["resultat"]
    assert r["partiel"]["phases"] == []


# ---------------------------------------------------------------- corrections de l'auteur après la contre-lecture R2

def test_3b_recharge_avec_les_fins_du_modele_cas_sain(depot, monkeypatch):
    """Au réel, le format du début du run (tokeniseur seul) ne porte que la fin du tokeniseur, celui du 3B chargé hors
    ligne porte aussi celles du modèle : ce n'est pas un encodage différent. Le run continue, et la lecture du 3B prend
    les terminaux du format qui génère (fins du modèle comprises), consignés. Le module relu (`cff3d90a`) arrêtait ici
    tout le run, phase décisive comprise (défaut trouvé par l'auteur pendant les corrections)."""
    f = _notations_artisanales(depot, monkeypatch)
    vrai = nrj2.charger_modele_et_format
    EN_PLUS = TOK.convert_tokens_to_ids("<s>")

    def charger(spec, mode, graine, hors_ligne=False):
        m, fmt = vrai(spec, mode, graine, hors_ligne=hors_ligne)
        if hors_ligne:
            fmt.fins = set(fmt.fins) | {EN_PLUS}            # fin du modèle en plus, comme `fins_du_modele` au réel
        return m, fmt

    monkeypatch.setattr(nrj2, "charger_modele_et_format", charger)
    run = "20261029-120001-rejeu-v2-jouet"
    resume = nrj2.executer(_config(), depot, run, None, str(f), autoriser_depot_sale=True)
    assert [p["statut"] for p in resume["phases"]] == ["écrit", "écrit"]
    t8 = verifier_resultat(depot, depot / "diag" / run / f"rejeu-jouet-8B-{nrj2.VARIANTE}.json")["resultat"]
    t3 = verifier_resultat(depot, depot / "diag" / run / f"rejeu-jouet-3B-{nrj2.VARIANTE}.json")["resultat"]
    assert t3["terminaux"]["n"] == t8["terminaux"]["n"] + 1
    assert resume["encodage"]["jouet-3B"]["terminaux"] == t3["terminaux"]


def test_controle_prealable_de_l_encodage_cas_sain_et_artefact(monkeypatch):
    """Contre-lecture R2, CLR2-06 : garde d'encodage sur les tokeniseurs seuls, avant les tests de l'instance."""
    sortie = nrj2.controle_prealable_encodage(_config())
    assert {j: e["valeurs_controlees_v2"] for j, e in sortie.items()} == {"jouet-8B": 94, "jouet-3B": 94}
    with pytest.raises(GardeArret, match="configuration du rejeu v2 incomplète"):
        nrj2.controle_prealable_encodage({k: v for k, v in _config().items() if k != "phases"})
    monkeypatch.setattr(nrj2, "jetons_terminaux", lambda tok, fins: [TOK.eos_token_id])
    with pytest.raises(GardeArret, match="un seul jeton, terminal"):
        nrj2.controle_prealable_encodage(_config())
