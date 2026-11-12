# Contre-lecture courte et différentielle des corrections du code du plancher v3 de T0.7 et du script d'instance v3 — v1

Écrite le 2026-11-11, de 04:05 à 04:24 UTC (heures relevées par `date -u`), par un **contre-lecteur neuf** (Claude Fable 5.2,
`claude-fable-5-2`, sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`), qui n'a écrit ni ce code, ni T0.7, ni la
première contre-lecture. J'ai lu le module de T0.7 : **je suis exclu de tout rôle de lecteur de P3-bis.** Processeur seulement :
aucune dépense, aucune instance, aucun appel de modèle, aucun commit, aucune poussée. Aucune donnée de 7a, de 7b ni de P3-bis ;
données de P3 lues (permises) : manifeste, `sondes-figees.json`, fichier léger, données génériques.

Différence relue en entier : `0d0c5da4061c28d808c3aa3b53c9a9a5e56a3a07..7e23a554aca040016a08fe510504adec172c6998` (branche
`prep/t07-plancher-v3-v1`, commits `84da23aa`, `68882c2d`, `7e23a554` ; neuf fichiers), le script
`scripts/etape_a_t07_variante_b_v3.sh` comparé ligne à ligne au v2 par `diff`, et `scripts/repetition_jouet_variante_b_t07_v3.py`.

## Verdict

**Sans défaut bloquant.** Les trois défauts de la première contre-lecture (CLP3-01 à CLP3-03) et les notes 05, 07, 10 sont
levés dans le code ; les mutations n34, n25c et n28 sont tuées ; l'attaque « un exemple retiré » est arrêtée sous la
configuration v8. Les corrections n'ouvrent aucun trou qui mène à une lecture fausse ou à un repli silencieux. Le script v3
fait ce que l'ordre (brouillon 6, § 13, S-12 et S-13) demande.

**Sept constats neufs, aucun bloquant** (CLC-P3-01 à -07). Deux méritent un geste avant le scellement, sans toucher au code :

- **CLC-P3-01** — la marge du témoin citée (« 4,3 fois le plafond ») vaut à 400 exemples ; aux effectifs réels des enjeux
  (1 591), « un exemple retiré » est arrêté à **1,3 fois** le plafond, et un empan décalé sur 8 exemples (0,5 %) passe au palier
  « carte » avec sa réserve. Le candidat 3 doit citer le chiffre avec ses effectifs.
- **CLC-P3-02** — au script, seule la révision du modèle est contrôlée avant le repli ; les autres contrôles de
  `controler_avant_ouverture` (sceaux de P3, témoin, directions) ne sont joués qu'à la passe à blanc, **après** la garde
  d'ouverture journalisée par le repli. Je les ai joués ici en mode réel sur les fichiers réels : ils passent.

## 1. Lu (empreintes vérifiées par `sha256sum` avant lecture)

- Première contre-lecture `…/plancher-v3-pieces-v1/contre-lecture-code-plancher-v3-v1.md`
  (`32cbc637386d02ad6b90983beb8f675fc1b92c129a20db93e8af22c6b79c9f80`).
- Rapport v2 du développeur `…/rapport-code-plancher-v3-v2.md`
  (`71cc3b89c2df3c8f511796af0e3597844fb8fd1ec37735f0cbeae21d7b5ca231`) ; configuration v8
  (`e31c7a79dc1b68d561874d4d42d63b5eb950931f06075927f239c7ad971fb328`, canonique `0f32c6de…` recalculée ici par
  `lecture_v4.empreinte_configuration`) ; `calibrage_gardes_v1.py`, `calibrage_gardes_v3.py`, `journal-calibrage-v3.txt` ;
  `repetition-jouet-v3-resume.json` et son journal ; `banc_mutations_plancher_v3_v1.py`, `-v4.py`, `journal-banc-v4.txt` ;
  `journal-essais-plancher-v3-v2.txt`.
- `registres/decisions.md` : lignes R-2305, R-2306, R-2309 seulement.
- Ordre `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon6.md`
  (`92d9aebee0634c910ef622a80e4ff2cd33c91df6014ab6a4f04885c0023d2fca`) : § 0 ter, P13, § 5 bis, § 13 (S-12, S-13).
- Code : la différence ; pour suivre les appels, `reextraction_p3_v1.py` en entier, `lecture_v4.py` (l. 128-262, 405-470),
  `lecture_v1.ouvrir_scores`, `repli_etapes_v2.py` (en-tête), `harnais/modeles.py` (`precharger_modele`,
  `regler_determinisme`), `environnements/lancer_pilote_a.charger_modele_et_format`, `sondes/familles.difference_moyennes`,
  `premier_test_ia/figees.ecrire_sondes`.

## 2. Tableau des défauts et notes de la première contre-lecture

| constat | état | preuve |
|---|---|---|
| **CLP3-01** seuils du palier « carte » | **levé** | `TOLERANCES` = 10⁻⁶, 10⁻³, 10⁻² (`reextraction_p3_v1.py`, l. 91) ; v8 admise, v7 refusée (« fixées d'avance »), v6 refusée (essai, joué ici) ; réserve « cause non établie » (l. 100-102) ; mutations c1 à c3 du développeur tuées ; attaque rejouée ici (§ 3) : « un exemple retiré » **arrêté** pour les deux concepts. Réserve : CLC-P3-01 |
| **CLP3-02** n34 | **levé** | rejouée sur copie : **tuée** par `test_lecture_descriptive_de_p3_ne_touche_pas_aux_scores_decisifs`, miroir retiré compris |
| **CLP3-02** n25c | **levé** | rejouée : **tuée** par `test_palier_global_le_pire_des_gardes` |
| **CLP3-02** n28 | **levé** | rejouée : **tuée** par `test_bout_en_bout_bras_etabli`, miroir retiré compris |
| **CLP3-03** contrôle avant l'ouverture | **levé dans le code** ; au script, **partiel avant le repli** | `controler_avant_ouverture` joué par la passe à blanc v2 (refus, code 2, rien d'écrit : essai) ; joué ici **en mode réel sur les fichiers réels de P3** avec la v8 : seul le cache refuse (absent de cette machine), et il passe avec un cache factice complet (`controle-reel.txt`) ; mutation c12 tuée par un essai de comportement (miroir retiré). Au script : CLC-P3-02. La « ligne de l'ordre » de R-2305 relève du brouillon 7, hors de cette différence |
| note **05** nombre de directions à l'étape B | **levé** | `exiger_nombre_de_directions` : mutations x1, x10, x11 tuées (tableau, index, nombre écrit) ; aucun arrêt faux sous des conditions retirées (`ouvrir_scores` filtre les colonnes, pas les directions). L'appel dans `etape_b` n'est tenu que par le miroir (CLC-P3-06) |
| note **07** fautes du bras | **levé** | quatre types ajoutés ; essai paramétré sur les quatre ; mutation x2 tuée. Conséquence : CLC-P3-04 |
| note **10** état des figées affiché | **levé** | ligne présente (`repli_etapes_v2.py`, l. 170-171) ; vue au journal de la répétition (« plancher des figées : {…: 'échec', …: 'établi'} ») ; tenue par le seul miroir (CLC-P3-06) |
| note 06 | déclarée | rapport v2, § 6 ; non appliquée, comme décidé |
| notes 04, 08, 09 | déclarées, non traitées | R-2305 ; la répétition jouet v3 joue désormais la vraie `reextraire` de bout en bout en succès (un point de la note 08 tombe) |

## 3. Réponses aux quatre questions

### (1) Mutations et attaque « un exemple retiré » sous la v8

**Mutations** (une copie de `src/`, mutée puis rétablie, empreinte comparée à l'arbre avant chaque mutation ; essais de
l'arbre ; `-o pythonpath=` ; import tracé : chaque module muté vient de la copie, à son empreinte mutée ; `banc_cl2.py`,
`banc-cl2.json`, 04:10 à 04:21 UTC) : n34, n25c, n28 **tuées** (ligne du tableau). Mutations du développeur tuées par le seul
miroir, rejouées sans lui : c12 **tuée** par un essai de comportement ; c14 et c17 **survivent** (CLC-P3-06).

**Attaque** (`attaque_fautes_partielles_v8.py` : données synthétiques du calibrage du développeur, importé tel quel ; **effectifs
réels de P3** — 478 exemples d'entraînement pour la tromperie, 1 591 pour les enjeux, lus dans `sondes-figees.json` — ; paliers
par `reextraction_p3_v1.palier` de l'arbre ; sortie `attaque-fautes-partielles-v8.json`) :

| faute | tromperie (478) | enjeux (1 591) |
|---|---|---|
| un exemple retiré (avant-dernier ; premier) | témoin 6,7 × 10⁻³ ; 8,2 × 10⁻³ : **arrêté** | témoin **1,32 × 10⁻³ ; 1,29 × 10⁻³ : arrêté** (directions 2,2 × 10⁻³ : « carte ») |
| empan décalé d'un jeton sur 0,5 % des exemples | 2 exemples, 9,1 × 10⁻³ : arrêté | **8 exemples, 8,8 × 10⁻⁴ : établi, palier « carte », réserve** |
| sur 1 % ; 2 % ; 5 % ; 10 % | arrêté (1,3 à 3,6 × 10⁻²) | arrêté (1,2 ; 1,7 ; 3,2 ; 4,3 × 10⁻³) |
| dernier jeton perdu sur les 2 % ; 5 % d'exemples les plus longs | arrêté | arrêté (1,1 ; 1,8 × 10⁻³) |

Sous la v7, la première contre-lecture estimait qu'une faute touchant jusqu'à 40 % des exemples des enjeux passait ; sous la
v8, la limite mesurée ici est entre 0,5 % et 1 %. Pour les enjeux, **le témoin est seul à arrêter** : les directions restent au
palier « carte » jusqu'à 10 % d'exemples touchés. Limites de cette mesure : données synthétiques ; exemples des enjeux de 20 à
40 jetons (ceux du calibrage), non la longueur réelle.

### (2) Les corrections ouvrent-elles un trou ?

**Contrôle avant l'ouverture : un cache partiel peut-il passer ?** Oui, sous trois formes étroites, sans conséquence sur une
lecture (`attaque_cache_partiel.py`, caches factices à la forme du cache réel : blobs et liens symboliques ; hors ligne) :

| cache | issue |
|---|---|
| complet | passe |
| index présent, un lien cassé | refusé (`GardeArret`, morceau nommé) |
| révision donnée par un nom de branche | refusé |
| **index absent, un morceau sur quatre présent** | **passe** |
| **index présent, un morceau de taille nulle** | **passe** (aucune taille contrôlée) |
| **index à la carte vide, aucun poids** | **passe** (0 poids) |
| index illisible ou sans `weight_map` | exception hors `GardeArret` (`JSONDecodeError`, `KeyError`) |

Aucune de ces formes ne sort d'un `snapshot_download` réussi (le lien n'est créé qu'une fois le fichier entier), et
`precharger_modele` s'arrête sur un échec. Si l'une survenait : chargement en échec après l'ouverture, les deux bras arrêtés,
motif écrit, aucune bascule (le cas que CLP3-03 voulait prévenir). CLC-P3-03.

**Élargissement de `FAUTES_DU_BRAS` : une faute de programmation masquée en « arrêt du bras » ?** Oui, par construction, et
c'est ce que R-2305 a décidé. Une `TypeError`, `AttributeError`, `IndexError` ou `KeyError` levée dans les blocs gardés
(chargement, `exemples_p3`, extraction, `_un_bras` : recettes de P3, `plancher_de`, `plancher_apparie`, `graine_de`) donne
« échec » du bras, motif écrit avec le type de l'exception, dans `reextraction-p3-t07.json`, `notation-t07.json` et l'index des
scores. Ce n'est pas silencieux, et aucun chemin ne laisse un bras « établi » après une exception (l'état « établi » est la
dernière instruction du bloc). Mais l'étape A finit en code 0 et le script écrit « FIN : étape A menée au bout » : rien ne
distingue, au code de sortie, un arrêt par la garde d'un arrêt par une faute du code. Avant l'élargissement, la même faute
arrêtait l'étape A après l'ouverture, sans résultat écrit : les deux issues viennent après l'ouverture. CLC-P3-04.

### (3) Script v3

| point | constat |
|---|---|
| `lecture_v4` partout où le v2 appelait `lecture_v2` | **oui** : l. 351 (`empreinte-config`), 406 (`repli-seul`), 416 (`passe-blanc`), 423 (`etape-a-apres-repli`) ; aucune occurrence de `lecture_v2` ni de `lecture_v3` hors de l'en-tête (`grep`) |
| `repli-recalcul` | **jamais appelé** (une seule occurrence, en commentaire, l. 6) |
| `CUBLAS_WORKSPACE_CONFIG` pour le bon processus | **oui** : `env CUBLAS_WORKSPACE_CONFIG=:4096:8 … lecture_v4 etape-a-apres-repli` (l. 423), le processus qui joue la réextraction ; valeur admise par `regler_determinisme` (`:4096:8`). Rejoué ici par fragment, variable lue dans le processus fils, dans les deux branches (EPYC, autre) : `fragment-env.txt` |
| révision de P3 avant toute dépense inutile | **oui pour le cache** : étape 8 (l. 327-350), avant la branche, le repli, la passe à blanc et l'étape A ; code 2, rien d'ouvert. Commande exacte rejouée ici sur caches factices : complet → code 0, lien cassé → code 1 donc arrêt (`fragment-etape8.txt`). Manifeste réel de P3 : `config.agent.modele` et `.revision` présents (`0e9e39f2…`, celle de P13). Le reste du contrôle : CLC-P3-02 |
| arrêts par identifiant (R10) | **inchangés** : `diff` vide sur `minuterie`, `fin_instance`, `arreter_minuterie_essai` (DELETE et PUT par `CONTAINER_ID`, `kill` par `MPID`) |
| borne S-13 | **conforme** : `F` gagne `nf × n_p3` ; `planchers-figees-t07.npz` compté `nf × P × 8 × (d + 1) + 2·10⁶`. Vérifié contre le code : `plancher_p3_<k>` porte `n_p3` nombres par action ; le fichier porte un vecteur `w` par direction (les deux principales de P3 agrègent par le maximum : aucune requête `q`), biais et noms dans l'index. Total recalculé ici à `n` = 5 760 : 1,869 × 10⁹ octets, sous 2 × 10⁹. CLC-P3-07 |
| entrées de P3 sur l'instance | les six fichiers cités par la v8 et leurs compagnons sont suivis à `main` (`git cat-file -e`) : l'extraction partielle du script les apporte |

**La répétition jouet couvre-t-elle ces points ?** En partie.
Couverts : les quatre commandes `lecture_v4` (jouées, code 0), un bras établi et un bras arrêté avec la vraie `reextraire`,
planchers et rapport poussés, contrôle de la passe à blanc écrit, borne comptée, minuterie par identifiant.
Non couverts (CLC-P3-05) : la branche EPYC ; tout le bloc réel de l'étape 8 (« sans objet » en essai) ; l'arrivée de
`CUBLAS_WORKSPACE_CONFIG` dans le processus (le verdict lit la ligne que le script écrit lui-même). Ces trois points sont
rejoués ici par fragments. Je n'ai pas rejoué la répétition entière : le dossier du développeur n'est plus dans le bac à sable,
et `68882c2d..7e23a554` ne change qu'un fichier d'essais (le script et `src/` répétés sont ceux du commit final).

### (4) Essais joués depuis mon arbre

Commande de la mère, `-o pythonpath=`, import tracé (greffon du développeur) : les cinq modules viennent de mon arbre, aux
empreintes du rapport v2 (`c25a8822…`, `66b6684c…`, `f193f1b1…`, `8e24642f…`, `fe08aaa1…`).

| passage | heures UTC | résultat |
|---|---|---|
| trois fichiers, extraction de départ | 04:07:47–04:08:22 | 43 passés, 30 sautés (données génériques de P3 hors de l'extraction), code 0 |
| trois fichiers, extraction élargie | 04:14:46–04:16:01 | **73 passés, 0 sauté, 0 échec** (73 s), code 0 |

Le développeur compte 72 passés et 1 sauté : son saut (fichier v8 hors de son extraction) passe ici.
La suite `tests/test_t07_*` entière n'est pas rejouée (contre-lecture courte ; le développeur l'a jouée au commit final).

## 4. Constats neufs

### CLC-P3-01 — à dire au candidat 3 : la marge du témoin vaut au calibrage, non aux effectifs réels

- **Où** : `reextraction_p3_v1.py`, l. 49-52 (« à 4,3 fois le plafond ») ; rapport v2, verdict et § 3 ; R-2309.
- **Constat** : le calibrage tire 400 exemples pour les enjeux ; P3 en a 1 591. À cet effectif, « un exemple retiré » donne
  1,3 × 10⁻³ : arrêté, à 1,3 fois le plafond. Un empan décalé sur 8 exemples passe au palier « carte ». Le rapport v2, § 9, le
  dit en réserve ; le texte du module et le verdict du rapport ne le disent pas.
- **Geste** : aucun changement de code ni de seuil. Dans le candidat 3, citer « 4,3 fois » avec « à 400 exemples, données
  synthétiques », ou citer la mesure à 1 591 ; ne pas écrire que toute faute d'un exemple est arrêtée.

### CLC-P3-02 — mineur, script : avant le repli, seul le cache est contrôlé

- **Où** : script v3, l. 345-348 (étape 8 : `revision_au_cache` seule) ; l. 406 (étape 11 : `repli-seul`, qui joue la garde
  d'ouverture journalisée) ; l. 416 (étape 12 : passe à blanc, où `controler_avant_ouverture` est joué en entier).
- **Chemin** : sceau d'une entrée de P3 faux, témoin ou directions absents du fichier léger à S7 → refus à l'étape 12, après
  l'ouverture journalisée du repli et le recalcul. Aucune lecture n'est faite ; une instance est perdue.
- **Portée réelle** : nulle si S7 porte les fichiers d'aujourd'hui ; contrôle joué ici en mode réel sur ces fichiers : il passe.
- **Correction proposée** : à l'étape 8, appeler `controler_avant_ouverture` en entier (lecture seule) ; ou une ligne de l'ordre
  (brouillon 7) : la fille le joue sur processeur avant la création.

### CLC-P3-03 — mineur : formes de cache partiel admises ; fautes de l'index hors `GardeArret`

- **Où** : `reextraction_p3_v1.py`, l. 474-483.
- **Correction proposée** : exiger l'index dès qu'un fichier `model-*-of-*.safetensors` est présent, et autant de morceaux que
  le nom en annonce ; taille non nulle ; `weight_map` non vide ; lecture de l'index sous `try`, faute → `GardeArret`. Sans
  cela, la passe à blanc sort en code 1 au lieu de 2 (le script s'arrête dans les deux cas).

### CLC-P3-04 — note : un bras arrêté par une faute du code ne se distingue que par son motif

- **Où** : `reextraction_p3_v1.py`, l. 99, 323, 344, 409 ; script v3, l. 424-432.
- **Geste proposé** (texte, non code) : dans le candidat 3 et l'ordre 7, un bras « échec » dont le motif ne commence pas par
  `GardeArret` est un arrêt technique : réserve et nœud, non un résultat sur la sonde (R4) ; la fille rapporte la ligne
  « plancher des figées ». R-2305 nommait `MemoryError` et `TypeError` ; le développeur ajoute `AttributeError` et
  `IndexError`, ceux de la note 07, déclarés au rapport.

### CLC-P3-05 — note : trois points du script jamais joués par la répétition

- Branche EPYC (`ENV_CPU=()`), celle attendue sur l'instance : rejouée ici, saine sous bash 5.2. Sous un bash antérieur à 4.4,
  `"${ENV_CPU[@]}"` vide échoue avec `set -u`, à l'étape 13, après le repli. Proposition : `${ENV_CPU[@]+"${ENV_CPU[@]}"}`.
- Bloc réel de l'étape 8 : rejoué ici par sa commande exacte. La branche « autre révision » (préchargement) n'est pas
  éprouvable hors ligne ; P13 (i) la rend inattendue.
- `CUBLAS_WORKSPACE_CONFIG` : la répétition pourrait lire `reglages.cublas_workspace_avant` dans `reextraction-p3-t07.json`.
- Le test « EPYC » lit le nom du processeur, non ses jeux d'instructions ; déclaré « non éprouvé » par l'ordre.

### CLC-P3-06 — note : essais tenus par le seul miroir, et trois mutations neuves survivantes

| mutation | issue |
|---|---|
| c14 : appel de `exiger_nombre_de_directions` retiré de `etape_b` | survit sans le miroir |
| c17 : état des figées non affiché | survit sans le miroir |
| x3 : nom du dossier du cache non comparé à la révision | **survit** |
| x8 : sonde figée absente du fichier léger admise par le contrôle | **survit** (une `KeyError` suit, hors `GardeArret`) |
| x9 : aucune sonde figée nommée, admis par le contrôle | **survit** |

Mutations neuves : 11 (x1 à x11), 8 tuées, 3 survivantes ; aucune des trois ne touche une lecture.

### CLC-P3-07 — note : borne de taille et journal

- Marge de la borne : 0,13 × 10⁹ octets, soit `n` ≤ 7 378 actions notées environ. `n` vient des mesures de 7b, que je ne lis
  pas. Proposition : la mère ou la fille calcule la borne sur processeur avant la création.
- Le v3 ajoute au journal la première ligne de `etape-a.txt` (l. 424), changement absent de l'en-tête. Elle porte le chemin
  des scores, les noms des sondes lues et l'état des bras : aucun score.

## 5. Écarts et gestes déclarés

- **Extraction élargie** de mon arbre, au-delà de `/src/`, `/tests/`, `/scripts/` et de la racine :
  `donnees/T0.7-faits-repe-v1/`, `donnees/T0.7-models-under-pressure-v1/`, `docs/sources/invites-2606.08892-v1/` (15,8 Mo).
- **Copie de la configuration v8** posée dans mon arbre, au chemin que lit `test_fichier_v8_egal_au_texte_des_essais`.
- **Lectures hors de l'arbre** : fichiers réels de P3 du dépôt principal (manifeste, `sondes-figees.json`, fichier léger,
  données génériques), par `controle_reel.py` et deux lectures de clés.
- **Aucun processus arrêté, aucune suppression récursive.** Restent dans mon bac à sable
  (`/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/cl2-plancher-v3/`) : la copie du banc, les caches
  factices, les dossiers temporaires de `pytest`. Arbre de travail retiré par `git worktree remove --force`.
- **Pièces** (16 fichiers et leur liste, 112 Ko, non committées) : `…/plancher-v3-pieces-v1/contre-lecture-courte-pieces-v1/` ; liste scellée
  `sha256sums-contre-lecture-courte-v1.txt` (`affc26ab0f9d348e7113f5841b38e1deefaebedb24d66f413fe443e54f681944`).
- **Non fait** : la répétition jouet entière ; la suite `tests/test_t07_*` entière ; le mode réel (aucune carte) ; le candidat 2
  ou 3 et l'ordre brouillon 7 (non lus).

## 6. Modèle

Claude Fable 5.2 (`claude-fable-5-2`), contre-lecteur neuf, sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`.
