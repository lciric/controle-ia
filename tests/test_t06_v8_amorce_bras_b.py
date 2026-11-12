"""Amorce v8 : le bras B (annexe) ne change rien au run de T0.6 et n'échoue jamais la course. Un faux module `faux_bras_b` (sur `BRAS_B_PYTHONPATH`) joue le rôle du module réel :
il écrit `diag/<run>/…json` et `runs/<run>/manifeste.json` (comme `ecrire_resultat`) ou échoue ou dort. Cas sain et artefacts (R5)."""
from __future__ import annotations

import os
import sys
import textwrap
from pathlib import Path

import pytest

import test_t06_v7_amorce as t6a
from test_t06_v7_amorce import _distant, _fichiers_distants, _git, _lancer_amorce, bac  # noqa: F401

RACINE = Path(__file__).resolve().parents[1]
AMORCE7 = RACINE / "scripts" / "amorce_instance_t06_v7.sh"
AMORCE8 = RACINE / "scripts" / "amorce_instance_t06_v8.sh"
BRANCHE = "calcul/t06-jouet-v4"
CONFIG = "docs/notes/g0-deux-semaines-v1/config-bras-b-t06-v1.json"

FAUX = {"ok": "pass",
        "echec": "raise SystemExit(7)",
        "leve": "raise RuntimeError('boum')",
        "dort": "import time; time.sleep(30)"}


def _faux_module(tmp_path, comportement: str) -> dict:
    d = tmp_path / "faux"
    d.mkdir(exist_ok=True)
    (d / "faux_bras_b.py").write_text(textwrap.dedent(f'''
        import argparse, json, pathlib
        ap = argparse.ArgumentParser(); [ap.add_argument(a) for a in ("--config", "--run-id", "--prereg")]; ap.add_argument("--autoriser-depot-sale", action="store_true")
        a = ap.parse_args()
        {FAUX[comportement]}
        for sous, nom in (("diag", "audit-fuite-r1-v4-bras-b-v1.json"), ("runs", "manifeste.json")):
            p = pathlib.Path(sous) / a.run_id; p.mkdir(parents=True, exist_ok=True); (p / nom).write_text(json.dumps({{"run_id": a.run_id}}), encoding="utf-8")
        print(json.dumps({{"issue": "non tranché"}}))
        '''), encoding="utf-8")
    return {"BRAS_B_MODULE": "faux_bras_b", "BRAS_B_PYTHONPATH": str(d), "BRAS_B_PYTHON": sys.executable}


def _avec_config(bac):
    f = bac["source"] / CONFIG
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text("{}", encoding="utf-8")
    t6a._commit_source(bac, "ajout de la configuration de l annexe")


def _sujets(distant):
    return _git(distant, "log", "--reverse", "--format=%s", BRANCHE).splitlines()


@pytest.fixture(params=["v7", "v8"])
def amorce(request, monkeypatch):
    monkeypatch.setattr(t6a, "AMORCE", AMORCE7 if request.param == "v7" else AMORCE8)
    return request.param


def test_cas_sain_le_bras_b_s_ajoute_apres_la_poussee_finale_sans_toucher_au_run(bac, amorce, tmp_path):
    """Avec la configuration au commit et le mode forcé : v8 ajoute UN commit de bras B après les commits du run ; v7 (sans bras B) n'en a aucun. Les commits du run sont identiques."""
    _avec_config(bac)
    distant = _distant(bac)
    code, journal, sortie, racine = _lancer_amorce(bac, distant, env_sup={"BRAS_B_FORCER": "1", **_faux_module(tmp_path, "ok")})
    assert code == 0 and (racine / "t06-fin-normale").exists(), sortie[-1200:]
    sujets = _sujets(distant)
    run_commits = [s for s in sujets if "bras B" not in s]
    assert len(run_commits) == (len(sujets) - 1 if amorce == "v8" else len(sujets))
    if amorce == "v7":
        assert not [f for f in _fichiers_distants(distant) if f.split("\t")[-1].startswith(("diag/bras-b-", "runs/bras-b-", "traces/bras-b-"))]
        return
    assert sujets[-1] == "T0.6 : bras B de l'audit de fuite (annexe, code 0)", sujets
    fichiers = [f.split("\t")[-1] for f in _fichiers_distants(distant)]
    assert any(f.startswith("diag/bras-b-") and f.endswith("audit-fuite-r1-v4-bras-b-v1.json") for f in fichiers)
    assert any(f.startswith("runs/bras-b-") and f.endswith("manifeste.json") for f in fichiers)
    assert any(f.startswith("traces/bras-b-") and f.endswith("bras-b.out") for f in fichiers)
    assert "bras B : code 0" in journal and "bras B : branche calcul/t06-jouet-v4 poussée" in journal and "ERREUR DE CHAÎNE" not in journal
    # l'ordre : la poussée finale du run est AVANT le début du bras B, et l'arrêt de l'instance après
    assert journal.index("poussée (résultats, données légères, morceaux et traces)") < journal.index("bras B : début") < journal.index("bras B : code 0")


