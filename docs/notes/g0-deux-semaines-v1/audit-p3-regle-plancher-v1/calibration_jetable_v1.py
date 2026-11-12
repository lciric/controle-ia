"""Calibration à graine jetable (99, …) : rapport des écarts types bootstrap quantile / aire du plancher simulé, selon rho ;
aucun taux de décision n'est calculé ni lu."""
import sys, importlib.util, numpy as np
spec = importlib.util.spec_from_file_location("a", sys.argv[1]); A = importlib.util.module_from_spec(spec); spec.loader.exec_module(A)
A.charger(sys.argv[2], sys.argv[3], sys.argv[4])
for rho in (4.0, 1.0, 0.5, 0.25):
    rat, cor, biais, et_entre = [], [], [], []
    for w in range(5):
        y, s, p, v, tc = A.generer(0.56, rho, "propre", "population", None, (99, 9, int(rho * 100), 0, 0, w))
        for k in range(2):
            g = A.GE(A.graine_manifeste((98, 9, int(rho * 100), 0, 0, w, k)))
            r = A.remede(s[k], p[k], True, g, A.NIVEAU, A.N)
            rat.append(r["sd_q"] / r["sd_A"]); cor.append(r["corr_A_q"]); biais.append(r["q95_point"] - 0.56)
            A0 = A.PROTO.aires_tirees(A.PROTO.comparaisons(p[k], A.N), np.ones((1, A.N)), A.N)[:, 0]
            et_entre.append(A0.std(ddof=1))
    print(f"rho={rho} : sd_q/sd_A {np.mean(rat):.2f} ; corr {np.mean(cor):.3f} ; Q - theta {np.mean(biais):+.4f} ; e.t. des 200 aires {np.mean(et_entre):.4f}")
