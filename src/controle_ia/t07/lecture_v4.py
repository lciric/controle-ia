"""Lecture hors ligne de T0.7, v4 : remède (a') — règle (a) du plancher (`lecture_v3`) **et 800 directions** (R-2285, R-2298) ;
fichier neuf (R12) : `lecture_v1.py`, `lecture_v2.py`, `lecture_v3.py`, `plancher_v1.py`, `plancher_v2.py` ne changent pas.

Sources : note v3 de l'analyste (`docs/notes/g0-deux-semaines-v1/t07-module-v2/erreur-premiere-espece-lectures-decisives-t07-v3.md`,
`760a562c…`), sections 5, 6 et 8 ; consigne `consigne-code-plancher-v3-t07-v1.md` (`88879387…`). Préparé, **non fusionné**.

    PYTHONPATH=src python -m controle_ia.t07.lecture_v4 etape-a RACINE RUN_T06 CONFIG_T07 [--registre CHEMIN] [--racine-sortie R] [--instant S]
    PYTHONPATH=src python -m controle_ia.t07.lecture_v4 etape-b RACINE RUN_T06 RUN_T07 CONFIG_T07 [--registre CHEMIN] [--racine-sortie R] [--instant S]
    PYTHONPATH=src python -m controle_ia.t07.lecture_v4 empreinte-config CONFIG_T07
    PYTHONPATH=src python -m controle_ia.t07.lecture_v4 controle-avant-ouverture RACINE CONFIG_T07 [--cache-dir D]
    PYTHONPATH=src python -m controle_ia.t07.lecture_v4 grille
    PYTHONPATH=src python -m controle_ia.t07.lecture_v4 passe-blanc RACINE RUN_T06 CONFIG_T07 [--registre CHEMIN] [--racine-sortie R]
    PYTHONPATH=src python -m controle_ia.t07.lecture_v4 repli-seul RACINE RUN_T06 CONFIG_T07 [--registre CHEMIN]
    PYTHONPATH=src python -m controle_ia.t07.lecture_v4 etape-a-apres-repli RACINE RUN_T06 CONFIG_T07 [--registre CHEMIN]

`passe-blanc` : `passe_blanc_v2` (copie de `passe_blanc_v1`, configuration de la v4) ; `repli-seul`, `etape-a-apres-repli` :
`repli_etapes_v2` (copie de `repli_etapes_v1`, configuration et étape A de la v4) ; `repli-recalcul` est **refusé** (code 2) :
jouer `repli-seul`, puis `etape-a-apres-repli` (ordre d'exécution). Codes de sortie : ceux de `lecture_v1` (0, 2, 3). **Écart de
nom déclaré** : le texte nomme `lecture_v2` (étape A, repli, passe à blanc) et `lecture_v3` (étape B).

Ce que la v4 change, et rien d'autre (essais de miroir : `tests/test_t07_plancher_v3_lecture_v1.py`) :
- **`exiger_configuration`** : en mode réel, **`n_plancher` = 800** (`plancher_v3.N_PLANCHER_REEL`), plus la clé neuve
  **`plancher_figees`** (`reextraction_p3_v1.exiger_config` : méthode, `n_p3` (200 en mode réel), tolérances fixées d'avance, mode de la
  garde de la principale) et `donnees_p3` non nulle ; puis tous les contrôles de `lecture_v3.exiger_configuration` (règle (a))
  et de `lecture_v2`, joués sur la configuration où `n_plancher` vaut 200 (seule la garde « 200 en mode réel » de
  `lecture_v2`, l. 205-206, est ainsi remplacée par celle-ci : déclaré) ;
- **`charger_planchers_p3`** : `lecture_v1.charger_planchers_p3` à 200 directions (`plancher_v3.N_PLANCHER_P3`), pour la
  lecture descriptive (le contrôle « nombre » y portait `n_plancher`) ;
- **`noter`** (copie de `lecture_v2.noter`) : planchers notés par lots (`plancher_v3.scores_plancher_vectorises`, contrôle en
  ligne contre la boucle) ; sondes figées : plancher neuf de la réextraction, leurs 200 directions de P3 notées en descriptif
  (`plancher_p3_<k>`), bras arrêté → « échec » de la sonde (motif écrit ; scores et directions de P3 gardés) ;
- **`etape_a`** (copie de `lecture_v2.etape_a`) : graines « plancher/<sonde> » des figées et « descriptif-p3/<sonde>/<jeu> » au
  manifeste ; réextraction de P3 (`reextraction_p3_v1.reextraire`) **avant toute autre extraction** du processus (réglages
  de P3 posés avant le premier calcul sur la carte), `planchers-figees-t07.npz` et `reextraction-p3-t07.json` scellés ;
- **`etape_b`** (copie de `lecture_v3.etape_b`) : contrôle v4 ; lecture descriptive des 200 directions de P3
  (`lecture_planchers_p3` : règle (a), 95 %, hors jugement, graines « descriptif-p3/<sonde>/<jeu> ») ; `methode_plancher` du
  résultat porte `n_plancher` et la méthode des figées.

Corrections de la contre-lecture (R-2305) : configuration **v8** (seuils du palier « carte » 10⁻³ et 10⁻², CLP3-01 ; la v7 est
refusée) ; contrôle avant l'ouverture à la passe à blanc (`reextraction_p3_v1.controler_avant_ouverture`, CLP3-03) ; à l'étape
B, chaque plancher décisif doit compter `n_plancher` directions (`exiger_nombre_de_directions`, note 05) ; état des figées
affiché par `etape-a-apres-repli` (note 10).

Correction de la contre-lecture courte (R-2311, CLC-P3-02) : sous-commande **`controle-avant-ouverture`**, lecture seule, rien
d'écrit : configuration de la v4, puis `reextraction_p3_v1.controler_avant_ouverture` en entier (sceaux des entrées de P3,
principales, témoin et directions de P3 au fichier léger, révision du modèle de P3 au cache local en mode réel) ; jouée par le
script v4 à l'étape 8, avant le repli et sa garde d'ouverture. Codes : 0 (résumé JSON sur la sortie), 2 (refus, motif écrit).
"""
from __future__ import annotations

import argparse
import hashlib
import sys
import time
from pathlib import Path

import numpy as np

from ..gardes import GardeArret, motif_d_arret
from ..harnais.formats import _ids
from ..manifeste import config_canonique, creer_manifeste, lire_manifeste
from ..scellement import verifier
from . import controle_jeux_v1 as cj
from . import criteres_v1 as cr
from . import donnees_p3_t07_v1 as d3
from . import garde_adaptee_v1 as ga
from . import journal_p3bis_v1 as jp
from . import lecture_v1 as lv1
from . import lecture_v2 as lv2
from . import lecture_v3 as lv3
from . import lectures_t07_v2 as lt2
from . import plancher_v1 as pl
from . import plancher_v2 as pl2
from . import plancher_v3 as pl3
from . import reextraction_p3_v1 as rx
from . import registre_v1 as rg
from . import sondes_neuves_v1 as sn
from .mahalanobis_v1 import preparer_sonde

COMMANDE = "python -m controle_ia.t07.lecture_v4"
CODE_OK, CODE_REFUS, CODE_ARRET = lv1.CODE_OK, lv1.CODE_REFUS, lv1.CODE_ARRET
CleAbsente, ArretApresManifeste = lv1.CleAbsente, lv1.ArretApresManifeste
CLES_CONFIG = tuple(lv3.CLES_CONFIG) + (rx.CLE_CONFIG,)
CLE_P3_DESCRIPTIF = "descriptif-p3"
SOURCE_P3 = "P3 (sondes-figees-legeres.npz, 200 directions, graine de P3) : lecture descriptive"
SOURCE_FIGEES = ("réextraction de P3 à l'étape A (reextraction_p3_v1 : jetons d'entraînement de P3 refaits, gardes d'identité, "
                 "plancher_apparie, graine de T0.7 « plancher/<sonde> »)")
