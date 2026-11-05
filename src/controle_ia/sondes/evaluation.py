"""Évaluation des sondes v0 (T0.7) : scores d'action, aire sous la courbe ROC, intervalles par blocs de tâches, et
comparaison au plancher aléatoire apparié en covariance (« une sonde qui ne le bat pas n'existe pas »).

Plancher (programme 8.1, brief T0.7, « style P3 ») — recette **provisoire**, à confronter au code de P3 dès réception :
des sondes linéaires aléatoires w ~ N(0, Σ), Σ étant la covariance des jetons de l'entraînement (toutes classes), centrées
(b = −w·μ), avec la même agrégation que la sonde comparée (pour l'attention, q ~ N(0, Σ) aussi). Une direction tirée
dans la covariance des activations suit leurs grands axes (longueur, style, position), qui corrèlent souvent avec les
étiquettes par confusion : c'est un plancher plus exigeant que des directions isotropes. Le plancher d'une évaluation
est un quantile de la distribution des aires sous la courbe de ces sondes sur le même jeu.
"""
from __future__ import annotations

import numpy as np
from scipy.stats import rankdata

from ..gardes import GardeArret
from ..harnais.sondes import score_action
from .familles import SondeLineaireJetons, _verifier_donnees


def scores_actions(sonde, sequences) -> np.ndarray:
    """Score de chaque action (toute la séquence de ses jetons), par l'agrégation de la sonde (harnais)."""
    return np.array([score_action(sonde, np.asarray(s), 0, len(s)) for s in sequences], dtype=np.float64)


def aire_sous_courbe(scores, y) -> float:
    """Statistique de Mann-Whitney normalisée ; ex aequo comptés pour moitié."""
    scores, y = np.asarray(scores, dtype=np.float64), np.asarray(y)
    if scores.shape != y.shape or scores.ndim != 1:
        raise GardeArret("scores et étiquettes : vecteurs de même longueur attendus")
    if not np.all(np.isfinite(scores)):
        raise GardeArret("score non fini")
    n1, n0 = int((y == 1).sum()), int((y == 0).sum())
    if n1 == 0 or n0 == 0 or n1 + n0 != y.size:
        raise GardeArret("les deux classes 0/1 sont nécessaires")
    r = rankdata(scores)
    return float((r[y == 1].sum() - n1 * (n1 + 1) / 2.0) / (n1 * n0))


def intervalle_blocs(scores, y, blocs, n_tirages: int, graine: int, niveau: float = 0.95) -> dict:
    """Intervalle percentile par rééchantillonnage des blocs (tâches) avec remise. Les tirages où une classe manque
    sont comptés et rapportés ; s'ils dépassent 1 % des tirages, arrêt (aucun repli silencieux)."""
    scores, y, blocs = np.asarray(scores, dtype=np.float64), np.asarray(y), np.asarray(blocs)
    if not (scores.shape == y.shape == blocs.shape):
        raise GardeArret("scores, étiquettes et blocs de même longueur attendus")
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
        valeurs.append(aire_sous_courbe(scores[i], y[i]))
    if degeneres > 0.01 * n_tirages:
        raise GardeArret(f"{degeneres} tirages sur {n_tirages} sans les deux classes : blocs trop déséquilibrés")
    a = (1.0 - niveau) / 2.0
    return {"aire": aire_sous_courbe(scores, y), "bas": float(np.quantile(valeurs, a)),
            "haut": float(np.quantile(valeurs, 1.0 - a)), "tirages": len(valeurs), "degeneres": degeneres}


def plancher_apparie(nom: str, couche: int, sequences_entrainement, agregation: str, n_sondes: int,
                     graine: int) -> list[SondeLineaireJetons]:
    """Sondes aléatoires appariées en covariance (recette provisoire, voir l'en-tête du module)."""
    d = _verifier_donnees(sequences_entrainement)
    if agregation not in ("max", "attention"):
        raise GardeArret(f"agrégation {agregation!r} refusée : max ou attention seulement")
    X = np.concatenate([np.asarray(s, dtype=np.float64) for s in sequences_entrainement])
    mu = X.mean(axis=0)
    S = np.cov(X, rowvar=False).reshape(d, d) + 1e-9 * np.eye(d)
    L = np.linalg.cholesky(S)
    rng = np.random.default_rng(int(graine))
    sondes = []
    for k in range(int(n_sondes)):
        w = L @ rng.standard_normal(d)
        q = (L @ rng.standard_normal(d)) if agregation == "attention" else None
        sondes.append(SondeLineaireJetons(f"{nom}-plancher-{k}", couche, agregation, w, float(-w @ mu), q, "plancher"))
    return sondes


def comparer_au_plancher(sonde, plancher: list, sequences_eval, y_eval, blocs_eval, n_tirages: int, graine: int,
                         quantile_plancher: float = 0.95, niveau: float = 0.95) -> dict:
    """La sonde existe si la borne basse de son intervalle dépasse le quantile du plancher sur le même jeu."""
    if not plancher:
        raise GardeArret("plancher vide")
    if any(p.agregation != sonde.agregation for p in plancher):
        raise GardeArret("plancher et sonde d'agrégations différentes")
    s = scores_actions(sonde, sequences_eval)
    ic = intervalle_blocs(s, y_eval, blocs_eval, n_tirages, graine, niveau)
    aires_plancher = np.array([aire_sous_courbe(scores_actions(p, sequences_eval), y_eval) for p in plancher])
    seuil = float(np.quantile(aires_plancher, quantile_plancher))
    return {"sonde": sonde.nom, "aire": ic["aire"], "bas": ic["bas"], "haut": ic["haut"],
            "plancher_quantile": seuil, "plancher_mediane": float(np.median(aires_plancher)),
            "n_plancher": len(plancher), "au_dessus_du_plancher": bool(ic["bas"] > seuil),
            "degeneres": ic["degeneres"]}
