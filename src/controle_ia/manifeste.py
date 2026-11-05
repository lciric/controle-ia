"""Manifeste de run (R9) : configuration et son empreinte, versions, graines, commit.

Graines : une `numpy.random.SeedSequence` racine par run ; chaque tâche reçoit une
graine dérivée par une clé de dérivation (`spawn_key`) calculée à partir de son nom.
Le manifeste consigne l'entropie racine et les clés : tout tirage se rejoue à
l'identique avec `generateur(manifeste["graines"][tache])`.
"""
from __future__ import annotations

import hashlib
import json
import platform
import re
import sys
from datetime import datetime, timezone
from importlib import metadata
from pathlib import Path

import numpy as np

from .gardes import GardeArret, etat_git, exiger_numpy_minimal
from .scellement import empreinte, sceller, verifier

BIBLIOTHEQUES = ("numpy", "scipy", "matplotlib", "torch", "transformers", "tokenizers", "safetensors", "huggingface_hub",
                 "transformer-lens", "vllm", "peft")
_RUN_ID = re.compile(r"^[0-9]{8}-[0-9]{6}-[a-z0-9][a-z0-9-]{0,62}$")


def config_canonique(config: dict) -> bytes:
    return json.dumps(config, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def cle_de_tache(tache: str) -> int:
    return int.from_bytes(hashlib.sha256(tache.encode("utf-8")).digest()[:8], "big")


def graines(taches: list[str], entropie: int | None = None) -> dict:
    exiger_numpy_minimal()
    if len(set(taches)) != len(taches):
        raise GardeArret(f"noms de tâches en double : {taches}")
    racine = np.random.SeedSequence(entropie)
    sortie = {}
    for t in taches:
        cle = cle_de_tache(t)
        ss = np.random.SeedSequence(racine.entropy, spawn_key=(cle,))
        sortie[t] = {"entropie": str(racine.entropy), "spawn_key": [str(cle)],
                     "etat_controle": [int(x) for x in ss.generate_state(2)]}
    return sortie


def generateur(graine: dict) -> np.random.Generator:
    ss = np.random.SeedSequence(int(graine["entropie"]), spawn_key=tuple(int(k) for k in graine["spawn_key"]))
    if [int(x) for x in ss.generate_state(2)] != graine["etat_controle"]:
        raise GardeArret("graine reconstruite ≠ graine consignée : numpy ou manifeste altéré")
    return np.random.default_rng(ss)


def versions() -> dict:
    v = {"python": sys.version.split()[0], "plateforme": platform.platform()}
    for b in BIBLIOTHEQUES:
        try:
            v[b] = metadata.version(b)
        except metadata.PackageNotFoundError:
            pass
    return v


def creer_manifeste(racine: str | Path, run_id: str, config: dict, taches: list[str], *,
                    entropie: int | None = None, decisif: bool = False,
                    prereg: str | Path | None = None, autoriser_depot_sale: bool = False,
                    commande: str | None = None) -> tuple[Path, dict]:
    """Crée et scelle `runs/<run_id>/manifeste.json`. Lève `GardeArret` sur toute violation."""
    racine = Path(racine)
    if not _RUN_ID.match(run_id):
        raise GardeArret(f"identifiant de run {run_id!r} : format AAAAMMJJ-HHMMSS-nom attendu")
    dossier = racine / "runs" / run_id
    if dossier.exists():
        raise GardeArret(f"{dossier} existe déjà : R12 interdit d'écraser un run")
    git = etat_git(racine)
    reserves = []
    if not git["propre"]:
        if not autoriser_depot_sale:
            raise GardeArret("arbre de travail non propre : committer avant le run\n" + git["statut"])
        reserves.append("arbre de travail non propre au lancement (autorisé explicitement)")
    prereg_info = None
    if decisif and prereg is None:
        raise GardeArret("run décisif sans préenregistrement : R1 interdit de lancer")
    if prereg is not None:
        from .prereg import exiger_prereg_scelle

        p = Path(prereg)
        try:
            chemin_rel = str(p.resolve().relative_to(racine.resolve()))
        except ValueError:
            raise GardeArret(f"préenregistrement {p} hors du dépôt {racine}") from None
        prereg_info = {"chemin": chemin_rel, "sha256": exiger_prereg_scelle(p)}
    canon = config_canonique(config)
    manifeste = {
        "run_id": run_id,
        "cree_le": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "commit": git["commit"],
        "depot_propre": git["propre"],
        "decisif": decisif,
        "preenregistrement": prereg_info,
        "config": config,
        "config_sha256": hashlib.sha256(canon).hexdigest(),
        "versions": versions(),
        "graines": graines(taches, entropie),
        "commande": commande,
        "reserves": reserves,
    }
    dossier.mkdir(parents=True)
    chemin = dossier / "manifeste.json"
    chemin.write_text(json.dumps(manifeste, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    sceller(chemin)
    return chemin, manifeste


def lire_manifeste(chemin: str | Path) -> tuple[dict, str]:
    """Vérifie l'empreinte puis la cohérence configuration/empreinte de configuration."""
    sha = verifier(chemin)
    m = json.loads(Path(chemin).read_text(encoding="utf-8"))
    if hashlib.sha256(config_canonique(m["config"])).hexdigest() != m["config_sha256"]:
        raise GardeArret(f"{chemin} : empreinte de configuration incohérente")
    return m, sha


def ecrire_resultat(racine: str | Path, manifeste_chemin: str | Path, nom: str, contenu: dict) -> Path:
    """Écrit et scelle `diag/<run_id>/<nom>.json`, rattaché au manifeste par son empreinte."""
    m, sha_m = lire_manifeste(manifeste_chemin)
    dossier = Path(racine) / "diag" / m["run_id"]
    dossier.mkdir(parents=True, exist_ok=True)
    chemin = dossier / f"{nom}.json"
    if chemin.exists():
        raise GardeArret(f"{chemin} existe déjà : R12 interdit d'écraser")
    corps = {"run_id": m["run_id"], "manifeste_sha256": sha_m, "resultat": contenu}
    chemin.write_text(json.dumps(corps, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    sceller(chemin)
    return chemin


def verifier_resultat(racine: str | Path, chemin_resultat: str | Path) -> dict:
    """Chaîne complète : résultat intact → manifeste intact → rattachement par empreinte."""
    verifier(chemin_resultat)
    corps = json.loads(Path(chemin_resultat).read_text(encoding="utf-8"))
    manifeste = Path(racine) / "runs" / corps["run_id"] / "manifeste.json"
    _, sha_m = lire_manifeste(manifeste)
    if sha_m != corps["manifeste_sha256"]:
        raise GardeArret(f"{chemin_resultat} : rattaché à un autre manifeste ({corps['manifeste_sha256'][:12]}…)")
    return corps


__all__ = ["graines", "generateur", "creer_manifeste", "lire_manifeste", "ecrire_resultat",
           "verifier_resultat", "config_canonique", "empreinte"]
