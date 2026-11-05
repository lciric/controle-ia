"""Politique de stockage par défaut (brief, T0.4), commune au run factice et à la validation sur modèle réel.

- Vecteurs d'action (maximum par coordonnée) et scores de sondes (maximum ou attention), calculés en ligne,
  pour tous les épisodes.
- Activations par jeton seulement pour les épisodes d'entraînement déclarés.
- Codage sur disque : `float32` (modèle en simple précision) ou `bfloat16-bits` (modèle en demi-précision
  bfloat16 : les 16 bits de poids fort de chaque valeur, sans perte puisque les valeurs capturées en
  viennent ; 2 octets par valeur). Toute valeur non représentable arrête le codage (aucun arrondi
  silencieux).
- Relecture : le disque rend ce qui a été calculé en ligne ; pour un épisode d'entraînement, vecteurs et
  scores recalculés hors ligne depuis les activations relues sont identiques au bit près.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np

from ..gardes import GardeArret
from ..manifeste import generateur
from ..scellement import sceller, verifier
from .activations import AGREGATIONS, couches_par_defaut
from .episode import vecteurs_par_action
from .sondes import AGREGATIONS_SONDE, exiger_identite, scores_en_ligne, sonde_lineaire_aleatoire

POSITIONS_COUCHE = {"precoce": 0, "mediane": 1, "tardive": 2}
CODAGES = ("float32", "bfloat16-bits")


def valider_politique(politique: dict, n_couches: int, episodes: int) -> None:
    """Gardes sur la politique, avant tout manifeste (aucun run à moitié créé)."""
    if not set(politique["episodes_par_jeton"]) <= set(range(episodes)):
        raise GardeArret(f"épisodes d'entraînement {politique['episodes_par_jeton']} hors de [0, {episodes}[")
    for methode in politique["vecteurs_par_action"]:
        if methode not in AGREGATIONS:
            raise GardeArret(f"vecteur d'action par {methode!r} refusé : seul {AGREGATIONS} (brief, T0.7)")
    couches = couches_par_defaut(n_couches)
    noms = [d["nom"] for d in politique["sondes"]]
    if len(set(noms)) != len(noms):
        raise GardeArret(f"noms de sondes en double : {noms}")
    for d in politique["sondes"]:
        pos = POSITIONS_COUCHE.get(d["couche"])
        if pos is None or pos >= len(couches):
            raise GardeArret(f"sonde {d['nom']} : couche {d['couche']!r} indisponible parmi {couches}")
        if d["agregation"] not in AGREGATIONS_SONDE:
            raise GardeArret(f"sonde {d['nom']} : agrégation {d['agregation']!r} refusée ; seulement {AGREGATIONS_SONDE} "
                             "(brief, T0.7)")


def construire_sondes(politique: dict, couches: list[int], largeur: int, graines: dict, prefixe: str = "sonde-") -> list:
    sondes = []
    for d in politique["sondes"]:
        pos = POSITIONS_COUCHE.get(d["couche"])
        if pos is None or pos >= len(couches):
            raise GardeArret(f"sonde {d['nom']} : couche {d['couche']!r} indisponible parmi {couches}")
        sondes.append(sonde_lineaire_aleatoire(d["nom"], couches[pos], largeur, d["agregation"],
                                               generateur(graines[f"{prefixe}{d['nom']}"])))
    return sondes


def calculer_en_ligne(politique: dict, episode, acts: dict, couches: list[int], sondes: list) -> tuple[dict, dict]:
    """Vecteurs d'action (par couche et par agrégation) et scores de sondes, depuis la mémoire."""
    vecteurs = {f"couche{c}/{m}": vecteurs_par_action(episode, acts, c, m)
                for c in couches for m in politique["vecteurs_par_action"]}
    return vecteurs, scores_en_ligne(episode, acts, sondes)