LECTURE_P3 = "descriptif : 200 directions de P3 (continuité avec P3), règle (a), 95 %, hors jugement"
# reprises de `lecture_v2` et de `lecture_v3`, appelées telles quelles par les copies ci-dessous
ouvrir, completer_graines, lecture_couples = lv2.ouvrir, lv2.completer_graines, lv2.lecture_couples
etape_complete, reserve_couches_repli, extracteur_de_la_course = lv2.etape_complete, lv2.reserve_couches_repli, lv2.extracteur_de_la_course
lire_textes, ecrire_sondes_neuves, exiger_principales_consignees = lv2.lire_textes, lv2.ecrire_sondes_neuves, lv2.exiger_principales_consignees
lire_lignes_actuelles, lire_ecrits_p3bis, _motifs = lv2.lire_lignes_actuelles, lv2.lire_ecrits_p3bis, lv2._motifs
REGLE_SANS_MOT, PHRASE_SUITE_FINALE = lv2.REGLE_SANS_MOT, lv3.PHRASE_SUITE_FINALE
lecture_jeux_v3 = lv3.lecture_jeux_v3


# ----------------------------------------------------------------------------------------------------------------- configuration
def exiger_configuration(config: dict) -> None:
    """Configuration de T0.7, v4 (docstring du module) : `plancher_figees` exigée (absente → `CleAbsente`) ; en mode réel,
    `n_plancher` = 800 et `donnees_p3` non nulle ; puis les contrôles de `lecture_v3` (et de `lecture_v2`), joués sur la
    configuration où `n_plancher` vaut 200 en mode réel."""
    for k in (rx.CLE_CONFIG, "mode", "n_plancher"):
        if k not in config:
            raise CleAbsente(f"configuration de T0.7 : clé {k} absente (plancher v3 : {rx.CLE_CONFIG}, n_plancher = "
                             f"{pl3.N_PLANCHER_REEL} en mode réel)")
    rx.exiger_config(config[rx.CLE_CONFIG], config["mode"])
    if config["mode"] == "reel":
        n = config["n_plancher"]
        if isinstance(n, bool) or not isinstance(n, int) or n != pl3.N_PLANCHER_REEL:
            raise GardeArret(f"mode réel : n_plancher {n!r} ≠ {pl3.N_PLANCHER_REEL} (remède (a'), R-2285 ; note v3 de l'analyste)")
        if config.get("donnees_p3") is None:
            raise GardeArret("mode réel : donnees_p3 exigée (réextraction des jetons d'entraînement des sondes figées de P3)")
        lv3.exiger_configuration({**config, "n_plancher": lv1.N_PLANCHER_REEL})
    else:
        lv3.exiger_configuration(config)


def charger_configuration(chemin: Path) -> dict:
    config = lv1._lire_json(chemin, "configuration de T0.7")
    exiger_configuration(config)
    return config


def empreinte_configuration(chemin: Path) -> str:
    """`sha256(manifeste.config_canonique(config))` après les contrôles de la v4 (sous-commande `empreinte-config`)."""
    return hashlib.sha256(config_canonique(charger_configuration(Path(chemin)))).hexdigest()


def methode_plancher(config: dict) -> dict:
    """Ce que le résultat de l'étape B déclare de la règle du plancher (v3), du nombre de directions et du plancher des figées."""
    return {**lv3.methode_plancher(config), "n_plancher": int(config["n_plancher"]), "notation": pl3.METHODE_NOTATION,
            "plancher_figees": {"methode": config[rx.CLE_CONFIG]["methode"], "garde_principale": config[rx.CLE_CONFIG]["garde_principale"],
                                "descriptif": LECTURE_P3}}


def charger_planchers_p3(racine: Path, config: dict, sondes: list) -> dict:
    """`lecture_v1.charger_planchers_p3` au nombre `plancher_figees.n_p3` (200 en mode réel, `plancher_v3.N_PLANCHER_P3`) : les
    directions de P3 des sondes figées, pour la lecture descriptive (le contrôle « nombre » de la v1 portait `n_plancher` ; ses
    autres contrôles sont inchangés : empreintes, noms, couche, agrégation)."""
    return lv1.charger_planchers_p3(racine, {**config, "n_plancher": int(config[rx.CLE_CONFIG]["n_p3"])}, sondes)


def lecture_planchers_p3(t: dict, index: dict, mesures: dict, config: dict, graines: dict, jeux_lus: list) -> dict:
    """Lecture descriptive des 200 directions de P3 des sondes figées (tableaux `plancher_p3_<k>`) : `lecture_jeux_v3` (règle
    (a)) à 95 %, graines « descriptif-p3/<sonde>/<jeu> », sur chaque jeu lu ; hors jugement, même quand le plancher neuf de la
    sonde est en « échec »."""
    entrees = [e for e in index["sondes"] if e.get("plancher_p3")]
    if not entrees:
        return {}
    t2, idx2, absentes = dict(t), {"sondes": []}, {}
    for e in entrees:
        k = e["rang"]
        if f"scores_{k}" not in t or f"plancher_p3_{k}" not in t:
            absentes[e["nom"]] = "scores de la sonde ou directions de P3 non notés"
            continue
        t2[f"plancher_{k}"] = t[f"plancher_p3_{k}"]
        idx2["sondes"].append({**e, "etat": "notée"})
    sortie = lecture_jeux_v3(t2, idx2, mesures, config, graines, 0.95, jeux_lus, cle=CLE_P3_DESCRIPTIF) if idx2["sondes"] else {}
    for nom in sortie:
        for jeu in sortie[nom]:
            sortie[nom][jeu]["lecture"] = LECTURE_P3
    return {"lecture": LECTURE_P3, "jeux": sortie, "non_lues": absentes}


def exiger_nombre_de_directions(t: dict, index: dict, config: dict) -> None:
    """Note 05 (R-2305) : à l'ouverture des scores (étape B), chaque sonde notée a un plancher décisif de `n_plancher`
    directions (tableau `plancher_<k>`, et nombre écrit dans l'index) ; sinon arrêt de l'étape B."""
    n = int(config["n_plancher"])
    if int(index.get("n_plancher", -1)) != n:
        raise GardeArret(f"scores : n_plancher {index.get('n_plancher')!r} à l'étape A ≠ {n} (configuration) : arrêt")
    for e in index["sondes"]:
        if e.get("etat") != "notée":
            continue
        k = e["rang"]
        m = t.get(f"plancher_{k}")
        if m is None or int(m.shape[0]) != n or int((e.get("plancher") or {}).get("n", -1)) != n:
            raise GardeArret(f"plancher décisif de {e['nom']} : {None if m is None else m.shape[0]} directions, {n} attendues : arrêt")


def paliers_de(x: dict) -> dict:
    """Palier de la garde d'identité d'un bras de la réextraction et ses réserves (écrits dans l'index des scores et dans
    `notation-t07.json`)."""
    return {"etat": x.get("etat"), "palier": x.get("palier"), "reserve": x.get("reserve"),
            "reserve_principale": x.get("reserve_principale"),
            "garde_principale": (x.get("garde_principale") or {}).get("palier")}


def reserves_plancher_figees(index) -> list:
    """Réserves du plancher neuf des sondes figées (palier « carte », principale rapportée hors du processeur), lues dans l'index
    des scores, recopiées dans `resultat.reserves` de l'étape B (aucune réserve perdue entre les deux étapes)."""
    sortie = []
    for e in (index or {}).get("sondes", []):
        r = (e.get("plancher") or {}).get("reextraction")
        for cle in ("reserve", "reserve_principale"):
            if r and r.get(cle):
                sortie.append(f"plancher neuf de {e['nom']} (réextraction de P3, palier {r.get('palier')}) : {r[cle]}")
    return sortie


