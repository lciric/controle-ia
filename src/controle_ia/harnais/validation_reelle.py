"""Validation du harnais sur modèle réel (T0.4 ; porte G0, critère 1), et sa répétition sur modèle jouet.

Sur la machine de calcul, après GO (jamais sans) :
    PYTHONPATH=src python -m controle_ia.harnais.validation_reelle --revision <commit> --prereg <préenregistrement> \
        --sortie-tests <sortie de pytest sur l'instance>
    … la même commande, plus --rejeu-de <run A>, pour le second processus.
Répétition sur processeur, modèle jouet, non décisive :
    PYTHONPATH=src python -m controle_ia.harnais.validation_reelle --repetition-jouet [--rejeu-de <run A>]

Phases, dans un seul processus (version 3 : préenregistrement T0.4 v3, N-010 et N-011, option a) :
1. logique, double précision (poids convertis sans perte, normalisations RMS en double précision), noyau
   d'attention « math » : un lot au régime de production ; contrôle du format ; empreintes des fichiers du
   modèle ; échantillon d'équivalence sur des lignes qui ne sont pas en tête de lot ; tolérance 1e-4 ;
   puis son contrôle positif : le défaut D1 (positions décodées décalées) est injecté dans la génération, la garde
   d'équivalence doit le voir au seuil de la phase ; gardes de la phase, puis du contrôle positif ;
2. chemin de production, simple précision, noyau d'attention de production, même régime de lots et de
   remplissage : contrôle strict du chemin que la production emprunte, avec son propre contrôle positif (D1) ;
3. production, demi-précision, noyau d'attention fixé : épisodes en lots ; équivalence sur une ligne par lot,
   lue sur le 99e centile des écarts par jeton (tolérance de production) ; politique de stockage (codage
   bfloat16-bits) ; relecture du disque bit à bit ; rejeu du premier lot dans le processus ; repère de précision
   (passe unique en demi contre double précision) ;
4. débit : génération seule, sans arrêt anticipé, pour plusieurs tailles de lot, au noyau de production.
Dans les phases 1 à 3, tous les écarts sont consignés avant que les gardes s'appliquent : un arrêt laisse les
profils complets. Contrôle négatif : décalé d'un jeton, dans la zone générée seulement, sur la grandeur que lit la
garde de sa phase (maximum, ou 99e centile en production).
Le rejeu dans un second processus est un second lancement à la même entropie (`--rejeu-de`) : configuration,
graines et code sont comparés à ceux du premier avant tout calcul ; puis tout est rejoué et comparé au bit
près (empreintes, logits, captures, fichiers), comparaison scellée.

Les gros tableaux (npz) vont dans `donnees/<run>/` (hors git, scellés sur place) ; leurs empreintes sont
dans les résultats scellés de `diag/<run>/`. Une fois le manifeste créé, tout arrêt (garde, panne, signal
TERM du délai externe du run ou du plafond de l'amorce) laisse un `arret.json` scellé, puis se propage : aucun
repli silencieux (R5). Les gardes d'avant le manifeste (liste blanche, révision, mémoire vive, code importé, arbre
gelé au commit cité, citations, rejeu incompatible, sortie des tests en mode décisif) ne laissent que leur message
sur la sortie d'erreur.
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import importlib.metadata
import json
import re
import signal
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import torch

from ..gardes import GardeArret
from ..manifeste import (config_canonique, creer_manifeste, ecrire_resultat, generateur, lire_manifeste,
                         verifier_resultat)
from . import politique as P
from .activations import couches_par_defaut, ecarts_par_jeton, passe_unique
from .episode import (EnvironnementJouet, bilan_controle_negatif, empreinte_episode, empreinte_tableaux,
                      exiger_controle_negatif_phase, exiger_gardes, generer_lot, jouer_episodes)
from .formats import FormatChat, verifier_format
from .modeles import (charger_modele, empreinte_poids, empreintes_fichiers_modele, exiger_modele_autorise,
                      fins_du_modele, modele_jouet, normalisations_en_double, noyaux_attention_permis,
                      regler_determinisme, tokeniseur_caracteres_chat)
from .stockage import estimer

COMMIT_CITE = re.compile(r"Commit du code d'analyse : `([0-9a-f]{40})`")
# chemins gelés par le commit cité : tout l'arbre (code, tests, scripts, dépendances, configuration de pytest et de
# git, gardes de .claude/…), sauf les dossiers documentaires et les sorties des runs
CHEMINS_GELES = (".", ":(exclude)prereg", ":(exclude)brouillons", ":(exclude)registres", ":(exclude)docs",
                 ":(exclude)diag", ":(exclude)runs", ":(exclude)donnees", ":(exclude)livrables", ":(exclude)papiers",
                 ":(exclude)traces", ":(exclude)CLAUDE.md")
REVISION_CITEE = re.compile(r"Révision du modèle : `([0-9a-f]{40})`")
ENTROPIE_CITEE = re.compile(r"Entropie : `([0-9]+)`")

PHASES_COMPAREES = ("logique", "chemin", "production")        # phases à garde d'équivalence (version 3)
SONDES = [{"nom": f"lineaire-{a}-{c}", "couche": c, "agregation": a}
          for c in ("precoce", "mediane", "tardive") for a in ("max", "attention")]

CONFIG_REELLE = {
    "objet": "validation du harnais sur modèle réel (T0.4 ; porte G0, critère 1) ; aucune mesure de fond",
    "modele": "meta-llama/Llama-3.1-8B-Instruct", "attention": "sdpa", "appareil": "cuda", "fils": 1,
    "memoire_vive_min_go": 96,                # double précision : conversion sur le processeur (≈ 80 Go au pic)
    "variables_gabarit": {"date_string": "26 Jul 2024"},
    "format": {"consigne": "Tu es l'agent 0. Propose une étape d'expérience, en une phrase.",
               "observations": ["Pas 0. Journal : ", "Pas 1. Journal : 0@0: Mesurer la température.",
                                "Pas 2. Journal : 0@1: Répéter la mesure."],
               "reponses": ["Je propose de mesurer la température.", "Je répète la mesure.",
                            "Je compare les deux mesures."],
               "texte_attendu_ouverture": "Today Date: 26 Jul 2024"},
    "logique": {"dtype": "float64", "noyau_attention": "math", "episodes": 8, "N": 2, "T": 10, "max_nouveaux": 256,
                "taille_lot": 8, "temperature": 1.0, "tolerance": 1e-4, "statistique": "max",
                "episodes_equivalence": [1, 6]},
    # chemin de production (version 3, N-011 option a) : simple précision, noyau et régime de production ; seuil entre
    # l'arrondi de la simple précision (1,27e-4 au plus dans la v1, noyau « math ») et l'effet de D1 (5,7e-2 au moins
    # dans la v2) : environ vingt fois chacun
    "chemin": {"dtype": "float32", "noyau_attention": "math", "episodes": 8, "N": 2, "T": 10, "max_nouveaux": 256,
               "taille_lot": 8, "temperature": 1.0, "tolerance": 3e-3, "statistique": "max",
               "episodes_equivalence": [1, 6]},
    # production (version 3) : noyau fixé (« math », le même qu'au chemin) ; garde sur le 99e centile des écarts par
    # jeton, par action et par couche ; seuil fondé sur le repère de la v2 (99e centile 0,087 au plus, deux calculs en
    # demi-précision) : 0,2 ; le maximum est rapporté sans seuil
    "production": {"dtype": "bfloat16", "noyau_attention": "math", "episodes": 16, "N": 2, "T": 10,
                   "max_nouveaux": 256, "taille_lot": 8, "temperature": 1.0, "tolerance": 0.2, "statistique": "q99",
                   "episodes_equivalence": [1, 14], "lots_rejeu_en_processus": [0]},
    "debit": {"tailles_lot": [1, 8, 32], "longueur_contexte": 2048, "max_nouveaux": 128},
    "politique": {"episodes_par_jeton": [1, 14], "vecteurs_par_action": ["max"], "sondes": SONDES},
    "controle_negatif": {"positions_min": 4, "actions_min": 10, "fraction_min": 0.95},
    # contrôle positif (versions 2 et 3) : le défaut D1 (positions décodées décalées de +1) est injecté dans la
    # génération des phases de logique et de chemin, rejouées sur T pas ; la garde d'équivalence doit le voir au seuil
    # de la phase
    "controle_positif": {"T": 5, "decalage_positions": 1, "positions_min": 4, "actions_min": 10, "fraction_min": 0.95},
    # double précision (version 2) : 64,2 Go de poids, plus le préremplissage d'un lot de 8 : quadratique en sa longueur
    # remplie, qui a atteint 2 329 jetons dans la v1 (≈ 104 Go au pic estimés) ; carte de 141 Go (H200)
    "memoire_carte_min_gio": 130,
    "tests_attendus": 206,                    # suite complète au commit cité, tous réussis (P0)
    "projection": {"episodes": 2000},
    "limite_s": 9000,
}

CONFIG_REPETITION = dict(
    CONFIG_REELLE,
    objet="répétition de la validation sur modèle jouet à poids aléatoires (processeur) ; non décisive",
    modele="jouet", appareil="cpu", memoire_vive_min_go=0,
    modele_jouet={"couches": 4, "largeur": 32, "tetes": 4, "tetes_cle_valeur": 2, "intermediaire": 64},
    format=dict(CONFIG_REELLE["format"], texte_attendu_ouverture=None),
    logique=dict(CONFIG_REELLE["logique"], episodes=4, N=2, T=3, max_nouveaux=16, taille_lot=4,
                 episodes_equivalence=[1, 2]),
    # seuil du chemin propre au jouet : son arrondi en simple précision (≈ 6e-7) et l'effet de D1 (≈ 2e-4) sont tous
    # deux bien plus petits que sur le modèle réel ; 1e-5 les sépare d'environ vingt fois chacun
    # noyau « defaut » au jouet seulement : sur processeur, en demi-précision et au noyau « math », génération et passe
    # unique y coïncident au bit près (la répétition déclencherait l'audit de symétrie sans rien éprouver)
    chemin=dict(CONFIG_REELLE["chemin"], episodes=4, N=2, T=3, max_nouveaux=16, taille_lot=4, tolerance=1e-5,
                noyau_attention="defaut", episodes_equivalence=[1, 2]),
    production=dict(CONFIG_REELLE["production"], episodes=4, N=2, T=3, max_nouveaux=16, taille_lot=2,
                    noyau_attention="defaut", episodes_equivalence=[1, 2]),
    politique=dict(CONFIG_REELLE["politique"], episodes_par_jeton=[1, 2]),
    debit={"tailles_lot": [1, 2, 4], "longueur_contexte": 48, "max_nouveaux": 8},
    controle_negatif={"positions_min": 4, "actions_min": 4, "fraction_min": 0.95},
    # T du contrôle positif différent de celui de la logique (contre-lecture 1 de la v2, V-2 : une confusion se voit)
    controle_positif={"T": 2, "decalage_positions": 1, "positions_min": 4, "actions_min": 4, "fraction_min": 0.95},
    memoire_carte_min_gio=0,
    limite_s=900,
)


# ---------------------------------------------------------------- configuration et graines

def valider_config(config: dict, revision: str | None) -> None:
    if config["modele"] != "jouet":
        exiger_modele_autorise(config["modele"], revision)
    for phase in PHASES_COMPAREES:
        c = config[phase]
        if min(c["episodes"], c["N"], c["T"], c["max_nouveaux"], c["taille_lot"]) < 1:
            raise GardeArret(f"{phase} : tailles ≥ 1 attendues")
        if not c["tolerance"] > 0:
            raise GardeArret(f"{phase} : tolérance {c['tolerance']} ≤ 0")
        if not set(c["episodes_equivalence"]) <= set(range(c["episodes"])) or not c["episodes_equivalence"]:
            raise GardeArret(f"{phase} : épisodes d'équivalence {c['episodes_equivalence']} hors de la phase")
        if c["noyau_attention"] not in ("math", "defaut"):
            raise GardeArret(f"{phase} : noyau d'attention {c['noyau_attention']!r} inconnu")
        if c["statistique"] not in ("max", "q99"):
            raise GardeArret(f"{phase} : statistique {c['statistique']!r} inconnue")
    if config["logique"]["dtype"] != "float64" or config["logique"]["statistique"] != "max":
        raise GardeArret("la phase de logique se fait en double précision, sur le maximum (versions 2 et 3)")
    if config["chemin"]["dtype"] != "float32" or config["chemin"]["statistique"] != "max":
        raise GardeArret("la phase de chemin se fait en simple précision, sur le maximum (version 3)")
    prod_, chem = config["production"], config["chemin"]
    if prod_["noyau_attention"] != chem["noyau_attention"] or (config["modele"] != "jouet"
                                                              and prod_["noyau_attention"] == "defaut"):
        raise GardeArret("le noyau d'attention de production est fixé, et le chemin l'emprunte (version 3)")
    if prod_["statistique"] != "q99":
        raise GardeArret("la garde de production lit le 99e centile (version 3, N-011)")
    cp = config["controle_positif"]
    if (cp["T"] < 1 or cp["T"] > min(config["logique"]["T"], chem["T"]) or cp["decalage_positions"] == 0
            or cp["positions_min"] < 1 or cp["actions_min"] < 1 or not 0 < cp["fraction_min"] <= 1):
        raise GardeArret(f"contrôle positif : réglage {cp} invalide")
    prod = config["production"]
    n_lots = -(-prod["episodes"] // prod["taille_lot"])
    if not set(prod["lots_rejeu_en_processus"]) <= set(range(n_lots)):
        raise GardeArret(f"lots de rejeu {prod['lots_rejeu_en_processus']} hors de [0, {n_lots}[")
    n_couches = config.get("modele_jouet", {}).get("couches", 32)
    P.valider_politique(config["politique"], n_couches, prod["episodes"])
    if max(config["debit"]["tailles_lot"]) > prod["episodes"] * prod["N"]:
        raise GardeArret("débit : plus de lignes que de transcriptions de production")
    cn = config["controle_negatif"]
    if cn["positions_min"] < 1 or cn["actions_min"] < 1 or not 0 < cn["fraction_min"] <= 1:
        raise GardeArret(f"contrôle négatif : réglage {cn} invalide")


def taches(config: dict) -> list[str]:
    t = ["modele-jouet"] if config["modele"] == "jouet" else []
    t += [f"sonde-{d['nom']}" for d in config["politique"]["sondes"]]
    for phase in PHASES_COMPAREES:
        c = config[phase]
        t += [f"{phase}/episode-{k}/action-{i}-{p}" for k in range(c["episodes"]) for p in range(c["T"])
              for i in range(c["N"])]
    cp = config["controle_positif"]
    for phase, tache_pc in (("logique", "controle-positif"), ("chemin", "controle-positif-chemin")):
        c = config[phase]
        t += [f"{tache_pc}/episode-{k}/action-{i}-{p}" for k in range(c["episodes"]) for p in range(cp["T"])
              for i in range(c["N"])]
    t += [f"debit/ligne-{r}" for r in range(max(config["debit"]["tailles_lot"]))]
    return t


def graine_entiere(graine: dict) -> int:
    return int(generateur(graine).integers(0, 2 ** 63 - 1))


# ---------------------------------------------------------------- gardes de lancement (avant le manifeste)

def exiger_code_cite(racine: Path, prereg: Path) -> str:
    """Garde : l'arbre gelé (`CHEMINS_GELES` : tout sauf les dossiers documentaires et les sorties) est, au
    lancement, celui du commit cité par le préenregistrement."""
    m = COMMIT_CITE.search(prereg.read_text(encoding="utf-8"))
    if not m:
        raise GardeArret(f"{prereg} ne cite pas le commit du code d'analyse (40 caractères hexadécimaux)")
    r = subprocess.run(["git", "-C", str(racine), "diff", "--quiet", m.group(1), "HEAD", "--", *CHEMINS_GELES],
                       capture_output=True, text=True)
    if r.returncode == 1:
        raise GardeArret(f"arbre gelé (code, tests, scripts, dépendances, configuration) modifié depuis le commit "
                         f"cité {m.group(1)[:12]}")
    if r.returncode != 0:
        raise GardeArret(f"comparaison au commit cité {m.group(1)[:12]} impossible : {r.stderr.strip()}")
    return m.group(1)


def exiger_citations(prereg: Path, revision: str | None, entropie: int | None) -> int:
    """Garde : la révision du modèle et l'entropie sont celles que cite le préenregistrement (rien de libre au
    lancement). Renvoie l'entropie citée."""
    texte = prereg.read_text(encoding="utf-8")
    r, e = REVISION_CITEE.search(texte), ENTROPIE_CITEE.search(texte)
    if not r or not e:
        raise GardeArret(f"{prereg} ne cite pas la révision du modèle ou l'entropie")
    if revision != r.group(1):
        raise GardeArret(f"révision {revision} ≠ révision citée {r.group(1)}")
    if entropie is not None and entropie != int(e.group(1)):
        raise GardeArret(f"entropie {entropie} ≠ entropie citée {e.group(1)}")
    return int(e.group(1))


