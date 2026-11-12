# Fiche de réception de la relance v4 de R1 (témoin, réparation, table v4, rejeu) — v1

- **Ce document** : la fiche de réception v4 de conv-audit, exigée par l'addendum v4 scellé
  (`prereg/R1-addendum-relance-v4.md`, `0f10881b32fa4c0e5ec1eb02cf88fbd0fcb6ad13f70b59abc2d84e45a99f61c8`, branche
  `prep/r1-relance-v4`, commit de scellement `937f13177892933955c9c34839b4b45a4db745df`, versement du témoin
  `5bd62a004279776c2718b3201c11001e16fa6527`) : étape 4 (« Attentes de réception », « Recalcul de réception »), écarts
  V4-E5, V4-E11, V4-E13, V4-E14, « Critères de lecture gelés », « Liste d'arrêt ». Version neuve (R12) ; modèle : la
  fiche v3 (`fiche-reception-r1-relance-v3-v1.md`, commit `cbad0b27`), qui n'est pas modifiée.
- **Écrite par** un rédacteur-développeur neuf (sous-agent, Claude Opus 5.5) pour conv-audit, consigne
  `docs/notes/runs-r1-r2-r4-v1/consigne-fiche-reception-r1-v4-v1.md` ; le 4 novembre 2026 vers 23:50 UTC (`date -u`).
  Je n'ai écrit ni l'addendum v4, ni son code, ni les fiches précédentes.
- **Statut : non scellée.** La session conv-audit la fait contre-lire, la scelle (`python -m controle_ia.scellement
  sceller`), la commite, la pousse, puis donne au canal son chemin et son empreinte ; **rien n'est récupéré avant**
  (V4-E13 ; condition de la récupération, non de la création).
- **Vérificateur mécanique** : `verifier_reception_r1_v4_v1.py` (même dossier ; bibliothèque standard, `python3 -I`) ; son
  bloc d'attendus (section 9) est la sortie exacte de `python3 -I verifier_reception_r1_v4_v1.py bloc` ; en mode réel il
  refuse une fiche dont le bloc diffère de ses constantes. Essais et banc : `rapport-fiche-reception-r1-v4-v1.md`.
- **Constat à l'écriture** : le témoin `20261104-091009-r1-v4-temoin-reel` est versé au commit `5bd62a00` (quatre
  fichiers : seuls leurs noms et empreintes ont été relevés, aucun contenu lu) ; la session 2 tourne (instance 59175807,
  créée à 23:19:50 UTC) ; **aucune sortie de `calcul/r1-v4-reparation-reel-v1` n'a été lue**, rien sous `donnees/`.

## 1. Ordre de la réception (aucune étape sautée, aucune inversée)

| étape | qui | quoi | condition pour passer |
|---|---|---|---|
| A | conv-audit | fiche contre-lue (R2), **scellée**, poussée ; chemin et empreinte au canal | compagnon égal |
| B | session-depot | **récupération à l'octet** : `git fetch` de la seule branche source ; commit de versement **préparé localement, non poussé**, sur la tête de `calcul/r1-r2-reel-v1`, qui ajoute exactement les 198 chemins de la section 3, recopiés par `git show <source>:<chemin>` (témoin : `git show 5bd62a00:<chemin>`) | la fiche scellée et son empreinte reçues et vérifiées |
| C | session-depot | **contrôles** : recalcul de réception (section 7), puis `verifier_reception_r1_v4_v1.py verifier` (section 8) sur ce commit local | sortie « RÉCEPTION CONFORME », code 0 |
| D | session-depot | **versement** : poussée de ce même commit (même identifiant) sur `calcul/r1-r2-reel-v1`, en avance rapide, sans réécriture ; message de versement : identifiant du commit, branche source et sa tête, noms des deux runs, empreinte de la fiche | poussée acceptée |
| E | conv-audit | récupération par la seule refspec `+refs/heads/calcul/r1-r2-reel-v1:refs/remotes/origin/calcul/r1-r2-reel-v1` ; **même vérificateur rejoué** (même recalcul) sur le commit nommé | code 0 et identifiant égal à celui du message |
| F | lecteur neuf (R13) | **seulement ensuite**, lecture selon les critères gelés (parent, v3, addendum v4) et les trois analyses scellées de conv-audit, dont les gardes sont mises à jour de leur côté (section 6) | — |

Code 2 (« ARRÊT [garde] ») ou 3 (« COURSE ARRÊTÉE ») à C ou E : rien n'est versé ni lu, rien n'est corrigé à la main,
Lazar est prévenu (section 5).

