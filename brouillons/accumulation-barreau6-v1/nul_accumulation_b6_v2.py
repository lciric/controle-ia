#!/usr/bin/env python3
"""Barreau 6, brouillon 2 — erreur de première espèce sous le nul, **règle retenue** (option (a) de la session mère, R-2263) :
10 000 tirages par blocs et intervalles au niveau 1 - 0,05/(2k) — v2.

La v1 (`nul_accumulation_b6_v1.py`, `c7e93bd8…`) a mesuré, à 2 000 tirages et au niveau 1 - 0,05/k, des taux au-dessus du
niveau annoncé. Cette v2 rejoue les **mêmes cellules** (64 et 36 tâches ; structures s0, s1, s2 ; nul pur ; nul « signal
présent » à décalage 1 et 2, densité q* choisie par la bissection de la v1, importée telle quelle) avec la règle retenue.

**Niveau annoncé** (inchangé, celui du texte) : par sonde et par côté 0,05/(2k), soit 0,00625 (k = 4), 0,00833 (k = 3),
0,0125 (k = 2) ; famille des k sondes : « accumuler bat » <= 0,025 ; « accumuler bat » ou « le maximum bat » <= 0,05.
**Niveau des intervalles** (règle retenue) : 1 - 0,05/(2k), soit une queue nominale de 0,05/(4k) par côté — marge contre
l'anti-conservatisme de l'intervalle percentile mesuré par la v1. Une cellule « DÉPASSE » quand la borne basse de
Clopper-Pearson à 95 % du taux d'un côté est au-dessus du niveau annoncé par sonde ; « au-dessus (non établi) » quand
seule l'estimation l'est.

Modèle, statistiques, planchers, règle des états : ceux du script de puissance versé (`puissance_accumulation_b6_v1.py`,
`ccc5310b…`), importé par la v1 du nul après vérification des empreintes, sans modification ; seuls `N_TIRAGES` et
`NIVEAUX` sont fixés ici. Lois gaussiennes **supposées** ; aucune donnée lue (R3, R7).

Graines (R9) : SeedSequence(ENTROPIE, spawn_key=(1, cellule, morceau)) ; entropie tirée une fois le 2026-11-10 à 16:42:34 UTC.
Lancement : `python3 -I -B <ce script> <script de puissance v1> <script du nul v1> <sortie .json>` ; quatre processus.
"""
from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import hashlib
import importlib.util
import json
import math
import platform
import sys
import time
from concurrent.futures import ProcessPoolExecutor

import numpy as np

ENTROPIE = 139867924097371433405432113141003785138
EMPREINTE_NUL_V1 = "c7e93bd8f76862a027b8b876ca3ab1ea28f6f39b3f459c570e40c7d315863e58"
N_TIRAGES = 10000
NIVEAUX = {4: 1 - 0.05 / 8, 3: 1 - 0.05 / 6, 2: 1 - 0.05 / 4}
ANNONCE = {4: 0.05 / 8, 3: 0.05 / 6, 2: 0.05 / 4}          # par sonde et par côté
N_REPLIQUES, MORCEAU = 2000, 250
NUL = None


def charger(chemin_puissance: str, chemin_nul: str):
    global NUL
    with open(chemin_nul, "rb") as f:
        if hashlib.sha256(f.read()).hexdigest() != EMPREINTE_NUL_V1:
            raise SystemExit("script du nul v1 : empreinte différente : arrêt")
    spec = importlib.util.spec_from_file_location("nul_b6_v1", chemin_nul)
    NUL = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(NUL)
    NUL.charger(chemin_puissance)
    NUL.P.N_TIRAGES = N_TIRAGES
    NUL.P.NIVEAUX = dict(NIVEAUX)


def morceau(args):
    cp_, cn_, n, s, delta, q, i, j = args
    if NUL is None:
        charger(cp_, cn_)
    P = NUL.P
    sigma_tau, rho = P.STRUCTURES[s]
    sigma_eta = math.sqrt(rho / (1 - rho)) if rho > 0 else 0.0
    rng = np.random.default_rng(np.random.SeedSequence(ENTROPIE, spawn_key=(1, i, j)))
    comptes = {k: {e: 0 for e in "AMZPS"} for k in NIVEAUX}
    diffs = []
    for _ in range(MORCEAU):
        hon, (org,), _ = P.episodes(rng, n, sigma_tau, sigma_eta, [delta], q)
        pl = P.plancher(rng, n, sigma_tau, sigma_eta, 0.0)
        r = P.lire_jeu(rng, hon, org, pl)
        diffs.append(r["difference"])
        for k, e in r["etats"].items():
            comptes[k][e] += 1
    return i, comptes, diffs


