# Audit A9 — A1-v3, seconde course (GO-2026-11-03-01), état interrompu — v1

**Verdict : cause d'infrastructure établie.** La course s'est arrêtée hors des codes 0, 2 et 3 du lanceur, parce que son hôte (le
conteneur de la session fille) a disparu sous elle. Rien n'a été lu, rien n'a été relancé. La règle de la section 8 du texte
scellé v2 admet une troisième course, sur le texte v3 et GO-2026-11-04-06, si ce texte est contre-lu, scellé, committé et poussé
avant la course.

Auditeur neuf : je n'ai écrit ni les textes v2 et v3, ni le code, ni les ordres, ni l'audit de la première course. Audit écrit le
4 novembre 2026, commencé à 08:28:51 UTC et rédigé à partir de 08:35:49 UTC (heures relevées par `date -u`). Aucun modèle, aucune
dépense, aucun commit, aucun `.sha256`, aucun fichier existant modifié. Je n'ai lu le contenu d'aucun fichier de la branche de
données ni de l'état scellé (aucune réponse, aucun score, ni manifeste, ni registre de dépense, ni journal). Chaque commande est
passée par `timeout 300 nice -n 10`, sauf les vérifications locales d'empreintes et les lectures de registres.

## 0. Pièces et contrôles d'intégrité

- Consigne `consigne-audit-A9-seconde-course-v1.md` : son compagnon est conforme.
- Texte v2 scellé : `/home/user/ideation-organism/orchestrator/prereg/preenregistrement-attaque-goodhart-v3-v2.md`. sha256
  recalculé `2a29f59353ce776f92d17799de25f8b75741f1c60dcc5edfbc427bf0ae3a8bb1`, égal à son compagnon et au fichier du commit public
  `4848ad97`. Lu : sections 0.5, 8 (règle d'admission, et paragraphe « Seconde course (v2) », points (1) à (4)) et 13 (points 7,
  7 bis, 7 ter, 9).
- Code lancé : `demonstrations/attaque_goodhart_v3.py` et `pole/attaque_goodhart_v3.py` à `4848ad97` sont identiques à ceux de
  `9776ed0` (le diff entre ces deux commits est vide pour ces deux fichiers). Les fins du lanceur sont relues à `4848ad97` (section 3).
- Modèle de forme : l'audit de la première course,
  `/home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/a1-v3-seconde-course-v1/audit-A9-a1-v3-premiere-course-v1.md`.
  Son compagnon est conforme.
- Rapport de la fille `rapport-fille-A-B-C-2026-11-04-0528.md`, sha256 `b72319837030eb728e3f146fd2d1edc1ec42a5b70b91becc1a48e46ced1e5ac0`,
  et son additif 1, sha256 `a3ec41f666f04797f2209ac221ec790bf4f5cb912c8dada3556dcef29fb8adff`, tous deux sur `origin/canal/fille-2026-11-04`.
  Leurs compagnons sont conformes. Le rapport est identique à `e9917725` et à `8cd6cffd`. L'additif apparaît à `8cd6cffd`
  (05:29:06 UTC). J'ai aussi lu le rapport court `rapport-court-2026-11-04-0153.md` (`1a8bbe7b`), qui recopie le journal de
  lancement jusqu'à 01:53:35 UTC, donc avant le départ.
- Ordres : `docs/procedures/ordre-fille-a1-v3-seconde-v1.md` et `docs/procedures/ordre-fille-neuve-2026-11-04-v1.md`. Leurs
  compagnons sont conformes.
- Registres (copie de travail de `main`) : `registres/decisions.md` R-1456, R-1462, R-1463, R-1464, R-1471 et R-1475 ;
  `registres/depenses.md` (ligne du 4 novembre 02:03 → 03:46) ; `registres/go.md`, lignes GO-2026-11-03-01 (l. 221) et
  GO-2026-11-04-06 (l. 244).
