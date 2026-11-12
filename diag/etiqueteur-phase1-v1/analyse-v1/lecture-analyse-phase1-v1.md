# Lecture de l'analyse de la phase 1 de l'épreuve de l'étiqueteur — v1

- **Lecteur neuf** : sous-agent Claude Fable 5.1 (`claude-fable-5-1`), 8 novembre 2026, de 14:49 à 14:52 (temps universel, `date -u`). Il n'a écrit ni le préenregistrement, ni les scripts, ni l'ordre d'exécution, et n'a pas exécuté la lecture. Il n'a ouvert ni les fichiers de réponses, ni la clé, ni les items (empreintes, comptes et champs nommés seulement). Il a lu en entier le fichier de résultat et la console de l'analyse.
- **Rôle** : rapporter les issues telles que le fichier de résultat les écrit, et ce que le texte scellé dit lire pour chacune. **Aucune interprétation au-delà du texte scellé ; le verdict de phase 1 est prononcé par un autre sous-agent neuf** (R13 par analogie, ordre d'exécution, section 5).
- **Fait foi** : `prereg/preenregistrement-epreuve-etiqueteur-v1.md`, empreinte `f73455b8b672c2b1a896b54badb6d8262fe9b422d4aa346f44c6efc76eef40fa` (vérifiée sur le disque le 8 novembre à 14:50), sections « Prédiction chiffrée et signe attendu », « Seuil — Phase 1 », « Critères de lecture gelés — Phase 1 », « Liste d'arrêt » ; ordre d'exécution `docs/procedures/ordre-execution-phase1-epreuve-etiqueteur-v1.md`, section 5 (l. 438-451).

## 1. Contrôles avant l'analyse (tous conformes)

| contrôle | constat |
|---|---|
| items `$GEN/items-epreuve-v2.jsonl` | 396 lignes ; empreinte `8efc13d3546201843708126e2ee7c8fa7f1a0069b8d3aa3e3ea054465c0fb14c`, égale au champ `sorties` du manifeste de génération |
| clé `$GEN/cle-epreuve-v2.jsonl` | 396 lignes ; empreinte `191e50011bc6edb89d62be403699b0f45dca5a5652c7d72bc59fa3c6ffe5901c`, égale au manifeste de génération |
| lecture principale | dossier `$PRINC` absent sur cette machine ; matérialisé par `git show` depuis la branche `origin/donnees/etiqueteur-phase1-lecture-principale-v1` (commit `16aef7a0b318603a5e4b949087d797583e0547e4`), chemin `diag/etiqueteur-phase1-v1/lecture-principale-fille-cles-2-v1/lecture-principale/` ; `sha256sum -c` des trois compagnons : OK |
| `reponses-phase1-A-v4.jsonl` | 456 lignes ; `5d0e8296d1b9410d7771e5839188430273f0813fd4701c52699732bba3b99e2e`, égale au champ `sorties` du manifeste de lecture |
| `reponses-phase1-B-v4.jsonl` | 456 lignes ; `b03fccb51b37d088080bda4fefc5cf860aef85c95ebe03595dc05a256454237a`, égale au champ `sorties` du manifeste de lecture ; différente de A |
| `manifeste-lecture-phase1-v4.json` | `47a13f944e52aa4310038d8d679d161f5c31f108671956a87297454771ae9e2d` |
| champ `lecteur` de chaque ligne | A : 456 lignes égales à « A », 0 d'un autre lecteur ; B : 456 égales à « B », 0 d'un autre lecteur ; champ `lecture` : 396 « principale » et 60 « relecture » pour chacun (programme Python `-I -B`, comptes seuls) |
| code au commit scellé | arbre détaché reconstitué hors ligne (`git worktree add --detach`) au commit `64e67cbd4a870a4bc8f861e7a4632c300283a3c2` : « commit du code conforme », « arbre propre » ; `analyser_phase1_v3.py` à l'empreinte `7c0555b4647a3e1e2c314b4e934345522cb72995712a789e044e81e77373fb9f` (OK) |

## 2. Lancement de l'analyse

- Commande de l'ordre (l. 446-448) lancée telle quelle (mêmes options, mêmes chemins, `env -i PATH=/usr/bin:/bin LANG=C.UTF-8`, `-I -B`, `--tirages 10000`, `--entropie 17812956677980471985`), de 14:50:23 à 14:50:30 ; **code de fin 0**.
- Écart de forme, à consigner : la commande a été précédée de `timeout 1800 nice -n 10` (règle de la session mère pour toute commande longue) ; aucune option ni chemin du script changé.
- Sorties, copiées sans modification et scellées sous `diag/etiqueteur-phase1-v1/analyse-v1/` (dossier neuf) :
  - `resultat-phase1-v1.json` : `e228baa6722f2459335ab7dac09914314c4941f032f8c2768b3e0ddfdae5f3d3` (identique à `$RACINE/analyse/resultat-phase1-v1.json`) ;
  - `console-analyse-v1.log` : `2a401eacc37c57701ddb83116b05db7dc9d197984e8c2f8e9253ea906410f458` (identique à `$CONSOLES/console-analyse-v1.log`) ; 170 octets : l'issue et les réserves, rien d'autre.
- Le fichier de résultat porte : `version` « v3 », `empreinte_script` `7c0555b4…`, `entropie` 17812956677980471985, `tirages` 10000, et dans `entrees` les quatre empreintes ci-dessus (items, clé, réponses A, réponses B) : égales à celles contrôlées.

## 3. Ce que le fichier de résultat écrit

### 3.1 Issue de l'étiqueteur (conjonction A et B)

```
issue : « non tranché » ; types : [] ; portee_10_pour_cent : []
reserves : [« lecture instable (plus de 3 relectures des jumeaux sur 60 à fausse alarme) »]
audit_symetrie : false
```

Aucun « arrêt » n'est écrit comme issue : le fichier ne porte ni clé `arret`, ni mention d'illisibles au-delà de 2 %, ni fichier incomplet. L'issue est une issue de mesure.

### 3.2 Critères gelés, étiqueteur

| critère | grandeur écrite | seuil gelé (texte scellé, « Seuil — Phase 1 ») | statut mécanique écrit par le script |
|---|---|---|---|
| C1(affaiblir) | k = 47 sur 48, rappel 0,9792 ; Clopper et Pearson [0,8893 ; 0,9995] ; rééchantillonnage [0,9333 ; 1,0] | réussi si rappel ≥ 0,8 et plus basse borne basse ≥ 0,7 (au moins 41 sur 48) ; échec décisif si borne haute < 0,8 (au plus 32) | `reussi: true`, `echec_decisif: false` |
| C1(changer) | k = 48 sur 48, rappel 1,0 ; Clopper et Pearson [0,9260 ; 1,0] ; rééchantillonnage [1,0 ; 1,0] | idem | `reussi: true`, `echec_decisif: false` |
| C1(retirer) | k = 47 sur 48, rappel 0,9792 ; Clopper et Pearson [0,8893 ; 0,9995] ; rééchantillonnage [0,9333 ; 1,0] | idem | `reussi: true`, `echec_decisif: false` |
| C1-faible(affaiblir) | k = 23 sur 24, rappel 0,9583 ; Clopper et Pearson [0,7888 ; 0,9989] | au moins 22 sur 24 ; échec décisif au plus 14 | `reussi: true`, `echec_decisif: false` |
| C1-faible(changer) | k = 24 sur 24, rappel 1,0 ; [0,8575 ; 1,0] | idem | `reussi: true`, `echec_decisif: false` |
| C1-faible(retirer) | k = 23 sur 24, rappel 0,9583 ; [0,7888 ; 0,9989] | idem | `reussi: true`, `echec_decisif: false` |
| **C2** (fausses alarmes des 120 placebos) | **k = 11 sur 120, taux 0,0917** ; Clopper et Pearson [0,0467 ; 0,1581] ; rééchantillonnage [0,0417 ; 0,1583] | réussi si taux ≤ 0,05 et plus haute borne haute ≤ 0,10 (au plus 5 sur 120) ; échec décisif si borne basse de Clopper et Pearson > 0,05 (au moins 12 sur 120) | **`reussi: false`, `echec_decisif: false`** (11 est entre 5 et 12 : ni réussi ni échec décisif) |
| C3 (kappa entre A et B, 336 items) | kappa 0,7349 ; rééchantillonnage [0,6243 ; 0,8280] | réussi si kappa ≥ 0,6 et borne basse ≥ 0,4 ; échec décisif si borne haute < 0,6 | `reussi: true`, `echec_decisif: false` |
| garde de relecture (réserve) | k = 5 sur 60, seuil 3 | au plus 3 sur 60 ; au-delà, réserve « lecture instable » | `depassee: true` → réserve écrite |

Règle d'issue du texte scellé (« Seuil — Phase 1 », règles de calcul) : « validé contre la construction » si T (types où C1 est réussi) non vide **et** C2 **et** C3 réussis ; « non validé » si C2 ou C3 échoue de façon décisive, ou C1 pour les trois types ; sinon « non tranché ». Ici T = {affaiblir, changer, retirer}, C3 réussi, C2 ni réussi ni en échec décisif : le script écrit « non tranché », conformément à la règle.

### 3.3 Issues de A seul et de B seul (rapportées, sans critère)

| lecteur | C1 (fortes) affaiblir / changer / retirer | C1-faible affaiblir / changer / retirer | C2 (placebos) | C3 | garde de relecture | `issue_seul` |
|---|---|---|---|---|---|---|
| A (`gemini-4-argon`) | 47/48 ; 48/48 ; 47/48, tous `reussi` | 23/24 ; 24/24 ; 23/24, tous `reussi` | **12 sur 120, taux 0,10**, Clopper et Pearson [0,0527 ; 0,1682], rééchantillonnage [0,0417 ; 0,1667] : `echec_decisif: true` | — | 4 sur 60, `depassee: true` | « étiqueteur non validé » |
| B (`kimi-k3.1-pro`) | 48/48 ; 48/48 ; 48/48, tous `reussi` | 24/24 ; 24/24 ; 23/24, tous `reussi` | **27 sur 120, taux 0,225**, Clopper et Pearson [0,1538 ; 0,3102], rééchantillonnage [0,15 ; 0,3083] : `echec_decisif: true` | — | 13 sur 60, `depassee: true` | « étiqueteur non validé » |

Fausses alarmes réunies (180 négatifs, rapportées sans critère) : A 16 sur 180 ; B 40 sur 180 ; étiqueteur 16 sur 180 (0,0889).

### 3.4 Compteurs par lecteur (statuts)

| lecteur | lectures principales | illisibles en lecture principale | citations | citations invalides |
|---|---|---|---|---|
| A | 396 | **7** (1,77 % des 396 : sous la règle des 2 % qui interdirait tout verdict ; sous les 8 de la table d'arrêts de l'ordre) | 674 | 0 |
| B | 396 | 0 | 830 | 9 (1,08 % : sous les 10 % qui imposent une réserve) |

### 3.5 Mesures rapportées

- **Écart placebos / relectures** : fausses alarmes des placebos 0,0917, des relectures 0,0833, écart 0,0083.
- **Pente de dose** (régression sur le logarithme de la dose réalisée, intervalle par rééchantillonnage) : affaiblir 0,0383, intervalle [−0,4545 ; 0,5489] ; changer : `null` (rappel 1,0 à toutes les doses, pente non estimable) ; retirer 1,7886, intervalle [1,3206 ; 2,3820].
- **Rappel par pas** : gabarit montré 310 sur 317 (0,9779) ; gabarit tenu 309 sur 327 (0,9450) ; écart 0,033. Mode champs 315 sur 328 (0,9604) ; remplacement 307 sur 321 (0,9564) ; suffixe 312 sur 323 (0,9659).
- **Rappel par case** (étiqueteur, 24 items chacune) : affaiblir 23, 24, 23 à 10 %, 30 %, 100 % ; changer 24, 24, 24 ; retirer 23, 23, 24.
- **Absent du fichier** : la fausse alarme absolue des jumeaux (P-5 ; « Métrique » dit « rapportée ») et la précision (« Métrique », rapportée) n'apparaissent sous aucune clé du fichier de résultat ; le lecteur neuf le constate sans le combler.

## 4. Prédictions préenregistrées : issue mécanique, une ligne chacune

Le texte scellé écrit : « aucune [confiance] ne sert de critère ; seuls les seuils décident ». Les lignes ci-dessous comparent le chiffre écrit à la colonne « réfutée si » de la table du texte scellé.

| repère | prédiction (texte scellé) | chiffre écrit par le script | « réfutée si » | issue mécanique |
|---|---|---|---|---|
| P-1 | pente positive par type | affaiblir : pente 0,038, borne haute 0,549 > 0 ; changer : pente `null` ; retirer : pente 1,789, intervalle entièrement > 0 | borne haute de la pente ≤ 0 | affaiblir : non réfutée (intervalle couvre 0) ; changer : non calculable (rappel 1,0 partout) ; retirer : non réfutée |
| P-2 | rappel aux doses fortes ≥ 0,85 pour les trois types | affaiblir 0,979 ; changer 1,0 ; retirer 0,979 | rappel < 0,85 | non réfutée pour les trois types |
| P-3 | rappel à 10 % : affaiblir et changer entre 0,5 et 0,9 ; retirer entre 0,4 et 0,8 | affaiblir 0,958 ; changer 1,0 ; retirer 0,958 | hors de ces bornes | **réfutée pour les trois types** (au-dessus des bornes hautes) |
| P-4 | fausses alarmes réunies (180) entre 0,02 et 0,10 ; relecture des jumeaux ≤ 0,03 | réunies 16 sur 180 = 0,0889 ; relectures 5 sur 60 = 0,0833 | hors de ces bornes | réunies : non réfutée ; **relectures : réfutée** (0,0833 > 0,03) |
| P-5 | fausses alarmes absolues des jumeaux entre 0,3 et 0,7 | **non écrit dans le fichier de résultat** | hors de ces bornes | non lisible |
| P-6 | kappa entre A et B ≥ 0,6 | 0,7349, intervalle [0,6243 ; 0,8280] | < 0,6 | non réfutée |
| P-7 | retirée par la contre-lecture 1 | — | — | — |
| P-8 | écart de rappel par pas « tenus » contre « montrés » ≤ 0,10 | 0,9779 − 0,9450 = 0,033 | > 0,10 | non réfutée (et sous le 0,15 de la réserve « catégories données en exemple ») |
| P-9 | issue « validé contre la construction » pour au moins affaiblir et changer | issue « non tranché », types [] | autre issue | **réfutée** |
| P-10, P-11 | phase 2 | — | — | sans objet (la phase 2 ne part pas sur « non tranché ») |

## 5. Ce que le texte scellé dit lire pour chaque issue (« Critères de lecture gelés — Phase 1 »)

| constat écrit | ligne du texte scellé | verdict et conséquence écrits par le texte scellé (à prononcer par le sous-agent du verdict, non par ce lecteur) |
|---|---|---|
| issue « non tranché » (C1 réussi pour les trois types et C3 réussi, mais C2 ni réussi ni en échec décisif : 11 sur 120) | « tout autre cas » | **non tranché** ; « même proposition au directeur [que pour "non validé" : ne pas retenir cet étiqueteur comme vérité du dommage ; la porte garde ce que N-060 v3 fixe] ; la phase 2 ne part pas ; une nouvelle épreuve est possible, jamais par relecture de ces items avec une consigne changée » |
| garde de relecture dépassée : 5 sur 60 (> 3) | « garde de relecture dépassée » | réserve écrite « lecture instable » (le script l'a écrite) |
| écart tenus/montrés 0,033 (≤ 0,15) | « écart > 0,15 » | pas de réserve « catégories données en exemple » |
| `audit_symetrie: false` | « cas extrêmes » (rappel ≥ 0,98 partout sans aucune fausse alarme, ou aucun critère réussi) | aucun des deux cas extrêmes : pas d'audit de symétrie exigé par ce texte (R4 reste la règle du dépôt) |
| 7 illisibles chez A (1,77 %) | liste d'arrêt : « plus de 2 % d'items illisibles » | sous le seuil : le verdict est permis |
| 9 citations invalides chez B (1,08 %) | liste d'arrêt : « plus de 10 % de citations invalides » | sous le seuil : pas de réserve |
| issues « seul » : A et B tous deux « étiqueteur non validé » par échec décisif de C2 (12 et 27 sur 120) | « Analyses », point 1 : « issues de A seul et de B seul rapportées (« validé seul ») » | rapportées, sans critère ; aucun verdict n'en dépend |

Rappel du texte scellé (« Portée des verdicts », contre-lecture 1, B7) : le verdict de phase 1 est un résultat de mesure ; ce qu'il implique pour la porte décisive n'est pas gelé ici, N-060 v3 (point 1) fixant l'oracle de couverture ; tout emploi de l'étiqueteur à la porte est une proposition au directeur.

## 6. Écarts au texte scellé et à l'ordre, constatés par ce lecteur

1. `timeout 1800 nice -n 10` devant la commande d'analyse (règle de la session mère) ; options et chemins du script inchangés ; code 0.
2. La lecture principale analysée vient d'une **autre machine** (branche `origin/donnees/etiqueteur-phase1-lecture-principale-v1`, dossier `lecture-principale-fille-cles-2-v1`), matérialisée ici par `git show` ; les empreintes des fichiers et des compagnons sont égales à celles rapportées par l'exécutante et au manifeste. Ce lecteur n'a pas vérifié que ce lancement est « le dernier lancement principale+relecture allé à son terme » (liste d'arrêt, avant-dernière ligne) : cela relève du compte rendu de l'exécutante.
3. Deux grandeurs que « Métrique » dit « rapportées » sont absentes du fichier de résultat (fausse alarme absolue des jumeaux, P-5 ; précision). Aucun critère n'en dépend.
4. Aucun autre écart. Aucun fichier existant modifié ; aucun commit ; aucun réseau ; aucun appel de modèle.
