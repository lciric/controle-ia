"""Essais R5 de la ligne `CODE-T07` (DS-3 bis accordée, option (a), R-2104 ; `src/controle_ia/t07/code_t07_v1.py` et garde d'ouverture
de `lecture_v2`) : avec `code_t07_exige` vrai, refus sans la ligne ; refus si le commit cité ou les empreintes diffèrent de l'arbre
exécuté ; refus si la ligne est postérieure à l'ouverture, ou à la première ouverture de l'étape A (relance) ; chaque cas avec son
cas sain. Le dépôt du code est un dépôt jetable (module factice) substitué au module importé par `dossier_du_module`."""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.scellement import sceller
from controle_ia.t07 import code_t07_v1 as ct
from controle_ia.t07 import lecture_v1 as lv1
from controle_ia.t07 import lecture_v2 as lv
from controle_ia.t07 import registre_v1 as rg
from test_t07_lecture_v1 import AVANT, INSTANT, RUN_T06
from test_t07_sondes_neuves_v1 import ExtracteurFactice, construire_complet

RACINE_DEPOT = Path(__file__).resolve().parents[1]
CONFIG_V4 = RACINE_DEPOT / "brouillons" / "T0.7-sondes-v0-v1-brouillon19-pieces" / "configuration-t07-v4.json"


def _git(d: Path, *args) -> str:
    return subprocess.run(["git", "-C", str(d), *args], capture_output=True, text=True, check=True).stdout.strip()


def depot_code(tmp: Path) -> tuple[Path, str, str]:
    """Dépôt jetable : `src/controle_ia/t07/a.py`, `b.py` ; commit du code C7, puis commit de scellement S7 qui n'y touche pas."""
    d = tmp / "code"
    m = d / "src" / "controle_ia" / "t07"
    m.mkdir(parents=True)
    _git(d, "init", "-q", "-b", "main")
    _git(d, "config", "user.email", "essai@example.invalid")
    _git(d, "config", "user.name", "essai")
    (m / "a.py").write_text("A = 1\n")
    (m / "b.py").write_text("B = 2\n")
    _git(d, "add", "-A")
    _git(d, "commit", "-q", "-m", "code")
    c7 = _git(d, "rev-parse", "HEAD")
    (d / "prereg.md").write_text("texte scellé\n")
    _git(d, "add", "-A")
    _git(d, "commit", "-q", "-m", "scellement")
    return d, c7, _git(d, "rev-parse", "HEAD")


def poser_code(j, depot: Path, commit: str, date: str = AVANT, retoucher=None) -> None:
    f = ct.ecrire_fichier_code(depot, commit, j.racine / "registres" / "code-t07" / "CODE-T07-v1.json")
    if retoucher:
        d = json.loads(f.read_text(encoding="utf-8"))
        retoucher(d)
        f.write_text(json.dumps(d), encoding="utf-8")
    sha = sceller(f)
    with open(j.registre, "a", encoding="utf-8") as r:
        r.write(rg.ecrire_ligne(rg.CODE_T07, date, "registres/code-t07/CODE-T07-v1.json", sha) + "\n")


@pytest.fixture
def jc(depot, tmp_path_factory, monkeypatch):
    j = construire_complet(depot)
    j.config["code_t07_exige"] = True
    d, c7, s7 = depot_code(tmp_path_factory.mktemp("code"))
    monkeypatch.setattr(ct, "dossier_du_module", lambda: d / "src" / "controle_ia" / "t07")
    j.pieces.update(code=d, c7=c7, s7=s7)
    return j


def _a(j, **kw):
    kw.setdefault("instant", INSTANT)
    kw.setdefault("extracteur", ExtracteurFactice())
    return lv.etape_a(j.racine, j.registre, j.config, RUN_T06, **kw)


def test_code_t07_cas_sain_commit_du_code_ancetre_de_la_tete(jc):
    """Cas sain : ligne présente, antérieure, commit du code (ancêtre de la tête S7), fichiers égaux : l'étape A part ; le
    contrôle est écrit dans `ouverture-t07.json`."""
    poser_code(jc, jc.pieces["code"], jc.pieces["c7"])
    ra = _a(jc)
    doc = json.loads((jc.racine / "diag" / ra["run_t07"] / "ouverture-t07.json").read_text(encoding="utf-8"))["resultat"]
    assert doc["code_t07"]["commit"] == jc.pieces["c7"] and doc["code_t07"]["fichiers"] == 2


def test_code_t07_absente_refus(jc):
    """Artefact : `code_t07_exige` vrai, aucune ligne `CODE-T07` → refus de la garde (code 2), rien d'écrit ; cas sain : faux,
    sans ligne → l'étape part (essais de bout en bout)."""
    with pytest.raises(rg.RefusRegistre, match="CODE-T07"):
        _a(jc)
    assert not (jc.racine / "runs").exists() or not any("t07" in p.name for p in (jc.racine / "runs").iterdir())


