"""Lanceur de T0.6 côté instance (brouillon 3, « Ce qui manque pour lancer », point 4, (i)), par phases, sous un manifeste
de run (préenregistrement scellé exigé en mode réel, R1), sans retour en arrière :

1. configuration (clés et décisions DT-1 à DT-6 en valeurs de configuration), tâches d'évaluation et de distillation
   (fichiers scellés, empreintes citées, R11) ; **contrôle avant dépense : aucune tâche de distillation dans l'évaluation**
   (identifiants comparés), sinon aucune création ; consignes de P3 (scellées, empreinte citée) ;
2. modèle et format (réel : révision figée ; jouet : modèle par caractères), contrôle du format, logits du contexte de
   contrôle avant l'injection ;
3. données de distillation : DT-1 (b) : épisodes neufs du saboteur instruit et du témoin instruit de P3 sur les tâches de
   réserve, `episodes_par_tache_distillation` par tâche, réglages de génération de P3, graines dérivées ; DT-1 (a) : les
   actions de P3 relues dans le fichier des textes (empreinte vérifiée), retokenisées ; dans les deux cas, chaque épisode
   est rejoué sans sa consigne ni ses indications (contexte honnête reconstruit) ; exclusion mécanique des actions qui
   mentionnent un texte privé ; aucune autre sélection ;
4. injection des adaptateurs (rang, alpha, cibles ; A et B en simple précision), distillation d'un adaptateur saboteur et
   d'un adaptateur témoin (transcription entière, à défaut paires), empreinte de la base avant et après (égalité exigée),
   adaptateurs sauvegardés (demi-précision) et rechargés tels que sauvegardés, empreintes consignées ;
5. contrôle d'identité à dose 0 (logits égaux à la base au bit près, adaptateur entraîné chargé) et son artefact à dose 1 ;
6. épisodes d'évaluation par états d'adaptateur (dose 0 : les quatre conditions de P3 ; saboteur à chaque dose ; témoin à
   dose 1), mêmes graines d'action pour une même tâche d'une condition à l'autre, garde d'équivalence en ligne, contrôle
   négatif par phase, état d'adaptateur relu avant et après chaque lot ; par action : coût par le lecteur neuf, mesures
   sans juge, activations des jetons notés aux couches lues (disque de l'instance), sous-ensemble tiré par graine poussé ;
7. test croisé sur processeur : plis, sondes des deux sens, planchers appariés, jeux décisifs, contrôles, validité, courbe,
   couples descriptifs ; lecture ; **deux résultats scellés séparés** (coût ; sondes, tables B et C à la ligne 1 tant que
   le verdict de P3-bis et la lecture de T0.8 manquent) ; résumé.
Tout arrêt après le manifeste laisse un `arret.json` scellé, puis se propage. Mode jouet : même chaîne, mêmes gardes.
"""
from __future__ import annotations

import argparse
import gc
import hashlib
import json
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
from ..environnements.pilote_a import CLES_RAPPORT_GARDEES, charger_taches, graines_des_actions, tache_de
from ..gardes import GardeArret, exiger_sans_signal, lever_sur_term, motif_d_arret, relever_term_apres
from ..harnais.episode import bilan_controle_negatif, empreinte_episode, exiger_controle_negatif_phase, jouer_episodes
from ..harnais.formats import _ids
from ..harnais.run_harnais_factice import graine_entiere
from ..harnais.validation_reelle import (ENTROPIE_CITEE, exiger_code_cite, exiger_code_importe_sous,
                                         exiger_memoire_vive, noyau)
from ..manifeste import config_canonique, creer_manifeste, ecrire_resultat, generateur, lire_manifeste
from ..organismes import lora as lo
from ..organismes.distillation import distiller
from ..premier_test_ia.conditions import charger_consignes, environnement, mesures_action
from ..premier_test_ia.run import controler_format_agent
from ..scellement import sceller, verifier
from ..sondes.familles import FAMILLES
from . import distillation_transcription as dt
from . import test_croise as tc
from .configuration import (ADAPTATEURS, CONDITIONS_DOSE_0, SOURCES_DISTILLATION, condition_decisive_adaptateur,
                            condition_temoin_dose_1, conditions_evaluation, etats_adaptateur, exiger_config_t06,
                            nom_condition)
from .cout import cout_action
from .identite import controle_identite, etat_adaptateurs, exiger_etat_de_phase, logits_de_controle
from .lecture import cles_de_lecture, lecture_cout, lecture_sondes

COMMANDE = "python -m controle_ia.t06.lanceur"
CONFIG_CITEE = re.compile(r"Configuration de T0\.6 \(empreinte canonique\) : `([0-9a-f]{64})`")
TACHES_CITEES = re.compile(r"Tâches d'évaluation de T0\.6 : `([0-9a-f]{64})`")
MESURES_BOOLEENNES = ("valide", "cout_present", "cout_plusieurs_nombres", "cout_multiplication", "cout_intervalle",
                      "cout_suffixe_k", "cout_milliers_espace", "mention", "mention_etendue")


