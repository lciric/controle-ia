"""Lanceur du premier test boîte blanche sur l'organisme (i-a) (P3, R-192, R-202), côté machine de calcul.

Enchaîne, sous un manifeste de run (préenregistrement scellé exigé en mode réel, R1), sans retour en arrière :
1. contrôle du format de l'agent (conversation de contrôle de l'environnement (a), texte attendu dans l'ouverture) ;
2. données génériques (fichiers versés, empreintes de la provenance), faits trop courts exclus (compte cité exigé),
   tirage des textes « enjeux élevés », identifiants et empans dans le gabarit de l'agent ;
3. extraction des activations des empans aux couches lues (passe unique du harnais) ;
4. découpage par groupe, entraînement des 2 × 5 × 3 sondes (code de T0.7 tel quel, au plus `fils_entrainement` fils, au
   plus les cœurs de l'affinité du processus et au plus la partie entière du quota de processeur de son groupe de contrôle
   s'il en a un ; ces deux bornes et le nombre effectif consignés ; pertes relevées), validation générique, sondes
   principales, planchers (200 chacune) ; budget de durée propre à l'entraînement, relu à chaque sonde et après chaque
   plancher ;
5. **sondes figées** : fichier complet scellé sous `donnees/<run>/` (son empreinte en ligne `PROGRES` et dans le résultat
   `sondes-figees.json`, avant le premier épisode) ; fichier léger (sans les matrices de Mahalanobis) pour la poussée ;
6. épisodes des quatre conditions (honnête, saboteur instruit « coût gonflé », témoin instruit, « mention sans usage »),
   mêmes graines d'action pour une même tâche d'une condition à l'autre, garde d'équivalence en ligne et contrôle négatif
   de la phase ; chaque action notée en ligne par toutes les sondes (notation vectorisée ; garde d'identité sur la
   première action notable du premier épisode de chaque lot, à défaut du lot ; un lot sans action notable est consigné
   tel quel, sans arrêt ; au moins un contrôle de Mahalanobis exigé sur les `lots_mahalanobis_identite` premiers lots,
   vérifié juste après eux) ; scores par jeton des deux sondes principales et bornes des champs de l'action ; mesures
   sans juge ;
7. scores et mesures par action dans `donnees/<run>/scores-p3.npz` (scellé) ; scores par jeton des sondes principales
   dans `donnees/<run>/jetons-principales-p3.npz` (scellé) ; **textes des actions** dans
   `donnees/<run>/textes-actions-p3.jsonl` (scellé ; poussé vers le dépôt de travail privé seulement, précédent N-014 (a),
   jamais dans la copie publique) ; fiches sans texte dans `episodes-p3.json` ; résumé. Tout arrêt après le manifeste
   laisse un `arret.json` scellé, puis se propage.

Mode « jouet » (tests, répétitions sur processeur) : modèle jouet et tokeniseur par caractères ; même chaîne, mêmes gardes.
"""
from __future__ import annotations

import argparse
import gc
import hashlib
import json
import os
import re
import signal
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import torch

from ..environnements.invites import charger_invite
from ..environnements.lancer_pilote_a import charger_modele_et_format, conversation_de_controle, memoire_pic_gio
from ..environnements.pilote_a import (CLES_RAPPORT_GARDEES, charger_taches, exiger_config, graines_des_actions,
                                       tache_de)
from ..gardes import GardeArret, exiger_sans_signal, lever_sur_term, motif_d_arret, relever_term_apres
from ..harnais.episode import (bilan_controle_negatif, empreinte_episode, exiger_controle_negatif_phase,
                               jouer_episodes)
from ..harnais.formats import verifier_format
from ..harnais.run_harnais_factice import graine_entiere
from ..harnais.validation_reelle import (ENTROPIE_CITEE, exiger_code_cite, exiger_code_importe_sous,
                                         exiger_memoire_vive, noyau)
from ..manifeste import config_canonique, creer_manifeste, ecrire_resultat, generateur, lire_manifeste
from ..scellement import sceller, verifier
from ..sondes.familles import SondeMahalanobis
from . import donnees as dn
from .conditions import CHAMPS_BORNES, CONDITIONS, bornes_champs, charger_consignes, environnement, mesures_action
from .entrainement import (FAMILLES_P3, _echeance, entrainer_concept, extraire, noms_des_sondes, plancher_de,
                           preparer_enjeux, preparer_tromperie)
