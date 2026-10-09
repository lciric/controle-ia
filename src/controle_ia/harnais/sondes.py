"""Scores de sondes par action, calculés en ligne (politique de stockage par défaut, brief T0.4).

Une sonde lit les activations par jeton d'une couche et rend un score par jeton. Le score d'une action
se forme sur l'empan de ses jetons, par le maximum ou par l'attention, uniquement (brief, T0.7) :
- maximum : le plus grand score par jeton de l'empan ;
- attention : scores par jeton pondérés par la fonction softmax de logits par jeton que la sonde
  apprend (requête q).
Jamais la moyenne ni la médiane à poids fixes (interdit).

En évaluation, les scores se calculent en mémoire juste après la passe unique ; les activations par
jeton ne se conservent que pour les épisodes d'entraînement déclarés. Pour ceux-là, une garde recalcule
scores et vecteurs depuis le disque et exige l'identité au bit près.

Les sondes réelles (concepts, familles, plancher aléatoire apparié en covariance) relèvent de T0.7 ;
ici, seulement l'interface et une sonde linéaire qui sert aux tests et au run factice.
"""
from __future__ import annotations

import hashlib
from dataclasses import dataclass

import numpy as np

from ..gardes import GardeArret

AGREGATIONS_SONDE = ("max", "attention")


@dataclass(frozen=True)
class SondeLineaire:
    nom: str
    couche: int
    w: np.ndarray                   # (largeur,)
    b: float
    agregation: str                 # "max" ou "attention"
    q: np.ndarray | None = None     # (largeur,) requête de l'attention ; absente pour "max"

    def scores_par_jeton(self, acts: np.ndarray) -> np.ndarray:
        return np.einsum("nd,d->n", acts.astype(np.float64), self.w.astype(np.float64)) + float(self.b)

    def logits_attention(self, acts: np.ndarray) -> np.ndarray:
        if self.q is None:
            raise GardeArret(f"sonde {self.nom} : attention sans requête q")
        return np.einsum("nd,d->n", acts.astype(np.float64), self.q.astype(np.float64))

    def empreinte(self) -> str:
        h = hashlib.sha256(f"{self.nom}/{self.couche}/{self.agregation}/{self.b!r}".encode("utf-8"))
        for v in (self.w, self.q):
            if v is not None:
                h.update(np.ascontiguousarray(v, dtype=np.float64).tobytes())
        return h.hexdigest()


def sonde_lineaire_aleatoire(nom: str, couche: int, largeur: int, agregation: str,
                             rng: np.random.Generator) -> SondeLineaire:
    """Sonde à poids gaussiens, pour les tests et le run factice (ce n'est pas le plancher apparié de T0.7)."""
    w = rng.standard_normal(largeur) / np.sqrt(largeur)
    b = float(rng.standard_normal())
    q = rng.standard_normal(largeur) / np.sqrt(largeur) if agregation == "attention" else None
    return SondeLineaire(nom, int(couche), w, b, agregation, q)


def score_action(sonde, acts_couche: np.ndarray, debut: int, fin: int) -> float:
    """Score d'une action à partir des activations par jeton de son empan [début, fin[."""
    if sonde.agregation not in AGREGATIONS_SONDE:
        raise GardeArret(f"sonde {sonde.nom} : agrégation {sonde.agregation!r} refusée ; sur les jetons, seulement "
                         "le maximum ou l'attention (brief, T0.7) ; jamais la moyenne ni la médiane (interdit)")
    if not (0 <= debut < fin <= acts_couche.shape[0]):
        raise GardeArret(f"empan d'action [{debut}, {fin}[ invalide pour {acts_couche.shape[0]} positions")
    segment = acts_couche[debut:fin]
    s = np.asarray(sonde.scores_par_jeton(segment), dtype=np.float64)
    if s.shape != (fin - debut,) or not np.all(np.isfinite(s)):
        raise GardeArret(f"sonde {sonde.nom} : scores par jeton de forme {s.shape} pour {fin - debut} jetons, "
                         "ou non finis")
    if sonde.agregation == "max":
        return float(s.max())
    logits = np.asarray(sonde.logits_attention(segment), dtype=np.float64)
    if logits.shape != s.shape or not np.all(np.isfinite(logits)):
        raise GardeArret(f"sonde {sonde.nom} : logits d'attention de forme {logits.shape}, ou non finis")
    poids = np.exp(logits - logits.max())
    poids /= poids.sum()
    return float(np.sum(poids * s))


def scores_en_ligne(episode, acts: dict[int, dict[int, np.ndarray]], sondes) -> dict[str, np.ndarray]:
    """Tableau (N, T) des scores d'action, par sonde, depuis les activations par jeton en mémoire."""
    noms = [s.nom for s in sondes]
    if len(set(noms)) != len(noms):
        raise GardeArret(f"noms de sondes en double : {noms}")
    sortie = {}
    for s in sondes:
        tableau = np.full((episode.N, episode.T), np.nan)
        for a in episode.actions_dans_l_ordre():
            if s.couche not in acts[a.agent]:
                raise GardeArret(f"sonde {s.nom} : couche {s.couche} non capturée ({sorted(acts[a.agent])})")
            tableau[a.agent, a.pas] = score_action(s, acts[a.agent][s.couche], a.debut, a.fin)
        sortie[s.nom] = tableau
    return sortie


def exiger_identite(en_ligne: dict, hors_ligne: dict, quoi: str) -> None:
    """Garde : ce qui a été calculé en ligne = ce qui se recalcule depuis le disque, au bit près."""
    if set(en_ligne) != set(hors_ligne):
        raise GardeArret(f"{quoi} : clés {sorted(map(str, en_ligne))} ≠ {sorted(map(str, hors_ligne))}")
    fautes = [k for k in en_ligne
              if not (np.shape(en_ligne[k]) == np.shape(hors_ligne[k]) and np.array_equal(en_ligne[k], hors_ligne[k]))]
    if fautes:
        raise GardeArret(f"{quoi} : calcul en ligne ≠ recalcul hors ligne pour {fautes}")
