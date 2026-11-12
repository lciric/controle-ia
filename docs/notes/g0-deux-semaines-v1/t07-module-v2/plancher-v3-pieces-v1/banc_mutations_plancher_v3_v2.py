"""Banc de mutations du plancher v3, v2 : rejoue la survivante m18 de la v1 (réglages de torch non rétablis) après l'essai ajouté,
et les mutations neuves des gardes d'entrée ajoutées (m33 à m36) ; même méthode que la v1 (copies, `-o pythonpath=`, import
tracé). m10 (v1) : équivalente (somme le long du même axe en mémoire : `.T.sum(axis=0)` d'une vue transposée = somme sur
l'axe contigu), non rejouée.

    python -I banc_mutations_plancher_v3_v2.py ARBRE SORTIE.json
"""
import importlib.util
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("banc_v1", ICI / "banc_mutations_plancher_v3_v1.py")
v1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v1)
RX, T_RX = v1.RX, v1.T_RX
v1.MUTATIONS = [m for m in v1.MUTATIONS if m[0] == "m18"] + [
    ("m33", "lignes des enjeux non contrôlées", RX, '    if [x["ligne"] for x in tir] != list(r["donnees"]["lignes_enjeux"]):', "    if False:", [T_RX]),
    ("m34", "nombre d'exemples non contrôlé", RX, '        if len(ex) != int(r["donnees"][f"exemples_{concept}"]):', "        if False:", [T_RX]),
    ("m35", "mode de P3 non contrôlé", RX, '    if p3["config"].get("mode") != mode:', "    if False:", [T_RX]),
    ("m36", "témoin absent : la principale prise pour témoin", RX, '        raise GardeArret(f"témoin {nom} absent du fichier léger de P3")',
     "        return s", [T_RX]),
]

if __name__ == "__main__":
    sys.exit(v1.main(Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()))
