# Contre-lecture (R2) : préenregistrement « mesure unanime » v10, lecture mécanique v6 et son essai brut, rédaction v4, séquence v10 et répétition générale v10

**Verdict : à corriger en v11.** Un constat **bloquant**, sur la séquence seule ; la logique de lecture, elle, tient.
- **CV10-1, la garde « toute trace bloque » bloque l'unique exécution.** La ligne 41 de `commandes-lecture-reelle-v10.sh`
  refuse le mode réel dès qu'un fichier répond à `sortie-reelle-v10*`. Or la répétition générale que le texte fait déposer
  « dans le commit qui porte ce texte » (lignes 59 à 61) s'appelle `sortie-reelle-v10-repetition.json` (et son `.sha256`) :
  elle y répond. Lancée comme le texte la gèle, depuis le dossier du préenregistrement, la séquence réelle s'arrête à
  l'étape 0 avec le code 3 (« une trace d'exécution réelle existe … ne rien renommer »). Vérifié en exécutant la ligne 41,
  extraite telle quelle, sur l'état exact du dossier déposé (`1ef46c7b`). L'arrêt survient avant toute lecture de données,
  donc rien n'est perdu (R1 tient). Mais la séquence gelée ne peut pas faire ce pour quoi elle est gelée, et le texte
  interdit lui-même le seul contournement (renommer ou déplacer). La répétition ne l'a pas vu : le mode `REPETITION` saute
  les lignes 34 à 45, et la garde n'a jamais été exercée sur l'état déposé, alors que CV9-2 le demandait (R5).

Le reste est mineur (CV10-2, CV10-3) : le mode `LECTURE_SEULE` réécrit une note déjà scellée, et il reste des restes de CV9-4 et
CV9-5. Je ne trouve **aucun faux « confirmé »** et aucun faux blocage d'un verdict. L'arbre, l'excès, les audits, les gardes et
les refus sont justes ; la répétition se rejoue à l'identique.

Vérifié en lançant, et conforme :
- **La répétition, rejouée** depuis une copie du dossier : 29,7 secondes, code 0. Les effectifs, la lecture et la table en
  vigueur sont identiques à l'octet. La sortie est identique hors de `manifeste.donnees` (le chemin du fichier lu). La note ne
  diffère que par sa ligne 3 (heure, et empreinte de la sortie, qui suit le chemin). Elle cite `785a33fa…`, **l'empreinte de
  la v10 sur disque** : la répétition a bien été faite sur le texte final (CV9-4 (d) fermé).
- **Après un scellement** (copie scellée par moi), une répétition écrit « scellé (compagnon vérifié) » **et** « RÉPÉTITION
  GÉNÉRALE ou essai : aucune donnée réelle » (CV9-4 (b) fermé).
- **Le mode `LECTURE_SEULE`**, sur une copie : il refuse un préenregistrement non scellé (code 1), une sortie absente (code 6),
  une sortie non scellée (code 1) et une sortie dont l'empreinte des données n'est pas `968414fc…` (code 1, à l'étape (3)).
  Il va au bout sur un artefact (la sortie de répétition dont seul le manifeste est retouché), mais un second appel
  **réécrit la note scellée** (CV10-2).
- **La branche E ≠ 60 de la séquence v10** (qui a changé : garde du `.partiel` de la table, ligne 58), sur un fichier au format
  réel où E = 52 : la garde de la ligne 58 laisse passer, la table est refaite au E et aux longueurs observés, scellée et lue,
  et la séquence va jusqu'à la note scellée (code 0, 8 minutes 26 secondes).
- **Les gardes extraites** : la ligne 41 rend 3 sur une sortie finale, un `.partiel`, une trace renommée (`-interrompue-1`) —
  et aussi sur la seule répétition déposée (CV10-1). La ligne 58 rend 5 sur un `.partiel` de table, 0 sinon.
- **L'essai brut de la lecture v6**, reproduit à l'octet : neuf feuilles, six audits, six refus.
- **L'arbre de M2 ter** : 64 combinaisons, bornes, deux r₀ ; aucun désaccord de feuille ni d'étiquette.
- **Le mélange à pas fixé**, par simulation ; **les gardes** (quinze entrées ; 705 appels de `verifier_scores_invalides` pendant
  un `main()` en mode réel) ; **les refus du mode réel** (quatorze refus et un cas sain) ; **toutes les empreintes de l'en-tête**.

- Contre-lecteur : sous-agent neuf Opus 5.5. Je n'ai écrit ni le préenregistrement, ni le script, ni la table, ni la lecture,
  ni la rédaction, ni la séquence, ni aucun des rapports précédents.
- Début : 2026-10-28 03:14:15 UTC (`date -u`). Fin : dernière ligne. Les heures d'`ls` sont à l'heure de Paris (UTC + 1).
- Processeur seul. Je n'ai ouvert, chargé ni empreinté aucun fichier de `donnees/` : l'empreinte `968414fc…` n'est donc **pas**
  vérifiée par moi.
- `commandes-lecture-reelle-v10.sh` n'a été lancé qu'en mode `REPETITION` et en mode `LECTURE_SEULE` (avec la sortie de
  répétition, et un deuxième argument `pas-un-commit`), toujours sur des copies du dossier placées dans mon dossier de travail,
  jamais avec un commit. Le mode réel n'a jamais été lancé : sur une copie, il lirait les données réelles par leur chemin
  absolu si la garde passait. Pour ses gardes, je n'ai exécuté que les lignes 41 et 58, extraites dans un script à part.
- Je n'ai modifié aucun fichier du dépôt et je n'ai fait aucun commit (`git status` vide avant et après). L'essai brut de la
  lecture a été rejoué dans le dossier du dépôt, mais vers la sortie standard seulement, avec `-B` : aucun fichier écrit.
- Interpréteur : `/opt/venv-essaim-sim-v1/bin/python -I -B`, numpy 2.5.4. Mes vérifications importent le script v8 et la
  lecture v6 **sans modification**, depuis la copie, dont les fichiers sont identiques à l'octet. La seule enveloppe posée
  l'est sur un nom du module (un compteur d'appels), jamais sur le fichier.

