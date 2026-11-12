# Préenregistrement — P3-bis, addendum 1 : garde du crédit à la création remplacée par écart (R-2399) — v1 — brouillon 2

- Auteur : rédacteur neuf (sous-agent, Claude Opus 5.5), consigne
  `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-redaction-p3bis-addendum1-v1.md`
  (`ae9deca66f3684cd6d25d7cda07c34c20f988ec48fa97802f17cdee706bc7be5`, vérifiée). Le rédacteur n'a écrit ni P3-bis, ni sa
  chaîne, ni le lanceur d'écart. Il n'a lu aucun fichier de T0.7. Du texte scellé, il n'a lu que les passages sur le
  crédit, la liste d'arrêt et les lignes citées ici. Le brouillon 2 suit un message de la mère du 2026-11-11 (après
  R-2406).
- Date (UTC) : brouillon 1, 2026-11-11, 23:35 (`0cf6c08bf78b56d1983e93026b9a60b9cab431acee889c4f4fd4d4e446e3bfec`) ;
  brouillon 2, 2026-11-11, 23:56 (`date -u`). Au scellement, la date du commit de scellement fait foi.
- Texte scellé complété : `prereg/P3-bis-temoin-positif-v1.md`
  (`76ab66ce967796b944e2ca585ee0dc2d780189e8e0cbe429e390c427a46121cb`), commit de scellement
  S = `8f8df8b2726a69568b4d4a54bae16188e7f1b3d0` (R-2386). Les numéros de ligne cités ci-dessous sont ceux de ce fichier.
- Registre cité : `registres/decisions.md` de `main` au commit `af712f39f35ddb00e71c18917cecefeedd388b2b`
  (`3842d8115f236326ee22a7e8719433f208180c2dc57e90b1e43b74755460979a`), entrées R-2386, R-2394 à R-2399, R-2401, R-2404,
  R-2406.
- **Nœud tranché par Lazar** : écart au préenregistrement scellé, R-2399 (2026-11-11 vers 23:16 UTC).
- Contre-lecture (R2) : `brouillons/P3-bis-temoin-positif-v1/P3-bis-ecart1-contre-lecture-v1.md`
  (`9b1013dbfe479a7b1cbcbe36fe88598b68037c24657f8d2f577789a908a9f33e`). Lecteur neuf d'un autre modèle (Claude Fable 5.2),
  verdict « scellable après corrections ». Correction C1 du lanceur exigée, correction C2 recommandée, couples A1 à A7
  pour l'addendum. Tout est retenu par la mère (R-2404) ; C1 et C2 sont faits dans le lanceur v2 (R-2406) ; A1 à A7 sont
  appliqués ici.
- Statut : brouillon 2, non scellé. Il sera scellé par son compagnon `.sha256`, puis versé sur `main` et, dans un commit
  postérieur à celui du lanceur d'écart, sur la branche d'écart `prep/p3bis-ecart1-credit-v1` (tirée de S).
  `scellement/p3bis-v2` reste à S. Une entrée est inscrite au registre des décisions. Aucune clé n'est écrite dans
  `registres/scellements-v1.md`. **Non décisif** : il ne touche ni à la lecture, ni à l'issue, ni au verdict, sinon par
  la réserve écrite plus bas.

## Objet

Le lanceur scellé `lancer_p3bis_v2.sh` refuse toute création tant que le crédit présent du compte de location est sous
20 USD plus 10 heures du prix des instances nommées en marche. Le 11 novembre, ce minimum valait 31,43 USD (R-2394), et
le crédit présent était bas (6,11 USD à 23:14:48Z, R-2398) parce que le compte se recharge automatiquement à solde bas
(R-2396, R-2398). P3-bis restait donc bloquée, alors que la recharge automatique tient le solde au-dessus de zéro. Cet
addendum remplace **cette seule garde**, pour la course de P3-bis sous ce texte.

## Mot de Lazar (verbatim)

