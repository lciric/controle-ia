# Journal du rédacteur de l'architecture de l'organisme — v1 (final)

- **Rédacteur** : sous-agent neuf de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, modèle Claude Opus 5.5 ; je n'ai écrit
  aucune pièce de l'organisme ni du programme de contrôle.
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-architecture-programme-organisme-v1.md`,
  `7335655c594f41acb78f19fdfddad98af8e2bd7f65e3efbb909b7a855aaacf92` (vérifiée contre son compagnon à 11:59 UTC) ; interdits communs
  v2 `1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f` (vérifiés).
- **Heures** (toutes relevées par `date -u`, 10 novembre 2026) : début 11:59:11 ; jalon 1 scellé 12:12:40 ; partie 1 scellée
  12:24:48 ; partie 2 scellée 12:29:44 ; programme et registre scellés 12:34:23 ; HTML et PDF scellés 12:36:04 ; ce journal écrit
  après le relevé de 12:36:55.
- **Dépense** : aucune. Aucun appel de modèle ni d'interface externe, aucune machine, aucune clé lue, aucune commande d'environnement.
  Aucun commit. Aucune publication (l'outil de page publiée n'a pas été utilisé : interdit 3 et CLAUDE.md).

## 1. Ce qui a été écrit (dossier `docs/notes/rapports-directeur/programme-organisme-complet-v1/`)

| fichier | sha256 | rôle |
|---|---|---|
| `programme-organisme-complet-v1.md` | `34239a541690a9812e007e9390da8b4f37743aa89ac9e8dd87746830b936bfc6` | source du programme (770 lignes) |
| `programme-organisme-complet-v1.html` | `88ff2497dad7d2d10fdb7dbd12fc2656809e7a6406022af1c732251355493cd2` | version lisible, autonome (aucune ressource externe) |
| `programme-organisme-complet-v1.pdf` | `856c2a83ccbf9bfa1be0e9c6777ad01174aa7a57325b1c791268866ae9a8fbe0` | imprimé depuis le HTML ; **25 pages A4** |
| `registre-affirmations-programme-v1.md` | `18e06990c3b1a738b2a6bbf2aae97a78e26cec9bcc361dbed4a7d6c173f52bea` | RA1 à RA133 (RA119 et RA133 réservés), 34 pièces abrégées, annexe de 113 empreintes de modules |
| `journal-programme-v1.md` | (compagnon) | ce journal |
| `jalons-architecture-v1/journal-programme-v1-jalon1.md` | `e96d0f7c941ab02a84170d67818c2c6359f33a57ff4f6663a5b0ccb3f478421f` | jalon 1 : sources lues, cloison |
| `jalons-architecture-v1/programme-organisme-complet-v1-partie1.md` | `978311cc2d23611a0d12b7e59b90b45378c9ffcec614442135f861018842f164` | jalon 2 : sections 0 à 4 |
| `jalons-architecture-v1/programme-organisme-complet-v1-partie2.md` | `2dae55735294ddf3f2b01ab56671f137593a5a4ba8a8f8b249205eae8c12708a` | jalon 3 : sections 5 à 9, annexes A et B |
| `jalons-architecture-v1/md-vers-html-v1.py` | `8e65288ee185ac3c6a0adcd9fbf5052d83861ee6009377c3822116fae1be6ca6` | convertisseur Markdown → HTML écrit pour ce rendu (aucun module Markdown n'est installé) |

**Chaîne de rendu** : `python3 -I jalons-architecture-v1/md-vers-html-v1.py programme-organisme-complet-v1.md
programme-organisme-complet-v1.html "…"`, puis le constructeur scellé de la mère
`docs/notes/rapports-directeur/construire-rapport-pdf-v1.py` (`0d3ad7545d8ecf46e6012a6925eebddb659085656d26731b5dd7121508d83bb6`),
qui pilote le Chromium installé par Playwright sous Node (`/opt/node-tools/node_modules/playwright`), sans réseau, dossier
temporaire dans mon bac à sable ; code de sortie 0. Polices locales (Carlito, Liberation, DejaVu). Un PDF d'essai (même source) a
été regardé à l'écran (pages 1, 2 et 13) avant le rendu final, puis effacé du bac à sable.

## 2. Corrections entre les jalons et la version finale (le jalon n'est jamais réécrit, R12)

1. **Dépense de l'épreuve fraîche du pont** : le jalon 2 (partie 1, § 4.3) portait « 1,11 USD dépensés » ; ce chiffre est celui de
   la relecture de la candidature (GO-2026-11-01-10, R-988), pas de l'épreuve. La dépense de l'épreuve est **1,34 USD sur 5**
   (`registres/depenses.md`, l. 303). Corrigé dans la version finale, avec L4 et L5 complétés (R-986).
2. **Préenregistrement de la boucle réelle** : « à mettre au dessin v65 » (inférence non sourcée) remplacé par « non scellé ; la lecture
   gelée du code v65 suit ses critères, section 8 du brouillon » (rapport du développeur v65, M5).
3. **Registre** : trois numéros de ligne du README public corrigés avant scellement (figure 2 à la l. 188 ; garde « le proposeur
   apprend le goût du juge » à la l. 71) et une ligne de la synthèse N12-N13 (dépense du tour 1 à la l. 29) ; RA128 marqué
   « complément de RA100 ». Contrôle par programme : 130 renvois utilisés dans le programme, tous définis au registre ; aucun renvoi
   réservé utilisé.

Toutes les corrections ont été faites par remplacements exacts, chaque chaîne trouvée une fois (script avec assertion), dans mon bac
à sable puis écrites sous les noms finaux.

## 3. Sources lues après le jalon 1 (le jalon 1 liste les premières, avec empreintes)

| pièce | sha256 | lecture |
|---|---|---|
| `resultats/attaque-goodhart-v2/README.md` du dépôt public | `c549a31b266b6952c9f7fc2922243eab21ca304fe7626099310016f071f8ccbb` | titres et lignes citées (A1 : l. 68-90) |
| rapport du développeur v65 (`origin/prep/organisme-v65-v1`) | `f84c14303eacf87e7e129955d3f9b7ba35fc7504545033c37b66b9c4ad5aff0c` | l. 41, 95, 158 par recherche (configuration `bff138d8…`) |
| note de la session-dépôt `registres/passations/2026-11-10-1114-decision-lazar-enveloppe-120-usd.md` (`origin/claude/upbeat-cray-dmauvv`) | `ddb77ed67196e50bddc4d0a75af7bc1ad05009b60de0af572269aa94bbae9114` | l. 17 par recherche (configuration `995eb918…`) |
| `pont-fiche-loi-v1/pont_v1.py` | `9fb2d9366e7764d4fc810b921e8565ca2dcae9af5f1b30ec8866efeb5d3eb692` | l. 1-52 |
| `docs/notes/organisme-boucle-reelle-v1/code-v65/contre-lecture-code-v65-v2.md` | `c4ddfc7ffd4b5cea1b0eb70e2a08ea551c8a8e8ef6f1a169ef8bebdab976ed03` | l. 145-165 et recherche, **après** le scellement du programme |
| `inventaire-idees-organisme-v5.md` (rédacteur voisin) | `42731234739fa3b8cfb933c49afc2de9817208c5e0554960fa2f21dc89ca445a` | titres et recherche ciblée seulement |
| `sorties-non-lues-v1.md` (rédacteur voisin) | `fd46a13e8e5ca3134e32555887caf128063d053f8df472fcd792fef4f9dffe11` | empreinte seulement |
| `registres/decisions.md` | lignes R-986, R-988, R-1057 (registre de `main` : autre objet que le « R-1057 » de conv-audit cité par `tests_de_mort_v5.py`), R-1099, R-1128 à R-1131, R-1469, R-1471, R-1738, R-1989, R-1994, R-1999, R-2000, R-2024, R-2026, R-2201 à R-2219 | lu ligne à ligne |
| `registres/depenses.md` | l. 236-238, 298-331, 332-350, 393-414 | lignes citées |
| docstrings de tête des 113 modules du pôle (fichiers cloisonnés exclus) | annexe du registre | première docstring |

## 4. Choix et gestes déclarés

- **Cloison** : ni ouverts, ni hachés : `orchestrator/pole/bras_attaque_v54.py`, `reserve_tenue_a_l_ecart_v60.py`, `_v61.py`, leur
  démonstration et leurs essais (exclus de chaque `git grep` et du calcul d'empreintes) ; la l. 202 du README public ; les § 3 bis et
  3 ter du programme de conception v7 ; le dossier `bras-attaque-v1/` de la branche de conv-audit (nom vu dans une liste de dossier) ;
  `coffre-attaques-inedites-v1/` (une ligne vue par `git grep`) ; `registres/index-bras-attaque-v1.md` ; tout « depuis zéro ».
- **Sorties non lues** : rien sous `donnees/` ; les sorties du collisionneur v8 et v9 sont listées en annexe A du programme à partir du
  registre et du registre des dépenses.
- **Niveau méthode** : les neuf voies de mesure adversariale sont nommées par leur titre seulement ; les attaques du juge sont décrites
  par classe et but, résultats scellés seulement.
- **Lecture d'autres branches** : par `git show <commit>:<chemin>` seulement (branches `origin/canal/conv-audit-n04`,
  `origin/prep/organisme-v65-v1`, `origin/claude/upbeat-cray-dmauvv`) ; aucun `fetch`, `ls-tree` ni `log --all`.
- **Outil de publication** : non utilisé (interdit 3 ; publication réservée à Lazar).
- **Hors chemins nommés** : seul mon bac à sable (`…/scratchpad/agents/redacteur-architecture-organisme/`) a reçu des fichiers de
  travail (outils de lecture, parties du registre, dossiers temporaires du rendu).

## 5. Faits survenus après le scellement du programme (12:34 UTC), non intégrés au texte v1

Relevés au registre à 12:36 UTC ; ils rendent en partie caduques les sections 4.6, 8.3 à 8.5 et l'annexe B, point 9 :

1. **R-2215 (12:20 UTC)** : la **contre-lecture du code v65 est rendue** (`c4ddfc7f…`) : « **utilisable pour la course après
   corrections** » ; bloquants **CLV65-01** (C1 rendu sans fausse jugée) et **CLV65-02** (un arrêt peut masquer une brèche) ; CLV65-03
   à -06 (vue servie non vérifiée ; 17 mutations sur 20 survivent ; garde 7 incomplète ; banc à 37 sur 38 sous `bwrap`) ; CLV65-07
   (le lanceur refuse `registres/go.md` : identifiants en double, lignes d'extension) ; CLV65-08 à -10. Avis sur le dossier du texte :
   `orchestrator/prereg/`, copie locale à l'octet ; pousser au dépôt public reste ta décision. **Décision de la mère : v66** sous
   noms neufs, développeur neuf lancé (consigne `264e8a08…`).
2. **R-2215 (2)** : **critères de lecture du tour 2 N12-N13 scellés** (`6bdbfe47…`, commit `9ca47466`) ; **lecteur neuf lancé**
   (Opus 5.5) : le pas (a) de R-2199 est en cours.
3. La contre-lecture v65 ne traite pas l'écart d'empreinte de configuration que relève le programme (`995eb918…` exigé par
   GO-2026-11-10-10 contre `bff138d8…` dans la v65) ; elle relève à part (CLV65-10) que l'empreinte de la configuration v5 gèle des
   chemins absolus de commandes absents de `main`. Avec la v66, la configuration changera encore : la condition « configuration v5
   `995eb918…` » de la ligne de GO est à relire par Lazar ou par la mère.
4. R-2213, R-2217, R-2219 : sections de résultats v3 contre-lues, puis v4 et v5 (organisme `77d0e57a…`, puis `b6a35432…`) ; le
   programme cite la v3 (`d6d702f5…`), dont la contre-lecture relève notamment une affirmation périmée sur l'enveloppe de 120 USD
   (CLR-01) — ce programme-ci la donne déjà inscrite (R-2206).

**Remplacement proposé pour une v2 du programme, § 4.6, puce « Préalables »** : « (1) contre-lecture du code v65 **rendue le
10 novembre** (`c4ddfc7f…`, R-2215) : utilisable après corrections, deux bloquants (CLV65-01, CLV65-02) ; la mère a décidé une
**v66** sous noms neufs (développeur neuf, consigne `264e8a08…`) ; ». Et § 8.5, première ligne : prochain pas « code v66 », puis
contre-lecture courte de la v66.

## 6. Trous et limites (repris de l'annexe B du programme, mis à jour)

1. Couches 1 et 2 au sens de N12 : non définies dans les pièces lisibles (l'inventaire voisin, v5, n'en donne pas non plus).
2. Écart d'empreinte de configuration (point 5.3 ci-dessus).
3. Audit de calibration des juges (N13 (a)) : décidé, sans trace d'exécution.
4. Étape 2 : aucun préenregistrement trouvé.
5. N-059 : état de codage non vérifié.
6. Continuité du code entre noyau de l'étape 1 et orchestrateur : affirmée par R-2152, non vérifiée.
7. Dépenses : relevé non exhaustif, sans total.
8. Pièces volontairement non lues : P-041 ; documents de l'organisme de Gemini ; sorties des courses des mentors ; conception de
   l'affinage ; verdicts primaires d'A1-v3, d'A1-v4 et de la validation du v9 (cités par la section de résultats v3 et la page
   publique) ; verdict d'A1 (`795e5e99…`) non retrouvé sur `main`.
9. Le programme v1 n'est pas contre-lu ; il est daté de 12:34 UTC et ne porte pas les faits du point 5.
