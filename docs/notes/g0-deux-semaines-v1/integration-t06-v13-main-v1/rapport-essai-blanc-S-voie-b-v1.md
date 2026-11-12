# Essai à blanc de la construction du commit de scellement S de T0.6, voie B (R-2062) — v1

- Auteur : le développeur de l'intégration (R-2054, R-2058, R-2062), sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy` ; n'écrit pas T0.6.
- Consigne : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-09-2200-v1/consigne-essai-blanc-construction-S-t06-voie-b-v1.md` (`7913056cd93e78d0806ee0dd02455013e8af91196619d7da0f4e9e8438d94306`, vérifiée, compagnon conforme).
- Lieu : `/tmp/claude-0/-home-user/1c58e8d5-f826-5476-bf99-3af565cb9c5a/scratchpad/essai-S/` (hors dépôt). Rien écrit dans `/home/user/controle-ia-travail` ni dans `/home/user/integ-t06` ; aucun `fetch` réseau, aucun `push`, aucune clé lue, aucun appel externe.
- Heures (`date -u`, 9 et 10 novembre 2026) : début 23:35:37 ; clone 23:36:40 ; S′ 23:41:58 ; fusion dans la copie de `main` 23:42:55 à 23:43:16 ; contrôles hors ligne 23:44:12 ; gardes du lanceur 23:46:32 ; suite ciblée v3 du 9 novembre 23:42:09 au 10 novembre 00:31:14.
- **Toutes les valeurs marquées « FACTICE » ci-dessous sont des valeurs d'essai à blanc ; rien n'est scellé pour de vrai, rien n'est poussé.**

**Verdict : voie B jouable.** S′ (descendant de `1609a4bf`, texte factice scellé, configuration copiée sous `prereg/`) passe tous les contrôles de `controles` jouables hors ligne (du 10 au 15 novembre ; refus le 16 par le calendrier, attendu), les gardes du lanceur v6 avant le manifeste (`exiger_code_cite` avec `1609a4bf`, `exiger_citations_t06`, `exiger_prereg_scelle`) et la suite ciblée v3 : **2 019 passés, 3 échoués, 0 sauté sur 2 022** ; les 3 échecs sont `test_corpus_arxiv` (`pypandoc` absent du `.venv` processeur, environnement), donc **2 019 / 2 019 hors `test_corpus_arxiv`**. Après fusion de S′ dans une copie de `main`, `commit_s` rend S′ et S′ est ancêtre de la tête. **Bloquants restants** : (1) Y1, Y2, Y9 de la r3 décrivent la voie A et deviennent faux (texte à réécrire, contre-lecture) ; (2) `docs/notes/bras-attaque/` est sur `main` et dans `1609a4bf` : tout clone et tout `verifier-arbre` le touchent (§ 0) ; (3) ce qui exige le réseau (fetch, jetons, branche de sortie, instance) reste à jouer.

## 0. Incident d'embargo à signaler (à lire d'abord)

- `docs/notes/bras-attaque/` (sous embargo) **est sur `main` depuis le commit `0ed05a32` (30 octobre 2026)**, donc aussi dans `1609a4bf`, dans `ff3e9a09` et dans tout clone de `main`. Je ne l'ai jamais ouvert, listé ni affiché.
- Le clone prescrit par la consigne (`git clone … /home/user/controle-ia-travail`) l'a **copié sur disque** à 23:36:40 UTC. Je l'ai vu par un test d'existence (nom seul), puis je l'ai retiré du disque dans tous les arbres de l'essai par extraction partielle (`git sparse-checkout set --no-cone '/*' '!/docs/notes/bras-attaque/'`, et la même exclusion ajoutée à la liste de l'amorce pour le clone réduit). Les objets restent dans le `.git` du clone temporaire. Pour compter ses entrées, j'ai lancé une fois `git ls-files -t` sur ce chemin en ne montrant que les lettres d'état (10 entrées, aucun nom affiché).
- **Tâche précédente (intégration, `/home/user/integ-t06`)** : les `verifier-arbre .` prescrits par la consigne d'intégration (22:25, 22:31, 23:31 UTC) ont **passé au hachage** tous les fichiers de `docs/`, ceux de `docs/notes/bras-attaque/` compris (« passage à un script » au sens de l'embargo). Aucun contenu n'a été affiché ; aucune ligne de sortie ne les nommait (ils étaient conformes). La routine R14 (`verifier-arbre .` sur l'arbre de la mère) fait de même. Je ne l'avais pas vu alors ; je le signale maintenant.
- Proposition : retirer ce dossier de `main` ou, au minimum, exclure `docs/notes/bras-attaque/` de `verifier-arbre` (une exclusion par nom dans `controle_ia.scellement`, R12 : module neuf) et des consignes qui prescrivent un clone complet. Le clone réduit de l'amorce v11 (`/docs/notes/`) le copie aussi sur l'instance.
- Dans cet essai, `verifier-arbre` n'a été lancé que sur un arbre où ce dossier était absent du disque (vérifié avant).

## 1. Clone et branches (commandes exactes)

```
mkdir -p essai-S && cd essai-S
git clone -q --no-local --single-branch --no-tags --branch main /home/user/controle-ia-travail depot      # main = 58f06cd8
cd depot && git remote remove origin
git fetch -q --no-tags /home/user/integ-t06 refs/heads/prep/integration-t06-v13-main-v1:refs/heads/integration-v1   # local, pour avoir 1609a4bf
git sparse-checkout set --no-cone '/*' '!/docs/notes/bras-attaque/'
git switch -q -c essai/S-voie-b 1609a4bf2c1572f72bb8542d81d963ac6a8481c4
```

- `--single-branch` : aucune autre branche de la mère n'est copiée (ni `essai/t06-explo-v3`, ni `donnees/lecture-b-7a-quarantaine-v1`, ni la branche de l'étiqueteur). La seule récupération (`fetch`) est locale, depuis ma branche d'intégration (lignée `ff3e9a09` + `1609a4bf` + mes trois commits), sans réseau.
- `1609a4bf` n'est pas un ancêtre de `main` (`58f06cd8`), et ma fusion `7c00367b` non plus (vérifié dans le dépôt de la mère, en lecture seule).

## 2. Texte factice et S′

### 2.1 Texte

- Source : `brouillons/T0.6-organismes-v0-v1-candidat12-r3.md` lu dans `main`, `c24e268ee9821d1f37ff612023a9f07735864614f57e3a9cf58517b05bc55331` (conforme).
- Couples Y1 à Y12 (`prereg/contre-lectures/T0.6-organismes-v0-v1-candidat12-r3-cl3-couples-v1.json`, `e3846ae5…`) appliqués par script, dans l'ordre, chaque « ancien » présent une fois exactement : texte obtenu **`7d7bfd2765266adcfd5ec8820ae6d85e4fb9e3c9ce6e08fdf53b4dab4bd8d122`**, égal à l'attendu.
- Dix marqueurs distincts (onze occurrences : `COMMIT_CODE_T06` deux fois), remplis ainsi :

| Marqueur | Valeur | Statut |
|---|---|---|
| `COMMIT_CODE_T06` (×2) | `1609a4bf2c1572f72bb8542d81d963ac6a8481c4` | plausible (consigne) |
| `EMPREINTES_CODE_T06` | `scripts/lancer_t06_v13.sh : 6940a337…` ; `scripts/amorce_instance_t06_v11.sh : 43d85659…` ; `scripts/tests-cibles-t06-v3.txt : e76d5e6b…` ; `scripts/tests-exclus-t06-v3.txt : ab70a1ed…` ; `src/controle_ia/t06/session_v12.py : 5b4ad5e9…` ; `lanceur_v6.py : e329493b…` ; `configuration_v6.py : 78996225…` ; `src/controle_ia/audit_fuite_r1_v4/bras_b_v4.py : 317a7ea5…` (empreintes complètes, relevées par `git show 1609a4bf:<chemin> \| sha256sum`) | réelles au commit `1609a4bf` |
| `EMPREINTE_AMORCE_T06` | `43d856596f4ff934ae6faa445faed0d00aaaa264b23b0bda344b6888dcd5e859` | réelle |
| `CHEMIN_CONFIG_T06` | `prereg/T0.6-organismes-config-7b-v1.json` (**nom proposé**, libre sur `main` ; sur le modèle de `prereg/P3-premier-test-config-v1.json`, `prereg/T0.5-pilote-config-v1.json`) | proposé |
| `EMPREINTE_CONFIG_T06` | `ca8003f90a9557ba42c8774e263407bdc2f4824b7f978f4c10f2e166ae97dd6d` : empreinte **canonique** (`controle_ia.t06.lanceur.empreinte_config`, JSON trié et compact), à ne pas confondre avec le sha256 du fichier, `b7a5c1ba…` | réelle pour cette copie |
| `MOT_LAZAR_GO_7B` | `R-0000 (FACTICE, essai à blanc de la voie B)` | FACTICE |
| `DECISION_LAZAR_ECART_DT4_R2041` | `FACTICE (essai à blanc de la voie B ; aucune décision n'est citée), R-0000` | FACTICE |
| `EMPREINTE_RELU_CL3_T06` | `000…0001` (64 caractères) | FACTICE |
| `CHEMIN_RAPPORT_CL3_T06` | `FACTICE/rapport-contre-lecture-3.md` | FACTICE |
| `EMPREINTE_RAPPORT_CL3_T06` | `000…0002` (64 caractères) | FACTICE |

- Texte factice écrit sous `prereg/T0.6-organismes-v0-v1.md` : `5e6c30111899b66d4513292c3b91d930bbdbf8fc5236f8615e48c1e99a05241e` ; `controle_ia.prereg.problemes` : **liste vide** (sections présentes, aucune marque « À REMPLIR », contre-lecture 3 avec deux empreintes distinctes, aucun marqueur restant).
- Remarque de fond pour la r4 (non bloquante pour la mécanique, bloquante pour le texte) : **les couples Y1, Y2 et Y9 décrivent la voie A**. Y1 dit « `1609a4bf` lui-même ne convient pas tant que l'arbre de `main` en diffère […] la valeur écrite ici est le commit d'intégration de la chaîne dans `main` » ; Y2 dit « L'arbre du commit de scellement n'est pas celui de `1609a4bf` […] relevé sur l'arbre du commit d'intégration » ; Y9 dit « commit d'intégration de 7b […] portée dans `main` ». Avec la voie B (commit cité `1609a4bf`, S descendant de `1609a4bf`), ces phrases deviennent fausses : la r4 doit les réécrire (couples neufs, contre-lecture).

### 2.2 Commits de l'essai (dans le clone seulement)

| Commit | Contenu | Arbre gelé |
|---|---|---|
| `1609a4bf` | point de départ | — |
| P = `5561a7c0bcf84d084a1e97b2ecb94d4253d2440b` | 71 compagnons `.sha256` des notes de `docs/notes/g0-deux-semaines-v1/` apportées sans sceau (copie exacte de mon commit `00cc8fce`) ; 71/71 conformes | = `1609a4bf` |
| **S′ = `6d0a4a49269ced3c3727250f5885a6cdbe289025`** | `prereg/T0.6-organismes-v0-v1.md` + compagnon (`5e6c3011…`) ; `prereg/T0.6-organismes-config-7b-v1.json` (copie octet pour octet de `docs/notes/g0-deux-semaines-v1/config-t06-reel-v1-brouillon5.json`, `b7a5c1baeee13f7589b296fb166180515422ebc8c7eff703994bb5b6835ae527`) + compagnon ; scellés par `PYTHONPATH=src python -m controle_ia.scellement sceller` | = `1609a4bf` |

P est un ajout de ma part (hors consigne) : sans lui, la fusion dans `main` y ferait entrer 71 fichiers sans sceau (`verifier-arbre` en échec, § 5) ; il est sous `docs/`, hors périmètre gelé, et ne change ni `commit_s` ni `exiger_code_cite`.

### 2.3 Pièces citées : présentes à `1609a4bf` ou ajoutées par S

| Pièce citée par le texte | À `1609a4bf` | Sceau à `1609a4bf` | Sur `main` | Dans S′ |
|---|---|---|---|---|
| configuration (`CHEMIN_CONFIG_T06`) | absente sous `prereg/` ; la source `docs/…/config-t06-reel-v1-brouillon5.json` y est **sans sceau** ; absente de `main` | — | non | **ajoutée** (copie + sceau) |
| tâches d'évaluation `donnees/20261007-082440-t05-extraction/taches-evaluation.json` (`76cdeace…`) | oui | oui, conforme | oui, identique | héritée |
| tâches de distillation `…/taches-entrainement.json` (`8d20a698…`) | oui | oui, conforme | oui, identique | héritée |
| consignes de P3 `prereg/P3-consignes-v1.md` (`a68468fe…`) | oui | oui, conforme | oui, identique | héritée |
| texte `prereg/T0.6-organismes-v0-v1.md` | absent (et absent de `main`) | — | non | **ajouté** (texte + sceau) |
| amorce v11 (`43d85659…`) | oui | (non exigé) | non | héritée |

La configuration (`b7a5c1ba…`) porte `go_id` GO-2026-11-02-28, `plafond_usd` 200, `fraction_equivalence` 0,05, `calendrier.dernier_jour_creation` 2026-11-15, `fin_go_utc` 2026-11-17T00:00:00Z, et ne cite pas d'autre fichier que les tâches et les consignes ci-dessus (`textes_p3`, `sondes_figees_p3`, `temoin_lexical` nuls).

## 3. Contrôles du lanceur v13, hors ligne

### 3.1 Méthode

Script `essai-S/scripts/controles_hors_ligne.sh`, construit **mécaniquement** à partir de `scripts/lancer_t06_v13.sh` (l. 76 à 117 : variables et fonctions, dont `commit_s` l. 112 ; l. 119 à 146 : `controles`), avec trois lignes changées seulement (`diff` vérifié) :

- l. 126 `git fetch -q origin main` → retirée (réseau interdit) ;
- l. 127 `merge-base --is-ancestor "$S" origin/main` → `… "$S" "$ORIGINE_SIMULEE"`, où `ORIGINE_SIMULEE` est la tête de la copie de `main` après fusion de S′ (§ 4) ;
- l. 144 (présence de `HF_TOKEN` et du jeton GitHub) → remplacée par une affectation neutre : **aucune variable lue**, contrôle non joué.

Commande : `T06_DEPOT=…/essai-S/main-copie ORIGINE_SIMULEE=4d92a2f0151107eada8f541cd887eb2348e46ff0 GO_ID= bash scripts/controles_hors_ligne.sh controles <dossier neuf> 2026-11-JJ`. `REG` = `registres/go.md` de la copie de `main` fusionnée (= celui de `main`, résolution `--ours`) ; `GO_ID` de la course (GO-2026-11-02-28, écrit en dur l. 83) ; interpréteurs : `python3` du système pour `session_v2 go` et `calendrier`, comme le lanceur.

### 3.2 Résultats

| Contrôle (ligne du lanceur) | Résultat |
|---|---|
| l. 123 `session_v2 go` : ligne GO-2026-11-02-28 lue dans `registres/go.md` de `main` | « GO-2026-11-02-28 conforme (plafond 200 USD, 2026-11-02 → 2026-11-16) », chaque jour du 10 au 16 |
| l. 124 place disque ≥ 3 Go | conforme |
| l. 125 `commit_s` (`git log --diff-filter=A -1 --format=%H -- prereg/T0.6-organismes-v0-v1.md.sha256`, depuis la tête fusionnée) | **rend S′ `6d0a4a49…`** |
| l. 127 S ancêtre d'`origin/main` (simulé) | **conforme** ; artefact : avec `ORIGINE_SIMULEE` = `main` avant fusion (`58f06cd8`), **refus** « commit de scellement 6d0a4a49… absent de origin/main (simulé) », code 2 |
| l. 128 texte présent dans S | conforme |
| l. 129-133 huit citations, une ligne chacune | **1 occurrence chacune** (forme au § 3.3) |
| l. 134-139 fichiers cités et sceaux présents dans S, sceau conforme | conforme pour les quatre ; `config.json` du dossier = configuration de S′ (octet pour octet) |
| l. 140 `session_v2 calendrier` | **conforme du 10 au 15 novembre** (« fin_go_utc_s=1794873600 dernier_jour_creation=2026-11-15 echeance_go=2026-11-16 ») ; **refus le 16** (« dernier jour de création (2026-11-15) dépassé le 2026-11-16 : nœud de Lazar, aucune création ») |
| l. 141-143 amorce v11 de S, empreinte citée sous la forme `` `scripts/amorce_instance_t06_v11.sh` (`43d85659…`) `` | conforme |
| l. 144 jetons | **non joué** (hors ligne, aucune variable lue) |
| l. 145-146 | « CONTRÔLES CONFORMES : S=6d0a4a49269ced3c3727250f5885a6cdbe289025 ; amorce v11 43d85659… ; GO GO-2026-11-02-28 ; … », code 0, pour chaque jour du 10 au 15 |

La consigne cite « la sous-commande `calendrier` de la session v12 » : le lanceur v13 appelle `calendrier` (et `go`) dans **`session_v2`** (`$SESSION`, l. 123 et 140) ; `session_v12` n'a pas de sous-commande `calendrier`. J'ai joué ce que joue le lanceur.

### 3.3 Forme exacte des huit lignes citées (texte de S′, une occurrence chacune)

```
l. 234  Entropie : `31538212097275005629337336542801867913`
l. 243  Configuration de T0.6 (empreinte canonique) : `ca8003f90a9557ba42c8774e263407bdc2f4824b7f978f4c10f2e166ae97dd6d`
l. 244  Tâches d'évaluation de T0.6 : `76cdeace861d2fff45ca732c55c2d97611dcd47edc7c27d62bdad4c37755e67e`
l. 238  Tests attendus : `2022`
l. 245  Chemin de la configuration de T0.6 : `prereg/T0.6-organismes-config-7b-v1.json`
l. 246  Chemin des tâches d'évaluation de T0.6 : `donnees/20261007-082440-t05-extraction/taches-evaluation.json`
l. 247  Chemin des tâches de distillation de T0.6 : `donnees/20261007-082440-t05-extraction/taches-entrainement.json`
l. 248  Chemin des consignes de P3 : `prereg/P3-consignes-v1.md`
```

Forme de l'amorce (l. 143, sur le texte aplati) : `` `scripts/amorce_instance_t06_v11.sh` (`43d856596f4ff934ae6faa445faed0d00aaaa264b23b0bda344b6888dcd5e859` `` présente (ligne « Amorce »).

### 3.4 Gardes du lanceur v6 avant le manifeste (en plus de la consigne : Y9 les demande)

Clone réduit fait comme celui de l'amorce v11 (`git clone --no-local --no-checkout --single-branch` de la branche d'essai ; `sparse-checkout --no-cone` avec la liste `CHEMINS_CLONAGE` de l'amorce, **plus** `!/docs/notes/bras-attaque/` ; `checkout` de S′). Script `essai-S/scripts/gardes_avant_manifeste.py` (rien n'est écrit : il s'arrête avant `creer_manifeste`), configuration = `config.json` produite par `controles` :

| Garde (`lanceur_v6.executer`, l. 164-180, puis `prereg`) | Résultat |
|---|---|
| `exiger_config_t06_v6` (registre `registres/go.md` du commit cloné) | passe |
| mode réel avec préenregistrement, pas une épreuve | passe (`reel`, `est_epreuve` faux) |
| `charger_taches_t06` | passe (`76cdeace…`, `8d20a698…`) |
| `charger_consignes` | passe (`a68468fe…`) |
| `charger_invite("H1-classification")` | passe |
| `exiger_code_importe_sous` | passe |
| `exiger_code_cite` (commit cité lu dans le texte : `1609a4bf`, HEAD = S′) | **passe** |
| `exiger_citations_t06` | **passe**, rend l'entropie `31538212097275005629337336542801867913` |
| `exiger_prereg_scelle` | **passe** (`5e6c3011…`) |

Artefacts (R5) : configuration modifiée (`plafond_usd` 199) → **refus** de `exiger_config_t06_v6` (« plafond 199 : exactement 200.0 USD ») et de `exiger_citations_t06` (« configuration 9ee70bb0… ≠ configuration citée ca8003f9… ») ; `exiger_code_cite` avec HEAD = tête de `main` fusionnée → **refus** (« arbre gelé … modifié depuis le commit cité 1609a4bf2c15 ») : l'instance doit cloner **S**, ce que fait l'amorce (`COMMIT=$S`, `checkout -q "$COMMIT"`, l. 291), pas la tête de `main`.

## 4. Fusion de S′ dans une copie de `main`

- Copie : second arbre du clone, branche `main-copie` partie de `58f06cd86b34d84f89ef28819cee4d246d67d6bb` (au-delà de `d82f89f5`, qui en est un ancêtre), même extraction partielle.
- `git merge --no-ff --no-commit essai/S-voie-b` : **trois conflits, les mêmes qu'à l'intégration** ; résolus selon R-2055 :

| Lieu | Résolution |
|---|---|
| `docs/notes/g0-deux-semaines-v1/e3-ter-v1/config-t06-course-explo-v1.json` et compagnon (ajoutés des deux côtés : `main` `1911a9e9…`, S′ `59e896b5…`) | `--ours` (`main`) ; version jouée ajoutée sous `config-t06-course-explo-v1-joue-be729130.json`, octet pour octet depuis `1609a4bf`, sceau `59e896b5a348a3d545d375cea148102e352d1c813f0939e1d99f3f1827e774b4` (ce nom n'est pas encore sur `main`) |
| `registres/go.md` | `--ours` ; lignes de S′ absentes de `main` : **0** |

- Garde des secrets avant le commit de fusion d'essai : 0. Noms sous embargo dans l'index : 0.
- Commit de fusion d'essai `M = 4d92a2f0151107eada8f541cd887eb2348e46ff0` (parents `58f06cd8` et S′).
- Depuis M : `git log --diff-filter=A -1 --format=%H -- prereg/T0.6-organismes-v0-v1.md.sha256` → **`6d0a4a49269ced3c3727250f5885a6cdbe289025` = S′** ; `git merge-base --is-ancestor S′ M` → vrai.
- `exiger_code_cite`, commit cité `1609a4bf`, HEAD = S′ : **passe** ; HEAD = M : refus (attendu, voir § 3.4).
- `verifier-arbre .` sur M (dossier sous embargo absent du disque, vérifié avant) : **1 problème**, la seule orpheline attendue (`consigne-argon-question-mere-v3.txt.sha256`) — grâce à P ; sans P, 71 compagnons manqueraient.

## 5. Suite ciblée v3 sur l'arbre de S′

- **Commande**, comme l'amorce v11 (l. 474 à 494) : depuis la racine du clone à S′ (`essai-S/depot`, HEAD `6d0a4a49…`), `PYTHONPATH=src python -m pytest -q -p no:cacheprovider --color=no <les 84 fichiers de scripts/tests-cibles-t06-v3.txt>`, `python` = `/home/user/controle-ia-travail/.venv/bin/python` (son `bin` en tête de `PATH`). Liste vérifiée avant : empreinte `e76d5e6b…` égale à celle de l'amorce.
- **Arbre** : celui de S′ = `1609a4bf` + 71 sceaux sous `docs/` + texte et configuration sous `prereg/` ; extraction partielle sans `docs/notes/bras-attaque/` (hors de tout ce que lisent les essais, vérifié dans le code des essais : leurs parcours `rglob` portent sur `src/`, sur des dossiers temporaires, ou sur des fichiers nommés de `docs/`).
- **Environnement** : `.venv` de la mère, `requirements-cpu.txt` (sans `requirements-donnees.txt`, donc sans `pypandoc_binary`), processeur seul.
- Début 2026-11-09 23:42:09 UTC, fin 2026-11-10 00:31:14 UTC. **Dernière ligne : « 3 failed, 2019 passed in 2939.87s (0:48:59) »** ; aucun fichier suivi par git n'a changé.

| Passés | Échoués | Sautés | Total | Attendu |
|---|---|---|---|---|
| **2 019** | **3** | **0** | 2 022 | 2 022 passés |

- Les 3 échecs : `tests/test_corpus_arxiv.py::test_traiter_papier_garde`, `::test_traiter_papier_trop_court_exclu`, `::test_constituer_s_arrete_au_besoin_et_numerote`, tous `ModuleNotFoundError: No module named 'pypandoc'` : **environnement processeur** (déjà consigné à R-2042), pas le code ; sous `requirements-gpu.txt` (qui inclut `requirements-donnees.txt`), ils passent, comme sur l'instance de 7a au même arbre gelé. **Hors `test_corpus_arxiv` : 2 019 / 2 019.**
- Par rapport à l'intégration (voie A, 2 017 / 5) : `test_cibles_invisibles_v2` et `test_t06_v13_liste` passent ici, parce que l'arbre de S′ ne contient ni `premier_test_ia/run_v2.py` ni les 27 essais venus de `main`.
- **Effet de la présence du texte** : aucun essai n'a changé de résultat parce que `prereg/T0.6-organismes-v0-v1.md` ou sa configuration existent. Les essais qui citent ce chemin (`tests/test_t06_v12_amorce.py`) écrivent leur propre texte dans un dépôt temporaire ; ceux qui lisent `registres/` (5 fichiers de la liste) passent, avec le `registres/go.md` de `1609a4bf`.
- Pour une valeur « Tests attendus » opposable : rejouer la liste sous `requirements-gpu.txt` (ou avec `pypandoc_binary==1.17` installé) sur l'arbre de S réel ; attendu « 2022 passed ».

## 6. Ce que S (et la r4) doivent contenir

1. **S a pour ancêtre `1609a4bf` et ne change rien dans le périmètre gelé** (`CHEMINS_GELES` : tout hors `prereg`, `brouillons`, `registres`, `docs`, `diag`, `runs`, `donnees`, `livrables`, `papiers`, `traces`, `CLAUDE.md`) : sinon `exiger_code_cite` avec `1609a4bf` refuse. Ni `src/`, ni `tests/`, ni `scripts/`, ni `.claude/`, ni fichier à la racine.
2. **Dans S** (S = le commit qui ajoute `prereg/T0.6-organismes-v0-v1.md.sha256`, c'est ce que rend `commit_s`) : `prereg/T0.6-organismes-v0-v1.md` (la r4) et son compagnon ; `prereg/T0.6-organismes-config-7b-v1.json` (nom proposé ; copie de `b7a5c1ba…`) et son compagnon.
3. **Déjà à `1609a4bf`, scellées, à ne pas toucher** : `donnees/20261007-082440-t05-extraction/taches-evaluation.json` (`76cdeace…`), `…/taches-entrainement.json` (`8d20a698…`), `prereg/P3-consignes-v1.md` (`a68468fe…`), avec leurs compagnons ; l'amorce v11 (`43d85659…`) et le lanceur v13 (`6940a337…`).
4. **Recommandé, avant S sur la même lignée** (ou dans le commit de fusion) : les 71 sceaux des notes de `docs/notes/g0-deux-semaines-v1/` (commit P de l'essai, copie de `00cc8fce`).
5. **Dans la r4** : les huit lignes citées sous la forme du § 3.3 (une occurrence chacune) ; la ligne « Amorce » sous la forme `` `scripts/amorce_instance_t06_v11.sh` (`<sha256>`) `` ; « Commit du code d'analyse : `1609a4bf2c1572f72bb8542d81d963ac6a8481c4` » à ses deux occurrences ; « Tests attendus : `2022` » si la suite sous `requirements-gpu.txt` le confirme (§ 5) ; « Configuration de T0.6 (empreinte canonique) » = l'empreinte **canonique** de la copie sous `prereg/` (`ca8003f9…` pour la copie de `b7a5c1ba…`) ; les quatre marqueurs de Lazar et de la contre-lecture 3 remplis pour de vrai ; **Y1, Y2 et Y9 réécrits pour la voie B** (§ 2.1).
6. **Puis** : fusion de S dans `main` avec les résolutions de R-2055 (trois conflits), poussée (décision de la mère), `controles` joué en ligne (le `fetch` et les jetons), avant le 15 novembre (refus le 16).

## 7. Ce qui ne peut pas être joué hors ligne

- l. 126 `git fetch origin main` et la vraie relation d'ancêtre avec `origin/main` (simulée ici par une fusion locale) ;
- l. 144 présence des jetons (`HF_TOKEN`, jeton GitHub) : aucune variable lue ;
- l'amorce sur une instance : clone depuis `DEPOT_URL` (S doit être atteignable depuis le dépôt distant, donc poussé via `main`), branche de sortie `T06_BRANCHE` absente du dépôt distant (défaut `calcul/t06-reel-v4` ; non vérifiable sans réseau), suite v3 sous l'image et `requirements-gpu.txt` (dont `pypandoc_binary`), carte, mémoire, run ;
- les marqueurs de Lazar et de la contre-lecture 3 (valeurs factices ici) ;
- la vérification de T0.7 scellé et du rapport d'audit DT-4 scellé (exigés par le GO et R-2048, hors de la chaîne).

## 8. Fichiers de l'essai (hors dépôt)

- `essai-S/depot/` : clone, branches `main` (58f06cd8), `integration-v1`, `essai/S-voie-b` (P, S′), `main-copie` (M, second arbre `essai-S/main-copie/`) ;
- `essai-S/clone-amorce/` : clone réduit à S′ ;
- `essai-S/texte/` : texte après couples (`7d7bfd27…`), empreintes de `1609a4bf` ;
- `essai-S/scripts/` : `appliquer_couples.py`, `remplir_marqueurs.py`, `controles_hors_ligne.sh`, `essai_code_cite_prereg.py`, `gardes_avant_manifeste.py` ;
- `essai-S/controles/` : dossiers de `controles` par jour (`lancement.txt`, `prereg-S.md`, `config.json`, `amorce.sh`), artefacts ;
- `essai-S/essais-v3/` : sortie brute de la suite (`tests.txt`, `tests.err`, `code.txt`, heures).
