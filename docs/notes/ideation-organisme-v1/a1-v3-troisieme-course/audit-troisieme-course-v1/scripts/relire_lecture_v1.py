"""Relecture indépendante (verdict R13, fille 9) : rejoue la lecture gelée `pole.attaque_goodhart_v3.lire` du code cité
(73 empreintes vérifiées) sur les suites, rejeux et audits de la trace scellée, et compare à la lecture écrite par la course.
Usage : python -I relire_lecture_v1.py <racine_code_orchestrator> <attaque-goodhart-v3.json> <manifeste.json> <sortie.json>"""
import json, sys
racine, trace, manif, sortie = sys.argv[1:5]
sys.path.insert(0, racine)
from pole import attaque_goodhart_v3 as a3  # noqa: E402
o = json.load(open(trace, encoding="utf-8"))
m = json.load(open(manif, encoding="utf-8"))
p = m["reglages"]["plan"]
ent = int(m["reglages"]["entropie_racine"])
lec = a3.lire(o["suites"], o["rejeux"], o["audit_A2"], p["mondes"], p["unites_par_case"], ent, p["fournisseurs"])
lec = json.loads(json.dumps(lec, ensure_ascii=False))
egal = lec == o["lecture"]
diff = []
if not egal:
    for w in lec["mondes"]:
        for k in lec["mondes"][w]:
            if lec["mondes"][w][k] != o["lecture"]["mondes"][w].get(k):
                diff.append(f"{w}.{k}")
json.dump({"lecture_relue_egale_a_la_lecture_ecrite": egal, "cles_differentes": diff, "lecture_relue": lec}, open(sortie, "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("égale :", egal, diff[:20])
