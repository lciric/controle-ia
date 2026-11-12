#!/usr/bin/env python3
"""Barreau 6, brouillon 2 — erreur de première espèce des états décisifs « accumuler bat » (A) et « le maximum bat » (M),
simulée sous le nul (Δ vrai = 0), aux effectifs de 7b (64 tâches) et au plan à 36 tâches — v1.

Demandé par la session mère (R-2261) après la contre-lecture 1 (CLA-09 : « aucune simulation sous le nul ne mesure le taux
réel »). Planification seulement, jamais une sélection (R3) : aucune donnée du programme n'est lue ; lois gaussiennes
**supposées** ; aucun chiffre de l'état de l'art (R7).

Le modèle, les statistiques d'épisode, les intervalles (percentiles d'un rééchantillonnage par blocs de tâches, 2 000 tirages),
les planchers (200 directions de même structure, quantile 0,95) et la règle des états (P, S, A, M, Z) sont **ceux du script
de puissance versé** `puissance_accumulation_b6_v1.py` (`ccc5310b…`), importé par son chemin après vérification de son
empreinte, sans modification : seules changent les cellules simulées.

Nul : le décalage delta porte sur une part q* des actions de l'organisme, q* étant choisi (bissection, échantillon de
40 000 épisodes par classe, nombres aléatoires communs) pour que la différence d'aires d'épisode somme - maximum vaille 0 dans
la population ; la classe « signal présent » (aires d'épisode bien au-dessus de 0,5) éprouve la règle complète, plancher
compris. Nul « pur » : delta = 0 (aucun signal ; Δ vrai = 0 par symétrie). Δ vrai résiduel de la bissection estimé et écrit
(moyenne des Δ des répliques, avec son erreur type).

Niveau nominal par sonde et par côté : (1 - niveau)/2, soit 0,00625 (k = 4), 0,00833 (k = 3), 0,0125 (k = 2) ; borne de
Bonferroni de la famille : k fois ce taux, soit 0,025 pour A seul et 0,05 pour A ou M. Une ligne « DÉPASSE » est imprimée
quand la borne basse de Clopper-Pearson à 95 % de P(A) (ou de P(M)) est au-dessus du taux nominal par sonde.

Graines (R9) : numpy.random.SeedSequence(ENTROPIE, spawn_key=(cellule, morceau)) ; entropie tirée une fois le 2026-11-10 à
16:29:56 UTC (`secrets.randbits(128)`), sans lecture de données ; distincte de celle du script de puissance.

Lancement : `python3 -I -B <chemin absolu de ce script> <chemin absolu du script de puissance> <sortie .json>` (texte sur la
sortie standard) ; quatre processus, un fil de calcul chacun.
"""
from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")

import hashlib
import importlib.util
import json
import math
import platform
import sys
import time
from concurrent.futures import ProcessPoolExecutor

import numpy as np
from scipy.stats import beta, rankdata

ENTROPIE = 263599732970041936733436419777776260927
EMPREINTE_PUISSANCE = "ccc5310b477ddac67d01dd11653ebb3117ed5cb303ee4c118d9069fc5a694079"
N_REPLIQUES = 2000
MORCEAU = 250
N_POP = 40000
P = None                     # module de puissance, chargé dans chaque processus


