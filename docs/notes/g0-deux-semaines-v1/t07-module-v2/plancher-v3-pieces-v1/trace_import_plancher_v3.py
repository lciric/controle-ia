"""Greffon pytest du banc de mutations du plancher v3 : à la fin de la session, écrit (fichier de `TRACE_IMPORT_SORTIE`) le chemin
et l'empreinte de chaque module neuf de T0.7 réellement importé (import tracé, R-2246)."""
import hashlib
import json
import os
import sys

NOMS = ("plancher_v3", "reextraction_p3_v1", "lecture_v4", "passe_blanc_v2", "repli_etapes_v2")


def pytest_sessionfinish(session, exitstatus):
    sortie = os.environ.get("TRACE_IMPORT_SORTIE")
    if not sortie:
        return
    vus = {}
    for n in NOMS:
        m = sys.modules.get(f"controle_ia.t07.{n}")
        if m is not None:
            with open(m.__file__, "rb") as f:
                vus[n] = {"chemin": os.path.realpath(m.__file__), "sha256": hashlib.sha256(f.read()).hexdigest()}
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump({"modules": vus, "code": int(exitstatus)}, f, ensure_ascii=False)
