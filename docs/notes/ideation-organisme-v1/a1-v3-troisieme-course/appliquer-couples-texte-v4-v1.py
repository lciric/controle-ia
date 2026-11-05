#!/usr/bin/env python3
"""Texte v4 (brouillon 1) d'A1-v3 = v3 scellée + les 15 couples de la contre-lecture complète, puis les couples du rédacteur.

Gardes : empreintes de la v3 scellée et des 15 couples égales à celles que nomme `couples-texte-v4-v1.json` ; chaque « ancien »
présent exactement une fois au moment de son application ; la citation du périmètre de GO-2026-11-04-06 (ligne qui porte « une
machine louée sur Vast sans carte (ou ») identique avant et après ; toute ligne retirée porte un « ancien », toute ligne ajoutée un
« nouveau » ; au motif du lanceur gelé `<<[A-Z0-9_]+>>` (chiffres compris), il ne reste que `<<COMMIT_LANCEUR_DURABLE>>`, deux fois ;
la cible ne doit pas exister (R12). Bibliothèque standard seulement.
Usage : `python3 -I appliquer-couples-texte-v4-v1.py TEXTE_V3_SCELLE DOSSIER_DE_LA_COURSE [DOSSIER_DE_SORTIE]`."""
import difflib
import hashlib
import json
import re
import sys
from pathlib import Path


def principal(source: Path, dossier: Path, sortie: Path, ici: Path) -> int:
    nos = json.loads((ici / "couples-texte-v4-v1.json").read_text(encoding="utf-8"))
    f_cl, cible = dossier / nos["couples_contre_lecture"], sortie / nos["cible"]
    for f, attendu in ((source, nos["source_sha256"]), (f_cl, nos["couples_contre_lecture_sha256"])):
        vu = hashlib.sha256(f.read_bytes()).hexdigest()
        print(f"{f.name} : sha256 {vu}")
        if vu != attendu:
            print(f"REFUS : empreinte de {f.name} {vu} au lieu de {attendu}")
            return 2
    if cible.exists():
        print(f"REFUS : {cible.name} existe déjà (R12) : rien n'est écrit")
        return 2
    lots = [("contre-lecture complète", [dict(c, n=i, lieu="couple du contre-lecteur") for i, c in
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
        if nom == "contre-lecture complète":
            print(f"après les 15 couples : sha256 {hashlib.sha256(texte.encode('utf-8')).hexdigest()}")
    apres = texte.splitlines(keepends=True)
    cite = "une machine louée sur Vast sans carte (ou"
    if [l for l in avant if cite in l] != [l for l in apres if cite in l] or len([l for l in apres if cite in l]) != 1:
        print("REFUS : la citation du périmètre de GO-2026-11-04-06 a changé")
        return 2
    marqueurs = re.findall(r"<<[A-Z0-9_]+>>", texte)
    print(f"marqueurs au motif du lanceur : {marqueurs}")
    if marqueurs != ["<<COMMIT_LANCEUR_DURABLE>>"] * 2:
        print("REFUS : il doit rester exactement deux <<COMMIT_LANCEUR_DURABLE>> et rien d'autre")
        return 2
    changees = [l for l in difflib.unified_diff(avant, apres, n=0) if l.startswith(("-", "+")) and not l.startswith(("---", "+++"))]
    anciens = [s for c in tous for s in c["ancien"].split("\n") if s]
    nouveaux = [s for c in tous for s in c["nouveau"].split("\n") if s]
    for l in changees:
        if l.strip() in ("-", "+"):
            continue
        if not any(s in l for s in (anciens if l.startswith("-") else nouveaux)):
            print(f"REFUS : ligne changée hors des couples : {l[:120]!r}")
            return 2
    print(f"citation du périmètre identique ; lignes retirées {sum(l.startswith('-') for l in changees)}, ajoutées "
          f"{sum(l.startswith('+') for l in changees)} ; lignes de la v3 : {len(avant)}, de la v4 (brouillon 1) : {len(apres)}")
    cible.write_bytes(texte.encode("utf-8"))
    print(f"cible {cible.name} écrite : sha256 {hashlib.sha256(cible.read_bytes()).hexdigest()}")
    return 0


if __name__ == "__main__":
    ici = Path(__file__).resolve().parent
    sys.exit(principal(Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]) if len(sys.argv) > 3 else Path(sys.argv[2]), ici))
