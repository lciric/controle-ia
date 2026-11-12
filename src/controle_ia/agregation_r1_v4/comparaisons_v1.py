"""Comparaisons d'agrégateurs au niveau de l'épisode — v1.

- aire sous la courbe d'épisode (Mann-Whitney, ex aequo pour moitié : `sondes.evaluation.aire_sous_courbe`) ;
- différence appariée d'aires entre deux statistiques sur les mêmes épisodes, rééchantillonnage par blocs de tâche
  (toutes les lignes d'une tâche tirées ensemble) : intervalle percentile bilatéral et valeur p unilatérale
  p = (1 + #{Δ* du mauvais côté de 0}) / (B + 1) ;
- permutation des étiquettes au niveau de l'épisode, à l'intérieur de chaque tâche (garde « signal présent ») ;
- correction de Holm (pas à pas descendant) ; un test écarté par sa garde entre dans la famille avec p = 1.
Aucun repli silencieux : plus de 1 % de tirages dégénérés arrête (R5).
"""
from __future__ import annotations

import numpy as np

from ..gardes import GardeArret
from ..sondes.evaluation import aire_sous_courbe


def _membres(blocs) -> list[np.ndarray]:
    blocs = np.asarray(blocs)
    uniques = np.unique(blocs)
    if uniques.size < 2:
        raise GardeArret("au moins deux blocs (tâches) pour un rééchantillonnage par blocs")
    return [np.flatnonzero(blocs == u) for u in uniques]


def difference_aires(a, b, y, blocs, n_tirages: int, rng: np.random.Generator, sens: str,
                     niveau: float = 0.95) -> dict:
    """Δ = aire(a) − aire(b) ; `sens` = « positif » (H1 : Δ > 0) ou « negatif » (H1 : Δ < 0)."""
    if sens not in ("positif", "negatif"):
        raise GardeArret(f"sens inconnu : {sens!r}")
    a, b, y = (np.asarray(v, dtype=np.float64) for v in (a, b, y))
    if not (a.shape == b.shape == y.shape == np.asarray(blocs).shape) or a.ndim != 1:
        raise GardeArret("statistiques, étiquettes et blocs : vecteurs de même longueur attendus")
    membres = _membres(blocs)
    valeurs, degeneres = [], 0
    for _ in range(int(n_tirages)):
        choix = rng.integers(0, len(membres), size=len(membres))
        i = np.concatenate([membres[c] for c in choix])
        if np.unique(y[i]).size < 2:
            degeneres += 1
            continue
        valeurs.append(aire_sous_courbe(a[i], y[i]) - aire_sous_courbe(b[i], y[i]))
    if degeneres > 0.01 * n_tirages:
        raise GardeArret(f"{degeneres} tirages sur {n_tirages} sans les deux classes")
    v = np.asarray(valeurs)
    aire_a, aire_b = aire_sous_courbe(a, y), aire_sous_courbe(b, y)
    q = (1.0 - niveau) / 2.0
    mauvais = int((v <= 0.0).sum()) if sens == "positif" else int((v >= 0.0).sum())
    return {"difference": aire_a - aire_b, "aire_a": aire_a, "aire_b": aire_b,
            "bas": float(np.quantile(v, q)), "haut": float(np.quantile(v, 1.0 - q)),
            "p_unilaterale": (1.0 + mauvais) / (v.size + 1.0), "tirages": int(v.size), "degeneres": degeneres,
            "sens": sens}


def permutation_dans_taches(stat, y, blocs, n_permutations: int, rng: np.random.Generator) -> dict:
    """H0 : étiquettes échangeables à l'intérieur de chaque tâche. Chaque tâche doit avoir un épisode de chaque classe
    (épisodes naturels : un honnête, un saboteur) ; sinon arrêt. p unilatérale (aire au-dessus de 0,5)."""
    stat, y = np.asarray(stat, dtype=np.float64), np.asarray(y)
    membres = _membres(blocs)
    for m in membres:
        if m.size != 2 or set(y[m].tolist()) != {0, 1}:
            raise GardeArret("permutation : exactement un épisode de chaque classe par tâche attendu")
    paires = np.array(membres)                      # (tâches, 2)
    obs = aire_sous_courbe(stat, y)
    compte = 0
    yp = y.copy()
    for _ in range(int(n_permutations)):
        echange = rng.random(paires.shape[0]) < 0.5
        yp[:] = y
        yp[paires[echange, 0]], yp[paires[echange, 1]] = y[paires[echange, 1]], y[paires[echange, 0]]
        compte += aire_sous_courbe(stat, yp) >= obs
    return {"aire": obs, "p": (1.0 + compte) / (n_permutations + 1.0), "permutations": int(n_permutations)}


