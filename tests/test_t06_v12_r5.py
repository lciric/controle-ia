"""Lanceur v10 / amorce v7 : les « Essais R5 à ajouter » de la contre-lecture Opus de la v9 (cas 1 et 2 de l'amorce, 3 de `instance_seule`, 4 du lanceur). Cas sain (v7) et
artefact (v6 : défaut reproduit) pour l'amorce ; cas sain (session v9) et artefact (session v8) pour `instance_seule`."""
from __future__ import annotations

import os
import subprocess
import sys
import time
from pathlib import Path

import pytest

import test_t06_v12_amorce as t6a
from test_t06_v12_amorce import CURL_FACTICE, ENV_DE_BASE, _distant, _lancer_amorce, bac  # noqa: F401
from controle_ia.t06 import session_v8 as s8
from controle_ia.t06 import session_v9 as s9
from controle_ia.t06.session import GardeSession

RACINE = Path(__file__).resolve().parents[1]
AMORCE6 = RACINE / "scripts" / "amorce_instance_t06_v6.sh"
AMORCE7 = RACINE / "scripts" / "amorce_instance_t06_v10.sh"


@pytest.fixture(params=["v6", "v7"])
def amorce(request, monkeypatch):
    monkeypatch.setattr(t6a, "AMORCE", AMORCE6 if request.param == "v6" else AMORCE7)
    return request.param


def _curl(tmp_path) -> dict:
    (tmp_path / "bin").mkdir(exist_ok=True)
    (tmp_path / "bin" / "curl").write_text(CURL_FACTICE, encoding="utf-8")
    (tmp_path / "bin" / "curl").chmod(0o755)
    return {"PATH": f"{tmp_path / 'bin'}:{os.environ['PATH']}", "CONTAINER_ID": "424242", "CONTAINER_API_KEY": "cle-factice", "MINUTERIE_PAS_S": "1",
            "MINUTERIE_REESSAI_S": "1", "FAUX_CURL_JOURNAL": str(tmp_path / "curl.txt")}


def _methodes(tmp_path) -> list:
    f = tmp_path / "curl.txt"
    return f.read_text(encoding="utf-8").split() if f.exists() else []


# --- cas 1 : premier démarrage après l'heure de dépense épuisée, aucun run ----------------------------------------------------------------------------
def test_r5_cas1_premier_demarrage_apres_la_depense_epuisee_seulement_delete(bac, amorce, tmp_path):
    distant = _distant(bac)
    env = {"AMORCE_ESSAI_LOCAL": "0", "DEPENSE_EPUISEE_UTC_S": str(int(time.time()) - 30), **_curl(tmp_path)}
    debut = time.time()
    code, journal, sortie, racine = _lancer_amorce(bac, distant, env_sup=env)
    methodes = _methodes(tmp_path)
    assert not (racine / "t06-fin-normale").exists() and "run :" not in sortie                       # aucun run n'a tourné
    if amorce == "v6":
        # artefact : la concurrence C08 / destruction n'a pas ici de consignation lente à gagner (aucun commit en attente) ; elle est reproduite aux cas 2 et E2-5 (commit en attente)
        assert methodes in (["DELETE"], ["DELETE", "DELETE"], ["PUT", "DELETE"]), methodes
        return
    assert code == 2 and "démarrage après l'heure de dépense épuisée" in sortie, sortie[-800:]
    assert methodes == ["DELETE"], (methodes, (racine / "t06-minuterie.log").read_text(encoding="utf-8")[-600:])
    assert time.time() - debut < 120


# --- cas 2 : run interrompu redémarré après cette heure -----------------------------------------------------------------------------------------------
def test_r5_cas2_run_interrompu_redemarre_apres_la_depense_epuisee_seulement_delete(bac, amorce, tmp_path):
    distant = _distant(bac)
    code, _, sortie, racine = _lancer_amorce(bac, distant, "a", {"FAUX_RUN": "arret"})                # run interrompu (arrêt pendant le run)
    assert code == 1 and not (racine / "t06-fin-normale").exists(), sortie[-800:]
    (racine / "t06-depense-epuisee-utc.txt").write_text(str(int(time.time()) - 30), encoding="utf-8")
    (racine / "amorce-depot" / "diag" / "en-attente").mkdir(parents=True, exist_ok=True)
    (racine / "amorce-depot" / "diag" / "en-attente" / "note.json").write_text("{}", encoding="utf-8")                 # un commit en attente : la consignation de C08 est assez longue pour que l'arrêt la devance en v6
    env = {"AMORCE_ESSAI_LOCAL": "0", "DEPENSE_EPUISEE_UTC_S": str(int(time.time()) - 30), "REFUS_ATTENTE_S": "180", **_curl(tmp_path)}
    debut = time.time()
    code2, _, sortie2, _ = _lancer_amorce(bac, distant, "a", env)
    methodes = _methodes(tmp_path)
    duree = time.time() - debut
    j = (racine / "t06-minuterie.log").read_text(encoding="utf-8") if (racine / "t06-minuterie.log").exists() else ""
    if amorce == "v6":
        # artefact : dans ce montage la v6 n'envoie pas de PUT (la minuterie voit l'ordre de destruction avant sa branche C08) ; le défaut lui-même (PUT puis perte du DELETE) est
        # reproduit, v6 contre v7, par `test_t06_v7_amorce_minuterie.py` (second démarrage avec un commit en attente à pousser)
        assert methodes in (["DELETE"], ["DELETE", "DELETE"], ["PUT", "DELETE"], ["PUT"]), methodes
        return
    assert methodes == ["DELETE"], (methodes, j[-600:])
    assert "refus annoncé" not in sortie2 and duree < 120, (duree, sortie2[-600:])                    # pas d'attente de 180 s du refus


# --- cas 3 : instance_seule ---------------------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("texte", ["error: 500 not found", "Error: 500 Not Found", '{"id": null}', '{"id": ""}', '{"id": {"x": 1}}', '[{"id": null}]', "not found",
                                   "Instance 123 not found", '{"success": false, "msg": "not found"}'])
def test_r5_cas3_instance_seule_non_concluante(texte):
    with pytest.raises(GardeSession):
        s9.instance_seule(texte, "123")


@pytest.mark.parametrize("texte", ["error 404: not found", "Error: 404 Not Found.", "404 not found", "HTTP 404: instance 123 not found", "404: no such instance", "404 Instance does not exist",
                                   '{"success": false, "status": 404, "msg": "Not Found"}', '{"error": "no such instance", "code": 404}', "Error 404: instance not found"])
def test_r5_cas3_instance_seule_introuvable_sur_404_exact(texte):
    assert s9.instance_seule(texte, "123") is False


@pytest.mark.parametrize("texte", ['{"id": 123}', '{"id": "123"}', '[{"id": 123}]', '{"instances": [{"id": 123}, {"id": 5}]}'])
def test_r5_cas3_instance_seule_presente(texte):
    assert s9.instance_seule(texte, "123") is True


def test_r5_cas3_artefact_la_session_v8_les_lisait_a_tort():
    assert s8.instance_seule("error: 500 not found", "123") is False                                  # lu comme une absence (500 pris pour un identifiant)
    assert s8.instance_seule('{"id": null}', "123") is False                                          # lu comme une absence
    assert s8.instance_seule("not found", "123") is False                                             # « not found » seul : absence en v8, non concluant en v9
