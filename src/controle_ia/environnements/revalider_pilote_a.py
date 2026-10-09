"""Revalidation courte de l'équivalence sur le domaine du pilote (T0.5).

P-007 retenue par Lazar, lue comme le plan (a) plus une revalidation courte avant le pilote (R-085 ; lecture confirmée
par Lazar le 2026-10-07, R-094) ; remarque CL-3 de la contre-lecture 1 du pilote. Préenregistrement :
`prereg/T0.5-revalidation-equivalence-pilote-v1.md` (brouillon 4 : contre-lecture RV-1 à RV-23, vérification courte
W-1 à W-14).

Deux bras de noyau d'attention (« defaut », puis « math ») jouent les mêmes épisodes : agent honnête, tâches
d'entraînement de l'extraction scellée aux énoncés les plus longs (jamais une tâche d'évaluation du pilote), mêmes
graines, demi-précision, garde d'équivalence différée sur toutes les actions. Chaque bras est écrit et scellé dès qu'il
est joué (épisodes, mesures), puis lu dès que son repère est calculé : un arrêt ultérieur ne perd pas un bras lu (RV-1).

Lectures d'un bras (`lire_bras`) :
- R1 : maximum, sur les actions et les couches, du 99e centile par action ≤ la tolérance ; avec marge si ≤ `marge_q99` ;
- R2 : contrôle négatif de l'action entière (T0.4 v3, P5) ;
- R3 : repère (passe unique en demi-précision au noyau du bras, contre passe unique en simple précision au noyau
  « math », sur les plus longues transcriptions du bras) : deux fois son 99e centile ≤ la tolérance, à chaque couche ;
- R4 : rejeu du lot 0 dans le processus : empreintes identiques ;
- R5 : domaine : assez d'actions comparées, une action remplie, et le plus long contexte comparé atteint une part fixée du
  plus long contexte joué ;
- R6 (« defaut » seulement, RV-3) : logique de la génération remplie au noyau par défaut, en simple précision, sur le lot 0
  : C1 écart maximal ≤ `chemin.tolerance`, C2 contrôle positif D1 vu, C3 contrôle négatif conforme ;
- R7 : pic de mémoire ≤ `memoire_pic_max_gio` (RV-2) ;
- R8 : durée projetée des épisodes du pilote ≤ `duree_max_episodes_pilote_s` (RV-15) ;
- audit de symétrie (RV-6) : écarts non nuls dans la zone générée à chaque couche (P9 de T0.4 v3), sondes d'audit, et
  rapport au repère ρ ≤ `rho_max` ; P9 ou sondes en défaut, ou ρ au-dessus au noyau par défaut : bras non conforme ; ρ
  au-dessus au noyau « math » : réserve.
Règle gelée (`choisir_noyau`) : le premier bras conforme avec marge (« defaut », puis « math ») ; sinon nœud, avec une
proposition prête si un bras n'est conforme que sans marge, ou s'il ne manque que le contrôle négatif de l'action entière
alors que sa garde restreinte à la zone générée est conforme.

Mode « jouet » : modèle jouet sur processeur, mêmes chaînes et mêmes gardes (tests et répétitions).
"""
from __future__ import annotations

import argparse
import gc
import hashlib
import json
import math
import re
import signal
import sys
import time
from pathlib import Path

import numpy as np
import torch

from ..gardes import GardeArret
from ..harnais.activations import ecarts_par_jeton, passe_unique
from ..harnais.run_harnais_factice import graine_entiere
from ..harnais.validation_reelle import (ENTROPIE_CITEE, exiger_code_cite, exiger_code_importe_sous,
                                         exiger_memoire_carte, noyau)
from ..manifeste import config_canonique, creer_manifeste, ecrire_resultat, generateur
from ..scellement import verifier
from .lancer_pilote_a import charger_modele_et_format
from .pilote_a import CLES_CONFIG, charger_taches, exiger_config, jouer_pilote

BRAS = ("defaut", "math")
TACHES_PILOTE = 64
EPISODES_PILOTE = 192          # 64 tâches × 3 épisodes (préenregistrement du pilote)
CLES_REVALIDATION = CLES_CONFIG + ("agent", "mode", "fils", "bras", "nombre_taches", "transcriptions_repere",
                                   "actions_min_comparees", "part_min_contexte_couvert", "memoire_carte_min_gio",
                                   "memoire_pic_max_gio", "marge_q99", "rho_max", "duree_max_s", "duree_max_bras_s",
                                   "duree_max_episodes_pilote_s", "chemin", "controle_positif")
CLES_CHEMIN = ("T", "tolerance")
CLES_CONTROLE_POSITIF = ("T", "decalage_positions", "positions_min", "actions_min", "fraction_min")
CONFIG_CITEE = re.compile(r"Configuration de la revalidation \(empreinte canonique\) : `([0-9a-f]{64})`")
TACHES_CITEES = re.compile(r"Tâches d'entraînement : `([0-9a-f]{64})`")
EVALUATION_CITEE = re.compile(r"Tâches d'évaluation : `([0-9a-f]{64})`")
INDEX_CITE = re.compile(r"Index des invites : `([0-9a-f]{64})`")    # RV-18 : l'invite H1 entre dans le domaine
COMMANDE = "python -m controle_ia.environnements.revalider_pilote_a"


