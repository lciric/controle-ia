"""Lanceur de T0.6 côté instance, v2 (contre-lecture du lanceur v1 : C01, C02, C03, C06, C07, C11, C16, L04, L05 ; nom neuf,
R12 : `lanceur.py` reste tel quel, ses étapes inchangées sont importées). Changements :
- C01, C02 : aucun état de sonde, aucune aire ni ligne de table dans les lignes `PROGRES`, le journal, la sortie standard
  (`run.json`) ni les traces : les lignes de progression ne portent que l'étape, des comptes et des durées ; le résumé
  imprimé omet les lignes A, B, C, gardées dans le résumé scellé (DT-4, point 6 du plan) ;
- C03 : activations par jeton écrites en demi-précision (float16, valeur hors de portée = arrêt, aucun arrondi
  silencieux vers l'infini) ; place libre vérifiée avant les épisodes contre le pire cas (actions × `max_nouveaux` ×
  largeur × 2 octets × couches, plus 10 %), sinon arrêt avant tout épisode ;
- C06 : exclusions comptées par adaptateur (réserve de la table A par adaptateur), contrôle négatif non concluant sous la
  table A (`lecture_v2`) ;
- C07 : jeux décisifs et de contrôle par `jeu_ou_echec` : un jeu qui échoue (tirages dégénérés) a l'état « échec », lignes
  B4 et C4 ; jamais un arrêt du run après les épisodes ;
- C11 : sous-ensemble d'activations poussé en morceaux de moins de 90 Mo, chacun scellé, avec un manifeste scellé ;
- C16 : activations d'une couche libérées avant d'en charger une autre ; durée de chaque couple descriptif en `PROGRES` ;
- L04 : nombre de pas d'AdamW déclaré par adaptateur (`configuration_v2.pas_de_distillation_declares`) ;
- L05 : état « non interprétable » selon la règle de configuration (`lecture.non_interpretable_si_au_dessus_seulement`).
"""
from __future__ import annotations

import argparse
import gc
import json
import shutil
import signal
import sys
import time
from pathlib import Path

import numpy as np
import torch

from ..environnements.invites import charger_invite
from ..environnements.lancer_pilote_a import charger_modele_et_format, conversation_de_controle, memoire_pic_gio
from ..gardes import GardeArret, exiger_sans_signal, lever_sur_term, motif_d_arret, relever_term_apres
from ..harnais.run_harnais_factice import graine_entiere
from ..harnais.validation_reelle import exiger_code_cite, exiger_code_importe_sous, exiger_memoire_vive, noyau
from ..manifeste import creer_manifeste, ecrire_resultat, generateur, lire_manifeste
from ..organismes import lora as lo
from ..premier_test_ia.conditions import charger_consignes
from ..premier_test_ia.run import controler_format_agent
from ..scellement import sceller
from . import distillation_transcription as dt
from . import test_croise as tc
from .configuration import ADAPTATEURS, condition_decisive_adaptateur, condition_temoin_dose_1, conditions_evaluation, nom_condition
from .configuration_v2 import exiger_config_t06_v2, exiger_pas_declares, pas_de_distillation_declares
from .identite import controle_identite, logits_de_controle
from .lanceur import (_ecrire_textes, charger_taches_t06, charger_textes_p3, cles_des_graines, couts_par_condition,
                      distiller_adaptateur, effectifs_des_lignes, empreinte_config, exemples_honnetes, exiger_citations_t06,
                      jouer_distillation, jouer_evaluation, progres, tableaux_des_mesures)
from .lecture_v2 import lecture_cout_v2, lecture_sondes_v2

COMMANDE = "python -m controle_ia.t06.lanceur_v2"
MORCEAU_MAX_OCTETS = 90_000_000            # C11 : le dépôt distant refuse tout fichier de plus de 100 Mo
MARGE_DISQUE = 1.10
FLOAT16_MAX = float(np.finfo(np.float16).max)
CLES_RESUME_SCELLEES_SEULEMENT = ("ligne_A", "ligne_B", "ligne_C")


