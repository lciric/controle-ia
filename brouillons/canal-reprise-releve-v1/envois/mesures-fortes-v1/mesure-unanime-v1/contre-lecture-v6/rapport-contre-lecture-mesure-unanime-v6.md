# Contre-lecture (R2) : préenregistrement « mesure unanime » v6, son script, sa table, son essai et la lecture mécanique v2

**Verdict : à corriger en v7.** Les six constats de la v5 sont fermés : CV5-1, CV5-2 et CV5-4 à CV5-6 entièrement, CV5-3
sur le fond, avec un reste (CV6-2). CV4-1 et CV4-4 sont fermés. Un constat demande une correction avant le scellement : la **ligne de lecture** de
`lecture_mecanique_v2.py` ne tient pas compte de l'audit du placebo. Si le placebo est en audit et que M1 et M4 sont
confirmés, elle imprime « la synthèse a raison … proposé à Lazar pour G1 et H2 » ; c'est un faux « confirmé », vérifié en
lançant (CV6-1). Elle cache aussi l'audit du maximum de M4, qui n'a d'ailleurs pas de ligne dans les critères. Le texte
donne en outre **deux seuils d'audit** au contrôle M2 : 0,075 dans le Seuil, 0,05 dans la table des prédictions (CV6-3). Le
reste est mineur à moyen :
- la feuille (4c) attribue une dérive de pas que rien ne mesure, et D et D′ sont tirés sur des rééchantillonnages séparés
  (CV6-2) ;
- les comparaisons tombent mal en flottant aux bornes exactes (CV6-4) ;
- quelques écarts séparent la lecture mécanique du texte (CV6-5) ;
- restes (CV6-6).

Sur les points vérifiés en lançant, tout est conforme :
- le code fait ce que le texte dit (excès apparié par sonde, mélange à pas fixé, quinze entrées des gardes, garde des
  actions invalides sur le chemin réel, refus du mode réel) ;
- l'essai synthétique v6 et la table v6 sont **reproduits à l'octet près** ;
- toutes les empreintes sont conformes.

- Contre-lecteur : sous-agent neuf Opus 5.5. Je n'ai écrit ni le préenregistrement, ni le script, ni la table, ni la
  lecture mécanique, ni aucun des rapports précédents.
- Début : 2026-10-28 01:15:17 UTC (`date -u`). Fin : dernière ligne. Les heures d'`ls` sont à l'heure de Paris (UTC + 1).
- Processeur seul. Je n'ai ouvert, chargé ni empreinté `donnees/20261019-230011-p3-reel/scores-p3.npz` ni aucun fichier de
  `donnees/` : l'empreinte `968414fc…` n'est **pas** vérifiée par moi. Je n'ai modifié aucun fichier du dépôt et je n'ai
  fait aucun commit. J'ai lancé le script v6 en `--test-gardes`, en `--synthetique` et en mode réel **sur le fichier
  synthétique** que le test des gardes écrit dans mon dossier (`gardes-cv6/`). Le script et la lecture sont importés sans
  modification dans mes vérifications : les seules enveloppes posées le sont sur des noms du module (un compteur, un
  mélange fautif, un rang abaissé), jamais sur le fichier.
- Pendant ma session, `git status` montre des fichiers modifiés dans `envois/pole-scientifique-automatique-v1/`, et un
  `python -m unittest` tourne qui n'est pas à moi : c'est une autre session. Rien n'a bougé dans le dossier de la mesure
  unanime.

## Empreintes lues

