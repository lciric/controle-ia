"""Essais de commande_argon_v3.py (recherche Google sur option) devant le faux amont local — aucune clé réelle, aucun appel
à l'interface de Google. Lancement :

    cd docs/notes/ideation-organisme-v1/argon-recherche-v1 && PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q \\
        -p no:cacheprovider test_commande_argon_v3.py
"""

import json
import math
import os
import subprocess
import sys

import pytest

ICI = os.path.dirname(os.path.abspath(__file__))
V3 = os.path.join(ICI, "commande_argon_v3.py")
V2 = "/opt/argon/commande_argon_v2.py"
FAUX = os.path.join(ICI, "faux_amont_gemini_recherche_v1.py")
CLE = "cle-FACTICE-tres-secrete-42"  # factice : jamais une vraie clé
CONSIGNE = "Propose trois idées de moniteurs pour le contrôle des agents.\n" * 20
PRIX_E, PRIX_S = 8.3, 41.5


@pytest.fixture
def amont(tmp_path):
    """Lance un faux amont (options données) ; rend (url de base, lecteur du journal). Arrêt par le PID (R10)."""
    processus = []

    def lancer(*options):
        journal = tmp_path / f"journal-{len(processus)}.jsonl"
        p = subprocess.Popen([sys.executable, "-I", "-B", FAUX, "--port", "0", "--journal", str(journal), *options],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        processus.append(p)
        ligne = p.stdout.readline().strip()
        assert ligne.startswith("pret http://127.0.0.1:"), ligne

        def lire():
            if not journal.exists():
                return []
            return [json.loads(x) for x in journal.read_text(encoding="utf-8").splitlines() if x.strip()]

        return ligne.split(" ", 1)[1] + "/v1beta", lire

    yield lancer
    for p in processus:
        p.terminate()
        try:
            p.wait(timeout=5)
        except subprocess.TimeoutExpired:
            p.kill()
            p.wait()


def lancer_commande(script, url, *options, plafond="3", consigne=CONSIGNE):
    env = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "PLAFOND_SESSION_USD": plafond, "ROLE_POLE": "proposeur_ideation",
           "GEMINI_API_KEY": CLE}
    r = subprocess.run([sys.executable, "-I", "-B", script, "--prix-entree", str(PRIX_E), "--prix-sortie", str(PRIX_S),
                        *options, "--url-base", url], input=consigne.encode("utf-8"), capture_output=True, env=env,
                       timeout=60)
    sortie = r.stdout.decode("utf-8")
    erreurs = r.stderr.decode("utf-8")
    objet = json.loads(sortie.strip().splitlines()[-1])
    return r.returncode, objet, sortie, erreurs


def corps_de(journal, action):
    return [e["corps"] for e in journal if e["chemin"].endswith(":" + action)]


def cout_jetons(objet):
    u = objet["usage"]
    return u["entree"] * PRIX_E / 1e6 + u["sortie"] * PRIX_S / 1e6


CHAMPS_V3 = {"requetes_web", "sources_web", "recherche_web", "requetes_web_facturees", "requetes_web_origine",
             "prix_requete_web_usd", "max_requetes_web_pire_cas", "cout_recherche_usd", "appuis_web", "outil_jetons"}


# --- (a) sans l'option : comportement de la v2 ---------------------------------------------------------------------------

def test_sans_outil_meme_corps_et_meme_sortie_que_la_v2(amont):
    url, journal = amont()
    code2, obj2, _, _ = lancer_commande(V2, url)
    code3, obj3, _, _ = lancer_commande(V3, url)
    j = journal()
    gen2, gen3 = corps_de(j, "generateContent")
    cpt2, cpt3 = corps_de(j, "countTokens")
    assert gen3 == gen2 and cpt3 == cpt2
    assert "tools" not in gen3 and set(gen3) == {"contents", "generationConfig"}
    assert code2 == code3 == 0
    assert obj3["version"] == "commande-argon-v3" and obj2["version"] == "commande-argon-v2"
    assert obj3["requetes_web"] == [] and obj3["sources_web"] == [] and obj3["recherche_web"] is False
    commun3 = {k: v for k, v in obj3.items() if k not in CHAMPS_V3 | {"version"}}
    commun2 = {k: v for k, v in obj2.items() if k != "version"}
    assert commun3 == commun2  # même texte, même coût, même garde, même diagnostic
    assert "Sources consultées" not in obj3["texte"]


# --- (a, d) avec l'option : l'outil google_search, et rien d'autre ------------------------------------------------------

