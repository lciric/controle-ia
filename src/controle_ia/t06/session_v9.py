"""Chaîne de session de T0.6, v9 (lanceur v10, contre-lecture Opus de la v9 : « Essais R5 à ajouter » 3 ; nom neuf, R12 : `session_v8.py` et les précédents restent tels quels).

Seule différence avec `session_v8.py` : `instance_seule` (réponse de `vastai show instance <ID> --raw`) devient plus étroite.
(1) Le texte d'introuvable est reconnu **sur un « 404 » exact et un message exact** : « 404 », éventuellement précédé de « error » / « http » et suivi de « : », puis (« instance <id> »)
    « not found » / « no such instance » / « does not exist ». Le « not found » seul, sans « 404 », n'est plus une absence ; « error: 500 not found » n'en a jamais été une.
(2) Un objet qui porte une clé `id` **sans identifiant lisible** (`{"id": null}`, `{"id": ""}`, un identifiant qui n'est ni un entier ni un texte non vide) est non concluant, pas une absence
    (la v8 le comparait à l'identifiant demandé et concluait à l'absence). Même règle pour les éléments d'une liste.
Le texte exact que Vast rend pour une instance détruite sera ajouté ici quand la fille 6 l'aura relevé à E3 ; d'ici là, seules ces formes à « 404 » établissent l'absence.

    python -I -m controle_ia.t06.session_v9 seule FICHIER ID        (codes : 0 répond, 4 introuvable, 2 non concluant)
    autres sous-commandes : celles de `session_v8`.
"""
from __future__ import annotations

import json
import re
import sys

from . import session_v2 as s2
from . import session_v8 as s8
from .session import GardeSession

CUDA_MAX_GOOD_MIN = s8.CUDA_MAX_GOOD_MIN
FIABILITE_MIN_OFFRE = s8.FIABILITE_MIN_OFFRE
INET_DOWN_MIN_MBPS = s8.INET_DOWN_MIN_MBPS
filtre_recherche = s8.filtre_recherche          # inchangés : ré-exportés pour que `session_v9` soit un point d'entrée complet
choisir_offre = s8.choisir_offre
corriger_prix = s8.corriger_prix
verifier_plafond_epreuve = s8.verifier_plafond_epreuve
instance_presente = s8.s7.instance_presente

_INTROUVABLE = re.compile(r"^(error[: ]*)?(http )?404[: ]*(instance( \d+)? )?(not found|no such instance|does not exist)$")


def _dit_introuvable(texte: str) -> bool:
    t = re.sub(r"[\s.\"']+$", "", texte.strip().lower())
    return bool(_INTROUVABLE.match(t))


_MESSAGE = re.compile(r"^(instance( \d+)? )?(not found|no such instance|does not exist)$")


def _message_introuvable(texte: str) -> bool:
    """Message d'une erreur JSON dont le statut vaut déjà exactement 404 : le message seul doit être exact."""
    t = re.sub(r"[\s.\"']+$", "", texte.strip().lower())
    return bool(_MESSAGE.match(t))


def _id_lisible(v) -> bool:
    return (isinstance(v, int) and not isinstance(v, bool)) or (isinstance(v, str) and v.strip() != "")


def instance_seule(texte: str, ident: str) -> bool:
    """Vrai : l'instance répond. Faux : ABSENCE établie. GardeSession : tout le reste (non concluant)."""
    brut = texte.strip()
    if not brut:
        raise GardeSession("réponse de show instance vide")
    try:
        v = json.loads(brut)
    except ValueError:
        if _dit_introuvable(brut):
            return False
        raise GardeSession("réponse de show instance illisible")
    if isinstance(v, dict) and "instances" in v:
        v = v["instances"]
    if isinstance(v, dict):
        if "id" in v:
            if not _id_lisible(v["id"]):
                raise GardeSession("réponse de show instance : identifiant illisible (null, vide ou d'un autre type) : non concluante")
            return str(v["id"]) == str(ident)
        if s8._statut_404(v) and any(_message_introuvable(str(v.get(k, ""))) for k in ("error", "msg", "message", "detail")):
            return False
        raise GardeSession("réponse de show instance sans id (objet d'erreur ou inconnu) : non concluante")
    if isinstance(v, list) and v and all(isinstance(i, dict) and "id" in i for i in v):
        if not all(_id_lisible(i["id"]) for i in v):
            raise GardeSession("réponse de show instance : identifiant illisible dans la liste : non concluante")
        return any(str(i["id"]) == str(ident) for i in v)
    raise GardeSession("réponse de show instance vide ou illisible : non concluante")


def main(argv: list[str]) -> int:
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
    return s8.main(argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
