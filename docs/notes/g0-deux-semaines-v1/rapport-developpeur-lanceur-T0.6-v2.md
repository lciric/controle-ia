# Rapport du développeur neuf — lanceur de T0.6, v2 (additif au rapport v1)

- Statut : rendu le 2026-11-05 20:55 UTC (heure relevée par `date -u`) par un développeur neuf (Claude Fable 5.1, sous-agent de la fille 7),
  qui n'a écrit ni le lanceur v1, ni la contre-lecture, ni le texte. Brief suivi : brief T1 (bloc-notes de la session) ;
  pièces : contre-lecture du lanceur v1 (`docs/notes/g0-deux-semaines-v1/contre-lecture-lanceur-T0.6-v1/contre-lecture-lanceur-T0.6-v1.md`,
  `5e35956554395686…`, vérifiée par `sha256sum -c`), couples `couples-contre-lecture-lanceur-T0.6-v1.json` (`a65e8d584f50bd7c…`,
  vérifié ; L04, L05, L11 lus pour en faire des valeurs de configuration), rapport v1, texte brouillon 4 (`8df90b8be08452a9…`,
  point 9, liste d'arrêt, devis, plan daté). Rien n'est loué, aucun modèle n'est téléchargé ni appelé, aucune clé n'est lue, rien
  sous `donnees/` ni `diag/` n'est lu, aucun fichier existant n'est modifié (R12 : tous les fichiers portent `_v2` ou `v2`,
  sauf les fichiers de l'instantané `96d10acb` de la branche, qui sont de la v2 et que j'ai complétés).
- Branche : `prep/t06-lanceur-v2` (arbre `/home/user/wt/t06-lanceur-v2`), par-dessus l'instantané `96d10acb` et le lanceur v1
  `4448fa9a` ; jalons J1 à J7 committés et poussés sur cette branche seulement ; dernier commit dans la réponse finale.
- Vérification de l'existant (brief, « vérifie d'abord ») : les quatre modules de l'instantané (`configuration_v2`, `lecture_v2`,
  `session_v2`, `lanceur_v2`) faisaient ce que l'avancement disait pour C01, C02, C03, C06, C07, C11 (côté lanceur), C12, C15,
  C16, L05 ; manquaient : la **vérification** des pas déclarés avant le manifeste (L04 n'était qu'un calcul écrit au résultat),
  le calendrier **vérifié contre le registre des GO** (L11), le forfait de téléchargement lu dans l'offre (C08), tous les essais,
  les deux scripts, les configurations. Complété en J1-J2.

## 1. Fichiers neufs et empreintes (sha256 au dernier commit ; la mère scelle, aucun `.sha256` écrit ici)

