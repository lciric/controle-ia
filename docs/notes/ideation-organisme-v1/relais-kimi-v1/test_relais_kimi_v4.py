"""Essais du relais Kimi v4 (recherche Web officielle seule) et de `commande_kimi_recherche_v1.py`, contre le faux amont v3 ;
clé factice, aucun réseau sortant. Lancer depuis ce dossier ou la racine :
    PYTHONDONTWRITEBYTECODE=1 python -m pytest -q -p no:cacheprovider test_relais_kimi_v4.py"""

import json
import os
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.request

import pytest

ICI = os.path.dirname(os.path.abspath(__file__))
CLE = "cle-factice-essai-v4-0123456789abcdefghij"
MODELE = "kimi-k3.1-pro"
PRIX_RECHERCHE = 0.005
FIBRES = "/v1/formulas/moonshot/web-search:latest/fibers"
DECL = "/v1/formulas/moonshot/web-search:latest/tools"
DECLARATION = {"type": "function", "function": {
    "name": "web_search", "description": "Search the web for information",
    "parameters": {"type": "object", "properties": {"query": {"description": "What to search for", "type": "string"}},
                   "required": ["query"]}}}


def port_libre():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


def lancer(cmd, env, motif, tmp, nom):
    chemin = os.path.join(tmp, nom + ".log")
    journal = open(chemin, "w")
    proc = subprocess.Popen(cmd, env=env, stdout=journal, stderr=subprocess.STDOUT, cwd=ICI)
    for _ in range(100):
        texte = open(chemin).read()
        if motif in texte:
            return proc, texte
        if proc.poll() is not None:
            raise RuntimeError(texte)
        time.sleep(0.05)
    raise RuntimeError("pas prêt : " + nom)


@pytest.fixture
def banc(tmp_path):
    procs = []

    def fabriquer(options_amont=(), options_relais=(), recherches=10):
        amont, texte = lancer([sys.executable, "-I", "-B", "faux_amont_kimi_v3.py", *options_amont],
                              {"PATH": "/usr/bin:/bin"}, "faux amont prêt", str(tmp_path), "amont")
        procs.append(amont)
        url_amont = texte.strip().split()[-1]
        port = port_libre()
        journal = str(tmp_path / "journal.jsonl")
        cmd = [sys.executable, "-I", "-B", "relais_kimi_v4.py", "--port", str(port), "--amont", url_amont,
               "--modeles-permis", MODELE, "--plafond-usd", "5", "--reserve-par-appel", "0.05",
               "--prix-entree", "2", "--prix-sortie", "10", "--prix-cache", "2",
               "--max-jetons-sortie-pire-cas", "1000", "--journal", journal]
        if recherches:
            cmd += ["--max-recherches", str(recherches), "--prix-recherche", str(PRIX_RECHERCHE)]
        relais, _ = lancer(cmd + list(options_relais), {"PATH": "/usr/bin:/bin", "KIMI_API_KEY": CLE}, "relais prêt",
                           str(tmp_path), "relais")
        procs.append(relais)
        return f"http://127.0.0.1:{port}", journal, url_amont, str(tmp_path / "relais.log")

    yield fabriquer
    for p in procs:
        p.kill()
        p.wait()


OUVREUR = urllib.request.build_opener(urllib.request.ProxyHandler({}))


def requete(url, chemin, corps=None, brut=None):
    donnees = brut if brut is not None else (None if corps is None else json.dumps(corps).encode())
    req = urllib.request.Request(url + chemin, data=donnees, method="GET" if donnees is None else "POST",
                                 headers={"Content-Type": "application/json"})
    try:
        with OUVREUR.open(req, timeout=30) as r:
            return r.status, json.load(r)
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read() or b"{}")


def etat(url):
    return requete(url, "/relais/etat")[1]


def journal_lu(chemin):
    return [json.loads(l) for l in open(chemin) if l.strip()]


def commande(url, consigne="Lis les sources.", plafond="3", options=(), env_plus=None):
    env = {"PATH": "/usr/bin:/bin", "PLAFOND_SESSION_USD": plafond, "ROLE_POLE": "lecteur_sources"}
    env.update(env_plus or {})
    r = subprocess.run([sys.executable, "-I", "-B", "commande_kimi_recherche_v1.py", "--url-relais", url,
                        "--sortie-min-jetons", "100", "--max-sortie-jetons", "1000", *options],
                       input=consigne, capture_output=True, text=True, cwd=ICI, env=env, timeout=120)
    return r.returncode, json.loads(r.stdout.strip().splitlines()[-1]), r


SAIN = {"model": MODELE, "messages": [{"role": "user", "content": "Bonjour"}], "max_tokens": 100}


# --- cas sain -----------------------------------------------------------------------------------------------------