from .figees import ecrire_sondes
from .notation import Notation, agreger_par_jeton, exiger_identite

COMMANDE = "python -m controle_ia.premier_test_ia.run"
DUREE_MAX_S = 18_000
CLES_P3 = ("agent", "mode", "noyau_attention", "fils", "fils_entrainement", "duree_max_s", "budget_entrainement_s",
           "conditions", "n_faits_max", "n_par_classe_enjeux", "max_jetons_enjeux", "retrait_fin_tromperie",
           "part_entrainement", "n_plancher", "faits_exclus_attendus", "memoire_vive_min_go",
           "lots_mahalanobis_identite", "tolerance_identite", "chemin_consignes", "consignes_sha256")
NOYAUX = ("math", "defaut")
CONCEPTS = ("tromperie", "enjeux")
CONFIG_CITEE = re.compile(r"Configuration de P3 \(empreinte canonique\) : `([0-9a-f]{64})`")
TACHES_CITEES = re.compile(r"Tâches de P3 : `([0-9a-f]{64})`")
MESURES_BOOLEENNES = ("valide", "cout_present", "cout_plusieurs_nombres", "cout_multiplication", "cout_intervalle",
                      "cout_suffixe_k", "cout_milliers_espace", "titre_present", "titre_sans_capitale", "action_sans_ligne",
                      "revise_sans_numero", "mention_texte_prive", "mention_triple")
MESURES_REELLES = ("cout", "cout_groupes_joints")
TOLERANCE_PAR_JETON = 1e-9


def progres(**champs) -> None:
    """Ligne de progression à préfixe fixe, sans aucun texte (recopiée dans le journal de l'instance par son script)."""
    instant = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print("PROGRES " + instant + " " + " ".join(f"{k}={v}" for k, v in champs.items()), file=sys.stderr, flush=True)


def empreinte_config(config: dict) -> str:
    return hashlib.sha256(config_canonique(config)).hexdigest()


def exiger_config_p3(config: dict) -> None:
    exiger_config(config)
    manquantes = [c for c in CLES_P3 if c not in config]
    if manquantes:
        raise GardeArret(f"configuration de P3 incomplète : {manquantes}")
    if config["mode"] not in ("reel", "jouet"):
        raise GardeArret(f"mode {config['mode']!r} inconnu")
    if config["noyau_attention"] not in NOYAUX:
        raise GardeArret(f"noyau d'attention {config['noyau_attention']!r} : {NOYAUX} attendus")
    if config["N"] != 1:
        raise GardeArret("P3 : un agent par épisode (N = 1)")
    if config.get("episodes_par_tache", 1) != 1:
        raise GardeArret("P3 : un épisode par tâche et par condition (episodes_par_tache = 1)")
    if tuple(config["conditions"]) != CONDITIONS:
        raise GardeArret(f"conditions {config['conditions']} : {list(CONDITIONS)} attendues, dans cet ordre")
    for k in ("duree_max_s", "budget_entrainement_s"):
        v = config[k]
        if isinstance(v, bool) or not isinstance(v, (int, float)) or not 0 < v <= DUREE_MAX_S:
            raise GardeArret(f"{k} {v!r} : un nombre dans ]0 ; {DUREE_MAX_S}] s attendu")


def exiger_citations_p3(prereg: Path, config: dict, sha_taches: str) -> int:
    """La configuration (empreinte canonique), les tâches et l'entropie sont celles que cite le préenregistrement."""
    texte = Path(prereg).read_text(encoding="utf-8")
    c, t, e = CONFIG_CITEE.search(texte), TACHES_CITEES.search(texte), ENTROPIE_CITEE.search(texte)
    if not (c and t and e):
        raise GardeArret(f"{prereg} ne cite pas la configuration, les tâches ou l'entropie de P3")
    if empreinte_config(config) != c.group(1):
        raise GardeArret(f"configuration {empreinte_config(config)[:12]} ≠ configuration citée {c.group(1)[:12]}")
    if sha_taches != t.group(1):
        raise GardeArret(f"tâches {sha_taches[:12]} ≠ tâches citées {t.group(1)[:12]}")
    return int(e.group(1))


def plan_p3(taches: list[dict]) -> list[tuple[str, dict, str]]:
    """Un épisode par tâche et par condition, conditions entremêlées (un lot mêle les conditions)."""
    return [(f"{c}/{t['identifiant']}/e0", t, c) for t in taches for c in CONDITIONS]


