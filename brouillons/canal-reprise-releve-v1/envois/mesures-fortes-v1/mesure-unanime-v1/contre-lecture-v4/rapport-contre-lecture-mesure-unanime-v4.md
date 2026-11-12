# Contre-lecture (R2) — préenregistrement « mesure unanime » v4 et son script, lecture entière

**Verdict : à corriger en v5.** Trois corrections changent une lecture : M2 ter a deux définitions contradictoires dans le
Seuil (CV4-1) ; un M3 « fragile » laisse passer un faux « confirmé » de M4 (CV4-2) ; la ligne placebo des critères n'est
pas bornée comme la table des prédictions (CV4-3). Le reste est mineur. Le code fait ce que le texte dit ; B tient sous le nul.

- Contre-lecteur : sous-agent neuf Opus 5.5. Je n'ai écrit ni le préenregistrement, ni le script, ni la table, ni les
  rapports précédents.
- Début : 2026-10-28 00:20:02 UTC (`date -u`). Fin : voir la dernière ligne. (Les heures d'`ls` sont en heure de Paris,
  une heure de plus.)
- Processeur seul. `scores-p3.npz` n'a été ni ouvert ni lu ; le script n'a pas été lancé sur lui. Aucun fichier du dépôt
  modifié ; aucun commit. Le script v4 a été lancé en `--test-gardes`, en mode réel **sur le fichier synthétique** des
  gardes (sans arguments, puis `--effectifs-seulement`), et importé sans modification par ma simulation.

## Empreintes lues

| fichier | empreinte | état |
|---|---|---|
| `preenregistrement-mesure-unanime-v4.md` | `5718717133a877a2210036d3b28ec1904ce431e8478f530d38c5ca1e67dde27e` | conforme ; dans le commit `5d75078d` |
| `analyse_fausses_alertes_v4.py` | `c13003d4b30f6bd13f0d7d17128845ca8e62704a7b5fddf36dca2d2aa4486349` | conforme ; identique dans `6906041b` (cité par le texte) |
| `sortie-synthetique-essai-v4.json` | `18ba975b59a9cef99cbce7dc883d3ace7d6d1cad47c59b35dfd5e0222d732cb0` | conforme ; manifeste : 5 tirages, commit nul, empreinte du script v4 |
| `table_m2bis_m4_v4.py` | `5bb61729897c43e0222022c81e8744af4a98e7f3bb575b1ede0e5f2b9546094f` | conforme ; **aucun compagnon `.sha256` sur disque, empreinte absente du texte** (CV4-5) |
| `table-m2bis-m4-v4.json` | `9b8d407812c242c3c13b499df1f1573591f9952ae6339f6049350fb4be762271` | conforme ; dans `5d75078d` ; même remarque |
| `contre-lecture-v3/rapport-…-v3.md` | `0fb0734a59514af24162b86ec3413ca87c657120f5658c584ea4b27cb8a5214c` | conforme à la citation |
| `contre-lecture-v1/rapport-…-v1.md` ; `complement-v2.md` | `5d47ae52…bf2d` ; `e5ca74bb…f7dc` | conformes |
| `src/controle_ia/bases/sequentiel.py` | `35a0983404d7a10d0bb736fa37307a108501785a207c27346be1cd02bab11ba8` | conforme ; « 0,21 à 0,35 » aux lignes 7 et 8 |
| `…/pari-de-signe/conception-pari-de-signe-v3.md` | `1518a12f0c9b755ec6ab0f958d9c6b77f8071d7f959f6e5c5cb60de38a15db14` | conforme ; ligne 117 = « dérive de composition calibrage → épreuve », mesurée par les contrôles 19 et 12 (ligne 128) |

Vérifié sur disque (R11) : le dossier du préenregistrement ne contient **aucun** fichier `.sha256`.

## 1. Fermeture de CV3-1 à CV3-9

