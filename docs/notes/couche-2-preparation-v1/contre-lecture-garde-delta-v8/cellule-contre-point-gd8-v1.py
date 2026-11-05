"""Contre-lecture GD8 (R2) — la « cellule » et le « point de dichotomie » de la v8 tirent-ils la même loi ?

Charge le script v8 (chemin donné, empreinte vérifiée) comme module, sans le modifier, et, pour une même étiquette, compare :
(a) `cellule(...)` (avec moments et artefacts, comme les passages) et (b) `processus` + `lectures_ebh` sans moments (comme `n_pour_puissance_fiche`).
Puis, sur G graines maîtresses, la retenue e-BH de (a) et de (b) avec leurs étiquettes respectives (cellule : `LOI|delta=…|n=288|n_garde=288|biais=0.0125|k=8` ;
point : `LOI|fiche|0.05|0.0125|8|n80f|288`). Cellule : ρ_A = ρ_B = 0,17, K_h = 5, K_s = 10, biais 0,0125, n = 288, k = 8, 2 000 répétitions.
Usage : python3 -I -B cellule-contre-point-gd8-v1.py SCRIPT_V8 SORTIE.json GRAINE1,GRAINE2,…
"""
import hashlib
import importlib.util
import json
import os
import sys

import numpy as np

SCRIPT, SORTIE = sys.argv[1:3]
GRAINES = [int(x) for x in sys.argv[3].split(",")]
assert hashlib.sha256(open(SCRIPT, "rb").read()).hexdigest() == "4c7c93a90e0be922e839f5826488edcc0745bde17f8a5de22f3a2a41bf75f1d1"
spec = importlib.util.spec_from_file_location("v8", SCRIPT)
v8 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v8)

loi = v8.LoiSynthetique(5, 10, 0.01, 0.40, 0.10, partage=True, effet_beta=0.17, echelle_b="beta", rho_b=0.17)
ebh = {"lectures": ["A"], "M": 2, "N": 0, "alpha": 0.05}
nom = loi.nom()
et_cel = f"{nom}|delta=0.05|n=288|n_garde=288|biais=0.0125|k=8"
et_pt = f"{nom}|fiche|0.05|0.0125|8|n80f|288"
res = {"script": os.path.basename(__file__), "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(), "numpy": np.__version__,
       "loi": nom, "etiquette_cellule": et_cel, "etiquette_point": et_pt, "meme_etiquette": {}, "par_graine": {}}


def point(graine, et):
    rng, _ = v8.rng_de(graine, et)
    g, c = v8.processus(loi, rng, 2000, 288, 288, 8, 0.05, 0.0125, None)
    lec = v8.lectures_ebh(loi, None, g, c, 2000, 288, 288, 8, 0.05, 0.0125, graine, et, ebh)
    return lec["ebh_A"]["retenues_fiches_du_sujet"]


# (1) même étiquette, même graine : la cellule et le point doivent rendre la même valeur
c = v8.cellule(loi, None, 2000, 288, 288, 0.05, [40.0, 160.0], 8, 0.0125, 20261029, et_cel, True, ebh)["ebh_A"]["retenues_fiches_du_sujet"]
p = point(20261029, et_cel)
res["meme_etiquette"] = {"cellule": c, "point": p, "identiques": c == p}
print("même étiquette :", res["meme_etiquette"], flush=True)
# (2) graines différentes, étiquettes de la v8
for g in GRAINES:
    c = v8.cellule(loi, None, 2000, 288, 288, 0.05, [40.0, 160.0], 8, 0.0125, g, et_cel, True, ebh)["ebh_A"]["retenues_fiches_du_sujet"]
    p = point(g, et_pt)
    res["par_graine"][str(g)] = {"cellule": c, "point": p}
    print(g, res["par_graine"][str(g)], flush=True)
cc = np.array([x["cellule"] for x in res["par_graine"].values()])
pp = np.array([x["point"] for x in res["par_graine"].values()])
res["resume"] = {"moyenne_cellule": float(cc.mean()), "moyenne_point": float(pp.mean()), "ecart_type_cellule": float(cc.std(ddof=1)),
                 "ecart_type_point": float(pp.std(ddof=1)), "graines": len(GRAINES)}
with open(SORTIE, "x", encoding="utf-8") as f:
    json.dump(res, f, indent=1, ensure_ascii=False)
    f.write("\n")
print(res["resume"])