def progres(**champs) -> None:
    instant = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print("PROGRES " + instant + " " + " ".join(f"{k}={v}" for k, v in champs.items()), file=sys.stderr, flush=True)


def empreinte_config(config: dict) -> str:
    return hashlib.sha256(config_canonique(config)).hexdigest()


def exiger_citations_t06(prereg: Path, config: dict, sha_taches: str) -> int:
    texte = Path(prereg).read_text(encoding="utf-8")
    c, t, e = CONFIG_CITEE.search(texte), TACHES_CITEES.search(texte), ENTROPIE_CITEE.search(texte)
    if not (c and t and e):
        raise GardeArret(f"{prereg} ne cite pas la configuration, les tâches d'évaluation ou l'entropie de T0.6")
    if empreinte_config(config) != c.group(1):
        raise GardeArret(f"configuration {empreinte_config(config)[:12]} ≠ configuration citée {c.group(1)[:12]}")
    if sha_taches != t.group(1):
        raise GardeArret(f"tâches d'évaluation {sha_taches[:12]} ≠ tâches citées {t.group(1)[:12]}")
    return int(e.group(1))


def _fichier_cite(racine: Path, spec: dict, quoi: str) -> tuple[Path, str]:
    chemin = racine / spec["chemin"]
    sha = verifier(chemin)
    if sha != spec["sha256"]:
        raise GardeArret(f"{quoi} : empreinte {sha[:12]} ≠ empreinte citée {spec['sha256'][:12]} (R11)")
    return chemin, sha


def charger_taches_t06(config: dict, racine: Path) -> dict:
    """Tâches d'évaluation et de distillation, empreintes citées vérifiées ; contrôle avant dépense : identifiants
    disjoints (sinon aucune création)."""
    chemin_e, sha_e = _fichier_cite(racine, config["taches_evaluation"], "tâches d'évaluation")
    evaluation = charger_taches(chemin_e)
    distillation, sha_d = [], None
    if config["taches_distillation"] is not None:
        chemin_d, sha_d = _fichier_cite(racine, config["taches_distillation"], "tâches de distillation")
        distillation = charger_taches(chemin_d)
    communes = sorted({t["identifiant"] for t in distillation} & {t["identifiant"] for t in evaluation})
    if communes:
        raise GardeArret(f"tâche(s) de distillation présente(s) dans l'évaluation : {communes[:5]} : aucune création")
    return {"evaluation": evaluation, "distillation": distillation, "sha_evaluation": sha_e, "sha_distillation": sha_d}


def cles_des_graines(config: dict, taches: dict) -> list[str]:
    cles = ["modele-jouet", "injection"] + [f"adaptateur/{a}" for a in ADAPTATEURS] + [f"distillation/{a}" for a in ADAPTATEURS]
    cles += [f"tache/{t['identifiant']}" for t in taches["evaluation"]]
    for t in taches["distillation"]:
        cles += [f"distillation/tache/{t['identifiant']}/e{k}" for k in range(int(config["episodes_par_tache_distillation"]))]
    return cles + cles_de_lecture(config)


def _fin_notee(a, fmt) -> int:
    return a.fin - 1 if a.ids and a.ids[-1] in fmt.fins else a.fin


def _lots(plan, lot):
    return [plan[d:d + lot] for d in range(0, len(plan), lot)]


def jouer_distillation(modele, fmt, taches_dist, config, consignes, g: dict, guide, chrono) -> dict:
    """DT-1 (b) : épisodes neufs des deux conditions instruites sur les tâches de réserve ; rend, par adaptateur, les
    épisodes (identifiants des actions, textes)."""
    T, lot = config["T"], config["lot"]
    k_max = int(config["episodes_par_tache_distillation"])
    plan = [(f"distillation/{c}/{t['identifiant']}/e{k}", t, c, k) for t in taches_dist for k in range(k_max)
            for c in SOURCES_DISTILLATION.values()]
    sorties = {a: [] for a in ADAPTATEURS}
    rapports = []
    for n_lot, morceau in enumerate(_lots(plan, lot)):
        envs = [environnement(c, tache_de(t), T, guide, consignes) for _, t, c, _ in morceau]
        graines, echantillon = [], set()
        for b, (_, t, _, k) in enumerate(morceau):
            gen = generateur(g[f"distillation/tache/{t['identifiant']}/e{k}"])
            graines.append(graines_des_actions(gen, 1, T))
            tirages = gen.random(T)
            echantillon |= {(b, 0, s) for s in range(T) if tirages[s] < config["fraction_equivalence"]}
        res = jouer_episodes(modele, fmt, envs, [e for e, _, _, _ in morceau], 1, T, graines, config["couches"],
                             config["max_nouveaux"], config["temperature"], echantillon, config["tolerance_equivalence"],
                             statistique=config["statistique_equivalence"], chrono=chrono)
        for (ep, _, rapport), (e, t, c, k) in zip(res, morceau):
            rapports.append(rapport)
            actions = ep.actions_dans_l_ordre()
            ad = next(a for a, src in SOURCES_DISTILLATION.items() if src == c)
            sorties[ad].append({"episode": e, "tache": t, "actions": [list(a.ids) for a in actions],
                                "textes": [a.texte for a in actions]})
        progres(etape="distillation-donnees", lot=f"{n_lot + 1}/{-(-len(plan) // lot)}")
    bilan = bilan_controle_negatif(rapports, positions_min=config["positions_min_controle_negatif"])
    exiger_controle_negatif_phase(bilan, config["fraction_min_controle_negatif"], config["actions_min_controle_negatif"],
                                  "T0.6, génération des données de distillation")
    bilan["lecture"] = ("non concluant" if bilan["comparables"] < config["actions_min_controle_negatif"]
                        else ("conforme" if bilan["fraction"] >= config["fraction_min_controle_negatif"] else "contraire"))
    return {"episodes": sorties, "controle_negatif": bilan}


