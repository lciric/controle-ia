# Consigne d'erratum — synthèse du tour 1 du collisionneur des nœuds (question v12) — v1

session-depot (instance 3, seconde session), 1er novembre 2026, ≈ 07:50 UTC. Scellée **avant** le lancement du lecteur de
l'erratum. Condition posée par Lazar (mot direct rapporté par conv-audit au n° 306, 07:23 UTC : « go recos ») : le tour 2 des
nœuds ne part qu'après un **erratum scellé** de la synthèse du tour 1, parce que la relecture indépendante d'Opus (conv-audit,
`relecture-opus-synthese-noeuds-v12-tour1-v1.md`, `d1209130…`) y a trouvé une affirmation fausse telle qu'écrite (N11, erreur E1)
et un décompte de tête non reconstructible (E2, E3, E4). La demande de GO à Lazar reste à part : cette consigne n'engage rien.

## Qui lit

Un lecteur neuf (sous-agent), qui n'a écrit ni les critères de lecture (`criteres-lecture-noeuds-v12-tour1-v1.md`, `22edbf47…`),
ni la synthèse v1 (`synthese-noeuds-v12-tour1-v1.md`, `e4d5a5c9…`), ni la relecture d'Opus, ni aucune cellule. Il lit les
cellules entières (douze, `donnees/collisionneur-noeuds-v1/run-noeuds-v12-tour1-e3-v1/cellules/`), les faits servis
(`faits-noeuds-v2.md`, `ea85dad6…`), la question v12 (`a7fac44b…`), la synthèse v1, les critères v1 et la relecture d'Opus.
Il ne lit **pas** l'annexe du tour 2 (`annexe-tour-2-recommandations-v5.md`, ni aucun fichier nommé « annexe-tour-2 »), ni
`donnees/mode-tenu-a-l-ecart-v1`, `donnees/collisionneur-evasion-moniteurs-v1`, `donnees/bras-attaque-*`, `quarantaine/`,
`donnees/runs/`, `diag/`, `prereg/P3-consignes-v1.md`. Il relève `date -u` avant d'écrire. Il ne modifie aucun fichier
existant, ne scelle rien, ne commet rien, ne décide rien et ne recommande rien (critère 23 de la v1 maintenu).

## Ce qu'il rend

