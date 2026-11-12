# P3-bis, écart 1 (R-2399) — contre-lecture de l'addendum 1 (brouillon 1) et du lanceur d'écart — v1

- Contre-lecteur neuf : sous-agent, **Claude Fable 5.2** (`claude-fable-5-2`), autre modèle que le développeur et le
  rédacteur (Opus 5.5). N'a écrit aucune pièce de P3-bis. **N'a lu aucun fichier de T0.7.**
- Écrit le 2026-11-11 à 23:48 UTC (heure relevée par `date -u`).
- Consigne : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-contre-lecture-ecart1-p3bis-v1.md`
  (`fffc7380bf308b1fe2716017ecb02dddf333021d1df9c656ce3ec30dee51533f`, vérifiée avant lecture).
- Aucun appel à l'outil de location réel, aucun appel de modèle, aucune dépense, aucun commit. Écrit : ce rapport et
  son compagnon ; un bac à sable sous `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/p3bis-ecart1-cl/`
  (arbre détaché en extraction partielle au commit d'écart, quatre chemins, aucun chemin interdit ; il y reste).

## Verdict

**Scellable après corrections** : une correction du lanceur (C1, obligatoire : une garde est affaiblie au-delà de
R-2399, constat rejoué), donc un lanceur sous un nom neuf, et les corrections de l'addendum qui en découlent (A1 à A7).
Rien d'autre ne s'oppose au scellement.

## Pièces relues (empreintes recalculées)

| Pièce | Empreinte | État |
|---|---|---|
| brouillon 1 de l'addendum, `brouillons/P3-bis-temoin-positif-v1/P3-bis-addendum-1-garde-credit-v1-brouillon1.md` | `0cf6c08bf78b56d1983e93026b9a60b9cab431acee889c4f4fd4d4e446e3bfec` | égale à la consigne |
| lanceur d'écart, `docs/procedures/P3-bis-temoin-positif-v1/lancer_p3bis_v2_ecart1_v1.sh` au commit `e13df72b94510fba947a2262fa2274624bef7da4` | `dc33635ff01c90326044ae17471e2bbaeccf424975dcb34b21e0ae83921ad1ea` | égale ; compagnon conforme |
| lanceur d'origine, `lancer_p3bis_v2.sh`, à S `8f8df8b2726a69568b4d4a54bae16188e7f1b3d0` et au commit d'écart | `029bdb5c114a6166a21fa93724d71a2bf6158dc9686993424f6fbe8462352b08` | identique aux deux commits |
| texte scellé `prereg/P3-bis-temoin-positif-v1.md` à S | `76ab66ce967796b944e2ca585ee0dc2d780189e8e0cbe429e390c427a46121cb` | égale (2813 lignes) |
| rapport du développeur, script d'essais, journal d'essais | `19c13a84…`, `acf6f7c8…`, `6ca23702…` | égales à l'addendum ; compagnons du dossier et des sorties conformes |
| consoles E1, E8, E9 citées par l'addendum | `68d47f87…`, `d31ac955…`, `8f574e6b…` | égales |
| `registres/decisions.md` au commit `4c0a3791…` | `c914bffb62399a7bd05e2a08b32ba8d16ad5052f900f1ebea6408ac38b7fdfda` | égale ; R-2386, R-2394 à R-2401 lues |

Du texte scellé, lu : l. 1128, 1840-1848 (table des issues, ligne 1 et suivantes affichées), 1930-2014 (liste d'arrêt),
2145-2154, 2170-2177, 2278-2292, et des lignes isolées rendues par la recherche des mots « crédit », « recharge »,
« code cité », « commit du code », `CHAINE_P3BIS`, `COMMIT_CODE_P3BIS`. Les mots « crédit » et « recharge » n'y
paraissent qu'aux l. 1128, 1937, 2151 et 2285 : l'addendum couvre les quatre.

## 1. Le diff du lanceur

`git diff --name-status S e13df72b` : 42 ajouts, aucun fichier modifié ni retiré (40 sous
`docs/notes/g0-deux-semaines-v1/p3bis-ecart1-v1/`, le lanceur d'écart et son compagnon) ; S est ancêtre du commit
d'écart, qui est son seul descendant sur la branche.

`diff lancer_p3bis_v2.sh lancer_p3bis_v2_ecart1_v1.sh` : sept blocs, tous dans les trois zones permises par R-2399.

| Bloc | Zone | Constat |
|---|---|---|
| `1a2,15`, `39c53`, `45c59` | en-tête, usage | conformes |
| `94,95c108,109` | contrôle de soi | conforme : `lancer_p3bis_v2.sh=$H/lancer_p3bis_v2.sh` ; le lanceur d'origine du dossier est comparé à sa copie de S comme les quatorze autres scripts ; le lanceur d'écart lui-même n'est comparé à rien (condition d'emploi 1 de l'addendum ; son empreinte est écrite sur la ligne « lanceur p3bis v2 » de `lancement.txt`, rejoué) |
| `189,192c203,210`, `194a213,229`, `196,197c231,232` | garde du crédit | conforme à R-2399 **sauf le constat C1** |

Toutes les autres gardes sont octet pour octet celles de S (dates, place, S, preuves, GO relu trois fois, jetons,
contrôles avant dépense, amorce, ligne « Lancement », branches, offres, liste fermée des instances, garde de calcul,
création). La clé lue par la relecture de l'écart (`["credit"]`) est celle du module commun
(`verifications_p3bis_v2.py`, fonction `credit`, l. 339-356 à S).

### C1 (à corriger, lanceur) — outil de location en échec avec une réponse lisible : l'écart crée, l'origine refusait

Ligne 210 du lanceur d'écart :
`if [ "$c" = 0 ] && [ "$cu" != 0 ]; then c=$cu; fi   # comme le tube d'origine (pipefail) : outil en échec, code de l'outil`.
Le commentaire n'est vrai que si le module rend 0. Si l'outil sort en échec **et** que sa sortie se lit avec un crédit
sous le minimum (module à 3), le tube d'origine rendait 3 et **refusait** (« crédit insuffisant ») ; le lanceur d'écart
garde `c=3`, ignore `cu`, relit un crédit positif et **crée**. Sous le lanceur d'origine, un outil en échec n'a
jamais mené à une création ; sous l'écart, si. R-2399 ne lève que le seuil du crédit, pas ce refus.

