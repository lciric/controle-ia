"""Garde d'empreinte du lanceur v3 au crochet `garde_calcul.py` (M2 de la contre-lecture `4591fe97…`, R-1984) : cas sains
et artefacts (R5).

Le crochet est appelé comme Claude Code l'appelle : un processus à part, l'entrée JSON de `PreToolUse` sur l'entrée
standard (`tool_name`, `tool_input.command`, `cwd`), code 0 (passe) ou 2 (bloqué, motif sur la sortie d'erreur). Les cas
qui modifient un fichier travaillent sur une copie du crochet dans un dossier jetable, où seule la constante
`DEPOT_COURSE` est remplacée par ce dossier ; le crochet réel du dépôt est appelé tel quel pour le cas sain réel. Le
lanceur n'est jamais exécuté : le crochet ne fait que lire et hacher."""
from __future__ import annotations

import hashlib
import importlib.util
import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]
HOOK = RACINE / ".claude" / "hooks" / "garde_calcul.py"
NOM = "lancer_course_ideation_pilier_attaque_v2_v3"
FICHIER = NOM + ".py"
LANCEUR = RACINE / "scripts" / FICHIER
EXACTE = "/usr/local/bin/python3 -I -B scripts/" + FICHIER
DEPOT_REEL = "/home/user/controle-ia-travail"
LIGNE_CONSTANTE = 'DEPOT_COURSE = Path("/home/user/controle-ia-travail")'


def appeler(hook: Path, commande: str, cwd: str | None, brut: str | None = None):
    entree = {"session_id": "essai", "hook_event_name": "PreToolUse", "tool_name": "Bash",
              "tool_input": {"command": commande, "description": "essai"}}
    if cwd is not None:
        entree["cwd"] = cwd
    r = subprocess.run([sys.executable, str(hook)], input=brut if brut is not None else json.dumps(entree),
                       capture_output=True, text=True, timeout=60)
    return r.returncode, r.stderr


@pytest.fixture
def jetable(tmp_path):
    """Copie du crochet, du lanceur et de son compagnon dans un dépôt jetable ; `DEPOT_COURSE` → ce dépôt."""
    (tmp_path / ".claude" / "hooks").mkdir(parents=True)
    (tmp_path / "scripts").mkdir()
    (tmp_path / "registres").mkdir()
    (tmp_path / "registres" / "go.md").write_text("# GO\n", encoding="utf-8")
    texte = HOOK.read_text(encoding="utf-8")
    assert texte.count(LIGNE_CONSTANTE) == 1
    hook = tmp_path / ".claude" / "hooks" / "garde_calcul.py"
    hook.write_text(texte.replace(LIGNE_CONSTANTE, f"DEPOT_COURSE = Path({str(tmp_path)!r})"), encoding="utf-8")
    shutil.copy(LANCEUR, tmp_path / "scripts" / FICHIER)
    shutil.copy(str(LANCEUR) + ".sha256", tmp_path / "scripts" / (FICHIER + ".sha256"))
    return {"racine": tmp_path, "hook": hook, "lanceur": tmp_path / "scripts" / FICHIER,
            "compagnon": tmp_path / "scripts" / (FICHIER + ".sha256")}


# ----------------------------------------------------------------------------------------------------------- cas sains

def test_sain_crochet_reel_commande_exacte():
    """Le crochet réel, sur le lanceur réel, depuis le dépôt réel : la commande permise passe (rien n'est exécuté)."""
    code, err = appeler(HOOK, EXACTE, DEPOT_REEL)
    assert code == 0, err


def test_sain_constante_egale_compagnon_et_fichier_reels():
    spec = importlib.util.spec_from_file_location("garde_calcul_essai_v3", HOOK)
    g = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(g)
    lue = hashlib.sha256(LANCEUR.read_bytes()).hexdigest()
    compagnon = (Path(str(LANCEUR) + ".sha256")).read_text().split()
    assert g.EMPREINTE_LANCEUR_V3 == lue == compagnon[0] and compagnon[1] == FICHIER
    assert g.COMMANDE_LANCEUR_V3 == EXACTE and str(g.DEPOT_COURSE) == DEPOT_REEL


def test_sain_copie_jetable(jetable):
    code, err = appeler(jetable["hook"], EXACTE, str(jetable["racine"]))
    assert code == 0, err


@pytest.mark.parametrize("commande", [
    "ls -la", "python -m pytest -q tests/test_" + FICHIER, "git status", "echo lancer_course_ideation_pilier_attaque_v2_v2.py",
    "cat scripts/lancer_course_ideation_pilier_attaque_v2_v3b.py",
])
def test_sain_commandes_qui_ne_citent_pas_le_lanceur(jetable, commande):
    """Les essais du lanceur (`test_…`), le lanceur v2 et un autre nom ne sont pas des citations du lanceur v3 ;
    `cwd` absent ne compte pas hors de la garde 3."""
    assert appeler(jetable["hook"], commande, None)[0] == 0


# ----------------------------------------------------------------------------------------------------------- artefacts