## Empreintes lues

| fichier | empreinte | état |
|---|---|---|
| `preenregistrement-mesure-unanime-v10.md` | `785a33fae9d835ee7529a44d76629dec7ce7bfd0544a5f7dc4b2a46646d1c3c2` | objet ; identique dans `HEAD` (`1ef46c7b`) ; pas de compagnon (normal) ; aucun « ⟨…⟩ » ; `prereg.exiger_prereg_scelle` passe sur une copie scellée par moi |
| `preenregistrement-mesure-unanime-v9.md` | `9206956b…49bd35e7` | conforme à l'en-tête |
| `analyse_fausses_alertes_v8.py` | `52b1760a…5400` | conforme ; compagnon conforme ; identique dans `f180e14d` (le commit cité) et dans `HEAD` |
| `sortie-synthetique-essai-v8.json` | `f83456be…fe62` | conforme ; compagnon conforme |
| `table_m2bis_m4_v8.py` → `table-m2bis-m4-v8.json` | `7e512516…e0d3` → `f63faada…b120` | conformes ; compagnons conformes ; chiffres cités = ceux de la table |
| `lecture_mecanique_v6.py` | `e34b0b61…8a00` | conforme ; compagnon conforme ; identique dans `f180e14d` |
| `essai_lecture_mecanique_v6.py` → `essai-lecture-mecanique-v6.json` | `c4ae28ec…d1ee8d4` → `0745cc20…bbdef` | conformes ; compagnons conformes ; sortie **reproduite à l'octet** |
| `rediger_note_lecture_v4.py` | `7e7ca108…920b` | conforme ; compagnon conforme ; identique dans `f180e14d` |
| `commandes-lecture-reelle-v10.sh` | `29ae9412…a5ce9` | conforme ; compagnon conforme ; identique dans `f180e14d` |
| `synthetique-format-reel-repetition.npz` | `447dc136…b709` | compagnon conforme |
| `effectifs-reel-v10-repetition.json`, `sortie-reelle-v10-repetition.json`, `lecture-mecanique-reelle-v10-repetition.json`, `note-lecture-mecanique-v10-repetition.md` | `c05aa6fa…`, `d36a7508…`, `fb733e70…`, `ebecd8c1…` | compagnons conformes ; dans `1ef46c7b` ; rejoués (section 2) |
| `table-en-vigueur-v10-repetition.txt` | `f6e65b72…2563` | dans `1ef46c7b`, **sans compagnon** (CV10-3) |
| `contre-lecture-v9/rapport-contre-lecture-mesure-unanime-v9.md` | `aeeca90d…79b3` | conforme à l'en-tête ; les dix-huit compagnons du dossier sont conformes ; les scripts que ce rapport cite (`scripts/…`) ne sont pas versés (CV10-3) |
| `src/controle_ia/bases/sequentiel.py` | `35a09834…11ba8` | conforme |

## 1. Fermeture de CV9-1 à CV9-5 (et des restes de CV4-1, CV4-4)

