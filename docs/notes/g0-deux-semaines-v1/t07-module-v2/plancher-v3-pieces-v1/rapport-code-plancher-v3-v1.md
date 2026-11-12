# Rapport du développeur : code du plancher v3 de T0.7 (remède (a') : règle (a) et 800 directions) — v1

Écrit le 2026-11-11, de 00:45 à 02:34 UTC (heures relevées par `date -u`), par un **développeur neuf** (Claude Opus 5.5,
`claude-opus-5-5`, sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`), qui n'a écrit ni T0.7, ni son module, ni
les notes de l'analyste, ni le plancher v2. Consigne :
`docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-code-plancher-v3-t07-v1.md`
(`88879387fe432e77e8541d7f63e9afcc1b299b3aafd1966c70f974b3c29beadd`, vérifiée par `sha256sum -c` avant lecture). **Préparation
réversible, non fusionnée dans `main`** (règle C7, R-2231). J'ai lu le texte de T0.7 (candidat 1, sections citées) et son
module : **je suis exclu de tout rôle de lecteur de P3-bis.** Aucune donnée de 7a, de 7b ni de P3-bis ; aucun appel de modèle ;
aucune instance ; aucune dépense. Données de P3 lues (permises) : manifeste, `sondes-figees.json`, fichier léger, données
génériques versées, traces de la régénération R-679 (branche `calcul/regeneration-sondes-p3-v1`, fichiers `run.err`,
`journal.txt`, `machine.txt`, `verdict-regeneration-v1.json`).

## Verdict

**Code du plancher v3 écrit, éprouvé et poussé** sur `prep/t07-plancher-v3-v1` (partie de `adb5f415`), **commit final
`0d0c5da4061c28d808c3aa3b53c9a9a5e56a3a07`** (deux commits : `6f9b4521`, puis palier et réserves portés jusqu'à l'étape B) ;
neuf fichiers neufs, aucun fichier existant modifié.

- **800 directions en mode réel** (`lecture_v4`, configuration **v7** : la v6 plus `n_plancher` = 800 et la clé neuve
  `plancher_figees` ; empreinte canonique **`4ff92c8e…`**) ; la v7 est **refusée par `lecture_v3` et `lecture_v2`**.
- **Notation vectorisée** (`plancher_v3.scores_plancher_vectorises`) : agrégation **égale au bit près** à la boucle à scores
  par jeton égaux ; produit par lots **non égal au bit près** (ordre des sommes de `dgemm` ≠ `dgemv`), écart mesuré ≤ 10⁻¹⁴ de
  l'échelle (tolérance 10⁻¹²) ; **≈ 50 à 70 fois plus rapide** que la boucle (mesuré ici).
- **Réextraction des jetons d'entraînement des sondes figées de P3 à l'étape A** (`reextraction_p3_v1`), code de P3 appelé tel
  quel, **garde d'identité à trois paliers** et **seconde garde** (la graine `plancher/<concept>` se lit dans le manifeste de
  P3 : les 200 directions sont redonnées et comparées) ; puis 800 directions neuves sous la graine de T0.7 ; **repli : arrêt du
  seul bras, motif écrit, aucune bascule vers les 200 de P3** ; les 200 de P3 notées et lues en descriptif.
- **Constat qui touche la consigne (à trancher)** : la sonde principale des enjeux (linéaire, Adam, 300 époques) est
  **chaotique** : au calibrage, un bruit de 10⁻⁴ par jeton change ses poids de **49 %** ; aucune tolérance au-delà de
  l'arithmétique ne sépare le bruit de carte d'une faute. **Proposition** (configuration v7 : `garde_principale` =
  « rapportee ») : la garde d'identité décisive porte sur un **témoin déterministe** (la sonde « différence de moyennes » du
  même concept, de la même couche, mêmes jetons ; pour la tromperie, la principale elle-même) et sur la seconde garde ; la
  principale refaite est rapportée (réserve si elle s'écarte). La lettre de la consigne (« decisive ») reste offerte par la
  même clé.
- **Essais** : 60 passés, 1 sauté (fichier v7 hors de l'extraction) dans les trois fichiers neufs ; **suite T0.7 de l'arbre :
  514 passés, 27 sautés (extraction réduite), 3 `xfail`, aucun échec** ; **banc de mutations : 37 mutations, 36 tuées, 1 équivalente, import tracé de la copie**.
- **Devis** : temps ajouté à l'étape A **≈ 0,23 h attendues, ≈ 0,66 h au pire (sans rien retirer au devis)** ; **+ 0,30 USD attendu, + 0,86 USD au pire à 1,30 USD de l'heure** ; **le total tient sous 20 USD** (variante B : attendu ≈ 5,5 à 7,4 USD, pire ≈ 12,5 à 16,4 USD), mais
  la marge du pire cas à la minuterie de 12 h se réduit (§ 8).

## 1. Lu (empreintes vérifiées)

- Note v3 de l'analyste, `docs/notes/g0-deux-semaines-v1/t07-module-v2/erreur-premiere-espece-lectures-decisives-t07-v3.md`
  (`760a562c15991421e6c1eca2b8f65072d82976a956482c599fdeb0cc1c46b602`, égale à son compagnon), entière (sections 5, 6 et 8
  surtout) ; v1 (`8e996ab0…`) et v2 (`5ccf0940…`) : empreintes seulement. Rapport du développeur du plancher v2
  (`rapport-developpeur-plancher-v2-v1.md`, `e285ae0d…`), pour la méthode (miroir, banc).
- Configuration v6, `docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v2-pieces-v1/configuration-t07-v6.json`
  (`475669dec1081f1bbde4a87d2e7c254772c08642ecef8e70b284d8ea35ce6364`, compagnon conforme ; canonique `7c61fcfb…` recalculée).
- Candidat 1 de T0.7, `brouillons/T0.7-sondes-v0-v1-candidat1.md` (`1718f2a0…`) : « Métrique », plancher (l. 1078-1100), ligne
  3 de la table l. 381 (« planchers de P3 » : voie de réextraction écartée au brouillon 12), « Calcul et dépense » (l. 1979-2013).
  Ordre d'exécution `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon5.md` (`d0b75d16…`) : commandes (§ 4.6, étapes 11 à
  13 : `lecture_v2 repli-seul`, `passe-blanc`, `etape-a-apres-repli`), devis (§ 6). Lignes de GO `GO-2026-11-10-04` et
  `GO-2026-11-10-06` (`registres/go.md`).
- Code au commit `adb5f415` : `plancher_v1.py` (`ac6e8263…`), `lecture_v1.py` (`62b34790…`, l. 534-575 et 683-705 lues),
  `lecture_v2.py` (`709b2feb…`), `lecture_v3.py` (`ac3666e4…`), `passe_blanc_v1.py` (`ff84d245…`), `repli_etapes_v1.py`
  (`26a6b521…`), `donnees_p3_t07_v1.py` (`acf02303…`), `sondes_neuves_v1.py` (`d4d354e7…`), `sondes/evaluation.py`
  (`1040674c…`, `plancher_apparie` gelée), `sondes/familles.py` (`6758b651…`), `harnais/sondes.py` (`f92657a6…`).
- **Code et données d'entraînement de P3** (étapes 1 à 4) : `premier_test_ia/run.py` (`b3f14d8e…` ; `_executer_apres_manifeste`,
  l. 393-440 : réglages, format, données, extraction, découpage, entraînement, planchers), `premier_test_ia/entrainement.py`
  (`7e701026…` : `preparer_tromperie`, `preparer_enjeux`, `extraire`, `plancher_de`), `premier_test_ia/donnees.py` (`fa89340e…` :
  `charger_faits`, `exemples_tromperie`, `charger_enjeux`, `tirer_enjeux`, `decouper`), `premier_test_ia/empans.py` (`58043c95…`).
  **Inchangés depuis le commit de P3** `97dd8290` (différentiel vide sur `premier_test_ia/{run,entrainement,donnees,empans,figees}.py`,
  `harnais/{activations,formats,modeles,run_harnais_factice}.py`, `sondes/{familles,evaluation}.py`,
  `environnements/lancer_pilote_a.py`) ; versions épinglées inchangées (`torch` 2.14.1, `transformers` 5.18.0, `numpy` 2.4.6).
  Données versées : `donnees/T0.7-faits-repe-v1/facts_true_false.csv` (`151b6163…`), `donnees/T0.7-models-under-pressure-v1/training/train.jsonl`
  (`04216df3…`). Run de P3 : `runs/20261019-230011-p3-reel/manifeste.json` (`3f21774c…` : configuration, 96 graines dont
  `tirage-enjeux`, `decoupage-<concept>`, `sonde/<nom>`, **`plancher/tromperie` et `plancher/enjeux`** : la seconde garde est
  possible), `diag/20261019-230011-p3-reel/sondes-figees.json` (`fb418127…` : 7 faits exclus, 2 000 lignes des enjeux, effectifs
  478/120 et 1 591/409, principales, 30 fils d'entraînement), `donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz`
  (`701f73bd…`). P3 a tourné sur **A100-SXM4-80GB**, CUDA 13.0, `torch` 2.14.1+cu130, réglages déterministes
  (`episodes-p3.json`, `reglages`).
- **Régénération R-679** (`calcul/regeneration-sondes-p3-v1`, commit `6e9fc847`, `traces/regeneration-sondes-p3-20261029-002107-J894/`) :
  sur une autre A100-SXM4-80GB (EPYC 7513, 30 fils de torch, OpenBLAS à 64), le fichier complet de P3 redonné **au bit près** ;
  durées relevées : extraction des 2 598 exemples (trois couches) **78,5 s**, entraînement des 15 sondes de la tromperie 72 s,
  des enjeux 26,6 min (la linéaire `enjeux-lineaire-c15` : 114 s dans P3).

## 2. Ce que fait le code (fichiers neufs seulement, R12)

| fichier (commit `0d0c5da4`) | sha256 | lignes |
|---|---|---|
| `src/controle_ia/t07/plancher_v3.py` | `c25a8822dc4a59d6d3a98b70f8b7aa92c45bbfdb571e482abf2a1a55ba440cd8` | 211 |
| `src/controle_ia/t07/reextraction_p3_v1.py` | `fe9b48e3bdd83e83da29d79947748346ca56be535a8be401ad8f290f553ee8a1` | 467 |
| `src/controle_ia/t07/lecture_v4.py` | `5cb4c44872472b94d995c9ace11530655539cfc68ec06874e0f6b6d005ae7d19` | 738 |
| `src/controle_ia/t07/passe_blanc_v2.py` | `66d1b5151c5dd6eb463f37d5f4987abb097afc50f64e2aa9e0adb2b5b40ba974` | 505 |
| `src/controle_ia/t07/repli_etapes_v2.py` | `70f587da4c68c90f6dcb7970cc4bd4d26d2a41dfdd1475aac255075404c91476` | 171 |
| `tests/miroir_plancher_v3_v1.py` | `bec93894e342b7b8be437a9d104220195031a36c9da119b5a08bf707bce840a5` | 160 |
| `tests/test_t07_plancher_v3_notation_v1.py` | `aabda246d2169add12ebeb6cdd79e00c0668c45951521aae5c037dbb0238d63b` | 185 |
| `tests/test_t07_plancher_v3_reextraction_v1.py` | `2628df5522c17be081159bed3e02bda289d2d3195f90b1a99d685a7cdde4e279` | 372 |
| `tests/test_t07_plancher_v3_lecture_v1.py` | `19708ac26eafc10e4d1e0a6549896315bc6a10e444b12a9d4231c95871998e9a` | 321 |

- **`plancher_v3.py`** (point 2) : `N_PLANCHER_REEL = 800`, `N_PLANCHER_P3 = 200` ; `scores_plancher_vectorises(plancher,
  sequences, taille_lot=4096, controle=2)` : directions mises en matrices (W, b, Q ; `SondeLineaireJetons` seule, même couche, même
  agrégation, maximum ou attention), actions mises bout à bout par lots d'au plus `taille_lot` jetons (une action jamais coupée,
  mémoire bornée : ≈ 0,16 Go par lot à 800 directions), passage exact en double précision, `A @ W + b`, puis **même agrégation que
  `harnais.sondes.score_action`** : maximum (`np.maximum.reduceat`, exact) ou attention (par action et direction : `exp(l − max l)`,
  division par la somme, somme des poids × scores, sommes faites le long de l'axe contigu comme dans la boucle) ; **jamais la
  moyenne ni la médiane** ; mêmes refus que la boucle (agrégation, empan vide, non fini). **Contrôle en ligne (garde R5)** à chaque
  appel de production : les 2 premières directions renotées par la boucle du harnais sur une action sur 8 et la dernière ; écart
  rapporté à l'échelle (max sur les jetons de |a|·|w| + |b|, plus 2 · max |a|·|q| · max |a·w + b| pour l'attention) au-delà de
  **10⁻¹²** → arrêt (aucune bascule).
- **`reextraction_p3_v1.py`** (point 3) : docstring du module, résumé :
  1. entrées de P3 par la clé `donnees_p3` (déjà dans la v6 : quatre fichiers à leur empreinte, `donnees_p3_t07_v1.controler`) ;
  2. **réglages de P3** (`harnais.modeles.regler_determinisme(fils de P3, carte)`, posés avant tout calcul de la réextraction et
     rétablis à la sortie) ; **modèle et format de l'agent de P3** (`charger_modele_et_format(config.agent de P3, …)`, cache local,
     graine « modele-jouet » en jouet), contrôle du format de P3 ;
  3. données et découpage de P3 (fonctions de P3, graines du manifeste de P3) avec gardes d'égalité : faits exclus, lignes des
     enjeux, nombre d'exemples, effectifs ;
  4. extraction des seuls exemples d'entraînement à la couche de la sonde (`entrainement.extraire`, simple précision) ;
  5. **garde d'identité** (§ 5) ; 6. **800 directions** par `plancher_apparie` sur ces jetons, **graine de T0.7** clé
     `plancher/<sonde>` (au manifeste de T0.7), noms `<sonde>-t07-plancher-<k>` ; fichier `donnees/<run-t07>/planchers-figees-t07.npz`
     (`figees.ecrire_sondes`, scellé) ; rapport `diag/<run-t07>/reextraction-p3-t07.json` (scellé).
  **Repli** : toute faute (entrée, modèle absent du cache, données, garde, carte) arrête **le seul bras** de la sonde concernée
  (« échec », motif écrit, type de l'exception compris) ; jamais l'étape A ; jamais les 200 de P3 en décisif.
- **`lecture_v4.py`** (points 1 et 3) : tête écrite à la main, plus trois **copies déclarées** (générateur du bac à sable,
  remplacements de `tests/miroir_plancher_v3_v1.py`) :
  - `exiger_configuration` : `plancher_figees` exigée (`CleAbsente`) ; en mode réel **`n_plancher` = 800** (200, 799, 800.0,
    `True` refusés), `donnees_p3` non nulle, tolérances égales à celles du module ; puis **tous les contrôles de `lecture_v3`
    et de `lecture_v2`**, joués sur la configuration où `n_plancher` vaut 200 (seule la garde « 200 » de la v2, l. 205-206, est
    ainsi remplacée : déclaré) ;
  - `charger_planchers_p3` : `lecture_v1.charger_planchers_p3` au nombre `plancher_figees.n_p3` (200 en réel ; le contrôle
    « nombre » de la v1 portait `n_plancher`) ;
  - `noter` (copie de `lecture_v2.noter`) : `pl.scores_plancher` → `pl3.scores_plancher_vectorises` (sondes, T7-P6, concepts) ;
    pour les figées : directions de P3 notées en descriptif (`plancher_p3_<k>`), bras arrêté → « échec » de la sonde avec motif
    (scores et directions de P3 gardés), palier et réserves de la garde dans l'index ;
  - `etape_a` (copie de `lecture_v2.etape_a`) : graines `plancher/<figée>` et `descriptif-p3/<figée>/<jeu>` au manifeste ;
    **réextraction placée avant toute autre extraction du processus** (juste après `ouverture-t07.json`, avant les sondes
    neuves) : les réglages de P3, l'espace de cuBLAS compris, sont posés avant le premier calcul sur la carte ; le modèle de P3
    est libéré avant le chargement de celui de la course ; `notation-t07.json` porte `planchers_figees` (fichier, états, paliers) ;
  - `etape_b` (copie de `lecture_v3.etape_b`) : contrôle v4, **lecture descriptive des 200 de P3** (`lecture_planchers_p3` :
    `lecture_jeux_v3` à 95 %, règle (a), hors jugement, même si le plancher neuf est en échec), réserves du plancher des figées
    recopiées dans `resultat.reserves` ; `methode_plancher` porte `n_plancher`, la notation et la méthode des figées ;
  - commande : `etape-a`, `etape-b`, `empreinte-config`, `grille` (celle de la v2), `passe-blanc`, `repli-seul`,
    `etape-a-apres-repli` ; **`repli-recalcul` refusé** (code 2 ; jouer les deux temps).
- **`passe_blanc_v2.py`, `repli_etapes_v2.py`** : `passe_blanc_v1.py` et `repli_etapes_v1.py` **à la lettre**, sauf la
  configuration (contrôle et chargement de `lecture_v4`), l'étape A appelée après le repli (`lecture_v4.etape_a`) et le nom de la
  commande ; nécessaires parce que la v1 refuse la v7 en mode réel (essai). Ni la passe à blanc ni le repli ne lisent de plancher.

## 3. Configuration v7 (point 1)

`docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/configuration-t07-v7.json`, sha256 du fichier
**`3701407cf96f2851de26b04df174432a6e5325227c1e1f5a24900a1fa44ef6ab`**, **empreinte canonique
`4ff92c8ef07943e093793c218967be36621410714be9634ccccc3c27811d2b38`** (`lecture_v4 empreinte-config`, code 0 ; la v6 y est refusée,
code 2, « clé plancher_figees absente » ; la v7 est refusée par `lecture_v3 empreinte-config`, code 2, « n_plancher 800 ≠ 200 »).
Différence avec la v6 (vérifiée par `diff`) : `"n_plancher": 800` (au lieu de 200) et la clé neuve
`"plancher_figees": {"methode": "reextraction_p3_v1", "n_p3": 200, "tolerances": {"processeur": 1e-06, "carte_sonde": 0.01,
"carte_directions": 0.1}, "garde_principale": "rapportee"}`. Rien d'autre (la clé `donnees_p3` est déjà dans la v6).
**`garde_principale` = « rapportee » est ma proposition** (§ 5) ; « decisive » donne la lettre de la consigne, empreinte
canonique alors autre.

## 4. Notation vectorisée : égalité à `scores_plancher` (point 2)

- **Au bit près, si possible** : l'**agrégation** l'est (essai : à scores par jeton pris dans la boucle, maximum et attention
  rendent au bit près `pl.scores_plancher`) ; le **produit matriciel par lot** ne l'est pas : la boucle fait un produit
  matrice-vecteur (`dgemv`) par direction et par action, le lot un produit matrice-matrice (`dgemm`) dont l'ordre des sommes
  diffère. **Écart déclaré** : |vectorisé − boucle| ≤ 10⁻¹² × échelle de l'action ; **mesuré ≤ 10⁻¹⁴** (de l'ordre de
  3 × 10⁻¹⁶) sur 20 tirages aléatoires (largeurs 8 à 64, 1 à 50 directions, lots de 1 à 10 000 jetons, une action plus longue
  qu'un lot) et sur les activations du faux run de 7b (jouet), maximum et attention ; 7 à 16 % des scores sont égaux au bit près.
- **Débit** (mesuré ici, quatre cœurs partagés avec la suite d'essais, 800 directions, largeur 4 096, actions de 225 jetons) :
  sur machine au repos (après le redémarrage du conteneur, `mesure-cout-v2.json`), notation vectorisée **57,8 s par million
  de jetons** (maximum) et **87,9 s** (attention) ; boucle du harnais **1 022 µs** (maximum) et **1 568 µs** (attention) par
  direction et par action de 225 jetons (la note v3 relevait 235 à 904 µs pour 50 à 200 jetons) : **≈ 63 fois plus rapide**.
  Sous charge (suite d'essais et banc en parallèle, `mesure-cout-v1.json`) : 115 et 192 s, 5 538 et 11 103 µs. Contrôle en ligne :
  ≈ 0,55 ms par action notée (une action sur huit, deux directions), soit ≈ 3 s par plancher de 5 760 actions.
- Le contrôle en ligne ne voit pas un écart limité aux actions ou directions non contrôlées (borne déclarée ; l'égalité sur
  toutes est éprouvée par les essais).

## 5. Garde d'identité : tolérance et justification (point 3)

**Ce qui est comparé** (fichier léger `701f73bd…`) :
- **témoin déterministe (décisif)** : la sonde « différence de moyennes » du même concept et de la même couche, refaite par
  `familles.entrainer` sur les jetons réextraits : `tromperie-difference_moyennes-c15` (la principale de la tromperie elle-même)
  et `enjeux-difference_moyennes-c15` (un des 24 couples du fichier léger) ; fonction directe des jetons d'où l'on tire Σ ;
- **seconde garde (décisive)** : les 200 directions de P3 redonnées par `entrainement.plancher_de` sous la graine
  `plancher/<concept>` du manifeste de P3, comparées aux 200 du fichier léger (noms, `w`, `b`) ;
- **principale refaite** par la recette de P3 (famille, couche, agrégation, graine `sonde/<nom>`, réglages par défaut, 30 fils
  de torch comme P3) : pour la tromperie, c'est le témoin ; pour les enjeux (linéaire), rapportée (`garde_principale` =
  « rapportee », réserve si elle sort du palier « processeur ») ou décisive (« decisive »), sans palier « carte » dans les deux cas.

**Écart** : ‖x′ − x‖ / ‖x‖ pour `w` (et `q`) ; |b′ − b| / (|b| + ‖w‖ · max ‖h‖) pour `b` (max ‖h‖ : plus grande norme d'un jeton
réextrait ; aucune moyenne sur les jetons) ; maximum sur les 200 directions.

**Tolérance fixée d'avance (configuration v7, contrôlée à l'égalité en mode réel), trois paliers** :

| palier | témoin | directions de P3 | lecture |
|---|---|---|---|
| identique | égalité au bit près | égalité au bit près | attendu (R-679) |
| processeur | ≤ 10⁻⁶ | ≤ 10⁻⁶ | ordre des sommes (fils, noyaux d'algèbre linéaire) ; aucune réserve |
| carte | ≤ 10⁻² | ≤ 10⁻¹ | accepté **avec réserve écrite** (non-déterminisme de la carte présumé), recopiée à l'étape B |
| échec | au-delà | au-delà | arrêt du seul bras (R11), motif écrit |

**Justification** (calibrage du bac à sable, `calibrage_gardes_v1.py` `df111323…` et `v2` `7ed65865…`, sorties
`calibrage-gardes-v1.json` `c5d4650e…` et `-v2.json` `46dce2f5…` ; jetons synthétiques de largeur 4 096, **spectre de Σ estimé sur
les 200 directions de P3** ; recettes gelées appelées telles quelles ; écart relatif de `w`) :

| perturbation | témoin, tromperie (2 444 jetons) | témoin, enjeux (12 154) | directions, tromperie | directions, enjeux | linéaire, enjeux |
|---|---|---|---|---|---|
| fils 1 contre 4 (processeur) | 0 | 0 | 6,1 × 10⁻¹¹ | 4,7 × 10⁻¹⁴ | 0 |
| bruit « carte » 10⁻⁴ par jeton | 4,4 × 10⁻⁵ | 2,2 × 10⁻⁵ | 8,5 × 10⁻⁴ | 2,3 × 10⁻⁴ | **0,49** |
| bruit « carte » 10⁻³ | 4,4 × 10⁻⁴ | 2,2 × 10⁻⁴ | 8,3 × 10⁻³ | 2,2 × 10⁻³ | **0,49** |
| bruit « carte » 10⁻² | 4,4 × 10⁻³ | 2,2 × 10⁻³ | 7,0 × 10⁻² | 2,3 × 10⁻² | **0,56** |
| faute : un exemple retiré | 6,7 × 10⁻³ | 4,3 × 10⁻³ | 1,6 × 10⁻² | 7,2 × 10⁻³ | 0,50 |
| faute : empan décalé d'un jeton | 0,12 | 2,4 × 10⁻² | 0,18 | 3,7 × 10⁻² | 0,58 |
| faute : autre découpage (20 %) | 0,11 | 6,0 × 10⁻² | 0,18 | 9,0 × 10⁻² | 0,91 |
| faute : autre couche | 1,5 | 1,4 | 1,7 | 1,6 | 1,5 |

- **Non-déterminisme de la carte** : sous les réglages de P3 (algorithmes déterministes, TF32 et réductions réduites coupés,
  espace de cuBLAS `:4096:8`), sur la carte de P3 (A100-SXM4-80GB, exigée par l'ordre d'exécution) et avec les versions
  épinglées, la régénération R-679 a redonné **au bit près** le fichier complet de P3 sur une autre machine : l'extraction est
  reproductible au bit ; le module pose ces réglages **avant tout calcul sur la carte** du processus de l'étape A. Restent les
  écarts du processeur (fils, noyaux d'OpenBLAS selon le processeur hôte) : mesurés ≤ 6 × 10⁻¹¹, d'où le palier « processeur »
  à 10⁻⁶ (quatre ordres de marge ; trois sous la plus petite faute). Si la carte s'écartait malgré tout, le palier « carte »
  l'admet jusqu'à un bruit d'environ 2 × 10⁻² par jeton (témoin) ; au-delà, ou pour une faute de données, d'empan, de découpage
  ou de couche, la garde arrête (marges : × 2,4 à × 11 sur l'empan décalé et le découpage ; × 100 sur la couche).
- **Recette linéaire chaotique** : 300 pas d'Adam depuis zéro sur une sonde au maximum, largeur 4 096 ≫ exemples : un bruit de
  10⁻⁴ par jeton ou un exemple retiré changent les poids d'environ 50 %. Aucune tolérance n'y sépare la carte d'une faute :
  seuls « identique » et « processeur » passent. Sur un hôte dont le processeur diffère de celui de P3 (EPYC 7513), les noyaux de
  `torch` (AVX2 contre AVX-512) peuvent changer les derniers bits et, par le chaos, les poids : **une garde décisive sur la
  linéaire risque un arrêt faux** sans que les jetons soient en cause ; d'où la proposition « rapportee » (§ 9, point 2).
- Sur le run jouet de P3 (essais), le cas sain est **identique au bit près** pour les deux bras, la sonde linéaire comprise.

## 6. Essais (point 4)

**Fichiers neufs : 61 essais, 60 passés, 1 sauté** (fichier v7 hors de l'extraction de l'arbre ; le contenu de la v7 est écrit
dans l'essai et vérifié par l'empreinte canonique), 63 à 76 s :
- `test_t07_plancher_v3_notation_v1.py` (20) : égalité à la boucle (10 cas aléatoires × 2 agrégations ; jouet × 2) ; agrégation au
  bit près (× 2) ; contrôle en ligne (cas sain ; artefacts : écart de 10⁻⁹ sur une action contrôlée → arrêt ; hors contrôle →
  non vu, déclaré ; joué à chaque appel) ; refus et cas sains (plancher vide, agrégations ou couches mêlées, autre classe,
  attention sans requête, maximum avec requête, « moyenne », empan vide, largeur, non fini, lot nul, aucune action) ; lots ;
  constantes ; aucune moyenne ni médiane dans les cinq modules neufs.
- `test_t07_plancher_v3_reextraction_v1.py` (23) : **un vrai run jouet de P3** (`premier_test_ia.run.executer`) sert de
  référence ; cas sain (deux bras « identique » : témoin, principale, 4 directions de P3 redonnées au bit près ; n directions
  neuves sous la graine de T0.7, égales à `plancher_apparie` sur les jetons captés, reproductibles, autres sous une autre
  graine) ; écriture scellée des planchers ; **artefacts** : bruit de carte 10⁻³ (palier « carte », réserve ; principale
  linéaire : 0,13 → réserve si « rapportee », échec si « decisive »), bruit fort, empan décalé, autre couche, graine des
  directions de P3 autre (seconde garde seule), témoin seul décisif, seconde garde sans objet, entrées fautives (données
  absentes, empreinte du manifeste, faits exclus, effectifs, principale autre, lignes des enjeux, nombre d'exemples, mode,
  témoin absent) ; réglages de torch rétablis (deux états initiaux) ; configuration ; paliers.
- `test_t07_plancher_v3_lecture_v1.py` (18) : configuration v7 (admise par la v4, refusée par la v3 et la v2, v6 refusée par la
  v4, `n_plancher` × 7, `donnees_p3`, tolérances, `n_p3`, contrôles de la v3 joués) ; commandes (`empreinte-config`,
  `repli-recalcul` refusé, `grille` égale) ; **miroir** (`noter`, `etape_a`, `etape_b`, `passe_blanc_v2`, `repli_etapes_v2`, au
  caractère près) ; passe à blanc et repli sous la configuration v4 ; **bout en bout** sur le faux run de 7b par la commande
  (bras arrêté : figées en échec, motif, aucune bascule, directions de P3 lues en descriptif, graines au manifeste ; bras établi :
  planchers = directions du double, notés par lots égaux à la boucle, issue L2 comme la v3, réserve « carte » recopiée à
  l'étape B) ; arrêt de l'étape A si le nombre de directions de P3 diffère.

**Suite T0.7 de l'arbre au commit final** (`tests/test_t07*.py`, `test_verifier_jeux_synthetiques_t07_v2.py`,
`test_premier_test_ia_run.py`, `test_regenerer_sondes_p3_v1.py`, un processus, un fil) : **514 passés, 27 sautés, 3 échecs attendus (`xfail`), aucun échec**, code 0
(02:19:55 à 02:33:47 UTC, 835,1 s ; `suite-t07-v4.txt`). Les 27 sauts tiennent à l'extraction réduite (motifs écrits :
configurations v2, v4 et du brouillon 19, fichier léger réel, chaîne de T0.6, commits et branche absents ; le fichier v7, mon
essai) ; les 3 `xfail` sont ceux du dépôt. Un premier passage (code avant le contrôle par échantillon) avait donné 11 échecs,
tous `FileNotFoundError` sur `brouillons/` hors de l'extraction, rejoués après extraction des pièces citées : 11 passés. Un
passage au commit final a été interrompu à 92 % par le redémarrage du conteneur (≈ 02:15, aucun échec affiché) et rejoué en
entier. **Aucun essai existant ne change d'issue** (mes fichiers sont neufs ; le balayage « aucune moyenne » de
`test_t07_lecture_v1.py`, qui lit tous les modules de `t07/`, passe).

**Extraction de l'arbre** (déclaré) : en plus de `/src/`, `/tests/`, `/scripts/` et de la racine, j'ai extrait les données
génériques de P3 (`donnees/T0.7-faits-repe-v1/`, `donnees/T0.7-models-under-pressure-v1/`), les invites
(`docs/sources/invites-2606.08892-v1/`, lues par le lanceur de P3) et les pièces des brouillons 14, 17 et du candidat 1 citées
par les essais existants ; rien d'interdit.

## 7. Banc de mutations (point 4)

Méthode de R-2246 : mutations sur **copies** de `src/` (bac à sable) ; essais visés joués avec `-o pythonpath=`,
`PYTHONPATH=<copie>/src:<arbre>/tests:<greffon>`, `--rootdir` et `-c` de l'arbre ; **import tracé** par le greffon
`trace_import_plancher_v3.py` (chemin et empreinte des cinq modules neufs réellement importés). Bancs `banc_mutations_plancher_v3_v1.py`
(32 mutations), `v2` (m18 rejouée après l'essai ajouté, m33 à m36 neuves), `v3` (au commit final : tout, plus m37).
**Résultat au commit final (banc v3, 02:00:40 à 02:14:59 UTC, `banc-mutations-plancher-v3-v3.json`) : copie saine 60 passés,
1 sauté, import de la copie ; 37 mutations, 36 tuées, 1 équivalente (m10) ; aucun import hors de la copie.** (Banc v1 au
commit `6f9b4521` : 32 mutations, 30 tuées, m10 et m18 survivantes ; m18 tuée en v2 après l'essai ajouté des réglages rétablis
à partir d'un état non déterministe, avec m33 à m36.)

| mutation | fichier | tuée par |
|---|---|---|
| m1 contrôle en ligne retiré | `plancher_v3` | contrôle joué à chaque appel |
| m2 tolérance vectorisée 10⁻⁶ | `plancher_v3` | contrôle en ligne (artefact 10⁻⁹) |
| m3 moyenne au lieu du maximum | `plancher_v3` | égalité à la boucle |
| m4 attention sans soustraction du maximum | `plancher_v3` | agrégation au bit près |
| m5 biais oublié | `plancher_v3` | égalité à la boucle |
| m6 dernier lot perdu | `plancher_v3` | égalité à la boucle |
| m7 `N_PLANCHER_REEL` = 200 | `plancher_v3` | constantes |
| m8 agrégations mêlées admises | `plancher_v3` | refus |
| m9 empan vide admis | `plancher_v3` | refus |
| **m10 attention : `.T.sum(axis=0)`** | `plancher_v3` | **équivalente** (même axe contigu en mémoire, même somme par paires) |
| m11 palier processeur relâché (5 × 10⁻³) | `reextraction` | bruit de carte (palier attendu « carte ») |
| m12 palier carte du témoin à 0,9 | `reextraction` | témoin seul décisif |
| m13 témoin non décisif | `reextraction` | témoin seul décisif |
| m14 seconde garde non décisive | `reextraction` | graine des directions de P3 autre |
| m15 « decisive » ignorée | `reextraction` | bruit de carte (« decisive ») |
| m16 garde sans effet (bascule) | `reextraction` | bruit de carte |
| m17 graine de P3 au lieu de celle de T0.7 | `reextraction` | cas sain (clés de graine) |
| m18 réglages de torch non rétablis | `reextraction` | réglages rétablis (état initial non déterministe) |
| m19 faits exclus non contrôlés | `reextraction` | faits exclus autres |
| m20 effectifs non contrôlés | `reextraction` | effectifs autres |
| m21 `n_plancher` ignoré | `reextraction` | cas sain |
| m22 réglages de P3 non posés | `reextraction` | cas sain |
| m23 principale autre admise | `reextraction` | principale autre |
| m33 lignes des enjeux non contrôlées | `reextraction` | lignes des enjeux |
| m34 nombre d'exemples non contrôlé | `reextraction` | nombre d'exemples |
| m35 mode de P3 non contrôlé | `reextraction` | mode |
| m36 témoin absent remplacé par la principale | `reextraction` | témoin absent |
| m24 `n_plancher` libre en mode réel | `lecture_v4` | configuration |
| m25 `donnees_p3` nulle admise | `lecture_v4` | configuration |
| m26 directions de P3 comptées sur `n_plancher` | `lecture_v4` | bout en bout (bras arrêté) |
| m27 bascule vers les 200 de P3 à l'échec | `lecture_v4` | miroir (premier essai en échec) |
| m28 planchers notés par la boucle | `lecture_v4` | miroir seulement |
| m29 lecture descriptive de P3 absente | `lecture_v4` | bout en bout |
| m30 graines des figées hors du manifeste | `lecture_v4` | miroir (premier essai en échec) |
| m31 passe à blanc sous la configuration v2 | `passe_blanc_v2` | miroir |
| m32 repli sous la configuration v2 | `repli_etapes_v2` | miroir |
| m37 réserves du plancher des figées non recopiées | `lecture_v4` | miroir (premier essai en échec) |

Limite : les essais s'arrêtent au premier échec (`-x`) ; « tuée par » nomme le premier essai en échec. m28 n'est tuée que par
le miroir (texte) : la boucle et la notation par lots donnent les mêmes scores à 10⁻¹⁴ près.

## 8. Coût et devis (point 5)

**Hypothèses** (étape A de la variante B, A100 SXM4 80 Go, ≥ 16 cœurs, ≤ 1,30 USD de l'heure carte et disque compris, tarif du devis
de l'étape A, `GO-2026-11-10-04` et `GO-2026-11-10-06`) : ≈ 1,3 million de jetons notés par couche (texte, « Calcul et
dépense ») ; planchers à 800 directions : 4 sondes principales, la sonde de T7-P6 et son témoin, 6 planchers de concepts (« meteo »
et « sports » × 3 couches, si `SCELLEMENT-CONCEPTS-T07` est inscrite), plus les 2 × 200 directions de P3 en descriptif : ≈ 12,5
planchers de 800 ; au pire 4 par attention ; ≈ 114 500 jetons d'entraînement des enjeux et ≈ 4 950 de la tromperie (estimés
sur les textes : ≈ 4,2 caractères par jeton, 128 au plus) ; relevés de P3 et de R-679 (§ 1) ; mesures du § 4, quatre cœurs.

| poste | ici (4 cœurs, mesuré ou relevé) | instance, attendu | instance, pire (hôte 2 × plus lent) |
|---|---|---|---|
| modèle de P3 depuis le cache local (16 Go), contrôle du format | — | 0,03 h | 0,10 h |
| extraction des 2 069 exemples d'entraînement, couche 15 | 78,5 s × 0,8 ≈ 63 s (R-679, A100) | 0,02 h | 0,04 h |
| témoins, principale linéaire refaite (114 s dans P3, 30 fils) | — | 0,05 h | 0,10 h |
| seconde garde et 800 directions (`plancher_apparie`, ×2 par concept) | 4,5 s pour 20 000 jetons → ≈ 26 s pour 114 500 | 0,02 h | 0,05 h |
| **sous-total réextraction** | | **0,12 h** | **0,29 h** |
| notation par lots, 12,5 planchers de 800 à 1,3 million de jetons | 75 s (maximum), 114 s (attention) par plancher → ≈ 18 min | 0,08 h | 0,30 h |
| contrôle en ligne (2 directions, une action sur 8) | ≈ 3 s par plancher | 0,01 h | 0,02 h |
| poussée des scores en plus (≈ 0,46 Go : 12,5 × 37 Mo) | — | 0,02 h | 0,05 h |
| **total ajouté (sans rien retirer)** | | **≈ 0,23 h** | **≈ 0,66 h** |

- **USD** (≤ 1,30 USD de l'heure) : **+ 0,30 USD attendu, + 0,86 USD au pire**. Devis de la variante B (ordre, brouillon 5,
  § 6 : attendu 5,2 à 7,1 USD, pire 11,6 à 15,5 USD) → **attendu ≈ 5,5 à 7,4 USD ; pire ≈ 12,5 à 16,4 USD : sous 20 USD.**
  Conséquences : la condition P8 de l'ordre devient `ANT0` ≤ 3,6 USD (au lieu de 4,5) ; la marge du pire cas à la minuterie de
  12 h passe de 1,1 h à ≈ 0,45 h (réserve CLE-12 aggravée), si l'on n'enlève rien au devis.
- **Ce que la notation par lots retire** : à 200 directions, la **boucle** du harnais coûtait, par plancher, 5 760 actions × 200 ×
  ≈ 1 ms ≈ 20 min (mesuré ici, 225 jetons ; 4,5 à 17 min selon la note v3) ; pour ≈ 12 planchers, **≈ 4 h**, que la ligne
  « notation ≈ 0,5 h » du devis (brouillon 19) ne comptait pas ; à 800 directions, la boucle demanderait ≈ 16 h. La notation
  par lots remplace cette boucle : **en net, l'étape A de la v4 est plus courte que celle de la v2 telle que codée**. Si l'on
  retirait du devis toute la ligne « notation ≈ 0,5 h » (1 h au pire), le net serait ≈ − 0,3 h ; elle couvre aussi d'autres
  notations (sondes, couples) : le tableau garde la borne prudente, sans rien retirer.
- **Mémoire** : réextraction ≈ 8 Go de mémoire vive au plus (covariance des 114 500 jetons en double précision, deux copies) et
  1,9 Go de jetons en simple précision ; notation ≈ 0,2 Go par lot ; modèle de P3 libéré de la carte avant le chargement du
  modèle de la course. Disque : `planchers-figees-t07.npz` ≈ 52 Mo ; `scores-actions-t07.npz` ≈ 0,6 Go (au lieu de ≈ 0,15).
- **Écart déclaré** : mesures sur un processeur Intel à quatre cœurs, mise à l'échelle supposée linéaire en cœurs (÷ 4 pour 16
  cœurs, ÷ 2 au pire) ; la durée réelle de l'étape A reste non mesurée (la passe à blanc ne relève que l'extraction).

## 9. Repli proposé et ce que le texte doit dire (pour le rédacteur du candidat 2)

1. **Statut des lectures touchées par l'arrêt d'un bras** (garde d'identité en échec, réextraction impossible : modèle de P3 absent
   du cache, données, carte) : la sonde figée concernée a ses lectures **décisives** ((i-a), T7-P1 ; chaque dose jugée de (ii),
   T7-P2) à l'état **« échec »** existant de `criteres_v1` (motif écrit : « plancher neuf de la sonde figée non établi
   (réextraction de P3) : … ») ; **aucune lecture décisive contre les 200 directions de P3** (R5) ; l'état de l'organisme suit la
   règle gelée (`etat_organisme` : U si une autre sonde est au-dessus ; E si toutes sont en échec ; Z sinon) ; T7-P1 n'est plus
   une réplication de P3 pour cette sonde (« non lue : échec du plancher neuf ») ; les 200 de P3 restent lues **en descriptif**
   (continuité, jamais dans le critère). À écrire dans « Liste d'arrêt » (arrêt du seul bras, motif écrit, aucune bascule) et
   dans « Plan », étape A.
2. **Garde de la principale linéaire** : nœud à trancher avant le scellement. Ma recommandation (confiance moyenne-haute) :
   **« rapportee »** (v7) : le témoin déterministe et la seconde garde portent l'identité des jetons ; la principale refaite est
   écrite avec son palier ; une réserve est écrite si elle sort du palier « processeur ». Option « decisive » : lettre de la
   consigne, risque d'arrêt faux (§ 5). Défaut proposé : « rapportee ».
3. **Palier « carte »** : lectures faites, réserve écrite (recopiée dans `resultat.reserves` de l'étape B) ; à déclarer au texte.
4. **Texte** (complète la note v3, § 8) : « Métrique » (n = 800 ; plancher des figées tiré de Σ réextraite, graine de T0.7
   `plancher/<sonde>` ; 200 de P3 en descriptif) ; « Plan », étape A (réextraction **avant toute autre extraction**, réglages de
   P3, gardes, fichiers `planchers-figees-t07.npz` et `reextraction-p3-t07.json`) ; « Module de lecture » (`lecture_v4`,
   `plancher_v3`, `reextraction_p3_v1`, `passe_blanc_v2`, `repli_etapes_v2` ; ligne `CODE-T07` : 26 modules) ; « Points
   d'entrée » : **`lecture_v4` seule** pour la passe à blanc, le repli, l'étape A et l'étape B (la v2 et la v3 refusent la v7 en
   mode réel : aucune lecture silencieuse sous l'ancienne règle n'est possible) ; configuration v7 et son empreinte canonique ;
   T7-P1 : « réplique la sonde de P3, pas son plancher » ; réserve CLE-12 et devis (§ 8).
5. **Ordre d'exécution** (version neuve, contre-lue) : commandes `lecture_v4 repli-seul`, `lecture_v4 passe-blanc`,
   `lecture_v4 etape-a-apres-repli` ; empreinte de la configuration v7 ; **exporter `CUBLAS_WORKSPACE_CONFIG=:4096:8`** dans le
   processus de l'étape A (le module le pose aussi par `setdefault` avant tout calcul sur la carte) ; recommandation pour viser le
   palier « identique » de la principale linéaire : hôte EPYC (AVX2) comme P3, ou `ATEN_CPU_CAPABILITY=avx2` et
   `MKL_CBWR=AVX2` au lancement (non éprouvé ici : déclaré) ; le modèle de P3 (révision `0e9e39f2…`) doit être au cache local
   (c'est celui de la course si 7b tourne sur la même révision ; sinon le bras s'arrête plutôt que de télécharger) ; devis et
   `HMAX` relus (§ 8).

## 10. Réserves

- Calibrage sur **données synthétiques** (spectre estimé sur 200 directions, queue supposée, classes séparées par un signal sur
  huit axes) : les marges du § 5 sont indicatives ; les vrais jetons de tromperie (≈ 4 950 estimés, 10,4 par exemple) sont plus
  nombreux que ceux du calibrage (2 444).
- Le mode réel n'est pas joué (aucune carte) : la réextraction réelle (Llama-3.1-8B, cuda) n'a tourné qu'en jouet (modèle par
  caractères, processeur) ; le chemin est le même code.
- Le contrôle en ligne ne couvre que 2 directions et une action sur 8 (borne déclarée, coût).
- `repli-recalcul` n'est pas offert par la v4 (refus explicite) ; l'ordre d'exécution n'utilise que les deux temps.
- Les copies (`noter`, `etape_a`, `etape_b`, passe à blanc, repli) suivent la v2 et la v3 telles qu'au commit `adb5f415` ; toute
  correction future de celles-ci doit être reportée (l'essai de miroir le signalera).
- Deux commits sur ma branche (le second régénère `lecture_v4.py` et ajoute des essais) ; rien n'est scellé à ce stade et aucun
  fichier n'est cité ailleurs : déclaré.
- Mesures de débit faites sur une machine partagée (quatre cœurs, suite d'essais et banc en parallèle) : prudentes.

## 11. Pièces (bac à sable `…/scratchpad/plancher-v3/bac/`, recopiées scellées dans ce dossier)

Dossier `docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/` (25 pièces, chacune avec son compagnon
`.sha256` ; **non committées** : la mère les verse) :

| pièce | sha256 |
|---|---|
| `banc-mutations-plancher-v3-v1.json` | `f10f29e44ff6f9b8713a2b25fa2e3f710779a3913407b9869576fea2b4c3359f` |
| `banc-mutations-plancher-v3-v2.json` | `f0b08a6ca8da8e72e0f216f93cde83823ba406e640c5bd9659daef99fac3c959` |
| `banc-mutations-plancher-v3-v3.json` | `3e65e2074e464579d1b81a74af40cc75e0bd0932cebca63c05ca71bbb2cde7fc` |
| `banc_mutations_plancher_v3_v1.py` | `41cb9ac96106d371c2d8f4a05cbc746b6e5f4fb7a0d535ce2fc34ce56c9b6238` |
| `banc_mutations_plancher_v3_v2.py` | `bc7e06585311f3c14994d9dcf42969207541a9734b1fd49185e5ecfcba9d7e67` |
| `banc_mutations_plancher_v3_v3.py` | `898b4e16e77a5f27cba00278534107c3cbfee20bd05a76657babc79916cc70ba` |
| `calibrage-gardes-v1.json` | `c5d4650e46f0f5e7fed3583517f62b47a97c010ae998d800f207d6117c092ab7` |
| `calibrage-gardes-v2.json` | `46dce2f5416b5531dcac389ef806253c803742abb06373d1a5d4f21939852661` |
| `calibrage_gardes_v1.py` | `df11132364c60ef0cf7c7bbc48c849988778649d2f5bbe36429cc281cf7d1457` |
| `calibrage_gardes_v2.py` | `7ed6586513f340af6c5ce940506fef144f2fb05d3de4593e3740a521e322ce69` |
| `configuration-t07-v7.json` | `3701407cf96f2851de26b04df174432a6e5325227c1e1f5a24900a1fa44ef6ab` |
| `generer_lecture_v4_v1.py` | `6604593b45f405e5ec363aa662f9b26fe5235d6efe04753f4669dc9083ccda23` |
| `journal-banc-v1.txt` | `8a670fa56577ae417f260b991194e5791d7852607102b311768ba922802bbd2f` |
| `journal-banc-v2.txt` | `21f1613845a4445b5414fc775670f1dd3221fbd8fd3ec65a3db57eb847196f48` |
| `journal-banc-v3.txt` | `ee53dbee72f3c2a51620183d0ef42cf398c1df160d3ad8dd5ef53e5203db5246` |
| `journal-calibrage-v1.txt` | `6faf058a5e42b97538abedc81f98d5e8666e211e4aabe765feb1e327bd8994b9` |
| `journal-calibrage-v2.txt` | `58fc49a00c271651b15e5291322e1269e58a668259ecbb28a27e778de5090ab5` |
| `journal-essais-plancher-v3-v1.txt` | `7b54e7f84a03c7a8170b5918e5c93d0088698f23faa87bfbe41ecf9544d82f5b` |
| `mesure-cout-v1.json` | `2af8a1939fccff693bf0c16d049622710f09c30dc073f1745eec7abb90659dbc` |
| `mesure-cout-v2.json` | `c1abf2a42e849e9dffe4a275690d0d61d42afc7cd49c73408fa2603b8fd7268d` |
| `mesure_cout_v1.py` | `be343b4689f32b3dfb0109bedae5610b842aba04e2da94143a662a6ed6fc3ff2` |
| `mesure_cout_v2.py` | `4deab6c667a4a4d38ef6d56853b87b9ba6ca4b105ed7352e88eff1fc35d6fbc6` |
| `spectre-200-directions.npy` | `43be7c88b14a7858cd592e808b306f78625b2e7310fedb276cf685a83fd5a863` |
| `suite-t07-v4.txt` | `5352055d85d4fa807c0f2138e558f6b565f1ed86c868a5b18ea51f3af87ff3c7` |
| `trace_import_plancher_v3.py` | `be3e150c2bafa653fc7ad531ec0d8bb3f52c9d344a87a38655fb53f1a656cb28` |

Restent dans le bac à sable (non versés) : les essais de fumée (`fumee_*.py`, `essai_rapide_v3.py`) et les sorties des suites v1 à v3 (`suite-t07-v1.txt` à `-v3.txt`). Le générateur rejoue les copies : `python -I generer_lecture_v4_v1.py ARBRE` (refuse d'écraser, R12) ; le banc : `python -I banc_mutations_plancher_v3_v3.py ARBRE SORTIE.json` (importe la v1 et la v2 de son dossier ; greffon dans `PYTHONPATH`).


