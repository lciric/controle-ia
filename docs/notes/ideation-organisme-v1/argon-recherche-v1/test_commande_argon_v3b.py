"""Essais de commande_argon_v3b.py (la v3 corrigée après deux contre-lectures) devant le faux amont local v2, et de bout
en bout derrière le relais (v1 en témoin, v2) — aucune clé réelle, aucun appel à l'interface de Google. Copie de
`test_commande_argon_v3.py` (inchangée, R12), ajustée à la v3b (provision des jetons d'outil dans la garde, nouveaux champs),
plus les essais des corrections. Lancement :

    cd docs/notes/ideation-organisme-v1/argon-recherche-v1 && PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q \\
        -p no:cacheprovider test_commande_argon_v3b.py
"""

import json
import math
import os
import subprocess
import sys

import pytest

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import commande_argon_v3b as v3b  # noqa: E402 — nom importable (essais unitaires de nettoyer_web, adresse_permise)

V3B = os.path.join(ICI, "commande_argon_v3b.py")
V2 = "/opt/argon/commande_argon_v2.py"
FAUX = os.path.join(ICI, "faux_amont_gemini_recherche_v2.py")
RELAIS_V1 = os.path.join(ICI, "..", "lancement-v2", "relais_gemini_v1.py")
RELAIS_V2 = os.path.join(ICI, "relais_gemini_v2.py")
CLE = "cle-FACTICE-tres-secrete-42"  # factice : jamais une vraie clé
CLE_DU_RELAIS = "cle-factice-du-relais-AIzaTEST-9876543210"  # factice : la « vraie » clé que seul le relais détient
CONSIGNE = "Propose trois idées de moniteurs pour le contrôle des agents.\n" * 20
PRIX_E, PRIX_S = 8.3, 41.5
PROVISION_OUTIL = 32768


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


def lancer_commande(script, url, *options, plafond="3", consigne=CONSIGNE, cle=CLE):
    env = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "PLAFOND_SESSION_USD": plafond, "ROLE_POLE": "proposeur_ideation",
           "GEMINI_API_KEY": cle}
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


CHAMPS_V3B = {"requetes_web", "sources_web", "recherche_web", "requetes_web_facturees", "requetes_web_origine",
              "prix_requete_web_usd", "max_requetes_web_pire_cas", "cout_recherche_usd", "appuis_web", "outil_jetons",
              "provision_outil_jetons", "supplement_recherche_usd"}


# --- (a) sans l'option : comportement de la v2 ---------------------------------------------------------------------------

def test_sans_outil_meme_corps_et_meme_sortie_que_la_v2(amont):
    url, journal = amont()
    code2, obj2, _, _ = lancer_commande(V2, url)
    code3, obj3, _, _ = lancer_commande(V3B, url)
    j = journal()
    gen2, gen3 = corps_de(j, "generateContent")
    cpt2, cpt3 = corps_de(j, "countTokens")
    assert gen3 == gen2 and cpt3 == cpt2
    assert "tools" not in gen3 and set(gen3) == {"contents", "generationConfig"}
    assert code2 == code3 == 0
    assert obj3["version"] == "commande-argon-v3b" and obj2["version"] == "commande-argon-v2"
    assert obj3["requetes_web"] == [] and obj3["sources_web"] == [] and obj3["recherche_web"] is False
    assert obj3["provision_outil_jetons"] is None and obj3["supplement_recherche_usd"] is None
    commun3 = {k: v for k, v in obj3.items() if k not in CHAMPS_V3B | {"version"}}
    commun2 = {k: v for k, v in obj2.items() if k != "version"}
    assert commun3 == commun2  # même texte, même coût, même garde, même diagnostic
    assert "Sources consultées" not in obj3["texte"]


