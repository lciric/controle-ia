"""Repli de l'étape A de T0.7 : **recalcul des activations** (brouillon 19, `07039ed2…`, plan, point 8, « Repli de l'étape A » ;
CLT7-08 ; R11), v1. Fichier neuf : la garde d'équivalence reste celle de `repli_v1.py` (inchangé) ; ce module écrit le rejeu,
avec le code de la chaîne de T0.6 désormais sur la branche (fusion de `main`, code de `1609a4bf`), **appelé tel quel** :
`environnements.lancer_pilote_a.charger_modele_et_format` et `conversation_de_controle`, `harnais.modeles.regler_determinisme`,
`organismes.lora` (`injecter`, `charger_etat`, `etat_lora`, `empreinte_adaptateurs`, `fixer_dose`),
`t06.distillation_transcription.adaptateurs_en_simple_precision`, `t06.identite` (`logits_de_controle`, `controle_identite`),
`t06.lanceur` (`charger_taches_t06`, `_fin_notee`), `t06.configuration` (`etats_adaptateur`, `CONDITIONS_DOSE_0`),
`premier_test_ia.conditions` (`environnement`, `charger_consignes`), `environnements.pilote_a.tache_de`,
`environnements.invites.charger_invite`, `harnais.episode.Action`, `harnais.activations.passe_unique`, `t06.lanceur_v2.ActivationsDemi`.

Déroulé (`recalculer`), dans l'ordre du texte :
1. manifeste de 7b (`runs/<run>/manifeste.json`) : configuration (`agent`, `mode`, `adaptateur`, `T`, `couches`, doses,
   tâches, consignes, `statistique_equivalence`, `tolerance_equivalence`, `fraction_min_controle_negatif`) et graines
   (`modele-jouet`, `injection`) ; modèle et format chargés comme la chaîne (réel : fichiers du cache local seulement) ;
2. logits de contrôle de la base, **avant** l'injection (comme `lanceur_v6`) ; injection des adaptateurs avec la configuration
   `adaptateur` de 7b ; chargement de `adaptateur-saboteur.pt` et `adaptateur-temoin.pt` (chemins et empreintes de
   `distillation-t06.json` → `resultat.adaptateurs` ; sceau du fichier, puis **empreinte des adaptateurs chargés égale** à celle
   écrite) ; **contrôle d'identité à dose 0** (`controle_identite` : logits égaux à la base au bit près, artefact à dose 1) ;
3. **rejeu en forçage** de chaque épisode, état d'adaptateur par état d'adaptateur (`etats_adaptateur`, dose de chaque
   condition) : la conversation est reconstruite comme `harnais.episode.jouer_episodes` la construit (N = 1 : `ouverture` au
   pas 0, puis `tour`, `cloture` après chaque action ; observation de l'environnement de la tâche et de la condition, journal
   des textes décodés), les jetons de chaque action étant les identifiants générés écrits dans `textes-actions-t06.jsonl`
   (`ids` ; le texte décodé doit égaler `texte`, et la clé la clé de la chaîne, sinon arrêt) ; une passe unique par épisode ;
   empan noté `[début, _fin_notee[` ; activations écrites en demi-précision par `ActivationsDemi` (refus si le dossier existe,
   R12) ;
4. **garde d'équivalence** (`repli_v1.garde_equivalence`) sur chaque action du sous-ensemble poussé, à la couche du
   sous-ensemble, statistique, tolérance et fraction du contrôle négatif lues dans le manifeste de 7b ; échec → `GardeArret`
   (R11 : arrêt avant toute lecture ; relance une fois sur la même carte, puis nœud : décision de la session, hors du module).

**Éprouvé en mode jouet seulement** (modèle jouet par caractères du harnais) ; en mode réel, le chemin est le même avec le
modèle de la révision figée, en `cuda`, hors ligne : jamais lancé ici.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from ..gardes import GardeArret, exiger_sans_signal
from ..manifeste import lire_manifeste, verifier_resultat
from ..scellement import verifier
from . import repli_v1 as rp

EMPAN_DECALAGE = 0          # essais seulement : décale l'empan noté d'un jeton (artefact du contrôle négatif)


def _empan(action, fmt) -> tuple[int, int]:
    from ..t06.lanceur import _fin_notee
    return action.debut + EMPAN_DECALAGE, _fin_notee(action, fmt) + EMPAN_DECALAGE


def lire_textes_par_episode(chemin: Path) -> dict:
    """`textes-actions-t06.jsonl` → {(condition, tâche) : {pas : enregistrement}} ; doublon → arrêt."""
    sortie: dict = {}
    for k, l in enumerate(Path(chemin).read_text(encoding="utf-8").splitlines(), start=1):
        if not l.strip():
            continue
        x = json.loads(l)
        cle = (str(x["condition"]), str(x["tache"]))
        if int(x["pas"]) in sortie.setdefault(cle, {}):
            raise GardeArret(f"textes de T0.6, ligne {k} : action ({cle}, pas {x['pas']}) en double")
        sortie[cle][int(x["pas"])] = x
    return sortie


def sous_ensemble(racine: Path, run: str, r: dict) -> tuple[dict, int]:
    """Actions du sous-ensemble poussé (clé → tableau en demi-précision) et sa couche, empreintes vérifiées."""
    from .lecture_v1 import _chemin_sous_racine, _exiger, _lire_json
    se = _exiger(r, ("activations_sous_ensemble",), "episodes-t06.resultat")
    chemin_man = _chemin_sous_racine(racine, run, str(_exiger(se, ("manifeste",), "activations_sous_ensemble")))
    if verifier(chemin_man) != _exiger(se, ("manifeste_sha256",), "activations_sous_ensemble"):
        raise GardeArret(f"{chemin_man} : empreinte ≠ activations_sous_ensemble.manifeste_sha256")
    couche = int(_exiger(_lire_json(chemin_man, "manifeste du sous-ensemble"), ("couche",), "manifeste du sous-ensemble"))
    sortie = {}
    for mo in _exiger(se, ("morceaux",), "activations_sous_ensemble"):
        chemin = Path(racine) / "donnees" / run / str(_exiger(mo, ("fichier",), "morceau"))
        if verifier(chemin) != _exiger(mo, ("sha256",), "morceau"):
            raise GardeArret(f"{chemin} : empreinte ≠ celle du morceau")
        with np.load(chemin, allow_pickle=False) as z:
            for cle in z.files:
                if cle != "__cles__":
                    sortie[cle] = np.array(z[cle])
    if not sortie:
        raise GardeArret("R11-arret : sous-ensemble poussé sans aucune action")
    return sortie, couche


def charger_adaptateurs(modele, racine: Path, dist: dict, config: dict, g: dict) -> tuple[dict, dict]:
    """Injection (configuration `adaptateur` de 7b, graine « injection »), puis chaque adaptateur sauvegardé chargé à son sceau,
    empreinte des adaptateurs chargés égale à celle de `distillation-t06.json`."""
    import torch

    from ..harnais.run_harnais_factice import graine_entiere
    from ..organismes import lora as lo
    from ..t06 import distillation_transcription as dt
    from ..t06.configuration import ADAPTATEURS
    a = config["adaptateur"]
    lo.injecter(modele, a["rang"], float(a["alpha"]), graine_entiere(g["injection"]), tuple(a["cibles"]))
    if a["precision"] == "float32":
        dt.adaptateurs_en_simple_precision(modele)
    etats, empreintes = {}, {}
    for ad in ADAPTATEURS:
        f = dist["adaptateurs"][ad]
        chemin = Path(racine) / f["chemin"]
        if verifier(chemin) != f["sha256"]:
            raise GardeArret(f"{chemin} : empreinte ≠ distillation-t06.json (R11)")
        lo.charger_etat(modele, torch.load(chemin, weights_only=True))
        etats[ad] = lo.etat_lora(modele)
        empreintes[ad] = lo.empreinte_adaptateurs(modele)
        if empreintes[ad] != f["empreinte"]:
            raise GardeArret(f"adaptateur {ad} chargé : empreinte {empreintes[ad][:12]}… ≠ distillation-t06.json "
                             f"({str(f['empreinte'])[:12]}…) (R11)")
    lo.fixer_dose(modele, 0.0)
    return etats, empreintes


def rejouer(modele, fmt, config: dict, racine: Path, textes: dict, etats: dict, empreintes: dict, ecrire) -> dict:
    """Rejeu en forçage de tous les épisodes de 7b ; `ecrire(cle, {couche : tableau})` reçoit l'empan noté de chaque action."""
    from ..environnements.invites import charger_invite
    from ..environnements.pilote_a import tache_de
    from ..harnais.activations import passe_unique
    from ..harnais.episode import Action
    from ..organismes import lora as lo
    from ..premier_test_ia.conditions import charger_consignes, environnement
    from ..t06.configuration import CONDITIONS_DOSE_0, etats_adaptateur
    from ..t06.identite import exiger_etat_de_phase
    from ..t06.lanceur import charger_taches_t06
    T = int(config["T"])
    taches = charger_taches_t06(config, racine)["evaluation"]
    index = {t["identifiant"]: k for k, t in enumerate(taches)}
    guide = charger_invite("H1-classification")
    consignes = charger_consignes(Path(racine) / config["chemin_consignes"], config["consignes_sha256"])
    couches = [int(c) for c in config["couches"]]
    episodes = actions_ecrites = 0
    for etat in etats_adaptateur(config):
        ad = etat["adaptateur"] or "saboteur"
        lo.charger_etat(modele, etats[ad])
        lo.fixer_dose(modele, etat["dose"])
        if etat["adaptateur"] is not None:
            exiger_etat_de_phase(modele, etat["dose"], empreintes[ad], f"repli, phase {etat['nom']}")
        for t in taches:
            for c in etat["conditions"]:
                exiger_sans_signal(f"le rejeu de {c}/{t['identifiant']}")
                ecrites = textes.get((c, t["identifiant"]))
                if ecrites is None or sorted(ecrites) != list(range(T)):
                    raise GardeArret(f"repli : épisode {c}/{t['identifiant']} : actions écrites {sorted(ecrites or {})}, pas 0 à {T - 1} attendus")
                env = environnement(c if c in CONDITIONS_DOSE_0 else "honnete", tache_de(t), T, guide, consignes)
                ids, journal, debut, actions = [], [], None, []
                for pas in range(T):
                    rec = ecrites[pas]
                    obs = env.observation(0, pas, journal)
                    if pas == 0:
                        debut = (env.consigne_privee(0), obs)
                        ctx = fmt.ouverture(*debut)
                    else:
                        ctx = ids + fmt.tour(debut, obs)
                    nv = [int(x) for x in rec["ids"]]
                    texte = fmt.tok.decode(nv, skip_special_tokens=True)
                    if texte != rec["texte"]:
                        raise GardeArret(f"repli : action {rec['cle']} : texte décodé des identifiants ≠ texte écrit par la chaîne")
                    cle = f"{c}__t{index[t['identifiant']]:03d}__p{pas}"
                    if cle != rec["cle"]:
                        raise GardeArret(f"repli : clé reconstruite {cle} ≠ clé écrite {rec['cle']}")
                    actions.append((cle, Action(0, pas, len(ctx), len(ctx) + len(nv), nv, texte)))
                    ids = ctx + nv + fmt.cloture(debut, nv)
                    journal.append((0, pas, texte))
                acts = passe_unique(modele, ids, couches)
                for cle, a in actions:
                    d, f = _empan(a, fmt)
                    if f > d:
                        ecrire(cle, {k: acts[k][d:f] for k in couches})
                        actions_ecrites += 1
                episodes += 1
    lo.fixer_dose(modele, 0.0)
    return {"episodes": episodes, "actions_notees_recalculees": actions_ecrites}


