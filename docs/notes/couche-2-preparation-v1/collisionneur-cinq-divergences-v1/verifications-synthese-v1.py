"""Vérifications du lecteur de synthèse (collisionneur couche 2) — v1. Exploratoire, processeur, non opposable.

Importe les fonctions de simulation-couche-2-executions-v1.py (sha256 20bb005c…, copie conforme de la pièce A2) et
refait les chiffres contestés entre les trois modèles. Graine maîtresse 20261029 (neuve). Graines par SeedSequence (R9).
"""
import importlib.util
import json
import math
import sys
import time

import numpy as np

spec = importlib.util.spec_from_file_location("simA2", sys.argv[1])
A2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(A2)

G = 20261029
R = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
L = A2.LAMBDAS
out = {"graine": G, "repetitions": R, "numpy": np.__version__}
t0 = time.time()

# V1. richesse déterministe de la garde W_n(δ) et planchers
out["V1_W"] = {f"n={n}|delta={d}": round(float(np.mean((1 + L * d) ** n)), 2)
               for n in (48, 64, 96) for d in (0.05, 0.07, 0.10)}
out["V1_planchers_garde_seuil20"] = {str(d): A2.unites_minimales_garde(d, 20.0) for d in (0.05, 0.07, 0.10)}

# V2. binormal : écart-type de l'écart de rappel entre deux moitiés N/2 (même cellule), points
z = A2.Z_TAU
dens = lambda x: math.exp(-x * x / 2) / math.sqrt(2 * math.pi)
d = A2.D_PRIME
def et_moities(N, tau=0.01):
    et_seuil = math.sqrt(tau * (1 - tau) / (N / 2)) / dens(z)
    return 100 * math.sqrt(2) * dens(z - d) * et_seuil
out["V2_binormal_moities_points"] = {N: round(et_moities(N), 2) for N in (4800, 6400, 9600, 19200)}
out["V2_constante_x_racineN"] = round(et_moities(10000) * 100 / 100, 3)  # σ·√N/100 → constante (points·√N/100)