- Branche de données : `refs/heads/donnees/attaque-goodhart-v3-a1v3-seconde-interrompue-v1`. `git ls-remote` donne `cef64e67…`.
  J'ai fait le fetch par une refspec explicite, puis lu `git log` (métadonnées), les noms des fichiers et leurs empreintes, ces
  dernières calculées sur les blobs sans en afficher le contenu (section 5).
- Métadonnées du harnais de la session fille `session_01Qi7Gr3s7JVgpRP17VcSyAf`, par les outils de session : événements de limite
  d'usage, de tâche et de démarrage, résultats de tour, et texte des commandes lancées (jamais leurs sorties). Abréviation : **H**.
  C'est la seule source indépendante de la fille et de la mère. Je l'ai ajoutée aux pièces de la consigne et j'en ai lu les
  métadonnées seulement.

## 1. Chronologie (UTC, 4 novembre 2026)

Sources : **RC**, rapport court de la fille (journal de lancement recopié) ; **RF**, rapport de la fille ; **AD**, son additif ;
**H**, harnais de la session fille ; **R-n**, registre des décisions ; **B**, branche de données (git) ; **E**, empreinte d'un
fichier de l'état scellé confrontée à une valeur attendue (section 5).

| Heure | Source | Fait |
|---|---|---|
| 01:45:50 | RC | clone public à `4848ad97`, `status --porcelain` vide ; texte `2a29f593…` égal à son compagnon ; registre des GO servi = `registres/go.md` de `canal/conv-audit-n04` à `6da2b577`, sha256 `8223230c…` ; empreintes de la configuration `e5306c47…`, de la commande `221df610…`, du registre `8ba92066…` et de `collisionneur_v7.py` `c9725f02…` |
| 01:46:05–02:02:45 | RC, RF, H | témoin de garde : `sleep 900` (PID 1985), relevés toutes les 110 s, fin détectée à 02:02:45 |
| 01:48:45–01:48:52 | RC | relais Argon temporaire de contrôle (port 8815, PID 2695) : un appel, code 0, 0,00064 USD, puis arrêt par PID |
| 01:49:27–01:49:29 | RC | port 8805 libre ; relais de course 8805 lancé, PID 2885, `--plafond-usd 410 --max-appels 9000`, aucune reprise interne |
| 01:49:38–01:49:39 | RC | `--verifier-seulement` : code 0, « conforme », mode course, Argon seul, `plafond_usd` 400, `duree_max_s` 259 200, GO-2026-11-03-01 |
| 02:02:54 | H (commande) | lancement : `nohup setsid env -i … nice -n 10 python3 -I -B demonstrations/attaque_goodhart_v3.py …/sortie-attaque-goodhart-v3 … --go GO-2026-11-03-01 > …/lanceur-sortie-a1-v3-seconde.txt 2>&1 < /dev/null &` ; PID relevé par `/proc/<pid>/cmdline` et écrit dans `lanceur.pid` |
| ≈ 02:03:0x | RF, R-1456, H (message de 02:03:27) | départ ; lanceur 4322, relais 2885, guetteur 4406 ; garde de session sur 4322 |
| 02:03:17 | H | garde de session lancée comme tâche suivie par le harnais (`garde_session_v1.sh 4322 … lanceur-periode1`, délai 7 200 000 ms) |
| 02:04:34 | RF | tâche C (collisionneur sans Argon) lancée |
| 02:04:20 | H | limite d'usage de 5 heures du compte : « allowed », utilisation 0,75 |
| 03:04:49 | RF | fin de la tâche C, code 0 |
| 03:04:52–03:04:53 | H | notification de fin de la tâche C, nouveau tour de la fille : **refusé**, erreur 429 « You've hit your 5-hour limit · resets 5:20am (UTC) » ; limite « rejected », utilisation 1. À partir d'ici, plus aucun tour de la fille ne peut aboutir |
| 03:13, 03:38 | RF | alertes du guetteur (échecs passagers du relais) |
| 03:44:11 | RF, AD | dernier relevé de la garde : lanceur 4322 vivant (« 01:41:14 écoulées » à la ligne de 05:23 du journal, selon la commande de la fille) |
| 03:45:18 | RF, AD, **E** | dernier appel du relais (champ `quand_utc` du dernier appel, confirmé par empreinte : section 5) |
| ≈ 03:46:01 | (déduit) | relevé suivant de la garde, attendu 110 s après 03:44:11 : **jamais écrit** selon RF (« dernier relevé 03:44:11 ») |
| 03:46:39 | H | `turn_handoff_available`, `worker_epoch` 2 |
| 03:46:40 | H | **tâche de garde arrêtée par le harnais** : « Stopped by a worker restart: …garde_session_v1.sh 4322 … », statut « stopped », raison `worker_restart` ; nouvelle initialisation |
| 03:46:43 | H | reprise du tour interrompu (`interrupted_turn`) : 429, même message de limite |
| 03:46:43 → 05:22:58 | H | aucun tour et aucune commande de la fille (la limite reste « rejected » jusqu'à 05:20) |
| 05:20:00 | H | remise à zéro annoncée de la limite (`resetsAt` 1793769600) |
| 05:22:53 | RF | démarrage du conteneur (`uptime -s`, constat de la fille) |
| 05:22:58 | H | `turn_handoff_available`, `worker_epoch` 3, initialisation |
| 05:23:09 | H (commande) | constat : `ps` sur les processus de la course, du relais, du guetteur et de la garde ; `tail` du journal de lancement et du journal du guetteur |
| 05:23:34 | H (commande) | compteurs calculés sur le journal du relais, écrits dans `compteurs-relais-apres-interruption.txt` ; trois lignes ajoutées au journal de lancement (interruption, compteurs, « aucune relance … sortie non lue ») |
| 05:23:52 | H (commande) | ligne « scellement » au journal, puis liste `EMPREINTES-sortie-a1-v3-seconde-interrompue-v1.txt` (tous les fichiers du dossier, `*.verrou` exclu) et son compagnon |
| 05:26:12 | H | alerte de la fille à la mère |
| 05:26:36 | B | commit `cef64e676ec50cd300dfd3c07c23f8b6041998e2` (parent `bfc077b6`) : « … interrompue par l'infrastructure : état scellé avant lecture » |
| 05:26 | R-1463 | consignation par la mère |
| 05:28:20, 05:29:06 | B | rapport (`e9917725`) et additif (`8cd6cffd`) sur `canal/fille-2026-11-04` |

Cohérence des sources. Les heures de RF, AD, R-1456, R-1462 et R-1463 concordent entre elles et avec H. Il y a deux nuances.
(i) « Coupée par la limite d'usage vers 03:46 » (AD, R-1462, texte v3) : selon H, la limite bloquait les tours de la fille dès
03:04:53, et l'événement de 03:46 est un redémarrage du processus de travail de la session (`worker_restart`). (ii) Le texte de la
fille de 05:28 et le message du commit de données disent « conteneur redémarré vers 03:45 », alors que RF dit « démarrage 05:22:53 ».
Les deux s'accordent avec H, qui montre deux redémarrages (03:46:39 et 05:22:58), le disque `/home/user` survivant à chacun.
Aucune contradiction sur les faits qui fondent la cause.

## 2. Cause

- **Les processus ont disparu ensemble, avec l'hôte.** La garde, processus distinct du lanceur, écrit un relevé toutes les 110 s
  et l'aurait écrit à la mort du seul lanceur. Elle n'a rien écrit après 03:44:11, et le harnais l'a déclarée « arrêtée par un
  redémarrage du processus de travail » à 03:46:40. Le relais n'a plus servi d'appel après 03:45:18. À 05:23, ni le lanceur, ni le
  relais 2885, ni le guetteur 4406 ne vivaient (RF). Une mort du seul lanceur (exception, mémoire) aurait laissé la garde l'écrire
  à ≈ 03:46:01.
- **Contexte établi par le harnais.** La session fille était bloquée par la limite d'usage de 5 heures du compte depuis 03:04:53
  (refus 429 à 03:04:53 et à 03:46:43, remise à zéro à 05:20). Son processus de travail a redémarré à 03:46:39 puis à 05:22:58,
  c'est-à-dire juste après la remise à zéro. Que la limite ait *causé* le redémarrage de 03:46 est vraisemblable : il tombe dans la
  fenêtre bloquée, et le redémarrage suivant suit la remise à zéro de près. Ce n'est pas prouvé : aucun événement ne nomme la
  raison du redémarrage. Dans les deux cas, la cause est l'infrastructure (l'hôte), pas l'instrument.
