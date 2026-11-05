"""V3 - L3 : calendrier du sabotage (classe M), regle toujours valide E_n >= 1/alpha.
Gaussien N(0,1), n0 = 200 (N=1, T=200), alpha = 0.05, B/sigma = 25. Couplage : memes Y pour tous les calendriers."""
import numpy as np
from scipy import stats
from eproc import logE, alarm_any, rho_opt

alpha, n0, sigma, B = 0.05, 200, 1.0, 25.0
reps = 40000
ss = np.random.SeedSequence(20261004)
rng = np.random.default_rng(ss.spawn(1)[0])
Y = rng.standard_normal((reps, n0))

for one_sided in [True, False]:
    rho, bnd = rho_opt(n0, sigma, alpha, one_sided)
    lab = "unilateral" if one_sided else "bilateral"
    a0, _ = alarm_any(Y, sigma, rho, alpha, one_sided)
    # borne terminale P(E_n0 >= 1/alpha), S_n0 ~ N(B, n0)
    if one_sided:
        term = stats.norm.sf((bnd - B) / np.sqrt(n0))
    else:
        term = stats.norm.sf((bnd - B) / np.sqrt(n0)) + stats.norm.cdf((-bnd - B) / np.sqrt(n0))
    z_fixed = stats.norm.sf(stats.norm.isf(alpha) - B / np.sqrt(n0))
    print(f"\n[{lab}] rho={rho:.4f}, frontiere a n0 : {bnd:.2f} ; P0(alarme d'ici n0) = {a0.mean():.4f}")
    print(f"   borne terminale P(E_n0>=1/alpha) = {term:.4f} ; z-test unilateral a horizon fixe = {z_fixed:.4f}")
    for m in [1, 10, 50, 200]:
        res = {}
        for sched in ["avance", "uniforme", "reporte"]:
            d = np.zeros(n0)
            if sched == "avance":
                d[:m] = B / m; last = m - 1
            elif sched == "reporte":
                d[n0 - m:] = B / m; last = n0 - 1
            else:
                idx = np.round(np.linspace(0, n0 - 1, m)).astype(int); d[idx] = B / m; last = idx[-1]
            hit, first = alarm_any(Y + d[None, :], sigma, rho, alpha, one_sided)
            before_last = (first < last).mean()   # alarme strictement avant la derniere action sabotee
            res[sched] = (hit.mean(), before_last)
        print(f"   m={m:3d} : " + " | ".join(f"{k}: alarme d'ici n0 {v[0]:.3f}, avant derniere action sabotee {v[1]:.3f}" for k, v in res.items()))
print(f"\nreps={reps}, graine SeedSequence(20261004), erreur MC ~ {np.sqrt(0.25/reps):.4f}")
