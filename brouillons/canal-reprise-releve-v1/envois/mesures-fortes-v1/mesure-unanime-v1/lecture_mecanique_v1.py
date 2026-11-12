"""Lecture **mécanique** de la sortie réelle de la mesure unanime selon les seuils gelés du préenregistrement v5 (section
« Seuil » et table des prédictions) : M1, M2 (contrôle), M2 bis, M2 ter (cinq issues ordonnées), M3 (24 cellules, L, B =
max(2L ; 0,10) ; tenu / fragile / audit), M4 (excès apparié ; max), placebo (24 cellules de M3 et max du bras M4 ; écart
> 0,05 → audit), cellule à 0 partout. Le script ne décide rien d'autre que ce que le texte gelé dit ; il imprime une table que
la note de lecture reprend telle quelle. Écrit **avant** la lecture des données réelles (R1) ; testé sur l'essai synthétique v5.

Usage : python -I -B lecture_mecanique_v1.py SORTIE.json TABLE.json [--alpha 0.05] > lecture.json
"""
import argparse
import json
import math
import sys

STATS = ("max", "somme_terminale", "somme_sequentielle", "page", "processus_e", "balayage")
TAUS = ("0.0", "0.5", "1.0", "2.0")
R0_TABLE = (0.0, 0.2, 0.5, 0.8)


def interpoler(table, cle, r0):
    xs = R0_TABLE
    ys = [table[f"r0={x}"][cle] for x in xs]
    if r0 <= xs[0]:
        return ys[0]
    if r0 >= xs[-1]:
        return ys[-1]
    for (x0, y0), (x1, y1) in zip(zip(xs, ys), zip(xs[1:], ys[1:])):
        if x0 <= r0 <= x1:
            return y0 + (y1 - y0) * (r0 - x0) / (x1 - x0)
    raise ValueError


