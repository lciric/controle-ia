"""Flux résiduel : crochets sur les couches du décodeur, passe avant unique, agrégation par action.

Définition : l'activation de la couche ℓ est la sortie du bloc de décodeur ℓ (indice à partir de 0),
c'est-à-dire le flux résiduel après ℓ + 1 blocs, avant la normalisation finale. La même définition sert
pendant la génération et pendant la passe avant unique, ce qui rend la garde d'équivalence exacte.
"""
from __future__ import annotations

import numpy as np
import torch

from ..gardes import GardeArret

FRACTIONS_COUCHES = (0.25, 0.5, 0.75)        # couches précoce, médiane et tardive (proposition, T0.7)
# Vecteur d'action : maximum par coordonnée sur les jetons de l'empan, seulement. Sur les jetons, le brief (T0.7)
# n'admet que le maximum ou l'attention ; l'attention est apprise par une sonde (voir `sondes`).
# Jamais la moyenne ni la médiane (interdit) ; le dernier jeton n'est pas admis non plus (R-030).
AGREGATIONS = ("max",)


def couches_par_defaut(n_couches: int) -> list[int]:
    if n_couches < 1:
        raise GardeArret(f"{n_couches} couche(s) : au moins une attendue")
    return sorted({min(n_couches - 1, max(0, int(round(f * n_couches)) - 1)) for f in FRACTIONS_COUCHES})


def blocs_decodeur(modele):
    try:
        return modele.model.layers
    except AttributeError:
        raise GardeArret(f"architecture {type(modele).__name__} : blocs de décodeur introuvables") from None


def type_de_capture(dtype: torch.dtype) -> torch.dtype:
    """Type des activations capturées : la double précision reste double ; tout autre type (simple, demi) passe en
    simple précision, conversion exacte depuis bfloat16 ou float16."""
    return torch.float64 if dtype == torch.float64 else torch.float32


class Crochets:
    """Capture, à chaque appel du modèle, la sortie des couches choisies.

    Sans `lignes` : lot de taille 1 exigé, morceaux (positions, largeur). Avec `lignes` : lot de toute
    taille, seules les lignes indiquées sont gardées, morceaux (lignes, positions, largeur) ; la
    reconstruction par ligne (remplissage, pas actifs) revient à l'appelant (`vider_lot`)."""

    def __init__(self, modele, couches, lignes=None):
        blocs = blocs_decodeur(modele)
        self.couches = sorted(set(int(c) for c in couches))
        if not self.couches or self.couches[0] < 0 or self.couches[-1] >= len(blocs):
            raise GardeArret(f"couches {couches} hors de [0, {len(blocs)}[")
        self.blocs = blocs
        self.lignes = None if lignes is None else [int(r) for r in lignes]
        self.morceaux: dict[int, list[np.ndarray]] = {c: [] for c in self.couches}
        self.poignees = []

    def _crochet(self, couche):
        def f(module, entrees, sortie):
            h = sortie[0] if isinstance(sortie, tuple) else sortie
            if h.dim() != 3:
                raise GardeArret(f"sortie de couche de forme {tuple(h.shape)} : (lot, positions, largeur) attendu")
            if self.lignes is None:
                if h.shape[0] != 1:
                    raise GardeArret(f"sortie de couche de forme {tuple(h.shape)} : lot de taille 1 attendu")
                self.morceaux[couche].append(h[0].detach().to("cpu", type_de_capture(h.dtype)).numpy().copy())
            else:
                if max(self.lignes) >= h.shape[0]:
                    raise GardeArret(f"lignes {self.lignes} hors d'un lot de {h.shape[0]}")
                self.morceaux[couche].append(h[self.lignes].detach().to("cpu", type_de_capture(h.dtype)).numpy().copy())
        return f

    def __enter__(self):
        self.poignees = [self.blocs[c].register_forward_hook(self._crochet(c)) for c in self.couches]
        return self

    def __exit__(self, *exc):
        for p in self.poignees:
            p.remove()
        self.poignees = []
        return False

    def vider(self) -> dict[int, np.ndarray]:
        """Lot de taille 1 : activations concaténées le long de la séquence, par couche ; remet à zéro."""
        if self.lignes is not None:
            raise GardeArret("capture par lignes : utiliser vider_lot")
        sortie = {c: (np.concatenate(v, axis=0) if v else np.zeros((0, 0), np.float32)) for c, v in self.morceaux.items()}
        self.morceaux = {c: [] for c in self.couches}
        return sortie

    def vider_lot(self) -> dict[int, list[np.ndarray]]:
        """Capture par lignes : morceaux bruts (lignes, positions, largeur), dans l'ordre des appels."""
        if self.lignes is None:
            raise GardeArret("capture sans lignes : utiliser vider")
        sortie = self.morceaux
        self.morceaux = {c: [] for c in self.couches}
        return sortie