def test_cas_sain_boucle_complete(banc):
    """Deux tours d'outil à deux appels chacun, raisonnement gardé, puis réponse finale ; coût = modèle + recherches."""
    url, j, url_amont, _ = banc(["--tours-outil", "2", "--appels-par-tour", "2", "--morceaux-raisonnement", "2"])
    code, d, r = commande(url)
    assert code == 0, r.stdout
    assert d["texte"] == "Bonjour le monde." and d["modele_servi"] == MODELE
    assert d["tours"] == 3 and d["recherches"] == 4 and d["recherches_non_executees"] == 0
    assert d["cout_recherches_usd"] == pytest.approx(4 * PRIX_RECHERCHE)
    assert d["cout_usd"] == pytest.approx(3 * (12 * 2 + 7 * 10) / 1e6 + 4 * PRIX_RECHERCHE, abs=2e-6)
    assert [json.loads(q)["query"] for q in d["requetes_recherche"]] == [f"requête {i}" for i in range(1, 5)]
    e = etat(url)
    assert e["recherches"] == 4 and e["cout_recherches_usd"] == pytest.approx(4 * PRIX_RECHERCHE)
    assert e["depense_usd"] == pytest.approx(d["cout_usd"], abs=2e-6)
    lignes = [l for l in journal_lu(j) if l.get("chemin") == FIBRES]
    assert len(lignes) == 4 and lignes[-1]["recherches"] == 4 and all(l["statut_fibre"] == "succeeded" for l in lignes)
    assert all(len(l["empreinte_arguments"]) == 64 for l in lignes)
    rendus = [l["tool_calls_rendus"] for l in journal_lu(j) if l.get("chemin") == "/v1/chat/completions"]
    assert rendus == [2, 2, 0]
    compte = json.load(OUVREUR.open(url_amont + "/faux/compteurs"))
    assert compte["fibres"] == 4 and compte["chat"] == 3 and compte["declarations"] == 1


def test_flux_reassemble_les_tool_calls(banc):
    url, _, _, _ = banc(["--appels-par-tour", "2"])
    statut, rep = requete(url, "/v1/chat/completions", dict(SAIN, tools=[DECLARATION]))
    assert statut == 200
    choix = rep["choices"][0]
    assert choix["finish_reason"] == "tool_calls"
    appels = choix["message"]["tool_calls"]
    assert [a["id"] for a in appels] == ["web_search:1", "web_search:2"]
    assert all(a["function"]["name"] == "web_search" and json.loads(a["function"]["arguments"])["query"] for a in appels)


def test_sans_outil_comportement_v3_garde(banc):
    url, j, _, _ = banc()
    statut, rep = requete(url, "/v1/chat/completions", SAIN)
    assert statut == 200 and rep["choices"][0]["message"]["content"] == "Bonjour le monde."
    assert journal_lu(j)[-1]["tool_calls_rendus"] == 0


def test_declaration_variante_apprise_par_le_relais(banc):
    """Une déclaration de l'amont différente de la doc n'est admise qu'après lecture par le relais."""
    url, _, _, _ = banc(["--declaration-variante"])
    statut, rep = requete(url, DECL)
    assert statut == 200
    variante = rep["tools"][0]
    assert variante != DECLARATION
    assert requete(url, "/v1/chat/completions", dict(SAIN, tools=[variante]))[0] == 200
    code, d, r = commande(url)
    assert code == 0, r.stdout


# --- outils interdits -----------------------------------------------------------------------------------------------

AUTRE = {"type": "function", "function": {"name": "get_weather", "parameters": {"type": "object", "properties": {}}}}


@pytest.mark.parametrize("champs", [
    {"tools": [AUTRE]},
    {"tools": [DECLARATION, AUTRE]},
    {"tools": [{"type": "builtin_function", "function": {"name": "$web_search"}}]},
    {"tools": [dict(DECLARATION, function=dict(DECLARATION["function"], description="autre"))]},
    {"tools": [{"type": "web_search"}]},
    {"tools": DECLARATION},
    {"tools": [DECLARATION], "tool_choice": {"type": "function", "function": {"name": "get_weather"}}},
    {"tool_choice": "required"},
    {"functions": [AUTRE["function"]]},
], ids=["autre_fonction", "deux_outils", "builtin_web_search", "declaration_alteree", "type_web_search",
        "tools_non_liste", "tool_choice_autre", "tool_choice_sans_tools", "ancien_functions"])
def test_outil_interdit_refuse_sans_envoi(banc, champs):
    url, j, url_amont, _ = banc()
    statut, rep = requete(url, "/v1/chat/completions", dict(SAIN, **champs))
    assert statut == 400, rep
    assert json.load(OUVREUR.open(url_amont + "/faux/compteurs"))["chat"] == 0
    assert etat(url)["depense_usd"] == 0