def test_sans_outil_garde_identique_a_la_v2_au_bord_du_plafond(amont):
    """La provision d'outil n'est comptée qu'avec --recherche-web : sans elle, même refus et même acceptation que la v2."""
    url, _ = amont()
    for plafond in ("0.45", "0.6", "0.9"):
        c2, o2, _, _ = lancer_commande(V2, url, "--sans-compter-jetons", plafond=plafond)
        c3, o3, _, _ = lancer_commande(V3B, url, "--sans-compter-jetons", plafond=plafond)
        assert c2 == c3 and o2["pire_cas_usd"] == o3["pire_cas_usd"] and o2["cout_usd"] == o3["cout_usd"]


# --- (a, d) avec l'option : l'outil google_search, et rien d'autre ------------------------------------------------------

def test_avec_recherche_le_corps_porte_exactement_l_outil(amont):
    url, journal = amont()
    _, obj2, _, _ = lancer_commande(V2, url)
    code, obj, _, _ = lancer_commande(V3B, url, "--recherche-web")
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
    # le reste du plafond paie d'abord 20 requêtes à 0,05 USD et 32 768 jetons d'outil au prix d'entrée, puis la provision
    # de pensée, puis la sortie
    garde = obj["entree_jetons_garde"]
    fixe = garde * PRIX_E / 1e6 + 20 * 0.05 + PROVISION_OUTIL * PRIX_E / 1e6
    attendu = min(65536, math.floor((3 - fixe) / (PRIX_S / 1e6)) - 8192)
    assert gen3["generationConfig"]["maxOutputTokens"] == attendu < gen2["generationConfig"]["maxOutputTokens"]
    assert obj["pire_cas_usd"] <= 3 and obj["provision_outil_jetons"] == PROVISION_OUTIL
    assert obj["pire_cas_usd"] == pytest.approx(fixe + (attendu + 8192) * PRIX_S / 1e6, abs=1e-6)


# --- (b) sources dans le texte et le JSON ---------------------------------------------------------------------------------

def test_sources_dans_le_texte_et_le_json(amont):
    url, _ = amont()
    code, obj, _, _ = lancer_commande(V3B, url, "--recherche-web")
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
    assert obj["supplement_recherche_usd"] == 0 and obj["avertissements"] == []


# --- (c) coût ------------------------------------------------------------------------------------------------------------

@pytest.mark.parametrize("prix", ["0.05", "0.014"])
def test_cout_jetons_plus_requetes_fois_prix(amont, prix):
    url, _ = amont()
    code, obj, _, _ = lancer_commande(V3B, url, "--recherche-web", "--prix-requete-web-usd", prix)
    assert code == 0 and obj["cout_origine"] == "usage"
    assert obj["requetes_web_facturees"] == 2
    assert obj["cout_recherche_usd"] == pytest.approx(2 * float(prix))
    assert obj["cout_usd"] == pytest.approx(cout_jetons(obj) + 2 * float(prix), rel=1e-12)


def test_jetons_d_outil_comptes_au_prix_d_entree(amont):
    url, _ = amont("--usage-outil", "1000")
    code, obj, _, erreurs = lancer_commande(V3B, url, "--recherche-web")
    assert code == 0 and obj["outil_jetons"] == 1000
    assert obj["cout_usd"] == pytest.approx(cout_jetons(obj) + 1000 * PRIX_E / 1e6 + 2 * 0.05, rel=1e-12)
    assert "toolUsePromptTokenCount" in erreurs


def test_garde_pire_cas_refuse_un_plafond_trop_bas(amont):
    url, journal = amont()
    # 0,9 USD : assez sans recherche (≈ 0,51 USD de pire cas minimal), pas avec 20 requêtes à 0,05 USD
    code, obj, _, erreurs = lancer_commande(V3B, url, "--recherche-web", "--sans-compter-jetons", plafond="0.9")
    assert code == 4 and obj["envoye"] is False and obj["cout_usd"] == 1e-6 and obj["cout_origine"] == "plancher"
    assert "20 requêtes de recherche" in obj["erreur"] and "rien envoyé" in obj["erreur"]
    assert "32768 jetons d'outil" in obj["erreur"]
    assert journal() == []  # rien n'est parti
    code, obj, _, _ = lancer_commande(V3B, url, "--recherche-web", plafond="0.9")  # avec countTokens (gratuit)
    assert code == 4 and obj["envoye"] is False
    assert corps_de(journal(), "generateContent") == []
    code, obj, _, _ = lancer_commande(V3B, url, "--sans-compter-jetons", plafond="0.9")  # même plafond, sans recherche
    assert code == 0