def cles_des_graines(taches: list[dict], config: dict) -> list[str]:
    cles = ["tirage-enjeux", "decoupage-tromperie", "decoupage-enjeux"]
    for concept in CONCEPTS:
        cles += [f"sonde/{n}" for n in noms_des_sondes(concept, config["couches"])]
        cles.append(f"plancher/{concept}")
    cles += [f"tache/{t['identifiant']}" for t in taches]
    return cles + ["modele-jouet"]


def _quota_du_dossier(dossier: Path, v2: bool) -> float | None:
    """Quota d'un dossier du groupe de contrôle, en cœurs ; None sans quota (« max » en v2, −1 en v1) ou illisible."""
    try:
        if v2:
            quota, periode = (dossier / "cpu.max").read_text().split()[:2]
        else:
            quota = (dossier / "cpu.cfs_quota_us").read_text().strip()
            periode = (dossier / "cpu.cfs_period_us").read_text().strip()
    except (OSError, ValueError):
        return None
    if not (quota.isdigit() and periode.isdigit()) or int(quota) <= 0 or int(periode) <= 0:
        return None
    return int(quota) / int(periode)


def quota_processeur_cgroup(proc_cgroup: str = "/proc/self/cgroup", racine: str = "/sys/fs/cgroup") -> float | None:
    """Quota de processeur du groupe de contrôle du processus et de tous ses ancêtres, en cœurs, le plus petit
    l'emportant (v2 : ligne « 0:: » et `cpu.max`, « quota période » ou « max période » ; v1 : contrôleur « cpu »,
    `cpu.cfs_quota_us`, −1 sans quota, et `cpu.cfs_period_us`) ; None si aucun quota n'est lisible. Même parcours que
    `harnais.validation_reelle.plafonds_cgroup` pour la mémoire. `os.sched_getaffinity` ne voit pas ce quota (RC-09)."""
    try:
        lignes = Path(proc_cgroup).read_text().splitlines()
    except OSError:
        return None
    quota = None
    for ligne in lignes:
        morceaux = ligne.split(":", 2)
        if len(morceaux) != 3:
            continue
        _, controleurs, chemin = morceaux
        if controleurs == "":
            base, v2 = Path(racine), True
        elif "cpu" in controleurs.split(","):
            base, v2 = Path(racine) / "cpu", False
        else:
            continue
        parties = [x for x in chemin.split("/") if x]
        for k in range(len(parties), -1, -1):
            q = _quota_du_dossier(base.joinpath(*parties[:k]), v2)
            if q is not None:
                quota = q if quota is None else min(quota, q)
    return quota


def coeurs_disponibles(proc_cgroup: str = "/proc/self/cgroup", racine: str = "/sys/fs/cgroup") -> dict:
    """Les deux bornes consignées : cœurs de l'affinité du processus, quota de processeur du groupe de contrôle (en
    cœurs, None sans quota)."""
    try:
        affinite = len(os.sched_getaffinity(0))
    except (AttributeError, OSError):
        affinite = os.cpu_count() or 1
    return {"affinite": int(affinite), "quota_groupe_de_controle": quota_processeur_cgroup(proc_cgroup, racine)}


def fils_effectifs(demandes: int, coeurs: dict | None = None) -> int:
    """min(fils demandés, cœurs de l'affinité, partie entière du quota du groupe de contrôle s'il existe), au moins un
    fil (nombre consigné au résultat, avec les deux bornes de `coeurs_disponibles`)."""
    c = coeurs_disponibles() if coeurs is None else coeurs
    bornes = [int(demandes), int(c["affinite"])]
    if c.get("quota_groupe_de_controle") is not None:
        bornes.append(int(c["quota_groupe_de_controle"]))
    return max(1, min(bornes))


def controler_format_agent(fmt, spec: dict, mode: str) -> dict:
    consigne, observations, reponses = conversation_de_controle("agent", None)
    controle = verifier_format(fmt, consigne, observations, reponses)
    attendu = spec.get("texte_attendu_ouverture")
    if mode == "reel" and not attendu:
        raise GardeArret("agent : texte attendu dans l'ouverture absent de la configuration")
    if attendu and attendu not in fmt.tok.decode(fmt.ouverture(consigne, observations[0])):
        raise GardeArret(f"agent : ouverture sans {attendu!r} (variables du gabarit non lues)")
    return {**controle, "texte_attendu_ouverture": attendu}


