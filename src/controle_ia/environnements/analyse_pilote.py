"""Analyse du pilote de l'environnement (a) (T0.5) : décomposition de variance des juges, couverture des cibles,
accord de l'appariement. Sur processeur, à partir des résultats scellés du run.

Décomposition (annexe C.1 de 2606.08892v2, p. 17-18), adaptée à un seul générateur (σ²_générateur = 0) :
- run A : un épisode par tâche, noté une fois ; run B : les mêmes ensembles, notés une seconde fois ;
  run C : un autre épisode par tâche, noté une fois ;
- σ²_ε (bruit du juge) = V[sA − sB] / 2 ; σ²_β (tâche) = Cov[sA, sC] ; σ²_δ (bruit de génération) =
  Cov[sA, sB] − Cov[sA, sC].
La somme des trois composantes ainsi estimées vaut (V̂[sA] + V̂[sB]) / 2 par construction (σ̂²_β s'y annule ;
contre-lecture 2 du pilote, D-1) : elle ne contrôle pas l'alignement des notes. L'article, lui, tire σ²_β de V[s] par
différence (équation 22, avec σ²_α = 0) : écart d'estimateur déclaré au préenregistrement.
Une tâche dont une des trois notes manque sort de la décomposition (nombre rapporté), sans imputation.
"""
from __future__ import annotations

import numpy as np

from ..gardes import GardeArret


def _cov(x: np.ndarray, y: np.ndarray) -> float:
    return float(np.mean((x - x.mean()) * (y - y.mean())) * len(x) / (len(x) - 1))


def decomposition_variance(sA, sB, sC) -> dict:
    """Composantes et parts ; les trois tableaux sont alignés par tâche (NaN = note manquante)."""
    a, b, c = (np.asarray(v, dtype=float) for v in (sA, sB, sC))
    if not (a.shape == b.shape == c.shape) or a.ndim != 1:
        raise GardeArret("notes A, B et C non alignées par tâche")
    gardees = ~(np.isnan(a) | np.isnan(b) | np.isnan(c))
    n = int(gardees.sum())
    if n < 3:
        raise GardeArret(f"{n} tâches complètes : décomposition impossible")
    a, b, c = a[gardees], b[gardees], c[gardees]
    eps = float(np.var(a - b, ddof=1) / 2)
    beta = _cov(a, c)
    delta = _cov(a, b) - beta
    total = beta + delta + eps
    parts = {k: (v / total if total > 0 else float("nan")) for k, v in
             (("tache", beta), ("generation", delta), ("juge", eps))}
    return {"taches": n, "taches_incompletes": int((~gardees).sum()),
            "composantes": {"tache": beta, "generation": delta, "juge": eps, "totale": total}, "parts": parts}


def kappa_cohen(x, y) -> float:
    """Kappa de Cohen pour deux étiquetages binaires de mêmes éléments."""
    x, y = np.asarray(x, dtype=bool), np.asarray(y, dtype=bool)
    if x.shape != y.shape or x.size == 0:
        raise GardeArret("étiquetages de tailles différentes ou vides")
    po = float(np.mean(x == y))
    pe = float(x.mean() * y.mean() + (1 - x.mean()) * (1 - y.mean()))
    if pe == 1.0:
        raise GardeArret("accord attendu égal à 1 (une seule classe) : kappa indéfini")
    return (po - pe) / (1 - pe)


def couverture(p_oui: dict[tuple[int, str], float], propositions: list[int], cibles: list[str],
               seuil: float = 0.5) -> dict:
    """Couverture d'un ensemble final : part des cibles appariées à au moins une proposition, et cibles couvertes.
    `p_oui[(numéro de proposition, identifiant de cible)]` ; une paire absente arrête (aucune valeur par défaut)."""
    manquantes = [(k, c) for k in propositions for c in cibles if (k, c) not in p_oui]
    if manquantes:
        raise GardeArret(f"{len(manquantes)} paires d'appariement absentes, dont {manquantes[:3]}")
    if not cibles:
        raise GardeArret("aucune cible")
    couvertes = sorted({c for c in cibles for k in propositions if p_oui[(k, c)] >= seuil})
    return {"part": len(couvertes) / len(cibles), "couvertes": couvertes}


# --- Brouillon 2 du préenregistrement du pilote (contre-lecture 1, CL-5 à CL-14) ----------------------------------

def parts_tronquees(composantes: dict) -> dict:
    """Parts avec les composantes estimées tronquées à 0 (CL-6) : une composante négative (estimation par différence de
    covariances) gonflerait la part du juge, jusqu'à la rendre supérieure à 1."""
    c = {k: max(float(composantes[k]), 0.0) for k in ("tache", "generation", "juge")}
    total = sum(c.values())
    return {k: (v / total if total > 0 else float("nan")) for k, v in c.items()}


