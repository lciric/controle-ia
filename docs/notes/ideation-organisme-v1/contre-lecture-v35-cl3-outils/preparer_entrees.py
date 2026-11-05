"""CL3 : entrées synthétiques d'une course simulée (aucune pièce réelle lue)."""
import json, os, sys
sys.path.insert(0, sys.argv[1])
from essais.test_v7_ideation import fiche_brute
d = sys.argv[2]
open(os.path.join(d, "question.md"), "w").write("Quelles questions de recherche affûtées ? (question synthétique CL3)")
open(os.path.join(d, "piece-a.md"), "w").write("# Pièce A (synthétique CL3)\nTexte de contexte.")
open(os.path.join(d, "piece-juge.md"), "w").write("# Antériorité (synthétique CL3)\nRien.")
open(os.path.join(d, "materiau.md"), "w").write("# Matériau (synthétique CL3)\nTour interne.")
json.dump({"temoins": [
    {"fiche": fiche_brute(nom="Sobre fort"), "attendu": "eligible", "classe": "vrai"},
    {"fiche": fiche_brute(nom="Verbeux vide", enonce="Long " * 50), "attendu": "ineligible",
     "note_max": {"falsifiabilite": 1}, "classe": "faux_falsifiabilite"},
    {"fiche": fiche_brute(nom="Assuré occupé", originalite={"niveau": "inedite", "texte": "jamais vu"}),
     "attendu": "ineligible", "note_max": {"originalite": 1}, "classe": "faux_anteriorite"},
    {"fiche": fiche_brute(nom="Jumeau"), "attendu": "eligible", "jumeau_de": "Sobre fort", "classe": "jumeau"}]},
    open(os.path.join(d, "temoins.json"), "w"), ensure_ascii=False)