def _sha_fichier(chemin) -> str:
    return hashlib.sha256(Path(chemin).read_bytes()).hexdigest()


def exiger_config_revalidation(config: dict) -> None:
    exiger_config(config, CLES_REVALIDATION)
    if config["mode"] not in ("reel", "jouet"):
        raise GardeArret(f"mode {config['mode']!r} inconnu")
    if list(config["bras"]) != list(BRAS):
        raise GardeArret(f"bras {config['bras']!r} : {list(BRAS)} attendus, dans cet ordre (règle de choix)")
    if config["statistique_equivalence"] != "q99" or config["episodes_par_tache"] != 1:
        raise GardeArret("revalidation : 99e centile (garde de production de T0.4 v3) et un épisode par tâche")
    if config["fraction_equivalence"] != 1.0:
        raise GardeArret("revalidation : toutes les actions comparées (fraction 1,0 ; RV-4)")
    if not 0 < config["marge_q99"] <= config["tolerance_equivalence"]:
        raise GardeArret("marge du 99e centile hors de ]0, tolérance]")
    if not (1 <= int(config["transcriptions_repere"]) <= config["nombre_taches"]):
        raise GardeArret("nombre de transcriptions du repère hors du plan")
    if config["duree_max_bras_s"] > config["duree_max_s"] or config["rho_max"] <= 0:
        raise GardeArret("durée d'un bras au-delà de la durée du run, ou ρ maximal non positif")
    for nom, cles in (("chemin", CLES_CHEMIN), ("controle_positif", CLES_CONTROLE_POSITIF)):
        manquantes = [c for c in cles if c not in config[nom]]
        if manquantes:
            raise GardeArret(f"configuration « {nom} » incomplète : {manquantes}")


def _sans_version(identifiant: str) -> str:
    return re.sub(r"v\d+$", "", identifiant)


def taches_d_entrainement(chemin_entrainement, chemin_evaluation, n: int) -> tuple[list[dict], dict]:
    """Les `n` tâches d'entraînement aux énoncés les plus longs (en caractères ; à égalité, l'ordre de la liste), dans
    l'ordre de la liste (RV-5), et la comparaison de leurs longueurs à celles des tâches d'évaluation du pilote. Arrêt si
    une tâche d'entraînement est aussi une tâche d'évaluation (identifiant exact ou sans le suffixe de version), si la
    liste d'évaluation compte moins de 64 tâches, ou s'il manque des tâches d'entraînement (R1, RV-8)."""
    entrainement = charger_taches(chemin_entrainement)
    evaluation = charger_taches(chemin_evaluation)
    if len(evaluation) < TACHES_PILOTE:
        raise GardeArret(f"{len(evaluation)} tâches d'évaluation, {TACHES_PILOTE} attendues")
    ids_eval = {t["identifiant"] for t in evaluation} | {_sans_version(t["identifiant"]) for t in evaluation}
    communes = sorted(t["identifiant"] for t in entrainement
                      if t["identifiant"] in ids_eval or _sans_version(t["identifiant"]) in ids_eval)
    if communes:
        raise GardeArret(f"tâches d'entraînement aussi tâches d'évaluation : {communes}")
    if len(entrainement) < n:
        raise GardeArret(f"{len(entrainement)} tâches d'entraînement, {n} attendues")
    rangs = sorted(range(len(entrainement)), key=lambda i: (-len(entrainement[i]["questions"]), i))[:n]
    choisies = [entrainement[i] for i in sorted(rangs)]
    longueurs = sorted(len(t["questions"]) for t in choisies)
    longueurs_eval = sorted(len(t["questions"]) for t in evaluation)
    return choisies, {"longueur_max_choisies": longueurs[-1], "longueur_min_choisies": longueurs[0],
                      "longueur_max_evaluation": longueurs_eval[-1],
                      "longueur_q90_evaluation": float(np.quantile(longueurs_eval, 0.9)),
                      "couvre_le_pilote": longueurs[-1] >= longueurs_eval[-1]}


