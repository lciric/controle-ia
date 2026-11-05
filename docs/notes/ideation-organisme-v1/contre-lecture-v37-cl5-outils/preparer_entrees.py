"""Entrées synthétiques d'une course simulée : question, deux pièces de 250 000 caractères (500 000 au total, au-dessus du
défaut de 400 000), témoins des quatre classes, liste blanche. Usage : python -B preparer_entrees.py DOSSIER ARBRE_V37"""

import json
import os
import sys

dossier, arbre = sys.argv[1], sys.argv[2]
sys.path.insert(0, arbre)
from pole import ideation as idn  # noqa: E402

os.makedirs(dossier, exist_ok=True)
q = os.path.join(dossier, "question.md")
open(q, "w", encoding="utf-8").write("Quelles questions de contrôle mériteraient une course ?")
pieces = []
for i in (1, 2):
    p = os.path.join(dossier, f"piece-{i}.md")
    ligne = "Texte de source primaire servi en pièce, sans consigne ni recette, pour mesurer la taille. "
    texte = (ligne * (250_000 // len(ligne) + 1))[:250_000]
    open(p, "w", encoding="utf-8").write(texte)
    pieces.append(p)
base = {"type": "question", "enonce": "Énoncé falsifiable.",
        "loi_predictive": {"espace_instances": "dix familles", "prediction": "effet de 0,2", "signe": "+",
                           "metrique": "rappel à fausses alertes fixées"},
        "perte_traduction": "aucune", "questions_servies": ["Q1"],
        "avantage": {"source": "programme", "texte": "avantage", "incopiable_parce_que": "raison"},
        "originalite": {"niveau": "transposition", "texte": "texte"},
        "demande_organisme": {"nature": "rien", "texte": ""},
        "cout": {"nature": "processeur", "ordre_de_grandeur": "jours"},
        "piege": "piège", "cosmetique_si": "si rien ne bouge", "anteriorite": []}
t = os.path.join(dossier, "temoins.json")
json.dump({"temoins": [
    {"fiche": dict(base, nom="Sobre fort"), "attendu": "eligible", "classe": "vrai"},
    {"fiche": dict(base, nom="Verbeux vide"), "attendu": "ineligible", "note_max": {"falsifiabilite": 1},
     "classe": "faux_falsifiabilite"},
    {"fiche": dict(base, nom="Assuré occupé"), "attendu": "ineligible", "note_max": {"originalite": 1},
     "classe": "faux_anteriorite"},
    {"fiche": dict(base, nom="Jumeau du sobre"), "attendu": "eligible", "jumeau_de": "Sobre fort", "classe": "jumeau"}]},
    open(t, "w", encoding="utf-8"), ensure_ascii=False)
lb = os.path.join(dossier, "liste-blanche.json")
idn.construire_liste_blanche([q, t] + pieces, lb)
print(json.dumps({"question": q, "pieces": pieces, "temoins": t, "liste_blanche": lb}))
