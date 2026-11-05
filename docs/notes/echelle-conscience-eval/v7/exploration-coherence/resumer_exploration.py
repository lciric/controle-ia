#!/usr/bin/env python3
"""Résumé de l'essai exploratoire des trois formes de la cohérence des deux sens (CLU-01 ; non décisif) : pour chaque
cas, ce que l'analyse prononcerait sans la cohérence (première issue commune parmi « positif », « inverse », « nul »)
et ce que chaque forme en laisse : « rencontre » (intervalle de e(m) qui rencontre [−δ ; δ]), « ponctuel »
(|e(m)| ≤ δ), « inclus » (intervalle de e(m) inclus dans [−δ ; δ]).
    python -I -B resumer_exploration.py explo-1.jsonl"""
import collections
import json
import sys

c = collections.defaultdict(collections.Counter)
for ligne in open(sys.argv[1], encoding="utf-8"):
    d = json.loads(ligne)
    pr = d["prononce_sans_regle"]
    issue = pr[0] if pr else "rien de commun parmi positif, inverse, nul"
    c[d["cas"]][f"sans la cohérence : {issue}"] += 1
    if pr:
        for regle, tenue in d["regles"].items():
            c[d["cas"]][f"{regle} : {issue if tenue else 'bloqué'}"] += 1
for cas, compte in c.items():
    print(cas)
    for k, n in compte.items():
        print(f"  {k} : {n}")
