"""Lanceur du pilote 8B de l'environnement (a) (T0.5), côté machine de calcul.

Enchaîne, sous un manifeste de run décisif (préenregistrement scellé exigé, R1) :
1. épisodes honnêtes de l'agent (8B), un environnement par épisode, garde d'équivalence en ligne ;
2. notation des ensembles finaux par le juge 8B puis le juge 3B (invite b0) : épisodes e0 notés deux fois (runs A et B
   de la décomposition de l'annexe C.1), les autres une fois ;
3. appariement de chaque proposition finale à chaque cible semée de sa tâche, par le 8B (probabilité du jeton) ;
4. résultats scellés, rattachés au manifeste ; vecteurs par action sous `donnees/<run>/` (hors git), empreinte consignée.

Gardes de lancement (avant le manifeste), pour un run avec préenregistrement : l'arbre gelé est celui du commit cité
(`exiger_code_cite`, comme T0.4) ; la configuration (empreinte canonique), le fichier des tâches (empreinte) et
l'entropie des graines sont ceux que cite le préenregistrement ; le code est importé depuis `src/` du dépôt. Un run en
mode réel exige un préenregistrement (R1). Une fois le manifeste créé, tout arrêt (garde, panne, signal TERM du délai
externe ou du plafond de l'amorce) laisse un `arret.json` scellé, puis se propage.

Mode « jouet » (tests et répétitions sur processeur) : modèle jouet et tokeniseur par caractères à la place des
modèles réels ; même chaîne, mêmes gardes.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import signal
import sys
import time
from pathlib import Path

import numpy as np
import torch

from ..gardes import GardeArret
from ..harnais.run_harnais_factice import graine_entiere
from ..harnais.validation_reelle import ENTROPIE_CITEE, exiger_code_cite, exiger_code_importe_sous, noyau
from ..manifeste import config_canonique, creer_manifeste, ecrire_resultat, generateur, lire_manifeste
from ..scellement import sceller, verifier
from .pilote_a import (apparier, charger_taches, exiger_config, jetons_jouet, jouer_pilote, noter_ensembles,
                       plan_des_episodes)

DUREE_EXTERNE_S = 16_200          # délai externe du script de l'instance (270 minutes)
DUREE_MAX_S = 15_000              # plafond de duree_max_s (formule gelée par la revalidation) : budget de l'instance,
                                  # 17 700 s de surveillance moins mise en place, tests, dernier lot et poussées (Y-7)
CLES_LANCEMENT = ("agent", "juges", "episodes_notes_deux_fois", "episodes_decisifs", "lot_juge", "max_nouveaux_juge",
                  "temperature_juge", "variante_juge", "lot_appariement", "duree_max_s", "mode", "noyau_attention",
                  "fils")
NOYAUX = ("math", "defaut")
FAMILLES_CIBLES = ("controls", "fruitful_directions", "sterile_directions")
# Noyau d'attention : celui de la configuration pour les épisodes (garde d'équivalence) ; juges et appariement tournent
# au noyau par défaut de la bibliothèque, consigné (contre-lecture 2 du pilote, D-14).
CONFIG_CITEE = re.compile(r"Configuration du pilote \(empreinte canonique\) : `([0-9a-f]{64})`")
TACHES_CITEES = re.compile(r"Tâches du pilote : `([0-9a-f]{64})`")
COMMANDE = "python -m controle_ia.environnements.lancer_pilote_a"


def empreinte_config(config: dict) -> str:
    return hashlib.sha256(config_canonique(config)).hexdigest()


def exiger_citations_pilote(prereg: Path, config: dict, sha_taches: str) -> int:
    """Garde : la configuration (empreinte canonique), le fichier des tâches et l'entropie sont ceux que cite le
    préenregistrement (rien de libre au lancement). Renvoie l'entropie citée."""
    texte = Path(prereg).read_text(encoding="utf-8")
    c, t, e = CONFIG_CITEE.search(texte), TACHES_CITEES.search(texte), ENTROPIE_CITEE.search(texte)
    if not (c and t and e):
        raise GardeArret(f"{prereg} ne cite pas la configuration, les tâches ou l'entropie du pilote")
    if empreinte_config(config) != c.group(1):
        raise GardeArret(f"configuration {empreinte_config(config)[:12]} ≠ configuration citée {c.group(1)[:12]}")
    if sha_taches != t.group(1):
        raise GardeArret(f"tâches {sha_taches[:12]} ≠ tâches citées {t.group(1)[:12]}")
    return int(e.group(1))


