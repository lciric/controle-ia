"""Amorce v9 de T0.6 : suite ciblée et figée (E3 du 7 novembre : la suite complète a joué 75 minutes de carte et 50 essais ont échoué sur l'image de l'instance).
Cas sain et artefact (R5) : la liste `scripts/tests-cibles-t06-v2.txt` est jouée telle quelle ; liste absente, altérée, vide, à chemin illisible ou à fichier absent : arrêt avant
tout essai ; `TESTS_ARGS` garde la priorité ; la liste et ses exclusions couvrent exactement les fichiers d'essais du dépôt (aucun fichier omis sans motif)."""
from __future__ import annotations

import hashlib
import re
import shutil
from pathlib import Path

import pytest

import test_t06_v12_amorce as t
from test_t06_v12_amorce import RACINE, _distant, _lancer_amorce, bac  # noqa: F401

AMORCE_V9 = RACINE / "scripts" / "amorce_instance_t06_v10.sh"
LISTE = RACINE / "scripts" / "tests-cibles-t06-v2.txt"
EXCLUS = RACINE / "scripts" / "tests-exclus-t06-v2.txt"
CHEMIN_LISTE = "scripts/tests-cibles-t06-v2.txt"


def _sha(p) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def _fichiers_listes(texte: str):
    return [x for x in texte.splitlines() if x]


def _installer(bac, texte_liste: str, creer=True):
    """Pose la liste dans le dépôt source du banc, avec des fichiers d'essais vides (le faux `python -m pytest` n'en lit aucun), et commit."""
    src = bac["source"]
    (src / "scripts" / "tests-cibles-t06-v2.txt").write_text(texte_liste, encoding="utf-8")
    if creer:
        for f in _fichiers_listes(texte_liste):
            if re.fullmatch(r"tests/test_[A-Za-z0-9_]+\.py", f):
                (src / f).parent.mkdir(parents=True, exist_ok=True)
                (src / f).write_text("", encoding="utf-8")
    t._commit_source(bac, "liste des essais")


def _amorce_a_empreinte(monkeypatch, tmp_path, empreinte: str):
    """Copie de l'amorce dont l'empreinte de la liste écrite en dur est remplacée (pour jouer la liste du banc) ; le banc cite l'empreinte de CETTE copie."""
    texte = AMORCE_V9.read_text(encoding="utf-8")
    nouveau = re.sub(r'LISTE_SHA256="[0-9a-f]{64}"', f'LISTE_SHA256="{empreinte}"', texte, count=1)
    assert nouveau != texte
    copie = tmp_path / "amorce_instance_t06_v10.sh"
    copie.write_text(nouveau, encoding="utf-8")
    monkeypatch.setattr(t, "AMORCE", copie)


def _arguments_pytest(racine) -> str:
    return (racine / "pytest-args.txt").read_text(encoding="utf-8").strip()


def test_empreinte_ecrite_en_dur_egale_celle_de_la_liste_du_depot():
    m = re.search(r'LISTE_SHA256="([0-9a-f]{64})"', AMORCE_V9.read_text(encoding="utf-8"))
    assert m, "empreinte de la liste absente de l'amorce"
    assert m.group(1) == _sha(LISTE), "la liste du dépôt n'est plus celle que l'amorce cite : réécrire l'amorce (nom neuf, R12)"


def _banc(tmp_path_factory, monkeypatch, texte_liste, empreinte=None, creer=True):
    """Construit un banc (copie de la fixture `bac`) dont l'amorce citée est la copie à empreinte de liste substituée."""
    tmp = tmp_path_factory.mktemp("liste")
    _amorce_a_empreinte(monkeypatch, tmp, empreinte or hashlib.sha256(texte_liste.encode()).hexdigest())
    b = t.fabriquer_bac(tmp)
    _installer(b, texte_liste, creer)
    return b


@pytest.mark.parametrize("texte", ["tests/test_alpha.py\ntests/test_beta_v2.py\n", "tests/test_seul.py\n"])
def test_sain_la_liste_est_jouee_et_journalisee(tmp_path_factory, monkeypatch, texte):
    b = _banc(tmp_path_factory, monkeypatch, texte)
    code, journal, sortie, racine = _lancer_amorce(b, _distant(b), env_sup={"TESTS_ATTENDUS": "7"})
    assert code == 0, sortie[-1500:]
    fichiers = _fichiers_listes(texte)
    assert _arguments_pytest(racine) == "-m pytest -q -p no:cacheprovider --color=no " + " ".join(fichiers), _arguments_pytest(racine)
    assert f"suite ciblée : {len(fichiers)} fichiers d'essais" in journal and "tests : 7 passed" in journal


@pytest.mark.parametrize("cas, texte, creer, attendu", [
    ("vide", "", True, "liste vide"),
    ("chemin_illisible", "tests/test_ok.py\n../tests/test_evade.py\n", True, "chemin illisible dans la liste : ../tests/test_evade.py"),
    ("chemin_hors_tests", "scripts/lancer_t06_v12.sh\n", True, "chemin illisible dans la liste : scripts/lancer_t06_v12.sh"),
    ("fichier_absent_du_depot", "tests/test_present.py\ntests/test_absent.py\n", False, "essai absent du dépôt : tests/test_present.py"),
])
def test_artefacts_liste_refusee_avant_tout_essai(tmp_path_factory, monkeypatch, cas, texte, creer, attendu):
    b = _banc(tmp_path_factory, monkeypatch, texte, creer=creer)
    code, journal, sortie, racine = _lancer_amorce(b, _distant(b), env_sup={"TESTS_ATTENDUS": "7"})
    assert code != 0 and attendu in journal + sortie and "arrêt avant tout essai" in journal + sortie, (journal + sortie)[-1500:]
    assert not (racine / "pytest-args.txt").exists(), "aucun essai ne doit être joué"
    assert "run : " not in journal