def test_outils_refuses_si_recherche_inactive(banc):
    url, _, _, _ = banc(recherches=0)
    assert requete(url, "/v1/chat/completions", dict(SAIN, tools=[DECLARATION]))[0] == 400
    assert requete(url, FIBRES, {"name": "web_search", "arguments": "{\"query\": \"x\"}"})[0] == 403
    assert requete(url, DECL)[0] == 403


@pytest.mark.parametrize("corps", [
    {"name": "fetch", "arguments": "{\"url\": \"https://exemple.org\"}"},
    {"name": "web_search", "arguments": {"query": "x"}},
    {"name": "web_search", "arguments": "pas du json"},
    {"name": "web_search", "arguments": "[1, 2]"},
    {"name": "web_search", "arguments": "{\"query\": \"x\"}", "en_plus": 1},
], ids=["autre_nom", "arguments_objet", "arguments_illisibles", "arguments_liste", "champ_en_plus"])
def test_fibre_mal_formee_refusee_sans_envoi(banc, corps):
    url, _, url_amont, _ = banc()
    assert requete(url, FIBRES, corps)[0] == 400
    assert json.load(OUVREUR.open(url_amont + "/faux/compteurs"))["fibres"] == 0
    assert etat(url)["recherches"] == 0


def test_autre_formule_refusee(banc):
    url, _, _, _ = banc()
    statut, _ = requete(url, "/v1/formulas/moonshot/fetch:latest/fibers", {"name": "fetch", "arguments": "{}"})
    assert statut == 403
    assert requete(url, FIBRES + "?x=1", {"name": "web_search", "arguments": "{}"})[0] == 403


# --- boucle bornée --------------------------------------------------------------------------------------------------

def test_boucle_bornee_en_tours(banc):
    """L'amont rend toujours des appels (même sous tool_choice none) : la commande s'arrête à --max-tours, code 5."""
    url, _, url_amont, _ = banc(["--toujours-outil"])
    code, d, r = commande(url, options=["--max-tours", "3"])
    assert code == 5 and "boucle non close" in d["erreur"], r.stdout
    assert d["tours"] == 3 and d["recherches"] == 2
    assert json.load(OUVREUR.open(url_amont + "/faux/compteurs"))["chat"] == 3


def test_borne_de_recherches_impose_la_fin(banc):
    """Borne de 3 recherches, l'amont en demande 2 par tour : la 4e n'est pas faite, la fin est imposée, code 0."""
    url, _, _, _ = banc(["--tours-outil", "5", "--appels-par-tour", "2"])
    code, d, r = commande(url, options=["--max-recherches", "3"])
    assert code == 0, r.stdout
    assert d["recherches"] == 3 and d["recherches_non_executees"] == 1 and d["tours"] == 3


def test_borne_du_relais_429_impose_la_fin(banc):
    url, _, _, _ = banc(["--tours-outil", "5"], recherches=2)
    code, d, r = commande(url)
    assert code == 0, r.stdout
    assert d["recherches"] == 2 and d["recherches_non_executees"] == 1
    e = etat(url)
    assert e["recherches"] == 2 and e["refus_recherche"] == 1


def test_fibre_en_echec_rendue_au_modele(banc):
    url, _, _, _ = banc(["--fibre-echec"])
    code, d, r = commande(url)
    assert code == 0 and d["recherches"] == 1 and d["recherches_non_executees"] == 1, r.stdout


# --- plafond --------------------------------------------------------------------------------------------------------

def test_plafond_du_relais_compte_le_prix_de_recherche(banc):
    """Plafond 0,012 USD : deux recherches passent (0,010), la troisième franchirait le plafond : 402."""
    url, _, _, _ = banc((), ["--plafond-usd", "0.012", "--reserve-par-appel", "0"])
    corps = {"name": "web_search", "arguments": "{\"query\": \"x\"}"}
    assert requete(url, FIBRES, corps)[0] == 200
    assert requete(url, FIBRES, corps)[0] == 200
    statut, rep = requete(url, FIBRES, corps)
    assert statut == 402
    e = etat(url)
    assert e["recherches"] == 2 and e["depense_usd"] == pytest.approx(0.010) and e["refus_recherche"] == 1


def test_plafond_du_relais_mixte_modele_et_recherche(banc):
    url, _, _, _ = banc((), ["--plafond-usd", "0.02", "--reserve-par-appel", "0"])
    assert requete(url, "/v1/chat/completions", dict(SAIN, max_tokens=1500))[0] == 200  # réserve ≈ 0,0153
    statut, _ = requete(url, FIBRES, {"name": "web_search", "arguments": "{\"query\": \"x\"}"})
    assert statut == 200
    assert etat(url)["depense_usd"] == pytest.approx((12 * 2 + 7 * 10) / 1e6 + PRIX_RECHERCHE)


