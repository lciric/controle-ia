"""Essais en mode jouet de la sonde de l'hôte durable d'A1-v3 (aucune location, aucun réseau, aucune clé de modèle).

Chaque garde de la sonde sur un cas sain et un artefact (R5) ; monde jouet : un dépôt privé nu (main avec un registre factice
et la vraie garde de calcul), Vast simulé par un fichier, la vraie course factice de la sonde (processus détaché).
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import subprocess
from pathlib import Path

import pytest

from controle_ia import hote_durable_a1_v3 as h
from controle_ia import sonde_hote_durable_a1_v3 as s

RACINE = Path(__file__).resolve().parents[1]
GARDE = RACINE / ".claude" / "hooks" / "garde_calcul.py"
JOUR = dt.date(2026, 11, 4)
JETON = "ghp_jouet_sonde_XYZ9876543210"
CLE_VAST = "vastjouet-sonde-cle-0001"
ENTETE = ("| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |\n"
          "|---|---|---|---|---|---|---|---|\n")
LIGNE_06 = ("| GO-2026-11-04-06 | 2026-11-04 | calcul | troisième course d'A1-v3, hôte durable | 400 USD | 2026-11-18 | "
            "Lazar | mot de Lazar |\n")
LIGNE_09 = ("| GO-2026-11-04-09 | 2026-11-04 | calcul | machine de l'hôte durable d'A1-v3 | 35 USD | 2026-11-18 | "
            "Lazar | mot de Lazar |\n")
OFFRE = {"id": 11, "num_gpus": 0, "dph_total": 0.12, "cpu_cores_effective": 8, "cpu_ram": 16000, "disk_space": 50,
         "reliability": 0.995}


def run(*cmd, cwd=None):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    return r.stdout.strip()


def sha(o: bytes) -> str:
    return hashlib.sha256(o).hexdigest()


# --- côté session ---------------------------------------------------------------------------------------------------------


def test_go_de_la_machine_cas_sain_artefacts_et_registre_reel(tmp_path):
    reg = tmp_path / "go.md"
    reg.write_text("# R\n\n" + ENTETE + LIGNE_06 + LIGNE_09)
    assert s.verifier_go_sonde(reg, GARDE, "GO-2026-11-04-09", JOUR)["plafond_usd"] == 35
    assert s.verifier_go_sonde(RACINE / "registres" / "go.md", GARDE, "GO-2026-11-04-09", JOUR)["echeance"] == "2026-11-18"
    for go, lignes, jour, motif in (("GO-2026-11-04-06", LIGNE_06 + LIGNE_09, JOUR, "aucun autre GO"),
                                    ("GO-2026-11-04-09", LIGNE_06, JOUR, "absent"),
                                    ("GO-2026-11-04-09", LIGNE_09.replace("35 USD", "36 USD"), JOUR, "exactement 35"),
                                    ("GO-2026-11-04-09", LIGNE_09, dt.date(2026, 11, 19), "hors de sa période"),
                                    ("GO-2026-11-04-09", LIGNE_09.replace("| calcul |", "| décision |"), JOUR, "calcul")):
        reg.write_text("# R\n\n" + ENTETE + lignes)
        with pytest.raises(h.Refus, match=motif):
            s.verifier_go_sonde(reg, GARDE, go, jour)


def test_plafond_de_depense_et_de_duree():
    assert s.verifier_plafond_sonde(0.40, 20) == pytest.approx(0.40 * 35 / 60)
    assert s.verifier_plafond_sonde(0.40, 30) <= s.PLAFOND_SONDE_USD
    for duree in (0, 31, -1):
        with pytest.raises(h.Refus, match="durée de la sonde"):
            s.verifier_plafond_sonde(0.1, duree)
    with pytest.raises(h.Refus, match="plafond 0.1 USD"):
        s.verifier_plafond_sonde(0.40, 20, plafond_usd=0.1)


def test_offre_la_moins_chere():
    offres = [OFFRE, dict(OFFRE, id=12, dph_total=0.09), dict(OFFRE, id=13, dph_total=0.05, num_gpus=1)]
    assert s.offre_la_moins_chere(offres, 12)["dph_total"] == 0.09  # la carte à 0,05 n'est pas conforme
    with pytest.raises(h.Refus, match="moins chère"):
        s.offre_la_moins_chere(offres, 11)
    with pytest.raises(h.Refus, match="sans carte"):
        s.offre_la_moins_chere(offres, 13)


def test_corps_sans_cle_de_modele():
    c = s.corps_sonde("a" * 40, OFFRE, 20, JETON)
    assert set(c["env"]) == {"COMMIT_PRIVE", "GO_ID", "PRIX_H_USD", "DUREE_MAX_S", "DEPOT_URL", "GH_TOKEN"}
    assert c["env"]["DUREE_MAX_S"] == "1200" and c["label"] == "sonde-a1-v3-v1"
    assert s.cles_de_modele({"CLE_ARGON": "x", "GEMINI_API_KEY_2": "y", "GH_TOKEN": "z", "ANTHROPIC_API_KEY": ""}) == \
        ["CLE_ARGON", "GEMINI_API_KEY_2"]
    with pytest.raises(h.Refus, match="GH_TOKEN absent"):
        s.corps_sonde("a" * 40, OFFRE, 20, "")
    assert s.AMORCE in __import__("base64").b64decode(c["script"].split()[1]).decode()


def test_creation_par_l_outil_refuse_une_cle_de_modele(tmp_path):
    outil = tmp_path / "vastai"
    outil.write_text("#!/bin/sh\necho \"${12} ${13}\" >&2\necho '{\"success\": true, \"new_contract\": 777}'\n")
    outil.chmod(0o755)
    c = s.corps_sonde("a" * 40, OFFRE, 20, JETON)
    assert s.ClientSondeCli(str(outil)).creer(11, c) == 777
    c["env"]["CLE_ARGON"] = "cle-qui-ne-doit-pas-partir"
    with pytest.raises(h.Refus, match="clé de modèle"):
        s.ClientSondeCli(str(outil)).creer(11, c)


def args_louer(tmp_path, **kw):
    reg = tmp_path / "go.md"
    reg.write_text("# R\n\n" + ENTETE + LIGNE_06 + kw.pop("ligne", LIGNE_09))
    offres = tmp_path / "offres.json"
    offres.write_text(json.dumps([OFFRE, dict(OFFRE, id=12, dph_total=0.09)]))
    a = dict(go="GO-2026-11-04-09", registre_main=str(reg), garde_main=str(GARDE), offres=str(offres), offre="12",
             commit_prive="a" * 40, journal_local=str(tmp_path / "journal-sonde.log"), duree_min="20",
             verifier_seulement=False)
    a.update(kw)
    return type("A", (), a)()


def test_louer_sonde_cas_sain_et_artefacts(tmp_path):
    vast = h.ClientVastJouet(tmp_path / "vast.json")
    env = {"GH_TOKEN": JETON}
    assert s.louer_sonde(args_louer(tmp_path), vast, JOUR, env) == 0
    assert [i["id"] for i in vast.instances()] == [90000001]
    j = (tmp_path / "journal-sonde.log").read_text()
    assert "la moins chère des conformes" in j and JETON not in j
    vast2 = h.ClientVastJouet(tmp_path / "vast2.json")
    for kw, e in (({"offre": "11"}, env), ({"duree_min": "45"}, env), ({"go": "GO-2026-11-04-06"}, env),
                  ({"ligne": LIGNE_09.replace("35 USD", "400 USD")}, env), ({"ligne": ""}, env), ({}, {})):
        assert s.louer_sonde(args_louer(tmp_path, **kw), vast2, JOUR, e) == 2
    assert s.louer_sonde(args_louer(tmp_path, verifier_seulement=True), vast2, JOUR, env) == 0
    assert vast2.instances() == []


# --- côté machine ---------------------------------------------------------------------------------------------------------


@pytest.fixture
def monde(tmp_path):
    def fabriquer(duree_max_s=1.0, course_s=60.0):
        nu = tmp_path / "prive.git"
        run("git", "init", "-q", "--bare", "-b", "main", str(nu))
        w = tmp_path / "w"
        run("git", "init", "-q", "-b", "main", str(w))
        (w / "registres").mkdir()
        (w / "registres/go.md").write_text("# R\n\n" + ENTETE + LIGNE_06 + LIGNE_09)
        (w / ".claude/hooks").mkdir(parents=True)
        (w / ".claude/hooks/garde_calcul.py").write_bytes(GARDE.read_bytes())
        run("git", "add", "-A", cwd=w)
        run("git", "-c", "user.name=j", "-c", "user.email=j@j", "commit", "-q", "-m", "main", cwd=w)
        run("git", "push", "-q", str(nu), "HEAD:refs/heads/main", cwd=w)
        clone = tmp_path / "amorce-depot"
        run("git", "clone", "-q", str(nu), str(clone))
        r = h.Reglages(travail=tmp_path / "sonde-a1-v3-v1", clone_prive=clone, periode_s=0.1, duree_max_s=duree_max_s,
                       plafond_machine_usd=s.PLAFOND_SONDE_USD, essais_poussee=2, attente_poussee_s=0, jouet=True,
                       vast_jouet=tmp_path / "vast.json", aujourd_hui=JOUR)
        h.ClientVastJouet(r.vast_jouet)._ecrire({"instances": [{"id": 90000001, "etat": "running"}], "gestes": []})
        env = {"GO_ID": "GO-2026-11-04-09", "PRIX_H_USD": "0.12", "DUREE_MAX_S": str(duree_max_s), "GH_TOKEN": JETON,
               "CONTAINER_ID": "90000001", "CONTAINER_API_KEY": CLE_VAST, "COMMIT_PRIVE": "a" * 40}
        return r, env, nu, course_s
    return fabriquer


def versees(nu, b):
    noms = subprocess.run(["git", "ls-tree", "-r", "--name-only", f"refs/heads/{b}"], cwd=nu, capture_output=True,
                          text=True)
    if noms.returncode != 0:
        return {}
    return {n: subprocess.run(["git", "show", f"refs/heads/{b}:{n}"], cwd=nu, capture_output=True).stdout
            for n in noms.stdout.split() if n.startswith(b + "/")}


def gestes(r):
    return json.loads(r.vast_jouet.read_text())["gestes"]


def test_sonde_cas_sain_plafond_de_duree_puis_destruction(monde):
    r, env, nu, course_s = monde(duree_max_s=1.5, course_s=60)
    assert s.MachineSonde(r, env, course_s).principal() == 0
    b = s.BRANCHE_SONDE
    f = versees(nu, b)
    j = f[f"{b}/journal-sonde-a1-v3-v1.log"].decode()
    for attendu in ("GO accepté par la garde de main", "faits de l'hôte", "clé d'instance : lecture faite, 1 instance(s), "
                    "la machine 90000001 vue", "course factice détachée", "PLAFOND DE DURÉE DE LA SONDE atteint",
                    "arrêt de course factice par son identifiant", "nature de la fin : plafond_de_duree_de_la_sonde"):
        assert attendu in j, attendu
    assert f[f"{b}/sortie-factice/battements.txt"].strip()
    manifeste = json.loads(f[f"{b}/sortie-factice/manifeste-factice.json"])
    assert manifeste["variables_de_cle"] == []  # la course factice n'a reçu aucune variable de clé
    for ligne in f[f"{b}/EMPREINTES-sonde-hote-durable-a1-v3-v1.txt"].decode().splitlines():
        e, nom = ligne.split("  ", 1)
        assert (nom, sha(f[f"{b}/{nom}"])) == (nom, e)
    assert all(JETON.encode() not in c and CLE_VAST.encode() not in c for c in f.values())
    assert gestes(r) == [["detruire", 90000001]]


def test_sonde_course_finie_avant_le_plafond(monde):
    r, env, nu, _ = monde(duree_max_s=30)
    assert s.MachineSonde(r, env, 0.3).principal() == 0
    f = versees(nu, s.BRANCHE_SONDE)
    assert "fin de la course factice avant le plafond : code 0" in f[f"{s.BRANCHE_SONDE}/journal-sonde-a1-v3-v1.log"].decode()
    assert f"{s.BRANCHE_SONDE}/sortie-factice/resultat-factice.json" in f
    assert gestes(r) == [["detruire", 90000001]]


@pytest.mark.parametrize("modif, motif", [
    ({"CLE_ARGON": "cle-interdite"}, "clé de modèle dans l'environnement"),
    ({"GEMINI_API_KEY_2": "cle-interdite"}, "clé de modèle dans l'environnement"),
    ({"GO_ID": "GO-2026-11-04-06"}, "aucun autre GO"),
    ({"PRIX_H_USD": "0.5"}, "prix horaire"),
    ({"GH_TOKEN": ""}, "GH_TOKEN"),
])
def test_sonde_refus_rien_ne_part(monde, modif, motif):
    r, env, nu, course_s = monde()
    env.update(modif)
    code = s.MachineSonde(r, env, course_s).principal()
    j = (r.travail / "journal-sonde-a1-v3-v1.log").read_text()
    assert motif in j and "course factice détachée" not in j
    assert "cle-interdite" not in j
    # en jouet le dépôt est local : le versement de l'état de refus passe même sans jeton
    assert code == 0 and "REFUS" in versees(nu, s.BRANCHE_SONDE)[f"{s.BRANCHE_SONDE}/journal-sonde-a1-v3-v1.log"].decode()
    assert gestes(r) == [["detruire", 90000001]]


def test_sonde_duree_au_dela_du_plafond_refusee(monde):
    r, env, nu, course_s = monde(duree_max_s=3600)
    assert s.MachineSonde(r, env, course_s).principal() == 0
    assert "durée de la sonde 60.0 min" in (r.travail / "journal-sonde-a1-v3-v1.log").read_text()


def test_sonde_reprise_ne_relance_rien(monde):
    r, env, nu, course_s = monde()
    r.travail.mkdir()
    (r.travail / "ETAT").write_text("course\n")
    assert s.MachineSonde(r, env, course_s).principal() == 0
    assert "REPRISE du conteneur de la sonde" in versees(nu, s.BRANCHE_SONDE_INTERROMPUE)[
        f"{s.BRANCHE_SONDE_INTERROMPUE}/journal-sonde-a1-v3-v1.log"].decode()
    assert not (r.travail / "sortie-factice").exists()
    assert gestes(r) == [["detruire", 90000001]]


def test_sonde_fuite_bloque_le_versement(monde):
    r, env, nu, _ = monde()
    r.travail.mkdir()
    (r.travail / "ETAT").write_text("course\n")
    (r.travail / "fuite.txt").write_text(JETON)
    assert s.MachineSonde(r, env).principal() == 3
    assert versees(nu, s.BRANCHE_SONDE_INTERROMPUE) == {}
    assert gestes(r) == [["arreter", 90000001]]


@pytest.mark.parametrize("env_modif, motif", [
    ({"GH_TOKEN": None}, "GH_TOKEN absente"), ({"CLE_ARGON": "x"}, "clé de modèle CLE_ARGON"),
    ({"GO_ID": "GO-2026-11-04-06"}, "au lieu de GO-2026-11-04-09"),
])
def test_amorce_sonde_refuse(tmp_path, env_modif, motif):
    env = {"PATH": os.environ["PATH"], "COMMIT_PRIVE": "a" * 40, "GO_ID": "GO-2026-11-04-09", "PRIX_H_USD": "0.1",
           "DUREE_MAX_S": "1200", "GH_TOKEN": JETON, "RACINE_AMORCE": str(tmp_path), "SAUTER_INSTALLATION": "1"}
    for k, v in env_modif.items():
        if v is None:
            env.pop(k)
        else:
            env[k] = v
    r = subprocess.run(["bash", str(RACINE / "scripts" / "amorce_sonde_hote_durable_a1_v3_v1.sh")], env=env,
                       capture_output=True, text=True)
    assert r.returncode == 2 and motif in r.stdout and JETON not in r.stdout + r.stderr
