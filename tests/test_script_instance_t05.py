"""Gardes du script de l'instance de T0.5 (`scripts/pilote_t05_instance.sh`), éprouvées de bout en bout sur un dépôt
local (vérification courte 2 de la revalidation, W-1, W-7 (a), W-9, W-10 ; relectures des différentiels, X-1, X-3, Y-1,
Y-11) : le script est exécuté tel quel, contre un dépôt distant local, avec un `python` et un `nvidia-smi` factices
(aucune installation, aucun processeur graphique). Le script mis à l'épreuve ne reçoit qu'un environnement minimal : sur
l'instance, pytest est lancé par ce même script et hérite de ses variables (`BRANCHE` d'un relancement, jetons…), qui
ne doivent pas changer l'issue des tests. Chaque garde a son cas sain et son artefact (R5)."""
from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

import pytest

from controle_ia.scellement import sceller

RACINE = Path(__file__).resolve().parents[1]
SCRIPT = RACINE / "scripts" / "pilote_t05_instance.sh"
# modules que le script appelle avant l'installation (contrôle des sceaux, X-3) : bibliothèque standard seulement
MODULES_AVANT_INSTALLATION = ("__init__.py", "gardes.py", "scellement.py")
# environnement minimal transmis au script mis à l'épreuve (X-1, Y-1) : rien de ce qu'il lit ne vient de l'extérieur
ENV_DE_BASE = ("PATH", "LANG", "LC_ALL", "LC_CTYPE", "TMPDIR")
PREREG = "prereg/revalidation.md"
ENTRAINEMENT = "donnees/20261007-000000-t05-extraction/taches-entrainement.json"
EVALUATION = "donnees/20261007-000000-t05-extraction/taches-evaluation.json"
CONFIG = "prereg/config.json"

PYTHON_FACTICE = """#!/usr/bin/env bash
# python factice : rien ne s'installe ni ne calcule ; chaque garde du script se lit sur le journal. Les options sont lues
# par position (« --config » du lanceur ne doit pas passer pour « -c »).
if [ "$1" = "-m" ] && [ "$2" = "pytest" ]; then
    printf '%s\\n' "${FAUX_PYTEST_LIGNE:-7 passed in 1.00s}"; exit "${FAUX_PYTEST_CODE:-0}"
fi
if [ "$1" = "-c" ]; then
    case "$2" in *"is_available() else 1"*) exit "${FAUX_CARTE_CODE:-0}" ;; esac
    echo "torch factice"; exit 0
fi
echo "lanceur factice : arrêt" >&2
exit 1
"""


def _git(d: Path, *args: str) -> str:
    r = subprocess.run(["git", "-C", str(d), *args], capture_output=True, text=True, check=True)
    return r.stdout.strip()


def _prereg(attendus: str = "7", evaluation: bool = True) -> str:
    return (f"# préenregistrement factice\n- Tests attendus : `{attendus}`\n"
            f"- Chemin de la configuration : `{CONFIG}`\n"
            f"- Chemin des tâches d'entraînement : `{ENTRAINEMENT}`\n"
            + (f"- Chemin des tâches d'évaluation : `{EVALUATION}`\n" if evaluation else ""))


def _prereg_pilote() -> str:
    return (f"# préenregistrement factice du pilote\n- Tests attendus : `7`\n- Chemin de la configuration : `{CONFIG}`\n"
            f"- Chemin des tâches : `{EVALUATION}` (sous donnees/, ajouté de force)\n")


@pytest.fixture
def bac(tmp_path):
    """Dépôt source (préenregistrement, configuration, tâches scellées sous donnees/), dépôt distant nu, environnement
    Python et nvidia-smi factices."""
    src = tmp_path / "source"
    (src / "prereg").mkdir(parents=True)
    _git(tmp_path, "init", "-q", "-b", "main", str(src))
    _git(src, "config", "user.email", "t@example.invalid")
    _git(src, "config", "user.name", "t")
    for d in ("runs", "diag"):                                    # dossiers suivis du vrai dépôt, où le run écrit
        (src / d).mkdir()
        (src / d / ".gitkeep").write_text("", encoding="utf-8")
    (src / PREREG).write_text(_prereg(), encoding="utf-8")
    (src / CONFIG).write_text("{}", encoding="utf-8")
    sceller(src / CONFIG)
    (src / "src" / "controle_ia").mkdir(parents=True)
    for nom in MODULES_AVANT_INSTALLATION:
        shutil.copy(RACINE / "src" / "controle_ia" / nom, src / "src" / "controle_ia" / nom)
    for chemin in (ENTRAINEMENT, EVALUATION):
        f = src / chemin
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text('{"taches": []}', encoding="utf-8")
        sceller(f)
    _git(src, "add", "-A")
    _git(src, "commit", "-qm", "init")
    venv = tmp_path / "venv"
    (venv / "bin").mkdir(parents=True)
    (venv / "bin" / "activate").write_text(f'export PATH="{venv}/bin:$PATH"\n', encoding="utf-8")
    for nom, texte in (("python", PYTHON_FACTICE), ("nvidia-smi", "#!/usr/bin/env bash\necho 'A100, 580, 81920 MiB'\n")):
        (venv / "bin" / nom).write_text(texte, encoding="utf-8")
        (venv / "bin" / nom).chmod(0o755)
    return {"racine": tmp_path, "source": src, "venv": venv}


