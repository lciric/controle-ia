"""Ajustement de K1 (meilleure loi softmax du seul trait z0 sous S-V1) et de son pendant sur z1 — v1.

Rédacteur neuf (Claude Opus 5.5), 7 novembre 2026. Lecture seule de l organisme. Maximum de vraisemblance attendue sous S-V1 sur
les 4 000 instances de l oracle v60, racine SeedSequence(20261107, spawn_key=(2,)) ; imprime les deux lois arrondies à 6 décimales
et leur mesure par l oracle. La ligne « 0 » donne K1, gelée en littéral dans puissance-boucle-reelle-v1.py et au brouillon 1.
"""
import sys, json, numpy as np
sys.path.insert(0, "/home/user/ideation-organism/orchestrator")
from scipy.optimize import minimize
from pole import a_blanc_v59 as A
from pole.oracle_tour_ferme_v60 import Oracle
m = A.charger_monde("/home/user/ideation-organism/orchestrator")
racine = int(np.random.SeedSequence(20261107, spawn_key=(2,)).generate_state(1, dtype=np.uint64)[0])
o = Oracle(m["loi"], racine, A.DIM)
Z = np.array([x["z"] for x in o.instances]); P = o.P
def fit(col):
    def f(t):
        a, c = t[:3], t[3:]
        s = np.outer(Z[:, col], a) + c
        s -= s.max(1, keepdims=True)
        lq = s - np.log(np.exp(s).sum(1, keepdims=True))
        return -np.mean(np.sum(P * lq, 1))
    r = minimize(f, np.zeros(6), method="BFGS")
    a, c = r.x[:3] - r.x[0], r.x[3:] - r.x[3]
    return [round(float(v), 6) for v in a], [round(float(v), 6) for v in c]
for col in (0, 1):
    a, c = fit(col)
    poids = [[a[k], 0.0] if col == 0 else [0.0, a[k]] for k in range(3)]
    loi = {"type": "softmax", "poids": poids, "biais": c}
    print(col, json.dumps(loi), o.mesurer(loi, {}))
print("racine_oracle", racine)
