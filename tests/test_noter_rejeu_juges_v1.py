"""Rejeu des juges du pilote de T0.5 (GO-2026-10-28-16), mode jouet : lecture par la probabilité du jeton de verdict
(valeurs exactes sur un modèle à bigrammes), cas sain et artefacts (R5) — note tronquée, critère ou valeur absents,
verdict hors échelle sous le seuil d'appui, jamais imputés ; gardes d'avant le manifeste ; garde d'encodage ; échéances
de phase, globale et externe ; signal TERM ; refus d'écraser (R12) ; lecture gelée (complétude sur les textes, Wilson,
contrôle de l'instrument sur la probabilité brute, audit R4 symétrique, accord, cellule composée, lecture après un
arrêt). Les essais marqués « contre-lecture, CLJ-0k » échouent sur le module relu (commit 33bd7c91)."""
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
from controle_ia.environnements import noter_pilote_a as npa
from controle_ia.environnements import noter_rejeu_juges_v1 as nrj
from controle_ia.environnements import pilote_a as pa
from controle_ia.environnements.juges import probabilite_oui
from controle_ia.environnements.rubrique import CRITERES, points_max
from controle_ia.gardes import GardeArret
from controle_ia.manifeste import generateur, graines, verifier_resultat
from controle_ia.scellement import empreinte, sceller
from test_noter_pilote_a import PILOTE, _pilote_arrete
from test_noter_pilote_a import _config as _config_notations
from test_pilote_a import FMT, TOK

NOTATIONS = "20261012-110100-notations-jouet"
COMPLET = ("SPECIFICITY: 3\nCOHERENCE: 2\nCOVERAGE: 4\nFEASIBILITY: 1\nNOVELTY: 2\nRIGOR: 3\nBALANCE: 1\n"
           "RESULT_REASONING: 2\nREDUNDANCY_PENALTY: -1\nIRRELEVANCE_PENALTY: 0")
DEMI = COMPLET.replace("COHERENCE: 2", "COHERENCE: 2.5")
SANS_NOVELTY = COMPLET.replace("NOVELTY: 2\n", "")
# réponses des notations rejouées (jouet), par clé : complète ; demi-point ; complète mais tronquée ; critère absent
TEXTES = {"2506.00001v1/e0/passe-0": (COMPLET, False), "2506.00001v1/e0/passe-1": (DEMI, False),
          "2506.00002v1/e0/passe-0": (COMPLET, True), "2506.00002v1/e0/passe-1": (SANS_NOVELTY, False)}


# ---------------------------------------------------------------- modèle à bigrammes : valeurs exactes

class Bigramme(torch.nn.Module):
    """Logits du jeton suivant fonction du seul jeton courant : les lois lues se calculent à la main."""

    def __init__(self, table):
        super().__init__()
        self.table = torch.nn.Parameter(table, requires_grad=False)

    def forward(self, input_ids, attention_mask=None, position_ids=None, use_cache=False, logits_to_keep=0, **_):
        lg = self.table[input_ids.to("cpu")]
        if isinstance(logits_to_keep, int):
            lg = lg[:, -logits_to_keep:] if logits_to_keep else lg
        else:
            lg = lg[:, logits_to_keep.to("cpu")]
        return SimpleNamespace(logits=lg)


def _i(c):
    return TOK.convert_tokens_to_ids(c)


def _table(espace=None, moins=None):
    t = torch.full((len(TOK), len(TOK)), -8.0)
    for c, v in (espace or {"0": 3.0, "1": 1.0, "2": 1.0, "3": 2.0, "4": 1.0, "5": 0.0, "-": 2.0}).items():
        t[_i(" "), _i(c)] = v
    for c, v in (moins or {"1": 1.0, "2": 0.0}).items():
        t[_i("-"), _i(c)] = v
    return t


def _attendu(table, lo, hi):
    """Loi exacte d'une valeur lue après « : » (jeton espace), par la règle de la chaîne (signe puis chiffre)."""
    s, m = torch.softmax(table[_i(" ")], -1), torch.softmax(table[_i("-")], -1)
    p = {v: float(s[_i("-")] * m[_i(str(-v))]) if v < 0 else float(s[_i(str(v))]) for v in range(lo, hi + 1)}
    masse = sum(p.values())
    return {v: x / masse for v, x in p.items()}, masse


CTX = [int(x) for x in TOK.encode("contexte du juge", add_special_tokens=False)]


def _lire(table, texte=COMPLET, complete=True, masse_min=0.5):
    return nrj.lire_par_probabilite(Bigramme(table), TOK, CTX, texte, CRITERES, complete, masse_min, TOK.pad_token_id)


def test_lecture_exacte_une_position_par_critere_et_regle_de_la_chaine():
    table = _table()
    r = _lire(table)
    total = 0.0
    for nom, lo, hi in CRITERES:
        loi, masse = _attendu(table, lo, hi)
        lu = r["criteres"][nom]
        assert lu["probabilites"].keys() == {str(v) for v in loi}
        assert all(math.isclose(lu["probabilites"][str(v)], p, rel_tol=1e-5) for v, p in loi.items())
        assert math.isclose(lu["masse"], masse, rel_tol=1e-5)
        assert math.isclose(lu["esperance"], sum(v * p for v, p in loi.items()), rel_tol=1e-5)
        total += lu["esperance"]
        # une seule position de décision : celle du premier caractère de la valeur écrite après la dernière occurrence
        c0 = COMPLET.rindex(nom + ": ") + len(nom) + 2
        assert isinstance(lu["position"], int) and lu["position"] == len(CTX) + c0 and lu["prefixe"] == " "
    assert math.isclose(r["score"], 100 * max(0.0, total) / points_max(CRITERES), rel_tol=1e-6)
    assert r["score"] == r["score_sans_appui"] and r["motif"] is None
    # « IRRELEVANCE_PENALTY: 0 » observé : « -1 » et « -2 » se lisent sur une seule passe hors du chemin (nœud « - ») ;
    # « REDUNDANCY_PENALTY: -1 » observé : tout est sur le chemin
    assert r["passes"] == 2


def test_lecture_insensible_aux_autres_positions():
    """Aucune moyenne sur les jetons : changer la loi après des jetons qui ne précèdent aucune valeur ne change rien."""
    table = _table()
    autre = table.clone()
    for c in "SPECIFICITYCOHERENCE:\n":
        autre[_i(c)] = torch.randn(len(TOK), generator=torch.Generator().manual_seed(ord(c)))
    a, b = _lire(table), _lire(autre)
    assert a["score"] == b["score"] and a["criteres"] == b["criteres"]


def test_demi_point_lu_par_probabilite_note_ecrite_illisible():
    table = _table()
    r = _lire(table, DEMI)
    assert r["score"] == _lire(table)["score"]                       # la position « 2 » de « 2.5 » porte la même loi
    assert nrj.lecture_ecrite(DEMI, CRITERES, False)["score"] is None


def test_fenetre_incomplete_critere_absent_valeur_absente_jamais_imputes():
    table = _table()
    r = _lire(table, COMPLET, complete=False)
    assert r["score"] is None and r["score_sans_appui"] is None and "fenêtre incomplète" in r["motif"] and r["passes"] == 0
    r = _lire(table, SANS_NOVELTY)
    assert r["score"] is None and r["motif"] == "critère absent : NOVELTY" and r["passes"] == 0
    r = _lire(table, COMPLET.replace("RIGOR: 3", "RIGOR:"))
    assert r["score"] is None and r["motif"] == "valeur absente après le critère : RIGOR"


