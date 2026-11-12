"""cl5 : lectures v4 (bancs de cl4) contre lectures v5 (rejeux cl5), mêmes scénarios et mêmes graines ; intervalles
comparés pour s'assurer que les activations et le calcul sont les mêmes (seule la lecture change)."""
import collections, glob, json, sys
v4 = {}
for f in glob.glob("/home/user/controle-ia-travail/docs/notes/echelle-conscience-eval/v5/contre-lecture-cl4/banc/banc-lot*.jsonl"):
    for l in open(f, encoding="utf-8"):
        d = json.loads(l); v4[(d["scenario"], d["graine"])] = d
changes, memes, ecarts_ic, n = collections.Counter(), 0, 0, 0
for f in sys.argv[1:]:
    for l in open(f, encoding="utf-8"):
        d = json.loads(l)
        a = v4.get((d["scenario"], d["graine"]))
        if a is None:
            continue
        n += 1
        for k in ("lambda_ab_petit_ic", "lambda_ab_grand_ic", "lambda_ba_petit_ic", "lambda_ba_grand_ic", "dl_ab_ic", "dl_ba_ic", "spec_ab_ic", "spec_ba_ic"):
            if a[k] != d[k]:
                ecarts_ic += 1
        lv4 = a["lecture"] + (f" [{len(a['reserves'])} réserve(s)]" if a["reserves"] else "")
        lv5 = d["lecture"] + (f" [{' ; '.join(d['reserves'])}]" if d["reserves"] else "")
        if a["lecture"] == d["lecture"] and a["reserves"] == d["reserves"]:
            memes += 1
        else:
            changes[(d["scenario"], lv4, lv5)] += 1
print(f"analyses comparées : {n} ; intervalles différents : {ecarts_ic} ; lectures et réserves identiques : {memes}")
for (s, a, b), k in sorted(changes.items()):
    print(f"  {s} : v4 « {a} » → v5 « {b} » ({k})")
