"""Rédaction **mécanique** de la note de lecture de la mesure unanime à partir de la lecture mécanique (`lecture_mecanique_v4.py`) — version 2 : E lu au manifeste (`E`), audits listés
et de la sortie réelle : la note reprend la table des verdicts telle quelle, les quantités citées, les réserves du script,
la provenance (empreintes, commit) — aucune phrase d'interprétation n'y est ajoutée par ce script ; l'auteur ajoute ensuite,
à la main et sous le titre « Réserves de l'auteur », ce que la lecture ne dit pas. Écrit avant toute lecture réelle (R1).

Usage : python -I -B rediger_note_lecture_v2.py LECTURE.json SORTIE.json --prereg FICHIER --commit SHA --heure HH:MM:SS > note.md
"""
import argparse
import hashlib
import json


def f3(x):
    return "—" if x is None else f"{x:.3f}".replace(".", ",")


def emp(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def main():
    a = argparse.ArgumentParser()
    a.add_argument("lecture")
    a.add_argument("sortie")
    a.add_argument("--prereg", required=True)
    a.add_argument("--commit", required=True)
    a.add_argument("--heure", required=True, help="heure UTC relevée par `date -u` dans un appel séparé")
    a.add_argument("--table", default=None)
    args = a.parse_args()
    lec = json.load(open(args.lecture, encoding="utf-8"))
    sortie = json.load(open(args.sortie, encoding="utf-8"))
    m, q, v = sortie["manifeste"], lec["quantites"], lec["verdicts"]
    L = lec["L"]
    out = []
    out.append("# Mesure unanime — note de lecture v1 : fausses alertes par épisode honnête entier de l'agrégateur séquentiel, sans puis avec corrélation injectée (scores de P3)\n")
    out.append(f"Lignée conv-audit (instance du 27 octobre 2026 ; servie par Fable 5.1), écrite après le relevé `date -u` de {args.heure} UTC le 28 octobre. "
               f"Préenregistrement **scellé** : `{args.prereg}` (`{emp(args.prereg)}`), commit du scellement `{args.commit}`. Sortie réelle : `{args.sortie}` "
               f"(`{emp(args.sortie)}`), script `{m.get('script')}` (`{m.get('empreinte_script')}`), données `{m.get('donnees')}` (`{m.get('empreinte_donnees')}`), "
               f"commit du manifeste `{m.get('commit')}`. Lecture mécanique : `{args.lecture}` (`{emp(args.lecture)}`)"
               + (f" ; table `{args.table}` (`{emp(args.table)}`)" if args.table else "") + ". **Une seule exécution réelle** (R1).\n")
    out.append("## Verdict (ligne de lecture gelée, appliquée mécaniquement)\n")
    out.append(f"**{lec['ligne_de_lecture']}**\n")
    if lec.get("audits"):
        out.append(f"Audits déclenchés : {', '.join(lec['audits'])} — rien d'autre n'est lu ; les verdicts ci-dessous sont **rapportés sans être lus**.\n")
    out.append("## Les verdicts, énoncé par énoncé (seuils gelés du préenregistrement)\n")
    out.append("| énoncé | verdict | quantités |")
    out.append("|---|---|---|")
    m1 = q["M1_par_action_tau0"]
    out.append(f"| M1 (seuil par action, τ = 0) | {v['M1']} | médiane {f3(m1['mediane'])}, intervalle [{f3(m1['intervalle'][0])} ; {f3(m1['intervalle'][1])}] |")
    out.append(f"| M1 bis (par action, de τ = 0 à τ = 2) | {v['M1_bis']} | {', '.join(f3(x) for x in q['M1_bis_par_action_par_tau'])} |")
    out.append(f"| M2 (contrôle, Ville à τ = 2) | {v['M2_controle']} | médiane {f3(q['M2_ville_tau2'])} |")
    b = q["M2_bis"]
    out.append(f"| M2 bis (Ville τ = 2 moins τ = 0) | {v['M2_bis']} | {f3(b['mediane'])} [{f3(b['intervalle'][0])} ; {f3(b['intervalle'][1])}] ; table au r₀ médian : {f3(b['table_au_r0'])} |")
    t = q["M2_ter"]
    out.append(f"| M2 ter (la lecture sur P3) | {v['M2_ter']} | Ville τ = 0 réelles {f3(t['ville_tau0_reelles'])} (table au r₀ : {f3(t['table_ville_tau0_au_r0'])}) ; mélange {f3(t['ville_melange'])} ; mélange à pas fixé {f3(t['ville_melange_pas_fixe'])} ; "
               f"D {f3(t['diff_reelles_moins_melange']['mediane'])} [{f3(t['diff_reelles_moins_melange']['intervalle_95'][0])} ; {f3(t['diff_reelles_moins_melange']['intervalle_95'][1])}] ; "
               f"D′ {f3(t['diff_reelles_moins_melange_pas_fixe']['mediane'])} [{f3(t['diff_reelles_moins_melange_pas_fixe']['intervalle_95'][0])} ; {f3(t['diff_reelles_moins_melange_pas_fixe']['intervalle_95'][1])}] ; "
               f"dérive mesurée {f3(t['derive_mesuree']['mediane'])} [{f3(t['derive_mesuree']['intervalle_95'][0])} ; {f3(t['derive_mesuree']['intervalle_95'][1])}] |")
    out.append(f"| M3 (24 cellules conformes, calibrage partagé) | {v['M3']} | L = {f3(L)}, B = {f3(lec['B'])} ; pire cellule {q['M3_pire'][0]} = {f3(q['M3_pire'][1])} ; fragiles : {len(q['M3_fragiles'])} ; audit : {len(q['M3_audit'])} |")
    m4 = q["M4"]
    out.append(f"| M4 (dépendance seule, excès apparié) | {v['M4']} | excès {f3(m4['exces'])} [{f3(m4['intervalle'][0])} ; {f3(m4['intervalle'][1])}] (différence des médianes {f3(m4.get('difference_des_medianes'))}) ; "
               f"quantité {f3(m4['quantite'])}, à τ = 0 {f3(m4['quantite_tau0'])} ; maximum conforme {f3(m4['max_conforme'])} ; table (excès au r₀) {f3(m4['table_exces_au_r0'])} |")
    out.append(f"| contrôle placebo | {v['placebo']} | écarts réelles − placebo sur les 24 cellules de M3 et le maximum de M4 : max |écart| = {f3(max(abs(e) for e in q['placebo_ecarts'].values()) if q['placebo_ecarts'] else None)} |")
    out.append(f"| cellule conforme à 0 | {v['cellule_a_zero']} | |")
    out.append("")
    out.append("## Corrélation intraclasse (rapportée, jamais une condition)\n")
    out.append(f"r₀ médian des sondes réelles : {f3(q['r0_median_reelles'])} ; placebo : {f3(q['r0_median_placebos'])} ; centré par pas : {f3(q.get('r0_median_centre_par_pas'))} ; "
               f"mélange à pas fixé : {f3(q.get('r0_melange_pas_fixe'))}.\n")
    out.append("## Réserves du script de lecture\n")
    out.append("\n".join(f"- {r}" for r in lec.get("reserves", [])) if lec.get("reserves") else "- aucune.")
    out.append("")
    out.append("## Les 24 cellules de M3 (médianes sur les sondes réelles)\n")
    out.append("| cellule | médiane |")
    out.append("|---|---|")
    for c, val in q["M3_24_cellules"].items():
        out.append(f"| {c} | {f3(val)} |")
    out.append("")
    out.append("## Manifeste\n")
    out.append(f"E = {m.get('E', m.get('gardes'))} ; K par pli = {m.get('K_par_pli')} ; L = {f3(L)} ; tirages {m.get('tirages')} ; rééchantillonnages {m.get('bootstrap')} ; "
               f"sondes réelles {m.get('sondes_reelles')}, placebo {m.get('sondes_placebo')} ; numpy {m.get('numpy')} ; python {m.get('python')} ; entropie {m.get('entropie')}.\n")
    out.append("## Réserves de l'auteur (à la main, après la lecture mécanique)\n")
    out.append("⟨À ÉCRIRE : ce que la lecture ne dit pas ; R4 si un résultat paraît trop propre ; aucune interprétation hors des critères gelés.⟩\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
