import json, pathlib, collections
N = pathlib.Path("/home/user/controle-ia-travail/docs/notes/echelle-conscience-eval")
rej = [json.loads(l) for l in (N / "v7/rejeu-bancs-cl5-cl6/rejeu-bancs-cl5-cl6-v7.jsonl").read_text().splitlines()]
bancs = {}
for p in list((N / "v6/contre-lecture-cl5/banc").glob("banc-cl5-lot*.jsonl")) + [x for x in (N / "v7/contre-lecture-cl6/banc").glob("banc-cl6-*.jsonl") if "rejeu" not in x.name]:
    for l in p.read_text().splitlines():
        d = json.loads(l); bancs[(p.name, d["scenario"], d["graine"])] = d
c = collections.Counter()
for r in rej:
    b = bancs[(r["banc"], r["scenario"], r["graine"])]
    t6 = b.get("issues_tenues")
    if t6 is not None and t6 != r["issues_tenues_v7"]:
        c[(r["banc"], json.dumps(t6, ensure_ascii=False)[:80], json.dumps(r["issues_tenues_v7"], ensure_ascii=False)[:90])] += 1
for k, v in c.items(): print(v, k)