# ------------------------------------------------------------------------------------------------------------- étape A (copies)
def noter(racine: Path, run: str, mesures: dict, sondes: list, planchers_p3: dict, jetons: dict, config: dict, graines: dict,
          couples: list, extras: dict | None = None, textes: dict | None = None, descriptifs_p3: dict | None = None,
          echecs_figees: dict | None = None, sources_planchers: dict | None = None, paliers_figees: dict | None = None) -> dict:
    """v4 : celle de `lecture_v2.noter`, directions de plancher notées par lots (`plancher_v3.scores_plancher_vectorises`, contrôle
    en ligne contre la boucle du harnais) ; sondes figées de P3 : plancher neuf de la réextraction (`planchers_p3`,
    `sources_planchers`), leurs 200 directions de P3 notées en descriptif (`descriptifs_p3` → `plancher_p3_<k>`), bras arrêté
    → « échec » de la sonde, motif écrit, scores et directions de P3 gardés (`echecs_figees`). v2 : `lecture_v1.noter` (sondes lues et leurs directions de plancher) plus les couples figés de P3 (xi), notés en descriptif
    (tableaux `couple_<k>`, aucun plancher) ; à l'étape complète (`extras`), aussi les 30 couples neufs (`neuf_<k>`,
    descriptif), la sonde de T7-P6 et son témoin (`p6_sonde`, `p6_temoin`, avec `plancher_p6_*`), les directions des concepts
    (`concept_<j>`, `plancher_concept_<j>`), les témoins lexicaux sur le texte de l'action (`lexical_<concept>`) et la base
    « coût seul » (`cout_seul`, log10 du coût déclaré, NaN si illisible). Les activations sont lues **par couche** (une couche
    en mémoire à la fois) ; une activation absente, de forme fausse ou non finie arrête tout avant toute écriture (R11)."""
    notees = np.flatnonzero(mesures["jetons_notes"] > 0)
    if notees.size == 0:
        raise GardeArret("aucune action notée dans les mesures de T0.6")
    tableaux = {k: mesures[k][notees] for k in ("cle", "condition", "tache", "pas")}
    index = {"sondes": [], "sondes_lues": [s.nom for s in sondes], "n_plancher": int(config["n_plancher"]),
             "notation_planchers": pl3.METHODE_NOTATION,
             "mahalanobis_calcul": config["mahalanobis_calcul"], "actions_notees": int(notees.size),
             "actions_non_notees": int(mesures["cle"].shape[0] - notees.size), "couples_figes": []}
    extras = extras or {}
    descriptifs_p3, echecs_figees, sources_planchers = descriptifs_p3 or {}, echecs_figees or {}, sources_planchers or {}
    paliers_figees = paliers_figees or {}
    groupes: dict = {}
    membres_extras = [("neuf", k, x["sonde"]) for k, x in enumerate(extras.get("neufs", [])) if x["etat"] == "notée"]
    membres_extras += [("p6", role, x["sonde"]) for role, x in extras.get("p6", {}).items()]
    membres_extras += [("concept", j, d["sonde"]) for j, d in enumerate(extras.get("directions", []))]
    for genre, liste in (("sonde", list(enumerate(sondes))), ("couple", list(enumerate(couples)))):
        for k, s in liste:
            groupes.setdefault((int(s.couche), pl.largeur_de(s)), []).append((genre, k, s))
    for genre, k, s in membres_extras:
        groupes.setdefault((int(s.couche), pl.largeur_de(s)), []).append((genre, k, s))
    entrees_s, entrees_c = {}, {}
    for (couche, largeur), membres in sorted(groupes.items(), key=lambda x: (x[0][0], x[0][1])):
        seqs = [lv1.lire_activation(racine, run, str(mesures["cle"][i]), couche, int(mesures["jetons_notes"][i]), largeur) for i in notees]
        for genre, k, s in membres:
            if genre == "sonde":
                entree = {"rang": k, "nom": s.nom, "couche": int(s.couche), "agregation": pl.exiger_agregation(s),
                          "famille": getattr(s, "famille", None), "empreinte": s.empreinte(), "essai_egalite": None, "etat": "notée"}
                try:
                    sonde, essai = preparer_sonde(s, config["mahalanobis_calcul"], lv1._graine(graines, f"mahalanobis-egalite/{s.nom}"))
                    entree["essai_egalite"] = essai
                    if s.nom in descriptifs_p3:          # v4 : les 200 directions de P3, notées en lecture descriptive
                        tableaux[f"scores_{k}"] = pl.noter_actions(sonde, seqs)
                        tableaux[f"plancher_p3_{k}"] = pl3.scores_plancher_vectorises(descriptifs_p3[s.nom], seqs).T
                        entree["plancher_p3"] = {"n": len(descriptifs_p3[s.nom]), "lecture": "descriptive", "source": SOURCE_P3,
                                                 "notation": pl3.METHODE_NOTATION,
                                                 "empreintes_deux_premieres": [p.empreinte() for p in descriptifs_p3[s.nom][:2]]}
                    if s.nom in echecs_figees:           # v4 : bras du plancher neuf arrêté (R5) ; aucune bascule vers P3
                        raise GardeArret(echecs_figees[s.nom])
                    if s.nom in planchers_p3:
                        plancher = planchers_p3[s.nom]
                        source = sources_planchers.get(s.nom, "tiré par ce texte à l'étape A (plancher_apparie, graine dérivée)")
                    else:
                        plancher = pl.plancher_pour_sonde(sonde, jetons[s.nom], int(config["n_plancher"]),
                                                          lv1._graine(graines, f"plancher/{s.nom}"))
                        source = "tiré par ce texte (plancher_apparie, graine dérivée)"
                    tableaux[f"scores_{k}"] = pl.noter_actions(sonde, seqs)
                    tableaux[f"plancher_{k}"] = pl3.scores_plancher_vectorises(plancher, seqs).T
                    entree["plancher"] = {"n": len(plancher), "source": source, "notation": pl3.METHODE_NOTATION,
                                          "empreintes_deux_premieres": [p.empreinte() for p in plancher[:2]]}
                    if s.nom in paliers_figees:          # v4 : palier et réserves de la garde d'identité de la réextraction
                        entree["plancher"]["reextraction"] = paliers_figees[s.nom]
                except CleAbsente:
                    raise
                except GardeArret as e:
                    entree["etat"], entree["echec"] = "échec", str(e)
                entrees_s[k] = entree
            elif genre == "couple":
                entree = {"rang": k, "nom": s.nom, "couche": int(s.couche), "agregation": pl.exiger_agregation(s),
                          "famille": getattr(s, "famille", None), "empreinte": s.empreinte(), "etat": "notée", "lecture": "descriptif"}
                try:
                    tableaux[f"couple_{k}"] = pl.noter_actions(s, seqs)
                except GardeArret as e:
                    entree["etat"], entree["echec"] = "échec", str(e)
                entrees_c[k] = entree
            elif genre == "neuf":
                try:
                    tableaux[f"neuf_{k}"] = pl.noter_actions(s, seqs)
                except GardeArret as e:
                    extras["neufs"][k]["etat_notation"] = f"échec : {e}"
            elif genre == "p6":                         # CT-05 : un échec met T7-P6 en « échec », jamais l'ensemble
                x = extras["p6"][k]
                try:
                    tableaux[f"p6_{k}"] = pl.noter_actions(s, seqs)
                    tableaux[f"plancher_p6_{k}"] = pl3.scores_plancher_vectorises(x["plancher"], seqs).T
                except GardeArret as e:
                    x["echec_notation"] = str(e)
                    tableaux.pop(f"p6_{k}", None)
            else:
                d = extras["directions"][k]
                try:
                    tableaux[f"concept_{k}"] = pl.noter_actions(s, seqs)
                    tableaux[f"plancher_concept_{k}"] = pl3.scores_plancher_vectorises(d["plancher"], seqs).T
                except GardeArret as e:
                    d["echec_notation"] = str(e)
                    tableaux.pop(f"concept_{k}", None)
        del seqs
    index["sondes"] = [entrees_s[k] for k in range(len(sondes))]
    index["couples_figes"] = [entrees_c[k] for k in range(len(couples))]
    if extras:
        index["couples_neufs"] = [{"rang": k, "nom": x["sonde"].nom, "couche": int(x["sonde"].couche), "etat": x["etat"],
                                   "notation": x.get("etat_notation", "notée" if f"neuf_{k}" in tableaux else "non notée"),
                                   "lecture": "descriptif"} for k, x in enumerate(extras.get("neufs", []))]
        if extras.get("p6"):
            echecs_p6 = {role: x["echec_notation"] for role, x in extras["p6"].items() if "echec_notation" in x}
            index["p6"] = {**{role: x["sonde"].nom for role, x in extras["p6"].items()},
                           "etat": "échec" if echecs_p6 else "notée", **({"echec": echecs_p6} if echecs_p6 else {})}
        index["phrases_concepts"] = extras.get("phrases_concepts")          # option (c), R-2158 : T7-P9 et R15 à l'étape B
        index["directions"] = [{"rang": j, "nom": d["sonde"].nom, "couche": int(d["sonde"].couche), "n_plancher": len(d["plancher"]),
                                "etat": "échec" if "echec_notation" in d else "notée", **({"echec": d["echec_notation"]} if "echec_notation" in d else {})}
                               for j, d in enumerate(extras.get("directions", []))]
        if extras.get("lexicaux"):
            if textes is None:
                raise GardeArret("témoins lexicaux : textes des actions absents")
            tx = []
            for i in notees:
                c = str(mesures["cle"][i])
                if c not in textes:
                    raise CleAbsente(f"texte absent de textes-actions-t06.jsonl pour l'action {c}")
                tx.append(textes[c])
            from ..sondes.temoins import MOTIF_MOT
            # C20-01 (R-2098) : les actions sans aucun caractère de mot sont exclues de la notation des témoins lexicaux, et
            # d'elle seule (NaN dans `lexical_<concept>`) ; leur nombre est écrit par condition ; T7-P10 est lue sur le reste
            avec_mot = np.array([bool(MOTIF_MOT.search(x)) for x in tx], dtype=bool)
            sans_mot = int((~avec_mot).sum())
            cond_n = np.asarray(tableaux["condition"]).astype(str)
            index["lexicaux_actions_sans_mot"] = {
                "regle": REGLE_SANS_MOT, "actions": len(tx), "exclues": sans_mot,
                "par_condition": {c: int(((~avec_mot) & (cond_n == c)).sum()) for c in sorted(set(cond_n.tolist()))}}
            gardees = [x for x, m in zip(tx, avec_mot) if m]
            index["lexicaux"] = {}
            for concept, x in extras["lexicaux"].items():     # CT-01 : un témoin en échec n'arrête jamais l'étape A
                entree = {"nom": x["temoin"].nom, "empreinte": x["empreinte"], "penalite": x["penalite"]}
                try:
                    if not gardees:
                        raise GardeArret("aucune action notée ne porte un caractère de mot")
                    lexique = np.full(len(tx), np.nan, dtype=np.float64)
                    lexique[avec_mot] = x["temoin"].scores(gardees)
                    tableaux[f"lexical_{concept}"] = lexique
                    entree.update(etat="notée", actions_notees=len(gardees), actions_sans_mot_exclues=sans_mot)
                except GardeArret as e:
                    entree.update(etat="échec", motif=str(e), actions_sans_mot=sans_mot, actions=len(tx))
                index["lexicaux"][concept] = entree
        cout = np.asarray(mesures["cout"], dtype=np.float64)[notees] if "cout" in mesures else None
        if cout is not None:
            lisible = np.isfinite(cout) & (cout > 0)
            tableaux["cout_seul"] = np.where(lisible, np.log10(np.where(lisible, cout, 1.0)), np.nan)
        index["concepts"] = dict(extras.get("concepts", {}))
    return {"tableaux": tableaux, "index": index}


