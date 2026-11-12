"""Banc de mutations du plancher v3, v4 : les corrections de la contre-lecture (R-2305 : CLP3-01 à 03, notes 05, 07, 10), au
commit des corrections ; même méthode que la v1 (copies de `src/`, `-o pythonpath=`, import tracé, copie saine d'abord).

    python -I banc_mutations_plancher_v3_v4.py ARBRE SORTIE.json
"""
import importlib.util
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("banc_v1", ICI / "banc_mutations_plancher_v3_v1.py")
v1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v1)
RX, L4, PB, RT = v1.RX, v1.L4, v1.PB, v1.RT
T_RX, T_LEC = v1.T_RX, v1.T_LEC
v1.MUTATIONS = [
    ("c1", "carte_sonde revenu à 1e-2 (v7)", RX, '"carte_sonde": 1e-3,', '"carte_sonde": 1e-2,', [T_RX]),
    ("c2", "carte_directions revenu à 1e-1 (v7)", RX, '"carte_directions": 1e-2}', '"carte_directions": 1e-1}', [T_RX]),
    ("c3", "réserve « carte » d'avant (« présumé »)", RX, 'RESERVE_CARTE = ("écart au palier « carte », cause non établie :',
     'RESERVE_CARTE = ("non-déterminisme de la carte présumé ; cause non établie :', [T_RX]),
    ("c4", "MemoryError hors des fautes du bras", RX, "KeyError, MemoryError, TypeError", "KeyError, TypeError", [T_RX]),
    ("c5", "TypeError hors des fautes du bras", RX, "MemoryError, TypeError, AttributeError", "MemoryError, AttributeError", [T_RX]),
    ("c6", "contrôle avant l'ouverture sans le témoin", RX, "        temoin = _temoin(racine, config, c, s)\n        n = len(",
     "        temoin = s\n        n = len(", [T_RX]),
    ("c7", "contrôle avant l'ouverture sans les directions de P3", RX,
     '        n = len(_directions_p3(racine, config, s, int(config[CLE_CONFIG]["n_p3"])))', "        n = 4", [T_RX]),
    ("c8", "cache : morceaux de l'index non contrôlés", RX, "        manquants += [x for x in attendus if not (dossier / x).is_file()]",
     "        manquants += []", [T_RX]),
    ("c9", "cache : fichiers essentiels non contrôlés", RX, "    manquants = [n for n in FICHIERS_MODELE if not (dossier / n).is_file()]",
     "    manquants = []", [T_RX]),
    ("c10", "cache jamais lu (mode réel compris)", RX, '    if mode == "reel":\n        cache = revision_au_cache(',
     '    if False:\n        cache = revision_au_cache(', [T_RX]),
    ("c11", "palier global : le meilleur (n25c)", RX, '        v["palier"] = max(decisifs, key=PALIERS.index)',
     '        v["palier"] = min(decisifs, key=PALIERS.index)', [T_RX]),
    ("c12", "passe à blanc sans contrôle de la réextraction", PB, "        reextraction_p3 = controler_avant_ouverture(racine, config)\n",
     "        reextraction_p3 = None\n", [T_LEC]),
    ("c13", "nombre de directions non exigé à l'étape B (fonction)", L4,
     '    n = int(config["n_plancher"])\n    if int(index.get("n_plancher", -1)) != n:', '    return\n    n = int(config["n_plancher"])\n    if int(index.get("n_plancher", -1)) != n:', [T_LEC]),
    ("c14", "nombre de directions non exigé à l'étape B (appel)", L4,
     "            exiger_nombre_de_directions(t, index, config)        # note 05", "            pass        # note 05", [T_LEC]),
    ("c15", "n34 : lecture descriptive dans les scores décisifs", L4, "    t2, idx2, absentes = dict(t), {\"sondes\": []}, {}",
     "    t2, idx2, absentes = t, {\"sondes\": []}, {}", [T_LEC]),
    ("c16", "n28 : réserve de la principale non recopiée", L4, '        for cle in ("reserve", "reserve_principale"):',
     '        for cle in ("reserve",):', [T_LEC]),
    ("c17", "état des figées non affiché après le repli", RT, "sondes lues {r['index']['sondes_lues']} ; plancher des \"",
     "sondes lues {r['index']['sondes_lues']} ; \"", [T_LEC]),
]

if __name__ == "__main__":
    sys.exit(v1.main(Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()))
