# Vérification de l'écart candidat 1 → candidat 2 — lentille « rejeu et versement » — addendum 2 de P3 — v1

**Verdict : scellable.** Le script rejoué sur des copies redonne le candidat 2 octet pour octet (`5d5e5aa8…`). Il refuse
sans rien écrire : un candidat 1 d'autre empreinte, une ancre « Date (UTC) » absente ou en double, un ancien texte absent
ou en double, un élément « Candidat 2 » mal formé. Les neuf empreintes des lignes changées égalent les fichiers qu'elles
désignent. `prereg.problemes` rend `[]`. La garde 1 lit une seule empreinte de module (`96727076…`) et une seule de
tests (`f9136b6d…`). Les six entrées « Contre-lecture » sont numérotées 1 à 6, chacune avec au moins deux empreintes.
Résultat identique avec l'entrée 7 prévue (sept entrées). Le plan v2 est juste : 35 sources à l'empreinte écrite ;
destinations uniques, sous `prereg/` ou `docs/`, absentes du dépôt ; tests v4 au chemin des tests du module. Aucune
correction du texte. Sept constats pour information, dont trois à faire au versement (VE-R-01, 02, 04).

| id | gravité | constat (une ligne) |
|---|---|---|
| VE-R-01 | information | Les deux rapports de la contre-lecture 7, cités par l'entrée prévue, manquent au plan v2 (ils naissent après lui) |
| VE-R-02 | information | Le script du texte final (`ecrire_texte_final_addendum2_v1.py`, `1f3933f8…`) n'est pas dans la consigne, pas cité, pas dans le plan. Essayé sur copies : sortie = candidat 2 + entrée 7 ; il refuse les chevrons |
| VE-R-03 | information | `prereg.problemes` ne voit pas les chevrons simples de l'entrée 7 (`<A>`, `<verdict A>`) ; seul le script du texte final les arrête |
| VE-R-04 | information | Le plan ne liste aucun compagnon `.sha256`. 11 pièces sur 35 changent de nom et 9 sources n'ont pas de compagnon : un compagnon copié porterait un mauvais nom |
| VE-R-05 | information | « Texte final : le candidat 2 et cette entrée » n'est vrai que si les deux vérificateurs de l'écart rendent « scellable » |
| VE-R-06 | information | Script du candidat 2 : élément lu sans contrôle d'empreinte, sortie écrasée sans contrôle, un message pour trois causes. Sans effet sur le candidat 2 |
| VE-R-07 | information | Quatre chemins cités naîtront au versement, au scellement ou après, plus les deux rapports de l'entrée 7 (liste en section 4) |

Chemins relatifs à `…/scratchpad/addendum2-p3/verification-ecart-candidat2-rejeu/`, sauf mention ; `…/addendum2-p3/`
est le dossier de travail de l'addendum 2.

## Cadre

- Vérificateur : sous-agent neuf. Je n'ai écrit ni l'addendum 2 (aucun brouillon, aucun candidat, aucun script), ni
  aucune version de son module ou de ses tests, ni aucune contre-lecture, vérification ou traitement antérieurs.
  Date : 2026-10-20, de 21:53:17 à 22:05 UTC environ.
- Écritures : seulement sous ce dossier (`copies/`, `rejeu/`, `artefacts/`, `outils/`, `journaux/`, ce rapport).
- Dépôt en lecture seule. git lu avec `--no-optional-locks`. Fichier lu : `src/controle_ia/prereg.py` (en entier).
  Pour `src/controle_ia/gardes.py` et `scellement.py`, seulement les imports et la forme du niveau module (par `ast`) :
  aucun effet à l'import. Le reste du dépôt n'est lu que par l'existence de chemins exacts. Aucune recherche récursive.
- Le module de l'addendum 2 n'est jamais importé : ses expressions de la garde 1 et ses chemins (`PREREG_ADDENDUM2`,
  `CHEMIN_MODULE`, `CHEMIN_TESTS`) sont lus par `ast`.
