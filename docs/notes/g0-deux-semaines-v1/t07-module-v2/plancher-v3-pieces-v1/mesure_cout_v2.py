"""v2 (machine au repos, après le redémarrage du conteneur ; même code que la v1). Mesure, sur le processeur de la session, du débit de la notation vectorisée du plancher v3 (800 directions, largeur 4 096), de la
boucle du harnais (référence), et de la covariance et du tirage (plancher_apparie) ; sortie JSON (argument 1)."""
import json, os, sys, time, platform
import numpy as np
sys.path.insert(0, "src")
from controle_ia.sondes.evaluation import plancher_apparie
from controle_ia.t07 import plancher_v1 as pl, plancher_v3 as p3
rng = np.random.default_rng(0)
d, k = 4096, 800
res = {"machine": platform.processor() or platform.machine(), "coeurs": os.cpu_count(), "openblas_fils": os.environ.get("OPENBLAS_NUM_THREADS")}
# actions de 225 jetons (≈ 1,3 million de jetons par couche pour 5 760 actions)
seqs = [rng.standard_normal((225, d)).astype(np.float32) for _ in range(40)]
jetons = sum(len(s) for s in seqs)
X = [rng.standard_normal((50, d)) for _ in range(60)]
for ag in ("max", "attention"):
    P = plancher_apparie("x", 15, X, ag, k, 1)
    t0 = time.perf_counter(); V = p3.scores_plancher_vectorises(P, seqs, controle=0); t = time.perf_counter() - t0
    res[f"vectorisee_{ag}_s_par_million_de_jetons"] = round(t / jetons * 1e6, 2)
    t0 = time.perf_counter(); B = pl.scores_plancher(P[:20], seqs[:10]); tb = time.perf_counter() - t0
    res[f"boucle_{ag}_us_par_direction_et_action_225_jetons"] = round(tb / (20 * 10) * 1e6, 1)
    t0 = time.perf_counter(); p3.controler_contre_la_boucle(P, seqs, V, 2); tc = time.perf_counter() - t0
    res[f"controle_en_ligne_{ag}_s_par_action"] = round(tc / len(seqs), 5)
# covariance et tirage (enjeux : ≈ 114 500 jetons ; ici 20 000 jetons, extrapolé linéairement en jetons)
Xc = [rng.standard_normal((100, d)).astype(np.float32) for _ in range(200)]
t0 = time.perf_counter(); P = plancher_apparie("y", 15, Xc, "max", 800, 2); tp = time.perf_counter() - t0
res["plancher_apparie_800_s_pour_20000_jetons"] = round(tp, 1)
print(json.dumps(res, ensure_ascii=False))
open(sys.argv[1], "w").write(json.dumps(res, ensure_ascii=False, indent=1) + "\n")
