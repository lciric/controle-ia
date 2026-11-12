# Préenregistrement — P3-bis, addendum 1 : garde du crédit à la création remplacée par écart (R-2399) — v1 — brouillon 1

- Auteur : rédacteur neuf (sous-agent, Claude Opus 5.5), consigne
  `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-redaction-p3bis-addendum1-v1.md`
  (`ae9deca66f3684cd6d25d7cda07c34c20f988ec48fa97802f17cdee706bc7be5`, vérifiée). N'a écrit ni P3-bis, ni sa chaîne, ni
  le lanceur d'écart ; n'a lu aucun fichier de T0.7 ; du texte scellé, n'a lu que ses passages sur le crédit et sa liste
  d'arrêt.
- Date (UTC) : brouillon 1, 2026-11-11, 23:35 (`date -u`). Au scellement, la date du commit de scellement fait foi.
- Texte scellé complété : `prereg/P3-bis-temoin-positif-v1.md`
  (`76ab66ce967796b944e2ca585ee0dc2d780189e8e0cbe429e390c427a46121cb`), commit de scellement
  S = `8f8df8b2726a69568b4d4a54bae16188e7f1b3d0` (R-2386). Les numéros de ligne cités ci-dessous sont ceux de ce fichier.
- Registre cité : `registres/decisions.md` de `main` au commit `4c0a3791b638c29f6897e91857542d0aec6cfaac`
  (`c914bffb62399a7bd05e2a08b32ba8d16ad5052f900f1ebea6408ac38b7fdfda`), entrées R-2386, R-2394 à R-2399, R-2401.
- **Nœud tranché par Lazar** : écart au préenregistrement scellé, R-2399 (2026-11-11 vers 23:16 UTC).
- Statut : brouillon 1, non contre-lu, non scellé. Forme exigée par R-2399 : contre-lecture courte par un lecteur neuf
  d'un autre modèle (R2), puis scellement, versement sur la branche de scellement après S et sur `main`.
  **Non décisif** : il ne touche ni à la lecture, ni à l'issue, ni au verdict, sinon par la réserve écrite plus bas.

## Objet

Le lanceur scellé `lancer_p3bis_v2.sh` refuse toute création tant que le crédit présent du compte de location est sous
20 USD plus 10 heures du prix des instances nommées en marche. Le 11 novembre, ce minimum valait 31,43 USD (R-2394) et le
crédit présent était bas (6,11 USD à 23:14:48Z, R-2398) parce que le compte se recharge automatiquement à solde bas
(R-2396, R-2398) : P3-bis restait bloquée sans qu'aucun risque de dépense non couverte ne le justifie. Cet addendum
remplace **cette seule garde**, pour la course de P3-bis sous ce texte.

## Mot de Lazar (verbatim)

- R-2399 (≈ 23:16 UTC) : « (b) Un écart écrit au texte scellé, qui tient la recharge automatique pour équivalente à la
  garde. : go ».
- Constat de la recharge automatique, R-2396 (≈ 22:46 UTC) : « vast se recharge tout seul, pon en est ou de la journee ? » ;
  R-2398 (≈ 23:14 UTC) : « j'ain chznge la cle kimi et recharge le nouveau compte kimi ; vast se recharge seul ».

## Ce qui change (garde du crédit seule)

Règle neuve : **la création est permise si la recharge automatique du compte de location est active (constatée par
Lazar, R-2396, R-2398) et si le crédit présent, lu dans la réponse de l'outil de location, est strictement positif** ;
crédit nul ou négatif : aucune création ; crédit illisible : aucune création.

| Passage du texte scellé | Phrase citée | Lecture sous l'écart |
|---|---|---|
| Liste d'arrêt, « Avant la création », l. 1936-1937 et 1947 | « un crédit sous 20 USD plus 10 heures du prix des instances nommées en marche ; […] : aucune création. » | se lit « un crédit présent nul ou négatif, ou illisible ; […] : aucune création » ; les autres motifs de la même ligne (l. 1936-1946) sont inchangés |
| Plan, « Ce que le code et la chaîne doivent changer », point 6, logique neuve (ii), l. 2150-2152 | « crédit exigé à la création : ≥ 20 USD plus 10 heures du prix des instances nommées en marche, recharge automatique du compte (`registres/depenses.md` l. 91) » | se lit « crédit exigé à la création : crédit présent > 0 et recharge automatique du compte active, constatée par Lazar » ; le montant de 20 USD plus 10 heures reste calculé et écrit au journal, sans bloquer |
| Table « ce qui change du 3 au 4 », ligne 14, l. 1128 | « ≥ 20 USD (≈ 9,5 h à 2,10) plus 10 h du prix des instances nommées en marche ; recharge automatique » | historique des brouillons, laissé tel quel ; lu sous l'écart comme la ligne précédente |
| Écarts du lanceur portés au texte, 8, l. 2285 | « recharge automatique du compte : non lisible par la chaîne, non contrôlée par elle » | **inchangé** : la recharge reste un fait déclaré par Lazar, que la chaîne ne vérifie pas (voir la réserve) |