def test_verdict_hors_echelle_sous_le_seuil_d_appui():
    """Le juge tient pour « 7 » (hors de toute échelle) : la loi renormalisée reste finie, mais la masse des valeurs
    admises est sous le seuil : aucun score appuyé (motif consigné), le score sans appui reste descriptif."""
    table = _table(espace={"0": 0.0, "1": 0.0, "2": 0.0, "3": 0.0, "4": 0.0, "5": 0.0, "-": 0.0, "7": 9.0})
    r = _lire(table)
    assert r["score"] is None and r["score_sans_appui"] is not None and "seuil d'appui" in r["motif"]
    assert all(lu["masse"] < 0.01 for lu in r["criteres"].values())
    assert _lire(table, masse_min=0.0)["score"] == r["score_sans_appui"]            # seuil nul : même valeur


def test_derniere_occurrence_comme_la_lecture_ecrite_et_ex_aequo_vers_le_bas():
    """La position lue est celle de la dernière occurrence du critère (même règle que `rubrique.lire_notes`) ; deux
    valeurs également probables : la valeur la plus probable rendue est la plus petite (règle déclarée)."""
    texte = "SPECIFICITY: 5\nanalysis\n" + COMPLET
    table = _table(espace={"0": 0.0, "1": 0.0, "2": 4.0, "3": 4.0, "4": 0.0, "5": 0.0, "-": 0.0})
    r = _lire(table, texte, masse_min=0.0)
    assert r["criteres"]["SPECIFICITY"]["position"] == len(CTX) + texte.rindex("SPECIFICITY: ") + len("SPECIFICITY: ")
    assert nrj.lecture_ecrite(texte, CRITERES, False)["notes"]["SPECIFICITY"] == 3
    assert r["criteres"]["SPECIFICITY"]["argmax"] == 2 and r["criteres"]["RIGOR"]["argmax"] == 2


def test_budget_releve_refuse_une_reponse_non_tronquee():
    """Garde de la phase « budget relevé » : seule une réponse tronquée se prolonge (arrêt avant toute génération)."""
    d = {"cle": "juge-x/t/e0/passe-0", "questions": "Why?", "ensemble": "PROPOSAL 1: x", "classification": None}
    ctx, _ = nrj._contexte_b0(FMT, d)
    n = {"cle": d["cle"], "jetons_contexte": len(ctx), "tronquee": False, "reponse": COMPLET}
    with pytest.raises(GardeArret, match="non tronquée"):
        nrj._budget_releve(Bigramme(_table()), FMT, [(d, n)], {d["cle"]: 1}, _config(), TOK.pad_token_id)
    with pytest.raises(GardeArret, match="contexte"):
        nrj._budget_releve(Bigramme(_table()), FMT, [(d, {**n, "tronquee": True, "jetons_contexte": 1})],
                           {d["cle"]: 1}, _config(), TOK.pad_token_id)


def test_loi_etalee_mais_massive_reste_appuyee():
    """L'appui porte sur la masse des valeurs admises, non sur la plus probable : six valeurs également probables qui
    prennent ensemble plus de la moitié de la masse donnent un score appuyé (aucune n'atteint 0,5 à elle seule)."""
    table = _table(espace={"0": 5.0, "1": 5.0, "2": 5.0, "3": 5.0, "-": 5.0 + math.log(3)}, moins={"1": 5.0, "2": 5.0})
    r = _lire(table)
    assert r["score"] is not None and min(lu["masse"] for lu in r["criteres"].values()) > 0.5
    assert max(max(lu["probabilites"].values()) for lu in r["criteres"].values()) < 0.5


class TokFusion:
    """Tokeniseur jouet qui fond l'espace et le signe (« ␣- », un jeton, comme le tokeniseur de Llama 3) ; sinon un
    caractère par jeton (ceux de TOK)."""
    FUSION = len(TOK)

    def _decouper(self, s):
        ids, offs, i = [], [], 0
        while i < len(s):
            if s[i:i + 2] == " -":
                ids.append(self.FUSION), offs.append((i, i + 2))
                i += 2
            else:
                ids.append(_i(s[i])), offs.append((i, i + 1))
                i += 1
        return ids, offs

    def encode(self, s, add_special_tokens=False):
        return self._decouper(s)[0]

    def __call__(self, s, add_special_tokens=False, return_offsets_mapping=False):
        ids, offs = self._decouper(s)
        return {"input_ids": ids, "offset_mapping": offs}


def test_espace_et_signe_fondus_position_de_decision_apres_les_deux_points():
    """« 0 » s'écrit « ␣ », « 0 » et « -1 » s'écrit « ␣- », « 1 » : les valeurs d'une pénalité divergent dès le jeton qui
    suit les deux-points ; leurs probabilités se lisent par la règle de la chaîne depuis cette position (valeurs
    exactes), celles des critères positifs après l'espace."""
    F = TokFusion.FUSION
    t = torch.full((F + 1, F + 1), -8.0)
    t[_i(":"), _i(" ")], t[_i(":"), F] = 2.0, 1.0
    for c, v in {"0": 1.0, "1": 0.5, "2": 2.0, "3": 1.5, "4": 0.0, "5": 0.0}.items():
        t[_i(" "), _i(c)] = v
    t[F, _i("1")], t[F, _i("2")] = 1.0, 0.0
    tok = TokFusion()
    r = nrj.lire_par_probabilite(Bigramme(t), tok, CTX, COMPLET, CRITERES, True, 0.0, TOK.pad_token_id)
    s = {k: torch.softmax(t[k], -1) for k in (_i(":"), _i(" "), F)}
    for nom, signe in (("REDUNDANCY_PENALTY", "-1"), ("IRRELEVANCE_PENALTY", "0")):
        p = {0: float(s[_i(":")][_i(" ")] * s[_i(" ")][_i("0")]),
             -1: float(s[_i(":")][F] * s[F][_i("1")]), -2: float(s[_i(":")][F] * s[F][_i("2")])}
        lu = r["criteres"][nom]
        assert math.isclose(lu["masse"], sum(p.values()), rel_tol=1e-5)
        assert all(math.isclose(lu["probabilites"][str(v)], x / sum(p.values()), rel_tol=1e-5) for v, x in p.items())
        assert lu["suite_commune"] == 0
        assert lu["position"] == len(CTX) + len(tok.encode(COMPLET[:COMPLET.rindex(nom + ":") + len(nom) + 1]))
    lu = r["criteres"]["SPECIFICITY"]
    q = {v: float(s[_i(" ")][_i(str(v))]) for v in range(6)}
    assert lu["suite_commune"] == 1 and math.isclose(lu["masse"], sum(q.values()), rel_tol=1e-5)
    assert r["passes"] == 2                         # une passe principale, une passe groupée hors du chemin


class TokRogne(TokFusion):
    """Décalages rognés de leur espace de tête (post-traitement « trim_offsets ») : aucun jeton ne porte plus le
    caractère qui suit les deux-points."""

    def _decouper(self, s):
        ids, offs = super()._decouper(s)
        return ids, [(a + 1, b) if s[a] == " " and b - a > 1 else (a, b) for a, b in offs]


