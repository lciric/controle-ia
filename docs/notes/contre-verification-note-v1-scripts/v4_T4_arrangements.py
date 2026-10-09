"""V4 - T4 : arrangements d'un multi-ensemble honnete (classe C), n0 = 200, N(0,1), alpha = 0.05.
Seuils de toutes les statistiques calibres par Monte-Carlo sous P0 (graine distincte).
Arrangements :
  honnete       : ordre d'origine (iid)
  tri_croissant : tout le vecteur trie par ordre croissant ("bas d'abord, grappe haute a la fin", version extreme)
  haut_fin      : les r plus grandes valeurs deplacees a la fin (ordre relatif conserve), le reste dans l'ordre d'origine
  haut_fin_trie : idem mais la grappe finale triee par ordre croissant
  haut_debut    : les r plus grandes valeurs au debut
"""
import numpy as np
from stats_ordre import *
from eproc import rho_opt

alpha, n0, sigma, r = 0.05, 200, 1.0, 10
ss = np.random.SeedSequence(4102026)
s_cal, s_att = ss.spawn(2)
rep_cal, rep_att = 40000, 20000

rho1, _ = rho_opt(n0, sigma, alpha, True)
rho2, _ = rho_opt(n0, sigma, alpha, False)

def all_stats(X):
    return {
        "e unilat.": eproc_max_logE(X, sigma, rho1, True),
        "e bilat.": eproc_max_logE(X, sigma, rho2, False),
        "somme term.": terminal_sum(X),
        "max": max_stat(X),
        f"scan w={r}": scan(X, r),
        "Page k=0.5": page_cusum(X, 0.5),
        "autocorr 1": lag1(X),
        "suites (peu)": runs_neg(X),
    }

Y0 = np.random.default_rng(s_cal).standard_normal((rep_cal, n0))
null = all_stats(Y0)
thr = {k: (np.log(1 / alpha) if k.startswith("e ") else calib(v, alpha)) for k, v in null.items()}

Y = np.random.default_rng(s_att).standard_normal((rep_att, n0))

def move_top_end(Y, r, sort_cluster=False, to_front=False):
    out = np.empty_like(Y)
    order = np.argsort(Y, axis=1)
    top = np.zeros_like(Y, dtype=bool)
    np.put_along_axis(top, order[:, -r:], True, axis=1)
    for i in range(Y.shape[0]):
        hi, lo = Y[i][top[i]], Y[i][~top[i]]   # ordre relatif d'origine conserve
        if sort_cluster:
            hi = np.sort(hi)
        out[i] = np.concatenate([hi, lo]) if to_front else np.concatenate([lo, hi])
    return out

arrs = {
    "honnete": Y,
    "tri_croissant": np.sort(Y, axis=1),
    "haut_fin": move_top_end(Y, r),
    "haut_fin_trie": move_top_end(Y, r, sort_cluster=True),
    "haut_debut": move_top_end(Y, r, to_front=True),
}
# verification du couplage trajectoriel : S^attaque_n <= S^honnete_n pour tout n
for name in ["tri_croissant", "haut_fin", "haut_fin_trie"]:
    d = np.cumsum(arrs[name], axis=1) - np.cumsum(Y, axis=1)
    print(f"couplage {name:14s}: max_n (S_att - S_hon) = {d.max():.2e}  (<= 0 attendu) ; ecart terminal max = {np.abs(d[:, -1]).max():.1e}")

print(f"\nTaux d'alarme (n0={n0}, r={r}, alpha={alpha}; calibrage {rep_cal} rep., attaque {rep_att} rep., erreur MC ~0.002-0.004)")
names = list(null.keys())
print(f"{'':15s}" + "".join(f"{k:>14s}" for k in names))
print(f"{'P0 (calib.)':15s}" + "".join(f"{(null[k] >= thr[k]).mean():14.4f}" for k in names))
for an, X in arrs.items():
    st = all_stats(X)
    print(f"{an:15s}" + "".join(f"{(st[k] >= thr[k]).mean():14.4f}" for k in names))