def decomposition_complete(sA, sB, sC) -> dict:
    """Décomposition (`decomposition_variance`), parts tronquées, et variance observée de sA, rapportée (CL-22). La
    somme des composantes vaut (V̂[sA] + V̂[sB]) / 2 par construction : ce n'est pas un contrôle d'alignement, que fait
    `lire_pilote.notes_alignees` (contre-lecture 2, D-1)."""
    d = decomposition_variance(sA, sB, sC)
    a, b, c = (np.asarray(v, dtype=float) for v in (sA, sB, sC))
    gardees = ~(np.isnan(a) | np.isnan(b) | np.isnan(c))
    d["parts_tronquees"] = parts_tronquees(d["composantes"])
    d["variance_observee_A"] = float(np.var(a[gardees], ddof=1))
    d["composantes_negatives"] = sorted(k for k in ("tache", "generation") if d["composantes"][k] < 0)
    return d


def intervalles_parts_comptes(sA, sB, sC, tirages: int, rng: np.random.Generator, niveau: float = 0.95) -> dict:
    """Intervalles des parts tronquées par rééchantillonnage des tâches (percentiles), en comptant les tirages écartés
    (décomposition impossible ou part illisible) au lieu de les sauter en silence (CL-13, R5)."""
    a, b, c = (np.asarray(v, dtype=float) for v in (sA, sB, sC))
    complet = ~(np.isnan(a) | np.isnan(b) | np.isnan(c))
    a, b, c = a[complet], b[complet], c[complet]
    n = len(a)
    if n < 3:
        raise GardeArret(f"{n} tâches complètes : intervalles impossibles")
    tirees, ecartes = {k: [] for k in ("tache", "generation", "juge")}, 0
    for _ in range(tirages):
        idx = rng.integers(0, n, size=n)
        try:
            p = parts_tronquees(decomposition_variance(a[idx], b[idx], c[idx])["composantes"])
        except GardeArret:
            ecartes += 1
            continue
        if any(v != v for v in p.values()):
            ecartes += 1
            continue
        for k in tirees:
            tirees[k].append(p[k])
    if not tirees["juge"]:
        raise GardeArret("aucun tirage lisible")
    q = (1 - niveau) / 2
    return {"bornes": {k: [float(np.quantile(v, q)), float(np.quantile(v, 1 - q))] for k, v in tirees.items()},
            "tirages": tirages, "ecartes": ecartes, "reserve": ecartes > 0.01 * tirages}


def difference_appariee(notes_8b: tuple, notes_3b: tuple, tirages: int, rng: np.random.Generator,
                        niveau: float = 0.95) -> dict:
    """Différence des parts tronquées du juge (3B − 8B) sur les tâches complètes pour les deux juges, intervalle par
    rééchantillonnage apparié (les mêmes tâches tirées pour les deux juges ; CL-7)."""
    tous = [np.asarray(v, dtype=float) for v in (*notes_8b, *notes_3b)]
    if len({v.shape for v in tous}) != 1:
        raise GardeArret("notes des deux juges non alignées par tâche")
    complet = ~np.any([np.isnan(v) for v in tous], axis=0)
    tous = [v[complet] for v in tous]
    n = int(complet.sum())
    if n < 3:
        raise GardeArret(f"{n} tâches complètes pour les deux juges")

    def diff(idx):
        p8 = parts_tronquees(decomposition_variance(*(v[idx] for v in tous[:3]))["composantes"])["juge"]
        p3 = parts_tronquees(decomposition_variance(*(v[idx] for v in tous[3:]))["composantes"])["juge"]
        return p3 - p8

    point = diff(np.arange(n))
    tirees, ecartes = [], 0
    for _ in range(tirages):
        try:
            d = diff(rng.integers(0, n, size=n))
        except GardeArret:
            ecartes += 1
            continue
        if d != d:
            ecartes += 1
            continue
        tirees.append(d)
    if not tirees:                  # juge aux notes constantes : aucun tirage lisible (contre-lecture 2, D-13)
        raise GardeArret(f"aucun tirage lisible sur {tirages} : différence appariée impossible")
    q = (1 - niveau) / 2
    return {"taches": n, "difference": point, "borne": [float(np.quantile(tirees, q)), float(np.quantile(tirees, 1 - q))],
            "tirages": tirages, "ecartes": ecartes, "reserve": ecartes > 0.01 * tirages}