| fichier | empreinte | état |
|---|---|---|
| `preenregistrement-mesure-unanime-v6.md` | `24b5785bfba3e5baf49101739b4ff99e97bf099f7c011782f5d914713b156de9` | objet ; identique dans `d9530ee1` (HEAD) ; pas encore de compagnon (normal : créé au scellement) |
| `preenregistrement-mesure-unanime-v5.md` | `29f91ff3ac7dfff277b051e1fe2d99447fe2a569ddba6527b7de546935270320` | conforme à l'en-tête ; v4 `57187171…`, v3 `3a52f304…`, v2 `e6369f43…`, v1 `7158affc…` conformes |
| `analyse_fausses_alertes_v6.py` | `603ffeb34465843470ea81b7134d891415a61e34fef0d6e555931e9619ccfb49` | conforme ; compagnon conforme ; identique dans `843eb7ce` (cité) |
| `sortie-synthetique-essai-v6.json` | `7de6e1a8975ce2a823c4fdd5176e294993627bd12ec2a70b0abe1215cd13a575` | conforme ; compagnon conforme ; dans `843eb7ce` ; **reproduit à l'octet près** (`--synthetique --tirages 5 --bootstrap 300`, 78 s) ; manifeste : `"bootstrap": 300` |
| `table_m2bis_m4_v6.py` | `4b8e536d246ffc8cd8955f213911851a9921156203bdf68cc5ab0f9b52e7bb6d` | conforme ; compagnon conforme ; dans `843eb7ce` ; ne diffère de la v5 que par le numéro de version |
| `table-m2bis-m4-v6.json` | `8a4e7eff134c785ac2c67d2f088a96fe647615ebf50d57fe044d343b37734bd7` | conforme ; compagnon conforme ; dans `843eb7ce` ; **reproduite à l'octet près** (804 s) ; chiffres identiques à la v5 (seul le nom du script change) |
| `lecture_mecanique_v2.py` | `62df1370e04e48daac5a8a8b9633bab7e02ec13df58f353399c53b623dde4e46` | conforme ; compagnon conforme ; dans `843eb7ce` |
| `contre-lecture-v5/rapport-…-v5.md` ; `contre-lecture-v4/rapport-…-v4.md` | `912dd47a…a5` ; `ef6b8770…7d4f86` | conformes ; compagnons conformes |
| `contre-lecture-v1/rapport-…-v1.md` ; `complement-v2.md` ; `contre-lecture-v3/rapport-…-v3.md` | `5d47ae52…bf2d` ; `e5ca74bb…f7dc` ; `0fb0734a…214c` | conformes |
| `src/controle_ia/bases/sequentiel.py` | `35a0983404d7a10d0bb736fa37307a108501785a207c27346be1cd02bab11ba8` | conforme ; « 0,21 à 0,35 » aux lignes 7 et 8 |
| synthèse `docs/notes/collisionneur-mesures-fortes-v1/synthese-mesures-fortes-v1.md` | `bed9107b…885e` | conforme sur `origin/main` ; « environ 40 % » à sa ligne 37 |

Aucun espace réservé « ⟨…⟩ ». Les seuls gabarits sont `<chemin absolu>`, `<E>`, `<commit du scellement>`, `<table en
vigueur>` et `<sortie des effectifs>` dans les commandes ; ils sont voulus.

## 1. Fermeture de CV5-1 à CV5-6 (et restes de CV4-1, CV4-4)

| constat | état | où et pourquoi |
|---|---|---|
| CV5-1 (seconde lecture de M2 ter par r₀) | **fermé** | La colonne « réfutation » de M2 ter dit « aucune réfutation formelle : l'issue est celle du Seuil (huit issues ordonnées) ; r₀ rapporté » (ligne 105). L'Hypothèse dit « le Seuil dit pourquoi » (lignes 65 et 66). r₀ n'est une condition nulle part dans M2 ter. Détail : « s'il dépasse α … huit issues » ; au-dessus de α, il en reste sept (CV6-6). |
| CV5-2 (excès du script ≠ texte et table) | **fermé** | Script, lignes 509 à 513, 524 et 528 : la différence est prise par sonde (`taux_m4(bras) − taux_m4(τ = 0)`), puis la médiane. Le rééchantillonnage tire les mêmes épisodes pour les deux termes (lignes 527 et 528). Le placebo est traité de même (ligne 532), et la différence des médianes est rapportée à côté (ligne 530). La table calcule la même quantité (lignes 53 à 62, médiane des différences par couple monde-sonde). L'essai v6 donne 0,037 (par sonde) et 0,0383 (différence des médianes), comme le constat de la v5 le prévoyait. Texte : lignes 29 à 31, 89 à 92, 109 et 154 à 158. |
| CV5-3 (trois issues attribuent trop) | **fermé, avec un reste** | Seuil, lignes 174 à 185 : (2a) exige le mélange > α, sinon (2b) « non attribuable » ; (3a) exige bb(D′) > 0, sinon (3b) ; (4a) exige Ville sur le mélange à pas fixé ≤ α, sinon (4b). Les huit lignes des critères existent (lignes 220 à 229). La lecture applique le même arbre (vérifié sur les 32 combinaisons, réponse 2). Reste : la feuille (4c) affirme une « dérive de pas » sans la mesurer, et D et D′ ont des rééchantillonnages séparés (CV6-2). |
| CV5-4 (r₀ biaisé par la dérive) | **fermé** | Ligne 144 : « attendu ≈ 0 **sans dérive** » ; lignes 147 à 150 : r₀ centré par pas, rapporté, jamais une condition ; ligne 145 : « pas » = indice brut. Le script applique ces trois points : `centrer_par_pas` (lignes 141 à 149) travaille sur la colonne de `X`, et la colonne de `X` est l'indice `pas` des données (ligne 265) ; les sorties sont aux lignes 484 et 485. Simulation : avec r₀ = 0,4 et une dérive de ± 0,3 par pas, r₀ brut vaut 0,25 à 0,30 et r₀ centré 0,34 à 0,40 ; la réserve de la lecture se déclenche. Le seuil « écart notable » n'est pas écrit dans le texte (CV6-5). |
| CV5-5 (deux dossiers de travail) | **fermé** | Plan, lignes 199 à 211 : tout est lancé depuis le dossier du préenregistrement, avec le chemin absolu des données. J'ai tout lancé ainsi, table comprise. |
| CV5-6 (restes) | **fermé** | « + 8 du mélange à pas fixé » (lignes 195 et 196) ; liste de M3 (lignes 83 et 84) ; décompte des gardes (lignes 22 à 25), juste : cinq cas sains, quatre artefacts de calcul, trois de chargement, E minimal, corrélation constante, plus la valeur ; `bootstrap` au manifeste (script, ligne 428 ; essai : 300) ; docstring de `un_passage` (lignes 188 à 190) ; « moyennes » (lignes 71 et 72). |
| CV4-1 (deux définitions de M2 ter) | **fermé** | Une seule définition (Seuil), sans r₀ ; la colonne « réfutation » est alignée (ligne 105). |
| CV4-4 (attributions trop larges) | **fermé, reste dans CV6-2** | (i) « marges et dépendance » quand le mélange dépasse α, et (ii) le mélange à pas fixé sont en place. Le reste, sur (4c), est l'analogue de CV5-3. |