def test_artefact_fichier_modifie_d_un_octet(jetable):
    with open(jetable["lanceur"], "ab") as f:
        f.write(b"#")
    code, err = appeler(jetable["hook"], EXACTE, str(jetable["racine"]))
    assert code == 2 and "empreinte épinglée" in err, err


def test_artefact_fichier_et_compagnon_modifies_ensemble(jetable):
    """Fichier modifié et compagnon réécrit pour lui correspondre : la constante épinglée bloque encore."""
    with open(jetable["lanceur"], "ab") as f:
        f.write(b"\n# autre contenu\n")
    h = hashlib.sha256(jetable["lanceur"].read_bytes()).hexdigest()
    jetable["compagnon"].write_text(f"{h}  {FICHIER}\n")
    code, err = appeler(jetable["hook"], EXACTE, str(jetable["racine"]))
    assert code == 2 and "empreinte épinglée" in err, err


@pytest.mark.parametrize("contenu,motif", [
    ("0" * 64 + "  " + FICHIER + "\n", "empreinte du compagnon"),
    (None, "mal formé"),                                     # bonne empreinte, autre nom
    ("", "mal formé"),                                       # vide
    ("pas une empreinte\n", "mal formé"),
])
def test_artefact_compagnon_modifie(jetable, contenu, motif):
    if contenu is None:
        h = jetable["compagnon"].read_text().split()[0]
        contenu = f"{h}  autre.py\n"
    jetable["compagnon"].write_text(contenu)
    code, err = appeler(jetable["hook"], EXACTE, str(jetable["racine"]))
    assert code == 2 and motif in err, err


def test_artefact_compagnon_absent(jetable):
    jetable["compagnon"].unlink()
    code, err = appeler(jetable["hook"], EXACTE, str(jetable["racine"]))
    assert code == 2 and "illisible" in err, err


def test_artefact_lanceur_absent_ou_lien(jetable, tmp_path):
    vrai = tmp_path / "ailleurs.py"
    shutil.move(jetable["lanceur"], vrai)
    code, err = appeler(jetable["hook"], EXACTE, str(jetable["racine"]))
    assert code == 2 and "absent ou lien symbolique" in err, err
    jetable["lanceur"].symlink_to(vrai)                       # même contenu, mais par un lien
    code, err = appeler(jetable["hook"], EXACTE, str(jetable["racine"]))
    assert code == 2 and "lien symbolique" in err, err


@pytest.mark.parametrize("commande", [
    EXACTE + " --accepter-sans-bac-a-sable",                  # argument en plus
    EXACTE + " ",                                             # espace en plus
    EXACTE + "; echo fini",                                   # commande composée
    "cd /tmp && " + EXACTE,
    "GO_ID=GO-2026-11-08-13 " + EXACTE,
    "python3 -I -B scripts/" + FICHIER,                       # interpréteur du PATH
    "/usr/bin/python3 -I -B scripts/" + FICHIER,              # autre interpréteur
    ".venv/bin/python -I -B scripts/" + FICHIER,
    "/usr/local/bin/python3 -B scripts/" + FICHIER,           # sans -I
    "/usr/local/bin/python3 -I scripts/" + FICHIER,           # sans -B
    "/usr/local/bin/python3 -I -B " + DEPOT_REEL + "/scripts/" + FICHIER,   # chemin absolu
    "/usr/local/bin/python3 -I -B ./scripts/" + FICHIER,
    "cat scripts/" + FICHIER,                                 # toute autre citation
    "sed -i s/a/b/ scripts/" + FICHIER,
    "echo x > scripts/" + FICHIER + ".sha256",
])
def test_artefact_commande_non_exacte(jetable, commande):
    code, err = appeler(jetable["hook"], commande, str(jetable["racine"]))
    assert code == 2 and "pas exactement" in err, err


@pytest.mark.parametrize("cwd", [None, "", "/tmp", "/home/user"])
def test_artefact_dossier_courant(jetable, cwd):
    code, err = appeler(jetable["hook"], EXACTE, cwd)
    assert code == 2 and ("dossier courant absent" in err or "lancé depuis" in err), err


def test_artefact_crochet_d_un_autre_depot(jetable, tmp_path):
    """Une copie du crochet hors de `DEPOT_COURSE` ne valide rien (la constante n'est pas remplacée ici)."""
    autre = tmp_path / "autre" / ".claude" / "hooks"
    autre.mkdir(parents=True)
    shutil.copy(HOOK, autre / "garde_calcul.py")
    code, err = appeler(autre / "garde_calcul.py", EXACTE, DEPOT_REEL)
    assert code == 2 and "crochet de" in err, err


def test_artefact_r10_garde_sa_priorite(jetable):
    code, err = appeler(jetable["hook"], "pkill -f " + NOM, str(jetable["racine"]))
    assert code == 2 and "R10" in err, err


def test_artefact_entree_illisible(jetable):
    code, err = appeler(jetable["hook"], "", None, brut="pas du json")
    assert code == 2 and "illisible" in err