- Lancements : interpréteur de la consigne (Python 3.11). Script et outils en `python -I -B`. Le seul outil qui importe
  `controle_ia.prereg` tourne depuis la racine du dépôt, avec `PYTHONPATH=src`, `python -B -s` et
  `PYTHONDONTWRITEBYTECODE=1`. Aucun `__pycache__` créé : `src/controle_ia/__pycache__` garde sa date du
  2026-10-19 23:20:33 UTC et ses fichiers ; mes dossiers n'en ont pas.
- Pendant mon travail, la session a fait le commit `49b482fa…` (21:57:07 UTC, « R-296 et GO-2026-10-20-10 … »). Il ne
  touche que `registres/decisions.md` et `registres/go.md` (`journaux/depot-commits-pendant.txt`). J'ai refait tous
  les contrôles d'existence à cette tête : résultats égaux (`journaux/controles-ecart-fin.log`). `git status
  --porcelain` est vide aux deux bouts.
- Le script du texte final (`…/addendum2-p3/candidat/ecrire_texte_final_addendum2_v1.py`, écrit à 21:52:45 UTC) n'était
  pas dans la consigne. Je l'ai lu comme une donnée et essayé sur des copies (VE-R-02).

## Pièces (empreintes recalculées ; égales à la consigne et aux compagnons, au début et à la fin)

| pièce (sous `…/addendum2-p3/`) | sha256 |
|---|---|
| candidat 1 `candidat/P3-addendum2-audit-verdict-v1-candidat1.md` | `9900a721560c87361efcf60660863727644e8fdc3ab88e4fd1f325a613306b0e` |
| rapport de la contre-lecture 6 `verification-candidat1/verification-candidat1-addendum2-P3-v1.md` | `3f0dce9ba99ab692b2d47660457a28b969ac3b0ac04b43f931f0101f05283f04` |
| candidat 2 `candidat/P3-addendum2-audit-verdict-v1-candidat2.md` | `5d5e5aa83c57d37e6406ea1d57e87bc841c8e69e22a4918324a36b2b877bc247` |
| script `candidat/ecrire_candidat2_addendum2_v1.py` | `51c7bd1b4886e43fd6a4bc80c8a11fbed3813c5307cd00b532c833d2295d5943` |
| élément `candidat/ligne-candidat2-addendum2-v1.md` | `7e106f17410587947775451f7ea58df978853b0e051338ba522c63d98b028568` |
| plan `candidat/plan-versement-addendum2-v2.json` | `6d312445bf7fa63bbea821c2a46c7d91f40918c1e5fe2df8190ae8594cdef39f` |
| module `module-v4/audit_verdict_p3_v1.py` | `967270761c92ce3875695b8e5da5a985295c963b324dd120a31d09db663f132d` |
| tests v4 `module-v4/test_audit_verdict_p3_v1.py` | `f9136b6dc5eebce6d9e9101fa910646b16fa544f0ee1d3a997030eb9319dbc07` |
| journaux v4 `module-v4/journaux/pytest-suite-v4-garde-r1.log` ; `r1-suite-v4.jsonl` | `cb24c899aa490bfa98e00b370c0ad388f13ddfbce6f277b21bd368a24ba12c36` ; `f2a4be52af0304831d77abeb36d78c46bb073f1a606f7eb56e3b0e3f576b3edd` |
| hors consigne : `candidat/ecrire_texte_final_addendum2_v1.py` | `1f3933f84bb8cacacdb185b848d3fa01a0fa86340c5a6c3c40c51a019f20322d` |
| validateur du dépôt `src/controle_ia/prereg.py` | `3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306` |

Les compagnons de `candidat/` (huit), `module-v4/`, `module-v4/journaux/` et du rapport de la contre-lecture 6 sont
justes (`journaux/compagnons-et-heures.log`).

## 1. Rejeu du script

**Docstring.** Elle dit ce que fait le script : trois arguments (candidat 1, élément, sortie) ; empreinte du candidat 1
vérifiée avant usage du texte (les octets sont lus pour le hachage, puis décodés seulement si l'empreinte est juste) ;
élément inséré tel quel juste avant « Date (UTC) » ; sortie écrite en entier, empreinte imprimée et écrite dans
`SORTIE.sha256` ; corrections VC1-01 à VC1-05 ; chaque ancien texte trouvé une seule fois ; aucun import du dépôt
(seulement `hashlib`, `sys`, `pathlib`). Plus de « candidat_essai_v1.py », plus de « fictives ici » (VC1-01, point 3).

**Rejeu** (`journaux/rejeu-script.log`). Copie du script dans `rejeu/`, copies du candidat 1 et de l'élément dans
`copies/` : `python -I -B rejeu/ecrire_candidat2_addendum2_v1.py copies/…candidat1.md copies/ligne-candidat2-addendum2-v1.md
rejeu/candidat2-rejoue.md` → code 0, empreinte imprimée `5d5e5aa83c57…7bc247` ; `cmp` avec le candidat 2 : identique
octet pour octet. Le compagnon écrit a la même empreinte (son nom de base suit le nom de sortie).

**Mots exacts du rapport, au sens de la docstring** (contrôle d'appoint ; la lentille « mots exacts » est l'autre
vérificateur). `outils/controles_ecart_v1.py`, partie B : les corrections sont extraites du rapport de la contre-lecture 6
lui-même, entre guillemets appariés après « remplacer » / « par » et « ajouter après l'entrée 5 ». Ce sont sept
remplacements (VC1-01, 02, 03, 04 deux fois, 05) et l'ajout de l'entrée 6, `<empreinte de ce rapport>` rempli par
`3f0dce9b…`. Appliqués au candidat 1 aux espaces près, avec l'élément « Candidat 2 » avant « Date (UTC) », ils donnent
le candidat 2 aux espaces près. Chaque ancien texte est trouvé une fois. Seuls les retours à la ligne et l'indentation
sont choisis par le script. Blocs changés : l. 20, l. 22-24 → 22-33, l. 638-641 → 647-667. Ma première exécution de
cet outil cherchait « remplacer » en minuscule seulement : il manquait VC1-02 et VC1-05, d'où un faux écart.
Corrigé (`[Rr]emplacer`) puis relancé : 0 écart. Le journal gardé est celui de la seconde exécution.

**Artefacts** (`outils/artefacts_script_v1.py`, `journaux/artefacts-script.log`). Chaque cas tourne sur des copies, dans
un processus neuf. Pour l'ancre et l'ancien texte, une copie du script vise l'empreinte de l'entrée altérée : seule sa
constante `CANDIDAT1` change, sinon le contrôle d'empreinte refuse avant. Script d'origine sur une ancre absente :
refus par l'empreinte.

| cas | code | sortie écrite | message |
|---|---|---|---|
| sain | 0 | oui, `5d5e5aa8…` | empreinte imprimée |
| candidat 1 d'autre empreinte (un octet changé) ; un octet ajouté | 1 ; 1 | non ; non | « candidat 1 : empreinte inattendue » |
| ancre absente, script d'origine | 1 | non | « candidat 1 : empreinte inattendue » |
| ancre absente ; ancre en double (script visé) | 1 ; 1 | non ; non | « élément « Candidat 2 » mal formé, ou ancre « Date (UTC) » absente ou en double » |
| ancien texte absent ; en double (script visé) | 1 ; 1 | non ; non | « trouvé 0 fois (une attendue) » ; « trouvé 2 fois » |
| élément sans « - » ; élément sans fin de ligne | 1 ; 1 | non ; non | même message que l'ancre |
| deux arguments | 2 | non | docstring |

**Heures.** Script 21:50:29, élément 21:50:40.835, candidat 2 21:50:40.873 UTC : « vers 21:50 UTC » est juste. Candidat
1 : 21:21:10 UTC, « vers 21:21 UTC » est juste (VC1-02).

## 2. Empreintes citées aux lignes changées

Chacune recalculée sur la source du plan qui porte cette empreinte. Le chemin cité juste avant est égal à la destination
du plan (`journaux/controles-ecart.log`, partie C).

| ligne du candidat 2 | empreinte | source (sous `…/addendum2-p3/`) | chemin cité = destination |
|---|---|---|---|
| 25 | `94560a3b…` | `candidat/ecrire_candidat1_addendum2_v1.py` | `prereg/contre-lectures/brouillons-addendum2-P3-v1/ecrire_candidat1_addendum2_v1.py` |
| 28, 661 | `9900a721…` | `candidat/P3-addendum2-audit-verdict-v1-candidat1.md` | (aucun chemin cité) |
| 30 | `51c7bd1b…` | `candidat/ecrire_candidat2_addendum2_v1.py` | `prereg/contre-lectures/brouillons-addendum2-P3-v1/ecrire_candidat2_addendum2_v1.py` |
| 651, 662 | `f9136b6d…` | `module-v4/test_audit_verdict_p3_v1.py` | (aucun ; versé à `docs/procedures/P3-addendum2-v1/test_audit_verdict_p3_v1.py`) |
| 653 | `cb24c899…` | `module-v4/journaux/pytest-suite-v4-garde-r1.log` | `prereg/contre-lectures/tests-v4-addendum2-P3-v1/pytest-suite-v4-garde-r1.log` |
| 655 | `f2a4be52…` | `module-v4/journaux/r1-suite-v4.jsonl` | `prereg/contre-lectures/tests-v4-addendum2-P3-v1/r1-suite-v4.jsonl` |
| 665 | `3f0dce9b…` | `verification-candidat1/verification-candidat1-addendum2-P3-v1.md` | `prereg/contre-lectures/verification-candidat1-addendum2-P3-v1.md` |

L'élément cite `ligne-candidat2-addendum2-v1.md` par son seul nom, « versé à côté » du script : le plan le verse à
`prereg/contre-lectures/brouillons-addendum2-P3-v1/ligne-candidat2-addendum2-v1.md` (`7e106f17…`), dans le dossier du
script. Les journaux v4 sont ceux que la contre-lecture 6 a recomptés (128 passés ; 576 traces, 0 refus).

## 3. `prereg.problemes`, garde 1, section « Contre-lecture »

Motifs de la garde 1, lus par `ast` dans la copie du module (`96727076…`) :
`EMPREINTE_MODULE_CITEE` = ``Module de l'addendum 2 \(sha256\) : `([0-9a-f]{64})` `` ;
`EMPREINTE_TESTS_CITEE` = ``Tests du module \(sha256\) : `([0-9a-f]{64})` ``. Partie D de `journaux/controles-ecart.log`.

| texte (copie) | sha256 | `problemes` | garde 1 : module ; tests (`findall`) | entrées | empreintes distinctes par entrée |
|---|---|---|---|---|---|
| candidat 2 | `5d5e5aa8…` | `[]` | `[96727076…]` ; `[f9136b6d…]` | 1 à 6 | 3, 3, 6, 5, 8, 3 |
| candidat 2 + entrée 7 (chevrons remplis par `a…a` et `b…b`, verdicts « scellable ») | `a1eac9b7…` | `[]` | `[96727076…]` ; `[f9136b6d…]` | 1 à 7 | 3, 3, 6, 5, 8, 3, 4 |
| candidat 2 + entrée 7, chevrons laissés (artefact) | `47350418…` | `[]` (VE-R-03) | `[96727076…]` ; `[f9136b6d…]` | 1 à 7 | 3, 3, 6, 5, 8, 3, 2 |

Dans les trois textes : aucun texte avant l'entrée 1 ; huit sections exigées présentes ; aucun `<<…>>` ni
« À REMPLIR ». L'entrée 7 prévue reprend la forme de la consigne mot pour mot, avec mes seuls retours à la ligne
(`artefacts/entree7-fictive.md`). Ses deux empreintes réelles sont justes : `9900a721…` est le candidat 1, `5d5e5aa8…`
le candidat 2. Son nom de rapport « rejeu » est celui de ce rapport.

## 4. Plan de versement

Lu comme une donnée (`copies/plan-versement-addendum2-v2.json`), partie E du journal :

- 35 lignes. Chaque source existe et a l'empreinte écrite. Destinations uniques, toutes sous `prereg/` (33) ou
  `docs/` (2), sans `..`. Aucune n'existe dans le dépôt (existence du chemin exact seulement), ni à `98a95de…` ni à
  `49b482fa…`. Aucune empreinte versée deux fois.
- `docs/procedures/P3-addendum2-v1/test_audit_verdict_p3_v1.py` ← `f9136b6d…` : ce sont les tests v4 cités en tête, au
  chemin `CHEMIN_TESTS` du module. `docs/procedures/P3-addendum2-v1/audit_verdict_p3_v1.py` ← `96727076…` : c'est
  le module cité en tête, au chemin `CHEMIN_MODULE`. Les tests v3 (`d0c5eb07…`) vont à
  `versions-relues-addendum2-P3-v1/test_audit_verdict_p3_v1-d0c5eb07.py`.
- Le plan contient ce que demandait VC1-06 : le script et la section du candidat 1, les deux journaux, le rapport de la
  contre-lecture 6, le candidat 1. Il ajoute le script du candidat 2, son élément et le candidat 2.
- Pièces versées sans être citées dans le texte (ni par chemin, ni par empreinte) : `mesure_duree_v3.py`,
  `mesure-duree-v3.log`, le brouillon 3, `section-contre-lecture-code-v1.md`, l'élément, le candidat 2. Elles
  appuient des pièces citées ; le candidat 2 sera cité par l'entrée 7 (`journaux/pieces-non-citees.log`).

**Chemins `prereg/…` et `docs/…` cités par le candidat 2** (partie F) :

| état | chemins |
|---|---|
| pièce du plan, même empreinte que celle citée à côté (19) | les 17 chemins `prereg/contre-lectures/…` du texte (l. 24, 29, 408, 607 à 664) ; `docs/procedures/P3-addendum2-v1/audit_verdict_p3_v1.py` (l. 78, 365, 521) et `…/test_audit_verdict_p3_v1.py` (l. 79, 411) |
| existe déjà dans le dépôt (11 ; contenu non lu, empreintes inchangées depuis le brouillon 5, hors de cette lentille) | `prereg/P3-premier-test-i-a-v1.md`, `prereg/P3-addendum-lecture-complementaire-v1.md`, `docs/verdicts/verdict-P3-premier-test-i-a-v1.md`, `docs/decisions/proposition-N-025-audit-verdict-P3-v1.md`, `docs/decisions/decision-N-026-v1.md`, `docs/notes/P3-mesures-v2/puissance-p3-v1.txt`, les quatre notes de `docs/notes/brainstorm-suite-P3-v1/`, `docs/procedures/P3-addendum-v1/` |
| naîtra au versement | `docs/procedures/P3-addendum2-v1/` (l. 410 : le dossier ; ses deux fichiers sont dans le plan) |
| naîtra au scellement | `prereg/P3-addendum2-audit-verdict-v1.md` (l. 367 ; `PREREG_ADDENDUM2` du module) et `prereg/P3-addendum2-audit-verdict-v1.md.sha256` (l. 516) |
| naîtra après le passage | `docs/verdicts/verdict-P3-premier-test-i-a-v2.md` (l. 363 : verdict complété, R12) |
| naîtront après ces rapports (entrée 7) | `prereg/contre-lectures/verification-ecart-candidat2-addendum2-P3-v1-mots.md` et `…-rejeu.md` (VE-R-01) |

La l. 16 cite toujours `…/addendum2-p3/revue-v2/contre-lecture-code-addendum2-v2.md`, chemin du bloc-notes, inchangé
depuis le brouillon 5. La pièce est versée sous `contre-lecture-code-b4-addendum2-P3-v1.md` avec la même empreinte
`8c2902e4…` (VC1-06 : aucune action).

## Constats détaillés

### VE-R-01 (information) — Les deux rapports de l'entrée 7 manquent au plan

- **Où.** Plan v2 ; entrée 7 prévue.
- **Preuve.** Partie F du journal : ni `…-v1-mots.md` ni `…-v1-rejeu.md` ne sont dans le plan ; aucun n'existe dans le
  dépôt. Normal : ils naissent après le plan.
- **Correction (mots exacts).** Avant le versement, écrire un plan de nouveau nom, `plan-versement-addendum2-v3.json`
  (R12). Il reprend les 35 lignes du v2 et ajoute deux lignes. Première ligne : destination
  `prereg/contre-lectures/verification-ecart-candidat2-addendum2-P3-v1-mots.md`, source le rapport « mots exacts »,
  sha256 `<A>`. Seconde ligne : destination `prereg/contre-lectures/verification-ecart-candidat2-addendum2-P3-v1-rejeu.md`,
  source `…/addendum2-p3/verification-ecart-candidat2-rejeu/verification-ecart-candidat2-addendum2-P3-v1-rejeu.md`,
  sha256 `<B>`. `<A>` et `<B>` sont les empreintes écrites dans l'entrée 7.

### VE-R-02 (information) — Script du texte final hors du plan

- **Où.** `…/addendum2-p3/candidat/ecrire_texte_final_addendum2_v1.py` (`1f3933f8…`, 21:52:45 UTC).
- **Preuve.** `journaux/texte-final-essai.log`. Sur des copies, avec mon entrée 7 fictive : code 0, sortie `a1eac9b7…`,
  égale octet pour octet à la concaténation candidat 2 + entrée 7 de la partie D. Avec les chevrons laissés : refus
  « entrée 7 mal formée ou chevrons non remplis », rien n'est écrit. Il vérifie aussi l'empreinte du candidat 2, la fin
  de l'entrée 6 et quatre empreintes dans l'entrée 7. Il n'est cité ni par le candidat 2 ni par l'entrée 7, et le plan
  v2 ne le verse pas. Le texte final reste vérifiable sans lui : candidat 2 versé avec son empreinte, plus l'entrée 7
  lisible, comme le dit « Texte final : le candidat 2 et cette entrée ». Dans le texte final, « qui écrit tout le
  texte » (élément « Candidat 2 ») se lit donc comme « tout le candidat 2 » ; l'entrée 7 le précise.
- **Correction (mots exacts).** Dans le plan v3, ajouter la ligne : destination
  `prereg/contre-lectures/brouillons-addendum2-P3-v1/ecrire_texte_final_addendum2_v1.py`, source
  `…/addendum2-p3/candidat/ecrire_texte_final_addendum2_v1.py`, sha256
  `1f3933f84bb8cacacdb185b848d3fa01a0fa86340c5a6c3c40c51a019f20322d`. Aucun mot du texte ne change.

### VE-R-03 (information) — Les chevrons simples échappent au validateur

- **Où.** `src/controle_ia/prereg.py`, `GABARIT = <<[A-Z0-9_]+>>` ; entrée 7 prévue (`<A>`, `<B>`, `<verdict A>`,
  `<verdict B>`).
- **Preuve.** Le candidat 2 plus l'entrée 7 aux chevrons laissés (`47350418…`) donne `problemes` = `[]`. La garde 1 y
  lit les bonnes empreintes. L'entrée 7 garde deux empreintes réelles (candidats 1 et 2), ce qui suffit à la règle
  « deux empreintes ». Le script du texte final refuse ce cas (VE-R-02). Un contrôle de « < » sur tout le texte serait
  faux : la l. 366 porte `<AAAAMMJJ-HHMMSS-addendum2-p3>`, voulu, dans la commande.
- **Correction (mots exacts).** Aucune dans le texte. Écrire le texte final par `ecrire_texte_final_addendum2_v1.py`,
  jamais à la main.

### VE-R-04 (information) — Compagnons au versement

- **Où.** Plan v2 (aucune ligne `.sha256`).
- **Preuve.** `journaux/compagnons-sources-plan.log` : 11 pièces sur 35 changent de nom (les deux contre-lectures du
  code b2, la b4, les notes v3, les deux rapports de la contre-lecture 5, les cinq versions relues). 9 sources n'ont pas
  de compagnon. Les compagnons existants citent le nom de base de la source : copiés tels quels sous un nouveau nom, ils
  échoueraient à `sha256sum -c`.
- **Correction (mots exacts).** Au versement, écrire pour chaque destination un compagnon
  « `<sha256>  <nom de base de la destination>` » (R6). Le vérifier par `sha256sum -c` dans son dossier, avant le
  commit.

### VE-R-05 (information) — « Texte final : le candidat 2 et cette entrée » suppose deux « scellable »

- **Où.** Entrée 7 prévue ; constante `CANDIDAT2` du script du texte final.
- **Preuve.** Si un vérificateur de l'écart rend « scellable après corrections », le texte final ne peut plus être le
  candidat 2 plus l'entrée 7 : il faut un candidat 3, un script de nouveau nom, et une entrée 7 qui cite le candidat 3.
  Mon verdict est « scellable ».
- **Correction (mots exacts).** Aucune si l'autre verdict est « scellable ». Sinon, ne pas utiliser l'entrée 7 sous
  cette forme.

### VE-R-06 (information) — Robustesse du script du candidat 2

- **Où.** `ecrire_candidat2_addendum2_v1.py`, l. 77-83.
- **Preuve.** L'élément n'a pas de contrôle d'empreinte : tout fichier qui commence par « - Candidat 2 : » et finit par
  une fin de ligne est accepté. `SORTIE` est écrasé sans contrôle (R12 : on n'écrase jamais). Un seul message couvre
  l'élément mal formé, l'ancre absente et l'ancre en double. Sans effet sur le candidat 2 : avec l'élément versé
  (`7e106f17…`), le rejeu redonne `5d5e5aa8…`, et le contenu de l'élément est lisible dans le texte.
- **Correction (mots exacts).** Aucune avant le scellement (changer le script changerait l'empreinte citée à la
  l. 30). Pour un futur script : vérifier l'empreinte de chaque entrée, refuser une sortie qui existe déjà, un message
  par cause.

### VE-R-07 (information) — Chemins qui naîtront plus tard

- **Où.** Candidat 2, l. 363, 367, 410, 516 ; entrée 7 prévue.
- **Preuve.** Section 4, tableau des chemins cités.
- **Correction (mots exacts).** Aucune. Au versement, vérifier que `docs/procedures/P3-addendum2-v1/` reçoit ses deux
  fichiers. Au scellement, vérifier que le commit de scellement ajoute `prereg/P3-addendum2-audit-verdict-v1.md.sha256`
  et que le texte scellé a cette empreinte (garde d'antériorité, l. 515-517).

## R1 et intégrité

- Rien n'a été ouvert sous `donnees/`, `diag/`, `runs/` ou `traces/` du dépôt. Je n'ai ouvert ni
  `prereg/P3-consignes-v1.md` ni aucun fichier `textes-actions-*`. Je n'ai calculé aucune grandeur de B1 ni de B2.
  Le module n'est pas importé. Aucun réseau, aucune commande Vast.ai.
- Les originaux sont intacts : les neuf fichiers de `…/addendum2-p3/` du tableau « Pièces » ont la même empreinte au
  début et à la fin (`journaux/fin.txt`). J'ai travaillé seulement sur des copies (`copies/`, `rejeu/`, `artefacts/`).
- Dépôt : tête `98a95de…` au début, `49b482fa…` à la fin (commit de la session, registres seulement). `git status
  --porcelain` vide aux deux bouts. Aucun fichier compilé écrit (`journaux/depot-debut.txt`, `journaux/fin.txt`).

## Reproductions

Interpréteur de la consigne, `PYTHONDONTWRITEBYTECODE=1`, chemins absolus :

- rejeu : `python -I -B rejeu/ecrire_candidat2_addendum2_v1.py copies/P3-addendum2-audit-verdict-v1-candidat1.md copies/ligne-candidat2-addendum2-v1.md <sortie>` ;
- artefacts : `python -I -B outils/artefacts_script_v1.py <copie du script> <copie du candidat 1> <copie de l'élément> <dossier vide>` ;
- contrôles B à F, depuis la racine du dépôt : `PYTHONPATH=src python -B -s outils/controles_ecart_v1.py copies <dossier avec entree7-fictive.md et entree7-chevrons.md> copies/verification-candidat1-addendum2-P3-v1.md /home/user/controle-ia-travail` ;
- texte final : `python -I -B <copie de ecrire_texte_final_addendum2_v1.py> copies/P3-addendum2-audit-verdict-v1-candidat2.md artefacts/entree7-fictive.md <sortie>`.

