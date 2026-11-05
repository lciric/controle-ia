"""Argon factice (contre-lecture CL7, étendu en CL8 : coût au barème, réponse de contrôle libre ; CL9 : `tarif_tout` —
coût de CHAQUE appel au tarif donné, entrée et sortie, jamais borné au plafond) : local, sans réseau, consigne chaque appel dans un journal JSONL.

Usage : python3 argon_factice.py JOURNAL CONFIG.json
CONFIG : {"cout": "plafond" | nombre, "casse_controle": bool, "casse_au_dela": entier (caractères),
          "dormir_s": nombre (sessions hors contrôle), "dormir_controle_s": nombre, "pid_fichier": chemin,
          "texte_controle": "OK", "casse_role": "juge_ideation" | "proposeur_ideation" | null}
Le coût rendu vaut PLAFOND_SESSION_USD (pire cas) par défaut.
"""
import json
import os
import re
import subprocess
import sys
import time

journal, config_f = sys.argv[1], sys.argv[2]
with open(config_f, encoding="utf-8") as f:
    cfg = json.load(f)
consigne = sys.stdin.read()
plafond = float(os.environ.get("PLAFOND_SESSION_USD", "0"))
role = os.environ.get("ROLE_POLE")
controle = consigne.startswith("Réponds exactement OK")
cout = plafond if cfg.get("cout", "plafond") == "plafond" else float(cfg["cout"])
# CL8 : coût du contrôle au barème (dollars par million de jetons ; caractères par jeton) — la commande ne borne PAS
# son coût au plafond (pire cas : le noyau dit que la commande est responsable de son propre plafond)
bareme = cfg.get("bareme_controle")
if controle and bareme:
    cout_bareme = (len(consigne) / bareme["car_par_jeton"]) * bareme["entree"] / 1e6 \
        + bareme.get("jetons_sortie", 0) * bareme["sortie"] / 1e6
    cfg["cout_controle"] = round(cout_bareme, 6)
    if bareme.get("borne_au_plafond") and cout_bareme > plafond:
        cfg["cout_controle"] = plafond
entree = {"t": time.time(), "pid": os.getpid(), "role": role, "controle": controle, "taille": len(consigne),
          "plafond": plafond, "cout_rendu": (cfg.get("cout_controle", cout) if controle else cout),
          "env": sorted(os.environ)}
if "seconde passe" in consigne or "première passe" in consigne:
    entree["passe"] = 2
elif "passe de proposition" in consigne:
    entree["passe"] = 1
tarif = cfg.get("tarif_tout")  # CL9 : {"usd_par_car_entree": x, "usd_par_car_sortie": y}


def consigner(e):
    with open(journal, "a", encoding="utf-8") as f:
        f.write(json.dumps(e, ensure_ascii=False) + "\n")


def sortir(texte, c=cout):
    if tarif:
        c = round(len(consigne) * tarif["usd_par_car_entree"] + len(texte) * tarif.get("usd_par_car_sortie", 0.0), 6)
    entree["cout_rendu"] = c
    entree["taille_sortie"] = len(texte)
    consigner(entree)
    print(json.dumps({"texte": texte, "cout_usd": c}, ensure_ascii=False))
    sys.exit(0)


if cfg.get("casse_au_dela") and len(consigne) > cfg["casse_au_dela"]:
    entree["cout_rendu"] = 0.0
    entree["casse"] = True
    consigner(entree)
    sys.stderr.write("requête trop grosse (quota simulé)\n")
    sys.exit(3)
if cfg.get("casse_role") and role == cfg["casse_role"] and not controle:
    entree["cout_rendu"] = 0.0
    entree["casse"] = True
    consigner(entree)
    sys.stderr.write("panne simulée\n")
    sys.exit(4)
if controle:
    if cfg.get("dormir_controle_s"):
        if cfg.get("pid_fichier"):
            p = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(120)"])
            with open(cfg["pid_fichier"], "w") as f:
                f.write(f"{os.getpid()} {p.pid}")
        time.sleep(cfg["dormir_controle_s"])
    if cfg.get("casse_controle"):
        sortir("KO")
    if cfg.get("controle_repond_notes") and role == "juge_ideation":  # CL8 : le juge lit la consigne et rend ses notes
        bloc_c = json.loads(re.search(r"```json\n(\[.*\])\n```", consigne, re.S).group(1))
        sortir("```json\n" + json.dumps({"notes": [{"identifiant": f["identifiant"], "criteres": {k: 3 for k in (
            "avantage", "originalite", "falsifiabilite", "traitabilite", "robustesse")}} for f in bloc_c]}) + "\n```",
            cfg.get("cout_controle", cout))
    sortir(cfg.get("texte_controle", "OK"), cfg.get("cout_controle", cout))