@pytest.mark.parametrize("cas", ["commit-inconnu", "commit-hors-lignee", "empreinte", "fichier-en-moins", "arbre-retouche",
                                 "fichier-en-plus"])
def test_code_t07_artefacts_commit_ou_empreintes(jc, cas):
    """Artefacts : commit cité absent ; commit hors de la lignée de la tête ; empreinte écrite fausse ; un fichier du module absent
    de la liste ; fichier de l'arbre exécuté retouché après le commit ; fichier en plus dans l'arbre exécuté → refus."""
    d, c7 = jc.pieces["code"], jc.pieces["c7"]
    m = d / "src" / "controle_ia" / "t07"
    if cas == "commit-inconnu":
        poser_code(jc, d, c7, retoucher=lambda x: x.update(commit="0" * 40))
    elif cas == "commit-hors-lignee":
        _git(d, "checkout", "-q", "-b", "autre", c7)
        (m / "a.py").write_text("A = 3\n")
        _git(d, "commit", "-q", "-am", "autre")
        autre = _git(d, "rev-parse", "HEAD")
        _git(d, "checkout", "-q", "main")
        poser_code(jc, d, autre)
    elif cas == "empreinte":
        poser_code(jc, d, c7, retoucher=lambda x: x["fichiers"].update({ct.PREFIXE + "a.py": "1" * 64}))
    elif cas == "fichier-en-moins":
        poser_code(jc, d, c7, retoucher=lambda x: x["fichiers"].pop(ct.PREFIXE + "b.py"))
    elif cas == "arbre-retouche":
        poser_code(jc, d, c7)
        (m / "a.py").write_text("A = 99\n")
    else:
        poser_code(jc, d, c7)
        (m / "c.py").write_text("C = 0\n")
    with pytest.raises(rg.RefusRegistre, match="CODE-T07"):
        _a(jc)


def test_code_t07_posterieure_a_l_ouverture_ou_a_la_premiere(jc):
    """Artefacts : ligne datée à l'instant de l'ouverture (pas strictement antérieure) → refus ; ligne antérieure à cette
    ouverture-ci mais postérieure à une première ouverture de l'étape A de ce run (relance) → refus ; cas sain : même ligne,
    aucune ouverture antérieure → l'étape part."""
    poser_code(jc, jc.pieces["code"], jc.pieces["c7"], date=rg.date_utc(INSTANT))
    with pytest.raises(rg.RefusRegistre, match="pas strictement antérieure"):
        _a(jc)


def test_code_t07_ligne_apres_la_premiere_ouverture(jc):
    poser_code(jc, jc.pieces["code"], jc.pieces["c7"], date=rg.date_utc(INSTANT - 100))
    rg.journaliser_ouverture(jc.registre, INSTANT - 500, f"etape-A/{RUN_T06}", "0" * 64)
    with pytest.raises(rg.RefusRegistre, match="première ouverture"):
        _a(jc)


def test_code_t07_forme_du_fichier(tmp_path):
    """Forme du fichier cité : cas sain (commit et liste) ; artefacts : clé en plus, commit court, chemin hors du module."""
    f = tmp_path / "c.json"
    f.write_text(json.dumps({"commit": "a" * 40, "fichiers": {ct.PREFIXE + "x.py": "b" * 64}}))
    assert ct.lire_fichier_code(f)["commit"] == "a" * 40
    for faux in ({"commit": "a" * 40, "fichiers": {ct.PREFIXE + "x.py": "b" * 64}, "autre": 1},
                 {"commit": "a" * 12, "fichiers": {ct.PREFIXE + "x.py": "b" * 64}},
                 {"commit": "a" * 40, "fichiers": {"src/controle_ia/t06/x.py": "b" * 64}},
                 {"commit": "a" * 40, "fichiers": {}}):
        f.write_text(json.dumps(faux))
        with pytest.raises(rg.RefusRegistre):
            ct.lire_fichier_code(f)


def test_configuration_v4_code_t07_exige(tmp_path):
    """La configuration brouillon v4 (v3 plus `code_t07_exige` vrai, R-2104) passe les contrôles du module, entropie mise à part."""
    if not CONFIG_V4.is_file():
        pytest.skip("configuration v4 absente")
    c = json.loads(CONFIG_V4.read_text(encoding="utf-8"))
    v3 = json.loads((CONFIG_V4.parent / "configuration-t07-v3.json").read_text(encoding="utf-8"))
    assert c["code_t07_exige"] is True and {k: x for k, x in c.items() if k != "code_t07_exige"} == {k: x for k, x in v3.items() if k != "code_t07_exige"}
    with pytest.raises(GardeArret, match="entropie = None"):
        lv.exiger_configuration(c)
    lv.exiger_configuration({**c, "entropie": 1})
    assert c["enonces_reserve"]["sha256"].startswith("8d20a698")
    assert lv1.CLES_CONFIG and "code_t07_exige" in lv1.CLES_CONFIG


