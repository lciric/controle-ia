"""Essais de `relais_gemini_v1.py` : le relais est lancé **dans son propre processus** (`python -I -B`) avec une clé
**factice** dans son seul environnement, devant un **faux amont local** (127.0.0.1, port libre) qui consigne ce qu'il reçoit.
Aucun réseau sortant, aucune vraie clé, aucun appel payant.

Cas sains : clé factice du client remplacée par la clé du relais, réponse relayée telle quelle (code, corps, type), compte
d'appels et d'octets dans `/relais/etat`, journal sans clé ni texte, bout en bout `commande_argon_v2.py --url-base` → relais
→ faux Gemini des essais de la commande (`FauxGemini` de `test_commande_argon_v2.py`). Artefacts (R5) : clé reçue du client
(en-tête, `Authorization`, `?key=`) retirée ; modèle hors liste (403, amont jamais appelé) ; chemin inconnu (403) ; bornes
`--max-appels` et `--max-octets-corps` (429, amont jamais appelé), y compris sous appels simultanés ; sans `Content-Length`
(411) ; amont injoignable (502) ; relais sans clé (code 2) ; variable de clé effacée de l'environnement du relais.

Lancer : `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m pytest -q -p no:cacheprovider
docs/notes/ideation-organisme-v1/lancement-v2/test_relais_gemini_v1.py` (depuis la racine du dépôt).
"""

import http.client
import json
import os
import subprocess
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import pytest

import relais_gemini_v1 as relais
from test_commande_argon_v2 import COMMANDE, FauxGemini, env_commande

ICI = os.path.dirname(os.path.abspath(__file__))
RELAIS = os.path.join(ICI, "relais_gemini_v1.py")
CLE_REELLE = "cle-factice-du-relais-AIzaTEST-9876543210-ne-jamais-imprimer"
CLE_CLIENT = "factice-relais"
TEXTE_SECRET = "TEXTE-DE-CONSIGNE-QUI-NE-DOIT-JAMAIS-ETRE-JOURNALISE"
REPONSE_SECRETE = "TEXTE-DE-REPONSE-QUI-NE-DOIT-JAMAIS-ETRE-JOURNALISE"
USAGE = {"promptTokenCount": 1000, "candidatesTokenCount": 10, "thoughtsTokenCount": 5, "totalTokenCount": 1015}


# --- faux amont -------------------------------------------------------------------------------------------------------

class FauxAmont:
    """Consigne chaque requête (chemin complet, tous les en-têtes, corps brut) ; répond selon `code` et `objet`."""

    def __init__(self):
        self.requetes = []
        self.code = 200
        self.objet = {"candidates": [{"content": {"role": "model", "parts": [{"text": REPONSE_SECRETE}]},
                                      "finishReason": "STOP"}], "modelVersion": "gemini-4-argon",
                      "usageMetadata": dict(USAGE)}
        self.attente_s = 0.0
        faux = self

        class Gestion(BaseHTTPRequestHandler):
            protocol_version = "HTTP/1.1"

            def log_message(self, *a):
                pass

            def do_POST(self):
                n = int(self.headers.get("Content-Length") or 0)
                corps = self.rfile.read(n)
                faux.requetes.append({"chemin": self.path, "en_tetes": {k.lower(): v for k, v in self.headers.items()},
                                      "corps": corps})
                if faux.attente_s:
                    time.sleep(faux.attente_s)
                brut = json.dumps(faux.objet).encode("utf-8")
                try:
                    self.send_response(faux.code)
                    self.send_header("Content-Type", "application/json; charset=UTF-8")
                    self.send_header("X-Temoin-Amont", "relaye")
                    self.send_header("Content-Length", str(len(brut)))
                    self.end_headers()
                    self.wfile.write(brut)
                except (BrokenPipeError, ConnectionResetError):
                    pass

        self.serveur = ThreadingHTTPServer(("127.0.0.1", 0), Gestion)
        self.serveur.daemon_threads = True
        self.url = f"http://127.0.0.1:{self.serveur.server_address[1]}"
        threading.Thread(target=self.serveur.serve_forever, daemon=True).start()

    def arreter(self):
        self.serveur.shutdown()
        self.serveur.server_close()


@pytest.fixture
def amont():
    a = FauxAmont()
    yield a
    a.arreter()


# --- lancement du relais dans son processus ---------------------------------------------------------------------------

