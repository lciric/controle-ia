# Vérification courte du candidat 1 du préenregistrement de la course réelle de l'organisme (différentiel du brouillon 3) — v1

- **Vérificateur** : Claude Fable 5.2 (`claude-fable-5-2`), sous-agent neuf de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv` ; autre modèle que le rédacteur (Claude Opus 5.5) ; n'a écrit ni ce texte, ni le code v65 ou v66, ni leurs contre-lectures.
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-verification-courte-course-candidat1-v1.md`, `62708e549655175283df040827efac6793d2ed0f03dd5ae0b73f70076a0bf4e2` (vérifiée par `sha256sum` avant lecture).
- **Heures** (temps universel, relevées par `date -u`, 10 novembre 2026) : début 17:00:39 ; rejeux du lanceur de 17:02:07 à 17:02:50 ; rapport écrit à 17:03.
- **Aucun appel de modèle, aucune dépense, aucun réseau, aucun commit.** Commandes git : `git status`, `git log`, `git rev-parse HEAD` et `git archive 7e415cba… orchestrator` sur l'arbre de l'organisme (lecture seule, vers le bac à sable), `git show 8053801a:registres/go.md` et `git show 0f5a6d9ac:registres/go.md` (registre d'avant l'inscription, pour un artefact). Aucun refus de permission ni de classifieur. Aucun chemin interdit ouvert ; aucune recherche récursive.
- **Bac à sable** : `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/verif-course-c1/` (rejeu du script, outil de comparaison `outils/comparer.py`, copie de l'arbre et sorties du lanceur sous `lanceur/`).

## Verdict

**Scellable.** Aucun constat bloquant ; aucun couple de correction. Trois remarques non bloquantes (VCC-7 à VCC-9), sans effet sur le texte.

## Pièces lues, empreintes vérifiées sur disque (toutes égales à leur compagnon `.sha256`)

| pièce (`docs/notes/organisme-boucle-reelle-v1/` sauf mention) | sha256 |
|---|---|
| `preenregistrement-boucle-reelle-organisme-v1-candidat1.md` | `46d7545b489a2037ede235d843ef8a0c504461a0a2d697af5db40de2400fd89d` |
| `couples-candidat1-boucle-reelle-v1.json` | `a84785ac867a486aafa781bbdcb25f2ddbb6204efea3d05cce12251148781224` |
| `faire-candidat1-boucle-reelle-v1.py` | `ec4d474393b33f3cffa807c517828b46939bf35107b0070cd3f5ceeb09b00e35` |
| `journal-candidat1-boucle-reelle-v1.md` | `0d67b705705c9d9a43bdc255431ed2386859b687facde79c5d8a8a134db6b55c` |
| `preenregistrement-boucle-reelle-organisme-v1-brouillon3.md` | `04598de62300185806975ae5df5fcdd054557f9a46b935e40d7d3479c240ec23` |
| `journal-brouillon3-boucle-reelle-v1.md` | `0dc830bc9a5318d9cf12be2c49ebb546899de457157cca79a1bd2f3776e40919` |
| `registres/go.md` (disque, et `git show 8053801a:registres/go.md`) | `8de009e115e263225746e734812dc0d9b5dd46c0407bf1727255c2d37c8d72b1` |
| arbre de l'organisme `/home/user/organisme-v65-cl` | tête `7e415cbaaa3ff602db43a44dad6b4307c08352c7` |

Registre lu : R-2253, R-2254, R-2265 (et R-2266, lancement de cette vérification), `registres/decisions.md`.

## Constats

**VCC-1 (mandat 1, tenu) — rejeu à l'octet.** `.venv/bin/python -I -B docs/notes/organisme-boucle-reelle-v1/faire-candidat1-boucle-reelle-v1.py --depot /home/user/controle-ia-travail --candidat <bac>/rejeu/candidat1-rejoue.md --couples <bac>/rejeu/couples-rejoues.json` → code 0 ; sortie `46d7545b…`, **égale à l'octet au candidat** (`cmp`) ; 33 couples ; fichier des couples rejoué égal au fichier déposé, champ `sortie.chemin` mis à part (seul champ qui dépend du chemin de sortie). Le script lit le brouillon 3 (`04598de6…`), le registre (`8de009e1…`) et les blocs du développeur (`9933ee11…`) et s'arrête sur toute empreinte différente ; la ligne de GO et le mot de Lazar sont lus dans le registre, non recopiés à la main.

**VCC-2 (mandat 2, tenu) — NL-1 (b), sections gelées comparées par programme.** Découpe du brouillon 3 et du candidat par titres `## ` : mêmes 19 sections, même ordre. Sections **égales à l'octet** : 1, 2 (hypothèse), 3 (dessin), 4 (prédictions et signes), 5 (métriques), 6 (seuils), 7 (plan d'analyse). Sections gelées changées : 8, 9, 10 ; pour chacune des huit sections gelées déclarées, le brouillon 3 auquel on applique **les seuls couples C1-13 à C1-17** redonne la section du candidat à l'octet. Différence ligne à ligne des sections gelées, entière :
- section 8 : la ligne C7 insérée juste avant la ligne C1 (C1-14) ; la fin de la ligne C1 (C1-13) ; la ligne V-8 (C1-15) ;
- section 9 : « déclenché d'office si C1 » → « déclenché d'office si C1 ou C7 » (C1-16) ;
- section 10 : nom du texte scellé, `…-v1-v<N>.md` → `…-v1-v1.md` (C1-17).

