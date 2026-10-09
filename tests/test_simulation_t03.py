"""Simulation de T0.3 : instrument seulement (R1). Aucun de ces tests ne calcule une cellule de la
grille décisive (`prereg/T0.3-grille-v2.json`, qui remplace la v1) : tailles, horizons, budgets et graines diffèrent.

Couvre : équivalence lots ↔ références scalaires, séries ↔ lots, invariances exactes (T1, L1),
attaques (positions, préservation du multi-ensemble, domination T4, suite intacte en T3),
calibrage (Monte-Carlo, conforme, exact, ρ), lois, lecture gelée, gardes (cas sain + artefact, R5),
et une chaîne complète sur une mini-grille (manifeste → blocs → lecture → scellement).
"""
import copy
import json
import math
import subprocess
from pathlib import Path

import numpy as np
import pytest
from scipy import stats

from conftest import committer
from controle_ia.agregateurs import (autocorrelation_lag1, balayage, balayage_multi, co_elevation,
                                     correlation_inter_agents, detecteur_e, dispersion_agents, max_par_action,
                                     page_cusum, somme_terminale, suites_wald_wolfowitz)
from controle_ia.agregateurs.processus_e import trajectoire_e
from controle_ia.gardes import GardeArret
from controle_ia.simulation_t03 import attaques as att
from controle_ia.simulation_t03 import blocs as B
from controle_ia.simulation_t03 import calibrage as cal
from controle_ia.simulation_t03 import lecture as LEC
from controle_ia.simulation_t03 import lots as L
from controle_ia.simulation_t03.lois import facteur_variance_ar1, marginale, tirer

GRAINE = np.random.SeedSequence(77007700)


def _rng(k):
    return np.random.default_rng(np.random.SeedSequence(GRAINE.entropy, spawn_key=(k,)))


# --- équivalence avec les références scalaires ---
@pytest.mark.parametrize("N,T", [(1, 30), (3, 12)])
def test_lots_egaux_aux_references(N, T):
    Xb = _rng(1).standard_normal((40, N, T))
    rho_u, rho_b = 0.21, 0.27
    refs = {
        "somme": (L.lot_somme(Xb), lambda X: somme_terminale(X)),
        "max": (L.lot_max(Xb), lambda X: max_par_action(X)),
        "glissante_5": (L.lot_glissante(Xb, 5), lambda X: balayage(X, 5)),
        "balayage_multi": (L.lot_balayage_multi(Xb), lambda X: balayage_multi(X)),
        "page": (L.lot_page(Xb), lambda X: page_cusum(X, 0.5)),
        "detecteur_e": (L.lot_detecteur_e(Xb), lambda X: detecteur_e(X)),
        "autocorr": (L.lot_autocorr(Xb), lambda X: autocorrelation_lag1(X)),
        "autocorr_abs": (L.lot_autocorr(Xb, True), lambda X: autocorrelation_lag1(X, absolue=True)),
        "suites": (L.lot_suites(Xb), lambda X: suites_wald_wolfowitz(X)),
        "e_unilat": (L.lot_e_max(Xb, rho_u, "unilateral"),
                     lambda X: float(np.max(trajectoire_e(X, 0.0, 1.0, rho_u, "unilateral")))),
        "e_bilat": (L.lot_e_max(Xb, rho_b, "bilateral"),
                    lambda X: float(np.max(trajectoire_e(X, 0.0, 1.0, rho_b, "bilateral")))),
    }
    if N > 1:
        refs["co_elevation_2"] = (L.lot_co_elevation(Xb, 2), lambda X: co_elevation(X, 2))
        refs["correlation_agents"] = (L.lot_correlation_agents(Xb), lambda X: correlation_inter_agents(X))
        mus = np.linspace(-0.5, 0.5, N)
        refs["dispersion_agents"] = (L.lot_dispersion_agents(Xb, mus), lambda X: dispersion_agents(X, mus))
    for nom, (v, f) in refs.items():
        ref = np.array([f(Xb[i]) for i in range(Xb.shape[0])])
        assert np.allclose(v, ref, rtol=1e-11, atol=1e-11), nom


def test_suites_avec_ex_aequo_et_cas_degenere():
    Xb = np.round(_rng(2).standard_normal((30, 2, 15)), 1)       # ex aequo à la médiane
    Xb[0, 0, :] = 1.0                                             # série constante : z = 0
    ref = np.array([suites_wald_wolfowitz(Xb[i]) for i in range(30)])
    assert np.allclose(L.lot_suites(Xb), ref, atol=1e-12)


def test_series_coherentes_avec_les_lots():
    x = _rng(3).standard_normal((25, 60))
    Xb = L.depuis_ordre(x, 1, 60)
    assert np.allclose(L.serie_page(x).max(axis=1), L.lot_page(Xb))
    assert np.allclose(L.serie_detecteur_e(x).max(axis=1), L.lot_detecteur_e(Xb))
    assert np.allclose(L.serie_glissante(x, 10).max(axis=1), L.lot_glissante(Xb, 10))
    assert np.allclose(L.serie_balayage_multi(x).max(axis=1), L.lot_balayage_multi(Xb))
    f = L.premiere_alarme(np.array([[0.0, 2.0, 3.0], [0.0, 0.0, 0.0]]), 1.5)
    assert f.tolist() == [1, -1]


