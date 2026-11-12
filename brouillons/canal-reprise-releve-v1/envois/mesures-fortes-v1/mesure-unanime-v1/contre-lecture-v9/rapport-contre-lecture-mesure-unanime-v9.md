# Contre-lecture (R2) : préenregistrement « mesure unanime » v9, lecture mécanique v5 et son essai brut, rédaction v3, séquence v9 et répétition générale v9

**Verdict : à corriger en v10.** La logique tient. L'arbre de M2 ter, l'excès apparié de M4, les audits, les gardes et les refus
sont justes, et la répétition **se rejoue** à l'identique jusqu'à la note, qui dit « NON SCELLÉ ». Je ne trouve aucun faux
« confirmé », et aucun faux blocage par la nouvelle règle « M2 bis réfutée = audit ». Un constat moyen reste, sur la **façon de
lancer** l'unique exécution :
- **CV9-1, lancement.** Le Plan d'analyse (ligne 250) et l'en-tête de la séquence (ligne 4) gèlent
  `nohup bash commandes-lecture-reelle-v9.sh … &`. C'est justement le mode que l'environnement de l'agent arrête quelques
  minutes après la fin de sa réponse. Une exécution d'environ 30 à 40 minutes lancée ainsi a donc toutes les chances d'être
  coupée pendant l'étape (2). Or la v9 fait de toute interruption une **version nouvelle**. Le délai de lancement que demandait
  CV8-1 n'est pas écrit non plus.

Le reste est mineur (CV9-2 à CV9-5). Le plus utile est CV9-2 : la garde du `.partiel` est levée par le renommage que la séquence
prescrit elle-même.

Vérifié en lançant, et conforme :
- **La répétition, rejouée** depuis une copie du dossier, en 30 secondes, code 0 :
  - les effectifs et la lecture sont identiques à l'octet ;
  - la sortie est identique hors du champ `donnees` (le chemin du fichier lu) ;
  - la note ne diffère que par sa ligne de provenance (heure, et empreinte du préenregistrement : voir CV9-4).
- **L'interruption, simulée** : arrêt du processus de l'étape (2) par son identifiant de processus (R10). Il reste un
  `sortie-reelle-v9-repetition.json.partiel` de 0 octet, aucun fichier final, et la séquence sort avec le code 143.
- **La garde du `.partiel`**, lignes 30 et 31 extraites telles quelles : elle rend le code 5 sur un `.partiel` et le code 3 sur
  une sortie existante. Mais elle rend 0 une fois le `.partiel` renommé comme prescrit (CV9-2).
- **La branche E ≠ 60 de la séquence v9**, qui a changé depuis la v8 (table écrite en `.partiel`, puis renommée), exercée sur
  un fichier au format réel où E = 52 : la table est refaite, scellée et lue, et la séquence va au bout (code 0).
- **L'essai brut de la lecture v5**, reproduit à l'octet : neuf feuilles, six audits, six refus.
- **L'arbre de M2 ter**, sur 64 combinaisons et aux bornes : aucun désaccord de feuille ni d'étiquette.
- **Le mélange à pas fixé**, par simulation.
- **M2 bis sous des marges très asymétriques** : la différence reste > 0, avec une borne basse > 0.
- **Les gardes** : quinze entrées ; 705 appels de `verifier_scores_invalides` pendant un `main()` en mode réel.
- **Les refus du mode réel** : treize refus et un cas sain.
- **Toutes les empreintes de l'en-tête.**

- Contre-lecteur : sous-agent neuf Opus 5.5. Je n'ai écrit ni le préenregistrement, ni le script, ni la table, ni la lecture,
  ni la rédaction, ni la séquence, ni aucun des rapports précédents.
- Début : 2026-10-28 02:53:37 UTC (`date -u`). Fin : dernière ligne. Les heures d'`ls` sont à l'heure de Paris (UTC + 1).
- Processeur seul. Je n'ai ouvert, chargé ni empreinté aucun fichier de `donnees/` : l'empreinte `968414fc…` n'est donc **pas**
  vérifiée par moi.
- `commandes-lecture-reelle-v9.sh` n'a été lancé qu'en mode `REPETITION`, sur des copies du dossier placées dans mon dossier de
  travail, jamais avec un commit. Pour la garde du mode réel, je n'ai exécuté que ses deux lignes, extraites dans un script à
  part : aucune lecture de données n'était possible.
- Je n'ai modifié aucun fichier du dépôt et je n'ai fait aucun commit.
- Interpréteur : `/opt/venv-essaim-sim-v1/bin/python -I -B`, numpy 2.5.4. Mes vérifications importent le script v8 et la
  lecture v5 **sans modification**, depuis la copie, dont les fichiers sont identiques à l'octet. La seule enveloppe posée
  l'est sur un nom du module (un compteur d'appels), jamais sur le fichier.

