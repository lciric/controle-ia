**Relecture courte de P3, angle texte (relecteur T, sous-agent neuf), 2026-10-19.** J'ai relu le dépôt à la tête 1030eb8, qui est au-dessus de 03cb538, en lecture seule. Aucun fichier du dépôt n'a été touché.

**Empreintes vérifiées**
- **Candidat 1** : `8070b64085ae649c68b79222fdfbb1aea1fc7e99edc5510822ea387b82805dd0`, égal à l'attendu. Il est identique, octet pour octet, à la sortie de `construire_candidat1.py` sur le brouillon 4 avec « 893 » (vérifié par `cmp`).
- **Brouillon 4** : `94e5ff12b45437760638309fe88031b181d7e49d0a49810b8525e12eebc7383b`. Il n'a pas de sceau compagnon, comme les autres brouillons de texte.
- **Contre-lectures** : `98d7201b…` et `57060da8…`, sceaux conformes.
- **Configuration et consignes** : configuration candidat 3 `702303e9…`, empreinte canonique recalculée `2f343a6f…` ; consignes candidat 2 `a68468fe…`.
- **Commit `03cb53804e0b98fe671b62ebf5ef2d819741e282`** : il existe. À ce commit, chaque empreinte est égale à celle du candidat :
  - amorce `0bfaeaa64a0c355ba04bf84c9afc76ea31034a837e44cd588becf88f3aa5dae0` ;
  - `p3_instance.sh` `2bfc6939efe8b68d17b921e0ea8b91e2809b04e5c37006c18364dc4776dc3663` ;
  - tests des gardes `cf4ab7b841a5599a23b01255a32d8e378200751c2472176892a7e02a5df956b3` ;
  - traitement de la chaîne `ad1d88d27dca0d4acfdbaed3238b179ea923574dd4abcf0811c5c025cb0e12ca`.
- **Chaîne** : 14 sceaux sur 14 conformes au brouillon 2, 12 sur 12 au brouillon 1.
- **Arbre gelé et modules antérieurs** : l'arbre gelé est identique de 03cb538 à la tête. Les modules gelés des étapes antérieures sont intacts : `git diff` de 2660b07 et de c63d4f1 vers 03cb538, sur les chemins de CH-08, est vide.
- **Offre du pilote** : `offre.json` `4f1eee6457818f4a5019aba35a9b3eb10f42e9d9173cc629623ee4b84083acc0`. Téléchargement 0,02604 USD par Go, stockage 0,02222 USD de l'heure.
- **Registre des dépenses** à 03cb538 : `c603a974…`. Ligne 26 : 0,039 USD par Go, « ≈ 20 Go, ≈ 0,8 USD », stockage 0,027 USD de l'heure.
- **Mesures v2** : `28b87c71…`, `aa049615…`, `8a08307c…`. Les seize empreintes de fichiers citées par le candidat sont égales au contenu à 03cb538.
- **Tests** :
  - 893 tests collectés à 03cb538, comme dans R-215.
  - J'ai simulé S dans un clone jetable : 03cb538, plus le candidat 1, la configuration candidat 3 et les consignes candidat 2, scellés. La suite complète y donne « 893 passed in 1724.47s (0:28:44) ». Cette ligne passe le motif des contrôles et celui du script de l'instance.
- **Gardes qui relisent le texte**, jouées sur ce S simulé :
  - configuration conforme ; commit cité 03cb538 ; entropie 173398867739501636779144561928402532101 ;
  - 240 épisodes et 96 graines ;
  - les neuf intitulés figurent une fois chacun ; `problemes()` est vide ;
  - la lecture précoce donne 893 et les trois chemins.
- **Bloc 9 des contrôles** : joué sur une copie du brouillon 2 avec la borne 0.05, il rend le code 0. Ses 19 valeurs sont présentes dans le texte.

**Constats**, du plus grave au moins grave

