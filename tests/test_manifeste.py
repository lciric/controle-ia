import json

import numpy as np
import pytest

from conftest import committer
from controle_ia.gardes import GardeArret, exiger_numpy_minimal
from controle_ia.manifeste import (creer_manifeste, ecrire_resultat, generateur, graines,
                                   lire_manifeste, verifier_resultat)

RUN = "20261004-120000-test"


def test_graines_derivees_deterministes_et_distinctes():
    a = graines(["t1", "t2"], entropie=12345)
    b = graines(["t2", "t1"], entropie=12345)
    assert a["t1"] == b["t1"]  # indépendant de l'ordre
    x1 = generateur(a["t1"]).standard_normal(5)
    x2 = generateur(a["t2"]).standard_normal(5)
    assert not np.allclose(x1, x2)
    assert np.array_equal(x1, generateur(b["t1"]).standard_normal(5))


def test_artefact_graine_alteree():
    g = graines(["t"], entropie=1)["t"]
    g["spawn_key"] = ["2"]
    with pytest.raises(GardeArret, match="graine"):
        generateur(g)


def test_artefact_taches_en_double():
    with pytest.raises(GardeArret, match="double"):
        graines(["t", "t"])


def test_garde_numpy():
    assert exiger_numpy_minimal("1.25.0") == "1.25.0"
    assert exiger_numpy_minimal("2.4.6")
    with pytest.raises(GardeArret):
        exiger_numpy_minimal("1.24.4")


def test_sain_chaine_complete(depot):
    chemin, m = creer_manifeste(depot, RUN, {"n": 3}, ["t"], entropie=7)
    assert m["depot_propre"] and m["reserves"] == []
    r = ecrire_resultat(depot, chemin, "resultat", {"v": 1})
    corps = verifier_resultat(depot, r)
    assert corps["resultat"] == {"v": 1}


def test_artefact_depot_sale(depot):
    (depot / "sale.txt").write_text("x")
    with pytest.raises(GardeArret, match="non propre"):
        creer_manifeste(depot, RUN, {}, ["t"])
    _, m = creer_manifeste(depot, RUN, {}, ["t"], autoriser_depot_sale=True)
    assert m["reserves"]  # la réserve est consignée, pas de repli silencieux


def test_artefact_run_existant(depot):
    creer_manifeste(depot, RUN, {}, ["t"])
    committer(depot)
    with pytest.raises(GardeArret, match="R12"):
        creer_manifeste(depot, RUN, {}, ["t"])


def test_artefact_identifiant_invalide(depot):
    with pytest.raises(GardeArret, match="format"):
        creer_manifeste(depot, "mon run", {}, ["t"])


def test_artefact_decisif_sans_prereg(depot):
    with pytest.raises(GardeArret, match="R1"):
        creer_manifeste(depot, RUN, {}, ["t"], decisif=True)


def test_artefact_config_alteree(depot):
    chemin, _ = creer_manifeste(depot, RUN, {"n": 3}, ["t"])
    m = json.loads(chemin.read_text())
    m["config"]["n"] = 4
    chemin.write_text(json.dumps(m))
    with pytest.raises(GardeArret):
        lire_manifeste(chemin)


def test_artefact_resultat_rattache_a_un_autre_manifeste(depot):
    chemin, _ = creer_manifeste(depot, RUN, {"n": 3}, ["t"])
    r = ecrire_resultat(depot, chemin, "resultat", {"v": 1})
    corps = json.loads(r.read_text())
    corps["manifeste_sha256"] = "0" * 64
    r.write_text(json.dumps(corps))
    (r.parent / "resultat.json.sha256").unlink()
    from controle_ia.scellement import sceller
    sceller(r)
    with pytest.raises(GardeArret, match="autre manifeste"):
        verifier_resultat(depot, r)