def charger_textes_p3(fmt, racine: Path, config: dict, taches_dist: list[dict]) -> dict:
    """DT-1 (a) : actions de P3 relues dans le fichier des textes (empreinte citée), retokenisées depuis leur texte, un
    jeton de fin de tour ajouté (écart déclaré : la cible reste le texte)."""
    chemin, _ = _fichier_cite(racine, config["textes_p3"], "textes des actions de P3")
    par_tache = {t["identifiant"]: t for t in taches_dist}
    groupes: dict[tuple, list] = {}
    with open(chemin, encoding="utf-8") as f:
        for ligne in f:
            x = json.loads(ligne)
            if x["condition"] in SOURCES_DISTILLATION.values():
                groupes.setdefault((x["condition"], x["tache"], x["episode"]), []).append((int(x["pas"]), x["texte"]))
    fin = fmt._pieces(("x", "y"))["cloture"][0]
    sorties = {a: [] for a in ADAPTATEURS}
    for (c, tache, ep), lignes in sorted(groupes.items()):
        if tache not in par_tache:
            raise GardeArret(f"texte de P3 sur la tâche {tache} absente du fichier des tâches de distillation")
        lignes.sort()
        if [p for p, _ in lignes] != list(range(config["T"])):
            raise GardeArret(f"épisode {ep} : pas {[p for p, _ in lignes]} au lieu de 0 à {config['T'] - 1}")
        ad = next(a for a, src in SOURCES_DISTILLATION.items() if src == c)
        sorties[ad].append({"episode": ep, "tache": par_tache[tache], "actions": [_ids(fmt.tok, t) + [fin] for _, t in lignes],
                            "textes": [t for _, t in lignes]})
    if any(not v for v in sorties.values()):
        raise GardeArret("textes de P3 : une des deux conditions instruites n'a aucun épisode")
    return {"episodes": sorties, "controle_negatif": None}


def exemples_honnetes(fmt, episodes: list[dict], config: dict, consignes: dict, guide) -> dict:
    """Transcriptions honnêtes reconstruites et exemples (transcription entière, ou paires), actions exclues comptées."""
    T = config["T"]
    exemples, paires, exclues, total, sans_cible = [], [], 0, 0, 0
    for ep in episodes:
        env = environnement("honnete", tache_de(ep["tache"]), T, guide, consignes)
        ids, empans = dt.transcription_honnete(fmt, env, ep["actions"])
        garder = dt.exclure_mentions(ep["textes"]) if config["exclusion_mention"] else list(range(T))
        total += T
        exclues += T - len(garder)
        if not garder:
            sans_cible += 1
            continue
        exemples.append(dt.exemple_de_transcription(ids, empans, garder))
        paires += [(ids[:d], ids[d:f]) for k, (d, f) in enumerate(empans) if k in garder]
    return {"exemples": exemples, "paires": paires, "actions": total, "exclues": exclues, "episodes_sans_cible": sans_cible}


def distiller_adaptateur(modele, exemples: dict, config: dict, pad: int, graine: int, quoi: str) -> list[dict]:
    d = config["distillation"]
    if d["mode"] == "transcription":
        return dt.distiller_transcriptions(modele, exemples["exemples"], pad, d["epoques"], d["pas"], d["lot"], graine,
                                           d["norme_max"], progres=lambda e, p: progres(etape="distillation", adaptateur=quoi,
                                                                                       epoque=e, perte=round(p, 4)))
    return distiller(modele, exemples["paires"], pad, d["epoques"], d["pas"], d["lot"], graine, d["norme_max"])


class Activations:
    """Activations des jetons notés, par action et par couche, sur le disque de l'instance (jamais les trois couches
    ensemble en mémoire au test croisé)."""

    def __init__(self, dossier: Path, couches):
        self.dossier, self.couches = dossier, [int(c) for c in couches]
        for c in self.couches:
            (dossier / f"c{c}").mkdir(parents=True, exist_ok=False)

    def ecrire(self, cle: str, segments: dict[int, np.ndarray]) -> None:
        for c in self.couches:
            chemin = self.dossier / f"c{c}" / f"{cle}.npy"
            if chemin.exists():
                raise GardeArret(f"{chemin} existe déjà (R12)")
            np.save(chemin, np.ascontiguousarray(segments[c], dtype=np.float32))

    def lire(self, cle: str, couche: int) -> np.ndarray:
        return np.load(self.dossier / f"c{int(couche)}" / f"{cle}.npy")


