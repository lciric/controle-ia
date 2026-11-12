"""Familles de sondes, v3 (C-V4-2 de la contre-lecture du lanceur de T0.6 v3 ; nom neuf, R12 : `familles.py` et `familles_v2.py`
restent tels quels). L'essai d'égalité de `familles_v2` porte sur 256 jetons **tirés** autour de μ ; la contre-lecture note qu'il
suffit pour l'implémentation, pas pour le domaine. Cet essai complémentaire porte sur 256 jetons **réels**, tirés des actions
du sous-ensemble d'activations, passés par la demi-précision (comme les activations versées), même tolérance (10⁻¹²) ; un écart
au-delà lève `GardeArret` (le couple est mis en « échec », jamais l'ensemble). Aucun repli : un tirage impossible (aucun jeton
réel, jeton non fini) est une `GardeArret`, pas un essai sauté."""
from __future__ import annotations

import numpy as np

from ..gardes import GardeArret
from .familles_v2 import N_JETONS_EGALITE, TOLERANCE_EGALITE, SondeMahalanobisV2


def jetons_reels(sequences, graine: int, n: int = N_JETONS_EGALITE) -> np.ndarray:
    """`min(n, total)` jetons réels tirés sans remise dans l'ensemble des jetons des séquences données (liste de tableaux
    (jetons, largeur)), passés par la demi-précision puis rendus en float64 ; graine entière dérivée par l'appelant (R9)."""
    seqs = [np.asarray(s) for s in sequences if np.asarray(s).ndim == 2 and np.asarray(s).shape[0] > 0]
    if not seqs:
        raise GardeArret("jetons réels : aucune séquence d'activations non vide pour l'essai d'égalité (C-V4-2)")
    largeur = {s.shape[1] for s in seqs}
    if len(largeur) != 1:
        raise GardeArret(f"jetons réels : largeurs différentes {sorted(largeur)}")
    pool = np.concatenate(seqs, axis=0)
    k = min(int(n), pool.shape[0])
    rng = np.random.default_rng(np.random.SeedSequence(int(graine), spawn_key=(2,)))
    idx = np.sort(rng.choice(pool.shape[0], size=k, replace=False))
    with np.errstate(over="ignore"):                 # le débordement est refusé juste dessous (jeton non fini), pas ignoré
        jetons = pool[idx].astype(np.float16).astype(np.float64)
    if not np.all(np.isfinite(jetons)):
        raise GardeArret("jetons réels : jeton non fini après passage par la demi-précision (C-V4-2)")
    return jetons


def verifier_egalite_jetons_reels(sonde: SondeMahalanobisV2, jetons: np.ndarray, tolerance: float = TOLERANCE_EGALITE,
                                  graine: int = 0, actions_pool: int | None = None) -> dict:
    """Essai d'égalité sur des jetons réels : scores par jeton de la v2 contre ceux du paquet gelé aux mêmes paramètres."""
    if not isinstance(sonde, SondeMahalanobisV2):
        raise GardeArret(f"sonde {getattr(sonde, 'nom', '?')} : l'essai d'égalité porte sur une sonde de Mahalanobis v2")
    jetons = np.asarray(jetons, dtype=np.float64)
    if jetons.ndim != 2 or jetons.shape[0] < 1 or jetons.shape[1] != sonde.mu.shape[0]:
        raise GardeArret(f"sonde {sonde.nom} : jetons de forme {jetons.shape}, (n, {sonde.mu.shape[0]}) attendue")
    reference = np.asarray(sonde.en_paquet_gele().scores_par_jeton(jetons), dtype=np.float64)
    valeurs = np.asarray(sonde.scores_par_jeton(jetons), dtype=np.float64)
    if not (np.all(np.isfinite(reference)) and np.all(np.isfinite(valeurs))):
        raise GardeArret(f"sonde {sonde.nom} : score non fini dans l'essai d'égalité sur jetons réels")
    ecart = float(np.max(np.abs(valeurs - reference) / np.maximum(np.abs(reference), np.finfo(np.float64).tiny)))
    r = {"jetons": "reels", "calcul": sonde.calcul, "n_jetons": int(jetons.shape[0]), "graine": int(graine),
         "actions_du_pool": actions_pool, "ecart_relatif_max": ecart, "tolerance": float(tolerance), "egal": bool(ecart <= tolerance)}
    if not r["egal"]:
        raise GardeArret(f"sonde {sonde.nom} : Mahalanobis v2 ≠ paquet gelé sur {jetons.shape[0]} jetons réels (écart relatif maximal "
                         f"{ecart:.3e} > {tolerance:g}) : couple en échec, le paquet gelé fait foi (C-V4-2)")
    return r
