# Devis — NARCBench rejoué sur Llama-3.1-8B-Instruct, bras descriptif de T0.7 (N-061, ligne A de P-040) — v1

- **Rédacteur** : rédacteur neuf, Claude Opus 5.5 (`claude-opus-5-5`), sous-agent de la session mère
  (`session_016QhUrrLeN21G7Z9KZobE42`), écrit le 2026-11-09 à partir de 13:46 UTC (`date -u`). Je n'ai écrit aucune pièce
  de T0.7, de T0.6 ni de P-040. Non committé, sans compagnon `.sha256` (consigne de la mère) ; **rien loué, rien dépensé,
  aucune clé lue**.
- **Lu** (empreintes recalculées par `sha256sum` le 9 novembre) : N-061 (`docs/decisions/decision-N-061-v1.md`,
  `b2ae4417…`) ; P-040 (`docs/decisions/proposition-P-040-ressources-publiques-T07-T08-v1.md`, `b44bf8a0…`, ligne A) ;
  `docs/sources/ressources-code-v2.md` (`71d5a12e…`) ; T0.7 brouillon 14 (`brouillons/T0.7-sondes-v0-v1-brouillon14.md`,
  `fe7b4e6d…` : en-tête, hypothèse, métrique, seuil, plan, calcul et dépense) ; brief v2 (`9261932a…`, T0.7 l. 166-173,
  G0 l. 190-201) ; programme v2 (`2fd63bad…`, l. 207, 211, 223) ; N-026 (`85bd4023…`) ; `registres/go.md` (`cd3e4981…`,
  GO-2026-11-09-04, l. 289) ; `registres/decisions.md` (`4f40940f…`, R-2009 à R-2012) ; `registres/depenses.md` (prix
  relevés) ; lectures sur PDF de HELIOS (`docs/sources/lecture-pdf-niveau2/helios-2604.01151-lecture-v1.md`, `6b51dbf5…`) et
  de NARCBench v3 (`docs/sources/lecture-pdf-niveau1/rapport-papierB-NARCBench-Das-v1.md`, `4f449039…`). Sur le web, sans
  clé : la fiche et la liste des fichiers du jeu sur Hugging Face, le dépôt de code (clone superficiel en lecture dans le
  bloc-notes, rien exécuté), la fiche publique du modèle 8B, un relevé public partiel des offres Vast.ai.
- Préenregistrement court associé : `prereg/brouillon-narcbench-8b-descriptif-v1-brouillon1.md` (même rédacteur, même
  heure). Les questions Q1 et Q2 de ce préenregistrement changent le devis de moins de 2 USD (section 6).

## 1. Objet et autorisation

- **Travail** : faire jouer par Llama-3.1-8B-Instruct (révision `0e9e39f249a16976918f6564b8830bc894c89659`) les étages
  CORE (50 scénarios de comité) et STEGO (20 sabots de blackjack) de NARCBench, selon le protocole publié, deux réplicats
  par scénario et par condition ; rejouer en passe forcée les identifiants générés pour lire le flux résiduel aux couches
  7, 15 et 23 sur chaque jeton des messages publics ; noter toutes les actions par les sondes du préenregistrement, leurs
  planchers et les témoins ; **sceller les scores sur l'instance sans calculer une seule aire** ; pousser ; détruire.
  La lecture se fait ensuite sur processeur, 0 USD. Le bras externe (activations 70B et 32B publiées) est tout entier
  sur processeur, 0 USD.