def test_avec_recherche_le_corps_porte_exactement_l_outil(amont):
    url, journal = amont()
    _, obj2, _, _ = lancer_commande(V2, url)
    code, obj, _, _ = lancer_commande(V3, url, "--recherche-web")
    assert code == 0, obj["erreur"]
    j = journal()
    gen2, gen3 = corps_de(j, "generateContent")
    cpt2, cpt3 = corps_de(j, "countTokens")
    assert set(gen3) == {"contents", "generationConfig", "tools"}
    assert gen3["tools"] == [{"google_search": {}}]
    assert gen3["contents"] == gen2["contents"]
    assert set(gen3["generationConfig"]) == {"maxOutputTokens", "thinkingConfig"}
    assert gen3["generationConfig"]["thinkingConfig"] == gen2["generationConfig"]["thinkingConfig"]
    assert cpt3 == cpt2 and "tools" not in cpt3  # countTokens inchangé
    # le reste du plafond paie d'abord 20 requêtes à 0,05 USD, puis la provision de pensée, puis la sortie
    garde = obj["entree_jetons_garde"]
    attendu = min(65536, math.floor((3 - garde * PRIX_E / 1e6 - 20 * 0.05) / (PRIX_S / 1e6)) - 8192)
    assert gen3["generationConfig"]["maxOutputTokens"] == attendu < gen2["generationConfig"]["maxOutputTokens"]
    assert obj["pire_cas_usd"] <= 3
    assert obj["pire_cas_usd"] == pytest.approx(garde * PRIX_E / 1e6 + 1.0 + (attendu + 8192) * PRIX_S / 1e6, abs=1e-6)


# --- (b) sources dans le texte et le JSON ---------------------------------------------------------------------------------

def test_sources_dans_le_texte_et_le_json(amont):
    url, _ = amont()
    code, obj, _, _ = lancer_commande(V3, url, "--recherche-web")
    assert code == 0
    assert obj["texte"].startswith("Réponse factice d'Argon.")
    assert "Sources consultées (recherche Google)" in obj["texte"]
    assert obj["requetes_web"] == ["requête factice 1 sur le contrôle des agents",
                                   "requête factice 2 sur le contrôle des agents"]
    assert len(obj["sources_web"]) == 3
    for i, s in enumerate(obj["sources_web"], 1):
        assert s == {"uri": f"https://vertexaisearch.cloud.google.com/grounding-api-redirect/FAUX{i}",
                     "titre": f"source-factice-{i}.example.org"}
        assert s["uri"] in obj["texte"] and s["titre"] in obj["texte"]
    for q in obj["requetes_web"]:
        assert q in obj["texte"]
    assert obj["appuis_web"] == 2 and obj["requetes_web_origine"] == "webSearchQueries"


# --- (c) coût ------------------------------------------------------------------------------------------------------------

@pytest.mark.parametrize("prix", ["0.05", "0.014"])
def test_cout_jetons_plus_requetes_fois_prix(amont, prix):
    url, _ = amont()
    code, obj, _, _ = lancer_commande(V3, url, "--recherche-web", "--prix-requete-web-usd", prix)
    assert code == 0 and obj["cout_origine"] == "usage"
    assert obj["requetes_web_facturees"] == 2
    assert obj["cout_recherche_usd"] == pytest.approx(2 * float(prix))
    assert obj["cout_usd"] == pytest.approx(cout_jetons(obj) + 2 * float(prix), rel=1e-12)


def test_jetons_d_outil_comptes_au_prix_d_entree(amont):
    url, _ = amont("--usage-outil", "1000")
    code, obj, _, erreurs = lancer_commande(V3, url, "--recherche-web")
    assert code == 0 and obj["outil_jetons"] == 1000
    assert obj["cout_usd"] == pytest.approx(cout_jetons(obj) + 1000 * PRIX_E / 1e6 + 2 * 0.05, rel=1e-12)
    assert "toolUsePromptTokenCount" in erreurs


def test_garde_pire_cas_refuse_un_plafond_trop_bas(amont):
    url, journal = amont()
    # 0,9 USD : assez sans recherche (≈ 0,51 USD de pire cas minimal), pas avec 20 requêtes à 0,05 USD
    code, obj, _, erreurs = lancer_commande(V3, url, "--recherche-web", "--sans-compter-jetons", plafond="0.9")
    assert code == 4 and obj["envoye"] is False and obj["cout_usd"] == 1e-6 and obj["cout_origine"] == "plancher"
    assert "20 requêtes de recherche" in obj["erreur"] and "rien envoyé" in obj["erreur"]
    assert journal() == []  # rien n'est parti
    code, obj, _, _ = lancer_commande(V3, url, "--recherche-web", plafond="0.9")  # avec countTokens (gratuit)
    assert code == 4 and obj["envoye"] is False
    assert corps_de(journal(), "generateContent") == []
    code, obj, _, _ = lancer_commande(V3, url, "--sans-compter-jetons", plafond="0.9")  # même plafond, sans recherche
    assert code == 0


def test_grounding_absent_cout_au_maximum_signale(amont):
    url, _ = amont("--sans-grounding")
    code, obj, _, erreurs = lancer_commande(V3, url, "--recherche-web")
    assert code == 0
    assert obj["requetes_web"] == [] and obj["sources_web"] == []
    assert obj["requetes_web_facturees"] == 20 and obj["requetes_web_origine"].startswith("maximum_pire_cas")
    assert obj["cout_usd"] == pytest.approx(cout_jetons(obj) + 20 * 0.05, rel=1e-12)
    assert any("groundingMetadata absent" in a for a in obj["avertissements"])
    assert "groundingMetadata absent" in erreurs
    assert "groundingMetadata absent" in obj["texte"]


