"""Alignement des sorties des runs de nuit sur `scores-p3.npz` (format fixé par conv-audit, n° 328).

Les quatre tableaux d'identité (`episode`, `pas`, `condition`, `tache`) des sorties sont ceux du fichier des scores du
run source, dans le même ordre ; leur empreinte (`empreinte_identite`) est écrite au manifeste (dans la configuration) et
vérifiée avant tout calcul. Les textes des actions (`textes-actions-p3.jsonl`) doivent suivre le même ordre, ligne à ligne.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np

from ..gardes import GardeArret
from ..scellement import verifier

CLES_IDENTITE = ("episode", "pas", "condition", "tache")


def empreinte_identite(tableaux: dict) -> str:
    """sha256 des quatre tableaux d'identité, dans l'ordre de `CLES_IDENTITE` : nom, type, forme, puis octets ; les
    chaînes passent en UTF-8 (une ligne par valeur, séparateur « \\n »), les entiers en int64 petit-boutiste."""
    h = hashlib.sha256()
    for k in CLES_IDENTITE:
        a = np.asarray(tableaux[k])
        h.update(f"{k}/{a.shape}\n".encode("utf-8"))
        if a.dtype.kind in ("U", "S", "O"):
            h.update("\n".join(str(x) for x in a.tolist()).encode("utf-8"))
        else:
            h.update(np.ascontiguousarray(a.astype("<i8")).tobytes())
        h.update(b"\x00")
    return h.hexdigest()


def charger_identite(chemin_scores, sha_attendue: str | None = None) -> dict:
    """Tableaux d'identité et colonnes utiles du fichier des scores du run source (scellé), avec son empreinte."""
    sha = verifier(chemin_scores)
    if sha_attendue is not None and sha != sha_attendue:
        raise GardeArret(f"{chemin_scores} : empreinte {sha[:12]} ≠ empreinte citée {sha_attendue[:12]}")
    with np.load(chemin_scores, allow_pickle=False) as z:
        sortie = {k: z[k] for k in z.files}
    manquantes = [k for k in (*CLES_IDENTITE, "jetons", "jetons_notes", "scores", "noms_sondes") if k not in sortie]
    if manquantes:
        raise GardeArret(f"{chemin_scores} : tableaux absents {manquantes}")
    sortie["sha256"] = sha
    return sortie


def charger_textes_alignes(chemin_textes, identite: dict, sha_attendue: str | None = None) -> list[dict]:
    """Textes des actions, ligne à ligne dans l'ordre des scores ; arrêt au premier écart d'identité."""
    sha = verifier(chemin_textes)
    if sha_attendue is not None and sha != sha_attendue:
        raise GardeArret(f"{chemin_textes} : empreinte {sha[:12]} ≠ empreinte citée {sha_attendue[:12]}")
    lignes = [json.loads(x) for x in Path(chemin_textes).read_text(encoding="utf-8").splitlines() if x.strip()]
    n = len(identite["episode"])
    if len(lignes) != n:
        raise GardeArret(f"{len(lignes)} textes pour {n} lignes de scores")
    for i, x in enumerate(lignes):
        for k in CLES_IDENTITE:
            v = identite[k][i]
            v = int(v) if k == "pas" else str(v)
            if x[k] != v:
                raise GardeArret(f"ligne {i} : {k} = {x[k]!r} dans les textes, {v!r} dans les scores (ordre rompu)")
    return lignes
