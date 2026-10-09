import subprocess

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.scellement import compagnon, sceller, verifier, verifier_arbre


def test_sain_sceller_puis_verifier(tmp_path):
    f = tmp_path / "a.json"
    f.write_text('{"x": 1}\n')
    h = sceller(f)
    assert verifier(f) == h
    assert sceller(f) == h  # idempotent
    # compatible avec sha256sum -c
    r = subprocess.run(["sha256sum", "-c", compagnon(f).name], cwd=tmp_path, capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr


def test_artefact_fichier_altere(tmp_path):
    f = tmp_path / "a.json"
    f.write_text("1\n")
    sceller(f)
    f.write_text("2\n")
    with pytest.raises(GardeArret, match="empreinte"):
        verifier(f)


def test_artefact_compagnon_absent(tmp_path):
    f = tmp_path / "a.json"
    f.write_text("1\n")
    with pytest.raises(GardeArret, match="absente"):
        verifier(f)


def test_artefact_compagnon_mauvais_nom(tmp_path):
    f = tmp_path / "a.json"
    f.write_text("1\n")
    h = sceller(f)
    compagnon(f).write_text(f"{h}  b.json\n")
    with pytest.raises(GardeArret, match="nom"):
        verifier(f)


def test_artefact_ecrasement_interdit(tmp_path):
    f = tmp_path / "a.json"
    f.write_text("1\n")
    sceller(f)
    f.write_text("2\n")
    with pytest.raises(GardeArret, match="R12"):
        sceller(f)


def test_artefact_fichier_absent(tmp_path):
    with pytest.raises(GardeArret, match="absent"):
        sceller(tmp_path / "rien.json")


def test_arbre_sain_et_artefacts(tmp_path):
    d = tmp_path / "diag"
    d.mkdir()
    ok = d / "ok.json"
    ok.write_text("1\n")
    sceller(ok)
    assert verifier_arbre(tmp_path) == []
    nu = d / "nu.json"
    nu.write_text("1\n")  # non scellé
    orphelin = d / "parti.json"
    orphelin.write_text("1\n")
    sceller(orphelin)
    orphelin.unlink()  # empreinte orpheline
    problemes = dict(verifier_arbre(tmp_path))
    assert "diag/nu.json" in problemes
    assert "orpheline" in problemes["diag/parti.json.sha256"]