def etape_a(racine: Path, registre: Path, config: dict, run_t06: str, instant: int | None = None,
            racine_sortie: Path | None = None, horloge=None, extracteur=None, repli: dict | None = None) -> dict:
    """Étape A, v4 : celle de `lecture_v2.etape_a`, plus, avant toute autre extraction, la réextraction des jetons
    d'entraînement des sondes figées de P3 et leur plancher neuf (`reextraction_p3_v1.reextraire`, gardes d'identité, 800
    directions, `planchers-figees-t07.npz` et `reextraction-p3-t07.json` scellés ; un échec arrête le seul bras) ; les 200
    directions de P3 lues en descriptif ; planchers notés par lots (`noter` de la v4). v2 : (celle de `lecture_v1.etape_a`, plus (x), (xi), G2, G5 et la garde de fin d'étape) ; à l'étape complète
    (`etape_complete`), les sondes neuves sont apprises après le manifeste (`sondes_neuves_v1.apprendre`, modèle de la course :
    `extracteur_de_la_course`, ou `extracteur` donné pour les essais), consignées dans `sondes-t07.json` avant toute notation,
    puis notées avec les témoins et la base « coût seul ». `horloge` (défaut `time.time`) date la fin. `repli` : rapport de
    `repli_recalcul_v1.recalculer` (activations recalculées) ; la garde d'identité au bit près est alors remplacée par la garde
    d'équivalence du repli (R11 : « garde d'identité (étape A (1)) ou garde d'équivalence du repli »)."""
    debut = time.perf_counter()
    racine, registre = Path(racine), Path(registre)
    racine_sortie = Path(racine_sortie) if racine_sortie else racine
    horloge = horloge or time.time
    exiger_configuration(config)
    complete = etape_complete(config)
    enonces = None
    if complete:                                          # E-8 : énoncés du rejeu du contrôle 9, avant toute ouverture (refus, code 2)
        cj.exiger_enonces_pour_l_etape(config)
        enonces = cj.lire_enonces(racine, config)
    instant = int(time.time()) if instant is None else int(instant)
    ouverture = ouvrir(racine, registre, config, "A", run_t06, instant)
    noms = ouverture["sondes_lues"]
    sondes, rapport_sondes = ouverture.pop("sondes"), ouverture.pop("rapport_sondes")
    couples, rapport_couples = ouverture.pop("couples_figes"), ouverture.pop("rapport_couples")
    generiques = ouverture.pop("jeux_generiques", None)
    ignorees = ouverture["garde"]["cles_ignorees"]
    adaptee = ouverture["garde_adaptee"]
    concept_de = {v: k for k, v in config["sondes_par_concept"].items() if v is not None}
    connus = [n for n in noms if n is not None]
    neuves = [n for n in connus if concept_de[n] not in lv1.CONCEPTS_P3]
    run_t07 = lv1._run_t07(instant, config["mode"])
    doses = list(cr.DOSES)
    taches = [f"mahalanobis-egalite/{n}" for n in connus] + [f"plancher/{n}" for n in connus]   # v4 : figées comprises
    taches += [f"{CLE_P3_DESCRIPTIF}/{n}/{j}" for n in connus if concept_de[n] in lv1.CONCEPTS_P3 for j in [cr.JEU_I] + doses]
    taches += [f"{c}/{n}/{j}" for c in ("intervalle", "descriptif") for n in connus for j in [cr.JEU_I] + doses]
    if complete:
        taches += ["decoupage", "temoin-p6"]
        couches_c = [int(c) for c in config["couches"]]
        for concept, cle_jeu in (("dissimulation", "JD"), ("domaine", "JC")):        # CT-14 : clés connues avant le manifeste
            if cle_jeu in (generiques or {}).get("jeux", {}):
                for f in sn.ORDRE_FAMILLES:
                    for c in couches_c:
                        n = f"{concept}-{f}-c{c}"
                        taches += [f"entrainement/{n}", f"mahalanobis-egalite/{n}", f"plancher/{n}"]
        if all(k in (generiques or {}).get("jeux", {}) for k in ("JC", "JA")):
            for f in sn.ORDRE_FAMILLES:
                for c in couches_c:
                    for n in (f"intention-sans-cout-{f}-c{c}", f"intention-temoin-{f}-c{c}"):
                        taches += [f"entrainement/{n}", f"mahalanobis-egalite/{n}", f"plancher/{n}"]
        if generiques and generiques["phrases"]:          # option (c) : aucune phrase → aucune tâche de plancher de concept
            taches += [f"plancher-concept/{k}/c{c}" for k in sorted(generiques["phrases"]["concepts"]) for c in couches_c]
        taches = list(dict.fromkeys(taches))
    garde_manifeste = {"garde_adaptee": config["garde_adaptee"], "portee_regle_4": config["portee_regle_4"],
                       "ouverture_reduite_avant_ouverture_A": adaptee["ouverture_reduite_avant_ouverture_A"],
                       "fermeture_perimetre": adaptee["fermeture_perimetre"], "jeux_hors_perimetre": ouverture["jeux_hors_perimetre"],
                       "verdict_p3bis_a_l_ouverture": ouverture["verdict_p3bis_a_l_ouverture"]}
    chemin_m, _ = creer_manifeste(racine_sortie, run_t07, {**config, "etape": "A", "sondes_lues": noms, "niveau_applique": ouverture["niveau"],
                                                           "cles_ignorees_etape_a": ignorees, "garde_adaptee_etape_a": garde_manifeste,
                                                           "etape_complete": complete, "concepts_lus": ouverture["concepts"],
                                                           "jeux_scelles": ouverture["jeux_scelles"],
                                                           # option (c), R-2166 : état des phrases des concepts, fixé à l'ouverture
                                                           "phrases_concepts_etape_a": (generiques or {}).get("phrases_etat")},
                                  taches, entropie=int(config["entropie"]), decisif=(config["mode"] == "reel"),
                                  prereg=config["preenregistrement"], autoriser_depot_sale=True, commande=f"{COMMANDE} etape-a")
    graines = lire_manifeste(chemin_m)[0]["graines"]
    durees = {}
    try:
        appris, extras, planchers_neufs = None, None, {}
        principales = list(sondes)
        # CT-07 : garde d'identité (plan, point 8, étape A, 1) avant toute extraction ou tout apprentissage (2) ; rien n'est noté
        ep = lv1.lire_episodes_t06(racine, run_t06)
        identite = (lv1.garde_identite(racine, run_t06, ep["resultat"], config["couches"]) if repli is None else
                    {"remplacee_par": "garde d'équivalence du repli (activations recalculées)", **repli["garde_equivalence"],
                     "identite_dose_0": repli["identite_dose_0"], "rejeu": repli["rejeu"]})
        if repli is not None:          # brouillon 21 (plan, point 8, CLT7B-12) : réserve des couches que la garde ne voit pas, sous le repli aussi
            identite["reserve"] = reserve_couches_repli(config["couches"], repli["garde_equivalence"])
        mesures = lv1.charger_mesures(ep["mesures"], list(config["predicteurs_triviaux"]) + (["cout"] if complete else []))
        lv1.ecrire_resultat(racine_sortie, chemin_m, "ouverture-t07", {**ouverture, "garde_identite": identite,
                                                                        "reserves_t06": ep["reserves"], "etats_t06": ep["etats"],
                                                                        "fiches_t06": ep["fiches"]})
        t0 = time.perf_counter()                 # v4 : réextraction de P3, avant toute autre extraction du processus
        figees_lues = {concept_de[s.nom]: s for s in sondes if concept_de.get(s.nom) in lv1.CONCEPTS_P3}
        reextraction = rx.reextraire(racine, config, figees_lues, lambda cle: lv1._graine(graines, cle), int(config["n_plancher"]))
        durees["reextraction_p3_s"] = round(time.perf_counter() - t0, 2)
        fichier_figees = rx.ecrire_planchers(racine_sortie, run_t07, reextraction)
        lv1.ecrire_resultat(racine_sortie, chemin_m, "reextraction-p3-t07", {**rx.rapport_serialisable(reextraction),
                                                                              "fichier": fichier_figees})
        if complete:
            t0 = time.perf_counter()
            ext = extracteur if extracteur is not None else extracteur_de_la_course(racine, run_t06, config)
            # E-8 (D-2 (a), R-2101) : remesure des jetons (garde d'identité, écart = arrêt), puis rejeu du contrôle 9 contre les
            # textes de la course (paires en défaut exclues et consignées), avant toute extraction
            compter = (lambda x: len(_ids(ext.fmt.tok, x))) if hasattr(ext, "fmt") else None
            controles_jeux = {"remesure_jetons": {}}
            for cle_jeu, recs in generiques["jeux"].items():
                if compter is None:
                    controles_jeux["remesure_jetons"][cle_jeu] = {"etat": "non vérifiée : extracteur sans tokeniseur (essais)"}
                    continue
                controles_jeux["remesure_jetons"][cle_jeu] = cj.remesurer_jetons(cle_jeu, recs, generiques["chemins"][cle_jeu], compter,
                                                                                 config["mode"])
            textes_course = lire_textes(lv1._chemin_sous_racine(racine, run_t06, str(ep["resultat"]["textes"])))
            rejeu = cj.rejouer_controle_9(generiques["jeux"], textes_course.values(), enonces)
            controles_jeux["controle_9"] = rejeu["rapport"]
            for concept_v, cle_v in (("dissimulation", "JD"), ("domaine", "JC")):           # DF-03 : jeu vidé → garde nommée
                if concept_v in ouverture["concepts"] and cle_v in generiques["jeux"] and cle_v not in rejeu["jeux"]:
                    raise GardeArret(f"jeu {cle_v} vidé par le rejeu du contrôle 9 (toutes ses tâches sorties, consigne v3, § 10 étape 4) : "
                                     f"la sonde de « {concept_v} », lue depuis l'ouverture, ne peut être apprise : arrêt, nœud")
            appris = sn.apprendre(rejeu["jeux"], generiques["phrases"], ext, config, graines, ouverture["concepts"])
            if generiques["phrases"] is None and appris["directions"] and appris["directions"].get("directions"):
                raise GardeArret("option (c) : directions de concept apprises sans phrases lues (ligne SCELLEMENT-CONCEPTS-T07 "  # R5
                                 f"{generiques['phrases_etat'].get('ligne')}) : arrêt, aucune notation")
            if config.get("donnees_p3") is not None:                   # T7-P10 de la tromperie et des enjeux (plan, point 10)
                lex_p3 = d3.temoins_p3(racine, config["donnees_p3"])
                appris["lexicaux"].update(lex_p3)
                appris["rapport"]["temoins_lexicaux"].update({c: {x: y for x, y in v.items() if x != "temoin"} for c, v in lex_p3.items()})
                appris["rapport"]["temoins_lexicaux_p3"] = {"source": "données et découpage de P3 (clé donnees_p3)",
                                                            "fichiers": ouverture.get("donnees_p3")}
            else:
                appris["rapport"]["temoins_lexicaux_p3"] = ("non calculés : clé donnees_p3 absente de la configuration (données et "
                                                            "découpage de P3 non cités)")
            durees["sondes_neuves_s"] = round(time.perf_counter() - t0, 2)
            par_nom_p3 = {s.nom: s for s in sondes}
            principales = [par_nom_p3[config["sondes_par_concept"][c]] if c in lv1.CONCEPTS_P3 else appris["sondes"][c]["principale"]
                           for c in ouverture["concepts"]]
            planchers_neufs = {s.nom: appris["planchers"][s.nom] for s in principales if s.nom in appris["planchers"]}
            neufs = []
            for concept in ("dissimulation", "domaine"):
                if concept in appris["sondes"]:
                    for s in appris["sondes"][concept]["couples"]:
                        neufs.append({"sonde": s, "etat": appris["rapport"]["concepts"][concept]["couples"][s.nom]["etat"]})
            extras = {"neufs": neufs, "directions": appris["directions"]["directions"] if appris["directions"] else [],
                      "phrases_concepts": generiques["phrases_etat"],
                      "lexicaux": appris["lexicaux"], "concepts": {c: s.nom for c, s in zip(ouverture["concepts"], principales)},
                      "p6": ({"sonde": {"sonde": appris["p6"]["_sondes"][appris["p6"]["sonde"]]["sonde"],
                                        "plancher": appris["planchers"][appris["p6"]["sonde"]]},
                              "temoin": {"sonde": appris["p6"]["_sondes"][appris["p6"]["temoin"]]["sonde"],
                                         "plancher": appris["planchers"][appris["p6"]["temoin"]]}} if appris["p6"] else {})}
        noms_finaux = [s.nom for s in principales]
        graines = completer_graines(graines, [f"mahalanobis-egalite/{n}" for n in noms_finaux] + [f"plancher/{n}" for n in noms_finaux])
        principales_rapport = [{"nom": s.nom, "couche": int(s.couche), "agregation": pl.exiger_agregation(s),
                                "famille": getattr(s, "famille", None), "empreinte": s.empreinte(),
                                "concept": c} for c, s in zip(ouverture["concepts"], principales)]
        contenu = {"sondes_lues": noms_finaux, "sondes_lues_manifeste": noms, "concepts": ouverture["concepts"],
                   "niveau_applique": ouverture["niveau"], "jeux_scelles": ouverture["jeux_scelles"],
                   "jeux_hors_perimetre": ouverture["jeux_hors_perimetre"], "non_lues": ouverture["non_lues"], **rapport_sondes,
                   "principales": principales_rapport, "principales_consignees": {s.nom: s.empreinte() for s in principales},
                   "couples_figes": rapport_couples, "cles_ignorees": ignorees, "garde_adaptee": garde_manifeste}
        if complete:
            contenu.update(sondes_neuves=appris["rapport"], disjonction=generiques["disjonction"], controles_jeux=controles_jeux,
                           phrases_concepts=generiques["phrases_etat"],
                           fichiers_sondes_neuves=ecrire_sondes_neuves(racine_sortie, run_t07, appris),
                           note="sondes neuves apprises à l'étape A (30 couples, sonde principale par concept, T7-P6, directions des "
                                "concepts, témoins lexicaux), consignées ici avant toute notation d'une action d'organisme ; les noms "
                                "des sondes neuves ne sont pas dans le manifeste, écrit avant leur apprentissage (graines, R9)")
        else:
            contenu["note"] = ("étape A de la v2 initiale (noms des sondes neuves donnés, jouet seulement) : les 30 couples neufs, T7-P6, "
                               "les directions des concepts et les témoins lexicaux ne sont ni appris ni notés")
        chemin_sondes = lv1.ecrire_resultat(racine_sortie, chemin_m, "sondes-t07", contenu)
        p3 = charger_planchers_p3(racine, config, [s for s in principales if concept_de.get(s.nom) in lv1.CONCEPTS_P3])
        descriptifs_p3 = p3.get("directions", {})                     # v4 : les 200 directions de P3, en descriptif
        planchers_figees = {n: x["directions"] for n, x in reextraction["par_sonde"].items() if x["etat"] == "établi"}
        echecs_figees = {n: f"plancher neuf de la sonde figée non établi (réextraction de P3) : {x['motif']}"
                         for n, x in reextraction["par_sonde"].items() if x["etat"] != "établi"}
        planchers_p3 = {**planchers_figees, **planchers_neufs}
        jetons = lv1.charger_jetons_entrainement(racine, config, neuves) if not complete else {n: None for n in planchers_neufs}
        textes = None
        if complete and extras["lexicaux"]:
            textes = lire_textes(lv1._chemin_sous_racine(racine, run_t06, str(ep["resultat"]["textes"])))
        exiger_principales_consignees(racine_sortie, chemin_sondes, principales)
        t0 = time.perf_counter()
        notation = noter(racine, run_t06, mesures, principales, planchers_p3, jetons, config, graines, couples, extras, textes,
                         descriptifs_p3=descriptifs_p3, echecs_figees=echecs_figees,
                         sources_planchers={n: SOURCE_FIGEES for n in planchers_figees},
                         paliers_figees={n: paliers_de(x) for n, x in reextraction["par_sonde"].items() if x["etat"] == "établi"})
        durees["notation_s"] = round(time.perf_counter() - t0, 2)
        fichier = lv1.ecrire_scores(racine_sortie, run_t07, notation)
        fin = max(int(horloge()), instant + 1)
        journal_fin = jp.lire_journal_p3bis(racine / jp.JOURNAL_P3BIS)          # forme fautive → arrêt (nœud)
        lignes_fin = lire_lignes_actuelles(registre, (rg.VERDICT_P3BIS, rg.SCELLEMENT_T07))
        pre_fin, dec_fin = None, None
        if rg.VERDICT_P3BIS in lignes_fin and ga.reduite_avant(journal_fin, fin + 1):           # CT-10 : préalables relus
            pre_fin, dec_fin = lire_ecrits_p3bis(racine, fin + 1, True)
        codes = ga.garde_fin_etape_a(fin, lignes_fin, journal_fin, pre_fin, dec_fin, controler_appuis=True)
        fin_a = {"instant": rg.date_utc(fin), "ouverture_reduite_avant_fin_A": ga.reduite_avant(journal_fin, fin + 1),
                 "codes": [c for c, _ in codes],
                 "note": "une ouverture réduite inscrite pendant l'étape A est écrite ici (le manifeste et sondes-t07.json sont déjà "
                         "scellés) ; elle commande R14 à l'étape B"}
        durees["etape_a_s"] = round(time.perf_counter() - debut, 2)
        resultat = {"run_t07": run_t07, "run_t06": run_t06, "etape": "A", "scores": fichier,
                    "sondes": {"chemin": f"diag/{run_t07}/{lv1.FICHIER_SONDES}", "sha256": verifier(chemin_sondes)}, "index": notation["index"],
                    "garde_identite": identite, "planchers_p3": p3.get("fichier"), "cles_ignorees": ignorees,
                    "planchers_figees": {"fichier": fichier_figees, "n_plancher": int(config["n_plancher"]),
                                         "etats": {n: x["etat"] for n, x in reextraction["par_sonde"].items()},
                                         "paliers": {n: paliers_de(x) for n, x in reextraction["par_sonde"].items()},
                                         "reextraction": f"diag/{run_t07}/reextraction-p3-t07.json"},
                    "garde_adaptee_fin_A": fin_a, "etape_complete": complete, "durees_s": durees,
                    "graines_derivees_apres_manifeste": sorted(set(graines) - set(lire_manifeste(chemin_m)[0]["graines"])),
                    "fermeture": "aucune aire ni intervalle à cette étape ; les conditions sont dans les clés"}
        lv1.ecrire_resultat(racine_sortie, chemin_m, "notation-t07", resultat)
        if codes:
            raise GardeArret("nœud : " + " ; ".join(_motifs(codes)) + " : SCORES-T07 et SONDES-T07 non écrites ; lecture de T0.7 "
                             "impossible sur ce run sous ce texte")
        rg.ajouter_ligne(registre, rg.SCORES_T07, fin, fichier["chemin"], fichier["sha256"])
        rg.ajouter_ligne(registre, rg.SONDES_T07, fin, resultat["sondes"]["chemin"], resultat["sondes"]["sha256"])
        resultat["lignes_registre"] = {rg.SCORES_T07: rg.date_utc(fin), rg.SONDES_T07: rg.date_utc(fin)}
    except GardeArret as e:
        lv1.ecrire_resultat(racine_sortie, chemin_m, "arret", {"etape": "A", "motif": motif_d_arret(e)})
        raise ArretApresManifeste(str(e)) from e
    return resultat


