"""Deux mutations du contre-lecteur sur `scripts/lancer_t06_v12.sh` (arbre détaché jetable du commit 7822a65b, jamais le dépôt) :
  L12-A : validation `^[0-9]*$` de T06_TESTS_ATTENDUS retirée (ligne remplacée par `:`) ;
  L12-B : recontrôle de GO-2026-11-06-01 à la création d'E3 bis retiré (ligne remplacée par `:`).
Chaque mutation : `tests/test_t06_v12_course.py` doit ÉCHOUER (code 1 de pytest). Puis le fichier est restauré et son empreinte
revérifiée (8b91be97…). Témoin : le fichier non muté passe (code 0).

Usage : python3.11 -I -B mutations_lanceur_v12_v1.py ARBRE BASETEMP
"""
from __future__ import annotations

import hashlib
import os
import subprocess
import sys
from pathlib import Path

ARBRE, BASE = Path(sys.argv[1]), Path(sys.argv[2])
F = ARBRE / "scripts/lancer_t06_v12.sh"
SHA = "8b91be979fac2695bb5f0db870c28aa4ca274c95889f35c7522dccd111aee7ff"
original = F.read_bytes()
assert hashlib.sha256(original).hexdigest() == SHA, "lanceur v12 déjà modifié : arrêt"
texte = original.decode("utf-8")
MUT = {
    "L12-A validation ^[0-9]*$ retirée": '    [[ "${T06_TESTS_ATTENDUS:-}" =~ ^[0-9]*$ ]] || { echo "T06_TESTS_ATTENDUS illisible (^[0-9]*$ exigé : un entier ou rien) : pas de création"; exit 2; }\n',
    "L12-B recontrôle de GO-2026-11-06-01 à la création retiré": '    [ "$EPR" != oui ] || [ "$GOC" != "$GO_EPREUVE_BIS" ] || python3 -I -B -c "$SESSION3" go "$REG" "$GO_EPREUVE" 5 >/dev/null || { echo "GO $GO_EPREUVE (5 premiers USD) non conforme au jour de la création de E3 bis"; exit 2; }\n',
}


def jouer(nom: str) -> int:
    bt = BASE / nom.split()[0]
    r = subprocess.run([sys.executable, "-I", "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", "--color=no", f"--basetemp={bt}",
                        "tests/test_t06_v12_course.py"], cwd=ARBRE, env={**os.environ, "PYTHONPATH": "src"}, capture_output=True, text=True, timeout=1800)
    print(f"{nom} : code {r.returncode} : {r.stdout.strip().splitlines()[-1] if r.stdout.strip() else ''}")
    return r.returncode


try:
    temoin = jouer("T0 témoin non muté")
    for nom, ligne in MUT.items():
        n = texte.count(ligne)
        if n != 1:
            print(f"{nom} : ligne trouvée {n} fois : mutation non jouée")
            continue
        F.write_text(texte.replace(ligne, "    :\n"), encoding="utf-8")
        code = jouer(nom)
        print("   ->", "TUÉE" if code == 1 else ("SURVIVANTE" if code == 0 else f"INVALIDE (code {code})"))
        F.write_bytes(original)
finally:
    F.write_bytes(original)
    print("restauration :", "conforme" if hashlib.sha256(F.read_bytes()).hexdigest() == SHA else "ÉCART")
