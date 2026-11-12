"""Chaîne v13 de T0.6 (lanceur `scripts/lancer_t06_v13.sh`, amorce `scripts/amorce_instance_t06_v11.sh`, `session_v12`, `configuration_v6`, `lanceur_v6`) :
plus aucun identifiant de GO d'épreuve écrit en dur (contre-lecture CLE3T-01 de l'ordre E3 ter). L'identifiant vient de la variable d'environnement `GO_ID`, la ligne est
lue dans `registres/go.md` (présente, type « calcul », accordée par Lazar, non échue, non révoquée), et le plafond de l'épreuve est borné par celui de la ligne.
Cas sain et artefacts (R5) : identifiant absent du registre, ligne de type « décision », ligne échue, plafond insuffisant, `GO_ID` vide ; chaque artefact arrête avec le
code attendu et ne crée rien. Les fixtures et les faux outils des essais v12 sont réutilisés ; aucun réseau, aucun appel à Vast."""
from __future__ import annotations

import difflib
import json
import os
import re
import shutil
import subprocess
from datetime import timedelta
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.scellement import sceller
from controle_ia.t06 import configuration_v5 as cf5
from controle_ia.t06 import configuration_v6 as cf6
from controle_ia.t06 import lanceur_v6 as la6
from controle_ia.t06 import session_v11 as s11
from controle_ia.t06 import session_v12 as s12
from controle_ia.t06.session import GardeSession
import test_t06_v12_amorce as t
from test_t06_v12_amorce import (CONFIG_E2, GO, RACINE, _commit_source, _config_epreuve, _dates_epreuve, _distant, _git, _lancer_amorce,  # noqa: F401
                                 _outils, fabriquer_bac)
from test_t06_v12_scripts import DF_FACTICE, OFFRES, VAST_REEL, env5

LANCEUR13 = RACINE / "scripts" / "lancer_t06_v13.sh"
LANCEUR12 = RACINE / "scripts" / "lancer_t06_v12.sh"
AMORCE11 = RACINE / "scripts" / "amorce_instance_t06_v11.sh"
AMORCE10 = RACINE / "scripts" / "amorce_instance_t06_v10.sh"
D = RACINE / "docs" / "notes" / "g0-deux-semaines-v1"
COURSE = "GO-2026-11-02-28"
NEUF = "GO-2099-01-01-01"           # ligne neuve d'épreuve (calcul, 16 USD), le modèle de la ligne d'E3 ter
DECISION = "GO-2099-01-01-02"       # ligne de type « décision », sans plafond
ECHU = "GO-2099-01-01-03"           # ligne de calcul échue hier
PETIT = "GO-2099-01-01-04"          # ligne de calcul à 3 USD
ABSENT = "GO-2099-01-01-09"         # aucun tel identifiant au registre
ENTETE = GO.split("\n")[0] + "\n" + GO.split("\n")[1] + "\n"
ANCIENS = ("GO-2026-11-06-01", "GO-2026-11-07-08")


def _lignes_go(plafond_neuf="16 USD"):
    auj, ech, _ = _dates_epreuve()
    return (f"| {NEUF} | {auj} | calcul | E3 ter de T0.6, galop d'essai de la garde d'équivalence | {plafond_neuf} | {ech} | Lazar | mot |\n"
            f"| {DECISION} | {auj} | décision | un nœud tranché, aucune dépense | — | {ech} | Lazar | mot |\n"
            f"| {ECHU} | {auj - timedelta(days=10)} | calcul | épreuve ancienne | 16 USD | {auj - timedelta(days=1)} | Lazar | mot |\n"
            f"| {PETIT} | {auj} | calcul | petite épreuve | 3 USD | {ech} | Lazar | mot |\n")


def _registre(tmp_path, nom="go.md", lignes=None) -> Path:
    reg = tmp_path / nom
    reg.write_text(GO + (_lignes_go() if lignes is None else lignes), encoding="utf-8")
    return reg


# =========================================================================================================================================================
# 1. `session_v12` : la ligne est lue, jamais écrite en dur
# =========================================================================================================================================================
def test_session_v12_cas_sain_ligne_neuve_lue_au_registre(tmp_path):
    reg = _registre(tmp_path)
    r = s12.ligne_go_calcul(reg, NEUF)
    assert r["plafond_usd"] == 16.0 and r["go"] == NEUF
    assert s12.plafond_de_la_ligne(reg, PETIT) == 3.0 and s12.plafond_de_la_ligne(reg, COURSE) == 200.0
    assert "≤ 16.0" in s12.verifier_plafond_epreuve("15", "0", NEUF, reg)
    assert "≤ 16.0" in s12.verifier_plafond_epreuve("16", "0", NEUF, reg)                                   # borne incluse (comme la course : configuration 200 = ligne 200)
    assert "≤ 16.0" in s12.verifier_plafond_epreuve("10.3", "5.7", NEUF, reg)


@pytest.mark.parametrize("go, motif", [(ABSENT, "absent du registre"), (DECISION, "type 'décision'"), (ECHU, "hors de sa période de validité"),
                                       ("", "illisible"), ("GO-X", "illisible"), ("n'importe quoi", "illisible")])
def test_session_v12_artefacts_ligne_absente_decision_echue_ou_identifiant_vide(tmp_path, go, motif):
    reg = _registre(tmp_path)
    with pytest.raises(GardeSession, match=re.escape(motif)):
        s12.ligne_go_calcul(reg, go)
    with pytest.raises(GardeSession, match=re.escape(motif)):
        s12.verifier_plafond_epreuve("1", "0", go, reg)


@pytest.mark.parametrize("plafond, ant, go, motif", [
    ("16.01", "0", NEUF, "> 16.0"), ("15", "1.5", NEUF, "> 16.0"), ("5.7", "0", PETIT, "> 3.0"), ("0", "0", NEUF, "> 0 exigé"),
    ("-1", "0", NEUF, "> 0 exigé"), ("15", "-0.5", NEUF, "≥ 0 exigé"), ("abc", "0", NEUF, "illisible"), ("15", "x", NEUF, "illisible"), ("nan", "0", NEUF, "non fini"),
])
def test_session_v12_artefacts_plafond_insuffisant_ou_illisible(tmp_path, plafond, ant, go, motif):
    with pytest.raises(GardeSession, match=re.escape(motif)):
        s12.verifier_plafond_epreuve(plafond, ant, go, _registre(tmp_path))


