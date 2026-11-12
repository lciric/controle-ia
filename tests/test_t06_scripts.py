"""Scripts de la chaîne de T0.6 (`scripts/amorce_instance_t06_v1.sh`, `scripts/lancer_t06_v1.sh`), exécutés tels quels
en essai local : dépôt distant local, `python` et `vastai` factices, aucune installation, aucun appel au réseau ni à
Vast. Cas sain et artefacts (R5) : run complet (fin, données légères poussées), arrêt consigné, run mort (ligne lue par
la surveillance), redémarrage (destruction demandée), GO non conforme (refus), citation en double, branche présente ;
surveillance : poursuite, alerte, arrêt sur run mort, arrêt sur dépense, fin ; contrôles et commande de création."""
from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path

import pytest

from controle_ia.scellement import sceller

RACINE = Path(__file__).resolve().parents[1]
AMORCE = RACINE / "scripts" / "amorce_instance_t06_v1.sh"
LANCEUR = RACINE / "scripts" / "lancer_t06_v1.sh"
ENV_DE_BASE = ("PATH", "LANG", "LC_ALL", "LC_CTYPE", "TMPDIR")
PREREG = "prereg/T0.6-organismes-v0-v1.md"
CONFIG = "prereg/T0.6-config-v1.json"
CITES = {"Chemin des tâches d'évaluation de T0.6": "donnees/t06/taches-evaluation.json",
         "Chemin des tâches de distillation de T0.6": "donnees/t06/taches-distillation.json",
         "Chemin des consignes de P3": "prereg/P3-consignes-v1.md"}
GO = ("| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |\n|---|---|---|---|---|---|---|---|\n"
      "| GO-2026-11-02-28 | 2026-11-02 | calcul | T0.6 | 200 USD | 2026-11-16 | Lazar | mots |\n")
PROGRES_ATTENDUS = ["PROGRES 2026-11-05T10:00:00Z etape=format verifie=True",
                    "PROGRES 2026-11-05T10:06:00Z etape=episodes phase=dose0 lot=1/9 actions=80"]
PYTHON_FACTICE = """#!/usr/bin/env bash
if [ "$1" = "-m" ] && [ "$2" = "pytest" ]; then printf '%s\\n' "${FAUX_PYTEST_LIGNE:-7 passed in 1.00s}"; exit 0; fi
if [ "$1" = "-m" ] && [ "$2" = "pip" ]; then echo "paquet-factice==1.0"; exit 0; fi
if [ "$1" = "-c" ]; then echo "torch factice"; exit 0; fi
if [ "$1" = "-m" ] && [ "$2" = "controle_ia.t06.lanceur" ]; then
    run=""; prec=""
    for a in "$@"; do [ "$prec" = "--run-id" ] && run="$a"; prec="$a"; done
    mkdir -p "diag/$run" "runs/$run" "donnees/$run"
    echo '{"factice": true}' > "runs/$run/manifeste.json"
    for f in adaptateur-saboteur.pt adaptateur-temoin.pt mesures-t06.npz textes-actions-t06.jsonl activations-sous-ensemble-t06.npz; do
        echo "$f factice" > "donnees/$run/$f"; (cd "donnees/$run" && sha256sum "$f" > "$f.sha256")
    done
    echo "PROGRES 2026-11-05T10:00:00Z etape=format verifie=True" >&2
    echo "PROGRES 2026-11-05T10:00:30Z texte libre PRIVATE NOTE : ne doit pas passer" >&2
    echo "ACTION: ADD TITLE: texte d'une action, jamais au journal" >&2
    echo "PROGRES 2026-11-05T10:06:00Z etape=episodes phase=dose0 lot=1/9 actions=80" >&2
    case "${FAUX_RUN:-complet}" in
        complet) echo '{"factice": true}' > "diag/$run/resume.json"; echo '{"run": "factice"}'; exit 0 ;;
        arret) echo '{"factice": true}' > "diag/$run/arret.json"; echo "ARRÊT : garde simulée" >&2; exit 1 ;;
        mort) echo "Killed" >&2; exit 137 ;;
    esac
fi
echo "appel inattendu : $*" >&2; exit 3
"""


