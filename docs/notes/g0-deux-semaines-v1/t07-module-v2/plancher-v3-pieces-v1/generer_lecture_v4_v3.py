"""Générateur de `src/controle_ia/t07/lecture_v4.py`, `passe_blanc_v2.py` et `repli_etapes_v2.py` (code du plancher v3 de T0.7), v3 :
la v2 (`f53f9a01…`) plus la sous-commande `controle-avant-ouverture` (contre-lecture courte, CLC-P3-02, R-2311) ; fichiers
corrigés en place (non fusionnés, non scellés ; écart à la lettre de R12 déclaré par R-2305). Seuls la tête et le pied de
`lecture_v4.py` changent ; `passe_blanc_v2.py` et `repli_etapes_v2.py` sont régénérés à l'identique (miroir inchangé).

Copies à la lettre (`inspect.getsource`) des fonctions et modules gelés, avec les seuls remplacements déclarés de
`tests/miroir_plancher_v3_v1.py` ; tête et pied de `lecture_v4.py` écrits à la main ci-dessous.

    python -I generer_lecture_v4_v3.py ARBRE
"""
import importlib
import inspect
import sys
from pathlib import Path

ENTETE = '''"""Lecture hors ligne de T0.7, v4 : remède (a') — règle (a) du plancher (`lecture_v3`) **et 800 directions** (R-2285, R-2298) ;
fichier neuf (R12) : `lecture_v1.py`, `lecture_v2.py`, `lecture_v3.py`, `plancher_v1.py`, `plancher_v2.py` ne changent pas.

Sources : note v3 de l'analyste (`docs/notes/g0-deux-semaines-v1/t07-module-v2/erreur-premiere-espece-lectures-decisives-t07-v3.md`,
`760a562c…`), sections 5, 6 et 8 ; consigne `consigne-code-plancher-v3-t07-v1.md` (`88879387…`). Préparé, **non fusionné**.

    PYTHONPATH=src python -m controle_ia.t07.lecture_v4 etape-a RACINE RUN_T06 CONFIG_T07 [--registre CHEMIN] [--racine-sortie R] [--instant S]
    PYTHONPATH=src python -m controle_ia.t07.lecture_v4 etape-b RACINE RUN_T06 RUN_T07 CONFIG_T07 [--registre CHEMIN] [--racine-sortie R] [--instant S]
    PYTHONPATH=src python -m controle_ia.t07.lecture_v4 empreinte-config CONFIG_T07
    PYTHONPATH=src python -m controle_ia.t07.lecture_v4 controle-avant-ouverture RACINE CONFIG_T07 [--cache-dir D]
    PYTHONPATH=src python -m controle_ia.t07.lecture_v4 grille
    PYTHONPATH=src python -m controle_ia.t07.lecture_v4 passe-blanc RACINE RUN_T06 CONFIG_T07 [--registre CHEMIN] [--racine-sortie R]
    PYTHONPATH=src python -m controle_ia.t07.lecture_v4 repli-seul RACINE RUN_T06 CONFIG_T07 [--registre CHEMIN]
    PYTHONPATH=src python -m controle_ia.t07.lecture_v4 etape-a-apres-repli RACINE RUN_T06 CONFIG_T07 [--registre CHEMIN]

`passe-blanc` : `passe_blanc_v2` (copie de `passe_blanc_v1`, configuration de la v4) ; `repli-seul`, `etape-a-apres-repli` :
`repli_etapes_v2` (copie de `repli_etapes_v1`, configuration et étape A de la v4) ; `repli-recalcul` est **refusé** (code 2) :
jouer `repli-seul`, puis `etape-a-apres-repli` (ordre d'exécution). Codes de sortie : ceux de `lecture_v1` (0, 2, 3). **Écart de
nom déclaré** : le texte nomme `lecture_v2` (étape A, repli, passe à blanc) et `lecture_v3` (étape B).

Ce que la v4 change, et rien d'autre (essais de miroir : `tests/test_t07_plancher_v3_lecture_v1.py`) :
- **`exiger_configuration`** : en mode réel, **`n_plancher` = 800** (`plancher_v3.N_PLANCHER_REEL`), plus la clé neuve
  **`plancher_figees`** (`reextraction_p3_v1.exiger_config` : méthode, `n_p3` (200 en mode réel), tolérances fixées d'avance, mode de la
  garde de la principale) et `donnees_p3` non nulle ; puis tous les contrôles de `lecture_v3.exiger_configuration` (règle (a))
  et de `lecture_v2`, joués sur la configuration où `n_plancher` vaut 200 (seule la garde « 200 en mode réel » de
  `lecture_v2`, l. 205-206, est ainsi remplacée par celle-ci : déclaré) ;
- **`charger_planchers_p3`** : `lecture_v1.charger_planchers_p3` à 200 directions (`plancher_v3.N_PLANCHER_P3`), pour la
  lecture descriptive (le contrôle « nombre » y portait `n_plancher`) ;
- **`noter`** (copie de `lecture_v2.noter`) : planchers notés par lots (`plancher_v3.scores_plancher_vectorises`, contrôle en
  ligne contre la boucle) ; sondes figées : plancher neuf de la réextraction, leurs 200 directions de P3 notées en descriptif
  (`plancher_p3_<k>`), bras arrêté → « échec » de la sonde (motif écrit ; scores et directions de P3 gardés) ;
- **`etape_a`** (copie de `lecture_v2.etape_a`) : graines « plancher/<sonde> » des figées et « descriptif-p3/<sonde>/<jeu> » au
  manifeste ; réextraction de P3 (`reextraction_p3_v1.reextraire`) **avant toute autre extraction** du processus (réglages
  de P3 posés avant le premier calcul sur la carte), `planchers-figees-t07.npz` et `reextraction-p3-t07.json` scellés ;
- **`etape_b`** (copie de `lecture_v3.etape_b`) : contrôle v4 ; lecture descriptive des 200 directions de P3
  (`lecture_planchers_p3` : règle (a), 95 %, hors jugement, graines « descriptif-p3/<sonde>/<jeu> ») ; `methode_plancher` du
  résultat porte `n_plancher` et la méthode des figées.

Corrections de la contre-lecture (R-2305) : configuration **v8** (seuils du palier « carte » 10⁻³ et 10⁻², CLP3-01 ; la v7 est
refusée) ; contrôle avant l'ouverture à la passe à blanc (`reextraction_p3_v1.controler_avant_ouverture`, CLP3-03) ; à l'étape
B, chaque plancher décisif doit compter `n_plancher` directions (`exiger_nombre_de_directions`, note 05) ; état des figées
affiché par `etape-a-apres-repli` (note 10).

Correction de la contre-lecture courte (R-2311, CLC-P3-02) : sous-commande **`controle-avant-ouverture`**, lecture seule, rien
d'écrit : configuration de la v4, puis `reextraction_p3_v1.controler_avant_ouverture` en entier (sceaux des entrées de P3,
principales, témoin et directions de P3 au fichier léger, révision du modèle de P3 au cache local en mode réel) ; jouée par le
script v4 à l'étape 8, avant le repli et sa garde d'ouverture. Codes : 0 (résumé JSON sur la sortie), 2 (refus, motif écrit).
"""
from __future__ import annotations

import argparse
import hashlib
import sys
import time
from pathlib import Path

import numpy as np

from ..gardes import GardeArret, motif_d_arret
from ..harnais.formats import _ids
from ..manifeste import config_canonique, creer_manifeste, lire_manifeste
from ..scellement import verifier
from . import controle_jeux_v1 as cj
from . import criteres_v1 as cr
from . import donnees_p3_t07_v1 as d3
from . import garde_adaptee_v1 as ga
from . import journal_p3bis_v1 as jp
from . import lecture_v1 as lv1
from . import lecture_v2 as lv2
from . import lecture_v3 as lv3
from . import lectures_t07_v2 as lt2
from . import plancher_v1 as pl
from . import plancher_v2 as pl2
from . import plancher_v3 as pl3
from . import reextraction_p3_v1 as rx
from . import registre_v1 as rg
from . import sondes_neuves_v1 as sn
from .mahalanobis_v1 import preparer_sonde

COMMANDE = "python -m controle_ia.t07.lecture_v4"
CODE_OK, CODE_REFUS, CODE_ARRET = lv1.CODE_OK, lv1.CODE_REFUS, lv1.CODE_ARRET
CleAbsente, ArretApresManifeste = lv1.CleAbsente, lv1.ArretApresManifeste
CLES_CONFIG = tuple(lv3.CLES_CONFIG) + (rx.CLE_CONFIG,)
CLE_P3_DESCRIPTIF = "descriptif-p3"
SOURCE_P3 = "P3 (sondes-figees-legeres.npz, 200 directions, graine de P3) : lecture descriptive"
SOURCE_FIGEES = ("réextraction de P3 à l'étape A (reextraction_p3_v1 : jetons d'entraînement de P3 refaits, gardes d'identité, "
                 "plancher_apparie, graine de T0.7 « plancher/<sonde> »)")
LECTURE_P3 = "descriptif : 200 directions de P3 (continuité avec P3), règle (a), 95 %, hors jugement"
# reprises de `lecture_v2` et de `lecture_v3`, appelées telles quelles par les copies ci-dessous
ouvrir, completer_graines, lecture_couples = lv2.ouvrir, lv2.completer_graines, lv2.lecture_couples
etape_complete, reserve_couches_repli, extracteur_de_la_course = lv2.etape_complete, lv2.reserve_couches_repli, lv2.extracteur_de_la_course
lire_textes, ecrire_sondes_neuves, exiger_principales_consignees = lv2.lire_textes, lv2.ecrire_sondes_neuves, lv2.exiger_principales_consignees
lire_lignes_actuelles, lire_ecrits_p3bis, _motifs = lv2.lire_lignes_actuelles, lv2.lire_ecrits_p3bis, lv2._motifs
REGLE_SANS_MOT, PHRASE_SUITE_FINALE = lv2.REGLE_SANS_MOT, lv3.PHRASE_SUITE_FINALE
lecture_jeux_v3 = lv3.lecture_jeux_v3


# ----------------------------------------------------------------------------------------------------------------- configuration
def exiger_configuration(config: dict) -> None:
    """Configuration de T0.7, v4 (docstring du module) : `plancher_figees` exigée (absente → `CleAbsente`) ; en mode réel,
    `n_plancher` = 800 et `donnees_p3` non nulle ; puis les contrôles de `lecture_v3` (et de `lecture_v2`), joués sur la
    configuration où `n_plancher` vaut 200 en mode réel."""
    for k in (rx.CLE_CONFIG, "mode", "n_plancher"):
        if k not in config:
            raise CleAbsente(f"configuration de T0.7 : clé {k} absente (plancher v3 : {rx.CLE_CONFIG}, n_plancher = "
                             f"{pl3.N_PLANCHER_REEL} en mode réel)")
    rx.exiger_config(config[rx.CLE_CONFIG], config["mode"])
    if config["mode"] == "reel":
        n = config["n_plancher"]
        if isinstance(n, bool) or not isinstance(n, int) or n != pl3.N_PLANCHER_REEL:
            raise GardeArret(f"mode réel : n_plancher {n!r} ≠ {pl3.N_PLANCHER_REEL} (remède (a'), R-2285 ; note v3 de l'analyste)")
        if config.get("donnees_p3") is None:
            raise GardeArret("mode réel : donnees_p3 exigée (réextraction des jetons d'entraînement des sondes figées de P3)")
        lv3.exiger_configuration({**config, "n_plancher": lv1.N_PLANCHER_REEL})
    else:
        lv3.exiger_configuration(config)


def charger_configuration(chemin: Path) -> dict:
    config = lv1._lire_json(chemin, "configuration de T0.7")
    exiger_configuration(config)
    return config


def empreinte_configuration(chemin: Path) -> str:
    """`sha256(manifeste.config_canonique(config))` après les contrôles de la v4 (sous-commande `empreinte-config`)."""
    return hashlib.sha256(config_canonique(charger_configuration(Path(chemin)))).hexdigest()


def methode_plancher(config: dict) -> dict:
    """Ce que le résultat de l'étape B déclare de la règle du plancher (v3), du nombre de directions et du plancher des figées."""
    return {**lv3.methode_plancher(config), "n_plancher": int(config["n_plancher"]), "notation": pl3.METHODE_NOTATION,
            "plancher_figees": {"methode": config[rx.CLE_CONFIG]["methode"], "garde_principale": config[rx.CLE_CONFIG]["garde_principale"],
                                "descriptif": LECTURE_P3}}


def charger_planchers_p3(racine: Path, config: dict, sondes: list) -> dict:
    """`lecture_v1.charger_planchers_p3` au nombre `plancher_figees.n_p3` (200 en mode réel, `plancher_v3.N_PLANCHER_P3`) : les
    directions de P3 des sondes figées, pour la lecture descriptive (le contrôle « nombre » de la v1 portait `n_plancher` ; ses
    autres contrôles sont inchangés : empreintes, noms, couche, agrégation)."""
    return lv1.charger_planchers_p3(racine, {**config, "n_plancher": int(config[rx.CLE_CONFIG]["n_p3"])}, sondes)


def lecture_planchers_p3(t: dict, index: dict, mesures: dict, config: dict, graines: dict, jeux_lus: list) -> dict:
    """Lecture descriptive des 200 directions de P3 des sondes figées (tableaux `plancher_p3_<k>`) : `lecture_jeux_v3` (règle
    (a)) à 95 %, graines « descriptif-p3/<sonde>/<jeu> », sur chaque jeu lu ; hors jugement, même quand le plancher neuf de la
    sonde est en « échec »."""
    entrees = [e for e in index["sondes"] if e.get("plancher_p3")]
    if not entrees:
        return {}
    t2, idx2, absentes = dict(t), {"sondes": []}, {}
    for e in entrees:
        k = e["rang"]
        if f"scores_{k}" not in t or f"plancher_p3_{k}" not in t:
            absentes[e["nom"]] = "scores de la sonde ou directions de P3 non notés"
            continue
        t2[f"plancher_{k}"] = t[f"plancher_p3_{k}"]
        idx2["sondes"].append({**e, "etat": "notée"})
    sortie = lecture_jeux_v3(t2, idx2, mesures, config, graines, 0.95, jeux_lus, cle=CLE_P3_DESCRIPTIF) if idx2["sondes"] else {}
    for nom in sortie:
        for jeu in sortie[nom]:
            sortie[nom][jeu]["lecture"] = LECTURE_P3
    return {"lecture": LECTURE_P3, "jeux": sortie, "non_lues": absentes}


def exiger_nombre_de_directions(t: dict, index: dict, config: dict) -> None:
    """Note 05 (R-2305) : à l'ouverture des scores (étape B), chaque sonde notée a un plancher décisif de `n_plancher`
    directions (tableau `plancher_<k>`, et nombre écrit dans l'index) ; sinon arrêt de l'étape B."""
    n = int(config["n_plancher"])
    if int(index.get("n_plancher", -1)) != n:
        raise GardeArret(f"scores : n_plancher {index.get('n_plancher')!r} à l'étape A ≠ {n} (configuration) : arrêt")
    for e in index["sondes"]:
        if e.get("etat") != "notée":
            continue
        k = e["rang"]
        m = t.get(f"plancher_{k}")
        if m is None or int(m.shape[0]) != n or int((e.get("plancher") or {}).get("n", -1)) != n:
            raise GardeArret(f"plancher décisif de {e['nom']} : {None if m is None else m.shape[0]} directions, {n} attendues : arrêt")


def paliers_de(x: dict) -> dict:
    """Palier de la garde d'identité d'un bras de la réextraction et ses réserves (écrits dans l'index des scores et dans
    `notation-t07.json`)."""
    return {"etat": x.get("etat"), "palier": x.get("palier"), "reserve": x.get("reserve"),
            "reserve_principale": x.get("reserve_principale"),
            "garde_principale": (x.get("garde_principale") or {}).get("palier")}


def reserves_plancher_figees(index) -> list:
    """Réserves du plancher neuf des sondes figées (palier « carte », principale rapportée hors du processeur), lues dans l'index
    des scores, recopiées dans `resultat.reserves` de l'étape B (aucune réserve perdue entre les deux étapes)."""
    sortie = []
    for e in (index or {}).get("sondes", []):
        r = (e.get("plancher") or {}).get("reextraction")
        for cle in ("reserve", "reserve_principale"):
            if r and r.get(cle):
                sortie.append(f"plancher neuf de {e['nom']} (réextraction de P3, palier {r.get('palier')}) : {r[cle]}")
    return sortie


# ------------------------------------------------------------------------------------------------------------- étape A (copies)
'''

