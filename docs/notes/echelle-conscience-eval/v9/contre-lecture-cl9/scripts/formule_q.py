"""Modèle linéaire sans bruit de l'annexe A de cl8 : contraste du jeu a = u + s_a, du jeu b = k·u + s_b ; u, s_a, s_b
orthogonaux. Vérifie q = k·pureté_a/pureté_b (pureté = cosinus de la direction apprise avec u) et calcule les deux
seuils de la bande 1,15 à |s_a| = |s_b| (même hétérogénéité des cadrages)."""
import numpy as np
rng = np.random.default_rng(1)
d = 256
B = np.linalg.qr(rng.normal(size=(d, 3)))[0].T
def q_et_puretes(k, na, nb, U=4.0):
    u, sa, sb = B[0] * U, B[1] * na, B[2] * nb
    ca, cb = (u + sa) / np.linalg.norm(u + sa), (k * u + sb) / np.linalg.norm(k * u + sb)
    ec_ab, ec_ba = ca @ (k * u + sb), cb @ (u + sa)
    pa, pb = ca @ (u / U), cb @ (u / U)
    return ec_ab / ec_ba, pa, pb
print("identité q = k·pa/pb (écart maximal sur 1 000 tirages au hasard) :",
      max(abs(q - k * pa / pb) for k, na, nb in rng.uniform([0.4, 0, 0], [2.0, 8, 8], size=(1000, 3))
          for q, pa, pb in [q_et_puretes(k, na, nb)]))
for r in (0.12, 0.85, 2.0, 3.1):
    haut = np.sqrt(1.3225 + 0.3225 * r)
    bas2 = 1 / 1.3225 - r * (1 - 1 / 1.3225)
    bas = np.sqrt(bas2) if bas2 > 0 else float("nan")
    print(f"r = {r} : la bande sonne (sans bruit) si k > {haut:.3f} ou si k < {bas:.3f} (soit 1/k > {1/bas if bas == bas else float('inf'):.2f})")
for k in (1.333, 0.75, 1.4, 0.6):
    n = np.sqrt(0.12) * 4
    q, pa, pb = q_et_puretes(k, n, n)
    print(f"|s_a| = |s_b| (r = 0,12), k = {k} : q = {q:.3f} ; puretés a {pa:.3f}, b {pb:.3f} (inégales dès que k ≠ 1)")
# miroir de cl9 : k = 0,6, composante de norme 3,2 dans le jeu b (en plus de |s| ≈ 1,39 des particularités)
na = np.sqrt(0.12) * 4; nb = np.sqrt(na**2 + 3.2**2)
print("miroir cl9 (k = 0,6 ; composante 3,2 dans b) : q = %.3f, puretés a %.3f, b %.3f" % q_et_puretes(0.6, na, nb))