def test_garde_compte_la_provision_d_outil(amont):
    """Un plafond qui passe sans provision d'outil et non avec : refusé sans envoi ; accepté avec une provision nulle."""
    url, journal = amont()
    # pire cas minimal sans provision d'outil : entrée + 1 USD + (4 096 + 8 192) × 41,5e-6 ≈ 1,53 USD ; la provision ajoute
    # 32 768 × 8,3e-6 ≈ 0,27 USD
    code, obj, _, _ = lancer_commande(V3B, url, "--recherche-web", "--sans-compter-jetons", plafond="1.6")
    assert code == 4 and obj["envoye"] is False and journal() == []
    code, obj, _, _ = lancer_commande(V3B, url, "--recherche-web", "--sans-compter-jetons", "--provision-outil-jetons",
                                      "0", plafond="1.6")
    assert code == 0 and obj["provision_outil_jetons"] == 0


def test_grounding_absent_cout_au_maximum_signale(amont):
    url, _ = amont("--sans-grounding")
    code, obj, _, erreurs = lancer_commande(V3B, url, "--recherche-web")
    assert code == 0
    assert obj["requetes_web"] == [] and obj["sources_web"] == []
    assert obj["requetes_web_facturees"] == 20 and obj["requetes_web_origine"].startswith("maximum_pire_cas")
    assert obj["cout_usd"] == pytest.approx(cout_jetons(obj) + 20 * 0.05, rel=1e-12)
    assert any("groundingMetadata absent" in a for a in obj["avertissements"])
    assert "groundingMetadata absent" in erreurs
    assert "groundingMetadata absent" in obj["texte"]


def test_requetes_illisibles_cout_au_maximum(amont):
    url, _ = amont("--sans-requetes")
    code, obj, _, _ = lancer_commande(V3B, url, "--recherche-web", "--max-requetes-web-pire-cas", "7")
    assert code == 0 and obj["requetes_web_facturees"] == 7 and len(obj["sources_web"]) == 3
    assert obj["cout_usd"] == pytest.approx(cout_jetons(obj) + 7 * 0.05, rel=1e-12)
    assert any("webSearchQueries" in a for a in obj["avertissements"])


def test_requetes_au_dela_du_pire_cas_code_8(amont):
    url, _ = amont("--requetes", "5")
    code, obj, _, _ = lancer_commande(V3B, url, "--recherche-web", "--max-requetes-web-pire-cas", "3")
    assert code == 8 and obj["texte"] == "" and obj["cout_origine"] == "usage"
    assert obj["cout_usd"] == pytest.approx(cout_jetons(obj) + 5 * 0.05, rel=1e-12)
    assert "au-delà du pire cas" in obj["erreur"]
    assert obj["supplement_recherche_usd"] == pytest.approx(2 * 0.05)


# --- v3b (1) : usage illisible et requêtes au-delà du maximum --------------------------------------------------------------

@pytest.mark.parametrize("usage", [("--sans-usage",), ("--usage-outil", "-1")])
def test_usage_absent_et_requetes_au_dela_du_maximum_cout_jamais_sous_estime(amont, usage):
    url, _ = amont("--requetes", "30", *usage)
    code, obj, _, _ = lancer_commande(V3B, url, "--recherche-web")  # maximum 20
    assert code == 8, obj["erreur"]
    assert obj["texte"] == "" and obj["cout_origine"] == "pire_cas" and obj["requetes_web_facturees"] == 30
    assert obj["supplement_recherche_usd"] == pytest.approx(10 * 0.05)
    assert obj["cout_usd"] == pytest.approx(obj["pire_cas_usd"] + 10 * 0.05, abs=1e-9)
    assert obj["cout_usd"] >= obj["pire_cas_usd"] + 0.5 - 1e-9  # au moins le minimum facturé des 10 requêtes de plus
    assert "au-delà du pire cas" in obj["erreur"] and "30 lues" in obj["erreur"]


