#!/usr/bin/env python3
"""Jeu jouet (v1) : meilleure réponse pure itérée, jeu fictif et jeu fictif unilatéral sur deux jeux matriciels à somme
nulle sans équilibre pur, avec OpenSpiel pris tel quel pour l'exploitabilité et pour le jeu fictif de référence.

Protocole et prédictions : `protocole-jouet-v1.md` (écrit avant l'exécution). Aucun lien avec l'arène du pilote :
le jouet ne lit aucun fichier du dépôt.

Convention : joueur ligne = défenseur (maximise le gain) ; joueur colonne = attaquant (minimise), comme dans
`resoudre_jeu` de l'arène (lignes = moniteurs, colonnes = attaques).

Dynamiques :
- D1 « br_alternee » : l'attaquant répond au dernier coup pur du défenseur, puis le défenseur au dernier coup pur de
  l'attaquant ;
- D2 « jeu_fictif » : chacun répond à la moyenne empirique des coups passés de l'autre (Brown 1951) ;
- D3 « jeu_fictif_unilateral » : le défenseur répond à la moyenne empirique des coups de l'attaquant, l'attaquant au
  dernier coup pur du défenseur (lecture du bras A du pilote « mélange d'équilibre »).

Commande :
    python jouet_meilleure_reponse_v1.py --iterations 2000 --repetitions 3 --sortie sortie-jouet-v1.json
"""
from __future__ import annotations

import argparse
import json
import platform
import subprocess
import sys
from pathlib import Path

import numpy as np
import pyspiel
from open_spiel.python import policy as policy_lib
from open_spiel.python.algorithms import exploitability as expl_lib
from open_spiel.python.algorithms import fictitious_play
from scipy.optimize import linprog

RACINE = 31415926                      # hors de toute plage de l'arène (20261xxx à 20269xxx)
CODES_JEUX = {"matrix_rps": 1, "pennies_biaises": 2}
CODES_DYNAMIQUES = {"br_alternee": 1, "jeu_fictif": 2, "jeu_fictif_unilateral": 3}
POINTS_RELEVE = (1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000)


# ---------------------------------------------------------------------------------------------------------------
# Jeux
# ---------------------------------------------------------------------------------------------------------------
def charger_jeu(nom: str):
    """Rend (jeu matriciel pyspiel, version tour par tour, matrice G des gains du joueur ligne)."""
    if nom == "matrix_rps":
        jeu = pyspiel.load_game("matrix_rps")
    elif nom == "pennies_biaises":
        lignes = [[2.0, -1.0], [-1.0, 1.0]]
        jeu = pyspiel.create_matrix_game("pennies_biaises", "Pile ou face biaisé", ["H", "T"], ["H", "T"], lignes,
                                         [[-x for x in l] for l in lignes])
    else:
        raise ValueError(f"jeu inconnu : {nom!r}")
    G = np.array([[jeu.player_utility(0, i, j) for j in range(jeu.num_cols())] for i in range(jeu.num_rows())])
    assert all(abs(jeu.player_utility(1, i, j) + G[i, j]) < 1e-12 for i in range(G.shape[0]) for j in range(G.shape[1]))
    return jeu, pyspiel.convert_to_turn_based(jeu), G


def valeur_et_equilibre(G: np.ndarray) -> tuple[float, np.ndarray, np.ndarray]:
    """Valeur v* et un équilibre (p*, q*) du jeu matriciel à somme nulle (programme linéaire, comme `resoudre_jeu`)."""
    ni, nj = G.shape
    c = np.zeros(ni + 1)
    c[-1] = -1
    r1 = linprog(c, A_ub=np.hstack([-G.T, np.ones((nj, 1))]), b_ub=np.zeros(nj),
                 A_eq=np.hstack([np.ones((1, ni)), np.zeros((1, 1))]), b_eq=[1],
                 bounds=[(0, None)] * ni + [(None, None)], method="highs")
    c2 = np.zeros(nj + 1)
    c2[-1] = 1
    r2 = linprog(c2, A_ub=np.hstack([G, -np.ones((ni, 1))]), b_ub=np.zeros(ni),
                 A_eq=np.hstack([np.ones((1, nj)), np.zeros((1, 1))]), b_eq=[1],
                 bounds=[(0, None)] * nj + [(None, None)], method="highs")
    if r1.status != 0 or r2.status != 0 or abs(-r1.fun - r2.fun) > 1e-7:
        raise RuntimeError("programme linéaire non résolu")
    return float(-r1.fun), r1.x[:ni] / r1.x[:ni].sum(), r2.x[:nj] / r2.x[:nj].sum()


