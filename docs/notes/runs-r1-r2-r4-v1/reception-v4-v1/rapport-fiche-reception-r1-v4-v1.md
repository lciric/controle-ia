# Rapport : fiche de réception v4 de R1 et son vérificateur — v1

- Rédacteur-développeur neuf (sous-agent, Claude Opus 5.5), pour conv-audit ; consigne
  `docs/notes/runs-r1-r2-r4-v1/consigne-fiche-reception-r1-v4-v1.md` (compagnon vérifié conforme au début). Commencé le
  4 novembre 2026 à 23:28 UTC (`date -u`) ; conteneur redémarré deux fois (vers 23:45 et 00:12 UTC ; fichiers retrouvés sur
  disque, rien refait) ; fini le 5 novembre vers 01:05 UTC. Je n'ai écrit ni l'addendum v4, ni son code, ni les fiches précédentes.
- Seul réseau : `git fetch origin refs/heads/prep/r1-relance-v4:refs/remotes/origin/prep/r1-relance-v4` (937f1317 →
  5bd62a00 ; l'arbre `/home/claude/wt/r1-v4` était resté à 937f1317). Aucun commit, aucun `.sha256`, aucun fichier
  existant modifié, aucune sortie de la session 2 ni contenu du témoin lu (noms et empreintes seulement), rien sous
  `donnees/` ni `/home/claude/coffre-*`, aucun modèle, aucune dépense.

## 1. Fichiers produits (dossier `docs/notes/runs-r1-r2-r4-v1/reception-v4-v1/`)

| fichier | rôle | sha256 |
|---|---|---|
| `fiche-reception-r1-v4-v1.md` | la fiche (à contre-lire puis sceller par conv-audit) | `50d5a895ac312b8537b12b0893a132dca75be60eba6a156a56f2bbf92e4f0b13` |
| `verifier_reception_r1_v4_v1.py` | vérificateur mécanique (`bloc`, `verifier`) | `3ea2352d57c7283420591fcbb8f6975aa4533fc2ee49257b1bb8703a2f4e93a4` |
| `test_verifier_reception_r1_v4_v1.py` | essais R5 (monde jouet ; garde `textes` sur les vraies pièces) | `23b7241edce90e37f056491159785d7f050a7e538bd1cd99f40bc5547fbe076d` |
| `banc_mutations_reception_r1_v4_v1.py` | banc de mutations | `5ff74a6e97d3228c53a99bc36883155dc42de120a9728be854b57be8db538f14` |
| `essais-verifier-reception-r1-v4-v1-sortie.txt` | sortie des essais | `0c6ca40d1b80faf59a587d20b7adc911507d2e2f20c073418f2cda213c89c2e3` |
| `banc-mutations-sortie-v1-partie-1.txt` | sortie du banc, partie 1 | `a65903f8b1be548192abe13cec14370b67cabf5cd58eaa6ce9e2f7e4c6c1cf80` |
| `banc-mutations-sortie-v1-partie-2.txt` | sortie du banc, partie 2 | `70a010faa50d0a47236424e3848ea58ce0afebd51d2a8d5be4e6daaab4f5be54` |
| `banc-mutations-sortie-v1-partie-3.txt` | sortie du banc, partie 3 | `e9b1b84eae574ca34192c18cc052b8a7ae4ad7873c7434f162bf6e409b8e429e` |
| `banc-mutations-sortie-v1-partie-4.txt` | sortie du banc, partie 4 | `da010a41d89d165440197ec0c5661d33246144230e4a254b1cc2001302516162` |
| `banc-mutations-sortie-v1-partie-5.txt` | sortie du banc, partie 5 | `f99e870794907e8532d09f99fd7f1501cd9bacaa9e3b67f150378f8f1c16569c` |

Ce rapport n'est pas dans la table (il ne peut citer sa propre empreinte). Aucun compagnon `.sha256` écrit (interdit de la consigne) : le scellement revient à conv-audit.

## 2. Ce que fait le vérificateur

`verifier_reception_r1_v4_v1.py verifier` rejoue, sur une copie récupérée (arbre du commit de versement, dépôt qui porte
ce commit, la branche source et 5bd62a00), toutes les attentes de la fiche, dans l'ordre de sa section 8 ; il lit les
JSON par clés nommées (filtre `filtrer` pour le rejeu, `extraire_reparation` pour la réparation, quatre clés du témoin),
les `.npz` par leurs seuls en-têtes `.npy` (`zipfile` + `ast.literal_eval` de l'en-tête ; aucun tableau chargé), et ne
compare les grandeurs de couverture qu'entre pièces, sans les afficher. Codes : 0 conforme, 2 arrêt nommé, 3 course
arrêtée (réception de l'arrêt seulement). `bloc` imprime le bloc d'attendus ; la fiche le porte à l'identique (essai
`test_bloc_de_la_fiche_reelle_egal_au_script`) et le mode réel refuse tout autre bloc.

## 3. Essais

`timeout 900 nice -n 10 .venv/bin/python -m pytest -q -p no:cacheprovider --basetemp=<scratchpad>/essais
docs/notes/runs-r1-r2-r4-v1/reception-v4-v1/test_verifier_reception_r1_v4_v1.py` : **118 passés, 0 sauté, 0 en échec**
(37 s ; numpy 2.4.6, pytest 9.1.1 ; sortie : `essais-verifier-reception-r1-v4-v1-sortie.txt`, avec les empreintes du
script, des essais et de la fiche).

- Cas sains (3) : monde jouet complet → « RÉCEPTION CONFORME », les 22 gardes nommées ; branche source nommée par
  `refs/remotes/origin/…` ; filtre des clés lues (aucune clé de `INTERDITS` dans `CHEMINS_LUS_REJEU`).
- Mode réel (2) : `test_mode_reel_textes_scelles_reels` — sur le dépôt de travail, la fiche au bloc égal aux constantes
  passe `fiche`, `runs`, `textes` sur les **vraies** pièces de `5bd62a00` (15 empreintes, compagnons, deux empreintes
  canoniques, diff 937f1317 → 5bd62a00 = les quatre fichiers du témoin, table v4 absente), puis s'arrête à
  `versement` (commit inexistant) ; `test_bloc_de_la_fiche_reelle_egal_au_script` — le bloc de la fiche égale
  `ATTENDUS`.
- Artefacts (110) : au moins un par attente et par contrôle (fiche non scellée, sceau faux, empreinte annoncée autre,
  format, jouet/réel croisés, bloc réel altéré ; pièce, compagnon, configuration canonique, diff du témoin, table v4 au
  commit du témoin, scellement non parent ; versement en trop, en moins, traces, existant modifié, chemin attendu
  réécrit, fusion, commit à deux parents de même arbre, commit absent ; octets source ≠ versé, témoin ≠ 5bd62a00,
  arbre ≠ commit, branche source d'un autre nom ; présence ; compagnon ; témoin (commit, commande, étape,
  rattachement) ; réparation (texte, commit, configuration, arbre sale, entropie, non décisive, `run_id`, version, voie,
  témoin cité, lots, ordre, consigné mal nommé ou d'empreinte fausse, table v3) ; table (sérialisation, version,
  réparation citée, table v3, témoin, clé en trop, métadonnée, entrée v3, ordre, méthode, `non_resolus_v4`, comptes,
  `corrections_verifiees`, comptes de base) ; chaîne locale (retrouvée rétrogradée en `non_resolu` dans une table
  cohérente avec elle-même — l'artefact de V4-E5 —, sceau non cité) ; commit du rejeu (hors branche, au témoin, au
  scellement, greffé de même arbre, chemin de plus, table réécrite après le rejeu) ; rejeu (commande v3, table citée
  d'avance, rattachement, verdict, table comparée, provenance v2, version, empreinte dite citée, `non_conformes`,
  actions, règle B, cinq cohérences avec la table, fichiers) ; `.npz` (tableau en trop, manquant, principal en float32,
  hors forme, ordre Fortran, type d'un commun, type d'identité, scores de P3 absents ou d'autre empreinte) ; recalcul
  (absent, deux lignes, inégal à l'octet, autres pièces, autres comptes, arbre absent, `src/` autre, configuration
  autre, table autre) ; courses arrêtées (rejeu « non conforme » → code 3, motif hors liste → code 2, rejeu absent →
  code 3, rejeu absent sans résultat de réparation → code 2, réparation arrêtée → code 3, course arrêtée avec un chemin
  hors des runs → code 2).
- Toutes les sorties (sain et artefacts) sont passées au crible de sentinelles posées sur les clés interdites (valeurs de
  P-R5, lectures du témoin et de la réparation, traces) : aucune n'apparaît.

## 4. Banc de mutations

`banc_mutations_reception_r1_v4_v1.py`, joué en cinq parties (chacune sous `timeout 900`, deux travailleurs, dossiers
d'essai effacés après chaque mutant), sur le script `3ea2352d…` et les essais `23b7241e…` : **105 mutants, tous tués**,
témoin (script non muté, 118 passés) conforme dans chaque partie ; aucune mutation inapplicable.

| partie | motifs | mutants | issue |
|---|---|---|---|
| 1 | fiche, runs, textes, versement | 22 | tous tués |
| 2 | octets, presence, compagnon, temoin | 8 | tous tués |
| 3 | reparation, table, chaine-locale | 28 | tous tués |
| 4 | commit-rejeu, verdict, table-comparee, provenance, comptes, coherence-table, fichiers | 19 | tous tués |
| 5 | npz, recalcul, filtre, generique (gardes des manifestes, rattachements, arrêts) | 28 | tous tués |

Passes d'exploration (sorties non gardées ; la première, `banc-mutations-sortie-v1-partie-A.txt`, NON CONFORME, a été
effacée de l'arbre — versée en instantané au commit `185191c8` par la session) : 9 + 9 + 4 + 7 survivants, traités ainsi
— **artefacts ajoutés** pour les contrôles non éprouvés (format de fiche, commit du témoin absent, scellement non parent,
pièce au compagnon complice, commit de versement à deux parents de même arbre, chemin attendu réécrit, course arrêtée
avec chemin hors des runs, branche source de même contenu et d'autre nom, version de réparation, consigné mal nommé,
rejeu absent sans réparation, cinq artefacts de table, deux de commit du rejeu, ordre Fortran, recalcul à deux lignes et
à configuration autre, `run_id` du manifeste) ; **contrôles redondants retirés** (chacun impliqué par un autre, dit en
commentaire au code) : `traces/` séparé (compris dans l'égalité des chemins), « compagnon sans fichier » (impossible
par construction), existence du commit du rejeu (comprise dans `merge-base`), table citée par la configuration du rejeu
et `config` égal au fichier (compris dans l'empreinte canonique et la garde `textes`), tableaux d'identité des scores
de P3 (compris dans le contrôle de forme `[n]`).

## 5. Dix points pour un contre-lecteur neuf

1. **Commits lancés supposés, non vérifiés par moi.** Le vérificateur exige `commit` = `937f1317…` au manifeste du témoin
   et `5bd62a00…` à celui de la réparation (addendum, « Coût et GO » : commit de scellement pour la session 1, commit du
   versement du témoin pour la session 2). Je n'ai pas lu le manifeste du témoin ni la commande de création de la
   session 2 (le registre des dépenses ne cite pas `COMMIT`). Si la session 2 a été lancée sur un autre commit, la
   réception s'arrête (`reparation`) : nœud, fiche nouvelle. À recouper par session-depot avant le scellement.
2. **Commit lancé du rejeu.** Il n'est pas connu d'avance : le script d'instance committe la réparation puis la table
   avant le rejeu, donc `commit` du manifeste du rejeu est un commit de la branche source. La fiche exige qu'il descende
   de 5bd62a00 et n'en diffère que par les 184 chemins de la réparation et de la table, blobs égaux aux versés. Cela
   suppose que l'étape « chaine » ne committe rien (vrai au code : `git commit … || true` sans changement) ; vérifier
   que rien d'autre (fichier non ignoré créé par les essais ou le préchargement) ne s'ajoute à `runs`, `diag`, `prereg`.
3. **Ordre « contrôles avant versement ».** Pour tenir l'ordre de la consigne avec un vérificateur qui lit un commit,
   la fiche fait préparer le commit de versement **localement, non poussé** (étape B), le fait vérifier (C), puis
   pousser tel quel (D) ; conv-audit rejoue le même vérificateur sur la ref récupérée (E). Écart de forme avec la v3
   (versement puis réception) à juger : il est plus strict, mais demande à session-depot de ne pas pousser avant C.
4. **Lecture de couverture par le vérificateur.** Il lit `empreinte_retrouvee` de la réparation, les méthodes de la
   table v4 et, du rejeu, `episodes_non_retrouves_v4`, `actions_non_retrouvees_v4`, `corrections_*`,
   `par_methode_resolution`, `methodes_resolution`, `empreintes_p3.trajectoires_identiques` — pour les comparer entre
   pièces, jamais pour les afficher. Ce sont des propriétés de l'instrument (V4-E2), non des scores, mais la couverture
   par condition entre dans un critère gelé (« sous 0,80 ») : juger si ces comparaisons muettes sont admises avant R13.
   `fidelite_toutes.conformes_longueur` et `contextes_conformes`, fixés en v3, ne le sont plus et ne sont pas lus.
5. **Identité des `.npz`.** Le type des quatre tableaux d'identité n'est pas écrit au parent ; la fiche l'exige égal à
   celui de `scores-p3.npz` (en-têtes seulement, empreinte `968414fc…` vérifiée). L'égalité des valeurs reste aux
   lecteurs des analyses (comme en v3). Les autres types (`<i8`, `|b1`, `<f8`, `<f2`) viennent du code de
   `rejeu_activations_v4` (écriture des `.npz`), non du texte du parent : à recouper.
6. **Chemins versés.** 198 chemins exactement, dont 89 épisodes consignés (`000` à `088`) : suppose que chaque cible est
   consignée une fois (vrai au code : `consigner` par cible dans l'étape « reparation », compteur continu). La table v4
   est versée à `prereg/R1-table-tokenisation-v4.json` sur `calcul/r1-r2-reel-v1` (chemin que cite la configuration v6
   et la commande de recalcul) ; les traces ne se versent pas.
7. **Recalcul de réception.** La fiche donne la commande exacte et l'arbre (`git worktree` à 5bd62a00 plus les trois
   pièces versées et les pièces de P3). Je ne l'ai pas jouée (tokeniseur et pièces de P3 sous `donnees/`, interdits
   ici) ; le vérificateur ne lit que sa sortie JSON et l'arbre `src/` (égal à 5bd62a00, `__pycache__` et `*.egg-info`
   exclus). Sa durée sur processeur n'est pas mesurée ; la commande porte `timeout 900`, à relever si elle ne suffit pas.
8. **Courses arrêtées.** Code 3 pour `arret.json` de la réparation, rejeu absent, ou `arret.json` du rejeu (motif fermé
   « non conforme » / « echec ») ; le vérificateur ne lit rien d'autre de l'arrêt. Le cas « table-v4 ou chaîne arrêtée »
   n'a pas de pièce propre (le script n'écrit pas d'`arret.json` pour ces étapes) : il se reçoit par l'absence du rejeu,
   sans plus de contrôle de la table. À juger si cela suffit pour le nœud.
9. **Ce que le vérificateur ne refait pas.** Il ne revérifie pas les corrections par l'empreinte de P3 (le recalcul et
   le rejeu le font), ni la configuration au-delà de l'égalité au fichier scellé, ni la reprise V4-E16 au-delà du nom
   de la branche source (`-v1` ou `-v2`) : la déclaration de reprise reste à vérifier par la session.
10. **Robustesse de l'outil.** Bibliothèque standard ; `git` en lecture seule ; arrêts nommés au premier écart ; toute
    exception de lecture rend le code 2 (garde `lecture`) ; aucun repli silencieux. Limites : le banc mute les gardes
    (toutes les occurrences ; 105 mutants tués), pas les fonctions d'aide (`chemins_attendus`, `entete_npy`, `blob_fichier`), couvertes
    seulement par le cas sain et les artefacts qui en dépendent ; les essais sont jouets (6 épisodes, T = 2), sauf la
    garde `textes`, jouée sur les vraies pièces de 5bd62a00.