def test_session_v12_artefacts_registre_absent_revocation_plafond_illisible_et_doublon(tmp_path):
    auj, ech, _ = _dates_epreuve()
    with pytest.raises(GardeSession, match="registre .* absent"):
        s12.ligne_go_calcul(tmp_path / "nulle-part.md", NEUF)
    reg = _registre(tmp_path, lignes=_lignes_go() + f"| GO-2099-01-01-05 | {auj} | révocation | révoque {NEUF} | — | {ech} | Lazar | mot |\n")
    with pytest.raises(GardeSession, match="révoqué"):
        s12.ligne_go_calcul(reg, NEUF)
    reg = _registre(tmp_path, lignes=_lignes_go("— (plafonds des GO de calcul cités)"))
    with pytest.raises(GardeSession, match="plafond .* illisible"):
        s12.ligne_go_calcul(reg, NEUF)
    reg = _registre(tmp_path, lignes=_lignes_go() + f"| {NEUF} | {auj} | calcul | seconde ligne, pas une extension | 30 USD | {ech} | Lazar | mot |\n")
    with pytest.raises(GardeSession, match="en double"):
        s12.ligne_go_calcul(reg, NEUF)


def test_session_v12_ligne_de_commande_codes_et_sorties(tmp_path):
    reg = str(_registre(tmp_path))
    auj = str(_dates_epreuve()[0])
    sortie = []
    def main(*argv):
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            code = s12.main(list(argv))
        sortie.append(buf.getvalue().strip())
        return code
    assert main("go-ligne", reg, NEUF) == 0 and sortie[-1].startswith(f"{NEUF} conforme (plafond 16 USD, {auj} → ")
    assert main("plafond-ligne", reg, NEUF, auj) == 0 and sortie[-1] == "16"
    assert main("plafond", "15", "0", NEUF, reg) == 0 and "≤ 16.0" in sortie[-1]
    assert main("plafond", "15", "0", NEUF, reg, auj) == 0
    for argv, motif in ((("go-ligne", reg, ABSENT), "absent du registre"), (("plafond-ligne", reg, DECISION), "type 'décision'"), (("go-ligne", reg, ECHU), "validité"),
                        (("plafond", "16.5", "0", NEUF, reg), "> 16.0"), (("plafond", "1", "0", "", reg), "illisible"), (("go-ligne", reg, NEUF, "pas-une-date"), "Invalid isoformat")):
        assert main(*argv) == 1 and motif in sortie[-1], (argv, sortie[-1])
    assert main("plafond", "15", "0", NEUF) == 2                                        # l'ancien appel à quatre arguments (v11, sans registre) n'est plus servi : usage, jamais un repli
    assert main("seule", str(tmp_path / "absent.json"), "123") == 2                       # les autres sous-commandes restent celles de la v11


def test_artefact_la_v11_refuse_la_ligne_neuve_en_dur_et_la_v12_la_lit(tmp_path):
    with pytest.raises(GardeSession, match="refusé"):
        s11.verifier_plafond_epreuve("15", "0", NEUF)
    assert "≤ 16.0" in s12.verifier_plafond_epreuve("15", "0", NEUF, _registre(tmp_path))
    assert s12.instance_seule is s11.instance_seule and s12.identifiants_nommes is s11.identifiants_nommes      # rien d'autre ne change


# =========================================================================================================================================================
# 2. `configuration_v6` et `lanceur_v6`
# =========================================================================================================================================================
def _epreuve(plafond, go=NEUF):
    c = json.loads((D / "config-t06-epreuve-e3-v3.json").read_text(encoding="utf-8"))          # configuration d'épreuve réelle du dépôt (E3 v3, plafond 4,3)
    c["plafond_usd"] = plafond
    c["go_id"] = go
    return c


@pytest.mark.parametrize("plafond", [0.01, 4.3, 8, 8.01, 15, 15.9, 16, 16.0])
def test_v6_accepte_un_plafond_d_epreuve_jusqu_au_plafond_de_la_ligne(tmp_path, plafond):
    cf6.exiger_config_t06_v6(_epreuve(plafond), _registre(tmp_path))


@pytest.mark.parametrize("plafond", [16.01, 17, 200, 0, -1, float("nan"), float("inf"), True, "15", None])
def test_v6_refuse_un_plafond_d_epreuve_hors_de_la_ligne_ou_illisible(tmp_path, plafond):
    with pytest.raises(GardeArret, match="plafond"):
        cf6.exiger_config_t06_v6(_epreuve(plafond), _registre(tmp_path))


@pytest.mark.parametrize("go, motif", [(ABSENT, "absent du registre"), (DECISION, "type 'décision'"), (ECHU, "validité"), (PETIT, "> plafond 3 USD")])
def test_v6_artefacts_ligne_absente_decision_echue_ou_trop_petite(tmp_path, go, motif):
    with pytest.raises(GardeArret, match=re.escape(motif)):
        cf6.exiger_config_t06_v6(_epreuve(4.3, go), _registre(tmp_path))


def test_v6_sans_registre_aucune_validation_d_epreuve_jamais_un_repli(tmp_path):
    with pytest.raises(GardeArret, match="registre des GO exigé"):
        cf6.exiger_config_t06_v6(_epreuve(4.3))
    with pytest.raises(GardeArret, match="registre des GO exigé"):
        cf6.exiger_config_t06_v6(_epreuve(0.5), None)


def test_v6_est_epreuve_tout_go_lisible_autre_que_la_course_et_la_course_inchangee(tmp_path):
    assert cf6.est_epreuve(_epreuve(4.3)) and cf6.est_epreuve(_epreuve(4.3, PETIT)) and cf6.est_epreuve(_epreuve(4.3, "GO-2026-11-06-01"))
    assert not cf6.est_epreuve(_epreuve(4.3, COURSE)) and not cf6.est_epreuve(_epreuve(4.3, "GO-X")) and not cf6.est_epreuve({"go_id": None}) and not cf6.est_epreuve({})
    c = json.loads((D / "config-t06-reel-v1-brouillon5.json").read_text(encoding="utf-8"))
    cf5.exiger_config_t06_v5(c)
    cf6.exiger_config_t06_v6(c)                                                   # la course se valide sans registre, comme en v5
    cf6.exiger_config_t06_v6(c, _registre(tmp_path))
    c["plafond_usd"] = 150
    with pytest.raises(GardeArret):
        cf6.exiger_config_t06_v6(c, _registre(tmp_path))


def test_artefact_la_v5_lit_la_ligne_neuve_comme_une_course_et_la_refuse(tmp_path):
    with pytest.raises(GardeArret, match=f"seul {COURSE} est accepté"):
        cf5.exiger_config_t06_v5(_epreuve(4.3))
    assert not cf5.est_epreuve(_epreuve(4.3))
    cf6.exiger_config_t06_v6(_epreuve(4.3), _registre(tmp_path))


