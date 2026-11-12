"""Grille des lignes L du critère 3 de T0.7 (brouillon 8, CLT7B-01) : rejeu du produit complet des entrées.

Entrées (section « Critères de lecture gelés » du brouillon 8) :
- G : garde d'ouverture et d'identité (ok, garde-echec, 7a) ;
- P : issue du fichier d'issue de P3-bis (absente, non lu, échec, non vu, non tranché, vu) ;
- A : table A de T0.6 (absent, arret, A1, A1b, A2, A3, A4, A5) ;
- I, II : état de l'organisme (i) et de l'organisme (ii) sur ses sondes principales lues (U, N, Z, E) ;
- F : fuite nommée par l'audit R7a ou R9a sur un jeu décisif (aucune, (i), (ii), les deux).

Règle : les lignes sont lues de haut en bas, la première qui s'applique ; le script vérifie qu'exactement une ligne
s'applique à chaque cas (aucune zone morte, aucun chevauchement) et imprime les effectifs par ligne.

    python3 -I -B grille_l_t07_brouillon8.py

Bibliothèque standard seule ; aucune donnée lue ; code de sortie 0 si la grille est complète et sans chevauchement, 2 sinon.
"""
from __future__ import annotations

import itertools
import sys

G = ("ok", "garde-echec", "7a")
P = ("absente", "non lu", "échec", "non vu", "non tranché", "vu")
A = ("absent", "arret", "A1", "A1b", "A2", "A3", "A4", "A5")
ETATS = ("U", "N", "Z", "E")
F = ("aucune", "(i)", "(ii)", "les deux")

ORDRE = ("R11-arret", "R12-invalide", "L0a", "L0b", "L0c", "L1", "L1b", "L6", "L4", "L4b", "L5", "L2", "L3")


def regles(g: str, p: str, a: str, i: str, ii: str, f: str) -> list[str]:
    """Toutes les lignes dont la condition est vraie, dans l'ordre de la table (sans règle de première ligne)."""
    vraies = []
    if g == "garde-echec":
        vraies.append("R11-arret")
    if g == "7a":
        vraies.append("R12-invalide")
    if g == "ok":
        if p in ("absente", "non lu", "échec"):
            vraies.append("L0a")
        if p == "non vu":
            vraies.append("L0b")
        if p == "non tranché":
            vraies.append("L0c")
        if p == "vu":
            if a in ("absent", "arret", "A1"):
                vraies.append("L1")
            if a in ("A1b", "A2", "A3"):
                vraies.append("L1b")            # ses sous-phrases (fuite (i), N, U, Z, E) couvrent tout (i) et sont exclusives
            if a in ("A4", "A5"):
                if f != "aucune":
                    vraies.append("L6")
                if i == "Z":
                    vraies.append("L4")
                if i == "E" or (i == "U" and ii == "E"):
                    vraies.append("L4b")
                if i == "N" or (i == "U" and ii == "N"):
                    vraies.append("L5")
                if i == "U" and ii == "U":
                    vraies.append("L2")
                if i == "U" and ii == "Z":
                    vraies.append("L3")
    return vraies


def premiere(vraies: list[str]) -> str:
    return next(l for l in ORDRE if l in vraies)


def main() -> int:
    effectifs = {l: 0 for l in ORDRE}
    trous, chevauchements = [], []
    total = 0
    for cas in itertools.product(G, P, A, ETATS, ETATS, F):
        total += 1
        v = regles(*cas)
        if not v:
            trous.append(cas)
            continue
        # chevauchement « vrai » : deux lignes vraies dont aucune n'est une garde préalable (L6 précède L4 à L3 par
        # construction : la fuite est une entrée à part ; tout autre doublon est un défaut de la grille)
        sans_garde = [l for l in v if l not in ("R11-arret", "R12-invalide", "L6")]
        if len(sans_garde) > 1:
            chevauchements.append((cas, v))
        effectifs[premiere(v)] += 1
    print(f"cas énumérés : {total} (= {len(G)} × {len(P)} × {len(A)} × {len(ETATS)} × {len(ETATS)} × {len(F)})")
    for l in ORDRE:
        print(f"  {l:13s} {effectifs[l]:6d}")
    print(f"trous : {len(trous)}")
    for c in trous[:10]:
        print("  ", c)
    print(f"chevauchements hors gardes et L6 : {len(chevauchements)}")
    for c, v in chevauchements[:10]:
        print("  ", c, v)
    sous_a4a5 = sum(effectifs[l] for l in ("L6", "L4", "L4b", "L5", "L2", "L3"))
    attendu = len(A[6:]) * len(ETATS) * len(ETATS) * len(F)       # G ok, P vu, A4 ou A5
    print(f"cas A4/A5 sous P = vu, G = ok : {sous_a4a5} (attendu {attendu})")
    ok = not trous and not chevauchements and sous_a4a5 == attendu and sum(effectifs.values()) == total
    print("GRILLE COMPLÈTE, SANS ZONE MORTE NI CHEVAUCHEMENT" if ok else "GRILLE EN DÉFAUT")
    return 0 if ok else 2


if __name__ == "__main__":
    sys.exit(main())
