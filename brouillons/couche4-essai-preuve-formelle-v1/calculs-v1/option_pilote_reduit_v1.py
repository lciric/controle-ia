"""Option D-1 (ii) : pilote réduit à 40 graines (8 par classe), mêmes 20 items de contrôle, audit sur 50 %.
Coûts unitaires repris de sortie-calculs-devis-v3.txt (USD) ; pire cas : plafonds et pires cas unitaires de la même sortie."""
import math
ATT = {"L": 1.162, "S": 0.374, "N": 0.18, "T": 0.55, "G": 0.26, "A": 0.19}
PIRE = {"L": 4.0, "S": 4.0, "N": 0.66, "T": 1.68, "G": 0.88, "A": 0.46}
graines, controle = 40, 20
g = math.ceil(graines * 1.2)
items = 2 * graines + controle
audit = math.ceil(0.5 * items)
for nom, c in (("attendu", ATT), ("pire cas", PIRE)):
    total = g * (c["T"] + c["G"]) + items * (c["L"] + c["S"] + c["N"]) + audit * c["A"]
    print(f"{nom:8s} : {items} items, {g} graines générées, total {total:.2f} USD")
