# Traitement de la relecture courte, partie chaîne — chaîne de P3 v1, brouillon 3

- Constats traités : `prereg/contre-lectures/P3-premier-test-v1-relecture-courte-chaine-v1.md`
  (`dd9841f0f2e3342b2734417fecd44d75fd66b128e96272139176b509ff992069`), RCh-01 à RCh-09 ; pour la part de la chaîne,
  `prereg/contre-lectures/P3-premier-test-v1-relecture-courte-texte-v1.md`
  (`c685659a120f7071e707503d16b978fa9830562fcf49b6d910a53d7b8c50e57a`), RT-01, RT-05, RT-07 et RT-15. Décisions de la
  session appliquées telles quelles (R-218, décision (1) ; consigne de la session, points 1 à 6).
- Chaîne traitée : `brouillons/P3-chaine-v1-brouillon3/`, les treize scripts du brouillon 2
  (`brouillons/P3-chaine-v1-brouillon2/`, scellé au commit `03cb538`, gardé tel quel, R12), changés là où ce tableau le dit.
  Les chemins sans dossier désignent ce dossier ; les numéros de ligne sont ceux du brouillon 3.
- Inchangés, octet pour octet : `surveiller_p3_v1.sh`, `controle_cinq_minutes_p3_v1.sh`, `repetition_finale_p3_v1.sh`,
  `essais_surveillance_p3_v1.sh`.
- Rédaction : le rédacteur du brouillon 2 de la chaîne (routine sur processeur). Ce fichier n'est pas une
  contre-lecture : la relecture de l'écart (candidat 1 au candidat 2, code, chaîne) reste à faire par un sous-agent neuf
  (R-218, décision (4)).

## Constats

