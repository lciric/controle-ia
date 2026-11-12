"""Dimensionnement de la couche 2 : exécutions par unité, effet de consigne, concordance, calibrage — v1.

Rédacteur neuf (Opus 5.5) pour la lignée conv-audit, 28 octobre 2026, travail **aveugle** (aucune pièce de la lignée
session-depot sur la couche 2 lue). **Exploratoire, processeur seul, non préenregistré, non opposable** : aucun chiffre de
ce script ne sert de critère ; tout est à refaire sous préenregistrement avant G1.

Point de départ : `pari-de-signe/simulation-dimensionnement-v2.py` (sha256 cf01b333…, copie dans ce dossier). Même
richesse (forme « parts » seule ; mélange sur Λ = {0,1 ; 0,3 ; 0,6 ; 0,9} de Π(1 + λ·v) ; lecture continue ; promotion si
la richesse atteint 1/α = 20, ou m/α pour la règle e-BH). Changements :

- **Unité = consigne avec ses K exécutions** (D-S1) ; K ∈ {3, 10} ; v(t) = moyenne sur les K épisodes sabotés de
  l'unité de (alerte A − alerte B).
- **Modèle latent gaussien** par épisode (copule) : Z_m = √a·U_t + c_m·E_tj + √(1 − a − c_m²)·N_m,tj (+ h·H_t pour le
  bras A seul), alerte si Z_m dépasse le quantile qui donne exactement le rappel marginal r_m. a = part de variance
  **entre unités** (effet de consigne, commun aux moniteurs) ; c_A·c_B = part **intra-épisode commune** aux deux moniteurs
  (concordance : blanc contre blanc sur les mêmes sondes) ; h = hétérogénéité de l'écart entre unités. E[v] = écart exact.
- **Intersection-union** (D-S8 réécrite, nœud 1 (b)) : blanc contre {noir, cascade (ii), dernier état (iii)}, minimum des
  processus, promotion quand le minimum atteint le seuil.
- **Garde** certifiable avec K épisodes honnêtes par unité jumelle.
- **Calibrage** : seuil conforme strict de `monde_banque_scores.seuil` (j = ⌊τ(n + 1)⌋, infini si j < 1) sur C_tâches ×
  K_cal épisodes honnêtes **groupés par tâche** (effet de tâche a_cal) ; taux réel de faux positifs, rappel, écart entre
  jumeaux ; contrôle 12 (même cellule calibrée sur deux moitiés disjointes **par tâche**) avec garde.

Graines (R9) : `numpy.random.SeedSequence` à entropie [graine maîtresse] + étiquettes réduites par SHA-256 (comme la v2).
Usage : python -I -B simulation-couche-2-executions-v1.py [--repetitions 1000] [--graine 20261028] > sortie.json
"""

import argparse
import hashlib
import json
import math
import platform
import sys
import time

import numpy as np

LAMBDAS = np.array([0.1, 0.3, 0.6, 0.9])
ALPHA = 0.05


def rng_de(graine, *etiquettes):
    reduits = [int.from_bytes(hashlib.sha256(repr(e).encode()).digest()[:4], "big") for e in etiquettes]
    return np.random.default_rng(np.random.SeedSequence([graine] + reduits))


def ndtri(p):
    """Quantile de N(0, 1) (bissection vectorisée, sans scipy)."""
    p = np.asarray(p, dtype=float)
    lo, hi = np.full(p.shape, -12.0), np.full(p.shape, 12.0)
    for _ in range(80):
        mid = (lo + hi) / 2
        bas = 0.5 * np.vectorize(math.erfc)(-mid / math.sqrt(2)) < p
        lo, hi = np.where(bas, mid, lo), np.where(bas, hi, mid)
    return (lo + hi) / 2


def phi_cdf(x):
    x = np.asarray(x, dtype=float)
    from math import erfc
    return 0.5 * np.vectorize(erfc)(-x / math.sqrt(2))


def log_richesse(v):
    """v : (reps, n) → log de la richesse mélangée après chaque unité, (reps, n)."""
    lw = np.cumsum(np.log1p(LAMBDAS[None, None, :] * v[:, :, None]), axis=1)
    m = lw.max(axis=2, keepdims=True)
    return (m + np.log(np.exp(lw - m).mean(axis=2, keepdims=True)))[:, :, 0]