def exiger_code_importe_sous(racine: Path) -> None:
    import controle_ia

    if (racine / "src").resolve() not in Path(controle_ia.__file__).resolve().parents:
        raise GardeArret("code importé hors de la racine du dépôt : lancer depuis la racine")


def plafonds_cgroup(proc_cgroup: str = "/proc/self/cgroup", racine: str = "/sys/fs/cgroup") -> list[str]:
    """Fichiers de plafond mémoire du groupe de contrôle du processus et de tous ses ancêtres (v2 : ligne « 0:: » et
    memory.max ; v1 : contrôleur « memory » et memory.limit_in_bytes)."""
    try:
        lignes = Path(proc_cgroup).read_text().splitlines()
    except OSError:
        return []
    fichiers = []
    for ligne in lignes:
        morceaux = ligne.split(":", 2)
        if len(morceaux) != 3:
            continue
        _, controleurs, chemin = morceaux
        if controleurs == "":
            base, nom = Path(racine), "memory.max"
        elif "memory" in controleurs.split(","):
            base, nom = Path(racine) / "memory", "memory.limit_in_bytes"
        else:
            continue
        parties = [x for x in chemin.split("/") if x]
        for k in range(len(parties), -1, -1):
            fichiers.append(str(base.joinpath(*parties[:k], nom)))
    return fichiers


