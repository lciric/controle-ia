"""Comparaison au plancher par différence appariée (remède (a) des lectures décisives de T0.7), v2 — fichier neuf (R12).

Préparé, **non fusionné**, en attente du mot de Lazar (nœud de R-2270, R-2271 : la définition de « au-dessus » est un seuil
gelé). Sources : note v2 de l'analyste `docs/notes/g0-deux-semaines-v1/t07-module-v2/erreur-premiere-espece-lectures-decisives-t07-v2.md`
(`5ccf0940…`), section 5, point 1 ; prototype `erreur-premiere-espece-t07-v1/remede_a_prototype_v1.py` (`3e488d70…`) ; consigne
`consigne-code-plancher-v2-t07-v1.md` (`4efbdbf4…`). `plancher_v1.py` ne change pas.

**Règle (a)** : une sonde est « au-dessus du plancher » si la **borne basse** de l'intervalle percentile, par blocs de tâches, de
la différence D = (aire de la sonde) − (quantile `quantile_plancher` des aires des directions du plancher) est **strictement
positive**. Sur chaque tirage de tâches, les aires de la sonde **et** des directions du plancher sont recalculées (mêmes tâches
tirées pour toutes) ; D* = A*_sonde − q*(A*_plancher) ; bornes = quantiles (1 − niveau)/2 et (1 + niveau)/2 de D*.

**Calcul exact.** Pour chaque direction k (la sonde en premier), une matrice de comparaisons entre tâches
C_k[t, u] = #(positif de t > négatif de u) + ½ #(égalités), comptée par tri ; **effectifs par tâche quelconques**. Un tirage
de multiplicités w (une par tâche) donne l'aire wᵀ C_k w / ((Σ w n1)(Σ w n0)) : numérateur et dénominateur sont des nombres
exacts en virgule flottante (entiers ou demi-entiers bien en deçà de 2⁵³), et la division est une seule opération ; l'aire
est donc **égale au bit près** à `sondes.evaluation.aire_sous_courbe` sur les actions tirées (essai versé, et contrôle à chaque
appel sur les aires ponctuelles).

**Tirages** : ceux d'`intervalle_blocs` (paquet gelé) sous la même graine — `default_rng(graine)`, un appel
`integers(0, blocs, size=blocs)` par tirage, blocs dans l'ordre de `np.unique` ; les tirages sans les deux classes sont
comptés et exclus, et au-delà de 1 % des tirages la fonction s'arrête (même garde, même message). `intervalle_blocs` est appelée
sous la même graine pour l'intervalle propre de la sonde (rapporté) ; l'égalité de ses bornes aux quantiles des aires de la
sonde sur les tirages de la différence est contrôlée à chaque appel (mêmes tirages, sinon arrêt).

Aucune moyenne ni médiane sur les jetons : la fonction ne lit que des scores d'action déjà agrégés (maximum ou attention).
"""
from __future__ import annotations

import numpy as np

from ..gardes import GardeArret
from ..sondes.evaluation import aire_sous_courbe, intervalle_blocs

METHODE = "difference_appariee_percentile"
SEUIL_DEGENERES = 0.01                         # celui d'`intervalle_blocs` (paquet gelé, l. 59)
LOT_DIRECTIONS = 25
SENS_DE_BAS = ("règle (a) : `bas` = quantile du plancher + borne basse de la différence appariée (aire de la sonde − quantile "
               "du plancher), `haut` = quantile + borne haute ; « au-dessus » si et seulement si la borne basse de la différence "
               "est strictement positive ; l'intervalle propre de la sonde est sous `bas_sonde` et `haut_sonde`")


