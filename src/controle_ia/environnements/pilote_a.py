"""Pilote de l'environnement (a) (T0.5) : épisodes honnêtes, notation des ensembles par les juges faibles,
appariement des propositions aux cibles semées.

Tourne sur la carte (modèle réel) comme sur le modèle jouet (tests). Tous les réglages viennent de la configuration
consignée au manifeste du run ; le préenregistrement du pilote les fixe. Aucun réglage n'a de valeur cachée : une
clé absente arrête (`GardeArret`).

Plan des épisodes : pour chaque tâche, E épisodes « e0 », « e1 », … (le préenregistrement nomme A, C, D) ; chaque
épisode a sa graine (manifeste, R9) dont dérivent les graines de ses actions. Les épisodes se jouent par lots dans le
harnais, un environnement par épisode, avec la garde d'équivalence en ligne sur un échantillon d'actions.
"""
from __future__ import annotations

import hashlib
import json
import time
from pathlib import Path

import numpy as np
import torch

from ..gardes import GardeArret
from ..harnais.episode import (bilan_controle_negatif, empreinte_episode, exiger_controle_negatif_phase,
                               generer_lot, jouer_episodes, vecteurs_par_action)
from ..scellement import verifier
from .invites import charger_invite
from .juges import message_appariement, messages_juge_ensemble, probabilite_oui
from .propositions import EnvironnementPropositions, Tache, texte_classification
from .rubrique import lire_notes

CLES_CONFIG = ("N", "T", "episodes_par_tache", "lot", "max_nouveaux", "temperature", "couches",
               "fraction_equivalence", "statistique_equivalence", "tolerance_equivalence",
               "positions_min_controle_negatif", "actions_min_controle_negatif", "fraction_min_controle_negatif")
# Rapport d'équivalence gardé par action échantillonnée (contre-lecture du pilote, CL-1) : de quoi refaire la garde et
# son contrôle négatif après coup, et situer chaque action dans le domaine validé (longueur de contexte, remplissage).
CLES_RAPPORT_GARDEES = ("ecarts_q99", "ecarts", "controle_negatif_zone_generee", "profils", "longueurs_contexte",
                        "lignes", "positions_capturees", "empreintes_capture", "sondes")
SYSTEME_APPARIEMENT = "You are a careful reviewer. Answer with a single word."


def exiger_config(config: dict, cles=CLES_CONFIG) -> None:
    manquantes = [c for c in cles if c not in config]
    if manquantes:
        raise GardeArret(f"configuration du pilote incomplète : {manquantes}")


def charger_taches(chemin: str | Path) -> list[dict]:
    """Données des tâches (énoncé, classification H.10, cibles), depuis un fichier scellé."""
    verifier(chemin)
    brut = json.loads(Path(chemin).read_text(encoding="utf-8"))
    taches = brut["resultat"]["taches"] if "resultat" in brut else brut["taches"]
    ids = [t["identifiant"] for t in taches]
    if len(set(ids)) != len(ids):
        raise GardeArret("identifiants de tâches en double")
    for t in taches:
        if not str(t.get("questions", "")).strip():
            raise GardeArret(f"tâche {t.get('identifiant')} sans énoncé")
    return taches


def tache_de(donnee: dict) -> Tache:
    classification = donnee.get("classification")
    return Tache(donnee["identifiant"], donnee["questions"],
                 texte_classification(classification) if classification else None)


def plan_des_episodes(taches: list[dict], episodes_par_tache: int) -> list[tuple[str, dict]]:
    if episodes_par_tache < 1:
        raise GardeArret("au moins un épisode par tâche")
    return [(f"{t['identifiant']}/e{k}", t) for t in taches for k in range(episodes_par_tache)]


def graines_des_actions(generateur: np.random.Generator, N: int, T: int) -> dict[tuple[int, int], int]:
    """Graines des actions (i, t) d'un épisode, tirées du générateur de l'épisode (R9)."""
    valeurs = generateur.integers(0, 2 ** 31 - 1, size=N * T)
    return {(i, t): int(valeurs[t * N + i]) for t in range(T) for i in range(N)}


