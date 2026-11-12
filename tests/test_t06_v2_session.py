"""Chaîne de session de T0.6 v2 (`controle_ia.t06.session_v2`, bibliothèque standard) : dépense cumulée sur toutes les
tentatives et le téléchargement (C08), offre relue et vérifiée (C12, C15), instances du programme, calendrier (L11) ; cas
sain et artefact (R5)."""
from __future__ import annotations

import copy
import json
from datetime import date
from pathlib import Path

import pytest

from controle_ia.t06 import session_v2 as se

RACINE = Path(__file__).resolve().parents[1]
CONFIG = json.loads((RACINE / "docs" / "notes" / "g0-deux-semaines-v1" / "config-t06-reel-v1-brouillon2.json").read_text(encoding="utf-8"))
ENTETE = "| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |\n|---|---|---|---|---|---|---|---|\n"
LIGNE = "| GO-2026-11-02-28 | 2026-11-02 | calcul | T0.6 | 200 USD | 2026-11-16 | Lazar | mots |"
OFFRE = {"id": 123, "gpu_name": "A100 SXM4", "gpu_ram": 81920, "num_gpus": 1, "cpu_ram": 258000, "cpu_cores_effective": 32.0,
         "disk_space": 500.0, "dph_total": 1.1, "storage_total_cost": 0.02, "inet_down_cost": 0.03, "rentable": True,
         "machine_id": 7, "host_id": 9}


def test_depense_cumulee_v2_toutes_tentatives_et_telechargement():
    d = se.depense_cumulee_v2(1.0, 0.03, 0, 50.0, 2.0, 3600 * 10)
    assert d["cumulee_usd"] == 62.3 and d["instance_usd"] == 10.3 and not d["arret"]
    assert d["epuisement_utc_s"] == int((200 - 52) / 1.03 * 3600)            # heure d'épuisement au prix de l'offre
    assert se.depense_cumulee_v2(1.0, 0.0, 0, 150.0, 2.0, 3600 * 48)["arret"]  # 48 h + 152 ≥ 200 : la v1 aurait dit non
    assert se.depense_cumulee_v2(1.0, 0.0, 0, 199.0, 2.0, 1)["arret"] and se.depense_cumulee_v2(1.0, 0.0, 0, 199.0, 2.0, 1)["epuisement_utc_s"] == 0
    assert se.depense_cumulee_v2(1.0, 0.0, 0, 0.0, 0.0, 3600, 250.0)["arret"]           # facture plus grande
    with pytest.raises(se.GardeSession, match="illisible"):
        se.depense_cumulee_v2(1.0, 0.0, 0, "x", 2.0, 10)
    with pytest.raises(se.GardeSession, match="positif"):
        se.depense_cumulee_v2(1.0, 0.0, 0, -1, 2.0, 10)
    assert se.main(["depense", "1.0", "0.03", "0", "50", "2", "36000"]) == 0
    assert se.main(["depense", "1.0", "0", "0", "150", "2", str(3600 * 48)]) == 1


def test_offre_conforme_et_relance(tmp_path):
    r = se.verifier_offre([OFFRE], CONFIG, "course")
    assert r == {"id": 123, "prix_carte": 1.1, "prix_stockage": 0.02, "telechargement": 0.03, "telechargement_forfait_usd": 1.2,
                 "carte": "A100 SXM4 80 Go", "machine_id": 7, "host_id": 9}
    assert se.verifier_offre({"offers": [OFFRE]}, CONFIG, "course")["id"] == 123
    h200 = {**OFFRE, "gpu_name": "H200 NVL", "gpu_ram": 143000, "dph_total": 4.6}
    assert se.verifier_offre(h200, CONFIG, "relance")["carte"].startswith("H200")
    with pytest.raises(se.GardeSession, match="carte 'H200 NVL'"):
        se.verifier_offre(h200, CONFIG, "course")
    f = tmp_path / "offre.json"
    f.write_text(json.dumps([OFFRE]), encoding="utf-8")
    c = tmp_path / "config.json"
    c.write_text(json.dumps(CONFIG), encoding="utf-8")
    assert se.main(["offre", str(f), str(c), "course"]) == 0 and se.main(["offre", str(f), str(c), "relance"]) == 1