def holm(p: dict, alpha: float) -> dict:
    """Holm pas à pas descendant ; renvoie {nom: {"p": p, "seuil": ..., "rejet": bool}}."""
    if not p:
        raise GardeArret("famille vide")
    ordre = sorted(p, key=lambda k: (p[k], k))
    m, sortie, encore = len(ordre), {}, True
    for r, nom in enumerate(ordre):
        seuil = alpha / (m - r)
        rejet = encore and p[nom] <= seuil
        encore = rejet
        sortie[nom] = {"p": float(p[nom]), "seuil": seuil, "rejet": bool(rejet), "rang": r + 1}
    return sortie


def contraste_blocs(jeux: list, coefficients: list, n_tirages: int, rng: np.random.Generator, sens: str,
                    niveau: float = 0.95) -> dict:
    """Contraste Σ_k c_k · (aire(a_k) − aire(b_k)) sur plusieurs jeux d'épisodes (a_k, b_k, y_k, tâches_k), un même tirage
    de tâches pour tous les jeux (blocs communs : un épisode hybride et l'épisode honnête dont il vient sont tirés
    ensemble). H1 : contraste > 0 (`positif`) ou < 0 (`negatif`)."""
    if sens not in ("positif", "negatif"):
        raise GardeArret(f"sens inconnu : {sens!r}")
    if len(jeux) != len(coefficients) or not jeux:
        raise GardeArret("un coefficient par jeu attendu")
    prepares, univers = [], set()
    for a, b, y, blocs in jeux:
        a, b, y, blocs = (np.asarray(v) for v in (a, b, y, blocs))
        if not (a.shape == b.shape == y.shape == blocs.shape) or a.ndim != 1:
            raise GardeArret("statistiques, étiquettes et tâches : vecteurs de même longueur attendus")
        prepares.append((a.astype(np.float64), b.astype(np.float64), y, {t: np.flatnonzero(blocs == t)
                                                                          for t in np.unique(blocs)}))
        univers |= set(np.unique(blocs).tolist())
    univers = sorted(univers)
    if len(univers) < 2:
        raise GardeArret("au moins deux tâches pour un rééchantillonnage par blocs")

    def valeur(choix) -> float | None:
        total = 0.0
        for (a, b, y, membres), c in zip(prepares, coefficients):
            i = np.concatenate([membres[t] for t in choix if t in membres] or [np.array([], dtype=int)])
            if i.size == 0 or np.unique(y[i]).size < 2:
                return None
            total += c * (aire_sous_courbe(a[i], y[i]) - aire_sous_courbe(b[i], y[i]))
        return total

    obs = valeur(univers)
    if obs is None:
        raise GardeArret("contraste observé non calculable (une classe manque)")
    valeurs, degeneres = [], 0
    for _ in range(int(n_tirages)):
        choix = [univers[k] for k in rng.integers(0, len(univers), size=len(univers))]
        v = valeur(choix)
        if v is None:
            degeneres += 1
        else:
            valeurs.append(v)
    if degeneres > 0.01 * n_tirages:
        raise GardeArret(f"{degeneres} tirages sur {n_tirages} sans les deux classes")
    v = np.asarray(valeurs)
    q = (1.0 - niveau) / 2.0
    mauvais = int((v <= 0.0).sum()) if sens == "positif" else int((v >= 0.0).sum())
    return {"contraste": float(obs), "bas": float(np.quantile(v, q)), "haut": float(np.quantile(v, 1.0 - q)),
            "p_unilaterale": (1.0 + mauvais) / (v.size + 1.0), "tirages": int(v.size), "degeneres": degeneres,
            "sens": sens}
