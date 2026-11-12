# Préenregistrement — porte G0 « prêt pour G1 » : grille de lecture — v4 — BROUILLON

**Brouillon, non décidé.** La v2 a été contre-lue une fois (CL1), la v3 une fois (CL2) ; cette v4 applique tous les
constats de CL2. Rien ici ne s'applique avant : (1) un mot **explicite** de Lazar sur D-G0-1, puis ses décisions sur
D-G0-2 à D-G0-13 ou leur défaut échu (annexe B) ; (2) une contre-lecture R2 de cette v4 par un sous-agent neuf ; (3) le
scellement d'une version sans le mot « brouillon » dans son nom (R12 : la v1, la v2 et la v3 restent telles quelles).

- Auteur : sous-agent neuf (main neuve, lancée le 2026-10-29). Je n'ai écrit ni la v1, ni la v2, ni la v3, ni CL1, ni CL2,
  ni l'un des avis, ni la synthèse du collisionneur, ni aucune des preuves que la grille lit.
- Rédaction : début 2026-10-29 11:33 UTC (`date -u`) ; fin : dernière ligne du fichier. Commit du dépôt au début :
  `8b742e46e7c40dcf45c710ef76b14c49a514aa29`. Clone **superficiel** (`git rev-parse --is-shallow-repository` = `true`).
  Toutes mes commandes sous `LC_ALL=C.UTF-8` (`locale -a` contient `C.utf8`).
- Pièces d'entrée (empreintes recalculées par `sha256sum` le 2026-10-29, égales à leur compagnon `.sha256`) :
  - v3 `prereg/brouillon-G0-grille-lecture-v3.md`, `15e7f229443d80f7625f1f0e16838457125f04dd1c185e1b2caac7442b70e328`
    (non modifiée ; base de cette v4, qui en reprend tout le texte sauf ce que la table ci-dessous change) ;
  - contre-lecture CL2 `prereg/contre-lectures/brouillon-G0-grille-lecture-v3-cl2.md`,
    `2ef445ccb27a1c549cc22e17c1a96e8a5e30572212bec4bae12166697bd778ee` (« CL2 » ci-dessous ; versée par R-780) ;
  - reprises de la v3 sans relecture complète par moi (citées d'après la v3 l. 13-24 ; CL2 l. 4 les a lues) : v2
    `aa47f6fc…`, CL1 `b2282047…`, synthèse repli `docs/notes/porte-g0-repli-v1/synthese-collisionneur-repli-g0-v1.md`
    `527f5853…`, avis Fable repli `f3435cfd…`, avis Fable grille `3c2c8c55…`, avis conv-audit n° 199 `0b31ae24…`.
- Documents qui font foi (`cd docs && sha256sum -c sha256sums-lancement-v2.txt` : trois OK le 2026-10-29 vers 11:39 UTC) :
  - brief v2 `docs/brief-claude-code-programme-complet-v2.md`, `9261932a11f29e8643175bc6e150d5455067f58a3cb1e57dca99e02cb17aa3b2`,
    section 7 « Porte G0 — prêt pour G1 » (l. 190-201 ; recopiées ci-dessous et comparées par `diff` : identiques) ;
  - programme v2 `docs/programme-controle-ia-v2.md`, `2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c` ;
  - `registres/decisions.md` (fichier vivant ; empreinte à 11:39 UTC :
    `95ae6c76c78f7b41a26eba228609e8cb8d4eeb138fa6de1d8876a257a7bcf999`) : l. 34 R-025 ; l. 462 N-027 ; l. 978 **R-750** ;
    l. 993 **R-765** ; l. 1008 R-780 (versement de CL2) ; vérifiées à cette empreinte ;
  - P-007 `docs/decisions/proposition-P-007-plan-G0-v1.md`, `56b9182b035c6f98ea6f1398f9bdd9bc686b9d51bc2d96ea12d6946c09a7a506`.
- **Décisions de Lazar intégrées (fixées, non rediscutées ici)** :
  - **R-750** (l. 978) : « borne du 31 janvier 2027 confirmée par Lazar dans cette session (« 31 janvier : go », ≈ 09:57
    UTC) » ; avec R-765 (« un seul verdict final »), le report est **unique**, au plus tard le 31 janvier 2027.
  - **R-765** (l. 993 ; mot direct de Lazar ≈ 11:03 UTC, consigné ainsi au registre) : « un échec scellé d'un critère pendant le report gèle ce critère jusqu'au
    second verdict ; il ne ferme pas la porte en cours de report. Un seul verdict final au 31 janvier 2027 au plus tard ; un
    critère réfuté par sa liste d'arrêt scellée n'est jamais retenté. »

## Ce que la v4 corrige

« Ligne v3 » renvoie à `15e7f229…` ; « ligne v4 » à ce fichier. Les changements de la v3 sur la v2 restent décrits dans la
v3 (l. 40-68) et sont tous conservés, sauf là où cette table dit le contraire. Les sept constats de CL2 sont **tous
acceptés**, aucun refusé ; les écarts de forme à la correction proposée sont dits dans la colonne et en section
« Contre-lecture ».

| n° | constat (CL2) | ligne v3 | ligne v4 | correction |
|---|---|---|---|---|
| 1 | **CLG2-01** (majeur) : D-G0-13 (a) gèle des négatifs issus des contrôles de la grille sur des critères sans run ; F-8.2 sur chiffre nu produit des faux négatifs | 137, 154, 235-239, 579, 581, 592-596, 679, 765 | @L1@ | défaut de D-G0-13 (a) **restreint** : gel seulement d'un négatif d'une preuve à (α) « présent », issu de sa liste d'arrêt ou de sa table gelée ; les négatifs de M-8.3, F-8.2, F-8.3 restent des négatifs du critère 8 et ne gèlent pas (dit dans la Métrique, le champ (γ), la section 2 et le Repli) ; D-G0-7 dit lui-même son exception pendant le report ; F-8.2 remplacée par le **script M-8.3** (écrit en entier) sur le chiffre **tel que la table l'écrit**, bornes numériques, doute → non concluant ; exécuté (annexe F) : « 0,5 », « 12 », « 8B » nus rendaient 3, 8, 11 négatifs par `grep -F` ; le script rend 0 négatif (0, 4 et 11 doutes) |
| 2 | **CLG2-02** (majeur) : D-G0-13 (b) hors de R-765, contredit D-G0-7 et le précédent T0.4 | 228-234, 765 | @L2@ | défaut de (b) = **règle de D-G0-7** : à la première lecture, seul le négatif par liste d'arrêt est gelé ; un négatif par ligne de table admet une version suivante autorisée avant son run sur cause nommée distincte du résultat, sinon non concluant ; la variante v3 (tout négatif de la première lecture gelé) passe en « autre option » |
| 3 | **CLG2-03** (majeur) : P-015 (b) est une condition en M-3.2 et une réserve en M-3.5 | 389, 395, 398, 410-415, 763 | @L3@ | D-G0-11 : **défaut « condition »** (avis Fable grille, CL2 § 4) ; autre option « réserve » (CL1 § 6) ; M-3.2 et M-3.5 suivent **le même état** sous chaque option (condition : non tenu — invalide ; réserve : réserve pour les deux) ; « date de la première lecture de sonde » rendue mécanique |
| 4 | **CLG2-04** (mineur) : `PRONONCE_1` ne prend pas un prononcé entre guillemets ; un verdict qui cite un prononcé antérieur rend « plusieurs mots » | 311, 317, 792 | @L4@ | `\**` → `[*«" ]*` (motif entre apostrophes simples, à cause du `"`) ; repli mécanique `LARGE_1` : 0 ligne stricte mais au moins une ligne large → non concluant, pas « absent » ; annexe C point 6 : prononcé une seule fois dans le verdict ; exécuté (annexe F) : trois verdicts de T0.4 inchangés, guillemets pris |
| 5 | **CLG2-05** (mineur) : aucun motif d'écart pour une pièce postérieure à un gel | 290-295 | @L5@ | motif **(m4)** « postérieure au gel de D-G0-13 », avec le chemin du verdict de la première lecture et la commande de la section 2 |
| 6 | **CLG2-06** (mineur) : jugements résiduels F-3.4, F-7.2, contrôle de D-G0-2, M-3.3, M-4.4, F-3.1 | 368-369, 396, 399, 402, 438, 550 | @L6@ | un motif ou une commande par contrôle, « non concluant si le motif échoue » écrit dans chaque ligne ; formes exigées ajoutées en annexe C point 6 ; motifs essayés sur données synthétiques et, pour F-7.2, sur le brouillon 5 du papier C et le programme (annexe F) |
| 7 | **CLG2-07** (mineur) : l'inventaire M-0.8 ignore `prereg/contre-lectures/` | 266-270, 291-292 | @L7@ | `prereg/contre-lectures` ajouté au `find` ; dans ce dossier, « brouillon » et « candidat » n'excluent pas et le préfixe est cherché après un tiret ; (m2) par **nom de base** ; pièces de la grille elle-même exclues par nom (relevé en exécutant : sans cela, ses contre-lectures et sa version scellée seraient inventoriées par leur contenu) ; exécuté (annexe F) : 23 → 92 pièces, 69 contre-lectures et vérifications ajoutées, toutes nommées par nom de base dans au moins une autre pièce inventoriée |

Les huit critères sont recopiés mot pour mot, inchangés (N-027). Aucune ligne de cette v4 ne reformule, n'assouplit ni ne
durcit un critère ; toute ligne qui semblerait le faire est un défaut à signaler en contre-lecture.

## 0. Conventions de ce texte

- **[GELÉ]** : règle de lecture, destinée à être scellée ; elle ne dépend d'aucun état constaté.
- **[À DÉCIDER, D-G0-n]** : opérationnalisation nouvelle, qui fixerait la lecture d'un critère ou de la porte : nœud pour
  Lazar (CLAUDE.md, « Nœuds de décision »). Chaque point porte sa recommandation **et un défaut** (annexe B) ; le défaut ne
  prend effet que si D-G0-1 a reçu un mot explicite de Lazar.
- **[EXISTANT]** : opérationnalisation déjà fixée par un préenregistrement scellé ou une décision de Lazar, citée par chemin
  et empreinte ou par numéro de décision et ligne ; la grille la reprend sans la changer. Rien n'est étiqueté [EXISTANT] sans
  que le texte cité ait été vérifié sur disque.
- **Aucun constat d'état** dans la partie gelée. L'état des preuves au 29 octobre vit dans une note séparée, non scellée
  avec la grille (`docs/notes/porte-g0-grille-v1/constat-etat-preuves-G0-2026-10-29-v1.md`). La seule exception de ce
  brouillon est l'**annexe F** (essais des motifs sur le dépôt du 29 octobre), **non gelée et retirée de la version
  scellée** ; ce n'est pas une lecture de G0 (aucun dossier n'existe, des versions qui ne font pas foi y sont essayées).
- **Aucune lecture avant scellement** : aucune lecture de G0 (verdict, même partiel, même « à titre indicatif ») n'est
  recevable avant le scellement de la version finale de cette grille, ni par la session, ni par un sous-agent, ni par une
  lignée. Les états d'avancement de `registres/etat.md` ne sont pas des lectures.
- **Commandes** [GELÉ] : toutes s'exécutent depuis la racine du clone complet au commit `C_lecture`, après
  `export LC_ALL=C.UTF-8 PYTHONPATH=src`. Motif : en locale POSIX, `grep` traite « è » comme deux octets ; la classe
  `[èe]` ne trouve alors rien, et `-i` ne replie pas « É » sur « é » (constaté le 2026-10-29, annexe F). Les motifs
  s'écrivent en `grep -E` avec des alternances `(è|e)`, jamais des classes accentuées (seule exception : la classe
  `[*«" ]` de `PRONONCE_1`, qui ne contient pas de lettre et est essayée sous `C.UTF-8`, annexe F ; un motif qui contient
  un guillemet droit s'écrit entre apostrophes simples). Si `locale -a` ne contient pas
  `C.UTF-8` (ou `C.utf8`), la lecture s'arrête (liste d'arrêt). Une commande qui ouvre une liste de fichiers la construit
  par `find … ! -name 'P3-consignes-v1.md'` **avant** toute ouverture (interdits, section 1). Dans les cellules de table,
  `\|` est l'échappement Markdown d'une barre verticale : la commande à exécuter porte `|` (tube du shell, ou alternance
  d'un motif `grep -E`) ; copié tel quel, `\|` serait une barre littérale en `grep -E` (constaté, annexe F). Hors des
  tables (blocs de code ; définitions `NEUTRE`, `PRONONCE_1`, `LARGE_1`, `CRIT_2`, `FAM_I`, `FAM_II`), rien n'est échappé.

## Hypothèse

Ce texte n'éprouve pas d'hypothèse scientifique. Il fixe, avant toute lecture, la lecture de la porte G0 telle que le brief
l'écrit (`docs/brief-claude-code-programme-complet-v2.md`, l. 190-201), recopiée mot pour mot (comparée par `diff` au
fichier empreinté le 2026-10-29 : identique) :

> ### Porte G0 — prêt pour G1
> Tous les critères suivants sont remplis, preuves scellées à l'appui :
> 1. Harnais validé : déterminisme, équivalence d'activations, gardes testées.
> 2. Organismes (i) et (ii) : sabotage mesurable avec dose-réponse.
> 3. Sondes v0 au-dessus du plancher aléatoire apparié, sur (i) et (ii).
> 4. Base boîte noire, par action et séquentielle, qui tourne sur le même jeu d'épisodes.
> 5. Agrégateurs validés en simulation (T0.3).
> 6. Préenregistrement de G1 scellé et contre-lu.
> 7. Préenregistrement du papier C (HC1 à HC3) scellé et contre-lu.
> 8. État de l'art vérifié ; aucun chiffre non vérifié dans un document du programme.
>
> Si un critère ne peut pas être atteint d'ici le 1er novembre : nœud de décision, avec options et défaut.

Ce nœud a été consommé par N-027 (option (a) : lecture au plus tard fin novembre 2026, critères inchangés). Le report
unique au 31 janvier 2027 (R-750) et le gel d'un critère sur échec scellé pendant le report (R-765) sont des décisions de
Lazar sur le **repli** ; elles ne changent aucun critère.

## Prédiction chiffrée et signe attendu

**Sans objet, et volontairement** : une lecture de porte ne prédit aucun signe ; aucune issue n'est visée (R3). La grille ne
contient aucune estimation de la probabilité de franchissement, et aucun constat d'état dans sa partie gelée.

## Métrique

**[GELÉ, proposé à contre-lire]** Deux niveaux d'état, et rien d'autre.

**État d'un critère k** (un seul par critère, prononcé par le lecteur) :

