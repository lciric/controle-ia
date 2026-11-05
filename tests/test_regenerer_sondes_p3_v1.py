"""Régénération des sondes figées de P3 (`scripts/regenerer_sondes_p3_v1.py`), mode jouet, dépôt jetable (R5) :
cas sain (arrêt juste après les sondes figées, aucun épisode, fichier identique au bit près : `accepte-identique`) ;
niveau 2 (sceau différent, fichier léger et aires identiques : `accepte-avec-declaration`) ; artefacts (tableau du
fichier léger, aire de validation, sonde manquante, référence au sceau faux, sortie qui existe déjà, lanceur qui va au
bout sans passer par les sondes figées)."""
import importlib.util
import json
from pathlib import Path

import numpy as np
import pytest

from controle_ia.premier_test_ia import run as rp
from controle_ia.scellement import sceller
from test_premier_test_ia_run import _config, _taches, entropie_fixe  # noqa: F401  (fixture autouse reprise)

RACINE_DEPOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("regenerer_sondes_p3_v1", RACINE_DEPOT / "scripts" / "regenerer_sondes_p3_v1.py")
rg = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rg)

RUN_REF = "20261028-120000-p3-jouet"


@pytest.fixture
def reference(depot, tmp_path, monkeypatch):
    """Un run jouet complet de P3, comme la référence ; le lanceur de la régénération est celui du dépôt."""
    f = _taches(depot)
    from conftest import committer
    committer(depot)
    config = _config(tmp_path)
    resume = rp.executer(config, depot, RUN_REF, None, str(f), autoriser_depot_sale=True)
    monkeypatch.setattr(rg, "importer_p3", lambda racine: rp)
    yield {"depot": depot, "taches": f, "config": config, "resume": resume,
           "legeres": depot / "donnees" / RUN_REF / "sondes-figees-legeres.npz",
           "diag": depot / "diag" / RUN_REF / "sondes-figees.json"}


def _lancer(ref, tmp_path, run_id, *, legeres=None, diag=None, sceau=None, sortie=None, manifeste=None):
    cfg = tmp_path / f"config-{run_id}.json"
    cfg.write_text(json.dumps(ref["config"]), encoding="utf-8")
    sortie = sortie or tmp_path / f"verdict-{run_id}.json"
    argv = ["--racine", str(ref["depot"]), "--config", str(cfg), "--taches", str(ref["taches"]), "--run-id", run_id,
            "--reference-legeres", str(legeres or ref["legeres"]), "--reference-diag", str(diag or ref["diag"]),
            "--sceau-attendu", sceau or ref["resume"]["sondes_figees_sha256"], "--sortie", str(sortie),
            "--autoriser-depot-sale", "--fils-blas", "1"] + (["--reference-manifeste", str(manifeste)] if manifeste else [])
    vraie = rp.progres
    try:
        code = rg._main(argv)
    finally:
        rp.progres = vraie                   # l'enveloppe d'arrêt ne survit pas à l'appel
    return code, (json.loads(sortie.read_text(encoding="utf-8")) if sortie.exists() else None)


def _copie_scellee(src: Path, dst: Path) -> Path:
    dst.write_bytes(src.read_bytes())
    sceller(dst)
    return dst


def test_cas_sain_identique_et_arret_avant_episodes(reference, tmp_path, capfd):
    code, v = _lancer(reference, tmp_path, "20261028-130000-p3-jouet")
    assert code == 0 and v["verdict"] == "accepte-identique"
    assert v["sceau_regenere"] == reference["resume"]["sondes_figees_sha256"]
    assert v["comparaison_legeres"]["conforme"] and v["comparaison_aires"]["conforme"]
    assert v["etapes_vues"][-1] == "sondes-figees" and "episodes" not in v["etapes_vues"]
    d = reference["depot"] / "diag" / "20261028-130000-p3-jouet"
    assert not (d / "episodes-p3.json").exists() and not (d / "resume.json").exists()
    arret = json.loads((d / "arret.json").read_text(encoding="utf-8"))["resultat"]
    assert "régénération" in arret["motif"] and arret["etape"] == "sondes figées"
    assert not (reference["depot"] / "donnees" / "20261028-130000-p3-jouet" / "scores-p3.npz").exists()
    assert "etape=episodes" not in capfd.readouterr().err


def test_niveau_2_sceau_different_legeres_et_aires_identiques(reference, tmp_path):
    diag = json.loads(reference["diag"].read_text(encoding="utf-8"))
    diag["resultat"]["sondes_figees_sha256"] = "f" * 64
    faux = tmp_path / "diag-faux.json"
    faux.write_text(json.dumps(diag), encoding="utf-8")
    sceller(faux)
    code, v = _lancer(reference, tmp_path, "20261028-130001-p3-jouet", diag=faux, sceau="f" * 64)
    assert code == 0 and v["verdict"] == "accepte-avec-declaration" and v["comparaison_legeres"]["ecart_max"] == 0.0


def _legeres_modifiees(reference, tmp_path, modifier) -> Path:
    with np.load(reference["legeres"], allow_pickle=False) as z:
        t = {k: np.array(z[k]) for k in z.files}
    modifier(t)
    p = tmp_path / "legeres-modifiees.npz"
    with open(p, "wb") as f:
        np.savez(f, **t)
    sceller(p)
    return p


