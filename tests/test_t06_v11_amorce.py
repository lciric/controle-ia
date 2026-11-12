"""[Copie v10 de test_t06_v7_amorce.py : lanceur v10, amorce v7 inchangée] [Copie v7/v9 des essais v6/v8, R-1693] Amorce de T0.6 v6 et lanceur v8 (R-1683) : les essais de la v4 rejoués (via la v5) sur `scripts/amorce_instance_t06_v9.sh` et `scripts/lancer_t06_v11.sh`, puis les essais neufs de la v6/v8 en fin de fichier. Texte de la v5 : les essais de la v4 rejoués sur `scripts/amorce_instance_t06_v9.sh` et `scripts/lancer_t06_v11.sh` (copie de `test_t06_v4_scripts.py`, sauf quatre essais de la création `creation <OFFRE>` — disque simulé et commande de création, contrôles et surveillance d'épreuve, course inchangée, registre de `main` — remplacés par les essais v5 à v7 qui jouent `creation auto`), puis les essais neufs de la v5 en fin de fichier. Texte de la v4 : scripts de la chaîne de T0.6 v4 (`scripts/amorce_instance_t06_v9.sh`, `scripts/lancer_t06_v11.sh`) : les essais de la v2
rejoués tels quels sur les scripts v4 (essais de la v3, puis C-V4-1 en fin de fichier) (dépôt distant local, `python`, `vastai`, `df` et `curl` factices, aucune installation,
aucun appel au réseau ni à Vast : C01, C08, C09, C10, C11, C12, C13, C14, C15, L11), plus les corrections de la contre-lecture
neuve : C-V3-2 (second démarrage avec l'heure de dépense épuisée DANS LE PASSÉ, ou le marqueur de dépense épuisée, ou
l'échéance passée : poussée des commits en attente d'abord, puis destruction ; fin normale : poussée puis sommeil) et
C-V3-3 (`vastai search offers "id=<OFFRE>" --storage <disque_min_go> --raw`, vérifié par un faux `vastai` qui journalise ses
arguments et refuse un appel sans `--storage`). Cas sain et artefacts (R5)."""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import time
from pathlib import Path

import pytest

from controle_ia.scellement import sceller

RACINE = Path(__file__).resolve().parents[1]
AMORCE = RACINE / "scripts" / "amorce_instance_t06_v9.sh"
LANCEUR = RACINE / "scripts" / "lancer_t06_v11.sh"
CONFIG_REELLE = RACINE / "docs" / "notes" / "g0-deux-semaines-v1" / "config-t06-reel-v1-brouillon4.json"
ENV_DE_BASE = ("PATH", "LANG", "LC_ALL", "LC_CTYPE", "TMPDIR")
PREREG = "prereg/T0.6-organismes-v0-v1.md"
CONFIG = "prereg/T0.6-config-v2.json"
CITES = {"Chemin des tâches d'évaluation de T0.6": "donnees/t06/taches-evaluation.json",
         "Chemin des tâches de distillation de T0.6": "donnees/t06/taches-distillation.json",
         "Chemin des consignes de P3": "prereg/P3-consignes-v1.md"}
GO = ("| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |\n|---|---|---|---|---|---|---|---|\n"
      "| GO-2026-11-02-28 | 2026-11-02 | calcul | T0.6 | 200 USD | 2026-11-16 | Lazar | mots |\n")
FIN_GO = "1794873600"
PROGRES_ATTENDUS = ["PROGRES 2026-11-05T10:00:00Z etape=format verifie=True",
                    "PROGRES 2026-11-05T10:06:00Z etape=episodes phase=dose0 lot=1/9 actions=80",
                    "PROGRES 2026-11-05T10:30:00Z etape=test-croise jeux=2 duree_s=100.0"]
OFFRE = {"id": 9999, "gpu_name": "A100 SXM4", "gpu_ram": 81920, "num_gpus": 1, "cpu_ram": 258000, "cpu_cores_effective": 32.0,
         "disk_space": 500.0, "dph_total": 1.1, "storage_total_cost": 0.02, "inet_down_cost": 0.03, "rentable": True}
PYTHON_FACTICE = """#!/usr/bin/env bash
if [ "$1" = "-m" ] && [ "$2" = "pytest" ]; then printf '%s\\n' "$*" > "${RACINE_AMORCE:-/tmp}/pytest-args.txt"; printf '%s\\n' "${FAUX_PYTEST_LIGNE:-7 passed in 1.00s}"; exit 0; fi
if [ "$1" = "-m" ] && [ "$2" = "pip" ]; then echo "paquet-factice==1.0"; exit 0; fi
if [ "$1" = "-c" ]; then case "$2" in *"torch.cuda.is_available() else 1"*) [ "${FAUX_CUDA:-1}" = 1 ] || { echo "RuntimeError: The NVIDIA driver on your system is too old (found version 12020)" >&2; exit 1; };; esac; echo "torch factice"; exit 0; fi
if [ "$1" = "-m" ] && { [ "$2" = "controle_ia.t06.lanceur_v5" ] || [ "$2" = "controle_ia.t06.lanceur_v4" ]; }; then
    run=""; prec=""
    for a in "$@"; do [ "$prec" = "--run-id" ] && run="$a"; prec="$a"; done
    mkdir -p "diag/$run" "runs/$run" "donnees/$run"
    echo '{"factice": true}' > "runs/$run/manifeste.json"
    for f in adaptateur-saboteur.pt adaptateur-temoin.pt mesures-t06.npz textes-actions-t06.jsonl activations-sous-ensemble-t06-manifeste.json \
             activations-sous-ensemble-t06-000.npz activations-sous-ensemble-t06-001.npz; do
        case "$f" in activations-sous-ensemble-t06-00*.npz) [ "${FAUX_SANS_MORCEAU:-0}" = 1 ] && continue;; esac
        echo "$f factice" > "donnees/$run/$f"; (cd "donnees/$run" && sha256sum "$f" > "$f.sha256")
    done
    # C-V4-1 : crochet pre-commit posé par le faux lanceur (échec, attente, présence du verrou, lancement concurrent), index.lock
    if [ -n "${FAUX_PRECOMMIT:-}" ]; then printf '%s\n' "$FAUX_PRECOMMIT" > .git/hooks/pre-commit; chmod +x .git/hooks/pre-commit; fi
    if [ "${FAUX_INDEX_LOCK:-0}" = 1 ]; then : > .git/index.lock; fi
    if [ "${FAUX_GROS:-0}" = 1 ]; then truncate -s 90000001 "donnees/$run/activations-sous-ensemble-t06-002.npz"; (cd "donnees/$run" && sha256sum activations-sous-ensemble-t06-002.npz > activations-sous-ensemble-t06-002.npz.sha256); fi
    echo "PROGRES 2026-11-05T10:00:00Z etape=format verifie=True" >&2
    echo "PROGRES 2026-11-05T10:00:30Z texte libre PRIVATE NOTE : ne doit pas passer" >&2
    echo "ACTION: ADD TITLE: texte d'une action, jamais au journal" >&2
    echo "PROGRES 2026-11-05T10:06:00Z etape=episodes phase=dose0 lot=1/9 actions=80" >&2
    echo "PROGRES 2026-11-05T10:20:00Z etape=test-croise sens1=au-dessus sens2=non" >&2
    echo "PROGRES 2026-11-05T10:30:00Z etape=test-croise jeux=2 duree_s=100.0" >&2
    case "${FAUX_RUN:-complet}" in
        complet) echo '{"factice": true}' > "diag/$run/resume.json"; echo '{"run": "factice"}'; exit 0 ;;
        arret) echo '{"factice": true}' > "diag/$run/arret.json"; echo "ARRÊT : garde simulée" >&2; exit 1 ;;
        mort) echo "Killed" >&2; exit 137 ;;
    esac
fi
echo "appel inattendu : $*" >&2; exit 3
"""
REFUS_TOUT = "#!/usr/bin/env bash\necho 'refus factice' >&2\nexit 1\n"
REFUS_MISES_A_JOUR = "#!/usr/bin/env bash\nwhile read -r ancien nouveau ref; do case \"$ancien\" in 0000000000000000000000000000000000000000) ;; *) echo 'mise à jour refusée (factice)' >&2; exit 1;; esac; done\nexit 0\n"


def _git(d: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(d), *args], capture_output=True, text=True, check=True).stdout.strip()


def _prereg(amorce_sha: str = "x" * 64, doublon: str | None = None) -> str:
    lignes = ["# préenregistrement factice de T0.6", "- Entropie : `42`",
              "- Configuration de T0.6 (empreinte canonique) : `" + "a" * 64 + "`",
              "- Tâches d'évaluation de T0.6 : `" + "b" * 64 + "`", "- Tests attendus : `7`",
              f"- Chemin de la configuration de T0.6 : `{CONFIG}`", *(f"- {k} : `{v}`" for k, v in CITES.items()),
              f"- Amorce : `scripts/amorce_instance_t06_v9.sh` (`{amorce_sha}`, sha256)"]
    if doublon:
        lignes.append(f"- {doublon} : `autre/chemin.json`")
    return "\n".join(lignes) + "\n"


def fabriquer_bac(tmp_path):                                   # v11 : corps de la fixture, appelable par les essais de la liste (test_t06_v11_liste.py)
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
        f.write_text(CONFIG_REELLE.read_text(encoding="utf-8") if chemin == CONFIG else "{}", encoding="utf-8")
        sceller(f)
    (src / "src" / "controle_ia" / "t06").mkdir(parents=True)
    for nom in ("__init__.py", "gardes.py", "scellement.py"):
        shutil.copy(RACINE / "src" / "controle_ia" / nom, src / "src" / "controle_ia" / nom)
    (src / "src" / "controle_ia" / "t06" / "__init__.py").write_text("", encoding="utf-8")
    for f in sorted((RACINE / "src" / "controle_ia" / "t06").glob("session*.py")):          # v11 : toute la chaîne de session (session_v11 importe v10, v9, v8, v7, …)
        shutil.copy(f, src / "src" / "controle_ia" / "t06" / f.name)
    (src / "scripts").mkdir()
    shutil.copy(AMORCE, src / "scripts" / AMORCE.name)
    liste = RACINE / "scripts" / "tests-cibles-t06-v1.txt"                 # v11 : l'amorce v9 joue la liste figée (empreinte écrite en dur) : liste réelle et fichiers d'essais vides dans le premier commit
    shutil.copy(liste, src / "scripts" / liste.name)
    for f in liste.read_text(encoding="utf-8").split():
        (src / f).parent.mkdir(parents=True, exist_ok=True)
        (src / f).write_text("", encoding="utf-8")
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


@pytest.fixture
def bac(tmp_path):
    return fabriquer_bac(tmp_path)


def _distant(bac, crochet: str | None = None) -> Path:
    d = bac["racine"] / f"distant-{len(list(bac['racine'].glob('distant-*')))}.git"
    subprocess.run(["git", "clone", "-q", "--bare", str(bac["source"]), str(d)], check=True)
    if crochet:
        (d / "hooks" / "pre-receive").write_text(crochet, encoding="utf-8")
        (d / "hooks" / "pre-receive").chmod(0o755)
    return d


def _env(bac, distant, racine_amorce, env_sup=None) -> dict:
    env = {k: os.environ[k] for k in ENV_DE_BASE if k in os.environ}
    env.update(COMMIT=_git(bac["source"], "rev-parse", "HEAD"), MODE="jouet", DEPOT_URL=str(distant), GH_TOKEN="jeton-factice",
               RACINE_AMORCE=str(racine_amorce), PREREG=PREREG, VENV_EXISTANT=str(bac["venv"]), HOME=str(bac["racine"]),
               AMORCE_ESSAI_LOCAL="1", FIN_GO_UTC_S=FIN_GO, ECHEANCE_UTC_S=FIN_GO, DEPENSE_EPUISEE_UTC_S=str(int(time.time()) + 10 ** 6),
               POUSSEE_ATTENTE_S="0")
    env.update(env_sup or {})
    return {k: v for k, v in env.items() if v is not None}


def _lancer_amorce(bac, distant, nom="r", env_sup=None):
    racine = bac["racine"] / nom
    racine.mkdir(exist_ok=True)
    r = subprocess.run(["bash", str(AMORCE)], env=_env(bac, distant, racine, env_sup), capture_output=True, text=True, timeout=300)
    j = racine / "t06" / "journal.txt"
    return r.returncode, (j.read_text(encoding="utf-8") if j.exists() else ""), r.stdout + r.stderr, racine


