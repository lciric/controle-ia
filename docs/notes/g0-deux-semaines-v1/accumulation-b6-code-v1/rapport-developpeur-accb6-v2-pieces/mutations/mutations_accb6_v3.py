"""Mutations du banc, v3 (R-2275) : celles de la v2, plus la garde de non-relance (`garde_v1.py`)."""
from mutations_accb6_v2 import MUTATIONS as V2

MUTATIONS = list(V2) + [
    ("R01", "garde_v1.py", "    if arrets:                                    # garde de non-relance (C1-12, C1-13 ; R-2275)",
     "    if False:", "garde de non-relance (arret-accb6.json d'un run quelconque)"),
    ("R02", "garde_v1.py", '(racine / "diag").glob(f"*/{FICHIER_ARRET}")', '(racine / "diag").glob(f"*/{FICHIER_LECTURE}.x")',
     "garde de non-relance : fichier cherché"),
]
