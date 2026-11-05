"""CL6 : la garde δ de notre bras sur un témoin HONNÊTE (gain 0,35, écarts de faux positifs d'espérance nulle) — le cas
sain qui manque au régime « tricheur ». Même monde que simuler_suite ; seule différence : excès 0 pour le témoin.
Usage : python -I -B garde_cas_sain.py COPIE_V39"""
import random, sys
sys.path.insert(0, sys.argv[1])
from pole import porte_pace as pp
graines, methode = pp.graines([20261029, 99], 200)
for n_dev in (40, 120, 400):
    res = {"tricheur": [], "honnete_avec_garde": [], "honnete_sans_garde": []}
    for g in graines:
        for nom in res:
            s = pp.simuler_suite(random.Random(g), "tricheur" if nom != "honnete_sans_garde" else "gain", m=20, n_dev=n_dev,
                                 fp_tricheur=(0.15 if nom == "tricheur" else 0.0))
            res[nom].append(pp.comparer(s))
    ligne = []
    for nom, rs in res.items():
        t = pp.agreger(rs)["pari_apparie"]
        ligne.append(f"{nom} : témoin validé {100 * t['temoins_valides'] / t['temoins']:.0f} %")
    print(f"n_dev = {n_dev:>3} ({methode}) : " + " ; ".join(ligne))
