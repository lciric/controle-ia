"""Contre-lecture v3 : recalcul des bornes de la règle primaire v3 en fractions exactes (bibliothèque standard + numpy)."""
from fractions import Fraction as F
from math import comb, ceil
import numpy as np

a = F(5, 100) / 32
print("alpha par test = 0,05/32 =", a, "=", float(a))
for n in (13, 14, 15):
    print(f"  n_iso = {n} : (1 + n)/10001 = {F(1 + n, 10001)} = {float(F(1 + n, 10001)):.7f} ≤ alpha ? {F(1 + n, 10001) <= a}")
print("plus grand n_iso :", max(n for n in range(100) if F(1 + n, 10001) <= a))
print("borne familiale 32 × 15/10001 =", F(32 * 15, 10001), "=", float(F(32 * 15, 10001)))
print("par lentille 16 × 15/10001 =", float(F(16 * 15, 10001)))
print("200 isotropes : plus petit p = 1/201 =", float(F(1, 201)), "> alpha ?", F(1, 201) > a)
k = ceil(F(99, 100) * 200)
print("quantile 0,99 inverted_cdf de 200 valeurs : statistique d'ordre", k, "(numpy :",
      int(np.quantile(np.arange(1, 201), 0.99, method="inverted_cdf")), ") ; n_pl max =", 200 - k,
      "; niveau de rang 3/201 =", F(3, 201), "=", round(float(F(3, 201)), 5))
# équivalence S > x_(198) ⇔ #{x ≥ S} ≤ 2, vérifiée sur des tirages entiers avec ex aequo
r = np.random.default_rng(np.random.SeedSequence(20261029))
bon = True
for _ in range(20000):
    x = r.integers(0, 6, 200); S = int(r.integers(0, 8))
    q = np.quantile(x.astype(float), 0.99, method="inverted_cdf")
    bon &= (S > q) == (int((x >= S).sum()) <= 2)
print("équivalence S > quantile ⇔ n_pl ≤ 2 (20 000 cas entiers avec ex aequo) :", bon)
def p(b, c):
    n = b + c
    return F(1) if n == 0 else min(F(1), F(2 * sum(comb(n, i) for i in range(min(b, c) + 1)), 2 ** n))
mins = []
for n in range(1, 17):
    ok = [(b, n - b) for b in range(n + 1) if b >= n - b and p(b, n - b) <= F(5, 100)]
    if ok:
        mins.append(f"{min(ok)[0]}-{min(ok)[1]}")
print("minima du test du signe (b + c de 6 à 16) :", ", ".join(mins))
