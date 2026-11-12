"""Repli de l'étape A de T0.7 : recalcul des activations (brouillon 19, `07039ed2…`, plan, point 8, « Repli de l'étape A » ;
CLT7-08 ; R11), v1 — **la garde d'équivalence seulement**.

Ce que le texte demande au repli, quand le disque de l'instance de 7b n'est plus disponible : charger le modèle, injecter les
adaptateurs de 7b (`organismes.lora`), contrôler l'identité à dose 0 (`t06.identite.controle_identite`), rejouer chaque
épisode en forçage depuis les identifiants générés, aux trois couches, puis **la garde d'équivalence** : sur chaque action du
sous-ensemble poussé, écart entre activations recalculées (passées en demi-précision) et sous-ensemble, **statistique et
tolérance de la configuration de 7b** (`config.statistique_equivalence`, `config.tolerance_equivalence` du manifeste, jamais
écrites en dur), par couche ; échec → relance une fois sur la même carte que la course ; second échec → arrêt, nœud.

Ce module écrit la garde (`garde_equivalence`) avec les fonctions du harnais (`harnais.activations.ecart_equivalence`,
`exiger_equivalence`, `exiger_controle_negatif`, appelées telles quelles) et la lecture de la statistique et de la tolérance
dans le manifeste de 7b (`parametres_equivalence`) ; elle est éprouvée sur des activations factices (cas sain à l'identique,
artefact décalé d'un jeton → échec, comme le contrôle négatif de T0.6). **Le rejeu des épisodes n'est pas écrit** (écart
déclaré au rapport) : il demande le modèle, les adaptateurs et la reconstruction des conversations de l'environnement par le
code de la chaîne de T0.6 (`t06.identite`, `harnais.episode`), qui n'est pas sur cette branche ; la commande
`repli-recalcul` refuse (code 2, rien écrit), comme avant.
"""
from __future__ import annotations

import numpy as np

from ..gardes import GardeArret
from ..harnais.activations import ecart_equivalence, exiger_controle_negatif, exiger_equivalence

STATISTIQUES = {"max": None, "q99": 0.99}


def parametres_equivalence(manifeste_7b: dict) -> tuple[str, float, float]:
    """`config.statistique_equivalence`, `config.tolerance_equivalence` et `config.fraction_min_controle_negatif` du manifeste
    de 7b (jamais en dur)."""
    try:
        stat = manifeste_7b["config"]["statistique_equivalence"]
        tol = manifeste_7b["config"]["tolerance_equivalence"]
        frac = manifeste_7b["config"]["fraction_min_controle_negatif"]
    except (KeyError, TypeError):
        raise GardeArret("manifeste de 7b : config.statistique_equivalence, tolerance_equivalence ou fraction_min_controle_negatif "
                         "absente") from None
    if isinstance(frac, bool) or not isinstance(frac, (int, float)) or not 0.0 < float(frac) <= 1.0:
        raise GardeArret(f"fraction minimale du contrôle négatif {frac!r} : nombre dans ]0, 1] attendu")
    if stat not in STATISTIQUES:
        raise GardeArret(f"statistique d'équivalence {stat!r} inconnue ({list(STATISTIQUES)})")
    if isinstance(tol, bool) or not isinstance(tol, (int, float)) or not 0.0 < float(tol) < 1.0:
        raise GardeArret(f"tolérance d'équivalence {tol!r} : nombre dans ]0, 1[ attendu")
    return stat, float(tol), float(frac)


def garde_equivalence(recalculees: dict, sous_ensemble: dict, couche: int, statistique: str, tolerance: float,
                      fraction_min: float) -> dict:
    """Pour chaque action du sous-ensemble poussé (clé → activations en demi-précision à `couche`), écart avec les activations
    recalculées (clé → {couche : tableau}), passées en demi-précision ; garde d'équivalence à la tolérance de 7b ; contrôle
    négatif décalé d'un jeton, qui doit dépasser la tolérance sur au moins `fraction_min` des actions (règle du contrôle négatif
    de T0.6 : une garde aveugle au décalage ne garde rien). Toute faute →
    `GardeArret` (R11 : arrêt avant toute lecture)."""
    if not sous_ensemble:
        raise GardeArret("repli : sous-ensemble poussé vide : garde d'équivalence impossible")
    q = STATISTIQUES[statistique]
    ecarts, decales = {}, {}
    for cle, attendu in sous_ensemble.items():
        if cle not in recalculees or int(couche) not in recalculees[cle]:
            raise GardeArret(f"repli : action {cle} du sous-ensemble non recalculée à la couche {couche}")
        g = np.asarray(recalculees[cle][int(couche)]).astype(np.float16).astype(np.float32)
        p = np.asarray(attendu).astype(np.float32)
        if g.shape != p.shape:
            raise GardeArret(f"repli : action {cle} : forme recalculée {g.shape} ≠ sous-ensemble {p.shape}")
        e = ecart_equivalence({int(couche): g}, {int(couche): p}, 0, q)[int(couche)]
        exiger_equivalence({int(couche): e}, float(tolerance), f"repli, action {cle}", statistique)
        ecarts[cle] = e
        if g.shape[0] > 1:
            decales[cle] = ecart_equivalence({int(couche): g}, {int(couche): p}, 1, q)[int(couche)]
    if not decales:
        raise GardeArret("repli : aucune action de deux jetons ou plus : contrôle négatif impossible")
    vus = sum(1 for e in decales.values() if e > float(tolerance))
    if vus < float(fraction_min) * len(decales):
        exiger_controle_negatif({int(couche): min(decales.values())}, float(tolerance),
                                f"repli, contrôle négatif ({vus} actions sur {len(decales)} au-dessus de la tolérance)")
    return {"controle_negatif": {"au_dessus": vus, "actions": len(decales), "fraction_min": float(fraction_min)},
            "actions": len(ecarts), "couche": int(couche), "statistique": statistique, "tolerance": float(tolerance),
            "ecart_max": max(ecarts.values()), "decale_min": min(decales.values())}


__all__ = ["parametres_equivalence", "garde_equivalence", "STATISTIQUES"]