## 2. Réponses aux points du brief

**Point 2 : M2 ter, un arbre à huit feuilles.**
- **Partition** : exhaustive et sans recouvrement. Les « sinon » sont emboîtés sur cinq conditions binaires : Ville réelles
  ≤ 0,05 ; bb(D) ≤ 0 ; Ville mélange > α ; bb(D′) > 0 ; Ville mélange à pas fixé ≤ α. Sur les 32 combinaisons, j'ai
  comparé `lecture_mecanique_v2.lire` à ma réécriture du Seuil à partir du texte : chaque combinaison tombe dans une feuille
  et une seule, les huit feuilles sont atteintes (1 : 16 ; 2a : 4 ; 2b : 4 ; 3a : 2 ; 3b : 2 ; 4a : 1 ; 4b : 1 ; 4c : 2), et
  il n'y a **aucun désaccord** (`sortie-verif-cv6-lecture-v1.json`).
- **Critères** : chaque feuille a sa ligne dans les critères.
- **r₀** : il n'est une condition nulle part dans M2 ter.
- **Attributions** : (2a), (2b), (3a), (3b), (4a) et (4b) sont justifiées par ce qui est mesuré ; (3b) dit bien « dérive
  possible ». (4c) ne l'est pas (CV6-2).
- **Définition de D et D′** : le texte ne dit pas comment ils sont définis. Le script prend la différence des médianes,
  alors que l'excès de M4 est désormais une médiane des différences par sonde (CV6-5).

**Point 3 : excès apparié de M4.**
- **Médiane sur les sondes des différences par sonde** : oui, voir CV5-2.
- **Même calibrage** : oui. À τ = 0, `Xe = X` et `Xcal = X` ; le bras M4 a `calibrage_sans_effet=True`, donc `Xcal = X`. Les
  deux termes ont la même permutation et les mêmes plis, donc les mêmes μ₀, σ et seuils (script, lignes 195 à 218, 470 et
  474).
- **Rééchantillonnage apparié** : oui (lignes 526 à 528).
- **La table** calcule le même excès.
- **Le faux « confirmé » par M3 « fragile » (CV4-2) est fermé.** J'ai abaissé d'un cran le rang conforme, dans les deux
  termes à la fois (`sortie-verif-cv6-defaut-niveau-v1.json`, 12 sondes, 10 tirages) :

  | r₀ | niveau à τ = 0 | excès par sonde |
  |---|---|---|
  | 0,2 | 0,048 → 0,078 | 0,0678 → 0,0688 (+0,001) |
  | 0,5 | 0,040 → 0,063 | 0,0413 → 0,0435 (+0,002) |

  Un défaut de niveau de 0,02 à 0,03, commun aux deux termes, ne déplace donc l'excès que de 0,001 à 0,002, bien en deçà du
  seuil de 0,02. Le résidu de second ordre que la v5 estimait à environ 0,2 δ est plus petit encore ici (0,03 à 0,09 δ).
