"""Configuration de T0.6, v2 (contre-lecture du lanceur v1, C04, C05, C15, L04, L05, L11 ; nom neuf, R12 : la v1 reste
telle quelle). Par-dessus `configuration.exiger_config_t06` :
- toute clé non lue par le lanceur est refusée (aucune valeur écrite par le candidat ne peut être ignorée en silence, R5) ;
- `temoin_lexical` et `sondes_figees_p3` doivent être nuls tant qu'ils ne sont pas branchés (C04) ; `fils_test_croise`
  est une clé exigée (C04) ;
- `carte` porte, par carte, le nom attendu de l'offre, la mémoire de carte minimale et le prix horaire maximal (C15, L10),
  la carte de la course et la carte de relance (DT-6) ;
- `calendrier` : dernier jour de création (L11, recommandation du lecteur : 15 novembre 2026) et fin du GO (instant UTC) ;
- `lecture.non_interpretable_si_au_dessus_seulement` (L05, recommandation : vrai) ;
- `distillation.unite_du_lot` (L04 : « transcription », un pas d'AdamW par transcription, 480 pas au plan (b) ; ou
  « action », une paire par action, mode « paires ») et `distillation.pas_declares` (L04 : le nombre de pas déclaré au
  texte, 480 au plan (b) ; vérifié avant le manifeste contre les tâches de distillation, les épisodes par tâche, les époques
  et le lot : `exiger_pas_declares` ; le nombre effectif, après exclusions, est écrit dans le résultat à côté du déclaré) ;
- `familles_descriptives` : familles des couples descriptifs famille × couche (T6-9), la famille décisive comprise (E0 : le coût
  de Mahalanobis sur processeur est linéaire en jetons, ≈ 27 ms par jeton ; l'écarter est une valeur de configuration) ;
- `offre` : bornes de l'offre lues à la création (C12) : mémoire vive, cœurs effectifs, disque, stockage, téléchargement,
  volume de téléchargement prévu (forfait du cumul, C08), étiquette des instances du programme.
Chaque valeur est une valeur de configuration : un changement de Lazar n'est pas du code.
"""
from __future__ import annotations

from datetime import date, datetime, timezone

from ..gardes import GardeArret
from ..sondes.familles import FAMILLES
from .configuration import CLES_DISTILLATION, CLES_T06, exiger_config_t06

CLES_T06_V2 = tuple(CLES_T06) + ("fils_test_croise", "calendrier", "lecture", "offre", "familles_descriptives")
CLES_DISTILLATION_V2 = tuple(CLES_DISTILLATION) + ("unite_du_lot", "pas_declares")
CLES_CARTE = ("course", "relance")
CLES_UNE_CARTE = ("nom", "nom_offre", "memoire_carte_min_mo", "prix_max_usd_h")
CLES_CALENDRIER = ("dernier_jour_creation", "fin_go_utc")
CLES_LECTURE = ("non_interpretable_si_au_dessus_seulement",)
CLES_OFFRE = ("memoire_vive_min_mo", "coeurs_effectifs_min", "disque_min_go", "stockage_max_usd_h", "telechargement_max_usd_go",
              "telechargement_go_prevu", "etiquette")
UNITES_DU_LOT = ("transcription", "action")


def _nombre(v) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def _exiger_carte(c: dict, quoi: str) -> None:
    if not isinstance(c, dict) or set(c) != set(CLES_UNE_CARTE):
        raise GardeArret(f"carte {quoi} : clés {CLES_UNE_CARTE} attendues")
    if not (isinstance(c["nom"], str) and c["nom"] and isinstance(c["nom_offre"], str) and c["nom_offre"]):
        raise GardeArret(f"carte {quoi} : nom et nom d'offre non vides attendus")
    if not (_nombre(c["memoire_carte_min_mo"]) and c["memoire_carte_min_mo"] > 0 and _nombre(c["prix_max_usd_h"])
            and c["prix_max_usd_h"] > 0):
        raise GardeArret(f"carte {quoi} : mémoire de carte et prix maximal strictement positifs attendus")


