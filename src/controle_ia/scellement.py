"""Scellement par empreinte compagnon (R6) et vérification (R11, R12).

Un dépôt est un fichier immuable. Son empreinte compagnon est `<fichier>.sha256`,
au format de `sha256sum` (« <hex>  <nom de base> »), donc vérifiable aussi par
`sha256sum -c <fichier>.sha256` depuis le dossier du fichier.

Utilisation en ligne de commande :
    python -m controle_ia.scellement sceller FICHIER...
    python -m controle_ia.scellement verifier FICHIER...
    python -m controle_ia.scellement verifier-arbre [RACINE]
"""
from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

from .gardes import GardeArret

SUFFIXE = ".sha256"
# Dossiers dont chaque fichier est un dépôt scellé. Les registres vivants
# (registres/*.md) sont versionnés par git ; les passations, jamais réécrites,
# sont scellées.
DOSSIERS_SCELLES = ("docs", "prereg", "runs", "diag", "livrables", "registres/passations")
IGNORES = {".gitkeep"}
_LIGNE = re.compile(r"^([0-9a-f]{64})  (\S.*)$")


def empreinte(chemin: str | Path) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def compagnon(chemin: str | Path) -> Path:
    return Path(str(chemin) + SUFFIXE)


def lire_compagnon(chemin_compagnon: str | Path, nom_attendu: str) -> str:
    texte = Path(chemin_compagnon).read_text(encoding="utf-8")
    lignes = [l for l in texte.splitlines() if l.strip()]
    if len(lignes) != 1:
        raise GardeArret(f"{chemin_compagnon} : une seule ligne attendue, {len(lignes)} trouvées")
    m = _LIGNE.match(lignes[0])
    if not m:
        raise GardeArret(f"{chemin_compagnon} : ligne illisible {lignes[0]!r}")
    if m.group(2) != nom_attendu:
        raise GardeArret(f"{chemin_compagnon} : nom {m.group(2)!r} au lieu de {nom_attendu!r}")
    return m.group(1)


def sceller(chemin: str | Path) -> str:
    """Écrit l'empreinte compagnon. Idempotent ; refuse d'écraser une empreinte différente (R12)."""
    p = Path(chemin)
    if p.name.endswith(SUFFIXE):
        raise GardeArret(f"{p} est une empreinte : on ne scelle pas une empreinte")
    if not p.is_file():
        raise GardeArret(f"{p} : fichier absent sur disque, rien à sceller")
    h = empreinte(p)
    c = compagnon(p)
    if c.exists():
        existante = lire_compagnon(c, p.name)
        if existante != h:
            raise GardeArret(
                f"{p} est déjà scellé avec une autre empreinte ({existante[:12]}…) : "
                "R12 interdit d'écraser — une nouvelle version prend un nouveau nom"
            )
        return h
    c.write_text(f"{h}  {p.name}\n", encoding="utf-8")
    return h


def verifier(chemin: str | Path) -> str:
    """Vérifie un dépôt contre son empreinte compagnon ; lève `GardeArret` sinon."""
    p = Path(chemin)
    c = compagnon(p)
    if not p.is_file():
        raise GardeArret(f"{p} : fichier absent sur disque")
    if not c.is_file():
        raise GardeArret(f"{p} : empreinte compagnon {c.name} absente")
    attendue = lire_compagnon(c, p.name)
    obtenue = empreinte(p)
    if obtenue != attendue:
        raise GardeArret(f"{p} : empreinte {obtenue[:12]}… ≠ scellée {attendue[:12]}…")
    return obtenue


def verifier_arbre(racine: str | Path = ".", dossiers=DOSSIERS_SCELLES) -> list[tuple[str, str]]:
    """Renvoie la liste des problèmes (chemin, motif) ; vide si tout est scellé et intact."""
    racine = Path(racine)
    problemes: list[tuple[str, str]] = []
    for d in dossiers:
        base = racine / d
        if not base.exists():
            continue
        for p in sorted(base.rglob("*")):
            if not p.is_file() or p.name in IGNORES:
                continue
            rel = str(p.relative_to(racine))
            if p.name.endswith(SUFFIXE):
                source = Path(str(p)[: -len(SUFFIXE)])
                if not source.is_file():
                    problemes.append((rel, "empreinte orpheline : le fichier scellé est absent"))
                continue
            try:
                verifier(p)
            except GardeArret as e:
                problemes.append((rel, str(e)))
    return problemes


def _main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 2
    action, args = argv[0], argv[1:]
    if action == "sceller":
        for a in args:
            print(f"{sceller(a)}  {a}")
        return 0
    if action == "verifier":
        for a in args:
            print(f"OK {verifier(a)[:12]}…  {a}")
        return 0
    if action == "verifier-arbre":
        problemes = verifier_arbre(args[0] if args else ".")
        for chemin, motif in problemes:
            print(f"ÉCHEC {chemin} : {motif}")
        print("arbre intact" if not problemes else f"{len(problemes)} problème(s)")
        return 0 if not problemes else 1
    print(f"action inconnue : {action}")
    return 2


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
