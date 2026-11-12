"""Exporte les résultats structurés d'une vérification par sous-agents (journal du workflow) : un JSON brut et un
rapport Markdown lisible (rapports et contre-vérifications, tels que rendus). Usage : exporter_verification.py JOURNAL
TITRE SORTIE_JSON SORTIE_MD"""
import json, sys
journal, titre, sj, sm = sys.argv[1:5]
labels, res = {}, []
for l in open(journal, encoding="utf-8"):
    d = json.loads(l)
    if d.get("type") == "started":
        labels[d["agentId"]] = d.get("label", "")
    elif d.get("type") == "result":
        res.append({"agent": d.get("agentId"), "role": labels.get(d.get("agentId"), ""), "resultat": d.get("result")})
json.dump({"titre": titre, "resultats": res}, open(sj, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
o = [f"# {titre}", "", "Export brut des rapports des sous-agents neufs (texte rendu par chacun, non retouché).", ""]
for r in res:
    x = r["resultat"]
    o.append(f"## {r['role']}")
    if isinstance(x, dict) and "verdict" in x:
        o += [f"Verdict : {x['verdict']}", ""]
        for m in x["remarques"]:
            o += [f"### {m['id']} ({m['gravite']})", "", f"Constat : {m['constat']}", "", f"Preuve : {m['preuve']}", "",
                  f"Correction proposée : {m['correction']}", ""]
        o += ["Vérifié :", ""] + [f"- {v}" for v in x["verifie"]] + ["", "Non vérifié :", ""] + [f"- {v}" for v in x["non_verifie"]] + [""]
    elif isinstance(x, dict) and "issue" in x:
        o += [f"Issue : {x['issue']} ; gravité jugée : {x['gravite_juste']}", "", f"Raisons : {x['raisons']}", "", f"Preuve : {x['preuve']}", ""]
    else:
        o += [str(x), ""]
open(sm, "w", encoding="utf-8").write("\n".join(o) + "\n")
print(len(res), "résultats exportés")