def lire(sortie, table, alpha=0.05):
    r = sortie["resultats"]
    L = sortie["manifeste"]["niveau_conforme_L"]
    B = max(2 * L, 0.10)
    lec = {"L": L, "B": B, "alpha": alpha, "verdicts": {}, "quantites": {}}
    med = lambda bloc, cle: bloc[cle]["reelles"]["mediane"]
    ib = lambda bloc, cle: bloc[cle]["reelles"]["mediane_intervalle_95"]
    r0 = r["correlation_intra_episode_r0"]["reelles"]["mediane"]
    lec["quantites"]["r0_median_reelles"] = r0
    lec["quantites"]["r0_median_placebos"] = (r["correlation_intra_episode_r0"]["placebos"] or {}).get("mediane")

    # M1
    m1, m1b = med(r["tau=0.0"], "par_action:max"), ib(r["tau=0.0"], "par_action:max")
    lec["quantites"]["M1_par_action_tau0"] = {"mediane": m1, "intervalle": m1b}
    lec["verdicts"]["M1"] = ("confirmé" if m1 >= 0.06 and m1b[0] > 0.03 else "réfuté" if m1 <= 0.03 else "non concluant")
    suite = [med(r[f"tau={t}"], "par_action:max") for t in TAUS]
    lec["quantites"]["M1_bis_par_action_par_tau"] = suite
    lec["verdicts"]["M1_bis"] = ("décroissant" if all(a >= b for a, b in zip(suite, suite[1:])) else
                                 "croissant" if all(a <= b for a, b in zip(suite, suite[1:])) else "ni l'un ni l'autre")

    # M2 contrôle
    v2 = med(r["tau=2.0"], "ville:processus_e")
    lec["quantites"]["M2_ville_tau2"] = v2
    lec["verdicts"]["M2_controle"] = "attendu" if v2 >= 0.075 else "AUDIT (bogue)"
    # M2 bis
    d = r["ville_tau2_moins_tau0"]
    attendu = interpoler(table, "difference_mediane", r0)
    lec["quantites"]["M2_bis"] = {"mediane": d["mediane"], "intervalle": d["intervalle_95"], "table_au_r0": attendu}
    lec["verdicts"]["M2_bis"] = ("aucune réfutation (r₀ ≥ 0,5)" if r0 >= 0.5 else
                                 "conforme à la table" if abs(d["mediane"] - attendu) <= 0.05 else "hors table (rapporté)")
    # M2 ter : cinq issues ordonnées
    v0 = med(r["tau=0.0"], "ville:processus_e")
    vm = med(r["melange_actions_permutees_tau=0"], "ville:processus_e")
    vmp = med(r["melange_pas_fixe_tau=0"], "ville:processus_e")
    dm = r["ville_tau0_reelles_moins_melange"]
    dmp = r["ville_tau0_reelles_moins_melange_pas_fixe"]
    lec["quantites"]["M2_ter"] = {"ville_tau0_reelles": v0, "ville_melange": vm, "ville_melange_pas_fixe": vmp,
                                  "diff_reelles_moins_melange": dm, "diff_reelles_moins_melange_pas_fixe": dmp,
                                  "table_ville_tau0_au_r0": interpoler(table, "ville_tau0_median", r0)}
    if v0 <= 0.05:
        issue = "(1) Ville tenue sur P3 à τ = 0"
    elif dm["intervalle_95"][0] <= 0:
        issue = "(2) marges seules"
    elif vm > alpha:
        issue = "(3) marges et dépendance"
    elif dmp["intervalle_95"][0] > 0:
        issue = "(4) dépendance naturelle suffisante"
    else:
        issue = "(5) structure intra-épisode avec dérive de pas"
    lec["verdicts"]["M2_ter"] = issue

    # M3 : 24 cellules
    cellules = {}
    pire = None
    for t in TAUS:
        for s in STATS:
            m = med(r[f"tau={t}"], f"conforme:{s}")
            cellules[f"tau={t}:{s}"] = m
            if pire is None or m > pire[1]:
                pire = (f"tau={t}:{s}", m)
    fragiles = {c: m for c, m in cellules.items() if (1.6 * L < m <= B) or m < 0.4 * L}
    audit = {c: m for c, m in cellules.items() if m > B}
    lec["quantites"]["M3_24_cellules"] = cellules
    lec["quantites"]["M3_pire"] = pire
    lec["verdicts"]["M3"] = ("AUDIT R4 — rien d'autre n'est lu" if audit else
                             f"tenu, fragile sur {len(fragiles)} cellule(s) (rapporté, la lecture continue)" if fragiles else "tenu")
    lec["quantites"]["M3_fragiles"] = fragiles
    lec["quantites"]["M3_audit"] = audit
    # M4
    ex = r["M4_exces_apparie"]
    mx = med(r["M4_dependance_seule_variance_constante_tau=2"], "conforme:max")
    lec["quantites"]["M4"] = {"exces": ex["exces"], "intervalle": ex["intervalle_95"], "quantite": r["M4_quantite"]["mediane"],
                              "quantite_tau0": ex["quantite_tau0"], "max_conforme": mx,
                              "table_exces_au_r0": interpoler(table, "M4_exces_median", r0)}
    if mx > 0.10:
        v4 = "AUDIT (maximum conforme > 0,10)"
    elif r0 >= 0.5:
        v4 = "non lisible à τ = 2 (r₀ ≥ 0,5), rapporté"
    elif ex["exces"] > 0.02 and ex["intervalle_95"][0] > 0 and mx <= 0.08:
        v4 = "confirmé"
    elif ex["exces"] <= 0:
        v4 = "réfuté"
    else:
        v4 = "non concluant"
    lec["verdicts"]["M4"] = v4
    # placebo : 24 cellules de M3 et max du bras M4
    ecarts = {}
    for t in TAUS:
        for s in STATS:
            b = r[f"tau={t}"][f"conforme:{s}"]
            if b.get("placebos"):
                ecarts[f"tau={t}:{s}"] = b["reelles"]["mediane"] - b["placebos"]["mediane"]
    b = r["M4_dependance_seule_variance_constante_tau=2"]["conforme:max"]
    if b.get("placebos"):
        ecarts["M4:max"] = b["reelles"]["mediane"] - b["placebos"]["mediane"]
    gros = {c: e for c, e in ecarts.items() if abs(e) > 0.05}
    lec["quantites"]["placebo_ecarts"] = ecarts
    lec["verdicts"]["placebo"] = f"AUDIT R4 sur {sorted(gros)}" if gros else "mêmes médianes (aucun écart > 0,05)"
    # cellule conforme à 0 partout
    zeros = [c for c, m in cellules.items() if m == 0.0 and r[f"tau={c.split(':')[0].split('=')[1]}"][f"conforme:{c.split(':')[1]}"]["reelles"]["q3"] == 0.0]
    lec["verdicts"]["cellule_a_zero"] = f"trop propre : {zeros}" if zeros else "aucune"
    # ligne de lecture gelée
    if "AUDIT" in lec["verdicts"]["M3"] or "AUDIT" in lec["verdicts"]["M2_controle"]:
        ligne = "audit avant toute lecture"
    elif lec["verdicts"]["M1"] == "confirmé" and v4 == "confirmé":
        ligne = "première ligne : la synthèse a raison (comparateur par épisode entier ; sommes sans niveau sous dépendance non vue, maximum tenu) — proposé à Lazar pour G1 et H2"
    elif lec["verdicts"]["M1"] == "confirmé" and v4 in ("non concluant", "réfuté"):
        ligne = "pas de dépassement établi des sommes sous dépendance non vue (τ = 2, 5 à 10 actions) ; rapporté avec r₀"
    elif v4.startswith("non lisible"):
        ligne = "M4 non lisible (r₀ ≥ 0,5) ; M2 ter porte le résultat"
    else:
        ligne = f"M1 {lec['verdicts']['M1']} ; voir les lignes des critères"
    lec["ligne_de_lecture"] = ligne
    return lec


def main():
    a = argparse.ArgumentParser()
    a.add_argument("sortie")
    a.add_argument("table")
    a.add_argument("--alpha", type=float, default=0.05)
    args = a.parse_args()
    with open(args.sortie, encoding="utf-8") as f:
        sortie = json.load(f)
    with open(args.table, encoding="utf-8") as f:
        table = json.load(f)["table"]
    lec = lire(sortie, table, args.alpha)
    lec["sources"] = {"sortie": args.sortie, "table": args.table, "script_sortie": sortie["manifeste"].get("script"),
                      "commit_sortie": sortie["manifeste"].get("commit"), "synthetique": sortie["manifeste"].get("synthetique")}
    json.dump(lec, sys.stdout, ensure_ascii=False, indent=1, allow_nan=False)
    print()


if __name__ == "__main__":
    main()
