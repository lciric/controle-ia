"""Invites publiées par Terekhov et al. (arXiv 2606.08892v2), transcrites et vérifiées sur le PDF.

Source : `docs/sources/invites-2606.08892-v1/` (18 invites, vérification par script, 18 conformes). Une invite n'est
rendue qu'après deux contrôles : son empreinte compagnon (scellement) et l'empreinte consignée dans `index.json`
(lui-même scellé). Toute différence arrête (R5, R11) : aucune invite modifiée n'entre dans un run.
"""
from __future__ import annotations

import json
from pathlib import Path

from ..gardes import GardeArret
from ..scellement import empreinte, verifier

RACINE_INVITES = Path(__file__).resolve().parents[3] / "docs" / "sources" / "invites-2606.08892-v1"


def index_invites(racine: str | Path = RACINE_INVITES) -> dict[str, dict]:
    """Index des invites par identifiant (H1, H3, H4, I8, …), après vérification de son scellement."""
    chemin = Path(racine) / "index.json"
    verifier(chemin)
    brut = json.loads(chemin.read_text(encoding="utf-8"))
    items = brut["invites"] if isinstance(brut, dict) and "invites" in brut else brut
    if not isinstance(items, list):
        raise GardeArret(f"{chemin} : liste d'invites attendue")
    index = {}
    for it in items:
        if it["id"] in index:
            raise GardeArret(f"{chemin} : identifiant d'invite en double : {it['id']}")
        index[it["id"]] = it
    return index


def charger_invite(identifiant: str, racine: str | Path = RACINE_INVITES) -> str:
    """Texte exact d'une invite transcrite ; arrêt si son fichier, son scellement ou l'index divergent."""
    index = index_invites(racine)
    if identifiant not in index:
        raise GardeArret(f"invite {identifiant!r} absente de l'index ({sorted(index)})")
    it = index[identifiant]
    chemin = Path(racine) / it["fichier"]
    h = verifier(chemin)
    if h != it["sha256"]:
        raise GardeArret(f"{chemin} : empreinte {h[:12]}… ≠ index {it['sha256'][:12]}…")
    return chemin.read_text(encoding="utf-8")


def empreinte_invite(identifiant: str, racine: str | Path = RACINE_INVITES) -> str:
    """Empreinte de l'invite telle que chargée (à consigner dans le manifeste d'un run)."""
    charger_invite(identifiant, racine)
    return empreinte(Path(racine) / index_invites(racine)[identifiant]["fichier"])
