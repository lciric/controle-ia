"""Lanceur « notations seules » du pilote de T0.5, côté machine de calcul (N-021, option (a), GO-2026-10-12-02).

Le pilote (`lancer_pilote_a`) s'est arrêté à son échéance interne pendant les notations décisives du juge 8B : ses
épisodes et son appariement sont écrits et scellés, aucune notation décisive ne l'est. Ce module refait les seules
notations décisives (épisodes `episodes_decisifs`, e0 noté deux fois : A, B et C de la décomposition) par les juges du
pilote, sur les ensembles finaux scellés de `episodes.json`, avec les mêmes paramètres, les mêmes graines (entropie du
pilote, mêmes clés `juge-<juge>/<épisode>/passe-<p>`) et le même découpage en lots. Il n'importe que des fonctions du
code cité par le pilote, sans les modifier ; ses notations s'écrivent dans `diag/<run des notations>/`, sous son propre
manifeste, jamais dans le dossier du pilote.

Gardes d'avant le manifeste : configuration complète et bornée ; préenregistrement en mode réel (R1) ; citations
(commit du code, configuration, run du pilote, empreintes de son manifeste, de ses épisodes et de son arrêt, tâches,
entropie) ; état du pilote constaté (épisodes et appariement scellés et rattachés, arrêt pendant les notations
décisives, aucune notation ni aucun résumé) ; paramètres des juges et versions égaux à ceux du pilote ; nombre exact de
notations par juge ; graines égales à celles du manifeste du pilote.

Après le manifeste : formats des juges contrôlés contre ceux, scellés, du début du pilote ; le 8B note lot par lot, puis
son fichier est écrit ; le 3B, préchargé avant, se charge hors ligne, format recontrôlé, note, puis son fichier est
écrit. Chaque juge a son échéance (le 8B depuis le début du run, le 3B depuis son premier lot), contrôlée avant chaque
lot : un juge échu s'arrête sans fichier (règle « tout ou rien » de la lecture) et le suivant commence. L'échéance
globale, elle, arrête le run (`noter_ensembles`), comme le signal TERM : aucune exception d'arrêt n'est attrapée pour
continuer (gardes.py). Une ligne `PROGRES` par lot (juge, rang et durée du lot, rien d'autre : aucun texte, aucun compte
de réponses) et une par fin de juge (statut, lots faits, durée) vont sur la sortie d'erreur. Tout arrêt levé après le
manifeste laisse un `arret.json` scellé (étape, motif, compteurs), puis se propage ; restent sans `arret.json` les
fenêtres déclarées par le préenregistrement (KILL du délai externe ou du plafond de l'amorce, arrêt brutal de l'hôte ou
de l'instance, exception ou signal pendant la consignation, signal pendant la création du manifeste ou juste après :
l'état et le début du run sont calculés avant le manifeste).
"""
from __future__ import annotations

import argparse
import gc
import json
import re
import signal
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import torch

from ..gardes import GardeArret, exiger_sans_signal, lever_sur_term, motif_d_arret, relever_term_apres
from ..harnais.run_harnais_factice import graine_entiere
from ..harnais.validation_reelle import ENTROPIE_CITEE, exiger_code_cite, exiger_code_importe_sous
from ..manifeste import (creer_manifeste, ecrire_resultat, graines, lire_manifeste, verifier_resultat, versions)
from ..scellement import empreinte, verifier
from .lancer_pilote_a import (TACHES_CITEES, charger_format_seul, charger_modele_et_format, controler_format,
                              demandes_de_notation, empreinte_config, exiger_invites, memoire_pic_gio,
                              precharger_juges)
from .pilote_a import charger_taches, noter_ensembles

COMMANDE = "python -m controle_ia.environnements.noter_pilote_a"
DUREE_EXTERNE_S = 24_000            # délai externe du script de l'instance pour cette étude (400 minutes)
DUREE_GLOBALE_MAX_S = 23_100        # borne de `duree_globale_s` : sous le délai externe, marge pour le dernier lot
CLES = ("mode", "run_pilote", "agent", "juges", "lot_juge", "max_nouveaux_juge", "temperature_juge", "variante_juge",
        "episodes_decisifs", "episodes_notes_deux_fois", "fils", "duree_max_juges_s", "duree_globale_s",
        "notations_attendues_par_juge")
