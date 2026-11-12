"""Table des empreintes de la note de conception du pilier « génération » (v1).

Calcule le SHA-256 de chaque pièce citée, sur disque ou par `git show` (pièce d'une branche
déjà dans le clone local), et imprime une table Markdown. Lecture seule ; aucun réseau.

Lancement, depuis la racine du dépôt :
    python -I -B docs/notes/ideation-organisme-v1/pilier-generation-v1/calculs-v1/table-empreintes-note-v1.py
"""
import hashlib
import subprocess
import sys

DOSSIER = "docs/notes/ideation-organisme-v1/pilier-generation-v1/"
PIECES = [
    ("consigne de cette note", "docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-note-pilier-generation-v1.md"),
    ("interdits communs v2", "docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md"),
    ("registre des décisions (vivant, à la lecture)", "registres/decisions.md"),
    ("N-044", "docs/decisions/decision-N-044-v1.md"),
    ("N-045 v2", "docs/decisions/decision-N-045-v2.md"),
    ("N-058", "docs/decisions/decision-N-058-v1.md"),
    ("N-064", "docs/decisions/decision-N-064-v1.md"),
    ("N-065", "docs/decisions/decision-N-065-v1.md"),
    ("synthèse du tour 2 N12-N13", "docs/notes/ideation-organisme-v1/course-2/collisionneur-n12-n13-v1/synthese-n12-n13-tour2-v1.md"),
    ("essai Lean, brouillon 3", "brouillons/couche4-essai-preuve-formelle-v1/essai-preuve-formelle-devis-v1-brouillon3.md"),
    ("essai Lean, contre-lecture 1", "prereg/contre-lectures/essai-preuve-formelle-devis-v1-brouillon1-cl1.md"),
    ("essai Lean, vérification courte", "prereg/contre-lectures/essai-preuve-formelle-devis-v1-brouillon2-verification-courte-v1.md"),
    ("programme de l'organisme v3", "docs/notes/rapports-directeur/programme-organisme-complet-v1/programme-organisme-complet-v3.md"),
    ("inventaire des idées v4", "docs/notes/rapports-directeur/programme-organisme-complet-v1/inventaire-idees-organisme-v4.md"),
    ("programme d'entretien v16", "brouillons/entretien-taif-v3/programme-entretien-taif-v16.md"),
    ("calcul des ordres de grandeur", DOSSIER + "calculs-v1/ordres-de-grandeur-pilier-generation-v1.py"),
    ("sortie du calcul", DOSSIER + "calculs-v1/sortie-ordres-de-grandeur-pilier-generation-v1.txt"),
    ("ce script", DOSSIER + "calculs-v1/table-empreintes-note-v1.py"),
]
PIECES_GIT = [
    ("programme de conception de l'organisme v1 (branche du canal, lu par git show)",
     "origin/canal/conv-audit-n04:brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/programme-conception-organisme-v1.md"),
]


def h_fichier(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def h_git(objet):
    sortie = subprocess.run(["git", "show", objet], capture_output=True, check=True).stdout
    return hashlib.sha256(sortie).hexdigest()


print("| pièce | chemin | sha256 |")
print("|---|---|---|")
for nom, chemin in PIECES:
    print(f"| {nom} | `{chemin}` | `{h_fichier(chemin)}` |")
for nom, objet in PIECES_GIT:
    print(f"| {nom} | `{objet}` | `{h_git(objet)}` |")
sys.stdout.flush()
