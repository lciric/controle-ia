"""Essais en mode jouet de la sonde v9 de l'hôte durable d'A1-v3 (contre-lectures `contre-lecture-sonde-v1.md` à
`contre-lecture-sonde-v3.md`, machine à une carte (v9), mandataire du conteneur de la fille, réponse de
création catégorisée ; m7 : cas sain
et artefact pour chaque garde, l'amorce et le script de démarrage compris). Aucune location, aucun réseau, aucune clé : `curl`
et `vastai` sont des outils factices, les dépôts sont locaux, Vast est un fichier.
"""
from __future__ import annotations

import base64
import datetime as dt
import hashlib
import json
import os
import subprocess
import sys
import time
import urllib.error
from pathlib import Path

import pytest

from controle_ia import hote_durable_a1_v3 as h
from controle_ia import sonde_hote_durable_a1_v3_v9 as s

RACINE = Path(__file__).resolve().parents[1]
GARDE = RACINE / ".claude" / "hooks" / "garde_calcul.py"
JOUR = dt.date(2026, 11, 5)  # v9 : jour de validité de GO-2026-11-05-01 (passé explicitement, jamais pris à la collecte)
JETON = "ghp_jouet_sonde_v4_XYZ987654321"
CLE_VAST = "vastjouet-cle-instance-v3-0001"
CLE_COMPTE = "vastjouet-cle-compte-v3-0002"
ENTETE = ("| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |\n"
          "|---|---|---|---|---|---|---|---|\n")
LIGNE_06 = "| GO-2026-11-04-06 | 2026-11-04 | calcul | A1-v3, Argon | 400 USD | 2026-11-18 | Lazar | mot |\n"
LIGNE_09_ANCIEN = "| GO-2026-11-04-09 | 2026-11-04 | calcul | machine de l'hôte durable | 35 USD | 2026-11-18 | Lazar | mot |\n"
LIGNE_09 = "| GO-2026-11-05-01 | 2026-11-05 | calcul | sonde v9, machine à une carte | 1 USD | 2026-11-06 | Lazar | mot |\n"  # v9
OFFRE = {"id": 11, "resource_type": "gpu", "num_gpus": 1, "dph_total": 0.12, "cpu_cores_effective": 8, "cpu_ram": 16000, "disk_space": 50,
         "reliability": 0.995}


def run(*cmd, cwd=None, env=None):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, env=env)
    assert r.returncode == 0, r.stderr
    return r.stdout.strip()


def outil(tmp_path, nom, corps):
    p = tmp_path / nom
    p.write_text("#!/bin/sh\n" + corps)
    p.chmod(0o755)
    return p


# --- bornes ----------------------------------------------------------------------------------------------------------------


def test_duree_et_plafond_mecanique():
    assert s.verifier_duree("1200") == 1200
    for brut in ("59", "1801", "abc", "", None, "12.5", "-60"):
        with pytest.raises(h.Refus, match="DUREE_MAX_S"):
            s.verifier_duree(brut)
    # borne de la minuterie : démarrage 10 min + durée + 25 min + 10 min de vie après l'échéance
    assert s.cout_maximal_usd(0.40, 1200) == pytest.approx(0.40 * (600 + 1200 + 1500 + 600 + 300) / 3600)  # f-2
    assert s.verifier_plafond(0.40, 1200) <= s.PLAFOND_SONDE_USD
    with pytest.raises(h.Refus, match="plafond 0.1"):
        s.verifier_plafond(0.40, 1200, plafond_usd=0.1)


def test_cles_interdites_communes_a_l_amorce():
    assert s.cles_de_modele({"CLE_ARGON": "x", "RR_ANTHROPIC_API_KEY_3": "y", "GH_TOKEN": "z", "KIMI_X": ""}) == \
        ["CLE_ARGON", "RR_ANTHROPIC_API_KEY_3"]
    amorce = (RACINE / s.AMORCE).read_text()
    assert s.MOTIF_AMORCE in amorce  # f2 : même liste, même ordre


# --- côté pilote -----------------------------------------------------------------------------------------------------------


def args_louer(tmp_path, **kw):
    reg = tmp_path / "go.md"
    reg.write_text("# R\n\n" + ENTETE + LIGNE_06 + kw.pop("ligne", LIGNE_09))
    offres = tmp_path / "offres.json"
    offres.write_text(json.dumps([OFFRE, dict(OFFRE, id=12, dph_total=0.09)]))
    a = dict(go="GO-2026-11-05-01", registre_main=str(reg), garde_main=str(GARDE), offres=str(offres), offre="12",
             commit_prive="a" * 40, journal_local=str(tmp_path / "journal-sonde-v9.log"), duree_s="1200",
             verifier_seulement=False)
    a.update(kw)
    return type("A", (), a)()


ENV_PILOTE = {"GH_TOKEN": JETON, "VAST_API_KEY": CLE_COMPTE, "GO_ID": "GO-2026-11-05-01"}


def test_louer_cas_sain_etat_ecrit_puis_seconde_location_refusee(tmp_path):
    vast = h.ClientVastJouet(tmp_path / "vast.json")
    t0 = dt.datetime(2026, 11, 4, 13, 0, tzinfo=dt.timezone.utc)
    assert s.louer(args_louer(tmp_path), vast, JOUR, dict(ENV_PILOTE), t0) == 0
    e = json.loads((tmp_path / "journal-sonde-v9.log.etat.json").read_text())
    assert e["identifiant"] == 90000001 and e["etiquette"] == "sonde-a1-v3-v9"
    assert e["borne_signe_de_vie_utc"] == "2026-11-04T13:30:00Z" and e["echeance_finale_utc"] == "2026-11-04T13:55:00Z"
    j = (tmp_path / "journal-sonde-v9.log").read_text()
    assert "LIGNE POUR registres/etat.md" in j and "-y" in j and JETON not in j and CLE_COMPTE not in j
    assert s.louer(args_louer(tmp_path), vast, JOUR, dict(ENV_PILOTE), t0) == 2  # R12 : jamais une seconde location
    assert len(vast.instances()) == 1


@pytest.mark.parametrize("env_modif, kw, motif", [
    ({"GO_ID": None}, {}, "GO_ID=GO-2026-11-05-01 exigé"),
    ({"CLE_ARGON": "x"}, {}, "clé de modèle"),
    ({}, {"go": "GO-2026-11-04-06"}, "aucun autre GO"),
    ({}, {"ligne": ""}, "absent"),
    ({}, {"offre": "11"}, "moins chère"),
    ({}, {"duree_s": "5000"}, "DUREE_MAX_S"),
    ({"GH_TOKEN": None}, {}, "GH_TOKEN absent"),
])
def test_louer_artefacts_rien_cree(tmp_path, env_modif, kw, motif):
    vast = h.ClientVastJouet(tmp_path / "vast.json")
    env = dict(ENV_PILOTE)
    for k, v in env_modif.items():
        env.pop(k) if v is None else env.__setitem__(k, v)
    assert s.louer(args_louer(tmp_path, **kw), vast, JOUR, env) == 2
    assert vast.instances() == [] and motif in (tmp_path / "journal-sonde-v9.log").read_text()


def test_louer_verification_seule_rien_cree(tmp_path):
    vast = h.ClientVastJouet(tmp_path / "vast.json")
    assert s.louer(args_louer(tmp_path, verifier_seulement=True), vast, JOUR, dict(ENV_PILOTE)) == 0
    assert vast.instances() == []


def client_factice(tmp_path, sortie, code=0):
    journal = tmp_path / "args-vastai.txt"
    o = outil(tmp_path, "vastai", f'echo "$@" >> "{journal}"\necho "VAST_API_KEY=$VAST_API_KEY" >&2\ncat <<\'FIN\'\n{sortie}\nFIN\n'
                                  f"exit {code}\n")
    env = {"PATH": os.environ["PATH"], "HOME": str(tmp_path), "VAST_API_KEY": CLE_COMPTE, "GH_TOKEN": JETON}
    return s.ClientPilote(env, str(o)), journal


def test_client_pilote_exige_la_cle_et_lit_une_reponse_sur_plusieurs_lignes(tmp_path):
    with pytest.raises(h.Refus, match="VAST_API_KEY absente"):
        s.ClientPilote({"PATH": "/usr/bin"})
    c, _ = client_factice(tmp_path, '{\n  "success": true,\n  "new_contract": 4321\n}')
    corps = s.corps("a" * 40, OFFRE, 1200, JETON, 1_800_000_000)
    assert c.creer(11, corps) == 4321


@pytest.mark.parametrize("sortie, code, motif", [
    ('{"success": false, "msg": "pas de place"}', 0, "erreur Vast"),  # v7 (a) : catégorie sûre
    ("texte sans JSON", 0, "CREATION_INCERTAINE"),
    ("erreur d'environnement GH_TOKEN=" + JETON, 1, "code 1"),
])
def test_client_pilote_reponses_refusees_illisibles_et_masquage(tmp_path, sortie, code, motif):
    c, _ = client_factice(tmp_path, sortie, code)
    with pytest.raises(h.Refus, match=motif) as e:
        c.creer(11, s.corps("a" * 40, OFFRE, 1200, JETON, 1_800_000_000))
    assert JETON not in str(e.value) and CLE_COMPTE not in str(e.value)


def test_creation_incertaine_bloque_toute_nouvelle_location(tmp_path):
    c, _ = client_factice(tmp_path, "texte sans JSON")
    assert s.louer(args_louer(tmp_path), c, JOUR, dict(ENV_PILOTE)) == 2
    assert (tmp_path / "journal-sonde-v9.log.creation-incertaine").exists()
    c2, _ = client_factice(tmp_path, '{"success": true, "new_contract": 5}')
    assert s.louer(args_louer(tmp_path), c2, JOUR, dict(ENV_PILOTE)) == 2  # inventaire d'abord


