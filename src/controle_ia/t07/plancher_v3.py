"""Plancher v3 de T0.7 (remède (a') : règle (a) et 800 directions ; R-2285, R-2298) — notation vectorisée des directions de
plancher, fichier neuf (R12). `plancher_v1.py` et `plancher_v2.py` ne changent pas.

Sources : note v3 de l'analyste `docs/notes/g0-deux-semaines-v1/t07-module-v2/erreur-premiere-espece-lectures-decisives-t07-v3.md`
(`760a562c…`), sections 5 et 8 ; consigne `consigne-code-plancher-v3-t07-v1.md` (`88879387…`), point 2.

`plancher_v1.scores_plancher` note chaque direction action par action par la boucle du harnais (`noter_actions` →
`sondes.evaluation.scores_actions` → `harnais.sondes.score_action`) : 235 à 904 µs par direction et par action (note v3, § 5),
soit 18 à 69 min par sonde à 800 directions et 5 760 actions. `scores_plancher_vectorises` rend **la même matrice** (actions ×
directions) par un produit matriciel par lot de jetons :

- jetons de plusieurs actions mis bout à bout (au plus `taille_lot` jetons par lot, une action jamais coupée ; mémoire bornée),
  passés en double précision (conversion exacte depuis la simple précision, comme `SondeLineaireJetons.scores_par_jeton`) ;
- scores par jeton `A @ W + b` (W : largeur × directions), puis **même agrégation que la boucle** : maximum par action
  (`np.maximum.reduceat`, exact) ou attention (logits `A @ Q` ; par action et par direction, poids `exp(l − max l)` divisés par
  leur somme, puis somme des poids × scores, sommes faites le long d'un axe contigu comme dans la boucle) ; **jamais la
  moyenne ni la médiane sur les jetons** ;
- mêmes refus que la boucle : agrégation hors du maximum et de l'attention, empan vide, score ou logit non fini.

**Égalité à la boucle** : l'agrégation est la même au bit près à scores par jeton égaux (essai versé) ; le produit matriciel par
lot (BLAS `dgemm`) n'additionne pas dans l'ordre du produit matrice-vecteur de la boucle (`dgemv`) : l'égalité au bit près n'est
pas garantie. Écart déclaré : |vectorisé − boucle| ≤ `TOLERANCE_VECTORISEE` (10⁻¹²) × échelle de l'action, l'échelle étant le
majorant naturel de l'erreur d'arrondi d'un produit scalaire, max sur les jetons de (|a|·|w| + |b|) (attention : plus
2 · max |a|·|q| · max |a·w + b|). **Contrôle en ligne** (`controler_contre_la_boucle`, garde R5) : à chaque appel de
production, les `CONTROLE_EN_LIGNE` premières directions sont renotées par la boucle du harnais sur une action sur
`PAS_CONTROLE` (et la dernière) ;
un écart au-delà de la tolérance arrête (aucun repli silencieux vers l'une ou l'autre notation).
"""
from __future__ import annotations

import numpy as np

from ..gardes import GardeArret
from ..sondes.familles import SondeLineaireJetons
from . import plancher_v1 as pl

N_PLANCHER_REEL = 800                 # remède (a'), R-2285 ; note v3 de l'analyste (`760a562c…`), verdict
N_PLANCHER_P3 = 200                   # directions de P3 (fichier léger `701f73bd…`), gardées en lecture descriptive
TOLERANCE_VECTORISEE = 1e-12
TAILLE_LOT_JETONS = 4096
CONTROLE_EN_LIGNE = 2
PAS_CONTROLE = 8                      # contrôle en ligne : une action sur huit, et la dernière (coût borné, déclaré)
METHODE_NOTATION = "vectorisee_par_lots_v3"


