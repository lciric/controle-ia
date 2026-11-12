# Contre-lecture R2 — consigne v3 du jeu de phrases des concepts sans lien de T0.7 (troisième tour) — cl1

- **Objet** : `docs/procedures/consigne-concepts-sans-lien-T0.7-v3.md` (sha256 `f3b9b4a8ebbc69ed10bbdccef414f48cf298c0727b88c25190ff43ad1d0b3af2`, égale à la commande) et son journal `…-v3-journal-v1.md` (`2031a0271644fd1535912b4e800e2aed60cfe8fa26980c9ac84e68510b43465e`).
- **Contre-lecteur** : Claude Fable 5.2, sous-agent neuf de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy` ; n'a écrit ni cette consigne, ni ses versions précédentes, ni le script ; d'un autre modèle que le rédacteur (Opus 5.5). Travail du 2026-11-10, de 10:55:42 à 11:08:02 UTC (heures relevées par `date -u`).
- **Exclusion** : j'ai lu des lignes du brouillon 21 de T0.7 ; je suis exclu de tout rôle de lecteur de P3-bis, et de tout rôle de lecteur de ce jeu.

## Verdict

**Scellable définitivement après les couples ci-dessous ; non scellable en l'état.** Un bloquant (B-1 : la remise au lecteur dit le rang du tour, renvoie à la v2 et porte la règle d'acceptation) ; onze constats à corriger ; quatre mineurs. Le fond tient : la v3 traite les causes relevées sans toucher aux questions qui ont fait échouer (Q1, Q3, Q4, Q5 mot pour mot, vérifié), les annexes A et B et la ligne de format sont égales à l'octet à celles de la v2, les quatre exemples passent tous leurs contrôles au tokeniseur réel, et le repli s'accorde au brouillon 21 à trois formulations près (A-8).

## Réponses aux sept points de la commande

1. **Remède sans abaisser la barre : oui, sous B-1.** Journaux de décompte comptés par motif, sans afficher de phrase : tour 1, sept « Q5 non » et un « Q1 » ; tour 2, quatre « Q5 non » et deux « Q4 oui » ; **aucun motif Q2** aux deux tours. Q1, Q3, Q4, Q5 et les trois branches de la règle sont ceux de la v2 mot pour mot (comparé à [v2 § 7]). **Q2** : le retrait de « même structure grammaticale » est la conséquence nécessaire de la phrase neutre libre, et la question gagne « toutes deux un énoncé général » ; elle n'a fait échouer aucune paire : jugé recevable, à déclarer comme changement du juge (c'est fait, réserve 8). **Q6** : rapportée seulement, recevable ; son statut ne doit pas être dit au lecteur (B-1h). Deux durcissements, tous deux déclarés : n < 56 est un échec, pas de remise complémentaire. Un écart non déclaré : l'échantillon passe de ⌈n / 10⌉ à « 7 » (B-1d, A-11).
2. **Ce que le témoin contrôle : gardé.** `direction_concept` (`temoins.py`, `3b051b6f…`, l. 57-88) concatène tous les jetons de chaque côté et soustrait deux moyennes ; l'appariement phrase à phrase ne sert qu'au rapport des longueurs. Une différence de style propre à un côté entre dans la direction ; elle rend le témoin **plus facile à faire passer au-dessus de son plancher**, donc déclenche un audit plus souvent : le sens de l'erreur est prudent pour ce qu'une sonde de sabotage doit montrer. L'appariement par longueur (C3, moyenne signée de C13) tient les positions de jetons, lues dans le même gabarit. Le registre n'est tenu que par le lecteur et par C13 : la section 1 promet « mêmes signes d'écriture » sans qu'aucune mesure compte virgules, traits d'union et apostrophes (A-10, mesure (d)). **C14 est un filet partiel** : rejoué sur les huit exemples calqués de la v2, il en arrête cinq (E1, E2, E3, E4, E7) ; la part de mots communs y est de 0,15 à 0,56 (moyenne 0,32) contre 0,06 à 0,15 (moyenne 0,08) pour les exemples de la v3 : le seuil de réserve de 0,25 sépare les deux façons d'écrire, je ne propose pas de le changer (M-3, M-4).
3. **C14, C15, annexe C.** Vérifié par programme : annexe C bien formée, sans doublon, disjointe de l'annexe A et des lexiques des autres concepts ; 132 et 34 entrées ; noyau libre : 11 entrées sur 19 pour `chats`, 47 sur 58 pour `geographie` ; aucune entrée du noyau couverte en partie. Pas de contradiction avec C7 (une phrase dont le seul mot du noyau est à l'annexe C passe C7 et tombe à C15 : en défaut de toute façon). Trous de l'annexe C contre la section 4.1 : noms de race et noms propres écrits en minuscules hors des quatre et des dix listés, chasse sans les mots de l'annexe A (`predator`, `carnivore`), soin (`flea`, `neutered`, `vaccine`), `hostile` que la remise à l'écrivain cite et qu'aucune liste ne porte (A-3). **72 paires : faisable** pour les deux concepts ; coût attendu en renvois : homographes de l'annexe C (`land`, `rest`, `drop`, `fall`, `age`, `bold`, `warm`), mots de météo interdits à la géographie par C7 (`rain`, `snow`, `wind`, `climate` : M-2), suites banales de quatre mots (C14). Réserve probable de C13 pour `chats` : `cat/cats` dans plus de 60 % des phrases. `hairball` reste au noyau : risque à Q4 (maladie), laissé au jugement de la mère.
4. **Exemples E9 à E12 : rejoués, conformes.** Tokeniseur de `/home/user/lot3-concepts/tokeniseur/` (trois empreintes égales à [v2 § 6]), hors ligne, `tokenizers` 0.23.2, `transformers` 5.18.0 : jetons 23/26, 21/23, 21/21, 26/26 ; écart relatif maximal 0,115 ; 20 à 22 mots ; alphabet fermé, aucune majuscule ni espace fautif ; aucun mot de l'annexe A ; aucun mot de l'annexe B dans les phrases neutres ; un mot du noyau et aucun mot d'un autre concept ni de l'annexe C dans chaque phrase du concept ; aucune suite commune de quatre ni de trois mots dans une paire ; distance minimale 18 entre eux, 16 aux exemples de la v2, aucune suite commune de six mots ; C4 : `jetons_texte`, `_ids` et compte nu égaux pour les huit phrases (`FormatChat`, date « 26 Jul 2024 », `empans.py` et `formats.py` de `main`). **La note de la section 5 est exacte.** Deux défauts de fond, non de contrôle (A-2) : E9 donne pour modèle un outil tranchant sous la règle « nothing sharp » ; E12 porte « thousands » d'un seul côté sous la règle des mots de nombre. Les deux phrases de remplacement proposées sont rejouées de même : 23/23 et 25/26 jetons, tous contrôles passés, annexe C étendue comprise.
5. **Remises.** À l'écrivain : autonome, sans seuil du juge ni histoire, à un mot près (« for this round », M-1). Au lecteur : **B-1** ; et les clés du fichier de réponses, que le script exige dans l'ordre, n'y sont pas (A-1).
6. **Repli et brouillon 21** (`f7dcb226…`, lignes 185, 186, 1403, 1449, 1794, 2080, 2493, 2536) : accord sur le fond (clé permise, aucun assemblage à moins de quatre concepts, T7-P9 non lue, étape A menée). Trois écarts de lettre (A-8) : le texte de la réserve (T0.7 écrit R15 dans ses mots), l'instant (« strictement avant l'instant de fermeture », première ligne `OUVERTURE-T07` ou plus tôt sous G5, et non « à l'ouverture »), et l'inscription de la ligne (« dans la session où l'acceptation est prononcée »). Une contradiction interne : 6.1 veut une version suivante de la consigne si un exemple échoue, 9.1 fait d'un refus qui exige de changer la consigne un échec du tour, sans consigne v4 (A-7). Hors de mon objet, à porter par la mère : le brouillon 21 cite la v3 sans empreinte (l. 724) et ne porte pas la réserve 5 (deux règles d'écriture dans un même fichier).
7. **Liste fermée du script** (script v2 `a858c40c…`, 2468 lignes, lu par `git show`) : cohérente dans l'ensemble, **incomplète sur six points** : empreinte de la consigne exigée des pièces des deux premiers tours (A-4b) ; contrôles appliqués aux paires gardées à l'assemblage (A-4a) ; forme du bloc `exemples` (A-5) ; statut de C6 (A-6) ; place de `Q6` dans les clés (A-1b) ; fichiers du second lecteur de Q4 (A-9) ; taille de l'échantillon (A-11).

## Constats

### Bloquant

**B-1 — La remise au lecteur porte l'histoire des échecs et la règle d'acceptation.** Sections 1 et 7 extraites telles quelles : titre « (troisième tour) », « concept du troisième tour », « exactement la règle de la v2 », « Seuils : ceux de la v2 […] inchangés », « (seuils inchangés) », renvois « [v2 § n] », et, en section 1, la liste des défauts des tours précédents (« une phrase neutre plus raide, des majuscules d'un seul côté, un ton d'humeur d'un seul côté »). Un lecteur qui sait que le tour est le troisième, que la règle est « une sur sept » et qu'un « oui » à Q4 pèse seul peut régler ses réponses sur l'issue : c'est une atteinte au juge (R3), même sans changer une question. Remède, couples B-1a à B-1j : section 1 dite sans les défauts passés ; section 7 sans rang de tour ni renvoi à la v2 ; **la remise au lecteur s'arrête avant la section 7.3** (borne `### 7.3 `, présente une fois) ; le statut de Q6 sort de la question ; la commande du lecteur ne dit rien des tours. Simulé : après couples, la remise au lecteur ne contient plus « tour », « v2 », « inchangé », « échec », « non conforme » ni « 56 ». **Point à trancher par la mère** : les deux premiers lecteurs ont reçu la règle (toute la section 7 de la v2) ; la retirer change l'information du juge, dans le sens de l'aveugle seulement ; à déclarer en réserve 6 et en provenance. Si la mère garde la section 7.3 dans la remise par parité, B-1f, B-1g et B-1h tombent et il faut alors, au minimum, ôter de la section 7.3 « (seuils inchangés) », « — exactement la règle de la v2 [v2 § 7] — » et la ligne « Seuils ». **Résidu** : les noms de fichiers en `-v3` remis au lecteur ; sans remède simple, à déclarer.

