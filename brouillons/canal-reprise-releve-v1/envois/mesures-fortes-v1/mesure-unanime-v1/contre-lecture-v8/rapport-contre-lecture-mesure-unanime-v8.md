# Contre-lecture (R2) : préenregistrement « mesure unanime » v8, son script, sa table, son essai, la lecture mécanique v4, la rédaction v2, le script de séquence v8 et la répétition générale

**Verdict : à corriger en v9.** La logique tient : la répétition générale **se rejoue** à l'identique, la séquence va au bout,
la branche E ≠ 60 comprise, et l'arbre de M2 ter comme l'excès de M4 sont justes. Je ne trouve aucun faux « confirmé » sur M1
ni sur M4. Deux constats moyens restent, à corriger avant le scellement :
- **CV8-1, durée de l'exécution réelle.** Avec 430 sondes, l'étape (2) prend environ **30 minutes de processeur**, et la table
  environ 10 minutes de plus si E ≠ 60. Ni le texte ni la séquence ne le disent, et la répétition (5 sondes, 32 secondes) ne
  pouvait pas le voir. Un lancement interrompu laisse un `sortie-reelle-v8.json` **vide**. La garde de la séquence refuse
  alors toute relance, et l'unique exécution serait perdue.
- **CV8-2, étiquette de la feuille (4b).** La lecture mécanique écrit encore « (4b) dérive et dépendance », alors que le Seuil
  v8 interdit ce mot tant que la dérive n'est pas mesurée. CV7-3 n'est fermé que dans le texte.

Le reste est mineur (CV8-3 à CV8-6).

Vérifié en lançant, et conforme :
- **La répétition, rejouée** depuis une copie du dossier :
  - les effectifs et la lecture sont identiques à l'octet ;
  - la sortie est identique au champ `donnees` près (le chemin du fichier) ;
  - la note régénérée ne diffère que par sa ligne de provenance.
- **La branche E ≠ 60**, que la répétition n'exerce pas : sur mon fichier au format réel où E = 52, la table est refaite au E
  et aux longueurs observés, puis scellée et lue ; la séquence va au bout (code 0).
- **L'étape 0** (préenregistrement scellé), exercée sur une copie scellée, et la **garde R12** de la séquence.
- **Les reproductions à l'octet** : l'essai synthétique v8, la **table v8** et l'essai déposé de la lecture.
- **L'arbre de M2 ter**, sur 64 combinaisons et aux bornes : aucun désaccord de feuille.
- **Les audits** : les cinq suspendent la ligne. La cellule de M3 à zéro ne fait **aucun** faux audit sous le nul (0 sur 300
  mondes, même avec des sondes identiques).
- **Les refus** : ceux du manifeste sur une sortie au format réel, et tous ceux du mode réel.
- **Les gardes** : quinze entrées ; 705 appels de `verifier_scores_invalides` pendant un `main()` réel.
- **Toutes les empreintes**.

- Contre-lecteur : sous-agent neuf Opus 5.5. Je n'ai écrit ni le préenregistrement, ni le script, ni la table, ni la lecture,
  ni la rédaction, ni la séquence, ni aucun des rapports précédents.
- Début : 2026-10-28 02:25:42 UTC (`date -u`). Fin : dernière ligne. Les heures d'`ls` sont à l'heure de Paris (UTC + 1).
- Processeur seul. Je n'ai ouvert, chargé ni empreinté aucun fichier de `donnees/` : l'empreinte `968414fc…` n'est donc **pas**
  vérifiée par moi.
- `commandes-lecture-reelle-v8.sh` n'a été lancé qu'en mode `REPETITION`, depuis deux copies du dossier placées dans mon
  dossier de travail (`copie-dossier/`, `copie-dossier-E52/`), jamais avec un commit. De l'étape 0 du mode réel, je n'ai lancé
  que la ligne Python, sur une copie scellée du préenregistrement (`etape0/`).
- Je n'ai modifié aucun fichier du dépôt et je n'ai fait aucun commit.
- Interpréteur : `/opt/venv-essaim-sim-v1/bin/python -I -B`, numpy 2.5.4. Mes vérifications importent le script v8 et la
  lecture v4 **sans modification**, depuis la copie. La seule enveloppe posée l'est sur un nom du module (un compteur
  d'appels), jamais sur le fichier.