def exiger_memoire_vive(min_go: float, meminfo: str = "/proc/meminfo", cgroups=None) -> dict | None:
    """Garde : assez de mémoire vive pour charger le modèle (un dépassement tue le processus sans trace). Mémoire
    effective = le plus petit de MemTotal (souvent l'hôte, dans un conteneur) et des plafonds du groupe de contrôle
    du processus et de ses ancêtres."""
    if not min_go:
        return None
    try:
        ligne = next(x for x in Path(meminfo).read_text().splitlines() if x.startswith("MemTotal:"))
    except (OSError, StopIteration):
        raise GardeArret(f"mémoire vive illisible ({meminfo}) : {min_go} Go exigés") from None
    total = int(ligne.split()[1]) * 1024 / 1e9
    plafond = None
    for c in (plafonds_cgroup() if cgroups is None else cgroups):
        try:
            v = Path(c).read_text().strip()
        except OSError:
            continue
        if v.isdigit() and int(v) < 2 ** 60:
            plafond = int(v) / 1e9 if plafond is None else min(plafond, int(v) / 1e9)
    effective = min(total, plafond) if plafond is not None else total
    if effective < min_go:
        raise GardeArret(f"mémoire vive effective {effective:.1f} Go < {min_go} Go exigés (MemTotal {total:.1f} Go, "
                         f"plafond du conteneur {plafond if plafond is None else round(plafond, 1)} Go)")
    return {"memtotal_go": round(total, 1), "plafond_conteneur_go": None if plafond is None else round(plafond, 1),
            "effective_go": round(effective, 1)}


def exiger_memoire_carte(min_gio: float, total_octets: int | None = None) -> float | None:
    """Garde : la carte a assez de mémoire (logique en double précision : jusqu'à environ 129 Go estimés au pire cas,
    note `docs/notes/memoire-double-precision-T0.4-v1.md`)."""
    if not min_gio:
        return None
    if total_octets is None:
        if not torch.cuda.is_available():
            raise GardeArret(f"carte graphique indisponible : {min_gio} Gio exigés")
        total_octets = torch.cuda.get_device_properties(0).total_memory
    gio = total_octets / 2 ** 30
    if gio < min_gio:
        raise GardeArret(f"mémoire de la carte {gio:.1f} Gio < {min_gio} Gio exigés")
    return round(gio, 2)


def exiger_rejeu_compatible(racine: Path, rejeu_de: str, config: dict) -> int:
    """Garde du run B, avant tout calcul : même configuration (révision comprise) et même code que le run A.
    Renvoie l'entropie du run A."""
    m_a, _ = lire_manifeste(racine / "runs" / rejeu_de / "manifeste.json")
    if hashlib.sha256(config_canonique(config)).hexdigest() != m_a["config_sha256"]:
        raise GardeArret(f"rejeu de {rejeu_de} : configuration (ou révision) différente de celle du run A")
    try:
        verifier_resultat(racine, racine / "diag" / rejeu_de / "resume.json")
    except (GardeArret, OSError) as e:
        raise GardeArret(f"rejeu de {rejeu_de} : résumé du run A absent ou altéré ({e})") from None
    r = subprocess.run(["git", "-C", str(racine), "diff", "--quiet", m_a["commit"], "HEAD", "--", *CHEMINS_GELES],
                       capture_output=True, text=True)
    if r.returncode != 0:
        raise GardeArret(f"rejeu de {rejeu_de} : arbre gelé (code, tests, scripts, dépendances, configuration) "
                         f"différent de celui du run A ({m_a['commit'][:12]})")
    return int(next(iter(m_a["graines"].values()))["entropie"])


# ---------------------------------------------------------------- modèle, format, épisodes

def charger(config: dict, revision: str | None, dtype: str, graines: dict):
    if config["modele"] == "jouet":
        tok = tokeniseur_caracteres_chat()
        m = modele_jouet(graine_entiere(graines["modele-jouet"]), len(tok), **config["modele_jouet"])
        m = m.to(getattr(torch, dtype))
        if dtype == "float64":
            normalisations_en_double(m)
        return m.eval(), tok
    return charger_modele(config["modele"], revision, dtype, config["appareil"], config["attention"])


