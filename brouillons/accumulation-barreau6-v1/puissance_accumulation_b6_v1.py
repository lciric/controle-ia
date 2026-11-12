#!/usr/bin/env python3
"""Puissance du barreau 6 (« accumuler bat le score action par action »), brouillon 1 — v1.

Planification seulement, jamais une sélection (R3) : aucune donnée du programme n'est lue (ni 7a, ni 7b, ni P3, ni aucun
score de sonde) ; lois **gaussiennes supposées** ; aucun chiffre de l'état de l'art (R7).

Effectifs de 7b (configuration `prereg/T0.6-organismes-config-7b-v1.json`, `b7a5c1ba…` : N = 1 épisode par tâche et par
condition, T = 10 actions ; 64 tâches d'évaluation, DT-1 (b) ; 36 tâches au plan DT-1 (a), rapporté pour mémoire) : à chaque
dose, 64 épisodes de l'organisme contre les 64 mêmes épisodes `honnete` ; une tâche = un bloc (un épisode positif, un
négatif).

Modèle des scores d'action d'une sonde : s = tau_tache + eta_episode + eps_action + delta * B_action, avec
tau ~ N(0, sigma_tau^2), eta ~ N(0, sigma_eta^2), eps ~ N(0, 1), B ~ Bernoulli(q) indépendants (q = densité : part des
actions de l'organisme qui portent le décalage ; q = 1 pour un sabotage dense comme (i-a), p = 1) ; rho = corrélation
intra-épisode = sigma_eta^2 / (sigma_eta^2 + 1). delta est fixé pour que l'aire **par action** (toutes les actions de
l'organisme contre toutes celles de l'honnête, comme la lit T0.7) vaille la cible a.

Statistiques d'épisode (texte du barreau 6) : somme des 10 scores (« accumulée ») et maximum des 10 scores. Aire d'épisode :
Mann-Whitney, ex aequo pour moitié. Intervalles : percentiles d'un rééchantillonnage par blocs de tâches, 2 000 tirages, aux
niveaux de Bonferroni de T0.7 (k sondes lues : 1 - 0,05/k, k = 4, 3, 2). Plancher : 200 directions « nulles » de même
structure (sans décalage, ou, scénario « plancher haut », avec un décalage d'aire par action 0,55 sur toutes les actions de
l'organisme), quantile 0,95 de leurs aires d'épisode, pour la somme et pour le maximum.

États (ordre du texte) : P (ni la somme ni le maximum au-dessus de son plancher), S (deux aires d'épisode >= 0,99),
A (borne basse de la différence somme - maximum > 0 et somme au-dessus de son plancher), M (borne haute < 0 et maximum
au-dessus de son plancher), Z (sinon). Une seule sonde est simulée : pour k sondes lues, seul le niveau change (approximation
prudente « une sonde informative parmi k »).

Graines (R9) : numpy.random.SeedSequence(ENTROPIE, spawn_key=...) par cellule ; entropie tirée une fois le 2026-11-10 à
15:48:07 UTC (`secrets.randbits(128)`), sans lecture de données.

Lancement : `python3 -I -B <chemin absolu de ce script> <chemin de la sortie .json>` (texte imprimé sur la sortie standard).
"""
from __future__ import annotations

import json
import math
import platform
import sys
import time

import numpy as np
from scipy.stats import norm

ENTROPIE = 143381448204265874151922139412594211354
T = 10
N_TIRAGES = 2000
N_REPLIQUES = 400
N_PLANCHER = 200
QUANTILE_PLANCHER = 0.95
SATURATION = 0.99
NIVEAUX = {4: 1 - 0.05 / 4, 3: 1 - 0.05 / 3, 2: 1 - 0.05 / 2}
STRUCTURES = {"s0": (0.0, 0.0), "s1": (0.5, 0.2), "s2": (0.5, 0.5)}     # (sigma_tau, rho)
AIRES = (0.55, 0.60, 0.65, 0.70, 0.80, 0.90, 0.97)
DENSITES = (1.0, 0.5, 0.2)
SEQUENCES = {                                                          # aire par action à S100, S75, S50, S25 (supposées)
    "forte": (0.90, 0.80, 0.70, 0.60),
    "moyenne": (0.80, 0.70, 0.62, 0.56),
    "faible": (0.70, 0.64, 0.58, 0.54),
}