def exiger_citations(prereg: Path, config: dict, sha_taches: str, sha_evaluation: str,
                     sha_index: str | None = None) -> int:
    """La configuration (empreinte canonique), les deux fichiers de tâches, l'index des invites transcrites (hors de
    l'arbre gelé ; l'invite H1 entre dans la consigne de l'agent, donc dans le domaine ; RV-18) et l'entropie sont ceux
    que cite le préenregistrement (RV-8). Rend l'entropie citée."""
    from .invites import RACINE_INVITES

    sha_index = verifier(RACINE_INVITES / "index.json") if sha_index is None else sha_index
    texte = Path(prereg).read_text(encoding="utf-8")
    c, t, v, e, i = (CONFIG_CITEE.search(texte), TACHES_CITEES.search(texte), EVALUATION_CITEE.search(texte),
                     ENTROPIE_CITEE.search(texte), INDEX_CITE.search(texte))
    if not (c and t and v and e and i):
        raise GardeArret(f"{prereg} ne cite pas la configuration, les tâches, l'index des invites ou l'entropie de la "
                         "revalidation")
    if sha_index != i.group(1):
        raise GardeArret(f"index des invites {sha_index[:12]} ≠ index cité {i.group(1)[:12]}")
    if hashlib.sha256(config_canonique(config)).hexdigest() != c.group(1):
        raise GardeArret("configuration ≠ configuration citée")
    if sha_taches != t.group(1):
        raise GardeArret(f"tâches d'entraînement {sha_taches[:12]} ≠ tâches citées {t.group(1)[:12]}")
    if sha_evaluation != v.group(1):
        raise GardeArret(f"tâches d'évaluation {sha_evaluation[:12]} ≠ tâches citées {v.group(1)[:12]}")
    return int(e.group(1))


def _infini_si_nan(x) -> float:
    return float("inf") if x is None or x != x else float(x)


def domaine_et_garde(fiches: list[dict]) -> dict:
    """Grandeur de la garde (R1) et domaine couvert (R5), sur les actions comparées de tous les épisodes."""
    q99, maxima, contextes, remplies, comparees = [], [], [], 0, 0
    joues = [int(a["debut"]) for f in fiches for a in f["actions"]]
    for f in fiches:
        eq = f["equivalence"]
        for cle, par_couche in eq["ecarts_q99"].items():
            comparees += 1
            q99 += [_infini_si_nan(v) for v in par_couche.values()]
            maxima += [_infini_si_nan(v) for v in eq["ecarts"][cle].values()]
            contextes.append(int(eq["longueurs_contexte"][cle]))
            remplies += int(eq["lignes"][cle]["remplissage"] > 0)
    return {"actions_comparees": comparees, "q99_max": max(q99) if q99 else None,
            "ecart_max": max(maxima) if maxima else None,
            "contexte_max": max(contextes, default=0), "contexte_max_joue": max(joues, default=0),
            "actions_remplies": remplies}


def q99_depasse(au_dessus: int, positions: int) -> bool:
    """Le 99e centile (interpolation linéaire) de `positions` valeurs dépasse le seuil dès qu'au moins
    positions − ⌊0,99 (positions − 1)⌋ d'entre elles le dépassent (condition suffisante, donc prudente ; RV-11)."""
    return positions > 0 and au_dessus >= positions - math.floor(0.99 * (positions - 1))


def garde_zone_generee(fiches: list[dict], tolerance: float, positions_min: int) -> dict:
    """Garde restreinte à la zone générée : 99e centile des écarts de la seule zone générée (par action et par couche)
    ; contrôle négatif sur le 99e centile de la zone générée décalée, la grandeur même de cette garde (RV-11) ; part des
    actions comparées dont la zone générée compte moins de 1 % des positions."""
    q99g, parts, comparables, passent = [], [], 0, 0
    for f in fiches:
        eq = f["equivalence"]
        for cle in eq["ecarts_q99"]:
            n = eq["positions_capturees"][cle]
            parts.append((n - eq["longueurs_contexte"][cle]) / n if n else 0.0)
            for prof in eq["profils"][cle].values():
                if prof["generee"]["jetons"]:
                    q99g.append(_infini_si_nan(prof["generee"]["q99"]))
            zone = eq["controle_negatif_zone_generee"].get(cle)
            if zone is None or min(v["positions"] for v in zone.values()) < positions_min:
                continue
            comparables += 1
            if all(q99_depasse(v["au_dessus"], v["positions"]) for v in zone.values()):
                passent += 1
    return {"q99_generee_max": max(q99g) if q99g else None, "comparables": comparables, "passent": passent,
            "fraction": passent / comparables if comparables else None,
            "part_zone_generee_sous_1pc": sum(x < 0.01 for x in parts) / len(parts) if parts else None}


