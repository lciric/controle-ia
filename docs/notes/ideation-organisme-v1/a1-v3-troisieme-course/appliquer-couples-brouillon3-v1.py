#!/usr/bin/env python3
"""Brouillon 3 du texte v3 d'A1-v3 = brouillon 2 + les 9 couples de la contre-lecture n° 4, puis les couples du rédacteur.

Gardes : empreintes du brouillon 2 et des couples de la contre-lecture égales à celles que nomme `couples-brouillon3-v3-v1.json` ;
chaque « ancien » présent exactement une fois au moment de son application ; ligne 545 (citation verbatim du périmètre de
GO-2026-11-04-06) identique avant et après ; toute ligne retirée porte un « ancien », toute ligne ajoutée un « nouveau » ; la cible
ne doit pas exister (R12). Bibliothèque standard seulement.
Usage : `python3 -I appliquer-couples-brouillon3-v1.py [DOSSIER_DE_LA_COURSE [DOSSIER_DE_SORTIE]]` (défauts : dossier du script)."""
import difflib
import hashlib
import json
import sys
from pathlib import Path


def principal(dossier: Path, sortie: Path, ici: Path) -> int:
    nos = json.loads((ici / "couples-brouillon3-v3-v1.json").read_text(encoding="utf-8"))
    source, cible = dossier / nos["source"], sortie / nos["cible"]
    f_cl = dossier / nos["couples_contre_lecture"]
    for f, attendu in ((source, nos["source_sha256"]), (f_cl, nos["couples_contre_lecture_sha256"])):
        vu = hashlib.sha256(f.read_bytes()).hexdigest()
        print(f"{f.name} : sha256 {vu}")
        if vu != attendu:
            print(f"REFUS : empreinte de {f.name} {vu} au lieu de {attendu}")
            return 2
    if cible.exists():
        print(f"REFUS : {cible.name} existe déjà (R12) : rien n'est écrit")
        return 2
    lots = [("contre-lecture n° 4", [dict(c, n=i, lieu="couple du contre-lecteur") for i, c in
                                     enumerate(json.loads(f_cl.read_text(encoding="utf-8")), 1)]),
            ("rédacteur", nos["couples"])]
    texte = source.read_text(encoding="utf-8")
    avant = texte.splitlines(keepends=True)
    tous = []
    for nom, couples in lots:
        for c in couples:
            n = texte.count(c["ancien"])
            if n != 1:
                print(f"REFUS : {nom}, couple {c['n']} ({c['lieu']}) : « ancien » présent {n} fois au moment de son application")
                return 2
            ligne = texte[:texte.index(c["ancien"])].count("\n") + 1
            texte = texte.replace(c["ancien"], c["nouveau"], 1)
            tous.append(c)
            print(f"{nom}, couple {c['n']} appliqué à la ligne {ligne} ({c['lieu']}) : {len(c['ancien'])} → {len(c['nouveau'])} "
                  "caractères")
    apres = texte.splitlines(keepends=True)
    if avant[544] != apres[544] or "une machine louée sur Vast sans carte (ou" not in apres[544]:
        print("REFUS : la ligne 545 a changé")
        return 2
    changees = [l for l in difflib.unified_diff(avant, apres, n=0) if l.startswith(("-", "+")) and not l.startswith(("---", "+++"))]
    anciens = [s for c in tous for s in c["ancien"].split("\n") if s]
    nouveaux = [s for c in tous for s in c["nouveau"].split("\n") if s]
    for l in changees:
        if not any(s in l for s in (anciens if l.startswith("-") else nouveaux)):
            print(f"REFUS : ligne changée hors des couples : {l[:120]!r}")
            return 2
    print(f"ligne 545 identique ; lignes retirées {sum(l.startswith('-') for l in changees)}, ajoutées "
          f"{sum(l.startswith('+') for l in changees)} ; lignes du brouillon 2 : {len(avant)}, du brouillon 3 : {len(apres)}")
    cible.write_bytes(texte.encode("utf-8"))
    print(f"cible {cible.name} écrite : sha256 {hashlib.sha256(cible.read_bytes()).hexdigest()}")
    return 0


if __name__ == "__main__":
    ici = Path(__file__).resolve().parent
    dossier = Path(sys.argv[1]) if len(sys.argv) > 1 else ici
    sys.exit(principal(dossier, Path(sys.argv[2]) if len(sys.argv) > 2 else dossier, ici))
