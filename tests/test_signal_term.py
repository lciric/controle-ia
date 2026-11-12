"""Drapeau du signal TERM des lanceurs de T0.5 (`gardes` ; relecture du remplissage de la revalidation, D-1) : un signal
dont l'exception est avalée ou convertie par une bibliothèque reste relevé aux points de contrôle, et l'arrêt consigné
porte le motif « signal TERM ». Cas sain et artefact pour chaque fonction (R5)."""
from __future__ import annotations

import pytest

from controle_ia import gardes
from controle_ia.gardes import GardeArret


def test_exiger_sans_signal_cas_sain_et_artefact():
    gardes.exiger_sans_signal("au pas 0")                       # cas sain : aucun signal reçu
    gardes.SIGNAL_TERM_RECU.append(15)
    with pytest.raises(GardeArret, match=r"signal TERM reçu .* \(relevé au pas 0\)"):
        gardes.exiger_sans_signal("au pas 0")


def test_lever_sur_term_pose_le_drapeau_puis_leve():
    assert not gardes.signal_term_recu()
    try:                                                         # une bibliothèque avale l'exception…
        gardes.lever_sur_term(15, None)
    except Exception:
        pass
    assert gardes.signal_term_recu() and gardes.SIGNAL_TERM_RECU == [15]   # … le drapeau reste posé
    gardes.lever_sur_term(15, None)          # second signal (timeout relaie TERM au groupe) : drapeau seul, K-1
    assert gardes.SIGNAL_TERM_RECU == [15, 15]
    with pytest.raises(GardeArret, match="signal TERM"):
        gardes.exiger_sans_signal("au pas 1")


def test_motif_et_relevement_cas_sain():
    e = ValueError("panne")
    assert gardes.motif_d_arret(e) == "ValueError: panne"
    gardes.relever_term_apres(e)                                 # rien : l'exception d'origine sera propagée


def test_motif_et_relevement_apres_conversion():
    gardes.SIGNAL_TERM_RECU.append(15)
    e = AttributeError("op sans surcharge")
    assert gardes.motif_d_arret(e).startswith(gardes.MOTIF_TERM) and "AttributeError: op sans surcharge" in \
        gardes.motif_d_arret(e)
    with pytest.raises(GardeArret, match="signal TERM") as info:
        gardes.relever_term_apres(e)
    assert info.value.__cause__ is e
    deja = GardeArret(gardes.MOTIF_TERM)                         # l'arrêt TERM lui-même : ni préfixe ni relevage
    assert gardes.motif_d_arret(deja) == f"GardeArret: {gardes.MOTIF_TERM}"
    gardes.relever_term_apres(deja)
