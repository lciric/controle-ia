"""V8 - (a) L5 : compensation a budget net nul ; (b) T2 avec P0 non echangeable (roles) ;
(c) T3 : puissance du scan selon la hauteur des valeurs de la suite."""
import numpy as np
from scipy import stats
from stats_ordre import scan, page_cusum, calib

alpha = 0.05
ss = np.random.SeedSequence(57721566)
seeds = iter(ss.spawn(32))

# (a) L5 : n0=200, 10 actions +2 sigma, 100 actions -0.2 sigma => B_net = 0
n0, R = 200, 20000
d = np.zeros(n0); d[:10] = 2.0; d[10:110] = -0.2
Y = np.random.default_rng(next(seeds)).standard_normal((R, n0))
X = Y + d
z = stats.norm.isf(alpha / 2)
c_max = stats.norm.isf(-np.expm1(np.log1p(-alpha) / n0))
q_chi = stats.chi2.isf(alpha, n0)
ks_crit = stats.kstwo.isf(alpha, n0)
def ks(Xr):
    s = np.sort(Xr, axis=1); F = stats.norm.cdf(s); i = np.arange(1, n0 + 1)
    return np.maximum((i / n0 - F).max(axis=1), (F - (i - 1) / n0).max(axis=1))
print("(a) L5, B_net = 0 (10 x +2 sigma, 100 x -0.2 sigma), n0=200, 20000 rep. :")
for lab, M in [("P0", Y), ("attaque", X)]:
    print(f"   {lab:8s} somme bilat. {(np.abs(M.sum(1)) >= z*np.sqrt(n0)).mean():.4f} | max {(M.max(1) >= c_max).mean():.4f} | "
          f"chi2 sum x^2 {((M**2).sum(1) >= q_chi).mean():.4f} | KS vs F0 {(ks(M) >= ks_crit).mean():.4f}")

# (b) T2 avec roles : N=3 agents de moyennes honnetes (-0.5, 0, +0.5), T=50 ; l'attaquant rebrasse uniformement tout I
N, T, R = 3, 50, 20000
mu = np.array([-0.5, 0.0, 0.5])[None, :, None]
g = np.random.default_rng(next(seeds))
Yh = mu + g.standard_normal((R, N, T))
flat = Yh.reshape(R, N * T)
Xs = np.take_along_axis(flat, np.argsort(g.random(flat.shape), axis=1), axis=1).reshape(R, N, T)
Y0 = mu + np.random.default_rng(next(seeds)).standard_normal((R, N, T))
stat = lambda A: A[:, 2].mean(1) - A[:, 0].mean(1)       # ecart de moyenne entre roles 3 et 1
t_low = np.quantile(stat(Y0), alpha)                      # alarme si l'ecart est anormalement petit
print(f"\n(b) T2 avec roles non echangeables (N=3, T=50) : taux d'alarme P0 {(stat(Y0) <= t_low).mean():.4f} ; "
      f"rebrassage uniforme sur tout I {(stat(Xs) <= t_low).mean():.4f}")
# rebrassage restreint au sous-groupe qui preserve P0 (temps a l'interieur de chaque agent)
Xw = np.take_along_axis(Yh, np.argsort(g.random(Yh.shape), axis=2), axis=2)
print(f"    rebrassage restreint (temps, par agent) {(stat(Xw) <= t_low).mean():.4f}")

# (c) T3 : suite de r valeurs consecutives prises juste au-dessus du quantile q du multi-ensemble, reste aleatoire
n, R = 200, 10000
Ycal = np.random.default_rng(next(seeds)).standard_normal((40000, n))
print("\n(c) T3 : puissance (scan fenetre r | Page k=0.5) quand la suite porte les r valeurs juste au-dessus du quantile q (n=200)")
thr_page = calib(page_cusum(Ycal), alpha)
for r in [3, 5, 10]:
    thr_scan = calib(scan(Ycal, r), alpha)
    row = []
    for q in [0.5, 0.7, 0.8, 0.9, 0.95, None]:
        g = np.random.default_rng(next(seeds))
        Y = np.sort(g.standard_normal((R, n)), axis=1)
        k0 = n - r if q is None else int(np.ceil(q * n))
        run = Y[:, k0:k0 + r]
        rest = np.concatenate([Y[:, :k0], Y[:, k0 + r:]], axis=1)
        rest = np.take_along_axis(rest, np.argsort(g.random(rest.shape), axis=1), axis=1)
        st = g.integers(0, n - r + 1, size=R)
        X = np.empty_like(Y)
        for i in range(R):
            X[i] = np.concatenate([rest[i, :st[i]], run[i], rest[i, st[i]:]])
        row.append(f"q={'top' if q is None else q}: {(scan(X, r) >= thr_scan).mean():.3f}|{(page_cusum(X) >= thr_page).mean():.3f}")
    print(f"   r={r:2d} :: " + "  ".join(row))
print("Graine : SeedSequence(57721566)")
