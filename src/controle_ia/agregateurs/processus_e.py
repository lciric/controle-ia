"""Processus e de mélange normal sur la somme des scores (note mathématique v2, section 2).

Avec S_n = Σ_{k≤n} (X_k − μ₀) et V_n = σ²n :
- bilatéral, λ ~ N(0, ρ²) : E_n = (1 + ρ²V_n)^(−1/2) · exp(ρ²S_n² / (2(1 + ρ²V_n))) ;
- unilatéral, λ demi-normal : E⁺_n = 2·(1 + ρ²V_n)^(−1/2) · exp(ρ²S_n² / (2(1 + ρ²V_n))) · Φ(ρS_n / √(1 + ρ²V_n)).
Valides (surmartingales positives d'espérance 1 sous P₀) si les incréments sont
indépendants ou des différences de martingale, μ₀ connu, σ connu ou majoré, et la loi
sous-gaussienne de paramètre σ². Calculs en logarithme pour éviter les débordements.
"""
from __future__ import annotations

import numpy as np
from scipy.special import log_ndtr

from ..gardes import GardeArret
from .indexation import ordre_lecture


def _verifier(rho: float, sigma: float) -> None:
    if not (rho > 0 and np.isfinite(rho)):
        raise GardeArret(f"ρ = {rho} : réel strictement positif attendu")
    if not (sigma > 0 and np.isfinite(sigma)):
        raise GardeArret(f"σ = {sigma} : réel strictement positif attendu")


def log_e_bilateral(S, n, sigma: float, rho: float) -> np.ndarray:
    _verifier(rho, sigma)
    S, n = np.asarray(S, float), np.asarray(n, float)
    a = 1.0 + rho * rho * sigma * sigma * n
    return -0.5 * np.log(a) + rho * rho * S * S / (2.0 * a)


def log_e_unilateral(S, n, sigma: float, rho: float) -> np.ndarray:
    _verifier(rho, sigma)
    S, n = np.asarray(S, float), np.asarray(n, float)
    a = 1.0 + rho * rho * sigma * sigma * n
    return np.log(2.0) - 0.5 * np.log(a) + rho * rho * S * S / (2.0 * a) + log_ndtr(rho * S / np.sqrt(a))


def e_bilateral(S, n, sigma: float, rho: float) -> np.ndarray:
    return np.exp(log_e_bilateral(S, n, sigma, rho))


def e_unilateral(S, n, sigma: float, rho: float) -> np.ndarray:
    return np.exp(log_e_unilateral(S, n, sigma, rho))


def trajectoire_e(X, mu0: float, sigma: float, rho: float, cote: str = "unilateral",
                  frontieres_de_pas: bool = False) -> np.ndarray:
    """log E_n le long de l'ordre de lecture (par action, ou aux frontières de pas si demandé)."""
    if cote not in ("unilateral", "bilateral"):
        raise GardeArret(f"côté {cote!r} inconnu")
    x = ordre_lecture(X) - mu0
    S = np.cumsum(x)
    n = np.arange(1, x.size + 1, dtype=float)
    if frontieres_de_pas:
        N = np.asarray(X).shape[0]
        S, n = S[N - 1::N], n[N - 1::N]
    f = log_e_unilateral if cote == "unilateral" else log_e_bilateral
    return f(S, n, sigma, rho)


def premiere_alarme(log_e: np.ndarray, alpha: float) -> int | None:
    """Indice (0-basé) de la première alarme log E_n ≥ log(1/α), ou None."""
    if not (0 < alpha < 1):
        raise GardeArret(f"α = {alpha} hors de ]0, 1[")
    idx = np.flatnonzero(np.asarray(log_e) >= np.log(1.0 / alpha))
    return int(idx[0]) if idx.size else None