- R-2399 (≈ 23:16 UTC) : « (b) Un écart écrit au texte scellé, qui tient la recharge automatique pour équivalente à la
  garde. : go ».
- Constat de la recharge automatique, R-2396 (≈ 22:46 UTC) : « vast se recharge tout seul, pon en est ou de la journee ? » ;
  R-2398 (≈ 23:14 UTC) : « j'ain chznge la cle kimi et recharge le nouveau compte kimi ; vast se recharge seul ».

## Ce qui change (garde du crédit seule)

Règle neuve : **la création est permise si la recharge automatique du compte de location est active (constatée par
Lazar, R-2396, R-2398) et si le crédit présent, lu dans la réponse de l'outil de location et arrondi au centime, est
strictement positif.** Les refus :
- crédit nul ou négatif (au centime) : aucune création ;
- crédit illisible : aucune création ;
- outil de location en échec, même si sa réponse se lit : aucune création.

| Passage du texte scellé | Phrase citée | Lecture sous l'écart |
|---|---|---|
| Liste d'arrêt, « Avant la création », l. 1936-1937 et 1947 | « un crédit sous 20 USD plus 10 heures du prix des instances nommées en marche ; […] : aucune création. » | se lit « un crédit présent nul ou négatif, ou illisible, ou un outil de location en échec ; […] : aucune création ». Les autres motifs de la même ligne (l. 1936-1946) ne changent pas |
| Plan, « Ce que le code et la chaîne doivent changer », point 6, logique neuve (ii), l. 2150-2152 | « crédit exigé à la création : ≥ 20 USD plus 10 heures du prix des instances nommées en marche, recharge automatique du compte (`registres/depenses.md` l. 91) » | se lit « crédit exigé à la création : crédit présent > 0 au centime et recharge automatique du compte active, constatée par Lazar ». Le montant de 20 USD plus 10 heures reste calculé et écrit au journal, sans bloquer |
| Table « ce qui change du 3 au 4 », ligne 14, l. 1128 | « ≥ 20 USD (≈ 9,5 h à 2,10) plus 10 h du prix des instances nommées en marche ; recharge automatique » | historique des brouillons, laissé tel quel ; lu sous l'écart comme la ligne précédente |
| Écarts du lanceur portés au texte, 8, l. 2285 | « recharge automatique du compte : non lisible par la chaîne, non contrôlée par elle » | **inchangé** : la recharge reste un fait déclaré par Lazar, que la chaîne ne vérifie pas (voir la réserve) |

Les mots « crédit » et « recharge » ne paraissent dans le texte scellé qu'à ces quatre lignes (1128, 1937, 2151, 2285),
selon le relevé de la contre-lecture.

## Ce qui ne change pas

- Le cœur de l'expérience : hypothèse, prédiction chiffrée et signe, métrique, seuil, plan d'analyse (hors le point 6
  (ii) ci-dessus), critères de lecture gelés.
- Tous les autres arrêts de la liste d'arrêt, dont les autres motifs « avant la création » (l. 1936-1946) : contrôles
  avant dépense, bornes de l'offre, liste fermée des instances, GO, borne de création du 18 novembre 2026, révocations.
- Le **plafond de 80 USD** de la dépense cumulée et sa surveillance (l. 1962-1968 ; point 6 (i), l. 2149-2150), arrêt
  par identifiant compris.
- Le GO (GO-2026-11-10-02, l. 1940-1941) et la date du rendez-vous (2026-11-20T12:00:00Z, l. 1999-2000).
- La règle de relance après une instance gardée ou arrêtée (l. 1949-1954).
- La ligne unique `SCELLEMENT-P3BIS` (l. 2009-2011) : cet addendum n'écrit aucune clé dans `registres/scellements-v1.md`.
- Tous les autres scripts de la chaîne, et `lancer_p3bis_v2.sh` lui-même, qui reste au dossier, égal à sa copie de S.

## Moyen

### Le lanceur d'écart v2

