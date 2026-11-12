"""Contre-lecture du complément v2 (données SYNTHÉTIQUES seulement). Importe le script v2 sans le modifier.

 I. M3 sous le nul avec K = 39 : loi du taux conforme d'une sonde à τ = 0 (un tirage) : P(≤ 1/60), P(< 0,02),
    P(> 0,08), P(> 0,10), moyenne.
 J. Bras M4 tel que codé (calibrage sans effet, évaluation avec effet τ = 2) à r0 = 0,2 et 0,8 ; et une variante
    « à variance marginale constante » (évaluation : r = sqrt(1/(1+τ²))·(x − m) + m + effet) qui isole la dépendance
    de l'élargissement d'échelle.
 K. Estimateur de corrélation intraclasse du script : biais pour r0 connu (0 ; 0,2 ; 0,5 ; 0,8), longueurs 5 à 10.
 L. Partage normalisation / seuils : positions dans la permutation des épisodes de normalisation.
Graines : SeedSequence(20261027234000), enfants consignés.
"""
import importlib.util
import json
import math
import sys

import numpy as np

ENTROPIE = 20261027234000


def charger(chemin):
    spec = importlib.util.spec_from_file_location("analyse_v2_relue", chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def donnees(rng, E, S, r0, tmin=5, tmax=10):
    u = rng.normal(0, math.sqrt(r0), size=(E, 1, S))
    X = u + rng.normal(0, math.sqrt(1 - r0), size=(E, tmax, S))
    masque = np.ones((E, tmax), bool)
    for e in range(E):
        masque[e, rng.integers(tmin, tmax + 1):] = False
    X[~masque] = np.nan
    return X, masque


def passage_variance_constante(m, X, masque, plis, perm, effet, tau):
    """Comme un_passage(calibrage_sans_effet=True) mais l'évaluation garde la variance marginale par action."""
    E = X.shape[0]
    sd = float(np.nanstd(X[masque])); mm = float(np.nanmean(X[masque]))
    c = 1.0 / math.sqrt(1.0 + tau * tau)
    Xe = mm + c * ((X - mm) + (tau * sd * effet)[:, None])
    rang = {e: i for i, e in enumerate(perm.tolist())}
    al = {s: np.zeros(E, bool) for s in m.STATISTIQUES}
    for ev in plis:
        cal = np.array(sorted(np.setdiff1d(np.arange(E), ev).tolist(), key=lambda e: rang[e]))
        ni, si = cal[:m.PART_NORMALISATION], cal[m.PART_NORMALISATION:]
        a = X[ni][masque[ni]]
        mu0, sig = float(a.mean()), float(a.std(ddof=1))
        fc, _ = m.statistiques((X[si] - mu0) / sig, masque[si])
        se = {s: m.seuil_conforme(fc[s], m.ALPHA) for s in m.STATISTIQUES}
        fe, _ = m.statistiques((Xe[ev] - mu0) / sig, masque[ev])
        for s in m.STATISTIQUES:
            al[s][ev] = fe[s] > se[s]
    return al


def main():
    m = charger(sys.argv[1])
    ss = np.random.SeedSequence(ENTROPIE)
    c = ss.spawn(4)
    out = {"manifeste": {"entropie": ENTROPIE, "enfants": [list(x.spawn_key) for x in c], "numpy": np.__version__,
                         "script_relu": sys.argv[1]}}
    # I
    rng = np.random.default_rng(c[0])
    taux = {s: [] for s in ("max", "somme_terminale", "processus_e")}
    for rep in range(200):
        X, mk = donnees(rng, 60, 1, 0.3)
        perm = rng.permutation(60)
        al, K = m.un_passage(X[:, :, 0], mk, m.plis_de_perm(perm), perm, np.zeros(60), 0.0)
        for s in taux:
            taux[s].append(float(al[("conforme", s)].mean()))
    out["I_M3_nul_K39_une_sonde"] = {s: {"moyenne": float(np.mean(v)), "P_le_1sur60": float(np.mean(np.array(v) <= 1 / 60 + 1e-12)),
                                         "P_inf_002": float(np.mean(np.array(v) < 0.02)), "P_sup_008": float(np.mean(np.array(v) > 0.08)),
                                         "P_sup_010": float(np.mean(np.array(v) > 0.10))} for s, v in taux.items()}
    out["I_K_par_pli"] = K
    # J
    rng = np.random.default_rng(c[1])
    J = {}
    for r0 in (0.2, 0.8):
        X, mk = donnees(rng, 60, 8, r0)
        perm = rng.permutation(60); plis = m.plis_de_perm(perm)
        code, varc = {}, {}
        for d in range(4):
            effet = rng.normal(size=60)
            for si in range(X.shape[2]):
                al, _ = m.un_passage(X[:, :, si], mk, plis, perm, effet, 2.0, calibrage_sans_effet=True)
                for k, v in al.items():
                    code.setdefault(f"{k[0]}:{k[1]}", []).append(float(v.mean()))
                alv = passage_variance_constante(m, X[:, :, si], mk, plis, perm, effet, 2.0)
                for k, v in alv.items():
                    varc.setdefault(f"conforme:{k}", []).append(float(v.mean()))
        J[f"r0={r0}"] = {"bras_tel_que_code": {k: float(np.mean(v)) for k, v in code.items()},
                         "variante_variance_constante": {k: float(np.mean(v)) for k, v in varc.items()}}
    out["J_bras_M4"] = J
    # K
    rng = np.random.default_rng(c[2])
    Kres = {}
    for r0 in (0.0, 0.2, 0.5, 0.8):
        est = []
        for rep in range(300):
            X, mk = donnees(rng, 60, 1, r0)
            est.append(m.correlation_intra_episode(X[:, :, 0], mk))
        Kres[f"r0={r0}"] = {"moyenne": float(np.mean(est)), "ecart_type": float(np.std(est, ddof=1))}
    out["K_correlation_intraclasse"] = Kres
    # L
    perm = np.random.default_rng(c[3]).permutation(60)
    pos = {e: i for i, e in enumerate(perm.tolist())}
    rang = pos
    positions_norm = set()
    for ev in m.plis_de_perm(perm):
        cal = sorted(np.setdiff1d(np.arange(60), ev).tolist(), key=lambda e: rang[e])
        positions_norm |= {pos[e] for e in cal[:m.PART_NORMALISATION]}
    out["L_positions_permutation_en_normalisation"] = sorted(positions_norm)
    json.dump(out, sys.stdout, ensure_ascii=False, indent=1)
    print()


if __name__ == "__main__":
    main()