def format_du_modele(modele, tok, config: dict) -> tuple[FormatChat, dict]:
    """Format de conversation (jetons d'arrêt : ceux du modèle plus le jeton qui ferme un tour du gabarit) et sa
    garde : transcription incrémentale = gabarit complet ; texte attendu dans l'ouverture (date figée)."""
    fmt = FormatChat(tok, variables=config["variables_gabarit"])
    fmt.fins = fins_du_modele(modele, tok) | {fmt._pieces(("x", "y"))["cloture"][0]}
    f = config["format"]
    controle = verifier_format(fmt, f["consigne"], f["observations"], f["reponses"])
    ouverture = tok.decode(fmt.ouverture(f["consigne"], f["observations"][0]))
    attendu = f.get("texte_attendu_ouverture")
    if attendu and attendu not in ouverture:
        raise GardeArret(f"ouverture sans {attendu!r} : le gabarit ne lit pas les variables figées")
    return fmt, {**controle, "fins": sorted(fmt.fins), "ouverture": ouverture,
                 "gabarit_sha256": hashlib.sha256(str(tok.chat_template).encode("utf-8")).hexdigest()}


def noyau(nom: str):
    if nom == "math":
        from torch.nn.attention import SDPBackend, sdpa_kernel

        return sdpa_kernel(SDPBackend.MATH)
    return contextlib.nullcontext()


def jouer_phase(modele, fmt, c: dict, graines: dict, phase: str, couches: list[int], lots=None, chrono=None,
                echeance=None, decalage_positions: int = 0) -> tuple[list, list]:
    """Joue les épisodes d'une phase par lots consécutifs (plan fixé par la configuration), gardes différées ;
    `decalage_positions` injecte le défaut D1 (contrôle positif seulement)."""
    E, B = c["episodes"], c["taille_lot"]
    plan = [list(range(j, min(j + B, E))) for j in range(0, E, B)]
    sorties = []
    with noyau(c["noyau_attention"]):
        for j, lot in enumerate(plan):
            if lots is not None and j not in lots:
                continue
            g = [{(i, p): graine_entiere(graines[f"{phase}/episode-{k}/action-{i}-{p}"])
                  for p in range(c["T"]) for i in range(c["N"])} for k in lot]
            echantillon = {(b, i, p) for b, k in enumerate(lot) if k in c["episodes_equivalence"]
                           for p in range(c["T"]) for i in range(c["N"])}
            sorties += jouer_episodes(modele, fmt, EnvironnementJouet(), [f"episode-{k}" for k in lot], c["N"], c["T"],
                                      g, couches, c["max_nouveaux"], c["temperature"], echantillon, c["tolerance"],
                                      chrono=chrono, garde="differee", echeance=echeance, empreinte_logits=True,
                                      decalage_positions=decalage_positions, statistique=c.get("statistique", "max"))
    return sorties, plan


def empreintes_episode(ep, acts, rapport, politique=None, couches=None, sondes=None) -> tuple[dict, dict, dict]:
    """Empreintes d'un épisode : trajectoire, activations par jeton, logits de chaque pas ; avec la politique :
    vecteurs d'action et scores (renvoyés aussi)."""
    emp = {**empreinte_episode(ep, acts),
           "logits": hashlib.sha256(json.dumps(rapport["empreintes_logits"], sort_keys=True).encode()).hexdigest()}
    v = s = {}
    if politique is not None:
        v, s = P.calculer_en_ligne(politique, ep, acts, couches, sondes)
        emp.update({"vecteurs": empreinte_tableaux(v), "scores": empreinte_tableaux(s)})
    return emp, v, s


def _maximum(valeurs) -> float | None:
    """Maximum où un NaN compte comme +∞ (une valeur illisible n'est jamais « sous le seuil »)."""
    v = [float("inf") if x != x else x for x in valeurs]
    return max(v) if v else None


def bilan_phase(sorties, c: dict, cn: dict) -> dict:
    """Résumé d'une phase, sur les seules actions comparées : écarts (toutes positions, puis par zone), contrôle
    négatif de phase, couverture par ligne comparée, domaine observé, zéros par couche et par zone, sondes d'audit.
    `ecart_max` : maximum sur les actions et les couches du maximum par action ; `ecart_q99_max` : maximum sur les
    actions et les couches du 99e centile par action (grandeur de la garde de production, version 3)."""
    rapports = [r for _, _, r in sorties if r["ecarts"]]
    cles = [(r, cle) for r in rapports for cle in r["ecarts"]]
    ecarts = [e for r, cle in cles for e in r["ecarts"][cle].values()]
    ecarts_q99 = [e for r, cle in cles for e in r["ecarts_q99"][cle].values()]
    max_ctx = _maximum(p["contexte"]["max"] for r, cle in cles for p in r["profils"][cle].values()
                       if p["contexte"]["jetons"])
    max_gen = _maximum(p["generee"]["max"] for r, cle in cles for p in r["profils"][cle].values()
                       if p["generee"]["jetons"])
    couches = sorted({c_ for r, cle in cles for c_ in r["profils"][cle]}, key=str)
    zeros = {str(c_): {z: [sum(r["profils"][cle][c_][z].get("nuls", 0) for r, cle in cles),
                           sum(r["profils"][cle][c_][z]["jetons"] for r, cle in cles)] for z in ("contexte", "generee")}
             for c_ in couches}
    lignes = [r["lignes"][cle] for r, cle in cles]
    generes = [r["positions_capturees"][cle] - r["longueurs_contexte"][cle] for r, cle in cles]
    sondes = [r["sondes"][cle] for r, cle in cles]
    return {
        "tolerance": c["tolerance"],
        "statistique": c.get("statistique", "max"),
        "actions_comparees": len(cles),
        "ecart_max": _maximum(ecarts),
        "ecart_q99_max": _maximum(ecarts_q99),
        "ecart_non_fini": any(x != x or x == float("inf") for x in ecarts),
        "max_contexte": max_ctx, "max_zone_generee": max_gen,
        "controle_negatif": bilan_controle_negatif(rapports, cn["positions_min"]),
        "couverture": {"actions_remplies": sum(x["remplissage"] > 0 for x in lignes),
                       "actions_finies_avant": sum(bool(x["finie_avant"]) for x in lignes),
                       "positions_generees_comparees": sum(generes),
                       "lignes_echantillon": sorted({x["ligne"] for x in lignes})},
        "domaine": {"contexte_max": max((r["longueurs_contexte"][cle] for r, cle in cles), default=0),
                    "generes_relus_max": max(generes, default=0),
                    "taille_lot": max((x["taille_lot"] for x in lignes), default=0)},
        "zeros": zeros,
        "sondes_audit": {"tableaux_distincts": all(x["tableaux_distincts"] for x in sondes),
                         "ulp_vu": all(x["ulp_vu"] for x in sondes)},
    }