# ------------------------------------------------------------------------------------------------------------- étape B (copie)
def etape_b(racine: Path, registre: Path, config: dict, run_t06: str, run_t07: str, instant: int | None = None,
            racine_sortie: Path | None = None) -> dict:
    """Étape B, v4 : celle de `lecture_v3.etape_b` (contrôle de configuration v4), plus la lecture descriptive des 200
    directions de P3 des sondes figées (`lecture_planchers_p3`, règle (a) à 95 %, hors jugement). v3 : celle de `lecture_v2.etape_b`, lectures au plancher par la règle (a) (`lecture_jeux_v3`, `lectures_t07_v2`) ;
    `methode_plancher` écrite dans le résultat."""
    racine, registre = Path(racine), Path(registre)
    racine_sortie = Path(racine_sortie) if racine_sortie else racine
    debut = time.perf_counter()
    exiger_configuration(config)
    instant = int(time.time()) if instant is None else int(instant)
    ouverture = ouvrir(racine, registre, config, "B", run_t06, instant, run_t07, racine_sortie)
    lignes = ouverture["garde"]["lignes"]
    t07 = ouverture["manifeste_t07"]
    graines = t07.pop("graines")
    chemin_m, sondes_lues, niveau = Path(t07["chemin"]), t07["sondes_lues"], t07["niveau"]
    graines = completer_graines(graines, [f"{c}/{n}/{j}" for c in ("intervalle", "descriptif", CLE_P3_DESCRIPTIF) for n in sondes_lues
                                          for j in [cr.JEU_I] + list(cr.DOSES)])
    p3, tableA, audit = ouverture["p3bis"], ouverture["table_A"], ouverture["audit"]
    r14 = ouverture["garde_adaptee"].get("r14")
    try:
        lu = lv1.lire_issue_mots_et_cout(racine / lignes[rg.ISSUE_MOTS_ET_COUT_T06]["chemin"],
                                         lignes[rg.ISSUE_MOTS_ET_COUT_T06]["sha256"], float(config["niveau_base_t06"]))
        aires_rec = None
        if lu["lisible"] and config["controle_aire"] == "recalcul":
            try:
                aires_rec = lv1.aires_recalculees_t06(racine / config["scores_base_t06"]["chemin"], lu["issue"])
            except cr.IssueIllisible as e:
                lu = {"lisible": False, "motif": f"fichier « mots et coût » illisible : {e}", "chemin": lu["chemin"]}
        derivation = (cr.deriver_classe(lu["issue"], config["p064"], config["controle_aire"], float(config["tolerance_aire"]),
                                        aires_rec) if lu["lisible"] else None)
        q = derivation["Q"] if derivation else "illisible"
        phrase_m = lu["issue"]["phrase"] if lu["lisible"] else None
        fuites = {**cr.entree_F(audit, derivation["doses_jugees"] if derivation else []),
                  "audit": {"chemin": audit["chemin"], "sha256": audit["sha256"], "consigne": audit["consigne"]}}
        ep = lv1.lire_episodes_t06(racine, run_t06)
        g = "ok"
        P_, A_ = p3["P"], tableA["A"]
        ouvre, lii, oii = cr.ouvre_scores(g, P_, A_, q), cr.lit_ii(g, P_, A_, q), cr.ouvre_ii(g, P_, A_, q)
        jugees = list(derivation["doses_jugees"]) if (derivation and lii) else []
        refusees = [] if oii else list(cr.DOSES)
        jeux, hors, etats_i, etats_ii, motifs, ecarts_base, couples = None, None, [], {}, {}, {}, None
        planchers_p3_lus, index = None, None
        complementaires, reserves_id = None, []
        if ouvre:
            chemin_scores = racine_sortie / lignes[rg.SCORES_T07]["chemin"]
            t, index = lv1.ouvrir_scores(chemin_scores, sondes_lues, refusees)
            exiger_nombre_de_directions(t, index, config)        # note 05 (R-2305) : n_plancher directions par plancher décisif
            rg.journaliser_ouverture(registre, instant, f"scores-t07/{run_t07} (Q = {q} ; conditions retirées : "
                                     f"{', '.join(refusees) or 'aucune'})", lignes[rg.SCORES_T07]["sha256"])
            mesures = lv1.charger_mesures(ep["mesures"], list(config["predicteurs_triviaux"]) + ["cout"])
            decisifs = [cr.JEU_I] + jugees
            descriptifs = [d for d in cr.DOSES if d not in jugees] if oii else []
            jeux = lecture_jeux_v3(t, index, mesures, config, graines, niveau, decisifs)
            hors = lecture_jeux_v3(t, index, mesures, config, graines, 0.95, descriptifs, cle="descriptif") if descriptifs else {}
            for n in hors:
                for d in hors[n]:
                    hors[n][d]["marque"] = cr.mention_dose(derivation, d, lu["issue"]["doses"][d])
            etats_i = [jeux[n][cr.JEU_I]["etat"] for n in sondes_lues]
            etats_ii = {d: [jeux[n][d]["etat"] for n in sondes_lues] for d in jugees}
            motifs = {f"{n}/{j}": jeux[n][j]["echec"] for n in jeux for j in jeux[n] if "echec" in jeux[n][j]}
            for d in jugees:
                aire_base = lu["issue"]["doses"][d]["aire"]
                ecarts_base[d] = {"aire_base_decisive": aire_base, "base_decisive": lu["issue"]["doses"][d]["base_decisive"],
                                  "ecarts": {n: float(jeux[n][d]["aire"]) - float(aire_base) for n in sondes_lues
                                             if jeux[n][d]["etat"] == cr.AU_DESSUS},
                                  "phrase_T06": cr.PHRASE_GAIN_T06}
            couples = lecture_couples(t, index, config, [cr.JEU_I] + ([d for d in cr.DOSES] if oii else []))
            planchers_p3_lus = lecture_planchers_p3(t, index, mesures, config, graines,
                                                    [cr.JEU_I] + ([d for d in cr.DOSES] if oii else []))
            position = {str(c): i for i, c in enumerate(mesures["cle"].tolist())}
            mes_t = {k: v[np.array([position[str(c)] for c in t["cle"].tolist()], dtype=np.int64)] for k, v in mesures.items()}
            concepts = index.get("concepts") or {c: config["sondes_par_concept"][c] for c in lv1.CONCEPTS
                                                 if config["sondes_par_concept"][c] in sondes_lues}
            complementaires = lt2.lectures(t, index, mes_t, config, graines, concepts, jugees, refusees, jeux)
            reserves_id = lt2.reserves(complementaires, jeux, sondes_lues, hors)
        motif_L1 = (tableA["motif"] if A_ in ("illisible", "arret") else lu["motif"] if q == "illisible" else None)
        issue = cr.issue_critere_3(g, P_, A_, q, etats_i, etats_ii, fuites["F"], derivation, phrase_m, motifs, motif_L1)
        reserves = list(ep["reserves"]) + (list(derivation["reserves"]) if derivation else [])
        reserves += reserves_plancher_figees(index)            # v4 : palier « carte », principale rapportée
        reserves += [f"{r['id']} : {r['phrase']} ({r['motif']})" for r in reserves_id if r["phrase"] != "non déclenchée"]
        if r14:
            reserves.append(f"R14 : {r14['phrase']}")
        finale = bool(r14) and (issue["issue"] in ("L0b", "L0c", "L7b", "L7c") or (issue["issue"] == "L1" and q == "illisible"))
        doses = {"Q": q, "p064": config["p064"], "controle_aire": config["controle_aire"],
                 "motif_Q_illisible": lu["motif"] if q == "illisible" else None,
                 "qualifiees": derivation["doses_qualifiees"] if derivation else [],
                 "jugees": derivation["doses_jugees"] if derivation else [],
                 "hors_jugement": derivation["doses_hors_jugement"] if derivation else [],
                 "non_calculables": derivation["doses_non_calculables"] if derivation else [],
                 "etat_ii_par_dose_jugee": issue["combinaison"]["(ii) état par dose"],
                 "base_par_dose": {d: lu["issue"]["doses"][d] for d in cr.DOSES} if lu["lisible"] else None,
                 "derivation": derivation,
                 "marques": {d: cr.mention_dose(derivation, d, lu["issue"]["doses"][d]) for d in cr.DOSES} if derivation else None,
                 "qualification_S100": cr.mention_dose(derivation, "S100", lu["issue"]["doses"]["S100"]) if derivation else
                 "non lue (Q illisible)",
                 "etiquette_fichier": derivation["etiquette_fichier"] if derivation else None,
                 "etiquette_recalculee": derivation["etiquette_recalculee"] if derivation else None,
                 "phrase_M": phrase_m, "ecart_a_la_base": ecarts_base}
        pred_ii = lv1._prediction_ii(issue, q, ouvre)
        if finale and issue["issue"] in ("L7b", "L7c", "L1"):
            pred_ii = f"non lue : {issue['issue']} ; {PHRASE_SUITE_FINALE}"
        lecture = {"run_t07": run_t07, "run_t06": run_t06, "etape": "B", "sondes_lues": sondes_lues, "niveau_applique": niveau,
                   "doses": doses, "bases": {"mots_et_cout": lu}, "p3bis": p3, "table_A": tableA, "fuites": fuites,
                   "cles_ignorees": ouverture["garde"]["cles_ignorees"], "reserves": reserves, "ouverture": ouverture,
                   "issue_critere_3": issue["issue"], "phrase": issue["phrase"], "sous_phrase_L1b": issue["sous_phrase_L1b"],
                   "sous_phrase_L7": issue["sous_phrase_L7"],
                   "entrees": issue["entrees"], "combinaison": {**issue["combinaison"], "sondes": sondes_lues},
                   "regle_mots_et_cout": issue["regle_mots_et_cout"], "scores_ouverts": ouvre, "scores_ii_ouverts": ouvre and oii,
                   "conditions_retirees": refusees if ouvre else None,
                   "scores": {"chemin": lignes[rg.SCORES_T07]["chemin"], "sha256": lignes[rg.SCORES_T07]["sha256"]} if ouvre else None,
                   "jeux": jeux, "jeux_hors_jugement": hors, "couples_figes_descriptif": couples, "planchers_p3_descriptif": planchers_p3_lus,
                   "garde_adaptee": {"r14": r14, "lancement_a_ouverture_reduite": ouverture["garde_adaptee"].get("lancement_a_ouverture_reduite"),
                                     "suite": PHRASE_SUITE_FINALE if finale else None},
                   "predictions": {"T7-P1": lv1._prediction_i(issue), "T7-P2": pred_ii,
                                   **(complementaires["predictions"] if complementaires else
                                      {"T7-P3 à T7-P19": "non lues : scores non ouverts (" + issue["issue"] + ")"})},
                   "bases_complementaires": complementaires["bases"] if complementaires else None,
                   "reserves_identifiees": reserves_id + ([{"id": "R14", "phrase": r14["phrase"], "motif": "ouverture réduite"}] if r14 else []),
                   "graines_derivees": complementaires["graines_derivees"] if complementaires else [],
                   "durees_s": {"etape_b_s": round(time.perf_counter() - debut, 2)},
                   "couverture": cr.enumerer_couverture(), "methode_plancher": methode_plancher(config)}
        lv1.ecrire_resultat(racine_sortie, chemin_m, "lecture-t07", lecture)
    except GardeArret as e:
        lv1.ecrire_resultat(racine_sortie, chemin_m, "arret-etape-b", {"etape": "B", "motif": motif_d_arret(e)})
        raise ArretApresManifeste(str(e)) from e
    return lecture


