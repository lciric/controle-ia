#!/usr/bin/env python3
"""Comptes et audit R4 du brouillon v9, tirés de la sortie scellée `atteignabilite-echelle-v8.json` (lignée
« session-depot », 27 octobre 2026 ; CLT-01, CLT-02, CLT-05). Non décisif ; aucune analyse refaite :
  1. issues atteintes parmi les 27 noms possibles (« désaccord des deux sens (cohérence) » compris) ;
  2. R3 : lectures « positif » et « inverse » sous H_0, par classe, et combien portent une réserve de la v8 ; « nul »
     sous H_A compensé ;
  3. les 386 analyses communes avec la simulation v7 (mêmes clés, mêmes graines) : lectures identiques au nom du
     désaccord près ? réserves de la v8 ajoutées, par classe ;
  4. prix des deux réserves sous des vérités sans signature et à contextes égaux ;
  5. prix de la cohérence sous H_0 à contextes inégaux (CLT-02).
    python -I -B comptes_et_audit_v8.py ATTEIGNABILITE_V8_JSON ATTEIGNABILITE_V7_JSON"""
import collections
import json
import re
import sys

sim = json.load(open(sys.argv[1], encoding="utf-8"))
v7 = json.load(open(sys.argv[2], encoding="utf-8"))
base = lambda l: re.sub(r" \(\d+ réserve\(s\)\)$", "", l)
nom = lambda e: e["cas"].rsplit(" ; tau ", 1)[0]
R1, R2 = "le λ du ", "jeux de force de contexte inégale"
r1 = lambda e: any(r.startswith(R1) for r in e["reserves"])
r2 = lambda e: any(r.startswith(R2) for r in e["reserves"])
F = ("fuite de signe inverse (petit)", "fuite de signe inverse (grand)", "fuite de signe inverse (petit et grand)")
PRONONCES = F + ("positif", "inverse", "pas de fuite", "nul")
NOMS = list(PRONONCES) + [f"{x} non confirmé (sens {s})" for x in PRONONCES for s in ("a→b", "b→a")] + [
    "désaccord des deux sens", "désaccord des deux sens (cohérence)", "indécis", "non certifiable",
    "certification asymétrique (grand seulement)", "certification asymétrique (petit seulement)"]

print("== 1. issues atteintes")
atteintes = collections.Counter(base(e["lecture"]) for e in sim["detail"])
print(f"analyses : {len(sim['detail'])} ; noms possibles : {len(NOMS)} ; atteints : {sum(1 for n in NOMS if atteintes[n])}")
print("non atteints :", [n for n in NOMS if not atteintes[n]])
print("hors liste :", [n for n in atteintes if n not in NOMS])

V8_B = ("H0 (0,6 et 0,4), jeu", "H0 (0,55 et 0,4), jeu", "H0 (0,4 et 0,6), jeu")
V8_D = ("H0 (0,7 et 0,7), contexte du jeu b × 1,333, jeu", "H0 (0,7 et 0,7), contexte du jeu b × 0,75, jeu")
V8_C = ("H1 (0,65 et 0,35), jeu", "H1 (0,7 et 0,35), jeu")


def classe(n):
    if n.startswith(V8_B):
        return "v8 B : H_0 à écart vrai sous δ, signatures croisées de signes opposés"
    if n == "H0 (0,6 et 0,4), d 256":
        return "v8 B, témoin : H_0 à écart vrai sous δ, sans signature"
    if n.startswith(V8_D):
        return "v8 D : fuite égale, contexte inégal, signatures croisées"
    if n.startswith(V8_C):
        return "v8 C : H_A compensé par des signatures croisées"
    if n == "H1 (0,65 et 0,35), d 256":
        return "v8 C, témoin : H_A (0,65 et 0,35) sans signature"
    if n.startswith(("H0 (0,5 et 0,5), contexte", "H0 (0,7 et 0,7), contexte", "H0 (0,9 et 0,9), contexte")):
        return "H_0 à contextes inégaux, sans signature (v7, v8)"
    if n.startswith("H0 (0,5 et 0,5), jeu "):
        return "v7 : H_0, signatures croisées de signes opposés"
    if n.startswith("H0 (0,5 et 0,5)") or n.startswith("pas de fuite"):
        return "H_0 et sans fuite"
    if n.startswith("signatures croisées"):
        return "signatures croisées de même signe, α = 0"
    if n.startswith("signature ") and "(0 et 0)" in n:
        return "signature d'un seul jeu, α = 0"
    if n.startswith("signatures des deux jeux"):
        return "double signature, α = 0"
    return None


