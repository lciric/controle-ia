"""Coûts de la plus petite suite décisive pour fermer la brèche de W2 — v1.

Chaque entrée vient d'une source nommée (sortie scellée de la troisième course, textes du nul v9 et de l'attaque v4) ou d'une
mesure de cette session (rejeu sous v8 : 10,7 s pour 200 évaluations). Aucun jugement n'est lancé ici.

Usage : python -I couts_suite_w2_v1.py <attaque-goodhart-v3.json>
"""
import json
import sys


def main():
    d = json.load(open(sys.argv[1], encoding="utf-8"))
    appels = {"W1": [], "W2": []}
    for s in d["suites"]:
        for t in s["tentatives"]:
            for a in t["appels"]:
                appels[s["monde"]].append((float(a["cout_usd"]), float(a["duree_s"])))
    par_appel = {w: sum(c for c, _ in v) / len(v) for w, v in appels.items()}
    duree = {w: sum(s for _, s in v) / len(v) for w, v in appels.items()}
    w1_appels, w1_usd = len(appels["W1"]), sum(c for c, _ in appels["W1"])
    # W2 sous le v9 : deux suites de 16 tentatives sans promotion, plus le juge ancien (v8) comme dans la troisième course
    w2_ancien = sum(len(t["appels"]) for s in d["suites"] if s["monde"] == "W2" and s["juge"] == "v8" for t in s["tentatives"])
    par_unite_w2_v9 = 2 * 16 + w2_ancien / 24
    w2_v9_appels = 24 * par_unite_w2_v9
    bas, haut = par_appel["W2"], par_appel["W1"]
    print("coût moyen par appel : W1 %.4f, W2 %.4f dollars ; durée moyenne : W1 %.1f s, W2 %.1f s" % (haut, bas, duree["W1"], duree["W2"]))
    print("W1 tel que joué : %d appels, %.2f dollars" % (w1_appels, w1_usd))
    print("W2 sous v9 : %.2f appels par unité, %.0f appels ; %.1f à %.1f dollars" % (par_unite_w2_v9, w2_v9_appels, w2_v9_appels * bas, w2_v9_appels * haut))
    print("attaque v4 telle que rédigée (W1 + W2) : %.0f appels ; %.1f à %.1f dollars" % (
        w1_appels + w2_v9_appels, w1_usd + w2_v9_appels * bas, w1_usd + w2_v9_appels * haut))
    print("attaque v4 proposée (W2 + W2 gradué, au plus) : %.0f appels ; %.1f à %.1f dollars ; durée des appels %.1f à %.1f h" % (
        2 * w2_v9_appels, 2 * w2_v9_appels * bas, 2 * w2_v9_appels * haut,
        2 * w2_v9_appels * duree["W2"] / 3600, 2 * w2_v9_appels * duree["W1"] / 3600))
    # Devis du brouillon 2 de l'attaque v4, recalculé
    print("devis du brouillon 2 recalculé : appels %d à %d, au plus %d ; dollars %.2f à %.2f, au plus %.2f" % (
        24 * (36 + 34), 24 * (48 + 40), 48 * 64, 24 * (36 + 34) * 0.062, 24 * (48 + 40) * 0.062, 48 * 64 * 0.062))
    # Étapes hors ligne : évaluations appariées (v9 et v8 sur les mêmes issues), 0,25 à 0,29 s mesurées, 0,5 s de devis
    for nom, n in (("rejeu des 48 lois", 48 * 200), ("W2 gradué (7 lignes x 1 000)", 7 * 1000), ("validation du v9 (31 x 1 000)", 31 * 1000)):
        print("%s : %d évaluations ; %.0f à %.0f min sur un cœur aux durées mesurées, %.0f min au devis de 0,5 s" % (
            nom, n, n * 0.25 / 60, n * 0.29 / 60, n * 0.5 / 60))
    print("plafond de multiplicité 1 - 0,95^16 = %.4f" % (1 - 0.95 ** 16))
    print("rejeu sous v8 mesuré : %.4f s par évaluation" % (10.7 / 200))


if __name__ == "__main__":
    main()
