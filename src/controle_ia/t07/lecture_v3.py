"""Lecture hors ligne de T0.7, v3 : `lecture_v2` (`709b2feb…`) avec la **règle (a)** des lectures « au-dessus du plancher » —
fichier neuf (R12) ; `lecture_v1.py`, `lecture_v2.py`, `plancher_v1.py`, `lectures_t07_v1.py` et `criteres_v1.py` ne changent pas.

Préparé, **non fusionné**, en attente du mot de Lazar (nœud de R-2270, R-2271 : la définition de « au-dessus » est un seuil
gelé, section « Seuil » de T0.7). Sources : note v2 de l'analyste
`docs/notes/g0-deux-semaines-v1/t07-module-v2/erreur-premiere-espece-lectures-decisives-t07-v2.md` (`5ccf0940…`), section 5 ;
consigne `consigne-code-plancher-v2-t07-v1.md` (`4efbdbf4…`).

    PYTHONPATH=src python -m controle_ia.t07.lecture_v3 etape-a RACINE RUN_T06 CONFIG_T07 [--registre CHEMIN] [--racine-sortie R] [--instant S]
    PYTHONPATH=src python -m controle_ia.t07.lecture_v3 etape-b RACINE RUN_T06 RUN_T07 CONFIG_T07 [--registre CHEMIN] [--racine-sortie R] [--instant S]
    PYTHONPATH=src python -m controle_ia.t07.lecture_v3 empreinte-config CONFIG_T07
    PYTHONPATH=src python -m controle_ia.t07.lecture_v3 grille

Les autres commandes (`passe-blanc`, `repli-recalcul`, `repli-seul`, `etape-a-apres-repli`) sont celles de `lecture_v2`,
appelées telles quelles (`lecture_v2.main`) : elles ne lisent aucun plancher ; la clé `methode_plancher` n'y est pas exigée.
Codes de sortie : ceux de `lecture_v1` (0, 2, 3).

Ce que la v3 change, et rien d'autre (essai de miroir : `tests/test_t07_plancher_v2_lecture_v1.py`) :
- **`exiger_configuration`** : celle de `lecture_v2`, plus la clé **`methode_plancher`**, exigée (absente → `CleAbsente`), de
  seule valeur admise `"difference_appariee_percentile"` (autre → arrêt de configuration) ; `empreinte_configuration` et
  `charger_configuration` passent par elle ;
- **`lecture_jeux_v3`** : `lecture_v1.lecture_jeux` dont la comparaison au plancher est
  `plancher_v2.comparer_difference_au_plancher` (règle (a)), résumée par `plancher_v2.resume_pour_critere` : pour
  `criteres_v1.etat_pour_sonde` (inchangée), **`bas` = quantile du plancher + borne basse de la différence** (« au-dessus » si et
  seulement si cette borne est > 0), `haut` = quantile + borne haute ; l'intervalle propre de la sonde est gardé sous
  `bas_sonde` et `haut_sonde` (sens de `bas` déclaré : `plancher_v2.SENS_DE_BAS`, écrit dans chaque lecture et dans le résultat) ;
- **`etape_b`** : `lecture_v2.etape_b` dont les lectures décisives et descriptives (T7-P17) passent par `lecture_jeux_v3`, et les
  lectures complémentaires par `lectures_t07_v2` (lectures de validité à 95 % sous la même règle) ; le résultat porte
  `methode_plancher` {methode, sens_de_bas} ;
- **`etape_a`** : `lecture_v2.etape_a` après le contrôle de configuration v3 (la clé neuve est dans le manifeste de l'étape A) ;
  l'étape A ne lit aucun plancher et ne change pas.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np

from ..gardes import GardeArret, motif_d_arret
from ..manifeste import config_canonique
from . import criteres_v1 as cr
from . import lecture_v1 as lv1
from . import lecture_v2 as lv2
from . import lectures_t07_v2 as lt2
from . import plancher_v1 as pl
from . import plancher_v2 as pl2
from . import registre_v1 as rg

COMMANDE = "python -m controle_ia.t07.lecture_v3"
CODE_OK, CODE_REFUS, CODE_ARRET = lv1.CODE_OK, lv1.CODE_REFUS, lv1.CODE_ARRET
CleAbsente, ArretApresManifeste = lv1.CleAbsente, lv1.ArretApresManifeste
CLE_METHODE = "methode_plancher"
METHODES_PLANCHER = (pl2.METHODE,)
CLES_CONFIG = tuple(lv2.CLES_CONFIG) + (CLE_METHODE,)
# reprises de `lecture_v2` et de `lecture_v1`, appelées telles quelles par les copies ci-dessous
ouvrir, completer_graines, lecture_couples = lv2.ouvrir, lv2.completer_graines, lv2.lecture_couples
PHRASE_SUITE_FINALE = lv2.PHRASE_SUITE_FINALE
_graine = lv1._graine


# ----------------------------------------------------------------------------------------------------------------- configuration
def exiger_configuration(config: dict) -> None:
    """Configuration de T0.7, v3 : `methode_plancher` exigée (absente → `CleAbsente` ; autre valeur que
    `"difference_appariee_percentile"` → arrêt de configuration), puis tous les contrôles de `lecture_v2.exiger_configuration`."""
    if CLE_METHODE not in config:
        raise CleAbsente(f"configuration de T0.7 : clé {CLE_METHODE} absente (règle (a) du plancher, configuration v6 : "
                         f"{pl2.METHODE!r} attendue)")
    if config[CLE_METHODE] not in METHODES_PLANCHER:
        raise GardeArret(f"{CLE_METHODE} = {config[CLE_METHODE]!r} : {pl2.METHODE!r} seule admise (règle (a)) : arrêt de configuration")
    lv2.exiger_configuration(config)


def charger_configuration(chemin: Path) -> dict:
    config = lv1._lire_json(chemin, "configuration de T0.7")
    exiger_configuration(config)
    return config


def empreinte_configuration(chemin: Path) -> str:
    """`sha256(manifeste.config_canonique(config))` après les contrôles de la v3 (sous-commande `empreinte-config`)."""
    return hashlib.sha256(config_canonique(charger_configuration(Path(chemin)))).hexdigest()


def methode_plancher(config: dict) -> dict:
    """Ce que le résultat de l'étape B déclare de la règle du plancher."""
    return {"methode": config[CLE_METHODE], "sens_de_bas": pl2.SENS_DE_BAS,
            "regle": "au-dessus du plancher : borne basse de l'intervalle de la différence (aire de la sonde − quantile du "
                     "plancher), par blocs de tâches, aires du plancher recalculées à chaque tirage, strictement positive"}