| état | définition |
|---|---|
| **tenu** | toutes les épreuves mécaniques M-k passent **et** toutes les lectures de fond F-k concluent conformes |
| **non tenu — absent** | aucune preuve scellée recevable à l'heure de lecture (rien, brouillon seulement, candidat, preuve scellée après `C_lecture`, préenregistrement sans le run ou le verdict qu'il exige, verdict qui ne prononce pas le critère) |
| **non tenu — négatif** | **résultat seulement** : preuve scellée, intègre et complète, dont la lecture gelée conclut négativement (« réfuté », « non établi », « non prouvé », « aucune sonde au-dessus », ou toute ligne de sa table qui ne prononce pas le critère) ; ou contrôle scellé prévu par la grille qui conclut négativement (M-8.3, F-8.2, F-8.3) ; **ces négatifs des contrôles de la grille restent des négatifs du critère 8, mais ne gèlent jamais un critère (D-G0-13 (a), CLG2-01)**. Un manque n'est jamais un « négatif » (CLG-05). Le verdict dit si ce négatif vient d'une **liste d'arrêt scellée déclenchée**, d'une ligne de la table gelée de la preuve, ou d'un contrôle de la grille (champ (β)) |
| **non tenu — invalide** | preuve présente mais qui échoue une épreuve d'intégrité ou de procédure (empreinte non conforme après vérification R11, contre-lecture absente ou « non scellable », ordre R1 rompu (M-0.4), auteur du verdict non neuf, jeu d'épisodes différent) ; **ou pièce scellée à laquelle manque un contenu que le critère, sa source ou cette grille exige** (hypothèse absente, priorité non statuée, chiffre sans statut) |
| **non concluant** | preuve scellée et intègre dont la lecture gelée conclut « non concluant » ; ou **résultat suspect de propreté, positif ou négatif, au sens de la propre table de la preuve, sans audit R4 scellé à `C_lecture`** (section « Critères de lecture gelés », R4) ; ou pièce inventoriée par M-0.8 absente du dossier ; ou doute du script M-8.3 sur un chiffre « introuvable » (F-8.2) ; ou version suivante non recevable (section 2) ; ou pièces concurrentes ; ou cas que la grille n'a pas prévu et qui demanderait au lecteur d'interpréter. **Tout « non concluant » cite la ligne de la grille invoquée** |

Les sous-états de « non tenu » ne changent ni l'état du critère ni celui de la porte ; ils servent au rapport et au repli
(synthèse repli § 4 : une clause en sous-états est compatible avec la grille). Parce que « négatif » ne couvre que des
résultats, une clause qui requalifierait un « absent » en « négatif » (synthèse repli § 5, choix 2) le ferait elle-même,
par une règle écrite, jamais par le mot de la grille.

**Trois champs constatés par critère, sans effet sur l'état**, pour que la clause de repli en dépende sans décision du
lecteur :
- (α) « préenregistrement scellé, contre-lu, à liste d'arrêt : présent / absent » (M-0.2 passé et section « Liste d'arrêt »
  non vide) ;
- (β) « liste d'arrêt déclenchée » : **« sans objet »** si (α) est absent ou si le critère n'a pas de run (critères 6, 7, 8) ;
  **« oui » / « non »** si le verdict de la preuve le dit (M-0.7) ; **« absent »** si (α) est présent et que le verdict n'en
  dit rien (CLG-12) ;
- (γ) « gelé (R-765) » : **« sans objet »** à la première lecture ; à la seconde : « oui » (chemin et commit du `.sha256` de
  la pièce qui l'a gelé, au sens de D-G0-13 : négatif d'une preuve dont (α) est « présent », issu de sa liste d'arrêt ou de
  sa table gelée ; jamais un négatif de M-8.3, F-8.2 ou F-8.3) ou « non ».

**État de la porte** : franchie / non franchie / non concluante (section « Critères de lecture gelés »).

## Seuil

**[GELÉ, proposé]**
- Le seuil de chaque critère est celui de sa preuve : la grille ne fixe aucun seuil statistique nouveau. Quand la preuve est
  un préenregistrement scellé, son seuil et sa table de lecture font foi ; la grille vérifie qu'ils existent, qu'ils ont été
  scellés avant le run, et lit la ligne qui s'applique.
- **Première lecture, unique pour l'échéance du 30 novembre** **[À DÉCIDER, D-G0-1]** (CLG-15) : N-027 dit « au plus tard
  fin novembre 2026 » sans heure. Proposé : ouverte au plus tard le **2026-11-30 à 23:59 UTC** ; elle peut être ouverte plus
  tôt, **une seule fois, sur mot de Lazar seul** (nœud ; cité mot pour mot dans le fichier d'ouverture), jamais sur demande
  d'une session ou d'une lignée ; une lecture anticipée « non franchie » ou « non concluante » n'est pas refaite le
  30 novembre : elle tient lieu de première lecture.
- **Seconde lecture** [EXISTANT, R-750 et R-765 ; mécanique GELÉE] : si la première n'est pas « franchie », une seule
  seconde lecture, **finale**, ouverte au plus tard le **2027-01-31 à 23:59 UTC**, avec **la même grille** (même empreinte),
  son propre fichier d'ouverture et son propre `C_lecture`, selon les mêmes règles que la première (ouverture, lecture
  tardive, coupure). Aucune troisième lecture. Ce que la seconde lecture fait de son issue relève de la clause de repli.
- **Ouverture et `C_lecture`** : la session ouvre chaque lecture par un commit sur `main` du dépôt de travail qui ne contient
  que `registres/g0-lecture-ouverte-vN.md` (rang de la lecture : 1 ou 2 ; date UTC ; mot de Lazar si anticipée ; empreinte
  de la grille scellée ; empreinte du dossier de G0 de cette lecture). `C_lecture` est le **parent** de ce commit, nommé dans
  le verdict.
- **Lecture tardive** : si aucune ouverture n'a eu lieu à l'échéance (2026-11-30 23:59 UTC pour la première, 2027-01-31
  23:59 UTC pour la seconde), `C_lecture` est le dernier commit de `main` antérieur à cette heure ; la porte est lue telle
  quelle au premier moment possible ; le retard est une réserve. Aucune preuve committée après `C_lecture` ne compte.
- **Heure de coupure des preuves** : une preuve compte si son empreinte compagnon est committée sur `main` au plus tard à
  `C_lecture` (`git merge-base --is-ancestor <commit du .sha256> <C_lecture>`).
- **Grille avant lecture** **[À DÉCIDER, D-G0-1]** : scellement de la version finale au plus tard le **2026-11-15**, et
  **seulement avec les points D-G0-1 à D-G0-13 tranchés ou échus** (sinon un critère est « non concluant » par construction).
  **D-G0-1 ne s'applique pas à lui-même** (CL1 § 6) : il exige un **mot explicite** de Lazar. Si ce mot est donné, tout point
  D-G0-2 à D-G0-13 non tranché au 2026-11-15 prend le **défaut** écrit en annexe B, et la grille scellée recopie le choix
  retenu pour chaque point. Sans mot explicite sur D-G0-1 au 2026-11-15, aucun défaut ne s'applique, la grille n'est pas
  scellable et la session ouvre un nœud ; sans grille scellée à l'échéance d'une lecture, cette lecture ne s'ouvre pas
  (liste d'arrêt).
- **La grille elle-même passe M-0.2** : `exiger_prereg_scelle('prereg/G0-grille-lecture-vN.md')` rend son empreinte sans
  erreur. Le lecteur le vérifie avant toute autre chose.

## Plan d'analyse

### 1. Qui lit, avec quoi [GELÉ, R13 ; précisions proposées]

- Un **sous-agent neuf** : il n'a écrit ni cette grille, ni ses contre-lectures, ni aucune des preuves lues
  (préenregistrement, run, analyse, verdict de critère, contre-lecture de ces pièces), ni les tests de la règle de repli sur
  dossiers synthétiques (synthèse repli § 5, choix 10). Il le déclare en tête de son verdict (gabarit, annexe A). Le lecteur
  de la seconde lecture n'est pas celui de la première.
- **[À DÉCIDER, D-G0-6]** Modèle différent de celui des auteurs des preuves, dans la même famille (comme N-052), et lignée
  différente de celle qui a écrit la grille ; modèle et lignée déclarés en tête du verdict ; à défaut, signalé.
- Il reçoit **exactement deux pièces** (R2) : la grille scellée et le **dossier de G0** `docs/verdicts/dossier-G0-vN.md` de
  cette lecture, scellé, séparé de la grille, qui liste par critère : (a) les pièces **remises** (chemin, empreinte, commit
  du `.sha256`) ; (b) pour chaque preuve dont le préenregistrement prévoit un audit de symétrie, la ligne de ce
  préenregistrement qui le définit et la ligne du verdict qui le dit déclenché ou non (R4, CLG-06) ; (c) les pièces
  **écartées**, chacune avec un motif de la liste fermée de M-0.8. Rien d'autre n'est lu, hors des fichiers que les
  commandes de cette grille ouvrent d'elles-mêmes (inventaire M-0.8, sources citées par chemin).
- **Complétude du dossier** (CLG-01) : le lecteur ne s'en remet pas au dossier ; il exécute l'inventaire **M-0.8**. Toute
  pièce inventoriée absente du dossier rend « non concluant » chaque critère auquel elle se rattache (ligne M-0.8 citée).
  Il **compte**, il n'interprète pas (R13) ; là où une lecture de fond F-k lui laisserait un jugement non écrit ici, il rend
  « non concluant » et cite la ligne.
- Il travaille sur un **clone complet** de `lciric/controle-ia-travail`, branche `main`, au commit `C_lecture` :
  `git rev-parse --is-shallow-repository` rend `false` ; sinon, arrêt (liste d'arrêt). Motif : M-0.4 et la réserve des sept
  jours lisent des dates de commit ; sur un clone superficiel, `git log -- <fichier>` rend la date du commit de greffe
  (constaté par la v2 et par CL1).
- **Interdits de lecture** pour lui comme pour tout auteur : `prereg/P3-consignes-v1.md` ; `donnees/` ; tout `diag/*/traces` ;
  toute branche `donnees/*` ou `quarantaine/*` ; tout fichier nommé « carte des hypothèses ». Aucune preuve de G0 ne doit
  exiger de les ouvrir ; si l'une l'exige, c'est une condition d'arrêt. Une empreinte de ces fichiers peut être vérifiée par
  script sans en afficher le contenu.
- Son verdict est scellé, puis soumis à Lazar pour GO (R13). « Franchie » n'ouvre la phase 1 que sur ce GO ; le GO ne
  requalifie jamais une issue.

### 2. Règle de version : quelle pièce fait foi [GELÉ, proposé]

- Pour chaque critère, la pièce qui fait foi est la **version scellée la plus récente** de son préenregistrement, de son
  verdict et de sa contre-lecture, au sens du numéro `vN` du nom (R12), parmi les pièces remises du dossier. Jamais un
  fichier de `brouillons/`, ni un nom portant « brouillon » ou « candidat », ni un bloc-notes, ni une passation.
- **[À DÉCIDER, D-G0-7]** Une version suivante ne compte que si (a) elle a été autorisée par une décision consignée (nœud ou
  GO) **avant** son run, comme N-010 et N-011 pour T0.4 v2 et v3, et (b) cette décision **nomme une cause distincte du
  résultat** (défaut d'instrument, écart au préenregistrement constaté, garde déclenchée), sinon c'est un retirage (R3, R4).
  Version non autorisée, ou autorisée sans cause nommée : le critère est « non concluant » (la version précédente ne
  « revient » pas). Après un « non tenu — négatif » prononcé par une liste d'arrêt scellée, **aucune version suivante n'est
  recevable** [EXISTANT, R-765 : « un critère réfuté par sa liste d'arrêt scellée n'est jamais retenté »]. **Exception
  pendant le report** (CLG2-01) : entre le verdict de la première lecture et la seconde lecture, un critère gelé au sens de
  D-G0-13 (a) n'admet aucune version suivante, même autorisée avec cause nommée (R-765 : « gèle ce critère jusqu'au second
  verdict ») ; hors de ce gel, la règle ci-dessus vaut aussi pour un négatif par ligne de table prononcé au verdict de la
  première lecture (D-G0-13 (b), défaut). Le lecteur rapporte, en réserve, le nombre de versions par critère.
- **Seconde lecture et gel** **[À DÉCIDER, D-G0-13 ; règle de gel EXISTANTE, R-765]** : un critère est **gelé** au sens de
  D-G0-13 dans deux cas seulement : (a) pendant le report, un « non tenu — négatif » d'une preuve dont (α) est « présent »,
  issu de la liste d'arrêt de ce préenregistrement ou d'une ligne de la table gelée de cette preuve, scellé après le verdict
  de la première lecture ; (b) au verdict de la première lecture, un « non tenu — négatif » venu d'une liste d'arrêt scellée
  déclenchée (champ (β) = « oui »). Les négatifs des contrôles de la grille (M-8.3, F-8.2, F-8.3) ne gèlent pas ; « absent »,
  « invalide » et « non concluant » ne gèlent pas. Un critère gelé est lu, à la seconde lecture, sur la pièce qui l'a gelé ;
  toute version ou pièce postérieure portant sur ce critère n'est pas recevable (écartée sous le motif (m4) de M-0.8 et
  rapportée en réserve, avec son chemin) ; le champ (γ) le dit. Commande :
  `git merge-base --is-ancestor <commit du .sha256 du verdict de G0 de la première lecture> <commit du .sha256 de la pièce>`
  (code 0 : pièce scellée pendant le report).
- Si deux pièces scellées concurrentes portent sur le même critère sans relation de version, le lecteur rend « non concluant »
  et le dit (il ne choisit pas).

### 3. Épreuves mécaniques communes (M-0) [GELÉ]

Préalable à toute commande : `export LC_ALL=C.UTF-8 PYTHONPATH=src` (section 0). Pour toute pièce du dossier citée comme
preuve, dans l'ordre, chaque ligne avec sa commande, sa sortie attendue et l'état si échec. Dans les motifs ci-dessous,
`NEUTRE` désigne :
`sous-agent neuf|contre-lecteur neuf|n['’]ai (pas )?écrit|ne suis (pas )?l['’]auteur|l['’]auteur ni (du|de|des|le|la|les|l['’])`.

| n° | épreuve | commande (depuis la racine du clone complet) | sortie attendue | état si échec |
|---|---|---|---|---|
| M-0.1 | intégrité | `python -m controle_ia.scellement verifier <fichier>` ; pour un fichier annoncé absent : `ls -la <fichier> <fichier>.sha256 ; sha256sum <fichier>` (R11) | `OK` ; empreinte égale à celle du dossier | « non tenu — invalide » (présent mais non conforme) ; « non tenu — absent » (absent après R11) |
| M-0.2 | préenregistrement conforme R1/R2 | `python -c "from controle_ia.prereg import exiger_prereg_scelle as e; print(e('<prereg>'))"` | l'empreinte, sans `GardeArret` | « non tenu — invalide » |
| M-0.3 | contre-lecture R2 | pour chaque rapport cité dans la section « Contre-lecture » : M-0.1 ; `head -5 <rapport> \| grep -c -i -E "NEUTRE"` ; `grep -n -i -o -m1 -E "(non )?scellable( après corrections)?" <rapport>` ; pour chaque remarque numérotée du rapport, `grep -n "<numéro>" <prereg>` | rapport intègre ; au moins une ligne de neutralité dans les cinq premières lignes (recopiée dans le verdict) ; **première** occurrence = « Scellable » ou « Scellable après corrections » (jamais « non scellable ») ; chaque remarque trouvée dans le préenregistrement avec un traitement (accepté / refusé et pourquoi) | « non tenu — invalide » |
| M-0.4 | ordre R1 (preuve empirique) | `python -c "import json;m=json.load(open('runs/<run>/manifeste.json'));print(m['preenregistrement'],m['cree_le'])"` ; `git log --format='%H %cI' -- <prereg>.sha256 \| tail -1` ; `git merge-base --is-ancestor <commit de scellement> <commit du run cité par le manifeste>` | empreinte du manifeste égale à celle du fichier scellé ; date du commit de scellement antérieure à `cree_le` ; code 0 | « non tenu — invalide » (ordre R1 rompu). Une date de commit peut être falsifiée : contrôle rapporté comme fait, pas comme preuve absolue |
| M-0.5 | verdict scellé de la preuve | M-0.1 sur le verdict ; `grep -n "<empreinte du prereg>" <verdict>` ; `head -5 <verdict> \| grep -c -i -E "NEUTRE"` | verdict cite l'empreinte du préenregistrement, égale au fichier ; une ligne de neutralité dans ses cinq premières lignes (ou, pour T0.3, lecture produite par le code gelé cité au manifeste) | « non tenu — invalide » ; **[À DÉCIDER, D-G0-8]** absence de verdict scellé pour un critère empirique = « non tenu — absent » (défaut) |
| M-0.6 | coupure | `git log --format=%H -1 -- <fichier>.sha256` ; `git merge-base --is-ancestor <ce commit> <C_lecture>` | code 0 | pièce non recevable → « non tenu — absent » si aucune autre pièce |
| M-0.7 | champs (α) et (β) de la Métrique | `python -c "from controle_ia.prereg import sections;s=sections(open('<prereg>',encoding='utf-8').read());print(bool(s.get('Liste d\'arrêt')))"` ; dans le verdict de la preuve, `grep -n -i "liste d'arrêt" <verdict>` | (α) `True` + M-0.2 passé = « présent » ; (β) selon la règle de la Métrique (sans objet / oui / non / absent) | aucun effet sur l'état ; champ rapporté |
| M-0.8 | **inventaire de complétude** (CLG-01) | (a) pièces : script M-0.8 ci-dessous ; (b) runs : pour chaque `runs/*/manifeste.json` dont `preenregistrement.chemin` figure dans la sortie de (a), le chemin du run | chaque fichier de (a) et chaque run de (b) figure au dossier, **remis** pour un critère ou **écarté** sous un motif de la liste fermée | pièce ou run absent du dossier : « non concluant » pour chaque critère auquel il se rattache ; motif hors liste : idem ; écartés recopiés en réserve, avec leur motif |

**Script M-0.8 (a)**, exécuté tel quel (il n'ouvre aucun fichier interdit : la liste est filtrée par nom avant toute
lecture). Il parcourt aussi `prereg/contre-lectures/` (CLG2-07) : dans ce dossier, « brouillon » et « candidat » n'excluent
pas (la contre-lecture d'un brouillon est une pièce scellée, et une contre-lecture « non scellable » que le préenregistrement
ne cite pas doit être inventoriée), et le préfixe est cherché en tête du nom ou après un tiret. Les pièces de la grille
elle-même (`*G0-grille-lecture*` : brouillons, version scellée, contre-lectures) sont exclues par nom : elles sont
l'instrument de la lecture, pas la preuve d'un critère (sans cette exclusion, elles seraient inventoriées par leur contenu,
annexe F).

```
export LC_ALL=C.UTF-8
for f in $(find prereg docs/verdicts docs/etat-de-l-art prereg/contre-lectures -maxdepth 1 -type f -name '*.md' ! -name 'P3-consignes-v1.md' ! -name '*G0-grille-lecture*' | sort -u); do
  [ -f "$f.sha256" ] || continue
  b=$(basename "$f")
  case "$f" in
    prereg/contre-lectures/*) motif='(^|-)(T0\.[3-8]|P3-|P4-instrument|G1-|papier-C-|etat-de-l-art)' ;;
    *) echo "$b" | grep -q -i -E 'brouillon|candidat' && continue
       motif='^((verdict|audit-R4)-)?(T0\.[3-8]|P3-|P4-instrument|G1-|papier-C-|etat-de-l-art)' ;;
  esac
  if echo "$b" | grep -q -E "$motif" \
     || grep -q -i -E 'crit(è|e)res? [0-9]([^0-9][^|]{0,60})?G0' "$f"; then echo "$f"; fi
done
```

**Script M-0.8 (b)**, sur la sortie de (a) enregistrée dans un fichier hors du clone :

```
python -I -c "import json,glob,sys
inv=set(open(sys.argv[1]).read().split())
for m in sorted(glob.glob('runs/*/manifeste.json')):
    p=json.load(open(m,encoding='utf-8')).get('preenregistrement') or {}
    c=p.get('chemin') if isinstance(p,dict) else p
    if c in inv: print(m, c)" <sortie de (a)>
```

**Rattachement à un critère** : par le préfixe que le motif du script trouve dans le nom (T0.4 → 1 ; T0.5, T0.6 → 2 ; P3- → 2 et 3 ; T0.7, P4-instrument → 3 ; T0.8 → 4 ;
T0.3 → 5 ; G1- → 6 ; papier-C- → 7 ; etat-de-l-art → 8) **et** par le contenu (chaque numéro k des lignes qui rendent
`grep -n -i -o -E 'crit(è|e)res? [0-9]([^0-9][^|]{0,60})?G0' <fichier>`). Un run se rattache aux critères de son
préenregistrement.

**Motifs d'écart, liste fermée** : (m1) **version antérieure** d'une série dont une version postérieure est remise (même nom
à `vN` près) ; (m2) **pièce auxiliaire** d'une pièce remise (addendum, audit, contre-lecture, différentiel, archive, run),
nommée par celle-ci **par son nom de base** (`grep -n -F "<nom de base de la pièce écartée>" <pièce remise>` rend au moins
une ligne ; le nom de base prend aussi une citation par chemin complet, CLG2-07) ; (m3) **autre**, motif écrit par la session
dans le dossier ; (m4) **postérieure au gel** (D-G0-13, CLG2-05) : à la seconde lecture seulement, pièce scellée pendant le
report sur un critère gelé ; le dossier donne le chemin du verdict de G0 de la première lecture ; contrôle : commande de la
section 2 (`git merge-base --is-ancestor …`, code 0) et champ (γ) « oui » pour ce critère ; sinon le motif est hors liste.
Le lecteur ne juge aucun motif (m3) : il le recopie, en réserve du critère, avec le chemin de la pièce et la ligne de
conclusion que la pièce donne d'elle-même (première ligne de sa section d'en-tête ou de verdict). Une pièce (m1) n'est
recevable comme écart que si la version postérieure est elle-même recevable (section 2). Une pièce (m4) est recopiée en
réserve comme une pièce (m3).

