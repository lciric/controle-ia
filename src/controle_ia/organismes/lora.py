"""Adaptateurs de rang faible (LoRA), implémentation autonome, pour les organismes de la famille (ii) (T0.6).

Chaque couche linéaire visée devient y = W x + (dose · α / r) · B(A x) : W est gelée ; A (r × entrée) est tirée par une
graine dérivée du manifeste (R9) ; B (sortie × r) part de zéro, donc l'adaptateur neuf ne change rien. La **dose** est
l'échelle de l'adaptateur entier, dans [0, 1] (P-009, option (a) : dose de (ii) par l'échelle de l'adaptateur) :
- à dose 0, la sortie est **exactement** celle du modèle de base, au bit près (le terme d'adaptation n'est pas
  calculé) : c'est le témoin α = 0 ;
- pour une seule couche, l'écart à la base est linéaire en la dose (testé) ; pour le modèle entier, il ne l'est pas.
Aucune dépendance nouvelle (pas de bibliothèque d'adaptateurs) : le code tient dans ce module et se teste sur le modèle
jouet.
"""
from __future__ import annotations

import hashlib
import math

import numpy as np
import torch
from torch import nn

from ..gardes import GardeArret

CIBLES_DEFAUT = ("q_proj", "k_proj", "v_proj", "o_proj")


class LineaireLoRA(nn.Module):
    def __init__(self, base: nn.Linear, rang: int, alpha: float, graine: int):
        super().__init__()
        if rang < 1:
            raise GardeArret(f"rang {rang} : au moins 1")
        self.base = base
        for p in self.base.parameters():
            p.requires_grad_(False)
        g = torch.Generator().manual_seed(int(graine))
        dtype, appareil = base.weight.dtype, base.weight.device
        a = torch.randn(rang, base.in_features, generator=g, dtype=torch.float64) / math.sqrt(base.in_features)
        self.A = nn.Parameter(a.to(dtype=dtype, device=appareil))
        self.B = nn.Parameter(torch.zeros(base.out_features, rang, dtype=dtype, device=appareil))
        self.echelle = float(alpha) / float(rang)
        self.dose = 1.0

    def forward(self, x):
        y = self.base(x)
        if self.dose == 0.0:
            return y
        return y + (self.dose * self.echelle) * ((x @ self.A.T) @ self.B.T)


def modules_lora(modele) -> dict[str, LineaireLoRA]:
    return {n: m for n, m in modele.named_modules() if isinstance(m, LineaireLoRA)}


def injecter(modele, rang: int, alpha: float, graine: int, cibles=CIBLES_DEFAUT) -> list[str]:
    """Remplace chaque couche linéaire dont le nom finit par une des cibles ; rend les noms remplacés (ordre stable).
    Graines des matrices A dérivées par couche (`SeedSequence`, R9). Arrêt si rien n'est visé ou si le modèle porte
    déjà des adaptateurs."""
    if modules_lora(modele):
        raise GardeArret("le modèle porte déjà des adaptateurs : une seule injection")
    visees = [(n, m) for n, m in modele.named_modules()
              if isinstance(m, nn.Linear) and n.rsplit(".", 1)[-1] in tuple(cibles)]
    if not visees:
        raise GardeArret(f"aucune couche linéaire visée par {tuple(cibles)}")
    graines = np.random.SeedSequence(int(graine)).spawn(len(visees))
    for (nom, lin), ss in zip(visees, graines):
        parent_nom, _, enfant = nom.rpartition(".")
        parent = modele.get_submodule(parent_nom) if parent_nom else modele
        setattr(parent, enfant, LineaireLoRA(lin, rang, alpha, int(ss.generate_state(1)[0])))
    for n, p in modele.named_parameters():
        if not (n.endswith(".A") or n.endswith(".B")):
            p.requires_grad_(False)
    return [n for n, _ in visees]


def fixer_dose(modele, dose: float) -> None:
    if not (0.0 <= float(dose) <= 1.0):
        raise GardeArret(f"dose {dose} hors de [0, 1]")
    mods = modules_lora(modele)
    if not mods:
        raise GardeArret("aucun adaptateur dans le modèle")
    for m in mods.values():
        m.dose = float(dose)


def parametres_entrainables(modele) -> list[nn.Parameter]:
    params = [p for p in modele.parameters() if p.requires_grad]
    noms = [n for n, p in modele.named_parameters() if p.requires_grad]
    if not params or not all(n.endswith(".A") or n.endswith(".B") for n in noms):
        raise GardeArret(f"paramètres entraînables inattendus : {noms[:5]}")
    return params


def etat_lora(modele) -> dict[str, torch.Tensor]:
    return {f"{n}.{k}": getattr(m, k).detach().to("cpu").clone() for n, m in modules_lora(modele).items() for k in ("A", "B")}


def charger_etat(modele, etat: dict[str, torch.Tensor]) -> None:
    attendu = etat_lora(modele)
    if set(attendu) != set(etat):
        raise GardeArret("adaptateurs : clés différentes entre l'état et le modèle")
    for cle, t in etat.items():
        if attendu[cle].shape != t.shape:
            raise GardeArret(f"adaptateur {cle} : forme {tuple(t.shape)} ≠ {tuple(attendu[cle].shape)}")
    mods = modules_lora(modele)
    with torch.no_grad():
        for cle, t in etat.items():
            nom, _, k = cle.rpartition(".")
            getattr(mods[nom], k).copy_(t.to(getattr(mods[nom], k).dtype))


def empreinte_base(modele) -> str:
    """sha256 des poids gelés seulement (hors adaptateurs) : prouve que la distillation n'a pas touché la base."""
    h = hashlib.sha256()
    for nom, p in sorted(modele.state_dict().items()):
        if nom.endswith(".A") or nom.endswith(".B"):
            continue
        nom_base = nom.replace(".base.", ".")
        t = p.detach().to("cpu").contiguous()
        h.update(nom_base.encode("utf-8"))
        h.update((t.view(torch.int16) if t.dtype == torch.bfloat16 else t).numpy().tobytes())
    return h.hexdigest()


def empreinte_adaptateurs(modele) -> str:
    h = hashlib.sha256()
    for cle, t in sorted(etat_lora(modele).items()):
        h.update(cle.encode("utf-8"))
        h.update((t.view(torch.int16) if t.dtype == torch.bfloat16 else t).contiguous().numpy().tobytes())
    return h.hexdigest()
