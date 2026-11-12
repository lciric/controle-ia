"""Test de dérive temporel, séparé, sur les épisodes honnêtes de la couche 2 — v1 (P-18), entièrement paramétré.

Source (lue le 29 octobre 2026) : P-18 (E-6) du format décision v5 de conv-audit (`decision-pilote-couche-2-v5.md`,
`255a364e…`, sur `refs/canal-local/conv-audit`), réécrit en v3 après la décision de Lazar sur P-17 (R-697 : coupe du
calibrage par graine scellée d'avance ; « dérive entre exécutions cherchée par un test temporel séparé ») :
« Test de dérive temporel, séparé, préenregistré sur les 9 600 honnêtes […] Ce qui reste à fixer : sa conséquence.
Options (a) conséquence gelée au préenregistrement : dérive au-delà d'un seuil scellé → nœud pour Lazar avant toute
lecture de G1 (la banque est signalée, pas jetée) ; (b) lecture d'épreuve seulement (consignée, sans conséquence).
[…] Forme proposée : écart des moyennes premières/dernières exécutions par tâche, en écart-type intra-tâche, seuil
scellé (0,10 est la valeur à laquelle la coupe temporelle cassait), bilatéral. »

**Rien n'est tranché** : la forme est « proposée », le seuil n'est pas scellé, la part des « premières/dernières »
exécutions et l'agrégation entre tâches ne sont écrites nulle part, la conséquence est ouverte. Ce module ne porte donc
aucune valeur par défaut : statistique, ses paramètres, seuil, conséquence, cellules et effectif minimal par tâche sont
des arguments obligatoires. Deux statistiques sont offertes :

- `ecart_premieres_dernieres` (forme proposée par P-18) : dans chaque tâche, épisodes rangés par rang de fabrique ;
  k = ⌊part × n_t⌋ premières et k dernières ; écart des moyennes (dernières − premières) ; moyenne de ces écarts sur les
  tâches (poids égaux), divisée par l'écart-type intra-tâche groupé (somme des carrés dans les tâches sur la somme des
  degrés de liberté n_t − 1). Positif : les scores montent avec le rang. Paramètre : `part` dans ]0 ; 0,5].
- `spearman_rang` (synthèse du tour complémentaire, § 3.1, A, « Spearman ») : corrélation de rang de Spearman entre rang
  de fabrique et score dans chaque tâche, moyenne sur les tâches (poids égaux). Aucun paramètre.

Le verdict est bilatéral, cellule par cellule : la dérive sonne si |statistique| > seuil dans au moins une cellule. Aucune
correction de multiplicité (le seuil porte sur une taille d'effet, comme P-18 la propose). Une p-valeur par permutation
des rangs dans chaque tâche est calculée si `n_permutations > 0` ; elle est consignée et **ne décide rien**.

Gardes (R5, aucun repli) : épisode non honnête, score non fini ou manquant, cellule inattendue, rang en double, tâche
trop courte, tâche constante (Spearman indéfini), écart-type intra-tâche nul, paramètre manquant ou inconnu.
"""
from __future__ import annotations

import math

import numpy as np
from scipy.stats import rankdata

from ..gardes import GardeArret, exiger_numpy_minimal
from ..manifeste import cle_de_tache

VERSION = "derive-v1"
ETIQUETTE_HONNETE = "honnete"
STATISTIQUES = {"ecart_premieres_dernieres": ("part",), "spearman_rang": ()}
CONSEQUENCES = ("noeud_avant_G1", "lecture_seule")
_TEXTE_CONSEQUENCE = {
    "noeud_avant_G1": "P-18 (a) : dérive au-delà du seuil scellé → nœud pour Lazar avant toute lecture de G1 ; "
                      "banque signalée, pas jetée",
    "lecture_seule": "P-18 (b) : lecture d'épreuve seulement, consignée, sans conséquence",
}


class DeriveConstatee(GardeArret):
    """La dérive a sonné sous la conséquence (a) de P-18 : nœud avant toute lecture de G1."""


def _exiger_reel(v, nom: str) -> float:
    if isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v):
        raise GardeArret(f"{nom} : réel fini exigé, reçu {v!r} (aucune imputation)")
    return float(v)