- **Nouveau faux « confirmé » ou faux blocage dans le calcul de l'excès** : je n'en trouve pas. Il en existe un en flottant,
  à la borne exacte de 0,02 (CV6-4), et un dans la ligne de lecture (CV6-1).

**Point 4 : mélange à pas fixé** (`sortie-verif-cv6-pas-fixe-v1.json`, 12 sondes, 10 mélanges, 2 mondes par scénario).
- **Marges par pas et masque** : gardés. Le code le montre (lignes 152 à 161), et le test des gardes le vérifie sur chaque
  pas (lignes 317 à 323).
- **Dépendance intra-épisode** : détruite. Avec r₀ = 0,4, sans dérive :
  - r₀ vaut 0,384 et 0,367 à l'origine, 0,003 et −0,001 sur le mélange à pas fixé ;
  - Ville vaut 0,075 et 0,042 sur les réelles, 0,005 sur le mélange à pas fixé ;
  - D et D′ sont égaux à 0,002 près.
- **Dérive linéaire avec le pas, sans effet épisode** (± 0,3 écart type par pas) :
  - avec des masques dispersés, le r₀ du mélange à pas fixé suit le r₀ d'origine (−0,045 contre −0,047 ; −0,049 contre
    −0,044 ; −0,047 contre −0,040 ; −0,051 contre −0,049) : la dérive survit ;
  - avec des masques en préfixe, le biais est faible des deux côtés (−0,001 à −0,027) ;
  - le r₀ centré par pas revient vers 0 (−0,013 à +0,014).
- **Ce que la question 4 attendait et qui n'arrive pas** : « réelles moins mélange complet > 0 ».
  - Une dérive linéaire de la moyenne, montante ou descendante, en préfixe ou dispersée, ne fait pas monter Ville : Ville
    réelles vaut 0 à 0,008, et D va de −0,005 à +0,003. D′ ≈ 0, comme attendu.
  - La raison : la standardisation est globale, et elle absorbe la dérive dans σ.
  - Ce n'est pas un défaut du mélange. En revanche, une dérive de moyenne **ne peut pas** produire le D > 0 qu'exige la
    feuille (4c), ce qui affaiblit encore son étiquette (CV6-2).

**Point 5 : gardes.**
- **`--test-gardes`** sort **quinze entrées**, soit quatorze gardes et `correlation_saine` = 0,171
  (`sortie-test-gardes-v6.json`).
- **`verifier_scores_invalides` est appelée sur le chemin réel** (`sortie-verif-cv6-chemin-reel-v1.json`) :
  - elle est appelée en tête de `un_passage` (ligne 192) ;
  - pendant un `main()` complet en mode réel sur le fichier synthétique (3 réelles, 2 placebo, 20 tirages, 2 000
    rééchantillonnages), elle est appelée **705 fois**, soit 5 × (1 + 3 × 20 + 2 × 20 + 2 × 20) : une fois par passage ;
  - avec un mélange fautif, qui écrit un score hors du masque, `main()` **s'arrête** sur « liste d'arrêt : score porté par
    une action invalide ».
- **Refus vérifiés en lançant** (`sortie-refus-mode-reel-v6.txt`) :
  - `--effectifs-seulement` sans empreinte, ou avec une empreinte vide ;
  - une empreinte fausse ;
  - `--tirages 5` ou `--bootstrap 300`, avec ou sans `--effectifs-seulement` ;
  - l'absence de `--commit` ou de `--sondes-placebo` ;
  - des effectifs faux (4 réelles ; 1 placebo) ;
  - `--reel` avec `--synthetique` ;
  - E = 40 (< 44).
- **Passent** : les valeurs par défaut écrites explicitement (`--tirages 20 --bootstrap 2000`). Le mode
  `--effectifs-seulement` sort E = 60, K = 39 dans les dix plis et L = 0,05 (`sortie-effectifs-synthetique-v6.json`).
- **Un reste** : dans le test, la garde des actions invalides ne lève pas si elle dort (CV6-6).

**Point 6 : chiffres cités.** Ceux que j'ai recalculés sont conformes :
- 0,395 ; 0,0725 et 0,077 ; 2/40 ; K = 39, rang 38 ;
- table v6 : Ville à τ = 0 (0 ; 0,033 ; 0,083 ; 0,133) ; Ville à τ = 2 (0,1375 à 0,1521) ; M2 bis (+0,138 ; +0,104 ;
  +0,065 ; +0,019) ; excès (0,143 ; 0,073 ; 0,027 ; 0,006) ; quantité brute (0,194 ; 0,124 ; 0,075 ; 0,0545) ; maximum
  (0,019 à 0,026, soit 0,38 à 0,52 L) ;