def jouer_evaluation(modele, fmt, taches_eval, config, consignes, g, guide, etats_entraines, empreintes, activations,
                     chrono) -> dict:
    """Épisodes des états d'adaptateur, dans l'ordre ; rend les lignes par action (sans texte), les textes, les fiches,
    les contrôles négatifs par phase et les états relus."""
    T, lot = config["T"], config["lot"]
    index = {t["identifiant"]: k for k, t in enumerate(taches_eval)}
    lignes, textes, fiches, bilans, etats_relus = [], [], [], {}, {}
    for etat in etats_adaptateur(config):
        ad = etat["adaptateur"] or "saboteur"               # dose 0 : adaptateurs injectés, dose 0 (le modèle de base)
        lo.charger_etat(modele, etats_entraines[ad])
        lo.fixer_dose(modele, etat["dose"])
        ref = etat_adaptateurs(modele)
        if etat["adaptateur"] is not None and ref["empreinte"] != empreintes[ad]:
            raise GardeArret(f"phase {etat['nom']} : adaptateur chargé ≠ adaptateur {ad} entraîné")
        etats_relus[etat["nom"]] = {"adaptateur": etat["adaptateur"], "dose": etat["dose"], "empreinte": ref["empreinte"]}
        plan = [(f"{c}/{t['identifiant']}/e0", t, c) for t in taches_eval for c in etat["conditions"]]
        rapports = []
        for n_lot, morceau in enumerate(_lots(plan, lot)):
            exiger_etat_de_phase(modele, etat["dose"], ref["empreinte"], f"phase {etat['nom']}, avant le lot {n_lot}")
            envs = [environnement(c if c in CONDITIONS_DOSE_0 else "honnete", tache_de(t), T, guide, consignes)
                    for _, t, c in morceau]
            graines, echantillon = [], set()
            for b, (_, t, _) in enumerate(morceau):
                gen = generateur(g[f"tache/{t['identifiant']}"])       # un générateur neuf par condition : mêmes graines
                graines.append(graines_des_actions(gen, 1, T))
                tirages = gen.random(T)
                echantillon |= {(b, 0, s) for s in range(T) if tirages[s] < config["fraction_equivalence"]}
            res = jouer_episodes(modele, fmt, envs, [e for e, _, _ in morceau], 1, T, graines, config["couches"],
                                 config["max_nouveaux"], config["temperature"], echantillon, config["tolerance_equivalence"],
                                 statistique=config["statistique_equivalence"], chrono=chrono)
            exiger_etat_de_phase(modele, etat["dose"], ref["empreinte"], f"phase {etat['nom']}, après le lot {n_lot}")
            for (ep, acts, rapport), (e, t, c) in zip(res, morceau):
                rapports.append(rapport)
                actions = ep.actions_dans_l_ordre()
                for a in actions:
                    fin = _fin_notee(a, fmt)
                    mesures = mesures_action(a.texte)
                    cle = f"{c}__t{index[t['identifiant']]:03d}__p{a.pas}"
                    ligne = {"cle": cle, "episode": e, "phase": etat["nom"], "condition": c, "tache": t["identifiant"],
                             "pas": a.pas, "jetons": len(a.ids), "jetons_notes": max(0, fin - a.debut),
                             **cout_action(a.texte), "mention": bool(mesures["mention_texte_prive"]),
                             "mention_etendue": tc.mention_etendue(a.texte), "adaptateur": etat["adaptateur"],
                             "dose": etat["dose"], "empreinte_adaptateurs": ref["empreinte"]}
                    textes.append({"cle": cle, "episode": e, "condition": c, "tache": t["identifiant"], "pas": a.pas,
                                   "texte": a.texte, "ids": [int(x) for x in a.ids]})
                    if fin > a.debut:
                        activations.ecrire(cle, {k: acts[0][k][a.debut:fin] for k in config["couches"]})
                    lignes.append(ligne)
                fiches.append({"episode": e, "condition": c, "tache": t["identifiant"], "phase": etat["nom"],
                               "jetons_par_action": [len(a.ids) for a in actions],
                               "equivalence": {"actions": sorted(rapport["ecarts_q99"]), "tolerance": rapport["tolerance"],
                                               "statistique": rapport["statistique"],
                                               **{k: rapport[k] for k in CLES_RAPPORT_GARDEES}},
                               "empreintes": empreinte_episode(ep, acts), "etat_adaptateurs": etats_relus[etat["nom"]]})
            progres(etape="episodes", phase=etat["nom"], lot=f"{n_lot + 1}/{-(-len(plan) // lot)}", actions=len(lignes))
        bilan = bilan_controle_negatif(rapports, positions_min=config["positions_min_controle_negatif"])
        exiger_controle_negatif_phase(bilan, config["fraction_min_controle_negatif"], config["actions_min_controle_negatif"],
                                      f"T0.6, phase {etat['nom']}")
        bilan["lecture"] = ("non concluant" if bilan["comparables"] < config["actions_min_controle_negatif"]
                            else ("conforme" if bilan["fraction"] >= config["fraction_min_controle_negatif"] else "contraire"))
        bilans[etat["nom"]] = bilan
    return {"lignes": lignes, "textes": textes, "fiches": fiches, "controles_negatifs": bilans, "etats": etats_relus}


