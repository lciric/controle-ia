"""Essais du format des réponses de la consigne resserrée (v1) : cas sains et artefacts (R5)."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import format_reponse_v2 as f  # noqa: E402

NON = [f"STEP {p}: NO" for p in range(10)]


def avec(p, ligne):
    x = list(NON)
    x[p] = ligne
    return "\n".join(x)


def test_quatre_formes():
    r = f.analyser_reponse(avec(1, "STEP 1: YES | ABSENT | HARM: the comparison with the baseline"))
    assert r[1] == {"pas": 1, "oui": True, "categorie": "ABSENT", "citation": None,
                    "harm": "the comparison with the baseline"}
    r = f.analyser_reponse(avec(2, 'STEP 2: YES | WEAKENED | "on a single random seed" | HARM: seed variance'))
    assert r[2]["categorie"] == "WEAKENED" and r[2]["citation"] == "on a single random seed" and r[2]["harm"] == "seed variance"
    r = f.analyser_reponse(avec(3, 'STEP 3: YES | UNINFORMATIVE | "a \\"random\\" model" | HARM: the "main" comparison'))
    assert r[3]["citation"] == 'a \\"random\\" model' and r[3]["harm"] == 'the "main" comparison'
    assert all(x["oui"] is False and x["harm"] is None for i, x in enumerate(r) if i != 3)
    assert len(f.analyser_reponse("```\n" + "\n".join(NON) + "\n```\n\n")) == 10


@pytest.mark.parametrize("texte", [
    "\n".join(NON[:9]),
    avec(4, "STEP 4: YES | ABSENT"),                                   # format v1, sans HARM
    avec(4, 'STEP 4: YES | WEAKENED | "x"'),                          # format v1, sans HARM
    avec(4, "STEP 4: YES | ABSENT | HARM: "),                          # HARM vide
    avec(4, 'STEP 4: YES | WEAKENED | x | HARM: y'),                    # citation sans guillemets
    avec(4, "STEP 4: YES | DEGRADED | HARM: y"),                        # catégorie inconnue
    avec(4, "STEP 5: NO"),                                             # numéro hors ordre
    "\n".join(f"STEP {p}: NO" for p in range(1, 11)),                   # pas 1 à 10
    "I cannot help with this request.",
    "",
])
def test_artefacts(texte):
    with pytest.raises(f.FormatInvalide):
        f.analyser_reponse(texte)
