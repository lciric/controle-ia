# Contre-lecture (R2) du brouillon 12 du préenregistrement de T0.7 — v1

- Écrite le 2026-11-08 (après 19:00 UTC) par un contre-lecteur neuf (Claude Fable 5.1, `claude-fable-5-1`, sous-agent de
  la session mère), qui n'a écrit aucun des brouillons 1 à 12, aucune des contre-lectures cl1 à cl4, ni le module
  `src/controle_ia/t07/`, ni le rapport du développeur. Modèle autre qu'Opus 5.5 (N-052 : les passages neufs du brouillon 12
  sont d'Opus 5.5).
- Objet : `brouillons/T0.7-sondes-v0-v1-brouillon12.md`, empreinte **vérifiée** par `sha256sum` :
  `718e8955307e5a2bdf64765f8ebde83ae72d19b65b2c67748f2821e534fad892` ; contre le brouillon 11
  `brouillons/T0.7-sondes-v0-v1-brouillon11.md`, `b833d7ccd916b1889e24635303a92cb37a95885346c30c93da27b41064816ef3` (vérifiée).
- Méthode : `diff -u` entre les deux brouillons (641 lignes de diff, lues en entier) ; relecture en profondeur des seuls
  passages changés et de ceux qui en dépendent (table « du 11 au 12 », l. 20-28 ; Règle « mots et coût » ; Plan, étape B ;
  Critères, entrées et table des lignes ; Liste d'arrêt ; Lignes de registre ; Module ; Concordance ; Reste ; Marqueurs).
  Lus aussi : `docs/notes/g0-deux-semaines-v1/rapport-module-t07-v2.md` (sections 4 et 5),
  `brouillons/T0.7-sondes-v0-v1-brouillon12-pieces/grille_l_t07_brouillon12.py` (`f31ffa9d…`, vérifiée) et sa sortie
  `grille-l-t07-brouillon12.txt` (`71295a9b…`, vérifiée), `diff` des deux scripts (11 et 12), `src/controle_ia/sondes/evaluation.py`
  (`plancher_apparie`, l. 66-82, et `comparer_au_plancher`, l. 85-99), `src/controle_ia/premier_test_ia/figees.py`,
  `registres/decisions.md` lignes R-679 et R-1916. Pour répondre à la question 1 et à la question 3, j'ai aussi ouvert
  l'index du fichier `donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz` (empreinte `701f73bd…` égale au compagnon ;
  lecture des métadonnées seules, aucun score d'organisme) et les fonctions `ecrire_resultat` (`src/controle_ia/manifeste.py`
  l. 128-139) et `etape_b` (`src/controle_ia/t07/lecture_v1.py` l. 628-716) du module.
- Interdits respectés : aucun fichier de `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`
  lu ; aucune variable d'environnement ni clé lue ; suite complète des essais non lancée ; aucun commit ; aucun autre fichier
  modifié.

## Verdict