| constat | état | où et pourquoi |
|---|---|---|
| CV9-1 (lancement par `nohup … &`, aucun délai) | **fermé** | En-tête, lignes 50 à 52 ; Plan d'analyse, lignes 260 à 262 ; séquence, lignes 4 à 7 : par l'outil d'exécution **en arrière-plan**, délai 7 200 000 ms, jamais `nohup … &`, jamais au premier plan borné à dix minutes ; journal écrit par la séquence elle-même (`tee -a`, ligne 36), donc la commande n'a pas besoin de redirection. **Cela suffit** : un processus lancé ainsi survit à la fin de la réponse, jusqu'à sa fin ou à son délai. Ma répétition passe l'étape (2) en 29 secondes pour 5 sondes, soit au pire 5,8 secondes par sonde (frais fixes du rééchantillonnage compris) : 430 sondes prendraient au plus 42 minutes, plus 10 minutes de table si E ≠ 60 ; le délai de deux heures garde une marge de plus du double. Un redémarrage du conteneur reste possible : il laisserait un `.partiel`, traité comme une interruption (lignes 54 à 57, 299 et 300). |
| CV9-2 (garde levée par son propre renommage ; table ; (3) et (4) ; `.partiel` non vide) | **à moitié** | Fermé : (a) la ligne 41 bloque toute trace, `-interrompue-N` compris (vérifié par extraction) ; (b) la ligne 58 garde le `.partiel` de la table (vérifié : code 5) ; (c) `LECTURE_SEULE` rejoue (3) et (4) sur la sortie scellée (lignes 43 et 44, exercé) ; (d) « un `.partiel` ne s'ouvre jamais » est écrit (en-tête, ligne 55 ; séquence, ligne 12). Ouvert : le motif de la ligne 41 attrape aussi la répétition déposée et **bloque l'unique exécution** (CV10-1) ; la garde n'a pas été exercée sur un état déposé, ce que CV9-2 demandait (« exercer la garde par un artefact déposé », R5) ; `LECTURE_SEULE` réécrit une note scellée (CV10-2). |
| CV9-3 (réfutation de M2 bis ; critère de (2a) ; réserve en (2b)) | **fermé** | Ligne 142 : « réfutée si r₀ < 0,5 et borne haute ≤ 0 → audit R4 de cohérence … qui suspend ». Ligne 283 : « D n'étant pas établie ; si bb(D′) > 0 malgré tout, réserve ». Ligne 284 : ligne des critères pour (2b) avec bb(D′) > 0. Le code pose la réserve en (2a) et en (2b) et nulle part ailleurs (vérifié : `reserve_2a_2b`). Remarque sans constat : le Seuil (lignes 220 et 221) n'attache toujours la réserve qu'à (2a) ; les critères la complètent, il n'y a pas de contradiction. |
| CV9-4 (date et instance en dur ; « répétition » d'après le scellement ; note non scellée ; empreinte absente) | **presque fermé** | Fermé : (b) « répétition » se déduit du commit `repetition-generale` (rédaction, lignes 47 et 48), vérifié après un scellement ; (c) la séquence scelle la note (ligne 84) ; (d) la note déposée cite `785a33fa…`, la v10 sur disque ; la date est passée par la séquence (ligne 81). Reste (a) : l'instance a un argument, mais la séquence ne le passe pas et sa valeur par défaut est celle qui était en dur (« instance du 27 octobre 2026 ; servie par Fable 5.1 », rédaction, ligne 29) (CV10-3). |
| CV9-5 (docstrings ; renvoi pour la branche E ≠ 60) | **à moitié** | Fermé : l'essai v6 liste les six audits (ligne 2) ; l'en-tête renvoie à la séquence v10. Ouvert (CV10-3) : la docstring de la lecture v6 (ligne 1) dit toujours « seuils gelés du préenregistrement v8 », celle de l'essai v6 (ligne 1) « Essai déposé de la lecture mécanique v5 » ; l'en-tête (lignes 62 et 63) dit que les contre-lectures des v8 et v9 « ont exercé la branche E ≠ 60 et l'interruption », mais c'étaient les séquences v8 et v9 ; celle de la v10 a changé (ligne 58, `LECTURE_SEULE`), et je suis le premier à l'exercer. |
| CV4-1 (deux définitions de M2 ter) | **fermé** | Une seule définition (lignes 216 à 230), sans r₀ : même feuille à r₀ = 0,1 et à 0,7 (vérifié). |
| CV4-4 (attributions trop larges) | **fermé** | Mélange à pas fixé vérifié (point 4) ; « dérive » n'est écrit qu'en (4c), où elle est mesurée. |

## 2. Réponses aux points du brief

**Répétition générale.** Rejouée avec `bash commandes-lecture-reelle-v10.sh REPETITION <copie du npz> 447dc136… 3 2`, depuis
`copie-dossier/` (la séquence efface elle-même, ligne 32, les sorties de répétition de la copie) : 29,7 secondes, code 0
(`repetition-rejouee-v10.log`).
- `effectifs-reel-v10-repetition.json` (`c05aa6fa…`), `lecture-mecanique-reelle-v10-repetition.json` (`fb733e70…`) et
  `table-en-vigueur-v10-repetition.txt` sont identiques à l'octet aux fichiers déposés.
- `sortie-reelle-v10-repetition.json` est identique en tout, sauf `manifeste.donnees`. La répétition déposée a lu
  `/tmp/…/scratchpad/repetition-generale/synthetique-format-reel.npz`, et non le fichier déposé ; l'empreinte est la même
  (`447dc136…`), donc le contenu aussi (CV10-3, pour le dire).
- La note ne diffère que par la ligne 3 : l'heure, et l'empreinte de la sortie.
- **La séquence va-t-elle jusqu'à la note ?** Oui, et la note est scellée. **Que dit la note ?** « Préenregistrement **NON
  SCELLÉ** (GardeArret) … **RÉPÉTITION GÉNÉRALE ou essai : aucune donnée réelle, cette note n'est pas une lecture** ». Après un
  scellement (`note-apres-scellement/`), elle dit « **scellé** (compagnon vérifié) » et toujours « RÉPÉTITION GÉNÉRALE ».
- **Verdicts de la répétition** : M1 confirmé ; M2 contrôle attendu ; M2 ter (1), avec Ville à 0,050 ; M3 tenu ; M4 confirmé ;
  première ligne. C'est un essai du code sur des scores synthétiques, sans valeur de résultat.
- **La garde « toute trace bloque »** (CV9-2), ligne 41 extraite telle quelle (`scripts/garde_trace_extraite_v1.sh` →
  `sortie-garde-trace-v1.txt`), sur des dossiers de test : 0 sans fichier ; 3 avec `sortie-reelle-v10.json`, avec le `.partiel`,
  avec `sortie-reelle-v10-interrompue-1.json.partiel` ; **3 avec la seule répétition** (`sortie-reelle-v10-repetition.json` et
  son `.sha256`) ; 0 avec la répétition v9. Sur l'état du dossier déposé (mêmes noms, fichiers vides) : **3**. Dans le dossier
  réel, `ls -d sortie-reelle-v10*` (lecture seule) rend exactement ces deux fichiers de répétition (CV10-1).
- **`LECTURE_SEULE`** (`copie-lecture-seule/`, `sortie-lecture-seule-v1.txt`), avec la sortie de répétition :
  - A, préenregistrement non scellé : code 1 (`GardeArret`) ;
  - B, scellé, sans sortie finale : code 6 ;
  - C, sortie finale non scellée : code 1 (« empreinte compagnon … absente ») ;
  - D, sortie de répétition scellée sous le nom réel : code 1 à l'étape (3) (« empreinte des données de la sortie ≠ celle
    attendue »), sans note ; il reste un `lecture-mecanique-reelle-v10.json.partiel` vide, sans conséquence ;
  - E, artefact (la même sortie, dont seul le manifeste est retouché : empreinte des données `968414fc…`, commit) : code 0,
    lecture et note scellées, la note dit « une seule exécution réelle (R1) » ;
  - F, second appel : code 0, et la note scellée de E (`3c923a62…`) est **remplacée** par une autre (`64c5a92a…`, heure
    nouvelle), compagnon effacé puis refait (CV10-2).