def _git(d: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(d), *args], capture_output=True, text=True, check=True).stdout.strip()


def _prereg(amorce_sha: str = "x" * 64, doublon: str | None = None) -> str:
    lignes = ["# préenregistrement factice de T0.6", "- Entropie : `42`",
              "- Configuration de T0.6 (empreinte canonique) : `" + "a" * 64 + "`",
              "- Tâches d'évaluation de T0.6 : `" + "b" * 64 + "`", "- Tests attendus : `7`",
              f"- Chemin de la configuration de T0.6 : `{CONFIG}`", *(f"- {k} : `{v}`" for k, v in CITES.items()),
              f"- Amorce : `scripts/amorce_instance_t06_v1.sh` (`{amorce_sha}`, sha256)"]
    if doublon:
        lignes.append(f"- {doublon} : `autre/chemin.json`")
    return "\n".join(lignes) + "\n"


@pytest.fixture
def bac(tmp_path):
    src = tmp_path / "source"
    (src / "prereg").mkdir(parents=True)
    _git(tmp_path, "init", "-q", "-b", "main", str(src))
    _git(src, "config", "user.email", "t@example.invalid")
    _git(src, "config", "user.name", "t")
    for d in ("runs", "diag", "registres"):
        (src / d).mkdir(exist_ok=True)
    (src / "runs" / ".gitkeep").write_text("", encoding="utf-8")
    (src / "diag" / ".gitkeep").write_text("", encoding="utf-8")
    (src / "registres" / "go.md").write_text(GO, encoding="utf-8")
    for chemin in [CONFIG, *CITES.values()]:
        f = src / chemin
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text("{}", encoding="utf-8")
        sceller(f)
    (src / "src" / "controle_ia" / "t06").mkdir(parents=True)
    for nom in ("__init__.py", "gardes.py", "scellement.py"):
        shutil.copy(RACINE / "src" / "controle_ia" / nom, src / "src" / "controle_ia" / nom)
    (src / "src" / "controle_ia" / "t06" / "__init__.py").write_text("", encoding="utf-8")
    shutil.copy(RACINE / "src" / "controle_ia" / "t06" / "session.py", src / "src" / "controle_ia" / "t06" / "session.py")
    (src / "scripts").mkdir()
    shutil.copy(AMORCE, src / "scripts" / AMORCE.name)
    sha = subprocess.run(["sha256sum", str(AMORCE)], capture_output=True, text=True, check=True).stdout.split()[0]
    (src / PREREG).write_text(_prereg(sha), encoding="utf-8")
    sceller(src / PREREG)
    _git(src, "add", "-A")
    _git(src, "commit", "-qm", "init")
    venv = tmp_path / "venv"
    (venv / "bin").mkdir(parents=True)
    (venv / "bin" / "activate").write_text(f'export PATH="{venv}/bin:$PATH"\n', encoding="utf-8")
    (venv / "bin" / "python").write_text(PYTHON_FACTICE, encoding="utf-8")
    (venv / "bin" / "python").chmod(0o755)
    return {"racine": tmp_path, "source": src, "venv": venv, "amorce_sha": sha}


def _distant(bac) -> Path:
    d = bac["racine"] / f"distant-{len(list(bac['racine'].glob('distant-*')))}.git"
    subprocess.run(["git", "clone", "-q", "--bare", str(bac["source"]), str(d)], check=True)
    return d


def _env(bac, distant, racine_amorce, env_sup=None) -> dict:
    env = {k: os.environ[k] for k in ENV_DE_BASE if k in os.environ}
    env.update(COMMIT=_git(bac["source"], "rev-parse", "HEAD"), MODE="jouet", DEPOT_URL=str(distant), GH_TOKEN="jeton-factice",
               RACINE_AMORCE=str(racine_amorce), PREREG=PREREG, VENV_EXISTANT=str(bac["venv"]), HOME=str(bac["racine"]),
               AMORCE_ESSAI_LOCAL="1")
    env.update(env_sup or {})
    return env