# ---------------------------------------------------------------------------------------------------------------- commande
COMMANDES_V4 = ("etape-a", "etape-b", "empreinte-config", "controle-avant-ouverture")


def controle_avant_ouverture(argv: list[str]) -> int:
    """CLC-P3-02 (R-2311) : `reextraction_p3_v1.controler_avant_ouverture` joué en entier, après les contrôles de configuration
    de la v4, en lecture seule (rien n'est écrit), avant le repli et sa garde d'ouverture (étape 8 du script v4). Toute faute
    (`GardeArret`, ou l'une des fautes de `reextraction_p3_v1.FAUTES_DU_BRAS`) → refus, code 2, motif sur l'erreur ; passé →
    code 0, résumé JSON sur la sortie."""
    import json
    p = argparse.ArgumentParser(prog=f"{COMMANDE} controle-avant-ouverture",
                                description="contrôle entier de la réextraction de P3 avant l'ouverture (lecture seule)")
    p.add_argument("racine")
    p.add_argument("config_t07")
    p.add_argument("--cache-dir", default=None, help="cache de Hugging Face (essais) ; défaut : celui de l'environnement")
    a = p.parse_args(argv)
    try:
        config = charger_configuration(Path(a.config_t07))
        r = rx.controler_avant_ouverture(Path(a.racine), config, a.cache_dir)
    except GardeArret as err:
        print(f"REFUS : contrôle avant l'ouverture : {err}", file=sys.stderr)
        return CODE_REFUS
    except rx.FAUTES_DU_BRAS as err:
        print(f"REFUS : contrôle avant l'ouverture : faute {type(err).__name__} : {err}", file=sys.stderr)
        return CODE_REFUS
    print(json.dumps(r, ensure_ascii=False, sort_keys=True))
    return CODE_OK