def matrices_du_plancher(plancher) -> dict:
    """W (largeur × directions), b (directions), Q (largeur × directions, attention seulement), agrégation, couche ; toutes
    les directions sont des `SondeLineaireJetons` de même couche, même agrégation (maximum ou attention), même largeur."""
    if not plancher:
        raise GardeArret("plancher vide")
    agregations = {pl.exiger_agregation(p) for p in plancher}
    if len(agregations) != 1:
        raise GardeArret(f"plancher d'agrégations mêlées {sorted(agregations)} : une seule attendue")
    couches = {int(p.couche) for p in plancher}
    if len(couches) != 1:
        raise GardeArret(f"plancher de couches mêlées {sorted(couches)} : une seule attendue")
    autres = [type(p).__name__ for p in plancher if type(p) is not SondeLineaireJetons]
    if autres:
        raise GardeArret(f"plancher : directions de classe {sorted(set(autres))} ; SondeLineaireJetons seule notée par lots")
    agregation = agregations.pop()
    W = np.stack([np.asarray(p.w, dtype=np.float64) for p in plancher], axis=1)
    if W.ndim != 2:
        raise GardeArret(f"plancher : poids de forme {W.shape}")
    b = np.array([float(p.b) for p in plancher], dtype=np.float64)
    Q = None
    if agregation == "attention":
        if any(p.q is None for p in plancher):
            raise GardeArret("plancher par attention : une direction sans requête q")
        Q = np.stack([np.asarray(p.q, dtype=np.float64) for p in plancher], axis=1)
        if Q.shape != W.shape:
            raise GardeArret(f"plancher : requêtes de forme {Q.shape} ≠ poids {W.shape}")
    elif any(p.q is not None for p in plancher):
        raise GardeArret("plancher par le maximum : une direction porte une requête q")
    return {"W": np.ascontiguousarray(W), "b": b, "Q": None if Q is None else np.ascontiguousarray(Q), "agregation": agregation,
            "couche": couches.pop(), "n": len(plancher)}


def _lots(longueurs, taille_lot: int):
    """Découpe des actions en lots consécutifs d'au plus `taille_lot` jetons (une action plus longue forme son propre lot)."""
    debut, total = 0, 0
    for i, n in enumerate(longueurs):
        if total and total + n > taille_lot:
            yield debut, i
            debut, total = i, 0
        total += n
    if total:
        yield debut, len(longueurs)


def _agreger_max(S: np.ndarray, bornes: np.ndarray) -> np.ndarray:
    return np.maximum.reduceat(S, bornes[:-1], axis=0)


def _agreger_attention(S: np.ndarray, L: np.ndarray, bornes: np.ndarray) -> np.ndarray:
    """Pour chaque action et chaque direction, les opérations de `harnais.sondes.score_action` (attention), dans le même
    ordre : poids = exp(l − max l) ; poids /= somme des poids ; somme(poids × s). Les sommes portent sur l'axe contigu (une
    ligne par direction), comme la somme d'un vecteur dans la boucle."""
    sortie = np.empty((bornes.size - 1, S.shape[1]), dtype=np.float64)
    for j, (a, z) in enumerate(zip(bornes[:-1], bornes[1:])):
        st = np.ascontiguousarray(S[a:z].T)
        lt = np.ascontiguousarray(L[a:z].T)
        poids = np.exp(lt - lt.max(axis=1, keepdims=True))
        poids /= poids.sum(axis=1, keepdims=True)
        sortie[j] = np.sum(poids * st, axis=1)
    return sortie


def scores_plancher_vectorises(plancher: list, sequences, taille_lot: int = TAILLE_LOT_JETONS,
                               controle: int = CONTROLE_EN_LIGNE) -> np.ndarray:
    """Matrice (actions, directions) des scores des directions de plancher sur les actions (`sequences` : une suite de
    tableaux jetons × largeur), égale à `plancher_v1.scores_plancher(plancher, sequences)` (docstring du module). `controle`
    premières directions renotées par la boucle du harnais (0 : aucun contrôle ; essais seulement)."""
    m = matrices_du_plancher(plancher)
    sortie = _scores_matrices(m, sequences, int(taille_lot))
    if int(controle) > 0:
        controler_contre_la_boucle(plancher, sequences, sortie, int(controle))
    return sortie


def _scores_matrices(m: dict, sequences, taille_lot: int) -> np.ndarray:
    if int(taille_lot) < 1:
        raise GardeArret(f"taille_lot {taille_lot} : au moins un jeton par lot")
    seqs = list(sequences)
    if not seqs:
        raise GardeArret("aucune action à noter")
    d = m["W"].shape[0]
    longueurs = []
    for s in seqs:
        s = np.asarray(s)
        if s.ndim != 2 or s.shape[1] != d:
            raise GardeArret(f"action de forme {s.shape} : (jetons, {d}) attendue")
        if s.shape[0] < 1:
            raise GardeArret(f"empan d'action [0, 0[ invalide pour 0 positions")
        longueurs.append(int(s.shape[0]))
    sortie = np.empty((len(seqs), m["n"]), dtype=np.float64)
    for a, z in _lots(longueurs, int(taille_lot)):
        A = np.concatenate([np.asarray(s, dtype=np.float64) for s in seqs[a:z]], axis=0)
        bornes = np.concatenate([[0], np.cumsum(longueurs[a:z])])
        S = A @ m["W"] + m["b"]
        if not np.all(np.isfinite(S)):
            raise GardeArret(f"plancher : score par jeton non fini (actions {a} à {z - 1})")
        if m["agregation"] == "max":
            sortie[a:z] = _agreger_max(S, bornes)
        else:
            L = A @ m["Q"]
            if not np.all(np.isfinite(L)):
                raise GardeArret(f"plancher : logit d'attention non fini (actions {a} à {z - 1})")
            sortie[a:z] = _agreger_attention(S, L, bornes)
        del A, S
    if not np.all(np.isfinite(sortie)):
        raise GardeArret("plancher : score d'action non fini")
    return sortie