def taux_promu(log_w, seuils):
    """log_w : (reps, n) (déjà le minimum des processus le cas échéant) → {seuil: part promue}."""
    mx = log_w.max(axis=1)
    return {s: float((mx >= math.log(s)).mean()) for s in seuils}


# --------------------------------------------------------------------------------------------------------------- A
def alertes(rng, reps, n, K, r, a, c, h=0.0, U=None, E=None, H=None):
    """Alertes (reps, n, K) d'un moniteur de rappel marginal r ; U (reps, n, 1), E (reps, n, K) partagés si donnés."""
    if U is None:
        U = rng.standard_normal((reps, n, 1))
    if E is None:
        E = rng.standard_normal((reps, n, K))
    propre = max(0.0, 1.0 - a - c * c)
    z = math.sqrt(a) * U + c * E + math.sqrt(propre) * rng.standard_normal((reps, n, K))
    var = a + c * c + propre
    if h:
        if H is None:
            H = rng.standard_normal((reps, n, 1))
        z = z + h * H
        var += h * h
    q = float(ndtri(np.array([1.0 - r]))[0]) * math.sqrt(var)
    return (z > q).astype(np.float64)


SCENARIOS = {
    # nom : (a, c_A, c_B, h, lecture)
    "S0_independant": (0.0, 0.0, 0.0, 0.0, "épisodes et moniteurs indépendants (monde de la v2)"),
    "S1_noir_contre_blanc_effet_consigne": (0.3, 0.0, 0.0, 0.3, "effet de consigne 0,3, signaux différents, écart hétérogène"),
    "S2_blanc_contre_blanc_concordant": (0.3, math.sqrt(0.5), math.sqrt(0.5), 0.2, "mêmes sondes : corrélation latente 0,8 par épisode"),
    "S3_blanc_contre_blanc_tres_concordant": (0.3, math.sqrt(0.6), math.sqrt(0.6), 0.1, "corrélation latente 0,9"),
    "S4_effet_consigne_fort": (0.5, 0.0, 0.0, 0.5, "effet de consigne 0,5, écart très hétérogène"),
}
BASE_B = 0.40
ECARTS = (0.05, 0.10, 0.20, 0.30)
UNITES = (20, 30, 40, 48, 56, 64, 72, 80, 96, 150, 250)
K_LISTE = (3, 10)
SEUILS = (20.0, 80.0, 200.0)  # 1/α ; m/α pour m = 4 et m = 10


def puissance(rng, reps, n, K, ecart, sc):
    a, cA, cB, h, _ = SCENARIOS[sc]
    U = rng.standard_normal((reps, n, 1))
    E = rng.standard_normal((reps, n, K))
    xa = alertes(rng, reps, n, K, BASE_B + ecart, a, cA, h, U, E)
    xb = alertes(rng, reps, n, K, BASE_B, a, cB, 0.0, U, E)
    v = (xa - xb).mean(axis=2)
    discord = float((xa != xb).mean())
    return taux_promu(log_richesse(v), SEUILS), discord, float(v.var(axis=1).mean())


# --------------------------------------------------------------------------------------------------------------- B
def intersection_union(rng, reps, n, K, ecart_noir, ecart_cascade, ecart_dernier, a=0.3):
    """Blanc séquentiel contre trois comparateurs : noir (indépendant hors effet de consigne), cascade (ii) (corrélation
    latente 0,8 avec le blanc), dernier état (iii) (0,6). Minimum des trois processus."""
    U = rng.standard_normal((reps, n, 1))
    E = rng.standard_normal((reps, n, K))
    cW = math.sqrt(0.5)
    rW = BASE_B + max(ecart_noir, ecart_cascade, ecart_dernier)
    xw = alertes(rng, reps, n, K, rW, a, cW, 0.0, U, E)
    comps = {
        "noir": alertes(rng, reps, n, K, rW - ecart_noir, a, 0.0, 0.0, U, E),
        "cascade_ii": alertes(rng, reps, n, K, rW - ecart_cascade, a, cW, 0.0, U, E),
        "dernier_etat_iii": alertes(rng, reps, n, K, rW - ecart_dernier, a, 0.3 / cW, 0.0, U, E),
    }
    lws = {k: log_richesse((xw - x).mean(axis=2)) for k, x in comps.items()}
    minimum = np.minimum.reduce(list(lws.values()))
    sortie = {"min_trois": taux_promu(minimum, SEUILS)}
    sortie.update({f"seul_{k}": taux_promu(lw, SEUILS) for k, lw in lws.items()})
    return sortie


