"""Gardes d'arrêt communes (R5).

Une garde qui commande un arrêt lève `GardeArret`. Elle n'a jamais de repli
silencieux : pas de valeur par défaut substituée, pas d'exception avalée.
Chaque garde est testée sur un cas sain et sur un artefact (voir `tests/`).
"""
from __future__ import annotations

import subprocess
from pathlib import Path

VERSION_NUMPY_MINIMALE = (1, 25)


class GardeArret(RuntimeError):
    """Arrêt commandé par une garde. Ne jamais l'attraper pour continuer."""


def _version_tuple(version: str) -> tuple[int, ...]:
    morceaux = []
    for partie in version.split("."):
        chiffres = ""
        for c in partie:
            if not c.isdigit():
                break
            chiffres += c
        if not chiffres:
            break
        morceaux.append(int(chiffres))
    if not morceaux:
        raise GardeArret(f"version illisible : {version!r}")
    return tuple(morceaux)


def exiger_numpy_minimal(version: str | None = None) -> str:
    """R9 : `numpy.random.SeedSequence` avec numpy >= 1.25."""
    if version is None:
        import numpy

        version = numpy.__version__
    if _version_tuple(version)[:2] < VERSION_NUMPY_MINIMALE:
        raise GardeArret(f"numpy {version} < 1.25 : R9 exige numpy >= 1.25")
    return version


def etat_git(racine: str | Path) -> dict:
    """Commit courant et propreté de l'arbre de travail."""
    racine = Path(racine)

    def git(*args: str) -> str:
        r = subprocess.run(["git", "-C", str(racine), *args], capture_output=True, text=True)
        if r.returncode != 0:
            raise GardeArret(f"git {' '.join(args)} a échoué dans {racine} : {r.stderr.strip()}")
        return r.stdout

    commit = git("rev-parse", "HEAD").strip()
    statut = git("status", "--porcelain", "--untracked-files=all")
    return {"commit": commit, "propre": statut.strip() == "", "statut": statut}


def exiger_depot_propre(racine: str | Path) -> str:
    """Un run se rattache à un commit exact : l'arbre doit être propre."""
    etat = etat_git(racine)
    if not etat["propre"]:
        raise GardeArret(
            "arbre de travail non propre : committer avant le run, ou autoriser "
            "explicitement (la réserve est alors consignée au manifeste)\n" + etat["statut"]
        )
    return etat["commit"]
