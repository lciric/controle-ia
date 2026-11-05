# SPARKS-EXP7-NUL — additif v9 au rapport du développeur (code v9 : protocole du tir et boucle de redémarrage)

Même rédacteur-développeur. Tâche : message de la mère du 5 novembre 2026 (vers 04:25 UTC). Il fait suite à la
contre-lecture du delta v5 → v8 (`contre-lecture-delta-v8-v1/contre-lecture-delta-v8-v1.md`, `e2f34fba…`, compagnon « OK »,
lue en entière). Travail de 04:25 à 06:35 UTC environ (`date -u`), plusieurs redémarrages du conteneur compris.

Interdits tenus : aucune poussée, aucun `.sha256` sur `main`, aucun réseau, aucun modèle, aucune dépense, aucune clé lue,
aucun texte touché (les 15 couples du brouillon 7 restent ceux du contre-lecteur).

**Verdict.**
- Code v9 : branche locale `prep/sparks-exp7-nul-v9`, commit `4d07d2a6830ab09cb91250016284efb5cbe8a91c`.
- Deux commits sur `4fd10407` : `a655bbfa`, puis la correction `4d07d2a6` (section 1 (b), identifiants de démarrage). 20 fichiers neufs, aucun fichier modifié.
- Liste fermée v9 conforme : « LISTE FERMÉE CONFORME : 188 fichiers ».
- Tir réel libéré par Lazar : clé d'instance acceptée et déclarée (R-1533), GO-2026-11-05-02. La mère a poussé `4d07d2a6` sur `prep/sparks-exp7-nul-v9` ; le tir part chez la fille.
- **Aucune contre-lecture du delta v9 (R-1534, mot de Lazar) : réserve.**
- Comptes : section 3. Répétition : section 4. Commande du tir : section 5.

## 1. Ce qui change (une ligne par point de la consigne et de la contre-lecture)

### (a) Mode tir du lanceur (`scripts/lancer_sparks_exp7_nul_v9.sh`, `src/controle_ia/sparks_exp7_nul_v9/vast_lecture.py`)

**Offre (point 11).**
- `recherche` imprime `vastai search offers 'num_gpus=1 rentable=true verified=true' -o dph_total --raw`. La sortie brute va
  dans un fichier, la sortie d'erreur dans un autre.
- `offres` lit le fichier en JSON strict, puis l'efface. Il garde les offres avec `resource_type` = « gpu », `num_gpus` = 1,
  `dph_total` > 0 et `storage_cost` ≥ 0, triées par prix croissant, au plus 4.
- Il n'imprime que `id`, `dph_total`, `storage_cost`, `resource_type` et les prix, et les écrit dans
  `offres-retenues.json`.
- **Règle des prix, écrite dans le module** :
  - `PRIX_CARTE` = `dph_total` de l'offre retenue ;
  - `PRIX_STOCKAGE` = `storage_cost` × 20 Go ÷ 730 h.
- `tir <COMMIT_CODE> <GO_ID> [MINUTES] [RANG]` prend l'offre de son rang. Les prix ne sont plus saisis à la main.

**Jeton (point 12)** : `-e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN` est écrit dans la commande du tir et dans celle de la
création, comme pour R1 v4 (N-009). Le jeton de la session n'est plus passé.

**Inventaire (point 10)** : `vastai show instances --raw`, la sortie d'erreur à part, lu en JSON strict et filtré par
identifiant entier.
- « Absente » : `{"instances": null}`, ou une liste lue sans cet identifiant.
- Tout le reste est « illisible » : un texte d'erreur (« 404 »), un objet d'erreur, un identifiant non entier dans la
  liste, un `actual_status` qui n'est pas une chaîne, du texte après le JSON.
- `actual_status` nul est lu « en_creation ».
- Aucun motif `404` n'est lu.
- Seuls l'identifiant, l'état, `cur_state` et `dph_total` sont imprimés.
- Chaque lecture est ajoutée à `etats-<ID>.txt`.

**Boucle de redémarrage (point 8, consigne a).** `boucle <ID>` rend un verdict sur les lectures de `etats-<ID>.txt` :

| Verdict | Condition |
|---|---|
| « absente » | la dernière lecture est absente |
| « indecis » | moins de 3 lectures, ou moins de 300 s entre la première et la dernière des trois |
| « arretee » | les trois dernières sont « exited » avec `cur_state` « stopped » |
| « boucle » | tous les autres cas |