## Empreintes lues

| fichier | empreinte | état |
|---|---|---|
| `preenregistrement-mesure-unanime-v9.md` | `9206956b25ecd64c4bfb0eecd484eaa5605a4680940a34070caf9aaf49bd35e7` | objet ; identique dans `HEAD` (`ea1c2114`) ; pas de compagnon (normal) ; aucun « ⟨…⟩ » ; `prereg.exiger_prereg_scelle` passe sur une copie scellée par moi, donc `problemes` = [] |
| `preenregistrement-mesure-unanime-v8.md` | `92c208af…8c1d` | conforme à l'en-tête |
| `analyse_fausses_alertes_v8.py` | `52b1760a…5400` | conforme ; compagnon conforme ; identique dans `4b894c7a`, le commit cité ; **inchangé depuis la v8** |
| `sortie-synthetique-essai-v8.json` | `f83456be…fe62` | conforme ; compagnon conforme |
| `table_m2bis_m4_v8.py` → `table-m2bis-m4-v8.json` | `7e512516…e0d3` → `f63faada…b120` | conformes ; compagnons conformes ; les chiffres cités dans le texte sont ceux de la table |
| `lecture_mecanique_v5.py` | `258800f0…3fc` | conforme ; compagnon conforme ; identique dans `4b894c7a` |
| `essai_lecture_mecanique_v5.py` → `essai-lecture-mecanique-v5.json` | `1b41319b…c981` → `63ba9773…b9f7` | conformes ; compagnons conformes ; sortie **reproduite à l'octet** |
| `rediger_note_lecture_v3.py` | `ebdaa4b2…312c` | conforme ; compagnon conforme ; identique dans `4b894c7a` |
| `commandes-lecture-reelle-v9.sh` | `ac1b6b65…b578` | conforme ; compagnon conforme ; identique dans `4b894c7a` |
| `synthetique-format-reel-repetition.npz` | `447dc136…b709` | compagnon conforme |
| `effectifs-reel-v9-repetition.json`, `sortie-reelle-v9-repetition.json`, `lecture-mecanique-reelle-v9-repetition.json`, `note-lecture-mecanique-v9-repetition.md` | `c05aa6fa…`, `d36a7508…`, `608e7822…`, `1c7506b3…` | compagnons conformes ; rejoués (section 2) |
| `contre-lecture-v8/rapport-contre-lecture-mesure-unanime-v8.md` | `989c02de…781dec` | conforme à l'en-tête ; les vingt compagnons du dossier sont conformes |
| `src/controle_ia/bases/sequentiel.py` | `35a09834…11ba8` | conforme |

## 1. Fermeture de CV8-1 à CV8-6 (et des restes de CV4-1, CV4-4)

