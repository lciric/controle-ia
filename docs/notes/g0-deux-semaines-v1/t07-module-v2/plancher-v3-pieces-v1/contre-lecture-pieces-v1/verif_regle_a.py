import sys, numpy as np
from controle_ia.t07 import plancher_v2 as p2, plancher_v1 as p1
from controle_ia.sondes.evaluation import aire_sous_courbe
import controle_ia.t07.plancher_v2 as m; print("import", m.__file__)
rng = np.random.default_rng(20261111)
pire = 0
for essai in range(12):
    nb = int(rng.integers(6, 30)); tailles = rng.integers(1, 9, size=nb)
    blocs = np.repeat(np.array([f"t{k:02d}" for k in rng.permutation(nb)]), tailles)
    n = blocs.size
    y = rng.integers(0, 2, size=n)
    if essai % 3 == 0:                       # quelques tâches à une seule classe
        for b in np.unique(blocs)[:2]:
            y[blocs == b] = 1
    K = int(rng.integers(3, 40))
    arrondi = [None, 1, 0][essai % 3]
    s = rng.standard_normal(n) + 0.8 * y
    P = rng.standard_normal((K, n)) + rng.uniform(0, 0.8, size=(K, 1)) * y
    if arrondi is not None:
        s, P = np.round(s, arrondi), np.round(P, arrondi)         # ex aequo nombreux
    ordre = rng.permutation(n); s, P, y, blocs = s[ordre], P[:, ordre], y[ordre], blocs[ordre]
    T, graine, q, niv = 300, int(rng.integers(1, 2**31)), 0.95, 0.9875
    try:
        r = p2.comparer_difference_au_plancher(s, P, y, blocs, T, graine, q, niv)
    except Exception as e:
        r = e
    # force brute : mêmes tirages qu'intervalle_blocs
    uniques = np.unique(blocs); membres = [np.flatnonzero(blocs == u) for u in uniques]
    g = np.random.default_rng(graine); D, deg = [], 0
    for _ in range(T):
        choix = g.integers(0, uniques.size, size=uniques.size)
        i = np.concatenate([membres[c] for c in choix])
        if len(set(y[i].tolist())) < 2:
            deg += 1; continue
        a = aire_sous_courbe(s[i], y[i]); ap = np.array([aire_sous_courbe(P[k][i], y[i]) for k in range(K)])
        D.append(a - np.quantile(ap, q))
    if deg > 0.01 * T:
        print(essai, "dégénérés", deg, "→ attendu arrêt ; rendu :", type(r).__name__, str(r)[:60]); continue
    a = (1 - niv) / 2
    bas, haut = float(np.quantile(D, a)), float(np.quantile(D, 1 - a))
    ok = (r["difference"]["bas"] == bas and r["difference"]["haut"] == haut and r["degeneres"] == deg
          and r["au_dessus_du_plancher"] == (bas > 0) and r["aire"] == aire_sous_courbe(s, y))
    v1 = p1.comparer_scores_au_plancher(s, P, y, blocs, T, graine, q, niv)
    ok = ok and all(r[k] == v1[k] for k in ("aire", "bas", "haut", "plancher_quantile", "plancher_mediane", "n_plancher", "degeneres", "tirages"))
    print(essai, "nb", nb, "n", n, "K", K, "arrondi", arrondi, "dég", deg, "bit près", ok, "bas", bas, "au-dessus", r["au_dessus_du_plancher"])
    pire += (not ok)
print("ÉCARTS :", pire)