class TokAPart(TokFusion):
    """« ␣5 » encodé à part en un seul jeton, en deux dans le contexte : la suite d'une valeur ne suit plus le contexte."""
    SEULE = TokFusion.FUSION + 1

    def encode(self, s, add_special_tokens=False):
        return [self.SEULE] if s == " 5" else super().encode(s)


def test_garde_d_encodage_cas_sain_et_artefacts():
    """Garde d'encodage (contre-lecture, « ce que je n'ai pas pu vérifier ») : le découpage attendu de « X: -1 » et
    « X: 0 » (réel : espace et signe fondus ; jouet : un caractère par jeton) et la cohérence de chaque valeur de chaque
    échelle (47 valeurs) ; tout autre encodage arrête avant toute phase."""
    sain = nrj.controler_encodage(TOK, "jouet")
    assert sain["valeurs_controlees"] == sum(hi - lo + 1 for _, lo, hi in CRITERES) == 47
    assert nrj.controler_encodage(TokFusion(), "reel")["sondes"] == {"X: -1": [[2, 4], [4, 5]], "X: 0": [[2, 3], [3, 4]]}
    for tok, mode in ((TOK, "reel"), (TokFusion(), "jouet"), (TokRogne(), "reel")):
        with pytest.raises(GardeArret, match="encodage de 'X: -1'"):
            nrj.controler_encodage(tok, mode)
    with pytest.raises(GardeArret, match="encodage de « SPECIFICITY: 5 »"):
        nrj.controler_encodage(TokAPart(), "reel")


LLAMA3_DECOUPE = (r"(?i:'s|'t|'re|'ve|'m|'ll|'d)|[^\r\n\p{L}\p{N}]?\p{L}+|\p{N}{1,3}| ?[^\s\p{L}\p{N}]+[\r\n]*"
                  r"|\s*[\r\n]+|\s+(?!\S)|\s+")


def _tokeniseur_a_la_llama_3(rogner: bool):
    """Tokeniseur simulé à la Llama 3 (expression de découpage du modèle, octets, BPE appris sur des lignes de notes) ;
    `rogner` : décalages rognés de leur espace de tête par le post-traitement (« trim_offsets »)."""
    from tokenizers import Regex, Tokenizer, decoders, models, pre_tokenizers, processors, trainers
    from transformers import PreTrainedTokenizerFast

    t = Tokenizer(models.BPE())
    t.pre_tokenizer = pre_tokenizers.Sequence([pre_tokenizers.Split(Regex(LLAMA3_DECOUPE), behavior="isolated"),
                                               pre_tokenizers.ByteLevel(add_prefix_space=False, use_regex=False)])
    t.decoder = decoders.ByteLevel()
    t.post_processor = processors.ByteLevel(trim_offsets=rogner)
    lignes = "\n".join(f"{n}: {v}" for n, lo, hi in CRITERES for v in range(lo, hi + 1)) + "\nX: -1\nX: 0\n"
    t.train_from_iterator([lignes] * 50, trainers.BpeTrainer(vocab_size=400, show_progress=False,
                                                             initial_alphabet=pre_tokenizers.ByteLevel.alphabet()))
    return PreTrainedTokenizerFast(tokenizer_object=t)


def test_garde_d_encodage_sur_un_tokeniseur_a_la_llama_3():
    """Découpage attendu au réel, vérifié sur un tokeniseur simulé à la Llama 3 (le vrai n'est pas sur ce disque) :
    « X: -1 » donne « Ġ- » (2, 4) puis « 1 », et la garde passe. Décalages rognés (un post-traitement « trim_offsets ») :
    aucun jeton ne porte plus le caractère qui suit les deux-points ; sans la garde, aucune lecture n'aurait de score.
    La garde arrête."""
    tok = _tokeniseur_a_la_llama_3(rogner=False)
    e = tok("X: -1", add_special_tokens=False, return_offsets_mapping=True)
    assert tok.convert_ids_to_tokens(e["input_ids"])[2:] == ["Ġ-", "1"]
    assert nrj.controler_encodage(tok, "reel")["valeurs_controlees"] == 47
    with pytest.raises(GardeArret, match="encodage de 'X: -1'"):
        nrj.controler_encodage(_tokeniseur_a_la_llama_3(rogner=True), "reel")


def test_loi_renormalisee_egale_probabilite_oui_a_deux_valeurs_et_garde():
    lp_oui, lp_non = -0.3, -1.7
    assert math.isclose(nrj.loi_renormalisee({1: lp_oui, 0: lp_non})[1], probabilite_oui(lp_oui, lp_non))
    with pytest.raises(GardeArret, match="non finie"):
        nrj.loi_renormalisee({0: float("-inf"), 1: 0.0})


def test_candidats_ambigus_arretent():
    class Tok:
        def encode(self, s, add_special_tokens=False):
            return {"0": [5], "1": [5, 6]}[s]

    with pytest.raises(GardeArret, match="non séparées"):
        nrj.candidats_de_valeur(Tok(), "", 0, 1)
    assert nrj.candidats_de_valeur(TOK, "", -2, 0) == {-2: [_i("-"), _i("2")], -1: [_i("-"), _i("1")], 0: [_i("0")]}


def test_bloc_des_notes():
    texte = "Scores:\n" + COMPLET + "\nNow the analysis.\nSPECIFICITY: 5\n"
    bloc = nrj.bloc_des_notes(texte, CRITERES)
    assert bloc == "Scores:\n" + COMPLET
    assert nrj.lecture_ecrite(bloc, CRITERES, False)["notes"]["SPECIFICITY"] == 3
    assert nrj.bloc_des_notes(SANS_NOVELTY, CRITERES) is None


def test_completude_wilson_et_seuil():
    assert nrj.etiquette_completude(179, 180)["lecture"].startswith("H_A")
    assert nrj.etiquette_completude(178, 180)["lecture"].startswith("H_B")
    lo, hi = nrj.wilson(180, 180)
    assert 0.978 < lo < 0.98 and hi == 1.0
    assert not nrj.etiquette_completude(180, 180)["tranchee"]          # H_A jamais tranchée à 180
    tranchees = [k for k in range(181) if nrj.etiquette_completude(k, 180)["tranchee"]]
    assert tranchees == list(range(176))                               # 180 tirages supposés indépendants : k ≤ 175
    assert nrj.etiquette_completude(99, 100)["lecture"].startswith("H_A")          # seuil atteint : inclus
    with pytest.raises(GardeArret):
        nrj.etiquette_completude(0, 0)


def test_completude_tranchee_sur_les_120_textes():
    """Contre-lecture, CLJ-07 : 180 notations de 120 textes (60 notés deux fois). La lecture ponctuelle reste sur les 180
    notations (H_A si k ≥ 179) ; « tranchée » se lit sur une notation par texte, les 120 passe-0 (k0 ≤ 116) ; garde :
    chaque texte de la cellule a sa passe-0, une seule."""
    assert [k0 for k0 in range(121) if nrj.etiquette_completude(170, 180, k0, 120)["tranchee"]] == list(range(117))
    c = nrj.etiquette_completude(175, 180, 117, 120)
    assert c["lecture"].startswith("H_B") and not c["tranchee"]          # tranchée sur 180, plus sur les 120 textes
    assert nrj.etiquette_completude(180, 180, 120, 120)["wilson95_textes"][0] < 0.97
    recs = ([_notation(i, appuye=i >= 3) for i in range(120)]
            + [_notation(i, passe=1, appuye=i >= 2) for i in range(60)])
    c = nrj.completude(recs)
    assert (c["n"], c["finis"], c["textes"], c["finis_textes"]) == (180, 175, 120, 117)
    assert c["lecture"].startswith("H_B") and not c["tranchee"] and c["wilson95_notations"][1] < 0.99
    with pytest.raises(GardeArret, match="passe-0"):
        nrj.completude(recs + [_notation(5)])                             # un texte deux fois en passe-0
    with pytest.raises(GardeArret, match="passe-0"):
        nrj.completude(recs[1:])                                          # un texte sans sa passe-0


