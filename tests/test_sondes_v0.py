"""Sondes v0 (T0.7) : familles, plancher apparié en covariance, aire sous la courbe et intervalles par blocs. Données
synthétiques : un axe de nuisance de grande variance, et un signal planté sur un ou deux jetons des actions positives
(le maximum ou l'attention le voient, une moyenne le diluerait). Gardes testées sur cas sain et artefact (R5)."""
from __future__ import annotations

import itertools

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.harnais.sondes import score_action
from controle_ia.sondes import evaluation as ev
from controle_ia.sondes import familles as fa

D = 12


def _donnees(graine, n=160, signal=3.0, etiquettes_aleatoires=False):
    rng = np.random.default_rng(graine)
    u = np.zeros(D)
    u[3] = 1.0                                                  # direction plantée, orthogonale à la nuisance
    seqs, y, blocs = [], [], []
    for i in range(n):
        L = int(rng.integers(4, 13))
        h = rng.standard_normal((L, D))
        h[:, 0] *= 6.0                                          # axe de nuisance de grande variance
        positif = int(rng.random() < 0.5)
        if positif and not etiquettes_aleatoires:
            k = rng.choice(L, size=min(2, L), replace=False)
            h[k] += signal * u
        seqs.append(h)
        y.append(int(rng.random() < 0.5) if etiquettes_aleatoires else positif)
        blocs.append(i // 8)                                    # 8 actions par tâche
    return seqs, np.array(y), np.array(blocs)


def _comparer(sonde, entr, test, graine=1):
    plancher = ev.plancher_apparie("p", 7, entr[0], sonde.agregation, n_sondes=60, graine=graine)
    return ev.comparer_au_plancher(sonde, plancher, test[0], test[1], test[2], n_tirages=400, graine=graine)


ENTR, TEST = _donnees(1), _donnees(2)
REG = fa.Reglages(epoques=200, pas=0.05)


@pytest.mark.parametrize("famille,agregation", [("difference_moyennes", "max"), ("lineaire", "max"),
                                                ("perceptron", "max"), ("attention", "attention"),
                                                ("lineaire", "attention")])
def test_familles_au_dessus_du_plancher_sur_signal_plante(famille, agregation):
    s = fa.entrainer(famille, f"s-{famille}", 7, ENTR[0], ENTR[1], agregation, graine=3, reglages=fa.Reglages(epoques=200))
    r = _comparer(s, ENTR, TEST)
    assert r["aire"] > 0.85 and r["au_dessus_du_plancher"], r
    assert 0.3 < r["plancher_mediane"] < 0.7


def test_mahalanobis_non_supervisee():
    s = fa.entrainer("mahalanobis", "m", 7, ENTR[0], ENTR[1], "max")
    assert s.agregation == "max"
    scores = ev.scores_actions(s, TEST[0])
    assert ev.aire_sous_courbe(scores, TEST[1]) > 0.75           # écart le long d'un axe de faible variance
    with pytest.raises(GardeArret, match="maximum seulement"):
        fa.entrainer("mahalanobis", "m", 7, ENTR[0], ENTR[1], "attention")


def test_etiquettes_aleatoires_sonde_inexistante():
    """Artefact (R5) : sans signal, la sonde entraînée ne bat pas le plancher : elle « n'existe pas »."""
    entr, test = _donnees(5, etiquettes_aleatoires=True), _donnees(6, etiquettes_aleatoires=True)
    for famille in ("difference_moyennes", "lineaire"):
        s = fa.entrainer(famille, "x", 7, entr[0], entr[1], "max", graine=3, reglages=fa.Reglages(epoques=100))
        assert not _comparer(s, entr, test)["au_dessus_du_plancher"]


def test_normalisation_repliee_dans_les_parametres():
    """Une transformation affine des activations par coordonnée ne change pas les scores d'action : la sonde rendue
    lit les activations brutes, normalisation repliée (testé pour la lecture linéaire et pour l'attention)."""
    a, c = np.linspace(0.5, 3.0, D), np.linspace(-4.0, 4.0, D)
    transformees = [h * a + c for h in ENTR[0]]
    for agregation in ("max", "attention"):
        s1 = fa.lineaire("l", 7, ENTR[0], ENTR[1], agregation, graine=4, reglages=fa.Reglages(epoques=50))
        s2 = fa.lineaire("l", 7, transformees, ENTR[1], agregation, graine=4, reglages=fa.Reglages(epoques=50))
        x1 = ev.scores_actions(s1, TEST[0])
        x2 = ev.scores_actions(s2, [h * a + c for h in TEST[0]])
        assert np.allclose(x1, x2, atol=1e-8), agregation


def test_determinisme_par_graine():
    s1 = fa.perceptron("p", 7, ENTR[0], ENTR[1], "max", graine=9, reglages=fa.Reglages(epoques=30))
    s2 = fa.perceptron("p", 7, ENTR[0], ENTR[1], "max", graine=9, reglages=fa.Reglages(epoques=30))
    s3 = fa.perceptron("p", 7, ENTR[0], ENTR[1], "max", graine=10, reglages=fa.Reglages(epoques=30))
    assert s1.empreinte() == s2.empreinte() != s3.empreinte()


def test_interface_du_harnais():
    """Les sondes rendues passent par `harnais.sondes.score_action`, qui refuse toute autre agrégation."""
    s = fa.attention("a", 7, ENTR[0], ENTR[1], graine=2, reglages=fa.Reglages(epoques=20))
    v = score_action(s, ENTR[0][0], 0, len(ENTR[0][0]))
    assert np.isfinite(v)
    with pytest.raises(GardeArret, match="max ou attention"):
        fa.entrainer("lineaire", "x", 7, ENTR[0], ENTR[1], "moyenne")
    with pytest.raises(GardeArret, match="maximum seulement"):
        fa.difference_moyennes("x", 7, ENTR[0], ENTR[1], "attention")
    with pytest.raises(GardeArret, match="attention"):
        fa.entrainer("attention", "x", 7, ENTR[0], ENTR[1], "max")


def test_gardes_des_donnees():
    with pytest.raises(GardeArret, match="deux classes"):
        fa.lineaire("x", 7, ENTR[0][:4], np.zeros(4, dtype=int))
    with pytest.raises(GardeArret, match="largeurs"):
        fa.lineaire("x", 7, [np.zeros((3, 4)), np.zeros((3, 5))], np.array([0, 1]))
    with pytest.raises(GardeArret, match="non finie"):
        fa.lineaire("x", 7, [np.full((3, 4), np.nan), np.zeros((3, 4))], np.array([0, 1]))
    with pytest.raises(GardeArret, match="famille"):
        fa.entrainer("forêt", "x", 7, ENTR[0], ENTR[1])


def test_aire_sous_la_courbe_contre_le_calcul_par_paires():
    rng = np.random.default_rng(0)
    s = rng.integers(0, 5, size=40).astype(float)                # nombreux ex aequo
    y = rng.integers(0, 2, size=40)
    pos, neg = s[y == 1], s[y == 0]
    attendu = np.mean([1.0 if a > b else 0.5 if a == b else 0.0 for a, b in itertools.product(pos, neg)])
    assert ev.aire_sous_courbe(s, y) == pytest.approx(attendu, abs=1e-12)
    with pytest.raises(GardeArret, match="deux classes"):
        ev.aire_sous_courbe(s, np.ones(40, dtype=int))


def test_intervalle_par_blocs_et_gardes():
    s = ev.scores_actions(fa.difference_moyennes("d", 7, ENTR[0], ENTR[1]), TEST[0])
    r = ev.intervalle_blocs(s, TEST[1], TEST[2], n_tirages=300, graine=1)
    assert r["bas"] <= r["aire"] <= r["haut"] and r["tirages"] + r["degeneres"] == 300
    with pytest.raises(GardeArret, match="deux blocs"):
        ev.intervalle_blocs(s, TEST[1], np.zeros_like(TEST[2]), n_tirages=10, graine=1)
    y = np.zeros(len(s), dtype=int)
    y[:8] = 1                                                    # une seule tâche porte les positifs
    with pytest.raises(GardeArret, match="déséquilibrés"):
        ev.intervalle_blocs(s, y, TEST[2], n_tirages=200, graine=1)


def test_plancher_apparie_en_covariance():
    p = ev.plancher_apparie("p", 7, ENTR[0], "max", n_sondes=2000, graine=3)
    W = np.stack([s.w for s in p])
    X = np.concatenate(ENTR[0])
    Li = np.linalg.inv(np.linalg.cholesky(np.cov(X, rowvar=False)))
    blanchie = Li @ np.cov(W, rowvar=False) @ Li.T               # w ~ N(0, Σ) ⇔ covariance blanchie ≈ identité
    assert np.allclose(blanchie, np.eye(D), atol=0.15)            # écart type d'échantillonnage ≈ 0,03
    assert all(abs(float(np.mean(s.scores_par_jeton(X)))) < 1e-8 for s in p[:5])   # centrées
    with pytest.raises(GardeArret, match="agrégations différentes"):
        ev.comparer_au_plancher(fa.attention("a", 7, ENTR[0], ENTR[1], reglages=fa.Reglages(epoques=5)), p,
                                TEST[0], TEST[1], TEST[2], 10, 1)
