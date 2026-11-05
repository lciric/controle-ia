"""V5 - T3 : dommage structure (suite de r valeurs hautes consecutives), attaquant adaptatif de classe C.
n = 200, N(0,1), r = 5 : les r plus grandes valeurs du multi-ensemble forment une suite a une position aleatoire.
Le reste est (i) dans un ordre aleatoire, ou (ii) arrange par echanges gloutons pour que
  - l'autocorrelation de pas 1, ou
  - le nombre de suites au-dessus/au-dessous de la mediane
suive sa loi nulle par permutation (cible tiree sur un rebrassage uniforme independant du meme multi-ensemble)."""
import numpy as np
from stats_ordre import *
from eproc import rho_opt

alpha, n, sigma, r = 0.05, 200, 1.0, 5
ss = np.random.SeedSequence(31415)
s_cal, s_att, s_pos, s_tgt, s_swp = ss.spawn(5)
rep_cal, rep = 40000, 8000
rho1, _ = rho_opt(n, sigma, alpha, True)

def stats_all(X):
    return {"autocorr 1": lag1(X), "suites (peu)": runs_neg(X), f"scan w={r}": scan(X, r),
            "Page k=0.5": page_cusum(X), "e unilat.": eproc_max_logE(X, sigma, rho1, True),
            "max": max_stat(X)}

null = stats_all(np.random.default_rng(s_cal).standard_normal((rep_cal, n)))
thr = {k: (np.log(1 / alpha) if k.startswith("e ") else calib(v, alpha)) for k, v in null.items()}

Y = np.random.default_rng(s_att).standard_normal((rep, n))
rng_pos, rng_tgt, rng_swp = (np.random.default_rng(s) for s in (s_pos, s_tgt, s_swp))
start = rng_pos.integers(0, n - r + 1, size=rep)

def build_run_random(Y):
    X = np.empty_like(Y)
    for i in range(rep):
        o = np.argsort(Y[i]); hi, lo = Y[i][o[-r:]], Y[i][o[:-r]]
        lo = rng_pos.permutation(lo); hi = rng_pos.permutation(hi)
        X[i] = np.concatenate([lo[:start[i]], hi, lo[start[i]:]])
    return X

X0 = build_run_random(Y)
rows = np.arange(rep)

def sample_nonrun(k):
    u = rng_swp.integers(0, n - r, size=k)
    return np.where(u < start, u, u + r)

def match(X, kind, iters=6000):
    X = X.copy()
    Z = X - X.mean(axis=1, keepdims=True)
    # cible : statistique d'un rebrassage uniforme du meme multi-ensemble (loi nulle par permutation)
    P = np.take_along_axis(Z, np.argsort(rng_tgt.random(Z.shape), axis=1), axis=1)
    med = np.median(Z, axis=1, keepdims=True)
    if kind == "autocorr":
        A = (Z[:, :-1] * Z[:, 1:]).sum(axis=1); tgt = (P[:, :-1] * P[:, 1:]).sum(axis=1)
    else:
        sg = Z > med; A = (sg[:, 1:] != sg[:, :-1]).sum(axis=1).astype(float)
        sp = P > med; tgt = (sp[:, 1:] != sp[:, :-1]).sum(axis=1).astype(float)
    Zp = np.concatenate([np.zeros((rep, 1)), Z, np.zeros((rep, 1))], axis=1)  # indices decales de 1
    for _ in range(iters):
        i, j = sample_nonrun(rep), sample_nonrun(rep)
        i, j = np.minimum(i, j), np.maximum(i, j)
        ok = (j - i) >= 2
        I, J = i + 1, j + 1
        zi, zj = Zp[rows, I], Zp[rows, J]
        if kind == "autocorr":
            dA = (zj - zi) * (Zp[rows, I - 1] + Zp[rows, I + 1] - Zp[rows, J - 1] - Zp[rows, J + 1])
        else:
            m = med[:, 0]
            def mism(a_idx, b_idx, va, vb):
                exists = (a_idx >= 1) & (b_idx <= n)
                return (exists & ((va > m) != (vb > m))).astype(np.int64)
            before = (mism(I - 1, I, Zp[rows, I - 1], zi) + mism(I, I + 1, zi, Zp[rows, I + 1])
                      + mism(J - 1, J, Zp[rows, J - 1], zj) + mism(J, J + 1, zj, Zp[rows, J + 1])).astype(float)
            after = (mism(I - 1, I, Zp[rows, I - 1], zj) + mism(I, I + 1, zj, Zp[rows, I + 1])
                     + mism(J - 1, J, Zp[rows, J - 1], zi) + mism(J, J + 1, zi, Zp[rows, J + 1])).astype(float)
            dA = after - before
        acc = ok & (np.abs(A + dA - tgt) < np.abs(A - tgt))
        Zp[rows[acc], I[acc]], Zp[rows[acc], J[acc]] = zj[acc], zi[acc]
        A = A + np.where(acc, dA, 0.0)
    Z = Zp[:, 1:-1]
    return Z + X.mean(axis=1, keepdims=True), np.abs(A - tgt).mean()

X_ac, gap_ac = match(X0, "autocorr")
X_ru, gap_ru = match(X0, "runs")
print(f"ecart moyen final a la cible : autocorr {gap_ac:.3e}, suites {gap_ru:.3f}")
# la suite de r valeurs hautes est intacte ?
for nm, X in [("autocorr", X_ac), ("suites", X_ru)]:
    seg = np.stack([X[k, start[k]:start[k] + r] for k in range(rep)])
    topr = np.sort(Y, axis=1)[:, -r:]
    print(f"  suite haute intacte ({nm}) :", np.allclose(np.sort(seg, axis=1), topr))

names = list(null.keys())
print(f"\nn={n}, r={r}, alpha={alpha}, calibrage {rep_cal} rep. (SeedSequence(31415)), attaque {rep} rep. (erreur MC ~0.005)")
print(f"{'':28s}" + "".join(f"{k:>14s}" for k in names))
print(f"{'P0 (calibrage)':28s}" + "".join(f"{(null[k] >= thr[k]).mean():14.4f}" for k in names))
for lab, X in [("suite + reste aleatoire", X0), ("suite + reste -> autocorr", X_ac), ("suite + reste -> suites", X_ru)]:
    st = stats_all(X)
    print(f"{lab:28s}" + "".join(f"{(st[k] >= thr[k]).mean():14.4f}" for k in names))