Sur « boucle », le lanceur imprime la destruction par l'identifiant avec `-y`, puis « NŒUD ». Le journal de Vast
(`vastai logs <ID> --tail 400`) est lu par `journal-amorce` :
- lignes « AMORCE V5 » prises **sans ancre** (point 18) ;
- comptes `REDEMARRAGES=` et `BOUCLE_PRESUMEE=`.

Les démarrages sont aussi comptés par l'amorce, dans le registre des démarrages (voir (b)).

**Sorties brutes (point 16)** :
- création, `start`, `destroy` : effacées par le lanceur ;
- offres, inventaires, journaux : effacées par `vast_lecture.py`, lisibles ou non, avec leur `.err` ;
- rien n'est versé.

**« no_such_ask » (point 14)** :
- sans identifiant rendu, c'est un refus net : « OFFRE RETIRÉE », code 7, aucun marqueur ;
- le lanceur imprime alors la commande `tir … RANG+1`, au plus jusqu'au rang 4 ; au-delà, « nouvelle recherche » ;
- un identifiant rendu l'emporte toujours (« CRÉÉE »).

**`start` refusé avec HTTP 200 (point 15).** « ENVOYÉ » seulement si la sortie porte la ligne exacte
`starting instance <ID>.`, ou `destroying instance <ID>.` pour `destroy` (texte de `start_instance_impl` et
`destroy_instance_impl`, `vastai` 1.8.3). Sinon, c'est « REFUSÉ », code 5.

**GO du tir (point 17)** : `sparks_exp7_nul_v9/tir.py` exige que le périmètre de la ligne nomme « SPARKS » et « tir »
(mot entier). Sinon, c'est le contrôle de la v5 (calcul, Lazar, au plus 5 USD, validité, révocation).

### (b) Amorce v9 (`scripts/amorce_instance_sparks_exp7_nul_v9.sh`) : la boucle est détectée par l'amorce elle-même

**Au redémarrage, un ordre neuf est exigé.** Les cas suivants sont tous traités comme une **boucle présumée** :
- branche des ordres absente ou illisible ;
- ordre déjà fait ou refusé ;
- ordre mal lu ;
- consignation impossible ;
- tout refus qui précède l'ordre : identifiant, commit du disque, GO à la date.

Dans tous ces cas, la machine écrit `sparks-v5-detruire`, ce qui déclenche une **destruction immédiate par la
minuterie**, sans attendre l'échéance. L'amorce attend la minuterie, puis sort en code 2.

**Création relancée.** Une création relancée sur un disque où elle a déjà été tentée sans dépôt extrait
(`sparks-v9-creation-tentee`, par exemple après un clonage impossible) est aussi une boucle. Sans ce contrôle, la création
se rejouerait à chaque tour.

**Chaque redémarrage est consigné au registre des démarrages, avant tout le reste** :
- plafond de 5 minutes, puis durée réelle à la fin du démarrage (`trap … EXIT`) ;
- le rang du démarrage est écrit au journal (« démarrage n° N ») ;
- la borne de la machine compte donc les démarrages d'une boucle (point 9).

**Identifiants de démarrage jamais réutilisés** (correction `4d07d2a6`, trouvée par la répétition locale, run 3).
- Le défaut : deux démarrages lancés dans la même seconde recevaient le même identifiant (`date +%s`). Le registre gardait
  alors un seul plafond par identifiant ; le plafond de 10 minutes de la copie, sans fin consignée, était écrasé par celui
  de la phase causale, et la borne était sous-estimée.
- La cause existait dès la v5. Une boucle serrée la rend plus probable.
- `nouvel_id` rend l'instant, ou le plus grand identifiant du registre + 1.

**L'ordre est consigné « fait » avant la borne.** Un refus après lui (borne ou prix illisibles, plafond trop bas, gardes non
passées) ne se rejoue pas : à la relance suivante, l'ordre n'est plus neuf, donc c'est une boucle, donc une destruction.

**Ordre « fin » avant la borne (point 19)** : un registre illisible n'empêche plus la destruction.

**Fin de la phase causale (point 5)** : « fin de la phase causale, code N, poussée vérifiée|non vérifiée ». Le message
« sans poussée vérifiée » n'est plus écrit quand la poussée est vérifiée.