- **La branche E ≠ 60 de la séquence v10** (`repetition-E52-v10.log`, `copie-dossier-E52/`, fichier au format réel où E = 52,
  écrit par `ecrire_npz_synthetique` importée sans modification : `scripts/ecrire_npz_E52_v10.py`, `106cb7a1…`). La séquence
  v10 va au bout, code 0, de 03:20:24 à 03:28:50 UTC :
  - E = 52 est lu par `--effectifs-seulement` ; K par pli vaut 31 ou 32, L = 0,0305 ;
  - aucun `.partiel` au départ, donc la ligne 58 laisse passer ; la table est refaite au E et aux longueurs observés
    (manifeste : `E` 52, « longueurs réelles (effectifs-reel-v10-repetition.json) »), en `.partiel` puis renommée et scellée
    (`table-m2bis-m4-v8-E52-repetition.json`, `34e2f69b…`), en 8 minutes (03:20:25 à 03:28:24 UTC, machine chargée par mes
    autres vérifications) ;
  - la sortie, la lecture et la note suivent, toutes scellées ; la lecture vérifie E = 52 dans la table comme dans la sortie ;
    `table-en-vigueur-v10-repetition.txt` désigne la table refaite ; la note dit « NON SCELLÉ » et « RÉPÉTITION GÉNÉRALE ».
