"""Module de lecture de T0.7 (sondes v0, critère 3 de G0, mode « coût »), v1.

Écrit d'après la section « Module de lecture `src/controle_ia/t07/` » du préenregistrement, commencé sur le brouillon 7, puis
réaligné sur le brouillon 11, puis sur le brouillon 14 `brouillons/T0.7-sondes-v0-v1-brouillon14.md` (`fe7b4e6d…`, non
scellé ; rapport `docs/notes/g0-deux-semaines-v1/rapport-module-t07-v3.md`). Lecture **hors ligne**
des activations enregistrées par la chaîne de T0.6 (`donnees/<run>/activations/c{7,15,23}/<cle>.npy`), sur processeur ;
aucun module gelé n'est touché (R12) ; noms versionnés.

- `registre_v1` : lignes de registre `| CLÉ | AAAA-MM-JJTHH:MM:SSZ | chemin | sha256 |`, lues au format exact de
  `scripts/controle_lecture_t06_v1.py` ; règle du registre partagé ; garde d'ouverture (antériorité stricte, sceaux) ;
  journal des ouvertures et des refus ;
- `criteres_v1` : critères de lecture gelés (ordre R11-arret, R12-invalide, L0a, L0b, L0c, L1, L1b, L7, L7b, L7c, L6, L4, L4b,
  L5, L2, L3), lecture et dérivation de la classe Q du fichier « mots et coût » de T0.6 (`deriver_classe`), état d'un jeu pour
  une sonde (règle L05 : « non interprétable » seulement si le jeu est au-dessus), énumérations de couverture ;
- `mahalanobis_v1` : notation de Mahalanobis par produit matriciel (`produit_matriciel_v2`) avec l'essai d'égalité au
  paquet gelé avant chaque usage ;
- `plancher_v1` : planchers appariés en covariance (recette de `sondes.evaluation.plancher_apparie`), notation des
  actions par le harnais (maximum ou attention : jamais la moyenne ni la médiane sur les jetons), comparaison au plancher
  à `niveau_decisif` ;
- `lecture_v1` : ouverture, garde d'identité des activations, notation (étape A), lecture mécanique (étape B), commande
  `python -m controle_ia.t07.lecture_v1 etape-a | etape-b | repli-recalcul | grille`.

Toute clé obligatoire absente arrête avec son nom complet ; aucun repli silencieux (R5).
"""
