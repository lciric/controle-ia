"""CL3 : juge externe FACTICE (aucun réseau, aucune clé). Journalise chaque réception ; rend des notes au gabarit."""
import json, re, sys
mode, journal = sys.argv[1], sys.argv[2]
consigne = sys.stdin.read()
with open(journal, "a") as f:
    f.write(json.dumps({"taille": len(consigne), "fiches_recues": "## Les fiches" in consigne,
                        "controle": "exactement OK" in consigne}) + "\n")
if "exactement OK" in consigne:
    print(json.dumps({"texte": "OK", "cout_usd": 0.002})); sys.exit(0)
bloc = json.loads(re.search(r"```json\n(\[.*\])\n```", consigne, re.S).group(1))
par_nom = {f["nom"]: f["identifiant"] for f in bloc}
notes = []
for f in bloc:
    c = {k: 2 for k in ("avantage", "originalite", "falsifiabilite", "traitabilite", "robustesse")}
    if f["nom"] == "Verbeux vide": c.update({"avantage": 1, "originalite": 1, "falsifiabilite": 0})
    if f["nom"] == "Assuré occupé": c.update({"avantage": 1, "originalite": 0})
    notes.append({"identifiant": f["identifiant"], "criteres": c, "justifications": {}})
doublons = [[par_nom["Jumeau"], par_nom["Sobre fort"]]] if "Jumeau" in par_nom and "Sobre fort" in par_nom else []
texte = "```json\n" + json.dumps({"notes": notes, "doublons": doublons}) + "\n```"
if mode == "nan":
    print('{"texte": ' + json.dumps(texte) + ', "cout_usd": NaN}'); sys.exit(0)
if mode == "code3":
    print(json.dumps({"texte": "", "cout_usd": 1.9})); sys.exit(3)
print(json.dumps({"texte": texte, "cout_usd": 0.3}))
