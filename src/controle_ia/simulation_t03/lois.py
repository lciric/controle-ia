"""Lois des scores pour T0.3 : lois honnêtes, lois de classe K (copules), mauvaises spécifications.

Toutes les lois ont, action par action, une moyenne 0 et une variance 1 (sauf `moyennes`,
où l'agent i a la moyenne μ_i). Un lot a la forme (R, N, T). Une loi se décrit par un dict
sérialisable (consigné dans la grille et le manifeste) et se tire par `tirer(rng, R, loi)`.
"""
from __future__ import annotations

import math

import numpy as np
from scipy import special, stats

from ..gardes import GardeArret

MARGINALES = ("gauss", "exp", "student5", "gumbel")


def marginale(Z, nom: str) -> np.ndarray:
    """Transporte des N(0, 1) vers la marginale F₀ standardisée : X = F₀⁻¹(Φ(Z)), monotone en Z."""
    if nom == "gauss":
        return Z
    if nom == "exp":       # Exp(1) − 1 : quantile −log(1 − Φ(Z)) = −log Φ(−Z)
        return -special.log_ndtr(-Z) - 1.0
    if nom == "student5":  # t5 / √(5/3), queue calculée du côté précis
        q = stats.t.isf(special.ndtr(-np.abs(Z)), 5)
        return np.sign(Z) * q / math.sqrt(5.0 / 3.0)
    if nom == "gumbel":    # Gumbel (maximum) standardisée
        return (-np.log(-special.log_ndtr(Z)) - np.euler_gamma) / (math.pi / math.sqrt(6.0))
    raise GardeArret(f"marginale {nom!r} inconnue ({MARGINALES})")


def tirer(rng: np.random.Generator, R: int, loi: dict) -> np.ndarray:
    """Tire un lot (R, N, T) de la loi décrite. Clés : type, N, T, et les paramètres du type."""
    t, N, T = loi["type"], int(loi["N"]), int(loi["T"])
    if R < 1 or N < 1 or T < 1:
        raise GardeArret(f"tailles invalides R={R}, N={N}, T={T}")
    if t == "iid":
        return marginale(rng.standard_normal((R, N, T)), loi.get("marginale", "gauss"))
    if t == "ar1":         # copule gaussienne AR(1) stationnaire par agent, agents indépendants
        phi = float(loi["phi"])
        if not (-1.0 < phi < 1.0):
            raise GardeArret(f"φ = {phi} hors de ]−1, 1[")
        E = rng.standard_normal((R, N, T))
        Z = np.empty_like(E)
        Z[:, :, 0] = E[:, :, 0]
        s = math.sqrt(1.0 - phi * phi)
        for k in range(1, T):
            Z[:, :, k] = phi * Z[:, :, k - 1] + s * E[:, :, k]
        return marginale(Z, loi.get("marginale", "gauss"))
    if t == "equicorrelation":   # corrélation c entre agents au même pas, pas indépendants
        c = float(loi["c"])
        if not (0.0 <= c < 1.0):
            raise GardeArret(f"c = {c} hors de [0, 1[")
        U = rng.standard_normal((R, 1, T))
        E = rng.standard_normal((R, N, T))
        return math.sqrt(c) * U + math.sqrt(1.0 - c) * E
    if t == "effet_episode":     # u ~ N(0, τ²) commun à l'épisode, variance totale 1
        tau = float(loi["tau"])
        if not (0.0 <= tau < 1.0):
            raise GardeArret(f"τ = {tau} hors de [0, 1[")
        u = rng.normal(0.0, tau, size=(R, 1, 1)) if tau > 0 else np.zeros((R, 1, 1))
        E = rng.standard_normal((R, N, T))
        return u + math.sqrt(1.0 - tau * tau) * E
    if t == "moyennes":          # agent i de moyenne μ_i, bruit N(0, 1) indépendant
        mus = np.asarray(loi["mus"], dtype=float)
        if mus.shape != (N,):
            raise GardeArret(f"μ de forme {mus.shape} : ({N},) attendu")
        return mus[None, :, None] + rng.standard_normal((R, N, T))
    raise GardeArret(f"type de loi {t!r} inconnu")


def facteur_variance_ar1(phi: float, n: int) -> float:
    """Var(Σ_{k≤n} Z_k)/n pour un AR(1) gaussien stationnaire de variance 1."""
    if phi == 0.0:
        return 1.0
    return (1 + phi) / (1 - phi) - 2 * phi * (1 - phi ** n) / (n * (1 - phi) ** 2)