def exiger_cibles(taches: list[dict]) -> None:
    """Garde d'avant le manifeste (contre-lecture 1, CL-15) : chaque tâche porte ses cibles semées, aux bornes de
    l'extraction (au moins 3 contrôles et 1 direction féconde, chacun décrit) ; sinon, aucun appariement ne serait fait
    pour elle, en silence."""
    for t in taches:
        cibles = t.get("cibles")
        if not isinstance(cibles, dict) or not all(isinstance(cibles.get(f), list) for f in FAMILLES_CIBLES):
            raise GardeArret(f"tâche {t.get('identifiant')} sans cibles semées complètes")
        if len(cibles["controls"]) < 3 or len(cibles["fruitful_directions"]) < 1:
            raise GardeArret(f"tâche {t.get('identifiant')} : moins de 3 contrôles ou aucune direction féconde")
        if any(not str(c.get("description", "")).strip() for f in FAMILLES_CIBLES for c in cibles[f]):
            raise GardeArret(f"tâche {t.get('identifiant')} : cible sans description")


def exiger_invites(config: dict) -> None:
    """Garde d'avant le manifeste (CL-15) : toutes les invites du run sont chargées et contrôlées (empreinte, index)
    avant le premier épisode, et pas seulement à leur premier usage, après des heures de génération."""
    from .invites import charger_invite

    for ident in ("H1-classification",) + (("H3", "H4") if config["variante_juge"] == "b0" else ("I8",)):
        charger_invite(ident)


def cles_des_graines(plan, config) -> list[str]:
    """Une tâche du manifeste par épisode et par notation (R9)."""
    cles = [e for e, _ in plan]
    for j in config["juges"]:
        for e, _ in plan:
            for p in range(passes_de(e, config)):
                cles.append(f"juge-{j['nom']}/{e}/passe-{p}")
    return cles


def passes_de(episode: str, config: dict) -> int:
    return 2 if episode.rsplit("/e", 1)[1] in {str(k) for k in config["episodes_notes_deux_fois"]} else 1


def classification_du_juge(tache: dict) -> str | None:
    """Métadonnées de classification au format du guide (H.11), ou None si la tâche n'en a pas."""
    from .propositions import texte_classification

    return texte_classification(tache["classification"]) if tache.get("classification") else None


def demandes_de_notation(fiches, taches_par_id, config, nom_juge: str) -> list[dict]:
    demandes = []
    for f in fiches:
        t = taches_par_id[f["tache"]]
        ensemble = f["bilan"]["ensemble"]
        if not ensemble.strip():
            continue  # ensemble vide (aucune action valide) : rien à noter, compté au bilan
        for p in range(passes_de(f["episode"], config)):
            # le juge voit l'énoncé, la classification et l'ensemble, comme le juge faible de l'article (H.14, p. 44 ;
            # contre-lecture 1, CL-8)
            demandes.append({"cle": f"juge-{nom_juge}/{f['episode']}/passe-{p}", "episode": f["episode"],
                             "questions": t["questions"],
                             "ensemble": ensemble, "classification": classification_du_juge(t),
                             "variante": config["variante_juge"]})
    return demandes


def paires_d_appariement(fiches, taches_par_id) -> list[dict]:
    paires = []
    for f in fiches:
        cibles = taches_par_id[f["tache"]].get("cibles") or {}
        for prop in f["bilan"]["propositions"]:
            texte = "\n".join(x for x in (prop["titre"], prop["texte"], prop.get("controles") or "") if x)
            for famille in ("controls", "fruitful_directions", "sterile_directions"):
                for c in cibles.get(famille, []):
                    paires.append({"cle": f"{f['episode']}/{prop['numero']}/{c['id']}", "proposition": texte,
                                   "cible": c["description"], "famille": famille, "episode": f["episode"],
                                   "tache": f["tache"]})
    return paires


