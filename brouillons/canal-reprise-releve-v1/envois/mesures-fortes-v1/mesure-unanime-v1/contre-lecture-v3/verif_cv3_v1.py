"""Contre-lecture v3 de la mesure unanime : vérifications indépendantes (processeur, synthétique seulement ; aucun accès
à scores-p3.npz). Importe le script v3 sans le modifier. Graines : SeedSequence(ENTROPIE_CV3, spawn_key=(partie, …)).
Parties :
  table R0     : refait la table gelée (Ville τ=0, τ=2, différence ; M4 sommes, max) à r0 donné, autre graine, 6 mondes
  m3           : M3 à τ = 0, une sonde par monde (pire cas « sondes parfaitement corrélées ») : part des mondes où une
                 cellule conforme dépasse 2L, ou tombe en zone fragile ; niveau réel à E = 59 contre L du manifeste
  marges       : Ville à τ = 0 sous indépendance (r0 = 0) avec des marges non gaussiennes (asymétrie, queues lourdes)
  m4E          : bras M4 à r0 = 0,2 avec E = 59 (K = 38, L = 1/39) contre E = 60
  transfo      : moments et corrélation intraclasse de Xe (bras M4) par Monte-Carlo
"""
import json, math, sys
sys.dont_write_bytecode = True
import numpy as np
sys.path.insert(0, "/home/claude/canal-conv-audit-n04/brouillons/canal-reprise-releve-v1/envois/mesures-fortes-v1/mesure-unanime-v1")
import analyse_fausses_alertes_v3 as a

ENTROPIE_CV3 = 3141592653
SOMMES = ("somme_terminale", "somme_sequentielle", "page", "processus_e", "balayage")


def monde(rng, r0, E=60, T=10, n=12, marge="gauss"):
    var_u = r0 / (1 - r0)
    u = rng.normal(0, math.sqrt(var_u), size=(E, 1, n))
    if marge == "gauss":
        b = rng.normal(0, 1, size=(E, T, n))
    elif marge == "lognormale":
        b = rng.lognormal(0, 0.8, size=(E, T, n)); b = (b - b.mean()) / b.std()
    elif marge == "student3":
        b = rng.standard_t(3, size=(E, T, n)) / math.sqrt(3.0)
    X = u + b
    masque = np.ones((E, T), bool)
    for e in range(E):
        masque[e, rng.integers(a.MIN_ACTIONS, T + 1):] = False
    X[~masque] = np.nan
    return X, masque


def partie_table(r0, reps=6, n=12, D=20):
    ville0, ville2, s4l, x4l, r0e = [], [], [], [], []
    for rep in range(reps):
        rng = np.random.default_rng(np.random.SeedSequence(ENTROPIE_CV3, spawn_key=(1, int(round(r0 * 10)), rep)))
        X, masque = monde(rng, r0, n=n)
        E = X.shape[0]; perm = rng.permutation(E); plis = a.plis_de_perm(perm)
        effets = [rng.normal(size=E) for _ in range(D)]
        for si in range(n):
            Xs = X[:, :, si]
            r0e.append(a.correlation_intra_episode(Xs, masque))
            al0, _ = a.un_passage(Xs, masque, plis, perm, effets[0], 0.0)
            ville0.append(al0[("ville", "processus_e")].mean())
            v2, s4, x4 = [], [], []
            for d in range(D):
                al2, _ = a.un_passage(Xs, masque, plis, perm, effets[d], 2.0)
                v2.append(al2[("ville", "processus_e")].mean())
                al4, _ = a.un_passage(Xs, masque, plis, perm, effets[d], 2.0, calibrage_sans_effet=True, variance_constante=True)
                s4.append(np.mean([al4[("conforme", s)].mean() for s in SOMMES]))
                x4.append(al4[("conforme", "max")].mean())
            ville2.append(np.mean(v2)); s4l.append(np.mean(s4)); x4l.append(np.mean(x4))
    return {"r0": r0, "mondes": reps, "sondes": n, "tirages": D, "r0_estime_median": float(np.median(r0e)),
            "ville_tau0_median": float(np.median(ville0)), "ville_tau2_median": float(np.median(ville2)),
            "difference_mediane": float(np.median(ville2) - np.median(ville0)),
            "M4_sommes_median": float(np.median(s4l)), "M4_max_median": float(np.median(x4l)),
            "M4_sommes_q1_q3": [float(np.quantile(s4l, .25)), float(np.quantile(s4l, .75))]}


def niveau_manifeste(E):
    K = E - math.ceil(E / a.PLIS) - a.PART_NORMALISATION
    return K, 1.0 - a.rang_conforme(K, a.ALPHA) / (K + 1)