**Prix de la boucle, déclaré (R4).** Au redémarrage, un ordre absent par incident de réseau (« ordres illisibles ») est lu
comme une boucle : l'instance est détruite avec ses modèles. C'est le choix de la consigne, qui protège la dépense plutôt que
les modèles. Le protocole écrit l'ordre et le pousse avant tout `start` ; cette séquence est inchangée.

### (c) Mineurs de la contre-lecture qui touchent le code

- Points 5, 10, 11, 12, 14, 15, 16, 17, 18 et 19 : faits, voir ci-dessus.
- Point 13 : la commande du tir (section 5) ne demande plus de sceller avant le tir.
- Points 6, 7, 26, 27 et 28 : textes ou risques déclarés. Ils ne touchent pas le code et restent aux couples du brouillon 7.

**Fichiers neufs** (branche `prep/sparks-exp7-nul-v9`, chacun avec son compagnon `.sha256`) :

| Fichier | sha256 |
|---|---|
| `scripts/amorce_instance_sparks_exp7_nul_v9.sh` | `e465e601325f6306b92873b5b7f3ac93815414ec71491cb83f4241cb972c0eb4` |
| `scripts/banc_mutations_sparks_exp7_nul_v9.py` | `aaa79161543e48e3da8a398cd96ffa1f00290f598940898824a4335855da5b4c` |
| `scripts/lancer_sparks_exp7_nul_v9.sh` | `53715b64183ee351c8c0b854a3b7ba522975c9638531c26b8283c685315630be` |
| `scripts/sparks_exp7_nul_instance_v9.sh` | `9d7bc05d35138ec1fbe5a6b80c902a091c3c2a6853956edbfce9d334ae661403` |
| `src/controle_ia/sparks_exp7_nul_v9/__init__.py` | `231f0f717cd40b6f38b87459bd51b55c8a934897e841f782ba5e417d44cf26c5` |
| `src/controle_ia/sparks_exp7_nul_v9/garde_code.py` | `5ad495acf061edbfd205f6212d42418c8cc8b564700dc06292239fa14a9c4841` |
| `src/controle_ia/sparks_exp7_nul_v9/liste-fermee-v1.txt` | `21716cc359888f582b6d5485f4948ec961596334a4df03171b7539f327383d90` |
| `src/controle_ia/sparks_exp7_nul_v9/tir.py` | `8cdc256cfb098523b409bcfb28faaba5516f7942a52eaa8d8779fc1ccfc86e2f` |
| `src/controle_ia/sparks_exp7_nul_v9/vast_lecture.py` | `883a25880d1e25490496680303c2204e83648e6a20190a9722362391cb3cb958` |
| `tests/test_sparks_exp7_nul_v9.py` | `d611e804fe45b05f1c23133a1d19b9a45bcae22f7abfea9e9d30c6b332c9edcd` |

Le script d'instance v9 est celui de la v8 : seuls changent la garde v9 et les essais v9. `manifeste_phase` et
`addendum_factice` restent ceux de la v8.

**Essais.** `tests/test_sparks_exp7_nul_v9.py` reprend l'essai v8, adapté au nouveau comportement :
- inventaire strict, en 13 cas ;
- `start` lu, en 7 cas ;
- « no_such_ask » ;
- refus au redémarrage, qui donnent désormais une boucle et un DELETE ;
- registre à quatre lignes.

Il ajoute la section 7 :
- offres et prix ;
- verdict de boucle, en 8 cas ;
- inventaires successifs ;
- journal de l'amorce sans ancre ;
- périmètre du GO, en 6 cas ;
- « no_such_ask » jusqu'au rang 4 ;
- boucle après une création refusée, avec un **témoin sans détection** (aucun DELETE) ;
- création relancée sans dépôt ;
- ordre « fin » avant la borne ;
- ordre consommé avant la borne ;
- message causal exact ;
- aucun `exit` avant l'ordre consommé ;
- sorties brutes effacées même illisibles.

**Banc v9.** Tout le banc v8 (v1 à v8), plus **31 mutations v9** (liste dans `scripts/banc_mutations_sparks_exp7_nul_v9.py`).

## 2. Ce que le tir v9 éprouve, et ce qu'il n'éprouve pas