def test_client_pilote_espace_refuse_et_destruction_avec_y(tmp_path):
    c, journal = client_factice(tmp_path, "[]")
    corps = s.corps("a" * 40, OFFRE, 1200, JETON, 1_800_000_000)
    corps["env"]["DEPOT_URL"] = "a b"
    with pytest.raises(h.Refus, match="espace"):
        c.creer(11, corps)
    c.detruire(777)
    assert journal.read_text().split("\n")[0] == "destroy instance 777 -y"  # M2
    for p in s.PROTEGEES:
        with pytest.raises(h.Refus, match="protégée"):
            c.detruire(p)


class VastFactice:
    def __init__(self, instances, reste_apres_destruction=False):
        self.liste, self.reste, self.gestes = list(instances), reste_apres_destruction, []

    def instances(self):
        return list(self.liste)

    def detruire(self, n):
        self.gestes.append(("detruire", n))
        if not self.reste:
            self.liste = [i for i in self.liste if i["id"] != n]


def etat_pilote(tmp_path, ident=4321):
    p = tmp_path / "etat.json"
    p.write_text(json.dumps({"identifiant": ident, "etiquette": "sonde-a1-v3-v9", "t0_utc": "2026-11-04T13:00:00Z",
                             "borne_signe_de_vie_utc": "2026-11-04T13:30:00Z",
                             "echeance_finale_utc": "2026-11-04T13:55:00Z"}))
    return type("A", (), {"etat": str(p), "journal_local": str(tmp_path / "controle.log")})()


def heure(hh, mm):
    return dt.datetime(2026, 11, 4, hh, mm, tzinfo=dt.timezone.utc)


@pytest.mark.parametrize("instances, vie, quand, code, gestes", [
    ([], False, heure(14, 30), 0, []),                                                       # déjà détruite
    ([{"id": 4321, "label": "sonde-a1-v3-v9"}], True, heure(13, 40), 5, []),                  # vivante : recontrôler (M-A)
    ([{"id": 4321, "label": "sonde-a1-v3-v9"}], False, heure(13, 20), 5, []),                 # avant la borne : recontrôler
    ([{"id": 4321, "label": "sonde-a1-v3-v9"}], True, heure(14, 10), 1, [("detruire", 4321)]),   # T0 + 70 : détruite (M-A)
    ([{"id": 4321, "label": "sonde-a1-v3-v9"}], False, heure(13, 31), 1, [("detruire", 4321)]),  # jamais démarrée (m2)
    ([{"id": 4321, "label": "sonde-a1-v3-v9"}], True, heure(14, 6), 1, [("detruire", 4321)]),    # minuterie en défaut
    ([{"id": 4321, "label": "autre"}], False, heure(14, 30), 2, []),                           # étiquette (f8)
])
def test_controler_du_pilote(tmp_path, instances, vie, quand, code, gestes):
    v = VastFactice(instances)
    assert s.controler(etat_pilote(tmp_path), v, lambda: vie, quand, {}) == code
    assert v.gestes == gestes


def test_controler_protegee_et_destruction_non_suivie(tmp_path):
    v = VastFactice([{"id": 58936096, "label": "sonde-a1-v3-v9"}])
    assert s.controler(etat_pilote(tmp_path, 58936096), v, lambda: False, heure(15, 0), {}) == 2 and v.gestes == []
    v = VastFactice([{"id": 4321, "label": "sonde-a1-v3-v9"}], reste_apres_destruction=True)
    assert s.controler(etat_pilote(tmp_path), v, lambda: False, heure(15, 0), {}) == 3


def test_offre_la_moins_chere_tiree_de_la_reponse(tmp_path, capsys):
    f = tmp_path / "offres.json"
    f.write_text(json.dumps([OFFRE, dict(OFFRE, id=12, dph_total=0.09), dict(OFFRE, id=13, dph_total=0.01, num_gpus=2)]))
    assert s.principal(["offre", "--offres", str(f)]) == 0 and capsys.readouterr().out.strip() == "12"
    f.write_text(json.dumps([dict(OFFRE, num_gpus=2)]))
    assert s.principal(["offre", "--offres", str(f)]) == 2


# --- script de démarrage : minuterie d'abord (M1), sans Python ------------------------------------------------------------


def depot_avec_amorce(tmp_path, amorce: str) -> tuple[Path, str]:
    nu = tmp_path / "prive.git"
    run("git", "init", "-q", "--bare", "-b", "main", str(nu))
    run("git", "-C", str(nu), "config", "uploadpack.allowFilter", "true")
    run("git", "-C", str(nu), "config", "uploadpack.allowReachableSHA1InWant", "true")  # comme GitHub
    w = tmp_path / "w-amorce"
    run("git", "init", "-q", "-b", "main", str(w))
    (w / "scripts").mkdir()
    (w / s.AMORCE).write_text(amorce)
    run("git", "add", "-A", cwd=w)
    run("git", "-c", "user.name=j", "-c", "user.email=j@j", "commit", "-q", "-m", "amorce", cwd=w)
    run("git", "push", "-q", str(nu), "HEAD:refs/heads/main", cwd=w)
    return nu, run("git", "rev-parse", "HEAD", cwd=w)


def lancer_demarrage(tmp_path, commit, depot, delete_code="200", label="sonde-a1-v3-v9", ident="123", minuterie=None):
    racine = tmp_path / "racine"
    racine.mkdir(exist_ok=True)
    if minuterie:
        (racine / "sonde-v9-minuterie.txt").write_text(minuterie)
    appels = tmp_path / "appels-curl.txt"
    bin_ = tmp_path / "bin"
    bin_.mkdir(exist_ok=True)
    outil(bin_, "curl", f'echo "$@" >> "{appels}"\n'
                        f'case "$*" in *"-X DELETE"*) printf "{delete_code}";; *"-X PUT"*) printf "200";; '
                        f'*) printf \'{{"id": {ident}, "label": "{label}"}}\';; esac\n')
    script = s.script_de_demarrage(commit)
    env = {"PATH": f"{bin_}:{os.environ['PATH']}", "HOME": str(tmp_path), "RACINE_SONDE": str(racine),
           "API_VAST": "https://vast.invalide/api/v0", "DUREE_MAX_S": "1", "SONDE_MARGE_S": "1", "SONDE_VIE_APRES_S": "1",
           "DEPOT_URL": str(depot), "GH_TOKEN": JETON, "CONTAINER_ID": ident, "CONTAINER_API_KEY": CLE_VAST,
           "GIT_CONFIG_GLOBAL": "/dev/null"}
    debut = time.time()
    r = subprocess.run(["bash", "-c", script], env=env, capture_output=True, text=True, timeout=120)
    # la minuterie, détachée, peut finir juste après le processus principal
    fin = time.time() + 15
    while time.time() < fin and "HTTP" not in ((racine / "sonde-v9-minuterie.log").read_text()
                                               if (racine / "sonde-v9-minuterie.log").exists() else ""):
        time.sleep(0.2)
    return r, racine, (appels.read_text() if appels.exists() else ""), time.time() - debut


def test_demarrage_cas_sain_minuterie_puis_clone_puis_amorce_puis_destruction(tmp_path):
    nu, commit = depot_avec_amorce(tmp_path, 'echo "amorce jouée" > "$RACINE_SONDE/amorce-jouee.txt"\n')
    r, racine, appels, _ = lancer_demarrage(tmp_path, commit, nu)
    assert r.returncode == 0, r.stderr
    assert (racine / "amorce-jouee.txt").exists()
    temps = (racine / "sonde-v9-temps.txt").read_text()
    assert "clone 0 en" in temps and "amorce finie" in temps
    log = (racine / "sonde-v9-minuterie.log").read_text()
    assert "DELETE instance 123 (essai 1) : HTTP 200" in log and "ALARME" not in log
    assert "-X DELETE" in appels and "/instances/123/" in appels and "-X PUT" not in appels
    assert CLE_VAST not in log + temps  # la clé d'instance ne va que dans l'en-tête de curl


def test_demarrage_clone_impossible_la_minuterie_detruit_quand_meme(tmp_path):
    r, racine, appels, _ = lancer_demarrage(tmp_path, "b" * 40, tmp_path / "pas-de-depot.git")
    assert "clone" in (racine / "sonde-v9-temps.txt").read_text() and not (racine / "amorce-jouee.txt").exists()
    assert "DELETE instance 123 (essai 1) : HTTP 200" in (racine / "sonde-v9-minuterie.log").read_text()  # M1(a)


@pytest.mark.parametrize("kw, attendu, interdit", [
    ({"delete_code": "403"}, "ALARME : destruction non obtenue avant la fin de vie", "-X PUT"),  # m-a : jamais d'arrêt
    ({"label": "autre-chose"}, "pas sonde-a1-v3-v9 : aucun geste", "-X DELETE"),
    ({"ident": "58936099"}, "instance protégée : aucun geste", "-X DELETE"),
    ({"ident": "12a"}, "identifiant illisible : aucun geste", "-X DELETE"),
])
def test_demarrage_artefacts_de_la_minuterie(tmp_path, kw, attendu, interdit):
    r, racine, appels, _ = lancer_demarrage(tmp_path, "b" * 40, tmp_path / "pas-de-depot.git", **kw)
    fin = time.time() + 15
    while time.time() < fin and attendu not in (racine / "sonde-v9-minuterie.log").read_text():
        time.sleep(0.2)
    assert attendu in (racine / "sonde-v9-minuterie.log").read_text()
    if interdit:
        assert interdit not in appels


def test_demarrage_reprise_garde_l_echeance_d_origine(tmp_path):
    passe = int(time.time()) - 3600
    r, racine, appels, duree = lancer_demarrage(tmp_path, "b" * 40, tmp_path / "pas-de-depot.git",
                                                minuterie=f"{passe - 100} {passe}\n")
    assert (racine / "sonde-v9-minuterie.txt").read_text().split() == [str(passe - 100), str(passe)]
    assert "DELETE instance 123" in (racine / "sonde-v9-minuterie.log").read_text() and duree < 60


