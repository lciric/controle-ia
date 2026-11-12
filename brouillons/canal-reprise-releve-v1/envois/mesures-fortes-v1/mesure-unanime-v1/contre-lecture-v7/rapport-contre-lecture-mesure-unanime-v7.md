# Contre-lecture (R2) : préenregistrement « mesure unanime » v7, son script, sa table, son essai, la lecture mécanique v3 et le script de séquence

**Verdict : à corriger en v8.** Un constat est **bloquant** : la lecture mécanique v3 **refuse toute sortie du mode réel**.
Elle compare le E de la table au champ `E` du manifeste de la sortie. Or ce champ n'existe qu'en mode synthétique ; en mode
réel, le manifeste porte `gardes`. Je l'ai vérifié en lançant : mode réel sur un fichier synthétique que j'ai créé, puis
lecture v3 → « E de la table (60) ≠ E de la sortie (None) », code de sortie 1 (CV7-1). La séquence gelée
(`commandes-lecture-reelle-v7.sh`) s'arrêterait donc à l'étape (3), **après** l'unique exécution réelle déjà faite et
scellée, et la lecture ne pourrait être réparée qu'une fois les données vues. Un constat moyen : une cellule conforme
« trop propre » n'atteint pas la ligne de lecture, qui peut alors dire « la synthèse a raison … proposé à Lazar »
(CV7-2, reste de CV6-1, vérifié en lançant). Le reste est mineur (CV7-3 à CV7-6).

Sur les points vérifiés en lançant, tout le reste est conforme :
- l'essai synthétique v7 et la table v7 sont **reproduits à l'octet près** ;
- l'arbre de M2 ter a **neuf feuilles**, exhaustives et disjointes, sans aucun désaccord entre la lecture v3 et ma réécriture
  du Seuil sur les 64 combinaisons ;
- tout audit (M3, contrôle M2, maximum du bras M4, placebo) suspend la ligne de lecture ;
- l'excès apparié de M4 est inchangé depuis la v6 et conforme ;
- le mélange à pas fixé fait ce que le texte dit ;
- les quinze entrées des gardes sont là, et la garde endormie lève ;
- les refus du mode réel tiennent ;
- toutes les empreintes sont conformes.

- Contre-lecteur : sous-agent neuf Opus 5.5. Je n'ai écrit ni le préenregistrement, ni le script, ni la table, ni la lecture
  mécanique, ni le script de séquence, ni aucun des rapports précédents.
- Début : 2026-10-28 01:53:10 UTC (`date -u`). Fin : dernière ligne. Les heures d'`ls` sont à l'heure de Paris (UTC + 1).
- Processeur seul. Je n'ai ouvert, chargé ni empreinté `donnees/20261019-230011-p3-reel/scores-p3.npz` ni aucun fichier de
  `donnees/`. L'empreinte `968414fc…` n'est donc **pas** vérifiée par moi. Je n'ai **pas** lancé
  `commandes-lecture-reelle-v7.sh` : je l'ai seulement lu.
- Je n'ai modifié aucun fichier du dépôt et je n'ai fait aucun commit.
- Lancé, toujours depuis le dossier du préenregistrement :
  - le script v7 en `--test-gardes`, en `--synthetique`, et en mode réel **sur le fichier synthétique** que le test des
    gardes écrit dans mon dossier (`gardes-cv7/`) ;
  - la table v7 ;
  - la lecture v3.
- Mes vérifications importent le script et la lecture sans modification. La seule enveloppe posée l'est sur un nom du module
  (une garde endormie), jamais sur le fichier.
- Pendant ma session, le commit `fb560f8b` a ajouté `rediger_note_lecture_v1.py` dans le dossier. Ce fichier ne fait pas
  partie de ma contre-lecture ; je le cite seulement en CV7-1, parce qu'il hérite du même défaut.

## Empreintes lues

