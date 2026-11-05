"""CL4 : « Argon » factice LOCAL (aucun réseau). Journalise ce qu'il reçoit (rôle, présence de fiches d'autres auteurs,
présence de « ## Les fiches »), puis rend une réponse conforme. Mode choisi par la variable MODE_FACTICE si transmise."""
import json, os, re, sys, time
c = sys.stdin.read()
journal = os.path.join(os.path.dirname(os.path.abspath(__file__)), "argon-journal.jsonl")
role = os.environ.get("ROLE_POLE")
with open(journal, "a", encoding="utf-8") as j:
    j.write(json.dumps({"t": time.time(), "role": role, "plafond": os.environ.get("PLAFOND_SESSION_USD"),
                        "cwd": os.getcwd(), "controle": "exactement OK" in c,
                        "contient_les_fiches": "## Les fiches" in c,
                        "contient_fiches_autres": bool(re.search(r"Idée simulée", c)),
                        "contient_materiau": "Matériau servi" in c, "longueur": len(c)}) + "\n")
if "exactement OK" in c:
    print(json.dumps({"texte": "OK", "cout_usd": 0.01})); sys.exit(0)
if "passe de proposition" in c:
    f = {"nom": "Argon idée", "type": "question", "enonce": "Énoncé falsifiable d'Argon.",
         "loi_predictive": {"espace_instances": "dix familles", "prediction": "0,2", "signe": "+", "metrique": "rappel"},
         "perte_traduction": "peu", "questions_servies": ["Q1"],
         "avantage": {"source": "methodes", "texte": "x", "incopiable_parce_que": "y"},
         "originalite": {"niveau": "inedite", "texte": "z"}, "demande_organisme": {"nature": "rien", "texte": ""},
         "cout": {"nature": "processeur", "ordre_de_grandeur": "jours"}, "piege": "p", "cosmetique_si": "c",
         "anteriorite": []}
    print(json.dumps({"texte": "```json\n" + json.dumps({"fiches": [f]}, ensure_ascii=False) + "\n```", "cout_usd": 0.3}))
    sys.exit(0)
bloc = json.loads(re.search(r"```json\n(\[.*\])\n```", c, re.S).group(1))
notes, par_nom = [], {f["nom"]: f["identifiant"] for f in bloc}
for f in bloc:
    k = {x: 2 for x in ("avantage", "originalite", "falsifiabilite", "traitabilite", "robustesse")}
    n = f["nom"].lower()
    if "verbeux" in n or "occup" in n:
        k.update({"avantage": 1, "originalite": 0, "falsifiabilite": 1})
    if "sobre" in n or "jumeau" in n:
        k.update({"avantage": 3, "originalite": 2})
    notes.append({"identifiant": f["identifiant"], "criteres": k, "justifications": {}})
d = [[par_nom["Jumeau"], par_nom["Sobre fort"]]] if "Jumeau" in par_nom and "Sobre fort" in par_nom else []
print(json.dumps({"texte": "```json\n" + json.dumps({"notes": notes, "doublons": d}) + "\n```", "cout_usd": 0.4}))
