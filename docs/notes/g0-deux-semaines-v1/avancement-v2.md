# Avancement du lanceur de T0.6 v2 (fichier de reprise ; branche `prep/t06-lanceur-v2` par-dessus `4448fa9a`)

Règle : chaque ligne passe à « fait » quand le fichier est sur le disque et committé ; un redémarrage reprend à la première
ligne « à faire ». Noms neufs (R12) : aucun fichier de la v1 n'est modifié.

| point | état | fichier(s) |
|---|---|---|
| C01 PROGRES sans état de sonde | fait (J1) | `t06/lanceur_v2.py` (`test_croise_v2`, `progres` neutres) ; essai `tests/test_t06_v2_lanceur_jouet.py::test_repetition_jouet_v2_par_la_commande_sans_fuite` |
| C02 `ligne_A` hors PROGRES, lignes A/B/C hors de `run.json` | fait (J1) | `t06/lanceur_v2.py` (`resume_imprimable`) ; même essai |
| C03 activations float16 + garde de disque | fait (J1) | `t06/lanceur_v2.py` (`ActivationsDemi`, `exiger_place_disque`) ; essais `test_place_disque_simulee`, `test_activations_demi_precision_sans_arrondi_silencieux` |
| C04 clés non lues refusées, `temoin_lexical`/`sondes_figees_p3` nuls exigés, `fils_test_croise` exigé | fait (J1) | `t06/configuration_v2.py` ; essais `tests/test_t06_v2_configuration.py` |
| C05 mémoire vive 128 000 Mo | fait (J1) | `config-t06-reel-v1-brouillon2.json` (`memoire_vive_min_go` 128, `offre.memoire_vive_min_mo` 128000) |
| C06 réserves par adaptateur + contrôle négatif sous A | fait (J1) | `t06/lecture_v2.py` ; essai `test_reserves_cout_par_adaptateur_et_controle_negatif` |
| C07 jeux par `jeu_ou_echec` | fait (J1) | `t06/lanceur_v2.py` ; vérifié dans la répétition jouet v2 |
| C08 dépense cumulée (antérieure + téléchargement), heure d'épuisement passée à l'amorce | fait (J2) | `t06/session_v2.py` ; `lancer_t06_v2.sh creation` (argument dépense antérieure, forfait lu dans l'offre, `DEPENSE_EPUISEE_UTC_S`) ; minuterie de `amorce_instance_t06_v2.sh` (consigne, pousse, « stopped ») ; essais J3 |
| C09 garde illisible → ALERTE, arrêt après trois échecs | fait (J2) | `lancer_t06_v2.sh surveillance` ; essai `test_surveillance_v2_cumul_mort_fin_et_garde_illisible` |
| C10 artefacts des poussées, disque simulé dans l'essai | fait (J3) | `tests/test_t06_v2_scripts.py` (poussée initiale refusée, poussée finale refusée trois fois, `df` factice) |
| C11 sous-ensemble en morceaux < 90 Mo + manifeste ; refus > 90 Mo avant commit ; données légères en commit à part | fait (J2) | `t06/lanceur_v2.py` ; `amorce_instance_t06_v2.sh` (`refuser_gros`, deux commits) ; essais J3 |
| C12 offre relue et vérifiée (carte, mémoire, cœurs, disque, prix, téléchargement), instances du programme | fait (J2) | `t06/session_v2.py` ; `lancer_t06_v2.sh creation` (`vastai search offers`, `vastai show instances`) ; essais J3 |
| C13 second démarrage après fin normale : poussée puis sleep infinity ; stopped → sleep infinity | fait (J2) | `amorce_instance_t06_v2.sh` (`t06-fin-normale`, `sommeil`) ; essais J3 |
| C14 échéance : consigner et pousser avant le DELETE | fait (J2) | minuterie de `amorce_instance_t06_v2.sh` (`t06-consigner.sh`) ; essai `test_minuterie_depense_epuisee_puis_echeance_consignent_et_poussent` |
| C15 prix maximal par carte en configuration, carte en argument | fait (J2) | `configuration_v2.py`, `session_v2.py` ; `lancer_t06_v2.sh creation OFFRE CARTE …` ; essais J3 |
| C16 libération des activations, durée par couple | fait (code) | `t06/lanceur_v2.py` |
| L04 unité du lot et pas déclarés (480) | fait (J1) | `configuration_v2.py` (`unite_du_lot`, `pas_declares` lu et vérifié avant le manifeste : `exiger_pas_declares`) ; essais |
| L05 règle « non interprétable » en configuration | fait (J1) | `configuration_v2.py`, `lecture_v2.py` ; essai `test_etat_du_jeu_v2_selon_la_regle` |
| L11 dernier jour de création et fin du GO en configuration | fait (J2) | `configuration_v2.py` (`calendrier`), `session_v2.py calendrier` ; `lancer_t06_v2.sh` (controles, creation : `FIN_GO_UTC_S` passée) ; amorce (vérifiée contre la configuration après le clonage) |
| configurations v2 (réelle brouillon 2, jouet v3) | fait (J1) | `config-t06-reel-v1-brouillon2.json`, `config-t06-jouet-v3.json` |
| essais v2 | fait (J3) | `tests/test_t06_v2_configuration.py`, `_session.py`, `_lanceur_jouet.py`, `_scripts.py` ; suite v1 + v2 : 139 essais |
| banc v2 | fait (J4) | `scripts/banc_mutations_t06_v2.py`, `banc-mutations-t06-v2.log`, `.json` (41 tuées sur 41) |
| E0 (test croisé synthétique, 0 USD) | fait (J5) | `scripts/epreuve_e0_t06_v2.py`, `epreuve-e0-t06-v2-journal.md` (1/64 et 1/256 ; Mahalanobis ≈ 26 ms/jeton : nœud, `familles_descriptives` ajoutée en configuration) |
| E1 (jouet sous l'amorce v2, 0 USD) | fait (J6) | `scripts/epreuve_e1_t06_v2.sh`, `epreuve-e1-t06-v2-journal.md` (0 mot interdit, 1 morceau, trois commits, fin normale) |
| rapport v2 | fait (J7) | `rapport-developpeur-lanceur-T0.6-v2.md` |
| familles descriptives en configuration (suite de E0) | fait (J5) | `configuration_v2.py` (`familles_descriptives`), `lanceur_v2.py`, configurations v2, essai |
