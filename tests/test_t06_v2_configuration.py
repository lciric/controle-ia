"""Configuration de T0.6 v2 (C04, C05, C15, L04, L05, L11) et lecture v2 (C06, L05) : cas sain et artefact (R5)."""
from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.t06 import configuration_v2 as cf
from controle_ia.t06 import lecture_v2 as le
from controle_ia.t06.test_croise import AU_DESSUS, ECHEC, NON_AU_DESSUS, NON_INTERPRETABLE

RACINE = Path(__file__).resolve().parents[1]
DOSSIER = RACINE / "docs" / "notes" / "g0-deux-semaines-v1"


def _config(nom="config-t06-jouet-v3.json"):
    c = json.loads((DOSSIER / nom).read_text(encoding="utf-8"))
    for k in ("taches_evaluation", "taches_distillation"):
        if c[k] and len(c[k]["sha256"]) != 64:
            c[k]["sha256"] = "a" * 64
    return c


def test_configurations_v2_conformes():
    j, r = _config(), _config("config-t06-reel-v1-brouillon2.json")
    cf.exiger_config_t06_v2(j)
    cf.exiger_config_t06_v2(r)
    assert r["memoire_vive_min_go"] == 128 and r["offre"]["memoire_vive_min_mo"] == 128000          # C05
    assert r["carte"]["course"]["prix_max_usd_h"] == 1.30 and r["carte"]["relance"]["prix_max_usd_h"] == 4.70   # C15, L10
    assert r["calendrier"] == {"dernier_jour_creation": "2026-11-15", "fin_go_utc": "2026-11-17T00:00:00Z"}  # L11
    assert cf.fin_go_utc_s(r) == 1794873600
    assert r["distillation"]["pas_declares"] == 480 and r["distillation"]["unite_du_lot"] == "transcription"   # L04
    assert cf.pas_attendus_avant_dependance(r, 32) == 480 and cf.exiger_pas_declares(r, 32)["pas_attendus"] == 480
    assert cf.pas_de_distillation_declares(r, 160, 1600) == {"unite_du_lot": "transcription", "unites": 160, "epoques": 3, "lot": 1,
                                                             "pas": 480, "pas_declares": 480, "conforme_au_declare": True}
    assert not cf.pas_de_distillation_declares(r, 159, 1590)["conforme_au_declare"]      # une transcription exclue : écart écrit
    assert r["lecture"]["non_interpretable_si_au_dessus_seulement"] is True              # L05
    assert r["offre"]["coeurs_effectifs_min"] == 16 and r["offre"]["disque_min_go"] == 150 and r["offre"]["telechargement_max_usd_go"] == 0.05
    assert r["temoin_lexical"] is None and r["sondes_figees_p3"] is None and r["fils_test_croise"] == 16
    assert r["familles_descriptives"] == ["difference_moyennes", "lineaire", "perceptron", "attention", "mahalanobis"]
    cf.exiger_config_t06_v2(dict(r, familles_descriptives=["difference_moyennes", "lineaire", "perceptron", "attention"]))   # Mahalanobis écartée


@pytest.mark.parametrize("modif, motif", [
    (lambda c: c.__setitem__("cle_inconnue", 1), "non lues"),
    (lambda c: c.__setitem__("temoin_lexical", {"chemin": "x", "sha256": "a" * 64}), "non branché"),
    (lambda c: c.__setitem__("sondes_figees_p3", {"chemin": "x", "sha256": "a" * 64}), "non branché"),
    (lambda c: c.pop("fils_test_croise"), "incomplète"),
    (lambda c: c.__setitem__("fils_test_croise", 0), "fils_test_croise"),
    (lambda c: c["carte"].pop("relance"), "course, relance"),
    (lambda c: c["carte"]["course"].__setitem__("prix_max_usd_h", 0), "strictement positifs"),
    (lambda c: c["carte"]["course"].pop("nom_offre"), "clés"),
    (lambda c: c["calendrier"].__setitem__("fin_go_utc", "2026-11-17T00:00:00+01:00"), "UTC"),
    (lambda c: c["calendrier"].__setitem__("dernier_jour_creation", "2026-11-17"), "précède"),
    (lambda c: c["calendrier"].__setitem__("dernier_jour_creation", "demain"), "AAAA-MM-JJ"),
    (lambda c: c["lecture"].__setitem__("non_interpretable_si_au_dessus_seulement", "oui"), "booléen"),
    (lambda c: c["distillation"].__setitem__("unite_du_lot", "action"), "va avec"),
    (lambda c: c["distillation"].pop("pas_declares"), "exactement"),
    (lambda c: c["distillation"].__setitem__("pas_declares", 0), "pas_declares"),
    (lambda c: c["distillation"].__setitem__("autre", 1), "exactement"),
    (lambda c: c["offre"].pop("etiquette"), "offre : clés"),
    (lambda c: c.__setitem__("familles_descriptives", ["lineaire", "autre"]), "familles_descriptives"),
    (lambda c: c.__setitem__("familles_descriptives", ["lineaire"]), "sonde décisive"),
    (lambda c: c.__setitem__("familles_descriptives", []), "familles_descriptives"),
    (lambda c: c["offre"].__setitem__("disque_min_go", -1), "positif"),
    (lambda c: c["offre"].__setitem__("etiquette", ""), "etiquette"),
])
def test_configuration_v2_artefacts(modif, motif):
    c = _config()
    modif(c)
    with pytest.raises(GardeArret, match=motif):
        cf.exiger_config_t06_v2(c)


