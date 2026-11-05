"""Analyse du banc cl7 : par scénario, lectures v7 ; pour chaque issue prononcée, écarts e(m), réserves, spécificités ;
puis deux corrections candidates, évaluées sans relancer d'analyse (sur les grandeurs consignées) :
  R1 réserve « écart en partie porté par des modèles différents » si max |e(m)| > δ/2 ;
  R2 marge : borne basse de Δλ_s − |e(petit)| − |e(grand)| > δ dans chaque sens (positif ; miroir pour inverse)."""
import json, sys, collections
D = 0.25
lignes = [json.loads(l) for f in sys.argv[1:] for l in open(f, encoding="utf-8")]
par = collections.defaultdict(list)
for d in lignes: par[d["scenario"]].append(d)
for sc, L in par.items():
    c = collections.Counter(d.get("lecture") + (f" ({len(d['reserves'])} rés.)" if d.get("reserves") else "") for d in L)
    print(f"{sc} [{len(L)}] : " + ", ".join(f"{k} {v}" for k, v in c.most_common()))
    for d in L:
        lu = d["lecture"]
        if lu in ("positif", "inverse", "nul"):
            e = d["ecart_sens"]; m = max(abs(v) for v in e.values())
            if lu == "positif":
                r2 = all(d[f"dl_{s}_ic"][0] - abs(e["petit"]) - abs(e["grand"]) > D for s in ("ab", "ba"))
            elif lu == "inverse":
                r2 = all(-d[f"dl_{s}_ic"][1] - abs(e["petit"]) - abs(e["grand"]) > D for s in ("ab", "ba"))
            else:
                r2 = None
            print(f"    graine {d['graine']} : {lu}, réserves {d['reserves']}, e = {e['petit']:+.3f} / {e['grand']:+.3f}, "
                  f"Δλ a→b {d['dl_ab_ic']}, b→a {d['dl_ba_ic']}, spécificité {d['spec_ab_ic']} {d['spec_ba_ic']} ; "
                  f"R1 (max|e| > δ/2) : {'réserve' if m > D / 2 else 'rien'} ; R2 (marge) : {r2}")
        elif lu == "désaccord des deux sens":
            t = d["issues_tenues"]
            print(f"    graine {d['graine']} : désaccord ; tenues {t} ; e = {d['ecart_sens']}")
