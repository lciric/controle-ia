"""Lanceur de T0.6 côté instance, v3 (contre-lecture neuve du lanceur v2, corrections C-V3-1 et C-V3-4 ; nom neuf, R12 :
`lanceur.py` et `lanceur_v2.py` restent tels quels, leurs étapes inchangées sont importées). Changements :
- C-V3-1 : chaque morceau du sous-ensemble d'activations est rempli jusqu'à une borne de **tableaux** plus petite que la
  borne du fichier (85 000 000 octets, ou borne du fichier − 1 Mo − 1 000 octets par action, la plus petite des deux) ; la
  vérification du fichier écrit reste à 90 000 000 octets (le dépôt distant refuse au-delà de 100 Mo) ; un fichier écrit qui
  dépasse quand même est retiré et réécrit en deux morceaux (récursivement), **jamais un arrêt de la course** ; avant tout
  épisode, une garde exige qu'une action au pire cas (`max_nouveaux` × largeur × 2 octets) tienne dans un morceau ;
- C-V3-4 : notation de Mahalanobis au choix de la configuration (`mahalanobis_calcul`, `configuration_v3`) : paquet gelé
  (défaut) ou `sondes/familles_v2` (produit matriciel) ; dans ce second cas, l'essai d'égalité au paquet gelé est joué
  **avant chaque usage** de chaque sonde (256 jetons tirés, écart relatif ≤ 10⁻¹²) ; un essai en échec met le couple en
  « échec » (jamais l'ensemble) ; le calcul retenu et chaque essai sont écrits dans le résultat scellé des sondes.
Inchangé de la v2 : C01, C02, C03, C06, C07, C11 (manifeste scellé), C16, L04, L05 ; lignes `PROGRES` sans état.
"""
from __future__ import annotations

import argparse
import gc
import json
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
from ..sondes import familles_v2 as fv2
from . import distillation_transcription as dt
from . import test_croise as tc
from .configuration import ADAPTATEURS, condition_decisive_adaptateur, condition_temoin_dose_1, conditions_evaluation, nom_condition
from .configuration_v2 import exiger_pas_declares, pas_de_distillation_declares
from .configuration_v3 import calcul_mahalanobis, exiger_config_t06_v3
from .identite import controle_identite, logits_de_controle
from .lanceur import (_ecrire_textes, charger_taches_t06, charger_textes_p3, cles_des_graines, couts_par_condition,
                      distiller_adaptateur, effectifs_des_lignes, empreinte_config, exemples_honnetes, exiger_citations_t06,
                      jouer_distillation, jouer_evaluation, progres, tableaux_des_mesures)
from .lanceur_v2 import (CLES_RESUME_SCELLEES_SEULEMENT, ActivationsDemi, actions_de_la_couche, exiger_place_disque, pire_cas_octets,
                         resume_imprimable)
from .lecture_v2 import lecture_cout_v2, lecture_sondes_v2

COMMANDE = "python -m controle_ia.t06.lanceur_v3"
MORCEAU_MAX_OCTETS = 90_000_000            # C11 : borne du FICHIER écrit (le dépôt distant refuse tout fichier de plus de 100 Mo)
MORCEAU_TABLEAUX_MAX_OCTETS = 85_000_000   # C-V3-1 : borne de remplissage des TABLEAUX d'un morceau (enveloppe npz ≈ 17 ko / 49 actions)
ENVELOPPE_MARGE_OCTETS = 1_000_000         # C-V3-1 : marge fixe d'enveloppe, et
ENVELOPPE_PAR_ACTION_OCTETS = 1_000        # marge par action (mesure : ≈ 340 octets par tableau)

__all__ = ["ActivationsDemi", "exiger_place_disque", "pire_cas_octets", "resume_imprimable", "CLES_RESUME_SCELLEES_SEULEMENT"]


