"""Sonde de mémoire de la carte, non décisive (version 2 de la validation de T0.4).

Elle charge le modèle réel en double précision, comme la phase de logique de la version 2, puis lui impose la charge de
cette phase au pire cas : un lot de 8 contextes longs, remplis à gauche, 256 jetons décodés sans arrêt anticipé, avec
des crochets sur deux lignes ; puis la passe unique la plus longue. Elle ne mesure que la mémoire de la carte et les
durées. Elle ne calcule aucune équivalence, aucun écart, aucune lecture (R1) : les jetons sont tirés au hasard.

    python -m controle_ia.harnais.sonde_memoire --revision <révision citée> --sortie <fichier JSON>
"""
from __future__ import annotations

import argparse
import json
import sys
import time

import torch

from ..gardes import GardeArret
from .activations import Crochets, couches_par_defaut, passe_unique
from .episode import generer_lot
from .modeles import charger_modele, noyaux_attention_permis, regler_determinisme

LOT, LONGUEUR, NOUVEAUX, LONGUEUR_PASSE, PAS_REMPLISSAGE = 8, 1400, 256, 1700, 37
JETONS = (1000, 120000)                     # jetons ordinaires (les jetons spéciaux de Llama 3 sont au-delà de 128 000)


def _memoire() -> dict:
    if not torch.cuda.is_available():
        return {"pic_go": None, "alloue_go": None, "reserve_go": None}
    return {"pic_go": round(torch.cuda.max_memory_allocated() / 1e9, 3),
            "alloue_go": round(torch.cuda.memory_allocated() / 1e9, 3),
            "reserve_go": round(torch.cuda.memory_reserved() / 1e9, 3)}


def _remise_a_zero() -> None:
    if torch.cuda.is_available():
        torch.cuda.reset_peak_memory_stats()


def mesurer_charge(modele, pad_id: int, graine: int = 0, lot: int = LOT, longueur: int = LONGUEUR,
                   nouveaux: int = NOUVEAUX, longueur_passe: int = LONGUEUR_PASSE, noyau=None) -> dict:
    """Charge de la phase de logique au pire cas, sur un modèle déjà chargé : pics de mémoire et durées par étape."""
    import contextlib
    noyau = noyau or contextlib.nullcontext
    g = torch.Generator().manual_seed(int(graine))
    couches = couches_par_defaut(modele.config.num_hidden_layers)
    bornes = (min(JETONS[0], modele.config.vocab_size // 2), min(JETONS[1], modele.config.vocab_size))
    contextes = [torch.randint(*bornes, (max(1, longueur - PAS_REMPLISSAGE * r),), generator=g).tolist()
                 for r in range(lot)]
    etapes = {}
    _remise_a_zero()
    t0 = time.perf_counter()
    with noyau(), torch.no_grad(), Crochets(modele, couches, lignes=[1, min(6, lot - 1)]) as c:
        sortis, plan = generer_lot(modele, contextes, nouveaux, 1.0, list(range(lot)), set(), pad_id)
        c.vider_lot()
    etapes["generation"] = {**_memoire(), "duree_s": round(time.perf_counter() - t0, 3),
                            "longueur_remplie": plan["longueur_remplie"], "passes_decodage": plan["passes_decodage"],
                            "jetons_generes": sum(len(x) for x in sortis)}
    _remise_a_zero()
    t0 = time.perf_counter()
    with noyau():
        passe_unique(modele, torch.randint(*bornes, (longueur_passe,), generator=g).tolist(), couches)
    etapes["passe_unique"] = {**_memoire(), "duree_s": round(time.perf_counter() - t0, 3), "jetons": longueur_passe}
    return etapes


def sonder(revision: str) -> dict:
    """Sur la carte : réglages, chargement en double précision, puis charge de la phase de logique."""
    from .validation_reelle import CONFIG_REELLE, noyau
    if not torch.cuda.is_available():
        raise GardeArret("sonde de mémoire : processeur graphique indisponible")
    reglages = regler_determinisme(CONFIG_REELLE["fils"], "cuda")
    total = torch.cuda.get_device_properties(0).total_memory
    _remise_a_zero()
    t0 = time.perf_counter()
    modele, tok = charger_modele(CONFIG_REELLE["modele"], revision, "float64", "cuda", CONFIG_REELLE["attention"])
    sortie = {"objet": "sonde de mémoire (non décisive) : chargement en double précision et charge de la phase de logique "
                       "au pire cas ; ni équivalence, ni écart, ni lecture",
              "revision": revision, "reglages": reglages, "carte_totale_gio": round(total / 2 ** 30, 2),
              "etapes": {"chargement": {**_memoire(), "duree_s": round(time.perf_counter() - t0, 3)}},
              "charge": {"lot": LOT, "longueur_max": LONGUEUR, "nouveaux": NOUVEAUX, "longueur_passe": LONGUEUR_PASSE}}
    with noyau("math"):
        sortie["noyaux_permis"] = noyaux_attention_permis()
    pad = tok.pad_token_id if tok.pad_token_id is not None else 128001
    try:
        sortie["etapes"].update(mesurer_charge(modele, pad, noyau=lambda: noyau("math")))
        sortie["issue"] = "tient"
    except torch.cuda.OutOfMemoryError as e:
        sortie["issue"] = "mémoire de la carte insuffisante"
        sortie["erreur"] = str(e).splitlines()[0][:300]
        sortie["etapes"]["au_moment_de_l_erreur"] = _memoire()
    pics = [e["pic_go"] for e in sortie["etapes"].values() if e.get("pic_go") is not None]
    sortie["pic_max_go"] = max(pics) if pics else None
    sortie["marge_go"] = None if not pics else round(total / 1e9 - max(pics), 3)
    return sortie


def main(argv=None) -> int:
    a = argparse.ArgumentParser()
    a.add_argument("--revision", required=True)
    a.add_argument("--sortie", required=True)
    args = a.parse_args(argv)
    try:
        sortie = sonder(args.revision)
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        return 1
    with open(args.sortie, "x", encoding="utf-8") as f:            # R12 : jamais d'écrasement
        json.dump(sortie, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps({k: sortie[k] for k in ("issue", "pic_max_go", "marge_go", "carte_totale_gio")}, ensure_ascii=False))
    return 0 if sortie["issue"] == "tient" else 2


if __name__ == "__main__":
    sys.exit(main())
