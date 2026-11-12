# Contre-lecture de la chaîne de la course de T0.6 (rendus 5, 6 et 7 de la fille 10) — v1

- **Contre-lecteur** : Claude Opus 5.5 (identifiant `claude-opus-5-5`), sous-agent neuf au sens de la règle R2 (tout préenregistrement est relu par un agent qui ne l'a pas écrit). Je n'ai écrit aucune des pièces lues. Je n'ai ni lu ni listé l'arbre `/home/user/wt-cl-course-v2` laissé par le contre-lecteur arrêté.
- **Consigne** : `docs/notes/g0-deux-semaines-v1/contre-lecture-t06-course-v2-consigne-v1.md` ; empreinte vérifiée par `sha256sum` avant toute lecture : `dcb2179970f5085257cb88f6eed77619ca919f7b526a3ce67fb8df2f4e6cc21a`, conforme.
- **Heures** (`date -u`) : début 09:07:08Z ; fin : voir la dernière section.
- **Arbre** : `/home/user/wt-cl-course-v2-b`, branche locale `prep/contre-lecture-t06-course-v2-b`, au commit `8cb539f9b7ecd20fab133bfffb590ca8e1fdfc63`. J'écris seulement sous ce dossier. Les pièces ont été lues par `git show <commit>:<chemin>`.
- **Comptages et essais** : faits dans deux arbres détachés, ceux des commits `7822a65b` et `c01d29ea`, créés dans mon bloc-notes. J'ai retiré celui de `c01d29ea` après le comptage : le disque de la machine était plein (378 Mo libres à 09:13Z).
- **Interpréteurs** :
  - pour les essais du programme : `/home/user/venv311/bin/python3.11`, lien vers `/usr/bin/python3.11`, Python 3.11.18, avec numpy 2.4.6, torch 2.14.1+cu130, transformers 5.18.0 et pytest 9.1.1 ;
  - pour mes scripts : `/home/user/controle-ia-travail/.venv/bin/python -I` (Python 3.13.18).
  Chaque commande pytest avait un `--basetemp` neuf, et un `TMPDIR` neuf pour le banc de mutations.
- **Interdits respectés** : aucun commit ni aucune poussée ; aucun fichier `.sha256` ; aucune clé ni variable d'environnement lue ; aucune commande `vastai` ; aucune dépense. Deux lectures réseau seulement, toutes deux `git ls-remote` en lecture des noms de branches. Aucune pièce de la fille 10 n'a été modifiée. Aucun résultat d'E3 bis n'a été lu au-delà de son compte rendu.

## Termes employés
- **T0.6** : la course qui fabrique deux organismes par adaptateur de rang faible (un saboteur et un témoin), puis enregistre leurs activations à plusieurs doses. Elle est prévue le 11 novembre, plafond de 200 USD (GO-2026-11-02-28).
- **GO** : ligne du registre `registres/go.md` qui consigne un accord de Lazar.
- **E3 bis** : la répétition générale de la chaîne, sur carte graphique (A100), le 8 novembre. Elle a joué la chaîne v11 : amorce v9 et liste figée v1.
- **E3-n** : point n de la grille de vérification d'E3 bis, dans l'ordre scellé `docs/procedures/ordre-fille-6-t06-e3bis-v3.md`. Deux points servent ici :
  - E3-3 : mémoire et secondes par pas de la distillation ;
  - E3-6 : garde d'équivalence au 99ᵉ centile sur un lot à dose 1.
- **Amorce** : le script qui tourne sur l'instance louée : clonage, installation, suite d'essais, run, bras B, arrêt.
- **Lanceur** : le script local. Il contrôle, imprime la commande de création et surveille.
- **Liste figée** : la liste des fichiers d'essais joués sur l'instance. Son empreinte est écrite en dur dans l'amorce.
- **Bras B** : contrefactuel de contexte de l'audit de fuite. C'est une annexe jouée après la course, qui ne la bloque jamais.
- **G4** : sa garde d'identité.
- **W** : la sonde figée qu'il relit.
- **Couple** : correction textuelle `{"id", "ancien", "nouveau"}`. Chaque « ancien » doit se trouver une seule fois dans la pièce visée.
- **R12** : règle « versions dans les noms : une version nouvelle prend un nom nouveau ».
- **R6** : règle « tout chiffre renvoie à un chemin et une empreinte ».

## Verdict par pièce

| pièce | verdict | couples | motif en une ligne |
|---|---|---|---|
| Chaîne v12 : lanceur v12 `8b91be97…`, amorce v10 `69b669e1…`, liste figée v2 `417f637e…`, banc v5 `c2e3efe3…`, essais neufs | **scellable** | 0 | Comptages exacts : 1 914 et 1 878. Les essais neufs passent : 347 sur 347. Banc : 21 mutations tuées sur 21. Mes deux mutations du lanceur sont tuées. La garde « ≠ 1914 » arrête avant le run. Aucun changement de code n'est recommandé. |
| Ordre de la course v2, brouillon `9cdffc7b…` | **scellable après couples** | 4 | Il manque le préalable « E3-6 réglé », que R-1769 exige avant la course (bloquant). Les attendus de la distillation manquent (moyen). Le commit demandé ne correspond pas à ce que vérifie `controles` (moyen). Le reste est conforme. |
| Devis v3 `10965742…` | **scellable après couples** | 2 | Les calculs sont justes aux arrondis près. Le débit de la H200 NVL est bien écrit comme une réserve, mais le devis ne dit pas qu'un débit moindre de 0,9 % suffit à faire passer P4' au-dessus de 200 USD (moyen). Le devis v2 cité n'a ni empreinte ni commit (mineur). |
| Candidat 12, révision 2 `0d6bf1c4…` | **scellable après couples** | 8 | W1 à W4 sont exacts, et la dérivation de 1914 est écrite avec sa réserve. Mais le contrôle de conformité du dépôt (`controle_ia.prereg`) le refuserait même rempli : section « Hypothèses » au pluriel, et 5 mentions historiques de `<<TESTS_ATTENDUS_T06>>` (moyen). Quatre empreintes caduques de la chaîne v11 restent sous la règle « tout écart : nœud » (moyen). |
| Addendum du bras B v3 `2ec90141…` | **scellable après couples** | 1 | Il dit exactement GO-2026-11-08-01 (0,3, borne incluse, lecture stricte) et rien d'autre. Seule différence avec l'ordre et R-1761 : il fait sceller le texte par « Lazar », au lieu de la session mère (mineur). |

**Bloquants : 1.** C'est le constat neuf N1 : le point E3-6 d'E3 bis n'est pas réglé, et l'ordre ne l'exige pas avant la création. Le régler ne coûte rien : il suffit de lire les fiches d'épisodes de la branche `essai/t06-e3bis-v1` (couples O1 et O2).

## Constats classés

### Bloquant
- **N1 — bloc `equivalence_99e_centile` absent pour les six états** (constat neuf ; détail plus bas).
  - **Le défaut** : l'extracteur d'épreuve v1 lit une clé que la chaîne n'a jamais écrite. Son « absent » ne prouve donc rien sur la garde.
  - **Ce qu'on ne sait pas** : si E3 bis a contrôlé ne serait-ce qu'une action. La probabilité qu'aucune ne l'ait été vaut environ 0,44.
  - **Ce qui manque** : l'ordre v2 ne fait pas régler E3-6 avant la création, alors que R-1769 l'exige.
  - **Correction** : couples O1 et O2 (préalable 7 et marqueur `<<REGLEMENT_E3_6>>`).

### Moyens
- **N2 — 45 pas déclarés, 4 entrées par adaptateur au journal** (constat neuf ; détail plus bas). Par le code, 4 entrées correspondent exactement à 3 époques, et non à 4 pas. Les adaptateurs ont fait 45 pas si chaque adaptateur avait ses 15 transcriptions. L'ordre ne fait relever ni ce nombre ni les époques à la course. Couple O3.
- **M1 — commit de la course (ordre, § 2.1)**.
  - **Ce qu'exige l'ordre** : `COMMIT`, « ancêtre de `refs/remotes/origin/prep/t06-course-v12` », et à l'étape 1 il passe `T06_BRANCHE_CODE`.
  - **Ce que fait `controles` du lanceur v12** (course, l. 115-142) : il ignore `T06_BRANCHE_CODE`, qui ne sert qu'à `controles-epreuve` (l. 147). Il retrouve lui-même S, le dernier commit de l'histoire extraite qui ajoute `prereg/T0.6-organismes-v0-v1.md.sha256` (`commit_s`, l. 108). Il exige que S soit ancêtre de `origin/main` (l. 123) et l'imprime en `S=` (l. 142). L'ordre attend `S=<COMMIT>`.
  - **Le risque** : la condition n'est satisfaisable que si la mère choisit un commit ancêtre des deux branches. Sinon, l'arrêt au préalable 1 tombe le jour de la course.
  - **Correction** : couple O4, qui écrit ce que vérifie le lanceur.
- **M2 — devis v3 : effet d'un débit moindre de la H200 NVL**.
  - **Ce qui est écrit** : la réserve est présente deux fois.
  - **Ce qui manque** : le devis ne chiffre pas la sensibilité. Avec les heures exactes (17,98 h et non 17,9), P4' (le pire cas du devis à la borne de 4,70 USD/h) vaut ≈ 198,5 USD, donc une marge de ≈ 1,5 USD. P4' dépasse 200 USD dès que la H200 NVL met 0,9 % de temps de plus que l'hôte lent de P1' ; P3' (le repli sur H200 NVL, hôte lent) dès 8,9 %.
  - **La conséquence** : la seule garde est alors l'arrêt à 200 USD cumulés. L'instance serait détruite avant la fin du run, et la course perdue pour environ 200 USD.
  - **Correction** : couple D1.
- **M3 — candidat 12 r2 refusé par `controle_ia.prereg.problemes`**. Ce contrôle est celui de `sceller_prereg` et de `exiger_prereg_scelle`. J'ai simulé le remplissage des quatre marqueurs restants avec des valeurs de la bonne forme. Le contrôle rend alors deux problèmes : « section absente : Hypothèse », parce que le texte titre « ## Hypothèses » ; et « marqueurs de gabarit restants : <<TESTS_ATTENDUS_T06>> », à cause des cinq mentions historiques aux lignes 3, 135 et 813. Après les couples W5 à W10, il n'en rend aucun, et les huit citations lues par `controles` restent uniques. La chaîne de T0.6 elle-même n'appelle pas ce contrôle : le défaut ne mord que si la mère scelle par `sceller_prereg`.
- **M4 — empreintes caduques de la chaîne v11 dans le candidat**.
  - **Ce qui est écrit** : le paragraphe de la chaîne v11 (l. 195) annonce « à recalculer au commit cité, tout écart : nœud ».
  - **Le défaut** : il cite le lanceur v11 `a0aea3d3…`, l'amorce v9 `be2183b0…`, la liste v1 `edc1c70e…` et les exclusions v1 `3db58d1d…`. Ce sont des versions des commits `999b6f07` et `6fb0aa61`, antérieures au rendu 4 et déclarées caduques par la contre-lecture de la v11, v2. Au commit de la course, ces fichiers valent `e134419b…`, `6a6897ce…`, `562b65fa…` et `5fc2d5db…`. La règle du texte ferait de cet écart un nœud au scellement.
  - **Correction** : couple W11, qui déclare ce paragraphe historique.

### Mineurs
- **m1** : l'addendum v3 dit « que Lazar scellera », l'ordre v2 dit « scellé par la mère », et le candidat 12 r2 dit « à sceller par Lazar ». R-1761 dit « (mère, ou nouvelle mère) ». Couples A1 et W12.
- **m2** : le devis v3 renvoie au devis v2 par son seul chemin. Ce fichier n'est ni sur `main` ni parmi les ancêtres de `8cb539f9`. Il existe sur la branche distante `prep/t06-candidat8-v1`, commit `c99d41e`, empreinte `f6f6195c…` selon R-1707. Couple D2.
- **m3** : arrondis du devis v3, sans effet sur le verdict :
  - 17,9 h au lieu de 17,98 h ;
  - calcul de l'A100 : 13,6 et non 13,7 ;
  - calcul de la H200 NVL : 41,3 à 72,3 et non 41,5 à 72,5 ;
  - attendu sur H200 NVL : 45,4 à 77,3, écrit « ≈ 46 à 78 ».

  Le stockage de l'attendu est compté à 0,0417 USD/h, alors qu'E3 bis a payé 0,0694 USD/h : 5,0 USD sur 72 h au lieu de 3,0, soit un attendu sous-estimé d'environ 2 USD. Le pire cas compte à la borne de 0,08 et n'est pas touché. Pas de couple, sauf la phrase de D1 sur les heures exactes.
- **m4** : deux empreintes historiques du candidat ne sont plus celles des fichiers : `tests/test_t06_cibles_invisibles_v1.py` (`0eada746…`, aujourd'hui `b7409f04…`, exclu de la liste v2) et le brouillon d'ordre d'E3 v5 (`f00e143d…`, aujourd'hui `d05ec5e9…`). Elles sont dans des paragraphes de candidats anciens. Pas de couple.
- **m5** : le commentaire de version v11 du lanceur v12 (l. 4) a été réécrit en « cite l'amorce v10 », alors que la v11 citait l'amorce v9. C'est sans effet. Pas de couple : le changer changerait l'empreinte citée.
- **m6** : la lecture stricte du bras B compare la carte et les versions de torch et de transformers, mais pas le pilote, qui valait 595.91.07 au rejeu. Sur une A100 de même modèle munie d'un autre pilote, un écart au bit arrêterait G4 sans défaut réel. C'est une limite non déclarée pour l'A100, qui ne touche que l'annexe. Pas de couple : la règle est celle de Lazar.
- **m7** : l'ordre accorde 100 minutes de silence pendant le bras B. La borne réelle est de 5 785 s : 2 400 s pour le module, 10 s pour l'arrêt forcé, 1 500 s pour le verrou, 3 × 600 s pour les poussées, puis 15 et 60 s d'attentes. La marge est donc de 215 s. Conforme.

## Preuves, dans l'ordre de la consigne

### 1. Nombre d'essais attendu, 1914 (R-1763)
- **Commande** : `/home/user/venv311/bin/python3.11 -I -B -m pytest --collect-only -q -p no:cacheprovider --basetemp=<neuf> $(cat scripts/tests-cibles-t06-vN.txt)`, jouée dans chaque arbre détaché.
  - **Liste v2** (commit `7822a65b`, 83 fichiers, `417f637e0db2657e…`) : « 1914 tests collected in 21.20s », code 0.
  - **Liste v1** (commit `c01d29ea`, 81 fichiers, `562b65facf1bcbf7…`) : « 1878 tests collected in 16.28s », code 0.
  - **Égalité attendue** : vérifiée, 1 914 et 1 878.
- **Décomposition de l'écart de +36** :
  - bras B v4 : +44 ;
  - bras B v3 : −32 ;
  - banc v5 : +9 ;
  - essais de la course v12 : +15.

  Les dix copies `test_t06_v11_*` deviennent `test_t06_v12_*`, avec les mêmes comptes : 80, 14, 19, 14, 16, 27, 23, 27, 6 et 32. Fichier : `sorties/comptage-essais-listes-v1-v2-v1.txt`.
- **L'amorce v10 compare le nombre exact** :
  - En mode course, elle lit `ATTENDUS` par `lire_unique "Tests attendus"` et refuse ce qui n'est pas un entier (l. 376-377).
  - Elle joue pytest sur les seuls fichiers de la liste. Si un essai échoue, elle arrête avec « tests en échec » (l. 483-485).
  - Elle exige ensuite que la dernière ligne vérifie `^$ATTENDUS passed(, [0-9]+ warnings?)? in [0-9.]+s( \(…\))?$`, sinon elle arrête avec « nombre de tests » (l. 487-489). Tout cela se passe avant le lancement du run (l. 494).

  Une ligne comme « 1913 passed, 1 skipped » est donc refusée ; une mention d'avertissements est acceptée.
- **Dépendances à l'environnement** : les trois fichiers jamais joués sur une instance (bras B v4, banc v5, course v12 : 68 essais) n'en ont aucune. Les deux conditions de saut de la liste sont remplies sur l'image : `python3.11` présent, module `trace_lite_conduite_v1` présent.

### 2. Bras B v4 conforme à GO-2026-11-08-01
- **Tolérance** : `TOLERANCE_SCORE = 0.3` (l. 71) et `ok = ecart <= TOLERANCE_SCORE` (l. 325) : borne incluse.
- **Lecture stricte** : `identite_exigee_au_bit` (l. 299-304) exige la même carte (`torch.cuda.get_device_name(0)`) et les mêmes versions (métadonnées des paquets) que le rejeu de R1 v4. Ce rejeu a été fait sur « NVIDIA A100-SXM4-80GB » avec torch « 2.14.1 » et transformers « 5.18.0 » (`runs/20261105-021737-r1-v4-rejeu-reel/manifeste.json`, `diag/…/rejeu-activations.json`). Dans ce cas, `ok = egal` au bit, quel que soit le score (l. 320-321). La version de torch lue est « 2.14.1 », sans le « +cu130 » de `torch.__version__`, comme au manifeste du rejeu : la comparaison est donc cohérente.
- **Différence entre v3 et v4** : notes, nom du module, `NOM_SORTIE`, `TOLERANCE_SCORE` et son commentaire, nom de la commande. Rien d'autre.
- **Essais rejoués** : `tests/test_bras_b_v4.py` (44 essais) passe, dans la passe de 103 essais réussis.
- **Banc v5** : « 21 mutations tuées sur 21 (témoin non muté réussi) », de 09:17:15Z à 09:24:22Z, code 0 (`sorties/essais-et-banc-v1.txt`).
- **Addendum v3 comparé à la v2** :
  - Ce qui change : le statut, le code décrit (v4), la lecture stricte décidée, 0,3 borne incluse, la justification réécrite pour 0,3 et le nom de la sortie scellée. Rien d'autre.
  - Empreintes de la mesure (`0bc1f89c…`, `4326bca2…`) : conformes au commit `84a62edd`.
  - Il dit donc exactement GO-2026-11-08-01, et rien d'autre. Seul écart avec les autres pièces : qui scelle (m1).

### 3. Lanceur v12 et amorce v10
- **Différences entre le lanceur v11 et le lanceur v12** (`diff`, 20 ajouts et 18 suppressions) :
  - en-tête v12 ;
  - `A=scripts/amorce_instance_t06_v10.sh` ;
  - messages « amorce v10 », « controles t06 v12 », « surveillance v12 » ;
  - renvois à `lancer_t06_v12.sh` dans la commande de création, `apres-creation` et le rang suivant ;
  - la ligne neuve 226 (validation de `T06_TESTS_ATTENDUS`).
- **Différences entre l'amorce v9 et l'amorce v10** : un commentaire, la bannière v10 (l. 67), le module par défaut `controle_ia.audit_fuite_r1_v4.bras_b_v4` (l. 421), et la liste v2 avec son empreinte écrite en dur `417f637e…` (l. 469), égale à celle du fichier. Ce sont bien les « trois lignes » annoncées.
- **Validation `^[0-9]*$`** : elle est à la l. 226, dans `creation`, avant la commande. Pour la course, la valeur n'est pas transmise : elle ne sert qu'aux épreuves ; l'amorce lit « Tests attendus » dans le préenregistrement.
- **Recontrôle des GO à la création** : GO-2026-11-02-28 avec 200 USD (l. 197), et GO-2026-11-06-01 avec 5 USD pour E3 bis (l. 198).
- **Mes deux mutations** (`scripts/mutations_lanceur_v12_v1.py`, contre `tests/test_t06_v12_course.py`) :
  - L12-A, validation retirée : tuée (1 échec) ;
  - L12-B, recontrôle de GO-2026-11-06-01 retiré : tuée (1 échec) ;
  - témoin : 15 essais réussis ;
  - fichier restauré, empreinte `8b91be97…` conforme.
- **Essais neufs rejoués** : 103 réussis en 135,48 s (bras B v4, banc v5, course, liste, cibles invisibles), puis 244 réussis en 560,33 s pour les neuf autres copies v12. Total : 347 réussis, 0 échec, 0 saut.
- **« motifs=28 »** : `CHEMINS_CLONAGE` compte 28 motifs dans l'amorce v10.

### 4. Ordre de la course v2 (brouillon)
- **Rejeu du générateur** `pieces/generer_ordre_course_v2.py` sur le brouillon v1 : octets identiques (`9cdffc7b…`).
- **Copie des couples** : identique à l'original sur `main` (`67b9c8ea…`).
- **Les 7 couples de la contre-lecture précédente** : chaque « ancien » est trouvé une fois dans la v1, et chaque « nouveau », adapté à la v12, une fois dans la v2. La première phrase du couple 7 est ensuite remplacée par le couple « sortie bras B » du générateur, et c'est juste : le module v4 n'imprime plus l'issue.
- **Valeurs** :
  - « motifs=28 » : 1 occurrence ; « motifs=27 » : 0 ;
  - « 5 800 s » : 1 ;
  - suite à 68 minutes dans le calendrier.

  À E3 bis, il s'est écoulé 1 h 11 min 45 s de la création au premier `PROGRES` ; avec 2 % d'essais de plus, environ 1 h 13. L'ordre écrit « ≈ 1 h 15 ».
- **Garde « ≠ 1914 »** : écrite (ne pas détruire, relever, écrire à la mère).
- **Marqueurs** : exactement `<<COMMIT_COURSE>>`, `<<CONFIG_COURSE>>` et `<<EMPREINTE_PREREG_T06>>`. Après le couple O2, `<<REGLEMENT_E3_6>>` s'y ajoute.
- **Commandes** : seulement `scripts/lancer_t06_v12.sh` (`controles`, `creation auto course|relance`, `surveillance`) et `fenetre_carte_t06_v1.sh` avec le lanceur v12. L'écart sur le commit est traité en M1.
- **Contenus interdits** : ni sortie brute, ni clé, ni chaîne de 64 hexadécimaux, ni JSON d'inventaire.
- **Ce qui manque** : E3-6 (N1) et les attendus de la distillation (N2).

Script : `scripts/verifier_ordre_course_v2_v1.py`.

### 5. Devis v3 (`scripts/recalcul_devis_v3_v1.py`, sortie `sorties/recalcul-devis-v3-v1.txt`)
- **Suite** : 67 min × 1,02 = 68,3 min, soit 1,139 h.
- **Divers** : 1,842 h.
- **Heures de marche** : 12,30 à 17,98 h.
- **Bras B à sa borne** : 5 775 à 5 785 s, soit 1,61 h.
- **Attendu** :
  - A100 : 17,6 à 28,3 USD ;
  - H200 NVL : 45,4 à 77,3 USD.
- **Pire cas recalculé** :

| scénario | aux prix constatés | à la borne de 4,70 USD/h |
|---|---|---|
| P1' (hôte A100 deux fois plus lent) | 56,6 | 56,6 |
| P2' (P1' plus une relance sur A100) | 87,4 | 87,4 |
| P3' (repli sur H200 NVL, hôte lent) | 159,4 | 184,4 |
| P4' (P3' après une erreur de mémoire sur A100) | 173,8 | 198,5 |

  Heures exactes. Avec les heures arrondies du devis (17,9 h) : 184,1 et 198,2. Les valeurs du devis (≈ 57 / 87 / 159 / 173, ≈ 184 / 198) sont justes aux arrondis près.