if cfg.get("dormir_s"):
    if cfg.get("pid_fichier"):
        p = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(120)"])
        with open(cfg["pid_fichier"], "w") as f:
            f.write(f"{os.getpid()} {p.pid}")
    time.sleep(cfg["dormir_s"])
FICHE = {"nom": "Argon A", "type": "question",
         "enonce": "Le transfert d'un moniteur vers le diffus suit-il une courbe prédite avant le test ?",
         "loi_predictive": {"espace_instances": "familles", "prediction": "rappel décroît", "signe": "-",
                            "metrique": "rappel à 1 % de fausses alertes"},
         "perte_traduction": "la forme est résumée par une pente", "questions_servies": ["Q4"],
         "avantage": {"source": "programme", "texte": "théorie explicite", "incopiable_parce_que": "exige la carte"},
         "originalite": {"niveau": "transposition", "texte": "détection de rupture"},
         "demande_organisme": {"nature": "ajout", "texte": "générateur"},
         "cout": {"nature": "processeur", "ordre_de_grandeur": "jours"},
         "piege": "artefact", "cosmetique_si": "courbes plates",
         "anteriorite": [{"reference": "référence", "statut": "SUPPOSE"}]}
if cfg.get("gros_champs"):
    n = int(cfg["gros_champs"])
    rempl = ("texte de méthode sans signal " * (n // 29 + 1))[:n]
    for k in ("enonce", "perte_traduction", "piege", "cosmetique_si"):
        FICHE[k] = rempl
    for k, sous in (("loi_predictive", ("espace_instances", "prediction", "metrique")),
                    ("avantage", ("texte", "incopiable_parce_que")), ("originalite", ("texte",)),
                    ("demande_organisme", ("texte",)), ("cout", ("ordre_de_grandeur",))):
        FICHE[k] = dict(FICHE[k], **{x: rempl for x in sous})
if cfg.get("listes_longues"):  # CL8 : listes sans borne au gabarit, guillemets échappés en JSON
    n = int(cfg["listes_longues"])
    FICHE["questions_servies"] = [("Q" + str(i) + " " + '"' * 70)[:80] for i in range(n)]
    FICHE["anteriorite"] = [{"reference": ('Référence "citée" ' * 30)[:500], "statut": "RAPPORTE"} for _ in range(n)]
if role == "proposeur_ideation":
    nb = int(cfg.get("nombre_fiches", 2))
    fiches = [dict(FICHE, nom=f"Argon {i}" + (" revue" if entree.get("passe") == 2 else "")) for i in range(nb)]
    sortir("```json\n" + json.dumps({"fiches": fiches}, ensure_ascii=False) + "\n```")
    f1 = dict(FICHE)
    f2 = dict(FICHE, nom="Argon B")
    if entree.get("passe") == 2:
        f1["nom"] = "Argon A revue"
    sortir("```json\n" + json.dumps({"fiches": [f1, f2]}, ensure_ascii=False) + "\n```")
bloc = json.loads(re.search(r"```json\n(\[.*\])\n```", consigne, re.S).group(1))
par_nom = {f["nom"]: f["identifiant"] for f in bloc}
notes, doublons = [], []
for f in bloc:
    c = {k: 2 for k in ("avantage", "originalite", "falsifiabilite", "traitabilite", "robustesse")}
    n = f["nom"].lower()
    if "verbeux" in n or "occup" in n:
        c.update({"avantage": 1, "originalite": 0, "falsifiabilite": 0})
    if "sobre" in n or "jumeau" in n:
        c.update({"avantage": 3, "originalite": 2})
    notes.append({"identifiant": f["identifiant"], "criteres": c, "justifications": {k: "j" for k in c}})
for f in bloc:
    if f["nom"].lower().startswith("jumeau"):
        cible = next((v for k, v in par_nom.items() if k.lower().startswith("sobre")), None)
        if cible:
            doublons.append([f["identifiant"], cible])
sortir("```json\n" + json.dumps({"notes": notes, "doublons": doublons}, ensure_ascii=False) + "\n```")