Rejoué au faux outil (bac à sable des essais, mêmes copies jouées, instance nommée 12345678) :

| Cas | Lanceur | Réponse, code de l'outil | Obtenu |
|---|---|---|---|
| X1 | écart v1 | `{"credit": 6.0}`, code 1 | **code 0, création demandée** (77777773) ; ligne officielle puis ligne d'écart écrites |
| X1o | origine | `{"credit": 6.0}`, code 1 | code 3, aucune création |
| X1b | écart v1 | `{"credit": 50.0}`, code 1 | code 2, aucune création (comme l'origine) |
| X2 | écart v1 | vide, code 3 | code 2, aucune création |

Gravité : faible en probabilité (il faut un outil en échec dont la sortie reste un objet JSON à champ `credit`),
mais c'est une garde affaiblie hors du périmètre de l'écart, et aucun des treize essais ne la couvre (E5 : outil en
échec **sans** réponse).

**Correction, couple exact** (lanceur sous un nom neuf, R12 : `lancer_p3bis_v2_ecart1_v2.sh`, le v1 gardé) —
ligne 210, remplacer

```
if [ "$c" = 0 ] && [ "$cu" != 0 ]; then c=$cu; fi   # comme le tube d'origine (pipefail) : outil en échec, code de l'outil
```

par

```
if [ "$cu" != 0 ]; then unset REPONSE_USER; printf '%s\n' "$CREDIT_LIGNE" | tee -a "$T/lancement.txt"; echo "crédit illisible (show user, outil en échec, code $cu) : pas de création"; exit 2; fi   # outil en échec : jamais de création, même si sa réponse se lit
```

(plus le nom neuf dans l'en-tête et l'usage, l. 2, 53 et 59). Éprouvée par moi sur une copie du bac à sable : outil en
échec code 1 avec `{"credit": 6.0}` → code 2, aucune création ; code 1 sans réponse → code 2 ; code 3 avec réponse
lisible → code 2 ; crédit 0 et −2,5 → code 3 ; « six » → code 2 ; 6,0 et 50,0 avec outil sain → code 0, création
factice. Essais R5 à ajouter au script d'essais (nom neuf) : l'artefact X1 (attendu : code 2, aucune création, aucune
ligne d'écart) ; E5 change de dernière ligne (« … outil en échec, code 1 … »).

### C2 (recommandé, même version neuve) — crédit positif sous le centime

`{"credit": 0.004}`, outil sain : le lanceur d'écart v1 **crée** (rejoué, X7) alors que la ligne officielle écrite au
journal dit « crédit 0.00 USD ». Le module commun arrondit au centime (`round(c, 2)`) ; la relecture de l'écart, non.
Couple : ligne 227, `sys.exit(0 if v > 0 else 3)'` → `sys.exit(0 if round(v, 2) > 0 else 3)'` (éprouvé : 0,004 →
code 3, aucune création). Sans effet pratique sur un compte à recharge automatique ; met le journal et la garde d'accord.

### Valeurs limites rejouées, conformes (écart v1)

`true`, `NaN`, `Infinity`, liste, chaîne `"6.0"`, champ absent : code 2, aucune création, aucune ligne d'écart
(arrêt au module commun ; la branche « illisible à la relecture » reste inatteignable, comme le dit le rapport).

### Essais rejoués

Script d'essais du commit d'écart joué en entier dans mon arbre (de 23:40:31 à 23:43:38 UTC, `date -u`) : code 0,
dernière ligne « ESSAIS DU LANCEUR D'ÉCART 1 DE P3-BIS : CONFORMES », treize cas conformes ; journal rejoué égal au
journal versé hors heures, durées et commit factice ; consoles **E1, E6, E8, E9** rejouées identiques aux consoles
versées (commits et chemins normalisés). E6 et E7 refusent au bloc 2, avant tout appel à l'outil ; E8 (origine, 6 USD)
refuse, E9 (écart, 6 USD) crée : la différence de comportement est bien celle de l'écart, et elle seule, hors C1.

Aval : relu par recherche dans les scripts de la chaîne à S ; `lancement.txt` n'y est lu que par les clés
`commit`, `branche`, `creation`, `etiquette`, `offre choisie`, `instance` ; aucune ne rencontre la ligne
d'écart ni l'empreinte du lanceur. Confirmé par E10 à E12.

## 2. L'addendum

Fond : il dit juste ce qui change (la garde du crédit, quatre passages) et ce qui ne change pas ; la règle neuve est
celle de R-2399 ; la réserve au verdict est écrite (« garde du crédit levée par écart, R-2399 ») ; le risque résiduel
est dit, instances nommées en marche comprises. Les trois mots de Lazar sont recopiés à l'identique du registre
(R-2396, R-2398, R-2399), heures comprises ; 31,43 USD (R-2394) et 6,11 USD à 23:14:48Z (R-2398) sont exacts.

Citations du texte scellé, vérifiées mot pour mot (retours à la ligne près) : l. 1937 et 1947 ; l. 2151-2152 ;
l. 1128 ; l. 2285 ; l. 1952-1954 ; l. 2289 ; l. 1844 (« si le code cité n'a pas changé »). Toutes exactes.
Renvois de lignes : 1936-1946, 1949-1954, 1955-1961, 1962-1968, 1999-2000, 2149-2152 exacts ; deux à resserrer (A5).

Corrections (ancien → neuf ; les anciens sont recopiés du brouillon 1, retours à la ligne près) :

- **A1** (suite de C1 ; « Moyen », premier point, et condition d'emploi 1) : nom, empreinte et commit du lanceur →
  ceux de `lancer_p3bis_v2_ecart1_v2.sh` (valeurs du développeur) ; « (seul commit au-dessus de S, ajouts
  seulement) » → à réécrire selon la branche (deux commits d'ajouts) ; dire que le v1 (`dc33635f…`) est gardé et
  **n'est jamais joué pour une création** ; essais : script, journal, nombre de cas et consoles de la version neuve.
- **A2** (« Ce qui change », règle neuve) : « crédit nul ou négatif : aucune création ; crédit illisible : aucune
  création. » → « crédit nul ou négatif (au centime) : aucune création ; crédit illisible, ou outil de location en
  échec même si sa réponse se lit : aucune création. » ; et, table, première ligne : « un crédit présent nul ou
  négatif, ou illisible ; » → « un crédit présent nul ou négatif, ou illisible, ou un outil de location en échec ; ».
- **A3** (« Moyen », différences, (c)) : « > 0, suite ; ≤ 0, code 3, aucune création ; illisible, code 2. » → ajouter
  « ; outil en échec, code 2, même si sa réponse se lit ».
- **A4** (« Moyen », premier point) : « comme le texte scellé le prévoit déjà pour une relance (l. 1952-1954 : … ) »
  → « par analogie avec ce que le texte scellé prévoit pour un autre cas, la relance après une instance arrêtée
  (l. 1952-1954 : … ) : un lanceur neuf sous un nom neuf y est un écart déclaré, non une version neuve du texte ».
  Le passage cité vise un lanceur qui ajoute une instance aux tolérées, pas la garde du crédit.
- **A5** (renvois) : « l. 2009-2012 » → « l. 2009-2011 » (deux fois : « Ce qui ne change pas », point ouvert 1) ;
  « le GO (GO-2026-11-10-02, l. 1940-1943) » → « le GO (GO-2026-11-10-02, l. 1940-1941) ».
- **A6** (statut, et réponses ci-dessous) : « puis scellement, versement sur la branche de scellement après S et sur
  `main`. » → « puis scellement par le compagnon `.sha256`, versement sur `main` et, dans un commit après celui du
  lanceur d'écart, sur la branche d'écart `prep/p3bis-ecart1-credit-v1` (tirée de S) ; `scellement/p3bis-v2` reste
  à S ; entrée au registre des décisions ; aucune clé dans `registres/scellements-v1.md`. » ; la section « Points
  ouverts du brouillon 1 » est remplacée par les réponses (a), (b), (c) ci-dessous, ce rapport cité par son chemin et
  son empreinte.
- **A7** (« Objet », facultatif) : « sans qu'aucun risque de dépense non couverte ne le justifie » contredit à moitié
  la section du risque résiduel → « alors que la recharge automatique tient le solde au-dessus de zéro ».

## 3. Réponses aux questions du rédacteur

**(a) Forme du scellement — oui, avec une précision.** Le texte (l. 2009-2011) interdit toute autre clé de P3-bis dans
`registres/scellements-v1.md` : l'addendum se scelle donc par son compagnon, son versement et une entrée au registre
des décisions, comme la mère le propose. La chaîne accepte une branche qui porte des commits après S : tout ce que
lisent le lanceur et les contrôles se rapporte à **S**, jamais à la tête d'une branche — `S` ajoute
`prereg/P3-bis-temoin-positif-v1.md.sha256` (lanceur l. 104) ; une branche distante contient S (l. 107 ; vrai
aujourd'hui de `origin/scellement/p3bis-v2` et d'`origin/prep/p3bis-ecart1-credit-v1`, relevé sur le clone local,
sans `fetch`) ; scripts et preuves comparés à `git show S:…` ; contrôles avant dépense sur un clone de S ; amorce
et `COMMIT=S` ; récupération : « S est ancêtre de la branche » de calcul. Le texte le dit lui-même (l. 2289 : « pas
forcément `main` »). Précisions : (1) R-2399 écrit « versés sur la branche de scellement après S » ; la mère propose la
branche d'écart, tirée de S : c'est mieux (`scellement/p3bis-v2` garde S pour tête), à consigner au registre comme la
lecture retenue ; (2) le lanceur se joue depuis un dossier où les quinze scripts d'origine sont ceux de S (un arbre de
la branche d'écart convient) ; (3) **non vérifié par moi, T0.7 m'étant interdit** : qu'aucun script de T0.7 (ni de T0.6)
ne parcoure `prereg/` par motif et ne bute sur un fichier `prereg/P3-bis-addendum-…` ; hors T0.7, je n'ai trouvé aucun
parcours de `prereg/` par motif dans `src`, `scripts`, `tests` et la chaîne. À faire vérifier par un agent qui
peut lire T0.7, avant le versement sur `main`.

**(b) Le lanceur d'écart est hors du « code cité » de la ligne 1 — oui, à une nuance d'énoncé près.** « Code cité »
désigne le commit du code de l'en-tête et son arbre gelé (contrôle 2 des contrôles avant dépense ; l. 2289-2291 :
« aucun épisode joué, code inchangé » ; l. 37). Vérifié : `git diff --quiet` sur les douze `CHEMINS_GELES` (aucun
sous `docs/`) rend 0 entre le commit du code `5e457525` et le commit d'écart, et entre S et le commit d'écart. Le
texte traite lui-même un lanceur neuf sous un nom neuf comme un « écart déclaré » compatible avec une relance « sous ce
texte » (l. 1952-1954). Nuance : la phrase du brouillon « Le lanceur n'est pas le code cité » est trop courte ; le
lanceur d'origine **est cité** par le texte, dans la chaîne (l. 2174-2175, `029bdb5c…`), et il ne change pas ; ce qui
s'ajoute est un fichier neuf, hors de l'arbre gelé. À écrire ainsi. La ligne 1 ne joue de toute façon que pour une
relance (N = 2 ou 3) ; selon R-2394, aucune instance de P3-bis n'a été créée.

**(c) Portée : toute tentative sous ce texte et ce GO — oui.** Le mot de R-2399 porte sur la garde, pas sur un
lancement ; la condition d'emploi 3 du brouillon le dit bien. Bornes à garder écrites : borne de création du
18 novembre 2026 ; une relance reste soumise à la ligne 1 et, s'il y a lieu, au nœud « Relance après une instance
gardée ou arrêtée » ; la réserve au verdict vaut pour toute la course dès qu'une création s'est faite sous l'écart ;
tout mot contraire de Lazar sur la recharge suspend l'écart (condition 4). Le constat de Lazar tenu pour valable
jusqu'à mot contraire est conforme à R-2399 ; pour une création qui tarderait de plusieurs jours, un relevé du crédit
par la mère avant le lancement (déjà sa pratique, R-2395, R-2398) suffit, sans nœud neuf.

## 4. Points ouverts

1. C1 demande un passage du développeur (une ligne, un essai, nom neuf) puis la mise à jour de l'addendum (A1 à A3) ;
   si la mère choisit de ne pas refaire le lanceur, l'addendum doit alors déclarer C1 comme une limite connue : je ne
   le recommande pas, la correction est d'une ligne.
2. Vérification (a)(3) par un agent autorisé à lire T0.7.
3. Mon arbre détaché reste dans le bac à sable (`git worktree list` le montre) ; je ne l'ai pas retiré.