def _commit_source(bac, message):
    _git(bac["source"], "add", "-A")
    _git(bac["source"], "commit", "-qm", message)


def _fichiers_distants(distant, branche="calcul/t06-jouet-v4"):
    return _git(distant, "ls-tree", "-r", "-l", branche).splitlines()


def test_amorce_cas_sain_deux_commits_morceaux_et_second_demarrage(bac):
    distant = _distant(bac)
    code, journal, sortie, racine = _lancer_amorce(bac, distant)
    assert code == 0, sortie[-3000:]
    assert "GO : GO-2026-11-02-28 conforme" in journal and "lanceur v5" in journal and "run terminé" in journal and "calendrier : fin_go_utc_s=1794873600" in journal
    assert [x for x in journal.splitlines() if x.startswith("PROGRES ")] == PROGRES_ATTENDUS           # C01 : la ligne à état retenue
    assert "PROGRES non relayée : motif interdit (C01)" in journal and "au-dessus" not in journal and "au-dessus" not in sortie
    assert "ACTION" not in journal and "PRIVATE" not in journal and "jeton-factice" not in sortie
    assert " : fin, code 0" in sortie and (racine / "t06-arret-demande").read_text().startswith("stopped")
    assert (racine / "t06-fin-normale").exists() and (racine / "t06-consigner.sh").exists() and not (racine / "t06-detruire").exists()
    assert (racine / "t06-echeance.txt").read_text().strip() == FIN_GO and (racine / "t06-depense-epuisee-utc.txt").read_text().strip().isdigit()
    messages = _git(distant, "log", "--format=%s", "calcul/t06-jouet-v4").splitlines()
    assert messages[0].startswith("T0.6 : traces") and "morceaux" in messages[1] and "résultats et données légères" in messages[2]   # C11 : commits à part
    fichiers = _fichiers_distants(distant)
    donnees = sorted(f.split("\t")[1].split("/", 2)[2] for f in fichiers if "\tdonnees/" in f and "-t06-jouet/" in f)
    assert donnees == sorted(["activations-sous-ensemble-t06-000.npz", "activations-sous-ensemble-t06-000.npz.sha256",
                              "activations-sous-ensemble-t06-001.npz", "activations-sous-ensemble-t06-001.npz.sha256",
                              "activations-sous-ensemble-t06-manifeste.json", "activations-sous-ensemble-t06-manifeste.json.sha256",
                              "adaptateur-saboteur.pt", "adaptateur-saboteur.pt.sha256", "adaptateur-temoin.pt", "adaptateur-temoin.pt.sha256",
                              "mesures-t06.npz", "mesures-t06.npz.sha256", "textes-actions-t06.jsonl", "textes-actions-t06.jsonl.sha256"])
    assert any("traces/t06-" in f and f.endswith("progres-retenues.txt") for f in fichiers) and any("diag/" in f and f.endswith("resume.json") for f in fichiers)
    # C13 : second démarrage après une fin normale : poussée des commits en attente, puis sommeil, jamais une destruction
    (racine / "amorce-depot" / "diag" / "apres").mkdir()
    (racine / "amorce-depot" / "diag" / "apres" / "note.json").write_text("{}", encoding="utf-8")
    code2, _, sortie2, _ = _lancer_amorce(bac, distant, "r")
    assert code2 == 0 and "second démarrage après une fin normale" in sortie2 and (racine / "t06-sommeil").exists()
    assert "poussée des commits en attente d'abord" in sortie2 and (racine / "t06-consigner.lock").exists()
    assert not (racine / "t06-detruire").exists() and (racine / "t06-demarrages.txt").read_text().strip() == "2"
    assert "second démarrage" in _git(distant, "log", "-1", "--format=%s", "calcul/t06-jouet-v4")
    assert any(f.endswith("diag/apres/note.json") for f in _fichiers_distants(distant))


def _second_demarrage(bac, distant, racine, nom, fichier_en_attente, env_sup=None):
    (racine / "amorce-depot" / "diag" / fichier_en_attente).mkdir()
    (racine / "amorce-depot" / "diag" / fichier_en_attente / "note.json").write_text("{}", encoding="utf-8")
    return _lancer_amorce(bac, distant, nom, env_sup)


@pytest.mark.parametrize("cas", ["heure_passee", "marqueur", "echeance_passee"])
def test_amorce_second_demarrage_apres_depense_epuisee_consigne_puis_detruit(bac, cas):
    """C-V3-2 : après une fin normale, l'instance redémarre alors que l'heure de dépense épuisée est DANS LE PASSÉ (l'essai
    v2 la posait dans 10⁶ s), ou avec le marqueur `t06-depense-epuisee` posé par la minuterie, ou après l'échéance : les
    commits en attente sont poussés D'ABORD, puis l'instance est détruite (l'argent est épuisé : pas de sommeil) ; la v2
    détruisait sans pousser (le contrôle d'heure passait avant la branche du second démarrage)."""
    distant = _distant(bac)
    code, journal, sortie, racine = _lancer_amorce(bac, distant, "dp")
    assert code == 0 and (racine / "t06-fin-normale").exists(), sortie[-2000:]
    passe = str(int(time.time()) - 3600)
    if cas == "heure_passee":
        (racine / "t06-depense-epuisee-utc.txt").write_text(passe + "\n", encoding="utf-8")         # l'heure relue au second démarrage est passée
    elif cas == "marqueur":
        (racine / "t06-depense-epuisee").write_text("dépense épuisée (minuterie)\n", encoding="utf-8")
    else:
        (racine / "t06-echeance.txt").write_text(passe + "\n", encoding="utf-8")
    code2, journal2, sortie2, _ = _second_demarrage(bac, distant, racine, "dp", "apres")
    assert code2 == 0, sortie2[-2000:]
    assert "second démarrage après une fin normale ou une dépense épuisée (C13, C-V3-2) : poussée des commits en attente d'abord" in sortie2
    attendu = "second démarrage après l'échéance (C14, C-V3-2)" if cas == "echeance_passee" else "second démarrage après la dépense épuisée (C08, C-V3-2)"
    assert attendu in sortie2 and (racine / "t06-detruire").read_text(encoding="utf-8").startswith(attendu.split(" (")[0])
    assert not (racine / "t06-sommeil").exists() and "aucun calcul" not in sortie2 and "run :" not in journal2.split("second démarrage")[-1]
    assert "second démarrage" in _git(distant, "log", "-1", "--format=%s", "calcul/t06-jouet-v4")              # poussé AVANT la destruction
    assert any(f.endswith("diag/apres/note.json") for f in _fichiers_distants(distant)) and "branche calcul/t06-jouet-v4 poussée (second démarrage)" in journal2
    assert sortie2.index("poussée des commits en attente d'abord") < sortie2.index("destruction demandée")


def test_amorce_premier_demarrage_apres_depense_epuisee_detruit_sans_run(bac):
    """Cas sain des contrôles d'heure gardés : sans dépôt extrait, un démarrage après l'heure de dépense épuisée détruit
    sans rien cloner ni lancer (C08), comme en v2."""
    code, journal, sortie, racine = _lancer_amorce(bac, _distant(bac), "d1", {"DEPENSE_EPUISEE_UTC_S": str(int(time.time()) - 60)})
    assert code == 2 and "démarrage après l'heure de dépense épuisée (C08) : aucun calcul" in sortie and (racine / "t06-detruire").exists()
    assert not (racine / "amorce-depot").exists() and journal == ""


def test_amorce_fichier_trop_gros_refuse_avant_le_commit(bac):
    distant = _distant(bac)
    code, journal, sortie, racine = _lancer_amorce(bac, distant, "g", {"FAUX_GROS": "1"})
    assert code == 1 and (racine / "t06-fin-anormale").exists() and not (racine / "t06-fin-normale").exists(), sortie[-3000:]     # C-V4-1 : fin anormale
    assert "FIN ANORMALE (C-V4-1)" in journal and "fichier(s) trop gros retiré(s) du commit" in journal
    assert "ERREUR DE CHAÎNE (C11)" in journal and "activations-sous-ensemble-t06-002.npz fait 90000001 octets > 90000000" in journal
    assert (racine / "t06-fichiers-trop-gros.txt").read_text().startswith("donnees/")
    fichiers = _fichiers_distants(distant)
    assert not any("activations-sous-ensemble-t06-002.npz\t" in f or f.endswith("activations-sous-ensemble-t06-002.npz") for f in fichiers)
    assert any(f.endswith("activations-sous-ensemble-t06-001.npz") for f in fichiers)
    tailles = [int(f.split()[3]) for f in fichiers if f.split()[3] != "-"]
    assert max(tailles) < 90_000_000 and any(f.endswith("t06-fichiers-trop-gros.txt") for f in fichiers)


def test_amorce_poussee_initiale_refusee(bac):
    distant = _distant(bac, REFUS_TOUT)
    code, journal, sortie, racine = _lancer_amorce(bac, distant, "pi")
    assert code == 2 and "poussée initiale de la branche calcul/t06-jouet-v4 refusée" in sortie and (racine / "t06-detruire").exists()
    assert "tests :" not in journal and "run :" not in journal


def test_amorce_poussee_finale_refusee_trois_fois_puis_second_demarrage(bac):
    distant = _distant(bac, REFUS_MISES_A_JOUR)
    code, journal, sortie, racine = _lancer_amorce(bac, distant, "pf")
    assert code == 1, sortie[-3000:]
    assert journal.count("poussée : tentative 3 refusée") >= 1 and "poussée finale impossible après trois tentatives" in journal
    assert " : fin, code 1" in sortie and (racine / "t06-fin-normale").exists() and (racine / "t06-arret-demande").exists()
    assert _git(distant, "log", "--format=%s", "calcul/t06-jouet-v4").splitlines() == ["init"]      # seule la création est passée
    assert "résultats et données légères" in _git(racine / "amorce-depot", "log", "--format=%s", "-3")  # committés sur l'instance
    code2, journal2, sortie2, _ = _lancer_amorce(bac, distant, "pf")
    assert code2 == 0 and "second démarrage" in sortie2 and "poussée : tentative 3 refusée" in journal2 and (racine / "t06-sommeil").exists()
    # le crochet levé, un troisième démarrage pousse tout
    (distant / "hooks" / "pre-receive").unlink()
    code3, journal3, _, _ = _lancer_amorce(bac, distant, "pf")
    assert code3 == 0 and "branche calcul/t06-jouet-v4 poussée (second démarrage)" in journal3
    assert any(f.endswith("activations-sous-ensemble-t06-001.npz") for f in _fichiers_distants(distant))


@pytest.mark.parametrize("env_sup, motif", [
    ({"FIN_GO_UTC_S": None}, "FIN_GO_UTC_S absente"), ({"FIN_GO_UTC_S": "demain"}, "FIN_GO_UTC_S absente ou non entière"),
    ({"DEPENSE_EPUISEE_UTC_S": None}, "DEPENSE_EPUISEE_UTC_S absente"), ({"DEPENSE_EPUISEE_UTC_S": "1"}, "après l'heure de dépense épuisée"),
    ({"FIN_GO_UTC_S": "1794873500"}, "fin du GO reçue (1794873500) ≠ calendrier.fin_go_utc"),
    ({"ECHEANCE_UTC_S": "1794873700"}, "ramenée"),
])
def test_amorce_variables_de_calendrier_et_de_depense(bac, env_sup, motif):
    code, journal, sortie, racine = _lancer_amorce(bac, _distant(bac), "v", env_sup)
    if motif == "ramenée":
        assert code == 0 and "échéance ramenée à la fin du GO (1794873600)" in sortie and (racine / "t06-echeance.txt").read_text().strip() == FIN_GO
    else:
        assert code == 2 and motif in sortie and (racine / "t06-detruire").exists(), sortie[-2000:]
        assert "run :" not in journal


def test_amorce_configuration_sans_calendrier_refusee(bac):
    src = bac["source"]
    (src / CONFIG).write_text("{}", encoding="utf-8")
    (src / (CONFIG + ".sha256")).unlink()
    sceller(src / CONFIG)
    _commit_source(bac, "config sans calendrier")
    code, journal, sortie, racine = _lancer_amorce(bac, _distant(bac), "c")
    assert code == 2 and "calendrier de la configuration non conforme" in sortie and "sans calendrier" in sortie and (racine / "t06-detruire").exists()


