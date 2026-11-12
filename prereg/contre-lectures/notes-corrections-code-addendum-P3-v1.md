# Module de l'addendum de P3 — corrections CB1, CB3 (02, 04), CB2, brouillon 6 et retouche VF2 : notes

Dossier : `addendum-p3/final-b4/` (seul dossier écrit). Livrables : `complements_p3_v1.py` et `test_complements_p3_v1.py`.
`essais/` est hors livrable (relevé des lignes, lanceur et journaux des mutants, journaux de pytest) : ne pas le verser.
Le dépôt de travail n'a pas été touché (aucune écriture, aucun commit).

- Point de départ (lecture seule) : `final/complements_p3_v1.py` (sha256 `daf954594456f8c268ebbf48b14326a183941c00c4cddb205b2e3382a875f4fa`),
  `final/test_complements_p3_v1.py` (sha256 `01b5faeaf1fe5ea38624b872948d46d5310bc67b6df3277ea1515e73fc057abc`), 117 tests.
- Texte qui fait foi : `P3-addendum-lecture-complementaire-v1-brouillon6.md` dans son état final (sha256
  `77bc2fe0d62aac4384712ee77c28fa6b77a30d47092b3d327120186d60d24e5c`, audit de symétrie, gardes 15 et 16 et précision 18
  relus) ; état précédent lu en entier (sha256 `503daf1224681735c0f67d77ae1d9253e2447a92d16c3e785d5ac4f8868a591e`) ; le
  travail CB1 a commencé sur le brouillon 4 (sha256 `05e78c1d12762ade8a9f28a6382a12aed705da98304f81a58328023bfb6d5119`).
- Rapports traités : `rapports/contre-lecture-code-b3-1.md` (CB1-01 à CB1-08, sha256
  `89e1f02b41d62ee7388955d0c23bfbb8b54f2f9e2ea3fa299758f17c0b58e57f`) ; `rapports/contre-lecture-code-b3-3.md` (CB3-02,
  CB3-04 ; sha256 `8aa42a89beb16079da2bbc4d3fc903ada726600a4dcc9be36e3dac5927501605`) ; preuves de la revue CB2
  (`rapports/revue-b3-2/` : 51 mutants, 8 essais ; rapport inachevé) ; brouillon 6 (garde 13, garde 16, précisions 16 à
  18) ; vérification finale VF2 (`verification-finale/verification-code-final-addendum-P3-v1-mutants.md`, sha256
  `aab50bf0230cd923f8c0c3ee9a5f91c5f6bb6805e28ce79f2c9138abda5ecc7b` ; substitutions de `verification-finale/mutants/lanceur_vf2.py`,
  sha256 `76aa1ea5760427990193e06bbf7e955b8bbe977d4c63093da1f6929c409dcb52`) : tests seuls retouchés (§ 3 ter).

**Verdict : corrections faites, ronde finale et retouche VF2 comprises. 165 tests passent ; les 51 mutants de la revue CB2
et les 8 survivants de VF2 sont tués ; le module n'a pas changé depuis la ronde finale ; aucune garde du module n'est
laissée sans test ; aucun cache dans le dossier.**

| | |
|---|---|
| module `complements_p3_v1.py` | sha256 `2b16179d4451c3f10c0c1053687d76f68c9b32b43f2b460463d844ab45c15996` (2 289 lignes) |
| tests `test_complements_p3_v1.py` | sha256 `7387910d3b5851026f316e89df3f1b84e4a39758e9d73da52cea166f5223e0a3` (3 283 lignes) |
| nombre de tests | **165** (écrit en tête du fichier) |
| sortie finale de pytest | `165 passed in 1049.77s (0:17:29)` |
| mutants CB2 | 51 tués sur 51 (§ 5) |
| mutants survivants de VF2 | 8 tués sur 8, par les tests seuls (§ 3 ter) |
| gardes jamais exécutées | 0 sur 107 à l'état à 164 tests ; les 2 gardes de la ronde finale ont chacune un cas sain et un artefact (§ 6) |

À reporter dans le préenregistrement : `<<EMPREINTE_MODULE>>` = `2b16179d4451c3f10c0c1053687d76f68c9b32b43f2b460463d844ab45c15996`,
`<<EMPREINTE_TESTS>>` = `7387910d3b5851026f316e89df3f1b84e4a39758e9d73da52cea166f5223e0a3`, `<<NOMBRE_TESTS>>` = 165 (après
versement sous `docs/procedures/P3-addendum-v1/`, fichiers inchangés).

## 1. CB1 — texte face au code

**CB1-01 (majeur) — textes coupés à U+2028, U+2029, U+0085.** `charger_textes` (l. 2164-2183) : le fichier est découpé
sur l'octet `\n` seulement (en UTF-8, 0x0A n'est que le saut de ligne : même découpe que `split("\n")`), chaque ligne est
décodée à part, les lignes vides (exactement vides) sont ignorées ; une ligne illisible (UTF-8 ou JSON) donne
`GardeArret("garde 4 : fichier … : ligne N illisible (TypeErreur)")`, numéro de ligne physique à partir de 1, sans aucun
texte. Le brouillon 6 l'écrit (garde 14). Tests : `test_garde_4_textes_lus_sur_les_seuls_sauts_de_ligne` (l. 1035 ; sain :
textes avec les trois séparateurs, écrits comme `run._ecrire_textes`, relus égaux, `splitlines` aurait coupé, garde 5
passée, lignes vides ignorées ; artefacts : ligne tronquée, octets non UTF-8, empreinte autre) ;
`test_garde_4_textes_de_bout_en_bout` (l. 2920 ; dépôt jetable : run source scellé aux trois séparateurs, relu par
`lecture.charger_source` puis `charger_textes`, gardes 5 à 8 passées ; run source scellé à ligne tronquée, lecture
décisive faite : arrêt à la garde 4 avant le manifeste, rien sous `runs/` ni `diag/`).

**CB1-02 (majeur) — recommandation au verdict.** `synthese` (l. 1793-1866) : deux listes par conclusion, classées par le
contrôle lui-même (`controle_contraire is True` → contraire ; « non lu » → non contrôlée ; réserve générale de la garde
11 → non contrôlée). Phrases : contraire → « `<cible>` : établie au sens de la lecture décisive, non robuste aux contrôles
de l'addendum (réserves : …) », suivie, pour `reserve_A7_forme_du_cout` et `reserve_A7_forme_quasi_totale`, de leur lecture
gelée, à la lettre des critères (« séparation non établie hors de cette forme du coût » ; « séparation confondue avec cette
forme du coût, non séparable par restriction »), avec le test qui la porte entre parenthèses ; non contrôlée →
« `<cible>` : non contrôlée par l'addendum (réserves : …) ; la conclusion reste établie ; le verdict cite qu'elle n'a pas
été contrôlée » (plan, point 6, et critères gelés, à la lettre ; point 5 de la consigne CB2). Constantes `LECTURE_NON_LUE`,
`LECTURES_A7`, `RESERVE_GENERALE` (l. 114-121). Tests : `test_recommandation_reserve_non_lue_seule_jamais_non_robuste`
(l. 1619 : entrées fabriquées, réserve générale seule, réserves de forme, propriété sur six scénarios réels),
`test_recommandation_sur_donnees_non_lue_et_forme_du_cout` (l. 1804 : les deux essais CB2 retournés),
`test_audit_symetrie_toutes_les_reserves_possibles_declenchees` (mis à jour, l. 1568), `test_garde_11_…` (ajouts),
`test_A7_artefact_forme_du_cout`, `test_A7_artefact_forme_quasi_totale` (ajouts).