- **Hypothèse sur la H200 NVL** : « débit égal à celui de l'A100 » est écrit comme une réserve, au poste distillation et aux réserves. L'effet d'un débit moindre est traité en M2 (couple D1). Ce cas n'est pas le plus probable, mais il n'est pas mesuré.

### 6. Candidat 12 révision 2
- **Rejeu du générateur** `appliquer-candidat12-r2-v1.py` sur le candidat 12 (`379328fa…`, vérifié) : octets identiques (`0d6bf1c4…`). La différence entre le candidat 12 et sa révision 2 tient en quatre lignes exactement : W4 (l. 3), W1 (l. 228), W2 (l. 680) et W3 (l. 813).
- **Dérivation de 1914** : écrite à la ligne « Tests attendus », avec sa réserve « la liste v2 n'a pas été relevée sur l'instance ». Mes comptages la confirment.
- **Citations** : sur 146 empreintes complètes citées, 76 désignent un fichier présent à `8cb539f9`. 70 sont égales et 6 diffèrent (M4, m4). Les 14 empreintes du paragraphe de la chaîne v12 sont égales ; les 8 préfixes vérifiables aussi (`sorties/verifier-candidat12-r2-v1.json`).
- **Lectures de la chaîne** : les 8 clés lues par `controles` apparaissent une fois chacune, une fois les marqueurs remplis. La citation de l'amorce a la forme exacte lue par le lanceur. `lire_unique` rend `1914`.
- **Marqueurs encore ouverts** : `<<COMMIT_CODE_T06>>`, `<<EMPREINTES_CODE_T06>>`, `<<EMPREINTE_AMORCE_T06>>` et `<<VALEURS_CITEES_T06>>`. Les 5 mentions résiduelles de `<<TESTS_ATTENDUS_T06>>` sont traitées en M3.