Le tir crée une instance au commit de tir, qui porte le code v9 sans addendum. L'amorce v9 clone, puis s'arrête à la garde du
code (« code ou addendum non conformes »), et le conteneur sort. Deux issues :
- **pas de boucle** : trois lectures « exited » avec `cur_state` « stopped » sur au moins 5 minutes, et `REDEMARRAGES=0`.
  L'ordre « fin » est poussé, puis `start` est envoyé. L'amorce lit l'ordre, se détruit, et l'inventaire rend « absente » ;
- **boucle** : la relance automatique refait l'amorce, qui trouve le disque, ne trouve aucun ordre et se détruit aussitôt.
  Le verdict rend « absente », et le journal porte « boucle de redémarrage présumée ». Si la machine ne se détruit pas, le
  verdict rend « boucle » et la session détruit l'instance par l'identifiant. Dans les deux cas, **nœud de Lazar** (points 8
  et 9).

Le tir n'éprouve ni `vastai copy`, ni la phase causale réelle, ni la copie d'un lot (risques déclarés, point 6).

## 3. Essais et banc

Fichiers d'essai : `tests/test_sparks_exp7_nul_v1.py` à `v4.py` et `tests/test_sparks_exp7_nul_v9.py`. Les sorties brutes, sans `.sha256`, sont dans `essais-et-banc-sparks-v9/`, et celles du premier commit dans son sous-dossier `commit-a655bbfa/`.

**Commit final `4d07d2a6`** :

| Passage | Résultat | Sortie | sha256 |
|---|---|---|---|
| Essais à la tête | 331 réussis, 0 échec, 0 sauté, code 0 | `essais-tete-4d07d2a6.txt` | `71547865c3adcb733e74153696336e3cbfd11c6e2f5ec00645f1d4c8cd990af7` |
| Essais sur le commit enfant `2cc4bb27` (addendum factice, `COMMIT_CODE=4d07d2a6…`) | 331 réussis, 0 échec, 0 sauté, code 0 | `essais-enfant-2cc4bb27.txt` | `813cc56742f8a2774cb9fc51bff441aadcfe45a55cdadc7b4d67fc99dce2f163` |
| Banc de mutations v9 | 232/232 tuées (code 1 et « failed ») : 22 v1, 52 v2, 40 v3, 30 v4, 30 v5, 6 v6, 7 v7, 11 v8, 34 v9 ; 8 témoins verts ; 0 défaut ; code 0 | `banc-4d07d2a6.txt` | `535b8730730dadc09183008a2a8e10681dab0c8faf239aee4d2ad174ca3cf45b` |
| Banc, détail | une ligne par mutation | `banc-4d07d2a6.json` | `3700b1b781f6117d68a1112c3209fa68385915f0a8036bc50dcad95d40dc1d75` |
| Exemple de sortie du mode tir (factice, hors réseau) | code 0 | `exemple-sortie-tir.txt` | `43ef8faf74f2fc711a80ecb6edf2b89b2ac1b1673b56e11a068013b4bb725abc` |

**Premier commit `a655bbfa`**, dont tous les runs sont comptés (R4) :

| Passage | Résultat | Sortie | sha256 |
|---|---|---|---|
| Essais à la tête | 329 réussis, 0 échec, 0 sauté | `commit-a655bbfa/essais-tete-a655bbfa.txt` | `ba764c16e7f74712e698d8af198acb3e144a467b334c3b40843d4075b855c0e1` |
| Essais sur le commit enfant `c2689059` | 329 réussis, 0 échec, 0 sauté | `commit-a655bbfa/essais-enfant-c2689059.txt` | `2a70ae06b9af07ae954f0a86a37e6e4a823ef226bfe2817954bcacda85987d2d` |
| Banc | 229/229 tuées (31 v9), 8 témoins verts, 0 défaut | `commit-a655bbfa/banc-a655bbfa.txt` | `9fb497cb05b107f72556b751d49a8020437845cbdcf78a9c6345fc5dcf8f74db` |
| Banc, détail | une ligne par mutation | `commit-a655bbfa/banc-a655bbfa.json` | `a00788e2bdca2baabb427a78cb3baec243b60230e944d96b35bfecfc8e83097f` |

**Avant le premier commit**, l'essai v9 a été joué trois fois pendant son écriture, sur des fichiers non committés :
- 1 échec, arrêt au premier ;
- 6 échecs : la capture du code sous `set -e` dans le lanceur, que la correction remplace par `R=0; … || R=$?` ; deux attendus d'essai faux ; le faux `vastai` d'un essai, qui n'imprimait pas « destroying instance 1. » ;
- 0 échec.

