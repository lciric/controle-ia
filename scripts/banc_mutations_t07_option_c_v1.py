#!/usr/bin/env python3
"""Banc de mutations de l'option (c) des phrases des concepts dans le module T0.7 (R-2166 ; brouillon 21, « Accord au code »,
point 20) — v1, fichier neuf (aucun banc de mutations du module T0.7 n'existait : seuls ceux de T0.6 et du bras B).

Chaque mutation est appliquée à un fichier de `src/controle_ia/t07/` (texte exact, présent une seule fois), les essais de
`tests/test_t07_option_c_concepts_v1.py` sont joués (`-x`), puis le fichier est **rétabli octet pour octet** (sha256 contrôlé,
même en cas d'erreur). Une mutation est « tuée » si les essais échouent. Résultat : un fichier JSON (`--sortie`).

À jouer sur un arbre propre (le banc refuse un `src/` modifié), jamais pendant un autre essai ou une répétition qui importe
`src/` de cet arbre.

    python scripts/banc_mutations_t07_option_c_v1.py --basetemp <dossier neuf> --sortie <résultat.json>
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parents[1]
ESSAIS = "tests/test_t07_option_c_concepts_v1.py"
MUTATIONS = [
    ("m1 phrases lues sans condition de fermeture", "src/controle_ia/t07/lecture_v2.py",
     'if lc is not None and lc["instant"] < int(fermeture):', 'if lc is not None:'),
    ("m2 « <= » au lieu de « < » (strictement avant)", "src/controle_ia/t07/lecture_v2.py",
     'if lc is not None and lc["instant"] < int(fermeture):', 'if lc is not None and lc["instant"] <= int(fermeture):'),
    ("m3 clé redevenue exigée", "src/controle_ia/t07/registre_v1.py",
     'EXIGEES_ETAPE_A = (RUN_CONFIRMATION_T06,)', 'EXIGEES_ETAPE_A = (RUN_CONFIRMATION_T06, SCELLEMENT_CONCEPTS_T07)'),
    ("m4 R15 jamais écrite", "src/controle_ia/t07/lectures_t07_v1.py",
     'r.append({"id": "R15"', 'None and r.append({"id": "R15"'),
    ("m5 état des phrases absent de l'index", "src/controle_ia/t07/lecture_v2.py",
     'index["phrases_concepts"] = extras.get("phrases_concepts")', 'index["phrases_concepts"] = None'),
    ("m6 minimum de quatre concepts ignoré", "src/controle_ia/t07/lecture_v2.py",
     'phrases = sn.lire_phrases_concepts(Path(racine) / lc["chemin"], min_concepts)',
     'phrases = sn.lire_phrases_concepts(Path(racine) / lc["chemin"], 1)'),
    ("m7 jeux lus seulement avec la ligne des concepts", "src/controle_ia/t07/lecture_v2.py",
     'if etape_complete(config):                          # option (c)',
     'if etape_complete(config) and rg.SCELLEMENT_CONCEPTS_T07 in lignes_v:  # option (c)'),
    ("m8 T7-P9 non lue rendue comme « aucune direction notée »", "src/controle_ia/t07/lectures_t07_v1.py",
     'if phrases9.get("etat") == ETAT_PHRASES_NON_LUES else', 'if False else'),
    ("m9 garde « directions sans phrases » retirée (étape A)", "src/controle_ia/t07/lecture_v2.py",
     'if generiques["phrases"] is None and appris["directions"] and appris["directions"].get("directions"):', 'if False:'),
    ("m10 garde « index incohérent » retirée (étape B)", "src/controle_ia/t07/lectures_t07_v1.py",
     'if dirs and phrases9.get("etat") == ETAT_PHRASES_NON_LUES:', 'if False:'),
    ("m11 état des phrases absent du manifeste", "src/controle_ia/t07/lecture_v2.py",
     '"phrases_concepts_etape_a": (generiques or {}).get("phrases_etat")}', '"phrases_concepts_etape_a": None}'),
    ("m12 tâches de plancher de concept écrites sans phrases", "src/controle_ia/t07/lecture_v2.py",
     'if generiques and generiques["phrases"]:', 'if generiques and generiques["jeux"]:'),
]


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--basetemp", required=True)
    ap.add_argument("--sortie", required=True)
    ap.add_argument("--python", default=sys.executable)
    a = ap.parse_args(argv)
    base = Path(a.basetemp).resolve()
    if base.exists():
        print(f"REFUS : {base} existe déjà (R12)", file=sys.stderr)
        return 2
    sale = subprocess.run(["git", "-C", str(ICI), "status", "--porcelain", "--", "src"], capture_output=True, text=True).stdout.strip()
    if sale:
        print(f"REFUS : src/ modifié dans l'arbre : {sale.splitlines()[:3]}", file=sys.stderr)
        return 2
    base.mkdir(parents=True)
    env = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "PYTHONPATH": "src", "PYTHONDONTWRITEBYTECODE": "1",
           "TMPDIR": str(base), "HOME": str(base), "LANG": "C.UTF-8"}
    res = []
    for i, (nom, fichier, avant, apres) in enumerate(MUTATIONS):
        p = ICI / fichier
        brut = p.read_bytes()
        h = hashlib.sha256(brut).hexdigest()
        texte = brut.decode("utf-8")
        if texte.count(avant) != 1:
            print(f"REFUS : mutation {nom!r} : texte trouvé {texte.count(avant)} fois dans {fichier}", file=sys.stderr)
            return 2
        bt = base / f"m{i + 1}"
        try:
            p.write_text(texte.replace(avant, apres), encoding="utf-8")
            r = subprocess.run([a.python, "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", f"--basetemp={bt}",
                                "-o", "tmp_path_retention_policy=none", ESSAIS], cwd=ICI, env=env, capture_output=True, text=True)
        finally:
            p.write_bytes(brut)
            shutil.rmtree(bt, ignore_errors=True)
        if hashlib.sha256(p.read_bytes()).hexdigest() != h:
            print(f"ARRÊT : {fichier} non rétabli après {nom!r}", file=sys.stderr)
            return 3
        lignes = [l for l in r.stdout.strip().splitlines() if l.strip()]
        echec = next((l.split(" ", 1)[1].split(" - ")[0] for l in lignes if l.startswith("FAILED ")), None)
        res.append({"mutation": nom, "fichier": fichier, "code": r.returncode, "tuee": r.returncode != 0,
                    "essai_qui_tue": echec, "derniere_ligne": lignes[-1] if lignes else r.stderr[-300:]})
        print(json.dumps(res[-1], ensure_ascii=False), flush=True)
    Path(a.sortie).write_text(json.dumps({"essais": ESSAIS, "mutations": res,
                                          "tuees": sum(x["tuee"] for x in res), "total": len(res)}, ensure_ascii=False, indent=1) + "\n",
                              encoding="utf-8")
    return 0 if all(x["tuee"] for x in res) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