def _distant(bac) -> Path:
    d = bac["racine"] / f"distant-{len(list(bac['racine'].glob('distant-*')))}.git"
    subprocess.run(["git", "clone", "-q", "--bare", str(bac["source"]), str(d)], check=True)
    return d


def _lancer(bac, distant: Path, travail: str = "t", env_sup: dict | None = None, chemin: str | None = None):
    env = {k: os.environ[k] for k in ENV_DE_BASE if k in os.environ}
    env.update(COMMIT=_git(bac["source"], "rev-parse", "HEAD"), ETUDE="revalidation", MODE="jouet",
               DEPOT_URL=str(distant), TRAVAIL=str(bac["racine"] / travail), PREREG=PREREG,
               VENV_EXISTANT=str(bac["venv"]), HOME=str(bac["racine"]))
    if chemin:
        env["PATH"] = chemin + os.pathsep + env["PATH"]
    env.update(env_sup or {})
    r = subprocess.run(["bash", str(SCRIPT)], env=env, capture_output=True, text=True, timeout=300)
    journal = bac["racine"] / travail / "journal.txt"
    return r.returncode, (journal.read_text(encoding="utf-8") if journal.exists() else "") + r.stderr


def _journal(bac, travail: str = "t") -> str:
    """Le journal seul, sans la sortie d'erreur : ce que la session lit après coup (Z-4)."""
    return (bac["racine"] / travail / "journal.txt").read_text(encoding="utf-8")


def test_cas_sain_lit_le_preenregistrement_puis_passe_les_tests(bac):
    """Cas sain : le préenregistrement est lu avant l'installation, la dernière ligne de pytest est conforme ; le run
    (lanceur factice) s'arrête ensuite, consigné."""
    code, sortie = _lancer(bac, _distant(bac))
    assert "préenregistrement lu : 7 tests attendus" in sortie
    assert "tests : 7 passed in 1.00s" in sortie and "run : " in sortie
    assert code == 1 and "ARRÊT pendant run" in sortie, sortie[-3000:]