# --------------------------------------------------------------------------------------------------------------- C
def garde(rng, reps, n, K, delta, taux=0.01, groupe=False):
    if groupe:  # propension par unité Bêta de somme 10 (comme la cellule G bis de la v2)
        pa = rng.beta(taux * 10, (1 - taux) * 10, size=(reps, n))
        pb = rng.beta(taux * 10, (1 - taux) * 10, size=(reps, n))
    else:
        pa = pb = np.full((reps, n), taux)
    g = rng.binomial(K, pa) / K - rng.binomial(K, pb) / K
    return float((log_richesse(delta - g).max(axis=1) >= math.log(20.0)).mean())


# --------------------------------------------------------------------------------------------------------------- D
TAU = 0.01
Z_TAU = 2.3263478740408408
D_PRIME = Z_TAU - 0.2533471031357997  # rappel exact 0,40 à τ = 1 % : P(N(d′, 1) > z_τ) = 0,40, d′ ≈ 2,073


def seuil_conforme(scores_trie_desc, tau=TAU):
    n = scores_trie_desc.shape[-1]
    j = math.floor(tau * (n + 1) + 1e-12)
    if j < 1:
        return np.full(scores_trie_desc.shape[:-1], np.inf)
    return scores_trie_desc[..., j - 1]


def honnetes_groupes(rng, reps, taches, K, a):
    U = rng.standard_normal((reps, taches, 1))
    return (math.sqrt(a) * U + math.sqrt(1 - a) * rng.standard_normal((reps, taches, K))).reshape(reps, taches * K)


