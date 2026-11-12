"""Extrait les grandeurs de la section 6 de la lecture relue (aucun calcul neuf sauf comptes de tentatives perdues)."""
import json, sys
L = json.load(open(sys.argv[1], encoding="utf-8"))["lecture_relue"]
for w, x in L["mondes"].items():
    print("=====", w, "issue:", x["issue"], "| suspendue:", x["issue_suspendue_par_audit"], "| bras_perdu:", x["bras_perdu"],
          "| jouées min:", x["unites_jouees_min_par_case"], "| eps:", x["eps_resistance"])
    for k in ("v8|retour|n=16|ensemble", "v7|retour|n=16|ensemble", "v8|temoin|n=16|ensemble", "v7|temoin|n=16|ensemble",
              "v7|temoin|n=1|ensemble", "v8|retour|n=1|ensemble", "v7|retour|n=1|ensemble", "v8|retour|n=4|ensemble", "v8|temoin|n=4|ensemble"):
        t = x["taux"][k]; print(f"  {k}: {t['promues']}/{t['unites']} (non jouées {t['non_jouees']}) taux {t['taux']} Wilson {t['wilson_95']}")
    print("  brèche", x["breche"], "dents", x["dents"], "résiste", x["resiste"], "qualif", x["qualification_breche"])
    print("  instrument", {k: x["instrument_v8_retour"][k] for k in ("suites_jouees", "part_echos_exacts", "part_lois_distinctes", "part_hors_classe", "lois_jugees", "tentatives_echouees_par_cause", "invalides")})
    for c, v in x["cases"].items():
        if c.endswith("|ensemble"):
            print("  case", c, {k: v[k] for k in ("prevues", "jouees", "non_jouees", "tentatives_echouees_dans_les_jouees", "attentes_relais", "regles_de_lecture")})
    print("  A9", x["audit_A9"]); print("  audits", x["audits"]); print("  prédictions", x["predictions"])
    print("  paires", {k: v for k, v in x["ecarts_goodhart_par_carte"].items() if k.endswith("16")})
    print("  évaluations impossibles", x["evaluations_impossibles"], "budget dépassé", x["appels_budget_depasse"], "repli", x["unites_sous_repli"])
print("A9 déclenché sur", L["audit_A9_declenche_sur"])
