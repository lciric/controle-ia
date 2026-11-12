"""Banc de mutations du bras B, v5 : strict sur le code de sortie de pytest (réserve de la contre-lecture de la v11 v2). Cas sains et artefacts (R5)."""
from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]


def _banc(nom):
    spec = importlib.util.spec_from_file_location(nom, RACINE / "scripts" / f"{nom}.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


@pytest.mark.parametrize("code, verdict", [(0, "survivante"), (1, "tuee"), (5, "invalide"), (2, "erreur"), (3, "erreur"), (4, "erreur"), (137, "erreur")])
def test_v5_classe_les_codes_de_pytest(code, verdict):
    assert _banc("banc_mutations_bras_b_v5").classer(code) == verdict


def test_artefact_v4_comptait_le_code_5_comme_tue():
    """La v4 : `tuee = r.returncode != 0` — un filtre `-k` vide (code 5) comptait la mutation comme tuée."""
    texte = (RACINE / "scripts" / "banc_mutations_bras_b_v4.py").read_text(encoding="utf-8")
    assert "tuee = r.returncode != 0" in texte and "classer" not in texte
    assert "tuee = r.returncode != 0" not in (RACINE / "scripts" / "banc_mutations_bras_b_v5.py").read_text(encoding="utf-8")


def test_les_filtres_de_la_v5_selectionnent_chacun_au_moins_un_essai():
    """Aucune mutation ne vise un filtre vide : chaque `-k` de la liste sélectionne au moins un essai de tests/test_bras_b_v4.py."""
    import re
    texte = (RACINE / "tests" / "test_bras_b_v4.py").read_text(encoding="utf-8")
    noms = re.findall(r"^def (test_[A-Za-z0-9_]+)", texte, re.M)
    for _, _, _, cible in _banc("banc_mutations_bras_b_v5").MUTATIONS:
        filtre = cible.removeprefix("test_")
        assert any(filtre in n for n in noms), (cible, "aucun essai sélectionné : le banc le verrait comme code 5")
