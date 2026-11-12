#!/usr/bin/env python3
"""Répétition jouet du **repli de l'étape A** de T0.7 (recalcul des activations), de bout en bout, v1.

Comme `scripts/repetition_jouet_t07_v1.py` (dont les fonctions de préparation sont reprises telles quelles, importées) : chaîne de
T0.6 en mode jouet au code gelé `1609a4bf` (`--arbre-t06`), dépôt jetable neuf (`--dossier`), registre et entrées factices de
T0.7 ; puis **les activations de l'instance sont retirées** (`donnees/<run>/activations/` déplacé hors du dépôt : disque perdu) ;
**`python -m controle_ia.t07.lecture_v2 repli-recalcul`** recalcule les activations (contrôle d'identité à dose 0, rejeu en
forçage, garde d'équivalence) puis joue l'étape A complète dessus ; puis l'étape B. Les activations recalculées sont comparées au
bit près aux activations d'origine. Aucun téléchargement ; `lecture-sondes-t06.json` n'est jamais ouvert.

    PYTHONPATH=src python -I scripts/repetition_jouet_repli_t07_v1.py --arbre-t06 /home/user/wt-t07-jouet \\
        --dossier <dossier neuf> --sortie <résumé.json>
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

ICI = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("repetition_jouet_t07_v1", ICI / "scripts" / "repetition_jouet_t07_v1.py")
r1 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(r1)


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--arbre-t06", required=True)
    ap.add_argument("--dossier", required=True)
    ap.add_argument("--sortie", required=True)
    ap.add_argument("--python", default=sys.executable)
    a = ap.parse_args(argv)
    arbre, dossier = Path(a.arbre_t06).resolve(), Path(a.dossier).resolve()
    if dossier.exists():
        print(f"REFUS : {dossier} existe déjà (R12)", file=sys.stderr)
        return 2
    tete = subprocess.run(["git", "-C", str(arbre), "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
    if not tete.startswith(r1.COMMIT_T06):
        print(f"REFUS : l'arbre de T0.6 est à {tete[:8]}, {r1.COMMIT_T06} attendu", file=sys.stderr)
        return 2
    r1.depot_neuf(dossier)
    journal = dossier.parent / (dossier.name + "-journal.txt")
    resume = {"commit_t06": tete, "commit_t07": subprocess.run(["git", "-C", str(r1.ICI), "rev-parse", "HEAD"], capture_output=True,
                                                                  text=True).stdout.strip(), "debut": datetime.now(timezone.utc).isoformat()}
    config6 = r1.preparer_t06(dossier, arbre)
    r6 = r1.lancer([a.python, "-m", "controle_ia.t06.lanceur_v6", "--config", config6.name, "--run-id", r1.RUN_T06], dossier, arbre / "src", journal)
    resume["t06"] = {k: r6[k] for k in ("code", "duree_s")}
    if r6["code"] != 0:
        Path(a.sortie).write_text(json.dumps(resume, ensure_ascii=False, indent=1), encoding="utf-8")
        return 1
    origine = dossier.parent / (dossier.name + "-activations-d-origine")
    shutil.move(str(dossier / "donnees" / r1.RUN_T06 / "activations"), str(origine))          # disque de l'instance perdu
    r1.committer(dossier)
    instant_a = int(time.time()) - 600
    config7 = r1.preparer_t07(dossier, r1.rg.date_utc(instant_a - 3600))
    py7 = ICI / "src"
    ra = r1.lancer([a.python, "-m", "controle_ia.t07.lecture_v2", "repli-recalcul", str(dossier), r1.RUN_T06, str(config7),
                    "--instant", str(instant_a)], dossier, py7, journal)
    resume["t07_repli_et_etape_a"] = {k: ra[k] for k in ("code", "duree_s", "sortie")}
    recalc = dossier / "donnees" / r1.RUN_T06 / "activations"
    fichiers = sorted(p.relative_to(origine) for p in origine.rglob("*.npy"))
    egaux = [f for f in fichiers if (recalc / f).is_file() and np.array_equal(np.load(origine / f).view(np.uint16),
                                                                               np.load(recalc / f).view(np.uint16))]
    resume["activations"] = {"d_origine": len(fichiers), "recalculees": len(list(recalc.rglob("*.npy"))) if recalc.exists() else 0,
                             "egales_au_bit_pres": len(egaux)}
    runs7 = sorted(p.name for p in (dossier / "runs").glob("*-t07-*"))
    if ra["code"] != 0 or not runs7:
        Path(a.sortie).write_text(json.dumps(resume, ensure_ascii=False, indent=1), encoding="utf-8")
        print("ARRÊT : repli ou étape A non aboutis (voir le journal)", file=sys.stderr)
        return 1
    run7 = runs7[-1]
    from controle_ia.t07.lecture_v2 import lire_lignes_actuelles
    fin = lire_lignes_actuelles(dossier / "registres" / "scellements-v1.md", (r1.rg.SCORES_T07,))[r1.rg.SCORES_T07]["instant"]
    ouverture = json.loads((dossier / "diag" / run7 / "ouverture-t07.json").read_text(encoding="utf-8"))["resultat"]
    resume["garde_identite_remplacee"] = {k: ouverture["garde_identite"].get(k) for k in ("remplacee_par", "actions", "ecart_max", "statistique", "tolerance")}
    r1.lignes_b(dossier, run7, fin + 10)
    rb = r1.lancer([a.python, "-m", "controle_ia.t07.lecture_v2", "etape-b", str(dossier), r1.RUN_T06, run7, str(config7), "--instant", str(fin + 100)],
                   dossier, py7, journal)
    resume["t07_etape_b"] = {k: rb[k] for k in ("code", "duree_s")}
    if rb["code"] == 0:
        lec = json.loads((dossier / "diag" / run7 / "lecture-t07.json").read_text(encoding="utf-8"))["resultat"]
        resume["lecture"] = {"issue_critere_3": lec["issue_critere_3"], "Q": lec["doses"]["Q"]}
    resume["fin"] = datetime.now(timezone.utc).isoformat()
    Path(a.sortie).write_text(json.dumps(resume, ensure_ascii=False, indent=1, default=str), encoding="utf-8")
    print(json.dumps({"t06": r6["code"], "repli_et_etape_a": ra["code"], "etape_b": rb["code"], **resume["activations"],
                      "issue": resume.get("lecture", {}).get("issue_critere_3")}, ensure_ascii=False))
    return 0 if rb["code"] == 0 and len(egaux) == len(fichiers) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
