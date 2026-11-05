import json, collections, sys
c = collections.defaultdict(collections.Counter)
det = collections.defaultdict(list)
for f in sys.argv[1:]:
    for l in open(f, encoding="utf-8"):
        d = json.loads(l); n = len(d.get("reserves") or [])
        lu = d.get("lecture", "code %s" % d.get("code")) + (" (%d rés.)" % n if n else "")
        c[d["scenario"]][lu] += 1
        det[d["scenario"]].append(d)
for k, v in c.items():
    print(k, dict(v))
    for d in det[k]:
        if d.get("lecture") in ("positif", "inverse", "nul") or "--detail" in sys.argv[0]:
            e = d["ecart_sens"]
            print("    graine", d["graine"], d["lecture"], d.get("reserves"), "e =", e, "dl_ab", d["dl_ab_ic"], "dl_ba", d["dl_ba_ic"],
                  "λab", d["lambda_ab_petit"], d["lambda_ab_grand"], "λba", d["lambda_ba_petit"], d["lambda_ba_grand"], "spec", d["spec_ab_ic"], d["spec_ba_ic"])