| fichier | sha256 | lignes |
|---|---|---|
| `docs/notes/g0-deux-semaines-v1/avancement-v2.md` | `52dd98852662e3c6e38b38f447861d429814ec8b102f54f4c95c3780a9f6d8f1` | 33 |
| `docs/notes/g0-deux-semaines-v1/banc-mutations-t06-v2.json` | `401bf86c09ca9568e7db1e7efc0d4df1626d83c6b6ba7acab91ed8b5d7e49871` | 391 |
| `docs/notes/g0-deux-semaines-v1/banc-mutations-t06-v2.log` | `c346995dca45c7a28b0c6a6a44acd140da60f9e7d9b6871d2e711d43e4373e51` | 49 |
| `docs/notes/g0-deux-semaines-v1/config-t06-jouet-v3.json` | `2bf0999558998927ce05d4e309e57984acb585a401b62f074fa32ab72e744c97` | 138 |
| `docs/notes/g0-deux-semaines-v1/config-t06-reel-v1-brouillon2.json` | `34ae15036cf85e1a826169b0ae5902e743f539236f4c518f38ddb4afdcf76d5d` | 142 |
| `docs/notes/g0-deux-semaines-v1/epreuve-e0-t06-v2-journal.md` | `b89af80835ef7cd2f464da1833f18ba0cd82103a369b60e9d67889ac44ce6e9d` | 72 |
| `docs/notes/g0-deux-semaines-v1/epreuve-e1-t06-v2-journal.md` | `8d9b4b4792f5750b2a9f5165772d1e0035ed3fa5b48b343eb5a08ea82b81c6b4` | 169 |
| `scripts/amorce_instance_t06_v2.sh` | `39c3e7fb31adff9b35e6a91ea5a42b853e54999ed638ce196adece95d7a82d66` | 324 |
| `scripts/banc_mutations_t06_v2.py` | `7acd71f8fb15623263061702a3fc52c77a9f7da6baade5e9d3b71749cc219e80` | 145 |
| `scripts/epreuve_e0_t06_v2.py` | `237be40260ce22b7f0648f659a7d3991f082f89dc544e9b2a2d1be089afad017` | 154 |
| `scripts/epreuve_e1_t06_v2.sh` | `9fa32c8c55d6ff22cada5f16949e8cd3921531d36309a3a8d60729d41d59e9a7` | 84 |
| `scripts/lancer_t06_v2.sh` | `474653157fd2f50fd0efd167847b3a6dc31ed468c3bf5abb46400701c28e9c6e` | 167 |
| `src/controle_ia/t06/configuration_v2.py` | `3ed5d436af9631aa928f132dbc7ac09cd39df5b0b8db1f2c53144c72010f5645` | 146 |
| `src/controle_ia/t06/lanceur_v2.py` | `f2db51fc85e06af1f3b1b05897f8c54db3867704fc6e0a11903002eec2107388` | 407 |
| `src/controle_ia/t06/lecture_v2.py` | `a84994746b90ab05631a2e7fcfe8fca330a036d0424d550aa1f3363d0db0e4f7` | 81 |
| `src/controle_ia/t06/session_v2.py` | `6d9f75989e5e21a26b600378167a84f349d4dbc1a9c8740ede7d8471f6779266` | 196 |
| `tests/test_t06_v2_configuration.py` | `0d0150990cc2270769610a570aef5aa402b9a9b1fc67e1843cb88ddd63a748a4` | 129 |
| `tests/test_t06_v2_lanceur_jouet.py` | `1688069f60a7c013158ae87d451bf43c1659e97506485aa46aacecc775c131cc` | 260 |
| `tests/test_t06_v2_scripts.py` | `a9cfd036fdf784e6e7107d477de53cf63b686978f293e77aad18ac92a46b0cba` | 491 |
| `tests/test_t06_v2_session.py` | `02f8d80335dcc08a14ca5b72da396c0aee39108fcc3216cdf44d70178425d241` | 121 |

Fichiers de la v1 (`t06/lanceur.py`, `lecture.py`, `session.py`, `configuration.py`, `test_croise.py`, scripts v1, essais v1,
configurations v1) : inchangés ; `git diff 4448fa9a HEAD --stat -- src/controle_ia/t06/lanceur.py src/controle_ia/t06/lecture.py
src/controle_ia/t06/session.py src/controle_ia/t06/configuration.py src/controle_ia/t06/test_croise.py scripts/*_v1.sh tests/test_t06_cout.py
tests/test_t06_distillation.py tests/test_t06_lanceur_jouet.py tests/test_t06_lecture.py tests/test_t06_scripts.py tests/test_t06_session.py
tests/test_t06_test_croise.py` est vide (vérifié). Paquets gelés (`organismes`, `sondes`, `harnais`, `premier_test_ia`, `environnements`) :
inchangés.

## 2. Traitement de chaque point de la liste fermée

