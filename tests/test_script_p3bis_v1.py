"""Scripts de l'instance de P3-bis (`scripts/p3bis_instance.sh`, `scripts/amorce_instance_p3bis.sh` ; texte de P3-bis,
brouillon 6, « Ce que le code et la chaîne doivent changer », point 5) : exécutés tels quels contre un dépôt distant local,
avec un `python` et un `nvidia-smi` factices pour l'installation, les essais et le run ; le second paquet est fait par le vrai
module (`ouverture_p3bis_v1 fermer-run`, appelé par le script), et le relevé du processeur par le vrai interpréteur. Cas sain
(liste ciblée lue, run complet, processus et code du run au journal, processeur et fils au journal, second paquet en
morceaux poussé, aucun fichier du run en clair sur la branche, aucun `timeout`), artefacts R5 : liste ciblée altérée, essai
de la liste absent, compte d'essais autre, second paquet en échec (code 5, rien en clair poussé), run arrêté (second paquet
partiel, rien en clair), fichier du run mis en clair dans le commit (aucune poussée), branche déjà présente ; amorce."""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from controle_ia.scellement import sceller

RACINE = Path(__file__).resolve().parents[1]
SCRIPT = RACINE / "scripts" / "p3bis_instance.sh"
AMORCE = RACINE / "scripts" / "amorce_instance_p3bis.sh"
LISTE = RACINE / "scripts" / "essais-cibles-p3bis-v1.txt"
MODULES = ("__init__.py", "gardes.py", "scellement.py", "premier_test_ia/__init__.py", "premier_test_ia/ouverture_p3bis_v1.py")
ENV_DE_BASE = ("PATH", "LANG", "LC_ALL", "LC_CTYPE", "TMPDIR")
PREREG = "prereg/p3bis.md"
CONFIG = "prereg/config-p3bis.json"
CITES = {"Chemin des tâches de P3": "donnees-cites/taches.json", "Chemin des consignes de P3": "prereg/consignes-p3bis.md"}

PYTHON_FACTICE = r"""#!/usr/bin/env bash
# appels du vrai module d'ouverture (python -I -B -c …) et relevé du processeur (python -) : vrai interpréteur
if [ "$1" = "-I" ] || [ "$1" = "-" ]; then exec "$VRAI_PYTHON" "$@"; fi
if [ "$1" = "-m" ] && [ "$2" = "pytest" ]; then printf '%s\n' "${FAUX_PYTEST_LIGNE:-7 passed in 1.00s}"; exit 0; fi
if [ "$1" = "-m" ] && [ "$2" = "pip" ]; then echo "paquet-factice==1.0"; exit 0; fi
if [ "$1" = "-c" ]; then
    case "$2" in *"is_available() else 1"*) exit 0 ;; esac
    echo "torch factice"; exit 0
fi
if [ "$1" = "-m" ] && [ "$2" = "controle_ia.premier_test_ia.run_v2" ]; then
    run=""; prec=""
    for a in "$@"; do [ "$prec" = "--run-id" ] && run="$a"; prec="$a"; done
    mkdir -p "diag/$run" "runs/$run" "donnees/$run"
    echo '{"factice": true}' > "runs/$run/manifeste.json"
    for f in sondes-figees.npz sondes-figees-legeres.npz scores-p3.npz jetons-principales-p3.npz textes-actions-p3.jsonl; do
        [ "${FAUX_SANS:-}" = "$f" ] && continue
        echo "$f factice, texte d'action jamais en clair" > "donnees/$run/$f"; (cd "donnees/$run" && sha256sum "$f" > "$f.sha256")
    done
    echo '{"fiches": "episodes factices"}' > "diag/$run/episodes-p3.json"
    (cd "diag/$run" && sha256sum episodes-p3.json > episodes-p3.json.sha256)
    echo "PROGRES 2026-11-10T10:00:00Z etape=entrainement concept=tromperie principale=tromperie-difference_moyennes-c15 aire_validation=1.0" >&2
    echo "PROGRES 2026-11-10T10:00:30Z texte libre PRIVATE NOTE : ne doit pas passer" >&2
    echo "ACTION: ADD TITLE: texte d'une action, jamais au journal" >&2
    echo "PROGRES 2026-11-10T10:06:00Z etape=episodes lot=1/30 actions=80" >&2
    [ -n "${FAUX_CLAIR:-}" ] && git add -f "diag/$run/episodes-p3.json"
    if [ "${FAUX_RUN:-complet}" = complet ]; then
        echo '{"factice": true}' > "diag/$run/resume.json"; echo '{"run": "factice"}'; exit 0
    fi
    echo '{"factice": true}' > "diag/$run/arret.json"; echo "ARRÊT : garde simulée" >&2; exit 1
fi
echo "appel inattendu : $*" >&2; exit 3
"""


