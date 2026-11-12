# Contre-lecture (R2) — préenregistrement « mesure unanime » v3 et son script, lecture entière

- Contre-lecteur : sous-agent neuf Opus 5.5. Je n'ai écrit ni le préenregistrement, ni le script, ni les rapports v1 et v2.
- Début : 2026-10-27 23:56:34 UTC (`date -u`). Fin : voir la dernière ligne.
- Processeur seul ; données synthétiques seulement. `scores-p3.npz` n'a été ni ouvert ni lu, et le script n'a pas été lancé
  en mode réel. Aucun fichier du dépôt n'a été modifié ; aucun commit.

## Verdict

**À corriger en v4.** Cinq corrections changent le texte : (1) le verdict placebo ne doit plus porter sur les cellules de M4,
qui dépendent de r₀ (CV3-1) ; (2) la « borne basse » de M4 n'est pas calculée par le script, et la table n'agrège pas comme
le script (CV3-2) ; (3) la borne d'audit de M3 bloque à tort quand E < 60 ; la table de M4 ne vaut que pour E = 60 (CV3-3) ;
(4) M2 ter attribue à la dépendance ce que la forme des marges peut produire aussi (CV3-4) ; (5) la formule du niveau
« 1/(K + 1) = 0,05 pour K = 39 » est fausse (CV3-5). Le reste est mineur (CV3-6 à CV3-9). Le code fait ce que le texte dit.
La table gelée se reproduit avec une autre graine.

## Empreintes lues (toutes conformes aux empreintes annoncées)

| fichier | empreinte |
|---|---|
| `preenregistrement-mesure-unanime-v3.md` | `3a52f3047c9462fc0db9eee4c971222d35d0ce025cf10709a7222e4fb918f30d` |
| `analyse_fausses_alertes_v3.py` | `1c37dd21f1066bebc495cc122da0d67e9081279a42e4413f2c2a87fcaa340e11` (identique dans le commit `8c90a573`) |
| `sortie-synthetique-essai-v3.json` | `0983f06bd8aee1717b2d948dd95bcc2419eda804876f3fb9e604ec27a3dacf2a` (identique dans `8c90a573`) |
| `table_m2bis_m4_v3.py` | `2440968ed39c44335975857ad8696d76be5ccc6061352b782acb57e735ab6088` (identique dans `8c90a573`) |
| `table-m2bis-m4-v3.json` | `982389998c468af3d243dc8ba4b897615fd90db94bb77491484e996a9780e0ba` (identique dans `8c90a573`) |
| `contre-lecture-v1/rapport-contre-lecture-mesure-unanime-v1.md` | `5d47ae52d44e81a25604220ba3482db2eec8cfb0fd5b426dcce9484ef15bbf2d` |
| `contre-lecture-v1/complement-v2.md` | `e5ca74bb11faece8ca72f932d6b78f3bac8f36fd6f11a515e8e3afb53bd4f7dc` |
| `src/controle_ia/bases/sequentiel.py` | `35a0983404d7a10d0bb736fa37307a108501785a207c27346be1cd02bab11ba8` (conforme ; le chiffre 0,21 à 0,35 est bien aux lignes 7 et 8 de la docstring) |
| synthèse `docs/notes/collisionneur-mesures-fortes-v1/synthese-mesures-fortes-v1.md` (`origin/main`) | `bed9107b67c969e0e9a97336000a569faf2c519dd556731ace14f29de404885e` (conforme ; citations « 40 % », A(a)1 et A(a)3 retrouvées, lignes 37, 72, 74, 99) |
| `…/pari-de-signe/conception-pari-de-signe-v3.md` (source du « contrôle 19 », ligne 117) | `1518a12f0c9b755ec6ab0f958d9c6b77f8071d7f959f6e5c5cb60de38a15db14` (une v5 existe : `95af46e4b8f317685ccc8755d6e3d0447ba109fd8771a0139eb9470c2bca8f8c`) |

