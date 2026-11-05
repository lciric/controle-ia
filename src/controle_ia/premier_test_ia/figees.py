"""Sondes figées de P3 : écriture et relecture d'un fichier scellé (npz) qui porte toutes les sondes et les planchers,
avant le premier épisode. L'empreinte du fichier fige l'ensemble ; chaque sonde garde aussi sa propre empreinte
(`empreinte()`), contrôlée à la relecture. Rien n'est sérialisé par `pickle` (`allow_pickle=False`)."""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from ..gardes import GardeArret
from ..harnais.sondes import SondeLineaire
from ..scellement import sceller, verifier
from ..sondes.familles import SondeLineaireJetons, SondeMahalanobis, SondePerceptron

TABLEAUX = {"SondeLineaireJetons": ("w", "q"), "SondeLineaire": ("w", "q"), "SondePerceptron": ("mu", "s", "W", "c", "v", "q"),
            "SondeMahalanobis": ("mu", "P")}
CLASSES = {"SondeLineaireJetons": SondeLineaireJetons, "SondeLineaire": SondeLineaire, "SondePerceptron": SondePerceptron,
           "SondeMahalanobis": SondeMahalanobis}


def _empreinte(s) -> str:
    return s.empreinte()


def ecrire_sondes(chemin, sondes, meta: dict) -> str:
    """Écrit le fichier (refus s'il existe, R12), le scelle et rend son empreinte."""
    chemin = Path(chemin)
    if chemin.exists():
        raise GardeArret(f"{chemin} existe déjà (R12)")
    noms = [s.nom for s in sondes]
    if len(set(noms)) != len(noms):
        raise GardeArret("sondes figées : noms en double")
    index, tableaux = [], {}
    for k, s in enumerate(sondes):
        classe = type(s).__name__
        if classe not in TABLEAUX:
            raise GardeArret(f"sonde {s.nom} : classe {classe} non sérialisable")
        entree = {"classe": classe, "nom": s.nom, "couche": int(s.couche), "agregation": s.agregation,
                  "famille": getattr(s, "famille", None), "b": float(s.b) if hasattr(s, "b") else None,
                  "empreinte": _empreinte(s), "tableaux": []}
        for t in TABLEAUX[classe]:
            v = getattr(s, t, None)
            if v is not None:
                tableaux[f"s{k}_{t}"] = np.asarray(v, dtype=np.float64)
                entree["tableaux"].append(t)
        index.append(entree)
    tableaux["index"] = np.frombuffer(json.dumps({"sondes": index, "meta": meta}, ensure_ascii=False,
                                                 sort_keys=True).encode("utf-8"), dtype=np.uint8)
    chemin.parent.mkdir(parents=True, exist_ok=True)
    with open(chemin, "wb") as f:
        np.savez(f, **tableaux)
    return sceller(chemin)


def lire_sondes(chemin, sha_attendue: str | None = None) -> tuple[list, dict, str]:
    """Relit le fichier scellé ; chaque sonde reconstruite doit rendre son empreinte écrite."""
    sha = verifier(chemin)
    if sha_attendue is not None and sha != sha_attendue:
        raise GardeArret(f"sondes figées : empreinte {sha[:12]} ≠ empreinte attendue {sha_attendue[:12]}")
    with np.load(chemin, allow_pickle=False) as z:
        index = json.loads(bytes(z["index"]).decode("utf-8"))
        sondes = []
        for k, e in enumerate(index["sondes"]):
            t = {n: z[f"s{k}_{n}"] for n in e["tableaux"]}
            classe = e["classe"]
            if classe == "SondeLineaireJetons":
                s = SondeLineaireJetons(e["nom"], e["couche"], e["agregation"], t["w"], e["b"], t.get("q"), e["famille"])
            elif classe == "SondeLineaire":
                s = SondeLineaire(e["nom"], e["couche"], t["w"], e["b"], e["agregation"], t.get("q"))
            elif classe == "SondePerceptron":
                s = SondePerceptron(e["nom"], e["couche"], e["agregation"], t["mu"], t["s"], t["W"], t["c"], t["v"], e["b"],
                                    t.get("q"), e["famille"])
            elif classe == "SondeMahalanobis":
                s = SondeMahalanobis(e["nom"], e["couche"], t["mu"], t["P"], e["agregation"], e["famille"])
            else:
                raise GardeArret(f"classe {classe!r} inconnue dans {chemin}")
            if _empreinte(s) != e["empreinte"]:
                raise GardeArret(f"sonde {e['nom']} : empreinte reconstruite ≠ empreinte écrite")
            sondes.append(s)
    return sondes, index["meta"], sha
