#!/usr/bin/env python3
"""Brouillon 2 du texte v3 d'A1-v3 = brouillon 1 + les couples de `couples-brouillon2-v3-v1.json`, appliqués dans l'ordre.

Gardes : empreinte de la source égale à celle des couples ; chaque « ancien » présent exactement une fois au moment de son
application ; la ligne 545 (citation verbatim du périmètre de GO-2026-11-04-06) identique avant et après ; aucune autre ligne que
celles des couples ne change (contrôle par différence ligne à ligne) ; la cible ne doit pas exister (R12). Bibliothèque standard
seulement ; lancé par `python3 -I appliquer-couples-brouillon2-v1.py <dossier>` (dossier par défaut : celui du script)."""
import difflib
import hashlib
import json
import sys
from pathlib import Path


def principal(dossier: Path) -> int:
    couples = json.loads((dossier / "couples-brouillon2-v3-v1.json").read_text(encoding="utf-8"))
    source, cible = dossier / couples["source"], dossier / couples["cible"]
    octets = source.read_bytes()
    vu = hashlib.sha256(octets).hexdigest()
    print(f"source {source.name} : sha256 {vu}")
    if vu != couples["source_sha256"]:
        print(f"REFUS : empreinte de la source {vu} au lieu de {couples['source_sha256']}")
        return 2
    if cible.exists():
        print(f"REFUS : {cible.name} existe déjà (R12) : rien n'est écrit")
        return 2
    texte = octets.decode("utf-8")
    avant = texte.splitlines(keepends=True)
    for c in couples["couples"]:
        n = texte.count(c["ancien"])
        if n != 1:
            print(f"REFUS : couple {c['n']} ({c['lieu']}) : « ancien » présent {n} fois au moment de son application")
            return 2
        ligne = texte[:texte.index(c["ancien"])].count("\n") + 1
        texte = texte.replace(c["ancien"], c["nouveau"], 1)
        print(f"couple {c['n']} appliqué à la ligne {ligne} ({c['lieu']}) : {len(c['ancien'])} → {len(c['nouveau'])} caractères")
    apres = texte.splitlines(keepends=True)
    if avant[544] != apres[544] or "une machine louée sur Vast sans carte (ou" not in apres[544]:
        print("REFUS : la ligne 545 a changé")
        return 2
    changees = [l for l in difflib.unified_diff(avant, apres, n=0) if l.startswith(("-", "+")) and not l.startswith(("---", "+++"))]
    print(f"ligne 545 identique ; lignes retirées {sum(l.startswith('-') for l in changees)}, ajoutées "
          f"{sum(l.startswith('+') for l in changees)} ; lignes du brouillon 1 : {len(avant)}, du brouillon 2 : {len(apres)}")
    # rien d'autre ne change : toute ligne retirée porte un « ancien », toute ligne ajoutée porte un « nouveau »
    anciens = [s for c in couples["couples"] for s in c["ancien"].split("\n") if s]
    nouveaux = [s for c in couples["couples"] for s in c["nouveau"].split("\n") if s]
    for l in changees:
        segments = anciens if l.startswith("-") else nouveaux
        if not any(s in l for s in segments):
            print(f"REFUS : ligne changée hors des couples : {l[:120]!r}")
            return 2
    cible.write_bytes(texte.encode("utf-8"))
    print(f"cible {cible.name} écrite : sha256 {hashlib.sha256(cible.read_bytes()).hexdigest()}")
    return 0


if __name__ == "__main__":
    sys.exit(principal(Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent))
