"""Statistiques vectorisées sur des lots d'épisodes de forme (R, N, T) — R répétitions.

Chaque fonction `lot_*` renvoie un tableau (R,), plus grand = plus suspect, et coïncide,
épisode par épisode, avec la référence scalaire de `controle_ia.agregateurs` (testé à 1e-9).
Les scores sont standardisés en amont : μ₀ = 0 et σ = 1 (ou z = x / σ_utilisé).
Les séries `serie_*` (N = 1) donnent la statistique courante après chaque action, pour
dater la première alarme ; leur maximum sur l'horizon est la statistique `lot_*`.
"""
from __future__ import annotations

import math

import numpy as np
from scipy.special import logsumexp

from ..agregateurs.processus_e import log_e_bilateral, log_e_unilateral
from ..gardes import GardeArret

LARGEURS_MULTI = (1, 2, 4, 8, 16, 32)
LAMBDAS_DETECTEUR = (0.25, 0.5, 1.0, 2.0)


def verifier_lot(Xb) -> np.ndarray:
    Xb = np.asarray(Xb, dtype=float)
    if Xb.ndim != 3 or min(Xb.shape) < 1:
        raise GardeArret(f"lot de forme {Xb.shape} : (R, N, T) attendu")
    if not np.all(np.isfinite(Xb)):
        raise GardeArret("lot avec valeurs non finies")
    return Xb


def ordre(Xb) -> np.ndarray:
    """(R, N, T) → (R, N·T) dans l'ordre « temps d'abord » : (0,0), (1,0), …, (N−1,0), (0,1), …"""
    Xb = verifier_lot(Xb)
    R, N, T = Xb.shape
    return Xb.transpose(0, 2, 1).reshape(R, N * T).copy()


def depuis_ordre(x, N: int, T: int) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    if x.ndim != 2 or x.shape[1] != N * T:
        raise GardeArret(f"ordre de lecture de forme {x.shape} : (R, {N * T}) attendu")
    return x.reshape(x.shape[0], T, N).transpose(0, 2, 1).copy()


# --- statistiques symétriques (invariantes par toute permutation des cases) ---
def lot_somme(Xb) -> np.ndarray:
    """Σ z sur valeurs triées : invariante au bit près par permutation (T1)."""
    x = ordre(Xb)
    return np.sort(x, axis=1).sum(axis=1)


def lot_max(Xb) -> np.ndarray:
    Xb = verifier_lot(Xb)
    return Xb.reshape(Xb.shape[0], -1).max(axis=1)


# --- statistiques d'ordre locales ---
def _sommes_glissantes(Xb, w: int) -> np.ndarray:
    R, N, T = Xb.shape
    if not (1 <= w <= T):
        raise GardeArret(f"fenêtre w = {w} hors de [1, T = {T}]")
    C = np.concatenate([np.zeros((R, N, 1)), np.cumsum(Xb, axis=2)], axis=2)
    return C[:, :, w:] - C[:, :, :-w]


def lot_glissante(Xb, w: int) -> np.ndarray:
    """Moyenne glissante de largeur w (en somme) : max sur agents et fenêtres (balayage de T3)."""
    Xb = verifier_lot(Xb)
    return _sommes_glissantes(Xb, w).max(axis=(1, 2))


def lot_balayage_multi(Xb, largeurs=LARGEURS_MULTI) -> np.ndarray:
    """Max de moyennes glissantes : max sur w ≤ T de lot_glissante(w)/√w."""
    Xb = verifier_lot(Xb)
    ws = [int(w) for w in largeurs if 1 <= int(w) <= Xb.shape[2]]
    if not ws:
        raise GardeArret(f"aucune largeur de {tuple(largeurs)} dans [1, T]")
    return np.max(np.stack([lot_glissante(Xb, w) / math.sqrt(w) for w in ws]), axis=0)


