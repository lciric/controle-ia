"""Exemple chiffré du document « le programme expliqué depuis zéro » (v2).

Illustration, pas un résultat : scores honnêtes simulés, indépendants, de loi normale centrée réduite.
Aucune donnée du programme n'est lue. Graines dérivées par numpy.random.SeedSequence (règle R9).

Ce que la v2 ajoute à la v1 (`exemple-chiffre-depuis-zero-v1.py`, laissée intacte) : l'horizon réel d'un épisode du
programme, dix actions d'un même agent (N = 1, T = 10 : texte scellé de T0.6, plan d'analyse, point 2), à côté de
l'horizon de 200 actions de la v1, choisi pour l'illustration.

- Horizon de 200 actions, budget B = 50 : mêmes calculs, même ordre de tirage et mêmes graines que la v1 (les douze
  premiers enfants de SeedSequence(20261110) sont ceux de la v1) ; la sortie de ces lignes doit être identique à celle
  de la v1, ce que le script vérifie contre la table V1_ATTENDU ci-dessous (copiée de la sortie de la v1).
- Horizon de 10 actions, budget B = 2,5 : même décalage par action et même part d'actions sabotées qu'à 200 actions
  (m = 5 sur 10 correspond à m = 100 sur 200 : δ = 0,5 ; m = 10 correspond à m = 200 : δ = 0,25) ; enfants 12 à 23.
  La ligne « toutes les dix actions sabotées à 0,5 σ » (budget 5) est donnée à part.
- La grille du paramètre ρ du processus e est celle de la v1, mise à l'échelle par √(200 / n0) : identique à la v1 pour
  n0 = 200 ; à n0 = 10, l'optimum dépasse la borne haute (1,0) de la grille de la v1.

Partie A (attaque par décalage, classe M de la note mathématique v3) : à budget total B fixé, on fait varier le nombre m
d'actions sabotées (décalage par action δ = B / m). On compare, au seuil de 1 % de fausses alertes : une action seule ;
le maximum de l'épisode (seuil exact) ; la somme à horizon fixé (formule fermée de L1) ; le processus e unilatéral toujours
valide (règle de Ville, seuil 1/α), lu à chaque action ; sa borne terminale (L3 b).

Partie B (attaque qui préserve le multi-ensemble des scores, classe C) : l'attaquant regroupe ses r plus hauts scores en un
bloc consécutif. Toute statistique symétrique (somme, maximum) est inchangée, trajectoire par trajectoire ; une somme
glissante courte le voit. À 200 actions, r = w = 10 (v1) ; à 10 actions, r = w = 3. Note de fin : avec une copule
autorégressive (classe K), à marges préservées, la somme n'est plus aveugle (note v3, section 4).

Usage : python -I exemple-chiffre-depuis-zero-v2.py
"""
import hashlib
import sys

import numpy as np
import scipy
from scipy.special import log_ndtr
from scipy.stats import norm

ENTROPIE = 20261110  # entropie racine de la v1, reprise telle quelle
N_ENFANTS = 24  # 0 à 11 : horizon de 200 (v1) ; 12 à 23 : horizon de 10 (v2)
ALPHA = 0.01
R = 20000
N0_LONG, B_LONG, MS_LONG = 200, 50.0, (10, 25, 50, 100, 200)
N0_EPISODE, B_EPISODE, MS_EPISODE = 10, 2.5, (1, 2, 5, 10)

# Graines (indices des enfants de SeedSequence(ENTROPIE).spawn(N_ENFANTS)), consignées ici et rappelées en sortie.
GRAINES_LONG = {"honnete": 0, "m": (1, 2, 3, 4, 5), "calendrier": (6, 7),
                "b_honnete": 8, "b_y": 9, "b_regroupement": 10, "b_copule": 11}
GRAINES_EPISODE = {"honnete": 12, "m": (13, 14, 15, 16), "calendrier": (17, 18),
                   "b_honnete": 19, "b_y": 20, "b_regroupement": 21, "b_copule": 22, "toutes_sabotees": 23}