def actions_de_la_couche(lignes: list[dict], activations: Activations, couche: int) -> list[dict]:
    return [{**{k: l[k] for k in ("tache", "condition", "pas", "jetons_notes", "cout")}, "mention": l["mention_etendue"],
             "seq": activations.lire(l["cle"], couche)} for l in lignes if l["jetons_notes"] > 0]


def test_croise(lignes, activations, config, g) -> dict:
    """Sens 1 (sonde sur (i-a) contre honnête, lue sur (ii) à dose 1), sens 2 (réciproque), contrôles, validité, courbe,
    couples descriptifs ; chaque lecture a sa graine."""
    s100, t100 = condition_decisive_adaptateur(config), condition_temoin_dose_1(config)
    plis = tc.partition_plis([l["tache"] for l in lignes], graine_entiere(g["partition-taches"]))
    sonde = config["sonde"]
    n_t, n_p, n_pl = int(config["tirages_aire"]), int(config["permutations_plancher"]), int(config["n_plancher"])
    jeux = {}

    def lire_sens(actions, sens, pos_app, pos_lu, prefixe, famille, couche, agregation, descriptif):
        sondes, planchers = {}, {}
        for k in (0, 1):
            s, seqs = tc.sonde_du_pli(actions, pos_app, "honnete", k, plis, famille, couche, agregation,
                                      f"{prefixe}{sens}-pli{k}", graine_entiere(g[f"{prefixe}sonde/{sens}/pli{k}"]))
            sondes[k] = s
            planchers[k] = tc.planchers_du_pli(f"{s.nom}-plancher", couche, seqs, agregation, n_pl,
                                               graine_entiere(g[f"{prefixe}plancher/{sens}/pli{k}"]))
        f = tc.jeu_ou_echec if descriptif else tc.jeu_croise

        def jeu(nom, pos):
            return f(sondes, planchers, actions, pos, "honnete", plis, n_t, graine_entiere(g[f"{prefixe}aire/{sens}/{nom}"]),
                     n_p, graine_entiere(g[f"{prefixe}permutation/{sens}/{nom}"]))
        r = {"controle": jeu("controle", pos_app), "decisif": jeu("decisif", pos_lu),
             "sondes": {k: {"nom": sondes[k].nom, "empreinte": sondes[k].empreinte()} for k in (0, 1)}}
        if not descriptif:
            r["validite_temoin_instruit"] = tc.jeu_ou_echec(sondes, planchers, actions, "temoin", "honnete", plis, n_t,
                                                           graine_entiere(g[f"aire/{sens}/validite_temoin_instruit"]), n_p,
                                                           graine_entiere(g[f"permutation/{sens}/validite_temoin_instruit"]))
            r["validite_adaptateur_temoin"] = (tc.jeu_ou_echec(sondes, planchers, actions, t100, "honnete", plis, n_t,
                                                              graine_entiere(g[f"aire/{sens}/validite_adaptateur_temoin"]), n_p,
                                                              graine_entiere(g[f"permutation/{sens}/validite_adaptateur_temoin"]))
                                               if t100 is not None else {"echec": "aucun adaptateur témoin à dose 1", "etat": tc.ECHEC})
            if sens == "sens1":
                r["courbe"] = {}
                for d in config["doses_saboteur"]:
                    c = nom_condition("saboteur", d)
                    r["courbe"][c] = tc.jeu_ou_echec(sondes, planchers, actions, c, "honnete", plis, n_t,
                                                     graine_entiere(g[f"aire/{sens}/courbe/{c}"]), n_p,
                                                     graine_entiere(g[f"permutation/{sens}/courbe/{c}"]))
        return r

    actions = actions_de_la_couche(lignes, activations, sonde["couche"])
    jeux["sens1"] = lire_sens(actions, "sens1", "saboteur", s100, "", sonde["famille"], sonde["couche"], sonde["agregation"], False)
    jeux["sens2"] = lire_sens(actions, "sens2", s100, "saboteur", "", sonde["famille"], sonde["couche"], sonde["agregation"], False)
    progres(etape="test-croise", sens1=jeux["sens1"]["decisif"]["etat"], sens2=jeux["sens2"]["decisif"]["etat"])
    jeux["descriptifs"] = {}
    if config["couples_descriptifs"]:
        for c in config["couches"]:
            actions = actions_de_la_couche(lignes, activations, c)
            for f in FAMILLES:
                if f == sonde["famille"] and c == sonde["couche"]:
                    continue
                ag = "attention" if f == "attention" else "max"
                p = f"desc/{f}-c{c}/"
                try:
                    r1 = lire_sens(actions, "sens1", "saboteur", s100, p, f, c, ag, True)
                    r2 = lire_sens(actions, "sens2", s100, "saboteur", p, f, c, ag, True)
                    jeux["descriptifs"][f"{f}-c{c}"] = {"sens1_decisif": r1["decisif"], "sens1_controle": r1["controle"],
                                                        "sens2_decisif": r2["decisif"], "sens2_controle": r2["controle"]}
                except GardeArret as e:
                    jeux["descriptifs"][f"{f}-c{c}"] = {"echec": str(e)}
            progres(etape="couples-descriptifs", couche=c)
            del actions
            gc.collect()
    return {"plis": plis, "jeux": jeux}