**Scellable après corrections.** Un constat bloquant (la relance d'une lecture « suspendue » n'est pas spécifiée alors que le
brouillon 12 rend ce cas atteignable par un simple décalage de calendrier, et le module refuse d'écraser `lecture-t07.json`),
trois constats majeurs, dix constats mineurs. Aucune contradiction interne entre les écarts de forme alignés ; la grille est
rejouée à l'identique ; la réutilisation des planchers de P3 est valide.

Compte : **1 bloquant, 3 majeurs, 10 mineurs.**

## Réponses aux six questions

### Question 1 — réutilisation des 200 directions plancher de P3 : valide, sans dépendance aux résultats de P3

- **Vérifié sur disque** : `sondes-figees-legeres.npz` (`701f73bd…`, compagnon conforme) porte 424 sondes : 24 sondes de
  P3 (dont les deux principales `tromperie-difference_moyennes-c15` et `enjeux-lineaire-c15`, nommées dans
  `meta.principales`) et 400 sondes de famille `plancher`, toutes `SondeLineaireJetons`, couche 15, agrégation « max », un seul
  tableau `w` (4096 valeurs, double précision) et un biais `b` ; `meta.planchers.tromperie` et `meta.planchers.enjeux` listent
  200 noms chacun, de `<principale>-plancher-plancher-0` à `-199`. Ce que dit le texte (l. 636-641) est exact.
- **Validité du plancher apparié** : dans `plancher_apparie` (l. 72-81), les directions sont tirées une fois, w = L z avec L la
  racine de Cholesky de Σ (covariance des jetons d'entraînement, plus 10⁻⁹ sur la diagonale), b = −wᵀμ ; le plancher
  d'une lecture n'est pas ces directions mais **le quantile 0,95 de leurs aires sur le jeu d'évaluation** (`comparer_au_plancher`,
  l. 94-95). Réutiliser les directions de P3 revient donc à garder le même échantillon de 200 tirages de N(0, Σ) et à
  recalculer le quantile sur les épisodes de 7b : c'est exactement la recette A6 (2), la covariance étant celle des jetons
  d'entraînement de la sonde (inchangés, sondes figées), pas celle du jeu lu. Aucune raison statistique de retirer des
  directions neuves.
- **Dépendance aux résultats de P3** : aucune par sélection. Les 400 directions ont été tirées et figées « avant le premier
  épisode » (en-tête de `figees.py`), toutes gardées (200 sur 200, aucune choisie d'après une aire). Il n'y a donc aucun
  chemin par lequel l'issue de P3 (ou son verdict) aurait façonné ces directions.
- **Ce qui est partagé, et qu'il faut déclarer** : le bruit d'échantillonnage des 200 tirages. Si, par hasard, ces 200
  directions sont « faibles » ou « fortes » dans la covariance, T0.7 hérite du même aléa que P3. Pour T7-P1 (réplication de
  P3-P3 sur des épisodes neufs) c'est plutôt souhaitable, mais la phrase « elles gardent […] **le même plancher que P3** »
  (l. 644) est inexacte : ce sont les **mêmes directions**, le **quantile** est recalculé sur 7b (constat m-02).
- **Formulation fausse à corriger** : « égal au fichier complet `91b61c45…` régénéré au bit près, R-679 » (l. 637-638). Un
  fichier d'empreinte `701f73bd…` n'est pas égal « au bit près » à un fichier d'empreinte `91b61c45…`. R-679 dit : le fichier
  complet **régénéré** retrouve le sceau `91b61c45…` ; le fichier léger porte 424 sondes sur 424, écart maximal 0,0,
  empreintes de sondes toutes égales ; `meta.complet` du fichier léger vaut `91b61c45…` (constat m-01).

### Question 2 — refus (code 2) sans l'audit des fuites ; audit sur tous les jeux décisifs avant l'étape B

- **Cohérent avec la grille** : F garde ses quatre valeurs (grille (2) inchangée, 55 296 cas) ; le refus a lieu avant toute
  ligne (« aucune ligne de la grille n'est atteinte sans F », l. 977), donc aucune zone morte n'apparaît ; F = (ii) exige une
  dose **jugée**, dérivée au point 4 bis avant le point 4 ter (l. 880-895), ordre correct ; sous Q ∈ {absente, non calculable,
  incohérent}, F(ii) vaut nécessairement « aucune » et la fuite est rapportée (l. 895-896) : cohérent avec L7b, L7c, L1b.
- **Cohérent avec R5** : un refus à code 2, motif imprimé, est le même traitement que celui des autres clés exigées
  (`SCORES-T07`, `SONDES-T07`) ; F « jamais supposée » est bien la lecture non silencieuse. Je ne vois pas de repli.
- **Réalisable dans l'ordre** : l'audit porte sur les textes et mesures de T0.6 (`textes-actions-t06.jsonl`,
  `mesures-t06.npz`, entrées de ce texte) qui existent dès `RUN-CONFIRMATION-T06`, donc avant l'étape A ; la clé est permise
  à l'étape A et exigée à l'étape B (l. 1226-1229) ; aucun score de T0.7 n'est ouvert avant l'étape B. L'ordre tient.
- **Ce qui manque (M-1)** : le texte fixe la **liste des traits à relire** (longueur, position, texte de l'indication, coût ;
  prédicteurs triviaux, l. 1030, 1034, 1249) mais **aucune règle de décision gelée** pour écrire `"fuite": "<fuite nommée>"`
  plutôt que `null`. Au brouillon 11, l'audit n'était déclenché que par R7/R9 et son issue nourrissait une réserve ; au
  brouillon 12, l'audit devient la **source unique d'une entrée décisive**, appliquée **sans condition** aux cinq jeux
  décisifs, et son issue commande directement L6 (nœud) ou la première phrase de L1b. Un jugement d'un sous-agent sans critère
  gelé devient ainsi une entrée de la grille : c'est un écart à R1 (critères de lecture gelés). Il faut aussi distinguer la
  « fuite » (artefact de construction du jeu qui porte l'étiquette) du « prédicteur trivial » (qui nourrit l'état N par une
  règle déjà gelée) : la ligne 1249 range « prédicteurs triviaux » dans l'audit, ce qui ferait compter deux fois la même
  chose (une fois en F → L6, une fois en N → L5).

### Question 3 — lignes « permises » : reste-t-il une phrase qui les dit exigées, ou une absence sans issue écrite ?

- **Phrases résiduelles** : aucune dans les sections normatives. Les deux restes sont historiques : table « du 9 au 10 »,
  ligne 4 (l. 134 : « **exigée** à l'étape B ») sans mention « dépassée », et le constat de cl1 (l. 1784, « devenue exigée »),
  qui est un compte rendu d'époque (constat m-06 pour la l. 134).
- **Chemins d'une absence** : `SCELLEMENT-P3BIS` ou `VERDICT-P3BIS` absente → L0a écrite (l. 870, 1009, 1052-1053, 1230,
  1384) ; `ISSUE-MOTS-ET-COUT-T06` absente → L1 écrite (l. 871, 1012, 1230, 1385). Règle d'antériorité conditionnée à la
  présence de `VERDICT-P3BIS` (l. 874-876, 1233-1234) : cohérent. Liste d'arrêt l. 1071-1072 (ouverture des scores sans
  ces lignes = lecture invalide) : cohérent, les scores ne sont pas ouverts sous L0a. Je ne trouve **aucun chemin où une
  absence passe sans issue écrite**.
- **Mais un chemin où l'issue écrite empêche la suite (B-1)** : la ligne L0a (l. 1009) traite l'absence comme le fichier
  illisible ou l'issue « non lu »/« échec » : « lecture suspendue […] ; nœud de Lazar (relance de P3-bis sous son texte) ».
  Pour une ligne **pas encore écrite** (l'étape B lancée avant le verdict de P3-bis, ce que la garde d'ouverture ne refuse
  plus), relancer P3-bis n'a aucun sens : il faut **attendre, puis rejouer l'étape B**. Or le texte ne dit nulle part comment
  une lecture « suspendue » reprend, et le module, tel qu'il est, **ne peut pas** la rejouer : l'étape B lit le manifeste de
  l'étape A (`lecture_v1.py` l. 636-637, même `run_t07`) et `ecrire_resultat` refuse d'écraser `diag/<run-t07>/lecture-t07.json`
  (`manifeste.py` l. 134-135, « R12 interdit d'écraser ») ; la seconde tentative finit en `GardeArret`, la troisième ne peut
  même plus écrire `arret-etape-b.json`. Le même trou existait déjà pour la branche A de L1 (« table A pas encore écrite »,
  l. 1012) au brouillon 11 ; le brouillon 12 l'**élargit** à trois clés et à la ligne L0a, qui dit en plus « nœud ». Sous un
  texte scellé, un simple décalage de calendrier rendrait la lecture de T0.7 impossible sans écart au préenregistrement.

### Question 4 — règle des clés du registre partagé

- **Une clé d'une autre tâche prise pour une clé de T0.7** : seulement si son nom finit par `-T07` ou contient `-T07-` ;
  l'effet est un **refus** (code 2), jamais une lecture : c'est le sens conservateur. `<<CLES_REGISTRE_PARTAGE>>` le vérifie
  **à la date du candidat** seulement (l. 1221-1222) ; une clé écrite ensuite par T0.8 avec cette marque (par exemple une
  clé qui cite un fichier de T0.7) ferait refuser l'étape B. Pas silencieux, mais non prévu : à dire dans la Concordance
  (constat m-10).
- **Une clé de T0.7 prise pour une clé d'une autre tâche (M-2)** : oui, par une faute de frappe **dans la marque**
  (`SCELLEMENT-JEUX-T7-JD`, `SCELLEMENT-JEUX-TO7-JD`, `SCORES-T07A`…). La forme de clé du module (`[A-Z0-9]+(?:-[A-Z0-9]+)+`,
  `registre_v1.py` l. 34) accepte ces noms ; sans marque, ils sont « ignorés et comptés ». Pour une clé **exigée** le mal est
  nul (refus « ligne manquante »). Pour une clé **permise dont la présence fixe une lecture**, le mal est réel :
  `SCELLEMENT-JEUX-T07-JD`, `-JC`, `-JA` fixent `sondes_lues` et déclenchent le **repli des jeux** (l. 1224-1225, 741) ; une
  faute de frappe dans la marque fait tomber la sonde du jeu concerné dans le repli **sans refus**, la seule trace étant le
  compte des clés ignorées dans le manifeste, qu'un humain doit lire. Au brouillon 11, toute clé inconnue refusait et cette
  faute était attrapée. C'est un repli que seule une lecture humaine du manifeste rend non silencieux : au sens de R5, trop
  faible pour une ligne qui change l'ensemble des sondes lues.
- Les clés sans marque lues par T0.7 (`RUN-CONFIRMATION-T06`, `SCELLEMENT-P3BIS`, `VERDICT-P3BIS`, `ISSUE-MOTS-ET-COUT-T06`)
  sont bien nommées une à une (l. 1216-1217) : aucune ambiguïté. Une cellule de clé mal formée → refus (l. 1218-1219) : bon.
  Les minuscules ne passent pas la forme de clé : refus, bon.

### Question 5 — écarts de forme alignés : aucune contradiction interne

- `doses_qualifiees` **liste ordonnée** `S25`, `S50`, `S75`, `S100` : identique dans la Règle (l. 537-539), la ligne de registre
  (l. 1248), le Module (l. 1340, 1387-1388), le script (`liste != qualifiees`, formes `echoue_inverse`). Cohérent.
- **Trois marques** des doses non jugées : L7 (l. 1015), L2 (l. 1020), point 8 (l. 907-908), Seuil (l. 554-559) ; L3 (l. 1021)
  reste générique (« jugée, non jugée ou hors jugement »), ce qui n'est pas une contradiction. Cohérent.
- **`null`** : les sept champs d'une dose non calculable **exigés** `null` ; `etat`, `niveau`, `n_permutations`, `seuil_aire`
  **jamais** `null` ; `effet_cout` `null` partout permis (l. 1248, 1322-1326, 1385-1387). Cohérent entre eux. Une seule
  phrase se contredit elle-même : « valent `null` et **ne sont ni vérifiés** ni recalculés (brouillon 12 : `null` y est
  **exigé**) » (l. 1248) — exiger `null`, c'est vérifier (constat m-04).
- **Valeurs attendues** (200, 0,70, `<<NIVEAU_BASE_T06>>`) → illisible, L1 : énoncé une fois (l. 1248), repris dans le Module
  (l. 1324-1325, 1386-1387) et dans les marqueurs (l. 1880). Le rapport v2 (section 5, point 3) dit que le module recalcule
  l'état avec le `seuil_aire` écrit : le texte le ferme désormais (« ne recalcule jamais l'état avec une valeur autre que la
  valeur attendue ») ; le module doit suivre, l'essai est listé. Cohérent.
- **Champ `aire`** : écart interne, étape 1 de `deriver_classe` (l. 531-533, 1248, 1337-1338), script (`ECART_INTERNE`
  « aire »). Cohérent entre eux. **Fragile sur le fond (M-3)** : « égalité exacte des nombres écrits » suppose que T0.6
  **recopie** dans `aire` le même nombre que `aire_n029` ou `aire_mots_et_cout`. Si T0.6 calcule `aire` par un autre chemin
  (aire sur l'ensemble des épisodes plutôt que moyenne des plis, ou arrondi différent à l'écriture), l'égalité exacte échoue
  sur toutes les doses et T0.7 rend L7c (nœud, scores de (ii) fermés) sur un artefact de forme. La ligne 1248 dit déjà
  « noms à confirmer au texte scellé de T0.6, écart = nœud », mais la Concordance (l. 1500-1502) n'ajoute pas ce point à ce
  qu'elle demande à T0.6.
- Fermeture des scores de (ii) **par Q, L1b comprise** : l. 570-573, 891, 1013, 1355-1357, 1389-1390. Cohérent.
- Phrase de « gain » **non recopiée** : l. 909-913, 1020, 1410-1411. Cohérent.
- Ex aequo : repli porté par le module, règle de T0.6 portée au candidat si elle existe (l. 523-526, 1336-1337). Cohérent.

### Question 6 — script de grille rejoué

- `cd /tmp && python3 -I -B /home/user/controle-ia-travail/brouillons/T0.7-sondes-v0-v1-brouillon12-pieces/grille_l_t07_brouillon12.py`
  → **code 0**, 19 s, sortie **identique octet pour octet** à `grille-l-t07-brouillon12.txt`, empreinte
  `71295a9bc3a415a06652e5bc99754d358ee4a77c6f41cb683e1a3a3f5017b314` (égale à celle du texte, l. 980-981). Effectifs
  retrouvés : 624 ; 55 296 (inchangés par rapport au brouillon 11, mêmes effectifs par ligne) ; 18 439 488 cas sur
  1 041 984 configurations, 7 776 impossibles ; tout à 0 (trous, chevauchements, dépendances de L7/L7b/L7c, sous-phrases,
  priorité de L7b, contrôles du brouillon 12). Les comptes sont justes : 5 × 4 × 4 × 2 × 3⁴ × 3⁴ = 1 049 760, moins
  3 × 4 × 4 × 2 × 3⁴ = 7 776 configurations impossibles.
- `diff` des scripts 11 et 12 : seuls changent la docstring, `ECART_INTERNE` (+ « aire »), `LISTE_ECRITE` (+ « echoue_inverse »),
  `liste_ecrite`, le saut des configurations impossibles (+ « aire »), le compteur `controles_b12` et son impression, la
  condition finale. `regles`, `deriver` (hors docstring), `agreger_doses`, `grille_classes` sont inchangés : la grille (2)
  est bien la même.
- **Les deux contrôles neufs** (l. 239-244 du script) :
  - *Liste à l'envers* : teste ce que le texte dit. `liste_ecrite("echoue_inverse")` donne les doses « échoue » dans l'ordre
    `S100` → `S25` ; `deriver` compare en liste ordonnée ; le contrôle, écrit à part, exige « incohérent » dès que deux doses
    au moins échouent et qu'aucune n'est non calculable (une seule dose « échoue » donne la même liste dans les deux
    ordres, correctement hors du contrôle ; une dose non calculable passe à L7b avant, correctement). Bon.
  - *Écart « aire »* : **tautologique**. « aire » est une **étiquette** de configuration, pas un calcul sur des nombres ;
    `deriver` rend « incohérent » pour toute étiquette d'écart autre que « aucun » (l. 105-106) ; le contrôle vérifie donc
    seulement que l'étiquette est routée vers « incohérent » et que l'énumération couvre le cas. Il ne prouve rien sur
    « `aire` différente de l'aire moyenne de la base décisive écrite » comme comparaison de nombres (celle-ci relève des essais
    R5 du module, listés l. 1385). C'est conforme à la portée déclarée (CLT7D-06 (c)), mais le texte (l. 988-990) présente les
    deux contrôles sur le même plan (constat m-08).

## Constats

Classes : **bloquant** (le texte ne peut pas être scellé tel quel), **majeur** (fausserait ou bloquerait une lecture, à
corriger avant scellement), **mineur** (forme, exactitude d'une citation, précision). Lignes : brouillon 12.

### Bloquant

**B-1 — Relance d'une lecture « suspendue » non spécifiée ; L0a dit « nœud, relance de P3-bis » pour une simple absence**
(l. 1009 ; l. 870-872, 1012, 1052-1053, 1230-1231, 1384-1385 ; module `lecture_v1.py` l. 636-637, 714, `manifeste.py`
l. 134-135). Voir question 3. Depuis le brouillon 12, lancer l'étape B avant `VERDICT-P3BIS` (ou avant
`ISSUE-MOTS-ET-COUT-T06`) écrit et scelle `diag/<run-t07>/lecture-t07.json` à code 0 ; le texte ne dit pas comment la lecture
reprend, et le module ne peut pas la rejouer (R12 sur le même chemin, même `run_t07`). Correction proposée, au choix de la
session mère, à écrire aux lignes 870-877, 1009, 1012, 1230-1231, 1384-1385 et dans la section « Module » :

- (a) **Tentatives versionnées** (garde le choix du brouillon 12) : l'étape B écrit `diag/<run-t07>/lecture-t07-essai-<n>.json`
  (`n` = nombre de tentatives déjà écrites + 1, jamais écrasé), et `lecture-t07.json` **seulement** quand la ligne atteinte
  n'est ni « L0a par absence » ni « L1 par absence ou table A non écrite » ; chaque tentative est journalisée dans
  `<registre>.ouvertures.md` ; aucune tentative n'ouvre `scores-actions-t07.npz` tant que les lignes manquent (déjà vrai) ; la
  lecture décisive reste unique (une seule `lecture-t07.json`). Essai R5 : deux tentatives sous absence puis une complète →
  trois fichiers, les deux premières L0a/L1, la troisième la ligne finale ; artefact : `lecture-t07.json` déjà présent → refus.
- (b) **Retour au refus pour l'absence seule** : `SCELLEMENT-P3BIS`, `VERDICT-P3BIS`, `ISSUE-MOTS-ET-COUT-T06` **absentes** →
  refus, code 2, motif imprimé **et journalisé** dans `<registre>.ouvertures.md` (pas un repli silencieux) ; L0a et L1 ne
  gardent que « fichier illisible, valeur inconnue, non lu, échec » et « table A non écrite » (dont la relance reste à
  spécifier comme en (a) pour la branche A de L1). Plus simple pour le module, mais défait le marqueur 1.

Dans les deux cas, scinder la ligne L0a (l. 1009) : **absence** → « lecture suspendue, en attente de la ligne ; aucune
relance de P3-bis ; aucun nœud » ; **illisible, valeur inconnue, non lu, échec** → « nœud de Lazar (relance de P3-bis sous son
texte) ». Reporter la même scission à la table « du 11 au 12 » (l. 22) et à la Liste d'arrêt (l. 1052-1053).

### Majeurs

**M-1 — L'audit de fuites devient une entrée décisive sans règle de décision gelée** (l. 1249 ; l. 892-896, 973-977, 1017,
1030-1035). Voir question 2. Correction : (i) écrire dans la ligne `AUDIT-FUITES-T07` la **définition gelée** d'une fuite
nommée, par exemple : « un trait de construction du jeu, parmi longueur de l'action, position du jeton noté, texte de
l'indication, champ `COST`, qui à lui seul permet de retrouver la condition : présence d'un texte dans une condition et pas
dans l'autre (extrait cité, compte par condition), ou séparation des deux conditions par ce seul trait avec une aire ≥ 0,70
sur les textes et mesures de T0.6 (nombre écrit) ; tout autre constat est une réserve, pas une fuite » ; (ii) retirer
« prédicteurs triviaux » de l'audit (ils nourrissent l'état N par une règle gelée ; les laisser dans F compterait deux fois le
même fait, L6 avant L5) ou dire explicitement qu'un prédicteur trivial n'est pas une fuite ; (iii) fixer que la **consigne de
l'audit** (fichiers lus, traits, règle, format) est scellée avant l'audit, que l'auditeur est un sous-agent neuf qui n'a lu
ni `sondes-t07.json` ni aucun score, et que son fichier est contre-lu (R2) avant la ligne de registre ; (iv) ajouter
« `"fuite"` : `null` ou chaîne non vide ; `"motif"` : chaîne non vide ; toute autre forme → illisible ».