def audit_symetrie(fiches: list[dict], repere: dict | None) -> dict:
    """Audit de symétrie d'un bras (RV-6, comme T0.4 v3) : écarts nuls de la zone générée par couche (P9 : au moins un
    écart non nul à chaque couche), sondes d'audit (tableaux distincts, perturbation d'un ulp vue) sur toutes les
    actions comparées, et rapport au repère ρ_ℓ = plus grand 99e centile par action à la couche ℓ / 99e centile du
    repère à ℓ."""
    nuls, jetons, q99_par_couche, sondes = {}, {}, {}, []
    for f in fiches:
        eq = f["equivalence"]
        for cle in eq["ecarts_q99"]:
            for c, prof in eq["profils"][cle].items():
                z = prof["generee"]
                if z["jetons"]:
                    nuls[str(c)] = nuls.get(str(c), 0) + z.get("nuls", 0)
                    jetons[str(c)] = jetons.get(str(c), 0) + z["jetons"]
            for c, v in eq["ecarts_q99"][cle].items():
                q99_par_couche[str(c)] = max(q99_par_couche.get(str(c), 0.0), _infini_si_nan(v))
            sondes.append(eq["sondes"][cle])
    p9 = bool(jetons) and all(nuls[c] < jetons[c] for c in jetons)
    rho = None
    if repere:
        rho = {c: (q / repere[c]["q99"] if repere.get(c, {}).get("q99") else float("inf"))
               for c, q in q99_par_couche.items()}
    return {"P9_zone_generee_non_nulle": p9, "nuls_zone_generee": nuls, "jetons_zone_generee": jetons,
            "sondes_conformes": bool(sondes) and all(s["tableaux_distincts"] and s["ulp_vu"] for s in sondes),
            "rho": rho, "rho_max_observe": max(rho.values()) if rho else None}


def lire_chemin(fiches_sain: list[dict], controle_negatif_sain: dict, fiches_d1: list[dict], config: dict) -> dict:
    """Phase « chemin » du noyau par défaut, en simple précision (RV-3, reprise de T0.4 v3) : C1, écart maximal par
    action et par couche ≤ `chemin.tolerance` ; C2, défaut D1 injecté vu (maximum de la zone générée au-dessus de la
    tolérance à chaque couche) pour au moins `fraction_min` des actions comparables, au moins `actions_min` ; C3, contrôle
    négatif de la phase conforme."""
    tol, cp = config["chemin"]["tolerance"], config["controle_positif"]
    maxima = [_infini_si_nan(v) for f in fiches_sain for d in f["equivalence"]["ecarts"].values() for v in d.values()]
    comparables = vus = 0
    for f in fiches_d1:
        for prof in f["equivalence"]["profils"].values():
            zones = [p["generee"] for p in prof.values()]
            if any(z["jetons"] < cp["positions_min"] for z in zones):
                continue
            comparables += 1
            vus += int(all(_infini_si_nan(z["max"]) > tol if z["max"] == z["max"] else False for z in zones))
    c2 = ("non concluant" if comparables < cp["actions_min"]
          else ("conforme" if vus / comparables >= cp["fraction_min"] else "contraire"))
    c1 = bool(maxima) and max(maxima) <= tol
    return {"C1_ecart_max": max(maxima) if maxima else None, "C1": c1, "C2_comparables": comparables, "C2_vus": vus,
            "C2": c2, "C3": controle_negatif_sain["lecture"],
            "conforme": bool(c1 and c2 == "conforme" and controle_negatif_sain["lecture"] == "conforme")}


def duree_projetee_pilote(chrono: dict, episodes: int) -> float | None:
    """Durée projetée des épisodes du pilote (RV-15) : génération et passes uniques du bras, à l'échelle des épisodes du
    pilote (192 contre `episodes`) ; les comparaisons, faites ici sur toutes les actions, n'y entrent pas."""
    if not episodes or "generation_s" not in chrono:
        return None
    return (chrono["generation_s"] + chrono.get("passe_unique_s", 0.0)) * EPISODES_PILOTE / episodes


def lire_bras(mesures: dict, controle_negatif: dict, repere: dict | None, rejeu_identique: bool | None,
              config: dict, panne: str | None = None, zone_generee: dict | None = None, audit: dict | None = None,
              chemin: dict | None = None, bras: str = "math", memoire_pic_gio: float | None = None,
              duree_projetee_s: float | None = None) -> dict:
    """Lecture gelée d'un bras. Un bras en panne, ou dont une mesure manque, est non conforme."""
    tol = config["tolerance_equivalence"]
    if panne is not None:
        return {"conforme": False, "conforme_avec_marge": False, "panne": panne}
    r1 = mesures["q99_max"] is not None and mesures["q99_max"] <= tol
    marge = r1 and mesures["q99_max"] <= config["marge_q99"]
    r2 = controle_negatif["lecture"]
    r3 = repere is not None and all(2 * _infini_si_nan(v["q99"]) <= tol for v in repere.values())
    r4 = bool(rejeu_identique)
    r5 = (mesures["actions_comparees"] >= config["actions_min_comparees"] and mesures["actions_remplies"] > 0
          and mesures["contexte_max"] >= config["part_min_contexte_couvert"] * mesures["contexte_max_joue"])
    r6 = True if bras != "defaut" else bool(chemin and chemin["conforme"])
    r7 = memoire_pic_gio is None or memoire_pic_gio <= config["memoire_pic_max_gio"]
    r8 = duree_projetee_s is None or duree_projetee_s <= config["duree_max_episodes_pilote_s"]
    a = audit or {}
    rho_haut = a.get("rho_max_observe") is not None and a["rho_max_observe"] > config["rho_max"]
    audit_ok = bool(audit) and a["P9_zone_generee_non_nulle"] and a["sondes_conformes"] and not (
        bras == "defaut" and rho_haut)
    base = bool(r1 and r2 == "conforme" and r3 and r4 and r5 and r6 and r7 and r8 and audit_ok)
    lecture = {"R1_garde_saine": r1, "R1_marge": marge, "R2_controle_negatif": r2, "R3_seuil_fonde": r3,
               "R4_rejeu": r4, "R5_domaine_couvert": r5, "R6_chemin_defaut": r6, "R7_memoire": r7, "R8_duree": r8,
               "audit_conforme": audit_ok, "reserve_rho": bool(rho_haut and bras != "defaut"),
               "audit_R4_ecarts_tous_nuls": mesures["ecart_max"] == 0,
               "conforme": base, "conforme_avec_marge": bool(base and marge)}
    if zone_generee is not None:
        zg = zone_generee
        g1 = zg["q99_generee_max"] is not None and zg["q99_generee_max"] <= tol
        g2 = (zg["comparables"] >= config["actions_min_controle_negatif"]
              and zg["fraction"] >= config["fraction_min_controle_negatif"])
        lecture["garde_zone_generee_conforme"] = bool(g1 and g2)
        # seul manque : le contrôle négatif de l'action entière ; la garde restreinte est conforme
        lecture["aveugle_action_entiere_seulement"] = bool(r1 and marge and r2 != "conforme" and r3 and r4 and r5
                                                          and r6 and r7 and r8 and audit_ok and g1 and g2)
    return lecture


