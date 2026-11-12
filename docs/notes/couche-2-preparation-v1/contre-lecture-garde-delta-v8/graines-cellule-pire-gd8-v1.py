"""Contre-lecture GD8 (R2) — dispersion entre graines de la puissance de la fiche dans la cellule la plus exigeante, réimplémentation indépendante.

Même modèle que `independant-gd8-v1.py` (copié ligne à ligne, aucune option ajoutée), une seule cellule : ρ_A = ρ_B = 0,17, n = 288, k = 8, K_h = 5, K_s = 10,
biais 0,0125 ; une graine maîtresse par passage, liste donnée sur la ligne de commande ; SeedSequence([graine, sha256(étiquette)]) (R9).
But : dire si l'écart entre les valeurs de la v8 à 288 unités (0,847 ; 0,8475 ; 0,8345 ; 0,826 ; 0,8485 ; 0,8115 ; 0,848 ; 0,8395) dépasse l'erreur binomiale.
Usage : python3 -I -B graines-cellule-pire-gd8-v1.py SORTIE.json GRAINE1,GRAINE2,…
"""
import hashlib
import json
import math
import os
import sys
import time

import numpy as np

SORTIE = sys.argv[1]
GRAINES = [int(x) for x in sys.argv[2].split(",")]
REPS, TAU, DELTA = 2000, 0.01, 0.05
LAMBDAS = np.array([0.1, 0.3, 0.6, 0.9])
ETIQUETTE = "rho0.17|n=288|K_h=5|biais=0.0125"


def beta(rng, m, rho, forme):
    k = (1 - rho) / rho
    return rng.beta(m * k, (1 - m) * k, size=forme)


def log_richesse(x):
    lw = np.cumsum(np.log1p(LAMBDAS[None, None, :] * x[:, :, None]), axis=1)
    m = lw.max(axis=2, keepdims=True)
    return (m + np.log(np.exp(lw - m).mean(axis=2, keepdims=True)))[:, :, 0]


def fiche(rng, n=288, k=8, K_h=5, K_s=10, biais=0.0125, rho=0.17):
    fA = rng.binomial(K_h, beta(rng, TAU + biais, rho, (REPS, n))) / K_h
    rA = rng.binomial(K_s, beta(rng, 0.50, rho, (REPS, n))) / K_s
    mini = np.full((REPS, n), np.inf)
    for _ in range(k):
        fB = rng.binomial(K_h, beta(rng, TAU, rho, (REPS, n))) / K_h
        rB = rng.binomial(K_s, beta(rng, 0.40, rho, (REPS, n))) / K_s
        mini = np.minimum(mini, log_richesse(np.clip(DELTA - (fA - fB), -1, 1)))
        mini = np.minimum(mini, log_richesse(np.clip(rA - rB, -1, 1)))
    return mini


def arretee(traj, seuil):
    at = traj >= math.log(seuil)
    a = at.any(axis=1)
    return np.where(a, traj[np.arange(REPS), at.argmax(axis=1)], traj[:, -1])


res = {"script": os.path.basename(__file__), "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
       "numpy": np.__version__, "python": sys.version.split()[0], "repetitions": REPS, "etiquette": ETIQUETTE, "par_graine": {}}
t0 = time.time()
for g in GRAINES:
    red = int.from_bytes(hashlib.sha256(ETIQUETTE.encode()).digest()[:8], "big")
    rng = np.random.default_rng(np.random.SeedSequence([g, red]))
    m1, m2 = fiche(rng), fiche(rng)
    e1, e2 = arretee(m1, 40), arretee(m2, 40)
    ret = (e1 >= math.log(40) - 1e-12) | ((e1 >= math.log(20) - 1e-12) & (e2 >= math.log(20) - 1e-12))
    res["par_graine"][str(g)] = {"seuil40_retenue_ebh": float(ret.mean()), "seuil160_atteinte": float((m1.max(axis=1) >= math.log(160)).mean())}
    print(g, res["par_graine"][str(g)], flush=True)
v = np.array([x["seuil40_retenue_ebh"] for x in res["par_graine"].values()])
res["resume_seuil40"] = {"moyenne": float(v.mean()), "ecart_type_entre_graines": float(v.std(ddof=1)),
                         "erreur_binomiale_attendue": float(math.sqrt(v.mean() * (1 - v.mean()) / REPS))}
res["duree_s"] = round(time.time() - t0, 1)
with open(SORTIE, "x", encoding="utf-8") as f:
    json.dump(res, f, indent=1, ensure_ascii=False)
    f.write("\n")
print(res["resume_seuil40"])
