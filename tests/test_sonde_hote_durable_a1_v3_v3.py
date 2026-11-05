"""Essais en mode jouet de la sonde v3 de l'hôte durable d'A1-v3 (contre-lectures `contre-lecture-sonde-v1.md` et
`contre-lecture-sonde-v2.md` ; m7 : cas sain
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
from controle_ia import sonde_hote_durable_a1_v3_v3 as s

RACINE = Path(__file__).resolve().parents[1]
GARDE = RACINE / ".claude" / "hooks" / "garde_calcul.py"
JOUR = dt.date(2026, 11, 4)
JETON = "ghp_jouet_sonde_v3_XYZ987654321"
CLE_VAST = "vastjouet-cle-instance-v3-0001"
CLE_COMPTE = "vastjouet-cle-compte-v3-0002"
ENTETE = ("| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |\n"
          "|---|---|---|---|---|---|---|---|\n")
LIGNE_06 = "| GO-2026-11-04-06 | 2026-11-04 | calcul | A1-v3, Argon | 400 USD | 2026-11-18 | Lazar | mot |\n"
LIGNE_09 = "| GO-2026-11-04-09 | 2026-11-04 | calcul | machine de l'hôte durable | 35 USD | 2026-11-18 | Lazar | mot |\n"
OFFRE = {"id": 11, "num_gpus": 0, "dph_total": 0.12, "cpu_cores_effective": 8, "cpu_ram": 16000, "disk_space": 50,
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
    assert s.cout_maximal_usd(0.40, 1200) == pytest.approx(0.40 * (600 + 1200 + 1500 + 600) / 3600)
    assert s.verifier_plafond(0.40, 1800) <= s.PLAFOND_SONDE_USD
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
    a = dict(go="GO-2026-11-04-09", registre_main=str(reg), garde_main=str(GARDE), offres=str(offres), offre="12",
             commit_prive="a" * 40, journal_local=str(tmp_path / "journal-sonde-v3.log"), duree_s="1200",
             verifier_seulement=False)
    a.update(kw)
    return type("A", (), a)()


ENV_PILOTE = {"GH_TOKEN": JETON, "VAST_API_KEY": CLE_COMPTE, "GO_ID": "GO-2026-11-04-09"}


def test_louer_cas_sain_etat_ecrit_puis_seconde_location_refusee(tmp_path):
    vast = h.ClientVastJouet(tmp_path / "vast.json")
    t0 = dt.datetime(2026, 11, 4, 13, 0, tzinfo=dt.timezone.utc)
    assert s.louer(args_louer(tmp_path), vast, JOUR, dict(ENV_PILOTE), t0) == 0
    e = json.loads((tmp_path / "journal-sonde-v3.log.etat.json").read_text())
    assert e["identifiant"] == 90000001 and e["etiquette"] == "sonde-a1-v3-v3"
    assert e["borne_signe_de_vie_utc"] == "2026-11-04T13:30:00Z" and e["echeance_finale_utc"] == "2026-11-04T13:55:00Z"
    j = (tmp_path / "journal-sonde-v3.log").read_text()
    assert "LIGNE POUR registres/etat.md" in j and "-y" in j and JETON not in j and CLE_COMPTE not in j
    assert s.louer(args_louer(tmp_path), vast, JOUR, dict(ENV_PILOTE), t0) == 2  # R12 : jamais une seconde location
    assert len(vast.instances()) == 1


@pytest.mark.parametrize("env_modif, kw, motif", [
    ({"GO_ID": None}, {}, "GO_ID=GO-2026-11-04-09 exigé"),
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
    assert vast.instances() == [] and motif in (tmp_path / "journal-sonde-v3.log").read_text()


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
    ('{"success": false, "msg": "pas de place"}', 0, "création refusée"),
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
    assert (tmp_path / "journal-sonde-v3.log.creation-incertaine").exists()
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
    p.write_text(json.dumps({"identifiant": ident, "etiquette": "sonde-a1-v3-v3", "t0_utc": "2026-11-04T13:00:00Z",
                             "borne_signe_de_vie_utc": "2026-11-04T13:30:00Z",
                             "echeance_finale_utc": "2026-11-04T13:55:00Z"}))
    return type("A", (), {"etat": str(p), "journal_local": str(tmp_path / "controle.log")})()


def heure(hh, mm):
    return dt.datetime(2026, 11, 4, hh, mm, tzinfo=dt.timezone.utc)


@pytest.mark.parametrize("instances, vie, quand, code, gestes", [
    ([], False, heure(14, 30), 0, []),                                                       # déjà détruite
    ([{"id": 4321, "label": "sonde-a1-v3-v3"}], True, heure(13, 40), 5, []),                  # vivante : recontrôler (M-A)
    ([{"id": 4321, "label": "sonde-a1-v3-v3"}], False, heure(13, 20), 5, []),                 # avant la borne : recontrôler
    ([{"id": 4321, "label": "sonde-a1-v3-v3"}], True, heure(14, 10), 1, [("detruire", 4321)]),   # T0 + 70 : détruite (M-A)
    ([{"id": 4321, "label": "sonde-a1-v3-v3"}], False, heure(13, 31), 1, [("detruire", 4321)]),  # jamais démarrée (m2)
    ([{"id": 4321, "label": "sonde-a1-v3-v3"}], True, heure(14, 6), 1, [("detruire", 4321)]),    # minuterie en défaut
    ([{"id": 4321, "label": "autre"}], False, heure(14, 30), 2, []),                           # étiquette (f8)
])
def test_controler_du_pilote(tmp_path, instances, vie, quand, code, gestes):
    v = VastFactice(instances)
    assert s.controler(etat_pilote(tmp_path), v, lambda: vie, quand, {}) == code
    assert v.gestes == gestes


def test_controler_protegee_et_destruction_non_suivie(tmp_path):
    v = VastFactice([{"id": 58936096, "label": "sonde-a1-v3-v3"}])
    assert s.controler(etat_pilote(tmp_path, 58936096), v, lambda: False, heure(15, 0), {}) == 2 and v.gestes == []
    v = VastFactice([{"id": 4321, "label": "sonde-a1-v3-v3"}], reste_apres_destruction=True)
    assert s.controler(etat_pilote(tmp_path), v, lambda: False, heure(15, 0), {}) == 3


def test_offre_la_moins_chere_tiree_de_la_reponse(tmp_path, capsys):
    f = tmp_path / "offres.json"
    f.write_text(json.dumps([OFFRE, dict(OFFRE, id=12, dph_total=0.09), dict(OFFRE, id=13, dph_total=0.01, num_gpus=1)]))
    assert s.principal(["offre", "--offres", str(f)]) == 0 and capsys.readouterr().out.strip() == "12"
    f.write_text(json.dumps([dict(OFFRE, num_gpus=1)]))
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


def lancer_demarrage(tmp_path, commit, depot, delete_code="200", label="sonde-a1-v3-v3", ident="123", minuterie=None):
    racine = tmp_path / "racine"
    racine.mkdir(exist_ok=True)
    if minuterie:
        (racine / "sonde-v3-minuterie.txt").write_text(minuterie)
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
    while time.time() < fin and "HTTP" not in ((racine / "sonde-v3-minuterie.log").read_text()
                                               if (racine / "sonde-v3-minuterie.log").exists() else ""):
        time.sleep(0.2)
    return r, racine, (appels.read_text() if appels.exists() else ""), time.time() - debut


def test_demarrage_cas_sain_minuterie_puis_clone_puis_amorce_puis_destruction(tmp_path):
    nu, commit = depot_avec_amorce(tmp_path, 'echo "amorce jouée" > "$RACINE_SONDE/amorce-jouee.txt"\n')
    r, racine, appels, _ = lancer_demarrage(tmp_path, commit, nu)
    assert r.returncode == 0, r.stderr
    assert (racine / "amorce-jouee.txt").exists()
    temps = (racine / "sonde-v3-temps.txt").read_text()
    assert "clone 0 en" in temps and "amorce finie" in temps
    log = (racine / "sonde-v3-minuterie.log").read_text()
    assert "DELETE instance 123 (essai 1) : HTTP 200" in log and "ALARME" not in log
    assert "-X DELETE" in appels and "/instances/123/" in appels and "-X PUT" not in appels
    assert CLE_VAST not in log + temps  # la clé d'instance ne va que dans l'en-tête de curl


def test_demarrage_clone_impossible_la_minuterie_detruit_quand_meme(tmp_path):
    r, racine, appels, _ = lancer_demarrage(tmp_path, "b" * 40, tmp_path / "pas-de-depot.git")
    assert "clone" in (racine / "sonde-v3-temps.txt").read_text() and not (racine / "amorce-jouee.txt").exists()
    assert "DELETE instance 123 (essai 1) : HTTP 200" in (racine / "sonde-v3-minuterie.log").read_text()  # M1(a)


@pytest.mark.parametrize("kw, attendu, interdit", [
    ({"delete_code": "403"}, "ALARME : destruction non obtenue avant la fin de vie", "-X PUT"),  # m-a : jamais d'arrêt
    ({"label": "autre-chose"}, "pas sonde-a1-v3-v3 : aucun geste", "-X DELETE"),
    ({"ident": "58936099"}, "instance protégée : aucun geste", "-X DELETE"),
    ({"ident": "12a"}, "identifiant illisible : aucun geste", "-X DELETE"),
])
def test_demarrage_artefacts_de_la_minuterie(tmp_path, kw, attendu, interdit):
    r, racine, appels, _ = lancer_demarrage(tmp_path, "b" * 40, tmp_path / "pas-de-depot.git", **kw)
    fin = time.time() + 15
    while time.time() < fin and attendu not in (racine / "sonde-v3-minuterie.log").read_text():
        time.sleep(0.2)
    assert attendu in (racine / "sonde-v3-minuterie.log").read_text()
    if interdit:
        assert interdit not in appels


def test_demarrage_reprise_garde_l_echeance_d_origine(tmp_path):
    passe = int(time.time()) - 3600
    r, racine, appels, duree = lancer_demarrage(tmp_path, "b" * 40, tmp_path / "pas-de-depot.git",
                                                minuterie=f"{passe - 100} {passe}\n")
    assert (racine / "sonde-v3-minuterie.txt").read_text().split() == [str(passe - 100), str(passe)]
    assert "DELETE instance 123" in (racine / "sonde-v3-minuterie.log").read_text() and duree < 60


def test_script_de_demarrage_exige_un_hash_et_corps_sans_cle():
    with pytest.raises(h.Refus):
        s.script_de_demarrage("main")
    c = s.corps("a" * 40, OFFRE, 1200, JETON, 1_800_000_000)
    assert set(c["env"]) == {"COMMIT_PRIVE", "GO_ID", "PRIX_H_USD", "DUREE_MAX_S", "DEPOT_URL", "GH_TOKEN", "ECHEANCE_UTC_S",
                             "TIR_MINUTERIE"}
    assert c["label"] == "sonde-a1-v3-v3" and c["env"]["GO_ID"] == "GO-2026-11-04-09"
    assert c["env"]["ECHEANCE_UTC_S"] == "1800000000" and c["env"]["TIR_MINUTERIE"] == "0"
    for mauvaise in (None, 0, -5, True, "1800000000"):
        with pytest.raises(h.Refus, match="échéance absolue"):
            s.corps("a" * 40, OFFRE, 1200, JETON, mauvaise)
    texte = base64.b64decode(c["script"].split()[1]).decode()
    assert texte.index("setsid bash") < texte.index("git init")  # la minuterie avant le clonage (M1)
    with pytest.raises(h.Refus, match="GH_TOKEN"):
        s.corps("a" * 40, OFFRE, 1200, "", 1_800_000_000)


# --- amorce v3 (m7 : cas sain jusqu'à exec, et artefacts) -----------------------------------------------------------------


def amorce(tmp_path, **modif):
    racine = tmp_path / "racine-amorce"
    d = racine / "amorce-depot" / "src" / "controle_ia"
    d.mkdir(parents=True, exist_ok=True)
    for nom in ("sonde_hote_durable_a1_v3.py", "hote_durable_a1_v3.py"):
        (d / nom).write_text("# factice\n")
    (d / "sonde_hote_durable_a1_v3_v3.py").write_text(
        "import os, sys, pathlib\npathlib.Path(os.environ['RACINE_AMORCE'], 'exec-atteint.txt').write_text(' '.join(sys.argv[1:]))\n")
    env = {"PATH": os.environ["PATH"], "COMMIT_PRIVE": "a" * 40, "GO_ID": "GO-2026-11-04-09", "PRIX_H_USD": "0.1",
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
    ({"GO_ID": "GO-2026-11-04-06"}, "au lieu de GO-2026-11-04-09"), ({"DUREE_MAX_S": "12a"}, "non entière"),
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
    env = {"PATH": os.environ["PATH"], "COMMIT_PRIVE": "a" * 40, "GO_ID": "GO-2026-11-04-09", "PRIX_H_USD": "0.1",
           "DUREE_MAX_S": "1200", "ECHEANCE_UTC_S": "1800000000", "GH_TOKEN": JETON, "RACINE_AMORCE": str(racine),
           "SAUTER_INSTALLATION": "1"}
    r = subprocess.run(["bash", str(RACINE / s.AMORCE)], env=env, capture_output=True, text=True)
    assert r.returncode == 2 and "absent du commit" in r.stdout


# --- machine ---------------------------------------------------------------------------------------------------------------


@pytest.fixture
def monde(tmp_path):
    def fabriquer(depuis_s=59.7, etiquette="sonde-a1-v3-v3"):
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
        (racine / "sonde-v3-minuterie.txt").write_text(f"{int(t0)} {int(t0) + 1260 + 1500}\n")
        (racine / "sonde-v3-temps.txt").write_text("demarrage …\nclone 0 en 3 s\n")
        (racine / "amorce-sonde-a1v3-v3.log").write_text("AMORCE SONDE V3 : installations en 40 s\n")
        r = s.reglages({})
        r.travail, r.clone_prive, r.periode_s, r.attente_poussee_s = racine / "sonde-a1-v3-v3", clone, 0.1, 0
        r.jouet, r.vast_jouet, r.aujourd_hui = True, tmp_path / "vast.json", JOUR
        h.ClientVastJouet(r.vast_jouet)._ecrire({"instances": [{"id": 90000001, "label": etiquette}], "gestes": []})
        env = {"GO_ID": "GO-2026-11-04-09", "PRIX_H_USD": "0.12", "DUREE_MAX_S": "60", "GH_TOKEN": JETON,
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
    assert s.MachineSondeV3(r, env, 120).principal() == 0
    vie = versees(nu, s.BRANCHE_VIE)
    assert f"{s.BRANCHE_VIE}/signe-de-vie.json" in vie
    f = versees(nu, s.BRANCHE)
    b = s.BRANCHE
    j = f[f"{b}/journal-sonde-a1-v3-v3.log"].decode()
    for attendu in ("GO accepté par la garde de main", "signe de vie poussé", "clé d'instance : lecture faite",
                    "PLAFOND DE DURÉE DE LA SONDE atteint", "nature de la fin : plafond_de_duree_de_la_sonde"):
        assert attendu in j, attendu
    for nom in s.FICHIERS_DEMARRAGE[:1] + s.FICHIERS_DEMARRAGE[2:]:  # f5 : journaux du démarrage versés
        assert f"{b}/demarrage/{nom}" in f, nom
    for ligne in f[f"{b}/EMPREINTES-sonde-hote-durable-a1-v3-v3.txt"].decode().splitlines():
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
    assert s.MachineSondeV3(r, env, 120).principal() == 0
    j = versees(nu, s.BRANCHE_REFUS)[f"{s.BRANCHE_REFUS}/journal-sonde-a1-v3-v3.log"].decode()
    assert motif in j and "course factice détachée" not in j and "cle-interdite" not in j
    assert versees(nu, s.BRANCHE) == {} and gestes(r) == [["detruire", 90000001]]


def test_machine_etiquette_autre_aucun_geste(monde):
    r, env, nu = monde(etiquette="autre")
    assert s.MachineSondeV3(r, env, 120).principal() == 4 and gestes(r) == []


def test_machine_exception_du_versement_attrapee_puis_arret(monde, monkeypatch):
    r, env, nu = monde()
    m = s.MachineSondeV3(r, env, 120)
    monkeypatch.setattr(m, "verser", lambda *a: (_ for _ in ()).throw(urllib.error.URLError("réseau")))
    assert m.principal() == 0 and gestes(r) == [["detruire", 90000001]]  # m-a : détruite même sans versement, jamais arrêtée
    m2 = s.MachineSondeV3(r, env, 120)
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
    m = s.MachineSondeV3(r, env, 120)
    monkeypatch.setattr(m, "client_vast", lambda: VastQuiRefuse(r.vast_jouet))
    assert m.principal() == 5 and gestes(r) == []  # m-a : aucun arrêt, la minuterie recommence
    m2 = s.MachineSondeV3(r, env, 120)
    monkeypatch.setattr(m2, "client_vast", lambda: VastQuiRefuse(r.vast_jouet, refuse_arret=True))
    m2.j = h.Journal(r.travail / "j2.log")
    assert m2.se_detruire(True) == 5 and "aucun arrêt" in (r.travail / "j2.log").read_text()
    m3 = s.MachineSondeV3(r, env, 120)
    m3.j = m2.j
    monkeypatch.setattr(m3, "client_vast", lambda: (_ for _ in ()).throw(ValueError("clé vide")))
    assert m3.se_detruire(True) == 4


def test_machine_reprise_et_fuite(monde):
    r, env, nu = monde()
    r.travail.mkdir()
    (r.travail / "ETAT").write_text("course\n")
    assert s.MachineSondeV3(r, env, 120).principal() == 0
    assert f"{s.BRANCHE_INTERROMPUE}/journal-sonde-a1-v3-v3.log" in versees(nu, s.BRANCHE_INTERROMPUE)
    (r.travail / "ETAT").write_text("verse\n")
    assert s.MachineSondeV3(r, env, 120).principal() == 0  # déjà versé : destruction seule


def test_machine_fuite_rien_verse(monde):
    r, env, nu = monde()
    r.travail.mkdir()
    (r.travail / "ETAT").write_text("course\n")
    (r.travail / "fuite.txt").write_text(JETON)
    assert s.MachineSondeV3(r, env, 120).principal() == 0
    assert versees(nu, s.BRANCHE_INTERROMPUE) == {} and gestes(r) == [["detruire", 90000001]]


def test_machine_signe_de_vie_deja_present_la_sonde_continue(monde):
    r, env, nu = monde()
    w = r.travail.parent / "w-vie"
    run("git", "init", "-q", "-b", "x", str(w))
    (w / "a").write_text("a")
    run("git", "add", "-A", cwd=w)
    run("git", "-c", "user.name=j", "-c", "user.email=j@j", "commit", "-q", "-m", "a", cwd=w)
    run("git", "push", "-q", str(nu), f"HEAD:refs/heads/{s.BRANCHE_VIE}", cwd=w)
    assert s.MachineSondeV3(r, env, 120).principal() == 0
    j = versees(nu, s.BRANCHE)[f"{s.BRANCHE}/journal-sonde-a1-v3-v3.log"].decode()
    assert "signe de vie non poussé" in j and "nature de la fin : plafond_de_duree_de_la_sonde" in j



# --- v3 : contre-lecture `contre-lecture-sonde-v2.md` ----------------------------------------------------------------------


def test_louer_echeance_absolue_controles_et_tir(tmp_path):
    vast = h.ClientVastJouet(tmp_path / "vast.json")
    t0 = dt.datetime(2026, 11, 4, 13, 0, tzinfo=dt.timezone.utc)
    assert s.louer(args_louer(tmp_path), vast, JOUR, dict(ENV_PILOTE), t0) == 0
    e = json.loads((tmp_path / "journal-sonde-v3.log.etat.json").read_text())
    assert e["controles_utc"] == ["2026-11-04T13:40:00Z", "2026-11-04T14:10:00Z"]  # M-A
    j = (tmp_path / "journal-sonde-v3.log").read_text()
    assert "controler" in j and "vastai destroy" not in j  # f-b : la ligne d'état renvoie à controler
    vast2 = h.ClientVastJouet(tmp_path / "vast2.json")
    a = args_louer(tmp_path / "x" if (tmp_path / "x").mkdir() is None else tmp_path, tir_minuterie=True)
    assert s.louer(a, vast2, JOUR, dict(ENV_PILOTE), t0) == 0
    e2 = json.loads(Path(a.journal_local + ".etat.json").read_text())
    assert e2["echeance_finale_utc"] == "2026-11-04T13:40:00Z" and e2["tir_minuterie"] is True  # marge courte (m-d)


def test_borne_ecrite_au_pire_cas():
    assert s.cout_maximal_usd(0.40, s.DUREE_MAX_S) == pytest.approx(0.50)   # 0,40 USD/h, 30 min : 0,50 USD au plus
    assert s.cout_maximal_usd(0.40, 1200) == pytest.approx(0.4333, abs=1e-4)
    assert s.cout_maximal_usd(0.40, 1200, s.MARGE_TIR_S) == pytest.approx(0.40 * 3000 / 3600)


def test_demarrage_echeance_absolue_passee_detruit_aussitot(tmp_path):
    """M-B : machine partie tard ; la minuterie prend l'échéance absolue du pilote, déjà passée, et détruit aussitôt."""
    racine = tmp_path / "racine"
    racine.mkdir()
    bin_ = tmp_path / "bin"
    bin_.mkdir()
    appels = tmp_path / "appels.txt"
    outil(bin_, "curl", f'echo "$@" >> "{appels}"\ncase "$*" in *"-X DELETE"*) printf 200;; '
                        "*) printf '{\"label\": \"sonde-a1-v3-v3\"}';; esac\n")
    env = {"PATH": f"{bin_}:{os.environ['PATH']}", "HOME": str(tmp_path), "RACINE_SONDE": str(racine),
           "API_VAST": "https://vast.invalide/api/v0", "DUREE_MAX_S": "1800", "SONDE_VIE_APRES_S": "1",
           "ECHEANCE_UTC_S": str(int(time.time()) - 10), "DEPOT_URL": str(tmp_path / "absent.git"), "GH_TOKEN": JETON,
           "CONTAINER_ID": "123", "CONTAINER_API_KEY": CLE_VAST, "GIT_CONFIG_GLOBAL": "/dev/null"}
    debut = time.time()
    subprocess.run(["bash", "-c", s.script_de_demarrage("b" * 40)], env=env, capture_output=True, timeout=120)
    t0, ech = (racine / "sonde-v3-minuterie.txt").read_text().split()
    assert int(ech) == int(env["ECHEANCE_UTC_S"]) < int(t0) + 1800
    assert "DELETE instance 123 (essai 1) : HTTP 200" in (racine / "sonde-v3-minuterie.log").read_text()
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
    log = (racine / "sonde-v3-minuterie.log").read_text()
    assert "ALARME : curl absent : repli par python3" in log and "DELETE instance 123 (essai 1)" in log
    assert "curl NON" in (racine / "sonde-v3-temps.txt").read_text()


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
        (racine / "sonde-v3-minuterie.txt").write_text(f"{passe - 100} {passe}\n")
    bin_ = tmp_path / "bin"
    bin_.mkdir()
    outil(bin_, "curl", 'sleep 2\ncase "$*" in *"-X DELETE"*) printf 200;; *) printf \'{"label": "sonde-a1-v3-v3"}\';; esac\n')
    env = {"PATH": f"{bin_}:{os.environ['PATH']}", "HOME": str(tmp_path), "RACINE_SONDE": str(racine),
           "API_VAST": "https://vast.invalide/api/v0", "DUREE_MAX_S": "1", "SONDE_MARGE_S": "1", "SONDE_VIE_APRES_S": "1",
           "DEPOT_URL": str(tmp_path / "absent.git"), "GH_TOKEN": JETON, "CONTAINER_ID": "123", "CONTAINER_API_KEY": CLE_VAST,
           "GIT_CONFIG_GLOBAL": "/dev/null"}
    r = subprocess.run(["unshare", "-pf", "bash", "-c", s.script_de_demarrage("b" * 40)], env=env, capture_output=True,
                       timeout=180)
    log = (racine / "sonde-v3-minuterie.log").read_text()  # lu après la fin de tout l'espace de processus
    assert "DELETE instance 123 (essai 1) : HTTP 200" in log, log
    assert "fin du principal" in (racine / "sonde-v3-temps.txt").read_text()