class ActivationsDemi:
    """Activations des jetons notés, par action et par couche, en demi-précision sur le disque de l'instance ; relues en
    simple précision (les sondes calculent en double)."""

    def __init__(self, dossier: Path, couches):
        self.dossier, self.couches = Path(dossier), [int(c) for c in couches]
        for c in self.couches:
            (self.dossier / f"c{c}").mkdir(parents=True, exist_ok=False)

    def ecrire(self, cle: str, segments: dict[int, np.ndarray]) -> None:
        for c in self.couches:
            chemin = self.dossier / f"c{c}" / f"{cle}.npy"
            if chemin.exists():
                raise GardeArret(f"{chemin} existe déjà (R12)")
            a = np.asarray(segments[c], dtype=np.float32)
            if not np.all(np.isfinite(a)) or float(np.abs(a).max(initial=0.0)) > FLOAT16_MAX:
                raise GardeArret(f"activation non finie ou hors de la demi-précision ({cle}, couche {c}) : aucun arrondi silencieux")
            np.save(chemin, np.ascontiguousarray(a.astype(np.float16)))

    def lire(self, cle: str, couche: int) -> np.ndarray:
        return np.load(self.dossier / f"c{int(couche)}" / f"{cle}.npy").astype(np.float32)


def pire_cas_octets(n_actions: int, max_nouveaux: int, largeur: int, n_couches: int) -> int:
    return int(n_actions) * int(max_nouveaux) * int(largeur) * 2 * int(n_couches)


def exiger_place_disque(dossier: Path, octets_attendus: int) -> dict:
    """Garde (C03) : la place libre du disque du dossier couvre le pire cas des activations, plus 10 %."""
    libre = shutil.disk_usage(str(dossier)).free
    exige = int(octets_attendus * MARGE_DISQUE)
    if libre < exige:
        raise GardeArret(f"place disque {libre / 1e9:.1f} Go < pire cas des activations {exige / 1e9:.1f} Go (marge 10 %) : "
                         "arrêt avant tout épisode")
    return {"libre_octets": int(libre), "pire_cas_octets": int(octets_attendus), "exige_octets": exige}