def test_le_lanceur_v6_ne_differe_du_v5_que_par_l_import_la_validation_la_commande_et_deux_messages():
    a = (RACINE / "src" / "controle_ia" / "t06" / "lanceur_v5.py").read_text(encoding="utf-8").splitlines()
    b = (RACINE / "src" / "controle_ia" / "t06" / "lanceur_v6.py").read_text(encoding="utf-8").splitlines()
    diff = [(x, y) for x, y in zip(a, b[1:]) if x != y]
    assert len(b) == len(a) + 1 and b[0].startswith("# [v6") and len(diff) == 5, diff
    assert "configuration_v6" in diff[0][1] and "lanceur_v6" in diff[1][1] and 'exiger_config_t06_v6(config, racine / "registres" / "go.md")' in diff[2][1]
    assert all("GO-2026-11-06-01" in x and "GO-2026-11-06-01" not in y for x, y in diff[3:])
    assert la6.exiger_config_t06_v6 is cf6.exiger_config_t06_v6 and la6.est_epreuve is cf6.est_epreuve and la6.COMMANDE.endswith("lanceur_v6")


class _ApresValidation(Exception):
    pass


def _racine_avec_registre(tmp_path, lignes=None) -> Path:
    """Racine factice : liens vers l'arbre du dépôt, sauf `registres/` qui porte le faux registre (le lanceur v6 lit `racine/registres/go.md`)."""
    r = tmp_path / "racine"
    r.mkdir()
    for p in RACINE.iterdir():
        if p.name not in ("registres", ".git"):
            (r / p.name).symlink_to(p)
    (r / "registres").mkdir()
    _registre(r / "registres", lignes=lignes)
    return r


def _jusqu_au_manifeste(config, racine, monkeypatch):
    monkeypatch.setattr(la6, "creer_manifeste", lambda *a, **k: (_ for _ in ()).throw(_ApresValidation()))
    la6.executer(config, racine, "20261108-000000-t06-reel", None)


def test_lanceur_v6_cas_sain_la_configuration_d_e3_ter_passe_jusqu_au_manifeste_avec_la_ligne_au_registre(tmp_path, monkeypatch):
    with pytest.raises(_ApresValidation):
        _jusqu_au_manifeste(_epreuve(15), _racine_avec_registre(tmp_path), monkeypatch)


@pytest.mark.parametrize("plafond, go, motif", [(15, ABSENT, "absent du registre"), (15, DECISION, "type 'décision'"), (15, ECHU, "validité"), (16.5, NEUF, "> plafond 16 USD")])
def test_lanceur_v6_artefacts_arret_a_la_validation_avant_tout_manifeste(tmp_path, monkeypatch, plafond, go, motif):
    with pytest.raises(GardeArret, match=re.escape(motif)):
        _jusqu_au_manifeste(_epreuve(plafond, go), _racine_avec_registre(tmp_path), monkeypatch)
    assert not list((tmp_path / "racine" / "registres").glob("*.json"))


def test_lanceur_v6_lit_le_registre_du_commit_a_la_racine_pas_un_autre(monkeypatch):
    """Sur l'arbre réel du dépôt (dont le registre ne porte pas la ligne neuve), la même configuration est arrêtée : le registre lu est bien `racine/registres/go.md`."""
    with pytest.raises(GardeArret, match=f"{NEUF} absent du registre"):
        _jusqu_au_manifeste(_epreuve(15), RACINE, monkeypatch)


def test_lanceur_v6_la_course_attend_son_preenregistrement_comme_en_v5(tmp_path, monkeypatch):
    c = json.loads((D / "config-t06-reel-v1-brouillon5.json").read_text(encoding="utf-8"))
    with pytest.raises(GardeArret, match="sans préenregistrement"):
        _jusqu_au_manifeste(c, _racine_avec_registre(tmp_path), monkeypatch)


# =========================================================================================================================================================
# 3. Lanceur `scripts/lancer_t06_v13.sh` : `--verifier-go-seulement`, `controles-epreuve`, `creation`
# =========================================================================================================================================================
PYTHON_FACTICE_V13 = t.PYTHON_FACTICE.replace('[ "$2" = "controle_ia.t06.lanceur_v5" ]', '[ "$2" = "controle_ia.t06.lanceur_v6" ]')
assert PYTHON_FACTICE_V13 != t.PYTHON_FACTICE


def _prereg_v11(sha: str) -> str:
    return t._prereg(sha).replace("scripts/amorce_instance_t06_v10.sh", "scripts/amorce_instance_t06_v11.sh")


@pytest.fixture
def bac13(tmp_path):
    """Le bac des essais v12, avec l'amorce v11, le faux `python` qui connaît `lanceur_v6` et un préenregistrement qui cite l'amorce v11."""
    b = fabriquer_bac(tmp_path)
    src = b["source"]
    shutil.copy(AMORCE11, src / "scripts" / AMORCE11.name)
    liste3 = RACINE / "scripts" / "tests-cibles-t06-v3.txt"                        # l'amorce v11 joue la liste figée v3 (empreinte en dur) : liste réelle et fichiers d'essais vides
    shutil.copy(liste3, src / "scripts" / liste3.name)
    for x in liste3.read_text(encoding="utf-8").split():
        (src / x).parent.mkdir(parents=True, exist_ok=True)
        if not (src / x).exists():
            (src / x).write_text("", encoding="utf-8")
    (b["venv"] / "bin" / "python").write_text(PYTHON_FACTICE_V13, encoding="utf-8")
    sha = subprocess.run(["sha256sum", str(AMORCE11)], capture_output=True, text=True, check=True).stdout.split()[0]
    (src / (t.PREREG + ".sha256")).unlink()                                       # R12 : le sceau de la v10 est retiré avant de sceller le texte neuf (on n'écrase jamais une empreinte)
    (src / t.PREREG).write_text(_prereg_v11(sha), encoding="utf-8")
    sceller(src / t.PREREG)
    _commit_source(b, "amorce v11")
    b["amorce_sha"] = sha
    return b


def _config_e3ter(plafond=15, go=NEUF, mode="reel") -> dict:
    return _config_epreuve(CONFIG_E2, go_id=go, plafond_usd=plafond, mode=mode)        # carte modeste des offres factices ; mode réel : HF_TOKEN exigé, T06_TESTS_ARGS refusé