| fichier | empreinte | état |
|---|---|---|
| `preenregistrement-mesure-unanime-v7.md` | `54bb2892a2083aa55a6e400628b71f6508a2462745881a2d11fa0cb723fc070a` | objet ; identique dans `HEAD` (`fb560f8b`, introduit par `71465e94`) ; `prereg.problemes` = [] ; pas de compagnon (normal : créé au scellement) |
| `preenregistrement-mesure-unanime-v6.md` | `24b5785bfba3e5baf49101739b4ff99e97bf099f7c011782f5d914713b156de9` | conforme à l'en-tête ; v5 `29f91ff3…`, v4 `57187171…`, v3 `3a52f304…`, v2 `e6369f43…`, v1 `7158affc…` conformes |
| `analyse_fausses_alertes_v7.py` | `463f910d4bf878d5c3b77a9e614d568f3a96ce7e6a3461d52831656434a7fff6` | conforme ; compagnon conforme ; identique dans `82af52c9` (cité) |
| `sortie-synthetique-essai-v7.json` | `5b1bc63bd93e0ccc838fc7cfcb61bdd14014d6263859ad75b5a6d9ba175c3fee` | conforme ; compagnon conforme ; dans `82af52c9` ; **reproduit à l'octet près** (`--synthetique --tirages 5 --bootstrap 300`, environ 70 s) |
| `table_m2bis_m4_v7.py` | `981ed2010cf32c42f4f205c3e6a2585a5ccd4f5b9d72f545af104b910737816f` | conforme ; compagnon conforme ; dans `82af52c9` ; ne diffère de la v6 que par le numéro de version |
| `table-m2bis-m4-v7.json` | `4e6fe7e1fccca4033dfdb1ccba1e24e5b9237279ba43846c466fe12c75fce66b` | conforme ; compagnon conforme ; dans `82af52c9` ; ne diffère de la v6 que par le nom du script ; **reproduite à l'octet près** (environ 570 s) |
| `lecture_mecanique_v3.py` | `6d4fbb2cb0883924ad585563c3a7baf33aef21c18d53ab07857b743962557427` | conforme ; compagnon conforme ; dans `82af52c9` |
| `essai-lecture-mecanique-v3-sur-synthetique-v7.json` | `81cd29aa5d7b479af914ad6b00d150c18b8893bdd7c40e319a3cc85ba5d6ea1c` | conforme ; compagnon conforme ; voir CV7-4 |
| `commandes-lecture-reelle-v7.sh` | `6679d908ee1a1adada25cfd17d47f8be7350d6de9c26adff363fd295562b68bc` | identique dans `HEAD` ; **pas de compagnon** et **pas cité** dans le texte (CV7-5) |
| `contre-lecture-v6/rapport-…-v6.md` | `23ce5f933117cbc6e9048132b7f89f785de53f0ecb86e93ac936f72dd9ded5b3` | conforme ; compagnon conforme |
| rapports v5, v4, v3, v1, complément v2 | `912dd47a…a5`, `ef6b8770…7d4f86`, `0fb0734a…214c`, `5d47ae52…bf2d`, `e5ca74bb…f7dc` | conformes |
| `src/controle_ia/bases/sequentiel.py` | `35a0983404d7a10d0bb736fa37307a108501785a207c27346be1cd02bab11ba8` | conforme ; « 0,21 à 0,35 » aux lignes 7 et 8 |

Il ne reste aucun espace réservé « ⟨…⟩ », « << >> » ou « À REMPLIR » dans le texte. Les seuls gabarits sont voulus, dans les
commandes : `<chemin absolu>`, `<E>`, `<commit du scellement>`, `<table en vigueur>` et `<sortie des effectifs>`.

## 1. Fermeture de CV6-1 à CV6-6 (et restes de CV4-1, CV4-4)

