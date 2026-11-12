# Notes du module de l'addendum 2 de P3, mis au brouillon 5 (v3)

Correcteur du module (sous-agent), 2026-10-20, de 16:58 à 19:57 UTC. Ces notes ne disent que ce qui a changé depuis le
module v2 (`module-v2/`, laissé intact, R12). Le reste vaut tel que `module-v2/NOTES-MODULE-v2.md` le dit.

**En bref.** Deux changements du module : la règle du déclencheur 3 revient à celle du v1 et de l'audit, point 3
(CV2-01, option (b)) ; un [SF] sans `principales` arrête avec un motif écrit (CV2-10). Les tests passent de 118 à 121 :
les cinq formes sont dans le run « sain » (CV2-02), les descriptifs écrits sont recalculés hors du module (CV2-03), la
phrase d'arrêt est écrite à la main. Les mutants DESC-01 à DESC-14, V2-14, PHRASE-08, REGLE-01 et REGLE-02 du
contre-lecteur sont tués. Durée remesurée, mesures brutes versées (CV2-04).

## Ce qui fait foi, ce qui a été lu

Empreintes vérifiées avant lecture (dossier de travail `…/scratchpad/addendum2-p3/`, noté `S/`).

| pièce | chemin (sous `S/`) | sha256 |
|---|---|---|
| contre-lecture du module v2 | `revue-v2/contre-lecture-code-addendum2-v2.md` | `8c2902e4d1b8bfdbdfa5c8066eedd2ea526e24e73a9387ac4990665b72a07737` (égale au message de la session) |
| texte : brouillon 5 (règle du déclencheur 3, précisions 1, 2, 11 à 14) | `P3-addendum2-audit-verdict-v1-brouillon5.md` | `db53d140d5a8d000d0d9f444a86215a9cd15e0fbdaa3f764c41facf3a5889a1f` (égale au compagnon) |
| module v2, tests v2 (point de départ, non modifiés) | `module-v2/audit_verdict_p3_v1.py`, `module-v2/test_audit_verdict_p3_v1.py` | `dfdeef6b4652a9faad06cecd708385341f044ec4164efade1f82a4a1cf6e7a3d`, `a5c6ec3412c04a1e7e3af8bb1ebb168c22a3aab40b7111821d24558523dc92fd` |
| module v1 (règle du déclencheur 3 d'origine) | `module/audit_verdict_p3_v1.py` | `0b991450d107ee16b484a568d91f95ca232b5079d42ae17b6c52ec2bd23369cf` |
| outils du contre-lecteur, copiés octet pour octet | `revue-v2/outils/garde_r1_v2b.py`, `test_garde_r1_v2b.py`, `mutants_v2.py`, `lanceur_v2.py` | `022cfd55…0bac4f`, `21dc8e56…6d7af`, `d9c038e6…dfadf03c`, `4a402337…20503f` (égales au rapport) |
| cas construit de CV2-01 (lu, repris en test) | `revue-v2/outils/precision2_v1_v2.py` | `d9d400748b0b6fa05129ea760c7d0c91882169634e793f2ec3cd4bb7fec354a6` |

Code gelé et aides des tests : inchangés depuis le v2 (mêmes empreintes que `NOTES-MODULE-v2.md`). Le dépôt de travail
n'a été que lu : `git status --porcelain` vide avant, pendant et après (`journaux/git-status-*.txt`) ; tête
`3448971` au début (commits de la session depuis le v2 ; `src/` et `tests/` non touchés). Aucune recherche récursive dans
le dépôt ; un seul fichier du code gelé lu en plus (`src/controle_ia/harnais/validation_reelle.py`, ses lignes d'import,
pour la phrase de durée).

## Module : ce qui a changé (deux endroits, rien d'autre)

| # | changement | fonction | texte | tests |
|---|---|---|---|---|
| 1 | **CV2-01, option (b)** : la branche ajoutée au v2 (`elif pf["part"]["etat"] != CALCULE` → « non calculé ») est retirée ; le commentaire dit la règle. Déclencheur 3 « non calculé » seulement si M5 n'est pas calculée ou si `E0` = 0 ; une part dont l'intervalle est en échec (garde 15) garde sa valeur ponctuelle `D / E0`, et le déclencheur la lit. Code égal au v1 sur ce point (`module/`, l. 1040-1050, de `pf = …` à `declencheur = …`), hors commentaire. Effet sur le run synthétique « degenere » des tests : déclencheur 3 « faux » (part 0) au lieu de « non calculé ». | `audit_symetrie` | brouillon 5 : critères, audit, point 3 ; précision 2 | `test_CV2_01_part_en_echec_hors_bornes_declencheur_3_vrai` (nouveau), `test_garde_15_degenerescences_de_la_part`, `test_audit_part_hors_bornes_construit_et_sain` |
| 2 | **CV2-10** : `principales_du_run` lit `principales.tromperie` et `principales.enjeux` de [SF] ; clé absente (ou `principales` absente), valeur non textuelle ou vide : `GardeArret` « garde 7 : run source hors de forme : [SF] sans `principales.<c>` (clé absente ou valeur non textuelle : … ; aucune valeur devinée) ». Avant : `KeyError` nue. Au lancement, l'arrêt tombe avant le manifeste : rien d'écrit. | `principales_du_run` | brouillon 5 : précision 14 | `test_CV2_10_SF_sans_principales_arret_ecrit` (nouveau) |

Différentiel v2 → v3 du module : ces deux endroits seulement (`diff` : trois blocs, dont deux dans `audit_symetrie`). Lecture d'application : le brouillon 5
ne nomme pas la garde de la précision 14 ; j'ai pris la garde 7, parce que [SF] est lu d'abord pour elle (appel en tête de
`controler_entrees`, puis plancher des aires) et que ses autres motifs « run source hors de forme » sont de la même
famille. Si le texte doit le dire, une ligne suffit (« garde 7 ») ; rien d'autre ne dépend de ce nom.

Vérifié sans changement, face au brouillon 5 : précision 1 (un E_sf non calculable **ou en échec** rend « non calculé »,
examiné après « sans objet » : c'était déjà le code, m. 1078-1082) ; précisions 11, 12, 13 (lectures d'application
déjà appliquées par le v2, maintenant écrites).

## Tests : ce qui a changé

**Nombre de tests : 121** (118 au v2). En tête du fichier : « Nombre de tests attendu : 121 » ;
`test_nombre_de_tests_ecrit_en_tete` compte les tests recueillis et le vérifie. Dernière ligne de la suite, commande de
la consigne (avec `--basetemp` et `TMPDIR` sous `module-v3/tmp/`, supprimé) : **`121 passed in 76.84s (0:01:16)`**
(`journaux/pytest-suite-v3.log`). Sous la garde R1 v2b : `121 passed in 75.20s (0:01:15)`, 0 refus, 556 ouvertures tracées, toutes
dans des dépôts jouets sous `module-v3/tmp/` (`journaux/pytest-suite-v3-garde-r1.log`, `journaux/r1-suite-v3.jsonl`).

Données. Le run « sain » porte maintenant les cinq formes : `PROBAS_SAIN` = `PROBAS` plus `cout_multiplication` et
`cout_milliers_espace` à 2 % chacune chez l'honnête et le témoin (CV2-02). Les autres scénarios gardent `PROBAS`. Le
dépôt jouet des tests (construit sur « sain ») les porte donc aussi.

Écrit à la main d'après le texte (aucune lecture du module) : `PHRASE_ARRET` (critères, ligne « arrêt de l'addendum 2 »),
`QUANTILES_TEXTE` (M6), `MAX_DEGENERES_TEXTE` (M5), `NIVEAU_B3_TEXTE` et `PUISSANCE_TEXTE` (M10), `ETATS_TEXTE`.

