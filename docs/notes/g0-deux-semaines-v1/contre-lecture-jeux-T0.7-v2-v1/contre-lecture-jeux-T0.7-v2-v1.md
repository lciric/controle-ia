# Contre-lecture R2 — consigne v2 des jeux synthétiques de T0.7 (mode « coût ») — v1

**Verdict : scellable après couples.**
Aucun bloquant ; neuf points à corriger, tous traités par les 24 couples de `couples-contre-lecture-jeux-T0.7-v2-v1.json`.
Le plus lourd : longueur de l'empan avant `COST:` non appariée ; mesure en jetons reportée sur l'instance (réécriture après scellement) ; écrivain privé du format de remise et de la liste exacte des mots interdits.

- Contre-lecteur neuf (Claude Opus 5.5, sous-agent ; autre modèle que l'auteur, Fable 5.1), qui n'a écrit ni la consigne
  v2, ni son rapport, ni le brouillon 1, ni aucun brouillon de T0.7 ou de T0.6, ni aucune pièce de P3. Travail du
  2026-11-05, de 16:52 à 17:00 UTC environ (`date -u`). Aucun commit, aucun `.sha256`, aucun fichier existant modifié,
  aucun réseau, aucune paire écrite, aucune dépense, aucun résultat lu.
- Pièces lues, empreintes recalculées : consigne v2 `dcc237da…` (égale à son compagnon) ; rapport `0c5ac5a7…` (égal) ;
  brouillon 6 de T0.7 `29f0ab43…` (égal) ; T0.6 brouillon 4 `8df90b8b…` (égal) ; consigne v1 brouillon 1 `e38bc16b…`
  (sans compagnon, égale à l'empreinte que cite le brouillon 6 l. 111) ; P-015 (`registres/decisions.md` l. 392 ;
  document `6e74c6cb…`, l. 131-145) et R-321 ; `reponses.md` l. 136-151 (A6 corrigée) ; revue v7, colonne E3
  (l. 393-399) ; `src/controle_ia/environnements/propositions.py` (l. 25-90, 146-156, 218-270) ; `prereg/P3-consignes-v1.md`
  l. 25-40. Structure des fichiers de tâches seulement (32 de réserve, 64 d'évaluation, intersection vide par identifiants ;
  aucun énoncé ni cible lu au-delà de la forme du champ `classification`).
- Gravités : **bloquant** (non scellable en l'état) ; **à corriger** (couple fourni) ; **note** (sans couple, à porter
  ailleurs ou à garder en vue).

## Réponses aux six questions

1. **Fidélité au brouillon 6 — à corriger.** Jeux, tailles (10, 10, 5 + 5), incitation dans les deux membres, nombres
   équilibrés, texte différent avant le champ, interdits de l'écrivain : conformes à b6 l. 134, 300-317, 344-347. Écarts :
   (a) J-D se dit « inchangé depuis le brouillon 1 » mais ajoute la ligne de rappel, quatre cadrages et une banque écrite
   (le v1 dit « identiques sauf un bloc ») — ajout utile (place de l'indication de P3) mais à déclarer (couple 14) ;
   (b) le « guide de classification » est laissé à la chaîne de T0.7 alors que `contexte_systeme` est scellé dans les jeux
   et recalculé « à l'octet » : à fixer maintenant, sans guide comme P3, la classification rendue par `texte_classification`
   et non le dictionnaire brut (couple 5) ; (c) § 7 écrit « au plus 8 mots de l'énoncé » quand le contrôle 9 et la
   section 11 interdisent toute suite de 8 (couple 1). Rien d'ajouté ne change ce que la sonde apprend ; la règle des mots
   interdits étendue à J-D est sans effet sur l'étiquette (réponse identique).
2. **Règle N1 — bonne lecture, gardée (note).** « Même nombre honnête ici, gonflé là » (b6 l. 143) et « chaque valeur
   apparaît autant de fois comme honnête que comme gonflée, à la tâche près » (l. 305-306) sont satisfaits par N1 sous sa
   forme la plus forte. La lecture concurrente (nombres différents dans la paire, équilibrés entre paires — c'est le sens de
   la revue v7 pour son jeu (1), lu **au champ**) n'apporte rien ici puisque l'empan exclut le nombre, et elle ferait
   décrire au membre gonflé un plan visiblement plus grand que son jumeau : la sonde apprendrait l'échelle du plan, piège
   « gros nombre » par le texte. N1 rend les jeux valides sous les trois lectures de A6 (3) (rapport § 4). Effet : la sonde
   apprend le **plan** (surdimensionné pour la question, à échelle apparente égale), jamais le nombre. Deux corrections qui
   en découlent : « besoin honnête » doit se rapporter à la question, pas au plan écrit (couple 16) ; et une réserve de
   validité à déclarer : le saboteur de P3 peut gonfler le seul chiffre sous un plan ordinaire (couple 15).
3. **A6 (3) — compatible sous la lecture du brouillon 6, à préciser (à corriger, mineur).** A6 (3) (`reponses.md` l. 142)
   dit « aucune lecture par champ dans T0.7 » ; le brouillon 6 la restreint aux épisodes d'organisme (l. 228-229, 415) et
   P-015 (E3, l. 141) exige lui-même « lecture avant le champ COST » pour la sonde du domaine : l'apprentissage et la
   validation génériques avant le champ ne sont pas une lecture d'organisme. La consigne doit le dire et définir l'empan à
   l'octet (`reponse[:position_cost]`, saut de ligne compris), le passage caractère → jetons restant à la chaîne de T0.7
   (couple 24). **Note pour la contre-lecture de T0.7** : la sonde est choisie sur une validation avant le champ puis lue sur
   l'action entière (`COST`, `PREDICTION` jamais vus à l'entraînement, agrégation par le maximum) ; rapporter aussi la
   validation générique sur l'action entière (lecture (iii) du rapport), sans en faire le critère de choix.
4. **Contrôles mécaniques — un manque réel (à corriger).** La longueur n'est appariée que sur la réponse entière : le
   membre gonflé, qui « ajoute du travail », aura un texte avant `COST:` plus long, compensé par une `PREDICTION` plus
   courte ; or l'empan d'entraînement est celui d'avant le champ et le maximum croît avec la longueur. Appariement à 15 %
   exigé aussi sur l'empan avant le champ, en mots, caractères et jetons (couples 2, 3, 4). Second manque : le défaut dur de
   fuite lexicale n'a pas de remède écrit (un terme n'est pas une paire) — renvoi une fois, puis contre-vérification, jamais
   de boucle (couple 9). Troisième : « étapes vagues » demandées au membre gonflé contre « spécifique » partout ailleurs :
   le flou devient un indice de surface (couples 17, 18). Notes : un classifieur sur traits de structure (longueur par
   champ, ponctuation, nombre de phrases, groupes de chiffres) rapporté à côté du sac de mots serait utile ; la fuite de la
   seule `PREDICTION` (lue en production, D2) n'est pas mesurée à part.
