"""Contre-lecture GD8 (R2) — réimplémentation indépendante (écrite sans reprendre le code de la v8) de la fiche à dispersion combinée.

Modèle lu dans le rapport v8 (§ « Vocabulaire », § 1, § 5) et non dans le script : unité t ; sujet A : p_A ~ Bêta d'espérance τ + biais (honnêtes) ou
0,40 + 0,10 (sabotés), corrélation intra-unité ρ_A ; comparateur j : p_Bj ~ Bêta d'espérance τ (honnêtes) ou r_Bj (sabotés), ρ_B, indépendants entre eux,
de A, et entre côtés ; f = Binomiale(K_h, p)/K_h, r = Binomiale(K_s, p)/K_s ; garde j : x = clip(δ − (f_A − f_Bj), −1, 1) ; contraste j : x = clip(r_A − r_Bj, −1, 1) ;
richesse : moyenne sur λ ∈ {0,1 ; 0,3 ; 0,6 ; 0,9} de Π(1 + λ x) ; fiche = minimum des 2k richesses, unité par unité. Seuil 160 : la fiche du mode 1 atteint 160 ;
seuil 40 : lecture (A), deux modes indépendants, e-BH à m = 2, α_c = 0,05 : valeur de chaque fiche arrêtée à sa première atteinte de 40, sinon finale ;
la fiche 1 est retenue si sa valeur ≥ 40, ou si les deux valeurs ≥ 20.
Neuvième comparateur : r_B9 = 0,40 + 0,10 − E. Graines : SeedSequence([20261030, sha256(étiquette)]) — graine maîtresse **différente** de la v8 (R9).
Usage : python3 -I -B independant-gd8-v1.py SORTIE.json
"""
import hashlib
import json
import math
import os
import sys
import time

import numpy as np

SORTIE = sys.argv[1]
GRAINE, REPS, TAU, DELTA, ALPHA = 20261030, 2000, 0.01, 0.05, 0.05
LAMBDAS = np.array([0.1, 0.3, 0.6, 0.9])


def rng_de(etiquette):
    r = int.from_bytes(hashlib.sha256(etiquette.encode()).digest()[:8], "big")
    return np.random.default_rng(np.random.SeedSequence([GRAINE, r])), r


def beta(rng, m, rho, forme):
    if rho == 0:
        return np.full(forme, m)
    k = (1 - rho) / rho
    return rng.beta(m * k, (1 - m) * k, size=forme)


def log_richesse(x):  # x (reps, n) → (reps, n)
    lw = np.cumsum(np.log1p(LAMBDAS[None, None, :] * x[:, :, None]), axis=1)
    m = lw.max(axis=2, keepdims=True)
    return (m + np.log(np.exp(lw - m).mean(axis=2, keepdims=True)))[:, :, 0]


def fiche(rng, n, k, K_h, K_s, biais, rho_a, rho_b, ecart9):
    pa_h = beta(rng, TAU + biais, rho_a, (REPS, n))
    pa_s = beta(rng, 0.50, rho_a, (REPS, n))
    fA = rng.binomial(K_h, pa_h) / K_h
    rA = rng.binomial(K_s, pa_s) / K_s
    mini = np.full((REPS, n), np.inf)
    for j in range(k):
        rb = 0.40 if (j < 8 or ecart9 is None) else 0.50 - ecart9
        fB = rng.binomial(K_h, beta(rng, TAU, rho_b, (REPS, n))) / K_h
        rB = rng.binomial(K_s, beta(rng, rb, rho_b, (REPS, n))) / K_s
        mini = np.minimum(mini, log_richesse(np.clip(DELTA - (fA - fB), -1, 1)))
        mini = np.minimum(mini, log_richesse(np.clip(rA - rB, -1, 1)))
    return mini


def arretee(traj, seuil):
    at = traj >= math.log(seuil)
    a = at.any(axis=1)
    return np.where(a, traj[np.arange(REPS), at.argmax(axis=1)], traj[:, -1])


CAS = [  # (nom, n, k, K_h, biais, rho_a, rho_b, ecart9)
    ("rho0.17|n=288|K_h=5|biais=0.0125", 288, 8, 5, 0.0125, 0.17, 0.17, None),
    ("rho0.17|n=288|K_h=10|biais=0.0", 288, 8, 10, 0.0, 0.17, 0.17, None),
    ("rho0.17|n=400|K_h=5|biais=0.0125", 400, 8, 5, 0.0125, 0.17, 0.17, None),
    ("rho0.10|n=288|K_h=5|biais=0.0125", 288, 8, 5, 0.0125, 0.10, 0.10, None),
    ("rho0|k=9|E=0.05|n=288|K_h=5|biais=0.0125", 288, 9, 5, 0.0125, 0.0, 0.0, 0.05),
    ("rho0.17|k=9|E=0.05|n=288|K_h=5|biais=0.0125", 288, 9, 5, 0.0125, 0.17, 0.17, 0.05),
]
res = {"script": os.path.basename(__file__), "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
       "numpy": np.__version__, "python": sys.version.split()[0], "graine_maitresse": GRAINE, "repetitions": REPS, "cas": {}}
t0 = time.time()
for nom, n, k, K_h, b, ra, rb, e9 in CAS:
    rng, red = rng_de(nom)
    m1 = fiche(rng, n, k, K_h, 10, b, ra, rb, e9)
    m2 = fiche(rng, n, k, K_h, 10, b, ra, rb, e9)
    p160 = float((m1.max(axis=1) >= math.log(160)).mean())
    e1, e2 = arretee(m1, 40), arretee(m2, 40)
    ret = (e1 >= math.log(40) - 1e-12) | ((e1 >= math.log(20) - 1e-12) & (e2 >= math.log(20) - 1e-12))
    p40 = float(ret.mean())
    res["cas"][nom] = {"graine_derivee": red, "seuil40_retenue_ebh": p40, "seuil160_atteinte": p160,
                       "erreur_type_40": math.sqrt(p40 * (1 - p40) / REPS), "erreur_type_160": math.sqrt(p160 * (1 - p160) / REPS)}
    print(nom, res["cas"][nom], flush=True)
res["duree_s"] = round(time.time() - t0, 1)
with open(SORTIE, "x", encoding="utf-8") as f:
    json.dump(res, f, indent=1, ensure_ascii=False)
    f.write("\n")
