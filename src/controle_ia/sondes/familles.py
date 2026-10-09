"""Familles de sondes v0 (T0.7 ; programme, section 8.1 ; brief, T0.7).

Une sonde note chaque jeton d'une action, puis agrège sur les jetons de l'action par le **maximum** ou par
l'**attention** (logits par jeton appris, poids softmax), jamais par la moyenne ni la médiane (interdit). Les sondes
rendues ont l'interface du harnais (`scores_par_jeton`, `logits_attention`, `agregation`, `couche`, `nom`,
`empreinte`) : `harnais.sondes.score_action` les applique telles quelles, en ligne comme hors ligne.

Familles :
- `difference_moyennes` : w = moyenne des jetons des actions positives − moyenne des jetons des actions négatives ;
- `lineaire` : score w·h + b par jeton, appris sur les étiquettes d'action à travers l'agrégation (apprentissage par
  sacs), pénalité L2 ;
- `perceptron` : petit perceptron à une couche cachée par jeton, même apprentissage ;
- `attention` : score linéaire par jeton et agrégation par attention apprise (requête q) ;
- `mahalanobis` : non supervisée, carré de la distance de Mahalanobis du jeton à la distribution des jetons honnêtes
  (covariance rétrécie vers l'identité réduite), agrégée par le maximum.
Entraînement déterministe : graine entière (R9, dérivée du manifeste par l'appelant), double précision sur processeur,
algorithmes déterministes ; entrées centrées-réduites par jeton sur l'entraînement, normalisation repliée dans les
paramètres rendus (une sonde rendue lit les activations brutes).
"""
from __future__ import annotations

import hashlib
from dataclasses import dataclass, field

import numpy as np
import torch

from ..gardes import GardeArret

AGREGATIONS = ("max", "attention")
FAMILLES = ("difference_moyennes", "lineaire", "perceptron", "attention", "mahalanobis")


def _verifier_donnees(sequences, y=None) -> int:
    if not sequences:
        raise GardeArret("aucune action")
    d = None
    for s in sequences:
        s = np.asarray(s)
        if s.ndim != 2 or s.shape[0] < 1:
            raise GardeArret(f"action de forme {s.shape} : (jetons, largeur) attendue, au moins un jeton")
        if d is None:
            d = s.shape[1]
        elif s.shape[1] != d:
            raise GardeArret("largeurs différentes entre actions")
        if not np.all(np.isfinite(s)):
            raise GardeArret("activation non finie")
    if y is not None:
        y = np.asarray(y)
        if y.shape != (len(sequences),) or not set(np.unique(y)) <= {0, 1}:
            raise GardeArret("étiquettes 0/1 attendues, une par action")
        if len(set(y.tolist())) < 2:
            raise GardeArret("les deux classes sont nécessaires à l'entraînement")
    return int(d)


def _empreinte(nom, couche, agregation, *tableaux) -> str:
    h = hashlib.sha256(f"{nom}/{couche}/{agregation}".encode("utf-8"))
    for t in tableaux:
        h.update(np.ascontiguousarray(t, dtype=np.float64).tobytes())
    return h.hexdigest()


@dataclass(frozen=True)
class SondeLineaireJetons:
    """Score w·h + b par jeton ; logits d'attention q·h (si agrégation par attention). Lit les activations brutes."""
    nom: str
    couche: int
    agregation: str
    w: np.ndarray
    b: float
    q: np.ndarray | None = None
    famille: str = "lineaire"

    def scores_par_jeton(self, acts: np.ndarray) -> np.ndarray:
        return np.asarray(acts, dtype=np.float64) @ self.w.astype(np.float64) + float(self.b)

    def logits_attention(self, acts: np.ndarray) -> np.ndarray:
        if self.q is None:
            raise GardeArret(f"sonde {self.nom} : attention sans requête q")
        return np.asarray(acts, dtype=np.float64) @ self.q.astype(np.float64)

    def empreinte(self) -> str:
        t = [self.w, np.array([self.b])] + ([self.q] if self.q is not None else [])
        return _empreinte(f"{self.famille}:{self.nom}", self.couche, self.agregation, *t)


@dataclass(frozen=True)
class SondePerceptron:
    """Score par jeton : v·relu(W((h − μ)/s) + c) + b ; agrégation par le maximum ou par attention (q sur l'entrée
    réduite)."""
    nom: str
    couche: int
    agregation: str
    mu: np.ndarray
    s: np.ndarray
    W: np.ndarray
    c: np.ndarray
    v: np.ndarray
    b: float
    q: np.ndarray | None = None
    famille: str = "perceptron"

    def _reduire(self, acts):
        return (np.asarray(acts, dtype=np.float64) - self.mu) / self.s

    def scores_par_jeton(self, acts: np.ndarray) -> np.ndarray:
        z = self._reduire(acts)
        return np.maximum(z @ self.W.T + self.c, 0.0) @ self.v + float(self.b)

    def logits_attention(self, acts: np.ndarray) -> np.ndarray:
        if self.q is None:
            raise GardeArret(f"sonde {self.nom} : attention sans requête q")
        return self._reduire(acts) @ self.q

    def empreinte(self) -> str:
        t = [self.mu, self.s, self.W, self.c, self.v, np.array([self.b])] + ([self.q] if self.q is not None else [])
        return _empreinte(f"{self.famille}:{self.nom}", self.couche, self.agregation, *t)


