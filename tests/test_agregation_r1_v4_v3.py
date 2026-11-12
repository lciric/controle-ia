"""Essais de `analyse_v3` : gardes de lancement Q1 à Q4 de la contre-lecture (cas sain et artefact, R5), règle du plafond,
liste fermée égale aux modules réellement importés."""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np
import pytest

from controle_ia.agregation_r1_v4 import analyse_v3 as an
from controle_ia.gardes import GardeArret
from controle_ia.manifeste import empreinte
from controle_ia.scellement import sceller
from test_agregation_r1_v4 import PREREG_MINIMAL, jeu_synthetique

RACINE = Path(__file__).resolve().parents[1]
RUN = "20261106-140000-agregation-r1-v4"


@pytest.fixture(scope="module")
def donnees(tmp_path_factory):
    d = tmp_path_factory.mktemp("donnees")
    ch = jeu_synthetique(d, largeur=4096, decalage=3.0)
    for c in ch[:2]:
        sceller(c)                         # compagnons de la réception v4 (simulés)
    return ch


def depot(tmp_path, table=None, sceller_prereg=True, chemin_prereg=an.PREREG_IMPOSE):
    dep = tmp_path / "depot"
    for c in an.CODE_CITE:
        (dep / c).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(RACINE / c, dep / c)
    lignes = table if table is not None else [f"| `{c}` | `{empreinte(RACINE / c)}` |" for c in an.CODE_CITE]
    pr = dep / chemin_prereg
    pr.parent.mkdir(parents=True, exist_ok=True)
    pr.write_text(PREREG_MINIMAL.format(a="0" * 64, b="1" * 64) + "\n" + "\n".join(lignes) + "\n", encoding="utf-8")
    if sceller_prereg:
        sceller(pr)
    for c in (["git", "init", "-q"], ["git", "add", "-A"],
              ["git", "-c", "user.email=e@x", "-c", "user.name=essai", "commit", "-qm", "essai"]):
        subprocess.run(c, cwd=dep, check=True)
    return dep, pr


def args(dep, ch, prereg=an.PREREG_IMPOSE):
    return ["--racine", str(dep), "--run-id", RUN, "--activations-maximum", str(ch[0]),
            "--activations-moyenne", str(ch[1]), "--scores-p3", str(ch[2]), "--prereg", prereg]


@pytest.fixture
def rapide(monkeypatch, donnees):
    orig = an.analyser
    monkeypatch.setitem(an.main.__globals__, "analyser", lambda e, r, *a: orig(e, r, 200, 200, 100, 10))
    monkeypatch.setattr(an, "EMPREINTE_SCORES_P3", empreinte(donnees[2]))


def test_sain_puis_second_passage(tmp_path, donnees, rapide):
    dep, _ = depot(tmp_path)
    assert an.main(args(dep, donnees)) == 0
    sortie = dep / "diag" / RUN / f"{an.NOM_SORTIE}.json"
    corps = json.loads(sortie.read_text(encoding="utf-8"))
    assert corps["resultat"]["H_AG"]
    m = json.loads((dep / "runs" / RUN / "manifeste.json").read_text(encoding="utf-8"))
    assert set(m["config"]["code_cite"]) == set(an.CODE_CITE) and m["preenregistrement"]["chemin"] == an.PREREG_IMPOSE
    subprocess.run(["git", "add", "-A"], cwd=dep, check=True)
    subprocess.run(["git", "-c", "user.email=e@x", "-c", "user.name=essai", "commit", "-qm", "sorties"], cwd=dep, check=True)
    a2 = args(dep, donnees)
    a2[3] = "20261106-150000-agregation-r1-v4"
    with pytest.raises(an.SecondPassage):
        an.main(a2)


def test_non_scelle_refuse_avant_chargement(tmp_path, donnees, rapide):
    dep, _ = depot(tmp_path, sceller_prereg=False)
    with pytest.raises(GardeArret, match="compagnon|scell"):
        an.main(args(dep, donnees))
    assert not (dep / "runs").exists()


