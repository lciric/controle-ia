"""Essais courts du jeu jouet v1 : cycle détecté, décroissance vérifiée, graine reproductible, identité des deux
exploitabilités (matrice et OpenSpiel). Lancer : `.venv/bin/python -m pytest -q` sur ce dossier."""
import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import jouet_meilleure_reponse_v1 as J  # noqa: E402


def _graine(cj, cd, r, racine=J.RACINE):
    return np.random.SeedSequence(entropy=racine, spawn_key=(cj, cd, r))


@pytest.mark.parametrize("jeu, periode_attendue", [("matrix_rps", 3), ("pennies_biaises", 2)])
def test_meilleure_reponse_alternee_cycle(jeu, periode_attendue):
    res = J.executer_dynamique(jeu, "br_alternee", 300, _graine(J.CODES_JEUX[jeu], 1, 0))
    assert res["periode"] == periode_attendue
    d = res["expl_dernier_defenseur"]
    assert d["etendue"] <= 1e-9                       # le dernier itéré ne décroît jamais
    assert d["max"] == pytest.approx({"matrix_rps": 1.0, "pennies_biaises": 1.2}[jeu])


@pytest.mark.parametrize("jeu", ["matrix_rps", "pennies_biaises"])
def test_jeu_fictif_decroit(jeu):
    res = J.executer_dynamique(jeu, "jeu_fictif", 2000, _graine(J.CODES_JEUX[jeu], 2, 0))
    em = res["expl_moyenne_openspiel"]
    assert em["2000"] < 0.05
    assert em["2000"] < em["200"] < em["20"]
    assert res["expl_dernier_defenseur"]["etendue"] <= 1e-9   # le dernier itéré du jeu fictif, lui, ne décroît pas


def test_jeu_fictif_openspiel_tel_quel_decroit():
    ref = J.reference_xfp("matrix_rps", 500)
    assert ref["expl_moyenne_openspiel"]["500"] < 0.05
    assert ref["expl_moyenne_openspiel"]["500"] < ref["expl_moyenne_openspiel"]["20"]


def test_graine_reproductible():
    a = J.executer_dynamique("matrix_rps", "jeu_fictif_unilateral", 200, _graine(1, 3, 0))
    b = J.executer_dynamique("matrix_rps", "jeu_fictif_unilateral", 200, _graine(1, 3, 0))
    assert a == b
    # une autre racine change au moins le premier coup ou la suite des paires (sur quelques racines)
    differents = any(J.executer_dynamique("matrix_rps", "jeu_fictif_unilateral", 200, _graine(1, 3, 0, racine=r))
                     ["paires_debut"] != a["paires_debut"] for r in (31415927, 31415928, 31415929, 31415930))
    assert differents


def test_identite_exploitabilite_matrice_openspiel():
    rng = np.random.default_rng(np.random.SeedSequence(entropy=J.RACINE, spawn_key=(9, 9, 9)))
    for jeu in ("matrix_rps", "pennies_biaises"):
        _, tb, G = J.charger_jeu(jeu)
        v, p_star, q_star = J.valeur_et_equilibre(G)
        assert J.expl_openspiel(tb, p_star, q_star) == pytest.approx(0.0, abs=1e-9)
        for _ in range(5):
            p = rng.dirichlet(np.ones(G.shape[0]))
            q = rng.dirichlet(np.ones(G.shape[1]))
            attendu = (J.expl_defenseur(G, p, v) + J.expl_attaquant(G, q, v)) / 2
            assert J.expl_openspiel(tb, p, q) == pytest.approx(attendu, abs=1e-9)


def test_periode_sain_et_sans_periode():
    assert J.periode([0, 1, 2] * 20) == 3
    assert J.periode([0, 1] * 20) == 2
    assert J.periode(list(range(40))) is None
