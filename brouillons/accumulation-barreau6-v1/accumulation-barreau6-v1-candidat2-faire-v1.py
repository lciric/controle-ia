#!/usr/bin/env python3
"""Barreau 6 — fabrique du candidat 2 à partir du candidat 1, par couples {ancien, nouveau} — v1.

Entrées : le candidat 1 (`accumulation-barreau6-v1-candidat1.md`, empreinte exigée ci-dessous) et le fichier de couples
`accumulation-barreau6-v1-candidat2-couples-v1.json` (couples C2-01 à C2-09 du rédacteur : code au commit
`5ee8a4ac8712221a31599e2a92dfbae981cc5704`, qui porte la garde de non-relance ; décisions de la mère R-2275, R-2276). Chaque
« ancien » doit figurer exactement une fois au moment de son application (sinon arrêt, rien d'écrit) ; le candidat 1 n'est
jamais réécrit ; le candidat 2 n'est pas écrasé s'il existe et diffère. Après écriture, le script imprime les marqueurs
`<<…>>` restants et les citations de l'ancien commit `56c624dd…`.

Lancement : `python3 -I -B <chemin absolu de ce script> <dossier du brouillon>` ; imprime « TOUT PASSE » et l'empreinte.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

EMPREINTE_C1 = "b8bbea6a371335311a1e42cc7b37b0d1ffb632ec670746a4695c8ee6c49bc742"
C1, C2 = "accumulation-barreau6-v1-candidat1.md", "accumulation-barreau6-v1-candidat2.md"
COUPLES = "accumulation-barreau6-v1-candidat2-couples-v1.json"


def main(dossier: str) -> None:
    d = Path(dossier)
    c1 = (d / C1).read_bytes()
    if hashlib.sha256(c1).hexdigest() != EMPREINTE_C1:
        sys.exit("candidat 1 : empreinte différente de celle attendue : arrêt")
    couples = json.loads((d / COUPLES).read_text(encoding="utf-8"))["couples"]
    if [c["id"] for c in couples] != [f"C2-{i:02d}" for i in range(1, 10)]:
        sys.exit("couples attendus : C2-01 à C2-09, dans l'ordre : arrêt")
    texte = c1.decode("utf-8")
    for c in couples:
        n = texte.count(c["ancien"])
        if n != 1:
            sys.exit(f"couple {c['id']} : « ancien » présent {n} fois (exactement une attendue) : arrêt, rien d'écrit")
        texte = texte.replace(c["ancien"], c["nouveau"])
    print(f"{len(couples)} couples appliqués")
    sortie = d / C2
    if sortie.exists():
        if sortie.read_text(encoding="utf-8") != texte:
            sys.exit("candidat 2 déjà présent et différent : arrêt, rien d'écrit (R12)")
        print("candidat 2 déjà présent, identique")
    else:
        sortie.write_text(texte, encoding="utf-8")
    restes = sorted(set(re.findall(r"<<[A-Z0-9_]+>>", texte)))
    print(f"marqueurs restants : {', '.join(restes) or 'aucun'}")
    print("citations de l'ancien commit 56c624dd : " + "; ".join(
        texte[max(0, m.start() - 40):m.end() + 10].replace("\n", " ") for m in re.finditer("56c624dd", texte)))
    print(f"TOUT PASSE ; candidat 2 : {hashlib.sha256(texte.encode('utf-8')).hexdigest()}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage : accumulation-barreau6-v1-candidat2-faire-v1.py <dossier du brouillon>")
    main(sys.argv[1])