@pytest.mark.parametrize("artefact, motif", [
    ("préenregistrement absent", "absent au commit"),
    ("nombre de tests à remplir", "nombre de tests attendus introuvable"),
    ("ligne du chemin absente", "chemin de la configuration ou des tâches introuvable"),
    ("configuration absente", "configuration prereg/config.json absente"),
    ("configuration sans sceau", "fichier cité prereg/config.json ou son sceau absent"),
    ("tâches absentes", "ou son sceau absent de l'arbre du commit"),
    ("sceau absent", "ou son sceau absent de l'arbre du commit"),
    ("empreinte altérée", f"sceau non conforme parmi les fichiers cités (ARRÊT : {EVALUATION} : empreinte"),
    ("configuration altérée", f"sceau non conforme parmi les fichiers cités (ARRÊT : {CONFIG} : empreinte"),
    ("sceau d'un autre fichier", f"(ARRÊT : {EVALUATION}.sha256 : nom 'taches-entrainement.json' au lieu de "
                                 "'taches-evaluation.json')"),
    ("sceau de deux lignes", f"(ARRÊT : {EVALUATION}.sha256 : une seule ligne attendue, 2 trouvées)"),
])
def test_lecture_precoce_du_preenregistrement_artefacts(bac, artefact, motif):
    """W-1, W-10 et X-3 : chaque artefact arrête avant l'installation (code 2), rien n'est lancé ni installé. Les sceaux
    sont lus aux règles du lanceur : un sceau qui nomme un autre fichier, ou de deux lignes, passerait `sha256sum -c`.
    Le journal seul nomme le fichier fautif et la cause (Z-1) ; la configuration altérée est arrêtée de même (Z-2)."""
    src = bac["source"]
    sceau = src / f"{EVALUATION}.sha256"
    if artefact == "préenregistrement absent":
        (src / PREREG).unlink()
    elif artefact == "nombre de tests à remplir":
        (src / PREREG).write_text(_prereg("À REMPLIR"), encoding="utf-8")
    elif artefact == "ligne du chemin absente":
        (src / PREREG).write_text(_prereg(evaluation=False), encoding="utf-8")
    elif artefact == "configuration absente":
        (src / CONFIG).unlink()
    elif artefact == "configuration sans sceau":
        (src / f"{CONFIG}.sha256").unlink()
    elif artefact == "tâches absentes":
        (src / EVALUATION).unlink()
    elif artefact == "sceau absent":
        sceau.unlink()
    elif artefact == "empreinte altérée":
        (src / EVALUATION).write_text('{"taches": [1]}', encoding="utf-8")
    elif artefact == "configuration altérée":                    # sceau gardé, contenu changé
        (src / CONFIG).write_text('{"autre": 1}', encoding="utf-8")
    elif artefact == "sceau d'un autre fichier":       # même contenu, donc même empreinte : seul le nom diffère
        sceau.write_text((src / f"{ENTRAINEMENT}.sha256").read_text(encoding="utf-8"), encoding="utf-8")
        assert subprocess.run(["sha256sum", "-c", "--quiet", sceau.name], cwd=sceau.parent).returncode == 0
    else:
        sceau.write_text(sceau.read_text(encoding="utf-8") + (src / f"{ENTRAINEMENT}.sha256").read_text(encoding="utf-8"),
                         encoding="utf-8")
        assert subprocess.run(["sha256sum", "-c", "--quiet", sceau.name], cwd=sceau.parent).returncode == 0
    _git(src, "add", "-A")
    _git(src, "commit", "-qm", artefact)
    code, sortie = _lancer(bac, _distant(bac))
    assert code == 2 and motif in _journal(bac), sortie[-2000:]
    assert "préenregistrement lu" not in sortie and "torch factice" not in sortie


def test_branche_neuve_cas_sain_present_et_injoignable(bac):
    """W-9 : branche absente (code 2 de git ls-remote) → suite ; présente (code 0) → arrêt ; vérification impossible
    (tout autre code) → arrêt, jamais de repli silencieux."""
    distant = _distant(bac)
    subprocess.run(["git", "-C", str(distant), "branch", "calcul/t05-revalidation-jouet-v1", "main"], check=True)
    code, sortie = _lancer(bac, distant)
    assert code == 2 and "déjà présente sur le dépôt distant" in _journal(bac)
    code, sortie = _lancer(bac, distant, travail="t2", env_sup={"BRANCHE": "calcul/t05-revalidation-jouet-v2"})
    assert "préenregistrement lu" in sortie                                              # cas sain : branche absente
    faux = bac["racine"] / "faux-git"
    faux.mkdir()
    (faux / "git").write_text(
        '#!/usr/bin/env bash\nif [ "$1" = ls-remote ]; then\n'
        '    echo "fatal: unable to access \'x\': Could not resolve host: exemple.invalid" >&2; exit 128\nfi\n'
        f'exec {shutil.which("git")} "$@"\n', encoding="utf-8")
    (faux / "git").chmod(0o755)
    code, sortie = _lancer(bac, distant, travail="t3", chemin=str(faux))
    j = _journal(bac, "t3")
    assert code == 2 and "vérification de la branche" in j and "impossible" in j and "Could not resolve host" in j


@pytest.mark.parametrize("ligne, conforme", [
    ("7 passed in 1.00s", True), ("7 passed, 1 warning in 1.00s", True), ("7 passed, 2 warnings in 1.00s", True),
    ("7 passed in 349.95s (0:05:49)", True),
    ("6 passed in 1.00s", False), ("70 passed in 1.00s", False), ("7 passed, 1 skipped in 1.00s", False),
    ("7 passed, 1 xfailed in 1.00s", False), ("1 failed, 6 passed in 1.00s", False), ("no tests ran in 0.01s", False),
])
def test_derniere_ligne_de_pytest(bac, ligne, conforme):
    """RV-14, W-10 et Y-4 : la dernière ligne de pytest doit être « N passed[, M warning(s)] in X s[ (h:mm:ss)] », rien
    d'autre ; pytest est appelé sans couleur."""
    code, sortie = _lancer(bac, _distant(bac), env_sup={"FAUX_PYTEST_LIGNE": ligne})
    if conforme:
        assert "run : " in sortie and "≠" not in sortie
    else:
        assert code == 1 and "≠ « 7 passed »" in sortie and "run : " not in sortie
    assert "--color=no" in SCRIPT.read_text(encoding="utf-8")


