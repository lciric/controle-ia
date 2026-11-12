"""Configuration de T0.6, v4 (contre-lecture du lanceur v3, C-V4-2 ; nom neuf, R12 : les v2 et v3 restent telles quelles).
Par-dessus `configuration_v3.exiger_config_t06_v3`, une clé neuve :
- `egalite_jetons_reels` (booléen, aucune valeur implicite) : si vrai, l'essai d'égalité de Mahalanobis v2 au paquet gelé est
  joué **aussi** sur 256 jetons réels tirés des actions du sous-ensemble d'activations (`sondes/familles_v3`), en plus des 256
  jetons tirés autour de μ. Vrai n'a de sens que sous `mahalanobis_calcul = produit_matriciel_v2` (sous le paquet gelé aucun
  essai n'est joué) : vrai sous le paquet gelé est refusé, jamais ignoré en silence. Joué à E3 (carte), clé de la configuration réelle.

C-V4-3 (ordres des épreuves E2 et E3) : une configuration d'épreuve porte `go_id = GO-2026-11-06-01` et `plafond_usd` = 1,5 (E2)
ou 3,5 (E3) ; le reste de la configuration est validé comme une configuration de course, le GO et le plafond de la course
étant substitués à ceux de l'épreuve pour la validation du reste (aucune autre règle n'est relâchée). Une configuration de
course garde `go_id = GO-2026-11-02-28` et `plafond_usd = 200`.
"""
from __future__ import annotations

from ..gardes import GardeArret
from ..sondes.familles_v2 import PAQUET_GELE
from .configuration_v3 import CLES_T06_V3, exiger_config_t06_v3

GO_EPREUVE = "GO-2026-11-06-01"          # épreuves à blanc E2 et E3 (5 USD cumulés, aucune donnée décisive)
PLAFONDS_EPREUVE = (1.5, 3.5)            # E2, E3 (GO-2026-11-06-01 : cumul ≤ 5 USD)
CLE_JETONS_REELS = "egalite_jetons_reels"
CLES_T06_V4 = tuple(CLES_T06_V3) + (CLE_JETONS_REELS,)


def exiger_config_t06_v4(config: dict) -> None:
    if CLE_JETONS_REELS not in config:
        raise GardeArret(f"configuration de T0.6 v4 incomplète : {[CLE_JETONS_REELS]} (C-V4-2 : booléen, aucune valeur implicite)")
    v = config[CLE_JETONS_REELS]
    if not isinstance(v, bool):
        raise GardeArret(f"{CLE_JETONS_REELS} : booléen attendu, pas {v!r}")
    reste = {k: x for k, x in config.items() if k != CLE_JETONS_REELS}
    if config.get("go_id") == GO_EPREUVE:
        if config.get("plafond_usd") not in PLAFONDS_EPREUVE or isinstance(config.get("plafond_usd"), bool):
            raise GardeArret(f"plafond {config.get('plafond_usd')!r} : {PLAFONDS_EPREUVE} USD attendus pour {GO_EPREUVE} (E2 ≤ 1,5, E3 ≤ 3,5)")
        from .configuration import GO_ID, PLAFOND_USD
        reste.update(go_id=GO_ID, plafond_usd=PLAFOND_USD)       # le reste est validé comme une configuration de course
    exiger_config_t06_v3(reste)
    if v and config.get("mahalanobis_calcul") == PAQUET_GELE:
        raise GardeArret(f"{CLE_JETONS_REELS} vrai sous le paquet gelé : aucun essai d'égalité n'est joué sous le paquet gelé (refus, pas d'ignorance silencieuse)")


def est_epreuve(config: dict) -> bool:
    """Vrai pour une configuration d'épreuve à blanc (E2, E3) : aucune donnée décisive, GO-2026-11-06-01."""
    return config.get("go_id") == GO_EPREUVE


def jetons_reels_voulus(config: dict) -> bool:
    return bool(config[CLE_JETONS_REELS])