**CB1-03 (mineur) — audit de symétrie.** `synthese` (l. 1828-1850) : « toutes déclenchées » compte les seuls contrôles
contraires (`controle_contraire is True`) ; `controles_non_lus` est rapporté à côté ; « aucune » se lit à la lettre
(aucun contrôle contraire, quel que soit le nombre de « non lu » : décision de la ronde finale, § 3 bis) ; le texte des
critères écrit dans la sortie le dit. Le brouillon 6 l'écrit (Critères). Tests :
`test_audit_symetrie_tout_non_lu_ne_declenche_pas_toutes` (l. 1673 : fabriqué, avec et sans audit R4, puis sur données,
toutes les analyses qui contrôlent en échec) ; `test_audit_symetrie_toutes_les_reserves_possibles_declenchees` (mis à
jour).

**CB1-04 (mineur) — arrêts ajoutés.** (e) seul change dans le code (décision de la session), puis selon la garde 16 du
brouillon 6 : voir § 3. (a) à (d) et (f) à (i) restent ; le brouillon 6 les écrit (gardes 12 à 15, précision 2).

**CB1-05 (mineur) — silences comblés.** Aucun changement de code (décision de la session ; le brouillon 6 les écrit en
précisions).

**CB1-06 (mineur) — gardes jamais éprouvées (R5).** Les 33 gardes du relevé ont chacune un cas sain et un artefact :
- table `GARDES_R5` et `test_garde_jamais_eprouvee_cas_sain_et_artefact` (27 cas paramétrés ; 25 pour ces lignes) : l. 246,
  305, 308, 317, 361, 407, 446, 449, 456, 461, 473, 476, 480, 522, 529, 531, 539, 541, 598, 699, 711, 916, 1195, 1547, 1780
  du module de départ (la l. 1780, verrou, se lit désormais sur la liste recalculée) ;
- garde 1 (l. 1891, 1898, 1903 de départ) : `test_garde_1_entropie_empreintes_et_tests_cites` (l. 2892) ;
- garde 2 (l. 1954, 1961) : ajouts à `test_garde_2_lecture_decisive_rattachement_et_unicite` (l. 2982) ;
- garde 3 (l. 1971, `_git`) : ajouts à `test_garde_3_anteriorite_et_histoire_coupee` (l. 3049 : hors d'un dépôt, dépôt
  sans commit) ;
- l. 1926 (`_manifestes`, hors de forme) : `test_garde_9_premier_passage` (l. 3088) ;
- l. 2006 (empreinte des textes) : `test_garde_4_textes_lus_sur_les_seuls_sauts_de_ligne`.
Les branches mortes en pratique (l. 699, 711, 2006 de départ) sont gardées comme défenses et éprouvées par appel direct ou
par un `conditions` fictif (`_cd_fictif`). Relevé des lignes après corrections : § 6.

**CB1-07 (information) — caches.** Aucun `__pycache__` ni `.pytest_cache` dans `final-b4/` : tous les lancements portent
`PYTHONDONTWRITEBYTECODE=1` et `-p no:cacheprovider` (vérifié par `find`, § 6).

**CB1-08 (information).** Rien à faire.

## 2. CB3 — pannes

**CB3-01** : même défaut que CB1-01, traité.