CLES_EGALES_AU_PILOTE = ("agent", "juges", "lot_juge", "max_nouveaux_juge", "temperature_juge", "variante_juge",
                         "episodes_decisifs", "episodes_notes_deux_fois", "fils")
VERSIONS_EGALES = ("torch", "transformers", "tokenizers", "numpy")
# intitulés propres à ce préenregistrement (relecture du plan, constat 12 : jamais la première occurrence d'un intitulé
# du pilote) ; le commit du code se lit par `exiger_code_cite` (« Commit du code d'analyse », une seule ligne)
CONFIG_CITEE = re.compile(r"Configuration des notations \(empreinte canonique\) : `([0-9a-f]{64})`")
RUN_PILOTE_CITE = re.compile(r"Run du pilote noté : `(\d{8}-\d{6}-[A-Za-z0-9_.-]+)`")
MANIFESTE_PILOTE_CITE = re.compile(r"Manifeste du pilote noté : `([0-9a-f]{64})`")
EPISODES_PILOTE_CITES = re.compile(r"Épisodes du pilote noté : `([0-9a-f]{64})`")
ARRET_PILOTE_CITE = re.compile(r"Arrêt du pilote noté : `([0-9a-f]{64})`")


def progres(**champs) -> None:
    """Ligne de progression, à préfixe fixe, sans aucun texte de réponse ni d'ensemble (recopiée dans le journal de
    l'instance par son script)."""
    instant = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print("PROGRES " + instant + " " + " ".join(f"{k}={v}" for k, v in champs.items()), file=sys.stderr, flush=True)


def exiger_config_notations(config: dict) -> None:
    manquantes = [c for c in CLES if c not in config]
    if manquantes:
        raise GardeArret(f"configuration des notations incomplète : {manquantes}")
    if config["mode"] not in ("reel", "jouet"):
        raise GardeArret(f"mode {config['mode']!r} inconnu")
    noms = [j["nom"] for j in config["juges"]]
    durees = config["duree_max_juges_s"]
    if not isinstance(durees, dict) or sorted(durees) != sorted(noms):
        raise GardeArret(f"duree_max_juges_s : une durée par juge attendue ({noms})")
    globale = config["duree_globale_s"]
    for nom, d in [*durees.items(), ("globale", globale)]:
        if isinstance(d, bool) or not isinstance(d, (int, float)) or not 0 < d <= DUREE_GLOBALE_MAX_S:
            raise GardeArret(f"durée {nom} {d!r} : un nombre dans ]0 ; {DUREE_GLOBALE_MAX_S}] s attendu")
    n = config["notations_attendues_par_juge"]
    if isinstance(n, bool) or not isinstance(n, int) or n <= 0:
        raise GardeArret(f"notations_attendues_par_juge {n!r} : un entier positif attendu")


def exiger_citations_notations(prereg: Path, config: dict, sha_taches: str, pilote: dict) -> int:
    """Garde : configuration, run du pilote, empreintes de son manifeste, de ses épisodes et de son arrêt, tâches et
    entropie sont ceux que cite le préenregistrement des notations. Renvoie l'entropie citée."""
    texte = Path(prereg).read_text(encoding="utf-8")
    trouves = {nom: rx.findall(texte) for nom, rx in (
        ("configuration", CONFIG_CITEE), ("run du pilote", RUN_PILOTE_CITE), ("manifeste", MANIFESTE_PILOTE_CITE),
        ("épisodes", EPISODES_PILOTE_CITES), ("arrêt", ARRET_PILOTE_CITE), ("tâches", TACHES_CITEES),
        ("entropie", ENTROPIE_CITEE))}
    for nom, valeurs in trouves.items():
        if len(set(valeurs)) != 1:
            raise GardeArret(f"{prereg} : {nom} cité{'e' if nom != 'run du pilote' else ''} "
                             f"{'plusieurs fois, différemment' if valeurs else 'nulle part'}")
    attendus = {"configuration": empreinte_config(config), "run du pilote": config["run_pilote"],
                "manifeste": pilote["manifeste_sha256"], "épisodes": pilote["episodes_sha256"],
                "arrêt": pilote["arret_sha256"], "tâches": sha_taches}
    for nom, valeur in attendus.items():
        if trouves[nom][0] != valeur:
            raise GardeArret(f"{nom} {str(valeur)[:12]} ≠ {nom} cité {trouves[nom][0][:12]}")
    return int(trouves["entropie"][0])


