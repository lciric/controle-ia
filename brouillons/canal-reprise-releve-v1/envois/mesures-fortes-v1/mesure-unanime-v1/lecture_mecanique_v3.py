"""Lecture **mécanique** de la sortie réelle de la mesure unanime selon les seuils gelés du préenregistrement v7 (section
« Seuil » et table des prédictions) : M1, M2 (contrôle), M2 bis, M2 ter (arbre à neuf feuilles, CV5-3, CV6-2), M3 (24 cellules, L, B =
max(2L ; 0,10) ; tenu / fragile / audit), M4 (excès apparié ; max), placebo (24 cellules de M3 et max du bras M4 ; écart
> 0,05 → audit), cellule à 0 partout ; r₀ brut et centré par pas rapportés (CV5-4, réserve si écart). Le script ne décide
rien d'autre que ce que le texte gelé dit ; il imprime une table que la note de lecture reprend telle quelle. Écrit **avant**
la lecture des données réelles (R1) ; testé sur l'essai synthétique v7. Version 3 (CV6-1 à CV6-6) : **tout audit** (M3, M2
contrôle, maximum du bras M4, placebo) **suspend la lecture** ; la feuille (4c) ne dit « dérive de pas » que si la dérive est
**mesurée** (borne basse de Ville mélange à pas fixé moins Ville mélange > 0), sinon « structure intra-épisode non
attribuée » ; comparaisons arrondies à 10⁻⁹ ; manifeste vérifié (script, empreinte des données attendue, E de la table = E
de la sortie) ; cellule « à zéro » = médiane et troisième quartile nuls ; M2 bis : « hors table » rapporté même pour r₀ ≥ 0,5.

Usage : python -I -B lecture_mecanique_v3.py SORTIE.json TABLE.json [--alpha 0.05] [--empreinte-donnees …] > lecture.json
"""
import argparse
import json
import math
import sys

STATS = ("max", "somme_terminale", "somme_sequentielle", "page", "processus_e", "balayage")
TAUS = ("0.0", "0.5", "1.0", "2.0")
R0_TABLE = (0.0, 0.2, 0.5, 0.8)


def arr(x):
    """CV6-4 : arrondi à 10⁻⁹ avant toute comparaison à une borne exacte."""
    return round(float(x), 9)


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