def test_arbre_sale_refuse(tmp_path, donnees, rapide):
    dep, _ = depot(tmp_path)
    (dep / "fichier-en-trop.txt").write_text("x", encoding="utf-8")
    with pytest.raises(GardeArret, match="non propre"):
        an.main(args(dep, donnees))
    assert not (dep / "diag").exists()


def test_chemin_prereg_impose(tmp_path, donnees, rapide):
    dep, _ = depot(tmp_path, chemin_prereg="prereg/autre-nom.md")
    with pytest.raises(GardeArret, match="chemin imposé"):
        an.main(args(dep, donnees, prereg="prereg/autre-nom.md"))


def test_liste_fermee_alteree(tmp_path, donnees, rapide):
    table = [f"| `{c}` | `{empreinte(RACINE / c)}` |" for c in an.CODE_CITE]
    table[3] = f"| `{an.CODE_CITE[3]}` | `{'0' * 64}` |"
    dep, _ = depot(tmp_path, table=table)
    with pytest.raises(GardeArret, match="≠ citée"):
        an.main(args(dep, donnees))
    juste = [f"| `{c}` | `{empreinte(RACINE / c)}` |" for c in an.CODE_CITE]
    dep2, _ = depot(tmp_path / "b", table=juste[:-1])
    with pytest.raises(GardeArret, match="absent de la table"):
        an.main(args(dep2, donnees))


def test_empreintes_entrees(tmp_path, donnees, rapide, monkeypatch):
    dep, _ = depot(tmp_path)
    monkeypatch.setattr(an, "EMPREINTE_SCORES_P3", "f" * 64)
    with pytest.raises(GardeArret, match="citée"):
        an.main(args(dep, donnees))
    assert not (dep / "runs").exists()


def test_compagnon_activations_faux(tmp_path, donnees):
    d = tmp_path / "d"
    d.mkdir()
    ch = [d / Path(c).name for c in donnees]
    for a, b in zip(donnees, ch):
        shutil.copy(a, b)
    sceller(ch[0])
    (d / (ch[1].name + ".sha256")).write_text(f"{'0' * 64}  {ch[1].name}\n", encoding="utf-8")
    chemins = {"activations_maximum": ch[0], "activations_moyenne": ch[1], "scores_p3": ch[2]}
    with pytest.raises(GardeArret, match="scellée"):
        an.exiger_entrees(chemins, empreinte(ch[2]))
    (d / (ch[1].name + ".sha256")).unlink()
    sceller(ch[1])
    assert set(an.exiger_entrees(chemins, empreinte(ch[2]))) == set(chemins)


def test_noms_de_la_fiche(tmp_path, donnees):
    autre = tmp_path / "scores.npz"
    shutil.copy(donnees[2], autre)
    with pytest.raises(GardeArret, match="fiche v4"):
        an.exiger_entrees({"scores_p3": autre}, empreinte(autre))


def test_lecture_plafond():
    ok = {"C1": "non concluant par construction (x)", "C2": "confirmé à cette puissance",
          "C3": "confirmé à cette puissance"}
    assert an.lire_hag(ok, 0.90) == "appuyée"
    assert an.lire_hag(ok, 0.97) == "appuyée à m = 1 seulement"
    assert an.lire_hag(ok, 0.9995) == "non interprétable (plafond ou fuite)"
    assert an.lire_hag({**ok, "C2": "réfuté"}, 0.9) == "contredite"
    assert an.lire_hag({**ok, "C2": "réfuté"}, 0.9995) == "non interprétable (plafond ou fuite)"


def test_liste_fermee_egale_aux_modules_importes():
    code = ("import sys, json\nfrom pathlib import Path\nimport controle_ia.agregation_r1_v4.analyse_v3\n"
            "r = Path('src').resolve().parent\n"
            "print(json.dumps(sorted(str(Path(m.__file__).resolve().relative_to(r)) for k, m in list(sys.modules.items())"
            " if k.startswith('controle_ia') and getattr(m, '__file__', None))))")
    out = subprocess.run([sys.executable, "-c", code], cwd=RACINE, capture_output=True, text=True, check=True,
                         env={"PYTHONPATH": "src", "PATH": "/usr/bin:/bin"})
    assert sorted(json.loads(out.stdout)) == sorted(an.CODE_CITE)
