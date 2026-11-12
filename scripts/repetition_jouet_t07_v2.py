#!/usr/bin/env python3
"""Répétition jouet de bout en bout de la lecture de T0.7, v2 : celle de `repetition_jouet_t07_v1.py` (fonctions de préparation
reprises telles quelles, importées), avec **l'entropie du run jouet de T0.6 fixée** (`--entropie-t06`, demande de la
contre-lecture du code, CT-01 : le run jouet de T0.6 tirait une entropie neuve à chaque fois, et un cas qui arrête l'étape A —
des actions sans caractère de mot — ne se rejouait pas). Le code gelé de T0.6 (`1609a4bf`) n'est pas modifié : sans
préenregistrement, `lanceur_v6.executer` passe `entropie=None` à `manifeste.creer_manifeste` ; une enveloppe, lancée par
`python -c` avec le code de l'arbre gelé, remplace ce seul argument par l'entropie donnée, puis appelle `lanceur_v6._main`.

`--repli` : les activations de l'instance sont retirées après le run de T0.6 (disque perdu), et l'étape A passe par
`lecture_v2 repli-recalcul` ; les activations recalculées sont comparées au bit près aux activations d'origine.

    PYTHONPATH=src python -I scripts/repetition_jouet_t07_v2.py --arbre-t06 /home/user/wt-t07-jouet --entropie-t06 N \\
        --dossier <dossier neuf> --sortie <résumé.json> [--repli]
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
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

ENVELOPPE = ("import sys\nfrom controle_ia.t06 import lanceur_v6 as la6\no = la6.creer_manifeste\n"
             "def fixe(*a, entropie=None, **k):\n    return o(*a, entropie=int(sys.argv[1]), **k)\n"
             "la6.creer_manifeste = fixe\nsys.exit(la6._main(sys.argv[2:]))\n")
MOT = re.compile(r"\w+")


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--arbre-t06", required=True)
    ap.add_argument("--entropie-t06", required=True, type=int)
    ap.add_argument("--dossier", required=True)
    ap.add_argument("--sortie", required=True)
    ap.add_argument("--python", default=sys.executable)
    ap.add_argument("--repli", action="store_true")
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
    resume = {"commit_t06": tete, "entropie_t06": a.entropie_t06, "repli": a.repli,
              "commit_t07": subprocess.run(["git", "-C", str(ICI), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip(),
              "debut": datetime.now(timezone.utc).isoformat()}
    config6 = r1.preparer_t06(dossier, arbre)
    r6 = r1.lancer([a.python, "-c", ENVELOPPE, str(a.entropie_t06), "--config", config6.name, "--run-id", r1.RUN_T06],
                   dossier, arbre / "src", journal)
    resume["t06"] = {k: r6[k] for k in ("code", "duree_s")}
    if r6["code"] != 0:
        Path(a.sortie).write_text(json.dumps(resume, ensure_ascii=False, indent=1), encoding="utf-8")
        return 1
    textes = [json.loads(l) for l in (dossier / "donnees" / r1.RUN_T06 / "textes-actions-t06.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    graines6 = json.loads((dossier / "runs" / r1.RUN_T06 / "manifeste.json").read_text())["graines"]     # DF-08 : entropie des graines
    resume["actions_t06"] = {"actions": len(textes), "sans_caractere_de_mot": sum(1 for x in textes if not MOT.search(x["texte"])),
                             "entropie_manifeste": sorted({int(g["entropie"]) for g in graines6.values()})}
    origine = None
    if a.repli:
        origine = dossier.parent / (dossier.name + "-activations-d-origine")
        shutil.move(str(dossier / "donnees" / r1.RUN_T06 / "activations"), str(origine))
    r1.committer(dossier)
    instant_a = int(time.time()) - 600
    config7 = r1.preparer_t07(dossier, r1.rg.date_utc(instant_a - 3600))
    py7 = ICI / "src"
    commande = "repli-recalcul" if a.repli else "etape-a"
    ra = r1.lancer([a.python, "-m", "controle_ia.t07.lecture_v2", commande, str(dossier), r1.RUN_T06, str(config7), "--instant", str(instant_a)],
                   dossier, py7, journal)
    resume["t07_etape_a"] = {k: ra[k] for k in ("code", "duree_s", "sortie")}
    if a.repli:
        recalc = dossier / "donnees" / r1.RUN_T06 / "activations"
        fichiers = sorted(p.relative_to(origine) for p in origine.rglob("*.npy"))
        egaux = [f for f in fichiers if (recalc / f).is_file() and np.array_equal(np.load(origine / f).view(np.uint16), np.load(recalc / f).view(np.uint16))]
        resume["activations"] = {"d_origine": len(fichiers), "egales_au_bit_pres": len(egaux)}
    runs7 = sorted(p.name for p in (dossier / "runs").glob("*-t07-*"))
    if ra["code"] != 0 or not runs7:
        Path(a.sortie).write_text(json.dumps(resume, ensure_ascii=False, indent=1), encoding="utf-8")
        print("ARRÊT : étape A de T0.7 non aboutie (voir le journal)", file=sys.stderr)
        return 1
    run7 = runs7[-1]
    lire = lambda nom: json.loads((dossier / "diag" / run7 / nom).read_text(encoding="utf-8"))["resultat"]
    notation = lire("notation-t07.json")
    resume["temoins_lexicaux_notation"] = notation["index"].get("lexicaux")
    from controle_ia.t07.lecture_v2 import lire_lignes_actuelles
    fin = lire_lignes_actuelles(dossier / "registres" / "scellements-v1.md", (r1.rg.SCORES_T07,))[r1.rg.SCORES_T07]["instant"]
    r1.lignes_b(dossier, run7, fin + 10)
    rb = r1.lancer([a.python, "-m", "controle_ia.t07.lecture_v2", "etape-b", str(dossier), r1.RUN_T06, run7, str(config7), "--instant", str(fin + 100)],
                   dossier, py7, journal)
    resume["t07_etape_b"] = {k: rb[k] for k in ("code", "duree_s")}
    if rb["code"] == 0:
        lec = lire("lecture-t07.json")
        resume["lecture"] = {"issue_critere_3": lec["issue_critere_3"], "Q": lec["doses"]["Q"],
                             "T7-P10": {c: (v.get("etat") if isinstance(v, dict) else v) for c, v in lec["predictions"]["T7-P10"].items()},
                             "reserves": [r["id"] for r in lec["reserves_identifiees"] if r["phrase"] != "non déclenchée"]}
    resume["fin"] = datetime.now(timezone.utc).isoformat()
    Path(a.sortie).write_text(json.dumps(resume, ensure_ascii=False, indent=1, default=str), encoding="utf-8")
    print(json.dumps({"t06": r6["code"], "etape_a": ra["code"], "etape_b": rb["code"], **resume["actions_t06"],
                      **resume.get("activations", {}), "issue": resume.get("lecture", {}).get("issue_critere_3")}, ensure_ascii=False))
    return 0 if rb["code"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