@pytest.mark.parametrize("usage", [("--sans-usage",), ("--usage-outil", "-1")])
def test_usage_illisible_sans_requetes_en_trop_reste_code_5_au_pire_cas(amont, usage):
    url, _ = amont(*usage)
    code, obj, _, _ = lancer_commande(V3B, url, "--recherche-web")
    assert code == 5 and obj["cout_origine"] == "pire_cas" and obj["cout_usd"] == obj["pire_cas_usd"]
    assert obj["supplement_recherche_usd"] == 0


# --- v3b (2) : requêtes vides, sources présentes ---------------------------------------------------------------------------

def test_requetes_vides_mais_sources_rendues_au_moins_une_requete_comptee(amont):
    url, _ = amont("--requetes-vides")
    code, obj, _, erreurs = lancer_commande(V3B, url, "--recherche-web")
    assert code == 0 and len(obj["sources_web"]) == 3
    assert obj["requetes_web_facturees"] == 20 >= 1
    assert obj["requetes_web_origine"] == "maximum_pire_cas (requêtes vides, sources présentes)"
    assert obj["cout_usd"] == pytest.approx(cout_jetons(obj) + 20 * 0.05, rel=1e-12)
    assert any("webSearchQueries vide" in a for a in obj["avertissements"]) and "webSearchQueries vide" in erreurs


def test_requetes_vides_sans_aucun_temoin_zero_requete(amont):
    url, _ = amont("--grounding-vide")
    code, obj, _, _ = lancer_commande(V3B, url, "--recherche-web")
    assert code == 0 and obj["requetes_web_facturees"] == 0 and obj["cout_recherche_usd"] == 0
    assert obj["requetes_web_origine"] == "webSearchQueries"
    assert obj["cout_usd"] == pytest.approx(cout_jetons(obj), rel=1e-12)


# --- v3b (3) : jetons d'outil au-delà de la provision ----------------------------------------------------------------------

def test_cout_au_dela_du_plafond_n_est_pas_un_succes(amont):
    url, _ = amont("--usage-outil", "400000")
    code, obj, _, _ = lancer_commande(V3B, url, "--recherche-web")
    assert code == 9 and obj["texte"] == "" and obj["cout_origine"] == "usage"
    assert obj["cout_usd"] > 3  # le coût réel est rendu, jamais sous-estimé
    assert obj["cout_usd"] == pytest.approx(cout_jetons(obj) + 400000 * PRIX_E / 1e6 + 2 * 0.05, rel=1e-12)
    assert "au-delà de la provision" in obj["erreur"] and "400000" in obj["erreur"]


def test_jetons_d_outil_a_la_provision_exacte_succes_sous_le_pire_cas(amont):
    url, _ = amont("--usage-outil", str(PROVISION_OUTIL))
    code, obj, _, _ = lancer_commande(V3B, url, "--recherche-web")
    assert code == 0 and obj["cout_usd"] <= obj["pire_cas_usd"] <= 3
    url, _ = amont("--usage-outil", str(PROVISION_OUTIL + 1))
    code, obj, _, _ = lancer_commande(V3B, url, "--recherche-web")
    assert code == 9


def test_ordre_des_echecs_pensees_puis_requetes_puis_outil(amont):
    url, _ = amont("--pensees", "9000", "--requetes", "30", "--usage-outil", "400000")
    assert lancer_commande(V3B, url, "--recherche-web")[0] == 7
    url, _ = amont("--requetes", "30", "--usage-outil", "400000")
    assert lancer_commande(V3B, url, "--recherche-web")[0] == 8
    url, _ = amont("--usage-outil", "400000", "--modele-servi", "gemini-9-autre")
    assert lancer_commande(V3B, url, "--recherche-web")[0] == 9  # prime sur le code 5