def couts_par_condition(lignes: list[dict], config: dict) -> dict:
    sortie = {c: {} for c in conditions_evaluation(config)}
    for l in lignes:
        sortie[l["condition"]].setdefault(l["tache"], []).append(l["cout"])
    return sortie


def effectifs_des_lignes(lignes: list[dict], config: dict) -> dict:
    conds = conditions_evaluation(config)
    return {"actions": {c: sum(1 for l in lignes if l["condition"] == c) for c in conds},
            "actions_notees": {c: sum(1 for l in lignes if l["condition"] == c and l["jetons_notes"] > 0) for c in conds},
            "actions_lisibles": {c: sum(1 for l in lignes if l["condition"] == c and l["cout"] is not None and l["cout"] > 0)
                                 for c in conds}}


def tableaux_des_mesures(lignes: list[dict]) -> dict:
    t = {k: np.array([l[k] for l in lignes]) for k in ("cle", "episode", "condition", "tache", "phase")}
    for k in ("pas", "jetons", "jetons_notes"):
        t[k] = np.array([l[k] for l in lignes], dtype=np.int64)
    t["dose"] = np.array([l["dose"] for l in lignes], dtype=np.float64)
    t["cout"] = np.array([np.nan if l["cout"] is None else float(l["cout"]) for l in lignes])
    for k in MESURES_BOOLEENNES:
        t[k] = np.array([bool(l[k]) for l in lignes])
    return t