# V3. contrôle 12, coupe dans les tâches, 64 tâches, une cellule ; variante Ue = U (mêmes tâches)
def c12_intra(rng, reps, taches, K_cal, a, n_sab, K, meme_U=False):
    promus = 0
    for _ in range(reps):
        U = rng.standard_normal((taches, 1))
        zc = math.sqrt(a) * U + math.sqrt(1 - a) * rng.standard_normal((taches, K_cal))
        h1, h2 = zc[:, : K_cal // 2].ravel(), zc[:, K_cal // 2:].ravel()
        s1, s2 = A2.seuil_conforme(-np.sort(-h1)), A2.seuil_conforme(-np.sort(-h2))
        Ue = U[:n_sab] if meme_U else rng.standard_normal((n_sab, 1))
        sab = math.sqrt(a) * Ue + math.sqrt(1 - a) * rng.standard_normal((n_sab, K)) + A2.D_PRIME
        v = ((sab > s1).mean(axis=1) - (sab > s2).mean(axis=1))[None, :]
        promus += bool((A2.log_richesse(v)[0] >= math.log(20.0)).any())
    return promus / reps

V3 = {}
for a in (0.0, 0.2, 0.3):
    for K_cal in (16, 30, 50, 75, 100, 150):
        for meme in (False, True):
            V3[f"a={a}|N={64*K_cal}|Ue=U:{meme}"] = c12_intra(A2.rng_de(G, "V3", a, K_cal, meme), R, 64, K_cal, a, 64, 10, meme)
out["V3_controle12_intra_une_cellule"] = V3
print("V3", round(time.time() - t0), file=sys.stderr)


# V4. lisibilité jointe : M cellules × 2 modes, moitiés partagées, coupe dans les tâches.
# Cellule c : Z = √a·U_t + √(1−a)·(√ρ·E + √(1−ρ)·N_c) ; ρ = corrélation intra-épisode entre cellules.
# Les deux modes ont des épisodes sabotés distincts sur les mêmes tâches (U partagé).
def lisibilite(rng, reps, M, rho, K_cal, a, n=64, K=10, seuil=20.0):
    union, une = 0, 0
    sa, sr = math.sqrt(a), math.sqrt(1 - a)
    for _ in range(reps):
        U = rng.standard_normal((n, 1))
        E = rng.standard_normal((n, K_cal))
        Nc = rng.standard_normal((M, n, K_cal))
        zc = sa * U + sr * (math.sqrt(rho) * E + math.sqrt(1 - rho) * Nc)  # (M, n, K_cal)
        h1 = zc[:, :, : K_cal // 2].reshape(M, -1)
        h2 = zc[:, :, K_cal // 2:].reshape(M, -1)
        s1 = A2.seuil_conforme(-np.sort(-h1, axis=1))  # (M,)
        s2 = A2.seuil_conforme(-np.sort(-h2, axis=1))
        promu = []
        for _mode in range(2):
            Es = rng.standard_normal((n, K))
            Ns = rng.standard_normal((M, n, K))
            zs = sa * U + sr * (math.sqrt(rho) * Es + math.sqrt(1 - rho) * Ns) + A2.D_PRIME
            v = (zs > s1[:, None, None]).mean(axis=2) - (zs > s2[:, None, None]).mean(axis=2)  # (M, n)
            lw = A2.log_richesse(v)
            promu.append((lw.max(axis=1) >= math.log(seuil)))
        promu = np.array(promu)  # (2, M)
        union += bool(promu.any())
        une += bool(promu[:, 0].any())
    return {"union_cellules_modes": union / reps, "une_cellule_deux_modes": une / reps}

V4 = {}
R4 = max(500, R // 2)
for K_cal in (75, 150):
    for M, rho in ((1, 0.0), (8, 0.0), (8, 0.8)):
        for a in (0.0, 0.3):
            V4[f"M={M}|rho={rho}|a={a}|N={64*K_cal}"] = lisibilite(A2.rng_de(G, "V4", M, rho, K_cal, a), R4, M, rho, K_cal, a)
# seuil corrigé (Bonferroni 2M/α = 320) proposé par C
for K_cal in (75, 150):
    V4[f"M=8|rho=0.0|a=0.3|N={64*K_cal}|seuil=320"] = lisibilite(A2.rng_de(G, "V4b", K_cal), R4, 8, 0.0, K_cal, 0.3, seuil=320.0)
out["V4_lisibilite_jointe"] = V4
print("V4", round(time.time() - t0), file=sys.stderr)

# V5. intersection-union (20/10/10) : 96 × K contre 64 × K
V5 = {}
for n, K in ((64, 10), (64, 5), (64, 3), (96, 3), (96, 5), (96, 6), (96, 7), (96, 10)):
    V5[f"n={n}|K={K}"] = A2.intersection_union(A2.rng_de(G, "V5", n, K), R, n, K, 0.20, 0.10, 0.10)["min_trois"][20.0]
out["V5_intersection_union_20_10_10"] = V5

# V6. un comparateur, 10 points, S1 et S2 : 96 × 6 et 96 × 7 (interpolations de A et C)
V6 = {}
for sc in ("S1_noir_contre_blanc_effet_consigne", "S2_blanc_contre_blanc_concordant"):
    for n, K in ((64, 10), (96, 5), (96, 6), (96, 7), (96, 10), (64, 3), (64, 5)):
        V6[f"{sc[:2]}|n={n}|K={K}"] = A2.puissance(A2.rng_de(G, "V6", sc, n, K), R, n, K, 0.10, sc)[0][20.0]
out["V6_un_comparateur_10pts"] = V6

# V7. tranche de l'organisme à 24 unités (C, riposte), 20 points, K = 10, seuil 20
V7 = {}
for sc in ("S1_noir_contre_blanc_effet_consigne", "S2_blanc_contre_blanc_concordant"):
    for n in (16, 24, 32):
        V7[f"{sc[:2]}|n={n}"] = A2.puissance(A2.rng_de(G, "V7", sc, n), R, n, 10, 0.20, sc)[0][20.0]
out["V7_organisme_20pts"] = V7

# V8. reproduction à graine neuve de quelques cellules de A1 § 2
V8 = {}
for sc in ("S1_noir_contre_blanc_effet_consigne", "S2_blanc_contre_blanc_concordant"):
    for K in (3, 10):
        V8[f"{sc[:2]}|n=64|ecart=0.05|K={K}"] = A2.puissance(A2.rng_de(G, "V8", sc, K), R, 64, K, 0.05, sc)[0][20.0]
out["V8_5pts_64"] = V8
out["duree_s"] = round(time.time() - t0, 1)
print(json.dumps(out, ensure_ascii=False, indent=1))