| constat | état | où et pourquoi |
|---|---|---|
| CV6-1 (la ligne ignore l'audit du placebo, cache celui du maximum de M4) | **fermé sur les audits ; ouvert sur la cellule à zéro** | Seuil, lignes 196 à 198 : tout audit suspend la lecture. Critères, ligne 241 : une ligne pour le maximum de M4. Lecture v3, lignes 165 à 168 : la ligne devient « AUDIT R4 avant toute lecture » dès qu'un des quatre verdicts contient « AUDIT ». Vérifié sur quatre cas : placebo à 0,08, maximum de M4 à 0,12, cellule de M3 à 0,11, contrôle M2 à 0,07 (`sortie-verif-cv7-lecture-v1.json`). Ouvert : la correction demandait de porter la réserve « trop propre » sur la ligne ; elle n'y est pas (CV7-2). La sortie du test déposée est partielle (CV7-4). |
| CV6-2 (la feuille (4c) affirme une dérive non mesurée ; tirages séparés) | **fermé, avec un reste** | Script, lignes 541 à 558 : un seul tirage d'épisodes par rééchantillonnage pour D, D′ et la dérive ; dérive = Ville sur le mélange à pas fixé moins Ville sur le mélange, avec son intervalle. Seuil, lignes 192 à 195 : (4c) exige bb(dérive) > 0, sinon (4d) « non attribuée ». Lecture v3, ligne 110 : idem. Critères, lignes 239 et 240. Reste : l'étiquette « dérive » de (4b) repose encore sur deux valeurs ponctuelles, ce que le texte interdit lui-même (ligne 195) ; et (2a) ne regarde pas D′ (CV7-3). |
| CV6-3 (deux seuils pour le contrôle M2) | **fermé** | Prédictions, ligne 112 : « médiane < 0,075 » ; Seuil, ligne 178 : « ≥ 0,075 » ; critères, ligne 242 ; lecture, ligne 82. |
| CV6-4 (bornes exactes en flottant) | **fermé** | Lecture, lignes 24 à 26 : `arr` = arrondi à 10⁻⁹. Il est appliqué à chaque comparaison à une borne (M1, contrôle M2, M2 bis, M2 ter, M3 avec L et B arrondis, M4, placebo, cellule à zéro, réserve sur r₀). Le texte le dit (lignes 160 et 196). Vérifié aux bornes : Ville à 0,05 et à 0,05000000000000001, bornes basses à 0 et à ± 3,5 × 10⁻¹⁸ ; tout tombe du bon côté. Seule exception, sans verdict de porte : M1 bis (CV7-6). |
| CV6-5 (écarts lecture et texte) | **fermé, avec un reste** | (a) « plus de 0,05 » (ligne 155). (b) Lecture, lignes 87 et 88 : « hors table » gardé même si r₀ ≥ 0,5. (c) Texte, ligne 249 : « médiane et troisième quartile nuls », comme la lecture. Mais la portée de la règle (24 cellules de M3 seulement, ou aussi les conformes des bras) n'est toujours pas dite (CV7-2). (d) Lignes 157 à 160 : « différences de médianes ». |
| CV6-6 (restes) | **à moitié** | Fermé : « huit issues au-dessus de α » (ligne 71) ; « +0,03 » attribué à l'essai v7 (ligne 111 ; l'essai donne D = D′ = 0,030 à r₀ = 0,201) ; garde endormie qui lève (script, lignes 328 à 334 ; vérifié : avec la garde endormie, `test_gardes` lève) ; empreintes dans la sortie des effectifs (lignes 428 à 431 ; vérifié). À moitié : la sortie du test de la lecture est déposée, mais elle a été faite sur la table v6 et retouchée à la main (CV7-4). La vérification du manifeste par la lecture est **cassée en mode réel** (CV7-1) et incomplète : ni l'empreinte du script, ni les tirages, ni le commit (CV7-5). La ligne 111 dit encore « huit issues ordonnées » pour neuf feuilles (CV7-6). |
| CV4-1 (deux définitions de M2 ter) | **fermé** | Une seule définition (Seuil, lignes 184 à 196), sans r₀ ; la colonne « réfutation » est alignée (ligne 111). |
| CV4-4 (attributions trop larges) | **fermé, reste dans CV7-3** | (i) « marges et dépendance » exige le mélange > α et bb(D′) > 0. (ii) Le mélange à pas fixé est en place et vérifié (réponse 4). (iii) « dérive » est mesurée en (4c). Le reste : (4b) et (2a), en CV7-3. |

## 2. Réponses aux points du brief

**Point 2 : M2 ter, un arbre à neuf feuilles.**
- **Partition : exhaustive et sans recouvrement.** Les « sinon » sont emboîtés sur six conditions binaires :
  - Ville réelles ≤ 0,05 ;
  - bb(D) ≤ 0 ;
  - Ville mélange > α ;
  - bb(D′) > 0 ;
  - Ville mélange à pas fixé ≤ α ;
  - bb(dérive) > 0.

  J'ai comparé `lecture_mecanique_v3.lire` à ma réécriture du Seuil faite à partir du texte seul, sur les 64 combinaisons.
  Chaque combinaison tombe dans une feuille et une seule, et les neuf feuilles sont atteintes : (1) 32 ; (2a) 8 ; (2b) 8 ;
  (3a) 4 ; (3b) 4 ; (4a) 2 ; (4b) 2 ; (4c) 2 ; (4d) 2. Il n'y a **aucun désaccord** (`sortie-verif-cv7-lecture-v1.json`).
- **Critères** : chaque feuille a sa ligne : (4a) 233, (4b) 234, (2b) 235, (3b) 236, (1) 237, (3a) 238, (4c) 239, (4d) 240,
  (2a) 244.
- **r₀** : il n'est une condition nulle part dans M2 ter (Seuil, lignes 184 à 195 ; lecture, lignes 99 à 111).
- **Attributions justifiées par la mesure** :
  - **(4c) l'est désormais.** D = D′ + dérive exactement : avec bb(D) > 0, bb(D′) ≤ 0 et bb(dérive) > 0, la structure passe
    par les marges par pas.
  - **(4d), (2b), (3a), (3b) et (4a) le sont** ; (3b) dit bien « dérive possible ».
  - **(4b) ne l'est pas tout à fait** : elle dit « dérive » sur deux valeurs ponctuelles (CV7-3).
  - **(2a) ne l'est pas tout à fait** : elle dit « la structure n'étant pas établie » sans regarder D′, qui peut l'établir
    (CV7-3).

