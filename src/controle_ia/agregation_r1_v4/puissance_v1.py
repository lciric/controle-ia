"""Puissance par simulation, calée sur les aires d'action publiées de P3 — v1.

Modèle (gaussien, classe M de la note mathématique v3) : 60 tâches ; par tâche un épisode honnête et un épisode saboteur de
n = 10 actions ; z = u_tâche + e_épisode + ε, u ~ N(0, τ²), e ~ N(0, η²), ε ~ N(0, 1) ; chaque action du saboteur reçoit le
décalage d (sabotage dense, m = n : le saboteur de P3 gonfle le coût à chaque proposition). Le décalage est tiré de l'aire
d'action visée : aire = Φ(d / √(2 (1 + τ² + η²))).
Épisodes hybrides (m < n) : l'épisode honnête d'une tâche dont m positions sont remplacées par les actions du saboteur de la
même tâche aux mêmes pas ; m = 1 : les dix positions ; 1 < m < n : dix sous-ensembles tirés par tâche.
Sortie : moyenne et écart type, sur R répliques (mêmes tirages pour toutes les valeurs de m), des aires d'épisode de chaque
statistique, des différences
somme − max ; puissance approchée d'un test unilatéral au niveau a : Φ(|E Δ| / sd Δ − z_{1−a}) du côté prédit.
"""
from __future__ import annotations

import numpy as np
from scipy.stats import norm

from ..gardes import GardeArret
from ..sondes.evaluation import aire_sous_courbe
from .agregateurs_v1 import STATISTIQUES, statistiques_matrice

N_ACTIONS = 10
N_TACHES = 60
AIRES_P3 = {"enjeux-lineaire-c15": 0.5248, "tromperie-difference_moyennes-c15": 0.5748}  # verdict P3 v2, l. 209 et 214


def decalage(aire_action: float, tau: float, eta: float) -> float:
    if not 0.5 <= aire_action < 1.0:
        raise GardeArret(f"aire d'action hors de [0,5 ; 1) : {aire_action}")
    return float(np.sqrt(2.0 * (1.0 + tau ** 2 + eta ** 2)) * norm.ppf(aire_action))


def positions_hybrides(m: int, rng: np.random.Generator, n: int = N_ACTIONS) -> list[np.ndarray]:
    if not 1 <= m < n:
        raise GardeArret(f"m hors de [1, {n - 1}] pour un hybride : {m}")
    if m == 1:
        return [np.array([t]) for t in range(n)]
    return [np.sort(rng.choice(n, size=m, replace=False)) for _ in range(10)]


M_GRILLE = (10, 5, 2, 1)


def une_replique(d: float, tau: float, eta: float, rng: np.random.Generator, ms=M_GRILLE,
                 n_taches: int = N_TACHES, n: int = N_ACTIONS) -> dict:
    """Mêmes tirages pour toutes les valeurs de m (les contrastes entre m sont appariés) : {m: {statistique: aire}}."""
    u = rng.normal(0.0, tau, size=n_taches)
    honnete = u[:, None] + rng.normal(0.0, eta, size=(n_taches, 1)) + rng.normal(size=(n_taches, n))
    saboteur = u[:, None] + rng.normal(0.0, eta, size=(n_taches, 1)) + rng.normal(size=(n_taches, n)) + d
    stats_h = statistiques_matrice(honnete)
    sortie = {}
    for m in ms:
        if m == n:
            positifs = saboteur
        else:
            positifs = []
            for j in range(n_taches):
                for pos in positions_hybrides(m, rng, n):
                    z = honnete[j].copy()
                    z[pos] = saboteur[j, pos]
                    positifs.append(z)
            positifs = np.asarray(positifs)
        stats_p = statistiques_matrice(positifs)
        y = np.r_[np.zeros(n_taches), np.ones(positifs.shape[0])]
        sortie[m] = {nom: aire_sous_courbe(np.r_[stats_h[nom], stats_p[nom]], y) for nom in STATISTIQUES}
    return sortie


def _puissance(valeurs: np.ndarray, niveaux) -> tuple[float, float, dict]:
    moy, et = float(valeurs.mean()), float(valeurs.std(ddof=1))
    p = {f"{a:.4f}": (float(norm.cdf(abs(moy) / et - norm.ppf(1 - a))) if et > 0 else float(moy != 0)) for a in niveaux}
    return moy, et, p


def simuler(aire_action: float, eta: float, tau: float, n_repliques: int, rng: np.random.Generator,
            ms=M_GRILLE, niveaux=(0.05, 0.05 / 3)) -> dict:
    """Aires moyennes par m et statistique ; Δ(m) = aire(somme) − aire(max) ; contraste Δ(n) − Δ(1) si n et 1 sont
    dans la grille ; puissance approchée de chaque test unilatéral, du côté du signe moyen simulé."""
    d = decalage(aire_action, tau, eta)
    aires = {m: {nom: [] for nom in STATISTIQUES} for m in ms}
    for _ in range(int(n_repliques)):
        for m, a in une_replique(d, tau, eta, rng, ms).items():
            for nom, v in a.items():
                aires[m][nom].append(v)
    sortie = {"aire_action": aire_action, "eta": eta, "tau": tau, "d": d, "repliques": int(n_repliques), "par_m": {}}
    deltas = {}
    for m in ms:
        a = {k: np.asarray(v) for k, v in aires[m].items()}
        deltas[m] = a["somme"] - a["max"]
        moy, et, p = _puissance(deltas[m], niveaux)
        sortie["par_m"][str(m)] = {"aires_moyennes": {k: float(v.mean()) for k, v in a.items()},
                                   "delta_somme_moins_max": {"moyenne": moy, "ecart_type": et,
                                                             "sens_simule": "positif" if moy >= 0 else "negatif"},
                                   "puissance_approchee": p}
    if N_ACTIONS in ms and 1 in ms:
        moy, et, p = _puissance(deltas[N_ACTIONS] - deltas[1], niveaux)
        sortie["contraste_dense_moins_concentre"] = {"moyenne": moy, "ecart_type": et, "puissance_approchee": p}
    return sortie
