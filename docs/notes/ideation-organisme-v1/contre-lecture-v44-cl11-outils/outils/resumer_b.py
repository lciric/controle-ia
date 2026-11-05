"""CL10 : résumé lisible des rapports B-* (une ligne par session d'Argon, issue, classement)."""
import json
import os
import sys
base = sys.argv[1]
for n in sorted(os.listdir(base)):
    if not n.startswith("B-") or not os.path.exists(os.path.join(base, n, "rapport.json")):
        continue
    r = json.load(open(os.path.join(base, n, "rapport.json")))
    lc = r.get("lanceur-course", {})
    print(f"== {n} : code course {lc.get('code')} ; Claude {r['claude']['cout']} ({r['claude']['appels']} appels) ; "
          f"Argon {r['argon_total']} ; total {r['total']} ; classements {r['classements']}")
    for a in r["argon_course"]:
        quoi = "contrôle" if a["controle"] else (f"passe {a['passe']}" if a["role"] == "proposeur_ideation" else a["role"])
        print(f"   course {quoi:<10} plafond {a['plafond']:<4} entrée {a['entree']:>9} sortie {a['sortie']:>7} coût {a['cout']:.4f}"
              + ("  > PLAFOND" if a["depasse_plafond"] else ""))
    if lc.get("code") != 0:
        print("   arrêt :", lc.get("erreur", "")[-400:].replace("\n", " "))
    fin = (r.get("course") or {}).get("fin")
    if fin:
        print("   fin :", {k: fin[k] for k in ("cout_total_usd", "cout_externe_usd", "arret")}, "gardes", fin["gardes_taille_sessions"])
    ctl = r.get("controle") or {}
    for f, v in ctl.items():
        if f.endswith(".json"):
            print("   contrôle", f, {k: v.get(k) for k in ("cout_claude_usd", "cout_externe_usd", "relancable")})
    b = r.get("bras")
    if b:
        for a in b["argon"]:
            print(f"   bras   {('contrôle' if a['controle'] else 'juge'):<10} plafond {a['plafond']:<4} entrée {a['entree']:>9} "
                  f"sortie {a['sortie']:>7} coût {a['cout']:.4f}" + ("  > PLAFOND" if a["depasse_plafond"] else ""))
        print("   bras code", b["code"], "fichiers", b["fichiers"], "journal", b.get("journal"), "garde", b.get("garde"))
        lb = r.get("bras-course", {})
        if b["code"] != 0:
            print("   bras arrêt :", lb.get("erreur", "")[-400:].replace("\n", " "))
