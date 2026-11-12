"""Configuration de T0.6 : clés exigées, valeurs par défaut des décisions DT-1 à DT-6 (leurs recommandations), phases et
conditions. Tout ce qui dépend d'une décision de Lazar est une valeur de configuration, jamais du code.

Conditions d'évaluation (brouillon 3, plan d'analyse, point 4) : à dose 0, les quatre conditions de P3 (`honnete`,
`saboteur`, `temoin`, `mention`, textes scellés de P3) ; adaptateur saboteur aux doses de `doses_saboteur` (`S25`, `S50`,
`S75`, `S100`) ; adaptateur témoin aux doses de `doses_temoin` (`T100`). Chaque état d'adaptateur (adaptateur, dose) est une
phase : un lot ne mêle que des conditions de même état (la dose est portée par les modules).
"""
from __future__ import annotations

from ..gardes import GardeArret
from ..premier_test_ia.conditions import CONDITIONS as CONDITIONS_P3

GO_ID = "GO-2026-11-02-28"
PLAFOND_USD = 200.0
DECISIONS_DEFAUT = {"DT-1": "b", "DT-2": "a", "DT-3": "a", "DT-4": "a", "DT-5": "a", "DT-6": "a"}
OPTIONS_DECISIONS = {"DT-1": ("a", "b"), "DT-2": ("a", "b"), "DT-3": ("a", "b"), "DT-4": ("a", "b"), "DT-5": ("a", "b"),
                     "DT-6": ("a", "b")}
ADAPTATEURS = ("saboteur", "temoin")
CONDITIONS_DOSE_0 = tuple(CONDITIONS_P3)            # honnete, saboteur, temoin, mention
SOURCES_DISTILLATION = {"saboteur": "saboteur", "temoin": "temoin"}   # condition de P3 dont l'adaptateur est distillé
CLES_T06 = ("mode", "agent", "N", "T", "lot", "max_nouveaux", "temperature", "couches", "fraction_equivalence",
            "statistique_equivalence", "tolerance_equivalence", "positions_min_controle_negatif",
            "actions_min_controle_negatif", "fraction_min_controle_negatif", "noyau_attention", "fils",
            "memoire_vive_min_go", "decisions", "chemin_consignes", "consignes_sha256", "taches_evaluation",
            "taches_distillation", "textes_p3", "episodes_par_tache_distillation", "exclusion_mention", "adaptateur",
            "distillation", "doses_saboteur", "doses_temoin", "sonde", "n_plancher", "tirages_cout", "tirages_aire",
            "permutations_tendance", "permutations_plancher", "fraction_activations_poussees", "couples_descriptifs",
            "temoin_lexical", "go_id", "plafond_usd", "carte", "audit", "sondes_figees_p3")
CLES_ADAPTATEUR = ("rang", "alpha", "cibles", "precision", "sauvegarde")
CLES_DISTILLATION = ("pas", "epoques", "lot", "norme_max", "mode")
CLES_AUDIT = ("effet_reference_log10", "aire_haute", "aire_basse", "plancher_haut")
MODES_DISTILLATION = ("transcription", "paires")
PRECISIONS = ("float32", "base")
SAUVEGARDES = ("float16", "float32")


def _nombre(v) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def nom_condition(adaptateur: str, dose: float) -> str:
    """`S25`, `S50`, `S75`, `S100` (saboteur), `T100` (témoin) : lettre de l'adaptateur et dose en centièmes."""
    if adaptateur not in ADAPTATEURS:
        raise GardeArret(f"adaptateur {adaptateur!r} inconnu : {ADAPTATEURS}")
    if not 0.0 < float(dose) <= 1.0:
        raise GardeArret(f"dose {dose} hors de ]0, 1] pour une condition d'adaptateur")
    c = int(round(float(dose) * 100))
    if abs(c - float(dose) * 100) > 1e-9:
        raise GardeArret(f"dose {dose} : centièmes entiers attendus")
    return f"{'S' if adaptateur == 'saboteur' else 'T'}{c}"