def comparaisons_par_taches(scores, y, blocs) -> dict:
    """Matrices de comparaisons entre tâches. `scores` : (directions, actions) ou (actions,) ; `y` : 0/1 ; `blocs` : tâche de
    chaque action. Rend `C` (directions, tâches, tâches), `n1` et `n0` (effectifs positifs et négatifs par tâche, entiers) et
    `blocs` (tâches dans l'ordre de `np.unique`, celui d'`intervalle_blocs`)."""
    X = np.asarray(scores, dtype=np.float64)
    if X.ndim == 1:
        X = X[None, :]
    y, blocs = np.asarray(y), np.asarray(blocs)
    if X.ndim != 2 or y.ndim != 1 or blocs.shape != y.shape or X.shape[1] != y.size or X.shape[0] < 1:
        raise GardeArret(f"scores de forme {X.shape}, étiquettes {y.shape}, blocs {blocs.shape} : (directions, actions), (actions,), "
                         "(actions,) attendues")
    if not np.all(np.isfinite(X)):
        raise GardeArret("score non fini")
    if not np.all((y == 0) | (y == 1)):
        raise GardeArret("étiquettes 0/1 attendues")
    pos, neg = y == 1, y == 0
    n_pos, n_neg = int(pos.sum()), int(neg.sum())
    if n_pos == 0 or n_neg == 0:
        raise GardeArret("les deux classes 0/1 sont nécessaires")
    uniques, code = np.unique(blocs, return_inverse=True)
    code = np.asarray(code).reshape(-1)
    nb = uniques.size
    t_pos, t_neg = code[pos], code[neg]
    G = np.zeros((nb, n_pos))
    G[t_pos, np.arange(n_pos)] = 1.0                      # positif → sa tâche
    C = np.empty((X.shape[0], nb, nb))
    lignes = np.arange(1, n_neg + 1)
    for k in range(X.shape[0]):
        p, q = X[k, pos], X[k, neg]
        ordre = np.argsort(q, kind="stable")
        cum = np.zeros((n_neg + 1, nb))
        cum[lignes, t_neg[ordre]] = 1.0
        np.cumsum(cum, axis=0, out=cum)                   # cum[r, u] = négatifs de la tâche u parmi les r plus petits
        q_tries = q[ordre]
        strict = np.searchsorted(q_tries, p, side="left")     # négatifs < p
        large = np.searchsorted(q_tries, p, side="right")     # négatifs ≤ p
        C[k] = G @ (0.5 * (cum[strict] + cum[large]))         # #(<) + ½ #(=), sommé par tâche du positif
    return {"C": C, "n1": np.bincount(t_pos, minlength=nb).astype(np.int64),
            "n0": np.bincount(t_neg, minlength=nb).astype(np.int64), "blocs": uniques}


def poids_des_tirages(n_blocs: int, n_tirages: int, graine: int) -> np.ndarray:
    """Multiplicités (tirages, blocs) des blocs tirés avec remise : **la suite d'`intervalle_blocs`** sous la même graine
    (`default_rng(graine)`, un appel `integers(0, n_blocs, size=n_blocs)` par tirage : même consommation du générateur)."""
    n_blocs, n_tirages = int(n_blocs), int(n_tirages)
    if n_blocs < 2:
        raise GardeArret("au moins deux blocs pour un rééchantillonnage par blocs")
    if n_tirages < 1:
        raise GardeArret(f"n_tirages {n_tirages} : au moins un tirage")
    rng = np.random.default_rng(int(graine))
    W = np.empty((n_tirages, n_blocs))
    for b in range(n_tirages):
        W[b] = np.bincount(rng.integers(0, n_blocs, size=n_blocs), minlength=n_blocs)
    return W