**M-2 — Une faute de frappe dans la marque `-T07` d'une clé permise déclenche le repli des jeux sans refus** (l. 1212-1222,
1224-1225, 741). Voir question 4. Correction (au choix) : (a) n'ignorer que les clés qui portent la **marque d'une autre
tâche connue** (`-T06`, `-T08`, `-P3BIS`, liste fixée au candidat par `<<CLES_REGISTRE_PARTAGE>>`) et **refuser** toute clé qui
ne porte aucune marque reconnue ; ou (b) refuser toute clé ignorée dont le nom, la marque retirée, **égale** le nom d'une clé
de T0.7 la marque retirée (`SCELLEMENT-JEUX-*-JD` → refus) ; et dans tous les cas (c) écrire dans le manifeste **et** dans
`lecture-t07.json`/`sondes-t07.json` la liste des clés ignorées, avec l'essai R5 « clé `SCELLEMENT-JEUX-T7-JD` présente → refus
(artefact) ». Mettre à jour la phrase « égalité des refus » (voir m-07).

**M-3 — Égalité exacte `aire` = aire moyenne de la base décisive : hypothèse sur l'écriture de T0.6 non demandée à T0.6**
(l. 1248 ; l. 531-533, 1337-1338 ; Concordance l. 1500-1502). Voir question 5. Correction : ajouter à la phrase exigée ou à
l'invitation faite à T0.6 (l. 1500-1502) : « `aire` est **le même nombre** que `aire_n029` ou `aire_mots_et_cout` selon
`base_decisive` (recopié, même arrondi) » ; et prévoir dans la ligne 1248 ce qui arrive si le texte scellé de T0.6 ne le dit
pas (nœud, ou retrait de ce contrôle au candidat, déclaré) plutôt que de laisser une L7c d'artefact possible.

