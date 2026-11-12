"""Notation de Mahalanobis par produit matriciel (`produit_matriciel_v2`) pour la lecture de T0.7, v1.

Miroir de `src/controle_ia/sondes/familles_v2.py` **cité au commit** `8cb539f9` (empreinte du fichier à ce commit
`4fea2c52b754fc180974c80ed9e83a3656d1b6aef7382a4451b7532a144153ad`, 94 lignes ; absent de `main`, non fusionné ; brouillon 12,
marqueur 8 du module ; brouillon 14, en-tête). Même quantité (h − μ)ᵀ P (h − μ) que le paquet gelé
`sondes.familles.SondeMahalanobis` (référence, R12), calculée par `((z @ P) * z).sum(axis=1)` au lieu de
`np.einsum("nd,de,ne->n")` ; **essai d'égalité au paquet gelé avant chaque usage** (`verifier_egalite_au_paquet_gele` : 256 jetons
tirés autour de μ, écart relatif maximal ≤ 10⁻¹², graine dérivée ; R-1624 (i)) : un échec met **le couple** en « échec »
(l'appelant l'écrit), jamais l'ensemble.

La classe `SondeMahalanobisV2`, `en_produit_matriciel`, `jetons_d_essai`, les constantes et le calcul de
`verifier_egalite_au_paquet_gele` sont égaux ligne à ligne au fichier cité ; **seuls écarts permis** (brouillon 14, en-tête) :
(a) en-tête et docstrings ; (b) import `from ..sondes.familles import SondeMahalanobis` au lieu de
`from .familles import SondeMahalanobis, entrainer, mahalanobis` (autre paquet) ; (c) `mahalanobis_v2` et `entrainer_v2` absents
(les sondes sont apprises par `familles.entrainer` du paquet gelé, puis réécrites par `preparer_sonde`) ; (d) le compte rendu de
l'essai porte deux champs de plus (`sonde`, `empreinte`) ; (e) `preparer_sonde` et `__all__` ajoutés. L'essai de miroir
(`tests/test_t07_lecture_v1.py`) compare ce fichier, par son arbre syntaxique, au fichier lu par
`git show 8cb539f9:src/controle_ia/sondes/familles_v2.py`, aux cinq écarts près, et compare les scores des deux classes.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from ..gardes import GardeArret
from ..sondes.familles import SondeMahalanobis

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
        return SondeMahalanobis(self.nom, self.couche, self.mu, self.P, self.agregation, self.famille)


def en_produit_matriciel(sonde: SondeMahalanobis) -> SondeMahalanobisV2:
    """Une sonde de Mahalanobis du paquet gelé, réécrite par produit matriciel (mêmes μ, P, nom, couche, agrégation, empreinte)."""
    if not isinstance(sonde, SondeMahalanobis):
        raise GardeArret(f"sonde {getattr(sonde, 'nom', '?')} : une sonde de Mahalanobis du paquet gelé est attendue")
    return SondeMahalanobisV2(sonde.nom, sonde.couche, sonde.mu, sonde.P, sonde.agregation, sonde.famille)


def jetons_d_essai(sonde: SondeMahalanobis, graine: int, n: int = N_JETONS_EGALITE) -> np.ndarray:
    """`n` jetons tirés autour de μ, à l'échelle conditionnelle 1/√diag(P) (R9 : graine entière dérivée par l'appelant)."""
    rng = np.random.default_rng(np.random.SeedSequence(int(graine), spawn_key=(1,)))
    diag = np.diag(np.asarray(sonde.P, dtype=np.float64))
    if not np.all(np.isfinite(diag)) or not np.all(diag > 0):
        raise GardeArret(f"sonde {sonde.nom} : diagonale de P non finie ou non positive")
    return sonde.mu + rng.standard_normal((int(n), sonde.mu.shape[0])) / np.sqrt(diag)


def verifier_egalite_au_paquet_gele(sonde: SondeMahalanobisV2, graine: int, n: int = N_JETONS_EGALITE,
                                    tolerance: float = TOLERANCE_EGALITE) -> dict:
    """Essai d'égalité, joué avant chaque usage : scores par jeton de la v2 contre ceux du paquet gelé aux mêmes paramètres ;
    écart relatif maximal ≤ `tolerance`, sinon `GardeArret` (l'appelant met le couple en « échec »)."""
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
                "tolerance": float(tolerance), "egal": bool(ecart <= tolerance), "sonde": sonde.nom, "empreinte": sonde.empreinte()}
    if not resultat["egal"]:
        raise GardeArret(f"sonde {sonde.nom} : Mahalanobis v2 ≠ paquet gelé (écart relatif maximal {ecart:.3e} > {tolerance:g} "
                         f"sur {n} jetons) : couple en échec, le paquet gelé fait foi")
    return resultat


def preparer_sonde(sonde, calcul: str, graine: int) -> tuple[object, dict | None]:
    """Sonde prête à noter : une sonde de Mahalanobis est réécrite en produit matriciel si `calcul` le dit, et l'essai d'égalité
    est joué avant tout usage (son compte rendu est rendu) ; toute autre sonde passe telle quelle (compte rendu nul)."""
    if calcul not in CALCULS_MAHALANOBIS:
        raise GardeArret(f"calcul de Mahalanobis {calcul!r} inconnu : {CALCULS_MAHALANOBIS}")
    if not isinstance(sonde, SondeMahalanobis) or calcul == PAQUET_GELE:
        return sonde, None
    v2 = sonde if isinstance(sonde, SondeMahalanobisV2) else en_produit_matriciel(sonde)
    return v2, verifier_egalite_au_paquet_gele(v2, graine)


__all__ = ["SondeMahalanobisV2", "en_produit_matriciel", "verifier_egalite_au_paquet_gele", "preparer_sonde", "jetons_d_essai",
           "PAQUET_GELE", "PRODUIT_MATRICIEL_V2", "CALCULS_MAHALANOBIS", "TOLERANCE_EGALITE", "N_JETONS_EGALITE"]
