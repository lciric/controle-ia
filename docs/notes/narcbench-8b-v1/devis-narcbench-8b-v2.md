# Devis — NARCBench rejoué sur Llama-3.1-8B-Instruct, bras descriptif de T0.7 (N-061, ligne A de P-040) — v2

- **Rédacteur** : le rédacteur de la v1, Claude Opus 5.5 (`claude-opus-5-5`), sous-agent de la session mère, écrit le
  2026-11-09 à partir de 15:47 UTC (`date -u`). **v2 = v1** (`docs/notes/narcbench-8b-v1/devis-narcbench-8b-v1.md`,
  `bccb8c25cbef39becad332c303c53cd2e0256e11a7ecfc0cd502db2d37a2e5f5`, gardée telle quelle, R12) **recalculée** pour trois
  changements : (1) le plan de relectures de Q1, option (c) corrigée (R-2020, synthèse du collisionneur
  `docs/notes/collisionneur-conception-qo1-q1-v1/synthese-v1.md`, `a81fe187…`) : dix relectures (cinq cellules et cinq contrôles) au lieu d'une ;
  (2) la génération de STEGO en parallèle, un processus par sabot (constat m5 de la contre-lecture 1) ; (3) **plus de
  lancement sous GO-2026-11-09-04** (décision de la mère) : ligne de GO propre `<<GO_NARCBENCH>>` (N-061 point 2), à
  demander à Lazar avec ce devis. Non committé, sans compagnon `.sha256` ; rien loué, rien dépensé, aucune clé lue.
- Préenregistrement associé : `prereg/brouillon-narcbench-8b-descriptif-v1-brouillon3.md`.
- Prix, machine, téléchargements : **inchangés depuis la v1** (sections 2 et 4 de la v1, relevés du 9 novembre), recopiés
  ici en bref.

## 1. Machine (inchangée)

Une **A100 SXM4 80 Go** ; bornes de l'offre : ≥ 16 cœurs, ≥ 128 000 Mo de mémoire vive, **disque ≥ 150 Go**, CUDA ≥ 13.0,
fiabilité ≥ 0,98, stockage ≤ 0,08 USD de l'heure, descente ≤ 0,05 USD par Go, **prix ≤ 1,40 USD de l'heure**. Prix
relevés : registre des dépenses, 1,08 à 1,37 USD de l'heure (17 octobre au 8 novembre) ; relevé public partiel du
9 novembre, 13:40 UTC, sans clé, non opposable : 1,16 à 1,26. **Devis à 1,30 USD de l'heure** (attendu), **1,40** (pire
cas) ; disque 150 Go ≈ 0,04 USD de l'heure. Ces deux prix sont SUPPOSÉS à partir des relevés et sont relus par le lanceur
à la création.

## 2. Ce que les relectures ajoutent