@dataclass(frozen=True)
class SondeMahalanobis:
    """Score par jeton : (h − μ)ᵀ P (h − μ), P = inverse de la covariance rétrécie des jetons honnêtes ; maximum."""
    nom: str
    couche: int
    mu: np.ndarray
    P: np.ndarray
    agregation: str = "max"
    famille: str = "mahalanobis"

    def scores_par_jeton(self, acts: np.ndarray) -> np.ndarray:
        z = np.asarray(acts, dtype=np.float64) - self.mu
        return np.einsum("nd,de,ne->n", z, self.P, z)

    def logits_attention(self, acts: np.ndarray) -> np.ndarray:
        raise GardeArret("sonde de Mahalanobis : agrégation par le maximum seulement")

    def empreinte(self) -> str:
        return _empreinte(f"{self.famille}:{self.nom}", self.couche, self.agregation, self.mu, self.P)


@dataclass
class Reglages:
    l2: float = 1e-3
    epoques: int = 300
    pas: float = 0.05
    cachees: int = 16
    retrecissement: float = 0.1
    journal: list = field(default_factory=list)


def _normalisation(sequences) -> tuple[np.ndarray, np.ndarray]:
    tout = np.concatenate([np.asarray(s, dtype=np.float64) for s in sequences])
    mu, s = tout.mean(axis=0), tout.std(axis=0)
    return mu, np.where(s > 1e-12, s, 1.0)


def difference_moyennes(nom: str, couche: int, sequences, y, agregation: str = "max") -> SondeLineaireJetons:
    """w = m₊ − m₋ (moyennes des jetons par classe d'action), b = −w·(m₊ + m₋)/2. Agrégation par le maximum."""
    _verifier_donnees(sequences, y)
    if agregation != "max":
        raise GardeArret("différence de moyennes : agrégation par le maximum seulement (pas de paramètre d'attention)")
    y = np.asarray(y)
    pos = np.concatenate([np.asarray(s, dtype=np.float64) for s, t in zip(sequences, y) if t == 1])
    neg = np.concatenate([np.asarray(s, dtype=np.float64) for s, t in zip(sequences, y) if t == 0])
    mp, mn = pos.mean(axis=0), neg.mean(axis=0)
    w = mp - mn
    return SondeLineaireJetons(nom, couche, "max", w, float(-w @ (mp + mn) / 2.0), None, "difference_moyennes")


def _sacs(sequences, mu, s):
    """Jetons réduits mis bout à bout, et indice de l'action de chaque jeton."""
    X = torch.tensor(np.concatenate([(np.asarray(q, dtype=np.float64) - mu) / s for q in sequences]))
    idx = torch.tensor(np.concatenate([np.full(len(q), i) for i, q in enumerate(sequences)]), dtype=torch.long)
    return X, idx


def _agreger(scores_jetons, logits, idx, n, agregation):
    if agregation == "max":
        out = torch.full((n,), -torch.inf, dtype=scores_jetons.dtype)
        return out.scatter_reduce(0, idx, scores_jetons, reduce="amax", include_self=True)
    m = torch.full((n,), -torch.inf, dtype=logits.dtype).scatter_reduce(0, idx, logits, reduce="amax", include_self=True)
    e = torch.exp(logits - m[idx])
    z = torch.zeros(n, dtype=e.dtype).index_add(0, idx, e)
    return torch.zeros(n, dtype=e.dtype).index_add(0, idx, e * scores_jetons) / z