def test_artefact_liste_alteree_l_empreinte_ne_correspond_plus(tmp_path_factory, monkeypatch):
    texte = "tests/test_alpha.py\n"
    b = _banc(tmp_path_factory, monkeypatch, texte, empreinte=hashlib.sha256(b"autre liste\n").hexdigest())
    code, journal, sortie, racine = _lancer_amorce(b, _distant(b), env_sup={"TESTS_ATTENDUS": "7"})
    assert code != 0 and "empreinte de scripts/tests-cibles-t06-v2.txt ≠ celle de l'amorce" in journal + sortie
    assert not (racine / "pytest-args.txt").exists() and "run : " not in journal


def test_artefact_liste_absente_jamais_de_repli_sur_la_suite_complete(tmp_path_factory, monkeypatch):
    b = _banc(tmp_path_factory, monkeypatch, "tests/test_alpha.py\n")
    (b["source"] / "scripts" / "tests-cibles-t06-v2.txt").unlink()
    t._commit_source(b, "liste retirée")
    code, journal, sortie, racine = _lancer_amorce(b, _distant(b), env_sup={"TESTS_ATTENDUS": "7"})
    assert code != 0 and "absente" in journal + sortie and not (racine / "pytest-args.txt").exists()


def test_tests_args_a_la_priorite_en_repetition_jouet(bac):
    code, journal, sortie, racine = _lancer_amorce(bac, _distant(bac), env_sup={"TESTS_ARGS": "tests/x.py,tests/y.py", "TESTS_ATTENDUS": "7", "PREREG_ABSENT": "1", "CONFIG": t.CONFIG})
    assert code == 0, sortie[-1500:]
    assert _arguments_pytest(racine) == "-m pytest -q -p no:cacheprovider --color=no tests/x.py tests/y.py" and "suite ciblée" not in journal


# --- la liste réelle et ses exclusions -----------------------------------------------------------------------------------------------------
def _exclus_depuis(texte: str) -> dict:
    out = {}
    for ligne in texte.splitlines():
        if ligne.strip() and not ligne.startswith("#"):
            chemin, _, motif = ligne.partition("\t")
            if chemin in out:
                raise AssertionError(f"doublon dans les exclusions : {chemin}")        # v11 : un doublon n'est plus écrasé en silence (lecture en dictionnaire)
            out[chemin] = motif.strip()
    return out


def _exclus():
    return _exclus_depuis(EXCLUS.read_text(encoding="utf-8"))


def test_un_doublon_dans_les_exclusions_est_detecte_cas_sain_et_artefact():
    assert _exclus_depuis("# c\ntests/test_a.py\tmotif écrit\ntests/test_b.py\tmotif écrit\n") == {"tests/test_a.py": "motif écrit", "tests/test_b.py": "motif écrit"}
    with pytest.raises(AssertionError, match="doublon dans les exclusions"):
        _exclus_depuis("tests/test_a.py\tmotif un\ntests/test_a.py\tmotif deux\n")


def test_les_motifs_des_fichiers_de_l_hote_durable_ne_disent_pas_a_tort_qu_ils_ont_echoue():
    """Contre-lecture R-1746 : le motif « échecs à E3 » ne vaut que pour les fichiers qui ont échoué (v3_v3, v3_v4, sonde v10)."""
    echoues = {"tests/test_hote_durable_a1_v3_v3.py", "tests/test_hote_durable_a1_v3_v4.py", "tests/test_sonde_hote_durable_a1_v3_v10.py"}
    for f, motif in _exclus().items():
        if "hote_durable" in f:
            assert ("échec" in motif and "à E3" in motif) == (f in echoues), (f, motif)


def test_liste_reelle_et_exclusions_couvrent_exactement_les_fichiers_d_essais():
    listes = _fichiers_listes(LISTE.read_text(encoding="utf-8"))
    exclus = _exclus()
    existants = sorted(f"tests/{p.name}" for p in (RACINE / "tests").glob("test_*.py"))
    assert len(set(listes)) == len(listes) and not (set(listes) & set(exclus)), "doublon ou fichier à la fois listé et exclu"
    assert all(re.fullmatch(r"tests/test_[A-Za-z0-9_]+\.py", f) for f in listes)
    manquants = [f for f in existants if f not in listes and f not in exclus]
    assert not manquants, f"fichiers d'essais ni dans la liste ni dans les exclusions motivées (décider, jamais d'omission silencieuse) : {manquants}"
    inconnus = [f for f in [*listes, *exclus] if f not in existants]
    assert not inconnus, f"liste ou exclusions citent des fichiers absents du dépôt : {inconnus}"
    assert all(len(m) >= 20 for m in exclus.values()), "chaque exclusion porte un motif écrit"
    assert "tests/test_t06_v12_liste.py" in listes and "tests/test_t06_v12_minuterie.py" in listes and "tests/test_t06_v11_nouveaux.py" in listes


def test_la_liste_exclut_l_hote_durable_et_ne_contient_que_des_fichiers_compilables_sous_python_3_11():
    listes = _fichiers_listes(LISTE.read_text(encoding="utf-8"))
    assert not [f for f in listes if "hote_durable" in f]
    import subprocess
    py311 = shutil.which("python3.11")
    if py311 is None:
        pytest.skip("python3.11 absent de cette machine : contrôle de syntaxe 3.11 non joué ici (l'image de l'instance est en 3.11 ; une erreur de syntaxe y ferait échouer la suite avant le run)")
    for f in listes:
        r = subprocess.run([py311, "-m", "py_compile", str(RACINE / f)], capture_output=True, text=True)
        assert r.returncode == 0, (f, r.stderr[-300:])
