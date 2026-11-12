"""Configuration de T0.6, v3 (contre-lecture neuve du lanceur v2, C-V3-4 ; nom neuf, R12 : la v2 reste telle quelle).
Par-dessus `configuration_v2.exiger_config_t06_v2` (clés exactes, C04), une clé neuve :
- `mahalanobis_calcul` : « paquet_gele » (la notation de Mahalanobis du paquet gelé `sondes/familles.py`, ≈ 20 ms par jeton)
  ou « produit_matriciel_v2 » (`sondes/familles_v2.py`, même formule par produit matriciel, égalité au paquet gelé vérifiée
  par le lanceur avant chaque usage). **Défaut : « paquet_gele »** tant que Lazar n'a pas tranché (nœud de la contre-lecture,
  point 8) ; la configuration réelle garde ce défaut. La v2 n'est permise qu'aux couples descriptifs : si la sonde décisive
  est de la famille Mahalanobis, le paquet gelé est exigé (un essai d'égalité en échec ne doit jamais arrêter l'ensemble).
Chaque valeur est une valeur de configuration : un changement de Lazar n'est pas du code.
"""
from __future__ import annotations

from ..gardes import GardeArret
from ..sondes.familles_v2 import CALCULS_MAHALANOBIS, PAQUET_GELE
from .configuration_v2 import CLES_T06_V2, exiger_config_t06_v2

CLE_MAHALANOBIS = "mahalanobis_calcul"
CLES_T06_V3 = tuple(CLES_T06_V2) + (CLE_MAHALANOBIS,)
DEFAUT_MAHALANOBIS = PAQUET_GELE


def exiger_config_t06_v3(config: dict) -> None:
    if CLE_MAHALANOBIS not in config:
        raise GardeArret(f"configuration de T0.6 v3 incomplète : {[CLE_MAHALANOBIS]} (C-V3-4 : {CALCULS_MAHALANOBIS}, défaut "
                         f"{DEFAUT_MAHALANOBIS!r} ; aucune valeur implicite)")
    calcul = config[CLE_MAHALANOBIS]
    if calcul not in CALCULS_MAHALANOBIS:
        raise GardeArret(f"{CLE_MAHALANOBIS} : {CALCULS_MAHALANOBIS} attendu, pas {calcul!r}")
    if calcul != PAQUET_GELE and isinstance(config.get("sonde"), dict) and config["sonde"].get("famille") == "mahalanobis":
        raise GardeArret(f"{CLE_MAHALANOBIS} : la sonde décisive est de la famille Mahalanobis : le paquet gelé est exigé "
                         "(la v2 est permise aux couples descriptifs seulement, C-V3-4 ; la v1 fixe d'ailleurs la famille décisive)")
    exiger_config_t06_v2({k: v for k, v in config.items() if k != CLE_MAHALANOBIS})


def calcul_mahalanobis(config: dict) -> str:
    return str(config[CLE_MAHALANOBIS])
