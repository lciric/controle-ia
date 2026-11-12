"""Greffon de pytest (développeur accb6-v2) : à la fin de la session, écrit le chemin de chaque module `controle_ia*` chargé et de
chaque module d'essais `test_accb6_*` / `conftest` (import tracé, R-2246) dans le fichier nommé par TRACE_IMPORT_ACCB6."""
import os
import sys


def pytest_sessionfinish(session, exitstatus):
    lignes = []
    for nom, m in sorted(sys.modules.items()):
        f = getattr(m, "__file__", None)
        if f and (nom == "controle_ia" or nom.startswith("controle_ia.") or nom.startswith("test_accb6_") or nom.startswith("test_t07_")
                  or nom == "conftest" or nom.startswith("essai_reverif")):
            lignes.append(f"{nom}\t{os.path.realpath(f)}")
    with open(os.environ["TRACE_IMPORT_ACCB6"], "w", encoding="utf-8") as sortie:
        sortie.write("\n".join(lignes) + "\n")