- **La consigne de lancement** est écrite partout où il le faut (en-tête, Plan d'analyse, en-tête de la séquence) et elle suffit
  (tableau de la section 1).

**Point 2 : M2 ter, un arbre à neuf feuilles.**
- **Partition : exhaustive et sans recouvrement**, par construction : des « sinon » emboîtés sur six conditions binaires (Ville
  réelles ≤ 0,05 ; bb(D) ≤ 0 ; Ville mélange > α ; bb(D′) > 0 ; Ville pas fixé ≤ α ; bb(dérive) > 0), chaque combinaison
  aboutit à une feuille et une seule.
- J'ai comparé `lecture_mecanique_v6.lire` à ma réécriture du Seuil, faite sur le texte seul (lignes 219 à 229), sur les
  64 combinaisons, avec pour base la sortie au format réel de la répétition v10 (`sortie-verif-cv10-arbre-v1.json`) :
  - les neuf feuilles sont atteintes : (1) 32 ; (2a) 8 ; (2b) 8 ; (3a) 4 ; (3b) 4 ; (4a) à (4d) 2 chacune ;
  - **aucun désaccord de feuille** ; **aucun désaccord d'étiquette** avec les lignes des critères (extraites du texte par motif).
- **Bornes** : 0,05 et 0,05 + 10⁻¹² donnent (1), 0,05 + 2 × 10⁻⁹ la suite ; bb(D) = 0 ou + 10⁻¹² se lit comme 0 ; mélange à 0,05
  n'est pas > α ; pas fixé à 0,05 est ≤ α ; bb(D′) = 0 et bb(dérive) = 0 donnent (4d). Tout tombe du côté du texte.
- **Critères** : chaque feuille a sa ligne ((4a) 272, (4b) 273, (2b) 274 et 284, (3b) 275, (1) 276, (3a) 277, (4c) 278, (4d) 279,
  (2a) 283), et chaque issue des autres énoncés aussi (M1 confirmé, non concluant, réfuté ; M3 fragile, audit ; M4 confirmé,
  non concluant ou réfuté, non lisible, maximum ; M2 contrôle ; M2 bis réfutée ; placebo ; cellule à zéro dans M3 et dans un bras).
- **r₀** n'est une condition nulle part dans M2 ter : même feuille à r₀ = 0,1 et à 0,7.
- **Attributions** (CV6-2) : (4c) est justifiée, puisque D = D′ + dérive **exactement** (trois différences des mêmes médianes sur
  le même tirage, script, lignes 557 à 560) ; (1), (2a), (2b), (3a), (3b), (4a), (4b) et (4d) n'affirment que ce qui est mesuré.

**Point 3 : excès apparié de M4.** Le script est inchangé depuis la v8 (même empreinte, identique dans `f180e14d`). Relu :
- médiane sur les sondes des différences par sonde : ligne 541 (point) et 545 (rééchantillonnage) ;
- même calibrage : à τ = 0, `Xe = Xcal = X` ; le bras a `calibrage_sans_effet=True`, donc `Xcal = X` ; mêmes `perm` et `plis`
  (lignes 487 et 491) ; donc mêmes μ₀, σ, seuils ;
- rééchantillonnage apparié : le même `idx` sert aux deux termes (ligne 545) ;
- la table calcule le même excès (manifeste de la table : « par sonde, quantité de M4 moins la même quantité à τ = 0 (même
  calibrage) ; médiane sur les sondes ») ; ses chiffres cités sont exacts (excès 0,1429 ; 0,0732 ; 0,0274 ; 0,0059 ; quantité
  brute 0,1937 ; 0,1238 ; 0,0748 ; 0,0545 ; maximum 0,0192 à 0,0263) ;
- « excès > 0,02 et borne basse > 0 » ferme le faux « confirmé » de CV4-2 : un défaut de niveau commun aux deux termes s'annule
  sonde par sonde ; la borne est stricte après arrondi (essai brut : 0,02 + 10⁻¹² donne « non concluant »).
- Aucun nouveau faux « confirmé » ni faux blocage : la lecture v6 ne diffère de la v5 que par les docstrings et un message
  (`diff`), et la v5 avait été vérifiée.

**Point 4 : mélange à pas fixé** (`sortie-verif-cv10-pas-fixe-v1.json` ; 12 sondes, E = 60, masques de 5 à 10 actions avec
quelques invalides au milieu, pour que le « pas » soit l'indice brut).
- Marges par pas et masque gardés, à chaque pas, dans les trois mondes (vérifié valeur par valeur, triées).
- **Dépendance r₀ = 0,3, sans dérive** : r₀ vaut 0,292 à l'origine, − 0,004 sur le pas fixé, − 0,010 sur le mélange : la
  dépendance est détruite ; Ville vaut 0,033 sur les réelles et 0 sur les deux mélanges, donc D = D′ = 0,033 et dérive = 0.
- **Dérive linéaire en t (0,3 par pas), sans effet épisode** : r₀ vaut − 0,006 à l'origine et − 0,008 sur le pas fixé (la
  dérive survit), − 0,001 sur le mélange ; Ville vaut 0 partout, donc D′ = 0 (« réelles moins pas fixé ≈ 0 » tient). « Réelles
  moins mélange complet > 0 » ne tient pas ici (D = 0) : une dérive de moyenne n'élève pas Ville sur les réelles dans ce monde.
  Les contre-lectures v6 à v9 l'avaient vu ; l'arbre en tient compte, puisqu'une dérive ne fabrique pas un faux « dépendance ».
- **Ni l'un ni l'autre** : r₀ ≈ 0 partout, D = D′ = 0.

**Point 5 : gardes.**
- `--test-gardes` sort **quinze entrées**, soit quatorze gardes et `correlation_saine` = 0,171 (`sortie-test-gardes-v10.json`).
  Le décompte de l'en-tête (cinq sains, quatre artefacts de calcul, trois de chargement, E minimal, corrélation constante) est exact.
- `verifier_scores_invalides` est appelée **705 fois** pendant un `main()` en mode réel sur le fichier de la répétition, soit
  5 sondes × 141 passages (`sortie-verif-cv10-gardes-v1.json`) : elle est sur le chemin réel (script, ligne 199).
- Le mode réel refuse, vérifié en lançant (`sortie-refus-mode-reel-v10.txt`, aucun octet écrit sur la sortie standard) :
  `--effectifs-seulement` sans empreinte, avec une empreinte vide ou fausse ; `--tirages 5` et `--bootstrap 300`, avec et sans
  `--effectifs-seulement` ; l'absence de `--commit` (ou un commit vide), de `--sondes-reelles` ou de `--sondes-placebo` ; des
  effectifs faux ; `--reel` avec `--synthetique`. Le cas sain écrit 807 octets, identiques aux effectifs déposés.

**Point 6 : chiffres cités.**
- Recalculés et conformes : 0,395 ; 0,0725 ; 0,077 (0,0773) ; 2/40 ; K = 39 ; rang 38 ; ceux de la table v8 (point 3, plus Ville à
  τ = 0 : 0 ; 0,033 ; 0,083 ; 0,133 ; Ville à τ = 2 : 0,138 à 0,152 ; M2 bis : + 0,138 ; + 0,104 ; + 0,065 ; + 0,019) ;
  « synthétique v8 : ≈ + 0,03 pour les deux à r₀ = 0,2 » (essai v8 : r₀ 0,201, D = D′ = 0,030) ; ceux de l'en-tête (« quinze
  entrées », « six audits », « six refus dont les trois propres au mode réel », « 3 sondes réelles, 2 placebo, E = 60 »).
