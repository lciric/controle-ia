# Contre-lecture (R2, R13) : préenregistrement « mesure unanime » v12, séquence v12, gardes isolées et leurs tests, lecture mécanique v8 et son essai, rédaction v6, répétition générale v12

**Verdict : à corriger en v13 — corrections de texte et de dépôt seulement ; aucun défaut de plomberie, aucune
modification de science, aucun faux « confirmé », aucun faux blocage.** CV11-1 est fermé et bien fermé ; CV11-3 est fermé ;
CV11-2 est fermé sauf que la correction de (f) a introduit une phrase fausse pour le dépôt v12 (CV12-1). La liste pour la v13 :
- **CV12-1** (texte, en-tête, ligne 62) : « une **copie** de ce fichier, de même empreinte et hors de `donnees/`, est le chemin lu » —
  faux pour la répétition v12 déposée : son manifeste (`repetition-v12/sortie-reelle-v12.json`, `manifeste.donnees`) et sa note
  (ligne 3) disent que le chemin lu est **le fichier déposé lui-même**,
  `…/mesure-unanime-v1/synthetique-format-reel-repetition.npz`. La phrase décrit la situation de la v11. Écrire « le fichier
  déposé lui-même (hors de `donnees/`) est le chemin lu », ou retirer la parenthèse.
