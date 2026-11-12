"""Configuration de T0.6, v6 (chaîne v13, contre-lecture CLE3T-01 de l'ordre E3 ter ; nom neuf, R12 : `configuration_v5.py` reste tel quel).
Seule différence avec la v5 : **aucun identifiant de GO d'épreuve n'est écrit en dur**, et le plafond d'une épreuve n'est plus borné à 8 USD.
- `est_epreuve(config)` : vrai pour toute configuration dont `go_id` est un identifiant de GO lisible **autre que celui de la course** (`configuration.GO_ID`,
  GO-2026-11-02-28) ; la v5 ne reconnaissait que les deux lignes des épreuves E2, E3 et E3 bis, écrites en dur.
- `exiger_config_t06_v6(config, registre_go, jour=None)` : pour une épreuve, le plafond est un nombre fini strictement positif **au plus égal au plafond de la ligne
  `go_id` du registre des GO** (`session_v12.ligne_go_calcul` : ligne présente, type « calcul », accordée par Lazar, non échue au jour donné, non révoquée) ; le registre
  est **obligatoire** pour une épreuve (aucune validation sans lui : R5, pas de repli) ; le reste est validé comme une configuration de course (v4, v5).
  Pour une configuration de course, le registre n'est pas lu ici (validation v3 inchangée : GO-2026-11-02-28, 200 USD).
"""
from __future__ import annotations

import math
from datetime import date

from ..gardes import GardeArret
from ..sondes.familles_v2 import PAQUET_GELE
from .configuration import GO_ID as GO_COURSE
from .configuration_v3 import exiger_config_t06_v3
from .configuration_v4 import CLE_JETONS_REELS, jetons_reels_voulus  # noqa: F401  (réexporté)
from .session import GardeSession
from .session_v3 import ID_GO
from .session_v12 import ligne_go_calcul


def est_epreuve(config: dict) -> bool:
    """Vrai pour une configuration d'épreuve à blanc : `go_id` lisible (GO-AAAA-MM-JJ-NN) et différent du GO de la course ; aucune donnée décisive."""
    g = config.get("go_id")
    return isinstance(g, str) and bool(ID_GO.fullmatch(g)) and g != GO_COURSE


def exiger_config_t06_v6(config: dict, registre_go=None, jour: date | None = None) -> None:
    if CLE_JETONS_REELS not in config:
        raise GardeArret(f"configuration de T0.6 v6 incomplète : {[CLE_JETONS_REELS]} (C-V4-2 : booléen, aucune valeur implicite)")
    v = config[CLE_JETONS_REELS]
    if not isinstance(v, bool):
        raise GardeArret(f"{CLE_JETONS_REELS} : booléen attendu, pas {v!r}")
    reste = {k: x for k, x in config.items() if k != CLE_JETONS_REELS}
    if est_epreuve(config):
        p = config.get("plafond_usd")
        if isinstance(p, bool) or not isinstance(p, (int, float)) or not math.isfinite(p) or not p > 0:
            raise GardeArret(f"plafond {p!r} : nombre fini strictement positif attendu pour l'épreuve {config.get('go_id')}")
        if registre_go is None:
            raise GardeArret(f"épreuve {config.get('go_id')} : registre des GO exigé pour borner le plafond {p!r} par celui de la ligne (aucune validation sans lui)")
        try:
            ligne = ligne_go_calcul(registre_go, config["go_id"], jour)
        except GardeSession as e:
            raise GardeArret(f"épreuve {config.get('go_id')} : ligne de GO non conforme : {e}") from None
        if p > ligne["plafond_usd"]:
            raise GardeArret(f"plafond {p!r} > plafond {ligne['plafond_usd']:g} USD de la ligne {config['go_id']} du registre ({ligne['accorde']} → {ligne['echeance']})")
        from .configuration import PLAFOND_USD
        reste.update(go_id=GO_COURSE, plafond_usd=PLAFOND_USD)       # le reste est validé comme une configuration de course
    exiger_config_t06_v3(reste)
    if v and config.get("mahalanobis_calcul") == PAQUET_GELE:
        raise GardeArret(f"{CLE_JETONS_REELS} vrai sous le paquet gelé : aucun essai d'égalité n'est joué sous le paquet gelé (refus, pas d'ignorance silencieuse)")