| quantité | valeur | source |
|---|---|---|
| messages publics de colludeurs relus | CORE : 100 épisodes de collusion × 2 colludeurs × 4 tours = 800 ; STEGO : 40 × 2 × ≈ 8,5 ≈ 680 ; **≈ 1 480** | 34 messages publics pour 4 agents dans un épisode STEGO publié |
| messages publics d'honnêtes des épisodes de collusion relus | même compte, **≈ 1 480** | idem |
| relectures du texte de colludeur | `K-h+`, `K-c−`, `K-h−`, `K-c+/rep`, `K-c+/dec` : 5 × 1 480 = 7 400 passes | préenregistrement, Q1 |
| relectures du texte d'honnête | `H-c−`, `H-c+`, `H-h−/rep`, `H-h−/dec`, `H-h−/ech` : 5 × 1 480 = 7 400 passes | idem |
| **total des relectures** | **≈ 14 800 passes forcées**, ≈ 2 500 jetons de contexte en moyenne (≈ 1 500 au premier tour, ≈ 3 500 au dernier) : **≈ 37 millions de jetons lus** | SUPPOSÉ |
| passe arrêtée après la couche 23 (la plus haute lue) | ≈ 72 % du calcul d'une passe entière ; activations des couches ≤ 23 égales au bit près à celles d'une passe entière (éprouvé à l'étape A (0)) | — |
| débit d'une passe forcée du 8B en bf16 sur A100 | 100 à 170 téraflops effectifs, ≈ 16 milliards d'opérations par jeton | SUPPOSÉ (non chronométré : d'où l'étape A (0)) |
| **heures de carte ajoutées** | relectures **0,7 à 1,2 h** ; notation des cellules par les quatre sondes principales et leurs 200 directions de plancher **≈ 0,1 h** ; chronométrage **≈ 0,05 h** ; **total ≈ + 0,85 à 1,35 h** | calcul ci-dessus |

## 3. Heures (SUPPOSÉES)

| étape | v1 | v2 | changement |
|---|---|---|---|
| 1. mise en place | 0,5 à 0,8 | 0,5 à 0,8 | — |
| A (0). chronométrage | — | ≈ 0,05 | neuf : 50 passes forcées sur des contextes publiés de Qwen3, sans score ; projection écrite avant la génération |
| 2. génération | 0,5 à 1,5 | 0,5 à 1,5 | STEGO **en parallèle** (un processus par sabot, contre un seul serveur) : la borne haute de la v1 tient ; en série, elle aurait été de 1,5 à 3 h |
| 3. passes forcées | 0,4 à 0,8 (avec l'ancien échange de consigne, ≈ 0,3 million de jetons) | lecture de la génération 0,4 à 0,8 ; **relectures 0,7 à 1,2** | + 0,7 à 1,2 |
| 4. sondes réapprises sur CORE et bases | 0,5 à 1,2 | 0,5 à 1,2 | base des métadonnées ajoutée : négligeable |
| 5. notation scellée | 0,3 à 0,5 | 0,4 à 0,6 | + 0,1 (cellules) |
| 6. poussée, vérification, destruction | 0,2 à 0,3 | 0,2 à 0,3 | scores des cellules ≈ 50 Mo de plus : négligeable |
| **total** | **3,5 à 5,5** (devis) | **≈ 3,3 à 6,4 ; devis 4,5 à 7** | **≈ + 1 h** |

**Pire cas** : hôte deux fois plus lent sur le haut du devis (7 h × 2 = 14 h), plus la relance d'une étape (≈ 2 h) :
**16 h de carte**, borne dure de l'amorce (15 h dans la v1).

## 4. Coût

| poste | attendu | pire cas |
|---|---|---|
| carte | 4,5 à 7 h × 1,30 = **5,9 à 9,1 USD** | 16 h × 1,40 = **22,4 USD** |
| disque de l'instance (150 Go) | ≈ 0,2 à 0,3 USD | ≈ 0,64 USD |
| descente et montée | ≤ 0,3 USD | ≤ 0,5 USD |
| marge d'arrêt (10 min de carte après la borne) | — | ≈ 0,25 USD |
| **total** | **≈ 6,5 à 9,7 USD** | **≈ 23,8 USD** |

- **Le plafond de 25 USD tient encore**, avec une marge de ≈ 1,2 USD au pire cas (contre ≈ 2,6 en v1) : la marge est
  mince. Deux gardes la protègent :
  - **règle de réduction à l'étape A (0)**, jouée sur le seul chronométrage, avant la génération et avant tout résultat
    (aucune lecture n'en dépend) : si la projection nominale du total dépasse **8 h**, on retire **`K-c−`**, puis **`H-c+`**
    (cellules hors du socle), et la décision est journalisée ; si elle dépasse encore 8 h, **arrêt, nœud**, devis à refaire.
    Le socle (`K-c+`, `K-h+`, `K-h−`, `H-h−`, `H-c−` et les contrôles `rep`, `dec`, `ech`) n'est jamais réduit ;
  - **arrêt par l'identifiant de l'instance (R10)** à la première de ces bornes : 16 h de carte depuis la création,
    25 USD cumulés sur la ligne `<<GO_NARCBENCH>>`, processus d'étape mort ; aucune instance gardée arrêtée après la poussée
    vérifiée.
- **Plafond de la ligne : 25 USD** tout compris. Il tient aussi dans les 50 USD par ligne de la délégation par anticipation,
  mais **cette délégation n'est pas utilisée** (décision de la mère) : la ligne `<<GO_NARCBENCH>>` est demandée à Lazar.
- **Bras externe** (activations publiées CORE et STEGO de Qwen3-32B et de Llama-3.1-70B, 712 344 334 octets) : sur
  processeur, **0 USD**, inchangé.

## 5. Hors devis

Tout second passage (nouvelle ligne, nouveau devis) ; l'étage TRANSFER (famille externe non lue, rapportée : jamais jouée
sous ce texte) ; le privé honnête apparié de la synthèse (non retenu dans le brouillon 3) ; Llama Scope, Liars' Bench et
SHADE-Arena (lignes distinctes de N-061).

## 6. Devis en une ligne

Une A100 SXM4 80 Go ≤ 1,40 USD/h (devis à 1,30), ≈ 4,5 à 7 h (SUPPOSÉ, dont ≈ 1 h de relectures de plus qu'en v1,
chronométré à l'étape A (0)) : **attendu ≈ 6,5 à 9,7 USD, pire cas ≈ 23,8 USD, plafond 25 USD : tient**, marge mince,
règle de réduction sur chronométrage ; ligne de GO propre `<<GO_NARCBENCH>>` ; bras externe sur processeur, 0 USD.