Le commit `8c90a573` contient le script v3, la table et la sortie synthétique. Le préenregistrement v3 n'y est pas : il est
dans `b522701b`. La version scellée devra être committée.

## Mes scripts et sorties (ce dossier, chacun avec un compagnon `.sha256`)

- `verif_cv3_v1.py` : importe le script v3 sans le modifier (`sys.dont_write_bytecode = True` ; interpréteur
  `/opt/venv-essaim-sim-v1/bin/python -I -B`, numpy 2.5.4). Graines : `SeedSequence(3141592653, spawn_key=(partie, …))`.
  Parties : `transfo` (5,), `table` (1, ⌊10 r₀⌉, monde), `m3` (2, E, ⌊10 r₀⌉, monde), `marges` (3, loi, monde),
  `m4E` (4, E, monde).
- Sorties : `sortie-verif-cv3-transfo-v1.json`, `sortie-verif-cv3-table-0_2-v1.json`, `sortie-verif-cv3-table-0_8-v1.json`,
  `sortie-verif-cv3-m3-v1.json`, `sortie-verif-cv3-marges-v1.json`, `sortie-verif-cv3-m4E-v1.json`,
  `sortie-test-gardes-v3.json` (sortie de `--test-gardes`, lancé avec `--dossier-tmp …/scratchpad/gardes-cv3`).

## Réponses

### 1. Fermeture de CM-1 à CM-11 et de (a) à (e)

| constat | état | raison |
|---|---|---|
| CM-1 | fermé | M3 est un contrôle. A(a)1 et A(a)3 sont tranchées. Le bras M4 est à variance constante. La première ligne s'appuie sur M1 et M4, M3 n'y est qu'une condition de validité. |
| CM-2 | fermé | M2 à τ = 2 devient un contrôle du mécanisme ; M2 ter est la lecture sur P3 ; r₀ est mesuré ; table gelée. Réserve : CV3-4. |
| CM-3 | fermé, avec une réserve | Finitude, scores constants, K, empreinte et effectifs : codés, obligatoires en mode réel, testés (sortie conforme). Réserve CV3-7 : le test « E minimal » n'exerce pas la garde de `main()`, et la garde de la corrélation intraclasse n'est pas testée. |
| CM-4 | fermé | `cal_idx` est trié par rang dans la permutation (lignes 135 à 138). |
| CM-5 | **à moitié** | L et K par pli sont au manifeste ; E ≥ 44 est dit. Mais « niveau exact 1/(K + 1) = 0,05 pour K = 39 » est faux (CV3-5). Les bornes de M3 ne tiennent pas pour E < 60 (CV3-3). |
| CM-6 | **à moitié** | Le verdict placebo couvre maintenant M4, dont les taux dépendent de r₀, pour la même raison que M1 et M2 (CV3-1). |
| CM-7 | fermé | Un vecteur commun par (τ, tirage), multiplié par τ·σ_sonde (ligne 334). |
| CM-8 | fermé | L'intervalle est dit conditionnel aux calibrages. |
| CM-9 | fermé, avec une réserve | Commit `8c90a573` vérifié ; empreinte de `bases/sequentiel.py` donnée et conforme. La section « Contre-lecture » dit encore « commit `ffd5968c` » (CV3-9). |
| CM-10 | fermé, avec une réserve | Lignes ajoutées : « M1 non concluant », « M3 fragile » ; « proposé à Lazar ». Le contrôle 19 n'a ni chemin ni empreinte (CV3-9). |
| CM-11 | **à moitié** (mineur) | Balayage et lancement : corrigés ; le repli à 0 de la corrélation intraclasse est devenu une erreur. La docstring du module dit encore « u_e ~ N(0, (τ·σ_cal)²) » (ligne 24). |
| (a) | fermé, avec des réserves | Bras M4 bien codé (réponse 2), prédiction conditionnelle à r₀, bras descriptif sans verdict, « fondée pour les sommes ». Réserves : CV3-1, CV3-2, CV3-6. |
| (b) | **à moitié** | Une seule définition, relative à L, avec une zone fragile. Mais faux blocage pour E < 60 (CV3-3), et « tenu » et « fragile » se recouvrent (CV3-8). |
| (c) | fermé | Table refaite avec le code v3 (20 tirages, 10 mondes), gelée avec empreinte ; réfutation retirée pour r₀ ≥ 0,5 ; M2 ter. Reproduite (réponse 3). Réserve : elle ne vaut qu'à E = 60 (CV3-3). |
| (d) | fermé, avec une réserve | Obligatoires en mode réel (ligne 305) et testées (empreinte fausse, effectifs faux). Réserve CV3-7. |
| (e) | fermé, avec une réserve | « Pas de dépassement établi », « proposé à Lazar », empreinte de `sequentiel.py`, K par pli, docstring, graine du test par SeedSequence, balayage. Le contrôle 19 est nommé sans chemin (CV3-9). |

