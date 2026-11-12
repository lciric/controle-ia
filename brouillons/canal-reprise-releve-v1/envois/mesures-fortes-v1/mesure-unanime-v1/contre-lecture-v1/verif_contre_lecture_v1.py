"""Vérifications de la contre-lecture (R2) du préenregistrement « mesure unanime » v1 — données SYNTHÉTIQUES seulement.

Importe le script relu sans le modifier (chemin passé en argument) et en appelle les fonctions.
Graines : numpy.random.SeedSequence(ENTROPIE_VERIF), enfants par partie (consignés dans la sortie).

Parties :
 A. M1 analytique : moyenne de 1 − 0,99^T pour T uniforme sur {5..10} et pour T = 8, 10.
 B. Cohérence de log_e_unilateral du script avec la formule de processus_e (σ = 1) : écart maximal.
 C. Taux moyens (par_action, Ville, conforme) selon la corrélation intra-épisode naturelle r0 ∈ {0 ; 0,2 ; 0,5 ; 0,8},
    à τ = 0 et τ = 2, avec un_passage du script (sondes indépendantes, longueurs valides uniformes 5..10).
 D. Distribution du taux conforme d'une sonde à τ = 0 (un tirage) : P(taux = 0), P(> 0,075), P(> 0,10), moyenne.
 E. Partage normalisation / seuils : quels indices servent à la normalisation (ordre trié de setdiff1d).
 F. Effet épisode : le même générateur est-il réutilisé d'une sonde à l'autre (effets différents par sonde) ?
"""
import importlib.util
import json
import math
import sys
import time

import numpy as np

ENTROPIE_VERIF = 20261027231500


def charger(chemin):
    spec = importlib.util.spec_from_file_location("analyse_relue", chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def donnees(rng, E, n_sondes, r0, tmin=5, tmax=10):
    u = rng.normal(0, math.sqrt(r0), size=(E, 1, n_sondes))
    X = u + rng.normal(0, math.sqrt(1 - r0), size=(E, tmax, n_sondes))
    masque = np.ones((E, tmax), bool)
    for e in range(E):
        k = rng.integers(tmin, tmax + 1)
        masque[e, k:] = False
    X[~masque] = np.nan
    return X, masque


def main():
    m = charger(sys.argv[1])
    ss = np.random.SeedSequence(ENTROPIE_VERIF)
    enfants = ss.spawn(6)
    sortie = {"manifeste": {"entropie": ENTROPIE_VERIF, "enfants": [list(c.spawn_key) for c in enfants],
                            "numpy": np.__version__, "python": sys.version.split()[0], "script_relu": sys.argv[1]}}
    # A
    Ts = np.arange(5, 11)
    sortie["A_M1_analytique"] = {"moyenne_T_uniforme_5_10": float(np.mean(1 - 0.99 ** Ts)),
                                 "T8": 1 - 0.99 ** 8, "T10": 1 - 0.99 ** 10, "T5": 1 - 0.99 ** 5,
                                 "T50_synthese": 1 - 0.99 ** 50,
                                 "conforme_attendu_K34": 1 - m.rang_conforme(34, 0.05) / 35,
                                 "conforme_attendu_K39": 1 - m.rang_conforme(39, 0.05) / 40,
                                 "K_min_admis": min(K for K in range(1, 100) if m.rang_conforme(K, 0.05) <= K),
                                 "E_min_admis": min(E for E in range(30, 61)
                                                    if m.rang_conforme(E - math.ceil(E / 10) - 20, 0.05) <= E - math.ceil(E / 10) - 20)}
    # B
    S = np.linspace(-30, 30, 601)
    ecart = 0.0
    from math import erfc, sqrt, log
    for n in range(1, 11):
        ref = []
        for s in S:
            a = 1 + 0.25 * n
            x = 0.5 * s / sqrt(a)
            ref.append(log(2) - 0.5 * log(a) + 0.25 * s * s / (2 * a) + log(0.5 * erfc(-x / sqrt(2))))
        ecart = max(ecart, float(np.max(np.abs(m.log_e_unilateral(S, float(n), 0.5) - np.array(ref)))))
    sortie["B_log_e_ecart_max_sur_S_dans_[-30,30]"] = ecart
    # C
    rng_c = np.random.default_rng(enfants[0])
    rng_plis = np.random.default_rng(enfants[1])
    plis = m.plis_de(60, rng_plis)
    C = {}
    t0 = time.time()
    for r0 in (0.0, 0.2, 0.5, 0.8):
        X, masque = donnees(rng_c, 60, 12, r0)
        res = {}
        for tau in (0.0, 2.0):
            ss_eff = np.random.SeedSequence(ENTROPIE_VERIF, spawn_key=(int(10 * tau), 7, int(10 * r0)))
            rngs = [np.random.default_rng(s) for s in ss_eff.spawn(4)]
            acc = {}
            for si in range(X.shape[2]):
                for di in range(4 if tau > 0 else 1):
                    al, _ = m.un_passage(X[:, :, si], masque, plis, rngs[di], tau)
                    for c, v in al.items():
                        acc.setdefault(f"{c[0]}:{c[1]}", []).append(float(v.mean()))
            res[f"tau={tau}"] = {k: {"moyenne": float(np.mean(v)), "mediane": float(np.median(v))} for k, v in acc.items()}
        res["ville_tau2_moins_tau0_moyenne"] = res["tau=2.0"]["ville:processus_e"]["moyenne"] - res["tau=0.0"]["ville:processus_e"]["moyenne"]
        C[f"r0={r0}"] = res
    sortie["C_taux_selon_correlation_naturelle"] = C
    sortie["C_duree_s"] = time.time() - t0
    # D
    rng_d = np.random.default_rng(enfants[2])
    taux = {s: [] for s in ("max", "somme_terminale", "processus_e")}
    for rep in range(150):
        X, masque = donnees(rng_d, 60, 1, 0.3)
        pl = m.plis_de(60, rng_d)
        al, _ = m.un_passage(X[:, :, 0], masque, pl, None, 0.0)
        for s in taux:
            taux[s].append(float(al[("conforme", s)].mean()))
    sortie["D_taux_conforme_une_sonde_tau0"] = {
        s: {"moyenne": float(np.mean(v)), "P_zero": float(np.mean(np.array(v) == 0)),
            "P_sup_0075": float(np.mean(np.array(v) > 0.075)), "P_sup_010": float(np.mean(np.array(v) > 0.10)),
            "quantile_95": float(np.quantile(v, 0.95))} for s, v in taux.items()}
    # E
    pl = m.plis_de(60, np.random.default_rng(enfants[3]))
    norm_count = np.zeros(60, int)
    for ev in pl:
        cal = np.setdiff1d(np.arange(60), ev)
        norm_count[cal[:m.PART_NORMALISATION]] += 1
    sortie["E_normalisation"] = {"indices_jamais_en_normalisation": int((norm_count == 0).sum()),
                                 "indice_max_en_normalisation": int(np.flatnonzero(norm_count).max()),
                                 "compte_par_indice_0_a_29": norm_count[:30].tolist()}
    # F
    g = np.random.default_rng(enfants[4])
    a = g.normal(size=5)
    b = g.normal(size=5)
    sortie["F_meme_generateur_reutilise_donne_des_effets_differents"] = bool(not np.allclose(a, b))
    json.dump(sortie, sys.stdout, ensure_ascii=False, indent=1)
    print()


if __name__ == "__main__":
    main()
