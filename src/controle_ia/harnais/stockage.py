"""Estimation du stockage des activations, avant de choisir la politique (brief, T0.4).

Politique par défaut : activations complètes par jeton seulement sur un sous-échantillon
d'entraînement ; en évaluation, vecteurs agrégés par action (maximum par coordonnée) et scores de
sondes calculés en ligne (maximum ou attention sur les jetons, brief T0.7). Les scores pèsent
8 octets par action et par sonde : négligeables, hors estimation.
"""
from __future__ import annotations

from ..gardes import GardeArret


def estimer(episodes: int, jetons_par_episode: int, actions_par_episode: int, couches: int, largeur: int,
            octets_par_valeur: int = 2, fraction_par_jeton: float = 0.1, agregations: int = 1) -> dict:
    """Octets pour (a) tout garder par jeton, (b) la politique par défaut."""
    if min(episodes, jetons_par_episode, actions_par_episode, couches, largeur, octets_par_valeur) < 1:
        raise GardeArret("estimation de stockage : toutes les tailles doivent être ≥ 1")
    if not 0.0 <= fraction_par_jeton <= 1.0:
        raise GardeArret(f"fraction {fraction_par_jeton} hors de [0, 1]")
    par_jeton = episodes * jetons_par_episode * couches * largeur * octets_par_valeur
    par_action = episodes * actions_par_episode * couches * largeur * octets_par_valeur * agregations
    defaut = int(round(fraction_par_jeton * par_jeton)) + par_action
    return {"tout_par_jeton_octets": par_jeton, "politique_defaut_octets": defaut,
            "tout_par_jeton_go": round(par_jeton / 1e9, 3), "politique_defaut_go": round(defaut / 1e9, 3),
            "hypotheses": {"episodes": episodes, "jetons_par_episode": jetons_par_episode,
                           "actions_par_episode": actions_par_episode, "couches": couches, "largeur": largeur,
                           "octets_par_valeur": octets_par_valeur, "fraction_par_jeton": fraction_par_jeton,
                           "agregations": agregations}}
