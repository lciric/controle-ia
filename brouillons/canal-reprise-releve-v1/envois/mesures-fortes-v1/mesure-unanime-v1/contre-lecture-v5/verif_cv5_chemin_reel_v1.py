"""Contre-lecture v5 : la garde `verifier_scores_invalides` est-elle sur le chemin réel ?
(1) `un_passage` refuse un tableau dont une action invalide porte un score (artefact passé par la fonction de production) ;
(2) `main()` en mode réel, sur un fichier synthétique créé par le script lui-même (jamais les données réelles), avec les
    défauts imposés (20 tirages, 2 000 rééchantillonnages) : nombre d'appels de la garde compté par un enrobage.
Usage : python -I -B verif_cv5_chemin_reel_v1.py DOSSIER_DU_SCRIPT FICHIER_SYNTHETIQUE.npz SORTIE_REELLE.json
Graines : SeedSequence(2810202605, spawn_key=(3,)) pour l'artefact (R9)."""
import contextlib
import hashlib
import importlib.util
import json
import sys

import numpy as np

DOSSIER, NPZ, SORTIE = sys.argv[1:4]
spec = importlib.util.spec_from_file_location("a5", f"{DOSSIER}/analyse_fausses_alertes_v5.py")
a = importlib.util.module_from_spec(spec)
spec.loader.exec_module(a)
compte = {}

rng = np.random.default_rng(np.random.SeedSequence(2810202605, spawn_key=(3,)))
X, masque, *_ = a.synthetique(rng, E=46, T=10, n_reelles=1, n_placebo=0)
Xs = X[:, :, 0]; perm = rng.permutation(46); plis = a.plis_de_perm(perm); effet = rng.normal(size=46)
Xart = a.melanger_actions_pas_fixe(Xs, masque, rng); Xart[~masque] = 0.0
try:
    a.un_passage(Xart, masque, plis, perm, effet, 0.0); compte["un_passage_sur_artefact"] = "NON DÉTECTÉ"
except RuntimeError as e:
    compte["un_passage_sur_artefact"] = str(e)

appels = {"n": 0}
orig = a.verifier_scores_invalides
def enrobee(X, m):
    appels["n"] += 1
    return orig(X, m)
a.verifier_scores_invalides = enrobee
empreinte = hashlib.sha256(open(NPZ, "rb").read()).hexdigest()
sys.argv = ["analyse_fausses_alertes_v5.py", "--reel", NPZ, "--empreinte-attendue", empreinte, "--sondes-reelles", "3",
            "--sondes-placebo", "2", "--commit", "essai-contre-lecture"]
with open(SORTIE, "w", encoding="utf-8") as f, contextlib.redirect_stdout(f):
    a.main()
d = json.load(open(SORTIE, encoding="utf-8"))
compte["appels_de_la_garde_pendant_main_reel"] = appels["n"]
compte["appels_attendus_un_passage"] = 5 * (2 * 20 + 1 + 3 * 20 + 2 * 20)
compte["manifeste_tirages"] = d["manifeste"]["tirages"]
compte["cles_resultats"] = list(d["resultats"])
compte["M4_exces_apparie"] = d["resultats"]["M4_exces_apparie"]
json.dump(compte, sys.stdout, ensure_ascii=False, indent=1); print()
