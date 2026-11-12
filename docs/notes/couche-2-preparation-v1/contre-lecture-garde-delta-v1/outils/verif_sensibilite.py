"""Contre-lecture de la garde δ : sensibilité au bruit, biais intermédiaires, « plancher », mutants (artefacts R5).

Lancement : python3 -B verif_sensibilite.py [--reps 4000] [--graine 4242]
Utilise les fonctions du script relu (copie_script/sim_garde.py, sha256 37c3dc7a…) sans les modifier.
"""
import argparse
import json
import math
import os
import sys

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ICI, "copie_script"))
import sim_garde as sg  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--reps", type=int, default=4000)
p.add_argument("--graine", type=int, default=4242)
a = p.parse_args()
R, G = a.reps, a.graine
SEUILS = [20.0, 160.0]
sortie = {"reglages": {"reps": R, "graine": G}}


def binom(K, tau):
    return lambda rng, reps, n, b: sg.tirage_binomial(rng, reps, n, K, tau, b)


def deux_points(h):
    # g = ±h à parts égales (moyenne nulle), plus biais
    return lambda rng, reps, n, b: rng.choice([-h, h], size=(reps, n)) + b


# ------------------------------------------------------------------ A. biais intermédiaires et bruit plus fort
lois = {"binom_K10_tau0.01": binom(10, 0.01), "binom_K10_tau0.05": binom(10, 0.05), "binom_K10_tau0.10": binom(10, 0.10),
        "binom_K10_tau0.20": binom(10, 0.20), "binom_K5_tau0.05": binom(5, 0.05), "binom_K3_tau0.10": binom(3, 0.10)}
A = {}
for nom, tirer in lois.items():
    for delta in (0.05, 0.10):
        for n in (64, 160, 960):
            for frac in (0.0, 0.25, 0.5, 0.75):
                b = frac * delta
                rng = sg.rng_de(G, "A", nom, delta, n, frac)
                g = tirer(rng, R, n, b)
                prem, _ = sg.part_certifiee(g, delta, SEUILS)
                A[f"{nom}|delta={delta}|n={n}|E[g]={b:.4f}"] = {
                    "sd_g": round(float(g.std()), 4), **{f"s{int(s)}": round(prem[str(s)]["part"], 4) for s in SEUILS}}
sortie["A_puissance_bruit_et_biais"] = A

# ------------------------------------------------------------------ B. « plancher » : certifications avant le plancher
B = {}
for nom, tirer in {"deux_points_0.1": deux_points(0.1), "deux_points_0.3": deux_points(0.3),
                   "deux_points_0.5": deux_points(0.5), "binom_K10_tau0.20": binom(10, 0.20)}.items():
    for delta, plancher in ((0.05, 93), (0.10, 48)):
        rng = sg.rng_de(G, "B", nom, delta)
        g = tirer(rng, R, 64, 0.0)
        prem, _ = sg.part_certifiee(g, delta, [20.0])
        lw = sg.log_richesse(delta - g)
        atteint = lw >= math.log(20.0)
        idx = np.where(atteint.any(axis=1), atteint.argmax(axis=1) + 1, -1)
        B[f"{nom}|delta={delta}|n=64"] = {"plancher_annonce": plancher, "part_certifiee_seuil20": prem["20.0"]["part"],
                                          "premiere_unite_min": (int(idx[idx > 0].min()) if (idx > 0).any() else None)}
sortie["B_avant_plancher"] = B


# ------------------------------------------------------------------ C. mutants de la garde contre les trois cellules
def part(g, delta, v_de):
    lw = sg.log_richesse(v_de(g, delta))
    return {str(s): round(float((lw >= math.log(s)).any(axis=1).mean()), 4) for s in SEUILS}


mutants = {
    "garde_correcte": lambda g, d: d - g,
    "signe_inverse": lambda g, d: g - d,
    "delta_oublie": lambda g, d: -g,
    "delta_double": lambda g, d: 2 * d - g,
    "marge_0.01_en_trop": lambda g, d: d + 0.01 - g,
}
C = {}
tirer = binom(10, 0.01)
for delta in (0.05, 0.10):
    for n in (64, 960):
        for cellule, b in (("honnete", 0.0), ("frontiere", delta), ("tricheur", 2 * delta)):
            rng = sg.rng_de(G, "C", delta, n, cellule)
            g = tirer(rng, R, n, b)
            for mnom, vde in mutants.items():
                C.setdefault(f"delta={delta}|n={n}|{mnom}", {})[cellule] = part(g, delta, vde)
sortie["C_mutants"] = C

print(json.dumps(sortie, indent=1, ensure_ascii=False))
