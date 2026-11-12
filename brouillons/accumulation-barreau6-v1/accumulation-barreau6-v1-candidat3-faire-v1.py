#!/usr/bin/env python3
"""Barreau 6 — fabrique du candidat 3 à partir du candidat 2, par couples {ancien, nouveau} — v1.

Entrées : le candidat 2 (`accumulation-barreau6-v1-candidat2.md`, empreinte exigée ci-dessous) et le fichier de couples
`accumulation-barreau6-v1-candidat3-couples-v1.json` (couples C3-01 à C3-16 du rédacteur : code au commit
`6c98ea20ab7ecfff0c7f10998b9dfad3d75cc625`, énumération v2, VB6-3, rendu de « non interprétable », « Reste » ; décisions de la
mère R-2277 à R-2279). Chaque « ancien » doit figurer exactement une fois au moment de son application (sinon arrêt, rien
d'écrit) ; le candidat 2 n'est jamais réécrit ; le candidat 3 n'est pas écrasé s'il existe et diffère. Après écriture, le
script imprime les marqueurs `<<…>>` restants et les citations du commit précédent `5ee8a4ac…`.

Lancement : `python3 -I -B <chemin absolu de ce script> <dossier du brouillon>` ; imprime « TOUT PASSE » et l'empreinte.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

EMPREINTE_C2 = "0716d3d52fd60f76b51c921ef8284580d70ddc587d855cfbc12381c1667baee1"
C2, C3 = "accumulation-barreau6-v1-candidat2.md", "accumulation-barreau6-v1-candidat3.md"
COUPLES = "accumulation-barreau6-v1-candidat3-couples-v1.json"


def main(dossier: str) -> None:
    d = Path(dossier)
    c2 = (d / C2).read_bytes()
    if hashlib.sha256(c2).hexdigest() != EMPREINTE_C2:
        sys.exit("candidat 2 : empreinte différente de celle attendue : arrêt")
    couples = json.loads((d / COUPLES).read_text(encoding="utf-8"))["couples"]
    if [c["id"] for c in couples] != [f"C3-{i:02d}" for i in range(1, 17)]:
        sys.exit("couples attendus : C3-01 à C3-16, dans l'ordre : arrêt")
    texte = c2.decode("utf-8")
    for c in couples:
        n = texte.count(c["ancien"])
        if n != 1:
            sys.exit(f"couple {c['id']} : « ancien » présent {n} fois (exactement une attendue) : arrêt, rien d'écrit")
        texte = texte.replace(c["ancien"], c["nouveau"])
    print(f"{len(couples)} couples appliqués")
    sortie = d / C3
    if sortie.exists():
        if sortie.read_text(encoding="utf-8") != texte:
            sys.exit("candidat 3 déjà présent et différent : arrêt, rien d'écrit (R12)")
        print("candidat 3 déjà présent, identique")
    else:
        sortie.write_text(texte, encoding="utf-8")
    restes = sorted(set(re.findall(r"<<[A-Z0-9_]+>>", texte)))
    print(f"marqueurs restants : {', '.join(restes) or 'aucun'}")
    print("citations du commit précédent 5ee8a4ac : " + "; ".join(
        texte[max(0, m.start() - 40):m.end() + 10].replace("\n", " ") for m in re.finditer("5ee8a4ac", texte)))
    print(f"TOUT PASSE ; candidat 3 : {hashlib.sha256(texte.encode('utf-8')).hexdigest()}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage : accumulation-barreau6-v1-candidat3-faire-v1.py <dossier du brouillon>")
    main(sys.argv[1])
