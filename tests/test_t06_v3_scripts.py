"""Scripts de la chaîne de T0.6 v3 (`scripts/amorce_instance_t06_v3.sh`, `scripts/lancer_t06_v3.sh`) : les essais de la v2
rejoués tels quels sur les scripts v3 (dépôt distant local, `python`, `vastai`, `df` et `curl` factices, aucune installation,
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
AMORCE = RACINE / "scripts" / "amorce_instance_t06_v3.sh"
LANCEUR = RACINE / "scripts" / "lancer_t06_v3.sh"
CONFIG_REELLE = RACINE / "docs" / "notes" / "g0-deux-semaines-v1" / "config-t06-reel-v1-brouillon3.json"
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
if [ "$1" = "-m" ] && [ "$2" = "pytest" ]; then printf '%s\\n' "${FAUX_PYTEST_LIGNE:-7 passed in 1.00s}"; exit 0; fi
if [ "$1" = "-m" ] && [ "$2" = "pip" ]; then echo "paquet-factice==1.0"; exit 0; fi
if [ "$1" = "-c" ]; then echo "torch factice"; exit 0; fi
if [ "$1" = "-m" ] && [ "$2" = "controle_ia.t06.lanceur_v3" ]; then
    run=""; prec=""
    for a in "$@"; do [ "$prec" = "--run-id" ] && run="$a"; prec="$a"; done
    mkdir -p "diag/$run" "runs/$run" "donnees/$run"
    echo '{"factice": true}' > "runs/$run/manifeste.json"
    for f in adaptateur-saboteur.pt adaptateur-temoin.pt mesures-t06.npz textes-actions-t06.jsonl activations-sous-ensemble-t06-manifeste.json \
             activations-sous-ensemble-t06-000.npz activations-sous-ensemble-t06-001.npz; do
        echo "$f factice" > "donnees/$run/$f"; (cd "donnees/$run" && sha256sum "$f" > "$f.sha256")
    done
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
              f"- Amorce : `scripts/amorce_instance_t06_v3.sh` (`{amorce_sha}`, sha256)"]
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
        f.write_text(CONFIG_REELLE.read_text(encoding="utf-8") if chemin == CONFIG else "{}", encoding="utf-8")
        sceller(f)
    (src / "src" / "controle_ia" / "t06").mkdir(parents=True)
    for nom in ("__init__.py", "gardes.py", "scellement.py"):
        shutil.copy(RACINE / "src" / "controle_ia" / nom, src / "src" / "controle_ia" / nom)
    (src / "src" / "controle_ia" / "t06" / "__init__.py").write_text("", encoding="utf-8")
    for nom in ("session.py", "session_v2.py"):
        shutil.copy(RACINE / "src" / "controle_ia" / "t06" / nom, src / "src" / "controle_ia" / "t06" / nom)
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


def _fichiers_distants(distant, branche="calcul/t06-jouet-v3"):
    return _git(distant, "ls-tree", "-r", "-l", branche).splitlines()


def test_amorce_cas_sain_deux_commits_morceaux_et_second_demarrage(bac):
    distant = _distant(bac)
    code, journal, sortie, racine = _lancer_amorce(bac, distant)
    assert code == 0, sortie[-3000:]
    assert "GO : GO-2026-11-02-28 conforme" in journal and "lanceur v3" in journal and "run terminé" in journal and "calendrier : fin_go_utc_s=1794873600" in journal
    assert [x for x in journal.splitlines() if x.startswith("PROGRES ")] == PROGRES_ATTENDUS           # C01 : la ligne à état retenue
    assert "PROGRES non relayée : motif interdit (C01)" in journal and "au-dessus" not in journal and "au-dessus" not in sortie
    assert "ACTION" not in journal and "PRIVATE" not in journal and "jeton-factice" not in sortie
    assert " : fin, code 0" in sortie and (racine / "t06-arret-demande").read_text().startswith("stopped")
    assert (racine / "t06-fin-normale").exists() and (racine / "t06-consigner.sh").exists() and not (racine / "t06-detruire").exists()
    assert (racine / "t06-echeance.txt").read_text().strip() == FIN_GO and (racine / "t06-depense-epuisee-utc.txt").read_text().strip().isdigit()
    messages = _git(distant, "log", "--format=%s", "calcul/t06-jouet-v3").splitlines()
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
    assert "second démarrage" in _git(distant, "log", "-1", "--format=%s", "calcul/t06-jouet-v3")
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
    assert "second démarrage" in _git(distant, "log", "-1", "--format=%s", "calcul/t06-jouet-v3")              # poussé AVANT la destruction
    assert any(f.endswith("diag/apres/note.json") for f in _fichiers_distants(distant)) and "branche calcul/t06-jouet-v3 poussée (second démarrage)" in journal2
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
    assert code == 0, sortie[-3000:]
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
    assert code == 2 and "poussée initiale de la branche calcul/t06-jouet-v3 refusée" in sortie and (racine / "t06-detruire").exists()
    assert "tests :" not in journal and "run :" not in journal


def test_amorce_poussee_finale_refusee_trois_fois_puis_second_demarrage(bac):
    distant = _distant(bac, REFUS_MISES_A_JOUR)
    code, journal, sortie, racine = _lancer_amorce(bac, distant, "pf")
    assert code == 1, sortie[-3000:]
    assert journal.count("poussée : tentative 3 refusée") >= 1 and "poussée finale impossible après trois tentatives" in journal
    assert " : fin, code 1" in sortie and (racine / "t06-fin-normale").exists() and (racine / "t06-arret-demande").exists()
    assert _git(distant, "log", "--format=%s", "calcul/t06-jouet-v3").splitlines() == ["init"]      # seule la création est passée
    assert "résultats et données légères" in _git(racine / "amorce-depot", "log", "--format=%s", "-3")  # committés sur l'instance
    code2, journal2, sortie2, _ = _lancer_amorce(bac, distant, "pf")
    assert code2 == 0 and "second démarrage" in sortie2 and "poussée : tentative 3 refusée" in journal2 and (racine / "t06-sommeil").exists()
    # le crochet levé, un troisième démarrage pousse tout
    (distant / "hooks" / "pre-receive").unlink()
    code3, journal3, _, _ = _lancer_amorce(bac, distant, "pf")
    assert code3 == 0 and "branche calcul/t06-jouet-v3 poussée (second démarrage)" in journal3
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
    assert "arrêt pendant run" in _git(distant, "log", "-3", "--format=%s", "calcul/t06-jouet-v3") and not (racine / "t06-fin-normale").exists()
    # redémarrage d'un run interrompu (ni fin normale, ni dépense épuisée) : partiels consignés, destruction
    (racine / "amorce-depot" / "diag" / "tard").mkdir()
    (racine / "amorce-depot" / "diag" / "tard" / "x.json").write_text("{}", encoding="utf-8")
    code2, _, sortie2, _ = _lancer_amorce(bac, distant, "a")
    assert code2 == 2 and "run interrompu" in sortie2 and (racine / "t06-detruire").exists()
    assert "redémarrage d'un run interrompu" in _git(distant, "log", "-1", "--format=%s", "calcul/t06-jouet-v3")
    distant2 = _distant(bac)
    code, journal, sortie, racine = _lancer_amorce(bac, distant2, "m", {"FAUX_RUN": "mort"})
    assert code == 1 and "RUN MORT sans résumé ni arrêt consigné (code 137)" in sortie and "RUN MORT" in journal
    assert "run mort" in _git(distant2, "log", "-3", "--format=%s", "calcul/t06-jouet-v3") and (racine / "t06-arret-demande").exists()


def test_amorce_refus_go_et_branche_presente(bac):
    distant = _distant(bac)
    subprocess.run(["git", "-C", str(bac["source"]), "push", "-q", str(distant), "HEAD:refs/heads/calcul/t06-jouet-v3"], check=True)
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
    messages = _git(distant, "log", "--format=%s", "-3", "calcul/t06-jouet-v3")
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
    env = {k: os.environ[k] for k in ENV_DE_BASE if k in os.environ}
    env.update(PATH=f"{b}:{env.get('PATH', '')}", HF_TOKEN="jeton-hf-factice", CONTROLE_IA_GITHUB_TOKEN="jeton-gh-factice",
               FAUX_JOURNAL=str(tmp_path / "journal.txt"), INTERVALLE="1", HOME=str(tmp_path))
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
    return env


def _creer(src, tmp_path, d, *args, **sup):
    return subprocess.run(["bash", str(LANCEUR), "creation", *args, str(d)], env=_env_session(src, tmp_path, **sup), capture_output=True, text=True, timeout=120)


def test_controles_disque_simule_et_commande_de_creation(depot_session, tmp_path):
    src = depot_session
    d = tmp_path / "controles"
    # C10 : place disque simulée par un `df` factice : 2,5 Go libres → refus ; 5 Go → conforme (jamais le disque de l'hôte)
    r = subprocess.run(["bash", str(LANCEUR), "controles", str(tmp_path / "c0"), "2026-11-05"], env=_env_session(src, tmp_path, FAUX_DF_LIBRE_KO="2500000"),
                       capture_output=True, text=True, timeout=120)
    assert r.returncode == 2 and "place disque : 2500000 ko libres" in r.stdout
    r = subprocess.run(["bash", str(LANCEUR), "controles", str(d), "2026-11-05"], env=_env_session(src, tmp_path), capture_output=True, text=True, timeout=120)
    assert r.returncode == 0, r.stdout + r.stderr
    assert "CONTRÔLES CONFORMES" in r.stdout and "GO-2026-11-02-28 conforme" in r.stdout and "fin_go_utc_s=1794873600 dernier_jour_creation=2026-11-15" in r.stdout
    lancement = (d / "lancement.txt").read_text(encoding="utf-8")
    assert lancement.count("commit ") == 1 and f"config {CONFIG}" in lancement and (d / "config.json").exists()
    # C12, C15 : offre relue par l'outil, prix lus dans l'offre, instances inventoriées, dépense antérieure cumulée, heure d'épuisement
    r = _creer(src, tmp_path, d, "9999", "course", "20")
    assert r.returncode == 0, r.stdout + r.stderr
    cmd = r.stdout.splitlines()[-1]
    assert cmd.startswith("GO_ID=GO-2026-11-02-28 timeout -k 10 300 vastai create instance 9999 ") and "--disk 150" in cmd and "--label t06-v2" in cmd
    assert "jeton-hf-factice" not in cmd and "$HF_TOKEN" in cmd and "ECHEANCE_UTC_S=1794873600" in cmd and "FIN_GO_UTC_S=1794873600" in cmd
    assert "-e BRANCHE=calcul/t06-reel-v3" in cmd and "amorce_instance_t06_v2" not in cmd and "base64 -d > /root/amorce.sh" in cmd
    epuis = int(cmd.split("DEPENSE_EPUISEE_UTC_S=")[1].split()[0])
    assert abs(epuis - (int(time.time()) + (200 - 20 - 1.2) / 1.12 * 3600)) < 120            # C08 : (200 − 20 − 1,2) / (1,1 + 0,02) h
    assert "OFFRE CONFORME : id=9999 prix_carte=1.1000 prix_stockage=0.0200 telechargement=0.0300 telechargement_forfait=1.2000" in r.stdout
    assert "prix_carte 1.1000" in (d / "lancement.txt").read_text(encoding="utf-8") and "anterieure 20" in (d / "lancement.txt").read_text(encoding="utf-8")
    # C-V3-3 : l'offre est relue au disque demandé par la configuration (150 Go), avant l'inventaire des instances
    appels = (tmp_path / "vastai-appels.txt").read_text(encoding="utf-8").splitlines()
    assert appels == ["search offers id=9999 --storage 150 --raw", "show instances --raw"] and "storage 150" in (d / "lancement.txt").read_text(encoding="utf-8")
    assert "amorce_instance_t06_v3" not in cmd and "lancer_t06_v3.sh apres-creation" in cmd
    # artefacts : offre hors des bornes (prix 1,31 → code 3) ; mauvaise carte ; relance H200 conforme ; instance présente ; dépense épuisée
    (tmp_path / "offre.json").write_text(json.dumps([{**OFFRE, "dph_total": 1.31}]), encoding="utf-8")
    r = _creer(src, tmp_path, d, "9999", "course", "0")
    assert r.returncode == 3 and "nœud" in r.stdout and "prix 1.31" in r.stdout
    (tmp_path / "offre.json").write_text(json.dumps([{**OFFRE, "gpu_name": "H200 NVL", "gpu_ram": 143000, "dph_total": 4.6}]), encoding="utf-8")
    r = _creer(src, tmp_path, d, "9999", "course", "0")
    assert r.returncode == 3 and "carte 'H200 NVL'" in r.stdout
    r = _creer(src, tmp_path, d, "9999", "relance", "53.3")
    assert r.returncode == 0 and "carte=H200 NVL" in r.stdout and "DEPENSE_EPUISEE_UTC_S=" in r.stdout.splitlines()[-1]
    inst = tmp_path / "instances.json"
    inst.write_text(json.dumps([{"id": 5, "label": "t06-v2", "actual_status": "running", "cur_state": "running"}]), encoding="utf-8")
    r = _creer(src, tmp_path, d, "9999", "relance", "0", FAUX_INSTANCES=str(inst))
    assert r.returncode == 3 and "déjà sur le compte : 5" in r.stdout
    (tmp_path / "offre.json").write_text(json.dumps([OFFRE]), encoding="utf-8")
    r = _creer(src, tmp_path, d, "9999", "course", "199")
    assert r.returncode == 3 and "déjà au plafond" in r.stdout
    r = _creer(src, tmp_path, d, "9999", "autre", "0")
    assert r.returncode == 2 and "course ou relance" in r.stdout
    r = subprocess.run(["bash", str(LANCEUR), "creation", "9999", "course", "0", str(d), "1794873601"], env=_env_session(src, tmp_path),
                       capture_output=True, text=True, timeout=120)
    assert r.returncode == 2 and "échéance 1794873601 hors de" in r.stdout
    r = _creer(src, tmp_path, tmp_path / "vide", "9999", "course", "0")
    assert r.returncode == 2 and "contrôles absents" in r.stdout
    # apres-creation : identifiant lu, sortie brute effacée, création écrite pour la surveillance
    f = tmp_path / "brut.json"
    f.write_text(json.dumps({"success": True, "new_contract": 424242}), encoding="utf-8")
    r = subprocess.run(["bash", str(LANCEUR), "apres-creation", str(f), "0", str(d)], capture_output=True, text=True, timeout=60)
    assert r.returncode == 0 and "CRÉÉE : instance 424242" in r.stdout and not f.exists()
    assert "instance 424242" in (d / "lancement.txt").read_text(encoding="utf-8") and "surveillance 424242" in r.stdout


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
