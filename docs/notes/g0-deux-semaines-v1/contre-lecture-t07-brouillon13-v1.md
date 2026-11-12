# Contre-lecture (R2) du brouillon 13 du préenregistrement de T0.7 — v1

- Écrite le 2026-11-08 (après 19:30 UTC) par un contre-lecteur neuf (Claude Fable 5.1, `claude-fable-5-1`, sous-agent de la
  session mère), qui n'a écrit aucun des brouillons 1 à 13, aucune des contre-lectures cl1 à cl4 ni celle du brouillon 12, ni le
  module `src/controle_ia/t07/`. Modèle autre qu'Opus 5.5 (N-052 : les passages neufs du brouillon 13 sont d'Opus 5.5).
- Objet : `brouillons/T0.7-sondes-v0-v1-brouillon13.md`, empreinte **vérifiée** par `sha256sum` :
  `bc698a03ebd7c6572f80b8e852213778b385ec45b5e32b47be8836496cdf0e91` (2 074 lignes) ; contre le brouillon 12
  `brouillons/T0.7-sondes-v0-v1-brouillon12.md`, `718e8955307e5a2bdf64765f8ebde83ae72d19b65b2c67748f2821e534fad892` (vérifiée).
- Méthode : `diff` entre les deux brouillons (525 lignes, lues en entier) ; lecture en profondeur des passages changés et de
  ceux qui en dépendent (table « du 12 au 13 », l. 22-36 ; Décisions l. 443-448 ; Règle « mots et coût » l. 550-584 ; Plan,
  étape B l. 910-965 ; Critères, entrées et table des lignes l. 1005-1100 ; Liste d'arrêt l. 1106-1150 ; Lignes de registre
  l. 1261-1343 ; Module l. 1352-1600 ; Concordance l. 1645-1668 ; Reste l. 1840-1860 ; table des constats l. 2027-2042 ;
  Marqueurs l. 2043-2074). Lus aussi : la contre-lecture du brouillon 12 (`71bf18cd…`), la ligne R-1924 de
  `registres/decisions.md`, le script `grille_l_t07_brouillon13.py` (`2677518b…`, vérifiée) et sa sortie, le `diff` des scripts
  12 et 13, et dans le module : `lecture_v1.py` (`ouvrir` l. 213-259, `lire_issue_p3bis`, `lire_table_A`, `lire_fuites`,
  `etape_b` l. 628-718, `main` l. 750-803), `registre_v1.py` (`lire_registre_t07` l. 111-151, `verifier_lignes`,
  `exiger_anteriorite`, `garde_ouverture`, `journaliser_ouverture` l. 194-206), `manifeste.py` (`ecrire_resultat` l. 128-139),
  `sondes/evaluation.py` (`aire_sous_courbe` l. 26-38), `premier_test_ia/statistiques.py` (`separation` l. 128-130,
  `aire_simple` l. 133-140). Pour la décision (4) et la question 4, j'ai extrait de l'historique git, sans rien modifier :
  `scripts/controle_lecture_t06_v1.py` (branche `origin/prep/t06-candidat8-v1`, commit `1ae198b4`, empreinte
  `ba2ba5cfe7484e7e30bb74e44420b46c9939dd5613bbb961b9725c3d46343c07`, égale à celle que cite le brouillon 13 l. 1269 et le
  candidat 12 r2 de T0.6 l. 334) et `brouillons/T0.6-organismes-v0-v1-candidat12-r2.md` (branche `origin/prep/t06-ordre-course-v2`,
  commit `8cb539f9`, 817 lignes), copiés dans mon répertoire de travail temporaire.
- Interdits respectés : aucun fichier de `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`
  lu ; aucune variable d'environnement ni clé lue ; suite complète des essais non lancée ; aucun commit ; aucun autre fichier
  modifié (seul ce rapport est créé).

## Verdict

**Scellable après corrections.** Aucun constat bloquant : le refus avant écriture (B-1 (b)) est bien spécifié et sa relance est
compatible avec R12 ; la grille est rejouée à l'identique ; les quatre décisions de R-1924 sont justes et je dis où les écrire.
Trois constats majeurs : (M-A) la garde d'ouverture de l'étape B ne liste pas « `lecture-t07.json` déjà écrit » parmi ses refus,
alors que le texte promet un refus et que le module, tel qu'il est, ouvrirait les scores puis écrirait `arret-etape-b.json` ;
(M-B) la définition gelée de la fuite fixe le seuil (0,70) et la fonction (`separation`) mais pas **la valeur par action** du
trait dont on prend l'aire, donc la séparation n'est pas calculable sans un choix de l'auditeur ; (M-C) le texte attribue au
script de T0.6 `controle_lecture_t06_v1.py` un refus « clé ni exigée ni permise » qu'il n'a pas (il **ignore** toute clé autre
que ses deux), et conditionne m-07 et la demande (4) de la Concordance à cette hypothèse déjà tranchée. Neuf constats mineurs.