Égalité aux textes préparés du journal du brouillon 3 (section 3, option (b)) : la ligne C7 du journal, extraite par programme, se retrouve **à l'octet, une seule fois**, juste avant la ligne C1 du candidat, et `nouveau` de C1-14 = ligne préparée + retour de ligne + `ancien` ; C1-16 égal au couple préparé 2, à l'octet ; C1-15 égal au couple préparé 3, les deux côtés prolongés de la même barre de fin de cellule (« … ligne C1 \| » → « … (ligne C7) \| ») ; le texte du marqueur `NOEUD_C1_SANS_RETENUE` (« l'issue est C7 « la chaîne garde, boucle non éprouvée » (ligne C7, lue avant C1) ») est dans C1-13, à l'octet. **Aucune autre issue changée** : les lignes C5, C4, C2, C3, C6 et le reste de C1, les vérifications V-1 à V-7, les mesures sans issue sont inchangés (différence ci-dessus exhaustive). Aucune hypothèse, prédiction, signe ni seuil changé. L'ordre de lecture reste cohérent : « la première ligne qui s'applique donne l'issue », C7 placée avant C1 ; le programme gelé (issues C1 à C6) n'est pas changé, la ligne C7 le dit (« le programme gelé rend C1 dans ce cas, le lecteur du verdict écrit C7 (V-8) »), et la section 8 portait déjà « quand le programme et ces vérifications divergent, l'issue du texte prime ».

**VCC-3 (mandat 2, tenu) — mots de Lazar et R-2265 exacts.** Verbatim de la ligne GO-2026-11-10-11 du registre : « NL-2 go, inscris GO-2026-11-10-11; Décisions qui t’attendent : : go recos » ; **égal à l'octet** au verbatim de R-2265 ; présent 4 fois dans le candidat, toujours entre guillemets et à l'octet (en-tête, ligne C1 de la section 8, section 13, ligne de GO recopiée). R-2265 consigne bien « NL-1 (b) (issue à part « la chaîne garde, boucle non éprouvée », prononcée par le lecteur du verdict, aucun code changé) » parmi les décisions prises selon les recommandations ; le journal du brouillon 3 donnait l'option (b) comme recommandée (0,6). L'heure (« vers 16:53 UTC ») est celle de R-2265.

**VCC-4 (mandat 3, tenu) — GO-2026-11-10-11 aux cinq endroits, ligne à l'octet.** Les cinq occurrences du marqueur `GO_COURSE_V66` du brouillon 3 (lignes 40, 578, 685, 707, 891 : en-tête, 12.1, commande de 12.4, section 13, ligne `go` du bloc `plan-gele-v66`) portent toutes GO-2026-11-10-11 dans le candidat (lignes 40, 580, 686, 708, 907). La ligne du registre (une seule ligne `| GO-2026-11-10-11 |` dans `registres/go.md` à `8de009e1…`) est dans le candidat **à l'octet, une fois, dans un bloc de code** (section 13) ; égale au champ `ligne_go_recopiee` des couples. Section 16 : seules différences avec le brouillon 3, la phrase d'introduction (C1-32) et la ligne `go:` ; le script contrôle en plus que les trois blocs sont égaux à ceux du développeur, la ligne `go` mise à part.

**VCC-5 (mandat 4, tenu) — lanceur en vérification seule, sur une copie.** Copie : `git archive 7e415cba… orchestrator` extraite sous `<bac>/lanceur/arbre/` ; candidat copié à l'octet sous `arbre/orchestrator/prereg/preenregistrement-boucle-reelle-organisme-v1-v1.md` (`46d7545b…`), scellé par `controle_ia.scellement sceller` ; dossier de course = `code-v66/configuration-v6/` (configuration `4743ddbe…`) plus `heritage-depart-v65.json` (`93dcf517…`) et son compagnon ; `registres/go.md` copié (`8de009e1…`). Commande de la section 12.4 avec `--verifier-seulement`, deux écarts dits (interpréteur `/home/user/controle-ia-travail/.venv/bin/python`, `TMPDIR` dans le bac à sable) ; lanceur en superutilisateur (uid 0) ; `bwrap` absent de la machine.

| cas | code | sortie d'erreur, telle quelle (sortie standard vide partout ; aucun dossier de sortie écrit) |
|---|---|---|
| **sain** | 2 | `refus : MachineRefusee : machine : bwrap ≥ 0.9 exigé (lu : None) : refus avant tout appel` (empreinte `73afff90…`, égale à celle du journal du candidat) |
| artefact : `--go GO-2026-11-08-02` | 2 | `refus : GoAbsent : mode réel : --registre-go et --go GO-2026-11-10-11 (celui du texte scellé) exigés` (`d6390f4e…`, égale à celle du journal) |
| artefact : `--go GO-2026-11-10-10` | 2 | même refus |
| artefact : registre d'avant l'inscription (`2c396b01…`, commit `0f5a6d9ac`, aucune ligne GO-2026-11-10-11) | 2 | `refus : GoAbsent : A15 : GO-2026-11-10-11 absent du registre …` |
| artefact : un mot du texte changé, sceau non refait | 2 | `refus : PreenregistrementRefuse : préenregistrement non scellé (compagnon .sha256 absent ou non conforme) …` |
| artefact : marqueur `<<GO_COURSE_V66>>` ajouté, sceau refait | 2 | `refus : PreenregistrementRefuse : marqueur(s) non rempli(s) : ['<<GO_COURSE_V66>>']` |
| sain, après restauration du texte (`46d7545b…`) | 2 | même refus que le cas sain (garde 22) |

Lecture, d'après le code du lanceur (`demonstrations/boucle_reelle_v66.py`, lignes 407 à 432 de la copie) : en mode réel l'ordre est texte scellé (garde 6 : chemin et nom, sceau, marqueurs, empreintes du code, plan, jeu planté), monde, empreinte de la configuration, identifiant et registre du GO (montant 45 USD), contenu de la configuration, garde 17 (héritage de départ), puis garde 22 (`exiger_machine`). Le cas sain franchit donc tout ce qui précède et **n'est refusé que par l'absence de `bwrap`** ; les artefacts montrent que le GO du plan, le registre, le sceau et les marqueurs sont bien lus.

**VCC-6 (mandat 5, tenu) — aucun marqueur ; nom du texte scellé.** Motif du lanceur `<<[A-Z0-9_-]+>>` : aucune occurrence ; aucune suite `<<` ni `>>` dans le candidat ; aucune des tournures `v<N>`, `{N}`, `<N>`, « brouillon 3, non scellé », « à remplir », noms de marqueurs. Le nom `preenregistrement-boucle-reelle-organisme-v1-v1.md` apparaît 6 fois (statut, liste d'arrêt en section 10, section 12.2 deux fois, commande de 12.4, section 13), sans autre variante ; il satisfait le motif du lanceur (`NOM_PREREG` : `^preenregistrement-boucle-reelle-organisme-v1-v[1-9][0-9]*\.md$`, sans « brouillon », dans `orchestrator/prereg/`) et a été accepté par lui (VCC-5). Empreintes entières ajoutées en section 15 vérifiées sur disque : consigne de la contre-lecture 1 `0042d919…4d23`, contre-lecture du code v65 `c4ddfc7f…ed03`, du code v66 `a2880368…7b00`, rapport de la contre-lecture 1 `90ba927e…395c`. L'affirmation de 12.2 sur l'outil `preparer_boucle_reelle_v66.py` (n'accepte que GO-2026-11-08-02 ou GO-2026-11-10-10) est exacte (ligne 38 de l'outil).

### Remarques non bloquantes (aucun couple)

**VCC-7 — limite du rejeu.** Hors d'une machine à `bwrap`, rien de ce qui suit la garde 22 n'est joué (sonde du bac, identité de l'utilisateur dédié, garde 15 de l'environnement, portes des relais, `exiger_go`, familles séparées). Le texte le dit et renvoie aux préalables de la section 12.3 ; le verdict « scellable » porte sur le texte, non sur ces préalables.

**VCC-8 — le mot de Lazar ne nomme pas NL-1.** Le verbatim ne dit que « go recos » pour les décisions en attente ; l'option (b) vient de la recommandation écrite (journal du brouillon 3, 0,6) et de sa consignation à R-2265. Le candidat cite le verbatim, « NL-1, option (b) » et R-2265 ensemble, ce qui est exact et traçable ; rien à changer.

**VCC-9 — statut écrit au conditionnel.** Le texte scellé gardera « candidat 1 au scellement… si la vérification courte du différentiel le dit scellable » et « (candidat 1) » au titre, au lieu du « texte scellé, version N » proposé au journal du brouillon 3 ; la vérification courte y est renvoyée au registre (un texte ne peut pas porter l'empreinte du rapport qui le relit). C'est cohérent et vrai au moment du scellement, à condition que la mère consigne au registre le chemin, l'empreinte et le verdict de ce rapport avec le scellement, comme la section 15 le promet.

## Ce qui reste (hors de ce mandat)

Scellement sous le nom `preenregistrement-boucle-reelle-organisme-v1-v1.md`, dépôt et consignation au registre ; copie à l'octet dans l'arbre de l'organisme de la machine ; préalables de la section 12.3 ; session qui porte les clés et loue la machine (non réglé par R-2265).
