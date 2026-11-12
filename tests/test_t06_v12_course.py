"""Réserves de la contre-lecture de la v11 (v2) reportées à la course, chaîne v12 (lanceur v12, amorce v10) : (1) `T06_TESTS_ATTENDUS` validé (^[0-9]*$) ; (2) vérification de
GO-2026-11-06-01 à la création d'E3 bis éprouvée (mutation L2) ; (3) amorce v10 : bras B v4 par défaut et liste figée v2. Cas sains et artefacts (R5)."""
from __future__ import annotations

import re
from pathlib import Path

import pytest

from test_t06_v12_plafond_e3bis import _controles_bis, _preparer_bis, _supp
from test_t06_v12_scripts import monde5, v5  # noqa: F401
from test_t06_v12_amorce import bac, depot_session, src_epreuve  # noqa: F401

RACINE = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize("valeur", ["", "0", "7", "1878"])
def test_tests_attendus_cas_sain_vide_ou_entier(monde5, valeur):
    m = monde5
    _preparer_bis(m["src"])
    d, r = _controles_bis(m)
    assert r.returncode == 0, r.stdout + r.stderr
    r = v5(m, "creation", "auto", "course", "0", d, T06_TESTS_ATTENDUS=valeur, **_supp(m))
    assert r.returncode == 0, r.stdout
    assert f"-e TESTS_ATTENDUS={valeur}" in r.stdout.splitlines()[-1] and "PYTEST_ADDOPTS" not in r.stdout


@pytest.mark.parametrize("valeur", ["7 -e PYTEST_ADDOPTS=-x", "7;rm", "abc", "-1", "1e3", "7 ", " 7", "1.5", "$(id)"])
def test_tests_attendus_artefacts_une_valeur_non_entiere_est_refusee_avant_toute_commande(monde5, valeur):
    m = monde5
    _preparer_bis(m["src"])
    d, r = _controles_bis(m)
    assert r.returncode == 0, r.stdout + r.stderr
    r = v5(m, "creation", "auto", "course", "0", d, T06_TESTS_ATTENDUS=valeur, **_supp(m))
    assert r.returncode == 2 and "T06_TESTS_ATTENDUS illisible" in r.stdout and "create instance" not in r.stdout and "PYTEST_ADDOPTS" not in r.stdout, r.stdout


def test_l2_la_creation_d_e3_bis_reverifie_la_ligne_des_5_premiers_usd_au_registre(monde5):
    """Mutation L2 de la contre-lecture : retirer la vérification de GO-2026-11-06-01 à la création ne devait être vu par aucun essai."""
    m = monde5
    _preparer_bis(m["src"])
    d, r = _controles_bis(m)
    assert r.returncode == 0, r.stdout + r.stderr
    sup = _supp(m)
    registre = Path(sup["T06_REGISTRE_GO"])
    ok = v5(m, "creation", "auto", "course", "0", d, **sup)
    assert ok.returncode == 0, ok.stdout                                                                 # cas sain : les deux lignes présentes
    sans = Path(m["tmp"]) / "go-sans-06-01.md"
    sans.write_text("\n".join(l for l in registre.read_text(encoding="utf-8").splitlines() if not l.startswith("| GO-2026-11-06-01 ")) + "\n", encoding="utf-8")
    sup2 = {**sup, "T06_REGISTRE_GO": str(sans)}
    r = v5(m, "creation", "auto", "course", "0", d, **sup2)
    assert r.returncode == 2 and "GO-2026-11-06-01" in r.stdout and "création" in r.stdout, r.stdout


def test_amorce_v10_bras_b_v4_par_defaut_et_liste_v2():
    a = (RACINE / "scripts" / "amorce_instance_t06_v10.sh").read_text(encoding="utf-8")
    assert "${BRAS_B_MODULE:-controle_ia.audit_fuite_r1_v4.bras_b_v4}" in a and 'LISTE_TESTS="scripts/tests-cibles-t06-v2.txt"' in a
    assert "bras_b_v3}" not in a and "tests-cibles-t06-v1" not in a.split('LISTE_TESTS="')[1].split("\n")[0]
    v9 = (RACINE / "scripts" / "amorce_instance_t06_v9.sh").read_text(encoding="utf-8")
    assert "bras_b_v3}" in v9 and 'LISTE_TESTS="scripts/tests-cibles-t06-v1.txt"' in v9                       # l'amorce v9 d'E3 bis est intacte
    diff = [(x, y) for x, y in zip(v9.splitlines()[2:], a.splitlines()[3:]) if x != y]
    assert len(diff) == 3 and all("bras_b_v" in x or "tests-cibles" in x or "LISTE_SHA256" in x or "DEMARRAGE" in x for x, y in diff), [d[0][:60] for d in diff]