**Point 3 : excès apparié de M4.** Le code est **inchangé depuis la v6** (le diff ne touche que D, D′, les effectifs et le
test). La contre-lecture v6 l'a vérifié en lançant ; je l'ai relu.
- **Médiane sur les sondes des différences par sonde** : script, lignes 531 et 535 (`taux_m4(bras) − taux_m4(τ = 0)` par
  sonde, puis la médiane).
- **Même calibrage** : à τ = 0, `Xe = Xcal = X`. Le bras M4 a `calibrage_sans_effet=True`, donc `Xcal = X`. Les deux termes
  ont la même permutation et les mêmes plis, donc les mêmes μ₀, σ et seuils (lignes 198 à 222).
- **Rééchantillonnage apparié** : le même `idx` sert aux deux termes (lignes 534 et 535).
- **La table calcule le même excès** : lignes 51 à 62 de la table, différence par couple monde-sonde puis médiane.
- **Le faux « confirmé » de CV4-2 est fermé.** Un défaut de niveau commun aux deux termes déplace l'excès de 0,001 à 0,002
  (contre-lecture v6, `sortie-verif-cv6-defaut-niveau-v1.json`), bien en deçà du seuil de 0,02.
- **Nouveau faux « confirmé » ou faux blocage dans l'excès** : je n'en trouve pas. Le faux « confirmé » que je trouve est
  ailleurs : il passe par la cellule à zéro et la ligne de lecture (CV7-2).

**Point 4 : mélange à pas fixé** (`sortie-verif-cv7-pas-fixe-v1.json` ; 12 sondes, E = 60, 10 mélanges, 600
rééchantillonnages appariés, deux mondes par scénario).
- **Marges par pas et masque** : gardés, par le code (lignes 156 à 165) et par le test des gardes, qui le vérifie à chaque pas
  (lignes 321 à 327).
- **Dépendance détruite** (r₀ = 0,3, sans dérive, masques dispersés) :
  - r₀ vaut 0,281 et 0,307 à l'origine, −0,001 et 0,000 sur le mélange à pas fixé ;
  - D vaut 0,047 et 0,048, D′ 0,045 et 0,047 ;
  - la dérive vaut 0,002 et 0,001, de borne basse −0,002.
