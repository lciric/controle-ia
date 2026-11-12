"""Essais du script de comptes par préenregistrement (v1) : cas sain et artefacts (R5)."""
import importlib.util
from pathlib import Path

import pytest

CHEMIN = Path(__file__).resolve().parents[1] / "scripts" / "comptes_par_preenregistrement_v1.py"
spec = importlib.util.spec_from_file_location("comptes_v1", CHEMIN)
comptes = importlib.util.module_from_spec(spec)
spec.loader.exec_module(comptes)


def ligne(prereg: str, ident: str, issue: str) -> str:
    return f"| `{prereg}` | e | {ident} | x | s | v | ev | {issue} | c | r |"


def test_cas_sain_groupes_et_taux():
    texte = "\n".join([
        "| préenregistrement | empreinte | prédiction | énoncé | seuil | verdict | ev | issue | contre-lu | runs |",
        ligne("prereg/T0.3-simulation-lemme-theoreme-v1.md", "P1.1", "confirmée"),
        ligne("prereg/T0.4-validation-modele-reel-v3.md", "P0", "confirmée"),
        ligne("prereg/T0.4-validation-modele-reel-v1.md", "P2", "non concluante"),
        ligne("prereg/P3-premier-test-i-a-v1.md", "P3-P1", "confirmée"),
        ligne("prereg/P3-premier-test-i-a-v1.md", "P3-P3", "réfutée"),
        ligne("prereg/P3-premier-test-i-a-v1.md", "P3-P4", "sans objet"),
        ligne("prereg/autre-v1.md", "X1", "sans run décisif cité par un manifeste"),
    ])
    sortie = comptes.rendre(comptes.lire_table(texte))
    assert "| preuves en simulation | 1 | 0 | 0 | 1 / 1 = 1,000 |" in sortie
    assert "| instruments | 1 | 0 | 1 | 1 / 2 = 0,500 |" in sortie
    assert "| prédictions empiriques | 1 | 1 | 0 | 1 / 2 = 0,500 |" in sortie
    assert "| **toutes** | 3 | 1 | 1 | 3 / 5 = 0,600 |" in sortie
    assert "Lignes lues : 7 ; tranchées : 5 ; hors taux : 2." in sortie
    # un préenregistrement sans ligne tranchée n'a pas de ligne propre
    assert "autre-v1.md" not in sortie


def test_artefact_table_vide_arrete():
    with pytest.raises(SystemExit):
        comptes.lire_table("| en-tête | seul |\n|---|---|\n")


def test_artefact_ligne_tronquee_arrete():
    with pytest.raises(SystemExit):
        comptes.lire_table("| `prereg/a-v1.md` | e | P1 |")