def test_script_de_demarrage_exige_un_hash_et_corps_sans_cle():
    with pytest.raises(h.Refus):
        s.script_de_demarrage("main")
    c = s.corps("a" * 40, OFFRE, 1200, JETON, 1_800_000_000)
    assert set(c["env"]) == {"COMMIT_PRIVE", "GO_ID", "PRIX_H_USD", "DUREE_MAX_S", "DEPOT_URL", "GH_TOKEN", "ECHEANCE_UTC_S",
                             "TIR_MINUTERIE"}
    assert c["label"] == "sonde-a1-v3-v9" and c["env"]["GO_ID"] == "GO-2026-11-05-01"
    assert c["env"]["ECHEANCE_UTC_S"] == "1800000000" and c["env"]["TIR_MINUTERIE"] == "0"
    for mauvaise in (None, 0, -5, True, "1800000000"):
        with pytest.raises(h.Refus, match="échéance absolue"):
            s.corps("a" * 40, OFFRE, 1200, JETON, mauvaise)
    texte = base64.b64decode(c["script"].split()[1]).decode()
    assert texte.index("setsid bash") < texte.index("git init")  # la minuterie avant le clonage (M1)
    with pytest.raises(h.Refus, match="GH_TOKEN"):
        s.corps("a" * 40, OFFRE, 1200, "", 1_800_000_000)


# --- amorce v9 (m7 : cas sain jusqu'à exec, et artefacts) -----------------------------------------------------------------


def amorce(tmp_path, **modif):
    racine = tmp_path / "racine-amorce"
    d = racine / "amorce-depot" / "src" / "controle_ia"
    d.mkdir(parents=True, exist_ok=True)
    for nom in ("sonde_hote_durable_a1_v3.py", "hote_durable_a1_v3.py"):
        (d / nom).write_text("# factice\n")
    (d / "sonde_hote_durable_a1_v3_v9.py").write_text(
        "import os, sys, pathlib\npathlib.Path(os.environ['RACINE_AMORCE'], 'exec-atteint.txt').write_text(' '.join(sys.argv[1:]))\n")
    env = {"PATH": os.environ["PATH"], "COMMIT_PRIVE": "a" * 40, "GO_ID": "GO-2026-11-05-01", "PRIX_H_USD": "0.1",
           "DUREE_MAX_S": "1200", "ECHEANCE_UTC_S": "1800000000", "GH_TOKEN": JETON, "RACINE_AMORCE": str(racine),
           "SAUTER_INSTALLATION": "1"}
    for k, v in modif.items():
        env.pop(k) if v is None else env.__setitem__(k, v)
    r = subprocess.run(["bash", str(RACINE / s.AMORCE)], env=env, capture_output=True, text=True)
    return r, racine


def test_amorce_cas_sain_jusqu_a_exec(tmp_path):
    r, racine = amorce(tmp_path)
    assert r.returncode == 0, r.stdout + r.stderr
    assert (racine / "exec-atteint.txt").read_text() == "hote" and JETON not in r.stdout + r.stderr


@pytest.mark.parametrize("modif, motif", [
    ({"GH_TOKEN": None}, "GH_TOKEN absente"), ({"CLE_ARGON": "x"}, "clé de modèle CLE_ARGON"),
    ({"RR_ANTHROPIC_API_KEY_3": "x"}, "clé de modèle RR_ANTHROPIC_API_KEY_3"),
    ({"GO_ID": "GO-2026-11-04-06"}, "au lieu de GO-2026-11-05-01"), ({"DUREE_MAX_S": "12a"}, "non entière"),
    ({"GO_ID": "GO-2026-11-04-09"}, "au lieu de GO-2026-11-05-01"),
])
def test_amorce_artefacts(tmp_path, modif, motif):
    r, racine = amorce(tmp_path, **modif)
    assert r.returncode == 2 and motif in r.stdout and not (racine / "exec-atteint.txt").exists()
    assert JETON not in r.stdout + r.stderr


def test_amorce_module_absent(tmp_path):
    racine = tmp_path / "racine-amorce"
    r, _ = amorce(tmp_path)
    (racine / "amorce-depot/src/controle_ia/hote_durable_a1_v3.py").unlink()
    (racine / "exec-atteint.txt").unlink()
    env = {"PATH": os.environ["PATH"], "COMMIT_PRIVE": "a" * 40, "GO_ID": "GO-2026-11-05-01", "PRIX_H_USD": "0.1",
           "DUREE_MAX_S": "1200", "ECHEANCE_UTC_S": "1800000000", "GH_TOKEN": JETON, "RACINE_AMORCE": str(racine),
           "SAUTER_INSTALLATION": "1"}
    r = subprocess.run(["bash", str(RACINE / s.AMORCE)], env=env, capture_output=True, text=True)
    assert r.returncode == 2 and "absent du commit" in r.stdout


# --- machine ---------------------------------------------------------------------------------------------------------------


@pytest.fixture
def monde(tmp_path):
    def fabriquer(depuis_s=59.7, etiquette="sonde-a1-v3-v9"):
        nu = tmp_path / "prive-machine.git"
        run("git", "init", "-q", "--bare", "-b", "main", str(nu))
        w = tmp_path / "w-machine"
        run("git", "init", "-q", "-b", "main", str(w))
        (w / "registres").mkdir()
        (w / "registres/go.md").write_text("# R\n\n" + ENTETE + LIGNE_06 + LIGNE_09)
        (w / ".claude/hooks").mkdir(parents=True)
        (w / ".claude/hooks/garde_calcul.py").write_bytes(GARDE.read_bytes())
        run("git", "add", "-A", cwd=w)
        run("git", "-c", "user.name=j", "-c", "user.email=j@j", "commit", "-q", "-m", "main", cwd=w)
        run("git", "push", "-q", str(nu), "HEAD:refs/heads/main", cwd=w)
        racine = tmp_path / "root"
        racine.mkdir()
        clone = racine / "amorce-depot"
        run("git", "clone", "-q", str(nu), str(clone))
        t0 = time.time() - depuis_s  # départ du conteneur, écrit par le script de démarrage
        (racine / "sonde-v9-minuterie.txt").write_text(f"{int(t0)} {int(t0) + 1260 + 1500}\n")
        (racine / "sonde-v9-temps.txt").write_text("demarrage …\nclone 0 en 3 s\n")
        (racine / "amorce-sonde-a1v3-v9.log").write_text("AMORCE SONDE V9 : installations en 40 s\n")
        (racine / "sonde-v9-memoire.txt").write_text("2026-11-04T22:40:00Z MemTotal 16384000 kB\n")
        r = s.reglages({})
        r.travail, r.clone_prive, r.periode_s, r.attente_poussee_s = racine / "sonde-a1-v3-v9", clone, 0.1, 0
        r.jouet, r.vast_jouet, r.aujourd_hui = True, tmp_path / "vast.json", JOUR
        h.ClientVastJouet(r.vast_jouet)._ecrire({"instances": [{"id": 90000001, "label": etiquette}], "gestes": []})
        env = {"GO_ID": "GO-2026-11-05-01", "PRIX_H_USD": "0.12", "DUREE_MAX_S": "60", "GH_TOKEN": JETON,
               "CONTAINER_ID": "90000001", "CONTAINER_API_KEY": CLE_VAST, "COMMIT_PRIVE": "a" * 40,
               "ECHEANCE_UTC_S": str(int(time.time()) + 3000), "TIR_MINUTERIE": "0"}
        return r, env, nu
    return fabriquer


def versees(nu, b):
    noms = subprocess.run(["git", "ls-tree", "-r", "--name-only", f"refs/heads/{b}"], cwd=nu, capture_output=True, text=True)
    if noms.returncode != 0:
        return {}
    return {n: subprocess.run(["git", "show", f"refs/heads/{b}:{n}"], cwd=nu, capture_output=True).stdout
            for n in noms.stdout.split()}


def gestes(r):
    return json.loads(r.vast_jouet.read_text())["gestes"]


def test_machine_cas_sain(monde):
    r, env, nu = monde()
    assert s.MachineSondeV9(r, env, 120).principal() == 0
    vie = versees(nu, s.BRANCHE_VIE)
    assert f"{s.BRANCHE_VIE}/signe-de-vie.json" in vie
    f = versees(nu, s.BRANCHE)
    b = s.BRANCHE
    j = f[f"{b}/journal-sonde-a1-v3-v9.log"].decode()
    for attendu in ("GO accepté par la garde de main", "signe de vie poussé", "clé d'instance : lecture faite",
                    "PLAFOND DE DURÉE DE LA SONDE atteint", "nature de la fin : plafond_de_duree_de_la_sonde"):
        assert attendu in j, attendu
    for nom in s.FICHIERS_DEMARRAGE[:1] + s.FICHIERS_DEMARRAGE[2:]:  # f5 : journaux du démarrage versés
        assert f"{b}/demarrage/{nom}" in f, nom
    for ligne in f[f"{b}/EMPREINTES-sonde-hote-durable-a1-v3-v9.txt"].decode().splitlines():
        e, nom = ligne.split("  ", 1)
        assert (nom, hashlib.sha256(f[f"{b}/{nom}"]).hexdigest()) == (nom, e)
    assert all(x.encode() not in c for c in f.values() for x in (JETON, CLE_VAST))
    assert gestes(r) == [["detruire", 90000001]]


@pytest.mark.parametrize("modif, motif", [
    ({"CLE_ARGON": "cle-interdite"}, "clé de modèle"), ({"DUREE_MAX_S": "abc"}, "DUREE_MAX_S"),
    ({"DUREE_MAX_S": "7200"}, "DUREE_MAX_S"), ({"GO_ID": "GO-2026-11-04-06"}, "aucun autre GO"),
    ({"PRIX_H_USD": "0.5"}, "prix horaire"),
])
def test_machine_refus_branche_de_refus(monde, modif, motif):
    r, env, nu = monde()
    env.update(modif)
    assert s.MachineSondeV9(r, env, 120).principal() == 0
    j = versees(nu, s.BRANCHE_REFUS)[f"{s.BRANCHE_REFUS}/journal-sonde-a1-v3-v9.log"].decode()
    assert motif in j and "course factice détachée" not in j and "cle-interdite" not in j
    assert versees(nu, s.BRANCHE) == {} and gestes(r) == [["detruire", 90000001]]