# --- v3b (4) : parties refusées --------------------------------------------------------------------------------------------

@pytest.mark.parametrize("partie", ["functionCall", "functionResponse", "executableCode", "codeExecutionResult"])
def test_parties_d_appel_ou_de_code_refusees(amont, partie):
    url, _ = amont("--partie", partie)
    code, obj, _, _ = lancer_commande(V3B, url, "--recherche-web")
    assert code == 5 and obj["texte"] == "" and partie in obj["erreur"]
    assert "seul google_search est déclaré" in obj["erreur"]
    code, obj, _, _ = lancer_commande(V3B, url)
    assert code == 5 and "aucun outil n'est déclaré" in obj["erreur"]


# --- v3b (5) : la clé ne sort jamais --------------------------------------------------------------------------------------

@pytest.mark.parametrize("options_amont", [(), ("--refus", "http400"), ("--cle-dans-titre",), ("--sans-grounding",),
                                           ("--modele-servi", "autre"), ("--cle-dans-modele",), ("--cle-dans-fin",),
                                           ("--cle-coupee-dans-titre",)])
def test_cle_jamais_dans_la_sortie(amont, options_amont):
    url, journal = amont(*options_amont)
    code, obj, sortie, erreurs = lancer_commande(V3B, url, "--recherche-web")
    assert CLE not in sortie and CLE not in erreurs
    assert all(e["cle_presente"] for e in journal())  # la clé (factice) est bien partie dans l'en-tête
    if options_amont == ("--refus", "http400"):
        assert "[clé]" in obj["erreur"]
    if options_amont == ("--cle-dans-titre",):
        assert code == 0 and "[clé]" in obj["sources_web"][0]["titre"]
    if options_amont == ("--cle-dans-modele",):
        assert code == 0 and obj["modele_servi"] == "gemini-4-argon-[clé]"
    if options_amont == ("--cle-dans-fin",):
        assert code == 5 and obj["fin"] == "AUTRE [clé]"
    if options_amont == ("--cle-coupee-dans-titre",):
        assert code == 0 and "[clé]" in obj["sources_web"][0]["titre"]
        m = len(CLE) // 2
        assert CLE[:m] + " " + CLE[m:] not in sortie


def test_nettoyer_web_masque_avant_et_apres_le_nettoyage():
    m = len(CLE) // 2
    assert v3b.nettoyer_web(f"a {CLE[:m]}\x00{CLE[m:]} b", CLE) == "a[clé]b"  # forme compacte, masquée
    assert v3b.nettoyer_web(f"a {CLE[:m]}\n{CLE[m:]} b", CLE) == "a[clé]b"
    assert v3b.nettoyer_web(f"titre\x00propre", CLE) == "titre propre"  # sans clé : rien ne change
    assert v3b.nettoyer_web(f"x{CLE}", CLE, 3) == "x[c…"  # le masquage passe avant la coupe
    assert v3b.masquer_objet({"a": [CLE, {CLE: 1}], "b": 2.0}, CLE) == {"a": ["[clé]", {"[clé]": 1}], "b": 2.0}


