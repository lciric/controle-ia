"""Repli de l'étape A (recalcul des activations), **garde d'ouverture d'abord** — v1, révisé par DF-01 (contre-lecture différentielle
du code, `dd794e2e…`) ; fichier neuf du jalon 12, jamais versé sous ce nom avant cette révision.

Ordre des gestes (plan, point 8, repli ; R11 ; variante B, R-2112) :

1. **Garde d'ouverture de l'étape A** (`lecture_v2.ouvrir`, journalisée) **avant tout calcul** : lignes de registre exigées et
   leurs sceaux, ligne de GO, refus de la course 7a (`go_id` du manifeste cité), `CODE-T07` si elle est exigée, garde adaptée.
   Refus → code 2, rien n'est calculé ; la relance après l'inscription de la ligne manquante est une simple attente.
2. **Reprise** : si `donnees/<run>/activations/` existe, il doit porter un rapport du repli scellé (`rapport-repli-t07.json`) qui le
   **couvre** (même run, même manifeste de 7b, empreinte des activations recalculée égale) : le recalcul n'est pas refait. Sans
   rapport qui le couvre → refus (R12 : ce ne sont pas des activations du repli).
3. **Recalcul** (`repli_recalcul_v1.recalculer`) sous un **nom daté** `donnees/<run>/activations-repli-<AAAAMMJJ-HHMMSS>/`, jamais
   écrasé : contrôle d'identité à dose 0, rejeu en forçage, garde d'équivalence. Échec (R11) → code 3, le dossier daté reste : la
   **relance une fois sur la même carte** recalcule sous un autre nom daté. Réussite → empreinte des activations, dossier renommé
   en `donnees/<run>/activations/` (absent : rien n'est écrasé), rapport scellé à côté des activations.

Commandes (par `python -m controle_ia.t07.lecture_v2`) :
- `repli-seul RACINE RUN_T06 CONFIG_T07 [--registre CHEMIN]` : 1 à 3 ; codes 0, 2 (refus de la garde, R12), 3 (R11) ;
- `etape-a-apres-repli RACINE RUN_T06 CONFIG_T07 [--registre CHEMIN]` : rapport relu et couvrant (2), puis `etape_a(…, repli=…)` (garde
  d'identité remplacée par la garde d'équivalence) ; codes de l'étape A ;
- `repli-recalcul` de `lecture_v2` enchaîne `repli` puis l'étape A (même ordre, même reprise).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from pathlib import Path

from ..gardes import GardeArret
from ..scellement import sceller, verifier
from . import registre_v1 as rg

RAPPORT = "rapport-repli-t07.json"
CODE_OK, CODE_REFUS, CODE_ARRET = 0, 2, 3


class RefusRepli(GardeArret):
    """Refus avant tout calcul (code 2)."""


class ArretRepli(GardeArret):
    """Arrêt R11 du recalcul (code 3) : identité à dose 0, rejeu, garde d'équivalence."""


def empreinte_activations(dossier: Path) -> tuple[str, int]:
    """sha256 de la liste triée « chemin relatif, sha256 du fichier » des activations `*.npy` du dossier ; et leur nombre."""
    h, n = hashlib.sha256(), 0
    for p in sorted(Path(dossier).rglob("*.npy")):
        h.update(f"{p.relative_to(dossier).as_posix()} {rg.sha256_de(p)}\n".encode("utf-8"))
        n += 1
    return h.hexdigest(), n


def _activations(racine: Path, run_t06: str) -> Path:
    return Path(racine) / "donnees" / run_t06 / "activations"


def lire_rapport(racine: Path, run_t06: str) -> dict:
    """Rapport du repli qui **couvre** `donnees/<run>/activations/` ; sinon `RefusRepli` (code 2, rien ne s'ouvre)."""
    racine = Path(racine)
    act = _activations(racine, run_t06)
    p = act / RAPPORT
    try:
        verifier(p)
        doc = json.loads(p.read_text(encoding="utf-8"))
        r = doc["rapport"]
        if doc.get("run_t06") != run_t06:
            raise RefusRepli(f"rapport du repli : run {doc.get('run_t06')!r} ≠ {run_t06!r}")
        m = r["manifeste_7b"]
        if m["chemin"] != f"runs/{run_t06}/manifeste.json" or verifier(racine / m["chemin"]) != m["sha256"]:
            raise RefusRepli("rapport du repli : manifeste de 7b autre que celui du recalcul")
        if not isinstance(r.get("garde_equivalence"), dict) or "ecart_max" not in r["garde_equivalence"]:
            raise RefusRepli("rapport du repli : garde d'équivalence absente")
        sha, n = empreinte_activations(act)
        if (sha, n) != (r.get("empreinte_activations"), r.get("fichiers_activations")):
            raise RefusRepli(f"rapport du repli : activations changées depuis le recalcul ({n} fichiers, empreinte {sha[:12]}…)")
    except RefusRepli:
        raise
    except GardeArret as e:
        raise RefusRepli(f"rapport du repli : {e}") from None
    except (OSError, ValueError, KeyError, TypeError) as e:
        raise RefusRepli(f"rapport du repli illisible ou absent ({type(e).__name__})") from None
    return r


