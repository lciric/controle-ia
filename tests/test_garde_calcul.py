"""Garde de calcul (hook PreToolUse) : cas sains et artefacts (R5)."""
import json
import shutil
import subprocess
import sys
from datetime import date, timedelta
from pathlib import Path

import pytest

HOOK = Path(__file__).resolve().parents[1] / ".claude" / "hooks" / "garde_calcul.py"
AUJ = date.today()
ENTETE = "| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |\n|---|---|---|---|---|---|---|---|\n"


def ligne(ident, accorde, echeance, typ="calcul", par="Lazar"):
    return f"| {ident} | {accorde} | {typ} | phase 0 | 150 USD | {echeance} | {par} | message |\n"


@pytest.fixture
def racine(tmp_path):
    (tmp_path / ".claude" / "hooks").mkdir(parents=True)
    shutil.copy(HOOK, tmp_path / ".claude" / "hooks" / "garde_calcul.py")
    (tmp_path / "registres").mkdir()
    return tmp_path


def registre(racine, contenu):
    (racine / "registres" / "go.md").write_text("# GO\n\n" + ENTETE + contenu, encoding="utf-8")


def lancer(racine, commande, brut=None):
    entree = brut if brut is not None else json.dumps({"tool_name": "Bash", "tool_input": {"command": commande}})
    r = subprocess.run([sys.executable, str(racine / ".claude" / "hooks" / "garde_calcul.py")],
                       input=entree, capture_output=True, text=True)
    return r.returncode, r.stderr


GO_OK = "GO-2026-10-05-01"


@pytest.mark.parametrize("commande", [
    "ls -la", "kill 12345", "kill -TERM 4242", "vastai show instances", "vastai destroy instance 987654",
    "python -m pytest", "echo pkillers",
])
def test_sain_commandes_ordinaires(racine, commande):
    registre(racine, "")
    assert lancer(racine, commande)[0] == 0


def test_sain_lancement_avec_go_valide(racine):
    registre(racine, ligne(GO_OK, AUJ - timedelta(days=1), AUJ + timedelta(days=10)))
    code, err = lancer(racine, f"GO_ID={GO_OK} vastai create instance 123 --image pytorch")
    assert code == 0, err


@pytest.mark.parametrize("commande", [
    "pkill -f vllm", "killall python3", "kill $(pgrep -f train.py)", "kill `pgrep python`",
    "pgrep -f serve | xargs kill", "pgrep -f serve | xargs -r kill -9", "sleep 1; pkill python",
])
def test_artefact_arret_par_motif(racine, commande):
    registre(racine, "")
    code, err = lancer(racine, commande)
    assert code == 2 and "R10" in err


def test_artefact_lancement_sans_go(racine):
    registre(racine, ligne(GO_OK, AUJ, AUJ + timedelta(days=10)))
    code, err = lancer(racine, "vastai create instance 123 --image pytorch")
    assert code == 2 and "identifiant de GO" in err


@pytest.mark.parametrize("contenu,motif", [
    ("", "absent de registres"),
    (ligne(GO_OK, AUJ - timedelta(days=30), AUJ - timedelta(days=1)), "hors de sa période"),
    (ligne(GO_OK, AUJ + timedelta(days=1), AUJ + timedelta(days=10)), "hors de sa période"),
    (ligne(GO_OK, AUJ, AUJ + timedelta(days=1), typ="publication"), "type"),
    (ligne(GO_OK, AUJ, AUJ + timedelta(days=1), par="Claude"), "Lazar"),
    (f"| {GO_OK} | {AUJ} | calcul | phase 0 |\n", "mal formé"),
    (f"| {GO_OK} | hier | calcul | p | 1 | demain | Lazar | m |\n", "dates"),
    (ligne(GO_OK, AUJ, AUJ) * 2, "double"),
])
def test_artefact_go_invalide(racine, contenu, motif):
    registre(racine, contenu)
    code, err = lancer(racine, f"GO_ID={GO_OK} vastai create instance 1")
    assert code == 2 and motif in err, err


def test_artefact_registre_absent(racine):
    code, err = lancer(racine, f"GO_ID={GO_OK} vastai create instance 1")
    assert code == 2 and "absent" in err


def test_artefact_entree_illisible(racine):
    registre(racine, "")
    code, err = lancer(racine, None, brut="pas du json")
    assert code == 2 and "illisible" in err