## 2. Textes qui encadrent la réception (au commit `5bd62a00`, garde `textes`)

Le commit `5bd62a00` a pour seul parent `937f1317` et n'en diffère que par les quatre fichiers du témoin ; la table v4
n'y est pas (R12).

| pièce | chemin | sha256 du fichier | compagnon au même commit |
|---|---|---|---|
| addendum v4 (texte qui gouverne) | `prereg/R1-addendum-relance-v4.md` | `0f10881b32fa4c0e5ec1eb02cf88fbd0fcb6ad13f70b59abc2d84e45a99f61c8` | égal |
| configuration de la réparation v2 | `prereg/R1-reparation-v4-config-v2.json` | `4d0655d1bac5b15d6cb604e5853bed0bfe1eb48d6235772e39b86a698b8d85e5` (canonique `c34bf464177468d160975800da3cfe13d67e722a2e3b3c3e4c3c46d503ab680a`) | égal |
| configuration du rejeu v6 | `prereg/R1-rejeu-config-v6.json` | `a9ebc6b0cd6c99e118ade7b304472b5452d2b43c63cc222d1adccd2ee4e95e75` (canonique `a3ef1bac5b8768604f2418da8b55c7adc8954f247485ea12c587bd00f407575f`) | égal |
| table de tokenisation v3 (22 entrées) | `prereg/R1-table-tokenisation-v3.json` | `ead8a66851b2af5dfa02635297056872032878fbd2987ba780fb6c9096766423` | égal |
| parent | `prereg/R1-R2-rejeu-p3-v1.md` | `80c85a0085f444dc10f36e4e226d015802d2e20294c4fff2ae67adb0aca4ddea` | égal |
| garde de chaîne | `src/controle_ia/runs_nuit/chaine_table_v4_v1.py` | `a015e89fd1cf39d887a05617298b7c930c939f60449b2c0ed9e75975d097bdd1` | égal |
| rejeu v4 | `src/controle_ia/runs_nuit/rejeu_activations_v4.py` | `d31dcec074b513b597a4920a5c6501326ee18c8cefe4bbd83d381f4ac4b25a08` | égal |
| lot fidèle v3 (témoin, réparation, table v4) | `src/controle_ia/runs_nuit/resolution_graine_lot_v3.py` | `9ce6d17818a04853db57fdbb70e347bc9fdd0153ba91c14b9530818c6b29f6e3` | égal |
| lot fidèle v2 (`charger_table_v4`) | `src/controle_ia/runs_nuit/resolution_graine_lot_v2.py` | `501ab45308f2ffe5e3cf25b0352b0d2e7f8bca0bb2ba7cd897c3b2c39b704f87` | égal |
| lot fidèle v1 (importé) | `src/controle_ia/runs_nuit/resolution_graine_lot_v1.py` | `5a9982b2a2248d5312c5a42bf34ac90c505ca579052985169aabb7e16c8c7156` | égal |
| résolution à graine v1 (importée) | `src/controle_ia/runs_nuit/resolution_graine_v1.py` | `cdc22b5ad2659f82f512c39545c52fc826a6be2dc60fb3aeafda0c5d014a9663` | égal |
| manifeste | `src/controle_ia/manifeste.py` | `1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d` | sans compagnon (déclaré) |
| scellement | `src/controle_ia/scellement.py` | `93beeb1c8aae75463afc98e76ffb330b1e4f26be9c08ae8fee539a2df6a94ef2` | sans compagnon (déclaré) |
| script d'instance v2 | `scripts/r1_v4_instance_v2.sh` | `a02eda0c4c8519a1d7d3ddd452001a7b8357c7e6925ca1e9c28be703d362b5ae` | égal |
| amorce v2 | `scripts/amorce_instance_r1_v4_v2.sh` | `22e64d72745168f947a37690e9bb29170011ef38f0649b6bbc7ca6f8825445b1` | égal |