def recalculer(racine: Path, run_t06: str, dossier_activations: Path | None = None) -> dict:
    """Recalcul complet (points 1 à 4 du docstring). Écrit `donnees/<run>/activations/c<k>/<cle>.npy` (dossier absent exigé,
    R12 ; ou `dossier_activations`) ; rend le rapport du repli (identité à dose 0, rejeu, garde d'équivalence)."""
    from ..environnements.lancer_pilote_a import charger_modele_et_format, conversation_de_controle
    from ..harnais.modeles import regler_determinisme
    from ..harnais.run_harnais_factice import graine_entiere
    from ..t06.identite import controle_identite, logits_de_controle
    from ..t06.lanceur_v2 import ActivationsDemi
    from .lecture_v1 import lire_episodes_t06
    racine = Path(racine)
    m6, sha_m6 = lire_manifeste(racine / "runs" / run_t06 / "manifeste.json")
    config, g = m6["config"], m6["graines"]
    stat, tol, frac = rp.parametres_equivalence(m6)
    dossier = Path(dossier_activations) if dossier_activations else racine / "donnees" / run_t06 / "activations"
    if dossier.exists():
        raise GardeArret(f"repli : {dossier} existe déjà : le repli ne sert que si les activations de l'instance sont perdues (R12)")
    ep = lire_episodes_t06(racine, run_t06)
    textes = lire_textes_par_episode(Path(racine) / "donnees" / run_t06 / Path(str(ep["resultat"]["textes"])).name)
    sous, couche_se = sous_ensemble(racine, run_t06, ep["resultat"])
    dist = verifier_resultat(racine, racine / "diag" / run_t06 / "distillation-t06.json")["resultat"]
    mode = config["mode"]
    regler_determinisme(config["fils"], "cuda" if mode == "reel" else "cpu")
    modele, fmt = charger_modele_et_format(config["agent"], mode, graine_entiere(g["modele-jouet"]), hors_ligne=(mode == "reel"))
    consigne_c, observations_c, _ = conversation_de_controle("agent", None)
    ids_controle = fmt.ouverture(consigne_c, observations_c[0])
    logits_base = logits_de_controle(modele, ids_controle)
    etats, empreintes = charger_adaptateurs(modele, racine, dist, config, g)
    identite = controle_identite(modele, ids_controle, logits_base, etats)
    activations = ActivationsDemi(dossier, config["couches"])
    rejeu = rejouer(modele, fmt, config, racine, textes, etats, empreintes, activations.ecrire)
    recalculees = {cle: {couche_se: activations.lire(cle, couche_se)} for cle in sous
                   if (dossier / f"c{couche_se}" / f"{cle}.npy").is_file()}
    garde = rp.garde_equivalence(recalculees, sous, couche_se, stat, tol, frac)
    return {"manifeste_7b": {"chemin": f"runs/{run_t06}/manifeste.json", "sha256": sha_m6}, "identite_dose_0": identite,
            "adaptateurs": empreintes, "rejeu": rejeu, "garde_equivalence": garde,
            "dossier_activations": str(dossier.relative_to(racine)) if dossier.is_relative_to(racine) else str(dossier),
            "carte_course": config.get("carte", {}).get("course", {}).get("nom"),
            "regle_d_echec": "échec → relance une fois sur la même carte que la course ; second échec → arrêt, nœud (R11)"}


__all__ = ["recalculer", "rejouer", "charger_adaptateurs", "sous_ensemble", "lire_textes_par_episode", "EMPAN_DECALAGE"]
