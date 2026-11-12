"""Constat neuf n° 2 (adaptation 4 de la contre-lecture de la course v2) : 45 pas déclarés à E3 bis, 4 entrées par adaptateur
au journal (clés « epoque », « perte »). Les adaptateurs ont-ils fait 45 pas d'optimiseur ?

Usage (Python 3.11 du programme, avec torch) :
    PYTHONPATH=<arbre>/src python3.11 -I -B verifier_pas_distillation_v1.py <arbre>

Joue `distiller_transcriptions` (le code exact de l'arbre) sur un petit modèle de langue jouet à adaptateurs, avec la
configuration de distillation d'E3 bis (3 époques, lot 1, pas 1e-4, norme 1,0) et 15 transcriptions (3 tâches × 5 épisodes,
plan (b)), en comptant les appels à `AdamW.step` ; puis la même chose avec 14 transcriptions (une exclue). N'écrit rien.
Imprime : pas déclarés (formule du lanceur), pas comptés, longueur et clés du journal.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import torch
from torch import nn

racine = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(racine / "src"))

from controle_ia.organismes import lora as lo  # noqa: E402
from controle_ia.t06 import distillation_transcription as dt  # noqa: E402
from controle_ia.t06.configuration_v2 import pas_attendus_avant_dependance, pas_de_distillation_declares  # noqa: E402
from controle_ia.organismes.distillation import IGNORE  # noqa: E402


class Sortie:
    def __init__(self, loss, logits):
        self.loss, self.logits = loss, logits


class Jouet(nn.Module):
    """Modèle de langue minuscule : plongement, une couche linéaire (cible des adaptateurs), tête."""

    def __init__(self, V=11, d=8):
        super().__init__()
        self.emb = nn.Embedding(V, d)
        self.q_proj = nn.Linear(d, d)
        self.tete = nn.Linear(d, V)

    def forward(self, input_ids, attention_mask=None, labels=None):
        h = self.q_proj(self.emb(input_ids))
        logits = self.tete(h)
        perte = None
        if labels is not None:
            perte = nn.functional.cross_entropy(logits[:, :-1].reshape(-1, logits.shape[-1]), labels[:, 1:].reshape(-1), ignore_index=IGNORE)
        return Sortie(perte, logits)


def jouer(n_transcriptions: int) -> dict:
    torch.manual_seed(0)
    m = Jouet()
    for p in m.parameters():
        p.requires_grad_(False)
    noms = lo.injecter(m, 2, 4.0, 7, ("q_proj",))
    lo.fixer_dose(m, 1.0)
    exemples = []
    for k in range(n_transcriptions):
        ids = [(3 * k + j) % 11 for j in range(6)]
        etiq = [IGNORE, IGNORE] + ids[2:]
        exemples.append((ids, etiq))
    compte = {"step": 0}
    vrai_step = torch.optim.AdamW.step

    def step_compte(self, *a, **k):
        compte["step"] += 1
        return vrai_step(self, *a, **k)

    torch.optim.AdamW.step = step_compte
    try:
        journal = dt.distiller_transcriptions(m, exemples, 0, 3, 1e-4, 1, 123, 1.0)
    finally:
        torch.optim.AdamW.step = vrai_step
    config = {"distillation": {"epoques": 3, "lot": 1, "unite_du_lot": "transcription", "pas_declares": 45}, "T": 4,
              "episodes_par_tache_distillation": 5, "decisions": {"DT-1": "b"}}
    return {"modules_injectes": len(noms), "transcriptions": n_transcriptions, "pas_comptes_adamw": compte["step"],
            "pas_attendus_avant_depense": pas_attendus_avant_dependance(config, 3),
            "pas_effectifs_formule": pas_de_distillation_declares(config, n_transcriptions, n_transcriptions * 4),
            "entrees_du_journal": len(journal), "cles_d_une_entree": sorted(journal[0]), "epoques_journalisees": [e["epoque"] for e in journal]}


print(json.dumps({"15_transcriptions": jouer(15), "14_transcriptions_une_exclue": jouer(14)}, ensure_ascii=False, indent=1))
