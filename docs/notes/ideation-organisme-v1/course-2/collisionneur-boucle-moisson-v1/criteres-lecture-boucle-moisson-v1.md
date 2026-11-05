# Critères de lecture — collisionneur « boucle itérative moisson ↔ fiches ↔ bisociateur » (question v1 de conv-audit), tour 1 (sous-tours E3-T1, E3-T2, E3-T3) — v1

session-depot (instance 3, seconde session), 1er novembre 2026, ≈ 10:27 UTC. **Scellés avant l'ouverture de toute cellule** : le run
`donnees/collisionneur-boucle-moisson-v1/run-boucle-moisson-e3-v1/` est **en cours** à l'heure du scellement (lancé 09:41 UTC sous
GO-2026-11-01-03 ; dix cellules faites d'après le journal, T3-C et T3-D restantes) ; aucune cellule n'a été lue par l'auteur de ces
critères, qui ne lira que le journal de lancement, `etat.md` et la sortie de `collisionneur_v7.py verifier` à la fin du run. Ils ne sont
pas modifiés après scellement (R12). Modèle : les critères du tour 1 des nœuds (`…/collisionneur-noeuds-v1/criteres-lecture-noeuds-v12-tour1-v1.md`,
`22edbf47…`), dont les critères 1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 13, 22, 23 et 25 s'appliquent tels quels (« annexe du tour 2 » y désigne
l'annexe des recommandations que conv-audit servira au tour 2, non servie et non lue par le lecteur) ; ce qui suit les adapte à une
question de conception à sept volets.

Pièces : question v1 `donnees/collisionneur-boucle-moisson-v1/question-collisionneur-boucle-moisson-fiches-v1.md` (`72b4f149…`, 797 mots,
identique à `question-etage3.md` du run) ; faits v1 `faits-boucle-moisson-v1.md` (`53f78bb2…`, 14 237 mots : pièce 1 dossier factuel de
l'organisme § 1, 2, 3, 7, 9, 10 ; pièce 2 rétrodiction de Swanson ; pièce 3 état des lieux de Gu et Krenn et décision de Lazar du
1er novembre ; pièces 4a et 4b lectures des essais de la mémoire ; l'antériorité de la boucle **n'est pas servie**) ; balayage
`balayage-faits-boucle-moisson-v1.txt`. Les systèmes publiés que Q6 nomme (Swanson et Arrowsmith ; Rzhetsky, Foster et Evans 2015 ;
Sourati et Evans 2023 ; Gu et Krenn 2024 ; AI Scientist v2, Agent Laboratory, Co-scientist, Robin, The Agentic Scientist) ne sont pas des
faits servis : tout ce qu'une espèce leur attribue est RAPPORTÉ (R7), sauf ce que la pièce 3 porte sur Gu et Krenn.

## A. Garde

1. **Niveau** : la question est au niveau méthode ; aucune conception d'attaque, rien sur le bras d'attaque ni sur l'auto-organisation
   inspirée d'Avalon (sujet suspendu) : tout passage qui y toucherait est compté « hors question », sans lecture de fond.
2. **La demande de Lazar reformulée est l'objet à critiquer, pas un fait** : une espèce qui la tient pour acquise sans la discuter est
   « acquiescente » (notée, pas écartée) ; la décision de Lazar sur Gu et Krenn (pièce 3) est un fait de la question (vrai par
   construction), pas un accord.
3. **Chiffres du dossier factuel** : tout chiffre qu'une espèce attribue aux pièces (24 contre 12 associations, −0,82 point, 0,27 / 0,55,
   nombres de fiches, coûts par course, etc.) est recoupé sur `faits-boucle-moisson-v1.md` (ligne) ; inexact ou absent → « inexact sur
   les pièces », par espèce. Les étiquettes d'état du dossier (DÉCIDÉ, PROPOSÉ, ESSAYÉ, CODÉ NON ACTIVÉ, PAS CONSTRUIT) sont des faits :
   une espèce qui prend un PROPOSÉ ou un PAS CONSTRUIT pour un existant est « inexacte sur l'état ».

## B. Les sept volets (unité de lecture : le volet)