def test_amorce_arret_consigne_run_mort_et_redemarrage_interrompu(bac):
    distant = _distant(bac)
    code, journal, sortie, racine = _lancer_amorce(bac, distant, "a", {"FAUX_RUN": "arret"})
    assert code == 1 and "arrêt pendant run (code 1) : résultats et données légères committés" in journal and "RUN MORT" not in sortie
    assert "arrêt pendant run" in _git(distant, "log", "-3", "--format=%s", "calcul/t06-jouet-v4") and not (racine / "t06-fin-normale").exists()
    assert not [f for f in _fichiers_distants(distant) if "traces/consignation-" in f]             # v7 (R-1692) : la consignation d'arrêt de l'amorce n'ajoute pas la trace de la minuterie (elle a déjà `traces()`)
    # redémarrage d'un run interrompu (ni fin normale, ni dépense épuisée) : partiels consignés, destruction
    (racine / "amorce-depot" / "diag" / "tard").mkdir()
    (racine / "amorce-depot" / "diag" / "tard" / "x.json").write_text("{}", encoding="utf-8")
    code2, _, sortie2, _ = _lancer_amorce(bac, distant, "a")
    assert code2 == 2 and "run interrompu" in sortie2 and (racine / "t06-detruire").exists()
    assert "redémarrage d'un run interrompu" in _git(distant, "log", "-1", "--format=%s", "calcul/t06-jouet-v4")
    distant2 = _distant(bac)
    code, journal, sortie, racine = _lancer_amorce(bac, distant2, "m", {"FAUX_RUN": "mort"})
    assert code == 1 and "RUN MORT sans résumé ni arrêt consigné (code 137)" in sortie and "RUN MORT" in journal
    assert "run mort" in _git(distant2, "log", "-3", "--format=%s", "calcul/t06-jouet-v4") and (racine / "t06-arret-demande").exists()


def test_amorce_refus_go_et_branche_presente(bac):
    distant = _distant(bac)
    subprocess.run(["git", "-C", str(bac["source"]), "push", "-q", str(distant), "HEAD:refs/heads/calcul/t06-jouet-v4"], check=True)
    code, journal, sortie, racine = _lancer_amorce(bac, distant, "b")
    assert code == 2 and "déjà présente" in sortie and (racine / "t06-detruire").exists()
    (bac["source"] / "registres" / "go.md").write_text(GO.replace("200 USD", "250 USD"), encoding="utf-8")
    _commit_source(bac, "go autre")
    code3, journal3, sortie3, racine3 = _lancer_amorce(bac, _distant(bac), "g")
    assert code3 == 2 and "refus : GO-2026-11-02-28 non conforme" in sortie3 and "exact" in sortie3 and (racine3 / "t06-detruire").exists()


CURL_FACTICE = """#!/usr/bin/env bash
# écrit « {"success": true} » dans le fichier de sortie (-o), imprime 200 ; journalise la méthode
sortie=""; methode=GET; prec=""
for a in "$@"; do [ "$prec" = "-o" ] && sortie="$a"; [ "$prec" = "-X" ] && methode="$a"; prec="$a"; done
echo "$methode" >> "$FAUX_CURL_JOURNAL"
[ -n "$sortie" ] && echo '{"success": true}' > "$sortie"
printf '200'
"""


def test_minuterie_depense_epuisee_puis_echeance_consignent_et_poussent(bac, tmp_path):
    """C08 et C14 : la minuterie (bash seul, `curl` factice) consigne et pousse à l'heure de dépense épuisée (puis demande
    « stopped »), puis consigne et pousse à l'échéance avant le DELETE."""
    distant = _distant(bac)
    code, _, sortie, racine = _lancer_amorce(bac, distant, "mi")
    assert code == 0, sortie[-2000:]
    (racine / "amorce-depot" / "diag" / "partiel").mkdir()
    (racine / "amorce-depot" / "diag" / "partiel" / "p.json").write_text("{}", encoding="utf-8")
    (tmp_path / "bin").mkdir()
    (tmp_path / "bin" / "curl").write_text(CURL_FACTICE, encoding="utf-8")
    (tmp_path / "bin" / "curl").chmod(0o755)
    env = {k: os.environ[k] for k in ENV_DE_BASE if k in os.environ}
    now = int(time.time())
    env.update(PATH=f"{tmp_path / 'bin'}:{env.get('PATH', '')}", CONTAINER_ID="424242", CONTAINER_API_KEY="cle-factice", HOME=str(tmp_path),
               MINUTERIE_PAS_S="1", MINUTERIE_REESSAI_S="1", FAUX_CURL_JOURNAL=str(tmp_path / "curl.txt"))
    r = subprocess.run(["bash", str(racine / "t06-minuterie.sh"), str(now + 4), str(now + 1), str(racine), "https://api.invalid/v0"],
                       env=env, capture_output=True, text=True, timeout=120)
    j = (racine / "t06-minuterie.log").read_text(encoding="utf-8")
    assert r.returncode == 0, j
    assert "DÉPENSE ÉPUISÉE (C08" in j and "PUT stopped (dépense épuisée) : HTTP 200" in j and "consigné (dépense épuisée) : code 0" in j
    assert "ÉCHÉANCE" in j and "consigné (échéance) : code 0" in j and "instance 424242 détruite" in j
    assert j.index("DÉPENSE ÉPUISÉE") < j.index("ÉCHÉANCE") < j.index("DELETE instance")
    assert (tmp_path / "curl.txt").read_text().split() == ["PUT", "DELETE"] and "cle-factice" not in j
    messages = _git(distant, "log", "--format=%s", "-3", "calcul/t06-jouet-v4")
    assert "(dépense épuisée)" in messages and any(f.endswith("diag/partiel/p.json") for f in _fichiers_distants(distant))
    # artefact : identifiant d'instance illisible → aucun geste
    env["CONTAINER_ID"] = "abc"
    r = subprocess.run(["bash", str(racine / "t06-minuterie.sh"), str(now + 1), "0", str(racine), "https://api.invalid/v0"], env=env,
                       capture_output=True, text=True, timeout=60)
    assert r.returncode == 3 and "identifiant d'instance illisible" in (racine / "t06-minuterie.log").read_text(encoding="utf-8")


VASTAI_FACTICE = """#!/usr/bin/env bash
[ -n "${FAUX_VASTAI_JOURNAL:-}" ] && printf '%s\\n' "$*" >> "$FAUX_VASTAI_JOURNAL"
if [ "$1" = logs ]; then cat "$FAUX_JOURNAL"; exit 0; fi
if [ "$1" = search ] && [ "$2" = offers ]; then
    # C-V3-3 : la relecture d'une offre exige « --storage <Go> » (sinon dph_total et storage_total_cost sont lus au disque par défaut)
    ok=0; prec=""; for a in "$@"; do [ "$prec" = "--storage" ] && [[ "$a" =~ ^[0-9]+([.][0-9]+)?$ ]] && ok=1; prec="$a"; done
    [ "$ok" = 1 ] || { echo "relecture sans --storage : refusée (factice, C-V3-3)" >&2; exit 3; }
    cat "$FAUX_OFFRE"; exit 0
fi
if [ "$1" = show ] && [ "$2" = instances ]; then cat "${FAUX_INSTANCES:-/dev/null}"; [ -n "${FAUX_INSTANCES:-}" ] || echo '[]'; exit 0; fi
echo "appel inattendu : $*" >&2; exit 3
"""
DF_FACTICE = """#!/usr/bin/env bash
printf 'Filesystem 1024-blocks Used Available Capacity Mounted on\\n/dev/factice 100000000 1000 %s 1%% /\\n' "${FAUX_DF_LIBRE_KO:-5000000}"
"""


def _outils(tmp_path) -> Path:
    b = tmp_path / "bin"
    b.mkdir(exist_ok=True)
    for nom, texte in (("vastai", VASTAI_FACTICE), ("df", DF_FACTICE)):
        (b / nom).write_text(texte, encoding="utf-8")
        (b / nom).chmod(0o755)
    return b


def _env_surveillance(tmp_path, journal: str) -> dict:
    b = _outils(tmp_path)
    (tmp_path / "journal.txt").write_text(journal, encoding="utf-8")
    (tmp_path / "inventaire-surveillance.json").write_text(json.dumps([{"id": 123456, "label": "t06-e2", "actual_status": "running"}]), encoding="utf-8")   # v7 : l'instance est présente
    env = {k: os.environ[k] for k in ENV_DE_BASE if k in os.environ}
    env.update(PATH=f"{b}:{env.get('PATH', '')}", HF_TOKEN="jeton-hf-factice", CONTROLE_IA_GITHUB_TOKEN="jeton-gh-factice",
               FAUX_JOURNAL=str(tmp_path / "journal.txt"), INTERVALLE="1", HOME=str(tmp_path),
               FAUX_INSTANCES=str(tmp_path / "inventaire-surveillance.json"), ABSENCE_ATTENTE_S="0")
    return env


def _lancement(d: Path, creation: int, prix="1.0", stockage="0.03", anterieure="0", telechargement="1.2", instance="123456"):
    d.mkdir(parents=True, exist_ok=True)
    (d / "lancement.txt").write_text(f"commit {'a' * 40}\nprix_carte {prix}\nprix_stockage {stockage}\ntelechargement_forfait {telechargement}\n"
                                     f"anterieure {anterieure}\ninstance {instance}\ncreation {creation}\n", encoding="utf-8")


def _surveiller(tmp_path, journal, creation, dossier="s", **champs):
    d = tmp_path / dossier
    _lancement(d, creation, **champs)
    r = subprocess.run(["bash", str(LANCEUR), "surveillance", "123456", str(d)], env=_env_surveillance(tmp_path, journal),
                       capture_output=True, text=True, timeout=120)
    return r.returncode, r.stdout + r.stderr, d


def test_surveillance_v3_cumul_mort_fin_et_garde_illisible(tmp_path):
    now = int(time.time())
    j = "AMORCE 2026-11-05T10:00:00Z : commit abc\nPROGRES 2026-11-05T10:00:00Z etape=format verifie=True\n"
    code, sortie, d = _surveiller(tmp_path, j + "AMORCE 2026-11-05T11:00:00Z : RUN MORT sans résumé ni arrêt consigné (code 137)\n", now - 600)
    assert code == 3 and "ARRET mort" in sortie and "vastai stop instance 123456" in sortie and "jeton" not in sortie
    # C08 : 10 h à 1,03 USD/h = 10,3 USD, plus 189 USD de tentatives antérieures et 1,2 USD de téléchargement = 200,5 ≥ 200 USD
    code, sortie, d = _surveiller(tmp_path, j, now - 10 * 3600, dossier="d", anterieure="189")
    assert code == 3 and "ARRET depense" in sortie and "200.50 USD" in sortie and "stop instance 123456" in sortie
    # la même instance sans dépense antérieure (11,5 USD) n'est jamais arrêtée : la boucle poursuit, coupée au bout de 3 s
    _lancement(tmp_path / "d2", now - 10 * 3600, anterieure="0")
    with pytest.raises(subprocess.TimeoutExpired):
        subprocess.run(["bash", str(LANCEUR), "surveillance", "123456", str(tmp_path / "d2")], env=_env_surveillance(tmp_path, j),
                       capture_output=True, text=True, timeout=3)
    assert "ALERTE sans PROGRES" in (tmp_path / "d2" / "surveillance.txt").read_text(encoding="utf-8")
    code, sortie, d = _surveiller(tmp_path, j + "AMORCE 2026-11-05T12:00:00Z : fin, code 0\n", now - 600, dossier="f")
    assert code == 0 and sortie.startswith("FIN") and (d / "progres.txt").read_text(encoding="utf-8").count("PROGRES ") == 1
    # C09 : garde de dépense illisible (prix illisible) → ALERTE, ALERTE, puis ARRET au troisième tour
    code, sortie, d = _surveiller(tmp_path, j, now - 600, dossier="i", prix="x")
    assert code == 3 and "ARRET garde" in sortie and "stop instance 123456" in sortie
    s = (d / "surveillance.txt").read_text(encoding="utf-8")
    assert s.count("ALERTE garde de dépense illisible") == 2 and "(1/3)" in s and "(2/3)" in s
    # R10 : identifiant qui n'est pas celui de lancement.txt
    _lancement(tmp_path / "z", now - 600, instance="999")
    r = subprocess.run(["bash", str(LANCEUR), "surveillance", "123456", str(tmp_path / "z")], env=_env_surveillance(tmp_path, j),
                       capture_output=True, text=True, timeout=60)
    assert r.returncode == 2 and "R10" in r.stdout