def lire(sortie, table, alpha=0.05, empreinte_donnees=None, table_manifeste=None):
    r = sortie["resultats"]
    L = arr(sortie["manifeste"]["niveau_conforme_L"])
    B = arr(max(2 * L, 0.10))
    lec = {"L": L, "B": B, "alpha": alpha, "verdicts": {}, "quantites": {}, "manifeste_verifie": {}}
    m = sortie["manifeste"]
    lec["manifeste_verifie"]["script"] = m.get("script")
    if m.get("script") != "analyse_fausses_alertes_v7.py":
        raise SystemExit(f"sortie d'un autre script que la v7 : {m.get('script')}")
    if empreinte_donnees is not None and m.get("empreinte_donnees") != empreinte_donnees:
        raise SystemExit("empreinte des données de la sortie ≠ celle attendue")
    if table_manifeste is not None and int(table_manifeste.get("E", -1)) != int(m.get("E", -2)):
        raise SystemExit(f"E de la table ({table_manifeste.get('E')}) ≠ E de la sortie ({m.get('E')})")
    lec["manifeste_verifie"]["empreinte_donnees"] = m.get("empreinte_donnees")
    lec["manifeste_verifie"]["E"] = m.get("E")
    med = lambda bloc, cle: bloc[cle]["reelles"]["mediane"]
    ib = lambda bloc, cle: bloc[cle]["reelles"]["mediane_intervalle_95"]
    r0 = r["correlation_intra_episode_r0"]["reelles"]["mediane"]
    lec["quantites"]["r0_median_reelles"] = r0
    lec["quantites"]["r0_median_placebos"] = (r["correlation_intra_episode_r0"]["placebos"] or {}).get("mediane")
    r0c = (r["correlation_intra_episode_r0"].get("centre_par_pas_reelles") or {}).get("mediane")
    lec["quantites"]["r0_median_centre_par_pas"] = r0c
    lec["quantites"]["r0_melange_pas_fixe"] = (r["correlation_intra_episode_r0"].get("melange_pas_fixe_reelles") or {}).get("mediane")
    lec["reserves"] = []
    if r0c is not None and arr(abs(r0c - r0)) > 0.05:
        lec["reserves"].append(f"r₀ brut {r0:.3f} et centré par pas {r0c:.3f} s'écartent de plus de 0,05 : une dérive avec le pas pèse sur r₀ ; "
                               "les lectures conditionnelles au r₀ médian (M4, M2 bis) sont à lire avec cette réserve (CV5-4)")

    # M1
    m1, m1b = med(r["tau=0.0"], "par_action:max"), ib(r["tau=0.0"], "par_action:max")
    lec["quantites"]["M1_par_action_tau0"] = {"mediane": m1, "intervalle": m1b}
    lec["verdicts"]["M1"] = ("confirmé" if arr(m1) >= 0.06 and arr(m1b[0]) > 0.03 else "réfuté" if arr(m1) <= 0.03 else "non concluant")
    suite = [med(r[f"tau={t}"], "par_action:max") for t in TAUS]
    lec["quantites"]["M1_bis_par_action_par_tau"] = suite
    lec["verdicts"]["M1_bis"] = ("décroissant" if all(a >= b for a, b in zip(suite, suite[1:])) else
                                 "croissant" if all(a <= b for a, b in zip(suite, suite[1:])) else "ni l'un ni l'autre")

    # M2 contrôle
    v2 = med(r["tau=2.0"], "ville:processus_e")
    lec["quantites"]["M2_ville_tau2"] = v2
    lec["verdicts"]["M2_controle"] = "attendu" if arr(v2) >= 0.075 else "AUDIT (bogue : médiane de Ville à τ = 2 < 0,075)"
    # M2 bis
    d = r["ville_tau2_moins_tau0"]
    attendu = interpoler(table, "difference_mediane", r0)
    lec["quantites"]["M2_bis"] = {"mediane": d["mediane"], "intervalle": d["intervalle_95"], "table_au_r0": attendu}
    conforme = "conforme à la table" if arr(abs(d["mediane"] - attendu)) <= 0.05 else "hors table (rapporté)"
    lec["verdicts"]["M2_bis"] = conforme + (" ; aucune réfutation (r₀ ≥ 0,5)" if arr(r0) >= 0.5 else "")
    # M2 ter : cinq issues ordonnées
    v0 = med(r["tau=0.0"], "ville:processus_e")
    vm = med(r["melange_actions_permutees_tau=0"], "ville:processus_e")
    vmp = med(r["melange_pas_fixe_tau=0"], "ville:processus_e")
    dm = r["ville_tau0_reelles_moins_melange"]
    dmp = r["ville_tau0_reelles_moins_melange_pas_fixe"]
    dd = r["ville_tau0_melange_pas_fixe_moins_melange"]  # CV6-2 : dérive mesurée
    lec["quantites"]["M2_ter"] = {"ville_tau0_reelles": v0, "ville_melange": vm, "ville_melange_pas_fixe": vmp,
                                  "diff_reelles_moins_melange": dm, "diff_reelles_moins_melange_pas_fixe": dmp, "derive_mesuree": dd,
                                  "table_ville_tau0_au_r0": interpoler(table, "ville_tau0_median", r0)}
    bbD, bbDp, bbDd = arr(dm["intervalle_95"][0]), arr(dmp["intervalle_95"][0]), arr(dd["intervalle_95"][0])
    v0, vm, vmp = arr(v0), arr(vm), arr(vmp)
    if v0 <= 0.05:
        issue = "(1) Ville tenue sur P3 à τ = 0"
    elif bbD <= 0:
        issue = "(2a) marges seules" if vm > alpha else "(2b) non attribuable"
    elif vm > alpha:
        issue = "(3a) marges et dépendance" if bbDp > 0 else "(3b) marges et structure intra-épisode"
    elif bbDp > 0:
        issue = "(4a) dépendance naturelle suffisante" if vmp <= alpha else "(4b) dérive et dépendance"
    else:
        issue = "(4c) structure intra-épisode avec dérive de pas mesurée" if bbDd > 0 else "(4d) structure intra-épisode non attribuée"
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
    fragiles = {c: m for c, m in cellules.items() if (arr(1.6 * L) < arr(m) <= B) or arr(m) < arr(0.4 * L)}
    audit = {c: m for c, m in cellules.items() if arr(m) > B}
    lec["quantites"]["M3_24_cellules"] = cellules
    lec["quantites"]["M3_pire"] = pire
    lec["verdicts"]["M3"] = ("AUDIT R4 — rien d'autre n'est lu" if audit else
                             f"tenu, fragile sur {len(fragiles)} cellule(s) (rapporté, la lecture continue)" if fragiles else "tenu")
    lec["quantites"]["M3_fragiles"] = fragiles
    lec["quantites"]["M3_audit"] = audit
    # M4
    ex = r["M4_exces_apparie"]
    mx = med(r["M4_dependance_seule_variance_constante_tau=2"], "conforme:max")
    lec["quantites"]["M4"] = {"exces": ex["exces"], "difference_des_medianes": ex.get("difference_des_medianes"),
                              "intervalle": ex["intervalle_95"], "quantite": r["M4_quantite"]["mediane"],
                              "quantite_tau0": ex["quantite_tau0"], "max_conforme": mx,
                              "table_exces_au_r0": interpoler(table, "M4_exces_median", r0)}
    if arr(mx) > 0.10:
        v4 = "AUDIT (maximum conforme > 0,10)"
    elif arr(r0) >= 0.5:
        v4 = "non lisible à τ = 2 (r₀ ≥ 0,5), rapporté"
    elif arr(ex["exces"]) > 0.02 and arr(ex["intervalle_95"][0]) > 0 and arr(mx) <= 0.08:
        v4 = "confirmé"
    elif arr(ex["exces"]) <= 0:
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
    gros = {c: e for c, e in ecarts.items() if arr(abs(e)) > 0.05}
    lec["quantites"]["placebo_ecarts"] = ecarts
    lec["verdicts"]["placebo"] = f"AUDIT R4 sur {sorted(gros)}" if gros else "mêmes médianes (aucun écart > 0,05)"
    # cellule conforme à 0 partout
    zeros = [c for c, m in cellules.items() if arr(m) == 0.0 and arr(r[f"tau={c.split(':')[0].split('=')[1]}"][f"conforme:{c.split(':')[1]}"]["reelles"]["q3"]) == 0.0]
    lec["verdicts"]["cellule_a_zero"] = f"trop propre (médiane et troisième quartile nuls) : {zeros}" if zeros else "aucune"
    # ligne de lecture gelée
    audits = [k for k in ("M3", "M2_controle", "M4", "placebo") if "AUDIT" in lec["verdicts"][k]]
    lec["audits"] = audits
    if audits:
        ligne = f"AUDIT R4 avant toute lecture ({', '.join(audits)}) : rien d'autre n'est lu ; les verdicts ci-dessus sont rapportés sans être lus"
    elif lec["verdicts"]["M1"] == "confirmé" and v4 == "confirmé":
        ligne = "première ligne : la synthèse a raison (comparateur par épisode entier ; sommes sans niveau sous dépendance non vue, maximum tenu) — proposé à Lazar pour G1 et H2"
    elif lec["verdicts"]["M1"] == "confirmé" and v4 in ("non concluant", "réfuté"):
        ligne = "pas de dépassement établi des sommes sous dépendance non vue (τ = 2, 5 à 10 actions) ; rapporté avec r₀"
    elif v4.startswith("non lisible"):
        ligne = "M4 non lisible (r₀ ≥ 0,5) ; M2 ter porte le résultat"
    else:
        ligne = f"M1 {lec['verdicts']['M1']} ; voir les lignes des critères"
    if lec["reserves"]:
        ligne += " — RÉSERVE : " + " ; ".join(lec["reserves"])
    lec["ligne_de_lecture"] = ligne
    return lec


def main():
    a = argparse.ArgumentParser()
    a.add_argument("sortie")
    a.add_argument("table")
    a.add_argument("--alpha", type=float, default=0.05)
    a.add_argument("--empreinte-donnees", default=None, help="empreinte attendue des données, comparée au manifeste de la sortie")
    args = a.parse_args()
    with open(args.sortie, encoding="utf-8") as f:
        sortie = json.load(f)
    with open(args.table, encoding="utf-8") as f:
        table = json.load(f)["table"]
    with open(args.table, encoding="utf-8") as f:
        table_manifeste = json.load(f).get("manifeste", {})
    lec = lire(sortie, table, args.alpha, args.empreinte_donnees, table_manifeste)
    lec["sources"] = {"sortie": args.sortie, "table": args.table, "script_sortie": sortie["manifeste"].get("script"),
                      "commit_sortie": sortie["manifeste"].get("commit"), "synthetique": sortie["manifeste"].get("synthetique")}
    json.dump(lec, sys.stdout, ensure_ascii=False, indent=1, allow_nan=False)
    print()


if __name__ == "__main__":
    main()