def bilan_controle_positif(sorties, c: dict, cp: dict) -> dict:
    """Contrôle positif (défaut D1 injecté). Une action comparée est comparable si sa zone générée compte au moins
    `positions_min` positions à chaque couche ; elle est vue si, à chaque couche, le maximum de l'écart dans la zone
    générée dépasse la tolérance de sa phase (logique ou chemin). Un maximum illisible (NaN) ne compte jamais comme vu.
    Descriptif (R4) : maximum du contexte des actions comparables, que D1 ne touche pas (attendu au niveau de P2)."""
    comparables, vus, courtes, manques, minimum = 0, 0, 0, [], float("inf")
    contextes = []
    for ep, _, r in sorties:
        for cle in r["ecarts"]:
            zones = [p["generee"] for p in r["profils"][cle].values()]
            if any(z["jetons"] < cp["positions_min"] for z in zones):
                courtes += 1
                continue
            comparables += 1
            contextes += [p["contexte"]["max"] for p in r["profils"][cle].values() if p["contexte"]["jetons"]]
            m = min(float("-inf") if z["max"] != z["max"] else z["max"] for z in zones)
            minimum = min(minimum, m)
            if m > c["tolerance"]:
                vus += 1
            else:
                manques.append(f"{ep.identifiant}:{cle}")
    return {"tolerance": c["tolerance"], "comparables": comparables, "vus": vus, "courtes": courtes, "manques": manques,
            "fraction": vus / comparables if comparables else None,
            "min_des_maxima": minimum if comparables else None, "positions_min": cp["positions_min"],
            "max_contexte": _maximum(contextes)}


def exiger_controle_positif(bilan: dict, cp: dict, quoi: str) -> None:
    """Garde : le défaut D1 injecté est vu par la garde d'équivalence pour au moins `fraction_min` des actions
    comparables. Sous `actions_min` actions comparables, rien ne se juge (lecture « non concluant »)."""
    if bilan["comparables"] < cp["actions_min"]:
        return
    if not bilan["fraction"] >= cp["fraction_min"]:
        raise GardeArret(f"{quoi} : défaut D1 injecté non vu au seuil de sa phase ({bilan['tolerance']}) pour "
                         f"{len(bilan['manques'])} action(s) "
                         f"sur {bilan['comparables']} ({bilan['manques'][:10]})")


def appliquer_gardes(sorties, bilan: dict, phase: str, cn: dict) -> None:
    """Gardes de fin de phase : équivalence de chaque action comparée, puis contrôle négatif de la phase ; toutes les
    fautes d'équivalence sont nommées dans un seul arrêt."""
    fautes = []
    for ep, _, r in sorties:
        for cle in r["ecarts"]:
            try:
                exiger_gardes(r, cle, f"{phase}, {ep.identifiant}, action ({cle})")
            except GardeArret as e:
                fautes.append(str(e))
    if fautes:
        raise GardeArret(f"{phase} : {len(fautes)} faute(s) de garde ; " + " | ".join(fautes[:20]))
    exiger_controle_negatif_phase(bilan["controle_negatif"], cn["fraction_min"], cn["actions_min"], phase)


def debit(chrono: dict) -> dict:
    g, p = chrono.get("generation_s", 0.0), chrono.get("passe_unique_s", 0.0)
    return {**chrono, "jetons_generes_par_s": chrono.get("jetons_generes", 0) / g if g > 0 else None,
            "jetons_passe_unique_par_s": chrono.get("jetons_passe_unique", 0) / p if p > 0 else None}


def memoire_max_go() -> float | None:
    if not torch.cuda.is_available():
        return None
    return round(torch.cuda.max_memory_allocated() / 1e9, 3)


def liberer() -> None:
    """Après `del modele` chez l'appelant : rend la mémoire du processeur graphique, remet le pic à zéro."""
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
        torch.cuda.reset_peak_memory_stats()


def repere_precision(modele, references: list, couches: list[int]) -> dict:
    """Repère descriptif : écart par jeton entre la passe unique du modèle courant (demi-précision) et celle de la
    phase de logique (double précision, version 2), sur les mêmes transcriptions et aux mêmes positions. L'appelant
    fixe le noyau d'attention : celui de la production (version 3)."""
    par_couche: dict[int, list] = {c: [] for c in couches}
    for ep, acts_ref in references:
        for tr in ep.transcriptions:
            a16 = passe_unique(modele, tr.ids, couches)
            for c in couches:
                par_couche[c].append(ecarts_par_jeton(a16[c], acts_ref[tr.agent][c]))
    sortie = {}
    for c, morceaux in par_couche.items():
        e = np.concatenate(morceaux)
        sortie[c] = {"jetons": int(e.size), "q50": float(np.quantile(e, 0.5)), "q99": float(np.quantile(e, 0.99)),
                     "max": float(e.max())}
    return sortie


# ---------------------------------------------------------------- run