## Constats neufs (adaptation 4)

### N1 — `equivalence_99e_centile` absent pour S100, S25, S50, S75, T100 et dose0 : **bloquant**
- **Où le bloc devait être lu** : l'extracteur `scripts/extraire_mesures_epreuve_t06_v1.py` (l. 54) lit `diag/<run>/episodes-t06.json` → `resultat.etats[<état>]["equivalence"]`.
- **Ce que la chaîne écrit** : `lanceur.jouer_evaluation` (appelé par `lanceur_v5`, l. 276-288) écrit à trois endroits différents :
  - sous `etats[<état>]`, seulement `{adaptateur, dose, empreinte}` (`lanceur.py`, l. 258) ;
  - le bloc d'équivalence, **par fiche d'épisode** : `fiches[k]["equivalence"]`, avec les actions contrôlées, la tolérance, la statistique et les écarts par couche (l. 294-297) ;
  - le contrôle négatif, **par état** : `controles_negatifs[<état>]` (l. 299-305).
- **Pourquoi il manque** : `lanceur.py` (`a3dde550…`), `lanceur_v5.py` (`17efa881…`), `harnais/episode.py` (`79113b49…`) et l'extracteur (`9a67b7b9…`) sont identiques aux commits `c01d29ea`, `7822a65b` et `8cb539f9`. Aucune version n'a jamais écrit ce bloc par état : l'« absent » vient de la construction même de l'extracteur. L'essai de l'extracteur (`tests/test_t06_v4_extraire.py`, l. 30 et 49) passe parce qu'il invente lui-même la clé `etats.dose0.equivalence`. Je l'ai reproduit sur la chaîne jouet (`lanceur_v5`, processeur, sans réseau) : l'extracteur v1 rend « absent » pour les quatre états, alors que chaque fiche porte son bloc (`sorties/reproduire-chaine-jouet-v1.json`, `scripts/reproduire_chaine_jouet_v1.py`).
- **Ce qu'on sait d'E3 bis** :
  - **Ce qui est sûr** : la garde a tourné, en mode « immédiat », sur les actions tirées (`jouer_episodes` → `exiger_gardes`). Un écart au 99ᵉ centile au-dessus de 0,2 aurait arrêté le run. Or E3 bis finit en code 0, sans `arret.json` : aucune action tirée n'a dépassé.
  - **Ce qui ne l'est pas** : le nombre d'actions tirées. Le tirage se fait par paire (tâche, pas), avec un générateur neuf par tâche ; ce sont donc les mêmes paires pour toutes les conditions (l. 266-270). E3 bis comptait 4 tâches × 4 pas = 16 paires, tirées à 5 % : 0,8 paire en moyenne. La probabilité qu'aucune ne le soit vaut 0,95¹⁶ ≈ 0,44. Dans ce cas, aucune action d'aucun état n'a été contrôlée, et l'objet d'E3-6 (la garde au 99ᵉ centile sur un lot à dose 1) n'a pas été observé.
  - **Le contrôle négatif de phase** : il demande au moins 10 actions comparables ; à E3 bis il était au mieux « non concluant ».
  - **À la course** : 64 tâches × 10 pas = 640 paires, environ 32 actions contrôlées par état d'adaptateur. La probabilité qu'aucune ne soit tirée vaut environ 6·10⁻¹⁵.
