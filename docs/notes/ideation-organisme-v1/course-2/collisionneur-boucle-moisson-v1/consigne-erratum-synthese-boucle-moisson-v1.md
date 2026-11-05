# Consigne d'erratum — synthese-boucle-moisson-v1.md — v1

session-depot (instance 3, seconde session), 1er novembre 2026, ≈ 16:07 UTC. Scellée **avant** le lancement du lecteur de l'erratum. Motif :
relecture indépendante d'Opus 5.5 (conv-audit, `relecture-opus-synthese-boucle-moisson-v1.md`, `02aacbfe…`, R-1052 de sa branche ; n° 317) : synthèse « tenue sous condition » ;
conv-audit demande un **erratum avant tout tour 2**. La synthèse v1 (`synthese-boucle-moisson-v1.md`, `48a514de…`) reste (R12). Consigne nouvelle de Lazar
(R-964) : la v2 ajoute une section **« Pistes générales consensuelles et pistes originales »** (sans recommandation du lecteur).

## Qui lit
Un lecteur neuf (sous-agent) qui n'a écrit ni les critères (`criteres-lecture-boucle-moisson-v1.md`, `3d0dc105…`), ni la synthèse v1, ni la relecture, ni aucune cellule. Il lit : les
critères (et ceux du tour 1 des nœuds, `22edbf47…`), la question servie (`donnees/collisionneur-boucle-moisson-v1/question-collisionneur-boucle-moisson-fiches-v1.md`), les faits servis (`donnees/collisionneur-boucle-moisson-v1/faits-boucle-moisson-v1.md`), les cellules du run
`donnees/collisionneur-boucle-moisson-v1/run-boucle-moisson-e3-v1/cellules/` et son `etat.md`, la synthèse v1, la relecture d'Opus. Il ne lit aucun fichier « annexe-tour-2 » ni les dossiers
interdits (`donnees/mode-tenu-a-l-ecart-v1`, `donnees/collisionneur-evasion-moniteurs-v1`, `donnees/bras-attaque-*`, `quarantaine/`,
`donnees/runs/`, `diag/`, `prereg/P3-consignes-v1.md`). Il relève `date -u`, recalcule les empreintes, ne modifie aucun fichier existant,
ne scelle rien, ne commet rien, ne décide rien, ne recommande rien, ne classe pas les espèces.

## Ce qu'il rend
1. **`erratum-synthese-boucle-moisson-v1.md`** : une table, une ligne par constat de la relecture d'Opus (tous, dans son ordre, avec le résumé de conv-audit — n° 317 point 2 : décomptes non reconstructibles (7 accords pour 8 énumérés dont 2 comptés deux fois ; 27 convergences ; 9 résolues ; 12 apports), deux accords soufflés par la question (« affiner sans capteur = reformuler » ; circularité de la rétrodiction), liste du tour 2 amputée de quatre divergences dont le refus de tout bandit par C, A rangée avec les recodeurs alors qu'elle relance leur code comme C, MAGenIdeas un seul cas), colonnes :
   constat ; ce que dit la v1 (citation, ligne) ; ce que disent les cellules ou les faits (renvoi) ; verdict (**confirmé** / **infirmé** /
   **non tranchable**, avec la raison) ; correction (texte exact de remplacement, original cité puis remplacement, ou « aucune »). Pour les
   décomptes : écrire la règle de comptage et recompter nominativement sur les cellules ; pour les accords « soufflés par la question » :
   appliquer le critère « vrai par construction » ; pour les divergences perdues : rétablir la liste complète du tour 2 ; pour les
   positions mal rangées : citer la cellule.
2. **`synthese-boucle-moisson-v2.md`** : la v1 intégrale, copiée, avec seulement les remplacements de l'erratum appliqués par script (chaque chaîne originale trouvée
   exactement une fois, arrêt sinon ; code de retour rapporté), une note de version en tête (trois à huit lignes), la table des empreintes
   conservée et complétée (relecture, consigne, erratum « empreinte calculée par session-depot au scellement »), et la section nouvelle
   « Pistes générales consensuelles et pistes originales » : (i) les positions tenues par les quatre espèces ou trois sur quatre en T3,
   avec leur réserve R4 ; (ii) les positions tenues par une seule espèce, non réfutées en T2, avec la cellule ; sans ajout ni jugement du
   lecteur. Longueur ≤ v1 + 900 mots.

## Ce que session-depot fait ensuite
Sondage de cinq corrections sur les cellules ; recalcul par programme de la table des empreintes de la v2 ; scellement ; consignation ;
versement sur le canal. La v1 reste.
