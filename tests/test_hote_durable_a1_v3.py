"""Essais en mode jouet de l'hôte durable d'A1-v3 (aucune location, aucun appel de modèle, aucun réseau).

Chaque garde est éprouvée sur un cas sain et sur un artefact (R5). Le monde jouet : un dépôt privé nu à quatre branches (main
avec la vraie garde de calcul, la source du registre, les pièces gelées factices, la configuration factice), un dépôt public
à deux commits (code gelé, puis texte scellé v3 et son compagnon), un relais factice qui ne sert que `/relais/etat`, un
lanceur factice dont le comportement est lu dans un fichier, et Vast simulé par un fichier JSON.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import socket
import subprocess
import sys
from pathlib import Path

import pytest

from controle_ia import hote_durable_a1_v3 as h

RACINE = Path(__file__).resolve().parents[1]
GARDE_REELLE = RACINE / ".claude" / "hooks" / "garde_calcul.py"
JOUR = dt.date(2026, 11, 4)
CLE = "cle-jouet-argon-ABCDEFGH123456"
JETON = "ghp_jouet_XYZ9876543210abcdef"
CLE_VAST = "vastjouet-cle-0001-abcdef"
ENTETE = ("| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |\n"
          "|---|---|---|---|---|---|---|---|\n")
LIGNE_06 = ("| GO-2026-11-04-06 | 2026-11-04 | calcul | troisième course d'A1-v3, hôte durable | 400 USD | 2026-11-18 | "
            "Lazar | mot de Lazar |\n")


def sha(o: bytes) -> str:
    return hashlib.sha256(o).hexdigest()


def run(*cmd, cwd=None):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    return r.stdout.strip()


def port_libre() -> int:
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def registre(tmp_path, *lignes, nom="go.md") -> Path:
    p = tmp_path / nom
    p.write_text("# Registre factice\n\n" + ENTETE + "".join(lignes), encoding="utf-8")
    return p


# --- GO : garde de main ----------------------------------------------------------------------------------------------------


def test_go_cas_sain_et_registre_reel_de_main(tmp_path):
    g = h.verifier_go(registre(tmp_path, LIGNE_06), GARDE_REELLE, "GO-2026-11-04-06", 400, JOUR)
    assert g["lignes"] == 1 and g["plafond_usd"] == 400
    # registre réel de main (17 doublons, dont l'extension de GO-2026-11-04-04 : la garde de main les admet)
    g = h.verifier_go(RACINE / "registres" / "go.md", GARDE_REELLE, "GO-2026-11-04-06", 400, JOUR)
    assert g["echeance"] == "2026-11-18"
    assert h.doublons_lecteur_du_lanceur(RACINE / "registres" / "go.md")  # le lecteur du lanceur, lui, le refuserait


@pytest.mark.parametrize("lignes, go, jour, motif", [
    ([], "GO-2026-11-04-06", JOUR, "absent"),
    ([LIGNE_06], "GO-2026-11-03-01", JOUR, "aucun autre GO"),
    ([LIGNE_06.replace("| calcul |", "| décision |")], "GO-2026-11-04-06", JOUR, "pas « calcul »"),
    ([LIGNE_06.replace("| Lazar |", "| directeur |")], "GO-2026-11-04-06", JOUR, "pas accordé par Lazar"),
    ([LIGNE_06], "GO-2026-11-04-06", dt.date(2026, 11, 19), "hors de sa période"),
    ([LIGNE_06], "GO-2026-11-04-06", dt.date(2026, 11, 3), "hors de sa période"),
    ([LIGNE_06.replace("400 USD", "399 USD")], "GO-2026-11-04-06", JOUR, "exactement 400"),
    ([LIGNE_06.replace("400 USD", "≈ 400 USD")], "GO-2026-11-04-06", JOUR, "exactement 400"),
    ([LIGNE_06, "| GO-2026-11-04-09 | 2026-11-04 | révocation | révoque GO-2026-11-04-06 | — | 2026-11-04 | Lazar | mot |\n"],
     "GO-2026-11-04-06", JOUR, "révoqué"),
    ([LIGNE_06, LIGNE_06], "GO-2026-11-04-06", JOUR, "en double"),
    ([LIGNE_06, LIGNE_06.replace("troisième course", "extension : autre plafond").replace("400 USD", "450 USD")],
     "GO-2026-11-04-06", JOUR, "exactement 400"),
])
def test_go_artefacts(tmp_path, lignes, go, jour, motif):
    with pytest.raises(h.Refus, match=motif):
        h.verifier_go(registre(tmp_path, *lignes), GARDE_REELLE, go, 400, jour)


def test_go_extension_conforme_admise(tmp_path):
    ext = LIGNE_06.replace("troisième course", "extension : précision du périmètre")
    assert h.verifier_go(registre(tmp_path, LIGNE_06, ext), GARDE_REELLE, "GO-2026-11-04-06", 400, JOUR)["extensions"] == 1


# --- Offre, corps de création, location, inventaire ------------------------------------------------------------------------


OFFRE = {"id": 123, "num_gpus": 0, "dph_total": 0.12, "cpu_cores_effective": 8, "cpu_ram": 16000, "disk_space": 50,
         "reliability": 0.995, "geolocation": "FR", "machine_id": 7}


def test_offre_cas_sain():
    assert h.verifier_offre([OFFRE, dict(OFFRE, id=124)], 123)["dph_total"] == 0.12


@pytest.mark.parametrize("modif, motif", [
    ({"num_gpus": 1}, "sans carte"), ({"num_gpus": None}, "sans carte"), ({"dph_total": 0.41}, "prix horaire"),
    ({"dph_total": True}, "prix horaire"), ({"dph_total": 0}, "prix horaire"), ({"cpu_ram": 4000}, "cpu_ram"),
    ({"reliability": 0.9}, "reliability"), ({"id": 999}, "0 dans la réponse"),
])
def test_offre_artefacts(modif, motif):
    with pytest.raises(h.Refus, match=motif):
        h.verifier_offre([dict(OFFRE, **modif)], 123)


def test_offre_en_double_refusee():
    with pytest.raises(h.Refus, match="2 dans la réponse"):
        h.verifier_offre([OFFRE, OFFRE], 123)


def args_louer(tmp_path, reg, **kw):
    offres = tmp_path / "offres.json"
    offres.write_text(json.dumps([OFFRE]))
    a = dict(go="GO-2026-11-04-06", registre_main=str(reg), garde_main=str(GARDE_REELLE), offres=str(offres),
             offre="123", commit_prive="a" * 40, commit_public="b" * 40, sha_texte="c" * 64, commit_registre="d" * 40,
             journal_local=str(tmp_path / "journal-location.log"), verifier_seulement=False, jouet=None)
    a.update(kw)
    return type("A", (), a)()


def test_louer_jouet_cas_sain_secrets_jamais_ecrits(tmp_path, monkeypatch):
    monkeypatch.setenv("CLE_ARGON", CLE)
    monkeypatch.setenv("GH_TOKEN", JETON)
    vast = h.ClientVastJouet(tmp_path / "vast.json")
    a = args_louer(tmp_path, registre(tmp_path, LIGNE_06))
    assert h.louer(a, vast, JOUR) == 0
    inst = vast.instances()
    assert len(inst) == 1 and set(inst[0]["env"]) >= {"CLE_ARGON", "GH_TOKEN", "COMMIT_PUBLIC"}
    journal = Path(a.journal_local).read_text()
    assert "machine créée : identifiant 90000001" in journal and CLE not in journal and JETON not in journal
    assert Path(a.journal_local + ".identifiant").read_text().strip() == "90000001"
    assert CLE not in (tmp_path / "vast.json").read_text()


def test_louer_artefacts_rien_cree(tmp_path, monkeypatch):
    vast = h.ClientVastJouet(tmp_path / "vast.json")
    monkeypatch.setenv("GH_TOKEN", JETON)
    monkeypatch.delenv("CLE_ARGON", raising=False)
    assert h.louer(args_louer(tmp_path, registre(tmp_path, LIGNE_06)), vast, JOUR) == 2  # clé d'Argon absente
    monkeypatch.setenv("CLE_ARGON", CLE)
    assert h.louer(args_louer(tmp_path, registre(tmp_path, LIGNE_06.replace("400", "300"))), vast, JOUR) == 2
    assert h.louer(args_louer(tmp_path, registre(tmp_path, LIGNE_06), offre="999"), vast, JOUR) == 2
    assert h.louer(args_louer(tmp_path, registre(tmp_path, LIGNE_06), commit_public="abc"), vast, JOUR) == 2
    assert h.louer(args_louer(tmp_path, registre(tmp_path, LIGNE_06), verifier_seulement=True), vast, JOUR) == 0
    assert vast.instances() == []
    assert "REFUS" in (tmp_path / "journal-location.log").read_text()


def test_inventaire_filtre_l_environnement():
    class C:
        def instances(self):
            return [{"id": 5, "label": "a1-v3-troisieme-v1", "actual_status": "running", "extra_env": [["CLE_ARGON", CLE]],
                     "onstart": "x", "dph_total": 0.1}]
    sortie = json.dumps(h.inventaire(C()))
    assert CLE not in sortie and "extra_env" not in sortie and '"id": 5' in sortie


def test_script_de_demarrage_exige_un_hash_complet():
    assert "checkout -q --detach " + "f" * 40 in h.script_de_demarrage("f" * 40)
    with pytest.raises(h.Refus):
        h.script_de_demarrage("main")


def test_creation_par_l_outil_vastai_secrets_masques(tmp_path):
    """Outil factice qui renvoie ses arguments : la réponse est lue, aucune valeur de secret n'en ressort."""
    outil = tmp_path / "vastai"
    outil.write_text("#!/bin/sh\necho \"$@\" >&2\necho '{\"success\": true, \"new_contract\": 4242}'\n")
    outil.chmod(0o755)
    c = h.ClientVastCli(str(outil))
    corps = h.corps_de_creation("a" * 40, "b" * 40, "c" * 64, "d" * 40, h.verifier_offre([OFFRE], 123),
                                {"CLE_ARGON": CLE, "GH_TOKEN": JETON})
    assert c.creer(123, corps) == 4242
    echec = tmp_path / "vastai-echec"
    echec.write_text("#!/bin/sh\necho \"${12} ${13}\"\nexit 1\n")  # renvoie l'argument --env, qui porte les secrets
    echec.chmod(0o755)
    with pytest.raises(h.Refus) as e:
        h.ClientVastCli(str(echec)).creer(123, corps)
    assert CLE not in str(e.value) and JETON not in str(e.value) and "[CLE_ARGON masquée]" in str(e.value)
    corps["env"]["CLE_ARGON"] = "a b"
    with pytest.raises(h.Refus, match="espace"):
        c.creer(123, corps)


