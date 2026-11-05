"""Bases par action et séquentielles sur des scores par action (boîte noire ou sondes) : mêmes statistiques, même
calibrage, pour que le plan 2 × 2 de G1 compare l'accès à agrégation égale (brief, T0.8).

Calibrage, toujours sur des épisodes honnêtes réservés, jamais sur l'évaluation :
- normalisation : (μ₀, σ) des scores par action des épisodes honnêtes de calibrage, mis en commun ;
- seuil de chaque statistique : rang conforme ⌈(K + 1)(1 − α)⌉ parmi les K valeurs sur épisodes honnêtes entiers
  (`simulation_t03.calibrage.seuil_conforme`). C'est la voie retenue pour G1 : la règle de Ville atteint 0,21 à 0,35 de
  faux positifs sous effet épisode (T0.3, P8). Si le rang dépasse K, le seuil est infini (aucune alarme) : jamais de
  repli silencieux sur un autre rang.

Statistiques courantes (après chaque action ; toutes croissantes, plus grand = plus suspect) :
- `max` : maximum des scores standardisés (base par action) ;
- `somme_terminale` : somme des scores standardisés, lue à la fin seulement (avant la fin : −∞) ;
- `somme_sequentielle` : maximum courant de la somme partielle (somme lue en continu) ;
- `page` : maximum courant de la somme cumulée de Page, C_t = max(0, C_{t−1} + z_t − k) ;
- `processus_e` : maximum courant du logarithme du processus e unilatéral de mélange normal (paramètre ρ) ;
- `balayage` : maximum courant des sommes sur w actions consécutives (−∞ avant la première fenêtre complète).
Valeurs finales identiques aux statistiques de T0.3 (`agregateurs`) : testé.
"""
from __future__ import annotations

import math

import numpy as np

from ..agregateurs.processus_e import trajectoire_e
from ..gardes import GardeArret
from ..simulation_t03.calibrage import seuil_conforme

STATISTIQUES = ("max", "somme_terminale", "somme_sequentielle", "page", "processus_e", "balayage")
CLES_CONFIG = ("alpha", "k_page", "rho_e", "w_balayage")


def exiger_config(config: dict) -> None:
    manquantes = [c for c in CLES_CONFIG if c not in config]
    if manquantes:
        raise GardeArret(f"configuration séquentielle incomplète : {manquantes}")
    if not (0.0 < float(config["alpha"]) < 1.0):
        raise GardeArret(f"α = {config['alpha']} hors de ]0, 1[")
    if int(config["w_balayage"]) < 1 or float(config["rho_e"]) <= 0:
        raise GardeArret("w ≥ 1 et ρ > 0 attendus")


def _scores(x) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    if x.ndim != 1 or x.size == 0:
        raise GardeArret(f"scores de forme {x.shape} : un vecteur non vide attendu (un score par action)")
    if not np.all(np.isfinite(x)):
        raise GardeArret("score par action non fini")
    return x


def calibrer_normalisation(episodes_honnetes: list) -> tuple[float, float]:
    """(μ₀, σ) des scores par action mis en commun sur au moins deux épisodes honnêtes de calibrage."""
    if len(episodes_honnetes) < 2:
        raise GardeArret("au moins deux épisodes honnêtes de calibrage")
    x = np.concatenate([_scores(e) for e in episodes_honnetes])
    sigma = float(np.std(x, ddof=1))
    if not (sigma > 0 and math.isfinite(sigma)):
        raise GardeArret(f"écart type des scores honnêtes {sigma} : scores constants, normalisation impossible")
    return float(np.mean(x)), sigma


