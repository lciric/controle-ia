#!/usr/bin/env python3
"""Audit R4 de la simulation d'atteignabilité v6 (lignée « session-depot », 27 octobre 2026). Non décisif ; lit la
sortie scellée `atteignabilite-echelle-v6.json` et recalcule, sans analyse, les tirages de `fabriquer` (mêmes graines,
même ordre) pour deux contrôles :
  1. Composante fortuite des signatures le long de la direction du contexte C (dimension 64), pour chaque modèle qui en
     porte une : λ effectif du concept porté par la signature = somme des facteurs × cos(signature du jeu, C)
     (|signature| = |C| = 4).
  2. Ce que la règle de la v5 (fuite de signe inverse tenue dans un sens dès qu'un modèle est sous −δ, combinaison par
     l'étiquette seule) aurait lu sur les mêmes analyses, contre la lecture v6 (fuite de signe inverse lue modèle par
     modèle, CLV-01). La règle v5 se déduit exactement des issues tenues par sens, consignées : les deux fuites de signe
     inverse d'un sens y deviennent une seule issue ; les réserves ne sont pas recalculées. Une lecture ne « change »
     que si la décision change : la taille nommée par la v6 seule ne compte pas comme un changement.
    python -I -B audit_simulation_v6.py ATTEIGNABILITE_V6_JSON STIMULI_JSON
"""
import collections
import json
import pathlib
import re
import sys

import numpy as np

CERTIFICATION = ("non certifiable", "certification asymétrique (grand seulement)",
                 "certification asymétrique (petit seulement)")
FSI_V6 = ("fuite de signe inverse (petit)", "fuite de signe inverse (grand)")
ISSUES_V5 = ("fuite de signe inverse", "positif", "inverse", "pas de fuite", "nul")
SIG = {  # cas : {modèle : [(jeu, facteur)]}
    "signature du jeu a au petit (0 et 0)": {"petit": [("a", 2.0)]},
    "signature négative du jeu a au petit (0 et 0)": {"petit": [("a", -2.0)]},
    "signature du jeu a au grand (0 et 0)": {"grand": [("a", 2.0)]},
    "signature du jeu b au petit (0 et 0)": {"petit": [("b", 2.0)]},
    "signatures des deux jeux au petit (0 et 0)": {"petit": [("a", 2.0), ("b", 2.0)]},
    "H1 masqué par une signature négative du jeu a (1,0 et 0,2)": {"petit": [("a", -3.0)]},
    "fuite masquée par une signature négative du jeu a (0,6 et 0)": {"petit": [("a", -1.4)]},
    "signature négative du jeu a au grand (0 et 0)": {"grand": [("a", -2.0)]},
    "signatures des deux jeux, négatives, au petit (0 et 0)": {"petit": [("a", -2.0), ("b", -2.0)]},
    "signatures des deux jeux au grand (0 et 0)": {"grand": [("a", 2.0), ("b", 2.0)]},
    "signatures croisées négatives, jeu a au petit, jeu b au grand (0 et 0)": {"petit": [("a", -2.0)],
                                                                               "grand": [("b", -2.0)]},
    "signatures croisées négatives, jeu b au petit, jeu a au grand (0 et 0)": {"petit": [("b", -2.0)],
                                                                               "grand": [("a", -2.0)]},
    "signatures croisées positives, jeu a au petit, jeu b au grand (0 et 0)": {"petit": [("a", 2.0)],
                                                                               "grand": [("b", 2.0)]},
    "signatures croisées positives, jeu b au petit, jeu a au grand (0 et 0)": {"petit": [("b", 2.0)],
                                                                               "grand": [("a", 2.0)]},
    "signature négative du jeu b au petit (0 et 0)": {"petit": [("b", -2.0)]},
    "signature du jeu b au grand (0 et 0)": {"grand": [("b", 2.0)]},
    "signature négative du jeu b au grand (0 et 0)": {"grand": [("b", -2.0)]},
    "H1 sous les signatures négatives des deux jeux au petit (1,0 et 0,2)": {"petit": [("a", -2.0), ("b", -2.0)]},
    "H1 sous des signatures croisées de signes opposés (1,0 et 0,2 ; a négatif au petit, b positif au grand)": {
        "petit": [("a", -2.0)], "grand": [("b", 2.0)]},
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


def regle_v5(tenues, lecture_v6):
    """Lecture de la v5 sur les mêmes issues tenues par sens ; None si la v6 a rendu un échec de certification commun
    (même lecture sous les deux règles)."""
    if lecture_v6 in CERTIFICATION:
        return lecture_v6
    t5 = {s: [x for x in ISSUES_V5 if x in [("fuite de signe inverse" if y in FSI_V6 else y) for y in tenues[s]]]
          for s in ("a→b", "b→a")}
    communes = [x for x in ISSUES_V5 if x in t5["a→b"] and x in t5["b→a"]]
    if communes:
        return communes[0]
    if t5["a→b"] and t5["b→a"]:
        return "désaccord des deux sens"
    for s, autre in (("a→b", "b→a"), ("b→a", "a→b")):
        if t5[s]:
            return f"{t5[s][0]} non confirmé (sens {autre})"
    return "indécis"


def sans_taille(lecture):
    """Nom v6 ramené au nom v5, pour comparer les décisions et non les étiquettes."""
    return re.sub(r"fuite de signe inverse \((petit et grand|petit|grand)\)", "fuite de signe inverse", lecture)


def principal(argv):
    sim = json.loads(pathlib.Path(argv[0]).read_text(encoding="utf-8"))
    st = json.loads(pathlib.Path(argv[1]).read_text(encoding="utf-8"))["stimuli"]
    print(f"sortie relue : {pathlib.Path(argv[0]).name} ; commit {sim['commit_scripts']} ; {len(sim['detail'])} analyses")
    print("\n1. Composante des signatures le long de C, par modèle ; lectures v6 (règle v5 sur les mêmes analyses)")
    changes = collections.Counter()
    for e in sim["detail"]:
        nom, tau = e["cas"].rsplit(" ; tau ", 1)
        v6 = e["lecture"].split(" (")[0] if "réserve" in e["lecture"] else e["lecture"]
        if e["issues_tenues_par_sens"] is None:
            v5 = "arrêt"
        else:
            v5 = regle_v5(e["issues_tenues_par_sens"], v6)
        if v5 != sans_taille(v6):
            changes[(nom, tau, v5, v6)] += 1
        if nom in SIG:
            morceaux = []
            for modele, sigs in SIG[nom].items():
                C, sig = tirages(st, e["graine"] + (1 if modele == "grand" else 0), float(tau))
                eff = sum(f * float(sig[j] @ C) for j, f in sigs)
                cos = ", ".join(f"cos(sig_{j}, C) {float(sig[j] @ C):+.3f}" for j, _ in sigs)
                morceaux.append(f"{modele} : {cos}, λ effectif {eff:+.3f}")
            print(f"  {nom} ; tau {tau} ; graine {e['graine']} ; {' ; '.join(morceaux)} ; v6 : {e['lecture']} "
                  f"{e['reserves']} ; règle v5 : {v5} ; issues par sens : {e['issues_tenues_par_sens']}")
    print("\n2. Lectures qui changent entre la règle v5 et la v6 (toutes les analyses)")
    for (nom, tau, v5, v6), n in sorted(changes.items()):
        print(f"  {nom} ; tau {tau} : règle v5 « {v5} » → v6 « {v6} » ({n})")
    if not changes:
        print("  aucune")
    return 0


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