def _exiger_parametres(statistique: str, parametres: dict) -> dict:
    if statistique not in STATISTIQUES:
        raise GardeArret(f"statistique {statistique!r} inconnue ({', '.join(STATISTIQUES)})")
    if not isinstance(parametres, dict):
        raise GardeArret("paramètres de la statistique : dictionnaire exigé (vide si aucun)")
    attendus = set(STATISTIQUES[statistique])
    if set(parametres) != attendus:
        raise GardeArret(f"paramètres de {statistique} : attendus {sorted(attendus)}, reçus {sorted(parametres)} "
                         "(aucun défaut)")
    sortie = {}
    if statistique == "ecart_premieres_dernieres":
        part = _exiger_reel(parametres["part"], "part")
        if not 0 < part <= 0.5:
            raise GardeArret(f"part {part} hors de ]0 ; 0,5]")
        sortie["part"] = part
    return sortie


def _grouper(episodes: list[dict], cellules: tuple[str, ...], n_min_par_tache: int) -> dict[str, dict]:
    """{tâche: {"rangs": tableau trié, "scores": {cellule: tableau dans l'ordre des rangs}}}."""
    if not isinstance(episodes, list) or not episodes:
        raise GardeArret("épisodes : liste non vide exigée")
    par_tache: dict[str, list] = {}
    rangs_vus = set()
    for i, e in enumerate(episodes):
        if not isinstance(e, dict) or set(e) != {"tache", "rang", "etiquette", "scores"}:
            raise GardeArret(f"épisode {i} : champs attendus tache, rang, etiquette, scores")
        if e["etiquette"] != ETIQUETTE_HONNETE:
            raise GardeArret(f"épisode {i} : étiquette {e['etiquette']!r} ; le test de dérive ne lit que les honnêtes")
        if not isinstance(e["tache"], str) or not e["tache"]:
            raise GardeArret(f"épisode {i} : tâche textuelle exigée")
        r = e["rang"]
        if isinstance(r, bool) or not isinstance(r, int) or r < 0:
            raise GardeArret(f"épisode {i} : rang de fabrique entier ≥ 0 exigé")
        if r in rangs_vus:
            raise GardeArret(f"rang {r} en double : un rang de fabrique désigne un seul épisode")
        rangs_vus.add(r)
        s = e["scores"]
        if not isinstance(s, dict) or set(s) != set(cellules):
            manque = sorted(set(cellules) - set(s)) if isinstance(s, dict) else cellules
            trop = sorted(set(s) - set(cellules)) if isinstance(s, dict) else []
            raise GardeArret(f"épisode {i} : cellules manquantes {manque}, inattendues {trop}")
        par_tache.setdefault(e["tache"], []).append(
            (r, {c: _exiger_reel(s[c], f"épisode {i}, cellule {c}") for c in cellules}))
    sortie = {}
    for t, liste in sorted(par_tache.items()):
        if len(liste) < n_min_par_tache:
            raise GardeArret(f"tâche {t!r} : {len(liste)} épisodes < {n_min_par_tache} exigés")
        liste.sort(key=lambda x: x[0])
        sortie[t] = {"rangs": np.array([x[0] for x in liste]),
                     "scores": {c: np.array([x[1][c] for x in liste]) for c in cellules}}
    return sortie


def _ecart(series: list[np.ndarray], part: float) -> float:
    ecarts, ss, ddl = [], 0.0, 0
    for x in series:
        n = len(x)
        k = int(math.floor(part * n))
        if k < 1:
            raise GardeArret(f"tâche de {n} épisodes : ⌊{part} × {n}⌋ = 0 épisode par extrémité")
        ecarts.append(float(np.mean(x[n - k:]) - np.mean(x[:k])))
        ss += float(np.sum((x - np.mean(x)) ** 2))
        ddl += n - 1
    sigma = math.sqrt(ss / ddl) if ddl > 0 else 0.0
    if not sigma > 0:
        raise GardeArret("écart-type intra-tâche nul : statistique indéfinie (scores constants dans chaque tâche)")
    return float(np.mean(ecarts)) / sigma


def _spearman(series: list[np.ndarray]) -> float:
    rhos = []
    for x in series:
        if np.all(x == x[0]):
            raise GardeArret("tâche à scores constants : Spearman indéfini (aucun repli)")
        rx = rankdata(x)
        rr = np.arange(len(x), dtype=float)
        rhos.append(float(np.corrcoef(rr, rx)[0, 1]))
    return float(np.mean(rhos))


def _statistique(statistique: str, params: dict, series: list[np.ndarray]) -> float:
    if statistique == "ecart_premieres_dernieres":
        return _ecart(series, params["part"])
    return _spearman(series)