def choisir_noyau(lectures: dict) -> tuple[str | None, dict | None]:
    """Règle gelée : le premier bras conforme avec marge, dans l'ordre (« defaut », puis « math ») ; sinon nœud (None),
    avec une proposition prête : un bras conforme sans marge (garde en ligne plus fréquente ou seuil, décision de
    Lazar), ou un bras qui ne manque que le contrôle négatif de l'action entière, garde restreinte conforme. Un bras non
    lu (run arrêté) n'est pas conforme."""
    for b in BRAS:
        if lectures.get(b, {}).get("conforme_avec_marge"):
            return b, None
    for b in BRAS:
        if lectures.get(b, {}).get("conforme"):
            return None, {"motif": "conforme sans marge (R1 au-dessus de la marge)", "noyau": b}
    for b in BRAS:
        if lectures.get(b, {}).get("aveugle_action_entiere_seulement"):
            return None, {"motif": "garde de l'action entière aveugle, garde restreinte conforme",
                          "garde": "zone générée", "noyau": b}
    return None, None


def statistiques_repere(bas: dict, ref: dict, couches) -> dict:
    """Écart par jeton entre activations de demi-précision (`bas`) et de référence (`ref`), mêmes transcriptions."""
    sortie = {}
    for c in couches:
        e = np.concatenate([ecarts_par_jeton(bas[k][c], ref[k][c]) for k in sorted(ref)])
        sortie[str(c)] = {"jetons": int(e.size), "q50": float(np.quantile(e, 0.5)), "q99": float(np.quantile(e, 0.99)),
                          "max": float(e.max())}
    return sortie


def _activations(modele, transcriptions: dict, couches) -> dict:
    return {k: {c: a.astype(np.float32) for c, a in passe_unique(modele, ids, couches).items()}
            for k, ids in transcriptions.items()}


def _empreintes_rejeu(fiches: list[dict]) -> dict:
    return {f["episode"]: {"empreintes": f["empreintes"], "captures": f["equivalence"].get("empreintes_capture")}
            for f in fiches}


def plus_longues_transcriptions(fiches: list[dict], n: int, bras: str) -> dict:
    """Les `n` plus longues transcriptions de l'agent (à égalité, l'ordre des épisodes), pour le repère (RV-12)."""
    toutes = [(f["episode"], tr) for f in fiches for tr in f.get("transcriptions", [])]
    rangs = sorted(range(len(toutes)), key=lambda i: (-len(toutes[i][1]["ids"]), i))[:n]
    return {f"{bras}|{toutes[i][0]}|{toutes[i][1]['agent']}": toutes[i][1]["ids"] for i in sorted(rangs)}


def _charger_bas(config: dict, graine_jouet: int):
    modele, fmt = charger_modele_et_format(config["agent"], config["mode"], graine_jouet)
    if config["mode"] == "jouet":
        modele = modele.to(torch.bfloat16).eval()
    return modele, fmt


def _modele_reference(config: dict, graine_jouet: int):
    """Modèle de référence du repère et de la phase « chemin » : simple précision (le même modèle jouet, ou la révision
    figée du 8B, conversion exacte des poids natifs en bfloat16)."""
    if config["mode"] == "jouet":  # poids arrondis en demi-précision puis convertis sans perte, comme ceux du 8B
        m, _ = charger_modele_et_format(config["agent"], "jouet", graine_jouet)
        return m.to(torch.bfloat16).to(torch.float32).eval()
    from ..harnais.modeles import charger_modele

    m, _ = charger_modele(config["agent"]["modele"], config["agent"]["revision"], "float32", "cuda", "sdpa")
    return m


