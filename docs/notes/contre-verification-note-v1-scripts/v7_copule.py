"""V7 - mise en garde : copule gaussienne AR(1) a marginale par pas preservee.
X_k = F0^{-1}(Phi(Z_k)), Z AR(1) stationnaire de coefficient phi. n0 = 200, alpha = 0.05.
Seuils calibres sous P0 iid (meme marginale). Puissance = taux d'alarme sous la copule."""
import numpy as np
from scipy import stats
from stats_ordre import *
from eproc import rho_opt

alpha, n0, sigma = 0.05, 200, 1.0
ss = np.random.SeedSequence(16180339)
seeds = iter(ss.spawn(32))
rho1, _ = rho_opt(n0, sigma, alpha, True)
rho2, _ = rho_opt(n0, sigma, alpha, False)

def ar1(g, R, n, phi):
    Z = np.empty((R, n)); Z[:, 0] = g.standard_normal(R)
    e = g.standard_normal((R, n)) * np.sqrt(1 - phi**2)
    for k in range(1, n):
        Z[:, k] = phi * Z[:, k - 1] + e[:, k]
    return Z

margs = {"N(0,1)": lambda Z: Z, "Exp(1)-1": lambda Z: stats.expon.ppf(stats.norm.cdf(Z)) - 1.0}

def S(X):
    return {"moy. unilat.": X.sum(axis=1), "moy. bilat.": np.abs(X.sum(axis=1)), "max": X.max(axis=1),
            "e unilat.": eproc_max_logE(X, sigma, rho1, True), "e bilat.": eproc_max_logE(X, sigma, rho2, False),
            "scan w=10": scan(X, 10), "Page k=0.5": page_cusum(X), "autocorr 1": lag1(X), "|autocorr 1|": np.abs(lag1(X))}

for mname, tr in margs.items():
    X0 = tr(np.random.default_rng(next(seeds)).standard_normal((40000, n0)))
    nul = S(X0)
    thr = {k: (np.log(1 / alpha) if k.startswith("e ") else calib(v, alpha)) for k, v in nul.items()}
    names = list(nul.keys())
    print(f"\nmarginale {mname} ; calibrage 40000 rep., copule 20000 rep.")
    print(f"{'':12s}" + "".join(f"{k:>13s}" for k in names))
    print(f"{'P0 iid':12s}" + "".join(f"{(nul[k] >= thr[k]).mean():13.4f}" for k in names))
    for phi in [-0.5, 0.2, 0.5, 0.8]:
        X = tr(ar1(np.random.default_rng(next(seeds)), 20000, n0, phi))
        st = S(X)
        print(f"{'phi=%+.1f' % phi:12s}" + "".join(f"{(st[k] >= thr[k]).mean():13.4f}" for k in names))
# reference analytique (gaussien) : puissance du test de moyenne unilateral = Phibar(z_a / sqrt(v_n))
for phi in [-0.5, 0.2, 0.5, 0.8]:
    v = (1 + phi) / (1 - phi) - 2 * phi * (1 - phi**n0) / (n0 * (1 - phi)**2)
    print(f"analytique phi={phi:+.1f}: facteur de variance v_n={v:.3f}, puissance moyenne unilat. = {stats.norm.sf(stats.norm.isf(alpha)/np.sqrt(v)):.4f}")
print("Graine : SeedSequence(16180339)")
