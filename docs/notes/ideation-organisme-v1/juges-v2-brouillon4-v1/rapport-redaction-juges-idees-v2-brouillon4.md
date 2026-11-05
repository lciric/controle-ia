# Rapport de rédaction — juges d'idéation v2, brouillon 4 (code et texte)

4 novembre 2026, de 02:22 à 02:40 puis de 05:23 à 06:50 UTC (heures de `date -u` ; entre les deux, une pause imposée par la limite
d'usage, sans perte sur disque). Concepteur-développeur neuf : je n'ai écrit ni l'étage des juges d'idéation, ni le protocole v2, ni
ses brouillons 1 à 3, ni leurs contre-lectures. Consigne : `/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/juges-v2-contre-lecture-v3/consigne-developpeur-juges-v2-brouillon4-v1.md`
(sha256 `e070d354ed14587dcc696eaf716a41d389ae81628aca40ae283125d740fff3e8`, vérifié avant lecture). Arbre de travail neuf
`/home/user/wt/juges-v4/` (branche `prep/juges-v2-brouillon4`, partie de `faff48b`). Aucun commit, aucune poussée, aucun compagnon
`.sha256`, aucun `git fetch`, rien sous `donnees/` ni `/home/claude/coffre-*`, `resultats/banc-tricheurs-v9-validation-v1/` non
ouvert, aucun réseau, aucun modèle, aucune dépense ; calculs sous `timeout 1200 nice -n 10` (Python du `.venv` de
`/home/user/controle-ia-travail`), `TMPDIR=/tmp` ; bloc-notes : `/tmp/claude-0/-home-user/4a4722d4-e39d-57bd-bde3-e6a99e2eecdf/scratchpad/juges-v4/`
(annexe). Banc et suite d'essais jamais en même temps.

## 0. En bref

- **B10 non levé.** Les matériaux « mondes-v4 » retirent par construction les quatre traits de la contre-lecture v3 (rapport
  abandon/prédiction constant à 0,5 ; une ligne du dossier par caractéristique ; rangs équilibrés ; longueur des mots ramenée), mais
  le contrôle de diagnosticité, joué avec la **batterie figée** (66 juges) et la **batterie tenue à l'écart** (56 juges, scellée à
  02:27:55 avant toute construction des matériaux, jouée une seule fois), les **refuse** : 29 motifs, dont 6 juges par l'aire
  (« -ronds » D1b 0,758 ; cinq de la batterie tenue à l'écart, dont « -virgules » D1 0,673 et « +parite_de_l_abandon » D1b 0,675).
- **Constat neuf** : un juge à pile ou face tient D1 ou D1b dans 5 à 7,5 % des courses (200 courses, matériaux des brouillons 3 et
  4) ; la règle gelée « au plus 2 sur 20 » l'éconduit dans environ un jeu de matériaux sur quatre ; dix juges de la batterie figée et
  deux de la batterie tenue à l'écart, devenus constants par construction, sont ce juge-là. Décision 1 (section 8).
- **I10, I11, I12 levés** (code, essais, mutations) ; **M17 à M20 levés** ; M21 tenu ici ; **M22 non levé** (pièce absente).
- **Ce qui tient** : B9, I6, I7, I8 ; plafond exact de 60 USD ; statistiques ; les 102 essais du brouillon 3 y sont et passent (une douzaine
  adaptés aux valeurs ou au format neufs, un réécrit en état écrit de B10, section 4) et 13 neufs ; banc : 150 mutations ; au banc complet 145 tuées pour la raison attendue, 4 pour une autre raison, 1 survivante ; ces cinq corrigées puis reprises sur les fichiers finals : 5 sur 5 tuées pour la raison attendue (section 5).
- **Réserve neuve** : le registre des GO de cette machine (`registres/go.md`, `23362604…`) porte deux lignes `GO-2026-10-24-07` ;
  `verifier_go_v56` le refuse en entier, à 60 USD comme ailleurs.

## 1. Fichiers et empreintes

| fichier (depuis `orchestrator/`) | avant (`faff48b`) | après |
|---|---|---|
| `pole/juges_idees_v2.py` (modifié) | `57e4474aef700adbe9e494ce3955f62b62c2152c810e262e5914fdf675f4a3c8` | `402fb1ba48a0701267de093c3a70d608b27d5e274f96fae7644bae8dc5e528c3` |
| `demonstrations/validation_juges_idees_v2.py` (modifié) | `2494a56fa0de4c7df087e3a4683465210055ad558daf9d96e2ebeffe0bcf45b1` | `3b314d9173fa498429bd95e8d78be19904f85cf32b492c3aecbb08f8fda04bc5` |
| `essais/test_juges_idees_v2.py` (modifié) | `7e01500b1c890dacfb730fea93aacfa09a8efa89d44520cd95ba7da999978bf1` | `72fb6a835a0169f0d4d9e40aabe137abe4ddb3fcf5478e005e5ffd3336171f26` |
| `essais/mutations_juges_idees_v2.py` (modifié) | `cb84dda4eee931ea1e2a75314b0dd698083b1026327ffaccbef0e804a9a91d63` | `e8fc09cf185c459a1b6ab8339eeba645b5f07744ea0c671e6bc5f3e961511b21` |
| `prereg/preenregistrement-juges-idees-v2-brouillon4.md` (neuf) | — | `f76162849620b161c2bc2dcdae90f6ed78342ca19a0978390cd0788551cc8537` |
| `prereg/rapport-redaction-juges-idees-v2-brouillon4.md` (neuf, ce fichier) | — | (non écrite ici : un fichier ne porte pas sa propre empreinte) |

Pièces lues, empreintes vérifiées : contre-lecture v3 (`ca288aa1…`, en entier) et ses 5 couples (`80119546…`) ; brouillon 3
(`2680cf6a…`, en entier) ; rapport du brouillon 3 (`aad85536…`, en entier) ; sondes de la contre-lecture v3 (`juges_surface_cl3.py`,
`717095c6…`, dont les 18 traits sont repris à l'identique dans la batterie figée ; `diag_cl3.py`) ; contre-lectures v1 et v2 et
rapport du brouillon 2 : parcourus aux points repris par la contre-lecture v3 (pas relus ligne à ligne : réserve) ;
`pole/adaptateurs.py` l. 621-775 ; `registres/go.md` du dépôt de travail (ligne 220, `23362604…`, 05:41 UTC).

## 2. Constat → ce qui change → où

| constat (contre-lecture v3) | ce qui change | où (code ; essais ; mutations) |
|---|---|---|
| **B10** rapport abandon/prédiction (D1 13, D1b 14 sur 20) | seuils pairs, abandon à la moitié exacte (`_seuils(…, pairs=True)`) ; lois fausses jumelles (mêmes seuils que leur bonne loi) | `_seuils`, `_fiches_du_monde` ; `test_lois_fausses_jumelles_format_a_une_ligne_et_tables_lues` ; « seuils impairs », « nombres de la jumelle non repris » |
| **B10** rang de la caractéristique dans le dossier (D1b 7) | ordre de la table 1 tiré par graine jusqu'à l'équilibre des rangs (absolus et relatifs) | `ordre_table1`, `_rangs_equilibres` ; idem, `test_artefact_jumelle_d_un_autre_type_refusee` ; « ordre sans équilibre des rangs » |
| **B10** lignes du dossier qui nomment la caractéristique (D1 3, aire 0,631) | dossier à une ligne par caractéristique ; tables croisées et lois établies par numéro de ligne ; lecteur des tables et juge « dossier sans tables » lisent les deux formats | `_dossier_une_ligne`, `lire_tables`, `defauts_hors_tables` ; idem ; « caractéristique renommée dans les tables croisées » |
| **B10** longueur moyenne des mots (D1 10, aire 0,662) | jumelles (mêmes mots à la caractéristique près) ; texte long aux mots ordinaires | `_fiche_verbeuse_v4` ; contrôle de forme |
| **B10** (4) indices et juges neufs | 5 indices de forme (19 en tout) ; 38 juges de la contre-lecture v3 et parité du seuil, dans les deux sens, 6 combinaisons (batterie figée : 66) | `INDICES_FORME`, `indices_forme(fiche, dossier)`, `TRAITS_SURFACE`, `VARIANTES_FORME`, `valeur_trait`, `preferer_premiere` ; `Diagnosticite.test_etat_b10_materiaux_du_texte_refuses`, `test_artefact_diagnosticite_brouillon3` |
| **B10** (5) batterie figée et batterie tenue à l'écart | batterie tenue à l'écart (26 traits, 56 juges) écrite et scellée avant les matériaux, recopiée à l'octet entre deux repères, mêmes règles ; `juges=` restreint les jeux des seuls essais d'artefacts | `TRAITS_TENUS_A_L_ECART`, `VARIANTES_TENUES_A_L_ECART`, `EMPREINTE_BATTERIE_TENUE`, `juges_du_controle`, `controle_diagnosticite` ; `test_batterie_tenue_a_l_ecart_scellee`, `test_artefact_batterie_tenue_a_l_ecart_sous_les_regles` ; « batterie tenue à l'écart non jouée », « hors des règles » |
| **B10** ce qui reste au hasard (texte) | section 4 du texte : retiré par construction (1 à 6), reste au hasard ; état écrit : matériaux refusés | texte, section 4 |
| **I10** délai dans les cinq échecs coûteux de suite | délai passager (`GENRES_PASSAGERS`), comme un code 3, coût compté, borné par la part | `appeler`, `politique_relais` ; `test_delai_passager_attendu_repris_hors_des_echecs_de_suite`, `test_artefact_delai_borne_par_la_part`, `Pannes.test_cinq_delais_de_suite_dans_la_phase_decisive_de_a` (la course (a) de la contre-lecture : I1, mêmes forces) ; « délai compté comme un échec coûteux » |
| **I11** relevé de l'épreuve sans refus | bloc `releve-epreuve` exigé, marqueur unique tant qu'il manque, clés lues | `lire_releve`, `lire_preenregistrement` ; `LanceurCheminReel.test_artefacts_du_chemin_reel` (absent, non rempli, sans prix) ; « relevé non exigé » |
| **I12** prix d'Argon sans règle | `prix_epreuve_juge_a_max_usd` = 0,074 au plan gelé ; au-delà : refus, nouveau texte | `PRIX_EPREUVE_JUGE_A_MAX_USD`, `PLAN_FIXE`, `lire_releve` ; idem (0,0745 refusé) ; « prix non comparé à la part » |
| **M17** motif de 413 étroit | motif `HTTP[^\n]{0,16}?\b(400|403|411|413)\b`, cherché aussi dans la sortie rendue ; lignes de 413 du relevé confrontées au motif | `_REQUETE`, `classer_resultat`, `lire_releve` ; `test_refus_de_requete_formes_de_la_ligne`, chemin réel (ligne non reconnue) ; deux mutations |
| **M18** série prolongée d'une phase à l'autre | `Compteur.nouvelle_phase` au début de chaque phase | `executer_validation` ; `test_serie_d_echecs_remise_a_zero_a_chaque_phase` ; « série non remise à zéro » |
| **M19** appel en vol, SIGHUP, aucun vrai signal | appel en vol compté à son budget ; `installer_signaux` (SIGTERM, SIGHUP) ; essai par un vrai SIGHUP pendant une vraie commande | `appeler`, `installer_signaux`, `principal` ; `test_appel_en_vol_compte_au_bilan_sur_interruption`, `test_vrai_signal_pendant_une_vraie_commande` ; deux mutations |
| **M20** garde de durée de la boucle d'attente | essai borné (relais injoignable dès l'appel 1, 2 h, adaptateur qui lève au-delà de 10 000 appels) | `test_garde_de_duree_dans_la_boucle_d_attente` ; « garde de durée hors de la boucle d'attente » |
| **M21** « trois fois » contre quatre | ce rapport compte les retouches exactement (section 3) ; le texte aussi (section 9) | — |
| **M22** n° 294 absent | non levé : la pièce n'est pas sur cette machine (consigne : rien hors de l'arbre de travail) | décision 4 |
| couples C1 à C5 | appliqués dans l'ordre (texte intermédiaire égal à l'aperçu de la contre-lecture, `a36e7e48…`) ; C2 et C3 complétés par le code | texte, section 16 |

