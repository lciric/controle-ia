# Rapport du développeur neuf — lanceur de T0.6, v3 (additif aux rapports v1 et v2)

- Statut : rendu le 2026-11-05 22:09 UTC (heure relevée par `date -u`) par un développeur neuf (Claude Fable 5.1, sous-agent de la
  fille 7, T1 bis), qui n'a écrit ni le lanceur v1 ou v2, ni les contre-lectures, ni le texte. Brief suivi : brief T1 bis (A)
  (bloc-notes de la session). Pièces lues en entier, empreintes recalculées et égales : contre-lecture neuve du lanceur v2
  (`contre-lecture-lanceur-T0.6-v2.md`, `b49ca28b660e122fcfa5722bde4ae4b0b67914b008bd5290a63b2d2b9b8f1f2e`, verdict « lançable
  après corrections »), corrections de code (`corrections-code-lanceur-T0.6-v3.md`, `9a89626bce12095930e1bd10006213e9f284f0574fda7c71895198381eb2c792`,
  C-V3-1 à C-V3-4), outil de mesure `outils/mesure_mahalanobis_v1.py` et ses deux sorties (einsum gelé 21,2 et 18,4 ms par
  jeton contre 0,18 et 0,23 ms par produit matriciel, écart relatif 5 à 6 × 10⁻¹⁵). Rien n'est loué, aucun modèle n'est
  téléchargé ni appelé, aucune clé n'est lue, rien sous `donnees/` ni `diag/` n'est lu, aucun fichier existant n'est modifié
  (R12 : tous les fichiers neufs portent `_v3`, `v3`, `v4`, `brouillon3` ou `familles_v2`), aucun `.sha256` n'est écrit.
- Branche : `prep/t06-lanceur-v2` (arbre `/home/user/wt/t06-lanceur-v2`), par-dessus le lanceur v2 `0d48103b` ; jalons J1 à J5
  committés et poussés sur cette branche seulement ; dernier commit dans la réponse finale.
- **Signatures des sous-commandes de `scripts/lancer_t06_v3.sh` : inchangées de la v2** (le texte du candidat peut les citer
  telles quelles) : `controles DOSSIER_NEUF [JOUR]` ; `creation OFFRE CARTE DEPENSE_ANTERIEURE_USD DOSSIER [ECHEANCE_UTC_S]`
  (CARTE = course | relance) ; `apres-creation FICHIER CODE DOSSIER` ; `surveillance ID DOSSIER [FACTURE_USD]`. Seuls changent
  le nom du script (`_v3`), l'amorce citée (`scripts/amorce_instance_t06_v3.sh`, par son empreinte dans le texte de S), la
  branche par défaut (`calcul/t06-reel-v3`, `calcul/t06-<MODE>-v3` à l'amorce), et le lanceur joué (`controle_ia.t06.lanceur_v3`).
  Les variables de l'amorce (`COMMIT`, `PREREG`, `BRANCHE`, `DEPOT_URL`, `ECHEANCE_UTC_S`, `FIN_GO_UTC_S`,
  `DEPENSE_EPUISEE_UTC_S`, `HF_TOKEN`, `GH_TOKEN`) sont celles de la v2.

## 1. Fichiers neufs et empreintes (sha256 au dernier commit ; la mère scelle, aucun `.sha256` écrit ici)

