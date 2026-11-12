"""Assemble le dossier d'entretien fusionné v2 (session-dépôt, 10 novembre 2026).

Usage : python scripts/assembler_dossier_entretien_v2.py PARTIES.json GARDE.pdf SORTIE.pdf

PARTIES.json : liste d'objets {partie, titre, auteur, source, sha256, fichier, pages_source?}
  - fichier : chemin local du PDF de la partie ;
  - sha256 : empreinte attendue de ce fichier (vérifiée avant toute copie ; arrêt si elle diffère, aucun repli) ;
  - pages_source (facultatif) : [premiere, derniere], pages 1-indexées à extraire du fichier (cas d'une partie reprise
    du dossier v1) ; sinon toutes les pages.
GARDE.pdf : page de garde et table des parties, déjà rendue (ses numéros de pages sont ceux que ce script calcule
  avec l'option --plan).

Avec --plan, le script n'écrit rien : il vérifie les empreintes et imprime, pour chaque partie, son nombre de pages
et ses pages de début et de fin dans le dossier, en supposant GARDE.pdf de N pages (--pages-garde N).
Les pages sont copiées sans retouche (pypdf), puis le manifeste SORTIE-parties.json est écrit à côté de SORTIE.
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter


def empreinte(chemin):
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def pages_de(partie):
    lecteur = PdfReader(partie["fichier"])
    if "pages_source" in partie:
        premiere, derniere = partie["pages_source"]
        if not (1 <= premiere <= derniere <= len(lecteur.pages)):
            raise SystemExit(f"partie {partie['partie']} : pages_source {premiere}-{derniere} hors du fichier "
                             f"({len(lecteur.pages)} pages)")
        return lecteur, list(range(premiere - 1, derniere))
    return lecteur, list(range(len(lecteur.pages)))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("parties")
    p.add_argument("garde")
    p.add_argument("sortie")
    p.add_argument("--plan", action="store_true")
    p.add_argument("--pages-garde", type=int, default=2)
    a = p.parse_args()

    parties = json.loads(Path(a.parties).read_text(encoding="utf-8"))
    for partie in parties:
        vue = empreinte(partie["fichier"])
        if vue != partie["sha256"]:
            raise SystemExit(f"ARRÊT partie {partie['partie']} : empreinte {vue} ≠ attendue {partie['sha256']}")

    n_garde = a.pages_garde if a.plan else len(PdfReader(a.garde).pages)
    debut = n_garde + 1
    plan = []
    for partie in parties:
        _, idx = pages_de(partie)
        plan.append({**{k: v for k, v in partie.items() if k != "fichier"}, "pages": len(idx), "debut": debut,
                     "fin": debut + len(idx) - 1})
        debut += len(idx)
    if a.plan:
        for l in plan:
            print(f"{l['partie']:<12} {l['pages']:>3} pages  {l['debut']:>3} à {l['fin']:>3}  {l['sha256'][:16]}")
        print(f"total {debut - 1} pages (garde {n_garde})")
        return

    ecrivain = PdfWriter()
    for page in PdfReader(a.garde).pages:
        ecrivain.add_page(page)
    for partie in parties:
        lecteur, idx = pages_de(partie)
        for i in idx:
            ecrivain.add_page(lecteur.pages[i])
    with open(a.sortie, "wb") as f:
        ecrivain.write(f)
    manifeste = Path(a.sortie).with_name(Path(a.sortie).stem + "-parties.json")
    manifeste.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"écrit {a.sortie} ({len(ecrivain.pages)} pages), {empreinte(a.sortie)}")
    print(f"écrit {manifeste}")


if __name__ == "__main__":
    sys.exit(main())