- essai v6 : D et D′ = 0,030 et 0,030 à r₀ = 0,201 ; descriptif 0,23 à 0,27 ;
- contre-lecture v3 : 0,005 ; 0,016 ; 0,041 (son rapport, lignes 181 et 244) ;
- docstring de `bases/sequentiel.py`, lignes 7 et 8.

Le « +0,03 » est attribué à l'essai **v5**, dont l'empreinte n'est plus dans la v6 ; l'essai v6 donne le même chiffre
(CV6-6). Le test de la lecture mécanique « sur l'essai synthétique » (lignes 26 et 27) n'a pas de sortie déposée (CV6-6).
Je l'ai refait (réponse 7).

**Point 7 : ce que je n'avais pas vu venir.** J'ai lancé la lecture mécanique sur l'essai v6 tel quel, puis sur des copies
modifiées (`sortie-verif-cv6-lecture-v1.json`).
- **Sur l'essai tel quel**, les verdicts sont M1 confirmé, M3 tenu, M4 confirmé, M2 ter (1). Sur la sortie du mode réel
  lancé sur mon fichier synthétique, ce sont M1 confirmé, M2 ter (4a), M3 tenu, M4 confirmé
  (`sortie-lecture-mecanique-sur-mode-reel-synthetique-v6.json`).
- **Placebo en audit** : la ligne de lecture dit « la synthèse a raison » (CV6-1).
- **Maximum de M4 > 0,10** : le verdict de M4 est bien l'audit, mais la ligne dit seulement « M1 confirmé ; voir les lignes
  des critères » (CV6-1).
- **M2 bis à r₀ = 0,6, écart de 0,12 à la table** : la lecture dit « aucune réfutation » et ne dit plus « hors table »
  (CV6-5).
- **Cellule conforme à médiane et troisième quartile nuls**, avec 10 % des sondes au-dessus de 2α : la lecture dit « trop
  propre », alors que le texte dit « à 0 pour toutes les sondes » (CV6-5).
- **En flottant** : L = 0,05000000000000001, donc 0,4 L = 0,020000000000000004. Un excès égal à 0,02 en valeur exacte est
  lu « > 0,02 » dans 54 % des cas (CV6-4, `verif-flottant-sortie.txt`).
- **La lecture ne vérifie pas le manifeste de la sortie** : ni les empreintes du script et des données, ni les tirages et
  rééchantillonnages, ni que la table en vigueur a le même E que la sortie. Elle lit l'essai synthétique à 5 tirages sans
  rien dire (CV6-6).

## 3. Constats

### CV6-1 : la ligne de lecture ignore l'audit du placebo et cache celui du maximum de M4 (moyen : faux « confirmé » possible)

- **Où** :
  - `lecture_mecanique_v2.py`, lignes 144 à 154 : la ligne ne teste que les audits de M3 et de M2 contrôle ;
  - texte, critères, ligne 233 : le placebo donne « audit R4 », sans dire si le reste se lit ;
  - Seuil, lignes 172 et 173, et prédictions, ligne 109 : « maximum > 0,10 → audit, à tout r₀ » ;
  - critères, lignes 215 à 234 : **aucune ligne** pour l'audit du maximum de M4.
- **Problème** :
  - J'ai pris l'essai v6 et posé un écart réelles − placebo de 0,08 sur une cellule de M3. Le verdict du placebo devient
    « AUDIT R4 sur ['tau=1.0:somme_terminale'] », mais la ligne de lecture reste « première ligne : la synthèse a raison
    (…) — proposé à Lazar pour G1 et H2 ».
  - Or la note de lecture « reprend sa table telle quelle » (ligne 27). Un artefact que le placebo est là pour voir (fuite,
    plis, rang) laisserait donc passer la proposition à Lazar. C'est le faux « confirmé » que la symétrie (R4) interdit.
  - Avec un maximum de M4 à 0,12, la ligne ne dit pas « audit ».
  - « Cellule à zéro » (trop propre, R4) n'apparaît pas dans la ligne non plus.