def exiger_config_t06(config: dict) -> None:
    """Gardes sur la configuration, avant tout manifeste ; aucune valeur cachée (une clé absente arrête)."""
    manquantes = [c for c in CLES_T06 if c not in config]
    if manquantes:
        raise GardeArret(f"configuration de T0.6 incomplète : {manquantes}")
    if config["mode"] not in ("reel", "jouet"):
        raise GardeArret(f"mode {config['mode']!r} inconnu")
    if config["N"] != 1:
        raise GardeArret("T0.6 : un agent par épisode (N = 1)")
    for k in ("T", "lot", "max_nouveaux", "n_plancher", "tirages_cout", "tirages_aire", "permutations_tendance",
              "permutations_plancher", "episodes_par_tache_distillation"):
        if not isinstance(config[k], int) or isinstance(config[k], bool) or config[k] < 1:
            raise GardeArret(f"{k} : entier ≥ 1 attendu, {config[k]!r}")
    d = config["decisions"]
    if not isinstance(d, dict) or set(d) != set(OPTIONS_DECISIONS):
        raise GardeArret(f"décisions : {sorted(OPTIONS_DECISIONS)} attendues, une valeur chacune")
    for k, v in d.items():
        if v not in OPTIONS_DECISIONS[k]:
            raise GardeArret(f"décision {k} : {OPTIONS_DECISIONS[k]} attendues, {v!r}")
    if d["DT-5"] != "a":
        raise GardeArret("DT-5 (b) : (i) à doses p < 1 et contrôles croisés ne sont pas écrits dans ce lanceur (nœud)")
    if d["DT-1"] == "b" and not config["taches_distillation"]:
        raise GardeArret("DT-1 (b) : fichier des tâches de distillation exigé (taches_distillation)")
    if d["DT-1"] == "a" and not (config["textes_p3"] and config["taches_distillation"]):
        raise GardeArret("DT-1 (a) : fichier des textes des actions de P3 (textes_p3) et fichier des tâches de P3 "
                         "(taches_distillation) exigés")
    for cle in ("taches_evaluation", "taches_distillation", "textes_p3", "temoin_lexical", "sondes_figees_p3"):
        v = config[cle]
        if v is not None and not (isinstance(v, dict) and isinstance(v.get("chemin"), str)
                                  and isinstance(v.get("sha256"), str) and len(v["sha256"]) == 64):
            raise GardeArret(f"{cle} : {{chemin, sha256}} attendus (ou null)")
    if config["taches_evaluation"] is None:
        raise GardeArret("taches_evaluation : fichier des tâches d'évaluation exigé")
    a = config["adaptateur"]
    if any(k not in a for k in CLES_ADAPTATEUR):
        raise GardeArret(f"adaptateur : clés {CLES_ADAPTATEUR} attendues")
    if not isinstance(a["rang"], int) or a["rang"] < 1 or not _nombre(a["alpha"]) or a["alpha"] <= 0:
        raise GardeArret("adaptateur : rang ≥ 1 et alpha > 0 attendus")
    if a["precision"] not in PRECISIONS or a["sauvegarde"] not in SAUVEGARDES:
        raise GardeArret(f"adaptateur : précision {PRECISIONS}, sauvegarde {SAUVEGARDES} attendues")
    if not isinstance(a["cibles"], list) or not a["cibles"]:
        raise GardeArret("adaptateur : liste de cibles non vide attendue")
    di = config["distillation"]
    if any(k not in di for k in CLES_DISTILLATION):
        raise GardeArret(f"distillation : clés {CLES_DISTILLATION} attendues")
    if di["mode"] not in MODES_DISTILLATION:
        raise GardeArret(f"distillation : mode {MODES_DISTILLATION} attendu")
    if not (_nombre(di["pas"]) and di["pas"] > 0 and isinstance(di["epoques"], int) and di["epoques"] >= 1
            and isinstance(di["lot"], int) and di["lot"] >= 1 and _nombre(di["norme_max"]) and di["norme_max"] > 0):
        raise GardeArret("distillation : pas > 0, époques ≥ 1, lot ≥ 1, norme_max > 0 attendus")
    for cle in ("doses_saboteur", "doses_temoin"):
        doses = config[cle]
        if not isinstance(doses, list) or not doses or any(not _nombre(x) or not 0.0 < x <= 1.0 for x in doses):
            raise GardeArret(f"{cle} : liste de doses dans ]0, 1] attendue")
        if sorted(doses) != doses or len(set(doses)) != len(doses):
            raise GardeArret(f"{cle} : doses croissantes, sans doublon, attendues")
        for x in doses:
            nom_condition("saboteur" if cle == "doses_saboteur" else "temoin", x)
    if 1.0 not in config["doses_saboteur"]:
        raise GardeArret("doses_saboteur : la dose 1 est exigée (jeu décisif du test croisé)")
    s = config["sonde"]
    if not (isinstance(s, dict) and s.get("famille") == "difference_moyennes" and s.get("agregation") == "max"
            and isinstance(s.get("couche"), int)):
        raise GardeArret("sonde décisive : différence de moyennes, agrégation par le maximum, couche entière (fixées d'avance)")
    if s["couche"] not in config["couches"]:
        raise GardeArret(f"sonde décisive à la couche {s['couche']} : hors des couches lues {config['couches']}")
    if config["go_id"] != GO_ID:
        raise GardeArret(f"GO {config['go_id']!r} : seul {GO_ID} est accepté pour T0.6")
    if not _nombre(config["plafond_usd"]) or config["plafond_usd"] != PLAFOND_USD:
        raise GardeArret(f"plafond {config['plafond_usd']!r} : exactement {PLAFOND_USD} USD (GO-2026-11-02-28)")
    if not 0.0 < float(config["fraction_activations_poussees"]) <= 1.0:
        raise GardeArret("fraction_activations_poussees dans ]0, 1] attendue")
    if not isinstance(config["exclusion_mention"], bool) or not isinstance(config["couples_descriptifs"], bool):
        raise GardeArret("exclusion_mention et couples_descriptifs : booléens attendus")
    au = config["audit"]
    if not isinstance(au, dict) or set(au) != set(CLES_AUDIT) or any(not _nombre(au[k]) for k in CLES_AUDIT):
        raise GardeArret(f"audit : clés {CLES_AUDIT}, nombres, attendues")


def etats_adaptateur(config: dict) -> list[dict]:
    """Phases d'évaluation, dans l'ordre : dose 0 (les quatre conditions de P3, adaptateurs injectés à dose 0), puis
    chaque dose du saboteur, puis chaque dose du témoin. `conditions` d'un état : celles que ses lots mêlent."""
    etats = [{"nom": "dose0", "adaptateur": None, "dose": 0.0, "conditions": list(CONDITIONS_DOSE_0)}]
    for ad, cle in (("saboteur", "doses_saboteur"), ("temoin", "doses_temoin")):
        for d in config[cle]:
            c = nom_condition(ad, d)
            etats.append({"nom": c, "adaptateur": ad, "dose": float(d), "conditions": [c]})
    return etats


def conditions_evaluation(config: dict) -> list[str]:
    return [c for e in etats_adaptateur(config) for c in e["conditions"]]


def condition_decisive_adaptateur(config: dict) -> str:
    """Condition de l'organisme (ii) à dose 1 (jeu décisif du test croisé, T6-1)."""
    return nom_condition("saboteur", 1.0)


def condition_temoin_dose_1(config: dict) -> str | None:
    return nom_condition("temoin", 1.0) if 1.0 in config["doses_temoin"] else None