def partie_m3(mondes=300):
    res = {"niveaux_manifeste_selon_E": {str(E): dict(zip(("K", "L"), niveau_manifeste(E))) for E in range(44, 61)}}
    for E, r0 in ((60, 0.0), (60, 0.3), (60, 0.8), (59, 0.2)):
        K, L = niveau_manifeste(E)
        taux = np.zeros((mondes, len(a.STATISTIQUES)))
        for w in range(mondes):
            rng = np.random.default_rng(np.random.SeedSequence(ENTROPIE_CV3, spawn_key=(2, E, int(round(r0 * 10)), w)))
            X, masque = monde(rng, r0, E=E, n=1)
            perm = rng.permutation(E); plis = a.plis_de_perm(perm)
            al, Kp = a.un_passage(X[:, :, 0], masque, plis, perm, np.zeros(E), 0.0)
            taux[w] = [al[("conforme", s)].mean() for s in a.STATISTIQUES]
        audit = (taux > 2 * L + 1e-12).any(axis=1)
        fragile = ((taux > 1.6 * L + 1e-12) | (taux < 0.4 * L - 1e-12)).any(axis=1)
        res[f"E={E},r0={r0}"] = {"K_manifeste": K, "L_manifeste": L, "K_par_pli": Kp,
                                 "niveau_reel_moyen_par_statistique": dict(zip(a.STATISTIQUES, taux.mean(0).round(4).tolist())),
                                 "part_mondes_une_cellule_tau0_au_dessus_de_2L": float(audit.mean()),
                                 "part_mondes_une_cellule_tau0_fragile": float(fragile.mean()),
                                 "part_par_cellule_au_dessus_de_2L": dict(zip(a.STATISTIQUES, (taux > 2 * L + 1e-12).mean(0).round(4).tolist()))}
    return res


def partie_marges(mondes=60, n=6):
    res = {}
    for marge in ("gauss", "lognormale", "student3"):
        v = []
        for w in range(mondes):
            rng = np.random.default_rng(np.random.SeedSequence(ENTROPIE_CV3, spawn_key=(3, ("gauss", "lognormale", "student3").index(marge), w)))
            X, masque = monde(rng, 0.0, n=n, marge=marge)
            E = X.shape[0]; perm = rng.permutation(E); plis = a.plis_de_perm(perm)
            for si in range(n):
                al, _ = a.un_passage(X[:, :, si], masque, plis, perm, np.zeros(E), 0.0)
                v.append(al[("ville", "processus_e")].mean())
        res[marge] = {"r0": 0.0, "ville_tau0_moyenne": float(np.mean(v)), "ville_tau0_mediane": float(np.median(v)),
                      "q1_q3": [float(np.quantile(v, .25)), float(np.quantile(v, .75))], "n": len(v)}
    return res


def partie_m4E(reps=6, n=12, D=20, r0=0.2):
    res = {}
    for E in (60, 59):
        s4l, x4l = [], []
        for rep in range(reps):
            rng = np.random.default_rng(np.random.SeedSequence(ENTROPIE_CV3, spawn_key=(4, E, rep)))
            X, masque = monde(rng, r0, E=E, n=n)
            perm = rng.permutation(E); plis = a.plis_de_perm(perm)
            effets = [rng.normal(size=E) for _ in range(D)]
            for si in range(n):
                s4, x4 = [], []
                for d in range(D):
                    al4, Kp = a.un_passage(X[:, :, si], masque, plis, perm, effets[d], 2.0, calibrage_sans_effet=True, variance_constante=True)
                    s4.append(np.mean([al4[("conforme", s)].mean() for s in SOMMES])); x4.append(al4[("conforme", "max")].mean())
                s4l.append(np.mean(s4)); x4l.append(np.mean(x4))
        K, L = niveau_manifeste(E)
        res[f"E={E}"] = {"K_manifeste": K, "L_manifeste": L, "K_par_pli": Kp, "M4_sommes_median": float(np.median(s4l)),
                         "M4_max_median": float(np.median(x4l))}
    return res


def partie_transfo(n_mc=4000, r0=0.3, tau=2.0):
    rng = np.random.default_rng(np.random.SeedSequence(ENTROPIE_CV3, spawn_key=(5,)))
    E, T = n_mc, 8
    X = rng.normal(0, math.sqrt(r0 / (1 - r0)), size=(E, 1)) + rng.normal(size=(E, T))
    masque = np.ones((E, T), bool)
    u = rng.normal(size=E)
    s, m = float(np.nanstd(X[masque])), float(np.nanmean(X[masque]))
    Xe = m + (X + tau * s * u[:, None] - m) / math.sqrt(1 + tau * tau)
    def icc(Y):
        return a.correlation_intra_episode(Y, masque)
    def asym(Y):
        z = (Y - Y.mean()) / Y.std(); return float((z ** 3).mean())
    Xl = np.exp(0.8 * rng.normal(size=(E, T))); Xl = (Xl - Xl.mean()) / Xl.std()
    sl, ml = float(Xl.std()), float(Xl.mean())
    Xle = ml + (Xl + tau * sl * u[:, None] - ml) / math.sqrt(1 + tau * tau)
    return {"r0": r0, "tau": tau, "moyenne_X": float(X.mean()), "moyenne_Xe": float(Xe.mean()), "variance_X": float(X.var()),
            "variance_Xe": float(Xe.var()), "icc_X": icc(X), "icc_Xe": icc(Xe), "icc_Xe_theorique": (r0 + tau * tau) / (1 + tau * tau),
            "lognormale_asymetrie_X": asym(Xl), "lognormale_asymetrie_Xe": asym(Xle)}


if __name__ == "__main__":
    p = sys.argv[1]
    out = {"script": "verif_cv3_v1.py", "entropie": ENTROPIE_CV3, "partie": sys.argv[1:], "numpy": np.__version__,
           "empreinte_script_v3_importe": __import__("hashlib").sha256(open(a.__file__, "rb").read()).hexdigest()}
    if p == "table":
        out["resultat"] = partie_table(float(sys.argv[2]))
    elif p == "m3":
        out["resultat"] = partie_m3()
    elif p == "marges":
        out["resultat"] = partie_marges()
    elif p == "m4E":
        out["resultat"] = partie_m4E()
    elif p == "transfo":
        out["resultat"] = partie_transfo()
    json.dump(out, sys.stdout, ensure_ascii=False, indent=1); print()
