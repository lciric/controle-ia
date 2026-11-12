"""Pire cas des plafonds du devis v7 bis (deux passes) : chaque session déclare exactement son plafond ; et le compteur du
relais (`--plafond-usd 40 --reserve-par-appel 10`). Aucun réseau. Usage : python -B plafonds_pire_cas.py ARBRE_V37 TRAVAIL"""

import json
import os
import sys

arbre, travail = sys.argv[1], sys.argv[2]
sys.path.insert(0, arbre)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pole import ideation as idn  # noqa: E402
from pole.adaptateurs import Resultat  # noqa: E402
from pole.relais_reel import Compteur  # noqa: E402

E = os.path.join(travail, "entrees")
lb = json.load(open(os.path.join(E, "liste-blanche.json")))
FICHE = {"nom": "Idée", "type": "question", "enonce": "Énoncé falsifiable.",
         "loi_predictive": {"espace_instances": "dix familles", "prediction": "effet", "signe": "+", "metrique": "rappel"},
         "perte_traduction": "aucune", "questions_servies": ["Q1"],
         "avantage": {"source": "programme", "texte": "a", "incopiable_parce_que": "r"},
         "originalite": {"niveau": "transposition", "texte": "t"}, "demande_organisme": {"nature": "rien", "texte": ""},
         "cout": {"nature": "processeur", "ordre_de_grandeur": "jours"}, "piege": "p", "cosmetique_si": "c",
         "anteriorite": []}


class Pire:
    """Chaque session coûte exactement son plafond (pire cas tenu par le noyau)."""
    nom = "pire-cas"

    def __init__(self):
        self.sessions = []

    def lancer(self, role, consigne, dossier, budget_usd, max_tours, modele=None):
        import re
        self.sessions.append((role, modele, budget_usd))
        if role == "proposeur_ideation":
            return Resultat("```json\n" + json.dumps({"fiches": [FICHE]}) + "\n```", [], budget_usd, "ok")
        idents = sorted(set(re.findall(r'"identifiant": "(T\d\d)"', consigne)))
        notes = [{"identifiant": i, "criteres": {k: 2 for k in idn.CRITERES}, "justifications": {}} for i in idents]
        return Resultat("```json\n" + json.dumps({"notes": notes, "doublons": []}) + "\n```", [], budget_usd, "ok")


budgets = {("proposeur_ideation", "claude-opus-5-5"): 5.0, ("proposeur_ideation", "claude-fable-5-1"): 10.0,
           ("juge_ideation", "claude-opus-5-5"): 4.0, ("juge_ideation", "claude-fable-5-1"): 7.0}
ad = Pire()
sortie = os.path.join(travail, "P1-pire-cas")
try:
    idn.executer_ideation(ad, sortie, liste_blanche=os.path.join(E, "liste-blanche.json"),
                          question=os.path.join(E, "question.md"), pieces=[os.path.join(E, "piece-1.md")],
                          proposeurs=[("opus", "claude-opus-5-5"), ("fable", "claude-fable-5-1")],
                          juges=[("juge-fable", "claude-fable-5-1"), ("juge-opus", "claude-opus-5-5")],
                          temoins=os.path.join(E, "temoins.json"), graine=1, budget_total_usd=40.0, budgets=budgets,
                          seconde_passe=True, cout_deja_engage_usd=0.4, taille_max_pieces=650_000)
    print("noyau : course complète")
except idn.CourseInterrompue as e:
    print("noyau, deux passes, chaque session à son plafond :", e)
print("sessions jouées :", [(r[:5], m[7:12], b) for r, m, b in ad.sessions], "dépense", 0.4 + sum(b for _, _, b in ad.sessions))
print("somme des plafonds Claude, deux passes, contrôles compris :", 0.4 + 2 * (5 + 10) + 7 + 4)

c = Compteur(40.0, 10.0)
for depense in (29.99, 30.01, 33.0):
    c = Compteur(40.0, 10.0)
    c.reserver(); c.regler(depense)
    print(f"relais 40/10, dépensé {depense} : appel suivant {'accepté' if c.reserver() else 'REFUSÉ (402)'}")
print("noyau : le juge Opus (plafond 4) part tant que dépense + 4 ≤ 40, soit jusqu'à 36 ; le juge Fable (7) jusqu'à 33")
