#!/usr/bin/env python3
"""Barreau 6 — diagnostic après l'arrêt sur la simulation sous le nul (brouillon 2) — v1.

La simulation sous le nul (`nul_accumulation_b6_v1.py`) mesure des taux de « accumuler bat » et de « le maximum bat »
au-dessus du niveau nominal par sonde dans plusieurs cellules. Ce diagnostic **ne change rien au texte** : il chiffre, pour la
décision de la session mère, deux remèdes possibles, sur les quatre cellules les plus défavorables, mêmes lois supposées,
même règle des états (script de puissance importé, empreinte vérifiée), 2 000 répliques par cellule :
  (v1) 10 000 tirages au lieu de 2 000, niveau inchangé (98,75 % pour k = 4) ;
  (v2) 2 000 tirages, niveau resserré : 1 - 0,05/(2k), soit 99,375 % pour k = 4 (queue de 0,3125 % par côté).
Le taux visé par sonde et par côté reste 0,00625 (k = 4).

Graines (R9) : SeedSequence(ENTROPIE, spawn_key=(variante, cellule, morceau)) ; entropie tirée le 2026-11-10 à 16:35:31 UTC.
Lancement : `python3 -I -B <ce script> <script de puissance> <script du nul> <sortie .json>`.
"""
from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import importlib.util
import json
import math
import sys
import time
from concurrent.futures import ProcessPoolExecutor

import numpy as np

ENTROPIE = 39080337479366024455014717359405036591
EMPREINTE_NUL = "c7e93bd8f76862a027b8b876ca3ab1ea28f6f39b3f459c570e40c7d315863e58"
CELLULES = [(64, "s1", 1.0), (64, "s0", 2.0), (36, "s0", 2.0), (36, "s1", 1.0)]
VARIANTES = {"v1": {"tirages": 10000, "niveau": 1 - 0.05 / 4}, "v2": {"tirages": 2000, "niveau": 1 - 0.05 / 8}}
N_REPLIQUES, MORCEAU = 2000, 250
NUL = None


def charger(chemin_puissance: str, chemin_nul: str):
    global NUL
    import hashlib
    with open(chemin_nul, "rb") as f:
        if hashlib.sha256(f.read()).hexdigest() != EMPREINTE_NUL:
            raise SystemExit("script du nul : empreinte différente : arrêt")
    spec = importlib.util.spec_from_file_location("nul_b6", chemin_nul)
    NUL = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(NUL)
    NUL.charger(chemin_puissance)          # vérifie l'empreinte du script de puissance


def morceau(args):
    cp_, cn_, variante, n, s, delta, q, i, j = args
    if NUL is None:
        charger(cp_, cn_)
    P = NUL.P
    P.N_TIRAGES = VARIANTES[variante]["tirages"]
    P.NIVEAUX = {4: VARIANTES[variante]["niveau"]}
    sigma_tau, rho = P.STRUCTURES[s]
    sigma_eta = math.sqrt(rho / (1 - rho)) if rho > 0 else 0.0
    rng = np.random.default_rng(np.random.SeedSequence(ENTROPIE, spawn_key=(list(VARIANTES).index(variante), i, j)))
    a = m = 0
    for _ in range(MORCEAU):
        hon, (org,), _ = P.episodes(rng, n, sigma_tau, sigma_eta, [delta], q)
        pl = P.plancher(rng, n, sigma_tau, sigma_eta, 0.0)
        e = P.lire_jeu(rng, hon, org, pl)["etats"][4]
        a += e == "A"
        m += e == "M"
    return variante, i, a, m


def main(cp_: str, cn_: str, sortie: str) -> None:
    debut = time.time()
    charger(cp_, cn_)
    plan = []
    for i, (n, s, delta) in enumerate(CELLULES):
        sigma_tau, rho = NUL.P.STRUCTURES[s]
        sigma_eta = math.sqrt(rho / (1 - rho)) if rho > 0 else 0.0
        plan.append((n, s, delta, NUL.q_nul(delta, sigma_tau, sigma_eta)))
    taches = [(cp_, cn_, v, n, s, d, q, i, j) for v in VARIANTES for i, (n, s, d, q) in enumerate(plan)
              for j in range(N_REPLIQUES // MORCEAU)]
    comptes = {(v, i): [0, 0] for v in VARIANTES for i in range(len(plan))}
    with ProcessPoolExecutor(max_workers=4) as ex:
        for v, i, a, m in ex.map(morceau, taches):
            comptes[(v, i)][0] += a
            comptes[(v, i)][1] += m
    lignes = []
    print(f"Diagnostic sous le nul — v1 ; entropie {ENTROPIE} ; {N_REPLIQUES} répliques ; taux visé par sonde et par côté 0,00625 (k = 4)")
    for v, cfg in VARIANTES.items():
        for i, (n, s, d, q) in enumerate(plan):
            a, m = comptes[(v, i)]
            ia, im = NUL.cp(a, N_REPLIQUES), NUL.cp(m, N_REPLIQUES)
            lignes.append({"variante": v, **cfg, "n": n, "structure": s, "delta": d, "q": q, "P_A": a / N_REPLIQUES, "IC95_P_A": ia,
                           "P_M": m / N_REPLIQUES, "IC95_P_M": im})
            print(f"{v} (tirages {cfg['tirages']}, niveau {cfg['niveau']:.5f}) n={n} {s} delta={d:.1f} q*={q:.3f} : "
                  f"P(A) {a / N_REPLIQUES:.4f} [{ia[0]:.4f} ; {ia[1]:.4f}] ; P(M) {m / N_REPLIQUES:.4f} [{im[0]:.4f} ; {im[1]:.4f}] ;"
                  f" famille (4 sondes) A {4 * a / N_REPLIQUES:.4f}, A ou M {4 * (a + m) / N_REPLIQUES:.4f}")
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump({"script": "diagnostic_nul_b6_v1.py", "entropie": str(ENTROPIE), "lignes": lignes,
                   "duree_s": round(time.time() - debut, 1)}, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")
    print(f"durée {round(time.time() - debut, 1)} s")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit("usage : diagnostic_nul_b6_v1.py <script de puissance> <script du nul> <sortie.json>")
    main(*sys.argv[1:])