@pytest.fixture
def src13(bac13, tmp_path):
    """Dépôt de session : origine locale, garde de calcul, lanceur v13, registre avec la ligne neuve (et les lignes artefacts), configuration d'E3 ter, branche `prep/essai-t06`."""
    src = bac13["source"]
    origin = _distant(bac13)
    _git(src, "remote", "add", "origin", str(origin))
    (src / ".claude" / "hooks").mkdir(parents=True)
    shutil.copy(RACINE / ".claude" / "hooks" / "garde_calcul.py", src / ".claude" / "hooks" / "garde_calcul.py")
    shutil.copy(LANCEUR13, src / "scripts" / LANCEUR13.name)
    (src / "registres" / "go.md").write_text(GO + _lignes_go(), encoding="utf-8")
    (src / "prereg" / "config-epreuve-e3ter.json").write_text(json.dumps(_config_e3ter(), ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    _commit_source(bac13, "E3 ter : registre et configuration")
    _git(src, "push", "-q", "origin", "HEAD:refs/heads/prep/essai-t06")
    _git(src, "fetch", "-q", "origin", "refs/heads/prep/essai-t06:refs/remotes/origin/prep/essai-t06")
    return src


def _env13(src, tmp_path, **sup):
    b = _outils(tmp_path)
    env = {k: os.environ[k] for k in t.ENV_DE_BASE if k in os.environ}
    env.update(PATH=f"{b}:{env.get('PATH', '')}", T06_DEPOT=str(src), HF_TOKEN="jeton-hf-factice", CONTROLE_IA_GITHUB_TOKEN="jeton-gh-factice", HOME=str(src.parent),
               T06_REGISTRE_GO=str(src / "registres" / "go.md"), T06_BRANCHE_CODE="prep/essai-t06", T06_BRANCHE="essai/t06-e3ter-test",
               T06_DEPENSE_EPREUVES_ANTERIEURES_USD="0", GO_ID=NEUF)
    env.update(sup)
    return {k: v for k, v in env.items() if v is not None}


def _v13(src, tmp_path, *args, **sup):
    return subprocess.run(["bash", str(LANCEUR13), *map(str, args)], env=_env13(src, tmp_path, **sup), capture_output=True, text=True, timeout=180)


def _arbre(d: Path) -> set:
    return {str(p.relative_to(d)) for p in d.rglob("*")}


def test_verifier_go_seulement_cas_sain_ne_cree_rien(src13, tmp_path):
    _outils(tmp_path)                                                                                        # les faux outils sont posés avant la photographie de l'arbre
    avant = _arbre(tmp_path)
    r = _v13(src13, tmp_path, "--verifier-go-seulement", "15")
    assert r.returncode == 0, r.stdout + r.stderr
    assert r.stdout.strip().startswith("GO VÉRIFIÉ, RIEN CRÉÉ : ") and f"{NEUF} conforme (plafond 16 USD" in r.stdout and "≤ 16.0" in r.stdout
    assert _arbre(tmp_path) == avant                                                                        # rien créé
    r = _v13(src13, tmp_path, "--verifier-go-seulement", "10.3", "5.7", str(_dates_epreuve()[0]))
    assert r.returncode == 0 and "= 16.0 ≤ 16.0" in r.stdout, r.stdout
    assert _arbre(tmp_path) == avant


@pytest.mark.parametrize("cas, args, sup, motif", [
    ("go_id_vide", ("15",), {"GO_ID": ""}, "GO_ID absent ou illisible"),
    ("go_id_absent_de_l_environnement", ("15",), {"GO_ID": None}, "GO_ID absent ou illisible"),
    ("go_id_illisible", ("15",), {"GO_ID": "GO-X"}, "GO_ID absent ou illisible"),
    ("identifiant_absent_du_registre", ("15",), {"GO_ID": ABSENT}, "absent du registre"),
    ("ligne_decision", ("15",), {"GO_ID": DECISION}, "type 'décision'"),
    ("ligne_echue", ("15",), {"GO_ID": ECHU}, "hors de sa période de validité"),
    ("plafond_insuffisant", ("16.5",), {}, "> 16.0"),
    ("plafond_insuffisant_avec_anterieure", ("15", "1.5"), {}, "> 16.0"),
    ("ligne_trop_petite", ("5.7",), {"GO_ID": PETIT}, "> 3.0"),
    ("go_de_la_course", ("15",), {"GO_ID": COURSE}, "GO de la course"),
    ("registre_absent", ("15",), {"T06_REGISTRE_GO": None}, "T06_REGISTRE_GO"),
    ("plafond_illisible", ("abc",), {}, "nombre positif en USD"),
])
def test_verifier_go_seulement_artefacts_code_2_et_rien_cree(src13, tmp_path, cas, args, sup, motif):
    _outils(tmp_path)
    avant = _arbre(tmp_path)
    r = _v13(src13, tmp_path, "--verifier-go-seulement", *args, **sup)
    assert r.returncode == 2 and motif in r.stdout and "GO VÉRIFIÉ" not in r.stdout, (cas, r.stdout + r.stderr)
    assert _arbre(tmp_path) == avant


def _controles13(src, tmp_path, nom, config="prereg/config-epreuve-e3ter.json", commit=None, **sup):
    d = tmp_path / nom
    return d, _v13(src, tmp_path, "controles-epreuve", d, commit or _git(src, "rev-parse", "HEAD"), config, **sup)


def test_controles_epreuve_cas_sain_ligne_neuve_lue_au_registre_de_main_et_dans_le_commit(src13, tmp_path):
    d, r = _controles13(src13, tmp_path, "ok")
    assert r.returncode == 0, r.stdout + r.stderr
    assert "CONTRÔLES D'ÉPREUVE CONFORMES" in r.stdout and f"GO {NEUF} (plafond de l'épreuve 15 USD sur 16, plafond de la ligne du registre ; " in r.stdout and "≤ 16.0" in r.stdout
    lanc = (d / "lancement.txt").read_text(encoding="utf-8")
    assert "epreuve oui" in lanc and f"go {NEUF}" in lanc and "plafond 15" in lanc and f"{NEUF} conforme (plafond 16 USD" in lanc and "amorce " + subprocess.run(["sha256sum", str(AMORCE11)], capture_output=True, text=True).stdout.split()[0] in lanc
    for ancien in ANCIENS:
        assert ancien not in lanc and ancien not in r.stdout


def _config_dans_le_commit(src, nom, config):
    f = src / "prereg" / nom
    f.write_text(json.dumps(config, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    _commit_source({"source": src}, nom)
    _git(src, "push", "-q", "origin", "HEAD:refs/heads/prep/essai-t06")
    _git(src, "fetch", "-q", "origin", "refs/heads/prep/essai-t06:refs/remotes/origin/prep/essai-t06")
    return f"prereg/{nom}"


@pytest.mark.parametrize("cas", ["go_id_vide", "go_id_absent_de_l_environnement", "go_id_different_de_la_configuration", "identifiant_absent_du_registre", "ligne_decision",
                                 "ligne_echue", "plafond_insuffisant", "plafond_insuffisant_avec_anterieure", "ligne_trop_petite", "go_de_la_course", "ligne_absente_du_commit"])
def test_controles_epreuve_artefacts_code_2_aucun_controle_conforme(src13, tmp_path, cas):
    src = src13
    sup, config = {}, "prereg/config-epreuve-e3ter.json"
    motif = {"go_id_vide": "GO_ID absent ou illisible", "go_id_absent_de_l_environnement": "GO_ID absent ou illisible", "go_id_different_de_la_configuration": "≠ GO_ID de l'environnement",
             "identifiant_absent_du_registre": "absent du registre", "ligne_decision": "type 'décision'", "ligne_echue": "hors de sa période de validité",
             "plafond_insuffisant": "> 16.0", "plafond_insuffisant_avec_anterieure": "> 16.0", "ligne_trop_petite": "> 3.0", "go_de_la_course": "GO de la course",
             "ligne_absente_du_commit": "commit postérieur au GO exigé"}[cas]
    if cas == "go_id_vide":
        sup["GO_ID"] = ""
    elif cas == "go_id_absent_de_l_environnement":
        sup["GO_ID"] = None
    elif cas == "go_id_different_de_la_configuration":
        sup["GO_ID"] = PETIT
    elif cas in ("identifiant_absent_du_registre", "ligne_decision", "ligne_echue", "ligne_trop_petite", "go_de_la_course"):
        go = {"identifiant_absent_du_registre": ABSENT, "ligne_decision": DECISION, "ligne_echue": ECHU, "ligne_trop_petite": PETIT, "go_de_la_course": COURSE}[cas]
        config = _config_dans_le_commit(src, f"config-{cas}.json", _config_e3ter(go=go, plafond=1.5 if cas == "ligne_trop_petite" else 15))
        sup["GO_ID"] = go
        # la ligne « trop petite » n'est pas refusée par la ligne elle-même (3 USD, conforme) mais par le plafond demandé : 1,5 passe ; on demande alors 5,7
        if cas == "ligne_trop_petite":
            config = _config_dans_le_commit(src, "config-petite-5-7.json", _config_e3ter(go=PETIT, plafond=5.7))
    elif cas == "plafond_insuffisant":
        config = _config_dans_le_commit(src, "config-16-5.json", _config_e3ter(plafond=16.5))
    elif cas == "plafond_insuffisant_avec_anterieure":
        sup["T06_DEPENSE_EPREUVES_ANTERIEURES_USD"] = "1.5"
    elif cas == "ligne_absente_du_commit":
        # le registre de « main » porte la ligne, celui du commit cloné ne la porte pas : l'amorce refuserait sur l'instance, le lanceur refuse avant
        reg_main = tmp_path / "go-main.md"
        reg_main.write_text((src / "registres" / "go.md").read_text(encoding="utf-8"), encoding="utf-8")
        (src / "registres" / "go.md").write_text(GO, encoding="utf-8")
        _commit_source({"source": src}, "commit sans la ligne")
        _git(src, "push", "-q", "origin", "HEAD:refs/heads/prep/essai-t06")
        _git(src, "fetch", "-q", "origin", "refs/heads/prep/essai-t06:refs/remotes/origin/prep/essai-t06")
        sup["T06_REGISTRE_GO"] = str(reg_main)
    d, r = _controles13(src, tmp_path, "x", config=config, **sup)
    assert r.returncode == 2 and motif in r.stdout + r.stderr, (cas, r.stdout + r.stderr)
    assert "CONTRÔLES D'ÉPREUVE CONFORMES" not in r.stdout
    assert not (d / "lancement.txt").exists() or "epreuve oui" not in (d / "lancement.txt").read_text(encoding="utf-8")


@pytest.fixture
def monde13(src13, tmp_path):
    """Le monde des essais de création v12 (faux `vastai` 1.8.3, faux `df`, offres, journal) autour du dépôt v13."""
    b = tmp_path / "bin"
    b.mkdir(exist_ok=True)
    for nom, texte in (("vastai", VAST_REEL), ("df", DF_FACTICE)):
        (b / nom).write_text(texte, encoding="utf-8")
        (b / nom).chmod(0o755)
    (tmp_path / "offres.json").write_text(json.dumps(OFFRES), encoding="utf-8")
    (tmp_path / "journal.txt").write_text("AMORCE 2026-11-07T10:00:00Z : commit abc\n", encoding="utf-8")
    return {"src": src13, "tmp": tmp_path}


def _c13(m, *args, **sup):
    e = env5(m, **{"T06_BRANCHE": "essai/t06-e3ter-test", "HF_TOKEN": "jeton-hf-factice", "GO_ID": NEUF, **sup})
    return subprocess.run(["bash", str(LANCEUR13), *map(str, args)], env=e, capture_output=True, text=True, timeout=180)


def test_creation_cas_sain_commande_sous_la_ligne_neuve_garde_de_calcul_rejouee(monde13):
    m = monde13
    d = m["tmp"] / "e3ter"
    r = _c13(m, "controles-epreuve", d, _git(m["src"], "rev-parse", "HEAD"), "prereg/config-epreuve-e3ter.json")
    assert r.returncode == 0, r.stdout + r.stderr
    r = _c13(m, "creation", "auto", "course", "0", d)
    assert r.returncode == 0, r.stdout + r.stderr
    cmd = r.stdout.splitlines()[-1]
    assert cmd.startswith(f"GO_ID={NEUF} timeout -k 10 300 ") and f"-e EPREUVE_GO_ID={NEUF} " in cmd and "-e CONFIG=prereg/config-epreuve-e3ter.json" in cmd
    assert "-e PREREG_ABSENT=1" in cmd and "-e BRANCHE=essai/t06-e3ter-test" in cmd and "lancer_t06_v13.sh apres-creation" in cmd and "TESTS_ARGS" not in cmd
    lanc = (d / "lancement.txt").read_text(encoding="utf-8")
    assert "plafond_creation 15" in lanc and "creation preparee" in lanc
    for ancien in ANCIENS:
        assert ancien not in cmd and ancien not in lanc
    # artefact : une sélection d'essais reste refusée en mode réel (inchangé de la v12)
    r = _c13(m, "creation", "auto", "course", "0", d, T06_TESTS_ARGS="tests/a.py,-x")
    assert r.returncode == 2 and "T06_TESTS_ARGS refusé en mode reel" in r.stdout, r.stdout


@pytest.mark.parametrize("cas", ["go_id_vide", "go_id_absent_de_l_environnement", "go_id_autre", "ligne_retiree_du_registre_a_la_creation", "ligne_echue_au_jour_de_la_creation"])
def test_creation_artefacts_aucune_commande_de_creation(monde13, cas):
    m = monde13
    d = m["tmp"] / "e3ter"
    r = _c13(m, "controles-epreuve", d, _git(m["src"], "rev-parse", "HEAD"), "prereg/config-epreuve-e3ter.json")
    assert r.returncode == 0, r.stdout + r.stderr
    sup = {}
    if cas == "go_id_vide":
        sup["GO_ID"] = ""
    elif cas == "go_id_absent_de_l_environnement":
        sup["GO_ID"] = None
    elif cas == "go_id_autre":
        sup["GO_ID"] = PETIT
    elif cas in ("ligne_retiree_du_registre_a_la_creation", "ligne_echue_au_jour_de_la_creation"):
        reg = m["tmp"] / "go-creation.md"
        if cas == "ligne_retiree_du_registre_a_la_creation":
            reg.write_text("\n".join(l for l in (m["src"] / "registres" / "go.md").read_text(encoding="utf-8").splitlines() if not l.startswith(f"| {NEUF} ")) + "\n", encoding="utf-8")
        else:
            auj, _, _ = _dates_epreuve()
            reg.write_text(GO + _lignes_go().replace(f"| {NEUF} | {auj} | calcul | E3 ter de T0.6, galop d'essai de la garde d'équivalence | 16 USD | {_dates_epreuve()[1]} |",
                                                     f"| {NEUF} | {auj - timedelta(days=10)} | calcul | E3 ter de T0.6, galop d'essai de la garde d'équivalence | 16 USD | {auj - timedelta(days=1)} |"), encoding="utf-8")
        sup["T06_REGISTRE_GO"] = str(reg)
    r = _c13(m, "creation", "auto", "course", "0", d, **sup)
    motif = {"go_id_vide": "≠ GO_ID de l'environnement", "go_id_absent_de_l_environnement": "≠ GO_ID de l'environnement", "go_id_autre": "≠ GO_ID de l'environnement",
             "ligne_retiree_du_registre_a_la_creation": "absent du registre", "ligne_echue_au_jour_de_la_creation": "hors de sa période de validité"}[cas]
    assert r.returncode == 2 and motif in r.stdout and "create instance" not in r.stdout and "COMMANDE DE CRÉATION" not in r.stdout, (cas, r.stdout + r.stderr)
    assert not (m["tmp"] / "appels.txt").exists() or "create instance" not in (m["tmp"] / "appels.txt").read_text(encoding="utf-8")


# =========================================================================================================================================================
# 4. Amorce `scripts/amorce_instance_t06_v11.sh` (essai local, aucun appel à Vast) : la ligne est lue dans registres/go.md du commit cloné
# =========================================================================================================================================================
def _epreuve_amorce13(bac13, nom, go=NEUF, branche="essai/t06-e3ter-test", mode="jouet", lignes=None, **sup):
    src = bac13["source"]
    (src / "registres" / "go.md").write_text(GO + (_lignes_go() if lignes is None else lignes), encoding="utf-8")
    c = _config_epreuve(CONFIG_E2, go_id=NEUF, plafond_usd=15, mode=json.loads(CONFIG_E2.read_text(encoding="utf-8"))["mode"])
    f = src / "prereg" / "config-epreuve.json"
    f.write_text(json.dumps(c, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    sceller(f)
    _commit_source(bac13, "épreuve E3 ter")
    _, _, fin = _dates_epreuve()
    env = {"EPREUVE_GO_ID": go, "PREREG_ABSENT": "1", "CONFIG": "prereg/config-epreuve.json", "BRANCHE": branche, "MODE": mode, "HF_TOKEN": "jeton-hf-factice",
           "FIN_GO_UTC_S": str(int(fin.timestamp())), "ECHEANCE_UTC_S": str(int(fin.timestamp())), "TESTS_ATTENDUS": ""}
    env.update(sup)
    distant = _distant(bac13)                                                                 # cloné APRÈS le commit de l'épreuve
    return (*_lancer_amorce13(bac13, distant, nom, env), distant)


def _lancer_amorce13(bac, distant, nom, env_sup):
    racine = bac["racine"] / nom
    racine.mkdir(exist_ok=True)
    r = subprocess.run(["bash", str(AMORCE11)], env=t._env(bac, distant, racine, env_sup), capture_output=True, text=True, timeout=300)
    j = racine / "t06" / "journal.txt"
    return r.returncode, (j.read_text(encoding="utf-8") if j.exists() else ""), r.stdout + r.stderr, racine


@pytest.mark.parametrize("mode", ["jouet", "reel"])
def test_amorce_v11_cas_sain_ligne_neuve_lue_dans_le_registre_du_commit(bac13, mode):
    code, journal, sortie, racine, distant = _epreuve_amorce13(bac13, "ep", mode=mode)
    assert code == 0, sortie[-2500:]
    assert f"GO : {NEUF} conforme (plafond 16 USD" in journal and f"GO={NEUF}" in journal and "répétition sans préenregistrement" in journal and "lanceur v6" in journal
    assert "AMORCE T06 v11 DEMARRAGE" in sortie and (racine / "t06-fin-normale").exists() and "essai/t06-e3ter-test" in _git(distant, "branch", "--list", "essai/*")
    assert (racine / "pytest-args.txt").exists()                                            # la suite ciblée figée (liste v2) est jouée, inchangée


@pytest.mark.parametrize("cas, go, lignes_cle, motif", [
    ("identifiant_absent_du_registre", ABSENT, None, f"{ABSENT} non conforme dans registres/go.md du commit ({ABSENT} absent du registre)"),
    ("ligne_decision", DECISION, None, "type 'décision'"),
    ("ligne_echue", ECHU, None, "hors de sa période de validité"),
    ("go_de_la_course", COURSE, None, "GO de la course"),
    ("identifiant_illisible", "GO-X", None, "identifiant de ligne de GO illisible"),
    ("ligne_retiree_du_commit", NEUF, "sans", f"{NEUF} absent du registre"),
])
def test_amorce_v11_artefacts_refus_et_destruction_demandee_avant_tout_run(bac13, cas, go, lignes_cle, motif):
    lignes = "" if lignes_cle == "sans" else None
    code, journal, sortie, racine, _ = _epreuve_amorce13(bac13, "ea", go=go, lignes=lignes)
    assert code == 2 and (racine / "t06-detruire").exists(), (cas, sortie[-2000:])
    assert motif in sortie, (cas, sortie[-1500:])
    assert "run :" not in journal and not (racine / "pytest-args.txt").exists()


def test_amorce_v11_plafond_de_la_ligne_transmis_au_calendrier(bac13):
    """Le plafond lu sur la ligne (16) sert à la vérification v3 du GO et au calendrier ; une ligne à un autre plafond passe aussi (rien n'est écrit en dur)."""
    auj, ech, _ = _dates_epreuve()
    lignes = f"| {NEUF} | {auj} | calcul | E3 ter, autre plafond | 23 USD | {ech} | Lazar | mot |\n"
    code, journal, sortie, racine, _ = _epreuve_amorce13(bac13, "ep23", lignes=lignes)
    assert code == 0, sortie[-2500:]
    assert f"GO : {NEUF} conforme (plafond 23 USD" in journal and "calendrier : fin_go_utc_s=" in journal


# =========================================================================================================================================================
# 5. Diff v12 → v13 : seules les lignes de la ligne de GO et du plafond changent, plus les renvois de noms de fichiers ; aucun identifiant en dur
# =========================================================================================================================================================
MARQUEURS_LANCEUR = ("GO_ID_ENV", "GO_EPREUVE", "go_epreuve", "plafond_ligne_go", "MOTIF_GO", "session_v1", "amorce_instance_t06_v1", "lancer_t06_v1", "v12", "v13",
                     "SESSION7", "verifier-go-seulement", "GO_ID", "PGL", "PLAF", "ligne de GO", "champ go", "ANT_EPR", "amorce v1", "CONTROLE_IA_GITHUB_TOKEN", "jeton_gh_nom", "JGHN", "GO-2026-11-06-01", "GO-2026-11-07-08", "usage :", "T06_REGISTRE_GO", "GOL=", "GO VÉRIFIÉ", "GO $GO_ID_ENV")
MARQUEURS_AMORCE = ("EPREUVE_GO", "PLAFOND_LIGNE_GO", "SESSION_V12", "lanceur_v5", "lanceur_v6", "lanceur v5", "lanceur v6", "v10", "v11", "GO-2026-11-06-01", "PREREG_ABSENT=1", "C-V4-3", "LISTE_TESTS")


def _diff(a: Path, b: Path):
    return [l for l in difflib.unified_diff(a.read_text(encoding="utf-8").splitlines(), b.read_text(encoding="utf-8").splitlines(), lineterm="", n=0)
            if (l.startswith("+") or l.startswith("-")) and not l.startswith(("+++", "---"))]


def test_diff_lanceur_v12_v13_ne_porte_que_la_ligne_de_go_le_plafond_et_les_renvois():
    d = _diff(LANCEUR12, LANCEUR13)
    assert d, "aucune différence"
    hors = [l for l in d if not any(m in l for m in MARQUEURS_LANCEUR)]
    assert not hors, hors
    assert 50 <= len(d) <= 90, len(d)                                                                      # une soixantaine de lignes touchées (ligne de GO, plafond, renvois, sous-commande de vérification), pas une réécriture
    code = "\n".join(l for l in LANCEUR13.read_text(encoding="utf-8").splitlines() if l.strip() and not l.lstrip().startswith("#"))
    assert "GO_EPREUVE" not in code and "go_epreuve" not in code and "session_v11" not in code                   # plus de constante ni de fonction en dur dans le code (les notes d'historique en commentaire restent)


def test_diff_amorce_v10_v11_ne_porte_que_la_ligne_de_go_et_le_lanceur_de_run():
    d = _diff(AMORCE10, AMORCE11)
    assert d, "aucune différence"
    hors = [l for l in d if not any(m in l for m in MARQUEURS_AMORCE)]
    assert not hors, hors
    assert 14 <= len(d) <= 26, len(d)
    a11 = AMORCE11.read_text(encoding="utf-8")
    code11 = "\n".join(l for l in a11.splitlines() if l.strip() and not l.lstrip().startswith("#"))
    assert 'LISTE_TESTS="scripts/tests-cibles-t06-v3.txt"' in code11 and "bras_b_v4}" in code11 and "tests-cibles-t06-v2" not in code11
    import hashlib
    assert re.search(r'LISTE_SHA256="([0-9a-f]{64})"', a11).group(1) == hashlib.sha256((RACINE / "scripts" / "tests-cibles-t06-v3.txt").read_bytes()).hexdigest()
    v3 = (RACINE / "scripts" / "tests-cibles-t06-v3.txt").read_text(encoding="utf-8").split()
    v2 = (RACINE / "scripts" / "tests-cibles-t06-v2.txt").read_text(encoding="utf-8").split()
    # R-1874, décision (a) de la mère : v3 = v2 + les deux essais v13 − test_t06_v12_liste.py (remplacé par test_t06_v13_liste.py, passé aux exclusions v3 avec ce motif)
    assert set(v3) == (set(v2) - {"tests/test_t06_v12_liste.py"}) | {"tests/test_t06_chaine_v13.py", "tests/test_t06_v13_liste.py"} and v3 == sorted(v3) and len(v3) == len(set(v3))
    ex2 = (RACINE / "scripts" / "tests-exclus-t06-v2.txt").read_text(encoding="utf-8").splitlines()[1:]
    ex3 = (RACINE / "scripts" / "tests-exclus-t06-v3.txt").read_text(encoding="utf-8").splitlines()[1:]
    neuves = [l for l in ex3 if l not in ex2]
    assert set(ex3) == set(ex2) | set(neuves) and len(ex3) == len(ex2) + 1 and len(neuves) == 1 and neuves[0].startswith("tests/test_t06_v12_liste.py\t") and "test_t06_v13_liste.py" in neuves[0], neuves
    entete3 = (RACINE / "scripts" / "tests-exclus-t06-v3.txt").read_text(encoding="utf-8").splitlines()[0]
    assert entete3.startswith("#") and "test_t06_v13_liste.py" in entete3 and "aucune exclusion ajoutée" not in entete3            # l'en-tête dit ce que la v3 ajoute


def test_aucun_identifiant_d_epreuve_en_dur_dans_le_code_de_la_chaine_v13():
    """Les identifiants des deux anciennes lignes ne figurent dans aucune ligne de CODE des cinq fichiers v13 (seules les notes d'historique en commentaire les citent encore)."""
    for f in (LANCEUR13, AMORCE11):
        code = [l for l in f.read_text(encoding="utf-8").splitlines() if l.strip() and not l.lstrip().startswith("#")]
        for ancien in ANCIENS:
            assert not [l for l in code if ancien in l], (f.name, ancien)
    for f in ("session_v12.py", "configuration_v6.py", "lanceur_v6.py"):
        texte = (RACINE / "src" / "controle_ia" / "t06" / f).read_text(encoding="utf-8")
        for ancien in ANCIENS:
            assert ancien not in texte, (f, ancien)
    v12 = LANCEUR12.read_text(encoding="utf-8")
    assert "GO_EPREUVE=GO-2026-11-06-01" in v12 and "GO_EPREUVE_BIS=GO-2026-11-07-08" in v12                       # la v12 est intacte (R12)
    assert "GO-2026-11-06-01) PLAFOND_LIGNE_GO=5" in AMORCE10.read_text(encoding="utf-8")


# =========================================================================================================================================================
# 6. Jeton GitHub sous l'un ou l'autre nom (CONTROLE_IA_GITHUB_TOKEN ou CONTROLE_IA_GITHUB_TOKEN_2), par présence du nom seulement, valeur jamais affichée
# =========================================================================================================================================================
VALEUR_2 = "jeton-gh-factice-deux-valeur"


def _sans_valeur(*textes):
    for x in textes:
        assert VALEUR_2 not in x and "jeton-gh-factice" not in x, "une valeur de jeton apparaît"


def test_jeton_github_nom_2_seul_cas_sain_controles_et_creation(monde13):
    m = monde13
    d = m["tmp"] / "e3ter"
    sup = {"CONTROLE_IA_GITHUB_TOKEN": None, "CONTROLE_IA_GITHUB_TOKEN_2": VALEUR_2}
    r = _c13(m, "controles-epreuve", d, _git(m["src"], "rev-parse", "HEAD"), "prereg/config-epreuve-e3ter.json", **sup)
    assert r.returncode == 0, r.stdout + r.stderr
    r = _c13(m, "creation", "auto", "course", "0", d, **sup)
    assert r.returncode == 0, r.stdout + r.stderr
    cmd = r.stdout.splitlines()[-1]
    assert "-e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN_2 " in cmd and "GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN " not in cmd            # relayé par son NOM, le shell de l'exécutante l'expansera
    _sans_valeur(r.stdout, r.stderr, (d / "lancement.txt").read_text(encoding="utf-8"))


def test_jeton_github_les_deux_noms_presents_le_premier_l_emporte(monde13):
    m = monde13
    d = m["tmp"] / "e3ter"
    sup = {"CONTROLE_IA_GITHUB_TOKEN_2": VALEUR_2}                                      # env5 pose déjà CONTROLE_IA_GITHUB_TOKEN
    r = _c13(m, "controles-epreuve", d, _git(m["src"], "rev-parse", "HEAD"), "prereg/config-epreuve-e3ter.json", **sup)
    assert r.returncode == 0, r.stdout + r.stderr
    r = _c13(m, "creation", "auto", "course", "0", d, **sup)
    assert r.returncode == 0 and "-e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN " in r.stdout.splitlines()[-1], r.stdout
    _sans_valeur(r.stdout, r.stderr)


@pytest.mark.parametrize("quoi", ["controles-epreuve", "creation"])
def test_jeton_github_artefact_aucun_des_deux_noms_arret_explicite(monde13, quoi):
    m = monde13
    d = m["tmp"] / "e3ter"
    if quoi == "creation":
        r = _c13(m, "controles-epreuve", d, _git(m["src"], "rev-parse", "HEAD"), "prereg/config-epreuve-e3ter.json")
        assert r.returncode == 0, r.stdout + r.stderr
        r = _c13(m, "creation", "auto", "course", "0", d, CONTROLE_IA_GITHUB_TOKEN=None, CONTROLE_IA_GITHUB_TOKEN_2=None)
        assert "create instance" not in r.stdout
    else:
        r = _c13(m, "controles-epreuve", d, _git(m["src"], "rev-parse", "HEAD"), "prereg/config-epreuve-e3ter.json", CONTROLE_IA_GITHUB_TOKEN=None, CONTROLE_IA_GITHUB_TOKEN_2=None)
        assert "CONTRÔLES D'ÉPREUVE CONFORMES" not in r.stdout
    assert r.returncode == 2 and "jeton absent (ni CONTROLE_IA_GITHUB_TOKEN ni CONTROLE_IA_GITHUB_TOKEN_2" in r.stdout, (quoi, r.stdout + r.stderr)


def test_jeton_github_artefact_nom_2_vide_vaut_absent(monde13):
    m = monde13
    d = m["tmp"] / "e3ter"
    r = _c13(m, "controles-epreuve", d, _git(m["src"], "rev-parse", "HEAD"), "prereg/config-epreuve-e3ter.json", CONTROLE_IA_GITHUB_TOKEN=None, CONTROLE_IA_GITHUB_TOKEN_2="")
    assert r.returncode == 2 and "jeton absent" in r.stdout, r.stdout


def _surveiller13(tmp_path, env_sup, duree=6):
    d = tmp_path / "s"
    t._lancement(d, int(__import__("time").time()) - 600)
    env = t._env_surveillance(tmp_path, t.JOURNAL_BON + f"AMORCE 2026-11-07T10:00:09Z : CONTROLE_IA_GITHUB_TOKEN_2={VALEUR_2}\n")
    env.update(env_sup)
    env = {k: v for k, v in env.items() if v is not None}
    try:
        r = subprocess.run(["bash", str(LANCEUR13), "surveillance", "123456", str(d)], env=env, capture_output=True, text=True, timeout=duree)
        return r.returncode, r.stdout + r.stderr, d
    except subprocess.TimeoutExpired as e:
        return None, (e.stdout.decode() if isinstance(e.stdout, bytes) else (e.stdout or "")), d


def test_surveillance_nom_2_seul_accepte_et_masque_aucun_des_deux_refuse(tmp_path):
    code, sortie, d = _surveiller13(tmp_path / "a", {"CONTROLE_IA_GITHUB_TOKEN": None, "CONTROLE_IA_GITHUB_TOKEN_2": VALEUR_2})
    (tmp_path / "a").mkdir(exist_ok=True)
    assert code is None or code == 0, sortie[-800:]                                       # la surveillance tourne (interrompue par le délai de l'essai), pas de refus
    assert "jeton GitHub absent" not in sortie
    texte = "\n".join(f.read_text(encoding="utf-8", errors="replace") for f in d.rglob("*") if f.is_file())
    assert VALEUR_2 not in texte and VALEUR_2 not in sortie and (d / "journal-dernier.txt").read_text(encoding="utf-8").count("***") >= 1   # masqué par un tube
    code, sortie, d = _surveiller13(tmp_path / "b", {"CONTROLE_IA_GITHUB_TOKEN": None, "CONTROLE_IA_GITHUB_TOKEN_2": None}, duree=30)
    assert code == 2 and "jeton GitHub absent ou trop court" in sortie, sortie[-800:]
    code, sortie, d = _surveiller13(tmp_path / "c", {"CONTROLE_IA_GITHUB_TOKEN": None, "CONTROLE_IA_GITHUB_TOKEN_2": "abc1234"}, duree=30)
    assert code == 2 and ("trop court" in sortie), sortie[-800:]
