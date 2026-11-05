"""GD2-02 (dernier point), Q6 : la loi réelle rééchantillonne-t-elle des unités entières ?
Fichiers marqués : la ligne i du fichier j vaut un code unique (i, j) ; on vérifie que, pour chaque tirage et chaque instant
t < min(n, n_garde), les k gardes et les k contrastes viennent de la même ligne i.
Usage : python3 -I -B verif_reechantillonnage.py SORTIE.json
"""
import importlib.util
import json
import os
import sys

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("sim_garde_v3", os.path.join(ICI, "copie_script", "sim_garde_v3.py"))
sim = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sim)

N, k = 97, 3
code = lambda i, j: (i * 10 + j) / 10_000  # unique, dans [−1 ; 1]
eg = [np.array([code(i, j) for i in range(N)]) for j in range(k)]
ev = [np.array([-code(i, j) for i in range(N)]) for j in range(k)]
res = {}
for n, ng in ((50, 50), (40, 70), (70, 40)):
    loi = sim.LoiReelle(eg, ev, False)
    gg, vv = loi.tirer(np.random.default_rng(5), 200, n, ng, k, 0.0)
    ig = np.rint(gg * 10_000).astype(int)  # i*10 + j
    iv = np.rint(-vv * 10_000).astype(int)
    lignes_g = ig // 10
    lignes_v = iv // 10
    m = min(n, ng)
    res[f"n={n},n_garde={ng}"] = {
        "k_gardes_meme_ligne": bool((lignes_g == lignes_g[:, :1, :]).all()),
        "k_contrastes_meme_ligne": bool((lignes_v == lignes_v[:, :1, :]).all()),
        "garde_et_contraste_meme_ligne_sur_min": bool((lignes_g[:, :, :m] == lignes_v[:, :, :m]).all()),
        "fichier_j_au_comparateur_j": bool(((ig % 10) == np.arange(k)[None, :, None]).all() and ((iv % 10) == np.arange(k)[None, :, None]).all()),
    }
json.dump(res, open(sys.argv[1], "w"), indent=1)
print(json.dumps(res, indent=1))