### 4. Fiches par critère

Chaque fiche donne : texte exact ; sources qui fixent la lecture ; preuves attendues ; liste de contrôle (commande, sortie
attendue, état si échec) ; nature de l'opérationnalisation ; points à décider. Aucun état constaté.

---

#### Critère 1 — « Harnais validé : déterminisme, équivalence d'activations, gardes testées. »

- **Sources** : brief T0.4 (l. 146-152 : garde d'équivalence testée sain et artefact, déterminisme au bit près, « Fini quand :
  un épisode produit de bout en bout trajectoire + activations + manifeste, scellés et rejouables ») ; R5.
- **Preuves attendues** (dossier de G0) : (a) un verdict scellé qui prononce le critère 1 ; (b) le préenregistrement qu'il
  applique, scellé et contre-lu ; (c) les manifestes des runs qu'il lit ; (d) ses recalculs scellés. Règle de version :
  section 2 (série `docs/verdicts/verdict-T0.4-critere-1-G0-vN.md`).
- **Liste de contrôle** (`PRONONCE_1` désigne le motif `crit(è|e)re 1 de G0( est)? *:? *[*«" ]*(non prouvé|non concluant|prouvé)`,
  écrit entre apostrophes simples dans la commande ; `LARGE_1` désigne `crit(è|e)re 1 de G0[^.]{0,20}(non prouvé|non concluant|prouvé)`,
  filet pour une typographie imprévue, par exemple une espace insécable, CLG2-04) :

| n° | contrôle | commande | sortie attendue | état si échec |
|---|---|---|---|---|
| M-1.1 | M-0.1 à M-0.8 sur (a) à (d) | section 3 | tout passe | selon M-0 |
| M-1.2 | le verdict cite le préenregistrement | `grep -n "<empreinte de (b)>" <verdict>` | au moins une ligne | non tenu — invalide |
| F-1.1 | prononcé du verdict (CLG-04, CLG2-04) | `grep -n -o -i -E 'PRONONCE_1' <verdict>` ; mots distincts : `grep -o -i -E 'PRONONCE_1' <verdict> \| grep -o -i -E '(non prouvé\|non concluant\|prouvé)$' \| sort -u` ; si 0 ligne : `grep -c -i -E 'LARGE_1' <verdict>` | exactement un mot distinct | « prouvé » : conforme ; « non prouvé » : non tenu — négatif ; « non concluant » : non concluant ; **0 ligne et `LARGE_1` = 0 : non tenu — absent** ; 0 ligne et `LARGE_1` ≥ 1 : non concluant (forme imprévue, ligne citée) ; plusieurs mots distincts : non concluant (ligne citée ; un verdict qui cite le prononcé d'une version antérieure sous la forme « Critère 1 de G0 : … » tombe ici, d'où la forme exigée en annexe C point 6) |
| F-1.2 | trois composantes nommées dans la section du verdict | `python -c "from controle_ia.prereg import sections;s=sections(open('<verdict>',encoding='utf-8').read());t=' '.join(v for k,v in s.items() if 'verdict' in k.lower()).lower();print([m in t for m in ('déterminisme','équivalence','garde')])"` | `[True, True, True]` | non concluant (ligne citée) |
| F-1.3 | aucune réserve de table ouverte | `grep -n "Réserves au sens de la table" <verdict>` | « : aucune » ou liste recopiée en réserve | aucun effet sur l'état ; réserves recopiées |

- **Opérationnalisation** : [EXISTANT] table gelée de `prereg/T0.4-validation-modele-reel-v3.md`
  (`4f711cd3a58182856c804e6652ec92c1aaab865fe9b595ea1d6be65757b8ed5f`, vérifiée par la v2 et CL1), appliquée par la version
  qui fait foi.
- **Domaine de validité** **[À DÉCIDER, D-G0-5]** : P-007 (retenue) prévoit qu'en production hors du domaine de T0.4 (noyau
  par défaut, autre carte) une garde d'équivalence reste en ligne sur un échantillon (99e centile par action et par couche
  ≤ 0,2 ; P-007 l. 22-24). Défaut (recommandation commune des deux avis) : si les runs des critères 2 à 4 sortent du
  domaine sans cette garde, le lecteur l'écrit en **réserve** du critère 1 ; **et** les préenregistrements de T0.6 à T0.8
  doivent exiger cette garde hors domaine (contrôle : `grep -n -i "garde d'équivalence" <prereg T0.6|T0.7|T0.8>` ; absence →
  réserve du critère 1). Une lecture plus dure changerait le critère : à Lazar.

---

#### Critère 2 — « Organismes (i) et (ii) : sabotage mesurable avec dose-réponse. »