def test_machine_etiquette_autre_aucun_geste(monde):
    r, env, nu = monde(etiquette="autre")
    assert s.MachineSondeV9(r, env, 120).principal() == 4 and gestes(r) == []


def test_machine_exception_du_versement_attrapee_puis_arret(monde, monkeypatch):
    r, env, nu = monde()
    m = s.MachineSondeV9(r, env, 120)
    monkeypatch.setattr(m, "verser", lambda *a: (_ for _ in ()).throw(urllib.error.URLError("réseau")))
    assert m.principal() == 0 and gestes(r) == [["detruire", 90000001]]  # m-a : détruite même sans versement, jamais arrêtée
    m2 = s.MachineSondeV9(r, env, 120)
    monkeypatch.setattr(m2, "sceller", lambda: (_ for _ in ()).throw(subprocess.TimeoutExpired("git", 120)))
    m2.nature_fin = "essai"
    assert m2.fin(s.BRANCHE) == 0  # M1(b) : TimeoutExpired dans le scellement, puis destruction


class VastQuiRefuse(h.ClientVastJouet):
    def __init__(self, chemin, refuse_arret=False):
        super().__init__(chemin)
        self.refuse_arret = refuse_arret

    def detruire(self, ident):
        raise urllib.error.URLError("destruction refusée")

    def arreter(self, ident):
        if self.refuse_arret:
            raise h.Refus("arrêt refusé")
        super().arreter(ident)


def test_machine_destruction_refusee_arret_puis_tout_refuse(monde, monkeypatch):
    r, env, nu = monde()
    m = s.MachineSondeV9(r, env, 120)
    monkeypatch.setattr(m, "client_vast", lambda: VastQuiRefuse(r.vast_jouet))
    assert m.principal() == 5 and gestes(r) == []  # m-a : aucun arrêt, la minuterie recommence
    m2 = s.MachineSondeV9(r, env, 120)
    monkeypatch.setattr(m2, "client_vast", lambda: VastQuiRefuse(r.vast_jouet, refuse_arret=True))
    m2.j = h.Journal(r.travail / "j2.log")
    assert m2.se_detruire(True) == 5 and "aucun arrêt" in (r.travail / "j2.log").read_text()
    m3 = s.MachineSondeV9(r, env, 120)
    m3.j = m2.j
    monkeypatch.setattr(m3, "client_vast", lambda: (_ for _ in ()).throw(ValueError("clé vide")))
    assert m3.se_detruire(True) == 4


def test_machine_reprise_et_fuite(monde):
    r, env, nu = monde()
    r.travail.mkdir()
    (r.travail / "ETAT").write_text("course\n")
    assert s.MachineSondeV9(r, env, 120).principal() == 0
    assert f"{s.BRANCHE_INTERROMPUE}/journal-sonde-a1-v3-v9.log" in versees(nu, s.BRANCHE_INTERROMPUE)
    (r.travail / "ETAT").write_text("verse\n")
    assert s.MachineSondeV9(r, env, 120).principal() == 0  # déjà versé : destruction seule


def test_machine_fuite_rien_verse(monde):
    r, env, nu = monde()
    r.travail.mkdir()
    (r.travail / "ETAT").write_text("course\n")
    (r.travail / "fuite.txt").write_text(JETON)
    assert s.MachineSondeV9(r, env, 120).principal() == 0
    assert versees(nu, s.BRANCHE_INTERROMPUE) == {} and gestes(r) == [["detruire", 90000001]]


def test_machine_signe_de_vie_deja_present_la_sonde_continue(monde):
    r, env, nu = monde()
    w = r.travail.parent / "w-vie"
    run("git", "init", "-q", "-b", "x", str(w))
    (w / "a").write_text("a")
    run("git", "add", "-A", cwd=w)
    run("git", "-c", "user.name=j", "-c", "user.email=j@j", "commit", "-q", "-m", "a", cwd=w)
    run("git", "push", "-q", str(nu), f"HEAD:refs/heads/{s.BRANCHE_VIE}", cwd=w)
    assert s.MachineSondeV9(r, env, 120).principal() == 0
    j = versees(nu, s.BRANCHE)[f"{s.BRANCHE}/journal-sonde-a1-v3-v9.log"].decode()
    assert "signe de vie non poussé" in j and "nature de la fin : plafond_de_duree_de_la_sonde" in j



# --- v3 : contre-lecture `contre-lecture-sonde-v2.md` ----------------------------------------------------------------------


def test_louer_echeance_absolue_controles_et_tir(tmp_path):
    vast = h.ClientVastJouet(tmp_path / "vast.json")
    t0 = dt.datetime(2026, 11, 4, 13, 0, tzinfo=dt.timezone.utc)
    assert s.louer(args_louer(tmp_path), vast, JOUR, dict(ENV_PILOTE), t0) == 0
    e = json.loads((tmp_path / "journal-sonde-v9.log.etat.json").read_text())
    assert e["controles_utc"] == ["2026-11-04T13:40:00Z", "2026-11-04T14:10:00Z"]  # M-A
    j = (tmp_path / "journal-sonde-v9.log").read_text()
    assert "controler" in j and "vastai destroy" not in j  # f-b : la ligne d'état renvoie à controler
    vast2 = h.ClientVastJouet(tmp_path / "vast2.json")
    a = args_louer(tmp_path / "x" if (tmp_path / "x").mkdir() is None else tmp_path, tir_minuterie=True)
    assert s.louer(a, vast2, JOUR, dict(ENV_PILOTE), t0) == 0
    e2 = json.loads(Path(a.journal_local + ".etat.json").read_text())
    assert e2["echeance_finale_utc"] == "2026-11-04T13:40:00Z" and e2["tir_minuterie"] is True  # marge courte (m-d)


def test_borne_ecrite_au_pire_cas():
    # f-2 : attente finale du principal (300 s) comptée ; 0,40 USD/h et 30 min dépassent désormais le plafond : refus
    assert s.cout_maximal_usd(0.40, s.DUREE_MAX_S) == pytest.approx(0.40 * 4800 / 3600)
    with pytest.raises(h.Refus, match="plafond"):
        s.verifier_plafond(0.40, s.DUREE_MAX_S)
    assert s.cout_maximal_usd(0.40, 1200) == pytest.approx(0.40 * 4200 / 3600)
    assert s.cout_maximal_usd(0.40, 1200, s.MARGE_TIR_S) == pytest.approx(0.40 * 3300 / 3600)  # commande recommandée


def test_demarrage_echeance_absolue_passee_detruit_aussitot(tmp_path):
    """M-B : machine partie tard ; la minuterie prend l'échéance absolue du pilote, déjà passée, et détruit aussitôt."""
    racine = tmp_path / "racine"
    racine.mkdir()
    bin_ = tmp_path / "bin"
    bin_.mkdir()
    appels = tmp_path / "appels.txt"
    outil(bin_, "curl", f'echo "$@" >> "{appels}"\ncase "$*" in *"-X DELETE"*) printf 200;; '
                        "*) printf '{\"label\": \"sonde-a1-v3-v9\"}';; esac\n")
    env = {"PATH": f"{bin_}:{os.environ['PATH']}", "HOME": str(tmp_path), "RACINE_SONDE": str(racine),
           "API_VAST": "https://vast.invalide/api/v0", "DUREE_MAX_S": "1800", "SONDE_VIE_APRES_S": "1",
           "ECHEANCE_UTC_S": str(int(time.time()) - 10), "DEPOT_URL": str(tmp_path / "absent.git"), "GH_TOKEN": JETON,
           "CONTAINER_ID": "123", "CONTAINER_API_KEY": CLE_VAST, "GIT_CONFIG_GLOBAL": "/dev/null"}
    debut = time.time()
    subprocess.run(["bash", "-c", s.script_de_demarrage("b" * 40)], env=env, capture_output=True, timeout=120)
    t0, ech = (racine / "sonde-v9-minuterie.txt").read_text().split()
    assert int(ech) == int(env["ECHEANCE_UTC_S"]) < int(t0) + 1800
    assert "DELETE instance 123 (essai 1) : HTTP 200" in (racine / "sonde-v9-minuterie.log").read_text()
    assert time.time() - debut < 60


def chemin_sans_curl(tmp_path) -> str:
    d = tmp_path / "bin-sans-curl"
    d.mkdir()
    for outil_ in ("bash", "date", "sleep", "grep", "head", "base64", "setsid", "git", "timeout", "tee", "cat", "python3"):
        cible = subprocess.run(["bash", "-c", f"command -v {outil_}"], capture_output=True, text=True).stdout.strip()
        if cible:
            (d / outil_).symlink_to(cible)
    return str(d)


def test_demarrage_curl_absent_alarme_et_repli_python(tmp_path):
    """m-c : sans curl, la minuterie le dit (ALARME) et appelle l'interface par python3 ; le DELETE est tenté."""
    racine = tmp_path / "racine"
    racine.mkdir()
    env = {"PATH": chemin_sans_curl(tmp_path), "HOME": str(tmp_path), "RACINE_SONDE": str(racine),
           "API_VAST": "https://vast.invalide/api/v0", "DUREE_MAX_S": "1", "SONDE_MARGE_S": "1", "SONDE_VIE_APRES_S": "1",
           "DEPOT_URL": str(tmp_path / "absent.git"), "GH_TOKEN": JETON, "CONTAINER_ID": "123", "CONTAINER_API_KEY": CLE_VAST,
           "GIT_CONFIG_GLOBAL": "/dev/null"}
    subprocess.run(["bash", "-c", s.script_de_demarrage("b" * 40)], env=env, capture_output=True, timeout=180)
    log = (racine / "sonde-v9-minuterie.log").read_text()
    assert "ALARME : curl absent au départ de la minuterie : repli par python3" in log and "DELETE instance 123 (essai 1)" in log
    assert "curl NON" in (racine / "sonde-v9-temps.txt").read_text()


