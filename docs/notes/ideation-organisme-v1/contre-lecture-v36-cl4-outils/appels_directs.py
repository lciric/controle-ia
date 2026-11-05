"""CL4 : appels directs du cœur (aucun réseau). (a) course déclarée réelle sans juge externe → classement lisible à deux
juges ; (b) adaptateur mixte dont la partie SIMULÉE est la commande externe → le juge externe lit les fiches dans la
course, sans attestation, coût remis à zéro ; (c) étiquette contenant « -p » → auto-préférence mal attribuée."""
import json, os, sys
code, entrees, sortie_base, py, factice = sys.argv[1:6]
sys.path.insert(0, code)
from pole import ideation as idn
from pole.adaptateurs import AdaptateurCommandeExterne, AdaptateurMixte
sys.path.insert(0, os.path.join(code, "demonstrations"))
import ideation_v1 as lanceur

E = lambda n: os.path.join(entrees, n)
communs = dict(liste_blanche=E("liste-blanche.json"), question=E("question.md"), pieces=[E("piece-a.md")],
               temoins=E("temoins.json"), graine=7, budget_total_usd=17.0,
               proposeurs=[("opus", "claude-opus-5-5"), ("fable", "claude-fable-5-1")],
               juges=[("juge-fable", "claude-fable-5-1"), ("juge-opus", "claude-opus-5-5")],
               budgets=dict(lanceur.BUDGETS_PAR_DEFAUT))

class SimuleNommeKit(lanceur.AdaptateurIdeationSimule):
    nom = "claude-sdk"   # se fait passer pour l'adaptateur du kit : le cœur ne vérifie que le nom

# (a)
if not os.path.exists(os.path.join(sortie_base, "D-a")): res = idn.executer_ideation(SimuleNommeKit(7), os.path.join(sortie_base, "D-a"), moteur="claude-sdk", **communs)
c = json.load(open(os.path.join(sortie_base, "D-a", "classement.json")))
print("(a) moteur claude-sdk, aucun juge externe : classement.json écrit, lisible =", c["lisible_L2_L4"],
      "; juges par ligne =", {l["nombre_juges"] for l in c["lignes"]}, "; nom_agregat =", c["lignes"][0]["nom_agregat"])

# (b)
journal = os.path.join(os.path.dirname(factice), "argon-journal.jsonl")
n0 = sum(1 for _ in open(journal)) if os.path.exists(journal) else 0
ext = AdaptateurCommandeExterne([py, "-I", factice], environnement={"PATH": "/usr/bin:/bin"})
mixte = AdaptateurMixte(reel=lanceur.AdaptateurIdeationSimule(7), simule=ext, roles_reels={"proposeur_ideation"})
args = dict(communs, juges=[("juge-fable", "claude-fable-5-1"), ("argon-dans-la-course", "gemini-argon")])
args["budgets"] = dict(communs["budgets"]); args["budgets"][("juge_ideation", "gemini-argon")] = 1.5
res = idn.executer_ideation(mixte, os.path.join(sortie_base, "D-b"), moteur="simule", **args)
lignes = [json.loads(l) for l in open(journal)][n0:]
print("(b) mixte(simule=commande externe) : appels reçus par la commande =",
      [(l["role"], l["contient_les_fiches"]) for l in lignes], "; coût compté pour ce juge =",
      [a["cout_compte_usd"] for a in res["journal"]["appels"] if a["etiquette"] == "argon-dans-la-course"],
      "; classement écrit =", os.path.exists(os.path.join(sortie_base, "D-b", "classement.json")))

# (c)
notes = {"j": {"argon-pro-p1-01": {"criteres": {k: 3 for k in idn.CRITERES}}}}
print("(c) étiquette « argon-pro » :", idn.lecture_auto_preference(notes, {"j": "gemini-argon"}, {"argon-pro": "gemini-argon"}))