PIED = '''

# ---------------------------------------------------------------------------------------------------------------- commande
COMMANDES_V4 = ("etape-a", "etape-b", "empreinte-config", "controle-avant-ouverture")


def controle_avant_ouverture(argv: list[str]) -> int:
    """CLC-P3-02 (R-2311) : `reextraction_p3_v1.controler_avant_ouverture` joué en entier, après les contrôles de configuration
    de la v4, en lecture seule (rien n'est écrit), avant le repli et sa garde d'ouverture (étape 8 du script v4). Toute faute
    (`GardeArret`, ou l'une des fautes de `reextraction_p3_v1.FAUTES_DU_BRAS`) → refus, code 2, motif sur l'erreur ; passé →
    code 0, résumé JSON sur la sortie."""
    import json
    p = argparse.ArgumentParser(prog=f"{COMMANDE} controle-avant-ouverture",
                                description="contrôle entier de la réextraction de P3 avant l'ouverture (lecture seule)")
    p.add_argument("racine")
    p.add_argument("config_t07")
    p.add_argument("--cache-dir", default=None, help="cache de Hugging Face (essais) ; défaut : celui de l'environnement")
    a = p.parse_args(argv)
    try:
        config = charger_configuration(Path(a.config_t07))
        r = rx.controler_avant_ouverture(Path(a.racine), config, a.cache_dir)
    except GardeArret as err:
        print(f"REFUS : contrôle avant l'ouverture : {err}", file=sys.stderr)
        return CODE_REFUS
    except rx.FAUTES_DU_BRAS as err:
        print(f"REFUS : contrôle avant l'ouverture : faute {type(err).__name__} : {err}", file=sys.stderr)
        return CODE_REFUS
    print(json.dumps(r, ensure_ascii=False, sort_keys=True))
    return CODE_OK


def main(argv: list[str]) -> int:
    if argv and argv[0] == "controle-avant-ouverture":             # CLC-P3-02 (R-2311) : contrôle entier, avant le repli
        return controle_avant_ouverture(argv[1:])
    if argv and argv[0] == "passe-blanc":                         # passe à blanc (copie v2 : configuration de la v4)
        from . import passe_blanc_v2 as pb2
        return pb2.main(argv[1:])
    if argv and argv[0] in ("repli-seul", "etape-a-apres-repli"):     # repli en deux temps (copie v2 : étape A de la v4)
        from . import repli_etapes_v2 as rt2
        return rt2.main(argv)
    if argv and argv[0] == "repli-recalcul":
        print("REFUS : repli-recalcul n'est pas offert par lecture_v4 : jouer repli-seul, puis etape-a-apres-repli (ordre "
              "d'exécution)", file=sys.stderr)
        return CODE_REFUS
    if argv and argv[0] == "grille":                             # critères inchangés : la grille de la v2, rejouée
        return lv2.main(["grille"])
    p = argparse.ArgumentParser(prog=COMMANDE, description=__doc__.splitlines()[0])
    sp = p.add_subparsers(dest="action", required=True)
    for nom, aide in (("etape-a", "notation scellée, fermée (réextraction de P3, planchers par lots)"),
                      ("etape-b", "lecture mécanique, règle (a), 800 directions")):
        q = sp.add_parser(nom, help=aide)
        q.add_argument("racine")
        q.add_argument("run_t06")
        if nom == "etape-b":
            q.add_argument("run_t07")
        q.add_argument("config_t07")
        q.add_argument("--registre", default=None, help="défaut : clé `registre` de la configuration")
        q.add_argument("--racine-sortie", default=None)
        q.add_argument("--instant", default=None, type=int, help="instant d'ouverture (secondes UTC) ; essais seulement")
    e = sp.add_parser("empreinte-config", help="empreinte canonique de la configuration (contrôles de la v4)")
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
            print(f"notation scellée, fermée : {r['scores']['chemin']} ; sondes lues {r['index']['sondes_lues']} ; plancher des "
                  f"figées : {r['planchers_figees']['etats']}")
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


__all__ = ["exiger_configuration", "charger_configuration", "empreinte_configuration", "methode_plancher", "charger_planchers_p3",
           "lecture_planchers_p3", "paliers_de", "reserves_plancher_figees", "exiger_nombre_de_directions", "controle_avant_ouverture", "noter", "etape_a", "etape_b", "main", "CLES_CONFIG",
           "CLE_P3_DESCRIPTIF", "SOURCE_P3",
           "SOURCE_FIGEES", "LECTURE_P3"]


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
'''