def _niveau_2(reference, tmp_path, run_id, **k):
    diag = json.loads(reference["diag"].read_text(encoding="utf-8"))
    diag["resultat"]["sondes_figees_sha256"] = "e" * 64
    if "aire" in k:
        c = next(iter(diag["resultat"]["aires_validation"]))
        n = next(iter(diag["resultat"]["aires_validation"][c]))
        diag["resultat"]["aires_validation"][c][n] += k.pop("aire")
    faux = tmp_path / f"diag-{run_id}.json"
    faux.write_text(json.dumps(diag), encoding="utf-8")
    sceller(faux)
    return _lancer(reference, tmp_path, run_id, diag=faux, sceau="e" * 64, **k)


def test_artefact_tableau_ecarte(reference, tmp_path):
    def pousser(t):
        k = next(k for k in t if k != "index")
        t[k] = t[k] + 1e-3
    code, v = _niveau_2(reference, tmp_path, "20261028-130002-p3-jouet",
                        legeres=_legeres_modifiees(reference, tmp_path, pousser))
    assert code == 0 and v["verdict"] == "refuse" and v["comparaison_legeres"]["ecart_max"] >= 1e-3


def test_artefact_ecart_sous_la_tolerance_accepte(reference, tmp_path):
    def pousser(t):
        k = next(k for k in t if k != "index")
        t[k] = t[k] + 1e-8
    code, v = _niveau_2(reference, tmp_path, "20261028-130003-p3-jouet",
                        legeres=_legeres_modifiees(reference, tmp_path, pousser))
    assert code == 0 and v["verdict"] == "accepte-avec-declaration"


def test_artefact_aire_ecartee(reference, tmp_path):
    code, v = _niveau_2(reference, tmp_path, "20261028-130004-p3-jouet", aire=1e-3)
    assert code == 0 and v["verdict"] == "refuse" and not v["comparaison_aires"]["conforme"]


def test_artefact_sonde_manquante(reference, tmp_path):
    def retirer(t):
        index = json.loads(bytes(t["index"]).decode("utf-8"))
        index["sondes"][0]["nom"] = "sonde-inconnue"
        t["index"] = np.frombuffer(json.dumps(index).encode("utf-8"), dtype=np.uint8)
    code, v = _niveau_2(reference, tmp_path, "20261028-130005-p3-jouet",
                        legeres=_legeres_modifiees(reference, tmp_path, retirer))
    assert code == 0 and v["verdict"] == "refuse"
    assert any("absentes" in p for p in v["comparaison_legeres"]["problemes"])


def test_artefact_references_non_conformes(reference, tmp_path):
    faux = _copie_scellee(reference["legeres"], tmp_path / "legeres.npz")
    faux.write_bytes(faux.read_bytes() + b"x")                    # sceau devenu faux
    code, v = _lancer(reference, tmp_path, "20261028-130006-p3-jouet", legeres=faux)
    assert code == 1 and v is None
    code, v = _lancer(reference, tmp_path, "20261028-130007-p3-jouet", sceau="d" * 64)   # référence ≠ sceau attendu
    assert code == 1 and v is None


def test_artefact_sortie_existante_et_mode_reel(reference, tmp_path):
    s = tmp_path / "deja.json"
    s.write_text("{}")
    code, _ = _lancer(reference, tmp_path, "20261028-130008-p3-jouet", sortie=s)
    assert code == 2 and s.read_text() == "{}"
    cfg = tmp_path / "reel.json"
    cfg.write_text(json.dumps(dict(reference["config"], mode="reel")), encoding="utf-8")
    assert rg._main(["--racine", str(reference["depot"]), "--config", str(cfg), "--taches", str(reference["taches"]),
                     "--run-id", "20261028-130009-x", "--reference-legeres", str(reference["legeres"]),
                     "--reference-diag", str(reference["diag"]), "--sortie", str(tmp_path / "v.json"),
                     "--autoriser-depot-sale"]) == 2


def test_artefact_lanceur_sans_sondes_figees(reference, tmp_path, monkeypatch):
    """Un lanceur qui n'émet jamais la ligne des sondes figées va au bout : refusé (code 1), aucun verdict."""
    monkeypatch.setattr(rg, "arreter_apres_sondes", lambda module: {"etapes": [], "arret": False})
    code, v = _lancer(reference, tmp_path, "20261028-130010-p3-jouet")
    assert code == 1 and v is None


def test_graines_egales_et_artefact(reference, tmp_path):
    m = reference["depot"] / "runs" / RUN_REF / "manifeste.json"
    code, v = _lancer(reference, tmp_path, "20261028-130011-p3-jouet", manifeste=m)
    assert code == 0 and v["verdict"] == "accepte-identique" and v["comparaison_graines"]["conforme"]
    assert v["comparaison_graines"]["cles_comparees"] >= 3 + 20
    faux = json.loads(m.read_text(encoding="utf-8"))
    k = next(k for k in faux["graines"] if k.startswith("sonde/"))
    faux["graines"][k] = faux["graines"]["plancher/enjeux"]
    f = tmp_path / "manifeste-faux.json"
    f.write_text(json.dumps(faux), encoding="utf-8")
    sceller(f)
    code, v = _lancer(reference, tmp_path, "20261028-130012-p3-jouet", manifeste=f)
    assert code == 0 and v["verdict"] == "refuse" and not v["comparaison_graines"]["conforme"]


def test_openblas_regle_et_relu():
    avant = rg.regler_openblas(1)["fils_avant"]
    r = rg.regler_openblas(2)
    assert r["fils"] == 2 and "MAX_THREADS" in r["config"]
    rg.regler_openblas(avant)
    with pytest.raises(SystemExit):
        rg.regler_openblas(10_000)                      # au-delà du plafond compilé : relu différent, arrêt


def test_comparer_graines_sans_sonde_refuse():
    assert not rg.comparer_graines({"tirage-enjeux": [1]}, {"tirage-enjeux": [1]})["conforme"]
