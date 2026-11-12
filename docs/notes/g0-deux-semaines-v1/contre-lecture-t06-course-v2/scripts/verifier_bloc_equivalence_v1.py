"""Constat neuf n° 1 (adaptation 4) : `equivalence_99e_centile` « absent » pour les six états d'E3 bis.

Montre, sans aucune donnée d'E3 bis, que la forme du résultat `episodes-t06` écrit par la chaîne v12 (`lanceur_v5` →
`lanceur.jouer_evaluation`) ne porte jamais de clé `equivalence` sous `etats[<état>]`, alors que l'extracteur
(`scripts/extraire_mesures_epreuve_t06_v1.py`) la lit exactement là ; le bloc d'équivalence existe, mais PAR FICHE
(`fiches[k]["equivalence"]`, une par épisode). Lecture du code source seulement (AST), aucun calcul, aucun réseau.

Usage : python -I verifier_bloc_equivalence_v1.py ARBRE
"""
from __future__ import annotations

import ast
import json
import sys
from pathlib import Path

arbre = Path(sys.argv[1]).resolve()
src = (arbre / "src/controle_ia/t06/lanceur.py").read_text(encoding="utf-8")
ext = (arbre / "scripts/extraire_mesures_epreuve_t06_v1.py").read_text(encoding="utf-8")
lv5 = (arbre / "src/controle_ia/t06/lanceur_v5.py").read_text(encoding="utf-8")

arbre_ast = ast.parse(src)
fonction = next(n for n in ast.walk(arbre_ast) if isinstance(n, ast.FunctionDef) and n.name == "jouer_evaluation")
cles_etats_relus, cles_fiche = set(), set()
for n in ast.walk(fonction):
    # etats_relus[etat["nom"]] = {...}
    if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Subscript) and isinstance(n.targets[0].value, ast.Name) \
            and n.targets[0].value.id == "etats_relus" and isinstance(n.value, ast.Dict):
        cles_etats_relus |= {k.value for k in n.value.keys if isinstance(k, ast.Constant)}
    # fiches.append({...})
    if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr == "append" and isinstance(n.func.value, ast.Name) \
            and n.func.value.id == "fiches" and n.args and isinstance(n.args[0], ast.Dict):
        cles_fiche |= {k.value for k in n.args[0].keys if isinstance(k, ast.Constant)}
retour = next(n for n in ast.walk(fonction) if isinstance(n, ast.Return))
cles_retour = sorted(k.value for k in retour.value.keys if isinstance(k, ast.Constant))

print(json.dumps({
    "jouer_evaluation.etats_relus[<état>] : clés écrites": sorted(cles_etats_relus),
    "jouer_evaluation.fiches[k] : clés écrites": sorted(cles_fiche),
    "jouer_evaluation : clés rendues": cles_retour,
    "lanceur_v5 écrit etats = ev['etats']": "\"etats\": ev[\"etats\"]" in lv5,
    "extracteur lit etats[<état>]['equivalence']": "v.get(\"equivalence\", ABSENT) for k, v in etats.items()" in ext,
    "extracteur lit fiches[k]['equivalence']": "fiches" in ext and "equivalence" in ext and "for f in" in ext,
    "conclusion": ("la clé « equivalence » n'est jamais écrite sous etats[<état>] : l'extracteur rend « absent » par construction"
                   if "equivalence" not in cles_etats_relus and "equivalence" in cles_fiche else "à revoir"),
}, ensure_ascii=False, indent=1))