def main(arbre: Path) -> int:
    sys.path.insert(0, str(arbre / "src"))
    sys.path.insert(0, str(arbre / "tests"))
    m = importlib.import_module("miroir_plancher_v3_v1")
    lv2 = importlib.import_module("controle_ia.t07.lecture_v2")
    lv3 = importlib.import_module("controle_ia.t07.lecture_v3")
    pb = importlib.import_module("controle_ia.t07.passe_blanc_v1")
    rt = importlib.import_module("controle_ia.t07.repli_etapes_v1")
    noter = m.appliquer(inspect.getsource(lv2.noter), m.NOTER)
    etape_a = m.appliquer(inspect.getsource(lv2.etape_a), m.ETAPE_A)
    etape_b = m.appliquer(inspect.getsource(lv3.etape_b), m.ETAPE_B)
    texte = ENTETE + noter + "\n\n" + etape_a + "\n\n# ------------------------------------------------------------------------------------------------------------- étape B (copie)\n" + etape_b + PIED
    dossier = arbre / "src" / "controle_ia" / "t07"
    for nom, contenu in (("lecture_v4.py", texte),
                         ("passe_blanc_v2.py", m.appliquer(Path(pb.__file__).read_text(encoding="utf-8"), m.PASSE_BLANC)),
                         ("repli_etapes_v2.py", m.appliquer(Path(rt.__file__).read_text(encoding="utf-8"), m.REPLI))):
        cible = dossier / nom
        if cible.exists():
            raise SystemExit(f"{cible} existe déjà : rien n'est écrasé (R12) ; le retirer à la main avant de régénérer")
        cible.write_text(contenu, encoding="utf-8")
        print("écrit", cible)
    return 0


if __name__ == "__main__":
    sys.exit(main(Path(sys.argv[1]).resolve()))