def charger_pilote_note(racine: Path, run_pilote: str) -> dict:
    """État du pilote constaté sur ses fichiers scellés : manifeste, épisodes et appariement rattachés à lui ; arrêt
    consigné pendant les notations décisives ; aucune notation, aucun résumé."""
    d = racine / "diag" / run_pilote
    chemin_m = racine / "runs" / run_pilote / "manifeste.json"
    if not chemin_m.exists():
        raise GardeArret(f"manifeste du pilote absent : {chemin_m}")
    manifeste, sha_m = lire_manifeste(chemin_m)
    corps = {}
    for nom in ("episodes", "appariements", "arret"):
        f = d / f"{nom}.json"
        if not f.exists():
            raise GardeArret(f"pilote {run_pilote} : {nom}.json absent")
        c = verifier_resultat(racine, f)
        if c["run_id"] != run_pilote or c["manifeste_sha256"] != sha_m:
            raise GardeArret(f"pilote {run_pilote} : {nom}.json rattaché à un autre run ou à un autre manifeste")
        corps[nom] = c["resultat"]
    deja = sorted(p.name for p in d.glob("notations-*.json")) + (["resume.json"] if (d / "resume.json").exists() else [])
    if deja:
        raise GardeArret(f"pilote {run_pilote} : {deja} déjà présents ; aucune notation n'est refaite par-dessus")
    etape = str(corps["arret"].get("etape", ""))
    if not etape.startswith("notations decisives par "):
        raise GardeArret(f"pilote {run_pilote} : arrêté à l'étape {etape!r}, et non pendant les notations décisives")
    if not corps["arret"].get("partiel", {}).get("appariement_ecrit"):
        raise GardeArret(f"pilote {run_pilote} : appariement non consigné comme écrit")
    return {"manifeste": manifeste, "manifeste_sha256": sha_m, "fiches": corps["episodes"]["fiches"],
            "formats": corps["episodes"]["formats"], "arret": corps["arret"],
            "episodes_sha256": empreinte(d / "episodes.json"), "arret_sha256": empreinte(d / "arret.json")}


def exiger_egal_au_pilote(config: dict, pilote: dict, mode: str) -> None:
    cp = pilote["manifeste"]["config"]
    for k in CLES_EGALES_AU_PILOTE:
        if config[k] != cp.get(k):
            raise GardeArret(f"{k} ≠ celui du pilote : aucun paramètre des juges ne change (N-021)")
    if mode == "reel":
        v, vp = versions(), pilote["manifeste"]["versions"]
        ecarts = [b for b in VERSIONS_EGALES if v.get(b) != vp.get(b)]
        if ecarts:
            raise GardeArret(f"versions ≠ celles du pilote : {ecarts}")


def demandes_decisives(pilote: dict, par_id: dict, config: dict, nom_juge: str) -> list[dict]:
    decisifs = {str(k) for k in config["episodes_decisifs"]}
    return [d for d in demandes_de_notation(pilote["fiches"], par_id, config, nom_juge)
            if d["episode"].rsplit("/e", 1)[1] in decisifs]


def cles_des_graines(demandes_par_juge: dict) -> list[str]:
    return [d["cle"] for dem in demandes_par_juge.values() for d in dem] + ["modele-jouet"]


def exiger_graines_du_pilote(cles: list[str], entropie: int, pilote: dict) -> None:
    """Graines égales, clé à clé, à celles du manifeste du pilote : mêmes graines et mêmes entrées ; l'identité des
    notations avec celles qu'aurait faites le pilote n'est pas garantie sur une autre carte ou une autre instance."""
    gp = pilote["manifeste"]["graines"]
    if any(g.get("entropie") != str(entropie) for g in gp.values()):
        raise GardeArret("entropie ≠ celle du pilote")
    neuves = graines(cles, entropie)
    ecarts = [k for k in cles if gp.get(k) != neuves[k]]
    if ecarts:
        raise GardeArret(f"graines ≠ celles du pilote pour {len(ecarts)} clés (dont {ecarts[0]!r})")