| constat | état | où et pourquoi |
|---|---|---|
| CV8-1 (durée ; une interruption perd l'unique exécution) | **à moitié** | Fermé : la durée est dite (lignes 46 et 47 ; séquence, lignes 5 et 6). La sortie passe par un fichier temporaire renommé à la fin (séquence, lignes 51 et 52) : je l'ai vérifié en interrompant, il reste un `.partiel` de 0 octet et aucun fichier final. Une garde refuse le `.partiel` (ligne 31 : code 5, vérifié). La Liste d'arrêt dit l'interruption (lignes 287 et 288). Ouvert : (a) le lancement prescrit, `nohup … &`, est celui que l'environnement de l'agent arrête après la réponse, et aucun délai n'est écrit, alors que CV8-1 demandait « en arrière-plan, avec un délai d'au moins 90 minutes » (CV9-1) ; (b) le renommage prescrit par la séquence lève sa propre garde, et le `.partiel` de la table n'est pas gardé (CV9-2). |
| CV8-2 (étiquette de (4b)) | **fermé** | Lecture v5, ligne 125 : « (4b) dépendance établie, mélange à pas fixé au-dessus de α », la même étiquette qu'au Seuil (ligne 216) et aux critères (ligne 262). Sur 64 combinaisons, il n'y a aucun désaccord d'étiquette (`sortie-verif-cv9-arbre-v1.json`). La lecture n'ajoute jamais « (dérive mesurée) ». Le Seuil le permet sans l'exiger (« n'y est écrit que si »), et la note rapporte la dérive mesurée avec son intervalle. |
| CV8-3 (M2 bis réfutée : audit ou non) | **à moitié** | Fermé : Seuil, lignes 198 et 199, et liste des audits (ligne 221) ; critère, ligne 279 ; lecture, lignes 103 et 190. L'essai brut le vérifie : `M2_bis_refutee` suspend la ligne. Ouvert : la colonne « réfutation » de M2 bis dans le tableau des prédictions (ligne 132) ne donne toujours que « « hors table » si l'écart dépasse 0,05 ; rapporté », sans le critère du Seuil ni le mot « audit ». CV8-3 le demandait « dans les deux cas » (CV9-3). |
| CV8-4 ((2a) avec bb(D′) > 0) | **à moitié** | Fermé : réserve au Seuil (lignes 210 et 211) et dans la lecture (lignes 120 et 121), vérifiée en (2a). Ouvert : le critère de (2a), ligne 272, dit toujours « la structure n'étant pas établie », sans « par D ». De plus, la lecture pose la réserve **aussi en (2b)**, ce que le texte ne dit pas (vérifié : `reserve_2a_2b`) (CV9-3). |
| CV8-5 (la séquence et la rédaction) | **à moitié** | Fermé : la séquence lance la rédaction (lignes 61 et 62) et vérifie son compagnon et celui de la rédaction (ligne 34). La rédaction n'écrit « scellé » qu'après `exiger_prereg_scelle` (rédaction, lignes 39 à 44) : « NON SCELLÉ » en répétition, vérifié. Ouvert (CV9-4) : la rédaction fige toujours en dur « instance du 27 octobre 2026 », « servie par Fable 5.1 » et « le 28 octobre » (ligne 45), ce que CV8-5 (b) demandait de ne plus faire. Son statut se déduit du seul scellement : une répétition faite après le scellement écrit « scellé (compagnon vérifié) … Sortie réelle … Une seule exécution réelle » (vérifié). La séquence ne scelle pas la note. La note déposée cite une empreinte du préenregistrement (`b10f2c11…`) qui n'est pas celle de la v9 sur disque. |
| CV8-6 (restes) | **fermé, deux restes** | Fermé : « neuf feuilles » (ligne 130) ; « synthétique v8 » (ligne 130) ; commentaire de la lecture (ligne 104) ; refus propres au mode réel déposés dans l'essai (tirages, rééchantillonnages, commit absent), avec un cas sain, reproduits à l'octet. Restes (CV9-5) : la docstring de la lecture v5 (ligne 1) dit « seuils gelés du préenregistrement v8 » ; celle de l'essai v5 (lignes 2 et 3) ne compte que cinq audits, alors que le code en exerce six. |
| CV4-1 (deux définitions de M2 ter) | **fermé** | Une seule définition (lignes 206 à 220), sans r₀ : vérifié, la même feuille à r₀ = 0,1 et à 0,7. |
| CV4-4 (attributions trop larges) | **fermé** | Le mélange à pas fixé est vérifié (réponse 4). On n'écrit « dérive » qu'en (4c), où elle est mesurée. Il reste les deux réserves d'étiquette de CV9-3. |

## 2. Réponses aux points du brief

**Répétition générale.** Je l'ai rejouée avec
`bash commandes-lecture-reelle-v9.sh REPETITION <copie du npz> 447dc136… 3 2`, depuis `copie-dossier/`, après avoir retiré
de la copie les sorties de répétition déposées : 29,8 secondes, code 0 (`repetition-rejouee-v9.log`).
- `effectifs-reel-v9-repetition.json` (`c05aa6fa…`) et `lecture-mecanique-reelle-v9-repetition.json` (`608e7822…`) sont
  identiques à l'octet aux fichiers déposés.
- `sortie-reelle-v9-repetition.json` est identique en tout, sauf `manifeste.donnees`, le chemin du fichier lu.
- La note `note-lecture-mecanique-v9-repetition.md` ne diffère de la note déposée que par la ligne 3. On y lit l'heure, et
  l'empreinte du préenregistrement : la note déposée cite `b10f2c11…`, la note rejouée `9206956b…`, celle de la v9 sur disque
  (CV9-4).
- **La séquence va-t-elle jusqu'à la note ?** Oui. **La note dit-elle « NON SCELLÉ » ?** Oui : « Préenregistrement **NON
  SCELLÉ** (GardeArret : répétition ou essai, pas une lecture réelle) ». Mais elle le dit parce que le préenregistrement n'est
  pas encore scellé, non parce que c'est une répétition. Après le scellement, une répétition écrirait « scellé » (CV9-4).
- **Verdicts de la répétition** : M1 confirmé ; M2 contrôle attendu ; M2 ter (1), avec Ville à 0,050, juste à α ; M3 tenu ;
  M4 confirmé ; première ligne. C'est un essai du code sur des scores synthétiques, sans valeur de résultat.
