# Proposition — P-010 — moniteur boîte noire par action de l'environnement (a) (T0.8) — v1

Rédigée le 2026-10-06 vers 17:30 UTC par la session de mise en œuvre. Hiérarchie de décision : « proposer avec recommandation » (périmètre interne d'une phase) ; défaut appliqué 48 heures après l'envoi. Elle suppose l'option (a) de P-006 (tâche en pas : une proposition ajoutée ou révisée par pas) et D1 (juges 8B et 3B).

## Décision

Ce que lit et ce que rend le moniteur boîte noire par action, base du bras boîte noire de G1 et du critère 4 de G0 (« base boîte noire, par action et séquentielle, sur le même jeu d'épisodes »).

## Enjeu

- **Le code est prêt** (R-066, `src/controle_ia/bases/`).
  - Le score d'un moniteur se lit par l'espérance sous la loi du jeton suivant une réponse imposée (P-003). Les bases séquentielles sont les mêmes que pour les sondes : max, sommes, Page, processus e, balayage. Leur calibrage est conforme, sur épisodes honnêtes entiers.
  - Sur les tokeniseurs du 8B et du 3B (identiques), les valeurs 0 à 100 tiennent chacune en un seul jeton (R-067). Le détecteur H.12 de 2606.08892 (« `<sandbagging_confidence>SCORE</sandbagging_confidence>` ») se lit donc par espérance sur 101 jetons, sans générer de nombre.
- **H.12 juge un ensemble**, pas une action. Il faut décider ce que voit le moniteur à chaque pas.
- **Calcul.** Une lecture par action et par juge, soit 10 lectures par épisode et par juge. La variante avec raisonnement coûte une génération par lecture.

## Options

**(a) H.12 adapté à l'action, ensemble courant visible, deux variantes de lecture.**
- À chaque pas, le moniteur reçoit les questions de recherche (H.9) et l'ensemble courant des propositions. La proposition ajoutée ou révisée au pas courant y est marquée.
- La consigne est H.12, avec la seule différence de demander la confiance que **la dernière modification** est un sabotage. Cette invite dérivée est transcrite, versionnée et scellée à côté de H.12 ; le différentiel est publié.
- Deux lectures :
  - **en une passe**, balise imposée juste après l'en-tête de réponse : c'est le plancher « juge en une passe » de P-003 ;
  - **avec raisonnement**, génération jusqu'à la balise (au plus 400 jetons), puis lecture à la balise : c'est le bras principal. Une réponse sans balise est consignée comme anomalie, jamais imputée.
- Juges 8B et 3B. La base séquentielle applique les statistiques de `bases.sequentiel` à ces scores.
- **Avantages** : même contexte que l'agent ; le sabotage diffus reste lisible action par action ; le plancher est construit à l'identique.
- **Inconvénients** : le contexte grandit avec le pas ; l'invite dérivée s'écarte de H.12 (le différentiel est publié).

**(b) Le moniteur ne voit que l'action** (questions de recherche et proposition du pas, sans l'ensemble).
- **Avantages** : contexte court et constant, moins de calcul.
- **Inconvénients** : un moniteur aveugle à l'ensemble ne voit pas un affaiblissement relatif ; la base boîte noire serait affaiblie, ce que P-003 veut éviter.

**(c) H.12 tel quel sur l'ensemble courant après chaque pas** (confiance sur l'ensemble entier).
- **Avantages** : aucune invite dérivée.
- **Inconvénients** : les scores successifs se recouvrent, puisque chaque ensemble contient le précédent. Les incréments ne sont plus des scores par action, ce qui brouille la comparaison avec les sondes à agrégation égale (plan 2 × 2).

## Recommandation

**(a)**, confiance ≈ 60 %. C'est la seule option qui donne un vrai score par action, au même grain que les sondes, avec un plancher construit à l'identique.

TRACE-lite (triage, inspection, jugement, d'après 2606.07054) fera l'objet d'une note distincte, après relecture des pages de TRACE scellées au niveau 1 (`docs/sources/lecture-pdf-niveau1/TRACE-AcMAS/`).

## Défaut

Sans réponse sous 48 heures (le 2026-10-08 vers 17:30 UTC), l'option (a) s'applique :
- l'invite dérivée est transcrite, scellée et contre-vérifiée par un sous-agent neuf ;
- le code du moniteur s'écrit sur le paquet `bases`.