| fichier | sha256 | lignes |
|---|---|---|
| `docs/notes/g0-deux-semaines-v1/avancement-v3.md` | `337636dfca72cfed383715e99a8f1082d2bbbbbfba9bebbbb88463cbd9140800` | 17 |
| `docs/notes/g0-deux-semaines-v1/banc-mutations-t06-v3.json` | `2ad2b3b461fb871741980c440c13e3009642c6da1b5d3bf18820178b675c4827` | 526 |
| `docs/notes/g0-deux-semaines-v1/banc-mutations-t06-v3.log` | `e59514340a117d4fe1fe3ad98705d0df0d9a4841550af9038363e3e2ac1a4990` | 64 |
| `docs/notes/g0-deux-semaines-v1/config-t06-jouet-v4.json` | `90634be97cc116c8da7cb818519e392b07188f198bdd9721fc869a3ca15ca299` | 139 |
| `docs/notes/g0-deux-semaines-v1/config-t06-reel-v1-brouillon3.json` | `915f858a44a5ad2d8f714626c5f4ec82f1a62def1a01da4738d367fccd7beb78` | 143 |
| `docs/notes/g0-deux-semaines-v1/epreuve-e1-t06-v3-journal.md` | `1c0fc075068533a3b3073a69162aabfee7bb98343ff5952644e41f3edc9ba904` | 207 |
| `scripts/amorce_instance_t06_v3.sh` | `16a03b8dfa1b1fc4e6331adc02b004b71e17b8f2c46044f5145085fb21e8cd8e` | 337 |
| `scripts/banc_mutations_t06_v3.py` | `298e50a5d2e6a382343daa76fa542c7ef126867066db66d6ae7c30fe426843cc` | 171 |
| `scripts/epreuve_e0_t06_v3.py` | `44da4b607f74d59cbb78f8f04f55deeecbd6fd369d2d36a68d50290d48e4d132` | 92 |
| `scripts/epreuve_e1_t06_v3.sh` | `7dccee9209beaf3ca4139fb675893ae4eb884635093cbb0be38a8ac21d724bcb` | 94 |
| `scripts/lancer_t06_v3.sh` | `2b45cea5c4204f906f25812f797d5f89e5b51a926e5a48c59f76c093f74a1036` | 172 |
| `src/controle_ia/sondes/familles_v2.py` | `4fea2c52b754fc180974c80ed9e83a3656d1b6aef7382a4451b7532a144153ad` | 94 |
| `src/controle_ia/t06/configuration_v3.py` | `e5083b8a56aafc522573c44ea9ad73648237916934fa6e876843bc72dafa92c0` | 35 |
| `src/controle_ia/t06/lanceur_v3.py` | `3bd8827aa33335aa2fdcc0f13437b9e6b6994944bed4fd9685bfb6e0648ccf09` | 414 |
| `tests/test_t06_v3_configuration.py` | `efe14a93b3e95123682094a29adf7866b59c40ae21f7292326f839dae9925a16` | 60 |
| `tests/test_t06_v3_familles.py` | `1a16acb5be45b2153e8d726b928557f4d35d367a2402d76eb7249e4bb7c1a802` | 76 |
| `tests/test_t06_v3_lanceur_jouet.py` | `5c33b75ef627875a3a7c5332754df817327b4ae5053e0363516831552c6ab179` | 407 |
| `tests/test_t06_v3_scripts.py` | `ae45170aef4d253039b1cc5224753103bf533a9d257ecbbc50999148e75cc456` | 543 |
| `docs/notes/g0-deux-semaines-v1/rapport-developpeur-lanceur-T0.6-v3.md` | (ce rapport : empreinte dans la réponse finale) | |

Fichiers v1, v2 et paquets gelés : inchangés (`git diff 0d48103b HEAD --stat` ne touche aucun fichier existant : vérifié,
sortie vide). `src/controle_ia/sondes/familles.py` (paquet gelé de T0.7) garde l'empreinte de `main`
`6758b651fdcbc6d0108a03263b79ffb1e7c5d0a8be57b0f10502c1645d2b457e` (essai `test_paquet_gele_intact`).

## 2. Traitement de C-V3-1 à C-V3-4