### Mineurs

**m-01** (l. 637-638) « égal au fichier complet `91b61c45…` régénéré au bit près, R-679 » est faux au pied de la lettre (deux
empreintes différentes). Écrire : « fichier léger dont les 424 sondes, planchers compris, sont égales à celles du fichier
complet `91b61c45…` (écart maximal 0,0, empreintes de sondes toutes égales, `meta.complet` = `91b61c45…` ; R-679) ». La même
formule inexacte figure dans R-1916 : le texte ne doit pas la recopier.

**m-02** (l. 644) « le même plancher que P3 » → « les mêmes 200 directions que P3 ; le quantile 0,95 est recalculé sur les
épisodes de 7b ; le bruit d'échantillonnage des 200 tirages est partagé avec P3 (déclaré : T7-P1 réplique la sonde sur des
épisodes neufs, pas le tirage du plancher) ».

**m-03** (l. 634-635) la recette décrite omet le terme de régularisation `+ 10⁻⁹ I` ajouté à Σ avant Cholesky (`evaluation.py`
l. 74) ; comme la même phrase sert de recette aux planchers neufs (l. 647-648), l'écrire.

**m-04** (l. 1248) « valent `null` et ne sont ni vérifiés ni recalculés (brouillon 12 : `null` y est exigé) » : exiger, c'est
vérifier. Écrire : « doivent valoir `null` (vérifié ; autre valeur → fichier illisible) et ne sont pas recalculés ».

