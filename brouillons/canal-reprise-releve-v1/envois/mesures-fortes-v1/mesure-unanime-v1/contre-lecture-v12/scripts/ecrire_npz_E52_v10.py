"""Contre-lecture v10 : fichier synthétique au format réel (condition « honnete » seule) à E = 52, écrit par
`ecrire_npz_synthetique` du script v8 importé SANS modification depuis la copie du dossier ; sert à exercer la branche
E ≠ 60 de la séquence v10 (table refaite, `.partiel` gardé), jamais à lire un résultat.
Graine : SeedSequence(2810202610, spawn_key=(52,)).
Usage : python -I -B ecrire_npz_E52_v10.py SCRIPT_V8.py SORTIE.npz
"""
import hashlib
import importlib.util
import json
import sys

import numpy as np

spec = importlib.util.spec_from_file_location("afa", sys.argv[1])
afa = importlib.util.module_from_spec(spec)
spec.loader.exec_module(afa)
rng = np.random.default_rng(np.random.SeedSequence(2810202610, spawn_key=(52,)))
afa.ecrire_npz_synthetique(sys.argv[2], rng, E=52, n_reelles=3, n_placebo=2)
print(json.dumps({"ecrit": sys.argv[2], "empreinte": hashlib.sha256(open(sys.argv[2], "rb").read()).hexdigest(),
                  "script_v8": hashlib.sha256(open(sys.argv[1], "rb").read()).hexdigest(), "E": 52}))
