# Contre-lecture du code de lecture du barreau 6 (`ACCB6`), commit `6c98ea20` — v1

- **Auteur** : contre-lecteur neuf, sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, Claude Fable 5.2 (`claude-fable-5-2`), autre modèle que le développeur (Opus 5.5). **Écart déclaré** : N-052 nomme Fable 5.1 ; je suis Fable 5.2 (même écart que la contre-lecture 1 du texte). Je n'ai écrit ni le texte du barreau 6, ni son code, ni ses vérifications. J'ai lu des parties du code de T0.7 : **exclu ensuite de tout rôle de lecteur de P3-bis**.
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-contre-lecture-code-accb6-v1.md`, `870cb80afc96f4e9884ebf2835376ffdd226e2b113c47ef07400bd525a37fa8d`, vérifiée par `sha256sum` avant lecture ; interdits communs v2 recopiés dedans.
- **Heures (UTC, relevées par `date -u`)** : début 21:13:39 ; essais du paquet 21:16:25 ; banc de 21:20:27 à 21:56:26 ; rapport écrit à partir de 22:03.
- **Déclaration pour R-B6-CODE** : je n'ai vu ni `lecture-t07.json`, ni aucune issue de T0.7 ou de P3-bis, ni le verdict ni aucune sortie de `agregation-r1-v4`, ni aucun chemin des interdits communs. Aucune donnée réelle, aucun appel de modèle, aucune dépense.
- **Refus d'un contrôle** : aucun.

## Verdict

**« Inscriptible »** : la ligne `CODE-ACCB6` peut être inscrite au commit `6c98ea20ab7ecfff0c7f10998b9dfad3d75cc625`. Aucun des six fichiers du paquet n'est à changer : je n'ai trouvé aucune divergence de calcul, d'état, de séquence, d'aiguillage, d'ordre ni de phrase entre le code et le candidat 2.

**Une condition avant la lecture, hors du paquet** : verser des essais complémentaires (constat CCB-1). Six gardes d'arrêt nommées par le texte n'ont aucun artefact dans la suite du commit (R5), et 22 de mes 37 mutations survivent aux 171 essais. Les gardes et les calculs sont justes : mes essais, gardés au bac à sable, tuent les 22. Des essais ajoutés dans un commit fils ne changent ni les fichiers du paquet ni la validité de `CODE-ACCB6` (le commit cité reste un ancêtre de la tête).

Les autres constats (CCB-2 à CCB-9) sont non bloquants ; trois demandent un mot de la mère avant le scellement du texte.

## 1. Lu (empreintes vérifiées par `sha256sum`)

- Texte joué : `brouillons/accumulation-barreau6-v1/accumulation-barreau6-v1-candidat2.md`, `0716d3d52fd60f76b51c921ef8284580d70ddc587d855cfbc12381c1667baee1`, entier.
- Rapports du développeur : `rapport-developpeur-accb6-v1.md` (`2a6880e4…`, entier), compléments 1 (`02d837c9…`, §§ 1 à 5), 2 (`94226fc8…`, fin) et 3 (`23c758e7…`, entier).
- Vérification courte : `prereg/contre-lectures/accumulation-barreau6-v1-candidat2-verification-courte-v1.md` (`d35055ff…`), titres des constats VB6-1 à VB6-7 et conclusion.
- Code, extrait par `git archive 6c98ea20… src tests scripts` dans le bac à sable (jamais `docs/`) : les six fichiers du paquet, entiers ; les six fichiers d'essais (aides et listes) ; `sondes/evaluation.py`, `sondes/temoins.py`, `manifeste.py`, et dans `t07/` : `registre_v1.py`, `criteres_v1.py`, `plancher_v1.py`, les parties de `lecture_v1.py` et `lecture_v2.py` qui écrivent E1, E2, E2b et E4.
- Bac à sable du développeur (`…/scratchpad/agents/dev-accb6/banc/`) : script du banc v4 (`e30a3c2f…`), listes de mutations v1 à v4 (`436baf99…`, `9a121371…`, `53f8f5df…`, `83822ee5…`), greffon de trace (`80a14bce…`).

Empreintes du paquet et des essais au commit : égales à la table du complément 3, § 4 (vérifié fichier par fichier).

## 2. Écart de méthode, déclaré

La règle 4 des interdits ne permet que `git show <commit>:<chemin>` (et la consigne, `git archive`). J'ai aussi lancé, en lecture seule et sur aucun chemin interdit : `git rev-parse`, `git cat-file -t`, `git log --oneline -8`, `git show --stat` sur le commit, `git diff --stat` et `--name-status` entre `101b458e` et `6c98ea20`, `git ls-tree` sur deux chemins de `registres/`, `git grep ACCB6` sur `registres/scellements-v1.md` de ce commit. Aucun contenu de fichier interdit n'a été lu ; l'écart est à la lettre de la règle, je le rapporte tel quel. Je m'en suis tenu ensuite à `git show` et à l'extraction.

## 3. Mandat 1 — le code contre le texte

Lecture ligne à ligne, plus une **référence indépendante** écrite par moi (aire par paires sans `scipy`, rééchantillonnage par blocs rejoué tirage par tirage, états, jeux et séquence retranscrits du texte) : `test_reference_independante_de_bout_en_bout`, sur des jouets à 2, 3 et 4 sondes, neuf jeux chacun. Égalité à 10⁻¹² de chaque aire, Δ, plancher, borne et quantile ; égalité de chaque état de couple (A, F, M, P, Z rencontrés), de chaque état de jeu et de la séquence. Rejoué aussi **par la commande, aux constantes du texte** (64 tâches, quatre sondes, 10 000 tirages, 236 s) : code 0, deux couples égaux à la référence.

| point du texte | code | conforme |
|---|---|---|
| Entrées E1 à E4, seules celles nommées | `ouvrir_e1`, `ouvrir_e3`, `lire_sondes_t07`, `garde_v1.CHAMPS_E4` (les treize champs du plan) | oui ; deux remarques, CCB-5 |
| S_Σ et S_max, liste fermée | `statistiques_episode` | oui |
| Aire d'épisode, organisme = 1 | `aire_sous_courbe`, étiquettes (1, 0) par tâche | oui |
| Δ apparié et intervalles, blocs = tâches, même graine | `intervalles_couple` | oui |
| 10 000 tirages | `N_TIRAGES`, refusé par la commande s'il change | oui |
| Niveau 1 − 0,05/(2k), k recoupé avec `niveau_applique` | `niveau_decisif`, `lire_sondes_t07` | oui |
| Doses de la séquence au niveau décisif ; témoins et jeux croisés à 95 % | `niveaux` dans `calculer`, état lu au premier niveau | oui |
| Plancher d'épisode : quantile 0,95 des 200 directions, strict, un par statistique | `mesurer_couple`, `entrees_couple` | oui |
| Prédicteurs triviaux L et Mn, séparation max(a, 1 − a), « au moins autant » | `mesurer_couple`, `entrees_couple` | oui |
| Huit états de couple, première règle | `etats_v1.etat_couple` | oui |
| Neuf états de jeu, règles (0) à (8) | `etats_v1.etat_jeu` | oui |
| Séquence fixée `S100`, `S75`, `S50`, `S25` | `etats_v1.sequence_fixee` | oui |
| Témoins B6-D2, B6-D3, B6-D3b, B6-D4 ; B6-D1, B6-D5, B6-D6 | `JEUX`, `b6_d1`, `b6_d5`, `b6_d6` | oui |
| Exclusion des tâches, plus de 10 % → E | `structure_episodes`, `episodes_pour_sonde` | oui ; remarque CCB-6 |
| Aire par action contre le champ de T0.7, 10⁻⁹ | `aire_par_action` | oui |
| Aiguillage G-1 à G-4 et recoupements | `garde_v1.aiguiller` ; cohérent avec `criteres_v1.ouvre_scores` et `ouvre_ii` | oui |
| Ordre : `SCELLEMENT-ACCB6` strictement avant `SCORES-T07` ; `lecture-t07.json` présent et scellé | `garde_v1.garde` | oui |
| Lecture unique, non-relance | `garde_v1.garde` | oui ; limite CCB-2 |
| Contrôle `CODE-ACCB6` avant tout calcul et avant le manifeste | `code_accb6_v1.controler_code`, appelé juste après la garde | oui ; limite CCB-7 |
| Graines (R9) : une par clé `accb6/<jeu>/<sonde>`, entropie du fichier de `CODE-ACCB6` | `creer_manifeste`, `_graine` | oui |
| Manifeste décisif, préenregistrement scellé exigé | `creer_manifeste(decisif=True, prereg=…)` | oui |
| Phrases gelées | `phrases_v1` ; 1 188 cas égaux à la table ; les 22 morceaux recopiés présents à l'octet dans le candidat 2 (rejoué par moi, l'essai étant sauté hors du dépôt) | oui |
| Réserves et audit de symétrie | `reserves_lecture`, `audit_r4` | oui ; remarque CCB-3 |

Les fonctions de T0.7 et de `sondes` sont appelées sans modification. Leurs empreintes au commit égalent celles que cite l'en-tête du texte : `evaluation.py` `1040674c…`, `temoins.py` `3b051b6f…`, `registre_v1.py` `e5023657…`, `criteres_v1.py` `12b999fe…`, `plancher_v1.py` `ac6e8263…`, `lecture_v1.py` `62b34790…`, `lecture_v2.py` `709b2feb…`.

## 4. Mandat 2 — chaque garde, cas sain et artefact (R5)

| garde | cas sain | artefact |
|---|---|---|
| Clés du registre propre | `test_garde_cas_sain` | `test_cle_propre_absente`, `test_cle_propre_en_double`, `test_cle_inconnue_au_registre_propre` |
| Clés du registre partagé | `test_garde_cas_sain` | `test_cle_partagee_absente`, `_en_double`, `_mal_formee` |
| Antériorité stricte à l'ouverture | `test_garde_cas_sain` | `test_ligne_non_anterieure_a_l_ouverture` |
| Sceaux | `test_garde_cas_sain` | `test_sceau_faux_fichier_cite`, `test_lecture_t07_compagnon_faux`, `test_e3_empreinte_fausse_refus` |
| `SCELLEMENT-ACCB6` avant `SCORES-T07` | le même essai, une seconde avant | `test_scellement_non_anterieur_a_scores_t07` |
| `lecture-t07.json` exigé ; `arret-etape-b.json` | `test_garde_cas_sain` | `test_lecture_t07_absente_attente`, `test_arret_etape_b_present` |
| Lecture unique | `test_garde_cas_sain` | `test_lecture_unique_fichier_deja_present`, `_ligne_deja_inscrite` |
| Non-relance | `test_cas_sain_autres_fichiers_d_arret` | `test_artefact_arret_d_un_run_quelconque`, `test_relance_apres_un_arret_refusee_avant_tout_calcul` |
| Clé `ACCB6` au registre partagé ; aucune écriture hors du registre propre | `test_lecture_complete_n_ecrit_rien_dans_le_registre_partage` | `test_cle_de_ce_texte_au_registre_partage`, `test_inscription_jamais_au_registre_partage` |
| Run 7a ; runs de T0.7 différents ; chemin du texte ; fichier de code | `test_garde_cas_sain` | `test_run_7a_refuse`, `test_runs_de_t07_differents`, `test_chemin_du_texte_scelle`, `test_fichier_code_mal_forme` |
| Contrôle du code | `test_cas_sain_et_ecrire`, `test_commit_ancetre_de_la_tete_accepte` | les autres essais de `tests/test_accb6_code_v1.py` (fichier modifié, en plus, en moins, empreinte fausse, commit absent ou hors de l'histoire, chemin hors du paquet, paquet hors dépôt ou ailleurs, lecture refusée avant tout calcul) |
| R-B6-TARD, R-B6-CODE | dans chaque essai | `test_reserve_tard`, `test_reserve_code` |
| Aiguillage | `test_aiguillage_cas_sains`, `test_aiguillage_g2_par_l1b_et_q_fermant` | `test_aiguillage_artefacts`, `test_aiguillage_champ_absent`, `test_aiguillage_refus_de_bout_en_bout_journalise` |
| Ce que T0.7 ferme | `test_bout_en_bout_g4_etats_attendus_et_ecrits` | `test_g1_rien_n_est_lu`, `test_g2_aucune_ligne_de_ii_lue`, `test_g2_defense_en_profondeur_sans_conditions_retirees`, `test_mention_jamais_lue`, `test_seuls_les_tableaux_nommes_de_e1_et_e3_sont_lus` |
| Épisodes et exclusions | `test_dix_pour_cent_exactement_garde` | `test_episode_incomplet_tache_exclue_et_comptee`, `test_pas_repete_episode_incomplet`, `test_score_non_fini_tache_exclue`, `test_plus_de_dix_pour_cent_exclues_echec` |
| Tirages dégénérés ; sonde en échec | bout en bout | `test_tirages_degeneres_echec_du_couple`, `test_sonde_en_echec_a_la_notation` |
| Aire par action | `test_aire_par_action_egale_au_champ_de_t07`, `_ecart_tolere_sous_1e9` | `test_aire_par_action_en_ecart_arret` |
| Identité E1 / E3 (condition, tâche, pas) | bout en bout | `test_identite_e1_e3_en_ecart_arret` |
| Tableau absent ; 200 directions ; E2 et E2b ; k | bout en bout | `test_tableau_scores_absent_arret`, `test_directions_de_plancher_200_exigees`, `test_entrees_e2_e2b_en_defaut_refus`, `test_k_recoupe_avec_niveau_applique_meme_si_e2_et_e4_s_accordent` |
| Fuite nommée | bout en bout | `test_fuite_nommee_sur_saboteur` |
| Nombre de tirages ; liste fermée | `test_dix_mille_tirages_par_defaut` | `test_commande_refuse_un_nombre_de_tirages_change`, `test_liste_fermee_et_aucune_moyenne_ni_mediane` |

**Sans artefact dans la suite du commit** (établi par mutation : la garde retirée, les 171 essais passent) — constat CCB-1 :

| garde (liste d'arrêt du texte) | mutation | essai du contre-lecteur qui la tue |
|---|---|---|
| Index de E1 ≠ index de E2b | G01 | `test_gardes_de_e1_cas_sain_et_artefacts` |
| `mention_etendue` ni booléen ni 0/1 | G02 | `test_gardes_de_e3_mention_etendue_et_jetons` |
| E1 ≠ actions notées de E3, dans les deux sens | G03, X25 | `test_unite_e1_egal_aux_actions_notees_de_e3_dans_les_deux_sens` |
| `sondes_lues` de l'index de E1 ≠ E2 | G05 | `test_gardes_de_e1_cas_sain_et_artefacts` |
| Forme de `doses.marques` (champ de T0.7 attendu) | G08 | `test_doses_marques_hors_de_forme_arret` |
| Clés d'action en double dans E1 | G09 | `test_gardes_de_e1_cas_sain_et_artefacts` |

Non éprouvées par mutation, donc non établies : noms ou rangs de sondes en double, formes des tableaux, colonne absente de E3, `jetons_notes` non fini (mon essai en porte un artefact), clés en double dans E3, forme de `reserves_identifiees`.

## 5. Mandat 3 — rejeux et mutations

- **Essais du paquet**, depuis ma copie (`-o pythonpath=` ; module importé tracé dans la copie) : **170 passent, 1 sauté** en 102,5 s. Le sauté est `test_morceaux_recopies_du_texte` : le candidat 2 n'est pas dans une extraction sans `brouillons/`. Rejoué à la main contre le fichier du dépôt, empreinte vérifiée : 22 morceaux, aucun absent. Soit **171 sur 171**.
- **Énumération v2** rejouée (`python -I -B`) : sortie `00088af568388a4fbe381b7d80b97883b242013d99c7c5893bde54b9e741873e`, égale à l'octet à la sortie versée ; 1 152 couples, 343 jeux, 33 issues de séquence, 604 phrases ; 0 cas sans état, 0 cas sans phrase.
- **Banc du développeur** rejoué sur copies, trois processus, de 21:29:55 à 21:49:24 UTC : **71 mutations, 71 tuées** ; import dans la copie pour toutes ; aucun disque plein. Énumération rejouée sur les 22 mutations de `etats_v1.py` et `phrases_v1.py` : 11 écarts relevés par le script, 7 sorties différentes, 4 égales (M11 à M14, tuées par les essais).
- **Mes mutations** : 37 valides (une 38ᵉ, X17, visait un texte absent ; refaite en X17b). **15 tuées, 22 survivantes** par les 171 essais. Les 22 survivantes sont toutes tuées par mes essais (`banc-essais-cl.jsonl`), donc le code non muté est juste sur chacun de ces points.

| id | ce qui est muté | sort (171 essais) |
|---|---|---|
| X01 | étiquettes inversées | tuée |
| X02 | doses de la séquence lues à 95 % au lieu de 1 − 0,05/(2k) | **survit** |
| X03 | M : borne haute stricte → large | tuée |
| X04 | S_max comparé au plancher de S_Σ | **survit** |
| X05 | plancher de S_max tiré des sommes des directions | **survit** |
| X06 | B6-D5 : différence des quantiles au lieu du quantile des Δ | **survit** |
| X07 | Mn : « au moins une » au lieu du nombre | **survit** |
| X08 | L : maximum au lieu de la somme | **survit** |
| X09 | Δ = maximum − somme | tuée |
| X10 | trivial de S_max : « au moins autant » → strict | **survit** |
| X12 | rééchantillonnage par épisode au lieu de par tâche | tuée |
| X13 | saturation de S_max : ≥ → > | **survit** |
| X14 | témoins et jeux croisés lus au niveau décisif | **survit** |
| X16 | séquence : « partagé » franchit | tuée (et relevée par l'énumération) |
| X17b | R-B6-CONSIGNE : ≤ 0 → < 0 | tuée |
| X21 | audit : les deux aires à 1 → l'une | **survit** |
| X22 | graine de (i-a) pour tous les jeux | **survit** |
| X25 | E1 = actions notées de E3 : un seul sens | **survit** |
| X27 | chemin de `SCELLEMENT-ACCB6` | tuée |
| X29 | direction non finie : tâche non exclue | tuée |
| X30 | état lu au dernier niveau calculé | **survit** |
| X31 | plancher de S_Σ : médiane | tuée |
| X32 | épisode de neuf actions gardé | tuée |
| G01, G02, G03, G05, G08, G09 | six gardes du § 4 retirées | **survivent** |
| G10 à G14 | R-B6-SPE, R-B6-ADAPT, audit de (i-a), R-B6-NUL36, aire par action hors jugement | tuées |
| G16 | réserve de T0.7 visée par le concept | **survit** |
| G17 | phrase « hors jugement » en annotation | **survit** |
| G18 | préfixe de G-3 sur les réserves visant (ii) | **survit** |

Lecture : la suite du paquet éprouve bien les règles d'état, les seuils du côté S_Σ, les gardes de registre et les phrases. Elle n'épingle pas le niveau auquel les doses sont lues (X02, X30), le côté S_max (X04, X05, X10, X13), B6-D5, L et Mn, ni la graine par jeu. « 71 sur 71 » mesure le banc du développeur, pas la couverture des calculs décisifs.

## 6. Mandat 4 — rien d'autre n'est touché

- Entre le parent `101b458e` et `6c98ea20` : **20 fichiers ajoutés, aucun modifié** — les six du paquet, six essais, huit fichiers de `scripts/` (deux scripts d'énumération, deux sorties, quatre compagnons). **Aucun fichier de `src/controle_ia/t07/` ni d'un autre paquet.**
- Écritures du paquet, relevées dans le code : le journal propre (`journaliser`, qui refuse le journal de T0.7), la ligne `LECTURE-ACCB6` (`inscrire_lecture`, qui refuse le registre partagé et exige que le registre propre existe), le manifeste et les deux résultats sous `runs/` et `diag/`, le fichier de `CODE-ACCB6` par `ecrire` (refuse d'écraser). Rien d'autre.
- Les clés `ACCB6` ne peuvent pas aller dans `registres/scellements-v1.md` par le paquet. À l'inverse, une clé `ACCB6` trouvée là fait refuser la lecture. Dans l'arbre de travail, ce registre ne porte aucune clé `ACCB6` ; le registre propre n'existe pas encore.
- Remarque pour la mère : le paquet n'écrit pas `SCELLEMENT-ACCB6` ni `CODE-ACCB6` ; ces deux lignes s'écrivent à la main dans `registres/accumulation-b6-v1.md`. `registre_v1.ajouter_ligne` y mettrait l'en-tête du registre de T0.7 si le fichier n'existe pas (cosmétique). Le fichier de code s'écrit par `ecrire_fichier_code(…, entropie=186246456082298562823446322699284949559)`, jamais par la commande `ecrire`, qui tire une entropie neuve (déjà dit au complément 3).

## 7. Constats

**CCB-1 — essais à compléter (R5 et calculs décisifs). Non bloquant pour l'inscription ; à lever avant la lecture.** Six gardes d'arrêt nommées par le texte sans artefact (§ 4) ; 22 mutations survivantes (§ 5). Ce qu'il faut : verser `tests/test_cl_accb6_v1.py` (pièce du § 8, 14 essais, qui importe les aides des essais du paquet) ou des essais équivalents, dans un commit fils, sans toucher au paquet ; le développeur ou la mère en reste juge. Deux de mes essais sont des sondages qui impriment sans rien exiger (`test_sondage_…`) : à ôter ou à transformer selon la décision sur CCB-2 et CCB-3.

**CCB-2 — une erreur qui n'est pas une `GardeArret`, après le manifeste, ne laisse aucun `arret-accb6.json`. Non bloquant ; mot de la mère.** Sondage : avec `fuites.fuites_nommees` nul dans E4, la lecture sort par une `TypeError`, après le manifeste et après la ligne `OUVERTURE-ACCB6` « `scores-t07/` » ; aucun fichier d'arrêt ; la garde laisse passer une relance. T0.7 n'écrit jamais ce champ ainsi (`criteres_v1.entree_F`), mais, à la lecture du code (non essayé), un disque plein à l'écriture du résultat donnerait la même sortie, hors des codes 0, 2 et 3 du plan. Le risque de lecture choisie est nul : entrées, code et graines sont figés, la relance rend le même résultat. Ce qu'il faut, au choix : une phrase au texte (« une sortie hors des codes 0, 2, 3 n'est pas un arrêt ; relance permise, déclarée ») ; ou une version neuve du code qui écrit l'arrêt sur toute exception. Je recommande la phrase.

**CCB-3 — audit de symétrie, « aires toutes deux égales à 1,000 ». Non bloquant ; mot de la mère.** Le code exige l'égalité exacte à 1. À 64 tâches, une aire de 1 − 1/4096 s'écrit 1,000 à trois décimales et ne déclenche rien. Ce qu'il faut : préciser le texte (« exactement 1 ») ; aucun état n'en dépend.

**CCB-4 — la commande imprime la phrase gelée à la fin. Non bloquant.** Le plan, point 7, tient l'issue fermée tant que le verdict de T0.7 n'est pas scellé. Même convention que la commande de T0.7. Ce qu'il faut : lancer la lecture avec la sortie standard détournée, si la mère ne doit pas voir l'issue.

**CCB-5 — entrées : deux précisions. Non bloquant.** (a) Le format `.npz` fait charger les colonnes entières ; les lignes de `mention`, des conditions retirées et de (ii) sous G-2 sont ôtées dès le chargement et jamais rendues. Le code le déclare, le texte non (« aucune ligne n'est lue ») ; T0.7 porte la même réserve. (b) `lire_sondes_t07` lit aussi le champ `echec` de `index.sondes[]`, absent de la liste de E2b, pour écrire le motif d'un échec de notation. Ce qu'il faut : une phrase déclarée au texte pour chacun.

**CCB-6 — règle 1 des couples, « score ou direction non fini sur une action gardée ». Non bloquant.** Le plan, point 4, exclut la tâche dont un score ou une direction n'est pas fini : il ne reste donc jamais de valeur non finie sur une action gardée, et cette cause de E n'est atteinte que par le seuil des 10 %. Le code suit le point 4. Tension interne au texte, à déclarer.

**CCB-7 — les calculs décisifs vivent hors de la liste de `CODE-ACCB6`. Non bloquant ; précaution au lancement.** `aire_sous_courbe`, `intervalle_blocs`, `difference_aires_appariee`, `manifeste`, `scellement` et les modules de T0.7 ne sont pas contrôlés (déclaré par le développeur). Après la fusion, un changement de `sondes/` passerait sans refus. Ce qu'il faut : au lancement, vérifier que ces fichiers égalent le commit `6c98ea20` (empreintes du § 3 ; `manifeste.py` `1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d`, `scellement.py` `93beeb1c8aae75463afc98e76ffb330b1e4f26be9c08ae8fee539a2df6a94ef2`, `gardes.py` `a83c48ceba4877a2e226c3fd43669b464152f18169bb082e9b1c48ed92179439`) et l'écrire.

**CCB-8 — aiguillage G-3 et G-4 sans recoupement avec l'issue. Observation.** Le texte ne recoupe `entrees.A` qu'avec `table_A.A` ; le code fait de même. Une issue `L1b` avec A4 irait en G-4 sans refus. T0.7 ne peut pas l'écrire (`criteres_v1.regles`). Rien à faire, sauf si la mère veut ce recoupement au texte.

**CCB-9 — en-têtes en retard. Cosmétique.** `tests/test_accb6_lecture_v1.py` nomme encore le brouillon 2 comme texte joué ; l'en-tête de `phrases_v1.py` nomme le script d'énumération v1. Aucun effet.

## 8. Pièces gardées au bac à sable (non versées)

Dossier `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/cl-code-accb6/` ; copies du code, copies de mutation et dossiers temporaires effacés (800 Ko restants).

| fichier | sha256 |
|---|---|
| `gardes-cl/test_cl_accb6_v1.py` (essais du contre-lecteur) | `cb0cc8a18a7b25a3846db93dd499f8f741fa928f336578e6586c5176db5537f4` |
| `banc/mutations_cl_v1.py` (X01 à X32) | `744de9135c6a984211b08072e51384bd92b73a29eae0599a2d894023341f8832` |
| `banc/mutations_cl_v2.py` (G01 à G18, X17b) | `389e8e030da79fbc94b3352ddadbc58c7a66414dd100d8f14dfcadb4f20f03b2` |
| `banc/banc_cl_v1.py`, `banc/banc_cl_v2.py` | `71f1873e51e8c9f2d338f17835453914e4f4ca226cc50c33e06e75223cbb0d22`, `bf0e67f3fc0137ec24a6d9d64ca9033f85479a4a8cb51798a5e3aa2a16065f21` |
| `banc/banc_essais_cl_v1.py` | `5b47fed1bcfc2fa92e5a3beb8fbc89a683ac2ced885d05f698c2ca4f79d17b8d` |
| `banc/morceaux_cl_v1.py` | `badd3b91082f2f64ba554e55db474128cc4734231bf10703c1db9d3d20e0be18` |
| `sorties/banc-dev.jsonl` (71 mutations du développeur) | `29f2d2568a6a55bd21e4849b9dfd13e088ede6ba82dd9e37b436092035c49c00` |
| `sorties/banc-cl.jsonl`, `sorties/banc-cl2.jsonl` | `e43c1b220172913b044611ee23664064dd65b5dcba7f0b58aefa7c8abd23992a`, `db9c85d39c92940b5a38c92ace99117e97126e0aa5d3163ed50e418ea14ae89e` |
| `sorties/banc-essais-cl.jsonl` (mes essais sur les 22 survivantes) | `86ca03b22ed6d20656108ebdfd6e7e444ebfb12ed931939f4ec3296ae3c8f7d0` |
| `sorties/enum-v2-rejouee.txt` | `00088af568388a4fbe381b7d80b97883b242013d99c7c5893bde54b9e741873e` |

Le bac à sable n'est pas durable : si la mère veut `test_cl_accb6_v1.py`, elle le copie avant la fin de la session.

## 9. Non fait

- La suite complète et les essais de T0.7 (règle 5 ; la mère les joue).
- Aucune vérification du texte lui-même (sections gelées, puissance) : hors mandat.
- Le candidat 3, ignoré comme demandé.
