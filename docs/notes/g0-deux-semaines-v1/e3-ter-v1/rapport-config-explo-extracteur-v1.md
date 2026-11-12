# Course exploratoire de T0.6 : configuration exploratoire et extracteur des comptes de la garde d'équivalence — rapport du développeur, v1

> **EXPLORATOIRE, NON OPPOSABLE (R-522)** : ce rapport prépare le run exploratoire ; aucun chiffre de résultat n'en sort.

- **Mission** : deux pièces manquantes avant la création de l'instance, nommées par l'ordre `docs/notes/g0-deux-semaines-v1/e3-ter-v1/ordre-course-dose-reponse-exploratoire-v1-brouillon1.md` (§ 2, § 4 A, § 5 étape 0, § 10) : la configuration exploratoire et le script de lecture de la garde ; plus la réponse aux trois `<<À VÉRIFIER>>` que le code permet d'instruire.
- **Développeur** : sous-agent neuf de la session mère (`session_016QhUrrLeN21G7Z9KZobE42`), modèle Fable 5.1 ; n'a écrit ni la chaîne v13 ni l'ordre.
- **Heure** : fichiers écrits entre 15:28 et 15:33 UTC le 8 novembre 2026 (`date -u`).
- **Règles tenues** : fichiers neufs seulement (R12) ; `git status --short` du dépôt principal : trois `??` (les fichiers ci-dessous) ; arbre de travail de la chaîne v13 (`/tmp/claude-0/-home-user/86976e6f-3fae-57b1-a905-26802f445363/scratchpad/wt-t06-v13`, détaché à `7822a65b`) : aucun fichier suivi modifié, ses six fichiers neufs non touchés ; aucun commit, aucune poussée, aucun `.sha256`, aucun réseau, aucune commande `vastai`, aucune instance, aucune dépense, aucune clé lue ; rien lu sous `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; sous `diag/` d'E3 bis, seuls les comptes de la garde (`fiches[*].equivalence`, `controles_negatifs`, `etats`, `descriptifs`, `controle_negatif_donnees`) ont été lus, aucune sonde ni score.
- **Base de code lue** : `main` ne porte pas la chaîne T0.6 ; la chaîne v12 est à `7822a65b` (`origin/prep/t06-course-v12`) et la chaîne v13 (six fichiers neufs d'un autre développeur) dans l'arbre de travail ci-dessus et dans `livrables/chaine-t06-v13-v1.zip` (`98f7d4cd128ebba3e251796cfc0d479b5ecf22cafbbe7a8bef81988357763e4c`, vérifié).

## 1. Verdict (trois lignes)

1. Les deux pièces existent et sont éprouvées : la configuration charge sous `configuration_v6` (dès que la ligne de GO est lisible, voir 2) ; l'extracteur (17 essais R5 verts) redonne sur E3 bis **0 paire sur 16** en évaluation et **3 sur 60** en distillation, comme la contre-lecture cl1.
2. **Deux bloquants dans `registres/go.md`, hors de mon périmètre (registre, décision de la mère)** : (a) la cellule « accordé par » de **GO-2026-11-08-11** n'est pas exactement `Lazar` → `session_v3.verifier_go_v3` (donc `session_v12`, `configuration_v6`, `lancer_t06_v13.sh --verifier-go-seulement` et `controles-epreuve`, l'amorce v11 et `lanceur_v6`) et la garde `.claude/hooks/garde_calcul.py` (l. 103) refusent la ligne ; (b) la ligne 280 (**GO-2026-11-08-09**, échéance « 2026-11-08 ≈ 21:34Z ») rend le registre entier illisible pour la garde de calcul (« registre GO mal formé ligne 280 : dates illisibles »), qui bloque alors **toute** commande `vastai create instance`, et le lanceur v13 la rejoue avant d'imprimer la commande (`creation`, l. 234).
3. Les trois `<<À VÉRIFIER>>` sont instruits (§ 5) : « relance retirée » et « prix 0 » sont **refusés** par le code (forme retenue : `prix_max_usd_h` 0,01) ; le pic de mémoire de carte ne dépend pas, au premier ordre, de la fraction (capture copiée sur processeur) et tient sur 80 Go à T = 10 (calcul borné, hypothèses dites) ; le bras B **n'est pas lancé** sous la ligne exploratoire (l'amorce v11 le débraye d'elle-même pour toute épreuve : `EPREUVE_GO_ID` non vide, l. 422), aucun changement de la v13 n'est nécessaire.

## 2. Fichiers créés (sha256 par `sha256sum`, 8 novembre 2026 ≈ 15:31 UTC)

| fichier | rôle | lignes | sha256 |
|---|---|---|---|
| `docs/notes/g0-deux-semaines-v1/e3-ter-v1/config-t06-course-explo-v1.json` | configuration exploratoire (§ 3) | 144 | `1911a9e9e78bd5108886d3f1e3f21edd28f88b82e78b9a9bcfebe9898028e734` |
| `scripts/extraire_garde_equivalence_t06_v1.py` | lecture des comptes de la garde (§ 4) | 321 | `6c6f659db483916639c7d7795a11c178a9ee5d35af97f6588923f6c6367fce4d` |
| `tests/test_extraire_garde_equivalence_t06_v1.py` | essais R5 de l'extracteur (17) | 269 | `4f2f9d5be42a918dcd8b831e2dc92fec1c6533a101b001c6ac45110e9e0208db` |
| `docs/notes/g0-deux-semaines-v1/e3-ter-v1/rapport-config-explo-extracteur-v1.md` | ce rapport | — | (empreinte dans la réponse finale) |

Aucun compagnon `.sha256` écrit (interdit par la commande) : le compagnon de la configuration est à écrire par la mère sur la branche d'épreuve (`python -m controle_ia.scellement sceller <fichier>` ; l'amorce exige `$CONFIG.sha256` et le vérifie, `amorce_instance_t06_v11.sh` l. 389–394).

## 3. Configuration exploratoire

Source : `config-t06-reel-v1-brouillon5.json` du candidat 12, retrouvée dans l'arbre `7822a65b` (`docs/notes/g0-deux-semaines-v1/`), empreinte vérifiée `b7a5c1baeee13f7589b296fb166180515422ebc8c7eff703994bb5b6835ae527` (= celle citée par l'ordre § 1). Sérialisation identique à la source (`json.dumps(indent=1, sort_keys=True, ensure_ascii=False)` + saut de ligne : rejoué à l'octet sur la source), si bien que le `diff -u` ne porte que les champs changés.

### 3.1 Diff (`diff -u` source → exploratoire, 7 lignes changées, 6 champs)

```
@@ -30,7 +30,7 @@ "calendrier"
-  "dernier_jour_creation": "2026-11-15",
+  "dernier_jour_creation": "2026-11-09",
   "fin_go_utc": "2026-11-17T00:00:00Z"            (inchangé : voir 3.2)