def test_amorce_curl_absent_refus_visible(tmp_path):
    r, racine = amorce(tmp_path, PATH=chemin_sans_curl(tmp_path))
    assert r.returncode == 2 and "curl absent : rien ne part" in r.stdout and not (racine / "exec-atteint.txt").exists()
    r2, _ = amorce(tmp_path / "bis" if (tmp_path / "bis").mkdir() is None else tmp_path, ECHEANCE_UTC_S="demain")
    assert r2.returncode == 2 and "ECHEANCE_UTC_S non entière" in r2.stdout


def unshare_possible() -> bool:
    try:
        return subprocess.run(["unshare", "-pf", "true"], capture_output=True, timeout=10).returncode == 0
    except (OSError, subprocess.TimeoutExpired):
        return False


@pytest.mark.skipif(not unshare_possible(), reason="unshare -pf indisponible")
@pytest.mark.parametrize("reprise", [False, True])
def test_demarrage_dans_un_espace_de_processus_a_part(tmp_path, reprise):
    """m-d et m-b : comme dans un conteneur (la mort du processus de numéro 1 tue tout l'espace), la minuterie détruit sur le
    chemin normal, et aussi à une reprise survenue après l'échéance et la fin de vie (le principal attend la minuterie)."""
    racine = tmp_path / "racine"
    racine.mkdir()
    if reprise:
        passe = int(time.time()) - 3600
        (racine / "sonde-v9-minuterie.txt").write_text(f"{passe - 100} {passe}\n")
    bin_ = tmp_path / "bin"
    bin_.mkdir()
    outil(bin_, "curl", 'sleep 2\ncase "$*" in *"-X DELETE"*) printf 200;; *) printf \'{"label": "sonde-a1-v3-v9"}\';; esac\n')
    env = {"PATH": f"{bin_}:{os.environ['PATH']}", "HOME": str(tmp_path), "RACINE_SONDE": str(racine),
           "API_VAST": "https://vast.invalide/api/v0", "DUREE_MAX_S": "1", "SONDE_MARGE_S": "1", "SONDE_VIE_APRES_S": "1",
           "DEPOT_URL": str(tmp_path / "absent.git"), "GH_TOKEN": JETON, "CONTAINER_ID": "123", "CONTAINER_API_KEY": CLE_VAST,
           "GIT_CONFIG_GLOBAL": "/dev/null"}
    r = subprocess.run(["unshare", "-pf", "bash", "-c", s.script_de_demarrage("b" * 40)], env=env, capture_output=True,
                       timeout=180)
    log = (racine / "sonde-v9-minuterie.log").read_text()  # lu après la fin de tout l'espace de processus
    assert "DELETE instance 123 (essai 1) : HTTP 200" in log, log
    assert "fin du principal" in (racine / "sonde-v9-temps.txt").read_text()


def test_machine_tir_de_la_minuterie_aucun_geste(monde):
    r, env, nu = monde()
    env["TIR_MINUTERIE"] = "1"
    assert s.MachineSondeV9(r, env, 120).principal() == 5
    assert gestes(r) == [] and f"{s.BRANCHE}/journal-sonde-a1-v3-v9.log" in versees(nu, s.BRANCHE)


@pytest.mark.parametrize("valeur, motif", [(None, "ECHEANCE_UTC_S"), ("demain", "ECHEANCE_UTC_S"),
                                           ("proche", "trop proche")])
def test_machine_echeance_absolue_absente_ou_trop_proche(monde, valeur, motif):
    r, env, nu = monde()
    if valeur is None:
        env.pop("ECHEANCE_UTC_S")
    elif valeur == "proche":
        env["ECHEANCE_UTC_S"] = str(int(time.time()) + 200)
    else:
        env["ECHEANCE_UTC_S"] = valeur
    assert s.MachineSondeV9(r, env, 120).principal() == 0
    j = versees(nu, s.BRANCHE_REFUS)[f"{s.BRANCHE_REFUS}/journal-sonde-a1-v3-v9.log"].decode()
    assert motif in j and "course factice détachée" not in j


def test_machine_echeance_absolue_raccourcit_la_course(monde):
    r, env, nu = monde(depuis_s=0)
    env["ECHEANCE_UTC_S"] = str(int(time.time()) + 362)  # 300 s de réserve au versement : 62 s utiles au plus
    m = s.MachineSondeV9(r, env, 120)
    assert m.principal() == 0 and m.r.duree_max_s <= 62.5


def test_client_pilote_n_ecrit_que_le_code(tmp_path):
    c, _ = client_factice(tmp_path, "ligne de sortie avec un identifiant d'une autre instance 999", 7)
    with pytest.raises(h.Refus) as e:
        c.instances()
    assert str(e.value) == "vastai show instances : code 7"  # f-a



# --- v4 : contre-lecture `contre-lecture-sonde-v3.md` (M-1, m-1, m-2, f-1, f-2, f-3, f-6) -------------------------------------


def test_delai_depasse_de_vastai_sans_jeton_et_marqueur(tmp_path, monkeypatch):
    """M-1 : faux `vastai` lent (démonstration du contre-lecteur) ; le délai donne un Refus sans ligne de commande ni jeton, et
    la création est marquée incertaine ; cas sain : le même outil, rapide, répond."""
    monkeypatch.setattr(s, "DELAI_VASTAI_S", 1)
    lent = outil(tmp_path, "vastai-lent", 'sleep 5\necho \'{"success": true, "new_contract": 1}\'\n')
    env = {"PATH": os.environ["PATH"], "HOME": str(tmp_path), "VAST_API_KEY": CLE_COMPTE, "GH_TOKEN": JETON}
    with pytest.raises(h.Refus) as e:
        s.ClientPilote(env, str(lent)).creer(11, s.corps("a" * 40, OFFRE, 1200, JETON, 1_800_000_000))
    assert str(e.value) == "vastai create instance : délai dépassé (1 s)" and e.value.__cause__ is None
    assert s.louer(args_louer(tmp_path), s.ClientPilote(env, str(lent)), JOUR, dict(ENV_PILOTE)) == 2
    marque = tmp_path / "journal-sonde-v9.log.creation-incertaine"
    assert marque.exists() and JETON not in marque.read_text() + (tmp_path / "journal-sonde-v9.log").read_text()
    rapide = outil(tmp_path, "vastai-rapide", 'echo \'{"success": true, "new_contract": 77}\'\n')
    assert s.ClientPilote(env, str(rapide)).creer(11, s.corps("a" * 40, OFFRE, 1200, JETON, 1_800_000_000)) == 77


def test_code_non_nul_de_create_marque_et_bloque_mais_pas_un_refus_avant_l_appel(tmp_path):
    """m-1 : un code non nul de `vastai create` marque la création incertaine ; un refus d'une garde avant l'appel, non."""
    c, _ = client_factice(tmp_path, "{}", 1)
    assert s.louer(args_louer(tmp_path), c, JOUR, dict(ENV_PILOTE)) == 2
    assert (tmp_path / "journal-sonde-v9.log.creation-incertaine").exists()
    c2, _ = client_factice(tmp_path, '{"success": true, "new_contract": 5}')
    assert s.louer(args_louer(tmp_path), c2, JOUR, dict(ENV_PILOTE)) == 2  # tant que le marqueur existe
    d = tmp_path / "avant"
    d.mkdir()

    class GardeAvantAppel:
        def creer(self, offre_id, corps):
            raise s.RefusAvantAppel("valeur d'environnement avec espace ou guillemet : refus (forme -e K=V)")
    assert s.louer(args_louer(d), GardeAvantAppel(), JOUR, dict(ENV_PILOTE)) == 2
    assert not (d / "journal-sonde-v9.log.creation-incertaine").exists()


def test_tir_premier_controle_a_t0_plus_45(tmp_path):
    """f-3 : en tir, l'échéance est T0 + 40 ; le premier contrôle vient après (T0 + 45)."""
    vast = h.ClientVastJouet(tmp_path / "vast.json")
    t0 = dt.datetime(2026, 11, 4, 13, 0, tzinfo=dt.timezone.utc)
    assert s.louer(args_louer(tmp_path, tir_minuterie=True), vast, JOUR, dict(ENV_PILOTE), t0) == 0
    e = json.loads((tmp_path / "journal-sonde-v9.log.etat.json").read_text())
    assert e["echeance_finale_utc"] == "2026-11-04T13:40:00Z"
    assert e["controles_utc"] == ["2026-11-04T13:45:00Z", "2026-11-04T14:10:00Z"]


class VastLent:
    def instances(self):
        raise subprocess.TimeoutExpired(["vastai", "show", "instances", "--raw"], 300)


def test_controler_delai_depasse_code_6(tmp_path):
    """f-6 : un délai dépassé de `show instances` (ou de `ls-remote`) rend le code 6, écrit, sans trace ; cas sain : code 5."""
    assert s.controler(etat_pilote(tmp_path), VastLent(), lambda: True, heure(13, 40), {}) == 6
    assert "DÉLAI DÉPASSÉ : vastai" in (tmp_path / "controle.log").read_text()
    v = VastFactice([{"id": 4321, "label": "sonde-a1-v3-v9"}])

    def ls_remote_lent():
        raise subprocess.TimeoutExpired(["git", "ls-remote"], 120)
    assert s.controler(etat_pilote(tmp_path), v, ls_remote_lent, heure(13, 40), {}) == 6
    assert s.controler(etat_pilote(tmp_path), v, lambda: True, heure(13, 40), {}) == 5