- **Dérive linéaire en t, sans effet épisode** (± 1 écart type sur l'épisode, masques dispersés) :
  - le r₀ du mélange à pas fixé suit le r₀ d'origine (−0,034 contre −0,031 ; −0,030 contre −0,026), alors que le mélange
    complet donne 0,000 et −0,003 : la dérive survit au mélange à pas fixé ;
  - le r₀ centré par pas revient près de 0 (0,008 et 0,012) ;
  - « réelles − mélange à pas fixé ≈ 0 » : oui, D′ = −0,001 ;
  - « réelles − mélange complet > 0 » : **non**, D = −0,003 et −0,005. Comme la contre-lecture v6 l'avait vu, une dérive de
    la moyenne élargit les marges du mélange complet (variance poolée), et le mélange complet alerte un peu **plus** que
    les réelles ;
  - Ville reste sous α partout (0 à 0,005) : feuille (1).
  - Ce n'est pas un défaut du mélange. Mais cela confirme qu'une dérive de moyenne ne produit pas le D > 0 de (4c) ; elle
    produit plutôt un D **abaissé** (CV7-3, (2a)).
- **Effet épisode lié à la longueur, masques en préfixe** (r₀ ≈ 0,3) : je craignais que le mélange à pas fixé garde la part
  de dépendance portée par les pas valides. Ce n'est pas le cas : D ≈ D′ (0,030 et 0,030 ; 0,071 et 0,070), dérive ≈ 0, r₀
  du mélange à pas fixé ≈ 0. En revanche, le r₀ **centré par pas** tombe de 0,30 à 0,24, soit un écart de 0,055 sans aucune
  dérive : la réserve de la ligne 155 se déclencherait en disant « dérive » (CV7-6).

**Point 5 : gardes.**
- **`--test-gardes`** sort **quinze entrées**, soit quatorze gardes et `correlation_saine` = 0,171
  (`sortie-test-gardes-v7.json`).
- **Garde endormie** : avec `verifier_scores_invalides` remplacée par une fonction vide, `test_gardes` **lève**
  (« garde endormie : un score porté par une action invalide est passé (R5) », `sortie-verif-cv7-garde-endormie-v1.json`).
  CV6-6 est fermé.
- **`verifier_scores_invalides` sur le chemin réel** : elle est appelée en tête de `un_passage` (ligne 196), donc à chaque
  passage. Le code est inchangé depuis la v6, où 705 appels ont été comptés pendant un `main()` réel.
- **Refus vérifiés en lançant** (`sortie-refus-mode-reel-v7.txt`) :
  - `--effectifs-seulement` sans empreinte, avec une empreinte vide ou avec une empreinte fausse ;
  - `--tirages 5` et `--bootstrap 300`, avec et sans `--effectifs-seulement` ;
  - l'absence de `--commit` (ou un commit vide), de `--sondes-reelles` ou de `--sondes-placebo` ;
  - le mode réel sans empreinte ;
  - des effectifs faux (4 réelles ; 1 placebo) ;
  - `--reel` avec `--synthetique` ;
  - E = 40.
- **Passent** : les défauts écrits explicitement. La sortie des effectifs donne E = 60, K = 39 dans les dix plis,
  L = 0,05000000000000001, plus les **empreintes des données et du script** (`463f910d…`, celle du fichier sur disque) et le
  nom du script (`sortie-effectifs-synthetique-v7.json`).

**Point 6 : chiffres cités.** Tous ceux que j'ai recalculés sont conformes :
- 0,395 ; 0,0725 et 0,077 ; 2/40 ; K = 39, rang 38 ;
- table v7 :
  - Ville à τ = 0 : 0 ; 0,033 ; 0,083 ; 0,133 ;
  - Ville à τ = 2 : 0,1375 à 0,1521 ;
  - M2 bis : +0,138 ; +0,104 ; +0,065 ; +0,019 ;
  - excès : 0,143 ; 0,073 ; 0,027 ; 0,006 ;
  - quantité brute : 0,194 ; 0,124 ; 0,075 ; 0,0545 ;
  - maximum : 0,019 à 0,026, soit 0,38 à 0,53 L ;
- essai v7 : D = D′ = 0,030 à r₀ = 0,201 ; descriptif 0,23 à 0,27 ; mélanges conformes 0,047 à 0,052 ; par action 0,083 ;
- contre-lecture v3 : 0,005 ; 0,016 ; 0,041 (son rapport, lignes 181 et 244) ;
- contre-lecture v4 : 340 mondes, faux « fragile » 0 à 8 % (son rapport, lignes 87 à 89) ;
- docstring de `bases/sequentiel.py`, lignes 7 et 8.

Les empreintes de l'en-tête correspondent aux fichiers. Les compagnons existent, sauf ceux du préenregistrement (normal) et
du script de séquence (CV7-5).

**Point 7 : ce que je n'avais pas vu venir.**
- **La lecture n'a jamais été essayée sur une sortie du mode réel** (CV7-1). L'essai déposé est une sortie synthétique, dont
  le manifeste porte `E` ; la sortie réelle ne le porte pas. Le même défaut atteint `rediger_note_lecture_v1.py`
  (ligne 79 : `m.get('E')` imprimerait « E = None »).
- **Une cellule conforme à zéro laisse passer la première ligne** (CV7-2). J'ai pris l'essai v7 et posé une cellule de M3 à
  médiane et troisième quartile nuls. M3 devient « tenu, fragile sur 1 cellule (la lecture continue) », la cellule à zéro dit
  « trop propre », et la ligne reste « première ligne : la synthèse a raison … — proposé à Lazar pour G1 et H2 ».
- Hors de ces deux points, la lecture applique **exactement** le Seuil :
  - M1 ; contrôle M2 ; M2 bis avec « hors table » à tout r₀ ;
  - M2 ter à neuf feuilles ;
  - M3 avec L et B du manifeste ;
  - M4 en excès, avec audit du maximum avant le r₀ ;
  - placebo sur 24 cellules plus le maximum de M4 ;
  - ligne de lecture.

  Elle n'ajoute rien d'autre. Sur la sortie de mon mode réel synthétique, une fois `E` ajouté à la main, elle lit : M1
  confirmé, M2 ter (4a), M3 tenu, M4 confirmé, placebo sans écart, et la première ligne.

## 3. Constats

### CV7-1 : la lecture mécanique v3 refuse toute sortie du mode réel (bloquant)

- **Où** :
  - `lecture_mecanique_v3.py`, lignes 53 et 54 : `int(table_manifeste.get("E", -1)) != int(m.get("E", -2))` → `SystemExit` ;
  - `analyse_fausses_alertes_v7.py`, lignes 281 à 283 et 434 à 441 : en mode réel, `meta` porte `episodes_honnetes`,
    `gardes` et `actions_valides_par_episode`, mais **pas** `E`. Seul le mode synthétique en porte un (ligne 298) ;
  - `commandes-lecture-reelle-v7.sh`, ligne 37 (étape 3), sous `set -euo pipefail` ;
  - texte, lignes 31 et 32 : la lecture « vérifie … E égal à celui de la table ».
- **Problème** :
  - Mode réel lancé sur mon fichier synthétique (3 réelles, 2 placebo, 20 tirages, 2 000 rééchantillonnages), puis lecture
    v3 avec `--empreinte-donnees` : « E de la table (60) ≠ E de la sortie (None) », code 1, aucune sortie
    (`sortie-lecture-v3-sur-mode-reel-synthetique-v7.err`, `sortie-verif-cv7-lecture-v1.json`, `mode_reel_sur_synthetique`).
  - Le refus ne dépend pas des données : **toute** exécution réelle le déclenche, que E vaille 60 ou non.
  - Dans la séquence gelée, l'étape (2) a déjà produit et scellé `sortie-reelle-v7.json`, et la ligne 17 interdit de la
    relancer. Réparer la lecture après coup, c'est la modifier **après** que la sortie réelle existe : une version nouvelle
    de l'outil de lecture, écrite avec les données en main, et un écart au préenregistrement scellé (nœud de décision).
    C'est exactement ce que R1 veut éviter.
  - L'essai déposé ne pouvait pas le voir : il a été fait sur une sortie synthétique.
- **Correction** :
  - (a) Option légère, qui ne touche que la lecture (v4) : comparer le E de la table à `m["gardes"]` en mode réel et à
    `m["E"]` en mode synthétique, et refuser si les deux manquent. Le script v7, la table v7 et l'essai v7 restent tels
    quels.
  - (b) Autre option : ajouter `"E": E` au manifeste du script dans les deux modes. Le script deviendrait v8, et l'essai et
    la table seraient à refaire.
  - Je recommande (a), avec la même correction dans `rediger_note_lecture_v1.py`.
  - Surtout, faire une **répétition générale** de toute la séquence avant le scellement : `commandes-lecture-reelle` avec un
    `.npz` synthétique écrit par `ecrire_npz_synthetique`, dans un dossier jetable, avec 3 réelles et 2 placebo. Déposer
    ses sorties avec leurs compagnons. Elle aurait vu ce défaut, et elle verra tout défaut de même famille (noms de clés,
    chemins, scellements).

### CV7-2 : une cellule « trop propre » n'atteint pas la ligne de lecture (moyen : faux « confirmé » possible ; reste de CV6-1 et CV6-5 (c))

- **Où** :
  - lecture v3, lignes 161 à 163 : le verdict `cellule_a_zero` est calculé, mais il n'entre ni dans `audits` ni dans
    `reserves` (lignes 165 à 178) ;
  - texte : Seuil, lignes 196 à 198, où la liste des audits ne comprend pas la cellule à zéro ; critères, ligne 249, sans
    portée dite.
- **Problème** :
  - Une cellule à zéro, c'est un seuil infini ou des alertes non comptées. Ce défaut rend aussi M3 « fragile » (médiane
    < 0,4 L), et « fragile » laisse la lecture continuer.
  - Vérifié en lançant sur l'essai v7, avec une cellule de M3 à médiane et troisième quartile nuls
    (`sortie-verif-cv7-lecture-v1.json`, `cellule_a_zero_tau0_somme_terminale`) :
    - M3 : « tenu, fragile sur 1 cellule(s) (la lecture continue) » ;
    - cellule à zéro : « trop propre » ;
    - ligne : « première ligne : la synthèse a raison … — proposé à Lazar pour G1 et H2 ».
  - R4 dit : « un résultat suspect de propreté … déclenche le même audit ». La note de lecture met la ligne en gras.
  - La correction de CV6-1 demandait de porter cette réserve sur la ligne ; elle n'y est pas.
  - La règle ne couvre que les 24 cellules de M3. Un maximum du bras M4 à zéro (posé à la main) passe sans rien dire, alors
    qu'il est attendu vers 0,02. La portée demandée en CV6-5 (c) n'est pas écrite.
