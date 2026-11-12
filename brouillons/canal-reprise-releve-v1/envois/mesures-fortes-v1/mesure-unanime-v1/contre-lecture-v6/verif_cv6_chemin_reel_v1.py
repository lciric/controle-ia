"""Contre-lecture v6 : la garde `verifier_scores_invalides` sur le chemin réel de `main()` (mode réel, fichier
synthétique écrit par le test des gardes, jamais les données réelles). Lancé depuis le dossier du préenregistrement ;
le script v6 est importé sans modification ; seules des enveloppes (compteur, mélange fautif) sont posées sur ses noms.

Usage : python -I -B verif_cv6_chemin_reel_v1.py NPZ_SYNTHETIQUE SORTIE_JSON_DU_MODE_REEL
(1) compte les appels de la garde pendant un `main()` complet en mode réel (3 réelles, 2 placebo, 20 tirages, 2 000) et
    écrit la sortie de ce mode réel ; (2) relance `main()` avec un mélange qui écrit un score hors du masque : la garde
    doit arrêter le run."""
import contextlib
import hashlib
import io
import json
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.getcwd())
import numpy as np  # noqa: E402

import analyse_fausses_alertes_v6 as a  # noqa: E402

npz, sortie_json = sys.argv[1], sys.argv[2]
h = hashlib.sha256(open(npz, "rb").read()).hexdigest()
argv = ["analyse_fausses_alertes_v6.py", "--reel", npz, "--empreinte-attendue", h, "--sondes-reelles", "3",
        "--sondes-placebo", "2", "--commit", "contre-lecture-v6-essai"]
compte = {"n": 0}
orig_garde, orig_mel = a.verifier_scores_invalides, a.melanger_actions


def garde_comptee(X, masque):
    compte["n"] += 1
    return orig_garde(X, masque)


a.verifier_scores_invalides = garde_comptee
sys.argv = argv
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    a.main()
with open(sortie_json, "w", encoding="utf-8") as f:
    f.write(buf.getvalue())
res = {"empreinte_npz": h, "appels_de_la_garde_pendant_main": compte["n"],
       "attendu": "5 sondes × (1 + 3×20 + 2×20 + 2×20) = 705 passages"}


def melange_fautif(X, masque, rng):
    Xm = orig_mel(X, masque, rng)
    Xm[~masque] = 0.0
    return Xm


a.verifier_scores_invalides = orig_garde
a.melanger_actions = melange_fautif
try:
    with contextlib.redirect_stdout(io.StringIO()):
        a.main()
    res["melange_fautif"] = "NON DÉTECTÉ"
except RuntimeError as e:
    res["melange_fautif"] = f"arrêt : {e}"
a.melanger_actions = orig_mel
json.dump(res, sys.stdout, ensure_ascii=False, indent=1)
print()