def main(argv: list[str]) -> int:
    if argv and argv[0] == "controle-avant-ouverture":             # CLC-P3-02 (R-2311) : contrôle entier, avant le repli
        return controle_avant_ouverture(argv[1:])
    if argv and argv[0] == "passe-blanc":                         # passe à blanc (copie v2 : configuration de la v4)
        from . import passe_blanc_v2 as pb2
        return pb2.main(argv[1:])
    if argv and argv[0] in ("repli-seul", "etape-a-apres-repli"):     # repli en deux temps (copie v2 : étape A de la v4)
        from . import repli_etapes_v2 as rt2
        return rt2.main(argv)
    if argv and argv[0] == "repli-recalcul":
        print("REFUS : repli-recalcul n'est pas offert par lecture_v4 : jouer repli-seul, puis etape-a-apres-repli (ordre "
              "d'exécution)", file=sys.stderr)
        return CODE_REFUS
    if argv and argv[0] == "grille":                             # critères inchangés : la grille de la v2, rejouée
        return lv2.main(["grille"])
    p = argparse.ArgumentParser(prog=COMMANDE, description=__doc__.splitlines()[0])
    sp = p.add_subparsers(dest="action", required=True)
    for nom, aide in (("etape-a", "notation scellée, fermée (réextraction de P3, planchers par lots)"),
                      ("etape-b", "lecture mécanique, règle (a), 800 directions")):
        q = sp.add_parser(nom, help=aide)
        q.add_argument("racine")
        q.add_argument("run_t06")
        if nom == "etape-b":
            q.add_argument("run_t07")
        q.add_argument("config_t07")
        q.add_argument("--registre", default=None, help="défaut : clé `registre` de la configuration")
        q.add_argument("--racine-sortie", default=None)
        q.add_argument("--instant", default=None, type=int, help="instant d'ouverture (secondes UTC) ; essais seulement")
    e = sp.add_parser("empreinte-config", help="empreinte canonique de la configuration (contrôles de la v4)")
    e.add_argument("config_t07")
    a = p.parse_args(argv)
    if a.action == "empreinte-config":
        try:
            print(empreinte_configuration(Path(a.config_t07)))
            return CODE_OK
        except GardeArret as err:
            print(f"REFUS : {err}", file=sys.stderr)
            return CODE_REFUS
    try:
        config = charger_configuration(Path(a.config_t07))
        if config["mode"] == "reel" and a.instant is not None:                                   # CT-06
            raise GardeArret("--instant refusé en mode réel (essais seulement) : l'instant d'ouverture est celui de l'horloge")
        registre = Path(a.registre) if a.registre else Path(a.racine) / config["registre"]
        racine_sortie = Path(a.racine_sortie) if a.racine_sortie else None
        if a.action == "etape-a":
            r = etape_a(Path(a.racine), registre, config, a.run_t06, a.instant, racine_sortie)
            print(f"notation scellée, fermée : {r['scores']['chemin']} ; sondes lues {r['index']['sondes_lues']} ; plancher des "
                  f"figées : {r['planchers_figees']['etats']}")
            return CODE_OK
        r = etape_b(Path(a.racine), registre, config, a.run_t06, a.run_t07, a.instant, racine_sortie)
        print(f"{r['issue_critere_3']} : {r['phrase']}")
        return CODE_OK
    except ArretApresManifeste as err:
        print(f"ARRÊT : {err}", file=sys.stderr)
        return CODE_ARRET
    except GardeArret as err:
        print(f"REFUS : {err}", file=sys.stderr)
        return CODE_REFUS


__all__ = ["exiger_configuration", "charger_configuration", "empreinte_configuration", "methode_plancher", "charger_planchers_p3",
           "lecture_planchers_p3", "paliers_de", "reserves_plancher_figees", "exiger_nombre_de_directions", "controle_avant_ouverture", "noter", "etape_a", "etape_b", "main", "CLES_CONFIG",
           "CLE_P3_DESCRIPTIF", "SOURCE_P3",
           "SOURCE_FIGEES", "LECTURE_P3"]


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