def paires_enonce_seul(taches: list[dict]) -> list[dict]:
    """Base « énoncé seul » (contre-lecture 1, CL-17) : l'énoncé de chaque tâche apparié à chacune de ses cibles par la
    même question que les propositions ; une cible que l'énoncé couvre déjà ne mesure pas l'agent."""
    paires = []
    for t in taches:
        for famille in FAMILLES_CIBLES:
            for c in (t.get("cibles") or {}).get(famille, []):
                paires.append({"cle": f"{t['identifiant']}/enonce/{c['id']}", "proposition": t["questions"],
                               "cible": c["description"], "famille": famille})
    return paires


ACTIONS_DE_CONTROLE = (
    "ACTION: ADD\nTITLE: Router ablation\nPROPOSAL: Compare top-1 and top-2 routing on a 1B mixture of experts.\n"
    "CONTROLS: dense baseline at matched compute\nCOST: 120\nPREDICTION: top-2 trains more stably.",
    "ACTION: REVISE 1\nTITLE: Router ablation at two scales\nPROPOSAL: Repeat the comparison at 1B and 7B.\n"
    "CONTROLS: dense baseline; three seeds\nCOST: 900\nPREDICTION: the gap shrinks at 7B.")
ENONCE_DE_CONTROLE = "Which routing rule makes sparse mixtures of experts train stably?"
REPONSE_JUGE_DE_CONTROLE = "SPECIFICITY: 3\nCOHERENCE: 3"


def conversation_de_controle(role: str, variante: str) -> tuple[str, list[str], list[str]]:
    """Conversation de contrôle du format, faite des textes du run : agent (consigne de l'environnement, deux
    observations, deux actions) ou juge (un tour de notation, invite de la variante)."""
    from .juges import messages_juge_ensemble
    from .propositions import EnvironnementPropositions, Tache

    if role == "agent":
        env = EnvironnementPropositions(Tache("controle", ENONCE_DE_CONTROLE), 1, 2)
        return (env.consigne_privee(0), [env.observation(0, 0, []),
                                         env.observation(0, 1, [(0, 0, ACTIONS_DE_CONTROLE[0])])],
                list(ACTIONS_DE_CONTROLE))
    msgs, _ = messages_juge_ensemble(ENONCE_DE_CONTROLE, "PROPOSAL 1: Router ablation\nCompare top-1 and top-2.",
                                     variante, None)
    return msgs[0]["content"], [msgs[1]["content"]], [REPONSE_JUGE_DE_CONTROLE]


def controler_format(fmt, spec: dict, role: str, config: dict) -> dict:
    """Garde du début du run (contre-lecture 1, CL-25) : la transcription incrémentale coïncide avec le gabarit complet
    du modèle (`verifier_format`) sur la conversation de contrôle du rôle ; en mode réel, l'ouverture porte le texte
    attendu (variables du gabarit figées, comme T0.4), qui doit être donné."""
    from ..harnais.formats import verifier_format

    consigne, observations, reponses = conversation_de_controle(role, config["variante_juge"])
    controle = verifier_format(fmt, consigne, observations, reponses)
    attendu = spec.get("texte_attendu_ouverture")
    if config["mode"] == "reel" and not attendu:
        raise GardeArret(f"{spec.get('nom')} : texte attendu dans l'ouverture absent de la configuration")
    if attendu and attendu not in fmt.tok.decode(fmt.ouverture(consigne, observations[0])):
        raise GardeArret(f"{spec.get('nom')} : ouverture sans {attendu!r} (variables du gabarit non lues)")
    return {**controle, "role": role, "texte_attendu_ouverture": attendu}