Toutes ces empreintes égalent celles de l'en-tête de l'addendum v4 (recalculées le 4 novembre par `git show
5bd62a00:<chemin> | sha256sum`, et par l'essai `test_mode_reel_textes_scelles_reels`).

## 3. Ce qui est versé (garde `versement`, `octets`, `presence`, `compagnon`)

Runs : témoin `T` = `20261104-091009-r1-v4-temoin-reel` ; réparation `R` de la forme `AAAAMMJJ-HHMMSS-r1-v4-reparation-reel`
; rejeu `J` de la forme `AAAAMMJJ-HHMMSS-r1-v4-rejeu-reel` (noms du script d'instance v2, `MODE=reel`), nommés par le
message de versement. Branche source : `calcul/r1-v4-reparation-reel-v1` (`-v2` seulement après une reprise V4-E16
déclarée avant la création ; une reprise dont la course arrêtée a écrit un manifeste relève d'un texte neuf : nœud).

Le commit de versement a **un seul parent** (la tête précédente de `calcul/r1-r2-reel-v1`) et **ajoute exactement ces
198 chemins** (statut « A » seulement ; rien de modifié ni de supprimé ; rien sous `traces/`) :

| groupe | chemins (chacun avec son compagnon `.sha256`) | nombre |
|---|---|---|
| témoin | `runs/T/manifeste.json`, `diag/T/resolution-graine-lot-v3-temoin.json` — **blobs égaux à ceux de `5bd62a00`**, empreintes `43e2dd5c605fc87f7aacd319ae258bbfd72a1dc27fcf6e7c3b5f6f3cc4e9ac01` et `25d68f3335867e7222c1a6f24d024edff14a6141947d5e618696e8be88145dd2` (compagnons `d03f7bf13257554ed8b560e82f28e8a43bb9747997b205d01f1f8a76cc3f9ff4`, `23b4473468a806d889aa4e2aa9b73ff0beabe115b2eefdf4be87bd6465cc49c2`) | 4 |
| réparation | `runs/R/manifeste.json`, `diag/R/resolution-graine-lot-v3-reparation.json`, `diag/R/episodes-reparation/000.json` … `088.json` (un par cible) | 182 |
| table v4 | `prereg/R1-table-tokenisation-v4.json` | 2 |
| rejeu | `runs/J/manifeste.json`, `diag/J/rejeu-activations.json`, `donnees/J/activations-p3-rejeu-v1.npz`, `donnees/J/activations-p3-rejeu-v1-maximum.npz`, `donnees/J/activations-p3-rejeu-v1-complement-hors-cout.npz` | 10 |

Hors témoin, chaque blob versé égale le blob de la tête de la branche source (à l'octet) ; l'arbre de travail reçu
égale le commit de versement ; dans les dossiers des trois runs (`runs/`, `diag/`, `donnees/`), aucun fichier en plus
ni en moins (pas d'`arret.json` dans une course qui va au bout) ; chaque compagnon a une ligne « `<hex>  <nom>` » égale
à l'empreinte du fichier. Un `.npz` de plus de 99 Mo est laissé sur l'instance par le script : il manquerait, la
réception s'arrête (nœud).

## 4. Attentes par pièce (toutes vérifiées par le script ; tout écart arrête)

### 4.1 Témoin (garde `temoin`)

| clé | attendu |
|---|---|
| manifeste `run_id`, `commande` | `T` ; `python -m controle_ia.runs_nuit.resolution_graine_lot_v3 --etape temoin` |
| `preenregistrement` | `{"chemin": "prereg/R1-addendum-relance-v4.md", "sha256": "0f10881b…61c8"}` |
| `config_sha256` | `c34bf464…680a`, égal au recalcul canonique de `config`, et `config` égal au fichier scellé |
| `commit` | `937f13177892933955c9c34839b4b45a4db745df` (commit de scellement, session 1) |
| `decisif`, `depot_propre`, `reserves` | `true`, `true`, `[]` |
| `graines.aucun-tirage-propre.entropie` | `36410133060804533274328900142752730279` |
| résultat : `run_id`, `manifeste_sha256` ; `resultat.etape`, `resultat.version` | `T`, empreinte du manifeste ; `temoin`, `resolution_graine_lot_v3` (seules clés lues ; la lecture du témoin n'est pas lue) |

### 4.2 Réparation (garde `reparation`)

| clé | attendu |
|---|---|
| manifeste | comme 4.1, sauf `run_id` = `R`, `commande` = `… resolution_graine_lot_v3 --etape reparation`, `commit` = `5bd62a004279776c2718b3201c11001e16fa6527` (commit du versement du témoin, session 2) |
| rattachement | `run_id` = `R`, `manifeste_sha256` = empreinte du manifeste |
| `resultat.etape`, `.version`, `.voie` | `reparation`, `resolution_graine_lot_v3`, `lot_fidele` |
| `resultat.temoin` | `chemin` = `diag/T/resolution-graine-lot-v3-temoin.json`, `sha256` = `25d68f33…5dd2`, `voie` = `lot_fidele` |
| `resultat.table_v3_sha256`, `.run_source` | `ead8a668…6423`, `20261019-230011-p3-reel` |
| `resultat.cibles`, `.lots_a_cible` | 89 distinctes, 28 lots |
| `resultat.episodes` | les 89 cibles dans l'ordre, chacune avec `empreinte_retrouvee` booléen |
| `resultat.episodes_consignes` | `episodes-reparation/000.json` … `088.json` dans l'ordre, chaque `sha256` = empreinte du fichier versé |

### 4.3 Table v4 `prereg/R1-table-tokenisation-v4.json` (gardes `table`, `chaine-locale`)

| attente | règle |
|---|---|
| sérialisation | octets = `json.dumps(table, sort_keys=True, ensure_ascii=False, indent=1) + "\n"` (`ecrire_table_v4`) |
| clés | celles de la table v3 hors `version`, `comptes`, `episodes`, reprises à l'identique, plus `version`, `regle_v4`, `table_v3_sha256`, `resultat_reparation_sha256`, `voie`, `temoin`, `comptes`, `corrections_verifiees`, `non_resolus_v4`, `episodes` |
| `version`, `table_v3_sha256`, `voie` | `4`, `ead8a668…6423`, `lot_fidele` |
| `resultat_reparation_sha256` | sceau du résultat de la réparation versé |
| `temoin` | `chemin` et `sha256` du témoin versé |
| `episodes` | les 22 entrées de la table v3, à l'identique et en tête, puis une entrée par cible, dans l'ordre des cibles, de méthode `identifiants` ou `non_resolu` |
| `non_resolus_v4` | exactement les entrées neuves `non_resolu`, dans l'ordre |
| `comptes` | recalculés depuis les entrées (règle de `construire_table_v4`) : ceux de la v3 hors méthodes, chaque méthode recomptée, `identiques_apres_table` = `identiques_base` + corrigées, `non_conformes` = `cibles_v4` = 89, `retrouvees_v4` = entrées neuves `identifiants` ; `episodes` 240, `identiques_base` 129, `signales` 22 |
| `corrections_verifiees` | `identiques_apres_table` − `identiques_base` |
| chaîne locale (V4-E5, sans tokeniseur) | entrées `identifiants` = exactement les épisodes `empreinte_retrouvee` vrai de la réparation ; chacune cite `resolution_graine.resultat_sha256` = sceau du résultat |

### 4.4 Rejeu (gardes `rejeu`, `commit-rejeu`, `rattachement`, `verdict`, `table-comparee`, `provenance`, `comptes`, `coherence-table`, `fichiers`)

| clé | attendu |
|---|---|
| manifeste `run_id`, `commande` | `J` ; `python -m controle_ia.runs_nuit.rejeu_activations_v4` |
| `preenregistrement`, `decisif`, `depot_propre`, `reserves` | comme 4.1 |
| `config_sha256`, `config` | `a3ef1bac…575f`, recalcul canonique égal, `config` égal au fichier scellé ; `chemin_table_tokenisation` = `prereg/R1-table-tokenisation-v4.json`, `table_tokenisation_sha256` = `construite-en-session` |
| `graines.fidelite.entropie` | `36410133060804533274328900142752730279` |
| `commit` (commit lancé) | présent au dépôt (branche source récupérée), descendant de `5bd62a00`, qui n'en diffère que par les 182 chemins de la réparation et les 2 de la table v4, **blobs égaux aux versés** (la table du rejeu est la table versée) |
| rattachement | `run_id` = `J`, `manifeste_sha256` = empreinte du manifeste |
| `resultat.verdict_fidelite` | `conforme` |
| `resultat.tokenisation.table_sha256` | sceau de la table v4 versée, **et** la table cite le sceau du résultat de la réparation versé (garde `table-comparee`) |
| `resultat.tokenisation.addendum` | `prereg/R1-addendum-relance-v4.md` à l'identique (V4-E14 ; garde `provenance`) |
| `tokenisation.version_table`, `.table_empreinte_citee` | `4`, `false` |
| `tokenisation.non_conformes`, `.signales`, `.trajectoires_identiques_base`, `.seuil_non_conformes` | `89`, `22`, `129`, `10` |
| `empreintes_p3.episodes`, `fidelite_toutes.actions` | `240`, `2400` |
| `tokenisation.episodes_non_resolus`, `.actions_non_resolues`, `.fideles_parmi_non_resolues` | `[]`, `0`, `0` (règle B : aucun signalé non résolu dans la table v3) |
| cohérence avec la table versée (comparée, **jamais affichée**) | `corrections_verifiees_au_chargement` = `corrections_verifiees` de la table ; `empreintes_p3.trajectoires_identiques` = `comptes.identiques_apres_table` ; `corrections_par_methode` = comptes de la table pour les 14 méthodes corrigées ; `par_methode_resolution` = {v1 15, v2 3, identifiants = `comptes.identifiants`, aucune = 240 − 18 − identifiants} ; `methodes_resolution` : 240 épisodes, méthode de table égale à la table, aucune hors table ; `episodes_non_retrouves_v4` = `non_resolus_v4` (ensemble), `actions_non_retrouvees_v4` = 10 × leur nombre |
| `resultat.fichiers` | les trois noms `.npz`, empreintes égales aux fichiers versés |

### 4.5 Fichiers `.npz` (garde `npz` ; en-têtes `.npy` seulement, aucun tableau chargé)

Dans chacun des trois fichiers, exactement 14 tableaux, aucun en ordre Fortran :

| fichier | tableau principal |
|---|---|
| `activations-p3-rejeu-v1.npz` | `moyenne` (2400, 3, 4096) `<f2` |
| `activations-p3-rejeu-v1-maximum.npz` | `maximum` (2400, 3, 4096) `<f2` |
| `activations-p3-rejeu-v1-complement-hors-cout.npz` | `maximum_hors_cout` (2400, 3, 4096) `<f2` |

Communs (parent, plan d'analyse, 1 ; `rejeu_activations_v4`, écriture) : `jetons_empan`, `jetons_empan_rejeu`
(2400,) `<i8` ; `couches` (3,) `<i8` ; `conforme_longueur`, `contexte_conforme`, `fidele`, `trajectoire_identique`,
`activations_identiques` (2400,) `|b1` ; `ecart_fidelite` (2400,) `<f8` ; identité `episode`, `pas`, `condition`,
`tache` (2400,) au type et à la forme des mêmes tableaux de `donnees/20261019-230011-p3-reel/scores-p3.npz`
(`968414fc7ce7db935c2c4a390a13e2eceebe2fd722628cccb52caf27128004cf`, empreinte vérifiée, en-têtes seulement). L'égalité
des **valeurs** d'identité à P3 reste vérifiée par les lecteurs de nos analyses, non par cette réception.

## 5. Ce qui arrête la réception

- **Code 2, « ARRÊT [garde] : … »** : toute attente des sections 2 à 4 et 7 non tenue, toute pièce illisible ; rien
  n'est versé (étape C) ou lu (étape E) ; écart à un texte scellé ou autre course : **nœud**, Lazar prévenu ; une
  fiche scellée ne se réécrit pas (version nouvelle, nom nouveau).
- **Code 3, « COURSE ARRÊTÉE »** (réception de l'arrêt seulement) : `diag/R/arret.json` (réparation arrêtée : ni table
  ni rejeu attendus), ou rejeu absent (étape « table-v4 » ou « chaine » arrêtée : `--run-rejeu` omis), ou
  `diag/J/arret.json` (rejeu arrêté, aucun `donnees/J`) ; sont vérifiés le versement (chemins dans les runs attendus,
  rien sous `traces/`), les octets, les compagnons, le témoin, les manifestes et le rattachement de l'arrêt ; du seul
  `arret.json` du rejeu, `resultat.verdict_fidelite` est lu, dans la liste fermée « non conforme », « echec » (« Table
  v4 non applicable » → « echec » : rien n'est lu) ; le reste d'`arret.json` (`partiel`, motif) n'est pas lu ; nœud
  porté à Lazar (critères gelés, « Liste d'arrêt »).
- Recalcul (section 7) en code non nul, ou sortie sans `recalcul_egal_a_l_octet` vrai : **la table n'est pas reçue**
  (étape 4) ; code 2.

## 6. Non lu avant les analyses ; gardes des analyses

- Jamais gardées, écrites ni affichées par le script (filtre dès le chargement) : `fideles`, `notees`,
  `fideles_parmi_contextes_conformes`, `notees_contextes_conformes`, `egalite_exacte`, `ecart_max`, `ecart_mediane`,
  `part_fideles_parmi_notees`, `p_r5_au_moins_90_pour_cent`, `fidelite_echantillon`, `controle_negatif`,
  `activations_identiques_au_bit`, `lecture`, `regle_repli_appliquee`, `conformes_longueur`, `contextes_conformes`
  (résultat du rejeu) ; du résultat de la réparation : `lecture`, `cibles_par_condition`, `retrouves_par_condition`,
  `empreintes_retrouvees`, `non_resolus`, `par_voie`, `lots_rapport` (indépendance des lignes) ; du témoin : tout hors
  rattachement, étape, version (sa `lecture` comprise). Les grandeurs de couverture (retrouvées, non retrouvées) ne
  sont que **comparées** entre pièces ; un message d'arrêt nomme la clé, jamais la valeur.
- Jamais ouverts : `traces/…` de la branche source (`r1-rejeu.json` y recopie la sortie standard du rejeu, P-R5
  comprise), le journal de l'instance (`etape=fin fideles=… notees=…`), la sortie du recalcul (elle porte les comptes
  de retrouvées : seul le script la lit). Si un message les relaie, la session le déclare au registre (« vu avant les
  analyses ») et aux lecteurs R13.
- Gardes des analyses de conv-audit, **à mettre à jour de son côté** (addendum v4, « Analyses ») : `texte` (texte qui
  gouverne = addendum v4, chemin et empreinte, lu dans `preenregistrement`), `table-comparee` (table versée **et**
  `resultat_reparation_sha256` = sceau de la réparation versée), `provenance` (`tokenisation.addendum` = addendum v4,
  commande `rejeu_activations_v4`). Cette fiche ne les modifie pas ; ses attendus sont les mêmes valeurs.

## 7. Recalcul de réception (V4-E5 ; processeur ; commande exacte)

Arbre de recalcul `<REC>` : `git worktree add --detach <REC> 5bd62a004279776c2718b3201c11001e16fa6527` (arbre `src/`
égal à `5bd62a00`, vérifié par le script), où l'on recopie depuis le commit de versement `<C>`, par `git show
<C>:<chemin>`, avec leurs compagnons : `runs/R/manifeste.json`, `diag/R/resolution-graine-lot-v3-reparation.json`,
`prereg/R1-table-tokenisation-v4.json` ; les pièces de P3 de la configuration de la réparation (`chemin_textes`,
`chemin_scores`, `chemin_fiches`, `chemin_manifeste_p3`, `chemin_taches`, `chemin_consignes`) à leurs chemins, leurs
empreintes étant revérifiées par le code lui-même ; tokeniseur `<TOK>` : `meta-llama/Llama-3.1-8B-Instruct`,
révision `0e9e39f249a16976918f6564b8830bc894c89659`, `tokenizer.json`
`79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4`, sans les poids. Puis :

```
cd <REC> && PYTHONPATH=src timeout 900 nice -n 10 python -m controle_ia.runs_nuit.chaine_table_v4_v1 \
    --config prereg/R1-reparation-v4-config-v2.json \
    --reparation diag/R/resolution-graine-lot-v3-reparation.json \
    --table prereg/R1-table-tokenisation-v4.json --reception --tokeniseur <TOK> \
    > <HORS>/recalcul-reception-r1-v4.json 2> <HORS>/recalcul-reception-r1-v4.err ; echo "code $?"
```

Attendu : code 0, une ligne JSON avec `version` = `chaine_table_v4_v1`, `recalcul_egal_a_l_octet` = `true`, `table` =
`prereg/R1-table-tokenisation-v4.json`, `table_sha256` = sceau de la table versée, `reparation` =
`diag/R/resolution-graine-lot-v3-reparation.json`, `resultat_reparation_sha256` = son sceau, `run_reparation` = `R`,
`table_v3_sha256` = `ead8a668…6423`, `cibles` 89, `entrees_v3` 22, `retrouvees` et `non_retrouvees` égales à la table
versée (garde `recalcul`). Ni `<HORS>/…json` ni `.err` ne sont affichés : seul le script les lit.

## 8. Vérification mécanique (commande exacte)

```
python3 -I docs/notes/runs-r1-r2-r4-v1/reception-v4-v1/verifier_reception_r1_v4_v1.py verifier \
    --fiche docs/notes/runs-r1-r2-r4-v1/reception-v4-v1/fiche-reception-r1-v4-v1.md --fiche-sha256 <empreinte annoncée> \
    --depot <dépôt> --racine <arbre du commit C> --commit-versement <C> \
    --source refs/remotes/origin/calcul/r1-v4-reparation-reel-v1 \
    --run-reparation R --run-rejeu J --scores-p3 <chemin de scores-p3.npz> \
    --sortie-recalcul <HORS>/recalcul-reception-r1-v4.json --racine-recalcul <REC>
```

Ordre des gardes : `fiche`, `runs`, `textes`, `versement`, `octets`, `presence`, `compagnon`, `temoin`, `reparation`,
`table`, `chaine-locale`, `rejeu`, `commit-rejeu`, `rattachement`, `verdict`, `table-comparee`, `provenance`,
`comptes`, `coherence-table`, `fichiers`, `npz`, `recalcul`. Sortie conforme : « RÉCEPTION CONFORME ; gardes passées :
… », code 0 ; elle ne contient ni valeur de P-R5 ni compte de couverture.

## 9. Bloc d'attendus (sortie de `verifier_reception_r1_v4_v1.py bloc` ; mêmes valeurs que les sections 2 à 7)

<!-- attendus-machine : debut -->
```json
{
 "addendum_tokenisation": "prereg/R1-addendum-relance-v4.md",
 "branches": {
  "source": [
   "calcul/r1-v4-reparation-reel-v1",
   "calcul/r1-v4-reparation-reel-v2"
  ],
  "versement": "calcul/r1-r2-reel-v1"
 },
 "commandes": {
  "rejeu": "python -m controle_ia.runs_nuit.rejeu_activations_v4",
  "reparation": "python -m controle_ia.runs_nuit.resolution_graine_lot_v3 --etape reparation",
  "temoin": "python -m controle_ia.runs_nuit.resolution_graine_lot_v3 --etape temoin"
 },
 "commits": {
  "scellement": "937f13177892933955c9c34839b4b45a4db745df",
  "temoin_verse": "5bd62a004279776c2718b3201c11001e16fa6527"
 },
 "comptes": {
  "T": 10,
  "actions": 2400,
  "cibles": 89,
  "entrees_v3": 22,
  "episodes": 240,
  "identiques_base": 129,
  "lots": 28,
  "seuil_non_conformes": 10
 },
 "config_rejeu": {
  "chemin": "prereg/R1-rejeu-config-v6.json",
  "sha256_canonique": "a3ef1bac5b8768604f2418da8b55c7adc8954f247485ea12c587bd00f407575f"
 },
 "config_reparation": {
  "chemin": "prereg/R1-reparation-v4-config-v2.json",
  "sha256_canonique": "c34bf464177468d160975800da3cfe13d67e722a2e3b3c3e4c3c46d503ab680a"
 },
 "entropie": "36410133060804533274328900142752730279",
 "format": "attendus-reception-r1-v4-v1",
 "jouet": false,
 "motifs_arret_rejeu": [
  "non conforme",
  "echec"
 ],
 "motifs_run": {
  "rejeu": "^[0-9]{8}-[0-9]{6}-r1-v4-rejeu-reel$",
  "reparation": "^[0-9]{8}-[0-9]{6}-r1-v4-reparation-reel$"
 },
 "npz": {
  "couches": [
   7,
   15,
   23
  ],
  "identite": [
   "episode",
   "pas",
   "condition",
   "tache"
  ],
  "largeur": 4096,
  "nom_sortie": "activations-p3-rejeu-v1",
  "principaux": {
   "activations-p3-rejeu-v1-complement-hors-cout.npz": "maximum_hors_cout",
   "activations-p3-rejeu-v1-maximum.npz": "maximum",
   "activations-p3-rejeu-v1.npz": "moyenne"
  },
  "type_principal": "<f2",
  "types": {
   "activations_identiques": "|b1",
   "conforme_longueur": "|b1",
   "contexte_conforme": "|b1",
   "couches": "<i8",
   "ecart_fidelite": "<f8",
   "fidele": "|b1",
   "jetons_empan": "<i8",
   "jetons_empan_rejeu": "<i8",
   "trajectoire_identique": "|b1"
  }
 },
 "pieces": {
  "prereg/R1-R2-rejeu-p3-v1.md": {
   "compagnon": true,
   "sha256": "80c85a0085f444dc10f36e4e226d015802d2e20294c4fff2ae67adb0aca4ddea"
  },
  "prereg/R1-addendum-relance-v4.md": {
   "compagnon": true,
   "sha256": "0f10881b32fa4c0e5ec1eb02cf88fbd0fcb6ad13f70b59abc2d84e45a99f61c8"
  },
  "prereg/R1-rejeu-config-v6.json": {
   "compagnon": true,
   "sha256": "a9ebc6b0cd6c99e118ade7b304472b5452d2b43c63cc222d1adccd2ee4e95e75"
  },
  "prereg/R1-reparation-v4-config-v2.json": {
   "compagnon": true,
   "sha256": "4d0655d1bac5b15d6cb604e5853bed0bfe1eb48d6235772e39b86a698b8d85e5"
  },
  "prereg/R1-table-tokenisation-v3.json": {
   "compagnon": true,
   "sha256": "ead8a66851b2af5dfa02635297056872032878fbd2987ba780fb6c9096766423"
  },
  "scripts/amorce_instance_r1_v4_v2.sh": {
   "compagnon": true,
   "sha256": "22e64d72745168f947a37690e9bb29170011ef38f0649b6bbc7ca6f8825445b1"
  },
  "scripts/r1_v4_instance_v2.sh": {
   "compagnon": true,
   "sha256": "a02eda0c4c8519a1d7d3ddd452001a7b8357c7e6925ca1e9c28be703d362b5ae"
  },
  "src/controle_ia/manifeste.py": {
   "compagnon": false,
   "sha256": "1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d"
  },
  "src/controle_ia/runs_nuit/chaine_table_v4_v1.py": {
   "compagnon": true,
   "sha256": "a015e89fd1cf39d887a05617298b7c930c939f60449b2c0ed9e75975d097bdd1"
  },
  "src/controle_ia/runs_nuit/rejeu_activations_v4.py": {
   "compagnon": true,
   "sha256": "d31dcec074b513b597a4920a5c6501326ee18c8cefe4bbd83d381f4ac4b25a08"
  },
  "src/controle_ia/runs_nuit/resolution_graine_lot_v1.py": {
   "compagnon": true,
   "sha256": "5a9982b2a2248d5312c5a42bf34ac90c505ca579052985169aabb7e16c8c7156"
  },
  "src/controle_ia/runs_nuit/resolution_graine_lot_v2.py": {
   "compagnon": true,
   "sha256": "501ab45308f2ffe5e3cf25b0352b0d2e7f8bca0bb2ba7cd897c3b2c39b704f87"
  },
  "src/controle_ia/runs_nuit/resolution_graine_lot_v3.py": {
   "compagnon": true,
   "sha256": "9ce6d17818a04853db57fdbb70e347bc9fdd0153ba91c14b9530818c6b29f6e3"
  },
  "src/controle_ia/runs_nuit/resolution_graine_v1.py": {
   "compagnon": true,
   "sha256": "cdc22b5ad2659f82f512c39545c52fc826a6be2dc60fb3aeafda0c5d014a9663"
  },
  "src/controle_ia/scellement.py": {
   "compagnon": false,
   "sha256": "93beeb1c8aae75463afc98e76ffb330b1e4f26be9c08ae8fee539a2df6a94ef2"
  }
 },
 "preenregistrement": {
  "chemin": "prereg/R1-addendum-relance-v4.md",
  "sha256": "0f10881b32fa4c0e5ec1eb02cf88fbd0fcb6ad13f70b59abc2d84e45a99f61c8"
 },
 "run_source_p3": "20261019-230011-p3-reel",
 "scores_p3": {
  "chemin": "donnees/20261019-230011-p3-reel/scores-p3.npz",
  "sha256": "968414fc7ce7db935c2c4a390a13e2eceebe2fd722628cccb52caf27128004cf"
 },
 "table_en_session": "construite-en-session",
 "table_v3": {
  "chemin": "prereg/R1-table-tokenisation-v3.json",
  "sha256": "ead8a66851b2af5dfa02635297056872032878fbd2987ba780fb6c9096766423"
 },
 "table_v4": "prereg/R1-table-tokenisation-v4.json",
 "temoin": {
  "fichiers": {
   "diag/20261104-091009-r1-v4-temoin-reel/resolution-graine-lot-v3-temoin.json": "25d68f3335867e7222c1a6f24d024edff14a6141947d5e618696e8be88145dd2",
   "diag/20261104-091009-r1-v4-temoin-reel/resolution-graine-lot-v3-temoin.json.sha256": "23b4473468a806d889aa4e2aa9b73ff0beabe115b2eefdf4be87bd6465cc49c2",
   "runs/20261104-091009-r1-v4-temoin-reel/manifeste.json": "43e2dd5c605fc87f7aacd319ae258bbfd72a1dc27fcf6e7c3b5f6f3cc4e9ac01",
   "runs/20261104-091009-r1-v4-temoin-reel/manifeste.json.sha256": "d03f7bf13257554ed8b560e82f28e8a43bb9747997b205d01f1f8a76cc3f9ff4"
  },
  "run": "20261104-091009-r1-v4-temoin-reel"
 },
 "version_chaine": "chaine_table_v4_v1",
 "version_lot": "resolution_graine_lot_v3",
 "voie": "lot_fidele"
}
```
<!-- attendus-machine : fin -->
