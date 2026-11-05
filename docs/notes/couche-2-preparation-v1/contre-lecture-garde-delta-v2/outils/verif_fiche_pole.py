"""Q2 — la fiche simulée (script v2) est-elle la fiche du pôle (v41) ? Entrées identiques, fonctions des deux côtés.

Usage : python3 -I -B verif_fiche_pole.py > ../sorties/verif_fiche_pole.json
"""
import importlib.util
import json
import math
import os
import sys

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))


def charger(nom, chemin):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


sim = charger("sim", os.path.join(ICI, "copie_script", "sim_garde_v2.py"))
pa = charger("pa", os.path.join(ICI, "copie_pole", "pari_apparie.py"))
sortie = {}

# --- bloc 1 : trajectoires et instant d'arrêt de la fiche (k contrastes, k gardes, mêmes unités) -------------------
rng = np.random.default_rng(np.random.SeedSequence([2026, 1029, 1]))
ecart_max, arrets_diff, essais, promues = 0.0, 0, 0, 0
for essai in range(600):
    k = int(rng.integers(1, 4))
    n = int(rng.integers(20, 260))
    delta = float(rng.choice([0.05, 0.10, 0.2]))
    m = int(rng.choice([1, 8]))
    K = int(rng.choice([3, 10]))
    tau = float(rng.choice([0.01, 0.10, 0.3]))
    gs = [rng.binomial(K, tau + float(rng.choice([0, 0.0125, -0.005])) if tau > 0.01 else tau, n) / K
          - rng.binomial(K, tau, n) / K for _ in range(k)]
    if essai % 7 == 0:  # écarts extrêmes pour l'écrêtage
        gs[0] = rng.choice([-1.0, -0.9, 0.0, 1.0], n)
    vs = [rng.binomial(K, float(rng.choice([0.5, 0.6, 0.9])), n) / K - rng.binomial(K, 0.4, n) / K for _ in range(k)]
    # côté script
    lg = np.stack([sim.log_richesse(sim.ecreter(delta - g[None, :])) for g in gs])[:, 0, :]
    lc = np.stack([sim.log_richesse(sim.ecreter(v[None, :])) for v in vs])[:, 0, :]
    mini_s = np.minimum(lg.min(axis=0), lc.min(axis=0))
    arret_s = int(sim.premiere_atteinte(mini_s[None, :], m / sim.ALPHA)[0])
    # côté pôle
    r = pa.evaluer({f"c{j}": [float(x) for x in vs[j]] for j in range(k)},
                   {f"g{j}": [float(x) for x in gs[j]] for j in range(k)}, delta=delta, alpha=0.05, m=m)
    mini_p = np.array(r["trajectoire_log_min"])
    ecart_max = max(ecart_max, float(np.abs(mini_s - mini_p).max()))
    arret_p = r["instant_d_arret"] or -1
    arrets_diff += int(arret_p != arret_s)
    promues += int(r["promue"])
    essais += 1
    assert abs(r["seuil_log"] - math.log(m / sim.ALPHA)) < 1e-15
sortie["bloc1_fiche_memes_unites"] = {"essais": essais, "ecart_max_trajectoire_min": ecart_max,
                                      "instants_d_arret_differents": arrets_diff, "fiches_promues_pole": promues}

# --- bloc 2 : ce que le script ne modélise pas : garde de longueur propre (unités honnêtes ≠ unités sabotées) -------
# Pôle : les contrastes portent sur les unités à sabotés, la garde sur les unités à honnêtes ; chaque processus s'arrête
# à sa dernière valeur. Exemple : 160 unités à sabotés, 100 à honnêtes.
rng = np.random.default_rng(np.random.SeedSequence([2026, 1029, 2]))
reps, n_c, n_g, delta = 2000, 160, 100, 0.10
prom_pole, prom_script_160 = 0, 0
for _ in range(reps):
    v = rng.binomial(10, 0.5, n_c) / 10 - rng.binomial(10, 0.4, n_c) / 10
    g = rng.binomial(10, 0.01, n_g) / 10 - rng.binomial(10, 0.01, n_g) / 10
    r = pa.evaluer({"c": list(map(float, v))}, {"g": list(map(float, g))}, delta=delta, alpha=0.05, m=8)
    prom_pole += int(r["promue"])
sortie["bloc2_longueurs_differentes"] = {
    "note": "contraste sur 160 unités à sabotés, garde sur 100 unités à honnêtes, δ = 0,10, seuil 160 (pôle, evaluer)",
    "part_promue_pole": prom_pole / reps}

# --- bloc 3 : seuil 20 du script contre lecture e-BH du pôle (k* = 8, huit fiches de même loi) -----------------------
# Script : « première atteinte de 20 » (maximum de la trajectoire). Pôle (Course, D-S25 bis) : la fiche s'arrête à
# m_c/α_c = 160 ; sinon sa valeur est la **dernière** ; puis ebh_pondere sur huit fiches de budget α/8.
def fiche_un_tirage(rng, n, delta, K, tau, k):
    gs = [rng.binomial(K, tau, n) / K - rng.binomial(K, tau, n) / K for _ in range(k)]
    vs = [rng.binomial(K, 0.5, n) / K - rng.binomial(K, 0.4, n) / K for _ in range(k)]
    lg = np.stack([sim.log_richesse(sim.ecreter(delta - g[None, :]))[0] for g in gs])
    lc = np.stack([sim.log_richesse(sim.ecreter(v[None, :]))[0] for v in vs])
    return np.minimum(lg.min(axis=0), lc.min(axis=0))


bloc3 = {}
for (n, delta, K, tau, k) in [(160, 0.05, 10, 0.01, 1), (160, 0.05, 10, 0.01, 3), (64, 0.10, 10, 0.01, 1),
                              (64, 0.10, 10, 0.01, 3), (160, 0.05, 10, 0.10, 1)]:
    rng = np.random.default_rng(np.random.SeedSequence([2026, 1029, 3, n, int(delta * 100), K, int(tau * 100), k]))
    R = 500
    max20, fin20, ebh_tous, ebh_part = 0, 0, 0, []
    for _ in range(R):
        logs_e = {}
        for f in range(8):
            mini = fiche_un_tirage(rng, n, delta, K, tau, k)
            atteint = np.nonzero(mini >= math.log(160))[0]
            val = float(mini[atteint[0]]) if atteint.size else float(mini[-1])
            logs_e[f] = val
            if f == 0:
                max20 += int(mini.max() >= math.log(20))
                fin20 += int(val >= math.log(20) - 1e-12)
        ret = pa.ebh_pondere(logs_e, {f: 0.05 / 8 for f in range(8)}, 0.05)
        ebh_tous += int(len(ret) == 8)
        ebh_part.append(len(ret) / 8)
    bloc3[f"n={n}|delta={delta}|K={K}|tau={tau}|k={k}"] = {
        "script_premiere_atteinte_20": max20 / R, "valeur_arretee_ou_finale_ge_20": fin20 / R,
        "ebh_huit_vraies_part_retenue": float(np.mean(ebh_part)), "ebh_huit_retenues": ebh_tous / R, "repetitions": R}
sortie["bloc3_seuil20_contre_ebh"] = bloc3
json.dump(sortie, sys.stdout, indent=1, ensure_ascii=False)
print()