@@ -44,7 +44,7 @@ "carte"."relance"
-   "prix_max_usd_h": 4.7
+   "prix_max_usd_h": 0.01
@@ -94,9 +94,9 @@
- "fraction_equivalence": 0.05,
+ "fraction_equivalence": 0.5,
- "go_id": "GO-2026-11-02-28",
+ "go_id": "GO-2026-11-08-11",
@@ -110,7 +110,7 @@ "offre"
-  "etiquette": "t06-v2",
+  "etiquette": "t06-explo",
@@ -118,7 +118,7 @@
- "plafond_usd": 200,
+ "plafond_usd": 100,
```

Tout le reste est celui du candidat 12 (T = 10, lot 8, `max_nouveaux` 400, six états, 64 tâches `76cdeace…`, 32 tâches de réserve `8d20a698…`, 480 pas, couches 7/15/23, Mahalanobis `produit_matriciel_v2`, `tolerance_equivalence` 0,2, `q99`, 10 / 4 / 0,95, `carte.course.prix_max_usd_h` 1,30 — la v2 à 2,10 sera un fichier séparé, non créé ici).

### 3.2 Les deux champs qui ne suivent pas la lettre de la consigne, et pourquoi

- **`calendrier.fin_go_utc`** : la consigne de la mère dit « `fin_go_utc` = 2026-11-16 », l'ordre dit « `<<FIN_GO_EXPLO>>` = échéance de la ligne (l'amorce l'exige) ». Le code exige **le lendemain 00:00 UTC de l'échéance** de la ligne du registre (`session_v2.verifier_calendrier` l. 129–133, `session_v3.verifier_calendrier_v3` l. 114, 129, appelés par `lancer_t06_v13.sh` l. 169 et 199 et par l'amorce l. 397–400 ; `configuration_v2` l. 76–83 n'exige, lui, que `dernier_jour_creation` < fin). L'échéance de GO-2026-11-08-11 est le 2026-11-16 (`registres/go.md` l. 282) : la valeur exigée est donc **`2026-11-17T00:00:00Z`**, qui est aussi celle du candidat 12 (dont la ligne GO-2026-11-02-28 échoit le même jour). Vérifié : `session_v3 calendrier` sur la configuration → `fin_go_utc_s=1794873600 dernier_jour_creation=2026-11-09 echeance_go=2026-11-16`, code 0 ; avec `2026-11-16T00:00:00Z` → « ≠ lendemain 00:00 UTC de l'échéance du GO (2026-11-17T00:00:00+00:00) », code 1. Le champ est donc **inchangé par nécessité**, non par oubli.
- **`carte.relance`** : voir § 5.1 (ni « retirée » ni « prix 0 » ne chargent ; 0,01 retenu).

### 3.3 Chargement sous `configuration_v6` (fonction `exiger_config_t06_v6(config, registre_go, jour)`, exécutée sans rien lancer)

- `est_epreuve(config)` → `True` (go_id lisible ≠ GO de la course).
- Sur le **registre réel** de `main`, jour 2026-11-08 : **REFUS** — « épreuve GO-2026-11-08-11 : ligne de GO non conforme : GO-2026-11-08-11 : accordé par "Lazar (« go », session mère ≈ 15:38Z, sur « il faut une nouvelle ligne d'autorisation de dépense »)", « Lazar » attendu » (`session_v3.verifier_go_v3` l. 65–66). Même refus par `lancer_t06_v13.sh --verifier-go-seulement 100` (code 2, « GO GO-2026-11-08-11 refusé : … »).
- Sur une **copie de travail du registre hors dépôt** (scratchpad, seule la cellule « accordé par » de cette ligne remplacée par `Lazar` ; le registre réel n'est pas touché) : **CHARGE** aux jours 8, 9 et 10 novembre ; `--verifier-go-seulement 100` → « GO VÉRIFIÉ, RIEN CRÉÉ : GO-2026-11-08-11 conforme (plafond 100 USD, 2026-11-08 → 2026-11-16) ; plafond d'épreuve 100 + dépense antérieure 0 = 100 ≤ 100.0 », code 0 ; `session_v3 calendrier` au 10 novembre → « dernier jour de création (2026-11-09) dépassé le 2026-11-10 : nœud de Lazar, aucune création », code 1 (le dernier jour de création est bien verrouillé).
- Garde de calcul `.claude/hooks/garde_calcul.py` sur une commande factice `GO_ID=GO-2026-11-08-11 echo vastai create instance …` (registre réel) : « GARDE … commande bloquée : registre GO mal formé ligne 280 : dates illisibles », code 2 — bloquant (b) du § 1 : la ligne 280 est GO-2026-11-08-09, échéance « 2026-11-08 ≈ 21:34Z » (`date.fromisoformat` échoue, hook l. 66–70) ; la chaîne, elle, ne lit les dates que de la ligne du GO demandé (`verifier_go_v3` l. 69), elle n'est pas gênée par la l. 280, mais le lanceur `creation` rejoue la garde (l. 234) et sortirait « garde de calcul : commande refusée ». Avec les deux cellules lisibles, la garde lirait aussi `g["par"] != "Lazar"` (l. 103) : la correction de (a) la concerne aussi.

## 4. Extracteur `scripts/extraire_garde_equivalence_t06_v1.py`

### 4.1 Clés réellement écrites par la chaîne (vérifiées dans le code et sur les fichiers d'E3 bis)

- `manifeste.ecrire_resultat` (l. 128–139) enveloppe chaque résultat : `{"run_id", "manifeste_sha256", "resultat": …}` ; **l'extracteur v1 et la description de cl1 (« `diag/<run>/episodes-t06.json`, `fiches[k]…` ») omettent l'enveloppe** : le vrai chemin est `resultat.fiches[k]`.
- `episodes-t06.json` → `resultat.fiches[k].{phase, condition, tache, episode, equivalence}` ; `equivalence` = `{actions (clés "i,t" triées), tolerance, statistique, ecarts_q99, ecarts, controle_negatif_zone_generee, profils, longueurs_contexte, lignes, positions_capturees, empreintes_capture, sondes}` (`lanceur.py` l. 292–297, `pilote_a.CLES_RAPPORT_GARDEES` l. 36–37 ; `sondes` est l'audit de symétrie des tableaux, pas une sonde de lecture) ; `resultat.controles_negatifs[<état>]` = `{comparables, passent, courtes, echecs, fraction, min_des_maxima, positions_min, statistique, lecture}` (`episode.py` l. 328–331, `lanceur.py` l. 302–304) ; `resultat.etats[<état>]` = `{adaptateur, dose, empreinte}` seulement (l. 258 : CLE3T-06 confirmée) ; `resultat.descriptifs.{memoire_pic_gio, duree_s, longueur_remplie_max, generation_s, passe_unique_s, …}`.
- `distillation-t06.json` → `resultat.controle_negatif_donnees` (même forme de bilan ; `lanceur_v5/v6` l. 266), `resultat.duree_s` ; aucun écart par action : `comparables + courtes` = actions contrôlées.
- `arret.json` → `resultat.{etape, motif, partiel, duree_s}` (`lanceur_v5/v6` l. 192 ; `gardes.motif_d_arret` : « GardeArret: … »).
- Paires indépendantes : rejeu du tirage depuis `manifeste.graines` (`manifeste.generateur`, puis `gen.integers(0, 2**31−1, size=N·T)` de `pilote_a.graines_des_actions` l. 73–76, puis `gen.random(T) < fraction`, `lanceur.py` l. 148–151 et 267–270) ; clés `tache/<id>` (évaluation : un générateur neuf par condition, mêmes pas dans les six états) et `distillation/tache/<id>/e<k>` (partagé par les deux conditions). L'essai `test_le_rejeu_du_tirage_est_celui_de_la_chaine` compare ma transcription aux fonctions mêmes de la chaîne (`controle_ia.manifeste.generateur`, `controle_ia.environnements.pilote_a.graines_des_actions`, identiques à l'octet entre `main` et `7822a65b`).

### 4.2 Sortie (comptes seuls, JSON, en-tête `"statut": "EXPLORATOIRE, NON OPPOSABLE (R-522)"`, fichier `garde-equivalence-<run>-exploratoire-non-opposable-r522.json` avec `--sortie`, jamais écrasé)

`manifeste` (sha256, compagnon, commit, numpy du manifeste et d'ici, rattachement des résultats par `manifeste_sha256`) ; `config` (fraction, T, N, lot, tolérances, seuils, go_id, mode) ; `paires_independantes` (évaluation et distillation : générateurs, paires, retenues, par générateur, pas retenus) ; `evaluation.phases[<état>]` (conditions, fiches, actions contrôlées, actions attendues du tirage = retenues × conditions, tolérances, statistiques, plus grand `ecarts_q99` et plus grand `ecarts` par couche, couches au-dessus de la tolérance, contrôle négatif) ; `distillation` (actions contrôlées = comparables + courtes, attendues = retenues × 2, bilan) ; `arret` (présent, étape, motif, lecture (i)/(ii)/autre) ; `descriptifs` (pic de mémoire, durées, « absent » si manquant) ; `e3_6` (verdict, motifs, règle, ligne).

**Règle de lecture E3-6** (transcription de l'ordre §§ 0, 2, 3, 4 A, 6, 9.1 ; l'ordre ne l'écrit pas sous forme de liste : à contre-lire) : « réglé » ⇔ aucun arrêt ; distillation et épisodes présents ; chaque état annoncé a des fiches ; ≥ 1 action contrôlée par état et en distillation (garde exercée de fait, adaptateurs injectés compris) ; q99 maximal ≤ tolérance par couche ; contrôle négatif « conforme » partout (lecture écrite par la chaîne : comparables ≥ 10, fraction ≥ 0,95). Sinon « non réglé » avec tous les motifs ; un arrêt est lu d'avance (i) ou (ii) selon le texte du motif (`activations.py` l. 217, `episode.py` l. 341).

Toute clé obligatoire absente → `CleAbsente` (SystemExit code 2, message « clé absente : <fichier>.<chemin> (jamais lue comme zéro) », rien sur la sortie standard).

### 4.3 Essais (R5)

```
PYTHONPATH=src timeout 900 nice -n 10 python -m pytest -q -p no:cacheprovider tests/test_extraire_garde_equivalence_t06_v1.py
→ 17 passed in 2.59s
```

Faux dossier aux vraies clés (forme du manifeste d'E3 bis `e9f0cbb4…` : `graines` par `controle_ia.manifeste.graines`, enveloppe `resultat`, six états, 4 tâches, 3 × 5 générateurs de distillation, T = 10, fraction 0,5). Cas sain : paires et actions contrôlées par état = retenues × conditions, q99 et max par couche, contrôle négatif conforme, rattachement, « E3-6 réglé », fichier de sortie marqué, refus d'écraser (R12). Artefacts : `controles_negatifs`, `etats`, `fiches`, `controle_negatif_donnees`, `fiches[k].equivalence.actions`, `config.fraction_equivalence` absents → arrêt explicite nommant la clé (code 2) ; dossier sans distillation → « E3-6 non réglé : distillation absente » ; sans épisodes → « épisodes absents », descriptifs « absent » ; `arret.json` présent → rapporté avec lecture (i), (ii) ou « autre » et « non réglé » ; q99 > tolérance et contrôle négatif « non concluant » → motifs ; état à zéro action contrôlée → « garde non exercée » ; deux manifestes sans `--run` → arrêt.

### 4.4 Rejeu sur E3 bis (comptes seuls, permis) — extrait de `a5c0e298` dans le scratchpad, compagnons vérifiés (`sha256sum -c` : manifeste, `episodes-t06.json`, `distillation-t06.json` OK)

Manifeste `runs/20261108-065822-t06-reel/manifeste.json` `e9f0cbb444efe335e7d9d37b4635f69595a5ef63294c5ec5fcf8e732a455f272` (= compagnon), commit `c01d29ea`, numpy 2.4.6 au manifeste et ici (même version : la réserve de version de cl1 ne s'applique pas à ce rejeu) ; config : fraction 0,05, T = 4, lot 8, GO-2026-11-07-08.

- **Évaluation : 16 paires (4 tâches × 4 pas), 0 retenue** (e1 à e4 : 0) → actions contrôlées **0** dans les six états (dose0 : 16 fiches, 4 conditions ; S25, S50, S75, S100, T100 : 4 fiches chacun), attendues du tirage 0 : observé = attendu ; `ecarts_q99` vides ; contrôles négatifs : comparables 0, lecture « non concluant » partout.
- **Distillation : 60 paires (3 tâches × 5 épisodes × 4 pas), 3 retenues** (d1/e0 pas 1 ; d3/e3 pas 1 ; d3/e4 pas 0) → **6 actions contrôlées** (comparables 6 + courtes 0 = 2 × 3 : observé = attendu), passent 6, fraction 1,0, `min_des_maxima` 1,0957, lecture « non concluant » (6 < 10), durée 576,0 s.
- Arrêt : absent. Descriptifs : `memoire_pic_gio` 18,4 Gio, `longueur_remplie_max` 1 744, génération 1 045,8 s, passe unique 10,1 s, épisodes 681,5 s.
- Ligne : « E3-6 non réglé : … aucune action contrôlée (garde non exercée) ; … contrôle négatif « non concluant » … (six états) ; distillation : contrôle négatif « non concluant » (comparables 6, fraction 1.0) » — c'est exactement l'état d'E3-6 relevé par cl1 (CLE3T-05, § 3 : 0/16, 3/60, 6 actions, non concluant).
- Fichier de sortie du rejeu (hors dépôt) : scratchpad `e3bis-lecture/garde-equivalence-20261108-065822-t06-reel-exploratoire-non-opposable-r522.json`, `fd9e5cd04dd1297d93f08fa4ebf23790d241784bc97ce006122c7ddc4177d6fa`.

## 5. Les trois `<<À VÉRIFIER>>` de l'ordre

### 5.1 Forme de la configuration sans repli H200 (ordre § 2, l. 40)

Éprouvé sous `exiger_config_t06_v6` (registre de travail, jour 8 novembre) : **« relance retirée » → REFUS** « carte : clés ('course', 'relance') attendues » (`configuration_v2.py` l. 68–69 : `set(carte) != set(CLES_CARTE)`) ; **« prix 0 » et « prix 0.0 » → REFUS** « carte relance : mémoire de carte et prix maximal strictement positifs attendus » (l. 48–50 : `prix_max_usd_h > 0`) ; `relance = null` → REFUS (l. 44–45). Aucune des deux formes de l'ordre ne charge, à aucune version (v2 à v6 enchaînent la v2). **Forme retenue : `carte.relance.prix_max_usd_h` = 0,01**, le plus petit prix positif, reste du bloc inchangé : le filtre de relance devient `… gpu_name=H200_NVL … dph_total<=0.01` (`session_v12 filtre CONFIG relance`, code 0) et `creation auto relance …` sortirait « aucune offre conforme dans la liste filtrée : nœud, pas de création » (code 3). Le repli est en outre déjà interdit par la commande de l'ordre (`creation auto course 0`, § 5 étape 2) : rien dans le lanceur ni l'amorce ne bascule de lui-même sur `relance` (le choix de carte est l'argument `CARTE`, `lancer_t06_v13.sh` l. 177–179, 212–214). Alternative pour la mère : laisser le bloc `relance` du candidat 12 inchangé (verrou procédural seul) ; la configuration livrée porte le verrou 0,01.

### 5.2 Pic de mémoire à lot 8, T = 10, fraction 0,5, A100 80 Go (ordre § 2, l. 45 ; § 8)

Ce qui est **calcul depuis le code** :
- La capture d'activations pendant la génération (`Crochets`, `activations.py` l. 57–70) copie chaque sortie de couche des lignes contrôlées **sur le processeur**, en `float32` (`type_de_capture`), à chaque passe : préremplissage (k lignes × L positions × 4 096) puis une position par passe de décodage ; rien n'est gardé sur la carte. La fraction change donc le nombre de lignes capturées par pas (espérance 4 sur 8 au lieu de 0,4) et la mémoire **vive** du processeur, pas la mémoire de la carte au premier ordre. Mémoire vive par lot (gardée jusqu'à la fin du lot, `acts_generation`, `episode.py` l. 204–231) : 3 couches × (L + jetons générés) × 4 096 × 4 octets par action contrôlée ≈ 130 Mo pour L ≈ 2 500 ; 40 actions attendues par lot (80 au pire) → ≈ 5 Go (≈ 11 Go au pire), plus la passe unique de 8 épisodes (3 × L_fin × 16 Ko ≈ 2,2 Go pour L_fin ≈ 5 600) ; la configuration exige `memoire_vive_min_go` 128 (E3 bis : 2,1 To) : sans risque.
- Mémoire de la **carte** : poids 8,03 G paramètres en bfloat16 (`charger_modele` « bfloat16 », `lancer_pilote_a.py` l. 263) ≈ 15,0 Gio ; cache clés-valeurs de Llama 3.1 8B : 32 couches × 2 × 8 têtes × 128 × 2 octets = 128 Kio par jeton et par ligne ; seuls les logits du dernier jeton sont calculés (`logits_to_keep=1`, `episode.py` l. 108, 131 : pas de tenseur vocabulaire × contexte). E3 bis (T = 4, lot 8, `longueur_remplie_max` 1 744) : pic mesuré **18,4 Gio** (`descriptifs.memoire_pic_gio`, `torch.cuda.max_memory_allocated` remis à zéro avant les épisodes, `lanceur_v5.py` l. 273, 278) ; cache à 2 144 jetons × 8 lignes = 2,1 Gio ; reste ≈ 1,3 Gio de transitoires.
- À T = 10 : le contexte le plus long borne le pic (`chrono["longueur_remplie_max"]`, `episode.py` l. 244–245). Borne : L_max ≤ L₀ + 9 × (400 jetons générés + observation) ; avec L₀ ≈ 700 et un pas ≈ 350 (E3 bis : 1 744 ≈ 700 + 3 × 350) → L_max ≈ 3 900 ; au pire (actions à 400 jetons, observations longues) ≈ 5 200. Cache à 5 600 jetons × 8 × 128 Kio ≈ **5,5 Gio** ; transitoires du préremplissage (états cachés 8 × 5 200 × 4 096 × 2 = 0,34 Go, intermédiaire du perceptron 8 × 5 200 × 14 336 × 2 ≈ 1,2 Go). **Pic estimé ≈ 22 à 25 Gio**, bien sous 80 Go.
- Surcoût de la fraction 0,5 sur la carte : l'indexation `h[self.lignes]` crée une copie bfloat16 (k × L × 4 096 × 2 ≤ 0,34 Go pour k = 8, L = 5 200) et, **si la conversion en float32 se fait sur la carte avant la copie** (comportement de `tensor.to("cpu", dtype)` : hypothèse non vérifiée ici, sans carte), un transitoire float32 ≤ 0,68 Go, libéré au retour du crochet : ≤ 1 Go, par couche et séquentiellement.

Ce qui est **hypothèse** : (1) le noyau d'attention `sdpa` avec masque de remplissage reste en mémoire linéaire (noyau efficace) ; si le noyau mathématique était choisi, les scores (8 × 32 × L² × 2 octets) pèseraient ≈ 13,8 Go à L = 5 200 — le total resterait ≈ 36 Gio < 80 Go ; (2) les longueurs de contexte à T = 10 (L₀, pas par tour) ne sont connues que par E3 bis à T = 4 ; (3) l'ordre de la conversion/copie dans `to("cpu", float32)`. Aucun scénario calculé ne dépasse 80 Go ; le temps : la capture n'ajoute que des copies carte → processeur de ≤ 85 Mo par couche et par préremplissage et de 16 Ko par passe de décodage, cohérent avec « ≤ 10 % » de l'ordre, non mesuré. Le pic réel sera lu dans `descriptifs.memoire_pic_gio` (l'extracteur le rend).

### 5.3 L'amorce lance-t-elle le bras B d'office après la course ? (ordre § 5 étape 4, l. 69)

Lu dans `scripts/amorce_instance_t06_v11.sh` : `bras_b()` (l. 418–442) est appelé à la fin normale, après la poussée finale (l. 553 : `pousser && … bras_b || true ; arreter_instance "fin du run" 0`). Il **n'est pas lancé** si `BRAS_B=0` (l. 420), si `MODE` ≠ `reel` (l. 421), **si `EPREUVE_GO_ID` est non vide et `BRAS_B_EPREUVE` ≠ 1** (l. 422 : journal « bras B : non lancé (épreuve à blanc) »), ou si la configuration du bras B est absente du commit (l. 423). Le run exploratoire passe par `controles-epreuve` → `creation` avec `EPR=oui`, et la commande imprimée porte `-e EPREUVE_GO_ID=GO-2026-11-08-11 -e MODE=reel -e PREREG_ABSENT=1 -e CONFIG=…` (`lancer_t06_v13.sh` l. 232) et jamais `BRAS_B_EPREUVE` : **le bras B est débrayé d'office sous la ligne exploratoire**, sans changement de la v13 ; le journal portera « bras B : non lancé (épreuve à blanc) ». Il ne serait lancé d'office que pour la course sous GO-2026-11-02-28 (sans `EPREUVE_GO_ID`). Les 0,33 h du bras B retirées du devis (§ 8) sont donc justes.

## 6. Liste exacte des fichiers du commit d'épreuve sur `prep/t06-explo-v1` (= `7822a65b` + …), sans la créer ni la commettre

Vérifiable par `git diff --name-only 7822a65b <<COMMIT_EXPLO>>` (comme `c01d29ea` pour E3 bis) :

1. `scripts/lancer_t06_v13.sh`
2. `scripts/amorce_instance_t06_v11.sh`
3. `src/controle_ia/t06/session_v12.py`
4. `src/controle_ia/t06/configuration_v6.py`
5. `src/controle_ia/t06/lanceur_v6.py`
6. `tests/test_t06_chaine_v13.py` (pas dans la liste figée v2 des essais de l'instance : joué sur processeur par la mère)
7. `docs/notes/g0-deux-semaines-v1/e3-ter-v1/config-t06-course-explo-v1.json`
8. `docs/notes/g0-deux-semaines-v1/e3-ter-v1/config-t06-course-explo-v1.json.sha256` (compagnon, `controle_ia.scellement sceller`)
9. `registres/go.md` portant la ligne GO-2026-11-08-11 **lisible par la chaîne et la garde** (§ 1, point 2 ; la ligne actuelle de `main` est refusée)

Rien d'autre : ni l'extracteur, ni ses essais, ni ce rapport (ils vivent sur `main`, la lecture A se fait sur processeur depuis `main`) ; les tâches, consignes et sondes citées sont déjà dans `7822a65b`. Le clonage réduit de l'amorce (`CHEMINS_CLONAGE`, l. 255–282) couvre `/docs/notes/`, `/registres/*.md`, `/scripts/`, `/src/`, `/tests/` : la configuration et son compagnon seront sur l'instance.

**Attention, deux versions de la chaîne v13 coexistent** : le zip `livrables/chaine-t06-v13-v1.zip` (`98f7d4cd…`, cité par le rapport du développeur v13 : `lancer_t06_v13.sh` `d23290943cc13ccfeedc5a2c4a25c71cc2ea8913d8c65d1b7edb1f2947befe0c`, `test_t06_chaine_v13.py` `3a469da71847db79e32900f79f00c5282208622069f2064d0ac476bb082e1c60`) et l'arbre de travail au 8 novembre 15:21 UTC (`lancer_t06_v13.sh` `6940a337d5e0c9a736aa7087275c5f6328133b67ed4df1c94535ba06a1965416`, `test_t06_chaine_v13.py` `ac81904423bc59309423a81ff99c2d62b0cce990782b53fad58eb29892897ada` ; 87 lignes d'essais ajoutées ou changées, section 6 « jeton GitHub sous l'un ou l'autre nom `CONTROLE_IA_GITHUB_TOKEN` / `CONTROLE_IA_GITHUB_TOKEN_2` », `jeton_gh_nom()` dans le lanceur) ; `amorce_instance_t06_v11.sh`, `session_v12.py`, `configuration_v6.py`, `lanceur_v6.py` sont identiques dans les deux. La mère choisit la version à commettre ; `<<COMMIT_V13>>` et la contre-lecture (R2) doivent citer les empreintes de celle-là.

## 7. Réserves

1. **Bloquant (a), registre** : la cellule « accordé par » de GO-2026-11-08-11 (`registres/go.md` l. 282) doit valoir exactement `Lazar` pour la chaîne et la garde ; le registre dit « une ligne par GO, jamais modifiée » et une ligne d'extension ne corrige pas la première (`verifier_go_v3` lit `propres[0]`, l. 62–66) : décision de la mère (ligne neuve sous un identifiant neuf, ou correction assumée et consignée). Les marqueurs `<<GO_COURSE_EXPLO>>` de l'ordre et `go_id` de la configuration suivront l'identifiant retenu (une configuration v1 bis, R12, si l'identifiant change).
2. **Bloquant (b), registre** : la ligne 280 (GO-2026-11-08-09, échéance « 2026-11-08 ≈ 21:34Z ») rend le registre illisible pour `garde_calcul.py` (l. 66–70) : aucune commande `vastai create instance` ne passe la garde, et `lancer_t06_v13.sh creation` la rejoue (l. 234). À régler avant toute création, quel que soit le GO.
3. La **règle E3-6** de l'extracteur est ma transcription (§ 4.2) : l'ordre dit « attendu conforme pour les six états et la distillation » (§ 3) et « probabilité de moins de 10 contrôlées ≈ 0 » (§ 2) mais ne pose pas la liste ; à contre-lire (R2), le script est écrit pour être relu avant la création (§ 5 étape 0).
4. `fin_go_utc` reste `2026-11-17T00:00:00Z` (§ 3.2) ; si la mère voulait littéralement « 2026-11-16 », le code le refuse (démontré).
5. `carte.relance.prix_max_usd_h` 0,01 est **un champ changé de plus que la lettre de l'ordre** (qui prévoyait « retirée ou prix 0 », refusés par le code) : à confirmer par la mère ; l'alternative (bloc inchangé) est écrite au § 5.1.
6. Le rejeu des paires repose sur `numpy` : même version qu'au manifeste pour E3 bis (2.4.6) ; pour le run exploratoire, l'extracteur imprime les deux versions pour que la lecture le note.
7. L'extracteur lit `descriptifs.memoire_pic_gio` et les durées, non le journal `PROGRES` (durées par étape) : la mère les relève au journal comme à E3 bis (cl1 § 4, point 7).
8. Les deux versions de la chaîne v13 (§ 6) : le rapport v13 et son éventuelle contre-lecture portent sur le zip ; l'arbre de travail a bougé pendant ma mission (suite d'essais encore en cours ailleurs) ; je n'ai modifié aucun de ses fichiers.

Heure de fin du rapport (`date -u`) : 2026-11-08 ≈ 15:33 UTC.
