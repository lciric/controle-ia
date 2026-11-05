import numpy as np
exec(open("v5_T3_adaptatif.py").read().split("X_ac, gap_ac")[0])
# recalcul direct du nombre de changements de signe
def nchg(X):
    med = np.median(X, axis=1, keepdims=True); s = X > med
    return (s[:, 1:] != s[:, :-1]).sum(axis=1)
X_ru, gap_ru = match(X0, "runs", iters=6000)
print("gap suivi:", gap_ru)
print("changements: aleatoire moy", nchg(X0).mean(), " apparie moy", nchg(X_ru).mean())
Pn = np.random.default_rng(0).standard_normal((rep, n))
print("sous P0 moy", nchg(Pn).mean(), " quantile 5%", np.quantile(nchg(Pn), 0.05))
# la mediane du multi-ensemble est-elle a l'interieur de la suite haute ? non (r=5 << n/2). Mais la ligne Z est centree :
print("seuil runs_neg:", thr["suites (peu)"])
