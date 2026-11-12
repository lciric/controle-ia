"""Contre-lecture, partie 2 (données SYNTHÉTIQUES seulement) : gardes de la liste d'arrêt et largeur des intervalles.

 G. Un score valide non fini (NaN) placé hors de l'ensemble de normalisation : le script s'arrête-t-il, ou compte-t-il
    zéro alerte en silence ?
 H. Intervalle par grappes (alertes figées, comme le script) contre dispersion réelle d'un jeu à l'autre (nouveau jeu de
    60 épisodes, calibrage refait) : écart type de la médiane de Ville à τ = 0 et du par-action, r0 = 0,2,
    6 sondes corrélées entre elles (facteur commun d'épisode et de sonde).
Graines : numpy.random.SeedSequence(ENTROPIE_VERIF2), enfants consignés.
"""
import importlib.util
import json
import math
import sys

import numpy as np

ENTROPIE_VERIF2 = 20261027232100


def charger(chemin):
    spec = importlib.util.spec_from_file_location("analyse_relue", chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def jeu(rng, E=60, S=6, r0=0.2, tmin=5, tmax=10):
    u = rng.normal(0, math.sqrt(r0), size=(E, 1, 1))  # effet d'épisode commun aux sondes (sondes corrélées)
    X = u + rng.normal(0, math.sqrt(1 - r0), size=(E, tmax, S))
    masque = np.ones((E, tmax), bool)
    for e in range(E):
        masque[e, rng.integers(tmin, tmax + 1):] = False
    X[~masque] = np.nan
    return X, masque


def main():
    m = charger(sys.argv[1])
    ss = np.random.SeedSequence(ENTROPIE_VERIF2)
    c = ss.spawn(3)
    sortie = {"manifeste": {"entropie": ENTROPIE_VERIF2, "enfants": [list(x.spawn_key) for x in c], "numpy": np.__version__}}
    # G
    rng = np.random.default_rng(c[0])
    X, masque = jeu(rng, S=1, r0=0.0)
    plis = m.plis_de(60, rng)
    X1 = X[:, :, 0].copy()
    ref, _ = m.un_passage(X1, masque, plis, None, 0.0)
    X1[59, 0] = np.nan  # épisode d'indice 59 : jamais en normalisation (ordre trié), action valide
    try:
        al, _ = m.un_passage(X1, masque, plis, None, 0.0)
        sortie["G_nan_hors_normalisation"] = {
            "arret": False,
            "alertes_reference": {f"{k[0]}:{k[1]}": int(v.sum()) for k, v in ref.items()},
            "alertes_avec_nan": {f"{k[0]}:{k[1]}": int(v.sum()) for k, v in al.items()}}
    except Exception as exc:  # noqa: BLE001
        sortie["G_nan_hors_normalisation"] = {"arret": True, "exception": repr(exc)}
    # H
    rng_h = np.random.default_rng(c[1])
    rng_b = np.random.default_rng(c[2])
    med_ville, med_pa, larg_ville, larg_pa = [], [], [], []
    for rep in range(40):
        X, masque = jeu(rng_h)
        pl = m.plis_de(60, rng_h)
        Av, Ap = [], []
        for si in range(X.shape[2]):
            al, _ = m.un_passage(X[:, :, si], masque, pl, None, 0.0)
            Av.append(al[("ville", "processus_e")])
            Ap.append(al[("par_action", "max")])
        Av, Ap = np.array(Av), np.array(Ap)
        med_ville.append(float(np.median(Av.mean(1))))
        med_pa.append(float(np.median(Ap.mean(1))))
        if rep < 10:
            bv, bp = [], []
            for _ in range(500):
                idx = rng_b.integers(0, 60, size=60)
                bv.append(float(np.median(Av[:, idx].mean(1))))
                bp.append(float(np.median(Ap[:, idx].mean(1))))
            larg_ville.append(float(np.std(bv)))
            larg_pa.append(float(np.std(bp)))
    sortie["H_dispersion"] = {
        "ville_tau0": {"ecart_type_entre_jeux": float(np.std(med_ville, ddof=1)), "ecart_type_grappes_moyen": float(np.mean(larg_ville)),
                       "moyenne": float(np.mean(med_ville))},
        "par_action_tau0": {"ecart_type_entre_jeux": float(np.std(med_pa, ddof=1)), "ecart_type_grappes_moyen": float(np.mean(larg_pa)),
                            "moyenne": float(np.mean(med_pa))},
        "jeux": 40, "jeux_avec_grappes": 10, "reechantillonnages": 500}
    json.dump(sortie, sys.stdout, ensure_ascii=False, indent=1)
    print()


if __name__ == "__main__":
    main()
