# Consigne d'erratum — synthèse du collisionneur N12-N13 — v1

session-depot (instance 3, seconde session), 1er novembre 2026, ≈ 09:37 UTC. Scellée **avant** le lancement du lecteur de l'erratum.
Motif : relecture indépendante d'Opus 5.5 (conv-audit, `relecture-opus-synthese-n12-n13-v1.md`, `c05949af…`, R-1038 de sa branche ;
n° 312) : synthèse « tenue sous condition » ; conv-audit et Lazar (carte de décision, § 166 de la relecture) demandent un **erratum
avant usage**. La synthèse v1 (`synthese-n12-n13-v1.md`, `b1d28f0d…`) reste (R12).

## Qui lit

Un lecteur neuf (sous-agent) qui n'a écrit ni les critères (`criteres-lecture-n12-n13-v1.md`, `71b63584…`), ni la synthèse v1, ni la
relecture, ni aucune cellule. Il lit : les critères N12-N13 et ceux du tour 1 des nœuds (`22edbf47…`) ; la question v2 (`9faee0aa…`) ;
les faits v1 (`faits-n12-n13-v1.md`, `ccec9e94…`) ; les douze cellules du run `run-n12-n13-e3-v1` ; `etat.md` ; la synthèse v1 ; la
relecture d'Opus. Il ne lit pas `annexe-tour-2-n12-n13-v1.md` ni les dossiers interdits (`donnees/mode-tenu-a-l-ecart-v1`,
`donnees/collisionneur-evasion-moniteurs-v1`, `donnees/bras-attaque-*`, `quarantaine/`, `donnees/runs/`, `diag/`,
`prereg/P3-consignes-v1.md`). Il relève `date -u`, recalcule les empreintes, ne modifie aucun fichier existant, ne scelle rien,
ne commet rien, ne décide rien, ne recommande rien, ne classe pas les espèces.

## Ce qu'il rend

1. **`erratum-synthese-n12-n13-v1.md`** : une table, une ligne par constat RN-01 à RN-14 de la relecture (et un par point 1 à 12 de
   sa section « Points qui exigeant les cellules »), colonnes : constat ; ce que dit la v1 (citation, ligne) ; ce que disent les
   cellules ou les pièces (renvoi) ; verdict (**confirmé** / **infirmé** / **non tranchable**, avec la raison) ; correction (texte
   exact de remplacement, original cité puis remplacement, ou « aucune »). Points qui exigent une règle écrite :
   - **RN-01** : écrire la règle de comptage des accords (critères 7, 10 et 11 du tour 1 : accord = même position en T1 chez
     au moins deux espèces avec une raison commune ; « large » = trois ou quatre ; vrai par construction exclu ; une espèce qui
     rejoint en T3 est une convergence, pas un accord) ; recompter ; nommer chaque accord avec ses espèces et sa raison ;
     décider sur les cellules si les liens 1, 3 et 6 sont des accords.
   - **RN-02** : liste nominative des apports seuls après retrait de ceux qui sont repris ou nés d'une critique ; les quatre
     risques de la couche 3 (un par espèce : A, B, C, D) traités chacun ; répartition corrigée.
   - **RN-03** : règle de sélection des divergences résolues parmi les cessions ; cessions recomptées (« A sur lui-même » et
     « D l'avait » exclues ou justifiées).
   - **RN-04** : rétablir l'objection de B en T1 sur (c3) (circularité ; le motif d'Avalon n'est pas diffus) comme divergence ou
     apport, avec ce qu'il en reste en T3, et la mettre en regard de la lecture vérifiée d'Avalon (pièce 4 : « Diffuse : en
     partie », « Menace : non établie »).
   - **RN-05** : recouper l'affirmation « N-045 ne couvre pas la génération d'instruments neufs » sur la pièce 1 (énoncés 1, 5,
     6 (ii) : sondes, adaptateurs, règle d'agrégation apprise) ; appliquer le critère 5 à A, B, C et D symétriquement (R4) ;
     rendre la réponse littérale de B et C à N12 (1).
   - **RN-06, RN-07** : réécrire les faits saillants 1 et 2 à la portée exacte des cellules (qui dit quoi : « (c1) est le
     témoin qui manque » chez qui ; troisième bras ajouté en T3 par A, B, C ; « cause collective non établie » chez C et D :
     renvoi de cellule ou « inférence du lecteur, retirée »).
   - **RN-08** : revoir « seule pièce sans dépense » (catégorie « sans dépense de carte » hors critère 13 ; appels de sous-agents) ;
     vérifier sur la pièce 5 ce qui est dit du post-hoc hors domaine (Table 1 de Damani, telle que la lecture vérifiée la
     rapporte) et retirer ce que la pièce ne porte pas ; dire si une espèce présente la recalibration de Platt comme établie
     par Damani ; dire si une cellule établit que les confiances des juges sont journalisées.
   - **RN-09** : nommer N-053 point 5 (« signal d'entraînement ou de sélection ») pour la divergence n° 1 ; dire sur A-T3 si les
     fiches filtrées entrent dans un entraînement ; dire comment le bras « récompense du signalement » de B détecte un
     signalement (mécanisme ou juge).
   - **RN-11** : pour les divergences 4, 5, 6 : raisons de chaque côté ; expliquer les codes « Q2, N4 » de C ; pour la 7 : nommer
     la pièce qui porte « l'invariant du noyau gelé » ou dire qu'aucune ne le porte ; retirer l'étiquette « jamais » de la n° 5
     si aucune espèce ne la porte.
   - **RN-12** : retirer la pièce ajoutée par le lecteur (« je le note pour la veille ») et les deux classements d'espèces.
   - **RN-13** : « 4 reprises » → deux reprises, deux critiques ; dire si une espèce nomme les « bornes » gelées.
   - **RN-14 (sécurité, majeure pour servir)** : les passages des lignes 79–80, 107–110, 117–118, 183 et 194 de la v1 qui
     reproduisent des paramètres de conception (entraînement de l'organisme sous récompense collective ; génération de code
     dans la couche 3) sont **remplacés par des renvois de cellule** (fichier, section), sans reproduire les paramètres ; le
     lecteur vérifie qu'aucun autre passage de la v1 ne le fait et le dit.
   - **RN-10, RN-15, RN-16, RN-17** : prendre acte (RN-10 : la réserve « effet d'ordre » sur N12 (3) reposera sur « le plus de
     détail » ou tombera avec l'accord) ; aucune correction attendue.
2. **`synthese-n12-n13-v2.md`** : la v1 intégrale, copiée, avec seulement les remplacements de l'erratum appliqués par script
   (chaque chaîne originale trouvée exactement une fois, arrêt sinon ; code de retour rapporté), note de version en tête (trois à
   huit lignes), table des empreintes de la v1 conservée et complétée (relecture d'Opus, cette consigne, erratum « empreinte calculée
   par session-depot au scellement ») ; longueur ≤ v1 + 800 mots.

## Ce que session-depot fait ensuite

Sondage de cinq corrections sur les cellules ; recalcul par programme de la table des empreintes de la v2 ; scellement des deux
fichiers ; consignation ; versement sur le canal. La v1 reste.