def trajectoires(x, mu0: float, sigma: float, config: dict) -> dict[str, np.ndarray]:
    """Valeur courante de chaque statistique après chaque action (vecteurs de même longueur que `x`)."""
    exiger_config(config)
    if not (sigma > 0 and math.isfinite(sigma)):
        raise GardeArret(f"σ = {sigma} : réel strictement positif attendu")
    z = (_scores(x) - mu0) / sigma
    T = z.size
    w, k = int(config["w_balayage"]), float(config["k_page"])
    if w > T:
        raise GardeArret(f"fenêtre de balayage w = {w} plus longue que l'épisode (T = {T})")
    s = np.cumsum(z)
    c, page = 0.0, np.empty(T)
    for t, v in enumerate(z):
        c = max(0.0, c + v - k)
        page[t] = c
    fenetres = np.full(T, -np.inf)
    cumul = np.concatenate([[0.0], s])
    fenetres[w - 1:] = cumul[w:] - cumul[:-w]
    terminale = np.full(T, -np.inf)
    terminale[-1] = math.fsum(z.tolist())
    log_e = trajectoire_e(z[None, :], 0.0, 1.0, float(config["rho_e"]), "unilateral")
    return {"max": np.maximum.accumulate(z), "somme_terminale": terminale,
            "somme_sequentielle": np.maximum.accumulate(s), "page": np.maximum.accumulate(page),
            "processus_e": np.maximum.accumulate(log_e), "balayage": np.maximum.accumulate(fenetres)}


def finales(traj: dict[str, np.ndarray]) -> dict[str, float]:
    return {nom: float(v[-1]) for nom, v in traj.items()}


def seuils_conformes(finales_calibrage: list[dict], alpha: float) -> dict[str, float]:
    """Seuil de chaque statistique au rang conforme parmi les épisodes honnêtes de calibrage (K ≥ 1)."""
    if not finales_calibrage:
        raise GardeArret("aucun épisode honnête de calibrage")
    return {nom: seuil_conforme([f[nom] for f in finales_calibrage], alpha) for nom in STATISTIQUES}


def decider(traj: dict[str, np.ndarray], seuils: dict[str, float]) -> dict[str, dict]:
    """Alarme (statistique finale strictement au-dessus du seuil) et indice de la première action en alarme."""
    sorties = {}
    for nom in STATISTIQUES:
        v, h = traj[nom], seuils[nom]
        au_dessus = np.flatnonzero(v > h)
        sorties[nom] = {"alarme": bool(au_dessus.size), "premiere_alarme": int(au_dessus[0]) if au_dessus.size else None}
    return sorties


def calibrer(normalisation: dict, seuils: dict, config: dict) -> dict:
    """Calibrage complet sur deux jeux honnêtes disjoints, donnés par identifiant d'épisode : (μ₀, σ) sur le premier,
    seuils conformes sur le second. Rien de l'évaluation (garde dans `evaluer`)."""
    exiger_config(config)
    communs = set(normalisation) & set(seuils)
    if communs:
        raise GardeArret(f"{len(communs)} épisode(s) servent à la normalisation et aux seuils : {sorted(communs)[:3]}")
    mu0, sigma = calibrer_normalisation(list(normalisation.values()))
    fin = [finales(trajectoires(e, mu0, sigma, config)) for e in seuils.values()]
    return {"mu0": mu0, "sigma": sigma, "seuils": seuils_conformes(fin, float(config["alpha"])), "K": len(seuils),
            "episodes_calibrage": sorted(set(normalisation) | set(seuils))}


def evaluer(episodes: dict, calibrage: dict, config: dict) -> dict[str, dict]:
    """Décision de chaque base sur chaque épisode d'évaluation (par identifiant), avec le calibrage figé. Arrêt si un
    épisode d'évaluation a servi au calibrage (liste d'arrêt de G1)."""
    fuite = set(episodes) & set(calibrage["episodes_calibrage"])
    if fuite:
        raise GardeArret(f"{len(fuite)} épisode(s) d'évaluation ont servi au calibrage : {sorted(fuite)[:3]}")
    return {e: decider(trajectoires(x, calibrage["mu0"], calibrage["sigma"], config), calibrage["seuils"])
            for e, x in episodes.items()}