def aires_tirees(C: np.ndarray, poids, n1, n0) -> np.ndarray:
    """Aires (directions, tirages) : wᵀ C_k w / ((Σ w n1)(Σ w n0)) ; tout tirage sans les deux classes est refusé (l'appelant
    les exclut et les compte)."""
    W = np.asarray(poids, dtype=np.float64)
    if W.ndim != 2 or W.shape[1] != C.shape[1] or C.shape[1] != C.shape[2]:
        raise GardeArret(f"poids de forme {W.shape} pour des comparaisons de forme {C.shape}")
    den = (W @ np.asarray(n1, dtype=np.float64)) * (W @ np.asarray(n0, dtype=np.float64))
    if np.any(den <= 0.0):
        raise GardeArret("tirage sans les deux classes passé au calcul des aires")
    sortie = np.empty((C.shape[0], W.shape[0]))
    for a in range(0, C.shape[0], LOT_DIRECTIONS):
        M = np.matmul(W[None], C[a:a + LOT_DIRECTIONS])
        sortie[a:a + LOT_DIRECTIONS] = (M * W[None]).sum(axis=-1)
    return sortie / den[None, :]


def difference_sur_poids(C: np.ndarray, n1, n0, poids, quantile_plancher: float, niveau: float) -> dict:
    """D* = A*_sonde − quantile des A*_plancher sur chaque tirage valide (`C[0]` : la sonde ; `C[1:]` : les directions) ;
    tirages sans les deux classes comptés, exclus, arrêt au-delà de 1 % ; bornes percentiles au niveau donné."""
    if C.shape[0] < 2:
        raise GardeArret("au moins une direction de plancher")
    W = np.asarray(poids, dtype=np.float64)
    valides = ((W @ np.asarray(n1, dtype=np.float64)) > 0) & ((W @ np.asarray(n0, dtype=np.float64)) > 0)
    degeneres = int((~valides).sum())
    if degeneres > SEUIL_DEGENERES * W.shape[0]:
        raise GardeArret(f"{degeneres} tirages sur {W.shape[0]} sans les deux classes : blocs trop déséquilibrés")
    A = aires_tirees(C, W[valides], n1, n0)
    D = A[0] - np.quantile(A[1:], float(quantile_plancher), axis=0)
    a = (1.0 - float(niveau)) / 2.0
    return {"bas": float(np.quantile(D, a)), "haut": float(np.quantile(D, 1.0 - a)), "tirages": int(D.size),
            "degeneres": degeneres, "aires_sonde": A[0]}


