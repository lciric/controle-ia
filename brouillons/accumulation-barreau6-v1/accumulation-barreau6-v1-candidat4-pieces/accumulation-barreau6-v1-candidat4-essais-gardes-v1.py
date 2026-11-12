#!/usr/bin/env python3
"""Essais ciblés des gardes du script de fabrication du candidat 4 (R5) : un cas sain et un artefact par garde.

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

NOM_C = "accumulation-barreau6-v1-candidat4-couples-v1.json"
NOM_S = "accumulation-barreau6-v1-candidat4-faire-v1.py"
NOM_4 = "accumulation-barreau6-v1-candidat4.md"


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
        return r.returncode, (r.stdout + r.stderr) + f"\n[candidat 4 {'présent' if present else 'absent'} après le lancement]"


def main(racine, essai, py, travail):
    base = json.loads((Path(essai) / NOM_C).read_text(encoding="utf-8"))
    par_id = lambda doc, i: next(c for c in doc["couples"] if c["id"] == i)  # noqa: E731
    cas = []

    def artefact(nom, attendu, modif=None, pre=None):
        doc = copy.deepcopy(base)
        if modif:
            modif(doc)
        code, sortie = jouer(racine, essai, py, doc, travail, pre)
        ok = (code == 0 and "TOUT PASSE" in sortie and "[candidat 4 présent" in sortie) if attendu is None else (code != 0 and all(x in sortie for x in ((attendu,) if isinstance(attendu, str) else attendu)) and "TOUT PASSE" not in sortie)
        lignes = [l for l in sortie.strip().splitlines() if l]
        cas.append((nom, ok, code, (lignes[-2] if len(lignes) > 1 else "")[:200] + " " + lignes[-1]))

    artefact("cas sain", None)

    def a1(doc):
        c = par_id(doc, "RV-03"); c["nouveau"] = c["nouveau"].replace("800", "801")
    artefact("RV-03 réécrit", "RV-03 : différent du couple de la revérification", a1)

    def a2(doc):
        c = par_id(doc, "C4-11"); c["gelee"] = False; c["g4"] = None
    artefact("C4-11 déclaré hors section gelée", "C4-11 : section réelle « Seuil »", a2)

    def a3(doc):
        c = par_id(doc, "C4-11")
        c["ancien"] = "plus de 1 % de tirages dégénérés, " + c["ancien"]
        c["nouveau"] = "plus de tirages dégénérés, " + c["nouveau"]
    artefact("suppression sensible non permise (« 1 % »)", "mot sensible supprimé en section gelée", a3)

    def a4(doc):
        c = par_id(doc, "C4-24"); c["nouveau"] = c["nouveau"] + " <<MARQUEUR_ESSAI>>"
    artefact("marqueur laissé", "marqueurs restants", a4)

    def a5(doc):
        c = par_id(doc, "C4-24"); c["nouveau"] = c["nouveau"] + " " + par_id(doc, "C4-25")["nouveau"]
    artefact("couple non réversible", "(retour) : texte cherché présent 2 fois", a5)

    def a6(doc):
        c = par_id(doc, "C4-01"); c["ancien"] = c["ancien"].replace("candidat 3", "candidat 9")
    artefact("ancien absent", "C4-01 : « ancien » présent 0 fois", a6)

    def a7(doc):
        c = par_id(doc, "C4-17"); c["g4"] = "G4-99"
    artefact("numéro G4 faux", "numéro de déclaration G4-99", a7)

    def pre8(d):
        (d / "sortie" / NOM_4).write_text("autre texte\n", encoding="utf-8")
    artefact("candidat 4 présent et différent (R12)", ("candidat 4 déjà présent et différent", "[candidat 4 présent après le lancement]"), None, pre8)

    def a9(doc):
        doc["sections_gelees"] = doc["sections_gelees"][:-1]
    artefact("liste des sections gelées tronquée", "liste des sections gelées différente", a9)

    def a11(doc):
        c = par_id(doc, "C4-24"); c["nouveau"] = c["nouveau"] + " À REMPLIR"
    artefact("problemes non vide : candidat 4 neuf effacé", ("controle_ia.prereg.problemes", "[candidat 4 absent après le lancement]"), a11)

    def a10(doc):
        c = par_id(doc, "C4-19"); c["nouveau"] = c["nouveau"] + "\n\n## Seuil\n\nfaux seuil"
    artefact("titre de niveau 2 inséré hors section gelée", "titres de niveau 2 changés", a10)

    for nom, ok, code, derniere in cas:
        print(f"{'OK ' if ok else 'ÉCHEC'} | {nom} | code {code} | {derniere}")
    print("TOUS CONFORMES" if all(ok for _, ok, _, _ in cas) else "ÉCART")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
