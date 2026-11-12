# Journal du candidat 1 du préenregistrement de la course réelle de l'organisme (code v66, configuration v6) — v1

- **Rédacteur** : Claude Opus 5.5 (`claude-opus-5-5`), rédacteur des brouillons 2 et 3, sous-agent de la session mère
  `session_01VJdZpSMxSdk2SJ1ScmdfNv`.
- **Ordre** : message de la mère portant les mots de Lazar (R-2265, verbatim : « NL-2 go, inscris GO-2026-11-10-11;
  Décisions qui t’attendent : : go recos ») ; même consigne (`bfdc52ad…`) et mêmes interdits communs v2.
- **Heures** (temps universel, relevées par `date -u`, 10 novembre 2026) : début 16:54:11 ; couples écrits à partir de
  16:56:12 ; candidat écrit à 16:58:07 ; passage au lanceur de 16:58:29 à 16:58:44 ; journal écrit à partir de 16:59 (heure
  de fin dans le rapport à la mère).
- **Aucune dépense, aucun appel de modèle, aucun réseau, aucun commit.** Commandes git : `git log`, `git grep` sur
  `registres/go.md` et `registres/decisions.md` seuls, `git show 8053801a:registres/go.md` et
  `git show 0f5a6d9ac:registres/go.md` (registre d'avant l'inscription, pour un artefact), et `git archive` de la tête
  `7e415cba` de l'arbre de l'organisme vers une copie de mon bac à sable (lecture seule ; demandé par la mère pour le passage
  au lanceur). Aucun refus de permission ni de classifieur. Brouillons 1 à 3 intacts (`736e3fd6…`, `f87ad0e4…`, `04598de6…`).

## 1. Entrées vérifiées et sorties

Entrées : brouillon 3 `04598de62300185806975ae5df5fcdd054557f9a46b935e40d7d3479c240ec23` ; `registres/go.md`
`8de009e115e263225746e734812dc0d9b5dd46c0407bf1727255c2d37c8d72b1` (égal au fichier du commit `8053801a`, comme le dit la
mère ; ligne GO-2026-11-10-11, ligne 301, une seule) ; blocs v66 `9933ee11…` ; R-2265 lu au registre.

| fichier (`docs/notes/organisme-boucle-reelle-v1/`) | sha256 |
|---|---|
| `preenregistrement-boucle-reelle-organisme-v1-candidat1.md` | `46d7545b489a2037ede235d843ef8a0c504461a0a2d697af5db40de2400fd89d` |
| `couples-candidat1-boucle-reelle-v1.json` | `a84785ac867a486aafa781bbdcb25f2ddbb6204efea3d05cce12251148781224` |
| `faire-candidat1-boucle-reelle-v1.py` | `ec4d474393b33f3cffa807c517828b46939bf35107b0070cd3f5ceeb09b00e35` |
| `journal-candidat1-boucle-reelle-v1.md` | ce fichier (empreinte à son compagnon) |

Commande (depuis `/home/user/controle-ia-travail`) : `.venv/bin/python -I -B docs/notes/organisme-boucle-reelle-v1/faire-candidat1-boucle-reelle-v1.py --depot /home/user/controle-ia-travail --candidat docs/notes/organisme-boucle-reelle-v1/preenregistrement-boucle-reelle-organisme-v1-candidat1.md --couples docs/notes/organisme-boucle-reelle-v1/couples-candidat1-boucle-reelle-v1.json` → code 0 ; jouée d'abord dans mon bac à sable, même candidat à l'octet.

**Contrôles du script** : **aucun marqueur** au motif du lanceur (`<<[A-Z0-9_-]+>>`) ; trois blocs égaux à l'octet à ceux du
développeur, la ligne `go` du plan portant GO-2026-11-10-11 ; aucune des tournures périmées listées (« brouillon 3, non
scellé », « Marqueurs restants », « v<N> », renvois à la ligne C1 pour le cas sans retenue, noms de marqueurs…) ne reste ; la
ligne de GO et le mot de Lazar sont **lus dans le registre** par le script, non recopiés à la main.

## 2. Couples : 33

