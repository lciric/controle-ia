#!/usr/bin/env python3
"""Tableau d'atteignabilité du brouillon v8, tiré de la sortie scellée `atteignabilite-echelle-v7.json` (lignée
« session-depot », 27 octobre 2026). Aucune transcription à la main des comptes : chaque case liste les lectures de
la case, par nombre décroissant, puis par nom ; entre parenthèses, le nombre de ces lectures qui portent au moins une
réserve. Libellés des trente cas de la v6 : ceux du tableau du brouillon v7, dans l'ordre de la simulation ; cas de la
v7 : libellé tiré de leur nom dans la simulation, en gras.
    python -I -B tableau_atteignabilite_v7.py ATTEIGNABILITE_V7_JSON
"""
import collections
import json
import re
import sys

LIBELLES_V6 = [
    "H_0 (0,5 et 0,5)", "pas de fuite (0 et 0)", "H_A (1,0 et 0,2)", "H_A faible (0,6 et 0,2)", "inverse (0,2 et 1,0)",
    "signe inverse (−0,6 et 0)", "signature du jeu a au 8B (+2), α = 0 (CLY-01)", "contexte faible aux deux tailles",
    "contexte faible au 8B", "signature du jeu a au 8B, négative (−2), α = 0 (CLZ-01)",
    "signature du jeu a au 70B (+2), α = 0", "signature du jeu b au 8B (+2), α = 0",
    "signatures des deux jeux au 8B (+2 et +2), α = 0 (CLZ-08)",
    "H_A masqué par une signature négative du jeu a (1,0 et 0,2 ; −3)",
    "fuite masquée par une signature négative du jeu a (0,6 et 0 ; −1,4)", "contexte faible au 70B",
    "fuite faible et égale (0,2 et 0,2) (CLW-01)",
    "fuite faible et égale, contexte du jeu b plus faible (0,15 et 0,15 ; jeu b × 0,6) (CLW-01)",
    "signature du jeu a au 70B, négative (−2), α = 0 (CLW-09)",
    "signatures des deux jeux au 8B, négatives (−2 et −2), α = 0 (CLW-02)",
    "signatures des deux jeux au 70B (+2 et +2), α = 0 (CLW-02)",
    "signatures croisées négatives : jeu a au 8B, jeu b au 70B (−2 et −2), α = 0 (CLV-01)",
    "signatures croisées négatives : jeu b au 8B, jeu a au 70B (−2 et −2), α = 0 (CLV-01)",
    "signatures croisées positives : jeu a au 8B, jeu b au 70B (+2 et +2), α = 0 (CLV-01)",
    "signatures croisées positives : jeu b au 8B, jeu a au 70B (+2 et +2), α = 0 (CLV-01)",
    "signature du jeu b au 8B, négative (−2), α = 0 (CLV-04)", "signature du jeu b au 70B (+2), α = 0 (CLV-04)",
    "signature du jeu b au 70B, négative (−2), α = 0 (CLV-04)",
    "H_A sous les signatures des deux jeux au 8B, négatives (1,0 et 0,2 ; −2 et −2) (CLV-04)",
    "H_A sous des signatures croisées de signes opposés (1,0 et 0,2 ; jeu a −2 au 8B, jeu b +2 au 70B) (CLV-04)"]
TAUS = ("0.15", "0.4", "0.8")


def libelle_v7(nom):
    x = nom.replace("H0 ", "H_0 ").replace("H1 ", "H_A ").replace(" au petit", " au 8B").replace(" au grand", " au 70B")
    x = re.sub(r", d (64|256)$", r" ; dimension \1", x)
    x = re.sub(r"^(H_0 \(0,5 et 0,5\)), (jeu .*)$", r"\1 ; signatures croisées de signes opposés : \2", x)
    x = x.replace("), ", ") ; ", 1)
    return f"**{x}** (CLU-01)"


def case(compte):
    total, avec = collections.Counter(), collections.Counter()
    for lecture, n in compte.items():
        base = re.sub(r" \(\d+ réserve\(s\)\)$", "", lecture)
        total[base] += n
        if base != lecture:
            avec[base] += n
    morceaux = sorted(total.items(), key=lambda kv: (-kv[1], kv[0]))
    return ", ".join(f"{k} {n}" + (f" ({avec[k]})" if avec[k] else "") for k, n in morceaux)


def principal(argv):
    sim = json.loads(open(argv[0], encoding="utf-8").read())
    noms = []
    for e in sim["detail"]:
        nom = e["cas"].rsplit(" ; tau ", 1)[0]
        if nom not in noms:
            noms.append(nom)
    assert len(noms) >= len(LIBELLES_V6)
    print("| vérité (α au 8B et au 70B) | tau 0,15 | tau 0,4 | tau 0,8 |")
    print("|---|---|---|---|")
    for i, nom in enumerate(noms):
        lib = LIBELLES_V6[i] if i < len(LIBELLES_V6) else libelle_v7(nom)
        cases = [case(sim["comptes"][f"{nom} ; tau {t}"]) if f"{nom} ; tau {t}" in sim["comptes"] else "—"
                 for t in TAUS]
        print(f"| {lib} | " + " | ".join(cases) + " |")


if __name__ == "__main__":
    principal(sys.argv[1:])