- **CV12-2** (dépôt) : le texte cite `contre-lecture-v11/rapport-contre-lecture-mesure-unanime-v11.md` (ligne 416), **absent du
  dossier** (vérifié sur disque, `find` sur tout l'arbre de travail : aucun fichier de ce nom) ; le rapport v11 n'existe que dans
  le bac à sable de son auteur (empreinte conforme, `d654dea6…`). Le verser avec ses scripts et sorties, comme pour la v10, dans
  le commit qui porte le texte ; de même pour ce rapport v12 (`contre-lecture-v12/`).
- **CV12-3** (test déposé, mineur) : `test-lecture-seule-v12.sh` n'exerce pas le second point de CV11-1 — la lecture déjà scellée,
  **vérifiée** avant la note (séquence, lignes 100 et 101) : ni le cas sain (note retirée, lecture scellée intacte → note refaite,
  lecture intacte), ni l'artefact (lecture corrompue d'un octet → refus à l'étape (3), aucune note). Je les ai exercés à la main
  (cas G et G ter, section 2 : conformes), mais R5 veut un test déposé ; quelques lignes suffisent (proposées en section 3).
- **CV12-4** (docstring, cosmétique) : `rediger_note_lecture_v6.py`, ligne 1 — l'insertion « — version 6 (CV11-3) : --instance et
  --date obligatoires ; docstrings » coupe la phrase « à partir de la lecture mécanique (…) et de la sortie réelle » ; ligne 6, la
  ligne d'usage omet `--instance`, `--date` (obligatoires) et `--table`.

Vérifié en lançant, et conforme (tout sur des copies dans mon bac à sable ; le mode réel jamais lancé ; aucun fichier de
`donnees/` ouvert, chargé ou empreinté) :
- **CV11-1** : `test-lecture-seule-v12.sh` déposé (30 s, code 0, ses six cas conformes) ; puis seize cas sur ma copie
  (`sortie-lecture-seule-v1.txt`) : sans instance → 1 avec message ; préenregistrement non scellé → 1 (`GardeArret`) ; sortie
  absente ou non scellée → 6 ; sortie scellée puis corrompue → 1 (« ARRÊT : … empreinte ≠ scellée ») ; table en vigueur absente
  → 1 (message de `cat`) ; compagnon de la table en vigueur faux → 1 (`sha256sum`) ; commit ≠ manifeste → **8** ; empreinte des
  données du manifeste ≠ réelle → 1 à l'étape (3), aucune note ; **cas sain → 0, lecture et note écrites et scellées, journal
  complet, aucune mort silencieuse** ; second appel → **7**, les quatre fichiers inchangés ; note retirée, lecture scellée intacte
  → 0, note refaite, lecture et compagnon intacts (date 2000 conservée) ; **G ter : lecture scellée puis corrompue d'un octet →
  1 (« ARRÊT : lecture-mecanique-reelle-v12.json : empreinte … ≠ scellée … »), aucune note écrite** ; lecture présente non scellée
  → refaite à l'octet et scellée ; `.partiel` de lecture laissé → refait ; note présente non scellée → refaite. Aucune autre fin
  de branche de `etape_0` ne finit par `… && { … }` : les trois branches finissent par `printf … >> "$TEMOIN"`,
  `bash garde-lecture-seule-v12.sh …` et `bash test-lecture-seule-v12.sh` ; les deux autres `&& {` de la séquence (ligne 37,
  dans `sceller`, suivi d'une commande ; ligne 87, dans un bloc `if` suivi d'autres commandes) ne sont pas en fin de fonction.
- **La répétition générale, rejouée** depuis une copie (`REPETITION`, copie du fichier `447dc136…`, 3 2, `MESURE_INSTANCE=x`
  dans l'environnement) : 1 min 0 s (dont 30 s pour les deux tests de l'étape 0), code 0 ; effectifs (`c05aa6fa…`), table en
  vigueur (`f6e65b72…`) et lecture (`1098dea6…`) **identiques à l'octet** au dépôt ; la sortie ne diffère que par
  `manifeste.donnees` ; la note, par sa ligne 3 (heure, empreinte de la sortie) ; elle commence par « répétition générale
  (aucune instance réelle) » (l'instance de l'environnement est bien écrasée, CV11-3 (d)), dit « NON SCELLÉ (GardeArret) » et
  « RÉPÉTITION GÉNÉRALE ou essai : aucune donnée réelle » ; aucun avertissement `utcnow` ; aucune trace au premier niveau.
- **La branche E ≠ 60** (fichier au format réel, E = 52, `106cb7a1…`, écrit par le script de la contre-lecture v10 ; lancé en
  arrière-plan) : au bout, code 0, 8 min 44 s ; table refaite au E et aux longueurs observés (K par pli 31 ou 32, L = 0,0305),
  scellée, **désignée par la table en vigueur scellée avant l'étape (2)** (journal, lignes 19 à 22 : CV11-3 (e)), vérifiée par la
  lecture (E = 52 dans la table comme dans la sortie) ; note scellée citant la table refaite ; six compagnons conformes ; aucun
  `.partiel`.
- **Le fond** (`scripts/verif_cv12_v1.py`) : arbre de M2 ter réécrit depuis le texte seul, 64 combinaisons × deux r₀ : **aucun
  désaccord** de feuille ni d'étiquette, réserve (2a)/(2b) conforme, r₀ jamais condition, bornes à 10⁻⁹ ; bornes de M1, M2,
  M2 bis, M3, M4, placebo et la ligne de lecture (aucun faux « confirmé », aucun faux blocage) ; **excès apparié de M4 recalculé
  par sonde** avec `un_passage` sur le fichier de la répétition : 0,0473 = la sortie déposée, de même la quantité (0,1025), la
  quantité à τ = 0 (0,050), le maximum (0,0133) et la différence des médianes (0,0525) ; mélange à pas fixé (marges par pas et
  masque gardés exactement ; r₀ = 0,25 → −0,004 ; une dérive de 0,3 par pas survit au pas fixé et s'aplatit au mélange) ;
  `--test-gardes` : quinze entrées ; **onze refus du mode réel sans un octet écrit** ; le cas sain écrit 807 octets identiques
  aux effectifs déposés ; l'essai brut de la lecture v8 **reproduit à l'octet** (`0745cc20…`) ; tous les chiffres cités.
- **R1** : les sections Hypothèse, Prédiction chiffrée, Métrique, Seuil, Critères de lecture gelés et Liste d'arrêt sont
  **identiques au bit près** entre la v11 et la v12 (`sortie-sections-v11-v12-v1.txt`) ; seuls l'en-tête, les noms de fichiers
  et la durée du Plan d'analyse, et la section Contre-lecture changent.
- **Empreintes** : toutes celles de l'en-tête correspondent aux fichiers ; les 65 compagnons du premier niveau, les 5 de
  `repetition-v12/` et les 11 de `contre-lecture-v10/` vérifient ; `prereg.problemes` ne relève rien sur la v12.

- Contre-lecteur : sous-agent neuf **Fable 5.1** (l'auteur de la v12 est Opus 4.8 : modèle différent, R13). Je n'ai écrit ni le
  préenregistrement, ni son code, ni la séquence, ni les gardes, ni les tests, ni aucun rapport précédent ; j'ai lu le rapport
  v11 (`d654dea6…`, empreinte vérifiée) comme le brief le demande.
- Début : 2026-10-28 04:43:46 UTC (`date -u`, appel séparé). Fin : dernière ligne. Les heures d'`ls` sont à l'heure de Paris
  (UTC + 1) : les fichiers v12 déposés datent de 04:08 à 04:40 UTC ; la note de répétition déposée (04:40:14 UTC) cite
  l'empreinte `89d278e8…` du texte v12 tel qu'il est sur disque (modifié pour la dernière fois à 04:38 UTC) : la répétition a été
  faite sur le texte final.
- Processeur seul. `commandes-lecture-reelle-v12.sh` n'a été lancé qu'en `REPETITION` et en `LECTURE_SEULE` (second argument
  `abc1234`, `pas-le-bon-commit` ou `repetition-generale`, jamais un commit réel), toujours sur des copies ; le mode réel
  jamais ; la garde témoin isolée a été lancée **en place** sur le dossier déposé (elle ne fait que tester l'existence de trois
  noms : code 0 ; depuis `repetition-v12/` : code 3). L'artefact de `LECTURE_SEULE` est un petit npz synthétique (3 + 2 sondes)
  dont le manifeste porte, à dessein, l'empreinte réelle `968414fc…` (comme le test déposé) : il vit dans
  `copie-lecture-seule/` avec un `LISEZMOI-ARTEFACT.txt`, et n'est pas une sortie. Aucune clé ni jeton lu ; **aucun `git`** (la
  branche a été lue dans le fichier `HEAD` du worktree : `canal/conv-audit-n04`) ; aucun fichier du dépôt modifié ; aucun
  commit. Interpréteur `/opt/venv-essaim-sim-v1/bin/python -I -B` (sans `-I` et avec `PYTHONPATH=…/src` pour `controle_ia`),
  numpy 2.5.4, bash 5.2.21. Mes vérifications importent le script v8 et la lecture v8 **sans modification** depuis la copie
  (empreintes assertées dans le script).

## Empreintes lues

| fichier | empreinte | état |
|---|---|---|
| `preenregistrement-mesure-unanime-v12.md` | `89d278e8e7ca02d1a8b4942b25c466287e70bce2a5c4aa190524355a82f56186` | objet ; pas encore scellé (voulu) ; aucun « ⟨…⟩ » ; `**` tous appariés (le seul impair est le littéral `` `**` `` de la ligne 422) ; `prereg.problemes` : aucun ; cité par la note de répétition déposée |
| `preenregistrement-mesure-unanime-v11.md`, `-v10.md`, `-v9.md`, v8 à v1 | `b1c1dd69…`, `785a33fa…`, `9206956b…` ; `92c208af`, `54bb2892`, `24b5785b`, `29f91ff3`, `57187171`, `3a52f304`, `e6369f43`, `7158affc` | conformes à l'en-tête |
| `analyse_fausses_alertes_v8.py` | `52b1760a…5400` | conforme ; compagnon conforme ; inchangé depuis la v8 (même empreinte qu'en v11) |
| `sortie-synthetique-essai-v8.json` | `f83456be…fe62` | conforme ; compagnon conforme |
| `lecture_mecanique_v8.py` | `7f28af2b…6a623` | conforme ; compagnon conforme ; **`diff` avec la v7 : trois lignes de docstring (1, 2, 15), rien d'autre** |
| `essai_lecture_mecanique_v8.py` → `essai-lecture-mecanique-v8.json` | `bedf26b8…ede2` → `0745cc20…bbdef` | conformes ; compagnons conformes ; essai ne diffère de la v7 que par la docstring et le nom du module chargé ; sortie **reproduite à l'octet**, identique à l'essai v7 déposé |
| `rediger_note_lecture_v6.py` | `f51eaf7e…9149` | conforme ; compagnon conforme ; ne diffère de la v5 que par la docstring (lignes 1, 6) et `--date` **`required=True`** (ligne 30) |
| `commandes-lecture-reelle-v12.sh` | `a971896d…053a` | conforme ; compagnon conforme ; exécutable |
| `garde-trace-reelle-v12.sh`, `test-garde-trace-v12.sh` | `3b6fc4d8…b85d`, `8d730dde…6b45` | conformes ; compagnons conformes ; ne diffèrent des v11 que par « v11 » → « v12 » |
| `garde-lecture-seule-v12.sh`, `test-lecture-seule-v12.sh` | `f5837407…734b`, `0fd827a2…52f8` | conformes ; compagnons conformes ; nouveaux en v12 |
| `table_m2bis_m4_v8.py` → `table-m2bis-m4-v8.json` | `7e512516…e0d3` → `f63faada…b120` | conformes ; compagnons conformes ; chiffres cités = ceux de la table |
| `synthetique-format-reel-repetition.npz` | `447dc136…b709` | compagnon conforme ; ma copie de même empreinte |
| `repetition-v12/` : effectifs, lecture, note, sortie, table en vigueur | `c05aa6fa…`, `1098dea6…`, `1e0c3fcf…`, `0d6561a4…`, `f6e65b72…` | cinq compagnons conformes ; rejoués (section 2) ; `manifeste.donnees` = le fichier déposé lui-même (CV12-1) |
| rapports v1 à v10, complément v2 | `5d47ae52…`, `0fb0734a…`, `ef6b8770…`, `912dd47a…`, `23ce5f93…`, `7783ab01…`, `989c02de…`, `aeeca90d…`, `c401043b…`, `e5ca74bb…` | conformes à l'en-tête ; onze compagnons de `contre-lecture-v10/` conformes |
| rapport v11 (`d654dea6…`) | conforme, **dans le bac à sable seulement** | `contre-lecture-v11/` absent du dossier (CV12-2) |
| `src/controle_ia/bases/sequentiel.py` | `35a09834…11ba8` | conforme |
| `…/pari-de-signe/conception-pari-de-signe-v3.md` (CV3-9) | `1518a12f…db14` | conforme (sous `brouillons/canal-reprise-releve-v1/envois/`) |
| `docs/notes/collisionneur-mesures-fortes-v1/synthese-mesures-fortes-v1.md` | `bed9107b…` cité « sur `main` » | **non vérifiable ici** (absent de ce worktree et de l'arbre principal local ; `git` interdit) ; conforme sur `origin/main` selon les contre-lectures v1, v3, v5 et v6 |

## 1. Fermeture de CV11-1 à CV11-3

| constat | état | où et pourquoi |
|---|---|---|
| CV11-1, premier point : `LECTURE_SEULE` mourait en silence (code 1) quand la note n'était pas scellée | **fermé** | Garde isolée `garde-lecture-seule-v12.sh` en `if … fi` à sortie explicite (0 ou 7, message dans les deux cas), dernière commande de la branche (séquence, ligne 52) ; branche REEL finie par `printf` (ligne 47), REPETITION par le test (ligne 55). Vérifié : seize cas, dont le cas sain → 0 avec journal complet et note scellée, second appel → 7 sans rien réécrire (section 2). Test déposé (R5) de bout en bout, lancé par la répétition (ligne 55) : vérifié en le lançant (code 0) et en relisant son journal dans ma répétition rejouée. |
| CV11-1, second point : une lecture déjà scellée n'était pas vérifiée avant la note (cas G ter) | **fermé dans la séquence, non couvert par le test déposé** (CV12-3) | Séquence, lignes 100 et 101 : `verifier` si le compagnon existe, sinon lecture refaite en `.partiel` puis renommée et scellée. Vérifié : G (lecture intacte → note refaite, lecture et compagnon intacts) ; G ter (un octet ajouté → « ARRÊT : … empreinte … ≠ scellée », code 1, **aucune note**) ; lecture présente non scellée → refaite à l'identique. Texte, ligne 60 : « vérifie la lecture déjà scellée avant d'en tirer la note (CV11-1) » : exact. |
| CV11-2 (a) `effectifs-reel-v10.json` dans la commande (1) | fermé | lignes 251 et 252 : `effectifs-reel-v12.json` ; la séquence écrit et lit le même nom (lignes 81, 82, 88). |
| CV11-2 (b) `**` orphelin ; décompte des contre-lectures | fermé | ligne 4 : « Pour mémoire, la v11 remplaçait la v10 (…), et la v10 la v9 (…) », sans `**` orphelin ; ligne 5 : « selon les contre-lectures précédentes » ; titre : « après onze contre-lectures » (dix rapports et le complément : la même convention qu'en v11, « dix »). |
| CV11-2 (c) commit du script | fermé | lignes 32 et 33 : « inchangé depuis la v8 (commit `32de42f2`) ; les v9 à v12 ne touchent que la lecture, la rédaction et la séquence, dans le commit qui porte ce texte ». |
| CV11-2 (d) durée | fermé | ligne 261 : « ≈ 40 à 50 minutes » ; ligne 52 : environ 40 minutes pour l'étape (2), environ 10 pour la table si E ≠ 60 : cohérent. Mesuré : 1 min 0 s pour 5 sondes (dont 30 s de tests fixes), 8 min 44 s avec la table. |
| CV11-2 (e) « dixième » | fermé | ligne 407 : « neuvième sous-agent neuf ». |
| CV11-2 (f) provenance du fichier de répétition | **fermé, mais la phrase ajoutée est fausse pour la v12** (CV12-1) | ligne 62 : « une copie de ce fichier … est le chemin lu » ; or `repetition-v12/sortie-reelle-v12.json`, `manifeste.donnees`, et la note déposée (ligne 3) disent `…/mesure-unanime-v1/synthetique-format-reel-repetition.npz`, le fichier déposé. |
| CV11-2 (g) « exercée sur l'état déposé » | fermé | ligne 63 : « exercées par leurs tests déposés sur un état planté qui reproduit l'état déposé » ; ligne 56 : « pour que les gardes soient exercées par leurs tests déposés » (CV11-3 (f) fermé par l'alignement du texte sur le comportement). |
| CV11-3 (a) docstrings ; `--date` | fermé (reste cosmétique, CV12-4) | lecture v8 : « préenregistrement v12 … v12 » (ligne 1), usage `lecture_mecanique_v8.py` (ligne 15) ; essai v8 : « lecture mécanique v8 », usage v8, charge `lecture_mecanique_v8.py` ; rédaction v6 : `lecture_mecanique_v8.py` (ligne 1), usage v6 (ligne 6), `--date` **obligatoire** (ligne 30 ; vérifié : la séquence le passe, lignes 108 et 109). |
| CV11-3 (b) `utcnow()` | fermé | séquence, ligne 108 : `datetime.datetime.now(datetime.timezone.utc)` ; aucun `DeprecationWarning` dans mes journaux. |
| CV11-3 (c) `rm …interdit-ecrasement` | fermé | ligne 37 : `sceller` sans `rm` (commentaire ligne 36) ; le module est idempotent et refuse une autre empreinte (`sortie-scellement-idempotence-v1.txt`). |
| CV11-3 (d) `MESURE_INSTANCE` en répétition | fermé | ligne 63 : forcé à « répétition générale (aucune instance réelle) » ; vérifié avec `MESURE_INSTANCE=x` dans l'environnement : la note dit l'étiquette de répétition. |
| CV11-3 (e) table en vigueur scellée après la sortie | fermé | ligne 91 : écrite et scellée à l'étape (1), avant la ligne 94 ; journal E = 52, lignes 19 à 22. |
| CV11-3 (f) garde non lancée en répétition | fermé par le texte | lignes 54 et 55 : les deux tests ; texte lignes 56 et 63 alignés. |

## 2. Réponses aux points du brief

**Point 1, `LECTURE_SEULE`** (`scripts/lecture_seule_cv12_v1.sh` → `sortie-lecture-seule-v1.txt`, copie `copie-lecture-seule/`,
sorties complètes `ls-cas*.out` à côté). Seize cas, tous au code attendu, chacun avec son message dans le journal :

| cas | état | code | ce qui est écrit |
|---|---|---|---|
| 0 | sans `MESURE_INSTANCE` | 1 | « MESURE_INSTANCE obligatoire » ; rien |
| A | préenregistrement non scellé | 1 | `GardeArret` ; rien |
| B, C | copie scellée par moi ; sortie absente / non scellée | 6 | « aucune sortie réelle finale scellée » ; rien |
| C bis | sortie scellée puis corrompue d'un octet | 1 | « ARRÊT : sortie-reelle-v12.json : empreinte … ≠ scellée … » ; rien |
| D1 | table en vigueur absente | 1 | message de `cat` ; rien |
| D1 bis | compagnon de la table en vigueur faux | 1 | `sha256sum … FAILED` ; rien |
| D2 | commit ≠ manifeste | **8** | « commit ≠ manifeste de la sortie » ; rien |
| D3 | empreinte des données du manifeste ≠ réelle | 1 | « empreinte des données de la sortie ≠ celle attendue » à l'étape (3) ; un `.partiel` vide de lecture reste (repris au cas H) |
| E | cas sain (artefact) | **0** | lecture et note écrites et scellées ; note « contre-lecture v12 (Fable 5.1), artefact, écrite après … Préenregistrement **scellé** (compagnon vérifié) … » ; aucune mention « RÉPÉTITION » (commit ≠ `repetition-generale`) |
| F | second appel | **7** | « la note … est déjà scellée (R12) … rien à reprendre » ; les quatre fichiers inchangés (empreintes avant/après) |
| G | note et compagnon retirés, lecture scellée intacte | 0 | note refaite ; lecture et compagnon intacts (date 2000-01-01 conservée) |
| **G ter** | lecture scellée puis corrompue d'un octet, note retirée | **1** | « ARRÊT : lecture-mecanique-reelle-v12.json : empreinte … ≠ scellée … » ; **aucune note** |
| G quater | lecture présente non scellée (coupure entre `mv` et `sceller`) | 0 | lecture refaite **identique à l'octet**, scellée ; note écrite |
| H | lecture absente, `.partiel` laissé | 0 | lecture refaite identique ; `.partiel` disparu |
| I | note présente non scellée | 0 | note refaite et scellée |

Témoin extrait dans ce dossier : pose 1 → 0, pose 2 → 1 (la séquence en fait un code 3), garde isolée ensuite → 3. La garde
isolée en direct (`sortie-garde-lecture-seule-directe-v1.txt`) : sans argument → 1 avec message ; note absente → 0 ; compagnon
présent → 7. Le test déposé (`sortie-test-lecture-seule-v1.txt`) : 30,2 s, code 0, ne laisse rien dans le dossier.

**Point 2, CV11-2** et **point 3, CV11-3** : tableau de la section 1. `diff lecture_mecanique_v7.py lecture_mecanique_v8.py` :
lignes 1, 2 et 15 (docstring) seulement.

**Point 4, R1** (`scripts/sections_v11_v12_v1.py` → `sortie-sections-v11-v12-v1.txt`) : Hypothèse (5 757 caractères),
Prédiction (3 851), Métrique (5 587), Seuil (3 205), Critères (4 940), Liste d'arrêt (820) : **identiques au bit près**. Le Plan
d'analyse change par les noms (`effectifs-reel-v12.json`, `sortie-reelle-v12.json`, `lecture_mecanique_v8.py`,
`rediger_note_lecture_v6.py`, `note-lecture-mecanique-v12.md`, `commandes-lecture-reelle-v12.sh`,
`journal-lecture-reelle-v12.log`) et « ≈ 40 à 50 minutes ». Aucune hypothèse, prédiction, seuil ni verdict n'a bougé.

**Point 5, répétition** (`repetition-rejouee-v12.log`, `comparaison-repetition-v1.txt`, début 04:54:27 UTC) et **branche
E ≠ 60** (`repetition-E52-v12.log`, `sortie-E52-resume-v1.txt`, 04:56:29 → 05:05:13 UTC) : voir le verdict. Verdicts de ces
essais du code, sans valeur de résultat : à E = 60, M1 confirmé, M2 attendu, M2 ter (1) avec Ville à 0,050, M3 tenu, M4
confirmé (excès 0,047), première ligne ; à E = 52, M1 non concluant, M2 ter (1), M3 tenu, M4 confirmé. Pour information, sans
constat (déjà dit en v9, v10, v11) : la feuille (1) de la répétition se joue à une alerte près (0,050 ≤ 0,05).

**Point 6, le fond** (`scripts/verif_cv12_v1.py` → `sortie-verif-cv12-1_arbre-v1.json`, `-2_bornes-`, `-3_exces_M4-`,
`-4_pas_fixe-`, `-5_chiffres-`) :
- **Arbre de M2 ter** : le Seuil réécrit depuis le texte (lignes 216 à 230), six conditions binaires (Ville réelles ≤ 0,05 ;
  bb(D) ≤ 0 ; Ville mélange > α ; bb(D′) > 0 ; Ville pas fixé ≤ α ; bb(dérive) > 0), 64 combinaisons × r₀ ∈ {0,1 ; 0,7} = 128
  lectures : **aucun désaccord** ; les neuf étiquettes du code sont mot pour mot celles du texte ; feuilles atteintes : (1) 64,
  (2a) 16, (2b) 16, (3a) 8, (3b) 8, (4a) à (4d) 4 chacune ; réserve d'incohérence posée exactement quand bb(D) ≤ 0 et bb(D′) > 0 ;
  **même feuille aux deux r₀**. Bornes : 0,05 et 0,05 + 10⁻¹² → (1), 0,05 + 2 × 10⁻⁹ → la suite ; bb(D) = 0 ou 10⁻¹² → ≤ 0 ;
  mélange à 0,05 n'est pas > α ; pas fixé à 0,05 est ≤ α ; bb(dérive) = 0 ou 10⁻¹² → (4d), 10⁻⁹ → (4c). Partition exhaustive et
  disjointe par construction (des « sinon » emboîtés).
- **M1, M2, M2 bis, M3, M4, placebo** aux bornes : M1 médiane 0,06 et bb 0,03 + 10⁻⁹ → confirmé, bb 0,03 → non concluant,
  0,03 → réfuté, 0,03 + 2 × 10⁻⁹ → non concluant ; M2 0,075 → attendu, 0,075 − 2 × 10⁻⁹ → audit ; M2 bis r₀ = 0,3 et borne
  haute 0 → audit « RÉFUTÉE », 10⁻⁹ → tenu, r₀ = 0,5 → aucune réfutation, écart 0,05 → conforme, 0,05 + 2 × 10⁻⁹ → hors table ;
  M3 cellule 0,10 → tenu fragile, 0,10 + 2 × 10⁻⁹ → audit, 0,08 → tenu, 0,08 + 2 × 10⁻⁹ → fragile, 0,02 → tenu, 0,02 − 2 × 10⁻⁹
  → fragile ; cellule (médiane 0, q3 0) → audit, q3 > 0 → aucune ; bras à zéro → réserve, pas d'audit ; **M4** excès 0,02 ou
  0,02 + 10⁻¹² → non concluant, 0,02 + 2 × 10⁻⁹ → confirmé ; bb 0 → non concluant, 10⁻⁹ → confirmé ; maximum 0,08 → confirmé,
  0,081 → non concluant ; excès 0 ou −10⁻¹² → réfuté ; maximum 0,10 → non concluant, 0,10 + 2 × 10⁻⁹ → audit, à r₀ = 0,5
  aussi ; r₀ = 0,5 → non lisible, 0,5 − 2 × 10⁻⁹ → confirmé ; placebo écart 0,05 → mêmes médianes, 0,05 + 2 × 10⁻⁹ → audit, sur
  le maximum du bras aussi.
- **Ligne de lecture** : première ligne seulement si M1 confirmé **et** M4 confirmé **et** aucun audit ; un audit (M3, M2 bis
  réfutée, placebo) fait passer la ligne à « AUDIT R4 avant toute lecture » même avec M1 et M4 confirmés ; M3 fragile seul ou
  M2 bis hors table seul laissent la première ligne ; M1 non concluant ou réfuté → « voir les lignes des critères » ; r₀ ≥ 0,5 →
  « M4 non lisible ; M2 ter porte le résultat ». **Aucun faux « confirmé », aucun faux blocage.**
- **Excès apparié de M4**, recalculé par sonde avec `un_passage` (mêmes graines : plis `SeedSequence(20261028)` enfant 0,
  effets `(20, 1)` et `(0, 1)`) sur le fichier de la répétition : excès par sonde 0,0763 ; 0,0473 ; 0,0425 → médiane **0,047333** =
  `M4_exces_apparie.exces` de la sortie déposée ; quantité 0,1025, quantité à τ = 0 0,050, maximum 0,01333, différence des
  médianes 0,0525 : tous égaux à la sortie ; la lecture lit bien `exces` (pas la différence des médianes) ; un défaut de niveau
  commun (+0,03 sur les deux termes) laisse l'excès inchangé.
- **Mélange à pas fixé** (E = 60, longueurs 5 à 10, une action invalide plantée au pas 3 d'un épisode sur sept) : marges par
  pas et masque gardés **exactement** ; effet épisode r₀ ≈ 0,25 → −0,004 sur le pas fixé, −0,022 sur le mélange ; dérive de 0,3
  par pas : moyenne par pas identique sur le pas fixé (−0,06 … 2,76), aplatie sur le mélange (≈ 1) ; rien : r₀ ≈ 0 partout ; la
  garde `verifier_scores_invalides` lève sur l'artefact (score sur une action invalide).
- **Gardes et refus** (`sortie-gardes-refus-v1.txt`, `sortie-test-gardes-v12.json`) : `--test-gardes` quinze entrées (quatorze
  gardes et `correlation_saine` = 0,171) ; onze refus du mode réel, **0 octet sur la sortie standard** : effectifs sans
  empreinte, empreinte fausse, `--tirages 5`, `--bootstrap 300`, `--tirages 5` avec `--effectifs-seulement`, sans `--commit`, sans
  `--sondes-placebo`, effectifs (4, 2) et (3, 1), `--reel` avec `--synthetique`, chemin inexistant ; le cas sain écrit 807 octets
  identiques aux effectifs déposés, sans aucun taux.
- **Chiffres** : 1 − 0,99⁵⁰ = 0,395 ; 0,0725 (T uniforme de 5 à 10) ; 0,0773 (T = 8) ; rang 38 et 2/40 = 0,05 pour K = 39 ;
  54 = 15 + 39 ; Ville à τ = 0 : 0 ; 0,033 ; 0,083 ; 0,133 ; à τ = 2 : 0,1375 à 0,1521 (« 0,138 à 0,152 ») ; M2 bis : 0,138 ;
  0,104 ; 0,065 ; 0,019 ; excès : 0,1429 ; 0,0732 ; 0,0274 ; 0,0059 ; quantité brute : 0,1937 ; 0,1238 ; 0,0748 ; 0,0545 ;
  maximum : 0,0192 à 0,0263, soit 0,38 à 0,53 L (« 0,4 à 0,5 L » : arrondi acceptable) ; interpolation à r₀ = 0,196 : excès
  0,0746, Ville 0,0327, M2 bis 0,1049 (la note déposée dit 0,075, 0,033, 0,105). La table n'affirme pas excès = différence des
  médianes (0,1471 ; 0,0738 ; 0,0282 ; 0,0078) : c'est bien la médiane des différences qui est lue.

**Point 7, empreintes et compagnons** (`sortie-empreintes-v1.txt`) : voir le tableau.

**Point 8, règle de contenu** : aucune occurrence de « tromper », « échapper », « contourner », « déjouer », « éviter la
détection », « saboter », « dissimuler », « leurrer » ; chaque énoncé M1 à M4 est une propriété de lois de probabilité (taux de
fausses alertes de l'agrégateur sous indépendance, sous dépendance naturelle, sous effet épisode injecté sur des épisodes
honnêtes ; niveau d'un calibrage conforme) ; l'« effet injecté » est un bruit ajouté à des scores honnêtes pour mesurer un
niveau, jamais une conduite d'agent. Aucune phrase ne franchit la ligne.

**Point 9, R8** : aucun « inédit » ; les « premier » du texte sont « premier plan », « deux premiers moments », « 15 premiers »
épisodes, « le premier » contre-lecteur ; « nouvelle » n'apparaît que dans « version nouvelle » (R12). Rien n'est affirmé sans
antécédent.

## 3. Constats

### CV12-1 : la provenance du fichier de répétition, corrigée pour la v11, est fausse pour la v12 (texte, mineur)

- **Où** : en-tête, ligne 62 : « (`447dc136…`, 3 sondes réelles, 2 placebo, E = 60 ; une **copie** de ce fichier, de même
  empreinte et hors de `donnees/`, est le chemin lu, CV11-2(f)) ».
- **Problème** : `repetition-v12/sortie-reelle-v12.json`, `manifeste.donnees`, et la note déposée (ligne 3) donnent
  `/home/claude/canal-conv-audit-n04/brouillons/canal-reprise-releve-v1/envois/mesures-fortes-v1/mesure-unanime-v1/synthetique-format-reel-repetition.npz` :
  le fichier **déposé lui-même**, pas une copie. La phrase décrit la répétition v11 (qui lisait une copie dans un bac à sable).
  Sans effet sur la science ni la plomberie (même empreinte, hors de `donnees/`), mais un texte scellé ne doit pas dire d'un
  dépôt ce que son manifeste contredit (R6).
- **Correction** (v13) : « le fichier déposé lui-même, hors de `donnees/`, est le chemin lu (manifeste) », ou retirer la
  parenthèse. Toute modification du texte change son empreinte, que la note de répétition cite : refaire la répétition (1 minute).

### CV12-2 : `contre-lecture-v11/` cité mais absent du dossier (dépôt, mineur)

- **Où** : ligne 416 : « `contre-lecture-v11/rapport-contre-lecture-mesure-unanime-v11.md`, `d654dea6…` ».
- **Problème** : le dossier n'existe pas (R11 : vérifié par `ls` et `find` sur tout l'arbre de travail) ; le rapport v11 et ses
  scripts et sorties ne sont que dans le bac à sable de son auteur (`/tmp/…/scratchpad/contre-lecture-mesure-unanime-v11/`,
  empreinte conforme). Les rapports v1 à v10 sont versés, et le texte en fait un chemin opposable.
- **Correction** : verser `contre-lecture-v11/` (rapport, compagnon, `scripts/`, sorties) et `contre-lecture-v12/` (ce rapport)
  dans le commit qui porte le texte, comme pour la v10 (reste de CV10-3).

### CV12-3 : le test déposé de `LECTURE_SEULE` ne couvre pas la vérification de la lecture déjà scellée (test, mineur)

- **Où** : `test-lecture-seule-v12.sh`, cas (B1) à (B4) ; séquence, lignes 100 et 101 ; texte, ligne 60 (« vérifie la lecture
  déjà scellée avant d'en tirer la note (CV11-1) »).
- **Problème** : la garde « lecture scellée → `verifier`, jamais refaite » n'est exercée ni sur son cas sain ni sur un artefact
  par le test déposé (R5) ; (B3) sort en 7 à l'étape 0, avant d'y arriver. Vérifié à la main : conforme (G, G ter, G quater).
- **Correction** (v13) : après (B3), ajouter (B3 bis) `rm note…md note…md.sha256 ; emp=$(sha256sum lecture…json)` → appel →
  attendu 0, note scellée, lecture inchangée ; puis (B3 ter) `rm note…md note…md.sha256 ; printf ' ' >> lecture…json` → appel →
  attendu ≠ 0 et `[ ! -e note…md ]` ; restaurer la lecture avant (B4). L'empreinte du test change, donc l'en-tête (ligne 48) et
  le compagnon vérifié par `compagnons`.

### CV12-4 : docstring de la rédaction v6 (cosmétique)

- **Où** : `rediger_note_lecture_v6.py`, ligne 1 : « à partir de la lecture mécanique (`lecture_mecanique_v8.py`) — version 6
  (CV11-3) : --instance et --date obligatoires ; docstrings » puis ligne 2 « et de la sortie réelle : la note reprend… » ; ligne 6 :
  « Usage : … --prereg FICHIER --commit SHA --heure HH:MM:SS > note.md ».
- **Problème** : l'insertion coupe la phrase ; l'usage omet `--instance` et `--date`, pourtant obligatoires (et `--table`). Sans
  effet : `argparse` refuse avec un message, jamais en silence.
- **Correction** : déplacer la mention de version en fin de paragraphe ; compléter l'usage.

Remarques sans constat : (i) une coupure entre `mv` et `sceller` de la sortie finale (ligne 95, quelques millisecondes) laisse
une sortie complète non scellée, que `LECTURE_SEULE` refuse (code 6) et que le témoin et la trace `sortie-reelle-v12.json`
rendent irrécupérable sans version nouvelle : c'est exactement ce que le texte dit (« interrompue avant la sortie finale
scellée → version nouvelle »), au prix d'une seconde lecture des données ; dit ici pour qu'on ne s'en étonne pas. (ii) Lancer
`REPETITION` après l'exécution réelle effacerait et régénérerait `repetition-v12/` (ligne 62 de la séquence) : le dépôt est
dans le commit, et le témoin ne protège pas ce sous-dossier ; sans conséquence sur l'unique exécution. (iii) La note de
`LECTURE_SEULE` porte l'instance de la reprise, pas celle du lancement réel : ni le manifeste de la sortie, ni le témoin
(ligne 47 : heure et commit), ni le journal (lignes 68 et 75 : heure, mode, commit) n'enregistrent `MESURE_INSTANCE` ; en cas
de reprise, l'instance du lancement réel ne vivrait que dans la passation. Une ligne `printf` de plus dans le témoin
suffirait, si on y tient ; ce n'est pas demandé par le texte.

## 4. Tableau des énoncés

| énoncé | énoncé lisible et unique ? | preuve / loi qui le porte | seuil gelé, lu mécaniquement ? |
|---|---|---|---|
| M1 (par action ≠ par épisode) | oui (lignes 93 à 96) | 1 − (1 − τ_a)^T sous indépendance : 0,0725 et 0,0773 recalculés ; décroissance sous corrélation (M1 bis) | 0,06 / bb 0,03 / 0,03 : bornes vérifiées ; identique v11 → v12 |
| M2 (contrôle du mécanisme) | oui | table gelée τ = 2 : 0,1375 à 0,1521 (recalculé depuis la table) ; « vrai par construction, ne dit rien de P3 » dit | 0,075 : borne vérifiée ; audit qui suspend |
| M2 bis (secondaire) | oui | table : 0,138 ; 0,104 ; 0,065 ; 0,019 ; interpolation vérifiée (0,1049 à r₀ = 0,196) | conforme/hors table ± 0,05 ; réfutée seulement si r₀ < 0,5 et borne haute ≤ 0 → audit : vérifié |
| M2 ter (la lecture sur P3) | oui, une seule définition (lignes 216 à 230) | neuf feuilles exhaustives et disjointes ; D = D′ + dérive sur le même tirage (script, lignes 556 à 568) ; mélange et pas fixé vérifiés par simulation | arbre : 128 lectures sans désaccord, étiquettes mot pour mot, bornes à 10⁻⁹, r₀ jamais condition |
| M3 (contrôle, échangeabilité) | oui | niveau exact (K + 1 − rang)/(K + 1) = 0,05, L pondéré ; 24 cellules listées | B = max(2 L ; 0,10), fragile ]1,6 L ; B] ou < 0,4 L, cellule à zéro : bornes vérifiées ; audit qui suspend |
| M4 (dépendance non vue : sommes, pas le maximum) | oui | excès apparié = médiane des différences par sonde, recalculé (0,0473 = sortie) ; table 0,143 … 0,006 ; maximum 0,019 à 0,026 ≤ α | excès > 0,02 et bb > 0 et max ≤ 0,08 ; réfuté ≤ 0 ; non lisible r₀ ≥ 0,5 ; audit max > 0,10 à tout r₀ : bornes vérifiées |

## 5. Mes scripts et sorties

Tout est dans `/tmp/claude-0/-home-claude/c5a45195-121d-5962-9d0a-4896cc046231/scratchpad/contre-lecture-mesure-unanime-v12/`.
Chaque script et chaque sortie a un compagnon `.sha256`. Les copies du dossier (`copie-dossier/`, `copie-dossier-E52/`,
`copie-lecture-seule/`), `depose-repetition-v12/` (copie des fichiers déposés pour comparaison), `donnees-repetition/`,
`donnees-E52/`, `gardes-tmp/` et `scellement-tmp/` sont de travail et ne reçoivent pas de compagnon (la séquence scelle
elle-même ce qu'elle produit).

| fichier | contenu |
|---|---|
| `heure-debut.txt`, `heure-debut-repetition.txt`, `heure-debut-E52.txt` | heures `date -u` relevées dans des appels séparés |
| `sortie-empreintes-v1.txt` | empreintes sur disque de tout ce qui est cité ; `sha256sum -c` de tous les compagnons (dossier, `repetition-v12/`, `contre-lecture-v10/`) |
| `scripts/sections_v11_v12_v1.py` → `sortie-sections-v11-v12-v1.txt` | comparaison section par section v11 / v12 (R1) |
| `sortie-test-garde-trace-v1.txt` | test déposé de la garde témoin ; garde en place (0) ; depuis `repetition-v12/` (3) |
| `sortie-test-lecture-seule-v1.txt` | test déposé de `LECTURE_SEULE`, lancé depuis la copie (30 s, code 0) |
| `scripts/lecture_seule_cv12_v1.sh` → `sortie-lecture-seule-v1.txt`, `ls-cas*.out` | seize cas de `LECTURE_SEULE` sur `copie-lecture-seule/` (artefact marqué par `LISEZMOI-ARTEFACT.txt`) |
| `sortie-garde-lecture-seule-directe-v1.txt`, `sortie-scellement-idempotence-v1.txt` | garde isolée en direct ; idempotence et refus d'écrasement du module de scellement |
| `repetition-rejouee-v12.log`, `comparaison-repetition-v1.txt` | répétition rejouée (copie-dossier) et comparaison au dépôt |
| `scripts/ecrire_npz_E52_v10.py` (copie du script de la contre-lecture v10) → `sortie-ecrire-npz-E52-v1.json`, `empreinte-E52.txt`, `repetition-E52-v12.log`, `sortie-E52-resume-v1.txt` | branche E ≠ 60 de la séquence v12 en répétition |
| `scripts/verif_cv12_v1.py` → `sortie-verif-cv12-1_arbre-v1.json`, `-2_bornes-`, `-3_exces_M4-`, `-4_pas_fixe-`, `-5_chiffres-` (et `sortie-verif-cv12.err`) | arbre, bornes, ligne de lecture, excès de M4 recalculé, mélange à pas fixé, chiffres ; graines `SeedSequence(2810202612, …)` |
| `sortie-gardes-refus-v1.txt`, `sortie-test-gardes-v12.json`, `effectifs-sain.json` | `--test-gardes`, onze refus, cas sain des effectifs |
| `essai-lecture-mecanique-v8-reproduit.json` | essai brut de la lecture v8 reproduit à l'octet (`0745cc20…`) |

Empreinte de ce rapport : dans `rapport-contre-lecture-mesure-unanime-v12.md.sha256`, à côté (un fichier ne peut pas contenir sa
propre empreinte).
Durée : 2 heures 0 minute 47 secondes d'horloge, de 04:43:46 à 06:44:33 UTC — dont une période sans aucune commande entre
05:05 et 06:36 UTC (dates de modification de mes fichiers, à l'heure de Paris dans `ls`) : le travail effectif tient dans
04:43 → 05:05 et 06:36 → 06:44 UTC, la branche E ≠ 60 comprise.

Fin : 2026-10-28 06:44:33 UTC (`date -u`, relevé dans un appel séparé avant l'écriture de cette ligne).