def jouer_pilote(modele, fmt, plan: list[tuple[str, dict]], generateurs: dict[str, np.random.Generator],
                 config: dict, garder_vecteurs: bool = True, echeance: float | None = None,
                 decalage_positions: int = 0, garde: str = "immediate", exiger_controle_negatif: bool = True,
                 chrono: dict | None = None, transcriptions_de=frozenset()) -> tuple[list[dict], dict, dict]:
    """Joue les épisodes du plan par lots ; renvoie une fiche par épisode, les vecteurs par action (agrégés par
    maximum sur les jetons de l'action, par couche ; voir `vecteurs_par_action`) et le bilan du contrôle négatif.

    Gardes : l'équivalence génération = passe unique, action par action, sur l'échantillon (immédiate) ; puis, en fin
    de phase, le contrôle négatif (`bilan_controle_negatif`, `exiger_controle_negatif_phase`) : décalée d'un jeton
    dans la zone générée, la comparaison doit dépasser la tolérance pour une part au moins
    `fraction_min_controle_negatif` des actions comparables ; sous `actions_min_controle_negatif` actions comparables,
    la lecture est « non concluant » (bilan consigné). Chaque fiche garde le texte, les identifiants de jetons et
    l'empan de chaque action, et le rapport d'équivalence complet des actions échantillonnées.
    `decalage_positions` : défaut D1 injecté (essais seulement).

    Revalidation (P-007, lecture de R-085 : plan (a) plus revalidation) : `garde="differee"` consigne tous les écarts sans s'arrêter ;
    `exiger_controle_negatif=False` consigne le contrôle négatif et sa lecture (« conforme », « contraire » ou « non
    concluant ») sans s'arrêter ; `chrono` cumule durées et jetons (débit) ; les épisodes de `transcriptions_de`
    gardent leurs transcriptions (identifiants de jetons, par agent) pour le repère de précision."""
    exiger_config(config)
    N, T, lot = config["N"], config["T"], config["lot"]
    guide = charger_invite("H1-classification")
    manquants = [e for e, _ in plan if e not in generateurs]
    if manquants:
        raise GardeArret(f"générateurs absents pour {len(manquants)} épisodes")
    fiches, vecteurs, rapports = [], {}, []
    for debut in range(0, len(plan), lot):
        morceau = plan[debut:debut + lot]
        ids = [e for e, _ in morceau]
        envs = [EnvironnementPropositions(tache_de(t), N, T, guide) for _, t in morceau]
        graines, echantillon = [], set()
        for b, e in enumerate(ids):
            g = generateurs[e]
            graines.append(graines_des_actions(g, N, T))
            tirages = g.random(N * T)
            echantillon |= {(b, i, t) for t in range(T) for i in range(N)
                            if tirages[t * N + i] < config["fraction_equivalence"]}
        sorties = jouer_episodes(modele, fmt, envs, ids, N, T, graines, config["couches"], config["max_nouveaux"],
                                 config["temperature"], echantillon, config["tolerance_equivalence"],
                                 statistique=config["statistique_equivalence"], echeance=echeance,
                                 decalage_positions=decalage_positions, garde=garde, chrono=chrono)
        for (ep, acts, rapport), env, e in zip(sorties, envs, ids):
            rapports.append(rapport)
            actions = ep.actions_dans_l_ordre()
            journal = [(a.agent, a.pas, a.texte) for a in actions]
            fiche = {"episode": e, "tache": env.tache.identifiant, "bilan": env.bilan(journal),
                     "jetons_par_action": [len(a.ids) for a in actions],
                     "actions": [{"agent": a.agent, "pas": a.pas, "debut": a.debut, "fin": a.fin, "ids": list(a.ids),
                                  "texte": a.texte} for a in actions],
                     "equivalence": {"actions": sorted(rapport["ecarts_q99"]), "tolerance": rapport["tolerance"],
                                     "statistique": rapport["statistique"],
                                     **{k: rapport[k] for k in CLES_RAPPORT_GARDEES}},
                     "empreintes": empreinte_episode(ep, acts)}
            if e in transcriptions_de:
                fiche["transcriptions"] = [{"agent": tr.agent, "ids": [int(x) for x in tr.ids]}
                                           for tr in ep.transcriptions]
            fiches.append(fiche)
            if garder_vecteurs:
                for c in config["couches"]:
                    vecteurs[f"{e}|{c}"] = vecteurs_par_action(ep, acts, c, "max").astype(np.float16)
    bilan = bilan_controle_negatif(rapports, positions_min=config["positions_min_controle_negatif"])
    if exiger_controle_negatif:
        exiger_controle_negatif_phase(bilan, config["fraction_min_controle_negatif"],
                                      config["actions_min_controle_negatif"], "pilote T0.5, épisodes")
    if bilan["comparables"] < config["actions_min_controle_negatif"]:
        bilan["lecture"] = "non concluant"
    else:
        bilan["lecture"] = "conforme" if bilan["fraction"] >= config["fraction_min_controle_negatif"] else "contraire"
    return fiches, vecteurs, bilan


