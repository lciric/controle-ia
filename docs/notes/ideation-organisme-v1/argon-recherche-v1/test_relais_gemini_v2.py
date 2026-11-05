"""Essais de `relais_gemini_v2.py` : **toute la suite de la v1** (`lancement-v2/test_relais_gemini_v1.py`, inchangée, R12)
rejouée sur la v2, plus les essais du masquage de la clé dans le corps relayé. Clé factice, faux amont local, aucun réseau
sortant, aucun appel payant.

La suite v1 est importée telle quelle ; ses deux références au relais (`RELAIS`, chemin du script lancé dans son processus,
et `relais`, module des essais unitaires) sont redirigées vers la v2 avant la collecte. Seul l'essai qui lit la version
(`test_etat_appels_refus_octets`) est redéfini ici, avec `relais-gemini-v2`.

Lancer (depuis ce dossier) : `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider test_relais_gemini_v2.py`
"""

import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
LANCEMENT_V2 = os.path.normpath(os.path.join(ICI, "..", "lancement-v2"))
sys.path.insert(0, LANCEMENT_V2)  # test_relais_gemini_v1, test_commande_argon_v2 (FauxGemini), relais_gemini_v1
sys.path.insert(0, ICI)

import relais_gemini_v2  # noqa: E402
import test_relais_gemini_v1 as suite_v1  # noqa: E402

suite_v1.RELAIS = os.path.join(ICI, "relais_gemini_v2.py")
suite_v1.relais = relais_gemini_v2

from test_relais_gemini_v1 import *  # noqa: E402,F401,F403 — fixtures et essais de la v1, rejoués sur la v2
from test_relais_gemini_v1 import CHEMIN_GEN, CLE_REELLE, CORPS, appeler, etat  # noqa: E402


def test_etat_appels_refus_octets(amont, relais_proc):  # redéfini : la version lue est celle de la v2
    e0 = etat(relais_proc.url)
    assert e0["appels"] == 0 and e0["refus"] == 0 and e0["octets_envoyes"] == 0 and e0["octets_recus"] == 0
    assert e0["max_appels"] == 64 and e0["max_octets_corps"] == 8_000_000 and e0["modeles"] == ["gemini-4-argon"]
    assert e0["amont"] == amont.url and e0["mandataire"] is False and e0["version"] == "relais-gemini-v2"
    corps = json.dumps(CORPS).encode("utf-8")
    appeler(relais_proc.url, CHEMIN_GEN, corps)
    appeler(relais_proc.url, "/v1beta/models/autre:generateContent", corps)
    e1 = etat(relais_proc.url)
    assert e1["appels"] == 1 and e1["refus"] == 1 and e1["appels_restants"] == 63
    assert e1["octets_envoyes"] == len(corps) and e1["octets_recus"] == len(json.dumps(amont.objet).encode("utf-8"))
    assert e1["reponses_par_statut"] == {"200": 1}


def test_les_essais_lancent_bien_la_v2():
    assert suite_v1.RELAIS.endswith("relais_gemini_v2.py") and suite_v1.relais.VERSION == "relais-gemini-v2"


# === v2 : la vraie clé masquée dans le corps relayé ======================================================================

def test_cle_dans_le_corps_masquee_et_longueur_recalculee(amont, relais_proc):
    amont.objet = {"candidates": [{"content": {"role": "model", "parts": [{"text": f"recopie {CLE_REELLE} et {CLE_REELLE}"}]},
                                   "finishReason": "STOP"}], "modelVersion": f"gemini-4-argon-{CLE_REELLE}",
                   "usageMetadata": {"promptTokenCount": 1}}
    statut, en_tetes, octets = appeler(relais_proc.url, CHEMIN_GEN, CORPS)
    assert statut == 200 and CLE_REELLE.encode() not in octets
    assert int(en_tetes["content-length"]) == len(octets)  # recalculé sur le corps relayé
    objet = json.loads(octets)
    assert objet["candidates"][0]["content"]["parts"][0]["text"] == "recopie [clé] et [clé]"
    assert objet["modelVersion"] == "gemini-4-argon-[clé]"
    (e,) = relais_proc.entrees_journal()
    assert e["cle_masquee_dans_reponse"] == 3 and e["modele_servi"] == "gemini-4-argon-[clé]"
    assert e["octets_reponse"] == len(json.dumps(amont.objet).encode("utf-8"))  # taille reçue de l'amont
    assert CLE_REELLE not in relais_proc.journal_brut()


def test_cle_dans_un_corps_d_erreur_masquee(amont, relais_proc):
    amont.code, amont.objet = 400, {"error": {"code": 400, "status": "INVALID_ARGUMENT", "message": f"clé {CLE_REELLE}"}}
    statut, _, octets = appeler(relais_proc.url, CHEMIN_GEN, CORPS)
    assert statut == 400 and json.loads(octets)["error"]["message"] == "clé [clé]"


def test_sans_cle_dans_le_corps_relaye_octet_pour_octet(amont, relais_proc):
    statut, _, octets = appeler(relais_proc.url, CHEMIN_GEN, CORPS)
    assert statut == 200 and octets == json.dumps(amont.objet).encode("utf-8")
    (e,) = relais_proc.entrees_journal()
    assert "cle_masquee_dans_reponse" not in e