def lot_page(Xb, k: float = 0.5) -> np.ndarray:
    """Somme cumulée de Page par agent, C_t = max(0, C_{t−1} + z_t − k) ; max sur agents et pas."""
    Xb = verifier_lot(Xb)
    R, N, T = Xb.shape
    C = np.zeros((R, N))
    M = np.zeros((R, N))
    for t in range(T):
        C = np.maximum(0.0, C + Xb[:, :, t] - k)
        M = np.maximum(M, C)
    return M.max(axis=1)


def lot_co_elevation(Xb, m: int) -> np.ndarray:
    """Max sur les pas de la somme des m plus hauts scores du pas (axe agents, T3)."""
    Xb = verifier_lot(Xb)
    if not (1 <= m <= Xb.shape[1]):
        raise GardeArret(f"m = {m} hors de [1, N = {Xb.shape[1]}]")
    hauts = np.sort(Xb, axis=1)[:, -m:, :]
    return hauts.sum(axis=1).max(axis=1)


def lot_detecteur_e(Xb, lambdas=LAMBDAS_DETECTEUR) -> np.ndarray:
    return serie_detecteur_e(ordre(Xb), lambdas).max(axis=1)


# --- statistiques d'ordre globales ---
def lot_autocorr(Xb, absolue: bool = False) -> np.ndarray:
    """Moyenne sur les agents de l'autocorrélation de pas 1 (centrage par agent), T ≥ 3."""
    Xb = verifier_lot(Xb)
    if Xb.shape[2] < 3:
        raise GardeArret("autocorrélation : T ≥ 3 requis")
    Z = Xb - Xb.mean(axis=2, keepdims=True)
    num = (Z[:, :, :-1] * Z[:, :, 1:]).sum(axis=2)
    den = (Z * Z).sum(axis=2)
    r = np.where(den == 0.0, 0.0, num / np.where(den == 0.0, 1.0, den)).mean(axis=1)
    return np.abs(r) if absolue else r


def lot_suites(Xb) -> np.ndarray:
    """Wald-Wolfowitz au-dessus/au-dessous de la médiane de l'agent ; −z moyen (peu de suites = suspect)."""
    Xb = verifier_lot(Xb)
    med = np.median(Xb, axis=2, keepdims=True)
    b = Xb > med
    n1 = b.sum(axis=2).astype(float)
    n2 = Xb.shape[2] - n1
    runs = 1.0 + (b[:, :, 1:] != b[:, :, :-1]).sum(axis=2)
    n = n1 + n2
    mu = 2.0 * n1 * n2 / n + 1.0
    var = 2.0 * n1 * n2 * (2.0 * n1 * n2 - n1 - n2) / (n * n * (n - 1.0))
    ok = (n1 > 0) & (n2 > 0) & (var > 0)
    z = np.where(ok, (runs - mu) / np.sqrt(np.where(ok, var, 1.0)), 0.0)
    return -z.mean(axis=1)


def lot_correlation_agents(Xb) -> np.ndarray:
    """Moyenne des corrélations de Pearson entre séries d'agents (N ≥ 2, T ≥ 3)."""
    Xb = verifier_lot(Xb)
    R, N, T = Xb.shape
    if N < 2 or T < 3:
        raise GardeArret("corrélation entre agents : N ≥ 2 et T ≥ 3 requis")
    Xc = Xb - Xb.mean(axis=2, keepdims=True)
    normes = np.sqrt((Xc ** 2).sum(axis=2))
    if np.any(normes == 0):
        raise GardeArret("corrélation entre agents : série constante")
    C = np.einsum("rit,rjt->rij", Xc, Xc) / (normes[:, :, None] * normes[:, None, :])
    iu = np.triu_indices(N, k=1)
    return C[:, iu[0], iu[1]].mean(axis=1)


def lot_dispersion_agents(Xb, mus) -> np.ndarray:
    Xb = verifier_lot(Xb)
    mus = np.asarray(mus, dtype=float)
    if mus.shape != (Xb.shape[1],):
        raise GardeArret(f"μ de forme {mus.shape} : ({Xb.shape[1]},) attendu")
    return (Xb.shape[2] * (Xb.mean(axis=2) - mus[None, :]) ** 2).sum(axis=1)