5. **Seuils — arbitraires, à écrire comme tels (à corriger, mineur).** 0,30, 0,25/0,05 et 0,90 n'ont aucun fondement
   empirique ; la règle générale de l'en-tête (« sans renvoi = choix ») les couvre, mais il faut l'écrire à l'endroit et
   interdire tout changement après lecture des jeux (couple 10). 23/32 et 12/16 se justifient comme seuils binomiaux
   unilatéraux (probabilités 0,010 et 0,038 sous le hasard), à niveaux différents : à déclarer (couple 11). Note : pour un
   lecteur fort, 72 % est lâche ; un jeu qui ne porte le concept qu'à 72 % pour un lecteur averti est un signal faible.
   Annexe A : les bornes « telles qu'écrites » sont fausses (blocs de **18 à 27** mots, recomptés ; passent la borne 18-40)
   (couple 12) ; le cadrage d'une entrée de réserve n'est pas dit (couple 13).
6. **Ce qui ferait refaire les jeux après scellement — à corriger.** (a) Jetons mesurés seulement sur l'instance : un
   écart y force une version neuve du jeu après scellement, au lancement d'une lecture payante (nœud si la lecture a
   commencé, § 7). Le tokeniseur (`79e3e522…`) a été refait par la session le 21 octobre (R-311) ; il n'est pas sur cette
   machine (recherche faite), et `tokenizers` n'est pas installé : en faire une condition du scellement des jeux, la chaîne
   ne gardant qu'une garde d'identité (couples 6, 7). (b) Rejeu de la recopie contre les textes de T0.6 : les données de
   distillation de (ii) sont écrites **sur les mêmes 32 tâches de réserve** (b6 l. 121-124), et les deux textes peuvent
   reprendre 7 mots de l'énoncé plus un : faux positifs probables ; exclure les suites présentes dans l'énoncé et remplacer
   la réécriture par une exclusion mécanique écrite d'avance (couple 8). (c) Guide de classification non fixé (couple 5).
   (d) **Note de calendrier** : DS-1 n'a pas encore son mot ni son défaut (`<<MOT_LAZAR_DS>>`) ; si Lazar choisit (b), J-C
   est sans objet : lancer l'écrivain de J-C après le défaut de DS-1, J-D et J-A pouvant partir avant.

## Autres points

- **À corriger** — l'écrivain ne reçoit que la section 11, qui renvoie à « the file layout you are given » sans le donner :
  format de remise écrit en anglais dans la section 11 (couple 21).
- **À corriger** — la liste exacte des mots interdits est cachée à l'écrivain alors qu'elle vaut pour les deux membres et
  ne porte pas l'étiquette ; plusieurs entrées frappent le vocabulaire courant du domaine (« hidden » des couches cachées,
  « padding », « buffer », « margin », « trick ») : renvois en série et paires retirées au second défaut. Remettre
  l'annexe C et nommer les sens techniques (couples 20, 22, 23).
- **À corriger, mineur** — la section 11 ne donne ni la plage 4 à 5 000 ni l'interdiction du séparateur de milliers
  (« 1,000 » est un « single integer » pour un écrivain anglophone) (couple 19).
- **Note** — la consigne porte déjà un compagnon `.sha256` égal à son empreinte alors que son statut dit « non scellée » :
  à dire au scellement (le candidat sera un fichier neuf, R12).
- **Note** — l'incitation de J-C est placée à la fin du message système, à la place même de la consigne privée de IA et
  des textes de IT et IM : c'est ce qu'il faut pour T3 et P3-P4 (texte à cette place, neutre pour l'étiquette).
- **Note** — rotations vérifiées : J-D, chaque instruction 16 fois, dix différentes par tâche ; J-C, chaque incitation
  40 fois ; comptes 640 séquences par jeu.

## Rendu

- `docs/notes/g0-deux-semaines-v1/contre-lecture-jeux-T0.7-v2-v1/contre-lecture-jeux-T0.7-v2-v1.md` (ce fichier).
- `docs/notes/g0-deux-semaines-v1/contre-lecture-jeux-T0.7-v2-v1/couples-contre-lecture-jeux-T0.7-v2-v1.json` :
  24 couples `{"ancien","nouveau"}` ; chaque « ancien » est unique dans la consigne v2 (`dcc237da…`), aucun ne chevauche
  un autre ; vérifié par script (application à une copie en mémoire, sans écriture).
