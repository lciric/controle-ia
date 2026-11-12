"""Lanceur de P3-bis (témoin positif planté), côté machine de calcul : la logique de P3 (`premier_test_ia.run`), importée
et inchangée, sans échéance.

Texte : `prereg/P3-bis-temoin-positif-v1.md` (brouillon 6 : `brouillons/P3-bis-temoin-positif-v1/
P3-bis-preenregistrement-v1-brouillon6.md`, `aeb1f63a…`), section « Ce que le code et la chaîne doivent changer », point
2 (a) ; décision DB-3 (a) (R-2015) ; GO-2026-11-02-29 : « aucun budget de temps qui coupe une étape ».

    PYTHONPATH=src python -m controle_ia.premier_test_ia.run_v2 --config C --taches T --run-id R [--prereg P]

Même point d'entrée que `run` (`--config`, `--taches`, `--run-id`, `--prereg`). Seul écart : la lecture des deux durées de
la configuration, `duree_max_s` et `budget_entrainement_s`.
- `null` (None) est accepté et veut dire « aucune échéance » ; une clé absente reste refusée (« configuration de P3
  incomplète ») ;
- toute autre valeur est contrôlée par `run.exiger_config_p3` lui-même (l. 110-113, même message) et garde l'échéance de
  P3 : une borne non nulle arrête encore ;
- la configuration citée et le manifeste gardent `null` : aucune durée numérique n'y est écrite.

**Moyen, choix déclaré** (le texte : « si l'appel de `_executer_apres_manifeste` exige une copie de la fonction, la copie
est déclarée et comparée ligne à ligne à l'original ») : `run._executer_apres_manifeste` est appelée **telle quelle, sans
copie**. Elle reçoit une vue de la configuration (`vue_sans_echeance`) où une durée `null` est lue comme l'infini
(`math.inf`) : `debut + inf` (l. 395) et `min(inf, depart + inf)` (l. 434) donnent une échéance infinie, que
`entrainement._echeance` et `harnais.episode.jouer_episodes` (« `time.perf_counter() > echeance` ») ne franchissent
jamais ; la fonction n'écrit aucune des deux durées (ni au manifeste, créé avant elle, ni dans ses résultats), donc l'infini
n'est écrit nulle part. Seule `run.executer` (l. 349-381) est recopiée ici, sous `executer` : elle appelle
`exiger_config_p3` en tête, qui refuse `null`. La copie est comparée ligne à ligne à l'original par `ecart_a_p3()` (essai
`test_copie_d_executer_comparee_a_celle_de_p3`) : seules diffèrent la garde de configuration et l'appel de
`_executer_apres_manifeste` (la vue des durées) ; la commande consignée au manifeste est celle de ce module.
"""
from __future__ import annotations

import argparse
import difflib
import inspect
import json
import math
import signal
import sys
import time
from pathlib import Path

from . import run as rp
from .run import (_executer_apres_manifeste, charger_consignes, charger_invite, charger_taches, cles_des_graines,
                  creer_manifeste, ecrire_resultat, empreinte_config, exiger_citations_p3, exiger_code_cite,
                  exiger_code_importe_sous, exiger_memoire_vive, motif_d_arret, plan_p3, relever_term_apres, verifier)
from ..gardes import GardeArret

COMMANDE = "python -m controle_ia.premier_test_ia.run_v2"
DUREES = ("duree_max_s", "budget_entrainement_s")
# lignes de `run.executer` que la copie change, et leur remplacement (comparaison ligne à ligne, `ecart_a_p3`)
ECART_ATTENDU = (
    ("    exiger_config_p3(config)", "    exiger_config_p3bis(config)"),
    ("        return _executer_apres_manifeste(config, racine, run_id, chemin_m, manifeste, taches, plan, consignes, etat,",
     "        return _executer_apres_manifeste(vue_sans_echeance(config), racine, run_id, chemin_m, manifeste, taches, plan,"),
    ("                                         debut)",
     "                                         consignes, etat, debut)"),
)


def _vue_controlee(config: dict) -> dict:
    """Vue pour la garde de P3 : une durée présente et `null` est remplacée par la borne permise de P3 (valeur que la garde
    accepte) ; une durée absente reste absente (refus « incomplète ») ; toute autre valeur passe telle quelle."""
    return {k: (rp.DUREE_MAX_S if k in DUREES and v is None else v) for k, v in config.items()}