def test_machine_tir_de_la_minuterie_aucun_geste(monde):
    r, env, nu = monde()
    env["TIR_MINUTERIE"] = "1"
    assert s.MachineSondeV3(r, env, 120).principal() == 5
    assert gestes(r) == [] and f"{s.BRANCHE}/journal-sonde-a1-v3-v3.log" in versees(nu, s.BRANCHE)


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
    assert s.MachineSondeV3(r, env, 120).principal() == 0
    j = versees(nu, s.BRANCHE_REFUS)[f"{s.BRANCHE_REFUS}/journal-sonde-a1-v3-v3.log"].decode()
    assert motif in j and "course factice détachée" not in j


def test_machine_echeance_absolue_raccourcit_la_course(monde):
    r, env, nu = monde(depuis_s=0)
    env["ECHEANCE_UTC_S"] = str(int(time.time()) + 362)  # 300 s de réserve au versement : 62 s utiles au plus
    m = s.MachineSondeV3(r, env, 120)
    assert m.principal() == 0 and m.r.duree_max_s <= 62.5


def test_client_pilote_n_ecrit_que_le_code(tmp_path):
    c, _ = client_factice(tmp_path, "ligne de sortie avec un identifiant d'une autre instance 999", 7)
    with pytest.raises(h.Refus) as e:
        c.instances()
    assert str(e.value) == "vastai show instances : code 7"  # f-a