- **Interruption** (`interruption-v9.log`, `copie-interruption/`) :
  - j'ai lancé la répétition, attendu « étape (2) lancée », puis arrêté le processus de calcul par son identifiant de
    processus ;
  - il reste `sortie-reelle-v9-repetition.json.partiel` (0 octet), sans fichier final, sans lecture et sans note ; la séquence
    sort avec le code 143 ;
  - la garde du mode réel (lignes 30 et 31, extraites telles quelles dans `scripts/garde_partiel_extraite_v1.sh` →
    `sortie-garde-partiel-v1.txt`) rend 0 sans fichier, 5 avec le `.partiel`, 3 avec une sortie, 3 avec les deux, et **0
    après le renommage en `sortie-reelle-v9-interrompue-1.json.partiel`** que la séquence prescrit (CV9-2).
- **La branche E ≠ 60 de la séquence v9** (`repetition-E52-v9.log`, `copie-dossier-E52/`, fichier au format réel à E = 52
  écrit par `ecrire_npz_synthetique`, importée sans modification : `scripts/ecrire_npz_E52_v9.py`, empreinte `3508613b…`).
  La séquence v9 va au bout, avec le code 0 :
  - E = 52 est lu par `--effectifs-seulement` ; K par pli vaut 31 ou 32 et L = 0,0305 ;
  - la table est refaite au E et aux longueurs observés (`--longueurs-json`), en `.partiel`, puis renommée et scellée
    (`table-m2bis-m4-v8-E52-repetition.json`, `ce709843…`), en 8 minutes sur une machine chargée (02:59:15 à 03:07:10 UTC) ;
  - la sortie, la lecture et la note suivent. La lecture vérifie E = 52 dans la table comme dans la sortie, et la note dit
    « NON SCELLÉ ».

**Point 2 : M2 ter, un arbre à neuf feuilles.**
- **Partition : exhaustive et sans recouvrement**, par construction. Ce sont des « sinon » emboîtés sur six conditions
  binaires : Ville réelles ≤ 0,05 ; bb(D) ≤ 0 ; Ville mélange > α ; bb(D′) > 0 ; Ville pas fixé ≤ α ; bb(dérive) > 0.
- J'ai comparé `lecture_mecanique_v5.lire` à ma réécriture du Seuil, faite sur le texte seul (lignes 209 à 219), sur les
  64 combinaisons, avec pour base la sortie **au format réel** de la répétition (`sortie-verif-cv9-arbre-v1.json`) :
  - les neuf feuilles sont atteintes : (1) 32 ; (2a) 8 ; (2b) 8 ; (3a) 4 ; (3b) 4 ; (4a) à (4d) 2 chacune ;
  - il n'y a **aucun désaccord de feuille** ;
  - il n'y a **aucun désaccord d'étiquette** avec les lignes des critères.
- **Bornes** : 0,05 et 0,05 + 10⁻¹² donnent (1), et 0,05 + 2 × 10⁻⁹ donne la suite. bb(D) = ± 10⁻¹² se lit comme 0, et le
  mélange à 0,05 n'est pas > α. Le mélange à pas fixé à 0,05 est ≤ α, et bb(dérive) = 0 donne (4d). Tout tombe du côté du texte.
- **Critères** : chaque feuille a sa ligne : (4a) 261, (4b) 262, (2b) 263, (3b) 264, (1) 265, (3a) 266, (4c) 267, (4d) 268,
  (2a) 272.
- **r₀** n'est une condition nulle part dans M2 ter (vérifié : même feuille à r₀ = 0,1 et à 0,7).
- **Attributions** :
  - (4c) est justifiée : D = D′ + dérive **exactement**, puisque les trois termes sont des différences des mêmes médianes sur
    le même tirage (script, lignes 557 à 560) ;
  - (1), (2b), (3a), (3b), (4a), (4b) et (4d) sont justifiées ;
  - (2a) l'est avec la réserve, mais son critère, ligne 272, la contredit encore quand bb(D′) > 0 (CV9-3).
- **Audits** : sur 36 cas tirés au hasard (six par audit), chacun suspend la ligne, qui commence par « AUDIT ».

**Point 3 : excès apparié de M4.** Le script est inchangé depuis la v8 (même empreinte). D'après le `diff` de la v6 à la v8,
le code de l'excès n'a pas bougé depuis la v6. Je l'ai relu :
- Médiane sur les sondes des différences par sonde : lignes 541 et 545.
- Même calibrage :
  - à τ = 0, `Xe = Xcal = X` ;
  - le bras a `calibrage_sans_effet=True`, donc `Xcal = X` ;
  - la permutation et les plis sont les mêmes ;
  - donc μ₀, σ et les seuils sont les mêmes.
- Rééchantillonnage apparié : le même `idx` sert aux deux termes (lignes 544 et 545).
- La table calcule le même excès, par couple monde-sonde. Ses chiffres cités sont exacts : excès 0,143 ; 0,073 ; 0,027 ; 0,006 ;
  quantité brute 0,194 ; 0,124 ; 0,075 ; 0,0545 ; maximum 0,019 à 0,026.
