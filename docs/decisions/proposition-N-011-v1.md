# Proposition — nœud N-011 — équivalence de production de T0.4 (demi-précision) — v1

Rédigée le 2026-10-05 par la session de mise en œuvre, après le verdict R13 scellé `docs/verdicts/verdict-T0.4-critere-1-G0-v2.md` (sha256 `98d53c70c09ff9b4c0eea4f7ae8779d6dfa10bb6401ca6ac4567283c6fac07cb`). La table gelée du préenregistrement v2 prescrit « réserve et nœud, au vu du repère ». C'est donc un nœud, sans défaut : j'attends ta décision.

## Décision

Comment rendre conforme l'équivalence de production (P4), en demi-précision, pour finir de prouver le critère 1 de G0, maintenant que la logique est validée.

## Enjeu

**Ce qui est acquis** (run `20261005-144628-validation-reelle`, H200 NVL) :
- logique du harnais validée sur le modèle réel : en double précision, écart maximal 9,8e-13 pour un seuil de 1e-4 ;
- le défaut D1, injecté exprès, est vu sur 20 actions sur 20 (au moins 5,7e-2) ;
- contrôles négatifs, rejeu dans le processus, relecture du disque, 192 tests : conformes.

**Ce qui manque :**
- **P4 contraire.** En demi-précision, l'écart maximal entre génération et passe unique vaut 0,52 pour un seuil de 0,1 ; 28 actions sur 40 dépassent.
- **P7 non atteint.** Le run s'arrête sur P4, avant le run B : le rejeu entre deux processus n'a pas tourné.

**Ce que montrent les données** (verdict, sections 5 et 6) :
- Tous les dépassements sont dans le contexte des lignes remplies à gauche (couches 15 et 23), aucun dans la zone générée (maximum 0,076).
- Une ligne sans remplissage donne un écart exactement nul.
- Avec remplissage, l'écart médian par jeton (0,014 à 0,019) ne dépend pas de la quantité de remplissage (3 à 441 jetons). C'est le niveau du repère : la demi-précision seule s'écarte de la double précision de 0,013 en médiane.
- Les maxima de la production restent sous ceux du repère (jusqu'à 0,79 à la couche 23, sans génération ni remplissage). La demi-précision a une longue queue sur quelques jetons.
- Explication probable : un noyau d'attention par tuiles somme dans un autre ordre quand le remplissage décale les jetons. C'est de l'arrondi, pas un défaut de logique.

**Ce qui reste ouvert** (réserve du juge) :
- le chemin de production n'est éprouvé par aucun contrôle strict : demi-précision, noyaux d'attention fusionnés, remplissage ;
- le noyau effectivement choisi n'est pas consigné.

**Le seuil de 0,1 sur le maximum ne tient pas en demi-précision.** Je l'avais fixé en supposant une queue d'au plus 1e-2. Le relever sur le maximum, au niveau du repère (0,8 à 1,6), rendrait la garde aveugle : en production, le plus petit maximum du contrôle négatif vaut 1,06, et un tel seuil ne le séparerait plus de l'arrondi.

## Options

**(a) Version 3 : garde de production sur le 99e centile, seuil fondé sur le repère, et contrôle strict du chemin de production.**
- En production, la garde lit, par action et par couche, le 99e centile des écarts par jeton, au lieu du maximum. Le contrôle négatif lit la même grandeur. Le maximum reste rapporté, sans seuil.
- Le seuil se fonde sur le repère, pas sur les valeurs vues en production : par exemple 0,2, soit deux fois le 99e centile du repère (0,087 à la couche 23). La génération et la passe unique s'écartent chacune de la double précision.
- Une phase de contrôle s'ajoute en simple précision, avec les noyaux de production et le remplissage, et avec le défaut D1 injecté. Elle répond à la réserve du juge. En simple précision, l'arrondi attendu est de 1e-4 à 1e-3 (1,27e-4 mesuré dans la v1 avec le noyau « math ») et D1 vers 5e-2 : ils se séparent.
- Le noyau d'attention de production est fixé et consigné.
- Avantages :
  - la production reste en demi-précision, donc le budget des phases suivantes est tenu ;
  - la garde garde son rôle (voir un désalignement) sans buter sur la queue d'arrondi ;
  - la réserve du juge est traitée ;
  - le run B s'exécute (P7).
- Inconvénients :
  - la statistique change (du maximum au 99e centile) : il faut la justifier par le repère seul, sinon on paraît déplacer le but ;
  - un cycle complet : code, tests, deux contre-lectures, scellement, run ;
  - environ une journée de travail et 2 à 4 dollars de carte.

**(b) Version 3 : production en simple précision** (génération et extraction), seuil de 0,1 gardé.
- Avantages :
  - aucun changement de statistique ;
  - équivalence attendue vers 1e-3 au plus ;
  - lecture la plus simple.
- Inconvénients :
  - les phases suivantes génèrent en simple précision : environ deux fois plus d'heures de carte et de mémoire. Au devis, la phase 1 passerait de 200 à 300 heures à 400 à 600, soit environ 250 à 500 dollars de plus ;
  - la demi-précision ne serait jamais validée.

**(c) Pas de version 3.**
- La logique reste validée, avec réserve sur la production.
- Avantage : aucun coût.
- Inconvénient : le critère 1 de G0 reste non prouvé (P4 et P7), donc la porte G0 ne peut pas se franchir sur ce critère.

## Recommandation

**(a)**, avec une confiance d'environ 65 %.
- La logique est acquise avec une marge de dix ordres de grandeur. Les écarts de la production restent dans l'enveloppe de la demi-précision mesurée par le repère.
- Le défaut est dans la statistique (le maximum, en demi-précision), pas dans le harnais.
- (a) garde le régime de calcul du devis et traite la seule réserve ouverte.
- Le risque principal tient à la justification du changement de statistique. Je l'écrirai dans le préenregistrement v3, avec la règle « jamais sur le maximum observé ». Je la soumettrai à deux contre-lectures neuves.

## Défaut

Aucun : nœud. J'attends ton GO sur une option.

## Autre point : N-009, destruction des instances

- Les cinq instances arrêtées coûtent leur disque chaque jour, dont environ 1,85 dollar par jour pour la H200 NVL (54332340).
- Le disque de 54332340 garde la seule copie des 16 fichiers de tableaux de la production. Le juge note qu'ils ne suffisent pas à localiser les jetons fautifs : les captures de génération n'ont été écrites nulle part.
- Recommandation : détruire 54183350, 54285455, 54298522 et 54311651 dès maintenant, et 54332340 après ta décision sur N-011.
