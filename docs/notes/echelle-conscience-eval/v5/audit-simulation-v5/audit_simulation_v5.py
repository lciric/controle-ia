#!/usr/bin/env python3
"""Audit R4 de la simulation d'atteignabilité v5 (lignée « session-depot », 27 octobre 2026). Non décisif ; lit la
sortie scellée `atteignabilite-echelle-v5.json` et recalcule, sans analyse, les tirages de `fabriquer` (mêmes graines,
même ordre) pour deux contrôles :
  1. Composante fortuite des signatures le long de la direction du contexte C (dimension 64) : λ effectif du concept
     porté par la signature = somme des facteurs × cos(signature du jeu, C) (|signature| = |C| = 4).
  2. Ce que la règle de la v4 (comparaison des premières issues de chaque sens) aurait lu sur les mêmes analyses,
     contre la lecture v5 (première issue tenue dans les deux sens, CLW-01) ; la règle v4 se déduit des lectures par
     sens consignées.
    python -I -B audit_simulation_v5.py ATTEIGNABILITE_V5_JSON STIMULI_JSON
"""
import collections
import json
import pathlib
import sys

import numpy as np

CERTIFICATION = ("non certifiable", "certification asymétrique (grand seulement)",
                 "certification asymétrique (petit seulement)")
ISSUES = ("fuite de signe inverse", "positif", "inverse", "pas de fuite", "nul")
SIG = {  # cas : (modèle portant la signature, [(jeu, facteur)])
    "signature du jeu a au petit (0 et 0)": ("petit", [("a", 2.0)]),
    "signature négative du jeu a au petit (0 et 0)": ("petit", [("a", -2.0)]),
    "signature du jeu a au grand (0 et 0)": ("grand", [("a", 2.0)]),
    "signature du jeu b au petit (0 et 0)": ("petit", [("b", 2.0)]),
    "signatures des deux jeux au petit (0 et 0)": ("petit", [("a", 2.0), ("b", 2.0)]),
    "H1 masqué par une signature négative du jeu a (1,0 et 0,2)": ("petit", [("a", -3.0)]),
    "fuite masquée par une signature négative du jeu a (0,6 et 0)": ("petit", [("a", -1.4)]),
    "signature négative du jeu a au grand (0 et 0)": ("grand", [("a", -2.0)]),
    "signatures des deux jeux, négatives, au petit (0 et 0)": ("petit", [("a", -2.0), ("b", -2.0)]),
    "signatures des deux jeux au grand (0 et 0)": ("grand", [("a", 2.0), ("b", 2.0)]),
}


def tirages(st, graine, tau, d=64):
    rng = np.random.default_rng(graine)
    C = np.linalg.qr(rng.normal(size=(d, 3)))[0].T[0]
    rng.normal(size=(64, d))
    cadrage = {}
    for s in st:
        k = (s["jeu"], s["paire"], s["classe"])
        if k not in cadrage:
            cadrage[k] = rng.normal(size=d) * tau
    sig = {}
    for jeu in ("a", "b"):
        v = sum(cadrage[(jeu, j, "eval")] - cadrage[(jeu, j, "reel")] for j in range(6)) / 6
        sig[jeu] = v / np.linalg.norm(v)
    return C, sig


def regle_v4(ab, ba):
    if ab == ba:
        return ab
    genre = [("certification" if L in CERTIFICATION else "issue" if L in ISSUES else "indécis") for L in (ab, ba)]
    if genre == ["certification", "certification"]:
        return "non certifiable"
    if "issue" not in genre:
        return "indécis"
    if genre == ["issue", "issue"]:
        return "désaccord des deux sens"
    return f"{ab} non confirmé (sens b→a)" if genre[0] == "issue" else f"{ba} non confirmé (sens a→b)"


def principal(argv):
    sim = json.loads(pathlib.Path(argv[0]).read_text(encoding="utf-8"))
    st = json.loads(pathlib.Path(argv[1]).read_text(encoding="utf-8"))["stimuli"]
    print(f"sortie relue : {pathlib.Path(argv[0]).name} ; commit {sim['commit_scripts']} ; {len(sim['detail'])} analyses")
    print("\n1. Composante des signatures le long de C ; lectures v5 (règle v4 sur les mêmes analyses)")
    changes = collections.Counter()
    for e in sim["detail"]:
        nom, tau = e["cas"].rsplit(" ; tau ", 1)
        ps = e["lecture_par_sens"]
        v4 = regle_v4(ps["a→b"], ps["b→a"]) if ps else "arrêt"
        v5 = e["lecture"].split(" (")[0] if "réserve" in e["lecture"] else e["lecture"]
        if v4 != v5:
            changes[(nom, v4, v5)] += 1
        if nom in SIG:
            modele, sigs = SIG[nom]
            C, sig = tirages(st, e["graine"] + (1 if modele == "grand" else 0), float(tau))
            eff = sum(f * float(sig[j] @ C) for j, f in sigs)
            cosinus = ", ".join(f"cos(sig_{j}, C) {float(sig[j] @ C):+.3f}" for j, _ in sigs)
            print(f"  {nom} ; tau {tau} ; graine {e['graine']} ; {cosinus} ; λ effectif porté au {modele} {eff:+.3f}"
                  f" ; v5 : {e['lecture']} {e['reserves']} ; règle v4 : {v4} ; issues par sens : {e['issues_tenues_par_sens']}")
    print("\n2. Lectures qui changent entre la règle v4 et la v5 (toutes les analyses)")
    for (nom, v4, v5), n in sorted(changes.items()):
        print(f"  {nom} : règle v4 « {v4} » → v5 « {v5} » ({n})")
    if not changes:
        print("  aucune")
    return 0


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