def test_carte_controlee_avant_les_tests_en_mode_reel(bac):
    """RV-14 : en mode réel, une carte invisible pour torch arrête avant les tests ; une carte visible laisse passer."""
    distant = _distant(bac)
    reel = {"MODE": "reel", "HF_TOKEN": "x", "BRANCHE": "calcul/t05-essai-carte-v1", "FAUX_CARTE_CODE": "1"}
    smi = str(bac["venv"] / "bin")                     # nvidia-smi est appelé avant l'activation de l'environnement
    code, sortie = _lancer(bac, distant, env_sup=reel, chemin=smi)
    assert code == 1 and "carte indisponible pour torch" in sortie and "tests : " not in sortie, sortie[-2000:]
    code, sortie = _lancer(bac, distant, travail="t2", env_sup=dict(reel, FAUX_CARTE_CODE="0",
                                                                     BRANCHE="calcul/t05-essai-carte-v2"), chemin=smi)
    assert "tests : 7 passed" in sortie, sortie[-2000:]


def test_environnement_de_l_instance_sans_effet(bac, monkeypatch):
    """X-1 et Y-1 : sur l'instance, pytest hérite des variables du script (relancement avec BRANCHE, jetons, chemins) ;
    elles ne changent ni le cas sain ni l'arrêt sur une branche présente."""
    for k, v in {"BRANCHE": "calcul/t05-pilote-reel-v2", "PREREG_ABSENT": "1", "TESTS_ATTENDUS": "3",
                 "CONFIG": "ailleurs.json", "TACHES": "ailleurs.json", "ENTRAINEMENT": "ailleurs.json",
                 "EVALUATION": "ailleurs.json", "HF_TOKEN": "x", "GH_TOKEN": "x", "FAUX_PYTEST_LIGNE": "1 passed in 1s",
                 "FAUX_CARTE_CODE": "1"}.items():
        monkeypatch.setenv(k, v)
    distant = _distant(bac)
    code, sortie = _lancer(bac, distant)
    assert "préenregistrement lu : 7 tests attendus" in sortie and "tests : 7 passed in 1.00s" in sortie
    assert code == 1 and "ARRÊT pendant run" in sortie, sortie[-3000:]
    subprocess.run(["git", "-C", str(distant), "branch", "-f", "calcul/t05-revalidation-jouet-v1", "main"], check=True)
    code, sortie = _lancer(bac, distant, travail="t2")
    assert code == 2 and "déjà présente sur le dépôt distant" in sortie


def test_etude_pilote_cas_sain_et_branche_presente(bac):
    """Y-11 : en ETUDE=pilote, la ligne « Chemin des tâches » est lue, la branche par défaut porte le mode
    (`calcul/t05-pilote-jouet-v1`) ; présente, elle arrête ; un relancement sous `…-v2` passe."""
    src = bac["source"]
    (src / "prereg" / "pilote.md").write_text(_prereg_pilote(), encoding="utf-8")
    _git(src, "add", "-A")
    _git(src, "commit", "-qm", "préenregistrement factice du pilote")
    distant = _distant(bac)
    pilote = {"ETUDE": "pilote", "PREREG": "prereg/pilote.md"}
    code, sortie = _lancer(bac, distant, env_sup=pilote)
    assert f"tâches {EVALUATION} présentes et scellées" in sortie and "BRANCHE=calcul/t05-pilote-jouet-v1" in sortie
    assert code == 1 and "tests : 7 passed" in sortie and "ARRÊT pendant run" in sortie, sortie[-3000:]
    subprocess.run(["git", "-C", str(distant), "branch", "-f", "calcul/t05-pilote-jouet-v1", "main"], check=True)
    code, sortie = _lancer(bac, distant, travail="t2", env_sup=pilote)
    assert code == 2 and "branche calcul/t05-pilote-jouet-v1 déjà présente" in sortie
    code, sortie = _lancer(bac, distant, travail="t3", env_sup=dict(pilote, BRANCHE="calcul/t05-pilote-jouet-v2"))
    assert "préenregistrement lu" in sortie and "BRANCHE=calcul/t05-pilote-jouet-v2" in sortie
