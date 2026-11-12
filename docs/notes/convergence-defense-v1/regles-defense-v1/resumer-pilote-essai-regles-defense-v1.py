#!/usr/bin/env python3
"""Résumé Markdown du pilote d'essai des règles de défense (lecture mécanique du JSON ; aucune lecture de résultat au
sens de R1 : racine d'essai, chiffres non opposables). Usage : python3 <ce fichier> PILOTE.json > PILOTE.md"""
import hashlib
import json
import sys
from pathlib import Path

p = Path(sys.argv[1])
c = json.loads(p.read_text(encoding="utf-8"))
man, an, temps, res = c["manifeste"], c["analyse"], c["temps"], c["resultats"]
cfg = man["config"]
N_DECISION = cfg["n_instances"]
noms = list(an["1"]["variantes"])
dec = ("R1", "R2", "R3")   # variantes de la décision : plus R4 à λ* (choix du gel § 3)
choix = an["choix_lambda"]
dec_r4 = choix["retenu"]
L = []
w = L.append
w(f"# Pilote d'essai — quatre règles de mise à jour de la défense — v1 (racines d'essai {man['racine']} / "
  f"{man['racine_tenue']} ; À NE PAS LIRE COMME UN RÉSULTAT)")
w("")
w(f"- Fichier : `{p.name}` — sha256 `{hashlib.sha256(p.read_bytes()).hexdigest()}`")
w(f"- Code : `{man['versions']['code_sha256']}` ; arène v4 `{man['versions']['arene_v4_sha256']}` ; gel "
  f"`{man['gel_sha256']}` ; configuration `{man['config_sha256']}` ; numpy {man['versions']['numpy']}, scipy "
  f"{man['versions']['scipy']}, Python {man['versions']['python']}")
w(f"- Commande : `{man['commande']}`")
w(f"- Tâches : {temps['taches']} (instances × δ), T = {cfg['T']}, variantes : {', '.join(noms)} ; λ ∈ "
  f"{list(man['lambdas'])}, références {list(man['references'])} ; finale {'complète' if man['complete'] else 'légère'}.")
w("")
w("## 1. Temps et extrapolation")
w("")
cpu = temps["cpu_somme_taches_s"]
mur = temps["mur_s"]
eff = cpu / (mur * temps["processus"])
w(f"- Processeur, somme des tâches : {cpu:.0f} s ; mur : {mur:.0f} s sur {temps['processus']} processus ; efficacité "
  f"(processeur / (mur × processus)) : {eff:.2f}.")
par_t = [r["cpu_tache_s"] for r in res]
w(f"- Par tâche (13 variantes) : moyenne {sum(par_t) / len(par_t):.1f} s, min {min(par_t):.1f} s, max {max(par_t):.1f} s "
  f"(plafond interne 600 s).")
w("")
w("| Variante | processeur trajectoire (s, moyenne) | processeur finale (s) | appels optimiseur | programmes linéaires "
  "| entraînements | départs attaquant |")
w("|---|---|---|---|---|---|---|")
cout_var = {}
for n in noms:
    cs = [an[cd]["variantes"][n]["cout"] for cd in ("1", "2")]
    moy = {k: sum(x[k] for x in cs) / 2 for k in cs[0]}
    cout_var[n] = moy
    w(f"| {n} | {moy['cpu_trajectoire_s']:.2f} | {moy['cpu_final_s']:.2f} | {moy['appels_optimiseur']:.0f} | "
      f"{moy['programmes_lineaires']:.0f} | {moy['entrainements']:.0f} | {moy['departs_attaquant']:.0f} |")
w("")
cpu_dec = sum(cout_var[n]["cpu_trajectoire_s"] + cout_var[n]["cpu_final_s"] for n in dec + ((dec_r4,) if dec_r4 else ()))
cpu_grille = sum(cout_var[n]["cpu_trajectoire_s"] + cout_var[n]["cpu_final_s"] for n in noms)
surcout = (sum(par_t) / len(par_t)) - cpu_grille      # contexte, M0, tenues : par tâche, hors variantes
w(f"- Hors variantes (contexte, M0, lois tenues) : ≈ {surcout:.1f} s par tâche.")
w(f"- **Extrapolation à N = {N_DECISION} par δ ({2 * N_DECISION} tâches)** :")
for lib, par_tache in (("décision à 4 variantes (R1, R2, R3, R4 à λ*)", cpu_dec + surcout),
                       ("grille complète (13 variantes)", cpu_grille + surcout)):
    tot = par_tache * 2 * N_DECISION
    w(f"  - {lib} : {par_tache:.1f} s par tâche → {tot / 60:.0f} min de processeur ; mur sur 2 processus : "
      f"{tot / 120:.0f} min à efficacité 1, {tot / (120 * eff):.0f} min à l'efficacité mesurée {eff:.2f} ; sur 4 "
      f"processus à efficacité 1 : {tot / 240:.0f} min.")