def coder(a: np.ndarray, codage: str) -> np.ndarray:
    if codage == "float32":
        if a.dtype != np.float32:
            raise GardeArret(f"codage float32 : tableau de type {a.dtype}")
        return a
    if codage == "bfloat16-bits":
        u = np.ascontiguousarray(a, dtype=np.float32).view(np.uint32)
        if np.any(u & np.uint32(0xFFFF)):
            raise GardeArret("codage bfloat16-bits : valeurs non représentables en bfloat16 (arrondi refusé)")
        return (u >> np.uint32(16)).astype(np.uint16)
    raise GardeArret(f"codage {codage!r} inconnu ; permis : {CODAGES}")


def decoder(a: np.ndarray, codage: str) -> np.ndarray:
    if codage == "float32":
        return a
    if codage == "bfloat16-bits":
        if a.dtype != np.uint16:
            raise GardeArret(f"décodage bfloat16-bits : tableau de type {a.dtype}")
        return (a.astype(np.uint32) << np.uint32(16)).view(np.float32)
    raise GardeArret(f"codage {codage!r} inconnu ; permis : {CODAGES}")


def ecrire_tableaux(chemin: Path, acts: dict | None, vecteurs: dict, scores: dict, codage: str = "float32") -> Path:
    """npz scellé : vecteurs d'action et scores toujours ; activations par jeton si `acts` est fourni."""
    if chemin.exists():
        raise GardeArret(f"{chemin} existe déjà : R12 interdit d'écraser")
    tableaux = {f"par_action/{k}": coder(v, codage) for k, v in vecteurs.items()}
    tableaux.update({f"scores/{k}": v for k, v in scores.items()})
    for agent, par_couche in (acts or {}).items():
        for couche, a in par_couche.items():
            tableaux[f"par_jeton/agent{agent}/couche{couche}"] = coder(a, codage)
    chemin.parent.mkdir(parents=True, exist_ok=True)
    np.savez(chemin, **tableaux)
    sceller(chemin)
    return chemin


def relire_et_controler(chemin: Path, politique: dict, episode, couches: list[int], sondes: list, vecteurs: dict,
                        scores: dict, par_jeton: bool, codage: str = "float32", acts: dict | None = None) -> None:
    """Garde : le disque rend ce qui a été calculé en ligne. Vecteurs et scores relus identiques au bit près ; pour
    un épisode d'entraînement, chaque tableau d'activations par jeton relu et décodé est identique au bit près, formes
    comprises, à celui de la mémoire (`acts`, obligatoire alors : toutes les positions, pas seulement les empans
    d'action), et vecteurs et scores recalculés hors ligne depuis ces activations le sont aussi."""
    if par_jeton and acts is None:
        raise GardeArret(f"{episode.identifiant} : relecture des activations par jeton sans la référence en mémoire")
    verifier(chemin)
    with np.load(chemin) as z:
        exiger_identite(vecteurs, {k[len("par_action/"):]: decoder(z[k], codage) for k in z.files
                                   if k.startswith("par_action/")}, f"{episode.identifiant}, vecteurs relus")
        exiger_identite(scores, {k[len("scores/"):]: z[k] for k in z.files if k.startswith("scores/")},
                        f"{episode.identifiant}, scores relus")
        cles = [k for k in z.files if k.startswith("par_jeton/")]
        if not par_jeton:
            if cles:
                raise GardeArret(f"{episode.identifiant} : activations par jeton conservées hors entraînement")
            return
        acts_disque: dict[int, dict[int, np.ndarray]] = {}
        for k in cles:
            _, agent, couche = k.split("/")
            acts_disque.setdefault(int(agent[len("agent"):]), {})[int(couche[len("couche"):])] = decoder(z[k], codage)
    exiger_identite({f"agent{a}/couche{c}": v for a, pc in acts.items() for c, v in pc.items()},
                    {f"agent{a}/couche{c}": v for a, pc in acts_disque.items() for c, v in pc.items()},
                    f"{episode.identifiant}, activations par jeton relues")
    v2, s2 = calculer_en_ligne(politique, episode, acts_disque, couches, sondes)
    exiger_identite(vecteurs, v2, f"{episode.identifiant}, vecteurs recalculés hors ligne")
    exiger_identite(scores, s2, f"{episode.identifiant}, scores recalculés hors ligne")