- **Correction** :
  - Texte, Seuil : ajouter la cellule à zéro à la liste des audits qui suspendent la lecture. C'est ce que R4 demande, et la
    ligne 249 pose déjà les questions d'un audit. Le minimum serait une réserve portée sur la ligne.
  - Écrire la portée : toutes les cellules conformes de la sortie (24 de M3, conformes du bras M4, des deux mélanges et du
    descriptif).
  - Lecture : `zeros` non vide → « AUDIT » (ou réserve ajoutée à `ligne`) ; étendre la boucle aux blocs des bras ; tester et
    déposer.

### CV7-3 : deux attributions de M2 ter dépassent encore la mesure (mineur ; reste de CV6-2 et CV4-4)

- **(4b) « dérive et dépendance »** (Seuil, ligne 193 ; critères, ligne 234 : « la dérive avec le pas pousse déjà Ville
  au-dessus de α »).
  - Elle se lit sur deux valeurs ponctuelles, mélange à pas fixé > α ≥ mélange, sans regarder bb(dérive). Le texte pose
    pourtant, à la ligne 195, qu'« on n'écrit « dérive » que si elle est mesurée ».
  - Correction : (4b) devient « dépendance établie, non suffisante seule (mélange à pas fixé > α) ». On ajoute « dérive
    mesurée » seulement si bb(dérive) > 0, ce qui reste rapporté sans nouvelle feuille.