def test_pas_declares_plan_b_et_plan_a():
    c = _config()
    with pytest.raises(GardeArret, match="aucune création"):
        cf.exiger_pas_declares(c, 3)                          # 3 tâches × 1 épisode, lot 2 → 2 pas ≠ 1 déclaré
    c2 = copy.deepcopy(c)
    c2["decisions"]["DT-1"] = "a"
    assert cf.exiger_pas_declares(c2, 3)["plan"] == "a"       # plan (a) : vérifié au résultat seulement
    c3 = copy.deepcopy(c)
    c3["distillation"].update({"mode": "paires", "unite_du_lot": "action", "pas_declares": 2})
    cf.exiger_config_t06_v2(c3)
    assert cf.pas_attendus_avant_dependance(c3, 2) == 2       # 2 tâches × 1 épisode × T = 2 actions, lot 2 → 1 pas… × 1 époque
    assert cf.exiger_pas_declares(c3, 2)["pas_attendus"] == 2


def _jeu(bas, quantile, aire, trivial_sep=None):
    return {"bas": bas, "haut": bas + 0.1, "aire": aire, "plancher": {"quantile": quantile},
            "triviaux": {"pas": {"separation": trivial_sep}, "jetons_notes": {"separation": None}}}


def test_etat_du_jeu_v2_selon_la_regle():
    # L05 : au-dessus et trivial plus séparant → « non interprétable » sous les deux règles ; sous le plancher et trivial
    # plus séparant → « non au-dessus » si la règle ne teste qu'au-dessus, « non interprétable » sinon
    assert le.etat_du_jeu_v2(_jeu(0.8, 0.6, 0.85), True) == AU_DESSUS
    assert le.etat_du_jeu_v2(_jeu(0.8, 0.6, 0.85, 0.9), True) == NON_INTERPRETABLE
    assert le.etat_du_jeu_v2(_jeu(0.5, 0.6, 0.55, 0.9), True) == NON_AU_DESSUS
    assert le.etat_du_jeu_v2(_jeu(0.5, 0.6, 0.55, 0.9), False) == NON_INTERPRETABLE
    assert le.etat_du_jeu_v2(_jeu(0.5, 0.6, 0.55), False) == NON_AU_DESSUS
    assert le.etat_du_jeu_v2({"echec": "x"}, True) == ECHEC
    jeux = {"sens1": {"decisif": _jeu(0.5, 0.6, 0.55, 0.9), "controle": _jeu(0.8, 0.6, 0.85), "courbe": {"S50": _jeu(0.5, 0.6, 0.55, 0.9)},
                      "sondes": {0: {"nom": "s"}}},
            "sens2": {"decisif": _jeu(0.8, 0.6, 0.85, 0.9), "controle": {"echec": "x", "etat": ECHEC}},
            "descriptifs": {"lineaire-c1": {"sens1_decisif": _jeu(0.5, 0.6, 0.55, 0.9)}, "autre": {"echec": "y"}}}
    le.appliquer_regle_etat(copy.deepcopy(jeux), True)
    j1 = le.appliquer_regle_etat(copy.deepcopy(jeux), True)
    assert j1["sens1"]["decisif"]["etat"] == NON_AU_DESSUS and j1["sens1"]["courbe"]["S50"]["etat"] == NON_AU_DESSUS
    assert j1["sens2"]["decisif"]["etat"] == NON_INTERPRETABLE and j1["sens2"]["controle"]["etat"] == ECHEC
    assert j1["descriptifs"]["lineaire-c1"]["sens1_decisif"]["etat"] == NON_AU_DESSUS and "etat" not in j1["sens1"]["sondes"][0]
    j2 = le.appliquer_regle_etat(copy.deepcopy(jeux), False)
    assert j2["sens1"]["decisif"]["etat"] == NON_INTERPRETABLE and j2["descriptifs"]["lineaire-c1"]["sens1_decisif"]["etat"] == NON_INTERPRETABLE


def test_reserves_cout_par_adaptateur_et_controle_negatif():
    c = _config()
    r = {"audit_R4_cout": {"declenche": False}, "T6-10": {}}
    eff = {"actions": {"S100": 10}, "actions_lisibles": {"S100": 10},
           "exclusions_par_adaptateur": {"saboteur": {"exclues": 2, "actions": 20}, "temoin": {"exclues": 0, "actions": 20}}}
    res = le.reserves_cout_v2(r, c, eff, None)
    assert res == ["paires de distillation exclues au-delà de 5 % pour l'adaptateur saboteur (2 sur 20)"]   # C06 : dilution refusée
    eff2 = {**eff, "exclusions_par_adaptateur": {"saboteur": {"exclues": 1, "actions": 20}, "temoin": {"exclues": 1, "actions": 20}}}
    assert le.reserves_cout_v2(r, c, eff2, None) == []
    assert le.reserves_cout_v2(r, c, eff2, "non concluant") == ["contrôle négatif de la garde d'équivalence « non concluant »"]
    assert le.reserves_cout_v2(r, c, eff2, "conforme") == []
