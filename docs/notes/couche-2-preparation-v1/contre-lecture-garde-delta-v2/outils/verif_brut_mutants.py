"""GD-07 et GD-08 en v2 : (1) le bloc brut garde-t-il des champs « frontière » et « tricheur » mal nommés ?
(2) À 400 unités (plus longue taille par défaut de la v2), les cellules d'artefacts séparent-elles les mutants ?

Usage : python3 -I -B verif_brut_mutants.py > ../sorties/verif_brut_mutants.json
"""
import importlib.util
import json
import math
import os
import subprocess
import sys

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(ICI, "copie_script", "sim_garde_v2.py")
spec = importlib.util.spec_from_file_location("sim", SCRIPT)
sim = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sim)
sortie = {}

# (1) fichier « réel » fictif de moyenne brute −0,03 (A tire moins que B), 180 unités
rng = np.random.default_rng(np.random.SeedSequence([20261029, 7]))
e = (rng.binomial(10, 0.02, 180) - rng.binomial(10, 0.05, 180)) / 10
chemin = os.path.join(ICI, "..", "sorties", "essais_entrees", "entrees", "brut_moyenne_negative.json")
with open(chemin, "w") as f:
    json.dump({"ecarts": [float(x) for x in e]}, f)
p = subprocess.run([sys.executable, "-I", "-B", SCRIPT, "--ecarts", chemin, "--repetitions", "2000", "--tailles", "400",
                    "--deltas", "0.05", "--m", "8,1", "--K", "10", "--taux", "0.01", "--biais", "0", "--comparateurs", "1",
                    "--sans-n80"], capture_output=True, text=True)
s = json.loads(p.stdout)
cel = s["cellules"]["reelle_brute|delta=0.05|n=400|biais=0.0|k=1"]
sortie["bloc_brut"] = {"moyenne_brute": s["ecarts_observes"]["moyenne_brute"],
                       "lois_garde": s["lois_garde"],
                       "brute_160": cel["160.0"], "brute_20": cel["20.0"],
                       "recentree_160_frontiere": s["cellules"]["reelle_recentree|delta=0.05|n=400|biais=0.0|k=1"]["160.0"]["frontiere_part"]}

# (2) mutants de la garde, binomiale K = 10, τ = 0,01, δ = 0,05, n = 400 ; parts honnête / frontière / tricheur
MUTANTS = {"correcte": lambda d, g: d - g, "signe_inverse": lambda d, g: d + g, "delta_oublie": lambda d, g: -g,
           "delta_double": lambda d, g: 2 * d - g, "marge_0.01_en_trop": lambda d, g: d + 0.01 - g}
tirer = sim.loi_garde_binomiale(10, 0.01)
mut = {}
for n in (160, 400):
    for nom, f in MUTANTS.items():
        rng = np.random.default_rng(np.random.SeedSequence([20261029, 8, n, len(nom)]))
        r = {}
        for cand, b in (("honnete", 0.0), ("frontiere", 0.05), ("tricheur", 0.10)):
            lw = sim.log_richesse(sim.ecreter(f(0.05, tirer(rng, 2000, n, b))))
            r[cand] = {str(s_): float((lw.max(axis=1) >= math.log(s_)).mean()) for s_ in (160.0, 20.0)}
        mut[f"n={n}|{nom}"] = r
sortie["mutants_delta0.05_K10_tau0.01"] = mut
json.dump(sortie, sys.stdout, indent=1, ensure_ascii=False)
print()