- **Correction** :
  - Texte, Seuil et critères :
    - écrire que **tout audit** suspend la lecture : contrôle M2 non atteint, M3 > B, maximum de M4 > 0,10, placebo
      > 0,05 sur une des 24 cellules ou sur le maximum de M4. Rien d'autre n'est lu avant l'audit, comme pour M3 ;
    - ajouter la ligne « M4 audit (maximum conforme > 0,10) : audit R4 avant tout » ;
    - dire que « cellule à zéro » est une réserve portée sur la ligne.
  - Lecture v3 : `ligne = "audit avant toute lecture : " + liste` dès qu'un verdict contient « AUDIT » ; la réserve « trop
    propre » est ajoutée à la ligne.
  - La retester sur les huit feuilles et sur ces trois cas, puis **déposer la sortie du test** avec son compagnon.

### CV6-2 : la feuille (4c) affirme une « dérive de pas » que rien ne mesure, et D et D′ ont des rééchantillonnages séparés (mineur ; reste de CV5-3)

- **Où** :
  - Seuil, lignes 183 et 184 ; critères, ligne 226 : « une dérive des scores avec le pas (seule ou mêlée à la dépendance)
    fait monter Ville » ;
  - script, lignes 534 à 547 : deux boucles de rééchantillonnage distinctes, l'une pour D (536 à 538), l'autre pour D′ (543
    à 545), chacune avec ses propres tirages d'épisodes.
- **Problème** :
  - (4c) se lit sur « bb(D) > 0 et bb(D′) ≤ 0 ». Ce n'est pas une mesure de la dérive : c'est une **absence de preuve**
    sur D′. La dérive se lirait sur Ville(mélange à pas fixé) − Ville(mélange), que personne ne calcule.
  - Deux faits rendent (4c) surtout sensible au bruit :
    - (a) **une dérive de la moyenne ne fait pas D > 0** (point 4 : D de −0,005 à +0,003). Ce qu'elle laisse, c'est
      D′ ≈ D ;
    - (b) **les deux bornes basses viennent de tirages différents**. Elles bougent alors de façon indépendante, d'environ
      un pas de grille de la médiane, soit environ 1/120.
      - Dans le monde 2 du scénario 1, D = D′ = 0,0458 exactement (même mélange, 0,0042 des deux côtés). Le script donne
        pourtant bb(D) = 0,0138 et bb(D′) = 0,0208, alors qu'un tirage partagé donne 0,0133 et 0,0133 (`journal-4c-a.txt`).
      - Sur 20 répliques indépendantes des deux boucles, D − D′ reste entre −0,001 et +0,001, mais l'écart |bb(D) − bb(D′)|
        monte jusqu'à 0,008 (`sortie-verif-cv6-feuille-4c-r040-c09-v1.json`, `…-r028-c09-v1.json`).
  - Quand la borne basse vraie est à moins d'environ 0,008 de 0, les deux boucles peuvent tomber de part et d'autre de 0
    **sans aucune dérive**. Le Seuil dit alors (4c) « avec dérive de pas » ou (4a), selon la graine du rééchantillonnage.
  - La fréquence est faible. Sur mes 13 mondes sans dérive (r₀ de 0,28 à 0,40, sondes corrélées entre elles), aucun ne
    tombe en (4c) : quand Ville réelles > α, bb(D) vaut 0,013 à 0,063, et aucune réplique ne change de feuille.
  - Ce sont des étiquettes rapportées, pas une porte. Mais (4c) attribue une cause sur P3, alors qu'une dérive de la
    moyenne ne peut pas la produire.
- **Correction** :
  - (i) Script : un **seul** tirage d'épisodes par rééchantillonnage pour le terme réel, le mélange et le mélange à pas fixé.
    D et D′ y gagnent la même incertitude, et leur écart ne reflète plus que l'écart des deux mélanges. Calculer aussi
    D″ = Ville(mélange à pas fixé) − Ville(mélange), avec son intervalle apparié.
  - (ii) Seuil : (4c) devient « **structure intra-épisode, dépendance non séparée de la dérive** » (non attribuable entre
    les deux, rapporté avec D, D′ et D″). « Dérive de pas » n'est écrit que si bb(D″) > 0.
  - Même règle, facultative, pour l'étiquette « dérive » de (4b), qui repose sur deux valeurs ponctuelles :
    mélange à pas fixé > α ≥ mélange.

### CV6-3 : deux seuils d'audit pour le contrôle M2 (mineur à moyen : liberté de lecture sur un audit)

- **Où** : Seuil, lignes 167 et 168 (« attendu si médiane à τ = 2 ≥ 0,075 ; sinon audit (bogue) ») ; prédictions, ligne 106
  (« réfutation : médiane ≤ 0,05 (bogue : audit) »).
