"""Taux de coupure à tort de la règle gelée des pannes (`analyse_gradient.regle_pannes`) quand les deux bras ont le même
taux d'échec extérieur p (descriptif, non opposable, R7 : comparaisons supposées indépendantes). Par comparaison, puis par
paire (appels + trois sources de recherche), puis P(au moins deux paires coupées sur six)."""
import json, math, sys
from essaim_m3 import analyse_gradient as A
lignes = []
for n in (10, 20, 30, 160, 480):
    for p in (0.02, 0.05, 0.10, 0.20, 0.30):
        une = A.coupure_sous_taux_identiques(n, p)
        paire = 1 - (1 - une) ** 4
        deux_sur_six = 1 - sum(math.comb(6, k) * paire ** k * (1 - paire) ** (6 - k) for k in (0, 1))
        lignes.append({"n": n, "p": p, "par_comparaison": round(une, 5), "par_paire_4_comparaisons": round(paire, 5),
                       "au_moins_2_sur_6": round(deux_sur_six, 5)})
json.dump(lignes, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
print(max(l["par_comparaison"] for l in lignes), max(l["au_moins_2_sur_6"] for l in lignes))
