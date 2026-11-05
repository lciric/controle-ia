"""Essais de `relais_kimi_v1.py` : le relais est lancé **dans son propre processus** (`python -I -B`) avec une clé **factice**
dans son seul environnement, devant un **faux amont local** (`http.server`, 127.0.0.1, port libre) qui imite l'API
compatible OpenAI de Moonshot et consigne ce qu'il reçoit. Aucun réseau sortant, aucune vraie clé, aucun appel payant.

Cas sain ; artefacts (R5) : modèle non permis, modèle servi différent (et absent), plafond atteint (en série et sous appels
simultanés), usage absent (pire cas), clé absente, chemin interdit, corps trop gros, max d'appels, clé effacée de
l'environnement après lecture, aucune clé ni texte dans le journal ; plus : flux refusé, outil intégré refusé, cache,
amont injoignable, arrêt par le PID de `$!` sans `setsid` ni `nohup`.

Lancer (depuis la racine du dépôt) : `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m pytest -q -p no:cacheprovider
docs/notes/ideation-organisme-v1/relais-kimi-v1/test_relais_kimi_v1.py`.
"""

import http.client
import json
import os
import signal
import subprocess
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import pytest

import relais_kimi_v1 as relais

ICI = os.path.dirname(os.path.abspath(__file__))
RELAIS = os.path.join(ICI, "relais_kimi_v1.py")
CLE_REELLE = "sk-cle-factice-du-relais-kimi-0123456789-ne-jamais-imprimer"
CLE_CLIENT = "sk-factice-client"
TEXTE_SECRET = "TEXTE-DE-CONSIGNE-QUI-NE-DOIT-JAMAIS-ETRE-JOURNALISE"
REPONSE_SECRETE = "TEXTE-DE-REPONSE-QUI-NE-DOIT-JAMAIS-ETRE-JOURNALISE"
MODELE = "kimi-k3.1-pro"  # nom factice des essais : l'identifiant réel est à lire dans la liste officielle
PRIX = {"entree": 1.0, "sortie": 4.0, "cache": 0.25}  # USD par million, factices
USAGE = {"prompt_tokens": 100_000, "completion_tokens": 50_000, "total_tokens": 150_000}
COUT_USAGE = (100_000 * 1.0 + 50_000 * 4.0) / 1e6  # 0,30 USD
CORPS = {"model": MODELE, "messages": [{"role": "user", "content": TEXTE_SECRET}], "max_tokens": 100}
OCTETS_CORPS = len(json.dumps(CORPS).encode("utf-8"))
PIRE_CAS = ((OCTETS_CORPS + 1024) * 1.0 + 100 * 4.0) / 1e6
CHEMIN = "/v1/chat/completions"


# --- faux amont -------------------------------------------------------------------------------------------------------

class FauxAmont:
    """Consigne chaque requête (chemin, en-têtes, corps) ; répond selon `code`, `objet` (ou `brut`) et `attente_s`."""

    def __init__(self):
        self.requetes, self.code, self.attente_s, self.brut = [], 200, 0.0, None
        self.objet = {"id": "chatcmpl-essai", "object": "chat.completion", "created": 1, "model": MODELE,
                      "choices": [{"index": 0, "message": {"role": "assistant", "content": REPONSE_SECRETE},
                                   "finish_reason": "stop"}], "usage": dict(USAGE)}
        faux = self

        class Gestion(BaseHTTPRequestHandler):
            protocol_version = "HTTP/1.1"

            def log_message(self, *a):
                pass

            def do_POST(self):
                corps = self.rfile.read(int(self.headers.get("Content-Length") or 0))
                faux.requetes.append({"chemin": self.path, "en_tetes": {k.lower(): v for k, v in self.headers.items()},
                                      "corps": corps})
                if faux.attente_s:
                    time.sleep(faux.attente_s)
                brut = faux.brut if faux.brut is not None else json.dumps(faux.objet).encode("utf-8")
                try:
                    self.send_response(faux.code)
                    self.send_header("Content-Type", "application/json")
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

