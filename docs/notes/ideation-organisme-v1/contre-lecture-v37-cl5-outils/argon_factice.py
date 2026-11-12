"""Argon factice, local, sans réseau : lit la consigne sur l'entrée standard, consigne ce qu'il reçoit dans un journal,
rend une ligne JSON {texte, cout_usd}. Usage : python -I argon_factice.py JOURNAL MODE
Modes : ok ; controle-ko-cout (contrôle : texte « KO », coût 0,15) ; grosse-consigne-casse (contrôle ok, toute consigne de
plus de 100 000 caractères : sortie code 3 sans ligne JSON)."""

import json
import os
import re
import sys
import time

journal, mode = sys.argv[1], sys.argv[2]
consigne = sys.stdin.read()
entree = {"t": time.time(), "role": os.environ.get("ROLE_POLE"), "plafond": os.environ.get("PLAFOND_SESSION_USD"),
          "taille": len(consigne), "controle": "exactement OK" in consigne, "a_les_fiches": "## Les fiches" in consigne,
          "mode": mode, "cwd": os.getcwd()}
with open(journal, "a", encoding="utf-8") as f:
    f.write(json.dumps(entree, ensure_ascii=False) + "\n")


def sortir(texte, cout, code=0):
    print(json.dumps({"texte": texte, "cout_usd": cout}, ensure_ascii=False))
    sys.exit(code)


if entree["controle"]:
    if mode == "controle-ko-cout":
        sortir("KO", 0.15)
    sortir("OK", 0.002)
if mode == "grosse-consigne-casse" and len(consigne) > 100_000:
    print("quota de jetons dépassé", file=sys.stderr)
    sys.exit(3)
if "passe de proposition" in consigne:
    base = {"nom": "Argon idée", "type": "question", "enonce": "Énoncé falsifiable de l'idée externe.",
            "loi_predictive": {"espace_instances": "dix familles", "prediction": "effet de 0,2", "signe": "+",
                               "metrique": "rappel à fausses alertes fixées"},
            "perte_traduction": "aucune", "questions_servies": ["Q1"],
            "avantage": {"source": "programme", "texte": "avantage", "incopiable_parce_que": "raison"},
            "originalite": {"niveau": "transposition", "texte": "texte"},
            "demande_organisme": {"nature": "rien", "texte": ""},
            "cout": {"nature": "processeur", "ordre_de_grandeur": "jours"},
            "piege": "piège", "cosmetique_si": "si rien ne bouge", "anteriorite": []}
    fiches = [dict(base, nom="Argon idée 1"), dict(base, nom="Argon idée 2")]
    sortir("```json\n" + json.dumps({"fiches": fiches}, ensure_ascii=False) + "\n```", 0.3)
bloc = json.loads(re.search(r"```json\n(\[.*\])\n```", consigne, re.S).group(1))
par_nom = {f["nom"]: f["identifiant"] for f in bloc}
notes = []
for f in bloc:
    c = {k: 2 for k in ("avantage", "originalite", "falsifiabilite", "traitabilite", "robustesse")}
    n = f["nom"].lower()
    if "verbeux" in n or "occup" in n:
        c.update({"avantage": 1, "originalite": 0, "falsifiabilite": 1})
    if "sobre" in n or "jumeau" in n:
        c.update({"avantage": 3, "originalite": 2})
    notes.append({"identifiant": f["identifiant"], "criteres": c, "justifications": {}})
doublons = []
j = next((v for k, v in par_nom.items() if k.lower().startswith("jumeau")), None)
s = next((v for k, v in par_nom.items() if k.lower().startswith("sobre")), None)
if j and s:
    doublons.append([j, s])
sortir("```json\n" + json.dumps({"notes": notes, "doublons": doublons}) + "\n```", 0.4)