def test_plafonds_ecrits_coherents():
    assert h.DUREE_MAX_MACHINE_H > 72 and abs(h.PLAFOND_MACHINE_USD - h.PRIX_MAX_H_USD * h.DUREE_MAX_MACHINE_H) < 1e-9
    assert h.PLAFOND_COURSE_USD == 400 and h.PLAFOND_RELAIS_USD >= 400 and h.MAX_APPELS_RELAIS >= 8000


# --- Monde jouet de la machine ---------------------------------------------------------------------------------------------

RELAIS = r'''
import json, os, sys, time, pathlib
from http.server import BaseHTTPRequestHandler, HTTPServer
a = sys.argv[1:]
port = int(a[a.index("--port") + 1]); journal = a[a.index("--journal") + 1]
DRAPEAU = pathlib.Path(%(drapeau)r); COMPORTEMENT = json.loads(pathlib.Path(%(comportement)r).read_text())
with open(journal, "a") as f:
    f.write(json.dumps({"debut": time.time()}) + "\n")
    if COMPORTEMENT.get("fuite"):
        f.write(os.environ.get("GEMINI_API_KEY", "") + "\n")
class G(BaseHTTPRequestHandler):
    def log_message(self, *x): pass
    def do_GET(self):
        corps = json.dumps({"plafond_usd": float(a[a.index("--plafond-usd") + 1]), "max_appels": int(a[a.index("--max-appels") + 1]),
                            "appels": 0, "depense_usd": 0.0, "cle_presente": bool(os.environ.get("GEMINI_API_KEY"))}).encode()
        self.send_response(200); self.send_header("Content-Length", str(len(corps))); self.end_headers(); self.wfile.write(corps)
s = HTTPServer(("127.0.0.1", port), G); s.timeout = 0.1
debut = time.time()
while True:
    s.handle_request()
    if COMPORTEMENT.get("relais_meurt") and not DRAPEAU.exists() and time.time() - debut > 0.5:
        DRAPEAU.write_text("mort une fois"); sys.exit(9)
'''