def _liberer() -> None:
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
        torch.cuda.reset_peak_memory_stats()


def cles_des_graines(ids_episodes: list[str]) -> list[str]:
    """Une graine par épisode, et par épisode du lot 0 pour la phase « chemin » et son contrôle positif (R9)."""
    return (ids_episodes + [f"chemin/{e}" for e in ids_episodes] + [f"controle-positif/{e}" for e in ids_episodes]
            + ["modele-jouet"])


def executer(config: dict, racine: Path, run_id: str, prereg: str | None, chemin_entrainement: str,
             chemin_evaluation: str, autoriser_depot_sale: bool = False, entropie_essai: int | None = None) -> dict:
    """`entropie_essai` : entropie fixée d'une répétition sans préenregistrement (tests) ; refusée avec un
    préenregistrement, qui cite la sienne."""
    racine = Path(racine)
    exiger_config_revalidation(config)
    if config["mode"] == "reel" and prereg is None:
        raise GardeArret("revalidation réelle sans préenregistrement : R1 interdit de lancer")
    if prereg is not None and entropie_essai is not None:
        raise GardeArret("entropie d'essai refusée avec un préenregistrement : seule l'entropie citée vaut")
    verifier(chemin_entrainement)
    verifier(chemin_evaluation)
    sha_taches, sha_evaluation = _sha_fichier(chemin_entrainement), _sha_fichier(chemin_evaluation)
    entropie = entropie_essai
    if prereg is not None:
        exiger_code_cite(racine, Path(prereg))
        exiger_code_importe_sous(racine)
        entropie = exiger_citations(Path(prereg), config, sha_taches, sha_evaluation)
    taches, domaine_enonces = taches_d_entrainement(chemin_entrainement, chemin_evaluation, config["nombre_taches"])
    plan = [(f"{t['identifiant']}/e0", t) for t in taches]
    ids_episodes = [e for e, _ in plan]
    config_m = dict(config, taches_entrainement=chemin_entrainement, taches_entrainement_sha256=sha_taches,
                    taches_evaluation=chemin_evaluation, taches_evaluation_sha256=sha_evaluation)
    chemin_m, manifeste = creer_manifeste(racine, run_id, config_m, cles_des_graines(ids_episodes), entropie=entropie,
                                          decisif=prereg is not None, prereg=prereg,
                                          autoriser_depot_sale=autoriser_depot_sale,
                                          commande=f"{COMMANDE} --run-id {run_id}")
    etat = {"etape": "mise en place", "lectures": {}}
    debut = time.perf_counter()
    try:
        return _executer_apres_manifeste(config, racine, chemin_m, manifeste, plan, ids_episodes, etat,
                                         domaine_enonces, debut)
    except Exception as e:          # garde, panne, signal TERM : consigné avec la règle sur les bras lus, puis propagé
        noyau_partiel, proposition = choisir_noyau(etat["lectures"])
        ecrire_resultat(racine, chemin_m, "arret", {
            "etape": etat["etape"], "motif": f"{type(e).__name__}: {e}", "duree_s": round(time.perf_counter() - debut, 1),
            "bras_lus": sorted(etat["lectures"]), "noyau_retenu_sur_les_bras_lus": noyau_partiel,
            "proposition_au_noeud": proposition})
        raise


def exiger_echeance_bras(echeance: float, bras: str) -> None:
    """Échéance du bras contrôlée avant le repère (vérification 2, W-3) ; la phase « chemin » la reçoit aussi."""
    if time.perf_counter() > echeance:
        raise GardeArret(f"limite de durée du bras {bras} dépassée avant le repère")


def exiger_carte_a100(nom: str) -> str:
    """Domaine revalidé : A100 80 Go (P-007 ; vérification 2, W-13). Une autre carte est un écart au préenregistrement :
    arrêt consigné avant tout bras, nœud. Le nom se lit par mot entier : « RTX A1000 » n'est pas une A100 (relecture du
    différentiel, X-9)."""
    if not re.search(r"\bA100\b", nom):
        raise GardeArret(f"carte « {nom} » : le domaine revalidé est une A100 (écart au préenregistrement, nœud)")
    return nom


def exiger_mesures_reelles(reel: bool, memoire_pic_gio, duree_projetee_s, bras: str) -> None:
    """R7 et R8 ne se lisent jamais sans mesure en mode réel (W-14). Appelée après l'écriture des épisodes et des mesures
    du bras, qui restent ainsi écrits et scellés (RV-1 ; relecture du différentiel, X-5)."""
    if reel and (memoire_pic_gio is None or duree_projetee_s is None):
        raise GardeArret(f"bras {bras} : pic de mémoire ou durée projetée absents en mode réel")


