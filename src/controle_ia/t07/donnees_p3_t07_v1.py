"""Données génériques de P3 pour T7-P10 de la tromperie et des enjeux (brouillon 19, `07039ed2…`, plan, point 10 : « témoin
lexical par concept, entraîné sur les données génériques du concept — pour la tromperie et les enjeux, les données de P3 à la
provenance scellée, **même découpage que P3** — avant toute lecture d'organisme »), v1.

Entrées (clé de configuration facultative `donnees_p3`, quatre fichiers cités par chemin et empreinte, sceaux vérifiés dans la
garde de l'étape A) : les 306 faits (`donnees/T0.7-faits-repe-v1/facts_true_false.csv`, `151b6163…`), les textes des enjeux
(`donnees/T0.7-models-under-pressure-v1/training/train.jsonl`, `04216df3…`), le manifeste du run de P3
(`runs/20261019-230011-p3-reel/manifeste.json`, `3f21774c…` : configuration et graines « tirage-enjeux »,
« decoupage-tromperie », « decoupage-enjeux ») et le résultat de P3 (`diag/20261019-230011-p3-reel/sondes-figees.json`,
`fb418127…` : `donnees.faits_exclus`, `donnees.lignes_enjeux`, `effectifs`). Rien de 7a, rien sous embargo.

**Découpage de P3 reproduit** avec les fonctions de P3 appelées telles quelles (`premier_test_ia.donnees.charger_faits`,
`exemples_tromperie`, `charger_enjeux`, `tirer_enjeux`, `decouper`) et les graines du manifeste de P3 (`manifeste.generateur`) :
- tromperie : exemples de P3 (fait sous les deux consignes), moins les faits que P3 a exclus faute d'empan (liste lue dans le
  résultat de P3, pas recalculée : elle dépend du tokeniseur) ; découpage par fait, graine « decoupage-tromperie » ;
- enjeux : tirage de P3 (graine « tirage-enjeux », `n_par_classe_enjeux`), **égal aux lignes écrites par P3** (sinon arrêt) ;
  découpage par paire, graine « decoupage-enjeux » ;
- garde : effectifs d'entraînement et de validation égaux à `effectifs` du résultat de P3 (sinon arrêt, R11).

**Empan du témoin** (interprétation déclarée) : le texte que lit la sonde de P3 — le fait (réponse imposée) pour la tromperie,
le texte de l'utilisateur pour les enjeux ; texte entier (la sonde en lit les jetons sans les 5 derniers, ou au plus 128 jetons :
coupures qui demandent le tokeniseur, non reproduites au niveau du texte). Pour la tromperie, les deux exemples d'un fait ont le
même texte : le témoin y est au hasard par construction (comme pour J-D). Pénalité choisie sur la validation générique de P3,
dans la liste gelée, sans tirage (`sondes_neuves_v1.PENALITES_LEXICALES`, ex aequo par l'ordre croissant). Un texte sans aucun
mot (le jeu des enjeux en porte un, `','`) est exclu de l'entraînement et de la validation du **témoin** seulement
(`temoin_lexical` le refuse) ; il est compté (`textes_sans_mot_exclus`).
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from ..gardes import GardeArret
from ..manifeste import generateur
from ..premier_test_ia import donnees as dn
from ..scellement import verifier
from ..sondes.evaluation import aire_sous_courbe
from ..sondes.temoins import MOTIF_MOT, temoin_lexical
from .sondes_neuves_v1 import PENALITES_LEXICALES

CLES = ("faits", "enjeux", "manifeste_p3", "sondes_figees_p3")
CHEMINS_REELS = {"faits": dn.CHEMIN_FAITS, "enjeux": dn.CHEMIN_ENJEUX, "manifeste_p3": "runs/20261019-230011-p3-reel/manifeste.json",
                 "sondes_figees_p3": "diag/20261019-230011-p3-reel/sondes-figees.json"}
SHA_REELLES = {"faits": dn.SHA_FAITS, "enjeux": dn.SHA_ENJEUX,
               "manifeste_p3": "3f21774ca2a740e059191e762a4922076d954ee4c3e728c9927ba436cb211685",
               "sondes_figees_p3": "fb41812732711c1a2a152fa776c46be5a4c50a72ccdc8fd9b7b7f9edcc37d208"}


def exiger_config(d, mode: str) -> None:
    """Forme de `donnees_p3` : objet aux quatre clés, chacune {chemin, sha256} ; en mode réel, les fichiers et empreintes de la
    provenance scellée de P3."""
    if not isinstance(d, dict) or set(d) != set(CLES):
        raise GardeArret(f"donnees_p3 : objet aux clés {list(CLES)} attendu")
    for k in CLES:
        if not isinstance(d[k], dict) or set(d[k]) != {"chemin", "sha256"} or not isinstance(d[k]["chemin"], str):
            raise GardeArret(f"donnees_p3.{k} : {{chemin, sha256}} attendu")
    if mode == "reel":
        for k in CLES:
            if d[k]["chemin"] != CHEMINS_REELS[k] or d[k]["sha256"] != SHA_REELLES[k]:
                raise GardeArret(f"donnees_p3.{k} : {CHEMINS_REELS[k]} à l'empreinte {SHA_REELLES[k][:8]}… attendu en mode réel")


def controler(racine: Path, d: dict) -> dict:
    """Sceau de chaque fichier (compagnon `.sha256` et empreinte de la configuration) ; faute → arrêt (R11)."""
    sortie = {}
    for k in CLES:
        chemin = Path(racine) / d[k]["chemin"]
        if not chemin.is_file():
            raise GardeArret(f"donnees_p3.{k} : {chemin} absent")
        sha = verifier(chemin)
        if sha != d[k]["sha256"]:
            raise GardeArret(f"donnees_p3.{k} : empreinte {sha[:12]}… ≠ configuration {d[k]['sha256'][:12]}… (R11)")
        sortie[k] = {"chemin": d[k]["chemin"], "sha256": sha}
    return sortie


def exemples_p3(racine: Path, d: dict) -> dict:
    """Textes, étiquettes et découpage de P3 pour la tromperie et les enjeux (docstring du module)."""
    racine = Path(racine)
    m = json.loads((racine / d["manifeste_p3"]["chemin"]).read_text(encoding="utf-8"))
    r = json.loads((racine / d["sondes_figees_p3"]["chemin"]).read_text(encoding="utf-8"))["resultat"]
    cfg, g = m["config"], m["graines"]
    part = float(cfg["part_entrainement"])
    faits = dn.charger_faits(racine / d["faits"]["chemin"], d["faits"]["sha256"])
    if cfg.get("n_faits_max") is not None:
        faits = faits[:int(cfg["n_faits_max"])]
    exclus = set(r["donnees"]["faits_exclus"])
    ex_t = [x for x in dn.exemples_tromperie(faits) if x["groupe"] not in exclus]
    if len(ex_t) != int(r["donnees"]["exemples_tromperie"]):
        raise GardeArret(f"données de P3 : {len(ex_t)} exemples de tromperie, {r['donnees']['exemples_tromperie']} écrits par P3 (R11)")
    lignes = dn.charger_enjeux(racine / d["enjeux"]["chemin"], d["enjeux"]["sha256"])
    tir = dn.tirer_enjeux(lignes, generateur(g["tirage-enjeux"]), int(cfg["n_par_classe_enjeux"]))
    if [x["ligne"] for x in tir] != list(r["donnees"]["lignes_enjeux"]):
        raise GardeArret("données de P3 : tirage des enjeux ≠ lignes écrites par P3 (R11)")
    sortie = {}
    for concept, ex, texte in (("tromperie", ex_t, "reponse"), ("enjeux", tir, "texte")):
        e, v = dn.decouper([x["groupe"] for x in ex], generateur(g[f"decoupage-{concept}"]), part)
        attendu = r["effectifs"][concept]
        if (len(e), len(v)) != (int(attendu["entrainement"]), int(attendu["validation"])):
            raise GardeArret(f"données de P3 : découpage de {concept} {len(e)}/{len(v)} ≠ effectifs de P3 "
                             f"{attendu['entrainement']}/{attendu['validation']} (R11)")
        sortie[concept] = {"textes": [x[texte] for x in ex], "y": np.array([int(x["y"]) for x in ex], dtype=np.int64),
                           "e": e, "v": v, "empan": "fait (réponse imposée)" if concept == "tromperie" else "texte de l'utilisateur"}
    return sortie


def temoins_p3(racine: Path, d: dict) -> dict:
    """Témoin lexical de la tromperie et des enjeux sur les données et le découpage de P3 (T7-P10)."""
    sortie = {}
    for concept, x in exemples_p3(racine, d).items():
        lisible = lambda i: bool(MOTIF_MOT.search(x["textes"][i]))
        e, v = [i for i in x["e"] if lisible(i)], [i for i in x["v"] if lisible(i)]
        exclus = {"entrainement": len(x["e"]) - len(e), "validation": len(x["v"]) - len(v)}
        tx_e, y_e = [x["textes"][i] for i in e], x["y"][e]
        tx_v, y_v = [x["textes"][i] for i in v], x["y"][v]
        aires, temoins = {}, {}
        for p in PENALITES_LEXICALES:
            t = temoin_lexical(f"lexical-{concept}", tx_e, y_e, p)
            temoins[p], aires[p] = t, aire_sous_courbe(t.scores(tx_v), y_v)
        meilleure = max(aires.values())
        p = next(q for q in PENALITES_LEXICALES if aires[q] == meilleure)
        sortie[concept] = {"temoin": temoins[p], "penalite": p, "aires_validation": {str(k): v for k, v in aires.items()},
                           "empan": x["empan"], "empreinte": temoins[p].empreinte(), "source": "données et découpage de P3",
                           "n_entrainement": len(e), "n_validation": len(v),
                           "textes_sans_mot_exclus": exclus}
    return sortie


__all__ = ["exiger_config", "controler", "exemples_p3", "temoins_p3", "CLES", "CHEMINS_REELS", "SHA_REELLES"]
