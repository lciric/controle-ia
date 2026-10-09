"""Agrégateurs : exactitude des formes closes, invariances, garanties locales, gardes (R5).

Ces tests valident l'instrument ; ils ne mesurent aucune puissance préenregistrée (R1).
"""
import math

import numpy as np
import pytest
from scipy import integrate, stats

from controle_ia.agregateurs import (autocorrelation_lag1, balayage, co_elevation,
                                     correlation_inter_agents, episode, max_par_action,
                                     ordre_lecture, page_cusum, somme_terminale, suites_wald_wolfowitz)
from controle_ia.agregateurs.processus_e import (log_e_bilateral, log_e_unilateral, premiere_alarme,
                                                 trajectoire_e)
from controle_ia.gardes import GardeArret

GRAINE = np.random.SeedSequence(20261004)


def _rng(k):
    return np.random.default_rng(np.random.SeedSequence(GRAINE.entropy, spawn_key=(k,)))


# --- processus e : formes closes contre intégration numérique (cas sain) ---
@pytest.mark.parametrize("S,n,sigma,rho", [(0.0, 10, 1.0, 0.3), (5.0, 50, 1.0, 0.2), (-4.0, 30, 2.0, 0.5), (12.0, 100, 0.7, 0.1)])
def test_formes_closes(S, n, sigma, rho):
    V = sigma * sigma * n
    f = lambda lam: math.exp(lam * S - lam * lam * V / 2) * stats.norm.pdf(lam, scale=rho)
    bi = integrate.quad(f, -np.inf, np.inf)[0]
    uni = 2 * integrate.quad(f, 0, np.inf)[0]
    assert math.isclose(math.log(bi), float(log_e_bilateral(S, n, sigma, rho)), rel_tol=0, abs_tol=1e-7)
    assert math.isclose(math.log(uni), float(log_e_unilateral(S, n, sigma, rho)), rel_tol=0, abs_tol=1e-6)


def test_monotonie_et_parite():
    S = np.linspace(-20, 20, 81)
    u = log_e_unilateral(S, 50, 1.0, 0.2)
    b = log_e_bilateral(S, 50, 1.0, 0.2)
    assert np.all(np.diff(u) > 0)              # unilatéral croissant en S
    assert np.allclose(b, b[::-1])             # bilatéral pair en S


def test_validite_sous_p0_et_artefact_sigma_sous_estime():
    """Garde de calibration : sous P₀, taux de fausses alarmes ≤ α (+ marge Monte-Carlo) ;
    artefact : σ sous-estimé de 30 % → dépassement détecté."""
    alpha, n_rep, N, T = 0.05, 3000, 1, 100
    rng = _rng(1)
    alarmes_ok = alarmes_mauvais = 0
    for _ in range(n_rep):
        X = rng.standard_normal((N, T))
        alarmes_ok += premiere_alarme(trajectoire_e(X, 0.0, 1.0, 0.2), alpha) is not None
        alarmes_mauvais += premiere_alarme(trajectoire_e(1.5 * X, 0.0, 1.0, 0.2), alpha) is not None
    taux_ok, taux_mauvais = alarmes_ok / n_rep, alarmes_mauvais / n_rep
    marge = 3 * math.sqrt(alpha * (1 - alpha) / n_rep)
    assert taux_ok <= alpha + marge
    assert taux_mauvais > alpha + marge


# --- indexation agnostique ---
def test_ordre_lecture_temps_d_abord():
    X = np.array([[0, 2, 4], [1, 3, 5]], float)       # N = 2, T = 3
    assert ordre_lecture(X).tolist() == [0, 1, 2, 3, 4, 5]


def test_episode_depuis_multi_ensemble_et_gardes():
    X = episode([(0, 0, 1.0), (1, 0, 2.0), (0, 1, 3.0), (1, 1, 4.0)], N=2, T=2)
    assert X.tolist() == [[1.0, 3.0], [2.0, 4.0]]
    with pytest.raises(GardeArret, match="deux fois"):
        episode([(0, 0, 1.0), (0, 0, 2.0)], N=1, T=1)
    with pytest.raises(GardeArret, match="sans score"):
        episode([(0, 0, 1.0)], N=1, T=2)
    with pytest.raises(GardeArret, match="hors"):
        episode([(3, 0, 1.0)], N=1, T=1)