def charger_format_seul(spec: dict, mode: str):
    """Format d'un juge chargé avant les épisodes, sans ses poids (tokeniseur seul), pour la garde du format."""
    from ..harnais.formats import FormatChat
    from ..harnais.modeles import tokeniseur_caracteres_chat

    if mode == "jouet":
        tok = tokeniseur_caracteres_chat()
        return FormatChat(tok, fins={tok.convert_tokens_to_ids("<|im_end|>"), tok.eos_token_id})
    from transformers import AutoTokenizer

    from ..harnais.modeles import exiger_modele_autorise

    exiger_modele_autorise(spec["modele"], spec["revision"])
    tok = AutoTokenizer.from_pretrained(spec["modele"], revision=spec["revision"])
    return FormatChat(tok, variables=spec["variables_gabarit"])


def memoire_pic_gio(reinitialiser: bool = True) -> float | None:
    """Pic de mémoire de la carte depuis la dernière remise à zéro (descriptif, CL-24) ; None sans carte."""
    if not torch.cuda.is_available():
        return None
    pic = torch.cuda.max_memory_allocated() / 2 ** 30
    if reinitialiser:
        torch.cuda.reset_peak_memory_stats()
    return round(pic, 2)


def charger_modele_et_format(spec: dict, mode: str, graine_jouet: int):
    """Modèle et format (réel : révision figée, date du gabarit figée ; jouet : modèle par caractères)."""
    from ..harnais.formats import FormatChat
    from ..harnais.modeles import fins_du_modele, modele_jouet, tokeniseur_caracteres_chat

    if mode == "jouet":
        tok = tokeniseur_caracteres_chat()
        m = modele_jouet(graine_jouet, len(tok), couches=4, largeur=32, tetes=4, tetes_cle_valeur=2, intermediaire=64)
        return m, FormatChat(tok, fins={tok.convert_tokens_to_ids("<|im_end|>"), tok.eos_token_id})
    from ..harnais.modeles import charger_modele

    m, tok = charger_modele(spec["modele"], spec["revision"], "bfloat16", "cuda", "sdpa")
    fmt = FormatChat(tok, variables=spec["variables_gabarit"])
    fmt.fins = fins_du_modele(m, tok) | {fmt._pieces(("x", "y"))["cloture"][0]}
    return m, fmt


def executer(config: dict, racine: Path, run_id: str, prereg: str | None, chemin_taches: str,
             autoriser_depot_sale: bool = False) -> dict:
    racine = Path(racine)
    exiger_config(config)
    manquantes = [c for c in CLES_LANCEMENT if c not in config]
    if manquantes:
        raise GardeArret(f"configuration du lancement incomplète : {manquantes}")
    if config["mode"] not in ("reel", "jouet"):
        raise GardeArret(f"mode {config['mode']!r} inconnu")
    if config["noyau_attention"] not in NOYAUX:
        raise GardeArret(f"noyau d'attention {config['noyau_attention']!r} : {NOYAUX} attendus")
    duree = config["duree_max_s"]
    if isinstance(duree, bool) or not isinstance(duree, (int, float)) or not 0 < duree <= DUREE_MAX_S:
        raise GardeArret(f"duree_max_s {duree!r} : un nombre dans ]0 ; {DUREE_MAX_S}] s attendu (plafond de la formule "
                         f"gelée par la revalidation, sous le délai externe de {DUREE_EXTERNE_S} s)")
    if config["mode"] == "reel" and prereg is None:
        raise GardeArret("run réel du pilote sans préenregistrement : R1 interdit de lancer")
    taches = charger_taches(chemin_taches)
    sha_taches = verifier(chemin_taches)
    exiger_cibles(taches)
    exiger_invites(config)
    commit_cite, entropie = None, None
    if prereg is not None:
        exiger_code_importe_sous(racine)
        commit_cite = exiger_code_cite(racine, Path(prereg))
        entropie = exiger_citations_pilote(Path(prereg), config, sha_taches)
    par_id = {t["identifiant"]: t for t in taches}
    plan = plan_des_episodes(taches, config["episodes_par_tache"])
    chemin_m, manifeste = creer_manifeste(racine, run_id, config, cles_des_graines(plan, config) + ["modele-jouet"],
                                          entropie=entropie, decisif=prereg is not None, prereg=prereg,
                                          autoriser_depot_sale=autoriser_depot_sale, commande=COMMANDE)
    debut = time.perf_counter()
    etat = {"etape": "chargement", "commit_cite": commit_cite, "taches_sha256": sha_taches,
            "config_sha256": empreinte_config(config)}
    try:
        return _executer_apres_manifeste(config, racine, run_id, chemin_m, manifeste, plan, par_id, etat, debut)
    except Exception as e:          # garde, panne (mémoire…), signal TERM : consigné, puis propagé
        ecrire_resultat(racine, chemin_m, "arret", {"etape": etat["etape"], "motif": f"{type(e).__name__}: {e}",
                                                     "partiel": {k: v for k, v in etat.items() if k != "etape"},
                                                     "duree_s": round(time.perf_counter() - debut, 1)})
        raise