@pytest.fixture
def depot_session(bac):
    src = bac["source"]
    origin = _distant(bac)
    _git(src, "remote", "add", "origin", str(origin))
    (src / ".claude" / "hooks").mkdir(parents=True)
    shutil.copy(RACINE / ".claude" / "hooks" / "garde_calcul.py", src / ".claude" / "hooks" / "garde_calcul.py")
    shutil.copy(LANCEUR, src / "scripts" / LANCEUR.name)
    return src


def _env_session(src, tmp_path, **sup):
    b = _outils(tmp_path)
    env = {k: os.environ[k] for k in ENV_DE_BASE if k in os.environ}
    env.update(PATH=f"{b}:{env.get('PATH', '')}", T06_DEPOT=str(src), HF_TOKEN="jeton-hf-factice", CONTROLE_IA_GITHUB_TOKEN="jeton-gh-factice",
               HOME=str(src.parent), FAUX_OFFRE=str(tmp_path / "offre.json"), FAUX_VASTAI_JOURNAL=str(tmp_path / "vastai-appels.txt"))
    if not (tmp_path / "offre.json").exists():
        (tmp_path / "offre.json").write_text(json.dumps([OFFRE]), encoding="utf-8")
    env.update(sup)
    return {k: v for k, v in env.items() if v is not None}


def _creer(src, tmp_path, d, *args, **sup):
    return subprocess.run(["bash", str(LANCEUR), "creation", *args, str(d)], env=_env_session(src, tmp_path, **sup), capture_output=True, text=True, timeout=120)




def test_controles_artefacts(depot_session, tmp_path):
    src = depot_session
    r = subprocess.run(["bash", str(LANCEUR), "controles", str(tmp_path / "c2"), "2026-11-16"], env=_env_session(src, tmp_path), capture_output=True, text=True, timeout=120)
    assert r.returncode == 2 and "dernier jour de création (2026-11-15) dépassé" in r.stdout            # L11
    r = subprocess.run(["bash", str(LANCEUR), "controles", str(tmp_path / "c4"), "2026-11-20"], env=_env_session(src, tmp_path), capture_output=True, text=True, timeout=120)
    assert r.returncode == 2 and "validité" in r.stdout
    env = _env_session(src, tmp_path)
    env["HF_TOKEN"] = ""
    r = subprocess.run(["bash", str(LANCEUR), "controles", str(tmp_path / "c3"), "2026-11-05"], env=env, capture_output=True, text=True, timeout=120)
    assert r.returncode == 2 and "jeton absent" in r.stdout
    _git(src, "rm", "-q", PREREG + ".sha256")
    _git(src, "commit", "-qm", "sceau retiré")
    (src / PREREG).write_text(_prereg("f" * 64), encoding="utf-8")
    sceller(src / PREREG)
    _commit_source({"source": src}, "nouveau scellement, amorce non citée")
    subprocess.run(["git", "-C", str(src), "push", "-q", "origin", "main"], check=True)
    r = subprocess.run(["bash", str(LANCEUR), "controles", str(tmp_path / "c1"), "2026-11-05"], env=_env_session(src, tmp_path), capture_output=True, text=True, timeout=120)
    assert r.returncode == 2 and "non citée" in r.stdout


# ---------------------------------------------------------------------------------------------------------------------------
# C-V4-1 : fin de run de l'amorce sous le verrou de consignation ; « rien à committer » ≠ commit en échec ; status propre
# ---------------------------------------------------------------------------------------------------------------------------
HOOK_VERROU = """#!/usr/bin/env bash
# journalise si le verrou de consignation est pris (par l'amorce, descripteur 9 hérité) pendant le commit
if flock -n "$RACINE_AMORCE/t06-consigner.lock" true; then echo LIBRE >> "$RACINE_AMORCE/hook-verrou.txt"; else echo PRIS >> "$RACINE_AMORCE/hook-verrou.txt"; fi
exit 0
"""
HOOK_ECHEC_UNE_FOIS = """#!/usr/bin/env bash
M="$RACINE_AMORCE/hook-essai-$(git rev-parse --git-dir | tr -c 'a-z0-9\n' _)-$(date +%s%N | cut -c1-12)"
if [ ! -e "$RACINE_AMORCE/hook-deja" ]; then : > "$RACINE_AMORCE/hook-deja"; echo "premier commit refusé (factice)" >&2; exit 1; fi
exit 0
"""
HOOK_ECHEC = "#!/usr/bin/env bash\necho 'commit refusé (factice)' >&2\nexit 1\n"


def _status(racine):
    return _git(racine / "amorce-depot", "status", "--porcelain", "--", "runs", "diag", "donnees", "traces")


def test_c_v4_1_cas_sain_verrou_pris_pendant_les_commits_de_fin_de_run_et_status_propre(bac):
    distant = _distant(bac)
    code, journal, sortie, racine = _lancer_amorce(bac, distant, "ok", {"FAUX_PRECOMMIT": HOOK_VERROU})
    assert code == 0, sortie[-2500:]
    pris = (racine / "hook-verrou.txt").read_text().split()
    assert len(pris) >= 3 and set(pris) == {"PRIS"}                      # résultats, morceaux, traces : tous sous le verrou
    assert (racine / "t06-fin-normale").exists() and not (racine / "t06-fin-anormale").exists() and not (racine / "t06-erreurs-chaine.txt").exists()
    assert _status(racine) == "" and "ERREUR DE CHAÎNE" not in journal
    import fcntl
    with open(racine / "t06-consigner.lock", "a") as f:                  # verrou relâché à la sortie
        fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)


def test_c_v4_1_arret_consigne_sous_le_verrou(bac):
    code, journal, sortie, racine = _lancer_amorce(bac, _distant(bac), "ar", {"FAUX_RUN": "arret", "FAUX_PRECOMMIT": HOOK_VERROU})
    assert code == 1 and "arrêt pendant run (code 1)" in journal
    pris = (racine / "hook-verrou.txt").read_text().split()
    assert len(pris) >= 2 and set(pris) == {"PRIS"}


def test_c_v4_1_rien_a_committer_n_est_pas_un_echec(bac):
    """Cas sain : un run sans morceau (index vide au commit des morceaux) finit normalement : « aucun morceau à committer »."""
    distant = _distant(bac)
    code, journal, sortie, racine = _lancer_amorce(bac, distant, "vide", {"FAUX_SANS_MORCEAU": "1"})
    assert code == 0 and "aucun morceau à committer" in journal and (racine / "t06-fin-normale").exists()
    assert not (racine / "t06-fin-anormale").exists() and not (racine / "t06-erreurs-chaine.txt").exists() and _status(racine) == ""


def test_c_v4_1_index_lock_pose_pendant_la_fin_de_run_fin_anormale_sans_fin_normale(bac):
    """Artefact : `index.lock` posé pendant la fin de run. La v3 lisait l'échec comme « aucun résultat léger à committer » et
    posait `t06-fin-normale` ; la v4 journalise « ERREUR DE CHAÎNE », pousse ce qui existe, pose `t06-fin-anormale`, code 1."""
    distant = _distant(bac)
    code, journal, sortie, racine = _lancer_amorce(bac, distant, "il", {"FAUX_INDEX_LOCK": "1"})
    assert code == 1, sortie[-2500:]
    assert "ERREUR DE CHAÎNE (C-V4-1) : git add en échec" in journal and "FIN ANORMALE (C-V4-1)" in journal
    assert (racine / "t06-fin-anormale").exists() and not (racine / "t06-fin-normale").exists() and (racine / "t06-erreurs-chaine.txt").exists()
    # l'index est vide parce que `git add` a échoué : le message « aucun… » peut figurer, mais l'échec d'ajout l'emporte (fin anormale)
    assert " : fin, code 1" in sortie and (racine / "t06-arret-demande").exists()
    assert _git(distant, "log", "--format=%s", "calcul/t06-jouet-v4").splitlines() == ["init"]       # rien n'a pu être committé : la poussée de ce qui existe est vide


def test_c_v4_1_commit_refuse_une_fois_puis_reussi_et_commit_toujours_refuse(bac):
    distant = _distant(bac)
    code, journal, sortie, racine = _lancer_amorce(bac, distant, "une", {"FAUX_PRECOMMIT": HOOK_ECHEC_UNE_FOIS, "COMMIT_ATTENTE_S": "0"})
    assert code == 0, sortie[-2500:]
    assert journal.count("commit en échec (tentative 1)") == 1 and "commit en échec (tentative 2)" not in journal      # réessayé une fois, réussi
    assert (racine / "t06-fin-normale").exists() and not (racine / "t06-fin-anormale").exists() and _status(racine) == ""
    assert any(f.endswith("activations-sous-ensemble-t06-001.npz") for f in _fichiers_distants(distant))
    distant2 = _distant(bac)
    code2, journal2, sortie2, racine2 = _lancer_amorce(bac, distant2, "tjrs", {"FAUX_PRECOMMIT": HOOK_ECHEC, "COMMIT_ATTENTE_S": "0"})
    assert code2 == 1 and "commit en échec (tentative 2)" in journal2 and "FIN ANORMALE (C-V4-1)" in journal2
    assert (racine2 / "t06-fin-anormale").exists() and not (racine2 / "t06-fin-normale").exists() and "aucun résultat léger à committer" not in journal2
    assert (racine2 / "t06-erreurs-chaine.txt").read_text().count("commit en échec") >= 2


def test_c_v4_1_status_non_vide_avant_la_fin_normale_rattrapage_ou_fin_anormale(bac):
    """Un fichier non consigné sous `runs`, `diag`, `donnees` ou `traces` empêche `t06-fin-normale` : le crochet du faux lanceur
    laisse un fichier que seul `consigner_partiel` rattrape (cas sain du rattrapage) ; un fichier qui ne peut pas partir
    (ignoré par aucun .gitignore mais retiré par la garde de taille) donne la fin anormale."""
    hook = """#!/usr/bin/env bash
# au commit des morceaux seulement, dépose un résultat léger tardif : il reste hors de l'index à ce commit
if git diff --cached --name-only | grep -q 'sous-ensemble-t06-000.npz$'; then mkdir -p diag/tardif; echo '{}' > diag/tardif/note.json; fi
exit 0
"""
    distant = _distant(bac)
    code, journal, sortie, racine = _lancer_amorce(bac, distant, "ras", {"FAUX_PRECOMMIT": hook})
    assert code == 0, sortie[-2500:]
    assert "git status --porcelain non vide avant la fin normale" in journal and "diag/tardif/" in journal
    assert (racine / "t06-fin-normale").exists() and not (racine / "t06-fin-anormale").exists() and _status(racine) == ""
    assert any(f.endswith("diag/tardif/note.json") for f in _fichiers_distants(distant))             # rattrapé par consigner_partiel "fin de run"


def test_c_v4_1_verrou_non_obtenu_fin_anormale_journalisee(bac):
    """Artefact : un autre processus tient le verrou de consignation plus longtemps que l'attente : la v4 le journalise, pousse au
    mieux et finit en fin anormale (jamais en silence)."""
    racine = bac["racine"] / "vr"
    racine.mkdir()
    detenteur = subprocess.Popen(["flock", "-x", str(racine / "t06-consigner.lock"), "sleep", "25"])
    try:
        time.sleep(0.5)
        distant = _distant(bac)
        code, journal, sortie, racine = _lancer_amorce(bac, distant, "vr", {"VERROU_ATTENTE_S": "2"})
    finally:
        detenteur.kill()
        detenteur.wait()
    assert code == 1, sortie[-2500:]
    assert "verrou de consignation non obtenu (fin de run)" in journal and (racine / "t06-fin-anormale").exists() and not (racine / "t06-fin-normale").exists()
    assert any(f.endswith("activations-sous-ensemble-t06-001.npz") for f in _fichiers_distants(distant))      # poussée au mieux : rien de perdu