@pytest.mark.parametrize("mauvais", [np.ones(5), np.ones((0, 3)), np.array([[1.0, np.nan]]), np.array([[np.inf, 0.0]])])
def test_garde_episode_artefacts(mauvais):
    with pytest.raises(GardeArret):
        max_par_action(mauvais)


# --- T1 : invariance exacte des statistiques symétriques ---
def test_invariance_par_permutation_au_bit_pres():
    rng = _rng(2)
    X = rng.standard_normal((5, 40)) * 1e3 + rng.standard_normal((5, 40)) * 1e-3
    for _ in range(20):
        P = rng.permutation(X.ravel()).reshape(X.shape)
        assert somme_terminale(P) == somme_terminale(X)
        assert max_par_action(P) == max_par_action(X)


# --- L1 : identité trajectorielle de la somme terminale ---
def test_identite_terminale():
    rng = _rng(3)
    Y = rng.standard_normal((3, 50))
    for m in (1, 7, 150):
        D = np.zeros(Y.size)
        D[rng.choice(Y.size, size=m, replace=False)] = 12.0 / m
        X = Y + D.reshape(Y.shape)
        assert math.isclose(somme_terminale(X), somme_terminale(Y) + 12.0, abs_tol=1e-9)


# --- T3 : garanties locales trajectorielles ---
def test_garantie_locale_balayage_et_page():
    rng = _rng(4)
    X = rng.standard_normal((2, 60))
    X[1, 20:25] = np.maximum(X[1, 20:25], 2.0)        # suite r = 5 de scores ≥ v = 2
    assert balayage(X, 5) >= 5 * 2.0 - 1e-12
    assert balayage(X, 3) >= 3 * 2.0 - 1e-12
    assert page_cusum(X, k=0.5) >= 5 * (2.0 - 0.5) - 1e-12


def test_garantie_locale_co_elevation():
    rng = _rng(5)
    X = rng.standard_normal((6, 30))
    X[:4, 17] = np.maximum(X[:4, 17], 1.5)             # 4 agents ≥ 1,5 au même pas
    assert co_elevation(X, 4) >= 4 * 1.5 - 1e-12


# --- statistiques d'ordre globales : sens et gardes ---
def test_autocorrelation_et_suites_sens():
    rng = _rng(6)
    iid = rng.standard_normal((1, 400))
    groupe = np.sort(iid, axis=1)                      # regroupement maximal
    assert autocorrelation_lag1(groupe) > autocorrelation_lag1(iid)
    assert suites_wald_wolfowitz(groupe) > suites_wald_wolfowitz(iid)


def test_correlation_inter_agents_sens_et_gardes():
    rng = _rng(7)
    commun = rng.standard_normal(100)
    correle = commun + 0.3 * rng.standard_normal((4, 100))
    assert correlation_inter_agents(correle) > 0.8
    with pytest.raises(GardeArret):
        correlation_inter_agents(rng.standard_normal((1, 100)))
    with pytest.raises(GardeArret, match="constante"):
        correlation_inter_agents(np.vstack([np.ones(10), rng.standard_normal(10)]))


@pytest.mark.parametrize("appel", [
    lambda X: balayage(X, 0), lambda X: balayage(X, 99), lambda X: co_elevation(X, 0),
    lambda X: co_elevation(X, 9), lambda X: autocorrelation_lag1(X[:, :2]),
    lambda X: max_par_action(X, sigma=0.0), lambda X: trajectoire_e(X, 0.0, 1.0, -0.1),
    lambda X: trajectoire_e(X, 0.0, 1.0, 0.2, cote="les deux"),
    lambda X: premiere_alarme(np.zeros(3), 1.5),
])
def test_gardes_parametres_artefacts(appel):
    X = np.random.default_rng(0).standard_normal((3, 20))
    with pytest.raises(GardeArret):
        appel(X)
