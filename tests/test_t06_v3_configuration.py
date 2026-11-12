"""Configuration de T0.6 v3 (C-V3-4 : clé `mahalanobis_calcul`, défaut « paquet_gele ») : cas sain et artefact (R5)."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.sondes.familles_v2 import PAQUET_GELE, PRODUIT_MATRICIEL_V2
from controle_ia.t06 import configuration_v2 as cf2
from controle_ia.t06 import configuration_v3 as cf3

RACINE = Path(__file__).resolve().parents[1]
DOSSIER = RACINE / "docs" / "notes" / "g0-deux-semaines-v1"


def _config(nom="config-t06-jouet-v4.json"):
    c = json.loads((DOSSIER / nom).read_text(encoding="utf-8"))
    for k in ("taches_evaluation", "taches_distillation"):
        if c[k] and len(c[k]["sha256"]) != 64:
            c[k]["sha256"] = "a" * 64
    return c


def test_configurations_v3_conformes_et_defaut_paquet_gele():
    j, r = _config(), _config("config-t06-reel-v1-brouillon3.json")
    cf3.exiger_config_t06_v3(j)
    cf3.exiger_config_t06_v3(r)
    assert cf3.calcul_mahalanobis(r) == PAQUET_GELE == cf3.DEFAUT_MAHALANOBIS            # la configuration réelle garde le défaut
    assert cf3.calcul_mahalanobis(j) == PAQUET_GELE
    # la v3 n'est que la v2 plus une clé : le reste de la configuration réelle est celui du brouillon 2, inchangé
    b2 = _config("config-t06-reel-v1-brouillon2.json")
    assert {k: v for k, v in r.items() if k != "mahalanobis_calcul"} == b2
    assert {k: v for k, v in j.items() if k != "mahalanobis_calcul"} == _config("config-t06-jouet-v3.json")
    cf3.exiger_config_t06_v3(dict(r, mahalanobis_calcul=PRODUIT_MATRICIEL_V2))            # permis : la sonde décisive n'est pas Mahalanobis


@pytest.mark.parametrize("modif, motif", [
    (lambda c: c.pop("mahalanobis_calcul"), "incomplète"),
    (lambda c: c.__setitem__("mahalanobis_calcul", "einsum"), "paquet_gele"),
    (lambda c: c.__setitem__("mahalanobis_calcul", None), "paquet_gele"),
    (lambda c: c.__setitem__("cle_inconnue", 1), "non lues"),
    (lambda c: c["sonde"].update({"famille": "mahalanobis"}) or c.__setitem__("mahalanobis_calcul", PRODUIT_MATRICIEL_V2), "paquet gelé est exigé"),
    (lambda c: c["calendrier"].__setitem__("dernier_jour_creation", "2026-11-17"), "précède"),
])
def test_configuration_v3_artefacts(modif, motif):
    c = _config()
    modif(c)
    with pytest.raises(GardeArret, match=motif):
        cf3.exiger_config_t06_v3(c)


def test_v2_et_v3_distinctes():
    """Une configuration v3 est refusée par la v2 (clé non lue), une configuration v2 par la v3 (clé manquante) : aucune
    valeur implicite d'un côté ni de l'autre."""
    with pytest.raises(GardeArret, match="non lues"):
        cf2.exiger_config_t06_v2(_config())
    with pytest.raises(GardeArret, match="incomplète"):
        cf3.exiger_config_t06_v3(_config("config-t06-jouet-v3.json"))
