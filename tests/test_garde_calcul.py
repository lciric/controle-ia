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


def test_sain_go_sans_echeance_hors_calcul(racine):
    """L-2 : une ligne « — » d'un GO qui n'est pas de calcul (comme GO-2026-10-07-01, dépôt distant) ne bloque pas le
    lancement cité par un GO de calcul valide."""
    registre(racine, ligne("GO-2026-10-07-01", AUJ - timedelta(days=3), "—", typ="dépôt distant")
             + ligne(GO_OK, AUJ - timedelta(days=1), AUJ + timedelta(days=10)))
    code, err = lancer(racine, f"GO_ID={GO_OK} vastai create instance 123 --image pytorch")
    assert code == 0, err


@pytest.mark.parametrize("contenu", [
    ligne(GO_OK, AUJ - timedelta(days=1), "—"),                                   # GO de calcul sans échéance
    ligne("GO-2026-10-07-01", AUJ - timedelta(days=3), "jamais", typ="dépôt distant")
    + ligne(GO_OK, AUJ - timedelta(days=1), AUJ + timedelta(days=10)),            # autre texte que « — »
])
def test_artefact_echeance_illisible(racine, contenu):
    registre(racine, contenu)
    code, err = lancer(racine, f"GO_ID={GO_OK} vastai create instance 123 --image pytorch")
    assert code == 2 and "dates illisibles" in err, err


def test_registre_reel_du_depot_accepte_le_go_de_calcul_de_la_phase_0():
    """Le vrai registre du dépôt (pas un registre factice : L-2) est lisible par la garde ; GO-2026-10-04-08, de calcul,
    est reconnu, sans juger sa période de validité (elle dépend de la date du test)."""
    import importlib.util

    spec = importlib.util.spec_from_file_location("garde_calcul", HOOK)
    g = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(g)
    go = g.lire_go(HOOK.parents[2] / "registres" / "go.md")
    assert go["GO-2026-10-04-08"]["type"] == "calcul" and go["GO-2026-10-04-08"]["par"] == "Lazar"
    assert go["GO-2026-10-04-08"]["echeance"] == date(2026, 11, 1)


def test_revocation_cas_sain_et_artefact(racine):
    """K-3 : une ligne « révocation » qui cite le GO cité bloque le lancement ; celle d'un autre GO, non."""
    autre = "GO-2026-10-05-02"
    valides = ligne(GO_OK, AUJ - timedelta(days=1), AUJ + timedelta(days=10)) + \
        ligne(autre, AUJ - timedelta(days=1), AUJ + timedelta(days=10))
    registre(racine, valides + f"| GO-2026-10-06-09 | {AUJ} | révocation | révoque {autre} | — | — | Lazar | message |\n")
    code, err = lancer(racine, f"GO_ID={GO_OK} vastai create instance 123 --image pytorch")
    assert code == 0, err
    registre(racine, valides + f"| GO-2026-10-06-09 | {AUJ} | révocation | révoque {GO_OK} | — | — | Lazar | message |\n")
    code, err = lancer(racine, f"GO_ID={GO_OK} vastai create instance 123 --image pytorch")
    assert code == 2 and "révoqué par GO-2026-10-06-09" in err, err


def ligne_ext(ident, accorde, echeance, typ="calcul", par="Lazar", perimetre="extension au pilote p-v1"):
    return f"| {ident} | {accorde} | {typ} | {perimetre} | 40 USD imputés à cette ligne | {echeance} | {par} | R-389 |\n"


def test_sain_ligne_d_extension_au_meme_identifiant(racine):
    """R-389 : une seconde ligne au même identifiant qui se dit « extension », même type, par Lazar, ni antérieure ni
    d'échéance plus lointaine, est admise ; le lancement cité passe et la validité reste celle de la première ligne."""
    import importlib.util

    registre(racine, ligne(GO_OK, AUJ - timedelta(days=2), AUJ + timedelta(days=10))
             + ligne_ext(GO_OK, AUJ - timedelta(days=1), AUJ + timedelta(days=10)))
    code, err = lancer(racine, f"GO_ID={GO_OK} vastai create instance 123 --image pytorch")
    assert code == 0, err
    spec = importlib.util.spec_from_file_location("garde_calcul", racine / ".claude" / "hooks" / "garde_calcul.py")
    g = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(g)
    go = g.lire_go(racine / "registres" / "go.md")
    assert go[GO_OK]["accorde"] == AUJ - timedelta(days=2) and go[GO_OK]["echeance"] == AUJ + timedelta(days=10)
    assert go[GO_OK]["extensions"] == ["extension au pilote p-v1"]


@pytest.mark.parametrize("extension", [
    ligne_ext(GO_OK, AUJ - timedelta(days=1), AUJ + timedelta(days=10), typ="publication"),        # autre type
    ligne_ext(GO_OK, AUJ - timedelta(days=1), AUJ + timedelta(days=10), par="Claude"),             # pas Lazar
    ligne_ext(GO_OK, AUJ - timedelta(days=1), AUJ + timedelta(days=30)),                           # échéance plus lointaine
    ligne_ext(GO_OK, AUJ - timedelta(days=5), AUJ + timedelta(days=10)),                           # antérieure à la première
    ligne_ext(GO_OK, AUJ - timedelta(days=1), AUJ + timedelta(days=10), perimetre="phase 0 bis"),  # ne se dit pas extension
])
def test_artefact_doublon_qui_n_est_pas_une_extension_admise(racine, extension):
    """R-389 : tout doublon qui n'est pas une extension admise bloque, comme avant (aucun repli silencieux, R5)."""
    registre(racine, ligne(GO_OK, AUJ - timedelta(days=2), AUJ + timedelta(days=10)) + extension)
    code, err = lancer(racine, f"GO_ID={GO_OK} vastai create instance 1")
    assert code == 2 and "double" in err, err