### À corriger

- **A-1 — Clés des réponses et rapport du lecteur absents de sa remise.** `lire_reponses` refuse (code 2) toute entrée dont les clés ne sont pas exactement, dans l'ordre, celles de `CLES_REPONSE` ; la section 7.2 dit « clés fixes » sans les nommer, et le rapport du lecteur, décrit en [v2 § 7], n'est plus décrit. Couples A-1a, A-1b.
- **A-2 — Deux exemples contredisent la règle qu'ils illustrent.** Couples A-2a (ciseau à bois : « flat steel blade, a bevelled edge »), A-2b (« many thousands of years »), A-2c (note des jetons, rejouée).
- **A-3 — Annexe C à compléter** (le journal, point 6, le demande) : 39 entrées pour `chats`, 24 pour `geographie`, chacune vérifiée par programme disjointe de l'annexe A, de l'annexe B et de l'annexe C actuelle ; les quatre exemples passent encore C15. Couples A-3a, A-3b, A-3c. Les comptes du journal (132 et 34) deviennent 171 et 58.
- **A-4 — Deux règles dans un même dossier, non écrites pour le script.** (a) `amont_tour2` refuse une sélection « faite sous une autre consigne » : `selection-v1.json` porte l'empreinte de la v2, le script v3 celle de la v3 ; un développeur qui suit « sur le modèle de `amont_tour2` » écrit un refus certain en voie réelle, que les essais sur un jeu factice ne verront pas. (b) Le mode `assembler` rejoue C2 à C10 sur tout le fichier : « ne repassent pas C2 » ne dit ni que les paires gardées passent le C2 de la v2, ni ce qu'il en est de C9, C14 et C15. Un refus à l'assemblage est un code 2 au dernier pas du lot. Couples A-4a, A-4b, A-4c.
- **A-5 — Bloc `exemples`** : `lire_exemples` exige huit lignes, `E1` à `E8`, `N1` à `N8` ; la v3 en a quatre, `E9` à `E12`, `N5` à `N8`. Couple A-5.
- **A-6 — C6 sans statut** : absent de « ce qui ne change pas », absent de la table 6.1, et le titre du point 5 le dit « étendu ». Couples A-6a, A-6b, A-6c.
- **A-7 — 6.1 contre 9.1** : faute de la consigne trouvée avant toute phrase. Couple A-7.
- **A-8 — Accord au brouillon 21 de T0.7** : texte de R15, instant de fermeture, session de l'inscription. Couples A-8a, A-8b, A-8c.
- **A-9 — Second lecteur de Q4** : ni décompte ni journal nommés, clés des réponses non dites, et les paires de réserve « soumises à mesure » réécriraient les mêmes noms (R12). Couple A-9.
- **A-10 — C13 et C0** : rapport (b) non défini quand une moyenne est nulle (cas des exemples de `chats` : deux `the` contre zéro) ; aucune mesure des signes d'écriture ; « couverte » non défini. Couples A-10a, A-10b, A-10c.
- **A-11 — Taille de l'échantillon** : le v2 tire ⌈n / 10⌉ sur les paires prises (6 si n est de 56 à 60) ; la v3 écrit « 7 ». Garder le calcul du v2 laisse le juge inchangé. Couples B-1d (section 7.1), A-11 (section 6).