Entre les deux commits, les essais neufs de la correction ont été joués une fois, ciblés : 5 réussis.

**Sauts** : les témoins v6 et v9 du banc sautent chacun un essai, parce que la copie du banc n'est pas un dépôt git (essai du mode tir). Le même essai passe à la tête comme sur l'enfant.

**Réserve (R4).** Les résultats sont propres. Mais :
- `vastai` n'est éprouvé que par des sorties imitées d'après sa source 1.8.3 ;
- la forme réelle de `show instances --raw`, et les valeurs de `actual_status` et `cur_state` d'une instance sortie seule, ne sont connues que par la source et le registre, pas par un appel ;
- le verdict de boucle est donc prudent : un `cur_state` resté « running » après une sortie lit « boucle ». Ce cas reste à trancher par le tir, avec le compte `REDEMARRAGES=` du journal.

## 4. Répétition jouet

**Jouée par moi, en local** (`unshare -pf`, aucun réseau, aucune poussée distante). Script : `essais-et-banc-sparks-v9/repetition-v9-locale.sh`.

Dispositif :
- dépôt nu local qui emprunte les objets du dépôt de travail (`alternates`, frontière superficielle recopiée) ;
- `DEPOT_URL=file://…` ;
- commit lancé = code v9 + addendum factice (écrit par `addendum_factice.py`) + registre des GO de `main` ;
- ordres poussés au dépôt nu ;
- faux `curl` journalisé.

Étapes :
1. création (fabrication jouet) ;
2. ordre 1 « copie » ;
3. ordre 2 « causal » ;
4. **relance sans ordre neuf**, c'est-à-dire une boucle. Elle remplace les étapes « rejoue » et « fin » de la v8 : en v9, la
   relance d'un ordre déjà fait est une boucle, qui détruit.

Attendus neufs :
- « démarrage n° N » à chaque redémarrage ;
- « fin de la phase causale, code [1-9], poussée vérifiée » (point 5) ;
- à l'étape 4, « ordre refusé (aucun ordre neuf) : boucle de redémarrage présumée, destruction immédiate » ;
- un seul DELETE.

Runs, tous comptés (R4) :
- **run 1** (`repetition-jouet-v9-locale-v1/`) : défaut du dispositif, pas du code. Le commit lancé ne portait pas le
  registre des GO de `main`, donc la ligne d'extension à 40 USD manquait.
  - Création : « GO non conforme : aucun calcul ».
  - Les relances suivantes ont toutes été lues comme des boucles (« GO-2026-11-04-04 non conforme à la date : boucle de
    redémarrage présumée, destruction immédiate ») : 3 DELETE, un par relance. Le faux `curl` laisse la machine en vie, ce
    qu'une vraie destruction ne ferait pas.
  - Fait utile : la détection marche aussi sur un refus qui précède l'ordre.
- **run 2** (`repetition-jouet-v9-locale-v2/`) : autre défaut du dispositif. L'addendum factice était écrit sous un autre
  nom, et son compagnon nommait `addendum.md`.
  - La garde du manifeste l'a refusé à juste titre : « MANIFESTE REFUSÉ : … nom 'addendum.md' au lieu de
    'SPARKS-EXP7-NUL-addendum-1.md' », puis arrêt avant tout calcul.
  - Run arrêté par moi après l'étape 1, par numéros de processus (R10).
- **run 3** (`repetition-jouet-v9-locale-v3/` et `essais-et-banc-sparks-v9/commit-a655bbfa/repetition-locale-v3-sortie.txt`, `422bf67b…`), au commit `a655bbfa` : complet, **tous les attendus « OK »**.
  - Fabrication : « ARRET 0/28 modèles dans les bornes », manifeste créé, poussée vérifiée.
  - Copie : « démarrage n° 2 », « lot impossible ».
  - Phase causale : « fin du calcul, code 1 », puis « fin de la phase causale, code 1, poussée vérifiée ». La cause du code 1 est lue au `run.err` : le départ « jouet » est cherché sur Hugging Face, hors réseau (point 6 de la contre-lecture).
  - Relance sans ordre neuf : « démarrage n° 6 », « boucle de redémarrage présumée, destruction immédiate ».
  - Un seul DELETE, aucune minuterie restante.
  - **Défaut trouvé à la lecture du registre des démarrages (R4)** : deux démarrages lancés dans la même seconde portaient le même identifiant, et le plafond de la copie était écrasé. Corrigé par `4d07d2a6` (`nouvel_id`), avec 2 essais et 3 mutations neufs.
