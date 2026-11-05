"""Distillation d'un organisme de la famille (ii) (T0.6) : réglage fin des adaptateurs de rang faible sur des paires
(contexte, action cible), la perte ne portant que sur les jetons de l'action.

Les paires viennent des épisodes de l'organisme instruit (famille (i)), rejoués **sans** sa consigne cachée ni ses
indications privées (c'est l'appelant qui reconstruit ces contextes) : l'adaptateur doit porter le comportement sans
qu'aucun texte ne le dise (2509.21344 : une sonde peut lire le texte qui dit le comportement). Entraînement
déterministe : ordre des paires tiré par la graine, lots remplis à droite, perte moyenne par jeton cible.
"""
from __future__ import annotations

import torch

from ..gardes import GardeArret
from .lora import parametres_entrainables

IGNORE = -100


def _lot(paires, pad_id: int):
    L = max(len(c) + len(a) for c, a in paires)
    ids = torch.full((len(paires), L), int(pad_id), dtype=torch.long)
    masque = torch.zeros((len(paires), L), dtype=torch.long)
    etiquettes = torch.full((len(paires), L), IGNORE, dtype=torch.long)
    for r, (c, a) in enumerate(paires):
        n = len(c) + len(a)
        ids[r, :n] = torch.tensor(list(c) + list(a), dtype=torch.long)
        masque[r, :n] = 1
        etiquettes[r, len(c):n] = torch.tensor(list(a), dtype=torch.long)
    return ids, masque, etiquettes


def perte_moyenne(modele, paires, pad_id: int, lot: int) -> float:
    """Perte d'entropie croisée moyenne par jeton d'action, sans gradient."""
    total, jetons = 0.0, 0
    appareil = next(modele.parameters()).device
    with torch.no_grad():
        for d in range(0, len(paires), lot):
            ids, masque, etiq = _lot(paires[d:d + lot], pad_id)
            logits = modele(input_ids=ids.to(appareil), attention_mask=masque.to(appareil)).logits[:, :-1]
            cible = etiq[:, 1:].to(appareil)
            pertes = torch.nn.functional.cross_entropy(logits.reshape(-1, logits.shape[-1]).float(), cible.reshape(-1),
                                                       ignore_index=IGNORE, reduction="sum")
            total += float(pertes)
            jetons += int((cible != IGNORE).sum())
    return total / jetons


def distiller(modele, paires: list[tuple[list[int], list[int]]], pad_id: int, epoques: int, pas: float, lot: int,
              graine: int, norme_max: float = 1.0) -> list[dict]:
    """Entraîne les seuls adaptateurs ; rend le journal (perte moyenne par époque). Arrêt si une paire est vide, si
    un paramètre hors adaptateurs est entraînable, ou si la perte devient non finie."""
    if not paires:
        raise GardeArret("aucune paire de distillation")
    if any(len(c) == 0 or len(a) == 0 for c, a in paires):
        raise GardeArret("paire de distillation avec contexte ou action vide")
    if epoques < 1 or lot < 1 or not pas > 0:
        raise GardeArret("époques ≥ 1, lot ≥ 1, pas > 0 attendus")
    params = parametres_entrainables(modele)
    opt = torch.optim.AdamW(params, lr=pas, weight_decay=0.0)
    g = torch.Generator().manual_seed(int(graine))
    appareil = next(modele.parameters()).device
    journal = [{"epoque": 0, "perte": perte_moyenne(modele, paires, pad_id, lot)}]
    modele.train()
    try:
        for e in range(1, epoques + 1):
            ordre = torch.randperm(len(paires), generator=g).tolist()
            for d in range(0, len(ordre), lot):
                ids, masque, etiq = _lot([paires[i] for i in ordre[d:d + lot]], pad_id)
                opt.zero_grad()
                sortie = modele(input_ids=ids.to(appareil), attention_mask=masque.to(appareil), labels=etiq.to(appareil))
                if not torch.isfinite(sortie.loss):
                    raise GardeArret(f"perte non finie à l'époque {e}")
                sortie.loss.backward()
                torch.nn.utils.clip_grad_norm_(params, norme_max)
                opt.step()
            journal.append({"epoque": e, "perte": perte_moyenne(modele, paires, pad_id, lot)})
    finally:
        modele.eval()
    return journal
