"""Essais de `analyse_v2` (recette de W alignée sur la principale) ; même jeu synthétique aux formats de la fiche v4."""
from __future__ import annotations

import json
import subprocess

import numpy as np
import pytest

from controle_ia.agregation_r1_v4 import analyse_v2 as an
from controle_ia.agregation_r1_v4 import entrees_v1 as en
from controle_ia.gardes import GardeArret
from test_agregation_r1_v4 import PREREG_MINIMAL, jeu_synthetique


def rngs(graine=1):
    return {t: np.random.default_rng(np.random.SeedSequence(graine, spawn_key=(k,)))
            for k, t in enumerate(an.TACHES_GRAINES)}


def test_plis_cinq_de_douze():
    taches = np.array([f"t{i:02d}" for i in range(60)])
    carte = an.plis_des_taches(taches, np.random.default_rng(0))
    assert sorted(np.bincount(list(carte.values())).tolist()) == [12] * 5
    with pytest.raises(GardeArret, match="60 attendues"):
        an.plis_des_taches(taches[:55], np.random.default_rng(0))


def test_reglages_de_la_principale():
    assert an.N_PLIS == 5 and an.C_L2 == 1.0


@pytest.mark.filterwarnings("ignore::RuntimeWarning")
def test_regression_v2_sain_et_artefact():
    rng = np.random.default_rng(0)
    X = rng.normal(size=(200, 5))
    w, _ = an.regression_l2(X, (X[:, 0] > 0).astype(int))
    assert w[0] > 1
    X[0, 0] = np.nan
    with pytest.raises(GardeArret, match="non convergée"):
        an.regression_l2(X, (rng.random(200) > 0.5).astype(int))


def test_ecart_type_nul_remplace_par_un(tmp_path):
    def r(mx, mo, p3):
        a = mx["maximum"].copy()
        a[:, 1, 0] = 2.0                 # dimension constante : écart type 0 → 1, aucune division par zéro
        mx["maximum"] = a
    e = en.charger(*jeu_synthetique(tmp_path, retouche=r), largeur=32)
    el = en.eligibles(e)
    carte = an.plis_des_taches(e.tache, np.random.default_rng(0))
    s = an.scores_hors_pli(e.maximum, e, el, np.asarray([carte[t] for t in e.tache]))
    assert np.all(np.isfinite(s[el]))


def test_analyse_v2_bout_en_bout(tmp_path):
    e = en.charger(*jeu_synthetique(tmp_path, largeur=32, decalage=1.5), largeur=32)
    r = an.analyser(e, rngs(), n_tirages=300, n_permutations=300, n_tirages_descriptifs=200, repliques_porte=20)
    r2 = an.analyser(e, rngs(), n_tirages=300, n_permutations=300, n_tirages_descriptifs=200, repliques_porte=20)
    assert json.dumps(r, sort_keys=True) == json.dumps(r2, sort_keys=True)
    assert set(r["confirmatoires"]) == {"C1", "C2", "C3"}


def test_commande_decisive_v2_formats_exacts(tmp_path):
    depot = tmp_path / "depot"
    depot.mkdir()
    ch = jeu_synthetique(tmp_path, largeur=4096, decalage=3.0)
    pr = depot / "prereg.md"
    pr.write_text(PREREG_MINIMAL.format(a="0" * 64, b="1" * 64), encoding="utf-8")
    from controle_ia.scellement import sceller
    sceller(pr)
    for c in (["git", "init", "-q"], ["git", "add", "-A"],
              ["git", "-c", "user.email=e@x", "-c", "user.name=essai", "commit", "-qm", "essai"]):
        subprocess.run(c, cwd=depot, check=True)
    args = ["--racine", str(depot), "--run-id", "20261106-130000-agregation-r1-v4",
            "--activations-maximum", str(ch[0]), "--activations-moyenne", str(ch[1]), "--scores-p3", str(ch[2]),
            "--prereg", str(pr)]
    orig = an.analyser
    an.main.__globals__["analyser"] = lambda e, r, *a: orig(e, r, 200, 200, 100, 10)
    try:
        assert an.main(args) == 0
    finally:
        an.main.__globals__["analyser"] = orig
    corps = json.loads((depot / "diag" / "20261106-130000-agregation-r1-v4" / f"{an.NOM_SORTIE}.json")
                       .read_text(encoding="utf-8"))
    assert corps["resultat"]["aires_action"]["W"] > 0.7
    m = json.loads((depot / "runs" / "20261106-130000-agregation-r1-v4" / "manifeste.json").read_text(encoding="utf-8"))
    assert m["decisif"] and m["preenregistrement"]["sha256"]
    with pytest.raises(GardeArret, match="existe déjà"):
        an.main(args)
