"""Exemple chiffré du document « le programme expliqué depuis zéro » (v1).

Illustration, pas un résultat : scores honnêtes simulés, indépendants, de loi normale centrée réduite.
Aucune donnée du programme n'est lue. Graines dérivées par numpy.random.SeedSequence (règle R9).

Partie A (attaque par décalage, classe M de la note mathématique v3) : à budget total B fixé, on fait varier
le nombre m d'actions sabotées (décalage par action delta = B / m). On compare, au seuil de 1 % de fausses
alertes : une action seule ; le maximum de l'épisode ; la somme à horizon fixé ; le processus e unilatéral
toujours valide (règle de Ville, seuil 1/alpha), lu à chaque action.

Partie B (attaque qui préserve le multi-ensemble des scores, classe C) : l'attaquant regroupe ses r plus hauts
scores en un bloc consécutif. Toute statistique symétrique (somme, maximum) est inchangée, trajectoire par
trajectoire ; une somme glissante courte le voit. Note de fin : avec une copule autorégressive (classe K), à
marges préservées, la somme n'est plus aveugle (note v3, section 4).

Usage : python -I exemple-chiffre-depuis-zero-v1.py
"""
import sys

import numpy as np
import scipy
from scipy.special import log_ndtr
from scipy.stats import norm

ENTROPIE = 20261110  # entropie racine, fixée à l'écriture du script
ALPHA = 0.01
N0 = 200
B = 50.0
R = 20000


def log_e_unilateral(s, n, rho):
    """Logarithme du processus e unilatéral à mélange demi-normal (note v3, section 2), sigma = 1."""
    v = 1.0 + rho * rho * n
    return (np.log(2.0) - 0.5 * np.log(v) + rho * rho * s * s / (2.0 * v)
            + log_ndtr(rho * s / np.sqrt(v)))


def frontiere(n, rho, alpha):
    """Plus petite somme S telle que E+_n(S) >= 1/alpha (le processus est croissant en S)."""
    bas, haut = 0.0, 50.0 * np.sqrt(n)
    for _ in range(200):
        milieu = 0.5 * (bas + haut)
        if log_e_unilateral(milieu, n, rho) >= np.log(1.0 / alpha):
            haut = milieu
        else:
            bas = milieu
    return haut


def rho_optimal(n, alpha):
    grille = np.linspace(0.01, 1.0, 991)
    valeurs = [frontiere(n, r, alpha) for r in grille]
    return float(grille[int(np.argmin(valeurs))])


def alarme_toujours_valide(x, rho, alpha):
    """Vrai si le processus e franchit 1/alpha à une action au plus tard à n0 (inclusivement)."""
    s = np.cumsum(x, axis=1)
    n = np.arange(1, x.shape[1] + 1)
    return (log_e_unilateral(s, n, rho) >= np.log(1.0 / alpha)).any(axis=1)


def partie_a(graines):
    z = norm.ppf(1.0 - ALPHA)
    rho = rho_optimal(N0, ALPHA)
    s_etoile = frontiere(N0, rho, ALPHA)
    borne_terminale = norm.sf((s_etoile - B) / np.sqrt(N0))
    somme_fixe = norm.sf(z - B / np.sqrt(N0))
    c_max = norm.ppf((1.0 - ALPHA) ** (1.0 / N0))
    print(f"[A] n0 = {N0}, B = {B:g}, alpha = {ALPHA}, R = {R}")
    print(f"[A] rho retenu (minimise la frontière à n0) = {rho:.2f} ; frontière terminale S* = {s_etoile:.3f}")
    print(f"[A] seuil par action z = {z:.4f} ; seuil exact du maximum c = {c_max:.4f}")
    rng0 = np.random.default_rng(graines[0])
    y0 = rng0.standard_normal((R, N0))
    fa_e = alarme_toujours_valide(y0, rho, ALPHA).mean()
    print(f"[A] honnête : fausses alertes du processus e (règle de Ville) = {fa_e:.4f}")
    print("[A] m ; delta ; P(une action sabotée > seuil par action) ; maximum de l'épisode ; "
          "somme à horizon fixé ; toujours valide (positions au hasard) ; borne terminale")
    for k, m in enumerate((10, 25, 50, 100, 200)):
        delta = B / m
        p_action = norm.sf(z - delta)
        p_max = 1.0 - norm.cdf(c_max) ** (N0 - m) * norm.cdf(c_max - delta) ** m
        rng = np.random.default_rng(graines[1 + k])
        y = rng.standard_normal((R, N0))
        positions = np.argsort(rng.random((R, N0)), axis=1)[:, :m]
        x = y.copy()
        np.put_along_axis(x, positions, np.take_along_axis(x, positions, axis=1) + delta, axis=1)
        p_e = alarme_toujours_valide(x, rho, ALPHA).mean()
        print(f"[A] {m:3d} ; {delta:.2f} ; {p_action:.4f} ; {p_max:.4f} ; {somme_fixe:.4f} ; "
              f"{p_e:.4f} ; {borne_terminale:.4f}")
    m = 100
    delta = B / m
    print(f"[A] calendrier, m = {m}, delta = {delta:.2f} : toujours valide ; somme à horizon fixé")
    for k, (nom, debut) in enumerate((("début", 0), ("fin", N0 - m))):
        rng = np.random.default_rng(graines[6 + k])
        x = rng.standard_normal((R, N0))
        x[:, debut:debut + m] += delta
        p_e = alarme_toujours_valide(x, rho, ALPHA).mean()
        p_fixe = (x.sum(axis=1) / np.sqrt(N0) > z).mean()
        print(f"[A] {nom} ; {p_e:.4f} ; {p_fixe:.4f}")


