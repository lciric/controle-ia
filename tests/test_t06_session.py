"""Chaîne de session de T0.6 (`controle_ia.t06.session`, bibliothèque standard) : GO, dépense, décision de
surveillance ; cas sain et artefact (R5)."""
from __future__ import annotations

from datetime import date, datetime, timezone

import pytest

from controle_ia.t06 import session as se

LIGNE = "| GO-2026-11-02-28 | 2026-11-02 | calcul | T0.6 organisme v0 et test croisé | 200 USD | 2026-11-16 | Lazar | mots |"
ENTETE = "| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |\n|---|---|---|---|---|---|---|---|\n"


def _registre(tmp_path, *lignes):
    p = tmp_path / "go.md"
    p.write_text(ENTETE + "\n".join(lignes) + "\n", encoding="utf-8")
    return p


def test_go_conforme_et_extension(tmp_path):
    r = se.verifier_go(_registre(tmp_path, LIGNE), date(2026, 11, 5))
    assert r["go"] == "GO-2026-11-02-28" and r["plafond_usd"] == 200.0
    ext = "| GO-2026-11-02-28 | 2026-11-03 | calcul | extension : disque | 200 USD | 2026-11-16 | Lazar | mots |"
    assert se.verifier_go(_registre(tmp_path, LIGNE, ext), date(2026, 11, 5))["ligne"] == 3
    assert se.main(["go", str(_registre(tmp_path, LIGNE)), "2026-11-05"]) == 0


@pytest.mark.parametrize("lignes, jour, motif", [
    ((), date(2026, 11, 5), "absent"),
    ((LIGNE.replace("| calcul |", "| dépôt |"),), date(2026, 11, 5), "calcul"),
    ((LIGNE.replace("| Lazar |", "| Claude |"),), date(2026, 11, 5), "Lazar"),
    ((LIGNE.replace("200 USD", "250 USD"),), date(2026, 11, 5), "exact"),
    ((LIGNE,), date(2026, 11, 17), "validité"),
    ((LIGNE,), date(2026, 11, 1), "validité"),
    ((LIGNE, LIGNE), date(2026, 11, 5), "double"),
    ((LIGNE, "| GO-2026-11-02-28 | 2026-11-03 | calcul | extension | 200 USD | 2026-11-20 | Lazar | x |"), date(2026, 11, 5), "double"),
    ((LIGNE, "| GO-2026-11-06-01 | 2026-11-06 | révocation | révoque GO-2026-11-02-28 | — | — | Lazar | x |"), date(2026, 11, 6), "révoqué"),
    ((LIGNE.replace("| 2026-11-02 |", "| 2026-13-02 |"),), date(2026, 11, 5), "illisible"),
])
def test_go_artefacts(tmp_path, lignes, jour, motif):
    with pytest.raises(se.GardeSession, match=motif):
        se.verifier_go(_registre(tmp_path, *lignes), jour)
    assert se.main(["go", str(_registre(tmp_path, *lignes)), jour.isoformat()]) == 1


def test_depense_cumulee():
    d = se.depense_cumulee(1.0, 0.03, 0, 3600 * 10)
    assert d["cumulee_usd"] == 10.3 and not d["arret"] and d["heures"] == 10.0
    assert se.depense_cumulee(1.0, 0.0, 0, 3600 * 200)["arret"]
    assert se.depense_cumulee(1.0, 0.0, 0, 3600, 250.0)["arret"]                # facture plus grande
    assert se.depense_cumulee(1.0, 0.0, 0, 3600, 2.0)["cumulee_usd"] == 2.0
    with pytest.raises(se.GardeSession, match="strictement positif"):
        se.depense_cumulee(0.0, 0.0, 0, 10)
    with pytest.raises(se.GardeSession, match="postérieure"):
        se.depense_cumulee(1.0, 0.0, 100, 10)
    with pytest.raises(se.GardeSession, match="illisible"):
        se.depense_cumulee("x", 0.0, 0, 10)
    assert se.main(["depense", "1.0", "0.03", "0", "36000"]) == 0 and se.main(["depense", "1.0", "0", "0", "720000"]) == 1


def test_decision_de_surveillance():
    base = {"arret": False, "cumulee_usd": 1.0}
    j = "AMORCE 2026-11-05T10:00:00Z : commit abc\nPROGRES 2026-11-05T10:30:00Z etape=episodes lot=1/9\n"
    t = datetime(2026, 11, 5, 10, 40, tzinfo=timezone.utc).timestamp()
    assert se.decider_surveillance(j, t, base) == "POURSUIVRE"
    assert se.decider_surveillance(j, t + 3 * 3600, base).startswith("ALERTE sans PROGRES")   # alerte, aucun arrêt
    assert se.decider_surveillance(j + "AMORCE 2026-11-05T12:00:00Z : RUN MORT sans résumé ni arrêt\n", t, base).startswith("ARRET mort")
    assert se.decider_surveillance(j, t, {"arret": True, "cumulee_usd": 200.5}).startswith("ARRET depense")
    assert se.decider_surveillance(j + "AMORCE 2026-11-05T12:00:00Z : fin, code 0\n", t + 9 * 3600, base).startswith("FIN")
    assert se.decider_surveillance("AMORCE 2026-11-05T10:00:00Z : refus : GO non conforme\n", t, base).startswith("REFUS")
    assert se.decider_surveillance("", t, base) == "POURSUIVRE"                 # journal vide : rien à lire, aucun arrêt
    # un run lent mais vivant n'est jamais arrêté : vingt heures sans PROGRES, dépense sous le plafond → alerte seulement
    assert se.decider_surveillance(j, t + 20 * 3600, base).startswith("ALERTE")