### Mineurs

- **M-1** — « for this round » dans la remise à l'écrivain. Couple M-1.
- **M-2** — La géographie perd les mots de météo par C7 ; le dire évite des renvois. Couple M-2.
- **M-3, M-4** — C14 n'arrête pas « par construction » les exemples de la v2 : cinq sur huit. Couples M-3, M-4.
- **Sans couple** : la liste fermée des mots de nombre de C13 n'a pas les pluriels (`thousands`, `hundreds`, `dozens`) ; l'en-tête « Statut » et la section 9, étape 1, sont à mettre à jour par la mère au scellement ; la remise à l'écrivain ne dit rien de l'équilibre des `the`, que C13 (b) mesure.

## Couples « texte actuel → texte corrigé »

Chaque « texte actuel » est recopié de la consigne et **vérifié par programme** : présent exactement le nombre de fois dit (une fois, sauf B-1e : quatre). Les 38 couples s'appliquent ensemble sans se gêner (appliqués en mémoire dans l'ordre ci-dessous ; la consigne corrigée garde ses marqueurs, ses cinq blocs et ses bornes, chacun une fois). Les fins de ligne dans un texte sont celles de la consigne.

### B-1a

Texte actuel :

````text
  registre, même naturel, mêmes longueurs, mêmes signes d'écriture. Une différence de surface constante d'un côté — une
  phrase neutre plus raide, des majuscules d'un seul côté, un ton d'humeur d'un seul côté — entre dans la direction ; or ces
  traits (raideur, noms propres, majuscules) se trouvent aussi dans les actions de l'agent, si bien qu'un témoin qui les
  porte peut passer son plancher **pour une autre raison que le sujet**, ce que le témoin doit précisément exclure.
