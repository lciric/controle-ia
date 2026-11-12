"""appliquer_couples_cl1_v1.py — applique par programme les 14 couples C01 à C14 de la contre-lecture 1
(`prereg/contre-lectures/essai-preuve-formelle-devis-v1-brouillon1-cl1.md`) au brouillon 1
(`brouillons/couche4-essai-preuve-formelle-v1/essai-preuve-formelle-devis-v1-brouillon1.md`).

Règles : les couples sont lus dans la contre-lecture elle-même (aucun texte retapé) ; la chaîne « À remplacer » est cherchée
avec les blancs et retours à la ligne normalisés ; elle doit apparaître **exactement une fois** dans le brouillon 1 ; les
quatorze passages ne doivent pas se chevaucher ; les remplacements se font sur le texte d'origine, de la fin vers le début.
Le brouillon 1 n'est pas modifié ; le résultat est écrit au chemin donné en argument. Aucun appel, aucun réseau.

Usage : python appliquer_couples_cl1_v1.py CONTRE_LECTURE BROUILLON1 SORTIE
"""
import hashlib
import re
import sys
from pathlib import Path


def empreinte(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def lire_couples(texte):
    entetes = list(re.finditer(r"^\*\*(C\d\d)\*\* \(([^)]*)\)", texte, re.M))
    couples = []
    for i, m in enumerate(entetes):
        fin = entetes[i + 1].start() if i + 1 < len(entetes) else texte.index("<!-- controle")
        bloc = texte[m.end():fin]
        a = bloc.index("- À remplacer :")
        b = bloc.index("- Par :")

        def citation(segment):
            lignes = []
            for ligne in segment.split("\n"):
                if ligne.startswith("  > "):
                    lignes.append(ligne[4:])
                elif ligne.rstrip() == "  >":
                    lignes.append("")
            return lignes

        ancien = " ".join(citation(bloc[a:b]))
        nouveau = "\n".join(citation(bloc[b:]))
        couples.append((m.group(1), m.group(2), ancien, nouveau))
    return couples


def main(cl, b1, sortie):
    texte_cl = Path(cl).read_text(encoding="utf-8")
    texte = Path(b1).read_text(encoding="utf-8")
    couples = lire_couples(texte_cl)
    assert [c[0] for c in couples] == [f"C{i:02d}" for i in range(1, 15)], [c[0] for c in couples]
    print(f"contre-lecture : {cl} ({empreinte(cl)})")
    print(f"brouillon 1    : {b1} ({empreinte(b1)})")
    portees = []
    for nom, constat, ancien, nouveau in couples:
        motif = r"\s+".join(re.escape(mot) for mot in ancien.split())
        trouves = list(re.finditer(motif, texte))
        assert len(trouves) == 1, f"{nom} : {len(trouves)} occurrence(s)"
        assert "|" not in nouveau or "|" in ancien, f"{nom} : barre verticale introduite"
        portees.append((trouves[0].start(), trouves[0].end(), nom, constat, nouveau))
        print(f"{nom} ({constat}) : 1 occurrence, caractères {trouves[0].start()}–{trouves[0].end()}, "
              f"{len(ancien.split())} mots remplacés par {len(nouveau.split())}")
    portees.sort()
    for (d1, f1, n1, _, _), (d2, f2, n2, _, _) in zip(portees, portees[1:]):
        assert f1 <= d2, f"chevauchement {n1} / {n2}"
    for debut, fin, nom, _, nouveau in reversed(portees):
        texte = texte[:debut] + nouveau + texte[fin:]
    Path(sortie).write_text(texte, encoding="utf-8")
    print(f"sortie         : {sortie} ({empreinte(sortie)})")
    print("14 couples appliqués, 0 défaut d'unicité, 0 chevauchement")


if __name__ == "__main__":
    main(*sys.argv[1:4])
