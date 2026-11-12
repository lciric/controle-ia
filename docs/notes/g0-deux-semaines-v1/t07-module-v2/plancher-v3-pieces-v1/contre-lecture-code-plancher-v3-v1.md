# Contre-lecture du code du plancher v3 de T0.7 (remède (a') : règle (a) et 800 directions) — v1

Écrite le 2026-11-11, de 02:41 à 03:19 UTC (heures relevées par `date -u`), par un **contre-lecteur neuf** (Claude Fable 5.2,
`claude-fable-5-2`, sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`), qui n'a écrit ni ce code, ni T0.7, ni les
notes de l'erreur de première espèce. J'ai lu le module de T0.7 : **je suis exclu de tout rôle de lecteur de P3-bis.** Processeur
seulement : aucune dépense, aucune instance, aucun appel de modèle, aucun commit, aucune poussée. Aucune donnée de 7a, de 7b ni de
P3-bis ; données de P3 lues (permises) : manifeste, `sondes-figees.json`, fichier léger.

Différence relue en entier : `fecbbcfeaa3d319dc50fdd16e2c7186078db709d..0d0c5da4061c28d808c3aa3b53c9a9a5e56a3a07` (branche
`prep/t07-plancher-v3-v1`, quatorze fichiers ajoutés, aucun fichier existant modifié : vérifié par `git diff --name-status`).

## Verdict

**Sans défaut bloquant.** Le code fait ce que la consigne et les notes demandent ; la règle (a) et la notation par lots sont
justes, vérifiées ici par des calculs indépendants ; aucune bascule vers les 200 directions de P3 n'existe dans le code.

**Trois points à corriger avant le scellement**, aucun n'est une faute du calcul :

- **CLP3-01** — le palier « carte » de la garde d'identité (10⁻² et 10⁻¹) est plus large que la plus petite faute du calibrage :
  une faute réelle d'étendue partielle passe « établi, palier carte », avec une réserve qui l'attribue à la carte. Le seuil est
  dans la configuration v7 : le corriger change son empreinte.
- **CLP3-02** — trois comportements dont la perte serait silencieuse ne sont protégés par aucun essai (mutations survivantes
  n34, n25c, n28), dont la séparation entre les 200 directions de P3 et les lectures complémentaires de l'étape B (R5).
- **CLP3-03** — rien ne répète la réextraction avant l'ouverture de l'étape A : un modèle de P3 absent du cache local fait
  perdre les lectures décisives des deux sondes figées après l'ouverture.

Sept notes (CLP3-04 à CLP3-10). Essais : 102 passés sur les fichiers du plancher v2 et v3 ; suite `tests/test_t07_*.py` : 429
passés, 22 sautés, 3 échecs attendus, aucun échec. Mutations neuves : 38, dont 28 tuées, 10 survivantes (une équivalente, une
non éprouvable sur processeur).

## 1. Lu (empreintes vérifiées par `sha256sum` avant lecture)

- Consigne `…/consignes-mere-2026-11-10-1136-v1/consigne-code-plancher-v3-t07-v1.md`
  (`88879387fe432e77e8541d7f63e9afcc1b299b3aafd1966c70f974b3c29beadd`).
- Rapport `…/plancher-v3-pieces-v1/rapport-code-plancher-v3-v1.md`
  (`cb31edc844c6bc4ee285219a819d2943fd140bf9d70f56d1da2e9e031520db92`) et les 25 pièces du dossier (compagnons tous conformes) ;
  configuration v7 (`3701407c…`), calibrage (`calibrage-gardes-v1.json` `c5d4650e…`, `-v2.json` `46dce2f5…`), bancs.
- Note v3 (`760a562c15991421e6c1eca2b8f65072d82976a956482c599fdeb0cc1c46b602`, sections 6, 8, 9) ; note v2
  (`5ccf0940cb30805736fe3022007cc96f7feaf6f1bb4c921710692ab4d4fdc2fc`, section 5).
- `registres/decisions.md`, lignes R-2273, R-2298, R-2304 seulement.
- Code : les quatorze fichiers de la différence, plus, pour suivre les appels, `sondes/evaluation.py`, `sondes/familles.py`
  (`SondeLineaireJetons`), `harnais/sondes.py` (`score_action`), `harnais/modeles.py` (`regler_determinisme`),
  `premier_test_ia/run.py` (l. 393-440), `premier_test_ia/entrainement.py`, `environnements/lancer_pilote_a.py`
  (`charger_modele_et_format`), `t07/plancher_v1.py`, `t07/criteres_v1.py` (`etat_pour_sonde`), `t07/lecture_v1.py`
  (`charger_planchers_p3`, `ouvrir_scores`, `garde_identite`).

## 2. Réponses aux cinq questions

### (1) Règle (a) — `plancher_v2.comparer_difference_au_plancher` : juste

- **Mêmes tirages pour la sonde et toutes les directions** : une seule matrice de multiplicités `W` (`poids_des_tirages`, l. 84-96)
  sert à toutes les lignes de `C` (`aires_tirees`, l. 99-112). Elle rejoue la suite d'`intervalle_blocs` (même générateur, un
  appel `integers` par tirage, blocs dans l'ordre de `np.unique`) ; l'égalité est contrôlée à chaque appel (l. 157-161).
- **Quantile du plancher recalculé par tirage** : `np.quantile(A[1:], q, axis=0)` (l. 126), l'axe 0 étant celui des directions.
- **Borne basse strictement positive** : `d["bas"] > 0.0` (l. 167) ; `resume_pour_critere` arrête si la borne se perd à
  l'addition au quantile (l. 185-187) ; `criteres_v1.etat_pour_sonde` compare `bas > quantile` (l. 176), strict aussi.
- **Tirages dégénérés** : comptés, exclus, arrêt au-delà de 1 % (l. 121-124), même critère que le paquet gelé.
- **Égalité au bit près avec `aire_sous_courbe`** : numérateur et dénominateur exacts (entiers ou demi-entiers), une seule
  division ; contrôlée à chaque appel sur les aires ponctuelles (l. 153-155).
- **Vérification indépendante** (`contre-lecture-pieces-v1/verif_regle_a.py`) : 12 jeux aléatoires (6 à 30 tâches, effectifs par
  tâche de 1 à 8, ordre des actions mêlé, scores arrondis pour créer des ex aequo, 3 à 40 directions, niveau 0,9875, 300
  tirages), comparés à une force brute qui rééchantillonne les actions et appelle `aire_sous_courbe` pour la sonde et chaque
  direction : **bornes de la différence, nombre de tirages dégénérés et aire égaux au bit près dans les 11 jeux lisibles** ; le
  douzième (7 tirages dégénérés sur 300) s'arrête comme attendu. Les clés communes égalent `plancher_v1.comparer_scores_au_plancher`.
- Mutations neuves n1 à n7c (quantile non recalculé, `>=`, garde des dégénérés, ex aequo, tirages désappariés, trois gardes,
  graine décalée) : **9 sur 9 tuées**, par des essais de comportement.

### (2) Notation par lots — `plancher_v3` : égale à la boucle ; le contrôle en ligne est partiel

- **Agrégations** : le maximum par `np.maximum.reduceat` (exact, aucune action vide : refus l. 132-133) ; l'attention refait les
  opérations de `harnais.sondes.score_action` dans le même ordre (l. 94-105). Aucune moyenne ni médiane.
- **Lots** : `_lots` (l. 78-87) ne coupe jamais une action et ne perd pas le dernier lot.
- **Vérifications indépendantes** : `verif_notation.py` (10 jeux, largeurs 16 à 256, lots de 1 à 10⁶ jetons, échelles
  extrêmes) : écart au plus 5,7 × 10⁻¹⁶ de l'échelle, ordre des actions identique pour chaque direction ;
  `verif_notation_taille_reelle.py`, **à la taille de production (800 directions, largeur 4 096, 36 actions, 8 251 jetons), toutes
  les directions renotées par la boucle** : écart 1,5 × 10⁻¹⁵ (maximum) et 7,7 × 10⁻¹⁷ (attention) de l'échelle, soit 4,6 × 10⁻¹²
  et 4,1 × 10⁻¹¹ du score ; lots 1,4 s et 2,4 s contre 29 s et 66 s pour la boucle.
- **Mémoire** : pic mesuré 294 Mo pour 800 directions, largeur 4 096, lots de 4 096 jetons (`tracemalloc`). Une action plus
  longue qu'un lot forme son propre lot : la borne est alors la longueur de l'action.
- **Le contrôle en ligne peut-il laisser passer un écart systématique ?** Oui, dans trois cas (note CLP3-06) : un écart limité
  aux directions de rang 2 et plus ; un écart limité aux actions hors de l'échantillon (une sur huit et la dernière) ; pour
  l'attention, un écart sous 10⁻¹² fois une échelle très gonflée. Les deux premiers sont déclarés par le développeur, le
  troisième non. L'égalité sur toutes les directions et toutes les actions est tenue par les essais et par mes vérifications ;
  le contrôle en ligne ne garde que contre une défaillance de la machine.

### (3) Réextraction — `reextraction_p3_v1` : conforme, sauf la largeur du palier « carte »

- **Réglages de P3 avant tout calcul sur la carte** : `reglages_de_p3` est entré (l. 312) avant `charger` (l. 319) ; dans
  `lecture_v4.etape_a`, la réextraction (l. 412) précède `extracteur_de_la_course`, et rien avant elle ne calcule sur la carte
  (`ouvrir`, `lire_episodes_t06`, `garde_identite` lisent le disque). Le repli tient en deux processus. Réserve : note CLP3-04.
- **Code de P3 appelé tel quel** : mêmes fonctions, mêmes graines, même ordre que `run._executer_apres_manifeste` ; le modèle est
  chargé par la même chaîne (`bfloat16`, `sdpa`) ; seuls les exemples d'entraînement et la couche de la sonde sont extraits.
- **Témoin déterministe** : juste. La covariance ne dépend ni des étiquettes ni de l'ordre ; le témoin (premier moment par
  classe) et la seconde garde (directions tirées de la covariance, biais tiré de la moyenne) se complètent.
- **Seconde garde** : la graine vient du manifeste de P3 (`_graine_p3`, l. 421-425) ; `plancher_de` est appelé comme dans P3.
- **Entrées réelles de P3, vérifiées sur processeur** (`verif_entrees_p3.py`) : la configuration v7 est admise ; le manifeste
  de P3 porte toutes les clés lues, dont les graines `plancher/tromperie`, `plancher/enjeux`, `sonde/enjeux-lineaire-c15` ;
  effectifs 478/120 et 1 591/409 ; le témoin `enjeux-difference_moyennes-c15` est au fichier léger (maximum, couche 15) ; 200
  directions par sonde. Aucune clé manquante n'arrêtera un bras sur l'instance.
- **Paliers et seuils** : « processeur » (10⁻⁶) justifié (≤ 6 × 10⁻¹¹ mesuré entre 1 et 4 fils) ; **« carte » non justifié :
  CLP3-01.**
- **« garde_principale » = « rapportee »** : je la tiens pour juste. La sonde linéaire refaite n'apporte aucune information sur
  l'identité des jetons (0,49 d'écart pour un bruit de 10⁻⁴ au calibrage) ; ce n'est pas elle qui laisserait passer une faute.
  **Une faute réelle peut passer au palier « carte » : par la largeur de ce palier (CLP3-01), non par ce réglage.** Elle n'est
  pas invisible : deux réserves sont écrites (palier « carte » ; principale hors du processeur) ; mais les lectures restent
  décisives et la réserve nomme la carte.
- **Repli sans bascule (R5)** : vérifié par lecture et par mutation. Un bras arrêté lève `GardeArret` avant toute écriture de
  `plancher_<k>` (`lecture_v4.noter`, l. 224-225) ; les directions de P3 ne vont que dans `plancher_p3_<k>`. Les mutations d27
  (bascule à l'échec) et n39 (directions de P3 notées à la place du plancher neuf) sont tuées par les essais de bout en bout.

### (4) `lecture_v4` : conforme

- **Configuration v7 exigée, v6 refusée** : rejoué par la commande. `lecture_v4 empreinte-config` rend `4ff92c8e…` (code 0) sur
  la v7 et refuse la v6 (code 2, « clé plancher_figees absente ») ; `lecture_v3` et `lecture_v2` refusent la v7 (code 2,
  « n_plancher 800 ≠ 200 »). Différence v6-v7 : `n_plancher` et la clé `plancher_figees`, rien d'autre.
- **800 directions en mode réel** : garde de configuration (l. 99-101) ; `n_plancher` est passé à la réextraction (l. 412) et lu
  par `sondes_neuves_v1` (sondes neuves, T7-P6, concepts). Mutation n26 tuée. Réserve : note CLP3-05.
- **Copies déclarées** : `passe_blanc_v2` et `repli_etapes_v2` comparés par `diff` à leurs originaux : seuls les remplacements
  déclarés. Les essais de miroir passent.
- **Ordre réextraction → autres extractions** : conforme (voir (3)). Protégé par le seul miroir (mutation n37).
- **Réserves recopiées à l'étape B** : la réserve du palier « carte » l'est (essai, mutations d37 et n29 tuées) ; celle de la
  principale rapportée l'est dans le code, sans essai (CLP3-02).

### (5) Essais joués depuis mon arbre

Commande de la mère, `-o pythonpath=`, import tracé (greffon du développeur) : les cinq modules neufs viennent de l'arbre, à
leurs empreintes (`c25a8822…`, `fe9b48e3…`, `5cb4c448…`, `66d1b515…`, `70f587da…`).

| passage | heures UTC | résultat |
|---|---|---|
| plancher v2 et v3, extraction de départ | 02:42:15–02:44:47 | 78 passés, 22 sautés, **2 échecs**, tous deux `FileNotFoundError` sur `brouillons/…/configuration-t07-v5.json`, hors de l'extraction |
| plancher v2 et v3, extraction élargie | 02:45:30–02:47:33 | **102 passés, 0 sauté, 0 échec** (122 s) |
| `tests/test_t07_*.py` (suite T0.7 entière) | 02:47:46–03:04:02 | **429 passés, 22 sautés, 3 échecs attendus, 0 échec** (974 s, code 0) |

Les 22 sauts tiennent à l'extraction (motifs écrits : chaîne de T0.6, fichier léger réel, commits et branche absents). Le
développeur compte 514 passés sur un ensemble plus large (trois fichiers d'essais de plus) : les deux nombres ne se comparent pas.

## 3. Défauts

### CLP3-01 — à corriger avant le scellement : palier « carte » plus large que la plus petite faute calibrée

- **Où** : `reextraction_p3_v1.py`, l. 82 (`TOLERANCES` : `carte_sonde` 10⁻², `carte_directions` 10⁻¹), l. 229-242 (`palier`),
  l. 91-92 et 393 (texte de la réserve) ; configuration v7, clé `plancher_figees.tolerances` ; rapport, § 5.
- **Constat** : le rapport écrit que, « pour une faute de données, d'empan, de découpage ou de couche, la garde arrête ». Le
  calibrage du développeur dit autre chose pour sa plus petite faute, « un exemple retiré » : témoin 6,7 × 10⁻³ (tromperie) et
  4,3 × 10⁻³ (enjeux), directions 1,6 × 10⁻² et 7,2 × 10⁻³ — **sous les deux plafonds : palier « carte », bras établi.** Pour
  « empan décalé d'un jeton » (tous les exemples), les directions des enjeux restent à 3,7 × 10⁻² (sous 10⁻¹) ; seul le témoin
  arrête, à 2,4 × 10⁻², soit 2,4 fois le plafond. Le palier couvre un bruit d'environ 2 × 10⁻² par jeton, sans rapport avec ce
  qu'une carte produit sous des réglages déterministes (R-679 : identique au bit près).
- **Chemin de défaillance** : une faute qui ne touche qu'une part des exemples sans changer les effectifs — par exemple un empan
  ou une troncature différents pour les seuls exemples longs des enjeux, jusqu'à environ 40 % des exemples à proportion du
  calibrage — donne un témoin sous 10⁻² et des directions sous 10⁻¹. Le bras est « établi », palier « carte » ; les 800 directions
  sont tirées d'une covariance qui n'est pas celle de P3 ; la réserve recopiée dit « non-déterminisme de la carte présumé ».
  Les gardes d'effectifs, de faits exclus et de lignes ne voient pas cette faute.
- **Mesure ici** (`test_cl_fautes_partielles.py`, run jouet de P3 des essais, sortie `fautes-partielles-v1.json`) : empan décalé
  d'un jeton sur **tous** les exemples de la sonde linéaire du jouet : témoin à 7,4 × 10⁻³, **palier « carte »** ; seule la
  seconde garde arrête, à 0,154 pour un plafond de 0,1. Les fautes partielles du jouet sont arrêtées, mais il n'a que 16 et 19
  exemples (un exemple y pèse 6 %) : ce run ne dit rien des effectifs réels.
- **Correction proposée** (seuil gelé : décision de la mère ; configuration v8, empreinte canonique neuve) :
  1. resserrer à `carte_sonde` = 10⁻³ et `carte_directions` = 10⁻². Justification par le même calibrage : un bruit de 10⁻³ par
     jeton donne 4,4 × 10⁻⁴ et 2,2 × 10⁻⁴ (témoin), 8,3 × 10⁻³ et 2,2 × 10⁻³ (directions) : il passe ; toutes les fautes calibrées
     sont arrêtées par le témoin (la plus petite, 4,3 × 10⁻³, à 4,3 fois le plafond). Ou supprimer le palier (au-delà du
     processeur : échec), au prix d'un arrêt de bras plus fréquent ;
  2. réécrire la réserve : « écart au-delà de l'arithmétique du processeur, cause non établie : carte, ou faute d'étendue
     partielle dans les jetons réextraits » ;
  3. corriger la phrase du rapport, § 5, avant qu'elle ne passe au candidat 2.
- Réserve sur ma proposition : le calibrage est synthétique, et aux effectifs réels (1 591 exemples) un exemple retiré pèse
  environ quatre fois moins qu'au calibrage (400) ; les gardes d'effectifs portent ce cas.

### CLP3-02 — à corriger : trois comportements à perte silencieuse sans essai

Ces fonctions sont écrites à la main : le miroir ne les couvre pas. Le code est juste aujourd'hui ; aucun essai ne le tient.
Chaque mutation survit à tous les essais neufs, miroir compris (lots 4 et 5 du banc).

| mutation | fichier, ligne | effet si la faute entrait | essai proposé |
|---|---|---|---|
| **n34** `t2 = t` au lieu de `dict(t)` | `lecture_v4.py`, l. 140 | `lecture_planchers_p3` (appelée l. 608) écrase `plancher_<k>` par les 200 directions de P3 avant `lectures_t07_v2.lectures` (l. 614) : les lectures complémentaires au plancher des figées (T7-P18) se font en silence contre P3 (R5) | bout en bout, bras établi : `plancher.n` = `n_plancher` dans T7-P18 des figées ; ou appeler la lecture descriptive après les lectures complémentaires |
| **n25c** `min` au lieu de `max` des paliers | `reextraction_p3_v1.py`, l. 392 | témoin « identique » et directions « carte » : palier « identique », réserve perdue | artefact où une seule des deux gardes est au palier « carte » |
| **n28** `reserve_principale` non recopiée | `lecture_v4.py`, l. 169 | la réserve de la principale rapportée n'arrive pas à l'étape B | le double du bout en bout porte une `reserve_principale` |

### CLP3-03 — à corriger (ordre d'exécution ou passe à blanc) : la réextraction n'est jamais répétée avant l'ouverture

- **Où** : `lecture_v4.etape_a`, l. 412, après `ouvrir` ; `reextraction_p3_v1.charger_modele_p3`, l. 273 (`hors_ligne` en mode
  réel) ; `passe_blanc_v2.py` (copie à la lettre : elle ne touche pas à la réextraction).
- **Chemin** : la révision du modèle de P3 manque au cache local, ou une entrée de P3 manque sur l'instance : les deux bras
  s'arrêtent (motif écrit, aucune bascule : conforme à R5), **après** l'ouverture. Les lectures décisives de la tromperie et des
  enjeux sont en « échec » sur ce run. Le rapport le signale (§ 9, point 5) sans garde.
- **Correction proposée** : un contrôle avant l'ouverture, dans la passe à blanc ou en tête de l'étape A (refus, code 2) :
  `lire_p3` (quatre sceaux), présence du témoin et des 200 directions au fichier léger, présence de la révision du modèle de P3
  dans le cache local. Sur processeur, ces contrôles passent sur les fichiers réels (`verif_entrees_p3.py`) ; seul le cache
  reste à vérifier sur l'instance. À défaut, une ligne de l'ordre d'exécution.

### Notes

- **CLP3-04** — `reextraction_p3_v1.py`, l. 134-139 : `carte_deja_initialisee` et `cublas_workspace_avant` sont rapportés, non
  gardés. Si la carte a déjà servi dans le processus, ou si l'espace de cuBLAS vaut `:16:8`, la réextraction continue. La garde
  d'identité verrait l'effet (palier autre qu'« identique »). Proposition : réserve écrite dans ces deux cas.
- **CLP3-05** — aucun contrôle, à l'étape B, que chaque plancher décisif compte `n_plancher` directions (`lecture_v3.py`,
  l. 135-137 ; `lecture_v4.etape_b`, l. 587). Le nombre est rapporté (`plancher.n`), non gardé ; il est juste par construction
  à l'étape A (n26 tuée). Proposition : en mode réel, arrêt si `plancher.n` ≠ `n_plancher` pour une lecture décisive.
- **CLP3-06** — `plancher_v3.py`, l. 41-42, 155-169, 195-205 : contrôle en ligne sur les deux premières directions seulement.
  Pour l'attention, l'échelle (l. 167) vaut en médiane 3,6 × 10⁴ fois le score à la taille de production (mesuré) : la
  tolérance de 10⁻¹² laisse passer un écart d'environ 4 × 10⁻⁸ du score, sans effet sur un rang. Proposition, sans coût : contrôler
  la première, celle du milieu et la dernière direction ; déclarer l'échelle de l'attention.
- **CLP3-07** — `reextraction_p3_v1.py`, l. 90 : `FAUTES_DU_BRAS` ne contient ni `MemoryError`, ni `TypeError`, ni
  `AttributeError`, ni `IndexError`. Le texte du module dit « toute faute arrête ce seul bras » ; une de celles-là arrête
  l'étape A après l'ouverture, sans résultat « arrêt » écrit. Ce n'est pas un repli silencieux. La covariance de 114 500 jetons
  demande environ 8 Go (estimation du développeur).
- **CLP3-08** — essais absents, effet limité : le biais `b` et la requête `q` peuvent sortir de l'écart de la garde sans qu'un
  essai le voie (n17, n18 ; `b` est pourtant seul à voir un décalage constant des activations, que ni le témoin ni la
  covariance ne voient) ; la principale n'a pas de palier « carte », sans essai (n22) ; la lecture descriptive de P3 peut prendre
  les graines décisives (n36) ; le nombre de fils de la principale refaite (n25e) et le chargement hors ligne (n25d) ne sont
  pas éprouvables sur le jouet. L'étape A n'est jamais jouée de bout en bout avec la vraie `reextraire` en succès (le bras
  établi passe par un double) ; l'accord des deux interfaces est vérifié ici par lecture.
- **CLP3-09** — palier « processeur » à 10⁻⁶, sans réserve : il admet aussi un bruit de carte d'environ 10⁻⁷ par jeton
  (à proportion du calibrage ; les directions sont les plus sensibles), sous le nom « processeur ». Sans effet sur le plancher ; à dire au texte. La seconde garde
  « sans objet » établit le bras sans réserve ; inatteignable en mode réel (manifeste de P3 épinglé, graines présentes).
- **CLP3-10** — `repli_etapes_v2.py`, l. 170 : `etape-a-apres-repli` n'affiche pas l'état du plancher des figées, que
  `etape-a` affiche (`lecture_v4.py`, l. 717). Sortie d'écran seulement ; `notation-t07.json` le porte.

## 4. Mutations (copies seulement, `-o pythonpath=`, import tracé)

Méthode de R-2246 : copie de `src/` dans le bac à sable, essais de l'arbre, `PYTHONPATH=<copie>/src:<arbre>/tests:<greffon>`,
`--rootdir` et `-c` de l'arbre ; greffon `trace_import_cl.py` (celui du développeur, étendu à `plancher_v2`, `lecture_v3`,
`lectures_t07_v2`). **Pour chaque mutation : module importé de la copie, à l'empreinte du fichier muté, aucun module neuf hors
de la copie.** Copie saine : 98 passés, 4 désélectionnés. Lots 1 à 3 **sans** les essais de miroir (`-k "not miroir"`), sans
`-x` ; lots 4 et 5 : survivantes de `lecture_v4` et n25c rejouées **avec** le miroir.

**Mutations du développeur que le miroir tuait (rejouées sans lui)** : m27 (bascule à l'échec), m30, m31, m32, m37 sont
**aussi tuées par un essai de comportement** (`test_bout_en_bout_bras_arrete_aucune_bascule`, `test_bout_en_bout_bras_etabli`,
`test_passe_blanc_v2_et_repli_v2_controlent_la_configuration_v4`) : le « miroir seulement » du rapport tenait à l'arrêt au premier
échec. **m28** (planchers notés par la boucle) n'est tuée que par le miroir : attendu, les deux notations rendent les mêmes
scores à 10⁻¹⁴ près.

**Mutations neuves : 38 ; 28 tuées ; 10 survivantes.**

| | mutation | fichier | issue |
|---|---|---|---|
| n1 | quantile du plancher non recalculé par tirage | `plancher_v2` | tuée (5 essais) |
| n2 | borne basse ≥ 0 | `plancher_v2` | tuée |
| n3 | garde des tirages dégénérés retirée | `plancher_v2` | tuée |
| n4 | ex aequo non comptés pour moitié | `plancher_v2` | tuée |
| n5 | tirages du plancher désappariés de ceux de la sonde | `plancher_v2` | tuée (5 essais) |
| n6 | contrôle d'égalité à `aire_sous_courbe` retiré | `plancher_v2` | tuée |
| n7 | contrôle des tirages contre `intervalle_blocs` retiré | `plancher_v2` | tuée |
| n7b | garde de la borne perdue à l'addition retirée | `plancher_v2` | tuée |
| n7c | graine des tirages décalée | `plancher_v2` | tuée (31 essais) |
| n8 | contrôle en ligne : première et dernière action seulement | `plancher_v3` | tuée |
| n9 | échelle du contrôle gonflée (× 10⁶) | `plancher_v3` | tuée |
| n12 | poids des directions en simple précision | `plancher_v3` | tuée (14 essais) |
| n12c | contrôle en ligne sur une seule direction | `plancher_v3` | tuée (essai des constantes seul) |
| n13 | réserve du palier « carte » non écrite | `reextraction` | tuée |
| n14 | réserve de la principale rapportée non écrite | `reextraction` | tuée |
| n15 | validation extraite au lieu de l'entraînement | `reextraction` | tuée (9 essais) |
| n17 | biais `b` hors de l'écart de la garde | `reextraction` | **survit** (CLP3-08) |
| n18 | requête `q` hors de l'écart de la garde | `reextraction` | **survit** (CLP3-08) |
| n21 | noms des directions redonnées non contrôlés | `reextraction` | survit, **équivalente** (`ecarts_sonde` compare le nom) |
| n22 | palier « carte » offert à la principale | `reextraction` | **survit** (CLP3-08) |
| n23 | seconde garde sous la graine de T0.7 | `reextraction` | tuée (6 essais) |
| n24 | sceaux des entrées de P3 non contrôlés | `reextraction` | tuée |
| n25 | tolérances non contrôlées à l'égalité en mode réel | `reextraction` | tuée |
| n25b | palier « carte » des directions à 0,9 | `reextraction` | tuée |
| n25c | palier global = le meilleur des paliers | `reextraction` | **survit** (CLP3-02) |
| n25d | modèle de P3 chargé en ligne en mode réel | `reextraction` | survit, **non éprouvable sur processeur** |
| n25e | fils de torch de P3 non posés pour la principale | `reextraction` | **survit** (CLP3-08) |
| n26 | figées : `n_p3` directions neuves au lieu de `n_plancher` | `lecture_v4` | tuée |
| n28 | `reserve_principale` non recopiée à l'étape B | `lecture_v4` | **survit** (CLP3-02) |
| n29 | paliers et réserves absents de l'index des scores | `lecture_v4` | tuée |
| n31 | clé `plancher_figees` non contrôlée | `lecture_v4` | tuée |
| n32 | contrôles de la v3 et de la v2 non joués en mode réel | `lecture_v4` | tuée |
| n34 | lecture descriptive de P3 écrite dans les scores décisifs | `lecture_v4` | **survit** (CLP3-02) |
| n35 | lecture descriptive de P3 à un autre niveau que 0,95 | `lecture_v4` | tuée |
| n36 | lecture descriptive de P3 sous les graines décisives | `lecture_v4` | **survit** (CLP3-08) |
| n37 | réextraction après l'apprentissage des sondes neuves | `lecture_v4` | tuée par le seul miroir |
| n38 | `repli-recalcul` admis | `lecture_v4` | tuée |
| n39 | directions de P3 notées à la place du plancher neuf | `lecture_v4` | tuée |

Heures UTC des lots : lot 1, 02:51:41–03:06:14 ; lot 2, 02:51:41–03:09:18 ; lot 3, depuis 03:06:53 ; lot 4, depuis 03:09:31 ;
ces quatre lots finis avant 03:15:02 ; lot 5 (n25c, miroir compris : 41 passés), fini à 03:19:04.

## 5. Écarts et gestes déclarés

- **Extraction élargie** de mon arbre, au-delà de `/src/`, `/tests/`, `/scripts/` et de la racine : `donnees/T0.7-faits-repe-v1/`,
  `donnees/T0.7-models-under-pressure-v1/`, `docs/sources/invites-2606.08892-v1/`,
  `brouillons/T0.7-sondes-v0-v1-candidat1-pieces/configuration-t07-v5.json` et son compagnon,
  `brouillons/T0.7-sondes-v0-v1-brouillon14-pieces/`, `brouillons/T0.7-sondes-v0-v1-brouillon14.md`,
  `brouillons/T0.7-sondes-v0-v1-brouillon17-pieces/`, `brouillons/T0.7-sondes-v0-v1-brouillon19-pieces/` (28 Mo en tout). Rien
  d'interdit ; noms des pièces vérifiés avant extraction.
- **Copie de la configuration v7** posée dans mon arbre, au chemin que lit `test_fichier_v7_egal_au_texte_des_essais` (fichier
  non versé au commit) : l'essai, sauté chez le développeur, passe.
- **Un processus arrêté par son PID** (R10) : le lot 2 du banc (PID 7775) et son essai en cours (PID 18836), à 03:09 UTC,
  parce que le lot 3 rejouait la fin de sa liste. La copie touchée a été rétablie et comparée à l'arbre avant le lot 4.
- **Disque** : descendu à 1,4 Go libres pendant la suite entière (dossiers temporaires de `pytest`), revenu à 3,1 Go. Aucune
  suppression récursive de ma part.
- **Pièces** versées sous `plancher-v3-pieces-v1/contre-lecture-pieces-v1/` (25 fichiers, moins de 200 Ko, non committées ; leurs empreintes sont dans
  `sha256sums-contre-lecture-v1.txt` du même dossier, scellé,
  `4cfbb43021f3da848795aa9e318d3029cc7b1e44e7c98a39bcf2d58acefbf4d1`) : bancs, scripts de vérification, sorties, traces d'import.
- **Non fait** : le mode réel (aucune carte) ; les trois fichiers d'essais hors du motif `tests/test_t07_*` que le développeur
  joignait à sa suite ; la relecture ligne à ligne de `lectures_t07_v2.lectures` contre la v1 (tenue par son miroir, qui passe,
  et par le décompte du `diff`).

## 6. Modèle

Claude Fable 5.2 (`claude-fable-5-2`), contre-lecteur neuf, sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`.
