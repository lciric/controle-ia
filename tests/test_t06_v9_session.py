"""Session v8 (lanceur v9) : contre-lecture Opus de la v8 (R-1693), clause de mémoire de carte (R-1694, R-1695). Cas sain et artefact (R5)."""
from __future__ import annotations

import json
import math
import re

import pytest

from controle_ia.t06 import session_v7 as s7
from controle_ia.t06 import session_v8 as s8
from controle_ia.t06.session import GardeSession
from test_t06_v6_amorce import OFFRE_E2, RACINE

NOTES = RACINE / "docs" / "notes" / "g0-deux-semaines-v1"


def _cfg(nom):
    return json.loads((NOTES / nom).read_text(encoding="utf-8"))


# --- instance_seule ------------------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("texte", [
    '{"success": false, "error": "invalid_args", "msg": "quelque chose"}',            # objet d'erreur sans id : NON une absence (défaut de la v8)
    '{"success": false}', '{}', '[]', 'null', '',
    'Internal Server Error : instance 40404 indisponible',                           # « 404 » dans un identifiant (défaut de la v8)
    'HTTP 500 : erreur interne, instance 7404',
    '{"success": false, "status": 500, "msg": "not found upstream"}',                 # statut 500 : pas une absence même si le mot figure
    '{"success": false, "status": 500, "msg": "Not Found"}', '{"success": false, "msg": "Not Found"}',            # message exact mais pas de statut 404 : non concluant
    '<html>502 Bad Gateway</html>',
])
def test_instance_seule_reponse_non_concluante_n_est_pas_une_absence(texte):
    with pytest.raises(GardeSession):
        s8.instance_seule(texte, "40404")


@pytest.mark.parametrize("texte", [
    "not found", "Error: Instance not found.", "no such instance", "Instance 123 does not exist",
    '{"success": false, "status": 404, "msg": "Not Found"}', '{"error": "no such instance", "code": 404}',
    '[{"id": 7}]', '{"id": 7}', '{"instances": [{"id": 7}]}',                          # une liste non vide / un objet portant un AUTRE id : absente
])
def test_instance_seule_absence_etablie(texte):
    assert s8.instance_seule(texte, "123") is False


@pytest.mark.parametrize("texte", ['{"id": 123, "actual_status": "running"}', '[{"id": 123}]', '{"instances": {"id": 123}}', '{"instances": [{"id": 123}, {"id": 5}]}'])
def test_instance_seule_presente(texte):
    assert s8.instance_seule(texte, "123") is True


def test_v7_reproduit_les_defauts_de_instance_seule():                                # artefact : la v7 lit ces réponses comme des absences
    assert s7.instance_seule('{"success": false, "error": "invalid_args"}', "123") is False
    assert s7.instance_seule("Internal Server Error : instance 40404", "123") is False


def test_cli_seule_codes(tmp_path):
    import subprocess
    import sys
    cmd = [sys.executable, "-I", "-B", "-c", f"import sys; sys.path.insert(0, '{RACINE / 'src'}'); from controle_ia.t06 import session_v8; sys.exit(session_v8.main(sys.argv[1:]))", "seule"]
    for texte, code in (('{"id": 5}', 0), ("not found", 4), ('{"success": false}', 2), ("Internal Server Error 40404", 2)):
        f = tmp_path / "r.json"
        f.write_text(texte, encoding="utf-8")
        r = subprocess.run([*cmd, str(f), "5"], capture_output=True, text=True)
        assert r.returncode == code, (texte, r.stdout)
    r = subprocess.run([*cmd, str(tmp_path / "absent.json"), "5"], capture_output=True, text=True)
    assert r.returncode == 2


# --- garde CUDA : valeurs non finies -------------------------------------------------------------------------------------------------------------
def _cfg_e2():
    return _cfg("config-t06-epreuve-e2-v2.json")


@pytest.mark.parametrize("valeur", [float("nan"), float("inf"), "nan", "NaN", "inf"])
def test_cuda_non_fini_refuse(valeur):
    o = {**OFFRE_E2, "id": 1, "machine_id": 1, "dph_total": 0.35, "storage_total_cost": 0.04, "cuda_max_good": valeur}
    with pytest.raises(GardeSession):
        s8.choisir_offre([o], _cfg_e2(), "course")


def test_cuda_nan_passait_en_v7():                                                    # artefact : NaN < 13 est faux, donc la v7 acceptait
    o = {**OFFRE_E2, "id": 1, "machine_id": 1, "dph_total": 0.35, "storage_total_cost": 0.04, "cuda_max_good": float("nan")}
    assert s7.choisir_offre([o], _cfg_e2(), "course")["id"] == 1


def test_cuda_valide_accepte():
    o = {**OFFRE_E2, "id": 1, "machine_id": 1, "dph_total": 0.35, "storage_total_cost": 0.04, "cuda_max_good": 13.0}
    assert s8.choisir_offre([o], _cfg_e2(), "course")["cuda_max_good"] == 13.0


# --- clause de mémoire de carte, en Go -----------------------------------------------------------------------------------------------------------
def test_clause_gpu_ram_en_go_depuis_memoire_carte_min_mo():
    f = s8.filtre_recherche(_cfg("config-t06-epreuve-e3-v2.json"), "course")
    assert re.search(r"gpu_name=A100_SXM4 gpu_ram>=78 ", f), f                         # 80000 // 1024 = 78 (jamais 80000 : Vast compte en Go)
    assert "gpu_ram>=80000" not in f
    assert f.startswith("num_gpus=1 rentable=true gpu_name=") and "cuda_max_good>=13.0" in f


