"""Témoins de concept et de lexique des sondes v0 (T0.7 ; préenregistrement, brouillon 3, étape 8 ; P-013 (b), R-168,
R-174). Lectures descriptives, sans effet sur le critère 3 de G0.

- `direction_concept` : direction d'un concept sans lien avec le sabotage, par différence des moyennes, sur les jetons, des
  phrases du concept et de leurs phrases neutres appariées (autant de phrases de chaque côté ; longueurs en jetons
  rapportées). Elle se lit comme une sonde linéaire, par le maximum de w·h sur les jetons d'une action (harnais). La
  moyenne qui la définit porte sur les phrases d'extraction, jamais sur les jetons d'une action lue (liste d'arrêt).
- `plancher_concept` : plancher propre à chaque direction, recette de `evaluation.plancher_apparie` appliquée aux jetons
  des phrases du concept et de leurs phrases neutres (même couche, agrégation par le maximum).
- `exiger_concept_sans_affect` : aucune direction d'affect (douleur, peur, tristesse, émotion négative, valence) n'entre
  dans cette passe : hors de P-013 (b), arrêt et nœud.
- `temoin_lexical` : régression logistique sur un sac de mots (unigrammes et bigrammes du texte de l'action, pondération
  tf-idf ajustée sur l'entraînement seulement, lignes de norme 1, pénalité L2 sur les poids, constante non pénalisée). Il
  lit le texte de l'action, jamais les activations. Ajustement déterministe (départ nul, L-BFGS, double précision) : aucun
  tirage, donc aucune graine à dériver.
- `difference_aires_appariee` : aire de a moins aire de b sur les mêmes actions ; intervalle percentile par
  rééchantillonnage des blocs (tâches) avec remise, les deux aires recalculées sur chaque tirage (T7-P6, T7-P8, T7-P10).
Module neuf : aucun module gelé n'est touché (R-160).
"""
from __future__ import annotations

import hashlib
import re
import unicodedata
from collections import Counter
from dataclasses import dataclass

import numpy as np
from scipy import sparse
from scipy.optimize import minimize

from ..gardes import GardeArret
from .evaluation import aire_sous_courbe, plancher_apparie
from .familles import SondeLineaireJetons, _verifier_donnees

# Racines refusées en tête d'un mot du nom d'un concept, lu sans accents ni capitales (P-013 (b) : aucune direction
# d'affect). Le refus d'un nom innocent qui commence comme l'une d'elles est un arrêt, jamais une lecture.
RACINES_AFFECT = ("douleur", "souffr", "peur", "crainte", "trist", "chagrin", "emotion", "affect", "valence", "plaisir",
                  "colere", "detresse", "angoiss", "anxi", "pain", "fear", "sad", "grief", "suffer", "distress", "anger",
                  "pleasure", "joy")
MOTIF_MOT = re.compile(r"\w+")