| constat | état | raison |
|---|---|---|
| CV3-1 (placebo sur M4) | **à moitié** | La ligne « contrôle placebo » des prédictions est bornée aux 24 cellules de M3 et au maximum de M4. Mais la ligne des critères (« placebo ≠ réelles sur **une cellule conforme** (écart > 0,05) → audit R4 ») ne l'est pas : les sommes du bras M4, du descriptif et du mélange sont des cellules conformes (CV4-3). |
| CV3-2 (quantité de M4) | fermé | `M4_quantite` (lignes 436 à 444) : par sonde, moyenne sur tirages et épisodes de chacune des cinq sommes, moyenne des cinq, médiane sur les réelles ; intervalle par grappes (2 000 rééchantillonnages des épisodes). La table (ligne 42) prend la même moyenne par sonde et par tirage, puis la médiane sur 120 couples (monde, sonde) : même quantité par sonde ; la médiane mêle dix mondes au lieu d'un (sans effet pour une prédiction à ± 0,05). Le Seuil dit « sa borne basse ». |
| CV3-3 (B, E < 60) | fermé | B = max(2L ; 0,10) ; `--effectifs-seulement` puis `--E` avant toute lecture de taux. La phrase « cette borne n'a pas été simulée sous le nul à E < 60 » peut maintenant renvoyer à ma simulation (réponse 3). |
| CV3-4 (marges) | **à moitié** | Bras « mélange » bien codé (réponse 2). Mais le Seuil garde l'ancienne définition de M2 ter à côté de la nouvelle (CV4-1), et « dépendance naturelle suffisante » ne demande pas que le mélange soit ≤ α (CV4-4). |
| CV3-5 (formule, L) | **à moitié** (mineur) | Hypothèse M3 corrigée (2/40) ; L pondéré sur les plis (ligne 360) et consigné. Mais la Métrique dit encore « niveau exact 1/(K + 1) » (ligne 99 du texte), et la docstring du script « K = 39 : niveau conforme exact 1/(K + 1) = 0,05 » (ligne 15) (CV4-6). |
| CV3-6 (moments) | fermé (mineur restant) | « Mêmes deux premiers moments », « tirages d'effet : ceux de τ = 2 » : écrits (la phrase est dite deux fois, lignes 68 et 69). La docstring de `un_passage` dit encore « seule la dépendance intra-épisode change » (CV4-6). |
| CV3-7 (gardes) | fermé | `verifier_effectif` est la fonction appelée par `main()` (ligne 353) et par le test ; vérifié aussi en lançant `main()` sur le petit fichier synthétique (E = 40 : refus). La garde de la corrélation intraclasse est exercée. La garde K de `main()` (ligne 355) reste inatteignable pour E ≥ 44 (K ≥ 24) : sans objet. |
| CV3-8 (tenu, fragile) | fermé | « Tenu (fragile compris) », « la première ligne de lecture s'applique », 24 cellules listées. Voir CV4-2 pour la conséquence sur M4. |
| CV3-9 (provenance) | **à moitié** (mineur) | Commits, rapport v3 (chemin et empreinte), contrôle 19 (chemin, empreinte, ligne, raison de la v3), en-tête « 5 tirages et sans commit », M1 réfuté, M2 ter entre 0,3 et 0,5 : faits. La docstring du script garde « u_e ~ N(0, (τ·σ_cal)²) » (ligne 30) et des commandes `…_v3.py` (lignes 34 et 35) (CV4-6). |

## 2. Le script fait-il ce que le texte dit ?

Oui, sur chaque point demandé.
- **Quantité de M4** : voir CV3-2 ci-dessus. Sortie synthétique : 0,085, intervalle [0,060 ; 0,113], placebo 0,091.
- **Niveau L** : `L = Σ_f |pli_f| · (K_f + 1 − rang_f)/(K_f + 1) / E`, avec K_f = E − |pli_f| − 15 et `niveau_conforme`
  juste (2/40 = 0,05 à K = 39 ; 1/31 = 0,032 à K = 30, soit E = 50). Consigné au manifeste avec `K_par_pli`.