def exiger_config_p3bis(config: dict) -> None:
    """Garde de configuration de P3-bis : celle de P3 (`run.exiger_config_p3`), sauf que `duree_max_s` et
    `budget_entrainement_s` peuvent valoir `null` (aucune échéance). Une valeur non nulle est contrôlée par la garde de P3,
    avec son message."""
    if not isinstance(config, dict):
        raise GardeArret("configuration : objet JSON attendu")
    rp.exiger_config_p3(_vue_controlee(config))


def vue_sans_echeance(config: dict) -> dict:
    """Vue de la configuration passée à `run._executer_apres_manifeste` : une durée `null` lue comme l'infini (aucune
    échéance), une durée numérique gardée (échéance de P3). Jamais écrite : le manifeste et la configuration citée gardent
    `null`."""
    return {k: (math.inf if k in DUREES and v is None else v) for k, v in config.items()}


def executer(config: dict, racine: Path, run_id: str, prereg: str | None, chemin_taches: str,
             autoriser_depot_sale: bool = False) -> dict:
    racine = Path(racine)
    exiger_config_p3bis(config)
    if config["mode"] == "reel" and prereg is None:
        raise GardeArret("run réel de P3 sans préenregistrement : R1 interdit de lancer")
    taches = charger_taches(chemin_taches)
    sha_taches = verifier(chemin_taches)
    consignes = charger_consignes(config["chemin_consignes"], config["consignes_sha256"])
    charger_invite("H1-classification")
    commit_cite, entropie = None, None
    if prereg is not None:
        exiger_code_importe_sous(racine)
        commit_cite = exiger_code_cite(racine, Path(prereg))
        entropie = exiger_citations_p3(Path(prereg), config, sha_taches)
    plan = plan_p3(taches)
    chemin_m, manifeste = creer_manifeste(racine, run_id, config, cles_des_graines(taches, config), entropie=entropie,
                                          decisif=prereg is not None, prereg=prereg,
                                          autoriser_depot_sale=autoriser_depot_sale, commande=COMMANDE)
    debut = time.perf_counter()
    etat = {"etape": "mémoire vive", "commit_cite": commit_cite, "taches_sha256": sha_taches,
            "config_sha256": empreinte_config(config), "consignes_sha256": consignes["sha256"]}
    try:
        etat["memoire_vive"] = exiger_memoire_vive(config["memoire_vive_min_go"]) if config["memoire_vive_min_go"] else None
        etat["etape"] = "chargement"
        return _executer_apres_manifeste(vue_sans_echeance(config), racine, run_id, chemin_m, manifeste, taches, plan,
                                         consignes, etat, debut)
    except Exception as e:          # garde, panne, signal TERM : consigné, puis propagé
        ecrire_resultat(racine, chemin_m, "arret", {"etape": etat["etape"], "motif": motif_d_arret(e),
                                                     "partiel": {k: v for k, v in etat.items() if k != "etape"},
                                                     "duree_s": round(time.perf_counter() - debut, 1)})
        relever_term_apres(e)
        raise


def ecart_a_p3() -> dict:
    """Comparaison ligne à ligne de `executer` (ce module) à `run.executer` (P3) : lignes retirées et ajoutées, dans
    l'ordre ; `conforme` si elles sont exactement celles d'`ECART_ATTENDU`. Sortie versée au candidat (texte, point 2 (a))."""
    a = inspect.getsource(rp.executer).splitlines()
    b = inspect.getsource(executer).splitlines()
    retirees, ajoutees = [], []
    for ligne in difflib.ndiff(a, b):
        if ligne.startswith("- "):
            retirees.append(ligne[2:])
        elif ligne.startswith("+ "):
            ajoutees.append(ligne[2:])
    attendu_r, attendu_a = [x for x, _ in ECART_ATTENDU], [y for _, y in ECART_ATTENDU]
    return {"lignes_p3": len(a), "lignes_p3bis": len(b), "retirees": retirees, "ajoutees": ajoutees,
            "conforme": retirees == attendu_r and ajoutees == attendu_a}


_signal_term = rp.lever_sur_term


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
