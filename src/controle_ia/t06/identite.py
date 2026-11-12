"""Contrôle d'identité à dose 0 et état d'adaptateur d'une phase (T0.6, métrique et liste d'arrêt).

- `logits_de_controle` : logits d'un contexte fixe (même plan de lot : une ligne, sans remplissage), en mémoire centrale ;
- `controle_identite` : avant l'injection, logits de la base ; après le chargement de chaque adaptateur entraîné, à dose 0,
  égalité au bit près exigée (un adaptateur neuf, B = 0, rend la base à toute dose : le contrôle n'est discriminant
  qu'avec un adaptateur entraîné) ; artefact du même contrôle (R5), sur la même carte : à dose 1, logits différents de
  la base exigés ;
- `etat_adaptateurs` : dose lue sur chaque module et empreinte des adaptateurs chargés ;
- `exiger_etat_de_phase` : l'état lu égale celui de la phase, sinon arrêt (un lot mêlé est impossible par construction, la
  dose étant portée par les modules ; artefact : adaptateur changé au milieu d'une phase).
"""
from __future__ import annotations

import torch

from ..gardes import GardeArret
from ..organismes.lora import charger_etat, empreinte_adaptateurs, fixer_dose, modules_lora


def logits_de_controle(modele, ids: list[int]) -> torch.Tensor:
    if not ids:
        raise GardeArret("contexte de contrôle vide")
    appareil = next(modele.parameters()).device
    with torch.no_grad():
        return modele(input_ids=torch.tensor([list(ids)], device=appareil), use_cache=False).logits.detach().to("cpu").clone()


def etat_adaptateurs(modele) -> dict:
    mods = modules_lora(modele)
    if not mods:
        raise GardeArret("aucun adaptateur dans le modèle")
    doses = {n: float(m.dose) for n, m in mods.items()}
    uniques = sorted(set(doses.values()))
    return {"doses": doses, "dose": uniques[0] if len(uniques) == 1 else None, "modules": len(mods),
            "empreinte": empreinte_adaptateurs(modele)}


def exiger_etat_de_phase(modele, dose: float, empreinte: str, quoi: str) -> dict:
    e = etat_adaptateurs(modele)
    if e["dose"] is None or abs(e["dose"] - float(dose)) > 0.0:
        raise GardeArret(f"{quoi} : dose lue sur les modules {sorted(set(e['doses'].values()))} ≠ dose de la phase {dose}")
    if e["empreinte"] != empreinte:
        raise GardeArret(f"{quoi} : adaptateurs chargés ({e['empreinte'][:12]}…) ≠ ceux de la phase ({empreinte[:12]}…)")
    return e


def controle_identite(modele, ids: list[int], logits_base: torch.Tensor, etats: dict[str, dict]) -> dict:
    """Pour chaque adaptateur entraîné (nom → état) : chargé à dose 0, logits égaux à la base au bit près ; chargé à
    dose 1, logits différents (artefact R5). Laisse le modèle à dose 0, le dernier adaptateur chargé."""
    if not etats:
        raise GardeArret("contrôle d'identité : aucun adaptateur entraîné")
    sortie = {}
    for nom, etat in etats.items():
        charger_etat(modele, etat)
        fixer_dose(modele, 0.0)
        l0 = logits_de_controle(modele, ids)
        if l0.shape != logits_base.shape or not torch.equal(l0, logits_base):
            raise GardeArret(f"contrôle d'identité à dose 0 en échec ({nom}) : logits différents de la base au bit près")
        fixer_dose(modele, 1.0)
        l1 = logits_de_controle(modele, ids)
        fixer_dose(modele, 0.0)
        if l1.shape == logits_base.shape and torch.equal(l1, logits_base):
            raise GardeArret(f"artefact du contrôle d'identité non vu ({nom}) : logits égaux à la base à dose 1")
        ecart = float((l1.float() - logits_base.float()).abs().max())
        sortie[nom] = {"dose_0_identique": True, "dose_1_differente": True, "ecart_max_dose_1": ecart,
                       "empreinte": empreinte_adaptateurs(modele)}
    return sortie