- **(2a) « marges seules »** (Seuil, ligne 188 ; critères, ligne 244 : « la structure n'étant pas établie »).
  - La branche (2) se lit sur bb(D) ≤ 0 seul. Or D = D′ + dérive, et une dérive de moyenne rend la dérive **négative** : le
    mélange complet alerte plus que le mélange à pas fixé (réponse 4). On peut donc avoir bb(D) ≤ 0 < bb(D′), c'est-à-dire
    une dépendance établie par D′, et lire « marges seules … structure non établie ».
  - La fenêtre est étroite (quelques millièmes dans mes simulations), et il faut en plus Ville réelles > α. C'est donc
    improbable.
  - Correction, en une phrase et sans nouvelle feuille : (2a) exige aussi bb(D′) ≤ 0, sinon (2b) « non attribuable »,
    rapportée avec D et D′.

### CV7-4 : l'essai déposé de la lecture n'est pas une sortie brute, et il porte sur la table v6 (mineur ; reste de CV6-1 et CV6-6)

- **Où** : `essai-lecture-mecanique-v3-sur-synthetique-v7.json`, bloc `sources` ; texte, lignes 30 et 31.
- **Problème** :
  - Le bloc `sources` n'est pas celui qu'écrit `main()` (lignes 197 et 198 : `sortie`, `table`, `script_sortie`,
    `commit_sortie`, `synthetique`). Il porte du texte écrit à la main : `"table": "table-m2bis-m4-v6.json (mêmes chiffres
    que la v7)"`, une liste `feuilles_exercees` et une `note`.
  - La lecture a donc été lancée avec la table **v6**, alors que le texte dit « testée sur l'essai synthétique v7 ». Le
    fichier n'est pas une sortie reproductible de l'outil.
  - Les neuf feuilles « exercées » et les cas d'audit (placebo, maximum de M4) n'ont aucune sortie déposée. Or CV6-1 demandait
    de « déposer la sortie du test ».
  - Aucun essai sur une sortie du mode réel (CV7-1).
- **Correction** : déposer la sortie **brute** de `lecture_mecanique_v4.py <essai v7> table-m2bis-m4-v7.json`, plus une sortie
  du test des feuilles et des audits, plus la répétition générale de CV7-1, chacune avec son compagnon.

### CV7-5 : vérification du manifeste incomplète, et script de séquence hors du texte (mineur ; reste de CV6-6, R6)

- **Manifeste** (lecture, lignes 47 à 56). Seuls le nom du script, l'empreinte des données (si `--empreinte-donnees` est
  donné) et E sont vérifiés.
  - J'ai posé sur l'essai une empreinte de script nulle, 1 tirage, 10 rééchantillonnages et aucun commit : la lecture
    **passe** (`manifeste_non_verifie`).
  - Le mode réel refuse déjà d'autres tirages, et la commande (3) passe l'empreinte des données : le risque est faible.
    CV6-6 demandait pourtant aussi l'empreinte du script (`463f910d…`), 20 tirages, 2 000 rééchantillonnages et un commit
    non vide.
  - Correction : les ajouter à la garde, et la tester sur un cas sain et sur un artefact.
