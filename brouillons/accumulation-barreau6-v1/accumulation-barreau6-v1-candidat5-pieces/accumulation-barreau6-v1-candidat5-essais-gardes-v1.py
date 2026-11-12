#!/usr/bin/env python3
"""Essais ciblés des gardes du script de fabrication du candidat 5 (R5) : un cas sain et un artefact par garde.

Lancement : python3 -I -B <ce script> <racine du dépôt> <dossier des pièces (couples + script, lu)> <python> <dossier de travail>
Chaque cas est joué dans un dossier temporaire neuf du dossier de travail ; le dépôt et le dossier des pièces ne sont jamais écrits.
"""
from __future__ import annotations

import copy
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

NOM_C = "accumulation-barreau6-v1-candidat5-couples-v1.json"
NOM_S = "accumulation-barreau6-v1-candidat5-faire-v1.py"
NOM_4 = "accumulation-barreau6-v1-candidat5.md"


def jouer(racine, essai, py, doc, travail, pre=None):
    with tempfile.TemporaryDirectory(dir=travail) as d:
        d = Path(d)
        (d / "sortie").mkdir()
        shutil.copy(Path(essai) / NOM_S, d / NOM_S)
        (d / NOM_C).write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        if pre:
            pre(d)
        r = subprocess.run([py, "-I", "-B", str(d / NOM_S), racine, str(d), str(d / "sortie")],
                           capture_output=True, text=True)
        present = (d / "sortie" / NOM_4).exists()
        return r.returncode, (r.stdout + r.stderr) + f"\n[candidat 5 {'présent' if present else 'absent'} après le lancement]"


def main(racine, essai, py, travail):
    base = json.loads((Path(essai) / NOM_C).read_text(encoding="utf-8"))
    par_id = lambda doc, i: next(c for c in doc["couples"] if c["id"] == i)  # noqa: E731
    cas = []

    def artefact(nom, attendu, modif=None, pre=None):
        doc = copy.deepcopy(base)
        if modif:
            modif(doc)
        code, sortie = jouer(racine, essai, py, doc, travail, pre)
        ok = (code == 0 and "TOUT PASSE" in sortie and "[candidat 5 présent" in sortie) if attendu is None else (code != 0 and all(x in sortie for x in ((attendu,) if isinstance(attendu, str) else attendu)) and "TOUT PASSE" not in sortie)
        lignes = [l for l in sortie.strip().splitlines() if l]
        cas.append((nom, ok, code, (lignes[-2] if len(lignes) > 1 else "")[:200] + " " + lignes[-1]))

    artefact("cas sain", None)

    def a1(doc):
        c = par_id(doc, "C5-08"); c["nouveau"] = c["nouveau"].replace("R-2277", "R-2278")
    artefact("Q-1 réécrit", "Q-1 : absent, en double ou différent du couple préparé", a1)

    def a2(doc):
        c = par_id(doc, "C5-10"); c["gelee"] = False; c["g5"] = None
    artefact("C5-10 déclaré hors section gelée", "C5-10 : section réelle « Liste d'arrêt »", a2)

    def a3(doc):
        c = par_id(doc, "C5-10")
        c["nouveau"] = c["nouveau"].replace("Champ de T0.7 attendu absent de E1, E2, E2b ou E4", "Champ de T0.7 attendu absent", 1)
    artefact("suppression sensible (« E1, E2, E2b ou E4 »)", "mot sensible supprimé en section gelée", a3)

    def a4(doc):
        c = par_id(doc, "C5-13"); c["nouveau"] = c["nouveau"] + " <<MARQUEUR_ESSAI>>"
    artefact("marqueur laissé", "marqueurs restants", a4)

    def a5(doc):
        c = par_id(doc, "C5-13"); c["nouveau"] = c["nouveau"] + " " + par_id(doc, "C5-14")["nouveau"]
    artefact("couple non réversible", "(retour) : texte cherché présent 2 fois", a5)

    def a6(doc):
        c = par_id(doc, "C5-01"); c["ancien"] = c["ancien"].replace("candidat 4", "candidat 9")
    artefact("ancien absent", "C5-01 : « ancien » présent 0 fois", a6)

    def pre8(d):
        (d / "sortie" / NOM_4).write_text("autre texte\n", encoding="utf-8")
    artefact("candidat 5 présent et différent (R12)", ("candidat 5 déjà présent et différent", "[candidat 5 présent après le lancement]"), None, pre8)

    def a11(doc):
        c = par_id(doc, "C5-13"); c["nouveau"] = c["nouveau"] + " À REMPLIR"
    artefact("problemes non vide : candidat 5 neuf effacé", ("controle_ia.prereg.problemes", "[candidat 5 absent après le lancement]"), a11)

    def a10(doc):
        c = par_id(doc, "C5-12"); c["nouveau"] = c["nouveau"] + "\n\n## Seuil\n\nfaux seuil"
    artefact("titre de niveau 2 inséré hors section gelée", "titres de niveau 2 changés", a10)

    for nom, ok, code, derniere in cas:
        print(f"{'OK ' if ok else 'ÉCHEC'} | {nom} | code {code} | {derniere}")
    print("TOUS CONFORMES" if all(ok for _, ok, _, _ in cas) else "ÉCART")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