def test_code_t07_commande_verifier(jc, capsys):
    """`code_t07_v1 verifier RACINE REGISTRE` (pas 1 de l'ordre d'exécution, avant la passe à blanc) : sans ligne → code 2 ;
    ligne conforme → code 0 ; arbre retouché → code 2. Rien n'est écrit au journal des ouvertures."""
    assert ct.main(["verifier", str(jc.racine), str(jc.registre)]) == 2
    poser_code(jc, jc.pieces["code"], jc.pieces["c7"])
    assert ct.main(["verifier", str(jc.racine), str(jc.registre)]) == 0 and "CODE-T07 conforme" in capsys.readouterr().out
    (jc.pieces["code"] / "src" / "controle_ia" / "t07" / "b.py").write_text("B = 3\n")
    assert ct.main(["verifier", str(jc.racine), str(jc.registre)]) == 2
    assert not jc.journal.exists()


# ------------------------------------------------------------------------------------- DF-02 (contre-lecture différentielle)
def test_DF02_paquets_importes_et_arbre_de_travail(jc):
    """DF-02 : tout `src/controle_ia/` de l'arbre exécuté égal au commit cité. Cas sain : arbre propre (essai du cas sain plus
    haut). Artefacts : un paquet importé hors de `t07/` changé dans un commit postérieur au commit cité → refus ; un fichier non
    suivi sous `src/controle_ia/` → refus (arbre de travail modifié)."""
    d, c7 = jc.pieces["code"], jc.pieces["c7"]
    poser_code(jc, d, c7)
    autre = d / "src" / "controle_ia" / "autre"
    autre.mkdir(parents=True)
    (autre / "y.py").write_text("Y = 1\n")
    with pytest.raises(rg.RefusRegistre, match="arbre de travail modifié"):
        _a(jc)
    _git(d, "add", "-A")
    _git(d, "commit", "-q", "-m", "paquet importé changé après C7")
    with pytest.raises(rg.RefusRegistre, match="paquets importés compris"):
        _a(jc, instant=INSTANT + 1)


def test_DF02_code_t07_exigee_et_controlee_a_l_etape_B(jc):
    """DF-02 : avec `code_t07_exige` vrai, l'étape B exige et contrôle `CODE-T07`. Cas sain : étape B lue ; artefact : module retouché
    entre les deux étapes → l'étape B refuse (code 2), rien d'écrit."""
    from test_t07_lecture_v1 import APRES_A, INSTANT_B
    from test_t07_lecture_v2 import lignes_audit, lignes_p3bis
    poser_code(jc, jc.pieces["code"], jc.pieces["c7"])
    ra = _a(jc)
    lignes_audit(jc, ra["run_t07"])
    lignes_p3bis(jc, APRES_A)
    m = jc.pieces["code"] / "src" / "controle_ia" / "t07" / "a.py"
    m.write_text("A = 2\n")
    with pytest.raises(rg.RefusRegistre, match="CODE-T07"):
        lv.etape_b(jc.racine, jc.registre, jc.config, RUN_T06, ra["run_t07"], instant=INSTANT_B)
    assert not (jc.racine / "diag" / ra["run_t07"] / "lecture-t07.json").exists()
    m.write_text("A = 1\n")
    lec = lv.etape_b(jc.racine, jc.registre, jc.config, RUN_T06, ra["run_t07"], instant=INSTANT_B + 1)
    assert lec["issue_critere_3"]


def test_DF02_passe_a_blanc_exige_code_t07(jc):
    """DF-02 : la passe à blanc contrôle `CODE-T07` avant tout (`code_t07_exige` vrai) : absente → refus ; conforme → tenue ;
    module retouché → refus ; rien d'écrit sur un refus."""
    from controle_ia.t07 import passe_blanc_v1 as pb
    from test_t07_passe_blanc_v1 import COUCHES_JOUET, extracteur_jouet, memoire
    jc.config["couches"] = list(COUCHES_JOUET)
    kw = dict(extracteur=extracteur_jouet(), mesure=memoire())
    with pytest.raises(pb.RefusPasse, match="CODE-T07 exigée"):
        pb.passe_a_blanc(jc.racine, jc.registre, jc.config, RUN_T06, instant=INSTANT, **kw)
    poser_code(jc, jc.pieces["code"], jc.pieces["c7"])
    r = pb.passe_a_blanc(jc.racine, jc.registre, jc.config, RUN_T06, instant=INSTANT + 1, **kw)
    assert r["issue"] == "tenue" and r["sortie"]["code_t07"]["commit"] == jc.pieces["c7"]
    (jc.pieces["code"] / "src" / "controle_ia" / "t07" / "b.py").write_text("B = 9\n")
    with pytest.raises(pb.RefusPasse, match="CODE-T07"):
        pb.passe_a_blanc(jc.racine, jc.registre, jc.config, RUN_T06, instant=INSTANT + 2, **kw)
    assert len(list((jc.racine / pb.DOSSIER).iterdir())) == 1