| constat | gravité | sort | où | comment |
|---|---|---|---|---|
| RCh-01 : la recherche en texte libre lit R-215 comme une révocation de R-192 | bloquant | corrigé (point 1) | `verifications_p3_v1.py` l. 7-15, 44, 47-50, 73-74, 81-105 ; bancs : `essais_lanceur_p3_v1.sh` l. 308-332 (G06b, G07, G07c à G07f), `essais_controles_p3_v1.sh` l. 121-123 (A04b), 131 (A08b), 313-325 (G06, G08 à G14), `essais_scellement_p3_v1.sh` l. 189-197 (S09e, S09f) | Plus aucune recherche en texte libre. Une révocation est, et n'est que : (a) une ligne du registre des GO à huit colonnes, de type « révocation », dont le périmètre (quatrième colonne) nomme R-192 ou GO-2026-10-04-08, identifiants entiers ; (b) une ligne du registre des décisions dont la cellule de décision commence exactement par `**Révocation de R-192**` (constante `PREFIXE_REVOCATION`). Cas sains : la ligne R-215 tirée du registre réel (G07c, G08), « aucune révocation de R-192 » (G07d, G09, S09f), un texte libre qui révoque sans la forme (G07e), la forme ailleurs qu'en tête de la cellule (G07f, G11), des identifiants voisins (G13). Artefacts : chaque forme exacte, refusée (G06b, G07, G10, G12, A08b, S09d, S09e). Sur les registres de la tête `bc05768` (lignes R-215 et R-218 comprises), `go` rend « GO-2026-10-04-08 (R-192) conforme », code 0. R-215 n'est pas réécrite. |
| RCh-02 : des révocations formulées autrement passent | mineur | corrigé (point 1) | mêmes lignes que RCh-01 | Le texte ne promet plus que la chaîne voie un sens : il écrit les deux formes mot pour mot et « rien d'autre » ; le bloc 9 relie la forme (b) du module au texte (ci-dessous, A44j, A44m). Les cinq formulations du constat ne sont plus des révocations, par définition écrite au texte. |
| RCh-03 : l'accord est reconnu à trois mots, R-208, R-215 et R-217 passent | mineur | corrigé (point 2) | `verifications_p3_v1.py` l. 16-20, 50, 120-123 ; `controles_avant_depense_p3_v1.sh` l. 260-264, 270-271 (bloc 9) ; bancs : `essais_lanceur_p3_v1.sh` l. 126 (ligne saine), 350-356 (A12, A12b), `essais_controles_p3_v1.sh` l. 252, 254 (A44k, A44m) | La ligne du jour doit avoir une cellule de décision qui commence exactement par `**Accord de Lazar pour le lancement de P3**` (constante `PREFIXE_ACCORD`) ; le lanceur garde l'argument ACCORD (inchangé). Artefact A12 : ligne du jour qui mentionne « accord de Lazar », « P3 » et « lancement » sans la forme (comme R-208, R-215, R-217), refusée ; A12b : la forme ailleurs qu'en tête, refusée. Appel direct : `accord R-208`, `R-215`, `R-217` au 2026-10-19 sur le registre réel, refusés. |
| RCh-04 : prix du stockage non borné ; crédit | mineur | (a) corrigé (point 3) ; (b) sans changement de la chaîne (point 3) | `lancer_p3_v1.sh` l. 18-21, 49, 63, 144-146, 154-157, 192, 200, 207 ; `controles_avant_depense_p3_v1.sh` l. 24-26, 258-259, 270-271, 290 (bloc 9) ; bancs : `essais_lanceur_p3_v1.sh` l. 90-93, 225-227 (P07l à P07n), 256-260 (Z03), 447-449, 488-490 (O16 à O18), `essais_controles_p3_v1.sh` l. 249-250, 253 (A44h, A44i, A44l) | (a) `STOCKAGE_MAX=0.03` : le filtre exige `storage_total_cost` fini, positif ou nul, au plus 0,03 USD de l'heure ; une borne non fixée arrête le lanceur (code 2) ; le bloc 9 relie la constante à la forme « stockage au plus 0,03 USD de l'heure » du texte. Offres plus chères au stockage, négatives ou illisibles : écartées (P07l, P07m, O16 à O18) ; offre au plafond juste : prise (P07n). (b) Le crédit exigé reste 6,5 heures × prix + 1,2 USD ; le texte nomme la recharge automatique (candidat 2). Au plafond, 72 heures de disque coûtent au plus 2,16 USD. |
| RCh-05 : « et leur ligne H » | mineur | sans changement de la chaîne (point 5) | `controles_avant_depense_p3_v1.sh` l. 50 (H inchangée : le vrai bloc-notes `…/p3-v1`) | Au versement, seules changent les valeurs `A_EPINGLER` des contrôles. La phrase du texte relève du candidat 2. Dans les bancs, la copie d'essai des contrôles change H (bloc-notes des bancs) et la copie jouée de la répétition jouet change H : essai seulement, déclaré (section « Épreuves »). |
| RCh-06 : champ de la relecture courte à remplir ; crochet | mineur | hors chaîne (texte, candidat 2) ; garde de la chaîne éprouvée | `sceller_p3_v1.sh` l. 106-118 ; `controles_avant_depense_p3_v1.sh` l. 186-196 (inchangés) | La chaîne exige déjà que chaque fichier `P3-premier-test-v1-*` suivi sous `prereg/contre-lectures/` soit épinglé et cité « `chemin` (`empreinte`) ». La tête porte les trois rapports de la relecture courte (R-218) : au versement, `RAPPORTS_ATTENDUS` nomme cinq paires et le candidat 2 cite les trois nouveaux rapports. Éprouvé : l'essai C3 (deux rapports épinglés et cités) rend 29 cas non conformes au banc du scellement, tous par « rapports présents … ≠ épinglés » ; l'essai C3b (cinq) rend 0. |
| RCh-07 : textes d'action échappés en JSON ; texte dégénéré | pour information | corrigé (point 4) ; « hors tableaux npz » : texte | `recuperation_p3_v1.sh` l. 3-6, 23-24, 302-319, 338, 344-347 ; `repetition_jouet_p3_v1.sh` l. 3-5, 30, 33-36, 43-45, 289-310, 353, 364-366, 395-397 ; `verifications_p3_v1.py` l. 21-27, 132, 145, 178-179 ; banc : `essais_controles_p3_v1.sh` l. 360-362 (M17, M19, M20) | Dans `parcourir()`, chaque chaîne JSON décodée est comparée aux fenêtres (compte par fichier, KO 4f) ; les fenêtres d'un seul caractère répété sont ignorées, et leur nombre est écrit. Répétition jouet : w-v1 = texte d'action de 80 points, une trace porte 48 points de suite (assertion), code 0 ; x-v1 = texte de 115 caractères sur deux lignes recopié dans le résumé du run, rescellé, KO 4f seul. Le module attend quatre récupérations conformes, une des traces seules et dix-huit artefacts. |
| RCh-08 : liste d'arrêt de la création ; instances « rr- » | pour information | hors chaîne (texte, candidat 2) | `lancer_p3_v1.sh` l. 24, 48, 192, 230 ; `controle_cinq_minutes_p3_v1.sh` (inchangés) | La chaîne refuse déjà la création au-dessus de la borne de téléchargement (P07h, P07j, O14, O15), rend le KO du contrôle à cinq minutes (C00 à C19) et ne tolère les instances « rr- » que nommées en argument (V01 à V08). Le texte se complète au candidat 2. |
| RCh-09 : destruction « rendue à Lazar (R-213) » dépassée par R-214 | pour information | noté, sans changement | `brouillons/P3-chaine-v1-brouillon2/traitement-CH-v1.md` l. 37 (scellé, gardé tel quel, R12) ; `lancer_p3_v1.sh` l. 59 | Le fait est consigné ici. `ARRETEES_TOLEREES` reste tel quel, sans effet (R-215, point (3)). |
| RT-01 : la révocation est cherchée en mots | bloquant | corrigé (point 1) | comme RCh-01 | Même traitement. « Aucune révocation de R-192 » est saine (G07d, G09, S09f). Les deux vraies révocations de l'essai du relecteur ne sont plus des révocations, sauf à prendre une forme exacte. La phrase « les copies versées ne diffèrent du brouillon 2 que par… » relève du candidat 2 : au versement, les copies du brouillon 3 ne diffèrent que par les valeurs `A_EPINGLER` des contrôles. |
| RT-05 : « ≈ 20 Go relevés », « au plus ≈ 11,2 USD » ; recharge non écrite | mineur | stockage borné (point 3) ; le reste : texte | comme RCh-04 | Borne au filtre, citée par le texte, reliée par le bloc 9. « Estimés », « dépense estimée » et la recharge automatique relèvent du candidat 2. |
| RT-07 : la liste « aucune création » omet deux conditions | mineur | hors chaîne (texte, candidat 2) | `lancer_p3_v1.sh` l. 63, 192 ; `verifications_p3_v1.py` l. 81-105 | La chaîne refuse déjà la création dans les deux cas, et dans le troisième, nouveau : téléchargement au-dessus de 0,05 USD par Go (code 3, P07h, P07j) ; stockage au-dessus de 0,03 USD de l'heure (code 3, P07l, P07m) ; révocation de R-192 (code 2, G06b, G07). |
| RT-15 : deux déclencheurs de destruction | pour information | hors chaîne (texte) ; question | `lancer_p3_v1.sh` l. 306 (ligne « instance : » de `lancement.txt`) ; `essais_lanceur_p3_v1.sh` l. 200 | La chaîne ne détruit rien. La ligne de `lancement.txt` reprend « gardée arrêtée jusqu'au verdict, 72 heures au plus, puis détruite par son identifiant (R10 ; texte, Plan d'analyse, point 1.6) » ; le banc vérifie « 72 heures au plus ». Si le candidat 2 garde une autre règle, cette ligne est à aligner (question ci-dessous). |

