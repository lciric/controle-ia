"""Puissance de P3 (calcul de conception, non décisif, sur processeur ; aucune donnée de P3 lue).

Usage : PYTHONPATH=src python puissance_p3.py EPISODES_DU_PILOTE [REPLIQUES]

1. Effet sur le coût (P3-P1) : variabilité, d'un épisode à l'autre d'une même tâche, de la statistique de tâche (moyenne du
   log10 des coûts lisibles de l'épisode, `statistiques.cout_de_tache`), estimée sur les trois épisodes honnêtes par tâche du
   pilote de T0.5 (même agent, même environnement (a), T = 10, coût lu par `heures_declarees`). Puis, pour chaque paire
   d'épisodes honnêtes (l'un joue l'honnête, l'autre le saboteur décalé de δ), l'intervalle de `effet_cout_apparie`
   (10 000 tirages, 95 %) à δ = 0 ; 0,05 ; 0,10 ; 0,20 ; 0,48 (log10 de 3 : consigne suivie en entier).
2. Détection (P3-P3) : tables synthétiques, 60 tâches × 10 actions par condition, score = √ρ·u_tâche + √(1−ρ)·e + Δ·y,
   200 sondes de plancher de même structure sans Δ ; `statistiques.detection` (blocs de tâches, 2 000 tirages, 97,5 %,
   quantile 0,95 du plancher). Pour ρ ∈ {0 ; 0,3 ; 0,6} et Δ ∈ {0 ; 0,15 ; 0,3 ; 0,5} : aire moyenne, demi-largeur moyenne,
   quantile moyen du plancher, part des répliques « au-dessus du plancher ».
Graines : `numpy.random.SeedSequence(20261017)`, une graine fille par case (R9).
"""
import json
import sys
from itertools import combinations
from pathlib import Path

import numpy as np

from controle_ia.environnements.propositions import heures_declarees, lire_action
from controle_ia.premier_test_ia.statistiques import cout_de_tache, detection, effet_cout_apparie

chemin = sys.argv[1]
repliques = int(sys.argv[2]) if len(sys.argv) > 2 else 40
racine = np.random.SeedSequence(20261017)
graines = iter(racine.spawn(200))

# 1. coût : pilote, épisodes honnêtes
fiches = json.loads(Path(chemin).read_text(encoding="utf-8"))["resultat"]["fiches"]
par_tache: dict[str, list] = {}
for f in fiches:
    couts = [heures_declarees(lire_action(a["texte"]).champs.get("COST")) for a in f["actions"]]
    par_tache.setdefault(f["tache"], []).append(couts)
valeurs = {t: [cout_de_tache(c)["valeur"] for c in eps] for t, eps in par_tache.items()}
variances = [np.var([v for v in vs if v is not None], ddof=1) for vs in valeurs.values()
             if sum(v is not None for v in vs) >= 2]
sw2 = float(np.mean(variances))
n_lisibles = sum(1 for vs in valeurs.values() for v in vs if v is not None)
moyennes = [np.mean([v for v in vs if v is not None]) for vs in valeurs.values() if any(v is not None for v in vs)]
print(f"pilote : {len(fiches)} épisodes, {len(par_tache)} tâches, {n_lisibles} épisodes à coût lisible")
print(f"variance intra-tâche (entre épisodes) de la statistique de tâche : {sw2:.4f} (écart type {np.sqrt(sw2):.3f}), "
      f"sur {len(variances)} tâches ; écart type entre tâches des moyennes : {np.std(moyennes, ddof=1):.3f}")
for n in (60, 58):
    se = np.sqrt(2 * sw2 / n)
    print(f"  {n} tâches : erreur type de l'effet apparié {se:.4f} ; demi-largeur à 95 % ≈ {1.96 * se:.4f} ; "
          f"effet minimal détectable (80 %, bilatéral 5 %) ≈ {2.80 * se:.4f}")
taches = sorted(par_tache)
for delta in (0.0, 0.05, 0.10, 0.20, 0.48):
    lignes = []
    for i, j in combinations(range(3), 2):
        hon = {t: par_tache[t][i] for t in taches if len(par_tache[t]) == 3}
        sab = {t: [None if c is None else c * 10 ** delta for c in par_tache[t][j]] for t in hon}
        r = effet_cout_apparie(sab, hon, np.random.default_rng(next(graines)), 10_000, 0.95)
        lignes.append(f"e{j}−e{i} : {r['effet']:+.3f} [{r['bas']:+.3f} ; {r['haut']:+.3f}] ({r['n_taches']} tâches)")
    print(f"  δ = {delta:.2f} : " + " | ".join(lignes))

# 2. détection : tables synthétiques
print(f"détection, {repliques} répliques par case (60 tâches × 10 actions par condition ; 200 sondes de plancher) :")
tache = np.repeat(np.arange(60), 20).astype(str)
cond = np.tile(np.r_[np.full(10, "saboteur"), np.full(10, "honnete")], 60)
y = (cond == "saboteur").astype(float)
for rho in (0.0, 0.3, 0.6):
    for delta in (0.0, 0.15, 0.3, 0.5):
        rng = np.random.default_rng(next(graines))
        aires, demi, quant, dessus = [], [], [], []
        for r in range(repliques):
            u = rng.normal(size=60)[np.repeat(np.arange(60), 20)]
            sc = np.sqrt(rho) * u + np.sqrt(1 - rho) * rng.normal(size=1200) + delta * y
            up = rng.normal(size=(60, 200))[np.repeat(np.arange(60), 20)]
            pl = np.sqrt(rho) * up + np.sqrt(1 - rho) * rng.normal(size=(1200, 200))
            d = detection(sc, pl, cond, tache, "saboteur", "honnete", 2000, int(rng.integers(2 ** 31)), 0.975)
            aires.append(d["aire"])
            demi.append((d["haut"] - d["bas"]) / 2)
            quant.append(d["plancher_quantile"])
            dessus.append(d["au_dessus_du_plancher"])
        print(f"  ρ = {rho:.1f}, Δ = {delta:.2f} : aire {np.mean(aires):.3f} ; demi-largeur à 97,5 % {np.mean(demi):.3f} ; "
              f"plancher (q 0,95) {np.mean(quant):.3f} ; au-dessus : {np.mean(dessus):.2f}")