- **La chaîne v12 le produit-elle et l'exige-t-elle avant la course ?** Non.
  - Elle écrira la même forme (blocs par fiche, rien par état).
  - Elle exige que la garde tienne pendant le run (arrêt sur écart). Elle n'exige pas que la garde ait été exercée.
  - L'ordre v2 ne mentionne pas l'équivalence : 0 occurrence.

  Classé bloquant, parce que R-1769 exige qu'E3-6 soit « à régler avant la course » et qu'aucune pièce ne le porte.
- **Couples qui le rendent obligatoire** (`couples-ordre-course-v2-v1.json`) :
  - **O1** ajoute le préalable 7 « Point E3-6 d'E3 bis réglé avant toute création ». Il exige une ligne du registre des décisions de `main` qui donne, pour chacun des six états, le nombre d'actions contrôlées, le plus grand écart au 99ᵉ centile, la tolérance et la lecture du contrôle négatif, lus dans les fiches. Si aucune action n'a été contrôlée, cette ligne porte la décision de Lazar. Sinon : arrêt et message.
  - **O2** ajoute le marqueur `<<REGLEMENT_E3_6>>` à la liste de ceux que remplit la mère.
- **Lecture proposée** (0 USD, liste blanche, éprouvée sur la sortie jouette) : `scripts/extraire_e3_6_et_e3_3_proposition_v1.py`, à jouer sur la branche `essai/t06-e3bis-v1` (`a5c0e298`). Je ne l'y ai pas jouée : ce sont les données d'E3 bis.
- **Code de la chaîne** : aucun changement recommandé. Un lanceur v6 exigerait une chaîne, une liste et un compte d'essais neufs, à trois jours de la course, alors que les blocs par fiche suffisent.