````

Texte corrigé :

````text
  registre, même naturel, mêmes longueurs, mêmes signes d'écriture. Une différence de surface constante d'un côté (de
  style, d'écriture ou de ton) entre dans la direction ; or de tels traits se trouvent aussi dans les actions de l'agent,
  si bien qu'un témoin qui les porte peut passer son plancher **pour une autre raison que le sujet**, ce que le témoin
  doit précisément exclure.
````

### B-1b

Texte actuel :

````text
## 7. Contre-vérification à l'aveugle (troisième tour)
````

Texte corrigé :

````text
## 7. Contre-vérification à l'aveugle
````

### B-1c

Texte actuel :

````text
- **Quand** : après le second passage du script v3 (code 0 sur la sélection du troisième tour) et avant l'assemblage.
````

Texte corrigé :

````text
- **Quand** : après le second passage du script (code 0 sur la sélection du lot) et avant l'assemblage.
````

### B-1d

Texte actuel :

````text
- **Échantillon** : dans chaque concept du troisième tour, 7 paires de la sélection (⌈64 / 10⌉), tirées sans remise par
````

Texte corrigé :

````text
- **Échantillon** : dans chaque concept du lot, ⌈n / 10⌉ paires de la sélection de n paires (7 pour n = 64), tirées sans remise par
````

### B-1e (4 occurrences, toutes dans la section 1)

Texte actuel :

````text
 [v2 § 1]
````

Texte corrigé :

````text
(rien : le renvoi est ôté, l'espace qui le précède compris)
````

### B-1f

Texte actuel :

````text
`remise-au-lecteur-v3.md` (sections 1 et 7 de cette consigne, extraites par programme et scellées)
````

Texte corrigé :

````text
`remise-au-lecteur-v3.md` (sections 1, 7.1 et 7.2 de cette consigne, extraites par programme et scellées ; la section 7.3 — conformité, règle d'acceptation, seuils — ne lui est pas remise)
````

### B-1g

Texte actuel :

````text
`exemples-v3.jsonl`, `format-lecture-v3.json` et `remise-au-lecteur-v3.md`
     (sections 1 et 7, mêmes bornes que [v2 § 6]) ; chacun scellé.
````

Texte corrigé :

````text
`exemples-v3.jsonl`, `format-lecture-v3.json` et `remise-au-lecteur-v3.md`
     (à l'octet : de la ligne qui commence par `## 1. ` incluse à celle qui commence par `## 2. ` exclue, puis de `## 7. ` incluse à `### 7.3 ` exclue ; chaque borne présente une seule fois, sinon refus ; **écart au v2**, qui remettait toute la section 7 : la règle d'acceptation et ses seuils ne sont plus remis au lecteur) ; chacun scellé.
````

### B-1h

Texte actuel :

````text
- **Q6** (la paire ; **rapportée, hors de la conformité**) : l'une des deux phrases vous semble-t-elle écrite pour imiter
  l'autre (même charpente, mots remplacés un à un) ? `aucune` / `A` / `B`.
````

Texte corrigé :

````text
- **Q6** (la paire) : l'une des deux phrases vous semble-t-elle écrite pour imiter
  l'autre (même charpente, mots remplacés un à un) ? `aucune` / `A` / `B`.
````

### B-1i

Texte actuel :

````text
Q2 oui, Q3 non pour les deux, Q4 non pour les deux, Q5 oui pour les deux [v2 § 7]. Q6 n'y entre pas : elle est comptée
````

Texte corrigé :

````text
Q2 oui, Q3 non pour les deux, Q4 non pour les deux, Q5 oui pour les deux [v2 § 7]. Q6 n'y entre pas (rapportée, hors de la conformité ; cela n'est pas dit au lecteur) : elle est comptée
````

### B-1j

Texte actuel :

````text
5. **Contre-vérification** (section 7) ; second lecteur de Q4 s'il le faut ; en cas d'échec, section 9.1.
````

Texte corrigé :

````text
5. **Contre-vérification** (section 7) ; second lecteur de Q4 s'il le faut ; en cas d'échec, section 9.1. La commande qui lance un lecteur ne dit ni le rang du tour, ni l'existence de tours antérieurs, ni leurs décomptes, ni la règle d'acceptation ; elle est gardée et citée en provenance.
````

### A-1a

Texte actuel :

````text
Réponses dans `reponses-lecteur-v3.json`, une entrée par item, clés fixes ; une citation exigée pour tout « oui » à Q4.
````

Texte corrigé :

````text
Réponses dans `reponses-lecteur-v3.json` : un objet `{"items": [...]}`, une entrée par item, clés exactement et dans cet ordre : `item`, `Q1_A`, `Q1_B`, `Q2`, `Q3_A`, `Q3_B`, `Q4_A`, `citation_Q4_A`, `Q4_B`, `citation_Q4_B`, `Q5_A`, `Q5_B`, `Q6` ; valeurs : celles de chaque question ci-dessous ; `citation_Q4_A` et `citation_Q4_B` : pour un « oui » à Q4, le passage cité, recopié tel quel de la phrase ; pour un « non », `null`. Rapport du lecteur `rapport-contre-verification-v3.md` : son modèle, ses heures (par `date -u`), les fichiers reçus avec leurs empreintes, la déclaration « aucun fichier de P3-bis », ses constats.
````

### A-1b

Texte actuel :

````text
clés de réponse du v2 **plus `Q6`**
````

Texte corrigé :

````text
clés de réponse du v2, dans leur ordre, **plus `Q6`** en dernière clé
````

### A-2a

Texte actuel :

````text
"phrase_neutre": "A standard wood chisel has a flat steel blade, a bevelled edge and a handle made of ash or beech."
````

Texte corrigé :

````text
"phrase_neutre": "A spirit level is a straight bar of wood or metal fitted with a small glass tube of liquid and a bubble."
````

### A-2b

Texte actuel :

````text
"phrase_concept": "A fjord is a long, narrow inlet of the sea with steep sides, carved by a glacier over many thousands of years."
````

Texte corrigé :

````text
"phrase_concept": "A fjord is a long, narrow inlet of the sea with steep rocky sides, carved out slowly by a moving glacier."
````

### A-2c

Texte actuel :

````text
jetons 23/26, 21/23, 21/21, 26/26 (écart relatif maximal
0,115) ; 20 à 22 mots ;
````

Texte corrigé :

````text
jetons 23/23, 21/23, 21/21, 25/26 (écart relatif maximal
0,087) ; 20 à 22 mots ;
````

### A-3a

Texte actuel :

````text
clever, smart, lazy, active, vocal
````

Texte corrigé :

````text
clever, smart, lazy, active, vocal, persian, burmese, bengal, abyssinian, birman, manx, himalayan, angora, siberian, predator, predators, predatory, carnivore, carnivores, stalk, stalks, chase, chases, scratch, scratches, scratched, sharp, flea, fleas, neutered, spayed, vaccine, vaccines, allergy, allergies, allergic, vomit, vomits, restless, sleepy, sound, sounds, noise, noises
````

### A-3b

Texte actuel :

````text
barren, inhospitable, treacherous
````

Texte corrigé :

````text
barren, inhospitable, treacherous, hostile, desolate, bleak, uninhabited, forbidding, asian, european, african, american, australian, antarctic, indian, alps, andes, himalayas, sahara, nile, amazon, caribbean, baltic, siberia, scandinavia, greenland, iceland
````

### A-3c

Texte actuel :

````text
>     long-haired, short-haired; never a breed name that English writes with a capital letter: list C forbids siamese,
>     maine coon, ragdoll and sphynx), grooming and coat care, food and water, and the
````

Texte corrigé :

````text
>     long-haired, short-haired; never a breed name that English writes with a capital letter: list C forbids siamese,
>     maine coon, ragdoll, sphynx, persian and others), grooming and coat care, food and water, and the
````

