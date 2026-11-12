# Contre-lecture (R2, R13) : préenregistrement « mesure unanime » v13, séquence v13, test de reprise v13, rédaction v7, gardes isolées v12 gardées, répétition générale v13

**Verdict : à corriger en v14 — un défaut de plomberie bloquant (CV13-1 : la garde témoin gardée sous son nom v12 teste des
noms v12 et ne voit aucune trace v13 ; elle est morte dans la séquence v13, et le texte la décrit comme vivante), plus trois
constats non bloquants (dépôt, limite de garde, commentaire). Aucune modification de science : les sections Hypothèse,
Prédiction, Métrique, Seuil, Critères de lecture gelés et Liste d'arrêt sont identiques au bit près à la v12 ; aucun faux
« confirmé », aucun faux blocage. CV12-1, CV12-3 et CV12-4 sont fermés et bien fermés ; CV12-2 n'est fermé qu'en partie.**

La protection « une seule exécution réelle » n'est **pas** perdue : le témoin `noclobber` (séquence, ligne 46) refuse toute
seconde exécution dans tous les scénarios honnêtes (vérifié). Ce qui est perdu, c'est une couche de garde entière (R5 :
« aucun repli silencieux » — la garde répond 0 quoi qu'il arrive) et la véracité du texte sur ses propres gardes (lignes 53 à
56 et 63). La correction change l'empreinte de la séquence, citée ligne 48 : elle passe nécessairement par une v14 et une
répétition refaite (une minute).