def test_curl_installe_apres_la_minuterie_et_tout_apt_get_borne():
    """f-1 et m-2, sur le texte du script : la minuterie part avant toute installation ; chaque `apt-get` et l'amorce sont sous
    `timeout` borné par la fin de vie (artefact : la v3 installait `curl` avant la minuterie, sans `timeout`)."""
    t = s.script_de_demarrage("a" * 40)
    assert t.index("setsid bash") < t.index("apt-get")
    for ligne in t.splitlines():
        if "apt-get" in ligne:
            assert "timeout -k 5" in ligne and "borne 120" in ligne, ligne
    assert 'timeout -k 10 "$(reste)" bash' in t
    from controle_ia import sonde_hote_durable_a1_v3_v3 as v3
    t3 = v3.script_de_demarrage("a" * 40)
    assert t3.index("apt-get") < t3.index("setsid bash")  # le défaut corrigé, toujours présent dans la v3 (R12)


@pytest.mark.skipif(not unshare_possible(), reason="unshare -pf indisponible")
def test_amorce_bloquee_et_destructions_refusees_conteneur_borne(tmp_path):
    """m-2 sous `unshare -pf` (démonstration du contre-lecteur) : l'amorce se bloque et chaque DELETE est refusé ; le conteneur
    sort quand même peu après sa fin de vie (artefact de la v3 : il ne sortait jamais)."""
    nu, commit = depot_avec_amorce(tmp_path, "sleep 3600\n")
    racine = tmp_path / "racine"
    racine.mkdir()
    bin_ = tmp_path / "bin"
    bin_.mkdir()
    outil(bin_, "curl", 'case "$*" in *"-X DELETE"*) printf 403;; *) printf \'{"label": "sonde-a1-v3-v9"}\';; esac\n')
    env = {"PATH": f"{bin_}:{os.environ['PATH']}", "HOME": str(tmp_path), "RACINE_SONDE": str(racine),
           "API_VAST": "https://vast.invalide/api/v0", "DUREE_MAX_S": "5", "SONDE_MARGE_S": "5", "SONDE_VIE_APRES_S": "5",
           "DEPOT_URL": str(nu), "GH_TOKEN": JETON, "CONTAINER_ID": "123", "CONTAINER_API_KEY": CLE_VAST,
           "GIT_CONFIG_GLOBAL": "/dev/null"}
    debut = time.time()
    r = subprocess.run(["unshare", "-pf", "bash", "-c", s.script_de_demarrage(commit)], env=env, capture_output=True,
                       timeout=200)
    duree = time.time() - debut
    log = (racine / "sonde-v9-minuterie.log").read_text()
    assert "HTTP 403" in log and "ALARME : destruction non obtenue" in log
    temps = (racine / "sonde-v9-temps.txt").read_text()
    assert "amorce finie" in temps and "fin du principal" in temps
    assert duree < 15 + 60 + 30, duree  # fin de vie (15 s) + attente de la minuterie + tolérance



# --- v5 remplacé en v9 : les offres sans carte sont des volumes ; la sonde loue une machine à une carte ---------------------
# (fait établi par la fille, 5 novembre 2026, 00:15 et 00:16 UTC : `num_gpus=0` ⇒ `resource_type` « disk »)

GPU_OK = dict(OFFRE, id=21, resource_type="gpu", num_gpus=1, gpu_name="GTX_1070", cpu_cores_effective=14, cpu_ram=8007,
              dph_total=0.055)
VOLUME = dict(OFFRE, id=31, resource_type="disk", num_gpus=0, cpu_ram=0, dph_total=0.01)


def test_offre_gpu_conforme_cas_sain():
    v = s.verifier_offre_sonde([GPU_OK], 21)
    assert v["resource_type"] == "gpu" and v["num_gpus"] == 1 and v["cpu_ram"] == 8007 and v["memoire_non_renseignee"] is False
    assert v["dph_total"] == 0.055 and v["gpu_name"] == "GTX_1070"


@pytest.mark.parametrize("modif, motif", [
    ({"resource_type": "disk", "num_gpus": 0}, "resource_type « disk » : volume de stockage"),
    ({"resource_type": None}, "« gpu » exigé"), ({"resource_type": "cpu"}, "« gpu » exigé"),
    ({"num_gpus": 2}, "2 carte(s) ; une exigée"), ({"num_gpus": 0}, "0 carte(s) ; une exigée"),
    ({"num_gpus": True}, "carte(s) ; une exigée"),
    ({"cpu_ram": 0}, "cpu_ram = 0 < 8000"),          # l'exception « non renseignée » de la v5 est retirée
    ({"cpu_ram": None}, "cpu_ram = None < 8000"), ({"cpu_ram": 4000}, "cpu_ram = 4000 < 8000"),
    ({"cpu_cores_effective": 2}, "cpu_cores_effective = 2 < 4"),
    ({"disk_space": 20}, "disk_space"), ({"reliability": 0.9}, "reliability"), ({"dph_total": 0.41}, "prix horaire"),
])
def test_offre_artefacts_v9(modif, motif):
    with pytest.raises(h.Refus, match=re_echappe(motif)):
        s.verifier_offre_sonde([dict(GPU_OK, **modif)], 21)


def re_echappe(t):
    import re
    return re.escape(t)


def test_la_moins_chere_ignore_les_volumes(tmp_path, capsys):
    f = tmp_path / "offres.json"
    f.write_text(json.dumps([GPU_OK, VOLUME, dict(GPU_OK, id=22, num_gpus=2, dph_total=0.02)]))
    assert s.principal(["offre", "--offres", str(f)]) == 0 and capsys.readouterr().out.strip() == "21"
    with pytest.raises(h.Refus, match="volume de stockage"):
        s.offre_la_moins_chere_sonde(json.loads(f.read_text()), 31)
    f.write_text(json.dumps([VOLUME]))
    assert s.principal(["offre", "--offres", str(f)]) == 2


def test_go_v9_cas_sain_et_artefacts(tmp_path):
    reg = tmp_path / "go-v9.md"
    reg.write_text("# R\n\n" + ENTETE + LIGNE_06 + LIGNE_09_ANCIEN + LIGNE_09)
    assert s.verifier_go_sonde(reg, GARDE, "GO-2026-11-05-01", JOUR)["plafond_usd"] == 1
    assert s.verifier_go_sonde(RACINE / "registres" / "go.md", GARDE, "GO-2026-11-05-01", JOUR)["echeance"] == "2026-11-06"
    for go in ("GO-2026-11-04-09", "GO-2026-11-04-06"):
        with pytest.raises(h.Refus, match="ne part que sous GO-2026-11-05-01"):
            s.verifier_go_sonde(reg, GARDE, go, JOUR)
    reg.write_text("# R\n\n" + ENTETE + LIGNE_09.replace("| 1 USD |", "| 2 USD |"))
    with pytest.raises(h.Refus, match="exactement 1 USD"):
        s.verifier_go_sonde(reg, GARDE, "GO-2026-11-05-01", JOUR)
    reg.write_text("# R\n\n" + ENTETE + LIGNE_09)
    with pytest.raises(h.Refus, match="hors de sa période"):
        s.verifier_go_sonde(reg, GARDE, "GO-2026-11-05-01", dt.date(2026, 11, 7))


def test_louer_refuse_le_go_09(tmp_path):
    vast = h.ClientVastJouet(tmp_path / "vast.json")
    env = dict(ENV_PILOTE, GO_ID="GO-2026-11-04-09")
    assert s.louer(args_louer(tmp_path, go="GO-2026-11-04-09"), vast, JOUR, env) == 2 and vast.instances() == []


def test_machine_refuse_le_go_09(monde):
    r, env, nu = monde()
    env["GO_ID"] = "GO-2026-11-04-09"
    assert s.MachineSondeV9(r, env, 120).principal() == 0
    j = versees(nu, s.BRANCHE_REFUS)[f"{s.BRANCHE_REFUS}/journal-sonde-a1-v3-v9.log"].decode()
    assert "ne part que sous GO-2026-11-05-01" in j and "course factice détachée" not in j


def meminfo(tmp_path, ko):
    p = tmp_path / f"meminfo-{ko}"
    p.write_text(f"MemTotal:       {ko} kB\nMemFree:        1000 kB\n" if ko is not None else "rien\n")
    return str(p)


@pytest.mark.parametrize("ko, code, motif", [
    (16384000, 0, "mémoire réelle 16384000 kB"),
    (2097152, 0, "mémoire réelle 2097152 kB"),
    (1048576, 2, "mémoire réelle 1048576 kB < 2 Go : rien ne part"),
    (None, 2, "mémoire réelle illisible"),
])
def test_amorce_memoire_reelle(tmp_path, ko, code, motif):
    r, racine = amorce(tmp_path, SONDE_MEMINFO=meminfo(tmp_path, ko))
    assert r.returncode == code and motif in r.stdout, r.stdout
    assert (racine / "exec-atteint.txt").exists() == (code == 0)
    releve = (racine / "sonde-v9-memoire.txt").read_text()
    assert ("MemTotal illisible" in releve) if ko is None else (f"MemTotal {ko} kB" in releve)


def test_memoire_reelle_versee_avec_la_sortie(monde):
    r, env, nu = monde()
    assert s.MachineSondeV9(r, env, 120).principal() == 0
    f = versees(nu, s.BRANCHE)
    assert b"MemTotal 16384000 kB" in f[f"{s.BRANCHE}/demarrage/sonde-v9-memoire.txt"]



# --- v6 : mandataire qui réémet les certificats (fait constaté par la fille, 4 novembre 2026, 22:48 et 22:51 UTC) -----------

MANDATAIRE = {"HTTPS_PROXY": "http://utilisateur:motdepasse-mandataire@mandataire.invalide:3128",
              "HTTP_PROXY": "http://utilisateur:motdepasse-mandataire@mandataire.invalide:3128",
              "NO_PROXY": "localhost,127.0.0.1", "SSL_CERT_FILE": "/chemin/jouet/ca-mandataire.crt",
              "REQUESTS_CA_BUNDLE": "/chemin/jouet/ca-mandataire.crt"}


