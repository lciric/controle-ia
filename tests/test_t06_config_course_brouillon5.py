"""Configuration de la course, brouillon 5 : seul changement par rapport au brouillon 4 = `offre.stockage_max_usd_h` à 0,08 (valeur réelle
du 7 novembre : 0,0417 USD/h). Chargée par le validateur de configuration puis par la chaîne de session du lanceur v10 (session_v9).
Cas sains et artefacts (R5)."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from controle_ia.t06 import configuration_v4 as cf4
from controle_ia.t06 import session_v9 as s9
from controle_ia.t06.session import GardeSession
from test_t06_v6_amorce import OFFRE_E2

D = Path(__file__).resolve().parents[1] / "docs" / "notes" / "g0-deux-semaines-v1"


def _c(nom="config-t06-reel-v1-brouillon5.json"):
    return json.loads((D / nom).read_text(encoding="utf-8"))


def _offre(carte, dph, sto):
    c = _c()["carte"][carte]
    return {**OFFRE_E2, "gpu_name": c["nom_offre"], "gpu_ram": c["memoire_carte_min_mo"], "dph_total": dph, "storage_total_cost": sto,
            "cuda_max_good": 13.0, "cpu_ram": 256000, "id": 4242, "machine_id": 7}


def test_un_seul_changement_par_rapport_au_brouillon_4_et_validateur_content():
    b4, b5 = _c("config-t06-reel-v1-brouillon4.json"), _c()
    assert b4["offre"]["stockage_max_usd_h"] == 0.03 and b5["offre"]["stockage_max_usd_h"] == 0.08
    b4["offre"]["stockage_max_usd_h"] = 0.08
    assert b4 == b5
    assert b5["plafond_usd"] == 200 and b5["go_id"] == "GO-2026-11-02-28" and b5["offre"]["telechargement_max_usd_go"] == 0.05
    assert b5["carte"]["course"]["prix_max_usd_h"] == 1.3 and b5["carte"]["relance"]["prix_max_usd_h"] == 4.7
    assert b5["carte"]["relance"]["memoire_carte_min_mo"] == 140000 and not cf4.est_epreuve(b5)
    for k in ("taches_evaluation", "taches_distillation"):
        assert len(b5[k]["sha256"]) == 64
    cf4.exiger_config_t06_v4(b5)


def test_clause_de_memoire_en_go_aux_deux_cartes():
    c = _c()
    assert "gpu_ram>=78 " in s9.filtre_recherche(c, "course") and "gpu_ram>=136 " in s9.filtre_recherche(c, "relance")


@pytest.mark.parametrize("carte, dph", [("course", 0.3617), ("relance", 3.9)])
def test_offre_reelle_a_0_0417_de_stockage_acceptee(carte, dph):               # cas sain : refusée par le brouillon 4 (0,03), acceptée par le 5
    r = s9.choisir_offre([_offre(carte, dph, 0.041667)], _c(), carte)
    assert r["prix_carte"] + r["prix_stockage"] == pytest.approx(dph, abs=1e-9)
    with pytest.raises(GardeSession, match="stockage"):
        s9.choisir_offre([_offre(carte, dph, 0.041667)], _c("config-t06-reel-v1-brouillon4.json"), carte)


@pytest.mark.parametrize("carte, dph", [("course", 0.3617), ("relance", 3.9)])
def test_stockage_au_dessus_de_0_08_et_prix_au_dessus_du_plafond_refuses(carte, dph):
    with pytest.raises(GardeSession, match="stockage"):
        s9.choisir_offre([_offre(carte, dph, 0.0801)], _c(), carte)
    cher = 1.31 if carte == "course" else 4.71
    with pytest.raises(GardeSession):
        s9.choisir_offre([_offre(carte, cher, 0.041667)], _c(), carte)