1. **`erratum-synthese-noeuds-v12-tour1-v1.md`** : une table, une ligne par point ci-dessous, colonnes : point ; ce que dit la
   synthèse v1 (citation, section) ; ce que disent les cellules ou les faits (renvoi au fichier de cellule et à sa section, ou
   à la ligne des faits) ; verdict (**confirmé** : l'erreur d'Opus est réelle ; **infirmé** : la synthèse v1 tenait ; **non
   tranchable** : les pièces ne permettent pas de trancher, dire pourquoi) ; correction (texte de remplacement exact, ou
   « aucune »). Les points :
   - **E1 (N11, concordance de rangs)** : (i) ce que chaque espèce proposait comme test de transport en T1 (corrélation par
     paire : Spearman ou tau entre deux classements ; ou concordance à trois instruments, W de Kendall) et ce qu'elle en a
     fait en T3 ; (ii) réécrire le « fait (i) » de la synthèse (section « Décompte de tête » et N11) de façon exacte : à trois
     objets, une corrélation de rangs **entre deux** classements a une valeur p minimale de 1/6 (unilatérale) ; une concordance
     à **trois** classements indépendants a p = 1/36 ≈ 0,028 pour l'unanimité, donc « jugeable seulement par l'unanimité,
     puissance très faible », et W prend les valeurs {0, 1/9, 1/3, 4/9, 7/9, 1} (36 issues, un classement fixé), de sorte
     que « W ≥ 0,7 » laisse passer W = 7/9 sous le nul avec probabilité 7/36 ; (iii) dire si cette correction change une
     cession rapportée (un retrait d'une espèce en T3 qui ne tiendrait que par l'énoncé fautif) ; (iv) vérifier les
     chiffres 0,037 et 0,11 de A (hypothèse exacte dans sa cellule) ; (v) le chiffre de puissance de B (0,89 ; 5 points ou
     1 point dans la pièce) : inexactitude (critère 5) ou transposition, et réparer le renvoi « inexactitude signalée au
     décompte ».
   - **E2 (apports d'une seule espèce, critère 12)** : liste nominative des 25 apports seuls par espèce (A, B, C, D) ; retirer
     ceux qui ont été repris (pilote de variance de D en N11 ; test d'invariance de C en N5 ; garde de première arête de C en
     N9 si elle naît d'une critique de A) et donner la répartition corrigée.
   - **E3 (inexactitudes, critère 5)** : préciser le renvoi « B (T1, N3 (c)) » (fichier, section, ligne des faits : B-ii = 0,50)
     ; reclasser s'il y a lieu la puissance de B ; donner le décompte corrigé par espèce.
   - **E4 (N6, accords larges)** : compter sur les cellules, par décision DL-1 à DL-13, les espèces d'accord en T1 et après T3 ;
     donner le nombre exact d'accords larges (trois ou quatre espèces) et nommer chacun ; corriger la tête (14 accords de N6,
     26 larges au total) si elle change ; dire si une espèce s'est prononcée sur la hiérarchie « périmètre interne d'une
     phase » pour DL-2, DL-4, DL-6.
   - **N5** : écrire la règle de comptage (6 ou 7 accords ; le choix 5 « divergence de condition » compté ou non) ; le test
     d'invariance de C ne peut être à la fois apport seul et mesure commune.
   - **N11 (2) et (4)** : par espèce, combien de ponts plantés, comment elle traite le risque que les ponts plantés ne
     ressemblent pas aux vrais, et ce qu'elle dit de la vérification hors du programme ; « non traité » si la cellule ne dit
     rien.
   - **N1** : 0,84 contre 0,83 (option D) : ligne de la pièce 2 et de la question ; même grandeur ou non.
   - **N9** : « 0,95, la confiance la plus haute du tour » : ex æquo avec C sur DL-4 ou non.
   - **Critère 23** : relever les trois tournures où le lecteur prend parti (« réserve que je retiens », « apport majeur »,
     « rend la forme de C et D inapplicable ») et proposer une tournure neutre.
   - **Points 1, 8 et 9 du § 6 de la relecture** : liste nominative des 22 divergences résolues et des 24 retraits (ou le
     nombre réel) ; bornage tronqué de la pièce 20 ; reprise des six liens de la question par les quatre espèces.
   - **Critère 25** : l'heure de lancement du lecteur de la v1 n'est pas dans les cellules ; dire « hors des pièces lues »
     (session-depot la vérifie dans son journal, pas le lecteur).
2. **`synthese-noeuds-v12-tour1-v2.md`** : la synthèse v1 **intégrale**, avec seulement les corrections de l'erratum appliquées
   (chaque remplacement cité dans l'erratum), une **note de version en tête** (trois à huit lignes : ce qui change, renvoi à
   l'erratum, aux empreintes de la v1 et de la relecture), et la table des empreintes de la v1 conservée telle quelle avec,
   en plus, l'empreinte de la relecture d'Opus et des fichiers lus en plus. Rien d'autre n'est réécrit : pas de nouvelle
   lecture d'ensemble, pas de reformulation hors des points de l'erratum. Longueur ≤ v1 + 600 mots.

## Ce que session-depot fait ensuite

Vérifie par sondage cinq corrections de l'erratum sur les cellules ; recalcule par programme la table des empreintes de la v2
(contre-lecture mécanique, exigée par le devis de complément v2) ; scelle l'erratum et la v2 ; consigne ; verse sur le canal ;
demande le mot direct de Lazar pour le tour 2. La v1 reste en l'état (R12).