def test_c_v4_1_minuterie_a_l_echeance_pendant_la_poussee_finale_aucun_fichier_perdu_ordre_garde(bac):
    """La minuterie lance `t06-consigner.sh` au milieu de la fin de run (pendant le premier commit, rendu lent) : elle attend le
    verrou, ne casse aucun commit (pas d'`index.lock` croisé), ne perd aucun fichier, et l'ordre des commits est celui de la fin de run."""
    hook = """#!/usr/bin/env bash
if [ ! -e "$RACINE_AMORCE/hook-lance" ]; then : > "$RACINE_AMORCE/hook-lance"
  setsid bash "$RACINE_AMORCE/t06-consigner.sh" "échéance" < /dev/null > "$RACINE_AMORCE/concurrent.log" 2>&1 &
  sleep 3
fi
exit 0
"""
    distant = _distant(bac)
    code, journal, sortie, racine = _lancer_amorce(bac, distant, "mn", {"FAUX_PRECOMMIT": hook})
    assert code == 0, sortie[-2500:]
    for _ in range(120):                                                         # la consignation concurrente finit après la sortie de l'amorce
        if "branche calcul/t06-jouet-v4 poussée (échéance)" in (racine / "concurrent.log").read_text():
            break
        time.sleep(0.5)
    c = (racine / "concurrent.log").read_text()
    assert "branche calcul/t06-jouet-v4 poussée (échéance)" in c and "ERREUR DE CHAÎNE" not in c and "ERREUR DE CHAÎNE" not in journal
    messages = _git(distant, "log", "--reverse", "--format=%s", "calcul/t06-jouet-v4").splitlines()
    assert messages[0] == "init" and "résultats et données légères" in messages[1] and "morceaux" in messages[2] and messages[3].startswith("T0.6 : traces")
    assert len(messages) == 5 and messages[4] == "T0.6 : journal de l'instance (échéance)"   # v9 (R-1692) : la consignation d'échéance n'a aucun résultat à ajouter, mais dépose le journal ; rien de doublé, rien de perdu
    assert sum(1 for f in _fichiers_distants(distant) if "activations-sous-ensemble-t06-00" in f) == 4 and (racine / "t06-fin-normale").exists()


def test_c_v4_1_verrou_relache_avant_l_arret_de_l_instance(bac):
    """Le verrou de consignation est relâché avant `arreter_instance` (sinon le sommeil qui suit le garderait et la minuterie ne
    pourrait plus consigner) : fin normale, fin anormale et arrêt consigné."""
    for nom, env, code_attendu in (("v1", {}, 0), ("v2", {"FAUX_INDEX_LOCK": "1"}, 1), ("v3", {"FAUX_RUN": "arret"}, 1)):
        code, journal, sortie, racine = _lancer_amorce(bac, _distant(bac), nom, env)
        assert code == code_attendu and (racine / "t06-arret-demande").exists(), (nom, sortie[-1500:])
        assert not (racine / "t06-verrou-tenu-a-l-arret").exists(), nom


def test_c_v4_1_delai_de_la_minuterie_couvre_l_attente_du_verrou():
    """La consignation de la minuterie attend le verrou jusqu'à 1500 s : son délai total doit être plus grand, sinon une fin de
    run en cours la ferait tuer avant la poussée et la minuterie détruirait l'instance (résultats perdus)."""
    import re
    texte = "\n".join(l for l in AMORCE.read_text(encoding="utf-8").splitlines() if not l.lstrip().startswith("#"))      # hors commentaires
    attente = [int(x) for x in re.findall(r"flock -w (\d+) 9", texte)]
    delai = [int(x) for x in re.findall(r'timeout -k 10 (\d+) bash "\$R/t06-consigner.sh" "\$1"', texte)]
    assert attente == [1500] and len(delai) == 1 and delai[0] > attente[0] + 600


def test_c_v4_1_fichier_non_rattrapable_fin_anormale(bac):
    """Artefact : le rattrapage `consigner_partiel "fin de run"` ne parvient pas à committer le fichier tardif (crochet qui refuse) :
    `git status --porcelain` reste non vide, donc fin anormale, jamais `t06-fin-normale`."""
    hook = """#!/usr/bin/env bash
if git diff --cached --name-only | grep -q 'sous-ensemble-t06-000.npz$'; then mkdir -p diag/tardif; echo '{}' > diag/tardif/note.json; : > "$RACINE_AMORCE/hook-arme"; fi
if [ -e "$RACINE_AMORCE/hook-arme" ] && git diff --cached --name-only | grep -q 'diag/tardif/note.json'; then echo "refusé (factice)" >&2; exit 1; fi
exit 0
"""
    code, journal, sortie, racine = _lancer_amorce(bac, _distant(bac), "nr", {"FAUX_PRECOMMIT": hook, "COMMIT_ATTENTE_S": "0"})
    assert code == 1, sortie[-2500:]
    assert "git status --porcelain non vide avant la fin normale" in journal and "fichiers non consignés après le rattrapage" in journal
    assert (racine / "t06-fin-anormale").exists() and not (racine / "t06-fin-normale").exists()


# ---------------------------------------------------------------------------------------------------------------------------
# C-V4-3 : épreuves à blanc E2 et E3 (GO-2026-11-06-01, 5 USD cumulés ; E2 ≤ 1,5, E3 ≤ 3,5 ; aucune donnée décisive)
# ---------------------------------------------------------------------------------------------------------------------------
from datetime import date, datetime, timedelta, timezone                      # noqa: E402

GO_E = "GO-2026-11-06-01"
CONFIG_E2 = RACINE / "docs" / "notes" / "g0-deux-semaines-v1" / "config-t06-epreuve-e2-v1.json"
CONFIG_E3 = RACINE / "docs" / "notes" / "g0-deux-semaines-v1" / "config-t06-epreuve-e3-v1.json"
OFFRE_E2 = {**OFFRE, "gpu_name": "RTX 4090", "gpu_ram": 24564, "cpu_ram": 64000, "cpu_cores_effective": 16.0, "dph_total": 0.35, "cuda_max_good": 13.2}


def _dates_epreuve():
    auj = datetime.now(timezone.utc).date()
    ech = auj + timedelta(days=3)
    fin = datetime.combine(ech + timedelta(days=1), datetime.min.time(), tzinfo=timezone.utc)
    return auj, ech, fin


def _go_epreuve(plafond="5 USD (E2 et E3 cumulés)"):
    auj, ech, _ = _dates_epreuve()
    return f"| {GO_E} | {auj} | calcul | épreuves à blanc E2 et E3 | {plafond} | {ech} | Lazar | mot |\n"


def _config_epreuve(chemin: Path, **modifs) -> dict:
    c = json.loads(chemin.read_text(encoding="utf-8"))
    _, ech, fin = _dates_epreuve()
    c["calendrier"] = {"dernier_jour_creation": str(ech - timedelta(days=1)), "fin_go_utc": fin.strftime("%Y-%m-%dT%H:%M:%SZ")}
    c.update(modifs)
    return c


def test_session_v3_go_plafond_depense_et_epuisement_simule(tmp_path):
    from controle_ia.t06 import session_v3 as s3
    from controle_ia.t06.session import GardeSession
    reg = tmp_path / "go.md"
    entete = GO.split("\n")[0] + "\n" + GO.split("\n")[1] + "\n"
    reg.write_text(entete + _go_epreuve(), encoding="utf-8")
    assert s3.verifier_go_v3(reg, GO_E, 5)["plafond_usd"] == 5.0                            # commentaire entre parenthèses admis
    for plafond, motif in ((200, "5 USD"), (4, "exact attendu"), ("x", "illisible")):
        with pytest.raises(GardeSession, match=motif if motif != "5 USD" else "exact attendu"):
            s3.verifier_go_v3(reg, GO_E, plafond)
    with pytest.raises(GardeSession, match="absent du registre"):
        s3.verifier_go_v3(reg, "GO-2026-11-02-28", 200)
    with pytest.raises(GardeSession, match="identifiant de GO illisible"):
        s3.verifier_go_v3(reg, "n'importe quoi", 5)
    reg.write_text(entete + _go_epreuve("5 USD ; 6 USD"), encoding="utf-8")
    with pytest.raises(GardeSession, match="exact attendu"):
        s3.verifier_go_v3(reg, GO_E, 5)                                                       # un commentaire hors parenthèses n'est pas admis
    # la dépense au plafond donné : 1,5 USD, antérieure 0,5, téléchargement 0,1, prix 0,5 + 0,02 par heure
    d = s3.depense_cumulee_v3(1.5, 0.5, 0.02, 1_000_000, 0.5, 0.1, 1_000_000 + 3600)
    assert d["plafond_usd"] == 1.5 and not d["arret"] and abs(d["cumulee_usd"] - 1.12) < 1e-9
    assert abs(d["epuisement_utc_s"] - (1_000_000 + 0.9 / 0.52 * 3600)) < 2
    assert s3.depense_cumulee_v3(1.5, 0.5, 0.02, 1_000_000, 0.5, 0.1, 1_000_000 + 3 * 3600)["arret"]
    assert s3.depense_cumulee_v3(200, 0.5, 0.02, 1_000_000, 0.5, 0.1, 1_000_000 + 3 * 3600)["arret"] is False   # le même cas sous 200 USD
    # épuisement simulé : n'avance que l'heure, jamais plus tard que l'épuisement réel ; 60 s au moins
    assert s3.depense_cumulee_v3(1.5, 0.5, 0.02, 1_000_000, 0, 0, 1_000_100, None, 600)["epuisement_utc_s"] == 1_000_600
    assert s3.depense_cumulee_v3(1.5, 0.5, 0.02, 1_000_000, 0, 0, 1_000_100, None, 10 ** 7)["epuisement_utc_s"] == int(1_000_000 + 1.5 / 0.52 * 3600)
    with pytest.raises(GardeSession, match="60 s au moins"):
        s3.depense_cumulee_v3(1.5, 0.5, 0.02, 1_000_000, 0, 0, 1_000_100, None, 30)
    # décision de surveillance : le texte nomme le plafond de l'épreuve, pas 200
    dec = s3.decider_surveillance_v3("", 1_000_000 + 3 * 3600, s3.depense_cumulee_v3(1.5, 0.5, 0.02, 1_000_000, 0, 0, 1_000_000 + 3 * 3600))
    assert dec.startswith("ARRET depense") and "plafond 1.5 USD" in dec


