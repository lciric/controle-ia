"""V9 - T4 : '<= alpha' ou seulement '<= taux sous P0' ?
P0 echangeable non iid (effet episode u ~ N(0, tau^2), var totale 1), regle unilaterale calibree pour N(0,1) iid.
n0 = 200, alpha = 0.05. Arrangements : honnete, tri croissant, r=10 plus hautes a la fin."""
import numpy as np
from stats_ordre import eproc_max_logE
from eproc import rho_opt

alpha, n0, R, r = 0.05, 200, 20000, 10
rho1, _ = rho_opt(n0, 1.0, alpha, True)
ss = np.random.SeedSequence(14142135)
for tau, s in zip([0.0, 0.1, 0.2], ss.spawn(3)):
    g = np.random.default_rng(s)
    Y = g.normal(0, tau, size=(R, 1)) + np.sqrt(1 - tau**2) * g.standard_normal((R, n0))
    srt = np.sort(Y, axis=1)
    o = np.argsort(Y, axis=1); top = np.zeros_like(Y, bool); np.put_along_axis(top, o[:, -r:], True, axis=1)
    hf = np.stack([np.concatenate([Y[i][~top[i]], Y[i][top[i]]]) for i in range(R)])
    a = {k: (eproc_max_logE(M, 1.0, rho1, True) >= np.log(1 / alpha)).mean() for k, M in
         [("honnete", Y), ("tri", srt), ("haut_fin", hf)]}
    print(f"tau={tau:.1f} : alarme honnete {a['honnete']:.4f} | tri croissant {a['tri']:.4f} | {r} plus hautes a la fin {a['haut_fin']:.4f}")
print("Graine : SeedSequence(14142135), 20000 rep.")