LANCEUR = r'''
import json, os, sys, time, pathlib
c = json.loads(pathlib.Path(%(comportement)r).read_text())
compteur = pathlib.Path(%(compteur)r)
if "--verifier-seulement" in sys.argv:
    print("conforme"); sys.exit(c.get("verifier", 0))
assert not [k for k in os.environ if "KEY" in k or "TOKEN" in k or "CLE" in k], "variable de clé dans l'environnement"
compteur.write_text(str(int(compteur.read_text() or 0) + 1) if compteur.exists() else "1")
sortie = pathlib.Path(sys.argv[sys.argv.index("demonstrations/attaque_goodhart_v3.py") + 1] if False else sys.argv[1])
sortie.mkdir(parents=True)
(sortie / "manifeste.json").write_text("{}")
time.sleep(c.get("duree_s", 0.3))
(sortie / "attaque-goodhart-v3.json").write_text(json.dumps({"code": c.get("code", 0)}))
sys.exit(c.get("code", 0))
'''


def depot_nu_avec_branches(tmp_path, branches: dict[str, dict[str, bytes]]) -> Path:
    nu = tmp_path / "prive.git"
    run("git", "init", "-q", "--bare", "-b", "main", str(nu))
    for b, fichiers in branches.items():
        w = tmp_path / f"w-{b.replace('/', '_')}"
        run("git", "init", "-q", "-b", b, str(w))
        for chemin, octets in fichiers.items():
            p = w / chemin
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(octets)
        run("git", "add", "-A", cwd=w)
        run("git", "-c", "user.name=j", "-c", "user.email=j@j", "commit", "-q", "-m", b, cwd=w)
        run("git", "push", "-q", str(nu), f"HEAD:refs/heads/{b}", cwd=w)
    return nu