- Le seuil « excès > 0,02 et borne basse > 0 » ferme le faux « confirmé » de CV4-2 : un défaut de niveau commun aux deux termes
  s'annule sonde par sonde.
- La borne est stricte après arrondi : un excès de 0,02 + 10⁻¹² donne « non concluant » (essai brut).
- Je ne trouve aucun nouveau faux « confirmé » ni aucun faux blocage dans M4.
- **Nouvelle règle de la v9, « M2 bis réfutée = audit qui suspend »** : j'ai cherché un faux blocage du côté des marges très
  asymétriques, où Ville monte déjà à τ = 0 sans dépendance (`sortie-verif-cv9-m2bis-v1.json`). J'ai pris des scores
  lognormaux, 30 sondes, E = 60, 20 tirages, sur trois mondes (σ du logarithme et part d'épisode : 1,0 et 0,3 ; 1,5 et 0,3 ;
  2,0 et 0,4) :

  | monde | r₀ médian | Ville à τ = 0 | Ville à τ = 2 | différence | intervalle (500 rééchantillonnages) |
  |---|---|---|---|---|---|
  | 1,0 et 0,3 | 0,208 | 0,092 | 0,149 | +0,058 | [0,033 ; 0,082] |
  | 1,5 et 0,3 | 0,116 | 0,092 | 0,167 | +0,075 | [0,046 ; 0,102] |
  | 2,0 et 0,4 | 0,104 | 0,075 | 0,173 | +0,098 | [0,081 ; 0,129] |

  L'effet injecté monte Ville **plus** que les marges ne la montent à τ = 0 : aucun faux audit sur ces mondes.

**Point 4 : mélange à pas fixé** (`sortie-verif-cv9-pas-fixe-v1.json` ; 12 sondes, E = 60, 5 mélanges par sonde, masques
dispersés).
- Les marges par pas et le masque sont gardés, à chaque pas et à chaque mélange, dans les trois mondes.
- **Dérive linéaire en t (0,3 par pas), sans effet épisode** :
  - r₀ vaut −0,050 à l'origine (avec des masques dispersés, la dérive biaise r₀ vers le bas, comme le dit CV5-4), −0,046 sur le
    pas fixé et 0,005 sur le mélange : **la dérive survit au mélange à pas fixé**, pas au mélange complet ;
  - Ville vaut 0 sur les réelles, 0,003 sur le mélange et 0 sur le pas fixé ;
  - D′ = 0, donc « réelles moins pas fixé ≈ 0 » tient. D = −0,003, donc « réelles moins mélange complet > 0 » ne tient pas :
    une dérive de moyenne élargit les marges poolées du mélange complet. Les contre-lectures v6 à v8 l'avaient vu, et l'arbre
    en tient compte, puisqu'une dérive ne fabrique pas un faux « dépendance ».
- **Dépendance r₀ = 0,3, sans dérive** :
  - r₀ vaut 0,331 à l'origine, 0,001 sur le pas fixé et −0,001 sur le mélange : la dépendance est détruite ;
  - D vaut 0,045 et D′ 0,047.
- **Ni l'un ni l'autre** : D = −0,003, D′ = −0,005.

**Point 5 : gardes.**
- `--test-gardes` sort **quinze entrées**, soit quatorze gardes et `correlation_saine` = 0,171 (`sortie-refus-mode-reel-v9.txt`,
  à la fin). Le décompte de l'en-tête (cinq sains, quatre artefacts de calcul, trois de chargement, E minimal, corrélation
  constante) est exact.
- `verifier_scores_invalides` est appelée **705 fois** pendant un `main()` en mode réel sur le fichier de la répétition, soit
  5 sondes × 141 passages (`sortie-verif-cv9-gardes-v1.json`). Elle est donc sur le chemin réel (script, ligne 199).
- Le mode réel refuse, vérifié en lançant (`sortie-refus-mode-reel-v9.txt`, aucun octet écrit sur la sortie standard) :
  - `--effectifs-seulement` sans empreinte, avec une empreinte vide ou avec une empreinte fausse ;
  - `--tirages 5` et `--bootstrap 300`, avec et sans `--effectifs-seulement` ;
  - l'absence de `--commit` (ou un commit vide), de `--sondes-reelles` ou de `--sondes-placebo` ;
  - des effectifs faux ;
  - `--reel` avec `--synthetique`.
- Le cas sain passe : 807 octets, identiques à l'octet aux effectifs déposés (vérifié par `cmp`). Les effectifs sont donc
  déterministes, ce qui compte pour CV9-2 (a).