def _sans_accents(texte: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", texte) if not unicodedata.combining(c)).lower()


def exiger_concept_sans_affect(concept: str) -> None:
    if not isinstance(concept, str) or not concept.strip():
        raise GardeArret("concept sans nom")
    for mot in MOTIF_MOT.findall(_sans_accents(concept)):
        for r in RACINES_AFFECT:
            if mot.startswith(r):
                raise GardeArret(f"concept {concept!r} : direction d'affect ({r!r}), hors de P-013 (b) : arrêt et nœud")


def direction_concept(concept: str, couche: int, phrases_concept, phrases_neutres) -> tuple[SondeLineaireJetons, dict]:
    """w = moyenne des jetons des phrases du concept − moyenne des jetons de leurs phrases neutres, b = −w·(m₊ + m₋)/2 ;
    lue par le maximum. Rend la sonde et un rapport (longueurs des paires, empreinte)."""
    exiger_concept_sans_affect(concept)
    if len(phrases_concept) != len(phrases_neutres):
        raise GardeArret(f"concept {concept!r} : {len(phrases_concept)} phrases du concept pour {len(phrases_neutres)} "
                         "phrases neutres ; des paires sont attendues")
    if len(phrases_concept) < 2:
        raise GardeArret(f"concept {concept!r} : au moins deux paires de phrases")
    if _verifier_donnees(phrases_concept) != _verifier_donnees(phrases_neutres):
        raise GardeArret(f"concept {concept!r} : largeurs différentes entre phrases du concept et phrases neutres")
    pos = np.concatenate([np.asarray(p, dtype=np.float64) for p in phrases_concept])
    neg = np.concatenate([np.asarray(p, dtype=np.float64) for p in phrases_neutres])
    mp, mn = pos.mean(axis=0), neg.mean(axis=0)
    w = mp - mn
    if not np.any(w != 0.0):
        raise GardeArret(f"concept {concept!r} : direction nulle (phrases du concept et neutres indiscernables)")
    sonde = SondeLineaireJetons(f"concept-{concept}-c{couche}", int(couche), "max", w, float(-w @ (mp + mn) / 2.0), None,
                                "concept")
    lc = tuple(len(p) for p in phrases_concept)
    ln = tuple(len(p) for p in phrases_neutres)
    return sonde, {"concept": concept, "couche": int(couche), "paires": len(lc), "jetons_concept": lc,
                   "jetons_neutres": ln, "ecart_longueur_max": max(abs(a - b) for a, b in zip(lc, ln)),
                   "empreinte": sonde.empreinte()}


def plancher_concept(concept: str, couche: int, phrases_concept, phrases_neutres, n_directions: int,
                     graine: int) -> list[SondeLineaireJetons]:
    """Directions aléatoires w ~ N(0, Σ), Σ covariance des jetons des phrases du concept et de leurs phrases neutres."""
    exiger_concept_sans_affect(concept)
    return plancher_apparie(f"concept-{concept}-c{couche}", couche, list(phrases_concept) + list(phrases_neutres), "max",
                            n_directions, graine)


def termes(texte: str) -> list[str]:
    """Unigrammes et bigrammes de mots, en minuscules."""
    mots = MOTIF_MOT.findall(texte.lower())
    return mots + [f"{a} {b}" for a, b in zip(mots, mots[1:])]


def _verifier_textes(textes) -> list[str]:
    textes = list(textes)
    if not textes:
        raise GardeArret("aucun texte")
    for t in textes:
        if not isinstance(t, str) or not MOTIF_MOT.search(t):
            raise GardeArret("texte d'action vide ou non textuel")
    return textes


def _matrice(textes, index: dict[str, int], idf: np.ndarray) -> sparse.csr_matrix:
    lignes, colonnes, valeurs = [], [], []
    for i, t in enumerate(textes):
        for terme, n in Counter(termes(t)).items():
            j = index.get(terme)
            if j is not None:
                lignes.append(i)
                colonnes.append(j)
                valeurs.append(n * idf[j])
    X = sparse.csr_matrix((valeurs, (lignes, colonnes)), shape=(len(textes), len(index)), dtype=np.float64)
    normes = np.sqrt(np.asarray(X.multiply(X).sum(axis=1)).ravel())
    return sparse.diags(np.where(normes > 0.0, 1.0 / np.where(normes > 0.0, normes, 1.0), 0.0)) @ X


@dataclass(frozen=True)
class TemoinLexical:
    """Score d'une action : x·w + b, x vecteur tf-idf de norme 1 de son texte (termes du vocabulaire d'entraînement)."""
    nom: str
    vocabulaire: tuple[str, ...]
    idf: np.ndarray
    w: np.ndarray
    b: float
    penalite: float
    famille: str = "lexical"

    def scores(self, textes) -> np.ndarray:
        textes = _verifier_textes(textes)
        index = {t: j for j, t in enumerate(self.vocabulaire)}
        s = _matrice(textes, index, self.idf) @ self.w + self.b
        if not np.all(np.isfinite(s)):
            raise GardeArret(f"témoin {self.nom} : score non fini")
        return np.asarray(s, dtype=np.float64)

    def empreinte(self) -> str:
        h = hashlib.sha256(f"{self.famille}:{self.nom}/{self.penalite!r}".encode("utf-8"))
        h.update("\n".join(self.vocabulaire).encode("utf-8"))
        for t in (self.idf, self.w, np.array([self.b])):
            h.update(np.ascontiguousarray(t, dtype=np.float64).tobytes())
        return h.hexdigest()


def temoin_lexical(nom: str, textes, y, penalite: float, iterations_max: int = 1000) -> TemoinLexical:
    """Ajuste le témoin sur les textes d'entraînement et leurs étiquettes 0/1 ; minimise Σ log(1 + exp(−s·z)) + λ‖w‖²/2.
    Une optimisation qui ne converge pas arrête (aucun repli silencieux, R5)."""
    textes = _verifier_textes(textes)
    y = np.asarray(y)
    if y.shape != (len(textes),) or not set(np.unique(y).tolist()) <= {0, 1}:
        raise GardeArret("étiquettes 0/1 attendues, une par texte")
    if len(set(y.tolist())) < 2:
        raise GardeArret("les deux classes sont nécessaires à l'entraînement")
    if not (isinstance(penalite, (int, float)) and not isinstance(penalite, bool) and penalite > 0.0):
        raise GardeArret("pénalité L2 strictement positive attendue")
    df = Counter(t for texte in textes for t in set(termes(texte)))
    vocabulaire = tuple(sorted(df))
    index = {t: j for j, t in enumerate(vocabulaire)}
    n = len(textes)
    idf = np.array([np.log((1.0 + n) / (1.0 + df[t])) + 1.0 for t in vocabulaire], dtype=np.float64)
    X = _matrice(textes, index, idf)
    yf = y.astype(np.float64)

    def objectif(theta):
        w, b = theta[:-1], theta[-1]
        z = X @ w + b
        p = np.exp(-np.logaddexp(0.0, -z))
        perte = float(np.sum(np.logaddexp(0.0, z) - yf * z) + 0.5 * penalite * w @ w)
        r = p - yf
        return perte, np.concatenate([X.T @ r + penalite * w, [r.sum()]])

    res = minimize(objectif, np.zeros(len(vocabulaire) + 1), jac=True, method="L-BFGS-B",
                   options={"maxiter": int(iterations_max), "gtol": 1e-8})
    if not res.success or not np.all(np.isfinite(res.x)):
        raise GardeArret(f"témoin {nom} : ajustement non convergé ({res.message})")
    return TemoinLexical(nom, vocabulaire, idf, res.x[:-1].copy(), float(res.x[-1]), float(penalite))


def difference_aires_appariee(scores_a, scores_b, y, blocs, n_tirages: int, graine: int, niveau: float = 0.95) -> dict:
    """Aire de a − aire de b sur les mêmes actions ; plus de 1 % de tirages sans les deux classes : arrêt."""
    a, b = np.asarray(scores_a, dtype=np.float64), np.asarray(scores_b, dtype=np.float64)
    y, blocs = np.asarray(y), np.asarray(blocs)
    if not (a.shape == b.shape == y.shape == blocs.shape) or a.ndim != 1:
        raise GardeArret("scores, étiquettes et blocs : vecteurs de même longueur attendus")
    uniques = np.unique(blocs)
    if uniques.size < 2:
        raise GardeArret("au moins deux blocs pour un rééchantillonnage par blocs")
    membres = [np.flatnonzero(blocs == u) for u in uniques]
    rng = np.random.default_rng(int(graine))
    valeurs, degeneres = [], 0
    for _ in range(int(n_tirages)):
        choix = rng.integers(0, uniques.size, size=uniques.size)
        i = np.concatenate([membres[c] for c in choix])
        if len(set(y[i].tolist())) < 2:
            degeneres += 1
            continue
        valeurs.append(aire_sous_courbe(a[i], y[i]) - aire_sous_courbe(b[i], y[i]))
    if degeneres > 0.01 * n_tirages:
        raise GardeArret(f"{degeneres} tirages sur {n_tirages} sans les deux classes : blocs trop déséquilibrés")
    q = (1.0 - niveau) / 2.0
    aire_a, aire_b = aire_sous_courbe(a, y), aire_sous_courbe(b, y)
    bas, haut = float(np.quantile(valeurs, q)), float(np.quantile(valeurs, 1.0 - q))
    return {"difference": aire_a - aire_b, "aire_a": aire_a, "aire_b": aire_b, "bas": bas, "haut": haut,
            "tirages": len(valeurs), "degeneres": degeneres, "a_au_dessus_de_b": bool(bas > 0.0)}
