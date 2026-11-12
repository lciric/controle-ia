"""cl5 : résume un banc (lecture, réserves, issues tenues par sens, λ et Δλ) et, si fourni, compare aux lignes du banc
de cl4 (analyse v4) aux mêmes graines."""
import collections, glob, json, sys
lignes = [json.loads(l) for f in sys.argv[1].split(",") for l in open(f, encoding="utf-8")]
cl4 = {}
if len(sys.argv) > 2:
    for f in glob.glob(sys.argv[2]):
        for l in open(f, encoding="utf-8"):
            d = json.loads(l); cl4[(d["scenario"], d["graine"])] = d
par = collections.OrderedDict()
for d in lignes:
    par.setdefault(d["scenario"], []).append(d)
for nom, ls in par.items():
    c = collections.Counter(d.get("lecture", f"arrêt {d.get('code')}") + (f" ({len(d['reserves'])} réserve(s))" if d.get("reserves") else "") for d in ls)
    print(f"== {nom} ({len(ls)} analyses) : {dict(c)}")
    for d in ls:
        if "lecture" not in d:
            print(f"   {d['graine']} | arrêt code {d.get('code')}"); continue
        v4 = cl4.get((nom, d["graine"]))
        comp = f" | cl4 (v4) : {v4['lecture']}" if v4 else ""
        print(f"   {d['graine']} | {d['lecture']} | réserves {d['reserves']} | tenues a→b {d['issues_tenues']['a→b']}, b→a {d['issues_tenues']['b→a']}"
              f" | λ a→b petit {d['lambda_ab_petit_ic']} grand {d['lambda_ab_grand_ic']} ; b→a petit {d['lambda_ba_petit_ic']} grand {d['lambda_ba_grand_ic']}"
              f" | Δλ a→b {d['dl_ab_ic']} b→a {d['dl_ba_ic']} | −λ−ν a→b p {d['ssi_ab_petit_ic']} g {d['ssi_ab_grand_ic']} ; b→a p {d['ssi_ba_petit_ic']} g {d['ssi_ba_grand_ic']}"
              f" | certif. bas a→b {d['Afixe_ab_petit_bas']}/{d['Afixe_ab_grand_bas']} b→a {d['Afixe_ba_petit_bas']}/{d['Afixe_ba_grand_bas']}{comp}")
