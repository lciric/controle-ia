"""Essais R5 des corrections de la contre-lecture du code de T0.7 (`contre-lecture-code-t07-v1.md`, `1efd31f6…`, sur le commit
`1f77b34d`) : CT-01 à CT-07, et les mineurs corrigés dans le code (CT-09, CT-10, CT-11, CT-13, CT-14, CT-15, CT-18). Chaque
correction : un cas sain et au moins un artefact. Faux run de 7b et jeux génériques de `tests/test_t07_sondes_neuves_v1.py`."""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.t07 import garde_adaptee_v1 as ga
from controle_ia.t07 import journal_p3bis_v1 as jp
from controle_ia.t07 import lecture_v1 as lv1
from controle_ia.t07 import lecture_v2 as lv
from controle_ia.t07 import lectures_t07_v1 as lt
from controle_ia.t07 import registre_v1 as rg
from controle_ia.t07 import sondes_neuves_v1 as sn
from test_t07_lecture_v1 import APRES_A, INSTANT, RUN_T06
from test_t07_lecture_v2 import ENTETE, lignes_audit, lignes_p3bis, ligne_j
from test_t07_sondes_neuves_v1 import _a, _b, _resultat, construire_complet, phrases_concepts

RACINE_DEPOT = Path(__file__).resolve().parents[1]
CONFIG_V2 = RACINE_DEPOT / "brouillons" / "T0.7-sondes-v0-v1-brouillon19-pieces" / "configuration-t07-v2.json"


@pytest.fixture
def complet(depot):
    return construire_complet(depot)


@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason="règle de CT-01 remplacée par C20-01 (R-2098) : une action sans caractère de mot est "
                   "exclue de la notation des témoins, qui notent le reste ; voir tests/test_t07_corrections_cl20_v1.py")
def test_CT01_action_sans_caractere_de_mot_temoin_en_echec_sans_arret(complet, monkeypatch):
    """CT-01 (bloquant) : une action sans caractère de mot ne fait plus arrêter l'étape A ; chaque témoin lexical est en « échec »
    (motif, compte des actions sans mot), aucun tableau `lexical_<concept>` n'est écrit, T7-P10 est « non lue » à l'étape B.
    Cas sain : l'essai de bout en bout (témoins notés)."""
    original = lv.lire_textes

    def avec_action_vide(chemin):
        t = original(chemin)
        t[sorted(t)[0]] = "?! ..."
        return t
    monkeypatch.setattr(lv, "lire_textes", avec_action_vide)
    ra = _a(complet)
    lx = ra["index"]["lexicaux"]
    assert all(x["etat"] == "échec" and x["actions_sans_mot"] == 1 for x in lx.values()) and set(lx) == {"dissimulation", "domaine"}
    with np.load(complet.racine / ra["scores"]["chemin"]) as z:
        assert not any(k.startswith("lexical_") for k in z.files)
    lignes_audit(complet, ra["run_t07"])
    lignes_p3bis(complet, APRES_A)
    lec = _b(complet, ra["run_t07"])
    assert all(lec["predictions"]["T7-P10"][c]["etat"].startswith("non lue : témoin lexical en échec") for c in ("dissimulation", "domaine"))


def test_CT02_manifeste_nomme_concepts_et_jeux_et_etape_B_les_exige(complet, monkeypatch):
    """CT-02 : le manifeste porte `concepts_lus` et `jeux_scelles` ; à l'étape B, des concepts de `sondes-t07.json` différents de
    ceux du manifeste → refus (artefact) ; cas sain : égaux, lecture faite."""
    ra = _a(complet)
    m = json.loads((complet.racine / "runs" / ra["run_t07"] / "manifeste.json").read_text())["config"]
    assert m["concepts_lus"] == ["tromperie", "enjeux", "dissimulation", "domaine"] and m["jeux_scelles"] == {"J-D": True, "J-C": True, "J-A": True}
    (complet.racine / "autre").mkdir()
    j2 = construire_complet(complet.racine / "autre")
    original = lv1.ecrire_resultat

    def concepts_changes(racine, chemin_m, nom, contenu):
        if nom == "sondes-t07":
            contenu = {**contenu, "concepts": list(reversed(contenu["concepts"]))}
        return original(racine, chemin_m, nom, contenu)
    monkeypatch.setattr(lv1, "ecrire_resultat", concepts_changes)
    ra2 = _a(j2)
    monkeypatch.setattr(lv1, "ecrire_resultat", original)
    lignes_audit(j2, ra2["run_t07"])
    lignes_p3bis(j2, APRES_A)
    with pytest.raises(rg.RefusRegistre, match="concepts de sondes-t07.json"):
        _b(j2, ra2["run_t07"])