### 2. Le script fait-il ce que le texte dit ?

Oui, sur tous les points demandés.
- **Bras M4** (lignes 124 à 130, 354) : `Xe = X + τ·σ·u`, puis `m + (Xe − m)/√(1 + τ²)`, avec m et σ (écart type sans
  correction) calculés sur `X[masque]`, c'est-à-dire les scores valides de la sonde, tous épisodes gardés. C'est la
  formule du texte. Avec `calibrage_sans_effet=True`, on a `Xcal = X`. La normalisation (μ₀, σ sur 15 épisodes), les seuils
  conformes et le quantile par action se calculent sur `Xcal` ; l'évaluation (conformes, Ville, par action) se fait sur `Xe`.
  Aucune fuite. Vérifié par Monte-Carlo (`transfo`, r₀ = 0,3, τ = 2, 4 000 épisodes) : variance 1,467 → 1,461 ; corrélation
  intraclasse 0,321 → 0,864 (théorie (r₀ + τ²)/(1 + τ²) = 0,86). Le bras M4 reprend les tirages d'effet de τ = 2
  (`effets[2.0]`) ; le texte ne le dit pas (CV3-6).
- **Bras descriptif** (ligne 355) : même appel sans `variance_constante` ; l'évaluation lit `X + τ·σ·u`. Conforme.
- **Partage normalisation / seuils** : `cal_idx` est trié par `rang[e]`. Les 15 premiers vont à la normalisation, les K
  suivants aux seuils. C'est l'ordre de la permutation, sans recouvrement avec le pli évalué. Conforme.
- **Gardes** : `--test-gardes` lancé ; les dix lignes attendues sont produites (`sortie-test-gardes-v3.json`) : 3 cas sains,
  empreinte fausse, deux effectifs faux, score non fini, scores constants, K = 12 trop petit. Deux trous (CV3-7) : la ligne
  « E_minimal » est écrite par `test_gardes` lui-même (comparaison `Xp.shape[0] < E_MINIMAL`), sans passer par le
  `SystemExit` de `main()` (ligne 316) ; la garde « corrélation intraclasse indéfinie » (ligne 173) n'est jamais exercée.
- **Manifeste** : empreinte du script (calculée sur `__file__`), commit (obligatoire en mode réel, mais chaîne libre, non
  vérifiée), `niveau_conforme_attendu` = 1 − rang/(K + 1) (juste), `K_conforme` (minimum sur les plis), `K_par_pli`,
  entropie, versions. Pour E = 59, les plis n'ont pas tous le même K (neuf à 38, un à 39) : L du manifeste (0,0256) est
  sous le niveau réel (0,029, simulé) (CV3-5).
- La sortie synthétique de l'auteur a été faite avec `tirages = 5` et `commit = null`. C'est un essai du code, pas la
  configuration du run réel (20 tirages) : à dire dans l'en-tête.

