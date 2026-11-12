# Contre-lecture 1 (R2) du brouillon 2 du préenregistrement de la course réelle de l'organisme d'idéation (code v66, configuration v6) — v1

- **Contre-lecteur** : sous-agent neuf de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, modèle Claude Fable 5.2 (`claude-fable-5-2`), autre modèle que le rédacteur des brouillons 1 et 2 (Claude Opus 5.5). N-052 nomme Fable 5.1 : écart de version déclaré (même réserve qu'en R-2053). Je n'ai écrit ni ce texte, ni le code v65 ou v66, ni leurs contre-lectures, ni le devis.
- **Heures** (temps universel, relevées par `date -u`, 10 novembre 2026) : début 14:53:22 ; essais ciblés 15:00:04 → 15:01:41 ; couples rejoués et repassés au lanceur à 15:09:15 ; rapport fini à 15:13:09.
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-contre-lecture-1-prereg-course-v66-b2-v1.md`, sha256 `0042d919954f945c53f736f82446e03c4744b56167c35d97448cfdb48c5e4d23`, vérifiée par `sha256sum` avant lecture.
- **Interdits communs v2 tenus** : aucun fichier ni branche interdit ouvert ; aucune variable d'environnement lue ni affichée ; aucun appel de modèle, aucun réseau, aucune instance, aucune dépense ; aucun `checkout`, `commit`, `push`, `fetch` ; arbre `/home/user/organisme-v65-cl` lu seulement (tête `7e415cbaaa3ff602db43a44dad6b4307c08352c7`, `git status` vide), essais joués depuis une copie dans mon bac à sable. Aucun refus de permission ni de classifieur. Écrit dans le dépôt : ce rapport et son compagnon, rien d'autre.
- **Texte relu** : `docs/notes/organisme-boucle-reelle-v1/preenregistrement-boucle-reelle-organisme-v1-brouillon2.md`, sha256 `f87ad0e40f1b2941e66d343bfb4b5eeaaefa22a3e2eeb448f852900de112b8a7` (égale à la consigne et au compagnon), lu en entier.

## 0. Verdict

**« Scellable après les mots de Lazar et corrections »** : après les deux mots de Lazar (NL-1, NL-2), les neuf couples CLC-01 à CLC-09 (section 8 ; texte après eux seuls : `b19db56e58302d57ee3d1aa114a6038f9aceb54b93b233930da513d7b4846cc6`) et la réécriture des passages que le remplissage des marqueurs laisserait périmés (CLB-04).

- Le texte est un préenregistrement complet au sens de R1, à une réserve près (CLB-03 : la prédiction P2 a une réfutation écrite et aucune ligne de lecture).
- Aucune hypothèse, aucun seuil, aucun signe ni chiffre de prédiction ne change entre le brouillon 1 et le brouillon 2 (sections 2 et 6 égales à l'octet ; section 4 : le seul couple B2-18).
- Le texte, marqueurs remplis de valeurs d'essai, **passe le lanceur gelé** jusqu'à la garde 22 (refus attendu ici : `bwrap` absent), avec la ligne de GO proposée en NL-2 lue à 45 USD.
- **Trois constats bloquent le scellement en l'état** (tous levés par couple ou par réécriture, aucun ne demande de code) : CLB-01 (la commande « exacte » de la section 12.4 est refusée par la garde 15), CLB-03 (P2), CLB-04 (passages périmés au candidat). Les autres sont à corriger au même passage.
- **Ce qui changerait mon verdict** : si la mère veut qu'une P2 manquée interdise C1, c'est un changement de critère de lecture, donc un troisième nœud pour Lazar (CLB-03).

## 1. Ce que j'ai vérifié et rejoué

Interpréteur `/home/user/controle-ia-travail/.venv/bin/python -I -B`. Bac à sable : `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/cl-prereg-course-v66/`.

| objet | résultat |
|---|---|
| empreintes données par la consigne | brouillon 2 `f87ad0e4…`, couples `43ba74e9…`, journal `ff364a2c…`, brouillon 1 `736e3fd6…`, contre-lecture v66 `a2880368…` : égales ; script `14011931…`, rapport v66 `f6433d38…`, contre-lecture v65 `c4ddfc7f…`, configuration v6 `4743ddbe…`, blocs `9933ee11…`, héritage `93dcf517…`, `registres/go.md` `2c396b01…` : égales à leurs compagnons ou au texte |
| couples du rédacteur, rejoués par un programme à moi (sans son script) | les 40 textes anciens trouvés chacun une fois dans le brouillon 1 ; brouillon 1 + 40 couples = brouillon 2 jusqu'à la section 16, à l'octet ; 17 couples en sections gelées (B2-18 à B2-34), comme annoncé |
| trois blocs de la section 16 | chacun une fois ; égaux à l'octet à `blocs-pour-le-texte-v66.md`, hors la ligne `go` |
| sections 2 (hypothèse) et 6 (seuils) | égales à l'octet entre brouillon 1 et brouillon 2 |
| chiffres de la section 4.2 et des tables 3.3 et 3.4 | égaux aux sorties `a23959fa…` et `fe2bc502…` (1 000 sur 1 000 ; 617 ; 501 ; 318 [0,290 ; 0,348] ; 994 ; 725 à 810 ; −0,004 et −0,005 ; gains de l'oracle) ; sondages : lignes 98 à 106, 122, 125, 129 du `README.md` de l'organisme, docstring du nul v8 (lignes 75 à 92), verdict d'A1-v3 (lignes 17 à 22, 47) : conformes |
| **lanceur gelé sur le texte** (copie de l'arbre ; texte nommé `…-v1.md`, marqueurs remplis de valeurs d'essai, scellé par `controle_ia.scellement sceller` ; dossier de course versé ; copie de `registres/go.md` avec la ligne proposée en NL-2 sous un identifiant d'essai) | commande de la section 12.4 avec `--verifier-seulement` : texte, monde, configuration (empreinte et contenu), GO, garde 17 passés ; **refus « MachineRefusee : bwrap ≥ 0.9 exigé (lu : None) », code 2** (garde 22, attendu ici). Sans le compagnon `.sha256` de l'héritage : refus à la garde 17 (CLB-08) |
| artefacts de la même commande | texte à marqueurs : refus (« marqueur(s) non rempli(s) ») ; vrai registre sans la ligne neuve : refus (« absent du registre ») ; `--go` autre que celui du texte : refus ; texte hors de `prereg/…-v<N>.md` : refus ; tous code 2 |
| ligne de GO proposée en NL-2, sonde `sonde_go.py` | lue par la garde de calcul (`lire_go`, 256 identifiants, aucune extension) ; `verifier_go_v66` : 45 USD « montant seul » du jour de l'accord au 30 novembre ; 40, 44,99 et 50 refusés ; veille et 1er décembre refusés |
| vérifications V-1 à V-8, sonde `sonde_v.py` (écrites à la lettre du texte) | sur les trois relevés à blanc versés et sur douze altérations en mémoire : section 3.2 |
| garde 15, sonde `sonde_garde15.py` (dictionnaires synthétiques, aucun environnement réel lu) | sans `POLE_MACHINE_JETABLE_V56=1` : refus ; avec elle et une variable de session courante : refus ; liste réduite : admis (CLB-01) |
| essais ciblés (14 classes de `test_boucle_reelle_v66.py`, `test_lecture_boucle_reelle_v66.py`, `test_boucle_reelle_v65.py`) | **53 passés, 74 en échec, 1 sauté**, deux fois ; tous les échecs sont des essais qui jouent une course entière, et la cause est le nom de mon bac à sable (CLB-02, section 9) : ce n'est pas un défaut du code |

Sondes, couples et sorties gardés dans le bac à sable : `sondes/sonde_go.py` `7c0f788a…`, `sondes/sonde_v.py` `2fde5672…`, `sondes/sonde_garde15.py` `2eb546b2…`, `couples/faire_couples_cl1.py` `24c903cb…`, `couples/couples-cl1.json` `a555f82c659907b273e47b913f0c48a4231a66115883c58d201383c0128ca514` (égal au bloc de la section 8), `sorties-essais-cibles.txt` `bb5585a6…`, `sorties-essais-cibles-2.txt` `adba0f6e…`.

## 2. Mandat 1 — complétude (R1) et couples en sections gelées

| élément de R1 | où | jugement |
|---|---|---|
| hypothèse | section 2 (H-boucle, parties a, b, c) | présent, inchangé |
| prédiction chiffrée et signe | section 4.1 (P1 à P7, probabilité simulée, réfutation ; signe + partout, « aucune prédiction ouverte dans un seul sens ») | présent ; **P2 sans conséquence de lecture** (CLB-03) |
| métrique | section 5 | présent |
| seuil | section 6 (α, m = 22, log(22/0,05), 0,02 nat, 2,0, 10⁻⁶) | présent, inchangé |
| plan d'analyse | section 7 (graines R9 : E = empreinte du texte scellé, `SeedSequence(E, spawn_key=…)` ; ordre ; oracle lu une fois) | présent |
| critères de lecture gelés | section 8 (C5, C4, C2, C3, C6, C1 ; V-1 à V-8) et section 9 (A1 à A4) | présent ; un marqueur (NL-1) ; CLB-03, CLB-06, CLB-09 |
| liste d'arrêt | section 10 (gardes 1 à 10, 13 à 16, 17 à 23) | présent ; deux lettres inexactes (CLB-07) |

**Les 17 couples B2-18 à B2-34.** Aucun ne touche une hypothèse, un seuil, un signe ni un chiffre de prédiction.

- **Alignements sur le code gelé, vérifiés au code** : B2-18 (la lecture compare `vues_servies["2"]`, `lecture_boucle_reelle_v66.py` l. 161-163) ; B2-19 à B2-21 (`wilson` et `PARTS_WILSON` l. 291-303 ; `jetons_de_l_usage` et `ReleveDeJetons`, cœur l. 273-331) ; B2-22 (`--releve-sha256` exigé, `lire_boucle_reelle_v66.py`) ; B2-23 (`consigne_sans_loi_gelee`, cœur l. 186-236 ; `lignes_de_tranche_servies` l. 334-342) ; B2-29 (audit A1, lecture l. 245-263) ; B2-30, B2-33, B2-34 (garde 7 : cœur l. 472-476, 561-565, 585-589 ; garde 22 : lanceur l. 271-294 et 434-436 ; garde 23 : cœur l. 141-169 ; jugements avant l'étage : cœur l. 421-449).
- **Plus que des alignements, dits tels par le rédacteur** : B2-24 à B2-28 ajoutent des clauses de lecture que le programme gelé ne calcule pas (V-1 à V-8, « le texte prime »). Sens vérifié : chacune ne peut que **retirer** C1 (vers C5 ou C4) ou ajouter « C4 (partielle) » sous C5 ; aucune ne rend C1 à un relevé que le programme lit autrement. Rien n'étant scellé, ces ajouts sont permis ; ils sont du ressort de cette contre-lecture, et je les tiens pour fondés (section 3.2).
- **Lettres inexactes** : B2-32 (« archive plus petite » : le code arrête sur tout autre nombre de membres) ; la ligne 21 de la liste d'arrêt, non touchée par le rédacteur, dit « refus » alors que le cœur v66 en fait un arrêt consigné (CLB-07).
- Hors sections gelées, B2-17 change le dessin (section 3.7 : les lois plantées promues en génération 2 sont testées) : conforme au code (cœur l. 461-469) et au devis (section 3.4, « chaîne cassée », 35,30 USD) ; l'issue se lit sur la promotion.

## 3. Mandat 2 — gardes, arrêts, vérifications V

### 3.1 Gardes et arrêts annoncés, au code v66 et aux essais

« Passé » : passé dans mes essais ciblés. « Course » : l'essai joue une course entière ; il existe, il a passé dans la suite rejouée par la contre-lecture du code v66 (323 passés), mais je n'ai pas pu le rejouer validement (section 9).

| garde ou arrêt | au code | cas sain | artefact |
|---|---|---|---|
| 6, texte scellé | lanceur l. 167-199, `lire_plan` l. 125-164 | `PlanEtTexte.test_texte_sain`, `test_plan_sain` : passés ; mon rejeu réel | `PlanEtTexte.test_texte_artefacts`, `test_plan_artefacts` : passés ; mes quatre artefacts |
| 7, lois plantées ni retenues ni servies | cœur l. 150-152, 472-476, 561-565, 585-589 ; lecture l. 164-169 | `Garde7EtCopies.test_unitaire_selection` : passé | `test_artefact_loi_plantee_dans_la_selection`, `…_dans_l_heritage_lu`, `…_a_la_relecture_finale` : course |
| 17, héritage de départ | lanceur l. 433 ; `boucle_reelle_v65.lire_heritage_depart` | `HeritageDepart.test_sain_accepte` : passé | `Gardes17Et19.test_garde_17`, `HeritageDepart.test_artefact_*` (cinq) : passés ; mon rejeu (compagnon absent) |
| 18, lois plantées jugées avec l'archive | cœur l. 117-119 | `JugeV66.test_sain_meme_calcul_que_v64_et_v65_membre_dominant_garde` : passé | `JugeV66.test_artefact_garde_18`, `JugeAvecArchive.test_artefact_garde_18_plantee_jugee_sans_archive`, `…_archive_plus_petite` : passés |
| 19, jeu planté | `boucle_reelle_v65.lire_jeu_plante` | `JeuPlante.test_sain_jeu_lu_a_l_octet` : passé | `Gardes17Et19.test_garde_19`, `JeuPlante.test_artefact_*` (cinq) : passés |
| 20, bras réel seul ; D2 | cœur l. 515-518 ; lanceur l. 142-145 | `BrasEtGeneration2.test_sain_bras_reel` : passé | `BrasGenerationsFamilles.test_garde_20_et_D2`, `BrasEtGeneration2.test_artefact_garde_20` : passés |
| 21, copies | `boucle_reelle_v65.copies_de_la_selection` ; cœur l. 566-571 | `BrasEtGeneration2.test_copies_garde_21` : passé ; `Garde7EtCopies.test_sain_copies_…` : course | `Garde7EtCopies.test_artefact_copie_d_une_carte_non_retenue` : course |
| 22, machine | lanceur l. 259-294, 434-436 | `Machine.test_sain_bac_reel_essai_a_blanc` : **sauté** (`bwrap` absent ; à jouer sur la machine, dit au texte) | `Machine.test_garde_22_avant_la_sonde`, `…_apres_la_sonde`, `test_artefact_bwrap_absent_refus_code_2_sans_repli_partout`, `BrancheReelle.test_garde_22_cablee_…`, `test_ordre_…` : passés ; mon rejeu réel |
| 23, vue servie | cœur l. 141-169, 364-374, 388-392 | `VueServie.test_sain_vues_servies_au_releve` : course | `VueServie.test_artefacts_garde_23_avant_l_appel`, `…_apres_l_appel` : passés ; `test_artefact_la_generation_2_ne_sert_que_K1` : course |
| arrêt qui ne masque pas une brèche | cœur l. 421-449 ; lecture l. 219-225 | `JugementsAuReleve.test_sain_jugements_puis_verdicts` : course | `JugementsAuReleve.test_artefact_arret_ne_masque_pas_une_fausse_promue` : passé |
| relevé incomplet lu C5 | lecture l. 82-127 | `Issues.test_C1_sain` : course | `Issues.test_C5_releve_incomplet_artefacts_de_la_contre_lecture` : passé |
| GO | lanceur l. 424-429 ; `registre_go_v66.py` | `BrancheReelle.test_vrai_registre_lu`, `test_go_enveloppe_lu_par_le_lanceur` : passés ; ma sonde | `BrancheReelle.test_refus_nommes` : passé ; ma sonde |
| 1 à 5, 8 à 10, 13 à 16 (reprises du tour fermé) | code v64 et v59 gelé | classes présentes dans `test_tour_ferme_v64.py`, `test_gardes_tour_ferme_v64.py`, `test_v59_boucle_fermee.py` (`Garde5PlafondEtage`, `Garde6Complete`, `Garde7`, `Garde9`, `Garde13Duree`, `MachineJetable`, `SondeDuBac`, `CommandeCode4`, `TestLectureHeritageV59`, …) | non rejouées par moi |

Toutes les gardes annoncées existent au code v66 avec un essai nommé. Ce que le texte dit non éprouvé (cas sain de la garde 22 ; K01, K17, K19) est exact.

### 3.2 Vérifications V-1 à V-8

**Faisables sur le relevé brut : oui.** Chaque champ nommé existe dans le relevé du cœur v66 (cœur l. 525-529, 550-560, 582-590) et dans les trois relevés versés. La lecture gelée ne peut pas les contourner : elles se font hors du programme, et le texte interdit toute issue autre que C5 sans les huit recopiées au verdict.

| relevé | programme | V |
|---|---|---|
| à blanc complet (`81b7fb54…`) | C1 | toutes tenues ; V-8 : non vide (12 retenues, 4 copies) |
| à blanc, arrêt des proposeurs en génération 2 | C5 | V-2, V-5 (génération 2), V-7 : manques |
| à blanc, arrêt pendant l'étage de la génération 1 | C5 | V-1, V-2, V-5 (génération 2), V-7 : manques |
| complet, `lecture_selection` retirée | **C1** | V-1 : manque → C5 |
| complet, `archives_de_jugement["2"]` retirée | **C1** | V-2 : manque → C5 |
| complet, `lu_sur_disque` autre ou absent | **C1** | V-4 → C4 (absent : voir CLB-09) |
| complet, aucun appel en génération 2 ; un seul en génération 1 | **C1** | V-5 : manque → C5 |
| complet, texte reçu autre que le texte bâti | **C1** | V-5 : écart → C4 |
| complet, deux appels du même proposeur | **C1** | V-5 à la lettre actuelle : ambigu (CLB-09) |
| complet, sélection finale `lu` ≠ `bilan_sha256` | **C1** | V-6 : écart → C4 |
| complet, `retenues["2"]` retirée | **C1** | V-7 : manque → C5 |
| complet, sélection de la génération 1 vidée de façon cohérente | **C1** | V-8 : vide → nœud NL-1 |

Les cas de CLV66-02 et CLV66-03 sont donc fermés par le texte. V-3 se lit sur `releve.arret` (« PlanteeSansArchive : … », cœur l. 593) et `generations_jouees` = [1] : faisable ; non atteignable par le cœur gelé (je rejoins la contre-lecture du code). Conseil, hors texte : que le lecteur du verdict joue les huit vérifications par un petit programme dont il verse l'empreinte (ma sonde peut servir de modèle).

## 4. Mandat 3 — commandes (12.4) et préalables (12.3)

Exact contre le lanceur et la configuration v6 : options de la commande réelle (lanceur l. 343-356, 407-410) ; `--releve-sha256` exigé ; `--utilisateur-bac 64097` ; chemin et nom du texte ; `--go` égal à celui du plan ; ordre des préalables 4 et 5 (le GO est vérifié avant la machine, lanceur l. 424-436 : Q-3 du journal est juste) ; sceau écrit par `controle_ia.scellement` accepté par `pole.outils.verifier_scelle` (essayé) ; neuf fichiers d'essais, banc, essai à blanc : conformes au rapport du développeur, section 7. `--collisionneur` et `--sha-collisionneur` : conformes à la commande v6 (l. 232, 585-586).

Inexact ou manquant : CLB-01 (environnement du lanceur, garde 15), CLB-02 (chemin réel de la sortie), CLB-05 (relais : Kimi absent du texte, options exigées, `--max-appels`, plafond « au plus égal »), CLB-08 (compagnon de l'héritage). Q-5 du journal : à la lecture de `tour_ferme_v64.roles_reels` (lanceur v64 l. 311), la part de chaque relais est aussi transmise aux commandes par la porte « environnement » (`PLAFOND_ETAPE_USD`) ; je ne l'ai pas suivie plus loin. Ne pas toucher la configuration.

## 5. Mandat 4 — les deux nœuds, et les nœuds cachés

- **NL-1 : bien posé.** Les trois options sont réelles, la sonde de la contre-lecture du code et la mienne montrent le cas (C1 rendue, V-8 « vide »). Je rejoins la recommandation (b). À ajouter au mot demandé à Lazar : sous (b), ce que l'issue neuve ouvre et n'ouvre pas ; sous (a) comme sous (b), le couple de remplissage doit **réécrire** la fin de la ligne C1, non seulement remplacer le marqueur (CLB-04). Aucun cas voisin non couvert trouvé : avec au moins une carte retenue, les copies éprouvent la lecture sur un contenu, même si la génération 2 ne propose rien de lisible.
- **NL-2 : bien posé, et la ligne proposée est lue** (section 1). Deux précisions à porter à Lazar avec elle : CLB-10 (la ligne exige « machine validée par l'essai à blanc », alors que louer la machine pour cet essai se fait sous cette même ligne ; nommer le texte par son nom de fichier).
- **Nœud caché possible : P2** (CLB-03). Le couple que je propose garde le comportement du programme gelé (aucune issue changée) ; l'autre lecture (P2 exigée pour C1) est un changement de critère, donc un nœud.
- **Pas des nœuds, mais à dire à Lazar** (CLB-13) : le registre des GO entier et les clés des deux relais seront posés sur la machine louée ; trois lignes de GO de 45 USD nommeront l'organisme (la ligne neuve dit « ne se cumulent pas » ; rien dans le code ne l'impose).

## 6. Mandat 5 — Q-4, et les autres questions du journal

- **Q-4 : le validateur qui fait foi pour ce texte est le lanceur de l'organisme** (`lire_preenregistrement` : chemin et nom fixés, sceau, aucun marqueur, 98 empreintes, plan, jeu planté, entropie). `controle_ia.prereg` n'est sur aucun chemin de cette course ; il refuse ce texte (huit « section absente », titres numérotés et libellés autres : essayé), comme il refuse le texte scellé d'A1-v3 archivé dans `prereg/` (essayé), précédent consigné en R-1562 et R-1609. Sceller par `controle_ia.scellement sceller`, ne pas renommer les sections (le code gelé et les contre-lectures citent leurs numéros). **À écrire au registre et au candidat**, parce que le précédent inverse existe pour un texte du programme (R-357 : refus de `sceller_prereg` jugé bloquant) : la règle « validateur du lanceur » ne vaut que pour les textes de l'organisme lus par son lanceur. La complétude R1 que `controle_ia.prereg` contrôle par les titres est contrôlée ici à la main (section 2) ; la section 15 doit porter l'empreinte du brouillon relu et celle de ce rapport (CLB-04).
- **Q-1** : garder V-5 à V-7 et `lu_sur_disque` (essayés, section 3.2 ; coût nul). **Q-2** : alignements, oui, sauf B2-24 à B2-28 qui sont des ajouts de lecture (section 2), fondés. **Q-3** : ordre juste. **Q-5** : configuration intacte ; plafond des relais **égal** à la part (CLB-05). **Q-6** : fait (section 1). **Q-7** : garder ; les quatre références sont celles que N-064 (point 4) exige, aucun chiffre n'en est tiré.

## 7. Constats

Gravité : **B** bloque le scellement en l'état ; **C** à corriger avant le scellement ; **m** mineur ; **i** information.

### CLB-01 (B, section 12.4 ; vérifié au code et par sonde) — la commande « exacte » est refusée par la garde 15

`tour_ferme_v64.exiger_machine_jetable_reel` (lanceur v66 l. 438) passe l'environnement du processus à `exiger_machine_jetable_v56` : `POLE_MACHINE_JETABLE_V56=1` exigée, et tout autre nom de variable dans une liste blanche fermée (`pole/etage_entre_generations_v56.py`, `NOMS_PERMIS` ; la configuration v6 n'ajoute rien). Le brouillon 2 ne nomme la variable nulle part (ni le rapport du développeur ni les contre-lectures du code). Telle qu'écrite, la commande est refusée (code 2, avant tout appel) ; une session superutilisateur ordinaire porte en plus des noms hors liste. Un texte scellé dont la commande exacte ne peut pas être jouée oblige à s'en écarter au lancement. **Couples CLC-01 et CLC-02** (préfixe `env -i`, noms tous dans la liste ; non joué sur une machine à `bwrap` : le point 5 de 12.3 le confirme).

### CLB-02 (C, section 12.3 ; trouvé en jouant les essais) — un chemin de sortie peut arrêter la course après les appels payés

Le dossier fermé de la tranche (créé sous `SORTIE/generation-<g>/`) est refusé si son chemin réel contient un fragment de `pole/ideation.py`, `FRAGMENTS_PIECES_INTERDITS` (« donnees », « banque », « prereg », « test-final », …). Le refus tombe dans l'étage, **après** les appels des proposeurs et le jugement : arrêt, code 3, C5, et une reprise demande un texte neuf. Preuve : mon bac à sable s'appelle `cl-prereg-course-v66` ; les 74 essais qui jouent une course y échouent sur « EtageRefuse : tranche exploratoire refusée avant tout appel : dossier fermé refusé ('prereg') » (142 occurrences), les 53 autres passent. **Couple CLC-03** (point 7 : dossiers frères, fragments nommés) et CLC-01.

### CLB-03 (B, section 8 ; R1) — P2 a une réfutation et aucune ligne de lecture

Section 4.1 : P2 (« V1 et V2 promues puis survivantes chacune », 1 000 sur 1 000, réfutation « l'une manque »). Section 8 : aucune ligne ne dit ce qu'une P2 manquée fait ; C1 ne demande que P1, P4, P6. Le programme calcule `p2_v1_v2` et n'en fait rien. Une P2 manquée sous une chaîne correcte est aussi improbable qu'une P1 manquée : le texte doit dire d'avance comment elle se lit. **Couple CLC-04** (issue inchangée, mention en tête, audit A3 pour la vraie manquante) : c'est le comportement du programme gelé, écrit. Si la mère veut qu'elle interdise C1 : nœud.

### CLB-04 (B, plusieurs sections ; à faire au candidat) — passages que le remplissage des marqueurs laisserait périmés

Le journal prévoit de remplir les marqueurs « par un couple déclaré ». Remplir ne suffit pas : un texte scellé ne peut pas dire que sa propre issue « attend la décision de Lazar ». À réécrire au candidat, une fois les mots reçus (lignes du brouillon 2) :

1. titre et statut (l. 1 à 13) : « brouillon 2 », « non contre-lu », « marqueurs restants », « aucune course réelle avant (i) à (iv) » ;
2. l. 28 : empreinte de `registres/go.md` (elle change à l'inscription de la ligne neuve) ; l. 31-33 et section 13 : mot de Lazar, verbatim, heure relevée ;
3. section 0, points 6 et 8 (l. 131-138) : « attend un nœud de Lazar », « ce qui manque avant de sceller » ;
4. section 8, ligne C1 (l. 456) : toute la fin, depuis « l'issue de ce cas attend » ; ligne V-8 (l. 472) : « issue du cas : nœud NL-1 » ;
5. section 11 (l. 538) et section 14 (l. 656-657) : renvois au « nœud NL-1 » ;
6. section 12.1 (ligne D1, D2, D3) et section 12.2, points 1 à 3 : faits, non plus à faire ;
7. section 15 : « Du texte : à faire » devient l'entrée de cette contre-lecture, avec l'empreinte du brouillon relu (`f87ad0e4…`), le chemin et l'empreinte de ce rapport, le traitement de CLB-01 à CLB-13, et la règle de Q-4 ;
8. trois occurrences de `GO_COURSE_V66` (l. 615, 637, 808) : même identifiant, de la forme `GO-AAAA-MM-JJ-NN`.

Le texte obtenu est à repasser au lanceur (`--verifier-seulement` depuis une copie, comme en section 1) et à une vérification courte du différentiel avant scellement.

### CLB-05 (C, section 12.3, point 6) — relais : Kimi absent, options exigées, nombre d'appels, plafond

(a) Le relais Kimi n'est pas nommé : c'est `docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v3.py` (`d54ed2bce54f5c89e9f078d1a03b5d8159894d6565ae560c3601c1e63ca76239`), hors du dossier de course ; son port par défaut n'est pas 8804 ; il exige `--modeles-permis`, `--plafond-usd` et trois prix (l. 748-750). (b) **Son `--max-appels` par défaut est 64** (l. 139), sous le nombre d'appels du devis quand chaque test prend ses tours ; au-delà le relais refuse (429) et la commande v6 sort en code 3 : arrêt de la course. (c) `servir` d'Argon exige `--port`, `--plafond-usd`, `--max-appels`, `--journal` (commande v6 l. 580-583). (d) « au plus égal à la part » permet un plafond de relais plus bas que la part, donc un arrêt par défaut de plafond que le devis (section 5) exclut : écrire « égal ». (e) Qui pose les clés, et où : dans l'environnement des relais seulement (le lanceur refuse toute variable de clé, `roles_reels` l. 283-286). **Couple CLC-03.** Les valeurs de `--max-appels` et des prix restent à fixer par la mère (je n'écris aucun chiffre non vérifié dans le texte).

### CLB-06 (C, section 8) — les écarts que le programme écrit sont plus nombreux que ceux que la ligne C4 nomme

`p6_ecarts` (lecture l. 130-188) écrit aussi : incident consigné des gardes 7, 21, 23 ; vue servie en génération 1 autre que {K1} ; retenues lues autres que les retenues écrites ; copie d'une carte non retenue ; loi plantée retenue ; relecture finale refusée. La parenthèse de la ligne C4 ne les nomme pas tous, et le texte « prime » : un lecteur pourrait lire une divergence là où le programme est plus strict que la lettre. **Couple CLC-05.**

### CLB-07 (m, section 10) — deux lettres de la liste d'arrêt

Garde 21 : « refus » ; au cœur v66 c'est un arrêt après la génération 1, incident consigné (l. 566-571), lu C5 et « C4 (partielle) ». Garde 18 : « archive plus petite » ; le code arrête sur tout autre nombre de membres (l. 117). **Couples CLC-06 et CLC-07.**

### CLB-08 (C, section 12.4 ; essayé) — le compagnon de l'héritage de départ

Sans `heritage-depart-v65.json.sha256` à côté du fichier, la garde 17 refuse (« sceau compagnon absent ou faux », code 2). Le texte ne nomme que le fichier. **Couple CLC-01.**

### CLB-09 (m, section 8) — lettre de V-4 à V-6

V-5 : « deux appels (Kimi, Argon) » ne dit pas qu'il en faut un par proposeur (champ `proposeur`, `kimi` et `argon` en mode réel : lanceur v64 l. 301). V-4 à V-6 : un champ à comparer absent est-il un manque ou un écart ? **Couples CLC-08 et CLC-09** (manque, C5).

### CLB-10 (C, nœud NL-2 ; hors texte) — la ligne de GO proposée

Lue par la garde et par le lanceur (section 1). À préciser dans le mot demandé à Lazar : (a) la ligne pose « machine jetable à bwrap validée par l'essai à blanc » parmi les conditions « toutes exigées », alors que la location de la machine, l'essai à blanc et les préalables 1 à 5 se font sous cette ligne : écrire que la machine se loue dès le scellement du texte et que les conditions valent pour les appels de modèles ; (b) nommer le texte (`preenregistrement-boucle-reelle-organisme-v1-v<N>.md`) ; (c) le fournisseur de la machine, si Lazar veut le garder (GO-2026-11-10-10 nommait Hetzner CPX32). Ne pas mettre de barre verticale ni commencer le périmètre par « extension ».

### CLB-11 (m, sections 3.7 et 10) — garde 22, deux nuances

L'identité comparée par le lanceur est celle **réglée** sur l'exécuteur sondé ; la mesure sur l'hôte (propriétaire du fichier témoin) est faite par la sonde (`controler_hote_apres_sonde`). L'ordre réel est : texte, monde, empreinte de la configuration, GO, contenu de la configuration, garde 17, garde 22, sonde, garde 15, rôles. Sans effet sur une issue ; à dire si le candidat est retouché à cet endroit.

### CLB-12 (i) — essais ciblés non rejouables depuis le bac à sable imposé

Section 9. La mère peut rejouer les mêmes classes depuis une copie dont le chemin ne porte aucun fragment refusé.

### CLB-13 (i) — à dire à Lazar, sans nœud

Registre des GO entier et clés des relais sur la machine louée ; trois lignes de GO de 45 USD pour l'organisme, non cumulables par le seul mot de la ligne neuve.

## 8. Couples exacts (CLC-01 à CLC-09)

Chaque texte ancien est présent exactement une fois dans le brouillon 2 (`f87ad0e4…`) au moment de son application, dans l'ordre ; texte obtenu : `b19db56e58302d57ee3d1aa114a6038f9aceb54b93b233930da513d7b4846cc6` (deux marqueurs restants, les mêmes) ; ce texte, marqueurs remplis de valeurs d'essai, passe le lanceur jusqu'à la garde 22. CLC-04 et CLC-05 touchent la section 8 (gelée) ; CLC-06 et CLC-07, la section 10 (gelée) ; CLC-08 et CLC-09, la section 8. Aucun ne touche une hypothèse, un seuil ni un signe.

```json
{
 "objet": "couples CLC-01 à CLC-09 de la contre-lecture 1 du brouillon 2 (f87ad0e4…)",
 "couples": [
  {
   "id": "CLC-01",
   "section": "12.4",
   "constat": "CLB-01, CLB-02, CLB-08",
   "ancien": "`DOSSIER_COURSE` = le dossier `configuration-v6/` versé, avec `heritage-depart-v65.json` ; `CHEMIN/registres/go.md` = la copie\ndu point 4 de la section 12.3 :",
   "nouveau": "`DOSSIER_COURSE` = le dossier `configuration-v6/` versé, avec `heritage-depart-v65.json` **et son compagnon\n`heritage-depart-v65.json.sha256`** (sans lui la garde 17 refuse, code 2) ; `CHEMIN/registres/go.md` = la copie\ndu point 4 de la section 12.3 ; `SORTIE` = un dossier neuf, frère de `SORTIE_ESSAI` (section 12.3, points 3 et 7).\n**Environnement du lanceur (garde 15)** : `POLE_MACHINE_JETABLE_V56=1` est exigée, et tout autre nom de variable doit\nêtre dans la liste blanche fermée de `pole/etage_entre_generations_v56.py` (`NOMS_PERMIS` ; la configuration v6 n'en\najoute aucun) ; aucune variable de clé (les relais tiennent les clés). D'où le préfixe `env -i` des deux commandes du\nlanceur, dont tous les noms sont dans la liste ; le point 5 de la section 12.3 le confirme sur la machine :"
  },
  {
   "id": "CLC-02",
   "section": "12.4",
   "constat": "CLB-01",
   "ancien": "```\npython3 -I -B demonstrations/boucle_reelle_v66.py SORTIE --preenregistrement prereg/",
   "nouveau": "```\nenv -i PATH=/usr/sbin:/usr/bin:/sbin:/bin HOME=/root LANG=C.UTF-8 TMPDIR=/tmp POLE_MACHINE_JETABLE_V56=1 \\\npython3 -I -B demonstrations/boucle_reelle_v66.py SORTIE --preenregistrement prereg/"
  },
  {
   "id": "CLC-03",
   "section": "12.3",
   "constat": "CLB-02, CLB-05",
   "ancien": "Chaque relais\n   local est lancé avec un plafond au plus égal à la part de son fournisseur (Kimi 33 USD, Argon 7 USD) ; valeurs notées au\n   rapport de course.",
   "nouveau": "Options exigées de\n   `servir` : `--port 8805`, `--plafond-usd`, `--max-appels`, `--journal`. Le relais Kimi (port 8804, à donner par `--port` :\n   son défaut est un autre port) est `relais_kimi_v3.py` (`d54ed2bce54f5c89e9f078d1a03b5d8159894d6565ae560c3601c1e63ca76239`,\n   dépôt de travail, `docs/notes/ideation-organisme-v1/relais-kimi-v1/`), hors du dossier de course ; il exige\n   `--modeles-permis`, `--plafond-usd` et ses trois prix, et son `--max-appels` par défaut est plus petit que le nombre\n   d'appels attendu si chaque test prend ses tours : il se donne toujours. Chaque relais est lancé avec un plafond **égal**\n   à la part de son fournisseur (Kimi 33 USD, Argon 7 USD : un plafond plus bas pourrait arrêter la course par défaut de\n   plafond, ce que le devis exclut) et un `--max-appels` au moins égal au nombre d'appels de son pire cas (devis,\n   section 3.4), sans quoi un refus du relais arrête la course (code 3). Les clés ne sont posées que dans l'environnement\n   des relais, jamais dans celui du lanceur ni dans un fichier. Valeurs notées au rapport de course.\n7. `SORTIE_ESSAI` (point 3) et `SORTIE` (section 12.4) sont deux dossiers neufs du même dossier parent, et `TMPDIR` vaut\n   `/tmp` : le chemin réel d'un dossier de sortie ne doit contenir aucun des fragments que refuse le dossier fermé de la\n   tranche (`pole/ideation.py`, `FRAGMENTS_PIECES_INTERDITS` : « donnees », « mode-tenu-a-l-ecart », « bras-attaque »,\n   « bras-d-attaque », « carte-des-hypotheses », « carte-hypotheses », « internes-des-moniteurs », « banque », « prereg »,\n   « test-final » ; chemin lu en minuscules, sans accents, `_` et espace lus `-`). Sinon l'étage refuse la tranche **après**\n   les appels payés des proposeurs : arrêt, code 3. L'essai à blanc du point 3, joué à côté de `SORTIE`, le montre sans\n   dépense."
  },
  {
   "id": "CLC-04",
   "section": "8",
   "constat": "CLB-03",
   "ancien": "Mesures sans issue : P3 (puissance aux vraies faibles), P7 (cartes réelles), coût, recherche de la loi plantée.",
   "nouveau": "Mesures sans issue : P3 (puissance aux vraies faibles), P7 (cartes réelles), coût, recherche de la loi plantée. **P2\nmanquée alors que P1 tient** (V1 ou V2 non promue, ou promue sans survivre) ne change pas l'issue ; elle s'écrit en tête du\nrapport, avant la phrase de résultat, et déclenche l'audit A3 pour la vraie manquante (non promue, promue non\nsurvivante, ou non concluante)."
  },
  {
   "id": "CLC-05",
   "section": "8",
   "constat": "CLB-06",
   "ancien": "**Les issues sont celles de ce texte.** Avant\nd'écrire l'issue",
   "nouveau": "**Les issues sont celles de ce texte.** Tout écart que le\nprogramme écrit dans `ecarts_p6` (incident consigné des gardes 7, 21 ou 23 ; héritage ou relecture finale refusés ;\nempreinte, vue lue, vue servie, retenues lues, archive ou nombre de membres d'archive de la génération 2 en écart ; copie\nd'une carte non retenue ; loi plantée retenue) est un écart de P6 au sens de la ligne C4 ; les vérifications V ne peuvent\nqu'en ajouter. Avant\nd'écrire l'issue"
  },
  {
   "id": "CLC-06",
   "section": "10",
   "constat": "CLB-07",
   "ancien": "| copie d'une carte non retenue → refus |",
   "nouveau": "| copie d'une carte non retenue → arrêt, code 3, incident consigné, lu C5 et « C4 (partielle) » |"
  },
  {
   "id": "CLC-07",
   "section": "10",
   "constat": "CLB-07",
   "ancien": "loi plantée jugée avec 0 membre ou avec une archive plus petite → arrêt, code 3",
   "nouveau": "loi plantée jugée avec 0 membre ou avec un autre nombre de membres que celui de l'archive de sa génération → arrêt, code 3"
  },
  {
   "id": "CLC-08",
   "section": "8",
   "constat": "CLB-09",
   "ancien": "`vues_servies[g].appels` porte deux appels (Kimi, Argon) et chaque `texte_recu_sha256` = `vues_servies[g].texte_sha256` | moins de deux appels : manque, C5 ;",
   "nouveau": "`vues_servies[g].appels` porte deux appels, un par proposeur (champ `proposeur` : `kimi` et `argon`, une fois chacun), et chaque `texte_recu_sha256` = `vues_servies[g].texte_sha256` | moins de deux appels, ou un proposeur absent : manque, C5 ;"
  },
  {
   "id": "CLC-09",
   "section": "8",
   "constat": "CLB-09",
   "ancien": "qu'il produit, et empêchent une lecture à vide si l'un d'eux se produisait quand même :",
   "nouveau": "qu'il produit, et empêchent une lecture à vide si l'un d'eux se produisait quand même. Dans V-4, V-5 et V-6, un champ à\ncomparer qui est absent ou nul compte comme un manque (C5), non comme un écart :"
  }
 ]
}
```

## 9. Limites et expositions déclarées

- **Essais ciblés.** La consigne fixe mon bac à sable à un dossier dont le nom contient « prereg », fragment que le dossier fermé refuse dans un chemin. Les essais qui jouent une course y échouent tous pour cette raison (74 en échec, 53 passés, 1 sauté, deux passages égaux). Je n'ai pas déplacé le dossier provisoire hors du chemin nommé par la consigne. Les gardes dont l'essai est une course entière ne sont donc attestées ici que par la lecture du code, par le nom de l'essai et par la suite rejouée à l'identique par la contre-lecture du code v66.
- **Non éprouvé** : tout ce qui demande `bwrap` (garde 22 au-delà du refus, garde 15 en situation, rôles réels, `--verifier-seulement` jusqu'au bout) ; le préfixe `env -i` de CLC-02 n'a été confronté qu'à la fonction de la garde 15.
- **Non relu** : les PDF des quatre références de N-064 ; le code des adaptateurs au-delà de `roles_reels` ; le collisionneur v7 (non ouvert).
- **Expositions.** Mes recherches dans `registres/decisions.md` (fichier nommé, lignes R-1738, R-2206, R-2215, R-2234, R-2243, R-2244, R-2248 et la question du validateur) ont affiché des fragments d'autres lignes (R-244, R-287, R-291, R-295, R-297, R-299, R-356, R-357, R-1562, R-1609, R-1889, R-2046, R-2053, R-2064, R-2065, R-2068, R-2213, R-2245) ; j'en reprends R-357, R-1562, R-1609 (Q-4) et R-2053 (version du contre-lecteur), rien d'autre. Aucune valeur d'une sonde de 7a n'a été sous mes yeux. Une liste de noms de fichiers suivis a été demandée avec `docs/notes/bras-attaque`, `diag`, `runs` et `donnees` exclus.

## 10. Points ouverts pour la mère

1. Porter NL-1 et NL-2 à Lazar, NL-2 avec les précisions de CLB-10.
2. Trancher CLB-03 : couple CLC-04 (routine) ou P2 exigée pour C1 (nœud).
3. Appliquer CLC-01 à CLC-09 ; fixer `--max-appels` et les prix des relais (CLB-05).
4. Écrire le candidat (CLB-04), le repasser au lanceur depuis une copie, puis vérification courte du différentiel.
5. Consigner la règle de Q-4 au registre.