### A-4a

Texte actuel :

````text
Les paires gardées de `meteo` et `sports` ne repassent pas C2.
````

Texte corrigé :

````text
Les paires gardées de `meteo` et `sports` ne passent jamais les contrôles neufs ou changés de la v3 (C2 changé, C9 étendu, C14, C15) : partout où le v2 les recontrôle (mode `assembler` : C2 à C10 sur les octets du fichier), elles passent **les contrôles du v2 tels quels** (C2 du v2 avec `MAJUSCULES_PERMISES`, C9 contre les seuls exemples de la v2) ; les paires de `chats` et `geographie` passent ceux de la v3. Sans cette séparation, une paire gardée qui porte `Celsius` ou `Olympic` ferait refuser l'assemblage (code 2).
````

### A-4b

Texte actuel :

````text
(71 chacun [D2]). Le script ne lit, des fichiers des deux
````

Texte corrigé :

````text
(71 chacun [D2]) ; `selection-v1.json` et les pièces des deux premiers tours ont été faites **sous la v2** : là où `amont_tour2` exigeait l'empreinte de la consigne courante (`sel["consigne"]["sha256"]`), `amont_tour3` exige `EMPREINTE_CONSIGNE_V2` pour les pièces des deux premiers tours et l'empreinte de cette consigne pour celles du troisième. Le script ne lit, des fichiers des deux
````

