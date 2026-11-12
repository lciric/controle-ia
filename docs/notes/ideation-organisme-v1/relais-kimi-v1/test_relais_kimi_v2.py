"""Essais de `relais_kimi_v2.py`. (1) **Tous les essais de la v1** rejoués sur la v2 : le module d'essais de la v1 est
importé, son module et son chemin de relais sont pointés vers la v2, et ses fonctions d'essai sont recueillies ici. Un
seul essai de la v1 est redéfini : le cas sain, qui attend la version « relais-kimi-v1 » dans `/relais/etat` ; ici, il
attend « relais-kimi-v2 », et rien d'autre ne change. (2) Les essais de l'option `--lister-modeles`, devant un faux amont
local qui sert `GET /v1/models`. Aucun réseau sortant, aucune vraie clé, aucun appel payant.

Lancer (depuis la racine du dépôt) : `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m pytest -q -p no:cacheprovider
docs/notes/ideation-organisme-v1/relais-kimi-v1/test_relais_kimi_v2.py`.
"""

import json
import os
import subprocess
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import pytest

import relais_kimi_v2
import test_relais_kimi_v1 as v1

ICI = os.path.dirname(os.path.abspath(__file__))
RELAIS_V2 = os.path.join(ICI, "relais_kimi_v2.py")

# (1) les essais de la v1, pointés vers la v2
v1.relais = relais_kimi_v2
v1.RELAIS = RELAIS_V2
from test_relais_kimi_v1 import *  # noqa: E402,F401,F403 — fonctions d'essai et accessoires de la v1, rejoués sur la v2
from test_relais_kimi_v1 import CLE_REELLE, MODELE, amont, appeler, etat, relais_proc  # noqa: E402,F401


def test_cas_sain_cle_posee_reponse_relayee_cout_compte(amont, relais_proc):  # noqa: F811 — redéfini : version v2
    statut, en_tetes, octets = appeler(relais_proc.url, en_tetes={"x-api-key": "cle-client-2", "X-Essai": "passe"})
    assert statut == 200 and json.loads(octets) == amont.objet
    (r,) = amont.requetes
    assert r["en_tetes"]["authorization"] == "Bearer " + CLE_REELLE and "x-api-key" not in r["en_tetes"]
    e = etat(relais_proc.url)
    assert e["appels"] == 1 and e["refus"] == 0 and e["refus_modele"] == 0 and e["modeles_permis"] == [MODELE]
    assert e["depense_usd"] == pytest.approx(v1.COUT_USAGE)
    assert e["version"] == "relais-kimi-v2"


def test_les_essais_de_la_v1_visent_bien_la_v2():
    assert v1.relais is relais_kimi_v2 and v1.RELAIS == RELAIS_V2


# (2) --lister-modeles --------------------------------------------------------------------------------------------------

class FauxAmontModeles:
    """Sert `GET /v1/models` ; consigne chaque requête ; `code`, `brut` réglables."""

    def __init__(self):
        self.requetes, self.code, self.brut = [], 200, None
        self.objet = {"object": "list", "data": [{"id": "kimi-k3.1-pro", "object": "model", "owned_by": "moonshot"},
                                                 {"id": "kimi-k2.5", "object": "model", "owned_by": "moonshot"}]}
        faux = self

        class Gestion(BaseHTTPRequestHandler):
            protocol_version = "HTTP/1.1"

            def log_message(self, *a):
                pass

            def _repondre(self):
                faux.requetes.append({"methode": self.command, "chemin": self.path,
                                      "en_tetes": {k.lower(): v for k, v in self.headers.items()}})
                brut = faux.brut if faux.brut is not None else json.dumps(faux.objet).encode("utf-8")
                self.send_response(faux.code)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(brut)))
                self.end_headers()
                self.wfile.write(brut)

            do_GET = do_POST = _repondre

        self.serveur = ThreadingHTTPServer(("127.0.0.1", 0), Gestion)
        self.serveur.daemon_threads = True
        self.url = f"http://127.0.0.1:{self.serveur.server_address[1]}"
        threading.Thread(target=self.serveur.serve_forever, daemon=True).start()

    def fermer(self):
        self.serveur.shutdown()
        self.serveur.server_close()