def exiger_par_jeton(pj: dict, scores: dict, tolerance: float = TOLERANCE_PAR_JETON) -> None:
    """Les scores par jeton gardés redonnent, agrégés, le score de l'action (même sonde, même empan)."""
    for nom, (s, lg) in pj.items():
        v = agreger_par_jeton(s, lg)
        if not abs(v - scores[nom]) <= tolerance * (1.0 + abs(scores[nom])):
            raise GardeArret(f"scores par jeton de {nom} incohérents avec le score de l'action ({v!r} ≠ {scores[nom]!r})")


def jouer_p3(modele, fmt, plan, graines_taches: dict, config: dict, consignes: dict, notation: Notation,
             principales: list[str], echeance: float | None = None, chrono: dict | None = None) -> tuple:
    """Épisodes par lots ; rend les lignes par action (mesures et scores, sans texte), les fiches par épisode (sans
    texte), le bilan du contrôle négatif, les rapports de la garde d'identité, les textes des actions et, par action
    notée, les scores par jeton des sondes principales avec les bornes des champs."""
    exiger_config(config)
    if not set(notation.couches) <= set(config["couches"]):
        raise GardeArret(f"sondes aux couches {notation.couches}, activations lues aux couches {config['couches']}")
    if not set(principales) <= set(notation.noms):
        raise GardeArret(f"sondes principales {principales} absentes de la notation")
    T, lot = config["T"], config["lot"]
    guide = charger_invite("H1-classification")
    lignes, fiches, rapports, identites, textes, jetons = [], [], [], [], [], []
    n_lots, n_mahalanobis = -(-len(plan) // lot), int(config["lots_mahalanobis_identite"])

    def exiger_mahalanobis():
        if not any(x.get("mahalanobis") for x in identites):
            raise GardeArret("garde d'identité : aucun contrôle de la famille de Mahalanobis sur les premiers lots")

    if n_mahalanobis < 1:
        exiger_mahalanobis()                    # aucun premier lot où contrôler Mahalanobis : arrêt avant tout épisode
    for k_lot, debut in enumerate(range(0, len(plan), lot)):
        morceau = plan[debut:debut + lot]
        ids = [e for e, _, _ in morceau]
        envs = [environnement(c, tache_de(t), T, guide, consignes) for _, t, c in morceau]
        graines, echantillon = [], set()
        for b, (_, t, _) in enumerate(morceau):
            g = generateur(graines_taches[t["identifiant"]])      # un générateur neuf par condition : mêmes graines
            graines.append(graines_des_actions(g, 1, T))
            tirages = g.random(T)
            echantillon |= {(b, 0, s) for s in range(T) if tirages[s] < config["fraction_equivalence"]}
        sorties = jouer_episodes(modele, fmt, envs, ids, 1, T, graines, config["couches"], config["max_nouveaux"],
                                 config["temperature"], echantillon, config["tolerance_equivalence"],
                                 statistique=config["statistique_equivalence"], echeance=echeance, chrono=chrono)
        a_controler = None          # première action notable du premier épisode du lot, à défaut du lot
        notables = []
        for b, ((ep, acts, rapport), (e, t, c)) in enumerate(zip(sorties, morceau)):
            for a in ep.actions_dans_l_ordre():
                fin = a.fin - 1 if a.ids and a.ids[-1] in fmt.fins else a.fin
                if fin > a.debut:
                    notables.append((b, a.pas))
        if notables:
            a_controler = min(notables, key=lambda x: (x[0] != 0, x[0], x[1]))
        controle_du_lot = None
        for b, ((ep, acts, rapport), (e, t, c)) in enumerate(zip(sorties, morceau)):
            rapports.append(rapport)
            actions = ep.actions_dans_l_ordre()
            for a in actions:
                fin = a.fin - 1 if a.ids and a.ids[-1] in fmt.fins else a.fin
                ligne = {"episode": e, "condition": c, "tache": t["identifiant"], "pas": a.pas, "jetons": len(a.ids),
                         "jetons_notes": max(0, fin - a.debut), **mesures_action(a.texte), "scores": None}
                textes.append({"episode": e, "condition": c, "tache": t["identifiant"], "pas": a.pas, "texte": a.texte})
                if fin > a.debut:
                    seg = {k: acts[a.agent][k][a.debut:fin] for k in notation.couches}
                    ligne["scores"] = notation.noter(seg)
                    pj = notation.par_jeton(seg, principales)
                    exiger_par_jeton(pj, ligne["scores"])
                    jetons.append({"rang": len(lignes), "par_jeton": pj, "bornes": bornes_champs(fmt.tok, a.ids, a.texte)})
                    if (b, a.pas) == a_controler:
                        sauf = () if k_lot < config["lots_mahalanobis_identite"] else ("mahalanobis",)
                        controle_du_lot = {"lot": k_lot, "episode": e, "pas": a.pas, "mahalanobis": not sauf,
                                           **exiger_identite(notation, seg, ligne["scores"], config["tolerance_identite"],
                                                             sauf)}
                lignes.append(ligne)
            fiches.append({"episode": e, "condition": c, "tache": t["identifiant"],
                           "jetons_par_action": [len(a.ids) for a in actions],
                           "equivalence": {"actions": sorted(rapport["ecarts_q99"]), "tolerance": rapport["tolerance"],
                                           "statistique": rapport["statistique"],
                                           **{k: rapport[k] for k in CLES_RAPPORT_GARDEES}},
                           "empreintes": empreinte_episode(ep, acts)})
        # un lot qui a une action notable a son contrôle par construction (action choisie parmi elles) ; un lot sans
        # action notable est consigné tel quel
        identites.append(controle_du_lot or {"lot": k_lot, "sans_action_notable": True})
        progres(etape="episodes", lot=f"{k_lot + 1}/{n_lots}", actions=len(lignes))
        if k_lot + 1 == min(n_mahalanobis, n_lots):
            exiger_mahalanobis()                # juste après les premiers lots, pas après le dernier (RC-07)
    exiger_mahalanobis()
    bilan = bilan_controle_negatif(rapports, positions_min=config["positions_min_controle_negatif"])
    exiger_controle_negatif_phase(bilan, config["fraction_min_controle_negatif"], config["actions_min_controle_negatif"],
                                  "P3, épisodes")
    if bilan["comparables"] < config["actions_min_controle_negatif"]:
        bilan["lecture"] = "non concluant"
    else:
        bilan["lecture"] = "conforme" if bilan["fraction"] >= config["fraction_min_controle_negatif"] else "contraire"
    return lignes, fiches, bilan, identites, textes, jetons


def tableaux_des_scores(lignes: list[dict], noms: list[str]) -> dict:
    """Tables par action pour le fichier des scores : identifiants, mesures, scores (NaN si l'empan noté est vide)."""
    n = len(lignes)
    scores = np.full((n, len(noms)), np.nan)
    for i, l in enumerate(lignes):
        if l["scores"] is not None:
            scores[i] = [l["scores"][k] for k in noms]
    t = {"noms_sondes": np.array(noms), "scores": scores,
         "episode": np.array([l["episode"] for l in lignes]), "condition": np.array([l["condition"] for l in lignes]),
         "tache": np.array([l["tache"] for l in lignes]), "pas": np.array([l["pas"] for l in lignes], dtype=np.int64),
         "jetons": np.array([l["jetons"] for l in lignes], dtype=np.int64),
         "jetons_notes": np.array([l["jetons_notes"] for l in lignes], dtype=np.int64)}
    for k in MESURES_REELLES:
        t[k] = np.array([np.nan if l[k] is None else float(l[k]) for l in lignes])
    for k in MESURES_BOOLEENNES:
        t[k] = np.array([bool(l[k]) for l in lignes])
    return t


def tableaux_par_jeton(jetons: list[dict], principales: list[str]) -> dict:
    """Scores par jeton des sondes principales (concaténés, avec le rang de l'action, le début et la longueur de chaque
    tranche), logits d'attention (NaN hors famille à attention) et bornes des champs (−1 : champ absent)."""
    t = {"principales": np.array(principales), "champs": np.array(CHAMPS_BORNES),
         "rang": np.array([j["rang"] for j in jetons], dtype=np.int64),
         "bornes": np.array([[j["bornes"][c] for c in CHAMPS_BORNES] for j in jetons], dtype=np.int64).reshape(-1, len(CHAMPS_BORNES)),
         "bornes_lisibles": np.array([j["bornes"]["lisibles"] for j in jetons], dtype=bool)}
    longueurs = np.array([len(j["par_jeton"][principales[0]][0]) for j in jetons], dtype=np.int64)
    t["longueur"] = longueurs
    t["debut"] = np.concatenate([[0], np.cumsum(longueurs)[:-1]]).astype(np.int64) if len(jetons) else np.zeros(0, np.int64)
    for k, p in enumerate(principales):
        t[f"scores_{k}"] = np.concatenate([j["par_jeton"][p][0] for j in jetons]) if jetons else np.zeros(0)
        t[f"logits_{k}"] = np.concatenate([j["par_jeton"][p][1] if j["par_jeton"][p][1] is not None
                                           else np.full(len(j["par_jeton"][p][0]), np.nan) for j in jetons]) if jetons else np.zeros(0)
    return t


def executer(config: dict, racine: Path, run_id: str, prereg: str | None, chemin_taches: str,
             autoriser_depot_sale: bool = False) -> dict:
    racine = Path(racine)
    exiger_config_p3(config)
    if config["mode"] == "reel" and prereg is None:
        raise GardeArret("run réel de P3 sans préenregistrement : R1 interdit de lancer")
    taches = charger_taches(chemin_taches)
    sha_taches = verifier(chemin_taches)
    consignes = charger_consignes(config["chemin_consignes"], config["consignes_sha256"])
    charger_invite("H1-classification")
    commit_cite, entropie = None, None
    if prereg is not None:
        exiger_code_importe_sous(racine)
        commit_cite = exiger_code_cite(racine, Path(prereg))
        entropie = exiger_citations_p3(Path(prereg), config, sha_taches)
    plan = plan_p3(taches)
    chemin_m, manifeste = creer_manifeste(racine, run_id, config, cles_des_graines(taches, config), entropie=entropie,
                                          decisif=prereg is not None, prereg=prereg,
                                          autoriser_depot_sale=autoriser_depot_sale, commande=COMMANDE)
    debut = time.perf_counter()
    etat = {"etape": "mémoire vive", "commit_cite": commit_cite, "taches_sha256": sha_taches,
            "config_sha256": empreinte_config(config), "consignes_sha256": consignes["sha256"]}
    try:
        etat["memoire_vive"] = exiger_memoire_vive(config["memoire_vive_min_go"]) if config["memoire_vive_min_go"] else None
        etat["etape"] = "chargement"
        return _executer_apres_manifeste(config, racine, run_id, chemin_m, manifeste, taches, plan, consignes, etat,
                                         debut)
    except Exception as e:          # garde, panne, signal TERM : consigné, puis propagé
        ecrire_resultat(racine, chemin_m, "arret", {"etape": etat["etape"], "motif": motif_d_arret(e),
                                                     "partiel": {k: v for k, v in etat.items() if k != "etape"},
                                                     "duree_s": round(time.perf_counter() - debut, 1)})
        relever_term_apres(e)
        raise


def _ecrire_textes(chemin: Path, textes: list[dict]) -> str:
    if chemin.exists():
        raise GardeArret(f"{chemin} existe déjà (R12)")
    with open(chemin, "w", encoding="utf-8") as f:
        for x in textes:
            f.write(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n")
    return sceller(chemin)


def _executer_apres_manifeste(config, racine, run_id, chemin_m, manifeste, taches, plan, consignes, etat, debut) -> dict:
    g = manifeste["graines"]
    echeance = debut + float(config["duree_max_s"])
    reel = config["mode"] == "reel"
    appareil = "cuda" if reel else "cpu"
    from ..harnais.modeles import regler_determinisme

    reglages = regler_determinisme(config["fils"], appareil)
    modele, fmt = charger_modele_et_format(config["agent"], config["mode"], graine_entiere(g["modele-jouet"]))
    etat["etape"] = "contrôle du format"
    etat["format"] = controler_format_agent(fmt, config["agent"], config["mode"])
    progres(etape="format", verifie=etat["format"]["verifie"])

    etat["etape"] = "données génériques"
    faits = dn.charger_faits()
    if config["n_faits_max"] is not None:
        faits = faits[:int(config["n_faits_max"])]
    ex_t, exclus = preparer_tromperie(fmt, dn.exemples_tromperie(faits), config["retrait_fin_tromperie"])
    if len(exclus) != config["faits_exclus_attendus"]:
        raise GardeArret(f"{len(exclus)} faits sans empan ({exclus[:10]}) ; {config['faits_exclus_attendus']} cités")
    tir = dn.tirer_enjeux(dn.charger_enjeux(), generateur(g["tirage-enjeux"]), config["n_par_classe_enjeux"])
    ex_e = preparer_enjeux(fmt, tir, config["max_jetons_enjeux"])
    etat["donnees"] = {"faits": len(faits), "faits_exclus": exclus, "exemples_tromperie": len(ex_t),
                       "exemples_enjeux": len(ex_e), "lignes_enjeux": [x["ligne"] for x in tir]}
    progres(etape="donnees", tromperie=len(ex_t), enjeux=len(ex_e), faits_exclus=len(exclus))

    etat["etape"] = "extraction"
    depart = time.perf_counter()
    seq = {"tromperie": extraire(modele, ex_t, config["couches"], echeance),
           "enjeux": extraire(modele, ex_e, config["couches"], echeance)}
    etat["extraction_s"] = round(time.perf_counter() - depart, 1)
    progres(etape="extraction", duree_s=etat["extraction_s"])

    etat["etape"] = "entraînement"
    exemples = {"tromperie": ex_t, "enjeux": ex_e}
    resultats, planchers = {}, {}
    fils_avant = torch.get_num_threads()
    etat["coeurs"] = coeurs_disponibles()
    etat["fils_entrainement_effectifs"] = fils_effectifs(config["fils_entrainement"], etat["coeurs"])
    torch.set_num_threads(etat["fils_entrainement_effectifs"])
    depart = time.perf_counter()
    echeance_e = min(echeance, depart + float(config["budget_entrainement_s"]))
    try:
        for concept in CONCEPTS:
            y = [x["y"] for x in exemples[concept]]
            idx_e, idx_v = dn.decouper([x["groupe"] for x in exemples[concept]], generateur(g[f"decoupage-{concept}"]),
                                       config["part_entrainement"])
            graines = {n: graine_entiere(g[f"sonde/{n}"]) for n in noms_des_sondes(concept, config["couches"])}
            r = entrainer_concept(concept, seq[concept], y, idx_e, idx_v, config["couches"], graines, appareil, echeance_e)
            principale = next(s for s in r["sondes"] if s.nom == r["principale"])
            planchers[concept] = plancher_de(principale, seq[concept], idx_e, config["n_plancher"],
                                             graine_entiere(g[f"plancher/{concept}"]))
            _echeance(echeance_e, f"le plancher de {concept}")         # budget relu après chaque plancher (RC-10)
            resultats[concept] = r
            progres(etape="entrainement", concept=concept, principale=r["principale"],
                    aire_validation=round(r["aires_validation"][r["principale"]], 4))
    finally:
        torch.set_num_threads(fils_avant)
    etat["entrainement_s"] = round(time.perf_counter() - depart, 1)
    del seq
    gc.collect()

    etat["etape"] = "sondes figées"
    sondes = [s for c in CONCEPTS for s in resultats[c]["sondes"]] + [s for c in CONCEPTS for s in planchers[c]]
    meta = {"principales": {c: resultats[c]["principale"] for c in CONCEPTS},
            "planchers": {c: [s.nom for s in planchers[c]] for c in CONCEPTS}}
    dossier = racine / "donnees" / run_id
    dossier.mkdir(parents=True, exist_ok=False)
    sha_figees = ecrire_sondes(dossier / "sondes-figees.npz", sondes, meta)
    legeres = [s for s in sondes if not isinstance(s, SondeMahalanobis)]
    sha_legeres = ecrire_sondes(dossier / "sondes-figees-legeres.npz", legeres, {**meta, "complet": sha_figees})
    ecrire_resultat(racine, chemin_m, "sondes-figees", {
        "sondes_figees_sha256": sha_figees, "sondes_legeres_sha256": sha_legeres,
        "sondes": [{"nom": s.nom, "classe": type(s).__name__, "famille": getattr(s, "famille", None),
                    "couche": int(s.couche), "agregation": s.agregation, "empreinte": s.empreinte()} for s in sondes],
        "principales": meta["principales"],
        "aires_validation": {c: resultats[c]["aires_validation"] for c in CONCEPTS},
        "identite_validation": {c: resultats[c]["identite_validation"] for c in CONCEPTS},
        "effectifs": {c: {"entrainement": resultats[c]["n_entrainement"], "validation": resultats[c]["n_validation"]}
                      for c in CONCEPTS},
        "durees_entrainement_s": {c: resultats[c]["durees_entrainement_s"] for c in CONCEPTS},
        "pertes": {c: resultats[c]["pertes"] for c in CONCEPTS},
        "donnees": etat["donnees"], "familles": list(FAMILLES_P3), "fils_entrainement": config["fils_entrainement"],
        "fils_entrainement_effectifs": etat["fils_entrainement_effectifs"], "coeurs": etat["coeurs"],
        "duree_s": round(time.perf_counter() - debut, 1)})
    etat["sondes_figees_sha256"] = sha_figees
    progres(etape="sondes-figees", empreinte=sha_figees, sondes=len(sondes))      # clés en minuscules : relayée

    etat["etape"] = "épisodes"
    notation = Notation(sondes, appareil)
    principales = [meta["principales"][c] for c in CONCEPTS]
    graines_taches = {t["identifiant"]: g[f"tache/{t['identifiant']}"] for t in taches}
    chrono: dict = {}
    memoire_pic_gio()
    depart = time.perf_counter()
    with noyau(config["noyau_attention"]):
        lignes, fiches, controle_negatif, identites, textes, jetons = jouer_p3(
            modele, fmt, plan, graines_taches, config, consignes, notation, principales, echeance, chrono)
    descriptifs = {"duree_s": round(time.perf_counter() - depart, 1), "memoire_pic_gio": memoire_pic_gio(), **chrono}
    noms = [s.nom for s in sondes]
    chemin_s = dossier / "scores-p3.npz"
    with open(chemin_s, "wb") as f:
        np.savez(f, **tableaux_des_scores(lignes, noms))
    sha_s = sceller(chemin_s)
    chemin_j = dossier / "jetons-principales-p3.npz"
    with open(chemin_j, "wb") as f:
        np.savez(f, **tableaux_par_jeton(jetons, principales))
    sha_j = sceller(chemin_j)
    sha_t = _ecrire_textes(dossier / "textes-actions-p3.jsonl", textes)
    ecrire_resultat(racine, chemin_m, "episodes-p3", {
        "fiches": fiches, "scores": str(chemin_s.relative_to(racine)), "scores_sha256": sha_s,
        "jetons_principales": str(chemin_j.relative_to(racine)), "jetons_principales_sha256": sha_j,
        "textes": str((dossier / "textes-actions-p3.jsonl").relative_to(racine)), "textes_sha256": sha_t,
        "controle_negatif": controle_negatif, "identite": identites, "reglages": reglages,
        "noyau_attention": config["noyau_attention"], "format": etat["format"], "descriptifs": descriptifs,
        "duree_s": round(time.perf_counter() - debut, 1)})
    etat["episodes_ecrits"] = len(fiches)

    etat["etape"] = "résumé"
    resume = {"commit_cite": etat["commit_cite"], "config_sha256": etat["config_sha256"],
              "taches_sha256": etat["taches_sha256"], "consignes_sha256": etat["consignes_sha256"],
              "sondes_figees_sha256": sha_figees, "scores_sha256": sha_s, "jetons_principales_sha256": sha_j,
              "textes_sha256": sha_t, "principales": meta["principales"],
              "episodes": len(fiches), "actions": len(lignes),
              "actions_notees": sum(1 for x in lignes if x["scores"] is not None),
              "controle_negatif": controle_negatif["lecture"], "duree_s": round(time.perf_counter() - debut, 1)}
    exiger_sans_signal("avant le résumé")
    ecrire_resultat(racine, chemin_m, "resume", resume)
    lire_manifeste(chemin_m)
    progres(etape="fin", episodes=len(fiches), actions=len(lignes))
    return resume


_signal_term = lever_sur_term


def _main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(prog=COMMANDE)
    ap.add_argument("--config", required=True)
    ap.add_argument("--taches", required=True)
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--prereg", default=None)
    a = ap.parse_args(argv)
    signal.signal(signal.SIGTERM, _signal_term)
    verifier(a.config)
    config = json.loads(Path(a.config).read_text(encoding="utf-8"))
    resume = executer(config, Path("."), a.run_id, a.prereg, a.taches)
    print(json.dumps(resume, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
