"""Dépôt d'empreintes sur l'Open Science Framework (`scripts/osf_depot_v1.py`) : `manifeste` sur un arbre factice
(cas sain ; artefacts : fichier sans compagnon, fichier non commis → refus, R5) ; `deposer` contre un faux serveur HTTP
local (cas sain, idempotence ; artefact : réponse illisible → arrêt sans nouvelle tentative). Aucune clé réelle n'est
lue : le jeton des essais est factice, posé par `monkeypatch`, et ne doit jamais apparaître dans les sorties."""
from __future__ import annotations

import hashlib
import importlib.util
import json
import re
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import pytest

from conftest import committer
from controle_ia.scellement import sceller

RACINE = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("osf_depot_v1", RACINE / "scripts" / "osf_depot_v1.py")
od = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(od)

JETON_FACTICE = "jeton-factice-qui-ne-doit-jamais-sortir"


# --------------------------------------------------------------------------- arbre factice
def _arbre(depot: Path) -> dict[str, str]:
    """Trois dossiers, un fichier scellé par dossier, commis ; renvoie chemin → sha256."""
    attendus = {}
    for rel, texte in [("prereg/P-1-v1.md", "# préenregistrement\n"),
                       ("docs/verdicts/verdict-X-v1.md", "# verdict\n"),
                       ("docs/decisions/decision-N-1-v1.md", "# décision\n")]:
        p = depot / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(texte, encoding="utf-8")
        attendus[rel] = sceller(p)
    (depot / "prereg" / "config-v1.json").write_text("{}\n")          # ni .md ni scellé : ignoré
    committer(depot)
    return attendus


def test_manifeste_cas_sain_arbre_et_ref(depot, monkeypatch):
    attendus = _arbre(depot)
    monkeypatch.delenv(od.NOM_JETON, raising=False)                   # aucun jeton nécessaire sans réseau
    sortie = depot / "livrables" / "osf-manifeste-v1" / "manifeste-v1.json"
    assert od.main(["manifeste", "--racine", str(depot), "--sortie", str(sortie)]) == 0
    m = json.loads(sortie.read_text(encoding="utf-8"))
    assert m["version"] == od.VERSION_MANIFESTE and m["nombre"] == 3 and m["exclus"] == []
    assert {f["chemin"]: f["sha256"] for f in m["fichiers"]} == attendus
    tete = od.git(depot, "rev-parse", "HEAD").strip()
    assert all(f["commit"] == tete and f["compagnon"] == f["chemin"] + ".sha256" for f in m["fichiers"])
    lisezmoi = sortie.parent / od.NOM_LISEZMOI
    assert "n'a pas été modifié après la date de dépôt" in lisezmoi.read_text(encoding="utf-8")
    assert not list(sortie.parent.glob("*.sha256"))                   # le script ne scelle rien (la mère scelle)
    # déterminisme : un second appel produit le même fichier, et ne refuse pas (même contenu)
    premier = sortie.read_bytes()
    assert od.main(["manifeste", "--racine", str(depot), "--sortie", str(sortie)]) == 0
    assert sortie.read_bytes() == premier
    # lecture par référence git : mêmes empreintes, source nommée, commit de la référence consigné
    sortie_ref = depot / "livrables" / "osf-manifeste-v1" / "manifeste-ref-v1.json"
    assert od.main(["manifeste", "--racine", str(depot), "--ref", "main", "--sortie", str(sortie_ref)]) == 0
    mr = json.loads(sortie_ref.read_text(encoding="utf-8"))
    assert {f["chemin"]: f["sha256"] for f in mr["fichiers"]} == attendus
    assert mr["references"] == {"main": tete} and all(f["source"] == "main" for f in mr["fichiers"])


