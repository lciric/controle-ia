"""Épisodes indexés (agent i, pas t) et ordre de lecture."""
from __future__ import annotations

from typing import Iterable

import numpy as np

from ..gardes import GardeArret


def verifier_episode(X) -> np.ndarray:
    """Garde : tableau réel fini de forme (N, T), N ≥ 1, T ≥ 1. Aucun repli silencieux."""
    X = np.asarray(X, dtype=float)
    if X.ndim != 2 or X.shape[0] < 1 or X.shape[1] < 1:
        raise GardeArret(f"épisode de forme {X.shape} : forme (N, T) attendue")
    if not np.all(np.isfinite(X)):
        raise GardeArret("épisode avec valeurs non finies (NaN ou infini)")
    return X


def episode(triplets: Iterable[tuple[int, int, float]], N: int, T: int) -> np.ndarray:
    """Construit un épisode (N, T) depuis un multi-ensemble de (i, t, score). Chaque case une fois."""
    X = np.full((N, T), np.nan)
    for i, t, x in triplets:
        if not (0 <= i < N and 0 <= t < T):
            raise GardeArret(f"indice ({i}, {t}) hors de ({N}, {T})")
        if not np.isnan(X[i, t]):
            raise GardeArret(f"case ({i}, {t}) fournie deux fois")
        X[i, t] = x
    if np.isnan(X).any():
        manquantes = int(np.isnan(X).sum())
        raise GardeArret(f"{manquantes} case(s) sans score")
    return X


def ordre_lecture(X) -> np.ndarray:
    """Scores dans l'ordre « temps d'abord » : (0,0), (1,0), …, (N−1,0), (0,1), …"""
    X = verifier_episode(X)
    return X.T.reshape(-1).copy()
