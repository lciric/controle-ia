# Dessin : une primitive d'expérience bornée dans le noyau (v1, brouillon)

Écrit par la lignée « session-depot » le 26 octobre 2026, à partir de 01:12 UTC, sur le GO de Lazar (R-471). Brouillon :
il sera confronté aux réponses des tours du collisionneur « agents outillés » (`donnees/collisionneur-agents-outilles-v1`)
et « interface de calcul bornée » (`donnees/collisionneur-agents-outilles-methodo-v1`, en cours), puis contre-lu par un
sous-agent neuf avant tout code. Rien n'est scellé ; aucun pilote scellé n'est modifié (version nouvelle du noyau).

## 1. Le but

Fermer la boucle « hypothèse → test bon marché → résultat rendu → révision » **dans** la course. Aujourd'hui l'organisme
ne peut tester ses hypothèses que par nous, hors de la course. Le test H-M1 l'a montré : une hypothèse de l'essaim,
testée par nous, a échoué pour une raison qu'un pré-test de quelques centimes aurait révélée. Le modèle répondait par une
lettre d'option au lieu de « Yes » ou « No » (R-459). L'essaim ne l'a jamais su.

## 2. Ce qui ne change pas

Les quatre raisons d'être de l'isolation restent entières :
- **validité** : vérités de `test` et de `test_final` et juge hors d'atteinte ;
- **dépense** : tout coût passe par le noyau, sous plafond et réservation au pire cas ;
- **secrets et dépôt** : aucune clé ni accès au dépôt pour l'organisme ;
- **traçabilité** : tout passe par une primitive journalisée.

L'organisme n'exécute jamais de code sur la carte. La carte n'exécute que du code fixe du noyau ; les textes de
l'organisme y sont des **données**.

## 3. Les primitives (minimum)

Toutes portent sur des **textes écrits par l'organisme**, jamais sur des tâches de la banque.

| primitive | entrée | rendu | jamais rendu |
|---|---|---|---|
| `activations` | jusqu'à N textes (≤ L jetons chacun), couches parmi une liste fixe, position : dernier jeton ou un jeton marqué | un identifiant de jeu de traits, gardé par le noyau ; formes et normes | rien d'une tâche de la banque |
| `repondre` | jusqu'à N dialogues (système, utilisateur, préremplissage d'assistant facultatif), une liste de jetons cibles | log-probabilités des jetons cibles au premier jeton, les k jetons de tête et leur masse ; génération gloutonne facultative de ≤ G jetons | — |
| `entrainer` étendu | comme aujourd'hui, mais sur un jeu de traits de l'organisme, avec **ses propres étiquettes** | identifiant de sonde | vérités de la banque |
| `predire` étendu | une sonde, des identifiants de textes de l'organisme | probabilités | — |

Dans `repondre`, le préremplissage et le tour séparé sont permis : ce sont les parades que proposent les réponses
d'Argon et du collisionneur sur la suite de H-M1. Avec `repondre`, l'organisme peut mesurer lui-même la validité d'une
question de verbalisation (masse « Yes » plus « No » par cellule) avant de s'en servir.

## 4. Les gardes

1. **Textes** : on refuse tout texte qui reprend une tâche de la banque, quelle que soit sa part (`train`, `test`,
   `test_final`). Le test est une quasi-copie : recouvrement de 5-grammes (Jaccard) au-dessus d'un seuil fixé d'avance,
   et une garde exacte par empreinte.
   - Avec la garde de fuite de la moisson, ce test ferme le canal « faire passer un texte de test au modèle et lire sa
     réponse ».
   - Le seuil est testé sur un cas sain et sur un artefact (R5) : des paraphrases d'items de test doivent être refusées.
2. **Étiquettes** : seules celles de l'organisme, sur ses textes. Aucune vérité de la banque n'est servie, sous aucune
   forme.
