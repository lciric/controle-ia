"""Mutations du banc, v4 (R-2278) : celles de la v3, plus les phrases de (i) alignées sur le candidat 2 (VB6-1, VB6-2)."""
from mutations_accb6_v3 import MUTATIONS as V3

MUTATIONS = list(V3) + [
    ("P01", "phrases_v1.py", 'PHRASE_I_A = "{barreau} établi pour le saboteur instruit (i-a) : " + CORPS_I_A',
     'PHRASE_I_A = "{barreau} établi pour le saboteur instruit (i-a) : " + CORPS_A', "VB6-1 : phrase de (i) en A (contrôle de consigne)"),
    ("P02", "phrases_v1.py", 'PHRASE_L_I_A = ("{barreau} établi pour le saboteur instruit seulement : " + CORPS_I_A',
     'PHRASE_L_I_A = ("{barreau} établi pour le saboteur instruit seulement : " + CORPS_A', "VB6-1 : ligne (i) A"),
    ("P03", "phrases_v1.py", 'PHRASE_L_I_M = ("{barreau} réfuté à cette puissance pour le saboteur instruit : le maximum des scores d\'action sépare mieux que leur "\n                "somme ; pour',
     'PHRASE_L_I_M = ("{barreau} réfuté à cette puissance pour le saboteur instruit : réfuté à cette puissance pour (i) : le maximum des scores d\'action sépare mieux que leur "\n                "somme ; pour',
     "VB6-2 : ligne (i) M sans répétition"),
    ("P04", "phrases_v1.py", '"puissance ; mode « coût » seul, horizon fixe de dix actions ; contrôle de consigne : `temoin` (B6-D3, B6-D3b) ; "',
     '"puissance ; mode « coût » seul, horizon fixe de dix actions ; contrôle de consigne : `temoin` (B6-D3) ; "', "texte du contrôle de consigne"),
]
