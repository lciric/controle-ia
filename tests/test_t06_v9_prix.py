"""R-1692, défaut E2-2 : le stockage était compté deux fois. Valeurs réelles de l'épreuve E2 (7 novembre) : dph_total 0,3617, storage_total_cost 0,041667
(carte 0,320 + disque 0,042 ; facturé 0,362 USD/h). Cas sain (v8 : somme = dph_total) et artefact (v7 reproduit le défaut : 0,4034)."""
from __future__ import annotations

import json
import subprocess
import sys

import pytest

from controle_ia.t06 import session_v3 as s3
from controle_ia.t06 import session_v7 as s7
from controle_ia.t06 import session_v8 as s8
from controle_ia.t06.session import GardeSession
from test_t06_v6_amorce import CONFIG_E2, OFFRE_E2, RACINE

REEL = {**OFFRE_E2, "dph_total": 0.3617, "storage_total_cost": 0.041667, "id": 4242, "machine_id": 7}


def _config():                                                               # la configuration d'E2 du dépôt borne le stockage à 0,03 : les 0,0417 réels la dépassent
    c = json.loads(CONFIG_E2.read_text(encoding="utf-8"))
    c["bornes_machine" if "bornes_machine" in c else next(k for k, v in c.items() if isinstance(v, dict) and "stockage_max_usd_h" in v)]["stockage_max_usd_h"] = 0.05
    return c


def test_v7_reproduit_le_defaut():                                           # artefact : la v7 ajoute le stockage à un total qui l'inclut
    r = s7.choisir_offre([REEL], _config(), "course")
    assert r["prix_carte"] + r["prix_stockage"] == pytest.approx(0.403367, abs=1e-6)


def test_v8_somme_egale_dph_total():                                         # cas sain
    r = s8.choisir_offre([REEL], _config(), "course")
    assert r["prix_carte"] == pytest.approx(0.320033, abs=1e-6)
    assert r["prix_stockage"] == pytest.approx(0.041667, abs=1e-9)
    assert r["prix_carte"] + r["prix_stockage"] == pytest.approx(0.3617, abs=1e-9)


def test_v8_depense_une_heure_contre_facture():                              # la garde de dépense lit PC+PS : une heure ≈ 0,362 facturé
    r = s8.choisir_offre([REEL], _config(), "course")
    d = s3.depense_cumulee_v3(3.5, r["prix_carte"], r["prix_stockage"], 0, 0.0, 0.0, maintenant_s=3600)
    assert d["instance_usd"] == pytest.approx(0.3617, abs=1e-6)
    assert abs(0.3617 - 0.362) / 0.362 < 0.002
    r7 = s7.choisir_offre([REEL], _config(), "course")
    d7 = s3.depense_cumulee_v3(3.5, r7["prix_carte"], r7["prix_stockage"], 0, 0.0, 0.0, maintenant_s=3600)
    assert d7["instance_usd"] > d["instance_usd"] * 1.10                              # le défaut surestimait de plus de 10 %


def test_v8_tri_sur_dph_total_seul():                                        # deux offres : l'ordre ne dépend plus du stockage compté deux fois
    a = {**REEL, "id": 1, "machine_id": 1, "dph_total": 0.3600, "storage_total_cost": 0.0400}
    b = {**REEL, "id": 2, "machine_id": 2, "dph_total": 0.3550, "storage_total_cost": 0.0460}   # v7 : a=0.400 < b=0.401 ; v8 : b d'abord
    assert s7.choisir_offre([a, b], _config(), "course")["id"] == 1
    assert s8.choisir_offre([a, b], _config(), "course")["id"] == 2


@pytest.mark.parametrize("dph,sto", [(0.04, 0.04), (0.03, 0.04)])
def test_v8_refuse_carte_sans_prix(dph, sto):                                # artefact : dph_total ≤ stockage → refus, pas de prix négatif
    with pytest.raises(GardeSession):
        s8.choisir_offre([{**REEL, "dph_total": dph, "storage_total_cost": sto}], _config(), "course")


def test_v8_garde_cuda_conservee():
    with pytest.raises(GardeSession):
        s8.choisir_offre([{**REEL, "cuda_max_good": 12.2}], _config(), "course")


def test_v8_cli_choisir(tmp_path):
    (tmp_path / "o.json").write_text(json.dumps([REEL]), encoding="utf-8")
    (tmp_path / "c.json").write_text(json.dumps(_config()), encoding="utf-8")
    p = subprocess.run([sys.executable, "-I", "-B", "-c", f"import sys; sys.path.insert(0, '{RACINE / 'src'}'); from controle_ia.t06 import session_v8; sys.exit(session_v8.main(sys.argv[1:]))", "choisir", str(tmp_path / "o.json"), str(tmp_path / "c.json"), "course"],
                       capture_output=True, text=True)
    assert p.returncode == 0, p.stdout + p.stderr
    assert "prix_carte=0.320033" in p.stdout and "prix_stockage=0.041667" in p.stdout and "dph_total=0.361700" in p.stdout