- **Script de séquence**. `commandes-lecture-reelle-v7.sh` (`6679d908…`) n'a pas de compagnon `.sha256`. Le texte ne le cite
  pas (le Plan d'analyse, lignes 212 à 224, décrit les commandes sans renvoyer au fichier). Son étape 0 vérifie les compagnons
  du script, de la table et de la lecture, mais pas le sien.
  - Correction : le citer avec son empreinte dans le Plan d'analyse, créer son compagnon, et l'ajouter à la ligne 18.
  - Même remarque pour `rediger_note_lecture_v1.py`, si la note de lecture doit en dépendre.

### CV7-6 : restes (mineur)

- **Prédictions, M2 ter** (ligne 111) : « l'issue est celle du Seuil (huit issues ordonnées) ». L'arbre a neuf feuilles,
  dont huit au-dessus de α. Écrire « neuf issues ordonnées ». Le commentaire de la lecture, ligne 89, dit encore « cinq issues
  ordonnées ».
- **M2 bis** (ligne 113) : « réfutation seulement si r₀ < 0,5 », mais aucun critère de réfutation n'est défini pour
  r₀ < 0,5. Le Seuil (lignes 178 et 179) ne donne que « conforme » ou « hors table », et la colonne « signe » dit « > 0 ».
  Écrire soit « “hors table” ou différence ≤ 0 vaut réfutation si r₀ < 0,5 », soit « aucune réfutation, rapporté ».
- **Réserve sur r₀** (lignes 153 à 156 ; lecture, lignes 66 à 68) : un effet épisode lié à la longueur, sous masques en
  préfixe, abaisse aussi le r₀ centré par pas (0,30 → 0,24 dans ma simulation, sans aucune dérive). Écrire « une dérive avec
  le pas, ou un effet épisode lié aux pas valides, pèse sur r₀ ».
- **M1 bis** (lecture, lignes 76 et 77) : la monotonie se teste sans arrondi. Deux médianes rationnellement égales mais
  différentes en flottant peuvent donner « croissant », qui est sa réfutation. Arrondir la suite à 10⁻⁹ comme le reste.
  C'est sans verdict de porte.

## 4. Mes scripts et sorties (dans ce dossier, chacun avec un compagnon `.sha256`)

| fichier | contenu |
|---|---|
| `verif_cv7_v1.py` | parties `lecture` (arbre sur 64 combinaisons et bornes exactes ; quatre audits ; cellule à zéro dans M3 et dans le bras M4 ; sortie du mode réel ; manifeste non vérifié), `pas_fixe` (dérive linéaire, bosse précoce, dépendance, effet lié à la longueur), `garde_endormie` ; script v7 et lecture v3 importés sans modification ; graines `SeedSequence(2810202607, spawn_key=(2, scénario, monde))` |
| `sortie-verif-cv7-lecture-v1.json`, `sortie-verif-cv7-pas-fixe-v1.json`, `sortie-verif-cv7-garde-endormie-v1.json` | leurs sorties |
| `refus_mode_reel_cv7_v1.sh`, `sortie-refus-mode-reel-v7.txt`, `sortie-effectifs-synthetique-v7.json` | refus du mode réel et effectifs, vérifiés en lançant |
| `sortie-test-gardes-v7.json` | `--test-gardes` (15 entrées) |
| `sortie-mode-reel-sur-synthetique-v7.json`, `sortie-lecture-v3-sur-mode-reel-synthetique-v7.err` | mode réel sur mon fichier synthétique (3 + 2 sondes, 20 tirages, 2 000 rééchantillonnages, commit `contre-lecture-v7-essai`) ; refus de la lecture v3 (CV7-1) |
| `sortie-synthetique-reproduite-v7.json` | essai reproduit (`5b1bc63b…`, à l'octet près) |
| `table-m2bis-m4-v7-reproduite.json` | table reproduite (`4e6fe7e1…`, à l'octet près ; environ 570 s, de 01:59 à 02:08:58 UTC) |
| `gardes-cv7/scores-synthetique-gardes.npz` (`b631b790…`), `gardes-cv7/scores-synthetique-petit.npz` (`21a88497…`) | fichiers synthétiques écrits par le test des gardes (`gardes-cv7-endormie/` : ceux du test avec la garde endormie) |
| `sortie-lecture-v3-sur-mode-reel-synthetique-v7.json` | sortie de la lecture v3 refusée : vide (0 octet) |
| `journal-fond.txt` | heures de fin des tâches lancées en arrière-plan |

Interpréteur `/opt/venv-essaim-sim-v1/bin/python -I -B`, numpy 2.5.4, tout lancé depuis le dossier du préenregistrement.

Empreinte de ce rapport : dans `rapport-contre-lecture-mesure-unanime-v7.md.sha256`, à côté (un fichier ne peut pas contenir
sa propre empreinte).

Fin : 2026-10-28 02:09:41 UTC (`date -u`, relevé dans un appel séparé avant l'écriture de cette ligne).