def executer(racine: str | Path, run_id: str, revision: str | None = None, entropie: int | None = None,
             config: dict | None = None, prereg: str | Path | None = None, rejeu_de: str | None = None,
             sortie_tests: str | Path | None = None, verifier_import: bool = True) -> dict:
    """`verifier_import=False` n'est permis qu'aux tests sur mini-dépôt ; la ligne de commande l'active toujours."""
    racine = Path(racine)
    config = config or CONFIG_REELLE
    depart = time.perf_counter()
    decisif = config["modele"] != "jouet"
    if decisif and (prereg is None or sortie_tests is None):
        raise GardeArret("validation sur modèle réel sans préenregistrement scellé ou sans sortie des tests de "
                         "l'instance : R1 et R5 interdisent de lancer")
    valider_config(config, revision)
    memoire = exiger_memoire_vive(config["memoire_vive_min_go"])
    if verifier_import:
        exiger_code_importe_sous(racine)
    commit_cite = exiger_code_cite(racine, Path(prereg)) if prereg is not None else None
    if prereg is not None:
        entropie = exiger_citations(Path(prereg), revision, entropie)
    config = dict(config, revision=revision)
    if rejeu_de is not None:
        entropie_a = exiger_rejeu_compatible(racine, rejeu_de, config)
        if entropie is not None and entropie != entropie_a:
            raise GardeArret(f"rejeu de {rejeu_de} : entropie {entropie} ≠ {entropie_a}")
        entropie = entropie_a
    tests = Path(sortie_tests).read_text(encoding="utf-8") if sortie_tests is not None else None
    if decisif and not tests_conformes(tests, config.get("tests_attendus")):
        raise GardeArret(f"P0 : la sortie des tests de l'instance ne finit pas par exactement {config.get('tests_attendus')} "
                         "tests réussis : aucun run")
    chemin_m, m = creer_manifeste(racine, run_id, config, taches(config), entropie=entropie, decisif=decisif,
                                  prereg=prereg, commande="python -m controle_ia.harnais.validation_reelle")
    donnees = racine / "donnees" / run_id
    echeance = depart + config["limite_s"]
    resume: dict = {"commit_cite": commit_cite, "memoire_vive_go": memoire}
    phase = "reglages"

    def temps():
        if time.perf_counter() > echeance:
            raise GardeArret(f"limite de durée de {config['limite_s']} s dépassée avant la phase {phase}")

    def phase_stricte(nom: str, nom_pc: str, tache_pc: str):
        """Phase stricte (logique en double précision ; chemin de production en simple précision, version 3) et son
        contrôle positif (défaut D1 injecté), même modèle et même noyau. Les deux bilans sont consignés avant les
        gardes : si une garde arrête le run, `arret.json` les contient tous deux. Gardes : celles de la phase, puis
        celle du contrôle positif. Rend les couches et, pour la logique, les références du repère de précision."""
        nonlocal phase
        phase = nom
        temps()
        c, cp = config[nom], config["controle_positif"]
        modele, tok = charger(config, revision, c["dtype"], graines)
        chargement = {"attention": getattr(modele.config, "_attn_implementation", None),
                      "type_des_poids": str(next(modele.parameters()).dtype),
                      "normalisations_en_double": getattr(modele, "normalisations_en_double", 0)}
        if nom == "logique":
            resume["chargement"] = chargement
            if config["modele"] != "jouet":
                resume["fichiers_modele"] = empreintes_fichiers_modele(config["modele"], revision)
            fmt, resume["format"] = format_du_modele(modele, tok, config)
        else:
            fmt, _ = format_du_modele(modele, tok, config)
        couches = couches_par_defaut(modele.config.num_hidden_layers)
        chrono: dict = {}
        sorties, plan = jouer_phase(modele, fmt, c, graines, nom, couches, chrono=chrono, echeance=echeance)
        references = [(ep, acts) for ep, acts, _ in sorties if int(ep.identifiant.split("-")[1]) in
                      c["episodes_equivalence"]]
        for ep, _, _ in sorties:
            ecrire_resultat(racine, chemin_m, f"{nom}-{ep.identifiant}-trajectoire", ep.en_dict())
        with noyau(c["noyau_attention"]):
            permis = noyaux_attention_permis()
        resume[nom] = {"plan_lots": plan, "dtype": c["dtype"], "noyau_attention": c["noyau_attention"],
                       "noyaux_permis": permis, "equivalence": bilan_phase(sorties, c, cn), "debit": debit(chrono),
                       "memoire_max_go": memoire_max_go(),
                       "episodes": [{"episode": ep.identifiant, "empreintes": empreintes_episode(ep, acts, r)[0],
                                     "equivalence": r} for ep, acts, r in sorties]}
        if nom != "logique":
            resume[nom]["chargement"] = chargement

        phase = nom_pc
        temps()
        c_pc = dict(c, T=cp["T"])
        chrono_pc: dict = {}
        if torch.cuda.is_available():
            torch.cuda.reset_peak_memory_stats()                     # pic propre au contrôle positif
        sorties_pc, plan_pc = jouer_phase(modele, fmt, c_pc, graines, tache_pc, couches, chrono=chrono_pc,
                                          echeance=echeance, decalage_positions=cp["decalage_positions"])
        for ep, _, _ in sorties_pc:
            ecrire_resultat(racine, chemin_m, f"{tache_pc}-{ep.identifiant}-trajectoire", ep.en_dict())
        resume[nom_pc] = {
            "plan_lots": plan_pc, "T": cp["T"], "decalage_positions": cp["decalage_positions"],
            "bilan": bilan_controle_positif(sorties_pc, c_pc, cp), "debit": debit(chrono_pc),
            "memoire_max_go": memoire_max_go(),
            "episodes": [{"episode": ep.identifiant, "empreintes": empreintes_episode(ep, acts, r)[0],
                          "profils": r["profils"]} for ep, acts, r in sorties_pc if r["ecarts"]]}
        del sorties_pc
        phase = nom
        appliquer_gardes(sorties, resume[nom]["equivalence"], nom, cn)
        phase = nom_pc
        exiger_controle_positif(resume[nom_pc]["bilan"], cp,
                                {"controle_positif": "contrôle positif"}.get(nom_pc, "contrôle positif du chemin"))
        del modele, sorties
        liberer()
        return couches, (references if nom == "logique" else None)

    try:
        if tests is not None:
            derniere = tests.strip().splitlines()[-1] if tests.strip() else ""
            ecrire_resultat(racine, chemin_m, "tests-instance", {"sortie": tests, "derniere_ligne": derniere})
            resume["tests_instance"] = {"derniere_ligne": derniere,
                                        "reussis": tests_conformes(tests, config.get("tests_attendus"))}
        ecrire_resultat(racine, chemin_m, "environnement-python",
                        {"distributions": sorted(f"{d.metadata['Name']}=={d.version}"
                                                 for d in importlib.metadata.distributions())})
        resume["reglages"] = regler_determinisme(config["fils"], config["appareil"])
        resume["reglages"]["memoire_carte_gio"] = exiger_memoire_carte(config["memoire_carte_min_gio"])
        graines = m["graines"]
        cn = config["controle_negatif"]

        couches, references = phase_stricte("logique", "controle_positif", "controle-positif")
        phase_stricte("chemin", "controle_positif_chemin", "controle-positif-chemin")

        phase = "production"
        temps()
        prod = config["production"]
        modele, tok = charger(config, revision, prod["dtype"], graines)
        fmt, _ = format_du_modele(modele, tok, config)
        largeur = modele.config.hidden_size
        codage = "bfloat16-bits" if prod["dtype"] == "bfloat16" else "float32"
        sondes = P.construire_sondes(config["politique"], couches, largeur, graines)
        chrono = {}
        sorties, plan = jouer_phase(modele, fmt, prod, graines, "production", couches, chrono=chrono, echeance=echeance)
        with noyau(prod["noyau_attention"]):
            permis_prod = noyaux_attention_permis()
        # bilan d'équivalence d'abord : un arrêt plus loin (relecture, rejeu, durée) garde les profils ; les gardes
        # de la production viennent après le repère (plus bas)
        resume["production"] = {"plan_lots": plan, "noyau_attention": prod["noyau_attention"],
                                "noyaux_permis": permis_prod, "couches": couches,
                                "largeur": largeur, "equivalence": bilan_phase(sorties, prod, cn), "debit": debit(chrono),
                                "episodes_equivalence": {ep.identifiant: r for ep, _, r in sorties if r["ecarts"]}}
        episodes, octets_par_jeton, jetons_par_episode = [], [], []
        for k, (ep, acts, r) in enumerate(sorties):
            par_jeton = k in config["politique"]["episodes_par_jeton"]
            emp, v, s = empreintes_episode(ep, acts, r, config["politique"], couches, sondes)
            ecrire_resultat(racine, chemin_m, f"production-{ep.identifiant}-trajectoire", ep.en_dict())
            npz = P.ecrire_tableaux(donnees / f"production-{ep.identifiant}-tableaux.npz",
                                    acts if par_jeton else None, v, s, codage)
            P.relire_et_controler(npz, config["politique"], ep, couches, sondes, v, s, par_jeton, codage, acts)
            jetons = sum(len(tr.ids) for tr in ep.transcriptions)
            jetons_par_episode.append(jetons)
            if par_jeton:
                octets_par_jeton.append(sum(P.coder(a, codage).nbytes for pc in acts.values() for a in pc.values())
                                        / (jetons * len(couches)))
            episodes.append({"episode": ep.identifiant, "par_jeton_conserve": par_jeton, "empreintes": emp,
                             "equivalence": r, "tableaux": str(npz.relative_to(racine)),
                             "tableaux_sha256": npz.with_name(npz.name + ".sha256").read_text().split()[0],
                             "tableaux_octets": npz.stat().st_size, "jetons": jetons})
        rejeu = []
        for j in prod["lots_rejeu_en_processus"]:
            refaits, _ = jouer_phase(modele, fmt, prod, graines, "production", couches, lots=[j], echeance=echeance)
            for (ep, acts, r), k in zip(refaits, plan[j]):
                emp = empreintes_episode(ep, acts, r, config["politique"], couches, sondes)[0]
                rejeu.append({"episode": ep.identifiant, "identique": emp == episodes[k]["empreintes"]
                              and r["empreintes_capture"] == episodes[k]["equivalence"]["empreintes_capture"],
                              "empreintes": emp, "empreintes_logits": r["empreintes_logits"],
                              "empreintes_capture": r["empreintes_capture"]})
        moyenne_jetons = sum(jetons_par_episode) / len(jetons_par_episode)
        actions = prod["N"] * prod["T"]
        par_episode_s = (chrono.get("generation_s", 0.0) + chrono.get("passe_unique_s", 0.0)) / prod["episodes"]
        octets_valeur = 2 if codage == "bfloat16-bits" else 4
        stockage = {"codage": codage, "octets_par_valeur_construction": octets_valeur,
                    "octets_par_jeton_et_couche": octets_par_jeton, "jetons_par_episode_moyen": moyenne_jetons,
                    "fichiers_par_jeton_octets": [e["tableaux_octets"] for e in episodes if e["par_jeton_conserve"]],
                    "projection": estimer(config["projection"]["episodes"], max(1, round(moyenne_jetons)), actions,
                                          len(couches), largeur, octets_valeur)}
        del resume["production"]["episodes_equivalence"]     # repris, complet, dans « episodes »
        with noyau(prod["noyau_attention"]):          # repère au noyau de production, comme ce qu'il situe (version 3)
            repere = repere_precision(modele, references, couches)
        resume["production"].update({
            "projection_heures": {"episodes": config["projection"]["episodes"], "taille_lot": prod["taille_lot"],
                                  "heures": par_episode_s * config["projection"]["episodes"] / 3600},
            "empreinte_poids": empreinte_poids(modele),
            "repere_precision": repere,
            "rejeu_en_processus": rejeu, "stockage": stockage,
            "sondes": [{"nom": x.nom, "couche": x.couche, "agregation": x.agregation, "empreinte": x.empreinte()}
                       for x in sondes],
            "episodes": episodes, "memoire_max_go": memoire_max_go()})
        # gardes d'équivalence de la production après le repère, le rejeu et le stockage : un P4 contraire se lit
        # au vu du repère (lecture gelée), et le run s'arrête ensuite
        appliquer_gardes(sorties, resume["production"]["equivalence"], "production", cn)

        phase = "debit"
        temps()
        if torch.cuda.is_available():
            torch.cuda.reset_peak_memory_stats()
        cd = config["debit"]
        transcriptions = [tr.ids[:cd["longueur_contexte"]] for ep, _, _ in sorties for tr in ep.transcriptions]
        mesures, panne = [], None
        for B in cd["tailles_lot"]:
            graines_lot = [graine_entiere(graines[f"debit/ligne-{r}"]) for r in range(B)]
            t0 = time.perf_counter()
            try:
                with noyau(prod["noyau_attention"]):                 # noyau de production (version 3)
                    nouveaux, _ = generer_lot(modele, transcriptions[:B], cd["max_nouveaux"], 1.0, graines_lot, set(),
                                              fmt.tok.pad_token_id if fmt.tok.pad_token_id is not None
                                              else min(fmt.fins))
            except torch.cuda.OutOfMemoryError as e:
                # débit descriptif (contre-lecture 1 de la v3, X-10) : un manque de mémoire de la carte s'y consigne,
                # sans arrêter le run ; toute autre exception (garde, signal TERM…) se propage
                panne = f"{type(e).__name__}: {str(e)[:300]}"
            if panne is not None:
                if torch.cuda.is_available():
                    torch.cuda.empty_cache()
                mesures.append({"taille_lot": B, "erreur": panne})
                break                                                # lots plus grands : plus de mémoire encore
            duree = time.perf_counter() - t0
            n = sum(len(x) for x in nouveaux)
            mesures.append({"taille_lot": B, "jetons_generes": n, "duree_s": duree, "jetons_par_s": n / duree,
                            "contexte_moyen": sum(len(x) for x in transcriptions[:B]) / B})
        resume["debit"] = {"mesures": mesures, "noyau_attention": prod["noyau_attention"],
                           "panne_memoire": panne is not None, "memoire_max_go": memoire_max_go()}
        del modele
        liberer()
        resume["lecture"] = lire(resume, config)
        resume["duree_s"] = time.perf_counter() - depart
    except Exception as e:          # garde, panne (mémoire, noyau refusé…), signal TERM : consigné, puis propagé
        resume["lecture_partielle"] = lire(resume, config)
        ecrire_resultat(racine, chemin_m, "arret", {"phase": phase, "motif": f"{type(e).__name__}: {e}",
                                                     "partiel": resume, "duree_s": time.perf_counter() - depart})
        raise
    chemin_r = ecrire_resultat(racine, chemin_m, "resume", resume)
    verifier_resultat(racine, chemin_r)
    sortie = {"manifeste": str(chemin_m), "resume": str(chemin_r), "lecture": resume["lecture"]}
    if rejeu_de is not None:
        try:
            sortie["comparaison"] = comparer_runs(racine, rejeu_de, run_id)
        except GardeArret as e:
            ecrire_resultat(racine, chemin_m, f"arret-comparaison-{rejeu_de}", {"motif": str(e)})
            raise
    return sortie