def regrouper(y, r, rng):
    """Classe C : les r plus hauts scores forment un bloc consécutif à une place tirée au hasard."""
    n = y.shape[1]
    x = np.empty_like(y)
    for i in range(y.shape[0]):
        ordre = np.argsort(y[i])
        hauts = np.sort(y[i, ordre[-r:]])
        masque = np.ones(n, dtype=bool)
        masque[ordre[-r:]] = False
        reste = y[i, masque]
        place = rng.integers(0, n - r + 1)
        x[i] = np.concatenate([reste[:place], hauts, reste[place:]])
    return x


def statistiques(x, w):
    # Somme des scores triés : même valeur mathématique que la somme, et même arrondi quel que soit l'ordre
    # des actions (une somme flottante dans l'ordre des actions diffère au dernier bit après réarrangement).
    somme = np.sort(x, axis=1).sum(axis=1)
    maximum = x.max(axis=1)
    c = np.cumsum(np.pad(x, ((0, 0), (1, 0))), axis=1)
    glissante = (c[:, w:] - c[:, :-w]).max(axis=1)
    xc = x - x.mean(axis=1, keepdims=True)
    autocorr = (xc[:, 1:] * xc[:, :-1]).sum(axis=1) / (xc * xc).sum(axis=1)
    return {"somme": somme, "maximum": maximum, f"somme glissante (w = {w})": glissante,
            "autocorrélation d'ordre 1": autocorr}


def partie_b(graines):
    r, w = 10, 10
    rng_h = np.random.default_rng(graines[8])
    stats_h = statistiques(rng_h.standard_normal((R, N0)), w)
    seuils = {k: np.quantile(v, 1.0 - ALPHA) for k, v in stats_h.items()}
    rng_y = np.random.default_rng(graines[9])
    y = rng_y.standard_normal((R, N0))
    x = regrouper(y, r, np.random.default_rng(graines[10]))
    stats_y = statistiques(y, w)
    stats_x = statistiques(x, w)
    print(f"[B] n0 = {N0}, r = {r}, R = {R}, seuils calibrés sur {R} épisodes honnêtes au quantile {1 - ALPHA}")
    print("[B] statistique ; taux d'alerte sans attaque ; taux d'alerte sous regroupement ; égalité trajectoire par trajectoire")
    for k in seuils:
        avant = (stats_y[k] > seuils[k]).mean()
        apres = (stats_x[k] > seuils[k]).mean()
        egal = bool(np.array_equal(stats_y[k], stats_x[k]))
        print(f"[B] {k} ; {avant:.4f} ; {apres:.4f} ; {egal}")
    print("[B] multi-ensemble préservé :", bool(np.array_equal(np.sort(x, axis=1), np.sort(y, axis=1))))
    phi = 0.5
    rng_k = np.random.default_rng(graines[11])
    e = rng_k.standard_normal((R, N0))
    xk = np.empty_like(e)
    xk[:, 0] = e[:, 0]
    for t in range(1, N0):
        xk[:, t] = phi * xk[:, t - 1] + np.sqrt(1.0 - phi * phi) * e[:, t]
    z = norm.ppf(1.0 - ALPHA)
    taux_somme = (xk.sum(axis=1) / np.sqrt(N0) > z).mean()
    taux_max = (xk.max(axis=1) > norm.ppf((1.0 - ALPHA) ** (1.0 / N0))).mean()
    print(f"[B] classe K (copule AR(1), phi = {phi}, marges N(0,1)) : somme unilatérale {taux_somme:.4f} ; "
          f"maximum {taux_max:.4f} (alpha = {ALPHA})")


def main():
    graines = np.random.SeedSequence(ENTROPIE).spawn(12)
    print(f"python {sys.version.split()[0]} ; numpy {np.__version__} ; scipy {scipy.__version__} ; entropie {ENTROPIE}")
    partie_a(graines)
    partie_b(graines)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
