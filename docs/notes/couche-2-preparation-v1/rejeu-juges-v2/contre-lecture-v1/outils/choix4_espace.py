"""Choix 4 (espace comprise dans la masse admise) : masse v1 (conditionnelle à l'espace, jetons de tête) et masse v2
(espace, valeur, fin de ligne) sur un juge simulé à bigrammes, en faisant varier la probabilité de l'espace après « : »
(le reste : gras « ** »). Lancer depuis la racine de la copie, PYTHONPATH=src:tests."""
import math, torch
import test_noter_rejeu_juges_v2 as t2
from controle_ia.environnements import noter_rejeu_juges_v1 as nrj, noter_rejeu_juges_v2 as nrj2
from controle_ia.environnements.rubrique import CRITERES
print("P(espace | « : »)   masse v1 (min)   masse v2 (min)   appui v1 / v2 (seuil 0,5)")
for logit_gras in (-20.0, 0.0, 2.0, 3.5, 4.0, 4.5, 6.0):
    table = t2._table()                       # « : » → espace (logit 4), chiffres, fin de ligne (logit 4)
    table[t2._i(":"), t2._i("*")] = logit_gras
    p_esp = float(torch.softmax(table[t2._i(":")], -1)[t2._i(" ")])
    r2 = t2._lire(table, masse_min=0.5)
    r1 = nrj.lire_par_probabilite(t2.BigrammeCache(table), t2.TOK, t2.CTX, t2._bloc(echelle=False), CRITERES, True,
                                  0.5, t2.TOK.pad_token_id)
    m1 = min(c["masse"] for c in r1["criteres"].values()); m2 = min(c["masse"] for c in r2["criteres"].values())
    print(f"{p_esp:18.4f} {m1:16.4f} {m2:16.4f}      {r1['score'] is not None} / {r2['score'] is not None}")