@pytest.fixture
def monde(tmp_path):
    def fabriquer(comportement=None, registre_source=None, sha_texte_faux=False, code_hors_lignee=False,
                  piece_fausse=False):
        comp = tmp_path / "comportement.json"
        comp.write_text(json.dumps(comportement or {}))
        nuit = h.NUIT
        relais = (RELAIS % {"drapeau": str(tmp_path / "relais-mort-une-fois"), "comportement": str(comp)}).encode()
        piece = b"consigne factice\n"
        conf = json.dumps({"pieces": {"consigne": {"chemin": "pieces/a.md", "sha256": sha(piece)}}}).encode()
        sources = {f"{nuit}/commande_argon_v56_nuit_v2.py": relais, f"{nuit}/registre_depense_cumulee_v1.py": b"# r\n",
                   f"{nuit}/pieces/a.md": piece, "donnees/espece-seule-v1/collisionneur_v7.py": b"# c\n"}
        reg_main = ("# Registre\n\n" + ENTETE + LIGNE_06).encode()
        nu = depot_nu_avec_branches(tmp_path, {
            "main": {"registres/go.md": reg_main, ".claude/hooks/garde_calcul.py": GARDE_REELLE.read_bytes()},
            h.SOURCE_REGISTRE: {"registres/go.md": registre_source or reg_main},
            h.REF_SOURCES: sources,
            h.REF_CONFIGURATION: {h.CHEMIN_CONF_DANS_REF: conf},
        })
        clone_prive = tmp_path / "amorce-depot"
        run("git", "clone", "-q", str(nu), str(clone_prive))
        commit_registre = run("git", "rev-parse", f"origin/{h.SOURCE_REGISTRE}", cwd=clone_prive)
        empreintes = {f"{nuit}/configuration-mini-course-kimi-argon-v3.json": sha(conf),
                      f"{nuit}/commande_argon_v56_nuit_v2.py": sha(relais),
                      f"{nuit}/registre_depense_cumulee_v1.py": sha(b"# r\n"),
                      "donnees/espece-seule-v1/collisionneur_v7.py": "0" * 64 if piece_fausse else sha(b"# c\n")}
        # dépôt public : code gelé, puis texte scellé v3 et compagnon
        pub = tmp_path / "public"
        run("git", "init", "-q", "-b", "main", str(pub))
        lanceur = pub / "orchestrator/demonstrations/attaque_goodhart_v3.py"
        lanceur.parent.mkdir(parents=True)
        lanceur.write_text(LANCEUR % {"comportement": str(comp), "compteur": str(tmp_path / "courses-lancees")})
        run("git", "add", "-A", cwd=pub)
        run("git", "-c", "user.name=j", "-c", "user.email=j@j", "commit", "-q", "-m", "code gelé", cwd=pub)
        gele = run("git", "rev-parse", "HEAD", cwd=pub)
        if code_hors_lignee:
            run("git", "checkout", "-q", "--orphan", "autre", cwd=pub)
        texte = pub / h.NOM_TEXTE
        texte.parent.mkdir(parents=True, exist_ok=True)
        texte.write_text("texte scellé v3 (jouet)\n")
        Path(str(texte) + ".sha256").write_text(f"{sha(texte.read_bytes())}  {texte.name}\n")
        run("git", "add", "-A", cwd=pub)
        run("git", "-c", "user.name=j", "-c", "user.email=j@j", "commit", "-q", "-m", "texte v3", cwd=pub)
        commit_public = run("git", "rev-parse", "HEAD", cwd=pub)
        r = h.Reglages(travail=tmp_path / "a1-v3-troisieme-v1", clone_prive=clone_prive, clone_public=tmp_path / "pub-clone",
                       depot_public=str(pub), racine_sources=tmp_path / "sources", empreintes=empreintes,
                       commit_code_gele=gele, python_relais=sys.executable, python_course=sys.executable,
                       port=port_libre(), periode_s=0.1, duree_max_s=600, attente_relais_s=10, essais_poussee=2,
                       attente_poussee_s=0, jouet=True, vast_jouet=tmp_path / "vast.json", aujourd_hui=JOUR)
        h.ClientVastJouet(r.vast_jouet)._ecrire({"instances": [{"id": 90000001, "etat": "running"}], "gestes": []})
        env = {"COMMIT_PUBLIC": commit_public, "SHA_TEXTE": ("e" * 64) if sha_texte_faux else sha(texte.read_bytes()),
               "COMMIT_REGISTRE": commit_registre, "GO_ID": "GO-2026-11-04-06", "PRIX_H_USD": "0.2",
               "CLE_ARGON": CLE, "GH_TOKEN": JETON, "CONTAINER_ID": "90000001", "CONTAINER_API_KEY": CLE_VAST}
        return r, env, nu
    return fabriquer