- **run 4** (`repetition-jouet-v9-locale-v4/`, `essais-et-banc-sparks-v9/repetition-locale-v4-sortie.txt`, `a8f972ec…`), au commit final `4d07d2a6` : **interrompu** par un redémarrage du conteneur, juste après l'écriture du commit lancé et avant la création. Il n'est pas rejoué : la mère et Lazar ont demandé de ne plus lancer de répétition (R-1534).

**Aucune répétition complète au commit final** : réserve. La différence `a655bbfa..4d07d2a6` se limite à `nouvel_id` dans l'amorce, avec ses essais et ses mutations.

**Commande de la répétition sur le dépôt de travail** (pour la mère, avec réseau). C'est celle de la v8 (rapport v8,
section 5), avec ces changements :
- `CODE=4d07d2a6830ab09cb91250016284efb5cbe8a91c` ;
- amorce v9 ;
- branche `essai/sparks-v9-repetition` ;
- étapes 4 et 5 de la v8 remplacées par l'étape 4 ci-dessous ;
- attendus de la section précédente.

Il faut d'abord pousser la branche `prep/sparks-exp7-nul-v9` : `worktree add … "$CODE"` exige que le commit soit connu du
dépôt où l'on joue.

```bash
#!/usr/bin/env bash
set -uo pipefail
CODE=4d07d2a6830ab09cb91250016284efb5cbe8a91c
DEPOT=/home/user/controle-ia-travail
URL=https://github.com/lciric/controle-ia-travail.git
J=$(mktemp -d /tmp/repetition-sparks-v9-XXXX); mkdir -p "$J/faux-bin" "$J/racine" "$J/home"
T() { timeout -k 10 "$@"; }
T 600 git -C "$DEPOT" worktree add -q --no-checkout -b essai/sparks-v9-repetition "$J/prep" "$CODE"
T 60 git -C "$J/prep" sparse-checkout set --no-cone '/*' '!/*/' '/prereg/SPARKS-EXP7-NUL-*' '/registres/go.md'
T 600 git -C "$J/prep" checkout -q essai/sparks-v9-repetition
cp "$DEPOT/registres/go.md" "$J/prep/registres/go.md"
T 60 git -C "$DEPOT" show "$CODE:src/controle_ia/sparks_exp7_nul_v8/addendum_factice.py" > "$J/addendum_factice.py"
T 60 python3 -I -B "$J/addendum_factice.py" "$J/prep/prereg/SPARKS-EXP7-NUL-addendum-1.md" "$CODE" || { echo "addendum factice non écrit : arrêt"; exit 2; }
T 60 git -C "$J/prep" add -A && T 60 git -C "$J/prep" -c user.name=essai -c user.email=essai@invalid commit -qm "essai : répétition v9 (addendum factice marqué)"
T 300 git -C "$J/prep" push -q origin essai/sparks-v9-repetition || { echo "poussée de la branche d'essai impossible : arrêt"; exit 2; }
LANCE=$(git -C "$J/prep" rev-parse HEAD); COURT=${LANCE:0:12}
printf '#!/bin/bash\necho "curl $*" >> "%s/faux.log"\nprintf 200\n' "$J" > "$J/faux-bin/curl"; chmod +x "$J/faux-bin/curl"
cp "${HOME}/.gitconfig" "$J/home/.gitconfig" 2>/dev/null || true
PROXY=(); for v in HTTPS_PROXY HTTP_PROXY NO_PROXY https_proxy http_proxy no_proxy GIT_SSL_CAINFO SSL_CERT_FILE REQUESTS_CA_BUNDLE; do
  [ -n "${!v:-}" ] && PROXY+=("$v=${!v}"); done
ENV=(env -i PATH="$J/faux-bin:/usr/sbin:/usr/bin:/sbin:/bin" HOME="$J/home" GIT_CONFIG_GLOBAL="$J/home/.gitconfig" "${PROXY[@]}"
     RACINE_AMORCE="$J/racine" MODE=jouet BRANCHE_PREFIXE=essai/ VENV_EXISTANT="$DEPOT/.venv" GO_DATE="$(date -u +%F)"
     COMMIT="$LANCE" COMMIT_CODE="$CODE" GH_TOKEN="${GH_TOKEN:-}" PRIX_HEURE_USD=0.8 PRIX_STOCKAGE_HEURE_USD=0.05
     ECHEANCE_UTC_S=$(( $(date +%s) + 10800 )) CONTAINER_ID=1 CONTAINER_API_KEY=factice DEPOT_URL="$URL")
A="$J/amorce-v9.sh"; T 60 git -C "$DEPOT" show "$CODE:scripts/amorce_instance_sparks_exp7_nul_v9.sh" > "$A"
etape() { T 5400 unshare -pf --mount-proc "${ENV[@]}" bash "$A" > "$J/$1.txt" 2>&1; echo "== $1 : code $?"; }
attendu() { if grep -qE -- "$3" "$2"; then echo "   OK   $1 : « $3 »"; else echo "   ÉCART $1 : « $3 » absent de $2"; fi; }
absent() { if grep -qE -- "$3" "$2" 2>/dev/null; then echo "   ÉCART $1 : « $3 » présent dans $2"; else echo "   OK   $1 : pas de « $3 »"; fi; }
O="$J/ordres-depot"; T 60 git init -q "$O"; T 60 git -C "$O" remote add origin "$URL"; mkdir -p "$O/ordres"
ordre() { echo "$2" > "$O/ordres/ordre-$1.json"; T 60 git -C "$O" add ordres && T 60 git -C "$O" -c user.name=essai -c user.email=essai@invalid commit -qm "essai : ordre $1" \
          && T 300 git -C "$O" push -q origin "HEAD:refs/heads/ordres/sparks-exp7-nul-v5-$COURT"; }
etape 1-creation
attendu 1 "$J/1-creation.txt" "mode jouet : addendum non exigé"
attendu 1 "$J/1-creation.txt" "fabrication, durée plafonnée"
attendu 1 "$J/racine/sparks/journal.txt" "essais : [0-9]+ passed"
attendu 1 "$J/racine/sparks/journal.txt" "essai d'égalité des lots : oui"
attendu 1 "$J/racine/sparks/journal.txt" "MANIFESTE CRÉÉ : runs/.*préenregistrement prereg/SPARKS-EXP7-NUL-addendum-1.md"
attendu 1 "$J/racine/sparks/journal.txt" "ADDENDUM FACTICE \(jouet\)"
absent  1 "$J/racine/sparks/run.err" "No module named"
attendu 1 "$J/racine/sparks/run.err" "ARRET 0/28 modèles dans les bornes"
attendu 1 "$J/racine/sparks-v5-demarrages.txt" "^d [0-9]+ [0-9]+$"
ordre 001 '{"numero": 1, "instance": "1", "phase": "copie", "deja_usd": 1.0, "cas": ["vraie01"], "premier": true, "copie_minutes": 5}'
etape 2-copie
attendu 2 "$J/2-copie.txt" "redémarrage consigné au registre des démarrages : démarrage n° 2"
attendu 2 "$J/2-copie.txt" "ordre 1 \(copie\)"
attendu 2 "$J/2-copie.txt" "lot impossible"
absent  2 "$J/2-copie.txt" "boucle de redémarrage présumée"
mkdir -p "$O/ordres/causal/reponses" && echo '{}' > "$O/ordres/causal/cle-ouverte-v1.json" && touch "$O/ordres/causal/reponses/.garde"
ordre 002 '{"numero": 2, "instance": "1", "phase": "causal", "deja_usd": 2.0}'
etape 3-causal
attendu 3 "$J/3-causal.txt" "ordre 2 \(causal\)"
attendu 3 "$J/racine/sparks-causal-002/journal.txt" "MANIFESTE CRÉÉ : runs/.*préenregistrement prereg/SPARKS-EXP7-NUL-addendum-1.md"
absent  3 "$J/racine/sparks-causal-002/run.err" "No module named"
attendu 3 "$J/racine/sparks-causal-002/journal.txt" "fin du calcul, code [1-9]"
attendu 3 "$J/3-causal.txt" "fin de la phase causale, code [1-9], poussée vérifiée"
absent  3 "$J/3-causal.txt" "boucle de redémarrage présumée"
etape 4-relance-sans-ordre-neuf
attendu 4 "$J/4-relance-sans-ordre-neuf.txt" "démarrage n° 6"
attendu 4 "$J/4-relance-sans-ordre-neuf.txt" "ordre refusé \(aucun ordre neuf\) : boucle de redémarrage présumée, destruction immédiate"
echo "   DELETE au journal : $(grep -c 'DELETE instance 1 ' "$J/racine/sparks-v5-minuterie.log") (attendu : 1)"
if pgrep -f "$J/racine/sparks-v5-minuterie.sh" >/dev/null; then echo "   ÉCART : minuterie restante"; else echo "   OK   aucune minuterie restante"; fi
echo "   branches à supprimer par Lazar : essai/sparks-v9-repetition essai/sparks-exp7-nul-v5-$COURT essai/sparks-exp7-nul-causal-v5-$COURT-002 ordres/sparks-exp7-nul-v5-$COURT"
T 120 git -C "$DEPOT" worktree remove --force "$J/prep"; T 60 git -C "$DEPOT" branch -D essai/sparks-v9-repetition
echo "sorties : $J/*.txt ; journal de la minuterie : $J/racine/sparks-v5-minuterie.log"
```