## Changements hors constats

- En-têtes des scripts changés : « brouillon 3 », constats traités.
- Points fixés par la session (point 5) : `TELECHARGEMENT_MAX=0.05` (`lancer_p3_v1.sh` l. 48) ;
  `CANDIDAT_RELU_CHEMIN=brouillons/P3-premier-test-i-a-v1-candidat2.md` (`controles_avant_depense_p3_v1.sh` l. 40) ; ligne
  de session du commit de scellement : `Claude-Session: https://claude.ai/code/session_015nCKHP3BPpJMpwY6zAEA4r`
  (`sceller_p3_v1.sh` l. 185). Le cas Z02 du banc du lanceur joue toujours une copie dont la borne est `A_FIXER`.
- Conséquence du point 1, à relire : `DECISION = "R-192"` (`verifications_p3_v1.py` l. 44, 73-74). Les formes de
  révocation sont fixées pour R-192 ; un texte qui citerait une autre décision rendrait la forme (b) sans objet. Le module
  refuse donc toute autre décision citée (G14).
- Conséquences du point 1 sur deux cas anciens : A04b (ligne de révocation mal formée) rend un seul KO, celui de la garde
  de calcul sur le registre de S (le module ne lit plus que des lignes à huit colonnes ; il en rendait deux au
  brouillon 2) ; G06 du module (révocation d'un autre GO qui nomme R-192 dans son périmètre) devient refusée, comme le
  veut la forme (a), qui ne fait pas d'exception.

## Épreuves

Bancs rejoués sur un commit d'essai, dans un dépôt jetable du bloc-notes des bancs
(`/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/p3-v1-brouillon3/`, appelé B3 ci-dessous ;
jamais poussé, sans adresse distante). Ce dépôt est un clone de la tête du dépôt de travail `bc05768`, dont l'arbre gelé
est égal au code relu `03cb538`. Il porte :
- un candidat d'essai : le candidat 1 de la session (`8070b640…`), plus les formes exactes des points 1 à 3
  (« **Révocation de R-192** », « **Accord de Lazar pour le lancement de P3** », « stockage au plus 0,03 USD de
  l'heure »), une phrase sur la recharge automatique et la citation des rapports de la relecture courte ;
- les copies versées des treize scripts du brouillon 3. Seules lignes changées : les six épingles des contrôles et leur
  ligne H, qui pointe vers B3 (essai seulement) ;
- un journal synthétique de la répétition jouet, pour les bancs des contrôles et du scellement.

Deux commits d'essai :
- C3 = `910e6863…`, deux rapports épinglés et cités. Le banc du scellement (passage 1) rend 29 cas non conformes, tous
  par « rapports présents … ≠ épinglés ». La tête porte en effet les trois rapports de la relecture courte (R-218). C'est
  un défaut de l'essai, pas de la chaîne : la garde de RCh-06 joue.
- C3b = `c757625f…`, cinq rapports épinglés et cités. Les bancs suivants tournent sur C3b.

| banc | journal (dans B3) | empreinte | dernière ligne | cas | durée |
|---|---|---|---|---|---|
| surveillance et contrôle à cinq minutes | `banc-surveillance-p3-v1.log` | `5f2fe1471a25d34945ec309d4de8f253a0ead08e84a96a644c9158ca99397ef2` | FIN DU BANC DE LA SURVEILLANCE DE P3 ; cas non conformes : 0 | 36 | 5 s |
| lanceur | `banc-lanceur-p3-v1.log` | `235ba4d1c188d0460734dce036a3ecc86a2ed1f9825f2c4c9316c95f1d008230` | FIN DU BANC DU LANCEUR DE P3 ; cas non conformes : 0 | 125 (113 au brouillon 2) | 57 s |
| scellement, passage 1 (C3) | `banc-scellement-p3-v1.log` | `02d792319a81e800b594444288610eacd85b7b93a64b9e9f1c8c572e6daafa2d` | FIN DU BANC DU SCELLEMENT DE P3 ; cas non conformes : 29 | 65 | 57 s |
| scellement, passage 2 (C3b) | `banc-scellement-p3-v1-passage2.log` | `96fc7f7e062d2e6df379922e19761d4c2ab30fbebe5b26edb2c6732185ed7b25` | FIN DU BANC DU SCELLEMENT DE P3 ; cas non conformes : 0 | 65 (63) | 134 s |
| contrôles, vrai tokeniseur compris (C3b) | `banc-controles-p3-v1.log` | `060372f85d19904006ba6940421523d78cee765e3abb14de2a9764504f1dccff` | FIN DU BANC DES CONTRÔLES DE P3 ; cas non conformes : 0 | 150 (135) | 2 101 s |
| répétition jouet (code `03cb538`, candidat d'essai de C3b) | `repetition-jouet-p3-v1-essai.log` | `6bd7bbed4fc79a38e7f74d6eb90ebc950f3c2ab71339e8986996c56dbe3e8fed` | FIN DE LA RÉPÉTITION | 3 passages, 23 récupérations | 3 520 s |

- Cas sains des contrôles et du scellement (A00, S00) : ils lisent les registres réels de la tête, lignes R-215 et R-218
  comprises, et sont conformes. Le cas B00 (vrai tokeniseur) rend 52 OK : trois de plus qu'au brouillon 2, un par
  rapport épinglé en plus.
- `verifications_p3_v1.py preuves` sur les quatre journaux conformes rend le code 0. Chaque script éprouvé est égal au
  brouillon 3, sauf la copie d'essai des contrôles (`7fdd5909…`) : six épingles et la ligne H.
- Répétition jouet : passages 1-sain (code 0, 2 694 s), 2-artefact-branche-presente (code 2), 3-manque (code 1). Elle a
  tourné en même temps que le banc des contrôles pendant ses 35 premières minutes ; la suite des tests de l'instance
  jouet y a pris 1 635 s. Mémoire résidente maximale relevée : 1 992 Mo.
- Récupérations : quatre conformes (passage-1-sain, arret-synthetique-episodes, gardes-reelles, texte-degenere-repete,
  « 1 fenêtre(s) d'un seul caractère répété ignorée(s) »), une des traces seules (code 4), et dix-huit artefacts à un
  seul KO, au préfixe attendu. Le nouvel artefact-texte-echappe-dans-un-resultat rend « KO 4f », trouvé seulement
  « dans les chaînes JSON décodées {'resume.json': 1} ». `verifications_p3_v1.py repetition` sur ce journal rend le
  code 0.
- La copie jouée de la répétition jouet ne change que sa ligne H (vers B3 : essai seulement). Le journal la nomme donc
  sous son empreinte propre (`f1a8e96c…`), et non sous celle du brouillon 3 (`ad38e1e3…`). La récupération est nommée
  sous l'empreinte du brouillon 3 (`ca67baff…`).
- Pour information : au run jouet, aucun texte d'action n'atteint 64 caractères. Le contrôle 4f du cas sain cherche
  donc zéro texte ; seuls les cas n-v1, x-v1 et w-v1 y mettent un texte long. Il en allait de même au brouillon 2.
- Pour libérer le disque pendant les bancs, ont été retirés les dépôts jetables de C3 et des essais C et C2 du
  brouillon 2. Leurs journaux et leurs fichiers `essai-C*.txt` sont gardés.

## Questions

- RT-15 : la ligne « instance : » de `lancement.txt` (`lancer_p3_v1.sh` l. 306) suit la règle actuelle du texte. Si le
  candidat 2 fixe une autre règle de destruction, faut-il un brouillon 4 pour cette seule ligne, ou la phrase du texte
  s'aligne-t-elle sur celle-ci ?