def branche(nu: Path, b: str) -> dict[str, str]:
    """Fichiers versés sur la branche b du dépôt nu (chemin relatif → contenu)."""
    sortie = subprocess.run(["git", "ls-tree", "-r", "--name-only", f"refs/heads/{b}"], cwd=nu, capture_output=True,
                            text=True)
    if sortie.returncode != 0:
        return {}
    return {n: subprocess.run(["git", "show", f"refs/heads/{b}:{n}"], cwd=nu, capture_output=True).stdout.decode(
        "utf-8", "replace") for n in sortie.stdout.split() if n.startswith(b + "/")}


def gestes(r) -> list:
    return json.loads(r.vast_jouet.read_text())["gestes"]


def jamais_de_secret(fichiers: dict[str, str]):
    for nom, contenu in fichiers.items():
        for s in (CLE, JETON, CLE_VAST):
            assert s not in contenu, f"secret dans {nom}"


def test_machine_cas_sain_verse_puis_detruit(monde):
    r, env, nu = monde({"code": 0})
    assert h.Machine(r, env).principal() == 0
    f = branche(nu, h.BRANCHE_DONNEES)
    b = h.BRANCHE_DONNEES
    assert f[f"{b}/code-sortie-lanceur.txt"].strip() == "0"
    assert f"{b}/sortie-attaque-goodhart-v3/attaque-goodhart-v3.json" in f
    liste = f[f"{b}/EMPREINTES-sortie-a1-v3-troisieme-v1.txt"]
    for ligne in liste.splitlines():  # chaque empreinte de la liste égale au fichier versé
        e, nom = ligne.split("  ", 1)
        assert (nom, sha(f[f"{b}/{nom}"].encode())) == (nom, e)
    j = f[f"{b}/journal-hote-a1-v3-troisieme-v1.log"]
    for attendu in ("GO accepté par la garde de main", "pièces gelées : 4 empreintes égales", "--verifier-seulement : code 0",
                    "course lancée : PID", "fin du lanceur : code 0", "arrêt de relais par son identifiant",
                    "inchangé", "nature de la fin : fin_du_lanceur"):
        assert attendu in j, attendu
    assert '"course_vivante": true' in f[f"{b}/garde-a1-v3-troisieme.jsonl"]
    jamais_de_secret(f)
    assert gestes(r) == [["detruire", 90000001]]
    assert (r.travail / "ETAT").read_text().strip() == "verse"