# ---------------------------------------------------------------------------------------------------------------
# Exploitabilité : côté matrice (par joueur) et côté OpenSpiel (NashConv / 2)
# ---------------------------------------------------------------------------------------------------------------
def expl_defenseur(G: np.ndarray, p: np.ndarray, v: float) -> float:
    """v* − min_j (pᵀG)_j : gain que l'attaquant arrache en meilleure réponse à p, au-delà de la valeur."""
    return float(v - np.min(p @ G))


def expl_attaquant(G: np.ndarray, q: np.ndarray, v: float) -> float:
    """max_i (Gq)_i − v* : gain que le défenseur arrache en meilleure réponse à q, au-delà de la valeur."""
    return float(np.max(G @ q) - v)


def politique_tabulaire(jeu_tb, p: np.ndarray, q: np.ndarray):
    pol = policy_lib.TabularPolicy(jeu_tb)
    for joueur, strat in ((0, p), (1, q)):
        for etat in pol.states_per_player[joueur]:
            pol.action_probability_array[pol.state_lookup[etat]] = np.asarray(strat, float)
    return pol


def expl_openspiel(jeu_tb, p: np.ndarray, q: np.ndarray) -> float:
    return float(expl_lib.exploitability(jeu_tb, politique_tabulaire(jeu_tb, p, q)))


# ---------------------------------------------------------------------------------------------------------------
# Meilleures réponses et dynamiques
# ---------------------------------------------------------------------------------------------------------------
def br_defenseur(G: np.ndarray, q: np.ndarray, rng: np.random.Generator) -> int:
    gains = G @ q
    cand = np.flatnonzero(gains >= gains.max() - 1e-12)
    return int(rng.choice(cand))


def br_attaquant(G: np.ndarray, p: np.ndarray, rng: np.random.Generator) -> int:
    gains = p @ G
    cand = np.flatnonzero(gains <= gains.min() + 1e-12)
    return int(rng.choice(cand))


def unite(n: int, i: int) -> np.ndarray:
    e = np.zeros(n)
    e[i] = 1.0
    return e


def periode(seq: list[int], max_periode: int | None = None) -> int | None:
    """Plus petite période P telle que la seconde moitié de `seq` soit P-périodique ; None sinon."""
    moitie = seq[len(seq) // 2:]
    max_periode = max_periode or len(moitie) // 2
    for P in range(1, max_periode + 1):
        if all(moitie[k] == moitie[k + P] for k in range(len(moitie) - P)):
            return P
    return None


def executer_dynamique(nom_jeu: str, dynamique: str, iterations: int, graine: np.random.SeedSequence) -> dict:
    jeu, jeu_tb, G = charger_jeu(nom_jeu)
    ni, nj = G.shape
    v, p_star, q_star = valeur_et_equilibre(G)
    rng = np.random.default_rng(graine)
    i, j = int(rng.integers(ni)), int(rng.integers(nj))        # premier coup pur de chacun
    comptes_D, comptes_A = unite(ni, i), unite(nj, j)          # historiques (moyennes empiriques × t)
    paires, expl_dernier_D, expl_dernier_os = [i * nj + j], [], []
    expl_moy_D, expl_moy_os, dist_q, dist_p, expl_dernier_D_tous = {}, {}, {}, {}, []
    for t in range(1, iterations + 1):
        p_moy, q_moy = comptes_D / comptes_D.sum(), comptes_A / comptes_A.sum()
        if dynamique == "br_alternee":
            j = br_attaquant(G, unite(ni, i), rng)              # répond au dernier coup pur du défenseur
            i = br_defenseur(G, unite(nj, j), rng)              # répond au dernier coup pur de l'attaquant
        elif dynamique == "jeu_fictif":
            i_new = br_defenseur(G, q_moy, rng)                 # simultané : chacun répond à la moyenne de l'autre
            j = br_attaquant(G, p_moy, rng)
            i = i_new
        elif dynamique == "jeu_fictif_unilateral":
            i = br_defenseur(G, q_moy, rng)                     # défenseur : moyenne des attaques passées (bras A)
            j = br_attaquant(G, unite(ni, i), rng)              # attaquant : dernier moniteur déployé
        else:
            raise ValueError(dynamique)
        comptes_D += unite(ni, i)
        comptes_A += unite(nj, j)
        paires.append(i * nj + j)
        expl_dernier_D_tous.append(expl_defenseur(G, unite(ni, i), v))
        if t in POINTS_RELEVE or t % 100 == 0:
            p_moy, q_moy = comptes_D / comptes_D.sum(), comptes_A / comptes_A.sum()
            expl_moy_D[t] = expl_defenseur(G, p_moy, v)
            expl_moy_os[t] = expl_openspiel(jeu_tb, p_moy, q_moy)
            expl_dernier_os.append((t, expl_openspiel(jeu_tb, unite(ni, i), unite(nj, j))))
            dist_q[t] = float(np.abs(q_moy - q_star).sum())
            dist_p[t] = float(np.abs(p_moy - p_star).sum())
    d = np.array(expl_dernier_D_tous)
    return {"jeu": nom_jeu, "dynamique": dynamique, "iterations": iterations, "valeur": v,
            "p_etoile": p_star.tolist(), "q_etoile": q_star.tolist(),
            "expl_dernier_defenseur": {"min": float(d.min()), "max": float(d.max()), "etendue": float(d.max() - d.min()),
                                       "premier": float(d[0]), "dernier": float(d[-1])},
            "expl_dernier_openspiel": expl_dernier_os,
            "expl_moyenne_defenseur": {str(k): x for k, x in expl_moy_D.items()},
            "expl_moyenne_openspiel": {str(k): x for k, x in expl_moy_os.items()},
            "dist_L1_moyenne_attaquant_q_etoile": {str(k): x for k, x in dist_q.items()},
            "dist_L1_moyenne_defenseur_p_etoile": {str(k): x for k, x in dist_p.items()},
            "moyenne_defenseur_finale": (comptes_D / comptes_D.sum()).tolist(),
            "moyenne_attaquant_finale": (comptes_A / comptes_A.sum()).tolist(),
            "periode": periode(paires), "paires_debut": paires[:12]}


def reference_xfp(nom_jeu: str, iterations: int) -> dict:
    """Jeu fictif d'OpenSpiel pris tel quel (`XFPSolver`, déterministe) : exploitabilité de la politique moyenne."""
    _, jeu_tb, _ = charger_jeu(nom_jeu)
    xfp = fictitious_play.XFPSolver(jeu_tb)
    releve = {}
    for t in range(1, iterations + 1):
        xfp.iteration()
        if t in POINTS_RELEVE:
            releve[str(t)] = float(expl_lib.exploitability(jeu_tb, xfp.average_policy()))
    return {"jeu": nom_jeu, "dynamique": "xfp_openspiel", "iterations": iterations, "expl_moyenne_openspiel": releve}


def manifeste() -> dict:
    try:
        commit = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, cwd=Path(__file__).parent,
                                check=False).stdout.strip()
    except OSError:
        commit = ""
    return {"script": Path(__file__).name, "racine": RACINE, "schema_graines":
            "SeedSequence(entropy=RACINE, spawn_key=(code_jeu, code_dynamique, repetition))",
            "codes_jeux": CODES_JEUX, "codes_dynamiques": CODES_DYNAMIQUES, "commit": commit,
            "versions": {"python": platform.python_version(), "numpy": np.__version__, "scipy": __import__("scipy").__version__,
                         "open_spiel": getattr(pyspiel, "__version__", "?")}}