def vastai_qui_note_son_environnement(tmp_path, stderr="", code=0, sortie='{"success": true, "new_contract": 31}'):
    note = tmp_path / "env-vu-par-vastai.txt"
    o = outil(tmp_path, "vastai-env", f'env | cut -d= -f1 | sort > "{note}"\nenv | grep -E "^(HTTPS_PROXY|SSL_CERT_FILE)=" '
                                      f'>> "{note}.valeurs"\nprintf \'%s\\n\' \'{stderr}\' >&2\necho \'{sortie}\'\nexit {code}\n')
    return o, note


def test_mandataire_transmis_quand_present(tmp_path):
    """(a) cas sain : les cinq variables du mandataire, présentes, sont transmises à `vastai` ; aucune autre (l'artefact
    `AUTRE_VARIABLE` ne passe pas)."""
    o, note = vastai_qui_note_son_environnement(tmp_path)
    env = {"PATH": os.environ["PATH"], "HOME": str(tmp_path), "VAST_API_KEY": CLE_COMPTE, "GH_TOKEN": JETON,
           "AUTRE_VARIABLE": "x", **MANDATAIRE}
    assert s.ClientPilote(env, str(o)).creer(11, s.corps("a" * 40, OFFRE, 1200, JETON, 1_800_000_000)) == 31
    vus = set(note.read_text().split())
    assert set(MANDATAIRE) <= vus and "AUTRE_VARIABLE" not in vus and "GH_TOKEN" not in vus
    assert vus <= {"PATH", "HOME", "LANG", "VAST_API_KEY", "PWD", "SHLVL", "_", "OLDPWD"} | set(MANDATAIRE)
    assert MANDATAIRE["HTTPS_PROXY"] in Path(str(note) + ".valeurs").read_text()


def test_mandataire_absent_rien_n_est_invente(tmp_path):
    """(a) artefact : sans variables du mandataire (ou vides), aucune n'est transmise."""
    o, note = vastai_qui_note_son_environnement(tmp_path)
    env = {"PATH": os.environ["PATH"], "HOME": str(tmp_path), "VAST_API_KEY": CLE_COMPTE, "HTTPS_PROXY": ""}
    assert s.ClientPilote(env, str(o)).creer(11, s.corps("a" * 40, OFFRE, 1200, JETON, 1_800_000_000)) == 31
    assert not (set(MANDATAIRE) & set(note.read_text().split()))


def test_valeurs_du_mandataire_masquees_au_journal(tmp_path):
    vast = h.ClientVastJouet(tmp_path / "vast.json")
    env = dict(ENV_PILOTE, **MANDATAIRE)
    a = args_louer(tmp_path)
    a.commit_prive = "a" * 40
    assert s.louer(a, vast, JOUR, env) == 0
    j = (tmp_path / "journal-sonde-v9.log").read_text()
    assert "motdepasse-mandataire" not in j and JETON not in j


@pytest.mark.parametrize("stderr", [
    "ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] self-signed certificate in certificate chain",
    "requests.exceptions.SSLError: CERTIFICATE_VERIFY_FAILED",
    "SSLCertVerificationError ghp_jouet_secret_dans_l_erreur",
])
def test_erreur_de_certificat_aucun_marqueur(tmp_path, stderr):
    """(b) : échec de certificat : refus « appel non parvenu à Vast (certificat) », aucun marqueur, sortie d'erreur jamais
    écrite ; une location reste possible ensuite."""
    o, _ = vastai_qui_note_son_environnement(tmp_path, stderr=stderr, code=1, sortie="")
    env = dict(ENV_PILOTE, PATH=os.environ["PATH"], HOME=str(tmp_path))
    c = s.ClientPilote(env, str(o))
    with pytest.raises(s.RefusCertificat, match=r"appel non parvenu à Vast \(certificat\) ; code 1"):
        c.creer(11, s.corps("a" * 40, OFFRE, 1200, JETON, 1_800_000_000))
    assert s.louer(args_louer(tmp_path), c, JOUR, env) == 2
    assert not (tmp_path / "journal-sonde-v9.log.creation-incertaine").exists()
    j = (tmp_path / "journal-sonde-v9.log").read_text()
    assert "appel non parvenu à Vast (certificat)" in j and "self-signed" not in j and "ghp_jouet_secret" not in j
    assert "SSL" not in j.replace("SSLCertVerificationError", "")  # rien de la sortie d'erreur
    o2, _ = vastai_qui_note_son_environnement(tmp_path, sortie='{"success": true, "new_contract": 32}')
    assert s.louer(args_louer(tmp_path), s.ClientPilote(env, str(o2)), JOUR, env) == 0  # aucun marqueur : location possible


@pytest.mark.parametrize("stderr", ["HTTP 500 : erreur interne", "", "certificat mentionné en français seulement"])
def test_autre_erreur_marqueur_pose(tmp_path, stderr):
    """(b) artefact : toute autre erreur après l'appel garde le marqueur de création incertaine (m-1)."""
    o, _ = vastai_qui_note_son_environnement(tmp_path, stderr=stderr, code=1, sortie="")
    env = dict(ENV_PILOTE, PATH=os.environ["PATH"], HOME=str(tmp_path))
    assert s.louer(args_louer(tmp_path), s.ClientPilote(env, str(o)), JOUR, env) == 2
    assert (tmp_path / "journal-sonde-v9.log.creation-incertaine").exists()
    assert stderr not in (tmp_path / "journal-sonde-v9.log").read_text() or stderr == ""



# --- v7 : réponse de création catégorisée, ls-remote sous mandataire (faits de la fille, 4 novembre 2026, 23:09 et 23:11) ---

SECRETS_V7 = [JETON, CLE_COMPTE, "motdepasse-mandataire"]


@pytest.mark.parametrize("texte, categorie, detail_attendu", [
    ('{"success": true, "new_contract": 4242}', "contrat", "4242"),
    ('{\n "success": true,\n "new_contract": 4243\n}', "contrat", "4243"),
    ("journal\n{'success': True, 'new_contract': 4244}", "contrat", "4244"),
    ("{'success': False, 'error': 'no_such_ask', 'msg': 'Instance type 123 is no longer available.'}", "no_such_ask",
     "no longer available"),
    ('{"success": false, "error": "invalid_args", "msg": "disk too large"}', "erreur Vast", "disk too large"),
    ("{'success': False, 'error': 'insufficient_credit', 'msg': 'Your balance is too low'}", "erreur Vast", "balance"),
    ('{"error": "bizarre", "msg": "sans success"}', "erreur Vast sans success faux", "sans success"),
    ("texte libre sans dictionnaire", "illisible", "longueur 29"),
    ("", "illisible", "longueur 0"),
])
def test_categories_de_la_reponse(texte, categorie, detail_attendu):
    cat, detail = s.categoriser_reponse(texte, SECRETS_V7)
    assert cat == categorie and detail_attendu in detail


def test_categorie_masquee_et_tronquee():
    long = "x" * 500
    texte = ("{'success': False, 'error': 'invalid_args', 'msg': 'jeton " + JETON + " et mandataire motdepasse-mandataire "
             + long + "', 'extra_env': 'GH_TOKEN=" + JETON + "'}")
    cat, detail = s.categoriser_reponse(texte, SECRETS_V7)
    assert cat == "erreur Vast" and JETON not in detail and "motdepasse-mandataire" not in detail
    assert "extra_env" not in detail and len(detail) < 2 * 200 + 40  # seuls error et msg, tronqués à 200
    illisible = s.categoriser_reponse("GH_TOKEN=" + JETON + " sans structure", SECRETS_V7)
    assert illisible == ("illisible", f"longueur {len('GH_TOKEN=' + JETON + ' sans structure')}")


def louer_avec_reponse(tmp_path, sortie):
    o = outil(tmp_path, "vastai-v7", "cat <<'FIN'\n" + sortie + "\nFIN\n")
    env = dict(ENV_PILOTE, PATH=os.environ["PATH"], HOME=str(tmp_path))
    return s.louer(args_louer(tmp_path), s.ClientPilote(env, str(o)), JOUR, env)


@pytest.mark.parametrize("sortie, code, marqueur, au_journal", [
    ('{"success": true, "new_contract": 5151}', 0, False, "réponse de création : contrat 5151"),
    ("{'success': False, 'error': 'no_such_ask', 'msg': 'Instance type 12 is no longer available.'}", 2, False,
     "no_such_ask"),
    ('{"success": false, "error": "invalid_args", "msg": "bad image"}', 2, False, "erreur Vast ; error='invalid_args'"),
    ('{"error": "bizarre"}', 2, True, "erreur Vast sans success faux"),
    ("réponse que personne ne sait lire", 2, True, "illisible (sortie standard"),  # v8 : longueurs des deux flux
])
def test_louer_catégorie_et_marqueur(tmp_path, sortie, code, marqueur, au_journal):
    """Cas sain (contrat) et un artefact par catégorie : seuls no_such_ask et erreur Vast avec success faux évitent le
    marqueur ; les autres le posent ; la réponse brute n'est jamais écrite hors de ses champs sûrs."""
    assert louer_avec_reponse(tmp_path, sortie) == code
    assert (tmp_path / "journal-sonde-v9.log.creation-incertaine").exists() == marqueur
    j = (tmp_path / "journal-sonde-v9.log").read_text()
    assert au_journal in j and JETON not in j
    if "personne" in sortie:
        assert "personne" not in j


def test_longueurs_de_la_commande_ecrites(tmp_path):
    assert louer_avec_reponse(tmp_path, '{"success": true, "new_contract": 6}') == 0
    j = (tmp_path / "journal-sonde-v9.log").read_text()
    c = s.corps("a" * 40, dict(OFFRE, id=12, dph_total=0.09), 1200, JETON, 1)
    lg = s.longueurs_de_creation(12, c)
    assert f"--args {lg['args_c']}, --env " in j and ", commande " in j and lg["args_c"] == len(c["script"])  # v8 : longueurs écrites à chaque essai


def faux_git(tmp_path, code=0, sortie=""):
    note = tmp_path / "env-vu-par-git.txt"
    o = outil(tmp_path, "git-faux", f'env | cut -d= -f1 | sort > "{note}"\nprintf "%s" "{sortie}"\nexit {code}\n')
    return str(o), note