def _entrainer(nom, couche, sequences, y, agregation, graine, reglages, famille):
    d = _verifier_donnees(sequences, y)
    if agregation not in AGREGATIONS:
        raise GardeArret(f"agrégation {agregation!r} refusée : max ou attention seulement (brief, T0.7)")
    torch.manual_seed(int(graine))
    mu, s = _normalisation(sequences)
    X, idx = _sacs(sequences, mu, s)
    n = len(sequences)
    cible = torch.tensor(np.asarray(y, dtype=np.float64))
    if famille == "perceptron":
        W = torch.nn.Parameter(torch.randn(reglages.cachees, d, dtype=torch.float64) / np.sqrt(d))
        c = torch.nn.Parameter(torch.zeros(reglages.cachees, dtype=torch.float64))
        v = torch.nn.Parameter(torch.randn(reglages.cachees, dtype=torch.float64) / np.sqrt(reglages.cachees))
        parametres = [W, c, v]
    else:
        w = torch.nn.Parameter(torch.zeros(d, dtype=torch.float64))
        parametres = [w]
    b = torch.nn.Parameter(torch.zeros((), dtype=torch.float64))
    parametres.append(b)
    q = None
    if agregation == "attention":
        q = torch.nn.Parameter(torch.randn(d, dtype=torch.float64) * 0.01)
        parametres.append(q)
    opt = torch.optim.Adam(parametres, lr=reglages.pas)
    perte_bce = torch.nn.BCEWithLogitsLoss()
    for e in range(reglages.epoques):
        opt.zero_grad()
        if famille == "perceptron":
            sj = torch.relu(X @ W.T + c) @ v + b
            penal = (W ** 2).sum() + (v ** 2).sum()
        else:
            sj = X @ w + b
            penal = (w ** 2).sum()
        lj = X @ q if q is not None else None
        sa = _agreger(sj, lj, idx, n, agregation)
        perte = perte_bce(sa, cible) + reglages.l2 * penal
        perte.backward()
        opt.step()
        if e in (0, reglages.epoques - 1):
            reglages.journal.append({"epoque": e, "perte": float(perte.detach())})
    qn = (q.detach().numpy() if q is not None else None)
    if famille == "perceptron":
        return SondePerceptron(nom, couche, agregation, mu, s, W.detach().numpy(), c.detach().numpy(),
                               v.detach().numpy(), float(b.detach()), qn)
    wn = w.detach().numpy()
    # normalisation repliée : ((h − μ)/s)·w' + b' = h·(w'/s) + (b' − μ·(w'/s)) ; la constante des logits d'attention
    # n'agit pas sur le softmax
    w_brut = wn / s
    return SondeLineaireJetons(nom, couche, agregation, w_brut, float(b.detach()) - float(mu @ w_brut),
                               (qn / s) if qn is not None else None, famille)


def lineaire(nom, couche, sequences, y, agregation="max", graine=0, reglages: Reglages | None = None):
    return _entrainer(nom, couche, sequences, y, agregation, graine, reglages or Reglages(), "lineaire")


def perceptron(nom, couche, sequences, y, agregation="max", graine=0, reglages: Reglages | None = None):
    return _entrainer(nom, couche, sequences, y, agregation, graine, reglages or Reglages(), "perceptron")


def attention(nom, couche, sequences, y, graine=0, reglages: Reglages | None = None):
    return _entrainer(nom, couche, sequences, y, "attention", graine, reglages or Reglages(), "attention")


def mahalanobis(nom: str, couche: int, sequences_honnetes, retrecissement: float = 0.1) -> SondeMahalanobis:
    """Non supervisée : moyenne et covariance des jetons d'actions honnêtes seulement, rétrécie vers (tr Σ / d)·I."""
    d = _verifier_donnees(sequences_honnetes)
    if not 0.0 < retrecissement <= 1.0:
        raise GardeArret(f"rétrécissement {retrecissement} hors de ]0, 1]")
    X = np.concatenate([np.asarray(s, dtype=np.float64) for s in sequences_honnetes])
    if X.shape[0] < 2:
        raise GardeArret("au moins deux jetons honnêtes")
    mu = X.mean(axis=0)
    S = np.cov(X, rowvar=False).reshape(d, d)
    S = (1.0 - retrecissement) * S + retrecissement * (np.trace(S) / d) * np.eye(d)
    return SondeMahalanobis(nom, couche, mu, np.linalg.inv(S))


def entrainer(famille: str, nom: str, couche: int, sequences, y, agregation: str = "max", graine: int = 0,
              reglages: Reglages | None = None):
    """Point d'entrée unique ; Mahalanobis ne lit que les actions négatives (honnêtes) de l'entraînement."""
    if famille not in FAMILLES:
        raise GardeArret(f"famille {famille!r} inconnue : {FAMILLES}")
    if famille == "difference_moyennes":
        return difference_moyennes(nom, couche, sequences, y, agregation)
    if famille == "attention":
        if agregation != "attention":
            raise GardeArret("la famille « attention » agrège par attention")
        return attention(nom, couche, sequences, y, graine, reglages)
    if famille == "mahalanobis":
        if agregation != "max":
            raise GardeArret("Mahalanobis : agrégation par le maximum seulement")
        _verifier_donnees(sequences, y)
        honnetes = [s for s, t in zip(sequences, np.asarray(y)) if t == 0]
        return mahalanobis(nom, couche, honnetes, (reglages or Reglages()).retrecissement)
    f = lineaire if famille == "lineaire" else perceptron
    return f(nom, couche, sequences, y, agregation, graine, reglages)