def test_manifeste_refuse_fichier_sans_compagnon(depot, capsys):
    _arbre(depot)
    (depot / "prereg" / "brouillon-v1.md").write_text("# brouillon non scellé\n", encoding="utf-8")
    committer(depot)
    sortie = depot / "livrables" / "osf-manifeste-v1" / "manifeste-v1.json"
    for args in (["manifeste", "--racine", str(depot), "--sortie", str(sortie)],
                 ["manifeste", "--racine", str(depot), "--ref", "main", "--sortie", str(sortie)]):
        assert od.main(args) == 1
        err = capsys.readouterr().err
        assert "ARRÊT" in err and "brouillon-v1.md" in err and "aucun compagnon" in err
        assert not sortie.exists()                                    # rien n'est écrit
    # l'exclusion explicite n'est pas un repli silencieux : le fichier est listé dans le manifeste et imprimé
    assert od.main(["manifeste", "--racine", str(depot), "--ref", "main", "--ignorer-non-scelles",
                    "--sortie", str(sortie)]) == 0
    m = json.loads(sortie.read_text(encoding="utf-8"))
    assert m["nombre"] == 3 and [x["chemin"] for x in m["exclus"]] == ["prereg/brouillon-v1.md"]
    assert "EXCLU main:prereg/brouillon-v1.md" in capsys.readouterr().out


def test_manifeste_refuse_fichier_altere_ou_non_commis(depot, capsys):
    _arbre(depot)
    sortie = depot / "livrables" / "osf-manifeste-v1" / "manifeste-v1.json"
    p = depot / "prereg" / "P-2-v1.md"
    p.write_text("# scellé mais pas commis\n", encoding="utf-8")
    sceller(p)
    assert od.main(["manifeste", "--racine", str(depot), "--sortie", str(sortie)]) == 1
    assert "non commis" in capsys.readouterr().err and not sortie.exists()
    committer(depot)
    p.write_text("# altéré après scellement\n", encoding="utf-8")   # empreinte ≠ compagnon : arrêt dur
    committer(depot)
    assert od.main(["manifeste", "--racine", str(depot), "--ignorer-non-scelles", "--sortie", str(sortie)]) == 1
    assert "altéré" in capsys.readouterr().err and not sortie.exists()