## 5. Commande exacte du tir, pour la fille

À ne lancer qu'après :
1. la réponse de Lazar au nœud R-1527 (clé d'instance) : donnée, risque accepté et déclaré (R-1533) ;
2. une ligne de GO du tir dans `registres/go.md` (posée : GO-2026-11-05-02) : type « calcul », Lazar, au plus 5 USD, valide le jour du tir, périmètre
   qui nomme « SPARKS » et « tir », par exemple « SPARKS-EXP7-NUL tir réel » ;
3. **la poussée de la branche `prep/sparks-exp7-nul-v9`** (commit `4d07d2a6…`) vers le dépôt de travail, par la mère :
   l'instance clone le dépôt et extrait le commit de tir, enfant du commit du code.

Il faut aussi `vastai` 1.8.3 dans le chemin de la session qui tire (point 22), ainsi que `VAST_API_KEY` et
`CONTROLE_IA_GITHUB_TOKEN` dans son environnement, jamais affichés. Toutes les commandes ci-dessous se jouent depuis un
clone du dépôt de travail extrait sur `prep/sparks-exp7-nul-v9`.

```bash
cd <clone du dépôt de travail> && git fetch -q origin prep/sparks-exp7-nul-v9 && git checkout -q 4d07d2a6830ab09cb91250016284efb5cbe8a91c
export SPARKS_REGISTRE_GO="$PWD/registres/go.md"        # registre de main, avec la ligne du tir
# 1. recherche d'offres : le lanceur imprime la commande ; la jouer telle quelle (sortie brute effacée par `offres`)
bash scripts/lancer_sparks_exp7_nul_v9.sh recherche
#    → timeout -k 10 120 env -i … vastai search offers 'num_gpus=1 rentable=true verified=true' -o dph_total --raw > … ; bash scripts/lancer_sparks_exp7_nul_v9.sh offres …
# 2. tir au rang 1 (25 minutes d'échéance) : contrôle de la liste fermée, du GO et du devis, puis le protocole pas à pas
bash scripts/lancer_sparks_exp7_nul_v9.sh tir 4d07d2a6830ab09cb91250016284efb5cbe8a91c <GO_ID_DU_TIR> 25 1
```

Le mode tir imprime alors, avec les valeurs de l'offre et du GO, les étapes :
0. le commit de tir `essai/sparks-v9-tir-4d07d2a6830a` ;
1. la création, avec `GO_ID=<GO_ID_DU_TIR>`, `--disk 20`, l'étiquette, `GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN`, puis
   `apres-creation … $? <code> <GO> 25 1`. Sur « OFFRE RETIRÉE », il imprime la commande du rang suivant ;
2. les trois inventaires, le verdict `boucle $ID` et `journal-amorce` ;
3. la conduite selon le verdict ;
4. l'ordre « fin » ;
5. `start`, suivi de `apres-commande` ;
6. l'inventaire « absente » ;
7. le repli par `destruction $ID` ;
8. le devis.

Un exemple de cette sortie, joué hors réseau avec un registre de GO factice (GO-2026-11-05-09), est dans
`essais-et-banc-sparks-v9/exemple-sortie-tir.txt`.
