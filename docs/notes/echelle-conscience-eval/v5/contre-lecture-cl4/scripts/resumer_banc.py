"""Résume les lignes du banc cl4 : lecture, réserves, lectures par sens, issues dont toutes les conditions tiennent."""
import collections, json, sys
par = collections.OrderedDict()
for f in sys.argv[1:]:
    for l in open(f, encoding="utf-8"):
        d = json.loads(l)
        par.setdefault(d["scenario"], []).append(d)
for nom, lignes in par.items():
    c = collections.Counter(d["lecture"] + (f" ({len(d['reserves'])} réserve(s))" if d.get("reserves") else "") for d in lignes)
    print(f"== {nom} ({len(lignes)} analyses) : {dict(c)}")
    for d in lignes:
        print(f"   {d['graine']} | {d['lecture']} | par sens {d['lecture_par_sens']['a→b']} / {d['lecture_par_sens']['b→a']} | "
              f"tenues a→b {d['issues_tenues']['ab']}, b→a {d['issues_tenues']['ba']} | "
              f"λ8 a→b {d['lambda_ab_petit_ic']} b→a {d['lambda_ba_petit_ic']} | Δλ a→b {d['dl_ab_ic']} b→a {d['dl_ba_ic']}")
