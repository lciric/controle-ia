"""Complément V4 : lisibilité jointe à 8 cellules × 2 modes, tailles plus grandes et seuils de diagnostic corrigés.
Exploratoire, processeur, non opposable. Graine 20261029 + étiquette « V4c »."""
import importlib.util, json, sys, runpy
ns = runpy.run_path(sys.argv[1].replace("simulation-couche-2-executions-v1.py", "verifications-synthese-v1.py"),
                    run_name="pas_main") if False else None
spec = importlib.util.spec_from_file_location("simA2", sys.argv[1]); A2 = importlib.util.module_from_spec(spec); spec.loader.exec_module(A2)
import math, numpy as np
def lisibilite(rng, reps, M, rho, K_cal, a, n=64, K=10, seuil=20.0):
    union = 0; sa, sr = math.sqrt(a), math.sqrt(1 - a)
    for _ in range(reps):
        U = rng.standard_normal((n, 1)); E = rng.standard_normal((n, K_cal)); Nc = rng.standard_normal((M, n, K_cal))
        zc = sa * U + sr * (math.sqrt(rho) * E + math.sqrt(1 - rho) * Nc)
        s1 = A2.seuil_conforme(-np.sort(-zc[:, :, :K_cal // 2].reshape(M, -1), axis=1))
        s2 = A2.seuil_conforme(-np.sort(-zc[:, :, K_cal // 2:].reshape(M, -1), axis=1))
        p = False
        for _m in range(2):
            Es = rng.standard_normal((n, K)); Ns = rng.standard_normal((M, n, K))
            zs = sa * U + sr * (math.sqrt(rho) * Es + math.sqrt(1 - rho) * Ns) + A2.D_PRIME
            v = (zs > s1[:, None, None]).mean(axis=2) - (zs > s2[:, None, None]).mean(axis=2)
            p = p or bool((A2.log_richesse(v).max(axis=1) >= math.log(seuil)).any())
        union += p
    return union / reps
G = 20261029; R = 1000; out = {}
for K_cal in (200, 300):
    for rho in (0.0, 0.8):
        out[f"M=8|rho={rho}|a=0.3|N={64*K_cal}|seuil=20"] = lisibilite(A2.rng_de(G, "V4c", K_cal, rho), R, 8, rho, K_cal, 0.3)
for K_cal in (75, 150):
    for s in (40.0, 80.0, 160.0):
        out[f"M=8|rho=0.0|a=0.3|N={64*K_cal}|seuil={int(s)}"] = lisibilite(A2.rng_de(G, "V4d", K_cal, s), R, 8, 0.0, K_cal, 0.3, seuil=s)
print(json.dumps(out, indent=1))
