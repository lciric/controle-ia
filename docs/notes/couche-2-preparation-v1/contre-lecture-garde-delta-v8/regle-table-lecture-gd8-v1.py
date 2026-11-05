"""Contre-lecture GD8 (R2) — applique à la lettre la règle de lecture de la table du pilote (rapport v8, § 1) et dit où elle ne rend rien.

Règle (rapport v8, § 1) : ρ_haut = ρ̂ + 1,645 × écart-type de la lecture (côté sabotage) ; dans chaque hypothèse sur le sujet (ρ_A = ρ_B ; ρ_A = 2 ρ_B), prendre la ligne
« égale ou immédiatement supérieure » à ρ_haut ; n_h = le plus grand des deux ; au-delà de la dernière ligne, « la table ne dit rien ».
Écart-type : celui de `precision-rho-pilote-v8-sortie.json` (p = 0,4) à la valeur de ρ de la grille {0,05 ; 0,10 ; 0,17 ; 0,25} égale ou immédiatement supérieure à ρ̂
(prudent ; au-delà de 0,25 : celui de 0,25), pour N ∈ {50 ; 100 ; 288} unités au pilote. Aucun tirage.
Usage : python3 -I -B regle-table-lecture-gd8-v1.py TABLEAUX_V8_SORTIE.json PRECISION_RHO_V8_SORTIE.json SORTIE.json
"""
import hashlib
import json
import os
import sys

T_CHEMIN, P_CHEMIN, SORTIE = sys.argv[1:4]
T = json.load(open(T_CHEMIN, encoding="utf-8"))
P = json.load(open(P_CHEMIN, encoding="utf-8"))
table = T["table_de_lecture_pilote"]
grille_sd = (0.05, 0.10, 0.17, 0.25)


def sd(rho_hat, N):
    r = next((g for g in grille_sd if g >= rho_hat - 1e-12), 0.25)
    return [c for c in P["cellules"] if c["p"] == 0.4 and c["rho"] == r and c["N"] == N][0]["ecart_type"]


def ligne(hyp, rho_haut):
    lignes = sorted([l for l in table if l["hypothese"] == hyp], key=lambda l: l["rho_B"])
    for l in lignes:
        if l["rho_B"] >= rho_haut - 1e-12:
            return l
    return None


res = {"script": os.path.basename(__file__), "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
       "entrees": {os.path.basename(c): hashlib.sha256(open(c, "rb").read()).hexdigest() for c in (T_CHEMIN, P_CHEMIN)},
       "grille_hypothese_1": sorted(l["rho_B"] for l in table if l["hypothese"] == "ρ_A = ρ_B"),
       "grille_hypothese_2": sorted(l["rho_B"] for l in table if l["hypothese"] == "ρ_A = 2 ρ_B"), "lectures": []}
for N in (50, 100, 288):
    for i in range(0, 31):
        rho_hat = i / 100
        haut = rho_hat + 1.645 * sd(rho_hat, N)
        l1, l2 = ligne("ρ_A = ρ_B", haut), ligne("ρ_A = 2 ρ_B", haut)
        if l1 is None or l2 is None:
            nh40 = nh160 = None
        else:
            nh40, nh160 = max(l1["n_h_40"], l2["n_h_40"]), max(l1["n_h_160"], l2["n_h_160"])
        res["lectures"].append({"N_pilote": N, "rho_chapeau": rho_hat, "rho_haut": round(haut, 4),
                                "ligne_hyp1": None if l1 is None else l1["rho_B"], "ligne_hyp2": None if l2 is None else l2["rho_B"],
                                "n_h_40": nh40, "n_h_160": nh160, "rendu": nh40 is not None})
for N in (50, 100, 288):
    L = [x for x in res["lectures"] if x["N_pilote"] == N]
    rendus = [x["rho_chapeau"] for x in L if x["rendu"]]
    res[f"N={N}"] = {"plus_grand_rho_chapeau_lu": max(rendus) if rendus else None,
                     "premier_rho_chapeau_sans_reponse": min((x["rho_chapeau"] for x in L if not x["rendu"]), default=None),
                     "sans_hypothese_2_premier_sans_reponse": min((x["rho_chapeau"] for x in L if x["ligne_hyp1"] is None), default=None)}
with open(SORTIE, "x", encoding="utf-8") as f:
    json.dump(res, f, indent=1, ensure_ascii=False)
    f.write("\n")
print("grilles :", res["grille_hypothese_1"], res["grille_hypothese_2"])
for N in (50, 100, 288):
    print(f"N = {N} :", res[f"N={N}"])
    for x in res["lectures"]:
        if x["N_pilote"] == N and x["rho_chapeau"] in (0.0, 0.03, 0.05, 0.08, 0.10, 0.13, 0.15, 0.17, 0.20):
            print("   ρ̂ = %.2f → ρ_haut %.3f ; ligne hyp1 %s, hyp2 %s → n_h %s / %s" % (x["rho_chapeau"], x["rho_haut"], x["ligne_hyp1"], x["ligne_hyp2"], x["n_h_40"], x["n_h_160"]))
