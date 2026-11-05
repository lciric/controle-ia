"""Puissance de M5 et de l'incrément sur la base « distance au départ » (addendum n° 1 de SPARKS-EXP7-NUL).

Script du rédacteur de l'addendum (calcul ; aucune donnée de l'expérience). numpy seul.
Graines : numpy.random.SeedSequence(20261104), enfants par scénario (R9).

M5 : aire sous la courbe au niveau de la paire, 12 paires ss contre 12 paires hh, score de paire = moyenne des deux
probabilités ; intervalle à 95 % par rééchantillonnage des paires dans chaque type (quantile 0,025, comme
`analyse.mesures_principales`) ; « discrimination absolue » si la borne inférieure > 0,5.
Modèle de simulation : latent par modèle ~ N(mu * y, 1) (y = 1 sycophante), probabilité = Phi(latent - mu / 2) ;
aire par modèle vraie = Phi(mu / sqrt(2)).

Incrément : 96 modèles (24 paires vraies, 12 hh, 12 ss) ; score de base D ~ N(muD * y, 1) ; lecteur
L = rho * zD + sqrt(1 - rho^2) * e + muL * y (zD = bruit de D) ; règle figée : moyenne des rangs de L et de D sur les 96 ;
G = AUC(combiné) - AUC(D) ; nul : réponses du lecteur permutées entre les 48 cas (paire entière, A vers A) ;
« incrément tenu » si G > 0 et p_perm <= 0,05.
"""
import math
import sys

import numpy as np


def phi(x):
    return 0.5 * (1 + np.vectorize(math.erf)(np.asarray(x) / math.sqrt(2)))


def auc(pos, neg):
    pos = np.asarray(pos)[:, None]
    neg = np.asarray(neg)[None, :]
    return ((pos > neg).sum() + 0.5 * (pos == neg).sum()) / (pos.size * neg.size)


def auc_rangs(scores, y):
    """AUC par les rangs (Mann-Whitney, égalités au rang moyen), vectorisée sur la dernière dimension."""
    s = np.asarray(scores, float)
    order = s.argsort(-1)
    r = np.empty_like(s)
    np.put_along_axis(r, order, np.arange(1, s.shape[-1] + 1, dtype=float), -1)
    # égalités : absentes en continu ; ignorées ici
    n1 = y.sum()
    n0 = y.size - n1
    return ((r * y).sum(-1) - n1 * (n1 + 1) / 2) / (n1 * n0)


def rangs(s):
    return s.argsort(-1).argsort(-1).astype(float) + 1.0


def puissance_m5(mu, n_sim, n_boot, rng):
    ok = 0
    for _ in range(n_sim):
        lat_ss = rng.normal(mu, 1, (12, 2))
        lat_hh = rng.normal(0, 1, (12, 2))
        p_ss = phi(lat_ss - mu / 2).mean(1)
        p_hh = phi(lat_hh - mu / 2).mean(1)
        i = rng.integers(12, size=(n_boot, 12))
        j = rng.integers(12, size=(n_boot, 12))
        a = p_ss[i][:, :, None]
        b = p_hh[j][:, None, :]
        bs = ((a > b).sum((1, 2)) + 0.5 * (a == b).sum((1, 2))) / 144.0
        ok += np.quantile(bs, 0.025) > 0.5
    return ok / n_sim


def structure():
    # 24 vraies (h, s), 12 hh, 12 ss ; y par modèle ; cas de chaque modèle
    y, cas = [], []
    for c in range(24):
        y += [0, 1]; cas += [c, c]
    for c in range(24, 36):
        y += [0, 0]; cas += [c, c]
    for c in range(36, 48):
        y += [1, 1]; cas += [c, c]
    return np.array(y), np.array(cas)


