"""« La règle n_h = max(288 ; n80 lu sur la loi réelle) est-elle un dé ? » — pilotes synthétiques (session-depot, synthèse P-26) — v1.

Tire des fichiers de pilote synthétiques (N_pilote unités, k comparateurs, f_A partagé, B_j binomiaux indépendants,
espérance g = 0 vraie), puis calcule n80 comme le ferait le script v4 sur un fichier réel : loi « réelle recentrée »
(`LoiReelle`, rééchantillonnage d'unités entières), minimum des k gardes, dichotomie `n_pour_puissance`. Compare à la
valeur de la loi vraie (binomiale). Réutilise la copie du script v4 (empreinte 5bf015b6…, non modifiée).
Exploratoire, processeur seul, non opposable.
"""
import argparse
import importlib.util
import json
import os
import platform
import sys
import time

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
CHEMIN_V4 = os.path.join(ICI, "script-v4-copie", "simulation-puissance-garde-delta-v4.py")
spec = importlib.util.spec_from_file_location("simv4", CHEMIN_V4)
simv4 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(simv4)


def principal():
    p = argparse.ArgumentParser()
    p.add_argument("--graine", type=int, required=True)
    p.add_argument("--pilotes", type=int, default=30)
    p.add_argument("--N", default="16,64,160", help="unités du fichier de pilote")
    p.add_argument("--K", default="10,3")
    p.add_argument("--taux", type=float, default=0.01)
    p.add_argument("--delta", type=float, default=0.05)
    p.add_argument("--seuil", type=float, default=160.0)
    p.add_argument("--k", type=int, default=8)
    p.add_argument("--biais", type=float, default=0.0)
    p.add_argument("--repetitions", type=int, default=1000)
    a = p.parse_args()
    debut = time.time()
    sortie = {"version": "pilote-synthetique-n80-v1", "statut": "exploratoire, non opposable",
              "script_v4_sha256": simv4.hashlib.sha256(open(CHEMIN_V4, "rb").read()).hexdigest(),
              "reglages": vars(a), "resultats": {}}
    for K in [int(x) for x in a.K.split(",")]:
        secours = simv4.LoiSynthetique(K, K, a.taux, 0.4, 0.10, True, 0.0)
        for N in [int(x) for x in a.N.split(",")]:
            rng, _ = simv4.rng_de(a.graine, f"pilotes|K={K}|N={N}")
            n80s, sd, nuls = [], [], []
            for i in range(a.pilotes):
                fa = rng.binomial(K, a.taux, size=N) / K
                fb = rng.binomial(K, a.taux, size=(a.k, N)) / K
                eg = [fa - fb[j] for j in range(a.k)]
                loi = simv4.LoiReelle(eg, [], True)
                r = simv4.n_pour_puissance(loi, secours, a.repetitions, a.delta, a.seuil, a.k, a.biais, a.graine,
                                           f"pilote|K={K}|N={N}|i={i}")
                n80s.append(r["n_approx"] if r["n_approx"] is not None else float("inf"))
                g = np.stack(eg)
                sd.append(float(g.std(ddof=1, axis=1).mean()))
                nuls.append(float((g == 0).mean()))
            n80s_arr = np.array(n80s, dtype=float)
            sortie["resultats"][f"K={K}|N_pilote={N}"] = {
                "n80_par_pilote": n80s,
                "quantiles_0_10_50_90_100": [float(x) for x in np.quantile(n80s_arr, [0, 0.1, 0.5, 0.9, 1.0])],
                "part_n80_sous_288": float((n80s_arr < 288).mean()),
                "ecart_type_moyen_de_g": float(np.mean(sd)), "part_moyenne_g_nul": float(np.mean(nuls))}
    sortie["environnement"] = {"python": platform.python_version(), "numpy": np.__version__,
                               "duree_s": round(time.time() - debut, 1)}
    json.dump(sortie, sys.stdout, indent=1, ensure_ascii=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    principal()