### 3. La table gelée

Je l'ai refaite avec le code v3, une autre graine et 6 mondes de 12 sondes et 20 tirages :

| r₀ | source | Ville τ = 0 | Ville τ = 2 | différence | M4 sommes | M4 max |
|---|---|---|---|---|---|---|
| 0,2 | table gelée | 0,033 | 0,138 | +0,104 | 0,124 | 0,023 |
| 0,2 | moi | 0,033 | 0,141 | +0,108 | 0,126 | 0,022 |
| 0,8 | table gelée | 0,133 | 0,152 | +0,019 | 0,055 | 0,023 |
| 0,8 | moi | 0,133 | 0,163 | +0,030 | 0,049 | 0,024 |

Écarts ≤ 0,011 partout, bien sous la tolérance de ± 0,05. Les prédictions du texte reprennent la table fidèlement : 0,00,
0,033, 0,083, 0,133 ; 0,138 à 0,152 ; +0,138, +0,104, +0,065, +0,019 ; 0,19, 0,12, 0,075, « 0,05 » pour 0,0545 (0,055
serait plus juste) ; maximum 0,02 à 0,03 pour 0,019 à 0,026. Deux réserves :
- la table ne vaut que pour E = 60. À E = 59, K tombe à 38 et L à 0,026, et les sommes de M4 tombent de 0,128 à **0,083**
  (r₀ = 0,2, même code ; `m4E`). L'écart (0,045) mange presque toute la tolérance (CV3-3) ;
- la table agrège autrement que le script (CV3-2).

### 4. Lectures de M3 et de M4

- **M3** : la partition est complète (toute médiane est ≤ 2L ou > 2L). Mais « fragile » est inclus dans « tenu », et le
  texte ne le dit pas (CV3-8). Pas de faux blocage à E = 60 : dans le pire cas, où les sondes sont parfaitement corrélées
  (une sonde par monde, 300 mondes), une cellule à τ = 0 dépasse 2L dans 3 % des mondes à r₀ = 0, 2,3 % à 0,3 et 2 %
  à 0,8. En revanche, **faux blocage pour E < 60** : à E = 59, r₀ = 0,2, cette part monte à **13 %** (4 à 6 % par
  cellule), parce que 2L = 0,051 ne laisse que trois alertes sur 59 épisodes (CV3-3).
- **M4** : la partition est complète pour r₀ < 0,5 (confirmé, réfuté, sinon non concluant ; audit si le maximum dépasse 0,10).
  « Non lisible si r₀ ≥ 0,5 » est prudent : la table donne encore 0,075 > L + 0,02 à r₀ = 0,5. Cela ne crée pas de faux
  « confirmé ». Le trou est ailleurs : la « borne basse » n'existe pas dans la sortie (CV3-2). Le texte ne dit pas non plus
  si l'audit « maximum > 0,10 » s'applique quand r₀ ≥ 0,5 (je le lis oui ; à écrire).

### 5. Lectures restantes qui laissent passer un faux « confirmé » ou qui bloquent à tort

- **Faux blocage** : le verdict placebo sur M4 (CV3-1) et la borne de M3 pour E < 60 (CV3-3).
- **Fausse attribution** : M2 ter « dépendance naturelle suffisante » (CV3-4).
- **Lecture libre** : pour le « confirmé » de M4, l'auteur choisit après coup quelle borne basse lire (CV3-2).
- Pas de faux « confirmé » trouvé sur M1, sur M4 (au point près), ni sur M3.

### 6. Chiffres cités contre leurs fichiers

Tous conformes : 1 − 0,99⁵⁰ = 0,395 ; 0,0725 pour T uniforme de 5 à 10 et 0,077 pour T = 8 (recalculés) ; table (réponse 3) ;
K = 39, rang 38, niveau 0,05, plis de 6 (manifeste synthétique) ; « ≈ 0,25 » du descriptif (sortie synthétique 0,23 à
0,27) ; 0,21 à 0,35 (docstring de `sequentiel.py`, lignes 7 et 8). Un énoncé faux : « niveau exact 1/(K + 1) = 0,05 pour
K = 39 » (CV3-5).

