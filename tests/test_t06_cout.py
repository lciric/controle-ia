"""Lecteur du coût neuf de T0.6 (P-015) : milliers à l'espace, formes douteuses, cas sain et artefact (R5)."""
from __future__ import annotations

import pytest

from controle_ia.environnements.propositions import heures_declarees
from controle_ia.t06 import cout


@pytest.mark.parametrize("champ, attendu", [
    ("120", 120.0), ("120 GPU-hours", 120.0), ("1 000", 1000.0), ("10 000 GPU-hours", 10000.0), ("1 000 000", 1e6),
    ("1 000", 1000.0), ("1,000", 1000.0), ("1,000.5", 1000.5), ("1,5", 1.5), ("2k", 2000.0), ("2 k", 2000.0),
    ("2.5k GPU-hours", 2500.0), ("about 300 (A100)", 300.0), ("120h", 120.0), ("0", 0.0),
])
def test_lecture_cas_sains(champ, attendu):
    assert cout.lire_cout(champ)["cout"] == attendu


def test_milliers_a_l_espace_corriges_par_rapport_au_lecteur_de_p3():
    assert heures_declarees("1 000") == 1.0                     # défaut connu du lecteur gelé (P-015)
    r = cout.lire_cout("1 000")
    assert r["cout"] == 1000.0 and r["cout_milliers_espace"]


def test_nombre_colle_a_des_lettres_lu_entier():
    assert heures_declarees("120h") == 12.0                     # repli du lecteur gelé sur un préfixe
    assert cout.lire_cout("120h")["cout"] == 120.0


def test_formes_douteuses_consignees_jamais_corrigees():
    r = cout.lire_cout("100-200 GPU-hours")
    assert r["cout"] == 100.0 and r["cout_intervalle"] and r["cout_plusieurs_nombres"]
    r = cout.lire_cout("3 x 100")
    assert r["cout"] == 3.0 and r["cout_multiplication"]
    assert cout.lire_cout("2k")["cout_suffixe_k"]
    assert cout.lire_cout("2 kg")["cout"] == 2.0 and not cout.lire_cout("2 kg")["cout_suffixe_k"]


def test_absence_et_illisibles():
    assert cout.lire_cout(None)["cout"] is None and not cout.lire_cout(None)["cout_present"]
    assert cout.lire_cout("unknown")["cout"] is None and cout.lire_cout("unknown")["cout_present"]
    assert not cout.cout_lisible(0) and not cout.cout_lisible(None) and not cout.cout_lisible(float("nan"))
    assert not cout.cout_lisible(True) and cout.cout_lisible(1.5)


def test_cout_action_lit_le_champ_de_l_action():
    texte = "ACTION: ADD\nTITLE: t\nPROPOSAL: p\nCONTROLS: c\nCOST: 1 200 GPU-hours\nPREDICTION: q"
    r = cout.cout_action(texte)
    assert r["valide"] and r["cout"] == 1200.0 and r["cout_milliers_espace"]
    r = cout.cout_action("rien de lisible")
    assert not r["valide"] and r["cout"] is None
