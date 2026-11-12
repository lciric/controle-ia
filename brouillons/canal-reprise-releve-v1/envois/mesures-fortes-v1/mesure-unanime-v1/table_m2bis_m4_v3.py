"""Table gelée de M2 bis et M4 (préenregistrement v3) : différence de la règle de Ville (τ = 2 moins τ = 0) et taux du bras
M4 (dépendance seule, variance constante) selon la corrélation intra-épisode naturelle r₀, avec le code v3 lui-même.
Mondes synthétiques : scores gaussiens, effet épisode de variance r₀/(1 − r₀) (corrélation intraclasse r₀), longueurs
valides de 5 à 10, 60 épisodes, 12 sondes, 20 tirages d'effet, 10 répétitions de monde. Graines par SeedSequence."""
import json, sys, math
import numpy as np
sys.dont_write_bytecode = True
sys.path.insert(0, ".")
import analyse_fausses_alertes_v3 as a

def monde(rng, r0, E=60, T=10, n=12):
    var_u = r0 / (1 - r0) if r0 < 1 else 1e6
    u = rng.normal(0, math.sqrt(var_u), size=(E, 1, n))
    X = u + rng.normal(0, 1, size=(E, T, n))
    masque = np.ones((E, T), bool)
    for e in range(E):
        masque[e, rng.integers(a.MIN_ACTIONS, T + 1):] = False
    X[~masque] = np.nan
    return X, masque

out = {"manifeste": {"script": "table_m2bis_m4_v3.py", "entropie": 2026102802, "repetitions": 10, "sondes": 12, "tirages": 20}, "table": {}}
for r0 in (0.0, 0.2, 0.5, 0.8):
    ville0, ville2, m4_sommes, m4_max, r0_est = [], [], [], [], []
    for rep in range(10):
        rng = np.random.default_rng(np.random.SeedSequence(2026102802, spawn_key=(int(r0 * 10), rep)))
        X, masque = monde(rng, r0)
        E = X.shape[0]; perm = rng.permutation(E); plis = a.plis_de_perm(perm)
        effets = [rng.normal(size=E) for _ in range(20)]
        for si in range(X.shape[2]):
            Xs = X[:, :, si]
            r0_est.append(a.correlation_intra_episode(Xs, masque))
            al0, _ = a.un_passage(Xs, masque, plis, perm, effets[0], 0.0)
            ville0.append(al0[("ville", "processus_e")].mean())
            v2, s4, x4 = [], [], []
            for d in range(20):
                al2, _ = a.un_passage(Xs, masque, plis, perm, effets[d], 2.0)
                v2.append(al2[("ville", "processus_e")].mean())
                al4, _ = a.un_passage(Xs, masque, plis, perm, effets[d], 2.0, calibrage_sans_effet=True, variance_constante=True)
                s4.append(np.mean([al4[("conforme", s)].mean() for s in ("somme_terminale", "somme_sequentielle", "page", "processus_e", "balayage")]))
                x4.append(al4[("conforme", "max")].mean())
            ville2.append(np.mean(v2)); m4_sommes.append(np.mean(s4)); m4_max.append(np.mean(x4))
    out["table"][f"r0={r0}"] = {"r0_estime_median": float(np.median(r0_est)),
                                "ville_tau0_median": float(np.median(ville0)), "ville_tau2_median": float(np.median(ville2)),
                                "difference_mediane": float(np.median(ville2) - np.median(ville0)),
                                "M4_sommes_median": float(np.median(m4_sommes)), "M4_max_median": float(np.median(m4_max)),
                                "M4_sommes_q1_q3": [float(np.quantile(m4_sommes, .25)), float(np.quantile(m4_sommes, .75))]}
json.dump(out, sys.stdout, ensure_ascii=False, indent=1); print()