## Constats

### CV3-1 — Le verdict placebo sur M4 bloque à tort (moyen à grave)

- **Où** : tableau des prédictions, ligne « contrôle placebo » (« statistiques conformes seulement (M3, M4) … écart > 0,05 →
  audit R4 ») ; critères, ligne « placebo ≠ réelles sur une cellule conforme ».
- **Problème** : les cellules de M4 ne sont pas à calibrage partagé. Leur taux dépend de r₀ (table : 0,194 à r₀ = 0 ; 0,124
  à 0,2 ; 0,075 à 0,5). Une sonde réelle, qui lit un trait de la tâche, peut avoir un r₀ plus élevé qu'une sonde placebo
  appariée en covariance. C'est l'argument qui a retiré M1 et M2 du verdict placebo (CM-6). Un écart de r₀ de 0,2 suffit
  à donner un écart de ≈ 0,07 > 0,05, donc un audit R4 sans défaut. Le phénomène est invisible dans la sortie synthétique,
  où réelles et placebo ont la même loi.
- **Correction** : borner le verdict placebo aux 24 cellules de M3 (calibrage partagé, niveau L quel que soit r₀). Pour M4 et
  le bras descriptif, rapporter l'écart avec le r₀ des deux groupes, ou comparer chaque groupe à la table à son propre r₀.
  On peut garder le maximum de M4 dans le verdict (0,019 à 0,026 pour tout r₀).

### CV3-2 — La « borne basse » de M4 n'est pas calculée ; la table et le script n'agrègent pas pareil (moyen)

- **Où** : Seuil, M4 (« médiane des cinq sommes > L + 0,02 et borne basse > L ») ; script, ligne 381 ; table, ligne 39.
- **Problème** : le script calcule `M4_mediane_des_cinq_sommes_reelles`, soit la médiane, sur les cinq statistiques, des
  médianes sur les sondes, mais il ne lui attache aucun intervalle. Il n'existe que des intervalles par statistique. La
  « borne basse » reste à choisir après lecture : la plus basse des cinq ? leur médiane ? C'est une liberté de lecture sur un
  verdict. La table gelée, elle, prend par sonde la moyenne des cinq sommes, puis la médiane sur les sondes. Ce n'est pas la
  même quantité. La sortie synthétique ne permet pas de calculer celle de la table, mais elle montre déjà que l'ordre
  compte : la médiane des cinq médianes vaut 0,090, leur moyenne 0,086.
- **Correction** : définir une seule quantité, par exemple « par sonde, moyenne des taux des cinq sommes ; médiane sur les
  sondes réelles ». La calculer dans le script, avec son intervalle par grappes, et la même dans la table. Écrire « borne
  basse de cet intervalle ».

### CV3-3 — Pour E < 60, la borne d'audit de M3 bloque à tort et la table de M4 ne vaut plus (moyen)

- **Où** : Seuil, M3 (« audit R4 si une médiane > 2 L ») ; prédictions, M4 (« valeur de la table … ± 0,05 ») ; Plan, Taille
  (« ≥ 44 gardés »).
- **Problème** : L vaut 0,05 à E = 60, mais 1/(K + 1) = 0,026 à 0,040 pour E de 44 à 59 (`m3`, tableau
  `niveaux_manifeste_selon_E`). À E = 59, 2L = 0,051 laisse trois alertes sur 59 épisodes. Dans le pire cas (sondes
  parfaitement corrélées), un audit sans défaut arrive dans 13 % des mondes, contre 2 à 3 % à E = 60. De même, la table de
  M4 est faite à E = 60 : à E = 59, les sommes valent 0,083 au lieu de 0,128 (r₀ = 0,2).