- Les empreintes de l'en-tête correspondent aux fichiers ; tous les compagnons existent, sauf celui du préenregistrement
  (normal) et celui de `table-en-vigueur-v10-repetition.txt` (CV10-3).
- Le texte ne contient aucun « ⟨…⟩ ». Le seul espace réservé est celui que la rédaction écrit (« ⟨À ÉCRIRE … ⟩ »), voulu.

**Point 7 : ce que je n'avais pas vu venir.**
- **La garde qui bloque la vraie exécution** (CV10-1) : chaque contre-lecture a rejoué la répétition, et la répétition ne
  traverse pas l'étape 0 du mode réel. Le motif proposé par la contre-lecture v9 (`compgen -G 'sortie-reelle-v9*'`) avait le
  même défaut.
- **`LECTURE_SEULE` sans limite** (CV10-2).
- Pour information, sans constat : la répétition tombe encore en (1) avec Ville à 0,050 et bb(D) = 0,012 > 0 ; la feuille (1) se
  joue à une alerte près (déjà dit en v9).

## 3. Constats

### CV10-1 : la garde « toute trace bloque » attrape la répétition déposée et bloque l'unique exécution (bloquant)

- **Où** :
  - séquence, ligne 41 : `if ls sortie-reelle-v10* >/dev/null 2>&1; then … exit 3; fi` ;
  - séquence, lignes 29 à 32 : la répétition écrit `sortie-reelle-v10-repetition.json` (suffixe `-repetition`) ;
  - texte, lignes 54 à 63 : « toute trace `sortie-reelle-v10*` … bloque le mode réel et ne se renomme pas pour relancer » ;
    la répétition est « déposée et scellée dans le commit qui porte ce texte » ; Plan d'analyse, lignes 246 et 260 : tout se
    lance depuis le dossier du préenregistrement.