def _jouer_bras(modele, fmt, bras, plan, ids_episodes, g, config, echeance) -> dict:
    """Épisodes et rejeu du lot 0 d'un bras, garde différée sur toutes les actions ; passes uniques du repère en
    demi-précision sur les plus longues transcriptions ; noyaux permis consignés (RV-13)."""
    from ..harnais.modeles import noyaux_attention_permis

    chrono: dict = {}
    depart = time.perf_counter()
    with noyau(bras):
        permis = noyaux_attention_permis() if torch.cuda.is_available() else None
        fiches, _, cn = jouer_pilote(modele, fmt, plan, {e: generateur(g[e]) for e in ids_episodes}, config,
                                     garder_vecteurs=False, echeance=echeance, garde="differee",
                                     exiger_controle_negatif=False, chrono=chrono,
                                     transcriptions_de=frozenset(ids_episodes))
        duree = time.perf_counter() - depart
        lot0 = plan[:config["lot"]]
        rejeu, _, _ = jouer_pilote(modele, fmt, lot0, {e: generateur(g[e]) for e, _ in lot0}, config,
                                   garder_vecteurs=False, echeance=echeance, garde="differee",
                                   exiger_controle_negatif=False)
        repere_ids = plus_longues_transcriptions(fiches, int(config["transcriptions_repere"]), bras)
        acts_bas = _activations(modele, repere_ids, config["couches"])
    premier = {e: v for e, v in _empreintes_rejeu(fiches).items() if e in dict(lot0)}
    return {"fiches": fiches, "controle_negatif": cn, "chrono": chrono, "duree_s": duree, "noyaux_permis": permis,
            "rejeu_identique": _empreintes_rejeu(rejeu) == premier, "repere_ids": repere_ids, "acts_bas": acts_bas,
            "memoire_pic_gio": (torch.cuda.max_memory_allocated() / 2 ** 30) if torch.cuda.is_available() else None}


def _phase_chemin(reference, fmt, plan, g, config, echeance) -> dict:
    """Logique de la génération remplie au noyau par défaut, en simple précision, sur le lot 0 (RV-3) : passage sain,
    puis défaut D1 injecté (décalage des positions), mêmes réglages que T0.4 v3 (garde sur le maximum)."""
    lot0 = plan[:config["lot"]]
    c = dict(config, T=config["chemin"]["T"], statistique_equivalence="max",
             tolerance_equivalence=config["chemin"]["tolerance"])
    c_pc = dict(c, T=config["controle_positif"]["T"])
    with noyau("defaut"):
        sain, _, cn = jouer_pilote(reference, fmt, lot0, {e: generateur(g[f"chemin/{e}"]) for e, _ in lot0}, c,
                                   garder_vecteurs=False, echeance=echeance, garde="differee",
                                   exiger_controle_negatif=False)
        d1, _, _ = jouer_pilote(reference, fmt, lot0, {e: generateur(g[f"controle-positif/{e}"]) for e, _ in lot0},
                                c_pc, garder_vecteurs=False, echeance=echeance, garde="differee",
                                exiger_controle_negatif=False,
                                decalage_positions=int(config["controle_positif"]["decalage_positions"]))
    return {"lecture": lire_chemin(sain, cn, d1, config), "controle_negatif": cn,
            "fiches_sain": sain, "fiches_d1": d1}


