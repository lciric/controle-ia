#!/usr/bin/env python3
"""Audit R4 de la simulation d'atteignabilité v7 (lignée « session-depot », 27 octobre 2026 ; CLU-01). Non décisif ;
lit la sortie scellée `atteignabilite-echelle-v7.json` et recalcule, sans analyse, les tirages de `fabriquer` (mêmes
graines, même ordre) :
  1. Ce que la règle de la v6 (issue commune par son seul nom, sans la cohérence des deux sens) aurait lu sur les mêmes
     analyses, contre la lecture v7. La règle v6 se déduit exactement des issues tenues par sens, consignées, et de
     l'échec de certification commun ; les réserves ne sont pas recalculées. Toutes les analyses.
  2. Pour chaque analyse des cas de la v7, l'écart du λ de chaque modèle entre les deux sens (point et intervalle) et
     la lecture.
  3. Contrefactuel, non décisif : la règle « les deux modèles » (une issue n'est bloquée que si les DEUX modèles
     rompent la cohérence, |e(m)| > δ chacun) au lieu de la règle v7 (« un seul suffit ») ; pour chaque analyse où la v7
     bloque une issue tenue dans les deux sens, le nombre de modèles qui rompent la cohérence.
  4. Composante fortuite des signatures le long de la direction du contexte C, pour les cas de la v7 qui en portent :
     λ effectif du concept porté par la signature = facteur × cos(signature du jeu, C) (|signature| = |C| = 4), en
     dimension 64 ou 256.
    python -I -B audit_simulation_v7.py ATTEIGNABILITE_V7_JSON STIMULI_JSON
"""
import collections
import json
import pathlib
import re
import sys

import numpy as np

CERTIFICATION = ("non certifiable", "certification asymétrique (grand seulement)",
                 "certification asymétrique (petit seulement)")
FSI = ("fuite de signe inverse (petit)", "fuite de signe inverse (grand)")
ISSUES = FSI + ("positif", "inverse", "pas de fuite", "nul")
ETAPE = {FSI[0]: 1, FSI[1]: 1, "positif": 2, "inverse": 3, "pas de fuite": 4, "nul": 5}
AUTRE = {"a→b": "b→a", "b→a": "a→b"}


def premiere_etape(issues):
    e = min(ETAPE[x] for x in issues)
    etape = [x for x in ISSUES if x in issues and ETAPE[x] == e]
    return "fuite de signe inverse (petit et grand)" if len(etape) == 2 else etape[0]


def regle_v6(tenues, lecture_v7):
    """Lecture de la v6 sur les mêmes issues tenues par sens (sans la cohérence des deux sens)."""
    if lecture_v7 in CERTIFICATION:
        return lecture_v7
    communes = [x for x in ISSUES if x in tenues["a→b"] and x in tenues["b→a"]]
    if communes:
        return premiere_etape(communes)
    if tenues["a→b"] and tenues["b→a"]:
        return "désaccord des deux sens"
    for s in ("a→b", "b→a"):
        if tenues[s]:
            return f"{premiere_etape(tenues[s])} non confirmé (sens {AUTRE[s]})"
    return "indécis"


def tirages(st, graine, tau, d):
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


MOTIF = re.compile(r"jeu (a|b) ([+−])([0-9,]+) au petit, jeu (a|b) ([+−])([0-9,]+) au grand, d (64|256)")


def signatures(nom):
    """{modèle : [(jeu, facteur)]} et dimension, lus dans le nom d'un cas de signatures croisées de la v7."""
    m = MOTIF.search(nom)
    if not m:
        return None, None
    f = lambda sg, v: (1 if sg == "+" else -1) * float(v.replace(",", "."))
    return {"petit": [(m.group(1), f(m.group(2), m.group(3)))], "grand": [(m.group(4), f(m.group(5), m.group(6)))]}, \
        int(m.group(7))


def principal(argv):
    sim = json.loads(pathlib.Path(argv[0]).read_text(encoding="utf-8"))
    st = json.loads(pathlib.Path(argv[1]).read_text(encoding="utf-8"))["stimuli"]
    n_v6 = len(sim["detail"]) - sum(1 for e in sim["detail"] if e["graine"] > 3328)
    print(f"sortie relue : {pathlib.Path(argv[0]).name} ; commit {sim['commit_scripts']} ; {len(sim['detail'])} analyses "
          f"({n_v6} des cas de la v6, graines 3002 à 3328)")
    print("\n1. Lectures qui changent entre la règle v6 (sans la cohérence) et la v7 (toutes les analyses)")
    changes = collections.Counter()
    for e in sim["detail"]:
        nom, tau = e["cas"].rsplit(" ; tau ", 1)
        v7 = re.sub(r" \(\d+ réserve\(s\)\)$", "", e["lecture"])
        v6 = "arrêt" if e["issues_tenues_par_sens"] is None else regle_v6(e["issues_tenues_par_sens"], v7)
        if v6 != v7:
            changes[(nom, tau, v6, v7)] += 1
    if not changes:
        print("  aucune")
    for (nom, tau, v6, v7), n in sorted(changes.items()):
        print(f"  {nom} ; tau {tau} : règle v6 « {v6} » → v7 « {v7} » ({n})")
    print("\n2. Cas de la v7 : écart du λ de chaque modèle entre les deux sens (point, intervalle), lecture")
    for e in sim["detail"]:
        if e["graine"] <= 3328:
            continue
        ep, ei = e["ecart_sens"], e["ecart_sens_ic"]
        txt = " ; ".join(f"{k} {ep[k]:+.3f} [{ei[k][0]:+.3f} ; {ei[k][1]:+.3f}]" for k in ("petit", "grand"))
        print(f"  {e['cas']} ; graine {e['graine']} ; {txt} ; {e['lecture']} ; tenues {e['issues_tenues_par_sens']}")
    print("\n3. Contrefactuel « les deux modèles » : analyses où la cohérence bloque une issue tenue dans les deux sens")
    compte = collections.Counter()
    for e in sim["detail"]:
        cm = e.get("conditions_manquantes") or {}
        bloquees = [k for k in cm if k.endswith("cohérence des deux sens")]
        if not bloquees:
            continue
        n = sum(abs(v) > 0.25 for v in e["ecart_sens"].values())
        compte[(e["cas"], n)] += 1
        print(f"  {e['cas']} ; graine {e['graine']} ; {', '.join(bloquees)} ; modèles qui rompent la cohérence : {n} ; "
              f"règle « les deux modèles » : {'bloque aussi' if n == 2 else 'laisserait prononcer'}")
    for (cas, n), k in sorted(compte.items()):
        print(f"  résumé : {cas} : {k} analyse(s) avec {n} modèle(s) incohérent(s)")
    print("\n4. Cas de la v7 à signatures croisées : composante des signatures le long de C, par modèle")
    for e in sim["detail"]:
        nom, tau = e["cas"].rsplit(" ; tau ", 1)
        sigs, d = signatures(nom)
        if sigs is None:
            continue
        morceaux = []
        for modele, liste in sigs.items():
            C, sig = tirages(st, e["graine"] + (1 if modele == "grand" else 0), float(tau), d)
            eff = sum(f * float(sig[j] @ C) for j, f in liste)
            morceaux.append(f"{modele} : cos(sig_{liste[0][0]}, C) {float(sig[liste[0][0]] @ C):+.3f}, λ effectif {eff:+.3f}")
        print(f"  {nom} ; tau {tau} ; graine {e['graine']} ; {' ; '.join(morceaux)} ; v7 : {e['lecture']}")


if __name__ == "__main__":
    principal(sys.argv[1:])
