"""Familles de sondes v3 (C-V4-2) : essai d'égalité de Mahalanobis v2 au paquet gelé sur jetons réels (demi-précision), cas sain
et artefacts (R5)."""
from __future__ import annotations

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.sondes import familles as fam
from controle_ia.sondes import familles_v2 as fv2
from controle_ia.sondes import familles_v3 as fv3


def _sonde_et_seqs(d=12, n=40, graine=3):
    rng = np.random.default_rng(graine)
    echelle = np.where(np.arange(d) < 3, 300.0, 1.0)
    seqs = [(rng.standard_normal((int(rng.integers(8, 20)), d)) * echelle + 5.0).astype(np.float16).astype(np.float64) for _ in range(n // 4)]
    return fv2.mahalanobis_v2("s", 1, seqs), seqs


def test_jetons_reels_egaux_au_paquet_gele_et_deterministes():
    s, seqs = _sonde_et_seqs()
    j = fv3.jetons_reels(seqs, 11, 64)
    assert j.shape == (64, 12) and np.array_equal(j, fv3.jetons_reels(seqs, 11, 64))
    assert not np.array_equal(j, fv3.jetons_reels(seqs, 12, 64))
    r = fv3.verifier_egalite_jetons_reels(s, j, graine=11, actions_pool=len(seqs))
    assert r["egal"] and r["jetons"] == "reels" and r["n_jetons"] == 64 and r["ecart_relatif_max"] <= fv2.TOLERANCE_EGALITE
    pool = np.concatenate(seqs)
    assert all(any(np.array_equal(t, p) for p in pool) for t in j[:5])                    # des jetons réels (déjà en demi-précision)


def test_moins_de_jetons_que_demande_prend_tout_sans_remise():
    s, seqs = _sonde_et_seqs()
    petit = [seqs[0][:5]]
    j = fv3.jetons_reels(petit, 1, 256)
    assert j.shape == (5, 12) and len({tuple(x) for x in j}) == 5


def test_artefact_sonde_v2_alteree_est_refusee():
    """Une v2 qui s'écarterait du paquet gelé (P perturbée côté v2 seulement) est arrêtée sur jetons réels."""
    s, seqs = _sonde_et_seqs()
    j = fv3.jetons_reels(seqs, 1, 64)

    class Fausse(fv2.SondeMahalanobisV2):
        def scores_par_jeton(self, acts):
            return super().scores_par_jeton(acts) * (1 + 1e-6)

    f = Fausse(s.nom, s.couche, s.mu, s.P, s.agregation, s.famille)
    with pytest.raises(GardeArret, match="≠ paquet gelé sur 64 jetons réels"):
        fv3.verifier_egalite_jetons_reels(f, j)


@pytest.mark.parametrize("jetons, motif", [
    (np.zeros((0, 12)), "forme"), (np.zeros((4, 7)), "forme"), (np.full((4, 12), np.nan), "non fini"), (np.zeros(12), "forme")])
def test_artefacts_jetons_illisibles(jetons, motif):
    s, _ = _sonde_et_seqs()
    with pytest.raises(GardeArret, match=motif):
        fv3.verifier_egalite_jetons_reels(s, jetons)


def test_artefacts_tirage_impossible_et_sonde_du_paquet_gele():
    s, seqs = _sonde_et_seqs()
    with pytest.raises(GardeArret, match="aucune séquence"):
        fv3.jetons_reels([], 1)
    with pytest.raises(GardeArret, match="aucune séquence"):
        fv3.jetons_reels([np.zeros((0, 12))], 1)
    with pytest.raises(GardeArret, match="largeurs"):
        fv3.jetons_reels([np.ones((3, 12)), np.ones((3, 7))], 1)
    with pytest.raises(GardeArret, match="non fini"):
        fv3.jetons_reels([np.full((3, 12), 1e10)], 1)                                      # déborde la demi-précision
    gele = fam.mahalanobis("g", 1, seqs)
    with pytest.raises(GardeArret, match="Mahalanobis v2"):
        fv3.verifier_egalite_jetons_reels(gele, np.ones((4, 12)))
