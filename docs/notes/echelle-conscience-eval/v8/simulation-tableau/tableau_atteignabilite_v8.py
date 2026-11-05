#!/usr/bin/env python3
"""Tableau d'atteignabilité du brouillon v9, tiré de la sortie scellée `atteignabilite-echelle-v8.json` (lignée
« session-depot », 27 octobre 2026). Copie de `tableau_atteignabilite_v7.py` (R12). Aucune transcription à la main
des comptes : chaque case liste les lectures de la case, par nombre décroissant, puis par nom ; entre parenthèses, le
nombre de ces lectures qui portent au moins une réserve, et, après « v8 », celles qui portent au moins une des deux
réserves nouvelles de la v8 (« λ change d'un sens à l'autre », « jeux de force de contexte inégale » ; CLT-01).
Libellés des trente cas de la v6 : ceux du tableau du brouillon v7 ; cas de la v7 : tirés de leur nom (CLU-01) ; cas
de la v8 : tirés de leur nom, en gras (CLT-01, CLT-02).
    python -I -B tableau_atteignabilite_v8.py ATTEIGNABILITE_V8_JSON
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


N_V7 = 30 + 25        # cas de la v6, puis de la v7, dans l'ordre de la simulation
V8 = ("le λ du ", "jeux de force de contexte inégale")


def libelle(nom, v8):
    x = nom.replace("H0 ", "H_0 ").replace("H1 ", "H_A ").replace(" au petit", " au 8B").replace(" au grand", " au 70B")
    x = re.sub(r", d (64|256)$", r" ; dimension \1", x)
    x = re.sub(r"^(H_0 \(0,5 et 0,5\)), (jeu .*)$", r"\1 ; signatures croisées de signes opposés : \2", x)
    x = x.replace("), ", ") ; ", 1)
    if not v8:
        return f"{x} (CLU-01)"
    signature = re.search(r"jeu [ab] [+−]", nom)            # « jeu a +0,6 au petit » ; pas « contexte du jeu b »
    cl = "CLT-01" if signature else ("CLT-02" if "contexte" in nom else "CLT-01, témoin")
    return f"**{x}** ({cl})"


def case(entrees):
    total, avec, avec8 = collections.Counter(), collections.Counter(), collections.Counter()
    for e in entrees:
        base = re.sub(r" \(\d+ réserve\(s\)\)$", "", e["lecture"])
        total[base] += 1
        if e["reserves"]:
            avec[base] += 1
        if any(r.startswith(V8) for r in e["reserves"]):
            avec8[base] += 1
    morceaux = sorted(total.items(), key=lambda kv: (-kv[1], kv[0]))
    def note(k):
        if not avec[k]:
            return ""
        return f" ({avec[k]}" + (f" ; v8 {avec8[k]}" if avec8[k] else "") + ")"
    return ", ".join(f"{k} {n}{note(k)}" for k, n in morceaux)


def principal(argv):
    sim = json.loads(open(argv[0], encoding="utf-8").read())
    noms = []
    for e in sim["detail"]:
        nom = e["cas"].rsplit(" ; tau ", 1)[0]
        if nom not in noms:
            noms.append(nom)
    assert len(noms) >= N_V7
    par_cle = collections.defaultdict(list)
    for e in sim["detail"]:
        par_cle[e["cas"]].append(e)
    print("| vérité (α au 8B et au 70B) | tau 0,15 | tau 0,4 | tau 0,8 |")
    print("|---|---|---|---|")
    for i, nom in enumerate(noms):
        lib = LIBELLES_V6[i] if i < len(LIBELLES_V6) else libelle(nom, i >= N_V7)
        cases = [case(par_cle[f"{nom} ; tau {t}"]) if f"{nom} ; tau {t}" in par_cle else "—" for t in TAUS]
        print(f"| {lib} | " + " | ".join(cases) + " |")


if __name__ == "__main__":
    principal(sys.argv[1:])