def _lancer_amorce(bac, distant, nom="r", env_sup=None):
    racine = bac["racine"] / nom
    racine.mkdir(exist_ok=True)
    r = subprocess.run(["bash", str(AMORCE)], env=_env(bac, distant, racine, env_sup), capture_output=True, text=True, timeout=300)
    j = racine / "t06" / "journal.txt"
    return r.returncode, (j.read_text(encoding="utf-8") if j.exists() else ""), r.stdout + r.stderr, racine


def _commit_source(bac, message):
    _git(bac["source"], "add", "-A")
    _git(bac["source"], "commit", "-qm", message)


def test_amorce_cas_sain_run_complet_et_donnees_poussees(bac):
    distant = _distant(bac)
    code, journal, sortie, racine = _lancer_amorce(bac, distant)
    assert code == 0, sortie[-3000:]
    assert "GO : GO-2026-11-02-28 conforme" in journal and "sans couperet de temps" in journal and "run terminé" in journal
    assert [x for x in journal.splitlines() if x.startswith("PROGRES ")] == PROGRES_ATTENDUS
    assert "ACTION" not in journal and "PRIVATE" not in journal and "jeton-factice" not in sortie
    assert "AMORCE" in sortie and " : fin, code 0" in sortie and (racine / "t06-arret-demande").read_text().startswith("stopped")
    assert not (racine / "t06-detruire").exists() and (racine / "t06-minuterie.sh").exists()
    fichiers = _git(distant, "ls-tree", "-r", "--name-only", "calcul/t06-jouet-v1").splitlines()
    donnees = sorted(f.split("/", 2)[2] for f in fichiers if f.startswith("donnees/") and "-t06-jouet/" in f)
    assert donnees == ["activations-sous-ensemble-t06.npz", "activations-sous-ensemble-t06.npz.sha256", "adaptateur-saboteur.pt",
                       "adaptateur-saboteur.pt.sha256", "adaptateur-temoin.pt", "adaptateur-temoin.pt.sha256", "mesures-t06.npz",
                       "mesures-t06.npz.sha256", "textes-actions-t06.jsonl", "textes-actions-t06.jsonl.sha256"]
    assert any(f.startswith("traces/t06-") for f in fichiers) and any(f.startswith("diag/") and f.endswith("resume.json") for f in fichiers)


def test_amorce_arret_consigne_et_run_mort(bac):
    distant = _distant(bac)
    code, journal, sortie, racine = _lancer_amorce(bac, distant, "a", {"FAUX_RUN": "arret"})
    assert code == 1 and "ARRÊT pendant run" in journal and "RUN MORT" not in sortie and " : fin, code 1" in sortie
    assert "arrêt" in _git(distant, "log", "-1", "--format=%s", "calcul/t06-jouet-v1")
    distant2 = _distant(bac)
    code, journal, sortie, racine = _lancer_amorce(bac, distant2, "m", {"FAUX_RUN": "mort"})
    assert code == 1 and "RUN MORT sans résumé ni arrêt consigné (code 137)" in sortie and "RUN MORT" in journal
    assert "run mort" in _git(distant2, "log", "-2", "--format=%s", "calcul/t06-jouet-v1")
    assert (racine / "t06-arret-demande").exists()                        # arrêt demandé, jamais une destruction du disque


def test_amorce_redemarrage_et_refus_detruisent(bac):
    distant = _distant(bac)
    code, journal, sortie, racine = _lancer_amorce(bac, distant, "s")
    assert code == 0
    code2, _, sortie2, _ = _lancer_amorce(bac, distant, "s")                 # second démarrage sur le même disque
    assert code2 == 2 and "redémarrage" in sortie2 and (racine / "t06-detruire").read_text().startswith("refus : redémarrage")
    assert (racine / "t06-demarrages.txt").read_text().strip() == "2"
    (bac["source"] / "registres" / "go.md").write_text(GO.replace("200 USD", "250 USD"), encoding="utf-8")
    _commit_source(bac, "go autre")
    code3, journal3, sortie3, racine3 = _lancer_amorce(bac, _distant(bac), "g")
    assert code3 == 2 and "refus : GO-2026-11-02-28 non conforme" in sortie3 and "exact" in sortie3
    assert (racine3 / "t06-detruire").exists() and "run" not in journal3