def _rec(note_ecrite, probabilites, masse=1.0):
    return {"ecrit": {"notes": {"RIGOR": note_ecrite}, "score": None},
            "proba": {"criteres": {"RIGOR": {"probabilites": probabilites, "masse": masse}}, "score": None}}


def _notation(i, ecrit=True, appuye=True, masse=0.9, admises=10, passe=0, motif=None):
    """Notation synthétique d'une cellule (lecture gelée) : texte i, note écrite valide aux `admises` premiers critères,
    loi lue concentrée sur la note écrite, de masse `masse` à chaque position ; `motif` : lecture en échec."""
    lus = {} if motif else {nom: {"probabilites": {str(lo): 1.0}, "masse": masse, "argmax": lo} for nom, lo, _ in CRITERES}
    return {"cle": f"juge-x/t{i}/e0/passe-{passe}", "ensemble_sha256": f"{i:064x}",
            "ecrit": {"notes": {nom: lo for nom, lo, _ in CRITERES[:admises]}, "score": 50.0 if ecrit else None},
            "proba": {"criteres": lus, "score": 50.0 if appuye and not motif else None,
                      "score_sans_appui": None if motif else 50.0, "motif": motif}}


def test_controle_d_alignement_cas_sain_et_artefact():
    """La note écrite, tirée de la loi lue, n'y est presque jamais improbable : cas sain « aligné » ; une lecture à la
    mauvaise position (note écrite à 1e-4) dans plus de 2 % des critères : « désaligné »."""
    sain = [_rec(3, {"3": 0.6, "2": 0.4})] * 99 + [_rec(3, {"3": 1e-4, "2": 0.9999})]
    assert nrj.alignement(sain)["lecture"] == "aligné" and nrj.alignement(sain)["improbables"] == 1
    faux = [_rec(3, {"3": 0.6, "2": 0.4})] * 97 + [_rec(3, {"3": 1e-4, "2": 0.9999})] * 3
    assert nrj.alignement(faux)["lecture"] == "désaligné"
    assert nrj.alignement([_rec(3, {})])["lecture"] == "sans note écrite lue"
    table = _table()
    r = {"ecrit": nrj.lecture_ecrite(COMPLET, CRITERES, False), "proba": _lire(table)}
    assert nrj.alignement([r])["lecture"] == "aligné"
    inverse = _table(espace={"0": 3.0, "1": -9.0, "2": -9.0, "3": -9.0, "4": 3.0, "5": 3.0, "-": 2.0})
    r = {"ecrit": nrj.lecture_ecrite(COMPLET, CRITERES, False), "proba": _lire(inverse, masse_min=0.0)}
    assert nrj.alignement([r])["lecture"] == "désaligné"


def test_masse_effondree_desalignee_jamais_tranchee():
    """Contre-lecture, CLJ-03, démonstration du contre-lecteur : la masse part sur un jeton « x », les valeurs gardent
    des proportions égales. La loi renormalisée reste plate (la note écrite n'y est jamais sous 0,001 : 500 critères,
    0 improbable) ; la probabilité brute s'effondre (masse admise au plus 3,7e-5). Le contrôle porte sur la probabilité
    brute : « désaligné », et la cellule se lit « non concluant », jamais « H_B tranchée »."""
    table = _table(espace={"x": 12.0, "0": 0.0, "1": 0.0, "2": 0.0, "3": 0.0, "4": 0.0, "5": 0.0, "-": 0.0},
                   moins={"1": 0.0, "2": 0.0})
    lu = _lire(table)
    assert lu["score"] is None and "seuil d'appui" in lu["motif"]
    assert math.isclose(max(c["masse"] for c in lu["criteres"].values()), 3.7e-5, rel_tol=0.01)
    ecrit = nrj.lecture_ecrite(COMPLET, CRITERES, False)
    recs = [{"cle": f"juge-x/t{i}/e0/passe-0", "ensemble_sha256": f"{i:064x}", "ecrit": ecrit, "proba": lu}
            for i in range(50)]
    a = nrj.alignement(recs)
    assert a["lecture"] == "désaligné" and a["criteres"] == 500 and a["improbables"] == 500    # module relu : « aligné »
    assert a["improbables_loi_renormalisee"] == 0                              # la loi renormalisée ne voit rien
    cell = nrj.lire_cellule(recs, "x/b0-relu", 1234)
    assert cell["lecture"] == "non concluant (instrument désaligné)" and cell["tranchee"] is False
    assert cell["lecture_brute"].startswith("H_B") and cell["tranchee_brute"] is True
    assert {"instrument désaligné", "trop défavorable : toutes les masses sous 0,01",
            "trop défavorable : scores écrits sans score appuyé au-delà de 0,05 × n"} <= set(
        cell["audit_r4"]["declencheurs"])


def test_audit_r4_symetrique_et_tirage_gele():
    """Contre-lecture, CLJ-05 et CLJ-06 : l'audit R4 se déclenche sur un résultat trop favorable comme sur un résultat
    trop défavorable, et sur la lecture par les jetons de tête ; les vingt notations relues sont tirées par la graine
    `audit-r4/<cellule>`, dérivée de l'entropie (R9), donc fixées avant toute lecture. Lectures en échec de
    l'instrument au-delà de 0,02 × n : « non concluant »."""
    def declencheurs(recs):
        return nrj.lire_cellule(recs, "x/b0-relu", 1234)["audit_r4"]["declencheurs"]

    neutre = [_notation(i) for i in range(90)] + [_notation(i, ecrit=False, appuye=False) for i in range(90, 100)]
    c = nrj.lire_cellule(neutre, "x/b0-relu", 1234)
    assert c["audit_r4"] == {"declencheurs": []} and c["lecture"].startswith("H_B") and c["tranchee"]
    assert declencheurs([_notation(i, masse=0.995) for i in range(100)]) == [
        "trop favorable : n sur n", "trop favorable : toutes les masses au-dessus de 0,99"]
    assert declencheurs([_notation(i, appuye=False, masse=0.005) for i in range(100)]) == [
        "trop défavorable : cellule à 0 ou presque (au plus 0,02 × n)", "trop défavorable : toutes les masses sous 0,01",
        "trop défavorable : scores écrits sans score appuyé au-delà de 0,05 × n"]
    tete = neutre[:87] + [_notation(i, admises=9) for i in range(87, 90)] + neutre[90:]
    assert declencheurs(tete) == ["jetons de tête : scores appuyés à note écrite non admise au-delà de 0,02 × n"]
    assert nrj.lire_cellule(tete, "x/b0-relu", 1234)["finis_appuyes_note_ecrite_non_admise"] == 3
    echec = neutre[:97] + [_notation(i, ecrit=False, motif="aucun jeton ne porte la valeur du critère RIGOR")
                           for i in range(97, 100)]
    c = nrj.lire_cellule(echec, "x/b0-relu", 1234)
    assert c["lectures_en_echec_instrument"] == 3 and "lecture en échec de l'instrument" in c["audit_r4"]["declencheurs"]
    assert c["lecture"] == "non concluant (lectures en échec de l'instrument)" and c["tranchee"] is False
    deux = neutre[:98] + [_notation(i, ecrit=False, motif="log-probabilité non finie au critère RIGOR") for i in (98, 99)]
    c = nrj.lire_cellule(deux, "x/b0-relu", 1234)                          # 2 ≤ 0,02 × 100 : audit, pas d'arrêt
    assert c["lecture"].startswith("H_B") and "lecture en échec de l'instrument" in c["audit_r4"]["declencheurs"]
    # tirage gelé : déterministe, vingt notations distinctes de la cellule, dérivé par la clé de la cellule (R9)
    fav = [_notation(i, masse=0.995) for i in range(100)]
    t = nrj.lire_cellule(fav, "x/b0-relu", 1234)["audit_r4"]
    cles = [r["cle"] for r in fav]
    g = generateur(graines(["audit-r4/x/b0-relu"], 1234)["audit-r4/x/b0-relu"])
    assert t["cle_graine"] == "audit-r4/x/b0-relu" and t["notations"] == [cles[i] for i in sorted(
        int(x) for x in g.choice(100, size=20, replace=False))]
    assert len(set(t["notations"])) == 20 and t == nrj.lire_cellule(fav, "x/b0-relu", 1234)["audit_r4"]
    assert nrj.tirage_audit(1234, "x/verdict-d-abord", cles)["notations"] != t["notations"]