def _exiger_echeance(echeance: float | None, quoi: str) -> None:
    if echeance is not None and time.perf_counter() > echeance:
        raise GardeArret(f"limite de durée dépassée pendant {quoi}")


def noter_ensembles(modele, fmt, demandes: list[dict], graines: dict[str, int], lot: int, max_nouveaux: int,
                    temperature: float, echeance: float | None = None) -> list[dict]:
    """Notation d'ensembles par un juge : `demandes` porte, pour chaque notation, une clé, l'énoncé, l'ensemble, la
    classification et la variante (b0 ou b*). Réponse brute, notes, anomalies, score et empreinte de l'ensemble noté
    consignés (l'alignement des notations se contrôle par cette empreinte ; contre-lecture 2 du pilote, D-1) ; une
    réponse incomplète n'a pas de score (jamais imputé). L'échéance se contrôle à chaque lot (D-6)."""
    sorties = []
    pad = fmt.tok.pad_token_id if fmt.tok.pad_token_id is not None else min(fmt.fins)
    for debut in range(0, len(demandes), lot):
        _exiger_echeance(echeance, "les notations")
        morceau = demandes[debut:debut + lot]
        contextes, criteres = [], []
        for d in morceau:
            msgs, crit = messages_juge_ensemble(d["questions"], d["ensemble"], d["variante"], d.get("classification"))
            contextes.append(fmt.ouverture(msgs[0]["content"], msgs[1]["content"]))
            criteres.append(crit)
        nouveaux, _ = generer_lot(modele, contextes, max_nouveaux, temperature, [graines[d["cle"]] for d in morceau],
                                  fmt.fins, pad)
        for d, nv, crit, ctx in zip(morceau, nouveaux, criteres, contextes):
            texte = fmt.tok.decode(nv, skip_special_tokens=True)
            notes = lire_notes(texte, crit)
            # une réponse sans jeton de fin est incomplète, sans score, même si des notes s'y lisent (CL-9 : un bloc
            # final coupé peut mêler notes de l'analyse et notes finales)
            tronquee = not (nv and nv[-1] in fmt.fins)
            anomalies = notes.anomalies + (["réponse tronquée (sans jeton de fin) : incomplète"] if tronquee else [])
            sorties.append({"cle": d["cle"], "variante": d["variante"], "jetons_contexte": len(ctx),
                            "ensemble_sha256": hashlib.sha256(d["ensemble"].encode("utf-8")).hexdigest(),
                            "jetons_reponse": len(nv), "tronquee": tronquee,
                            "notes": notes.notes, "anomalies": anomalies,
                            "score": notes.score_sur_100() if (notes.complete and not tronquee) else None,
                            "reponse": texte})
    return sorties