- **Correction** : audit si une médiane > max(2L ; 0,10), et zone fragile ]1,6 L ; max(2L ; 0,10)] ; ou une borne en nombre
  d'alertes tirée de la loi binomiale (E, L). Je ne l'ai pas simulé ; à vérifier sous le nul avant scellement. Pour M4 :
  « si E < 60, la table est refaite au E observé avec `table_m2bis_m4_v3.py`, scellée, avant toute lecture d'un taux ». E se
  lit au chargement, sans lire de taux. Sinon, exprimer la prédiction en excès sur L.

### CV3-4 — M2 ter attribue à la dépendance ce que la forme des marges produit aussi (moyen)

- **Où** : hypothèse M2 ter ; Seuil (« dépendance naturelle suffisante ») ; critères, ligne M2 ter.
- **Problème** : la règle de Ville suppose des scores standardisés gaussiens et indépendants. À r₀ = 0, sans aucune
  dépendance, son taux à τ = 0 passe de 0,005 (marges gaussiennes) à 0,016 (Student à 3 degrés) et 0,041 (lognormale
  standardisée, asymétrie ≈ 3,7) (`marges`, 360 sondes par loi). Avec r₀ entre 0,3 et 0,5, où la table gaussienne donne
  0,05 à 0,08, l'asymétrie des scores de P3 peut à elle seule faire passer Ville au-dessus de α. « La dépendance naturelle
  suffit » serait alors une attribution fausse.
- **Correction** : écrire « dépendance naturelle ou forme des marges (non séparées) ». Ou ajouter un bras descriptif
  « mélange » : Ville à τ = 0 sur les scores dont les actions sont permutées entre épisodes. Les marges sont gardées et r₀
  tombe vers 0. La différence réelles moins mélange isole alors la dépendance. Graine dérivée, consignée.

### CV3-5 — Formule du niveau conforme fausse dans le texte ; L sous-estimé à E = 59 (mineur à moyen)

- **Où** : hypothèse M3 (« niveau exact 1/(K + 1) = 0,05 pour K = 39 ») ; Métrique (« niveau exact 1/(K + 1) »).
- **Problème** : le niveau exact est (K + 1 − ⌈(K + 1)(1 − α)⌉)/(K + 1). Il vaut 2/40 = 0,05 pour K = 39 (1/40 = 0,025), et
  1/(K + 1) seulement pour 19 ≤ K ≤ 38. Le code est juste (ligne 326), comme la ligne M3 du tableau (« 0,05 si E = 60 ;
  sinon 1/(K + 1) »). Les deux phrases ne le sont pas. Autre point : le manifeste donne L pour le plus petit K. À E = 59
  (un pli à K = 39), le niveau réel simulé est 0,029 pour un L de 0,0256.
- **Correction** : corriger les deux phrases. Définir L comme la moyenne sur les plis, pondérée par la taille du pli, de
  (K_f + 1 − rang_f)/(K_f + 1), et la consigner au manifeste.

### CV3-6 — M4 : « seule la dépendance change » est trop fort (mineur)

- **Où** : hypothèse M4, Métrique.
- **Problème** : la moyenne et la variance sont gardées (vérifié). La forme des marges, elle, change : une lognormale
  d'asymétrie 3,7 tombe à 0,33 (`transfo`). Cela rend M4 plus prudent, surtout pour le maximum, et ne crée pas de faux
  « confirmé ». Mais la phrase est inexacte. Le bras M4 reprend aussi les tirages d'effet de τ = 2, sans que le texte le dise.
- **Correction** : écrire « mêmes deux premiers moments marginaux ; la forme des marges se rapproche de la gaussienne » et
  « tirages d'effet : ceux de τ = 2 ».

### CV3-7 — Deux gardes non exercées (R5) (mineur)