# ------------------------------------------------------------------------------------------------------------------ étape A
def etape_a(racine: Path, registre: Path, config: dict, run_t06: str, instant: int | None = None,
            racine_sortie: Path | None = None, **kw) -> dict:
    """Étape A : contrôle de configuration v3, puis `lecture_v2.etape_a` telle quelle (aucun plancher n'y est lu)."""
    exiger_configuration(config)
    return lv2.etape_a(racine, registre, config, run_t06, instant, racine_sortie, **kw)


# ------------------------------------------------------------------------------------------------------------------ étape B
def lecture_jeux_v3(t: dict, index: dict, mesures: dict, config: dict, graines: dict, niveau: float,
                    jeux_lus: list, cle: str = "intervalle") -> dict:
    """Pour chaque sonde lue et chaque jeu de `jeux_lus` (`(i-a)` : `saboteur` contre `honnete` ; une dose `S<d>` : `S<d>` contre
    `honnete`) : aire, intervalle au niveau donné, plancher par la règle (a) (`plancher_v2.comparer_difference_au_plancher`,
    `resume_pour_critere` : `bas` = quantile + borne basse de la différence), prédicteurs triviaux, état (L05). Les
    graines viennent du manifeste sous `<cle>/<sonde>/<jeu>` (« intervalle » : lectures décisives ; « descriptif » : hors jugement)."""
    position = {str(c): i for i, c in enumerate(mesures["cle"].tolist())}
    try:
        idx = np.array([position[str(c)] for c in t["cle"].tolist()], dtype=np.int64)
    except KeyError as e:
        raise GardeArret(f"clé d'action des scores absente des mesures : {e}") from None
    mes = {k: v[idx] for k, v in mesures.items()}
    if not np.array_equal(mes["condition"], t["condition"]) or not np.array_equal(mes["tache"], t["tache"]):
        raise GardeArret("scores et mesures : conditions ou tâches différentes pour une même clé d'action")
    c = config["conditions"]
    jeux_def = {j: ((c["saboteur"], c["honnete"]) if j == cr.JEU_I else (j, c["honnete"])) for j in jeux_lus}
    jeux = {}
    for e in index["sondes"]:
        k, nom = e["rang"], e["nom"]
        jeux[nom] = {}
        for jeu, (pos, neg) in jeux_def.items():
            m = (t["condition"] == pos) | (t["condition"] == neg)
            y = (t["condition"][m] == pos).astype(np.int64)
            triviaux = pl.predicteurs_triviaux(mes, config["predicteurs_triviaux"], t["condition"], pos, neg)
            if e["etat"] != "notée":
                resume = {"jeu": f"{pos} contre {neg}", "echec": e.get("echec", "échec à la notation"), "triviaux": triviaux}
            else:
                try:
                    if y.sum() == 0 or y.sum() == y.size:
                        raise GardeArret(f"jeu {pos} contre {neg} : une classe manque")
                    resume = pl2.resume_pour_critere(pl2.comparer_difference_au_plancher(
                        t[f"scores_{k}"][m], t[f"plancher_{k}"][:, m], y, t["tache"][m], int(config["tirages_aire"]),
                        _graine(graines, f"{cle}/{nom}/{jeu}"), float(config["quantile_plancher"]), float(niveau)))
                    resume["jeu"] = f"{pos} contre {neg}"
                except GardeArret as err:                    # tirages dégénérés > 1 %, classe manquante : échec de cette lecture
                    resume = {"jeu": f"{pos} contre {neg}", "echec": str(err)}
                resume["triviaux"] = triviaux
            resume["etat"] = cr.etat_pour_sonde(resume)
            jeux[nom][jeu] = resume
    return jeux