@pytest.mark.parametrize("modif, motif", [
    ({"gpu_name": "RTX 4090"}, "carte"), ({"gpu_ram": 40000}, "mémoire de carte"), ({"num_gpus": 2}, "une seule"),
    ({"cpu_ram": 64000}, "mémoire vive"), ({"cpu_cores_effective": 8}, "cœurs"), ({"disk_space": 100}, "disque"),
    ({"dph_total": 1.31}, "prix"), ({"dph_total": 0}, "prix"), ({"storage_total_cost": 0.05}, "stockage"),
    ({"inet_down_cost": 0.06}, "téléchargement"), ({"rentable": False}, "louable"), ({"id": "abc"}, "identifiant"),
    ({"cpu_ram": None}, "mémoire vive"),
])
def test_offre_artefacts(modif, motif):
    with pytest.raises(se.GardeSession, match=motif):
        se.verifier_offre([{**OFFRE, **modif}], CONFIG, "course")
    with pytest.raises(se.GardeSession, match="exactement une"):
        se.verifier_offre([OFFRE, OFFRE], CONFIG, "course")
    with pytest.raises(se.GardeSession, match="exactement une"):
        se.verifier_offre([], CONFIG, "course")


def test_instances_du_programme():
    assert se.verifier_instances([], "t06-v2") == {"instances_du_programme": 0, "total": 0}
    assert se.verifier_instances([{"id": 1, "label": "autre", "actual_status": "running", "cur_state": "running"}], "t06-v2")["total"] == 1
    with pytest.raises(se.GardeSession, match="déjà sur le compte : 5"):
        se.verifier_instances({"instances": [{"id": 5, "label": "t06-v2-x", "actual_status": "exited", "cur_state": "stopped"}]}, "t06-v2")
    with pytest.raises(se.GardeSession, match="illisible"):
        se.verifier_instances("x", "t06-v2")


def _registre(tmp_path, *lignes):
    tmp_path.mkdir(exist_ok=True)
    p = tmp_path / "go.md"
    p.write_text(ENTETE + "\n".join(lignes) + "\n", encoding="utf-8")
    return p


def test_calendrier_contre_le_registre(tmp_path):
    reg = _registre(tmp_path, LIGNE)
    r = se.verifier_calendrier(CONFIG, reg, date(2026, 11, 15))
    assert r == {"fin_go_utc_s": 1794873600, "dernier_jour_creation": "2026-11-15", "echeance_go": "2026-11-16", "jour": "2026-11-15"}
    with pytest.raises(se.GardeSession, match="dernier jour de création .* dépassé"):
        se.verifier_calendrier(CONFIG, reg, date(2026, 11, 16))
    with pytest.raises(se.GardeSession, match="validité"):
        se.verifier_calendrier(CONFIG, reg, date(2026, 11, 17))
    c = copy.deepcopy(CONFIG)
    c["calendrier"]["fin_go_utc"] = "2026-11-16T00:00:00Z"
    with pytest.raises(se.GardeSession, match="lendemain 00:00 UTC"):
        se.verifier_calendrier(c, reg, date(2026, 11, 5))
    c["calendrier"]["fin_go_utc"] = "2026-11-18T00:00:00Z"
    with pytest.raises(se.GardeSession, match="lendemain"):
        se.verifier_calendrier(c, reg, date(2026, 11, 5))
    c = copy.deepcopy(CONFIG)
    c["calendrier"]["dernier_jour_creation"] = "2026-11-17"
    with pytest.raises(se.GardeSession, match="après la fin du GO"):
        se.verifier_calendrier(c, reg, date(2026, 11, 5))
    with pytest.raises(se.GardeSession, match="sans calendrier"):
        se.verifier_calendrier({}, reg, date(2026, 11, 5))
    reg2 = _registre(tmp_path / "autre", LIGNE.replace("2026-11-16", "2026-11-20"))
    with pytest.raises(se.GardeSession, match="lendemain"):
        se.verifier_calendrier(CONFIG, reg2, date(2026, 11, 5))
    f = tmp_path / "c.json"
    f.write_text(json.dumps(CONFIG), encoding="utf-8")
    assert se.main(["calendrier", str(f), str(reg), "2026-11-05"]) == 0 and se.main(["calendrier", str(f), str(reg), "2026-11-16"]) == 1


def test_surveillance_v2_cumul(tmp_path):
    j = tmp_path / "j.txt"
    j.write_text("AMORCE 2026-11-05T10:00:00Z : commit abc\nPROGRES 2026-11-05T10:00:00Z etape=format verifie=True\n", encoding="utf-8")
    assert se.main(["surveillance", str(j), "36000", "1.0", "0.03", "0", "0", "0"]) == 0
    assert se.main(["surveillance", str(j), "36000", "1.0", "0.03", "0", "150", "2"]) == 0      # 10,3 + 152 < 200
    assert se.main(["surveillance", str(j), str(48 * 3600), "1.0", "0.0", "0", "150", "2"]) == 0  # décision ARRET écrite, code 0