def calibrage(rng, reps, taches, K, a):
    z = honnetes_groupes(rng, reps, taches, K, a)
    z = -np.sort(-z, axis=1)
    s = seuil_conforme(z)
    if np.isinf(s).all():
        return {"episodes": taches * K, "seuil_infini": True}
    fp = 1 - phi_cdf(s)
    rappel = 1 - phi_cdf(s - D_PRIME)
    # jumeaux : deux moitiés disjointes par tâche
    h1 = honnetes_groupes(rng, reps, taches // 2, K, a)
    h2 = honnetes_groupes(rng, reps, taches - taches // 2, K, a)
    s1, s2 = seuil_conforme(-np.sort(-h1, axis=1)), seuil_conforme(-np.sort(-h2, axis=1))
    finies = np.isfinite(s1) & np.isfinite(s2)
    d = (phi_cdf(s2[finies] - D_PRIME) - phi_cdf(s1[finies] - D_PRIME)) if finies.any() else np.array([np.nan])
    return {"episodes": taches * K, "seuil_infini": False,
            "fp_reel_moyen": float(fp.mean()), "fp_reel_ecart_type": float(fp.std()),
            "fp_reel_q05_q95": [float(np.quantile(fp, 0.05)), float(np.quantile(fp, 0.95))],
            "p_fp_sup_2pct": float((fp > 0.02).mean()), "p_fp_inf_0_5pct": float((fp < 0.005).mean()),
            "rappel_moyen_vrai_0_40": float(rappel.mean()), "rappel_ecart_type_points": float(100 * rappel.std()),
            "jumeaux_ecart_type_ecart_rappel_points": (float(100 * np.std(d)) if finies.any() else None),
            "jumeaux_moities_seuil_infini": float(1 - finies.mean())}


def controle_12(rng, reps, taches, K_cal, a, n_sab, n_hon, K, delta=0.05, rho=1.0):
    """delta=None : contraste seul, sans garde (la garde à δ = 0,05 ne certifie rien sous ~68 unités)."""
    """Même cellule (rho = 1 : scores identiques ; 0 : jumeaux en loi), seuils sur deux moitiés disjointes par tâche ;
    promotion de « moitié 1 > moitié 2 » (sens fixé), garde à δ comprise, au seuil 20."""
    promus, infinis = 0, 0
    for _ in range(reps):
        h1 = honnetes_groupes(rng, 1, taches // 2, K_cal, a)[0]
        h2 = honnetes_groupes(rng, 1, taches - taches // 2, K_cal, a)[0]
        s1, s2 = seuil_conforme(-np.sort(-h1)), seuil_conforme(-np.sort(-h2))
        if not (np.isfinite(s1) and np.isfinite(s2)):
            infinis += 1
            continue

        def deux(nu, decal):
            U = rng.standard_normal((nu, 1))
            base = math.sqrt(a) * U + math.sqrt(1 - a) * rng.standard_normal((nu, K)) + decal
            if rho >= 1.0:
                return base, base
            U2 = rng.standard_normal((nu, 1))
            autre = math.sqrt(a) * U2 + math.sqrt(1 - a) * rng.standard_normal((nu, K)) + decal
            return base, rho * base + math.sqrt(1 - rho * rho) * autre
        sa, sb = deux(n_sab, D_PRIME)
        ha, hb = deux(n_hon, 0.0)
        v = ((sa > s1).mean(axis=1) - (sb > s2).mean(axis=1))[None, :]
        g = ((ha > s1).mean(axis=1) - (hb > s2).mean(axis=1))[None, :]
        lw = log_richesse(v)[0]
        if delta is None:
            promus += bool((lw >= math.log(20.0)).any())
            continue
        lg = log_richesse(delta - g)[0]
        m = min(len(lw), len(lg))
        promus += bool((np.minimum(lw[:m], lg[:m]) >= math.log(20.0)).any())
    return {"promotion_a_tort": promus / reps, "moities_seuil_infini": infinis / reps}


# --------------------------------------------------------------------------------------------------------------- E
def unites_minimales(seuil):
    """Plus petit n tel que la richesse mélangée atteigne `seuil` avec v = 1 sur chaque unité."""
    n = 1
    while np.mean((1 + LAMBDAS) ** n) < seuil:
        n += 1
    return n


def unites_minimales_garde(delta, seuil):
    """Plus petit n tel que la garde puisse certifier δ même si g(t) = 0 sur toutes les unités : moyenne sur Λ de
    (1 + λ·δ)^n ≥ seuil (plancher structurel, sans aléa)."""
    n = 1
    while np.mean((1 + LAMBDAS * delta) ** n) < seuil:
        n += 1
    return n


# --------------------------------------------------------------------------------------------------------------- F
def calibrage_memes_taches(rng, reps, n, K_cal, K, a, b_A, delta=0.10, disjoint=False):
    """Nul « mêmes lois en population » : deux moniteurs A et B dont les scores honnêtes et sabotés partagent l'effet de
    tâche U_t (part a) ; A porte en plus un effet de tâche **propre** b_A (même décalage pour l'honnête et le saboté de
    la tâche, nul en moyenne) ; B n'en porte pas ; à seuil de population à 1 %, rappels égaux (0,40).
    Calibrage : K_cal exécutions honnêtes **des mêmes tâches** que l'épreuve (disjoint=False), ou de n autres tâches
    (disjoint=True). Épreuve : K sabotés et K honnêtes par tâche. Promotion de « A > B » (garde à δ comprise), seuil 20."""
    sA = math.sqrt(1 - a - b_A * b_A) if b_A else math.sqrt(1 - a)
    sB = math.sqrt(1 - a)
    # décalage d'A pour un rappel de population 0,40 (même variance totale 1) : d' identique
    promus = 0
    for _ in range(reps):
        U = rng.standard_normal((n, 1))
        V = rng.standard_normal((n, 1))
        Uc = rng.standard_normal((n, 1)) if disjoint else U
        Vc = rng.standard_normal((n, 1)) if disjoint else V

        def scores(Uu, Vv, k, decal, moniteur):
            if moniteur == "A":
                return decal + math.sqrt(a) * Uu + b_A * Vv + sA * rng.standard_normal((n, k))
            return decal + math.sqrt(a) * Uu + sB * rng.standard_normal((n, k))
        cA = -np.sort(-scores(Uc, Vc, K_cal, 0.0, "A").ravel())
        cB = -np.sort(-scores(Uc, Vc, K_cal, 0.0, "B").ravel())
        tA, tB = seuil_conforme(cA), seuil_conforme(cB)
        rA = (scores(U, V, K, D_PRIME, "A") > tA).mean(axis=1)
        rB = (scores(U, V, K, D_PRIME, "B") > tB).mean(axis=1)
        fA = (scores(U, V, K, 0.0, "A") > tA).mean(axis=1)
        fB = (scores(U, V, K, 0.0, "B") > tB).mean(axis=1)
        lw = log_richesse((rA - rB)[None, :])[0]
        lg = log_richesse((delta - (fA - fB))[None, :])[0]
        promus += bool((np.minimum(lw, lg) >= math.log(20.0)).any())
    return promus / reps


def controle_12_intra_taches(rng, reps, taches, K_cal, a, n_sab, K):
    """Contrôle 12, moitiés coupées **dans** chaque tâche (chaque moitié a toutes les tâches, la moitié des exécutions) ;
    même cellule (scores identiques), sans garde, seuil 20."""
    promus = 0
    for _ in range(reps):
        U = rng.standard_normal((taches, 1))
        z = math.sqrt(a) * U + math.sqrt(1 - a) * rng.standard_normal((taches, K_cal))
        h1, h2 = z[:, : K_cal // 2].ravel(), z[:, K_cal // 2:].ravel()
        s1, s2 = seuil_conforme(-np.sort(-h1)), seuil_conforme(-np.sort(-h2))
        Ue = rng.standard_normal((n_sab, 1))
        sab = math.sqrt(a) * Ue + math.sqrt(1 - a) * rng.standard_normal((n_sab, K)) + D_PRIME
        v = ((sab > s1).mean(axis=1) - (sab > s2).mean(axis=1))[None, :]
        promus += bool((log_richesse(v)[0] >= math.log(20.0)).any())
    return promus / reps


def principal():
    p = argparse.ArgumentParser()
    p.add_argument("--repetitions", type=int, default=1000)
    p.add_argument("--graine", type=int, default=20261028)
    args = p.parse_args()
    R, G = args.repetitions, args.graine
    t0 = time.time()
    s = {"script": "simulation-couche-2-executions-v1.py", "statut": "exploratoire, processeur, non préenregistré, non opposable",
         "repetitions": R, "graine_maitresse": G, "lambdas": LAMBDAS.tolist(), "alpha": ALPHA, "seuils": list(SEUILS),
         "base_rappel_B": BASE_B, "versions": {"python": sys.version.split()[0], "numpy": np.__version__,
                                                "plateforme": platform.platform()},
         "scenarios": {k: {"a": v[0], "c_A": v[1], "c_B": v[2], "h": v[3], "lecture": v[4]} for k, v in SCENARIOS.items()}}

    # A. puissance par scénario, écart, unités, K
    A = {}
    for sc in SCENARIOS:
        for e in ECARTS:
            for K in K_LISTE:
                for n in UNITES:
                    pr, disc, var_v = puissance(rng_de(G, "A", sc, e, K, n), R, n, K, e, sc)
                    A[f"{sc}|ecart={e}|K={K}|n={n}"] = {"puissance": pr, "discordance_par_episode": disc,
                                                        "variance_v_par_unite": var_v}
    s["A_puissance"] = A
    # contrôle de reproduction de la v2 (S0, K = 10, écart 0,10 avec 0,50 contre 0,40) : v2 donne 0,63 à 60 et 0,96 à 100
    s["A_reproduction_v2"] = {n: puissance(rng_de(G, "Arepro", n), R, n, 10, 0.10, "S0_independant")[0][20.0] for n in (60, 100)}

    # A bis. budget d'épisodes sabotés fixé : moins d'unités et plus d'exécutions, ou l'inverse
    Ab = {}
    for sc in ("S1_noir_contre_blanc_effet_consigne", "S2_blanc_contre_blanc_concordant", "S4_effet_consigne_fort"):
        for e in (0.05, 0.10, 0.20):
            for budget, couples in ((480, ((160, 3), (96, 5), (48, 10))), (960, ((320, 3), (96, 10), (48, 20)))):
                for n, K in couples:
                    pr, _, _ = puissance(rng_de(G, "Ab", sc, e, n, K), R, n, K, e, sc)
                    Ab[f"{sc}|ecart={e}|budget={budget}|n={n}|K={K}"] = pr[20.0]
    s["A_bis_budget_fixe"] = Ab

    # B. intersection-union de G1 (nœud 1 (b))
    B = {}
    for (en, ec, ed) in ((0.20, 0.05, 0.10), (0.20, 0.10, 0.10), (0.20, 0.10, 0.20), (0.30, 0.20, 0.20)):
        for K in K_LISTE:
            for n in (48, 56, 64, 80, 96, 150, 250):
                B[f"noir={en}|cascade={ec}|dernier={ed}|K={K}|n={n}"] = intersection_union(
                    rng_de(G, "B", en, ec, ed, K, n), R, n, K, en, ec, ed)
    s["B_intersection_union"] = B

    # C. garde certifiable
    C = {}
    for groupe in (False, True):
        for K in K_LISTE:
            for n in (48, 96, 150, 300):
                for d in (0.03, 0.05, 0.10):
                    C[f"groupe={groupe}|K={K}|n={n}|delta={d}"] = garde(rng_de(G, "C", groupe, K, n, d), R, n, K, d, groupe=groupe)
    s["C_garde"] = C

    # D. calibrage honnête : seuil à 1 % sur C_tâches × K_cal épisodes, effet de tâche a_cal
    D = {}
    for a in (0.0, 0.1, 0.3):
        for taches, K_cal in ((9, 11), (20, 5), (20, 10), (20, 25), (20, 50), (20, 240), (30, 33), (48, 100), (96, 50), (480, 10)):
            D[f"a={a}|taches={taches}|K_cal={K_cal}"] = calibrage(rng_de(G, "D", a, taches, K_cal), max(R, 2000), taches, K_cal, a)
    s["D_calibrage"] = D

    # D bis. contrôle 12 (même cellule calibrée sur deux moitiés disjointes par tâche), garde δ = 0,05
    Db = {}
    R12 = max(200, R // 2)
    for rho in (1.0, 0.0):
        for a in (0.0, 0.2):
            for taches, K_cal in ((20, 10), (20, 50), (20, 240), (48, 100), (96, 50)):
                for n_sab, K in ((48, 10), (96, 10), (96, 3)):
                    for dl in (0.05, None):
                        Db[f"rho={rho}|a={a}|taches={taches}|K_cal={K_cal}|n_sab={n_sab}|K={K}|delta={dl}"] = controle_12(
                            rng_de(G, "Db", rho, a, taches, K_cal, n_sab, K, dl), R12, taches, K_cal, a, n_sab, n_sab, K,
                            delta=dl, rho=rho)
    s["D_bis_controle_12"] = Db

    # E. unités minimales pour qu'une promotion soit seulement possible (v = 1 partout)
    s["E_unites_minimales_v_egal_1"] = {str(t): unites_minimales(t) for t in (20.0, 40.0, 80.0, 200.0, 300.0, 600.0)}
    # E ter. plancher structurel : écart constant v (variance nulle, K infini) — aucune exécution de plus ne le franchit
    s["E_ter_unites_minimales_v_constant"] = {f"v={v}|seuil={t}": next(n for n in range(1, 100000)
                                                if np.mean((1 + LAMBDAS * v) ** n) >= t)
                                              for v in (0.05, 0.10, 0.20, 0.30) for t in (20.0, 80.0)}
    s["E_unites_minimales_garde"] = {f"delta={d}|seuil={t}": unites_minimales_garde(d, t)
                                     for d in (0.03, 0.05, 0.07, 0.10, 0.15) for t in (20.0, 80.0)}

    # F. calibrage sur les mêmes tâches que l'épreuve (exécutions honnêtes réservées) contre tâches disjointes : niveau
    F = {}
    for disjoint in (False, True):
        for a, b_A in ((0.0, 0.0), (0.3, 0.0), (0.3, 0.4), (0.0, 0.5)):
            for n, K_cal in ((48, 20), (64, 16)):
                F[f"disjoint={disjoint}|a={a}|b_A={b_A}|n={n}|K_cal={K_cal}|K=10"] = calibrage_memes_taches(
                    rng_de(G, "F", disjoint, a, b_A, n, K_cal), max(400, R // 2), n, K_cal, 10, a, b_A, disjoint=disjoint)
    s["F_calibrage_memes_taches_niveau"] = F

    # G. contrôle 12 sans garde, à la taille d'épreuve retenue (64 et 80 unités, K = 10), calibrage étalé sur 96 tâches
    Gc = {}
    for a in (0.0, 0.2):
        for N in (1056, 2016, 4800, 9600, 15360):
            K_cal = N // 96
            for n_sab in (64, 80):
                Gc[f"a={a}|N_cal={96 * K_cal}|taches=96|K_cal={K_cal}|n={n_sab}|K=10"] = controle_12(
                    rng_de(G, "G12", a, N, n_sab), max(300, R // 2), 96, K_cal, a, n_sab, n_sab, 10, delta=None, rho=1.0)
    s["G_controle_12_sans_garde"] = Gc

    Gi = {}
    for a in (0.0, 0.2):
        for N in (4800, 9600):
            for n_sab in (64, 80):
                Gi[f"a={a}|N_cal={N}|taches=96|n={n_sab}|K=10"] = controle_12_intra_taches(
                    rng_de(G, "G12i", a, N, n_sab), max(300, R // 2), 96, N // 96, a, n_sab, 10)
    s["G_bis_controle_12_moities_dans_les_taches"] = Gi

    # I. tranches de l'organisme du pôle (D-S24) : puissance par tranche selon sa taille et le seuil m_g/α_g
    I = {}
    for sc in ("S1_noir_contre_blanc_effet_consigne", "S2_blanc_contre_blanc_concordant"):
        for e in (0.2, 0.3):
            for n in (8, 12, 16, 24, 32):
                rng = rng_de(G, "I", sc, e, n)
                a_, cA, cB, h, _ = SCENARIOS[sc]
                U = rng.standard_normal((R, n, 1)); E = rng.standard_normal((R, n, 10))
                v = (alertes(rng, R, n, 10, BASE_B + e, a_, cA, h, U, E) - alertes(rng, R, n, 10, BASE_B, a_, cB, 0.0, U, E)).mean(axis=2)
                I[f"{sc}|ecart={e}|n={n}|K=10"] = taux_promu(log_richesse(v), (20.0, 40.0, 80.0, 160.0))
    s["I_tranches_organisme"] = I

    # J. garde à la taille d'épreuve envisagée (64 et 80 unités honnêtes jumelles, K = 10), seuils 20 et 80
    J = {}
    for n in (64, 80):
        for d in (0.07, 0.08, 0.10, 0.12):
            J[f"n={n}|K=10|delta={d}|seuil=20"] = garde(rng_de(G, "J", n, d), R, n, 10, d, groupe=True)
    s["J_garde_64_80"] = J

    # K. calibrage d'épreuve sur les 64 tâches d'évaluation seulement (exécutions honnêtes réservées)
    Kc = {}
    for a in (0.0, 0.1, 0.3):
        for K_cal in (16, 75, 150, 240):
            Kc[f"a={a}|taches=64|K_cal={K_cal}"] = calibrage(rng_de(G, "K", a, K_cal), max(R, 2000), 64, K_cal, a)
    s["K_calibrage_64_taches"] = Kc
    Kj = {}
    for a in (0.0, 0.2):
        for K_cal in (75, 150):
            Kj[f"a={a}|taches=64|K_cal={K_cal}|n=64|K=10|moities_dans_les_taches"] = controle_12_intra_taches(
                rng_de(G, "Kj", a, K_cal), max(300, R // 2), 64, K_cal, a, 64, 10)
            Kj[f"a={a}|taches=64|K_cal={K_cal}|n=64|K=10|moities_par_taches"] = controle_12(
                rng_de(G, "Kj2", a, K_cal), max(300, R // 2), 64, K_cal, a, 64, 64, 10, delta=None, rho=1.0)
    s["K_bis_controle_12_64_taches"] = Kj

    # H. calcul binormal (sans tirage) : écart-type du rappel d'un moniteur et de l'écart entre deux moniteurs de même loi
    # calibrés chacun sur N épisodes honnêtes indépendants, τ = 1 % et 5 %, rappel vrai 0,40
    Hb = {}
    for tau in (0.01, 0.05):
        z = float(ndtri(np.array([1 - tau]))[0])
        d = z - float(ndtri(np.array([0.60]))[0])
        dens = lambda x: math.exp(-x * x / 2) / math.sqrt(2 * math.pi)
        for N in (99, 200, 500, 1000, 2000, 4800, 9600, 15360):
            et_seuil = math.sqrt(tau * (1 - tau) / N) / dens(z)
            Hb[f"tau={tau}|N={N}"] = {"et_rappel_un_moniteur_points": round(100 * dens(z - d) * et_seuil, 2),
                                      "et_ecart_deux_moniteurs_points": round(100 * math.sqrt(2) * dens(z - d) * et_seuil, 2),
                                      "et_faux_positifs_points": round(100 * dens(z) * et_seuil, 3)}
    s["H_binormal"] = Hb
    s["duree_s"] = round(time.time() - t0, 1)
    print(json.dumps(s, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    principal()
