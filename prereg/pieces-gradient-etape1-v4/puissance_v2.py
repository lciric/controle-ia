"""Taux des lectures de la règle gelée de la v4 (trois niveaux, Δ ≥ 0,10 dans chaque réplique), par le code gelé
`analyse_gradient.puissance_h_g1` (non opposable, R7 : modèle de variance supposé). Deux répliques de trois paires."""
import json, sys
from essaim_m3 import analyse_gradient as A
sortie = []
for sigma in (0.0, 0.25, 0.5):
    for gain in (0.0, 0.10, 0.20):
        r = A.puissance_h_g1(gain, n_repliques=2, paires_par_replique=3, sigma_replique=sigma, repetitions=400, n_tirages=400,
                             entropie=20261026)
        print(json.dumps(r, ensure_ascii=False), flush=True)
        sortie.append(r)
json.dump(sortie, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