def test_filtre_v7_sans_la_clause_reproduit_le_defaut_d_e3():                         # artefact : le filtre de la v7 laissait passer les 40 Go
    assert "gpu_ram" not in s7.filtre_recherche(_cfg("config-t06-epreuve-e3-v2.json"), "course")


@pytest.mark.parametrize("mo, go", [(80000, 78), (20000, 19), (140000, 136), (1024, 1), (1025, 1)])
def test_conversion_mo_en_go(mo, go):
    c = _cfg("config-t06-epreuve-e3-v2.json")
    c["carte"]["course"]["memoire_carte_min_mo"] = mo
    assert f"gpu_ram>={go} " in s8.filtre_recherche(c, "course")


def test_la_clause_separe_40_go_et_80_go_comme_vast():
    """Modèle de la recherche de Vast : `gpu_ram` en Go. 40 960 Mo (40 Go) refusé, 81 920 Mo (80 Go) accepté ; la garde locale (Mo) reste inchangée."""
    n = int(re.search(r"gpu_ram>=(\d+)", s8.filtre_recherche(_cfg("config-t06-epreuve-e3-v2.json"), "course")).group(1))
    assert not (40960 / 1024 >= n) and (81920 / 1024 >= n)
    assert not (40960 / 1024 >= 79000)                                                # artefact : en Mo la clause ne rend rien (constat de la fille 6)
    assert not (81920 / 1024 >= 80000)


@pytest.mark.parametrize("mo", [0, -5, None, True, "80000", float("nan"), 500])
def test_memoire_carte_illisible_refusee(mo):
    c = _cfg("config-t06-epreuve-e3-v2.json")
    c["carte"]["course"]["memoire_carte_min_mo"] = mo
    with pytest.raises(GardeSession):
        s8.filtre_recherche(c, "course")


def test_garde_locale_en_mo_conservee():
    o = {**OFFRE_E2, "id": 1, "machine_id": 1, "dph_total": 0.5, "storage_total_cost": 0.04, "cuda_max_good": 13.2, "gpu_name": "A100 SXM4", "gpu_ram": 40960, "cpu_ram": 256000, "cpu_cores_effective": 32.0, "disk_space": 400}
    c = _cfg("config-t06-epreuve-e3-v2.json")
    with pytest.raises(GardeSession):
        s8.choisir_offre([o], c, "course")
    o["gpu_ram"] = 81920
    assert s8.choisir_offre([o], c, "course")["id"] == 1


# --- chemin de relance (carte H200 NVL), valeurs réelles lues par la fille 6 à 17:35Z (R-1699, R-1700) ----------------------------------------------
REEL_H200 = {**OFFRE_E2, "id": 9001, "machine_id": 31, "gpu_name": "H200 NVL", "gpu_ram": 143771, "cpu_ram": 193278, "cpu_cores_effective": 64.0,
             "disk_space": 800, "dph_total": 3.3617, "storage_total_cost": 0.041667, "reliability": 0.9906, "cuda_max_good": 13.2, "inet_down_cost": 0.02, "rentable": True}


def test_relance_filtre_et_clause_gpu_ram_en_go():
    f = s8.filtre_recherche(_cfg("config-t06-epreuve-e3-v3.json"), "relance")
    assert "gpu_name=H200_NVL gpu_ram>=136 " in f and "dph_total<=4.7" in f and "cuda_max_good>=13.0" in f and "reliability>=0.98" in f, f
    assert 143771 / 1024 >= 136 and not (80 * 1024 / 1024 >= 136)                     # une H200 NVL passe, une A100 de 80 Go non ; 140000 Mo // 1024 = 136 Go (et non 140 : arrondi vers le bas)


def test_relance_choisir_sur_les_valeurs_reelles():
    r = s8.choisir_offre([REEL_H200], _cfg("config-t06-epreuve-e3-v3.json"), "relance")
    assert r["id"] == 9001 and r["prix_carte"] + r["prix_stockage"] == pytest.approx(3.3617, abs=1e-9) and r["prix_stockage"] == pytest.approx(0.041667)


def test_relance_stockage_trop_cher_refuse():
    cher = {**REEL_H200, "id": 9002, "machine_id": 32, "dph_total": 3.30, "storage_total_cost": 0.097222}
    with pytest.raises(GardeSession, match="stockage"):
        s8.choisir_offre([cher], _cfg("config-t06-epreuve-e3-v3.json"), "relance")
    # cas sain : le rang 1 conforme est pris même si un rang moins cher a un stockage hors borne
    assert s8.choisir_offre([cher, REEL_H200], _cfg("config-t06-epreuve-e3-v3.json"), "relance")["id"] == 9001


def test_relance_carte_a100_refusee_par_la_garde_locale():
    a100 = {**REEL_H200, "id": 9003, "machine_id": 33, "gpu_name": "A100 SXM4", "gpu_ram": 81920, "dph_total": 1.2}
    with pytest.raises(GardeSession):
        s8.choisir_offre([a100], _cfg("config-t06-epreuve-e3-v3.json"), "relance")
