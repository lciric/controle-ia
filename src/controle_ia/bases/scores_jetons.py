"""Score continu d'un moniteur génératif par la probabilité des jetons (P-003, T0.8).

Le moniteur reçoit sa consigne et son contenu, puis une réponse imposée qui s'arrête juste avant la valeur à lire (par
exemple la balise ouvrante `<sandbagging_confidence>` du détecteur H.12 de 2606.08892, ou rien d'autre que l'en-tête de
réponse pour un juge en une passe). Le score est l'espérance de la valeur sous la loi du jeton suivant, renormalisée sur
les jetons des valeurs admises ; la masse de ces jetons avant renormalisation est consignée (une masse faible veut dire
que le moniteur voulait écrire autre chose : anomalie consignée, jamais remplacée).

Aucun nombre n'est généré puis relu : la même lecture vaut pour toutes les conditions et toutes les intensités (leçon de
P3 : jamais de verdict sur une fenêtre tronquée ; remarque du lecteur de la porte GC sur 2606.18276 : un instrument qui
change entre la référence et la suite crée à lui seul une destination commune).
"""
from __future__ import annotations

import math
from typing import Sequence

import torch

from ..environnements.pilote_a import logits_derniere_position
from ..gardes import GardeArret


def jetons_des_valeurs(tok, valeurs: Sequence[int]) -> dict[int, int]:
    """valeur → identifiant du jeton unique qui l'écrit. Arrêt si une valeur tient sur plusieurs jetons, si deux valeurs
    partagent un jeton, ou si la liste est vide."""
    if not valeurs:
        raise GardeArret("aucune valeur admise")
    ids = {}
    for v in valeurs:
        e = tok.encode(str(v), add_special_tokens=False)
        if len(e) != 1:
            raise GardeArret(f"la valeur {v!r} ne tient pas en un seul jeton : {e}")
        ids[int(v)] = int(e[0])
    if len(set(ids.values())) != len(ids):
        raise GardeArret("deux valeurs partagent un même jeton")
    return ids


def esperance(logprobs: torch.Tensor, jetons: dict[int, int]) -> tuple[float, float]:
    """(espérance de la valeur renormalisée sur les jetons des valeurs, masse de ces jetons avant renormalisation)."""
    if logprobs.ndim != 1:
        raise GardeArret(f"log-probabilités de forme {tuple(logprobs.shape)} : un vecteur attendu")
    ids = torch.tensor(list(jetons.values()), dtype=torch.long)
    lp = logprobs[ids].to(torch.float64)
    if not torch.isfinite(lp).any():
        raise GardeArret("probabilité nulle sur toutes les valeurs admises")
    m = torch.logsumexp(lp, 0)
    p = torch.exp(lp - m)
    valeurs = torch.tensor(list(jetons.keys()), dtype=torch.float64)
    s, masse = float((p * valeurs).sum()), float(torch.exp(m))
    if not (math.isfinite(s) and 0.0 < masse <= 1.0 + 1e-5):      # log-probabilités en simple précision
        raise GardeArret(f"espérance {s} ou masse {masse} hors domaine")
    return s, min(masse, 1.0)


def contexte_impose(fmt, systeme: str, utilisateur: str, reponse_imposee: str) -> list[int]:
    """Ouverture du dialogue (gabarit du modèle) suivie de la réponse imposée, jetonisée sans jeton spécial."""
    ctx = list(fmt.ouverture(systeme, utilisateur))
    if reponse_imposee:
        ctx += fmt.tok.encode(reponse_imposee, add_special_tokens=False)
    return ctx


def scores_moniteur(modele, fmt, demandes: list[dict], jetons: dict[int, int], lot: int,
                    masse_min: float) -> list[dict]:
    """Un score par demande (clé, système, utilisateur, réponse imposée) : espérance, masse, anomalie si la masse est
    sous `masse_min`. Lots à remplissage à gauche, positions explicites : le score ne dépend pas de la composition du
    lot (testé)."""
    if lot < 1:
        raise GardeArret("taille de lot ≥ 1 attendue")
    if not (0.0 <= masse_min < 1.0):
        raise GardeArret(f"masse minimale {masse_min} hors de [0, 1)")
    cles = [d["cle"] for d in demandes]
    if len(set(cles)) != len(cles):
        raise GardeArret("clés de demande en double")
    pad = fmt.tok.pad_token_id if fmt.tok.pad_token_id is not None else min(fmt.fins)
    sorties = []
    for debut in range(0, len(demandes), lot):
        morceau = demandes[debut:debut + lot]
        contextes = [contexte_impose(fmt, d["systeme"], d["utilisateur"], d.get("reponse_imposee", ""))
                     for d in morceau]
        lp = logits_derniere_position(modele, contextes, pad)
        for d, ligne, ctx in zip(morceau, lp, contextes):
            s, masse = esperance(ligne, jetons)
            sorties.append({"cle": d["cle"], "score": s, "masse": masse, "anomalie": masse < masse_min,
                            "jetons_contexte": len(ctx)})
    return sorties
