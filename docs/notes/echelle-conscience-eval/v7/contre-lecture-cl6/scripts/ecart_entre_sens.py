"""cl6 : règle candidate (exploration, non décisive) : écart du λ d'un même modèle entre les deux sens,
|λ_a→b(m) − λ_b→a(m)| sur les estimations ponctuelles, pour les analyses qui prononcent une issue (bancs de cl5 et cl6)."""
import collections, json, pathlib
SB = pathlib.Path("/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/contre-lecture-echelle-v7")
D = pathlib.Path("/home/user/controle-ia-travail/docs/notes/echelle-conscience-eval/v6/contre-lecture-cl5/banc")
lignes = []
for f in sorted(D.glob("banc-cl5-lot*.jsonl")) + sorted((SB / "banc").glob("banc-cl6-*.jsonl")):
    for l in f.read_text().splitlines():
        d = json.loads(l)
        if "lecture" in d:
            lignes.append((f.name, d))
NON_PRONONCE = ("non confirmé", "désaccord", "indécis", "non certifiable", "asymétrique")
par_scenario = collections.defaultdict(list)
for f, d in lignes:
    lec = d["lecture"]
    if any(x in lec for x in NON_PRONONCE):
        continue
    e8 = abs(d["lambda_ab_petit"] - d["lambda_ba_petit"]); e70 = abs(d["lambda_ab_grand"] - d["lambda_ba_grand"])
    par_scenario[(d["scenario"], lec)].append(round(max(e8, e70), 2))
for (sc, lec), v in sorted(par_scenario.items()):
    print(f"{sc:40s} {lec:35s} n={len(v):2d} écart max entre sens (par analyse) : {v}")