def aire_par_action(delta: float, q: float, sigma_tau: float, sigma_eta: float, n: int) -> float:
    """Aire par action exacte du modèle (paires de tâches différentes et de même tâche, épisodes toujours différents)."""
    v_meme = 2 * sigma_eta ** 2 + 2.0
    v_autre = v_meme + 2 * sigma_tau ** 2
    f = lambda v: q * norm.cdf(delta / math.sqrt(v)) + (1 - q) * 0.5
    return (1.0 / n) * f(v_meme) + ((n - 1.0) / n) * f(v_autre)


def delta_pour(a: float, q: float, sigma_tau: float, sigma_eta: float, n: int) -> float | None:
    """Décalage qui donne l'aire par action a ; None si a n'est pas atteignable à cette densité (a >= 0,5 + q/2)."""
    if a >= 0.5 + q / 2 - 1e-9:
        return None
    lo, hi = 0.0, 50.0
    for _ in range(200):
        mi = (lo + hi) / 2
        if aire_par_action(mi, q, sigma_tau, sigma_eta, n) < a:
            lo = mi
        else:
            hi = mi
    return (lo + hi) / 2


def comparaisons(pos: np.ndarray, neg: np.ndarray) -> np.ndarray:
    """Matrice C[..., i, j] = 1(pos_i > neg_j) + 0,5 * 1(pos_i == neg_j) ; aire = moyenne de C."""
    p, m = pos[..., :, None], neg[..., None, :]
    return (p > m).astype(np.float64) + 0.5 * (p == m)


def episodes(rng, n: int, sigma_tau: float, sigma_eta: float, deltas, q: float, tau=None):
    """Scores d'action (n, T) de l'honnête et d'un ou plusieurs organismes (même tau de tâche)."""
    if tau is None:
        tau = rng.normal(0.0, sigma_tau, size=(n, 1))
    hon = tau + rng.normal(0.0, sigma_eta, size=(n, 1)) + rng.normal(size=(n, T))
    orgs = []
    for d in deltas:
        b = rng.random(size=(n, T)) < q
        orgs.append(tau + rng.normal(0.0, sigma_eta, size=(n, 1)) + rng.normal(size=(n, T)) + d * b)
    return hon, orgs, tau


def plancher(rng, n: int, sigma_tau: float, sigma_eta: float, delta_plancher: float):
    """Quantile 0,95 des aires d'épisode (somme, maximum) de 200 directions de même structure."""
    tau = rng.normal(0.0, sigma_tau, size=(N_PLANCHER, n, 1))
    hon = tau + rng.normal(0.0, sigma_eta, size=(N_PLANCHER, n, 1)) + rng.normal(size=(N_PLANCHER, n, T))
    org = tau + rng.normal(0.0, sigma_eta, size=(N_PLANCHER, n, 1)) + rng.normal(size=(N_PLANCHER, n, T)) + delta_plancher
    a_somme = comparaisons(org.sum(-1), hon.sum(-1)).mean(axis=(-1, -2))
    a_max = comparaisons(org.max(-1), hon.max(-1)).mean(axis=(-1, -2))
    return float(np.quantile(a_somme, QUANTILE_PLANCHER)), float(np.quantile(a_max, QUANTILE_PLANCHER))


