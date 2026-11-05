"""CL3 : deux appels directs de executer_ideation (moteur simulé, juge externe FACTICE local, aucun réseau).
D3 : course marquée « claude-sdk » au manifeste (adaptateur simulé) — pour éprouver ensuite le bras du lanceur sans commande.
D4 : adaptateur mixte dont le rôle juge_ideation est une commande externe → reçoit-elle les fiches pendant la course ?"""
import json, os, sys
racine, S, E, O, PY = sys.argv[1:6]
sys.path.insert(0, racine); sys.path.insert(0, os.path.join(racine, "demonstrations"))
from pole import ideation as idn
from pole.adaptateurs import AdaptateurMixte, AdaptateurJugeExterne
from ideation_v1 import AdaptateurIdeationSimule, BUDGETS_PAR_DEFAUT
base = dict(liste_blanche=f"{E}/liste-blanche.json", question=f"{E}/question.md", pieces=[f"{E}/piece-a.md"],
            temoins=f"{E}/temoins.json", graine=20261028, budget_total_usd=17.0, proposeurs=[("opus", "claude-opus-5-5")],
            pieces_juge=[f"{E}/piece-juge.md"])
b = dict(BUDGETS_PAR_DEFAUT); b[("juge_ideation", "gemini-argon")] = 3.0
# D3
idn.executer_ideation(AdaptateurIdeationSimule(20261028), f"{S}/D3", juges=[("juge-opus", "claude-opus-5-5")], budgets=b,
                      moteur="claude-sdk", juges_externes=[("argon", "gemini-argon", None)], **base)
print("D3 : course écrite, moteur au manifeste =", json.load(open(f"{S}/D3/manifeste-depart.json"))["reglages"]["moteur"])
# D4
journal = f"{S}/journal-argon-D4.jsonl"; open(journal, "w").close()
externe = AdaptateurJugeExterne([PY, "-I", f"{O}/argon_factice.py", "normal", journal], environnement={"PATH": "/usr/bin:/bin"})
mixte = AdaptateurMixte(externe, AdaptateurIdeationSimule(20261028), {"juge_ideation"})
for nom, juges in (("D4a", [("argon", "gemini-argon")]), ("D4b", [("juge-opus", "claude-opus-5-5")])):
    try:
        res = idn.executer_ideation(mixte, f"{S}/{nom}", juges=juges, budgets=b, moteur="simule", **base)
        print(nom, ": course rendue, juges =", juges, "; aucune attestation demandée")
    except Exception as e:
        print(nom, ": arrêt", type(e).__name__, str(e)[:200])
print("réceptions de la commande externe pendant les courses D4 :", open(journal).read())