- **Problème** :
  - Dans le dossier déposé (`1ef46c7b`), `sortie-reelle-v10*` répond à `sortie-reelle-v10-repetition.json` et à son `.sha256`.
    Lancée comme le texte le gèle, `bash commandes-lecture-reelle-v10.sh <commit>` passe le contrôle du scellement (ligne 39),
    puis sort avec le code 3 à la ligne 41, avant l'étape (1) (`sortie-garde-trace-v1.txt`, cas `etat_depose`).
  - Rien n'est lu, donc R1 tient. Mais la séquence gelée ne peut pas faire l'unique exécution. Le seul contournement (déplacer
    ou renommer la répétition) contredit le texte (« ne rien renommer », « déposés dans le commit qui porte ce texte »). Corriger
    la ligne change l'empreinte de la séquence, citée à la ligne 48 : c'est une version nouvelle de toute façon.
  - Le défaut n'a été vu par personne parce que le mode `REPETITION` saute les lignes 34 à 45 : la répétition « répétée avec
    succès » (ligne 262) n'a jamais traversé l'étape 0 du mode réel, et la garde n'a pas été exercée sur un état déposé (R5,
    demandé par CV9-2).
- **Correction** (séquence v11, texte v11) :
  - Ne plus tester un préfixe que la répétition partage. Au choix : (a) un témoin `execution-reelle-v11.commencee`, créé à
    l'étape 0 par `set -o noclobber; : > execution-reelle-v11.commencee` (échec = trace), jamais effacé, plus la liste explicite
    `sortie-reelle-v11.json`, `sortie-reelle-v11.json.partiel`, `sortie-reelle-v11-interrompue-*` ; ou (b) écrire la répétition
    sous un nom qui ne commence pas par `sortie-reelle-v11` (par exemple dans un sous-dossier `repetition-v11/`), et garder le
    motif ; ou (c) filtrer : `ls -d sortie-reelle-v11* 2>/dev/null | grep -v -- '-repetition' | grep -q . && exit 3`. Je
    recommande (a) avec (b) : le témoin ne dépend d'aucun nom de sortie.
  - Faire passer la répétition par la même garde (une fonction appelée dans les deux modes, avec le suffixe), pour que la
    répétition exerce l'étape 0.
  - Déposer le test de la garde (R5) : la ligne extraite passe sur l'état du dossier tel qu'il sera au moment du lancement
    (répétition déposée comprise) et bloque sur trois artefacts (sortie finale, `.partiel`, trace renommée).

### CV10-2 : `LECTURE_SEULE` réécrit une note et une lecture déjà scellées (mineur)

