#!/usr/bin/env python3
"""Barreau 6, brouillon 2 — puissance sous la **règle retenue** (option (a) de la session mère, R-2263) : 10 000 tirages par
blocs et intervalles au niveau 1 - 0,05/(2k) — v2.

Mêmes lois **supposées**, mêmes cellules (105, dont 63 non atteignables), mêmes six scénarios de séquence, mêmes 400
répliques et 200 directions que la v1 (`puissance_accumulation_b6_v1.py`, `ccc5310b…`), importée par son chemin après
vérification de son empreinte ; seuls changent `N_TIRAGES` (10 000), `NIVEAUX` (k = 4 : 99,375 % ; k = 3 : 99,167 % ;
k = 2 : 98,75 %) et l'entropie. La perte de puissance est la différence avec la sortie versée de la v1
(`puissance-accumulation-b6-v1.json`, `5f9f598f…`), dont l'empreinte est vérifiée. Planification seulement (R3) ; aucune
donnée lue ; aucun chiffre de l'état de l'art (R7).

Graines (R9) : SeedSequence(ENTROPIE, spawn_key=...) aux clés de la v1 ; entropie tirée une fois le 2026-11-10 à 16:42:34 UTC.
Lancement : `python3 -I -B <ce script> <script de puissance v1> <sortie json de la v1> <sortie .json>` ; quatre processus.
"""
from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import hashlib
import importlib.util
import json
import platform
import sys
import time
from concurrent.futures import ProcessPoolExecutor

import numpy as np

ENTROPIE = 93336667468152066419228967737062682034
EMPREINTE_V1 = "ccc5310b477ddac67d01dd11653ebb3117ed5cb303ee4c118d9069fc5a694079"
EMPREINTE_SORTIE_V1 = "5f9f598fd8fca05d706bce78faf4a68fe08fbf91a56b314b07cefbe896987223"
N_TIRAGES = 10000
NIVEAUX = {4: 1 - 0.05 / 8, 3: 1 - 0.05 / 6, 2: 1 - 0.05 / 4}
P = None


def charger(chemin: str):
    global P
    with open(chemin, "rb") as f:
        if hashlib.sha256(f.read()).hexdigest() != EMPREINTE_V1:
            raise SystemExit("script de puissance v1 : empreinte différente : arrêt")
    spec = importlib.util.spec_from_file_location("puissance_b6_v1", chemin)
    P = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(P)
    P.N_TIRAGES, P.NIVEAUX, P.ENTROPIE = N_TIRAGES, dict(NIVEAUX), ENTROPIE


def tache(args):
    chemin, genre, params = args
    if P is None:
        charger(chemin)
    if genre == "cellule":
        return genre, params, P.cellule(*params)
    return genre, params, P.sequence(*params)


