"""Run factice : traverse toute la chaîne manifeste → résultat → scellement → vérification → rejeu.

    python -m controle_ia.run_factice [--racine .] [--run-id AAAAMMJJ-HHMMSS-factice]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from .gardes import GardeArret
from .manifeste import creer_manifeste, ecrire_resultat, generateur, lire_manifeste, verifier_resultat
from .scellement import verifier_arbre

TACHES = ["tirage-a", "tirage-b"]


def calcul(manifeste: dict) -> dict:
    sortie = {}
    for t in TACHES:
        x = generateur(manifeste["graines"][t]).standard_normal(manifeste["config"]["n"])
        sortie[t] = {"moyenne": float(x.mean()), "sha256_tirage": hashlib.sha256(x.tobytes()).hexdigest()}
    return sortie


def executer(racine: str | Path, run_id: str, entropie: int | None = None) -> dict:
    racine = Path(racine)
    chemin_m, m = creer_manifeste(racine, run_id, {"objet": "run factice", "n": 1000}, TACHES,
                                  entropie=entropie, commande="python -m controle_ia.run_factice")
    resultat = calcul(m)
    chemin_r = ecrire_resultat(racine, chemin_m, "resultat", resultat)
    corps = verifier_resultat(racine, chemin_r)
    # Rejeu : mêmes graines, résultat identique au bit près, sinon arrêt.
    m_relu, _ = lire_manifeste(chemin_m)
    if calcul(m_relu) != corps["resultat"]:
        raise GardeArret("rejeu non identique au bit près")
    problemes = [p for p in verifier_arbre(racine, ("runs", "diag")) if run_id in p[0]]
    if problemes:
        raise GardeArret(f"arbre non intact : {problemes}")
    return {"manifeste": str(chemin_m), "resultat": str(chemin_r), "rejeu": "identique"}


def main(argv=None) -> int:
    a = argparse.ArgumentParser()
    a.add_argument("--racine", default=".")
    a.add_argument("--run-id", default=None)
    a.add_argument("--entropie", type=int, default=None)
    args = a.parse_args(argv)
    run_id = args.run_id or datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S") + "-factice"
    print(json.dumps(executer(args.racine, run_id, args.entropie), indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