def repli(racine: Path, registre: Path, config: dict, run_t06: str, instant: int | None = None) -> dict:
    """Garde d'ouverture, puis reprise ou recalcul (docstring du module). Rend {reprise, rapport, chemin, sha256, ouverture}.
    Refus de la garde : `RefusRegistre` (code 2) ; R12 : `RefusRepli` (code 2) ; R11 : `ArretRepli` (code 3)."""
    from . import repli_recalcul_v1 as rr
    from .lecture_v2 import exiger_configuration, ouvrir
    racine, registre = Path(racine), Path(registre)
    try:
        exiger_configuration(config)
    except GardeArret as e:
        raise RefusRepli(f"configuration : {e}") from None
    instant = int(time.time()) if instant is None else int(instant)
    ouverture = ouvrir(racine, registre, config, "A", run_t06, instant)                   # DF-01 : la garde d'abord
    resume_garde = {"instant": rg.date_utc(instant), "garde": "garde d'ouverture de l'étape A, journalisée avant le recalcul",
                    "code_t07": ouverture.get("code_t07")}
    act = _activations(racine, run_t06)
    if act.exists():
        r = lire_rapport(racine, run_t06)
        return {"reprise": True, "rapport": r, "chemin": str((act / RAPPORT).relative_to(racine)),
                "sha256": verifier(act / RAPPORT), "ouverture": resume_garde}
    date = time.strftime("%Y%m%d-%H%M%S", time.gmtime(instant))
    dossier = act.parent / f"activations-repli-{date}"
    if dossier.exists():
        raise RefusRepli(f"{dossier} existe déjà (R12)")
    try:
        r = rr.recalculer(racine, run_t06, dossier)
    except GardeArret as e:
        raise ArretRepli(f"{e} ; recalcul gardé sous {dossier.name} (relance une fois sur la même carte, sous un nom neuf, puis nœud)") from None
    sha, n = empreinte_activations(dossier)
    r.update(empreinte_activations=sha, fichiers_activations=n, ecrit_sous=str(dossier.relative_to(racine)),
             dossier_activations=str(act.relative_to(racine)), garde_d_ouverture=resume_garde)
    dossier.rename(act)                                       # `act` absent : rien n'est écrasé
    chemin = act / RAPPORT
    chemin.write_text(json.dumps({"nature": "repli de l'étape A de T0.7 : recalcul des activations sous la garde d'ouverture",
                                  "run_t06": run_t06, "instant": rg.date_utc(instant), "rapport": r},
                                 ensure_ascii=False, indent=1, default=str) + "\n", encoding="utf-8")
    return {"reprise": False, "rapport": r, "chemin": str(chemin.relative_to(racine)), "sha256": sceller(chemin),
            "ouverture": resume_garde}


def main(argv: list[str]) -> int:
    from .lecture_v2 import ArretApresManifeste, charger_configuration, etape_a
    p = argparse.ArgumentParser(prog="python -m controle_ia.t07.lecture_v2", description=__doc__.splitlines()[0])
    sp = p.add_subparsers(dest="action", required=True)
    for nom in ("repli-seul", "etape-a-apres-repli"):
        s = sp.add_parser(nom)
        s.add_argument("racine")
        s.add_argument("run_t06")
        s.add_argument("config_t07")
        s.add_argument("--registre", default=None)
    a = p.parse_args(argv)
    try:
        config = charger_configuration(Path(a.config_t07))
    except GardeArret as err:
        print(f"REFUS : {err}", file=sys.stderr)
        return CODE_REFUS
    registre = Path(a.registre) if a.registre else Path(a.racine) / config["registre"]
    if a.action == "repli-seul":
        try:
            r = repli(Path(a.racine), registre, config, a.run_t06)
        except ArretRepli as err:
            print(f"ARRÊT (R11, repli) : {err}", file=sys.stderr)
            return CODE_ARRET
        except GardeArret as err:
            print(f"REFUS : {err}", file=sys.stderr)
            return CODE_REFUS
        g = r["rapport"]["garde_equivalence"]
        print(f"repli : {'reprise sur un recalcul couvert' if r['reprise'] else 'recalcul fait'}, garde d'équivalence passée "
              f"({g.get('actions')} actions, écart maximal {g.get('ecart_max')}) ; rapport {r['chemin']} {r['sha256']}")
        return CODE_OK
    try:
        rapport = lire_rapport(Path(a.racine), a.run_t06)
        r = etape_a(Path(a.racine), registre, config, a.run_t06, repli=rapport)
    except ArretApresManifeste as err:
        print(f"ARRÊT : {err}", file=sys.stderr)
        return CODE_ARRET
    except GardeArret as err:
        print(f"REFUS : {err}", file=sys.stderr)
        return CODE_REFUS
    print(f"notation scellée, fermée : {r['scores']['chemin']} ; sondes lues {r['index']['sondes_lues']}")
    return CODE_OK