@pytest.fixture
def amont_modeles():
    a = FauxAmontModeles()
    yield a
    a.fermer()


def lister(amont_url, cle=CLE_REELLE, extra=()):
    env = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "LANG": "C.UTF-8"}
    if cle is not None:
        env["KIMI_API_KEY"] = cle
    p = subprocess.run([sys.executable, "-I", "-B", RELAIS_V2, "--lister-modeles", "--amont", amont_url, *extra],
                       env=env, capture_output=True, text=True, timeout=30)
    return p.returncode, p.stdout, p.stderr


def test_lister_imprime_seulement_les_identifiants_tries(amont_modeles):
    code, sortie, erreurs = lister(amont_modeles.url)
    assert code == 0 and sortie.splitlines() == ["kimi-k2.5", "kimi-k3.1-pro"] and erreurs == ""
    assert "moonshot" not in sortie and "object" not in sortie, "seulement les identifiants"
    assert CLE_REELLE not in sortie + erreurs


def test_lister_fait_un_seul_appel_get_v1_models_avec_la_cle(amont_modeles):
    lister(amont_modeles.url)
    (r,) = amont_modeles.requetes
    assert r["methode"] == "GET" and r["chemin"] == "/v1/models"
    assert r["en_tetes"]["authorization"] == "Bearer " + CLE_REELLE


def test_lister_sans_les_reglages_du_service(amont_modeles):
    """En mode liste, --modeles-permis, --plafond-usd et les prix ne sont pas exigés."""
    code, sortie, _ = lister(amont_modeles.url)
    assert code == 0 and "kimi-k3.1-pro" in sortie


@pytest.mark.parametrize("code_amont", [401, 403, 500])
def test_lister_statut_non_200_code_3_corps_non_recopie(amont_modeles, code_amont):
    amont_modeles.code = code_amont
    amont_modeles.brut = json.dumps({"error": {"message": "CORPS-SECRET " + CLE_REELLE}}).encode("utf-8")
    code, sortie, erreurs = lister(amont_modeles.url)
    assert code == 3 and sortie == "" and f"statut {code_amont}" in erreurs
    assert "CORPS-SECRET" not in erreurs and CLE_REELLE not in sortie + erreurs


@pytest.mark.parametrize("brut", [b"pas du json", b"{}", b'{"data": "x"}', b'{"data": []}', b'{"data": [{"nom": 1}]}'])
def test_lister_reponse_illisible_ou_vide_code_3(amont_modeles, brut):
    amont_modeles.brut = brut
    code, sortie, erreurs = lister(amont_modeles.url)
    assert code == 3 and sortie == "" and CLE_REELLE not in erreurs


def test_lister_cle_absente_code_2_sans_appel(amont_modeles):
    code, sortie, erreurs = lister(amont_modeles.url, cle=None)
    assert code == 2 and sortie == "" and "aucune clé dans la variable KIMI_API_KEY" in erreurs
    assert amont_modeles.requetes == []


def test_lister_amont_injoignable_code_3():
    code, sortie, erreurs = lister("http://127.0.0.1:1")
    assert code == 3 and sortie == "" and "injoignable" in erreurs and CLE_REELLE not in erreurs


def test_lister_amont_invalide_code_2(amont_modeles):
    code, _, erreurs = lister("https://api.moonshot.ai/v1")
    assert code == 2 and "--amont" in erreurs


def test_service_sans_reglages_obligatoires_refus_code_2(amont_modeles):
    env = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "KIMI_API_KEY": CLE_REELLE}
    p = subprocess.run([sys.executable, "-I", "-B", RELAIS_V2, "--amont", amont_modeles.url, "--port", "0"],
                       env=env, capture_output=True, text=True, timeout=30)
    assert p.returncode == 2 and "--modeles-permis" in p.stderr and "--prix-cache" in p.stderr
    assert CLE_REELLE not in p.stdout + p.stderr and amont_modeles.requetes == []


def test_v1_inchangee():
    """R12 : la v1 garde son nom de version et n'a pas l'option."""
    import relais_kimi_v1
    assert relais_kimi_v1.VERSION == "relais-kimi-v1"
    assert "--lister-modeles" not in relais_kimi_v1.analyseur().format_help()