# Lignes de la sortie de la v1 (journal de la v1, `b69932b1…`) que l'horizon de 200 doit reproduire à l'identique.
V1_ATTENDU = [
    "[A] n0 = 200, B = 50, alpha = 0.01, R = 20000",
    "[A] rho retenu (minimise la frontière à n0) = 0.23 ; frontière terminale S* = 47.424",
    "[A] seuil par action z = 2.3263 ; seuil exact du maximum c = 3.8894",
    "[A] honnête : fausses alertes du processus e (règle de Ville) = 0.0032",
    "[A]  10 ; 5.00 ; 0.9962 ; 1.0000 ; 0.8867 ; 0.7584 ; 0.5723",
    "[A]  25 ; 2.00 ; 0.3721 ; 0.5302 ; 0.8867 ; 0.7100 ; 0.5723",
    "[A]  50 ; 1.00 ; 0.0924 ; 0.0989 ; 0.8867 ; 0.6876 ; 0.5723",
    "[A] 100 ; 0.50 ; 0.0339 ; 0.0393 ; 0.8867 ; 0.6741 ; 0.5723",
    "[A] 200 ; 0.25 ; 0.0189 ; 0.0270 ; 0.8867 ; 0.6703 ; 0.5723",
    "[A] début ; 0.9712 ; 0.8861",
    "[A] fin ; 0.5910 ; 0.8860",
    "[B] somme ; 0.0102 ; 0.0102 ; True",
    "[B] maximum ; 0.0109 ; 0.0109 ; True",
    "[B] somme glissante (w = 10) ; 0.0093 ; 1.0000 ; False",
    "[B] autocorrélation d'ordre 1 ; 0.0082 ; 0.7195 ; False",
    "[B] multi-ensemble préservé : True",
    "[B] classe K (copule AR(1), phi = 0.5, marges N(0,1)) : somme unilatérale 0.0892 ; maximum 0.0093 (alpha = 0.01)",
]

SORTIE = []


def ecrire(ligne):
    SORTIE.append(ligne)
    print(ligne)


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


def grille_rho(n):
    """Grille de la v1 (0,01 à 1,0, 991 points) mise à l'échelle √(200 / n) : identique à la v1 pour n = 200."""
    return np.linspace(0.01, 1.0, 991) * np.sqrt(200.0 / n)


def rho_optimal(n, alpha):
    grille = grille_rho(n)
    valeurs = [frontiere(n, r, alpha) for r in grille]
    k = int(np.argmin(valeurs))
    if k == 0 or k == len(grille) - 1:
        raise SystemExit(f"rho optimal au bord de la grille (n = {n}, indice {k}) : grille à élargir")
    return float(grille[k])


def alarme_toujours_valide(x, rho, alpha):
    """Vrai si le processus e franchit 1/alpha à une action au plus tard à n0 (inclusivement)."""
    s = np.cumsum(x, axis=1)
    n = np.arange(1, x.shape[1] + 1)
    return (log_e_unilateral(s, n, rho) >= np.log(1.0 / alpha)).any(axis=1)