@pytest.fixture
def src_epreuve(depot_session):
    """Dépôt source avec le GO d'épreuve (dates relatives à aujourd'hui), les configurations E2 et E3 (calendrier relatif), la
    branche `prep/essai-t06` poussée et relevée par un fetch à refspec explicite : de quoi lancer `controles-epreuve`."""
    src = depot_session
    reg = src / "registres" / "go.md"
    reg.write_text(reg.read_text(encoding="utf-8") + _go_epreuve(), encoding="utf-8")
    for nom, chemin in (("e2", CONFIG_E2), ("e3", CONFIG_E3)):
        f = src / "prereg" / f"config-epreuve-{nom}.json"
        f.write_text(json.dumps(_config_epreuve(chemin), ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    _commit_source(src.parent and {"source": src}, "épreuves : GO et configurations")
    _git(src, "push", "-q", "origin", "HEAD:refs/heads/prep/essai-t06")
    _git(src, "fetch", "-q", "origin", "refs/heads/prep/essai-t06:refs/remotes/origin/prep/essai-t06")
    return src


def _controles_epreuve(src, tmp_path, d, config="prereg/config-epreuve-e2.json", commit=None, **sup):
    sup.setdefault("T06_BRANCHE_CODE", "prep/essai-t06")
    sup.setdefault("T06_BRANCHE", "essai/t06-e2-test")
    sup.setdefault("T06_DEPENSE_EPREUVES_ANTERIEURES_USD", "0")                          # R-1696 : exigée par controles-epreuve
    if sup.get("T06_REGISTRE_GO", "") is None:
        del sup["T06_REGISTRE_GO"]
    else:
        sup.setdefault("T06_REGISTRE_GO", str(src / "registres" / "go.md"))               # registre de « main » (ici : celui de l'arbre d'essai)
    return subprocess.run(["bash", str(LANCEUR), "controles-epreuve", str(d), commit or _git(src, "rev-parse", "HEAD"), config],
                          env=_env_session(src, tmp_path, **sup), capture_output=True, text=True, timeout=120)




@pytest.mark.parametrize("cas", ["commit_hors_branche", "go_de_la_course", "plafond_hors_epreuve", "mode_illisible", "branche_code_calcul", "go_absent_du_registre", "go_plafond_200", "jeton_hf_reel"])
def test_c_v4_3_controles_d_epreuve_artefacts(src_epreuve, tmp_path, cas):
    src = src_epreuve
    sup, config = {}, "prereg/config-epreuve-e2.json"
    if cas == "commit_hors_branche":
        (src / "hors.txt").write_text("x", encoding="utf-8")
        _commit_source({"source": src}, "hors branche")                                       # commit local, jamais poussé ni relevé
    elif cas in ("go_de_la_course", "plafond_hors_epreuve", "mode_illisible"):
        modifs = {"go_de_la_course": {"go_id": "GO-2026-11-02-28", "plafond_usd": 1.5}, "plafond_hors_epreuve": {"plafond_usd": 4.95}, "mode_illisible": {"mode": "autre"}}[cas]
        f = src / "prereg" / "config-epreuve-x.json"
        f.write_text(json.dumps(_config_epreuve(CONFIG_E2, **modifs)), encoding="utf-8")
        _commit_source({"source": src}, cas)
        _git(src, "push", "-q", "origin", "HEAD:refs/heads/prep/essai-t06")
        _git(src, "fetch", "-q", "origin", "refs/heads/prep/essai-t06:refs/remotes/origin/prep/essai-t06")
        config = "prereg/config-epreuve-x.json"
    elif cas == "branche_code_calcul":
        sup["T06_BRANCHE_CODE"] = "calcul/t06-reel-v4"
    elif cas in ("go_absent_du_registre", "go_plafond_200"):
        reg = src / "registres" / "go.md"
        texte = reg.read_text(encoding="utf-8")
        reg.write_text(texte.replace(_go_epreuve(), "") if cas == "go_absent_du_registre" else texte.replace("5 USD (E2 et E3 cumulés)", "200 USD"), encoding="utf-8")
        _commit_source({"source": src}, cas)
        _git(src, "push", "-q", "origin", "HEAD:refs/heads/prep/essai-t06")
        _git(src, "fetch", "-q", "origin", "refs/heads/prep/essai-t06:refs/remotes/origin/prep/essai-t06")
    elif cas == "jeton_hf_reel":
        config = "prereg/config-epreuve-e3.json"
        sup["HF_TOKEN"] = ""
    r = _controles_epreuve(src, tmp_path, tmp_path / "x", config=config, **sup)
    assert r.returncode == 2, (cas, r.stdout + r.stderr)
    if cas == "go_de_la_course":
        assert "ne sert que les épreuves à blanc" in r.stdout                              # refus par le GO lui-même, pas seulement par le plafond
    assert not (tmp_path / "x" / "lancement.txt").exists() or "epreuve oui" not in (tmp_path / "x" / "lancement.txt").read_text(encoding="utf-8")




def _epreuve_amorce(bac, nom, go=GO_E, branche="essai/t06-e2-test", mode="jouet", **sup):
    """Amorce sous une configuration d'épreuve (registre et configuration du dépôt de l'essai posés avant)."""
    src = bac["source"]
    (src / "registres" / "go.md").write_text(GO + _go_epreuve(), encoding="utf-8")
    c = _config_epreuve(CONFIG_E2, mode=json.loads(CONFIG_E2.read_text(encoding="utf-8"))["mode"])
    f = src / "prereg" / "config-epreuve.json"
    f.write_text(json.dumps(c, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    sceller(f)
    _commit_source(bac, "épreuve")
    _, _, fin = _dates_epreuve()
    env = {"EPREUVE_GO_ID": go, "PREREG_ABSENT": "1", "CONFIG": "prereg/config-epreuve.json", "BRANCHE": branche, "MODE": mode, "HF_TOKEN": "jeton-hf-factice",
           "FIN_GO_UTC_S": str(int(fin.timestamp())), "ECHEANCE_UTC_S": str(int(fin.timestamp())), "TESTS_ATTENDUS": ""}
    env.update(sup)
    distant = _distant(bac)                                                                   # cloné APRÈS le commit de l'épreuve
    return (*_lancer_amorce(bac, distant, nom, env), distant)


@pytest.mark.parametrize("mode", ["jouet", "reel"])
def test_c_v4_3_amorce_epreuve_cas_sain(bac, mode):
    """L'amorce admet une épreuve (GO d'épreuve, branche essai/…, sans préenregistrement) en mode jouet comme en mode réel ;
    elle vérifie le GO d'épreuve et le calendrier, jamais ceux de la course."""
    code, journal, sortie, racine, distant = _epreuve_amorce(bac, "ep", mode=mode)
    assert code == 0, sortie[-2500:]
    assert f"GO : {GO_E} conforme (plafond 5 USD" in journal and f"GO={GO_E}" in journal and "répétition sans préenregistrement" in journal
    assert (racine / "t06-fin-normale").exists() and "essai/t06-e2-test" in _git(distant, "branch", "--list", "essai/*")


@pytest.mark.parametrize("cas", ["go_de_la_course", "branche_calcul", "sans_prereg_absent", "reel_sans_epreuve", "go_expire"])
def test_c_v4_3_amorce_epreuve_artefacts(bac, cas):
    sup = {}
    if cas == "go_de_la_course":
        sup["go"] = "GO-2026-11-02-28"
    elif cas == "branche_calcul":
        sup["branche"] = "calcul/t06-reel-v4"
    elif cas == "sans_prereg_absent":
        sup["PREREG_ABSENT"] = "0"
    elif cas == "reel_sans_epreuve":
        sup.update(mode="reel", EPREUVE_GO_ID="")
    elif cas == "go_expire":
        sup["FIN_GO_UTC_S"] = "1794873600"                                                        # fin du GO ≠ calendrier de la configuration d'épreuve
    code, journal, sortie, racine, _ = _epreuve_amorce(bac, "ea", **sup)
    assert code == 2 and (racine / "t06-detruire").exists(), (cas, sortie[-2000:])
    motif = {"go_de_la_course": "seuls GO-2026-11-06-01 et GO-2026-11-07-08 (E3 bis) sont des épreuves à blanc", "branche_calcul": "doit commencer par essai/",
             "sans_prereg_absent": "PREREG_ABSENT=1 exigé", "reel_sans_epreuve": "n'est permis qu'en mode jouet (R1)", "go_expire": "fin du GO reçue"}[cas]
    assert motif in sortie, (cas, sortie[-1500:])
    assert "run :" not in journal


def test_c_v4_3_materiel_et_virgules_des_essais_joues(bac):
    """La ligne MATERIEL (MemTotal, cœurs, flock) est au journal et relayée ; `TESTS_ARGS` à virgules devient une liste d'essais."""
    distant = _distant(bac)
    code, journal, sortie, racine = _lancer_amorce(bac, distant, "mat", {"TESTS_ARGS": "tests/x.py,tests/y.py", "TESTS_ATTENDUS": "7", "PREREG_ABSENT": "1", "CONFIG": CONFIG})
    assert code == 0, sortie[-2500:]
    import re
    m = re.search(r"AMORCE \S+ : MATERIEL MemTotal_ko=(\d+) coeurs=(\d+) flock=(oui|non)", journal)
    assert m and int(m.group(1)) > 0 and int(m.group(2)) >= 1 and m.group(3) == "oui", journal[:1500]
    assert (racine / "pytest-args.txt").read_text().strip().endswith("--color=no tests/x.py tests/y.py")          # virgules → espaces




def test_c_v4_1_consignation_code_de_sortie_poussee_de_ce_qui_existe_mais_echec_de_chaine(bac):
    """`t06-consigner.sh` (celle de la minuterie) sort en code 2 quand la poussée de ce qui existe a eu lieu mais qu'un commit a échoué,
    en code 0 quand tout est parti (cas sain)."""
    code, journal, sortie, racine = _lancer_amorce(bac, _distant(bac), "cs")
    assert code == 0
    (racine / "amorce-depot" / "diag" / "n1").mkdir()
    (racine / "amorce-depot" / "diag" / "n1" / "a.json").write_text("{}", encoding="utf-8")
    r = subprocess.run(["bash", str(racine / "t06-consigner.sh"), "sain"], capture_output=True, text=True, timeout=120)
    assert r.returncode == 0, r.stdout + r.stderr
    (racine / "amorce-depot" / "diag" / "n2").mkdir()
    (racine / "amorce-depot" / "diag" / "n2" / "b.json").write_text("{}", encoding="utf-8")
    hook = racine / "amorce-depot" / ".git" / "hooks" / "pre-commit"
    hook.write_text(HOOK_ECHEC, encoding="utf-8")
    hook.chmod(0o755)
    r = subprocess.run(["bash", str(racine / "t06-consigner.sh"), "artefact"], capture_output=True, text=True, timeout=120, env={**os.environ, "COMMIT_ATTENTE_S": "0"})
    assert r.returncode == 2 and "poussée faite de ce qui existe (artefact), mais un ajout ou un commit a échoué" in r.stdout, r.stdout + r.stderr


# ---------------------------------------------------------------------------------------------------------------------------------
# Essais neufs de l'amorce v7 et du lanceur v8 (R-1677, R-1683 ; cas sain et artefact pour chaque garde, R5)
# ---------------------------------------------------------------------------------------------------------------------------------
import re                                                                                                     # noqa: E402

from controle_ia.t06 import session_v7 as s7                                                                  # noqa: E402
from controle_ia.t06.session import GardeSession                                                              # noqa: E402

GIT_REEL = shutil.which("git")


def _distant_filtrant(bac) -> Path:
    d = _distant(bac)
    subprocess.run(["git", "-C", str(d), "config", "uploadpack.allowFilter", "true"], check=True)
    subprocess.run(["git", "-C", str(d), "config", "uploadpack.allowAnySHA1InWant", "true"], check=True)
    return d


def _ajouter_arbre_lourd(bac):
    src = bac["source"]
    for chemin in ("docs/sources/pdf/tiers.pdf", "registres/passations/passation.md", "brouillons/brouillon.md", "livrables/livrable.zip", "gemini/g.txt",
                   "docs/sources/autre-source/x.md", "docs/notes/note.json", "docs/sources/invites-2606.08892-v1/invite.md", "docs/procedures/p.md",
                   "registres/etat.md", "pyproject.toml", "requirements-gpu.txt", "brouillons/ordres-t06-e2-e3-v5/ordre.md"):
        f = src / chemin
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(chemin + "\n" + "x" * 1000, encoding="utf-8")      # contenus distincts : un blob par fichier
    _commit_source(bac, "arbre avec dossiers lourds")


def test_clonage_reduit_extraction_partielle_ligne_de_debit_et_chemins(bac):
    """Cas sain : seuls les chemins de la liste sont extraits (dossiers lourds absents, blobs absents du clone), la ligne CLONAGE donne les mesures."""
    _ajouter_arbre_lourd(bac)
    distant = _distant_filtrant(bac)
    code, journal, sortie, racine = _lancer_amorce(bac, distant, env_sup={"DEPOT_URL": f"file://{distant}"})        # file:// : le filtre de blobs est honoré
    assert code == 0, sortie[-2500:]
    m = re.search(r"AMORCE \S+ : CLONAGE mode=jouet secondes=(\d+) octets_git=(\d+) octets_arbre=(\d+) debit_Mo_s=(\d+\.\d\d) motifs=(\d+)", sortie)
    assert m and int(m.group(1)) >= 1 and int(m.group(2)) > 0 and int(m.group(3)) > 0 and int(m.group(5)) >= 20, sortie[:1500]
    assert "AMORCE T06 v9 DEMARRAGE" in sortie
    depot = racine / "amorce-depot"
    for present in ("src", "scripts", "prereg", "donnees", "docs/notes/note.json", "docs/sources/invites-2606.08892-v1/invite.md", "docs/procedures/p.md",
                    "registres/go.md", "registres/etat.md", "pyproject.toml", "requirements-gpu.txt", "brouillons/ordres-t06-e2-e3-v5/ordre.md"):
        assert (depot / present).exists(), present
    for exclu in ("docs/sources/pdf", "registres/passations", "brouillons/brouillon.md", "livrables", "gemini", "docs/sources/autre-source"):
        assert not (depot / exclu).exists(), exclu
    assert "jeton-factice" not in sortie and (racine / "t06-fin-normale").exists()
    manquants = subprocess.run(["git", "-C", str(depot), "rev-list", "--objects", "--missing=print", "--all"], capture_output=True, text=True).stdout
    assert sum(1 for l in manquants.splitlines() if l.startswith("?")) >= 4, manquants[:500]


@pytest.mark.parametrize("etape, motif", [("set", "set"), ("init", "init")])
def test_clonage_reduit_extraction_partielle_impossible_est_un_refus_qui_cite_le_message_de_git(bac, tmp_path, etape, motif):
    """Artefact : `git sparse-checkout init|set` en échec → refus nommé qui CITE le message de git (R-1683), aucun run, aucun repli sur l'extraction complète."""
    distant = _distant_filtrant(bac)
    b = tmp_path / "faux-git"
    b.mkdir()
    (b / "git").write_text(f'#!/usr/bin/env bash\nif [[ " $* " == *" sparse-checkout "* && " $* " == *" {etape} "* ]]; then echo "message de git : sparse-checkout {etape} refusé (factice)" >&2; exit 1; fi\nexec {GIT_REEL} "$@"\n',
                           encoding="utf-8")
    (b / "git").chmod(0o755)
    code, journal, sortie, racine = _lancer_amorce(bac, distant, env_sup={"PATH": f"{b}:{os.environ['PATH']}"})
    assert code == 2 and f"refus : extraction partielle impossible (sparse-checkout {motif}) : message de git : sparse-checkout {etape} refusé (factice)" in sortie, sortie[-1500:]
    assert (racine / "t06-detruire").exists() and "CLONAGE mode=" not in sortie


def test_refus_annonce_puis_attend_avant_de_demander_la_destruction(bac):
    distant = _distant(bac)
    t0 = time.time()
    code, _, sortie, racine = _lancer_amorce(bac, distant, env_sup={"COMMIT": "abcdef", "REFUS_ATTENTE_ESSAI_S": "2"})
    assert time.time() - t0 >= 2 and code == 2, sortie[-1200:]
    i_refus, i_annonce, i_detruire = (sortie.index(x) for x in ("refus : COMMIT de 40 caractères attendu", "refus annoncé : destruction demandée dans 2 s", "destruction demandée (refus"))
    assert i_refus < i_annonce < i_detruire
    t0 = time.time()
    code, _, sortie, _ = _lancer_amorce(bac, distant, "r2", env_sup={"COMMIT": "abcdef"})
    assert code == 2 and "destruction demandée dans 0 s" in sortie and time.time() - t0 < 60


def test_refus_precoce_attend_aussi(bac):
    distant = _distant(bac)
    t0 = time.time()
    code, _, sortie, racine = _lancer_amorce(bac, distant, env_sup={"FIN_GO_UTC_S": "", "REFUS_ATTENTE_ESSAI_S": "2"})
    assert code == 2 and time.time() - t0 >= 2 and "refus annoncé : destruction demandée dans 2 s" in sortie, sortie[-1200:]
    assert sortie.index("FIN_GO_UTC_S absente") < sortie.index("refus annoncé") and (racine / "t06-detruire").exists()


def test_refus_attente_constante_de_180_s_hors_essai():
    texte = "\n".join(l for l in AMORCE.read_text(encoding="utf-8").splitlines() if not l.lstrip().startswith("#"))
    assert texte.count("REFUS_ATTENTE_S=180") == 1
    assert texte.count('[ "$ESSAI" = 1 ] && REFUS_ATTENTE_S="${REFUS_ATTENTE_ESSAI_S:-0}"') == 1
    assert texte.count("attente_refus; detruire") == 1 and texte.count("attente_refus; echo") == 1
    assert "REFUS_ATTENTE_S=\"${REFUS_ATTENTE_S" not in texte
    assert "sparse-checkout init --no-cone 2>&1" in texte and "2>/dev/null || refus \"extraction partielle" not in texte      # le message de git n'est plus jeté


def test_sparse_liste_exclut_les_dossiers_lourds_et_contient_le_necessaire():
    liste = re.search(r"CHEMINS_CLONAGE='(.*?)'\nT_CLONE0", AMORCE.read_text(encoding="utf-8"), re.S).group(1).splitlines()
    for requis in ("/src/", "/tests/", "/scripts/", "/prereg/", "/donnees/", "/diag/", "/runs/", "/docs/notes/", "/registres/*.md", "/pyproject.toml",
                   "/brouillons/ordres-t06-e2-e3-v5/"):
        assert requis in liste, requis
    for exclu in ("/docs/sources/pdf/", "/docs/sources/", "/registres/", "/registres/passations/", "/docs/", "/brouillons/", "/livrables/", "/gemini/", "/*", "/"):
        assert exclu not in liste, exclu


# --- lanceur v8 : surveillance -----------------------------------------------------------------------------------------------------

VASTAI_V8 = """#!/usr/bin/env bash
# faux vastai de la surveillance v8 : séquences par appel (dernière valeur répétée) ; les clés figurent dans les sorties brutes, comme extra_env chez Vast
printf '%s\\n' "$*" >> "$FAUX_VASTAI_JOURNAL"
cle="$1_$2"; f="$FAUX_COMPTEUR_$cle"; n=$(cat "$f" 2>/dev/null || echo 0); n=$((n + 1)); echo "$n" > "$f"
suite() { local i=0 v last; for v in ${1//,/ }; do i=$((i + 1)); last="$v"; [ "$i" = "$n" ] && { echo "$v"; return; }; done; echo "$last"; }
extra='"extra_env": [["HF_TOKEN", "'"${HF_TOKEN:-}"'"], ["GH_TOKEN", "'"${CONTROLE_IA_GITHUB_TOKEN:-}"'"], ["VAST_API_KEY", "'"${VAST_API_KEY:-}"'"], ["GH2", "'"${GH_TOKEN:-}"'"]]'
if [ "$1" = logs ]; then
    if [ -n "${FAUX_JOURNAL_APRES:-}" ] && [ "$n" -ge 2 ]; then cat "$FAUX_JOURNAL_APRES"; exit "${FAUX_LOGS_CODE_APRES:-0}"; fi
    cat "$FAUX_JOURNAL"; exit 0
fi
if [ "$1 $2" = "show instances" ]; then
    case "$(suite "${FAUX_LISTE:-presente}")" in
        presente) echo '[{"id": 123456, "label": "t06-e2", '"$extra"'}]' ;;
        autre) echo '[{"id": 999, "label": "autre", '"$extra"'}]' ;;
        vide) echo '[]' ;;
        nul) echo 'null' ;;
        illisible) echo 'boum' ;;
        panne) echo "api en panne" >&2; exit 1 ;;
    esac
    exit 0
fi
if [ "$1 $2" = "show instance" ]; then
    case "$(suite "${FAUX_SEULE:-repond}")" in
        repond) echo '{"id": 123456, '"$extra"'}' ;;
        introuvable) echo 'Error 404: instance not found' >&2; exit 1 ;;
        vide) echo '{}' ;;
        illisible) echo 'boum' ;;
        panne) echo "api en panne" >&2; exit 1 ;;
    esac
    exit 0
fi
exit 3
"""


def _surveiller_v8(tmp_path, journal, dossier="s", env_sup=None, duree=None, **champs):
    d = tmp_path / dossier
    _lancement(d, int(time.time()) - 600, **champs)
    env = _env_surveillance(tmp_path, journal)
    b = tmp_path / "bin"
    (b / "vastai").write_text(VASTAI_V8, encoding="utf-8")                         # après _env_surveillance, qui réécrit le faux vastai ordinaire
    env.update(FAUX_VASTAI_JOURNAL=str(tmp_path / "appels.txt"), FAUX_COMPTEUR_=str(tmp_path / "n"), ABSENCE_ATTENTE_S="0")
    env.pop("FAUX_INSTANCES", None)
    env.update(env_sup or {})
    try:
        r = subprocess.run(["bash", str(LANCEUR), "surveillance", "123456", str(d)], env=env, capture_output=True, text=True, timeout=duree or 120)
        return r.returncode, r.stdout + r.stderr, d
    except subprocess.TimeoutExpired as e:
        sortie = e.stdout.decode() if isinstance(e.stdout, bytes) else (e.stdout or "")
        return None, sortie, d


JOURNAL_BON = "AMORCE 2026-11-07T10:00:00Z : commit abc\nAMORCE 2026-11-07T10:00:01Z : CLONAGE mode=jouet secondes=3\nAMORCE 2026-11-07T10:00:05Z : jeton-gh-factice ne doit pas rester\n"


def test_surveillance_v8_liste_non_vide_sans_l_instance_deux_fois_arret_mort(tmp_path):
    code, sortie, d = _surveiller_v8(tmp_path, JOURNAL_BON, env_sup={"FAUX_LISTE": "autre"})
    assert code == 3 and "ARRET mort : instance 123456 absente à deux relevés" in sortie and "stop instance" not in sortie, sortie
    assert "CLONAGE mode=jouet" in (d / "journal-instance.txt").read_text(encoding="utf-8")
    appels = (tmp_path / "appels.txt").read_text(encoding="utf-8").splitlines()
    assert "logs 123456 --tail 20000" in appels and sum(1 for a in appels if a.startswith("show instances")) == 2          # R-1683 : tail 20000


def test_surveillance_v8_liste_non_vide_sans_l_instance_puis_presente_n_arrete_pas(tmp_path):
    code, sortie, d = _surveiller_v8(tmp_path, JOURNAL_BON, env_sup={"FAUX_LISTE": "autre,presente"}, duree=6)
    assert code is None and "ARRET" not in sortie


def test_surveillance_v8_une_liste_vide_n_est_pas_une_absence(tmp_path):
    """R-1683 : `[]` aux deux relevés, l'instance seule répond → ALERTE sur la sortie standard, la surveillance poursuit (jamais ARRET mort)."""
    code, sortie, d = _surveiller_v8(tmp_path, JOURNAL_BON, env_sup={"FAUX_LISTE": "vide", "FAUX_SEULE": "repond"}, duree=7)
    assert code is None and "ARRET" not in sortie and "ALERTE liste d'inventaire non concluante (code 3" in sortie and "instance présente" in sortie, sortie
    assert "show instance 123456 --raw" in (tmp_path / "appels.txt").read_text(encoding="utf-8")



@pytest.mark.parametrize("liste, seule", [("vide", "introuvable"), ("panne", "introuvable")])      # v9 : ("nul", "vide") n'est plus une absence (voir le test suivant)
def test_surveillance_v8_instance_seule_introuvable_deux_fois_arret_mort(tmp_path, liste, seule):
    code, sortie, d = _surveiller_v8(tmp_path, JOURNAL_BON, env_sup={"FAUX_LISTE": liste, "FAUX_SEULE": seule})
    assert code == 3 and "ARRET mort" in sortie and "instance seule introuvable" in sortie, sortie
    appels = (tmp_path / "appels.txt").read_text(encoding="utf-8").splitlines()
    assert sum(1 for a in appels if a.startswith("show instance 123456")) == 2


def test_surveillance_v9_liste_nulle_et_instance_seule_vide_ne_concluent_pas(tmp_path):
    """R-1693 : `null` et `{}` ne sont pas des absences (la v8 les lisait comme « introuvable ») : ARRET inventaire au troisième relevé, jamais ARRET mort."""
    code, sortie, d = _surveiller_v8(tmp_path, JOURNAL_BON, env_sup={"FAUX_LISTE": "nul", "FAUX_SEULE": "vide"})
    assert code == 3 and "ARRET inventaire" in sortie and "ARRET mort" not in sortie, sortie


def test_surveillance_v8_instance_seule_introuvable_une_fois_puis_repond_n_arrete_pas(tmp_path):
    code, sortie, d = _surveiller_v8(tmp_path, JOURNAL_BON, env_sup={"FAUX_LISTE": "vide", "FAUX_SEULE": "introuvable,repond"}, duree=6)
    assert code is None and "ARRET" not in sortie


@pytest.mark.parametrize("seule", ["illisible", "panne"])
def test_surveillance_v8_presence_non_etablie_trois_fois_arret_inventaire_avec_compteur_sur_la_sortie(tmp_path, seule):
    """Artefact : ni la liste ni l'instance seule ne concluent : ALERTE (1/3), (2/3) sur la sortie standard, puis ARRET inventaire — pas d'ARRET mort."""
    code, sortie, d = _surveiller_v8(tmp_path, JOURNAL_BON, env_sup={"FAUX_LISTE": "vide", "FAUX_SEULE": seule, "INTERVALLE": "1"}, duree=60)
    assert code == 3 and "ALERTE inventaire (1/3)" in sortie and "ALERTE inventaire (2/3)" in sortie and "ARRET inventaire" in sortie and "ARRET mort" not in sortie, sortie
    assert "ALERTE inventaire (1/3)" in (d / "surveillance.txt").read_text(encoding="utf-8")


def test_surveillance_v8_le_journal_copie_survit_a_un_releve_sans_journal(tmp_path):
    (tmp_path / "apres.txt").write_text("Error: no such instance 123456\n", encoding="utf-8")
    code, sortie, d = _surveiller_v8(tmp_path, JOURNAL_BON, env_sup={"FAUX_JOURNAL_APRES": str(tmp_path / "apres.txt")}, duree=6)
    assert "CLONAGE mode=jouet" in (d / "journal-instance.txt").read_text(encoding="utf-8")
    assert "no such instance" in (d / "journal-dernier.txt").read_text(encoding="utf-8")


CLES = {"HF_TOKEN": "hf-secret-aaaa1111", "CONTROLE_IA_GITHUB_TOKEN": "gh-secret-bbbb2222", "GH_TOKEN": "ghtok-secret-cccc3333", "VAST_API_KEY": "vast-secret-dddd4444"}


def test_surveillance_v8_masquage_par_un_tube_aucune_cle_sur_le_disque(tmp_path):
    """Chacune des quatre clés figure dans le journal, dans l'inventaire et dans la réponse de show instance : aucune ne reste dans un fichier du dossier,
    aucun fichier brut (`journal-tour.txt`) n'existe."""
    journal = JOURNAL_BON + "".join(f"AMORCE 2026-11-07T10:00:09Z : {nom}={val}\n" for nom, val in CLES.items())
    for k, (liste, seule) in enumerate((("autre,presente", "repond"), ("vide", "repond"))):
        sous = tmp_path / f"cas{k}"
        sous.mkdir()
        code, sortie, d = _surveiller_v8(sous, journal, env_sup={**CLES, "FAUX_LISTE": liste, "FAUX_SEULE": seule}, duree=6)
        assert not (d / "journal-tour.txt").exists()
        texte = "\n".join(f.read_text(encoding="utf-8", errors="replace") for f in d.rglob("*") if f.is_file())
        for nom, val in CLES.items():
            assert val not in texte and val not in sortie, (k, nom)
        fichier = d / ("inventaire-tour.json" if k == 0 else "instance-seule.json")
        assert fichier.exists() and fichier.read_text(encoding="utf-8").count("***") >= 4, fichier


@pytest.mark.parametrize("nom", sorted(CLES))
def test_surveillance_v8_une_cle_presente_de_moins_de_8_caracteres_refuse_la_surveillance(tmp_path, nom):
    code, sortie, d = _surveiller_v8(tmp_path, JOURNAL_BON, env_sup={**CLES, nom: "abc1234"}, duree=30)
    assert code == 2 and ("trop court" in sortie or f"{nom} présente mais de moins de 8 caractères" in sortie), sortie     # HF et GitHub : garde existante ; GH_TOKEN et VAST : garde neuve
    assert nom in ("HF_TOKEN", "CONTROLE_IA_GITHUB_TOKEN") or f"{nom} présente mais de moins de 8 caractères" in sortie
    assert not (d / "journal-dernier.txt").exists()


def test_session_v7_presence_tri_etat_et_instance_seule():
    assert s7.instance_presente([], "1") is None and s7.instance_presente(None, "1") is None and s7.instance_presente({"instances": []}, "1") is None
    assert s7.instance_presente([{"id": 2}], "1") is False and s7.instance_presente([{"id": 1}], "1") is True
    for faux in ("x", [3]):
        with pytest.raises(GardeSession):
            s7.instance_presente(faux, "1")
    assert s7.instance_seule('{"id": 5}', "5") and s7.instance_seule('[{"id": 5}]', "5") and s7.instance_seule('{"instances": [{"id": 5}]}', "5")
    for introuvable in ("{}", "[]", "null", '{"id": 6}', "Error 404: instance not found", "no such instance", "Does not exist"):
        assert s7.instance_seule(introuvable, "5") is False, introuvable
    for illisible in ("boum", "", "<html>"):
        with pytest.raises(GardeSession):
            s7.instance_seule(illisible, "5")


def test_session_v7_main_codes_de_presence(tmp_path):
    for contenu, attendu in (("[]", 3), ("null", 3), ('[{"id": 2}]', 1), ('[{"id": 1}]', 0), ("boum", 2)):
        (tmp_path / "i.json").write_text(contenu, encoding="utf-8")
        assert s7.main(["presente", str(tmp_path / "i.json"), "1"]) == attendu, contenu
    for contenu, attendu in (('{"id": 1}', 0), ("{}", 4), ("Error 404", 4), ("boum", 2)):
        (tmp_path / "s.json").write_text(contenu, encoding="utf-8")
        assert s7.main(["seule", str(tmp_path / "s.json"), "1"]) == attendu, contenu
    assert s7.main(["seule", str(tmp_path / "absent.json"), "1"]) == 2
    cfg = json.loads((RACINE / "docs/notes/g0-deux-semaines-v1/config-t06-epreuve-e2-v2.json").read_text(encoding="utf-8"))
    assert s7.filtre_recherche(cfg, "course") == "num_gpus=1 rentable=true gpu_name=RTX_4090 reliability>=0.98 inet_down>=500 cuda_max_good>=13.0 cpu_ram>=32 cpu_cores_effective>=8 disk_space>=150 dph_total<=0.6"


# --- R-1686 : carte invisible pour torch (pilote trop ancien) ------------------------------------------------------------------------

def _faux_nvidia_smi(tmp_path) -> Path:
    b = tmp_path / "faux-nvidia"
    b.mkdir()
    (b / "nvidia-smi").write_text('#!/usr/bin/env bash\nif [[ "$*" == *noheader* ]]; then echo "535.230.02"; else echo "name, driver_version, memory.total [MiB]"; echo "NVIDIA A100-SXM4-80GB, 535.230.02, 81920 MiB"; fi\n',
                                  encoding="utf-8")
    (b / "nvidia-smi").chmod(0o755)
    return b


def test_carte_invisible_pour_torch_en_mode_reel_refus_qui_cite_le_pilote(bac, tmp_path):
    """Cas sain : carte visible, mode réel → l'épreuve va au bout (test_c_v4_3_amorce_epreuve_cas_sain[reel]). Artefact : torch.cuda.is_available() faux → refus
    immédiat qui cite la version du pilote, cause consignée sur la branche, aucun essai ni run joué."""
    b = _faux_nvidia_smi(tmp_path)
    code, journal, sortie, racine, distant = _epreuve_amorce(bac, "carte", mode="reel", FAUX_CUDA="0", PATH=f"{b}:{os.environ['PATH']}", REFUS_ATTENTE_ESSAI_S="1")
    assert code == 2, sortie[-2500:]
    assert "refus : carte invisible pour torch (torch.cuda.is_available() faux) : pilote 535.230.02, CUDA de torch" in sortie, sortie[-2500:]
    assert "carte invisible pour torch : torch.cuda.is_available() faux ; pilote 535.230.02" in journal and "too old (found version 12020)" in journal
    assert "refus annoncé : destruction demandée dans 1 s" in sortie and (racine / "t06-detruire").exists()
    assert "tests :" not in journal and "run :" not in journal and not (racine / "t06-fin-normale").exists()               # aucun calcul
    assert "arrêt pendant contrôle de la carte" in _git(distant, "log", "--format=%s", "essai/t06-e2-test")                # la cause reste sur la branche


def test_carte_invisible_n_arrete_pas_une_repetition_jouet(bac, tmp_path):
    """La garde ne vaut qu'en mode réel : en jouet (aucune carte), FAUX_CUDA=0 ne change rien."""
    b = _faux_nvidia_smi(tmp_path)
    code, journal, sortie, racine, _ = _epreuve_amorce(bac, "jouet", mode="jouet", FAUX_CUDA="0", PATH=f"{b}:{os.environ['PATH']}")
    assert code == 0 and "carte invisible" not in sortie and (racine / "t06-fin-normale").exists(), sortie[-1500:]


# --- E3 bis sous GO-2026-11-07-08 (ligne à 3 USD) et TESTS_ARGS hors du mode jouet (contre-lecture de la v11, R-1746) ---------------------------------------------------
GO_BIS = "GO-2026-11-07-08"


def _epreuve_amorce_bis(bac, nom, *, plafond_ligne="3 USD", avec_bis=True, mode="jouet", **sup):
    src = bac["source"]
    auj, ech, _ = _dates_epreuve()
    ech_bis = ech + timedelta(days=2)
    fin_bis = datetime.combine(ech_bis + timedelta(days=1), datetime.min.time(), tzinfo=timezone.utc)
    reg = GO + _go_epreuve() + (f"| {GO_BIS} | {auj} | calcul | E3 bis | {plafond_ligne} | {ech_bis} | Lazar | mot |\n" if avec_bis else "")
    (src / "registres" / "go.md").write_text(reg, encoding="utf-8")
    c = _config_epreuve(CONFIG_E2, go_id=GO_BIS)
    c["calendrier"] = {"dernier_jour_creation": str(ech_bis - timedelta(days=1)), "fin_go_utc": fin_bis.strftime("%Y-%m-%dT%H:%M:%SZ")}
    f = src / "prereg" / "config-epreuve.json"
    f.write_text(json.dumps(c, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    sceller(f)
    _commit_source(bac, "épreuve E3 bis")
    env = {"EPREUVE_GO_ID": GO_BIS, "PREREG_ABSENT": "1", "CONFIG": "prereg/config-epreuve.json", "BRANCHE": "essai/t06-e3bis-test", "MODE": mode, "HF_TOKEN": "jeton-hf-factice",
           "FIN_GO_UTC_S": str(int(fin_bis.timestamp())), "ECHEANCE_UTC_S": str(int(fin_bis.timestamp())), "TESTS_ATTENDUS": ""}
    env.update(sup)
    distant = _distant(bac)
    return (*_lancer_amorce(bac, distant, nom, env), distant)


def test_amorce_e3_bis_cas_sain_go_2026_11_07_08_ligne_a_3_usd(bac):
    code, journal, sortie, racine, distant = _epreuve_amorce_bis(bac, "bis")
    assert code == 0, sortie[-2500:]
    assert f"GO : {GO_BIS} conforme (plafond 3 USD" in journal and f"GO={GO_BIS}" in journal and (racine / "t06-fin-normale").exists()


@pytest.mark.parametrize("cas, kw, motif", [("sans_ligne", {"avec_bis": False}, "absent du registre"), ("ligne_a_5_usd", {"plafond_ligne": "5 USD"}, "plafond")])
def test_amorce_e3_bis_artefacts_la_ligne_du_registre_est_verifiee(bac, cas, kw, motif):
    code, journal, sortie, racine, _ = _epreuve_amorce_bis(bac, "bisa", **kw)
    assert code == 2 and (racine / "t06-detruire").exists() and motif in sortie and "run :" not in journal, (cas, sortie[-1500:])


def test_tests_args_refuse_en_mode_reel_meme_pour_une_epreuve(bac):
    code, journal, sortie, racine, _ = _epreuve_amorce(bac, "ta1", mode="reel", TESTS_ARGS="tests/x.py")
    assert code == 2 and "TESTS_ARGS n'est permis qu'en répétition jouet" in sortie and "run :" not in journal, sortie[-1500:]


def test_tests_args_cas_sain_admis_en_epreuve_jouet(bac):
    code, journal, sortie, racine, _ = _epreuve_amorce(bac, "ta2", mode="jouet", TESTS_ARGS="tests/x.py")
    assert code == 0 and "tests/x.py" in (racine / "pytest-args.txt").read_text(encoding="utf-8"), sortie[-1500:]