def lancer_relais(amont_url, journal=None, cle=CLE_REELLE, variable="GEMINI_API_KEY", args=()):
    """Rend (processus, url ou None, première ligne de sortie)."""
    env = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "LANG": "C.UTF-8"}
    if cle is not None:
        env[variable] = cle
    ligne_cmd = [sys.executable, "-I", "-B", RELAIS, "--port", "0", "--amont", amont_url, *args]
    if journal:
        ligne_cmd += ["--journal", journal]
    proc = subprocess.Popen(ligne_cmd, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    ligne = proc.stdout.readline()
    if not ligne.startswith("relais prêt sur "):
        try:
            sortie, erreurs = proc.communicate(timeout=10)
        except subprocess.TimeoutExpired:
            proc.kill()
            sortie, erreurs = proc.communicate(timeout=10)
        return proc, None, ligne + sortie + erreurs
    return proc, ligne.split()[3], ligne


class Relais:
    def __init__(self, amont_url, tmp_path, args=()):
        self.journal = str(tmp_path / "journal-relais-gemini.jsonl")
        self.proc, self.url, self.premiere_ligne = lancer_relais(amont_url, self.journal, args=args)
        assert self.url, self.premiere_ligne
        assert CLE_REELLE not in self.premiere_ligne

    def arreter(self):
        self.proc.kill()
        sortie, erreurs = self.proc.communicate(timeout=10)
        assert CLE_REELLE not in self.premiere_ligne + sortie + erreurs, "la clé ne sort jamais du relais"

    def entrees_journal(self, au_moins=1):
        limite = time.time() + 3.0
        while True:
            entrees = []
            if os.path.exists(self.journal):
                with open(self.journal, encoding="utf-8") as f:
                    entrees = [json.loads(l) for l in f if l.strip()]
            if len(entrees) >= au_moins or time.time() > limite:
                return entrees

    def journal_brut(self):
        return open(self.journal, encoding="utf-8").read() if os.path.exists(self.journal) else ""


@pytest.fixture
def relais_proc(amont, tmp_path):
    r = Relais(amont.url, tmp_path)
    yield r
    r.arreter()


def appeler(url, chemin, corps=None, cle=CLE_CLIENT, methode="POST", en_tetes=None, sans_longueur=False):
    hote, port = url.replace("http://", "").split(":")
    c = http.client.HTTPConnection(hote, int(port), timeout=30)
    h = {"Content-Type": "application/json"}
    if cle is not None:
        h["x-goog-api-key"] = cle
    h.update(en_tetes or {})
    donnees = json.dumps(corps).encode("utf-8") if isinstance(corps, dict) else corps
    if sans_longueur:
        c.putrequest(methode, chemin, skip_accept_encoding=True)
        for k, v in h.items():
            c.putheader(k, v)
        c.endheaders()
    else:
        c.request(methode, chemin, body=donnees, headers=h)
    r = c.getresponse()
    octets = r.read()
    en_tetes_r = {k.lower(): v for k, v in r.getheaders()}
    c.close()
    return r.status, en_tetes_r, octets


def etat(url):
    statut, _, octets = appeler(url, "/relais/etat", methode="GET", cle=None)
    assert statut == 200
    return json.loads(octets)


CHEMIN_GEN = "/v1beta/models/gemini-4-argon:generateContent"
CHEMIN_COMPTE = "/v1beta/models/gemini-4-argon:countTokens"
CORPS = {"contents": [{"role": "user", "parts": [{"text": TEXTE_SECRET}]}],
         "generationConfig": {"maxOutputTokens": 100, "thinkingConfig": {"thinkingBudget": 8192}}}


# === cas sains ==========================================================================================================

def test_cle_remplacee_et_reponse_relayee_telle_quelle(amont, relais_proc):
    statut, en_tetes, octets = appeler(relais_proc.url, CHEMIN_GEN, CORPS)
    assert statut == 200 and json.loads(octets) == amont.objet
    assert en_tetes["content-type"] == "application/json; charset=UTF-8" and en_tetes["x-temoin-amont"] == "relaye"
    (r,) = amont.requetes
    assert r["chemin"] == CHEMIN_GEN and json.loads(r["corps"]) == CORPS, "corps relayé tel quel"
    assert r["en_tetes"]["x-goog-api-key"] == CLE_REELLE, "la clé factice du client est remplacée par celle du relais"
    assert r["en_tetes"]["content-type"] == "application/json"
    assert r["en_tetes"]["accept-encoding"] == "identity"


def test_count_tokens_relaye(amont, relais_proc):
    amont.objet = {"totalTokens": 1234}
    statut, _, octets = appeler(relais_proc.url, CHEMIN_COMPTE, {"contents": CORPS["contents"]})
    assert statut == 200 and json.loads(octets) == {"totalTokens": 1234}
    (r,) = amont.requetes
    assert r["chemin"] == CHEMIN_COMPTE and r["en_tetes"]["x-goog-api-key"] == CLE_REELLE
    (e,) = relais_proc.entrees_journal()
    assert e["action"] == "countTokens" and e["totalTokens"] == 1234 and e["statut_amont"] == 200


def test_code_et_corps_d_erreur_amont_relayes(amont, relais_proc):
    amont.code, amont.objet = 400, {"error": {"code": 400, "status": "INVALID_ARGUMENT", "message": "refus"}}
    statut, _, octets = appeler(relais_proc.url, CHEMIN_GEN, CORPS)
    assert statut == 400 and json.loads(octets) == amont.objet
    (e,) = relais_proc.entrees_journal()
    assert e["statut_amont"] == 400 and e["statut_erreur_amont"] == "INVALID_ARGUMENT"
    assert etat(relais_proc.url)["reponses_par_statut"] == {"400": 1}


def test_etat_appels_refus_octets(amont, relais_proc):
    e0 = etat(relais_proc.url)
    assert e0["appels"] == 0 and e0["refus"] == 0 and e0["octets_envoyes"] == 0 and e0["octets_recus"] == 0
    assert e0["max_appels"] == 64 and e0["max_octets_corps"] == 8_000_000 and e0["modeles"] == ["gemini-4-argon"]
    assert e0["amont"] == amont.url and e0["mandataire"] is False and e0["version"] == "relais-gemini-v1"
    corps = json.dumps(CORPS).encode("utf-8")
    appeler(relais_proc.url, CHEMIN_GEN, corps)
    appeler(relais_proc.url, "/v1beta/models/autre:generateContent", corps)
    e1 = etat(relais_proc.url)
    assert e1["appels"] == 1 and e1["refus"] == 1 and e1["appels_restants"] == 63
    assert e1["octets_envoyes"] == len(corps) and e1["octets_recus"] == len(json.dumps(amont.objet).encode("utf-8"))
    assert e1["reponses_par_statut"] == {"200": 1}


def test_journal_sans_cle_ni_texte(amont, relais_proc):
    appeler(relais_proc.url, CHEMIN_GEN, CORPS)
    (e,) = relais_proc.entrees_journal()
    brut = relais_proc.journal_brut()
    assert CLE_REELLE not in brut and CLE_CLIENT not in brut
    assert TEXTE_SECRET not in brut and REPONSE_SECRETE not in brut and '"candidates"' not in brut
    assert e["usageMetadata"] == USAGE and e["modele"] == "gemini-4-argon" and e["modele_servi"] == "gemini-4-argon"
    assert e["chemin"] == CHEMIN_GEN and e["methode"] == "POST" and e["statut_amont"] == 200
    assert e["octets_corps"] == len(json.dumps(CORPS).encode("utf-8")) and e["quand_utc"].endswith("+00:00")
    assert set(e) == {"quand_utc", "duree_s", "methode", "chemin", "modele", "action", "octets_corps", "statut_amont",
                      "octets_reponse", "usageMetadata", "modele_servi"}


def test_variable_de_cle_effacee_de_l_environnement_du_relais(relais_proc):
    assert etat(relais_proc.url)["variable_cle_encore_presente"] is False


def test_lire_cle_efface_la_variable():
    env = {"GEMINI_API_KEY": " " + CLE_REELLE + "\n", "AUTRE": "x"}
    assert relais.lire_cle(env, "GEMINI_API_KEY") == CLE_REELLE
    assert env == {"AUTRE": "x"}
    with pytest.raises(relais.RelaisInvalide):
        relais.lire_cle({"GEMINI_API_KEY": "   "}, "GEMINI_API_KEY")
    with pytest.raises(relais.RelaisInvalide):
        relais.lire_cle({}, "GEMINI_API_KEY")


def test_servir_refuse_si_la_variable_est_encore_la():
    with pytest.raises(relais.RelaisInvalide):
        relais.servir(0, "x", "http://127.0.0.1:1", ["m"], 1, 1, environnement={"GEMINI_API_KEY": "x"})


def test_variable_de_cle_au_choix(amont):
    proc, url, sortie = lancer_relais(amont.url, args=("--variable-cle", "CLE_RELAIS_ESSAI"))
    assert url is None and proc.returncode == 2 and "CLE_RELAIS_ESSAI" in sortie, "la clé est dans l'autre variable"
    proc, url, ligne = lancer_relais(amont.url, variable="CLE_RELAIS_ESSAI", args=("--variable-cle", "CLE_RELAIS_ESSAI"))
    try:
        assert url, ligne
        appeler(url, CHEMIN_GEN, CORPS)
        assert amont.requetes[-1]["en_tetes"]["x-goog-api-key"] == CLE_REELLE
    finally:
        proc.kill()
        proc.communicate(timeout=10)


# === artefacts (R5) =====================================================================================================

def test_cle_du_client_retiree_en_tete_authorization_et_parametre(amont, relais_proc):
    chemin = CHEMIN_GEN + "?key=CLE-CLIENT-EN-PARAMETRE&alt=json&access_token=jeton-client"
    statut, _, _ = appeler(relais_proc.url, chemin, CORPS, cle="CLE-CLIENT-EN-EN-TETE",
                           en_tetes={"Authorization": "Bearer jeton-client", "X-Goog-Api-Client": "essai/1"})
    assert statut == 200
    (r,) = amont.requetes
    assert r["chemin"] == CHEMIN_GEN + "?alt=json", "paramètres de clé retirés, les autres gardés"
    assert r["en_tetes"]["x-goog-api-key"] == CLE_REELLE
    assert "authorization" not in r["en_tetes"] and "proxy-authorization" not in r["en_tetes"]
    assert r["en_tetes"]["x-goog-api-client"] == "essai/1", "les autres en-têtes passent"
    brut = relais_proc.journal_brut()
    assert "CLE-CLIENT" not in brut and "jeton-client" not in brut
    (e,) = relais_proc.entrees_journal()
    assert e["chemin"] == CHEMIN_GEN + "?alt=json"


def test_sans_cle_du_client_le_relais_pose_quand_meme_la_sienne(amont, relais_proc):
    """Le relais ne demande rien au client : la clé factice de la commande n'est qu'une exigence de la commande."""
    statut, _, _ = appeler(relais_proc.url, CHEMIN_GEN, CORPS, cle=None)
    assert statut == 200 and amont.requetes[0]["en_tetes"]["x-goog-api-key"] == CLE_REELLE


@pytest.mark.parametrize("modele", ["gemini-3-pro", "gemini-4-argon-x", "GEMINI-4-ARGON", "gemini-4-argon%2F"])
def test_modele_hors_liste_refuse_sans_envoi(amont, relais_proc, modele):
    statut, _, octets = appeler(relais_proc.url, f"/v1beta/models/{modele}:generateContent", CORPS)
    assert statut == 403 and "erreur" in json.loads(octets)
    assert amont.requetes == []
    e = etat(relais_proc.url)
    assert e["appels"] == 0 and e["refus"] == 1
    (j,) = relais_proc.entrees_journal()
    assert j["statut"] == 403 and TEXTE_SECRET not in relais_proc.journal_brut()


def test_liste_blanche_etendue_par_option(amont, tmp_path):
    r = Relais(amont.url, tmp_path, args=("--modele", "gemini-4-argon", "--modele", "gemini-essai"))
    try:
        assert appeler(r.url, "/v1beta/models/gemini-essai:generateContent", CORPS)[0] == 200
        assert appeler(r.url, "/v1beta/models/gemini-4-argon:countTokens", CORPS)[0] == 200
        assert appeler(r.url, "/v1beta/models/gemini-3-pro:generateContent", CORPS)[0] == 403
        assert len(amont.requetes) == 2 and etat(r.url)["modeles"] == ["gemini-4-argon", "gemini-essai"]
    finally:
        r.arreter()


@pytest.mark.parametrize("methode, chemin", [
    ("POST", "/v1beta/models/gemini-4-argon:streamGenerateContent"),
    ("POST", "/v1/models/gemini-4-argon:generateContent"),
    ("POST", "/v1beta/models/gemini-4-argon:generateContent/suite"),
    ("POST", "/v1beta/models"),
    ("POST", "/v1beta/models/gemini-4-argon"),
    ("POST", "/relais/etat"),
    ("POST", "/"),
    ("GET", "/v1beta/models/gemini-4-argon:generateContent"),
    ("GET", "/v1beta/models"),
    ("PUT", "/v1beta/models/gemini-4-argon:generateContent"),
    ("DELETE", "/v1beta/models/gemini-4-argon:generateContent"),
])
def test_chemin_ou_methode_inconnus_refuses_sans_envoi(amont, relais_proc, methode, chemin):
    statut, _, octets = appeler(relais_proc.url, chemin, CORPS, methode=methode)
    assert statut == 403 and "erreur" in json.loads(octets)
    assert amont.requetes == []
    assert etat(relais_proc.url)["refus"] == 1


def test_max_appels_429_sans_envoi(amont, tmp_path):
    r = Relais(amont.url, tmp_path, args=("--max-appels", "2"))
    try:
        assert appeler(r.url, CHEMIN_GEN, CORPS)[0] == 200
        assert appeler(r.url, CHEMIN_COMPTE, CORPS)[0] == 200
        statut, _, octets = appeler(r.url, CHEMIN_GEN, CORPS)
        assert statut == 429 and "max-appels" in json.loads(octets)["erreur"]
        assert appeler(r.url, CHEMIN_COMPTE, CORPS)[0] == 429
        assert len(amont.requetes) == 2, "rien n'est envoyé au-delà de la borne"
        e = etat(r.url)
        assert e["appels"] == 2 and e["refus"] == 2 and e["appels_restants"] == 0
        j = r.entrees_journal(4)
        assert [x.get("statut", x.get("statut_amont")) for x in j] == [200, 200, 429, 429]
    finally:
        r.arreter()


def test_max_appels_zero_refuse_tout(amont, tmp_path):
    r = Relais(amont.url, tmp_path, args=("--max-appels", "0"))
    try:
        assert appeler(r.url, CHEMIN_GEN, CORPS)[0] == 429 and amont.requetes == []
    finally:
        r.arreter()


def test_max_octets_corps_429_sans_envoi(amont, tmp_path):
    corps_juste = json.dumps(CORPS).encode("utf-8")
    r = Relais(amont.url, tmp_path, args=("--max-octets-corps", str(len(corps_juste))))
    try:
        assert appeler(r.url, CHEMIN_GEN, corps_juste)[0] == 200, "à la borne : passe"
        statut, _, octets = appeler(r.url, CHEMIN_GEN, corps_juste + b" ")
        assert statut == 429 and "max-octets-corps" in json.loads(octets)["erreur"]
        assert len(amont.requetes) == 1
        e = etat(r.url)
        assert e["appels"] == 1 and e["refus"] == 1 and e["octets_envoyes"] == len(corps_juste)
        assert TEXTE_SECRET not in r.journal_brut()
    finally:
        r.arreter()


def test_appels_simultanes_ne_franchissent_pas_la_borne(amont, tmp_path):
    amont.attente_s = 0.3
    r = Relais(amont.url, tmp_path, args=("--max-appels", "3"))
    try:
        statuts = []
        verrou = threading.Lock()

        def un_appel():
            s = appeler(r.url, CHEMIN_GEN, CORPS)[0]
            with verrou:
                statuts.append(s)

        fils = [threading.Thread(target=un_appel) for _ in range(8)]
        for f in fils:
            f.start()
        for f in fils:
            f.join(timeout=30)
        assert sorted(statuts) == [200, 200, 200, 429, 429, 429, 429, 429]
        assert len(amont.requetes) == 3
    finally:
        r.arreter()


def test_sans_content_length_411_sans_envoi(amont, relais_proc):
    statut, _, _ = appeler(relais_proc.url, CHEMIN_GEN, sans_longueur=True)
    assert statut == 411 and amont.requetes == [] and etat(relais_proc.url)["refus"] == 1


def test_amont_injoignable_502(tmp_path):
    s = ThreadingHTTPServer(("127.0.0.1", 0), BaseHTTPRequestHandler)
    port = s.server_address[1]
    s.server_close()
    r = Relais(f"http://127.0.0.1:{port}", tmp_path)
    try:
        statut, _, octets = appeler(r.url, CHEMIN_GEN, CORPS)
        assert statut == 502 and "amont injoignable" in json.loads(octets)["erreur"]
        e = etat(r.url)
        assert e["appels"] == 1 and e["reponses_par_statut"] == {"502": 1}
        (j,) = r.entrees_journal()
        assert j["statut"] == 502 and CLE_REELLE not in r.journal_brut()
    finally:
        r.arreter()


def test_refus_de_demarrer_sans_cle(amont):
    proc, url, sortie = lancer_relais(amont.url, cle=None)
    assert url is None and proc.returncode == 2 and "aucune clé dans la variable GEMINI_API_KEY" in sortie
    proc, url, sortie = lancer_relais(amont.url, cle="   ")
    assert url is None and proc.returncode == 2


def test_refus_de_demarrer_amont_en_clair_non_local(amont):
    proc, url, sortie = lancer_relais("http://exemple.invalid")
    assert url is None and proc.returncode == 2 and "boucle locale" in sortie and CLE_REELLE not in sortie


def test_ecoute_sur_la_boucle_locale_seulement(relais_proc):
    assert relais_proc.url.startswith("http://127.0.0.1:")
    assert relais.HOTE == "127.0.0.1" and "--hote" not in relais.analyseur().format_help()


def test_chemin_sans_cle():
    assert relais.chemin_sans_cle("/v1beta/models/gemini-4-argon:generateContent?key=K") == (
        "/v1beta/models/gemini-4-argon:generateContent", "gemini-4-argon", "generateContent")
    assert relais.chemin_sans_cle("/v1beta/models/m.1_2-3:countTokens?a=1&KEY=K&b=2") == (
        "/v1beta/models/m.1_2-3:countTokens?a=1&b=2", "m.1_2-3", "countTokens")
    for mauvais in ("/v1beta/models/m:streamGenerateContent", "/v1beta/models/a/b:generateContent", "/v1beta/models/",
                    "/v1/models/m:generateContent", "//v1beta/models/m:generateContent"):
        assert relais.chemin_sans_cle(mauvais) == (None, None, None)


def test_usage_d_une_reponse_ne_garde_que_les_comptes():
    corps = json.dumps({"candidates": [{"content": {"parts": [{"text": "secret"}]}}], "modelVersion": "m",
                        "usageMetadata": {"promptTokenCount": 3, "detail": [{"x": 1}], "candidatesTokenCount": 2}})
    assert relais.usage_d_une_reponse(corps.encode()) == {"usageMetadata": {"promptTokenCount": 3, "candidatesTokenCount": 2},
                                                          "modele_servi": "m"}
    assert relais.usage_d_une_reponse(b"pas du json") == {} and relais.usage_d_une_reponse(b"[1]") == {}


def test_mandataire_de():
    assert relais.mandataire_de({}) is None
    assert relais.mandataire_de({"HTTPS_PROXY": "http://127.0.0.1:40191"}) == ("127.0.0.1", 40191, {})
    hote, port, h = relais.mandataire_de({"https_proxy": "http://u:p%40s@mandataire:3128"})
    assert (hote, port) == ("mandataire", 3128) and h["Proxy-Authorization"].startswith("Basic ")
    with pytest.raises(relais.RelaisInvalide):
        relais.mandataire_de({"HTTPS_PROXY": "https://sans-port"})


# === bout en bout : commande_argon_v2.py --url-base → relais → faux Gemini ==============================================

@pytest.fixture
def faux_gemini():
    s = FauxGemini()
    yield s
    s.arreter()


def lancer_commande(url_relais, consigne="x" * 4000, args=(), env=None):
    p = subprocess.run([sys.executable, "-I", "-B", COMMANDE, "--url-base", url_relais + "/v1beta", *args],
                       input=consigne.encode("utf-8"), capture_output=True, env=env or env_commande(cle=CLE_CLIENT),
                       timeout=120)
    lignes = [l for l in p.stdout.decode("utf-8").splitlines() if l.strip()]
    sortie = p.stdout.decode("utf-8") + p.stderr.decode("utf-8")
    assert CLE_REELLE not in sortie, "la clé du relais ne peut pas sortir de la commande : elle ne l'a jamais"
    return p.returncode, json.loads(lignes[-1]), p.stderr.decode("utf-8")


def test_bout_en_bout_commande_relais_faux_gemini(faux_gemini, tmp_path):
    r = Relais(faux_gemini.url.replace("/v1beta", ""), tmp_path)
    try:
        code, o, err = lancer_commande(r.url)
        assert code == 0 and err == "", err
        assert o["texte"] == "OK" and o["cout_origine"] == "usage" and o["envoye"] is True and o["cout_usd"] > 0
        assert o["modele_servi"] == "gemini-4-argon" and o["entree_jetons_comptee"] == 1000
        (compte,), (gen,) = faux_gemini.comptes(), faux_gemini.generations()
        assert compte["cle"] == CLE_REELLE and gen["cle"] == CLE_REELLE, "la clé factice de la commande est remplacée"
        assert gen["chemin"] == "/v1beta/models/gemini-4-argon:generateContent"
        assert gen["corps"]["contents"] == [{"role": "user", "parts": [{"text": "x" * 4000}]}]
        assert gen["corps"]["generationConfig"] == {"maxOutputTokens": 65536, "thinkingConfig": {"thinkingBudget": 8192}}
        e = etat(r.url)
        assert e["appels"] == 2 and e["refus"] == 0 and e["reponses_par_statut"] == {"200": 2}
        j = r.entrees_journal(2)
        assert [x["action"] for x in j] == ["countTokens", "generateContent"]
        assert j[0]["totalTokens"] == 1000 and j[1]["usageMetadata"] == FauxGemini.USAGE
        brut = r.journal_brut()
        assert "xxxx" not in brut and CLE_CLIENT not in brut and CLE_REELLE not in brut
    finally:
        r.arreter()


def test_bout_en_bout_commande_accepte_la_cle_factice_et_la_refuse_vide(faux_gemini, tmp_path):
    r = Relais(faux_gemini.url.replace("/v1beta", ""), tmp_path)
    try:
        code, o, _ = lancer_commande(r.url, env=env_commande(cle=""))
        assert code == 2 and "GEMINI_API_KEY absente ou vide" in o["erreur"], "la commande exige une clé non vide"
        code, o, _ = lancer_commande(r.url, env=env_commande(cle=CLE_CLIENT))
        assert code == 0 and o["texte"] == "OK"
        assert faux_gemini.generations()[0]["cle"] == CLE_REELLE
    finally:
        r.arreter()


def test_bout_en_bout_erreur_amont_remonte_par_la_commande(faux_gemini, tmp_path):
    faux_gemini.mode = "http400"
    r = Relais(faux_gemini.url.replace("/v1beta", ""), tmp_path)
    try:
        code, o, _ = lancer_commande(r.url)
        assert code == 3 and "HTTP 400" in o["erreur"] and o["cout_origine"] == "plancher"
        assert etat(r.url)["reponses_par_statut"] == {"200": 1, "400": 1}
    finally:
        r.arreter()


def test_bout_en_bout_modele_hors_liste_la_commande_echoue_sans_envoi(faux_gemini, tmp_path):
    r = Relais(faux_gemini.url.replace("/v1beta", ""), tmp_path)
    try:
        code, o, _ = lancer_commande(r.url, args=("--modele", "gemini-3-pro"))
        assert code == 3 and "HTTP 403" in o["erreur"]
        assert faux_gemini.requetes == [] and etat(r.url)["appels"] == 0
    finally:
        r.arreter()


def test_bout_en_bout_borne_d_appels_la_commande_echoue_sans_envoi(faux_gemini, tmp_path):
    r = Relais(faux_gemini.url.replace("/v1beta", ""), tmp_path, args=("--max-appels", "1"))
    try:
        code, o, _ = lancer_commande(r.url)
        assert code == 3 and "HTTP 429" in o["erreur"], "le compte passe, la génération est refusée par la borne"
        assert len(faux_gemini.comptes()) == 1 and faux_gemini.generations() == []
    finally:
        r.arreter()


def test_enveloppe_v3_sans_cle_ni_fichier():
    """L'enveloppe v3 ne lit aucun fichier de clé, pose la clé factice, pointe la commande sur le relais local."""
    complet = open(os.path.join(ICI, "appel-argon-v3.sh"), encoding="utf-8").read()
    texte = "\n".join(l for l in complet.splitlines() if not l.startswith("#"))  # les commentaires citent l'ancien montage
    assert ".cle-gemini" not in texte and "cat " not in texte and "$(cat" not in texte and "<" not in texte
    assert "GEMINI_API_KEY=factice-relais" in texte
    assert "--url-base http://127.0.0.1:8788/v1beta" in texte
    assert "commande_argon_v2.py" in texte and "appel-argon-v3" in complet
    assert "HTTPS_PROXY=" not in texte and "SSL_CERT_FILE=" not in texte, "boucle locale : aucun mandataire"
