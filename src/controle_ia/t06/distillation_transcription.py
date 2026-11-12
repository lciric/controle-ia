"""Distillation par transcription entière (T0.6, plan d'analyse, point 3, « mode de distillation ») : une séquence par
épisode, la transcription honnête reconstruite de l'organisme instruit, la perte ne portant que sur les jetons de ses
actions (environ 6,6 fois moins de calcul que dix paires ; fonction neuve sous nom neuf, R12 ; `organismes.distillation`
reste tel quel et sert de repli, mode « paires »).

- `transcription_honnete` : rejeu d'un épisode instruit sans sa consigne cachée ni ses indications privées : l'environnement
  (a) honnête (sans `instructions_cachees` ni `indications_privees`), nourri du journal des propres actions de l'organisme
  instruit ; les identifiants des actions sont collés tels quels (jamais retokenisés) ; rend les identifiants et les empans ;
- `exemple_de_transcription` : étiquettes IGNORE hors des empans des actions ;
- `distiller_transcriptions` : même entraînement que `distiller` (AdamW, lots remplis à droite, norme bornée, graine), sur
  des exemples (identifiants, étiquettes) ;
- `exclure_mentions` : règle mécanique écrite au texte : les actions que `mesures_action` marque `mention_texte_prive`
  sortent des cibles (l'organisme apprendrait à citer une note absente) ; aucune autre sélection ;
- `adaptateurs_en_simple_precision` : A et B en float32 (un pas d'AdamW de 1·10⁻⁴ est du même ordre que l'écart entre
  deux valeurs représentables de A en bfloat16), la base restant au type du modèle ; le calcul de l'adaptation se fait en
  float32 et revient au type de la base ; à dose 0 le terme n'est pas calculé (la base au bit près reste vraie) ;
- `etat_initial` : état neuf (A tirée par la graine de l'adaptateur, dérivée par couche comme `injecter`, B = 0), pour
  distiller un second adaptateur sur le même modèle injecté une seule fois.
"""
from __future__ import annotations

import types

import numpy as np
import torch
from torch import nn

from ..gardes import GardeArret
from ..organismes.distillation import IGNORE
from ..organismes.lora import LineaireLoRA, modules_lora, parametres_entrainables
from ..premier_test_ia.conditions import mesures_action


def transcription_honnete(fmt, env_honnete, actions: list[list[int]]) -> tuple[list[int], list[tuple[int, int]]]:
    """Identifiants de la transcription honnête (environnement sans texte privé) autour des actions données, et empans
    [début, fin[ de chaque action. L'environnement doit être honnête (aucun texte privé) et avoir autant de pas que
    d'actions."""
    if getattr(env_honnete, "instructions_cachees", None) or getattr(env_honnete, "indications_privees", None):
        raise GardeArret("reconstruction du contexte honnête : l'environnement porte un texte privé")
    if not actions or len(actions) != env_honnete.T:
        raise GardeArret(f"{len(actions)} actions pour {env_honnete.T} pas")
    journal: list[tuple[int, int, str]] = []
    ids: list[int] = []
    empans = []
    debut = None
    for t, a in enumerate(actions):
        if not a:
            raise GardeArret(f"action vide au pas {t}")
        obs = env_honnete.observation(0, t, journal)
        if t == 0:
            debut = (env_honnete.consigne_privee(0), obs)
            ids = fmt.ouverture(*debut)
        else:
            ids = ids + fmt.tour(debut, obs)
        d = len(ids)
        ids = ids + list(a)
        empans.append((d, d + len(a)))
        ids = ids + fmt.cloture(debut, list(a))
        journal.append((0, t, fmt.tok.decode(list(a), skip_special_tokens=True)))
    return ids, empans


def exemple_de_transcription(ids: list[int], empans: list[tuple[int, int]], garder=None) -> tuple[list[int], list[int]]:
    """Étiquettes de la transcription : les jetons des empans gardés, IGNORE ailleurs. `garder` : indices des actions
    gardées (None : toutes). Arrêt si un empan est vide, hors de la transcription, chevauche un autre, ou si rien n'est
    gardé."""
    etiq = [IGNORE] * len(ids)
    gardes = list(range(len(empans))) if garder is None else [int(k) for k in garder]
    if not gardes:
        raise GardeArret("transcription sans aucune action gardée")
    fin_precedente = -1
    for k, (d, f) in enumerate(empans):
        if not (0 <= d < f <= len(ids)) or d < fin_precedente:
            raise GardeArret(f"empan {k} [{d}, {f}[ invalide ou chevauchant pour {len(ids)} jetons")
        fin_precedente = f
        if k in gardes:
            etiq[d:f] = ids[d:f]
    return list(ids), etiq


def _lot(exemples, pad_id: int):
    L = max(len(i) for i, _ in exemples)
    ids = torch.full((len(exemples), L), int(pad_id), dtype=torch.long)
    masque = torch.zeros((len(exemples), L), dtype=torch.long)
    etiq = torch.full((len(exemples), L), IGNORE, dtype=torch.long)
    for r, (i, e) in enumerate(exemples):
        ids[r, :len(i)] = torch.tensor(i, dtype=torch.long)
        masque[r, :len(i)] = 1
        etiq[r, :len(e)] = torch.tensor(e, dtype=torch.long)
    return ids, masque, etiq