w("")
w("## 2. Les mesures bougent-elles ? (moyennes sur 6 instances par δ ; bruit non opposable)")
w("")
for cd in ("1", "2"):
    b = an[cd]
    w(f"### δ = {b['delta']} (code {cd}, n = {b['n']})")
    w("")
    w("| Variante | V final (iii) | X = 1 − V | (ii) tenues final | (i) vus | fausses alertes | I1 | I3 − nul | "
      "cos consécutif | valeur jeu restreint | poids purs |")
    w("|---|---|---|---|---|---|---|---|---|---|---|")
    for n in noms:
        v = b["variantes"][n]
        cy = v["cycle"]
        i3 = "—" if cy["I3_moins_nul"] is None else f"{cy['I3_moins_nul']:+.3f}"
        vjr = f"{v['valeur_jeu_restreint_finale']:.3f}" if "valeur_jeu_restreint_finale" in v else "—"
        pur = f"{v['poids']['part_pure']:.2f}" if "poids" in v else "—"
        w(f"| {n} | {v['V_iii_final']:.4f} | {v['exploitabilite_finale']:.4f} | {v['ii_final']:.4f} | "
          f"{v['i_final_vus']:.4f} | {v['fpr_moyen']:.4f} | {cy['I1_progres']:+.4f} | {i3} | "
          f"{v['cos_consecutif_moyen']:.3f} | {vjr} | {pur} |")
    w("")
    w("(iii) par tour, moyenne :")
    w("")
    for n in noms:
        w(f"- {n} : " + ", ".join(f"{x:.3f}" for x in b["variantes"][n]["iii_par_tour"]))
    w("")
    w("(ii) par tour, moyenne :")
    w("")
    for n in noms:
        w(f"- {n} : " + ", ".join(f"{x:.3f}" for x in b["variantes"][n]["ii_par_tour"]))
    if "valeur_jeu_restreint_par_tour" in b["variantes"].get("R3", {}):
        w("")
        w("R3′ (valeur du jeu restreint par tour, les deux joueurs à l'équilibre) : " +
          ", ".join(f"{x:.3f}" for x in b["variantes"]["R3"]["valeur_jeu_restreint_par_tour"]))
    w("")
    w("Contrastes appariés contre R2 (moyenne [B2 = q0,00625 ; q0,99375], 20 000 rééchantillonnages, n = 6 : "
      "intervalles larges, non opposables) :")
    w("")
    w("| Contraste | V (iii) | (ii) |")
    w("|---|---|---|")
    for n in noms:
        if n == "R2":
            continue
        cv = b["contrastes_contre_R2"][f"{n} - R2 (V_iii_final)"]
        ci = b["contrastes_contre_R2"][f"{n} - R2 (ii_final)"]
        f = lambda c: f"{c['moyenne']:+.4f} [{c['quantiles']['q0.00625']:+.4f} ; {c['quantiles']['q0.99375']:+.4f}]"  # noqa
        w(f"| {n} − R2 | {f(cv)} | {f(ci)} |")
    w("")
    w(f"Contrôles : entraînements {b['entrainements']}, non convergés {b['non_convergences']} ; départs de l'attaquant "
      f"{b['attaquant']['departs']}, non finis {b['attaquant']['non_finis']}, réponses à la limite "
      f"{b['attaquant']['reponses_a_la_limite']} ; processeur par tâche moyenne {b['cpu_tache_s']['moyenne']:.1f} s, "
      f"max {b['cpu_tache_s']['max']:.1f} s.")
    w("")
w("## 3. Choix de λ* par la règle du gel (§ 3), sur les deux δ confondus")
w("")
w(f"- Règle : {choix['regle']} ; tolérance {choix['tolerance']}.")
w("- Moyenne de V(R4) par variante : " + " ; ".join(f"{k} {v:.4f}" for k, v in sorted(choix["par_variante"].items())))
w(f"- **Retenu : {choix['retenu']}** (λ = {choix['lam']}, référence « {choix['reference']} »). Cosinus consécutif moyen "
  f"de la variante retenue : " + ", ".join(f"{an[cd]['variantes'][choix['retenu']]['cos_consecutif_moyen']:.3f}"
                                           for cd in ("1", "2")) + " (δ 1 ; δ 2).")
w("")
w("## 4. Réserves de lecture")
w("")
w("- Racine d'essai, 6 instances par δ : rien ici n'est opposable ; aucune prédiction du préenregistrement n'en est tirée "
  "(seuls λ*, la référence et la projection de temps en viennent, par des règles écrites avant le pilote).")
w("- R4 à grand λ tend vers une défense figée (cosinus consécutif ≈ 1) : la règle de choix de λ* peut retenir cette "
  "extrémité ; point soumis au directeur dans le brouillon de préenregistrement.")
print("\n".join(L))