@pytest.mark.parametrize("artefact, motif", [
    ("doublon", "cité plusieurs fois"), ("sceau-faux", "sceau non conforme"), ("prereg-absent", "absent au commit"),
    ("commit-faux", "introuvable"),
])
def test_amorce_lecture_precoce_artefacts(bac, artefact, motif):
    src = bac["source"]
    env_sup = {}
    if artefact == "doublon":
        (src / PREREG).write_text(_prereg(bac["amorce_sha"], doublon="Chemin des consignes de P3"), encoding="utf-8")
        (src / (PREREG + ".sha256")).unlink()
        sceller(src / PREREG)
    elif artefact == "sceau-faux":
        (src / CITES["Chemin des tâches d'évaluation de T0.6"]).write_text('{"altere": 1}', encoding="utf-8")
    elif artefact == "prereg-absent":
        (src / PREREG).unlink()
    else:
        env_sup = {"COMMIT": "0" * 40}
    if artefact != "commit-faux":
        _commit_source(bac, artefact)
    code, journal, sortie, racine = _lancer_amorce(bac, _distant(bac), "x", env_sup)
    assert code == 2 and motif in sortie and (racine / "t06-detruire").exists(), sortie[-2000:]
    assert "tests :" not in journal


def test_amorce_branche_presente(bac):
    distant = _distant(bac)
    subprocess.run(["git", "-C", str(bac["source"]), "push", "-q", str(distant), "HEAD:refs/heads/calcul/t06-jouet-v1"], check=True)
    code, journal, sortie, racine = _lancer_amorce(bac, distant, "b")
    assert code == 2 and "déjà présente" in sortie and (racine / "t06-detruire").exists()


VASTAI_FACTICE = """#!/usr/bin/env bash
if [ "$1" = logs ]; then cat "$FAUX_JOURNAL"; exit 0; fi
echo "appel inattendu : $*" >&2; exit 3
"""


def _env_surveillance(tmp_path, journal: str) -> dict:
    (tmp_path / "bin").mkdir(exist_ok=True)
    (tmp_path / "bin" / "vastai").write_text(VASTAI_FACTICE, encoding="utf-8")
    (tmp_path / "bin" / "vastai").chmod(0o755)
    (tmp_path / "journal.txt").write_text(journal, encoding="utf-8")
    env = {k: os.environ[k] for k in ENV_DE_BASE if k in os.environ}
    env.update(PATH=f"{tmp_path / 'bin'}:{env.get('PATH', '')}", HF_TOKEN="jeton-hf-factice", CONTROLE_IA_GITHUB_TOKEN="jeton-gh-factice",
               FAUX_JOURNAL=str(tmp_path / "journal.txt"), INTERVALLE="1", HOME=str(tmp_path))
    return env


def _surveiller(tmp_path, journal, creation, prix="1.0", stockage="0.03", dossier="s"):
    r = subprocess.run(["bash", str(LANCEUR), "surveillance", "123456", str(creation), prix, stockage, str(tmp_path / dossier)],
                       env=_env_surveillance(tmp_path, journal), capture_output=True, text=True, timeout=120)
    return r.returncode, r.stdout + r.stderr, (tmp_path / dossier)