- **Mélange** (`melanger_actions`, lignes 119 à 125) : `Xm[masque] = valeurs[permutation]`, permutation de toutes les
  actions valides de tous les épisodes ; masque inchangé ; une permutation par (sonde, tirage), 20 générateurs
  `SeedSequence(20261028, spawn_key=(7, 1)).spawn(20)` ; mêmes plis, même permutation et même calibrage qu'à τ = 0
  (`un_passage(Xm, …, 0.0)`). Ville réelles moins mélange : médiane des réelles moins médiane du mélange, intervalle par
  grappes apparié (mêmes indices d'épisodes pour les deux) (lignes 446 à 452). r₀ du mélange rapporté (synthétique : 0,002).
- **`--effectifs-seulement`** : sort après E, `K_par_pli`, L et le nombre d'actions valides par épisode ; aucun appel à
  `un_passage`, aucun taux. Lancé sur le fichier synthétique : E = 60, K = 39 dans les dix plis, L = 0,05. Il charge les
  scores (garde de finitude) et applique `verifier_effectif` (sur E = 40 : refus, `RuntimeError`). Il ne compare pas
  l'empreinte si on ne la passe pas, et la commande (1) du Plan ne la passe pas (CV4-6).
- **Gardes** : `--test-gardes --dossier-tmp …/scratchpad/gardes-cv4` → `sortie-test-gardes-v4.json` : **treize** entrées,
  soit douze gardes (sain, sain bras M4, chargement sain, empreinte fausse, deux effectifs faux, E minimal, E sain,
  corrélation constante, score non fini, scores constants, K = 12 trop petit) et la valeur `correlation_saine` = 0,171.
  Aucune garde endormie.
- **Arguments obligatoires** : `--reel` sans les quatre arguments → `SystemExit` « mode réel : … obligatoires » (vérifié).
  `--effectifs-seulement` en est exempté (voulu). `--tirages` et `--bootstrap` restent libres en mode réel ; le manifeste
  les consigne (CV4-6).
- Bras M4 et descriptif : inchangés depuis la v3 (diff v3 → v4 lu), donc la vérification de la v3 tient.

## 3. La règle d'audit de M3 sous le nul, avec des sondes corrélées

Simulation `verif_cv4_m3_v1.py` (code v4 importé tel quel ; graines `SeedSequence(2810202604, spawn_key=(partie, E,
variante, monde))`). Mondes : 30 sondes, r₀ = 0,3, longueurs valides 5 à 10 (masque commun), une permutation par monde ;
l'effet épisode de chaque sonde partage 50 % de sa variance avec les autres (variante « épisode ») ; variante plus dure :
elles partagent aussi 50 % du bruit par action (« épisode+action »). Faux audit : une des médianes > B ; faux « fragile » :
une médiane dans ]1,6 L ; B] ou < 0,4 L.

| partie | E | variante | mondes | L | B | faux audit | faux « fragile » (haut / bas) | plus haute médiane (médiane des mondes / maximum) |
|---|---|---|---|---|---|---|---|---|
| 6 cellules à τ = 0 | 60 | épisode | 120 | 0,050 | 0,10 | **0/120** | 0,8 % (0,8 % / 0) | 0,050 / 0,083 |
| 6 cellules à τ = 0 | 50 | épisode | 120 | 0,032 | 0,10 | **0/120** | 0 (0 / 0) | 0,020 / 0,050 |
| 6 cellules à τ = 0 | 50 | épisode+action | 100 | 0,032 | 0,10 | **0/100** | 4 % (4 % / 0) | 0,030 / 0,060 |
| 24 cellules, 3 tirages par τ > 0 | 60 | épisode | 12 | 0,050 | 0,10 | **0/12** | 0 (0 / 0) | 0,054 / 0,075 |
| 24 cellules, 3 tirages par τ > 0 | 50 | épisode | 12 | 0,032 | 0,10 | **0/12** | 8,3 % (8,3 % / 0) | 0,033 / 0,053 |
| 24 cellules, 3 tirages par τ > 0 | 50 | épisode | 48 (les 12 précédents compris) | 0,032 | 0,10 | **0/48** | 8,3 % (8,3 % / 0) | 0,040 / 0,067 |

