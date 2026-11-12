"""Chaîne de session de T0.6, v10 (lanceur v11, E3 du 7 novembre ; nom neuf, R12 : `session_v9.py` et les précédents restent tels quels).

Seule différence avec `session_v9.py` : le texte RÉEL que Vast rend pour une instance détruite, relevé en E3 (instance 59623267, fille 6, 22:27:24Z) :
`vastai show instance <ID> --raw` rend, en code 0, `{"instances": null}` (trois lignes). Ce texte, seul, est une **absence probable** et non une absence établie :
`instance_seule` le refuse comme NON CONCLUANT, avec un message qui nomme la cause. L'absence n'est établie que par une liste d'inventaire NON vide qui ne contient pas
l'identifiant, à deux relevés (inchangé dans le lanceur : code de retour 1 de `presente`). `{"id": null}`, un texte 500 et un 404 sans message exact restent non concluants
(`session_v9`).

    python -I -m controle_ia.t06.session_v10 seule REPONSE.json ID    (code 0 répond, 2 non concluant, 4 introuvable établi par le seul texte)
    autres sous-commandes : celles de `session_v9`.
"""
from __future__ import annotations

import json
import re
import sys

from . import session_v9 as s9
from .session import GardeSession

filtre_recherche, choisir_offre, corriger_prix = s9.filtre_recherche, s9.choisir_offre, s9.corriger_prix
instance_presente = s9.instance_presente


TOTAUX_GO_EPREUVES = ("5", "8")      # GO-2026-11-06-01 (5 USD) ; avec GO-2026-11-07-08 (E3 bis, 3 USD de plus) : 8 USD pour E2, E3 et E3 bis cumulées


def verifier_plafond_epreuve(plafond, anterieures, total=None) -> str:
    """`session_v8.verifier_plafond_epreuve` (plafond + dépense réelle des autres épreuves ≤ total − 0,1) avec le total du GO donné : « 5 » par défaut, « 8 » seulement pour E3 bis
    (GO-2026-11-07-08, 3 USD de plus sur GO-2026-11-06-01). Tout autre total est refusé."""
    from decimal import Decimal
    t = "5" if total is None else str(total)
    if t not in TOTAUX_GO_EPREUVES:
        raise GardeSession(f"total du GO des épreuves {t!r} refusé : {TOTAUX_GO_EPREUVES} seulement")
    from . import session_v8 as s8
    ancien = s8.GO_EPREUVES_USD
    s8.GO_EPREUVES_USD = t
    try:
        return s8.verifier_plafond_epreuve(plafond, anterieures)
    finally:
        s8.GO_EPREUVES_USD = ancien


def absence_probable(texte: str) -> bool:
    """Vrai pour le texte réel d'une instance détruite : un objet dont la seule clé est `instances` et vaut `null`."""
    try:
        v = json.loads(texte.strip())
    except ValueError:
        return False
    return isinstance(v, dict) and list(v) == ["instances"] and v["instances"] is None


_IDENT_DU_MESSAGE = re.compile(r"(?i)\binstance\s+(\d+)\b")


def instance_seule(texte: str, ident: str) -> bool:
    """`session_v9.instance_seule` plus deux refus : le texte réel `{"instances": null}` (absence probable) et un message « … instance <N> … not found » dont N n'est PAS l'identifiant demandé
    (contre-lecture R-1731, essai 11) : il parle d'une autre instance, il ne conclut pas pour celle-ci."""
    if absence_probable(texte):
        raise GardeSession('réponse {"instances": null} : absence probable, établie seulement par une liste d\'inventaire non vide sans l\'instance, à deux relevés : non concluante')
    for n in _IDENT_DU_MESSAGE.findall(texte):
        if n != str(ident):
            raise GardeSession(f"message d'introuvable pour l'instance {n}, pas pour {ident} : non concluant")
    return s9.instance_seule(texte, ident)


def main(argv: list[str]) -> int:
    if len(argv) in (3, 4) and argv[0] == "plafond":
        try:
            print(verifier_plafond_epreuve(argv[1], argv[2], argv[3] if len(argv) == 4 else None))
        except GardeSession as e:
            print(str(e))
            return 1
        return 0
    if len(argv) == 3 and argv[0] == "seule":
        try:
            texte = open(argv[1], encoding="utf-8", errors="replace").read()
            absente = not instance_seule(texte, argv[2])
        except OSError as e:
            print(f"réponse de show instance illisible ({e.__class__.__name__})")
            return 2
        except GardeSession as e:
            print(str(e))
            return 2
        if absente:
            print(f"instance {argv[2]} INTROUVABLE")
            return 4
        print(f"instance {argv[2]} répond")
        return 0
    return s9.main(argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