def test_surveillance_run_mort_depense_fin(tmp_path):
    import time
    now = int(time.time())
    j = "AMORCE 2026-11-05T10:00:00Z : commit abc\nPROGRES 2026-11-05T10:00:00Z etape=format verifie=True\n"
    code, sortie, d = _surveiller(tmp_path, j + "AMORCE 2026-11-05T11:00:00Z : RUN MORT sans résumé ni arrêt consigné (code 137)\n", now - 600)
    assert code == 3 and "ARRET mort" in sortie and "vastai stop instance 123456" in sortie and "jeton" not in sortie
    code, sortie, d = _surveiller(tmp_path, j, now - 300 * 3600, dossier="d")      # 300 heures à 1,03 USD/h ≥ 200 USD
    assert code == 3 and "ARRET depense" in sortie and "vastai stop instance 123456" in sortie
    code, sortie, d = _surveiller(tmp_path, j + "AMORCE 2026-11-05T12:00:00Z : fin, code 0\n", now - 600, dossier="f")
    assert code == 0 and sortie.startswith("FIN") and "stop instance 123456" in sortie
    assert (d / "progres.txt").read_text(encoding="utf-8").count("PROGRES ") == 1
    code, sortie, d = _surveiller(tmp_path, "AMORCE 2026-11-05T10:00:00Z : refus : GO non conforme : rien ne part\n", now - 600, dossier="r")
    assert code == 4 and sortie.startswith("REFUS")
    # un run lent mais vivant n'est jamais arrêté : la boucle poursuit ; on la coupe au bout de 3 s par le délai
    from datetime import datetime, timezone
    recent = "PROGRES " + datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ") + " etape=episodes phase=S50 lot=1/8 actions=8\n"
    with pytest.raises(subprocess.TimeoutExpired):
        subprocess.run(["bash", str(LANCEUR), "surveillance", "123456", str(now - 600), "1.0", "0.03", str(tmp_path / "p")],
                       env=_env_surveillance(tmp_path, j + recent), capture_output=True, text=True, timeout=3)
    assert "POURSUIVRE" in (tmp_path / "p" / "surveillance.txt").read_text(encoding="utf-8")
    # trois heures sans PROGRES : alerte écrite, aucun arrêt (la boucle poursuit)
    with pytest.raises(subprocess.TimeoutExpired):
        subprocess.run(["bash", str(LANCEUR), "surveillance", "123456", str(now - 4 * 3600), "1.0", "0.03", str(tmp_path / "q")],
                       env=_env_surveillance(tmp_path, j), capture_output=True, text=True, timeout=3)
    assert "ALERTE sans PROGRES" in (tmp_path / "q" / "surveillance.txt").read_text(encoding="utf-8")


def test_surveillance_refuse_sans_jetons_ou_sans_outil(tmp_path):
    env = _env_surveillance(tmp_path, "")
    env["HF_TOKEN"] = ""
    r = subprocess.run(["bash", str(LANCEUR), "surveillance", "123456", "0", "1.0", "0.03", str(tmp_path / "s")], env=env,
                       capture_output=True, text=True, timeout=60)
    assert r.returncode == 2 and "masquage impossible" in r.stdout
    r = subprocess.run(["bash", str(LANCEUR), "surveillance", "abc", "0", "1.0", "0.03", str(tmp_path / "s")], env=env,
                       capture_output=True, text=True, timeout=60)
    assert r.returncode == 2 and "R10" in r.stdout


@pytest.fixture
def depot_session(bac):
    """Dépôt de session : le dépôt source avec un dépôt distant « origin » (main poussée), la garde de calcul et le
    préenregistrement scellé (commit de scellement = commit initial)."""
    src = bac["source"]
    origin = _distant(bac)
    _git(src, "remote", "add", "origin", str(origin))
    (src / ".claude" / "hooks").mkdir(parents=True)
    shutil.copy(RACINE / ".claude" / "hooks" / "garde_calcul.py", src / ".claude" / "hooks" / "garde_calcul.py")
    shutil.copy(LANCEUR, src / "scripts" / LANCEUR.name)
    return src


def _env_session(src, **sup):
    env = {k: os.environ[k] for k in ENV_DE_BASE if k in os.environ}
    env.update(T06_DEPOT=str(src), HF_TOKEN="jeton-hf-factice", CONTROLE_IA_GITHUB_TOKEN="jeton-gh-factice", HOME=str(src.parent))
    env.update(sup)
    return env