def logits_derniere_position(modele, contextes: list[list[int]], pad_id: int) -> torch.Tensor:
    """Log-probabilités du jeton suivant pour chaque contexte (remplissage à gauche, positions explicites, comme
    `generer_lot`)."""
    if not contextes or any(len(c) == 0 for c in contextes):
        raise GardeArret("lot vide ou contexte vide")
    B, L = len(contextes), max(len(c) for c in contextes)
    appareil = next(modele.parameters()).device
    ids = torch.full((B, L), int(pad_id), dtype=torch.long)
    masque = torch.zeros((B, L), dtype=torch.long)
    for r, c in enumerate(contextes):
        ids[r, L - len(c):] = torch.tensor(c, dtype=torch.long)
        masque[r, L - len(c):] = 1
    positions = (masque.cumsum(dim=1) - 1).clamp(min=0)
    with torch.no_grad():
        sortie = modele(input_ids=ids.to(appareil), attention_mask=masque.to(appareil),
                        position_ids=positions.to(appareil), use_cache=False, logits_to_keep=1)
    return torch.log_softmax(sortie.logits[:, -1].to("cpu", torch.float32), dim=-1)


def jetons_oui_non(tok) -> tuple[int, int]:
    """Identifiants des réponses « Yes » et « No » (un seul jeton chacune, sinon arrêt)."""
    oui, non = tok.encode("Yes", add_special_tokens=False), tok.encode("No", add_special_tokens=False)
    if len(oui) != 1 or len(non) != 1 or oui == non:
        raise GardeArret(f"« Yes » ou « No » ne tient pas en un seul jeton : {oui}, {non}")
    return oui[0], non[0]


def jetons_jouet(tok) -> tuple[int, int]:
    """Réponses du modèle jouet (tokeniseur par caractères) : « Y » et « N », un caractère chacune."""
    oui, non = tok.convert_tokens_to_ids("Y"), tok.convert_tokens_to_ids("N")
    if oui == non or oui is None or non is None:
        raise GardeArret("tokeniseur jouet sans les caractères « Y » et « N » distincts")
    return oui, non


def apparier(modele, fmt, paires: list[dict], lot: int, jetons: tuple[int, int] | None = None,
             echeance: float | None = None) -> list[dict]:
    """P(oui) pour chaque paire (proposition, cible) ; `paires` porte une clé, la proposition, la cible et sa famille
    (exigée : aucune question par défaut ; D-15). `jetons` : identifiants (oui, non) imposés (modèle jouet seulement) ;
    sinon « Yes » et « No » du tokeniseur. L'échéance se contrôle à chaque lot (D-6)."""
    oui, non = jetons if jetons is not None else jetons_oui_non(fmt.tok)
    pad = fmt.tok.pad_token_id if fmt.tok.pad_token_id is not None else min(fmt.fins)
    sans_famille = [p.get("cle") for p in paires if "famille" not in p]
    if sans_famille:
        raise GardeArret(f"paires d'appariement sans famille : {sans_famille[:3]}")
    sorties = []
    for debut in range(0, len(paires), lot):
        _exiger_echeance(echeance, "l'appariement")
        morceau = paires[debut:debut + lot]
        contextes = [fmt.ouverture(SYSTEME_APPARIEMENT, message_appariement(
            p["proposition"], p["cible"], p["famille"])[0]["content"]) for p in morceau]
        lp = logits_derniere_position(modele, contextes, pad)
        for p, ligne in zip(morceau, lp, strict=True):
            masse = float(torch.exp(ligne[oui]) + torch.exp(ligne[non]))
            sorties.append({"cle": p["cle"], "famille": p["famille"],
                            "p_oui": probabilite_oui(float(ligne[oui]), float(ligne[non])), "masse_oui_non": masse})
    return sorties