- Chemin : `docs/procedures/P3-bis-temoin-positif-v1/lancer_p3bis_v2_ecart1_v2.sh`.
- Empreinte : sha256 **`2e294e5a64086806591cdd0724561d7a8d7fdaab464705c22f9b92687d6607fb`** (compagnon `.sha256`
  conforme).
- Branche et commit : branche `prep/p3bis-ecart1-credit-v1`, commit `f3ff571d85b67770c2c8e53468fe918cda1d4310`. La branche
  porte deux commits au-dessus de S, `e13df72b94510fba947a2262fa2274624bef7da4` (v1) puis `f3ff571d…` (v2), tous deux
  d'ajouts seulement.
- Origine : copie de `lancer_p3bis_v2.sh` à S (`029bdb5c114a6166a21fa93724d71a2bf6158dc9686993424f6fbe8462352b08`, cité
  par le texte, l. 2174-2175, laissé tel quel), sous un nom neuf (R12).
- Lanceur v1 : `lancer_p3bis_v2_ecart1_v1.sh` (`dc33635ff01c90326044ae17471e2bbaeccf424975dcb34b21e0ae83921ad1ea`), gardé
  tel quel, **n'est jamais joué pour une création**.
- Précédent : la même forme est prévue par le texte scellé pour un autre cas, la relance après une instance arrêtée
  (l. 1952-1954 : « un lanceur neuf, sous un nom neuf (R12) […] c'est un écart déclaré »). Un lanceur neuf sous un nom neuf
  y est un écart déclaré, non une version neuve du texte. On l'applique ici par analogie.

### Ce qui diffère du lanceur d'origine

Différences relues sur `diff`. Rapports du développeur :
- `docs/notes/g0-deux-semaines-v1/p3bis-ecart1-v1/rapport-ecart1-lanceur-v1.md`
  (`19c13a84fb528ee9a8912aad1120fa766fc26c14a5649f2f8a147f07dcab65a7`) ;
- `docs/notes/g0-deux-semaines-v1/p3bis-ecart1-v1/rapport-ecart1-lanceur-v2.md`
  (`0162617a9e561d532bdbfc470b66e5836c4294084d36c3916c61a23663e3d002`).

Les différences :
- (a) l'en-tête et l'usage, sous le nom neuf ;
- (b) le contrôle de soi : le lanceur d'origine du dossier est comparé à sa copie de S, comme les autres scripts de la
  chaîne ;
- (c) le bloc 9, garde du crédit :
  - la ligne officielle du crédit (montant exigé de 20 USD plus 10 heures) est toujours écrite au journal et dans
    `lancement.txt` ; son refus « insuffisant » ne bloque plus ;
  - outil de location en échec : la ligne officielle est écrite, puis le lanceur rend le code 2, aucune création, même si
    sa réponse se lit (correction C1) ;
  - une ligne fixe d'écart est écrite : « écart 1 (R-2399) : garde du crédit remplacée par la recharge automatique du
    compte (mot de Lazar) ; crédit présent > 0 exigé » ;
  - le crédit de la même réponse est relu par programme et arrondi au centime comme dans le module commun (correction
    C2) : > 0, la création suit ; ≤ 0, code 3, aucune création ; illisible, code 2.

Rien d'autre ne change : selon la contre-lecture, toutes les autres gardes sont octet pour octet celles de S.

### Essais R5 du v2

Cas sain et artefacts, sur un faux outil de location ; aucun appel réel, aucune dépense.
- Script : `docs/notes/g0-deux-semaines-v1/p3bis-ecart1-v1/essais_ecart1_lanceur_p3bis_v2.sh`
  (`e9a8dc69f39aa41e69209136db97aa9c2a1ab00400ca947c804934eabdaf0762`).
- Journal : `docs/notes/g0-deux-semaines-v1/p3bis-ecart1-v1/essais-ecart1-lanceur-p3bis-v2.log`
  (`5ee8246ebfee9b6a71676ad06d5a330db4bdc24a1af81a9e7eb08fa651e98952`). 15 cas, dernière ligne « ESSAIS DU LANCEUR
  D'ÉCART 1 DE P3-BIS : CONFORMES ».

Les consoles citées sont sous `docs/notes/g0-deux-semaines-v1/p3bis-ecart1-v1/sorties-essais-v2/` ; tous les compagnons
sont conformes.

Artefacts refusés :
- crédit nul (E1, `console-E1-credit-nul.txt`, `68d47f8765191df9bb4b6a6442993350c8efd2a62431d72e4c4e2937c46bc34b`) et
  crédit négatif (E2) ;
- crédit illisible (E3, E4) ;
- outil en échec sans réponse (E5, `console-E5-outil-en-echec.txt`,
  `738a16475d14ddbd0e4cd20aca4be4116c0ae3b3c6ce10a08387609a089aedc9`) ;
- **outil en échec avec une réponse lisible** (E14, C1 : code 2, `console-E14-outil-en-echec-reponse-lisible.txt`,
  `f4152abfea2b95d1fe4be5b8fe01e0a600e928fd98f203dadf00c24014d0eae0`) ;
- **crédit sous le centime** (E15, C2 : code 3, `console-E15-credit-sous-le-centime.txt`, même empreinte que E1, ce qui
  est attendu : les deux consoles écrivent « crédit 0.00 USD » puis le même refus) ;
- lanceur d'origine absent ou modifié (E6, E7).

Témoin : le lanceur d'origine, à crédit bas, refuse (E8, `console-E8-temoin-origine-credit-6.txt`,
`d31ac9559367ff523b92e581d86d38d435fe5450659c860b2f8019f735cad79b`).