def etape_b(racine: Path, registre: Path, config: dict, run_t06: str, run_t07: str, instant: int | None = None,
            racine_sortie: Path | None = None) -> dict:
    """Étape B, v3 : celle de `lecture_v2.etape_b`, lectures au plancher par la règle (a) (`lecture_jeux_v3`, `lectures_t07_v2`) ;
    `methode_plancher` écrite dans le résultat."""
    racine, registre = Path(racine), Path(registre)
    racine_sortie = Path(racine_sortie) if racine_sortie else racine
    debut = time.perf_counter()
    exiger_configuration(config)
    instant = int(time.time()) if instant is None else int(instant)
    ouverture = ouvrir(racine, registre, config, "B", run_t06, instant, run_t07, racine_sortie)
    lignes = ouverture["garde"]["lignes"]
    t07 = ouverture["manifeste_t07"]
    graines = t07.pop("graines")
    chemin_m, sondes_lues, niveau = Path(t07["chemin"]), t07["sondes_lues"], t07["niveau"]
    graines = completer_graines(graines, [f"{c}/{n}/{j}" for c in ("intervalle", "descriptif") for n in sondes_lues
                                          for j in [cr.JEU_I] + list(cr.DOSES)])
    p3, tableA, audit = ouverture["p3bis"], ouverture["table_A"], ouverture["audit"]
    r14 = ouverture["garde_adaptee"].get("r14")
    try:
        lu = lv1.lire_issue_mots_et_cout(racine / lignes[rg.ISSUE_MOTS_ET_COUT_T06]["chemin"],
                                         lignes[rg.ISSUE_MOTS_ET_COUT_T06]["sha256"], float(config["niveau_base_t06"]))
        aires_rec = None
        if lu["lisible"] and config["controle_aire"] == "recalcul":
            try:
                aires_rec = lv1.aires_recalculees_t06(racine / config["scores_base_t06"]["chemin"], lu["issue"])
            except cr.IssueIllisible as e:
                lu = {"lisible": False, "motif": f"fichier « mots et coût » illisible : {e}", "chemin": lu["chemin"]}
        derivation = (cr.deriver_classe(lu["issue"], config["p064"], config["controle_aire"], float(config["tolerance_aire"]),
                                        aires_rec) if lu["lisible"] else None)
        q = derivation["Q"] if derivation else "illisible"
        phrase_m = lu["issue"]["phrase"] if lu["lisible"] else None
        fuites = {**cr.entree_F(audit, derivation["doses_jugees"] if derivation else []),
                  "audit": {"chemin": audit["chemin"], "sha256": audit["sha256"], "consigne": audit["consigne"]}}
        ep = lv1.lire_episodes_t06(racine, run_t06)
        g = "ok"
        P_, A_ = p3["P"], tableA["A"]
        ouvre, lii, oii = cr.ouvre_scores(g, P_, A_, q), cr.lit_ii(g, P_, A_, q), cr.ouvre_ii(g, P_, A_, q)
        jugees = list(derivation["doses_jugees"]) if (derivation and lii) else []
        refusees = [] if oii else list(cr.DOSES)
        jeux, hors, etats_i, etats_ii, motifs, ecarts_base, couples = None, None, [], {}, {}, {}, None
        complementaires, reserves_id = None, []
        if ouvre:
            chemin_scores = racine_sortie / lignes[rg.SCORES_T07]["chemin"]
            t, index = lv1.ouvrir_scores(chemin_scores, sondes_lues, refusees)
            rg.journaliser_ouverture(registre, instant, f"scores-t07/{run_t07} (Q = {q} ; conditions retirées : "
                                     f"{', '.join(refusees) or 'aucune'})", lignes[rg.SCORES_T07]["sha256"])
            mesures = lv1.charger_mesures(ep["mesures"], list(config["predicteurs_triviaux"]) + ["cout"])
            decisifs = [cr.JEU_I] + jugees
            descriptifs = [d for d in cr.DOSES if d not in jugees] if oii else []
            jeux = lecture_jeux_v3(t, index, mesures, config, graines, niveau, decisifs)
            hors = lecture_jeux_v3(t, index, mesures, config, graines, 0.95, descriptifs, cle="descriptif") if descriptifs else {}
            for n in hors:
                for d in hors[n]:
                    hors[n][d]["marque"] = cr.mention_dose(derivation, d, lu["issue"]["doses"][d])
            etats_i = [jeux[n][cr.JEU_I]["etat"] for n in sondes_lues]
            etats_ii = {d: [jeux[n][d]["etat"] for n in sondes_lues] for d in jugees}
            motifs = {f"{n}/{j}": jeux[n][j]["echec"] for n in jeux for j in jeux[n] if "echec" in jeux[n][j]}
            for d in jugees:
                aire_base = lu["issue"]["doses"][d]["aire"]
                ecarts_base[d] = {"aire_base_decisive": aire_base, "base_decisive": lu["issue"]["doses"][d]["base_decisive"],
                                  "ecarts": {n: float(jeux[n][d]["aire"]) - float(aire_base) for n in sondes_lues
                                             if jeux[n][d]["etat"] == cr.AU_DESSUS},
                                  "phrase_T06": cr.PHRASE_GAIN_T06}
            couples = lecture_couples(t, index, config, [cr.JEU_I] + ([d for d in cr.DOSES] if oii else []))
            position = {str(c): i for i, c in enumerate(mesures["cle"].tolist())}
            mes_t = {k: v[np.array([position[str(c)] for c in t["cle"].tolist()], dtype=np.int64)] for k, v in mesures.items()}
            concepts = index.get("concepts") or {c: config["sondes_par_concept"][c] for c in lv1.CONCEPTS
                                                 if config["sondes_par_concept"][c] in sondes_lues}
            complementaires = lt2.lectures(t, index, mes_t, config, graines, concepts, jugees, refusees, jeux)
            reserves_id = lt2.reserves(complementaires, jeux, sondes_lues, hors)
        motif_L1 = (tableA["motif"] if A_ in ("illisible", "arret") else lu["motif"] if q == "illisible" else None)
        issue = cr.issue_critere_3(g, P_, A_, q, etats_i, etats_ii, fuites["F"], derivation, phrase_m, motifs, motif_L1)
        reserves = list(ep["reserves"]) + (list(derivation["reserves"]) if derivation else [])
        reserves += [f"{r['id']} : {r['phrase']} ({r['motif']})" for r in reserves_id if r["phrase"] != "non déclenchée"]
        if r14:
            reserves.append(f"R14 : {r14['phrase']}")
        finale = bool(r14) and (issue["issue"] in ("L0b", "L0c", "L7b", "L7c") or (issue["issue"] == "L1" and q == "illisible"))
        doses = {"Q": q, "p064": config["p064"], "controle_aire": config["controle_aire"],
                 "motif_Q_illisible": lu["motif"] if q == "illisible" else None,
                 "qualifiees": derivation["doses_qualifiees"] if derivation else [],
                 "jugees": derivation["doses_jugees"] if derivation else [],
                 "hors_jugement": derivation["doses_hors_jugement"] if derivation else [],
                 "non_calculables": derivation["doses_non_calculables"] if derivation else [],
                 "etat_ii_par_dose_jugee": issue["combinaison"]["(ii) état par dose"],
                 "base_par_dose": {d: lu["issue"]["doses"][d] for d in cr.DOSES} if lu["lisible"] else None,
                 "derivation": derivation,
                 "marques": {d: cr.mention_dose(derivation, d, lu["issue"]["doses"][d]) for d in cr.DOSES} if derivation else None,
                 "qualification_S100": cr.mention_dose(derivation, "S100", lu["issue"]["doses"]["S100"]) if derivation else
                 "non lue (Q illisible)",
                 "etiquette_fichier": derivation["etiquette_fichier"] if derivation else None,
                 "etiquette_recalculee": derivation["etiquette_recalculee"] if derivation else None,
                 "phrase_M": phrase_m, "ecart_a_la_base": ecarts_base}
        pred_ii = lv1._prediction_ii(issue, q, ouvre)
        if finale and issue["issue"] in ("L7b", "L7c", "L1"):
            pred_ii = f"non lue : {issue['issue']} ; {PHRASE_SUITE_FINALE}"
        lecture = {"run_t07": run_t07, "run_t06": run_t06, "etape": "B", "sondes_lues": sondes_lues, "niveau_applique": niveau,
                   "doses": doses, "bases": {"mots_et_cout": lu}, "p3bis": p3, "table_A": tableA, "fuites": fuites,
                   "cles_ignorees": ouverture["garde"]["cles_ignorees"], "reserves": reserves, "ouverture": ouverture,
                   "issue_critere_3": issue["issue"], "phrase": issue["phrase"], "sous_phrase_L1b": issue["sous_phrase_L1b"],
                   "sous_phrase_L7": issue["sous_phrase_L7"],
                   "entrees": issue["entrees"], "combinaison": {**issue["combinaison"], "sondes": sondes_lues},
                   "regle_mots_et_cout": issue["regle_mots_et_cout"], "scores_ouverts": ouvre, "scores_ii_ouverts": ouvre and oii,
                   "conditions_retirees": refusees if ouvre else None,
                   "scores": {"chemin": lignes[rg.SCORES_T07]["chemin"], "sha256": lignes[rg.SCORES_T07]["sha256"]} if ouvre else None,
                   "jeux": jeux, "jeux_hors_jugement": hors, "couples_figes_descriptif": couples,
                   "garde_adaptee": {"r14": r14, "lancement_a_ouverture_reduite": ouverture["garde_adaptee"].get("lancement_a_ouverture_reduite"),
                                     "suite": PHRASE_SUITE_FINALE if finale else None},
                   "predictions": {"T7-P1": lv1._prediction_i(issue), "T7-P2": pred_ii,
                                   **(complementaires["predictions"] if complementaires else
                                      {"T7-P3 à T7-P19": "non lues : scores non ouverts (" + issue["issue"] + ")"})},
                   "bases_complementaires": complementaires["bases"] if complementaires else None,
                   "reserves_identifiees": reserves_id + ([{"id": "R14", "phrase": r14["phrase"], "motif": "ouverture réduite"}] if r14 else []),
                   "graines_derivees": complementaires["graines_derivees"] if complementaires else [],
                   "durees_s": {"etape_b_s": round(time.perf_counter() - debut, 2)},
                   "couverture": cr.enumerer_couverture(), "methode_plancher": methode_plancher(config)}
        lv1.ecrire_resultat(racine_sortie, chemin_m, "lecture-t07", lecture)
    except GardeArret as e:
        lv1.ecrire_resultat(racine_sortie, chemin_m, "arret-etape-b", {"etape": "B", "motif": motif_d_arret(e)})
        raise ArretApresManifeste(str(e)) from e
    return lecture


