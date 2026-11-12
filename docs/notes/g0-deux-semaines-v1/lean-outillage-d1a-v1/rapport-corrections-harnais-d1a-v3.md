# Essai Lean, outillage D-1a — rapport des corrections du harnais — v3

- **Pour** : la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`. **Écrit par** : l'auteur du harnais (sous-agent développeur,
  Opus 5.5, `claude-opus-5-5`). Heures relevées par `date -u` : contre-lecture courte vérifiée à 01:30:40 UTC ; rapport vers
  01:55 UTC.
- **Lu, empreinte vérifiée** : `contre-lecture-courte-harnais-d1a-v2.md` (`1fea30ab…`, égale à son compagnon), décision R-2302
  (message de la mère : la garde de fond devient la défense principale et obligatoire).
- **Livrable** : commit `5e7c080d8eeb1f3cd57b737dbf97e780e2ae8551` (arbre `707217c9c1f361d3130310a4573a57a798c61fb0`), branche
  `prep/lean-outillage-d1a-v3` partie de `99192fd2`, poussée seule, **sans fusion**. 52 fichiers neufs, aucun fichier existant
  modifié (R12). Empreintes : `empreintes-harnais-v3.txt`.
- **Essais** : 78 essais v3 passent ; les 169 essais v1 et v2 passent toujours (`journal-essais-r5-v3.txt`).
- **Mutations** : 52 sur des copies, **52 tuées**, aucune par délai (`journal-mutations-harnais-v3.json`, script
  `scripts/lean_essai_d1a_v3/mutations_harnais_v3.py`). Méthode : import tracé, `-o pythonpath=` sur la copie, sans
  `PYTHONPATH` hérité.
- **Ni serveur, ni dépense, ni appel de modèle, ni appel à l'API de Hetzner. Aucune valeur de clé.**

## Verdict

- **Conception changée.** Le rejeu du module de l'agent par le noyau est la garde principale (G-L8, neuve). Il tourne dans
  un processus qui n'importe jamais ce module et n'exécute aucun de ses codes. Le fichier de contrôle de la v2, qui
  l'importait, est retiré.
- **Défauts corrigés et éprouvés hors machine** : les trois bloquants (CLC2-01, CLC2-02, CLC2-04) et les cinq à corriger
  (CLC2-03, CLC2-05 à CLC2-08).
- **Premier pas sur la machine.** Ce qui exige Lean (le vérificateur lui-même, l'exécution de code à la compilation) est
  écrit comme premier pas de l'épreuve, avec les items qui le prouvent ; rien d'autre ne se lance avant ce pas.

## La garde de fond (décision de la mère, point 1)

### `verificateur_noyau_v3.lean`

Programme Lean du harnais, lancé par `lean --run` dans un second bac, après la compilation. **Non compilé ici.**

- **Lecture de l'item.** Il lit `Item.olean` par `readModuleData` : le module n'est jamais importé, aucun initialiseur,
  attribut ou extension de l'agent n'est exécuté.
- **Imports.** Les imports déclarés par le module doivent être dans la liste permise. L'environnement est construit à partir
  de ces seuls imports, avec le code épinglé de Mathlib.
- **Rejeu.** Chaque déclaration du module est rejouée par le noyau (`Lean.Environment.replay`).
- **Pour chaque énoncé attendu** :
  - genre ;
  - axiomes (`CollectAxioms`, sur l'environnement rejoué), limités à `propext`, `Classical.choice`, `Quot.sound` ;
  - énoncé **imprimé par le harnais**, dans un environnement où aucune extension de l'agent n'est chargée (le rejeu n'ajoute
    que des constantes : ni instance, ni notation, ni délaborateur de l'agent), en forme ordinaire et en `pp.all` ;
  - **aller-retour** : ce texte, réélaboré par le harnais, doit redonner le type vérifié. L'égalité se juge sur les termes
    (`isDefEq` en transparence réductible), jamais sur le texte.
- **Constantes de l'agent.** Chaque constante non théorème du module est imprimée (type et valeur) pour le relecteur.

### Lancement, épinglage, lecture

- **Lancement (`executeur_bac_v3`)** :
  - second bac `bwrap` et `systemd-run` ;
  - item lié en lecture seule ;
  - `LEAN_PATH` **sans** le dossier de l'item, si bien qu'un `Lean.olean` posé par l'agent ne masque rien ;
  - inventaire du dossier de l'item, réduit à `Item.lean`, `Item.olean` et `Item.ilean`.
- **Épinglage** : la version de la chaîne vient du commit de Mathlib épinglé à l'installation ; l'empreinte du vérificateur
  est inscrite dans `chaine-v1.json` par `epreuve_isolement_v3 epingler-verificateur` ; l'exécuteur refuse tout item si le
  fichier change ensuite.
- **Lecture stricte (`gardes_lean_v3`)** :
  - code 0 ;
  - JSON seulement ;
  - une seule ligne d'imports et une seule ligne de rejeu ;
  - une ligne par nom attendu, aucune hors des noms attendus ;
  - aucun doublon ;
  - le marqueur de fin, au nonce du harnais, en dernier.
- **Gardes par le noyau.** G-L8 (rejeu), G-L2 (axiomes), G-L3 (axiome, constante non sûre ou partielle, import hors liste),
  G-L4 (présent, de genre théorème), G-L5 (énoncé imprimé, aller-retour), G-L6 (constantes imprimées) et G-L7 (intégrité).
- **Seconde ligne.** Les gardes **textuelles** restent en seconde ligne : leur échec reste un échec, mais rien ne repose sur
  elles seules. G-L7 ne dépend plus de G-L3+, car aucun code de l'agent ne tourne dans le vérificateur.

### Pourquoi le rejeu couvre CLC2-01 et CLC2-02

Un texte caché aux gardes textuelles, ou du code exécuté à la compilation, ne peut que :

- **ajouter des déclarations** : elles sont rejouées par le noyau, et une déclaration hors noyau est refusée (G-L8) ;
- **ajouter un axiome** : il est vu par le genre (G-L3) et par les axiomes de l'énoncé (G-L2) ;
- **changer le sens d'un énoncé** (instance, notation, délaborateur) : il est vu par l'aller-retour (G-L5), puisque ces
  extensions ne sont pas chargées ;
- **réécrire l'`.olean`** : il est lu comme des données, puis rejoué ;
- **poser un fichier dans `/item`** : il est vu par l'inventaire (G-L7) et absent de `LEAN_PATH`.

Le lexique et les mots de G-L3+ sont corrigés quand même (ci-dessous).

## Défaut par défaut

| Défaut | Correction (fichier v3) | Essai : cas sain / artefact | Mutations tuées |
|---|---|---|---|
| **CLC2-01** lexique | `gardes_lean_v3.masquer` reprend les prédicats d'identifiant de Lean (lettres ASCII, `isLetterLike`, indices ; `λ`, `Σ`, `Π`, `é` ne sont pas des lettres). Un début de commentaire ou de littéral n'est admis qu'en début de fichier, après un blanc, après un identifiant (commentaire) ou après `(`, `[`, `{`, `⟨`, `⦃` ou `,` ; ailleurs ⇒ refus. Cas sains admis : `f '' s`, `f ⁻¹' s` (note 1). | Artefacts : les trois sources (`//-x`, `\/-1`, `<--`), `«»`, `'a'r"\"`, `1'"'`, `»` seul, `"a"--b`, `(x)'a'`, `é"x"`, `"a"x` ; artefact Lean `gl0_lexique_lean_v3.lean`. Sain : `x₁'`, `ℝ`, `⟨"a", 'b'⟩`, `["a","b"]`, `y--c`, chaîne brute. | l01 à l06 (l05 = n02) |
| **CLC2-02** code exécuté | Défense principale : le rejeu (ci-dessus). Seconde ligne : G-L3+ refuse `simproc`, `dsimproc`, `simproc_decl`, `dsimproc_decl`, les formes Qq (`by_elabq`, `run_cmdq`…), les règles `tactic` d'Aesop, les types de code méta et d'entrées-sorties (`TacticM`, `MetaM`, `CoreM`, `TermElabM`, `CommandElabM`, `SimpM`, `IO`… même qualifiés) et `unsafe…`. | 12 formes refusées ; imports permis admis. Premier pas sur la machine : `noyau_simproc_hors_noyau_v3.lean` et `noyau_run_cmd_hors_noyau_v3.lean` (déclaration hors noyau ⇒ G-L8) ; `gl3_simproc_execution_v3.lean` et `gl3_aesop_tactique_v3.lean` (relevé sans jugement : le code tourne-t-il ?). | t01 à t03, n09, n10, g01 à g15 |
| **CLC2-03** minuterie | `minuterie_v3` : la boucle de destruction et la lecture de `veiller` attrapent **toute** exception sauf `GardeArret`, la journalisent et réessaient. L'absence demande deux lectures (`GET` en 404 **et** absente de l'inventaire). Le refus de nom est journalisé. `hetzner_v3` convertit aussi un corps non UTF-8. | 200 sans « server » (deux fois) puis destruction ; corps `\xff…` converti sans jeton ; un seul 404 ne suffit pas (25 essais bornés) ; refus de nom journalisé, sans DELETE. | h01, h02, m01, m02 |
| **CLC2-04** réponse perdue | **Intention écrite au journal des créations avant l'appel**, échéance armée à l'heure de l'intention ; étiquette unique `creation=<jeton>` sur le serveur. Si l'appel ou la lecture de sa réponse échoue : recherche par étiquette (avec retentatives), destruction par identifiant, journal, arrêt. `detruire --etiquette` rattrape une session coupée. | Intention lue dans le journal **pendant** l'appel ; étiquette sur le corps de la création ; réponse perdue ⇒ serveur 777 trouvé par étiquette et détruit, intention et destruction au journal ; `detruire --etiquette` en ligne de commande. | h03, m05, m06 |
| **CLC2-05** pannes du bac | Un **témoin de montage** (`/usr/bin/true`, mêmes liaisons) est lancé avant chaque exécution ; son échec arrête l'exécuteur. `classer_execution` ne lit plus que le résultat de systemd, jamais une sortie de l'agent. | L'agent qui écrit « bwrap: » n'arrête rien ; témoin en échec ⇒ `ErreurBac` avec le message de `bwrap` ; le bac appelle le témoin avant tout lancement (Lean et Python). | x01, x08 |
| **CLC2-06** pare-feu | `hetzner_v3.verifier_coupure_nuage` lit le serveur : ses pare-feux doivent être **exactement** `[(F, "applied")]` ; puis la seule règle sortante de coupure ; commande `minuterie_v3 verifier-coupure`, qui écrit le relevé au journal. | Sain ; artefacts : « pending », deux pare-feux, aucun ; la commande écrit son journal. | h06 |
| **CLC2-07** plafond par GO | Voir le détail ci-dessous. | `18.52`, `1.96`, `≈ 1 050,40`, `0,30 0,30`, `1,234.5`, `-3,00` ; mot « x », « oui », `N-999`, GO non accordé par Lazar ou inconnu, refusés ; `GO-2026-11-10-13` et `N-013` acceptés ; seconde machine refusée, puis acceptée avec `N-013` ; option `--journal-creations` refusée ; coût du journal (10 USD) qui fait refuser un type sinon admis. | m07 à m11 |
| **CLC2-08** survivantes | n02 (`»` seul), n04 (nom attendu sans ligne), n09 (`set_option` à plusieurs blancs, `skipKernelTC` seul), n10 (imports hors liste), n12 (pause plafonnée à 300 s), n15 (lecture en échec avant l'échéance), n17 (filtre « ipv4 »), n20 (`IPAddressDeny=any`), n21 (`--unshare-all`) : un essai chacune. | voir la colonne « mutations » | l05, g12, n09, n10, m03, m04, h07, x05, x06 |
| **Notes 2, 3, 4, 6** | Inventaire de l'item ; tampon « réseau fermé » périmé au bout d'une heure ; sorties lues en octets et bornées ; devise « EUR » exigée, liste des types sans page suivante. | Fichier `Lean.olean` posé dans l'item ⇒ G-L7 ; tampon vieux d'une heure ⇒ sonde relancée ; « USD » et page suivante refusés. | g13, x07, h04, h05 |

### CLC2-07 : détail de la correction

- **Journal des créations** à chemin fixé dans le code : `…/lean-outillage-d1a-v1/journal-creations-machines-v1.jsonl`. Ce
  n'est pas une option de la commande.
- **Déjà-dépensé** = le plus haut de trois valeurs :
  - le registre des dépenses, lignes à 9 colonnes ;
  - la valeur déclarée (exigée si une ligne n'est pas standard) ;
  - la somme « heures entamées × prix » des machines du journal.
- **Mot de Lazar** : identifiant d'une ligne de `registres/go.md` accordée par Lazar et dans sa période, ou d'une décision
  `N-xxx` de `docs/decisions/`. Il est vérifié.
- **`lire_montant`** : point ou virgule décimale ; plus d'un séparateur ⇒ ligne non standard ; montant négatif ⇒ arrêt.
  Le passage des mutations a fait trouver un vrai défaut : « 1,234.5 » était lu 1,234 ; corrigé.

## Premier pas sur la machine (point 4) : ce qu'il doit établir

`piloter_poste_v3.sh apres` enchaîne `epingler-verificateur` puis `epreuve_isolement_v3 noyau`. Si un attendu du groupe
« noyau » manque, l'épreuve s'arrête (`set -e`).

| Item (`artefacts_r5_v3/`) | Attendu |
|---|---|
| `sain_v1.lean` | rejeu et aller-retour réussis, G-L1 à G-L8 passent |
| `noyau_simproc_hors_noyau_v3.lean` | un `simproc` ajoute `etape_1._hors_noyau : False` (valeur `True.intro`) avec `debug.skipKernelTC` posé par programme ; le rejeu doit la refuser (G-L8) |
| `noyau_run_cmd_hors_noyau_v3.lean` | même déclaration par `run_cmd` ; refusée au rejeu |
| `noyau_instance_enonce_v3.lean` | instance qui fait de `≤` sur ℕ une relation toujours vraie ; l'aller-retour doit échouer (G-L5) |
| `gl3_simproc_execution_v3.lean`, `gl3_aesop_tactique_v3.lean` | **relevé** : la trace `CODE-AGENT-EXECUTE-…` paraît-elle dans la sortie de la compilation ? Réponse à la question « à établir en premier » de CLC2-02 |

## Réserves écrites

1. **Interfaces de Lean non éprouvées.** `verificateur_noyau_v3.lean` est écrit de mémoire contre les interfaces de Lean :
   `readModuleData`, `importModules` (le paramètre `loadExts` éventuel de la version épinglée), `Lean.Replay` et
   `Environment.replay` (`Std.HashMap`), `CollectAxioms`, `Parser.runParserCategory`, `Term.TermElabM.run'`, `ppExpr`,
   `Core.Context`, `ConstantInfo.value?`.
   - Si la chaîne épinglée n'a pas `Lean.Replay`, le repli écrit est `lean4checker` à un commit épinglé, dont `Replay` est
     l'origine.
   - Il en va de même des artefacts du premier pas (`simproc_decl`, `addDecl` avec `debug.skipKernelTC`) : une erreur se
     verra au premier pas.
2. **Aller-retour strict.** Un énoncé qui s'appuie sur une instance ou une notation de l'agent ne se réélabore pas sans les
   extensions de l'agent, et échoue G-L5. C'est voulu, mais c'est un refus de plus, à écrire dans les consignes des bras ;
   l'artefact `gl6_instance_anonyme_v1.lean` échouera aussi G-L5. Les univers polymorphes et les énoncés qui ne se
   réimpriment pas à l'identique (délaborateurs de Mathlib) peuvent aussi échouer : à mesurer au premier pas sur l'item sain.
3. **Imports de l'agent exécutés.** Le vérificateur exécute les initialiseurs des **imports permis** (Mathlib et ses
   dépendances, code épinglé), jamais ceux du module de l'agent. C'est la même confiance que `lean4checker`.
4. **Limite de la minuterie.** La minuterie tourne dans le processus de la session : si la session meurt, l'intention et
   l'étiquette au journal permettent `detruire --etiquette`, mais **personne ne le lance seul**. `garde_calcul.py` ne
   connaît toujours pas Hetzner : c'est hors de ma branche, je ne le propose qu'à titre de proposition.
5. **Notes non traitées** : 16.3 (seccomp, espaces d'utilisateur imbriqués, quota de disque de l'item) et note 5
   (`attribute [simp] a [init] b`, sans effet puisque ce n'est pas du Lean valide).

## Fichiers versés (non committés, scellés)

| Fichier | Empreinte |
|---|---|
| `rapport-corrections-harnais-d1a-v3.md` (ce fichier) | compagnon `.sha256` |
| `journal-essais-r5-v3.txt` | `dde7188d33b024935530264982ba3a98edd69e41e9340c8ab8271b9394297918` |
| `journal-mutations-harnais-v3.json` | `55fec01b5b5b4dca3620f26da7133a807fa6695dc814274f5fac1b2a44429554` |
| `empreintes-harnais-v3.txt` | `bcb2ece6965dceb3fe8787258ebac9b7f67eb1f6f4bfb1935672d652a5029383` |

| Module v3 | Empreinte |
|---|---|
| `verificateur_noyau_v3.lean` | `87a363e7ec824538b48982b762e8e737f91fb35c5207802f5ae0750e9d3c4b36` |
| `gardes_lean_v3.py` | `258b3e2b567f679a508d80852c9edebd1ce381a00f6ee195fc3cb3ec5e379c3f` |
| `executeur_bac_v3.py` | `95e7e09286fc140efa386ac2275eb787df6829c7c93e07be385b206838debfcf` |
| `epreuve_isolement_v3.py` | `286cf93f08eed4a339c84df2833cbead9951012f74c44917a9556e377dfa2e5b` |
| `minuterie_v3.py` | `537abff237a5b8e7d5032408053df44cc79795cd4d3daacf5cc24b680b8364cc` |
| `hetzner_v3.py` | `f84c7673cf81e5bedc145e0d23254f1ec42fc9e01e6e281a98ed03603173bc42` |