Cas sain :
- E9 : lanceur v2 à crédit bas, création factice, ligne officielle puis ligne d'écart (`console-E9-sain-credit-6.txt`,
  `8f574e6b53d5813bb66baaf52816b0a37a20c4b1326d5661049e4752d191351e`) ;
- E10 à E12 : contrôle à cinq minutes, surveillance et destruction conformes sur les traces de E9 ;
- E13 : crédit haut.

Témoin négatif (R4) : les essais v2 joués sur le v1 reproduisent C1 (E14 crée). Script
`sorties-essais-v2/temoin-essais-v2-sur-lanceur-v1.sh` (`b6dbc70c810e99092c1c88282b68613711896c91dfb1f9668fde55472720b132`),
journal `sorties-essais-v2/temoin-essais-v2-sur-lanceur-v1.log`
(`e23fb874f7962ed9fba65055c07b2e734242e5a9c34acb4253eae44e69df9752`).

### Aval inchangé

Aucun script en aval (contrôle à cinq minutes, surveillance, récupération, destruction, module commun) ne relit
l'empreinte du lanceur ni la ligne d'écart. C'est le constat des rapports et de la contre-lecture. Les contrôles avant
dépense jouent sur un clone de S.

## Conditions d'emploi

1. Avant chaque lancement, la session calcule le `sha256sum` du lanceur v2 et l'écrit, avec l'heure par `date -u`. Toute
   empreinte autre que `2e294e5a64086806591cdd0724561d7a8d7fdaab464705c22f9b92687d6607fb` : aucun lancement. Le lanceur
   d'écart ne vérifie pas sa propre empreinte.
2. Il est joué depuis un dossier de la chaîne où `lancer_p3bis_v2.sh` et les autres scripts d'origine sont ceux de S
   (sinon il refuse : E6, E7). Un arbre de la branche d'écart convient. Aucun autre script de la chaîne n'est remplacé.
   Le lanceur v1 et le lanceur d'origine ne sont jamais joués pour une création.
3. Il sert à toute tentative de la course sous ce texte et sous GO-2026-11-10-02, dans la borne de création de l'en-tête.
4. La recharge automatique est tenue pour active sur le constat de Lazar (R-2396, R-2398). Tout mot contraire de Lazar
   suspend l'écart : retour à la garde scellée, ou nœud.

## Réserve au verdict et risque résiduel

- **Réserve écrite au verdict**, transmise au lecteur R13 : « garde du crédit levée par écart, R-2399 ». Elle vaut pour
  toute la course dès qu'une création s'est faite sous l'écart.