def test_ordre_de_lecture_aller_retour():
    Xb = _rng(4).standard_normal((3, 4, 5))
    x = L.ordre(Xb)
    assert x[0, 1] == Xb[0, 1, 0] and x[0, 4] == Xb[0, 0, 1]
    assert np.array_equal(L.depuis_ordre(x, 4, 5), Xb)


def test_gardes_des_lots():
    with pytest.raises(GardeArret):
        L.lot_somme(np.zeros((2, 3)))
    with pytest.raises(GardeArret):
        L.lot_max(np.full((2, 1, 3), np.nan))
    with pytest.raises(GardeArret):
        L.lot_glissante(np.zeros((2, 1, 3)), 4)
    with pytest.raises(GardeArret):
        L.lot_correlation_agents(np.zeros((2, 1, 5)))


# --- invariances exactes ---
def test_T1_invariance_au_bit_pres():
    x = _rng(5).standard_normal((50, 40))
    xp = att.rebrassage(x, _rng(6))
    for f in (L.lot_somme, L.lot_max, lambda X: L.lot_e_terminal(X, 0.2)):
        assert np.array_equal(f(L.depuis_ordre(x, 1, 40)), f(L.depuis_ordre(xp, 1, 40)))
        assert np.array_equal(f(L.depuis_ordre(x, 4, 10)), f(L.depuis_ordre(att.tri_croissant(x), 4, 10)))


