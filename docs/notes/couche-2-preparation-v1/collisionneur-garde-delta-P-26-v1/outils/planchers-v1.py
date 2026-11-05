"""Tailles minimales à écarts nuls (g = 0 partout, biais b retranché : incrément δ − b) — fonction de la copie v4. Déterministe."""
import importlib.util, os, json, sys
ICI = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("simv4", os.path.join(ICI, "script-v4-copie", "simulation-puissance-garde-delta-v4.py"))
simv4 = importlib.util.module_from_spec(spec); spec.loader.exec_module(simv4)
res = {}
for d in (0.04, 0.05, 0.06, 0.075, 0.10):
    for b in (0.0, 0.005, 0.0125):
        for s in (20, 40, 160, 320):
            res[f"delta={d}|biais={b}|seuil={s}"] = simv4.taille_minimale_ecarts_nuls(d - b, s)
json.dump(res, sys.stdout, indent=1); print()
