#!/usr/bin/env python3
"""Barreau 6 — fabrique du brouillon 2 à partir du brouillon 1, par couples {ancien, nouveau} — v1.

Entrées : le brouillon 1 (`accumulation-barreau6-v1-brouillon1.md`, empreinte exigée ci-dessous) et le fichier de couples
(`accumulation-barreau6-v1-brouillon2-couples-v1.json`) : liste `couples` appliquée dans l'ordre — les 28 couples de la
contre-lecture 1 (`prereg/contre-lectures/accumulation-barreau6-v1-brouillon1-cl1.md`, `c13cbdde…`), recopiés tels quels,
puis les couples B2 du rédacteur — et liste `options_N_B6_3` (couples prêts pour les options (b) et (c) de N-B6-3, **non
appliqués** : seule leur applicabilité au brouillon 2 est vérifiée).

Règles : chaque « ancien » doit figurer exactement une fois au moment de son application (sinon arrêt, rien d'écrit) ;
l'empreinte du texte après les 28 couples de la contre-lecture est comparée à celle que le rédacteur a relevée avant
d'ajouter ses couples ; le brouillon 1 n'est jamais réécrit ; le brouillon 2 n'est pas écrasé s'il existe.

Lancement : `python3 -I -B <chemin absolu de ce script> <dossier du brouillon>` ; imprime « TOUT PASSE » et l'empreinte du
brouillon 2.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

EMPREINTE_B1 = "a2d8186340fc3cd6f9fc16ab46ca81e741ce75361e43e9e34b899061a2f60c2f"
EMPREINTE_RAPPORT_CL1 = "c13cbdde18a29122f7ff17c56432280ad5d24452e9c576dc7b2faffc2b5b4fb1"
EMPREINTE_APRES_CL1 = "e903c91c504442248ac7e4539b8bae58c988614b9434d9c7fa66c7af9da81b6c"
B1, B2 = "accumulation-barreau6-v1-brouillon1.md", "accumulation-barreau6-v1-brouillon2.md"
COUPLES = "accumulation-barreau6-v1-brouillon2-couples-v1.json"


def sha(texte: str) -> str:
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()


def appliquer(texte: str, couples: list) -> str:
    for c in couples:
        n = texte.count(c["ancien"])
        if n != 1:
            sys.exit(f"couple {c['id']} : « ancien » présent {n} fois (exactement une attendue) : arrêt, rien d'écrit")
        texte = texte.replace(c["ancien"], c["nouveau"])
    return texte


def main(dossier: str) -> None:
    d = Path(dossier)
    b1 = (d / B1).read_bytes()
    if hashlib.sha256(b1).hexdigest() != EMPREINTE_B1:
        sys.exit("brouillon 1 : empreinte différente de celle attendue : arrêt")
    doc = json.loads((d / COUPLES).read_text(encoding="utf-8"))
    if doc.get("rapport_cl1_sha256") != EMPREINTE_RAPPORT_CL1:
        sys.exit("fichier de couples : empreinte du rapport de contre-lecture absente ou différente : arrêt")
    couples = doc["couples"]
    cl1 = [c for c in couples if c["id"].startswith("CL1-")]
    if [c["id"] for c in cl1] != [f"CL1-{i:02d}" for i in range(1, 29)] or couples[:28] != cl1:
        sys.exit("les 28 couples de la contre-lecture doivent venir d'abord, dans l'ordre : arrêt")
    texte = appliquer(b1.decode("utf-8"), cl1)
    if sha(texte) != EMPREINTE_APRES_CL1:
        sys.exit(f"après les 28 couples de la contre-lecture : empreinte {sha(texte)} ≠ {EMPREINTE_APRES_CL1} : arrêt")
    print(f"28 couples de la contre-lecture appliqués ; empreinte intermédiaire {EMPREINTE_APRES_CL1} (égale à l'attendue)")
    texte = appliquer(texte, couples[28:])
    print(f"{len(couples) - 28} couples du rédacteur appliqués")
    for option, liste in doc["options_N_B6_3"].items():
        appliquer(texte, liste)
        print(f"option {option} de N-B6-3 : {len(liste)} couples applicables au brouillon 2 (non appliqués)")
    sortie = d / B2
    if sortie.exists():
        if sortie.read_text(encoding="utf-8") != texte:
            sys.exit("brouillon 2 déjà présent et différent : arrêt, rien d'écrit (R12)")
        print("brouillon 2 déjà présent, identique")
    else:
        sortie.write_text(texte, encoding="utf-8")
    print(f"TOUT PASSE ; brouillon 2 : {sha(texte)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage : accumulation-barreau6-v1-brouillon2-faire-v1.py <dossier du brouillon>")
    main(sys.argv[1])