### N2 — « 45 pas déclarés, 4 entrées par adaptateur » : **moyen**
- **Par le code, ce que contient le journal** : `distiller_transcriptions` (`src/controle_ia/t06/distillation_transcription.py`, l. 109-146) écrit une entrée avant l'entraînement (époque 0), puis une par époque. Pour 3 époques, cela fait 1 + 3 = 4 entrées, avec les clés `epoque` et `perte`. C'est exactement ce qu'a relevé E3 bis.
- **Par le code, le nombre de pas** : l'optimiseur fait époques × ⌈exemples / lot⌉ pas, soit 3 × exemples avec un lot de 1.
- **Ce que l'extracteur appelle des pas** :
  - Son « pas : 4 » compte les entrées du journal.
  - Son « `pas_declares` 45/45 » est le contrôle d'avant le run (`exiger_pas_declares` : nombre déclaré égal au nombre attendu des tâches), et non le nombre de pas faits.
- **Où se trouve le nombre de pas faits** : la chaîne l'écrit sous `distillation-t06.json` → `donnees.<adaptateur>.pas_declares.{pas, conforme_au_declare}`, et l'annonce au journal par `PROGRES … etape=donnees-distillation saboteur_exemples=N temoin_exemples=N`.
- **Démonstration avec le code exact** (`scripts/verifier_pas_distillation_v1.py`, `sorties/verifier-pas-distillation-v1.json`) :
  - 15 transcriptions : 45 appels à `AdamW.step`, journal de 4 entrées ;
  - 14 transcriptions : 42 appels, journal toujours de 4 entrées, `conforme_au_declare` faux, et aucun arrêt.

  La chaîne jouette confirme : `donnees.*.pas_declares.pas` = 6 pour 2 exemples, avec 4 entrées au journal.