def partie_a(graines, n0, b, ms, g, m_cal, prefixe):
    z = norm.ppf(1.0 - ALPHA)
    rho = rho_optimal(n0, ALPHA)
    s_etoile = frontiere(n0, rho, ALPHA)
    borne_terminale = norm.sf((s_etoile - b) / np.sqrt(n0))
    somme_fixe = norm.sf(z - b / np.sqrt(n0))
    c_max = norm.ppf((1.0 - ALPHA) ** (1.0 / n0))
    ecrire(f"{prefixe} n0 = {n0}, B = {b:g}, alpha = {ALPHA}, R = {R}")
    ecrire(f"{prefixe} rho retenu (minimise la frontière à n0) = {rho:.2f} ; frontière terminale S* = {s_etoile:.3f}")
    ecrire(f"{prefixe} seuil par action z = {z:.4f} ; seuil exact du maximum c = {c_max:.4f}")
    rng0 = np.random.default_rng(graines[g["honnete"]])
    y0 = rng0.standard_normal((R, n0))
    fa_e = alarme_toujours_valide(y0, rho, ALPHA).mean()
    ecrire(f"{prefixe} honnête : fausses alertes du processus e (règle de Ville) = {fa_e:.4f}")
    ecrire(f"{prefixe} m ; delta ; P(une action sabotée > seuil par action) ; maximum de l'épisode ; "
           "somme à horizon fixé ; toujours valide (positions au hasard) ; borne terminale")
    p_e_cal = None
    for k, m in enumerate(ms):
        delta = b / m
        p_action = norm.sf(z - delta)
        p_max = 1.0 - norm.cdf(c_max) ** (n0 - m) * norm.cdf(c_max - delta) ** m
        rng = np.random.default_rng(graines[g["m"][k]])
        y = rng.standard_normal((R, n0))
        positions = np.argsort(rng.random((R, n0)), axis=1)[:, :m]
        x = y.copy()
        np.put_along_axis(x, positions, np.take_along_axis(x, positions, axis=1) + delta, axis=1)
        p_e = alarme_toujours_valide(x, rho, ALPHA).mean()
        if m == m_cal:
            p_e_cal = p_e
        ecrire(f"{prefixe} {m:3d} ; {delta:.2f} ; {p_action:.4f} ; {p_max:.4f} ; {somme_fixe:.4f} ; "
               f"{p_e:.4f} ; {borne_terminale:.4f}")
    m = m_cal
    delta = b / m
    ecrire(f"{prefixe} calendrier, m = {m}, delta = {delta:.2f} : toujours valide ; somme à horizon fixé")
    for k, (nom, debut) in enumerate((("début", 0), ("fin", n0 - m))):
        rng = np.random.default_rng(graines[g["calendrier"][k]])
        x = rng.standard_normal((R, n0))
        x[:, debut:debut + m] += delta
        p_e = alarme_toujours_valide(x, rho, ALPHA).mean()
        p_fixe = (x.sum(axis=1) / np.sqrt(n0) > z).mean()
        ecrire(f"{prefixe} {nom} ; {p_e:.4f} ; {p_fixe:.4f}")
    ecrire(f"{prefixe} prix de la garantie toujours valide, m = {m_cal}, positions au hasard : "
           f"somme à horizon fixé {somme_fixe:.4f} - toujours valide {p_e_cal:.4f} = "
           f"{100.0 * (somme_fixe - p_e_cal):.1f} points")
    return rho


def toutes_sabotees(graines, n0, delta, rho, i_graine, prefixe):
    """Toutes les actions de l'épisode sabotées au même décalage (budget n0·delta)."""
    z = norm.ppf(1.0 - ALPHA)
    b = n0 * delta
    c_max = norm.ppf((1.0 - ALPHA) ** (1.0 / n0))
    s_etoile = frontiere(n0, rho, ALPHA)
    p_action = norm.sf(z - delta)
    p_max = 1.0 - norm.cdf(c_max - delta) ** n0
    somme_fixe = norm.sf(z - b / np.sqrt(n0))
    borne_terminale = norm.sf((s_etoile - b) / np.sqrt(n0))
    rng = np.random.default_rng(graines[i_graine])
    x = rng.standard_normal((R, n0)) + delta
    p_e = alarme_toujours_valide(x, rho, ALPHA).mean()
    p_fixe_sim = (x.sum(axis=1) / np.sqrt(n0) > z).mean()
    p_max_sim = (x.max(axis=1) > c_max).mean()
    ecrire(f"{prefixe} toutes les {n0} actions sabotées, delta = {delta:.2f} (B = {b:g}) : une action {p_action:.4f} ; "
           f"maximum {p_max:.4f} (simulé {p_max_sim:.4f}) ; somme à horizon fixé {somme_fixe:.4f} "
           f"(simulé {p_fixe_sim:.4f}) ; toujours valide {p_e:.4f} ; borne terminale {borne_terminale:.4f}")


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