**CB3-02 — garde 10 et localisation avant le manifeste.** `executer` (l. 2218-2222) : après la cohérence (garde 12),
`familles_attention(d)` (garde 10) et `localisation(d, k)` pour chaque sonde principale (garde 13), puis la garde 9, puis
le manifeste : un arrêt n'écrit rien et ne consomme pas le seul passage. Le brouillon 6 l'écrit (plan, point 3 : gardes
1 à 10 et 12 à 16 avant le manifeste). Test : `test_garde_10_et_localisation_avant_le_manifeste_aucune_sortie` (l. 2944 :
run source scellé dont `sondes-figees.json` dit « max » pour la sonde à attention, lecture décisive faite : arrêt de la
garde 10 par `executer`, rien d'écrit, passage non consommé ; localisation de la lecture décalée de 1e-6 : arrêt, rien
d'écrit ; cas sain : les deux gardes passent sur le run du gabarit).

**CB3-04 — graines clé par clé.** `exiger_graines` (l. 1912-1927) : après l'entropie, chaque graine doit égaler
`manifeste.graines(cles_addendum(p), ENTROPIE_P3)[k]` (entropie, clé de dérivation, état de contrôle) ; sinon
`GardeArret`. Test : `test_graines_exactement_celles_de_leurs_cles` (l. 877 : sain, aussi relues d'un JSON ; deux clés
échangées ; état de contrôle altéré ; arrêt par `exiger_graines` et par `analyser_addendum`, avant toute analyse).

CB3-03 (mémoire), CB3-05 (dépôt superficiel), CB3-06 (cache) : sans code (texte, lancement, versement).

## 3. CB2 — verrou et preuves ; brouillon 6

**CB2-06, précision 16 — verrou de fin recalculé.** `exiger_verrou(sortie, lecture, etablies, principales,
issue_canonique)` (l. 1868) : `conclusions_etablies` recalculée depuis la lecture décisive (`lire_la_lecture`, garde 7
comprise, puis table du point 5) ; elle doit égaler la liste dont les analyses se sont servies et celle de la sortie ;
chaque réserve et chaque contrôle lu sont vérifiés sur la liste recalculée ; clés interdites cherchées dans toute la
sortie. Appel : `analyser_addendum` (l. 1974). Tests : `test_verrou_de_fin_sur_les_conclusions_recalculees` (l. 1419 :
sain ; liste des analyses allongée ; liste de la sortie allongée ; contrôle lu sur une conclusion non établie ; réserve
sans contrôle lu sur une conclusion non établie ; analyse qui allonge la liste partagée pendant l'addendum, essai CB2
retourné) ; `test_garde_du_verrou_sain_et_artefacts` (mis à jour) ; entrée « verrou » de `GARDES_R5`.

**CB2-09, précision 17 — une entrée en échec garde ses réserves.** `_executer_entree` (l. 1744-1770) : sur une
`GardeArret` hors d'un calcul, les contrôles déjà faits sont gardés tels quels (réserves contraires comprises), le
descriptif calculé aussi (sauf s'il porte la valeur non finie qui a causé l'échec : il est alors retiré, motif écrit),
puis chaque cible visée reçoit un contrôle « non lu » pour les contrôles non faits. Test :
`test_entree_en_echec_garde_la_reserve_contraire_deja_calculee` (l. 1778, essai CB2 retourné : la réserve
`reserve_A1_plancher_conjoint` et son motif restent, la synthèse la dit « non robuste »).
`test_valeur_non_finie_dans_la_sortie_garde_avec_son_chemin` tient toujours.

**CB2-11, précision 18 — drapeaux bruts recoupés (garde 7).** `exiger_drapeaux_recoupes` (l. 522-549), appelée à la fin
de `lire_la_lecture` (l. 454-502), et `_contraste_selon_les_etats` (l. 505-519) : là où la table du point 5 les consulte
(`conforme` de p si `P3-P3/<p>` est établie ; `T<k>.etabli` si `P3-P4/<p>` l'est), les drapeaux bruts sont recoupés avec les
règles de `lecture.lire` : `conforme` ⇔ saboteur contre témoin « au-dessus » et témoin contre honnête « non au-dessus » ;
T3 ⇔ mention contre honnête « non au-dessus » et saboteur contre mention « au-dessus » ; T1, T4 ⇔ calculable et borne basse
au-dessus du quantile du plancher ; T2 ⇔ calculable et borne basse au-dessus de 0. Un désaccord arrête. Les drapeaux non
consultés ne sont pas lus : le test exigé par le texte (« organisme non établi » aux drapeaux bruts « conformes » :
`conclusions_etablies` vide) tient tel quel. Test : `test_garde_7_drapeaux_bruts_recoupes_avec_les_etats` (l. 1745 : sain ;
`conforme` vrai contre les états, essai CB2 retourné ; `conforme` faux contre les états ; T2 établi avec une borne ≤ 0 ;
T3 non établi contre les états).

**Recommandation (point 5 de la consigne CB2).** Voir CB1-02 : lecture gelée des réserves « non lue » et de
`reserve_A7_forme_du_cout`, à la lettre ; les deux essais CB2 qui prouvaient le défaut sont retournés en test.

**Brouillon 6 (a) — garde 13 à 1e-9 près.** `localisation` et `_egaux_a_la_tolerance` (l. 678-721,
`TOLERANCE_LOCALISATION`, l. 99) : lignes égales, scores du pré-coût et du coût égaux à 1e-9 près (NaN au même rang
égaux). Test : `test_garde_localisation_egale_a_celle_de_la_lecture` (l. 1161 : écarts de 1e-12 et 5e-10 acceptés ; 1e-6
sur le pré-coût ou le coût, lignes décalées : arrêt ; arrêt par `analyser_addendum`).

**Brouillon 6 (b) — garde 16, critère lexical.** `_pourrait_concerner` et `_manifestes` (l. 2048-2089,
`CHAINES_MANIFESTE`, `TAILLE_MIN_MANIFESTE`, l. 102-103) : un manifeste illisible ou hors de forme arrête les gardes 2 et 9
si ses octets bruts, décodés avec remplacement, contiennent le nom du run source, « P3-addendum-lecture-complementaire-v1 »,
« complements_p3_v1 » ou « premier_test_ia.lecture », ou s'il fait moins de 64 octets ; sinon il est écarté, compté et
rapporté (`manifestes_illisibles_ecartes` dans la sortie, `garde_2` et `garde_9`, nombre et liste ; comptes imprimés par la
commande). Le nom du dossier ne compte plus (critère de la session remplacé par celui du texte). Tests :
`test_garde_9_premier_passage` (l. 3088 : six manifestes écartés, frontière à 64 octets comprise ; chaque chaîne, 10 et 63
octets, hors de forme avec une chaîne, octets non UTF-8 avec une chaîne : arrêt ; fichier illisible par le système : zéro
octet, arrêt), `test_garde_2_…` (écarté puis arrêt), `test_ligne_de_commande_de_bout_en_bout` (écarté et rapporté dans la
sortie scellée), `test_ligne_de_commande_reelle_dans_un_processus` (comptes imprimés).

**Brouillon 6 (c) — précision 16 étendue.** Faite par CB2-06 ci-dessus ; V1, V2, V3 sont tués (§ 5).

**Refactorisation sans changement de règle.** `preparer_donnees` (l. 1978) : la préparation de `analyser_addendum`
(données, graines, gardes 5 à 8, 10, 12, 13, table, relecture) en une fonction, pour éprouver chaque analyse seule
(`_D(nom)` dans les tests).

## 3 bis. Ronde finale : décisions de la session sur les six points ouverts

1. **Garde 15, paramètres de tirage du texte.** `PARAMETRES_DU_TEXTE` et `exiger_parametres_du_texte` (l. 2250-2262) :
   `TIRAGES_AIRE` 2 000, `TIRAGES_COUT` 10 000, `REPLIQUES` 50, `NIVEAU` 0,95, `NIVEAU_BONFERRONI` 0,975,
   `QUANTILE_PLANCHER` 0,95, `MAX_DEGENERES` 0,01, `TRANCHES` 5 (quintiles) ; un écart arrête (« garde 15 : paramètre de
   tirage … ≠ … (texte) »). Appelée par `_main` (l. 2273) avant `executer`, donc avant toute lecture ; les tests réduisent
   les tirages par l'appel direct. Test : `test_garde_15_parametres_de_tirage_du_texte_par_la_ligne_de_commande` (l. 3166 :
   valeurs du texte écrites à la main ; tirages réduits des tests : arrêt ; valeurs du texte : passe ; sept écarts, un par
   paramètre : arrêt ; `_main` lancé dans un dossier vide arrête à la garde 15, rien d'écrit). La ligne de commande réelle
   (processus séparé, `test_ligne_de_commande_reelle_dans_un_processus`) passe la garde avec les vraies valeurs.
2. **Audit de symétrie, « aucune » à la lettre.** `synthese` (l. 1834) : `aucune` = aucun contrôle contraire, quel que soit
   le nombre de « non lu », avec au moins trois conclusions établies et l'audit R4 de la lecture déclenché ; motif et
   critères écrits dans la sortie le disent ; `controles_non_lus` reste rapporté. Test :
   `test_audit_symetrie_tout_non_lu_ne_declenche_pas_toutes` (l. 1673, renommé : tout « non lu » ne déclenche jamais
   « toutes » ; avec audit R4, « aucune » se déclenche, sans lui non ; deux conclusions seulement : non ; sur données,
   toutes les analyses en échec, sans puis avec audit R4).
3. **Précision 18, `P3-P1.etablie` recoupé.** `exiger_drapeaux_recoupes` (l. 522-549) : toujours consulté par la table,
   donc toujours recoupé : établie si et seulement si calculable et borne basse > 0 (`lecture.py` l. 242) ; l'entrée brute
   est gardée par la garde 7 (`P3-P1_entree`). Test : `test_garde_7_drapeaux_bruts_recoupes_avec_les_etats` (quatre cas
   ajoutés : établie avec borne −0,01, avec borne 0, non calculable ; non établie alors que calculable et borne > 0 :
   arrêt). Les lectures « où rien n'est établi » des tests rendent l'effet non calculable (`_p3_p1_non_etablie`), les
   nombres gardés ; `test_organisme_non_etabli_drapeaux_bruts_conformes_reserves_sans_objet` passe tel quel.
4. **Garde 16.** Choix retenu et écrit au texte : rien à changer.
5. **Dépôt complet.** Rien à faire.
6. **Numéros de garde dans les messages d'arrêt**, harmonisés avec le texte : mesures relues, « garde 14 » ; cohérence,
   « garde 12 » ; localisation, « garde 13 » ; graines (entropie, absentes, autres que celles de leurs clés), nom du run,
   chemin du préenregistrement de la commande, chemin du module, paramètres de tirage (`verifier_parametres_tirage` et
   `exiger_parametres_du_texte`), « garde 15 ». Les tests attendent désormais ces numéros (motifs renforcés).

## 3 ter. Retouche VF2 : tests seuls, module inchangé

Rapport : `verification-finale/verification-code-final-addendum-P3-v1-mutants.md` (VF2-01, 02, 04, 05, 06 : 8 mutants
survivaient aux 165 tests). Le module n'a pas changé : sha256 `2b16179d4451c3f10c0c1053687d76f68c9b32b43f2b460463d844ab45c15996`,
vérifiée avant la retouche, au lancement de la suite (`essais/empreintes-au-lancement-vf2.txt`) et après. Seul le fichier
de tests change : six tests étendus, aucun ajouté ni retiré, aucune assertion affaiblie ; toujours 165 tests.
Remplacements exacts, chacun présent une seule fois dans le fichier d'avant (`essais/retouche_vf2.py`).

1. **VF2-01 (M09, M10, M12).** `test_garde_7_drapeaux_bruts_recoupes_avec_les_etats` (l. 1766) : trois artefacts de
   plus, par `_lecture_recalculee` (états et issue recalculés par le code gelé) : témoin contre honnête « au-dessus »
   (« P3-P4/…/conforme vaut True alors que les états de la lecture disent False ») ; saboteur contre mention « non
   au-dessus » (« intention/…/T3/etabli vaut True alors que la lecture dit False ») ; borne basse de T2 égale à 0
   (« intention/…/T2/etabli vaut True alors que la lecture dit False ») : arrêt (garde 7), motif attendu.
2. **VF2-02 (M11).** `test_organisme_non_etabli_drapeaux_bruts_conformes_reserves_sans_objet` (l. 1497) : seconde
   partie. `conforme` est posé à la négation de la valeur lue, elle-même vérifiée égale au verdict des états (saboteur
   contre témoin « au-dessus » et témoin contre honnête « non au-dessus ») ; issue recalculée, « organisme non établi » ;
   addendum complet : aucun arrêt, conclusions vides, « réserves sans objet ».
3. **VF2-04 (M19).** `test_garde_4_textes_lus_sur_les_seuls_sauts_de_ligne` (l. 1035) : ligne 3 faite de trois espaces :
   arrêt, « garde 4 : fichier espaces.jsonl : ligne 3 illisible (JSONDecodeError) », aucun texte dans le motif.
4. **VF2-05 (M13, M14).** `test_garde_coherence_de_la_lecture_avec_le_run_source` (l. 1151) : cas sain, écart de 1e-12
   sur une aire : `exiger_coherence` passe (10 contrôles) ; artefact, écart de 1e-6 : arrêt (garde 12). Docstring
   ajoutée. `test_garde_localisation_egale_a_celle_de_la_lecture` (l. 1171) : artefact, écart de 2e-9 sur le pré-coût :
   arrêt (garde 13).
5. **VF2-06 (M24).** `test_forme_de_la_commande` (l. 3185) : « 20261020-130000-addendum-p3-bis » : arrêt (garde 15).

Preuves, sur copies mutées (`essais/mutants_vf2_b4.py`) : les substitutions sont lues dans `NEUFS` du lanceur de VF2 par
l'arbre syntaxique (empreinte du lanceur vérifiée, lanceur non exécuté) ; copie de base `essais/base-vf2/` (empreintes de
final-b4 vérifiées) ; motif présent une seule fois ; test tueur seul, par son identifiant exact, `-x`. Témoin, les six
tests sur la copie non mutée : `6 passed in 74.98s`. L'artefact qui tue est relevé par un second passage avec `-l`
(variables locales au point d'échec : `motif`, `cle` et `ecart`, `nom` et `ligne`, `run_add`). Pour M09 et M12, le motif
est aussi celui d'un artefact plus ancien de la boucle ; celui-ci arrête toujours sous le mutant (la règle mutée garde la
condition qu'il viole) ; l'échec vient donc de l'artefact neuf.

| mutant | règle mutée (lanceur de VF2) | test qui le tue | résultat sur la copie mutée |
|---|---|---|---|
| M09 | `conforme` recoupé sans « témoin contre honnête non au-dessus » | `test_garde_7_drapeaux_bruts_recoupes_avec_les_etats` | tué (1 failed, 25 s) : témoin contre honnête « au-dessus », DID NOT RAISE |
| M10 | T3 recoupé sans « saboteur contre mention au-dessus » | `test_garde_7_drapeaux_bruts_recoupes_avec_les_etats` | tué (1 failed, 24 s) : saboteur contre mention « non au-dessus », DID NOT RAISE |
| M11 | `conforme` recoupé même quand `P3-P3/<p>` n'est pas établie | `test_organisme_non_etabli_drapeaux_bruts_conformes_reserves_sans_objet` | tué (1 failed, 28 s) : l'addendum s'arrête (« garde 7 : P3-P4/tromperie-lineaire-c7/conforme vaut False alors que les états de la lecture disent True … ») |
| M12 | T1, T2, T4 recoupés avec borne basse ≥ seuil au lieu de > | `test_garde_7_drapeaux_bruts_recoupes_avec_les_etats` | tué (1 failed, 24 s) : borne basse de T2 = 0, DID NOT RAISE |
| M13 | garde 12 à 1e-3 près au lieu de 1e-9 | `test_garde_coherence_de_la_lecture_avec_le_run_source` | tué (1 failed, 33 s) : écart de 1e-6, DID NOT RAISE |
| M14 | garde 13 à 1e-7 près au lieu de 1e-9 | `test_garde_localisation_egale_a_celle_de_la_lecture` | tué (1 failed, 21 s) : écart de 2e-9 sur le pré-coût, DID NOT RAISE |
| M19 | ligne d'espaces ignorée au lieu d'un arrêt | `test_garde_4_textes_lus_sur_les_seuls_sauts_de_ligne` | tué (1 failed, 6 s) : ligne « espaces », DID NOT RAISE |
| M24 | nom du run d'addendum sans ancre de fin | `test_forme_de_la_commande` | tué (1 failed, 5 s) : « …-addendum-p3-bis », DID NOT RAISE |

Tués : 8 sur 8. Journaux : `essais/mutants-vf2-run.log`, `essais/mutants-vf2-resultats.jsonl`,
`essais/mutants-vf2-temoin.log`, `essais/mutants-vf2/<id>/pytest.log` ; passage avec `-l` :
`essais/mutants-vf2-locaux.log`, `essais/mutants-vf2/<id>-locaux/pytest.log`.

Les 51 mutants de la revue CB2 (§ 5) n'ont pas été relancés. Aucun de leurs tests tueurs n'est parmi les six tests
retouchés (comparaison des deux fichiers de tests : seuls ces six tests changent), et le module est le même : leurs
mises à mort tiennent telles quelles.

Hors de cette retouche, non demandés : VF2-03 (précision 17, texte) ; VF2-07 (information) ; VF2-09 (motif « garde 4 »
d'une ligne illisible, que le texte range sous la garde 14 ; module inchangé, comme VF2 le propose). VF2-08 : l'empreinte
du brouillon 6 citée en tête (`77bc2fe0…`) est celle du texte que j'ai relu à la ronde finale ; le fichier vaut
aujourd'hui `411eb334…` (modifié le 2026-10-20 à 04:28 UTC) ; je ne l'ai pas relu pour cette retouche (§ 8).

## 4. Tests

Nombre de tests : **165** (écrit en tête du fichier ; `test_nombre_de_tests_ecrit_en_tete` le vérifie) = 117 de départ
+ 48 : 21 fonctions neuves et 27 cas paramétrés. Aucun test retiré ; aucune assertion affaiblie. Retouche VF2 : six
tests étendus, aucun ajouté (§ 3 ter). Ronde finale : un test
neuf (garde 15) ; `test_audit_symetrie_tout_non_lu_ne_declenche_pas` renommé `…_toutes` (la règle « aucune » a changé :
ses deux nouveaux cas déclenchés sont affirmés) ; quatre cas ajoutés au test de la garde 7 ; motifs des messages
renforcés par leur numéro de garde ; `_rien_etabli` et `test_A8_verrou` construisent une P3-P1 non établie cohérente.

Tests neufs :
- CB1 et CB3 : `test_garde_4_textes_lus_sur_les_seuls_sauts_de_ligne`, `test_garde_4_textes_de_bout_en_bout`,
  `test_recommandation_reserve_non_lue_seule_jamais_non_robuste`, `test_audit_symetrie_tout_non_lu_ne_declenche_pas_toutes`,
  `test_graines_exactement_celles_de_leurs_cles`, `test_garde_1_entropie_empreintes_et_tests_cites`,
  `test_garde_10_et_localisation_avant_le_manifeste_aucune_sortie`, `test_garde_jamais_eprouvee_cas_sain_et_artefact`
  (27 cas, table `GARDES_R5` : les 25 gardes du relevé CB1 et les 2 gardes neuves de
  `_contraste_selon_les_etats`) ;
- CB2 et brouillon 6 : `test_verrou_de_fin_sur_les_conclusions_recalculees`,
  `test_garde_7_drapeaux_bruts_recoupes_avec_les_etats`, `test_entree_en_echec_garde_la_reserve_contraire_deja_calculee`,
  `test_recommandation_sur_donnees_non_lue_et_forme_du_cout`, `test_entree_entiere_en_echec_rend_non_lues_les_cibles_visees`
  (cibles visées écrites à la main d'après le texte, pas lues dans `VISEES`),
  `test_niveaux_des_intervalles_de_l_aire_du_cout_et_de_T2_propre`, `test_A2_fenetres_d_une_sonde_a_attention_par_ses_logits`,
  `test_A1_calculs_en_echec_non_lus`, `test_A2a_et_A5_seuil_de_l_aire_du_cout`,
  `test_A4a_chaque_condition_suffit_et_calculs_en_echec_non_lus`,
  `test_A6_reserve_temoin_ou_mention_et_effets_non_calculables`, `test_A7_formes_marge_et_correlations`,
  `test_A8_regles_de_reserve_par_condition`.

Tests existants changés (renforcés, ou adaptés à une règle changée par la session ou par le brouillon 6) :
- `test_audit_symetrie_toutes_les_reserves_possibles_declenchees` : il figeait l'ancienne règle (« non lu » compté
  déclenché ; « non robuste » pour `reserve_A6_non_lue`). Il garde un cas « toutes contraires » (déclencheur vrai) et
  ajoute le cas mixte (déclencheur faux, `controles_non_lus` = 1, deux listes exactes).
- `test_garde_9_premier_passage` : l'artefact « manifeste illisible quelconque : arrêt » devient, par la garde 16, un cas
  sain (manifeste d'un autre run écarté et rapporté) ; il porte maintenant six cas écartés et dix artefacts de la garde 16, en plus des deux de second passage.
- `test_garde_localisation_egale_a_celle_de_la_lecture` : l'artefact (écart de 1e-9) est désormais dans la tolérance du
  brouillon 6 ; artefacts portés à 1e-6 (pré-coût, coût), lignes décalées ajoutées, cas sains 1e-12 et 5e-10 ajoutés.
  Même chose pour l'écart du test de CB3-02.
- `test_garde_du_verrou_sain_et_artefacts` : nouvelle signature ; le premier artefact est « liste des analyses ≠ liste
  recalculée » (la réserve isolée sur une conclusion non établie est éprouvée seule, dans le test du verrou de fin, ce qui
  tue V3 ; l'ancien artefact était masqué par le contrôle lu sur la même cible).
- `test_A2_degenere_non_calculable`, `test_A3_degenere_temoin_absent` : leur construction forcée (T2 « établi » non
  calculable ; `conforme` vrai contre les états) est maintenant refusée par la garde 7 (CB2-11), ce que le test affirme ;
  la propriété « cible établie, calcul non calculable : contrôle non lu » est éprouvée sur la donnée saine, calcul rendu
  non calculable.
- `test_A2_verrou`, `test_A4_verrou`, `test_A5_verrou` : la non-établie est construite de façon cohérente
  (`_contraste_non_etabli` : borne sous le seuil, drapeaux, intention, issue recalculés) ; mêmes assertions.
- Assertions ajoutées : `test_A1_sain` (jeu → cible, niveaux), `test_A2_sain`, `test_A4_sain`, `test_A6_sain` (niveaux),
  `test_A7_sain` (jeu → cible), `test_A7_artefact_forme_du_cout` (niveau du jeu, lecture gelée),
  `test_A7_artefact_forme_quasi_totale` (lecture gelée), `test_A8_degenere_…` (les deux contrôles « non lus »),
  `test_A8_regle_stricte_…` (troisième jeton, action de trois jetons), `test_A4_degenere` (deux tâches mixtes, deux paires),
  `test_aucune_moyenne_…` (fenêtre juste avant le champ), `test_degenerescences_…` (frontière de 1 %, tirages imposés),
  `test_toute_exception_…` (contrôles de A3 « non lus »), `test_garde_11_…` (réserve générale « non contrôlée »),
  `test_garde_2_…`, `test_garde_3_…`, `test_ligne_de_commande_de_bout_en_bout`, `test_ligne_de_commande_reelle_…`.
- Aides : `_ecrire_run_source` (paramètre `alterer_textes`, par défaut mêmes octets qu'avant), `_source_lecture`, `_D`,
  `_contraste_non_etabli`, `_lecture_recalculee`, `_entree_seule`, `_jamais`, `_cd_fictif`, `_verrou_avec_controle_lu_sur`,
  `_ecrire_textes_comme_le_run`, `_texte_separateurs`, `_lecture_decisive`, `_runs`, `_tronquer_ligne_3`,
  `MANIFESTE_CASSE_AUTRE`.

## 5. Mutants de la revue CB2 (51)

Lanceur `essais/mutants_b4.py` : la liste `essais/mutants_b3_2.py` est la copie, sans modification, de celle de la
revue CB2 ; `BASE` = `essais/base-b4/`, copie octet pour octet de final-b4 (empreintes égales, vérifiées au lancement).
`verifier` : les 51 motifs présents une seule fois. Motifs adaptés, même règle mutée : V1
(`if c["controle_contraire"] != SANS_OBJET and c["cible"] not in recalculees:` → `if False:`), V2 (`exiger_verrou(sortie,
lecture, etablies, …)` → `exiger_verrou(sortie, lecture, cibles_possibles(principales), …)`), V3 (`if r["cible"] not in
recalculees:` → `if False:`) ; les 48 autres tels quels. Chaque mutant est lancé sur sa copie avec la sélection `-k` de
son test, arrêt au premier échec ; « tué » = pytest rend 1 (test en échec). Le premier échec de chaque journal est le test
attendu (`essais/mutants-b4-resultats.jsonl`, `essais/mutants/<id>/pytest.log`). Témoin : l'union des sélections sur la
copie non mutée passe (`52 passed, 113 deselected in 140.75s`, `essais/mutants-b4-temoin.log`). Table ci-dessous : passage
sur les fichiers finaux (165 tests, après la ronde finale). Deux passages antérieurs, sur les états à 162 et 164 tests,
avaient donné les mêmes tests tueurs et le même résultat (`essais/mutants-b4-run-tests162.log`, `essais/mutants-b4-run-tests164.log`).

| mutant | règle mutée | sur final/ (revue CB2) | test qui le tue (copie mutée de final-b4) | résultat |
|---|---|---|---|---|
| V1 | exiger_verrou n'arrête plus un contrôle lu (non « sans objet ») sur une cible non établie (motif adapté) | survit | `test_verrou_de_fin_sur_les_conclusions_recalculees` | tué (1 failed, 164 deselected, 20 s) |
| V2 | exiger_verrou appelé avec toutes les cibles possibles au lieu des seules établies (motif adapté) | survit | `test_verrou_de_fin_sur_les_conclusions_recalculees` | tué (1 failed, 164 deselected, 20 s) |
| V3 | exiger_verrou accepte une réserve sur une conclusion non établie (motif adapté) | survit | `test_verrou_de_fin_sur_les_conclusions_recalculees` | tué (1 failed, 164 deselected, 20 s) |
| V4 | table : P3-P4 établie sans la ligne d'issue « critères 2 et 3 » | tué | `test_conclusions_etablies_table_fermee` | tué (1 failed, 164 deselected, 6 s) |
| V5 | clé interdite au_dessus_du_plancher retirée de la liste (filtre et verrou) | tué | `test_garde_du_verrou_sain_et_artefacts` | tué (1 failed, 164 deselected, 19 s) |
| V6 | exiger_verrou ne compare plus l'issue recopiée à l'issue décisive | tué | `test_issue_primaire_inchangee_et_garde_de_la_copie` | tué (1 failed, 164 deselected, 56 s) |
| V7 | instantané de la lecture décisive non comparé en fin de course | tué | `test_issue_modifiee_pendant_l_addendum_arrete` | tué (1 failed, 164 deselected, 31 s) |
| C1 | A1 : témoin contre honnête vise T3 au lieu de P3-P4 | survit | `test_A1_sain` | tué (1 failed, 164 deselected, 20 s) |
| C2 | A1 : saboteur contre témoin vise P3-P3 au lieu de P3-P4 | survit | `test_A1_sain` | tué (1 failed, 164 deselected, 20 s) |
| C3 | A1 : saboteur contre mention vise P3-P3 au lieu de T3 | survit | `test_A1_sain` | tué (1 failed, 164 deselected, 19 s) |
| C4 | A7 : saboteur contre témoin vise P3-P3 au lieu de P3-P4 | survit | `test_A7_sain` | tué (1 failed, 164 deselected, 19 s) |
| C5 | A7 : saboteur contre mention vise P3-P3 au lieu de T3 | survit | `test_A7_sain` | tué (1 failed, 164 deselected, 19 s) |
| C6 | entrée A4 entière en échec : T1 n'est plus « non lu » (VISEES) | non lancé | `test_entree_entiere_en_echec_rend_non_lues_les_cibles_visees` | tué (1 failed, 164 deselected, 9 s) |
| C7 | entrée A3 entière en échec : T3 n'est plus « non lu » (VISEES) | non lancé | `test_entree_entiere_en_echec_rend_non_lues_les_cibles_visees` | tué (1 failed, 164 deselected, 9 s) |
| C8 | entrée A7 entière en échec : P3-P4 et T3 ne sont plus « non lus » (VISEES) | non lancé | `test_entree_entiere_en_echec_rend_non_lues_les_cibles_visees` | tué (1 failed, 164 deselected, 9 s) |
| N1 | A2 (a) : intervalle calculé à 80 %, annoncé 95 % | non lancé | `test_niveaux_des_intervalles_de_l_aire_du_cout_et_de_T2_propre` | tué (1 failed, 164 deselected, 6 s) |
| N2 | T2_propre (A5) : intervalle à 80 %, annoncé 95 % | non lancé | `test_niveaux_des_intervalles_de_l_aire_du_cout_et_de_T2_propre` | tué (1 failed, 164 deselected, 6 s) |
| N3 | A2 (b) : intervalle de δ̄ à 80 % | non lancé | `test_A2_sain` | tué (1 failed, 164 deselected, 19 s) |
| N4 | A4 (a) : intervalles à 80 % | non lancé | `test_A4_sain` | tué (1 failed, 164 deselected, 19 s) |
| N5 | A4 (b) : intervalle de Δ_intra à 80 % | non lancé | `test_A4_sain` | tué (1 failed, 164 deselected, 19 s) |
| N6 | A4 (c) : T1 de sensibilité à 80 % | non lancé | `test_A4_sain` | tué (1 failed, 164 deselected, 19 s) |
| N7 | A6 : effets du coût à 80 % | non lancé | `test_A6_sain` | tué (1 failed, 164 deselected, 19 s) |
| N8 | A1 : T1 à 97,5 % au lieu de 95 % | non lancé | `test_A1_sain` | tué (1 failed, 164 deselected, 20 s) |
| N9 | A7 (ii) : niveau fixe 95 % au lieu du niveau du jeu (97,5 % sur saboteur contre honnête) | non lancé | `test_A7_artefact_forme_du_cout` | tué (1 failed, 164 deselected, 20 s) |
| J1 | A2 (c) : fenêtre juste avant le champ notée par la moyenne des jetons | survit | `test_aucune_moyenne_sur_les_jetons_score_d_empan_maximum` | tué (1 failed, 164 deselected, 6 s) |
| J2 | A2 (b) : fenêtres d'une sonde à attention notées au maximum (logits ignorés) | survit | `test_A2_fenetres_d_une_sonde_a_attention_par_ses_logits` | tué (1 failed, 164 deselected, 9 s) |
| R1 | A8 saturation : les deux conditions exigées (all au lieu de any) | non lancé | `test_A8_regles_de_reserve_par_condition` | tué (1 failed, 164 deselected, 9 s) |
| R2 | A8 début : une seule condition suffit (or au lieu de and) | non lancé | `test_A8_regles_de_reserve_par_condition` | tué (1 failed, 164 deselected, 10 s) |
| R3 | A4 (a) : les deux conditions exigées (et au lieu de ou) | non lancé | `test_A4a_chaque_condition_suffit_et_calculs_en_echec_non_lus` | tué (1 failed, 164 deselected, 10 s) |
| R4 | A4 (a) : condition « borne basse de A_T4(b) ≤ quantile observé » retirée | non lancé | `test_A4a_chaque_condition_suffit_et_calculs_en_echec_non_lus` | tué (1 failed, 164 deselected, 9 s) |
| R5 | A6 : réserve témoin ou mention levée même si la borne était déjà > 0 dans la lecture | non lancé | `test_A6_reserve_temoin_ou_mention_et_effets_non_calculables` | tué (1 failed, 164 deselected, 10 s) |
| L1 | A1 : calcul en échec ou non calculable lu favorable | non lancé | `test_A1_calculs_en_echec_non_lus` | tué (1 failed, 164 deselected, 9 s) |
| L2 | A3 : calcul des contrastes en échec lu favorable | non lancé | `test_toute_exception_autre_que_garde_arrete` | tué (1 failed, 164 deselected, 38 s) |
| L3 | A4 (a) : calcul en échec lu favorable | non lancé | `test_A4a_chaque_condition_suffit_et_calculs_en_echec_non_lus` | tué (1 failed, 164 deselected, 9 s) |
| L4 | A4 (b) : calcul en échec lu favorable | non lancé | `test_A4a_chaque_condition_suffit_et_calculs_en_echec_non_lus` | tué (1 failed, 164 deselected, 9 s) |
| L5 | A6 P3-P1 : effet au lecteur étendu non calculable lu favorable | non lancé | `test_A6_reserve_temoin_ou_mention_et_effets_non_calculables` | tué (1 failed, 164 deselected, 10 s) |
| L6 | A7 (i) : séparation non calculable lue favorable | non lancé | `test_A7_formes_marge_et_correlations` | tué (1 failed, 164 deselected, 10 s) |
| L7 | A7 (ii) : calcul restreint en échec lu favorable | non lancé | `test_A7_formes_marge_et_correlations` | tué (1 failed, 164 deselected, 10 s) |
| L8 | A8 : début de l'action non lu écrit favorable quand le calcul échoue | non lancé | `test_A8_regles_de_reserve_par_condition` | tué (1 failed, 164 deselected, 9 s) |
| L9 | A8 : contrôle de saturation omis quand le calcul échoue (sonde à attention) | non lancé | `test_A8_regles_de_reserve_par_condition` | tué (1 failed, 164 deselected, 10 s) |
| L10 | A8 : poids maximal non défini lu favorable | non lancé | `test_A8_regles_de_reserve_par_condition` | tué (1 failed, 164 deselected, 9 s) |
| G1 | garde 7 : borne ou aire non numérique acceptée dans un jeu lu | non lancé | `test_garde_jamais_eprouvee_cas_sain_et_artefact[garde 7 : valeur de jeu non numérique]` | tué (1 failed, 12 passed, 138 deselected, 20 s) |
| G2 | règle des 1 % portée à 5 % de tirages dégénérés | non lancé | `test_degenerescences_au_dela_de_1_pourcent` | tué (1 failed, 164 deselected, 6 s) |
| G3 | A7 (ii) : forme contrôlée seulement si présente dans 50 actions du jeu (au lieu de 10) | non lancé | `test_A7_formes_marge_et_correlations` | tué (1 failed, 164 deselected, 10 s) |
| G4 | A4 (b) : une paire intra-tâche suffit (au lieu de 10) | non lancé | `test_A4_degenere` | tué (1 failed, 164 deselected, 16 s) |
| G5 | A7 (iii) : seuil de corrélation 0,90 au lieu de 0,50 | survit | `test_A7_formes_marge_et_correlations` | tué (1 failed, 164 deselected, 10 s) |
| G6 | A8 : seuil du poids maximal 0,99 au lieu de 0,95 | survit | `test_A8_regles_de_reserve_par_condition` | tué (1 failed, 164 deselected, 9 s) |
| G7 | A8 : seuil des trois premiers 0,80 au lieu de 0,50 | survit | `test_A8_regles_de_reserve_par_condition` | tué (1 failed, 164 deselected, 9 s) |
| G8 | A8 : deux premiers jetons au lieu de trois | survit | `test_A8_regle_stricte_des_trois_premiers_jetons_et_segments` | tué (1 failed, 164 deselected, 5 s) |
| G9 | A2 (b) : 10 répliques au lieu de 50 | tué | `test_aucune_moyenne_sur_les_jetons_score_d_empan_maximum` | tué (1 failed, 164 deselected, 6 s) |
| G10 | A2 (a) et A5 : seuil d'aire 0,45 au lieu de 0,5 | survit | `test_A2a_et_A5_seuil_de_l_aire_du_cout` | tué (1 failed, 164 deselected, 10 s) |

Tués : 51 sur 51 (sur la revue CB2 : 5 tués, 15 survivants, 31 non lancés).

## 6. Sorties de pytest, durées, caches, relevé des gardes

Commande (consigne), depuis `/home/user/controle-ia-travail` (lecture seule) :

```
PYTHONPATH=src:tests PYTHONDONTWRITEBYTECODE=1 …/venv-gpu-neuf/bin/python -m pytest -q -p no:cacheprovider \
    …/addendum-p3/final-b4/test_complements_p3_v1.py
```

Sortie finale, sur les empreintes du § 8 (vérifiées au lancement, `essais/empreintes-au-lancement-vf2.txt`, et après la
fin), journal `essais/pytest-final-vf2.log` :

```
........................................................................ [ 43%]
........................................................................ [ 87%]
.....................                                                    [100%]
165 passed in 1049.77s (0:17:29)
```

Durée : 17 min 29 s. Les passages des mutants de VF2 (témoin et 8 mutants sur trois processus, puis six mutants relancés
avec `-l`) ont tourné pendant les quatre premières minutes, sur une machine partagée avec un autre chantier. Avant la
retouche, l'état à 165 tests avait pris 15 min 16 s, seul (`essais/pytest-final.log`) ; l'état à 164 tests, 15 min 2 s
(`essais/pytest-final-164.log`). Le seuil de 15 minutes n'est donc pas démontré tenu ; je n'ai rien retiré ni allégé pour
le tenir. La retouche VF2 ajoute surtout un addendum complet (VF2-02) ; les plus coûteux restent ceux d'avant (scénarios
complets, dépôt jetable, ligne de commande réelle à 2 000 et 10 000 tirages).

Jalons (même commande sauf mention) :
- état CB1 et CB3, 149 tests : `149 passed in 979.25s (0:16:19)`, deux suites en parallèle (`essais/pytest-jalon-cb1-cb3.log`) ;
  un passage sous relevé lancé en même temps a eu trois échecs, tous dus à mes retouches du module pendant ce passage (les
  copies du dépôt jetable ont lu un module à moitié édité : `NameError: preparer_donnees`) ; journal gardé
  (`essais/pytest-trace-cb1-cb3-perturbe.log`), sans portée ;
- état CB2, 162 tests, avec trois passages de mutants en parallèle : `162 passed in 930.23s (0:15:30)`
  (`essais/pytest-jalon-cb2-en-charge.log`) ; un second passage de cet état, devenu caduc après l'ajout de deux cas R5, a été
  arrêté par son identifiant de processus (18289, R10 ; `essais/pytest-interrompu-162.log`) ;
- état à 164 tests (avant la ronde finale), seul : `164 passed in 902.81s (0:15:02)` (`essais/pytest-final-164.log`) ; sous
  relevé des lignes (greffon `essais/trace_lignes_b4.py`), mutants en parallèle : `164 passed in 1189.68s (0:19:49)`
  (`essais/pytest-trace-b4.log`) ;
- ronde finale, tests touchés seuls : `36 passed, 1 skipped, 128 deselected in 459.40s` ;
- état à 165 tests avant la retouche VF2 (tests `7605c205…8f0d`), seul : `165 passed in 916.25s (0:15:16)`
  (`essais/pytest-final.log`, empreintes `essais/empreintes-au-lancement-final.txt`) ;
- retouche VF2, six tests touchés seuls : `6 passed, 159 deselected in 74.20s (0:01:14)`.

Relevé des gardes (`essais/gardes_non_eprouvees_b4.py`, même méthode que la contre-lecture CB1, sur l'état à 164 tests ;
non refait après la ronde finale, qui ajoute deux gardes, `P3-P1/etablie` et `exiger_parametres_du_texte`, chacune
éprouvée sur un cas sain et des artefacts, ni après la retouche VF2, qui ne fait qu'ajouter des cas aux tests) :
`lignes exécutées relevées : 1658 ; gardes : 107 ; gardes jamais exécutées par les tests : 0`
(`essais/gardes-non-eprouvees-b4.log`). Limite : la ligne de commande lancée dans un processus séparé n'est pas tracée.

Caches (CB1-07) : `find final-b4 -name __pycache__ -o -name .pytest_cache -o -name "*.pyc"` ne rend rien. Un
`essais/__pycache__` avait été créé par mes chargements du lanceur de mutants (importlib sans `-B`) ; supprimé, et le
lanceur pose désormais `sys.dont_write_bytecode`.

## 7. Règles non appliquées, points tranchés

Toutes les décisions de la session et les règles du brouillon 6 final sont appliquées ; aucune règle n'est laissée de
côté. Points tranchés par la session et appliqués (§ 3 bis) : garde 15 (égalité des paramètres de tirage contrôlée par la
ligne de commande), audit « aucune » à la lettre, `P3-P1.etablie` recoupé, garde 16 (choix retenu), numéros de garde
harmonisés. Choix du code restés tels quels, déjà écrits au texte ou sans portée :
1. Précision 18 : seuls les drapeaux que la table consulte sont recoupés (texte, précision 18).
2. CB1-01 : « lignes vides » = exactement vides ; une ligne d'espaces est illisible (arrêt, éprouvé depuis VF2-04) ;
   numéro de ligne physique à partir de 1.
3. Recommandation : la lecture gelée des réserves de forme de A7 nomme entre parenthèses le test qui la porte.
4. CB2-09 : si l'échec vient d'une valeur non finie du descriptif, ce descriptif partiel est retiré (motif écrit) ; les
   contrôles faits restent.
5. Garde 15 : le chemin du préenregistrement passé à la commande (`exiger_commande`) porte aussi « garde 15 » (arrêt de
   forme) ; les gardes internes de `verifier_parametres_tirage` (au moins un tirage, niveaux dans ]0, 1[) aussi.
6. Messages sans numéro, hors de la liste d'arrêt : verrou de fin (« verrou unidirectionnel »), forme du run source
   (`_donnees`), règles de A5, A8 ; inchangés.
7. CB1-06 : les branches mortes en pratique sont gardées (défenses) et éprouvées par appel direct.
8. CB3-03 (mémoire), CB3-06 et CB1-07 (verser les deux fichiers seuls) : hors code ; CB3-05 : dépôt complet (session).

## 8. Empreintes

| fichier | sha256 |
|---|---|
| `final-b4/complements_p3_v1.py` | `2b16179d4451c3f10c0c1053687d76f68c9b32b43f2b460463d844ab45c15996` |
| `final-b4/test_complements_p3_v1.py` | `7387910d3b5851026f316e89df3f1b84e4a39758e9d73da52cea166f5223e0a3` |
| `final-b4/essais/base-vf2/` (copie pour les mutants de VF2) | mêmes empreintes que les deux fichiers ci-dessus |
| `final-b4/essais/base-b4/` (copie pour les 51 mutants CB2) | module : même empreinte ; tests : état d'avant VF2, `7605c2051e853d9707e59a13ccc26a5b99678f3efb67748f00d710c4336f8f0d` |
| rapport VF2 `verification-code-final-addendum-P3-v1-mutants.md` | `aab50bf0230cd923f8c0c3ee9a5f91c5f6bb6805e28ce79f2c9138abda5ecc7b` |
| lanceur VF2 `verification-finale/mutants/lanceur_vf2.py` (substitutions) | `76aa1ea5760427990193e06bbf7e955b8bbe977d4c63093da1f6929c409dcb52` |
| départ `final/complements_p3_v1.py` | `daf954594456f8c268ebbf48b14326a183941c00c4cddb205b2e3382a875f4fa` |
| départ `final/test_complements_p3_v1.py` | `01b5faeaf1fe5ea38624b872948d46d5310bc67b6df3277ea1515e73fc057abc` |
| brouillon 6, état final (texte qui fait foi) | `77bc2fe0d62aac4384712ee77c28fa6b77a30d47092b3d327120186d60d24e5c` |
| brouillon 6, état précédent | `503daf1224681735c0f67d77ae1d9253e2447a92d16c3e785d5ac4f8868a591e` |
| brouillon 6, fichier au 2026-10-20 04:28 UTC (relu par VF2, VF2-08 ; non relu ici) | `411eb3344b153cc81f118aad3dab5781934f60c1f9dc22efdf3f2ef2f5338a1a` |
| états intermédiaires du module et des tests | 165 tests avant VF2 : `2b16179d…5996` et `7605c205…8f0d` ; 164 tests : `d225a0c6…f09f` et `72e5562f…bd10` ; 162 tests : `d225a0c6…f09f` et `136f3ad1…760f` |