def puissance_increment(muD, muL, rho, n_sim, n_perm, rng):
    y, cas = structure()
    ok = 0
    gains = []
    for _ in range(n_sim):
        zD = rng.normal(0, 1, 96)
        D = zD + muD * y
        L = rho * zD + math.sqrt(1 - rho ** 2) * rng.normal(0, 1, 96) + muL * y
        rD, rL = rangs(D), rangs(L)
        aD = auc_rangs(D, y)
        G = auc_rangs((rD + rL) / 2, y) - aD
        gains.append(G)
        # permutation des cas : la paire (A, B) du lecteur du cas c va au cas pi(c)
        Lp = L.reshape(48, 2)
        perms = np.argsort(rng.random((n_perm, 48)), axis=1)
        Lperm = Lp[perms].reshape(n_perm, 96)
        rLp = rangs(Lperm)
        Gp = auc_rangs((rD[None, :] + rLp) / 2, y) - aD
        p = (1 + (Gp >= G).sum()) / (1 + n_perm)
        ok += (G > 0) and (p <= 0.05)
    return ok / n_sim, float(np.mean(gains))


def mu_de(a):
    """mu tel que Phi(mu / sqrt 2) = a (aire par modèle vraie)."""
    lo, hi = 0.0, 10.0
    for _ in range(80):
        m = (lo + hi) / 2
        if float(phi(m / math.sqrt(2))) < a:
            lo = m
        else:
            hi = m
    return (lo + hi) / 2