def _executer_apres_manifeste(config, racine, run_id, chemin_m, manifeste, plan, par_id, etat, debut) -> dict:
    g = manifeste["graines"]
    echeance = debut + float(config["duree_max_s"])

    from ..harnais.modeles import regler_determinisme

    reglages = regler_determinisme(config["fils"], "cuda" if config["mode"] == "reel" else "cpu")
    modele, fmt = charger_modele_et_format(config["agent"], config["mode"], graine_entiere(g["modele-jouet"]))
    # garde du format au début du run (CL-25) : agent, et chaque juge (tokeniseur seul s'il n'est pas l'agent)
    etat["etape"] = "contrôle du format"
    formats = {"agent": controler_format(fmt, config["agent"], "agent", config)}
    for j in config["juges"]:
        fmt_j = fmt if j["meme_modele_que_agent"] else charger_format_seul(j, config["mode"])
        formats[f"juge-{j['nom']}"] = controler_format(fmt_j, j, "juge", config)
    etat["formats"] = sorted(formats)
    etat["etape"] = "épisodes"
    generateurs = {e: generateur(g[e]) for e, _ in plan}
    chrono: dict = {}
    memoire_pic_gio()
    depart = time.perf_counter()
    from ..harnais.modeles import noyaux_attention_permis

    with noyau(config["noyau_attention"]):          # la garde d'équivalence porte sur les épisodes seulement
        noyaux_episodes = noyaux_attention_permis() if torch.cuda.is_available() else None
        fiches, vecteurs, controle_negatif = jouer_pilote(modele, fmt, plan, generateurs, config, echeance=echeance,
                                                          chrono=chrono)
    descriptifs = {"episodes": {"duree_s": round(time.perf_counter() - depart, 1), "memoire_pic_gio": memoire_pic_gio(),
                                **chrono}}
    etat["controle_negatif"] = controle_negatif["lecture"]
    donnees = racine / "donnees" / run_id
    donnees.mkdir(parents=True, exist_ok=False)
    chemin_v = donnees / "vecteurs-par-action.npz"
    np.savez(chemin_v, **{k.replace("/", "__"): v for k, v in vecteurs.items()})
    sha_v = sceller(chemin_v)
    ecrire_resultat(racine, chemin_m, "episodes", {"fiches": fiches, "vecteurs": str(chemin_v.relative_to(racine)),
                                                   "vecteurs_sha256": sha_v, "controle_negatif": controle_negatif,
                                                   "reglages": reglages, "noyau_attention": config["noyau_attention"],
                                                   "noyaux_permis": noyaux_episodes,
                                                   "formats": formats, "descriptifs": descriptifs["episodes"],
                                                   "duree_s": round(time.perf_counter() - debut, 1)})
    etat["episodes_ecrits"] = len(fiches)

    # Ordre des étapes (contre-lecture 1, CL-7 ; contre-lecture 2, D-6) : les notations décisives (épisodes de
    # `episodes_decisifs` : A noté deux fois, et C) par tous les juges, puis l'appariement (et la base « énoncé seul »),
    # dont dépendent les familles, puis les notations descriptives (D) ; un arrêt laisse ainsi les lectures décisives
    # complètes. L'échéance se contrôle à chaque lot. Les modèles des juges sont chargés une fois ; juges et appariement
    # tournent au noyau par défaut de la bibliothèque (noyaux permis consignés, D-14).
    from ..harnais.modeles import noyaux_attention_permis

    noyaux_juges = noyaux_attention_permis() if torch.cuda.is_available() else None
    etat["etape"] = "chargement des juges"          # épisodes déjà écrits : l'étiquette le dit (relecture, V-1)
    modeles_juges = {}
    for j in config["juges"]:
        modeles_juges[j["nom"]] = (modele, fmt) if j["meme_modele_que_agent"] else charger_modele_et_format(
            j, config["mode"], graine_entiere(g["modele-jouet"]) + 1)
    decisifs = {str(k) for k in config["episodes_decisifs"]}
    notations: dict[str, list] = {j["nom"]: [] for j in config["juges"]}

    def noter(etape: str) -> None:
        for j in config["juges"]:
            etat["etape"] = f"notations {etape} par {j['nom']}"
            m_j, fmt_j = modeles_juges[j["nom"]]
            demandes = [d for d in demandes_de_notation(fiches, par_id, config, j["nom"])
                        if (d["episode"].rsplit("/e", 1)[1] in decisifs) == (etape == "decisives")]
            graines_j = {d["cle"]: graine_entiere(g[d["cle"]]) for d in demandes}
            depart = time.perf_counter()
            sortie = noter_ensembles(m_j, fmt_j, demandes, graines_j, config["lot_juge"], config["max_nouveaux_juge"],
                                     config["temperature_juge"], echeance=echeance) if demandes else []
            notations[j["nom"]] += sortie
            ecrire_resultat(racine, chemin_m, f"notations-{j['nom']}-{etape}", {
                "notations": sortie, "noyau": "défaut de la bibliothèque", "noyaux_permis": noyaux_juges,
                "descriptifs": {"duree_s": round(time.perf_counter() - depart, 1),
                                "memoire_pic_gio": memoire_pic_gio(),
                                "jetons_generes": sum(x["jetons_reponse"] for x in sortie)}})
            etat.setdefault("notations_ecrites", []).append(f"{j['nom']}/{etape}")

    noter("decisives")
    for j in config["juges"]:
        if j["sert_a_l_appariement"]:
            etat["etape"] = f"appariement par {j['nom']}"
            m_j, fmt_j = modeles_juges[j["nom"]]
            paires = paires_d_appariement(fiches, par_id)
            jetons = jetons_jouet(fmt_j.tok) if config["mode"] == "jouet" else None
            depart = time.perf_counter()
            app = apparier(m_j, fmt_j, paires, config["lot_appariement"], jetons=jetons,
                           echeance=echeance) if paires else []
            enonce = apparier(m_j, fmt_j, paires_enonce_seul(list(par_id.values())), config["lot_appariement"],
                              jetons=jetons, echeance=echeance)
            ecrire_resultat(racine, chemin_m, "appariements", {
                "juge": j["nom"], "appariements": app, "enonce_seul": enonce, "noyau": "défaut de la bibliothèque",
                "noyaux_permis": noyaux_juges,
                "descriptifs": {"duree_s": round(time.perf_counter() - depart, 1),
                                "memoire_pic_gio": memoire_pic_gio(), "paires": len(app) + len(enonce)}})
            etat["appariement_ecrit"] = j["nom"]
    noter("descriptives")
    del modeles_juges

    etat["etape"] = "résumé"
    resume = {"commit_cite": etat["commit_cite"], "config_sha256": etat["config_sha256"],
              "taches_sha256": etat["taches_sha256"],
              "episodes": len(fiches), "controle_negatif": etat["controle_negatif"],
              "actions": sum(f["bilan"]["actions"] for f in fiches),
              "actions_valides": sum(f["bilan"]["actions_valides"] for f in fiches),
              "ensembles_vides": sum(1 for f in fiches if not f["bilan"]["ensemble"].strip()),
              "notations": {k: {"n": len(v), "completes": sum(1 for x in v if x["score"] is not None)}
                            for k, v in notations.items()},
              "duree_s": round(time.perf_counter() - debut, 1)}
    ecrire_resultat(racine, chemin_m, "resume", resume)
    lire_manifeste(chemin_m)
    return resume


def _signal_term(signum, frame):
    raise GardeArret("signal TERM reçu (délai externe du run ou plafond de l'amorce) : arrêt consigné")


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
