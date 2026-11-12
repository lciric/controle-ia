"""Fenêtre de carte de la course (GO-2026-11-07-02) : 12 recherches à 15 minutes (ici pas de 0 s), A100 d'abord, bascule sur la relance seulement après la douzième absence d'offre.
Faux lanceur qui rend, à chaque appel, la réponse prévue. Cas sains et artefacts (R5)."""
import os
import subprocess
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]
FENETRE = RACINE / "scripts" / "fenetre_carte_t06_v1.sh"


def _faux_lanceur(tmp_path, reponses: list[tuple[int, str]]) -> Path:
    """Le n-ième appel rend la n-ième réponse (la dernière se répète) ; chaque appel est consigné avec ses arguments."""
    d = tmp_path / "rep"
    d.mkdir(exist_ok=True)
    lignes = ["#!/usr/bin/env bash", f'echo "$*" >> "{tmp_path}/appels.txt"', f'n=$(wc -l < "{tmp_path}/appels.txt")', 'case "$n" in']
    for k, (code, texte) in enumerate(reponses, 1):
        lignes.append(f'{k}) echo "{texte}"; exit {code};;')
    code, texte = reponses[-1]
    lignes += [f'*) echo "{texte}"; exit {code};;', "esac"]
    f = tmp_path / "faux-lanceur.sh"
    f.write_text("\n".join(lignes) + "\n", encoding="utf-8")
    (tmp_path / "appels.txt").write_text("", encoding="utf-8")
    return f


def _lancer(tmp_path, reponses, **env):
    dossier = tmp_path / "dossier"
    dossier.mkdir(exist_ok=True)
    e = {"PATH": os.environ["PATH"], "FENETRE_PAS_S": "0", **env}
    r = subprocess.run(["bash", str(FENETRE), str(_faux_lanceur(tmp_path, reponses)), str(dossier), "0"], env=e, capture_output=True, text=True, timeout=60)
    appels = (tmp_path / "appels.txt").read_text(encoding="utf-8").splitlines()
    return r, appels, (dossier / "fenetre.txt").read_text(encoding="utf-8") if (dossier / "fenetre.txt").exists() else ""


AUCUNE = (3, "aucune offre conforme dans la liste filtrée : rang 1 : stockage trop cher : nœud, pas de création")


def test_cas_sain_une_a100_conforme_des_la_premiere_recherche(tmp_path):
    r, appels, j = _lancer(tmp_path, [(0, "OFFRE CONFORME : id=1 rang=1")])
    assert r.returncode == 0 and "A100 CONFORME à la recherche 1/12" in r.stdout and len(appels) == 1
    assert appels[0] == "creation auto course 0 " + str(tmp_path / "dossier")


def test_cas_sain_une_a100_apparait_a_la_cinquieme_recherche(tmp_path):
    r, appels, j = _lancer(tmp_path, [AUCUNE] * 4 + [(0, "OFFRE CONFORME : id=2 rang=1")])
    assert r.returncode == 0 and "recherche 5/12" in r.stdout and len(appels) == 5
    assert j.count("recherche") == 5 and "code 3" in j


def test_fenetre_epuisee_apres_douze_recherches_code_10(tmp_path):
    r, appels, j = _lancer(tmp_path, [AUCUNE])
    assert r.returncode == 10 and len(appels) == 12 and "FENÊTRE ÉPUISÉE" in r.stdout and "creation auto relance" in r.stdout
    assert j.count("recherche") == 12 and "12/12" in j


def test_treizieme_recherche_n_existe_pas(tmp_path):
    r, appels, _ = _lancer(tmp_path, [AUCUNE])
    assert len(appels) == 12


@pytest.mark.parametrize("code, texte", [(3, "trois essais de création déjà faits (essai_creation = 3) : arrêt"), (3, "dépense cumulée déjà au plafond"), (2, "jeton absent : pas de création"),
                                         (2, "GO non conforme au jour de la création"), (3, "inventaire : instance du programme présente")])
def test_artefact_une_autre_reponse_n_est_pas_une_absence_d_offre_pas_de_bascule(tmp_path, code, texte):
    r, appels, j = _lancer(tmp_path, [(code, texte)])
    assert r.returncode == 2 and len(appels) == 1 and "pas de bascule" in r.stdout, (r.stdout, r.stderr)


def test_artefact_arret_a_la_septieme_recherche_sur_une_erreur(tmp_path):
    r, appels, j = _lancer(tmp_path, [AUCUNE] * 6 + [(2, "recherche filtrée impossible (--storage 150) : pas de création")])
    assert r.returncode == 2 and len(appels) == 7 and "recherche 7/12" in r.stdout


def test_echeance_transmise_et_parametres_illisibles(tmp_path):
    dossier = tmp_path / "dossier"
    dossier.mkdir()
    f = _faux_lanceur(tmp_path, [(0, "OFFRE CONFORME : id=3")])
    r = subprocess.run(["bash", str(FENETRE), str(f), str(dossier), "0", "1794800000"], env={"PATH": os.environ["PATH"], "FENETRE_PAS_S": "0"}, capture_output=True, text=True)
    assert r.returncode == 0 and "1794800000" in (tmp_path / "appels.txt").read_text()
    r = subprocess.run(["bash", str(FENETRE), str(f), str(dossier), "0"], env={"PATH": os.environ["PATH"], "FENETRE_N": "abc"}, capture_output=True, text=True)
    assert r.returncode == 2
    r = subprocess.run(["bash", str(FENETRE), str(f), str(tmp_path / "absent"), "0"], env={"PATH": os.environ["PATH"]}, capture_output=True, text=True)
    assert r.returncode == 2