# ---------------------------------------------------------------- lecture et comparaison

# dernière ligne de pytest : « N passed[, M warnings] in X.XXs[ (h:mm:ss)] » ; rien d'autre (skipped, failed, xfailed…)
TESTS_REUSSIS = re.compile(r"^(\d+) passed(, \d+ warnings?)? in [0-9.]+s( \(\d+:\d{2}:\d{2}\))?$")


def tests_conformes(sortie: str | None, attendus: int | None) -> bool:
    """P0 : la dernière ligne de pytest annonce exactement `attendus` tests réussis, et rien d'autre."""
    if not sortie or not sortie.strip() or attendus is None:
        return False
    m = TESTS_REUSSIS.match(sortie.strip().splitlines()[-1])
    return bool(m) and int(m.group(1)) == attendus


def lire(resume: dict, config: dict) -> dict:
    """Lecture gelée des prédictions mesurables dans un seul processus (le rejeu entre processus est lu par
    `comparer_runs`). Issues : « conforme », « contraire », « non concluant », « non atteint » (phase non jouée).
    Les comparaisons s'écrivent « not (x <= seuil) » : une valeur illisible n'est jamais conforme."""
    lecture = {}
    f = resume.get("format")
    lecture["format"] = "non atteint" if f is None else ("conforme" if f.get("verifie") is True else "contraire")
    t = resume.get("tests_instance")
    if t is None:
        lecture["tests_instance"] = "sans objet"
    else:
        lecture["tests_instance"] = ("conforme" if tests_conformes(t["derniere_ligne"], config.get("tests_attendus"))
                                     else "contraire")
    cn = config["controle_negatif"]
    for phase in PHASES_COMPAREES:
        p_eq, p_neg = f"{phase}_equivalence", f"{phase}_controle_negatif"
        bilan = resume.get(phase, {}).get("equivalence")
        if bilan is None:
            lecture[p_eq] = lecture[p_neg] = "non atteint"
            continue
        tol, cv = bilan["tolerance"], bilan["couverture"]
        # grandeur de la garde de la phase : maximum, ou 99e centile par action (production, version 3)
        x = bilan["ecart_q99_max"] if bilan.get("statistique", "max") == "q99" else bilan["ecart_max"]
        if x is None or not (x <= tol):
            lecture[p_eq] = "contraire"
            mc, mg = bilan["max_contexte"], bilan["max_zone_generee"]
            if (phase == "logique" and x is not None and x <= 1e-2 and mc is not None and mg is not None
                    and mc >= 1e-5 and mg >= 1e-5 and max(mc, mg) <= 3 * min(mc, mg)):
                lecture[p_eq] = "non concluant : précision probable"     # écart diffus, contexte et zone générée
        elif phase in ("logique", "chemin") and not (cv["actions_remplies"] > 0 and cv["actions_finies_avant"] > 0
                                                     and cv["positions_generees_comparees"] > 0
                                                     and any(x_ != 0 for x_ in cv["lignes_echantillon"])):
            lecture[p_eq] = "non concluant"
        else:
            lecture[p_eq] = "conforme"
        neg = bilan["controle_negatif"]
        if neg["comparables"] < cn["actions_min"]:
            lecture[p_neg] = "non concluant"
        else:
            lecture[p_neg] = "conforme" if neg["fraction"] >= cn["fraction_min"] else "contraire"
    cpc = config["controle_positif"]
    for cle_pc in ("controle_positif", "controle_positif_chemin"):
        pc = resume.get(cle_pc)
        if pc is None:
            lecture[cle_pc] = "non atteint"
        elif pc["bilan"]["comparables"] < cpc["actions_min"]:
            lecture[cle_pc] = "non concluant"
        else:
            lecture[cle_pc] = "conforme" if pc["bilan"]["fraction"] >= cpc["fraction_min"] else "contraire"
    prod = resume.get("production", {})
    if "rejeu_en_processus" in prod:
        lecture["rejeu_en_processus"] = ("conforme" if prod["rejeu_en_processus"]
                                         and all(r["identique"] for r in prod["rejeu_en_processus"]) else "contraire")
    else:
        lecture["rejeu_en_processus"] = "non atteint"
    declenche = []
    for phase in PHASES_COMPAREES:
        bilan = resume.get(phase, {}).get("equivalence")
        if bilan is None:
            continue
        generees = [z["generee"] for z in bilan["zeros"].values()]
        if generees and sum(t_ for _, t_ in generees) > 0 and all(n == t_ for n, t_ in generees):
            declenche.append(phase)
    lecture["audit_symetrie"] = ("déclenché (" + ", ".join(declenche) + ") : aucun écart non nul dans la zone générée ; "
                                 "réserve maintenue, nœud de décision" if declenche else "non déclenché")
    return lecture