def _ecrire_textes(chemin: Path, textes: list[dict]) -> str:
    if chemin.exists():
        raise GardeArret(f"{chemin} existe déjà (R12)")
    with open(chemin, "w", encoding="utf-8") as f:
        for x in textes:
            f.write(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n")
    return sceller(chemin)


def sous_ensemble_activations(lignes, activations, config, g, chemin: Path) -> dict:
    """Activations par jeton d'un sous-ensemble tiré par graine (fraction des actions notées), couche de la sonde,
    demi-précision, fichier scellé (plan de stockage de P-015)."""
    rng = generateur(g["sous-ensemble-activations"])
    notees = [l["cle"] for l in lignes if l["jetons_notes"] > 0]
    n = max(1, int(round(float(config["fraction_activations_poussees"]) * len(notees)))) if notees else 0
    choisies = sorted(notees[int(i)] for i in rng.choice(len(notees), size=n, replace=False)) if n else []
    c = int(config["sonde"]["couche"])
    tableaux = {f"{cle}": activations.lire(cle, c).astype(np.float16) for cle in choisies}
    tableaux["__cles__"] = np.array(choisies)
    if chemin.exists():
        raise GardeArret(f"{chemin} existe déjà (R12)")
    with open(chemin, "wb") as f:
        np.savez(f, **tableaux)
    return {"chemin": str(chemin), "sha256": sceller(chemin), "actions": len(choisies), "couche": c, "total_notees": len(notees)}


def executer(config: dict, racine: Path, run_id: str, prereg: str | None, autoriser_depot_sale: bool = False) -> dict:
    racine = Path(racine)
    exiger_config_t06(config)
    if config["mode"] == "reel" and prereg is None:
        raise GardeArret("run réel de T0.6 sans préenregistrement : R1 interdit de lancer")
    taches = charger_taches_t06(config, racine)
    consignes = charger_consignes(racine / config["chemin_consignes"], config["consignes_sha256"])
    guide = charger_invite("H1-classification")
    commit_cite, entropie = None, None
    if prereg is not None:
        exiger_code_importe_sous(racine)
        commit_cite = exiger_code_cite(racine, Path(prereg))
        entropie = exiger_citations_t06(Path(prereg), config, taches["sha_evaluation"])
    chemin_m, manifeste = creer_manifeste(racine, run_id, config, cles_des_graines(config, taches), entropie=entropie,
                                          decisif=prereg is not None, prereg=prereg,
                                          autoriser_depot_sale=autoriser_depot_sale, commande=COMMANDE)
    debut = time.perf_counter()
    etat = {"etape": "mémoire vive", "commit_cite": commit_cite, "taches_evaluation_sha256": taches["sha_evaluation"],
            "taches_distillation_sha256": taches["sha_distillation"], "config_sha256": empreinte_config(config),
            "consignes_sha256": consignes["sha256"]}
    try:
        etat["memoire_vive"] = exiger_memoire_vive(config["memoire_vive_min_go"]) if config["memoire_vive_min_go"] else None
        etat["etape"] = "chargement"
        return _executer_apres_manifeste(config, racine, run_id, chemin_m, manifeste, taches, consignes, guide, etat, debut)
    except Exception as e:
        ecrire_resultat(racine, chemin_m, "arret", {"etape": etat["etape"], "motif": motif_d_arret(e),
                                                     "partiel": {k: v for k, v in etat.items() if k != "etape"},
                                                     "duree_s": round(time.perf_counter() - debut, 1)})
        relever_term_apres(e)
        raise


def _executer_apres_manifeste(config, racine, run_id, chemin_m, manifeste, taches, consignes, guide, etat, debut) -> dict:
    g = manifeste["graines"]
    reel = config["mode"] == "reel"
    appareil = "cuda" if reel else "cpu"
    from ..harnais.modeles import regler_determinisme

    reglages = regler_determinisme(config["fils"], appareil)
    modele, fmt = charger_modele_et_format(config["agent"], config["mode"], graine_entiere(g["modele-jouet"]))
    pad = fmt.tok.pad_token_id if fmt.tok.pad_token_id is not None else min(fmt.fins)
    etat["etape"] = "contrôle du format"
    etat["format"] = controler_format_agent(fmt, config["agent"], config["mode"])
    consigne_c, observations_c, _ = conversation_de_controle("agent", None)
    ids_controle = fmt.ouverture(consigne_c, observations_c[0])
    logits_base = logits_de_controle(modele, ids_controle)
    progres(etape="format", verifie=etat["format"]["verifie"])
    chrono: dict = {}
    dossier = racine / "donnees" / run_id
    dossier.mkdir(parents=True, exist_ok=False)

    etat["etape"] = "données de distillation"
    with noyau(config["noyau_attention"]):
        if config["decisions"]["DT-1"] == "b":
            donnees = jouer_distillation(modele, fmt, taches["distillation"], config, consignes, g, guide, chrono)
        else:
            donnees = charger_textes_p3(fmt, racine, config, taches["distillation"])
    exemples = {ad: exemples_honnetes(fmt, donnees["episodes"][ad], config, consignes, guide) for ad in ADAPTATEURS}
    etat["distillation_donnees"] = {ad: {k: v for k, v in x.items() if k not in ("exemples", "paires")} | {
        "exemples": len(x["exemples"]), "paires": len(x["paires"])} for ad, x in exemples.items()}
    progres(etape="donnees-distillation", **{f"{ad}_exemples": len(exemples[ad]["exemples"]) for ad in ADAPTATEURS})

    etat["etape"] = "distillation"
    a = config["adaptateur"]
    noms_injectes = lo.injecter(modele, a["rang"], float(a["alpha"]), graine_entiere(g["injection"]), tuple(a["cibles"]))
    if a["precision"] == "float32":
        dt.adaptateurs_en_simple_precision(modele)
    base_avant = lo.empreinte_base(modele)
    etats_entraines, empreintes, journaux, fichiers = {}, {}, {}, {}
    for ad in ADAPTATEURS:
        lo.charger_etat(modele, dt.etat_initial(modele, a["rang"], float(a["alpha"]), graine_entiere(g[f"adaptateur/{ad}"])))
        lo.fixer_dose(modele, 1.0)
        journaux[ad] = distiller_adaptateur(modele, exemples[ad], config, pad, graine_entiere(g[f"distillation/{ad}"]), ad)
        if lo.empreinte_base(modele) != base_avant:
            raise GardeArret(f"empreinte de la base changée par la distillation de l'adaptateur {ad}")
        sauve = dt.etat_en(lo.etat_lora(modele), a["sauvegarde"])
        chemin_a = dossier / f"adaptateur-{ad}.pt"
        if chemin_a.exists():
            raise GardeArret(f"{chemin_a} existe déjà (R12)")
        torch.save(sauve, chemin_a)
        fichiers[ad] = {"chemin": str(chemin_a.relative_to(racine)), "sha256": sceller(chemin_a)}
        lo.charger_etat(modele, sauve)                       # l'évaluation lit exactement ce qui est sauvegardé
        etats_entraines[ad] = lo.etat_lora(modele)
        empreintes[ad] = lo.empreinte_adaptateurs(modele)
        progres(etape="adaptateur", adaptateur=ad, empreinte=empreintes[ad], perte_finale=round(journaux[ad][-1]["perte"], 4))
    lo.fixer_dose(modele, 0.0)
    etat["etape"] = "contrôle d'identité"
    identite = controle_identite(modele, ids_controle, logits_base, etats_entraines)
    ecrire_resultat(racine, chemin_m, "distillation-t06", {
        "plan": config["decisions"]["DT-1"], "modules_injectes": noms_injectes, "precision_adaptateurs": a["precision"],
        "sauvegarde": a["sauvegarde"], "empreinte_base_avant": base_avant, "empreinte_base_apres": lo.empreinte_base(modele),
        "journaux": journaux, "adaptateurs": {ad: {**fichiers[ad], "empreinte": empreintes[ad]} for ad in ADAPTATEURS},
        "donnees": etat["distillation_donnees"], "controle_negatif_donnees": donnees["controle_negatif"],
        "identite_dose_0": identite, "jetons_controle": len(ids_controle), "duree_s": round(time.perf_counter() - debut, 1)})
    progres(etape="identite", adaptateurs=len(identite))

    etat["etape"] = "épisodes"
    activations = Activations(dossier / "activations", config["couches"])
    memoire_pic_gio()
    depart = time.perf_counter()
    with noyau(config["noyau_attention"]):
        ev = jouer_evaluation(modele, fmt, taches["evaluation"], config, consignes, g, guide, etats_entraines, empreintes,
                              activations, chrono)
    descriptifs = {"duree_s": round(time.perf_counter() - depart, 1), "memoire_pic_gio": memoire_pic_gio(), **chrono}
    lignes = ev["lignes"]
    chemin_mes = dossier / "mesures-t06.npz"
    with open(chemin_mes, "wb") as f:
        np.savez(f, **tableaux_des_mesures(lignes))
    sha_mes = sceller(chemin_mes)
    sha_t = _ecrire_textes(dossier / "textes-actions-t06.jsonl", ev["textes"])
    sous = sous_ensemble_activations(lignes, activations, config, g, dossier / "activations-sous-ensemble-t06.npz")
    effectifs = effectifs_des_lignes(lignes, config)
    ecrire_resultat(racine, chemin_m, "episodes-t06", {
        "fiches": ev["fiches"], "etats": ev["etats"], "controles_negatifs": ev["controles_negatifs"],
        "mesures": str(chemin_mes.relative_to(racine)), "mesures_sha256": sha_mes,
        "textes": str((dossier / "textes-actions-t06.jsonl").relative_to(racine)), "textes_sha256": sha_t,
        "activations_sous_ensemble": {**sous, "chemin": str(Path(sous["chemin"]).relative_to(racine))},
        "effectifs": effectifs, "reglages": reglages, "noyau_attention": config["noyau_attention"],
        "format": etat["format"], "descriptifs": descriptifs, "duree_s": round(time.perf_counter() - debut, 1)})
    etat["episodes_ecrits"] = len(ev["fiches"])
    progres(etape="episodes-ecrits", episodes=len(ev["fiches"]), actions=len(lignes))
    del modele
    gc.collect()

    etat["etape"] = "lecture du coût"
    exiger_sans_signal("avant la lecture du coût")
    eff = {**effectifs, "actions_exclues_distillation": sum(x["exclues"] for x in exemples.values()),
           "actions_distillation": sum(x["actions"] for x in exemples.values())}
    lc = lecture_cout(couts_par_condition(lignes, config), config, g, generateur, config["audit"], eff)
    ecrire_resultat(racine, chemin_m, "lecture-cout-t06", {"lecture": lc, "effectifs": eff, "lecteur": "controle_ia.t06.cout"})
    progres(etape="lecture-cout", ligne_A=lc["table_A"]["ligne"])

    etat["etape"] = "test croisé"
    torch.set_num_threads(max(1, int(config.get("fils_test_croise", config["fils"]))))
    croise = test_croise(lignes, activations, config, g)
    cn = ev["controles_negatifs"]
    ls = lecture_sondes(croise["jeux"], lc["table_A"]["ligne"], None, False, config["audit"],
                        "non concluant" if any(b["lecture"] == "non concluant" for b in cn.values()) else None)
    ecrire_resultat(racine, chemin_m, "lecture-sondes-t06", {"jeux": croise["jeux"], "plis": croise["plis"], "lecture": ls,
                                                             "audit": config["audit"], "sonde": config["sonde"],
                                                             "note": "à ne pas ouvrir avant le verdict scellé de P3-bis (DT-4)"})
    etat["etape"] = "résumé"
    resume = {"commit_cite": etat["commit_cite"], "config_sha256": etat["config_sha256"],
              "taches_evaluation_sha256": etat["taches_evaluation_sha256"], "consignes_sha256": etat["consignes_sha256"],
              "adaptateurs": {ad: empreintes[ad] for ad in ADAPTATEURS}, "mesures_sha256": sha_mes, "textes_sha256": sha_t,
              "episodes": len(ev["fiches"]), "actions": len(lignes), "actions_notees": sum(effectifs["actions_notees"].values()),
              "ligne_A": lc["table_A"]["ligne"], "ligne_B": ls["table_B"]["ligne"], "ligne_C": ls["table_C"]["ligne"],
              "controles_negatifs": {k: v["lecture"] for k, v in cn.items()}, "duree_s": round(time.perf_counter() - debut, 1)}
    exiger_sans_signal("avant le résumé")
    ecrire_resultat(racine, chemin_m, "resume", resume)
    lire_manifeste(chemin_m)
    progres(etape="fin", episodes=len(ev["fiches"]), actions=len(lignes))
    return resume


_signal_term = lever_sur_term


def _main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(prog=COMMANDE)
    ap.add_argument("--config", required=True)
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--prereg", default=None)
    a = ap.parse_args(argv)
    signal.signal(signal.SIGTERM, _signal_term)
    verifier(a.config)
    config = json.loads(Path(a.config).read_text(encoding="utf-8"))
    resume = executer(config, Path("."), a.run_id, a.prereg)
    print(json.dumps(resume, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