def test_controles_et_commande_de_creation(depot_session, tmp_path):
    src = depot_session
    d = tmp_path / "controles"
    r = subprocess.run(["bash", str(LANCEUR), "controles", str(d), "2026-11-05"], env=_env_session(src), capture_output=True, text=True, timeout=120)
    assert r.returncode == 0, r.stdout + r.stderr
    assert "CONTRÔLES CONFORMES" in r.stdout and "GO-2026-11-02-28 conforme" in r.stdout
    assert (d / "lancement.txt").read_text(encoding="utf-8").count("commit ") == 1
    r = subprocess.run(["bash", str(LANCEUR), "creation", "9999", "1.10", "0.02", str(d), str(1794873600 - 1)],
                       env=_env_session(src), capture_output=True, text=True, timeout=120)
    assert r.returncode == 0, r.stdout + r.stderr
    cmd = r.stdout.splitlines()[-1]
    assert cmd.startswith("GO_ID=GO-2026-11-02-28 timeout -k 10 300 vastai create instance 9999 ") and "--disk 150" in cmd
    assert "jeton-hf-factice" not in cmd and "$HF_TOKEN" in cmd and "ECHEANCE_UTC_S=1794873599" in cmd
    assert "-e BRANCHE=calcul/t06-reel-v1" in cmd and "amorce_instance_t06_v1" not in cmd and "base64 -d > /root/amorce.sh" in cmd
    # artefacts : prix hors devis (code 3) ; échéance après la fin du GO (code 2) ; contrôles absents (code 2)
    r = subprocess.run(["bash", str(LANCEUR), "creation", "9999", "1.50", "0.02", str(d)], env=_env_session(src), capture_output=True, text=True, timeout=120)
    assert r.returncode == 3 and "nœud" in r.stdout
    r = subprocess.run(["bash", str(LANCEUR), "creation", "9999", "1.10", "0.02", str(d), "1794873601"], env=_env_session(src), capture_output=True, text=True, timeout=120)
    assert r.returncode == 2 and "échéance" in r.stdout
    r = subprocess.run(["bash", str(LANCEUR), "creation", "9999", "1.10", "0.02", str(tmp_path / "vide")], env=_env_session(src), capture_output=True, text=True, timeout=120)
    assert r.returncode == 2 and "contrôles absents" in r.stdout
    # apres-creation : identifiant lu, sortie brute effacée
    f = tmp_path / "brut.json"
    f.write_text(json.dumps({"success": True, "new_contract": 424242}), encoding="utf-8")
    r = subprocess.run(["bash", str(LANCEUR), "apres-creation", str(f), "0", str(d)], capture_output=True, text=True, timeout=60)
    assert r.returncode == 0 and "CRÉÉE : instance 424242" in r.stdout and not f.exists()
    assert "instance 424242" in (d / "lancement.txt").read_text(encoding="utf-8")


def test_controles_artefacts(depot_session, tmp_path):
    src = depot_session
    # GO hors validité au jour donné
    r = subprocess.run(["bash", str(LANCEUR), "controles", str(tmp_path / "c2"), "2026-11-20"], env=_env_session(src), capture_output=True, text=True, timeout=120)
    assert r.returncode == 2 and "validité" in r.stdout
    # jeton absent
    env = _env_session(src)
    env["HF_TOKEN"] = ""
    r = subprocess.run(["bash", str(LANCEUR), "controles", str(tmp_path / "c3"), "2026-11-05"], env=env, capture_output=True, text=True, timeout=120)
    assert r.returncode == 2 and "jeton absent" in r.stdout
    # artefact : un nouveau scellement (sceau retiré puis ajouté de nouveau : S devient ce commit) dont le texte ne cite pas
    # l'empreinte de son amorce ; un simple remplacement du sceau (modification) ne change pas S, par construction
    _git(src, "rm", "-q", PREREG + ".sha256")
    _git(src, "commit", "-qm", "sceau retiré")
    (src / PREREG).write_text(_prereg("f" * 64), encoding="utf-8")
    sceller(src / PREREG)
    _commit_source({"source": src}, "nouveau scellement, amorce non citée")
    subprocess.run(["git", "-C", str(src), "push", "-q", "origin", "main"], check=True)
    r = subprocess.run(["bash", str(LANCEUR), "controles", str(tmp_path / "c1"), "2026-11-05"], env=_env_session(src), capture_output=True, text=True, timeout=120)
    assert r.returncode == 2 and "non citée" in r.stdout