def passe_unique(modele, ids: list[int], couches) -> dict[int, np.ndarray]:
    """Une passe avant sur la transcription complète (sans cache) : activations (jetons, largeur) par couche."""
    if not ids:
        raise GardeArret("passe avant sur une transcription vide")
    appareil = next(modele.parameters()).device
    with torch.no_grad(), Crochets(modele, couches) as c:
        modele(torch.tensor([ids], device=appareil), use_cache=False, logits_to_keep=1)
        acts = c.vider()
    for couche, a in acts.items():
        if a.shape[0] != len(ids):
            raise GardeArret(f"couche {couche} : {a.shape[0]} positions capturées pour {len(ids)} jetons")
    return acts


def agreger(acts: np.ndarray, debut: int, fin: int, methode: str) -> np.ndarray:
    """Vecteur d'une action à partir de ses jetons [début, fin[ : maximum par coordonnée."""
    if methode not in AGREGATIONS:
        raise GardeArret(f"agrégation {methode!r} refusée pour un vecteur d'action : seul le maximum par coordonnée "
                         "est permis ; l'attention passe par une sonde apprise (brief, T0.7) ; "
                         "jamais la moyenne ni la médiane sur les jetons (interdit)")
    if not (0 <= debut < fin <= acts.shape[0]):
        raise GardeArret(f"empan d'action [{debut}, {fin}[ invalide pour {acts.shape[0]} positions")
    return acts[debut:fin].max(axis=0)


def ecarts_par_jeton(g: np.ndarray, p: np.ndarray) -> np.ndarray:
    """Écart relatif par jeton, ‖g_n − p_n‖ / ‖p_n‖ (norme euclidienne sur la largeur), en double précision.

    Mesure par jeton : les activations massives de quelques positions (premier jeton, séparateurs)
    n'écrasent pas l'échelle des autres, contrairement à un écart rapporté au maximum global."""
    g64, p64 = g.astype(np.float64), p.astype(np.float64)
    return np.linalg.norm(g64 - p64, axis=1) / np.maximum(np.linalg.norm(p64, axis=1), 1e-30)


def ecart_equivalence(acts_generation: dict[int, np.ndarray], acts_passe: dict[int, np.ndarray],
                      decalage: int = 0, quantile: float | None = None) -> dict[int, float]:
    """Par couche, maximum sur les jetons capturés pendant la génération de l'écart relatif par jeton avec la
    passe unique ; avec `quantile` (version 3, production en demi-précision), ce quantile au lieu du maximum.
    `decalage` = k > 0 compare la génération au jeton n − k de la passe : contrôle négatif, qui doit dépasser la
    tolérance (une garde aveugle au décalage d'un jeton ne garde rien). Un écart illisible (NaN) rend un NaN."""
    ecarts = {}
    for couche, g in acts_generation.items():
        p = acts_passe[couche]
        if g.shape[0] <= decalage or g.shape[0] > p.shape[0] or g.shape[1] != p.shape[1]:
            raise GardeArret(f"couche {couche} : formes incompatibles {g.shape} et {p.shape} (décalage {decalage})")
        e = ecarts_par_jeton(g[decalage:], p[: g.shape[0] - decalage])
        ecarts[couche] = float(e.max() if quantile is None else np.quantile(e, quantile))
    return ecarts


