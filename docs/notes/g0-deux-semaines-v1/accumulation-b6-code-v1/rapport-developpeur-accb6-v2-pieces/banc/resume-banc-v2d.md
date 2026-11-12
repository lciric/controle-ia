
### mutations_temoin_v2 (2)
| T00 | témoin : commentaire seul | SURVIT | 191 passed, 1 skipped, 3 deselected in 234.81s (0:03:54) | 235.9 ; énumération : sortie égale (hors empreintes) |
| T01 | témoin : texte du motif (libre, lu par les essais dans la constante) | SURVIT | 191 passed, 1 skipped, 3 deselected in 233.39s (0:03:53) | 234.5 |

### mutations_accb6_code_v2 (20)
| V01 | E-1 : 200 directions (nombre d'avant T0.7 scellé) | tuée | test_accb6_lecture_v1.py::test_bout_en_bout_g4_etats_attendus_et_ecrits | 5.0 ; énumération : sortie égale (hors empreintes) |
| V02 | E-1 : 799 directions | tuée | test_accb6_lecture_v1.py::test_bout_en_bout_g4_etats_attendus_et_ecrits | 4.9 ; énumération : sortie égale (hors empreintes) |
| V03 | E-1 : 801 directions | tuée | test_accb6_lecture_v1.py::test_bout_en_bout_g4_etats_attendus_et_ecrits | 4.9 ; énumération : sortie égale (hors empreintes) |
| V04 | E-1 : plus de 800 directions acceptées | tuée | test_accb6_lecture_v1.py::test_directions_de_plancher_800_exigees[801] | 126.7 |
| V05 | E-1 : moins de 800 directions acceptées | tuée | test_accb6_lecture_v1.py::test_directions_de_plancher_800_exigees[200] | 126.9 |
| V06 | E-1 : garde du nombre de directions retirée | tuée | test_accb6_lecture_v1.py::test_directions_de_plancher_800_exigees[200] | 127.1 |
| V07 | E-1 : motif écrit (nombres permutés) | tuée | test_accb6_lecture_v1.py::test_directions_de_plancher_800_exigees[200] | 119.6 |
| V08 | E-3 : réserve du plancher neuf non recopiée (code v1) | tuée | test_accb6_lecture_v1.py::test_reserve_plancher_neuf_recopiee_unite | 124.3 |
| V09 | E-3 : préfixe cherché n'importe où dans la chaîne | tuée | test_accb6_lecture_v1.py::test_reserve_plancher_neuf_recopiee_unite | 118.4 |
| V10 | E-3 : toutes les chaînes de resultat.reserves recopiées | tuée | test_accb6_lecture_v1.py::test_reserve_plancher_neuf_recopiee_unite | 125.3 |
| V11 | E-3 : aucune sonde visée | tuée | test_accb6_lecture_v1.py::test_reserve_plancher_neuf_recopiee_unite | 125.7 |
| V12 | E-3 : toutes les sondes lues visées | tuée | test_accb6_lecture_v1.py::test_reserve_plancher_neuf_recopiee_unite | 122.1 |
| V13 | E-3 : resultat.reserves hors de forme accepté | tuée | test_accb6_lecture_v1.py::test_reserve_plancher_neuf_recopiee_unite | 124.1 |
| V14 | E-3 : entrée qui n'est pas une chaîne acceptée | tuée | test_accb6_lecture_v1.py::test_reserve_plancher_neuf_recopiee_unite | 126.0 |
| V15 | E-3 : phrase tronquée (pas telle quelle) | tuée | test_accb6_lecture_v1.py::test_reserve_plancher_neuf_recopiee_unite | 125.2 |
| V16 | E-3 : identifiant de la réserve | tuée | test_accb6_lecture_v1.py::test_reserve_plancher_neuf_recopiee_unite | 122.4 |
| V17 | E-3 : motif absent (annotation « (None) ») | tuée | test_accb6_lecture_v1.py::test_reserve_plancher_neuf_recopiee_unite | 121.4 |
| V18 | E-3 : ordre (avant reserves_identifiees) | tuée | test_accb6_lecture_v1.py::test_reserve_plancher_neuf_recopiee_unite | 123.0 |
| V19 | E-3 : préfixe faux | tuée | test_accb6_lecture_v1.py::test_reserve_plancher_neuf_recopiee_unite | 112.8 |
| V20 | E-3 : resultat.reserves absent → arrêt (le champ n'est pas exigé) | tuée | test_accb6_lecture_v1.py::test_bout_en_bout_g4_etats_attendus_et_ecrits | 10.5 |

### mutations_cl_v1 (23)
| X01 | étiquettes inversées (organisme = 0) | tuée | test_accb6_contre_lecture_v1.py::test_reference_independante_de_bout_en_bout[4-5-fuites0] | 19.0 |
| X02 | doses de la séquence lues à 95 % au lieu de 1 − 0,05/(2k) (survivante aux 171 essais d'après la contre-lecture) | tuée | test_accb6_contre_lecture_v1.py::test_reference_independante_de_bout_en_bout[4-5-fuites0] | 18.1 |
| X03 | M : borne haute stricte → large | tuée | test_accb6_contre_lecture_v1.py::test_unites_seuils_cote_maximum | 44.6 |
| X04 | S_max comparé au plancher de S_Σ (survivante aux 171 essais d'après la contre-lecture) | tuée | test_accb6_contre_lecture_v1.py::test_unites_seuils_cote_maximum | 43.0 |
| X05 | plancher de S_max tiré des sommes des directions (survivante aux 171 essais d'après la contre-lecture) | tuée | test_accb6_contre_lecture_v1.py::test_reference_independante_de_bout_en_bout[4-5-fuites0] | 17.8 |
| X06 | B6-D5 : différence des quantiles au lieu du quantile des Δ (survivante aux 171 essais d'après la contre-lecture) | tuée | test_accb6_contre_lecture_v1.py::test_reference_independante_de_bout_en_bout[4-5-fuites0] | 17.8 |
| X07 | Mn : au moins une au lieu du nombre (survivante aux 171 essais d'après la contre-lecture) | tuée | test_accb6_contre_lecture_v1.py::test_reference_independante_de_bout_en_bout[4-5-fuites0] | 17.3 |
| X08 | L : maximum au lieu de la somme des jetons notés (survivante aux 171 essais d'après la contre-lecture) | tuée | test_accb6_contre_lecture_v1.py::test_reference_independante_de_bout_en_bout[4-5-fuites0] | 17.3 |
| X09 | Δ = max − somme | tuée | test_accb6_contre_lecture_v1.py::test_reference_independante_de_bout_en_bout[4-5-fuites0] | 18.0 |
| X10 | trivial de S_max : au moins autant → strictement plus (survivante aux 171 essais d'après la contre-lecture) | tuée | test_accb6_contre_lecture_v1.py::test_unites_seuils_cote_maximum | 42.3 |
| X12 | rééchantillonnage par épisode au lieu de par tâche | tuée | test_accb6_contre_lecture_v1.py::test_reference_independante_de_bout_en_bout[4-5-fuites0] | 17.8 |
| X13 | saturation ≥ → > (survivante aux 171 essais d'après la contre-lecture) | tuée | test_accb6_contre_lecture_v1.py::test_unites_seuils_cote_maximum | 42.1 |
| X14 | témoins et jeux croisés : état au niveau décisif au lieu de 95 % (survivante aux 171 essais d'après la contre-lecture) | tuée | test_accb6_contre_lecture_v1.py::test_reference_independante_de_bout_en_bout[4-5-fuites0] | 22.0 |
| X16 | séquence : « partagé » franchit | tuée | test_accb6_etats_v1.py::test_sequence_fixee_toutes_les_issues | 53.6 ; énumération : écart relevé par le script : ÉCART : séquence ('partagé', 'non tranché : fuite nommée', 'non tranché : fuite nommée', 'non tranché : fuite nommée') : module (('S100',), 'S75', 'non tranché : fuite nommée') ≠ transcription ((), 'S100', 'partagé') |
| X17 | R-B6-CONSIGNE : Δ ≤ 0 → < 0 | erreur : ancien présent 0 fois |  | None |
| X21 | audit R4 : les deux aires à 1 → l'une (survivante aux 171 essais d'après la contre-lecture) | tuée | test_accb6_contre_lecture_v1.py::test_unite_audit_les_deux_aires_a_un | 40.7 |
| X22 | graine du jeu (i-a) pour tous les jeux (survivante aux 171 essais d'après la contre-lecture) | tuée | test_accb6_contre_lecture_v1.py::test_reference_independante_de_bout_en_bout[4-5-fuites0] | 17.1 |
| X25 | E1 = actions notées de E3 : un seul sens (survivante aux 171 essais d'après la contre-lecture) | tuée | test_accb6_contre_lecture_v1.py::test_unite_e1_egal_aux_actions_notees_de_e3_dans_les_deux_sens | 42.2 |
| X27 | chemin de SCELLEMENT-ACCB6 = prereg/accumulation-barreau6-v1.md | tuée | test_accb6_garde_v1.py::test_chemin_du_texte_scelle | 206.1 |
| X29 | direction non finie : tâche non exclue | tuée | test_accb6_lecture_v1.py::test_score_non_fini_tache_exclue | 127.3 |
| X30 | état du couple au dernier niveau calculé (95 % pour une dose) (survivante aux 171 essais d'après la contre-lecture) | tuée | test_accb6_contre_lecture_v1.py::test_reference_independante_de_bout_en_bout[4-5-fuites0] | 18.7 |
| X31 | plancher de S_Σ : médiane au lieu du quantile 0,95 | tuée | test_accb6_contre_lecture_v1.py::test_reference_independante_de_bout_en_bout[4-5-fuites0] | 19.5 |
| X32 | épisode de neuf actions gardé | tuée | test_accb6_contre_lecture_v1.py::test_reference_independante_de_bout_en_bout[4-5-fuites0] | 6.1 |

### mutations_cl_v2 (15)
| G01 | index de E1 ≠ index de E2b (survivante aux 171 essais d'après la contre-lecture) | tuée | test_accb6_contre_lecture_v1.py::test_gardes_de_e1_cas_sain_et_artefacts | 44.3 |
| G02 | mention_etendue ni booléen ni 0/1 (survivante aux 171 essais d'après la contre-lecture) | tuée | test_accb6_contre_lecture_v1.py::test_gardes_de_e3_mention_etendue_et_jetons | 43.4 |
| G03 | E1 = actions notées de E3 (garde entière) (survivante aux 171 essais d'après la contre-lecture) | tuée | test_accb6_contre_lecture_v1.py::test_unite_e1_egal_aux_actions_notees_de_e3_dans_les_deux_sens | 42.6 |
| G05 | sondes_lues de l'index de E1 (survivante aux 171 essais d'après la contre-lecture) | tuée | test_accb6_contre_lecture_v1.py::test_gardes_de_e1_cas_sain_et_artefacts | 41.1 |
| G08 | forme de doses.marques et doses.hors_jugement (survivante aux 171 essais d'après la contre-lecture) | tuée | test_accb6_contre_lecture_v1.py::test_doses_marques_hors_de_forme_arret | 50.9 |
| G09 | clés d'action en double dans E1 (survivante aux 171 essais d'après la contre-lecture) | tuée | test_accb6_contre_lecture_v1.py::test_gardes_de_e1_cas_sain_et_artefacts | 41.8 |
| G10 | R-B6-SPE : seule → une | tuée | test_accb6_garde_v1.py::test_reserve_dir_et_spe | 219.2 |
| G11 | R-B6-ADAPT lue sur B6-D3b | tuée | test_accb6_contre_lecture_v1.py::test_reserve_adapt_lue_sur_b6_d4_et_non_sur_b6_d3b | 56.4 |
| G12 | audit R4 : (i-a) décisive en « le maximum bat » | tuée | test_accb6_garde_v1.py::test_audit_r4_declencheurs | 217.9 |
| G13 | R-B6-NUL36 : (ii) en « le maximum bat » à la dose d'arrêt | tuée | test_accb6_garde_v1.py::test_reserve_nul36 | 219.3 |
| G14 | aire par action : doses hors jugement non comparées | tuée | test_accb6_contre_lecture_v1.py::test_aire_par_action_d_une_dose_hors_jugement_en_ecart_arret | 59.5 |
| G16 | réserves de T0.7 : sonde visée par le concept (survivante aux 171 essais d'après la contre-lecture) | tuée | test_accb6_contre_lecture_v1.py::test_reserves_de_t07_sonde_visee_par_le_nom_ou_par_le_concept | 57.7 |
| G17 | phrase « hors jugement » en annotation (survivante aux 171 essais d'après la contre-lecture) | tuée | test_accb6_contre_lecture_v1.py::test_annotations_sous_g3_prefixe_et_hors_jugement | 56.5 |
| G18 | G-3 : préfixe des réserves visant (ii) (survivante aux 171 essais d'après la contre-lecture) | tuée | test_accb6_contre_lecture_v1.py::test_annotations_sous_g3_prefixe_et_hors_jugement | 59.8 |
| X17b | R-B6-CONSIGNE : Δ ≤ 0 → < 0 (X17 corrigée : cible introuvable au lot 1) | tuée | test_accb6_garde_v1.py::test_reserve_consigne | 218.4 |

### mutations_accb6_v4 (71)
| M01 | couple : F avant E | tuée | test_accb6_etats_v1.py::test_etat_couple_regles_et_ordre[modif1-E] | 3.4 ; énumération : écart relevé par le script : ÉCART : couple {'echec': True, 'fuite': 'nommée', 'dessus_somme': False, 'dessus_max': False, 'sature_somme': False, 'sature_max': False, 'delta': 'ni', 'trivial_somme': False, 'trivial_max': False} : module F ≠ transcription E |
| M02 | couple : règle P (et → ou) | tuée | test_accb6_etats_v1.py::test_etat_couple_regles_et_ordre[modif8-Z] | 3.5 ; énumération : écart relevé par le script : ÉCART : couple {'echec': False, 'fuite': 'aucune', 'dessus_somme': False, 'dessus_max': True, 'sature_somme': False, 'sature_max': False, 'delta': 'ni', 'trivial_somme': False, 'trivial_max': False} : module P ≠ transcription Z |
| M03 | couple : règle S (et → ou) | tuée | test_accb6_etats_v1.py::test_etat_couple_regles_et_ordre[modif6-A] | 3.5 ; énumération : écart relevé par le script : ÉCART : couple {'echec': False, 'fuite': 'aucune', 'dessus_somme': False, 'dessus_max': True, 'sature_somme': False, 'sature_max': True, 'delta': 'ni', 'trivial_somme': False, 'trivial_max': False} : module S ≠ transcription Z |
| M04 | couple : prédicteur trivial ignoré pour A | tuée | test_accb6_etats_v1.py::test_etat_couple_regles_et_ordre[modif9-N] | 3.5 ; énumération : écart relevé par le script : ÉCART : couple {'echec': False, 'fuite': 'aucune', 'dessus_somme': True, 'dessus_max': False, 'sature_somme': False, 'sature_max': False, 'delta': 'bas>0', 'trivial_somme': True, 'trivial_max': False} : module A ≠ transcription N |
| M05 | couple : A sans S_Σ au-dessus du plancher | tuée | test_accb6_etats_v1.py::test_etat_couple_regles_et_ordre[modif8-Z] | 3.5 ; énumération : écart relevé par le script : ÉCART : couple {'echec': False, 'fuite': 'aucune', 'dessus_somme': False, 'dessus_max': True, 'sature_somme': False, 'sature_max': False, 'delta': 'bas>0', 'trivial_somme': False, 'trivial_max': False} : module A ≠ transcription Z |
| M06 | couple : trivial de S_Σ pour M | tuée | test_accb6_etats_v1.py::test_etat_couple_regles_et_ordre[modif13-N] | 3.4 ; énumération : écart relevé par le script : ÉCART : couple {'echec': False, 'fuite': 'aucune', 'dessus_somme': False, 'dessus_max': True, 'sature_somme': False, 'sature_max': False, 'delta': 'haut<0', 'trivial_somme': False, 'trivial_max': True} : module M ≠ transcription N |
| M07 | jeu : « partagé » retiré | tuée | test_accb6_etats_v1.py::test_etat_jeu[etats1-False-partag\xe9] | 3.6 ; énumération : écart relevé par le script : ÉCART : jeu ('A', 'M') (fuite False) : module accumuler bat ≠ transcription partagé |
| M08 | jeu : règles (6) et (7) permutées | tuée | FAILED test_accb6_etats_v1.py::test_etat_jeu[etats6-False-sous le plancher] | 3.6 ; énumération : écart relevé par le script : ÉCART : jeu ('P',) (fuite False) : module saturé ≠ transcription sous le plancher |
| M09 | jeu : « échec » sur une seule E | tuée | FAILED test_accb6_etats_v1.py::test_etat_jeu[etats6-False-sous le plancher] | 3.6 ; énumération : écart relevé par le script : ÉCART : jeu ('E', 'P') (fuite False) : module échec ≠ transcription sous le plancher |
| M10 | séquence : ordre des doses | tuée | test_accb6_etats_v1.py::test_une_phrase_et_une_seule_par_cas | 3.7 ; énumération : écart relevé par le script : ÉCART : ordre des doses du module ('S25', 'S50', 'S75', 'S100') ≠ ('S100', 'S75', 'S50', 'S25') |
| M11 | saturation 0,99 | tuée | test_accb6_etats_v1.py::test_seuils_stricts_par_le_calcul | 3.8 ; énumération : sortie égale (hors empreintes) |
| M12 | exclusion 10 % | tuée | test_accb6_lecture_v1.py::test_constantes_du_texte | 110.1 ; énumération : sortie égale (hors empreintes) |
| M13 | quantile du plancher | tuée | test_accb6_lecture_v1.py::test_constantes_du_texte | 110.3 ; énumération : sortie égale (hors empreintes) |
| M14 | familles N-054 | tuée | test_accb6_etats_v1.py::test_familles_n054 | 3.1 ; énumération : sortie égale (hors empreintes) |
| M15 | niveau 1 − 0,05/(2k) | tuée | test_accb6_lecture_v1.py::test_bout_en_bout_g4_etats_attendus_et_ecrits | 11.0 |
| M16 | moyenne au lieu de la somme (même aire) | tuée | test_accb6_lecture_v1.py::test_somme_et_maximum_egaux_a_la_reference | 28.3 |
| M17 | minimum au lieu du maximum | tuée | test_accb6_lecture_v1.py::test_bout_en_bout_g4_etats_attendus_et_ecrits | 11.3 |
| M18 | plancher : stricte → large | tuée | test_accb6_etats_v1.py::test_seuils_stricts_par_le_calcul | 3.5 |
| M19 | Δ : stricte → large | tuée | test_accb6_etats_v1.py::test_seuils_stricts_par_le_calcul | 3.6 |
| M20 | graine : mêmes tirages | tuée | test_accb6_lecture_v1.py::test_manifeste_graines_par_jeu_et_sonde_et_memes_tirages | 19.6 |
| M21 | 10 000 tirages | tuée | test_accb6_lecture_v1.py::test_g1_rien_n_est_lu | 26.8 |
| M22 | condition mention lue | tuée | test_accb6_lecture_v1.py::test_g2_aucune_ligne_de_ii_lue | 31.0 |
| M23 | G-2 : lignes de (ii) lues | tuée | test_accb6_lecture_v1.py::test_g2_defense_en_profondeur_sans_conditions_retirees | 118.1 |
| M24 | tolérance de l'aire par action | tuée | test_accb6_lecture_v1.py::test_aire_par_action_en_ecart_arret | 96.1 |
| M25 | identité E1/E3 | tuée | test_accb6_lecture_v1.py::test_identite_e1_e3_en_ecart_arret | 102.3 |
| M26 | fuites ignorées | tuée | test_accb6_lecture_v1.py::test_fuite_nommee_sur_saboteur | 106.6 |
| M27 | R-B6-DIR inversée | tuée | test_accb6_garde_v1.py::test_reserve_adapt | 167.4 |
| M28 | R-B6-NUL36 | tuée | test_accb6_garde_v1.py::test_reserve_dir_et_spe | 168.6 |
| M29 | audit R4 |Δ| > 0,35 | tuée | test_accb6_garde_v1.py::test_audit_r4_declencheurs | 170.5 |
| M30 | trivial : au moins autant | tuée | test_accb6_etats_v1.py::test_seuils_stricts_par_le_calcul | 3.5 |
| M31 | 200 directions exigées | tuée | test_accb6_lecture_v1.py::test_directions_de_plancher_800_exigees[200] | 126.5 |
| M32 | épisode : pas 0 à 9 | tuée | test_accb6_lecture_v1.py::test_pas_repete_episode_incomplet | 76.5 |
| M33 | exclusion : plus de 10 % | tuée | test_accb6_lecture_v1.py::test_dix_pour_cent_exactement_garde | 72.9 |
| M34 | aire par action : garde retirée | tuée | test_accb6_lecture_v1.py::test_aire_par_action_en_ecart_arret | 92.4 |
| M35 | agrégation : garde retirée | tuée | test_accb6_lecture_v1.py::test_entrees_e2_e2b_en_defaut_refus[agregation] | 95.1 |
| M36 | k recoupé avec niveau_applique | tuée | test_accb6_lecture_v1.py::test_k_recoupe_avec_niveau_applique_meme_si_e2_et_e4_s_accordent | 124.7 |
| M37 | ordre : scellement strictement avant SCORES-T07 | tuée | test_accb6_garde_v1.py::test_scellement_non_anterieur_a_scores_t07 | 150.9 |
| M38 | arret-etape-b.json | tuée | test_accb6_garde_v1.py::test_arret_etape_b_present | 155.4 |
| M39 | lecture unique (fichier) | tuée | test_accb6_garde_v1.py::test_lecture_unique_fichier_deja_present | 160.3 |
| M40 | clé ACCB6 au registre partagé | tuée | test_accb6_garde_v1.py::test_cle_de_ce_texte_au_registre_partage | 160.1 |
| M41 | run 7a refusé | tuée | test_accb6_garde_v1.py::test_run_7a_refuse | 159.6 |
| M42 | aiguillage : recoupement de G-1 | tuée | test_accb6_garde_v1.py::test_aiguillage_artefacts[G-1-modif0-recoupement] | 167.7 |
| M43 | aiguillage : L1b et Q | tuée | test_accb6_lecture_v1.py::test_g3_ii_descriptif_jamais_etabli | 31.0 |
| M44 | aiguillage : recoupement de A | tuée | FAILED test_accb6_garde_v1.py::test_aiguillage_artefacts[G-3-modif8-\u2260 table_A.A] | 171.3 |
| M45 | aiguillage : lignes A de G-3 | tuée | test_accb6_lecture_v1.py::test_bout_en_bout_g4_etats_attendus_et_ecrits | 11.0 |
| M46 | R-B6-TARD | tuée | test_accb6_garde_v1.py::test_reserve_tard | 152.5 |
| M47 | R-B6-CODE | tuée | test_accb6_garde_v1.py::test_reserve_code | 174.1 |
| M48 | journal propre | tuée | test_accb6_lecture_v1.py::test_bout_en_bout_g4_etats_attendus_et_ecrits | 4.1 |
| M49 | sceaux du registre partagé | tuée | test_accb6_garde_v1.py::test_ligne_non_anterieure_a_l_ouverture[0] | 150.5 |
| M50 | aiguillage : conditions retirées sous G-2 | tuée | test_accb6_garde_v1.py::test_aiguillage_artefacts[G-2-modif5-recoupement] | 177.7 |
| M51 | entropie de CODE-ACCB6 | tuée | test_accb6_garde_v1.py::test_fichier_code_mal_forme[code3-entropie] | 158.1 |
| M52 | N-B6-3 option (a) | tuée | test_accb6_lecture_v1.py::test_bout_en_bout_g4_etats_attendus_et_ecrits | 10.4 ; énumération : sortie différente (333 lignes) |
| M53 | table : ordre des lignes | tuée | test_accb6_etats_v1.py::test_une_phrase_et_une_seule_par_cas | 3.5 ; énumération : écart relevé par le script : ole_ia/accumulation_b6/phrases_v1.py", line 94, in phrase_etat
    raise GardeArret(f"état {etat!r} sans phrase dans la dernière ligne de la table (A et M ont leurs lignes)")
controle_ia.gardes.GardeArret: état 'le maximum bat' sans phrase dans la dernière ligne de la table (A et M ont leurs lignes) |
| M54 | G-3 : arrêt en M réfuté | tuée | test_accb6_etats_v1.py::test_g3_jamais_etabli_pour_l_organisme_sans_consigne | 3.3 ; énumération : sortie différente (27 lignes) |
| M55 | phrase de « partagé » | tuée | test_accb6_etats_v1.py::test_phrases_de_la_table_mot_pour_mot | 3.6 ; énumération : sortie différente (131 lignes) |
| C01 | commit ancêtre de la tête | tuée | test_accb6_code_v1.py::test_commit_non_ancetre_de_la_tete | 167.0 |
| C02 | fichiers du paquet au commit = liste | tuée | test_accb6_code_v1.py::test_fichier_du_commit_absent_de_la_liste_et_du_paquet_importe | 170.3 |
| C03 | fichiers du paquet importé = liste | tuée | test_accb6_code_v1.py::test_fichier_en_plus_ou_en_moins_dans_le_paquet_importe[ajout] | 169.8 |
| C04 | empreintes au commit | tuée | test_accb6_code_v1.py::test_empreinte_ecrite_fausse | 211.5 |
| C05 | empreintes du paquet importé | tuée | test_accb6_code_v1.py::test_fichier_du_paquet_importe_modifie | 216.7 |
| C06 | commit cité présent | tuée | test_accb6_code_v1.py::test_commit_absent | 239.9 |
| C07 | paquet à sa place dans le dépôt | tuée | test_accb6_code_v1.py::test_paquet_ailleurs_dans_le_depot | 261.8 |
| C08 | chemins listés dans le paquet | tuée | test_accb6_code_v1.py::test_chemin_liste_hors_du_paquet | 259.4 |
| C09 | paquet hors dépôt git | tuée | test_accb6_code_v1.py::test_paquet_hors_d_un_depot_git | 270.6 |
| C10 | appel du contrôle par la lecture | tuée | test_accb6_code_v1.py::test_lecture_refusee_avant_tout_calcul | 227.7 |
| R01 | garde de non-relance (arret-accb6.json d'un run quelconque) | tuée | test_accb6_lecture_v1.py::test_directions_de_plancher_200_par_la_commande_code_3_puis_relance_refusee | 166.3 |
| R02 | garde de non-relance : fichier cherché | tuée | test_accb6_lecture_v1.py::test_directions_de_plancher_200_par_la_commande_code_3_puis_relance_refusee | 149.6 |
| P01 | VB6-1 : phrase de (i) en A (contrôle de consigne) | tuée | test_accb6_phrases_texte_v1.py::test_chaque_phrase_produite_egale_la_table_du_texte | 227.6 ; énumération : sortie différente (60 lignes) |
| P02 | VB6-1 : ligne (i) A | tuée | test_accb6_phrases_texte_v1.py::test_chaque_phrase_produite_egale_la_table_du_texte | 244.5 ; énumération : sortie différente (7 lignes) |
| P03 | VB6-2 : ligne (i) M sans répétition | tuée | test_accb6_phrases_texte_v1.py::test_chaque_phrase_produite_egale_la_table_du_texte | 233.6 ; énumération : sortie différente (7 lignes) |
| P04 | texte du contrôle de consigne | tuée | test_accb6_phrases_texte_v1.py::test_chaque_phrase_produite_egale_la_table_du_texte | 194.8 ; énumération : sortie différente (67 lignes) |