def tout_executer(iterations: int, repetitions: int, racine: int = RACINE) -> dict:
    runs = []
    for nom_jeu, cj in CODES_JEUX.items():
        for dyn, cd in CODES_DYNAMIQUES.items():
            for r in range(repetitions):
                graine = np.random.SeedSequence(entropy=racine, spawn_key=(cj, cd, r))
                res = executer_dynamique(nom_jeu, dyn, iterations, graine)
                res["repetition"] = r
                res["graine"] = {"entropy": racine, "spawn_key": [cj, cd, r]}
                runs.append(res)
        runs.append(reference_xfp(nom_jeu, iterations))
    return {"manifeste": manifeste(), "iterations": iterations, "repetitions": repetitions, "runs": runs}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--iterations", type=int, default=2000)
    ap.add_argument("--repetitions", type=int, default=3)
    ap.add_argument("--sortie", type=Path, default=Path(__file__).parent / "sortie-jouet-v1.json")
    args = ap.parse_args(argv)
    if args.sortie.exists():
        print(f"refus : {args.sortie} existe déjà (R12 : nouvelle version = nouveau nom)", file=sys.stderr)
        return 2
    corps = tout_executer(args.iterations, args.repetitions)
    args.sortie.write_text(json.dumps(corps, ensure_ascii=False, indent=1), encoding="utf-8")
    for run in corps["runs"]:
        em = run["expl_moyenne_openspiel"]
        der = run.get("expl_dernier_defenseur", {})
        print(f"{run['jeu']:16s} {run['dynamique']:22s} rep={run.get('repetition', '-')} "
              f"dernier_D[min,max]=[{der.get('min', float('nan')):.3f},{der.get('max', float('nan')):.3f}] "
              f"moy_os@20={em.get('20', float('nan')):.4f} @200={em.get('200', float('nan')):.4f} "
              f"@{args.iterations}={em.get(str(args.iterations), float('nan')):.4f} periode={run.get('periode')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