## Empreintes lues

| fichier | empreinte | état |
|---|---|---|
| `preenregistrement-mesure-unanime-v8.md` | `92c208af6a4806997fd9218d0ae024a125b0da08e604e86afde170dd12958c1d` | objet ; identique dans `HEAD` (`45c3547f`) ; `prereg.problemes` = [] ; pas de compagnon (normal : il est créé au scellement) ; aucun « ⟨…⟩ » |
| `preenregistrement-mesure-unanime-v7.md` | `54bb2892…c070a` | conforme à l'en-tête |
| `analyse_fausses_alertes_v8.py` | `52b1760a…5400` | conforme ; compagnon conforme ; identique dans `3dacb461`, le commit cité |
| `sortie-synthetique-essai-v8.json` | `f83456be…fe62` | conforme ; compagnon conforme ; **reproduit à l'octet près** (79 s) |
| `table_m2bis_m4_v8.py` | `7e512516…e0d3` | conforme ; compagnon conforme ; ne diffère de la v7 que par le nom et le numéro de version |
| `table-m2bis-m4-v8.json` | `f63faada…b120` | conforme ; compagnon conforme ; **reproduite à l'octet près** (13 min 20 s, machine chargée) |
| `lecture_mecanique_v4.py` | `1d070ea8…b61a` | conforme ; compagnon conforme |
| `essai_lecture_mecanique_v4.py` → `essai-lecture-mecanique-v4.json` | `7ffb3af2…5ff4` → `e60dab70…2c00` | conformes ; compagnons conformes ; sortie **reproduite à l'octet près** |
| `commandes-lecture-reelle-v8.sh` | `f75579f4…f781` | conforme ; compagnon conforme |
| `rediger_note_lecture_v2.py` | `818761e3…d8e3` | conforme ; compagnon conforme |
| `synthetique-format-reel-repetition.npz` | `447dc136…b709` | compagnon conforme ; tableaux **identiques** à ceux qu'écrit `ecrire_npz_synthetique` avec la graine `(9, 9)` (l'empreinte du zip dépend de l'heure d'écriture) |
| `effectifs-reel-v8-repetition.json` | `c05aa6fa…3f1b` | compagnon conforme ; **rejoué à l'octet près** |
| `sortie-reelle-v8-repetition.json` | `d36a7508…5865` | compagnon conforme ; rejouée (`9ca9971f…`) : **égale hors du champ `donnees`** |
| `lecture-mecanique-reelle-v8-repetition.json` | `bde7667a…aefe` | compagnon conforme ; **rejouée à l'octet près** |
| `note-lecture-repetition-generale-v8.md` | `a539c2c5…dc20` | compagnon conforme ; régénérée : seule la ligne de provenance diffère (CV8-5) |
| `contre-lecture-v7/rapport-…-v7.md` | `7783ab01…94dd6` | conforme ; les quinze compagnons du dossier sont conformes |
| `src/controle_ia/bases/sequentiel.py` | `35a09834…11ba8` | conforme |

## 1. Fermeture de CV7-1 à CV7-6 (et des restes de CV4-1, CV4-4)

