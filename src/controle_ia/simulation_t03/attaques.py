"""Attaques de T0.3 dans l'ordre de lecture x : (R, n₀) (pour N = 1, l'axe du temps).

- Classe M : décalages δ_k ≥ 0 sur m positions, Σ δ_k = B (budget total), positions selon un schéma.
- Classe C : réarrangements, éventuellement dépendants des données, du multi-ensemble de chaque
  épisode ; ils le préservent exactement (testé).
"""
from __future__ import annotations

import numpy as np

from ..gardes import GardeArret
from .lots import depuis_ordre, ordre

SCHEMAS = ("aleatoire", "un_agent", "reparti", "bloc", "debut", "fin", "uniforme", "adaptatif")


def melanger(a, rng: np.random.Generator) -> np.ndarray:
    """Permutation uniforme indépendante de chaque ligne."""
    a = np.asarray(a)
    return np.take_along_axis(a, np.argsort(rng.random(a.shape), axis=-1), axis=-1)


def _distincts(rng, R: int, n: int, m: int) -> np.ndarray:
    return np.argsort(rng.random((R, n)), axis=1)[:, :m]


# --- classe M ---
def positions(schema: str, m: int, N: int, T: int, R: int, rng: np.random.Generator,
              y=None) -> np.ndarray:
    """m positions distinctes par épisode, dans l'ordre de lecture (agent = k mod N, pas = k div N)."""
    n0 = N * T
    if not (1 <= m <= n0):
        raise GardeArret(f"m = {m} hors de [1, n₀ = {n0}]")
    if schema == "aleatoire":
        return _distincts(rng, R, n0, m)
    if schema == "debut":
        return np.tile(np.arange(m), (R, 1))
    if schema == "fin":
        return np.tile(np.arange(n0 - m, n0), (R, 1))
    if schema == "uniforme":
        return np.tile(((np.arange(m) + 0.5) * n0 / m).astype(np.int64), (R, 1))
    if schema == "bloc":
        s = rng.integers(0, n0 - m + 1, size=R)
        return s[:, None] + np.arange(m)[None, :]
    if schema == "un_agent":
        if m > T:
            raise GardeArret(f"un seul agent : m = {m} > T = {T}")
        return _distincts(rng, R, T, m) * N
    if schema == "reparti":
        comptes = [m // N + (1 if i < m % N else 0) for i in range(N)]
        if max(comptes) > T:
            raise GardeArret(f"réparti : {max(comptes)} actions par agent > T = {T}")
        return np.concatenate([_distincts(rng, R, T, c) * N + i for i, c in enumerate(comptes) if c > 0],
                              axis=1)
    if schema == "adaptatif":   # les m actions honnêtes de plus bas score : cachées au max
        if y is None:
            raise GardeArret("schéma adaptatif : scores honnêtes requis")
        return np.argsort(np.asarray(y), axis=1, kind="stable")[:, :m]
    raise GardeArret(f"schéma {schema!r} inconnu ({SCHEMAS})")


def decalages(genre: str, m: int, B: float, R: int, rng: np.random.Generator) -> np.ndarray:
    """δ de forme (R, m), Σ δ = B par épisode : égaux, ou poids de Dirichlet(1, …, 1) tirés par épisode."""
    if genre == "egaux":
        return np.full((R, m), B / m)
    if genre == "dirichlet":
        g = rng.standard_gamma(1.0, size=(R, m))
        return B * g / g.sum(axis=1, keepdims=True)
    raise GardeArret(f"décalages {genre!r} inconnus")


def appliquer_decalages(y, P, delta) -> np.ndarray:
    y = np.asarray(y, dtype=float)
    P = np.asarray(P)
    Ps = np.sort(P, axis=1)
    if Ps.shape[0] != y.shape[0] or Ps.min() < 0 or Ps.max() >= y.shape[1] or np.any(np.diff(Ps, axis=1) <= 0):
        raise GardeArret("positions de sabotage invalides (hors bornes ou répétées)")
    x = y.copy()
    x[np.arange(y.shape[0])[:, None], P] += delta
    return x


# --- classe C ---
def tri_croissant(x) -> np.ndarray:
    return np.sort(np.asarray(x, dtype=float), axis=1)


def top_r_a_la_fin(x, r: int) -> np.ndarray:
    """Les r plus hautes valeurs passent en fin d'horizon ; ordres relatifs conservés (T4)."""
    x = np.asarray(x, dtype=float)
    R, n0 = x.shape
    if not (1 <= r <= n0):
        raise GardeArret(f"r = {r} hors de [1, {n0}]")
    o = np.argsort(x, axis=1, kind="stable")
    haut = np.zeros(x.shape, dtype=bool)
    np.put_along_axis(haut, o[:, -r:], True, axis=1)
    cle = np.arange(n0)[None, :] + n0 * haut
    return np.take_along_axis(x, np.argsort(cle, axis=1, kind="stable"), axis=1)


def bloc_top_r(x, r: int, rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray]:
    """Les r plus hautes valeurs, dans un ordre aléatoire, forment une suite consécutive placée à
    une position uniforme ; le reste est dans un ordre aléatoire (T3). Renvoie (x, début)."""
    x = np.asarray(x, dtype=float)
    R, n0 = x.shape
    if not (1 <= r < n0):
        raise GardeArret(f"r = {r} hors de [1, {n0}[")
    o = np.argsort(x, axis=1)
    hi = melanger(np.take_along_axis(x, o[:, -r:], axis=1), rng)
    lo = melanger(np.take_along_axis(x, o[:, :-r], axis=1), rng)
    debut = rng.integers(0, n0 - r + 1, size=R)
    pos = np.arange(n0)[None, :]
    dans = (pos >= debut[:, None]) & (pos < debut[:, None] + r)
    out = np.empty_like(x)
    out[dans] = hi.ravel()
    out[~dans] = lo.ravel()
    return out, debut


def rebrassage(x, rng: np.random.Generator) -> np.ndarray:
    """Permutation uniforme de toutes les positions (T2 avec H = toutes les permutations)."""
    return melanger(np.asarray(x, dtype=float), rng)


def rebrassage_intra_agent(Xb, rng: np.random.Generator) -> np.ndarray:
    """Permutation uniforme du temps, indépendante pour chaque agent : (R, N, T) → (R, N, T)."""
    return melanger(np.asarray(Xb, dtype=float), rng)


def _hors_bloc(rng, debut, r: int, n0: int) -> np.ndarray:
    u = rng.integers(0, n0 - r, size=debut.size)
    return np.where(u < debut, u, u + r)


def apparier(x, debut, r: int, cible: str, rng: np.random.Generator, iterations: int):
    """Attaquant adaptatif de classe C (T3) : échanges gloutons hors de la suite [début, début + r[
    pour amener la statistique globale (`autocorr` : Σ Z_k Z_{k+1} ; `suites` : nombre de
    changements de côté de la médiane) sur une cible tirée d'un rebrassage uniforme du même
    multi-ensemble (sa loi nulle par permutation). Renvoie (x réarrangé, écart final à la cible)."""
    x = np.asarray(x, dtype=float)
    R, n0 = x.shape
    debut = np.asarray(debut)
    if cible not in ("autocorr", "suites"):
        raise GardeArret(f"cible {cible!r} inconnue")
    moy = x.mean(axis=1, keepdims=True)
    Z = x - moy
    P = melanger(Z, rng)
    lignes = np.arange(R)
    if cible == "autocorr":
        A = (Z[:, :-1] * Z[:, 1:]).sum(axis=1)
        tgt = (P[:, :-1] * P[:, 1:]).sum(axis=1)
        m = None
    else:
        med = np.median(Z, axis=1, keepdims=True)
        m = med[:, 0]
        sg, sp = Z > med, P > med
        A = (sg[:, 1:] != sg[:, :-1]).sum(axis=1).astype(float)
        tgt = (sp[:, 1:] != sp[:, :-1]).sum(axis=1).astype(float)
    Zp = np.concatenate([np.zeros((R, 1)), Z, np.zeros((R, 1))], axis=1)   # indices décalés de 1
    Xp = np.concatenate([np.zeros((R, 1)), x, np.zeros((R, 1))], axis=1)   # valeurs d'origine, échangées
                                                                           # avec Z : multi-ensemble exact

    def desaccord(a, b, va, vb):
        existe = (a >= 1) & (b <= n0)
        return (existe & ((va > m) != (vb > m))).astype(float)

    for _ in range(iterations):
        i, j = _hors_bloc(rng, debut, r, n0), _hors_bloc(rng, debut, r, n0)
        i, j = np.minimum(i, j), np.maximum(i, j)
        ok = (j - i) >= 2
        I, J = i + 1, j + 1
        zi, zj = Zp[lignes, I], Zp[lignes, J]
        zim, zip_, zjm, zjp = Zp[lignes, I - 1], Zp[lignes, I + 1], Zp[lignes, J - 1], Zp[lignes, J + 1]
        if cible == "autocorr":
            dA = (zj - zi) * (zim + zip_ - zjm - zjp)
        else:
            avant = (desaccord(I - 1, I, zim, zi) + desaccord(I, I + 1, zi, zip_)
                     + desaccord(J - 1, J, zjm, zj) + desaccord(J, J + 1, zj, zjp))
            apres = (desaccord(I - 1, I, zim, zj) + desaccord(I, I + 1, zj, zip_)
                     + desaccord(J - 1, J, zjm, zi) + desaccord(J, J + 1, zi, zjp))
            dA = apres - avant
        acc = ok & (np.abs(A + dA - tgt) < np.abs(A - tgt))
        Zp[lignes[acc], I[acc]] = zj[acc]
        Zp[lignes[acc], J[acc]] = zi[acc]
        xi, xj = Xp[lignes[acc], I[acc]], Xp[lignes[acc], J[acc]]
        Xp[lignes[acc], I[acc]] = xj
        Xp[lignes[acc], J[acc]] = xi
        A = A + np.where(acc, dA, 0.0)
    return Xp[:, 1:-1].copy(), A - tgt


def co_elevation_top(Xb, mc: int, rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray]:
    """Les mc plus hautes valeurs de l'épisode sont placées chez mc agents distincts au même pas
    (pas uniforme) ; le reste est réparti uniformément sur les autres cases (T3, axe agents)."""
    Xb = np.asarray(Xb, dtype=float)
    R, N, T = Xb.shape
    if not (1 <= mc <= N):
        raise GardeArret(f"mc = {mc} hors de [1, N = {N}]")
    x = ordre(Xb)
    o = np.argsort(x, axis=1)
    top = melanger(np.take_along_axis(x, o[:, -mc:], axis=1), rng)
    reste = melanger(np.take_along_axis(x, o[:, :-mc], axis=1), rng)
    pas = rng.integers(0, T, size=R)
    agents = np.argsort(rng.random((R, N)), axis=1)[:, :mc]
    dans = np.zeros(x.shape, dtype=bool)
    np.put_along_axis(dans, pas[:, None] * N + agents, True, axis=1)
    out = np.empty_like(x)
    out[dans] = top.ravel()
    out[~dans] = reste.ravel()
    return depuis_ordre(out, N, T), pas