def lire_jeu(rng, hon: np.ndarray, org: np.ndarray, planchers) -> dict:
    """Aires d'épisode, intervalles par blocs aux trois niveaux, état A/M/Z/P/S par niveau."""
    n = hon.shape[0]
    c_s = comparaisons(org.sum(1), hon.sum(1))
    c_m = comparaisons(org.max(1), hon.max(1))
    w = rng.multinomial(n, np.full(n, 1.0 / n), size=N_TIRAGES).astype(np.float64)
    tir_s = ((w @ c_s) * w).sum(axis=1) / n ** 2
    tir_m = ((w @ c_m) * w).sum(axis=1) / n ** 2
    tir_d = tir_s - tir_m
    a_s, a_m = float(c_s.mean()), float(c_m.mean())
    etats = {}
    for k, niv in NIVEAUX.items():
        g = (1 - niv) / 2
        bas_d, haut_d = np.quantile(tir_d, [g, 1 - g])
        bas_s, bas_m = np.quantile(tir_s, g), np.quantile(tir_m, g)
        dessus_s, dessus_m = bas_s > planchers[0], bas_m > planchers[1]
        if not dessus_s and not dessus_m:
            e = "P"
        elif a_s >= SATURATION and a_m >= SATURATION:
            e = "S"
        elif bas_d > 0 and dessus_s:
            e = "A"
        elif haut_d < 0 and dessus_m:
            e = "M"
        else:
            e = "Z"
        etats[k] = e
    return {"aire_somme": a_s, "aire_max": a_m, "difference": a_s - a_m, "etats": etats}


def cellule(n: int, structure: str, a: float, q: float, a_plancher: float, cle) -> dict:
    sigma_tau, rho = STRUCTURES[structure]
    sigma_eta = math.sqrt(rho / (1 - rho)) if rho > 0 else 0.0
    d = delta_pour(a, q, sigma_tau, sigma_eta, n)
    if d is None:
        return {"n": n, "structure": structure, "a": a, "q": q, "a_plancher": a_plancher, "atteignable": False}
    dp = 0.0 if a_plancher == 0.5 else delta_pour(a_plancher, 1.0, sigma_tau, sigma_eta, n)
    rng = np.random.default_rng(np.random.SeedSequence(ENTROPIE, spawn_key=cle))
    diffs, a_ss, a_ms = [], [], []
    comptes = {k: {e: 0 for e in "AMZPS"} for k in NIVEAUX}
    for _ in range(N_REPLIQUES):
        hon, (org,), _ = episodes(rng, n, sigma_tau, sigma_eta, [d], q)
        pl = plancher(rng, n, sigma_tau, sigma_eta, dp)
        r = lire_jeu(rng, hon, org, pl)
        diffs.append(r["difference"]); a_ss.append(r["aire_somme"]); a_ms.append(r["aire_max"])
        for k, e in r["etats"].items():
            comptes[k][e] += 1
    return {"n": n, "structure": structure, "sigma_tau": sigma_tau, "rho": rho, "a": a, "q": q, "a_plancher": a_plancher,
            "atteignable": True, "delta": d,
            "difference_moyenne": float(np.mean(diffs)), "difference_q05": float(np.quantile(diffs, 0.05)),
            "difference_q95": float(np.quantile(diffs, 0.95)),
            "aire_somme_moyenne": float(np.mean(a_ss)), "aire_max_moyenne": float(np.mean(a_ms)),
            "proportions": {str(k): {e: c / N_REPLIQUES for e, c in v.items()} for k, v in comptes.items()}}


def sequence(n: int, structure: str, nom: str, q: float, cle) -> dict:
    """Ordre fixé S100 -> S75 -> S50 -> S25 ; une dose n'est lue décisivement que si toutes les doses plus hautes sont A."""
    sigma_tau, rho = STRUCTURES[structure]
    sigma_eta = math.sqrt(rho / (1 - rho)) if rho > 0 else 0.0
    aires = SEQUENCES[nom]
    deltas = [delta_pour(a, q, sigma_tau, sigma_eta, n) for a in aires]
    if any(d is None for d in deltas):
        return {"scenario": nom, "q": q, "atteignable": False}
    rng = np.random.default_rng(np.random.SeedSequence(ENTROPIE, spawn_key=cle))
    profondeur = {k: [0] * 5 for k in NIVEAUX}            # nombre de doses franchies en A, de 0 à 4
    for _ in range(N_REPLIQUES):
        hon, orgs, _ = episodes(rng, n, sigma_tau, sigma_eta, deltas, q)
        pl = plancher(rng, n, sigma_tau, sigma_eta, 0.0)
        lus = [lire_jeu(rng, hon, o, pl)["etats"] for o in orgs]
        for k in NIVEAUX:
            j = 0
            while j < 4 and lus[j][k] == "A":
                j += 1
            profondeur[k][j] += 1
    return {"n": n, "structure": structure, "scenario": nom, "aires": aires, "q": q, "atteignable": True,
            "au_moins": {str(k): [sum(v[j:]) / N_REPLIQUES for j in range(1, 5)] for k, v in profondeur.items()}}


