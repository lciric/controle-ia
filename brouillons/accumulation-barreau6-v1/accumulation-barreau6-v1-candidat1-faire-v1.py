#!/usr/bin/env python3
"""Barreau 6 — fabrique du candidat 1 à partir du brouillon 2, par couples {ancien, nouveau} — v1.

Entrées : le brouillon 2 (`accumulation-barreau6-v1-brouillon2.md`, empreinte exigée ci-dessous) et le fichier de couples
`accumulation-barreau6-v1-candidat1-couples-v1.json` : couples CP-01 à CP-19 du développeur du code (rapports
`rapport-developpeur-accb6-v1.md`, `2a6880e4…`, et complément, `02d837c9…`), appliqués tels qu'écrits (CP-07 en deux couples,
CP-07a et CP-07b), puis couples C1-01 à C1-17 du rédacteur. Chaque « ancien » doit figurer exactement une fois au moment de
son application (sinon arrêt, rien d'écrit) ; le brouillon 2 n'est jamais réécrit ; le candidat 1 n'est pas écrasé s'il
existe et diffère. Après écriture, le script imprime les marqueurs `<<…>>` restants.

Lancement : `python3 -I -B <chemin absolu de ce script> <dossier du brouillon>` ; imprime « TOUT PASSE » et l'empreinte.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

EMPREINTE_B2 = "9f070e31734be21d753967e0df11ee2aae174906d170a36f27a45c52714494c3"
B2, C1 = "accumulation-barreau6-v1-brouillon2.md", "accumulation-barreau6-v1-candidat1.md"
COUPLES = "accumulation-barreau6-v1-candidat1-couples-v1.json"
ORDRE_CP = ["CP-01", "CP-02", "CP-03", "CP-04", "CP-05", "CP-06", "CP-07a", "CP-07b", "CP-08", "CP-09", "CP-10", "CP-11", "CP-12",
            "CP-13", "CP-14", "CP-15", "CP-16", "CP-17", "CP-18", "CP-19"]


def main(dossier: str) -> None:
    d = Path(dossier)
    b2 = (d / B2).read_bytes()
    if hashlib.sha256(b2).hexdigest() != EMPREINTE_B2:
        sys.exit("brouillon 2 : empreinte différente de celle attendue : arrêt")
    doc = json.loads((d / COUPLES).read_text(encoding="utf-8"))
    couples = doc["couples"]
    if [c["id"] for c in couples[:len(ORDRE_CP)]] != ORDRE_CP:
        sys.exit("les couples du développeur doivent venir d'abord, dans l'ordre CP-01 à CP-19 : arrêt")
    if [c["id"] for c in couples[len(ORDRE_CP):]] != [f"C1-{i:02d}" for i in range(1, 18)]:
        sys.exit("couples du rédacteur attendus : C1-01 à C1-17, dans l'ordre : arrêt")
    texte = b2.decode("utf-8")
    for c in couples:
        n = texte.count(c["ancien"])
        if n != 1:
            sys.exit(f"couple {c['id']} : « ancien » présent {n} fois (exactement une attendue) : arrêt, rien d'écrit")
        texte = texte.replace(c["ancien"], c["nouveau"])
    print(f"{len(ORDRE_CP)} couples du développeur et {len(couples) - len(ORDRE_CP)} couples du rédacteur appliqués")
    sortie = d / C1
    if sortie.exists():
        if sortie.read_text(encoding="utf-8") != texte:
            sys.exit("candidat 1 déjà présent et différent : arrêt, rien d'écrit (R12)")
        print("candidat 1 déjà présent, identique")
    else:
        sortie.write_text(texte, encoding="utf-8")
    restes = sorted(set(re.findall(r"<<[A-Z0-9_]+>>", texte)))
    print(f"marqueurs restants : {', '.join(restes) or 'aucun'}")
    print(f"TOUT PASSE ; candidat 1 : {hashlib.sha256(texte.encode('utf-8')).hexdigest()}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage : accumulation-barreau6-v1-candidat1-faire-v1.py <dossier du brouillon>")
    main(sys.argv[1])
