"""Puissance de la garde δ de la porte PACE v40 (contre-lecture CL7) : témoin honnête contre tricheur, graines à moi.

Usage : python3 -B garde_puissance.py ARBRE REPETITIONS"""
import random
import sys

ARBRE, N = sys.argv[1], int(sys.argv[2])
sys.path.insert(0, ARBRE)
import numpy as np  # noqa: E402
from pole import porte_pace as pp  # noqa: E402

racine = np.random.SeedSequence(7_000_029)


def taux(regime, **k):
    graines = [int(s.generate_state(1)[0]) for s in racine.spawn(N)]
    v = 0
    for g in graines:
        r = pp.comparer(pp.simuler_suite(random.Random(g), regime, **k))
        v += next(d for d in r["decisions"] if d["temoin"])["pari_apparie"]["validee"]
    return v / N


print(f"{N} suites par ligne ; graine racine 7000029 (SeedSequence) ; témoin gain 0,35 ; m candidats")
print(f"{'réglage':<52} {'honnête validé':>14} {'tricheur validé':>15}")
for nom, k in (("monde par défaut, m=20, n=120", dict(m=20, n_dev=120)),
               ("monde par défaut, m=20, n_dev=120, n_garde=400", dict(m=20, n_dev=120, n_garde=400)),
               ("monde par défaut, m=20, n_dev=120, n_garde=1000", dict(m=20, n_dev=120, n_garde=1000)),
               ("δ = 0,10, m=20, n_dev=120, n_garde=120", dict(m=20, n_dev=120, delta=0.10)),
               ("δ = 0,10, m=20, n_dev=120, n_garde=400", dict(m=20, n_dev=120, delta=0.10, n_garde=400)),
               ("cas sain de l'essai : bruit 0,02, n_garde 600, m=5", dict(m=5, n_dev=120, bruit_fp=0.02, n_garde=600)),
               ("bruit 0,02, n_garde 120, m=5", dict(m=5, n_dev=120, bruit_fp=0.02, n_garde=120))):
    print(f"{nom:<52} {100 * taux('honnete_garde', **k):>13.1f}% {100 * taux('tricheur', **k):>14.1f}%")