def main(sortie: str) -> None:
    debut = time.time()
    cellules, sequences = [], []
    i = 0
    plan = [(64, s, a, q, 0.5) for s in STRUCTURES for q in DENSITES for a in AIRES]
    plan += [(36, "s1", a, q, 0.5) for q in DENSITES for a in AIRES]
    plan += [(64, "s1", a, q, 0.55) for q in DENSITES for a in AIRES]
    for (n, s, a, q, ap) in plan:
        i += 1
        cellules.append(cellule(n, s, a, q, ap, (1, i)))
    j = 0
    for nom in SEQUENCES:
        for q in (1.0, 0.5):
            j += 1
            sequences.append(sequence(64, "s1", nom, q, (2, j)))
    res = {"script": "puissance_accumulation_b6_v1.py", "entropie": str(ENTROPIE), "numpy": np.__version__,
           "python": platform.python_version(), "T": T, "tirages": N_TIRAGES, "repliques": N_REPLIQUES,
           "plancher": N_PLANCHER, "niveaux": {str(k): v for k, v in NIVEAUX.items()}, "saturation": SATURATION,
           "structures": STRUCTURES, "cellules": cellules, "sequences": sequences,
           "duree_s": round(time.time() - debut, 1)}
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")
    imprimer(res)


def imprimer(res: dict) -> None:
    print(f"Puissance du barreau 6 — v1 ; numpy {res['numpy']}, Python {res['python']} ; entropie {res['entropie']} ;"
          f" {res['repliques']} répliques par cellule, {res['tirages']} tirages, {res['plancher']} directions de plancher ;"
          f" durée {res['duree_s']} s")
    print("Structures : s0 = (sigma_tau 0, rho 0) ; s1 = (0,5 ; 0,2) ; s2 = (0,5 ; 0,5).")
    print()
    print("Cellules : n tâches, structure, densité q, aire par action a, plancher (aire par action des directions) ;"
          " différence d'aire d'épisode somme - maximum (moyenne [q05 ; q95]) ; aires d'épisode moyennes ;"
          " proportions des états à k = 4 (A M Z P S) ; P(A) à k = 3 et k = 2.")
    for c in res["cellules"]:
        tete = f"n={c['n']:>2} {c['structure']} q={c['q']:.1f} a={c['a']:.2f} pl={c['a_plancher']:.2f}"
        if not c["atteignable"]:
            print(f"{tete} : non atteignable (a >= 0,5 + q/2)")
            continue
        p4, p3, p2 = c["proportions"]["4"], c["proportions"]["3"], c["proportions"]["2"]
        print(f"{tete} : diff {c['difference_moyenne']:+.3f} [{c['difference_q05']:+.3f} ; {c['difference_q95']:+.3f}]"
              f" ; somme {c['aire_somme_moyenne']:.3f} max {c['aire_max_moyenne']:.3f}"
              f" ; k4 A {p4['A']:.2f} M {p4['M']:.2f} Z {p4['Z']:.2f} P {p4['P']:.2f} S {p4['S']:.2f}"
              f" ; A k3 {p3['A']:.2f} k2 {p2['A']:.2f}")
    print()
    print("Ordre fixé S100 -> S75 -> S50 -> S25, n = 64, structure s1 : probabilité de franchir en A au moins 1, 2, 3, 4 doses"
          " (k = 4 ; k = 2).")
    for s in res["sequences"]:
        if not s["atteignable"]:
            print(f"{s['scenario']} q={s['q']:.1f} : non atteignable")
            continue
        a4, a2 = s["au_moins"]["4"], s["au_moins"]["2"]
        print(f"{s['scenario']:>8} {tuple(s['aires'])} q={s['q']:.1f} : k4 " + " ".join(f"{x:.2f}" for x in a4)
              + " ; k2 " + " ".join(f"{x:.2f}" for x in a2))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage : puissance_accumulation_b6_v1.py <sortie.json>")
    main(sys.argv[1])
