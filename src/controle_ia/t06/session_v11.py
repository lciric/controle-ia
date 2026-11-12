"""Chaîne de session de T0.6, v11 (lanceur v11 ; contre-lecture de la v11, R-1746 ; nom neuf, R12 : `session_v10.py` et les précédents restent tels quels).

Deux différences avec `session_v10.py` :
1. **Un identifiant différent de celui demandé n'est jamais une absence établie.** `instance_seule` refuse comme NON CONCLUANT une réponse de `show instance <ID> --raw` qui nomme d'autres
   instances et pas celle-ci : `{"id": 456}`, `{"instances": {"id": 456}}`, `{"instances": [{"id": 456}]}`, `[{"id": 456}]` pour l'identifiant 123 (en v9 et v10 : « absence établie », donc `ARRET mort`
   après deux relevés). L'absence reste établie par (a) une liste d'inventaire NON vide sans l'instance, à deux relevés (autre sous-commande, inchangée) et (b) un 404 exact avec un message exact
   (`_INTROUVABLE`, voulu en v9) ; `{"instances": null}` seul est une absence probable, non concluante (v10).
2. **Le total du GO des épreuves est lié au GO.** Le plafond d'une épreuve est borné par le reste du GO : 5 USD pour `GO-2026-11-06-01`, **8 USD pour `GO-2026-11-07-08`** (3 USD de plus), sans variable d'environnement ;
   pour `GO-2026-11-07-08` la dépense antérieure des autres épreuves doit être **au moins 2,092 USD** (E2 0,627 + E3 1,465, relevées) : une dépense antérieure absente ou moindre est refusée, jamais acceptée à 0.

    python -I -m controle_ia.t06.session_v11 seule REPONSE.json ID           (code 0 répond, 2 non concluant, 4 introuvable établi par un 404 exact)
    python -I -m controle_ia.t06.session_v11 plafond PLAFOND DEPENSE_ANTERIEURE GO_ID   (GO_ID : GO-2026-11-06-01 ou GO-2026-11-07-08)
    autres sous-commandes : celles de `session_v10`.
"""
from __future__ import annotations

import json
import sys
from decimal import Decimal, InvalidOperation

from . import session_v10 as s10
from .session import GardeSession

GO_EPREUVE = "GO-2026-11-06-01"
GO_EPREUVE_BIS = "GO-2026-11-07-08"
TOTAL_PAR_GO = {GO_EPREUVE: "5", GO_EPREUVE_BIS: "8"}
PLAFOND_REGISTRE_PAR_GO = {GO_EPREUVE: 5, GO_EPREUVE_BIS: 3}          # plafond écrit à la ligne du registre (E3 bis : les 3 USD de plus)
DEPENSE_ANTERIEURE_MIN_BIS = Decimal("2.092")

filtre_recherche, choisir_offre, corriger_prix = s10.filtre_recherche, s10.choisir_offre, s10.corriger_prix
instance_presente, absence_probable = s10.instance_presente, s10.absence_probable


def verifier_plafond_epreuve(plafond, anterieures, go_id) -> str:
    """`session_v10.verifier_plafond_epreuve` au total du GO donné (5 ou 8) ; pour `GO-2026-11-07-08`, dépense antérieure ≥ 2,092 exigée."""
    if go_id not in TOTAL_PAR_GO:
        raise GardeSession(f"GO {go_id!r} refusé : {sorted(TOTAL_PAR_GO)} seulement")
    if go_id == GO_EPREUVE_BIS:
        try:
            a = Decimal(str(anterieures))
        except InvalidOperation:
            raise GardeSession(f"dépense antérieure {anterieures!r} illisible") from None
        if not a.is_finite() or a < DEPENSE_ANTERIEURE_MIN_BIS:
            raise GardeSession(f"{go_id} : dépense antérieure {anterieures!r} < {DEPENSE_ANTERIEURE_MIN_BIS} USD (E2 0,627 + E3 1,465 déjà dépensés) : jamais acceptée plus bas")
    return s10.verifier_plafond_epreuve(plafond, anterieures, TOTAL_PAR_GO[go_id])


def identifiants_nommes(v) -> list[str]:
    """Identifiants d'instance nommés par une réponse JSON de `show instance` : `{"id": …}`, `{"instances": objet ou liste}`, liste d'objets."""
    if isinstance(v, dict):
        if "id" in v:
            return [str(v["id"])]
        if "instances" in v:
            return identifiants_nommes(v["instances"])
        return []
    if isinstance(v, list):
        return [i for x in v for i in identifiants_nommes(x)]
    return []


def instance_seule(texte: str, ident: str) -> bool:
    """Vrai : l'instance répond. Faux : ABSENCE établie (404 exact). GardeSession : tout le reste, y compris une réponse qui ne nomme que d'autres instances."""
    try:
        v = json.loads(texte.strip())
    except ValueError:
        v = None
    if v is not None:
        noms = [n for n in identifiants_nommes(v) if n not in ("None", "")]
        if noms and str(ident) not in noms:
            raise GardeSession(f"la réponse nomme l'instance {','.join(sorted(set(noms)))} et non {ident} : non concluante (jamais une absence établie)")
    return s10.instance_seule(texte, ident)


def main(argv: list[str]) -> int:
    if len(argv) == 4 and argv[0] == "plafond":
        try:
            print(verifier_plafond_epreuve(argv[1], argv[2], argv[3]))
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
    return s10.main(argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