Compte : **0 bloquant, 3 majeurs, 9 mineurs.**

## Réponses aux cinq questions

### (a) Le refus code 2 avant toute écriture est-il sans effet de bord ? La relance sur le même run respecte-t-elle R12 ?

- **La règle écrite est sans effet de bord**, dans toutes les branches que le texte nomme : lignes exigées absentes, en
  double, mal formées, postérieures, sceau faux (l. 910-922, 1110-1116, 1317-1327) ; `lecture-cout-t06.json` absent ou sans
  table A (l. 914, 1325-1327, 1376-1377) ; fichier d'audit illisible ou `consigne` différente de la ligne (l. 1027-1028,
  1343) ; clé du registre refusée par la règle M-2 (l. 1119-1121). Dans chacune, « rien d'écrit » ne laisse que la ligne du
  journal `<registre>.ouvertures.md` (l. 1543-1546), qui n'est pas un résultat rattaché au manifeste. Le module confirme la
  faisabilité : à l'étape B, aucun manifeste neuf n'est créé (`etape_b` l. 636-637 lit celui de l'étape A), et toute
  `GardeArret` levée **avant** le bloc `try` de la l. 644 remonte à `main` comme refus code 2 sans écriture (l. 801-803). Pour
  que la règle tienne, le module devra déplacer dans `ouvrir` (avant la l. 644) les contrôles qui sont aujourd'hui dans le
  `try` : table A (`lire_table_A`), fichier d'issue de P3-bis (`lire_issue_p3bis` quand une ligne manque), fichier d'audit
  (`lire_fuites`) ; le texte le déclare (« défait le marqueur 1 du module ») mais pas pour la table A ni le fichier d'audit
  (constat m-04).
- **Une branche manque dans la garde écrite (M-A)** : « `diag/<run-t07>/lecture-t07.json` déjà présent ». Le texte dit « une
  tentative après lui → refus » (l. 1551, l. 1498) et le script modélise ce refus dans la garde (`garde_etape_b`, `lecture_deja_ecrite`),
  mais aucune des trois listes de la garde (l. 910-922, 1110-1116, 1317-1327) ne le porte. Sans cette ligne, le module tel
  qu'il est ouvrirait les scores (journal « OUVERTURE »), lirait, puis échouerait à `ecrire_resultat` (`manifeste.py` l. 134-135)
  → `GardeArret` → `arret-etape-b.json` **écrit et scellé**, code 3 : un fichier d'arrêt rattaché au manifeste d'un run qui porte
  une lecture valide. Même question pour `arret-etape-b.json` déjà présent (après un code 3) : le texte ne dit pas si l'étape
  B se relance (le module écrirait alors `lecture-t07.json` au succès, mais un second échec ferait échouer l'écriture du second
  `arret-etape-b.json` dans le gestionnaire d'exception, et `main` rendrait code 2 « REFUS » pour un arrêt).
- **Le journal** : le module journalise une ligne `OUVERTURE-T07` à la fin de `ouvrir` (l. 258), **avant** les contrôles des
  fichiers ; sous la règle du brouillon 13, un refus pour table A absente suivrait une ligne « ouverture ». Le texte doit fixer
  la forme de la ligne de refus et son ordre (constat m-01). Le même journal est partagé avec le script de T0.6, qui y écrit
  `OUVERTURE-SONDES-T06` (script l. 101) : des lignes `OUVERTURE-T07` et des lignes de refus distinctes s'y lisent sans
  confusion.
- **R12 et la relance** : compatible. Rien n'est versionné ni écrasé : le manifeste de l'étape A n'est pas touché ; le
  registre et le journal ne reçoivent que des lignes ajoutées ; `lecture-t07.json` est écrit une fois (l. 1548-1551) et
  `ecrire_resultat` refuse d'écraser. L'énumération (0) du script le vérifie pour les 511 cas (sortie identique, question e).
  Une seule réserve, portée par M-A : la « troisième tentative refusée » doit être un refus **de la garde**, sinon elle n'est
  pas sans effet de bord.

### (b) La définition gelée de la fuite est-elle opérante ? La séparation est-elle calculable par l'audit sans score de T0.7 ?

- **Ce qui est opérant** : la fuite est restreinte à une différence **de construction** (chaîne de T0.6), portée **dans les
  jetons notés**, à quatre traits nommés, avec un seuil (≥ 0,70) et une fonction (`statistiques.separation`, max(a, 1 − a),
  existante l. 128-130) ; ce qui ne compte pas est écrit (prédicteurs triviaux → N, comportement, consigne hors des jetons,
  trait sous 0,70) ; le domaine du fichier est fermé (`fuite`, `trait`, `separation`, `motif`) et vérifié par le module ;
  l'auditeur ne lit que les textes et mesures de T0.6, qui existent dès `RUN-CONFIRMATION-T06`, jamais un score de T0.7 : la
  séparation est **indépendante de T0.7** par construction. C'est un vrai progrès sur le brouillon 12.
- **Ce qui manque pour que le nombre soit calculable sans choix de l'auditeur (M-B)** : `separation` prend une **aire**, et
  une aire suppose une **valeur par action** et une étiquette. Le texte ne dit pas quelle valeur porte chaque trait. Pour
  `extrait` on devine un indicateur 0/1 (« nombre d'actions où il figure par condition ») ; pour `empan` (« premier ou dernier
  jeton noté »), `format_cout`, `gabarit`, rien n'est dit : un auditeur peut prendre un indicateur, un compte d'occurrences, une
  longueur, et obtenir des séparations différentes sur les mêmes textes. Il manque aussi le périmètre (« sur les actions du
  jeu » : toutes les actions notées des deux conditions, lisibles et illisibles ?). Correction : fixer **la valeur par action =
  indicateur 0/1 du trait tel que cité** (l'extrait est présent dans les jetons notés ; le jeton d'empan est celui cité ; la
  forme du champ `COST` est celle citée ; l'élément de gabarit est présent), l'aire par `statistiques.aire_simple(valeurs,
  condition, positifs = condition du jeu, negatifs = "honnete")` sur **toutes les actions notées des deux conditions**
  (`mesures-t06.npz`), puis `separation` de cette aire. Avec un indicateur, l'aire vaut 0,5 + (p₁ − p₀)/2 : « ≥ 0,70 » revient
  à « le trait est présent dans au moins 40 points de pourcentage d'actions de plus (ou de moins) dans une condition que dans
  l'autre », ce qui rend la règle lisible et recalculable par le contre-lecteur du fichier d'audit.
- **Surdéclaration à corriger** (m-03) : « les champs `trait` et `separation` […] rendent la règle de séparation vérifiable
  par le module » (l. 2039-2040) : le module vérifie le **domaine** ([0,70 ; 1]), pas le calcul ; la vérification du calcul
  relève de la consigne scellée et de la contre-lecture du fichier.

### (c) La tolérance 5 × 10⁻⁴ sur `aire` est-elle justifiée ?

- **Oui sur le fond** : si T0.6 écrit `aire` arrondie à trois décimales, l'écart au nombre exact est au plus une demi-unité de
  la troisième décimale, et un recalcul sur les mêmes scores par `aire_sous_courbe` (ex aequo pour moitié, l. 26-38, même
  recette que la Règle l. 540) n'a pas d'autre source d'écart. La branche « égalité » est bien distinguée, le nœud « ni
  définition ni scores stockés » est écrit (l. 1341, 1645-1650), le choix est porté par un marqueur et par la configuration.
  Le candidat 12 r2 de T0.6 (l. 536-548) ne définit **aucun fichier ni champ `aire`** : le choix se fera au candidat 12 r3 ou
  suivant, comme le texte le prévoit.
- **Deux réserves mineures** (m-02) : (i) la comparaison est stricte à la frontière (« > 5 × 10⁻⁴ ») et se fait en flottants :
  pour une aire exacte 0,7345 écrite 0,735, l'écart binaire peut valoir 5,000…06 × 10⁻⁴ et déclencher L7c sur un artefact ;
  écrire la tolérance avec une marge (« > 5 × 10⁻⁴ + 10⁻⁹ ») ou, plus simple, comparer **l'aire recalculée arrondie au nombre de
  décimales du nombre écrit** à ce nombre ; (ii) les essais R5 (l. 1509-1511) testent 4 × 10⁻⁴ et 6 × 10⁻⁴, pas la frontière ;
  ajouter l'essai « écart exactement 5 × 10⁻⁴ → pas L7c ». La justification « choix de ce rédacteur » est déclarée, ce qui
  suffit à R1 : le seuil ne peut pas favoriser un signe.

### (d) Reste-t-il une contradiction interne ?

- **Aucune contradiction entre règles** sur les points changés : refus / L0a / L1 cohérents entre le Plan (l. 910-922), les
  Entrées (l. 1005-1015), la table (l. 1068-1072), la Liste d'arrêt (l. 1110-1118), les Clés par étape (l. 1317-1329), le
  Module (l. 1543-1559, 1561-1564) et le script ; F et son fichier cohérents entre 4 ter (l. 937-942), la ligne de registre
  (l. 1343), R7 / R9 (l. 1090, 1094), la Liste d'arrêt (l. 1143-1145) ; `aire` cohérent entre la Règle (l. 568-573), la
  ligne (l. 1341), le Module (l. 1437-1439), la Concordance (l. 1645-1650), le marqueur (l. 2073) ; règle M-2 cohérente entre
  Lignes (l. 1288-1310), Liste d'arrêt (l. 1119-1121), essais (l. 1504-1508), Concordance (l. 1658-1668), marqueur (l. 2072).
- **Trois incohérences de fait ou de forme**, classées : (M-C) ce que le texte dit du script de T0.6 est faux (voir
  question 4 de la contre-lecture du brouillon 12, qui ne pouvait pas vérifier ; je l'ai fait) ; (m-05) l. 1542 dit
  « `diag/<run-t07>/arret.json` sur toute `GardeArret` après le manifeste » alors qu'à l'étape B le fichier est
  `arret-etape-b.json` (l. 916, 1068, 1115, 1544 ; module l. 716) ; (m-07) l. 1999 (table historique de cl4) garde « Q =
  absente », valeur qui n'existe plus.
- **Une règle écrite plus large que le module et que le registre ne le supporteraient** (m-06) : « (1) cellule de clé mal
  formée → refus » (l. 1295-1296) refuserait une ligne d'en-tête ou de séparation de table Markdown si quelqu'un en
  ajoutait une au registre ; le module (l. 128) ne refuse que si la ligne a quatre cellules et une date au format ; le script
  de T0.6 ignore tout. Préciser.

### (e) Script rejoué

`cd /tmp && python3 -I -B /home/user/controle-ia-travail/brouillons/T0.7-sondes-v0-v1-brouillon13-pieces/grille_l_t07_brouillon13.py`
→ **code 0**, 17 s, sortie **identique octet pour octet** à `grille-l-t07-brouillon13.txt`, empreinte
`f9d8e0239a4e9a73080eb67f5d239573005d236d0fd3a5996e4d7e155196ba4a` (égale à celle du texte, l. 1033). Énumération (0) :
512 cas, 0 défaut, 511 relances, 0 défaut, 0 valeur « absente » restée ; (1) 624 ; (2) 55 296 ; (3) 18 439 488 sur
1 041 984, 7 776 impossibles ; tout à 0. `diff` des scripts 12 et 13 : seuls changent la docstring, les trois tuples P, A, Q
(renommage), `ENTREES_B`, `garde_etape_b`, `verifier_garde_b`, l'impression de (0) et la condition finale ; `regles`,
`deriver`, `agreger_doses`, `grille_classes` et les contrôles du brouillon 12 sont inchangés : les effectifs de (1) à (3) sont
bien ceux du brouillon 12. Portée de (0), telle que déclarée (l. 1038-1039) : modèle de la règle de présence des neuf entrées
et de la règle R12 ; il ne modélise ni le fichier d'audit illisible, ni la consigne différente, ni la règle M-2 (m-08).

## Avis sur les quatre décisions de R-1924 (restes du rédacteur, pas encore écrites)

### (1) Règle « marque retirée » restreinte aux clés dont la forme sans marque égale une clé dont la présence fixe une lecture

**Juste.** La menace que la règle (3) doit arrêter est la seule qui survive à la règle (4) : une clé de T0.7 **permise dont la
présence change la lecture** tapée avec la marque d'une **autre** tâche de la liste (`SCELLEMENT-JEUX-T08-JD` pour
`SCELLEMENT-JEUX-T07-JD`) tomberait en « ignorée » et déclencherait le repli des jeux sans refus. Pour une clé **exigée**, la
même faute donne « ligne manquante → refus » ; pour une clé permise sans effet sur la lecture (`SCELLEMENT-T07`, `GO-*`,
`CODE-T07` quand DS-3 bis n'est pas accordée), elle est sans effet. La seule famille concernée est donc `SCELLEMENT-JEUX-T07-JD`,
`-JC`, `-JA` (`sondes_lues`, repli des jeux, l. 1266, 1312). La règle actuelle, elle, refuserait `SCELLEMENT-T06`, `SCORES-T08`,
`SCELLEMENT-T08` : j'ai vérifié que le candidat 12 r2 de T0.6 n'écrit **aucune** clé de registre (il ne cite que
`SCELLEMENT-T07` et `SCELLEMENT-P3BIS`, lues par son script, l. 334), donc rien ne casse aujourd'hui ; mais T0.8 n'est pas écrit, et la
règle large mettrait T0.7 à la merci d'un nom choisi ailleurs. Restreindre est le bon sens.

**Comment l'écrire** (liste explicite, jamais « et analogues » dans le texte scellé) :
- l. 1298-1301 (règle (3)) : « **sauf si son nom, marque retirée, égale `SCELLEMENT-JEUX-JD`, `SCELLEMENT-JEUX-JC` ou
  `SCELLEMENT-JEUX-JA`** (forme sans marque des seules clés de T0.7 dont la présence fixe une lecture : `sondes_lues` et repli
  des jeux) → refus » ; retirer la « conséquence déclarée » (l. 1303-1306 : `SCELLEMENT-T08`, `SCORES-T08`, `SCELLEMENT-T06`…
  ne font plus refuser) et la remplacer par « une clé d'une autre tâche bâtie sur le patron `SCELLEMENT-JEUX-<marque>-*` fait
  refuser ; la Concordance demande à T0.8 de ne pas l'employer » ;
- l. 1119-1121 (Liste d'arrêt) : même restriction ;
- l. 1504-1508 (essais R5) : garder l'artefact `SCELLEMENT-JEUX-T08-JD` → refus ; **ajouter les cas sains** `SCELLEMENT-T08`,
  `SCORES-T08`, `SCELLEMENT-T06` → ignorées et comptées ;
- l. 1658-1661 (Concordance (2)) : « aucune de leurs clés n'a la forme `SCELLEMENT-JEUX-<marque>-JD|JC|JA` » à la place de
  « marque retirée, n'égale une clé de T0.7 » ;
- l. 1310 et l. 2072 (marqueur) : « ni ne tombe sous la règle (3) restreinte » ; l. 28 (table « du 12 au 13 », ligne 3) et
  l. 2033 (table des constats, M-2) : une phrase « règle (3) restreinte au brouillon 14 (R-1924 (1)) ».

### (2) L1 par fichier « mots et coût » illisible, L7b, L7c = issues finales sous ce texte ; correction par version neuve

**Juste**, et c'est la seule lecture compatible avec R12 et avec le registre « jamais réécrit » : une ligne
`ISSUE-MOTS-ET-COUT-T06` corrigée serait en double (refus), `lecture-t07.json` est écrit et ne peut l'être deux fois. Le reste
déclaré (l. 1554-1559) se ferme ainsi sans inventer de clé ni de fichier « -R1 » dans ce texte.

**Deux précautions à écrire avec la décision** :
- la version neuve **ne relit pas** ce que `lecture-t07.json` porte déjà (sous L7b et L7c : T7-P1 et les lectures sur (i-a),
  `temoin`, `mention`, `T100` sont faites et scellées) ; elle lit (ii) seule, sur les mêmes scores scellés, sous une clé
  d'issue et un fichier de résultat neufs qu'elle nomme (sinon une double lecture de (i) devient possible) ;
- sa ligne de registre **ne peut pas** s'appeler `SCELLEMENT-T07` : le script de T0.6 exige **exactement une** ligne de cette
  clé (`lire_registre`, l. 70-72 du script `ba2ba5cf…`) ; une seconde ferait refuser la lecture de T0.6. La version neuve
  prendra une clé à part (`SCELLEMENT-T07-V2` par exemple), que son propre module exigera ; le dire ici évite de le découvrir
  au nœud (constat m-09).

**Lignes à changer** : l. 1072 (L1, colonne lecture) : remplacer « la lecture attend une table A et une issue […] lisibles (ou
la relance de T0.6 sous son texte) […] (suite après correction d'un fichier illisible : section « Module », « Relance ») » par
« **issue finale sous ce texte** : la ligne L1 et son motif sont écrits dans `lecture-t07.json` ; toute lecture après correction
du fichier de T0.6 demande une **version neuve de ce préenregistrement** (R12), jamais une relance sur ce run » ; l. 1075-1076
(L7b, L7c) : « les lectures de (ii) attendent la levée du nœud **sous une version neuve de ce texte**, qui lit (ii) seule sur les
mêmes scores » à la place de « sous ce même texte » ; l. 934-936 (plan 4 bis) et l. 2016 (CLT7D-03, mention « au brouillon 14 :
version neuve ») de même ; l. 1554-1559 (Relance) : remplacer le « reste déclaré, non tranché » par « **tranché (R-1924 (2))** :
L1 par fichier illisible, L7b et L7c sont des issues finales sous ce texte ; correction par version neuve, clé de registre à
part, lecture de (ii) seule » ; l. 31 (table « du 12 au 13 », ligne 6) et l. 2031 (« trois déclarés non tranchés ») :
« tranchés au brouillon 14 ».

### (3) Garde d'ordre : étape A refusée si `VERDICT-P3BIS` est déjà inscrit

**Juste, et nécessaire.** CLT7B-03 exige `SCORES-T07` et `SONDES-T07` **strictement antérieures** à `VERDICT-P3BIS` (l. 907-908,
919-920, 1138-1139, 1324-1325) ; une étape A ouverte après `VERDICT-P3BIS` écrirait deux lignes postérieures et **toute étape B
sur ce run serait refusée à jamais** : la minute de carte et l'extraction (jusqu'à 10 USD) seraient dépensées pour un run mort.
Le brouillon 13 a aggravé le risque en écrivant que `VERDICT-P3BIS` « peut précéder l'étape A » (l. 1316), alors que l'ordre
forcé par le texte est A < `VERDICT-P3BIS` < B. `SCELLEMENT-P3BIS` et `ISSUE-MOTS-ET-COUT-T06` peuvent, elles, précéder A sans
dommage. Le module devra retirer `VERDICT_P3BIS` de `PERMISES_ETAPE_A` (`registre_v1.py` l. 58) et refuser sa présence à l'étape
A ; `exiger_anteriorite` (l. 185-186) devient inconditionnelle à l'étape B puisque la clé est exigée.

**Lignes à changer** : l. 1315-1317 (Clés par étape, étape A) : « permises `SCELLEMENT-P3BIS` et `ISSUE-MOTS-ET-COUT-T06`
(elles peuvent précéder l'étape A) ; **`VERDICT-P3BIS` présente à l'ouverture de l'étape A → refus, code 2, journalisé** (garde
d'ordre : `SCORES-T07` et `SONDES-T07` doivent lui être strictement antérieures, CLT7B-03 ; une étape A postérieure rendrait
toute étape B impossible sur ce run) ; **si l'étape A n'a pas abouti avant `VERDICT-P3BIS`, la lecture de T0.7 sur ce run est
impossible sous ce texte : nœud, pas une attente** » ; l. 906-909 (Plan, étape A, point 3) : une phrase « l'étape A ne s'ouvre
pas si `VERDICT-P3BIS` est déjà inscrite (garde d'ordre) » ; l. 1138-1139 (Liste d'arrêt) : ajouter « étape A ouverte après
`VERDICT-P3BIS` » ; l. 1561-1565 (essais R5) : « `VERDICT-P3BIS` présente à l'ouverture de l'étape A → refus (artefact) ; absente
→ ouverture (cas sain) » ; table « du 12 au 13 » : ligne neuve au brouillon 14.

### (4) `controle_lecture_t06_v1.py` absent de `main` : cité au commit et vérifié au candidat (marqueur)

**Juste, et je peux déjà fournir ce que le marqueur demande.** Le script est sur `origin/prep/t06-candidat8-v1`, commit
`1ae198b4` (« Candidat 8 : bloc de règle « mots et coût » v2 »), empreinte `ba2ba5cf…` **égale** à celle citée par le texte
(l. 1269) et par le candidat 12 r2 de T0.6 (l. 334). Deux faits à vérifier au candidat, que j'ai lus : (a) `lire_registre`
(l. 61-72 du script) **ignore toute ligne dont la première cellule n'est pas `SCELLEMENT-T07` ou `SCELLEMENT-P3BIS`** (l. 66-67) :
il ne refuse jamais une clé inconnue, il exige exactement une ligne de chacune de ses deux clés (l. 71-72) ; (b) il journalise `OUVERTURE-SONDES-T06`
dans le même `<registre>.ouvertures.md` (l. 101). Le fait (a) corrige le texte (constat M-C) et règle par construction la
demande (4) de la Concordance pour T0.6 (reste T0.8).

**Comment l'écrire** : plutôt qu'un quinzième marqueur, étendre la ligne `<<COMMIT_CODE_T06>>`, `<<EMPREINTES_CODE_T06>>`
(l. 2069) : « y compris `scripts/controle_lecture_t06_v1.py` (`ba2ba5cf…`), cité **au commit** du texte scellé de T0.6, absent de
`main` au 8 novembre (branche `prep/t06-candidat8-v1`, commit `1ae198b4`) ; à vérifier au candidat : empreinte égale,
`lire_registre` ignore toute clé autre que ses deux (l. 66-67), journal `OUVERTURE-SONDES-T06` (l. 101) ». Mettre à jour la
table « du 12 au 13 », ligne 7 (l. 32) si le compte des marqueurs change. Si la mère préfère un marqueur
à part (`<<SCRIPT_CONTROLE_T06>>`), mettre à jour l. 2045-2053 (quinze marqueurs). Dans les deux cas, corriger l. 1269-1270 (« qui prend le registre en argument, l. 20-23 » : exact) et l. 1282-1284 (voir M-C).

## Constats

Classes : **bloquant** (le texte ne peut pas être scellé tel quel), **majeur** (fausserait ou bloquerait une lecture, ou cite un
fait faux qui porte une règle ; à corriger avant scellement), **mineur** (forme, exactitude, précision). Lignes : brouillon 13.

### Bloquant

Aucun.

### Majeurs

**M-A — « `lecture-t07.json` déjà écrit » n'est pas dans la garde d'ouverture de l'étape B** (l. 910-922, 1110-1116, 1317-1327 ;
promesse l. 1551 et l. 1498 ; script `garde_etape_b`). Voir question (a). Sans cette ligne, la « tentative après lui » du
texte n'est pas un refus mais une lecture complète suivie d'un `arret-etape-b.json` écrit et scellé (code 3), avec les scores
ouverts et journalisés : effet de bord contraire à « rien d'écrit » et à R12. Correction, dans les trois listes de la garde et
l. 1543-1551 : « **`diag/<run-t07>/lecture-t07.json` ou `arret-etape-b.json` déjà présent → refus de la garde, code 2, journalisé,
avant toute ouverture des scores** (R12 : la lecture décisive est unique ; un arrêt après manifeste est un nœud, pas une
attente : l'étape B ne se relance pas après un code 3 sous ce texte) » ; essai R5 : « `lecture-t07.json` présent → refus sans
ouverture (artefact) ; `arret-etape-b.json` présent → refus (artefact) ».

**M-B — La définition gelée de la fuite ne fixe pas la valeur par action dont `separation` prend l'aire** (l. 1343 ; consigne
l. 1342 ; l. 2039). Voir question (b). Correction, dans la ligne `AUDIT-FUITES-T07` : « **valeur par action du trait =
indicateur 0/1** (extrait présent dans les jetons notés ; jeton d'empan égal au jeton cité ; forme du champ `COST` égale à la
forme citée ; élément de gabarit présent) ; **aire par `statistiques.aire_simple`** (positifs = condition du jeu, négatifs =
`honnete`) sur **toutes les actions notées des deux conditions** (`mesures-t06.npz`) ; `separation` de cette aire ; nombre écrit
dans `separation` » ; recopier dans la consigne (l. 1342) ; essai R5 : un fichier d'audit dont `separation` ne se recalcule pas
depuis les textes et mesures à 10⁻⁹ près → contre-lecture en échec (pas le module, qui ne vérifie que le domaine).

**M-C — Le texte attribue au script de T0.6 un refus qu'il n'a pas** (l. 1282-1284 : « mêmes refus : […] clé ni exigée ni
permise » ; l. 1285-1287 et 1580 : « refusée là si le script de T0.6 refuse toute clé ni exigée ni permise, à contrôler » ;
l. 1662-1666 : « si `controle_lecture_t06_v1.py` refuse toute clé ni exigée ni permise, les lignes que T0.7 ajoute […] feraient
refuser la lecture de T0.6 »). Fait vérifié sur le script `ba2ba5cf…` (l. 66-67) : il **ignore** toute ligne dont la clé n'est
pas l'une de ses deux ; le refus « clé ni exigée ni permise » est **propre à T0.7** (`registre_v1.py` l. 128-129). La citation
est fausse au pied de la lettre (R6 : un fichier cité par empreinte doit être décrit exactement), et deux règles s'appuient sur
une hypothèse déjà tranchée. Correction : l. 1282-1284 : « mêmes motifs `DATE` et `SHA`, même `sceau_conforme`, mêmes refus de
forme (ligne manquante, en double, mal formée, non strictement antérieure, sceau faux) ; **le refus « clé ni exigée ni permise »
est propre à T0.7 : le script de T0.6 ignore toute clé autre que ses deux** (`lire_registre`, l. 66-67) » ; l. 1285-1287 et
1580 : « égalité des refus sur les deux clés communes ; une clé inconnue est ignorée par le script de T0.6 et traitée ici par la
règle du registre partagé » ; l. 1662-1666 : « le script de T0.6 (`ba2ba5cf…`) ignore les clés de T0.7 par construction ; la
demande ne vise que T0.8 ».

### Mineurs

**m-01** (l. 1543-1547 ; module `ouvrir` l. 258, `journaliser_ouverture` l. 202-206) : la **forme de la ligne de refus** du
journal n'est pas fixée et l'ordre n'est pas dit. Écrire : « une ligne `| REFUS-T07 | date UTC | etape-B/<run> | clés ou
fichiers manquants ou fautifs : motif | registre <sha256> |`, écrite **après tous les contrôles de la garde** (registre, fichiers,
`lecture-t07.json` absent) ; la ligne `OUVERTURE-T07` n'est écrite que si la garde passe ». Le journal est partagé avec T0.6
(`OUVERTURE-SONDES-T06`) : le dire.

**m-02** (l. 572, 1341, 1437-1439, 1509-1511) : frontière de la tolérance en flottants et essai de frontière absent (question c).
Écrire « |`aire` − aire recalculée| > 5 × 10⁻⁴ + 10⁻⁹ » ou « aire recalculée arrondie au nombre de décimales du nombre écrit ≠
nombre écrit » ; essai : écart exactement 5 × 10⁻⁴ (0,7345 écrit 0,735) → pas L7c.

**m-03** (l. 2039-2040) : « rendent la règle de séparation vérifiable par le module » → « rendent le **domaine** de la règle
vérifiable par le module ([0,70 ; 1], `null` si et seulement si `fuite` est `null`) ; le calcul est vérifié par le contre-lecteur
du fichier, sous la consigne scellée ».

**m-04** (l. 912-913 « défait le marqueur 1 du module (déclaré) » ; Module l. 1352 et suivantes) : les changements du module
qu'impose le brouillon 13 ne sont déclarés que pour le marqueur 1. Lister : (i) table A, fichier d'issue de P3-bis et fichier
d'audit contrôlés **dans la garde**, avant tout `try` (`etape_b` l. 644-655) ; (ii) table A à valeur hors de A1 à A5 → **L1
écrite**, plus une `GardeArret` (`lire_table_A` l. 515-516 donne aujourd'hui un code 3) ; (iii) `VERDICT-P3BIS` exigée à l'étape
B et refusée à l'étape A (`PERMISES_ETAPE_A` l. 58, `exiger_anteriorite` l. 185-186) ; (iv) `lire_fuites` par la ligne de registre
et non par la configuration (`audit_fuites`, l. 551), déjà marqueur 6 ; (v) règle du registre partagé (l. 128-129) ; (vi)
`controle_aire`, `tolerance_aire`, `marques_autres_taches` dans `exiger_configuration` ; (vii) ligne de refus au journal.

**m-05** (l. 1542) : « `diag/<run-t07>/arret.json` sur toute `GardeArret` après le manifeste » → « `arret.json` à l'étape A,
`arret-etape-b.json` à l'étape B » (l. 19 du module, l. 916, 1068, 1115 du texte). Même remarque, sans conséquence, pour « ni
`arret.json` » dans les listes de l'étape B (l. 916, 1068, 1115) : ce fichier est celui de l'étape A.

**m-06** (l. 1295-1296) : « (1) cellule de clé mal formée → refus » : préciser « une ligne du registre à quatre cellules dont la
deuxième est une date au format et dont la première ne vérifie pas la forme de clé `[A-Z0-9]+(-[A-Z0-9]+)+` → refus ; le
registre ne porte ni en-tête ni ligne de séparation (créé par `ajouter_ligne`) ; toute autre ligne non conforme est ignorée »
(module l. 123-129 ; le script de T0.6 ignore tout hors ses deux clés).

**m-07** (l. 1999, table historique des constats de cl4) : « fichier illisible → Q = absente, L1 » → ajouter « (valeur nommée
« illisible » depuis le brouillon 13) ».

**m-08** (l. 1035-1039, 1573) : la portée de l'énumération (0) dit « neuf entrées exigées » ; dire aussi ce qu'elle ne
modélise pas : fichier d'audit illisible, `consigne` différente de la ligne, règle du registre partagé, `lecture-t07.json` déjà
présent (ce dernier **est** modélisé par `lecture_deja_ecrite` : le texte ne le dit pas).

**m-09** (l. 1558-1559, et décision (2)) : le texte propose `ISSUE-MOTS-ET-COUT-T06-R1` et `lecture-t07-ii.json` comme exemples
pour la suite ; avec la décision (2), remplacer par la phrase « version neuve de ce préenregistrement, sous une clé de registre
**autre que `SCELLEMENT-T07`** (le script de T0.6 exige exactement une ligne de cette clé, l. 71-72), qui lit (ii) seule ».

## Ce que je n'ai pas relu

Les sections inchangées du brouillon 12 (contre-lues cinq fois) ; le code du module au-delà des fonctions citées
(`criteres_v1.py`, `plancher_v1.py`, `mahalanobis_v1.py`, les essais) ; le script de T0.6 au-delà de `lire_registre`,
`sceau_conforme` et du journal ; le candidat 12 r2 de T0.6 au-delà des l. 160-170, 330-336, 496-548 ; les données de T0.6 et
de P3 (aucune ouverte). Aucun chiffre de ce rapport ne vient de l'état de l'art.