def test_CT03_R9_cherchee_sur_tous_les_jeux_d_organisme():
    """CT-03 : aire hors de [0,05 ; 0,95] ou quantile du plancher > 0,70 sur un jeu non décisif (T7-P18 sur `T100`, jeu hors
    jugement) → R9 ; cas sain : aires dans l'intervalle → pas de R9."""
    sain = {"aire": 0.7, "plancher_quantile": 0.6, "etat": "non au-dessus"}
    decisifs = {"s": {"(i-a)": dict(sain)}}
    base = {"predictions": {"T7-P18": {"s": {"T100 contre honnete": dict(sain), "R3": False}}}}
    ids = lambda r: [x["id"] for x in r]
    assert "R9" not in ids(lt.reserves(base, decisifs, ["s"], {"s": {"S25": dict(sain)}}))
    trop = {"predictions": {"T7-P18": {"s": {"T100 contre honnete": {**sain, "aire": 0.99}, "R3": False}}}}
    r = lt.reserves(trop, decisifs, ["s"], {})
    assert "R9" in ids(r) and "T7-P18" in next(x["motif"] for x in r if x["id"] == "R9")
    r = lt.reserves(base, decisifs, ["s"], {"s": {"S25": {**sain, "plancher_quantile": 0.75}}})
    assert "R9" in ids(r) and "hors jugement" in next(x["motif"] for x in r if x["id"] == "R9")


def test_CT04_familles_et_reglages_contraints(complet):
    """CT-04 : `familles` autre que la liste gelée, ou `reglages` autre que nul ou les valeurs par défaut → arrêt de
    configuration (jamais ignorée) ; cas sain : liste gelée, réglages nuls ou par défaut."""
    c = complet.config
    lv.exiger_configuration(c)
    lv.exiger_configuration({**c, "reglages": None})
    lv.exiger_configuration({**c, "reglages": sn.reglages_par_defaut()})
    with pytest.raises(GardeArret, match="familles = .*arrêt de configuration"):
        lv.exiger_configuration({**c, "familles": ["lineaire"]})
    with pytest.raises(GardeArret, match="reglages = .*arrêt de configuration"):
        lv.exiger_configuration({**c, "reglages": {**sn.reglages_par_defaut(), "epoques": 10}})


def test_CT05_echec_de_T7P6_et_d_une_direction_sans_arret(complet, monkeypatch):
    """CT-05 : un essai d'égalité en échec pour la sonde de T7-P6 met T7-P6 en « échec » (étape A menée au bout, T7-P6 « non
    lue » à l'étape B) ; une direction de concept en échec est écrite « échec », les autres notées."""
    original_p, original_d = sn.preparer_sonde, sn.direction_concept

    def preparer(s, calcul, g):
        if s.nom.startswith("intention-sans-cout"):
            raise GardeArret("essai d'égalité au paquet gelé en échec (essai)")
        return original_p(s, calcul, g)

    def direction(concept, couche, pos, neg):
        if concept == "jardins" and couche == 7:
            raise GardeArret("direction nulle (essai)")
        return original_d(concept, couche, pos, neg)
    monkeypatch.setattr(sn, "preparer_sonde", preparer)
    monkeypatch.setattr(sn, "direction_concept", direction)
    ra = _a(complet)
    s = _resultat(complet, ra["run_t07"], "sondes-t07.json")["sondes_neuves"]
    assert s["p6"]["etat"].startswith("échec : essai d'égalité")
    assert sum(1 for d in s["directions"] if str(d.get("etat", "")).startswith("échec")) == 1 and len(s["directions"]) == 6
    lignes_audit(complet, ra["run_t07"])
    lignes_p3bis(complet, APRES_A)
    lec = _b(complet, ra["run_t07"])
    assert lec["predictions"]["T7-P6"]["etat"].startswith("non lue")
    assert len(lec["predictions"]["T7-P9"]["lectures"]) == 5