def comparer_runs(racine: str | Path, run_a: str, run_b: str) -> dict:
    """Rejeu entre processus : mêmes configuration, graines et code ; au bit près, phase par phase et épisode par
    épisode : empreintes (trajectoire, activations, logits, vecteurs, scores), captures et profils d'équivalence,
    fichiers npz, poids, fichiers du modèle ; et même lecture. Résultat scellé dans `diag/<run_b>/`."""
    racine = Path(racine)
    m_a, _ = lire_manifeste(racine / "runs" / run_a / "manifeste.json")
    m_b, _ = lire_manifeste(racine / "runs" / run_b / "manifeste.json")
    if m_a["config_sha256"] != m_b["config_sha256"]:
        raise GardeArret(f"{run_a} et {run_b} : configurations différentes, rejeu sans objet")
    if m_a["graines"] != m_b["graines"]:
        raise GardeArret(f"{run_a} et {run_b} : graines différentes, rejeu sans objet")
    r = subprocess.run(["git", "-C", str(racine), "diff", "--quiet", m_a["commit"], m_b["commit"], "--", *CHEMINS_GELES],
                       capture_output=True, text=True)
    if r.returncode != 0:
        raise GardeArret(f"{run_a} et {run_b} : arbre gelé différent entre {m_a['commit'][:12]} et "
                         f"{m_b['commit'][:12]}")
    a = verifier_resultat(racine, racine / "diag" / run_a / "resume.json")["resultat"]
    b = verifier_resultat(racine, racine / "diag" / run_b / "resume.json")["resultat"]
    differences = []
    for phase in PHASES_COMPAREES:
        ea = {e["episode"]: e for e in a[phase]["episodes"]}
        eb = {e["episode"]: e for e in b[phase]["episodes"]}
        if set(ea) != set(eb):
            differences.append({"phase": phase, "motif": "épisodes différents"})
            continue
        for ep in sorted(ea):
            for cle in sorted(set(ea[ep]["empreintes"]) | set(eb[ep]["empreintes"])):
                if ea[ep]["empreintes"].get(cle) != eb[ep]["empreintes"].get(cle):
                    differences.append({"phase": phase, "episode": ep, "empreinte": cle})
            for cle in ("empreintes_capture", "profils"):
                if ea[ep]["equivalence"].get(cle) != eb[ep]["equivalence"].get(cle):
                    differences.append({"phase": phase, "episode": ep, "equivalence": cle})
            if ea[ep].get("tableaux_sha256") != eb[ep].get("tableaux_sha256"):
                differences.append({"phase": phase, "episode": ep, "motif": "fichier npz différent"})
    # le débit (durées) et le pic de mémoire sont descriptifs : hors comparaison
    sans_duree = lambda pc: None if pc is None else {k: v for k, v in pc.items()                  # noqa: E731
                                                     if k not in ("debit", "memoire_max_go")}
    for cle_pc in ("controle_positif", "controle_positif_chemin"):
        if sans_duree(a.get(cle_pc)) != sans_duree(b.get(cle_pc)):
            differences.append({"phase": cle_pc, "motif": "contrôle positif différent"})
    for cle in ("empreinte_poids",):
        if a["production"][cle] != b["production"][cle]:
            differences.append({"phase": "production", "motif": "poids différents"})
    if a.get("fichiers_modele") != b.get("fichiers_modele"):
        differences.append({"motif": "fichiers du modèle différents"})
    for cle in ("reglages", "chargement", "format"):                 # même machine, même chargement, même gabarit
        if a.get(cle) != b.get(cle):
            differences.append({"motif": f"{cle} différents", "a": a.get(cle), "b": b.get(cle)})
    if a.get("chemin", {}).get("chargement") != b.get("chemin", {}).get("chargement"):   # chargement du chemin
        differences.append({"phase": "chemin", "motif": "chargement différent",
                            "a": a.get("chemin", {}).get("chargement"), "b": b.get("chemin", {}).get("chargement")})
    if a["production"].get("repere_precision") != b["production"].get("repere_precision"):
        differences.append({"phase": "production", "motif": "repère de précision différent"})
    if m_a["versions"] != m_b["versions"]:
        differences.append({"motif": "versions des bibliothèques différentes", "a": m_a["versions"], "b": m_b["versions"]})
    if a.get("lecture") != b.get("lecture"):
        differences.append({"motif": "lectures différentes", "a": a.get("lecture"), "b": b.get("lecture")})
    corps = {"run_a": run_a, "run_b": run_b, "identique": not differences, "differences": differences,
             "lecture": "conforme" if not differences else "contraire"}
    ecrire_resultat(racine, racine / "runs" / run_b / "manifeste.json", f"comparaison-{run_a}", corps)
    return corps


def _signal_term(signum, frame):
    raise GardeArret("signal TERM reçu (délai externe du run ou plafond de l'amorce) : arrêt consigné")


def main(argv=None) -> int:
    a = argparse.ArgumentParser()
    a.add_argument("--racine", default=".")
    a.add_argument("--run-id", default=None)
    a.add_argument("--revision", default=None)
    a.add_argument("--prereg", default=None)
    a.add_argument("--entropie", type=int, default=None)
    a.add_argument("--rejeu-de", default=None)
    a.add_argument("--sortie-tests", default=None)
    a.add_argument("--repetition-jouet", action="store_true")
    args = a.parse_args(argv)
    signal.signal(signal.SIGTERM, _signal_term)
    config = CONFIG_REPETITION if args.repetition_jouet else CONFIG_REELLE
    suffixe = "repetition-jouet" if args.repetition_jouet else "validation-reelle"
    run_id = args.run_id or datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S") + "-" + suffixe
    sortie = executer(args.racine, run_id, args.revision, args.entropie, config, args.prereg, args.rejeu_de,
                      args.sortie_tests)
    print(json.dumps(sortie, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