def perte_moyenne_transcriptions(modele, exemples, pad_id: int, lot: int) -> float:
    total, jetons = 0.0, 0
    appareil = next(modele.parameters()).device
    with torch.no_grad():
        for d in range(0, len(exemples), lot):
            ids, masque, etiq = _lot(exemples[d:d + lot], pad_id)
            logits = modele(input_ids=ids.to(appareil), attention_mask=masque.to(appareil)).logits[:, :-1]
            cible = etiq[:, 1:].to(appareil)
            total += float(torch.nn.functional.cross_entropy(logits.reshape(-1, logits.shape[-1]).float(),
                                                             cible.reshape(-1), ignore_index=IGNORE, reduction="sum"))
            jetons += int((cible != IGNORE).sum())
    if jetons == 0:
        raise GardeArret("aucun jeton cible dans les exemples")
    return total / jetons


def distiller_transcriptions(modele, exemples: list[tuple[list[int], list[int]]], pad_id: int, epoques: int, pas: float,
                             lot: int, graine: int, norme_max: float = 1.0, progres=None) -> list[dict]:
    """Entraîne les seuls adaptateurs sur des transcriptions entières ; rend le journal (perte moyenne par jeton cible,
    par époque). Arrêt : aucun exemple, exemple sans cible, étiquettes de longueur différente, paramètre hors adaptateurs
    entraînable, perte non finie."""
    if not exemples:
        raise GardeArret("aucune transcription de distillation")
    for k, (i, e) in enumerate(exemples):
        if not i or len(i) != len(e):
            raise GardeArret(f"transcription {k} : identifiants et étiquettes de longueurs différentes, ou vides")
        if all(x == IGNORE for x in e[1:]):
            raise GardeArret(f"transcription {k} : aucun jeton cible")
    if epoques < 1 or lot < 1 or not pas > 0:
        raise GardeArret("époques ≥ 1, lot ≥ 1, pas > 0 attendus")
    params = parametres_entrainables(modele)
    opt = torch.optim.AdamW(params, lr=pas, weight_decay=0.0)
    g = torch.Generator().manual_seed(int(graine))
    appareil = next(modele.parameters()).device
    journal = [{"epoque": 0, "perte": perte_moyenne_transcriptions(modele, exemples, pad_id, lot)}]
    modele.train()
    try:
        for e in range(1, epoques + 1):
            ordre = torch.randperm(len(exemples), generator=g).tolist()
            for d in range(0, len(ordre), lot):
                ids, masque, etiq = _lot([exemples[i] for i in ordre[d:d + lot]], pad_id)
                opt.zero_grad()
                sortie = modele(input_ids=ids.to(appareil), attention_mask=masque.to(appareil), labels=etiq.to(appareil))
                if not torch.isfinite(sortie.loss):
                    raise GardeArret(f"perte non finie à l'époque {e}")
                sortie.loss.backward()
                torch.nn.utils.clip_grad_norm_(params, norme_max)
                opt.step()
            journal.append({"epoque": e, "perte": perte_moyenne_transcriptions(modele, exemples, pad_id, lot)})
            if progres is not None:
                progres(e, journal[-1]["perte"])
    finally:
        modele.eval()
    return journal


def exclure_mentions(textes: list[str]) -> list[int]:
    """Indices des actions gardées : celles que `mesures_action` ne marque pas `mention_texte_prive`."""
    return [k for k, t in enumerate(textes) if not mesures_action(t)["mention_texte_prive"]]


def _forward_simple(self, x):
    y = self.base(x)
    if self.dose == 0.0:
        return y
    adaptation = (x.to(self.A.dtype) @ self.A.T) @ self.B.T
    return y + (self.dose * self.echelle) * adaptation.to(y.dtype)


def adaptateurs_en_simple_precision(modele) -> int:
    """A et B passent en float32 (attribut d'instance : la classe `LineaireLoRA` n'est pas touchée) ; rend le nombre de
    modules convertis. Garde : au moins un adaptateur."""
    mods = modules_lora(modele)
    if not mods:
        raise GardeArret("aucun adaptateur dans le modèle")
    for m in mods.values():
        m.A = nn.Parameter(m.A.detach().to(torch.float32))
        m.B = nn.Parameter(m.B.detach().to(torch.float32))
        m.forward = types.MethodType(_forward_simple, m)
    for n, p in modele.named_parameters():
        p.requires_grad_(n.endswith(".A") or n.endswith(".B"))
    return len(mods)


def etat_initial(modele, rang: int, alpha: float, graine: int) -> dict[str, torch.Tensor]:
    """État neuf d'un adaptateur (A tirée par graines dérivées par couche, dans l'ordre des modules, comme `injecter` ;
    B = 0), à charger par `charger_etat` sur un modèle déjà injecté (une seule injection par modèle)."""
    mods = modules_lora(modele)
    if not mods:
        raise GardeArret("aucun adaptateur dans le modèle")
    graines = np.random.SeedSequence(int(graine)).spawn(len(mods))
    etat = {}
    for (nom, m), ss in zip(mods.items(), graines):
        neuf = LineaireLoRA(m.base, rang, alpha, int(ss.generate_state(1)[0]))
        if neuf.A.shape != m.A.shape or neuf.B.shape != m.B.shape:
            raise GardeArret(f"adaptateur {nom} : rang {rang} ≠ rang injecté")
        etat[f"{nom}.A"] = neuf.A.detach().to("cpu", m.A.dtype).clone()
        etat[f"{nom}.B"] = torch.zeros_like(m.B, device="cpu")
    return etat


def etat_en(etat: dict[str, torch.Tensor], dtype: str) -> dict[str, torch.Tensor]:
    """Copie de l'état au type demandé (sauvegarde en demi-précision : ≈ 27 Mo pour un adaptateur de rang 16 du 8B)."""
    return {k: v.detach().to("cpu", getattr(torch, dtype)).clone() for k, v in etat.items()}