- **Où** : `test_gardes`, lignes 253 à 255 ; `correlation_intra_episode`, ligne 173 ; `main`, lignes 315 à 319.
- **Problème** : la ligne « E_minimal » est produite par une comparaison écrite dans le test, pas par la garde de `main()`. La
  garde de la corrélation intraclasse et celle du K dans `main()` ne sont jamais déclenchées.
- **Correction** : sortir la garde de E dans une fonction et la tester sur 40 et sur 60. Tester la corrélation intraclasse sur
  des scores constants. Ou lancer `main()` en sous-processus sur le petit fichier synthétique et vérifier le message.

### CV3-8 — « Tenu » et « fragile » se recouvrent ; les cellules de M3 ne sont pas listées (mineur)

- **Où** : Seuil, M3 ; critères (première ligne : « M3 tenu »).
- **Problème** : une médiane à 1,8 L est à la fois « tenue » et « fragile ». La première ligne de lecture s'applique-t-elle
  alors ? D'après « la lecture continue », oui, mais ce n'est pas écrit. Le texte ne dit pas non plus que M3 couvre les
  24 cellules à calibrage partagé (6 statistiques × 4 τ, sondes réelles), hors bras M4 et descriptif.
- **Correction** : écrire « tenu (fragile compris) » et lister les 24 cellules.

### CV3-9 — Provenance et restes (mineur)

- La section « Contre-lecture » dit « CM-9 accepté (commit `ffd5968c` …) » : c'est le commit de la v2. Elle dit aussi que la
  v3 « est relue par le même contre-lecteur sur les seuls changements (`complement-v3.md`) ». C'est faux : elle a été relue en
  entier par un contre-lecteur neuf. Citer ce rapport, son chemin et son empreinte.
- « Contrôle 19 de la conception du pari, v3 § 5 » : donner le chemin et l'empreinte
  (`brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/pari-de-signe/conception-pari-de-signe-v3.md`,
  `1518a12f…`, ligne 117), et dire pourquoi la v3 plutôt que la v5 (`95af46e4…`).
- La docstring du module garde « σ_cal » (ligne 24).
- L'en-tête doit dire que l'essai synthétique a été fait avec 5 tirages et sans commit.
- La prédiction de M2 ter ne dit rien pour r₀ entre 0,3 et 0,5 (le Seuil renvoie alors à « rapporté avec r₀ », ce qui suffit).
- M1 « réfuté » (taux ≤ 0,03) voudrait encore dire que le seuil par action n'est pas un comparateur par épisode, mais
  trop prudent cette fois. La ligne de lecture le dit à demi ; on peut l'écrire.

## Chiffres de ce rapport et leurs fichiers

| chiffre | fichier |
|---|---|
| table refaite r₀ = 0,2 et 0,8 | `sortie-verif-cv3-table-0_2-v1.json`, `sortie-verif-cv3-table-0_8-v1.json` |
| M3 sous le nul : 3 % / 2,3 % / 2 % à E = 60, 13 % à E = 59 ; niveau 0,029 contre L = 0,0256 ; L selon E | `sortie-verif-cv3-m3-v1.json` |
| Ville τ = 0, r₀ = 0 : 0,005 / 0,016 / 0,041 | `sortie-verif-cv3-marges-v1.json` |
| M4 sommes 0,128 (E = 60) contre 0,083 (E = 59) | `sortie-verif-cv3-m4E-v1.json` |
| variance, corrélation intraclasse, asymétrie sous M4 | `sortie-verif-cv3-transfo-v1.json` |
| gardes | `sortie-test-gardes-v3.json` |
| sortie synthétique de l'auteur (médiane 0,090 et moyenne 0,086 des cinq médianes de M4 ; 5 tirages) | `sortie-synthetique-essai-v3.json` (`0983f06b…`) |

Les empreintes des scripts et sorties sont dans leurs compagnons `.sha256`.

Fin : 2026-10-28 00:05:38 UTC (`date -u`).