**Point 6 : chiffres cités.**
- Tous ceux que j'ai recalculés sont conformes : 0,395 ; 0,0725 ; 0,077 ; 2/40 ; K = 39 ; rang 38 ; ceux de la table v8
  (point 3, plus Ville à τ = 0 : 0 ; 0,033 ; 0,083 ; 0,133 ; Ville à τ = 2 : 0,138 à 0,152 ; M2 bis : +0,138 ; +0,104 ; +0,065 ;
  +0,019) ; ceux de l'en-tête (« quinze entrées », « six audits », « six refus dont les trois propres au mode réel »,
  « 3 sondes réelles, 2 placebo, E = 60 ») ; « environ 30 minutes » (ma répétition : 5 sondes en 29 secondes à l'étape (2),
  cohérent avec les 4,2 secondes par sonde mesurées par la contre-lecture v8).
- Les empreintes de l'en-tête correspondent aux fichiers, et tous les compagnons existent, sauf celui du préenregistrement
  (normal).
- Le texte ne contient aucun « ⟨…⟩ ». Le seul espace réservé est dans la note produite par la rédaction (« ⟨À ÉCRIRE … ⟩ »), et il
  est voulu.
- Un chiffre du dépôt ne renvoie à rien sur disque : l'empreinte `b10f2c11…` citée par la note de répétition déposée (CV9-4).

**Point 7 : ce que je n'avais pas vu venir.**
- **Le mode de lancement** (CV9-1).
- **La garde levée par sa propre procédure** (CV9-2).
- **Pour information, sans constat** : la répétition tombe en (1) avec Ville à 0,050, soit 3 alertes sur 60 au plus pour la
  sonde médiane, alors que bb(D) = 0,012 > 0. Avec E = 60 et un seul tirage à τ = 0, la feuille (1) se joue à une alerte près.
  C'est voulu, puisque le Seuil lit la médiane ponctuelle, mais Lazar peut vouloir savoir que (1) et (3)/(4) sont séparées
  par un seul épisode.

## 3. Constats

### CV9-1 : le lancement prescrit, `nohup … &`, est celui que l'environnement arrête, et aucun délai n'est écrit (moyen ; reste de CV8-1)