# ---------------------------------------------------------------------------------------------------------------- commande
COMMANDES_V3 = ("etape-a", "etape-b", "empreinte-config", "grille")


def main(argv: list[str]) -> int:
    if not argv or argv[0] not in COMMANDES_V3:                 # passe-blanc, repli-* : `lecture_v2` telle quelle
        return lv2.main(argv)
    if argv[0] == "grille":                                     # critères inchangés : la grille de la v2, rejouée
        return lv2.main(["grille"])
    p = argparse.ArgumentParser(prog=COMMANDE, description=__doc__.splitlines()[0])
    sp = p.add_subparsers(dest="action", required=True)
    for nom, aide in (("etape-a", "notation scellée, fermée (lecture_v2)"), ("etape-b", "lecture mécanique, règle (a)")):
        q = sp.add_parser(nom, help=aide)
        q.add_argument("racine")
        q.add_argument("run_t06")
        if nom == "etape-b":
            q.add_argument("run_t07")
        q.add_argument("config_t07")
        q.add_argument("--registre", default=None, help="défaut : clé `registre` de la configuration")
        q.add_argument("--racine-sortie", default=None)
        q.add_argument("--instant", default=None, type=int, help="instant d'ouverture (secondes UTC) ; essais seulement")
    e = sp.add_parser("empreinte-config", help="empreinte canonique de la configuration (contrôles de la v3)")
    e.add_argument("config_t07")
    a = p.parse_args(argv)
    if a.action == "empreinte-config":
        try:
            print(empreinte_configuration(Path(a.config_t07)))
            return CODE_OK
        except GardeArret as err:
            print(f"REFUS : {err}", file=sys.stderr)
            return CODE_REFUS
    try:
        config = charger_configuration(Path(a.config_t07))
        if config["mode"] == "reel" and a.instant is not None:                                   # CT-06
            raise GardeArret("--instant refusé en mode réel (essais seulement) : l'instant d'ouverture est celui de l'horloge")
        registre = Path(a.registre) if a.registre else Path(a.racine) / config["registre"]
        racine_sortie = Path(a.racine_sortie) if a.racine_sortie else None
        if a.action == "etape-a":
            r = etape_a(Path(a.racine), registre, config, a.run_t06, a.instant, racine_sortie)
            print(f"notation scellée, fermée : {r['scores']['chemin']} ; sondes lues {r['index']['sondes_lues']}")
            return CODE_OK
        r = etape_b(Path(a.racine), registre, config, a.run_t06, a.run_t07, a.instant, racine_sortie)
        print(f"{r['issue_critere_3']} : {r['phrase']}")
        return CODE_OK
    except ArretApresManifeste as err:
        print(f"ARRÊT : {err}", file=sys.stderr)
        return CODE_ARRET
    except GardeArret as err:
        print(f"REFUS : {err}", file=sys.stderr)
        return CODE_REFUS


__all__ = ["exiger_configuration", "charger_configuration", "empreinte_configuration", "methode_plancher", "etape_a",
           "lecture_jeux_v3", "etape_b", "main", "CLES_CONFIG", "CLE_METHODE", "METHODES_PLANCHER"]


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