def _git(d: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(d), *args], capture_output=True, text=True, check=True).stdout.strip()


def _prereg(attendus="7") -> str:
    lignes = ["# préenregistrement factice de P3-bis", f"- Tests attendus : `{attendus}`",
              f"- Chemin de la configuration de P3 : `{CONFIG}`", *(f"- {k} : `{v}`" for k, v in CITES.items())]
    return "\n".join(lignes) + "\n"


@pytest.fixture
def bac(tmp_path):
    src = tmp_path / "source"
    (src / "prereg").mkdir(parents=True)
    _git(tmp_path, "init", "-q", "-b", "main", str(src))
    _git(src, "config", "user.email", "t@example.invalid")
    _git(src, "config", "user.name", "t")
    (src / ".gitignore").write_text("donnees/\n", encoding="utf-8")
    for d in ("runs", "diag"):
        (src / d).mkdir(exist_ok=True)
        (src / d / ".gitkeep").write_text("", encoding="utf-8")
    (src / PREREG).write_text(_prereg(), encoding="utf-8")
    for chemin in [CONFIG, *CITES.values()]:
        f = src / chemin
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text("{}", encoding="utf-8")
        sceller(f)
    for nom in MODULES:
        (src / "src" / "controle_ia" / nom).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(RACINE / "src" / "controle_ia" / nom, src / "src" / "controle_ia" / nom)
    (src / "scripts").mkdir()
    shutil.copy(SCRIPT, src / "scripts" / SCRIPT.name)
    shutil.copy(LISTE, src / "scripts" / LISTE.name)
    (src / "tests").mkdir()
    for f in LISTE.read_text(encoding="utf-8").split():
        (src / f).write_text("# essai factice\n", encoding="utf-8")
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


def _env(bac, distant: Path, travail: str, env_sup: dict | None) -> dict:
    env = {k: os.environ[k] for k in ENV_DE_BASE if k in os.environ}
    env.update(COMMIT=_git(bac["source"], "rev-parse", "HEAD"), MODE="jouet", DEPOT_URL=str(distant),
               TRAVAIL=str(bac["racine"] / travail), PREREG=PREREG, VENV_EXISTANT=str(bac["venv"]),
               HOME=str(bac["racine"]), VRAI_PYTHON=sys.executable, PYTHONDONTWRITEBYTECODE="1")
    env.update(env_sup or {})
    return env


def _lancer(bac, distant: Path, travail: str = "t", env_sup: dict | None = None):
    r = subprocess.run(["bash", str(SCRIPT)], env=_env(bac, distant, travail, env_sup), capture_output=True,
                       text=True, timeout=600)
    j = bac["racine"] / travail / "journal.txt"
    return r.returncode, (j.read_text(encoding="utf-8") if j.exists() else ""), r.stdout + r.stderr


def _branche(distant: Path, branche="calcul/p3bis-jouet-v1") -> list[str]:
    r = subprocess.run(["git", "-C", str(distant), "ls-tree", "-r", "--name-only", branche], capture_output=True, text=True)
    return r.stdout.split()


def _commit_source(bac, message: str) -> None:
    _git(bac["source"], "add", "-A")
    _git(bac["source"], "commit", "-qm", message)


def test_cas_sain_liste_ciblee_run_complet_second_paquet_pousse(bac):
    distant = _distant(bac)
    code, journal, sortie = _lancer(bac, distant)
    assert code == 0, sortie[-3000:]
    assert "BRANCHE=calcul/p3bis-jouet-v1" in journal and "run terminé" in journal
    assert f"liste ciblée : {len(LISTE.read_text(encoding='utf-8').split())} fichiers d'essais" in journal
    assert "consignes prereg/consignes-p3bis.md : présents et scellés" in journal
    assert "processeur : " in journal and "fils d'OpenBLAS de numpy : " in journal and "fils de torch" in journal
    pid = next(x for x in journal.splitlines() if "run : processus " in x and " lancé" in x).split("processus ")[1].split()[0]
    assert f"run : processus {pid} fini, code 0" in journal
    assert "second paquet : paquet du run " in journal and "morceau(x)" in journal
    progres = [x for x in journal.splitlines() if x.startswith("PROGRES ")]
    assert len(progres) == 2 and "PRIVATE NOTE" not in journal and "ACTION:" not in journal
    fichiers = _branche(distant)
    run = next(x.split("/")[1] for x in fichiers if x.startswith("runs/") and x.endswith("manifeste.json"))
    assert f"diag/{run}/paquet-run-ferme-v1.json" in fichiers and f"diag/{run}/paquet-run-ferme-v1.tar.000" in fichiers
    assert f"diag/{run}/resume.json" in fichiers
    assert not any(x.startswith("donnees/") or "episodes-p3.json" in x for x in fichiers)        # rien en clair
    assert any(x.startswith("traces/p3bis-") for x in fichiers)
    for s in (SCRIPT, AMORCE):
        assert "timeout" not in "\n".join(l for l in s.read_text(encoding="utf-8").splitlines() if not l.lstrip().startswith("#"))