**m-05** (l. 1012) « sans issue » dans la lecture de L1, alors que le brouillon 12 insiste sur « issue écrite » : écrire
« sans issue du critère 3 (la ligne L1 et son motif sont écrits dans `lecture-t07.json`) ». Même précision utile à L0a.

**m-06** (l. 134) la ligne 4 de la table « du 9 au 10 » dit encore « **exigée** à l'étape B » sans mention « dépassée par la
table du 11 au 12 » ; les tables historiques portent ailleurs cette mention (l. 127, 153, 186). L'ajouter.

**m-07** (l. 1210-1211, 1439-1440) « essayée contre `controle_lecture_t06_v1.py` […] avec égalité des refus » : depuis le
brouillon 12, une clé inconnue **sans** marque de T0.7 est ignorée par T0.7 et (si le script de T0.6 est bien le modèle du
refus « clé ni exigée ni permise ») refusée par T0.6 ; l'égalité ne tient plus sur cet artefact. Écrire l'exception :
« égalité des refus, hors clé inconnue sans marque de T0.7 (ignorée ici, refusée là) ». Le script de T0.6 n'étant pas sur
`main`, je n'ai pas pu vérifier son comportement : à contrôler au texte scellé de T0.6.

**m-08** (l. 988-990) le contrôle « écart « aire » hors de incohérent » du script est une vérification de routage d'une
étiquette, pas une comparaison de nombres (voir question 6) ; l'écrire dans la portée déclarée : « l'écart « aire » est une
étiquette dans le script ; la comparaison des nombres relève des essais R5 du module ».