def regle_plan_b(part: float, borne_basse: float, part_incompletes: float, seuil_part: float = 0.8,
                 seuil_borne: float = 0.6, seuil_incompletes: float = 0.2) -> str:
    """Règle du plan B pour un juge (CL-6) : « plan B » si sa part tronquée dépasse 0,8 et la borne basse 0,6, ou si
    plus de 20 % de ses réponses (A, B, C) sont incomplètes ; « nœud » (zone d'indécision) si la part dépasse 0,8 mais
    pas la borne ; sinon « rubrique gardée »."""
    if part_incompletes > seuil_incompletes:
        return "plan B"
    if part != part:
        return "nœud"
    if part > seuil_part:
        return "plan B" if borne_basse > seuil_borne else "nœud"
    return "rubrique gardée"


def tirer_paires(paires: list[dict], rng: np.random.Generator, par_strate: int) -> list[dict]:
    """Sous-échantillon d'appariement stratifié par famille et par décision du 8B (CL-10) : au plus `par_strate`
    paires par strate, tirées sans remise ; chaque paire porte son poids (inverse de la probabilité de tirage)."""
    strates: dict[tuple, list] = {}
    for p in paires:
        strates.setdefault((p["famille"], bool(p["oui_8b"])), []).append(p)
    sortie = []
    for cle in sorted(strates, key=str):
        groupe = strates[cle]
        k = min(par_strate, len(groupe))
        for i in sorted(rng.choice(len(groupe), size=k, replace=False).tolist()):
            sortie.append(dict(groupe[i], poids=len(groupe) / k, strate=list(cle)))
    return sortie


def kappa_pondere(reference, juge, poids) -> dict:
    """Kappa de Cohen pondéré (poids d'échantillonnage), accords positif et négatif. Une seule classe pondérée :
    kappa indéfini (None), jamais une valeur par défaut."""
    r, j, w = np.asarray(reference, bool), np.asarray(juge, bool), np.asarray(poids, float)
    if not (r.shape == j.shape == w.shape) or r.size == 0 or np.any(w <= 0):
        raise GardeArret("étiquettes ou poids non alignés, vides ou non positifs")
    W = w.sum()
    po = float(w[r == j].sum() / W)
    pr, pj = float(w[r].sum() / W), float(w[j].sum() / W)
    pe = pr * pj + (1 - pr) * (1 - pj)
    a, b, c = float(w[r & j].sum()), float(w[r & ~j].sum()), float(w[~r & j].sum())
    d = float(w[~r & ~j].sum())
    return {"kappa": (po - pe) / (1 - pe) if pe < 1 else None, "accord": po,
            "accord_positif": 2 * a / (2 * a + b + c) if (2 * a + b + c) > 0 else None,
            "accord_negatif": 2 * d / (2 * d + b + c) if (2 * d + b + c) > 0 else None}


def intervalle_kappa_par_tache(echantillon: list[dict], tirages: int, rng: np.random.Generator,
                               niveau: float = 0.95) -> dict:
    """Intervalle du kappa pondéré par rééchantillonnage des tâches (les paires sont groupées par tâche, CL-5) ;
    tirages au kappa indéfini comptés."""
    taches = sorted({p["tache"] for p in echantillon})
    par_tache = {t: [p for p in echantillon if p["tache"] == t] for t in taches}
    valeurs, ecartes = [], 0
    for _ in range(tirages):
        tir = [p for i in rng.integers(0, len(taches), size=len(taches)) for p in par_tache[taches[i]]]
        k = kappa_pondere([p["reference"] for p in tir], [p["oui_8b"] for p in tir], [p["poids"] for p in tir])["kappa"]
        if k is None:
            ecartes += 1
        else:
            valeurs.append(k)
    if not valeurs:
        return {"borne": None, "tirages": tirages, "ecartes": ecartes, "reserve": True}
    q = (1 - niveau) / 2
    return {"borne": [float(np.quantile(valeurs, q)), float(np.quantile(valeurs, 1 - q))], "tirages": tirages,
            "ecartes": ecartes, "reserve": ecartes > 0.01 * tirages}


def masse_lisible(masses, mediane_min: float = 0.5, part_faible_max: float = 0.05, faible: float = 0.1) -> dict:
    """Lisibilité de l'appariement (CL-15) : la probabilité renormalisée sur {Yes, No} n'a de sens que si la masse de
    ces deux jetons n'est pas minuscule ; médiane ≥ 0,5 et moins de 5 % des paires sous 0,1."""
    m = np.asarray(masses, float)
    if m.size == 0:
        raise GardeArret("aucune paire d'appariement")
    mediane, part = float(np.median(m)), float(np.mean(m < faible))
    return {"mediane": mediane, "part_sous_seuil": part, "lisible": mediane >= mediane_min and part < part_faible_max}
