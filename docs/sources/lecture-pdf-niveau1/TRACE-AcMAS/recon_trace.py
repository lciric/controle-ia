# Reconstruction from TRACE Table 1 (p.6) and Table 5 (p.17)
tasks = ["SSN","Bank","AA","Spam","Elect","Jira","API","Exp","Perf","Charity"]
ben = [27,9,14,34,9,24,29,9,24,10]
mal = [27,26,33,25,27,27,32,24,28,25]
T5 = {
 "Full":  [(0.963,1.000,0.926,0.962),(0.457,1.000,0.269,0.424),(0.340,1.000,0.061,0.114),(0.576,0.000,0.000,0.000),(0.250,0.000,0.000,0.000),(0.588,1.000,0.222,0.364),(0.885,1.000,0.781,0.877),(0.879,1.000,0.833,0.909),(0.538,1.000,0.143,0.250),(0.914,1.000,0.880,0.936)],
 "Seq":   [(0.889,1.000,0.778,0.875),(0.857,1.000,0.808,0.894),(0.830,1.000,0.758,0.862),(0.695,0.590,0.920,0.719),(0.306,1.000,0.074,0.138),(0.725,1.000,0.481,0.650),(0.656,0.824,0.438,0.571),(0.727,0.941,0.667,0.780),(0.596,0.889,0.286,0.432),(0.743,1.000,0.640,0.780)],
 "TRACE": [(0.463,0.481,0.926,0.633),(0.657,0.719,0.885,0.793),(0.723,0.750,0.909,0.822),(0.644,0.545,0.960,0.696),(0.444,0.733,0.407,0.524),(0.529,0.543,0.704,0.613),(0.574,0.554,0.969,0.705),(0.576,0.679,0.792,0.731),(0.673,0.634,0.929,0.754),(0.771,0.774,0.960,0.857)],
}
reported_total = {"Full":(0.648,1.000,0.405,0.577),"Seq":(0.706,0.883,0.580,0.700),"TRACE":(0.606,0.641,0.844,0.713)}
for m,rows in T5.items():
    TPs=FPs=TNs=FNs=0
    print(f"--- {m} ---")
    for t,b,ma,(acc,p,r,f) in zip(tasks,ben,mal,rows):
        tp = round(r*ma); fn = ma-tp
        correct = round(acc*(b+ma)); tn = correct - tp; fp = b - tn
        # check precision consistency
        pchk = tp/(tp+fp) if tp+fp>0 else 0.0
        print(f"{t:8s} TP={tp:3d} FN={fn:3d} TN={tn:3d} FP={fp:3d} FPR={fp/b:5.2f} prec_chk={pchk:.3f} (rep {p:.3f})")
        TPs+=tp;FPs+=fp;TNs+=tn;FNs+=fn
    N=TPs+FPs+TNs+FNs
    pooled = ((TPs+TNs)/N, TPs/(TPs+FPs) if TPs+FPs else 0, TPs/(TPs+FNs), 2*TPs/(2*TPs+FPs+FNs))
    macro = tuple(sum(x[i] for x in rows)/len(rows) for i in range(4))
    print(f"POOLED acc={pooled[0]:.4f} prec={pooled[1]:.4f} rec={pooled[2]:.4f} F1={pooled[3]:.4f} | FP={FPs}/189 FPR={FPs/189:.3f} TP={TPs}/274")
    print(f"MACRO  acc={macro[0]:.4f} prec={macro[1]:.4f} rec={macro[2]:.4f} F1={macro[3]:.4f}")
    print(f"REPORTED total {reported_total[m]}")