### A-4c

Texte actuel :

````text
entropie imposée** éprouvée de bout en bout sur un jeu factice ([cls2] D2-2) ;
````

Texte corrigé :

````text
entropie imposée** éprouvée de bout en bout sur un jeu factice dont l'amont porte l'empreinte de la v2 et dont une paire gardée porte une majuscule d'exception de la v2 (`Celsius`) ([cls2] D2-2) ;
````

### A-5

Texte actuel :

````text
identifiants d'exemples admis `E9` à `E12`.
````

Texte corrigé :

````text
bloc `exemples` de cette consigne : **quatre** lignes, indices `E9` à `E12`, domaines `N5` à `N8` dans cet ordre (`lire_exemples` du v2 exige huit lignes, `E1` à `E8`, `N1` à `N8` : gardé tel quel pour le bloc de la v2, lu pour C9).
````

### A-6a

Texte actuel :

````text
5. **C6 étendu → C15 (neuf)** :
````

Texte corrigé :

````text
5. **C15 (neuf ; C6 reste inchangé)** :
````

### A-6b

Texte actuel :

````text
- **Ce qui ne change pas** : C1 (hors le point 11), C3, **C4**, C5, C7, C8
````

Texte corrigé :

````text
- **Ce qui ne change pas** : C1 (hors le point 11), C3, **C4**, C5, C6, C7, C8
````

### A-6c

Texte actuel :

````text
essai atteste que C3, C4, C5, C7, C8, C10, C11 et C12 sont **identiques au caractère** à ceux du v2.
````

Texte corrigé :

````text
essai atteste que C3, C4, C5, C6, C7, C8, C10 et C12 sont **identiques au caractère** à ceux du v2, et C11 hors de ce que le point 16 et le point 4 changent à l'assemblage.
````

### A-7

Texte actuel :

````text
3) ; ou un refus du script (code 2) que la mère ne peut lever sans changer cette consigne.
````

Texte corrigé :

````text
3) ; ou, **une fois l'écrivain lancé**, un refus du script (code 2) que la mère ne peut lever sans changer cette consigne.
  Avant le lancement de l'écrivain (étapes 1 et 2), une faute de cette consigne (section 6.1 : un exemple en défaut, une annexe mal formée) se corrige par une version suivante, contre-lue sur ce seul point (R12) : aucune phrase n'existe, aucun tour n'est consommé.
````

### A-8a

Texte actuel :

