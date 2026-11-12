# Contre-lecture 4 (R2, N-052) — préenregistrement de P3-bis, brouillon 11 — v1

- **Rôle** : contre-lecteur neuf au sens de R2, sous-agent de la session mère qui a repris le 2026-11-10 (R-2191). Je n'ai écrit ni P3-bis, ni ses brouillons, ni son code, ni sa chaîne, ni ses contre-lectures 1 à 3, ni les contre-lectures de son code. **Je n'ai lu aucun fichier de T0.7** (interdit de ma consigne).
- **Modèle** : Claude Fable 5.2 (`claude-fable-5-2`), autre modèle que le rédacteur du brouillon 11 (Claude Opus 5.5).
- **Heures** (relevées par `date -u`, le 2026-11-10) : début 11:38:16 UTC ; rapport écrit à 11:52:59 UTC.
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-contre-lecture-4-p3bis-brouillon11-v1.md` (`8c17493782162173050fedb12f56c0181d8604b37740c0ddeb8adfe94fc73f53`, égale à son compagnon), interdits communs v2 recopiés.
- **Texte relu** : `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon11.md` (`409c37ed4aa4f149565d8b0a45ae94c16b572f35967f080a0df629985549b290`, égale à son compagnon), lu en entier (1 949 lignes).
- **Lu aussi, empreintes recalculées, égales aux compagnons** : couples du brouillon 11 (`52074c5da7a3e287ce3a59ff2ff952c19ab02630599f0c0f0589de2b3399cfbb`), script (`1015bd16222041a0ede8b0cfca0e9c7edd7bbaf0f819c5ee949e53cda1700862`, non rejoué : il écrit le brouillon), journal (`b75a9708488ec0eee729e115d4c74553e031a6c58db4ed080488772811221952`) ; brouillons 6, 9 et 10 (sections gelées comparées par programme) ; contre-lecture 1 (`8399dc55ae358712ca97b4cffa5f79d98e45207ad25494b8abc01c98b7921ae0`), contre-lecture 2 (`f12d7f211f0b1b92eb1a59ec543442d2d79aaa9e476507ec8a8b9ec408d4ef0e`), contre-lecture 3 (`4c3cb62831a42f8e02e632ea1c7d111f94bb24b9ad066ace9e1ccfe148fde622`), entières ; contre-lecture différentielle du code `a1de3915` (`845c4de54e72207a320edf089c606bacf0cd87837d473ab654de48c3ddc839c9`, entière) ; contre-lecture différentielle du code v2 et de la chaîne (`011942534477d65627b961f09e814c2fe0693d44b7d525633466fd4a918c00d9`, table des constats CD) ; table des noms communs (`766992f4ea5eea8b5e319fd315e2ea0cb646c8f0e0400bf32a2bf5fdcb83d06a`) ; décision N-066 (`21e83ed58c7498c65b7f9ae78613bc38301acdf0dd15a9890af13e6c0edbd351`) ; `registres/go.md` (`9733d45c318f46326aabc4bdc81eb496153f2291b2f1c81e1cef90cb7a815836` à ma lecture ; l. 217, 292 à 299) ; `registres/decisions.md`, lignes R-799, R-2099, R-2103, R-2104, R-2113, R-2130, R-2131, R-2133, R-2153, R-2157, R-2158, R-2165 à R-2170, et en tête R-2177, R-2182, R-2191 ; `registres/scellements-v1.md` (quatre lignes) ; rapports du lanceur v1, complément v1 et v2 (`748568cb…`, `59e1da14…`, `06ea31cf…`, passages cités) ; `puissance-p3-bis-v2.txt` (`1df8311f…`) ; `src/controle_ia/prereg.py` (entier).
- **Code lu, au commit `a1de39151ebae29138a389829751397074239615`, par `git show`** : `src/controle_ia/premier_test_ia/ouverture_p3bis_v2.py` (`1361382e669f26d5568c81044e160c7fc122f4264832ffb70ec8d9b4714d2a13` ; constantes, journal, registres, `garde_ouverture`, `ouvrir`, `exposer_issue`, ligne de commande) ; chaîne `docs/procedures/P3-bis-temoin-positif-v1/` : `verifications_p3bis_v1.py` (en-tête, constantes, `go`, `valeurs`, `constantes`), `sceller_p3bis_v1.sh` (entier), `controles_avant_depense_p3bis_v1.sh` (épingles, extraction, blocs 8 à 14), `repetition_finale_p3bis_v1.sh`, `lancer_p3bis_v1.sh` et `recuperation_p3bis_v1.sh` (constantes et épingles) ; `harnais/validation_reelle.py` l. 66-76 ; `scellement.py` (`verifier_arbre`).
- **Essais ciblés, sur processeur, dans mon bac à sable** (`/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/contre-lecteur-4-p3bis/`) : identité avec P3 et vingt et une empreintes du code recalculées ; les 47 couples réappliqués en mémoire au brouillon 10 ; `prereg.problemes` ; sous-commandes `go` et `valeurs` de la chaîne sur le brouillon 11 ; dix-huit sondes de `garde_ouverture` et du format du journal sur des registres fabriqués (module `1361382e…` monté seul avec `gardes.py` et `scellement.py` du même commit) ; `verifier_arbre` sur le seul dossier de l'empreinte orpheline (CL4-08) ; mes dix-sept couples appliqués à une copie de travail, non versée.

## Verdict

**Scellable après corrections** : dix-sept couples (CL4-C01 à CL4-C17, liste exacte en fin de rapport), dont cinq dans des sections gelées (« Plan d'analyse », point 8 ; « Liste d'arrêt »), qui ne changent ni hypothèse, ni prédiction, ni signe, ni métrique, ni seuil, ni critère de lecture, ni aucun code.

Le fond tient : R1 est complet, les sections gelées « Hypothèse », « Prédiction », « Seuil » sont égales à l'octet au brouillon 6 (le dernier contre-lu), « Métrique » et « Critères » n'en diffèrent que par les changements déclarés, et le texte dit ce que fait le code `a1de3915` sur D-1 à D-4, la voie normale et les trois décisions du rendez-vous, à quatre précisions près (CL4-02 à CL4-05).

**Mais le candidat n'est pas atteignable en l'état, pour quatre raisons de procédure hors du texte** : le registre des GO de `main` est refusé en entier par la chaîne et par la garde de calcul (CL4-07) ; la lignée du code porte une empreinte orpheline qui fait refuser le scellement après le commit local de S (CL4-08) ; la machine de la session n'a que 713 316 ko libres pour 12 692 612 exigés (CL4-06) ; la branche de la chaîne (`614fd5da`, `8ad29273`) n'est pas dans ce clone (CL4-11).

## Ce que j'ai vérifié et trouvé juste

- **R1** : hypothèses H-B1 (décisive), H-B2, H-B3 ; prédictions chiffrées et signées PB-1 à PB-15 ; métrique ; seuils ; plan en onze points ; table gelée à cinq lignes avec phrases gelées, réserves et fichier d'issue ; liste d'arrêt. `prereg.problemes` rend exactement deux lignes : contre-lecture 4 sans ses deux empreintes, six marqueurs.
- **Écart du 10 au 11** : brouillon 10 (`9038a015…`) plus les 47 couples, chacun trouvé une fois, donne le brouillon 11 à l'octet (`409c37ed…`) ; seules « Plan d'analyse » et « Liste d'arrêt » changent parmi les sections gelées, comme la table l'annonce. **Écart du 6 au 11** : « Hypothèse », « Prédiction » et « Seuil » identiques ; « Métrique » : une ligne (l. 43-45 → 44-46) ; « Critères » : ligne 1 (borne, instances) et formule de l'affichage ; plan et liste d'arrêt : zones annoncées par les tables des brouillons 7 à 11.
- **Marqueurs remplis, contre `git`** : `a1de3915` existe, descend de `02217f1c` ; de `02217f1c` à `a1de3915`, `src`, `tests`, `scripts`, `requirements-*` et `.claude` ne changent que par les huit chemins cités ; identité avec P3 : quatorze lignes, toutes `A`, empreinte de la sortie `65a09fb52ab479a69b109859899efa95c8b92966e0fa2c5d8e70002e8d0c7708` ; les vingt et une empreintes du code citées sont celles des fichiers à ce commit ; les six pièces du brouillon sont sur `main` aux empreintes citées (les six recalculées par moi : `7d35576d…`, `8ab04d54…`, `c9d0b6c3…`, `1df8311f…`, `8399dc55…`, `2c55346b…`).
- **Code contre texte, plan, point 8** : en-tête du journal, clés, modes, dix-sept codes de refus dans l'ordre du texte ; prédicat (i) à (viii) à la lettre de `lire_ligne_journal` et `exiger_format_journal`, sauf les fins de ligne (CL4-02) ; fichier vide hors format et jamais remis à zéro ; horloge en arrière refusée sans ligne, avant toute lecture des registres, date égale permise ; clé `RENDEZ-VOUS-P3BIS-[1-9][0-9]*` ; `pleine-anticipee` refusée dès que `SCORES-T07` et `SONDES-T07` sont conformes, après les contrôles du journal, des écrits, de la garde et de la suite des décisions (sondes S4b) ; `reduite` permise sous « ouvrir » avec la garde en vigueur (S6d) ; voie normale ouverte sous « maintenir » et sous « ouvrir » sans garde (S2, S5d) ; « ouvrir pleinement » admise en première décision (S4) ; fichier d'issue à quatre clés, accord avec l'issue mécanique exigé par `exposer-issue`.
- **Borne de création** : `BORNE_CREATION=2026-11-18` au lanceur et au module commun, en plus de l'échéance du GO ; rejouée par moi sur une copie du registre sans les trois lignes fautives : le 10 et le 18 acceptés, le 19 et le 23 refusés par la borne, le 9 et le 24 par la validité du GO. Le texte la porte à l'en-tête, aux critères (ligne 1), à la liste d'arrêt (création, relance) et aux décisions ; 36 heures avant le rendez-vous, exact.
- **GO** : ligne GO-2026-11-10-02 de `registres/go.md` (l. 292) égale à ce que cite l'en-tête (octroi, plafond mot pour mot, échéance) ; aucune révocation qui la nomme ; une seule ligne « - GO : » et une seule ligne « - Lancement : » ; N-066 conforme à ce que le texte en dit.
- **Formes lues par la chaîne** : `valeurs` rend 19 sur 19 ; les huit intitulés une fois chacun ; treize épingles `A_EPINGLER` aux contrôles et une à la récupération, comme P-5 ; `registres/`, `docs/`, `brouillons/` et `prereg/` sont hors de `CHEMINS_GELES` (douze motifs), donc P-3 est faisable.
- **Chiffres (R6)** : 0,0287 et 0,0137 recalculés par la formule ; 0,6389, 0,6585, 0,7124, 0,7624, 0,1415, 0,3965 lus dans `puissance-p3-bis-v2.txt` ; 16 783 360 = 1 639 × 10 240, corps de 16 780 800 octets, longueur maximale 16 780 792 ; devis (19,95 ; ≈ 22 ; ≈ 9,5 ; ≈ 41 ; ≈ 38 h ; ≈ 1,9 USD par jour) ; ≈ 47,7 Mo ; 12 692 612 = 11 644 036 + 1 048 576 ko ; 531 = 436 + 95 ; 389 = 144 + 58 + 99 + 46 + 42.
- **R5** : les gardes neuves ont un cas sain et un artefact d'après les deux contre-lectures du code (`01194253…`, `845c4de5…`, table « Points demandés ») et mes sondes ; je n'ai pas rejoué les suites d'essais (règle 5 ; 0,7 Go libres).
- **Contre-lectures 1 à 3** : les points de la contre-lecture 1 (B1, I1 à I10, M1 à M9) se retrouvent dans le texte, à la lecture ; M10 et M11 dits ; D1 à D11 de la contre-lecture 2 et D1 à D6 de la contre-lecture 3 traités aux endroits que les tables annoncent (16 777 216 ne reste que dans les deux tables d'historique). CD-01 à CD-06 et CD-09 de la contre-lecture différentielle traités ou portés aux préalables ; CD-07 en partie (CL4-10) ; CD-08 non porté (CL4-15).

## Constats

| # | gravité | lieu | constat et preuve | correction |
|---|---|---|---|---|
| CL4-01 | **bloquant pour le scellement** (texte périmé) | en-tête l. 24 et 231 ; table l. 439 ; code, point 2, l. 1437 ; P-7 l. 1654 ; marqueurs l. 1940 (et l. 1923-1924, « sous réserve ») | Le texte dit six fois que la contre-lecture différentielle courte de `a1de3915` est « en cours ». Elle est rendue depuis 10:40 UTC (R-2158) : `contre-lecture-differentielle-code-a1de3915-v1.md` (`845c4de5…`), « citable au scellement », six constats mineurs dont C-1 à C-3 « à porter au brouillon 11 ». Le rapport n'est pas cité, alors que P-5 et le bloc 14 des contrôles exigent chaque rapport cité par son chemin et son empreinte. C-3 est porté ; C-1 et C-2 ne le sont pas (CL4-02, CL4-03). R-2167 dit déjà « contre-lu, R-2158 » : registre et texte divergent. | CL4-C01 à CL4-C04 ; les mentions d'historique (l. 24, 439, 1923-1924) restent, le statut du candidat les date. |
| CL4-02 | à corriger (section gelée) | plan, point 8, prédicat, l. 1084 ; P-9 | « fins de ligne CRLF lues comme LF » est inexact : le retour chariot seul et les fins de ligne mêlées sont lus de même (sonde S1 : quatre formes au format ; C-1 de `845c4de5…`). Ce prédicat est le contrat commun avec le lecteur de T0.7 : il doit être exact. | CL4-C05, CL4-C06 |
| CL4-03 | à corriger (section gelée) | liste d'arrêt, « Journal des ouvertures hors de son format », l. 1402-1406 | Un journal hors format verrouille tout : `garde_ouverture` relit le journal entier à chaque tentative et refuse `ligne-mal-formee`, voie normale comprise (sonde S3) ; la ligne fautive n'étant jamais corrigée, plus aucun verdict n'est ouvrable par la garde. Le texte dit « écart consigné » et le nœud côté T0.7, pas cette conséquence pour P3-bis ni le sort d'une réparation (C-2 de `845c4de5…`). | CL4-C07 |
| CL4-04 | à corriger (sections gelées) | plan, point 8, choix du code (a), l. 1106-1108 ; liste d'arrêt l. 1398 | D-4 est écrite sans condition (« … qui cite un autre chemin … : rien d'ouvert »). Le code ne la juge que sous une dernière décision « ouvrir » (`garde_adaptee_en_vigueur`) : avec `SCELLEMENT-T07` et la garde à un autre chemin, la voie normale ouvre (S6), « ouvrir pleinement » aussi (S6b), « ouvrir » refuse (S6c). À la lettre du texte scellé, la garde ouvrirait là où la liste d'arrêt dit « rien d'ouvert ». | CL4-C08, CL4-C09 (le texte suit le code, conforme à R-2103 ; C-4 de `845c4de5…`) |
| CL4-05 | mineur (section gelée) | plan, point 8, rendez-vous, l. 1160-1164, contre le résumé (3) et (4), l. 1208-1216 | « Lazar écrit l'une de deux décisions … plus tard, une troisième » contredit le résumé (4) (« écrite au rendez-vous »), et le code admet « ouvrir pleinement » en première décision (S4). Le piège n'est dit qu'au résumé : « ouvrir » sans garde adaptée en vigueur n'ouvre rien (S5), ne peut plus être suivi (S5b), et toute ligne de rendez-vous inscrite ensuite fait refuser jusqu'à la voie normale (S5c). | CL4-C10 ; et, hors texte : la mère vérifie l'état de T0.7 avant de porter le rendez-vous à Lazar. |
| CL4-06 | **bloquant de procédure** (machine), texte à mettre à jour | préalables P-1 et P-4 ; ligne « Tests attendus » | Les relevés du texte sont ceux de la machine de la mère précédente. Sur celle de la mère qui a repris (R-2191) : `df -Pk /` à 11:43:30 UTC : **713 316 ko libres** (99 % ; 12 692 612 exigés par `PLACE_MIN_KO` : il manque 11 979 296 ko) ; `/usr/bin/python3.11` : 3.11.17 ; `.venv` : Python 3.13.16. Ni la répétition finale (P-4, P-6) ni le recompte de N (P-2) ne sont jouables ici en l'état. | CL4-C11, CL4-C12 ; place à trouver par la mère avant P-2. |
| CL4-07 | **bloquant de procédure**, hors du texte | `registres/go.md` l. 297 à 299 sur `main` ; P-3 | GO-2026-11-10-07, -08 et -09 n'ont que six colonnes (colonnes « accordé par » et « référence » absentes). `verifications_p3bis_v1.py go` rend « registre des GO mal formé ligne 297 : 8 colonnes attendues, 6 trouvées » (code 1) ; la garde de calcul, jouée à blanc comme au bloc 5, bloque de même (code 2). P-3 demande de porter ce registre sur la branche de scellement : l'étape 6 du scellement, le bloc 5 des contrôles et **toute création sous tout GO** refuseraient. | Hors texte : la mère (ou Lazar : « une ligne par GO, jamais modifiée ») règle le registre ; CL4-C13 ajoute la vérification à P-3. |
| CL4-08 | **bloquant de procédure** (chaîne et lignée) | `sceller_p3bis_v1.sh`, vérification de S ; bloc 14 des contrôles ; lignée `a1de3915` | À `a1de3915`, `docs/notes/ideation-organisme-v1/question-mere-reponses/consigne-argon-question-mere-v3.txt.sha256` existe sans son fichier (R-799 ; `git cat-file -e`). `verifier_arbre` sur ce dossier extrait rend « empreinte orpheline : le fichier scellé est absent ». Or le scellement exige « arbre intact » sur l'extraction de S, **après** le commit local de S (sinon « S commité localement, NON poussé »), et le bloc 14 l'exige avant toute création. Le rapport du lanceur v1 (`748568cb…`, l. 31-33) relevait cette anomalie comme « étrangère » ; aucun préalable ne la règle. | CL4-C14, CL4-C15 (préalable P-10) ; la voie est à décider par la mère (docs/ est hors de l'arbre gelé). |
| CL4-09 | mineur (R6) | « Métrique », PB-2 ; plan, point 10 | Le niveau « au plus 2⁻⁶ » renvoie à `nulle-appariee-v1.txt` (`c333a4c7…`), qui n'est pas au dépôt (`git ls-files` : absent ; bac à sable du contre-lecteur 1). Les nombres sont au rapport `8399dc55…`, § 2, M2 et § 5. | CL4-C16 (hors section gelée) |
| CL4-10 | mineur | devis, « Brouillon 10 » ; CD-07 | Le stockage d'une instance gardée est « compté dans la dépense de la course », mais personne ne le relève une fois la surveillance arrêtée ; le plafond de 80 USD n'est alors plus surveillé. | CL4-C17 |
| CL4-11 | limite de cette contre-lecture ; préalable | commits `614fd5da` et `8ad29273` | Absents de ce clone (`git cat-file -t` : objets inconnus ; aucune référence `prep/p3bis*`). Non vérifiés à la source : la sortie v3 de l'essai de fermeture (`57d3467c…`), la sortie du rejeu de concordance (`3e2fada3…`), `PLACE_MIN_KO=12692612` (à `a1de3915` : `A_MESURER`). Recoupés seulement avec le complément v2 du lanceur (`06ea31cf…`, l. 40, 45, 119-123, 160-163) et la contre-lecture `845c4de5…`, qui a relu la sortie v3 par `git show`. | La mère récupère la branche `prep/p3bis-lanceur-v1` et recalcule ces trois empreintes avant le candidat ; je n'ai pas le droit de `fetch`. |
| CL4-12 | à porter au marqueur `CONTRE_LECTURE_4_P3BIS` | section « Contre-lecture », entrée 4 | L'entrée annonce des fichiers de T0.7 (brouillons 16 et 19, `registre_v1.py`) et « Fable recommandé ». Cette contre-lecture est de Fable 5.2 et **sans aucun fichier de T0.7** : je n'ai vérifié ni ce que G2 et G3 de T0.7 lisent du journal, ni les trois écrits, ni la concordance avec le brouillon 16 ; ils reposent sur l'essai de concordance (R-2103), son rejeu (R-2113) et P-9. Je n'ai lu aucun résultat de la « mesure unanime » ; R-2157, que j'ai lue, nomme sa branche de quarantaine, que je n'ai pas ouverte. | Texte proposé pour le marqueur, ci-dessous. |
| CL4-13 | point ouvert (déjà connu, R-2167) | plan, point 8 ; décisions | La date du rendez-vous reste « proposée » jusqu'au défaut du 2026-11-11 vers 16:03 UTC. Un scellement avant cette heure expose à un écart à un texte scellé si Lazar la change. | Sceller après le défaut ou après le mot de Lazar ; l'écrire au candidat (« date tenue : défaut échu, R-… »). |
| CL4-14 | mineur, hors texte | ma consigne | Elle dit « ≥ 12,69 Go » : le seuil est 12 692 612 ko de 1 024 octets, soit ≈ 13,0 Go (12,10 Gio), comme l'écrit P-4. | Rien au texte. |
| CL4-15 | mineur | CD-08 de `01194253…` | `ouvrir --date-paquet` reste fixée par l'appelant ; elle ne commande que la réserve « écrit après la lecture fermée ». Non porté au texte, sans effet sur l'issue. | Une phrase au candidat, ou rien. |
| CL4-16 | mineur | en-tête, « Lu », l. 102 | `registres/go.md` est cité par l'empreinte `e682abb0…` sans commit ; registre vivant, il vaut `9733d45c…` à ma lecture (lignes 217 et 292 inchangées). | Citer par commit, comme le fait le reste de l'en-tête. |

## Marqueurs restants et qui les lève

| marqueur | état | qui, quand | dépend de |
|---|---|---|---|
| `TESTS_ATTENDUS_P3BIS` | 531 provisoire (Python 3.13, deux comptes concordants : R-2113, `845c4de5…`) | session mère, après P-1 et P-2 | environnement 3.11 et place disque (CL4-06) |
| `LONGUEURS_P3BIS` | à mesurer au vrai tokeniseur ; fichier JSON des longueurs attendues à verser | session mère (accès au tokeniseur) | A = T exigé, sinon nœud ; brouillon neuf des consignes s'il faut |
| `EMPREINTE_CONSIGNES_P3BIS` | à remplir après la mesure | rédacteur du candidat | `LONGUEURS_P3BIS` |
| `EMPREINTE_CONFIG_P3BIS` | à remplir après les consignes | rédacteur du candidat | `EMPREINTE_CONSIGNES_P3BIS` |
| `CHAINE_P3BIS` | chaîne à `614fd5da` ; restent épingles et passages canoniques | développeur de la chaîne, session mère | P-5, P-6, donc CL4-06, CL4-07, CL4-08, CL4-11 |
| `CONTRE_LECTURE_4_P3BIS` | ce rapport | session mère | empreintes ci-dessous |

Aucun marqueur ne doit survivre au scellement ; tous sont remplissables au candidat. Le candidat différera du brouillon 11 par ces six remplissages et par les couples retenus : cet écart n'est relu par personne tant qu'une relecture courte, au moins par programme (couples appliqués par script, sections gelées comparées au brouillon 11), n'est pas faite ; `CANDIDAT_RELU` l'épingle.

**Texte proposé pour le marqueur** (à adapter par la mère) : « contre-lecteur neuf **Claude Fable 5.2** (`claude-fable-5-2`), autre modèle que les rédacteurs (Opus 5.5), qui n'a écrit ni ce texte, ni les contre-lectures 1 à 3, ni le code de P3-bis, ni sa chaîne, ni leurs contre-lectures, et qui n'a lu aucun fichier de T0.7 ni aucun résultat de la « mesure unanime » ; 10 novembre 2026, de 11:38 à 11:52 UTC ; brouillon relu `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon11.md`, `409c37ed4aa4f149565d8b0a45ae94c16b572f35967f080a0df629985549b290` ; rapport `brouillons/P3-bis-temoin-positif-v1/contre-lecture-4-brouillon11-v1.md`, <empreinte du rapport> ; verdict « scellable après corrections » (CL4-01 bloquant de texte ; CL4-02 à CL4-04 à corriger ; CL4-05, CL4-09, CL4-10, CL4-14 à CL4-16 mineurs ; CL4-06 à CL4-08 et CL4-11 bloquants de procédure) ; traitement : … ».

## Gestes déclarés

- **Git, au-delà de `git show <commit>:<chemin>`**, tous en lecture seule, sans écriture d'index ni de référence : `git status` et `git log --oneline` (trois commits de `main`, deux de la lignée du code, trois de `registres/go.md`) ; `git cat-file -t` et `-e`, `git merge-base --is-ancestor` ; `git diff --name-status` et `--name-only` entre commits nommés, restreints aux chemins de l'en-tête et à `src tests scripts requirements-* .claude` ; `git for-each-ref` sur `prep/p3bis*` et `scellement/p3bis*` ; un `git branch -a` filtré, qui a affiché des noms de branches `canal/…` et aucun nom interdit ; `git ls-files` filtré par motifs nommés ; un `git archive a1de3915 -- docs/notes/ideation-organisme-v1/question-mere-reponses` (sept fichiers, dans mon bac à sable, effacés ensuite) pour CL4-08. Si la règle 4 se lit à la lettre, ces gestes la dépassent : je les signale.
- **Garde de calcul** jouée une fois à blanc (commande fictive sur l'entrée standard, comme le bloc 5) : aucun appel externe, aucune location.
- **Lu en passant** : des lignes du registre des décisions étrangères à P3-bis (R-2165 à R-2170, R-2177, R-2182, R-2191 en tête) ; R-2157 nomme la branche de quarantaine de la « mesure unanime » (non ouverte) ; R-2153 et R-2166 parlent de T0.7 (lignes de registre, aucun fichier de T0.7).
- **Interdits tenus** : aucun fichier ni branche de la règle 1 ouvert ; aucune valeur de sonde de 7a vue ; aucune clé lue ; aucun appel de modèle ni d'interface ; aucun commit ; aucune suite complète ; recherches dans des fichiers nommés seulement. **Aucun refus de permissions ni de classifieur.**
- **Écrit** : ce rapport et son compagnon, rien d'autre dans le dépôt ; fichiers de travail dans mon bac à sable (copies du code à `a1de3915`, sondes, copie d'épreuve du brouillon 11 avec mes couples, `913767a9284256ea6675e33a993df18ee9f4afb7ae4d3a70cb597acfde779bea`, non versée).

## Sondes de la garde d'ouverture (module `1361382e…`, 11:47 UTC)

```
S1 LF : au format, 1 ligne(s)
S1 CRLF : au format, 1 ligne(s)
S1 CR seul : au format, 1 ligne(s)
S1 mêlées : au format, 1 ligne(s)
S2 voie normale sous « maintenir », pleine : AUTORISÉ mode pleine — chemin normal (rendez-vous sans objet)
S3 journal hors format, voie normale conforme, pleine : REFUS ligne-mal-formee — journal des ouvertures hors format : ligne 3 : 1 cellules, 6 attendues
S4 première décision « ouvrir pleinement », sans scores, pleine-anticipee : AUTORISÉ mode pleine-anticipee — branche 2 (décision « ouvrir pleinement ») : T0.7 ne lit plus la course 7b sous son texte, nœud de Lazar
S4b idem, scores conformes, pleine-anticipee : REFUS ni-scores-ni-ouvrir — lignes SCORES-T07 et SONDES-T07 inscrites et conformes au registre des scellements : « pleine-anticipee » refusée, seule « pleine » est permise ; le m
S4b idem, pleine : AUTORISÉ mode pleine — chemin normal (rendez-vous sans objet)
S5 « ouvrir » sans garde adaptée, reduite : REFUS garde-adaptee-absente — T0.7 non scellé (aucune ligne SCELLEMENT-T07) ; [garde-adaptee-absente] aucune ligne GARDE-ADAPTEE-T07-P3BIS
S5 idem, pleine-anticipee : REFUS garde-adaptee-absente — T0.7 non scellé (aucune ligne SCELLEMENT-T07) ; [garde-adaptee-absente] aucune ligne GARDE-ADAPTEE-T07-P3BIS
S5b « ouvrir » sans réduite puis « ouvrir pleinement », pleine-anticipee : REFUS ligne-apres-decision-finale — ligne RENDEZ-VOUS-P3BIS-2 après la décision « ouvrir » de RENDEZ-VOUS-P3BIS-1 : seule une décision « ouvrir pleinement » est permise, et seulement apr
S5c « ouvrir » puis « maintenir », pleine : REFUS ligne-apres-decision-finale — ligne RENDEZ-VOUS-P3BIS-2 après la décision « ouvrir » de RENDEZ-VOUS-P3BIS-1 : seule une décision « ouvrir pleinement » est permise, et seulement apr
S5d « ouvrir » sans garde, scores conformes, pleine : AUTORISÉ mode pleine — chemin normal (rendez-vous sans objet)
S6 SCELLEMENT-T07 et garde à un autre chemin, voie normale, pleine : AUTORISÉ mode pleine — chemin normal
S6b idem sous « ouvrir pleinement », pleine-anticipee : AUTORISÉ mode pleine-anticipee — branche 2 (décision « ouvrir pleinement ») : T0.7 ne lit plus la course 7b sous son texte, nœud de Lazar
S6c idem sous « ouvrir », reduite : REFUS garde-adaptee-absente — SCELLEMENT-T07 cite 'prereg/autre-texte.md', 'prereg/T0.7-sondes-v0-v1.md' attendu (D-4, R-2103) ; [garde-adaptee-absente] GARDE-ADAPTEE-T07-P3BIS cit
S6d cas sain : garde en vigueur sous « ouvrir », reduite : AUTORISÉ mode reduite — branche 1 (ouverture réduite à l'issue)
```

## Liste exacte des couples (à appliquer par script au brouillon 11, dans l'ordre ; chaque « ancien » y figure une fois)

Vérifié sur une copie de travail : dix-sept couples appliqués, chacun trouvé une fois ; sections gelées touchées : « Plan d'analyse » (CL4-C05, CL4-C08, CL4-C10) et « Liste d'arrêt » (CL4-C07, CL4-C09), rien d'autre ; `prereg.problemes` inchangé ; `valeurs` de la chaîne : 19 sur 19 ; huit intitulés, ligne « - GO : » et ligne « - Lancement : » inchangés. Le « nouveau » de CL4-C14 tient sur deux lignes (une ligne de table ajoutée) ; tous les autres tiennent sur une ligne.

**CL4-C01** — non gelée — en-tête, commit du code — constat CL4-01

ancien :

~~~
**sous réserve de sa contre-lecture différentielle courte, en cours** (R-2131) :
~~~

nouveau :

~~~
**contre-lu** par la contre-lecture différentielle courte, rendue (R-2158 ; `brouillons/P3-bis-temoin-positif-v1/contre-lecture-differentielle-code-a1de3915-v1.md`, `845c4de54e72207a320edf089c606bacf0cd87837d473ab654de48c3ddc839c9`, égale à son compagnon : « citable au scellement », aucun constat bloquant, six constats mineurs, dont C-1 à C-4 portés à ce texte) ; pour tout commit neuf, la règle reste :
~~~

**CL4-C02** — non gelée — Ce que le code et la chaîne doivent changer, point 2 — constat CL4-01

ancien :

~~~
contre-lecture différentielle courte de `02217f1c..a1de3915` en cours, R-2131
~~~

nouveau :

~~~
contre-lecture différentielle courte de `02217f1c..a1de3915` rendue, `845c4de5…`, R-2158 : citable au scellement, aucun constat bloquant
~~~

**CL4-C03** — non gelée — Préalables, P-7 — constat CL4-01

ancien :

~~~
(en cours, R-2131) rendue sans défaut qui change le code
~~~

nouveau :

~~~
(R-2131) rendue sans défaut qui change le code — **fait** : R-2158, rapport `845c4de5…`, cité à l'en-tête
~~~

**CL4-C04** — non gelée — Marqueurs restants, table, COMMIT_CODE_P3BIS — constat CL4-01

ancien :

~~~
(en cours, R-2131 ; préalable P-7)
~~~

nouveau :

~~~
(rendue, `845c4de5…`, R-2158 : citable au scellement ; préalable P-7 fait)
~~~

**CL4-C05** — GELÉE : Plan d'analyse — point 8, journal, prédicat unique — constat CL4-02

ancien :

~~~
lu en UTF-8 (fins de ligne CRLF lues comme LF), est au format
~~~

nouveau :

~~~
lu en UTF-8 (fins de ligne CRLF et retour chariot seul lus comme LF, mêlés ou non, par la lecture en mode texte ; l'écrivain n'écrit que LF ; C-1 de la contre-lecture `845c4de5…`), est au format
~~~

**CL4-C06** — non gelée — Préalables, P-9 — constat CL4-02

ancien :

~~~
le lecteur de T0.7 appliquant en entier le prédicat du plan, point 8 (R-2103)
~~~

nouveau :

~~~
le lecteur de T0.7 appliquant en entier le prédicat du plan, point 8 (R-2103), les cas « retour chariot seul » et « fins de ligne mêlées » ajoutés au rejeu (C-1 de la contre-lecture `845c4de5…`)
~~~

**CL4-C07** — GELÉE : Liste d'arrêt — journal des ouvertures hors de son format — constat CL4-03

ancien :

~~~
la ligne n'est jamais corrigée en place (R12), une ligne neuve de la garde suit.
~~~

nouveau :

~~~
la ligne n'est jamais corrigée en place (R12), une ligne neuve de la garde suit ; **tant que le journal est hors format, la garde refuse toute ouverture, voie normale comprise** (`ligne-mal-formee` à chaque tentative ; un refus peut alors être daté avant une ligne lisible plus haute, C-2 de la contre-lecture `845c4de5…`) : aucun verdict sans un mot de Lazar (nœud) ; toute réparation du journal est un écart déclaré, décidé par ce nœud.
~~~

**CL4-C08** — GELÉE : Plan d'analyse — point 8, choix du code (a), D-4 — constat CL4-04

ancien :

~~~
motif « … attendu (D-4, R-2103) » ;
~~~

nouveau :

~~~
motif « … attendu (D-4, R-2103) » ; ces cas de la garde adaptée ne sont jugés que sous une dernière décision « ouvrir » (branche 1) : sous la voie normale ou sous « ouvrir pleinement », le chemin de ces deux lignes n'est pas jugé, la garde adaptée n'y étant pas employée (C-4 de la contre-lecture `845c4de5…`) ;
~~~

**CL4-C09** — GELÉE : Liste d'arrêt — garde d'ouverture en refus, D-4 — constat CL4-04

ancien :

~~~
qui cite un autre chemin que `prereg/T0.7-sondes-v0-v1.md` (D-4)) :
~~~

nouveau :

~~~
qui cite un autre chemin que `prereg/T0.7-sondes-v0-v1.md`, sous une dernière décision « ouvrir » (D-4 ; branche 1 seulement)) :
~~~

**CL4-C10** — GELÉE : Plan d'analyse — point 8, rendez-vous écrit de Lazar — constat CL4-05

ancien :

~~~
ou « ouvrir » ; plus tard, une troisième
~~~

nouveau :

~~~
ou « ouvrir » (à n'écrire que si la garde adaptée est en vigueur : sans elle, « ouvrir » n'ouvre rien et ne peut plus être suivi d'aucune décision, toute ligne de rendez-vous inscrite ensuite faisant refuser jusqu'à la voie normale, `ligne-apres-decision-finale` ; résumé, (3)) ; au rendez-vous ou plus tard, une troisième
~~~

**CL4-C11** — non gelée — Préalables, P-1 — constat CL4-06

ancien :

~~~
(`/usr/bin/python3.11`, version 3.11.18 sur la machine de la session)
~~~

nouveau :

~~~
(`/usr/bin/python3.11` ; version à relever au candidat sur la machine de la session qui scelle : 3.11.18 sur celle de la mère précédente, 3.11.17 sur celle de la mère qui a repris, R-2191, relevée par la contre-lecture 4 le 2026-11-10 à 11:43 UTC, où `.venv` est en Python 3.13.16)
~~~

**CL4-C12** — non gelée — Préalables, P-4 — constat CL4-06

ancien :

~~~
relevé à 2026-11-10T10:28:32Z : 11 512 240 ko libres, il en manquait 1 180 372 ko
~~~

nouveau :

~~~
relevé à 2026-11-10T10:28:32Z, sur la machine de la mère précédente : 11 512 240 ko libres, il en manquait 1 180 372 ko ; relevé à 2026-11-10T11:43:30Z par la contre-lecture 4, sur la machine de la mère qui a repris (R-2191) : 713 316 ko libres, il en manque 11 979 296 ko ; à relever de nouveau au candidat
~~~

**CL4-C13** — non gelée — Préalables, P-3 — constat CL4-07

ancien :

~~~
exactement une ligne GO-2026-11-10-02 dans `git show <branche>:registres/go.md`, égale à celle de `main` ;
~~~

nouveau :

~~~
exactement une ligne GO-2026-11-10-02 dans `git show <branche>:registres/go.md`, égale à celle de `main` ; registre accepté en entier par le module commun `go` et par la garde de calcul, qui refusent tout le registre dès qu'une ligne « | GO-… » n'a pas huit colonnes (le 2026-11-10 à 11:43 UTC, les lignes 297 à 299 de `registres/go.md` sur `main`, GO-2026-11-10-07 à GO-2026-11-10-09, n'en ont que six : contre-lecture 4, CL4-07) ;
~~~

**CL4-C14** — non gelée — Préalables, ligne P-10 neuve — constat CL4-08

ancien :

~~~
sortie versée : aucune discordance ; une discordance est un nœud |
~~~

nouveau :

~~~
sortie versée : aucune discordance ; une discordance est un nœud |
| P-10 | **Arbre scellé intact sur la lignée de scellement** : au commit du code `a1de3915`, `verifier-arbre` relève une empreinte orpheline, `docs/notes/ideation-organisme-v1/question-mere-reponses/consigne-argon-question-mere-v3.txt.sha256` (R-799 : fichier jamais versé sur `main`) ; tant qu'elle est dans la lignée, le bloc 14 des contrôles avant dépense et la vérification de S par `sceller_p3bis_v1.sh` (jouée après le commit local de S) refusent ; avant S, un commit de la branche de scellement, hors de l'arbre gelé, règle ce point par la voie que la mère décide et consigne au registre (contre-lecture 4, CL4-08) | session mère | `verifier-arbre` sur l'extraction `git archive` de la branche, chemins interdits exclus : dernière ligne « arbre intact » ; rejoué par la répétition finale |
~~~

**CL4-C15** — non gelée — Préalables, ordre — constat CL4-08

ancien :

~~~
P-9 dès que les deux codes sont finaux ; enfin S.
~~~

nouveau :

~~~
P-9 dès que les deux codes sont finaux ; P-10 avec P-3, avant P-6 ; enfin S.
~~~

**CL4-C16** — non gelée — Contre-lecture, entrée 1 — constat CL4-09

ancien :

~~~
M11 : déclaré (code, point 8), non corrigé (R12).
~~~

nouveau :

~~~
M11 : déclaré (code, point 8), non corrigé (R12). La sortie `nulle-appariee-v1.txt` (`c333a4c7…`) citée à « Métrique » et au plan, point 10, est restée dans le bac à sable de ce contre-lecteur et n'est pas versée au dépôt : ses nombres se lisent dans son rapport, cité ci-dessus par son chemin et son empreinte (§ 2, M2 et § 5 ; R6).
~~~

**CL4-C17** — non gelée — Devis, brouillon 10, instance gardée — constat CL4-10

ancien :

~~~
compté dans la dépense de la course ; le second
~~~

nouveau :

~~~
compté dans la dépense de la course et relevé par la session mère à chaque reprise (routine R14, point 4), la surveillance étant alors arrêtée, avec retour à Lazar avant que la dépense cumulée n'approche 80 USD (CD-07 de la contre-lecture `01194253…`) ; le second
~~~