def test_budget_de_la_commande_empeche_la_recherche(banc):
    """Plafond de session trop court pour rechercher puis conclure : aucune recherche, fin imposée."""
    url, _, url_amont, _ = banc(["--tours-outil", "3"])
    code, d, r = commande(url, plafond="0.0105", options=["--marge-resultat-octets", "1000"])
    assert code == 0, r.stdout
    assert d["recherches"] == 0 and d["recherches_non_executees"] == 1
    assert json.load(OUVREUR.open(url_amont + "/faux/compteurs"))["fibres"] == 0
    assert d["cout_usd"] <= 0.0105


def test_budget_de_la_commande_trop_court_pour_appeler(banc):
    url, _, url_amont, _ = banc()
    code, d, _ = commande(url, plafond="0.0001")
    assert code == 4 and d["cout_usd"] == pytest.approx(1e-6)
    assert json.load(OUVREUR.open(url_amont + "/faux/compteurs"))["chat"] == 0


def test_prix_recherche_obligatoire(tmp_path):
    r = subprocess.run([sys.executable, "-I", "-B", "relais_kimi_v4.py", "--port", "0", "--modeles-permis", MODELE,
                        "--plafond-usd", "1", "--prix-entree", "2", "--prix-sortie", "10", "--prix-cache", "2",
                        "--max-recherches", "3"], env={"PATH": "/usr/bin:/bin", "KIMI_API_KEY": CLE}, cwd=ICI,
                       capture_output=True, text=True, timeout=30)
    assert r.returncode == 2 and "--prix-recherche" in r.stderr and CLE not in r.stderr + r.stdout


# --- clé ------------------------------------------------------------------------------------------------------------

def test_cle_jamais_au_journal_ni_en_sortie(banc):
    url, j, _, log = banc(["--tours-outil", "2"])
    code, d, r = commande(url)
    assert code == 0
    requete(url, "/v1/chat/completions", dict(SAIN, tools=[AUTRE]))
    requete(url, FIBRES, {"name": "fetch", "arguments": "{}"})
    for texte in (open(j).read(), open(log).read(), r.stdout, r.stderr, json.dumps(etat(url))):
        assert CLE not in texte
    assert etat(url)["variable_cle_encore_presente"] is False


def test_erreur_amont_sur_fibre_comptee(banc):
    url, j, _, _ = banc(["--fibre-statut-erreur", "500"])
    statut, _ = requete(url, FIBRES, {"name": "web_search", "arguments": "{\"query\": \"x\"}"})
    assert statut == 500
    e = etat(url)
    assert e["recherches"] == 1 and e["cout_recherches_usd"] == pytest.approx(PRIX_RECHERCHE)


# --- non-régression de la v3 (mêmes barrières, faux amont v3) ----------------------------------------------------

def test_v3_flux_client_refuse(banc):
    url, _, _, _ = banc()
    assert requete(url, "/v1/chat/completions", dict(SAIN, stream=True))[0] == 400


def test_v3_modele_servi_different(banc):
    url, j, _, _ = banc(["--modele-servi", "kimi-k3"])
    statut, rep = requete(url, "/v1/chat/completions", dict(SAIN, tools=[DECLARATION]))
    assert statut == 502 and "modèle servi différent" in rep["erreur"]
    assert journal_lu(j)[-1]["cout_usd"] > 0


def test_v3_flux_coupe_avant_done_pendant_un_appel_d_outil(banc):
    url, _, _, _ = banc(["--couper-apres", "2"])
    statut, rep = requete(url, "/v1/chat/completions", dict(SAIN, tools=[DECLARATION]))
    assert statut == 502 and "coupé" in rep["erreur"]


def test_v3_modele_non_permis(banc):
    url, _, _, _ = banc()
    assert requete(url, "/v1/chat/completions", dict(SAIN, model="kimi-k3"))[0] == 403


def test_v3_commande_kimi_v1_contre_relais_v4(banc):
    url, _, _, _ = banc(["--morceaux-raisonnement", "3"])
    r = subprocess.run([sys.executable, "-I", "-B", "commande_kimi_v1.py", "--url-relais", url], input="Juge ceci.",
                       capture_output=True, text=True, cwd=ICI,
                       env={"PATH": "/usr/bin:/bin", "PLAFOND_SESSION_USD": "3", "ROLE_POLE": "juge_ideation"})
    assert r.returncode == 0, r.stdout
    assert json.loads(r.stdout.strip().splitlines()[-1])["texte"] == "Bonjour le monde."