- **Réponse sur E3 bis** : les 4 entrées sont exactement celles d'un entraînement de 3 époques, compatible avec 45 pas. Les adaptateurs ont fait 45 pas si et seulement si chacun avait ses 15 transcriptions (aucun épisode dont toutes les actions auraient été exclues). La ligne `donnees-distillation` du journal d'E3 bis le tranche sans ouvrir de résultat ; elle n'est pas au compte rendu de la fille 6.
- **Les secondes par pas d'E3 bis ne valent pas** : `distillation.duree_s` (576 s) est compté depuis le début du run (l. 183 → l. 268). Il comprend le chargement du modèle, le contrôle du format, la génération des 30 épisodes de distillation, l'entraînement des deux adaptateurs et le contrôle d'identité. Les « 12,8 s/pas » et « 6,4 s/pas » du compte rendu ne sont donc pas des vitesses d'entraînement ; ils ne servent pas au devis, qui ne les utilise pas.
- **Ce que la course doit vérifier** (couple O3) :
  - au journal : `saboteur_exemples=160 temoin_exemples=160` (480 pas d'AdamW par adaptateur, ligne L04 du candidat) ;
  - trois lignes d'époque, puis `etape=adaptateur`, pour chaque adaptateur ;
  - les secondes par pas, tirées des heures de ces lignes ;
  - après le scellement, pour le lecteur neuf : `donnees.<adaptateur>.pas_declares` = 480, conforme.

  Aucune garde n'arrête un déficit de pas : il est seulement consigné. Le candidat le traite en réserve (exclusions au-delà de 5 %).

## Fichiers écrits (sous `docs/notes/g0-deux-semaines-v1/contre-lecture-t06-course-v2/`)

| fichier | sha256 |
|---|---|
| `couples-ordre-course-v2-v1.json` (4 couples : O1 à O4) | `e16cfc8846e1cc99394f5d0dfe09d8f1537aa2161496e4475e7b9406a5caaed3` |
| `couples-devis-v3-v1.json` (2 : D1, D2) | `9f9facd9545aab78e0a07799295013f429e02d58898a7b379233a994f588ac38` |
| `couples-candidat12-r2-v1.json` (8 : W5 à W12) | `f094a8046257d9d3f87cc50de626cda5d7a15e27a727961a6a80b7ee254a59df` |
| `couples-addendum-bras-b-v3-v1.json` (1 : A1) | `467f53c9ea070051750358ba8447ee111f96d613090b6ba8fe82a8f36be48253` |
| `scripts/ecrire_et_eprouver_couples_v1.py` (écrit et éprouve les 15 couples) | `05fdf1a5213cb6ce5c27219ad2102f92de03813133abffc82851af72b6c5962a` |
| `scripts/verifier_empreintes_rendus_v1.py` | `17328d390319fb8190759dcb359cca1c8221b46e4d5112b59ce31bcf89398893` |
| `scripts/recalcul_devis_v3_v1.py` | `a2ce90e3fa986cee8a59c26309f48a5f302de5fe31e74536e8045932a1c27424` |
| `scripts/verifier_ordre_course_v2_v1.py` | `17959f16f002bf68e9754b65bb999063ac7451f7c24ef77373163709ddc7271d` |
| `scripts/verifier_candidat12_r2_v1.py` | `c607daecdd333128751119840f92eab29290247a1e454c954f1457ab24e46db8` |
| `scripts/retrouver_versions_citees_v1.py` | `a78fd0c89d3a88281e4a107594ff53d21fa0ff3c99c4edf796fd4ac56d09d8fb` |
| `scripts/simuler_scellement_candidat12_r2_v1.py` | `7899a92c19bb2ed20ae6298548f83216c720dce8652138d5eb27a7dbdbd654c4` |
| `scripts/mutations_lanceur_v12_v1.py` | `c6623bce4b24d48eeb8999131d511ba207dd47a5fee2210d25a36670ca004f36` |
| `scripts/verifier_bloc_equivalence_v1.py` | `0b691943bfb59513c1cb5cab365fd7fefeec74afb2a454bdb6b56f0b98c6674f` |
| `scripts/verifier_pas_distillation_v1.py` | `56417ede95d40cc5341c4a4ba7506261a4ca8d63dcc5a4975f4dbda9d261989c` |
| `scripts/reproduire_chaine_jouet_v1.py` | `f7a698524d496002aa816b47c5539ac1e2a5e0ec12f6dfa830fb785c7c282faf` |
| `scripts/extraire_e3_6_et_e3_3_proposition_v1.py` (lecture proposée, non une pièce de la chaîne) | `acaf648f747751038af1cc8b8c066796d9b237c52492b21121731994d04a7db3` |
| `sorties/` : 15 sorties des scripts ci-dessus, dont les comptages, les essais, le banc, les mutations et la reproduction jouette | — |

Ce fichier lui-même n'a pas d'empreinte ici : la session mère la relève.

## Heures
Début 09:07:08Z ; fin 10:01Z (`date -u`). Les deux arbres détachés de mon bloc-notes (commits `c01d29ea` et `7822a65b`) ont été retirés par `git worktree remove` : reste l'arbre `/home/user/wt-cl-course-v2-b`.