# ---------------------------------------------------------------- chaîne jouet

def _messages_courts(questions, ensemble, variante="b0", classification=None):
    """Invite courte (tests seulement) : la chaîne est la même, les passes jouet restent brèves."""
    return ([{"role": "system", "content": "Judge."},
             {"role": "user", "content": "Q: " + questions.strip() + "\nP: " + ensemble.strip() + "\n"}], CRITERES)


def _notations_artisanales(depot, monkeypatch, run=NOTATIONS, courtes=True):
    """Pilote jouet arrêté, puis notations « rejouées » faites par le vrai lanceur, aux réponses remplacées par les
    textes de `TEXTES` (notes, anomalies, score et troncature recalculés par la règle du pilote)."""
    f, _ = _pilote_arrete(depot, monkeypatch)
    if courtes:
        monkeypatch.setattr(pa, "messages_juge_ensemble", _messages_courts)
        monkeypatch.setattr(nrj, "messages_juge_ensemble", _messages_courts)
    vrai = pa.noter_ensembles

    def noter(m, fmt, morceau, graines, lot, max_nouveaux, temperature, echeance=None):
        sortie = vrai(m, fmt, morceau, graines, lot, max_nouveaux, temperature, echeance=echeance)
        for x in sortie:
            texte, tronquee = TEXTES[x["cle"].split("/", 1)[1]]
            x.update(reponse=texte, tronquee=tronquee, jetons_reponse=len(TOK.encode(texte, add_special_tokens=False)),
                     **nrj.lecture_ecrite(texte, CRITERES, tronquee))
        return sortie

    monkeypatch.setattr(npa, "noter_ensembles", noter)
    npa.executer(_config_notations(), depot, run, None, str(f), autoriser_depot_sale=True)
    monkeypatch.setattr(npa, "noter_ensembles", vrai)
    committer(depot)
    return f


def _phases(duree=300, variantes=nrj.VARIANTES):
    return [{"juge": j, "variante": v, "duree_max_s": duree} for v in variantes for j in ("jouet-8B", "jouet-3B")]


def _config(**changes):
    c = _config_notations()
    return {**{k: c[k] for k in nrj.CLES_EGALES_AUX_NOTATIONS}, "mode": "jouet", "run_notations": NOTATIONS,
            "phases": _phases(), "max_nouveaux_verdict": 16, "max_nouveaux_suite": 8, "masse_min_appui": 0.0,
            "duree_globale_s": 1800, **changes}


def _fichiers(depot, run):
    return sorted(p.name for p in (depot / "diag" / run).glob("*.json"))


def test_bout_en_bout_trois_variantes_deux_juges_et_lecture(depot, monkeypatch, capsys):
    f = _notations_artisanales(depot, monkeypatch)
    capsys.readouterr()                                   # lignes du lanceur des notations jouet écartées
    run = "20261029-100000-rejeu-jouet"
    resume = nrj.executer(_config(), depot, run, None, str(f), autoriser_depot_sale=True)
    assert [(p["juge"], p["variante"], p["statut"]) for p in resume["phases"]] == [
        (j, v, "écrit") for v in nrj.VARIANTES for j in ("jouet-8B", "jouet-3B")]
    assert resume["echeance"] == {"duree_globale_s": 1800.0, "echeance_externe": None, "reste_externe_s": None,
                                  "retenue_s": 1800.0, "source": "configuration"}
    assert {j: e["valeurs_controlees"] for j, e in resume["encodage"].items()} == {"jouet-8B": 47, "jouet-3B": 47}
    assert _fichiers(depot, run) == sorted([f"rejeu-{j}-{v}.json" for v in nrj.VARIANTES
                                            for j in ("jouet-8B", "jouet-3B")] + ["resume.json"])
    assert _fichiers(depot, NOTATIONS) == ["notations-jouet-3B-decisives.json", "notations-jouet-8B-decisives.json",
                                           "resume.json"]                    # rien d'écrit chez les notations rejouées
    for j in ("jouet-8B", "jouet-3B"):
        b0 = verifier_resultat(depot, depot / "diag" / run / f"rejeu-{j}-b0-relu.json")["resultat"]["notations"]
        assert [r["cle"].split("/", 1)[1] for r in b0] == list(TEXTES)
        assert [r["proba"]["score"] is not None for r in b0] == [True, True, False, False]   # appui nul (jouet)
        assert [r["ecrit"]["score"] is not None for r in b0] == [True, False, False, False]
        assert b0[2]["proba"]["motif"].startswith("fenêtre incomplète") and b0[3]["proba"]["motif"].startswith("critère")
        assert all(r["jetons_reponse_reencodes"] == r["jetons_reponse_rejoues"] for r in b0)    # tokeniseur jouet
        bud = verifier_resultat(depot, depot / "diag" / run / f"rejeu-{j}-budget-releve.json")["resultat"]["notations"]
        assert [r["cle"] for r in bud] == [b0[2]["cle"]] and bud[0]["suite"] is not None and bud[0]["jetons_suite"] <= 8
        vda = verifier_resultat(depot, depot / "diag" / run / f"rejeu-{j}-verdict-d-abord.json")["resultat"]
        assert len(vda["notations"]) == 4 and vda["consigne_verdict_sha256"] == nrj.EMPREINTE_CONSIGNE
        assert all(r["jetons_reponse"] <= 16 for r in vda["notations"])
    m = json.loads((depot / "runs" / run / "manifeste.json").read_text())
    mp = json.loads((depot / "runs" / PILOTE / "manifeste.json").read_text())
    assert {g["entropie"] for g in m["graines"].values()} == {next(iter(mp["graines"].values()))["entropie"]}
    assert m["graines"]["modele-jouet"] == mp["graines"]["modele-jouet"]
    assert sum(k.startswith("rejeu-v1/verdict-d-abord/") for k in m["graines"]) == 8
    assert sum(k.startswith("rejeu-v1/budget-releve/") for k in m["graines"]) == 2
    err = capsys.readouterr().err
    lignes = [x for x in err.splitlines() if x.startswith("PROGRES ")]
    assert lignes and "SPECIFICITY" not in err and "idée" not in err
    assert all(" variante=" in x and " juge=" in x for x in lignes)
    lecture = nrj.lire_rejeu(depot, run)
    assert lecture["source"] == "resume" and not lecture["arret_consigne"]
    c = lecture["cellules"]["jouet-8B/b0-relu"]
    # les notes jouet sont écrites à la main, non tirées du modèle jouet (masses de 0,005 à 0,04) : sur la probabilité
    # brute, 2 des 19 notes écrites sont improbables, la loi renormalisée n'en voit aucune (CLJ-03 au naturel)
    assert (c["alignement"]["improbables"], c["alignement"]["improbables_loi_renormalisee"]) == (2, 0)
    assert c["lecture"] == "non concluant (instrument désaligné)" and c["tranchee"] is False
    assert (c["n"], c["finis"], c["finis_ecrits"]) == (4, 2, 1) and c["lecture_brute"].startswith("H_B")
    assert (c["textes"], c["finis_textes"]) == (2, 1) and c["statut"] == "écrit" and c["statut_consigne"] == "écrit"
    assert c["accord"]["paires"] == 1 and c["accord"]["criteres"] == 10
    assert lecture["cellules"]["jouet-3B/budget-releve"]["n"] == 4                 # cellule composée
    assert c["rythme"]["s_par_notation"] is not None and c["rythme"]["passes_forcees"] >= 2
    assert c["alignement"]["criteres"] >= 10 and c["alignement"]["positions_lues"] == 20
    assert c["reencodage"] == {"notations": 4, "ecarts": 0}
    # « COHERENCE: 2.5 » lu par son jeton de tête « 2 » : score appuyé, note écrite non admise (CLJ-06), audit déclenché
    assert c["finis_appuyes_note_ecrite_non_admise"] == 1
    assert "jetons de tête : scores appuyés à note écrite non admise au-delà de 0,02 × n" in c["audit_r4"]["declencheurs"]
    assert c["audit_r4"]["cle_graine"] == "audit-r4/jouet-8B/b0-relu" and len(c["audit_r4"]["notations"]) == 4
    monkeypatch.setattr(nrj, "alignement", lambda recs: {"lecture": "aligné"})        # instrument supposé juste
    c = nrj.lire_rejeu(depot, run)["cellules"]["jouet-8B/b0-relu"]
    assert c["lecture"].startswith("H_B") and "lecture_brute" not in c and c["tranchee"] is True    # 1 texte sur 2