| id | gelée | constat | objet |
|---|---|---|---|
| C1-01 | non | CLB-04 (1) | titre : « v1 (candidat 1) » |
| C1-02 | non | CLB-04 (1) ; R-2265 | statut du candidat 1 |
| C1-03 | non | CLB-04 (6) | rédacteur |
| C1-04 | non | CLB-04 (6) | heures |
| C1-05 | non | CLB-04 (6) ; R-2265 | consigne et message |
| C1-06 | non | CLB-04 (2) ; NL-2 ; R-2265 | ligne de GO, mot de Lazar, registre après inscription (`8de009e1…`, commit `8053801a`) |
| C1-07 | non | R-2265 | registre : R-2265 |
| C1-08 | non | CLB-04 (6) | arbres (`main` à `8053801a`) |
| C1-09 | non | NL-2 | pièce : ligne de GO de la course |
| C1-10 | non | candidat 1 | pièces versées |
| C1-11 | non | NL-1 (b) | section 0, point 6 : issue C7 |
| C1-12 | non | CLB-04 (3) | section 0, point 8 : ce qui reste |
| C1-13 | **oui** | NL-1 (b) ; R-2265 | fin de la ligne C1 : mot de Lazar, issue C7 |
| C1-14 | **oui** | NL-1 (b) ; journal du brouillon 3, § 3 | ligne C7 insérée avant C1 (texte tenu prêt, à l'octet) |
| C1-15 | **oui** | NL-1 (b) ; idem | V-8 : issue C7 |
| C1-16 | **oui** | NL-1 (b) ; idem | A1 d'office sous C1 ou C7 |
| C1-17 | **oui** | CLB-04 (8) | nom du texte scellé, `…-v1-v1.md` (liste d'arrêt) |
| C1-18 | non | NL-1 (b) | section 11 : issue C7 |
| C1-19 | non | CLB-04 (6) ; R-2265 | 12.2, points 1 à 3 au passé ; phrase du validateur gardée |
| C1-20 | non | CLB-04 (8) | commande : nom du texte scellé |
| C1-21 | non | CLB-04 (2) ; NL-2 ; R-2265 | section 13 : identifiant et mot de Lazar |
| C1-22 | non | CLB-04 (8) | section 13 : nom du texte scellé |
| C1-23 | non | NL-2 ; R-2265 | section 13 : ligne de GO recopiée à l'octet (bloc de code) |
| C1-24 | non | NL-1 (b) | section 14 : issue C7 |
| C1-25 | non | CLB-04 (7) | section 15 : empreinte entière de la consigne de la contre-lecture 1 |
| C1-26 | non | CLB-04 (7) | section 15 : pièces du candidat 1 |
| C1-27 | non | CLB-04 (7) | section 15 : CLB-04 réglé |
| C1-28 | non | CLB-04 (7) | section 15 : vérification courte sur ce texte, consignée au registre |
| C1-29 | non | CLB-04 (7) | section 15 : empreinte entière de la contre-lecture du code v65 |
| C1-30 | non | CLB-04 (7) | section 15 : empreinte entière de la contre-lecture du code v66 |
| C1-31 | non | NL-1 (b) | section 15 : CLV66-04, issue C7 |
| C1-32 | non | NL-2 | section 16, introduction : identifiant de la ligne de GO |
| C1-33 | non (bloc lu par le lanceur) | NL-2 ; R-2265 | identifiant porté aux trois occurrences restantes (12.1, commande de 12.4, ligne `go` du bloc `plan-gele-v66`) |

**Sections gelées** : C1-13 à C1-16 portent l'option (b) de NL-1, décidée par Lazar (R-2265), avec les textes tenus prêts au
journal du brouillon 3, à l'octet ; C1-17 remplit le nom du texte. Aucune hypothèse, prédiction, signe ni seuil ne change ;
le seul changement de critère est celui que Lazar a décidé (issue C7).

**Section 15** : contre-lecture 1, brouillon relu `f87ad0e40f1b2941e66d343bfb4b5eeaaefa22a3e2eeb448f852900de112b8a7`, rapport
`90ba927ec9ec390026f3d2dbbab2fe32f1e8ff8bb553f49a15842ce5e420395c`, couples `a555f82c…` (entier dans le texte), consigne
`0042d919…` (entière) ; contre-lectures du code v65 `c4ddfc7f…` et v66 `a2880368…` (entières). La vérification courte du
candidat ne peut pas être citée par le texte qu'elle relit : le texte dit qu'elle se consigne au registre avec le scellement.

## 2 bis. Passage au lanceur de l'organisme (validateur qui fait foi)

**Copie** (bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/prereg-course-v66/c1/lanceur/`) :
`git archive 7e415cbaaa3ff602db43a44dad6b4307c08352c7 orchestrator` extrait dans `arbre/` ; le candidat copié à l'octet
sous `arbre/orchestrator/prereg/preenregistrement-boucle-reelle-organisme-v1-v1.md` (`46d7545b…`) et scellé par
`controle_ia.scellement sceller` ; dossier de course `course/` = `code-v66/configuration-v6/` versé, plus
`heritage-depart-v65.json` (`93dcf517…`) et son compagnon ; `registres/go.md` copié (`8de009e1…`).

**Commande** (celle de la section 12.4, avec `--verifier-seulement` ; deux écarts dits : l'interpréteur est
`/home/user/controle-ia-travail/.venv/bin/python` et `TMPDIR` pointe dans le bac à sable) :
`env -i PATH=/usr/sbin:/usr/bin:/sbin:/bin HOME=/root LANG=C.UTF-8 TMPDIR=…/lanceur/tmp POLE_MACHINE_JETABLE_V56=1 …/python -I -B demonstrations/boucle_reelle_v66.py …/lanceur/sortie --preenregistrement prereg/preenregistrement-boucle-reelle-organisme-v1-v1.md --heritage-depart …/course/heritage-depart-v65.json --configuration …/course/configuration-boucle-reelle-v6.json --moteur reel --confirmer-moteur-reel --registre-go …/registres/go.md --go GO-2026-11-10-11 --bac reel --utilisateur-bac 64097 --verifier-seulement`

| cas | code | ce que rend le lanceur (sortie d'erreur, telle quelle) | empreinte de la sortie |
|---|---|---|---|
| **sain** (16:58:29 → 16:58:30) | **2** | `refus : MachineRefusee : machine : bwrap ≥ 0.9 exigé (lu : None) : refus avant tout appel` ; sortie standard vide ; aucun dossier de sortie écrit | `73afff90…` |
| artefact : `--go GO-2026-11-08-02` | 2 | `refus : GoAbsent : mode réel : --registre-go et --go GO-2026-11-10-11 (celui du texte scellé) exigés` | `d6390f4e…` |
| artefact : registre d'avant l'inscription (`2c396b01…`, commit `0f5a6d9ac`) | 2 | `refus : GoAbsent : A15 : GO-2026-11-10-11 absent du registre …` | `4e7ebb8b…` |

**Lecture** : dans l'ordre du lanceur (texte, monde, empreinte de la configuration, GO, contenu de la configuration,
garde 17, garde 22), le cas sain passe le texte (chemin et nom fixés, sceau, aucun marqueur, 98 empreintes de code égales à
l'arbre, plan gelé, jeu planté), le monde, la configuration v6, la ligne **GO-2026-11-10-11 lue à 45 USD** et la garde 17
(héritage de départ et son compagnon), puis **refuse à la garde 22 sur la seule absence de `bwrap`**, refus attendu ici. Les
deux artefacts montrent que le GO est bien lu dans le plan du texte et dans le registre. Rien n'a été appelé, aucune porte de
plafond posée.

## 3. Ce qui reste

- Vérification courte du différentiel brouillon 3 → candidat 1, puis scellement sous le nom
  `preenregistrement-boucle-reelle-organisme-v1-v1.md` (choix du numéro 1 : premier texte scellé de cette course ; à
  changer par un couple si la mère en veut un autre).
- Sur la machine : préalables de la section 12.3 (garde 22 en situation).
- Non réglé par R-2265, rappelé par la mère : la session qui porte les clés et loue la machine.
