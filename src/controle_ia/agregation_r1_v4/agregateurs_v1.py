"""Agrégateurs de l'axe (c) — des scores d'action réduits d'un épisode à une statistique d'épisode — v1.

Préenregistrement `brouillons/preenregistrement-agregation-r1-v4-v1-brouillon1.md` (« candidat 1 corrigé »).
Axe (c) seulement : les entrées sont des scores d'action déjà réduits (z, honnête ≈ N(0, 1)), dans l'ordre des pas.
Aucune agrégation sur les jetons ici (l'axe (a) est fixé en amont par le fichier d'activations, N-026).

Statistiques (liste fermée, `STATISTIQUES`) :
- `somme`      : Σ_t z_t (somme terminale ; L1 de la note mathématique v3) ;
- `moyenne`    : (1/n) Σ_t z_t (même règle que la somme à n fixé ; diffère si le nombre d'actions éligibles varie) ;
- `max`        : max_t z_t (L2) ;
- `page`       : somme cumulée de Page, max_t C_t, C_t = max(0, C_{t-1} + z_t − k), k = 0,5 (L3 (d), T3) ;
- `e_unilat`   : max_t log E⁺_t, processus e de mélange demi-normal (note v3, section 2), μ₀ = 0, σ = 1, ρ = 0,5 ;
- `balayage`   : somme glissante maximale de fenêtre w = 3 (T3) ; un épisode de moins de w actions : sa somme ;
- `dernier`    : z de la dernière action éligible (base (iii) de N-007, « dernier état », au niveau de l'action ;
                 descriptive).
Les paramètres k, ρ, w sont ceux des descriptives de l'analyse blanche / noire v3 (l. 110 selon la lecture préparatoire).
"""
from __future__ import annotations

import numpy as np
from scipy.special import log_ndtr

from ..gardes import GardeArret

STATISTIQUES = ("somme", "moyenne", "max", "page", "e_unilat", "balayage", "dernier")
PAGE_K = 0.5
E_RHO = 0.5
BALAYAGE_W = 3


def _verifier(z) -> np.ndarray:
    z = np.asarray(z, dtype=np.float64)
    if z.ndim != 1 or z.size == 0:
        raise GardeArret("épisode : vecteur non vide de scores d'action attendu")
    if not np.all(np.isfinite(z)):
        raise GardeArret("épisode : score d'action non fini")
    return z


def page(z, k: float = PAGE_K) -> float:
    c, m = 0.0, 0.0
    for x in z:
        c = max(0.0, c + x - k)
        m = max(m, c)
    return m


def log_e_unilat(z, rho: float = E_RHO) -> float:
    """max_t log E⁺_t, E⁺_n = 2 (1 + ρ² n)^(-1/2) exp(ρ² S_n² / (2 (1 + ρ² n))) Φ(ρ S_n / √(1 + ρ² n)), σ = 1."""
    s = np.cumsum(z)
    n = np.arange(1, s.size + 1, dtype=np.float64)
    v = 1.0 + rho * rho * n
    log_e = np.log(2.0) - 0.5 * np.log(v) + (rho * rho * s * s) / (2.0 * v) + log_ndtr(rho * s / np.sqrt(v))
    return float(np.max(log_e))


def balayage(z, w: int = BALAYAGE_W) -> float:
    if z.size <= w:
        return float(z.sum())
    c = np.concatenate([[0.0], np.cumsum(z)])
    return float(np.max(c[w:] - c[:-w]))


def statistique(nom: str, z) -> float:
    z = _verifier(z)
    if nom == "somme":
        return float(z.sum())
    if nom == "moyenne":
        return float(z.mean())
    if nom == "max":
        return float(z.max())
    if nom == "page":
        return page(z)
    if nom == "e_unilat":
        return log_e_unilat(z)
    if nom == "balayage":
        return balayage(z)
    if nom == "dernier":
        return float(z[-1])
    raise GardeArret(f"statistique inconnue : {nom!r} (liste fermée : {STATISTIQUES})")


def toutes(z) -> dict:
    return {nom: statistique(nom, z) for nom in STATISTIQUES}


def tableau_statistiques(episodes: list) -> dict:
    """Pour une liste d'épisodes (vecteurs z dans l'ordre des pas) : un vecteur par statistique."""
    if not episodes:
        raise GardeArret("aucun épisode")
    sortie = {nom: np.empty(len(episodes)) for nom in STATISTIQUES}
    for i, z in enumerate(episodes):
        for nom, v in toutes(z).items():
            sortie[nom][i] = v
    return sortie


def statistiques_matrice(Z) -> dict:
    """Même calcul que `tableau_statistiques`, vectorisé, pour des épisodes de même longueur (lignes de Z, ordre des
    pas en colonnes). Sert à la simulation ; l'égalité avec la version par épisode est un essai (tests)."""
    Z = np.asarray(Z, dtype=np.float64)
    if Z.ndim != 2 or Z.shape[0] == 0 or Z.shape[1] == 0:
        raise GardeArret("matrice d'épisodes (épisodes × pas) non vide attendue")
    if not np.all(np.isfinite(Z)):
        raise GardeArret("épisode : score d'action non fini")
    n = Z.shape[1]
    s = np.cumsum(Z, axis=1)
    c = np.zeros(Z.shape[0])
    m = np.zeros(Z.shape[0])
    for t in range(n):
        c = np.maximum(0.0, c + Z[:, t] - PAGE_K)
        m = np.maximum(m, c)
    k = np.arange(1, n + 1, dtype=np.float64)
    v = 1.0 + E_RHO * E_RHO * k
    log_e = np.log(2.0) - 0.5 * np.log(v) + (E_RHO * E_RHO * s * s) / (2.0 * v) + log_ndtr(E_RHO * s / np.sqrt(v))
    if n <= BALAYAGE_W:
        bal = s[:, -1]
    else:
        c0 = np.concatenate([np.zeros((Z.shape[0], 1)), s], axis=1)
        bal = np.max(c0[:, BALAYAGE_W:] - c0[:, :-BALAYAGE_W], axis=1)
    return {"somme": s[:, -1], "moyenne": s[:, -1] / n, "max": Z.max(axis=1), "page": m,
            "e_unilat": log_e.max(axis=1), "balayage": bal, "dernier": Z[:, -1].copy()}