3. **Budget**, par génération et par course :
   - nombre de requêtes, nombre de textes, jetons au total, secondes de carte ;
   - réservation au pire cas avant l'exécution, au tarif horaire de la carte fixé dans la configuration ;
   - le refus est un statut, jamais un texte.
4. **Analyse adaptative** : la primitive ne touche aucun item de test, donc elle n'ouvre aucun canal nouveau vers les
   vérités. Le seul canal existant reste le score de `test` rendu par génération, inchangé. Les mesures de l'organisme
   portent sur ses propres stimuli : il peut surapprendre ses stimuli, pas le test.
5. **Canaux auxiliaires** : temps de calcul rendu arrondi, messages d'erreur fixes, tailles bornées. La carte ne lit aucun
   fichier de l'organisme hors de la requête.
6. **Journal** : chaque requête et chaque rendu sont consignés (`journal-experiences.jsonl`), avec les empreintes des
   textes, les secondes de carte, le coût et la graine. Tout est déterministe : type de nombre fixé, pas
   d'échantillonnage sauf graine journalisée.

## 5. L'exécution sur la carte

Trois options :
- **(i) Noyau sur l'instance à carte pendant la course.** Le modèle est chargé une fois ; la primitive est synchrone.
  Coût : celui de la carte pendant toute la course (≈ 1,1 USD/h pour une A100, illustratif ; 2 à 5 USD pour une course
  de 2 à 4 h). Le plus simple. **Recommandé pour le premier pilote.**
- **(ii) File asynchrone entre générations** : les requêtes de la génération g sont exécutées par un travail sur carte, et
  leurs résultats arrivent à la génération g+1. Moins cher, mais la boucle est lente : un aller-retour par génération.
- **(iii) Ouvrier à carte loué pendant la fenêtre d'une génération** : entre les deux.

Le modèle ouvert est celui de l'étape 1 : Llama-3.1-8B-Instruct, révision `0e9e39f2…`, révision vérifiée par le dossier
du cache (R-456).

## 6. Exploration contre confirmation

- Tout ce que l'organisme mesure avec la primitive est de l'**exploration**. Il peut en tirer un instrument (une question
  de verbalisation, une sonde, une direction) et le servir à ses castes pour classer les tâches. La seule mesure qui
  décide reste le juge du noyau sur `test_final`, inchangé.
- Au-delà, une **confirmation** préenregistrée, côté humain, peut reprendre les hypothèses et les instruments que
  l'organisme déclare à la fin de la course, sur des stimuli neufs construits hors de la course.
  - La sortie de course s'enrichit d'un fichier `hypotheses-testees.json` : hypothèse, instrument, stimuli, résultats de
    la primitive.
  - L'hypothèse n'est pas vérifiée par le juge. Elle est une proposition pour la confirmation.

## 7. Ce qui reste ouvert

- Les bornes chiffrées (N, L, G, k, requêtes et secondes de carte par génération) : à fixer par une répétition sur un
  modèle minuscule, puis par devis.
- Le seuil de quasi-copie : à fixer par un essai sur la banque v3, avec des paraphrases.
- La forme exacte du contrat pour les organismes : version du contrat, et compatibilité avec les organismes qui ne
  l'emploient pas.
- La coordination avec conv-audit : quel noyau porte la primitive (celui de l'étape 1 ou celui du pilote 4), et quel texte
  de pilote l'emploie en premier.
- Le devis de location (GO de calcul) avant tout essai réel.

## 8. Étapes

1. Ce dessin v1, puis v2 nourrie des réponses du collisionneur, puis contre-lecture R2 par un sous-agent neuf.
2. Le code, sur une branche neuve depuis la tête du noyau convenue avec conv-audit, avec des essais sain et artefact :
   garde de quasi-copie, budget, refus, journal, déterminisme.
3. Une répétition sur processeur avec un modèle minuscule du Hub (sans dépense).
4. Un devis, puis un GO de calcul, et un premier pilote descriptif qui emploie la primitive, sous un texte scellé par
   conv-audit.
