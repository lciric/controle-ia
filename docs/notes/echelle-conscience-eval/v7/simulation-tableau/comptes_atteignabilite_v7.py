#!/usr/bin/env python3
"""Comptes du brouillon v8 tirés de la sortie scellée `atteignabilite-echelle-v7.json` (lignée « session-depot »,
27 octobre 2026) : issues atteintes parmi les 26 noms possibles ; lectures « positif » ou « inverse » sous H_0 (classes
du texte) ; comparaison aux 17 cases communes avec la simulation v6 (règle v6 sur les mêmes analyses : voir l'audit).
    python -I -B comptes_atteignabilite_v7.py ATTEIGNABILITE_V7_JSON ATTEIGNABILITE_V6_JSON"""
import collections
import json
import re
import sys

sim = json.load(open(sys.argv[1], encoding="utf-8"))
v6 = json.load(open(sys.argv[2], encoding="utf-8"))
base = lambda l: re.sub(r" \(\d+ réserve\(s\)\)$", "", l)
F = ("fuite de signe inverse (petit)", "fuite de signe inverse (grand)", "fuite de signe inverse (petit et grand)")
PRONONCES = F + ("positif", "inverse", "pas de fuite", "nul")
NOMS = list(PRONONCES) + [f"{x} non confirmé (sens {s})" for x in PRONONCES for s in ("a→b", "b→a")] + [
    "désaccord des deux sens", "indécis", "non certifiable", "certification asymétrique (grand seulement)",
    "certification asymétrique (petit seulement)"]
atteintes = collections.Counter(base(e["lecture"]) for e in sim["detail"])
print(f"noms possibles : {len(NOMS)} ; atteints : {sum(1 for n in NOMS if atteintes[n])}")
print("non atteints :", [n for n in NOMS if not atteintes[n]])
print("hors liste :", [n for n in atteintes if n not in NOMS])


def classe(nom):
    if nom.startswith("H0 (0,5 et 0,5), jeu "):
        return "H_0, signatures croisées de signes opposés (v7)"
    if nom.startswith("H0 (0,5 et 0,5)") or nom.startswith("pas de fuite"):
        return "H_0 et sans fuite"
    if nom.startswith("signatures croisées"):
        return "signatures croisées de même signe, α = 0"
    if nom.startswith("signature ") and "(0 et 0)" in nom:
        return "signature d'un seul jeu, α = 0"
    if nom.startswith("signatures des deux jeux"):
        return "double signature, α = 0"
    return None


par = collections.defaultdict(collections.Counter)
for e in sim["detail"]:
    c = classe(e["cas"].rsplit(" ; tau ", 1)[0])
    if c:
        par[c]["analyses"] += 1
        if base(e["lecture"]) in ("positif", "inverse"):
            par[c][base(e["lecture"])] += 1
for c, k in par.items():
    print(f"{c} : {dict(k)}")
# cases communes avec la v6 : mêmes clés, mêmes graines
communes = [k for k in v6["comptes"] if k in sim["comptes"]]
diff = [k for k in communes if sim["comptes"][k] != v6["comptes"][k]]
print(f"cases communes avec la simulation v6 : {len(communes)} ; lectures différentes dans {len(diff)} :")
for k in diff:
    print(f"  {k} : v6 {v6['comptes'][k]} → v7 {sim['comptes'][k]}")
