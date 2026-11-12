"""Configuration de T0.6 v4 (C-V4-2 : clé `egalite_jetons_reels`, booléen sans valeur implicite) et configuration réelle du
brouillon 4 (R-1624 : `mahalanobis_calcul = produit_matriciel_v2`, `familles_descriptives` inchangées) : cas sain et artefact (R5)."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.sondes.familles_v2 import PAQUET_GELE, PRODUIT_MATRICIEL_V2
from controle_ia.t06 import configuration_v3 as cf3
from controle_ia.t06 import configuration_v4 as cf4

DOSSIER = Path(__file__).resolve().parents[1] / "docs" / "notes" / "g0-deux-semaines-v1"


def _config(nom="config-t06-jouet-v5.json"):
    c = json.loads((DOSSIER / nom).read_text(encoding="utf-8"))
    for k in ("taches_evaluation", "taches_distillation"):
        if c[k] and len(c[k]["sha256"]) != 64:
            c[k]["sha256"] = "a" * 64
    return c


def test_configurations_v4_conformes_reelle_en_produit_matriciel_et_jetons_reels():
    j, r = _config(), _config("config-t06-reel-v1-brouillon4.json")
    cf4.exiger_config_t06_v4(j)
    cf4.exiger_config_t06_v4(r)
    assert cf3.calcul_mahalanobis(r) == PRODUIT_MATRICIEL_V2 and cf4.jetons_reels_voulus(r) is True       # R-1624, C-V4-2
    assert cf3.calcul_mahalanobis(j) == PAQUET_GELE and cf4.jetons_reels_voulus(j) is False
    b3 = _config("config-t06-reel-v1-brouillon3.json")                       # le reste est celui du brouillon 3, inchangé
    assert {k: v for k, v in r.items() if k not in ("mahalanobis_calcul", "egalite_jetons_reels")} == {k: v for k, v in b3.items() if k != "mahalanobis_calcul"}
    assert r["familles_descriptives"] == b3["familles_descriptives"] and "mahalanobis" in r["familles_descriptives"]
    assert {k: v for k, v in j.items() if k != "egalite_jetons_reels"} == _config("config-t06-jouet-v4.json")


@pytest.mark.parametrize("modif, motif", [
    (lambda c: c.pop("egalite_jetons_reels"), "incomplète"),
    (lambda c: c.__setitem__("egalite_jetons_reels", "oui"), "booléen"),
    (lambda c: c.__setitem__("egalite_jetons_reels", 1), "booléen"),
    (lambda c: c.__setitem__("egalite_jetons_reels", True), "paquet gelé"),                # vrai sous le paquet gelé : refusé, pas ignoré
    (lambda c: c.__setitem__("cle_inconnue", 1), "non lues"),
    (lambda c: c.__setitem__("mahalanobis_calcul", "einsum"), "paquet_gele"),
])
def test_configuration_v4_artefacts(modif, motif):
    c = _config()
    modif(c)
    with pytest.raises(GardeArret, match=motif):
        cf4.exiger_config_t06_v4(c)


def test_v3_et_v4_distinctes():
    """Une configuration v4 est refusée par la v3 (clé non lue), une configuration v3 par la v4 (clé manquante)."""
    with pytest.raises(GardeArret, match="non lues"):
        cf3.exiger_config_t06_v3(_config())
    with pytest.raises(GardeArret, match="incomplète"):
        cf4.exiger_config_t06_v4(_config("config-t06-jouet-v4.json"))


# ---- C-V4-3 : configurations des épreuves à blanc E2 et E3 (GO-2026-11-06-01) ----------------------------------------------
def test_configurations_d_epreuve_conformes_et_artefacts():
    e2, e3 = _config("config-t06-epreuve-e2-v1.json"), _config("config-t06-epreuve-e3-v1.json")
    cf4.exiger_config_t06_v4(e2)
    cf4.exiger_config_t06_v4(e3)
    assert cf4.est_epreuve(e2) and cf4.est_epreuve(e3) and not cf4.est_epreuve(_config("config-t06-reel-v1-brouillon4.json"))
    assert (e2["plafond_usd"], e3["plafond_usd"]) == (1.5, 3.5) and e2["go_id"] == e3["go_id"] == cf4.GO_EPREUVE
    assert e2["mode"] == "jouet" and e3["mode"] == "reel" and e3["offre"]["etiquette"] == "t06-e3" and e2["offre"]["disque_min_go"] == 150
    assert e3["mahalanobis_calcul"] == PRODUIT_MATRICIEL_V2 and e3["egalite_jetons_reels"] is True            # E3 joue C-V4-2
    for modif, motif in ((lambda c: c.__setitem__("plafond_usd", 4.0), "attendus pour GO-2026-11-06-01"),
                         (lambda c: c.__setitem__("plafond_usd", 200), "attendus pour GO-2026-11-06-01"),
                         (lambda c: c.__setitem__("plafond_usd", True), "attendus pour GO-2026-11-06-01"),
                         (lambda c: c.__setitem__("T", 0), None), (lambda c: c["calendrier"].__setitem__("dernier_jour_creation", "2026-11-12"), "précède")):
        c = _config("config-t06-epreuve-e3-v1.json")
        modif(c)
        with pytest.raises(GardeArret, match=motif):
            cf4.exiger_config_t06_v4(c)
    c = _config("config-t06-reel-v1-brouillon4.json")                           # la course garde GO-2026-11-02-28 et 200 USD
    c["plafond_usd"] = 1.5
    with pytest.raises(GardeArret, match="200"):
        cf4.exiger_config_t06_v4(c)


def test_lanceur_v4_r1_seule_l_epreuve_tourne_en_reel_sans_preenregistrement(tmp_path):
    from controle_ia.t06 import lanceur_v4 as la4
    with pytest.raises(GardeArret, match="R1 interdit de lancer"):
        la4.executer(_config("config-t06-reel-v1-brouillon4.json"), tmp_path, "r", None)           # la course sans préenregistrement : refusée
    with pytest.raises(GardeArret, match="n'est jamais décisive"):
        la4.executer(_config("config-t06-epreuve-e3-v1.json"), tmp_path, "r", "prereg/x.md")        # une épreuve avec un préenregistrement : refusée
    with pytest.raises(Exception) as e:                                                              # l'épreuve passe le garde R1 (échoue plus loin : tâches absentes)
        la4.executer(_config("config-t06-epreuve-e3-v1.json"), tmp_path, "r", None)
    assert "R1 interdit" not in str(e.value)