def test_fin_propre_quel_que_soit_le_code_du_lanceur(monde):
    r, env, nu = monde({"code": 3})
    assert h.Machine(r, env).principal() == 0
    assert branche(nu, h.BRANCHE_DONNEES)[f"{h.BRANCHE_DONNEES}/code-sortie-lanceur.txt"].strip() == "3"
    assert gestes(r) == [["detruire", 90000001]]


def test_plafond_de_duree_de_la_machine(monde):
    r, env, nu = monde({"code": 0, "duree_s": 60})
    r.duree_max_s = 1.0
    assert h.Machine(r, env).principal() == 0
    f = branche(nu, h.BRANCHE_DONNEES)
    j = f[f"{h.BRANCHE_DONNEES}/journal-hote-a1-v3-troisieme-v1.log"]
    assert "PLAFOND DE LA MACHINE atteint" in j and "arrêt de course par son identifiant" in j
    assert "arrêt au plafond de la machine" in f[f"{h.BRANCHE_DONNEES}/code-sortie-lanceur.txt"]
    assert gestes(r) == [["detruire", 90000001]]


def test_plafond_de_depense_de_la_machine(monde):
    r, env, nu = monde({"code": 0, "duree_s": 60})
    r.plafond_machine_usd = 0.00005  # à 0,2 USD/h : atteint en moins d'une seconde
    assert h.Machine(r, env).principal() == 0
    assert "PLAFOND DE LA MACHINE" in branche(nu, h.BRANCHE_DONNEES)[f"{h.BRANCHE_DONNEES}/journal-hote-a1-v3-troisieme-v1.log"]


def test_reprise_du_conteneur_ne_relance_rien(monde, tmp_path):
    r, env, nu = monde({"code": 0})
    r.travail.mkdir()
    (r.travail / "ETAT").write_text("course\n")
    (r.travail / "journal-hote-a1-v3-troisieme-v1.log").write_text("départ antérieur\n")
    assert h.Machine(r, env).principal() == 0
    assert not (tmp_path / "courses-lancees").exists()  # aucun lanceur parti
    f = branche(nu, h.BRANCHE_INTERROMPUE)
    assert "REPRISE du conteneur" in f[f"{h.BRANCHE_INTERROMPUE}/journal-hote-a1-v3-troisieme-v1.log"]
    assert branche(nu, h.BRANCHE_DONNEES) == {}
    assert gestes(r) == [["detruire", 90000001]]


def test_reprise_apres_versement_detruit_seulement(monde):
    r, env, nu = monde({"code": 0})
    assert h.Machine(r, env).principal() == 0
    assert h.Machine(r, env).principal() == 0
    assert gestes(r) == [["detruire", 90000001], ["detruire", 90000001]]
    assert branche(nu, h.BRANCHE_INTERROMPUE) == {}


@pytest.mark.parametrize("option, motif", [
    ({"sha_texte_faux": True}, "texte v3 : empreinte"),
    ({"code_hors_lignee": True}, "ne descend pas du code gelé"),
    ({"piece_fausse": True}, "pièce donnees/espece-seule-v1/collisionneur_v7.py"),
    ({"registre_source": ("# R\n\n" + ENTETE + LIGNE_06 + LIGNE_06).encode()}, "en double"),
    ({"registre_source": ("# R\n\n" + ENTETE).encode()}, "absent"),
    ({"comportement": {"verifier": 2}}, "--verifier-seulement en code 2"),
])
def test_refus_avant_la_course_rien_ne_part(monde, tmp_path, option, motif):
    r, env, nu = monde(**option)
    assert h.Machine(r, env).principal() == 0
    assert not (tmp_path / "courses-lancees").exists()
    f = branche(nu, h.BRANCHE_REFUS)
    j = f[f"{h.BRANCHE_REFUS}/journal-hote-a1-v3-troisieme-v1.log"]
    assert "REFUS" in j and motif in j, j[-600:]
    jamais_de_secret(f)
    assert gestes(r) == [["detruire", 90000001]]