def borne_de_remplissage(n_actions: int) -> int:
    """Octets de tableaux admis dans un morceau de `n_actions` actions : la plus petite des deux bornes de C-V3-1."""
    return int(min(MORCEAU_TABLEAUX_MAX_OCTETS, MORCEAU_MAX_OCTETS - ENVELOPPE_MARGE_OCTETS - ENVELOPPE_PAR_ACTION_OCTETS * int(n_actions)))


def pire_cas_action_octets(max_nouveaux: int, largeur: int) -> int:
    return int(max_nouveaux) * int(largeur) * 2


def exiger_action_tient_dans_un_morceau(max_nouveaux: int, largeur: int) -> dict:
    """Garde (C-V3-1), avant tout épisode : une action au pire cas tient dans un morceau ; sinon arrêt avant toute dépense
    (après les épisodes, aucune action ne peut plus être « plus grande qu'un morceau », et aucun arrêt n'a lieu)."""
    pire, borne = pire_cas_action_octets(max_nouveaux, largeur), borne_de_remplissage(1)
    if pire > borne:
        raise GardeArret(f"une action au pire cas ({max_nouveaux} jetons × {largeur} × 2 octets = {pire} octets) ne tient pas dans un "
                         f"morceau ({borne} octets de tableaux) : arrêt avant tout épisode (C-V3-1)")
    return {"pire_cas_action_octets": pire, "borne_remplissage_une_action": borne}


def _ecrire_morceau(courant: dict, dossier: Path, prefixe: str, morceaux: list, reecrits: list) -> None:
    """Écrit un morceau ; si le fichier écrit dépasse `MORCEAU_MAX_OCTETS`, il est retiré et réécrit en deux (C-V3-1)."""
    k = len(morceaux)
    chemin = dossier / f"{prefixe}-{k:03d}.npz"
    if chemin.exists():
        raise GardeArret(f"{chemin} existe déjà (R12)")
    with open(chemin, "wb") as f:
        np.savez(f, __cles__=np.array(sorted(courant)), **courant)
    taille = chemin.stat().st_size
    if taille > MORCEAU_MAX_OCTETS:
        if len(courant) < 2:
            raise GardeArret(f"{chemin.name} : {taille} octets > {MORCEAU_MAX_OCTETS} avec une seule action : impossible à couper "
                             "(exclu par la garde d'avant les épisodes)")
        chemin.unlink()                                    # fichier retiré de l'instance avant tout commit, réécrit en deux
        reecrits.append({"fichier_retire": chemin.name, "octets": int(taille), "actions": len(courant)})
        cles = sorted(courant)
        m = len(cles) // 2
        _ecrire_morceau({c: courant[c] for c in cles[:m]}, dossier, prefixe, morceaux, reecrits)
        _ecrire_morceau({c: courant[c] for c in cles[m:]}, dossier, prefixe, morceaux, reecrits)
        return
    morceaux.append({"fichier": chemin.name, "sha256": sceller(chemin), "actions": len(courant), "octets": int(taille),
                     "octets_tableaux": int(sum(a.nbytes for a in courant.values()))})