- **Ni l'instrument, ni le proposeur, ni une règle décidée pendant la course.**
  - Le lanceur n'a écrit ni trace d'exception ni aucune de ses sorties (section 3).
  - Les cinq échecs du relais étaient passagers (RF). Sous v3.1, avec `relais_perdu_h: aucun`, ils sont attendus et ne mènent
    jamais à un arrêt (section 8 du texte, « Aucun arrêt sur relais »).
  - La dépense (48,5 USD) et la durée (≈ 1 h 42) sont loin du plafond (400 USD) et de la durée maximale (72 h). Aucune
    `ArretAttaque` n'a donc pu se produire, et une `ArretAttaque` aurait écrit `attaque-goodhart-v3.json`, qui n'existe pas.
  - Personne n'a envoyé de signal. Entre 02:05 et 05:23, H ne montre aucune commande de la fille. Le guetteur, par la règle
    acceptée, n'arrête jamais rien. Aucun mot de Lazar ni aucun arrêt n'est consigné (R-1456 à R-1464).
- **Bornes de l'instant.** La mort a eu lieu après 03:45:18 (dernier appel servi) et, pour la garde, avant ≈ 03:46:01. Le harnais
  l'a vue à 03:46:39–40. Comme les trois processus sont morts ensemble, le lanceur est mort entre 03:45:18 et ≈ 03:46:01, ou au
  plus tard au redémarrage de 03:46:39. Je ne peux pas resserrer davantage sans lire le registre de dépense ni le journal du
  guetteur (section 8).

