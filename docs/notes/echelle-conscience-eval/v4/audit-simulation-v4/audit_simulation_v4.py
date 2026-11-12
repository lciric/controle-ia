#!/usr/bin/env python3
"""Audit R4 de la simulation d'atteignabilité v4 (lignée « session-depot », 27 octobre 2026). Non décisif ; lit la
sortie scellée `atteignabilite-echelle-v4.json` et recalcule, sans analyse, les tirages de `fabriquer` (mêmes graines,
même ordre) pour deux contrôles :
  1. Composante fortuite des signatures le long de la direction du contexte C : en dimension 64, la signature d'un jeu
     n'est pas orthogonale à C ; sa composante est une vraie poussée du format le long du concept. λ effectif du
     concept porté par la signature = facteur × cos(signature, C) (|signature| = |C| = 4 ; l'effet du contexte vaut
     |C| à la couche lue).
  2. Ce que la règle de la v3 aurait lu sur les mêmes analyses : sens a→b seul pour « non certifiable »,
     « certification asymétrique », « fuite de signe inverse », « pas de fuite » et « nul » ; « positif » et « inverse »
     confirmés par b→a. La lecture du sens a→b de la v4 suit le même ordre que la v3 ; la règle v3 se déduit donc des
     deux lectures par sens.
    python -I -B audit_simulation_v4.py ATTEIGNABILITE_V4_JSON STIMULI_JSON
"""
import collections
import json
import pathlib
import sys

import numpy as np

SIG = {  # cas : (modèle portant la signature, [(jeu, facteur)])
    "signature du jeu a au petit (0 et 0)": ("petit", [("a", 2.0)]),
    "signature négative du jeu a au petit (0 et 0)": ("petit", [("a", -2.0)]),
    "signature du jeu a au grand (0 et 0)": ("grand", [("a", 2.0)]),
    "signature du jeu b au petit (0 et 0)": ("petit", [("b", 2.0)]),
    "signatures des deux jeux au petit (0 et 0)": ("petit", [("a", 2.0), ("b", 2.0)]),
    "H1 masqué par une signature négative du jeu a (1,0 et 0,2)": ("petit", [("a", -3.0)]),
    "fuite masquée par une signature négative du jeu a (0,6 et 0)": ("petit", [("a", -1.4)]),
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


def regle_v3(ab, ba):
    if ab in ("positif", "inverse"):
        return ab if ba == ab else f"{ab} non confirmé (sens b→a)"
    return ab


def principal(argv):
    sim = json.loads(pathlib.Path(argv[0]).read_text(encoding="utf-8"))
    st = json.loads(pathlib.Path(argv[1]).read_text(encoding="utf-8"))["stimuli"]
    print(f"sortie relue : {argv[0]} ; commit {sim['commit_scripts']} ; {len(sim['detail'])} analyses")
    print("\n1. Composante des signatures le long de C, et lectures (v4 ; règle v3 sur les mêmes analyses)")
    changes = collections.Counter()
    for e in sim["detail"]:
        nom, tau = e["cas"].rsplit(" ; tau ", 1)
        ps = e["lecture_par_sens"]
        v3 = regle_v3(ps["a→b"], ps["b→a"]) if ps else "arrêt"
        lecture_v4 = e["lecture"].split(" (")[0] if "réserve" in e["lecture"] else e["lecture"]
        if v3 != lecture_v4:
            changes[(nom, v3, lecture_v4)] += 1
        if nom in SIG:
            modele, sigs = SIG[nom]
            C, sig = tirages(st, e["graine"] + (1 if modele == "grand" else 0), float(tau))
            eff = sum(f * float(sig[j] @ C) for j, f in sigs)
            cosinus = ", ".join(f"cos(sig_{j}, C) {float(sig[j] @ C):+.3f}" for j, _ in sigs)
            print(f"  {nom} ; tau {tau} ; graine {e['graine']} ; {cosinus} ; λ effectif porté au {modele} {eff:+.3f}"
                  f" ; v4 : {e['lecture']} ; règle v3 : {v3} ; par sens : {ps['a→b']} / {ps['b→a']}")
    print("\n2. Lectures qui changent entre la règle v3 et la v4 (toutes les analyses)")
    for (nom, v3, v4), n in sorted(changes.items()):
        print(f"  {nom} : règle v3 « {v3} » → v4 « {v4} » ({n})")
    return 0


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