def main():
    partie = sys.argv[1] if len(sys.argv) > 1 else "m5"
    if partie == "m5":
        enfants = iter(np.random.SeedSequence(20261104).spawn(100))
        print("M5 : puissance (borne inférieure à 95 % > 0,5), 12 ss contre 12 hh ; 1000 simulations, 2000 tirages")
        for auc_modele in (0.5, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9):
            mu = mu_de(auc_modele)
            rng = np.random.default_rng(next(enfants))
            a = phi(rng.normal(mu, 1, (20000, 2)) - mu / 2).mean(1)
            b = phi(rng.normal(0, 1, (2000, 2)) - mu / 2).mean(1)
            auc_paire = float((a[:, None] > b[None, :]).mean())
            pw = puissance_m5(mu, 1000, 2000, np.random.default_rng(next(enfants)))
            print(f"  aire par modèle {auc_modele:.2f} (aire de paire ≈ {auc_paire:.3f}) : puissance {pw:.3f}", flush=True)
        return
    if partie == "copie":
        # nul « le lecteur ne lit que D » : L = D + sigma * e (aucune information au-delà de D)
        enfants = iter(np.random.SeedSequence(20261107).spawn(100))
        y, _ = structure()
        print("Nul « lecteur = D + bruit » : taux d'« incrément tenu » ; 300 simulations, 1000 permutations")
        for aD in (0.6, 0.75, 0.9):
            for sigma in (0.25, 0.5, 1.0):
                rng = np.random.default_rng(next(enfants))
                ok = 0
                for _ in range(300):
                    D = rng.normal(0, 1, 96) + mu_de(aD) * y
                    L = D + sigma * rng.normal(0, 1, 96)
                    rD, rL = rangs(D), rangs(L)
                    a0 = auc_rangs(D, y)
                    G = auc_rangs((rD + rL) / 2, y) - a0
                    perms = np.argsort(rng.random((1000, 48)), axis=1)
                    Lperm = L.reshape(48, 2)[perms].reshape(1000, 96)
                    Gp = auc_rangs((rD[None, :] + rangs(Lperm)) / 2, y) - a0
                    pv = (1 + (Gp >= G).sum()) / 1001
                    ok += (G > 0) and (pv <= 0.05)
                print(f"  aire D {aD:.2f}, bruit {sigma:.2f} : taux {ok / 300:.3f}", flush=True)
        return
    if partie.startswith("boot"):
        # règle retenue : borne inférieure à 95 % de G par rééchantillonnage des 48 cas (rangs recalculés) > 0,
        # et G > 0 ; deux nuls (lecteur sans information ; lecteur = D + bruit) et des alternatives
        conj = partie.endswith("c")
        enfants = iter(np.random.SeedSequence({"boot1": 20261108, "boot2": 20261109, "boot3": 20261110,
                                               "boot1c": 20261111, "boot2c": 20261112, "boot3c": 20261113}[partie]).spawn(100))
        y, _ = structure()
        yy = y.reshape(48, 2)
        def decide(D, L, rng, nb=1000):
            G = auc_rangs((rangs(D) + rangs(L)) / 2, y) - auc_rangs(D, y)
            idx = rng.integers(48, size=(nb, 48))
            Db = D.reshape(48, 2)[idx].reshape(nb, 96)
            Lb = L.reshape(48, 2)[idx].reshape(nb, 96)
            yb = yy[idx].reshape(nb, 96)
            n1 = yb.sum(1)
            n0 = 96 - n1
            def aucb(sc):
                r = rangs(sc)
                return ((r * yb).sum(1) - n1 * (n1 + 1) / 2) / (n1 * n0)
            Gb = aucb((rangs(Db) + rangs(Lb)) / 2) - aucb(Db)
            boot = (G > 0) and (np.quantile(Gb, 0.025) > 0)
            if not conj:
                return boot, G
            perms = np.argsort(rng.random((1000, 48)), axis=1)
            Lp = L.reshape(48, 2)[perms].reshape(1000, 96)
            Gp = auc_rangs((rangs(D)[None, :] + rangs(Lp)) / 2, y) - auc_rangs(D, y)
            pv = (1 + (Gp >= G).sum()) / 1001
            return boot and pv <= 0.05, G
        scen = {"boot1": [("nul-indep", 0.75, 0.5, 0.0), ("nul-indep", 0.9, 0.5, 0.0),
                          ("copie", 0.75, 0.25, None), ("copie", 0.9, 0.25, None), ("copie", 0.9, 0.5, None)],
                "boot2": [("alt", 0.6, 0.75, 0.0), ("alt", 0.75, 0.75, 0.0), ("alt", 0.75, 0.85, 0.0),
                          ("alt", 0.75, 0.85, 0.5), ("alt", 0.9, 0.85, 0.0)],
                "boot3": [("alt", 0.9, 0.95, 0.0), ("alt", 0.9, 0.95, 0.5), ("alt", 0.95, 0.95, 0.0),
                          ("alt", 0.6, 0.85, 0.0), ("copie", 0.6, 0.25, None)]}[partie.rstrip("c")]
        print(f"Règle par rééchantillonnage des cas (G > 0 et borne inférieure à 95 % > 0)"
              f"{' et p_perm ≤ 0,05 (conjonction)' if conj else ''} ; 200 simulations, 1000 tirages ; {partie}")
        for kind, aD, x, rho in scen:
            rng = np.random.default_rng(next(enfants))
            ok, gs = 0, []
            for _ in range(200):
                zD = rng.normal(0, 1, 96)
                D = zD + mu_de(aD) * y
                if kind == "copie":
                    L = D + x * rng.normal(0, 1, 96)
                else:
                    L = rho * zD + math.sqrt(1 - rho ** 2) * rng.normal(0, 1, 96) + mu_de(x) * y
                d, g = decide(D, L, rng)
                ok += d
                gs.append(g)
            lib = f"lecteur = D + bruit {x:.2f}" if kind == "copie" else f"aire lecteur {x:.2f}, corrélation du bruit {rho:.1f}"
            print(f"  {kind} : aire D {aD:.2f}, {lib} : taux {ok / 200:.3f}, gain moyen {np.mean(gs):+.3f}", flush=True)
        return
    graine = {"inc1": 20261105, "inc2": 20261106}[partie]
    aDs = {"inc1": (0.6, 0.75), "inc2": (0.9, 0.95)}[partie]
    enfants = iter(np.random.SeedSequence(graine).spawn(100))
    print(f"Incrément sur la base D (G > 0 et p_perm ≤ 0,05) ; 300 simulations, 1000 permutations ; partie {partie}")
    for aD in aDs:
        for aL in (0.5, 0.75, 0.85, 0.95):
            for rho in (0.0, 0.5):
                pw, g = puissance_increment(mu_de(aD), mu_de(aL), rho, 300, 1000, np.random.default_rng(next(enfants)))
                print(f"  aire D {aD:.2f}, aire lecteur {aL:.2f}, corrélation du bruit {rho:.1f} : "
                      f"puissance {pw:.3f}, gain moyen {g:+.3f}", flush=True)


if __name__ == "__main__":
    main()