- **Problème** :
  - Une médiane entre 0,05 et 0,075 est un audit pour le Seuil (et pour la lecture, ligne 64), mais pas pour la table des
    prédictions.
  - L'audit suspend toute lecture (critères, ligne 227). Deux seuils pour un arrêt, c'est la liberté de lecture que la
    série de contre-lectures ferme depuis CV4-1.
  - C'est peu probable : la table donne 0,138 à 0,152.
- **Correction** : aligner la colonne « réfutation » sur le Seuil : « médiane < 0,075 → audit (bogue) ».

### CV6-4 : comparaisons aux bornes exactes en flottant (mineur, mais il touche un verdict)

- **Où** : `lecture_mecanique_v2.py`, lignes 102 et 121 ; script, ligne 420 (L).
- **Problème** :
  - Les taux sont rationnels. Le terme du bras M4 est un multiple de 1/1 200, et la médiane de l'excès un multiple de
    1/12 000 : un excès **exactement** égal à 0,02 est atteignable.
  - En flottant, la différence de deux moyennes de booléens tombe d'un côté ou de l'autre. Sur 20 000 cas exactement à
    0,02, 10 799 sont lus « > 0,02 », donc « confirmé », alors que le texte dit « > 0,02 » strict
    (`verif-flottant-sortie.txt`).
  - De même, L = 0,05000000000000001 fait 0,4 L = 0,020000000000000004. Une cellule de M3 exactement à 0,02 (24/1 200,
    atteignable à τ > 0) est lue « fragile » ; elle ne l'est pas avec L = 0,05.
  - Les bornes basses comparées à 0 (D, D′, excès) ont le même défaut. J'ai pris 1 876 couples « médiane des réelles,
    médiane du mélange » de même valeur rationnelle : 389 donnent une différence flottante de ± 3,5 × 10⁻¹⁸ au lieu de 0. Une
    borne basse exactement nulle peut donc être lue « > 0 », c'est-à-dire « structure établie » (`verif-flottant-sortie.txt`,
    partie 3).
- **Correction** : dans la lecture, arrondir chaque quantité comparée à un seuil, par exemple à 10⁻⁹, avant la comparaison
  (`round(x, 9)`), et arrondir L de même. Le dire dans le Seuil : « comparaisons à 10⁻⁹ près ».

### CV6-5 : écarts entre la lecture mécanique et le texte (mineur)

- (a) **Réserve sur r₀** : la lecture la déclenche si |r₀ centré − r₀| > 0,05 (lignes 48 à 50). Le texte dit seulement
  « un écart notable » (ligne 148). Écrire « plus de 0,05 » dans la Métrique.
- (b) **M2 bis à r₀ ≥ 0,5** : la lecture remplace « conforme à la table » ou « hors table » par « aucune réfutation » (ligne
  69). Le Seuil donne les deux étiquettes sans condition sur r₀ et ajoute seulement « aucune réfutation ». Garder les deux
  dans la lecture : « hors table, aucune réfutation (r₀ ≥ 0,5) ».
- (c) **Cellule à zéro** : la lecture lit « médiane et troisième quartile nuls » (ligne 142) ; le texte dit « à 0 pour
  toutes les sondes » (ligne 234). `resume` ne sort pas le maximum par sonde.
  - Ajouter `max` à `resume` et lire `max == 0`, ou écrire « au moins 75 % des sondes » dans le texte.
  - Dire aussi si la règle couvre seulement les 24 cellules de M3, ou aussi les conformes du bras M4 et des mélanges.
- (d) **Définition de D et D′** : le script prend la **différence des médianes** (lignes 539 et 546). Le texte (lignes 140,
  143 et 175 à 176) ne le dit pas, alors que l'excès de M4 est désormais une médiane des différences par sonde. Écrire
  « différence des médianes sur les sondes » pour D et D′, comme pour M2 bis (ligne 107).

### CV6-6 : restes (mineur)

- **Hypothèse M2** (lignes 65 et 66) : « s'il dépasse α, le Seuil dit pourquoi (huit issues…) ». Au-dessus de α, il reste
  sept feuilles : écrire « sept issues, la huitième étant “tenue” ».
- **Prédictions, M2 ter** (ligne 105) : « synthétique v5 : +0,03 » renvoie à un essai dont l'empreinte n'est plus dans la v6.
  L'essai v6 donne le même chiffre : citer l'essai v6 (`7de6e1a8…`).
- **En-tête** (lignes 26 et 27) : la lecture mécanique est « testée sur l'essai synthétique » (le commit dit « exercé sur les
  huit »), mais aucune sortie n'est déposée (R6). Déposer ce test avec un compagnon (voir CV6-1).