@pytest.mark.parametrize("schema", att.SCHEMAS)
def test_L1_identite_terminale_et_positions(schema):
    N, T, R, m, Bv = 3, 12, 60, 6, 7.5
    g = _rng(7)
    y = g.standard_normal((R, N * T))
    P = att.positions(schema, m, N, T, R, g, y)
    assert P.shape == (R, m) and P.min() >= 0 and P.max() < N * T
    assert np.all(np.diff(np.sort(P, axis=1), axis=1) > 0)
    for genre in ("egaux", "dirichlet"):
        d = att.decalages(genre, m, Bv, R, g)
        assert np.allclose(d.sum(axis=1), Bv)
        x = att.appliquer_decalages(y, P, d)
        assert np.allclose(L.lot_somme(L.depuis_ordre(x, N, T)) - L.lot_somme(L.depuis_ordre(y, N, T)), Bv, atol=1e-10)
    if schema == "un_agent":
        assert np.all(P % N == 0)
    if schema == "reparti":
        comptes = np.stack([(P % N == i).sum(axis=1) for i in range(N)], axis=1)
        assert np.all(comptes == m // N)


def test_positions_gardes():
    g = _rng(8)
    with pytest.raises(GardeArret):
        att.positions("un_agent", 13, 3, 12, 5, g)
    with pytest.raises(GardeArret):
        att.positions("adaptatif", 3, 1, 10, 5, g)
    with pytest.raises(GardeArret):
        att.appliquer_decalages(np.zeros((1, 5)), np.array([[1, 1]]), 1.0)


# --- classe C ---
def _meme_multiensemble(a, b):
    return np.array_equal(np.sort(a, axis=1), np.sort(b, axis=1))


def test_classe_C_preserve_le_multiensemble_et_T4_domine():
    g = _rng(9)
    y = g.standard_normal((80, 50))
    for x in (att.tri_croissant(y), att.top_r_a_la_fin(y, 7), att.bloc_top_r(y, 5, g)[0], att.rebrassage(y, g)):
        assert _meme_multiensemble(x, y)
    for x in (att.tri_croissant(y), att.top_r_a_la_fin(y, 7)):     # sommes partielles dominées (T4)
        assert np.all(np.cumsum(x, axis=1) <= np.cumsum(y, axis=1) + 1e-12)
    xf = att.top_r_a_la_fin(y, 7)
    assert np.array_equal(np.sort(xf[:, -7:], axis=1), np.sort(y, axis=1)[:, -7:])
    Yb = g.standard_normal((10, 3, 8))
    Xi = att.rebrassage_intra_agent(Yb, g)
    assert np.array_equal(np.sort(Xi, axis=2), np.sort(Yb, axis=2))


def test_bloc_top_r_et_appariement_adaptatif():
    g = _rng(10)
    y = g.standard_normal((200, 60))
    x, debut = att.bloc_top_r(y, 5, g)
    bloc = np.stack([x[i, debut[i]:debut[i] + 5] for i in range(200)])
    assert np.array_equal(np.sort(bloc, axis=1), np.sort(y, axis=1)[:, -5:])
    for cible in ("autocorr", "suites"):
        xa, ecart = att.apparier(x, debut, 5, cible, g, 1500)
        assert _meme_multiensemble(xa, y)
        assert all(np.array_equal(xa[i, debut[i]:debut[i] + 5], x[i, debut[i]:debut[i] + 5]) for i in range(200))
        Z = xa - xa.mean(axis=1, keepdims=True)
        if cible == "autocorr":                                   # écart final cohérent avec l'état
            A = (Z[:, :-1] * Z[:, 1:]).sum(axis=1)
            assert np.median(np.abs(ecart) / (Z * Z).sum(axis=1)) < 0.01
        else:
            med = np.median(Z, axis=1, keepdims=True)
            A = ((Z > med)[:, 1:] != (Z > med)[:, :-1]).sum(axis=1)
            assert np.median(np.abs(ecart)) <= 2
        assert A.shape == (200,)


def test_co_elevation_top():
    g = _rng(11)
    Y = g.standard_normal((50, 4, 9))
    X, pas = att.co_elevation_top(Y, 3, g)
    assert _meme_multiensemble(L.ordre(X), L.ordre(Y))
    v3 = np.sort(L.ordre(Y), axis=1)[:, -3]
    assert np.all(L.lot_co_elevation(X, 3) >= 3 * v3 - 1e-12)
    for i in range(50):
        assert np.sum(X[i, :, pas[i]] >= v3[i]) >= 3


# --- calibrage ---
def test_seuil_mc_continu_et_discret():
    v = _rng(12).standard_normal(100000)
    t = cal.seuil_mc(v, 0.05)
    assert (v >= t).mean() == 0.05
    d = np.repeat(np.arange(10.0), 1000)                       # discret : conservateur
    t = cal.seuil_mc(d, 0.05)
    assert (d >= t).mean() <= 0.05
    with pytest.raises(GardeArret):
        cal.seuil_mc(np.array([1.0, np.nan]), 0.05)
    with pytest.raises(GardeArret):
        cal.seuil_mc(v, 1.5)


def test_conforme_rang_et_taux():
    assert cal.rang_conforme(1000, 0.05) == 951
    assert math.isclose(cal.taux_conforme(1000, 0.05), 1 - 951 / 1001)
    assert cal.rang_conforme(999, 0.05) == 950
    v = np.arange(1.0, 1001.0)
    assert cal.seuil_conforme(v, 0.05) == 951.0
    assert cal.seuil_conforme(np.arange(1.0, 10.0), 0.05) == math.inf


def test_conforme_valide_sous_dependance():
    """Le calibrage conforme sur épisodes entiers tient α même sous effet épisode (artefact pour Ville)."""
    g = _rng(13)
    loi = {"type": "effet_episode", "tau": 0.3, "N": 1, "T": 30}
    taux = []
    for _ in range(40):
        c = cal.seuil_conforme(L.lot_somme(tirer(g, 200, loi)), 0.05)
        taux.append((L.lot_somme(tirer(g, 200, loi)) >= c).mean())
    assert abs(np.mean(taux) - cal.taux_conforme(200, 0.05)) < 4 * np.std(taux) / math.sqrt(40) + 0.005


def test_seuils_exacts_et_formes_closes():
    c = cal.seuil_max_exact(0.05, 200)
    assert math.isclose(stats.norm.cdf(c) ** 200, 0.95, rel_tol=1e-12)
    assert math.isclose(cal.seuil_somme_exact(0.05, 100), stats.norm.isf(0.05) * 10)
    assert math.isclose(cal.puissance_max(0.05, 200, 0.0, 10), 0.05, rel_tol=1e-9)
    assert math.isclose(cal.puissance_somme(0.05, 100, 0.0), 0.05, rel_tol=1e-12)
    p = [cal.puissance_max(0.05, 200, 20.0, m) for m in (1, 2, 5, 10, 50, 200)]
    assert all(a >= b for a, b in zip(p, p[1:])) and p[-1] > 0.05
    assert math.isclose(cal.rejet_somme_sous_variance(0.05, 1.0), 0.05, rel_tol=1e-12)


def test_rho_optimal_minimise_la_frontiere():
    for cote in ("unilateral", "bilateral"):
        rho, s = cal.rho_optimal(150, 0.05, cote)
        assert s <= cal.frontiere(150, rho * 1.2, 0.05, cote) and s <= cal.frontiere(150, rho / 1.2, 0.05, cote)


def test_facteur_variance_ar1_exact():
    for phi in (-0.5, 0.3, 0.9):
        n = 37
        exact = 1 + 2 * sum((1 - h / n) * phi ** h for h in range(1, n))
        assert math.isclose(facteur_variance_ar1(phi, n), exact, rel_tol=1e-12)


# --- lois ---
@pytest.mark.parametrize("nom", ["gauss", "exp", "student5", "gumbel"])
def test_marginales_standardisees_et_monotones(nom):
    Z = _rng(14).standard_normal(400000)
    X = marginale(Z, nom)
    assert abs(X.mean()) < 0.01 and abs(X.var() - 1) < 0.03
    o = np.argsort(Z)
    assert np.all(np.diff(X[o]) >= 0)


def test_lois_dependance_et_gardes():
    g = _rng(15)
    X = tirer(g, 2000, {"type": "ar1", "phi": 0.6, "N": 2, "T": 50})
    r = (X[:, :, :-1] * X[:, :, 1:]).mean()
    assert abs(r - 0.6) < 0.02 and abs(X.var() - 1) < 0.03
    X = tirer(g, 4000, {"type": "equicorrelation", "c": 0.4, "N": 3, "T": 20})
    assert abs((X[:, 0, :] * X[:, 1, :]).mean() - 0.4) < 0.02
    for loi in ({"type": "ar1", "phi": 1.0, "N": 1, "T": 5}, {"type": "inconnue", "N": 1, "T": 5},
                {"type": "moyennes", "mus": [0.0], "N": 2, "T": 5}):
        with pytest.raises(GardeArret):
            tirer(g, 3, loi)


# --- lecture gelée ---
def test_criteres_de_lecture():
    assert LEC.egal(0.05, 20000, 0.05, 100000)[0] == "conforme"
    assert LEC.egal(0.08, 20000, 0.05, 100000)[0] == "contraire"
    assert LEC.au_dessus(0.08, 20000, 0.05, 100000)[0] == "conforme"
    assert LEC.au_dessus(0.051, 20000, 0.05, 100000)[0] == "non concluant"
    assert LEC.au_dessus(0.02, 20000, 0.05, 100000)[0] == "contraire"
    assert LEC.en_dessous(0.02, 20000, 0.05, 100000)[0] == "conforme"
    assert LEC.au_plus(0.051, 20000, 0.05, 100000)[0] == "conforme"
    assert LEC.theorie(0.5, 20000, 0.5)[0] == "conforme" and LEC.theorie(0.52, 20000, 0.5)[0] == "contraire"
    assert LEC.au_moins(0.995, 20000, 0.99)[0] == "conforme" and LEC.au_moins(0.95, 20000, 0.99)[0] == "contraire"
    assert LEC.trajectoriel(0)[0] == "conforme" and LEC.trajectoriel(1)[0] == "contraire"
    assert LEC.verdict([{"etat": "conforme"}, {"etat": "conforme"}]) == "confirmée"
    assert LEC.verdict([{"etat": "conforme"}, {"etat": "non concluant"}]) == "non concluante"
    assert LEC.verdict([{"etat": "contraire"}, {"etat": "conforme"}]) == "réfutée"


def test_fusion_de_replication():
    principale = {"predictions": {"P2.1": {"verdict": "réfutée", "cellules": [
        {"nom": "a", "etat": "contraire", "genre": "statistique"},
        {"nom": "b", "etat": "contraire", "genre": "statistique"},
        {"nom": "c", "etat": "contraire", "genre": "trajectoriel"},
        {"nom": "d", "etat": "conforme", "genre": "statistique"}]}}}
    rep = {"predictions": {"P2.1": {"cellules": [{"nom": "a", "etat": "conforme"}, {"nom": "b", "etat": "contraire"},
                                                  {"nom": "c", "etat": "conforme"}]}}}
    f = LEC.fusionner(principale, rep)
    etats = {c["nom"]: c["etat"] for c in f["predictions"]["P2.1"]["cellules"]}
    assert etats == {"a": "non concluant", "b": "contraire", "c": "contraire", "d": "conforme"}
    # une violation trajectorielle observée en réplication compte, même sur une cellule conforme
    principale["predictions"]["P7.1"] = {"verdict": "confirmée", "cellules": [
        {"nom": "t", "etat": "conforme", "genre": "trajectoriel"}]}
    rep["predictions"]["P7.1"] = {"cellules": [{"nom": "t", "etat": "contraire", "genre": "trajectoriel"}]}
    f = LEC.fusionner(principale, rep)
    assert f["predictions"]["P7.1"]["verdict"] == "réfutée" and f["predictions"]["P7.1"]["a_auditer"] == ["t"]
    assert f["predictions"]["P2.1"]["verdict"] == "réfutée"
    assert principale["predictions"]["P2.1"]["cellules"][0]["etat"] == "contraire"   # pas d'effet de bord
    assert f["predictions"]["P2.1"]["a_repliquer"] == [] and f["predictions"]["P2.1"]["repliquees"] == ["a", "b"]


def test_garde_p0_saine_et_artefact():
    res = {"cfg": "x", "garde": True, "R0": 100000, "R_cal": 100000, "garde_exclus": [],
           "alarmes_p0": {"somme": 5000, "page": 5050, "e_unilat_ville": 1700, "suites": 3600},
           "genres": {"somme": "exact", "page": "mc", "e_unilat_ville": "ville", "suites": "mc_discret"}}
    assert B.garde_p0(res, 0.05, 4.0) == []
    entre = copy.deepcopy(res)                    # 0,0533 : entre l'ancienne borne (0,05276) et la nouvelle (0,05390)
    entre["alarmes_p0"]["suites"] = 5330
    assert B.garde_p0(entre, 0.05, 4.0) == []
    entre["alarmes_p0"]["suites"] = 5450
    assert len(B.garde_p0(entre, 0.05, 4.0)) == 1
    mauvais = copy.deepcopy(res)
    mauvais["alarmes_p0"].update({"somme": 6000, "page": 4000, "e_unilat_ville": 6000, "suites": 6000})
    assert len(B.garde_p0(mauvais, 0.05, 4.0)) == 4
    mauvais["garde_exclus"] = ["e_unilat_ville"]
    assert len(B.garde_p0(mauvais, 0.05, 4.0)) == 3


# --- chaîne complète sur une mini-grille (non décisive) ---
def _mini_grille():
    g = lambda N, T, marg="gauss": {"type": "iid", "marginale": marg, "N": N, "T": T}
    P1 = ["somme", "somme_bilat", "max", "glissante_5", "glissante_10", "balayage_multi", "page", "detecteur_e",
          "e_unilat_ville", "e_unilat_cal", "e_bilat_ville", "e_terminal_ville", "autocorr", "autocorr_abs", "suites"]
    PN = P1 + ["co_elevation_2", "co_elevation_3", "co_elevation_N", "correlation_agents"]
    EX = ["somme", "somme_bilat", "max"]
    petit = ["somme", "max", "e_unilat_ville", "e_terminal_ville"]
    configs = {
        "gauss_1x24": {"loi": g(1, 24), "garde": True, "exacts": EX, "alarmes": P1},
        "gauss_3x12": {"loi": g(3, 12), "garde": True, "exacts": EX, "alarmes": PN},
        "gauss_1x12": {"loi": g(1, 12), "garde": True, "exacts": ["somme", "max"], "alarmes": petit + ["page"]},
        "gauss_1x36": {"loi": g(1, 36), "garde": True, "exacts": ["somme", "max"], "alarmes": petit},
        "exp_1x24": {"loi": g(1, 24, "exp"), "garde": True, "exacts": [], "garde_exclus": ["e_unilat_ville", "e_bilat_ville"],
                     "alarmes": ["somme", "somme_bilat", "max", "glissante_10", "page", "e_unilat_ville", "e_bilat_ville",
                                 "autocorr", "autocorr_abs"]},
        "hetero_3x8": {"loi": {"type": "moyennes", "mus": [-0.5, 0.0, 0.5], "N": 3, "T": 8}, "garde": True, "exacts": [],
                       "alarmes": ["dispersion_agents"]},
        "ar03_1x24": {"loi": {"type": "ar1", "phi": 0.3, "marginale": "gauss", "N": 1, "T": 24}, "garde": True,
                      "exacts": ["somme"], "alarmes": ["somme", "max", "autocorr", "page", "glissante_10", "e_unilat_cal"]},
    }
    cop = ["somme", "somme_bilat", "max", "e_unilat_ville", "e_bilat_ville", "page", "glissante_10", "autocorr", "autocorr_abs"]
    reglages = [{"nom": "a_gauss", "loi": g(1, 24)}, {"nom": "a_tau", "loi": {"type": "effet_episode", "tau": 0.3, "N": 1, "T": 24}},
                {"nom": "a_sigma", "loi": g(1, 24), "sigma_utilise": 0.7}, {"nom": "b_gauss", "loi": g(3, 12)},
                {"nom": "b_equi", "loi": {"type": "equicorrelation", "c": 0.3, "N": 3, "T": 12}}]
    return {
        "version": "mini", "alpha": 0.1, "entropie": "123456789",
        "tailles": {"R": 300, "R_cal": 3000, "R0": 3000, "R_P2": 400, "equivalence": 4},
        "replication": {"facteur_R": 2},
        "configs": configs,
        "configs_par_bloc": {"P1a": ["gauss_1x24", "gauss_3x12"], "P1b": ["gauss_1x12", "gauss_1x36", "gauss_3x12"],
                             "P2": ["gauss_1x24"], "P3": [], "P34": ["gauss_1x24"], "P4": ["gauss_1x24", "gauss_3x12"],
                             "P43": ["hetero_3x8"], "P5_temps": ["gauss_1x24"], "P5_agents": ["gauss_3x12"],
                             "P6": ["gauss_1x24", "exp_1x24", "gauss_3x12", "ar03_1x24"], "P7": ["gauss_1x24"],
                             "P8": ["gauss_1x24", "gauss_3x12"]},
        "P1a": {"configs": [[1, 24], [3, 12]], "B": [4], "m": [1, 3, 24], "schemas": list(att.SCHEMAS[:-2]) + ["adaptatif"]},
        "P1b": {"configs": [[1, 12], [1, 36], [3, 12]], "B": [4], "m": 2},
        "P2": {"config": [1, 24], "B": [6], "m": [1, 4, 24]},
        "P3": {"configs": [[1, 24], [3, 12]], "B": [5], "m": [1, 4], "calendriers": ["debut", "uniforme", "aleatoire", "fin"]},
        "P34": {"config": [1, 24], "B": [6], "m": [3], "alarmes": ["e_unilat_cal", "e_unilat_ville", "page", "detecteur_e",
                                                                  "glissante_10", "balayage_multi"]},
        "P4": {"configs": [[1, 24], [3, 12]], "arrangements_T1": ["tri_croissant", "bloc_top_5", "top_10_fin", "apparie_autocorr"],
               "arrangements_T2": ["tri_croissant", "bloc_top_5"], "iterations_appariement": 30},
        "P43": {"config": "hetero_3x8"},
        "P5_temps": {"T": 24, "r": [3, 5], "alarmes": ["glissante_5", "glissante_10", "balayage_multi", "page", "autocorr",
                                                      "suites", "max", "e_unilat_ville"],
                     "iterations_appariement": 30, "tolerance_autocorr": 0.5, "tolerance_suites": 30},
        "P5_agents": {"config": [3, 12], "mc": 2, "alarmes": ["co_elevation_2", "co_elevation_N", "page", "glissante_5", "somme",
                                                            "max", "correlation_agents"]},
        "P6": {"cellules": [
            {"nom": "ar_g+", "role": "copule_temps", "cfg": "gauss_1x24", "loi": {"type": "ar1", "phi": 0.4, "N": 1, "T": 24}, "alarmes": cop},
            {"nom": "ar_g-", "role": "copule_temps", "cfg": "gauss_1x24", "loi": {"type": "ar1", "phi": -0.4, "N": 1, "T": 24}, "alarmes": cop},
            {"nom": "ar_e+", "role": "copule_temps", "cfg": "exp_1x24",
             "loi": {"type": "ar1", "phi": 0.4, "marginale": "exp", "N": 1, "T": 24}, "alarmes": cop},
            {"nom": "equi", "role": "equicorrelation", "cfg": "gauss_3x12", "loi": {"type": "equicorrelation", "c": 0.3, "N": 3, "T": 12},
             "alarmes": ["somme", "max", "e_unilat_ville", "co_elevation_N", "correlation_agents", "page", "autocorr"]},
            {"nom": "c2606", "role": "construction_2606", "cfg": "ar03_1x24", "loi": {"type": "ar1", "phi": 0.6, "N": 1, "T": 24},
             "alarmes": ["somme", "max", "autocorr", "page", "glissante_10", "e_unilat_cal"]}]},
        "P7": {"T": 24, "arrangements": ["tri_croissant", "top_10_fin"], "alarmes": ["e_unilat_ville", "e_bilat_ville", "page", "glissante_10"]},
        "P8": {"reglages": reglages, "alarmes": ["e_unilat_ville", "somme", "max", "page"],
               "conforme": {"K": 40, "n_test": 30, "L": 3, "statistiques": ["e_unilat", "somme"]},
               "lecture": {"bien_specifies": ["a_gauss", "b_gauss"], "signe": {"a_tau": "a_gauss", "b_equi": "b_gauss"},
                           "depasse": ["a_tau"]}},
    }


PREREG_MINI = "# Mini préenregistrement de test\n\n- Commit du code d'analyse : `{commit}`\n- Grille : {sha}\n\n" + "\n\n".join(
    f"## {s}\n\nTexte de test." for s in ("Hypothèse", "Prédiction chiffrée et signe attendu", "Métrique", "Seuil",
                                           "Plan d'analyse", "Critères de lecture gelés", "Liste d'arrêt")) + (
    "\n\n## Contre-lecture\n\nTexte de test : brouillon `" + "a" * 64 + "`, rapport `" + "b" * 64 + "`.\n")


def _preparer(depot, grille=None):
    """Mini-dépôt : code factice et grille scellée committés (commit cité), puis préenregistrement scellé."""
    from controle_ia.prereg import sceller_prereg
    from controle_ia.scellement import sceller

    grille = grille or _mini_grille()
    (depot / "src").mkdir(exist_ok=True)
    (depot / "src" / "code_factice.py").write_text("X = 1\n", encoding="utf-8")
    gp = depot / "grille.json"
    gp.write_text(json.dumps(grille), encoding="utf-8")
    sha = sceller(gp)
    committer(depot)
    commit = subprocess.run(["git", "-C", str(depot), "rev-parse", "HEAD"], capture_output=True, text=True,
                            check=True).stdout.strip()
    pp = depot / "prereg.md"
    pp.write_text(PREREG_MINI.format(sha=sha, commit=commit), encoding="utf-8")
    sceller_prereg(pp)
    committer(depot)
    return pp, gp


ATTENDUES = {"P1.1", "P1.2", "P1.3", "P1.4", "P2.1", "P2.2", "P2.3", "P3.1", "P3.2", "P3.3", "P3.4", "P4.1", "P4.2",
             "P4.3", "P5.1", "P5.2", "P5.3", "P5.4", "P5.5", "P6.1", "P6.2", "P6.3", "P6.4", "P6.5", "P7.1",
             "P7.2", "P7.3", "P8.1", "P8.2", "P8.3", "P8.4"}


def test_chaine_complete_mini_grille(depot):
    from controle_ia.manifeste import verifier_resultat
    from controle_ia.prereg import sceller_prereg
    from controle_ia.simulation_t03.figures import figures
    from controle_ia.simulation_t03.run_t03 import executer, taches

    pp, gp = _preparer(depot)
    grille = json.loads(gp.read_text(encoding="utf-8"))
    assert len(set(taches(grille))) == len(taches(grille))
    sortie = executer(depot, pp, gp, "20261004-130000-mini", verifier_import=False)
    corps = verifier_resultat(depot, sortie["lecture"])
    lec = corps["resultat"]["lecture"]
    assert set(lec["predictions"]) == ATTENDUES
    for p in ("P1.1", "P3.1", "P4.1", "P5.1", "P5.4", "P7.1"):      # théorèmes trajectoriels : exacts même en petit
        assert lec["predictions"][p]["verdict"] == "confirmée", (p, lec["predictions"][p])
    assert set(lec["audit_symetrie"]) == {"bornes", "formes_closes", "egalites", "audit_declenche"}
    prog = corps["resultat"]["programme"]
    assert len(prog) == 6 and all(set(ligne["exiges"]) <= ATTENDUES for ligne in prog)
    assert (depot / "diag" / "20261004-130000-mini" / "lecture.md").exists()
    faites = figures(depot, "20261004-130000-mini", alpha=0.1)
    assert len(faites) == 6 and all((depot / "diag" / "20261004-130000-mini" / "figures" / Path(f).name).exists()
                                    for f in faites)
    with pytest.raises(GardeArret, match="écraser"):
        figures(depot, "20261004-130000-mini", alpha=0.1)
    # artefact : grille non citée par le préenregistrement → arrêt
    pp2 = depot / "prereg2.md"
    pp2.write_text(PREREG_MINI.format(sha="0" * 64, commit="0" * 40), encoding="utf-8")
    sceller_prereg(pp2)
    committer(depot)
    with pytest.raises(GardeArret, match="ne cite pas"):
        executer(depot, pp2, gp, "20261004-130001-mini", verifier_import=False)
    # artefact : tâche absente du manifeste → arrêt (aucun repli silencieux)
    ctx = B.Contexte(grille, {}, "")
    with pytest.raises(GardeArret, match="absente du manifeste"):
        ctx.rng("P7/Y")


# --- gardes de la liste d'arrêt : artefacts (R5) ; le cas sain est la chaîne complète ci-dessus ---
def test_garde_commit_cite_artefact(depot):
    from controle_ia.simulation_t03.run_t03 import executer

    pp, gp = _preparer(depot)
    (depot / "src" / "code_factice.py").write_text("X = 2\n", encoding="utf-8")
    committer(depot)
    with pytest.raises(GardeArret, match="modifiés depuis le commit cité"):
        executer(depot, pp, gp, "20261004-140000-mini", verifier_import=False)


def test_garde_commit_cite_sous_branches(depot, tmp_path_factory):
    from controle_ia.simulation_t03.run_t03 import exiger_code_cite

    pp, gp = _preparer(depot)
    assert len(exiger_code_cite(depot, pp, gp)) == 40                    # cas sain
    (depot / "tests").mkdir()
    (depot / "tests" / "t.py").write_text("x = 1\n", encoding="utf-8")
    committer(depot)
    with pytest.raises(GardeArret, match="modifiés depuis le commit cité"):  # tests/ modifié
        exiger_code_cite(depot, pp, gp)
    texte = pp.read_text(encoding="utf-8")
    inconnu = depot / "inconnu.md"
    inconnu.write_text(texte.replace(texte.split("`")[1], "1" * 40), encoding="utf-8")
    with pytest.raises(GardeArret, match="impossible"):                   # commit inconnu
        exiger_code_cite(depot, inconnu, gp)
    sans = depot / "sans.md"
    sans.write_text("Commit du code d'analyse : `abc`\n", encoding="utf-8")
    with pytest.raises(GardeArret, match="ne cite pas le commit"):        # commit absent ou abrégé
        exiger_code_cite(depot, sans, gp)
    dehors = tmp_path_factory.mktemp("ailleurs") / "grille.json"
    with pytest.raises(GardeArret, match="hors du dépôt"):                # grille hors du dépôt
        exiger_code_cite(depot, pp, dehors)


def test_garde_code_importe(depot):
    from controle_ia.simulation_t03.run_t03 import exiger_code_importe_sous

    exiger_code_importe_sous(Path(__file__).resolve().parents[1])         # cas sain : le dépôt qui héberge le code
    with pytest.raises(GardeArret, match="hors de"):
        exiger_code_importe_sous(depot)                                    # artefact : un autre arbre


def test_blocs_refuses_partout(depot):
    from controle_ia.simulation_t03.run_t03 import executer

    pp, gp = _preparer(depot)
    with pytest.raises(GardeArret, match="ne se choisissent pas"):
        executer(depot, pp, gp, "20261004-140001-mini", blocs=["P2"], verifier_import=False)
    with pytest.raises(GardeArret, match="ne se choisissent pas"):
        executer(depot, pp, gp, "20261004-140007-mini", blocs=["P2"], replication_de="x", verifier_import=False)


def test_garde_duree_artefact(depot):
    from controle_ia.simulation_t03.run_t03 import executer

    pp, gp = _preparer(depot)
    with pytest.raises(GardeArret, match="durée"):
        executer(depot, pp, gp, "20261004-140002-mini", limite_s=0.0, verifier_import=False)


def test_garde_calibrage_artefact(depot, monkeypatch):
    from controle_ia.simulation_t03.run_t03 import executer

    pp, gp = _preparer(depot)
    vrai = cal.seuil_max_exact
    monkeypatch.setattr(cal, "seuil_max_exact", lambda a, n: vrai(a, n) - 0.7)
    with pytest.raises(GardeArret, match="garde de calibrage"):
        executer(depot, pp, gp, "20261004-140003-mini", verifier_import=False)


def test_garde_seuil_non_fini_artefact(depot, monkeypatch):
    from controle_ia.simulation_t03.run_t03 import executer

    pp, gp = _preparer(depot)
    monkeypatch.setattr(cal, "seuil_mc", lambda v, a: math.inf)
    with pytest.raises(GardeArret, match="seuils non finis"):
        executer(depot, pp, gp, "20261004-140004-mini", verifier_import=False)


def test_garde_equivalence_artefact(depot, monkeypatch):
    from controle_ia.simulation_t03.run_t03 import executer

    pp, gp = _preparer(depot)
    vrai = L.lot_max
    monkeypatch.setattr(L, "lot_max", lambda Xb: vrai(Xb) + 1e-6)
    with pytest.raises(GardeArret, match="équivalence"):
        executer(depot, pp, gp, "20261004-140005-mini", verifier_import=False)


def test_garde_multiensemble_artefact(depot, monkeypatch):
    from controle_ia.simulation_t03.run_t03 import executer

    pp, gp = _preparer(depot)
    vrai = att.bloc_top_r

    def fausse(x, r, rng):
        out, debut = vrai(x, r, rng)
        out = out.copy()
        out[:, 0] += 1.0                                  # une valeur perdue, une autre inventée
        return out, debut

    monkeypatch.setattr(att, "bloc_top_r", fausse)
    with pytest.raises(GardeArret, match="multi-ensemble non préservé"):
        executer(depot, pp, gp, "20261004-140006-mini", verifier_import=False)


def test_puissance_dispersion_exacte():
    mus = [-0.5, 0.0, 0.5]
    # valeurs de la contre-lecture (énumération indépendante, 4 décimales)
    for T, v in ((30, 0.9050), (40, 0.9673), (50, 0.9897)):
        assert abs(cal.puissance_dispersion_rebrassage(T, mus, 0.05) - v) < 6e-5
    # Monte-Carlo sur une taille non décisive (T = 12)
    g = _rng(17)
    loi = {"type": "moyennes", "mus": mus, "N": 3, "T": 12}
    c = stats.chi2.isf(0.05, 3)
    X = tirer(g, 40000, loi)
    Xt = L.depuis_ordre(att.rebrassage(L.ordre(X), g), 3, 12)
    p = (L.lot_dispersion_agents(Xt, mus) >= c).mean()
    p_th = cal.puissance_dispersion_rebrassage(12, mus, 0.05)
    assert abs(p - p_th) < 4 * math.sqrt(p_th * (1 - p_th) / 40000)
    with pytest.raises(GardeArret):
        cal.puissance_dispersion_rebrassage(12, [0.0, 1.0], 0.05)


# --- références ajoutées à `agregateurs` pour T0.3 ---
def test_references_ajoutees():
    X = _rng(16).standard_normal((1, 80))
    assert math.isclose(detecteur_e(X, (1.0,)), max(page_cusum(X, 0.5), detecteur_e(X, (1.0,))))
    assert math.isclose(detecteur_e(X, (1.0,)), page_cusum(X, 0.5)) or page_cusum(X, 0.5) == 0.0
    assert math.isclose(balayage_multi(X, (4,)), balayage(X, 4) / 2.0)
    Y = np.array([[1.0, 3.0], [0.0, 0.0]])
    assert math.isclose(dispersion_agents(Y, [0.0, 1.0]), 2 * 2.0 ** 2 + 2 * 1.0 ** 2)
    with pytest.raises(GardeArret):
        dispersion_agents(Y, [0.0])
    with pytest.raises(GardeArret):
        detecteur_e(X, (0.0, 1.0))
    with pytest.raises(GardeArret):
        balayage_multi(X, (100,))