def main(chemin_v1: str, sortie_v1: str, sortie: str) -> None:
    debut = time.time()
    charger(chemin_v1)
    with open(sortie_v1, "rb") as f:
        brut = f.read()
    if hashlib.sha256(brut).hexdigest() != EMPREINTE_SORTIE_V1:
        raise SystemExit("sortie json de la v1 : empreinte différente : arrêt")
    v1 = json.loads(brut)
    plan = [(64, s, a, q, 0.5) for s in P.STRUCTURES for q in P.DENSITES for a in P.AIRES]
    plan += [(36, "s1", a, q, 0.5) for q in P.DENSITES for a in P.AIRES]
    plan += [(64, "s1", a, q, 0.55) for q in P.DENSITES for a in P.AIRES]
    taches = [(chemin_v1, "cellule", (n, s, a, q, ap, (1, i + 1))) for i, (n, s, a, q, ap) in enumerate(plan)]
    j = 0
    for nom in P.SEQUENCES:
        for q in (1.0, 0.5):
            j += 1
            taches.append((chemin_v1, "sequence", (64, "s1", nom, q, (2, j))))
    cellules, sequences = [None] * len(plan), []
    with ProcessPoolExecutor(max_workers=4) as ex:
        for genre, params, r in ex.map(tache, taches):
            if genre == "cellule":
                cellules[params[-1][1] - 1] = r
            else:
                sequences.append(r)
    comparaison = []
    for c2, c1 in zip(cellules, v1["cellules"]):
        assert (c2["n"], c2["structure"], c2["a"], c2["q"], c2["a_plancher"]) == (c1["n"], c1["structure"], c1["a"], c1["q"], c1["a_plancher"])
        if not c2["atteignable"]:
            continue
        comparaison.append({"n": c2["n"], "structure": c2["structure"], "a": c2["a"], "q": c2["q"], "a_plancher": c2["a_plancher"],
                            **{f"P_A_k{k}_v1": c1["proportions"][k]["A"] for k in ("4", "3", "2")},
                            **{f"P_A_k{k}_v2": c2["proportions"][k]["A"] for k in ("4", "3", "2")},
                            "P_M_k4_v1": c1["proportions"]["4"]["M"], "P_M_k4_v2": c2["proportions"]["4"]["M"]})
    res = {"script": "puissance_accumulation_b6_v2.py", "entropie": str(ENTROPIE), "tirages": N_TIRAGES,
           "niveaux": {str(k): v for k, v in NIVEAUX.items()}, "numpy": np.__version__, "python": platform.python_version(),
           "repliques": P.N_REPLIQUES, "cellules": cellules, "sequences": sequences, "comparaison_v1": comparaison,
           "duree_s": round(time.time() - debut, 1)}
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")
    print(f"Puissance du barreau 6 — règle retenue (10 000 tirages ; niveaux 99,375 % / 99,167 % / 98,75 % pour k = 4 / 3 / 2) — v2 ;"
          f" numpy {np.__version__} ; entropie {ENTROPIE} ; durée {res['duree_s']} s")
    print("Cellules atteignables : Δ moyen ; états à k = 4 (A M Z P S) ; P(A) k = 4 : v2 (v1) ; P(A) k = 2 : v2 (v1).")
    for c, d in zip([c for c in cellules if c["atteignable"]], comparaison):
        p4 = c["proportions"]["4"]
        print(f"n={c['n']:>2} {c['structure']} q={c['q']:.1f} a={c['a']:.2f} pl={c['a_plancher']:.2f} : diff {c['difference_moyenne']:+.3f}"
              f" ; k4 A {p4['A']:.2f} M {p4['M']:.2f} Z {p4['Z']:.2f} P {p4['P']:.2f} S {p4['S']:.2f}"
              f" ; P(A) k4 {d['P_A_k4_v2']:.2f} ({d['P_A_k4_v1']:.2f}) ; k2 {d['P_A_k2_v2']:.2f} ({d['P_A_k2_v1']:.2f})"
              f" ; P(M) k4 {d['P_M_k4_v2']:.2f} ({d['P_M_k4_v1']:.2f})")
    print()
    print("Ordre fixé S100 -> S75 -> S50 -> S25, n = 64, s1 : au moins 1, 2, 3, 4 doses en A (k = 4 ; k = 2) ; v1 entre parenthèses.")
    seq_v1 = {(s["scenario"], s["q"]): s for s in v1["sequences"]}
    for s in sequences:
        if not s["atteignable"]:
            print(f"{s['scenario']} q={s['q']:.1f} : non atteignable")
            continue
        o = seq_v1[(s["scenario"], s["q"])]
        print(f"{s['scenario']:>8} q={s['q']:.1f} : k4 " + " ".join(f"{x:.2f}({y:.2f})" for x, y in zip(s["au_moins"]["4"], o["au_moins"]["4"]))
              + " ; k2 " + " ".join(f"{x:.2f}({y:.2f})" for x, y in zip(s["au_moins"]["2"], o["au_moins"]["2"])))


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit("usage : puissance_accumulation_b6_v2.py <script de puissance v1> <sortie json de la v1> <sortie.json>")
    main(*sys.argv[1:])