# --------------------------------------------------------------------------- faux serveur
class FauxOSF:
    """Interface v2 et service de fichiers factices, en mémoire. `mode` : « sain » ou « illisible »."""

    def __init__(self, mode: str = "sain"):
        self.mode = mode
        self.projets: dict[str, dict] = {}
        self.fichiers: dict[str, dict[str, dict]] = {}
        self.requetes: list[tuple[str, str, dict]] = []
        serveur = self

        class H(BaseHTTPRequestHandler):
            def log_message(self, *a):  # silence
                pass

            def _repondre(self, statut: int, corps: bytes, type_contenu="application/vnd.api+json"):
                self.send_response(statut)
                self.send_header("Content-Type", type_contenu)
                self.send_header("Content-Length", str(len(corps)))
                self.end_headers()
                self.wfile.write(corps)

            def _json(self, statut, doc):
                self._repondre(statut, json.dumps(doc, ensure_ascii=False).encode("utf-8"))

            def _traiter(self):
                u = urlparse(self.path)
                n = int(self.headers.get("Content-Length") or 0)
                corps = self.rfile.read(n) if n else b""
                serveur.requetes.append((self.command, self.path, dict(self.headers)))
                if self.headers.get("Authorization") != f"Bearer {JETON_FACTICE}":
                    return self._json(401, {"errors": [{"detail": "jeton refusé"}]})
                base = f"http://{self.headers['Host']}"
                if self.command == "GET" and u.path == "/v2/users/me/":
                    return self._json(200, {"data": {"id": "u5er1", "type": "users",
                                                     "attributes": {"full_name": "Utilisateur Factice"}}})
                if self.command == "GET" and u.path == "/v2/users/me/nodes/":
                    if serveur.mode == "illisible":
                        return self._repondre(200, b"<html>pas du JSON</html>", "text/html")
                    return self._json(200, {"data": list(serveur.projets.values()), "links": {"next": None}})
                if self.command == "POST" and u.path == "/v2/nodes/":
                    attr = json.loads(corps)["data"]["attributes"]
                    ident = f"n0d{len(serveur.projets) + 1}"
                    serveur.projets[ident] = {"id": ident, "type": "nodes",
                                              "attributes": {"title": attr["title"], "public": attr.get("public", False)},
                                              "links": {"html": f"https://osf.example/{ident}/"}}
                    serveur.fichiers[ident] = {}
                    return self._json(201, {"data": serveur.projets[ident]})
                m = re.fullmatch(r"/v2/nodes/(\w+)/", u.path)
                if self.command == "PATCH" and m:
                    p = serveur.projets[m.group(1)]
                    p["attributes"]["public"] = json.loads(corps)["data"]["attributes"]["public"]
                    return self._json(200, {"data": p})
                m = re.fullmatch(r"/v2/nodes/(\w+)/files/", u.path)
                if self.command == "GET" and m:
                    ident = m.group(1)
                    return self._json(200, {"data": [{"id": f"{ident}:osfstorage", "type": "files",
                                                      "attributes": {"provider": "osfstorage", "kind": "folder"},
                                                      "links": {"upload": f"{base}/v1/resources/{ident}/providers/osfstorage/"}}]})
                m = re.fullmatch(r"/v2/nodes/(\w+)/files/osfstorage/", u.path)
                if self.command == "GET" and m:
                    return self._json(200, {"data": list(serveur.fichiers[m.group(1)].values())})
                m = re.fullmatch(r"/v1/resources/(\w+)/providers/osfstorage/", u.path)
                if self.command == "PUT" and m:
                    q = parse_qs(u.query)
                    nom, ident = q["name"][0], m.group(1)
                    sha = hashlib.sha256(corps).hexdigest()
                    fid = f"{ident}f{len(serveur.fichiers[ident]) + 1}"
                    serveur.fichiers[ident][nom] = {
                        "id": fid, "type": "files",
                        "attributes": {"name": nom, "kind": "file", "size": len(corps),
                                       "date_created": "2026-11-05T16:30:00.000000Z",
                                       "date_modified": "2026-11-05T16:30:00.000000Z",
                                       "extra": {"hashes": {"sha256": sha, "md5": hashlib.md5(corps).hexdigest()}}},
                        "links": {"upload": f"{base}/v1/resources/{ident}/providers/osfstorage/{fid}"}}
                    return self._json(201, {"data": {"attributes": {"name": nom, "kind": "file",
                                                                    "extra": {"hashes": {"sha256": sha}}}}})
                return self._json(404, {"errors": [{"detail": f"inconnu : {self.command} {self.path}"}]})

            do_GET = do_POST = do_PUT = do_PATCH = _traiter

        self.httpd = ThreadingHTTPServer(("127.0.0.1", 0), H)
        self.url = f"http://127.0.0.1:{self.httpd.server_address[1]}/v2"
        self.fil = threading.Thread(target=self.httpd.serve_forever, daemon=True)
        self.fil.start()

    def arreter(self):
        self.httpd.shutdown()
        self.httpd.server_close()


@pytest.fixture
def faux(request):
    s = FauxOSF(getattr(request, "param", "sain"))
    yield s
    s.arreter()


def _manifeste_pret(depot) -> Path:
    _arbre(depot)
    sortie = depot / "livrables" / "osf-manifeste-v1" / "manifeste-v1.json"
    assert od.main(["manifeste", "--racine", str(depot), "--sortie", str(sortie)]) == 0
    return sortie


def test_deposer_a_blanc(faux, monkeypatch, capsys):
    monkeypatch.setenv(od.NOM_JETON, JETON_FACTICE)
    assert od.main(["deposer", "--a-blanc", "--api", faux.url]) == 0
    sortie = capsys.readouterr()
    assert sortie.out.strip() == "Utilisateur Factice"                     # le nom, rien d'autre
    assert [(m, p) for m, p, _ in faux.requetes] == [("GET", "/v2/users/me/")]
    assert JETON_FACTICE not in sortie.out + sortie.err and faux.projets == {}