def partie_b(graines, n0, r, w, g, prefixe):
    rng_h = np.random.default_rng(graines[g["b_honnete"]])
    stats_h = statistiques(rng_h.standard_normal((R, n0)), w)
    seuils = {k: np.quantile(v, 1.0 - ALPHA) for k, v in stats_h.items()}
    rng_y = np.random.default_rng(graines[g["b_y"]])
    y = rng_y.standard_normal((R, n0))
    x = regrouper(y, r, np.random.default_rng(graines[g["b_regroupement"]]))
    stats_y = statistiques(y, w)
    stats_x = statistiques(x, w)
    ecrire(f"{prefixe} n0 = {n0}, r = {r}, R = {R}, seuils calibrés sur {R} épisodes honnêtes au quantile {1 - ALPHA}")
    ecrire(f"{prefixe} statistique ; taux d'alerte sans attaque ; taux d'alerte sous regroupement ; "
           "égalité trajectoire par trajectoire")
    for k in seuils:
        avant = (stats_y[k] > seuils[k]).mean()
        apres = (stats_x[k] > seuils[k]).mean()
        egal = bool(np.array_equal(stats_y[k], stats_x[k]))
        ecrire(f"{prefixe} {k} ; {avant:.4f} ; {apres:.4f} ; {egal}")
    ecrire(f"{prefixe} multi-ensemble préservé : {bool(np.array_equal(np.sort(x, axis=1), np.sort(y, axis=1)))}")
    phi = 0.5
    rng_k = np.random.default_rng(graines[g["b_copule"]])
    e = rng_k.standard_normal((R, n0))
    xk = np.empty_like(e)
    xk[:, 0] = e[:, 0]
    for t in range(1, n0):
        xk[:, t] = phi * xk[:, t - 1] + np.sqrt(1.0 - phi * phi) * e[:, t]
    z = norm.ppf(1.0 - ALPHA)
    taux_somme = (xk.sum(axis=1) / np.sqrt(n0) > z).mean()
    taux_max = (xk.max(axis=1) > norm.ppf((1.0 - ALPHA) ** (1.0 / n0))).mean()
    ecrire(f"{prefixe} classe K (copule AR(1), phi = {phi}, marges N(0,1)) : somme unilatérale {taux_somme:.4f} ; "
           f"maximum {taux_max:.4f} (alpha = {ALPHA})")


def verifier_v1():
    """Garde : l'horizon de 200 doit reproduire la sortie de la v1, ligne à ligne (préfixes [A] et [B])."""
    manquantes = [ligne for ligne in V1_ATTENDU if ligne not in SORTIE]
    if manquantes:
        for ligne in manquantes:
            print("[garde] ligne de la v1 non reproduite :", ligne)
        return False
    return True


def main():
    with open(__file__, "rb") as f:
        empreinte = hashlib.sha256(f.read()).hexdigest()
    graines = np.random.SeedSequence(ENTROPIE).spawn(N_ENFANTS)
    ecrire(f"python {sys.version.split()[0]} ; numpy {np.__version__} ; scipy {scipy.__version__} ; entropie {ENTROPIE}")
    ecrire(f"[graines] SeedSequence({ENTROPIE}).spawn({N_ENFANTS}) ; horizon 200 : {GRAINES_LONG} ; "
           f"horizon 10 : {GRAINES_EPISODE}")
    ecrire(f"[script] sha256 {empreinte}")
    partie_a(graines, N0_LONG, B_LONG, MS_LONG, GRAINES_LONG, 100, "[A]")
    partie_b(graines, N0_LONG, 10, 10, GRAINES_LONG, "[B]")
    rho10 = partie_a(graines, N0_EPISODE, B_EPISODE, MS_EPISODE, GRAINES_EPISODE, 5, "[A10]")
    toutes_sabotees(graines, N0_EPISODE, 0.5, rho10, GRAINES_EPISODE["toutes_sabotees"], "[A10]")
    partie_b(graines, N0_EPISODE, 3, 3, GRAINES_EPISODE, "[B10]")
    ok = verifier_v1()
    ecrire(f"[garde] horizon de 200 identique à la sortie de la v1 : {ok}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