def test_go_refuse_sur_la_machine(monde, tmp_path):
    r, env, nu = monde()
    env["GO_ID"] = "GO-2026-11-03-01"
    assert h.Machine(r, env).principal() == 0
    assert "aucun autre GO" in branche(nu, h.BRANCHE_REFUS)[f"{h.BRANCHE_REFUS}/journal-hote-a1-v3-troisieme-v1.log"]
    assert not (tmp_path / "courses-lancees").exists()


def test_port_deja_pris_refuse(monde, tmp_path):
    r, env, nu = monde()
    with socket.socket() as s:
        s.bind(("127.0.0.1", r.port))
        s.listen()
        assert h.Machine(r, env).principal() == 0
    assert "déjà pris" in branche(nu, h.BRANCHE_REFUS)[f"{h.BRANCHE_REFUS}/journal-hote-a1-v3-troisieme-v1.log"]


def test_relais_mort_relance_jamais_arrete(monde):
    r, env, nu = monde({"code": 0, "duree_s": 3, "relais_meurt": True})
    assert h.Machine(r, env).principal() == 0
    j = branche(nu, h.BRANCHE_DONNEES)[f"{h.BRANCHE_DONNEES}/journal-hote-a1-v3-troisieme-v1.log"]
    assert "relais mort (code 9) : relancé avec les mêmes réglages" in j and "fin du lanceur : code 0" in j


def test_fuite_d_un_secret_rien_verse_machine_arretee(monde):
    r, env, nu = monde({"code": 0, "fuite": True})
    assert h.Machine(r, env).principal() == 3
    assert branche(nu, h.BRANCHE_DONNEES) == {}
    j = (r.travail / "journal-hote-a1-v3-troisieme-v1.log").read_text()
    assert "valeur de secret trouvée dans ['relais-argon-journal-a1-v3-troisieme.jsonl']" in j and CLE not in j
    assert gestes(r) == [["arreter", 90000001]]


def test_branche_deja_presente_rien_ecrase_machine_arretee(monde, tmp_path):
    r, env, nu = monde({"code": 0})
    run("git", "push", "-q", str(nu), f"refs/remotes/origin/main:refs/heads/{h.BRANCHE_DONNEES}", cwd=r.clone_prive)
    assert h.Machine(r, env).principal() == 3
    assert "déjà présente (R12)" in (r.travail / "journal-hote-a1-v3-troisieme-v1.log").read_text()
    assert gestes(r) == [["arreter", 90000001]]


def test_identifiant_de_machine_illisible_aucun_geste(monde):
    r, env, nu = monde({"code": 0})
    env["CONTAINER_ID"] = "90000001; rm -rf /"
    assert h.Machine(r, env).principal() == 4
    assert gestes(r) == []


@pytest.mark.parametrize("retire, motif", [("CLE_ARGON", "CLE_ARGON absente"), (None, "au lieu de GO-2026-11-04-06")])
def test_amorce_refuse_sans_variable_ou_autre_go(tmp_path, retire, motif):
    env = {"PATH": os.environ["PATH"], "COMMIT_PRIVE": "a" * 40, "COMMIT_PUBLIC": "b" * 40, "SHA_TEXTE": "c" * 64,
           "COMMIT_REGISTRE": "d" * 40, "GO_ID": "GO-2026-11-04-06", "PRIX_H_USD": "0.2", "CLE_ARGON": CLE,
           "GH_TOKEN": JETON, "RACINE_AMORCE": str(tmp_path), "SAUTER_INSTALLATION": "1"}
    if retire:
        env.pop(retire)
    else:
        env["GO_ID"] = "GO-2026-11-03-01"
    r = subprocess.run(["bash", str(RACINE / "scripts" / "amorce_hote_durable_a1_v3_v1.sh")], env=env, capture_output=True,
                       text=True)
    assert r.returncode == 2 and motif in r.stdout and CLE not in r.stdout + r.stderr
