"""Sondages du contre-lecteur court (CLB6), contre le code 282e295e non muté : artefacts que la suite ne joue pas."""
import io, json
import numpy as np
import pytest
from controle_ia.gardes import GardeArret
from controle_ia.scellement import sceller
from controle_ia.accumulation_b6 import garde_v1 as gv
from controle_ia.accumulation_b6 import lecture_v1 as lv
from test_accb6_lecture_v1 import RUN_T07, _lire, construire, chaine_plancher_neuf, tirages  # noqa: F401


def _e1_plancher(j, rang, n):
    t = dict(j.t)
    p = t[f"plancher_{rang}"]
    t[f"plancher_{rang}"] = p[:n] if n <= p.shape[0] else np.vstack([p] * (n // p.shape[0] + 1))[:n]
    index = json.loads((j.racine / "diag" / RUN_T07 / "notation-t07.json").read_text())["resultat"]["index"]
    t["index"] = np.frombuffer(json.dumps(index, ensure_ascii=False, sort_keys=True).encode("utf-8"), dtype=np.uint8)
    p = j.racine / "donnees" / RUN_T07 / gv.FICHIER_SCORES
    buf = io.BytesIO(); np.savez(buf, **t)
    p.write_bytes(buf.getvalue()); (p.parent / (p.name + ".sha256")).unlink(); sha = sceller(p)
    j.registre_partage.write_text(j.registre_partage.read_text(encoding="utf-8").replace(j.lignes["scores"][1], sha), encoding="utf-8")


@pytest.mark.parametrize("rang,n", [(1, 200), (1, 3200), (0, 3200), (1, 0)])
def test_nombre_de_directions_sur_une_autre_sonde_et_multiples(depot, tirages, rang, n):
    j = construire(depot)
    nom = j.sondes[rang]["nom"]
    _e1_plancher(j, rang, n)
    with pytest.raises(lv.ArretAccb6, match=f"sonde {nom} : {n} directions de plancher, 800 attendues"):
        _lire(j)
    assert gv.LECTURE_ACCB6 not in j.registre_propre.read_text(encoding="utf-8")


@pytest.mark.parametrize("faux", ["", {}, 0, False, (), {"a": 1}, 3.5])
def test_reserves_fausses_vides_arret(faux):
    if faux == ():
        pytest.skip("un tuple ne vient pas d'un JSON")
    with pytest.raises(GardeArret, match="liste de chaînes attendue"):
        lv.reserves_t07_recopiees({"reserves": faux}, [])


def test_reserves_entrees_non_chaines_et_prefixe():
    s = [{"nom": "a-c1", "concept": "a"}]
    for x in (None, 1, ["plancher neuf de a-c1"], b"plancher neuf de a-c1".decode()[:0] or None):
        with pytest.raises(GardeArret, match="chaîne attendue"):
            lv.reserves_t07_recopiees({"reserves": ["ok", x]}, s)
    # préfixe exact : « plancher neuf » sans « de », majuscule, espace en tête : non recopiés
    for c in ("plancher neuf : a-c1", "Plancher neuf de a-c1", " plancher neuf de a-c1", "plancher neufs de a-c1", "plancher neuf de"):
        assert lv.reserves_t07_recopiees({"reserves": [c]}, s) == []
    r = lv.reserves_t07_recopiees({"reserves": ["plancher neuf de a-c1 (x) : y"] * 2}, s)
    assert len(r) == 2 and all(x["sondes_visees"] == ["a-c1"] for x in r)          # doublons gardés, dans l'ordre
    # noms emboîtés : la sonde « a-c1 » est visée par une chaîne qui nomme « a-c15 » (appartenance, non ancrage)
    s2 = [{"nom": "a-c1", "concept": "a"}, {"nom": "a-c15", "concept": "a"}]
    r2 = lv.reserves_t07_recopiees({"reserves": ["plancher neuf de a-c15 (x) : y"]}, s2)
    print("\nCLB6 noms emboîtés :", r2[0]["sondes_visees"])


def test_g1_reserves_non_lues(depot, tirages):
    """Sous G-1, rien de `resultat.reserves` n'est lu, même hors de forme."""
    from test_accb6_lecture_v1 import e4_jouet, ecrire_resultat, _corps
    j = construire(depot, sans_e4=True)
    e4 = e4_jouet(j, "G-1")
    e4["reserves"] = {"hors": "forme"}
    ecrire_resultat(j.racine, j.racine / "runs" / RUN_T07 / "manifeste.json", "lecture-t07", e4)
    corps = _corps(j, _lire(j))
    print("\nCLB6 G-1 :", corps["aiguillage"]["ligne"], corps["reserves_t07"])
    assert corps["aiguillage"]["ligne"] == "G-1" and corps["reserves_t07"] == []