- **Risque résiduel** : la recharge automatique n'est ni lue ni contrôlée par la chaîne (l. 2285). Si elle fait défaut
  pendant la course, le compte peut s'épuiser et l'instance être arrêtée par le loueur. Le risque touche aussi les
  instances nommées en marche sur le même compte. La surveillance et la liste d'arrêt s'appliquent alors telles quelles :
  - instance vue arrêtée deux fois de suite : arrêt par son identifiant et consignation (l. 1955-1961) ;
  - relance soumise à la règle « Relance après une instance gardée ou arrêtée » (l. 1949-1954, nœud de Lazar) ;
  - dépense cumulée toujours bornée à 80 USD (l. 1962-1968).

  L'écart ne relâche aucune de ces règles.

## Réponses aux questions du brouillon 1

Réponses de la contre-lecture, retenues par la mère (R-2404).

**(a) Forme du scellement.**
- L'addendum se scelle par son compagnon `.sha256`, son versement et une entrée au registre des décisions. En effet, le
  texte (l. 2009-2011) interdit toute autre clé de P3-bis dans `registres/scellements-v1.md`.
- Le versement se fait sur `main` et, dans un commit postérieur à celui du lanceur d'écart, sur la branche d'écart
  `prep/p3bis-ecart1-credit-v1` (tirée de S). `scellement/p3bis-v2` garde S pour tête. R-2399 disait « versés sur la
  branche de scellement après S » ; c'est la branche d'écart qui est la lecture retenue, consignée au registre.
- La chaîne accepte une branche qui porte des commits après S. Tout ce que lisent le lanceur et les contrôles se rapporte
  à S, jamais à la tête d'une branche. Le texte le dit lui-même : écart 11 du lanceur, l. 2289, « S en argument du
  lanceur, contenu dans une branche du dépôt distant (pas forcément `main`) ».
- **Vérifié par la mère** (R-2404) : aucun module de T0.7 ne parcourt `prereg/` par motif. Un fichier
  `prereg/P3-bis-addendum-…` ne gêne donc pas T0.7. Le contre-lecteur, à qui T0.7 était interdit, n'a trouvé aucun
  parcours de ce genre dans `src`, `scripts`, `tests` ni dans la chaîne.

**(b) Le lanceur d'écart est hors du « code cité » de la ligne 1 des critères (l. 1844 : « si le code cité n'a pas
changé »).**
- Le « code cité » désigne le commit du code de l'en-tête et son arbre gelé.
- Le lanceur d'origine est bien cité par le texte, dans la chaîne (l. 2174-2175, `029bdb5c…`), mais il ne change pas.
  Ce qui s'ajoute est un fichier neuf, hors de l'arbre gelé.
- La contre-lecture a vérifié que l'arbre gelé est identique entre le commit du code et le commit d'écart v1
  (`e13df72b…`), ainsi qu'entre S et ce commit. Le commit v2 (`f3ff571d…`) n'ajoute que des fichiers sous `docs/`
  (relevé par `git diff --name-status e13df72b f3ff571d` : ajouts seulement).
- La ligne 1 ne joue que pour une relance. Selon R-2394, aucune instance de P3-bis n'a encore été créée.

**(c) Portée.** L'écart vaut pour toute tentative sous ce texte et ce GO (condition d'emploi 3). Les bornes restent
écrites :
- borne de création du 18 novembre 2026 ;
- une relance reste soumise à la ligne 1 et, s'il y a lieu, au nœud « Relance après une instance gardée ou arrêtée » ;
- réserve au verdict dès la première création sous l'écart ;
- suspension sur tout mot contraire de Lazar (condition 4).

Le constat de Lazar est tenu pour valable jusqu'à mot contraire, ce qui est conforme à R-2399. Si la création tarde de
plusieurs jours, un relevé du crédit par la mère avant le lancement suffit (sa pratique, R-2395, R-2398), sans nœud
neuf.
