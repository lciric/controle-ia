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


MOTIF_TERM = "signal TERM reçu (délai externe du run ou plafond de l'amorce) : arrêt consigné"
# signaux TERM reçus par le processus : posés par `lever_sur_term`, jamais retirés (les tests les effacent)
SIGNAL_TERM_RECU: list[int] = []


def lever_sur_term(signum, frame) -> None:
    """Gestionnaire du signal TERM des lanceurs de T0.5 : pose le drapeau, puis lève `GardeArret`. Une bibliothèque peut
    avaler l'exception levée pendant son code, ou la convertir (import paresseux de torch, pendant la mise en place :
    vu le 2026-10-10, relecture de la revalidation, D-1). Le drapeau reste alors posé : `exiger_sans_signal` le relève
    aux points de contrôle (chaque pas des épisodes, chaque lot des notations et de l'appariement, avant le repère,
    avant le résumé), et le bloc qui consigne l'arrêt écrit le motif « signal TERM » quelle que soit l'exception.
    Seul le premier signal lève : `timeout` relaie TERM au processus puis à son groupe, et un second signal ne doit pas
    interrompre la consignation de l'arrêt (vérification 2 du remplissage, K-1) ; il pose le drapeau, relevé comme le
    premier aux points de contrôle."""
    premier = not SIGNAL_TERM_RECU
    SIGNAL_TERM_RECU.append(signum)
    if premier:
        raise GardeArret(MOTIF_TERM)


def signal_term_recu() -> bool:
    return bool(SIGNAL_TERM_RECU)


def exiger_sans_signal(ou: str) -> None:
    """Point de contrôle : un signal TERM reçu, même avalé ou converti par une bibliothèque, arrête ici."""
    if SIGNAL_TERM_RECU:
        raise GardeArret(f"{MOTIF_TERM} (relevé {ou})")


def motif_d_arret(e: BaseException) -> str:
    """Motif consigné dans `arret.json` : celui de l'exception, précédé du signal TERM s'il a été reçu."""
    motif = f"{type(e).__name__}: {e}"
    return motif if not SIGNAL_TERM_RECU or MOTIF_TERM in motif else f"{MOTIF_TERM} ; exception reçue : {motif}"


def relever_term_apres(e: BaseException) -> None:
    """Après la consignation de l'arrêt : un signal TERM reçu est l'arrêt qui fait foi, même si l'exception vue est
    autre (conversion par une bibliothèque) ; sinon l'exception d'origine est propagée par l'appelant."""
    if SIGNAL_TERM_RECU and not (isinstance(e, GardeArret) and MOTIF_TERM in str(e)):
        raise GardeArret(MOTIF_TERM) from e


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
