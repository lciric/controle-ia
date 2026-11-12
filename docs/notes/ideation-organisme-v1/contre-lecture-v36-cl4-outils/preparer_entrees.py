"""CL4 : prépare des entrées de course simulée (question, pièce, matériau, témoins, liste blanche) dans un dossier donné."""
import json, os, sys
code, dest = sys.argv[1], sys.argv[2]
sys.path.insert(0, code)
from pole import ideation as idn
os.makedirs(dest, exist_ok=True)
def fiche(**m):
    f = {"nom": "Essai", "type": "question",
         "enonce": "Le transfert d'un moniteur vers le diffus suit-il une courbe prédite avant le test ?",
         "loi_predictive": {"espace_instances": "dix familles", "prediction": "rappel décroît", "signe": "-",
                            "metrique": "rappel à 1 % de fausses alertes"},
         "perte_traduction": "pente", "questions_servies": ["Q4"],
         "avantage": {"source": "programme", "texte": "théorie", "incopiable_parce_que": "carte"},
         "originalite": {"niveau": "transposition", "texte": "rupture"},
         "demande_organisme": {"nature": "ajout", "texte": "générateur"},
         "cout": {"nature": "processeur", "ordre_de_grandeur": "jours"},
         "piege": "artefact", "cosmetique_si": "plates", "anteriorite": []}
    f.update(m); return f
ecr = lambda n, t: open(os.path.join(dest, n), "w", encoding="utf-8").write(t)
ecr("question.md", "Quelles questions affûtées ?")
ecr("piece-a.md", "# Pièce A\nContexte.")
ecr("piece-juge.md", "# Antériorité\nRien.")
ecr("materiau.md", "# Matériau du tour interne\nFiches anonymes du tour interne.")
json.dump({"temoins": [
    {"fiche": fiche(nom="Sobre fort"), "attendu": "eligible", "classe": "vrai"},
    {"fiche": fiche(nom="Verbeux vide", enonce="Long " * 40), "attendu": "ineligible", "note_max": {"falsifiabilite": 1},
     "classe": "faux_falsifiabilite"},
    {"fiche": fiche(nom="Assuré occupé"), "attendu": "ineligible", "note_max": {"originalite": 1}, "classe": "faux_anteriorite"},
    {"fiche": fiche(nom="Jumeau"), "attendu": "eligible", "jumeau_de": "Sobre fort", "classe": "jumeau"}]},
    open(os.path.join(dest, "temoins.json"), "w", encoding="utf-8"), ensure_ascii=False)
idn.construire_liste_blanche([os.path.join(dest, n) for n in ("question.md", "piece-a.md", "piece-juge.md", "materiau.md",
                                                             "temoins.json")], os.path.join(dest, "liste-blanche.json"))
idn.ecrire_json_scelle(os.path.join(dest, "attestation-materiau.json"),
                       {"lecteur": "lecteur-cl4", "lu_le": "2026-10-28",
                        "materiau_sha256": {"materiau.md": idn.sha256_fichier(os.path.join(dest, "materiau.md"))}})
print("ok", dest)