| point | état | où, et comment c'est éprouvé |
|---|---|---|
| C01 PROGRES sans état de sonde | **fait** | `lanceur_v2.test_croise_v2` : `PROGRES etape=test-croise jeux=2 duree_s=…`, `etape=couple-descriptif couple=… duree_s=…` ; aucune autre ligne ne porte un état, une aire ni une ligne de table. Amorce v2 : relais des seules lignes `PROGRES` bien formées **et** sans mot interdit (`au-dessus`, `interpr`, `échec`, `aire=`, `bas=`, `haut=`, `ligne_`, `table_`, `plancher`) ; une ligne retenue est comptée (`progres-retenues.txt`, versé aux traces). Essais : `test_t06_v2_lanceur_jouet.py::test_repetition_jouet_v2_par_la_commande_sans_fuite` (sortie standard et d'erreur capturées : mots interdits absents, aucune valeur d'aire non entière des jeux décisifs parmi les valeurs de PROGRES ni de `run.json`) ; `test_t06_v2_scripts.py::test_amorce_cas_sain…` (ligne `sens1=au-dessus` du faux lanceur retenue, absente du journal et de la sortie) ; E1 (0 occurrence dans journal, `run.err`, `run.json`, traces). Banc : mutations C01 tuées. |
| C02 `ligne_A` hors PROGRES, lignes A/B/C hors de `run.json` | **fait** | `progres(etape="lecture-cout", duree_s=…)` ; `resume_imprimable` retire `ligne_A`, `ligne_B`, `ligne_C` de la sortie standard ; le résumé scellé (`diag/<run>/resume.json`) les garde. Essai : même répétition (`run_json` sans ces clés, résumé scellé avec). |
| C03 activations float16 + garde de disque | **fait** | `ActivationsDemi` : écrit en float16 après contrôle de finitude et de portée (valeur > 65 504 ou non finie = arrêt, aucun arrondi silencieux), relit en float32 (les sondes calculent en double) ; `exiger_place_disque` avant les épisodes : pire cas = actions × `max_nouveaux` × largeur × 2 octets × couches, + 10 %, lu dans la configuration et le modèle. Essais : `test_place_disque_simulee` (place simulée par `shutil.disk_usage` remplacé : 100 Go passe, 60 Go < 62,3 Go arrête ; jamais le disque de l'hôte), `test_activations_demi_precision_sans_arrondi_silencieux`. |
| C04 clés non lues refusées ; `temoin_lexical`, `sondes_figees_p3` nuls ; `fils_test_croise` exigé | **fait** | `configuration_v2.exiger_config_t06_v2` : ensemble exact des clés (`CLES_T06_V2`), clés de `distillation` exactes, nul exigé pour les deux clés non branchées, `fils_test_croise` entier ≥ 1 (lu par `torch.set_num_threads`). Essais : `test_t06_v2_configuration.py` (22 artefacts paramétrés). |
| C05 mémoire vive 128 000 Mo | **fait** | `config-t06-reel-v1-brouillon2.json` : `memoire_vive_min_go` 128 (unité décimale de `exiger_memoire_vive` : 128 × 10⁹ octets = 128 000 Mo, ≈ 119 Gio) et `offre.memoire_vive_min_mo` 128 000 (borne de l'offre, C12). Réserve : `MemTotal` d'une machine louée avec exactement 128 000 Mo peut être un peu sous 128 × 10⁹ (réserve du noyau) ; l'offre la moins chère conforme aura en pratique bien plus (relevés 258 000 Mo) ; à relire au devis. |
| C06 réserves par adaptateur ; contrôle négatif sous A | **fait** | `lecture_v2.reserves_cout_v2` : exclusions comptées par adaptateur (`exclusions_par_adaptateur`, écrit par le lanceur), réserve « contrôle négatif non concluant » ajoutée aux réserves de la table A. Essai : `test_reserves_cout_par_adaptateur_et_controle_negatif` (2 sur 20 pour le saboteur seul : réserve ; 1 + 1 : aucune). |
| C07 jeux par `jeu_ou_echec` | **fait** | `test_croise_v2` : tout jeu (décisifs, contrôles, validité, courbe, descriptifs) par `jeu_ou_echec` ; l'état « échec » est une valeur du résultat scellé, jamais un arrêt. Banc : mutation « jeu décisif par jeu_croise » tuée. |
| C08 dépense cumulée, heure d'épuisement | **fait** | `session_v2.depense_cumulee_v2` (antérieure + forfait de téléchargement + instance ; `epuisement_utc_s`) ; `lancer_t06_v2.sh creation OFFRE CARTE DEPENSE_ANTERIEURE_USD DOSSIER` (forfait = `inet_down_cost` × `offre.telechargement_go_prevu` (40 Go)), `DEPENSE_EPUISEE_UTC_S` passée à l'amorce, écrite dans `lancement.txt` et relue par `surveillance` ; minuterie de l'amorce : à cette heure, consigne, pousse, PUT « stopped ». Essais : `test_depense_cumulee_v2…`, `test_surveillance_v2_cumul…` (189 + 1,2 + 10,3 = 200,5 : ARRET ; la v1 aurait poursuivi), `test_minuterie_depense_epuisee…` (`curl` factice). |
| C09 garde illisible → ALERTE, arrêt après trois | **fait** | `lancer_t06_v2.sh surveillance` : compteur `ILLISIBLES` ; ALERTE (1/3, 2/3), `ARRET garde` au troisième échec de suite, code 3, commande d'arrêt par l'identifiant imprimée. Essai : prix illisible dans `lancement.txt`. |
| C10 artefacts des poussées, disque simulé | **fait** | `test_t06_v2_scripts.py` : crochet `pre-receive` du dépôt nu qui refuse tout (poussée initiale refusée → refus, destruction, rien ne part) ou toute mise à jour (poussée finale refusée trois fois → journal, `t06-fin-normale`, arrêt code 1, commits gardés sur l'instance ; second démarrage : repousse ; crochet levé : tout part) ; `controles` avec un `df` factice (2,5 Go refusé, 5 Go conforme). Les deux échecs de la v1 liés au disque de l'hôte **ne se reproduisent pas ici** (12 Go libres au départ) ; les essais v2 n'en dépendent plus. |
| C11 morceaux < 90 Mo, manifeste, refus avant commit, commits à part | **fait** | `lanceur_v2.sous_ensemble_en_morceaux` (borne 90 000 000 octets, taille du fichier écrit vérifiée, manifeste scellé avec fichiers, empreintes, octets, clés) ; amorce : `refuser_gros` avant **chaque** commit (fichier indexé > 90 Mo retiré de l'index, journalisé « ERREUR DE CHAÎNE (C11) », listé dans `t06-fichiers-trop-gros.txt` versé aux traces), commit des données légères (adaptateurs, mesures, textes, manifeste) poussé **avant** le commit des morceaux. Essais : `test_sous_ensemble_en_morceaux_sous_la_borne`, `test_amorce_fichier_trop_gros…` (fichier de 90 000 001 octets refusé, les autres poussés, taille maximale poussée < 90 Mo), `test_amorce_cas_sain…` (ordre des commits). E0 : ≈ 12 morceaux attendus à la taille réelle. |
| C12 offre relue et vérifiée, instances | **fait** | `lancer_t06_v2.sh creation` : `vastai search offers "id=<OFFRE>" --raw` → `session_v2 offre` (une seule offre ; `gpu_name` = `carte.<CARTE>.nom_offre` ; `gpu_ram` ≥ mémoire de carte ; `num_gpus` 1 ; `cpu_ram` ≥ 128 000 ; `cpu_cores_effective` ≥ 16 ; `disk_space` ≥ 150 ; `dph_total` ≤ prix maximal de la carte ; `storage_total_cost` ≤ 0,03 ; `inet_down_cost` ≤ 0,05 ; `rentable`) ; prix lus dans l'offre, jamais donnés à la main ; `vastai show instances --raw` → `session_v2 instances` (aucune étiquette `t06-v2…`). Essais : 13 artefacts d'offre, instances, et la chaîne avec `vastai` factice (prix 1,31 → code 3 « nœud » ; H200 en « course » refusée, en « relance » admise ; instance présente → code 3). |
| C13 second démarrage, « stopped » → sommeil | **fait** | amorce : `t06-fin-normale` posé avant l'arrêt ; au second démarrage avec `t06-fin-normale` ou `t06-depense-epuisee` : `t06-consigner.sh` (commits en attente poussés) puis `sommeil` (`sleep infinity` ; essai : fichier `t06-sommeil`) ; sans ces marqueurs (run interrompu) : partiels consignés puis destruction comme en v1 ; après un « stopped » obtenu : sommeil au lieu de `sleep 10; exit`. Essais : cas sain (second démarrage pousse `diag/apres/note.json`, dort, jamais `t06-detruire`), run interrompu (destruction après consignation). |
| C14 échéance : consigner et pousser avant le DELETE | **fait** | minuterie v2 (bash seul) : à l'échéance, `t06-consigner.sh "échéance"` (git seul : deux commits, poussée en trois essais) **avant** la boucle de DELETE ; `t06-consigner.sh` est écrit par l'amorce après le clonage et sert aussi à la dépense épuisée et au second démarrage. Essai : `test_minuterie_depense_epuisee_puis_echeance_consignent_et_poussent` (`curl` factice journalisant PUT puis DELETE ; ordre DÉPENSE ÉPUISÉE < ÉCHÉANCE < DELETE ; commits poussés ; artefact : identifiant illisible → aucun geste). |
| C15 prix maximal par carte, carte en argument | **fait** | `carte.course` (A100 SXM4 80 Go, `nom_offre` « A100 SXM4 », 80 000 Mo, 1,30) et `carte.relance` (H200 NVL, 140 000 Mo, **4,70** USD/h, couple L10) dans la configuration ; `creation … CARTE …` ; `PRIX_MAX` retiré du script. |
| C16 libération des activations, durée par couple | **fait** (instantané, vérifié) | `del actions; gc.collect()` avant chaque couche ; `durees_s` par couple dans le résultat scellé et en `PROGRES`. E0 : pic de mémoire non cumulé entre couches (2 Go au 1/64). |
| L04 480 pas déclarés, « lot 1 » = une transcription | **fait, en configuration** | `distillation.unite_du_lot` (« transcription ») et `distillation.pas_declares` (480 au réel : 32 tâches × 5 épisodes × 3 époques / lot 1 ; 1 au jouet v3) ; `exiger_pas_declares` **avant le manifeste** (plan (b) : déclaré ≠ attendu des tâches de réserve → aucune création) ; au résultat (`distillation-t06.json`) : `pas_declares` (déclaré, attendu, plan) et, par adaptateur, `pas_de_distillation_declares` (pas effectifs après exclusions, `conforme_au_declare`). Essais : `test_pas_declares_faux_aucune_creation` (480 déclarés au jouet → arrêt sans manifeste), `test_pas_declares_plan_b_et_plan_a`. Le choix de fond (480 contre 4 800) reste un **nœud de Lazar** : la valeur par défaut est celle du lecteur (480, déclarés). |
| L05 « non interprétable » si au-dessus seulement | **fait, en configuration** | `lecture.non_interpretable_si_au_dessus_seulement` (vrai au réel et au jouet, recommandation du lecteur) ; `lecture_v2.appliquer_regle_etat` réécrit l'état de chaque jeu selon la règle et écrit la règle dans chaque jeu et dans le résultat (`regle`). Essai : `test_etat_du_jeu_v2_selon_la_regle` (les deux règles, cas sain et artefact). |
| L11 dernier jour 15 novembre, fin du GO 2026-11-17T00:00:00Z | **fait, en configuration et vérifié** | `calendrier` dans la configuration ; `session_v2 calendrier` vérifie que `fin_go_utc` = lendemain 00:00 UTC de l'échéance lue au registre des GO (`2026-11-16` → `1794873600`), que le dernier jour précède la fin, que le jour (contrôles, création) ne dépasse pas le dernier jour ; `lancer_t06_v2.sh` passe `FIN_GO_UTC_S` à l'amorce, qui la revérifie contre la configuration après le clonage (refus sinon) ; plus aucun `1794873600` en dur dans les scripts v2. Essais : `test_calendrier_contre_le_registre`, contrôles le 16 novembre refusés, amorce avec `FIN_GO_UTC_S` fausse refusée. |
| E0 | **fait (0 USD)** | `scripts/epreuve_e0_t06_v2.py`, journal `epreuve-e0-t06-v2-journal.md` : 1/64 et 1/256 (la taille réelle, 31,5 Go, ne tient pas sous 2 Go). **Résultat saillant : Mahalanobis coûte ≈ 26 ms par jeton** (paquet gelé) : ≈ 9 h par couche à la taille réelle sur ce processeur, 8 à 20 h de carte sur l'instance pour les trois couples, contre ≈ 1 h au devis ; le reste du test croisé tient en ≈ 2 h sur 4 cœurs. Suite : clé `familles_descriptives` (valeur de configuration ; la configuration réelle garde les cinq familles du texte) ; **nœud de Lazar** (retirer Mahalanobis de la course). |
| E1 | **fait (0 USD)** | `scripts/epreuve_e1_t06_v2.sh`, journal `epreuve-e1-t06-v2-journal.md` : vrai lanceur v2 sous la vraie amorce v2, dépôt nu local, `vastai` absent ; 36 lignes PROGRES neutres, 0 mot interdit dans journal, `run.err`, `run.json`, traces ; 1 morceau ; trois commits (données légères, morceaux, traces) ; `t06-fin-normale` ; deux gardes vues en passant (nombre de tests attendus faux → arrêt avant le run ; dépôt sale → run mort consigné). |

Déclaré, hors de la liste : (a) le résultat scellé `lecture-sondes-t06.json` (états des jeux, aires) est poussé sous `diag/`
comme en v1, fermé « à ne pas ouvrir avant le verdict scellé de P3-bis » : c'est la conception du texte (deux résultats
scellés séparés, point 6) ; la v2 ne le chiffre pas ; (b) `arret.json` porte le motif d'un arrêt (jamais un état de jeu, les
jeux ne s'arrêtent plus) ; (c) les noms d'offre Vast (`A100 SXM4`, `H200 NVL`) et la mémoire de carte en Mo sont des valeurs
de configuration à confirmer sur une relecture d'offre réelle avant la course (aucun appel ici).

## 3. Comptes d'essais

- Commande (suite v1 et v2 de T0.6, un seul processus, sous le verrou de la machine) :
  `cd /home/user/wt/t06-lanceur-v2 && . /home/user/controle-ia-travail/.venv/bin/activate && export PYTHONPATH=src && flock /home/user/wt/.pytest.lock timeout 900 nice -n 10 python -m pytest -q -p no:cacheprovider tests/test_t06_cout.py tests/test_t06_distillation.py tests/test_t06_test_croise.py tests/test_t06_lecture.py tests/test_t06_session.py tests/test_t06_lanceur_jouet.py tests/test_t06_scripts.py tests/test_t06_v2_configuration.py tests/test_t06_v2_session.py tests/test_t06_v2_lanceur_jouet.py tests/test_t06_v2_scripts.py`
- Résultat : **143 passed in 90.74s (0:01:30)** (Thu Nov  5 20:51:18 UTC 2026 → Thu Nov  5 20:54:58 UTC 2026 UTC ; code 0) ; dont 76 essais v1 et 67 essais v2 (cas avec les paramètres).
- Essais v1 seuls (les sept fichiers, rejoués au début, 19:24 UTC) : **76 passed in 47.43s** ; les deux échecs connus de
  `test_t06_scripts.py` (disque de l'hôte) ne se reproduisent pas sur cette machine (12 Go libres) ; en v2, `controles` est
  éprouvé avec un `df` factice et n'en dépend plus.
- Répétition jouet v2 par la commande, rejouée seule cinq fois de suite (entropies neuves) après la correction de l'essai
  (comparaison des valeurs non entières seulement : au jouet, une aire de pli vaut souvent 0, ½ ou 1 et coïncidait avec un
  compte) : 5 passed sur 5.
- Banc de mutations v2 (`scripts/banc_mutations_t06_v2.py`, journal `banc-mutations-t06-v2.log`, `.json`) : 4 témoins (vert, vert, vert, vert), **41 mutations, 41 tuées, 0 survivante(s) ou inapplicable(s)** ; durée Thu Nov  5 20:44:49 UTC 2026 → Thu Nov  5 20:51:18 UTC 2026 UTC. Au premier rejeu, la mutation « C07 : jeu décisif par jeu_croise » avait survécu (la répétition jouet n'a pas de tirage dégénéré) : l'essai `test_jeu_decisif_en_echec_sans_arret_du_run` (S100 sur une seule tâche par pli : un quart des rééchantillonnages la perd) a été ajouté et la tue.
- Disque : arbre de travail 2,4 Go (aucune installation) ; E0 effacée après lecture ; mémoire vive : pic 2 Go (E0 1/64).

## 4. Dix points pour un contre-lecteur

1. **Fuite différentielle fermée des deux côtés.** Le code ne met plus d'état dans `PROGRES` ; l'amorce, en plus, retient toute
   ligne `PROGRES` qui porterait un mot d'état (motif `MOTIF_INTERDIT`) et la compte. Vérifier que le motif ne retient aucune
   ligne légitime (E1 : 36 lignes relayées, 0 retenue) et qu'il couvre les mots du texte (« au-dessus », « non interprétable »,
   « échec », « plancher », aires, lignes).
2. **`run.json` sans lignes de table, résumé scellé avec.** `resume_imprimable` ; le résumé scellé reste la pièce du verdict.
   Le résultat scellé des sondes est poussé fermé (conception du texte) : relire si un chiffrement est voulu (nœud).
3. **Pas déclarés (L04).** `pas_declares` est vérifié avant le manifeste contre tâches × épisodes × époques / lot au plan (b) ;
   l'effectif après exclusions est écrit à côté (écart déclaré, pas un arrêt). Le nombre 480 est celui du lecteur ; Lazar tranche.
4. **Calendrier (L11).** La fin du GO n'est plus en dur : configuration → `session_v2 calendrier` (contre le registre) →
   `FIN_GO_UTC_S` à l'amorce → revérifiée contre la configuration clonée. Le dernier jour de création (15 novembre) bloque
   `controles` et `creation` le 16.
5. **Dépense cumulée (C08).** `creation` reçoit la dépense antérieure (registre des dépenses, à la main : seule valeur donnée à
   la main, à relire) ; le forfait de téléchargement = prix de l'offre × 40 Go ; l'heure d'épuisement passe à l'amorce et à la
   minuterie, qui consigne, pousse et demande « stopped ». Vérifier que la relance H200 (4,70 USD/h) entre bien par
   `DEPENSE_ANTERIEURE_USD` de la tentative A100.
6. **Morceaux (C11).** Borne 90 Mo sur la taille du fichier écrit ; `refuser_gros` relit `git diff --cached` avant chaque
   commit ; données légères d'abord. Vérifier qu'aucun autre fichier poussé (traces, `diag/`) ne peut dépasser 90 Mo : les
   traces sont des journaux ; `diag/<run>/lecture-sondes-t06.json` porte les jeux (quelques Mo) ; `refuser_gros` les couvre.
7. **Minuterie (C14, C08).** Bash et `curl` seuls, deux échéances ; `t06-consigner.sh` écrit par l'amorce après le clonage.
   Entre le démarrage et le clonage, rien n'est consignable (journal « rien à consigner »).
8. **Second démarrage (C13).** Trois cas : fin normale ou dépense épuisée → pousser puis dormir ; run interrompu → consigner
   puis détruire ; jamais relancer. L'état « stopped » obtenu → dormir (la session arrête par l'identifiant).
9. **E0 et Mahalanobis.** ≈ 26 ms par jeton, linéaire ; la clé `familles_descriptives` rend le retrait possible sans code ;
   la configuration réelle garde les cinq familles tant que Lazar n'a pas tranché. Relire la pente et l'extrapolation (deux
   points, machine partagée).
10. **Ce qui n'est pas éprouvé.** E2 (Vast : clone partiel avec jeton, PUT « stopped », DELETE, redémarrage réel), E3 (carte :
    mémoire de la distillation, déterminisme, débit des activations) ; noms d'offre Vast ; `MemTotal` contre 128 × 10⁹.

## 5. Commandes exactes

- Répétition jouet v2 (≈ 25 s) : `… python -m pytest -q tests/test_t06_v2_lanceur_jouet.py -k repetition` (commande complète en § 3).
- E0 : `flock /home/user/wt/.pytest.lock timeout 900 nice -n 10 python scripts/epreuve_e0_t06_v2.py <dossier> --echelle 1/64` ;
  E1 : `VENV=/home/user/controle-ia-travail/.venv timeout 900 nice -n 10 bash scripts/epreuve_e1_t06_v2.sh <dossier-neuf>` ;
  banc : `PYTHONPATH=src timeout 3000 nice -n 10 python -I -B scripts/banc_mutations_t06_v2.py SORTIE.json`.
- Course réelle (après scellement du candidat et de ses pièces, l'amorce v2 citée par son empreinte, la configuration réelle
  copiée sous `prereg/` avec `pas_declares`, `calendrier`, `carte`, `offre`, `familles_descriptives` ; la session exécute
  elle-même la commande imprimée) :
  1. `GO_ID=GO-2026-11-02-28 DEPOT_URL=https://github.com/lciric/controle-ia-travail.git bash scripts/lancer_t06_v2.sh controles <DOSSIER_NEUF>` ;
  2. `GO_ID=GO-2026-11-02-28 DEPOT_URL=https://github.com/lciric/controle-ia-travail.git bash scripts/lancer_t06_v2.sh creation <OFFRE> course <DEPENSE_ANTERIEURE_USD> <DOSSIER> [ECHEANCE_UTC_S]`
     (relance DT-6 : `… creation <OFFRE_H200> relance <DEPENSE_DE_LA_TENTATIVE_A100> <DOSSIER_NEUF>` après de nouveaux `controles`) → exécuter la
     commande imprimée (elle enchaîne `apres-creation`) ;
  3. `GO_ID=GO-2026-11-02-28 DEPOT_URL=https://github.com/lciric/controle-ia-travail.git bash scripts/lancer_t06_v2.sh surveillance <ID> <DOSSIER> [FACTURE_USD]` ;
     sur `ARRET …` ou `FIN`, exécuter `timeout -k 5 120 vastai stop instance <ID>` (R10) ; après le verdict, destruction par l'identifiant.
  Variables de l'amorce v2 (posées par la commande imprimée) : `COMMIT`, `PREREG`, `BRANCHE` (`calcul/t06-reel-v2`), `DEPOT_URL`,
  `ECHEANCE_UTC_S`, `FIN_GO_UTC_S`, `DEPENSE_EPUISEE_UTC_S`, `HF_TOKEN`, `GH_TOKEN`. Le plan daté du texte doit citer
  `scripts/lancer_t06_v2.sh <sous-commande> …` (couple L01, à porter sur la v2).

## 6. Nœuds et réserves pour Lazar (défauts choisis, tous en configuration)

- L04 : 480 pas déclarés (défaut du lecteur) ; L05 : « non interprétable » testé si au-dessus seulement (vrai) ; L11 : dernier
  jour de création 15 novembre, fin du GO `2026-11-17T00:00:00Z` ; L10 : H200 à 4,70 USD/h ; E0 : Mahalanobis dans les
  couples descriptifs (gardée par défaut, ≈ 8 à 30 h de calcul : recommandation, la retirer par `familles_descriptives`).

## 7. Trois risques

- Risque 1 — **durée du test croisé** : avec Mahalanobis, 8 à 30 h de carte payée (E0, extrapolée depuis deux points sur une
  machine partagée) ; sans elle, ≈ 2 h sur 4 cœurs ; le devis compte ≈ 1 h. À trancher avant le scellement.
- Risque 2 — **interface de Vast non tirée** (E2 absente) : noms d'offre (`gpu_name`), unités (`gpu_ram`, `cpu_ram` en Mo),
  `cpu_cores_effective`, `inet_down_cost`, PUT « stopped », DELETE, redémarrage réel : tout vient de SPARKS v12 et de P3,
  rien n'a été appelé ici ; une clé d'offre mal nommée bloquerait `creation` (sans dépense) ; une mauvaise unité laisserait
  passer une offre trop petite.
- Risque 3 — **gardes de l'instance jamais jouées sur la vraie chaîne** : clone partiel avec jeton, `python3.11 -m venv` et
  `requirements-gpu.txt`, suite complète des essais (nombre attendu cité), mémoire de la distillation (E3), `MemTotal` contre
  128 × 10⁹ ; et le résultat scellé des sondes poussé fermé mais lisible par quiconque ouvre le dépôt privé (conception du texte).