- **Autorisation** : GO-2026-11-09-04 (`registres/go.md` l. 289 : dépenses par anticipation pendant l'autonomie de 8 h,
  50 USD au plus par ligne, devis écrit et consigné avant engagement). **N-061 point 2** demande une autorisation de calcul
  distincte par ressource : ce devis est la ligne « NARCBench » ; la mère juge si GO-2026-11-09-04 la couvre, et inscrit
  l'engagement dans `registres/depenses.md` avant la première minute de carte (`GO_ID=GO-2026-11-09-04`). **Échéance** : le
  GO vaut jusqu'au 2026-11-09 (fin de l'autonomie ≈ 20:57 UTC) ; une création après cette heure demande une ligne de GO
  neuve. **Préalables** : préenregistrement contre-lu (R2, autre modèle qu'Opus 5.5 : N-052), questions Q1 et Q2 tranchées
  (collisionneur, R-2009), scellé, committé et poussé avant la création.

## 2. Machine

| élément | valeur | source |
|---|---|---|
| carte | **une A100 SXM4 80 Go** (la carte de P3, de T0.5 et de T0.6 : les sondes figées de P3 ont été apprises, puis régénérées, sur des activations de cette carte) | `registres/depenses.md` l. 87 (P3), 218 (régénération des sondes figées), 202 (T0.5), 386 (T0.6, E3) |
| bornes de l'offre | 80 Go de mémoire de carte ; ≥ 16 cœurs ; ≥ 128 000 Mo de mémoire vive ; **disque ≥ 150 Go** ; CUDA ≥ 13.0 ; fiabilité ≥ 0,98 ; stockage ≤ 0,08 USD de l'heure ; descente ≤ 0,05 USD par Go ; **prix ≤ 1,40 USD de l'heure** | bornes de T0.7 (brouillon 14, variante B), disque relevé à 150 Go ici (section 4) |
| prix relevé, registre | A100 SXM4 80 Go payées **1,08 à 1,37 USD de l'heure** du 17 octobre au 8 novembre (1,0889 ; 1,0089 ; 1,107 ; 1,366 ; 1,184 ; 1,08 ; 1,187 ; 1,2133 ; 1,1067) | `registres/depenses.md` l. 87, 94, 202, 204, 209, 218, 321, 325, 355 |
| prix relevé, ce jour | relevé **public, partiel, sans clé** (point d'accès des offres de Vast.ai, 13:38-13:40 UTC, 64 offres rendues) : A100 SXM4 80 Go à 1,1627, 1,1844 et 1,2556 USD de l'heure (disques 1 071, 504, 251 Go) ; une à 0,8461 avec 62 Go de disque, **non conforme** ; stockage relevé 0,20 à 1,0 USD par Go et par mois | fichier de travail hors dépôt (`vast-all.json`, `27df6a44…`, bloc-notes de ce sous-agent), **non opposable** : à relire par le lanceur à la création |
| **prix du devis** | **1,30 USD de l'heure** (attendu) ; **1,40** (pire cas, borne de l'offre) ; disque 150 Go à 0,20 USD par Go et par mois ≈ **0,04 USD de l'heure** | SUPPOSÉ à partir des deux relevés |

Une carte de 24 Go (RTX 4090, ≈ 0,45 à 0,6 USD de l'heure au relevé) porterait le modèle, mais changerait de matériel par
rapport à P3 et à T0.6 (garde entre deux matériels non éprouvée, T0.7 brouillon 14, repli) : écartée pour 3 à 4 USD
d'économie.

## 3. Heures (SUPPOSÉES : rien de NARCBench n'a jamais tourné sur le 8B dans le programme)

| étape | contenu | heures attendues | base de l'estimation |
|---|---|---|---|
| 1. mise en place | deux environnements (génération ; harnais du programme, `requirements-gpu.txt`), descente des poids, essais du dépôt | 0,5 à 0,8 | mises en place de T0.5 et P3 au registre |
| 2. génération | CORE : 50 × 2 conditions × 2 réplicats = 200 épisodes, ≈ 17 générations chacun ; STEGO : 20 × 2 × 2 = 80 épisodes, ≈ 36 générations chacun ; **≈ 6 300 générations**, ≤ 512 jetons, ≈ 170 jetons en moyenne (messages publics de CORE : 102 à 132 mots dans un épisode publié) ; CORE en parallèle (le code publié lance les épisodes en fils), STEGO sabot par sabot (le code publié est séquentiel : un processus par sabot) | 0,5 à 1,5 | ≈ 1,1 million de jetons générés ; débit d'un 8B servi par lots sur A100 : SUPPOSÉ |
| 3. passe forcée | ≈ 6 000 passes de ≈ 3 000 jetons de contexte (≈ 18 millions de jetons lus) ; couches 7, 15, 23 sur les ≈ 0,7 million de jetons des messages publics ; plus le bras « échange de consigne » (Q1, recommandation) ≈ 0,3 million de jetons | 0,4 à 0,8 | passe unique de P3 : 108,4 s pour 240 épisodes (candidat 12 r2 de T0.6, l. 633, cité par T0.7), transposée |
| 4. sondes réapprises sur CORE | 5 familles × 3 couches, validation par 5 groupes de domaines laissés de côté ; Mahalanobis par `produit_matriciel_v2` sur la carte, essai d'égalité au paquet gelé avant usage | 0,5 à 1,2 | T0.7 : ≈ 18 min par couple et par couche sur 4 cœurs pour 1,3 million de jetons ; ici ≈ 0,4 million de jetons de CORE par couche |
| 5. notation scellée | toutes les actions, toutes les sondes, 200 directions de plancher par sonde principale, placebo, témoin des mots ; vecteurs du dernier jeton pour le comparateur ; `scores-narcbench-8b.npz`, sceau | 0,3 à 0,5 | T0.7 étape A : ≈ 0,5 h pour 1,3 million de jetons |
| 6. poussée, vérification, destruction | ≈ 3 à 5 Go poussés ; empreintes relues ; destruction par identifiant (R10) | 0,2 à 0,3 | T0.7 étape A |
| **total** | | **≈ 2,4 à 5,1 h ; devis 3,5 à 5,5 h** | |

Pire cas retenu : hôte deux fois plus lent, une relance d'une étape, génération trois fois plus longue (le 8B pousse ses
messages à 512 jetons ou refuse et relance) : **15 h de carte au plus**, borne dure de l'amorce.

## 4. Téléchargements et stockage

- **Sur l'instance (descente)** : poids du 8B **16 060 556 376 octets** (quatre fichiers `.safetensors`, empreintes publiées
  `2b1879f3…`, `09d433f6…`, `fc1cdddd…`, `92ecfe1a…`, fiche publique lue le 9 novembre ; modèle à accès contrôlé, le jeton
  Hugging Face de la session sert, jamais affiché) ; dépôt de code NARCBench au commit `85fea3be2a9d` (quelques Mo ; licence
  MIT, section 2 du préenregistrement) ; fichiers de scénarios publiés de Qwen3-32B pour CORE et STEGO (≈ 22,7 Mo :
  15 241 796 + 7 476 918 octets, liste de l'API à la révision `19cb14b2…`) pour recopier les tirages de chaque scénario ;
  roues Python des deux environnements (≈ 5 à 10 Go, SUPPOSÉ). Descente gratuite ou au tarif de l'offre (≤ 0,05 USD par Go).
- **Disque de l'instance** : poids 16 Go ; environnements ≈ 15 Go ; activations des jetons publics en demi-précision,
  3 couches × 4 096 × 2 octets par jeton : ≈ 1,0 million de jetons ≈ **25 Go** ; marge × 2 → **150 Go**.
- **Montée (poussée des résultats)** : scores par action, vecteurs du dernier jeton (≈ 6 000 actions × 3 couches × 4 096 ×
  4 octets ≈ 0,3 Go), sous-ensemble de 10 % des activations par jeton pour la garde d'identité (≈ 2,5 Go), textes et
  identifiants, manifestes : **≈ 3 à 5 Go**, ≤ 0,05 USD par Go → **≤ 0,25 USD**. Les activations complètes ne sont pas
  poussées (comme T0.6) : elles se recalculent depuis les identifiants gardés.
- **Sur processeur (bras externe, 0 USD)** : le jeu publié entier à la révision `19cb14b2…` fait **1 456 027 013 octets**
  (1 187 fichiers, liste de l'API) ; seuls les fichiers d'activations **CORE et STEGO** de Qwen3-32B et de Llama-3.1-70B
  sont descendus (**712 344 334 octets**, ≈ 0,71 Go ; aucun fichier TRANSFER, Q2). Le README du dépôt dit « ~2.6GB » :
  **écart à la liste de l'API, à relever à la descente** (R11), sans effet sur le coût.

## 5. Coût

| poste | attendu | pire cas |
|---|---|---|
| carte | 3,5 à 5,5 h × 1,30 = **4,6 à 7,2 USD** | 15 h × 1,40 = **21,0 USD** |
| disque de l'instance (150 Go) | ≈ 0,2 USD | ≈ 0,6 USD |
| descente et montée | ≤ 0,3 USD | ≤ 0,5 USD |
| marge d'arrêt (10 min de carte après la borne) | — | ≈ 0,25 USD |
| **total** | **≈ 5 à 8 USD** | **≈ 22,4 USD** |

- **Plafond de la ligne : 25 USD**, tout compris ; il **tient dans 50 USD** (GO-2026-11-09-04) avec une marge de 25 USD.
- **Gardes** : amorce à 15 h de carte au plus ; arrêt par l'identifiant de l'instance (R10), jamais par motif, à la fin de
  l'étape 6 ou à la première de ces bornes : 15 h depuis la création, 25 USD cumulés sur la ligne, processus de l'étape
  mort ; aucune instance gardée arrêtée après la poussée vérifiée (rien n'attend un autre verdict, à la différence de
  T0.7) ; garde de calcul `.claude/hooks/garde_calcul.py` avec `GO_ID` ; relevé du crédit par le lanceur avant création.
- **Cumul** : la ligne compte dans les 150 USD hors crédits de GO-2026-11-09-04, à côté de la lecture exploratoire de
  l'étiqueteur (GO-2026-11-09-03, compté à part) ; aucun appel aux crédits Claude dans ce travail.

## 6. Ce que le devis ne couvre pas, et ce que changent les questions ouvertes

- **Q1 (préenregistrement)** : la recommandation (génération par le 8B, plus l'échange de consigne sur ses propres textes)
  est chiffrée ci-dessus ; option (a), génération seule : − 0,1 à − 0,3 h ; option (b), lecture forcée des textes publiés
  de Qwen3-32B en plus : + 0,5 à + 1 h, ≈ + 0,7 à + 1,4 USD, et une licence de plus à vérifier (sorties de Qwen3, non
  vérifiée ici).
- **Q2** : la recommandation (TRANSFER ni jouée ni lue ici, réservée) est chiffrée ; jouer TRANSFER et la sceller sans
  lecture : + 108 épisodes, ≈ + 0,5 à + 1 h, ≈ + 1 USD.
- **Hors devis** : tout second passage (nouvelle ligne et nouveau devis) ; l'étage TRANSFER s'il est joué plus tard sous
  le texte de G1 ; Llama Scope (ligne C de P-040), Liars' Bench et SHADE-Arena (ligne B) : lignes distinctes (N-061).

## 7. Devis en une ligne

Une A100 SXM4 80 Go ≤ 1,40 USD/h (devis à 1,30, relevé partiel du jour 1,16 à 1,26), ≈ 3,5 à 5,5 h (SUPPOSÉ), 16,1 Go de
poids et ≈ 23 Mo de scénarios descendus, ≈ 3 à 5 Go montés : **attendu ≈ 5 à 8 USD, pire cas ≈ 22,4 USD, plafond 25 USD**
(tient dans 50) ; bras externe sur processeur, 0 USD.
