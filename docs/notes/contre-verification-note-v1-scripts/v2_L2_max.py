"""V2 - L2 : seuil du max, borne de l'union, puissance exacte (gaussien, independance)."""
import numpy as np
from scipy import stats

alpha = 0.05
Phibar, Phibar_inv = stats.norm.sf, stats.norm.isf

def c_exact(n, alpha):
    # P0(M_n >= c) = 1 - (1 - Phibar(c))^n = alpha
    return Phibar_inv(-np.expm1(np.log1p(-alpha) / n))

print("Seuil du max : exact vs sqrt(2 log(n/alpha)), et taux de faux positifs reel avec l'approximation")
for n in [1, 20, 100, 200, 1000, 2000]:
    ce, ca = c_exact(n, alpha), np.sqrt(2 * np.log(n / alpha))
    fpr_approx = -np.expm1(n * np.log1p(-Phibar(ca)))
    print(f"  n={n:5d}  c_exact={ce:5.3f}  approx={ca:5.3f}  FPR(approx)={fpr_approx:.4f}")

def power_exact(n, m, b):   # b = B / sigma
    c = c_exact(n, alpha)
    return -np.expm1((n - m) * np.log1p(-Phibar(c)) + m * np.log1p(-Phibar(c - b / m)))

def union_bound(n, m, b):
    c = c_exact(n, alpha)
    return m * Phibar(c - b / m) + (n - m) * Phibar(c)

print("\nBorne de l'union a B = 0 (sous P0) : n*Phibar(c_n), limite -log(1-alpha) =", round(-np.log1p(-alpha), 5))
for n in [1, 2, 20, 200, 2000]:
    print(f"  n={n:5d}  union bound sous P0 = {union_bound(n, 1, 0.0):.5f}")

print("\nPuissance exacte du max vs borne de l'union, B choisi pour que le test terminal unilateral ait puissance 0,5")
for n in [20, 200, 2000]:
    b = stats.norm.isf(alpha) * np.sqrt(n)        # B/sigma tel que Phibar(z_a - B/(sigma sqrt n)) = 0.5
    row = []
    for m in [1, 2, 5, 10, 20, 50, 100, 1000]:
        if m > n: continue
        row.append(f"m={m}: {power_exact(n, m, b):.3f} (UB {min(union_bound(n, m, b), 9.999):.3f})")
    print(f"  n={n}, B/sigma={b:.1f} :: " + " | ".join(row))
    # excès asymptotique a m=n : alpha + (1-alpha) phi(c_n) B/sigma
    c = c_exact(n, alpha)
    print(f"     m=n exact = {power_exact(n, n, b):.4f} ; approx alpha+(1-alpha)phi(c)B/sigma = {alpha + (1-alpha)*stats.norm.pdf(c)*b:.4f}")

# monotonie en m (log-concavite de Phi) : verification numerique
ok = True
for n in [20, 200, 2000]:
    for b in [1, 5, 20, 60]:
        p = [power_exact(n, m, b) for m in range(1, n + 1)]
        ok &= np.all(np.diff(p) <= 1e-15)
print("\nPuissance du max decroissante en m (gaussien) sur la grille testee :", ok)

# Grille T0.3 : puissance du test terminal (L1) a B fixe en fonction de n0 = N*T
print("\nL1 / prediction 1 : puissance du test terminal unilateral Phibar(z_a - B/(sigma sqrt(NT))) a B/sigma = 20")
for N in [1, 2, 3, 5, 10]:
    print("  N=%2d : " % N + "  ".join(f"T={T}: {Phibar(stats.norm.isf(alpha) - 20/np.sqrt(N*T)):.3f}" for T in [20, 50, 100, 200]))
