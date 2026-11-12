"""Puissance par simulation du préenregistrement « candidat 1 corrigé » (agrégateurs, R1 v4) — script à côté du brouillon 1.

Calage : aires d'action publiées de P3 (verdict P3 v2, l. 209 et 214 : 0,5248 enjeux, 0,5748 tromperie), puis une grille
jusqu'à 0,99 (la sonde W de R1, entraînée sur l'organisme flagrant, n'a aucune aire lue par l'auteur ; grille seulement).
Graine : SeedSequence(20261106) racine, une graine dérivée par cellule (R9). Sortie : JSON sur la sortie standard.
Commande : PYTHONPATH=src timeout 900 nice -n 10 python brouillons/preenregistrement-agregation-r1-v4-v1-puissance.py
"""
import json
import sys

import numpy as np

from controle_ia.agregation_r1_v4.puissance_v1 import AIRES_P3, simuler

AIRES = (0.5248, 0.5748, 0.65, 0.75, 0.85, 0.95, 0.99)
ETAS = (0.0, 0.5)
TAUS = (0.0, 0.5)
REPLIQUES = 200
racine = np.random.SeedSequence(20261106)
cellules = [(a, e, t) for a in AIRES for e in ETAS for t in TAUS]
enfants = racine.spawn(len(cellules))
sortie = {"racine": 20261106, "repliques": REPLIQUES, "aires_p3": AIRES_P3, "numpy": np.__version__, "cellules": []}
for (a, e, t), g in zip(cellules, enfants):
    sortie["cellules"].append(simuler(a, e, t, REPLIQUES, np.random.default_rng(g)))
    print(f"{a} {e} {t}", file=sys.stderr, flush=True)
json.dump(sortie, sys.stdout, ensure_ascii=False, indent=1)
