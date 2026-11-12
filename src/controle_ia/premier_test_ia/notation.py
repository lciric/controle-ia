"""Notation vectorisée des actions par toutes les sondes de P3 (sondes de T0.7 et planchers), en double précision, sur la
carte ou sur le processeur, et garde d'identité contre le code de référence (`harnais.sondes.score_action`).

Même calcul que les sondes elles-mêmes, réorganisé par couche :
- sondes linéaires (`SondeLineaireJetons`, `SondeLineaire` du harnais, planchers) : scores par jeton A·W + b en une
  multiplication de matrices ; agrégation par le maximum, ou par l'attention (logits A·Q, poids softmax sur les jetons) ;
- perceptrons : v·relu(W((h − μ)/s) + c) + b par jeton ; maximum ou attention (q sur l'entrée réduite) ;
- Mahalanobis : (h − μ)ᵀ P (h − μ) par jeton, par produits de matrices au lieu de `einsum` sans BLAS ; maximum.
Jamais la moyenne ni la médiane sur les jetons. La garde d'identité recalcule, sur les actions échantillonnées, chaque
score par `score_action` (processeur, double précision) et exige l'égalité à `tolerance` près en valeur relative
(1 + |score|) ; sinon arrêt.
"""
from __future__ import annotations

import numpy as np
import torch

from ..gardes import GardeArret
from ..harnais.sondes import AGREGATIONS_SONDE, score_action
from ..sondes.familles import SondeMahalanobis, SondePerceptron


def _t(x, appareil):
    return torch.as_tensor(np.asarray(x, dtype=np.float64), device=appareil)


class Notation:
    def __init__(self, sondes, appareil: str = "cpu"):
        noms = [s.nom for s in sondes]
        if not sondes or len(set(noms)) != len(noms):
            raise GardeArret("notation : sondes absentes ou noms en double")
        self.noms, self.appareil, self.sondes = noms, appareil, list(sondes)
        self.couches = sorted({int(s.couche) for s in sondes})
        self._lineaires, self._perceptrons, self._mahalanobis = {}, {}, {}
        for c in self.couches:
            lin = [s for s in sondes if s.couche == c and not isinstance(s, (SondePerceptron, SondeMahalanobis))]
            for s in sondes:
                if s.couche == c and s.agregation not in AGREGATIONS_SONDE:
                    raise GardeArret(f"sonde {s.nom} : agrégation {s.agregation!r} refusée (maximum ou attention)")
            if lin:
                d = np.asarray(lin[0].w).shape[0]
                W = np.stack([np.asarray(s.w, dtype=np.float64) for s in lin], axis=1)
                b = np.array([float(s.b) for s in lin])
                att = np.array([s.agregation == "attention" for s in lin])
                if att.any() and any(s.q is None for s, a in zip(lin, att) if a):
                    raise GardeArret("sonde linéaire à attention sans requête q")
                Q = np.stack([np.asarray(s.q, dtype=np.float64) if a else np.zeros(d) for s, a in zip(lin, att)], axis=1)
                self._lineaires[c] = ([s.nom for s in lin], _t(W, appareil), _t(b, appareil), torch.as_tensor(att, device=appareil),
                                      _t(Q, appareil))
            self._perceptrons[c] = [(s.nom, s.agregation, _t(s.mu, appareil), _t(s.s, appareil), _t(s.W, appareil),
                                     _t(s.c, appareil), _t(s.v, appareil), float(s.b),
                                     None if s.q is None else _t(s.q, appareil))
                                    for s in sondes if s.couche == c and isinstance(s, SondePerceptron)]
            self._mahalanobis[c] = [(s.nom, _t(s.mu, appareil), _t(s.P, appareil))
                                    for s in sondes if s.couche == c and isinstance(s, SondeMahalanobis)]

    @staticmethod
    def _agreger(S, logits, attention):
        """S, logits : (n, K) ; attention : (K,) booléen. Maximum par colonne, ou somme pondérée par softmax. La somme
        pondérée est calculée pour toutes les colonnes puis écartée par `where` pour les sondes au maximum : aucune
        moyenne n'entre jamais dans un score (la garde d'identité contre `score_action` le confirme)."""
        maxi = S.max(dim=0).values
        if logits is None:
            return maxi
        p = torch.softmax(logits, dim=0)
        return torch.where(attention, (p * S).sum(dim=0), maxi)

    def noter(self, segments: dict) -> dict[str, float]:
        """`segments[couche]` : activations (jetons, largeur) de l'empan noté. Rend un score par sonde."""
        sortie = {}
        with torch.no_grad():
            for c in self.couches:
                if c not in segments:
                    raise GardeArret(f"notation : couche {c} absente des activations")
                a = np.asarray(segments[c])
                if a.ndim != 2 or a.shape[0] < 1:
                    raise GardeArret(f"notation : empan vide ou mal formé à la couche {c}")
                A = _t(a, self.appareil)
                if not bool(torch.isfinite(A).all()):
                    raise GardeArret(f"notation : activation non finie à la couche {c}")
                if c in self._lineaires:
                    noms, W, b, att, Q = self._lineaires[c]
                    S = A @ W + b
                    v = self._agreger(S, (A @ Q) if bool(att.any()) else None, att)
                    sortie.update(zip(noms, v.cpu().numpy().tolist()))
                for nom, ag, mu, s, Wp, cp, vp, bp, q in self._perceptrons[c]:
                    Z = (A - mu) / s
                    sj = torch.relu(Z @ Wp.T + cp) @ vp + bp
                    if ag == "max":
                        sortie[nom] = float(sj.max())
                    else:
                        p = torch.softmax(Z @ q, dim=0)
                        sortie[nom] = float((p * sj).sum())
                for nom, mu, P in self._mahalanobis[c]:
                    Z = A - mu
                    sortie[nom] = float(((Z @ P) * Z).sum(dim=1).max())
        valeurs = np.array([sortie[n] for n in self.noms])
        if not np.all(np.isfinite(valeurs)):
            raise GardeArret("notation : score non fini")
        return {n: sortie[n] for n in self.noms}

    def par_jeton(self, segments: dict, noms) -> dict[str, tuple[np.ndarray, np.ndarray | None]]:
        """Scores par jeton (avant agrégation) et logits d'attention (familles à attention ; sinon None) des sondes
        nommées, pour la localisation du signal dans l'action. Même calcul que `noter`, sur les mêmes tenseurs."""
        sortie = {}
        with torch.no_grad():
            for nom in noms:
                s = next((x for x in self.sondes if x.nom == nom), None)
                if s is None:
                    raise GardeArret(f"notation par jeton : sonde {nom} inconnue")
                c = int(s.couche)
                A = _t(np.asarray(segments[c]), self.appareil)
                if c in self._lineaires and nom in self._lineaires[c][0]:
                    noms_c, W, b, att, Q = self._lineaires[c]
                    j = noms_c.index(nom)
                    sj = A @ W[:, j] + b[j]
                    lg = (A @ Q[:, j]) if bool(att[j]) else None
                elif any(p[0] == nom for p in self._perceptrons[c]):
                    _, ag, mu, sd, Wp, cp, vp, bp, q = next(p for p in self._perceptrons[c] if p[0] == nom)
                    Z = (A - mu) / sd
                    sj = torch.relu(Z @ Wp.T + cp) @ vp + bp
                    lg = (Z @ q) if ag == "attention" else None
                else:
                    _, mu, P = next(p for p in self._mahalanobis[c] if p[0] == nom)
                    Z = A - mu
                    sj, lg = ((Z @ P) * Z).sum(dim=1), None
                sortie[nom] = (sj.cpu().numpy().astype(np.float64), None if lg is None else lg.cpu().numpy().astype(np.float64))
        return sortie


