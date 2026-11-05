"""Nuls supplémentaires du contre-lecteur pour la règle de l'incrément (G > 0, borne inf. 95 % > 0, p_perm <= 0,05).
Rangs moyens aux égalités (comme le texte), rééchantillonnage des cas avec rangs recalculés, permutation des cas.
Graines : SeedSequence(20261104 + 900), un enfant par scénario."""
import math
import sys

import numpy as np
from scipy.stats import rankdata, norm


def structure(n_v=24, n_hh=12, n_ss=12):
    y = []
    for _ in range(n_v):
        y += [0, 1]
    for _ in range(n_hh):
        y += [0, 0]
    for _ in range(n_ss):
        y += [1, 1]
    return np.array(y)


def auc_r(r, y):
    n1 = y.sum(-1)
    n0 = y.shape[-1] - n1
    return ((r * y).sum(-1) - n1 * (n1 + 1) / 2) / (n1 * n0)


def G_de(D, L, y):
    rD = rankdata(D, axis=-1)
    rL = rankdata(L, axis=-1)
    return auc_r(rankdata((rD + rL) / 2, axis=-1), y) - auc_r(rD, y)


def decide(D, L, y, rng, nb=1000, npm=1000):
    nc = y.size // 2
    G = G_de(D, L, y)
    idx = rng.integers(nc, size=(nb, nc))
    Db = D.reshape(nc, 2)[idx].reshape(nb, -1)
    Lb = L.reshape(nc, 2)[idx].reshape(nb, -1)
    yb = y.reshape(nc, 2)[idx].reshape(nb, -1)
    ok_classes = (yb.sum(1) > 0) & (yb.sum(1) < yb.shape[1])
    Gb = G_de(Db[ok_classes], Lb[ok_classes], yb[ok_classes])
    lb = np.quantile(Gb, 0.025)
    perms = np.argsort(rng.random((npm, nc)), axis=1)
    Lp = L.reshape(nc, 2)[perms].reshape(npm, -1)
    Gp = G_de(np.broadcast_to(D, Lp.shape), Lp, np.broadcast_to(y, Lp.shape))
    pv = (1 + (Gp >= G).sum()) / (1 + npm)
    return (G > 0) and (lb > 0) and (pv <= 0.05), (G > 0) and (pv <= 0.05), (G > 0) and (lb > 0), G


def mu_de(a):
    return math.sqrt(2) * norm.ppf(a)


def lecteur(kind, D, zD, y, rng, x):
    n = D.size
    if kind == "copie-discrete":          # copie bruitée de D, puis ramenée à 5 niveaux (probabilités à égalités)
        L = D + x * rng.normal(0, 1, n)
        q = np.quantile(L, [0.2, 0.4, 0.6, 0.8])
        return np.digitize(L, q).astype(float)
    if kind == "copie-3niv":
        L = D + x * rng.normal(0, 1, n)
        q = np.quantile(L, [1 / 3, 2 / 3])
        return np.digitize(L, q).astype(float)
    if kind == "constant-echecs":         # lecteur sans information, 0,5 partout, sauf 10 % d'échecs (pire valeur)
        L = np.full(n, 0.5)
        nc = n // 2
        for c in rng.choice(nc, size=max(1, nc // 10), replace=False):
            a, b = 2 * c, 2 * c + 1
            if y[a] != y[b]:
                s = a if y[a] == 1 else b
                h = b if s == a else a
                L[s], L[h] = 0.0, 1.0
            else:
                L[a], L[b] = 1.0, 0.0
        return L
    if kind == "relatif":                 # lecteur qui compare A et B sur D seulement (fonction de D dans la paire)
        Dp = D.reshape(-1, 2)
        d = (Dp[:, 0] - Dp[:, 1]) / x
        pA = 1 / (1 + np.exp(-d))
        return np.stack([pA, 1 - pA], 1).reshape(-1)
    if kind == "relatif+abs":             # relatif dans la paire plus niveau de la paire, bruité
        Dp = D.reshape(-1, 2)
        lvl = Dp.mean(1, keepdims=True) + 0.5 * rng.normal(0, 1, (Dp.shape[0], 1))
        d = Dp - Dp.mean(1, keepdims=True)
        return (lvl + d / x).reshape(-1)
    if kind == "heterosced":              # copie de D avec bruit plus fort au centre (fonction non monotone du bruit)
        return D + x * rng.normal(0, 1, n) * (1 + 2 * np.exp(-D ** 2))
    if kind == "nul-indep":
        return rng.normal(0, 1, n)
    raise ValueError(kind)


SCEN = {
    "a": [("copie-discrete", 0.90, 0.25), ("copie-discrete", 0.75, 0.25), ("copie-3niv", 0.90, 0.25),
          ("constant-echecs", 0.90, None), ("relatif", 0.90, 0.3), ("relatif", 0.75, 0.3)],
    "b": [("relatif+abs", 0.90, 0.5), ("heterosced", 0.90, 0.3), ("copie-discrete", 0.98, 0.25),
          ("nul-indep", 0.98, None), ("copie-discrete", 0.99, 0.1)],
    "c": [("copie-discrete", 0.90, 0.25, (12, 6, 6)), ("copie-discrete", 0.75, 0.25, (12, 6, 6)),
          ("relatif", 0.90, 0.3, (12, 6, 6)), ("copie-discrete", 0.90, 0.25, (6, 3, 3))],
}


def main():
    part = sys.argv[1]
    enf = iter(np.random.SeedSequence(20261104 + 900 + ord(part)).spawn(50))
    nsim = int(sys.argv[2]) if len(sys.argv) > 2 else 200
    for sc in SCEN[part]:
        kind, aD, x = sc[:3]
        struct = sc[3] if len(sc) > 3 else (24, 12, 12)
        y = structure(*struct)
        rng = np.random.default_rng(next(enf))
        conj = perm = boot = 0
        gs = []
        for _ in range(nsim):
            zD = rng.normal(0, 1, y.size)
            D = zD + mu_de(aD) * y
            L = lecteur(kind, D, zD, y, rng, x)
            c, p, b, g = decide(D, L, y, rng)
            conj += c; perm += p; boot += b; gs.append(g)
        print(f"{kind:16s} aire D {aD:.2f} x {x} cas {struct}: conjonction {conj/nsim:.3f}  permutation seule {perm/nsim:.3f}"
              f"  rééch. seul {boot/nsim:.3f}  gain moyen {np.mean(gs):+.4f}", flush=True)


if __name__ == "__main__":
    main()