print("\n== 2. R3 et voisins de cl6 : lectures prononcées par classe (avec réserve v8 : λ change | contexte inégal | l'une ou l'autre | aucune)")
par = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))
for e in sim["detail"]:
    c = classe(nom(e))
    if not c:
        continue
    b = base(e["lecture"])
    par[c]["analyses"]["n"] += 1
    if b in ("positif", "inverse", "nul"):
        k = par[c][b]
        k["n"] += 1
        k["λ change"] += r1(e)
        k["contexte inégal"] += r2(e)
        k["l'une ou l'autre"] += r1(e) or r2(e)
        k["aucune"] += not (r1(e) or r2(e))
for c in sorted(par):
    d = {k: dict(v) for k, v in par[c].items()}
    print(f"{c} : {d}")
print("lectures fausses sans réserve v8, détail :")
for e in sim["detail"]:
    c = classe(nom(e))
    b = base(e["lecture"])
    faux = (c and c.startswith(("v8 B :", "v8 D :")) and b in ("positif", "inverse")) or \
           (c and c.startswith("v8 C :") and b == "nul")
    if faux and not (r1(e) or r2(e)):
        print(f"  {e['cas']} graine {e['graine']} : {b} ; e = {e['ecart_sens']} {e['ecart_sens_ic']} ; q = {e['rapport_Ec']}")

print("\n== 3. analyses communes avec la simulation v7")
d7 = {(x["cas"], x["graine"]): x for x in v7["detail"]}
communes = [e for e in sim["detail"] if (e["cas"], e["graine"]) in d7]
renommees, autres, ajout = 0, [], collections.Counter()
for e in communes:
    a, b = base(d7[(e["cas"], e["graine"])]["lecture"]), base(e["lecture"])
    if a != b:
        if a == "désaccord des deux sens" and b == "désaccord des deux sens (cohérence)":
            renommees += 1
        else:
            autres.append((e["cas"], e["graine"], a, b))
    n7, n8 = len(d7[(e["cas"], e["graine"])]["reserves"]), len(e["reserves"])
    if n8 != n7:
        ajout[(classe(nom(e)) or nom(e), b, "λ change" if r1(e) else "", "contexte inégal" if r2(e) else "")] += 1
print(f"analyses communes : {len(communes)} ; « désaccord des deux sens » renommé « (cohérence) » : {renommees} ; "
      f"autres lectures différentes : {len(autres)}")
for x in autres:
    print("  ", x)
print("réserves v8 ajoutées (classe ou cas, lecture, réserves) :")
for k, n in sorted(ajout.items(), key=lambda kv: -kv[1]):
    print(f"  {n} × {k}")

print("\n== 4. prix des réserves v8 sous des vérités sans signature, à contextes égaux")
PROPRES = ("H0 (0,5 et 0,5)", "pas de fuite (0 et 0)", "H1 (1,0 et 0,2)", "H1 faible (0,6 et 0,2)",
           "inverse (0,2 et 1,0)", "signe inverse (−0,6 et 0)", "fuite faible égale (0,2 et 0,2)",
           "H0 (0,5 et 0,5), d 256", "H1 (1,0 et 0,2), d 256", "H0 (0,6 et 0,4), d 256", "H1 (0,65 et 0,35), d 256")
prix = collections.defaultdict(collections.Counter)
for e in sim["detail"]:
    if nom(e) in PROPRES:
        b = base(e["lecture"])
        if b in ("positif", "inverse", "nul"):
            prix[b]["n"] += 1
            prix[b]["λ change"] += r1(e)
            prix[b]["contexte inégal"] += r2(e)
            prix[b]["l'une ou l'autre"] += r1(e) or r2(e)
print({k: dict(v) for k, v in prix.items()})

print("\n== 5. prix de la cohérence sous H_0 à contextes inégaux (CLT-02)")
for e_nom in sorted({nom(e) for e in sim["detail"] if classe(nom(e)) == "H_0 à contextes inégaux, sans signature (v7, v8)"}):
    k = collections.Counter()
    for e in sim["detail"]:
        if nom(e) == e_nom:
            b = base(e["lecture"])
            k[b + (" (contexte inégal)" if r2(e) else "")] += 1
    print(f"  {e_nom} : {dict(k)}")