def sous_ensemble_en_morceaux(lignes, activations, config, g, dossier: Path, prefixe: str = "activations-sous-ensemble-t06") -> dict:
    """Sous-ensemble d'activations (fraction des actions notées, couche de la sonde, demi-précision), écrit en morceaux
    npz de moins de `MORCEAU_MAX_OCTETS`, chacun scellé, et un manifeste scellé (fichiers, empreintes, clés)."""
    rng = generateur(g["sous-ensemble-activations"])
    notees = [l["cle"] for l in lignes if l["jetons_notes"] > 0]
    n = max(1, int(round(float(config["fraction_activations_poussees"]) * len(notees)))) if notees else 0
    choisies = sorted(notees[int(i)] for i in rng.choice(len(notees), size=n, replace=False)) if n else []
    c = int(config["sonde"]["couche"])
    morceaux, courant, octets = [], {}, 0

    def vider():
        nonlocal courant, octets
        if not courant:
            return
        k = len(morceaux)
        chemin = dossier / f"{prefixe}-{k:03d}.npz"
        if chemin.exists():
            raise GardeArret(f"{chemin} existe déjà (R12)")
        with open(chemin, "wb") as f:
            np.savez(f, __cles__=np.array(sorted(courant)), **courant)
        taille = chemin.stat().st_size
        if taille > MORCEAU_MAX_OCTETS:
            raise GardeArret(f"{chemin.name} : {taille} octets > {MORCEAU_MAX_OCTETS} : morceau trop gros (C11)")
        morceaux.append({"fichier": chemin.name, "sha256": sceller(chemin), "actions": len(courant), "octets": int(taille)})
        courant, octets = {}, 0

    for cle in choisies:
        a = activations.lire(cle, c).astype(np.float16)
        if a.nbytes > MORCEAU_MAX_OCTETS:
            raise GardeArret(f"action {cle} : {a.nbytes} octets, plus grande qu'un morceau")
        if octets + a.nbytes > MORCEAU_MAX_OCTETS:
            vider()
        courant[cle] = a
        octets += a.nbytes
    vider()
    manifeste = dossier / f"{prefixe}-manifeste.json"
    if manifeste.exists():
        raise GardeArret(f"{manifeste} existe déjà (R12)")
    corps = {"couche": c, "precision": "float16", "actions": len(choisies), "total_notees": len(notees), "morceau_max_octets": MORCEAU_MAX_OCTETS,
             "morceaux": morceaux, "cles": choisies}
    manifeste.write_text(json.dumps(corps, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    return {"manifeste": str(manifeste), "manifeste_sha256": sceller(manifeste), "morceaux": morceaux, "actions": len(choisies),
            "couche": c, "total_notees": len(notees)}


def actions_de_la_couche(lignes: list[dict], activations, couche: int) -> list[dict]:
    return [{**{k: l[k] for k in ("tache", "condition", "pas", "jetons_notes", "cout")}, "mention": l["mention_etendue"],
             "seq": activations.lire(l["cle"], couche)} for l in lignes if l["jetons_notes"] > 0]


def test_croise_v2(lignes, activations, config, g) -> dict:
    """Comme `lanceur.test_croise`, mais chaque jeu passe par `jeu_ou_echec` (C07), les activations d'une couche sont
    libérées avant d'en charger une autre (C16), la durée de chaque couple est consignée, et les lignes de progression ne
    portent aucun état."""
    s100, t100 = condition_decisive_adaptateur(config), condition_temoin_dose_1(config)
    plis = tc.partition_plis([l["tache"] for l in lignes], graine_entiere(g["partition-taches"]))
    sonde = config["sonde"]
    n_t, n_p, n_pl = int(config["tirages_aire"]), int(config["permutations_plancher"]), int(config["n_plancher"])
    durees = {}

    def lire_sens(actions, sens, pos_app, pos_lu, prefixe, famille, couche, agregation, complet):
        sondes, planchers = {}, {}
        for k in (0, 1):
            s, seqs = tc.sonde_du_pli(actions, pos_app, "honnete", k, plis, famille, couche, agregation,
                                      f"{prefixe}{sens}-pli{k}", graine_entiere(g[f"{prefixe}sonde/{sens}/pli{k}"]))
            sondes[k] = s
            planchers[k] = tc.planchers_du_pli(f"{s.nom}-plancher", couche, seqs, agregation, n_pl,
                                               graine_entiere(g[f"{prefixe}plancher/{sens}/pli{k}"]))

        def jeu(nom, pos):
            return tc.jeu_ou_echec(sondes, planchers, actions, pos, "honnete", plis, n_t, graine_entiere(g[f"{prefixe}aire/{sens}/{nom}"]),
                                   n_p, graine_entiere(g[f"{prefixe}permutation/{sens}/{nom}"]))
        r = {"controle": jeu("controle", pos_app), "decisif": jeu("decisif", pos_lu),
             "sondes": {k: {"nom": sondes[k].nom, "empreinte": sondes[k].empreinte()} for k in (0, 1)}}
        if complet:
            r["validite_temoin_instruit"] = jeu("validite_temoin_instruit", "temoin")
            r["validite_adaptateur_temoin"] = (jeu("validite_adaptateur_temoin", t100) if t100 is not None
                                               else {"echec": "aucun adaptateur témoin à dose 1", "etat": tc.ECHEC})
            if sens == "sens1":
                r["courbe"] = {nom_condition("saboteur", d): jeu(f"courbe/{nom_condition('saboteur', d)}", nom_condition("saboteur", d))
                               for d in config["doses_saboteur"]}
        return r

    depart = time.perf_counter()
    actions = actions_de_la_couche(lignes, activations, sonde["couche"])
    jeux = {"sens1": lire_sens(actions, "sens1", "saboteur", s100, "", sonde["famille"], sonde["couche"], sonde["agregation"], True),
            "sens2": lire_sens(actions, "sens2", s100, "saboteur", "", sonde["famille"], sonde["couche"], sonde["agregation"], True)}
    durees["decisif"] = round(time.perf_counter() - depart, 1)
    progres(etape="test-croise", jeux=2, duree_s=durees["decisif"])
    del actions
    gc.collect()
    jeux["descriptifs"] = {}
    if config["couples_descriptifs"]:
        for c in config["couches"]:
            gc.collect()                                   # C16 : rien de la couche précédente n'est plus référencé ici
            actions = actions_de_la_couche(lignes, activations, c)
            for f in config["familles_descriptives"]:            # familles en configuration (E0 : coût de Mahalanobis)
                if f == sonde["famille"] and c == sonde["couche"]:
                    continue
                ag = "attention" if f == "attention" else "max"
                p, nom = f"desc/{f}-c{c}/", f"{f}-c{c}"
                depart = time.perf_counter()
                try:
                    r1 = lire_sens(actions, "sens1", "saboteur", s100, p, f, c, ag, False)
                    r2 = lire_sens(actions, "sens2", s100, "saboteur", p, f, c, ag, False)
                    jeux["descriptifs"][nom] = {"sens1_decisif": r1["decisif"], "sens1_controle": r1["controle"],
                                                "sens2_decisif": r2["decisif"], "sens2_controle": r2["controle"]}
                except GardeArret as e:
                    jeux["descriptifs"][nom] = {"echec": str(e)}
                durees[nom] = round(time.perf_counter() - depart, 1)
                progres(etape="couple-descriptif", couple=nom, duree_s=durees[nom])
            del actions
            gc.collect()
    return {"plis": plis, "jeux": jeux, "durees_s": durees}


def executer(config: dict, racine: Path, run_id: str, prereg: str | None, autoriser_depot_sale: bool = False) -> dict:
    racine = Path(racine)
    exiger_config_t06_v2(config)
    if config["mode"] == "reel" and prereg is None:
        raise GardeArret("run réel de T0.6 sans préenregistrement : R1 interdit de lancer")
    taches = charger_taches_t06(config, racine)
    pas_declares = exiger_pas_declares(config, len(taches["distillation"]))          # L04, avant toute dépense
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
            "consignes_sha256": consignes["sha256"], "pas_declares": pas_declares}
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
    largeur = int(modele.config.hidden_size)
    etat["etape"] = "contrôle du format"
    etat["format"] = controler_format_agent(fmt, config["agent"], config["mode"])
    consigne_c, observations_c, _ = conversation_de_controle("agent", None)
    ids_controle = fmt.ouverture(consigne_c, observations_c[0])
    logits_base = logits_de_controle(modele, ids_controle)
    progres(etape="format", verifie=etat["format"]["verifie"])
    chrono: dict = {}
    dossier = racine / "donnees" / run_id
    dossier.mkdir(parents=True, exist_ok=False)
    etat["etape"] = "place disque"
    n_actions = len(taches["evaluation"]) * len(conditions_evaluation(config)) * int(config["T"])
    etat["disque"] = exiger_place_disque(dossier, pire_cas_octets(n_actions, config["max_nouveaux"], largeur, len(config["couches"])))
    progres(etape="disque", libre_go=round(etat["disque"]["libre_octets"] / 1e9, 1), pire_cas_go=round(etat["disque"]["pire_cas_octets"] / 1e9, 1))

    etat["etape"] = "données de distillation"
    with noyau(config["noyau_attention"]):
        if config["decisions"]["DT-1"] == "b":
            donnees = jouer_distillation(modele, fmt, taches["distillation"], config, consignes, g, guide, chrono)
        else:
            donnees = charger_textes_p3(fmt, racine, config, taches["distillation"])
    exemples = {ad: exemples_honnetes(fmt, donnees["episodes"][ad], config, consignes, guide) for ad in ADAPTATEURS}
    etat["distillation_donnees"] = {ad: {k: v for k, v in x.items() if k not in ("exemples", "paires")} | {
        "exemples": len(x["exemples"]), "paires": len(x["paires"]),
        "pas_declares": pas_de_distillation_declares(config, len(x["exemples"]), len(x["paires"]))} for ad, x in exemples.items()}
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
        lo.charger_etat(modele, sauve)
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
        "pas_declares": etat["pas_declares"], "identite_dose_0": identite, "jetons_controle": len(ids_controle),
        "duree_s": round(time.perf_counter() - debut, 1)})
    progres(etape="identite", adaptateurs=len(identite))

    etat["etape"] = "épisodes"
    activations = ActivationsDemi(dossier / "activations", config["couches"])
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
    sous = sous_ensemble_en_morceaux(lignes, activations, config, g, dossier)
    effectifs = effectifs_des_lignes(lignes, config)
    ecrire_resultat(racine, chemin_m, "episodes-t06", {
        "fiches": ev["fiches"], "etats": ev["etats"], "controles_negatifs": ev["controles_negatifs"],
        "mesures": str(chemin_mes.relative_to(racine)), "mesures_sha256": sha_mes,
        "textes": str((dossier / "textes-actions-t06.jsonl").relative_to(racine)), "textes_sha256": sha_t,
        "activations_sous_ensemble": {**sous, "manifeste": str(Path(sous["manifeste"]).relative_to(racine)), "precision": "float16"},
        "activations_disque": {"precision": "float16", "dossier": str((dossier / "activations").relative_to(racine))},
        "effectifs": effectifs, "reglages": reglages, "noyau_attention": config["noyau_attention"],
        "format": etat["format"], "descriptifs": descriptifs, "disque": etat["disque"], "duree_s": round(time.perf_counter() - debut, 1)})
    etat["episodes_ecrits"] = len(ev["fiches"])
    progres(etape="episodes-ecrits", episodes=len(ev["fiches"]), actions=len(lignes), morceaux=len(sous["morceaux"]))
    del modele
    gc.collect()

    cn = ev["controles_negatifs"]
    cn_lecture = "non concluant" if any(b["lecture"] == "non concluant" for b in cn.values()) else None
    etat["etape"] = "lecture du coût"
    exiger_sans_signal("avant la lecture du coût")
    eff = {**effectifs, "exclusions_par_adaptateur": {ad: {"exclues": x["exclues"], "actions": x["actions"]} for ad, x in exemples.items()}}
    lc = lecture_cout_v2(couts_par_condition(lignes, config), config, g, generateur, config["audit"], eff, cn_lecture)
    ecrire_resultat(racine, chemin_m, "lecture-cout-t06", {"lecture": lc, "effectifs": eff, "lecteur": "controle_ia.t06.cout",
                                                           "note": "lu dans l'ordre du point 7 du plan, avant tout verdict de la table A"})
    progres(etape="lecture-cout", duree_s=round(time.perf_counter() - debut, 1))

    etat["etape"] = "test croisé"
    torch.set_num_threads(max(1, int(config["fils_test_croise"])))
    croise = test_croise_v2(lignes, activations, config, g)
    ls = lecture_sondes_v2(croise["jeux"], lc["table_A"]["ligne"], config, None, False, config["audit"], cn_lecture)
    ecrire_resultat(racine, chemin_m, "lecture-sondes-t06", {"jeux": croise["jeux"], "plis": croise["plis"], "lecture": ls,
                                                             "durees_s": croise["durees_s"], "audit": config["audit"],
                                                             "sonde": config["sonde"], "regle": config["lecture"],
                                                             "note": "à ne pas ouvrir avant le verdict scellé de P3-bis (DT-4)"})
    etat["etape"] = "résumé"
    resume = {"commit_cite": etat["commit_cite"], "config_sha256": etat["config_sha256"],
              "taches_evaluation_sha256": etat["taches_evaluation_sha256"], "consignes_sha256": etat["consignes_sha256"],
              "adaptateurs": {ad: empreintes[ad] for ad in ADAPTATEURS}, "mesures_sha256": sha_mes, "textes_sha256": sha_t,
              "sous_ensemble_manifeste_sha256": sous["manifeste_sha256"], "morceaux": len(sous["morceaux"]),
              "episodes": len(ev["fiches"]), "actions": len(lignes), "actions_notees": sum(effectifs["actions_notees"].values()),
              "ligne_A": lc["table_A"]["ligne"], "ligne_B": ls["table_B"]["ligne"], "ligne_C": ls["table_C"]["ligne"],
              "controles_negatifs": {k: v["lecture"] for k, v in cn.items()}, "duree_s": round(time.perf_counter() - debut, 1)}
    exiger_sans_signal("avant le résumé")
    ecrire_resultat(racine, chemin_m, "resume", resume)
    lire_manifeste(chemin_m)
    progres(etape="fin", episodes=len(ev["fiches"]), actions=len(lignes))
    return resume


def resume_imprimable(resume: dict) -> dict:
    """Résumé imprimé sur la sortie standard (`run.json`, versé aux traces) : sans les lignes des tables (C02)."""
    return {k: v for k, v in resume.items() if k not in CLES_RESUME_SCELLEES_SEULEMENT}


_signal_term = lever_sur_term


def _main(argv: list[str]) -> int:
    from ..scellement import verifier

    ap = argparse.ArgumentParser(prog=COMMANDE)
    ap.add_argument("--config", required=True)
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--prereg", default=None)
    a = ap.parse_args(argv)
    signal.signal(signal.SIGTERM, _signal_term)
    verifier(a.config)
    config = json.loads(Path(a.config).read_text(encoding="utf-8"))
    resume = executer(config, Path("."), a.run_id, a.prereg)
    print(json.dumps(resume_imprimable(resume), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