- **Où** : séquence, lignes 40 à 45, 72, 76 à 78 et 82 à 84 (`rm -f …sha256` avant chaque `sceller`) ; texte, lignes 57 et 58
  (« se reprend par le mode `LECTURE_SEULE` ») ; R12 (« on n'écrase jamais ») ; Plan d'analyse, ligne 259 (la note de lecture
  reprend la note mécanique « telle quelle »).
- **Problème** :
  - (a) `LECTURE_SEULE` se lance autant de fois qu'on veut, y compris quand la séquence est allée au bout. Chaque appel efface le
    compagnon de la lecture et de la note, puis réécrit et rescelle les deux. La lecture est déterministe, donc identique, mais
    la note change (l'heure) : vérifié, une note scellée `3c923a62…` devient `64c5a92a…` (cas E puis F). Une note déjà reprise
    dans `lecture-mesure-unanime-v1.md` peut ainsi changer sous elle, sans trace.
  - (b) En `LECTURE_SEULE`, la table refaite (E ≠ 60), lue dans `table-en-vigueur-v10.txt`, n'est pas vérifiée par son compagnon
    (la ligne 48 ne vérifie que la table gelée), et `table-en-vigueur-v10.txt` n'est pas scellé.
  - (c) Le commit passé à `LECTURE_SEULE` n'est pas comparé à celui du manifeste de la sortie : la note pourrait citer deux
    commits différents.
- **Correction** : en `LECTURE_SEULE`, refuser si `note-lecture-mecanique-v11.md.sha256` existe (la séquence est allée au bout) ;
  si la lecture est déjà scellée, la vérifier au lieu de la réécrire ; ne jamais effacer un compagnon ; vérifier le compagnon de
  la table en vigueur et sceller `table-en-vigueur-v11.txt` à l'étape (2) ; refuser si le commit passé diffère de celui du
  manifeste.

### CV10-3 : restes de CV9-4 (a) et de CV9-5 (mineur)

- **Instance en dur** : la rédaction a pris l'argument `--instance`, mais sa valeur par défaut est l'ancienne valeur en dur
  (« lignée conv-audit (instance du 27 octobre 2026 ; servie par Fable 5.1) », ligne 29), et la séquence ne le passe pas
  (ligne 82). Une exécution par une autre instance, ou servie par un autre modèle, écrirait une provenance fausse. Correction :
  la séquence passe `--instance` depuis une variable obligatoire, et l'argument n'a pas de valeur par défaut.
- **Mois** : la ligne 81 ne traduit qu'« October » et « November » ; un lancement en décembre écrirait « December ».
- **Docstrings** : `lecture_mecanique_v6.py`, ligne 1 : « seuils gelés du préenregistrement v8 » (écrire « v11 ») ;
  `essai_lecture_mecanique_v6.py`, ligne 1 : « Essai déposé de la lecture mécanique v5 » (écrire « v6 »).
- **Renvoi** : en-tête, lignes 62 et 63, « les contre-lectures des v8 et v9 … ont exercé la branche E ≠ 60 et l'interruption » :
  c'étaient les séquences v8 et v9. La v10 a changé cette branche (ligne 58) et ajouté `LECTURE_SEULE`. Mes sorties
  (`repetition-E52-v10.log`, `sortie-garde-table-v1.txt`, `sortie-lecture-seule-v1.txt`) peuvent être citées pour la v10 ; la
  v11 devra être exercée à son tour.
- **Compagnon** : `table-en-vigueur-v10-repetition.txt` est déposé dans `1ef46c7b` sans `.sha256` (R6).
- **Provenance de la répétition** : la répétition déposée a lu une copie du fichier, à
  `/tmp/…/scratchpad/repetition-generale/synthetique-format-reel.npz`, et non `synthetique-format-reel-repetition.npz`. Même
  empreinte, donc même contenu ; le dire en une demi-ligne.
- **Versement des contre-lectures** : `contre-lecture-v9/` (comme `contre-lecture-v8/`) contient les sorties et leurs
  compagnons, mais pas les scripts que son rapport cite (`scripts/verif_cv9_v1.py`, `scripts/garde_partiel_extraite_v1.sh`,
  `scripts/ecrire_npz_E52_v9.py`, …) : ses sorties ne se refont pas depuis le dépôt. Verser aussi `scripts/` (le mien compris).

## 4. Mes scripts et sorties

Tout est dans ce dossier. Chaque script et chaque sortie a un compagnon `.sha256`. Les copies du dossier ne reçoivent un
compagnon que pour les fichiers que j'y ai produits (la séquence scelle elle-même les siens). Les dossiers de test
`garde-trace/` et `garde-table/` ne contiennent que des fichiers vides aux noms du dossier déposé (certains finissent par
`.sha256`) : ils n'ont pas de compagnon, à dessein.

| fichier | contenu |
|---|---|
| `scripts/verif_cv10_v1.py` | parties `arbre` (64 combinaisons, étiquettes, bornes, r₀, réserve en (2a) et (2b)), `pas_fixe`, `gardes` (compteur d'appels) ; script v8 et lecture v6 importés sans modification ; graines `SeedSequence(2810202610, spawn_key=(partie, …))` |
| `sortie-verif-cv10-arbre-v1.json`, `sortie-verif-cv10-pas-fixe-v1.json`, `sortie-verif-cv10-gardes-v1.json` (et leurs `.err`) | leurs sorties |
| `scripts/garde_trace_extraite_v1.sh` → `sortie-garde-trace-v1.txt` | ligne 41 de la séquence, extraite telle quelle, sur sept états (`garde-trace/`), dont l'état du dossier déposé |
| `sortie-garde-table-v1.txt` | ligne 58 extraite, deux états (`garde-table/`) |
| `scripts/refus_mode_reel_cv10_v1.sh` → `sortie-refus-mode-reel-v10.txt` | quatorze refus du mode réel et un cas sain (`refus-cv10/`) |
| `sortie-test-gardes-v10.json` | `--test-gardes` (quinze entrées ; fichiers du test dans `gardes-cv10/`) |
| `essai-lecture-mecanique-v6-reproduit.json` (et `.err`) | essai brut de la lecture v6 ; identique au déposé hors des deux chemins de `sources` (j'ai passé des chemins absolus) ; rejoué avec les chemins relatifs, il est identique à l'octet |
| `copie-dossier/`, `repetition-rejouee-v10.log`, `heure-debut-repetition.txt`, `depose-v10/` | répétition rejouée ; copie des fichiers de répétition déposés, pour la comparaison |
| `copie-lecture-seule/`, `sortie-lecture-seule-v1.txt`, `repetition-apres-scellement-v10.log`, `note-apres-scellement/` | `LECTURE_SEULE`, cas A à F (copie scellée par moi) ; répétition après scellement |
| `scripts/ecrire_npz_E52_v10.py` → `donnees-E52/` | fichier au format réel où E = 52 |
| `copie-dossier-E52/`, `repetition-E52-v10.log` | séquence v10 en répétition à E = 52 |
| `donnees-repetition/` | copie du `.npz` de la répétition (`447dc136…`) |

Empreinte de ce rapport : dans `rapport-contre-lecture-mesure-unanime-v10.md.sha256`, à côté (un fichier ne peut pas contenir
sa propre empreinte).

Fin : 2026-10-28 03:29:47 UTC (`date -u`, relevé dans un appel séparé avant l'écriture de cette ligne).
