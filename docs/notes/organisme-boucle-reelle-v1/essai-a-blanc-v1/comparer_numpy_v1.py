"""Comparaison de huit jugements du dessin (V1 à V4, F1 à F4, archive {K1}, racine 123456789) sous deux interpréteurs — v1.

Rédacteur neuf (Claude Opus 5.5), 7 novembre 2026. Lecture seule de l organisme ; n importe pas l oracle (scipy absent du Python
du système). Imprime la version de numpy puis les log W maximaux (repr) ; deux sorties égales à l octet = aucun écart.
"""
import sys, json
sys.path.insert(0, "/home/user/ideation-organism/orchestrator")
import numpy as np
from pole import a_blanc_v59 as A
m = A.charger_monde("/home/user/ideation-organism/orchestrator"); L = m["loi"]
k1 = {"type": "softmax", "poids": [[0.0, 0.0], [-0.834964, 0.0], [-0.242046, 0.0]], "biais": [0.0, 0.941698, 0.721847]}
U = {"type": "fixe", "probas": [1.0, 1.0, 1.0]}; B = {"type": "fixe", "probas": [0.3, 0.4, 0.3]}
V = {"V1-loi-du-monde": L, "V2-trait-z1-seul": {"type": "softmax", "poids": [[0.0, r[1]] for r in L["poids"]], "biais": list(L["biais"])},
     "V3-loi-du-monde-temperee-0.08": {"type": "transformee", "base": L, "puissance": 0.08},
     "V4-loi-du-monde-melee-uniforme-0.85": {"type": "melange", "composantes": [L, U], "poids": [0.15, 0.85]}}
F = {"F1-copie-renommee-de-K1": json.loads(json.dumps(k1)),
     "F2-K1-melee-uniforme-0.2": {"type": "melange", "composantes": [k1, U], "poids": [0.8, 0.2]},
     "F3-K1-melee-aveugle-fixe-0.2": {"type": "melange", "composantes": [k1, B], "poids": [0.8, 0.2]},
     "F4-K1-temperee-inclinee": {"type": "transformee", "base": k1, "puissance": 1.2, "inclinaison": [0.0, 0.05, -0.05]}}
out = {}
for g, lois in (("V", V), ("F", F)):
    for n, l in lois.items():
        ev, d = A.juger_carte(l, m, {"K1": k1}, 123456789, f"cmp|{g}|{n}")
        out[n] = repr(ev["log_richesse_max"])
print(np.__version__, json.dumps(out))
