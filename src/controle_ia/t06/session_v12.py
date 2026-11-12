"""Chaîne de session de T0.6, v12 (lanceur v13 ; contre-lecture CLE3T-01 de l'ordre E3 ter ; nom neuf, R12 : `session_v11.py` et les précédents restent tels quels).

Seule différence avec `session_v11.py` : **aucun identifiant de GO n'est écrit en dur**. La v11 n'acceptait que les deux lignes des épreuves E2, E3 (total 5 USD) et E3 bis
(total 8 USD, dépense antérieure ≥ 2,092 exigée), écrites en dur. Ici la ligne de GO d'une épreuve est **lue dans le registre** (`registres/go.md`) :
- `ligne_go_calcul(registre, go_id, jour)` : la ligne existe, est de type « calcul », accordée par Lazar, porte un plafond lisible (« N USD », commentaire entre
  parenthèses admis), n'est ni échue (accord ≤ jour ≤ échéance) ni révoquée, et toute seconde ligne au même identifiant est une extension conforme (R-389) :
  c'est `session_v3.verifier_go_v3` appelée avec le plafond **de la ligne elle-même** ; elle rend ce plafond ;
- `verifier_plafond_epreuve(plafond, anterieures, go_id, registre, jour)` : décimaux exacts, plafond > 0, dépense antérieure ≥ 0, et
  **plafond + dépense antérieure ≤ plafond de la ligne** (plus de borne à 8 USD, plus de marge de 0,1 USD propre aux lignes cumulées, plus de dépense antérieure
  minimale liée à une ligne précise : une ligne séparée a une dépense antérieure de 0).
Toute vérification manquée lève `GardeSession` ; en ligne de commande : code 1 et le motif sur la dernière ligne, jamais un repli (R5).
`instance_seule`, `identifiants_nommes` et les autres sous-commandes sont ceux de `session_v11` (import, aucune copie).

    python -I -m controle_ia.t06.session_v12 go-ligne REGISTRE_GO.md GO_ID [AAAA-MM-JJ]            (imprime « GO conforme (plafond P USD, accord → échéance) »)
    python -I -m controle_ia.t06.session_v12 plafond-ligne REGISTRE_GO.md GO_ID [AAAA-MM-JJ]       (imprime le seul plafond de la ligne, en USD, après les mêmes vérifications)
    python -I -m controle_ia.t06.session_v12 plafond PLAFOND DEPENSE_ANTERIEURE GO_ID REGISTRE_GO.md [AAAA-MM-JJ]
    autres sous-commandes : celles de `session_v11` (`seule`, puis `session_v10`, …).
"""
from __future__ import annotations

import sys
from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path

from . import session as s1
from . import session_v3 as s3
from . import session_v11 as s11
from .session import GardeSession

filtre_recherche, choisir_offre, corriger_prix = s11.filtre_recherche, s11.choisir_offre, s11.corriger_prix
instance_presente, absence_probable = s11.instance_presente, s11.absence_probable
identifiants_nommes, instance_seule = s11.identifiants_nommes, s11.instance_seule


def plafond_de_la_ligne(registre, go_id: str) -> float:
    """Plafond écrit à la (première) ligne du registre portant `go_id`, en USD (« N USD », commentaire entre parenthèses admis). Rien d'autre n'est vérifié ici."""
    if not s3.ID_GO.fullmatch(str(go_id)):
        raise GardeSession(f"identifiant de GO illisible : {go_id!r} (GO-AAAA-MM-JJ-NN attendu)")
    fichier = Path(registre)
    if not fichier.is_file():
        raise GardeSession(f"registre {registre} absent")
    for n, l in enumerate(fichier.read_text(encoding="utf-8").splitlines(), 1):
        if not s1.LIGNE_GO.match(l):
            continue
        c = s1._cellules(l)
        if len(c) != 8:
            raise GardeSession(f"ligne {n} : 8 colonnes attendues, {len(c)}")
        if c[0] == go_id:
            if c[2] != "calcul":                                  # la cause première d'abord : une ligne « décision » n'a pas de plafond lisible
                raise GardeSession(f"{go_id} : type {c[2]!r}, « calcul » attendu")
            p = s3._plafond_ligne(c[4])
            if p is None:
                raise GardeSession(f"{go_id} : plafond {c[4]!r} illisible (« N USD » attendu : pas une ligne de calcul plafonnée)")
            return p
    raise GardeSession(f"{go_id} absent du registre")


def ligne_go_calcul(registre, go_id: str, jour: date | None = None) -> dict:
    """Ligne de GO de calcul valide au jour donné, sans identifiant en dur : `session_v3.verifier_go_v3` au plafond lu sur la ligne elle-même
    (existence, type « calcul », accordée par Lazar, extensions conformes, accord ≤ jour ≤ échéance, non révoquée). Rend aussi `plafond_usd`."""
    return s3.verifier_go_v3(registre, go_id, plafond_de_la_ligne(registre, go_id), jour)


def verifier_plafond_epreuve(plafond, anterieures, go_id, registre, jour: date | None = None) -> str:
    """`session_v8.verifier_plafond_epreuve` dont le total est le plafond de la ligne `go_id` du registre, sans marge : plafond + dépense antérieure ≤ plafond de la ligne."""
    ligne = ligne_go_calcul(registre, go_id, jour)
    try:
        p, a = Decimal(str(plafond)), Decimal(str(anterieures))
    except InvalidOperation:
        raise GardeSession(f"plafond ({plafond!r}) ou dépense antérieure ({anterieures!r}) illisible") from None
    if not (p.is_finite() and a.is_finite()):
        raise GardeSession("plafond ou dépense antérieure non fini")
    if p <= 0 or a < 0:
        raise GardeSession(f"plafond {p} (> 0 exigé) ou dépense antérieure {a} (≥ 0 exigé)")
    limite = Decimal(repr(float(ligne["plafond_usd"])))
    if p + a > limite:
        raise GardeSession(f"plafond d'épreuve {p} + dépense antérieure {a} = {p + a} > {limite} (plafond de la ligne {go_id} du registre, {ligne['accorde']} → {ligne['echeance']})")
    return f"plafond d'épreuve {p} + dépense antérieure {a} = {p + a} ≤ {limite} (plafond de la ligne {go_id} du registre)"


def _jour(argv: list[str], n: int) -> date | None:
    return date.fromisoformat(argv[n]) if len(argv) > n else None


def main(argv: list[str]) -> int:
    try:
        if len(argv) in (3, 4) and argv[0] == "go-ligne":
            r = ligne_go_calcul(argv[1], argv[2], _jour(argv, 3))
            print(f"{r['go']} conforme (plafond {r['plafond_usd']:g} USD, {r['accorde']} → {r['echeance']})")
            return 0
        if len(argv) in (3, 4) and argv[0] == "plafond-ligne":
            r = ligne_go_calcul(argv[1], argv[2], _jour(argv, 3))
            print(f"{r['plafond_usd']:g}")
            return 0
        if len(argv) in (5, 6) and argv[0] == "plafond":
            print(verifier_plafond_epreuve(argv[1], argv[2], argv[3], argv[4], _jour(argv, 5)))
            return 0
    except (GardeSession, ValueError) as e:                       # ValueError : jour illisible ; jamais un repli
        print(str(e))
        return 1
    if argv and argv[0] in ("go-ligne", "plafond-ligne", "plafond"):
        print(f"usage : {argv[0]} : voir l'en-tête de session_v12 (nombre d'arguments)", file=sys.stderr)
        return 2
    return s11.main(argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