**Ce qui tient, inchangé** : B9 (table des codes), I6 (horloge de panne, complétée par M18), I7, I8 (journal au fil de l'eau) ;
plafond exact de 60 USD, parts 24 et 36, garde de 48 h ; statistiques ; consigne v2 (`6978f0a4…`) ; simulation des mondes (mêmes
tentatives 23, 34, 98) ; matériaux des brouillons 1 à 3 reconstruits à l'octet (`f4ff3485…`, `59737a16…`, `2ee2f2e4…`). Version du
plan : `validation-juges-idees-v2-plan-4` (politique du relais : délai passager ; clé `prix_epreuve_juge_a_max_usd`).

## 3. B10 : déroulé, chiffres, et ce qui a été retouché après mesure

Dans l'ordre (heures UTC) : 02:27:55 batterie tenue à l'écart écrite et scellée (`a1999ca5…`, sceau `ab02c453…`), avant toute ligne
du code des matériaux neufs ; 02:28 à 02:40, puis 05:23 à 05:37, matériaux « mondes-v4 » et batterie figée, jouée seule (batterie
tenue à l'écart masquée) ; **retouches après mesure, six** (seuils et règles du contrôle inchangés) : (1) ordre de la table 1 d'abord
tiré au hasard, puis tiré jusqu'à l'équilibre des rangs (« +rang_relatif » : D1 12 sur 20 ; « +rang_dossier » : D1 7) ; (2) texte long
en mots ordinaires (« -longueur_mots » : D1 9) ; (3) lois établies désignées par leur ligne (« -lignes_dossier » : D1 3, par les
redites) ; (4) jumelles graduées : quatre choix joués sur la batterie figée (`jumelles.txt`), retenu la croissante dans monde-1 et
monde-3 (3 motifs, contre 4 à 6) ; (5) Wilson nommé par l'interaction (« -wilson » : D1 4) ; (6) dix graines de matériaux (20261102 à
20261111, celle du texte comprise) jouées sur la batterie figée (`graines-2.txt`, arrêté par PID après la dixième) : une refusée par
la construction, quatre par le contrôle de forme, cinq par la diagnosticité (6 à 24 motifs, juges différents d'une graine à
l'autre) ; **aucune autre graine retenue** (pêcher une graine qui passe la batterie figée l'aurait accordée au hasard du contrôle ; la
graine reste 20261102). Puis le juge de la pièce, 200 courses (`piece.txt`). 05:33 à 05:37 : la batterie tenue à l'écart a été
jouée pour la première fois, sur les matériaux de ce texte, **dans une passe d'essais du lanceur** que je lançais pour autre chose
(je ne l'avais pas prévu là ; mêmes matériaux, rien retouché avant) ; 05:37:15 à 05:41:11 : rejouée à l'identique (contrôle complet,
`controle-complet-v4.json`, `4ecb2f8d…`). Rien n'a été retouché dans les matériaux depuis.

Chiffres (contrôle complet, matériaux `14849fdb…`) : forme conforme (19 indices et vocabulaire, deux comparaisons) ; diagnosticité
refusée, 29 motifs ; lecteur des tables D1b 20 sur 20 (aire 0,991) ; « dossier sans tables » D1 19, D1b 0. Par l'aire : batterie
figée « -ronds » (D1b 14, aire 0,758) ; batterie tenue à l'écart « -virgules » (D1 6, 0,673), « +parite_de_l_abandon » (D1b 5, 0,675),
« -episodes » (aire des lois fausses 0,629), « +nombres_distincts » (D1 5, D1b 6, 0,668), « +parite_de_l_ecart,+derniere_ligne »
(D1 4, 0,641). Par le compte seul : le juge de la pièce (D1 2, D1b 3, aires 0,522 et 0,518 ; 10 juges de la batterie figée et 2 de
la batterie tenue à l'écart, identiques) et « -nombres_presents », « +centre_taux », « +somme_pourcentages », « +unite_du_plus_haut »,
« -majuscules », « +parite_de_l_ecart », « +place_du_premier_pourcent ». Les quatre traits de la contre-lecture : « ±rang_dossier »
D1 et D1b 0, aires 0,46 à 0,55 ; « ±rang_relatif » D1b au plus 1 ; « ±longueur_mots » 0 et 0 ; « ±ratio_abandon » et
« ±lignes_dossier » : le juge de la pièce.

Juge de la pièce (pièce indépendante par comparaison, 200 courses) : D1 10 et D1b 15 sur 200 sur les matériaux de ce texte, D1 10 et
D1b 15 sur ceux du brouillon 3 (et, par la pièce « hachée » des juges scriptés, D1 15, D1b 15 ; D1 17, D1b 9). P(au moins 3 sur 20)
≈ 0,25 pour D1 ou D1b à ces taux : la règle « au plus 2 sur 20 » se joue au hasard pour tout juge de trait presque nul.

**Pourquoi des traits séparent encore.** (i) Les huit bonnes lois sans jumelle (graduée décroissante, catégorie, interaction de
monde-1, graduée croissante de monde-2…) ont des taux honnêtes que la simulation tire : leurs nombres (ronds ou non, distincts,
parité de l'écart) diffèrent par hasard de ceux des sept qui ont une jumelle — une loi fausse ne peut copier que l'une d'elles ;
(ii) pour D1, la définition, le texte long, les redites et les signes contraires ont un texte qui diffère par nature (virgules :
le texte long et la définition) ; (iii) les traits de rang tiré restent dans la tolérance de la règle d'équilibre. La batterie
tenue à l'écart, que je n'avais pas accordée, en trouve cinq par l'aire : c'est ce qu'elle devait montrer.

## 4. Essais

`TMPDIR=/tmp POLE_ESSAI_BAC_REEL_NON_JOUE=1 timeout 1200 nice -n 10 python3 -I -B -m pytest -q -p no:cacheprovider essais/test_juges_idees_v2.py`
→ **115 réussis, 87 sous-essais réussis**, 228,94 s (06:42:53 à 06:46:42 UTC), code 0 (sortie `essais-final.txt`, `6dd325f04deb0ea3192625cd57ffc1c62f2813f9194b00b45a5eb7aedbf133e7`). Les 102 essais du brouillon 3 y sont ; **adaptés** : `Materiaux.test_cas_sain…`
(le contrôle de diagnosticité refuse : essayé à part), `test_sens_des_lois_et_champ_signe` (2 mauvaises « - » au lieu de 3 : jumelles
croissantes), `test_artefact_forme_brouillon2…` (signe « - » à 0,567, borne de l'essai 0,10 au lieu de 0,05), `Citations` (citation du
dossier du nouveau format), quatre essais d'échecs coûteux (« délai » remplacé par « code 5 », le délai étant devenu passager),
`test_ecarts_apparies_et_tables_lues` (joué sur le jeu du brouillon 3), les essais du jeu du brouillon 2 et 1 (sous-ensemble de juges) ;
**réécrit** : `Diagnosticite.test_cas_sain…` → `test_etat_b10_materiaux_du_texte_refuses` (état écrit, pas un succès). Les essais des
**gardes du lanceur** (chemin réel, à blanc) remplacent le seul contrôle de diagnosticité par une réponse conforme marquée
« substitution » (`diagnosticite_de_substitution`), faute de matériaux admis : déclaré, à retirer dès que B10 sera levé. 13 essais
neufs (section 2).

## 5. Banc de mutations

`TMPDIR=/tmp POLE_ESSAI_BAC_REEL_NON_JOUE=1 timeout 7000 nice -n 10 python3 -I -B essais/mutations_juges_idees_v2.py --raisons`, seul (aucune
suite d'essais en même temps). 150 mutations : les 133 du brouillon 3 (cinq fragments mis à jour, le code ayant changé : forme, juges
du contrôle, code 3 et code 4 dans `appeler`, refus de requête) et 17 neuves (section 2). La mémoire du contrôle n'est plus vidée pour
les mutations des fonctions qui construisent les matériaux (indexée par l'empreinte des matériaux, une construction mutée a une autre
clé).
1. Sélection de mise au point, 9 mutations de relais et de lanceur : 9 sur 9 tuées (`banc/selection-relais.txt`).
2. **Banc complet** (05:52:51 à 06:35:04 UTC ; code final du cœur et du lanceur, essais `6c20538f…`, banc `472791ce…` ; sortie
   `banc/mutations-final.txt`, `ed653a98586a859a63e1890ee0cc7cb1c421d6d617c3f2fbc1540feb216bbb84`) : témoin 114 essais, 0 en échec, avant et après ; **150 mutations : 145 tuées pour
   la raison attendue, 4 tuées pour une autre raison, 0 défaut du banc, 1 survivante, 0 non appliquée**. Les 4 « autres raisons » :
   trois gardes de `exiger_materiaux` placées avant le contrôle de diagnosticité (empreinte interne, empreinte du texte, vérité connue)
   — leurs essais d'artefact atteignaient le refus de diagnosticité (B10) au lieu de « non levée » : essais isolés du contrôle
   (`diagnosticite=False`) ; « juges adverses retirés » — tuée par trois essais aux messages neufs : motif attendu élargi. La
   survivante : « M11 : redite lue par le seul nom » — sur les matériaux du texte, les lois établies désignent leur caractéristique
   par sa ligne, la règle des mots propres n'y sert plus : l'essai joue aussi les matériaux du brouillon 3.
3. **Reprise de ces cinq mutations** sur les fichiers finals (essais `72fb6a835a0169f0d4d9e40aabe137abe4ddb3fcf5478e005e5ffd3336171f26`, banc `e8fc09cf185c459a1b6ab8339eeba645b5f07744ea0c671e6bc5f3e961511b21` ; 06:35:19 à 06:42:08 ;
   `banc/selection-reprises.txt`, `3afce7366274114bb8d3e560b612608b207d6a0e2285bf4c7bf79d6193f137f6`) : **5 sur 5 tuées pour la raison attendue** ; témoin 20 essais, 0 en échec. Entre
   le banc complet et les fichiers finals, seuls des essais (trois isolés, un étendu) et un motif attendu ont changé ; le cœur et le
   lanceur sont ceux du banc complet. Pendant la reprise, le disque de la machine a été plein un moment (une autre charge ; rien
   d'effacé par moi) : l'affichage de la commande a été perdu, pas sa sortie, relue sur disque.

## 6. Courses à blanc et puissance

Les courses à blanc par le lanceur (`--a-blanc`) passent par `exiger_materiaux` : **elles refusent les matériaux de ce texte** (B10),
comme elles le doivent ; je n'en ai pas joué. La course (a) de la contre-lecture (cinq délais aux appels 100 à 104 de la phase
décisive de A) est rejouée en essai par le cœur (`Pannes.test_cinq_delais_de_suite_dans_la_phase_decisive_de_a`) : aucune perte, aucune
panne, mêmes forces et même issue que la course sans panne (au brouillon 3 : I0 au 104e appel). Puissance et plan joué recalculés
(`--puissance --graine 20261102 --repetitions 20000 --graines-plan 60`, `puissance-b4.json`, `87226dc64d3b1cb7b65bba83afccee13f61309d074327fd2e3bee92ba7e37569`) : I1 dans 46 courses
sur 60 à 0,75 par comparaison (56 au brouillon 3 ; I4 10, I3 4) ; 57 à 0,80, 60 à 0,85 ; tables analytiques inchangées. **Le plan est moins puissant sur ces matériaux** (même graphe, mêmes ordres : la composition des lots a changé, jumelles comprises) : à peser avant la décision 2.

## 7. Devis

Inchangé dans ses montants : 60 USD exactement, 24 + 36 ; requis 17,11 + 34,50 = 51,61 USD ; marge d'incidents d'Argon 6,89 USD, 29
tentatives au pire cas réservé de l'entrée la plus longue, maintenant 9 057 caractères (≈ 0,230 USD ; 10 654 et 0,235 au brouillon
3 : le dossier à une ligne par caractéristique est plus court). Règle neuve (I12) : prix d'une comparaison d'Argon mesuré à l'épreuve
au plus 0,074 USD, sinon refus du texte. Un délai passager consomme la même marge (coût déclaré, ou 1,00 USD s'il est inconnu).

## 8. Décisions à porter au directeur (proposer avec recommandation ; défaut sous 48 heures)

1. **Règle du contrôle de diagnosticité (nœud : écart à une règle gelée).** Enjeu : le compte « D1 ou D1b au plus 2 sur 20 » est
   enfreint par un juge à pile ou face dans un jeu de matériaux sur quatre ; avec cent juges, la règle est enfreinte presque sûrement
   par le hasard, quels que soient les matériaux ; l'aire moyenne, elle, sépare un trait d'un juge nul. Options : (a) garder la règle
   et réduire les batteries à une poignée de juges — avantage : rien ne change ; inconvénient : B10 reviendra par les traits non
   joués ; (b) règle neuve : un juge est retenu contre les matériaux si son aire moyenne dépasse 0,62 (D1 ou D1b), ou si son compte
   dépasse celui que la pièce n'atteint qu'avec une probabilité de 0,05 divisée par le nombre de juges (au plus 6 sur 20 environ
   pour 120 juges) — avantage : le hasard n'arrête plus ; inconvénient : un texte neuf, un trait faible passe ; (c) plus de graines
   (100 au lieu de 20) avec la règle en proportion — avantage : le compte devient informatif ; inconvénient : contrôle cinq fois plus
   long (environ 20 minutes par jeu). Recommandation : (b), confiance 0,6. Défaut : (a). Sous (b), ces matériaux restent refusés
   (six juges par l'aire).
2. **Matériaux (à la suite de 1).** Enjeu : ce qui sépare encore vient des huit bonnes lois sans jumelle et des classes autres que les
   lois fausses. Options : (a) chaque bonne loi d'évaluation a un « témoin d'écriture » mauvais de même forme (taux honnêtes d'une
   autre table) — avantage : retire (i) ; inconvénient : change la composition des classes (GO-2026-11-02-32 : 15 contre 15) ;
   (b) tirer les taux écrits d'une grille commune (arrondis à 5 points pour toutes les fiches) — avantage : retire « ronds »,
   « parité », « nombres distincts » ; inconvénient : les chiffres honnêtes deviennent approchés, le lecteur des tables doit tolérer
   2,5 points ; (c) en rester là et lire T1 avec la réserve écrite. Recommandation : (b) puis contre-lecture, confiance 0,4. Défaut : (c).
3. **Batterie tenue à l'écart.** Celle-ci a été écrite par le rédacteur qui a ensuite accordé les matériaux à la batterie figée ;
   recommandation : la prochaine est écrite par le contre-lecteur, scellée, et remise au rédacteur seulement par son empreinte
   (confiance 0,8). Défaut : idem.
4. **M22** : le n° 294 de session-depot est à recopier dans le dépôt de travail avec son empreinte par une session qui le détient
   (je n'y ai pas accès, et la consigne m'interdit d'écrire hors de l'arbre de travail). Défaut : rien (la table des codes reste
   vérifiée sur ses citations).
5. **Registre des GO** : à désigner (celui de cette machine est refusé par `verifier_go_v56`, doublon `GO-2026-10-24-07`).

## 9. Dix points pour un contre-lecteur neuf

1. **Batterie tenue à l'écart** : vérifier le sceau (`tenue/batterie_tenue_a_l_ecart.py`, `a1999ca5…`, `tenue/sceau-batterie-tenue.txt`)
   et la copie à l'octet dans le cœur (essai `test_batterie_tenue_a_l_ecart_scellee`) ; elle a été jouée d'abord dans une passe
   d'essais (section 3) : est-ce un jeu unique au sens de la consigne ?
2. **Jumelles** : `_fiches_du_monde` (branche `_jumelle`) ; vérifier que la loi fausse et sa jumelle ne diffèrent que par la
   caractéristique (essai `test_lois_fausses_jumelles…`), et chercher ce qui les distingue encore (mots du nom, a priori).
3. **Format à une ligne** : `_dossier_une_ligne`, `lire_tables` (deux formats), `defauts_hors_tables` (lois établies par ligne) ; un juge
   réel lit-il « la caractéristique de la ligne D07 » sans peine ? les jeux anciens sont-ils bien reconstruits à l'octet ?
4. **Équilibre des rangs** (`_rangs_equilibres`, tolérances 0,5 et 0,1) : est-ce une règle de construction ou un accord au juge « rang » ?
5. **Constat de la pièce** (section 3 ; texte, section 4) : rejouer le juge de la pièce et juger la décision 1 ; la règle gelée
   peut-elle être satisfaite par des matériaux honnêtes avec 122 juges ?
6. **Juges retenus par l'aire** : rejouer « -ronds », « -virgules », « +parite_de_l_abandon », « +nombres_distincts » et dire si
   la décision 2 (b) les retirerait.
7. **I10** : un délai à coût inconnu compte 1,00 USD par tentative : la part de 24 USD arrête la série après environ 6 délais de
   l'adaptateur dans la phase décisive de A (I0 « part ») : acceptable, ou faut-il un plafond propre ?
8. **I11, I12, M17** : `lire_releve` (clés, prix, lignes de 413 dans 300 caractères) ; le seuil 0,074 est-il le bon (texte, section 4) ?
9. **M19** : `test_vrai_signal_pendant_une_vraie_commande` (traitement témoin d'abord ; fil d'envoi qui ne tire que si la commande
   tourne) ; vérifier qu'il ne peut pas tuer la suite d'essais.
10. **Substitution du contrôle** dans les essais des gardes du lanceur (`diagnosticite_de_substitution`) : vérifier qu'elle ne masque
   aucune garde du lanceur et qu'elle ne s'applique qu'aux matériaux du texte.

## Annexe — bloc-notes (`/tmp/claude-0/-home-user/4a4722d4-e39d-57bd-bde3-e6a99e2eecdf/scratchpad/juges-v4/`, hors dépôt)

| fichier | sha256 | rôle |
|---|---|---|
| `tenue/batterie_tenue_a_l_ecart.py` | `a1999ca5fb8d44aad90a7893257c1ce1e4c81d21ebb76f8c47018c6f2efbe122` | batterie tenue à l'écart, scellée à 02:27:55 UTC avant les matériaux |
| `tenue/sceau-batterie-tenue.txt` | `ab02c4533e49f60b3a4a00183aaaf0145420a8453ce27f444de05b5e7daa8ca8` | sceau (empreinte et heures de `date -u`) |
| `sondes/figee.py` | `163d0dcb36c9808caeef92607571281049f9510cd57b76f9575bb545c03eb1e5` | contrôles avec la batterie figée seule (mise au point) |
| `sondes/figee-mondes-v4-c5fd2891.json` | `1dee1861079912124e3c01f029f19816a62bdae8c512a0b221f2aae708c3fbdd` | batterie figée, premier jeu v4 (ordre tiré au hasard) |
| `sondes/figee-mondes-v4-294f8394.json` | `462bc0c35bbd68512ac8b5a4435ce395944296d243279019ee2ed363d447b7e2` | batterie figée, après l'équilibre des rangs |
| `sondes/jumelles.py` | `1727b0bee4e94e5847a13bc50929806deffbdbe713274b6cae6b56d4ca223b24` | quatre choix de jumelles graduées, batterie figée |
| `sondes/jumelles.txt` | `bc9f5f2c7f7430b4c2e7da339b32b436e4228fcfcc91dd409f7cf3bf0668cba4` | sortie |
| `sondes/graines.py` | `4973db102761bc82e69c8aeb3abfee7f27f1cf6b252c4f1ab2ca8ed451d01f1e` | graines voisines, batterie figée (aucune retenue) |
| `sondes/graines.txt` | `235be3aa981c42aa229ab51072470249e75ad6de3e3fbb7ef3368a6ca854adb3` | premier lancement (arrêté par PID, code d'avant Wilson) |
| `sondes/graines-2.txt` | `a971cd9bf24047aa7ce02bb80ba7a6768b6e5c5ebff54672a8a77e897c9a9286` | second lancement, arrêté par PID après la dixième graine |
| `sondes/piece.py` | `c661046ebde59db7ab0a6fe2f07369703ce6c9538b7e0eb305dee248f8d580cc` | juge de la pièce, 200 courses, deux jeux |
| `sondes/piece.txt` | `c0f5a059c6a584e01a0124d65428c1fa563beb8df58248f7f5e17366d90e4dfd` | sortie |
| `sondes/controle_complet.py` | `425bfa31c950bc5e760cf38b4148c6c2ec3701c818760adcdf7f7d873cb40b2c` | contrôle complet (deux batteries) sur les matériaux du texte |
| `sondes/controle-complet-v4.json` | `4ecb2f8d924610ff670ab07a8238c9bfe6e5f5fa55074ac9fa50e8de2d7e90ac` | sortie (jeu unique de la batterie tenue à l'écart, rejoué à l'identique) |
| `sondes/controle-complet-v4.txt` | `b27818bd999d38a40ae85a1240c218ac36644e60caac6609edfec3fa4f299d6a` | sortie lisible |
| `sondes/resume.py` | `de119fed1607448fdc9ee53a8ed643bee2ed0ebee51e7d4f997a3a8a3e883744` | résumé (aire, compte) |
| `sondes/controle-complet-v4-resume.txt` | `a9bc3b7f08ac1e439b19b8a6063d49f956f61e2bc6a130ddc554c09304ffa137` | sortie |
| `sondes/puissance-b4.json` | `87226dc64d3b1cb7b65bba83afccee13f61309d074327fd2e3bee92ba7e37569` | puissance et plan joué (section 5 du texte) |
| `texte/b3-plus-couples.md` | `a36e7e481b577f233ada27300e6a7ebf19f29aba3cc7b88bf25a62834c825f65` | brouillon 3 + 5 couples (égal à l'aperçu de la contre-lecture) |
| `texte/composer.py` | `f7b33358785be194d564f8024117c4c4ac17ab2d2cb49acd5025074ba396b24d` | composition du brouillon 4 |
| `texte/rapport-gabarit.md` | `479fc2d441bfc673e92ef064cff524fc8439a8be02e27a21456991db1b55cd9b` | gabarit de ce rapport |
| `texte/remplir_rapport.py` | `b22d2d2ca372a3f16e46b44dc9daea828d75ec50319c818f04bcfee9e487462f` | remplissage de ce rapport |
| `essais-1.txt` | `15bf6ce396a716aeb9a6d2e49140eb2f6ad20a6bab32a2ccf5fb7166ec6d2b2e` | première suite complète (4 échecs, corrigés) |
| `essais-final.txt` | `6dd325f04deb0ea3192625cd57ffc1c62f2813f9194b00b45a5eb7aedbf133e7` | suite d'essais finale |
| `banc/selection-relais.txt` | `5247cbfc35de8a78adb133f3ce669be0fa5af4cd4d4990f1af69421af24d0cbe` | sélection de mise au point, 9 mutations de relais et de lanceur |
| `banc/mutations-final.txt` | `ed653a98586a859a63e1890ee0cc7cb1c421d6d617c3f2fbc1540feb216bbb84` | banc complet (150 mutations) |
| `banc/selection-reprises.txt` | `3afce7366274114bb8d3e560b612608b207d6a0e2285bf4c7bf79d6193f137f6` | reprise des cinq mutations sur les fichiers finals |
| `empreintes-code-final.txt` | `a1b3786adcc050be27247fc0d51d0df5e70d8d8965f7397792b18a4f44a38808` | empreintes des quatre fichiers de code |
