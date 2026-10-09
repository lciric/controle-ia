"""T0.4 v3, contre-lecture 1 (X-1) : la grandeur de la garde de production de la v3 (99e centile, par action et par
couche, des écarts par jeton sur toutes les positions capturées) recalculée sur la production de la v2.
Source : champ `q99` (toutes positions) des profils d'`arret.json` du run A de la v2, calculé par `profil_ecarts`
avec `np.quantile(e, 0.99)` sur le même tableau que la garde de la v3 (`ecart_equivalence(..., quantile=0.99)`).
Lancement depuis la racine du dépôt : python3 -I diag/T0.4-v3-recalculs/q99_production_v2_v1.py"""
import hashlib
import json
from pathlib import Path

chemin = Path("diag/20261005-144628-validation-reelle/arret.json")
print("arret.json sha256", hashlib.sha256(chemin.read_bytes()).hexdigest())
prod = json.loads(chemin.read_text())["resultat"]["partiel"]["production"]
repere = prod["repere_precision"]
par_couche, plus_grand, ou = {}, -1.0, None
fractions = []
for e in prod["episodes"]:
    eq = e["equivalence"]
    for cle, profil in eq["profils"].items():
        n, lc = eq["positions_capturees"][cle], eq["longueurs_contexte"][cle]
        fractions.append((n - lc) / n)
        for c, p in profil.items():
            par_couche[c] = max(par_couche.get(c, 0.0), p["q99"])
            if p["q99"] > plus_grand:
                plus_grand, ou = p["q99"], (e["episode"], cle, c)
cles = sorted(par_couche, key=int)
print("actions comparées :", len(fractions))
print("plus grand 99e centile par action :", round(plus_grand, 4), "à", ou)
print("par couche :", {c: round(par_couche[c], 4) for c in cles})
print("99e centile du repère :", {c: round(repere[c]["q99"], 4) for c in cles})
print("rapport au repère :", {c: round(par_couche[c] / repere[c]["q99"], 3) for c in cles})
q = max(r["q99"] for r in repere.values())
print("deux fois le 99e centile du repère le plus haut :", round(2 * q, 4))
print("seuil 0,2 / plus grand 99e centile :", round(0.2 / plus_grand, 3), "; 2 × repère / plus grand :", round(2 * q / plus_grand, 3))
print("zone générée / positions capturées, par action : min", round(min(fractions), 4), "; max", round(max(fractions), 4))