## Fichiers rendus (chacun avec son compagnon `.sha256`)

| fichier | sha256 |
|---|---|
| `outils/controles_ecart_v1.py` | `fe613d7c32fc2980bb35fa645eb63b37073edbd11cd29d1e1f6bf0918aff16f8` |
| `outils/artefacts_script_v1.py` | `51fac9f47b46b950edb9005d48ba27019f3b87fd2279813e08c44074bb785ca5` |
| `rejeu/candidat2-rejoue.md` | `5d5e5aa83c57d37e6406ea1d57e87bc841c8e69e22a4918324a36b2b877bc247` |
| `artefacts/entree7-fictive.md` ; `artefacts/entree7-chevrons.md` | `157933f7aa4f75b17cdb380722963307efe657b9a906169ddc58e2effaebfb9a` ; `c1cfbbe5d451fc25d7f28ae39ff23089d63498b4d430c19f5ca775f742027f26` |
| `artefacts/candidat2-plus-entree7-fictive.md` ; `…-chevrons-laisses.md` (essais, pas des candidats) | `a1eac9b79d8884772bf001d82150ed1842cd703bd2cba6f92dc955d1e15b3fb8` ; `473504187536e80675749b1028ca5614106b84d6aaa2d2d5059a983195a1072c` |
| `artefacts/texte-final/final-fictif.md` (essai) | `a1eac9b79d8884772bf001d82150ed1842cd703bd2cba6f92dc955d1e15b3fb8` |
| `journaux/rejeu-script.log` ; `journaux/artefacts-script.log` | `719914a1d0afd6df64921219317bbfb4a91d602cc79cba8d79e66dbc985605d0` ; `6925798dc68bdb3c5ae2e27ba34df71be565f9e2965e9a4866e2524a8464c7af` |
| `journaux/controles-ecart.log` ; `journaux/controles-ecart-fin.log` | `900f72bfa563e6bd4941a03dd9838d7cacde451eb4f821b97bf02046b87c6b23` ; `da3ac52078dfbd71bc49e5ac4d198a6e2c625e384f7ecfd187c34bb6c6e534a2` |
| `journaux/texte-final-essai.log` ; `journaux/compagnons-et-heures.log` | `6f49e6a02e8f48b17feab2b94821ed436669a6cef37beed4a94eea35b661f437` ; `d505f6e21af0533aefc1436138be4ed44f084ccca415b92ce0d079f9450665fe` |
| `journaux/compagnons-sources-plan.log` ; `journaux/pieces-non-citees.log` | `352e013b14d2cbd16430187fa2fe672113faff003f135cc8c3416d811043d57c` ; `01e96fd418371aad6aa94e5808b29d0596be625b2d125a8d2f425384ae402426` |
| `journaux/debut.txt` ; `journaux/fin.txt` ; `journaux/copies.sha256.txt` | `bf4afcbc356b66eaf8dbb47fdaad509074f263731ee9676ef1dcf4880d340e41` ; `47e76f7e6975845dc57b0ff7199b7d9661115e078e2a685b92eb999a137073b9` ; `6447f316d58f1009a58695c37d329cae35699a966058b21289ed7d8182a34e83` |
| `journaux/depot-debut.txt` ; `journaux/depot-commits-pendant.txt` | `f5cf64e22039358ddcc7c6aa9fc3efa150784f5dab09d89d1dc86e4d567d22c0` ; `745ae416a3be139f8d8e3d094383117eef5ec49550af7f18ecdcd2dcd61fa552` |
| `copies/` (sept copies, empreintes du tableau « Pièces ») ; `artefacts/cas/` (entrées altérées, scripts visés) | voir leurs compagnons |
