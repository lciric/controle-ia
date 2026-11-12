"""Brouillon 2 du dossier (ii-b) : application des couples, par script, sans écriture au moindre écart.

Usage : python3 -I appliquer-brouillon2-ii-b-v1.py DOSSIER [--ecrire]
Sans `--ecrire`, le script vérifie et rend les empreintes sans rien écrire (essai à blanc).

Ordre (consigne de la mère, brouillon 2 ; R-2060) :
1. empreintes vérifiées : les quatre brouillons 1 (égales à leurs compagnons `.sha256`), la liste des couples de la
   contre-lecture 1 (`couples-contre-lecture-ii-b-v1-cl1.json`, `bafe6779…`) et la liste des couples de la mère et du
   rédacteur (`couples-mere-redacteur-ii-b-v2.json`, empreinte écrite ci-dessous) ;
2. couples Z1 à Z24, dans l'ordre de la liste, chacun sur son fichier ; chaque « ancien » doit être présent **exactement une
   fois** au moment de son application ; après eux, chaque texte doit égaler l'empreinte de l'annexe B de la contre-lecture 1 ;
3. couples de la mère et du rédacteur (M2, M4, M7, R, S), dans l'ordre de leur liste, même règle d'unicité ;
4. contrôles : plus aucune occurrence de « 8 sur 64 » rattachée à E-O3 hors de la mention « brouillon 1 : 8 » ; les blocs
   cités (« > ») de la consigne privée inchangés ; même ensemble de marqueurs `<<…>>` dans l'ordre ;
5. aucun fichier de sortie ne doit exister (R12) ; puis, avec `--ecrire` seulement, écriture des `…-v1-brouillon2.md`.
Tout écart : arrêt (code 2) avant toute écriture.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

COUPLES_CL1 = ("couples-contre-lecture-ii-b-v1-cl1.json", "bafe677976d184e7cc28025213ce82e4c73b030faa1c4236d458fb3a2741a0f2")
COUPLES_MERE = ("couples-mere-redacteur-ii-b-v2.json", "eca35617820570746f34e1473ba8dbd0b0234b10b79a8c6dbc573bd0c9ec1f3b")
FICHIERS = ("conception-ii-b-v1-brouillon1.md", "consigne-privee-maitre-ii-b-v1-brouillon1.md",
            "devis-ii-b-v1-brouillon1.md", "ordre-exploratoire-ii-b-v1-brouillon1.md")
ANNEXE_B = {"conception-ii-b-v1-brouillon1.md": "8b6771c55ee520f9cb84e2fe0243c490ce7e06daed054af16798b56c3b1c0315",
            "consigne-privee-maitre-ii-b-v1-brouillon1.md": "1d9d6bb13ca2a4660ff66f071129c7c707df711036738f4bfc1430aa69a83e3c",
            "devis-ii-b-v1-brouillon1.md": "67c2856f34563e3c6e207df4d0e77c200910670a5cb19168fa83e04d0d94e7cc",
            "ordre-exploratoire-ii-b-v1-brouillon1.md": "2f095a6f55a7d7d538ebf10ca9d550179a02c1ea1f8d230bc13829c91af0776d"}
MARQUEUR = re.compile(r"<<[A-Z0-9_]+>>")


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def arret(motif: str) -> None:
    print(f"ARRÊT, rien n'est écrit : {motif}")
    sys.exit(2)


def blocs_cites(texte: str) -> list[str]:
    blocs, courant = [], []
    for ligne in texte.splitlines():
        if ligne.startswith(">"):
            courant.append(ligne)
        elif courant:
            blocs.append("\n".join(courant))
            courant = []
    if courant:
        blocs.append("\n".join(courant))
    return blocs


def appliquer(textes: dict, couples: list, quoi: str) -> list[str]:
    journal = []
    for c in couples:
        f = c["fichier"]
        if f not in textes:
            arret(f"{quoi} {c['id']} : fichier {f} inconnu")
        n = textes[f].count(c["ancien"])
        if n != 1:
            arret(f"{quoi} {c['id']} ({f}) : « ancien » présent {n} fois au moment de son application")
        textes[f] = textes[f].replace(c["ancien"], c["nouveau"], 1)
        journal.append(f"{c['id']}\t{f}\tune occurrence\tappliqué")
    return journal


def main(argv: list[str]) -> int:
    if len(argv) not in (2, 3) or (len(argv) == 3 and argv[2] != "--ecrire"):
        print(__doc__)
        return 2
    d = Path(argv[1])
    ecrire = len(argv) == 3
    listes = {}
    for nom, attendu in (COUPLES_CL1, COUPLES_MERE):
        b = (d / nom).read_bytes()
        if sha(b) != attendu:
            arret(f"{nom} : empreinte {sha(b)} ≠ {attendu}")
        listes[nom] = json.loads(b.decode("utf-8"))
    textes, avant = {}, {}
    for f in FICHIERS:
        b = (d / f).read_bytes()
        compagnon = (d / (f + ".sha256")).read_text(encoding="utf-8").split()[0]
        if sha(b) != compagnon:
            arret(f"{f} : empreinte {sha(b)} ≠ compagnon {compagnon}")
        textes[f] = b.decode("utf-8")
        avant[f] = sha(b)
    journal = appliquer(textes, listes[COUPLES_CL1[0]], "couple de la contre-lecture")
    for f, attendu in ANNEXE_B.items():
        h = sha(textes[f].encode("utf-8"))
        if h != attendu:
            arret(f"{f} après Z1 à Z24 : {h} ≠ annexe B {attendu}")
        journal.append(f"annexe B\t{f}\t{h}\tégale")
    journal += appliquer(textes, listes[COUPLES_MERE[0]], "couple de la mère ou du rédacteur")
    # contrôles
    for f, t in textes.items():
        for m in re.finditer(r"8 (?:épisodes acceptés )?sur 64", t):
            contexte = t[max(0, m.start() - 40):m.end() + 5]
            if "brouillon 1 : 8" not in t[max(0, m.start() - 60):m.end() + 60] and "à « au plus 8 sur 64 »" not in contexte \
                    and "plus de 8" not in contexte:
                arret(f"{f} : « {contexte} » : constante d'E-O3 non mise à jour (M2)")
    k1 = (d / "consigne-privee-maitre-ii-b-v1-brouillon1.md").read_text(encoding="utf-8")
    if blocs_cites(k1) != blocs_cites(textes["consigne-privee-maitre-ii-b-v1-brouillon1.md"]):
        arret("consigne privée : blocs cités changés")
    o1 = (d / "ordre-exploratoire-ii-b-v1-brouillon1.md").read_text(encoding="utf-8")
    if set(MARQUEUR.findall(o1)) != set(MARQUEUR.findall(textes["ordre-exploratoire-ii-b-v1-brouillon1.md"])):
        arret("ordre : ensemble des marqueurs changé")
    sorties = {f: f.replace("-brouillon1.md", "-brouillon2.md") for f in FICHIERS}
    for s in sorties.values():
        if (d / s).exists():
            arret(f"{s} existe déjà (R12)")
    for ligne in journal:
        print(ligne)
    print(f"marqueurs de l'ordre : {len(set(MARQUEUR.findall(textes['ordre-exploratoire-ii-b-v1-brouillon1.md'])))} distincts")
    for f in FICHIERS:
        print(f"{f}\tavant {avant[f]}\t{sorties[f]}\taprès {sha(textes[f].encode('utf-8'))}")
    if ecrire:
        for f in FICHIERS:
            (d / sorties[f]).write_bytes(textes[f].encode("utf-8"))
        print("ÉCRIT : quatre fichiers neufs")
    else:
        print("ESSAI À BLANC : rien n'est écrit")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
