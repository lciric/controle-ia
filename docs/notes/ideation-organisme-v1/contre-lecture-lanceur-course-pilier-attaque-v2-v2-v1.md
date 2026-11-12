# Contre-lecture du lanceur de la course de l'organisme d'idéation sur la question v2 du pilier attaque (version 2)

Contre-lecteur neuf (règle R2 ; je n'ai écrit aucune ligne des fichiers lus), 9 novembre 2026. Objet : autoriser ou non la
règle de permission limitée à la seule commande `python3 -I -B scripts/lancer_course_ideation_pilier_attaque_v2_v2.py`
(décision de Lazar, R-1978 ; voie (a), R-1981 ; lanceur rapporté en R-1983).

## Ce que j'ai lu, et comment

- Lanceur : `scripts/lancer_course_ideation_pilier_attaque_v2_v2.py` (`dc743fa891bbabe3cf565c3281d93d3008c71927ccf333911dc04134ac74dade`, 638 lignes),
  compagnon `.sha256` conforme ; essais : `tests/test_lancer_course_ideation_pilier_attaque_v2_v2.py`
  (`869d31af4784d155b773ce5c15049162b8f5850d4f9bf798e34eea8a6af6b681`, 354 lignes).
- Registre : `registres/decisions.md` R-1937 à R-1940 et R-1978 à R-1983 ; `registres/go.md` ligne GO-2026-11-08-13 (type calcul,
  Lazar, 20 USD, échéance 2026-11-15, aucune ligne de révocation qui la cite) ; devis `rapports/fille-ideation-1-v1/devis-course-ideation-pilier-attaque-v2-v1.md`
  (`531849e3…`) ; mesure épinglée `rapports/fille-ideation-1-v1/mesurer-consignes-pilier-attaque-v2-v1.json` (`db44b41e…`) ;
  enveloppe `appel-argon-v5.sh` (`37c0205e…`) ; garde `.claude/hooks/garde_calcul.py` et `.claude/settings.json`.
- Orchestrateur : clone `/home/user/ideation-organism` au commit `f39a7f4ab9e3da1e11629b1be329304cd5b8a1b0`, arbre propre, neuf
  empreintes épinglées toutes concordantes (vérifiées par `sha256sum`). Lecture seule de `orchestrator/demonstrations/ideation_v8.py`
  → v7 → v6 → v5 → v4 → v2 (analyseur d'arguments, `roles_et_budgets`, `garde_de_la_course`, `verifier_reglages_lanceur`, `_principal`),
  `orchestrator/pole/ideation_v2.py` (constantes l. 230-258, formules l. 1194-1312, `verifier_reglages` l. 1429-1558, sommes
  l. 1948-1973, gardes de passe l. 2279-2311 et 2496-2516, garde du juge l. 2967-2989), `orchestrator/pole/adaptateurs.py`
  (sonde l. 195-235, clés l. 418-422 et 651-656), `orchestrator/pole/relais.py`. **Rien de l'orchestrateur n'a été importé ni
  exécuté dans mon processus** ; les seuls programmes lancés sont les essais du lanceur (faux orchestrateur) et de petits calculs
  d'arithmétique et de lecture d'en-têtes de fichiers.
- Essais : `PYTHONPATH=src timeout 900 .venv/bin/python -m pytest -q -p no:cacheprovider --basetemp=<scratchpad>/pytest-cl-org tests/test_lancer_course_ideation_pilier_attaque_v2_v2.py`
  → **41 passés en 2,4 s** ; dossier temporaire supprimé. Aucun appel de modèle, aucun lancement de la course.
- Interdits respectés : aucune lecture sous `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ;
  ni `env`, `printenv`, `set`, ni aucune clé ; rien commité.

## Verdict

**Autorisable après corrections** — aucun constat bloquant ; un constat majeur sur l'intégrité de l'orchestrateur (cache
d'octets non couvert par « arbre propre »), un constat majeur sur la règle elle-même (elle autorise une commande, pas un contenu),
et des constats mineurs. Les corrections demandent une **version 3 du lanceur** (R12 : nouveau nom), donc une règle qui nomme
`…_v2_v3.py`, et une garde d'empreinte dans le crochet existant. Si Lazar préfère lancer sans attendre la version 3, le risque
résiduel du constat majeur 1 est faible et dit en clair ci-dessous ; les plafonds, le GO et le refus sans bac à sable tiennent
tels quels.

## Réponses aux six points

### (1) Aucun contournement — tenu, à une réserve d'intégrité près (M1)

- La commande construite (`commande_course`, l. 309-346) est la commande canonique du devis § 5 point 2, crochets résolus, plus
  les plafonds externes du § 4 : aucun drapeau qui désactive ou affaiblit le bac à sable (`--accepter-sans-bac-a-sable`,
  `--motif-sans-bac-a-sable`), aucune tolérance de somme, aucun relèvement de garde de taille ni de prix (`--taille-max-consigne-externe`,
  `--taille-max-consigne-externe-bras`, `--prix-entree-usd-par-million-jetons`). La liste interdite (l. 151-155) couvre les
  trois familles, et `garde_drapeaux` (l. 353-364) refuse aussi les préfixes qu'argparse accepterait et la forme `=valeur`.
- Aucun remplacement de fonction : le lanceur n'importe rien de l'orchestrateur dans son processus (seul texte `from pole…` : la
  sonde, exécutée dans un processus à part, l. 162-167 et 486-504) ; essai l. 295-301.
- Orchestrateur non modifié : commit épinglé, `git status --porcelain` vide, neuf empreintes (l. 272-290). **Mais** `git status
  --porcelain` ignore les fichiers du `.gitignore` (`__pycache__/`, `*.pyc`), et `-B` empêche d'écrire un cache d'octets, pas de le
  lire : voir M1.
- Refus sans bac à sable : `sonder_bac_a_sable` appelle `pole.adaptateurs.etat_bac_a_sable_detaille` **telle quelle** (deux
  `bwrap … true`, lecture seule) et exige `actif` **et** `proc_neuf` vrais (l. 500-503) — plus strict que l'orchestrateur, qui
  tolère `proc_neuf` faux hors root (`demonstrations/ideation_v2.py` l. 1197-1201). Sonde illisible ou en panne → refus, rien écrit
  (essais l. 222-233). L'orchestrateur refait sa propre sonde avant tout appel (l. 1196) : double garde.
- Ordre des gardes (l. 559-575) : toutes avant la moindre écriture ; puis manifeste de départ scellé, liste blanche par
  l'orchestrateur lui-même et vérifiée contre les pièces (l. 532-543), course, manifeste de fin scellé ; signaux relayés par PID
  (R10, l. 602-612).

### (2) Argent — conforme

- Sommes recalculées comme l'orchestrateur (`pole/ideation_v2.py` l. 1511-1519 et 1950-1958 ; le lanceur l. 384-418 reproduit
  les mêmes termes, défauts compris : contrôle Claude 0,2 × 2 modèles, passes × proposeurs, juges ; externe : contrôle 1,25 +
  passe 1 1,70 + passe 2 2,30 + juge 2,5 + contrôle du bras 0,2) : **externe 7,95 < 8,0 (strict, l. 425) ; Claude 0,4 + 8,0 + 1,5 =
  9,9 ≤ 12,0**. Totaux transmis exigés égaux à 12,0 et 8,0 (l. 423).
- Voie (a) de R-1981 tenue : passe 1 ≤ 1,70 (= 1,70), passe 2 ≥ 2,25 (= 2,30), prix prudent gardé (défaut 10), seconde passe gardée.
  Seul écart au devis : contrôle externe 1,35 → 1,25, **réduction** d'un plafond (permise par R-1978), consignée au manifeste
  (`PLAFOND_REDUIT`, l. 127-131). Rien hors du devis.
- GO : `verifier_go` (l. 223-262) exige une seule ligne principale, 8 colonnes, type calcul, Lazar, période, non révoquée,
  périmètre « organisme d'idéation » et « question v2 » ; essai sur le registre réel l. 243-245. La colonne plafond (« 20 USD »)
  n'est pas lue : mineur m2.
- `--budget-passe-2-externe-usd` n'est admis par l'orchestrateur qu'avec `--proposeur-externe` et `--seconde-passe` (l. 1012-1016) :
  tous présents. Sans matériau, aucune attestation de matériau n'est exigée (`pole/ideation_v2.py` l. 1503 et 1975 : condition
  `materiau_lu`) : la mention « aucun matériau : `--seconde-passe` gardée » du lanceur est juste.

### (3) Gardes de taille recalculées par moi — course et passe 1 justes, passe 2 mal étiquetée (m1), juge mal comparé (m3)

Formules lues dans `pole/ideation_v2.py` : prix prudent 10 / 10⁶ / 4 = 2,5 × 10⁻⁶ USD par caractère (l. 236-237) ;
`taille_max_consigne_par_defaut(p, prov) = max(0, int(p / prix + 10⁻⁶) − prov)` (l. 1229-1230) ; provision de la course
`nombre × 12 000 × 5` (l. 246, 1203-1211) ; provision d'une passe `nombre × max(8 000, plus grande fiche admise) × 5`
(l. 258, 1298-1312, 2497-2511) ; garde de la course = min(contrôle entrée seule, passe 2 − provision) (l. 1233-1253 et
`garde_de_la_course`, `demonstrations/ideation_v2.py` l. 905-917). Les arrondis flottants donnent bien 500 000, 680 000,
920 000 (vérifié : 1,70 / 2,5e-6 = 679 999,99…, + 10⁻⁶ puis `int` → 680 000).

| Garde (orchestrateur) | Calcul | Taille admise | Consigne mesurée | Marge | Lanceur (l. 464-469) |
|---|---|---|---|---|---|
| Course : contrôle d'Argon, 1,25 | 500 000 | — | — | — | 500 000 ✓ |
| Course : passe 2, 2,30 − 8 × 12 000 × 5 | 920 000 − 480 000 | 440 000 | 415 253 | **+24 747** | 440 000, +24 747 ✓ |
| Passe 1 d'Argon, 1,70 − 8 × 8 000 × 5 | 680 000 − 320 000 | 360 000 | 60 637 | **+299 363** | 360 000, +299 363 ✓ |
| Passe 2 d'Argon, fiches ≤ 8 000 | 920 000 − 320 000 | 600 000 | ≈ 60 637 + 8 × 8 009 ≈ 124 700 | ≈ +475 000 | compare 600 000 à **414 778** : voir m1 |
| Passe 2 d'Argon, fiches de taille f > 8 000 | 920 000 − 40 f | | ≈ 60 637 + 8 (f + 9) | tient si **f ≤ 17 901** | non calculé : voir m1 |
| Juge d'Argon (bras différé, hors de cette course), 2,5 − 52 × 2 000 × 5 | 1 000 000 − 520 000 | 480 000 | consigne du juge, non 415 253 | voir m3 | « marge contre 415 253 » |

Les marges de R-1983 sont donc justes pour la course (+24 747) et la passe 1 (+299 363) ; la « marge » de la passe 2
(+185 222) n'est pas une grandeur que l'orchestrateur calcule (m1) ; la réserve de R-1983 (« fiches d'Argon ≤ ≈ 17 900 ») est
exacte : au-delà, la passe 2 d'Argon est refusée **avant envoi** par `garder_session_externe` (l. 2279-2296) et la course
s'arrête. Conséquence chiffrée : Argon joue ses deux passes **avant** les proposeurs Claude (l. 2512-2516), donc l'arrêt
coûterait au plus les contrôles (1,25 + 2 × 0,2) et la passe 1 d'Argon (1,70) : ≤ 3,35 USD au pire, 0 chez les proposeurs Claude.

### (4) Secrets — tenu, une nuance de formulation (m4)

Aucune valeur de clé écrite, transmise, imprimée ni consultée : `environnement_sans_cles` (l. 507-512) décide sur les **noms**
(liste de `pole/relais.py` l. 15-18 reprise à l'identique, plus un motif large), retire ces noms de l'environnement de la sonde,
de la liste blanche et de la course, et le manifeste n'en porte que les noms (essai l. 133-134 : la valeur factice est absente
du manifeste). L'orchestrateur refuse de lui-même tout nom de clé (`adaptateurs.py` l. 418-422, 651-656) ; le retrait des noms
n'est pas un contournement mais la condition d'emploi que l'orchestrateur impose (« la clé reste dans le relais »). Les relais
(Claude 8787, Gemini 8788) détiennent seuls les vraies clés et sont hors du lanceur ; l'enveloppe d'Argon n'exporte qu'une
clé factice (`appel-argon-v5.sh` l. 30). La seule nuance : `dict(os.environ)` (l. 555) copie toutes les valeurs dans la mémoire
du lanceur avant filtrage — rien n'en sort, mais « jamais lues » (l. 589) est trop fort : m4.

### (5) Règle de permission `Bash(python3 -I -B scripts/lancer_course_ideation_pilier_attaque_v2_v2.py)` — étroite sur la forme, pas sur le fond (M2)

- Forme : sans `:*`, la règle n'autorise que cette chaîne exacte ; le lanceur refuse tout argument (l. 626-629, essai l. 238-240) ;
  `DEPOT` vient de `__file__`, et `verifier_pieces` exige que le dépôt soit `/home/user/controle-ia-travail` (l. 294-295) : une
  copie du dépôt ailleurs ne pourrait pas servir. Le crochet `garde_calcul.py` laisse passer (aucun motif de lancement
  d'instance) et bloque toujours les arrêts par motif.
- Fond : **la règle autorise une commande, non un contenu**. Un fichier modifié (par `Edit`, `Write`, `sed`, ou une session
  future) s'exécuterait sous la même règle sans aucune question ; l'empreinte que le lanceur écrit dans son manifeste
  (l. 582) n'est qu'une trace après coup. Je recommande une **garde d'empreinte** au crochet `PreToolUse` déjà actif
  (`.claude/hooks/garde_calcul.py`) : si la commande cite `lancer_course_ideation_pilier_attaque_v2_v3.py` (ou v2), lire le
  fichier, calculer sa `sha256`, la comparer à la valeur épinglée dans le crochet **et** au compagnon `.sha256` ; bloquer sinon
  (code 2, motif dit). Un cas sain et un artefact (fichier modifié d'un octet) dans les essais du crochet. En défense en
  profondeur : règles `deny` sur `Edit`, `Write` et `MultiEdit` pour ce chemin et son `.sha256`. Interpréteur absolu dans la règle
  (`/usr/local/bin/python3`, celui que l'enveloppe d'Argon appelle, l. 31) plutôt que `python3` qui suit `PATH` (m5).

### (6) Essais R5 — chaque garde a au moins un cas sain et un artefact ; quelques artefacts manquent (m6)

Couverts : arguments (sain : bout en bout ; artefact l. 238) ; GO (sain réel l. 243 ; hors période l. 248, révoqué l. 255) ;
orchestrateur (modifié l. 262, empreinte l. 269, commit l. 275) ; pièces (l. 281, 352) ; drapeaux (l. 155-174, préfixes et
`=valeur` compris) ; sommes (l. 179-217 : valeur du devis, égalité, défauts de l'orchestrateur 11,20, bout en bout) ; bac à
sable (l. 222-233 : inactif, sans /proc, illisible, erreur) ; clés (l. 288-292 et 127-134) ; tailles (l. 305-349 : borne basse
2,25, passe 2 trop basse, passe 1 trop basse, bout en bout, mesure illisible) ; scellement (l. 139-141) ; code de l'orchestrateur
rendu (l. 146-150). Manquent : voir m6.

## Constats

### Bloquants — aucun.

### Majeurs

**M1 — Le cache d'octets du clone échappe à « aucune modification »** (`verifier_orchestrateur`, l. 279-281 ; sonde l. 489,
liste blanche l. 535, course l. 600). `git status --porcelain` ne liste pas les fichiers ignorés ; `orchestrator/pole/__pycache__/`
existe (5 fichiers du 8 novembre 19:34, dont `outils`, `caviardage`, `__init__`, importés par la chaîne), et j'ai vérifié sur
leurs en-têtes que trois sont **valides** pour Python (horodatage et taille de la source concordants) : Python 3.13 les importe
à la place des sources empreintées, `-B` n'empêchant que l'écriture. Ces octets ne sont couverts ni par le commit, ni par
`git status`, ni par les neuf empreintes. Aucun indice d'altération (ils datent des essais de la fille, sources inchangées
depuis 09:37), mais la garde a un trou. Corrections (version 3) : (a) refuser si `git status --porcelain --ignored` n'est pas
vide (ou si un `__pycache__` ou un `.pyc` existe sous `orchestrator/`) ; (b) de plus, placer `PYTHONPYCACHEPREFIX` dans
l'environnement transmis, vers un dossier neuf hors du clone (par exemple `<dossier_sortie>/pycache`), pour la sonde, la liste
blanche et la course : Python ne lit alors plus les `__pycache__` du clone. Essais : cas sain (clone sans cache) et artefact
(un `.pyc` planté à côté d'une source → refus). Procédure immédiate possible, hors lanceur : supprimer le dossier
`orchestrator/pole/__pycache__/` (fichier ignoré, pas une modification de l'orchestrateur) avant tout lancement, et le consigner.

**M2 — La règle autorise une commande, pas un contenu** (point 5). Correction : garde d'empreinte au crochet
`.claude/hooks/garde_calcul.py`, règles `deny` sur l'édition du lanceur, interpréteur absolu. Sans cela, l'exception accordée
par Lazar vaut pour tout code futur portant ce nom de fichier.

### Mineurs

**m1 — Garde « passe 2 aux fiches de 8 000 » mal étiquetée** (l. 468, commentaire l. 122-123 ; essai l. 310). Elle compare la
taille admise avec des fiches de 8 000 (600 000) à la **consigne maximale** mesurée avec des fiches de 44 259 (414 778) : deux
hypothèses incompatibles ; la « marge » de 185 222 n'existe pas chez l'orchestrateur, qui compare la consigne réelle de passe 2
à `920 000 − 40 × max(8 000, plus grande fiche admise)`. Correction : rapporter (i) la consigne de passe 2 aux fiches de 8 000
(≈ 60 637 + 8 × 8 009) contre 600 000, et (ii) le seuil de fiche au-delà duquel la passe 2 serait refusée :
`f_max = ⌊(taille_max(p2, 0) − consigne_passe_1 − 72) / 48⌋` = 17 901 caractères, avec la dépense maximale en cas de refus
(≤ 3,35 USD, voir point 3). Ne change pas la décision.

**m2 — Plafond du GO non lu** (`verifier_go`, l. 246-262). La colonne « 20 USD » n'est pas comparée à 12,0 + 8,0 codés en dur.
Correction : extraire le nombre et exiger `plafond ≥ TOTAL_CLAUDE_USD + TOTAL_EXTERNE_USD`.

**m3 — « Marge contre 415 253 » du juge d'Argon** (l. 477-481). Le juge n'est jamais comparé à la consigne de contrôle du
proposeur ; l'orchestrateur compare sa propre consigne (fiches servies + témoins + pièce-juge ; au maximum 2 194 842 selon la
mesure, qui dit déjà `passerait_au_maximum: false` même à 3,5) à `plafond / prix − 52 × 2 000 × 5` (l. 2969-2983). Rapporter
480 000 contre `consigne_du_juge_maximale`, marquer « ne passerait pas au maximum théorique ; dépend des fiches réelles » ; sans
effet sur cette course (bras différé).

**m4 — Formulation « valeurs jamais lues »** (l. 508, 589 ; `dict(os.environ)` l. 555). Construire l'environnement transmis sans
copie intégrale (`{n: os.environ[n] for n in os.environ if n not in retires}`) et écrire « aucune valeur de clé écrite, transmise
ni consultée ».

**m5 — Interpréteur par `PATH`** dans la règle et dans `sys.executable` : préférer `/usr/local/bin/python3` dans la règle ; le
lanceur pourrait refuser si `sys.executable` n'est pas ce chemin (le kit `claude-agent-sdk` 0.2.172 est installé pour cet
interpréteur ; un autre interpréteur ferait refuser l'orchestrateur à `importer_sdk`, à 0 USD).

**m6 — Artefacts d'essai manquants** (R5) : GO de type ≠ calcul, accordé par un autre que Lazar, périmètre étranger, identifiant
en double ; totaux transmis ≠ 12 + 8 (l. 423) ; mesure à un autre prix que 10 (l. 451) ; `--nombre` ≠ mesure (l. 454) ;
`ecrire_scelle` sur fichier existant (l. 521) ; dossier de run déjà présent (l. 574) ; orchestrateur absent (l. 274) ; chemin
avec espace (l. 313) ; `date -u` illisible (l. 185). Un cas chacun.

## Réserves (hors constats)

- Les deux relais (Claude 8787 avec `--modeles-permis claude-opus-5-5,claude-fable-5-1` exactement ; Gemini v2 8788 avec la vraie
  clé) sont hors du lanceur et hors de la règle : leur lancement demande ses propres permissions ; s'ils manquent, l'orchestrateur
  refuse avant tout appel (`verifier_relais`, l. 1364-1366 ; contrôle d'Argon avant Claude), à 0 USD.
- Le lanceur ne passe pas `--racine-depot` : les lectures interdites aux agents sont la sortie, le clone et le dossier personnel
  de l'utilisateur (l. 1202-1203) ; sous root, le dépôt de travail n'y figure pas. Sans portée ici (agents sans aucun outil,
  `tools=[]`), mais à savoir.
- `sys.executable` est hérité : sous la règle, c'est le `python3` du `PATH` de la session (m5).
- Ce rapport n'est pas scellé par moi (consigne : un seul fichier nouveau) ; empreinte donnée dans la passation au demandeur, à
  sceller par `python -m controle_ia.scellement sceller`.

## Avis sur la règle, en une phrase

Écrire la règle pour la **version 3** du lanceur (M1 corrigé, m1 à m4 au passage), avec l'interpréteur absolu, **et** la garde
d'empreinte au crochet `garde_calcul.py` ; à défaut, si Lazar lance sur la version 2 telle quelle, supprimer d'abord
`orchestrator/pole/__pycache__/` et le consigner, en sachant que la règle couvrira tout contenu futur du fichier tant que le
crochet ne vérifie pas l'empreinte.
