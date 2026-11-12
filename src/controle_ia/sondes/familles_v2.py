"""Familles de sondes, v2 : notation de Mahalanobis par produit matriciel (C-V3-4 de la contre-lecture neuve du lanceur de
T0.6 v2 ; nom neuf, R12 : le paquet gelé `sondes/familles.py` reste tel quel et reste la référence).

Le paquet gelé calcule le score par jeton (h − μ)ᵀ P (h − μ) par `np.einsum("nd,de,ne->n")` sans `optimize`, qui
contourne les produits matriciels (≈ 18 à 26 ms par jeton à la largeur 4 096 : E0, mesure de la contre-lecture). La même
quantité, calculée par `((z @ P) * z).sum(axis=1)`, coûte 80 à 120 fois moins, avec un écart relatif de l'ordre de 10⁻¹⁵.

`SondeMahalanobisV2` a la même interface que `SondeMahalanobis` (`scores_par_jeton`, `logits_attention`, `agregation`,
`couche`, `nom`, `famille`, `empreinte`) et les mêmes paramètres (μ, P) : seule la formule de calcul change, pas la quantité.
Avant chaque usage, le lanceur v3 joue `verifier_egalite_au_paquet_gele` : 256 jetons tirés, écart relatif maximal exigé
≤ `TOLERANCE_EGALITE` (10⁻¹²), sinon `GardeArret` (arrêt du couple, état « échec », jamais de l'ensemble). Le choix entre le
paquet gelé et cette v2 est une clé de configuration (`mahalanobis_calcul`, `configuration_v3`), défaut : paquet gelé.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from ..gardes import GardeArret
from .familles import SondeMahalanobis, entrainer, mahalanobis

PAQUET_GELE, PRODUIT_MATRICIEL_V2 = "paquet_gele", "produit_matriciel_v2"
CALCULS_MAHALANOBIS = (PAQUET_GELE, PRODUIT_MATRICIEL_V2)
TOLERANCE_EGALITE = 1e-12
N_JETONS_EGALITE = 256


@dataclass(frozen=True)
class SondeMahalanobisV2(SondeMahalanobis):
    """Même score que `SondeMahalanobis` ((h − μ)ᵀ P (h − μ), maximum sur les jetons), par produit matriciel."""
    calcul: str = PRODUIT_MATRICIEL_V2

    def scores_par_jeton(self, acts: np.ndarray) -> np.ndarray:
        z = np.asarray(acts, dtype=np.float64) - self.mu
        return ((z @ self.P) * z).sum(axis=1)

    def en_paquet_gele(self) -> SondeMahalanobis:
        """La sonde du paquet gelé aux mêmes paramètres (référence de l'essai d'égalité)."""
        return SondeMahalanobis(self.nom, self.couche, self.mu, self.P, self.agregation, self.famille)


def en_produit_matriciel(sonde: SondeMahalanobis) -> SondeMahalanobisV2:
    """Une sonde du paquet gelé, réécrite par produit matriciel (mêmes μ, P, nom, couche, agrégation, empreinte)."""
    if not isinstance(sonde, SondeMahalanobis):
        raise GardeArret(f"sonde {getattr(sonde, 'nom', '?')} : une sonde de Mahalanobis du paquet gelé est attendue")
    return SondeMahalanobisV2(sonde.nom, sonde.couche, sonde.mu, sonde.P, sonde.agregation, sonde.famille)


def mahalanobis_v2(nom: str, couche: int, sequences_honnetes, retrecissement: float = 0.1) -> SondeMahalanobisV2:
    """Même apprentissage que `familles.mahalanobis` (paquet gelé), sonde rendue en produit matriciel."""
    return en_produit_matriciel(mahalanobis(nom, couche, sequences_honnetes, retrecissement))


def entrainer_v2(famille: str, nom: str, couche: int, sequences, y, agregation: str = "max", graine: int = 0, reglages=None,
                 calcul: str = PAQUET_GELE):
    """`familles.entrainer` du paquet gelé ; une sonde de Mahalanobis est réécrite en produit matriciel si `calcul` le dit."""
    if calcul not in CALCULS_MAHALANOBIS:
        raise GardeArret(f"calcul de Mahalanobis {calcul!r} inconnu : {CALCULS_MAHALANOBIS}")
    sonde = entrainer(famille, nom, couche, sequences, y, agregation, graine, reglages)
    if famille == "mahalanobis" and calcul == PRODUIT_MATRICIEL_V2:
        return en_produit_matriciel(sonde)
    return sonde


def jetons_d_essai(sonde: SondeMahalanobis, graine: int, n: int = N_JETONS_EGALITE) -> np.ndarray:
    """`n` jetons tirés autour de μ, à l'échelle conditionnelle 1/√diag(P) (R9 : graine entière dérivée par l'appelant)."""
    rng = np.random.default_rng(np.random.SeedSequence(int(graine), spawn_key=(1,)))
    diag = np.diag(np.asarray(sonde.P, dtype=np.float64))
    if not np.all(np.isfinite(diag)) or not np.all(diag > 0):
        raise GardeArret(f"sonde {sonde.nom} : diagonale de P non finie ou non positive")
    return sonde.mu + rng.standard_normal((int(n), sonde.mu.shape[0])) / np.sqrt(diag)


def verifier_egalite_au_paquet_gele(sonde: SondeMahalanobisV2, graine: int, n: int = N_JETONS_EGALITE,
                                    tolerance: float = TOLERANCE_EGALITE) -> dict:
    """Essai d'égalité, joué avant chaque usage : scores par jeton de la v2 contre ceux du paquet gelé aux mêmes paramètres,
    sur `n` jetons tirés ; écart relatif maximal ≤ `tolerance`, sinon `GardeArret` (l'appelant met le couple en « échec »)."""
    if not isinstance(sonde, SondeMahalanobisV2):
        raise GardeArret(f"sonde {getattr(sonde, 'nom', '?')} : l'essai d'égalité porte sur une sonde de Mahalanobis v2")
    acts = jetons_d_essai(sonde, graine, n)
    reference = np.asarray(sonde.en_paquet_gele().scores_par_jeton(acts), dtype=np.float64)
    valeurs = np.asarray(sonde.scores_par_jeton(acts), dtype=np.float64)
    if reference.shape != (int(n),) or valeurs.shape != (int(n),):
        raise GardeArret(f"sonde {sonde.nom} : scores de forme {valeurs.shape} et {reference.shape}, ({n},) attendue")
    if not (np.all(np.isfinite(reference)) and np.all(np.isfinite(valeurs))):
        raise GardeArret(f"sonde {sonde.nom} : score non fini dans l'essai d'égalité")
    ecart = float(np.max(np.abs(valeurs - reference) / np.maximum(np.abs(reference), np.finfo(np.float64).tiny)))
    resultat = {"calcul": sonde.calcul, "n_jetons": int(n), "graine": int(graine), "ecart_relatif_max": ecart,
                "tolerance": float(tolerance), "egal": bool(ecart <= tolerance)}
    if not resultat["egal"]:
        raise GardeArret(f"sonde {sonde.nom} : Mahalanobis v2 ≠ paquet gelé (écart relatif maximal {ecart:.3e} > {tolerance:g} "
                         f"sur {n} jetons) : couple en échec, le paquet gelé fait foi")
    return resultat