| id | gravité | où | ce qui est écrit | ce qui est juste, et pourquoi | correction proposée |
|---|---|---|---|---|---|
| RT-01 | bloquant | candidat l. 44-47 ; `brouillons/P3-chaine-v1-brouillon2/verifications_p3_v1.py` l. 42, 84-92 ; `registres/decisions.md` l. 352 (R-215) | Une révocation de R-192 serait une ligne R-… qui « révoque », « retire » ou « annule » R-192. La chaîne refuse alors de lancer. | Le module cherche des mots, pas un sens : un verbe collé à « R-192 » (l. 88-89). R-215 contient « révocation de R-192 » et « annule R-192 ». La commande `python3 -I …/verifications_p3_v1.py go <candidat 1> registres/go.md registres/decisions.md` rend « décision R-192 révoquée, retirée ou annulée par R-215 », code 1. Avec le registre de 03cb538, elle rend le code 0. Ce contrôle tourne au scellement (l. 147), dans les contrôles (l. 144) et dans le lanceur (l. 131). Il tourne aussi dans le cas sain G00 du banc des contrôles, qui lit le registre du commit éprouvé (`essais_controles_p3_v1.sh` l. 287). En l'état, S ne peut pas être scellé. Une phrase comme « aucune révocation de R-192 » bloquerait aussi la chaîne. À l'inverse, deux vraies révocations passent sans être vues (essai du motif) : « Lazar retire sa décision R-192 » et « R-192 (option (b) élargie) est annulée ». | Changer le module, dans un brouillon 3 de la chaîne : une forme fixe et rare, par exemple une cellule de décision qui commence par « **Révocation de R-192** » avec la source « Lazar ». Ajouter un artefact et un cas sain qui reprend la phrase de R-215, puis rejouer les bancs. Écrire cette forme exacte au texte. Corriger aussi la phrase « Les copies versées ne diffèrent du brouillon 2 que par… » (l. 403-406). R-215 ne se réécrit pas. |
| RT-02 | mineur | candidat l. 100, 104-106, 364 ; Seuil l. 227 ; `lecture.py` l. 297-299 | H-P3c : « ne sépare pas le témoin de l'honnête ». T3 : « ne sépare pas de l'honnête la condition mention ». Ligne 6 : la conclusion n'exclut pas la lecture du texte trompeur « sauf T3 établi ». | Le Seuil dit : « non au-dessus » se lit « non détecté à cette puissance », jamais « ne sépare pas ». Une moitié de T3 est un « non au-dessus », alors que l'aire minimale détectable vaut ≈ 0,57 à 0,58 (l. 335-336). Le mot « exclut » est donc trop fort. C'est le défaut de TC-04, revenu par T3. | Dans H-P3c et T3, écrire : « ne sépare pas au sens du seuil (non détecté à cette puissance) ». Ligne 6 : « T3 établi : lecture du texte trompeur non détectée à cette puissance ; aire, intervalle et plancher de mention contre honnête rapportés ». |
| RT-03 | mineur | candidat l. 343-345, 365 ; `lecture.py` (03cb538) l. 297-299, 352, 366, 373 ; R-202 (1) | « Fuite avérée » rend un jeu « non interprétable ». La seule conséquence écrite porte sur saboteur contre honnête. La ligne 7 suppose « saboteur contre témoin non au-dessus ». | Trois cas n'ont aucune ligne écrite. J'ai joué `issue()` sur des sorties synthétiques : <br>• saboteur contre témoin au-dessus mais non interprétable donne « non concluant pour la validité » ; <br>• témoin contre honnête en échec donne la même ligne ; <br>• saboteur contre mention non interprétable laisse « intention établie », car T3 ignore la fuite. <br>Or R-202 (1) dit qu'une fuite mène à la ligne « non interprétable ». Le verdict prononcé par un sous-agent neuf (règle R13) et l'issue calculée par le code peuvent donc diverger. | Écrire qu'un jeu non interprétable ou en échec ne compte ni « au-dessus » ni « non au-dessus », et quelle ligne s'applique alors. Pour T3, deux voies : aligner le code (nouveau commit), ou écrire l'asymétrie. |
| RT-04 | mineur | candidat l. 147-149 ; brouillon 3 l. 101-102 | La forme du champ `COST` est comptée, sans rien dire de son effet. | Le brouillon 3 écrivait : « « 3 × 400 » se lit 3 ; une forme propre au saboteur peut masquer ou fabriquer l'effet ». Cette phrase a disparu au brouillon 4, sans être annoncée dans les changements (l. 72-80). Il ne reste que « peut masquer l'effet, pas le fabriquer » pour les milliers (l. 138), qui ne vaut pas pour les autres formes. C'est une limite perdue de P3-P1, qui est décisive. | Rétablir la phrase dans le paragraphe sur la forme du champ `COST`. |
| RT-05 | mineur | candidat l. 301-305, 316-321, 395 ; `registres/depenses.md` l. 19 et 26 ; `lancer_p3_v1.sh` l. 182-188, 206, 280 | « ≈ 20 Go relevés à l'offre 29019328 » ; « soit au plus ≈ 11,2 USD ». | Les 20 Go sont une prévision écrite avant le run (l. 19 : « modèle, roues »), pas une mesure ; un volume ne dépend pas de l'offre. Le prix du stockage n'est pas borné par le filtre : il est seulement archivé (l. 206). 11,2 USD est donc une estimation, alors que la liste d'arrêt (l. 395) en fait une borne. L'arithmétique est juste : 8,02 + 0,22 + 1,00 + 1,94 = 11,18. Le crédit exigé vaut 6,5 × 1,30 + 1,2 = 9,65 USD (l. 280) : le disque des 72 heures repose sur la recharge automatique (R-150), qui n'est pas écrite. | Écrire « ≈ 20 Go estimés » et « dépense estimée à ≈ 11,2 USD, recalculée à la création avec le prix de stockage de l'offre retenue ». Sinon, borner `storage_total_cost` dans le filtre. Nommer la recharge automatique. |
| RT-06 | mineur | candidat l. 8-9, 407, 455 ; `src/controle_ia/prereg.py` l. 26-27, 37-60 ; `sceller_p3_v1.sh` l. 52-54, 114-117 | « Le texte scellé sera la copie, octet pour octet, du candidat relu » ; un champ « [après la relecture courte : …] » reste à remplir. | Ce champ changera après cette relecture : le texte scellé sera un candidat 2, que personne n'aura relu. `problemes()` ne voit pas ce champ, car il ne cherche que « À REMPLIR » et « <<…>> » ; sur le S simulé, il rend `[]`. Le scellement exige chaque rapport épinglé, nommé `P3-premier-test-v1-…-v1.md` et cité « `prereg/contre-lectures/<nom>` (`<sha256>`) ». Il y aura trois rapports, pas un seul. | Faire un candidat 2 qui cite les trois rapports sous cette forme, avec leur traitement. Faire relire l'écart entre candidat 1 et candidat 2 par un sous-agent neuf. Marquer « À REMPLIR » tout champ restant. |
| RT-07 | mineur | candidat l. 392-394 | La ligne « aucune création » liste : prix, cœurs, mémoire, crédit, instance, GO, accord. | Deux conditions nouvelles du candidat y manquent : un téléchargement au-dessus de 0,05 USD par Go (l. 301-303 ; lanceur l. 187), et une révocation de R-192 (l. 44-47). | Ajouter ces deux conditions. |
| RT-08 | mineur | candidat l. 331-332 ; `docs/notes/P3-mesures-v2/puissance-p3-v1.txt` l. 5 | « À δ = 0, l'une des trois paires a une borne basse de +0,03 ». | La sortie brute imprime « +0.000 » pour la paire e2−e1. J'ai rejoué la section 1 de `puissance_p3.py` avec les mêmes graines, en n'imprimant que des nombres : bornes basses +0,0296 (e2−e0) et +0,000214 (e2−e1). Deux paires sur trois passent donc le critère de P3-P1 à δ = 0. Les deux font intervenir l'épisode 2. | Écrire « deux des trois paires, toutes deux avec l'épisode 2 ». Dire que P3 n'y est pas exposé : toutes les conditions jouent l'épisode e0, avec les mêmes graines d'action. Produire une nouvelle sortie à plus de décimales (R12). |
| RT-09 | mineur | candidat l. 212 et 295-296 ; `lecture.py` l. 226-240 ; R-202 (1) | Placebo « avant toute autre lecture de détection » (l. 212). Mais l'ordre du point 3 place le placebo après P3-P4 (l. 295-296). | Le texte se contredit ; le code suit le point 3. L'ordre ne change aucun nombre, car chaque lecture a sa propre graine. R-202 dit « avant la vraie ». | Garder une seule règle. |
| RT-10 | mineur (forme) | candidat l. 109 | « **[nœud soumis à Lazar le 17 octobre et retenu (R-203)** ». | Le crochet ouvrant n'est jamais fermé : le fichier compte deux « [ » pour un seul « ] ». Le fond est juste : R-203 dit « test T4 ajouté ». | Retirer le « [ ». |
| RT-11 | pour information | candidat l. 159-162 ; `recuperation_p3_v1.sh` l. 243, 275, 322-323 | Les textes sont cherchés « dans tous les autres fichiers ajoutés ». | Les tableaux npz sont exclus de cette recherche : leurs chaînes sont seulement bornées à 80 caractères (contrôle 4d), et le fichier léger des sondes n'est pas lu. Les autres valeurs écrites sont justes : 200, 1 000, affichage borné à 200, 64 et 48. | Ajouter « hors tableaux npz ». |
| RT-12 | pour information | candidat l. 322-324 ; `lancer_p3_v1.sh` l. 56, 245, 250-251 | « Seules sont tolérées » les instances d'autres projets d'étiquette « rr- », « comptées dans le crédit exigé ». | Elles doivent aussi être nommées en argument du lanceur. Seules celles en marche entrent dans le crédit. Les quatre identifiants détruits sont justes (R-212, R-214). | Préciser ces deux conditions. |
| RT-13 | pour information | candidat l. 436-437 ; `tests/test_premier_test_ia_gardes_v1.py` l. 1-5, 362, 389 | « 20 tests, un par garde listée ». | 18 tests couvrent les 16 gardes listées. Les 2 autres couvrent deux points que TC-11 disait non testés : les mêmes graines d'action, et le plan de la garde d'identité. | Le dire. |
| RT-14 | pour information | candidat l. 453-454 ; `tests/test_script_p3.py` l. 290 ; R-215 | Test du plafond de l'amorce « (cas sain et artefact, R5) ». | Le test joue seulement le plafond atteint. « L'artefact » (poussée retirée) a été une mutation faite une fois à la main. | L'écrire ainsi. |
| RT-15 | pour information | candidat l. 265-268 et 320-321 ; R-213 | Instance « gardée arrêtée jusqu'au verdict, 72 heures au plus », puis « détruite … une fois la récupération faite ». | Le texte donne deux déclencheurs différents. Rien n'est prévu si la destruction est refusée, comme dans R-213. | Garder une seule règle ; si la destruction est refusée, la rendre à Lazar. |
| RT-16 | pour information | candidat l. 325 ; R-215 | « Installation et suite des tests (≈ 26 minutes au pilote) ». | À 03cb538, la suite seule prend 27 à 29 minutes (1 631 s ; 1 724 s ici). Les bornes tiennent quand même : 40 + 305 < 360 minutes. | Écrire la durée attendue pour P3. |
| RT-17 | pour information | candidat l. 305 ; R6 | `registres/depenses.md` « l. 26 au commit `03cb538` ». | La règle R6 demande un chemin et une empreinte : ici `c603a97492517ff6edf977f542dffb4992378fb149fe02c2e58ff4b3b124085d`. | Ajouter l'empreinte. |
| RT-18 | pour information | candidat l. 7 | « les deux contre-lectures R2 du brouillon 3 ». | La seconde contre-lecture porte sur la chaîne, brouillon 1 (l. 419). | Corriger le libellé. |

**Constats d'origine, angle texte**
- **TC-01, traité en partie.** L'audit est gelé (l. 338-350). La ligne est toujours écrite (l. 354-355). La ligne « non interprétable » existe (l. 362). Les données sont gardées (l. 157-162, 176-181). Il reste RT-03.
- **TC-02, traité.** Les gardes sont écrites l. 293-295 ; `lecture.py` l. 80-99 porte les quatre.
- **TC-03, traité.** Cinq jeux (l. 182-184), dix jeux et miroir (l. 340-342), placebo (l. 212-213).
- **TC-04, traité en partie.** Seuil l. 226-228 et réfutation l. 125. Il reste RT-02.
- **TC-05, traité.** Mentions l. 152-156, identiques à `conditions.py` l. 34-36. Textes gardés, aires sans mention (l. 347-348), deux niveaux (l. 98-109), limite écrite (l. 364).
- **TC-06, traité.** L. 122, 124, 327-336 : les nombres sont égaux à la sortie brute. Une phrase est inexacte (RT-08).
- **TC-07, traité.** L. 93-94, 234-236, 367-368.
- **TC-08, traité.** L. 136-140 ; voir aussi RT-04.
- **TC-09, traité.** L. 134-136.
- **TC-10, traité.** L. 171-175, 379-380.
- **TC-11, traité.** L. 436-438 ; empreinte vérifiée ; 20 tests (RT-13).
- **TC-12, traité.** L. 258-259, 301-302, 308-311. Mesure : 822,8 s par couche, × 3 ≈ 2 470 s.
- **TC-13, traité.** 306 faits, 7 exclus, 598 exemples. 52 jetons sur 56 tâches, 51 sur 4. « 2,2 s » a disparu.
- **TC-14, traité.** L. 296-297.
- **TC-15, traité.** L. 359, 367, 299-300.
- **TC-16 à TC-19, traités.** TC-16 l. 190-192 ; TC-17 l. 218-222 ; TC-18 l. 192-194 ; TC-19 l. 263-268.
- **TC-20, traité.** (a) l. 147-149 ; (b) l. 387 ; (c) `run.py` l. 102-103 ; (d) l. 445 et `__init__.py` à 03cb538 ; (e) l. 174-175 ; (f) l. 252-254 ; (g) l. 168-170 ; (h) l. 384-385.
- **Constats de la chaîne qui touchent le texte, traités** :
  - CH-02 (l. 40-44) ; CH-03 (l. 410) ; CH-04 (l. 301-302, 392) ; CH-05 (l. 384-385) ;
  - CH-08 (l. 24-26) ; CH-11 (l. 42-44) ; CH-12 (l. 287-290) ;
  - CH-13 et CH-17 (l. 322-324) ; CH-18 (l. 159-162) ; CH-21 (l. 312-315) ; CH-23 (l. 402).
- **CH-09, traité en partie** : RT-01.
- **CH-10, traité en partie** : RT-05 et RT-07.
- **Sans objet pour le texte** : CH-01, CH-06, CH-07, CH-14, CH-15, CH-16, CH-19, CH-20, CH-22, CH-24.

**Ce que je n'ai pas pu vérifier**
- Je n'ai pas rejoué les bancs ni les répétitions (angle chaîne). Des journaux non officiels, je n'ai lu que la dernière ligne : 0 cas non conforme au dernier passage de chaque banc.
- Les affirmations sur le code ne sont que sondées (angle code) : « chaque combinaison testée », gardes « testées sur cas sain et artefact ».
- Je ne connais ni le volume réellement téléchargé, ni le prix du stockage de l'offre qui sera prise, ni les durées réelles sur l'instance.
- Je n'ai pas pu jouer le bloc 10, avec le vrai tokeniseur : pas d'accès au réseau.
- Je n'ai pas relu les PDF 2509.21344 et 2605.27958.
- La recharge automatique est lue dans R-150 et dans la passation, pas sur le compte.

**Fichiers de travail**, tous hors du dépôt, dans `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p3-relecture-courte/texte/` :
- le clone jetable `depot`, où le S simulé est le commit fc85d7b ;
- `candidat1-rejoue.md`, `gardes_texte.py`, `bloc9.py`, `issue_cas.py`, `puissance_delta0.py`, `suite-essai-s.txt`.

**Jugement d'ensemble** : scellable après traitement. RT-01 passe en premier : en l'état, la chaîne refuse le scellement.