| constat | état | où et pourquoi |
|---|---|---|
| CV7-1 (bloquant : la lecture refusait toute sortie réelle) | **fermé** | Script, ligne 450 : `"E": E` est écrit après `**meta`, dans les deux modes. Lecture v4, lignes 62 et 63 : E de la table comparé à `m["E"]`. Répétition déposée, et **rejouée par moi** à l'identique. J'ai exercé ce que la répétition ne couvre pas : la branche E ≠ 60 (E = 52 : table refaite, scellée, lue ; code 0), l'étape 0 (refus sans compagnon, passage après scellement d'une copie) et la garde R12 (code 3 si la sortie existe). Restent CV8-1 (durée) et CV8-5 (rédaction hors de la séquence). |
| CV7-2 (cellule « trop propre ») | **fermé** | Seuil, lignes 190 à 192 et 211 à 212 ; critères, lignes 267 et 268 ; lecture, lignes 176, 177 et 187 (audit), 178 à 185 (bras : réserve portée sur la ligne). Vérifié sur la sortie au format réel (`cellule_M3_a_zero` → « AUDIT R4 » ; `cellule_bras_a_zero` → réserve, pas d'audit). Sous le nul, aucun faux audit : 0 sur 300 mondes, à r₀ = 0 et à 0,3, même avec des sondes **identiques**. L'épisode en tête du classement dépasse presque toujours le seuil conforme calculé sans lui. |
| CV7-3 ((4b) et (2a) dépassent la mesure) | **à moitié** | Texte : (4b) renommée (lignes 207 et 208 ; critère, ligne 252). Mais la lecture, ligne 122, écrit toujours « (4b) dérive et dépendance » (CV8-2). (2a) : la v8 retient « D′ rapportée » (ligne 201) plutôt que la condition proposée. Or le critère de la ligne 262 dit encore « la structure n'étant pas établie », et la lecture ne pose aucune réserve quand bb(D′) > 0 (vérifié, CV8-4). |
| CV7-4 (essai de la lecture non brut) | **fermé** | `essai_lecture_mecanique_v4.py` est déposé et sa sortie est reproduite à l'octet, sur l'essai v8 et la table v8. Elle couvre les neuf feuilles, les cinq audits, la réserve des bras, la borne 0,02, la réfutation de M2 bis et trois refus. Reste mineur : les refus propres au mode réel n'ont pas d'artefact déposé (CV8-6). |
| CV7-5 (manifeste ; séquence hors du texte) | **à moitié** | Lecture, lignes 53 à 59 : empreinte du script, tirages, rééchantillonnages et commit sont vérifiés. Le cas sain passe et dix artefacts sont refusés sur la sortie au format réel (`refus_manifeste_format_reel`). La séquence est citée avec son empreinte (ligne 40) et son compagnon existe. Mais sa ligne 27 ne vérifie ni son propre compagnon (correction demandée en CV7-5) ni celui de la rédaction. Et elle ne lance pas la rédaction, que le texte place dans la séquence (CV8-5). |
| CV7-6 (restes) | **à moitié** | Fermés : « neuf feuilles » (ligne 81) ; la réserve sur r₀ dit « ou un effet épisode lié à la longueur » (ligne 165 ; lecture, lignes 77 à 79) ; M1 bis arrondi (lecture, lignes 87 et 88) ; réfutation de M2 bis au Seuil (ligne 189). Ouverts : la ligne 121 dit encore « huit issues ordonnées » ; la colonne « réfutation » de M2 bis (ligne 123) ne donne pas le critère du Seuil ; le commentaire de la lecture (ligne 103) dit « cinq issues ordonnées » (CV8-6). |
| CV4-1 (deux définitions de M2 ter) | **fermé** | Une seule définition (lignes 197 à 210), sans r₀. |
| CV4-4 (attributions trop larges) | **fermé, reste d'étiquettes** | Mélange à pas fixé vérifié (réponse 4) ; « dérive » mesurée en (4c). Le reste porte sur les étiquettes de (4b) et (2a) (CV8-2, CV8-4). |

## 2. Réponses aux points du brief

**Répétition générale.** Je l'ai rejouée avec `bash commandes-lecture-reelle-v8.sh REPETITION <copie du npz> 447dc136… 3 2`,
depuis `copie-dossier/` : 32 secondes, code 0.
- `effectifs-reel-v8-repetition.json` et `lecture-mecanique-reelle-v8-repetition.json` sont identiques à l'octet aux fichiers
  déposés.
- `sortie-reelle-v8-repetition.json` est identique en tout, sauf `manifeste.donnees`, le chemin du fichier lu.
- Rejouée sur les sorties rejouées, la rédaction v2 ne diffère de la note déposée que par la ligne 3 (provenance).
- **Va-t-elle au bout en mode réel ?** Oui, sur le plan logique :
  - la branche E ≠ 60 va au bout (E = 52, L = 0,0305, K = 31 ou 32 selon les plis) ;
  - l'étape 0 passe sur un préenregistrement scellé ;
  - la garde R12 refuse une seconde exécution ;
  - les noms de clés, les chemins et les scellements sont justes.

  En pratique, c'est **sous condition de durée** (CV8-1).

**Point 2 : M2 ter, un arbre à neuf feuilles.**
- **Partition : exhaustive et sans recouvrement**, par construction. Les « sinon » sont emboîtés sur six conditions binaires :
  - Ville réelles ≤ 0,05 ;
  - bb(D) ≤ 0 ;
  - Ville mélange > α ;
  - bb(D′) > 0 ;
  - Ville pas fixé ≤ α ;
  - bb(dérive) > 0.
- J'ai comparé `lecture_mecanique_v4.lire` à ma réécriture du Seuil, faite sur le texte seul, sur les 64 combinaisons, avec
  pour base la sortie **au format réel** de la répétition :
  - les neuf feuilles sont atteintes : (1) 32 ; (2a) 8 ; (2b) 8 ; (3a) 4 ; (3b) 4 ; (4a) à (4d) 2 chacune ;
  - il n'y a **aucun désaccord de feuille** ;
  - il y a **deux désaccords d'étiquette**, tous deux sur (4b) (CV8-2).
- **Bornes** : 0,05 et 0,05 + 10⁻¹⁷, bornes basses à 0 et à ± 3 × 10⁻¹⁸, mélange à 0,05 : tout tombe du côté du texte
  (`sortie-verif-cv8-lecture-v1.json`).
- **Critères** : chaque feuille a sa ligne : (4a) 251, (4b) 252, (2b) 253, (3b) 254, (1) 255, (3a) 256, (4c) 257, (4d) 258,
  (2a) 262.
- **r₀** n'est une condition nulle part dans M2 ter.
- **Attributions** :
  - (4c) est justifiée : D = D′ + dérive **exactement**, pour la valeur ponctuelle comme pour chaque tirage, puisque les trois
    termes sont des différences des mêmes médianes sur le même tirage (script, lignes 557 à 560) ;
  - (1), (2b), (3a), (3b), (4a) et (4d) sont justifiées ;
  - (4b) l'est dans le texte, pas dans la lecture (CV8-2) ;
  - (2a) ne l'est pas tout à fait quand bb(D′) > 0 (CV8-4).

**Point 3 : excès apparié de M4.** Le code est **inchangé depuis la v6** : le diff de la v7 à la v8 ne touche que la ligne
de commande, le nom du script et `"E"`.
- Médiane sur les sondes des différences par sonde : lignes 541 et 545.
- Même calibrage :
  - à τ = 0, `Xe = Xcal = X` ;
  - le bras a `calibrage_sans_effet=True`, donc `Xcal = X` ;
  - la permutation et les plis sont les mêmes ;
  - donc μ₀, σ et les seuils sont les mêmes.
- Rééchantillonnage apparié : le même `idx` sert aux deux termes (lignes 544 et 545).
- La table calcule le même excès (lignes 48 à 62 : `s4 − s0` par couple monde-sonde, puis la médiane). Elle est reproduite à
  l'octet.
- Le faux « confirmé » de CV4-2 est fermé par construction : un défaut de niveau commun aux deux termes s'annule sonde par
  sonde. La contre-lecture v6 l'a mesuré à 0,001 ou 0,002, bien en deçà de 0,02.
- Je ne trouve aucun nouveau faux « confirmé » ni aucun faux blocage **dans M4**. Le maximum vaut environ 0,02 et l'audit se
  déclenche au-dessus de 0,10. Le seul chemin que je trouve vers une première ligne discutable passe par M2 bis (CV8-3).

**Point 4 : mélange à pas fixé** (`sortie-verif-cv8-pas-fixe-v1.json` ; 12 sondes, E = 60, 5 mélanges par sonde, masques
dispersés).
- Les marges par pas et le masque sont gardés : je l'ai vérifié à chaque pas et à chaque mélange, et le test des gardes le
  vérifie aussi.
- **Dérive linéaire en t, sans effet épisode** :
  - r₀ vaut 0,024 à l'origine (les masques dispersés font de la dérive un léger effet épisode), 0,016 sur le pas fixé et
    0,001 sur le mélange : la dérive survit au mélange à pas fixé, pas au mélange complet ;
  - Ville vaut 0 sur les réelles, 0,003 sur le mélange et 0,003 sur le pas fixé ;
  - D = D′ = −0,003 : « réelles moins pas fixé ≈ 0 » tient ; « réelles moins mélange complet > 0 » ne tient pas, comme les
    contre-lectures v6 et v7 l'avaient vu (une dérive de moyenne élargit les marges poolées du mélange complet).
- **Dépendance r₀ = 0,3, sans dérive** :
  - r₀ vaut 0,305 à l'origine, 0,000 sur le pas fixé et −0,003 sur le mélange : la dépendance est détruite ;
  - D vaut 0,047 et D′ 0,045.

**Point 5 : gardes.**
- `--test-gardes` sort **quinze entrées**, soit quatorze gardes et `correlation_saine` = 0,171 (`sortie-refus-mode-reel-v8.txt`,
  à la fin).
- `verifier_scores_invalides` est appelée **705 fois** pendant un `main()` réel sur le fichier de la répétition, soit 5 sondes ×
  141 passages (`sortie-verif-cv8-gardes-v1.json`). Elle est donc bien sur le chemin réel (ligne 199).
- Le mode réel refuse, vérifié en lançant (`sortie-refus-mode-reel-v8.txt`) :
  - `--effectifs-seulement` sans empreinte, avec une empreinte vide ou avec une empreinte fausse ;
  - `--tirages 5` et `--bootstrap 300`, avec et sans `--effectifs-seulement` ;
  - l'absence de `--commit` (ou un commit vide), de `--sondes-reelles` ou de `--sondes-placebo` ;
  - des effectifs faux ;
  - `--reel` avec `--synthetique`.
- Le cas sain passe.

**Point 6 : chiffres cités.** Tous ceux que j'ai recalculés sont conformes :
- 0,395 ; 0,0725 ; 0,077 ; 2/40 ; K = 39 ; rang 38 ;
- table v8, reproduite :
  - Ville à τ = 0 : 0 ; 0,033 ; 0,083 ; 0,133 ;
  - Ville à τ = 2 : 0,1375 à 0,1521 ;
  - M2 bis : +0,138 ; +0,104 ; +0,065 ; +0,019 ;
  - excès : 0,143 ; 0,073 ; 0,027 ; 0,006 ;
  - quantité brute : 0,194 ; 0,124 ; 0,075 ; 0,0545 ;
  - maximum : 0,019 à 0,026 ;
- essai v8, reproduit : D = D′ = 0,030 à r₀ = 0,201 ; descriptif 0,23 à 0,27 ; mélanges conformes 0,047 à 0,052 ; par action
  0,083 ;
- en-tête : « quinze entrées » ; « cinq audits » et « trois refus » dans l'essai de la lecture ; répétition « 3 sondes
  réelles, 2 placebo, E = 60 ».

Les empreintes de l'en-tête correspondent aux fichiers. Tous les compagnons existent, sauf celui du préenregistrement (normal).
Le texte ne contient aucun « ⟨…⟩ ». Le seul espace réservé est dans la note produite par la rédaction (« ⟨À ÉCRIRE … ⟩ »), et il
est voulu.

**Point 7 : ce que je n'avais pas vu venir.**
- **La durée de l'unique exécution** (CV8-1).
- **M2 bis réfutée** laisse passer la première ligne, alors que le critère l'appelle « audit » (CV8-3).
- **Pour information, sans constat** : la granularité 1/E coûte un peu sous le nul aux six cellules de M3 à τ = 0, qui n'ont
  qu'un tirage.
  - Avec des sondes **identiques** (borne haute : la médiane vaut alors le taux d'une seule sonde), une de ces six cellules
    dépasse B = 0,10, soit 7 alertes sur 60, dans **1,7 %** des mondes à r₀ = 0 et **3,0 %** à r₀ = 0,3
    (`sortie-verif-cv8-zero-identiques-v1.json`, 300 mondes).
  - Le placebo, borné à un écart de 0,05, a la même granularité.
  - La contre-lecture v4 n'avait trouvé aucun faux audit sur 340 mondes, avec 30 sondes qui partagent la moitié de leur
    variance d'épisode (`contre-lecture-v4/verif_cv4_m3_v1.py`, ligne 2).
  - Le vrai taux se situe entre les deux, selon la corrélation des 30 sondes réelles entre elles. C'est un coût connu, pas un
    défaut de la v8. Lazar peut vouloir le savoir avant le GO.

## 3. Constats

### CV8-1 : la durée de l'exécution réelle n'est dite nulle part, et une interruption perdrait l'unique exécution (moyen)

- **Où** :
  - Plan d'analyse, lignes 227 à 242 ; Liste d'arrêt, ligne 277 ;
  - `commandes-lecture-reelle-v8.sh` :
    - ligne 25 : la garde R12 ;
    - ligne 42 : `> "sortie-reelle-v8$SUF.json"` crée le fichier avant le calcul, et `json.dump` n'écrit qu'à la fin ;
    - lignes 34 à 38 : la table si E ≠ 60.
- **Problème** :
  - Temps processeur mesuré (`duree_mode_reel_v1.py` → `sortie-duree-mode-reel-v1.txt`) : **4,2 s par sonde** pour les 141
    passages de `main()`. Pour 430 sondes, cela fait **environ 30 minutes** pour l'étape (2), plus environ 30 secondes de
    rééchantillonnages.
  - Si E ≠ 60, la table refaite demande environ 9 à 10 minutes de plus. Ma table à E = 52 a pris 12 minutes sur une machine
    chargée (`journal-heures.txt`).
  - La répétition (5 sondes, 32 secondes) ne pouvait pas le faire voir.
  - Lancée au premier plan par un agent (10 minutes au plus), ou en arrière-plan avec le délai par défaut (30 minutes), la
    séquence est arrêtée pendant l'étape (2). Il reste alors un `sortie-reelle-v8.json` **vide** : `set -e` arrête le script,
    le fichier n'est pas scellé, et aucun taux n'est lu.
  - La ligne 25 refuse ensuite toute relance (code 3), et la ligne 277 fait de toute relance une « version nouvelle ». Une
    simple coupure coûterait donc une version et un écart à dire, sans qu'aucun résultat ait été vu.
- **Correction** :
  - Dans le Plan d'analyse et en tête du script de séquence, dire la durée attendue (environ 30 minutes de processeur pour
    (2), environ 10 de plus si E ≠ 60) et la façon de lancer : en arrière-plan, avec un délai d'au moins 90 minutes.
  - Dans la séquence, écrire la sortie dans un fichier temporaire, puis le renommer en `sortie-reelle-v8.json` une fois
    `json.dump` fini. Ainsi, une exécution interrompue ne laisse pas de fichier final.
  - Dans la Liste d'arrêt, dire ce que vaut une exécution **interrompue sans sortie** : ce n'est pas une lecture, et une
    relance est permise une fois, dite dans la note. Ou bien dire explicitement le contraire.
  - Tester la nouvelle séquence en répétition.

### CV8-2 : la lecture mécanique écrit « (4b) dérive et dépendance », que le Seuil v8 interdit (moyen ; reste de CV7-3)

- **Où** :
  - `lecture_mecanique_v4.py`, ligne 122 ;
  - texte, Seuil, lignes 207 et 208 : (4b) « dépendance établie, mélange à pas fixé au-dessus de α », avec « le mot
    « dérive » n'y est écrit que si la dérive mesurée a une borne basse > 0 » ; critère, ligne 252 ;
  - traitement de CV7-3, ligne 358 : « feuille (4b) renommée sans le mot « dérive » » ;
  - `essai-lecture-mecanique-v4.json`, feuille (4b).
- **Problème** :
  - La lecture est l'outil gelé dont la note reprend le verdict « tel quel ». Si la sortie réelle tombe en (4b), la note écrira
    le mot que le texte interdit, et le nom ne correspondra à aucune ligne des critères.
  - Je l'ai vérifié : 2 désaccords d'étiquette sur 64 combinaisons, tous deux sur (4b), que bb(dérive) soit positive ou non
    (`sortie-verif-cv8-lecture-v1.json`, `arbre`).
- **Correction** : lecture v5, ligne 122 : « (4b) dépendance établie, mélange à pas fixé au-dessus de α », avec « (dérive
  mesurée) » ajouté seulement si `bbDd > 0`. Corriger le commentaire de la ligne 103 (« cinq issues »), puis refaire et
  redéposer l'essai de la lecture et la répétition.

### CV8-3 : M2 bis réfutée est un « audit » pour les critères, mais pas pour le Seuil ni pour la lecture (mineur)

- **Où** :
  - critère, ligne 269 : « → audit de cohérence, rapporté » ;
  - Seuil, lignes 211 et 212 : la liste des audits qui suspendent ne la contient pas ;
  - lecture, ligne 187 : ne la compte pas ;
  - Prédictions, ligne 123 : la colonne « réfutation » ne donne que « « hors table » si l'écart dépasse 0,05 ; rapporté » et ne
    dit pas le critère du Seuil (ligne 189).
- **Problème** :
  - Vérifié sur la sortie au format réel : M2 bis « RÉFUTÉE » avec le contrôle M2 « attendu », et la ligne reste « première
    ligne : la synthèse a raison … — proposé à Lazar pour G1 et H2 ». Aucune réserve n'est portée (`M2_bis_refutee`).
  - Le cas est improbable : il faut Ville à τ = 0 au moins égale à Ville à τ = 2 ≥ 0,075, avec r₀ < 0,5. Mais le texte se
    contredit sur sa portée.
- **Correction** : choisir.
  - Soit M2 bis réfutée entre dans la liste des audits qui suspendent (Seuil, ligne 212 ; lecture, ligne 187).
  - Soit la ligne 269 dit « réserve de cohérence » et la lecture la porte sur la ligne (`reserves`).
  - Dans les deux cas, la colonne « réfutation » de la ligne 123 reprend le critère du Seuil.

### CV8-4 : (2a) dit encore « la structure n'étant pas établie » même quand D′ l'établit (mineur ; reste de CV7-3)

- **Où** : Seuil, ligne 201 (« D′ rapportée ») ; critère, ligne 262 ; lecture, ligne 118.
- **Problème** :
  - Avec bb(D) ≤ 0 < bb(D′) et un mélange > α, la lecture dit « (2a) marges seules », sans réserve (vérifié :
    `2a_avec_bbDp_positif`).
  - Le critère affirme alors une chose que la mesure contredit.
  - La v8 n'a retenu que « D′ rapportée ». C'est un choix défendable, puisque la fenêtre est étroite, mais il n'est pas suivi
    jusqu'au critère.
- **Correction**, au choix et sans nouvelle feuille :
  - soit (2a) exige aussi bb(D′) ≤ 0, sinon (2b) ;
  - soit la lecture ajoute une réserve « D′ établie (bb > 0) en (2a) », et la ligne 262 dit « la structure n'étant pas
    établie par D ».

### CV8-5 : la séquence ne fait pas tout ce que le texte lui prête, et la note de répétition cite un préenregistrement « scellé » qui ne l'est pas (mineur ; reste de CV7-5)

- **Où** :
  - texte, ligne 40 : « commandes (1) à (3) puis la rédaction mécanique » ;
  - lignes 240 et 241 : « le tout par `commandes-lecture-reelle-v8.sh` », « répété avec succès » ;
  - séquence, lignes 27 et 45 à 51 ;
  - `rediger_note_lecture_v2.py`, lignes 35 et 36 ;
  - `note-lecture-repetition-generale-v8.md`, ligne 3.
- **Problème** :
  - (a) La séquence ne lance pas `rediger_note_lecture_v2.py`. Elle ne vérifie ni son compagnon ni le sien (CV7-5 demandait le
    sien). La note de la répétition a donc été rédigée à la main, hors de la séquence répétée.
  - (b) Cette note dit « Préenregistrement **scellé** : `preenregistrement-mesure-unanime-v7.md` (`54bb2892…`) ». La v7 n'a
    jamais été scellée, et la répétition est celle de la v8. La rédaction écrit le mot « scellé » sans rien vérifier. Elle
    fige aussi en dur « note de lecture v1 », « instance du 27 octobre » et « le 28 octobre ».
  - (c) La répétition ne passe ni par l'étape 0, ni par la garde R12, ni par la branche E ≠ 60. Je les ai exercées : elles
    tiennent (réponse 1). Mais rien de déposé ne le montre.
- **Correction** :
  - Soit le texte dit « commandes (1) à (3) par la séquence ; la rédaction ensuite, à la main, avec l'heure relevée par
    `date -u` ». Soit la séquence la lance, en prenant l'heure en argument.
  - Ajouter `commandes-lecture-reelle-v8.sh.sha256` et `rediger_note_lecture_v2.py.sha256` à la ligne 27.
  - La rédaction vérifie le scellement du préenregistrement (`prereg.exiger_prereg_scelle`) avant d'écrire « scellé », ou
    écrit « non scellé (répétition) ». Elle ne fige pas la date.
  - Déposer une répétition de la branche E ≠ 60 : mon fichier à E = 52 et ses sorties peuvent servir, voir la section 4.

### CV8-6 : restes (mineur)

- **Ligne 121** :
  - « l'issue est celle du Seuil (huit issues ordonnées) » : écrire « neuf feuilles ordonnées » (CV7-6) ;
  - « synthétique v7 : ≈ +0,03 » : les chiffres sont ceux de l'essai v8, cité dans l'en-tête avec son empreinte. Écrire
    « essai v8 » (R6).
- **Refus du mode réel dans la lecture** : tirages, rééchantillonnages et commit absent ou vide n'ont qu'un cas sain déposé
  (la répétition). Leur artefact n'est déposé nulle part (R5 ; CV7-5 : « la tester sur un cas sain et sur un artefact »).
  Ils tiennent (`sortie-verif-cv8-lecture-v1.json`, `refus_manifeste_format_reel`) : ajouter ces cas à
  `essai_lecture_mecanique_v4.py`, sur la sortie au format réel de la répétition.
- **Remarque, sans correction nécessaire** : la lecture saute les vérifications de tirages, de rééchantillonnages et de commit
  dès que le manifeste porte `synthetique`. C'est voulu pour l'essai, et la séquence ne lui donne que la sortie réelle.

## 4. Mes scripts et sorties

Tout est dans ce dossier, chaque fichier avec un compagnon `.sha256`.

| fichier | contenu |
|---|---|
| `scripts/verif_cv8_v1.py` | parties `lecture` (arbre sur 64 combinaisons et étiquettes ; bornes ; (2a) avec bb(D′) > 0 ; M2 bis réfutée ; cellules à zéro ; refus du manifeste au format réel), `zero` (faux audits sous le nul), `pas_fixe`, `gardes` (compteur d'appels) ; script v8 et lecture v4 importés sans modification ; graines `SeedSequence(2810202608, spawn_key=(partie, …))` |
| `sortie-verif-cv8-lecture-v1.json`, `sortie-verif-cv8-zero-identiques-v1.json`, `sortie-verif-cv8-pas-fixe-v1.json`, `sortie-verif-cv8-gardes-v1.json` (et leurs `.err`) | leurs sorties |
| `scripts/refus_mode_reel_cv8_v1.sh` → `sortie-refus-mode-reel-v8.txt` | refus du mode réel et `--test-gardes` (15 entrées) ; fichiers du test dans `gardes-cv8/` |
| `scripts/duree_mode_reel_v1.py` → `sortie-duree-mode-reel-v1.txt` | temps processeur par sonde, extrapolé à 430 sondes (CV8-1) |
| `scripts/ecrire_npz_E52_v1.py` → `donnees-E52/synthetique-E52.npz` (`05c769d1…785f`) | fichier au format réel où E = 52 |
| `copie-dossier/` | copie du dossier ; répétition rejouée (`effectifs-…`, `sortie-…`, `lecture-…-repetition.json`, scellés par la séquence) ; journal : `repetition-rejouee.log`, à la racine |
| `copie-dossier-E52/` | répétition de la branche E ≠ 60 : `table-m2bis-m4-v8-E52-repetition.json` (`b61d1f60…`), effectifs, sortie, lecture ; journal : `repetition-E52.log`, à la racine |
| `donnees-repetition/` | copie du `.npz` de la répétition (`447dc136…`) |
| `etape0/` | copie scellée du préenregistrement, pour l'étape 0 ; `.npz` régénéré par `ecrire_npz_synthetique` ; sortie : `sortie-etape0-v8.txt`, à la racine |
| `sortie-synthetique-reproduite-v8.json`, `table-m2bis-m4-v8-reproduite.json`, `essai-lecture-mecanique-v4-reproduit.json` | reproductions à l'octet (et leurs `.err`) |
| `note-lecture-repetition-rejouee-v8.md` | rédaction v2 relancée sur la répétition rejouée |
| `journal-heures.txt` | heures UTC de début et de fin des tâches en arrière-plan |

Empreinte de ce rapport : dans `rapport-contre-lecture-mesure-unanime-v8.md.sha256`, à côté (un fichier ne peut pas contenir
sa propre empreinte).

Fin : 2026-10-28 02:46:51 UTC (`date -u`, relevé dans un appel séparé avant l'écriture de cette ligne).