def executer(config: dict, racine: Path, run_id: str, prereg: str | None, chemin_taches: str,
             autoriser_depot_sale: bool = False) -> dict:
    racine = Path(racine)
    exiger_config_notations(config)
    if config["mode"] == "reel" and prereg is None:
        raise GardeArret("run réel des notations sans préenregistrement : R1 interdit de lancer")
    taches = charger_taches(chemin_taches)
    sha_taches = verifier(chemin_taches)
    exiger_invites(config)
    pilote = charger_pilote_note(racine, config["run_pilote"])
    if pilote["arret"].get("partiel", {}).get("taches_sha256") != sha_taches:
        raise GardeArret("tâches ≠ celles du pilote (arret.json, partiel.taches_sha256)")
    exiger_egal_au_pilote(config, pilote, config["mode"])
    commit_cite = None
    entropie = int(next(iter(pilote["manifeste"]["graines"].values()))["entropie"])
    if prereg is not None:
        exiger_code_importe_sous(racine)
        commit_cite = exiger_code_cite(racine, Path(prereg))
        entropie = exiger_citations_notations(Path(prereg), config, sha_taches, pilote)
    par_id = {t["identifiant"]: t for t in taches}
    demandes = {j["nom"]: demandes_decisives(pilote, par_id, config, j["nom"]) for j in config["juges"]}
    for nom, dem in demandes.items():
        if len(dem) != config["notations_attendues_par_juge"]:
            raise GardeArret(f"juge {nom} : {len(dem)} notations à faire, {config['notations_attendues_par_juge']} "
                             f"attendues")
    cles = cles_des_graines(demandes)
    exiger_graines_du_pilote(cles, entropie, pilote)
    # état et début du run calculés avant le manifeste : entre sa création et le bloc qui consigne l'arrêt, plus rien ne
    # s'exécute (vérification courte du code, constat 1)
    etat = {"etape": "chargement", "commit_cite": commit_cite, "run_pilote": config["run_pilote"],
            "episodes_sha256": pilote["episodes_sha256"], "taches_sha256": sha_taches,
            "config_sha256": empreinte_config(config), "juges": {}}
    debut = time.perf_counter()
    chemin_m, manifeste = creer_manifeste(racine, run_id, config, cles, entropie=entropie,
                                          decisif=prereg is not None, prereg=prereg,
                                          autoriser_depot_sale=autoriser_depot_sale, commande=COMMANDE)
    try:
        return _apres_manifeste(config, racine, chemin_m, manifeste, pilote, demandes, etat, debut)
    except Exception as e:          # garde, panne, signal TERM, échéance globale : consigné, puis propagé
        ecrire_resultat(racine, chemin_m, "arret", {"etape": etat["etape"], "motif": motif_d_arret(e),
                                                     "partiel": {k: v for k, v in etat.items() if k != "etape"},
                                                     "duree_s": round(time.perf_counter() - debut, 1)})
        relever_term_apres(e)
        raise