4. **Q1 (objet, état minimal, règle d'arrêt, garde contre la boucle qui tourne en rond)** : par espèce, la définition d'« embryon » retenue,
   l'état minimal mesurable entre deux versions (ou l'aveu qu'« affiner » = « reformuler »), la règle d'arrêt (gain marginal, budget) avec
   son seuil s'il est chiffré, et la garde ; une règle d'arrêt sans grandeur mesurable est « non opérationnelle ».
5. **Q2 (moisson ciblée sans fuite)** : par espèce, la dérivation des requêtes, la garde contre la fuite (aucun texte de test, aucun
   identifiant d'épisode) et contre la redondance (ne ramener que ce que la fiche cite), et la réponse à « métadonnées et résumés seuls
   suffisent-ils ? » ; une garde contre la fuite non mécanique (« on fera attention ») est « non opérationnelle ».
6. **Q3 (appariement élargi, trois bras)** : par espèce et par bras (« loin mais proche », « jamais reliés », « trou à structure commune »),
   ce qui change dans la règle ; si le vivier élargi noie les fiches (réponse et raison) ; les nombres proposés (paires par bras, fiches par
   proposeur) **avec la base invoquée** : un nombre sans base est « non motivé ».
7. **Q4 (allocation)** : bandit contre allocation uniforme avec arrêt ; pire cas de chacun ; un avis sans pire cas est « incomplet ».
8. **Q5 (rétrodiction)** : validité du test à date de coupure pour un champ jeune ; témoins manquants nommés ; la fuite par les modèles
   entraînés après la coupure et la fermeture proposée (vérifiable ou non) ; le lecteur relève si l'espèce s'appuie sur la rétrodiction de
   Swanson (pièce 2) et la cite juste.
9. **Q6 (ce qui existe, reprendre tel quel)** : par espèce, la liste des systèmes et, pour chacun, « reprendre tel quel » / « s'inspirer »
   / « écarter » avec la raison ; tout RAPPORTÉ ; une espèce qui attribue à un système une capacité précise sans source est « RAPPORTÉ sans
   source » (compté).
10. **Q7 (ordre)** : boucle avant la course 2, course 2 d'abord, ou boucle en génération 2 ; la raison ; le lien avec le pré-pilote.

## C. Accords, divergences, apports

11. Critères 7, 8, 9, 12, 13 du tour 1, l'unité étant le volet ; symétrie R4 (critère 10) : accord à quatre = réserve ; option présentée la
    première ou avec le plus de détail par la question (le bandit en Q4 ; la boucle elle-même en Q7) = réserve « effet d'ordre ».
12. **Options manquantes** : toute forme de boucle ou d'allocation que la question ne nomme pas est « apport » ; le lecteur relève si elle
    est reprise par une autre espèce.
13. **Lien avec la non-convergence** (chantier de session-depot, hors question) : si une espèce lie la boucle à une dynamique qui tourne en
    rond (Q1) par un mécanisme nommé, le lecteur le note comme apport sans le juger.

## D. Synthèse

14. **Forme** : en tête, auteur (lecteur neuf, modèle nommé ; s'il est celui d'une espèce, le dire), date UTC relevée après la lecture
    complète, empreintes recalculées de tout ce qui a été lu, état du run, annexe du tour 2 non lue ; décompte : accords (et larges),
    convergences nées de la critique, divergences résolues / non résolues, apports seuls, inexactitudes sur les pièces (par espèce),
    inexactitudes sur l'état, RAPPORTÉ sans source, acquiescences, réponses non opérationnelles, passages hors question ; puis une table par
    volet Q1 à Q7 (position de chaque espèce en T1 et en T3, raison, pire cas et garde, pièce qui trancherait) ; puis la liste des
    divergences non résolues et des accords trop propres pour le tour 2 (annexe de conv-audit).
15. **Traçabilité** : chaque affirmation renvoie à une cellule (`E3-Tn-…-X.md`, section), à la question (volet) ou à une pièce des faits
    (numéro, ligne) ; recalcul montré en une ligne quand il y en a un.
16. **Rien n'est tranché ; aucune recommandation du lecteur** : la boucle est une décision de programme de Lazar ; le collisionneur ne décide
    rien.
17. **Ordre et lecteur** : lecture complète de toutes les cellules valides avant d'écrire ; lecteur neuf qui n'a pas écrit ces critères ;
    modèle nommé.
