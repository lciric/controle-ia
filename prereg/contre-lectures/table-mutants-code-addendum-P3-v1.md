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