| correction | état | où, et comment c'est éprouvé |
|---|---|---|
| **C-V3-1** morceaux : borne de tableaux plus petite, fichier > 90 Mo réécrit en deux, jamais un arrêt | **fait** | `lanceur_v3.py` : `MORCEAU_MAX_OCTETS` 90 000 000 (borne du **fichier** écrit, gardée), `MORCEAU_TABLEAUX_MAX_OCTETS` 85 000 000, `borne_de_remplissage(n) = min(85 000 000, 90 000 000 − 1 000 000 − 1 000 × n)` (les deux formes de la correction, la plus petite retenue) ; `_ecrire_morceau` : un fichier écrit qui dépasse 90 000 000 octets est retiré et réécrit en deux (récursivement), consigné dans `reecrits` du manifeste et du résultat, jamais un `GardeArret` ; garde neuve **avant tout épisode** `exiger_action_tient_dans_un_morceau` (`max_nouveaux` × largeur × 2 octets ≤ borne d'une action ; réel : 3,3 Mo ≪ 85 Mo), qui rend impossible le seul cas encore arrêtant (« action plus grande qu'un morceau », gardé par défense). Essais (`test_t06_v3_lanceur_jouet.py`) : `test_sous_ensemble_en_morceaux_v3_borne_de_remplissage` (remplissage < fichier : aucune réécriture ; borne par action ; **artefact : remplissage = fichier, deux actions à 100 octets de la borne, fichier > borne → réécrit en deux, le run finit, et la v2 aux mêmes bornes arrête « morceau trop gros »**) ; `test_sous_ensemble_bornes_reelles_et_scenario_de_la_contre_lecture` (bornes réelles sur des actions de 222 × 4 096 en demi-précision : morceau de 46 actions, 83,7 Mo de tableaux, enveloppe < 30 ko, fichier < 90 Mo, aucune réécriture ; puis **le scénario du point 2 de la contre-lecture** : remplissage à la borne du fichier, 50 actions dont la somme tombe à 2 688 octets de 90 000 000, l'enveloppe fait dépasser le fichier de quelques ko, retiré et réécrit en deux morceaux de 25 actions, le run finit) ; `test_garde_action_tient_dans_un_morceau` (cas sain et artefact) ; répétition jouet (manifeste : `tableaux_max_octets` 85 000 000, `reecrits` vide, `octets_tableaux` ≤ borne). Banc : 3 mutations C-V3-1 tuées (borne de remplissage ramenée à 90 Mo ; arrêt restauré au lieu de la réécriture ; garde d'avant les épisodes retirée) plus les deux mutations C11 de la v2 rejouées. |
| **C-V3-2** amorce : second démarrage avant les contrôles d'heure | **fait** | `amorce_instance_t06_v3.sh` : la branche `amorce-depot` présent passe **avant** « démarrage après l'échéance » et « après l'heure de dépense épuisée » ; avec `t06-fin-normale` ou `t06-depense-epuisee` : `t06-consigner.sh "second démarrage"` d'abord (commits en attente poussés), **puis** destruction si l'argent est épuisé (marqueur posé par la minuterie, ou heure de dépense épuisée passée, code 0) ou si l'échéance est passée, sommeil après une fin normale ; run interrompu : consignation puis destruction (comme en v2). Les deux contrôles d'heure restent, après, pour un premier démarrage sans dépôt (rien ne part). `t06-consigner.sh` prend un verrou `flock` (`t06-consigner.lock`) : la minuterie (relancée au second démarrage, qui consigne elle-même à l'échéance) et l'amorce ne font jamais deux `git` à la fois sur le dépôt extrait ; `flock` ajouté aux outils exigés (util-linux). Essais (`test_t06_v3_scripts.py`) : `test_amorce_second_demarrage_apres_depense_epuisee_consigne_puis_detruit` paramétré sur trois cas, **heure de dépense épuisée dans le passé** relue au second démarrage (l'essai v2 la posait à + 10⁶ s), marqueur `t06-depense-epuisee`, échéance passée : commit en attente poussé (vu sur le dépôt distant) **avant** la demande de destruction, aucun sommeil, aucun run ; cas sain `test_amorce_cas_sain…` (fin normale, heures futures : poussée puis sommeil) ; `test_amorce_premier_demarrage_apres_depense_epuisee_detruit_sans_run` (sans dépôt : destruction sans clonage, C08 gardée). Banc : 3 mutations C-V3-2 tuées (contrôle d'heure remis avant la branche, comme en v2 ; sommeil au lieu de la destruction ; poussée omise) plus la mutation C13 de la v2. |
| **C-V3-3** `creation` : offre relue avec `--storage <disque_min_go>` | **fait** | `lancer_t06_v3.sh creation` : `offre.disque_min_go` lu dans la configuration des contrôles (150 Go), vérifié entier positif, puis `vastai search offers "id=<OFFRE>" --storage <DISQUE> --raw` ; `storage <DISQUE>` écrit dans `lancement.txt`. Essai : faux `vastai` qui journalise ses arguments et **refuse** une relecture sans `--storage <nombre>` ; l'essai exige la ligne exacte `search offers id=9999 --storage 150 --raw` puis `show instances --raw`. Banc : mutation « sans --storage » tuée. À comparer à E2 avec le prix de l'instance créée (point 9 de la contre-lecture). |
| **C-V3-4** Mahalanobis par produit matriciel, égalité au paquet gelé avant chaque usage, clé de configuration | **fait, défaut : paquet gelé** | `sondes/familles_v2.py` (le paquet gelé `sondes/familles.py` est intact) : `SondeMahalanobisV2`, même interface et mêmes paramètres (μ, P) que `SondeMahalanobis`, même empreinte, `scores_par_jeton` par `((z @ P) * z).sum(1)` ; `verifier_egalite_au_paquet_gele` : 256 jetons tirés (graine dérivée de celle de la sonde par `SeedSequence`, R9), écart relatif maximal ≤ 10⁻¹² contre le paquet gelé aux mêmes paramètres, sinon `GardeArret`. `configuration_v3.py` : clé **exigée** `mahalanobis_calcul` ∈ {`paquet_gele`, `produit_matriciel_v2`} (aucune valeur implicite, C04), **défaut `paquet_gele`** tant que Lazar n'a pas tranché ; la v2 est refusée si la sonde décisive était de la famille Mahalanobis. `lanceur_v3.test_croise_v3` : sous la v2, chaque sonde de Mahalanobis (2 sens × 2 plis par couple) est réécrite puis **vérifiée avant tout usage** ; un essai raté met **le couple** en « échec » (le `try` des couples descriptifs), jamais l'ensemble ; le calcul retenu et chaque essai (écart, graine, nombre de jetons) sont écrits dans le résultat scellé des sondes (`mahalanobis_calcul`, `verifications_mahalanobis`) et le résumé ; rien de cela en `PROGRES`. Configurations : `config-t06-reel-v1-brouillon3.json` et `config-t06-jouet-v4.json` = brouillon 2 et jouet v3 **plus la seule clé** `"mahalanobis_calcul": "paquet_gele"` (vérifié par l'essai de configuration v3). Essais : `test_t06_v3_familles.py` (égalité < 10⁻¹² par jeton et par action, même empreinte, interface, essai sur cas sain et artefact : formule altérée de 10⁻⁹ → `GardeArret`) ; répétition jouet paramétrée sur les deux calculs (sous la v2 : 12 essais d'égalité, tous égaux) ; `test_couples_mahalanobis_v2_egaux_au_paquet_gele_et_echec_borne_au_couple` (mêmes activations, mêmes graines : aires, bornes, quantiles de plancher des couples Mahalanobis égaux à 10⁻⁹ près entre les deux calculs ; essai raté simulé → les deux couples Mahalanobis en « échec », les autres jeux identiques, aucun arrêt, lecture T6-9 « échec »). Banc : 7 mutations C-V3-4 tuées. Durées : § 4. |

## 3. Comptes d'essais (commandes exactes, chacune sous le verrou de la machine, une suite à la fois)

- Préambule commun : `cd /home/user/wt/t06-lanceur-v2 && . /home/user/controle-ia-travail/.venv/bin/activate && export PYTHONPATH=src`,
  puis chaque suite par `flock /home/user/wt/.pytest.lock timeout 900 nice -n 10 python -m pytest -q -p no:cacheprovider --basetemp=/tmp/pytest-t06v3 <fichiers>`,
  suivie de `rm -rf /tmp/pytest-t06v3` (répertoire temporaire effacé après chaque suite ; jamais `-n`).
- Suite v1 (`tests/test_t06_cout.py tests/test_t06_distillation.py tests/test_t06_test_croise.py tests/test_t06_lecture.py tests/test_t06_session.py tests/test_t06_lanceur_jouet.py tests/test_t06_scripts.py`) :
  **76 passed in 47.73s** (Thu Nov 5 21:37:52 → 21:38:42 UTC 2026).
- Suite v2 (`tests/test_t06_v2_configuration.py tests/test_t06_v2_session.py tests/test_t06_v2_lanceur_jouet.py tests/test_t06_v2_scripts.py`) :
  **67 passed in 52.64s** (21:38:42 → 21:39:37 UTC) ; **les 143 essais de la v2 restent verts** sur les fichiers v1 et v2 intacts.
- Suite v3 (`tests/test_t06_v3_configuration.py tests/test_t06_v3_familles.py tests/test_t06_v3_lanceur_jouet.py tests/test_t06_v3_scripts.py`), rejouée au
  dernier état du code : **42 passed in 88.39s (0:01:28)** (22:07:06 → 22:08:37 UTC) : configuration v3 8 (dont 6 artefacts paramétrés),
  familles v2 3, lanceur jouet v3 10 (répétition jouet par la commande sous les deux calculs), scripts v3 21 (dont les 3 cas
  paramétrés de C-V3-2 et les 6 de calendrier et dépense). Le message du commit J2 dit « 37 » : compte de tête faux, le bon est 42.
- Banc de mutations v3 (`scripts/banc_mutations_t06_v3.py`, journal `banc-mutations-t06-v3.log`, résultat `.json`) :
  `TMPDIR=<bloc-notes>/banc-v3 PYTHONPATH=src flock /home/user/wt/.pytest.lock timeout 2400 nice -n 10 python -I -B scripts/banc_mutations_t06_v3.py docs/notes/g0-deux-semaines-v1/banc-mutations-t06-v3.json`
  (délai 2 400 s par prudence ; durée réelle 8 min 39 s, sous les 900 s) : 6 témoins verts, **55 mutations, 55 tuées, 0 survivante ou
  inapplicable** (Thu Nov 5 21:57:05 → 22:05:44 UTC 2026) : les 41 mutations de la v2 rejouées (sur `lanceur_v3.py`, l'amorce v3 et la
  chaîne v3 avec les essais v3 ; sur `configuration_v2.py`, `lecture_v2.py`, `session_v2.py` et les deux gardes C03 de `lanceur_v2.py`,
  partagés tels quels par la v3, avec leurs essais ; la mutation « C11 : morceau trop gros admis » vise la nouvelle forme de la garde et
  « C02 » remplace `resume_imprimable` importé), plus **14 mutations des corrections** : C-V3-1 ×3, C-V3-2 ×3, C-V3-3 ×1, C-V3-4 ×7.
  Un premier rejeu (21:41 → 21:50 UTC, 54 tuées) avait compté « survivante » la mutation « défaut v2 au lieu du paquet gelé » parce
  qu'elle écrivait un nom non importé (erreur d'import, code 2 de pytest, et non un échec d'essai) ; la mutation a été réécrite avec la
  chaîne littérale et le banc entier rejoué (c'est le rejeu consigné).
- Disque : arbre de travail inchangé (aucune installation) ; épreuves E0 (160 Mo + 124 Mo) et E1 effacées après lecture ; mémoire vive :
  pic 2,0 Go (E0 v3 au 1/64).

## 4. Mesure de durée de Mahalanobis v2 (C-V3-4), paquet gelé contre produit matriciel

Même protocole que l'épreuve E0 v2 (activations synthétiques, même entropie 20261105 donc **mêmes données**, 4 fils, `nice -n 10`,
réglages de lecture de la configuration réelle : 200 planchers, 200 permutations, 2 000 tirages), couche 7, par
`scripts/epreuve_e0_t06_v3.py` sous `produit_matriciel_v2` ; les durées « paquet gelé » sont celles de l'épreuve E0 v2
(`epreuve-e0-t06-v2-journal.md`, même machine, 20:04–20:27 UTC). Commandes :
`flock /home/user/wt/.pytest.lock timeout 900 nice -n 10 python scripts/epreuve_e0_t06_v3.py <bloc-notes>/e0-v3 --echelle 1/64 --calcul produit_matriciel_v2 --couche 7`
(21:51:48 → 21:54:39 UTC) et `… <bloc-notes>/e0-v3-256 --echelle 1/256 …` (21:55:08 → 21:57:04 UTC).

| échelle | jetons (couche 7) | mahalanobis-c7, paquet gelé (E0 v2) | mahalanobis-c7, produit matriciel v2 (E0 v3) | essais d'égalité | autres couples, E0 v3 (lineaire / perceptron / attention / décisif) |
|---|---|---|---|---|---|
| 1/256 | 5 058 | **144,0 s** | **54,4 s** | 4, tous égaux, écart relatif max 5,4 × 10⁻¹⁵ | 12,9 / 14,4 / 14,7 / 15,7 s (E0 v2 : 13,2 / 12,2 / 12,9 / 13,9) |
| 1/64 | 20 037 | **536,2 s** | **66,7 s** | 4, tous égaux, écart relatif max 4,5 × 10⁻¹⁵ | 19,7 / 26,0 / 30,3 / 21,9 s (E0 v2 : 16,1 / 21,8 / 22,6 / 18,8) |

- Pentes en jetons (deux points) : paquet gelé ≈ **26 ms par jeton** ; produit matriciel ≈ **0,8 ms par jeton** (le reste du couple :
  200 planchers notés, rééchantillonnage, permutations ; les autres familles ont des pentes de 0,2 à 0,65 ms). Constante : ≈ 12 s
  (gelé) contre ≈ 50 s (v2) : la différence est **l'essai d'égalité lui-même**, qui note 256 jetons par le paquet gelé (≈ 26 ms × 256
  ≈ 7 s par sonde, 4 sondes par couple ≈ 27 s) : coût fixe, négligeable à la taille réelle. La machine était 20 à 35 % plus lente
  pendant E0 v3 que pendant E0 v2 (autres couples : voir la table ; un autre sous-agent actif), ce qui majore la v2.
- Taille réelle (≈ 1,28 million de jetons notés par couche, 4 cœurs) : paquet gelé ≈ 9,3 h par couche (E0 v2) ; produit matriciel
  ≈ 50 + 0,8 × 1 280 ≈ **1 100 s ≈ 18 min par couche, ≈ 1 h pour les trois couples Mahalanobis** (contre ≈ 28 h), soit un gain
  d'environ 30 fois sur le couple entier (80 à 120 fois sur la seule notation, mesure de la contre-lecture). Sur 16 cœurs, moins.
- Jouet (E1 rejouée sous les deux calculs, 32 de largeur) : couples Mahalanobis 0,1 s dans les deux cas ; 12 essais d'égalité,
  écart relatif maximal 3,9 × 10⁻¹⁵ ; trop petit pour une mesure de durée.
- **Défaut gardé : paquet gelé** (nœud de Lazar). Pour la course, la valeur `produit_matriciel_v2` de `mahalanobis_calcul` est prête
  et éprouvée ; la retirer de la course (`familles_descriptives`) reste l'autre voie, sans code.

## 5. E1 rejouée avec le lanceur v3 sous l'amorce v3

`scripts/epreuve_e1_t06_v3.sh`, journal `epreuve-e1-t06-v3-journal.md` : vrai lanceur v3 (`controle_ia.t06.lanceur_v3`,
modèle par caractères) sous la vraie amorce v3, dépôt nu local, `vastai` absent du chemin, 0 USD ; 2026-11-05 21:50 UTC, 38 s,
code 0 ; 55 essais joués par l'amorce (nombre attendu vérifié) ; 36 lignes `PROGRES` neutres, dont `episodes-ecrits …
morceaux=1 reecrits=0` ; **0 mot interdit** dans le journal, `run.err`, `run.json` et les 8 traces poussées ; `run.json` sans lignes
de table, avec `mahalanobis_calcul` et `morceaux_reecrits` ; 1 morceau (14 actions, 6 400 octets de tableaux, fichier 11 346 octets :
≈ 350 octets d'enveloppe par tableau, ce qui confirme la mesure de la contre-lecture), manifeste v3 scellé (`tableaux_max_octets`
85 000 000, `reecrits` vide) ; trois commits poussés dans l'ordre (données légères, morceaux, traces) ; `t06-fin-normale`,
`t06-arret-demande`, aucun `t06-detruire`. Rejouée une seconde fois sous `produit_matriciel_v2` (`MAHALANOBIS_CALCUL_E1`) :
code 0, 12 essais d'égalité égaux (écart 3,9 × 10⁻¹⁵), 0 mot interdit. Le second démarrage (C-V3-2) n'est pas rejoué par E1 (sans
minuterie) : il est éprouvé par `tests/test_t06_v3_scripts.py` (trois cas, plus le cas sain).

## 6. Dix points pour un contre-lecteur

1. **C-V3-1, deux bornes.** Vérifier que la borne de remplissage est bien celle des tableaux (`a.nbytes`, demi-précision) et la
   borne de 90 Mo celle du fichier (`stat`), que `borne_de_remplissage(n)` prend la plus petite des deux formes, et que la
   réécriture en deux ne laisse aucun fichier > 90 Mo sur l'instance (`unlink` avant réécriture, numéros réattribués, manifeste
   `reecrits`). Le seul `GardeArret` restant (« plus grande qu'un morceau ») est rendu inatteignable par la garde d'avant les
   épisodes : relire `exiger_action_tient_dans_un_morceau` contre `max_nouveaux` et la largeur réelle (4 096).
2. **C-V3-1, scénario réel.** L'essai `…scenario_de_la_contre_lecture` rejoue le point 2 de la contre-lecture avec les constantes
   réelles (50 actions, 2 688 octets sous la borne) : il écrit ≈ 180 Mo dans le répertoire temporaire ; vérifier qu'il tient dans
   les limites de disque de la machine de contre-lecture.
3. **C-V3-2, ordre.** Dans l'amorce v3, lire la branche `amorce-depot` : consigner d'abord, décider ensuite ; vérifier que la
   minuterie relancée juste avant (échéance passée → elle consigne aussi) et l'amorce ne se gênent pas : verrou `flock` dans
   `t06-consigner.sh` (la fin de run de l'amorce, elle, commit sans verrou comme en v2 : risque 3).
4. **C-V3-2, codes de sortie.** `detruire … 0` après un second démarrage « argent épuisé » : code 0 (rien d'anormal : la poussée a
   eu lieu) ; en production `detruire` attend la minuterie puis `exit`. Vérifier que `sommeil` n'est atteint que pour une fin
   normale avec les deux heures encore à venir.
5. **C-V3-3.** `--storage` est passé avec la valeur de `offre.disque_min_go` (150) ; l'outil réel accepte-t-il `--storage` sur
   `search offers` avec `--raw` (E2) ? Le faux `vastai` de l'essai l'exige ; une syntaxe différente de l'outil réel bloquerait
   `creation` sans dépense.
6. **C-V3-4, défaut.** La configuration réelle brouillon 3 garde `paquet_gele` : la course réelle, telle quelle, paie encore
   ≈ 8 à 30 h de Mahalanobis (nœud de Lazar, point 8 de la contre-lecture). Passer à `produit_matriciel_v2` est une valeur de
   configuration, à sceller avec le texte.
7. **C-V3-4, essai d'égalité.** 256 jetons tirés autour de μ à l'échelle 1/√diag(P) ; écart relatif ≤ 10⁻¹² ; mesuré ≈ 10⁻¹⁵.
   Vérifier que la graine de l'essai (dérivée de celle de la sonde, `spawn_key=(1,)`) est écrite au résultat et que l'essai est
   bien joué avant chaque usage (une fois par sonde, 12 fois au jouet, 2 couches × 2 sens × 2 plis par couple).
8. **C-V3-4, égalité des lectures.** `test_couples_mahalanobis_v2…` compare aires, bornes et quantiles de plancher des couples
   Mahalanobis entre les deux calculs à 10⁻⁹ ; les planchers (sondes linéaires) ne dépendent pas du calcul ; seule la sonde
   change de formule.
9. **Suites et banc.** Les 143 essais v1 et v2 restent verts (rejoués) ; 37 essais v3 ; banc v3 : toutes les mutations v2 rejouées
   sur les fichiers v3 (celles de `configuration_v2`, `lecture_v2`, `session_v2` et des deux gardes C03 de `lanceur_v2` portent
   sur les fichiers partagés, importés tels quels par la v3) plus 14 mutations des quatre corrections.
10. **Ce qui n'est pas éprouvé.** E2 et E3 (Vast, carte) inchangées ; la syntaxe `--storage` de l'outil réel ; le verrou `flock`
    sur l'image de l'instance (installé si absent, util-linux) ; la durée de Mahalanobis v2 sur 16 cœurs.

## 7. Nœuds et réserves pour Lazar (défauts pris)

- Mahalanobis (point 8 de la contre-lecture) : défaut **paquet gelé** gardé dans la configuration réelle brouillon 3 ; la v2
  (option (d)) est en place, éprouvée égale, et se choisit par `mahalanobis_calcul`.
- Branche par défaut `calcul/t06-reel-v3` et amorce v3 : à citer par le texte (couples du candidat ; signatures inchangées).

## 8. Trois risques

- Risque 1 — **Mahalanobis encore au paquet gelé par défaut** : tant que Lazar n'a pas tranché, la configuration réelle brouillon 3 fait
  payer ≈ 8 à 30 h de carte pour trois couples descriptifs ; la v2 (≈ 1 h sur 4 cœurs, égalité éprouvée à 10⁻¹⁵) et le retrait par
  `familles_descriptives` sont deux valeurs de configuration prêtes ; la décision doit précéder le scellement du candidat.
- Risque 2 — **interface de Vast non tirée** (E2) : `vastai search offers "id=…" --storage 150 --raw` est la forme supposée de l'outil
  (documentation, pas d'appel ici) ; une syntaxe différente bloquerait `creation` sans dépense ; et `flock` doit exister sur l'image
  (`util-linux`, installé par l'amorce s'il manque, sinon refus précoce). C-V3-3 doit être confirmée par le prix de l'instance créée.
- Risque 3 — **concurrence résiduelle sur le dépôt extrait** : `t06-consigner.sh` est sous verrou (minuterie et second démarrage),
  mais la fin de run de l'amorce (commits des résultats, des morceaux et des traces) commit sans verrou, comme en v2 : si la
  minuterie consigne au même instant (dépense épuisée ou échéance tombant pendant la poussée finale), un `index.lock` peut faire
  échouer un commit ; la poussée en trois essais et le second démarrage (C-V3-2) rattrapent les commits restés en attente, mais
  pas un commit jamais fait. À relire pour une v4, ou à éprouver en E2 par une échéance posée pendant la poussée.