def test_ls_remote_sous_mandataire_cas_sain_et_echecs(tmp_path):
    env = {"PATH": os.environ["PATH"], "HOME": str(tmp_path), "GH_TOKEN": JETON, **MANDATAIRE, "AUTRE": "x"}
    o, note = faux_git(tmp_path, 0, "abc123\\trefs/heads/x")
    assert s.branche_existe(s.BRANCHE_VIE, env, o) is True
    vus = set(note.read_text().split())
    assert set(MANDATAIRE) <= vus and "AUTRE" not in vus
    o2, _ = faux_git(tmp_path, 0, "")
    assert s.branche_existe(s.BRANCHE_VIE, env, o2) is False  # ls-remote réussi, branche absente : vrai « pas de vie »
    o3, _ = faux_git(tmp_path, 128, "")
    with pytest.raises(s.RefusRecontroler, match="code 128"):
        s.branche_existe(s.BRANCHE_VIE, env, o3)
    with pytest.raises(s.RefusRecontroler, match="FileNotFoundError"):
        s.branche_existe(s.BRANCHE_VIE, env, str(tmp_path / "git-absent"))


def test_controler_echec_de_ls_remote_code_6_jamais_destruction(tmp_path):
    v = VastFactice([{"id": 4321, "label": "sonde-a1-v3-v9"}])

    def echec():
        raise s.RefusRecontroler("ls-remote : code 128")
    assert s.controler(etat_pilote(tmp_path), v, echec, heure(13, 35), {}) == 6 and v.gestes == []
    assert "RECONTRÔLER : ls-remote : code 128" in (tmp_path / "controle.log").read_text()
    assert s.controler(etat_pilote(tmp_path), v, lambda: False, heure(13, 35), {}) == 1  # vrai « pas de vie » : détruite



# --- v8 : refus sur la sortie d'erreur avec le code 0, et nouvel essai sur « no_such_ask » (fille, 23:35 et 23:38 UTC) -------

FORME_DE_LA_FILLE = ("{'success': False?, 'error': True, 'msg': 'error 404/3603: no_such_ask  Instance type by id 1 is not "
                     "available.'}")


def vastai_deux_flux(tmp_path, nom, stdout="", stderr="", code=0):
    o = outil(tmp_path, nom, f"cat <<'FIN1'\n{stdout}\nFIN1\ncat >&2 <<'FIN2'\n{stderr}\nFIN2\nexit {code}\n")
    env = {"PATH": os.environ["PATH"], "HOME": str(tmp_path), "VAST_API_KEY": CLE_COMPTE, "GH_TOKEN": JETON}
    return s.ClientPilote(env, str(o))


def corps_v8():
    return s.corps("a" * 40, OFFRE, 1200, JETON, 1_800_000_000)


def test_contrat_sur_la_sortie_standard(tmp_path):
    assert vastai_deux_flux(tmp_path, "v1", stdout='{"success": true, "new_contract": 808}', stderr="avertissement").creer(
        11, corps_v8()) == 808


@pytest.mark.parametrize("stdout, stderr, code, classe, motif", [
    ("", FORME_DE_LA_FILLE, 0, "RefusNoSuchAsk", "no_such_ask"),                       # refus sur stderr, code 0
    ("", "{'success': False, 'error': 'no_such_ask', 'msg': 'gone'}", 0, "RefusNoSuchAsk", "sortie d'erreur, code 0"),
    ('{"success": false, "error": "invalid_args", "msg": "bad"}', "", 0, "RefusVastSansCreation", "invalid_args"),
    ("", "{'success': False, 'error': 'insufficient_credit', 'msg': 'balance " + JETON + "'}", 1, "RefusVastSansCreation",
     "insufficient_credit"),
    ("", "", 0, "Refus", "illisible (sortie standard 1 caractères, sortie d'erreur 1, code 0)"),  # deux flux vides
])
def test_categorie_des_deux_flux(tmp_path, stdout, stderr, code, classe, motif):
    c = vastai_deux_flux(tmp_path, "v2", stdout, stderr, code)
    with pytest.raises(h.Refus) as e:
        c.creer(11, corps_v8())
    assert type(e.value).__name__ == classe and motif in str(e.value), str(e.value)
    assert JETON not in str(e.value) and CLE_COMPTE not in str(e.value)
    if classe == "RefusNoSuchAsk":
        assert isinstance(e.value, s.RefusVastSansCreation)
    if classe == "RefusVastSansCreation":
        assert not isinstance(e.value, s.RefusNoSuchAsk)


def test_motif_mal_forme_de_la_fille():
    cat, detail = s.categoriser_reponse(FORME_DE_LA_FILLE, SECRETS_V7)
    assert cat == "no_such_ask" and "Instance type by id 1" in detail and "error='True'" in detail


OFFRES_V8 = [dict(OFFRE, id=100 + k, dph_total=round(0.05 + 0.01 * k, 2)) for k in range(7)]


def vastai_compteur(tmp_path, reponses):
    """Faux `vastai` : la n-ième création rend la n-ième réponse (stdout, stderr) ; le compte des appels est gardé."""
    d = tmp_path / "reponses"
    d.mkdir(exist_ok=True)
    for n, (so, se) in enumerate(reponses, 1):
        (d / f"{n}.out").write_text(so)
        (d / f"{n}.err").write_text(se)
    compte = tmp_path / "compte"
    o = outil(tmp_path, "vastai-compteur",
              f'n=$(( $(cat "{compte}" 2>/dev/null || echo 0) + 1 )); echo $n > "{compte}"; echo "$3" >> "{compte}.offres"\n'
              f'[ -f "{d}/$n.out" ] || n=$(ls "{d}" | grep -c out)\ncat "{d}/$n.out"; cat "{d}/$n.err" >&2; exit 0\n')
    env = dict(ENV_PILOTE, PATH=os.environ["PATH"], HOME=str(tmp_path))
    return s.ClientPilote(env, str(o)), compte, env


def louer_v8(tmp_path, client, env, offres=None, offre="100", **kw):
    a = args_louer(tmp_path, **kw)
    Path(a.offres).write_text(json.dumps(offres if offres is not None else OFFRES_V8))
    a.offre = offre
    return s.louer(a, client, JOUR, env)


NSA = ("", "{'success': False, 'error': True, 'msg': 'error 404/3603: no_such_ask  Instance type is not available.'}")


def test_no_such_ask_puis_contrat_au_deuxieme_essai(tmp_path):
    c, compte, env = vastai_compteur(tmp_path, [NSA, ('{"success": true, "new_contract": 909}', "")])
    assert louer_v8(tmp_path, c, env) == 0
    assert Path(str(compte) + ".offres").read_text().split() == ["100", "101"]  # par prix croissant
    j = (tmp_path / "journal-sonde-v9.log").read_text()
    assert "essai 1/5 : offre 100" in j and "essai 1 refusé" in j and "contrat 909 (essai 2)" in j
    e = json.loads((tmp_path / "journal-sonde-v9.log.etat.json").read_text())
    assert e["identifiant"] == 909 and e["prix_h_usd"] == 0.06
    assert not (tmp_path / "journal-sonde-v9.log.creation-incertaine").exists()


def test_cinq_no_such_ask_refus_final_sans_marqueur(tmp_path):
    c, compte, env = vastai_compteur(tmp_path, [NSA] * 7)
    assert louer_v8(tmp_path, c, env) == 2
    assert compte.read_text().strip().splitlines()[0] == "5"
    assert Path(str(compte) + ".offres").read_text().split() == ["100", "101", "102", "103", "104"]
    j = (tmp_path / "journal-sonde-v9.log").read_text()
    assert "5 essai(s), tous « no_such_ask » : refus final" in j and "essai 5/5" in j
    assert not (tmp_path / "journal-sonde-v9.log.creation-incertaine").exists()


def test_moins_d_offres_conformes_que_cinq(tmp_path):
    offres = [OFFRES_V8[0], OFFRES_V8[1], dict(OFFRE, id=150, num_gpus=2, dph_total=0.01)]  # la carte n'est jamais essayée
    c, compte, env = vastai_compteur(tmp_path, [NSA] * 3)
    assert louer_v8(tmp_path, c, env, offres) == 2
    assert Path(str(compte) + ".offres").read_text().split() == ["100", "101"]
    assert "2 essai(s), tous « no_such_ask »" in (tmp_path / "journal-sonde-v9.log").read_text()


@pytest.mark.parametrize("reponse, marqueur", [
    (('{"success": false, "error": "invalid_args", "msg": "bad image"}', ""), False),  # erreur Vast : arrêt, sans marqueur
    (("", ""), True),                                                                  # illisible : arrêt, marqueur
])
def test_autre_erreur_ne_relance_pas(tmp_path, reponse, marqueur):
    c, compte, env = vastai_compteur(tmp_path, [reponse, ('{"success": true, "new_contract": 1}', "")])
    assert louer_v8(tmp_path, c, env) == 2
    assert compte.read_text().strip().splitlines()[0] == "1"
    assert (tmp_path / "journal-sonde-v9.log.creation-incertaine").exists() == marqueur


def test_garde_de_depense_recalculee_a_chaque_essai(tmp_path):
    """Mode normal, 1 800 s : 0,09 USD/h passe la garde ; 0,39 USD/h (conforme à l'offre) la dépasse : arrêt avant l'appel."""
    offres = [dict(OFFRE, id=100, dph_total=0.09), dict(OFFRE, id=101, dph_total=0.39)]
    c, compte, env = vastai_compteur(tmp_path, [NSA, ('{"success": true, "new_contract": 2}', "")])
    assert louer_v8(tmp_path, c, env, offres, duree_s="1800") == 2
    assert Path(str(compte) + ".offres").read_text().split() == ["100"]  # le second essai n'a pas été appelé
    j = (tmp_path / "journal-sonde-v9.log").read_text()
    assert "plafond 0.5 USD" in j and not (tmp_path / "journal-sonde-v9.log.creation-incertaine").exists()