def echelle_par_action(m: dict, sequences, colonnes) -> np.ndarray:
    """Majorant naturel de l'erreur d'arrondi, par action et par direction de `colonnes` : max sur les jetons de |a|·|w| + |b|
    (attention : plus 2 · max |a|·|q| · max |a·w + b|)."""
    cols = list(colonnes)
    W, b = np.abs(m["W"][:, cols]), np.abs(m["b"][cols])
    sortie = np.empty((len(list(sequences)), len(cols)), dtype=np.float64)
    for i, s in enumerate(sequences):
        A = np.asarray(s, dtype=np.float64)
        e = (np.abs(A) @ W + b).max(axis=0)
        if m["agregation"] == "attention":
            lq = (np.abs(A) @ np.abs(m["Q"][:, cols])).max(axis=0)
            sv = np.abs(A @ m["W"][:, cols] + m["b"][cols]).max(axis=0)
            e = e + 2.0 * lq * sv
        sortie[i] = e
    return sortie


def ecart_a_la_boucle(plancher: list, sequences, vectorises: np.ndarray, colonnes, actions=None) -> dict:
    """Écart, sur les directions `colonnes` et les actions `actions` (toutes par défaut), entre la notation vectorisée et la
    boucle du harnais (`plancher_v1.noter_actions`) : écart maximal absolu, écart maximal rapporté à l'échelle, part des scores
    égaux au bit près."""
    cols = list(colonnes)
    tout = list(sequences)
    lignes = list(range(len(tout))) if actions is None else sorted(set(int(i) for i in actions))
    seqs = [tout[i] for i in lignes]
    boucle = np.stack([pl.noter_actions(plancher[j], seqs) for j in cols], axis=1)
    v = np.asarray(vectorises)[np.ix_(lignes, cols)]
    echelle = echelle_par_action(matrices_du_plancher([plancher[j] for j in cols]), seqs, range(len(cols)))
    ecart = np.abs(v - boucle)
    return {"directions": cols, "actions": len(seqs), "actions_controlees": lignes if actions is not None else "toutes",
            "ecart_max": float(ecart.max()),
            "ecart_relatif_max": float((ecart / np.maximum(echelle, np.finfo(np.float64).tiny)).max()),
            "egaux_au_bit_pres": float(np.count_nonzero(v == boucle)) / max(v.size, 1), "tolerance": TOLERANCE_VECTORISEE}


def actions_controlees(n_actions: int, pas: int = PAS_CONTROLE) -> list:
    """Une action sur `pas` (la première comprise) et la dernière."""
    return sorted(set(range(0, int(n_actions), int(pas))) | {int(n_actions) - 1})


def controler_contre_la_boucle(plancher: list, sequences, vectorises: np.ndarray, n: int = CONTROLE_EN_LIGNE,
                               pas: int = PAS_CONTROLE) -> dict:
    """Garde en ligne (R5) : les `n` premières directions renotées par la boucle du harnais sur une action sur `pas` et la
    dernière (borne déclarée : un écart limité aux autres actions ou directions n'y est pas vu ; l'égalité sur toutes est
    éprouvée par les essais) ; écart rapporté à l'échelle au-delà de `TOLERANCE_VECTORISEE` → arrêt."""
    seqs = list(sequences)
    e = ecart_a_la_boucle(plancher, seqs, vectorises, range(min(int(n), len(plancher))), actions_controlees(len(seqs), pas))
    if not e["ecart_relatif_max"] <= TOLERANCE_VECTORISEE:
        raise GardeArret(f"notation vectorisée du plancher ≠ boucle du harnais : écart relatif {e['ecart_relatif_max']:.3e} > "
                         f"{TOLERANCE_VECTORISEE:g} (directions {e['directions']}) : arrêt, aucune bascule silencieuse")
    return e


__all__ = ["N_PLANCHER_REEL", "N_PLANCHER_P3", "TOLERANCE_VECTORISEE", "TAILLE_LOT_JETONS", "CONTROLE_EN_LIGNE", "PAS_CONTROLE",
           "METHODE_NOTATION", "actions_controlees",
           "matrices_du_plancher", "scores_plancher_vectorises", "echelle_par_action", "ecart_a_la_boucle",
           "controler_contre_la_boucle"]
