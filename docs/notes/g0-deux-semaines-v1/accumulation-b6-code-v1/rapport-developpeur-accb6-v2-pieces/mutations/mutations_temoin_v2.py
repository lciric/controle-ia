"""Témoin du banc (aucun effet) : un commentaire changé ; doit survivre (code 0), sinon le banc tue tout par construction."""
MUTATIONS = [
    ("T00", "etats_v1.py", "# « Seuil », règle 4 : aire d'épisode ≥ 0,99", "# « Seuil », règle 4 : aire d'épisode ≥ 0,99 (témoin du banc)",
     "témoin : commentaire seul"),
    ("T01", "lecture_v1.py", "MOTIF_PLANCHER_NEUF = \"écrite par T0.7", "MOTIF_PLANCHER_NEUF = \"Écrite par T0.7",
     "témoin : texte du motif (libre, lu par les essais dans la constante)"),
]