def exiger_config_t06_v2(config: dict) -> None:
    exiger_config_t06(config)
    inconnues = sorted(set(config) - set(CLES_T06_V2))
    if inconnues:
        raise GardeArret(f"clés de configuration non lues par le lanceur : {inconnues} (refus, R5)")
    manquantes = [c for c in CLES_T06_V2 if c not in config]
    if manquantes:
        raise GardeArret(f"configuration de T0.6 v2 incomplète : {manquantes}")
    for cle in ("temoin_lexical", "sondes_figees_p3"):
        if config[cle] is not None:
            raise GardeArret(f"{cle} : non branché dans ce lanceur ; une valeur serait ignorée (C04) : nul exigé")
    f = config["fils_test_croise"]
    if not isinstance(f, int) or isinstance(f, bool) or f < 1:
        raise GardeArret("fils_test_croise : entier ≥ 1 attendu")
    carte = config["carte"]
    if not isinstance(carte, dict) or set(carte) != set(CLES_CARTE):
        raise GardeArret(f"carte : clés {CLES_CARTE} attendues (course, relance)")
    for k in CLES_CARTE:
        _exiger_carte(carte[k], k)
    cal = config["calendrier"]
    if not isinstance(cal, dict) or set(cal) != set(CLES_CALENDRIER):
        raise GardeArret(f"calendrier : clés {CLES_CALENDRIER} attendues")
    try:
        dernier = date.fromisoformat(cal["dernier_jour_creation"])
        fin = datetime.fromisoformat(cal["fin_go_utc"].replace("Z", "+00:00"))
    except (TypeError, ValueError, AttributeError):
        raise GardeArret("calendrier : dernier_jour_creation (AAAA-MM-JJ) et fin_go_utc (instant UTC) attendus") from None
    if fin.tzinfo is None or fin.utcoffset() != timezone.utc.utcoffset(None):
        raise GardeArret("calendrier : fin_go_utc en UTC attendue")
    if dernier >= fin.date():
        raise GardeArret("calendrier : le dernier jour de création précède la fin du GO")
    le = config["lecture"]
    if not isinstance(le, dict) or set(le) != set(CLES_LECTURE) or not isinstance(le["non_interpretable_si_au_dessus_seulement"], bool):
        raise GardeArret(f"lecture : clés {CLES_LECTURE}, booléen, attendues")
    di = config["distillation"]
    if set(di) != set(CLES_DISTILLATION_V2):
        raise GardeArret(f"distillation : clés {CLES_DISTILLATION_V2} attendues, exactement (L04 : unite_du_lot, pas_declares)")
    if di["unite_du_lot"] not in UNITES_DU_LOT:
        raise GardeArret(f"distillation.unite_du_lot : {UNITES_DU_LOT} attendu (L04)")
    if (di["unite_du_lot"] == "transcription") != (di["mode"] == "transcription"):
        raise GardeArret("distillation : unite_du_lot « transcription » va avec le mode « transcription », « action » avec « paires »")
    if not isinstance(di["pas_declares"], int) or isinstance(di["pas_declares"], bool) or di["pas_declares"] < 1:
        raise GardeArret("distillation.pas_declares : entier ≥ 1 attendu (L04 : 480 au plan (b))")
    fd = config["familles_descriptives"]
    if not isinstance(fd, list) or not fd or len(set(fd)) != len(fd) or any(f not in FAMILLES for f in fd):
        raise GardeArret(f"familles_descriptives : liste non vide, sans doublon, parmi {FAMILLES} attendue (E0 : Mahalanobis coûte "
                         "≈ 27 ms par jeton sur processeur ; la retirer est une valeur de configuration, pas du code)")
    if config["sonde"]["famille"] not in fd:
        raise GardeArret("familles_descriptives : la famille de la sonde décisive doit en faire partie")
    o = config["offre"]
    if not isinstance(o, dict) or set(o) != set(CLES_OFFRE):
        raise GardeArret(f"offre : clés {CLES_OFFRE} attendues")
    for k in CLES_OFFRE:
        if k == "etiquette":
            if not isinstance(o[k], str) or not o[k]:
                raise GardeArret("offre.etiquette : texte non vide attendu")
        elif not _nombre(o[k]) or o[k] < 0:
            raise GardeArret(f"offre.{k} : nombre positif attendu")


def fin_go_utc_s(config: dict) -> int:
    return int(datetime.fromisoformat(config["calendrier"]["fin_go_utc"].replace("Z", "+00:00")).timestamp())


def pas_de_distillation_declares(config: dict, n_transcriptions: int, n_actions: int) -> dict:
    """Nombre de pas d'AdamW effectif (L04) : une transcription par pas en mode « transcription », une action par pas en
    mode « paires », multiplié par les époques et divisé par le lot ; comparé au nombre déclaré (`pas_declares`)."""
    d = config["distillation"]
    unites = n_transcriptions if d["unite_du_lot"] == "transcription" else n_actions
    pas = int(d["epoques"]) * (-(-int(unites) // int(d["lot"])))
    return {"unite_du_lot": d["unite_du_lot"], "unites": int(unites), "epoques": int(d["epoques"]), "lot": int(d["lot"]),
            "pas": pas, "pas_declares": int(d["pas_declares"]), "conforme_au_declare": pas == int(d["pas_declares"])}


def pas_attendus_avant_dependance(config: dict, n_taches_distillation: int) -> int:
    """Pas d'AdamW attendus avant toute dépense, au plan (b) : tâches de réserve × épisodes par tâche transcriptions par
    adaptateur (× T actions en mode « paires »), sans exclusion."""
    d = config["distillation"]
    unites = int(n_taches_distillation) * int(config["episodes_par_tache_distillation"])
    if d["unite_du_lot"] == "action":
        unites *= int(config["T"])
    return int(d["epoques"]) * (-(-unites // int(d["lot"])))


def exiger_pas_declares(config: dict, n_taches_distillation: int) -> dict:
    """Garde (L04) : au plan (b), le nombre déclaré au texte égale le nombre attendu des tâches de réserve ; sinon arrêt
    avant le manifeste. Au plan (a), le nombre d'épisodes vient du fichier des textes : vérifié au résultat seulement."""
    attendus = pas_attendus_avant_dependance(config, n_taches_distillation)
    declares = int(config["distillation"]["pas_declares"])
    if config["decisions"]["DT-1"] == "b" and attendus != declares:
        raise GardeArret(f"distillation : {declares} pas déclarés (L04) ≠ {attendus} pas attendus "
                         f"({n_taches_distillation} tâches × {config['episodes_par_tache_distillation']} épisodes, "
                         f"{config['distillation']['epoques']} époques, lot {config['distillation']['lot']}) : aucune création")
    return {"pas_declares": declares, "pas_attendus": attendus, "plan": config["decisions"]["DT-1"]}