# --- processus e (ordre de lecture, unités standardisées : σ = 1) ---
def serie_e(x, rho: float, cote: str) -> np.ndarray:
    """log E_n pour n = 1…n₀ ; x : (R, n₀) dans l'ordre de lecture."""
    if cote not in ("unilateral", "bilateral"):
        raise GardeArret(f"côté {cote!r} inconnu")
    x = np.asarray(x, dtype=float)
    S = np.cumsum(x, axis=1)
    n = np.arange(1, x.shape[1] + 1, dtype=float)[None, :]
    f = log_e_unilateral if cote == "unilateral" else log_e_bilateral
    return f(S, n, 1.0, rho)


def lot_e_max(Xb, rho: float, cote: str) -> np.ndarray:
    """max_n log E_n : alarme toujours valide si ≥ log(1/α) (Ville)."""
    return serie_e(ordre(Xb), rho, cote).max(axis=1)


def lot_e_terminal(Xb, rho: float) -> np.ndarray:
    """log E⁺_{n₀}, fonction de la seule somme terminale (invariante par permutation)."""
    Xb = verifier_lot(Xb)
    n0 = Xb.shape[1] * Xb.shape[2]
    return log_e_unilateral(lot_somme(Xb), float(n0), 1.0, rho)


# --- séries pour la datation de l'alarme (ordre de lecture, toute N ; pour Page et les
#     fenêtres, l'axe est celui d'un agent unique : N = 1) ---
def serie_page(x, k: float = 0.5) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    out = np.empty_like(x)
    C = np.zeros(x.shape[0])
    for t in range(x.shape[1]):
        C = np.maximum(0.0, C + x[:, t] - k)
        out[:, t] = C
    return out


def serie_detecteur_e(x, lambdas=LAMBDAS_DETECTEUR) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    lam = np.asarray(lambdas, dtype=float)
    if lam.ndim != 1 or lam.size == 0 or not np.all(lam > 0):
        raise GardeArret(f"λ = {lambdas} : liste non vide de réels > 0 attendue")
    log_poids = -math.log(lam.size)
    L = np.full((x.shape[0], lam.size), -np.inf)
    out = np.empty_like(x)
    for n in range(x.shape[1]):
        L = np.maximum(L, 0.0) + lam[None, :] * x[:, n:n + 1] - lam[None, :] ** 2 / 2.0
        out[:, n] = logsumexp(L + log_poids, axis=1)
    return out


def serie_glissante(x, w: int) -> np.ndarray:
    """Somme de la fenêtre de largeur w qui finit à l'action n (−∞ avant la w-ième action)."""
    x = np.asarray(x, dtype=float)
    if not (1 <= w <= x.shape[1]):
        raise GardeArret(f"fenêtre w = {w} hors de [1, {x.shape[1]}]")
    C = np.concatenate([np.zeros((x.shape[0], 1)), np.cumsum(x, axis=1)], axis=1)
    out = np.full(x.shape, -np.inf)
    out[:, w - 1:] = C[:, w:] - C[:, :-w]
    return out


def serie_balayage_multi(x, largeurs=LARGEURS_MULTI) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    ws = [int(w) for w in largeurs if 1 <= int(w) <= x.shape[1]]
    if not ws:
        raise GardeArret(f"aucune largeur de {tuple(largeurs)} dans [1, {x.shape[1]}]")
    return np.max(np.stack([serie_glissante(x, w) / math.sqrt(w) for w in ws]), axis=0)


def premiere_alarme(serie, seuil: float) -> np.ndarray:
    """Indice (0-basé) de la première action où la série atteint le seuil ; −1 si jamais."""
    serie = np.asarray(serie)
    touche = serie >= seuil
    return np.where(touche.any(axis=1), touche.argmax(axis=1), -1)


__all__ = [n for n in dir() if n.startswith(("lot_", "serie_"))] + [
    "verifier_lot", "ordre", "depuis_ordre", "premiere_alarme", "LARGEURS_MULTI", "LAMBDAS_DETECTEUR"]