````text
  réserve est déclarée dans T0.7, sa provenance et tout texte qui cite ses sondes (« plancher sémantique non mesuré : jeu
  des concepts refusé trois fois à la contre-vérification à l'aveugle »). Les fichiers de `meteo` et de `sports` restent
  versés, scellés et non employés.
````

Texte corrigé :

````text
  réserve **R15** de T0.7 s'applique dans les mots de T0.7 (« plancher sémantique non lu : jeu des phrases des concepts non scellé à l'ouverture (T7-P9 non lue) » ; brouillon 21, table des réserves) ; la provenance du jeu en dit la cause (« jeu
  des concepts refusé trois fois à la contre-vérification à l'aveugle »). Les fichiers de `meteo` et de `sports` restent
  versés, scellés et non employés.
````

### A-8b

Texte actuel :

````text
- **Échéance** : si la ligne `SCELLEMENT-CONCEPTS-T07` n'est pas écrite à l'ouverture de l'étape A, T0.7 suit le même
  repli, que le lot soit en cours ou non ; une ligne écrite après l'ouverture ne sert pas à cette étape (choix de cette
````

Texte corrigé :

````text
- **Échéance** : si la ligne `SCELLEMENT-CONCEPTS-T07` n'est pas inscrite **strictement avant l'instant de fermeture** que fixe T0.7 (première ligne `OUVERTURE-T07` de l'étape A du run, ou plus tôt selon sa règle G5), T0.7 suit le même
  repli (R15), que le lot soit en cours ou non ; une ligne inscrite après cet instant est exclue pour de bon sur ce lancement (choix de cette
````

### A-8c

Texte actuel :

````text
   code 0, `chats` et `geographie` sont acceptés au troisième tour et C12 passe ; la mère écrit alors
   `SCELLEMENT-CONCEPTS-T07`, avant l'ouverture de l'étape A, sans autre choix. Sinon, section 9.1.
````

Texte corrigé :

````text
   code 0, `chats` et `geographie` sont acceptés au troisième tour et C12 passe ; la mère écrit alors
   `SCELLEMENT-CONCEPTS-T07` dans la session où l'acceptation est prononcée, sans autre choix ; la ligne ne sert à T7-P9 que si elle précède strictement l'instant de fermeture de T0.7 (section 9.1, échéance). Sinon, section 9.1.
````

### A-9

Texte actuel :

````text
      sur une entropie neuve ; fichiers `echantillon-q4-<concept>-v3.json`, `cle-q4-<concept>-v3.json`) et mode
      `decompter-q4 --concept <c>` (réponses `reponses-q4-<concept>-v3.json` ; toute paire à « oui » retirée et remplacée
      par la réserve valide suivante, elle-même soumise au même lecteur ; plancher de la section 3).
````

Texte corrigé :

````text
      sur une entropie neuve ; fichiers `echantillon-q4-<concept>-v3.json`, `cle-q4-<concept>-v3.json` ; items `{item, phrase_A, phrase_B}`, place de la phrase du concept tirée, comme l'échantillon) et mode
      `decompter-q4 --concept <c>` (réponses `reponses-q4-<concept>-v3.json`, clés `item`, `Q4_A`, `citation_Q4_A`, `Q4_B`, `citation_Q4_B` ; décompte `decompte-q4-<concept>-v3.json` et `journal-decompte-q4-<concept>-v3.txt` ; toute paire à « oui » retirée et remplacée
      par la réserve valide suivante, elle-même soumise au même lecteur dans des fichiers de passage suivant, de mêmes noms suivis de `-p2`, `-p3`, … avant `.json` (R12 : aucun nom réécrit) ; plancher de la section 3).
````

### A-10a

Texte actuel :

````text
  9. **C13** (rapporté, réserves) : garder toutes les mesures du v2 ; en ajouter trois, par concept du troisième tour :
     (a) part des paires qui ont au moins une suite de **trois** mots en commun, **réserve si plus d'un quart** ;
     (b) moyenne par rôle du nombre de `the` par phrase, **réserve si l'une dépasse l'autre de plus de la moitié** (rapport
     au-dessus de 1,5) ; (c) moyenne par paire de la part de mots communs (taille de l'intersection des ensembles de mots
     sur celle de leur union), **réserve si au-dessus de 0,25**. Seuils sans étalonnage, fixés ici.
````

Texte corrigé :

````text
  9. **C13** (rapporté, réserves) : garder toutes les mesures du v2 ; en ajouter quatre, par concept du troisième tour :
     (a) part des paires qui ont au moins une suite de **trois** mots en commun, **réserve si plus d'un quart** ;
     (b) moyenne par rôle du nombre de `the` par phrase, **réserve si l'une dépasse l'autre de plus de la moitié** (rapport
     au-dessus de 1,5 ; réserve aussi si l'une est nulle et l'autre non) ; (c) moyenne par paire de la part de mots communs (taille de l'intersection des ensembles de mots
     sur celle de leur union), **réserve si au-dessus de 0,25** ; (d) moyenne par rôle, par phrase, du nombre de virgules, de traits d'union et d'apostrophes, chacun à part, **réserve selon la règle de (b)**. Seuils sans étalonnage, fixés ici.
````

### A-10b

Texte actuel :

````text
Seuils neufs (C14 : quatre mots ; C13 : un quart, 1,5, 0,25 ; C0 : huit entrées)
````

Texte corrigé :

````text
Seuils neufs (C14 : quatre mots ; C13 : un quart, 1,5 pour (b) et (d), 0,25 ; C0 : huit entrées)
````

### A-10c

Texte actuel :

````text
chaque concept du
     troisième tour garde **au moins huit entrées de noyau** qui ne sont pas couvertes par son annexe C
````

Texte corrigé :

````text
chaque concept du
     troisième tour garde **au moins huit entrées de noyau** qui ne sont pas couvertes par son annexe C (une entrée est couverte dès qu'une de ses formes est une entrée de l'annexe C)
````

### A-11

Texte actuel :

````text
12. **Échantillon** (`echantillon --tour 3`) : 7 paires par concept du troisième tour,
````

Texte corrigé :

````text
12. **Échantillon** (`echantillon --tour 3`) : ⌈n / 10⌉ paires par concept du troisième tour (7 pour n = 64, calcul du v2 inchangé),
````

### M-1

Texte actuel :

````text
extra forbidden words for this round
````

Texte corrigé :

````text
extra forbidden words for concept sentences
````

### M-2

Texte actuel :

````text
character, and list C forbids them in lower case. Never volcanoes
````

Texte corrigé :

````text
character, and list C forbids them in lower case. The weather words of list B (rain, snow, wind, climate, season and the like) are not available either: describe water, ice and dry land without them. Never volcanoes
````

### M-3

Texte actuel :

````text
sont plus un cas sain (ils échoueraient à C14 par construction)
````

Texte corrigé :

````text
sont plus un cas sain (cinq des huit, E1, E2, E3, E4 et E7, échouent à C14)
````

### M-4

Texte actuel :

````text
C3 (longueurs), C2 (majuscules, espaces), C14 (anti-calque), C13
````

Texte corrigé :

````text
C3 (longueurs), C2 (majuscules, espaces), C14 (anti-calque, partiel : trois des huit exemples calqués de la v2 n'ont aucune suite commune de quatre mots), C13
````

## Gestes déclarés, interdits tenus, refus

- **Lu** : interdits communs v2 (`1ee3b370…`, en entier, règle 9 comprise) ; la consigne v3 et son journal, en entier ; la v2 (`79f2c89c…`) hors de ses exemples, ceux-ci lus par programme seulement (mesures affichées, jamais leur texte) ; `registres/decisions.md`, lignes R-2125, R-2155, R-2158, R-2174 ; le script v2 par `git show` de la branche `prep/t07-concepts-script-v2` (commit `220c7c7f`, `a858c40c…`) dans le bloc-notes ; la contre-lecture du script v2 (`9d024078…`, lignes des constats D2) ; `temoins.py` l. 30-92, `empans.py` l. 36-64, `formats.py` l. 15-70 de `main` ; `sondes_neuves_v1.py` au commit `8dc1cb09` (l. 196-222, 328-374) ; le brouillon 21 de T0.7 par recherche de « R15 » et de la clé des concepts, neuf lignes lues.
- **Sous `donnees/t07-concepts-v1/`** : les deux journaux de décompte, par comptage de motifs (`grep -o`, aucune phrase affichée), et deux compagnons `.sha256` de décompte. **Jamais ouverts** : les rapports des lecteurs (la section 9 de la consigne les donne au contre-lecteur ; la commande de la mère m'interdit toute phrase du jeu, et leurs constats en citent : non lus, déclaré), les remises des écrivains, sélections, échantillons, clés, réponses, décomptes en JSON, `/home/user/lot3-concepts/remise-ecrivain*/` ; de `/home/user/lot3-concepts/`, le seul dossier `tokeniseur/`. Non lue : la contre-lecture de la v1.
- **Jamais ouverts** : tout `lecture-sondes-t06.json` ; les branches interdites ; tout `diag/` et `runs/` de 7a ; `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`, `registres/index-bras-attaque*` ; l'étiqueteur ; `scripts/extraire_mesures_epreuve_t06_v1.py` ; les textes d'actions de P3 ; tout fichier de P3-bis. Aucune recherche récursive ; aucun `env`, `printenv`, `set`, `export -p`, `/proc/*/environ` ; aucun appel externe, aucune dépense ; aucune écriture git ; suite d'essais non lancée.
- **Écrits** : ce fichier et son compagnon `.sha256` ; scripts de rejeu et consigne corrigée simulée dans le bloc-notes de la session, hors du dépôt.
- **Refus rencontrés** : aucun.
