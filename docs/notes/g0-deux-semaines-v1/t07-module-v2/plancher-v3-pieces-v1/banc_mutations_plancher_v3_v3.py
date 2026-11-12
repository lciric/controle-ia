"""Banc de mutations du plancher v3, v3 : au commit `0d0c5da4` (palier et réserves portés jusqu'à l'étape B), rejoue toutes les
mutations de la v1 et de la v2 (m10 comprise, équivalente attendue) et ajoute m37 (réserves du plancher des figées non recopiées
à l'étape B) ; même méthode (copies, `-o pythonpath=`, import tracé).

    python -I banc_mutations_plancher_v3_v3.py ARBRE SORTIE.json
"""
import importlib.util
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent


def charger(nom):
    spec = importlib.util.spec_from_file_location(nom, ICI / f"{nom}.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


v1 = charger("banc_mutations_plancher_v3_v1")
base = list(v1.MUTATIONS)
v2 = charger("banc_mutations_plancher_v3_v2")
v1.MUTATIONS = base + [m for m in v2.v1.MUTATIONS if m[0] != "m18"] + [
    ("m37", "réserves du plancher des figées non recopiées à l'étape B", v1.L4,
     "        reserves += reserves_plancher_figees(index)            # v4", "        reserves += []            # v4", [v1.T_LEC]),
]

if __name__ == "__main__":
    sys.exit(v1.main(Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()))