def test_CT06_instant_refuse_en_mode_reel(tmp_path):
    """CT-06 : `--instant` refusé en mode réel (code 2, motif) ; cas sain : permis en jouet (essais de la commande)."""
    if not CONFIG_V2.is_file():
        pytest.skip("configuration v2 absente")
    c = {**json.loads(CONFIG_V2.read_text(encoding="utf-8")), "entropie": 7}
    chemin = tmp_path / "config-reelle.json"
    chemin.write_text(json.dumps(c), encoding="utf-8")
    for action in (["etape-a", str(tmp_path), "run", str(chemin)], ["repli-recalcul", str(tmp_path), "run", str(chemin)]):
        assert lv.main(action + ["--instant", "1800000000"]) == 2
    assert not (tmp_path / "runs").exists() and not (tmp_path / "diag").exists()


def test_CT07_garde_d_identite_avant_l_apprentissage(complet, monkeypatch):
    """CT-07 : une garde d'identité en échec arrête l'étape A **avant** l'apprentissage : aucun jeu extrait, ni `sondes-t07.json`
    ni `sondes-neuves-t07.npz` (artefact : apprentissage appelé → échec) ; cas sain : l'essai de bout en bout."""
    appris = []
    monkeypatch.setattr(sn, "apprendre", lambda *a, **k: appris.append(1))
    monkeypatch.setattr(lv1, "garde_identite", lambda *a, **k: (_ for _ in ()).throw(GardeArret("R11-arret : essai")))
    with pytest.raises(lv.ArretApresManifeste, match="R11-arret"):
        _a(complet)
    assert not appris
    assert not list((complet.racine / "diag").glob("*-t07-*/sondes-t07.json"))
    assert not list((complet.racine / "donnees").glob("*-t07-*/sondes-neuves-t07.npz"))


def test_CT09_CT10_garde_de_fin_et_R14():
    """CT-09 : réduite datée exactement de la fin de l'étape A → R14 (comme la garde de fin, `<=`). CT-10 : `VERDICT-P3BIS` avec
    réduite, G1 faux ou appui faux → nœud dès la fin de l'étape A (artefacts) ; cas sain : tout conforme → aucun code."""
    c = ga._cas_synthetique({"S": 0, "R": 1, "V": 2, "oA": 3, "fA": 4, "P": 5}, "réduite", jp.PLEINE, False)
    t = c["t"]
    r14 = ga.reserve_r14([{**o, "instant": t["fA"]} if o["mode"] == jp.REDUITE else o for o in c["journal"]], t["fA"])
    assert r14 is not None
    lignes = {k: v for k, v in c["lignes"].items() if k in (rg.SCELLEMENT_T07, rg.VERDICT_P3BIS)}
    journal = [o for o in c["journal"] if o["instant"] <= t["fA"]]
    assert ga.garde_fin_etape_a(t["fA"], lignes, journal, c["prealables"], c["decisions"], controler_appuis=True) == []
    g1_faux = {**lignes, rg.SCELLEMENT_T07: {**lignes[rg.SCELLEMENT_T07], "instant": t["V"] + 1}}
    assert ga.SCELLEMENT_APRES_VERDICT in [x for x, _ in ga.garde_fin_etape_a(t["fA"], g1_faux, journal, c["prealables"],
                                                                                 c["decisions"], controler_appuis=True)]
    mauvais = [{**o, "appui": "RENDEZ-VOUS-P3BIS-1=" + "9" * 64 + " GARDE-ADAPTEE-T07-P3BIS=" + "1" * 64} for o in journal]
    assert ga.APPUI_FAUX in [x for x, _ in ga.garde_fin_etape_a(t["fA"], lignes, mauvais, c["prealables"], c["decisions"],
                                                                 controler_appuis=True)]


@pytest.mark.xfail(strict=True, raises=jp.JournalFautif, reason="son cas sain écrit un appui « x », hors forme depuis D-3 (R-2103) ; règle des dates "
                   "rejouée aux formes exactes : tests/test_t07_journal_p3bis_d3_v1.py::test_D3_regle_des_dates_inchangee")
def test_CT11_dates_du_journal_non_decroissantes(tmp_path):
    """CT-11 : une ligne datée avant la précédente → journal hors de son format (nœud) ; cas sain : dates croissantes."""
    p = tmp_path / "j.md"
    p.write_text(ENTETE + ligne_j(jp.REFUS_OUVERTURE_P3BIS, 100, jp.REDUITE) + "\n" + ligne_j(jp.OUVERTURE_P3BIS, 200, jp.REDUITE, "x") + "\n",
                 encoding="utf-8")
    assert len(jp.lire_journal_p3bis(p)) == 2
    p.write_text(ENTETE + ligne_j(jp.OUVERTURE_P3BIS, 200, jp.REDUITE, "x") + "\n" + ligne_j(jp.REFUS_OUVERTURE_P3BIS, 100, jp.PLEINE) + "\n",
                 encoding="utf-8")
    with pytest.raises(jp.JournalFautif, match="antérieure à la ligne précédente"):
        jp.lire_journal_p3bis(p)