- **`test_gardes`**, lignes 325 et 326 : si la garde des actions invalides dort, le test écrit « NON DÉTECTÉ » au lieu de
  lever, contre sa docstring (« lève si une garde dort ») et R5 (aucun repli silencieux). Lever une `AssertionError` comme
  pour les autres gardes.
- **`--effectifs-seulement`** (lignes 421 à 423) : la sortie ne porte ni l'empreinte des données ni celle du script, alors
  qu'elle nourrit la table refaite si E ≠ 60. Les y ajouter.
- **Lecture mécanique** (lignes 167 à 171) : elle ne garde de la table que `["table"]` et ne vérifie rien du manifeste de la
  sortie. Ajouter une garde, testée sur un cas sain et sur un artefact : empreinte du script = `603ffeb3…`, empreinte des
  données = `968414fc…`, 20 tirages, 2 000 rééchantillonnages, `commit` non vide, et le E de la table égal au E de la sortie.

## 4. Mes scripts et sorties (ce dossier, chacun avec un compagnon `.sha256`)

| fichier | contenu |
|---|---|
| `verif_cv6_v1.py` | parties `lecture` (arbre sur 32 combinaisons, audits, M2 bis, cellule à zéro), `pas_fixe` (dérive et dépendance), `feuille_4c` (bruit de rééchantillonnage sur D et D′), `defaut_niveau` (excès sous un défaut de niveau commun) ; script v6 et lecture v2 importés sans modification ; graines `SeedSequence(2810202606, spawn_key=(partie, scénario, monde))` |
| `sortie-verif-cv6-lecture-v1.json`, `sortie-verif-cv6-pas-fixe-v1.json`, `sortie-verif-cv6-defaut-niveau-v1.json` | leurs sorties |
| `sortie-verif-cv6-feuille-4c-r040-c09-v1.json`, `sortie-verif-cv6-feuille-4c-r028-c09-v1.json`, `journal-4c-b.txt`, `journal-4c-c.txt` | `feuille_4c`, scénarios 2 (r₀ = 0,4, c = 0,9, six mondes) et 3 (r₀ = 0,28, c = 0,9, quatre mondes), avec 20 répliques des deux boucles de rééchantillonnage ; journaux ligne par ligne |
| `journal-pas-fixe.txt` | journal de la partie `pas_fixe` |
| `journal-4c-a.txt` | scénario 1 de `feuille_4c` (r₀ = 0,35, sondes corrélées c = 0,5), trois mondes, arrêté par son PID pour libérer le processeur (R10) ; il a été lancé avant que j'ajoute les répliques. Les champs écrits sont reproduits à l'identique par `feuille_4c 0.35 0.5 3 0`, car les répliques ne consomment le générateur qu'après eux |
| `verif_cv6_chemin_reel_v1.py`, `sortie-verif-cv6-chemin-reel-v1.json` | 705 appels de la garde pendant `main()` en mode réel sur le fichier synthétique ; arrêt sur un mélange fautif |
| `sortie-mode-reel-sur-synthetique-v6.json`, `sortie-lecture-mecanique-sur-mode-reel-synthetique-v6.json` | ce mode réel (3 + 2 sondes, 20 tirages, 2 000 rééchantillonnages) et sa lecture mécanique |
| `sortie-test-gardes-v6.json`, `sortie-refus-mode-reel-v6.txt`, `sortie-effectifs-synthetique-v6.json` | gardes (15 entrées), refus et effectifs, vérifiés en lançant |
| `sortie-synthetique-reproduite-v6.json`, `table-m2bis-m4-v6-reproduite.json` | essai et table reproduits (`7de6e1a8…`, `8a4e7eff…`, à l'octet près) |
| `verif_cv6_flottant_v1.py`, `verif-flottant-sortie.txt` | bornes exactes en flottant (L, 0,4 L ; excès à 0,02 ; différences de médianes égales) |
| `gardes-cv6/scores-synthetique-gardes.npz`, `gardes-cv6/scores-synthetique-petit.npz` | fichiers synthétiques écrits par le test des gardes |

Interpréteur `/opt/venv-essaim-sim-v1/bin/python -I -B`, numpy 2.5.4, tout lancé depuis le dossier du préenregistrement.

Empreinte de ce rapport : dans `rapport-contre-lecture-mesure-unanime-v6.md.sha256`, à côté (un fichier ne peut pas contenir
sa propre empreinte).

Fin : 2026-10-28 01:39:07 UTC (`date -u`, relevé dans un appel séparé avant l'écriture de cette ligne).
