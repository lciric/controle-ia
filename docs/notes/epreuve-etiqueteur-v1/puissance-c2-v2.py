# Calculs de puissance pour l'épreuve de l'étiqueteur v2 (exploratoire). Bibliothèque standard seulement.
# Rédacteur neuf, 8 novembre 2026. Exécuté avec `python -I`.
from math import lgamma, log, exp


def lcomb(n, k):
    return lgamma(n + 1) - lgamma(k + 1) - lgamma(n - k + 1)


def pmf(k, n, p):
    if p <= 0.0:
        return 1.0 if k == 0 else 0.0
    if p >= 1.0:
        return 1.0 if k == n else 0.0
    return exp(lcomb(n, k) + k * log(p) + (n - k) * log(1 - p))


def cdf(k, n, p):
    return sum(pmf(i, n, p) for i in range(0, k + 1))


def sf(k, n, p):  # P(X >= k)
    return 1.0 - cdf(k - 1, n, p) if k > 0 else 1.0


def bissection(f, lo, hi, it=60):
    for _ in range(it):
        m = (lo + hi) / 2
        if f(m) > 0:
            hi = m
        else:
            lo = m
    return (lo + hi) / 2


def clopper_pearson(k, n, a=0.05):
    lo = 0.0 if k == 0 else bissection(lambda p: sf(k, n, p) - a / 2, 0.0, 1.0)
    hi = 1.0 if k == n else bissection(lambda p: a / 2 - cdf(k, n, p), 0.0, 1.0)
    return lo, hi


print("== 1. Règle v1 de C2 sur 120 placebos : réussi k<=5 ; échec décisif k>=12 ; zone morte 6..11 ==")
for p in (0.02, 0.03, 0.05, 0.07, 0.09, 0.10, 0.12, 0.15):
    r = cdf(5, 120, p); e = sf(12, 120, p)
    print(f"p vrai {p:.2f} : P(réussi) {r:.3f}  P(échec décisif) {e:.3f}  P(non tranché) {1-r-e:.3f}")

print("\n== 2. Demi-largeur de l'intervalle exact à 95 % au taux observé p, selon n ==")
for p in (0.05, 0.10):
    for n in (120, 240, 300, 360, 480, 560, 600):
        k = round(p * n); lo, hi = clopper_pearson(k, n)
        print(f"p={p:.2f} n={n:4d} k={k:3d} : [{lo:.3f} ; {hi:.3f}] demi-largeur {(hi-lo)/2:.3f}"
              )

print("\n== 2 bis. Plus petit n tel que l'intervalle exact à 95 % autour de k=round(p n) ait une demi-largeur <= 0,025 ==")
for p in (0.05, 0.10):
    n = 60
    while True:
        k = round(p * n); lo, hi = clopper_pearson(k, n)
        if (hi - lo) / 2 <= 0.025:
            print(f"p={p:.2f} : n = {n} (k={k}, [{lo:.3f} ; {hi:.3f}])"); break
        n += 10

print("\n== 3. Règle à seuil unique, sans zone morte : « validé » si k <= k*, sinon « non validé » ==")
print("   Contrainte : P(validé | p=0,10) <= 0,05 et P(validé | p=0,05) >= 0,90 ; plus petit n, et son k*")
for n in range(120, 700, 10):
    ok = None
    for k in range(n + 1):
        if sf(k + 1, n, 0.10) >= 0.95 and cdf(k, n, 0.05) >= 0.90:
            ok = k; break
    if ok is not None:
        print(f"   n = {n}, k* = {ok} (seuil {ok/n:.3f}) : P(validé|0,05)={cdf(ok,n,0.05):.3f} P(validé|0,10)={cdf(ok,n,0.10):.3f} "
              f"P(validé|0,03)={cdf(ok,n,0.03):.3f} P(validé|0,07)={cdf(ok,n,0.07):.3f} P(validé|0,09)={cdf(ok,n,0.09):.3f}")
        break
print("   Même règle, hypothèses plus serrées : P(validé | p=0,08) <= 0,05 et P(validé | p=0,04) >= 0,90")
for n in range(120, 1500, 10):
    ok = None
    for k in range(n + 1):
        if sf(k + 1, n, 0.08) >= 0.95 and cdf(k, n, 0.04) >= 0.90:
            ok = k; break
    if ok is not None:
        print(f"   n = {n}, k* = {ok} (seuil {ok/n:.3f})"); break

print("\n== 4. Caractéristiques de la règle à seuil unique pour quelques n (seuil 0,07 arrondi en dessous) ==")
for n in (240, 300, 360):
    k = int(0.07 * n)
    print(f"   n={n} k*={k} : " + "  ".join(f"P(validé|{p:.2f})={cdf(k,n,p):.3f}" for p in (0.03, 0.05, 0.07, 0.09, 0.10, 0.12)))

print("\n== 5. Garde d'instabilité des relectures : au plus 5 % ; selon n relectures ==")
for n in (60, 120, 180):
    for s in (0.05,):
        kmax = max(k for k in range(n + 1) if clopper_pearson(k, n)[1] <= 0.10 and k / n <= s)
        print(f"   n={n} : garde « au plus {kmax} » (borne haute {clopper_pearson(kmax,n)[1]:.3f}) ; "
              + "  ".join(f"P(tenue|{p:.2f})={cdf(kmax,n,p):.3f}" for p in (0.01, 0.03, 0.05, 0.08, 0.10)))

print("\n== 6. Observé en phase 1 : intervalles exacts ==")
for nom, k, n in (("étiqueteur C2", 11, 120), ("Argon seul C2", 12, 120), ("Kimi seul C2", 27, 120),
                  ("étiqueteur relectures", 5, 60), ("Argon relectures", 4, 60), ("Kimi relectures", 13, 60)):
    lo, hi = clopper_pearson(k, n); print(f"   {nom}: {k}/{n} = {k/n:.3f} [{lo:.3f} ; {hi:.3f}]")

print("\n== 7. Comparer deux lecteurs/paires sur les mêmes placebos : différence détectable (approximation normale) ==")
from math import sqrt
for n in (240, 360):
    for (p1, p2) in ((0.05, 0.10), (0.05, 0.08), (0.09, 0.15)):
        se = sqrt((p1 * (1 - p1) + p2 * (1 - p2)) / n)
        print(f"   n={n} : {p1:.2f} contre {p2:.2f} : écart {p2-p1:.2f}, écart-type {se:.3f}, z={(p2-p1)/se:.2f} (appariement ignoré : prudent)")
