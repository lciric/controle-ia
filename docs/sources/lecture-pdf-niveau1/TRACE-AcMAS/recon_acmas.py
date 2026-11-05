# AcMAS Table 1 (p.6), F1 values: order CSQA, GSM8K, InjecAgent, PoisonRAG, HotPotQA
F1 = {
 "TAM":        {"sync":[0.28,0.27,0.51,0.27,0.26], "async":[0.19,0.18,0.34,0.18,0.17]},
 "PERM":       {"sync":[0.38,0.37,0.64,0.36,0.33], "async":[0.27,0.26,0.43,0.25,0.24]},
 "G-Safeguard":{"sync":[0.74,0.71,0.69,0.72,0.70], "async":[0.46,0.44,0.41,0.43,0.42]},
 "BlindGuard": {"sync":[0.58,0.56,0.54,0.57,0.55], "async":[0.35,0.33,0.31,0.33,0.32]},
 "AcMAS":      {"sync":[0.95,0.95,0.93,0.95,0.94], "async":[0.94,0.94,0.92,0.94,0.93]},
}
m = lambda v: sum(v)/len(v)
for k,v in F1.items():
    print(f"{k:12s} sync={m(v['sync']):.3f} async={m(v['async']):.3f}")
for mode in ["sync","async"]:
    gs, bg = m(F1["G-Safeguard"][mode]), m(F1["BlindGuard"][mode])
    allb = m([m(F1[b][mode]) for b in ["TAM","PERM","G-Safeguard","BlindGuard"]])
    ac = m(F1["AcMAS"][mode])
    print(f"{mode}: AcMAS={ac:.3f} | best(GS)={gs:.3f} gain={ac-gs:+.3f} | mean(GS,BG)={(gs+bg)/2:.3f} gain={ac-(gs+bg)/2:+.3f} | mean(all4)={allb:.3f} gain={ac-allb:+.3f}")