def comparer_difference_au_plancher(scores_sonde, scores_plancher, y, blocs, n_tirages: int, graine: int,
                                    quantile_plancher: float = 0.95, niveau: float = 0.95) -> dict:
    """Règle (a) sur scores seuls (étape B) ; mêmes arguments que `plancher_v1.comparer_scores_au_plancher`. Rend les clés de
    celle-ci — `aire`, `bas` et `haut` (intervalle propre de la sonde par `intervalle_blocs`, rapporté), `plancher_quantile`,
    `plancher_mediane`, `n_plancher`, `degeneres`, `tirages`, `niveau`, `plancher` {quantile, quantile_plancher, mediane, max,
    n}, `effectifs` — plus `difference` {estimation, bas, haut, methode, niveau, tirages, degeneres}, et
    **`au_dessus_du_plancher` = borne basse de la différence > 0** (sens neuf, déclaré)."""
    s = np.asarray(scores_sonde, dtype=np.float64)
    P = np.asarray(scores_plancher, dtype=np.float64)
    y, blocs = np.asarray(y), np.asarray(blocs)
    if s.ndim != 1 or P.ndim != 2 or P.shape[1] != s.size or P.shape[0] < 1:
        raise GardeArret(f"scores de forme {s.shape} et plancher de forme {P.shape} : (n_actions,) et (n_directions, n_actions) attendues")
    if not 0.5 < float(niveau) < 1.0:
        raise GardeArret(f"niveau {niveau} hors de ]0,5 ; 1[")
    if not 0.0 < float(quantile_plancher) < 1.0:
        raise GardeArret(f"quantile_plancher {quantile_plancher} hors de ]0 ; 1[")
    comp = comparaisons_par_taches(np.vstack([s[None, :], P]), y, blocs)
    C, n1, n0 = comp["C"], comp["n1"], comp["n0"]
    W = poids_des_tirages(comp["blocs"].size, n_tirages, graine)
    aire = aire_sous_courbe(s, y)                                       # paquet gelé
    aires = np.array([aire_sous_courbe(P[k], y) for k in range(P.shape[0])])
    ponctuelles = aires_tirees(C, np.ones((1, comp["blocs"].size)), n1, n0)[:, 0]
    if ponctuelles[0] != aire or not np.array_equal(ponctuelles[1:], aires):
        raise GardeArret("aires du comptage par tâches ≠ aire_sous_courbe du paquet gelé : comptage inexact, arrêt")
    d = difference_sur_poids(C, n1, n0, W, float(quantile_plancher), float(niveau))
    ic = intervalle_blocs(s, y, blocs, int(n_tirages), int(graine), float(niveau))
    a = (1.0 - float(niveau)) / 2.0
    if (ic["degeneres"] != d["degeneres"] or ic["tirages"] != d["tirages"]
            or float(np.quantile(d["aires_sonde"], a)) != ic["bas"] or float(np.quantile(d["aires_sonde"], 1.0 - a)) != ic["haut"]):
        raise GardeArret("tirages de la différence ≠ tirages d'intervalle_blocs sous la même graine : arrêt")
    seuil = float(np.quantile(aires, float(quantile_plancher)))
    difference = {"estimation": float(ic["aire"]) - seuil, "bas": d["bas"], "haut": d["haut"], "methode": METHODE,
                  "niveau": float(niveau), "tirages": d["tirages"], "degeneres": d["degeneres"]}
    return {"aire": ic["aire"], "bas": ic["bas"], "haut": ic["haut"], "plancher_quantile": seuil,
            "plancher_mediane": float(np.median(aires)), "n_plancher": int(aires.size),
            "au_dessus_du_plancher": bool(d["bas"] > 0.0),
            "degeneres": ic["degeneres"], "tirages": ic["tirages"], "niveau": float(niveau),
            "plancher": {"quantile": seuil, "quantile_plancher": float(quantile_plancher), "mediane": float(np.median(aires)),
                         "max": float(aires.max()), "n": int(aires.size)},
            "effectifs": {"positifs": int((y == 1).sum()), "negatifs": int((y == 0).sum())},
            "difference": difference}


def resume_pour_critere(r: dict) -> dict:
    """Résumé au format de `criteres_v1.etat_pour_sonde` (inchangée) : `bas` = quantile + borne basse de la différence,
    `haut` = quantile + borne haute ; intervalle propre de la sonde sous `bas_sonde`, `haut_sonde` ; `sens_de_bas` écrit. Garde :
    `bas` > quantile doit valoir `au_dessus_du_plancher` (borne basse de la différence > 0) ; une borne positive perdue à
    l'addition (inférieure à la moitié de l'écart entre deux flottants voisins du quantile) arrête, sans repli."""
    q = float(r["plancher_quantile"])
    d = r["difference"]
    sortie = dict(r)
    sortie.update({"bas_sonde": r["bas"], "haut_sonde": r["haut"], "bas": q + float(d["bas"]), "haut": q + float(d["haut"]),
                   "sens_de_bas": SENS_DE_BAS})
    if (sortie["bas"] > q) != bool(r["au_dessus_du_plancher"]) or bool(r["au_dessus_du_plancher"]) != (float(d["bas"]) > 0.0):
        raise GardeArret(f"borne basse de la différence {d['bas']!r} et quantile du plancher {q!r} : « au-dessus » illisible sur "
                         "l'échelle de l'aire (borne perdue à l'addition) : arrêt")
    return sortie


__all__ = ["METHODE", "SENS_DE_BAS", "comparaisons_par_taches", "poids_des_tirages", "aires_tirees", "difference_sur_poids",
           "comparer_difference_au_plancher", "resume_pour_critere"]