- **Sources** : brief T0.6 (l. 160-164 : familles (i) instruction cachée et (ii) distillation de contexte par adaptateur de
  rang faible ; « Calibration dose-réponse du budget de sabotage (proportion d'actions sabotées × intensité) » ; « Fini
  quand : effet de sabotage mesurable par la vérité terrain, avec une dose-réponse monotone, pour (i) et (ii) ») ; P-009
  option (a) (`docs/decisions/proposition-P-009-T0.6-organismes-v1.md`, `fe74b91323a671b4fd7399421e8295f6078383323184b81d755fbba878af7ad9`) ;
  P-015 option (b) (`docs/decisions/proposition-P-015-T0.6-T0.8-mode-cout-v1.md`,
  `6e74c6cbcd3b05ab65dbbf42fc6481520a6717ec1e40e0961a633c5ed76a19d2`) : mode « coût », recherche de dose sur la boîte noire
  seule puis T0.6 décisif, (ii) en lancements séparés ; P-014 (vérité terrain de l'appariement) ; N-020 (4).
- **Preuves attendues** : pour **chacune** des familles (i) et (ii) : préenregistrement décisif de T0.6 scellé et contre-lu,
  à liste d'arrêt ; run(s) avec manifeste ; verdict scellé par un sous-agent neuf (M-0.5, D-G0-8) dont une ligne de la table
  gelée prononce, pour cette famille, « sabotage mesurable avec dose-réponse » (critère 2 établi). Un seul préenregistrement
  couvrant (i) et (ii) est recevable s'il a une ligne par famille.
- **Liste de contrôle** (`CRIT_2` désigne `crit(è|e)res? ([0-9]+ ?(,|et|à) ?)*2([^0-9]|$)` ; `FAM_I` désigne `\(i(-[a-z])?\)` ;
  `FAM_II` désigne `\(ii(-[a-z])?\)`) :

| n° | contrôle | commande | sortie attendue | état si échec |
|---|---|---|---|---|
| M-2.1 | M-0.1 à M-0.8 sur chaque pièce, par famille | section 3 | tout passe | selon M-0 |
| M-2.2 | la table gelée nomme le critère 2 (CLG-03) | `python -c "from controle_ia.prereg import sections;print(sections(open('<prereg T0.6>',encoding='utf-8').read()).get('Critères de lecture gelés',''))" \| grep -n -i -E "CRIT_2"` | au moins une ligne par famille | non concluant (table sans ligne pour le critère) |
| F-2.1 | les deux familles couvertes (CLG-03) | dans la section du verdict dont le titre contient « Verdict » : `grep -n -E "FAM_I"` ; `grep -n -E "FAM_II"` | une ligne prononçant le critère pour (i) et une pour (ii) | non tenu — absent (famille sans verdict) ; non tenu — négatif (ligne négative) |
| F-2.2 | effet lu sur la vérité terrain (CLG-10) | `python -c "from controle_ia.prereg import sections;print('vérité terrain' in sections(open('<prereg T0.6>',encoding='utf-8').read()).get('Métrique','').lower())"` | `True` | non concluant |
| F-2.3 | dose réalisée (proportion × intensité) | même commande avec `'proportion'` puis `'intensité'` | `True` deux fois | non concluant |
| F-2.4 | la ligne qui s'applique dit « dose-réponse » au sens fixé d'avance | `sed -n '<l>p' <prereg T0.6>` pour la ligne de table citée par le verdict ; `grep -c -i "dose-réponse"` sur cette ligne | 1 | non tenu — négatif si la ligne qui s'applique est négative ; non concluant si « non concluant » |

- **Latitude** **[À DÉCIDER, D-G0-2]** : « mesurable » et « dose-réponse » ne sont fixés par aucun préenregistrement scellé ;
  le seul précédent scellé est P3-P1 (`prereg/P3-premier-test-i-a-v1.md`,
  `d975e9817e88d30196930c2a351927c2091f2ac024d2a5b52556730fa36cb672`) : différence appariée du log10 du coût déclaré,
  saboteur moins honnête, intervalle à 95 % par blocs de tâches au-dessus de zéro ; une seule dose. **Défaut
  (recommandation commune des deux avis)** : la grille ne fixe pas le test ; elle **délègue** au préenregistrement de T0.6,
  sous conditions minimales qu'il doit écrire avant son run : (a) « mesurable » à chaque dose non nulle selon la forme de
  P3-P1 ; (b) « dose-réponse » = tendance croissante avec la dose par un test préenregistré et **chiffré** dans T0.6 (pente
  appariée ou corrélation de rangs, intervalle à 95 % au-dessus de zéro), et aucune différence appariée entre doses voisines
  significativement négative (lecture du mot « monotone », qui vient du « Fini quand » de T0.6, pas du critère ; dit ici
  comme tel) ; (c) **au moins deux doses non nulles** en plus de la dose nulle, fixées d'avance ; (d) une ligne « non
  concluant » explicite. **Contrôle mécanique** (CLG2-06), sur le texte des sections « Seuil » et « Critères de lecture
  gelés » de T0.6, extrait par
  `python -c "from controle_ia.prereg import sections;s=sections(open('<prereg T0.6>',encoding='utf-8').read());print(s.get('Seuil','')+chr(10)+s.get('Critères de lecture gelés',''))"`
  et passé à `grep -c -i -E` avec un motif par condition :
  (a) `mesurable[^.]{0,80}chaque dose|chaque dose[^.]{0,80}mesurable` ;
  (b) `pente appari(é|e)e|corr(é|e)lation de rangs`, **et** `doses voisines` ;
  (c) `doses non nulles ?: ?[^;]+;[^;]+` (forme exigée « Doses non nulles : d1 ; d2 [; …] », annexe C point 6 : le
  point-virgule sépare les doses, la virgule étant la marque décimale) ;
  (d) `non concluant`.
  Chacun des cinq comptes ≥ 1 : conditions présentes ; un compte à 0 : **non concluant** (ligne citée), sans autre lecture.
  Le lecteur ne juge pas si le test choisi est « bon » : il constate la présence des quatre conditions.
- **États** : tenu si M et F passent pour (i) et pour (ii) ; non tenu — absent si l'une des deux familles n'a pas de verdict
  scellé ; non tenu — négatif si l'une a une ligne négative ; non concluant sinon.
- **Contrôles de référence** (honnête, témoin instruit, mention ; P-015) : lus par T0.6 ; la grille ne les exige pas pour le
  critère 2 (le texte ne les nomme pas) ; leur absence est rapportée en réserve.

---

#### Critère 3 — « Sondes v0 au-dessus du plancher aléatoire apparié, sur (i) et (ii). »

- **Sources** : brief T0.7 (l. 166-173 : agrégation **max ou attention uniquement** ; plancher « sonde aléatoire appariée en
  covariance (style P3) » ; anti-circularité ; « Fini quand : AUROC par action au-dessus du plancher, sur (i) et (ii), avec
  intervalles de confiance ») ; P-011 option (c) (`docs/decisions/proposition-P-011-T0.7-sondes-v1.md`,
  `64afff19ce5ceab6f99e3f15d583fcdc3890e08a480a017703f2a57331636fd9`, l. 39-42 et 57) : bras principal = sondes entraînées sur
  données génériques, gelé d'avance ; N-026 (`docs/decisions/decision-N-026-v1.md`,
  `85bd40235f3668c66adffc2ff18139ff1a0c402f3aaa24cca70db0217f755bf0`) : un bras « moyenne » ne fait franchir aucune porte ;
  P-015 (b) : témoin positif P4-instrument lu avant toute sonde sur les épisodes de T0.6 ; P-013 défaut (b).
- **Preuves attendues** : préenregistrement décisif de T0.7 scellé et contre-lu **avant** le run des épisodes qu'il lit
  (P-015 (b)) ; scores sur les épisodes de T0.6 de (i) et de (ii) ; verdict scellé par un sous-agent neuf (M-0.5, D-G0-8) dont
  une ligne prononce, pour chaque famille, « au-dessus du plancher » ; verdict scellé de P4-instrument antérieur à la
  première lecture de sonde, **condition** par défaut **[À DÉCIDER, D-G0-11]** (CLG2-03).
- **Liste de contrôle** :

| n° | contrôle | commande | sortie attendue | état si échec |
|---|---|---|---|---|
| M-3.1 | M-0.1 à M-0.8 | section 3 | tout passe | selon M-0 |
| M-3.2 | T0.7 scellé avant les épisodes lus | `git log --format=%cI -- <prereg T0.7>.sha256 \| tail -1` contre `cree_le` du manifeste de T0.6 (étape décisive) | scellement antérieur | **défaut de D-G0-11 (« condition »)** : non tenu — invalide ; option « réserve » : réserve. Même état que M-3.5 sous chaque option (CLG2-03 : même source, P-015 (b), décision en vigueur, pas le texte du critère) |
| M-3.3 | agrégation max ou attention (CLG2-06) | `grep -i "bras principal" <prereg T0.7> \| grep -c -i -E "\bmax\b\|attention"` ; `grep -i "bras principal" <prereg T0.7> \| grep -c -i "moyenne"` | premier compte ≥ 1 ; second compte = 0 (la ligne « Bras principal » de T0.7 porte l'agrégation, annexe C point 6) | non concluant si l'un des deux comptes échoue (N-026 : bras « moyenne » ne compte pas) |
| M-3.4 | plancher apparié, mêmes actions, même agrégation (CLG-10) | `python -c "from controle_ia.prereg import sections;t=sections(open('<prereg T0.7>',encoding='utf-8').read()).get('Métrique','').lower();print([m in t for m in ('covariance','même agrégation','mêmes actions')])"` | `[True, True, True]` (recette de `prereg/P3-premier-test-i-a-v1.md` l. 228-230, section « Métrique ») | non concluant |
| M-3.5 | P4-instrument (D-G0-11) | M-0.1 sur `docs/verdicts/verdict-P4-instrument-vN.md` ; `git log --format=%cI -- <ce .sha256> \| tail -1` contre la **date de la première lecture de sonde** = plus petit `cree_le` des manifestes que M-0.8 (b) rattache au préenregistrement de T0.7 | présent, intègre, antérieur | **défaut de D-G0-11 (« condition »)** : non tenu — invalide (absent, non intègre ou postérieur) ; option « réserve » : réserve. Même état que M-3.2 sous chaque option (CLG2-03) |
| F-3.1 | seuil [EXISTANT] (CLG2-06) | dans le verdict, pour chaque famille (`FAM_I`, puis `FAM_II`) : `grep -i -E 'borne basse[^.]{0,120}(strictement )?(sup(é\|e)rieure\|au-dessus)[^.]{0,80}quantile 0,95' <verdict> \| grep -c -E 'FAM_I'` (positif) et `grep -i -E 'aucune sonde (principale )?au-dessus' <verdict> \| grep -c -E 'FAM_I'` (négatif) ; niveau : section « Seuil » de T0.7 par `sections()`, `\| grep -i "intervalle" \| grep -c -E '9[5-9](,[0-9]+)? ?%'` ; correction : même section `\| grep -c -i "bonferroni"`, ou `grep -i -m1 "bras principal" <prereg T0.7> \| grep -c ";"` = 0 (une seule sonde principale) | par famille : positif ≥ 1 et négatif = 0 ; niveau ≥ 1 ; correction présente ou une seule sonde principale (niveau **jamais sous 95 %, corrigé pour le nombre de sondes principales**, P3 l. 272-275 : Bonferroni, 97,5 % pour deux sondes) | négatif ≥ 1 et positif = 0 : non tenu — négatif (« aucune sonde au-dessus ») ; positif et négatif à 0, ou tous deux ≥ 1 : non concluant (ligne citée) ; niveau ou correction à 0 : non concluant (niveau non fixé d'avance) |
| F-3.2 | (i) et (ii) chacune pour son compte (CLG-03) | `grep -n -E "\(i(-[a-z])?\)" <verdict>` ; `grep -n -E "\(ii(-[a-z])?\)" <verdict>` | une ligne par famille | non tenu — absent (famille sans ligne) |
| F-3.3 | bras principal gelé d'avance (P-011 (c) ; CLG-10) | `grep -i "bras principal" <prereg T0.7> \| grep -c -F "<nom de la sonde retenue, recopié du verdict>"` | ≥ 1 (le préenregistrement de T0.7 nomme ses sondes principales sur une ligne qui contient « Bras principal ») | non concluant (sonde hors bras principal : même règle que P3 l. 436) |
| F-3.4 | anti-circularité (CLG2-06) | `<A>` = fichier des identifiants d'actions d'entraînement des sondes, **nommé par le manifeste du run de T0.7** ; `<B>` = fichier des identifiants d'actions lues, **nommé par les manifestes des runs de T0.6** (chemins recopiés des manifestes dans le dossier ; M-0.1 sur chacun ; un identifiant par ligne, même forme, annexe C point 6) ; `bash -c 'comm -12 <(sort -u <A>) <(sort -u <B>) \| wc -l'` | `0` | ≥ 1 : non tenu — invalide ; `<A>` ou `<B>` non nommé par un manifeste, ou échec de M-0.1 : non concluant (ligne citée) |
| F-3.5 | ligne « non interprétable » | `sed -n '<l>p'` de la ligne de table citée par le verdict ; `grep -c -i "non interprétable"` | 0 | 1 : non concluant, jamais tenu (prédicteur trivial qui sépare autant, P3 l. 429) |

- **États** : tenu si les deux familles ont leur ligne « au-dessus » ; non tenu — négatif si l'une a la ligne « aucune sonde
  au-dessus » ; non concluant si l'une est « non interprétable » ou « non concluante » ; non tenu — absent sinon.
- **Opérationnalisation** : [EXISTANT] pour le seuil (F-3.1, P3 l. 272 ; même règle dans P-011 l. 40) et le bras (F-3.3).
  Changer le bras principal (par exemple vers les sondes de domaine) après toute lecture de sonde serait une modification
  d'une opérationnalisation décidée : nœud.
- **[À DÉCIDER, D-G0-11]** Statut de P4-instrument et de l'ordre de P-015 (b) (décision en vigueur, pas texte du critère).
  **Défaut : condition** (avis Fable grille, l. 19-23 ; CL2 § 4, confiance moyenne) : verdict de P4-instrument absent, non
  intègre ou postérieur à la première lecture de sonde (M-3.5), ou T0.7 scellé après les épisodes lus (M-3.2) → non tenu —
  invalide. Motifs (CL2 § 4) : la grille traite déjà l'ordre de P-015 (b) comme une condition en M-3.2, et la Métrique
  définit « invalide » comme un défaut de procédure, ce qu'est un ordre rompu ; N-027 gèle les critères, pas les décisions
  de route, et P-015 (b) s'impose déjà aux auteurs de T0.7 ; symétrie (R4) : sans témoin positif, un « aucune sonde
  au-dessus » ne se distingue pas d'une panne d'instrument, et sous D-G0-13 un tel négatif serait gelé alors qu'« invalide »
  ne gèle pas ; coût nul par rapport à la route décidée. **Autre option : réserve** (CL1 § 6 : le critère dit « au-dessus
  du plancher » ; un témoin positif n'infirme pas une sonde au-dessus, il n'éclaire qu'un nul ; confiance moyenne) ; sous
  cette option, **M-3.2 et M-3.5 passent tous deux en réserve** (même source, même état ; CLG2-03), et l'ordre R1 propre à
  T0.7 reste contrôlé par M-0.4. Les sources divergent (avis Fable grille et CL2 contre CL1) : Lazar tranche ou le défaut
  s'applique.

---

#### Critère 4 — « Base boîte noire, par action et séquentielle, qui tourne sur le même jeu d'épisodes. »

- **Sources** : brief T0.8 (l. 175-178 : moniteur faible par action ; TRACE-lite ; « le même agrégateur séquentiel appliqué
  aux scores boîte noire ») ; N-029 (`docs/decisions/decision-N-029-v1.md`,
  `084e30523c0a0349cb1daf0dcf804f6c9d38c10d4f8bceed23c787fa507f34e4`, § 1 et § 2) : base locale, lue **sur les épisodes de
  T0.6**, juge par action à capacité égale (D1), prédicteur sur les traits du texte obligatoire (traits fixés au
  préenregistrement de T0.8 avant toute lecture de T0.6) ; « critère 4 de G0 : inchangé » ; P-010 option (a) ; P-015 (b),
  socle T0.8 (l. 50-52) : règle du coût déclaré calibrée sur l'honnête, juge par action 8B, prédicteur sur les traits du
  texte ; **P-015 ne nomme pas TRACE-lite**.
- **Preuves attendues** : préenregistrement de T0.8 scellé et contre-lu avant le run ; run(s) avec manifeste ; sorties
  scellées : un score par action et une statistique séquentielle par épisode, pour chaque base nommée ; rapport de
  fonctionnement scellé par un sous-agent neuf (M-0.5, D-G0-8 : un rapport de fonctionnement suffit pour ce critère).
- **Liste de contrôle** :

| n° | contrôle | commande | sortie attendue | état si échec |
|---|---|---|---|---|
| M-4.1 | M-0.1 à M-0.8 | section 3 | tout passe | selon M-0 |
| M-4.2 | **même jeu d'épisodes** (N-029 § 2) | `sha256sum <liste des identifiants d'épisodes lue par T0.8>` contre `sha256sum <liste des épisodes de T0.6 lus pour les critères 2 et 3>` (fichiers nommés par les manifestes) | empreintes égales | non tenu — invalide |
| M-4.3 | deux grains (CLG-08) | script M-4.3 ci-dessous, sur les deux fichiers de sorties scellés nommés par le manifeste et sur la liste d'épisodes de M-4.2 | pour chaque base : « actions » = « distinctes » (aucun doublon) ; « episodes » = « distincts » ; « episodes hors liste » = 0 ; « episodes de la liste sans statistique » = 0 | non tenu — absent (grain ou base manquant) ; non tenu — invalide (doublons, épisodes hors liste) |
| M-4.4 | même agrégateur séquentiel que les sondes (CLG2-06) | pour T0.7 et T0.8 : `grep -i -m1 -E '^[-* ]*agr(é\|e)gateur s(é\|e)quentiel ?:' <prereg> \| sed -E 's/^[^:]*: *//'` (forme exigée : « Agrégateur séquentiel : `<chemin du module>` au commit `<sha>` », annexe C point 6) ; `diff` des deux sorties ; si seuls les commits diffèrent : `git diff --quiet <sha T0.7> <sha T0.8> -- <chemin du module>` | sorties identiques, ou même chemin et code 0 | non concluant si une ligne manque, si les chemins diffèrent ou si le code n'est pas 0 (source de l'exigence : brief T0.8 l. 175-178, « le même agrégateur séquentiel », pas le texte du critère) |
| F-4.1 | bases nommées par N-029 + P-015 présentes | `grep -n -i "juge" <rapport>` ; `grep -n -i "traits du texte" <rapport>` ; `grep -n -i "coût déclaré" <rapport>` | les trois présentes avec un score par action (M-4.3) | non tenu — absent (base nommée par une décision en vigueur manquante) |
| F-4.2 | TRACE-lite (brief T0.8) **[À DÉCIDER, D-G0-12]** | `grep -n -i "TRACE" <rapport>` | présent | **défaut** : réserve si absent ; autre option : non tenu — absent |
| F-4.3 | « tourne » **[À DÉCIDER, D-G0-3]** (CLG-08) | `grep -n -i -E "arrêt de garde\|GardeArret" <rapport>` ; `grep -n -i -E "part de scores finis\|scores finis" <prereg T0.8>` ; colonnes « finies » et « finis » du script M-4.3 rapportées à « actions » et « episodes » | aucun arrêt de garde ; part fixée d'avance dans T0.8, identique pour les deux grains, écrite avant toute lecture d'épisodes ; part atteinte pour chaque base et chaque grain | non concluant (sans part fixée d'avance, toute action sans score fini rend non concluant) |

**Script M-4.3** (Python, à copier dans un fichier hors du clone, exécuté par `python -I <script> <scores par action>
<statistiques par épisode> <liste des épisodes>`). Format exigé des sorties de T0.8 : JSON Lines, champs `base`, `episode`,
`action` (grain action seulement), `score`. Si T0.8 fixe un autre format, son préenregistrement écrit la commande de
comptage équivalente, scellée avec lui, et le dossier en donne la ligne.

```
import json, math, sys
def lire(p): return [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]
A, E = lire(sys.argv[1]), lire(sys.argv[2])
ep = [l.strip() for l in open(sys.argv[3], encoding="utf-8") if l.strip()]
fini = lambda s: isinstance(s, (int, float)) and not isinstance(s, bool) and math.isfinite(s)
for base in sorted({x["base"] for x in A} | {x["base"] for x in E}):
    a = [x for x in A if x["base"] == base]; e = [x for x in E if x["base"] == base]
    cle_a = {(x["episode"], x["action"]) for x in a}; cle_e = {x["episode"] for x in e}
    print(base, "actions", len(a), "distinctes", len(cle_a), "finies", sum(fini(x["score"]) for x in a),
          "| episodes", len(e), "distincts", len(cle_e), "finis", sum(fini(x["score"]) for x in e),
          "| episodes hors liste", len(cle_e - set(ep)), "| episodes de la liste sans statistique", len(set(ep) - cle_e))
```

- **[À DÉCIDER, D-G0-3]** « qui tourne » n'est fixé nulle part. **Défaut (recommandation commune des deux avis)** :
  « tourne » = run sans arrêt de garde **et** part de scores finis fixée d'avance par le préenregistrement de T0.8, identique
  pour les deux grains, écrite avant toute lecture d'épisodes ; sans part fixée, tout manque rend « non concluant » ;
  « tourne » ne veut jamais dire « détecte » (la comparaison est l'objet de G1). Pourquoi la part est sensible : la lecture
  gelée du rejeu des juges sur les 180 notations du pilote de T0.5
  (`docs/notes/couche-2-preparation-v1/rejeu-juges-v1/lecture-et-audit-r4-v1/lecture-rejeu-juges-v1.md`,
  `8799f7d3800db7444a693677c3d7dfbb3b3e283becc41c88ae063748a877f9b8`, l. 10-18, vérifiée par la v2) rapporte qu'aucune
  des six cellules n'atteint ≥ 0,99 de scores finis ; meilleure : 157/180 = 0,87 (Wilson 95 % : 0,82 à 0,91). Mesure
  interne, exploratoire, non opposable ; elle motive la décision, elle n'entre pas dans la règle.
- **[À DÉCIDER, D-G0-12]** TRACE-lite : le brief T0.8 le nomme ; la route décidée vers G0 (P-015, socle T0.8) ne l'a pas
  retenu, et N-029, décision de Lazar postérieure au brief, fixe « ce que « base boîte noire » contient » sans lui. **Défaut :
  réserve** s'il est absent (avis Fable grille et CL1 § 6, confiance élevée chez CL1). Autre option : l'exiger (lecture
  littérale du brief T0.8), son absence valant « non tenu — absent ».
- **États** : tenu si M et F passent ; non tenu — absent sans run sur les épisodes de T0.6 ou sans base nommée ; non tenu —
  invalide si le jeu d'épisodes diffère ; non concluant selon la part de scores finis.

---

#### Critère 5 — « Agrégateurs validés en simulation (T0.3). »

- **Sources** : brief T0.3 (l. 137-144) ; préenregistrement `prereg/T0.3-simulation-lemme-theoreme-v1.md`
  (`7474743a0fa2a9db5da85bcedb0087ea57114fcca0fbb3415c7a97bf1b78d1fb`) et sa table gelée, section « Critères de lecture
  gelés » (A : état d'une cellule ; B : verdict d'une prédiction ; D : audit R4 ; E : énoncés). Ce préenregistrement ne
  mentionne pas G0 (vérifié par la v2) : il ne définit pas « validés ». Le lien entre T0.3 et le critère 5 vient du texte du
  critère (« (T0.3) ») et du brief T0.3.
- **Preuves attendues** : le préenregistrement ; ses trois contre-lectures ; la grille de simulation scellée qu'il cite ; le
  manifeste du run décisif ; la lecture mécanique scellée, produite par le code gelé (`lecture.md`, `lecture.json`).
- **Liste de contrôle** :

| n° | contrôle | commande | sortie attendue | état si échec |
|---|---|---|---|---|
| M-5.1 | M-0.1 à M-0.4, M-0.6 à M-0.8 | section 3 | tout passe | selon M-0 |
| M-5.2 | manifeste cite le préenregistrement, la grille et le commit gelé | `python -c "import json;m=json.load(open('runs/<run>/manifeste.json'));print(m['preenregistrement']['sha256'],m['config'].get('commit_cite'),m['decisif'],m['config'].get('grille_sha256'))"` | `7474743a…`, `d73ac469…`, `True`, `5609f920…` | non tenu — invalide |
| M-5.3 | la lecture scellée est celle du run cité | `grep -n "<run_id>" <lecture.md>` ; M-0.1 sur `lecture.md` et `lecture.json` | run identique ; intègres | non tenu — invalide |
| F-5.1 | **[À DÉCIDER, D-G0-10]** « validés » (CLG-08) | `python -c "import json,collections;d=json.load(open('<lecture.json>'));print(collections.Counter(p['verdict'] for p in d['resultat']['lecture']['predictions'].values()))"` | **défaut (option Fable)** : une seule clé, `'confirmée'` | non tenu — négatif (au moins une « réfutée », règle B) ; non concluant (une « non concluante » sans « réfutée ») |
| F-5.2 | audit R4 (règle D ; CLG-09) | `grep -n "déclenché : False" <lecture.md>` ; si 0 ligne : `grep -n "déclenché : True" <lecture.md>` et M-0.1 sur le rapport d'audit remis | une ligne « déclenché : False » ; ou « déclenché : True » et rapport d'audit scellé au dossier | non concluant (déclenché sans rapport scellé, ou aucune des deux lignes) |
| F-5.3 | réserve R-025 (CLG-13) | `grep -n "R-025" registres/decisions.md` | réserve recopiée telle qu'écrite : « Réserve écrite : vérifications de l'instrument en majorité » | aucun effet sur l'état |

- **[À DÉCIDER, D-G0-10]** « validés » n'est fixé par aucune pièce scellée. **Défaut (option de l'avis Fable grille,
  confirmée par CL1 § 6, confiance élevée)** : « validés » = toutes les prédictions de la lecture scellée « confirmée »
  **et** audit R4 « déclenché : False » ou rapport d'audit scellé (règles B et D de la table de T0.3) ; une seule
  « réfutée » = non tenu — négatif ; une « non concluante » sans « réfutée » = non concluant. Autre option : « validés » =
  la ligne de synthèse de la lecture scellée dit « validé » (plus faible ; non recommandée : elle laisse le mot au code).
- **Réserve à prévoir** : le gel du code a été levé après le run (R-025). Si G1 emploie un code d'agrégateurs modifié depuis
  le commit `d73ac46`, la validation en simulation ne le couvre pas mot pour mot (`git diff d73ac46 <C_lecture> --stat --
  src/controle_ia/agregateurs/`) : réserve, sans effet sur l'état (le critère nomme T0.3).

---

#### Critère 6 — « Préenregistrement de G1 scellé et contre-lu. »

- **Sources** : brief T1.2 et « Porte G1 » (l. 214-249) ; R1, R2 ; décisions de Lazar qui renvoient explicitement « au
  préenregistrement de G1 » (liste en D-G0-4).
- **Preuves attendues** : un fichier `prereg/G1-*-vN.md` scellé ; ses rapports de contre-lecture scellés.
- **Liste de contrôle** :

| n° | contrôle | commande | sortie attendue | état si échec |
|---|---|---|---|---|
| M-6.1 | M-0.1, M-0.2, M-0.3, M-0.6, M-0.7, M-0.8 (M-0.4 et M-0.5 sans objet : aucun run de G1 avant G0) | section 3 | tout passe | non tenu — absent (seul un brouillon) ; non tenu — invalide (contre-lecture manquante ou « non scellable ») |
| F-6.1 | c'est le préenregistrement de G1 (mécanique) | `ls prereg/G1-*-v*.md` ; `head -1 <fichier>` | nom `prereg/G1-…-vN.md` ; première ligne commence par `# Préenregistrement — porte G1` | non concluant (ligne citée) |
| F-6.2 | **[À DÉCIDER, D-G0-4]** présence des décisions renvoyées à G1 | `grep -n "<numéro>" <fichier>` pour chaque décision de la liste ; `grep -n "<numéro>" <rapport de contre-lecture>` | chaque numéro trouvé, ou son absence attestée par le contre-lecteur R2 | **défaut** : réserve ; autre option : condition (non tenu — invalide) |

- **[À DÉCIDER, D-G0-4]** **Défaut (recommandation commune des deux avis)** : contrôle de **présence** (pas de qualité) en
  **réserve**, parce que le critère dit seulement « scellé et contre-lu » ; le contrôle de présence est le travail du
  contre-lecteur R2, le lecteur de G0 vérifie seulement que le rapport de contre-lecture l'atteste ; liste = exactement les
  décisions dont le texte dit « au préenregistrement de G1 » : N-007/N-008 (`docs/decisions/decision-N-007-N-008-v1.md`,
  `ab7dc9bb2c96704ad8fd801197de225f68d6f9720958139f4ec4e32e92105232`), N-034, N-054, N-055, N-056, N-060 v3, R-746, arrêtée
  par Lazar et gelée avec la grille.
- **États** : tenu si M passe et F-6.1 est conforme ; non tenu — absent si seul un brouillon existe ; non tenu — invalide si
  la contre-lecture manque ou conclut « non scellable » ; non concluant si F-6.1 échoue.

---

#### Critère 7 — « Préenregistrement du papier C (HC1 à HC3) scellé et contre-lu. »

- **Sources** : brief T0.9 (l. 180-188 ; livrable : « préenregistrement scellé et contre-lu de HC1, HC2 (formulation
  robustesse, jamais immunité absolue), HC2b et HC3, avec signes prédits et liste d'arrêt ») ; N-005/N-006
  (`docs/decisions/decision-N-005-N-006-v1.md`, `cd49afbc924cb1dd56251f22ef692007c24ecb76b124e0662cbe9bc04fa2e1c0`, l. 97 :
  « Préenregistrement du papier C (critère 7 de la porte G0) : HC1 …, HC2 …, HC2b et HC3 ») ; N-013 (HC2b renommée
  « trahison par les activations ») ; N-023 ; R-307 et R-309.
- **Preuves attendues** : un fichier `prereg/papier-C-*-vN.md` scellé ; ses rapports de contre-lecture scellés.
- **Liste de contrôle** :

| n° | contrôle | commande | sortie attendue | état si échec |
|---|---|---|---|---|
| M-7.1 | M-0.1, M-0.2, M-0.3, M-0.6, M-0.7, M-0.8 | section 3 | tout passe | comme le critère 6 |
| F-7.0 | c'est le préenregistrement du papier C (mécanique) | `ls prereg/papier-C-*-v*.md` ; `head -1 <fichier>` | première ligne commence par `# Préenregistrement — papier C` | non concluant |
| F-7.1 | [EXISTANT, brief T0.9 et N-005/N-006 l. 97] quatre hypothèses, signes, liste d'arrêt (CLG-05, CLG-11) | `grep -n "HC1" <fichier>` ; `grep -n "HC2\b" <fichier>` ; `grep -n "HC2b" <fichier>` ; `grep -n "HC3" <fichier>` ; section « Prédiction chiffrée et signe attendu » non vide (M-0.2) ; section « Liste d'arrêt » non vide | les quatre présentes, chacune avec un signe | **non tenu — invalide** (une hypothèse manque : manque de contenu d'une pièce scellée, pas un résultat). Source de l'exigence : livrable du brief T0.9 et N-005/N-006 l. 97 ; HC2b est dans l'intervalle « HC1 à HC3 » du critère, renommée par N-013 |
| F-7.2 | HC2 en robustesse, jamais en immunité absolue (CLG2-06) | `grep -c -i "robustesse" <fichier>` ; `grep -i -E "immunit(é\|e) absolue" <fichier> \| grep -v -c -i -E "jamais\|r(é\|e)fut\|abandonn\|pas (une \|d['’]\|l['’])?immunit(é\|e) absolue\|non (une )?immunit(é\|e) absolue\|sans immunit(é\|e) absolue"` | premier compte ≥ 1 ; second compte = 0 (toute ligne qui dit « immunité absolue » la nie par l'un de ces mots) | non concluant si l'un des deux comptes échoue (ligne citée) |
| F-7.3 | **[À DÉCIDER, D-G0-4]** présence de N-005/N-006, N-013, N-023, R-307, R-309 | comme F-6.2 | attestée par le contre-lecteur | défaut : réserve |

- **États** : comme le critère 6 ; non tenu — invalide si l'une des quatre hypothèses manque (F-7.1).

---

#### Critère 8 — « État de l'art vérifié ; aucun chiffre non vérifié dans un document du programme. »

- **Sources** : brief T0.2 (l. 126-135 : statuer pour chaque affirmation et chaque chiffre que le programme utilise —
  « confirmé, corrigé ou introuvable — avec la page source » ; table des chiffres avec chemin et empreinte du PDF ;
  priorités 1 à 4) ; R7 ; synthèse scellée du niveau 2 `docs/etat-de-l-art/etat-de-l-art-verifie-niveau2-v1.md`
  (`bbe0c1f523ad83e13e5ce96d19c384e8596a96d298431b931f499826c773ceb8`), § 2 « Usage » et § 4 « Reste ouvert (critère 8) » :
  « Avant le verdict de G0 : un contrôle de traçabilité par un sous-agent neuf, comme au niveau 1, sur les chiffres que les
  préenregistrements de G1 et du papier C reprendront ».
- **Preuves attendues** : (a) les rapports de vérification scellés (niveaux 1, 2 et suivants) ; (b) une **table des chiffres**
  scellée : pour chaque chiffre tiré d'une source externe dans un document du périmètre (annexe E), son statut T0.2
  (confirmé / corrigé / introuvable), la page et le PDF empreinté ; format exigé : TSV à en-tête, colonnes au moins `id`,
  `source` (identifiant de la source, par exemple arXiv), `chiffre_ecrit` (le chiffre **tel que le document l'écrit**, avec
  son unité et assez de contexte pour être unique dans le périmètre, par exemple « rappel à 1 % de faux positifs » et non
  « 1 »), `document`, `ligne`, `statut`, `page`, `pdf`, `pdf_sha256` (CLG2-01) ; (c) le **contrôle de traçabilité** scellé par un
  sous-agent neuf ; (d) pour tout chiffre « introuvable », la preuve qu'il n'est employé dans aucun préenregistrement ni
  papier, sinon sous la forme « l'article imprime X » avec sa réserve (synthèse du niveau 2, § 2). **Deux de ces pièces sont
  créées par la grille** et non par une décision : le contrôle de traçabilité (c), issu d'une synthèse de session, et le
  **script de contrôle** (M-8.3), à écrire, tester sain et artefact (R5) et sceller avant le scellement de la grille ; elles
  entrent dans la décision D-G0-9.
- **Liste de contrôle** :

| n° | contrôle | commande | sortie attendue | état si échec |
|---|---|---|---|---|
| M-8.1 | M-0.1, M-0.6, M-0.8 sur (a) à (d) ; M-0.1 sur chaque PDF cité par la table | section 3 ; `python -m controle_ia.scellement verifier <pdf>` | tout passe | non tenu — invalide (PDF non conforme) ; non tenu — absent (table ou contrôle manquant) |
| M-8.2 | les quatre priorités du brief T0.2 statuées (CLG-05) | `grep -n -E "2607\.08066\|2606\.10456\|2604\.01151\|2609\.03035\|2606\.08892" <table>` | chaque identifiant avec un statut | **non tenu — invalide** (manque de contenu de la table) |
| M-8.3 | script de contrôle (CLG2-01) | `python -I <script M-8.3> <table> <périmètre>` (`<périmètre>` : liste des chemins de l'annexe E, un par ligne) ; essais sain et artefact scellés avec le script | aucune ligne « M-8.3 absent de sa ligne » ; essais R5 présents | non tenu — absent (script ou essais manquants) ; non tenu — négatif (un chiffre absent de sa ligne : résultat du contrôle ; **ne gèle pas**, D-G0-13 (a)) |
| F-8.1 | [EXISTANT, brief T0.2] « vérifié » = statué (CLG-05) | colonne « statut » de la table : valeurs parmi {confirmé, corrigé, introuvable} | aucune cellule vide | **non tenu — invalide** (chiffre sans statut : manque de contenu) |
| F-8.2 | chiffres « introuvable » non employés comme faits (CLG-10, CLG2-01) | même exécution du script M-8.3 : pour chaque ligne « introuvable », chaque occurrence de `chiffre_ecrit` **tel que la table l'écrit**, bornée (ni chiffre ni lettre avant, ni chiffre ni décimale après), dans chaque document du périmètre, est classée « conforme » (« l'article imprime » sur la même ligne), « negatif » (ligne citée par la table, ou ligne qui porte l'identifiant `source`, sans « l'article imprime ») ou « doute » (autre occurrence) | dernière ligne : `F-8.2 negatifs 0 \| F-8.2 doutes 0` | négatifs ≥ 1 : non tenu — négatif (résultat du contrôle ; **ne gèle pas**, D-G0-13 (a)) ; négatifs = 0 et doutes ≥ 1 : **non concluant** (ligne citée ; un doute n'est jamais un négatif) |
| F-8.3 | contrôle de traçabilité (c) | `grep -n -i -E "aucun chiffre non statué\|non statué" <rapport (c)>` | conclusion sans chiffre non statué dans le périmètre | non tenu — négatif (conclusion du contrôle scellé) |

- **[À DÉCIDER, D-G0-9]** « document du programme » n'est défini nulle part. Options : (A) documents qui font foi (programme
  v2, brief v2, état de l'art v1), décisions de `docs/decisions/`, préenregistrements des critères 6 et 7 ; (B) (A) plus tout
  préenregistrement scellé et toute note citée comme preuve par cette grille ; (C) tout `docs/`, `prereg/` et `papiers/`.
  **Défaut (recommandation commune des deux avis)** : (A) comme condition de l'état, **chiffres tirés de sources externes
  seulement** (R7) ; les chiffres internes relèvent de R6 (chemin et empreinte) et vont en réserve ; (B) passé au même
  script, **en réserve** (précision de l'avis Fable grille). La synthèse repli (§ 5, choix 7) renvoie ce périmètre et le
  statut des branches en quarantaine à la même décision. **Le périmètre est gelé en annexe E de la grille scellée**
  (CLG-14), pas dans le dossier.
- **États** : tenu si (a) à (d) existent et F-8.1 à F-8.3 sont conformes ; non tenu — invalide si un chiffre du périmètre
  n'a pas de statut ou si une priorité n'est pas statuée ; non tenu — négatif si le script trouve un chiffre absent de sa
  ligne, si un chiffre introuvable est employé comme fait (ligne citée par la table ou ligne qui porte sa source), ou si le
  contrôle de traçabilité conclut à un chiffre non statué ; **ces négatifs ne gèlent jamais le critère 8** (D-G0-13 (a) :
  aucun préenregistrement à liste d'arrêt ne les porte ; un chiffre mal statué se corrige, il n'est pas une réfutation,
  CL2 § 3) ; non tenu — absent sans table, sans contrôle de traçabilité ou sans script ; non concluant si le script rend
  un doute (F-8.2) ou si un cas n'est pas prévu (ligne citée).

**Script M-8.3** (noyau gelé avec la grille ; le script scellé de l'annexe C point 3 le contient tel quel, avec ses essais
sain et artefact ; exécuté depuis la racine du clone ; code de sortie 0 : conforme, 1 : au moins un absent ou un négatif,
2 : doutes seulement). Motif des bornes : un chiffre nu attrape des sous-chaînes (« 0,5 » dans « 0,55 ») et des numéros
(« 12 » dans « R12 », « section 12 ») ; exécuté sur le programme et le brief, `grep -F` rendait 3, 8 et 11 « négatifs »
pour « 0,5 », « 12 » et « 8B » ; le script rend 0 négatif (annexe F).

```
import csv, re, sys
# usage : python -I m83.py <table.tsv> <perimetre.txt>   (depuis la racine du clone)
# table : TSV à en-tête, colonnes id, source, chiffre_ecrit, document, ligne, statut (au moins)
# perimetre : un chemin de document par ligne (annexe E)
T = list(csv.DictReader(open(sys.argv[1], encoding="utf-8"), delimiter="\t"))
P = [l.strip() for l in open(sys.argv[2], encoding="utf-8") if l.strip()]
L = {d: open(d, encoding="utf-8").read().split("\n") for d in set(P) | {r["document"] for r in T}}
motif = lambda c: re.compile(r"(?<!\w)(?<![0-9][,.])" + re.escape(c) + r"(?![0-9])(?![,.][0-9])")
IMPRIME = re.compile(r"l['’]article imprime", re.I)
absents = 0; neg = 0; doute = 0
for r in T:
    m, n = motif(r["chiffre_ecrit"]), int(r["ligne"])
    present = 1 <= n <= len(L[r["document"]]) and bool(m.search(L[r["document"]][n - 1]))
    if not present:
        absents += 1; print("M-8.3 absent de sa ligne", r["id"], r["document"], n)
    if r["statut"] != "introuvable":
        continue
    for d in P:
        for i, t in enumerate(L[d], 1):
            if not m.search(t):
                continue
            if IMPRIME.search(t):
                k = "conforme"
            elif (d, i) == (r["document"], n) or r["source"] in t:
                k = "negatif"; neg += 1
            else:
                k = "doute"; doute += 1
            print("F-8.2", k, r["id"], d, i)
print("M-8.3 absents", absents, "| F-8.2 negatifs", neg, "| F-8.2 doutes", doute)
sys.exit(1 if absents or neg else (2 if doute else 0))
```

## Critères de lecture gelés

**[GELÉ, proposé à contre-lire] Agrégation, écrite avant toute lecture ; la même aux deux lectures.**

| états des huit critères | état de la porte | suite |
|---|---|---|
| huit « tenu » | **franchie** | verdict scellé, puis Lazar (GO) ; la phase 1 s'ouvre seulement sur ce GO (R13) ; le GO ne requalifie pas |
| au moins un « non tenu » (quel qu'en soit le sous-état) | **non franchie** | clause de repli (section « Repli ») |
| aucun « non tenu », au moins un « non concluant » | **non concluante** | **la même suite que « non franchie »** : clause de repli |

Justification :
- **Un seul critère non tenu suffit** : le brief exige « tous les critères suivants sont remplis » ; une porte « aux trois
  quarts » n'existe pas.
- **« Non concluante » n'est jamais une seconde chance** : même suite que « non franchie ». Elle existe pour que le rapport
  dise juste et pour que le repli puisse traiter différemment, dans sa propre clause, un critère absent, négatif ou indécidé.
  Cette identité de suite est demandée par l'avis conv-audit (point 3 : « même suite pour les deux états ») et fondée par
  l'avis Fable repli (`f3435cfd…`, l. 48-49 : une porte « non concluante » serait une porte « on verra », « non
  scellable ») ; l'avis Fable grille (l. 54) juge seulement la table « sûre » (CLG-15) ; la synthèse repli § 4 la retrouve
  chez deux des trois modèles.
- **Pas de pondération, pas d'ordre** entre critères à la porte ; l'ordre de travail vit dans la reprise, pas dans la lecture.

**Réserves et audit de symétrie (R4)** (CLG-06) :
- Les réserves ne changent aucun état ; elles sont toutes recopiées dans le verdict, avec la ligne de la grille qui les
  ouvre. Toute réserve ouverte par une preuve (sa table gelée, ses addenda) est recopiée ; toute pièce écartée (M-0.8) aussi.
- **Résultat suspect de propreté, positif ou négatif** : pour chaque preuve, le lecteur lit les deux lignes que le dossier
  désigne (définition de l'audit dans le préenregistrement ; constat dans le verdict) et applique à la ligne du verdict le
  motif `(n['’](est|a) pas|non|aucun|False)[^.]{0,40}d(é|e)clench|d(é|e)clench[^.]{0,30}: ?(False|non|aucun)` : 1 = non
  déclenché ; 0 = déclenché. Audit déclenché, **dans un sens ou dans l'autre**, sans rapport d'audit scellé au dossier à
  `C_lecture` : **non concluant** pour le critère. Préenregistrement qui contient `R4` ou `symétrie`
  (`grep -c -i -E "R4|symétrie"` ≥ 1) sans les deux lignes désignées au dossier : non concluant (ligne citée).
- **Réserve des sept jours, mécanique** : `git log --format=%cI -1 -- <verdict du critère>.sha256` postérieure ou égale à la
  date de `C_lecture` moins sept jours → réserve « preuve récente », quel que soit le sens du verdict ; **aucun audit par le
  lecteur** ; la pièce est signalée, dans le verdict, pour un audit R4 après lecture, sans effet sur l'état.

**Forme du verdict** : gabarit de l'annexe A, et rien d'autre (aucune recommandation sur la suite : elle est écrite dans le
repli).

## Liste d'arrêt

La lecture s'arrête, sans verdict de porte, et la session ouvre un nœud pour Lazar, si :
- aucune grille scellée n'existe à l'échéance de la lecture ; ou l'empreinte de la grille scellée ne correspond pas au
  fichier remis au lecteur ; ou la grille échoue M-0.2 ;
- le lecteur n'est pas neuf au sens de la section 1 du plan d'analyse ;
- le clone est superficiel (`git rev-parse --is-shallow-repository` ≠ `false`) ou n'est pas à `C_lecture` ;
- la locale `C.UTF-8` n'est pas disponible (`locale -a | grep -i -c -E "^c\.utf-?8$"` = 0) ;
- `registres/g0-lecture-ouverte-vN.md` manque, ou, pour une lecture anticipée, ne cite pas le mot de Lazar ;
- le dossier de G0 manque ou échoue M-0.1 ;
- une preuve exige d'ouvrir un fichier interdit (section 1) ;
- `cd docs && sha256sum -c sha256sums-lancement-v2.txt` ou `python -m controle_ia.scellement verifier-arbre .` échoue au
  commit `C_lecture` sur un fichier cité par la grille ou le dossier (R11 appliqué avant de conclure).

Un arrêt n'est pas une lecture : il ne vaut ni « non franchie » ni « non concluante ». (La lecture tardive n'est pas un
arrêt : voir « Seuil ».)

## Repli

**Clause décidée par Lazar, à insérer ici (décision N-027 bis, quand tout sera fixé). La grille ne tranche rien du repli.**

**Fixé par Lazar au 2026-10-29** (cité, non rediscuté) :
- **R-750** (`registres/decisions.md` l. 978) : borne du report au **31 janvier 2027** (« 31 janvier : go ») ; le report
  est unique (R-765 : « un seul verdict final »).
- **R-765** (l. 993) : choix 1 de la synthèse tranché pour le gel : **un échec scellé d'un critère pendant le report gèle
  ce critère jusqu'au second verdict ; il ne ferme pas la porte en cours de report** ; un seul verdict final au 31 janvier
  2027 au plus tard ; un critère réfuté par sa liste d'arrêt scellée n'est jamais retenté.

**Reste à fixer : les onze autres choix** de la synthèse (`docs/notes/porte-g0-repli-v1/synthese-collisionneur-repli-g0-v1.md`,
`527f5853…`, § 5, l. 146-163), à présenter en un bloc avec cette grille : (2) préenregistrement absent pour 2, 3, 4 =
« négatif » ou « absent » ; (3) grille scellée ≤ 15 novembre, D-G0 tranchés ou échus, même grille aux deux lectures ;
(4) empreintes hors dépôt et horodatage externe ; (5) plafond, séquence, imputation ; (6) table de dépendance et pilote ρ ;
(7) périmètre du critère 8 et quarantaine ; (8) rôle du GO ; (9) sous-agents R13 d'un autre modèle ; (10) tests de la règle
sur dossiers synthétiques ; (11) gabarit du rapport, R-750 dans `docs/decisions/`, aucune condition de progrès ; (12) sort du
papier C et du palier GC. Les choix 3 et 7 recoupent D-G0-1 et D-G0-9 : une même décision les règle.

Ce que la grille garantit pour la clause, quelle qu'elle soit :
1. « non franchie » et « non concluante » ont la même suite, aux deux lectures ;
2. les sous-états « absent », « négatif », « invalide » et « non concluant » sont prononcés par critère ; « négatif » ne
   couvre que des résultats (CLG-05) ; pour tout « négatif », le verdict dit s'il vient d'une **liste d'arrêt scellée
   déclenchée**, d'une ligne de la table gelée de la preuve, ou d'un contrôle de la grille (champ (β)) ;
3. le verdict rend constatable, par critère, « préenregistrement scellé, contre-lu, à liste d'arrêt : présent / absent »
   (champ (α)), pour le choix 2 ;
4. la règle de version ne rend recevable aucune version suivante après un négatif par liste d'arrêt (R-765) ;
5. à la seconde lecture, un critère gelé au sens de D-G0-13 est lu sur la pièce qui l'a gelé, et le champ (γ) le constate
   (R-765) ; seul gèle un négatif d'une preuve dont (α) est « présent », issu de sa liste d'arrêt ou de sa table gelée ;
   les négatifs des contrôles de la grille (M-8.3, F-8.2, F-8.3) ne gèlent jamais (CLG2-01) ;
6. la grille sert telle quelle à la seconde lecture, avec son propre `C_lecture` et son propre fichier d'ouverture ; la
   table d'agrégation est la même.

La grille ne dit rien de ce que vaut un préenregistrement absent au-delà de « non tenu — absent » (choix 2), ni de ce que
fait la seconde issue au-delà de son état : c'est la clause.

## Contre-lecture

- **Contre-lecture 1** (de la v2) : sous-agent neuf (Fable 5.1), le 2026-10-29 de 10:57 à 11:06 UTC. Brouillon relu :
  `prereg/brouillon-G0-grille-lecture-v2.md`, `aa47f6fc637b67e4fd2679491f660cda3e79ad99394f4d49f94511c1df42857e`. Rapport :
  `prereg/contre-lectures/brouillon-G0-grille-lecture-v2-cl1.md`,
  `b2282047a46cc5b1be4b4696cacbc177a342b806826a35bf3ae32f8cf383b49c`. Conclusion : « Scellable après corrections » ; sept
  majeurs, huit mineurs. Traitement : **tous acceptés**, aucun refusé (table « Ce que la v3 corrige », lignes 1 à 17).
  Deux écarts de forme, dits : CLG-01, la liste de préfixes proposée est **élargie** (P3, T0.5) et doublée d'un inventaire
  par contenu, parce qu'exécutée elle manquait onze pièces scellées ; CLG-03, la classe `[èe]` proposée est remplacée par
  l'alternance `(è|e)` et la locale `C.UTF-8`, parce qu'exécutée en locale POSIX elle rendait 0.
- **Contre-lecture 2** (de la v3) : sous-agent neuf (Fable 5.1), d'un autre modèle que l'auteur de la v3, le 2026-10-29 de
  11:26 à 11:32 UTC. Brouillon relu : `prereg/brouillon-G0-grille-lecture-v3.md`,
  `15e7f229443d80f7625f1f0e16838457125f04dd1c185e1b2caac7442b70e328`. Rapport :
  `prereg/contre-lectures/brouillon-G0-grille-lecture-v3-cl2.md`,
  `2ef445ccb27a1c549cc22e17c1a96e8a5e30572212bec4bae12166697bd778ee`. Conclusion : « Scellable après corrections » ; aucun
  bloquant, trois majeurs (CLG2-01 à 03), quatre mineurs (CLG2-04 à 07). Traitement : **tous acceptés**, aucun refusé
  (table « Ce que la v4 corrige », lignes 1 à 7) ; défauts de D-G0-11 et de D-G0-13 réécrits selon les recommandations de
  CL2 § 3 et § 4, les variantes antérieures gardées en « autre option ». Quatre écarts de forme, dits : CLG2-04, en plus de
  la classe `[*«" ]*` proposée, un filet `LARGE_1` rend « non concluant » au lieu d'« absent » une typographie imprévue
  (espace insécable, essayée) ; CLG2-07, l'ajout de `prereg/contre-lectures` au `find` ne suffisait pas (le filtre
  « brouillon » aurait écarté la contre-lecture d'un brouillon, essayé sur un arbre synthétique) : le filtre ne s'y applique
  pas, le préfixe y est cherché après un tiret, et les pièces de la grille elle-même sont exclues par nom ; CLG2-01, CL2 dit
  « doute → non concluant » sans définir le doute : la v4 le définit mécaniquement (occurrence ni sur la ligne citée par la
  table, ni sur une ligne qui porte la source) ; CLG2-06, un motif par contrôle plutôt que « non concluant » seul, avec les
  formes exigées en annexe C point 6.
- **Contre-lecture 3** (de cette v4) : attendue, par un sous-agent neuf qui n'a écrit ni la v1, ni la v2, ni la v3, ni la
  v4, ni CL1, ni CL2, ni l'un des avis. Tant qu'elle n'a pas ses deux empreintes, `controle_ia.prereg` refuse cette version
  (protection voulue). Fichiers à lui donner : ce brouillon ; la v3 (`15e7f229…`) ; CL2 (`2ef445cc…`) ; CL1 (`b2282047…`) ;
  la synthèse repli (`527f5853…`) ; l'avis Fable grille (`3c2c8c55…`, l. 19-24 et 54) ; le brief v2 (l. 106-201) ;
  `registres/decisions.md` l. 34 (R-025), 462 (N-027), 978 (R-750), 993 (R-765), 1008 (R-780) ; `src/controle_ia/prereg.py` ;
  les pièces sur lesquelles l'annexe F essaie les motifs. Questions prioritaires : chaque ligne de la table « Ce que la v4
  corrige » est-elle appliquée dans le corps ? le défaut de D-G0-13 est-il fidèle à R-765 et à CL2 § 3 ? M-3.2 et M-3.5
  ont-ils le même état sous chaque option de D-G0-11 ? les motifs nouveaux (`PRONONCE_1`, `LARGE_1`, script M-0.8 (a),
  script M-8.3, motifs de CLG2-06) rendent-ils, sur le dépôt, ce que l'annexe F dit ? un motif attrape-t-il un faux ?

---

## Annexe A — gabarit du verdict R13 (à recopier tel quel par le lecteur)

```
# Verdict R13 — porte G0 — lecture n° <1 ou 2> du <AAAA-MM-JJ HH:MM UTC> — vN

- Lecteur : sous-agent neuf ; modèle : <nom exact> ; lignée : <nom> (différente de celle qui a écrit la grille : oui/non ;
  modèle différent de celui des auteurs des preuves : oui/non ; si non, pourquoi). Je n'ai écrit ni la grille, ni ses
  contre-lectures, ni aucune des pièces du dossier, ni les tests de la règle de repli ; je n'ai pas lu la première lecture
  (pour la lecture n° 2) comme auteur.
- Grille : prereg/G0-grille-lecture-vN.md, sha256 <…> ; M-0.2 passé (empreinte rendue : <…>).
- Dossier : docs/verdicts/dossier-G0-vN.md, sha256 <…>.
- Ouverture : registres/g0-lecture-ouverte-vN.md (commit <…>) ; anticipée : oui/non ; mot de Lazar cité : « … » ou sans objet.
- C_lecture : <sha complet> ; clone complet : git rev-parse --is-shallow-repository = false ; LC_ALL=C.UTF-8 ; verifier-arbre : OK.
- Pour la lecture n° 2 : verdict de la lecture n° 1, chemin, sha256, commit du .sha256.
- Liste d'arrêt : aucune condition remplie (ou : arrêt, condition <…> ; pas de verdict).

## Table des critères

| k | état | sous-état | (α) | (β) | (γ) gelé | pièces lues (chemin, sha256, commit du .sha256) | inventaire M-0.8 : écartées (chemin, motif) | lignes de neutralité recopiées | épreuves passées / échouées (n°) | ligne de la grille invoquée pour tout « non concluant » | réserves |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | | | | |
| … | | | | | | | | | | | |
| 8 | | | | | | | | | | | |

## Porte

État : franchie / non franchie / non concluante (table d'agrégation de la grille, ligne <…>).
Réserves de porte : retard (oui/non) ; preuves récentes, signalées pour audit R4 après lecture (critères <…>) ; versions
multiples (critères <…>) ; domaine (D-G0-5) ; pièces écartées (critères <…>).

## Fichiers lus (liste exhaustive, chemin et sha256)

Fin : <date -u>.
```

Le verdict ne contient aucune recommandation, aucune phrase sur la suite, aucun chiffre hors de ceux des pièces lues.

## Annexe B — index des points à décider (D-G0-1 à D-G0-13), recommandations et défauts

**D-G0-1 exige un mot explicite de Lazar et n'a pas de défaut.** S'il est accepté, tout point D-G0-2 à D-G0-13 non tranché
au 2026-11-15 prend la colonne « défaut ». Sans ce mot au 2026-11-15, aucun défaut ne s'applique et la grille n'est pas
scellable (nœud).

| n° | objet | défaut (si D-G0-1 accepté) | autre option | source du défaut |
|---|---|---|---|---|
| D-G0-1 | première lecture au plus tard le 2026-11-30 23:59 UTC, unique pour cette échéance ; anticipable une seule fois sur mot de Lazar seul ; grille scellée ≤ 2026-11-15 avec D-G0-1 à 13 tranchés ou échus ; règle des défauts ci-dessus | **aucun : mot explicite exigé** | — | CL1 § 6 |
| D-G0-2 | critère 2 délégué au préenregistrement de T0.6 sous conditions (a)-(d) | délégation sous (a)-(d) | définition fixée dans la grille | commune aux deux avis |
| D-G0-3 | « tourne » = sans arrêt de garde + part de scores finis fixée d'avance par T0.8, mêmes deux grains, avant toute lecture ; « tourne » ≠ « détecte » | cette définition | — | commune |
| D-G0-4 | critères 6 et 7 : contrôle de présence des décisions renvoyées, attesté par le contre-lecteur R2 ; listes N-007/N-008, N-034, N-054, N-055, N-056, N-060 v3, R-746 (G1) ; N-005/N-006, N-013, N-023, R-307, R-309 (C) | **réserve** | condition (non tenu — invalide) | commune |
| D-G0-5 | critère 1 hors domaine sans garde en ligne ; garde de P-007 exigée dans T0.6 à T0.8 | **réserve** + exigence amont | non tenu — invalide du critère concerné | commune |
| D-G0-6 | lecteur d'un modèle différent des auteurs des preuves, même famille ; lignée différente de celle de la grille | oui, déclaré, à défaut signalé | — | commune |
| D-G0-7 | version suivante recevable seulement si autorisée avant son run avec une cause nommée distincte du résultat ; sinon non concluant ; aucune après un négatif par liste d'arrêt (R-765) | cette règle | — | commune |
| D-G0-8 | verdict scellé par sous-agent neuf exigé pour 2, 3, 4 (rapport de fonctionnement suffisant pour 4) ; absence = non tenu — absent | cette règle | — | commune |
| D-G0-9 | critère 8 : périmètre (A) en condition, chiffres externes ; internes sous R6 en réserve ; (B) au script en réserve ; périmètre gelé en annexe E | **(A)**, (B) en réserve | (B) ou (C) en condition | commune sur (A) ; (B) en réserve : avis Fable grille |
| D-G0-10 | critère 5 : « validés » = toutes les prédictions « confirmée », aucune « réfutée », audit R4 « déclenché : False » ou scellé | **option Fable** | ligne de synthèse de la lecture | avis Fable grille et CL1 § 6 (confiance élevée) |
| D-G0-11 | critère 3 : P4-instrument absent ou postérieur | **réserve** | condition (non tenu — invalide ; avis Fable grille) | CL1 § 6 (confiance moyenne) ; **les deux sources divergent** |
| D-G0-12 | critère 4 : TRACE-lite absent | **réserve** | non tenu — absent (lecture littérale du brief T0.8) | avis Fable grille et CL1 § 6 (confiance élevée) |
| D-G0-13 | **nouveau (v3)** : raccord de R-765 à la grille. (a) « échec scellé » = sous-état « non tenu — négatif » (résultat d'une lecture gelée, liste d'arrêt ou ligne de table) d'une pièce scellée après le verdict de la première lecture ; « absent », « invalide », « non concluant » ne gèlent pas ; (b) un critère « non tenu — négatif » au verdict de la première lecture est gelé de même (statut reporté tel quel) ; (c) un critère gelé est lu à la seconde lecture sur la pièce qui l'a gelé ; toute pièce postérieure sur ce critère est non recevable et rapportée en réserve | **(a), (b), (c)** | pour (b) : D-G0-7 s'applique au premier négatif par ligne de table (version suivante recevable si cause nommée), seul le négatif par liste d'arrêt restant gelé | recommandation de la v3 seule (confiance moyenne), à contre-lire en CL2 ; motif : R-765 et CL1 § 5 (1) |

**Existantes, reprises sans changement** : critère 1, table de `prereg/T0.4-validation-modele-reel-v3.md` ; critère 3, seuil
« borne basse strictement au-dessus du quantile 0,95 du plancher » (P3 l. 272 ; P-011 l. 40), correction pour le nombre de
sondes (P3 l. 274-275), recette du plancher (P3 l. 228-230), bras principal générique (P-011 (c)), agrégation max ou
attention (brief T0.7, N-026) ; critère 4, contenu de la base (N-029 § 1, P-015 l. 50-52) et même jeu d'épisodes (N-029 § 2) ;
critère 7, contenu du livrable (brief T0.9, N-005/N-006 l. 97) ; critère 8, statuts « confirmé, corrigé, introuvable »
(brief T0.2), règle d'usage (synthèse du niveau 2, § 2), contrôle de traçabilité avant G0 (§ 4) ; repli : report unique au
31 janvier 2027 (R-750), gel sur échec scellé et jamais de nouvel essai après une liste d'arrêt (R-765).

## Annexe C — ce qu'il reste à produire avant le scellement et avant la lecture (sans état)

1. Mot explicite de Lazar sur D-G0-1 ; décisions D-G0-2 à D-G0-13 (ou défaut échu) ; contre-lecture R2 de cette v3 ;
   scellement de `prereg/G0-grille-lecture-vN.md` au plus tard le 2026-11-15 ; M-0.2 sur la grille ; annexe F retirée.
2. Pour chaque lecture, `docs/verdicts/dossier-G0-vN.md` (pièces remises, pointeurs R4, pièces écartées avec motif de la
   liste fermée de M-0.8), scellé ; périmètre du critère 8 recopié en annexe E au commit de scellement de la grille.
3. Script du critère 8, essais sain et artefact (R5), scellés.
4. Clause de repli : les onze choix restants, insérés dans la version scellée (N-027 bis) ; R-750 porté dans
   `docs/decisions/`.
5. Procédure d'ouverture : gabarit de `registres/g0-lecture-ouverte-vN.md` ; clone complet et locale `C.UTF-8` pour le
   lecteur.
6. **Formes exigées des pièces à venir**, pour que les commandes de la grille les lisent sans jugement : préenregistrements
   de T0.6 à T0.8 qui nomment le critère par son numéro seul (« critère 2 de G0 », « critères 2 et 3 de G0 », jamais un
   intervalle « 1 à 3 ») ; familles écrites « (i) », « (ii) » ou « (i-a) » ; « vérité terrain », « proportion » et
   « intensité » dans la section « Métrique » de T0.6 ; « covariance », « même agrégation », « mêmes actions » dans la
   section « Métrique » de T0.7 ; une ligne « Bras principal : … » dans T0.7 ; part de scores finis et format JSON Lines
   dans T0.8 ; garde d'équivalence hors domaine (P-007) dans T0.6 à T0.8 ; verdicts qui portent une ligne de neutralité
   dans leurs cinq premières lignes et un prononcé de la forme « Critère k de G0 : … ».

## Annexe D — réserves de rédaction

- Je n'ai pas relu en entier la v1, l'avis Fable grille (lu : l. 10 et 54), ni l'avis conv-audit n° 199 : je les cite
  d'après la v2 et CL1, qui les ont recalculés et appliqués point par point (CL1 § 2, aucun refus).
- La clause de repli de conv-audit (`62cc6fbf…`) n'a pas été lue par moi.
- Les brouillons de T0.6 à T0.8, de G1 et du papier C ne sont pas lus au-delà de ce que l'annexe F en essaie (le brouillon 5
  du papier C, par `grep "HC2"` seulement).
- `registres/decisions.md` est vivant : il a bougé pendant la rédaction (`fc8884ce…` à 11:08 UTC, `34f45866…` à 11:16 UTC) ;
  les lignes citées (34, 462, 978, 989, 993, 994) sont restées en place, vérifiées à la seconde empreinte.
- En lisant les en-têtes des verdicts P3 v1 et v2 pour essayer le motif de neutralité, j'en ai vu la ligne d'issue ; rien
  de cette lecture n'entre dans la partie gelée (la seule phrase d'état de la v2, l. 313, est retirée).
- D-G0-13 est une proposition de cette v3 seule ; aucun avis ne l'a examinée.
- Les motifs restent des motifs : celui de neutralité attrape aussi une phrase qui nierait la neutralité (essai synthétique
  de l'annexe F) ; c'est pourquoi la ligne trouvée est recopiée dans le verdict.

## Annexe E — périmètre du critère 8 (gelé avec la grille ; rempli au commit de scellement)

Selon l'option retenue en D-G0-9 (défaut : (A)), la version scellée recopie ici, au commit de son scellement :
1. les documents qui font foi, par chemin et empreinte (`docs/sha256sums-lancement-v2.txt`) ;
2. la liste rendue par `find docs/decisions -maxdepth 1 -type f -name '*.md' | sort`, chaque fichier avec son empreinte ;
3. pour les préenregistrements des critères 6 et 7, qui peuvent être scellés après la grille : la **règle de nom**
   `prereg/G1-*-vN.md` et `prereg/papier-C-*-vN.md`, version qui fait foi au sens de la section 2.
Un document du programme créé après le scellement de la grille et hors de la règle 3 n'entre pas au périmètre : il est
passé au script en réserve. Pour (B) ou (C), la liste s'étend de même, par commande `find` recopiée et sortie figée.

## Annexe F — essais des motifs sur le dépôt du 29 octobre [NON GELÉE ; retirée de la version scellée]

Exécutés au commit `9d99f29d` (clone superficiel), sous `LC_ALL=C.UTF-8` sauf mention, le 2026-10-29 entre 11:07 et 11:16
UTC. Ce ne sont pas des lectures de G0 : aucun dossier n'existe et des versions qui ne font pas foi sont essayées exprès.
Objet : montrer que chaque motif corrigé trouve les pièces existantes et n'attrape pas de faux.

**Locale (n° 19).** `locale` rend `LC_CTYPE="POSIX"` ; `locale -a | grep -i -c -E "^c\.utf-?8$"` rend 1 (la locale exigée existe). Sur `prereg/P3-premier-test-i-a-v1.md` : `grep -c -i -E "crit[èe]res? 2"`
rend **0** en POSIX et 4 sous `LC_ALL=C.UTF-8` ; `grep -c -i -E "crit(è|e)res? 2"` rend 4 dans les deux ; le motif de CL1
`grep -c -i "crit[èe]res\? 2\b"` rend 0 en POSIX.

**M-0.8, inventaire (CLG-01).** Le script rend **23** pièces scellées : `docs/etat-de-l-art/` niveaux 1 et 2 ;
`docs/verdicts/` : `audit-R4-T0.5-pilote-notations-v1`, `audit-R4-T0.5-pilote-v1`, `verdict-P3-premier-test-i-a-v1` et `-v2`,
`verdict-T0.4-critere-1-G0-v1` à `-v3`, `verdict-T0.5-pilote-notations-v1`, `verdict-T0.5-pilote-v1`,
`verdict-T0.5-revalidation-v2` ; `prereg/` : `P3-addendum-lecture-complementaire-v1`, `P3-addendum2-audit-verdict-v1`,
`P3-premier-test-i-a-v1`, `T0.3-simulation-lemme-theoreme-v1`, `T0.4-validation-modele-reel-v1` à `-v3`,
`T0.5-pilote-8B-v1`, `T0.5-pilote-notations-v1`, `T0.5-revalidation-equivalence-pilote-v1` et `-v2`. Aucun faux : les
préenregistrements et verdicts sans lien avec G0 (`gradient-etape1-sondes-*`, `test-echelle-conscience-eval-*`,
`test-hm1-gabarit-style-*`, `verdict-lecture-echelle-conscience-eval-v10`, `gabarit-preregistrement-v1`,
`porte-GC-loi-de-deference-v1`) ne sont pas pris. Les préfixes de CL1 seuls (T0.4, T0.3, …) en prenaient 10 de ces 23 :
P3 (4 pièces, qui nomment les « critères 2 et 3 de G0 ») et T0.5 (7 pièces, qui nomment le « critère 2 de G0 ») manquaient.
Volet runs : 14 manifestes rattachés (T0.3 : 1 ; T0.4 : 4 ; T0.5 : 5 ; P3 : 4, dont 2 non décisifs pour les addenda).
`P3-consignes-v1.md` n'est jamais ouvert (exclu par `find` avant lecture).

**F-1.1 (CLG-04).** Motif `PRONONCE_1` sur `docs/verdicts/verdict-T0.4-critere-1-G0-vN.md` : v1 l. 3 → un seul mot,
« non concluant » ; v2 l. 10 → un seul mot, « non prouvé » ; v3 l. 11 → un seul mot, « prouvé ». Les trois issues sont
attrapées, une par version. L'ancien motif `Critère 1 de G0 : prouvé` rend 0 sur v1 et sur v2 (il aurait rendu « absent »
au lieu de « non concluant » et « négatif »).

**M-2.2, F-2.1, F-3.2 (CLG-03).** `CRIT_2` rend P3 l. 17, 57, 122, 431 (l'ancien motif : l. 122 seulement ; la l. 431, citée
comme modèle, est désormais trouvée) ; `T0.5-pilote-8B-v1` l. 152, 174, 183 ; rien sur T0.4 v3 ni sur T0.3. Essai
synthétique : « critère 20 de G0 » et « critères 12 et 13 » non pris ; « critère 2 de G0 », « critères 1, 2 et 3 »,
« Critères 2 et 3 de G0 » pris. Limite : un intervalle « critères 1 à 3 » n'est pas pris (d'où l'annexe C, point 6).
Familles : `FAM_I` prend « (i) », « (i-a) », « (i) et (ii) », pas « (ii) », « (iii) » ; `FAM_II` prend « (ii) », « (ii-b) »,
« (i) et (ii) », pas « (i) », « (iii) ». Sur P3 : `FAM_I` 5 lignes, `FAM_II` 1 ; l'ancien `grep "(i)"` : 0.

**M-0.3, M-0.5 (CLG-07).** `head -5 | grep -c -i -E "NEUTRE"` rend 1 sur chacune des huit pièces attendues :
`T0.4-v3-rapport-contre-lecture-1-v1`, `-2-v1`, `T0.3-rapport-contre-lecture-1-v1` à `-3-v1`, CL1,
`verdict-T0.4-critere-1-G0-v3`, `verdict-T0.5-pilote-v1`. L'ancien `n'ai pas écrit` : 0 sur sept d'entre elles ; `neuf`
seul : jusqu'à 12 lignes par fichier. Témoins à 0 : brief v2, programme v2, préenregistrements T0.3 et T0.4 v3, synthèse
du niveau 2. « auteur ni » nu prenait `verdict-P3-premier-test-i-a-v2.md` l. 608 (« ni par l'auteur ni par le
correcteur ») : faux, écarté par le motif resserré. Les verdicts P3 v1 et v2 ne portent aucune ligne de neutralité dans
leurs cinq premières lignes : remis comme preuves, ils échoueraient M-0.5 (information pour le dossier, pas une lecture).
Essai synthétique : « Il n'a pas été écrit par un sous-agent neuf » est pris (limite dite en annexe D).

**M-0.3, « scellable » (n° 20).** `grep -o -m1` rend « Scellable après corrections » en première occurrence sur les six
rapports essayés ; CL1 contient aussi « non scellable » (l. 52) et « scellable » plus bas, non pris par `-m1`.

**F-5.1, F-5.2, M-5.2 (CLG-08, CLG-09).** La commande F-5.1 s'exécute sur `diag/20261004-080257-t03/lecture.json` (une
seule clé de verdict) ; `grep -n "déclenché : False"` rend `lecture.md` l. 39 ; M-5.2 rend `7474743a`, `d73ac469…`, `True`,
`5609f920` ; M-0.1 OK sur `lecture.md` et `lecture.json`.

**R4, pointeurs (n° 21).** Motif de négation sur quatre lignes : `verdict-T0.4-critere-1-G0-v3.md` l. 11 (« P9 n'est pas
déclenché ») → non déclenché ; `lecture.md` de T0.3 l. 39 (« déclenché : False ») → non déclenché ;
`verdict-T0.5-pilote-v1.md` l. 57 (« Audit R4, déclenché par … ») → déclenché (un rapport `audit-R4-T0.5-pilote-v1.md`
existe) ; même fichier l. 117 (« Déclencheur « trop propre » : aucun ») → non déclenché. Le verdict de T0.4 v3 n'a aucune
ligne qui contienne à la fois « R4 » ou « symétrie » et « déclench » : un motif générique ne le lirait pas, d'où les
pointeurs du dossier.

**F-1.2, M-3.4, F-2.2 (CLG-10).** F-1.2 sur le verdict T0.4 v3 : section « 1. Verdict », `[True, True, True]`. M-3.4 sur P3 :
« covariance » l. 129 et 228, « même agrégation » l. 229 et 244, « mêmes actions » l. 230 et 240, tous dans la section
« Métrique » (l. 163-269). F-2.2 : « vérité terrain » absent de la section « Métrique » de P3 et de T0.5 pilote : la
condition porte sur T0.6 (annexe C, point 6). F-8.2 : `grep -c "l'article imprime"` rend 1 sur la synthèse du niveau 2.

**Échappement (n° 19).** `printf 'a|b\nb\nx\n' | grep -c -E "x\|b"` rend 0 (barre littérale) ; sans `-E`, `grep -c "x\|b"`
rend 3 (alternance GNU) ; `grep -o -E "(non prouvé\|prouvé)$"` ne prend pas « non prouvé ». D'où la convention de la section 0.

**F-7.1 (CLG-11).** Sur `brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md` : `HC2` 19 lignes, `HC2\b` 16,
`HC2b` 10 ; aucune ligne qui ne porte que « HC2b » n'est prise par `HC2\b`. Essai : « HC2 et HC2b », « HC2, », « HC2. »
pris ; « HC2b seul », « HC20 » non pris.

**M-4.3 (CLG-08).** Script essayé sur trois fichiers synthétiques du dossier de travail (un score `NaN`, un score `null`,
un épisode sans statistique) : comptes par base corrects, scores non finis non comptés, épisode manquant compté.

Fin de rédaction : voir la ligne suivante (heure lue par `date -u`).
Fin de rédaction : 2026-10-29 11:24:45 UTC.