def ecart_decale_zone_generee(acts_generation: dict[int, np.ndarray], acts_passe: dict[int, np.ndarray],
                              longueur_contexte: int, tolerance: float) -> dict | None:
    """Contrôle négatif restreint à la zone où génération et passe unique suivent des chemins différents : les
    positions décodées. On compare g_n à p_{n−1} pour n ≥ longueur_contexte + 1, les deux positions dans la zone
    générée (la première position décodée, comparée au dernier jeton du contexte, est exclue : elle passerait
    d'elle-même). Par couche, la grandeur que lirait la garde de la phase sous ce décalage d'un jeton :
    - « max » : maximum de l'écart décalé de la zone générée ; le maximum croît avec les positions lues, si bien que
      le voir au-dessus de la tolérance suffit à dire que la garde, qui lit toute l'action, le verrait aussi ;
    - « q99 » (version 3, contre-lecture 1, X-2) : 99e centile sur les positions que lit la garde de la production,
      le contexte non décalé suivi de la zone générée décalée. Le 99e centile ne croît pas avec les positions lues :
      un décalage confiné à une zone générée de moins de 1 % des positions de l'action lui échappe, et ce contrôle
      négatif doit le montrer ;
    - le nombre de positions décalées au-dessus de la tolérance, et leur nombre.
    None si l'action a moins de deux positions décodées capturées (trop courte : comptée à part)."""
    sortie = {}
    for couche, g in acts_generation.items():
        p = acts_passe[couche]
        debut = longueur_contexte + 1
        if g.shape[0] > p.shape[0] or g.shape[1] != p.shape[1]:
            raise GardeArret(f"couche {couche} : formes incompatibles {g.shape} et {p.shape}")
        if g.shape[0] <= debut:
            return None
        e = ecarts_par_jeton(g[debut:], p[debut - 1: g.shape[0] - 1])
        e_action = np.concatenate([ecarts_par_jeton(g[:longueur_contexte], p[:longueur_contexte]), e])
        sortie[couche] = {"max": float(e.max()), "q99": float(np.quantile(e_action, 0.99)),
                          "au_dessus": int(np.sum(e > tolerance)), "positions": int(e.size)}
    return sortie


def profil_ecarts(acts_generation: dict[int, np.ndarray], acts_passe: dict[int, np.ndarray],
                  longueur_contexte: int | None = None) -> dict[int, dict]:
    """Description de la distribution des écarts par jeton (quantiles 0,5, 0,99, maximum, écarts nuls), par couche ;
    avec `longueur_contexte`, séparément pour le contexte et pour la zone générée (positions décodées)."""
    def decrire(e):
        if e.size == 0:
            return {"jetons": 0}
        return {"jetons": int(e.size), "q50": float(np.quantile(e, 0.5)), "q99": float(np.quantile(e, 0.99)),
                "max": float(e.max()), "nuls": int(np.sum(e == 0.0))}
    profil = {}
    for couche, g in acts_generation.items():
        e = ecarts_par_jeton(g, acts_passe[couche][: g.shape[0]])
        profil[couche] = decrire(e)
        if longueur_contexte is not None:
            profil[couche]["contexte"] = decrire(e[:longueur_contexte])
            profil[couche]["generee"] = decrire(e[longueur_contexte:])
    return profil


def sonde_de_comparaison(acts_generation: dict[int, np.ndarray], acts_passe: dict[int, np.ndarray]) -> dict:
    """Audit de symétrie (R4) : les deux côtés sont des tableaux distincts, et la mesure voit une perturbation d'une
    unité au dernier rang (un ulp) sur une seule valeur de la passe unique."""
    distincts = all(not np.shares_memory(g, acts_passe[c]) for c, g in acts_generation.items())
    couche = min(acts_generation)
    g = acts_generation[couche]
    p = acts_passe[couche][: g.shape[0]].copy()
    n = g.shape[0] - 1
    p[n, 0] = np.nextafter(p[n, 0], p.dtype.type(np.inf), dtype=p.dtype)        # un ulp dans le type capturé
    avant = ecarts_par_jeton(g[n:], acts_passe[couche][n:n + 1])[0]
    apres = ecarts_par_jeton(g[n:], p[n:n + 1])[0]
    return {"tableaux_distincts": bool(distincts), "ulp_vu": bool(apres != avant)}


def exiger_equivalence(ecarts: dict[int, float], tolerance: float, quoi: str, statistique: str = "max") -> None:
    """Garde : la génération et la passe unique donnent les mêmes activations, à la tolérance consignée près ;
    `statistique` nomme la grandeur lue par couche (maximum, ou 99e centile en production, version 3)."""
    fautes = {c: e for c, e in ecarts.items() if not e <= tolerance}
    if fautes:
        nom = "écarts" if statistique == "max" else f"écarts, {statistique}"
        raise GardeArret(f"{quoi} : activations de génération ≠ passe unique ({nom} {fautes} > {tolerance})")


def exiger_controle_negatif(ecarts_decales: dict[int, float], tolerance: float, quoi: str) -> None:
    """Garde : décalée d'un jeton, la comparaison doit dépasser la tolérance à chaque couche ; sinon la garde
    d'équivalence ne verrait pas un désalignement entre transcription et activations."""
    aveugles = {c: e for c, e in ecarts_decales.items() if not e > tolerance}
    if aveugles:
        raise GardeArret(f"{quoi} : garde d'équivalence aveugle au décalage d'un jeton (écarts {aveugles} ≤ {tolerance})")