def charger(chemin: str):
    global P
    with open(chemin, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != EMPREINTE_PUISSANCE:
        raise SystemExit(f"script de puissance : empreinte {sha} ≠ {EMPREINTE_PUISSANCE} : arrêt")
    spec = importlib.util.spec_from_file_location("puissance_b6", chemin)
    P = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(P)
    return P


def _aire(pos, neg) -> float:
    r = rankdata(np.r_[pos, neg])
    n1, n0 = len(pos), len(neg)
    return float((r[:n1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0))


def delta_population(q: float, delta: float, sigma_tau: float, sigma_eta: float) -> tuple[float, float, float]:
    """Δ de population (aires d'épisode somme - maximum) ; nombres aléatoires communs d'un appel à l'autre."""
    rng = np.random.default_rng(np.random.SeedSequence(ENTROPIE, spawn_key=(0,)))
    tau = rng.normal(0.0, sigma_tau, size=(N_POP, 1))
    hon = tau + rng.normal(0.0, sigma_eta, size=(N_POP, 1)) + rng.normal(size=(N_POP, P.T))
    u = rng.random(size=(N_POP, P.T))
    org = tau + rng.normal(0.0, sigma_eta, size=(N_POP, 1)) + rng.normal(size=(N_POP, P.T)) + delta * (u < q)
    a_s, a_m = _aire(org.sum(1), hon.sum(1)), _aire(org.max(1), hon.max(1))
    return a_s - a_m, a_s, a_m


def q_nul(delta: float, sigma_tau: float, sigma_eta: float):
    lo, hi = 0.02, 1.0
    d_lo, d_hi = delta_population(lo, delta, sigma_tau, sigma_eta)[0], delta_population(hi, delta, sigma_tau, sigma_eta)[0]
    if not (d_lo < 0 < d_hi):
        return None
    for _ in range(30):
        mi = (lo + hi) / 2
        if delta_population(mi, delta, sigma_tau, sigma_eta)[0] < 0:
            lo = mi
        else:
            hi = mi
    return (lo + hi) / 2


def morceau(args):
    chemin, n, structure, delta, q, cellule, k_morceau, nb = args
    if P is None:
        charger(chemin)
    sigma_tau, rho = P.STRUCTURES[structure]
    sigma_eta = math.sqrt(rho / (1 - rho)) if rho > 0 else 0.0
    rng = np.random.default_rng(np.random.SeedSequence(ENTROPIE, spawn_key=(1, cellule, k_morceau)))
    comptes = {k: {e: 0 for e in "AMZPS"} for k in P.NIVEAUX}
    diffs = []
    for _ in range(nb):
        hon, (org,), _ = P.episodes(rng, n, sigma_tau, sigma_eta, [delta], q)
        pl = P.plancher(rng, n, sigma_tau, sigma_eta, 0.0)
        r = P.lire_jeu(rng, hon, org, pl)
        diffs.append(r["difference"])
        for k, e in r["etats"].items():
            comptes[k][e] += 1
    return cellule, comptes, diffs


def cp(x: int, n: int) -> tuple[float, float]:
    bas = 0.0 if x == 0 else float(beta.ppf(0.025, x, n - x + 1))
    haut = 1.0 if x == n else float(beta.ppf(0.975, x + 1, n - x))
    return bas, haut


def main(chemin_puissance: str, sortie: str) -> None:
    debut = time.time()
    charger(chemin_puissance)
    plan = []
    for n in (64, 36):
        for s in P.STRUCTURES:
            sigma_tau, rho = P.STRUCTURES[s]
            sigma_eta = math.sqrt(rho / (1 - rho)) if rho > 0 else 0.0
            plan.append({"n": n, "structure": s, "delta": 0.0, "q": 1.0, "nature": "nul pur"})
            for delta in (1.0, 2.0):
                q = q_nul(delta, sigma_tau, sigma_eta)
                if q is None:
                    plan.append({"n": n, "structure": s, "delta": delta, "q": None, "nature": "aucun q* (pas de changement de signe)"})
                    continue
                d0, a_s, a_m = delta_population(q, delta, sigma_tau, sigma_eta)
                plan.append({"n": n, "structure": s, "delta": delta, "q": q, "nature": "nul, signal présent",
                             "delta_population": d0, "aire_somme_population": a_s, "aire_max_population": a_m})
    taches = []
    for i, c in enumerate(plan):
        if c["q"] is None:
            continue
        for j in range(N_REPLIQUES // MORCEAU):
            taches.append((chemin_puissance, c["n"], c["structure"], c["delta"], c["q"], i, j, MORCEAU))
    resultats = {i: {"comptes": {k: {e: 0 for e in "AMZPS"} for k in P.NIVEAUX}, "diffs": []} for i in range(len(plan))}
    with ProcessPoolExecutor(max_workers=4) as ex:
        for i, comptes, diffs in ex.map(morceau, taches):
            for k in comptes:
                for e in comptes[k]:
                    resultats[i]["comptes"][k][e] += comptes[k][e]
            resultats[i]["diffs"].extend(diffs)
    cellules = []
    for i, c in enumerate(plan):
        if c["q"] is None:
            cellules.append(c)
            continue
        r = resultats[i]
        nrep = len(r["diffs"])
        ligne = dict(c)
        ligne["repliques"] = nrep
        ligne["delta_moyen_repliques"] = float(np.mean(r["diffs"]))
        ligne["erreur_type_delta_moyen"] = float(np.std(r["diffs"], ddof=1) / math.sqrt(nrep))
        ligne["etats"] = {}
        for k, niv in P.NIVEAUX.items():
            nominal = (1 - niv) / 2
            a, m = r["comptes"][k]["A"], r["comptes"][k]["M"]
            ligne["etats"][str(k)] = {
                "proportions": {e: v / nrep for e, v in r["comptes"][k].items()},
                "nominal_par_sonde_et_par_cote": nominal,
                "P_A": a / nrep, "IC95_P_A": cp(a, nrep), "P_M": m / nrep, "IC95_P_M": cp(m, nrep),
                "borne_famille_A": k * a / nrep, "borne_famille_A_ou_M": k * (a + m) / nrep,
                "depasse_A": cp(a, nrep)[0] > nominal, "depasse_M": cp(m, nrep)[0] > nominal}
        cellules.append(ligne)
    res = {"script": "nul_accumulation_b6_v1.py", "entropie": str(ENTROPIE), "script_puissance": EMPREINTE_PUISSANCE,
           "numpy": np.__version__, "python": platform.python_version(), "repliques": N_REPLIQUES, "n_population": N_POP,
           "cellules": cellules, "duree_s": round(time.time() - debut, 1)}
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")
    imprimer(res)


def imprimer(res: dict) -> None:
    print(f"Barreau 6 — erreur de première espèce sous le nul — v1 ; numpy {res['numpy']}, Python {res['python']} ;"
          f" entropie {res['entropie']} ; script de puissance {res['script_puissance'][:12]}… ; {res['repliques']} répliques"
          f" par cellule ; durée {res['duree_s']} s")
    print("Nominal par sonde et par côté : 0,00625 (k = 4) ; 0,00833 (k = 3) ; 0,0125 (k = 2). Famille (k sondes) : A <= 0,025 ;"
          " A ou M <= 0,05.")
    depasse = []
    for c in res["cellules"]:
        tete = f"n={c['n']:>2} {c['structure']} delta={c['delta']:.1f} {c['nature']}"
        if c["q"] is None:
            print(f"{tete} : sans objet")
            continue
        pop = (f" ; q*={c['q']:.3f}, Δ pop {c['delta_population']:+.4f}, aires pop somme {c['aire_somme_population']:.3f}"
               f" max {c['aire_max_population']:.3f}") if "delta_population" in c else ""
        print(f"{tete}{pop} ; Δ moyen des répliques {c['delta_moyen_repliques']:+.4f} (e.t. {c['erreur_type_delta_moyen']:.4f})")
        for k in ("4", "3", "2"):
            e = c["etats"][k]
            pr = e["proportions"]
            print(f"   k={k} : P(A) {e['P_A']:.4f} [{e['IC95_P_A'][0]:.4f} ; {e['IC95_P_A'][1]:.4f}]"
                  f" ; P(M) {e['P_M']:.4f} [{e['IC95_P_M'][0]:.4f} ; {e['IC95_P_M'][1]:.4f}]"
                  f" ; nominal {e['nominal_par_sonde_et_par_cote']:.5f} ; famille A {e['borne_famille_A']:.4f}"
                  f", A ou M {e['borne_famille_A_ou_M']:.4f} ; Z {pr['Z']:.3f} P {pr['P']:.3f} S {pr['S']:.3f}")
            if e["depasse_A"] or e["depasse_M"]:
                depasse.append(f"{tete} k={k}")
    print()
    if depasse:
        print("DÉPASSE (borne basse de Clopper-Pearson au-dessus du nominal par sonde) : " + " ; ".join(depasse))
    else:
        print("Aucune cellule où la borne basse de Clopper-Pearson de P(A) ou de P(M) dépasse le nominal par sonde.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("usage : nul_accumulation_b6_v1.py <script de puissance> <sortie.json>")
    main(sys.argv[1], sys.argv[2])
