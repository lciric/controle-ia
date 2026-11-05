"""Contre-lecture GD8 (R2) — l'écart d'environ 0,01 entre la réimplémentation indépendante et la v8 (retenue e-BH à 288 unités, ρ = 0,17, K_h = 5,
biais 0,0125) est-il réel ? Test apparié en graines : pour chaque graine g, deux familles de deux fiches, l'une tirée par `processus` de la v8 (chargé
depuis son fichier, empreinte vérifiée, non modifié), l'autre par la réimplémentation de `independant-gd8-v1.py` ; la même règle e-BH (`retenues_famille`
de la v8, vérifiée identique à la règle écrite à la main, `cellule-contre-point` et essai du rapport) est appliquée aux deux. Rend la retenue et
l'atteinte de 40 et de 160 par graine, et la différence moyenne avec son erreur type.
Usage : python3 -I -B test-ecart-gd8-v1.py SCRIPT_V8 SORTIE.json G1,G2,…
"""
import hashlib
import importlib.util
import json
import math
import os
import sys

import numpy as np

SCRIPT, SORTIE = sys.argv[1:3]
GRAINES = [int(x) for x in sys.argv[3].split(",")]
assert hashlib.sha256(open(SCRIPT, "rb").read()).hexdigest() == "4c7c93a90e0be922e839f5826488edcc0745bde17f8a5de22f3a2a41bf75f1d1"
spec = importlib.util.spec_from_file_location("v8", SCRIPT)
v8 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v8)
REPS = 2000
LAM = np.array([0.1, 0.3, 0.6, 0.9])
loi = v8.LoiSynthetique(5, 10, 0.01, 0.40, 0.10, partage=True, effet_beta=0.17, echelle_b="beta", rho_b=0.17)


def lr(x):
    lw = np.cumsum(np.log1p(LAM[None, None, :] * x[:, :, None]), axis=1)
    m = lw.max(axis=2, keepdims=True)
    return (m + np.log(np.exp(lw - m).mean(axis=2, keepdims=True)))[:, :, 0]


def beta(rng, m, rho, f):
    k = (1 - rho) / rho
    return rng.beta(m * k, (1 - m) * k, size=f)


def fiche_indep(rng, n=288):
    fA = rng.binomial(5, beta(rng, 0.0225, 0.17, (REPS, n))) / 5
    rA = rng.binomial(10, beta(rng, 0.5, 0.17, (REPS, n))) / 10
    F = np.full((REPS, n), np.inf)
    for _ in range(8):
        fB = rng.binomial(5, beta(rng, 0.01, 0.17, (REPS, n))) / 5
        rB = rng.binomial(10, beta(rng, 0.4, 0.17, (REPS, n))) / 10
        F = np.minimum(F, lr(np.clip(0.05 - (fA - fB), -1, 1)))
        F = np.minimum(F, lr(np.clip(rA - rB, -1, 1)))
    return F


def fiche_v8(rng):
    g, c = v8.processus(loi, rng, REPS, 288, 288, 8, 0.05, 0.0125, None)
    return np.minimum(g.min(axis=0), c.min(axis=0))


def mesures(f1, f2):
    _, _, ret = v8.retenues_famille([f1, f2], 2, 0.05)
    return {"retenue40": float(ret[:, 0].mean()), "atteinte40": float((f1.max(axis=1) >= math.log(40)).mean()),
            "atteinte160": float((f1.max(axis=1) >= math.log(160)).mean())}


res = {"script": os.path.basename(__file__), "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(), "numpy": np.__version__,
       "graines": GRAINES, "par_graine": {}}
for g in GRAINES:
    r_v8 = np.random.default_rng(np.random.SeedSequence([g, 8]))
    r_in = np.random.default_rng(np.random.SeedSequence([g, 9]))
    a = mesures(fiche_v8(r_v8), fiche_v8(r_v8))
    b = mesures(fiche_indep(r_in), fiche_indep(r_in))
    res["par_graine"][str(g)] = {"v8": a, "independant": b}
    print(g, a, b, flush=True)
for m in ("retenue40", "atteinte40", "atteinte160"):
    d = np.array([x["v8"][m] - x["independant"][m] for x in res["par_graine"].values()])
    res[f"difference_{m}"] = {"moyenne_v8_moins_independant": float(d.mean()), "erreur_type": float(d.std(ddof=1) / math.sqrt(len(d))) if len(d) > 1 else None}
with open(SORTIE, "x", encoding="utf-8") as f:
    json.dump(res, f, indent=1, ensure_ascii=False)
    f.write("\n")
print({k: v for k, v in res.items() if k.startswith("difference")})
