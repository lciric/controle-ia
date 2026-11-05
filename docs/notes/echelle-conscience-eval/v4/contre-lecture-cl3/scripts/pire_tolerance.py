"""Dépense réelle au pire si le prix relu dépasse l'offre de 5 % au plus (tolérance du lanceur v3) :
balayage du domaine admis par choisir_offre_v3.evaluer (prix ≤ 3,50 USD/h, descente ≤ 0,005 USD/Go, stockage < prix)."""
import importlib.util, itertools, pathlib
import numpy as np
spec = importlib.util.spec_from_file_location("co", "/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/wt-echelle-v1/echelle-v3/scripts/choisir_offre_v3.py")
CO = importlib.util.module_from_spec(spec); spec.loader.exec_module(CO)
LATENCE_S = 80   # pas de 60 s + 20 s d'attente de l'arrêt (cl2)
pires = []
for dph, desc, stock in itertools.product(np.linspace(0.5, 3.5, 301), np.linspace(0, 0.005, 11), np.linspace(0, 0.6, 61)):
    o = {"id": 1, "gpu_ram": 81920, "num_gpus": 2, "cuda_max_good": 13.2, "dph_total": float(dph),
         "inet_down_cost": float(desc), "storage_total_cost": float(stock)}
    e = CO.evaluer(o, 3.5, 0.005, 8.0)
    if e is None:
        continue
    _, duree, pire = e
    for f in (1.0, 1.05):
        reel = (duree + LATENCE_S) / 3600 * dph * f + 160 * desc + 24 * stock * f
        pires.append((reel, f, dph, desc, stock, duree, pire))
for f in (1.0, 1.05):
    m = max(p for p in pires if p[1] == f)
    print(f"facteur de prix {f}: dépense réelle maximale {m[0]:.3f} USD (dph {m[2]:.2f}, descente {m[3]:.4f}, stockage {m[4]:.3f}, durée {m[5]} s, pire calculé {m[6]:.4f})")
