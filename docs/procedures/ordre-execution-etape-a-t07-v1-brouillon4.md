# Ordre d'exécution — étape A de T0.7, variante B (instance A100 neuve, activations recalculées) — v1, brouillon 4

> **VARIANTE B** (décision de la mère, R-2112) : l'étape A ne se joue pas sur l'instance de 7b. Une instance **A100 neuve**,
> créée par la fille après la course de 7b et la poussée de ses résultats, clone le code de T0.7, récupère la sortie de 7b par
> refspec explicite, joue les essais figés **avant** la descente du modèle, borne la taille des sorties, **recalcule les
> activations** (repli, garde d'équivalence), puis joue la passe à blanc et l'étape A, pousse ses sorties sur une branche neuve
> (fichiers lourds en morceaux scellés) et demande l'état « stopped » ; la fille la détruit par son identifiant. **Ligne de GO :
> GO-2026-11-10-06** (mot de Lazar, R-2115), non cumulée avec GO-2026-11-10-04 : **20 USD au total sous les deux lignes**.
> Script de l'instance : **`scripts/etape_a_t07_variante_b_v2.sh`** (`e68d3306…`), neuf arguments.

- **Statut** : brouillon 4, écrit le 2026-11-10 à partir de 15:14 UTC (`date -u`) par un sous-agent développeur **neuf**
  de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv` (Claude Opus 5.5, `claude-opus-5-5`), qui n'a écrit ni T0.7, ni son
  module, ni le script v2, ni les brouillons 1 à 3 de cet ordre, ni leurs contre-lectures (il a lu T0.7 : exclu ensuite de tout
  rôle de lecteur de P3-bis). Consigne de la mère : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-essai-degeneres-ordre-b4-t07-v1.md`
  (`a3e326e46bf00e6392a52e42204ab20e52dd3a3ecddec8e8b10bf26c79be1696`, vérifiée par `sha256sum`). Remplace le brouillon 3
  (`b053a2207006c49d7aca8d8e5975d7539857474d98591368088cda1fc2a1b484`, gardé tel quel, R12) ; les brouillons 1 et 2 restent tels
  quels. Porte : la contre-lecture courte v3 (`d0fe90538160779ea6386a9f3a622ca0636575631254a76a5bec857915e4e8c6`, O-1 à O-6) ;
  le rapport complémentaire 5 (`e58be6c9051d928e3818175ace1dbfd2db6afd2c6e725d7278032dbe13a90e90`, script v2, point 8) ; la
  contre-lecture courte de l'option (c) (`7a32746203bf9b467898dbf82a04f32428bf9bd886f93902f82b57d9b0c719e6`, CLC-03, CLC-08) ;
  la contre-lecture orchestrée du brouillon 22 de T0.7 (`prereg/contre-lectures/T0.7-sondes-v0-v1-brouillon22-cl-orchestree-v1.md`,
  `47537dfa7d4f97d0266f72eb3d791996d2ea0aa8f35a098a721c1d72ab251a60` : GARDES-CODE-01, CONCORDANCE-01 et CLO-08) ; le registre
  R-2153, R-2220, R-2229, R-2231, R-2241, R-2246, R-2249. **La ligne d'essais attendue (`ATT`) est mesurée** dans un clone fait
  comme celui de l'instance (§ 11 bis). **Non contre-lu.** Le script v2 n'est pas modifié : ce que je propose d'y changer est au
  § 13 (une version v3 est une décision de la mère).
- **Texte qui régit l'étape** : le préenregistrement scellé de T0.7, **désigné par sa ligne `SCELLEMENT-T07`** du registre
  `registres/scellements-v1.md` de `main` (P5 ; jamais par une empreinte écrite dans cet ordre) : « Calcul et dépense » (variante
  B : « instance A100 SXM4 80 Go ≤ 1,30 USD de l'heure […] recalcul des activations (point 8, repli) ») ; « Écrits exigés par
  P3-bis » (b) 2 « Variante B » (même code, même configuration, même règle de `sondes_lues`) ; liste d'arrêt (ligne « instance
  d'étiquette `t06…` ou `t07…` déjà sur le compte », CLO-08, R-2249) ; lignes de registre **`GO-LECTURE-T07`** (extrait scellé de
  la ligne du GO cité pour la variante B) et **`CODE-T07`** (DS-3 bis (a), R-2104 ; fichier `CODE-T07-v2.json` au commit C7,
  R-2231).
- **Autorisation** : **GO-2026-11-10-06** (calcul, Lazar ; R-2115 ; `registres/go.md` de `main`) : extension de
  GO-2026-11-10-04 à la variante B ; **dépense totale sous GO-2026-11-10-04 et sous GO-2026-11-10-06 ≤ 20 USD** (O-4) ; instance
  A100, **la H200 seulement après un mot de Lazar** ; échéance le **2026-11-23** ; périmètre : recalcul des activations depuis la
  sortie poussée de 7b, puis passe à blanc et étape A. La délégation GO-2026-10-20-07 (≤ 10 USD par lancement) ne couvre pas le
  pire cas du devis (§ 6).
- **Exécutante** : la fille porteuse des clés (Vast.ai, GitHub, Hugging Face), session `<<ID_SESSION_FILLE>>` ; journal
  `journal-etape-a-t07-b-v1.md`, une ligne datée par geste (`date -u`).

## 0. Objet

Après la fin normale de 7b et la poussée vérifiée de ses résultats : créer une instance A100 neuve qui joue, sans autre geste de la
fille que la surveillance, le script `scripts/etape_a_t07_variante_b_v2.sh` (§ 5) : minuterie ; clone partiel de la seule
branche `main` au commit de scellement S7 ; **registres nommés** de `main` et fichiers qu'ils citent ; **périmètre des jeux**
contrôlé contre l'argument `PERIMETRE` (C-1) ; sortie de 7b par refspec explicite (fichiers nommés) ; paquets ; **essais figés**
(dernière ligne égale à `ATT`, **avant** le modèle, O-1) ; **taille des sorties bornée** (O-2) ; modèle ; puis, **dans cet ordre** :
**`CODE-T07`** (inscrite par la mère avant la création, contrôlée sur l'instance), **repli** (garde d'ouverture d'abord, puis
recalcul et garde d'équivalence), **passe à blanc**, **étape A** ; poussées sur une branche neuve (légers d'abord, fichiers de plus
de 90 Mo en morceaux scellés) ; état « stopped » demandé. La fille vérifie la poussée et **détruit l'instance par son
identifiant** (R10). Ni épisode, ni étape B, ni lecture d'un résultat.

## 0 bis. Ce qui change depuis le brouillon 3

| Point | Source | Réglé par le script v2 (`e68d3306…`) | Porté par cet ordre | Reste |
|---|---|---|---|---|
| **O-1** ligne d'essais | `d0fe9053…` ; `e58be6c9…` § 8 ; CLC-03 | essais joués à l'étape 6, **avant** la borne de taille et le modèle (étape 8) ; mode de mesure `ARRET_APRES_ESSAIS` (essai local seulement) | `ATT` **mesurée** dans un clone fait comme celui de l'instance, à la branche qui porte l'essai GARDES-CODE-01 (§ 11 bis) ; conditions de validité contrôlées par la fille (P12) ; commande de remesure écrite | essais joués **après** les paquets (≤ 1 h, attendu 0,15 h payées en cas d'écart) ; interpréteur de la mesure 3.13 contre 3.11 sur l'instance (§ 13, S-2) ; `8cb539f9` atteignable depuis `main` (fusion « ours », R-2229) : l'essai du miroir passe à la mesure |
| **O-2** taille des sorties | `d0fe9053…` | étape 7 : borne haute calculée **avant toute ouverture** (§ 5 bis), au-dessus de 2 000 000 000 octets → code 2, rien d'ouvert ; tout fichier de plus de 90 000 000 octets découpé en morceaux de 50 000 000 octets scellés, manifeste scellé, recomposition vérifiée sur l'instance, poussée par lots de 10 | § 5 bis (calcul écrit) ; § 4.6 (vérification des morceaux sans rien rapatrier) ; § 9 (recomposition avant l'étape B) | borne non confrontée à une sortie réelle (répétition jouet seulement) |
| **O-3** minuterie | `d0fe9053…` | chaque `DELETE` journalisé avec son code HTTP ; la minuterie meurt avec le conteneur à l'état « stopped » (dit par le script) | § 4.7 corrigé : après « stopped », **seule la fille détruit** ; rappel daté à `ECH` (fille et mère) | `DELETE` réel avec la clé de l'instance non répété (API locale seulement) |
| **O-4** dépense antérieure | `d0fe9053…` | — | `ANT0` = dépense inscrite sous **GO-2026-11-10-04 et GO-2026-11-10-06** ; P8 de même ; échéance de la minuterie bornée par `20 − ANT0` (§ 4.4) | — |
| **O-5** registres | `d0fe9053…` ; `e58be6c9…` § 3 | registres **nommés** (`scellements-v1.md`, `.ouvertures.md`, `ouvertures-p3bis-v1.md`, `prealables-p3bis-v1.md`, `go.md`) ; `registres/index-bras-attaque*` hors de l'extraction et refusé par `interdit()` | le clone de la fille n'extrait plus `/registres/*.md` mais des registres nommés (§ 4.1) | chemins de 7a cités par un registre : non refusés par `interdit()` (§ 13, S-3) ; contrôle de la fille au § 4.1 |
| **O-6** | `d0fe9053…` | en-tête « brouillon 4 » | § 4.4 : un écart d'encodage du script **arrête le bloc** (aucune création) | recopie des journaux du script des jeux : jouée par la mesure avec un journal présent par jeu (§ 11 bis), pas encore sur une instance |
| **C-1 et option (c)** | `d0fe9053…` C-1 ; R-2166 ; `e58be6c9…` § 5 | argument `PERIMETRE` exigé, ni plus ni moins que les lignes de `main` ; passage « sans concepts » répété (code 0, phrases non lues) | marqueur `PERIMETRE_T07` ; P3 et § 4.1 : périmètre recalculé du registre et comparé ; règle de fermeture écrite | décision de la mère : attendre ou non `SCELLEMENT-JEUX-T07-JC` et `SCELLEMENT-CONCEPTS-T07` avant la création (P3) |
| **Règle de C7** | R-2231 ; R-2241 Q-5 | contrôles `C7` ancêtre de S7, `git diff --quiet C7 S7 -- src tests`, S7 ancêtre de `main` | P6 et P9 : `src/` de C7 égal à `37485ce5`, `tests/` de C7 égal à celui de S7, `CODE-T07` cite `CODE-T07-v2.json` au commit C7 | — |
| **Filtre d'inventaire** | CLO-08, CLO-09, R-2249 | — | § 4.2 et P10 : étiquettes `t06…` et `t07…` seules | étiquettes des autres tâches (§ 13, S-5) |
| **GARDES-CODE-01** | `47537dfa…` ; R-2249 | — | essai `tests/test_t07_tirages_degeneres_v1.py` versé avant C7 (P9) ; compté dans `ATT` | fusion dans `main` par la mère |
| **CLC-08** | `7a327462…` | non réglé (l. 362 du script) | § 7 : la fille lit le motif dans `repli-<n>.err` avant de conclure « ligne manquante » | § 13, S-4 |

## 1. Cadre

| Élément | Valeur |
|---|---|
| Code de T0.7 | **C7** : commit de `main` dont `src/` égale celui de `37485ce50601b7d7ff9035bc34c734ec689ca731` (arbre `744a9e16…`) et dont `tests/` égale celui de S7, fixé après la fusion des essais CLC-04 et GARDES-CODE-01 (R-2231, R-2241 Q-5 et Q-6, R-2249) ; **S7** : commit de scellement de T0.7, descendant de C7, `git diff --quiet C7 S7 -- src tests`, ancêtre de `main` ; contrôlés par la fille (§ 4.1) et sur l'instance |
| Script de l'instance | `scripts/etape_a_t07_variante_b_v2.sh`, sha256 `e68d3306bd76a549ec97eb6b153d03ec544c92944ae74293d8c0db8cfda62269` (commit `04bc14a2`, sur `main`) ; répété en jouet (rapport complémentaire 5, § 5, passage 4 ; rejoué par la contre-lecture `7a327462…`, § 2) |
| Arguments | `S7 C7 RUN6 CFG BR BR7B 'ATT' ECH PER` (neuf, dans cet ordre) |
| Configuration | `CFG` (ligne (A)), copiée sous `prereg/` et scellée dans S7 (base : `brouillons/T0.7-sondes-v0-v1-brouillon19-pieces/configuration-t07-v4.json`, `3d19b08c…`, `code_t07_exige` vrai) ; empreinte canonique `<<EMPREINTE_CONFIG_T07>>`, revérifiée sur l'instance ; **chemins qu'elle cite** (lus par le script, étape 2) : les six de la v4 (§ 11 bis), contrôlés par la fille (P12) |
| Périmètre des jeux | `PER` (ligne (A)) : lignes `SCELLEMENT-JEUX-T07-JD`, `-JA`, `-JC`, `SCELLEMENT-CONCEPTS-T07` présentes à `main` à la création, séparées par des virgules (`JD,JA` à l'écriture de cet ordre), ou `aucun` |
| Course lue | 7b : run `RUN6`, branche `BR7B` (`calcul/t06-confirmation-7b-v1`, ou `-v2`, `-v3`), lue par refspec explicite |
| Machine | une **A100 SXM4 80 Go**, ≤ 1,30 USD de l'heure ; filtre de la chaîne de T0.6 (`session_v7.filtre_recherche`, `1609a4bf` : `reliability>=0.98`, `inet_down>=500`, `cuda_max_good>=13.0`) ; ≥ 16 cœurs, ≥ 128 Go de mémoire vive ; **disque 100 Go** (modèle ≈ 16 Go, paquets ≈ 10 Go, activations recalculées ≈ 31,5 Go, sorties ≤ 2 Go et leurs morceaux) ; image `python:3.11-bookworm` ; étiquette `t07-b-v1` ; mode « args » (aucun serveur SSH) ; **H200 seulement après un mot de Lazar**, hors de cet ordre |
| Dossier de la fille | `/home/user/etape-a-t07-b-v1/` (neuf ; `-v2` à une reprise) |
| Branche de sortie | **`donnees/t07-etape-a-v1`**, absente du dépôt distant avant la première poussée (contrôlé par le script) ; sinon `-v2` ; jamais `main`, jamais une branche `calcul/…` |
| Dépôt | `https://github.com/lciric/controle-ia-travail.git`, en dur dans le script hors essai ; jamais `lciric/controle-ia` |
| Échéances | création après la poussée vérifiée de 7b et les préalables du § 3, au plus tard le **2026-11-22 à 12:00Z** ; **minuterie** : destruction par l'identifiant à `ECH` = création + `HMAX` (≤ 12 h, § 4.4), tant que le conteneur vit ; la fille détruit dès la poussée vérifiée |

## 2. Embargos et chemins interdits

1. **Jamais** la fille ni l'instance n'ouvrent, n'affichent, ne copient, ne hachent ni ne passent à un outil un
   `lecture-sondes-t06.json` (de 7b, de 7a, d'aucun run) ni son compagnon. Sur l'instance, la branche de 7b est lue par refspec
   explicite dans un **clone partiel** (`--filter=blob:none`) : seuls les fichiers **nommés** sont extraits (`runs/<run>/manifeste.json`,
   `diag/<run>/episodes-t06.json`, `diag/<run>/distillation-t06.json`, `diag/<run>/arret.json` s'il existe, et, dans
   `donnees/<run>/`, adaptateurs, mesures, textes, manifeste et morceaux du sous-ensemble) ; `diag/<run>/` n'est jamais listé ; le
   contenu de `lecture-sondes-t06.json` **n'est jamais descendu** ; le script s'arrête s'il le trouve dans l'arbre.
2. **Jamais** `donnees/lecture-b-7a-quarantaine-v1`, la branche `essai/t06-explo-v3`, ni `diag/`, `runs/`, `donnees/` de 7a
   (`20261109-070232-t06-reel`) ; clones de la **seule branche `main`** (`--single-branch`), `git fetch` par refspec explicite ;
   un registre qui citerait un chemin de 7a arrête la fille avant la création (§ 4.1 ; § 13, S-3).
3. **Jamais** `scripts/extraire_mesures_epreuve_t06_v1.py`, `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`,
   `docs/notes/bras-attaque/`, `registres/index-bras-attaque*` (O-5 : ni dans le clone de la fille, ni sur l'instance),
   l'étiqueteur ; **règle 9** : aucune recherche récursive sur un arbre qui contient un chemin interdit sans l'exclure (`git grep`
   avec exclusions) ; jamais `verifier-arbre`.
4. **Aucune lecture de résultat de 7b** : `lecture-cout-t06.json`, `resume.json`, `distillation-t06.json`, `episodes-t06.json`,
   `run.err` jamais affichés (le module de T0.7 lit ce qu'il lui faut ; la fille, rien).
5. **Aucune lecture des sorties de l'étape A** (`scores-actions-t07.npz`, ses morceaux, `sondes-t07.json`, `ouverture-t07.json`,
   `notation-t07.json`, `sondes-neuves-t07.npz`, ses morceaux, `temoins-lexicaux-t07.json`, manifeste du run de T0.7) : hachées
   ou comptées, jamais affichées. Peuvent être lus, sans donnée décisive : le rapport du repli, la sortie de la passe à blanc,
   `taille-estimee.json`, le motif d'un `repli-<n>.err`, et les champs `octets`, `morceaux[].fichier`, `morceaux[].octets` et
   `morceaux[].sha256` des manifestes `*.morceaux.json` (§ 4.6) ; la fille n'en recopie que les champs du § 8.
6. **Aucune sortie de P3-bis lue ni citée** : seul le module lit, par sa garde, les registres de P3-bis (présence, date, sceau).
7. **Secrets** : clés par leur nom (`HF_TOKEN`, jeton GitHub) ; jamais `env`, `printenv`, `set` sans argument, `export -p`,
   `/proc/*/environ` ; jamais affichés `creation-brute.json`, `offres.json`, `instances.json` ; garde des secrets à 0 avant tout
   envoi de texte.

## 3. Préalables bloquants (vérifiés par la fille, écrits au journal avec l'heure)

| # | Préalable | Où | Sinon |
|---|---|---|---|
| P1 | **Course 7b** : fin normale, branche `BR7B` poussée, rapatriement vérifié (compte rendu de la fille de 7b) ; **l'instance de 7b est détruite** selon son ordre (étiquette `t06-v2` : elle bloquerait P10) | compte rendu ; § 4.2 | attente |
| P2 | **`RUN-CONFIRMATION-T06`** au registre de `main`, chemin `runs/<RUN6>/manifeste.json` ; **le même fichier** sur `BR7B` (empreinte égale) | § 4.1 | attente |
| P3 | **Périmètre des jeux** (C-1, option (c)) : au plus une ligne chacune parmi `SCELLEMENT-JEUX-T07-JD`, `-JA`, `-JC` et `SCELLEMENT-CONCEPTS-T07` ; `PER` égale exactement l'ensemble des lignes présentes à `main` ; fichiers, compagnons et journaux du script des jeux sur `main`. **Règle de fermeture** : la première ligne `OUVERTURE-T07` de l'étape A de ce run, écrite par la **garde du repli** (avant tout recalcul), ferme le périmètre ; une ligne inscrite après est exclue pour de bon. **Option (c)** : sans `SCELLEMENT-CONCEPTS-T07`, l'étape A va au bout « sans concepts » (phrases non lues, aucune direction ni tâche de plancher de concept ; T7-P9 « non lue », réserve R15 à l'étape B) ; la mère dit par un écrit daté, recopié au journal avant la création, si elle attend `-JC` et les concepts | § 4.1 | attente (décision de la mère) |
| P4 | **`GO-LECTURE-T07`** : une ligne ; son extrait scellé est une ligne de `registres/go.md` et nomme `GO` (ligne (A)) ; non révoquée, non échue ; aucune ligne `GO-ETAPE-A-T07`, ou, si elle existe, la garde lira l'une ou l'autre (écrit au journal) | § 4.1 | rien |
| P5 | **`SCELLEMENT-T07`** : une ligne, égale à `<<LIGNE_SCELLEMENT_T07>>` (c'est elle qui désigne le texte scellé de T0.7) | § 4.1 | arrêt, nœud |
| P6 | **`CODE-T07`** : une ligne, inscrite par la mère avant la création, citant **`registres/code-t07/CODE-T07-v2.json`** (écrit par `python -m controle_ia.t07.code_t07_v1 ecrire <clone> C7 registres/code-t07/CODE-T07-v2.json`, scellé ; R-2231) dont le champ `commit` est C7 ; `CODE-T07-v1.json` reste versé, jamais cité | § 4.1 | rien |
| P7 | `SCORES-T07`, `SONDES-T07` absentes ; `VERDICT-P3BIS` et le journal de P3-bis relevés (présence, date), jugés par la garde | § 4.1 | arrêt, nœud |
| P8 | **Engagement** de dépense sous `GO` au registre des dépenses (mère) ; **`ANT0` = dépense déjà inscrite sous GO-2026-11-10-04 et sous GO-2026-11-10-06** (O-4) ; **`20 − ANT0` ≥ pire cas du devis** (§ 6 : 15,5 USD), soit `ANT0` ≤ 4,5 USD | § 4.1 | rien (au-delà : devis neuf, mot de Lazar) |
| P9 | **Code** (R-2231) : C7 ancêtre de S7 ; `src/` de C7 égal à `37485ce5` ; `git diff --quiet C7 S7 -- src tests` ; S7 ancêtre de `main` ; essais CLC-04 (`tests/test_t07_ouvrir_reel_concepts_v1.py`) et GARDES-CODE-01 (`tests/test_t07_tirages_degeneres_v1.py`) présents à S7 ; script de l'instance à son empreinte (§ 1) | § 4.1 | arrêt |
| P10 | `vastai` 1.8.3 ; `HF_TOKEN` et le jeton GitHub présents (par le nom) ; **inventaire : aucune instance d'étiquette `t06…` ni `t07…`** (CLO-08 : une instance d'une autre tâche du programme — P3-bis, T0.8, pièces HD ou R du texte de validité de l'adaptateur — n'interdit ni ne retarde la création) | § 4.2 | attente (`t06…` de 7b non détruite) ; arrêt (autre) |
| P11 | **Heure** : création au plus tard le 2026-11-22 à 12:00Z | `date -u` | nœud |
| P12 | **Ligne d'essais `ATT`** (O-1) valable pour S7 : arbre `tests/` de S7 = `79230a584e8675f1771fd4f0a9315de71c2bcbdc`, arbre `src/` de S7 = `744a9e16f1635ff402e798b4ac868a57311e44b8` (ceux de la mesure, § 11 bis) ; la configuration `CFG` cite les six chemins de la v4 ; sinon `ATT` est **remesurée** par la commande du § 11 bis à S7, avant la création | § 4.1 | remesure (mère), puis seulement création |

## 4. Étapes et commandes (session de la fille)

L'état du shell ne survit pas d'une commande à l'autre : **chaque bloc commence par la ligne (A)**. Les clés passent par leur nom.

**(A)** :

```bash
W=/home/user/etape-a-t07-b-v1; M=$W/main; J=$W/journal-etape-a-t07-b-v1.md; GO=GO-2026-11-10-06; GO4=GO-2026-11-10-04; PLAF=20; ANT0=<<DEPENSE_ANTERIEURE_USD>>; RUN6=<<RUN_T06_7B>>; BR7B=<<BRANCHE_7B>>; C7=<<COMMIT_CODE_T07>>; S7=<<COMMIT_SCELLEMENT_T07>>; CFG=<<CHEMIN_CONFIG_T07>>; PER=<<PERIMETRE_T07>>; ATT='346 passed, 2 skipped, 4 xfailed'; BR=donnees/t07-etape-a-v1; SCRIPT=scripts/etape_a_t07_variante_b_v2.sh; SHA_SCRIPT=e68d3306bd76a549ec97eb6b153d03ec544c92944ae74293d8c0db8cfda62269; URL=https://github.com/lciric/controle-ia-travail.git; j() { printf '%s %s\n' "$(date -u +%FT%TZ)" "$*" >> "$J"; }
```

### 4.1 Préalables depuis `main` (lecture seule)

```bash
# (A) — registres NOMMÉS (O-5) : jamais le motif /registres/*.md, qui extrairait registres/index-bras-attaque*
mkdir -p "$W" && git clone -q --filter=blob:none --no-checkout --single-branch --branch main "$URL" "$M" && git -C "$M" sparse-checkout set --no-cone '/registres/scellements-v1.md' '/registres/go.md' '/registres/depenses.md' '/registres/ouvertures-p3bis-v1.md' '/registres/prealables-p3bis-v1.md' '/registres/go-extraits/' '/registres/code-t07/' "/$SCRIPT" && git -C "$M" checkout -q main && git -C "$M" rev-parse HEAD; j "main $(git -C "$M" rev-parse HEAD)"
REG="$M/registres/scellements-v1.md"; for k in RUN-CONFIRMATION-T06 SCELLEMENT-JEUX-T07-JD SCELLEMENT-JEUX-T07-JA SCELLEMENT-JEUX-T07-JC SCELLEMENT-CONCEPTS-T07 GO-LECTURE-T07 GO-ETAPE-A-T07 SCELLEMENT-T07 CODE-T07 SCORES-T07 SONDES-T07 VERDICT-P3BIS; do printf '%s %s\n' "$k" "$(grep -c "^| $k |" "$REG")"; done
P=; for k in JD JA JC CONCEPTS; do c=SCELLEMENT-JEUX-T07-$k; [ "$k" = CONCEPTS ] && c=SCELLEMENT-CONCEPTS-T07; [ "$(grep -c "^| $c |" "$REG")" = 1 ] && P="$P,$k"; done; P=${P#,}; [ -n "$P" ] || P=aucun; [ "$P" = "$PER" ] && echo "PERIMETRE conforme ($PER)" || echo "ÉCART : PERIMETRE $PER, registre $P"
awk -F'|' 'NF >= 6 { gsub(/ /, "", $4); print $4 }' "$REG" "$M/registres/prealables-p3bis-v1.md" 2>/dev/null | grep -E '20261109-070232-t06-reel|lecture-sondes-t06|bras-attaque|mode-tenu-a-l-ecart|lecture-b-7a|extraire_mesures_epreuve' | wc -l
LR=$(grep '^| RUN-CONFIRMATION-T06 |' "$REG"); PR=$(printf '%s\n' "$LR" | awk -F'|' '{gsub(/ /,"",$4); print $4}'); HR=$(printf '%s\n' "$LR" | awk -F'|' '{gsub(/ /,"",$5); print $5}'); [ "$PR" = "runs/$RUN6/manifeste.json" ] && git -C "$M" fetch -q origin "refs/heads/$BR7B:refs/remotes/origin/$BR7B" && [ "$(git -C "$M" show "refs/remotes/origin/$BR7B:$PR" | sha256sum | cut -d' ' -f1)" = "$HR" ] && echo "RUN-CONFIRMATION-T06 conforme à $BR7B"
LA=$(grep '^| GO-LECTURE-T07 |' "$REG"); PA=$(printf '%s\n' "$LA" | awk -F'|' '{gsub(/ /,"",$4); print $4}'); HA=$(printf '%s\n' "$LA" | awk -F'|' '{gsub(/ /,"",$5); print $5}'); [ "$(sha256sum < "$M/$PA" | cut -d' ' -f1)" = "$HA" ] && [ "$(cut -d' ' -f1 "$M/$PA.sha256")" = "$HA" ] && [ "$(grep -c '^| GO-' "$M/$PA")" = 1 ] && grep -qxF -- "$(grep '^| GO-' "$M/$PA")" "$M/registres/go.md" && grep -q "^| $GO |" "$M/$PA" && echo "GO-LECTURE-T07 conforme ($GO)"
[ "$(grep '^| SCELLEMENT-T07 |' "$REG")" = "$(cat "$W/ligne-scellement-t07.txt")" ] && echo "SCELLEMENT-T07 inchangée"
LC=$(grep '^| CODE-T07 |' "$REG"); PC=$(printf '%s\n' "$LC" | awk -F'|' '{gsub(/ /,"",$4); print $4}'); HC=$(printf '%s\n' "$LC" | awk -F'|' '{gsub(/ /,"",$5); print $5}'); [ "$PC" = registres/code-t07/CODE-T07-v2.json ] && [ "$(sha256sum < "$M/$PC" | cut -d' ' -f1)" = "$HC" ] && [ "$(cut -d' ' -f1 "$M/$PC.sha256")" = "$HC" ] && [ "$(python3 -I -c 'import json,sys; print(json.load(open(sys.argv[1]))["commit"])' "$M/$PC")" = "$C7" ] && echo "CODE-T07 conforme (CODE-T07-v2.json, C7)"
grep -cE "$GO4|$GO" "$M/registres/depenses.md"
git -C "$M" merge-base --is-ancestor "$C7" "$S7" && git -C "$M" diff --quiet 37485ce50601b7d7ff9035bc34c734ec689ca731 "$C7" -- src && git -C "$M" diff --quiet "$C7" "$S7" -- src tests && git -C "$M" merge-base --is-ancestor "$S7" HEAD && [ -n "$(git -C "$M" ls-tree "$S7" -- tests/test_t07_ouvrir_reel_concepts_v1.py)" ] && [ -n "$(git -C "$M" ls-tree "$S7" -- tests/test_t07_tirages_degeneres_v1.py)" ] && [ "$(sha256sum < "$M/$SCRIPT" | cut -d' ' -f1)" = "$SHA_SCRIPT" ] && echo "code et script conformes"
[ "$(git -C "$M" rev-parse "$S7:tests")" = 79230a584e8675f1771fd4f0a9315de71c2bcbdc ] && [ "$(git -C "$M" rev-parse "$S7:src")" = 744a9e16f1635ff402e798b4ac868a57311e44b8 ] && [ "$(git -C "$M" show "$S7:$CFG" | python3 -I -c 'import json,sys
def f(x):
    if isinstance(x, dict):
        if isinstance(x.get("chemin"), str): yield x["chemin"]
        for v in x.values(): yield from f(v)
    elif isinstance(x, list):
        for v in x: yield from f(v)
print(" ".join(sorted(set(f(json.load(sys.stdin))))))')" = "diag/20261019-230011-p3-reel/sondes-figees.json donnees/20261007-082440-t05-extraction/taches-entrainement.json donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz donnees/T0.7-faits-repe-v1/facts_true_false.csv donnees/T0.7-models-under-pressure-v1/training/train.jsonl runs/20261019-230011-p3-reel/manifeste.json" ] && echo "ATT valable pour S7"
```

Attendus : `1` pour `RUN-CONFIRMATION-T06`, `GO-LECTURE-T07`, `SCELLEMENT-T07`, `CODE-T07` ; `0` ou `1` pour chaque ligne de
jeux et pour les concepts, et « PERIMETRE conforme » ; `0` pour `SCORES-T07`, `SONDES-T07` ; `GO-ETAPE-A-T07` et
`VERDICT-P3BIS` relevés ; **`0`** pour le compte des chemins interdits ou de 7a cités par un registre (sinon nœud : le script de
l'instance ne refuse pas un chemin de 7a, § 13, S-3) ; les messages « conforme », « inchangée », « code et script conformes »,
« ATT valable pour S7 » ; au moins une ligne d'engagement, et `ANT0` = somme des dépenses inscrites sous les deux lignes.
`ligne-scellement-t07.txt` : la ligne `SCELLEMENT-T07` (P5), écrite à l'octet par la fille au début. « ATT valable » absent :
P12, remesure par la mère (§ 11 bis), nouvelle valeur de `ATT` écrite au journal par un écrit daté de la mère. La branche de 7b
est lue **par refspec**, dans un clone partiel, et seul le manifeste y est lu (empreinte, jamais affiché).

### 4.2 Outil et inventaire (filtre `t06…` et `t07…` seulement : CLO-08, R-2249)

```bash
# (A)
vastai --version; date -u +%FT%TZ
timeout -k 5 120 vastai show instances --raw 2>/dev/null | python3 -I -c 'import json,sys; d=json.load(sys.stdin); d=d.get("instances", d) if isinstance(d, dict) else d; print([(i.get("id"), i.get("label"), i.get("actual_status")) for i in (d or []) if str(i.get("label") or "").startswith(("t06", "t07"))])'
```

Seuls l'identifiant, l'étiquette et l'état des instances `t06…` et `t07…` sont imprimés. **Attendu : liste vide.** Une instance
d'une autre tâche du programme (P3-bis, T0.8, pièces HD ou R du texte de validité) n'est pas imprimée et n'interdit ni ne
retarde la création (liste d'arrêt de T0.7, CLO-08 ; écrits gelés (b) 1 et 2). Une instance `t06…` (celle de 7b, `t06-v2`, non
encore détruite) : attente de sa destruction selon son ordre, puis inventaire refait. Une instance `t07…` : arrêt, compte rendu
(une seconde instance de cette étape ne se crée jamais sans écrit de la mère).

### 4.3 Recherche de l'offre

```bash
# (A)
timeout -k 5 120 vastai search offers 'num_gpus=1 rentable=true gpu_name=A100_SXM4 reliability>=0.98 inet_down>=500 cuda_max_good>=13.0 cpu_ram>=128 cpu_cores_effective>=16 disk_space>=100 dph_total<=1.3' -o dph_total --storage 100 --raw > "$W/offres.json" 2>"$W/offres.err"; echo "code $?"
python3 -I -c 'import json,sys; o=json.load(open(sys.argv[1])); o=o.get("offers", o) if isinstance(o, dict) else o; o=[x for x in o if x.get("gpu_name")=="A100 SXM4" and x.get("num_gpus")==1 and float(x.get("dph_total",9))<=1.3 and float(x.get("gpu_ram",0))>=79000]; x=o[0] if o else None; print("aucune offre" if x is None else "id=%s carte=%s prix_h=%.4f stockage_h=%s machine=%s cuda=%s offres=%d" % (x["id"], x["gpu_name"], float(x["dph_total"]), x.get("storage_total_cost"), x.get("machine_id"), x.get("cuda_max_good"), len(o)))' "$W/offres.json"
```

Au plus **trois** recherches, espacées d'au moins 30 minutes ; vides : compte rendu, nœud (aucune autre carte sans mot). Le prix
horaire relevé (`prix_h`, carte et disque compris) entre au relevé de dépense (§ 6) et à la borne de la minuterie (§ 4.4) ;
`offres.json` n'est jamais affiché.

### 4.4 Création, une fois

```bash
# (A) ; OFFRE = l'id de la ligne imprimée au § 4.3 ; PRIX_H = son prix_h
B64=$(base64 -w0 < "$M/$SCRIPT") && [ "$(printf %s "$B64" | base64 -d | sha256sum | cut -d' ' -f1)" = "$SHA_SCRIPT" ] || { echo "ÉCART : encodage du script : aucune création"; j "ÉCART : encodage du script"; exit 2; }
HMAX=$(python3 -I -c 'import sys; p,a=map(float,sys.argv[1:3]); print(max(0, min(43200, int((20.0 - a - 1.2 - 0.1) / p * 3600))))' "$PRIX_H" "$ANT0"); [ "$HMAX" -ge 39240 ] || { echo "ÉCART : borne de la minuterie $HMAX s < pire cas du devis : aucune création (nœud)"; exit 2; }
TC=$(date +%s); ECH=$((TC + HMAX)); j "création demandée, TC=$TC, échéance de la minuterie $ECH (HMAX=$HMAX s)"
GO_ID=$GO timeout -k 10 300 vastai create instance "$OFFRE" --raw --image python:3.11-bookworm --disk 100 --cancel-unavail --label t07-b-v1 --env "-e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN" --entrypoint bash --args -c "echo $B64 | base64 -d > /root/etape-a-t07-b.sh && bash /root/etape-a-t07-b.sh $S7 $C7 $RUN6 $CFG $BR $BR7B '$ATT' $ECH $PER" > "$W/creation-brute.json" 2>&1; echo "code $?"
python3 -I -c 'import json,sys; d=json.load(open(sys.argv[1])); print("succès :", d.get("success"), "; identifiant :", d.get("new_contract"))' "$W/creation-brute.json"
```

`GO_ID=$GO` en tête : la garde de calcul de la session exige un GO valide de `registres/go.md` dans la commande. **O-6** : un écart
d'encodage du script, ou une borne de minuterie sous le pire cas du devis (39 240 s = 10,9 h, § 6), **arrête le bloc** : aucune
création. **O-4** : `HMAX` = la plus petite de 12 h et de la durée que paie `20 − ANT0 − 1,20 (téléchargement) − 0,10 (disque
après l'arrêt)` au prix relevé. L'identifiant imprimé devient `ID` (écrit au journal) ; `creation-brute.json` n'est jamais
affiché. Création incertaine (code ≠ 0 sans identifiant) : inventaire (§ 4.2) avant tout autre geste ; **aucune seconde
création** sans écrit de la mère. **Rappel daté à `ECH`** (O-3) : la fille l'écrit au journal et le pose dans sa session ; la mère
le pose aussi dans la sienne (inventaire du § 4.2 à `ECH`, destruction par l'identifiant si l'instance est encore là).

### 4.5 Surveillance (toutes les 15 minutes ; aucun couperet de temps)

```bash
# (A) ; ID, TC et PRIX_H du journal
timeout -k 5 120 vastai logs "$ID" --tail 400 2>/dev/null | grep -E '^[0-9TZ:-]+ T07 ' | tail -n 20
out=$(timeout -k 5 120 vastai show instance "$ID" --raw 2>/dev/null); printf '%s' "$out" | python3 -I -c 'import json,sys; d=json.load(sys.stdin); d=d.get("instances", d) if isinstance(d, dict) else d; d=d[0] if isinstance(d, list) else d; print("état :", d.get("actual_status"), "/", d.get("intended_status"))'
python3 -I -c 'import sys,time; p,tc,ant=map(float,sys.argv[1:4]); h=(time.time()-tc)/3600; c=ant+p*h+1.2; print(f"cumul sous GO-2026-11-10-04 et GO-2026-11-10-06 ≈ {c:.2f} USD (carte et disque {p*h:.2f}, téléchargement borné 1,20, antérieur {ant:.2f}) ; projeté + 15 min {c+p/4:.2f}")' "$PRIX_H" "$TC" "$ANT0"
```

Seules les lignes `… T07 …` du script sont lues (jamais d'état de sonde, d'aire ni de score : le script n'en imprime aucun).
Attendu, dans l'ordre : minuterie lancée (PID, échéance) ; carte ; code conforme ; cinq lignes « registre … » (recopié de main ou
absent) ; une ligne par élément du périmètre (présent, journaux du script ; ou « absente, hors du périmètre ») ; registres
recopiés, périmètre `PER` ; sortie de 7b extraite ; **essais : code 0, ligne égale à `ATT`** ; **taille estimée … ≤ borne**
(octets, morceaux prévus) ; disque libre ; modèle au cache local ; configuration et empreinte ; `CODE-T07 conforme` ; repli, essai
1, code 0 (« recalcul fait ») ; « poussé » ; passe à blanc code 0 ; « poussé » ; étape A code 0, run ; « poussé » (légers) ;
« découpé (O-2) » et « poussé … morceaux » s'il y a des fichiers de plus de 90 Mo ; « poussé » (traces) ; `FIN` ; « fin, code
0 ; état « stopped » demandé : HTTP 200 ». Une ligne `ARRET` : § 7. Une ligne `MINUTERIE` : l'échéance est atteinte (§ 4.7).

### 4.6 Vérification de la poussée (sans rien rapatrier des sorties)

```bash
# (A)
git -C "$M" ls-remote origin "refs/heads/$BR"; git -C "$M" fetch -q --filter=blob:none origin "refs/heads/$BR:refs/remotes/origin/$BR" && git -C "$M" log --format=%s "$S7..origin/$BR" | head -n 20 && git -C "$M" diff --stat "$S7" "origin/$BR" -- src tests | tail -n 1
R7=refs/remotes/origin/$BR; for f in $(git -C "$M" diff --name-only --diff-filter=A "$S7" "$R7" -- replis-t07 passes-blanches-t07 runs diag donnees | grep -v '\.sha256$' | grep -v 'lecture-sondes-t06' | grep -v '\.morceau-[0-9][0-9][0-9]$'); do a=$(git -C "$M" show "$R7:$f" | sha256sum | cut -d' ' -f1); b=$(git -C "$M" show "$R7:$f.sha256" 2>/dev/null | cut -d' ' -f1); [ "$a" = "$b" ] && echo "OK $f" || echo "ÉCART $f"; done
for m in $(git -C "$M" diff --name-only --diff-filter=A "$S7" "$R7" -- donnees | grep '\.morceaux\.json$'); do git -C "$M" show "$R7:$m" | python3 -I -c 'import json,subprocess,sys
m = json.load(sys.stdin); r, ref, base, nom = sys.argv[1:5]
def g(*a):
    p = subprocess.run(["git", "-C", r, *a], capture_output=True, text=True)
    return p.stdout if p.returncode == 0 else ""
noms = set(g("ls-tree", "-r", "--name-only", ref, "--", base).split())
ok = all(base + "/" + x["fichier"] in noms and (g("show", ref + ":" + base + "/" + x["fichier"] + ".sha256").split() or [""])[0] == x["sha256"] for x in m["morceaux"]) and sum(x["octets"] for x in m["morceaux"]) == m["octets"]
print("OK" if ok else "ÉCART", nom, len(m["morceaux"]), "morceaux")' "$M" "$R7" "$(dirname "$m")" "$m"; done
git -C "$M" show "$R7:registres/scellements-v1.md" | grep -E '^\| (SCORES|SONDES)-T07 \|' | cut -d'|' -f2,3
```

Attendu : les commits de la branche (garde et repli, passe à blanc, étape A légers, morceaux par lots s'il y en a, traces),
**aucun changement sous `src` ni `tests`**, `OK` pour chaque fichier léger **ajouté par l'instance** (jamais un fichier venu de
`main` ou de 7b ; les activations ne sont jamais poussées ; le rapport du repli est
`donnees/<run>/activations/rapport-repli-t07.json`), `OK` pour chaque manifeste de morceaux (chaque morceau nommé présent dans l'arbre, son compagnon égal à l'empreinte que le
manifeste écrit, somme des tailles écrites égale à la taille du fichier ; **aucun morceau descendu** : le clone est partiel, seuls
l'arbre, les manifestes et les compagnons sont lus ; `git ls-tree -l` n'est pas employé, il descendrait chaque morceau pour en
donner la taille), et les deux lignes `SCORES-T07`, `SONDES-T07` (clé et date seulement). L'empreinte de chaque morceau et la
recomposition se vérifient avant l'étape B (§ 9).

### 4.7 Arrêt et destruction par l'identifiant (R10), inventaire final

```bash
# (A)
timeout -k 5 120 vastai destroy instance "$ID" -y; echo "code $?"; j "destruction demandée ($ID)"
out=$(timeout -k 5 120 vastai show instance "$ID" --raw 2>&1); c=$?; [ "$out" = '{"instances": null}' ] && echo "absente (texte exact), code $c" || echo "texte autre (non affiché), code $c"
```

Dès la poussée vérifiée (§ 4.6), ou sur un `ARRET` une fois ses traces poussées, ou à l'atteinte du plafond (§ 6). **O-3,
corrigé** : le script demande de lui-même l'état « stopped » à sa fin (`FIN` ou `ARRET`) ; **la minuterie, sous-processus du
conteneur, meurt alors avec lui** : elle ne garantit la destruction que si l'instance tourne encore à `ECH`. Après « stopped »,
**seule la fille détruit** ; le disque reste facturé (≤ 0,08 USD de l'heure) jusqu'à la destruction : rappel daté à `ECH`
(§ 4.4), et, si la session de la fille tombe, la mère fait détruire par l'identifiant écrit au journal. Une ligne
`MINUTERIE : DELETE, essai n : HTTP c` au journal de l'instance dit l'essai de destruction et son code ; « cinq DELETE sans
succès » : destruction par la fille, aussitôt. Du **seul identifiant créé** ; jamais `pkill`, `killall`, ni un geste sur une
autre instance ; inventaire du § 4.2 après.

## 5. Ce que joue l'instance (`scripts/etape_a_t07_variante_b_v2.sh`, `e68d3306…`)

0. **Arguments et minuterie** : neuf arguments ; `ECH` dans [maintenant, maintenant + 24 h] ; `PERIMETRE` parmi `JD`, `JA`, `JC`,
   `CONCEPTS` ou `aucun` ; `ATTENDU` « - » refusé hors mesure ; variables d'essai refusées hors essai ; minuterie : `DELETE` de
   l'instance par son identifiant (`CONTAINER_ID`, API de Vast) à `ECH`, cinq essais journalisés avec leur code HTTP (O-3).
1. **Machine** : outils, jetons par leur nom, carte visible (`nvidia-smi`).
2. **Code** : clone partiel de la seule branche `main`, extraction partielle (motifs fixes, registres nommés, chemins cités par la
   configuration ; `diag/*/lecture-sondes-t06.json*` exclu ; ni `docs/notes/bras-attaque/` ni `registres/index-bras-attaque*`),
   commit S7 ; gardes : tête = S7, C7 ancêtre, `git diff --quiet C7 S7 -- src tests`, S7 ancêtre de `main`.
3. **Registres nommés de `main`** (O-5 : `scellements-v1.md`, `scellements-v1.md.ouvertures.md`, `ouvertures-p3bis-v1.md`,
   `prealables-p3bis-v1.md`, `go.md`) et **fichiers qu'ils citent** avec leurs compagnons (hors du run de 7b ; un fichier suivi à
   S7 hors de l'extraction partielle y est d'abord ajouté) ; chemin interdit cité → arrêt ; **périmètre** (C-1) : chaque ligne de
   jeux et la ligne des concepts au plus une fois, présentes **exactement** comme `PERIMETRE` le dit (sinon arrêt, « rien n'est
   ouvert »), fichiers et compagnons présents, **journaux du script** du dossier de chaque jeu recopiés ; `src/` et `tests/`
   inchangés (contrôlé).
4. **Sortie de 7b**, par refspec explicite, fichiers nommés seulement (§ 2.1) ; `arret.json` de 7b recopié s'il existe (la garde
   le lit) ; fichiers cités par la configuration de 7b recopiés de `main`.
5. **Environnement** : `python3 -m venv`, `pip install -r requirements-gpu.txt` de S7 (borne 3 600 s) ; torch voit la carte.
6. **Essais figés** `tests/test_t07_*.py` (liste et empreintes dans les traces), **avant le modèle** (O-1) : code 0 **et**
   dernière ligne, durée retirée, égale à `ATT` ; sinon arrêt de code 2 (aucun modèle descendu, rien d'ouvert) ; `src/` et
   `tests/` non écrits par les essais (contrôlé).
7. **Taille des sorties de l'étape A** estimée et bornée **avant toute ouverture** (O-2, § 5 bis) : au-dessus de la borne →
   arrêt de code 2, nœud, rien d'ouvert ; estimation impossible → arrêt.
8. **Modèle** descendu au cache local (`precharger_modele`, révision figée du manifeste de 7b, `HF_TOKEN`) ; tout le reste lit
   hors ligne ; empreinte canonique de la configuration.
9. **`CODE-T07`** : `python -m controle_ia.t07.code_t07_v1 verifier . registres/scellements-v1.md` (commit cité ancêtre de la
   tête, fichiers du module importé égaux à la liste, tout `src/controle_ia/` égal au commit cité et arbre de travail propre,
   DF-02 ; `PYTHONDONTWRITEBYTECODE=1`) ; non conforme → arrêt ; le même contrôle est rejoué par la garde du repli, la passe à
   blanc et l'étape A.
10. **Branche neuve** (absente du distant, sinon arrêt R12) ; poussées par chemins explicites : **légers d'abord** (aucun fichier
    de plus de 90 000 000 octets dans l'index), puis chaque fichier plus lourd **découpé** (`split -b 50000000`, morceaux scellés,
    recomposition vérifiée contre le fichier et son compagnon, manifeste `<fichier>.morceaux.json` scellé, original déplacé hors
    du dépôt), poussé par lots de 10 morceaux (O-2).
11. **Repli** (`lecture_v2 repli-seul`, DF-01) : **garde d'ouverture de l'étape A d'abord** (journalisée ; refus → code 2, rien
    n'est calculé, l'instance s'arrête ; cette ouverture **ferme le périmètre des jeux**, C-1) ; puis recalcul **sous un nom
    daté**, identité à dose 0, rejeu en forçage, garde d'équivalence ; réussite → `activations/`, rapport scellé à côté ; code 3
    (R11) → **une** relance sous un nom daté neuf ; second échec → nœud ; poussée « garde, repli ».
12. **Passe à blanc** : `lecture_v2 passe-blanc` (`CODE-T07` d'abord ; mémoire de la notation jugée) ; sortie poussée quelle que
    soit son issue ; code ≠ 0 → arrêt, l'étape A ne part pas.
13. **Étape A** : `lecture_v2 etape-a-apres-repli` (rapport du repli relu et couvrant ; garde d'ouverture rejouée, `CODE-T07`
    comprise ; garde d'identité remplacée par la garde d'équivalence) ; sorties, registre (`SCORES-T07`, `SONDES-T07`) et journal
    des ouvertures poussés (légers, puis morceaux) ; code ≠ 0 → nœud, aucune relance sous ce texte ; `lecture-sondes-t06.json`
    absent de l'arbre (contrôlé) ; `FIN` ; « stopped » demandé ; la fille détruit.

## 5 bis. Taille des sorties de l'étape A (O-2), calcul fait par le script avant toute ouverture

Borne haute, nombres en `float64`, `np.savez` sans compression ; entrées lues sur l'instance sans rien ouvrir de décisif :
`n` = actions notées (`jetons_notes > 0` de `mesures-t06.npz` de 7b, sceau vérifié), `s` = octets des clés d'une action (`cle`,
`condition`, `tache`, `pas`), `d` = largeur des activations (en-tête du premier morceau du sous-ensemble de 7b, sceau vérifié),
`P` = `n_plancher`, `couches`, `L` = sondes lues au plus, `K` = concepts neufs appris (`JD`, `JC` du périmètre), `p6` = 1 si `JA`
et `JC` sont au périmètre, `C` = concepts des phrases (si `CONCEPTS` est au périmètre), `D` = `C × couches` :

- `F = L(1+P) + 8·couches + 5·couches·K + 2·p6·(1+P) + D(1+P) + K + 1` nombres par action ;
- `scores-actions-t07.npz` ≤ `n × (8F + s) + 5·10⁶` octets ;
- `sondes-neuves-t07.npz` ≤ `8 × [couches·K·(d²+d) + couches·K·(22d+64) + 2·p6·(d²+d) + (K+2·p6)·P·2d + D·d] + 5·10⁶` ;
- autres sorties : 5·10⁷ ; **total ≤ 2·10⁹ octets** (`BORNE`), sinon arrêt de code 2 avant toute ouverture (nœud) ;
- fichier de plus de 9·10⁷ octets (`SEUIL`) : morceaux de 5·10⁷ (`MORCEAU`), lots de 10 (`LOT`) ; nombre de morceaux prévu écrit
  dans `taille-estimee.json` (lisible par la fille, § 2.5).

Ordre de grandeur (non mesuré, pour juger la borne ; aucune donnée de 7b) : à `d` = 4 096, `couches` = 3, `P` = 200, `K` = 2,
`p6` = 1, la part des sondes neuves est d'environ 1,1·10⁹ octets, dominée par les matrices `d × d` ; la marge restante sous la
borne dépend de `n`, inconnu avant 7b. Un dépassement arrête l'instance après les paquets et les essais (≈ 0,3 à 1,2 h payées),
avant le modèle : § 13, S-6.

## 6. Devis de la variante B (A100, essais, recalcul des activations puis étape A) et dépense

| Phase | Attendu (h) | Pire cas (h) | Source |
|---|---|---|---|
| Création, démarrage, image | 0,10 | 0,30 | E2 (R-1689 : démarrage en file 17 min) |
| Clone partiel, registres, sortie de 7b | 0,10 | 0,45 | E2 (R-1687) ; borne du clonage de l'amorce de T0.6 (900 s) ; clone de la mesure : 104 Mo extraits (§ 11 bis) |
| Paquets (`requirements-gpu.txt`) | 0,15 | 0,50 | amorce de T0.6 (installation bornée à 3 600 s) ; **supposé** |
| Essais de T0.7 (17 fichiers) | 0,25 | 0,60 | **mesuré** : 716,0 s dans le clone de la mesure (§ 11 bis), machine partagée |
| Taille bornée | 0,01 | 0,05 | lecture de deux en-têtes |
| Modèle (≈ 16 Go) | 0,10 | 1,00 | `inet_down` ≥ 500 Mb/s : ≈ 0,07 h ; pire : débit dix fois plus bas |
| Repli : recalcul et garde d'équivalence | 0,10 | 0,40 | brouillon 19 : 576 épisodes × 0,45 s ≈ 0,07 h ; écriture de 31,5 Go ; une relance R11 au pire |
| Passe à blanc | 0,10 | 0,20 | estimation de la passe (échantillon) |
| Étape A | 2,00 à 3,50 | 4,00 à 7,00 | brouillon 19, « Calcul et dépense » ; pire : hôte deux fois plus lent |
| Poussées (légers, morceaux) | 0,10 | 0,40 | sorties ≤ 2 Go (borne du § 5 bis), lots de 500 Mo |
| **Total** | **3,0 à 4,5** | **7,9 à 10,9** | |

- **Coût** (≤ 1,30 USD de l'heure, carte et disque de 100 Go compris dans `dph_total`) : attendu **≈ 3,9 à 5,9 USD** ; pire cas
  ≈ 10,3 à 14,2 USD ; plus le téléchargement, borné à 24 Go × 0,05 USD = **1,20 USD**, et le disque après l'arrêt jusqu'à la
  destruction (≤ 0,08 USD de l'heure, ≤ 1 h). **Attendu ≈ 5,2 à 7,1 USD ; pire cas ≈ 11,6 à 15,5 USD.**
- **Plafond** : **20 USD sous GO-2026-11-10-04 et GO-2026-11-10-06 ensemble** (O-4 ; `PLAF`, ligne (A)) : la part disponible
  pour cette instance est `20 − ANT0` ; P8 exige qu'elle couvre le pire cas (`ANT0` ≤ 4,5 USD). La minuterie est bornée par
  `HMAX` (§ 4.4) : la carte ne peut pas dépasser `20 − ANT0 − 1,30` tant que le conteneur vit.
- **Relevé** : bloc du § 4.5 (`PRIX_H` = `prix_h` du § 4.3, `ANT0` sous les deux lignes) ; **compte rendu** à Lazar à 10 USD
  (aucun arrêt) ; **arrêt** dès que le cumul plus un quart d'heure de carte atteint `PLAF` : destruction par l'identifiant
  (§ 4.7), nœud, aucune relance sans un mot de Lazar sur un devis neuf. La facture, si connue, fait foi. Dépense inscrite sous
  `GO` (la mère vérifie la somme sous les deux lignes).

## 7. Arrêts

- Préalable manquant, empreinte différente, chemin interdit ou de 7a cité par un registre, `ATT` non valable pour S7 sans
  remesure, recherche vide, création incertaine : rien n'est créé (ou plus rien) ; compte rendu.
- Ligne `ARRET` du script : **code 2 avant la branche** (machine, code, registres, périmètre, sortie de 7b, environnement,
  **essais** — ligne différente de `ATT` : après les paquets, avant le modèle —, **taille au-dessus de la borne**, modèle,
  `CODE-T07`, branche présente) : rien d'ouvert, rien de poussé ; **code 3** (refus de la garde au repli, repli après relance,
  passe à blanc, découpage, étape A) : traces poussées si la branche existe. **CLC-08** : un repli en code 2 est journalisé
  « ligne manquante : attente » **quel que soit son motif** ; la fille lit d'abord la première ligne de
  `traces/t07-etape-a-b-v1/repli-<n>.err` sur la branche poussée (motif du refus, sans donnée décisive) ; une création neuve
  n'a lieu que sur un écrit de la mère (même GO, devis inchangé), quand la cause est levée. Dans tous les cas : la fille relève la
  ligne, vérifie ce qui est poussé (§ 4.6), **détruit** (§ 4.7), compte rendu, nœud de la mère.
- Plafond (§ 6), minuterie, refus d'un contrôle ou d'un classifieur : arrêt, compte rendu ; aucun contournement.

## 8. Compte rendu de la fille (nombres seuls, ≤ 400 mots)

`vastai --version` ; P1 à P12 (valeurs ; `PER` ; `ANT0` sous les deux lignes ; « ATT valable pour S7 ») ; recherche (offre, prix,
cuda) ; identifiant, `TC`, `HMAX`, `ECH` ; lignes `T07` (machine, code, registres, périmètre, sortie de 7b, **essais : code et
ligne**, **taille estimée : octets et morceaux prévus**, disque libre, modèle, configuration, `CODE-T07`, repli : actions et écart
maximal de la garde, passe à blanc : issue, frontière, mémoire, durée estimée, étape A : code et run, **morceaux poussés**, fin et
code HTTP de « stopped ») ; tête de la branche, commits, `OK` / `ÉCART` (fichiers légers et manifestes de morceaux) ; dépense
relevée ; destruction, inventaire final ; écarts. **Ni score, ni aire, ni contenu des sorties de l'étape A.** Journal (garde des
secrets à 0) envoyé à la mère.

## 9. Ce qui suit, et ce que cet ordre ne fait pas

- **Suite (mère)** : recopier **à l'octet**, dans le registre et le journal des ouvertures de `main`, les lignes `SCORES-T07`,
  `SONDES-T07` et `OUVERTURE-T07` écrites sur l'instance, après avoir vérifié que le journal de P3-bis de `main` ne porte aucune
  ligne datée avant la fin de l'étape A qui manquait à la copie de l'instance (sinon nœud ; G2, G4) ; inscrire la dépense et
  vérifier la somme sous GO-2026-11-10-04 et GO-2026-11-10-06 ; rappel daté à `ECH` levé.
- **Avant l'étape B** (son propre ordre) : pour chaque fichier découpé, recomposition par la commande écrite dans son manifeste
  (`cat <fichier>.morceau-[0-9][0-9][0-9] > <fichier> && sha256sum -c <fichier>.sha256`), chaque morceau à l'empreinte de son
  compagnon, empreinte du fichier recomposé égale à celle de la ligne `SCORES-T07` ou `SONDES-T07` (sans rien ouvrir d'autre) ;
  **C-4** : étape B jouée à S7 (tête détachée), `PYTHONDONTWRITEBYTECODE=1`, arbre propre (`CODE-T07` contrôlée aux deux étapes).
- **Ne fait pas** : aucun épisode ; aucune étape B ; aucune lecture de sortie ; aucune modification du code, du texte, de la
  configuration ou de la chaîne de T0.6 ; aucune fusion ; aucune écriture sur `main` ; aucun contact externe ni appel de modèle ;
  aucune H200.

## 10. À juger par la contre-lecture

1. La ligne `GO-LECTURE-T07` pour cette instance (variante B), dont l'extrait cite GO-2026-11-10-06 ; la borne `HMAX` de la
   minuterie (O-4) et l'exigence `ANT0` ≤ 4,5 USD (P8) contre le plafond commun de 20 USD.
2. `ATT` : mesurée sous Python 3.13.16 et le paquet local (§ 11 bis) ; l'instance joue Python 3.11 et `requirements-gpu.txt`
   (mêmes versions figées de `numpy`, `scipy`, `pytest`, `torch` en construction carte) ; conditions de validité de P12 ; risque
   résiduel § 13, S-2.
3. P10 : lecture stricte de la ligne d'arrêt corrigée (CLO-08) pour la variante B : **toute** instance `t06…` ou `t07…` bloque la
   création, celle de 7b comprise (« autre que celle de 7b » ne vaut que pour l'étape annexe sur l'instance de 7b, abandonnée).
4. P3 : la mère décide avant la création d'attendre ou non `SCELLEMENT-JEUX-T07-JC` et `SCELLEMENT-CONCEPTS-T07` ; la garde du
   repli ferme le périmètre avant tout recalcul (C-1).
5. Borne de taille (§ 5 bis) et seuils de découpage : proposés par le script, non confrontés à une sortie réelle.
6. Lecture des manifestes de morceaux (tailles, noms) par la fille, et du motif d'un `repli-<n>.err` (§ 2.5).
7. Seuil de compte rendu (10 USD) et marge d'un quart d'heure : proposés.

## 11. Répétitions du script de l'instance (mode jouet)

Le script v1 a été répété au brouillon 3 (`99e4c926…`, trois passages). Le **script v2** (`e68d3306…`) est répété par
`scripts/repetition_jouet_variante_b_t07_v2.py` (rapport complémentaire 5, § 5, passage 4, 12:08 à 12:17 UTC, commit `16f59d63` :
**douze verdicts conformes** — normal (`PERIMETRE=JD,JA,JC,CONCEPTS`) code 0 ; « sans concepts » (`PERIMETRE=JD,JA,JC`, ligne
absente de `main`) code 0, phrases non lues ; branche déjà poussée → code 2 ; périmètre faux → code 2 avant tout repli ; mesure
« 20 passed » ; découpage O-2 en morceaux scellés, recomposition égale ; minuterie saine (« HTTP 200 ») et en échec (cinq
« HTTP 500 », destruction laissée à la session)) ; **rejoué** par la contre-lecture courte de l'option (c) (`7a327462…`, § 2 :
12 verdicts conformes ; artefact du contre-lecteur : script sans `registres/go.md` → refus de la garde du repli). Non répétés
(réel seulement) : Vast, paquets, modèle, carte, `DELETE` avec la clé de l'instance. **Pas de répétition neuve dans ce
brouillon** (la consigne ne la demande pas ; le script est inchangé).

## 11 bis. Mesure de `ATT` dans un clone fait comme celui de l'instance (O-1)

- **Quand, où** : le 2026-11-10, de 15:17:26 (clone) à 15:29:36 (fin des essais) UTC (`date -u`), dans le bac à sable du sous-agent, après la partie 1 de la
  consigne (essai GARDES-CODE-01 commité et poussé), **sur la branche `prep/t07-essai-degeneres-v1`**, tête
  `2c8ab779ca6df361d562e120ba34045be675853a` (partie de `06deda58` de `main` ; seul ajout : `tests/test_t07_tirages_degeneres_v1.py`).
- **Méthode** : script de mesure du sous-agent (bac à sable, non versé ; empreinte `98beca19097036d64fbec4f6779183f0e899afe9c21f6ba755164b6324b3aec1`), qui recopie **les étapes 2,
  3 et 6 du script v2** : `git clone -q --filter=blob:none --no-checkout --single-branch --branch <branche> https://github.com/lciric/controle-ia-travail.git`
  (clone partiel à branche unique : seuls les objets atteignables depuis la branche) ; mêmes motifs d'extraction partielle,
  mêmes registres nommés, mêmes chemins cités par la configuration (v4 : `diag/20261019-230011-p3-reel/sondes-figees.json`, `donnees/20261007-082440-t05-extraction/taches-entrainement.json`, `donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz`, `donnees/T0.7-faits-repe-v1/facts_true_false.csv`, `donnees/T0.7-models-under-pressure-v1/training/train.jsonl`, `runs/20261019-230011-p3-reel/manifeste.json`) ; tête au commit mesuré ; registres
  recopiés et fichiers qu'ils citent (`donnees/t07-jeux-synthetiques-v2/dissimulation-v2.jsonl`, `…/intention-autres-modes-v2.jsonl`,
  `prereg/T0.8-base-A-mots-et-cout-v1.md`) ; périmètre `JD,JA` (journaux du script : un par jeu, recopiés) ; puis, depuis le
  dépôt, `TZ=UTC PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python -m pytest -q -rsxX -p no:cacheprovider --color=no tests/test_t07_*.py --basetemp=<bac>/essais-tmp -o tmp_path_retention_policy=failed`,
  dernière ligne, durée retirée (`sed -E 's/ in [0-9.]+s.*$//'`).
- **Écarts à l'instance, déclarés** : branche mesurée au lieu de `main` (S7 = C7 = H = sa tête ; même atteignabilité que `main` à
  `06deda58`, plus l'essai) ; étape 4 (sortie de 7b) et étape 5 (paquets) non jouées (aucune course 7b ; interpréteur local
  **Python 3.13.16**, `numpy` 2.4.6, `scipy` 1.17.1, `pytest` 9.1.1, `torch` 2.14.1 en construction processeur, contre Python 3.11
  et `requirements-gpu.txt` sur l'instance) ; aucun jeton posé (le mandataire de la session porte l'accès) ; registres de `main` à
  `06deda58` (les lignes inscrites plus tard ajoutent des fichiers cités ; aucun essai de T0.7 ne lit le registre de `main`).
- **Résultat** : code 0, **`ATT` = `346 passed, 2 skipped, 4 xfailed`** (17 fichiers ; durée 716,0 s). Sauts et échecs attendus, nommés :
  - sautés (2) : `tests/test_t07_lecture_v1.py:504` (branche `origin/prep/t06-candidat8-v1` non récupérée, déclaré) ;
    `tests/test_t07_lecture_v2.py:911` (commit `061ac380` absent du clone, déclaré) — les deux tiennent au clone à branche unique,
    comme sur l'instance (O-1) ;
  - échecs attendus (4) : `test_CT01_action_sans_caractere_de_mot_temoin_en_echec_sans_arret` et
    `test_CT11_dates_du_journal_non_decroissantes` (`tests/test_t07_corrections_cl1_v1.py`),
    `test_journal_cas_sain_lignes_et_refus_lus` (`tests/test_t07_lecture_v2.py`), `test_garde_refusee_rien_calcule_puis_relance`
    (`tests/test_t07_repli_etapes_v1.py`) ;
  - **l'essai du miroir de `familles_v2` passe** (`8cb539f9` atteignable depuis la branche, donc depuis `main` à `06deda58` :
    fusion « ours », R-2229 ; CLC-03 levé) ; les essais du repli passent (`docs/sources/invites-2606.08892-v1/` extrait) ;
  - compte recoupé : 344 essais dans les quinze fichiers de `37485ce5` (CLO-04), plus 3 de l'essai CLC-04 et 5 de l'essai
    GARDES-CODE-01 = 352 = 346 + 2 + 4 ; aucun avertissement dans la ligne ; `essais.err` vide ; `src/` et `tests/` non écrits ;
  - pièces (bac à sable, non versées, empreintes relevées avant suppression) : `essais.txt` `2b506a189c696b4f4aad86cdc26a7fc2e36c3b95863c3916831ac351c83947b1`,
    `essais-liste.txt` (17 fichiers et leurs empreintes) `bd49a36795b15228a9cfde88b411b98ae842223e35fbb75e57eebe04dcb26415`,
    journal de la mesure `d15f94b8622c3d4c3bce542738329810f2ad001e91104975bdbd493192cb7a6b`.
- **Commande de remesure** (si P12 échoue) : la même, avec `--branch main` et la tête au commit S7 (méthode exacte du script :
  `ESSAI_LOCAL=1 ARRET_APRES_ESSAIS=1` ne peut pas tourner sans course 7b ni dépôt local dont `main` porte S7), soit, depuis un
  dossier neuf : `git clone -q --filter=blob:none --no-checkout --single-branch --branch main https://github.com/lciric/controle-ia-travail.git d && git -C d sparse-checkout init --no-cone`,
  motifs de l'étape 2 du script v2 (l. 102-131 : `REGISTRES`, `MOTIFS`, `NOMMES`, `CITES` tirés de `CFG` à S7) passés à
  `git -C d sparse-checkout set --no-cone --stdin` (l. 132), `git -C d checkout -q <S7>`, recopie des registres nommés et des fichiers
  qu'ils citent, journaux du script des jeux (étape 3, l. 141-166, hors chemins de 7a), puis la commande pytest ci-dessus depuis `d`.

## 12. Marqueurs (à remplir par la mère ; une occurrence chacun)

Remplis à ce brouillon : `GO_VARIANTE_B_T07` = **GO-2026-11-10-06** (R-2115) ; le plafond, **20 USD**, est celui de cette ligne,
commun avec GO-2026-11-10-04 (`PLAF`) ; **`LIGNE_ESSAIS_T07`** = `ATT` mesurée (§ 11 bis), valable sous P12.

| Marqueur (sans chevrons) | Où | Valeur |
|---|---|---|
| `ID_SESSION_FILLE` | en-tête | identifiant de la session fille |
| `EMPREINTE_CONFIG_T07` | § 1 | empreinte canonique de la configuration de T0.7 scellée |
| `LIGNE_SCELLEMENT_T07` | § 3 | la ligne `SCELLEMENT-T07` exacte |
| `DEPENSE_ANTERIEURE_USD` | ligne (A) | dépense déjà inscrite sous GO-2026-11-10-04 **et** GO-2026-11-10-06 (attendu `0`) |
| `RUN_T06_7B` | ligne (A) | run de 7b |
| `BRANCHE_7B` | ligne (A) | branche poussée par 7b (`calcul/t06-confirmation-7b-v1`, ou suivante) |
| `COMMIT_CODE_T07` | ligne (A) | C7 (R-2231) |
| `COMMIT_SCELLEMENT_T07` | ligne (A) | S7 |
| `CHEMIN_CONFIG_T07` | ligne (A) | chemin de la configuration scellée dans S7 |
| `PERIMETRE_T07` | ligne (A) | lignes de jeux et de concepts présentes à `main` à la création (`JD,JA` à l'écriture de cet ordre), ou `aucun` |

## 13. Constats sur le script v2 (non modifié ; correction proposée pour une v3, décision de la mère)

| id | gravité | constat | correction proposée (v3, décision de la mère) | ce que fait cet ordre en attendant |
|---|---|---|---|---|
| S-1 | à corriger si l'environnement change | L'étape 6 compare **toute** la dernière ligne de `pytest` (durée seule retirée) à `ATT` : un compte d'avertissements (« , 1 warning ») ou d'erreurs de collecte change la ligne sans changer les essais ; l'arrêt tombe après les paquets (≈ 0,2 à 0,7 h payées, ≤ 1 USD), avant le modèle. La mesure (Python 3.13) n'en a aucun. | retirer `, N warning(s)` avant la comparaison, ou comparer en plus la liste triée des essais non passés (`essais-sauts.txt`) à une liste scellée | `ATT` mesurée sans avertissement ; P12 ; écart → compte rendu, remesure, création neuve sur écrit de la mère |
| S-2 | risque résiduel | Mesure sous Python 3.13.16 (bac à sable) ; l'instance joue Python 3.11 (image `python:3.11-bookworm`) et `requirements-gpu.txt` (mêmes versions figées, `torch` en construction carte). `python3.11` existe sur la machine de la session, sans `torch` : une mesure sous 3.11 demanderait d'y installer `torch` (≈ 1 Go ; disque serré). | la mère peut remesurer sous 3.11 avec la commande du § 11 bis, ou accepter le risque | déclaré (§ 10.2) |
| S-3 | à corriger | `interdit()` (l. 141) ne refuse pas un chemin de 7a (`20261109-070232-t06-reel`) cité par un registre ; aucun registre n'en cite aujourd'hui (trois lignes au commit `2c8ab779`). | ajouter `*20261109-070232-t06-reel*` au motif de `interdit()` | § 4.1 : compte des chemins interdits ou de 7a cités par un registre, `0` exigé avant la création |
| S-4 | mineur (CLC-08) | l. 362 : un repli en code 2 est journalisé « refus de la garde (ligne manquante : attente …) » quel que soit son motif. | libellé neutre : « refus de la garde (motif : repli-<n>.err) », ou première ligne du motif | § 7 : la fille lit le motif dans `repli-<n>.err` |
| S-5 | hors du script (concordance) | La ligne d'arrêt corrigée (CLO-08) et le filtre du § 4.2 ne regardent que les étiquettes `t06…` et `t07…` : une instance d'une autre tâche du programme **étiquetée** `t06…` ou `t07…` bloquerait la création (P10), à tort selon les écrits (b) 1 et 2. | aux rédacteurs des ordres de P3-bis, de T0.8 et du texte de validité : étiquettes hors de ces deux préfixes | P10 ; point ouvert pour la mère |
| S-6 | mineur | La borne de taille (étape 7) se calcule après les paquets et les essais ; un dépassement arrête après ≈ 0,3 à 1,2 h payées. La part des sondes neuves (matrices `d × d`) est d'environ 1,1·10⁹ octets à `d` = 4 096, `K` = 2, `p6` = 1 (§ 5 bis) : la marge sous 2·10⁹ dépend de `n`, inconnu avant 7b. | estimer avant l'étape 5 (un `pip install numpy==2.4.6` suffit à la lecture des deux en-têtes) ; ou relever la borne après un calcul de la mère sur les nombres de 7b | § 5 bis ; § 7 (code 2 avant le modèle) |
| S-7 | cosmétique | `essais-sauts.txt` porte deux fois certaines lignes `XFAIL` (résumé court de `-rsxX` et lignes de résultat). | sans effet sur la comparaison | rien |

Sources : `scripts/etape_a_t07_variante_b_v2.sh` (`e68d3306…`, lu en entier) ; ordre brouillon 3 (`b053a220…`) ; contre-lecture
courte v3 (`d0fe9053…`) ; rapport complémentaire 5 (`e58be6c9…`) ; contre-lecture courte de l'option (c) (`7a327462…`) ;
contre-lecture orchestrée du brouillon 22 (`47537dfa…`) ; brouillon 22 de T0.7 (`brouillons/T0.7-sondes-v0-v1-brouillon22.md`,
lu pour la liste d'arrêt l. 1897-1900 et le module l. 2427-2438 ; brouillon, non opposable : le texte qui fait foi est celui de la
ligne `SCELLEMENT-T07`) ; `registres/go.md` de `main` (GO-2026-11-10-04, GO-2026-11-10-06) ; `registres/decisions.md` de `main`
(R-2112, R-2115, R-2153, R-2220, R-2229, R-2231, R-2241, R-2246, R-2249) ; `registres/scellements-v1.md` au commit `2c8ab779`
(trois lignes : `SCELLEMENT-JEUX-T07-JD`, `SCELLEMENT-JEUX-T07-JA`, `SCELLEMENT-T08-BASE-A`).