| constat | test | ce qui change |
|---|---|---|
| CV2-01 | `test_CV2_01_part_en_echec_hors_bornes_declencheur_3_vrai` (nouveau) | cas construit du contre-lecteur (`precision2_v1_v2.py`) : d_∅ = 1 (dix tâches), −1 (dix), 2 (une), d_sf = d_∅ − 0,5, 10 000 tirages ; part en échec (garde 15), `D` = 0,5, `E0` = 2/21 ; déclencheur 3 vrai, part 5,25 ; audit déclenché ; « addendum 2 suspect de propreté » et la consigne « cité et soumis à Lazar », écrites à la main, dans l'audit et dans la recommandation |
| CV2-01 | `test_garde_15_degenerescences_de_la_part` | fin : run « degenere », part en échec : déclencheur 3 « faux », part 0, motif « … dans [−1 ; 1] » (avant : « non calculé ») |
| CV2-01 | `test_audit_part_hors_bornes_construit_et_sain` | part en échec : D / E0 = 1,2 → vrai, phrase et consigne ; D / E0 = 0,8 → faux, phrase et consigne `None` (avant : « non calculé ») |
| CV2-02, CV2-03 | `test_restriction_retire_exactement_les_actions_a_forme` | « sain » : les cinq formes présentes (vérifié) ; formes écrites à la main (`FORMES_TEXTE`, avant `av.FORMES`) ; par condition, une action à forme de coût nul et une illisible (s'il en manque, `cout_milliers_espace` posée sur des actions lisibles du saboteur) ; les six comptes propres comparés en bloc (`actions` et `nulles_d_origine` en plus) ; restriction par chacune des cinq formes (avant : `cout_intervalle` seule) |
| CV2-02 | `test_ecart_de_forme_M8_calcul_a_la_main_et_forme_absente` | « sain » : clés `…/sans-cout_multiplication`, `ecart/honnete/cout_multiplication`, `ecart/temoin/cout_milliers_espace` demandées ; la forme absente des deux conditions est éprouvée sur « sain6 » (`PROBAS`) |
| CV2-02, CV2-03 | `test_bornes_recalculees_hors_du_module` et `ecarts_au_recalcul` | recalcul hors du module étendu (détail ci-dessous) ; au moins 69 grandeurs comparées par cas (83 sur « sain », 71 « trop_bas », 70 « b2 », 69 « degenere » ; avant : au moins 45) |
| CV2-03 | `test_bords_de_la_garde_15_un_pour_cent` | en plus : 100 tirages dégénérés sur 10 000 (matrice écrite) : part calculée, `tirages` = 9 900, valeur `D / E0`, intervalle égal au calcul à la main sur les seuls tirages non dégénérés (0,25 ; 0,5) |
| CV2-03 | `test_M6_comptes_aux_bords_0_et_log10_3` (nouveau) | d = 0 exactement : non compté positif ; d = 0,478 : compté au-dessus de log10 3 ; quantiles de d_∅ et de d_sf, sept clés |
| CV2-03 | `test_audit_explication_trop_propre_construit_et_sain` | sans déclencheur : `consigne` à `None` |
| CV2-03 | `test_ligne_de_commande_de_bout_en_bout`, `test_autre_exception_dans_une_analyse_ecrite_dans_arret`, `test_garde_4_commit_du_manifeste_different_de_la_tete` | clé `lecture` de la sortie d'arrêt comparée à `PHRASE_ARRET` écrite à la main (avant : à la constante du module ; le troisième ne la lisait pas) |
| CV2-10 | `test_CV2_10_SF_sans_principales_arret_ecrit` (nouveau) | cas sain : `principales_du_run` rend les deux sondes de [SF], dans l'ordre ; artefacts : `principales` absente, `enjeux` absente, `enjeux` = `None`, `tromperie` = 3 : `GardeArret` (type exact) au motif écrit, fonction pure ; lancement réel (dépôt jouet, [SF] sans `principales.enjeux` après la garde 6) : arrêt, rien d'écrit |

Recalcul hors du module (`ecarts_au_recalcul`, CV2-03), en plus de E_sf, D, E0, M, M7, E_-f et M8 (bornes) : comptes propres
de M3 pour `R_sf` et pour chaque `R_f` ; M5 : tâches de T_sf, classement et libellé de D, classements de E0, part
(état, valeur, intervalle sur les tirages non dégénérés, nombre de tirages, dégénérés, mention « instable ») ; M6 :
classements de M, tâches où d_∅ > 0 et > log10 3, quantiles de d_∅ et de d_sf, nombre de tâches de T_sf ; classements de
E_sf, E_-f et M7, nombre de tâches sans forme ; M8 : classement, nombre de tâches, actions lisibles avec la forme et sans
forme ; M9 : chaque colonne de chaque ligne (lisibles comptés sur la table, pas sur les listes du module) ; M10 :
demi-largeur, `A_seuil`, `A_80`, distances basse et haute, `A_seuil` et `A_80` à la distance basse (z et z80 par
`statistics.NormalDist`, à la main) ; audit : phrase, consigne et ligne de la recommandation selon le déclencheur
(« sain », « b2 », « degenere » : faux, tout à `None` ; « trop_bas » : vrai).

## Campagne de mutants rejouée sur le module v3

Versions éprouvées : module `96727076…`, tests `d0c5eb07…` (celles qui sont rendues ; chaque lanceur vérifie
l'empreinte de sa base). Tous les lancements depuis la racine du dépôt, interpréteur de la consigne, `-B`,
`PYTHONDONTWRITEBYTECODE=1`, `-p no:cacheprovider`, `--basetemp` et `TMPDIR` sous `module-v3/tmp/` (supprimé), sous la
garde R1 v2b, trois mutants à la fois. Deux lots chacun : un premier lot (mutants nouveaux et mutants visés par la
session), puis le reste ; un mutant déjà fait n'est pas relancé ; les deux lots portent sur les mêmes versions.

### Mes mutants : contrôle des survivants porté sur le v3

`controle-survivants/controle_survivants_v3.py` : copie du script du v2, base v3, garde v2b, suite arrêtée au premier
échec (`-x`). Liste : les 107 mutants de la première campagne (`revue-mutants/mutants_revue.py`, lu comme texte ; F23
adapté comme au v2), N01 à N10 du brouillon 4 **sans N04** (son code n'existe plus : c'est la règle retirée par CV2-01 ;
son contraire est V3-01), et douze mutants nouveaux V3-01 à V3-12 (brouillon 5, CV2-01, CV2-03, CV2-10). Résultats :
`controle-survivants/resultats-survivants-v3.jsonl` ; journaux `journaux/controle-survivants-v3-lot1.log` (V3-01 à
V3-12, fini à 17:18 UTC) et `…-lot2.log` (le reste, de 17:33 à 17:58 UTC).

**128 mutants, 128 tués, 0 survivant, 0 refus R1, 0 erreur.**

| famille | lancés | tués | dont survivants de la campagne d'origine (tués / total) |
|---|---|---|---|
| A : réserve mal câblée | 9 | 9 | 5 / 5 |
| B : cible fausse | 4 | 4 | — |
| C : cas de B1 ou de B2 inversé, bornes | 11 | 11 | — |
| D : mention sans cible P3-P1 | 1 | 1 | — |
| E : verrou ouvert | 11 | 11 | 5 / 5 |
| F : garde retirée (F23 adapté) | 24 | 24 | 13 / 13 |
| G : seuil ou niveau changé | 16 | 16 | 6 / 6 |
| H : NaN remplacé par l'infini | 3 | 3 | 2 / 2 |
| I : clés et graines (R9) | 10 | 10 | 4 / 4 |
| J : méthode (restriction, M5 à M8) | 11 | 11 | 5 / 5 |
| K : audit de symétrie | 4 | 4 | 1 / 1 |
| L : lancement | 3 | 3 | — |
| N : règles du brouillon 4 (N01 à N10, sans N04) | 9 | 9 | — |
| V3 : brouillon 5, CV2-01, CV2-03, CV2-10 | 12 | 12 | — |
| **total** | **128** | **128** | 41 / 41 |

| mutant | règle mutée | état | premier test en échec |
|---|---|---|---|
| V3-01 | déclencheur 3 : part en échec (garde 15) rendue « non calculé » (changement 6 du v2 rétabli) | tué | `test_garde_15_degenerescences_de_la_part` |
| V3-02 | déclencheur 3 : part en échec rendue « faux » (déclencheur tu) | tué | `test_garde_15_degenerescences_de_la_part` |
| V3-03 | déclencheur 3 lu sur la valeur de la part calculée (0 si la part est en échec) | tué | `test_audit_part_hors_bornes_construit_et_sain` |
| V3-04 | [SF] sans `principales` : aucune garde (valeur absente passée telle quelle) | tué | `test_CV2_10_SF_sans_principales_arret_ecrit` |
| V3-05 | [SF] sans `principales` : exception nue (accès direct) | tué | `test_CV2_10_SF_sans_principales_arret_ecrit` |
| V3-06 | [SF] sans `principales` : motif sans garde ni clé nommée | tué | `test_CV2_10_SF_sans_principales_arret_ecrit` |
| V3-07 | [SF] : seule `principales.enjeux` contrôlée | tué | `test_CV2_10_SF_sans_principales_arret_ecrit` |
| V3-08 | [SF] : valeur non textuelle acceptée | tué | `test_CV2_10_SF_sans_principales_arret_ecrit` |
| V3-09 | M5 : nombre de tirages de la part = tous les tirages (dégénérés compris) | tué | `test_bords_de_la_garde_15_un_pour_cent` |
| V3-10 | M8 : actions lisibles « sans forme » comptées sans la seule forme f | tué | `test_bornes_recalculees_hors_du_module[sain-10000]` |
| V3-11 | M3 : comptes propres, « actions » = actions lisibles | tué | `test_restriction_retire_exactement_les_actions_a_forme` |
| V3-12 | M6 : quantiles de d_sf absents (None) quand T_sf n'est pas vide | tué | `test_bornes_recalculees_hors_du_module[sain-10000]` |

### Mutants du contre-lecteur : sa campagne rejouée sur le v3

`outils-revue/lanceur_v3.py` : copie de son lanceur (`4a402337…`) ; changent seulement la base (module et tests v3,
empreintes lues dans leurs compagnons), le fichier de résultats, les dossiers temporaires (un dossier de mutant tué est
effacé ; la fin du journal d'un survivant est gardée dans sa ligne), la garde (`garde_r1_v2b`). Sa liste
(`outils-revue/mutants_v2.py`, copie octet pour octet, `d9c038e6…`) et sa règle (suite **entière**, sans `-x`) sont
inchangées. Résultats : `outils-revue/resultats-mutants-v3.jsonl` ; journaux `journaux/campagne-revue-v3-lot1.log`
(les 18 visés : DESC-01 à DESC-14, V2-14, PHRASE-08, REGLE-01, REGLE-02 ; de 17:18 à 17:28 UTC) et `…-lot2.log` (les
212 autres ; de 17:58 à 19:50 UTC).

**230 mutants : 2 sans objet au v3, 228 lancés, 215 tués, 13 survivants ; 0 refus R1 ; 0 erreur.** Aucun mutant tué au
v2 ne survit au v3. Au v2 : 200 tués, 30 survivants.

| famille | mutants | sans objet au v3 (motif absent) | lancés | tués au v3 | survivants au v3 | au v2 : tués / survivants |
|---|---|---|---|---|---|---|
| V2 : règles changées entre v1 et v2 | 22 | 2 | 20 | 20 | 0 | 21 / 1 |
| PRE : précisions d'application 1 à 10 | 26 | 0 | 26 | 25 | 1 | 25 / 1 |
| G : gardes 1 à 15 | 75 | 0 | 75 | 67 | 8 | 66 / 9 |
| SEUIL : seuils, niveaux, tirages, graines | 47 | 0 | 47 | 45 | 2 | 45 / 2 |
| REGLE : autres règles écrites | 38 | 0 | 38 | 36 | 2 | 34 / 4 |
| DESC : descriptifs écrits | 14 | 0 | 14 | 14 | 0 | 2 / 12 |
| PHRASE : phrases de la table des critères | 8 | 0 | 8 | 8 | 0 | 7 / 1 |
| **total** | **230** | **2** | **228** | **215** | **13** | 200 / 30 |

Les mutants demandés par la session sont tous tués :

| mutant | tests en échec (suite entière) | fonctions de test |
|---|---|---|
| DESC-01 | 3 | `test_bornes_recalculees_hors_du_module`, `test_restriction_retire_exactement_les_actions_a_forme` |
| DESC-02 | 5 | les deux mêmes |
| DESC-03 | 2 | `test_bornes_recalculees_hors_du_module` |
| DESC-04, DESC-05 | 7 chacun | `test_bords_de_la_garde_15_un_pour_cent`, `test_bornes_recalculees_hors_du_module` |
| DESC-06 | 5 | `test_bornes_recalculees_hors_du_module`, `test_classements_et_libelles_du_seuil` (déjà tué au v2) |
| DESC-07, DESC-08, DESC-09, DESC-10 | 3, 9, 9, 3 | `test_M6_comptes_aux_bords_0_et_log10_3`, `test_bornes_recalculees_hors_du_module` |
| DESC-11, DESC-12, DESC-13, DESC-14 | 4, 8, 8, 8 | `test_bornes_recalculees_hors_du_module` |
| V2-14 | 8 | `test_audit_explication_trop_propre_construit_et_sain`, `test_audit_part_hors_bornes_construit_et_sain`, `test_bornes_recalculees_hors_du_module` |
| PHRASE-08 | 5 | `test_ligne_de_commande_de_bout_en_bout`, `test_autre_exception_dans_une_analyse_ecrite_dans_arret`, `test_garde_4_commit_du_manifeste_different_de_la_tete` |
| REGLE-01, REGLE-02 | 3 chacun | `test_bornes_recalculees_hors_du_module`, `test_restriction_retire_exactement_les_actions_a_forme` |

Sans objet au v3 : **V2-21** (« précision 2 retirée ») est exactement le changement 1 de ce module ; **V2-22** visait la
branche retirée. Leur contraire, la règle du v2 remise dans le v3, est tué (V3-01, V3-02, plus haut).

Les 13 survivants sont ceux du v2, moins G6-02 :
- **équivalents** selon le contre-lecteur (5) : PRE1-03, G1-02, G1-07, G9-03, REGLE-32 ;
- **bords et types de CV2-05** (8), séparés par des cas construits, sans effet sur le run réel selon le contre-lecteur ;
  non traités, la session ne les a pas demandés : G4-02, G9-01, G9-02, G13-02, G13-04, SEUIL-11, SEUIL-33, REGLE-30.

**Réserve (R4) : G6-02 est tué au v3, mais par effet de bord.** Il n'échoue qu'à `test_CV2_10_SF_sans_principales_arret_ecrit`,
qui injecte sa panne en remplaçant `exiger_garde_6` du lancement ; le mutant appelle le chargeur gelé directement, la
panne n'est donc pas injectée et l'arrêt attendu ne vient pas. Ce test n'éprouve pas la conversion des exceptions du
chargeur (le cas de CV2-05). Je le compte « tué », sans le compter comme couvert.

Comptés de la même façon sur les deux fichiers de résultats : le test qui tue le plus de mutants est
`test_bornes_recalculees_hors_du_module` (59 mutants au v3, 25 au v2) ; tués par un seul test (identifiant paramétré
compris) : 108 au v3, 123 au v2. Durée moyenne par mutant : 96 s (suite entière).

## Durée mesurée (CV2-04)

Outil : `mesure-duree/mesure_duree_v3.py` (`545d533433834060edd80ea34e0a28c73cdf4f059e548e7ff310ecec5b0dcdb2`), lancé
une fois sous la garde R1 v2b (0 refus ; 65 ouvertures tracées, toutes dans le dépôt jouet ; `journaux/r1-mesure-duree.jsonl`).
Dépôt git jouet de taille réelle, construit sous `module-v3/tmp/` puis supprimé : 60 tâches, 4 conditions, 10 pas, 600
actions par condition, 430 sondes (2 principales, 214 de plancher chacune), **les cinq formes présentes** (`PROBAS_SAIN` :
chaque `E_-f` et chaque écart de forme calculés, le cas le plus chargé) ; lecture décisive par le code gelé ; module v3 aux
constantes du jouet ; texte scellé. Quatre passages ; dans chacun : la vraie commande dans un processus séparé
(10 000 tirages ; sortie scellée vérifiée : 13 contrôles écrits, 9 lus, 4 sans objet), un processus qui ne fait
qu'importer le module (durée murale, et imports mesurés dans ce processus en trois parts), un processus vide, la fonction
pure seule. Mémoire : `ru_maxrss` du processus de la commande, rendu par `os.wait4`, en Kio.

Mesures brutes : **`module-v3/mesures-duree-v1.txt`** (sha256 `c16ace640bd273ce073c384292771da946d2d3ec1dfee1be07b47c69115191ba`, compagnon à côté).

| grandeur | quatre mesures |
|---|---|
| ligne de commande complète (murale) | 5,403 ; 5,464 ; 5,399 ; 5,672 s (processeur 5,69 à 5,96 s) |
| processus qui ne fait qu'importer (murale) | 4,310 ; 4,139 ; 4,384 ; 4,165 s |
| imports mesurés dans ce processus | 3,279 ; 3,224 ; 3,379 ; 3,223 s, dont `controle_ia.harnais.validation_reelle` 2,05 à 2,15 s (il importe `torch`, l. 53), numpy 0,14 à 0,15 s, reste du module 0,98 à 1,13 s |
| processus vide (`python -B -c pass`) | 0,017 à 0,018 s |
| fonction pure seule (10 000 tirages) | 0,515 ; 0,453 ; 0,483 ; 0,505 s |
| mémoire maximale | 699 668 à 699 980 Kio = 683,3 à 683,6 Mio = 716,5 à 716,8 Mo |
| charge de la machine (1 min) | 1,84 à 1,92 (machine partagée, 4 cœurs) |

L'écart entre le processus qui ne fait qu'importer (≈ 4,2 s) et ses imports (≈ 3,3 s) est hors des imports : démarrage
(0,02 s) et surtout sortie de l'interpréteur ; je ne l'ai pas décomposé plus. Ces mesures concordent avec celles du v2
(module v2 ; rédacteur : 5,33 à 6,49 s, sur un jouet sans `cout_multiplication` ni `cout_milliers_espace` ;
contre-lecteur : 5,10 à 6,26 s).

Phrase proposée pour `<<DUREE_MESUREE>>` (forme corrigée de CV2-04, chiffres de ce fichier seulement) :

> environ 5,5 s pour la ligne de commande complète (de 5,4 à 5,7 s sur quatre mesures ; processus séparé, dépôt jouet à
> taille réelle : 60 tâches, 4 conditions, 10 pas, 600 actions par condition, 430 sondes, les cinq formes présentes ;
> 10 000 tirages), dont 3,2 à 3,4 s d'imports (surtout la bibliothèque de calcul tensoriel, tirée par
> `harnais.validation_reelle` : 2,0 à 2,2 s) et 0,45 à 0,52 s pour la fonction pure ; mémoire maximale ≈ 683 Mio
> (≈ 717 Mo) ; mesures : `<chemin du fichier versé>/mesures-duree-v1.txt` (sha256 `c16ace640bd273ce073c384292771da946d2d3ec1dfee1be07b47c69115191ba`).

Le chemin est à remplacer par celui où la session versera le fichier ; l'empreinte ne change pas si le fichier est versé
tel quel. Les huit mesures du v2 (deux mesureurs) peuvent être citées en plus, avec leurs fichiers
(`module-v2/mesure-duree/mesure-duree-v2.json`, `f035bb49…` ; `revue-v2/journaux/mesure-duree-revue.json`, `804305a8…`),
mais elles portent sur le module v2.

## R1 et intégrité

- Tables synthétiques seulement. Rien lu sous `donnees/`, `diag/`, `runs/`, `traces/` du dépôt ; ni
  `prereg/P3-consignes-v1.md`, ni un fichier `textes-actions-*` du dépôt ; aucune grandeur de B1 ni de B2 calculée sur le
  réel.
- Garde R1 : `outils-revue/garde_r1_v2b.py`, copie de celle du contre-lecteur (CV2-11 : sans les faux positifs de
  `shutil.rmtree`). Épreuve rejouée sur la copie (`outils-revue/test_garde_r1_v2b.py`, 14 tests, `journaux/pytest-epreuve-garde-v2b.log`) :
  14 passed, deux passages (le premier dans une série interrompue, voir plus bas), 17 refus attendus chacun, 34 au total
  dans `journaux/r1-epreuve-garde-v2b.jsonl`, tous sur des chemins `__garde_r1_inexistant__` qui n'existent pas. Puis : suite, mesure de durée, chaque
  lancement des deux campagnes : 0 refus partout (suite : 556 ouvertures tracées ; mesure : 65 ; mes 128 lancements et les 228 du contre-lecteur : champ `refus_R1` à 0 sur chaque ligne de résultats).
- Interruption : une première série « épreuve, suite, suite sous la garde » a été lancée avant le dernier changement des
  tests (ajout au test des 1 % de dégénérés) ; la suite était passée (121 passed), la suite sous la garde a été arrêtée
  par son PID (R10) ; journaux rangés dans `journaux/essais-avant-gel/`. Tous les résultats rendus portent sur les
  versions gelées (module `96727076…`, tests `d0c5eb07…`).
- Dépôt de travail : `git status --porcelain` vide au début, avant la suite et à la fin ; aucun `__pycache__` ni `.pyc`
  créé (lancements `-B`, `PYTHONDONTWRITEBYTECODE=1`, `-p no:cacheprovider`). Dossier de travail hors de `module-v3/` :
  1 815 fichiers, liste d'empreintes identique au début (16:58) et à la fin (19:52) (`journaux/empreintes-dossier-avant.txt`, `…-apres.txt`, `a6769a36a8cd1bfc6d572a4124c13288e05720dabf0fdb80455111dad13d79aa` toutes deux) ; `module-v2/` inchangé. Tête du dépôt : `3448971` au début, `0e5060a` à la fin (commits de la session) ; `src/` et `tests/` identiques entre les deux (`git diff --stat` vide) ; aucun `.pyc` nouveau sous `src/`, `tests/`, `docs/procedures/`.

## Constats non traités ici

CV2-05 à CV2-09 et CV2-11 (information) : non demandés par la session ; le module et les tests n'en tiennent pas compte,
sauf CV2-11 (garde v2b reprise). CV2-10, suggestion d'une empreinte des colonnes du run source revérifiée à la fin (comme
pour [L]) : non faite (ni demandée, ni au brouillon 5).

## Fichiers rendus

Chaque fichier de `module-v3/` a son compagnon `<nom>.sha256` (« <empreinte>  <nom> », vérifiable par `sha256sum -c`
depuis son dossier). Celui de ces notes est `NOTES-MODULE-v3.md.sha256`.

| fichier (sous `module-v3/`) | rôle | sha256 |
|---|---|---|
| `audit_verdict_p3_v1.py` | **module v3** | `967270761c92ce3875695b8e5da5a985295c963b324dd120a31d09db663f132d` |
| `test_audit_verdict_p3_v1.py` | **tests v3 (121)** | `d0c5eb07da17a1bf27fc38905edd648e4653ba9f3652076560ee4c4c3ba83b28` |
| `mesures-duree-v1.txt` | **mesures brutes de durée (CV2-04)** | `c16ace640bd273ce073c384292771da946d2d3ec1dfee1be07b47c69115191ba` |
| `mesure-duree/mesure_duree_v3.py` | outil de mesure | `545d533433834060edd80ea34e0a28c73cdf4f059e548e7ff310ecec5b0dcdb2` |
| `controle-survivants/controle_survivants_v3.py` | mes mutants, portés sur le v3 | `90e582f7af6e8b7e218449684d7491af32a226988def0a24e0dacde8f152768b` |
| `controle-survivants/resultats-survivants-v3.jsonl` | 128 résultats | `c54035f4e82399ac950cd641299706832068b85360295eb1f008bbadf711d123` |
| `outils-revue/lanceur_v3.py` | lanceur du contre-lecteur, copie adaptée | `a1f318daf8412b082ac2bc64fd622402e95a81639c8219cceb6ad7dadf4a6814` |
| `outils-revue/mutants_v2.py` | liste du contre-lecteur (copie octet pour octet) | `d9c038e67b5e2f8cd7016c089faf02d0fd8ab86fee527d34e31304e1cfadf03c` |
| `outils-revue/garde_r1_v2b.py` | garde R1 du contre-lecteur (copie octet pour octet) | `022cfd55eac2298b9f00b371d5141d37a98561662d2f424255983199160bac4f` |
| `outils-revue/test_garde_r1_v2b.py` | épreuve de la garde (copie octet pour octet) | `21dc8e56c0111decc26c43edca1837d2841946e49c70f0f7b058790df986d7af` |
| `outils-revue/resultats-mutants-v3.jsonl` | 230 résultats | `21b117a5308015116e6aadeb6c0f84d6525f8e2460e6429325ef8e38cf353079` |
| `journaux/pytest-suite-v3.log` | suite, commande de la consigne | `ab96e5ff95ee2fcc1a3c4578bff5d2da41b2dec3147a5aee21b17698d265e293` |
| `journaux/pytest-suite-v3-garde-r1.log` | suite sous la garde R1 | `9a6012879fd511360702203b5dfe00b43d3f7e290e48b561b82acc5fa35ea7df` |
| `journaux/r1-suite-v3.jsonl` | journal de la garde (suite) | `05f7fbb1c7cb26ffc0ba81832d8d6c57a67ecbabbcdbddc4f09c4f195b924023` |
| `journaux/pytest-epreuve-garde-v2b.log` | épreuve de la garde | `354a1afe702562e2b708bdfe6dcd5741af8b10112fb7da8d114ff3aff0a6847f` |
| `journaux/r1-epreuve-garde-v2b.jsonl` | journal de la garde (épreuve, deux passages) | `e2d444cd25be94d446e3792d52a48d8cbfc1f80d5b93e19c13e27b9210d115a0` |
| `journaux/mesure-duree-v3.log` | sortie de la mesure | `c4c18fa1777bfffff7c24d71fc70dc261ba7f62c4197f178903b26aeed002e18` |
| `journaux/r1-mesure-duree.jsonl` | journal de la garde (mesure) | `067a1a7b201e029039909f9d3d6fda04e0c0b1b8fa8df414fec6555389d81281` |
| `journaux/controle-survivants-v3-lot1.log` | mes mutants, lot 1 | `6a31bfdaaf7f9599a02b6db81f3f0f5143bece5e0e30175de7c5e5fab0a7d02d` |
| `journaux/controle-survivants-v3-lot2.log` | mes mutants, lot 2 | `5b138548863cd23e870efa4f56ae41425fac6d7739ea20e097cbeb60cd4f9011` |
| `journaux/campagne-revue-v3-lot1.log` | contre-lecteur, lot 1 | `80dc0115acee5ad69cc2a183ad9bc1ea3f5d6d9aba00d5067a42035c3402b60d` |
| `journaux/campagne-revue-v3-lot2.log` | contre-lecteur, lot 2 | `1ddf7ee995ec166acd88d187f3377f5d59f33362dc5ed29ff21aec855a426d23` |
| `journaux/essais-avant-gel/pytest-suite-v3-essai1.log` | essai avant gel : suite, tests `4faa2458…` (avant l'ajout au test des 1 %) | `4a1faec26a9608a3a2e2bd7c54aaf1ecf0d8e19934d572c5e9fe6422dd7b5443` |
| `journaux/essais-avant-gel/pytest-suite-v3-essai2.log` | essai avant gel : même suite, second passage | `89d3209e8e790a538589250e67c71ac33ce826ad254fcfb93631d33bad32794a` |
| `journaux/essais-avant-gel/pytest-suite-v3-garde-r1-essai2-interrompu.log` | essai avant gel : suite sous la garde, arrêtée par son PID (R10) | `cdb4ee2aea69cc6a83331bbe96dc2caa9a299d21329efb0336fc02a82e1839a8` |
| `journaux/git-head-avant.txt` | tête du dépôt au début | `4764e3fb965d1e9f9a0c58fc4143a719ffcaa2bc0893a8b5797317bd01f197e9` |
| `journaux/git-head-apres.txt` | tête du dépôt à la fin | `907f30e1fe65ac90b45cab702953e426af1e47ac20bb67ac6628da63699c0178` |
| `journaux/empreintes-dossier-avant.txt` | dossier de travail hors de `module-v3/`, début | `a6769a36a8cd1bfc6d572a4124c13288e05720dabf0fdb80455111dad13d79aa` |
| `journaux/empreintes-dossier-apres.txt` | même liste, fin | `a6769a36a8cd1bfc6d572a4124c13288e05720dabf0fdb80455111dad13d79aa` |
| `journaux/git-status-avant.txt`, `…-avant-suite.txt`, `…-apres.txt` | état git (vides) | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