def test_lecture_ecrite_au_pilote_et_r12(depot, monkeypatch):
    f = _notations_artisanales(depot, monkeypatch)
    run = "20261029-100001-rejeu-jouet"
    cfg = _config(phases=_phases(variantes=("b0-relu",)))
    nrj.executer(cfg, depot, run, None, str(f), autoriser_depot_sale=True)
    with pytest.raises(GardeArret, match="R12"):
        nrj.executer(cfg, depot, run, None, str(f), autoriser_depot_sale=True)
    from controle_ia.manifeste import ecrire_resultat
    chemin_m = depot / "runs" / run / "manifeste.json"
    ecrire_resultat(depot, chemin_m, "lecture-rejeu-v1", nrj.lire_rejeu(depot, run))
    with pytest.raises(GardeArret, match="R12"):
        ecrire_resultat(depot, chemin_m, "lecture-rejeu-v1", nrj.lire_rejeu(depot, run))


def test_echeance_de_phase_le_suivant_continue(depot, monkeypatch):
    f = _notations_artisanales(depot, monkeypatch)
    run = "20261029-100002-rejeu-jouet"
    phases = [{"juge": "jouet-8B", "variante": "b0-relu", "duree_max_s": 1e-9},
              {"juge": "jouet-3B", "variante": "b0-relu", "duree_max_s": 300}]
    resume = nrj.executer(_config(phases=phases), depot, run, None, str(f), autoriser_depot_sale=True)
    assert [(p["statut"], p["lots_faits"]) for p in resume["phases"]] == [("échu", 0), ("écrit", 2)]
    assert _fichiers(depot, run) == ["rejeu-jouet-3B-b0-relu.json", "resume.json"]       # tout ou rien
    lecture = nrj.lire_rejeu(depot, run)
    assert lecture["cellules"]["jouet-8B/b0-relu"] == {"lecture": "non mesurée", "statut": "échu"}


def test_echeance_globale_aucune_phase_ne_commence(depot, monkeypatch):
    f = _notations_artisanales(depot, monkeypatch)
    run = "20261029-100003-rejeu-jouet"
    resume = nrj.executer(_config(phases=_phases(duree=0.5), duree_globale_s=0.5), depot, run, None, str(f),
                          autoriser_depot_sale=True)
    assert {p["statut"] for p in resume["phases"]} == {"non-commencé"}
    assert _fichiers(depot, run) == ["resume.json"]


def test_signal_term_consigne_et_propage(depot, monkeypatch):
    f = _notations_artisanales(depot, monkeypatch)
    vrai = nrj._relire_b0

    def relire(*a, **k):
        sortie = vrai(*a, **k)
        gardes.SIGNAL_TERM_RECU.append(15)           # signal avalé par une bibliothèque : drapeau seul
        return sortie

    monkeypatch.setattr(nrj, "_relire_b0", relire)
    run = "20261029-100004-rejeu-jouet"
    with pytest.raises(GardeArret, match="signal TERM"):
        nrj.executer(_config(), depot, run, None, str(f), autoriser_depot_sale=True)
    assert _fichiers(depot, run) == ["arret.json"]
    r = verifier_resultat(depot, depot / "diag" / run / "arret.json")["resultat"]
    assert r["etape"] == "b0-relu par jouet-8B" and r["partiel"]["phases"][0]["lots_faits"] == 1
    assert r["partiel"]["echeance"]["source"] == "configuration"            # échéance consignée dans l'arrêt aussi
    c = nrj.lire_rejeu(depot, run)["cellules"]
    assert c["jouet-8B/b0-relu"] == {"lecture": "non mesurée (arrêt)", "statut": "arrêt pendant la phase"}
    assert c["jouet-3B/b0-relu"] == {"lecture": "non mesurée (arrêt)", "statut": "non atteinte"}


