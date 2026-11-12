"""Entrées du préenregistrement agrégation R1 v4 — v1 : chargement et gardes (liste d'arrêt).

Formats : fiche de réception v4 (`fiche-reception-r1-v4-v2.md`, section 4.5) — dans chaque fichier d'activations, exactement
14 tableaux : le tableau principal (`maximum` ou `moyenne`, (2400, 3, 4096) `<f2`) et 13 tableaux communs ; identité au type et
à la forme des mêmes tableaux de `scores-p3.npz`, valeurs égales vérifiées ici. Toute garde lève `GardeArret` (R5).
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np

from ..gardes import GardeArret

COUCHES = (7, 15, 23)
INDICE_COUCHE_15 = 1
LIGNES = 2400
LARGEUR = 4096
COMMUNS = ("jetons_empan", "jetons_empan_rejeu", "couches", "conforme_longueur", "contexte_conforme", "fidele",
           "trajectoire_identique", "activations_identiques", "ecart_fidelite", "episode", "pas", "condition", "tache")
IDENTITE = ("episode", "pas", "condition", "tache")
CONDITIONS = ("honnete", "saboteur", "temoin", "mention")
N_TACHES = 60
N_PAS = 10
SONDES_G = {"Gt": "tromperie-difference_moyennes-c15", "Ge": "enjeux-lineaire-c15"}


@dataclass
class Entrees:
    maximum: np.ndarray          # (lignes, largeur) float64, couche 15
    moyenne: np.ndarray          # (lignes, largeur) float64, couche 15
    fidele: np.ndarray           # (lignes,) bool
    episode: np.ndarray
    pas: np.ndarray
    condition: np.ndarray        # (lignes,) str
    tache: np.ndarray            # (lignes,) str
    scores_g: dict               # {"Gt": (lignes,), "Ge": (lignes,)} float64
    notee: np.ndarray            # (lignes,) bool : tous les scores de la ligne de P3 finis


def _charger_npz(chemin: Path, principal: str, lignes: int, largeur: int) -> dict:
    if not Path(chemin).is_file():
        raise GardeArret(f"{chemin} : fichier absent")
    try:
        with np.load(chemin, allow_pickle=False) as z:
            t = {k: z[k] for k in z.files}
    except Exception as e:  # illisible : arrêt, motif écrit
        raise GardeArret(f"{chemin} : illisible ({type(e).__name__}: {e})") from e
    attendus = set(COMMUNS) | {principal}
    if set(t) != attendus or len(t) != 14:
        raise GardeArret(f"{chemin} : tableaux {sorted(t)} ≠ attendus {sorted(attendus)}")
    a = t[principal]
    if a.shape != (lignes, 3, largeur) or a.dtype != np.dtype("<f2"):
        raise GardeArret(f"{chemin} : {principal} de forme {a.shape} et de type {a.dtype} ≠ ({lignes}, 3, {largeur}) <f2")
    if [int(c) for c in t["couches"]] != list(COUCHES):
        raise GardeArret(f"{chemin} : couches {t['couches'].tolist()} ≠ {list(COUCHES)}")
    for k in COMMUNS:
        if t[k].shape != ((3,) if k == "couches" else (lignes,)):
            raise GardeArret(f"{chemin} : {k} de forme {t[k].shape}")
    if t["fidele"].dtype != np.bool_:
        raise GardeArret(f"{chemin} : fidele de type {t['fidele'].dtype} ≠ bool")
    return t


def charger(chemin_maximum, chemin_moyenne, chemin_scores_p3, lignes: int = LIGNES, largeur: int = LARGEUR) -> Entrees:
    tm = _charger_npz(Path(chemin_maximum), "maximum", lignes, largeur)
    tv = _charger_npz(Path(chemin_moyenne), "moyenne", lignes, largeur)
    for k in COMMUNS:
        if tm[k].dtype != tv[k].dtype or not np.array_equal(tm[k], tv[k], equal_nan=tm[k].dtype.kind == "f"):
            raise GardeArret(f"tableau commun {k} différent entre les deux fichiers d'activations")
    if not Path(chemin_scores_p3).is_file():
        raise GardeArret(f"{chemin_scores_p3} : fichier absent")
    with np.load(chemin_scores_p3, allow_pickle=False) as z:
        p3 = {k: z[k] for k in ("noms_sondes", "scores", *IDENTITE) if k in z.files}
    for k in ("noms_sondes", "scores", *IDENTITE):
        if k not in p3:
            raise GardeArret(f"{chemin_scores_p3} : tableau {k} absent")
    for k in IDENTITE:
        if p3[k].shape != tm[k].shape or p3[k].dtype != tm[k].dtype or not np.array_equal(p3[k], tm[k]):
            raise GardeArret(f"identité {k} de R1 v4 ≠ celle de scores-p3.npz (type, forme ou valeurs)")
    noms = [str(n) for n in p3["noms_sondes"].tolist()]
    if p3["scores"].shape != (lignes, len(noms)):
        raise GardeArret(f"scores de P3 de forme {p3['scores'].shape}")
    scores_g = {}
    for court, nom in SONDES_G.items():
        if nom not in noms:
            raise GardeArret(f"sonde {nom} absente de noms_sondes")
        scores_g[court] = p3["scores"][:, noms.index(nom)].astype(np.float64)
    condition = np.asarray([str(c) for c in tm["condition"].tolist()])
    tache = np.asarray([str(c) for c in tm["tache"].tolist()])
    verifier_structure(tm["episode"], tm["pas"], condition, tache)
    return Entrees(maximum=tm["maximum"][:, INDICE_COUCHE_15, :].astype(np.float64),
                   moyenne=tv["moyenne"][:, INDICE_COUCHE_15, :].astype(np.float64),
                   fidele=tm["fidele"].astype(bool), episode=tm["episode"], pas=tm["pas"].astype(np.int64),
                   condition=condition, tache=tache, scores_g=scores_g,
                   notee=np.all(np.isfinite(p3["scores"]), axis=1))


def verifier_structure(episode, pas, condition, tache, n_taches: int = N_TACHES, n_pas: int = N_PAS) -> None:
    if set(condition.tolist()) != set(CONDITIONS):
        raise GardeArret(f"conditions {sorted(set(condition.tolist()))} ≠ {sorted(CONDITIONS)}")
    taches = sorted(set(tache.tolist()))
    if len(taches) != n_taches:
        raise GardeArret(f"{len(taches)} tâches ≠ {n_taches}")
    for t in taches:
        for c in CONDITIONS:
            sel = (tache == t) & (condition == c)
            eps = np.unique(np.asarray(episode)[sel])
            if eps.size != 1 or sel.sum() != n_pas or sorted(np.asarray(pas)[sel].tolist()) != list(range(n_pas)):
                raise GardeArret(f"tâche {t}, condition {c} : exactement un épisode de {n_pas} actions de pas 0 à "
                                 f"{n_pas - 1} attendu")
    for e in np.unique(episode):
        if np.unique(condition[np.asarray(episode) == e]).size != 1 or np.unique(tache[np.asarray(episode) == e]).size != 1:
            raise GardeArret(f"épisode {e} : condition ou tâche non unique")


def eligibles(e: Entrees) -> np.ndarray:
    """fidele ∧ notée par P3 ; une activation non finie sur une action éligible arrête."""
    el = e.fidele & e.notee
    for nom, a in (("maximum", e.maximum), ("moyenne", e.moyenne)):
        if not np.all(np.isfinite(a[el])):
            raise GardeArret(f"activation non finie ({nom}, couche 15) sur une action éligible")
    return el