def _lancer_relais(script, amont_url):
    env = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "GEMINI_API_KEY": CLE_DU_RELAIS}
    p = subprocess.Popen([sys.executable, "-I", "-B", script, "--port", "0", "--amont", amont_url], env=env,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    ligne = p.stdout.readline()
    assert ligne.startswith("relais prêt sur "), ligne
    return p, ligne.split()[3]


def _arreter(p):
    p.kill()  # par le PID (R10)
    p.communicate(timeout=10)


@pytest.mark.parametrize("options_amont", [("--cle-dans-titre",), ("--refus", "http400"), ("--cle-dans-modele",)])
def test_bout_en_bout_relais_v2_la_vraie_cle_ne_sort_pas(amont, options_amont):
    url, journal = amont(*options_amont)
    relais, url_relais = _lancer_relais(RELAIS_V2, url.replace("/v1beta", ""))
    try:
        code, obj, sortie, erreurs = lancer_commande(V3B, url_relais + "/v1beta", "--recherche-web", cle="factice-relais")
    finally:
        _arreter(relais)
    assert CLE_DU_RELAIS not in sortie and CLE_DU_RELAIS not in erreurs
    assert all(e["cle_presente"] for e in journal())
    if options_amont == ("--cle-dans-titre",):
        assert code == 0 and obj["sources_web"][0]["titre"] == "titre avec clé [clé]"
    if options_amont == ("--refus", "http400"):
        assert code == 3 and "[clé]" in obj["erreur"]
    if options_amont == ("--cle-dans-modele",):
        assert code == 0 and obj["modele_servi"] == "gemini-4-argon-[clé]"


def test_temoin_relais_v1_laisse_passer_la_vraie_cle_dans_le_corps(amont):
    """Artefact (R5) : le défaut que corrige le relais v2. Avec le relais v1, la commande ne peut masquer que la clé factice
    qu'elle détient ; la vraie clé recopiée par l'amont dans un titre traverse jusqu'à la sortie."""
    url, _ = amont("--cle-dans-titre")
    relais, url_relais = _lancer_relais(RELAIS_V1, url.replace("/v1beta", ""))
    try:
        code, obj, sortie, _ = lancer_commande(V3B, url_relais + "/v1beta", "--recherche-web", cle="factice-relais")
    finally:
        _arreter(relais)
    assert code == 0 and CLE_DU_RELAIS in obj["sources_web"][0]["titre"]


# --- v3b (6) : dernière ligne lisible par splitlines ----------------------------------------------------------------------

def test_derniere_ligne_lisible_par_splitlines_avec_separateur_unicode(amont):
    url, _ = amont("--texte-separateurs")
    code, obj, sortie, _ = lancer_commande(V3B, url, "--recherche-web")
    assert code == 0
    # ce que fait AdaptateurCommandeExterne.lire_derniere_ligne (orchestrateur-v52/arbre/pole/adaptateurs.py)
    lignes = [l for l in sortie.splitlines() if l.strip()]
    lu = json.loads(lignes[-1])
    assert len(lignes) == 1 and lu == obj
    assert " ligne paragraphe\x85suite" in lu["texte"]
    assert " " not in sortie and " " not in sortie and "\x85" not in sortie


# --- v3b (7) : adresses des sources ---------------------------------------------------------------------------------------

@pytest.mark.parametrize("uri, schema", [("javascript:alert(1)//x", "javascript"), ("data:text/html,x", "data"),
                                         ("file:///etc/passwd", "file"), ("https:///sans-hote", "https sans hôte"),
                                         ("sans-schema", "absent")])
def test_adresse_non_web_refusee(amont, uri, schema):
    url, _ = amont("--uri-source", uri)
    code, obj, _, _ = lancer_commande(V3B, url, "--recherche-web")
    assert code == 0
    assert obj["sources_web"][0]["uri"] == f"[adresse refusée : schéma {schema}]"
    assert uri not in obj["texte"] and uri not in json.dumps(obj["sources_web"])
    assert any("adresse(s) de source refusée(s)" in a for a in obj["avertissements"])
    assert obj["sources_web"][1]["uri"].startswith("https://")


def test_adresse_permise():
    assert v3b.adresse_permise("https://exemple.org/a") == (True, None)
    assert v3b.adresse_permise("http://exemple.org") == (True, None)
    assert v3b.adresse_permise("HTTPS://exemple.org") == (True, None)
    assert v3b.adresse_permise("http://[::1") == (False, "illisible")


# --- v3b (8) : bornes du texte ajouté -------------------------------------------------------------------------------------

def test_bornes_des_sources_et_de_la_section(amont):
    url, _ = amont("--sources", "1000", "--requetes", "300", "--longueur-champs", "600")
    code, obj, _, _ = lancer_commande(V3B, url, "--recherche-web", "--max-requetes-web-pire-cas", "400",
                                      "--prix-requete-web-usd", "0.001")
    assert code == 0 and obj["requetes_web_facturees"] == 300  # le compte facturé n'est jamais coupé
    assert len(obj["requetes_web"]) == 50 and len(obj["sources_web"]) == 50
    assert all(len(q) <= 201 for q in obj["requetes_web"])
    assert all(len(s["titre"]) <= 201 and len(s["uri"]) <= 501 for s in obj["sources_web"])
    section = obj["texte"].split("Réponse factice d'Argon.", 1)[1]
    assert len(section) <= v3b.LONGUEUR_MAX_SECTION + 200 and "section coupée" in section
    assert any("section des sources coupée" in a for a in obj["avertissements"])
    assert any("950 source(s) au-delà" in a for a in obj["avertissements"])
    assert any("300 requêtes lues : 50 listées" in a for a in obj["avertissements"])


# --- non-conformités ----------------------------------------------------------------------------------------------------

def test_modele_servi_different_code_5(amont):
    url, _ = amont("--modele-servi", "gemini-9-autre")
    code, obj, _, _ = lancer_commande(V3B, url, "--recherche-web")
    assert code == 5 and obj["texte"] == "" and obj["cout_origine"] == "usage"
    assert "gemini-9-autre" in obj["erreur"]
    assert obj["cout_usd"] == pytest.approx(cout_jetons(obj) + 2 * 0.05, rel=1e-12)  # la recherche est comptée


def test_reponse_tronquee_et_bloquee_code_5(amont):
    url, _ = amont("--tronquee")
    code, obj, _, _ = lancer_commande(V3B, url, "--recherche-web")
    assert code == 5 and "MAX_TOKENS" in obj["erreur"]
    url, _ = amont("--refus", "bloque")
    code, obj, _, _ = lancer_commande(V3B, url, "--recherche-web")
    assert code == 5 and "bloquée" in obj["erreur"]


def test_refus_http_de_l_outil_code_3_sans_repli(amont):
    url, journal = amont("--refus", "http400")
    code, obj, _, _ = lancer_commande(V3B, url, "--recherche-web")
    assert code == 3 and obj["cout_origine"] == "plancher" and obj["cout_usd"] == 1e-6
    assert "google_search déclaré" in obj["erreur"] and "aucun repli" in obj["erreur"]
    assert len(corps_de(journal(), "generateContent")) == 1  # aucune relance


def test_reglages_refuses_code_2(amont):
    url, journal = amont()
    code, _, _, _ = lancer_commande(V3B, url, "--recherche-web", "--prix-requete-web-usd", "0")
    assert code == 2
    code, _, _, _ = lancer_commande(V3B, url, "--recherche-web", "--max-requetes-web-pire-cas", "0")
    assert code == 2
    code, _, _, _ = lancer_commande(V3B, url, "--recherche-web", "--provision-outil-jetons", "-1")
    assert code == 2
    assert journal() == []


# --- enveloppe v4b -------------------------------------------------------------------------------------------------------

def test_enveloppe_v4b_ne_change_que_la_commande_lancee():
    v4 = open(os.path.join(ICI, "appel-argon-v4.sh"), encoding="utf-8").read().splitlines()
    v4b = open(os.path.join(ICI, "appel-argon-v4b.sh"), encoding="utf-8").read().splitlines()
    # v4b = la ligne d'interpréteur, quatre lignes de commentaire ajoutées, puis la v4 entière où seul le chemin change
    assert v4b[0] == v4[0] == "#!/bin/sh"
    assert all(x.startswith("# ") for x in v4b[1:5])
    attendu = [x.replace("/opt/argon/commande_argon_v3.py", "/opt/argon/commande_argon_v3b.py") for x in v4[1:]]
    assert v4b[5:] == attendu
    assert sum(a != b for a, b in zip(v4b[5:], v4[1:])) == 1  # une seule ligne différente : celle de exec
    assert subprocess.run(["sh", "-n", os.path.join(ICI, "appel-argon-v4b.sh")]).returncode == 0