## Ce qui ne change pas

Hypothèse, prédiction chiffrée et signe, métrique, seuil, plan d'analyse (hors le point 6 (ii) ci-dessus), critères de
lecture gelés ; tous les autres arrêts de la liste d'arrêt, dont les autres motifs « avant la création » (l. 1936-1946 :
contrôles avant dépense, bornes de l'offre, liste fermée des instances, GO, borne de création du 18 novembre 2026,
révocations) ; le **plafond de 80 USD** de la dépense cumulée et sa surveillance (l. 1962-1968 ; point 6 (i), l. 2149-2150),
arrêt par identifiant compris ; le GO (GO-2026-11-10-02, l. 1940-1943) ; la date du rendez-vous (2026-11-20T12:00:00Z,
l. 1999-2000) ; la règle de relance après une instance gardée ou arrêtée (l. 1949-1954) ; la ligne unique
`SCELLEMENT-P3BIS` (l. 2009-2012 : cet addendum n'écrit aucune clé dans `registres/scellements-v1.md`) ; tous les autres
scripts de la chaîne, et `lancer_p3bis_v2.sh` lui-même, qui reste au dossier égal à sa copie de S.

## Moyen

- **Lanceur d'écart** : `docs/procedures/P3-bis-temoin-positif-v1/lancer_p3bis_v2_ecart1_v1.sh`,
  sha256 **`dc33635ff01c90326044ae17471e2bbaeccf424975dcb34b21e0ae83921ad1ea`** (compagnon `.sha256` conforme), branche
  `prep/p3bis-ecart1-credit-v1`, commit `e13df72b94510fba947a2262fa2274624bef7da4` (seul commit au-dessus de S, ajouts
  seulement). Copie de `lancer_p3bis_v2.sh` à S (`029bdb5c114a6166a21fa93724d71a2bf6158dc9686993424f6fbe8462352b08`,
  laissé tel quel), nom neuf (R12), comme le texte scellé le prévoit déjà pour une relance (l. 1952-1954 : « un lanceur
  neuf, sous un nom neuf (R12) […] c'est un écart déclaré »).
- **Différences avec le lanceur d'origine** (relues sur `diff`, et rapport
  `docs/notes/g0-deux-semaines-v1/p3bis-ecart1-v1/rapport-ecart1-lanceur-v1.md`,
  `19c13a84fb528ee9a8912aad1120fa766fc26c14a5649f2f8a147f07dcab65a7`) : (a) en-tête et usage sous le nom neuf ;
  (b) contrôle de soi : le lanceur d'origine du dossier est comparé à sa copie de S, comme les autres scripts de la chaîne ;
  (c) bloc 9 : la ligne officielle du crédit (montant exigé de 20 USD plus 10 heures) est toujours écrite au journal et
  dans `lancement.txt`, son refus « insuffisant » ne bloque plus ; une ligne fixe d'écart est écrite
  (« écart 1 (R-2399) : garde du crédit remplacée par la recharge automatique du compte (mot de Lazar) ; crédit présent > 0
  exigé ») ; le crédit de la même réponse est relu par programme : > 0, suite ; ≤ 0, code 3, aucune création ; illisible,
  code 2. Rien d'autre ne change.
- **Essais R5** (cas sain et artefacts, faux outil de location, aucun appel réel, aucune dépense) : script
  `docs/notes/g0-deux-semaines-v1/p3bis-ecart1-v1/essais_ecart1_lanceur_p3bis_v1.sh`
  (`acf6f7c800894d8b67a922490e7fdf8707290ecbaf7d208933f4e4aa0a23eb47`), journal
  `docs/notes/g0-deux-semaines-v1/p3bis-ecart1-v1/essais-ecart1-lanceur-p3bis-v1.log`
  (`6ca23702c372eb328c3175dcc7c36aaad53fd27feff16129d3b6076e7f109a22`), dernière ligne « ESSAIS DU LANCEUR D'ÉCART 1 DE
  P3-BIS : CONFORMES », 13 cas. Artefacts refusés : crédit nul (E1, console
  `sorties-essais-v1/console-E1-credit-nul.txt`, `68d47f8765191df9bb4b6a6442993350c8efd2a62431d72e4c4e2937c46bc34b`) et
  négatif (E2), illisible (E3 à E5), lanceur d'origine absent ou modifié (E6, E7) ; témoin : lanceur d'origine à crédit bas
  refusé (E8, `console-E8-temoin-origine-credit-6.txt`, `d31ac9559367ff523b92e581d86d38d435fe5450659c860b2f8019f735cad79b`) ;
  cas sain : lanceur d'écart à crédit bas, création factice, ligne officielle puis ligne d'écart
  (E9, `console-E9-sain-credit-6.txt`, `8f574e6b53d5813bb66baaf52816b0a37a20c4b1326d5661049e4752d191351e`), puis contrôle à
  cinq minutes, surveillance et destruction conformes sur ses traces (E10 à E12) ; crédit haut (E13). Chemins des consoles
  relatifs à `docs/notes/g0-deux-semaines-v1/p3bis-ecart1-v1/`, compagnons conformes.
- **Aval inchangé** : selon le rapport, aucun script en aval (contrôle à cinq minutes, surveillance, récupération,
  destruction, module commun) ne relit l'empreinte du lanceur ni la ligne d'écart ; les contrôles avant dépense jouent sur
  un clone de S.

## Conditions d'emploi

1. Avant chaque lancement, la session calcule `sha256sum` du lanceur d'écart et l'écrit (heure par `date -u`) ; toute
   empreinte autre que `dc33635ff01c90326044ae17471e2bbaeccf424975dcb34b21e0ae83921ad1ea` : aucun lancement. Le lanceur
   d'écart ne vérifie pas sa propre empreinte.
2. Il est joué depuis le dossier de la chaîne, où `lancer_p3bis_v2.sh` reste égal à sa copie de S (sinon il refuse, E6,
   E7) ; aucun autre script de la chaîne n'est remplacé.
3. Il sert à toute tentative de la course sous ce texte et sous GO-2026-11-10-02, dans la borne de création de l'en-tête ;
   le lanceur d'origine n'est plus employé pour la création.
4. La recharge automatique est tenue pour active sur le constat de Lazar (R-2396, R-2398) ; tout mot contraire de Lazar
   suspend l'écart (retour à la garde scellée, ou nœud).

## Réserve au verdict et risque résiduel

- **Réserve écrite au verdict** (transmise au lecteur R13) : « garde du crédit levée par écart, R-2399 ».
- **Risque résiduel** : la recharge automatique n'est ni lue ni contrôlée par la chaîne (l. 2285). Si elle fait défaut
  pendant la course, le compte peut s'épuiser et l'instance être arrêtée par le loueur ; le risque touche aussi les
  instances nommées en marche sur le même compte. La surveillance et la liste d'arrêt s'appliquent alors telles quelles :
  instance vue arrêtée deux fois de suite, arrêt par son identifiant et consignation (l. 1955-1961) ; relance soumise à
  la règle « Relance après une instance gardée ou arrêtée » (l. 1949-1954, nœud de Lazar) ; dépense cumulée toujours
  bornée à 80 USD (l. 1962-1968). L'écart ne relâche aucune de ces règles.

## Points ouverts du brouillon 1 (à trancher avant le scellement)

1. Forme du scellement : la l. 2009-2012 interdit toute autre clé de P3-bis dans `registres/scellements-v1.md` ; l'addendum
   se scelle donc par son compagnon `.sha256`, un commit sur la branche de scellement après S et une entrée au registre
   des décisions. À confirmer, et à vérifier que la chaîne (écart 11 du lanceur, l. 2289 : « S en argument du lanceur,
   contenu dans une branche du dépôt distant (pas forcément `main`) ») accepte une branche de scellement qui porte des
   commits après S.
2. Critères de lecture, ligne 1 (l. 1844, vue dans une sortie de recherche, non lue au-delà) : une relance sous ce texte
   exige notamment « si le code cité n'a pas changé ». Le lanceur n'est pas le code cité (`COMMIT_CODE_P3BIS`) ; à confirmer par la contre-lecture
   que l'emploi du lanceur d'écart n'y touche pas.
3. Durée de validité du constat de Lazar : ce brouillon le tient pour valable jusqu'à mot contraire (condition 4) ; la mère
   peut préférer une confirmation de Lazar si le lancement tarde.
