"""Vérifie les tables d'empreintes (16 premiers caractères) des fichiers RENDU des rendus 5, 6 et 7 de la fille 10.

Usage : python -I verifier_empreintes_rendus_v1.py DEPOT
Lit chaque fichier par `git show <commit>:<chemin>` ; n'écrit rien.
"""
import hashlib, re, subprocess, sys

DEPOT = sys.argv[1]
RENDUS = [
    ("84a62edd30bc30f79bef69cbcc34c42c72cc8acd", "RENDU-fille-10-bras-b-v4-v1.md"),
    ("7822a65b6afb1595ce467ffeb55c8a7f736b20dc", "RENDU-fille-10-course-v12-v1.md"),
    ("8cb539f9b7ecd20fab133bfffb590ca8e1fdfc63", "RENDU-fille-10-ordre-course-v2-v1.md"),
]

def montrer(commit, chemin):
    r = subprocess.run(["git", "-C", DEPOT, "show", f"{commit}:{chemin}"], capture_output=True)
    return r.stdout if r.returncode == 0 else None

ecarts = 0
for commit, rendu in RENDUS:
    texte = montrer(commit, rendu).decode("utf-8")
    print(f"== {rendu} @ {commit[:8]}")
    for ligne in texte.splitlines():
        m = re.match(r"^\| (?:\([^)]*\) )?`([^`]+)`(?: \(inchangé\))? \| ([0-9a-f]{16}) \|$", ligne)
        if not m:
            continue
        chemin, attendu = m.group(1), m.group(2)
        contenu = montrer(commit, chemin)
        if contenu is None:
            print(f"  ABSENT   {chemin}")
            ecarts += 1
            continue
        calc = hashlib.sha256(contenu).hexdigest()
        ok = calc.startswith(attendu)
        ecarts += 0 if ok else 1
        print(f"  {'OK ' if ok else 'ÉCART'}  {attendu} {calc} {chemin}")
print("écarts :", ecarts)