def arguments(amont_url, plafond="10", modeles=MODELE, extra=()):
    return ["--port", "0", "--amont", amont_url, "--modeles-permis", modeles, "--plafond-usd", plafond,
            "--prix-entree", str(PRIX["entree"]), "--prix-sortie", str(PRIX["sortie"]), "--prix-cache", str(PRIX["cache"]),
            *extra]


def lancer_relais(args, journal=None, cle=CLE_REELLE, variable="KIMI_API_KEY"):
    """Rend (processus, url ou None, sortie)."""
    env = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "LANG": "C.UTF-8"}
    if cle is not None:
        env[variable] = cle
    ligne_cmd = [sys.executable, "-I", "-B", RELAIS, *args] + (["--journal", journal] if journal else [])
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
    def __init__(self, amont_url, tmp_path, **kw):
        self.journal = str(tmp_path / "journal-relais-kimi.jsonl")
        self.proc, self.url, self.premiere_ligne = lancer_relais(arguments(amont_url, **kw), self.journal)
        assert self.url, self.premiere_ligne
        assert CLE_REELLE not in self.premiere_ligne

    def arreter(self):
        self.proc.kill()
        sortie, erreurs = self.proc.communicate(timeout=10)
        assert CLE_REELLE not in self.premiere_ligne + sortie + erreurs, "la clé ne sort jamais du relais"
        brut = self.journal_brut()
        assert CLE_REELLE not in brut and TEXTE_SECRET not in brut and REPONSE_SECRETE not in brut

    def entrees_journal(self, au_moins=1):
        limite = time.time() + 3.0
        while True:
            entrees = []
            if os.path.exists(self.journal):
                with open(self.journal, encoding="utf-8") as f:
                    entrees = [json.loads(l) for l in f if l.strip()]
            if len(entrees) >= au_moins or time.time() > limite:
                return entrees
            time.sleep(0.02)

    def journal_brut(self):
        return open(self.journal, encoding="utf-8").read() if os.path.exists(self.journal) else ""


@pytest.fixture
def relais_proc(amont, tmp_path):
    r = Relais(amont.url, tmp_path)
    yield r
    r.arreter()


def appeler(url, chemin=CHEMIN, corps=CORPS, methode="POST", en_tetes=None, sans_longueur=False):
    hote, port = url.replace("http://", "").split(":")
    c = http.client.HTTPConnection(hote, int(port), timeout=30)
    h = {"Content-Type": "application/json", "Authorization": "Bearer " + CLE_CLIENT}
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
    statut, _, octets = appeler(url, relais.CHEMIN_ETAT, corps=None, methode="GET")
    assert statut == 200
    return json.loads(octets)


# === cas sain ===========================================================================================================

def test_cas_sain_cle_posee_reponse_relayee_cout_compte(amont, relais_proc):
    statut, en_tetes, octets = appeler(relais_proc.url, en_tetes={"x-api-key": "cle-client-2", "X-Essai": "passe"})
    assert statut == 200 and json.loads(octets) == amont.objet
    assert en_tetes["x-temoin-amont"] == "relaye" and en_tetes["content-type"] == "application/json"
    (r,) = amont.requetes
    assert r["chemin"] == CHEMIN and json.loads(r["corps"]) == CORPS, "corps relayé tel quel"
    assert r["en_tetes"]["authorization"] == "Bearer " + CLE_REELLE, "la clé du client est remplacée par celle du relais"
    assert "x-api-key" not in r["en_tetes"] and r["en_tetes"]["x-essai"] == "passe"
    assert r["en_tetes"]["accept-encoding"] == "identity"
    e = etat(relais_proc.url)
    assert e["appels"] == 1 and e["refus"] == 0 and e["refus_modele"] == 0 and e["usages_absents"] == 0
    assert e["depense_usd"] == pytest.approx(COUT_USAGE) and e["engage_usd"] == 0
    assert e["reponses_par_statut"] == {"200": 1} and e["flux"] == "refusé" and e["modeles_permis"] == [MODELE]
    assert e["version"] == "relais-kimi-v1" and e["amont"] == amont.url and e["mandataire"] is False
    (j,) = relais_proc.entrees_journal()
    assert j["modele"] == MODELE and j["modele_servi"] == MODELE and j["usage"] == USAGE and j["usage_absent"] is False
    assert j["cout_usd"] == pytest.approx(COUT_USAGE) and j["statut_amont"] == 200 and j["quand_utc"].endswith("+00:00")