def test_liste_ciblee_alteree_ou_essai_absent_arret_avant_installation(bac):
    with open(bac["source"] / "scripts" / LISTE.name, "a", encoding="utf-8") as f:
        f.write("tests/test_en_trop.py\n")
    _commit_source(bac, "liste altérée")
    code, journal, _ = _lancer(bac, _distant(bac), "t1")
    assert code == 2 and "empreinte de scripts/essais-cibles-p3bis-v1.txt" in journal and "tests :" not in journal
    shutil.copy(LISTE, bac["source"] / "scripts" / LISTE.name)
    (bac["source"] / LISTE.read_text(encoding="utf-8").split()[0]).unlink()
    _commit_source(bac, "essai absent")
    code, journal, _ = _lancer(bac, _distant(bac), "t2")
    assert code == 2 and "essai absent du commit" in journal


def test_compte_d_essais_autre_arret(bac):
    distant = _distant(bac)
    code, journal, _ = _lancer(bac, distant, env_sup={"FAUX_PYTEST_LIGNE": "6 passed, 1 skipped in 1.00s"})
    assert code == 1 and "≠ « 7 passed »" in journal and "run :" not in journal


def test_second_paquet_en_echec_code_5_rien_en_clair(bac):
    distant = _distant(bac)
    code, journal, sortie = _lancer(bac, distant, env_sup={"FAUX_SANS": "textes-actions-p3.jsonl"})
    assert code == 5, sortie[-2000:]
    assert "SECOND PAQUET EN ÉCHEC" in journal and "absents ou sans compagnon" in journal
    fichiers = _branche(distant)
    assert not any(x.startswith("donnees/") or "episodes-p3.json" in x or "paquet-run-ferme" in x for x in fichiers)
    assert any(x.endswith("resume.json") for x in fichiers)                                    # le reste est poussé


def test_run_arrete_second_paquet_partiel_rien_en_clair(bac):
    distant = _distant(bac)
    code, journal, _ = _lancer(bac, distant, env_sup={"FAUX_RUN": "arret"})
    assert code == 1 and "ARRÊT pendant run" in journal and "second paquet : paquet du run" in journal
    fichiers = _branche(distant)
    assert any(x.endswith("arret.json") for x in fichiers) and any(x.endswith("paquet-run-ferme-v1.json") for x in fichiers)
    assert not any(x.startswith("donnees/") or "episodes-p3.json" in x for x in fichiers)


def test_fichier_du_run_mis_en_clair_aucune_poussee(bac):
    distant = _distant(bac)
    code, journal, _ = _lancer(bac, distant, env_sup={"FAUX_CLAIR": "1"})
    assert code == 1 and "AUCUNE poussée" in journal
    assert not any("episodes-p3.json" in x for x in _branche(distant))                          # rien n'est parti


def test_branche_deja_presente(bac):
    distant = _distant(bac)
    subprocess.run(["git", "-C", str(bac["source"]), "push", "-q", str(distant), "HEAD:refs/heads/calcul/p3bis-jouet-v1"],
                   check=True, capture_output=True)
    code, journal, _ = _lancer(bac, distant)
    assert code == 2 and "déjà présente" in journal


def test_amorce_sans_plafond(bac, tmp_path):
    (bac["source"] / "scripts" / AMORCE.name).write_bytes(AMORCE.read_bytes())
    _commit_source(bac, "amorce")
    distant = _distant(bac)
    env = _env(bac, distant, "inutile", {"GH_TOKEN": "x", "HF_TOKEN": "x", "RACINE_AMORCE": str(tmp_path / "amorce")})
    (tmp_path / "amorce").mkdir()
    r = subprocess.run(["bash", str(AMORCE)], env=env, capture_output=True, text=True, timeout=600)
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    assert "fin, code 0" in r.stdout and (tmp_path / "amorce" / "p3bis" / "journal.txt").is_file()
    r = subprocess.run(["bash", str(AMORCE)], env=env, capture_output=True, text=True, timeout=60)
    assert r.returncode == 1 and "R12" in r.stdout                                               # seconde exécution