def _executer_apres_manifeste(config, racine, chemin_m, manifeste, plan, ids_episodes, etat, domaine_enonces,
                              debut) -> dict:
    g = manifeste["graines"]
    from ..harnais.modeles import regler_determinisme

    reel = config["mode"] == "reel"
    reglages = regler_determinisme(config["fils"], "cuda" if reel else "cpu")
    memoire_carte = exiger_memoire_carte(config["memoire_carte_min_gio"]) if reel else None
    carte = exiger_carte_a100(torch.cuda.get_device_name(0)) if reel else None
    graine_jouet = graine_entiere(g["modele-jouet"])
    echeance_run = debut + float(config["duree_max_s"])
    resultats = {}
    for bras in config["bras"]:
        etat["etape"] = f"bras {bras}"
        echeance = min(echeance_run, time.perf_counter() + float(config["duree_max_bras_s"]))
        modele, fmt = _charger_bas(config, graine_jouet)
        if reel:
            torch.cuda.reset_peak_memory_stats()
        try:
            r = _jouer_bras(modele, fmt, bras, plan, ids_episodes, g, config, echeance)
        except torch.cuda.OutOfMemoryError as exc:  # panne de mémoire signalée : consignée, bras non conforme
            del modele
            _liberer()
            lecture = lire_bras({}, {}, None, None, config, panne=f"mémoire : {exc}"[:500])
            ecrire_resultat(racine, chemin_m, f"lecture-{bras}", {"lecture": lecture})
            etat["lectures"][bras] = lecture
            continue
        del modele
        _liberer()
        mesures = domaine_et_garde(r["fiches"])
        projetee = duree_projetee_pilote(r["chrono"], len(ids_episodes))
        ecrire_resultat(racine, chemin_m, f"episodes-{bras}", {"fiches": r["fiches"]})
        ecrire_resultat(racine, chemin_m, f"mesures-{bras}", {
            "mesures": mesures, "controle_negatif": r["controle_negatif"], "chrono": r["chrono"],
            "duree_s": r["duree_s"], "rejeu_identique": r["rejeu_identique"], "noyaux_permis": r["noyaux_permis"],
            "memoire_pic_gio": r["memoire_pic_gio"], "duree_projetee_episodes_pilote_s": projetee,
            "repere_transcriptions": {k: len(v) for k, v in r["repere_ids"].items()}})
        exiger_mesures_reelles(reel, r["memoire_pic_gio"], projetee, bras)    # R7, R8 jamais lues sans mesure (W-14)
        # repère (et, pour « defaut », phase « chemin ») en simple précision, dès la fin du bras (RV-1)
        etat["etape"] = f"repère et chemin {bras}"
        exiger_echeance_bras(echeance, bras)           # l'échéance du bras borne aussi le repère et le chemin (W-3)
        reference = None
        try:
            reference = _modele_reference(config, graine_jouet)
            with noyau("math"):
                acts_ref = _activations(reference, r["repere_ids"], config["couches"])
            repere = statistiques_repere(r["acts_bas"], acts_ref, config["couches"])
            chemin = _phase_chemin(reference, fmt, plan, g, config, echeance) if bras == "defaut" else None
        except torch.cuda.OutOfMemoryError as exc:  # panne de mémoire pendant le repère ou le chemin (W-2) : comme
            reference = None                        # pendant le bras : consignée, bras non conforme, l'autre se joue
            _liberer()
            lecture = lire_bras({}, {}, None, None, config,
                                panne=f"mémoire pendant le repère ou la phase « chemin » : {exc}"[:500])
            ecrire_resultat(racine, chemin_m, f"lecture-{bras}", {"lecture": lecture})
            etat["lectures"][bras] = lecture
            continue
        del reference
        _liberer()
        zone = garde_zone_generee(r["fiches"], config["tolerance_equivalence"], config["positions_min_controle_negatif"])
        audit = audit_symetrie(r["fiches"], repere)
        lecture = lire_bras(mesures, r["controle_negatif"], repere, r["rejeu_identique"], config, zone_generee=zone,
                            audit=audit, chemin=chemin["lecture"] if chemin else None, bras=bras,
                            memoire_pic_gio=r["memoire_pic_gio"], duree_projetee_s=projetee)
        sortie = {"lecture": lecture, "repere": repere, "zone_generee": zone, "audit": audit,
                  "chemin": None if chemin is None else {"lecture": chemin["lecture"],
                                                         "controle_negatif": chemin["controle_negatif"]}}
        ecrire_resultat(racine, chemin_m, f"lecture-{bras}", sortie)
        if chemin is not None:
            ecrire_resultat(racine, chemin_m, "chemin-defaut", {"sain": chemin["fiches_sain"], "d1": chemin["fiches_d1"]})
        etat["lectures"][bras] = lecture
        resultats[bras] = {"mesures": mesures, "repere": repere, "zone_generee": zone, "audit": audit,
                           "controle_negatif": r["controle_negatif"], "rejeu_identique": r["rejeu_identique"],
                           "memoire_pic_gio": r["memoire_pic_gio"], "duree_projetee_episodes_pilote_s": projetee,
                           "longueur_remplie_max": r["chrono"].get("longueur_remplie_max"),
                           "chemin": None if chemin is None else chemin["lecture"]}
    etat["etape"] = "résumé"
    noyau_retenu, proposition = choisir_noyau(etat["lectures"])
    resume = {"lectures": etat["lectures"], "noyau_retenu": noyau_retenu, "noeud": noyau_retenu is None,
              "proposition_au_noeud": proposition, "reglages": reglages, "memoire_carte_gio": memoire_carte,
              "carte": carte,
              "domaine_enonces": domaine_enonces,
              "reserves": ([] if domaine_enonces["couvre_le_pilote"] else
                           ["énoncés de la revalidation plus courts que le plus long énoncé du pilote (RV-5)"])
              + [f"rapport au repère au-dessus de {config['rho_max']} au noyau « {b} »"
                 for b, x in etat["lectures"].items() if x.get("reserve_rho")],
              "bras": resultats}
    ecrire_resultat(racine, chemin_m, "resume", resume)
    return resume


def _signal_term(signum, frame):
    raise GardeArret("signal TERM reçu (délai externe du run ou plafond de l'amorce) : arrêt consigné")


def _main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(prog=COMMANDE)
    ap.add_argument("--config", required=True)
    ap.add_argument("--entrainement", required=True)
    ap.add_argument("--evaluation", required=True)
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--prereg")
    a = ap.parse_args(argv)
    signal.signal(signal.SIGTERM, _signal_term)
    verifier(a.config)
    config = json.loads(Path(a.config).read_text(encoding="utf-8"))
    resume = executer(config, Path("."), a.run_id, a.prereg, a.entrainement, a.evaluation)
    print(json.dumps({"noyau_retenu": resume["noyau_retenu"], "lectures": resume["lectures"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