def test_lecture_apres_arret_phases_ecrites_lues(depot, monkeypatch):
    """Contre-lecture, CLJ-01 : un signal TERM pendant la troisième phase laisse `arret.json`, sans `resume.json` ; la
    lecture gelée lit les deux phases écrites et scellées, la phase en cours est « non mesurée (arrêt) », les suivantes
    « non atteinte ». Sans résumé ni arrêt (KILL), les fichiers écrits se lisent encore ; un fichier sans sceau ne se
    lit pas."""
    f = _notations_artisanales(depot, monkeypatch)
    vrai = nrj._verdict_d_abord

    def verdict(*a, **k):
        gardes.SIGNAL_TERM_RECU.append(15)           # TERM pendant le premier lot de la troisième phase
        return vrai(*a, **k)

    monkeypatch.setattr(nrj, "_verdict_d_abord", verdict)
    run = "20261029-100014-rejeu-jouet"
    with pytest.raises(GardeArret, match="signal TERM"):
        nrj.executer(_config(), depot, run, None, str(f), autoriser_depot_sale=True)
    assert _fichiers(depot, run) == ["arret.json", "rejeu-jouet-3B-b0-relu.json", "rejeu-jouet-8B-b0-relu.json"]
    lecture = nrj.lire_rejeu(depot, run)
    c = lecture["cellules"]
    assert lecture["source"] == "arret" and lecture["arret_consigne"]
    assert all(c[f"jouet-{j}/b0-relu"]["n"] == 4 and c[f"jouet-{j}/b0-relu"]["statut"] == "écrit"
               and c[f"jouet-{j}/b0-relu"]["lecture_brute"].startswith("H_B") for j in ("8B", "3B"))
    assert c["jouet-8B/verdict-d-abord"] == {"lecture": "non mesurée (arrêt)", "statut": "arrêt pendant la phase"}
    assert [c[f"jouet-{j}/{v}"]["statut"] for v in ("verdict-d-abord", "budget-releve") for j in ("3B", "8B")
            if (j, v) != ("8B", "verdict-d-abord")] == ["non atteinte"] * 3
    d = depot / "diag" / run
    for p in (d / "arret.json", d / "arret.json.sha256"):
        p.unlink()                                   # artefact de test : arrêt par KILL, rien de consigné
    (d / "rejeu-jouet-8B-verdict-d-abord.json").write_text("{", encoding="utf-8")        # écrit à moitié, sans sceau
    lecture = nrj.lire_rejeu(depot, run)
    c = lecture["cellules"]
    assert lecture["source"].startswith("aucune") and c["jouet-3B/b0-relu"]["n"] == 4
    assert c["jouet-3B/b0-relu"]["statut_consigne"] is None
    assert c["jouet-8B/verdict-d-abord"] == {"lecture": "non mesurée (fichier non scellé)", "statut": "non consigné"}
    assert c["jouet-3B/verdict-d-abord"] == {"lecture": "non mesurée (non consignée)", "statut": "non consigné"}


def test_echeance_externe_courte_aucune_phase_commencee_puis_tuee(depot, monkeypatch):
    """Contre-lecture, CLJ-02 : l'échéance du module vient de la chaîne (délai externe moins la marge du dernier lot).
    Une échéance externe courte donne « non-commencé » à toute phase qu'elle ne couvre pas, au lieu d'une phase
    commencée puis tuée par le délai externe ; l'échéance retenue est consignée. En mode réel, elle est exigée ; passée,
    elle arrête avant le manifeste."""
    f = _notations_artisanales(depot, monkeypatch)
    run = "20261029-100015-rejeu-jouet"
    resume = nrj.executer(_config(), depot, run, None, str(f), autoriser_depot_sale=True,
                          echeance_externe=time.time() + 60)
    assert [p["statut"] for p in resume["phases"]] == ["non-commencé"] * 6     # durée globale (1800 s) : elles tenaient
    e = resume["echeance"]
    assert e["source"] == "externe" and 40 < e["retenue_s"] <= 60 and e["duree_globale_s"] == 1800
    assert _fichiers(depot, run) == ["resume.json"]
    autre = "20261029-100016-rejeu-jouet"
    with pytest.raises(GardeArret, match="déjà passée"):
        nrj.executer(_config(), depot, autre, None, str(f), autoriser_depot_sale=True, echeance_externe=time.time() - 1)
    with pytest.raises(GardeArret, match="horodatage fini"):
        nrj.executer(_config(), depot, autre, None, str(f), autoriser_depot_sale=True, echeance_externe=float("nan"))
    assert not (depot / "runs" / autre).exists()
    with pytest.raises(GardeArret, match="sans échéance externe"):
        nrj.executer(_config(mode="reel"), depot, autre, "prereg/fiche.md", str(f))


def test_encodage_different_arrete_avant_toute_phase(depot, monkeypatch):
    """Garde d'encodage dans la chaîne : un tokeniseur qui ne découpe pas les valeurs comme la lecture le suppose arrête
    au contrôle du format, `arret.json` consigné, aucune phase commencée."""
    f = _notations_artisanales(depot, monkeypatch)
    monkeypatch.setitem(nrj.DECOUPAGES_ATTENDUS, "jouet", nrj.DECOUPAGES_ATTENDUS["reel"])
    run = "20261029-100017-rejeu-jouet"
    with pytest.raises(GardeArret, match="encodage de 'X: -1'"):
        nrj.executer(_config(), depot, run, None, str(f), autoriser_depot_sale=True)
    assert _fichiers(depot, run) == ["arret.json"]
    r = verifier_resultat(depot, depot / "diag" / run / "arret.json")["resultat"]
    assert r["etape"] == "contrôle de l'encodage des valeurs" and r["partiel"]["phases"] == []


def test_contexte_reconstruit_different_arrete_apres_le_manifeste(depot, monkeypatch):
    f = _notations_artisanales(depot, monkeypatch)

    def autres(questions, ensemble, variante="b0", classification=None):
        msgs, crit = _messages_courts(questions, ensemble, variante, classification)
        msgs[0]["content"] += " Be strict."
        return msgs, crit

    monkeypatch.setattr(nrj, "messages_juge_ensemble", autres)
    run = "20261029-100005-rejeu-jouet"
    with pytest.raises(GardeArret, match="contexte reconstruit"):
        nrj.executer(_config(), depot, run, None, str(f), autoriser_depot_sale=True)
    assert verifier_resultat(depot, depot / "diag" / run / "arret.json")["resultat"]["etape"] == "b0-relu par jouet-8B"


@pytest.mark.parametrize("changement, motif", [
    ({"lot_juge": 3}, "lot_juge ≠ celui des notations rejouées"),
    ({"run_notations": "20261012-110199-absent"}, "manifeste des notations rejouées absent"),
    ({"phases": [{"juge": "jouet-8B", "variante": "autre", "duree_max_s": 9}]}, "variante 'autre' inconnue"),
    ({"phases": [{"juge": "jouet-9B", "variante": "b0-relu", "duree_max_s": 9}]}, "juge 'jouet-9B' inconnu"),
    ({"phases": [{"juge": "jouet-8B", "variante": "budget-releve", "duree_max_s": 9}]}, "sans b0-relu"),
    ({"phases": _phases()[:1] * 2}, "phase en double"),
    ({"phases": _phases(duree=1801)}, "hors de"),
    ({"max_nouveaux_verdict": 8}, "max_nouveaux_verdict"),
    ({"masse_min_appui": 1.5}, "masse_min_appui"),
    ({"duree_globale_s": 5401}, "duree_globale_s"),
    ({"variante_juge": "b*"}, "b0"),
])
def test_gardes_de_configuration_cas_sain_et_artefacts(depot, monkeypatch, changement, motif):
    f = _notations_artisanales(depot, monkeypatch)
    run = "20261029-100006-rejeu-jouet"
    with pytest.raises(GardeArret, match=motif):
        nrj.executer(_config(**changement), depot, run, None, str(f), autoriser_depot_sale=True)
    assert not (depot / "runs" / run).exists()
    nrj.exiger_config_rejeu(_config())                                                     # cas sain


def test_config_incomplete_et_reel_sans_fiche(depot):
    with pytest.raises(GardeArret, match="incomplète"):
        nrj.executer({k: v for k, v in _config().items() if k != "phases"}, depot, "20261029-100007-x", None, "t.json")
    with pytest.raises(GardeArret, match="R1"):
        nrj.executer(_config(mode="reel"), depot, "20261029-100008-x", None, "t.json")
    assert not (depot / "runs").exists()