def _apres_manifeste(config, racine, chemin_m, manifeste, pilote, demandes, etat, debut) -> dict:
    g = manifeste["graines"]
    echeance_globale = debut + float(config["duree_globale_s"])
    from ..harnais.modeles import noyaux_attention_permis, regler_determinisme

    reglages = regler_determinisme(config["fils"], "cuda" if config["mode"] == "reel" else "cpu")
    etat["reglages"] = reglages
    juges = config["juges"]
    agent = next(j for j in juges if j["meme_modele_que_agent"])
    # chargement (téléchargement en mode réel) du juge qui est l'agent, consigné sous son étape propre, comme au pilote
    # (contre-lecture R2, angle « code du lanceur »)
    etat["etape"] = f"chargement du juge {agent['nom']}"
    depart = time.perf_counter()
    modele, fmt = charger_modele_et_format(config["agent"], config["mode"], graine_entiere(g["modele-jouet"]))
    chargements = {agent["nom"]: round(time.perf_counter() - depart, 1)}
    # formats contrôlés au début, contre ceux, scellés, du début du pilote (relecture du plan, constat 11)
    etat["etape"] = "contrôle du format"
    formats = {}
    for j in juges:
        fmt_j = fmt if j["meme_modele_que_agent"] else charger_format_seul(j, config["mode"])
        formats[j["nom"]] = controler_format(fmt_j, j, "juge", config)
        if formats[j["nom"]] != pilote["formats"].get(f"juge-{j['nom']}"):
            raise GardeArret(f"juge {j['nom']} : format ≠ celui du début du pilote")
    etat["etape"] = "préchargement des juges"
    etat["precharges"] = precharger_juges(config)
    noyaux = noyaux_attention_permis() if torch.cuda.is_available() else None
    modeles = {agent["nom"]: (modele, fmt)}
    sorties = {}
    for j in juges:
        nom = j["nom"]
        if nom not in modeles:
            etat["etape"] = f"chargement du juge {nom}"
            depart = time.perf_counter()
            m_j, fmt_j = charger_modele_et_format(j, config["mode"], graine_entiere(g["modele-jouet"]) + 1,
                                                  hors_ligne=True)
            chargements[nom] = round(time.perf_counter() - depart, 1)
            if controler_format(fmt_j, j, "juge", config) != formats[nom]:
                raise GardeArret(f"{nom} : format chargé hors ligne ≠ format contrôlé au début du run")
            modeles[nom] = (m_j, fmt_j)
        m_j, fmt_j = modeles[nom]
        etat["etape"] = f"notations decisives par {nom}"
        dem = demandes[nom]
        lot = config["lot_juge"]
        lots = [dem[k:k + lot] for k in range(0, len(dem), lot)]
        graines_j = {d["cle"]: graine_entiere(g[d["cle"]]) for d in dem}
        depart_j = time.perf_counter()
        # échéance du juge : le premier (8B) depuis le début du run, les suivants depuis leur premier lot
        echeance_j = (debut if nom == agent["nom"] else depart_j) + float(config["duree_max_juges_s"][nom])
        # compteurs consignés pendant le run (résumé, arrêt) : lots seulement ; les jetons ne sont consignés que pour un
        # juge écrit, avec son fichier (aucune part du résultat d'un juge échu ou arrêté ; contre-lecture R2)
        suivi = {"lots": len(lots), "lots_faits": 0, "statut": "en cours"}
        etat["juges"][nom] = suivi
        memoire_pic_gio()
        sortie, jetons = [], 0
        for k, morceau in enumerate(lots, 1):
            exiger_sans_signal(f"avant le lot {k} du juge {nom}")
            if time.perf_counter() > echeance_j:
                suivi["statut"] = "échu"
                break
            t0 = time.perf_counter()
            part = noter_ensembles(m_j, fmt_j, morceau, graines_j, lot, config["max_nouveaux_juge"],
                                   config["temperature_juge"], echeance=echeance_globale)
            sortie += part
            suivi["lots_faits"] = k
            jetons += sum(x["jetons_reponse"] for x in part)
            # rang et durée du lot seulement : aucun compte de réponses (tronquées, complètes, jetons), qui serait une
            # part du résultat décisif visible pendant le run (contre-lecture R2)
            progres(juge=nom, lot=f"{k}/{len(lots)}", duree_s=f"{time.perf_counter() - t0:.1f}")
        suivi["duree_s"] = round(time.perf_counter() - depart_j, 1)
        suivi["memoire_pic_gio"] = memoire_pic_gio()
        if suivi["statut"] == "en cours":
            ecrire_resultat(racine, chemin_m, f"notations-{nom}-decisives", {
                "notations": sortie, "noyau": "défaut de la bibliothèque", "noyaux_permis": noyaux,
                "descriptifs": {"duree_s": suivi["duree_s"], "memoire_pic_gio": suivi["memoire_pic_gio"],
                                "jetons_generes": jetons, "lots": len(lots)}})
            suivi["statut"] = "écrit"
            suivi["jetons_generes"] = jetons
            suivi["notations"] = len(sortie)
            suivi["completes"] = sum(1 for x in sortie if x["score"] is not None)
        progres(juge=nom, fin=suivi["statut"], lots_faits=f"{suivi['lots_faits']}/{len(lots)}",
                duree_s=suivi["duree_s"])
        # mémoire rendue avant le juge suivant
        del modeles[nom], m_j, fmt_j
        if nom == agent["nom"]:
            del modele, fmt
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

    etat["etape"] = "résumé"
    resume = {"run_pilote": config["run_pilote"], "commit_cite": etat["commit_cite"],
              "config_sha256": etat["config_sha256"], "taches_sha256": etat["taches_sha256"],
              "episodes_sha256": etat["episodes_sha256"], "juges": etat["juges"], "chargements_s": chargements,
              "precharges": etat["precharges"], "reglages": reglages,
              "duree_s": round(time.perf_counter() - debut, 1)}
    exiger_sans_signal("avant le résumé")
    ecrire_resultat(racine, chemin_m, "resume", resume)
    lire_manifeste(chemin_m)
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