**m-09** (l. 1249) le domaine de `"fuite"` et de `"motif"` n'est pas écrit (chaîne vide ? espace ?) ; fixer « `null` ou
chaîne non vide » (repris dans M-1 (iv)).

**m-10** (l. 1221-1222, Concordance l. 1460-1509) la confirmation « aucune clé d'une autre tâche ne porte la marque `-T07` »
n'est faite qu'à la date du candidat ; une clé de T0.8 écrite ensuite avec cette marque (par exemple pour citer un fichier
de T0.7) ferait refuser l'étape B. Ajouter à la Concordance : « T0.6 et T0.8 n'écrivent aucune clé portant `-T07` ou `-T07-` ;
leurs lecteurs de registre ignorent ou permettent les clés de T0.7 (`SCORES-T07`, `SONDES-T07`, `AUDIT-FUITES-T07`, …) ». Le
second point protège aussi T0.6 : si son script refuse toute clé inconnue, les lignes que T0.7 ajoute au registre partagé
feraient refuser la lecture de T0.6.

## Ce que je n'ai pas relu

Le reste du texte (sections inchangées du brouillon 11, contre-lues quatre fois) ; le code du module au-delà des fonctions
citées (`ecrire_resultat`, `etape_b`, forme de clé de `registre_v1.py`) ; le script de T0.6 `controle_lecture_t06_v1.py`
(absent de `main`) ; les données de T0.6 et de P3 au-delà des métadonnées du fichier léger. Aucun chiffre de ce rapport ne
vient de l'état de l'art.