def test_requetes_illisibles_cout_au_maximum(amont):
    url, _ = amont("--sans-requetes")
    code, obj, _, _ = lancer_commande(V3, url, "--recherche-web", "--max-requetes-web-pire-cas", "7")
    assert code == 0 and obj["requetes_web_facturees"] == 7 and len(obj["sources_web"]) == 3
    assert obj["cout_usd"] == pytest.approx(cout_jetons(obj) + 7 * 0.05, rel=1e-12)
    assert any("webSearchQueries" in a for a in obj["avertissements"])


def test_requetes_au_dela_du_pire_cas_code_8(amont):
    url, _ = amont("--requetes", "5")
    code, obj, _, _ = lancer_commande(V3, url, "--recherche-web", "--max-requetes-web-pire-cas", "3")
    assert code == 8 and obj["texte"] == "" and obj["cout_origine"] == "usage"
    assert obj["cout_usd"] == pytest.approx(cout_jetons(obj) + 5 * 0.05, rel=1e-12)
    assert "au-delà du pire cas" in obj["erreur"]


# --- non-conformités ----------------------------------------------------------------------------------------------------

def test_modele_servi_different_code_5(amont):
    url, _ = amont("--modele-servi", "gemini-9-autre")
    code, obj, _, _ = lancer_commande(V3, url, "--recherche-web")
    assert code == 5 and obj["texte"] == "" and obj["cout_origine"] == "usage"
    assert "gemini-9-autre" in obj["erreur"]
    assert obj["cout_usd"] == pytest.approx(cout_jetons(obj) + 2 * 0.05, rel=1e-12)  # la recherche est comptée


def test_reponse_tronquee_et_bloquee_code_5(amont):
    url, _ = amont("--tronquee")
    code, obj, _, _ = lancer_commande(V3, url, "--recherche-web")
    assert code == 5 and "MAX_TOKENS" in obj["erreur"]
    url, _ = amont("--refus", "bloque")
    code, obj, _, _ = lancer_commande(V3, url, "--recherche-web")
    assert code == 5 and "bloquée" in obj["erreur"]


def test_refus_http_de_l_outil_code_3_sans_repli(amont):
    url, journal = amont("--refus", "http400")
    code, obj, _, _ = lancer_commande(V3, url, "--recherche-web")
    assert code == 3 and obj["cout_origine"] == "plancher" and obj["cout_usd"] == 1e-6
    assert "google_search déclaré" in obj["erreur"] and "aucun repli" in obj["erreur"]
    assert len(corps_de(journal(), "generateContent")) == 1  # aucune relance


def test_reglages_refuses_code_2(amont):
    url, journal = amont()
    code, _, _, _ = lancer_commande(V3, url, "--recherche-web", "--prix-requete-web-usd", "0")
    assert code == 2
    code, _, _, _ = lancer_commande(V3, url, "--recherche-web", "--max-requetes-web-pire-cas", "0")
    assert code == 2
    assert journal() == []


# --- la clé ne sort jamais ----------------------------------------------------------------------------------------------

@pytest.mark.parametrize("options_amont", [(), ("--refus", "http400"), ("--cle-dans-titre",), ("--sans-grounding",),
                                           ("--modele-servi", "autre")])
def test_cle_jamais_dans_la_sortie(amont, options_amont):
    url, journal = amont(*options_amont)
    code, obj, sortie, erreurs = lancer_commande(V3, url, "--recherche-web")
    assert CLE not in sortie and CLE not in erreurs
    assert all(e["cle_presente"] for e in journal())  # la clé (factice) est bien partie dans l'en-tête
    if options_amont == ("--refus", "http400"):
        assert "[clé]" in obj["erreur"]
    if options_amont == ("--cle-dans-titre",):
        assert code == 0 and "[clé]" in obj["sources_web"][0]["titre"]


# --- enveloppe v4 --------------------------------------------------------------------------------------------------------

def test_enveloppe_v4_ne_change_que_la_commande_lancee():
    v3 = open("/opt/argon/appel-argon-v3.sh", encoding="utf-8").read().splitlines()
    v4 = open(os.path.join(ICI, "appel-argon-v4.sh"), encoding="utf-8").read().splitlines()
    # v4 = la ligne d'interpréteur, trois lignes de commentaire ajoutées, puis la v3 entière où seul le chemin change
    assert v4[0] == v3[0] == "#!/bin/sh"
    assert all(x.startswith("# ") for x in v4[1:4])
    attendu = [x.replace("/opt/argon/commande_argon_v2.py", "/opt/argon/commande_argon_v3.py") for x in v3[1:]]
    assert v4[4:] == attendu
    assert sum(a != b for a, b in zip(v4[4:], v3[1:])) == 1  # une seule ligne différente : celle de exec
    assert subprocess.run(["sh", "-n", os.path.join(ICI, "appel-argon-v4.sh")]).returncode == 0