- **Où** :
  - Plan d'analyse, lignes 250 et 251 : « le tout par `nohup bash commandes-lecture-reelle-v9.sh <commit du scellement> >
    journal-lecture-reelle-v9.log 2>&1 &` (≈ 30 à 40 minutes) » ;
  - en-tête, lignes 46 et 47 : « lancement en arrière-plan » ;
  - séquence, lignes 4 à 6 ;
  - Liste d'arrêt, lignes 287 et 288 : une interruption = version nouvelle.
- **Problème** :
  - La séquence sera lancée par un agent de cette lignée, dans l'environnement de Claude Code. La documentation de l'outil
    d'exécution de cette session le dit en toutes lettres : une commande lancée en arrière-plan **par l'outil**
    (`run_in_background`) continue après la fin de la réponse, jusqu'à sa fin ou à son délai ; **un processus que le shell
    détache lui-même (`nohup`, `&`) est d'ordinaire arrêté quelques minutes après la réponse**.
  - L'étape (2) dure environ 30 minutes, et 10 de plus si E ≠ 60. Il suffit que l'agent rende la main une fois (une passation,
    une question à Lazar) pour que l'exécution soit coupée.
  - La v9 fait de cette coupure une version nouvelle : un écart à dire et une v10, sans qu'aucun résultat ait été vu.
  - Le délai que demandait CV8-1 (au moins 90 minutes) n'est écrit nulle part. Or le délai par défaut de l'outil en arrière-plan
    est de 30 minutes, à peine celui de l'étape (2).
- **Correction** :
  - Plan d'analyse et en-tête de la séquence : « lancé par l'outil d'exécution en arrière-plan (`run_in_background`), avec un
    délai de 7 200 000 ms (deux heures, le maximum), sans `nohup` ni `&` ; la commande est
    `bash commandes-lecture-reelle-v9.sh <commit> > journal-lecture-reelle-v9.log 2>&1` ; un délai atteint est une
    interruption ».
  - Rien d'autre ne change : la séquence et ses gardes restent telles quelles.

### CV9-2 : la garde du `.partiel` est levée par le renommage que la séquence prescrit ; la table et les étapes (3) et (4) n'ont pas de procédure (mineur ; reste de CV8-1)

- **Où** :
  - séquence, ligne 31 : `[ -e sortie-reelle-v9.json.partiel ] && … exit 5` ;
  - lignes 8 à 10 : « l'auteur renomme le `.partiel` en `sortie-reelle-v9-interrompue-N.json.partiel` » ;
  - lignes 43 et 44 : la table en `.partiel` ;
  - Liste d'arrêt, lignes 287 et 288.
- **Problème** :
  - (a) Une fois le `.partiel` renommé comme prescrit, les lignes 30 et 31 passent (code 0, `sortie-garde-partiel-v1.txt`).
    Rien d'autre n'arrête alors une **seconde exécution v9** : les effectifs se réécrivent à l'identique, `sceller` est
    idempotent, et l'étape (2) repart. La garde qui tient l'unique exécution (R1) ne tient donc que tant que l'auteur ne suit
    pas la procédure de la séquence elle-même. Le texte l'interdit, mais la garde ne le fait pas.
  - (b) Une interruption pendant la table (E ≠ 60) laisse `table-m2bis-m4-v8-E<E>.json.partiel`, que rien ne garde. Une relance
    v9 passe en silence, alors que la Liste d'arrêt fait de tout `.partiel` laissé par la séquence une version nouvelle. Le
    problème est le même pour une interruption entre l'étape (1) et le scellement des effectifs.
  - (c) Une interruption pendant (3) ou (4), avec la sortie déjà scellée, bloque toute relance (code 3). Or rien ne dit si (3)
    et (4), qui ne lisent aucune donnée, peuvent être relancées seules sur la sortie scellée.
  - (d) Un `.partiel` non vide (coupure pendant l'écriture JSON finale) peut contenir des taux. Rien ne dit qu'il ne s'ouvre pas.
- **Correction** :
  - Ligne 31 : refuser tout fichier qui commence par `sortie-reelle-v9` (par exemple
    `compgen -G 'sortie-reelle-v9*' > /dev/null && exit 5`). Ou mieux, créer dès l'étape 0 un témoin
    `execution-reelle-v9.commencee` (avec `set -o noclobber`), jamais effacé, et refuser s'il existe. Cela couvre (a) et (b).
  - Liste d'arrêt : « après une interruption en (3) ou (4), ces deux commandes seules sont relancées sur la sortie scellée,
    dit » (ou l'inverse, dit) ; « un `.partiel` ne s'ouvre pas : on consigne sa taille et son empreinte ».
  - Exercer la garde par un artefact déposé (R5).

### CV9-3 : deux restes de CV8-3 et CV8-4 dans le texte (mineur)

- **Où** :
  - tableau des prédictions, ligne 132, colonne « réfutation » de M2 bis ;
  - critère de (2a), ligne 272 ;
  - Seuil, lignes 210 et 211 ;
  - lecture v5, lignes 118 à 121.
- **Problème** :
  - La ligne 132 ne dit pas la réfutation du Seuil (r₀ < 0,5 et borne haute ≤ 0) ni qu'elle est un audit qui suspend. CV8-3
    le demandait « dans les deux cas ».
  - Le critère de (2a) affirme « la structure n'étant pas établie » même quand la réserve (bb(D′) > 0) dit le contraire.
  - La lecture pose cette réserve aussi en (2b), ce que le Seuil ne dit qu'en (2a). C'est prudent, mais le texte et le code
    divergent.
- **Correction** :
  - Ligne 132 : « réfutée si r₀ < 0,5 et borne haute ≤ 0 → audit R4 de cohérence (suspend) ; « hors table » si l'écart dépasse
    0,05, rapporté ».
  - Ligne 272 : « la structure n'étant pas établie par D (réserve si D′ l'établit) ».
  - Seuil, ligne 210 : placer la réserve au nœud (2), pour (2a) et (2b), comme le fait la lecture.

### CV9-4 : la rédaction fige encore la date et l'instance, déduit « répétition » du seul scellement, et la note n'est pas scellée par la séquence (mineur ; reste de CV8-5)

- **Où** :
  - `rediger_note_lecture_v3.py`, lignes 35, 39 à 45 et 49 ;
  - séquence, lignes 61 à 63 ;
  - en-tête du texte, lignes 51 à 53 ;
  - `note-lecture-mecanique-v9-repetition.md`, ligne 3.
- **Problème** :
  - (a) « instance du 27 octobre 2026 », « servie par Fable 5.1 » et « le 28 octobre » restent en dur. Une exécution le
    29 octobre, ou servie par un autre modèle, écrirait une provenance fausse. CV8-5 (b) demandait de ne pas figer la date.
  - (b) Le statut se lit sur le compagnon du préenregistrement seulement. Sur une copie scellée par moi, une répétition écrit :
    « Préenregistrement **scellé** (compagnon vérifié) … Sortie réelle … **Une seule exécution réelle** (R1) »
    (`note-apres-scellement/note-repetition-apres-scellement.md`). Une répétition refaite après le scellement, utile avant le
    lancement, produirait donc une note qu'on ne distingue de la vraie que par le suffixe de son nom et par le commit
    `repetition-generale`.
  - (c) La séquence ne scelle pas la note mécanique (étape (4)), que la note de lecture doit reprendre « telle quelle ». La
    reprise ne peut donc pas être vérifiée par empreinte (R6). Le texte dit « déposés et scellés » : la note de répétition a
    été scellée à la main.
  - (d) La note de répétition déposée cite le préenregistrement `b10f2c11…`, un brouillon de la v9 qui n'est pas sur disque.
    La v9 sur disque est `9206956b…`. La répétition a donc été faite avant les dernières retouches du texte. Le code est le même,
    et la répétition vaut pour lui, mais la provenance déposée renvoie à un fichier absent.
- **Correction** :
  - La séquence passe `--date "$(date -u +%F)"`, et la rédaction n'écrit plus l'instance ni le modèle en dur : elle les prend en
    argument.
  - La rédaction reçoit le mode (`--repetition`, que la séquence passe quand `COMMIT=REPETITION`) et écrit alors « RÉPÉTITION —
    aucune donnée réelle » en tête, quel que soit le scellement. Elle n'écrit « Une seule exécution réelle » qu'hors répétition.
  - La séquence scelle `note-lecture-mecanique-v9.md` à l'étape (4).
  - Refaire la répétition sur le texte final (ou dire, dans l'en-tête, qu'elle a été faite sur le brouillon `b10f2c11…`).

### CV9-5 : restes (mineur)

- **Docstrings** :
  - `lecture_mecanique_v5.py`, ligne 1 : « seuils gelés du préenregistrement v8 (… v9) ». Écrire « v9 ».
  - `essai_lecture_mecanique_v5.py`, lignes 2 et 3 : la liste des audits omet M2 bis réfutée, que le code exerce (ligne 89).
- **Branche E ≠ 60** : l'en-tête (ligne 53) renvoie à la contre-lecture v8 pour cette branche. Mais celle-ci a exercé la
  séquence v8, et la v9 a changé cette branche (table en `.partiel`, puis renommée). Ma répétition à E = 52 l'exerce (section 2,
  code 0) : ses sorties peuvent être citées à la place.
- **Remarque, sans correction nécessaire** : la lecture saute la vérification du placebo si le bloc `placebos` est vide
  (lignes 170 et 173). C'est sans effet en mode réel, où le script exige 400 placebos.

## 4. Mes scripts et sorties

Tout est dans ce dossier. Chaque script et chaque sortie a un compagnon `.sha256`. Les copies du dossier ne reçoivent un
compagnon que pour les fichiers que j'y ai produits.

| fichier | contenu |
|---|---|
| `scripts/verif_cv9_v1.py` | parties `arbre` (64 combinaisons, étiquettes, bornes, r₀, réserve en (2a) et (2b), audits), `pas_fixe`, `gardes` (compteur d'appels), `m2bis` (faux blocage sous marges lognormales) ; script v8 et lecture v5 importés sans modification ; graines `SeedSequence(2810202609, spawn_key=(partie, …))` |
| `sortie-verif-cv9-arbre-v1.json`, `sortie-verif-cv9-pas-fixe-v1.json`, `sortie-verif-cv9-gardes-v1.json`, `sortie-verif-cv9-m2bis-v1.json` (et leurs `.err`) | leurs sorties |
| `scripts/refus_mode_reel_cv9_v1.sh` → `sortie-refus-mode-reel-v9.txt` | refus du mode réel et `--test-gardes` (quinze entrées) ; fichiers du test dans `gardes-cv9/` |
| `scripts/garde_partiel_extraite_v1.sh` → `sortie-garde-partiel-v1.txt` | lignes 30 et 31 de la séquence, extraites telles quelles, sur cinq états du dossier (`garde-partiel/`) |
| `essai-lecture-mecanique-v5-reproduit.json` (et `.err`) | essai brut de la lecture v5 reproduit à l'octet |
| `copie-dossier/`, `repetition-rejouee-v9.log` | répétition rejouée : effectifs, sortie, lecture et note `-repetition` |
| `copie-interruption/`, `interruption-v9.log` | répétition interrompue à l'étape (2) : `.partiel` de 0 octet, code 143 |
| `note-apres-scellement/` | copie scellée du préenregistrement et note de répétition rédigée après le scellement (CV9-4 (b)) |
| `scripts/ecrire_npz_E52_v9.py` → `donnees-E52/synthetique-E52.npz` | fichier au format réel où E = 52 |
| `copie-dossier-E52/`, `repetition-E52-v9.log`, `journal-heures-E52.txt` | séquence v9 en répétition à E = 52 : table refaite, scellée, lue |
| `donnees-repetition/` | copie du `.npz` de la répétition (`447dc136…`) |

Empreinte de ce rapport : dans `rapport-contre-lecture-mesure-unanime-v9.md.sha256`, à côté (un fichier ne peut pas contenir
sa propre empreinte).

Fin : 2026-10-28 03:08:38 UTC (`date -u`, relevé dans un appel séparé avant l'écriture de cette ligne).