def tester_derive(episodes: list[dict], *, statistique: str, parametres: dict, seuil: float, consequence: str,
                  cellules: list[str] | tuple[str, ...], n_min_par_tache: int, n_permutations: int,
                  entropie: int | None) -> dict:
    """Calcule la statistique de dérive par cellule et le verdict bilatéral au seuil. Tous les arguments sont
    obligatoires ; `entropie` est exigée si `n_permutations > 0` et doit être `None` sinon."""
    exiger_numpy_minimal()
    params = _exiger_parametres(statistique, parametres)
    seuil = _exiger_reel(seuil, "seuil")
    if seuil <= 0:
        raise GardeArret(f"seuil {seuil} : strictement positif exigé")
    if consequence not in CONSEQUENCES:
        raise GardeArret(f"conséquence {consequence!r} inconnue ({', '.join(CONSEQUENCES)})")
    cellules = tuple(cellules)
    if not cellules or len(set(cellules)) != len(cellules) or any(not isinstance(c, str) or not c for c in cellules):
        raise GardeArret(f"cellules : liste non vide, sans doublon, exigée ({cellules})")
    if isinstance(n_min_par_tache, bool) or not isinstance(n_min_par_tache, int) or n_min_par_tache < 2:
        raise GardeArret(f"effectif minimal par tâche {n_min_par_tache!r} : entier ≥ 2 exigé")
    if isinstance(n_permutations, bool) or not isinstance(n_permutations, int) or n_permutations < 0:
        raise GardeArret(f"n_permutations {n_permutations!r} : entier ≥ 0 exigé")
    if n_permutations > 0 and entropie is None:
        raise GardeArret("permutations demandées sans entropie (R9)")
    if n_permutations == 0 and entropie is not None:
        raise GardeArret("entropie fournie sans permutation : incohérent")
    groupes = _grouper(episodes, cellules, n_min_par_tache)

    racine = np.random.SeedSequence(entropie) if n_permutations > 0 else None
    par_cellule = {}
    for c in cellules:
        series = [groupes[t]["scores"][c] for t in groupes]
        valeur = _statistique(statistique, params, series)
        entree = {"valeur": valeur, "sonne": abs(valeur) > seuil}
        if racine is not None:
            rng = np.random.default_rng(np.random.SeedSequence(racine.entropy, spawn_key=(cle_de_tache(c),)))
            nulles = np.empty(n_permutations)
            for b in range(n_permutations):
                nulles[b] = _statistique(statistique, params, [rng.permutation(x) for x in series])
            entree["p_permutation_bilaterale"] = float((1 + np.sum(np.abs(nulles) >= abs(valeur)))
                                                       / (1 + n_permutations))
        par_cellule[c] = entree
    sonne = any(v["sonne"] for v in par_cellule.values())
    return {
        "version": VERSION, "statistique": statistique, "parametres": params, "seuil": seuil, "bilateral": True,
        "consequence": consequence, "texte_consequence": _TEXTE_CONSEQUENCE[consequence],
        "cellules": list(cellules), "n_taches": len(groupes),
        "n_episodes": int(sum(len(g["rangs"]) for g in groupes.values())), "n_min_par_tache": n_min_par_tache,
        "n_permutations": n_permutations,
        "entropie": None if racine is None else str(racine.entropy),
        "par_cellule": par_cellule, "sonne": sonne,
        "cellules_qui_sonnent": [c for c in cellules if par_cellule[c]["sonne"]],
        "note": "p-valeur par permutation consignée seulement ; seule |valeur| > seuil décide",
    }


def exiger_sans_derive(verdict: dict) -> dict:
    """Applique la conséquence scellée : sous (a), une dérive qui sonne lève `DeriveConstatee` (nœud avant G1) ; sous
    (b), le verdict est renvoyé pour consignation, sans conséquence."""
    if verdict.get("version") != VERSION or verdict.get("consequence") not in CONSEQUENCES:
        raise GardeArret("verdict de dérive illisible ou d'une autre version")
    if verdict["sonne"] and verdict["consequence"] == "noeud_avant_G1":
        raise DeriveConstatee(f"dérive au-delà du seuil {verdict['seuil']} dans {verdict['cellules_qui_sonnent']} "
                              f"({verdict['statistique']}) : {verdict['texte_consequence']}")
    return verdict


__all__ = ["VERSION", "STATISTIQUES", "CONSEQUENCES", "DeriveConstatee", "tester_derive", "exiger_sans_derive"]
