# Vérification du lanceur v3 de la course de l'organisme d'idéation (question v2 du pilier attaque) et de la garde d'empreinte du crochet

Vérificateur neuf (règle R2 ; je n'ai écrit aucune ligne des fichiers lus ; autre modèle que le développeur), 9 novembre 2026.
Objet : avant que la session mère n'écrive la règle de permission accordée par Lazar (R-1978, « Oui, la règle »), dire si (1) le
lanceur v3 applique la contre-lecture du v2 (M1, m1 à m6) et si (2) la garde d'empreinte ajoutée au crochet de calcul (M2) est juste.

## Ce que j'ai lu, et comment

Tout au commit `b14e840f` de `main` (arbre propre hors deux dossiers non suivis sans lien : `anteriorite-co-scientist-v1/`,
`docs/sources/co-scientist-v1/`). Empreintes recalculées par `sha256sum`, toutes conformes aux valeurs annoncées :

- lanceur v3 `scripts/lancer_course_ideation_pilier_attaque_v2_v3.py` : `0a704661f1b648ff329d173e8c015b85f6923ef893249b6240e971afaa0a93ca`
  (782 lignes, mode 100644, pas un lien) ; compagnon `.sha256` : même empreinte, bon nom de fichier ;
- essais `tests/test_lancer_course_ideation_pilier_attaque_v2_v3.py` : `0ff05ed5c8955fac4a30ef08dce5512ab72cd5f55d1a7d1cd77340100801789d`
  (661 lignes), compagnon conforme ;
- lanceur v2 `…_v2_v2.py` : `dc743fa891bbabe3cf565c3281d93d3008c71927ccf333911dc04134ac74dade` (inchangé ; `diff -u` v2 → v3 lu en entier) ;
- contre-lecture du v2 : `4591fe97d97cc74d6106cdcd40e77dc409c23238a7cb42cdb17d25fb1e7c7bdd` ;
- crochet `.claude/hooks/garde_calcul.py` : `184b3bbd92e95a10af2237c939b33ddce61c5bee7c7526076a1c91d863588502` ; `git diff b14e840f~1 b14e840f`
  sur ce fichier lu en entier : 61 lignes ajoutées, 2 retirées (signature de `decider`, appel de `decider`), rien d'autre touché ;
- essais du crochet `tests/test_garde_calcul.py` (`fac60788…`, 179 lignes) et `tests/test_garde_calcul_empreinte_lanceur_v3_v1.py`
  (`559ef672…`, 185 lignes, compagnon conforme) ;
- `registres/decisions.md` R-1978 à R-1991 ; ligne GO-2026-11-08-13 de `registres/go.md` (type calcul, Lazar, 20 USD, échéance
  2026-11-15) ; `.claude/settings.json` (crochet seul, aucune permission encore) ; aucun `settings.local.json`.
- Documentation en ligne de Claude Code lue le jour même : `code.claude.com/docs/en/permissions` (syntaxe des règles, chemins
  `//`, ordre refus → demande → autorisation, confiance du dossier, redirections), `…/hooks` (champ `cwd`, code 2),
  `…/settings` (fichiers et préséance), `…/permission-modes` (chemins protégés, mode `acceptEdits`).
- Essais lancés (`.venv`, Python 3.13.18, `-p no:cacheprovider`, dossier temporaire sous mon bloc-notes, supprimé ensuite) :
  `tests/test_garde_calcul.py` + `tests/test_garde_calcul_empreinte_lanceur_v3_v1.py` + `tests/test_lancer_course_ideation_pilier_attaque_v2_v3.py`
  → **153 passés en 7,7 s** (37 + 38 + 78), aucun sauté. Le cas sain réel du crochet (commande exacte, lanceur réel, dépôt réel) est
  dans ce lot ; `test_orchestrateur_sain_clone_reel` a tourné sur le vrai clone (commit `f39a7f4a…`, arbre propre fichiers
  ignorés compris, aucun cache d'octets, neuf empreintes).
- À la main : le crochet appelé comme Claude Code l'appelle (entrée JSON sur l'entrée standard, `cwd` fourni), sur une vingtaine
  de commandes (tableau au point (c)) ; interpréteur, chemins de `git` et `date`, état du clone, module `pole` absent de
  `sys.modules` après chargement du lanceur. Le lanceur n'a **jamais été exécuté par sa commande** ; aucun modèle appelé ;
  aucune lecture sous `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; ni `env`, `printenv`,
  `set`, ni clé ; rien commité ; ce rapport est le seul fichier écrit.

## Verdict

**Règle écrivable telle quelle.** Aucun constat bloquant, aucun constat majeur. Les sept corrections de la contre-lecture (M1,
m1 à m6) sont faites et chacune a un cas sain et au moins un artefact ; la garde d'empreinte du crochet (M2) laisse passer la
seule commande permise sur le seul contenu épinglé et bloque chaque écart que j'ai essayé ; les gardes de GO et de R10 sont
intactes ; la syntaxe proposée correspond à la documentation. Six constats mineurs, dont deux de durcissement à faire **au moment
d'écrire la règle** (ils ne touchent ni le lanceur ni le crochet : `-I -B` sur la commande du crochet dans `settings.json`,
essai d'import renforcé), les autres consignables sans geste. Réserves en fin de rapport, dont une de fond : la règle épingle
le **contenu du lanceur**, non l'interpréteur, la bibliothèque standard ni le clone au-delà de ses neuf fichiers.

## (a) M1 et m1 à m6 : faites, essayées (cas sain et artefact)

| Correction | Où (lanceur v3) | Essais (cas sain / artefact) | Avis |
|---|---|---|---|
| **M1** refus des fichiers ignorés | `verifier_orchestrateur` l. 357-360 : `git status --porcelain --ignored` non vide → refus | sain : l. 394-397 et clone réel l. 482-489 ; artefacts : `.pyc` valide planté sous `__pycache__/` (tait par `git status`, l. 400-409), autre fichier ignoré `trace.log` (l. 412-415) | juste |
| **M1** aucun cache d'octets sous `orchestrator/` | `caches_d_octets` l. 331-343 (`__pycache__`, `.pyc`, `.pyo`, `.git` exclu) ; l. 361-363 | artefacts : `.pyc` **suivi par git** (hors `status` et hors `--ignored`, l. 418-425), dossier `__pycache__` vide (l. 428-430, que git ne voit jamais) | juste, ceinture et bretelles |
| **M1** préfixe de cache hors du clone | `options_interprete` l. 377-379 : `-I -B -X pycache_prefix=<sortie>/pycache` ; `verifier_prefixe_pycache` l. 382-390 (absolu, neuf, hors du clone) ; variable `PYTHONPYCACHEPREFIX` aussi transmise l. 646-647 ; sonde, liste blanche et course l. 618, 671, 744 | l. 433-460 : un `.pyc` leurre valide (même taille, même horodatage qu'une autre source) **est lu** sous `-I -B` seul (le trou de M1 reproduit), la variable seule **ne tient pas** sous `-I` (`sys.pycache_prefix` reste `None`), l'option `-X` fait lire la source et n'écrit rien ; l. 463-479 : préfixe dans le clone, déjà présent, relatif, et de bout en bout | juste ; constat du développeur exact et important (la contre-lecture ne proposait que la variable, insuffisante sous `-I`) |
| **m1** seuil réel de la passe 2 | `seuil_fiche_passe_2` l. 540-544, `garde_tailles` l. 575-602 : passe 2 aux fiches de 8 000 comparée à 60 637 + 8 × 8 009 = 124 709 (marge 475 291) ; seuil ⌊(920 000 − 60 637 − 72) / 48⌋ = 17 901 ; dépense si refus 1,25 + 0,4 + 1,70 = 3,35 | l. 322-338 (plus « 185222 » ni « marge_contre_415253 »), l. 602-610 (artefact : seule la garde `passe_2_fiches_8000` tombe), l. 613-618 (borne : 17 901 tient, 17 902 non) | recalculé par moi : exact |
| **m2** plafond du GO lu | `lire_plafond_go` l. 257-262 (forme « nombre USD » seule), `verifier_go` l. 303-306 : ≥ 12 + 8 | sain : registre réel → 20,0 (l. 516-518) ; artefacts : 19, 19,99, « vingt », vide (l. 521-527) | juste ; « 20 USD » du registre réel lu |
| **m3** juge d'Argon | l. 603-610 : 480 000 contre `consigne_du_juge_maximale` 2 194 842 → −1 714 842, « ne passerait pas au maximum théorique ; dépend des fiches réelles », rapporté sans garde | l. 335-338 | juste |
| **m4** environnement sans copie | l. 637-648 : filtrage par noms, `env[n]` lu seulement pour les noms gardés ; `executer` l. 692 : `os.environ` tel quel, plus de `dict(os.environ)` ; manifeste l. 730-731 | l. 532-545 : une correspondance qui **lève à la lecture d'une clé** passe ; chaîne `dict(os.environ)` absente | juste |
| **m5** interpréteur absolu | `PYTHON_COURSE = "/usr/local/bin/python3"` l. 180 ; `verifier_interprete` l. 312-321 : absolu, présent, exécutable, **égal à `sys.executable`** ; première garde de `executer` l. 696 | sain l. 494-503 ; artefacts : relatif, absent, `/bin/sh` (l. 506-511) ; vérifié par moi : sous la commande permise `sys.executable` vaut `/usr/local/bin/python3` ; sous le `.venv`, refus | juste ; l'enveloppe d'Argon v5 appelle le même interpréteur (l. 28 de l'enveloppe) |
| **m6** artefacts manquants | — | GO : type, accordé par, périmètre, doublon (l. 550-566) ; totaux ≠ 12 + 8 (l. 569-574) ; prix ≠ 10 et `--nombre` ≠ mesure (l. 590-599) ; `ecrire_scelle` sur fichier existant (l. 621-626) ; dossier de run présent (l. 629-637) ; orchestrateur absent (l. 640-643) ; chemin avec espace (l. 646-650) ; `date -u` illisible et sain (l. 653-661) | les dix cas demandés sont là |

Le trou du cache d'octets est fermé à deux niveaux indépendants : **avant** (aucun fichier hors du commit ne peut exister dans
le clone, et aucun `.pyc`, même suivi, sous `orchestrator/` ; j'ai vérifié qu'un `git status --porcelain --ignored` lancé depuis
le sous-dossier `orchestrator/` rapporte bien tout le dépôt, racine comprise) et **pendant** (le préfixe envoie toute lecture
et toute écriture de cache vers un dossier neuf hors du clone ; sous `-B` rien n'y est écrit). Les processus lancés entre la
vérification et la course (sonde, liste blanche) tournent avec les mêmes options : ils ne régénèrent aucun cache dans le clone.

Vérification de fond du v2 → v3 par le `diff` : hors les ajouts ci-dessus, rien n'a changé dans la commande canonique
(`commande_course` l. 409-447 : seule option d'interpréteur ajoutée, `-X pycache_prefix=…`), les plafonds (contrôle externe
1,25 ; passe 1 1,70 ; passe 2 2,30 ; juge 2,5 ; sommes 7,95 < 8,0 et 9,9 ≤ 12,0, essais l. 195-233), la liste des drapeaux
interdits (l. 185-189, essais l. 171-190), la sonde du bac à sable (`actif` **et** `proc_neuf`, l. 630-633, essais l. 238-250),
le relais des signaux par PID (l. 746-756) ni les manifestes scellés.

## (b) Aucun contournement

- Aucun drapeau qui affaiblit le bac à sable, tolère une somme ou relève une garde de taille : `DRAPEAUX_INTERDITS` inchangés,
  `garde_drapeaux` refuse en entier, abrégé (préfixe argparse) et `=valeur` ; `arguments_en_plus` est vide en production
  (`Reglages.production()` ne le fixe pas) et `principal` refuse tout argument de ligne de commande (l. 770-773).
- Aucun remplacement de fonction : `grep` de `setattr`, `monkeypatch`, `importlib`, `__import__`, `exec(`, `eval(` dans le
  lanceur : aucun hors commentaires. Les imports sont de la bibliothèque standard seule (l. 71-81).
- L'orchestrateur n'est jamais importé dans le processus du lanceur : la seule mention d'un module `pole` est la chaîne
  `SONDE_BAC_A_SABLE` (l. 196-201), exécutée par `-c` dans un processus à part ; j'ai chargé le lanceur dans un interpréteur et
  vérifié `sys.modules` : aucun `pole`, aucun `pole.*`. Sous `-I` (donc `-P`), ni le dossier `scripts/` ni le dossier courant ne
  sont sur `sys.path` : un `json.py` planté dans le dépôt ne serait pas chargé.
- Les réglages (`Reglages`) ne sont accessibles qu'aux essais, pas à la ligne de commande ; l'environnement n'est lu que pour
  filtrer les noms de clé et le transmettre ; les variables `PYTHON*` sont ignorées par `-I`.

## (c) La garde du crochet

Lecture : `garder_lanceur_v3` (l. 113-141) est appelée par `decider` après la garde R10 et avant la garde de GO (l. 144-148). Elle
ne s'éveille que si la commande cite `lancer_course_ideation_pilier_attaque_v2_v3` (motif l. 62, bornes alphanumériques :
`test_lancer_…` n'est pas une citation, `…_v3.py.sha256` et `…_v3b.py` — ce dernier n'en est pas une non plus — traités comme
voulu). Alors, dans l'ordre : égalité **stricte** avec `COMMANDE_LANCEUR_V3` ; `cwd` présent ; `realpath(cwd) == realpath(DEPOT_COURSE)` ;
le crochet lui-même dans `DEPOT_COURSE` ; fichier présent, pas un lien symbolique ; empreinte lue = constante épinglée ;
compagnon lisible, une ligne, format `sha256sum`, bon nom, même empreinte. Tout écart → code 2, motif écrit ; aucun repli
(compagnon illisible → bloqué, non ignoré ; liste vide → « mal formé », pas d'exception non traitée).

Appels à la main (entrée JSON comme Claude Code l'envoie, `cwd` donné sauf mention) :

| Commande | Code | Motif |
|---|---|---|
| commande exacte, `cwd` = dépôt | **0** | passe (contenu épinglé) |
| commande exacte, `cwd` = dépôt avec `/` final | 0 | `realpath` normalise |
| commande exacte, `cwd` = `scripts/` du dépôt | 2 | « lancé depuis … exigé » |
| commande exacte, sans `cwd` | 2 | « dossier courant absent » |
| commande exacte avec deux espaces | 2 | « pas exactement » |
| `LD_PRELOAD=… ` + exacte ; `nohup ` + exacte ; exacte + ` &` ; `GO_ID=… ` + exacte | 2 | « pas exactement » |
| `git add scripts/<lanceur v3>` ; `git commit -m '… <nom> …'` ; `sha256sum -c scripts/<lanceur v3>.sha256` | 2 | « pas exactement » (toute citation hors la commande exacte) |
| `git add scripts/` ; `verifier-arbre .` ; `pytest … tests/test_<lanceur v3>.py` ; `cd docs && sha256sum -c …` ; `vastai show instances` ; `kill 1234` | 0 | ne citent pas le lanceur ; routine intacte |
| `GO_ID=GO-2026-11-08-13 vastai create instance 1` | 0 | garde de GO intacte : GO valide aujourd'hui |
| `pkill -f <nom>` (essai l. 178-180) | 2 | R10 garde sa priorité |
| crochet lancé par `/usr/local/bin/python3 -I -B` (voir mineur 2) | 0 / 2 | sain passe, artefact bloque |

Les essais couvrent le reste : octet ajouté (l. 93-97) ; fichier **et** compagnon réécrits ensemble (l. 100-107 : la constante
du crochet bloque encore — c'est la raison d'être de l'épinglage dans le crochet) ; compagnon à mauvaise empreinte, autre nom,
vide, texte, absent (l. 110-128) ; lanceur absent puis **lien symbolique vers le même contenu** (l. 131-138) ; quinze commandes
non exactes dont argument en plus, interpréteur du `PATH`, autre interpréteur, `.venv`, sans `-I`, sans `-B`, chemin absolu,
`./scripts/`, `cd /tmp &&` (l. 141-160) ; `cwd` absent, vide, `/tmp`, `/home/user` (l. 163-166) ; copie du crochet dans un autre
dépôt (l. 169-175) ; entrée illisible (l. 183-185). Les 37 essais antérieurs du crochet (GO, R10, extensions R-389, révocations)
passent sans modification ; le `diff` montre que `lire_go`, `LANCEMENTS`, `ARRETS_PAR_MOTIF` et la boucle des GO sont intacts.

Sur le champ `cwd` : la documentation des crochets le définit comme « Current working directory when the hook is invoked » et
précise qu'il devient « the new directory after Claude runs `cd` » ; il suit donc bien le dossier où la commande s'exécutera, et
le fichier que Python ouvrira (`cwd/scripts/<lanceur v3>.py`) est celui que le crochet a haché. Un `scripts/` remplacé par un lien
vers un autre dossier ne changerait rien : le crochet hache à travers le lien le même fichier que Python exécuterait ; seul le
fichier final ne doit pas être un lien, ce qui est vérifié.

## (d) Les règles proposées, au regard de la documentation

- `Bash(/usr/local/bin/python3 -I -B scripts/<lanceur v3>.py)` : « `Bash(npm run build)` | Matches the exact command `npm run build` » ;
  les règles Bash « match the whole command text, with `*` standing in for any text » ; sans `*` ni `:*`, correspondance exacte.
  La commande ne contient aucun `*` (sinon elle serait lue comme un motif). Exacte : **juste**.
- `Edit(//home/user/controle-ia-travail/…)` : les règles Read et Edit suivent la syntaxe gitignore avec quatre formes ; « `//path` |
  Absolute path from filesystem root » ; avertissement explicite : « A pattern like `/Users/alice/file` isn't an absolute path. The
  single leading slash anchors at the settings source » — la double barre est donc la bonne forme. Les règles `Edit` couvrent aussi
  `Write`, `NotebookEdit` et l'ancien `MultiEdit` (« use `Edit(docs/**)` in place of `Write(docs/**)` ») ; les redirections de sortie
  d'une commande Bash (`> fichier`, `>>`) sont vérifiées contre les règles `Edit` et les chemins protégés. Les trois refus
  proposés sont donc exacts et suffisants pour les outils d'édition ; nul besoin de règles `Write(...)` séparées.
- Préséance : « Rules are evaluated in order: deny, then ask, then allow. The first match in that order determines the outcome » ;
  vaut entre fichiers de réglages (« a user-level deny blocks a project-level allow »). « PreToolUse hook decisions don't bypass
  permission rules » et un crochet silencieux (code 0) n'approuve rien : notre crochet ne fait que bloquer, donc il ajoute une
  condition sans jamais en retirer. Juste.
- Emplacement : `.claude/settings.json` (projet, commité) est lu en session nuagique à un seul dépôt. Les règles **allow** d'un
  fichier de projet « grant capability, so Claude Code applies them only after you accept the workspace trust dialog » ; les
  crochets et les refus s'appliquent sans attendre. Voir réserve 1.

## (e) Reste-t-il une voie pour que la commande permise exécute autre chose que le contenu épinglé ?

Dans le périmètre que la règle peut tenir : **non**. La commande exacte ne porte ni argument, ni variable, ni redirection ; le
crochet exige le dossier courant du dépôt et hache le fichier que Python ouvrira ; le lanceur n'importe que la bibliothèque
standard, sous `-I` ; l'orchestrateur est tenu par commit épinglé, arbre propre fichiers ignorés compris, neuf empreintes, et
préfixe de cache hors du clone ; les pièces par empreinte.

Hors de ce périmètre, trois dépendances que la règle **ne peut pas** épingler et qu'il faut nommer (réserves, pas défauts) :
(i) l'interpréteur `/usr/local/bin/python3` (lien vers `python3.13`), sa bibliothèque standard et ses `site-packages`
(un `sitecustomize.py` ou un `.pth` y serait chargé même sous `-I`) ; (ii) les fichiers de profil de l'interpréteur de commandes
(`.bashrc`, etc.), d'où viennent `PATH` et l'environnement hérités — `git` et `date` sont trouvés par le `PATH` (`/usr/bin/git`,
`/usr/bin/date` ici) ; (iii) le clone de l'orchestrateur au-delà des neuf fichiers empreintés (`pole/outils.py`, `caviardage.py`,
`__init__.py`…), garanti par `git` au commit épinglé. Toutes trois sont hors du dossier de travail ou des « chemins protégés »
de Claude Code (les fichiers de démarrage de l'interpréteur de commandes en font partie), donc jamais écrites sans question hors
du mode `bypassPermissions` ; et une altération de (i) ou (ii) compromettrait toute commande, pas seulement celle-ci.

## Constats

### Bloquants — aucun.

### Majeurs — aucun.

### Mineurs

**m-v3-1 — Essai d'absence d'import trop faible** (`tests/test_lancer_…_v2_v3.py` l. 312-317). `"import pole" not in texte`
ne détecterait pas `from pole import x` (la chaîne « import pole » n'y figure pas). J'ai vérifié à la main qu'aucun tel import
n'existe ; l'essai, lui, ne le prouve pas. Correction (essais seulement, pas le lanceur) : un motif par ligne
`^\s*(from\s+pole\b|import\s+pole\b)` dont le seul match admis est dans `SONDE_BAC_A_SABLE`, et, à l'exécution, après
`exec_module`, `assert not [m for m in sys.modules if m == "pole" or m.startswith("pole.")]`.

**m-v3-2 — Le crochet tourne sans `-I`** (`.claude/settings.json` : `python3 "$CLAUDE_PROJECT_DIR/.claude/hooks/garde_calcul.py"`).
Un script lancé sans `-I`/`-P` a son propre dossier en tête de `sys.path` : un `json.py`, `re.py` ou `hashlib.py` déposé dans
`.claude/hooks/` remplacerait la bibliothèque standard et pourrait neutraliser la garde. Le dossier `.claude` est un chemin
protégé (écriture jamais approuvée sans question hors `bypassPermissions`), donc le risque est faible, mais la correction est
gratuite : `python3 -I -B "$CLAUDE_PROJECT_DIR/.claude/hooks/garde_calcul.py"`. Vérifié par moi sous `/usr/local/bin/python3 -I -B` :
cas sain 0, artefact 2 (le crochet n'utilise que la bibliothèque standard, lit l'entrée standard, ne dépend d'aucune variable
`PYTHON*`). À faire dans le même geste que l'écriture de la règle ; les essais du crochet n'en dépendent pas.

**m-v3-3 — `git` et `date` par le `PATH`** (lanceur l. 218, 325). Un `git` planté sur le `PATH` pourrait faire mentir
`rev-parse` et `status` (les neuf empreintes, calculées en Python, tiendraient ; les autres fichiers du clone non). Le `PATH`
hérité vient des fichiers de profil, protégés ; la commande permise ne peut pas le modifier (toute variable en préfixe la rend
inexacte). Correction, **pour une version future seulement** (R12 : nouveau nom, nouvelle empreinte, nouvelle vérification ;
pas exigée avant la règle) : `/usr/bin/git` et `/usr/bin/date` en chemins absolus, vérifiés présents comme l'interpréteur.

**m-v3-4 — Préfixe de message trompeur** (crochet l. 67) : tout blocage s'annonce « GARDE (registres/go, R10) », y compris ceux
de la garde d'empreinte (le motif dit ensuite « M2, R-1984 »). Cosmétique ; à corriger à la prochaine modification du crochet.

**m-v3-5 — Coût d'usage de la citation bloquée** : `git add scripts/<lanceur v3>`, `git commit -m` qui cite le nom,
`sha256sum -c scripts/<lanceur v3>.sha256`, `python -m controle_ia.scellement verifier scripts/<lanceur v3>` sont bloqués
(voulu : la mère l'a annoncé). Les équivalents passent : `git add scripts/`, `verifier-arbre .`, motifs `*_v2_v[3].py`, outil
`Read`. Aucun changement demandé ; à consigner dans la passation pour les sessions suivantes.

**m-v3-6 — `.claude/hooks/__pycache__/garde_calcul.cpython-313.pyc`** (fichier ignoré par git, créé par les essais qui
chargent le crochet avec `importlib`). Sans effet : le crochet est exécuté comme script (`__main__`), jamais importé par Claude
Code, et `-B` (mineur 2) empêchera sa recréation par le crochet lui-même. À supprimer pour la propreté ; lancer les essais
avec `python -B` évite son retour.

## Réserves (hors constats)

1. **Confiance du dossier.** Les règles `allow` d'un `.claude/settings.json` commité ne s'appliquent qu'après acceptation de la
   confiance du dossier (en nuage : le mécanisme de confiance du dépôt de la session). Si la session neuve qui lance la course
   n'a pas cette confiance, la commande **demande** au lieu de passer : échec sûr, mais à prévoir (la mère l'accepte ou Lazar).
   Les refus et le crochet, eux, s'appliquent dès le départ.
2. **Mode de permission.** En `bypassPermissions`, chemins protégés, refus `Edit` et questions disparaissent ; seul le crochet
   resterait. Ne jamais lancer la course dans ce mode. En `acceptEdits`, `sed`, `cp`, `mv`, `rm` sont approuvés d'office dans
   le dossier de travail : une édition du lanceur par motif (`sed -i … scripts/*_v2_v3.py`, qui ne cite pas le nom) passerait le
   crochet — mais le fichier modifié ne peut plus être lancé (empreinte), ce qui est le but de la garde ; l'édition du crochet
   lui-même reste sous chemin protégé (question) et refus `Edit`.
3. **Durée de la course et outil Bash.** Un appel Bash au premier plan est borné (120 s par défaut, 600 s au plus) ; la course
   dure bien plus. Il faut `run_in_background` (champ de l'outil, hors du texte de la commande : la règle et le crochet n'en
   dépendent pas). Si l'outil tuait le lanceur par SIGKILL, le relais de signaux par PID (SIGTERM, SIGINT, SIGHUP) ne jouerait
   pas et l'orchestrateur continuerait sous ses propres plafonds : lancer en arrière-plan.
4. **Trois dépendances hors épinglage** : interpréteur et sa bibliothèque, profils de l'interpréteur de commandes, clone au-delà
   des neuf fichiers (point (e)). Acceptables, à savoir.
5. **Hors objet, vu en route** : `python -m controle_ia.scellement verifier-arbre .` rapporte **1 problème** sans lien avec ce
   dossier : `docs/notes/ideation-organisme-v1/question-mere-reponses/consigne-argon-question-mere-v3.txt.sha256` est une
   empreinte orpheline (fichier scellé absent ; compagnon commité en R-1759). La routine de reprise (R14, étape 1) le verra ;
   à traiter par la mère (R11 : vérifier sur disque avant de déclarer le fichier absent).
6. Ce rapport n'est pas scellé par moi (consigne : un seul fichier nouveau, rien d'autre) ; empreinte donnée dans ma passation,
   à sceller par `python -m controle_ia.scellement sceller`.

## Texte de règle définitif recommandé

`.claude/settings.json` (projet, commité) — la seule différence avec le texte proposé est `-I -B` sur la commande du crochet
(mineur 2) ; les quatre règles sont celles proposées, inchangées :

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 -I -B \"$CLAUDE_PROJECT_DIR/.claude/hooks/garde_calcul.py\""
          }
        ]
      }
    ]
  },
  "permissions": {
    "allow": [
      "Bash(/usr/local/bin/python3 -I -B scripts/lancer_course_ideation_pilier_attaque_v2_v3.py)"
    ],
    "deny": [
      "Edit(//home/user/controle-ia-travail/scripts/lancer_course_ideation_pilier_attaque_v2_v3.py)",
      "Edit(//home/user/controle-ia-travail/scripts/lancer_course_ideation_pilier_attaque_v2_v3.py.sha256)",
      "Edit(//home/user/controle-ia-travail/.claude/hooks/garde_calcul.py)"
    ]
  }
}
```

Après écriture : `/status` dans la session pour voir le fichier chargé ; lancer la course **depuis la racine du dépôt**, en
arrière-plan, dans une session qui a la confiance du dépôt, jamais en `bypassPermissions` ; relais Claude (8787) et Gemini (8788)
démarrés à part (hors de la règle, comme la contre-lecture du v2 l'a noté) ; sinon l'orchestrateur refuse à 0 USD.