def test_le_run_de_t06_est_identique_avec_et_sans_bras_b(bac, tmp_path, monkeypatch):
    """Mêmes commits du run (sujets), même code de sortie, même marqueur de fin normale, avec et sans bras B (v8)."""
    monkeypatch.setattr(t6a, "AMORCE", AMORCE8)
    _avec_config(bac)
    d1, d2 = _distant(bac), _distant(bac)
    c1, _, _, r1 = _lancer_amorce(bac, d1, "avec", {"BRAS_B_FORCER": "1", **_faux_module(tmp_path, "ok")})
    c2, _, _, r2 = _lancer_amorce(bac, d2, "sans", {"BRAS_B": "0"})
    assert c1 == c2 == 0 and (r1 / "t06-fin-normale").exists() and (r2 / "t06-fin-normale").exists()
    avec = [s for s in _sujets(d1) if "bras B" not in s]
    sans = _sujets(d2)
    norm = lambda l: [" ".join(x.split()[:2]) if "run 2026" in x else x for x in l]               # les identifiants de run portent l'heure
    assert norm(avec) == norm(sans) and len(_sujets(d1)) == len(sans) + 1


@pytest.mark.parametrize("comportement, code_attendu", [("echec", 7), ("leve", 1)])
def test_artefact_le_bras_b_qui_echoue_ne_fait_pas_echouer_la_course(bac, tmp_path, monkeypatch, comportement, code_attendu):
    monkeypatch.setattr(t6a, "AMORCE", AMORCE8)
    _avec_config(bac)
    distant = _distant(bac)
    code, journal, sortie, racine = _lancer_amorce(bac, distant, env_sup={"BRAS_B_FORCER": "1", **_faux_module(tmp_path, comportement)})
    assert code == 0 and (racine / "t06-fin-normale").exists() and not (racine / "t06-fin-anormale").exists(), sortie[-1200:]
    assert f"bras B : code {code_attendu}" in journal and "sans effet sur le run de T0.6" in journal and "ERREUR DE CHAÎNE" not in journal
    assert _sujets(distant)[-1] == f"T0.6 : bras B de l'audit de fuite (annexe, code {code_attendu})"        # les sorties d'erreur sont consignées, rien d'autre


def test_artefact_le_delai_depasse_ne_bloque_pas(bac, tmp_path, monkeypatch):
    monkeypatch.setattr(t6a, "AMORCE", AMORCE8)
    _avec_config(bac)
    distant = _distant(bac)
    code, journal, sortie, racine = _lancer_amorce(bac, distant, env_sup={"BRAS_B_FORCER": "1", "BRAS_B_DUREE_MAX_S": "2", **_faux_module(tmp_path, "dort")})
    assert code == 0 and (racine / "t06-fin-normale").exists(), sortie[-1200:]
    assert "bras B : code 124" in journal


@pytest.mark.parametrize("env, motif", [({}, "non lancé (mode jouet)"), ({"BRAS_B": "0", "BRAS_B_FORCER": "1"}, "non lancé (BRAS_B=0)")])
def test_non_lance_en_jouet_ou_desactive(bac, tmp_path, monkeypatch, env, motif):
    monkeypatch.setattr(t6a, "AMORCE", AMORCE8)
    _avec_config(bac)
    distant = _distant(bac)
    code, journal, sortie, racine = _lancer_amorce(bac, distant, env_sup={**env, **_faux_module(tmp_path, "ok")})
    assert code == 0 and motif in journal
    assert not [f for f in _fichiers_distants(distant) if f.split("\t")[-1].startswith(("diag/bras-b-", "runs/bras-b-", "traces/bras-b-"))]


def test_configuration_absente_non_lance(bac, tmp_path, monkeypatch):
    monkeypatch.setattr(t6a, "AMORCE", AMORCE8)
    distant = _distant(bac)
    code, journal, sortie, racine = _lancer_amorce(bac, distant, env_sup={"BRAS_B_FORCER": "1", **_faux_module(tmp_path, "ok")})
    assert code == 0 and "configuration absente du commit" in journal


def test_epreuve_sans_autorisation_non_lance_et_avec_autorisation_lance(tmp_path):
    """La fonction `bras_b` seule (extraite de l'amorce) : en épreuve à blanc (EPREUVE_GO_ID non vide) elle ne part pas sans BRAS_B_EPREUVE=1 ; avec, elle part ; en mode jouet jamais sans BRAS_B_FORCER."""
    import subprocess

    fonction = subprocess.run(["sed", "-n", "/^bras_b() {/,/^}/p", str(AMORCE8)], capture_output=True, text=True, check=True).stdout
    assert fonction.startswith("bras_b() {")
    (tmp_path / "cfg.json").write_text("{}", encoding="utf-8")

    def jouer(**env):
        harnais = (f'journal() {{ echo "$*"; }}; prendre_verrou() {{ return 1; }}; T={tmp_path}; MODE=reel; BRAS_B_CONFIG={tmp_path / "cfg.json"}; '
                   f'BRAS_B_PYTHON=false; {fonction}\nbras_b; echo "retour $?"')
        e = {"PATH": os.environ["PATH"], **env}
        return subprocess.run(["bash", "-c", harnais], env=e, capture_output=True, text=True, cwd=tmp_path).stdout
    assert "non lancé (épreuve à blanc)" in jouer(EPREUVE_GO_ID="GO-X") and "retour 0" in jouer(EPREUVE_GO_ID="GO-X")
    avec = jouer(EPREUVE_GO_ID="GO-X", BRAS_B_EPREUVE="1")
    assert "bras B : début" in avec and "bras B : code 1" in avec and "retour 0" in avec                  # `false` joue le module en échec : la fonction rend quand même 0
    assert "non lancé (BRAS_B=0)" in jouer(BRAS_B="0")