def agreger_par_jeton(s: np.ndarray, logits: np.ndarray | None, debut: int = 0, fin: int | None = None) -> float:
    """Score d'action recalculé depuis les scores par jeton, sur les jetons [début, fin[ : maximum, ou somme pondérée par
    le softmax des logits restreints (famille « attention ») ; jamais la moyenne ni la médiane."""
    s = np.asarray(s, dtype=np.float64)[debut:fin]
    if s.size == 0:
        raise GardeArret("agrégation par jeton : aucun jeton dans l'intervalle")
    if logits is None:
        return float(s.max())
    lg = np.asarray(logits, dtype=np.float64)[debut:fin]
    p = np.exp(lg - lg.max())
    return float(np.sum(p / p.sum() * s))


def exiger_identite(notation: Notation, segments: dict, scores: dict, tolerance: float = 1e-6,
                    sauf_familles=()) -> dict:
    """Garde d'identité : chaque score de `scores` (calculé par `notation`) égale celui du code de référence. Rend le plus
    grand écart relatif ; `sauf_familles` : familles exclues du recalcul (Mahalanobis, coûteux sur processeur)."""
    pire, controlees = 0.0, 0
    for s in notation.sondes:
        if getattr(s, "famille", None) in sauf_familles:
            continue
        seg = np.asarray(segments[s.couche])
        ref = score_action(s, seg, 0, seg.shape[0])
        ecart = abs(scores[s.nom] - ref) / (1.0 + abs(ref))
        pire = max(pire, ecart)
        controlees += 1
        if not ecart <= tolerance:
            raise GardeArret(f"garde d'identité : sonde {s.nom}, score {scores[s.nom]!r} ≠ référence {ref!r} "
                             f"(écart relatif {ecart:.3g} > {tolerance})")
    return {"sondes_controlees": controlees, "ecart_relatif_max": pire}