def main(cp_: str, cn_: str, sortie: str) -> None:
    debut = time.time()
    charger(cp_, cn_)
    P = NUL.P
    plan = []
    for n in (64, 36):
        for s in P.STRUCTURES:
            sigma_tau, rho = P.STRUCTURES[s]
            sigma_eta = math.sqrt(rho / (1 - rho)) if rho > 0 else 0.0
            plan.append({"n": n, "structure": s, "delta": 0.0, "q": 1.0, "nature": "nul pur"})
            for delta in (1.0, 2.0):
                q = NUL.q_nul(delta, sigma_tau, sigma_eta)
                d0, a_s, a_m = NUL.delta_population(q, delta, sigma_tau, sigma_eta)
                plan.append({"n": n, "structure": s, "delta": delta, "q": q, "nature": "nul, signal présent",
                             "delta_population": d0, "aire_somme_population": a_s, "aire_max_population": a_m})
    taches = [(cp_, cn_, c["n"], c["structure"], c["delta"], c["q"], i, j) for i, c in enumerate(plan)
              for j in range(N_REPLIQUES // MORCEAU)]
    res = {i: {"comptes": {k: {e: 0 for e in "AMZPS"} for k in NIVEAUX}, "diffs": []} for i in range(len(plan))}
    with ProcessPoolExecutor(max_workers=4) as ex:
        for i, comptes, diffs in ex.map(morceau, taches):
            for k in comptes:
                for e in comptes[k]:
                    res[i]["comptes"][k][e] += comptes[k][e]
            res[i]["diffs"].extend(diffs)
    cellules, depasse, au_dessus = [], [], []
    for i, c in enumerate(plan):
        r, nrep = res[i], len(res[i]["diffs"])
        ligne = dict(c, repliques=nrep, delta_moyen_repliques=float(np.mean(r["diffs"])),
                     erreur_type_delta_moyen=float(np.std(r["diffs"], ddof=1) / math.sqrt(nrep)), etats={})
        for k in NIVEAUX:
            a, m = r["comptes"][k]["A"], r["comptes"][k]["M"]
            ia, im = NUL.cp(a, nrep), NUL.cp(m, nrep)
            e = {"niveau_intervalle": NIVEAUX[k], "annonce_par_sonde_et_par_cote": ANNONCE[k],
                 "proportions": {x: v / nrep for x, v in r["comptes"][k].items()},
                 "P_A": a / nrep, "IC95_P_A": ia, "P_M": m / nrep, "IC95_P_M": im,
                 "famille_A": k * a / nrep, "famille_A_ou_M": k * (a + m) / nrep,
                 "depasse_A": ia[0] > ANNONCE[k], "depasse_M": im[0] > ANNONCE[k],
                 "au_dessus_A": a / nrep > ANNONCE[k], "au_dessus_M": m / nrep > ANNONCE[k]}
            ligne["etats"][str(k)] = e
            tete = f"n={c['n']} {c['structure']} delta={c['delta']:.1f} k={k}"
            for cote in ("A", "M"):
                if e[f"depasse_{cote}"]:
                    depasse.append(f"{tete} côté {cote}")
                elif e[f"au_dessus_{cote}"]:
                    au_dessus.append(f"{tete} côté {cote}")
        cellules.append(ligne)
    sortie_doc = {"script": "nul_accumulation_b6_v2.py", "entropie": str(ENTROPIE), "tirages": N_TIRAGES,
                  "niveaux_intervalles": {str(k): v for k, v in NIVEAUX.items()}, "annonce": {str(k): v for k, v in ANNONCE.items()},
                  "numpy": np.__version__, "python": platform.python_version(), "repliques": N_REPLIQUES, "cellules": cellules,
                  "depasse": depasse, "au_dessus_non_etabli": au_dessus, "duree_s": round(time.time() - debut, 1)}
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(sortie_doc, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")
    print(f"Barreau 6 — nul, règle retenue (10 000 tirages, niveau 1 - 0,05/(2k)) — v2 ; numpy {np.__version__} ; entropie {ENTROPIE} ;"
          f" {N_REPLIQUES} répliques ; durée {sortie_doc['duree_s']} s")
    print("Annoncé par sonde et par côté : 0,00625 (k = 4), 0,00833 (k = 3), 0,0125 (k = 2) ; famille : A <= 0,025 ; A ou M <= 0,05.")
    for c in cellules:
        pop = (f" ; q*={c['q']:.3f}, aires pop {c['aire_somme_population']:.3f}") if "aire_somme_population" in c else ""
        print(f"n={c['n']:>2} {c['structure']} delta={c['delta']:.1f} {c['nature']}{pop} ; Δ moyen {c['delta_moyen_repliques']:+.4f}"
              f" (e.t. {c['erreur_type_delta_moyen']:.4f})")
        for k in ("4", "3", "2"):
            e = c["etats"][k]
            pr = e["proportions"]
            print(f"   k={k} : P(A) {e['P_A']:.4f} [{e['IC95_P_A'][0]:.4f} ; {e['IC95_P_A'][1]:.4f}] ; P(M) {e['P_M']:.4f}"
                  f" [{e['IC95_P_M'][0]:.4f} ; {e['IC95_P_M'][1]:.4f}] ; annoncé {e['annonce_par_sonde_et_par_cote']:.5f} ;"
                  f" famille A {e['famille_A']:.4f}, A ou M {e['famille_A_ou_M']:.4f} ; Z {pr['Z']:.3f} P {pr['P']:.3f} S {pr['S']:.3f}")
    print()
    print("DÉPASSE (borne basse de Clopper-Pearson au-dessus de l'annoncé) : " + (" ; ".join(depasse) or "aucune cellule"))
    print("Au-dessus de l'annoncé, non établi (estimation seule) : " + (" ; ".join(au_dessus) or "aucune cellule"))


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit("usage : nul_accumulation_b6_v2.py <script de puissance v1> <script du nul v1> <sortie.json>")
    main(*sys.argv[1:])
