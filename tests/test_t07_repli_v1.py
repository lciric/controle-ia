"""Essais R5 de la garde d'équivalence du repli de l'étape A de T0.7 (`src/controle_ia/t07/repli_v1.py` ; brouillon 19,
plan, point 8, repli ; « Gardes et essais R5 » : « repli du recalcul : garde d'équivalence sur activations factices (cas sain
à l'identique, artefact décalé d'un jeton → échec, comme le contrôle négatif de T0.6) »)."""
from __future__ import annotations

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.t07 import lecture_v2 as lv
from controle_ia.t07 import repli_v1 as rp

MANIFESTE = {"config": {"statistique_equivalence": "q99", "tolerance_equivalence": 0.2, "fraction_min_controle_negatif": 0.95}}


def _activations(n_actions: int = 12, couche: int = 15, d: int = 16):
    rng = np.random.default_rng(7)
    sous = {f"a{k}": rng.standard_normal((5 + k % 4, d)).astype(np.float16) for k in range(n_actions)}
    return sous, couche


def test_parametres_lus_dans_le_manifeste_jamais_en_dur():
    assert rp.parametres_equivalence(MANIFESTE) == ("q99", 0.2, 0.95)
    for faute in ({"config": {}}, {"config": {**MANIFESTE["config"], "statistique_equivalence": "moyenne"}},
                  {"config": {**MANIFESTE["config"], "tolerance_equivalence": 1.5}},
                  {"config": {**MANIFESTE["config"], "fraction_min_controle_negatif": 0}}):
        with pytest.raises(GardeArret):
            rp.parametres_equivalence(faute)


def test_garde_cas_sain_a_l_identique_et_artefact_decale_d_un_jeton():
    """Cas sain : activations recalculées égales au sous-ensemble (après passage en demi-précision) → la garde passe, contrôle
    négatif vu ; artefact : recalcul décalé d'un jeton → échec ; action manquante ou de forme autre → échec."""
    sous, c = _activations()
    stat, tol, frac = rp.parametres_equivalence(MANIFESTE)
    sain = {k: {c: v.astype(np.float32)} for k, v in sous.items()}
    r = rp.garde_equivalence(sain, sous, c, stat, tol, frac)
    assert r["actions"] == len(sous) and r["ecart_max"] == 0.0 and r["controle_negatif"]["au_dessus"] == len(sous)
    decale = {k: {c: np.roll(v.astype(np.float32), 1, axis=0)} for k, v in sous.items()}
    with pytest.raises(GardeArret, match="activations de génération ≠ passe unique"):
        rp.garde_equivalence(decale, sous, c, stat, tol, frac)
    with pytest.raises(GardeArret, match="non recalculée"):
        rp.garde_equivalence({k: v for k, v in list(sain.items())[1:]}, sous, c, stat, tol, frac)
    with pytest.raises(GardeArret, match="forme recalculée"):
        rp.garde_equivalence({**sain, "a0": {c: np.zeros((2, 16), dtype=np.float32)}}, sous, c, stat, tol, frac)
    with pytest.raises(GardeArret, match="vide"):
        rp.garde_equivalence(sain, {}, c, stat, tol, frac)


def test_garde_aveugle_au_decalage_refusee():
    """Contrôle négatif : des actions à jetons identiques rendent la garde aveugle au décalage d'un jeton → échec."""
    c = 15
    sous = {f"a{k}": np.ones((6, 8), dtype=np.float16) for k in range(5)}
    sain = {k: {c: v.astype(np.float32)} for k, v in sous.items()}
    with pytest.raises(GardeArret, match="aveugle au décalage"):
        rp.garde_equivalence(sain, sous, c, "q99", 0.2, 0.95)


def test_commande_repli_recalcul_refuse_rien_ecrit(tmp_path):
    assert lv.main(["repli-recalcul", str(tmp_path), "run", str(tmp_path / "c.json")]) == 2
    assert not any(tmp_path.iterdir())