def _reecrire(chemin, changer):
    corps = json.loads(chemin.read_text())
    changer(corps)
    chemin.write_text(json.dumps(corps, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    Path(str(chemin) + ".sha256").unlink()             # artefact de test : ancien sceau retiré, puis rescellé
    sceller(chemin)


@pytest.mark.parametrize("changer, motif", [
    (lambda c: c["resultat"]["notations"][0].update(score=99.0), "lecture écrite refaite ≠ score"),
    (lambda c: c["resultat"]["notations"][1].update(ensemble_sha256="0" * 64), "ensemble ≠ ensemble noté"),
    (lambda c: c["resultat"]["notations"].pop(), "3 notations rejouées, 4 attendues"),
    (lambda c: c["resultat"]["notations"][0].update(cle="juge-jouet-8B/x/e0/passe-0"), "clé"),
])
def test_alignement_des_notations_rejouees_artefacts(depot, monkeypatch, changer, motif):
    f = _notations_artisanales(depot, monkeypatch)
    chemin = depot / "diag" / NOTATIONS / "notations-jouet-8B-decisives.json"
    sauve = {p: p.read_bytes() for p in (chemin, Path(str(chemin) + ".sha256"))}
    run = "20261029-100009-rejeu-jouet"
    _reecrire(chemin, changer)
    with pytest.raises(GardeArret, match=motif):
        nrj.executer(_config(), depot, run, None, str(f), autoriser_depot_sale=True)
    assert not (depot / "runs" / run).exists()
    for p, b in sauve.items():
        p.write_bytes(b)
    nrj.exiger_alignement(*_demandes_et_notations(depot, f, "jouet-8B"), "jouet-8B", 4)     # cas sain


def _demandes_et_notations(depot, f, nom):
    pil = npa.charger_pilote_note(depot, PILOTE)
    par_id = {t["identifiant"]: t for t in pa.charger_taches(str(f))}
    n = nrj.charger_notations_rejouees(depot, NOTATIONS, [nom])
    return npa.demandes_decisives(pil, par_id, _config(), nom), n["notations"][nom]


def test_notations_rattachees_a_un_autre_manifeste(depot, monkeypatch):
    f = _notations_artisanales(depot, monkeypatch)
    from controle_ia.manifeste import creer_manifeste, lire_manifeste
    chemin_autre, _ = creer_manifeste(depot, "20261012-100002-autre-run", {"essai": 1}, ["x"], autoriser_depot_sale=True)
    _, sha_autre = lire_manifeste(chemin_autre)
    _reecrire(depot / "diag" / NOTATIONS / "notations-jouet-3B-decisives.json",
              lambda c: c.update(manifeste_sha256=sha_autre))
    with pytest.raises(GardeArret):
        nrj.executer(_config(), depot, "20261029-100010-rejeu-jouet", None, str(f), autoriser_depot_sale=True)


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
               "Consigne du verdict d'abord": nrj.EMPREINTE_CONSIGNE, "Tâches du pilote": empreinte(f),
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
    monkeypatch.setattr(nrj, "exiger_code_importe_sous", lambda racine: None)
    commit = subprocess.run(["git", "-C", str(depot), "rev-parse", "HEAD"], capture_output=True, text=True,
                            check=True).stdout.strip()
    mp = json.loads((depot / "runs" / PILOTE / "manifeste.json").read_text())
    entropie = int(next(iter(mp["graines"].values()))["entropie"])
    c = _config(phases=_phases(variantes=("b0-relu",)))
    sain = _fiche(depot, c, f, entropie, commit)
    cas = [(_fiche(depot, _config(), f, entropie, commit, "f-config.md"), "configuration"),
           (_fiche(depot, c, f, entropie + 1, commit, "f-entropie.md"), "entropie citée ≠ celle du pilote"),
           (_fiche(depot, c, f, entropie, commit, "f-notations.md",
                   remplacements={"Notations rejouées du jouet-3B": "1" * 64}), "notations rejouées du jouet-3B"),
           (_fiche(depot, c, f, entropie, commit, "f-juge-absent.md",
                   remplacements={"Notations rejouées du jouet-3B": None}), "attendues pour"),
           (_fiche(depot, c, f, entropie, commit, "f-consigne.md",
                   remplacements={"Consigne du verdict d'abord": "2" * 64}), "consigne"),
           (_fiche(depot, c, f, entropie, commit, "f-double.md",
                   en_plus=(f"- Run des notations rejouées : `{NOTATIONS}`",)), "cité 2 fois"),
           (_fiche(depot, c, f, entropie, commit, "f-taches.md", remplacements={"Tâches du pilote": "3" * 64}),
            "tâches")]
    committer(depot)
    for p, motif in cas:
        with pytest.raises(GardeArret, match=motif):
            nrj.executer(c, depot, "20261029-100011-rejeu-jouet", str(p), str(f))
        assert not (depot / "runs" / "20261029-100011-rejeu-jouet").exists()
    resume = nrj.executer(c, depot, "20261029-100012-rejeu-jouet", str(sain), str(f), autoriser_depot_sale=True)
    assert resume["commit_cite"] == commit
    m = json.loads((depot / "runs" / "20261029-100012-rejeu-jouet" / "manifeste.json").read_text())
    assert m["decisif"] and m["preenregistrement"]["chemin"] == "prereg/fiche.md"


def test_invite_reelle_b0_relue(depot, monkeypatch):
    """Invite réelle (H3, H4), sans raccourci : la phase « b0-relu » d'un juge relit le contexte rejoué au jeton près."""
    f = _notations_artisanales(depot, monkeypatch, courtes=False)
    run = "20261029-100013-rejeu-jouet"
    phases = [{"juge": "jouet-3B", "variante": "b0-relu", "duree_max_s": 600}]
    resume = nrj.executer(_config(phases=phases), depot, run, None, str(f), autoriser_depot_sale=True)
    assert resume["phases"][0]["statut"] == "écrit"
    b0 = verifier_resultat(depot, depot / "diag" / run / "rejeu-jouet-3B-b0-relu.json")["resultat"]["notations"]
    assert [r["proba"]["score"] is not None for r in b0] == [True, True, False, False]
    assert all(r["jetons_contexte"] > 5000 for r in b0)


def test_consigne_du_verdict_d_abord_figee():
    assert nrj.EMPREINTE_CONSIGNE == hashlib.sha256(nrj.CONSIGNE_VERDICT_D_ABORD.encode("utf-8")).hexdigest()
    lignes = nrj.CONSIGNE_VERDICT_D_ABORD.splitlines()
    assert [x.split(":")[0] for x in lignes[1:11]] == [n for n, _, _ in CRITERES]


def test_fonctions_importees_sans_copie():
    """Le module importe le code cité du pilote, sans copie ni enveloppe."""
    from controle_ia.environnements import juges, rubrique
    from controle_ia.harnais import episode
    assert nrj.generer_lot is episode.generer_lot and nrj.lire_notes is rubrique.lire_notes
    assert nrj.messages_juge_ensemble is juges.messages_juge_ensemble
    assert nrj.charger_pilote_note is npa.charger_pilote_note and nrj.progres is npa.progres
    assert nrj.logits_derniere_position is pa.logits_derniere_position and nrj._LIGNE is rubrique._LIGNE
