"""Mutations du banc, v2 (R-2272) : celles de la v1, plus le contrôle du code (`code_accb6_v1.py`) et son appel par la lecture."""
from mutations_accb6_v1 import MUTATIONS as V1

MUTATIONS = list(V1) + [
    ("C01", "code_accb6_v1.py", 'if _git(depot, "merge-base", "--is-ancestor", commit, tete)[0] != 0:', "if False:", "commit ancêtre de la tête"),
    ("C02", "code_accb6_v1.py", "    if au_commit != ecrits:", "    if False:", "fichiers du paquet au commit = liste"),
    ("C03", "code_accb6_v1.py", "    if importes != ecrits:", "    if False:", "fichiers du paquet importé = liste"),
    ("C04", "code_accb6_v1.py", "        if code != 0 or _sha(blob) != s:", "        if False:", "empreintes au commit"),
    ("C05", "code_accb6_v1.py", "        if _sha((dossier / Path(p).name).read_bytes()) != s:", "        if False:", "empreintes du paquet importé"),
    ("C06", "code_accb6_v1.py", 'if not COMMIT.fullmatch(commit) or _git(depot, "cat-file", "-e", f"{commit}^{{commit}}")[0] != 0:',
     "if not COMMIT.fullmatch(commit):", "commit cité présent"),
    ("C07", "code_accb6_v1.py", "    if dossier != (depot / PREFIXE).resolve():", "    if False:", "paquet à sa place dans le dépôt"),
    ("C08", "code_accb6_v1.py", 'fautifs = [p for p, s in d["fichiers"].items() if not (_du_paquet(p) and rg.SHA.fullmatch(s))]',
     "fautifs = []", "chemins listés dans le paquet"),
    ("C09", "code_accb6_v1.py", '    if c != 0:\n        raise rg.RefusRegistre(f"CODE-ACCB6 : le paquet importé',
     '    if False:\n        raise rg.RefusRegistre(f"CODE-ACCB6 : le paquet importé', "paquet hors dépôt git"),
    ("C10", "lecture_v1.py", '        code = ca.controler_code(racine, g["lignes_propres"][gv.CODE_ACCB6], dossier_code)', "        code = None",
     "appel du contrôle par la lecture"),
]
