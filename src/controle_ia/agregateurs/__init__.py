"""Agrégateurs de scores par action, indexés par (agent i, pas t).

Indexation agnostique : un épisode est un tableau de scores de forme (N, T) — N agents,
T pas ; N = 1 et N = k sont le même objet. L'ordre de lecture séquentielle est
« temps d'abord » : au pas t, les N agents, puis le pas t + 1.

Convention : chaque statistique renvoie un réel, plus grand = plus suspect. Les
statistiques invariantes par permutation (somme, max, histogramme) sont calculées
sur des valeurs triées ou par sommation exacte, pour que l'invariance soit exacte
en virgule flottante (T1 de la note mathématique v2).
"""
from .indexation import episode, ordre_lecture, verifier_episode
from .processus_e import e_bilateral, e_unilateral, trajectoire_e
from .statistiques import (STATISTIQUES, autocorrelation_lag1, balayage, balayage_multi,
                           co_elevation, correlation_inter_agents, detecteur_e, dispersion_agents,
                           max_par_action, page_cusum, somme_terminale, suites_wald_wolfowitz)

__all__ = ["episode", "ordre_lecture", "verifier_episode", "e_bilateral", "e_unilateral",
           "trajectoire_e", "STATISTIQUES", "autocorrelation_lag1", "balayage", "co_elevation",
           "correlation_inter_agents", "max_par_action", "page_cusum", "somme_terminale",
           "suites_wald_wolfowitz", "balayage_multi", "detecteur_e", "dispersion_agents"]