@pytest.mark.parametrize("contenu, motif", [
    (lambda: phrases_concepts().replace('{"format_lecture": "phrase_seule"}', '{"format_lecture": "gabarit"}'), "première ligne"),
    (lambda: "\n".join(l for l in phrases_concepts().splitlines() if "jardins" not in l) + "\n", "au moins 2"),
    (lambda: "\n".join(l for k, l in enumerate(phrases_concepts().splitlines()) if k not in (2, 3)) + "\n", "moins de deux paires"),
    (lambda: phrases_concepts().replace('"phrase_neutre": "le pot dort ici"', '"phrase_neutre": ""'), "attendu"),
])
def test_CT13_lecteur_des_phrases_des_concepts_artefacts(tmp_path, contenu, motif):
    """CT-13 : lecteur des phrases des concepts : cas sain (deux concepts, trois paires) ; format inconnu, trop peu de concepts
    (quatre exigés en mode réel), moins de deux paires, phrase vide → arrêt."""
    p = tmp_path / "c.jsonl"
    p.write_text(phrases_concepts(), encoding="utf-8")
    assert set(sn.lire_phrases_concepts(p, 2)["concepts"]) == {"chats", "jardins"}
    with pytest.raises(GardeArret, match="au moins 4"):
        sn.lire_phrases_concepts(p, 4)
    p.write_text(contenu(), encoding="utf-8")
    with pytest.raises(GardeArret, match=motif):
        sn.lire_phrases_concepts(p, 2)


def test_CT14_graines_des_cles_connues_inscrites_au_manifeste(complet):
    """CT-14 : les clés connues avant le manifeste (30 couples, sondes possibles de T7-P6, directions) sont dans le manifeste ;
    seules les clés nommées après lui (sondes choisies, lectures) sont dérivées après."""
    ra = _a(complet)
    g = json.loads((complet.racine / "runs" / ra["run_t07"] / "manifeste.json").read_text())["graines"]
    assert {"entrainement/dissimulation-lineaire-c15", "mahalanobis-egalite/domaine-mahalanobis-c23",
            "entrainement/intention-sans-cout-perceptron-c7", "plancher-concept/chats/c15", "decoupage", "temoin-p6"} <= set(g)
    derivees = _resultat(complet, ra["run_t07"], "sondes-t07.json")["sondes_neuves"]["graines_derivees_apres_manifeste"]
    assert not [k for k in derivees if k.startswith(("entrainement/", "plancher-concept/"))]


def test_CT15_ligne_de_scellement_comparee_au_preenregistrement(complet):
    """CT-15 : ligne `SCELLEMENT-T07` d'un autre chemin que le préenregistrement de la configuration → refus de la garde ; cas
    sain : même chemin, ouverture."""
    lv.ouvrir(complet.racine, complet.registre, {**complet.config, "preenregistrement": "prereg/T0.7-sondes-v0-v1.md"}, "A",
              RUN_T06, INSTANT)
    with pytest.raises(rg.RefusRegistre, match="préenregistrement de la configuration"):
        lv.ouvrir(complet.racine, complet.registre, {**complet.config, "preenregistrement": "prereg/autre.md"}, "A", RUN_T06, INSTANT + 1)


def test_CT18_prediction_partiellement_lue():
    """CT-18 : une seule des trois lectures faite → « partiellement lue », lectures nommées (jamais « confirmée »)."""
    lus = {"(i-a)": {"etat": "au-dessus"}, "temoin": {"etat": "non calculable : condition temoin absente"},
           "(ii)": {"etat": "non lue : scores de (ii) fermés par Q (S100)"}}
    x = lt._prediction_validite(lus, {"(i-a)": "au-dessus", "temoin": "au-dessus", "(ii)": "non au-dessus"})
    assert x["etat"].startswith("partiellement lue") and "temoin" in x["etat"] and "confirmée" not in x["etat"]
    tous = {**lus, "temoin": {"etat": "au-dessus"}, "(ii)": {"etat": "non au-dessus"}}
    assert lt._prediction_validite(tous, {"(i-a)": "au-dessus", "temoin": "au-dessus", "(ii)": "non au-dessus"})["etat"] == "confirmée"