## 3. Code de sortie

- **Aucun code de sortie, ni écrit, ni capté.** Le lanceur a été détaché sans enveloppe qui écrive son code (écart déclaré par la
  fille à 02:03, R-1456).
- **Aucune des fins prévues n'a eu lieu.** La sortie standard et la sortie d'erreur du lanceur sont redirigées vers
  `lanceur-sortie-a1-v3-seconde.txt` (commande de 02:02:54). Ce fichier, dans l'état scellé, a pour sha256
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` : il est **vide**. Or, à `4848ad97` (identique à `9776ed0`),
  chaque fin écrit dans ce fichier :
  - code 2 : `refus : …` sur la sortie d'erreur (`demonstrations/attaque_goodhart_v3.py:562-567`), avant le manifeste ;
  - code 3 : `attaque-goodhart-v3.json` scellé (`:618`) et résumé JSON sur la sortie d'erreur (`:619-621`) ;
  - code 0 (mode course) : `attaque-goodhart-v3.json` (`:640`) et résumé sur la sortie standard (`:641-646`) ;
  - exception non rattrapée : trace sur la sortie d'erreur.
- **Le manifeste prouve que la course a dépassé le code 2.** La sortie scellée contient `manifeste.json` (écrit à `:592`, après la
  branche du code 2 et avant `jouer_tout`, `:607`) et le registre de dépense, mais **aucun `attaque-goodhart-v3.json`** (noms des fichiers
  de la branche, section 5).
- **Portée de l'écart d'enregistrement : nulle sur la conclusion.** Une enveloppe lancée dans le même conteneur serait morte avec
  lui et n'aurait écrit aucun code. L'absence de toute sortie dans `lanceur-sortie-…` suffit à établir la fin hors des codes 0, 2
  et 3. L'écart reste un écart à consigner : l'ordre ne demandait pas d'enveloppe, mais R-1456 annonçait « le code sera pris de
  son état final » ; l'état final n'en porte aucun.

## 4. Dépense

- **48,49583 USD au relais pour 620 appels** (615 « OK », 5 « ECHEC »), dernier appel à 03:45:18Z. Ce chiffre est établi dans
  l'état scellé lui-même, par empreinte. À 05:23:34, la fille a écrit `compteurs-relais-apres-interruption.txt` (son programme : le
  plus grand `depense_cumulee_usd` du journal du relais, selon le texte de la commande dans H). Ce fichier a pour sha256
  `11c13fe40ba6d7c0ba99a3456416f019f7af250bdeb11e7e4ad279db94ab5a03`. C'est exactement l'empreinte de la chaîne
  `appels journalisés 620 ; statuts {'OK': 615, 'ECHEC': 5} ; dépense cumulée relais 48.49583 USD ; dernier appel 2026-11-04T03:45:18Z`
  suivie d'un saut de ligne. J'ai construit cette chaîne avec les chiffres de RF et le format de la commande, puis je l'ai hachée.
  Je n'ai pas lu le fichier.
- Contrôle hors course : 0,00064 USD sur le relais temporaire 8815 (RC). Total sous GO-2026-11-03-01 : 48,49647 USD (RF ;
  `registres/depenses.md` donne 48,49583 USD pour la course).
- **Non apparié au registre de dépense de la sortie** (`registre-depense-cumulee-v1.jsonl`, sha256 `5d9d2cbc…`) : la consigne en
  interdit la lecture. L'audit de la première course avait fait cet appariement appel par appel. Ici, le chiffre repose sur le
  journal du relais, confirmé par l'empreinte ci-dessus.
- **Borne.** Le relais sert sur un seul fil, donc au plus un appel était en vol à la mort. Le relais ne journalise un appel qu'à
  sa fin : un appel en vol ne figure pas dans les 48,49583 USD et serait au plus égal au pire cas réservé par appel
  (`budget_appel_usd` 1,8 USD, vérification de 01:49:39). La dépense réelle est donc comprise entre 48,49583 et ≈ 50,30 USD. Seule
  la facturation du fournisseur dirait si un appel était en vol.
- Plafond 400 USD loin ; aucun appel après la mort. Aucune commande de la fille entre 02:05 et 05:23. Après 05:23, ses commandes
  (lues dans H jusqu'à 08:31) ne relancent ni le relais, ni la commande d'Argon, ni le lanceur. La seule occurrence de
  `commande_argon` est le `ps` du constat de 05:23:09.
- Hors du plafond de GO-2026-11-04-06, comme le dit la v3 (section 0.5 bis).

## 5. État scellé

- Branche `donnees/attaque-goodhart-v3-a1v3-seconde-interrompue-v1`, commit `cef64e676ec50cd300dfd3c07c23f8b6041998e2`
  (05:26:36 UTC), seul commit propre à la branche (parent `bfc077b6`, de `main`). Il ajoute 21 fichiers sous
  `donnees/attaque-goodhart-v3-a1v3-seconde-interrompue-v1/` : les 19 de la liste, la liste et son compagnon.
- Liste `EMPREINTES-sortie-a1-v3-seconde-interrompue-v1.txt` : sha256 recalculé sur le blob,
  **`fd66feb72b46b6a088c2d01b9d6aaefe38ef151713e8eee6cba7b8e4e863dae0`**, égal à l'empreinte attendue et à son compagnon (ce que
  j'ai affiché du compagnon se limite à des lignes « empreinte nom »). La liste compte 19 lignes, toutes au format « empreinte
  nom » (j'ai affiché ces lignes à travers un filtre de format ; aucune ligne hors format). Les **19 empreintes sont égales, une à
  une, à celles des blobs du commit**.
- Fichiers (noms seuls) : `ALERTE-statuts` (vide, `e3b0c442…`) ; `compteurs-relais-apres-interruption.txt` ;
  `controle-argon-relais-temporaire/` (4 fichiers) ; `guetteur-a1-v3-seconde-v1.log` ; `guetteur.pid` ;
  `journal-lancement-a1-v3-seconde-v1.log` ; `lanceur-sortie-a1-v3-seconde.txt` (vide) ; `lanceur.pid` ; `registre-go.md` ;
  `relais-argon-journal-a1-v3-seconde.jsonl` ; `relais-argon-sortie-a1-v3-seconde.txt` ; `relais.pid` ;
  `sortie-attaque-goodhart-v3/manifeste.json` (+ `.sha256`) ; `sortie-attaque-goodhart-v3/registre-depense-cumulee-v1.jsonl` ;
  `verification-sortie.txt`. **Aucun fichier de résultat.**
- Vérifications par empreinte, sans lecture :
  - `lanceur.pid` = sha256 de « 4322\n », `relais.pid` = « 2885\n », `guetteur.pid` = « 4406\n ». Ce sont les identifiants de
    RF, et le fichier du guetteur porte bien son identifiant (le défaut 1403/1405 de la première course ne se répète pas).
  - `registre-go.md` (`8223230c…`) = `registres/go.md` de `canal/conv-audit-n04` à `6da2b577`. Ce registre porte
    GO-2026-11-03-01 une seule fois (l. 79), ligne identique octet pour octet à la l. 221 de `registres/go.md` de `main`.
- Moment du scellement : la liste a été calculée à 05:23:52, après les dernières lignes ajoutées au journal de lancement (05:23:34
  et 05:23:52). Celles-ci sont donc dans l'état scellé, contrairement à la première course.

## 6. Règle de la section 8 appliquée point par point

Règle (texte v2, section 8) : « une seconde course est une course nouvelle ; elle n'est admise qu'après un arrêt d'infrastructure
(…) ou après une fin de course sans lecture utile pour une cause d'infrastructure établie par l'audit A9 — (…) arrêt du lanceur
hors de ses codes 0, 2 et 3 (exception, signal) (…) —, sur un texte nouveau et un GO nouveau, et elle est rapportée avec la course
arrêtée ou non lue ». Le paragraphe « Seconde course (v2) », point (3), ajoute : « toute fin de l'hôte avant celle du lanceur est
un arrêt d'infrastructure de plus (…) : rien n'est relancé sous ce texte, l'état est scellé tel quel (…) ; une troisième course
demanderait encore un texte neuf et un GO neuf, sous la règle ci-dessus ».

Les cinq points que l'audit doit établir (v2, section 0.5 ; v3, section 0.5 bis) :
1. **Fin hors des codes 0, 2 et 3 : établie.** Manifeste présent, `attaque-goodhart-v3.json` absent, sortie du lanceur vide
   (section 3).
2. **Cause d'infrastructure, non l'instrument, ni le proposeur, ni une règle décidée pendant la course : établie.** Les processus
   sont morts ensemble, avec l'hôte ; le harnais a consigné `worker_restart` à 03:46:40 ; la session était sous limite d'usage
   depuis 03:04:53 ; aucun arrêt n'a été décidé, aucune `ArretAttaque` n'était possible (section 2).
3. **Dépense : établie, appariée au journal du relais seulement.** 620 appels et 48,49583 USD sont confirmés dans l'état scellé
   par empreinte, avec au plus un appel en vol non compté (≤ 1,8 USD). L'appariement au registre de dépense de la sortie n'est pas
   fait, la consigne interdisant de le lire (section 4).
4. **Rien lu ni relancé : établi pour la sortie, autant que H le montre.** Les commandes de la fille (02:05 → 08:31) ne lisent ni
   le manifeste, ni le registre de dépense, ni aucun fichier de résultat, et ne relancent rien. Ce que la fille a lu (journal de
   lancement, journal du guetteur, journal du relais pour les statuts et la dépense, taille du dossier par `du`) est ce que la
   section 0.5 bis de la v3 et l'audit de la première course admettent. Le scellement précède toute autre lecture.
5. **Portée de l'écart d'enregistrement du code de sortie : nulle sur la conclusion** (section 3).

Conditions de la course suivante :
- **Arrêt ou fin sans lecture utile pour une cause d'infrastructure établie par l'audit A9 : satisfaite** par cet audit.
- **Texte nouveau : en cours, non satisfaite à cette heure.** Le texte v3 est au brouillon 1 (sha256 `6e65136a…`, compagnon
  conforme). Il porte deux marqueurs (AUDIT_A9_SECONDE ; COMMIT_LANCEUR_DURABLE, deux fois) que le lanceur refuse tant qu'ils
  restent. Il lui reste la contre-lecture n° 4, le scellement, le commit et la poussée avant la course.
- **GO nouveau : satisfaite.** GO-2026-11-04-06 est à la ligne 244 de `registres/go.md` (`main`, copie de travail) : calcul,
  400 USD, 2026-11-04, échéance 2026-11-18, par Lazar, sur son « mot de Lazar dans cette session, 4 novembre 2026, vers 07:05 UTC,
  verbatim : « go pour tes recos sur A1-v3, SPARKS et juges » ». La ligne est identique octet pour octet (sha256 de la ligne
  `785dab40…`) sur `canal/conv-audit-n04` à `0aa04b5c`, où elle figure une seule fois. Aucune révocation ne la nomme.
- **Rapportée avec les courses arrêtées : prévue** par la v3 (section 0.5 bis, « Règle de lecture »), avec la première et la
  seconde, jamais seule, et avec A1.
- **Rien relancé sous la v2 : tenu** (section 4).

Conclusion pour le marqueur AUDIT_A9_SECONDE de la v3 : chemin
`docs/notes/ideation-organisme-v1/a1-v3-troisieme-course/audit-A9-a1-v3-seconde-course-v1.md` ; commit et empreinte à remplir par
le directeur au versement (je ne committe ni ne scelle). Texte : « cause d'infrastructure établie : fin hors des codes 0, 2 et 3
(manifeste présent, aucun `attaque-goodhart-v3.json`, sortie du lanceur vide), par disparition de l'hôte — processus de travail
de la session fille redémarré à 03:46:39–40 UTC (garde arrêtée « worker_restart »), session sous limite d'usage de 5 heures
depuis 03:04:53 UTC ; 620 appels, 48,49583 USD au relais (au plus un appel en vol, ≤ 1,8 USD) ; état scellé `fd66feb7…` non
lu, rien relancé ; écart du code de sortie sans portée sur la conclusion ».

## 7. Règles de conduite de la v2 (section 8, « Seconde course (v2) » ; section 13, 7 bis et 7 ter) : constats

- (1) **Hôte gardé vivant : appliqué, mais impuissant.** La garde a été éprouvée sur un processus factice. Elle était suivie par
  le harnais, avec des relevés toutes les 110 s (< 5 min), et armée à 02:03:17 avec un délai de 2 h. La mort (≈ 03:45–03:46) est
  survenue avant l'échéance de ce délai (04:03:17) : le délai n'est pas en cause. La garde tient la session active ; elle ne peut
  rien contre la limite d'usage, qui empêchait tout tour dès 03:04:53, ni contre le redémarrage de 03:46.
- (2) **Observée du dehors : non tenue de fait de 03:04:53 à 05:22.** La fille ne pouvait plus agir. La mère était, elle aussi,
  sous la même limite, commune au compte, depuis ≈ 02:35 (R-1462). La perte a été vue à 05:23, ≈ 1 h 37 après. Les alertes du
  guetteur de 03:13 et 03:38 n'ont pu être lues par personne pendant la course. La phrase de RF « aucune cause durable, donc
  aucun message pendant la course » est donc incomplète : la fille ne pouvait de toute façon envoyer aucun message après 03:04:53.
  Cela ne change rien à l'admission (aucune règle ne fait d'un défaut d'observation un arrêt), mais c'est un fait à rapporter.
- (3) **Fin brutale, acceptée : c'est le cas réalisé.** Le texte la prévoyait.
- (4) **Argon seul : tenu, autant que les pièces le montrent.** Le relais temporaire 8815 a été arrêté par PID à 01:48:52, avant
  le départ. Les tâches A (Astra, finie à 01:47) et C (sans Argon, port 8812) n'utilisaient pas Argon. Aucune autre utilisation
  n'est consignée.
- 7 bis, identifiants pris du processus : tenu (section 5). Hôte nommé : la fille `session_01Qi7Gr3s7JVgpRP17VcSyAf`, qui a
  remplacé la fille de l'ordre v1 (`session_01XJ6Mgq5AWikCJZKnsMkbRZ`, limite hebdomadaire, R-1178) sur l'ordre de la mère
  (R-1453).
- Écarts de nommage déclarés par la fille : branche `…-seconde-interrompue-v1` et liste `…-seconde-interrompue-v1.txt`, au lieu
  de `…-seconde-v1`. Sans effet.

## 8. Ce que l'audit ne montre pas (réserves)

- R1. **Aucun fichier de l'état scellé n'est lu.** Les faits du journal de lancement (relevés de garde, 03:44:11), du journal du
  guetteur (alertes 03:13 et 03:38) et du journal du relais, hors du fichier de compteurs confirmé par empreinte, reposent sur RF,
  AD et R-1463. Je n'ai pas vérifié que le manifeste est un manifeste de départ seul ; par le code, il est écrit avant
  `jouer_tout`.
- R2. **Instant exact de la mort et signal ou gel : indéterminés.** L'instant est borné par 03:45:18 et ≈ 03:46:01, ou au plus
  tard 03:46:39. La borne ≈ 03:46:01 suppose que la garde écrivait exactement toutes les 110 s. Le registre de dépense (dernier
  `debut`) dirait si un appel était en vol ; non lu.
- R3. **Lien causal entre la limite d'usage et le redémarrage de 03:46 : vraisemblable, non prouvé.** Aucun événement du harnais
  ne nomme la raison du redémarrage. Sans effet sur la conclusion : dans les deux cas, la cause est l'hôte.
- R4. **Dépense réelle : 48,49583 USD au moins, ≈ 50,30 USD au plus** (un appel en vol éventuel au pire cas réservé). Seule la
  facturation du fournisseur le dirait. Pas d'appariement au registre de dépense de la sortie.
- R5. **H est une source de métadonnées de plateforme**, lue par les outils de session : je n'ai lu que des événements, des
  résultats de tour et le texte des commandes, jamais leurs sorties. Les commandes antérieures à 01:53 et les sous-agents
  éventuels de la fille ne sont pas lus. Entre 02:05 et 05:23, H ne montre aucune commande.
- R6. Le fichier verrou du dossier de sortie (`*.verrou`), s'il existait, est exclu de la liste et de la branche par la fille
  (commande de 05:23:52). Dans la première course, il était vide. Sans effet.
- R7. Faits du texte v3 brouillon 1 (section 0.5 bis) à préciser, sans changer la règle :
  - « coupée par la limite d'usage vers 03:46 » : la limite bloquait depuis 03:04:53 ; 03:46:39 est le redémarrage du processus
    de travail ;
  - « durée jusqu'au dernier appel : ≈ 1 h 43 » : de ≈ 02:03:0x à 03:45:18, c'est ≈ 1 h 42 ;
  - la garde a été arrêtée par le harnais (`worker_restart`), fait que le texte ne cite pas.
- R8. Leçon pour la troisième course (fait, non règle) : la limite d'usage est commune au compte. La mère, la fille et les
  sous-agents l'ont atteinte ensemble (R-1462). Un hôte durable indépendant des sessions (v3) supprime la cause ; il ne supprime
  pas l'observation suspendue tant que la limite dure : la machine devra se garder, se sceller et se détruire seule, comme la v3
  le prévoit.
