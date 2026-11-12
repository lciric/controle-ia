"""Extracteur de mesures d'épreuve (C-V4-3) : liste blanche, aucune sonde décisive lue ; clé absente = « absent » ; cas sain et
artefacts (R5)."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "extraire_mesures_epreuve_t06_v1.py"
spec = importlib.util.spec_from_file_location("extraire", SCRIPT)
ex = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ex)


def _ecrire(d: Path, nom: str, resultat: dict):
    (d / f"{nom}.json").write_text(json.dumps({"manifeste_sha256": "x", "resultat": resultat, "run_id": d.name}), encoding="utf-8")


def _branche(tmp_path, avec_reels=True, complet=True) -> Path:
    d = tmp_path / "diag" / "20261107-100000-t06-reel"
    d.mkdir(parents=True)
    ver = {"desc/mahalanobis-c7/sens1/pli0": {"egal": True, "ecart_relatif_max": 4e-15, "n_jetons": 256}}
    if avec_reels:
        ver["desc/mahalanobis-c7/sens1/pli0/reels"] = {"egal": True, "ecart_relatif_max": 7e-15, "n_jetons": 256, "jetons": "reels"}
    _ecrire(d, "episodes-t06", {"descriptifs": {"duree_s": 900.0, "memoire_pic_gio": 61.2, "dose0": 12.5}, "reglages": {"deterministe": True},
                                "disque": {"libre_octets": 10}, "morceau": {"pire_cas_action_octets": 1}, "noyau_attention": "defaut",
                                "activations_sous_ensemble": {"actions": 12, "total_notees": 100, "couche": 15, "precision": "float16", "morceaux": [{}], "reecrits": []},
                                "etats": {"dose0": {"equivalence": {"tolerance": 1e-3, "actions": ["a1"]}, "fiches": "NE_PAS_LIRE"}}})
    _ecrire(d, "distillation-t06", {"duree_s": 300.0, "pas_declares": {"pas_declares": 45}, "plan": "b", "journaux": {"saboteur": [{"perte": 1.0, "pas": 1}] * 45},
                                    "identite_dose_0": {"saboteur": {"ecart": 0.0}}, "jetons_controle": 40, "precision_adaptateurs": "float32"})
    jeux = {"sens1": {"decisif": {"aire": 0.123456789, "etat": "AIRE_SECRETE", "plancher": {"quantile": 0.987654321}}}}
    _ecrire(d, "lecture-sondes-t06", {"mahalanobis_calcul": "produit_matriciel_v2", "egalite_jetons_reels": avec_reels, "verifications_mahalanobis": ver,
                                      "durees_s": {"decisif": 10.0, "mahalanobis-c7": 33.3}, "jeux": jeux, "lecture": {"table_B": "LIGNE_SECRETE"}})
    _ecrire(d, "resume", {"duree_s": 1300.0, "episodes": 24, "actions": 240, "actions_notees": 200, "morceaux": 1, "morceaux_reecrits": 0,
                          "mahalanobis_calcul": "produit_matriciel_v2", "ligne_A": "A3", "ligne_B": "B1", "ligne_C": "C1"})
    if not complet:
        (d / "resume.json").unlink()
    return tmp_path


def test_mesures_liste_blanche_sans_aucune_sonde_decisive(tmp_path):
    m = ex.mesures(_branche(tmp_path))
    texte = json.dumps(m, ensure_ascii=False)
    for secret in ("AIRE_SECRETE", "0.123456789", "0.987654321", "LIGNE_SECRETE", "NE_PAS_LIRE", "A3", '"B1"', '"C1"'):
        assert secret not in texte, secret
    assert m["episodes"]["memoire_pic_gio"] == 61.2 and m["episodes"]["chrono"] == {"dose0": 12.5}
    assert m["equivalence_99e_centile"] == {"dose0": {"tolerance": 1e-3, "actions": ["a1"]}}
    assert m["distillation"]["pas_par_adaptateur"]["saboteur"]["pas"] == 45 and m["distillation"]["identite_dose_0"] == {"saboteur": {"ecart": 0.0}}
    assert m["mahalanobis"]["jetons_tires"]["tous_egaux"] is True and m["mahalanobis"]["jetons_reels"] == {
        "essais": 1, "tous_egaux": True, "ecart_relatif_max": 7e-15, "n_jetons_min_max": [256, 256]}
    assert m["durees_par_couple_s"] == {"decisif": 10.0, "mahalanobis-c7": 33.3} and m["resume"]["episodes"] == 24 and "ligne_A" not in m["resume"]


def test_cles_absentes_imprimees_absent_et_artefacts(tmp_path):
    m = ex.mesures(_branche(tmp_path / "a", avec_reels=False, complet=False))
    assert m["resume"]["episodes"] == "absent" and m["mahalanobis"]["jetons_reels"]["tous_egaux"] == "absent" and m["mahalanobis"]["egalite_jetons_reels"] is False
    with pytest.raises(SystemExit, match="0 trouvé"):
        ex.mesures(tmp_path / "vide")
    b = _branche(tmp_path / "b")
    (b / "diag" / "20261107-110000-t06-reel").mkdir()
    with pytest.raises(SystemExit, match="2 trouvé"):
        ex.mesures(b)