def sous_ensemble_en_morceaux(lignes, activations, config, g, dossier: Path, prefixe: str = "activations-sous-ensemble-t06") -> dict:
    """Sous-ensemble d'activations (fraction des actions notées, couche de la sonde, demi-précision), écrit en morceaux npz :
    tableaux remplis jusqu'à `borne_de_remplissage`, fichier vérifié à `MORCEAU_MAX_OCTETS`, fichier trop gros réécrit en deux
    (C-V3-1) ; chaque morceau scellé, manifeste scellé (fichiers, empreintes, clés, réécritures)."""
    rng = generateur(g["sous-ensemble-activations"])
    notees = [l["cle"] for l in lignes if l["jetons_notes"] > 0]
    n = max(1, int(round(float(config["fraction_activations_poussees"]) * len(notees)))) if notees else 0
    choisies = sorted(notees[int(i)] for i in rng.choice(len(notees), size=n, replace=False)) if n else []
    c = int(config["sonde"]["couche"])
    morceaux, reecrits, courant, octets = [], [], {}, 0
    for cle in choisies:
        a = activations.lire(cle, c).astype(np.float16)
        if a.nbytes > borne_de_remplissage(1):
            raise GardeArret(f"action {cle} : {a.nbytes} octets, plus grande qu'un morceau (exclu par la garde d'avant les épisodes)")
        if courant and octets + a.nbytes > borne_de_remplissage(len(courant) + 1):
            _ecrire_morceau(courant, dossier, prefixe, morceaux, reecrits)
            courant, octets = {}, 0
        courant[cle] = a
        octets += a.nbytes
    if courant:
        _ecrire_morceau(courant, dossier, prefixe, morceaux, reecrits)
    manifeste = dossier / f"{prefixe}-manifeste.json"
    if manifeste.exists():
        raise GardeArret(f"{manifeste} existe déjà (R12)")
    corps = {"couche": c, "precision": "float16", "actions": len(choisies), "total_notees": len(notees),
             "morceau_max_octets": MORCEAU_MAX_OCTETS, "tableaux_max_octets": MORCEAU_TABLEAUX_MAX_OCTETS,
             "enveloppe_marge_octets": ENVELOPPE_MARGE_OCTETS, "enveloppe_par_action_octets": ENVELOPPE_PAR_ACTION_OCTETS,
             "morceaux": morceaux, "reecrits": reecrits, "cles": choisies}
    manifeste.write_text(json.dumps(corps, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    return {"manifeste": str(manifeste), "manifeste_sha256": sceller(manifeste), "morceaux": morceaux, "reecrits": reecrits,
            "actions": len(choisies), "couche": c, "total_notees": len(notees)}


def sonde_du_pli_v3(actions, positifs, negatifs, pli_lu, plis, famille, couche, agregation, nom, graine, calcul) -> tuple:
    """`test_croise.sonde_du_pli`, puis, pour une sonde de Mahalanobis sous le calcul v2 : réécriture par produit matriciel et
    essai d'égalité au paquet gelé **avant tout usage** (C-V3-4 ; `GardeArret` si l'écart dépasse la tolérance). Rend la
    sonde, ses jetons d'entraînement et le compte rendu de l'essai (nul sous le paquet gelé)."""
    sonde, seqs = tc.sonde_du_pli(actions, positifs, negatifs, pli_lu, plis, famille, couche, agregation, nom, graine)
    if famille != "mahalanobis" or calcul == fv2.PAQUET_GELE:
        return sonde, seqs, None
    sonde = fv2.en_produit_matriciel(sonde)
    return sonde, seqs, fv2.verifier_egalite_au_paquet_gele(sonde, int(graine))


def test_croise_v3(lignes, activations, config, g) -> dict:
    """Comme `lanceur_v2.test_croise_v2` (C07, C16, lignes de progression sans état), avec le calcul de Mahalanobis de la
    configuration (C-V3-4) : essai d'égalité joué avant chaque usage, écrit par sonde dans le résultat ; un essai en échec met
    le couple en « échec », jamais l'ensemble."""
    s100, t100 = condition_decisive_adaptateur(config), condition_temoin_dose_1(config)
    plis = tc.partition_plis([l["tache"] for l in lignes], graine_entiere(g["partition-taches"]))
    sonde = config["sonde"]
    calcul = calcul_mahalanobis(config)
    n_t, n_p, n_pl = int(config["tirages_aire"]), int(config["permutations_plancher"]), int(config["n_plancher"])
    durees, verifications = {}, {}

    def lire_sens(actions, sens, pos_app, pos_lu, prefixe, famille, couche, agregation, complet):
        sondes, planchers = {}, {}
        for k in (0, 1):
            s, seqs, v = sonde_du_pli_v3(actions, pos_app, "honnete", k, plis, famille, couche, agregation,
                                         f"{prefixe}{sens}-pli{k}", graine_entiere(g[f"{prefixe}sonde/{sens}/pli{k}"]), calcul)
            sondes[k] = s
            if v is not None:
                verifications[f"{prefixe}{sens}/pli{k}"] = v
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
                if f == "mahalanobis":
                    jeux["descriptifs"][nom]["mahalanobis_calcul"] = calcul
                durees[nom] = round(time.perf_counter() - depart, 1)
                progres(etape="couple-descriptif", couple=nom, duree_s=durees[nom])
            del actions
            gc.collect()
    return {"plis": plis, "jeux": jeux, "durees_s": durees, "mahalanobis_calcul": calcul, "verifications_mahalanobis": verifications}


def executer(config: dict, racine: Path, run_id: str, prereg: str | None, autoriser_depot_sale: bool = False) -> dict:
    racine = Path(racine)
    exiger_config_t06_v3(config)
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
    etat["morceau"] = exiger_action_tient_dans_un_morceau(config["max_nouveaux"], largeur)              # C-V3-1, avant tout épisode
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
        "activations_sous_ensemble": {**sous, "manifeste": str(Path(sous["manifeste"]).relative_to(racine)), "precision": "float16",
                                      "morceau_max_octets": MORCEAU_MAX_OCTETS, "tableaux_max_octets": MORCEAU_TABLEAUX_MAX_OCTETS},
        "activations_disque": {"precision": "float16", "dossier": str((dossier / "activations").relative_to(racine))},
        "effectifs": effectifs, "reglages": reglages, "noyau_attention": config["noyau_attention"],
        "format": etat["format"], "descriptifs": descriptifs, "disque": etat["disque"], "morceau": etat["morceau"],
        "duree_s": round(time.perf_counter() - debut, 1)})
    etat["episodes_ecrits"] = len(ev["fiches"])
    progres(etape="episodes-ecrits", episodes=len(ev["fiches"]), actions=len(lignes), morceaux=len(sous["morceaux"]), reecrits=len(sous["reecrits"]))
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
    croise = test_croise_v3(lignes, activations, config, g)
    ls = lecture_sondes_v2(croise["jeux"], lc["table_A"]["ligne"], config, None, False, config["audit"], cn_lecture)
    ecrire_resultat(racine, chemin_m, "lecture-sondes-t06", {"jeux": croise["jeux"], "plis": croise["plis"], "lecture": ls,
                                                             "durees_s": croise["durees_s"], "audit": config["audit"],
                                                             "sonde": config["sonde"], "regle": config["lecture"],
                                                             "mahalanobis_calcul": croise["mahalanobis_calcul"],
                                                             "verifications_mahalanobis": croise["verifications_mahalanobis"],
                                                             "note": "à ne pas ouvrir avant le verdict scellé de P3-bis (DT-4)"})
    etat["etape"] = "résumé"
    resume = {"commit_cite": etat["commit_cite"], "config_sha256": etat["config_sha256"],
              "taches_evaluation_sha256": etat["taches_evaluation_sha256"], "consignes_sha256": etat["consignes_sha256"],
              "adaptateurs": {ad: empreintes[ad] for ad in ADAPTATEURS}, "mesures_sha256": sha_mes, "textes_sha256": sha_t,
              "sous_ensemble_manifeste_sha256": sous["manifeste_sha256"], "morceaux": len(sous["morceaux"]), "morceaux_reecrits": len(sous["reecrits"]),
              "episodes": len(ev["fiches"]), "actions": len(lignes), "actions_notees": sum(effectifs["actions_notees"].values()),
              "mahalanobis_calcul": croise["mahalanobis_calcul"],
              "ligne_A": lc["table_A"]["ligne"], "ligne_B": ls["table_B"]["ligne"], "ligne_C": ls["table_C"]["ligne"],
              "controles_negatifs": {k: v["lecture"] for k, v in cn.items()}, "duree_s": round(time.perf_counter() - debut, 1)}
    exiger_sans_signal("avant le résumé")
    ecrire_resultat(racine, chemin_m, "resume", resume)
    lire_manifeste(chemin_m)
    progres(etape="fin", episodes=len(ev["fiches"]), actions=len(lignes))
    return resume


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
