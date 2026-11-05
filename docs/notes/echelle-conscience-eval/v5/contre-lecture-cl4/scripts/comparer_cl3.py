"""Compare, graine par graine, les rejeux cl4 (analyse v4) aux lignes du banc de cl3 (analyse v3, mêmes activations)."""
import json, sys
CL3 = "/home/user/controle-ia-travail/docs/notes/echelle-conscience-eval/v4/contre-lecture-cl3/banc/banc.jsonl"
v3 = {}
for l in open(CL3, encoding="utf-8"):
    d = json.loads(l)
    v3[(d["scenario"], d["graine"])] = d
cles = [k for k in ("lambda_ab_petit_ic", "lambda_ab_grand_ic", "lambda_ba_petit_ic", "lambda_ba_grand_ic", "dl_ab_ic",
                    "dl_ba_ic", "spec_ab_ic", "spec_ba_ic", "Afixe_ab_petit_bas", "Afixe_ba_grand_bas")]
for f in sys.argv[1:]:
    for l in open(f, encoding="utf-8"):
        d = json.loads(l)
        k = (d["scenario"], d["graine"])
        if k not in v3:
            continue
        a = v3[k]
        egal = all(a.get(c) == d.get(c) for c in cles)
        print(f"{k[0]:24s} {k[1]} : v3 « {a['lecture']} » -> v4 « {d['lecture']} » ; par sens {d['lecture_par_sens']} ; "
              f"intervalles identiques à cl3 : {egal}")