def test_deposer_cas_sain_puis_idempotent(depot, faux, monkeypatch, capsys):
    sortie = _manifeste_pret(depot)
    capsys.readouterr()
    monkeypatch.setenv(od.NOM_JETON, JETON_FACTICE)
    assert od.main(["deposer", "--api", faux.url, "--manifeste", str(sortie)]) == 0
    s1 = capsys.readouterr()
    assert "projet créé : n0d1 (privé)" in s1.out and "identifiant du projet : n0d1" in s1.out
    assert "adresse              : https://osf.example/n0d1/" in s1.out
    assert "date de dépôt (interface) : 2026-11-05T16:30:00.000000Z" in s1.out
    sha_local = hashlib.sha256(sortie.read_bytes()).hexdigest()
    assert f"sha256 relue (interface)  : {sha_local}" in s1.out and "ÉCART" not in s1.out
    assert s1.out.count("CONFORME") == 2 and "fichiers nouveaux    : 2" in s1.out
    assert set(faux.fichiers["n0d1"]) == {"manifeste-v1.json", "LISEZMOI.md"}
    assert faux.projets["n0d1"]["attributes"]["public"] is False
    assert sum(m == "PUT" for m, _, _ in faux.requetes) == 2
    assert JETON_FACTICE not in s1.out + s1.err
    # second dépôt du même manifeste : rien de nouveau, et le script le dit
    del faux.requetes[:]
    assert od.main(["deposer", "--api", faux.url, "--manifeste", str(sortie)]) == 0
    s2 = capsys.readouterr()
    assert "projet réutilisé : n0d1" in s2.out and "rien de nouveau" in s2.out
    assert "fichiers nouveaux    : 0 (second dépôt du même manifeste : rien créé)" in s2.out
    assert not any(m in ("PUT", "POST") for m, _, _ in faux.requetes) and len(faux.projets) == 1
    assert JETON_FACTICE not in s2.out + s2.err
    # un manifeste différent sous le même nom : refus (R12), rien téléversé
    sortie.write_text(sortie.read_text(encoding="utf-8").replace('"nombre": 3', '"nombre": 3 '), encoding="utf-8")
    del faux.requetes[:]
    assert od.main(["deposer", "--api", faux.url, "--manifeste", str(sortie)]) == 1
    s3 = capsys.readouterr()
    assert "autre empreinte" in s3.err and not any(m == "PUT" for m, _, _ in faux.requetes)
    # --public rend public le projet existant (le manifeste est d'abord remis dans son état déposé)
    sortie.write_text(sortie.read_text(encoding="utf-8").replace('"nombre": 3 ', '"nombre": 3'), encoding="utf-8")
    assert od.main(["deposer", "--api", faux.url, "--manifeste", str(sortie), "--public"]) == 0
    assert faux.projets["n0d1"]["attributes"]["public"] is True
    assert "visibilité           : public" in capsys.readouterr().out


@pytest.mark.parametrize("faux", ["illisible"], indirect=True)
def test_deposer_reponse_illisible_arrete_sans_retenter(depot, faux, monkeypatch, capsys):
    sortie = _manifeste_pret(depot)
    capsys.readouterr()
    monkeypatch.setenv(od.NOM_JETON, JETON_FACTICE)
    assert od.main(["deposer", "--api", faux.url, "--manifeste", str(sortie)]) == 1
    s = capsys.readouterr()
    assert "ARRÊT" in s.err and "réponse illisible" in s.err and "aucune nouvelle tentative" in s.err
    assert [(m, p.split("?")[0]) for m, p, _ in faux.requetes] == [("GET", "/v2/users/me/nodes/")]   # une seule fois
    assert faux.projets == {} and JETON_FACTICE not in s.out + s.err


def test_deposer_erreur_interface_sans_en_tete(faux, monkeypatch, capsys):
    monkeypatch.setenv(od.NOM_JETON, "mauvais-jeton-factice")
    assert od.main(["deposer", "--a-blanc", "--api", faux.url]) == 1
    s = capsys.readouterr()
    assert "ERREUR DE L'INTERFACE : statut 401" in s.err and "jeton refusé" in s.err
    assert "mauvais-jeton-factice" not in s.out + s.err and "Authorization" not in s.out + s.err


def test_sans_jeton_rien_n_est_tente(faux, monkeypatch, capsys):
    monkeypatch.delenv(od.NOM_JETON, raising=False)
    assert od.main(["deposer", "--a-blanc", "--api", faux.url]) == 1
    assert od.NOM_JETON in capsys.readouterr().err and faux.requetes == []
