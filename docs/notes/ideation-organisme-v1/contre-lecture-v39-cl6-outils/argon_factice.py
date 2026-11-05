"""Argon factice (CL6) : commande externe locale, sans réseau ni clé. Lit la consigne sur l'entrée standard, consigne
l'appel, répond selon le rôle (ROLE_POLE) et imprime la ligne {"texte", "cout_usd"} attendue par l'adaptateur.

Options : --journal CHEMIN (une ligne JSON par appel) ; --cout-controle X ; --cout-plein (proposeur et juge déclarent le
plafond de session) ; --controle-ko X (contrôle « KO » au coût X) ; --casse-au-dela N (sortie 3 sans ligne si la consigne
dépasse N caractères) ; --dormir S --pids CHEMIN (dans le rôle proposeur : lance un petit-enfant qui dort S secondes, écrit
les identifiants de processus, puis dort S secondes).
"""
import json
import os
import re
import subprocess
import sys
import time

args = sys.argv[1:]


def opt(nom, defaut=None):
    return args[args.index(nom) + 1] if nom in args else defaut


consigne = sys.stdin.read()
role = os.environ.get("ROLE_POLE", "?")
plafond = float(os.environ.get("PLAFOND_SESSION_USD", "0"))
controle = "exactement OK" in consigne
if opt("--journal"):
    with open(opt("--journal"), "a", encoding="utf-8") as f:
        f.write(json.dumps({"pid": os.getpid(), "role": role, "controle": controle, "plafond": plafond,
                            "taille": len(consigne), "quand": time.time()}) + "\n")
if opt("--casse-au-dela") and len(consigne) > int(opt("--casse-au-dela")):
    print("requête trop grande (factice)", file=sys.stderr)
    sys.exit(3)
if controle:
    if opt("--controle-ko"):
        print(json.dumps({"texte": "KO", "cout_usd": float(opt("--controle-ko"))}))
    elif "--controle-au-plafond" in args:  # CL6 : pire cas, chaque contrôle coûte le plafond de SA session
        print(json.dumps({"texte": "OK", "cout_usd": plafond}))
    else:
        print(json.dumps({"texte": "OK", "cout_usd": float(opt("--cout-controle", "0.01"))}))
    sys.exit(0)
cout = plafond if "--cout-plein" in args else 0.25
if role == "juge_ideation" and opt("--dormir-juge"):  # CL6 : session du juge qui dure (interruption du bras)
    with open(opt("--pids"), "w") as f:
        f.write(f"{os.getpid()}\n")
    time.sleep(float(opt("--dormir-juge")))
if role == "proposeur_ideation":
    if opt("--dormir"):
        s = opt("--dormir")
        p = subprocess.Popen([sys.executable, "-c", f"import time; time.sleep({s})"])
        with open(opt("--pids"), "w") as f:
            f.write(f"{os.getpid()} {p.pid}\n")
        time.sleep(float(s))
    base = {"type": "question", "enonce": "Le transfert d'un moniteur vers le diffus suit-il une courbe prédite ?",
            "loi_predictive": {"espace_instances": "dix familles", "prediction": "rappel décroît", "signe": "-",
                               "metrique": "rappel à 1 % de fausses alertes"},
            "perte_traduction": "résumée par une pente", "questions_servies": ["Q4"],
            "avantage": {"source": "programme", "texte": "théorie explicite", "incopiable_parce_que": "exige la carte"},
            "originalite": {"niveau": "transposition", "texte": "détection de rupture"},
            "demande_organisme": {"nature": "ajout", "texte": "générateur"},
            "cout": {"nature": "processeur", "ordre_de_grandeur": "jours"}, "piege": "artefact de découpe",
            "cosmetique_si": "courbes plates", "anteriorite": [{"reference": "référence factice", "statut": "SUPPOSE"}]}
    suffixe = " (revue)" if "première passe" in consigne else ""
    fiches = [dict(base, nom="Argon A" + suffixe), dict(base, nom="Argon B" + suffixe)]
    print(json.dumps({"texte": "```json\n" + json.dumps({"fiches": fiches}, ensure_ascii=False) + "\n```", "cout_usd": cout}))
    sys.exit(0)
bloc = json.loads(re.search(r"```json\n(\[.*\])\n```", consigne, re.S).group(1))
par_nom = {f["nom"]: f["identifiant"] for f in bloc}
notes = []
for f in bloc:
    c = {k: 2 for k in ("avantage", "originalite", "falsifiabilite", "traitabilite", "robustesse")}
    if f["nom"] == "Verbeux vide":
        c.update({"avantage": 1, "originalite": 1, "falsifiabilite": 0})
    if f["nom"] == "Assuré occupé":
        c.update({"avantage": 1, "originalite": 0})
    notes.append({"identifiant": f["identifiant"], "criteres": c, "justifications": {}})
doublons = [[par_nom["Jumeau"], par_nom["Sobre fort"]]] if "Jumeau" in par_nom and "Sobre fort" in par_nom else []
print(json.dumps({"texte": "```json\n" + json.dumps({"notes": notes, "doublons": doublons}) + "\n```", "cout_usd": cout}))