- **CV13-1** (plomberie ; **bloquant**) — `garde-trace-reelle-v12.sh`, ligne 7 ; `commandes-lecture-reelle-v13.sh`, lignes 34, 44 et
  54 ; `test-garde-trace-v12.sh`, lignes 14 à 17 ; texte, lignes 48, 53 à 56 et 63. La garde teste les trois noms littéraux
  `execution-reelle-v12.commencee`, `sortie-reelle-v12.json`, `sortie-reelle-v12.json.partiel` ; la séquence v13 pose le témoin
  `execution-reelle-v13.commencee` (ligne 34) et écrit `sortie-reelle-v13.json` et son `.partiel` (lignes 94 et 95). Démontré sur
  une copie : témoin v13 posé → code 0 ; sortie finale v13 → 0 ; `.partiel` v13 → 0 ; témoin v12 → 3 ; `.partiel` v12 → 3
  (`sortie-cv13-1-garde-aveugle-v1.txt`). Le test déposé `test-garde-trace-v12.sh` ne plante que des noms v12 et un état
  `repetition-v12/sortie-reelle-v12.json` : il passe, et donne une assurance fausse pour la v13. Le texte dit (lignes 53 et 54)
  que l'étape 0 « refuse toute sortie réelle nommée explicitement (`sortie-reelle-v13.json` et son `.partiel`) » — faux pour le
  code déposé — et (ligne 63) que les gardes sont « exercées par leurs tests déposés sur un état planté qui reproduit l'état
  déposé » — faux pour la garde témoin (l'état planté est v12). L'autre garde gardée, `garde-lecture-seule-v12.sh`, reçoit le
  nom de la note en argument et reste juste. **Correction** : une garde `garde-trace-reelle-v14.sh` et son test
  `test-garde-trace-v14.sh` aux noms v14 (état sain planté : `repetition-v14/sortie-reelle-v14.json`) ; séquence v14, lignes 38,
  44 et 54 ; `test-lecture-seule-v14.sh`, ligne 37 (il copie les gardes et leurs tests par leur nom) ; texte, ligne 48 ;
  répétition refaite. **Proposé** (au choix de l'auteur) pour que la classe d'erreur ne revienne plus : que la séquence passe
  les trois noms en arguments à la garde (`bash garde-trace-reelle-v14.sh "$TEMOIN" "$SORTIE" "$SORTIE.partiel"`), la garde
  devenant indépendante de la version comme `garde-lecture-seule-v12.sh` l'est déjà, et que le test vérifie que le `TEMOIN=`
  de la séquence est bien le nom qu'il plante.
- **CV13-2** (dépôt ; non bloquant, à faire dans le commit de la v14) — `contre-lecture-v11/` et `contre-lecture-v12/` ; texte,
  lignes 432 et 433 (« versés dans l'arbre »). Le rapport v12 demandait de verser `contre-lecture-v11/` « avec ses scripts et
  sorties, comme pour la v10 ». Le dossier versé contient 6 fichiers sur les 25 porteurs d'un compagnon dans le bac à sable de
  son auteur : aucun des quatre scripts (`scripts/verif_cv11_v1.py`, `lecture_seule_cv11_v1.sh`, `repro_set_e_v1.sh`,
  `ecrire_npz_E52_v10.py`), aucune des sorties que le rapport v11 cite comme preuves (`sortie-lecture-seule-v1.txt` — la preuve
  de CV11-1 —, `sortie-verif-cv11-*.json`, `sortie-test-gardes-v11.json`, `repetition-rejouee-v11.log`, `repetition-E52-v11.log`,
  `sortie-E52-resume-v1.txt`, etc.). La copie s'est arrêtée après `heure-debut-repetition.txt` (ordre alphabétique, horodatages à
  la même seconde). `contre-lecture-v12/` : 24 sur 32 ; manquent `sortie-sections-v11-v12-v1.txt` (la preuve R1 citée aux lignes 57
  et 153 du rapport v12), `empreinte-E52.txt`, `sortie-ecrire-npz-E52-v1.json`, les trois `heure-debut*.txt` et deux `.err` vides.
  Les 30 fichiers versés sont identiques à l'octet à leurs sources (`sortie-versement-cv12-2-v1.txt`). Les deux bacs à sable
  existent encore : `cp` suffit. Le texte n'a pas à changer (il ne cite que les rapports, dont les empreintes sont justes).
- **CV13-3** (plomberie, limite ; non bloquant — observation (g1) de l'auteur) — `commandes-lecture-reelle-v13.sh`, ligne 61. En
  mode `REPETITION`, le refus des données réelles est un test de préfixe de chemin absolu : un chemin relatif
  (`../../../../../donnees/…`), un lien symbolique ailleurs, une copie hors de `donnees/`, ou même un double séparateur
  (`…/canal-conv-audit-n04//donnees/…`) passent (démontré par comparaison de chaînes, sans ouvrir aucun fichier :
  `sortie-g1-g2-etoiles-v1.txt`). Une garde par empreinte (`[ "$EMPREINTE" != "$EMPREINTE_REELLE" ] || exit 4`, avec
  `EMPREINTE_REELLE` de la ligne 33) fermerait le trou quel que soit le chemin, car le script compare l'argument 3 à l'empreinte du
  fichier lu : lire le fichier réel en répétition exige de passer `968414fc…`. Non bloquant seul : la garde protège l'opérateur
  contre sa propre erreur, le texte nomme le fichier de répétition par son nom et son empreinte, la répétition déposée a lu le bon
  fichier (`447dc136…`), et le scénario exige de taper l'empreinte réelle dans une commande de répétition. Puisque la séquence est
  réécrite pour CV13-1, **recommandé** d'ajouter cette ligne en v14 (coût nul ; le texte ne décrit pas la ligne 61). Le chemin
  relatif de la répétition déposée n'est pas un défaut : la séquence fait `cd` vers son dossier (ligne 25), le manifeste enregistre
  `synthetique-format-reel-repetition.npz` et l'empreinte `447dc136…` le rattache au fichier déposé ; ma répétition rejouée avec le
  même chemin relatif reproduit la sortie déposée à l'octet.
- **CV13-4** (commentaire ; non bloquant, cosmétique — observation (g2)) — `test-lecture-seule-v13.sh`, ligne 53 : « le commit est
  comparé, ligne 68 » ; la comparaison est ligne 71 de la séquence v13 (et déjà 71 en v12 ; 68 en v11 : renvoi périmé depuis la
  v12). Le test doit être réédité pour CV13-1 (ligne 37) : corriger le renvoi au passage (ou l'ôter : « dans la branche
  `LECTURE_SEULE` »).

Remarques sans constat : (i) texte, ligne 435 : « phrase coupée dans `rediger_note_lecture_v7.py` recollée » — la coupure était
dans la v6, la v7 la recolle ; lisible, pas une erreur. (ii) Ligne 62 : « le fichier déposé lui-même, de même empreinte et hors de
`donnees/` » — « de même empreinte » est devenu redondant ; sans conséquence. (iii) Le manifeste de la répétition v13 enregistre un
chemin relatif là où la v12 enregistrait un chemin absolu ; les deux désignent le fichier déposé (voir CV13-3).

- **Contre-lecteur** : sous-agent neuf servi par **Fable 5.1** (identifiant de modèle `claude-fable-5-1`), tel que mon invite système
  me le donne : modèle différent de l'auteur de la v13 (Opus 4.6) et de l'instance qui orchestre (Opus 5.5), R13. Je n'ai écrit ni
  le préenregistrement, ni son code, ni la séquence, ni les gardes, ni les tests, ni aucun rapport précédent ; j'ai lu le rapport
  v12 (`a061e2a6…`, empreinte vérifiée) et la section 4 du rapport v11 (`d654dea6…`, vérifiée) comme le brief le demande.
- Début : 2026-10-28 08:27:21 UTC (`date -u`, appel séparé). Les heures d'`ls` sont à l'heure de Paris (UTC + 1) : le texte v13
  déposé date de 08:17 UTC, la séquence v13 de 08:03, le test v13 de 08:00, la rédaction v7 de 07:51, les compagnons de 08:20, la
  répétition déposée de 08:21 UTC ; sa note cite l'empreinte `f52de345…` du texte v13 tel qu'il est sur disque : la répétition a
  été faite sur le texte final.
- Processeur seul. `commandes-lecture-reelle-v13.sh` n'a été lancé qu'en `REPETITION` (sur le fichier synthétique déposé, chemin
  relatif, `MESURE_INSTANCE=x`) et en `LECTURE_SEULE` (second argument `COMMITTEST` ou `MAUVAIS_COMMIT` par le test déposé, jamais un
  commit réel), toujours sur des copies ; le mode réel jamais (son chemin de données est codé en dur vers `donnees/`). **Aucun
  fichier de `donnees/` lu, listé, ouvert ni empreinté** ; la démonstration de CV13-3 est une comparaison de chaînes. Aucun fichier
  existant du dépôt modifié ; seul `contre-lecture-v13/` est écrit ; aucun `git`, aucun commit, aucune dépense, aucune clé ni jeton
  lu. Interpréteur `/opt/venv-essaim-sim-v1/bin/python` (avec `-I -B` dans la séquence ; `-B` et `PYTHONPATH=…/src` pour
  `controle_ia`), numpy 2.5.4, bash 5.2. Mes vérifications importent `prereg` et `scellement` du dépôt sans modification.

## Empreintes lues

| fichier | empreinte | état |
|---|---|---|
| `preenregistrement-mesure-unanime-v13.md` | `f52de3456e95872cb100cc6b866f7ad1912cdc52d664a48b4da2eccd3070c578` | objet ; = l'attendue du brief ; pas encore scellé (voulu) ; `prereg.problemes` : aucun ; 437 lignes ; `**` tous appariés (569 occurrences, l'impair étant le littéral `` `**` `` de la ligne 422, comme en v12 : 547) ; aucun ⟨…⟩, « À REMPLIR » ni `<<…>>` ; cité par la note de répétition déposée |
| `preenregistrement-mesure-unanime-v12.md` | `89d278e8e7ca02d1a8b4942b25c466287e70bce2a5c4aa190524355a82f56186` | = l'attendue du brief ; gardée (R12) |
| v11, v10, v9 ; v8 à v1 | `b1c1dd69…`, `785a33fa…`, `9206956b…` ; `92c208af`, `54bb2892`, `24b5785b`, `29f91ff3`, `57187171`, `3a52f304`, `e6369f43`, `7158affc…a935` | conformes à l'en-tête et à la ligne 306 |
| `analyse_fausses_alertes_v8.py` | `52b1760a…5400` | conforme ; inchangé depuis la v8 ; compagnon conforme |
| `sortie-synthetique-essai-v8.json` | `f83456be…fe62` | conforme |
| `lecture_mecanique_v8.py` ; `essai_lecture_mecanique_v8.py` → `essai-lecture-mecanique-v8.json` | `7f28af2b…6a623` ; `bedf26b8…ede2` → `0745cc20…bdef` | conformes |
| `commandes-lecture-reelle-v13.sh` | `edc08b3fc1b8b7d786c2197e5b518a214f69956615143746ba07b11b09c7dbd8` | conforme ; compagnon conforme ; ne diffère de la v12 que par les noms v12 → v13 (texte, témoin, sorties, journal, sous-dossier, test de reprise) et v6 → v7 (rédaction) ; les gardes et le test de garde restent cités en v12 (`sortie-diff-sequence-v12-v13-v1.txt`) |
| `garde-trace-reelle-v12.sh` ; `test-garde-trace-v12.sh` | `3b6fc4d8…b85d` ; `8d730dde…6b45` | conformes aux citations ; **gardés tels quels : noms v12 codés en dur (CV13-1)** |
| `garde-lecture-seule-v12.sh` | `f5837407…734b` | conforme ; prend le nom de la note en argument : juste pour la v13 |
| `test-lecture-seule-v13.sh` | `ac080806c9c824142014910507bc9cb8b14ff77619f788ed85d43a4dd3f1c9ce` | conforme ; compagnon conforme ; ne diffère de la v12 que par les noms et l'ajout des cas (B3 bis) et (B3 ter) (`sortie-diff-test-v12-v13-v1.txt`) ; 38 s, code 0, ne laisse rien |
| `rediger_note_lecture_v7.py` | `a9af81c40864b77ecbcef8f3930ddb0061fbd2ae102c836ddeee084fc4b49ab8` | conforme ; compagnon conforme ; ne diffère de la v6 que par la docstring (lignes 1, 5, 7) : logique identique |
| `table_m2bis_m4_v8.py` → `table-m2bis-m4-v8.json` | `7e512516…e0d3` → `f63faada…b120` | conformes |
| `synthetique-format-reel-repetition.npz` | `447dc136dde083f68d1f9899344207bd5b8a6caf56c95b441d1c492dd72cb709` | compagnon conforme ; = `manifeste.empreinte_donnees` de la répétition déposée |
| `repetition-v13/` : effectifs, table en vigueur, sortie, lecture, note | `c05aa6fa…`, `f6e65b72…`, `a4b3e1b1…`, `a06029e8…`, `01b127a3…` | cinq compagnons conformes ; effectifs et table en vigueur identiques à l'octet à la v12 ; sortie identique à la v12 hors `manifeste.donnees` (chemin relatif) ; lecture identique hors `sources.sortie` ; note identique hors ligne 3 ; **rejoués : quatre identiques à l'octet, la note ne diffère que par l'heure** |
| rapports v1 à v12, complément v2 | `5d47ae52…`, `0fb0734a…`, `ef6b8770…`, `912dd47a…`, `23ce5f93…`, `7783ab01…`, `989c02de…`, `aeeca90d…`, `c401043b…`, `d654dea6…a825`, `a061e2a6…dbf1`, `e5ca74bb…` | conformes à l'en-tête et à la section Contre-lecture ; `contre-lecture-v11/` et `contre-lecture-v12/` présents (CV13-2 : contenu partiel) |
| `src/controle_ia/bases/sequentiel.py` ; `…/pari-de-signe/conception-pari-de-signe-v3.md` | `35a09834…1ba8` ; `1518a12f…db14` | conformes |
| `donnees/…/scores-p3.npz` | `968414fc…` cité | **non vérifié, à dessein** (R1 : rien n'est lu sous `donnees/`) |
| `docs/notes/collisionneur-mesures-fortes-v1/synthese-mesures-fortes-v1.md` | `bed9107b…` cité « sur `main` » | absent de ce worktree : non vérifiable ici (comme en v12) |

Compagnons `.sha256` : 68 au premier niveau, 5 dans `repetition-v13/`, 6 dans `contre-lecture-v11/`, 20 + 4 dans
`contre-lecture-v12/` : **tous vérifient** (`sortie-compagnons-v1.txt`). Les 33 empreintes pleines et les 19 courtes citées par le
texte sont toutes retrouvées sur disque, aux deux exceptions dites (`sortie-verif-cv13-texte-v1.json`).

## 1. Fermeture de CV12-1 à CV12-4

| constat | état | où et pourquoi |
|---|---|---|
| CV12-1 (« une copie » → « le fichier déposé lui-même ») | **fermé, juste** | texte, ligne 62 ; `repetition-v13/sortie-reelle-v13.json`, `manifeste.donnees` = `synthetique-format-reel-repetition.npz`, résolu depuis le dossier du préenregistrement (séquence, ligne 25) : le fichier déposé, empreinte `447dc136…` ; la note déposée (ligne 3) dit la même chose. |
| CV12-2 (verser `contre-lecture-v11/` et `-v12/`) | **fermé en partie** (CV13-2) | les répertoires existent, les rapports y sont avec les empreintes citées ; mais 6 fichiers sur 25 pour la v11 (aucun script), 24 sur 32 pour la v12. |
| CV12-3 (cas « note supprimée, lecture scellée » et « lecture corrompue ») | **fermé, juste** | `test-lecture-seule-v13.sh`, lignes 67 à 84 : (B3 bis) attend 0, note scellée, lecture inchangée ; (B3 ter) corrompt la lecture d'un octet après l'avoir sauvée, attend ≠ 0 et aucune note, restaure. Lancé par la répétition (séquence, ligne 55) et seul (38 s, code 0). **Rejoué à la main** pour vérifier que (B3 ter) échoue pour la bonne raison : code 1, « ARRÊT : lecture-mecanique-reelle-v13.json : empreinte 14664d3e… ≠ scellée a88c01b4… », aucune note, aucun `.partiel` ; (B3 bis) : « OK a88c01b4… lecture », lecture inchangée, note refaite et scellée (`sortie-lecture-seule-main-v1.txt`). Texte, ligne 61 : la liste des cas est exactement celle du test, dans l'ordre. |
| CV12-4 (docstring de la rédaction) | **fermé, juste** | `rediger_note_lecture_v7.py`, lignes 1 à 7 : phrase recollée, mention de version en fin de paragraphe, usage avec `--instance NOM --date DATE [--table FICHIER]` ; `argparse` : `--instance` et `--date` `required=True` (lignes 30, 31). |

## 2. Réponses aux points du brief

**(b) Rien d'autre n'a changé** (`diff-texte-v12-v13.txt`, `sortie-verif-cv13-texte-v1.json`) : les six sections de science sont
**identiques au bit près** (Hypothèse 5 754 caractères, Prédiction 3 848, Métrique 5 584, Seuil 3 202, Critères 4 937, Liste
d'arrêt 817) ; le Plan d'analyse est identique jusqu'au point « **Commandes** » (959 caractères) et ne diffère ensuite que par les
noms (`effectifs-reel-v13.json`, `sortie-reelle-v13.json`, `lecture-mecanique-reelle-v13.json`, `rediger_note_lecture_v7.py`,
`note-lecture-mecanique-v13.md`, `commandes-lecture-reelle-v13.sh`, `journal-lecture-reelle-v13.log`) ; la section Contre-lecture
commence par celle de la v12 et ajoute dix lignes (428 à 437). Le reste du diff : titre, lignes 3 et 4 (auteur, « Remplace la
v12 »), 31 (date), 32 (« v9 à v13 »), 47 et 48 (noms et empreintes de la séquence, du test et de la rédaction), 53 à 55 (témoin,
sortie, sous-dossier v13), 61 et 62 (cas du test ; « le fichier déposé lui-même »). Aucune hypothèse, prédiction, seuil, critère
ni ligne d'arrêt n'a bougé.

**(c) Noms et empreintes** : tableau ci-dessus ; croisement automatique de toutes les empreintes du texte avec le disque : 33
pleines et 19 courtes, aucune introuvable hors les deux non vérifiables à dessein.

**(d) Répétition déposée** : 3 sondes réelles, 2 placebo, E = 60 (manifeste, effectifs) ; chemin lu = le fichier déposé ; note
« répétition générale (aucune instance réelle) … **RÉPÉTITION GÉNÉRALE ou essai : aucune donnée réelle, cette note n'est pas une
lecture** », « NON SCELLÉ (GardeArret) » (attendu avant scellement) ; empreinte du préenregistrement citée = `f52de345…` du texte
v13 sur disque. Rejouée depuis une copie isolée (08:33:54 → 08:35:06 UTC, dont 30 s pour les deux tests de l'étape 0 ; code 0) :
effectifs, table en vigueur, sortie et lecture **identiques à l'octet** au dépôt, note identique hors l'heure ; les deux gardes
exercées par leurs tests (journal) ; rien d'écrit au premier niveau (`repetition-rejouee-v13.log`, `comparaison-repetition-v1.txt`).
Verdicts de cet essai du code, sans valeur de résultat (inchangés depuis la v9) : M1 confirmé, M2 attendu, M2 ter (1), M3 tenu,
M4 confirmé (excès 0,047), première ligne.

**(e) Section de traitement CV12** (lignes 428 à 437) : fidèle au rapport v12 — contre-lecteur Fable 5.1, chemin et empreinte du
rapport, verdict et ses motifs (« texte et dépôt seulement, aucun défaut de plomberie »), les quatre constats résumés
conformément à leurs énoncés (CV12-1 : ligne 62, la phrase décrivait la v11 ; CV12-3 : B3 bis et B3 ter ; CV12-4 : docstring et
usage). Seule nuance : « versés dans l'arbre » pour CV12-2 est vrai des répertoires, pas de leur contenu (CV13-2).

**(f) Autres défauts** : CV13-1 (voir le verdict). Vérifié aussi : les deux gardes isolées sont bien appelées par la séquence v13
(lignes 44, 52, 54, 55) ; `compagnons()` (ligne 38) cite les dix bons compagnons, tous présents ; `sceller` du dépôt est idempotent et
refuse une autre empreinte (`scellement.py`, lignes 64 à 71) ; `exiger_prereg_scelle` vérifie puis contrôle la conformité ; les
fichiers v12 sont gardés (R12) ; aucune trace `execution-reelle-v13.commencee`, `sortie-reelle-v13.json` ni `.partiel` au premier
niveau du dossier déposé.

**(g1)** : limite à consigner, non bloquante seule ; recommandée en v14 puisque la séquence y est réécrite (CV13-3).
**(g2)** : non bloquant, cosmétique ; à corriger au passage (CV13-4).

**Règle de contenu (R-597)** : ce rapport décrit les gardes d'un préenregistrement et le défaut de l'une d'elles ; il ne contient
aucune recette d'évasion de moniteur ; les énoncés M1 à M4 restent des propriétés de lois de probabilité sur des épisodes honnêtes.

## 3. Mes scripts et sorties (dans ce dossier, chacun avec son compagnon `.sha256`)

| fichier | contenu |
|---|---|
| `heure-debut.txt`, `heure-debut-repetition.txt` | heures `date -u` relevées dans des appels séparés (début ; début et fin de la répétition rejouée) |
| `diff-texte-v12-v13.txt` | `diff` brut des deux textes (69 lignes) |
| `sortie-empreintes-v1.txt` | empreintes sur disque de tout ce que cite la v13, et de `repetition-v13/` |
| `sortie-compagnons-v1.txt` | `sha256sum -c` de tous les compagnons du dossier et des sous-dossiers |
| `sortie-versement-cv12-2-v1.txt` | `contre-lecture-v11/` et `-v12/` versés comparés aux bacs à sable (manquants ; identité des versés) |
| `sortie-diff-sequence-v12-v13-v1.txt`, `sortie-diff-test-v12-v13-v1.txt`, `sortie-diff-redaction-v6-v7-v1.txt` | diffs bruts et normalisés (noms vNN) de la séquence, du test de reprise et de la rédaction |
| `sortie-comparaison-repetition-v12-v13-v1.txt` | répétitions v12 et v13 déposées : différences champ par champ |
| `repetition-rejouee-v13.log`, `comparaison-repetition-v1.txt` | répétition rejouée sur la copie et comparaison au dépôt |
| `scripts/verif_cv13_v1.py` → `sortie-verif-cv13-texte-v1.json` | `prereg.problemes`, sections R1 au bit près, croisement des empreintes, `**`, marqueurs |
| `sortie-g1-g2-etoiles-v1.txt` | appariement global des `**` ; (g1) test de chaîne de la ligne 61 et garde par empreinte ; chemins des manifestes v11 à v13 ; (g2) renvoi de ligne |
| `sortie-lecture-seule-main-v1.txt` | cas (B2), (B3 bis), (B3 ter) de `LECTURE_SEULE` rejoués à la main, messages capturés |
| `sortie-cv13-1-garde-aveugle-v1.txt` | garde témoin v12 sur traces v13 (0, 0, 0) et v12 (3, 3) ; `noclobber` seul |
| `sortie-tests-deposes-v1.txt` | `test-lecture-seule-v13.sh` (38 s, 0) et `test-garde-trace-v12.sh` (0) lancés seuls depuis la copie |

Les copies de travail (`copie-dossier-*/`, `copie-lecture-seule-*/`) restent dans mon bac à sable et ne sont pas versées.
Empreinte de ce rapport : dans `rapport-contre-lecture-mesure-unanime-v13.md.sha256`, à côté.
Durée : 16 minutes 34 secondes, de 08:27:21 à 08:43:55 UTC, la répétition rejouée comprise.

Fin : 2026-10-28 08:43:55 UTC (`date -u`, relevé dans un appel séparé avant l'écriture de cette ligne).