Lecture. Les six cellules à τ = 0 sont les plus exposées (aucune moyenne sur les tirages ; taux en pas de 1/E). Aucun faux
audit sur 340 mondes à τ = 0 ; la borne haute à 95 % d'un 0/120 est 2,5 % : **la règle tient sous 5 %** à E = 60 et à
E = 50. Sur les 24 cellules, aucun faux audit non plus (0/12 à E = 60 ; 0/48 à E = 50, borne haute 6 %). Le faux
« fragile » vaut 0 à 4 % à τ = 0 et jusqu'à 8 % sur les 24 cellules à E = 50 (surestimé : 3 tirages au lieu de 20) ; il
ne bloque rien. À E = 50, B = 0,10 vaut 3,1 L et une médiane > B demande 6 alertes sur 50 quand on en
attend 1,6 : le faux audit est quasi impossible, mais la règle est **lâche** (voir CV4-2). À E < 60, la médiane des
conformes à τ = 0 tombe sous L (0,025 contre 0,032 à E = 50 : médiane d'un compte discret) ; le « ≈ L » de la prédiction
est biaisé vers le bas, sans atteindre 0,4 L. Les 24 cellules, avec 3 tirages au lieu de 20 (médianes plus bruitées : estimation
prudente), et 12 mondes seulement : ordre de grandeur, pas une probabilité fine.

## 4. Lectures qui laissent passer un faux « confirmé » ou qui bloquent à tort

- **Liberté de lecture** : deux définitions de M2 ter (CV4-1).
- **Faux « confirmé » de M4** : par M3 « fragile haut » (CV4-2).
- **Faux blocage** : ligne placebo des critères (CV4-3).
- **Fausse attribution** : « dépendance naturelle suffisante » quand le mélange dépasse déjà α, ou quand la différence vient
  d'une dérive avec le pas (CV4-4).
- Pas de faux « confirmé » trouvé sur M1 ; pas de faux audit de M3 sous le nul (réponse 3).

## 5. Chiffres cités contre leurs fichiers

Recalculés : 1 − 0,99⁵⁰ = 0,395 ; 0,0725 (T uniforme de 5 à 10) ; 0,077 (T = 8). Synthèse sur `origin/main` :
`bed9107b…` conforme. Tous conformes à la table v4 (`table-m2bis-m4-v4.json`, `9b8d4078…`) : Ville τ = 0 : 0,000 ; 0,033 ; 0,083 ; 0,133 ;
τ = 2 : 0,138 à 0,152 ; M2 bis : +0,138 ; +0,104 ; +0,065 ; +0,019 ; M4 : 0,194 ; 0,124 ; 0,075 ; 0,0545 (« ≈ 0,05 ») ;
maximum : 0,019 à 0,026 (« 0,02 à 0,03 »). Essai synthétique v4 : « +0,03 à r₀ = 0,2 » (différence réelles moins mélange
0,030, r₀ médian 0,201) ; descriptif ≈ 0,25 (0,23 à 0,27) ; K = 39, rang 38, L = 0,05. Inexacts : « table gelée, code v3 »
(ligne 50 : c'est le code v4 ; la docstring de la table dit aussi « code v3 ») ; « max ≈ L » (lignes 85 et 87) alors que la
table donne 0,019 à 0,026, soit 0,4 à 0,5 L.

## Constats

### CV4-1 — M2 ter a deux définitions contradictoires dans le Seuil (moyen à grave : liberté de lecture sur un verdict)

- **Où** : Seuil, lignes 128 à 130 (« dépendance naturelle suffisante si Ville à τ = 0 > α **et r₀ médian ≥ 0,3** ; Ville
  tenue si ≤ 0,05 **et r₀ médian ≤ 0,3** ») et lignes 136 à 139 (« dépendance naturelle suffisante si Ville réelles > α **et
  la différence réelles moins mélange a une borne basse > 0** ; marges seules … ; Ville tenue si médiane réelles ≤ 0,05 »).
  Critères, ligne « Ville tenue » : « (r₀ ≤ 0,3) ».
- **Problème** : la première est celle de la v3, laissée en place. Avec Ville réelles = 0,07, r₀ = 0,2 et une différence
  de borne basse > 0, la seconde dit « suffisante », la première « rapporté ». Avec Ville ≤ 0,05 et r₀ = 0,5, la seconde dit
  « tenue », la première « rapporté », et la ligne des critères affirme « r₀ ≤ 0,3 ». Le lecteur choisirait après coup.
- **Correction** : supprimer les lignes 128 à 130 ; garder une seule définition (la seconde, complétée par CV4-4) ; dire si
  r₀ y entre (je propose : non pour « suffisante », qui repose sur le mélange ; rapporté avec r₀) ; retirer « (r₀ ≤ 0,3) »
  de la ligne des critères ou l'ajouter à la définition ; aligner la colonne « réfutation » des prédictions.

### CV4-2 — Un M3 « fragile » laisse passer un faux « confirmé » de M4 (moyen)

- **Où** : Seuil, M3 (« fragile … la lecture continue, la première ligne de lecture s'applique ») et M4 (« confirmé si la
  quantité > L + 0,02 et sa borne basse > L »).
- **Problème** : M4 est comparé au niveau **théorique** L, pas au niveau **mesuré** des mêmes statistiques sous calibrage
  partagé. Un défaut qui monte le niveau des conformes (fuite, rang, plis) jusqu'à B passe en « fragile » : jusqu'à 0,10 à
  E = 60 (2 L), jusqu'à 0,10 à E = 50 (3,1 L). Le même défaut monte les sommes du bras M4 au-dessus de L + 0,02 (0,07 à
  E = 60 ; 0,052 à E = 50) sans aucune dépendance non vue, et le maximum de M4 (attendu 0,02) peut rester sous 0,08 :
  « confirmé » à tort, et la première ligne des critères propose alors une règle à Lazar pour G1. Je n'ai pas construit ce
  défaut ; le constat tient à la forme de la règle (seuil fixe contre niveau mesurable).
- **Correction** (au choix, la première de préférence) : (a) lire M4 en **excès apparié** : quantité de M4 moins la même
  quantité (cinq sommes, mêmes sondes) à τ = 0 sous calibrage partagé, calculée par le script avec un intervalle par
  grappes apparié ; « confirmé » si l'excès > 0,02 et sa borne basse > 0 ; la table calcule le même excès ; (b) à défaut :
  « M4 confirmé exige qu'aucune des 24 médianes de M3 ne soit dans ]1,6 L ; B] ». Coût de (b) sous le nul : 0 à 8 % de mondes
  (réponse 3) ; (a) ne coûte rien.

### CV4-3 — La ligne placebo des critères n'est pas bornée (moyen : faux blocage ; reste de CV3-1)

- **Où** : critères, « placebo ≠ réelles sur une cellule conforme (écart > 0,05) → audit R4 ».
- **Problème** : la table des prédictions borne le verdict aux 24 cellules de M3 et au maximum de M4 ; la ligne des critères
  dit « une cellule conforme », ce qui couvre les sommes du bras M4 (dépendantes de r₀ : 0,19 à 0,05 selon la table) et le
  descriptif. Un écart de r₀ entre réelles et placebo, légitime, déclencherait un audit sans défaut.
- **Correction** : écrire « sur une des 24 cellules de M3 ou sur le maximum conforme du bras M4 ».

### CV4-4 — « Dépendance naturelle suffisante » : deux attributions encore trop larges (mineur à moyen)

- **Où** : Seuil, M2 ter (seconde définition) ; critères, ligne M2 ter.
- **Problème** : (i) si le mélange dépasse déjà α (marges très asymétriques : jusqu'à 0,04 selon la v3, davantage possible)
  et que la différence est positive, la dépendance n'est pas « suffisante » : les deux s'ajoutent ; (ii) le mélange détruit
  la dépendance **et** toute dérive commune avec le pas (scores qui montent avec le rang de l'action) ; la différence
  « réelles moins mélange » mesure la structure intra-épisode, pas la seule dépendance.
- **Correction** : « suffisante » exige aussi Ville sur le mélange ≤ α ; sinon « marges et dépendance » ; écrire « structure
  intra-épisode (dépendance ou dérive avec le pas) », ou ajouter un mélange **à pas fixé** (scores permutés entre épisodes au
  même pas) qui garde la dérive et détruit la dépendance.

### CV4-5 — Empreintes de la table gelée absentes (mineur à moyen, R6)

- **Où** : en-tête, « Table gelée … (empreintes dans leurs compagnons …) ».
- **Problème** : aucun compagnon `.sha256` dans le dossier (vérifié sur disque) ; les empreintes de `table_m2bis_m4_v4.py`
  et `table-m2bis-m4-v4.json` ne figurent pas dans le texte, alors que la table porte toutes les prédictions de M2 ter, M2 bis
  et M4.
- **Correction** : écrire `5bb61729897c43e0222022c81e8744af4a98e7f3bb575b1ede0e5f2b9546094f` et
  `9b8d407812c242c3c13b499df1f1573591f9952ae6339f6049350fb4be762271` dans l'en-tête ; créer les compagnons au scellement
  (et pour le script et la sortie synthétique).

### CV4-6 — Restes (mineur)

- Métrique, ligne 99 : « niveau exact 1/(K + 1) » → « (K + 1 − rang)/(K + 1) ».
- Script : docstring lignes 15 (« 1/(K + 1) = 0,05 »), 30 (« σ_cal »), 34 et 35 (`…_v3.py`) ; `un_passage` (« seule la
  dépendance intra-épisode change »). Table : docstring « code v3 ». Texte, ligne 50 : « code v3 » → « code v4 ».
- « max ≈ L » (prédictions M4 et placebo) → « ≈ 0,02 (0,4 à 0,5 L) ».
- Lignes 68 et 69 : la même phrase deux fois.
- Plan, commande (1) : ajouter `--empreinte-attendue 968414fc…` (sinon E est lu sans vérifier le fichier).
- Mode réel : écrire que `--tirages` et `--bootstrap` gardent leurs défauts (20 et 2 000), ou les rendre fixes.
- « Audit si maximum > 0,10 » : écrire « à tout r₀ ».
- La table refaite au E observé garde des longueurs uniformes de 5 à 10 ; `--effectifs-seulement` donne les longueurs
  réelles : les passer à la table, ou dire que la prédiction est faite à longueurs uniformes.
- « Cette borne n'a pas été simulée sous le nul à E < 60 » : renvoyer à la réponse 3 de ce rapport.
- En-tête : « par `--test-gardes` (… ) » : treize entrées (douze gardes et une valeur).

## Mes scripts et sorties (ce dossier, chacun avec un compagnon `.sha256`)

| fichier | contenu |
|---|---|
| `verif_cv4_m3_v1.py` | simulation de M3 sous le nul (réponse 3) |
| `sortie-verif-cv4-m3-tau0-E60-episode-v1.json`, `…-tau0-E50-episode-v1.json`, `…-tau0-E50-episode+action-v1.json` | 6 cellules à τ = 0 |
| `sortie-verif-cv4-m3-tau_pos-E60-episode-v1.json`, `…-tau_pos-E50-episode-v1.json`, `…-tau_pos-E50-episode-48mondes-v1.json` | 24 cellules, 3 tirages |
| `sortie-test-gardes-v4.json` | `--test-gardes` du script v4 |
| `sortie-effectifs-synthetique-v4.json` | `--effectifs-seulement` sur le fichier synthétique des gardes |

Interpréteur `/opt/venv-essaim-sim-v1/bin/python -I -B`, numpy 2.5.4.

Fin : 2026-10-28 00:29:49 UTC (`date -u`).