def test_cache_compte_au_prix_du_cache(amont, relais_proc):
    amont.objet["usage"] = {"prompt_tokens": 100_000, "completion_tokens": 0, "total_tokens": 100_000,
                            "prompt_tokens_details": {"cached_tokens": 60_000}}
    assert appeler(relais_proc.url)[0] == 200
    assert etat(relais_proc.url)["depense_usd"] == pytest.approx((40_000 * 1.0 + 60_000 * 0.25) / 1e6)
    amont.objet["usage"] = {"prompt_tokens": 100_000, "completion_tokens": 0, "total_tokens": 100_000,
                            "cached_tokens": 100_000}
    assert appeler(relais_proc.url)[0] == 200
    assert etat(relais_proc.url)["depense_usd"] == pytest.approx((40_000 + 15_000 + 25_000) / 1e6)


def test_bareme_cout_usage_et_pire_cas():
    b = relais.Bareme(1.0, 4.0, 0.25, 1000)
    assert b.cout_usage(USAGE) == pytest.approx(COUT_USAGE)
    assert b.cout_usage({"prompt_tokens": 10, "completion_tokens": 0, "cached_tokens": 30}) == pytest.approx(
        (10 * 0.25 + 20 * 4.0) / 1e6), "cache au-delà de prompt_tokens : excédent au prix fort"
    assert b.cout_usage({"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 20}) == pytest.approx(
        (10 + 20 + 5 * 4.0) / 1e6), "jetons au total sans case : prix fort"
    for mauvais in (None, {}, {"prompt_tokens": 1}, {"prompt_tokens": "1", "completion_tokens": 1},
                    {"prompt_tokens": True, "completion_tokens": 1}, {"prompt_tokens": -1, "completion_tokens": 1}):
        assert b.cout_usage(mauvais) is None
    assert b.pire_cas(100, {}) == pytest.approx((1124 + 1000 * 4.0) / 1e6), "sans max_tokens : borne de l'option"
    assert b.pire_cas(100, {"max_tokens": 10, "n": 3}) == pytest.approx((1124 + 30 * 4.0) / 1e6)
    assert b.pire_cas(100, {"max_tokens": 10, "max_completion_tokens": 50}) == pytest.approx((1124 + 200) / 1e6)
    with pytest.raises(relais.RelaisInvalide):
        relais.Bareme(-1, 1, 1, 1)
    with pytest.raises(relais.RelaisInvalide):
        relais.Bareme(1, float("nan"), 1, 1)


# === modèles : barrière R-764 ===========================================================================================

@pytest.mark.parametrize("modele", ["kimi-k2.5", "kimi-k3.1-pro-preview", "KIMI-K3.1-PRO", " kimi-k3.1-pro", None, 3,
                                    ["kimi-k3.1-pro"]])
def test_modele_non_permis_refuse_sans_envoi(amont, relais_proc, modele):
    corps = dict(CORPS, model=modele)
    if modele is None:
        del corps["model"]
    statut, _, octets = appeler(relais_proc.url, corps=corps)
    assert statut == 403 and "modèle non permis" in json.loads(octets)["erreur"]
    assert amont.requetes == []
    e = etat(relais_proc.url)
    assert e["appels"] == 0 and e["refus"] == 1 and e["refus_modele"] == 1 and e["depense_usd"] == 0
    (j,) = relais_proc.entrees_journal()
    assert j["statut"] == 403


@pytest.mark.parametrize("servi", ["kimi-k2.5", "kimi-k3.1-pro-2026-10", None])
def test_modele_servi_different_refus_de_modele_reponse_non_relayee(amont, relais_proc, servi):
    if servi is None:
        del amont.objet["model"]
    else:
        amont.objet["model"] = servi
    statut, _, octets = appeler(relais_proc.url)
    o = json.loads(octets)
    assert statut == 502 and "modèle servi différent" in o["erreur"] and o["modele_servi"] == servi
    assert REPONSE_SECRETE.encode() not in octets, "la réponse d'un autre modèle ne sort pas du relais"
    assert len(amont.requetes) == 1
    e = etat(relais_proc.url)
    assert e["refus_modele"] == 1 and e["ecarts_modele_servi"] == 1 and e["appels"] == 1
    assert e["depense_usd"] == pytest.approx(COUT_USAGE), "l'amont a servi : la dépense est portée"
    (j,) = relais_proc.entrees_journal()
    assert j["statut"] == 502 and j["modele"] == MODELE and j["modele_servi"] == servi


def test_reponse_d_erreur_amont_relayee_sans_ecart_de_modele(amont, relais_proc):
    amont.code = 400
    amont.objet = {"error": {"type": "invalid_request_error", "message": "refus"},
                   "usage": {"prompt_tokens": 0, "completion_tokens": 0}}
    statut, _, octets = appeler(relais_proc.url)
    assert statut == 400 and json.loads(octets) == amont.objet
    e = etat(relais_proc.url)
    assert e["refus_modele"] == 0 and e["depense_usd"] == 0 and e["reponses_par_statut"] == {"400": 1}


def test_liste_de_modeles_permis(amont, tmp_path):
    r = Relais(amont.url, tmp_path, modeles="kimi-k3.1-pro, kimi-essai")
    try:
        assert etat(r.url)["modeles_permis"] == ["kimi-k3.1-pro", "kimi-essai"]
        amont.objet["model"] = "kimi-essai"
        assert appeler(r.url, corps=dict(CORPS, model="kimi-essai"))[0] == 200
        assert appeler(r.url, corps=dict(CORPS, model="kimi-k2.5"))[0] == 403
        assert len(amont.requetes) == 1
    finally:
        r.arreter()


@pytest.mark.parametrize("modeles", ["", " , ", "role=kimi-k3.1-pro", "moonshot/kimi", "kimi k3"])
def test_modeles_permis_invalides_refus_de_demarrer(amont, modeles):
    proc, url, sortie = lancer_relais(arguments(amont.url, modeles=modeles))
    assert url is None and proc.returncode == 2 and "--modeles-permis" in sortie and CLE_REELLE not in sortie


# === plafond en dollars ==================================================================================================

def test_plafond_atteint_402_sans_envoi(amont, tmp_path):
    r = Relais(amont.url, tmp_path, plafond="1.0")  # réserve 0,40 ; coût lu 0,30 par appel
    try:
        assert [appeler(r.url)[0] for _ in range(3)] == [200, 200, 200]  # 0,9 dépensés ; 0,9 + 0,4 > 1
        statut, _, octets = appeler(r.url)
        assert statut == 402 and "plafond" in json.loads(octets)["erreur"]
        assert len(amont.requetes) == 3, "rien n'est envoyé au-delà du plafond"
        e = etat(r.url)
        assert e["appels"] == 3 and e["refus"] == 1 and e["depense_usd"] == pytest.approx(0.9)
        assert e["restant_usd"] == pytest.approx(0.1) and e["engage_usd"] == 0
        assert r.entrees_journal(4)[-1]["statut"] == 402
    finally:
        r.arreter()


def test_plafond_tenu_sous_appels_simultanes(amont, tmp_path):
    amont.attente_s = 0.4
    r = Relais(amont.url, tmp_path, plafond="1.0")  # deux réserves de 0,40 tiennent, pas trois
    try:
        statuts, verrou = [], threading.Lock()

        def un_appel():
            s = appeler(r.url)[0]
            with verrou:
                statuts.append(s)

        fils = [threading.Thread(target=un_appel) for _ in range(8)]
        for f in fils:
            f.start()
        for f in fils:
            f.join(timeout=30)
        assert sorted(statuts) == [200, 200] + [402] * 6 and len(amont.requetes) == 2
        assert etat(r.url)["depense_usd"] == pytest.approx(0.6)
    finally:
        r.arreter()


def test_reserve_au_pire_cas_de_la_requete(amont, tmp_path):
    """Sans max_tokens, la réserve est le pire cas (262 144 jetons de sortie à 4 USD ≈ 1,05 USD) : au-dessus du plafond."""
    r = Relais(amont.url, tmp_path, plafond="1.0")
    try:
        corps = {k: v for k, v in CORPS.items() if k != "max_tokens"}
        assert appeler(r.url, corps=corps)[0] == 402 and amont.requetes == []
    finally:
        r.arreter()


def test_usage_absent_compte_au_pire_cas(amont, relais_proc):
    del amont.objet["usage"]
    assert appeler(relais_proc.url)[0] == 200
    e = etat(relais_proc.url)
    assert e["usages_absents"] == 1 and e["depense_usd"] == pytest.approx(PIRE_CAS, abs=1e-6)
    (j,) = relais_proc.entrees_journal()
    assert j["usage_absent"] is True and j["usage"] is None and j["cout_usd"] == pytest.approx(PIRE_CAS, abs=1e-6)


@pytest.mark.parametrize("brut, code", [(b"pas du json", 200), (b'{"error": {"message": "x"}}', 500),
                                        (b'{"usage": {"prompt_tokens": "beaucoup"}}', 200)])
def test_usage_illisible_compte_au_pire_cas(amont, relais_proc, brut, code):
    amont.brut, amont.code = brut, code
    statut, _, _ = appeler(relais_proc.url)
    assert statut == (502 if code == 200 else code)  # 200 illisible : aucun modèle servi lisible, donc écart
    e = etat(relais_proc.url)
    assert e["usages_absents"] == 1 and e["depense_usd"] == pytest.approx(PIRE_CAS, abs=1e-6)


def test_amont_injoignable_502_sans_depense(tmp_path):
    s = ThreadingHTTPServer(("127.0.0.1", 0), BaseHTTPRequestHandler)
    port = s.server_address[1]
    s.server_close()
    r = Relais(f"http://127.0.0.1:{port}", tmp_path)
    try:
        statut, _, octets = appeler(r.url)
        assert statut == 502 and "amont injoignable" in json.loads(octets)["erreur"]
        e = etat(r.url)
        assert e["depense_usd"] == 0 and e["engage_usd"] == 0 and e["reponses_par_statut"] == {"502": 1}
    finally:
        r.arreter()


# === clé ================================================================================================================

def test_cle_absente_refus_de_demarrer(amont):
    proc, url, sortie = lancer_relais(arguments(amont.url), cle=None)
    assert url is None and proc.returncode == 2 and "aucune clé dans la variable KIMI_API_KEY" in sortie
    proc, url, sortie = lancer_relais(arguments(amont.url), cle="   ")
    assert url is None and proc.returncode == 2
    proc, url, sortie = lancer_relais(arguments(amont.url) + ["--variable-cle", "CLE_KIMI_ESSAI"])
    assert url is None and proc.returncode == 2 and "CLE_KIMI_ESSAI" in sortie and CLE_REELLE not in sortie


def test_variable_de_cle_au_choix(amont, tmp_path):
    proc, url, ligne = lancer_relais(arguments(amont.url) + ["--variable-cle", "CLE_KIMI_ESSAI"],
                                     variable="CLE_KIMI_ESSAI")
    try:
        assert url, ligne
        assert appeler(url)[0] == 200 and amont.requetes[-1]["en_tetes"]["authorization"] == "Bearer " + CLE_REELLE
        assert etat(url)["variable_cle_encore_presente"] is False
    finally:
        proc.kill()
        proc.communicate(timeout=10)


def test_cle_effacee_de_l_environnement_apres_lecture(relais_proc):
    assert etat(relais_proc.url)["variable_cle_encore_presente"] is False


def test_lire_cle_efface_la_variable():
    env = {"KIMI_API_KEY": " " + CLE_REELLE + "\n", "AUTRE": "x"}
    assert relais.lire_cle(env, "KIMI_API_KEY") == CLE_REELLE and env == {"AUTRE": "x"}
    env = {"KIMI_API_KEY": "  "}
    with pytest.raises(relais.RelaisInvalide):
        relais.lire_cle(env, "KIMI_API_KEY")
    assert env == {}, "effacée même vide"
    with pytest.raises(relais.RelaisInvalide):
        relais.lire_cle({"KIMI_API_KEY": "a\nb"}, "KIMI_API_KEY")
    with pytest.raises(relais.RelaisInvalide):
        relais.lire_cle({}, "KIMI_API_KEY")


def test_servir_refuse_si_la_variable_est_encore_la():
    with pytest.raises(relais.RelaisInvalide):
        relais.servir(0, "x", "http://127.0.0.1:1", ["m"], relais.Bareme(1, 1, 1, 1), 1, 0, 1, 1,
                      environnement={"KIMI_API_KEY": "x"})


def test_cle_jamais_en_argument_ni_en_fichier():
    aide = relais.analyseur().format_help()
    assert "--cle " not in aide and "--fichier-cle" not in aide and "--hote" not in aide


def test_aucune_cle_ni_texte_dans_le_journal(amont, relais_proc):
    appeler(relais_proc.url)                                             # sain
    appeler(relais_proc.url, corps=dict(CORPS, model="kimi-k2.5"))       # refus de modèle
    appeler(relais_proc.url, corps=dict(CORPS, stream=True))             # flux refusé
    amont.objet["model"] = "autre"
    appeler(relais_proc.url)                                             # écart de modèle servi
    brut = relais_proc.journal_brut()
    assert len(relais_proc.entrees_journal(4)) == 4
    assert CLE_REELLE not in brut and CLE_CLIENT not in brut and "Bearer" not in brut
    assert TEXTE_SECRET not in brut and REPONSE_SECRETE not in brut and '"choices"' not in brut and '"messages"' not in brut


# === chemins, corps, bornes =============================================================================================

@pytest.mark.parametrize("methode, chemin", [
    ("POST", "/v1/chat/completions?stream=true"),
    ("POST", "/v1/chat/completions/"),
    ("POST", "//v1/chat/completions"),
    ("POST", "/v1/completions"),
    ("POST", "/v1/embeddings"),
    ("POST", "/v1/files"),
    ("POST", "/v1/batches"),
    ("POST", "/v1/tokenizers/estimate-token-count"),
    ("POST", "/relais/etat"),
    ("POST", "/"),
    ("GET", "/v1/models"),
    ("GET", "/v1/users/me/balance"),
    ("GET", "/relais/etat?x=1"),
    ("PUT", CHEMIN),
    ("DELETE", CHEMIN),
])
def test_chemin_ou_methode_interdits_refuses_sans_envoi(amont, relais_proc, methode, chemin):
    statut, _, octets = appeler(relais_proc.url, chemin=chemin, methode=methode)
    assert statut == 403 and "erreur" in json.loads(octets)
    assert amont.requetes == [] and etat(relais_proc.url)["refus"] == 1


def test_corps_trop_gros_413_sans_envoi(amont, tmp_path):
    r = Relais(amont.url, tmp_path, extra=("--max-octets-corps", str(OCTETS_CORPS)))
    try:
        assert appeler(r.url)[0] == 200, "à la borne : passe"
        statut, _, octets = appeler(r.url, corps=json.dumps(CORPS).encode("utf-8") + b" ")
        assert statut == 413 and "max-octets-corps" in json.loads(octets)["erreur"]
        assert len(amont.requetes) == 1 and etat(r.url)["refus"] == 1
    finally:
        r.arreter()


def test_max_appels_429_sans_envoi(amont, tmp_path):
    r = Relais(amont.url, tmp_path, extra=("--max-appels", "2"))
    try:
        assert [appeler(r.url)[0] for _ in range(4)] == [200, 200, 429, 429]
        assert len(amont.requetes) == 2
        e = etat(r.url)
        assert e["appels"] == 2 and e["refus"] == 2 and e["appels_restants"] == 0
    finally:
        r.arreter()


@pytest.mark.parametrize("corps, motif", [
    (dict(CORPS, stream=True), "flux"),
    (dict(CORPS, stream="oui"), "flux"),
    (dict(CORPS, tools=[{"type": "builtin_function", "function": {"name": "$web_search"}}]), "outil"),
    (dict(CORPS, tools="x"), "outil"),
    (b"pas du json", "objet JSON"),
    (b"[1, 2]", "objet JSON"),
])
def test_corps_refuses_400_sans_envoi(amont, relais_proc, corps, motif):
    statut, _, octets = appeler(relais_proc.url, corps=corps)
    assert statut == 400 and motif in json.loads(octets)["erreur"] and amont.requetes == []


def test_outils_de_type_function_passent(amont, relais_proc):
    corps = dict(CORPS, stream=False, tools=[{"type": "function", "function": {"name": "f", "parameters": {}}}])
    assert appeler(relais_proc.url, corps=corps)[0] == 200


def test_sans_content_length_411_sans_envoi(amont, relais_proc):
    assert appeler(relais_proc.url, sans_longueur=True)[0] == 411 and amont.requetes == []


def test_ecoute_sur_la_boucle_locale_seulement(relais_proc):
    assert relais_proc.url.startswith("http://127.0.0.1:") and relais.HOTE == "127.0.0.1"


@pytest.mark.parametrize("amont_url", ["http://exemple.invalid", "https://api.moonshot.ai/v1", "ftp://x"])
def test_amont_invalide_refus_de_demarrer(amont_url):
    proc, url, sortie = lancer_relais(arguments(amont_url))
    assert url is None and proc.returncode == 2 and "--amont" in sortie and CLE_REELLE not in sortie


@pytest.mark.parametrize("extra", [("--plafond-usd", "0"), ("--plafond-usd", "nan"), ("--prix-sortie", "-1"),
                                   ("--max-appels", "-1"), ("--reserve-par-appel", "-0.1")])
def test_reglages_invalides_refus_de_demarrer(amont, extra):
    proc, url, sortie = lancer_relais(arguments(amont.url) + list(extra))
    assert url is None and proc.returncode == 2 and CLE_REELLE not in sortie


def test_mandataire_de():
    assert relais.mandataire_de({}) is None
    assert relais.mandataire_de({"HTTPS_PROXY": "http://127.0.0.1:40191"}) == ("127.0.0.1", 40191, {})
    hote, port, h = relais.mandataire_de({"https_proxy": "http://u:p%40s@mandataire:3128"})
    assert (hote, port) == ("mandataire", 3128) and h["Proxy-Authorization"].startswith("Basic ")
    with pytest.raises(relais.RelaisInvalide):
        relais.mandataire_de({"HTTPS_PROXY": "https://sans-port"})


# === arrêt par PID (R10 ; incident du 30 octobre) ======================================================================

def test_dollar_point_d_exclamation_est_le_pid_du_relais_et_l_arret_par_pid_le_tue(amont, tmp_path):
    """Lancement comme en production : `env -i … python3 … &` dans un shell, sans `setsid` ni `nohup` ; `$!` doit être le
    PID que le relais rend dans `/relais/etat`, et `kill <pid>` doit fermer le port."""
    journal_sortie = tmp_path / "relais-kimi-v1.log"
    ligne = " ".join(["env", "-i", "PATH=/usr/bin:/bin", "LANG=C.UTF-8", f"KIMI_API_KEY={CLE_REELLE}", sys.executable,
                      "-I", "-B", RELAIS, *arguments(amont.url)])
    shell = subprocess.Popen(["bash", "-c", f"{ligne} > {journal_sortie} 2>&1 & echo $!; wait $!"],
                             stdout=subprocess.PIPE, text=True)
    try:
        pid = int(shell.stdout.readline())
        limite, url = time.time() + 10, None
        while time.time() < limite and not url:
            texte = journal_sortie.read_text(encoding="utf-8") if journal_sortie.exists() else ""
            if texte.startswith("relais prêt sur "):
                url = texte.split()[3]
            time.sleep(0.05)
        assert url, "le relais n'a pas démarré"
        assert etat(url)["pid"] == pid, "$! est le PID du processus Python du relais"
        os.kill(pid, signal.SIGTERM)
        shell.wait(timeout=10)
        with pytest.raises(OSError):
            etat(url)
        assert CLE_REELLE not in journal_sortie.read_text(encoding="utf-8")
    finally:
        if shell.poll() is None:
            shell.kill()


def test_pas_de_setsid_ni_nohup_dans_la_ligne_de_lancement():
    doc = relais.__doc__
    lancement = doc[doc.index("    env -i"):]
    assert "setsid" not in lancement and "nohup" not in lancement and "echo $!" in lancement
