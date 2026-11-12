# Vérification de l'écart candidat 1 → candidat 2 — addendum 2 de P3 — lentille « mots exacts » — v1

**Verdict : scellable.** Le candidat 2 est le candidat 1, plus les sept corrections de texte de la contre-lecture 6
(VC1-01 point 1, VC1-02, VC1-03 points 1 et 2, VC1-04 points 1 et 2, VC1-05) en mots exacts, plus l'élément
« Candidat 2 » de l'en-tête. Rien d'autre. Seuls les retours à la ligne diffèrent des mots du rapport. Aucune
correction n'est oubliée. Les neuf sections de l'analyse sont égales octet pour octet. L'élément « Candidat 2 » est
exact : heure, empreintes, et ce qu'il dit du script (son rejeu redonne le candidat 2 octet pour octet). L'entrée 6
est la recommandation de VC1-03 point 2, chevron rempli par l'empreinte du rapport. L'entrée 7 prévue est exacte. Elle
suffit si les deux verdicts sont « scellable » et si les deux rapports entrent au plan de versement (VE-M-01).

| id | gravité | constat (une ligne) |
|---|---|---|
| VE-M-01 | information | Entrée 7 prévue : exacte ; suffisante à trois conditions (deux verdicts « scellable » ; deux rapports au plan de versement, absents du plan v2 ; entrée remplie comparée par programme à la forme relue) |
| VE-M-02 | information | « qui écrit tout le texte » (élément « Candidat 2 ») se lit, dans le texte final, avec l'entrée 7 qui dit « le candidat 2 et cette entrée » : pas de contradiction ; précision possible dans l'entrée 7, sans obligation |
| VE-M-03 | information | Script du texte final (pièce hors consigne) : sortie juste sur un essai ; il refuse les chevrons non remplis mais accepte une entrée 7 au texte changé ; ni cité ni au plan v2 |
| VE-M-04 | information | Journaux et outils des contre-lectures 6 et 7 : cités par empreinte dans les rapports, chemins du bloc-notes, non versés (même pratique qu'aux contre-lectures 1 à 5) |
| VE-M-05 | information | Tête du dépôt changée pendant mon travail par un commit de la session (registres seulement) ; validateur et code gelé lus inchangés |

Aucun constat critique, majeur, mineur ni de forme.

Chemins relatifs à `…/scratchpad/addendum2-p3/verification-ecart-candidat2-mots/`, sauf mention ; `…/addendum2-p3/`
est le dossier de travail de l'addendum 2.

## Cadre

- Vérificateur : sous-agent neuf. Je n'ai écrit ni l'addendum 2 (aucun brouillon, aucun candidat, aucun script), ni
  aucune version de son module ou de ses tests, ni aucune contre-lecture, vérification ou traitement antérieurs.
  Date : 2026-10-20, de 21:55 à 22:10 UTC environ.
- Écritures : seulement sous `…/addendum2-p3/verification-ecart-candidat2-mots/`. Chaque fichier écrit a son
  compagnon `.sha256` (« empreinte, deux espaces, nom de base »).
- Dépôt de travail en lecture seule. git lu avec `--no-optional-locks`. Aucune recherche récursive : seuls des
  fichiers nommés (`src/controle_ia/prereg.py`, `gardes.py` et `scellement.py` pour leurs imports) et deux tests
  d'existence de chemins. Rien ouvert sous `donnees/`, `diag/`, `runs/`, `traces/` ; ni `prereg/P3-consignes-v1.md`,
  ni aucun fichier `textes-actions-*`. Aucun réseau, aucune commande Vast.ai.
- Module de l'addendum 2 : jamais importé ni exécuté. Les deux expressions de la garde 1 sont lues par l'arbre
  syntaxique (module `ast`), puis compilées seules.
- Interpréteur de la consigne (Python 3.11.17), `-B`, `PYTHONDONTWRITEBYTECODE=1`. Mes outils tournent en `-I` et
  n'importent rien du dépôt, sauf `outils/garde1_problemes_entree7_v1.py`, qui importe `controle_ia.prereg`
  (`PYTHONPATH=src`, depuis la racine du dépôt).
- Pièce hors consigne : `…/addendum2-p3/candidat/ecrire_texte_final_addendum2_v1.py` (21:52:45 UTC,
  `1f3933f8…`), apparue avant mon début. Je l'ai lue comme une donnée et essayée sur des copies (VE-M-03).

## Pièces (empreintes recalculées au début et à la fin ; égales à la consigne et aux compagnons)

| pièce (sous `…/addendum2-p3/`) | sha256 |
|---|---|
| candidat 1 `candidat/P3-addendum2-audit-verdict-v1-candidat1.md` | `9900a721560c87361efcf60660863727644e8fdc3ab88e4fd1f325a613306b0e` |
| rapport de la contre-lecture 6 `verification-candidat1/verification-candidat1-addendum2-P3-v1.md` | `3f0dce9ba99ab692b2d47660457a28b969ac3b0ac04b43f931f0101f05283f04` |
| candidat 2 `candidat/P3-addendum2-audit-verdict-v1-candidat2.md` | `5d5e5aa83c57d37e6406ea1d57e87bc841c8e69e22a4918324a36b2b877bc247` |
| script `candidat/ecrire_candidat2_addendum2_v1.py` | `51c7bd1b4886e43fd6a4bc80c8a11fbed3813c5307cd00b532c833d2295d5943` |
| élément d'en-tête `candidat/ligne-candidat2-addendum2-v1.md` | `7e106f17410587947775451f7ea58df978853b0e051338ba522c63d98b028568` |
| plan de versement `candidat/plan-versement-addendum2-v2.json` | `6d312445bf7fa63bbea821c2a46c7d91f40918c1e5fe2df8190ae8594cdef39f` |
| module `module-v4/audit_verdict_p3_v1.py` ; tests v4 `module-v4/test_audit_verdict_p3_v1.py` | `967270761c92ce3875695b8e5da5a985295c963b324dd120a31d09db663f132d` ; `f9136b6dc5eebce6d9e9101fa910646b16fa544f0ee1d3a997030eb9319dbc07` |
| journaux `module-v4/journaux/pytest-suite-v4-garde-r1.log` ; `r1-suite-v4.jsonl` | `cb24c899aa490bfa98e00b370c0ad388f13ddfbce6f277b21bd368a24ba12c36` ; `f2a4be52af0304831d77abeb36d78c46bb073f1a606f7eb56e3b0e3f576b3edd` |
| validateur du dépôt `src/controle_ia/prereg.py` | `3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306` |

Compagnons justes (`sha256sum -c`) : les deux candidats, les deux scripts d'écriture, l'élément d'en-tête, la section
de la session, le plan v2, le rapport de la contre-lecture 6, le module, les tests v4, les deux journaux
(`journaux/fin.txt`).

## 1. Différentiel candidat 1 → candidat 2 et mots exacts

**Différentiel brut** (`journaux/mots-exacts-ecart.log`, partie 4) : trois blocs, rien d'autre.

| bloc (candidat 1 → candidat 2) | section | origine |
|---|---|---|
| l. 20 → l. 20 | en-tête | VC1-02 |
| l. 22-24 → l. 22-33 | en-tête | VC1-04 point 1 et VC1-01 point 1 (élément « Candidat 1 ») ; élément « Candidat 2 » ajouté avant « - Date (UTC) » |
| l. 638-641 → l. 647-667 | Contre-lecture | VC1-04 point 2, VC1-03 point 1, VC1-05 (fin de l'entrée 5) ; VC1-03 point 2 (entrée 6) |

Chaque ligne nouvelle commence par « - » (nouvel élément) ou par deux espaces (suite d'élément) : la structure de
liste est gardée. Aucune ligne de suite ne commence par « Contre-lecture ».

**Mots exacts, par programme** (`outils/mots_exacts_ecart_v1.py`). L'outil lit le rapport de la contre-lecture 6
lui-même. Dans le bloc « **Correction » de chaque constat VC1-01 à VC1-07, il extrait les actions « remplacer « A »
par « B » » et « ajouter après l'entrée 5 « C » », guillemets imbriqués compris, avec leur point. Il normalise les
espaces (toute suite d'espaces, retours à la ligne compris, devient une espace). Il reconstruit le candidat 2 attendu
depuis le candidat 1, puis le compare au candidat 2. Résultats :

- actions trouvées : exactement les sept attendues (VC1-01 point 1, VC1-02, VC1-03 points 1 et 2, VC1-04 points 1
  et 2, VC1-05) ; aucune en trop ; aucune dans VC1-06 et VC1-07 (information, sans correction de texte) ;
- chaque ancien texte se trouve une seule fois dans le candidat 1 ; les six anciens textes sont disjoints ;
- l'entrée 5 est le dernier élément du candidat 1 : « ajouter après l'entrée 5 » revient à ajouter à la fin ;
- **candidat 2 normalisé = candidat 1 + corrections du rapport + entrée 6 + élément « Candidat 2 » : vrai** ;
- l'élément « Candidat 2 » se trouve octet pour octet, une fois, juste avant « - Date (UTC) » ;
- les quatre paires du script (lues par `ast.literal_eval`, jamais exécutées) donnent chacune les mots du rapport :
  paire 1 = VC1-02 ; paire 2 = VC1-04 point 1 ; paire 3 = VC1-01 point 1 ; paire 4 = VC1-04 point 2, VC1-03 point 1,
  VC1-05 et l'entrée 6 (VC1-03 point 2), qui se suivent dans le texte.

**Épreuve de l'outil** (R5 ; `outils/artefacts_outil_v1.py`, `journaux/epreuve-outil-artefacts.log`). Cas sain :
vrai. Artefacts construits depuis le candidat 2 : un mot ôté dans l'entrée 6 → faux ; un chiffre changé dans
« Seuil » → faux, et la section « Seuil » est signalée changée ; VC1-05 défait → faux ; chevron de l'entrée 6 rempli
par une autre empreinte → faux. Un retour à la ligne déplacé seul → vrai, comme voulu (espaces normalisés), et la
section « Contre-lecture » est signalée changée octet pour octet.

**Points sans correction de texte.** VC1-01 point 2 : script 1 et section au plan v2, mêmes empreintes. VC1-01
point 3 : script de nouveau nom ; sa docstring dit ce qu'il fait, sans « candidat_essai_v1.py » ni « fictives ici » ;
il écrit tout le texte, élément d'en-tête compris, lu d'un fichier à côté ; son rejeu redonne le candidat 2 (section
2) ; il est cité par son chemin versé et son empreinte, et versé de même au plan v2.

## 2. Élément « Candidat 2 » de l'en-tête

| dit | fait | état |
|---|---|---|
| « écrit par la session 14 (2026-10-20 vers 21:50 UTC) » | candidat 2 écrit à 21:50:40 UTC (son compagnon aussi ; script à 21:50:29 ; élément à 21:50:40) | = |
| « à partir du candidat 1 (sha256 `9900a721…`) » | le script refuse toute autre empreinte : essai d'un candidat 1 changé d'un octet → « candidat 1 : empreinte inattendue », code 1, rien écrit | = |
| « par le script `prereg/contre-lectures/brouillons-addendum2-P3-v1/ecrire_candidat2_addendum2_v1.py` (sha256 `51c7bd1b…`) » | empreinte égale au fichier ; ce chemin et cette empreinte au plan v2 | = |
| « qui écrit tout le texte, cet élément compris (lu dans `ligne-candidat2-addendum2-v1.md`, versé à côté) » | rejeu sur copies (`journaux/rejeu-script-candidat2.log`) : sortie `5d5e5aa8…` = candidat 2 octet pour octet ; l'élément est lu du fichier et inséré tel quel ; ce fichier est au plan v2 dans le même dossier que le script | = (voir VE-M-02 pour le texte final) |
| « corrections VC1-01 à VC1-05 de la contre-lecture 6, en mots exacts » | section 1 | = |
| « aucune règle, garde, réserve ni nombre de l'analyse ne change » | section 5 | = |
| « module et tests v4 inchangés » | `96727076…` et `f9136b6d…`, égaux à l'en-tête et au rapport de la contre-lecture 6 | = |
| « la session n'a calculé aucune grandeur de B1 ni de B2 » | dire de la session ; rien dans l'écart ne touche B1 ni B2 | non vérifiable ici |

L'empreinte de l'élément lui-même (`7e106f17…`) ne peut pas figurer dans l'élément ; son texte est entier dans le
candidat, et son compagnon et le plan v2 la donnent. La docstring dit « vérifié avant toute lecture » : le script lit
les octets, puis vérifie l'empreinte avant de les décoder ; rien n'est utilisé avant. Rien dans l'élément ne promet
plus que ce qui est fait.

Les autres changements de l'en-tête sont dans l'élément « Candidat 1 » : heure 21:21 (le candidat 1 est écrit à
21:21:10 UTC), comptes de VC1-04, script 1 cité par `94560a3b…`, égal au fichier et au plan v2.

## 3. Entrée 6

- Égale, espaces normalisés, au texte recommandé par VC1-03 point 2, avec `<empreinte de ce rapport>` remplacé par
  `3f0dce9ba99ab692b2d47660457a28b969ac3b0ac04b43f931f0101f05283f04` : vrai. C'est l'empreinte du fichier et de son
  compagnon.
- Une seule entrée 6, après l'entrée 5, dernière du fichier. Le validateur la lit (entrées 1 à 6 ; 3 empreintes
  distinctes dans l'entrée 6).
- Empreintes de l'entrée 6 : candidat 1 `9900a721…`, tests v4 `f9136b6d…`, rapport `3f0dce9b…`, toutes égales à
  leurs fichiers. Chemin du rapport au plan v2, même empreinte.
- Nombres de VC1-03 point 1 relus sur les journaux cités : « 128 passed », code 0 ; 576 traces, champ `refus` faux
  pour les 576.

## 4. Entrée 7 prévue (forme à chevrons de la consigne)

Texte copié dans `outils/entree7-prevue-consigne.md`. Vérifications (`journaux/garde1-problemes-entree7.log`,
`journaux/empreintes-ecart.log`, `journaux/texte-final-essai.log`) :

- empreintes écrites : candidat 1 `9900a721…` et candidat 2 `5d5e5aa8…`, égales aux fichiers ;
- chevrons : `<A>`, `<verdict A>`, `<B>`, `<verdict B>`, rien d'autre ;
- chemins `prereg/contre-lectures/verification-ecart-candidat2-addendum2-P3-v1-mots.md` et `…-rejeu.md` : absents du
  dépôt ; le nom de base du premier est celui de ce rapport ; aucun des deux n'est au plan v2 (VE-M-01) ;
- les mots sur les vérificateurs (« n'ont écrit ni le texte, ni ses scripts, ni aucune version du module ou de ses
  tests, ni aucune contre-lecture antérieure ») sont vrais pour moi ;
- texte final d'essai (pas un candidat : chevrons remplis par des valeurs d'essai, verdicts « scellable ») :
  `prereg.problemes` = `[]` ; entrées 1 à 7 lues, 3, 3, 6, 5, 8, 3 et 4 empreintes distinctes ; garde 1 : une seule
  empreinte de module (`96727076…`), une seule de tests (`f9136b6d…`) ;
- R6 : l'entrée cite chaque rapport par chemin et empreinte, et chaque candidat par empreinte ; elle n'a pas d'autre
  nombre. R2 : elle nomme les deux vérificateurs neufs, leurs lentilles, leurs rapports et leurs verdicts.

## 5. Analyse inchangée ; validateur ; garde 1

- Sections du candidat 1 et du candidat 2 (titres « ## ») : mêmes titres, même ordre. « Hypothèse », « Prédiction
  chiffrée et signe attendu », « Métrique », « Seuil », « Plan d'analyse », « Critères de lecture gelés »,
  « Précisions d'application (brouillons 4 et 5) », « Liste d'arrêt », « Limites écrites » : égales octet pour octet.
- En-tête hors éléments « Candidat 1 » et « Candidat 2 » : égal octet pour octet (auteur, brouillons 2 à 5, date,
  commit cité, entropie, empreintes du module et des tests, nombre de tests attendu `128`, décision, documents qui font
  foi, entrées, code gelé, emplacement, statut, périmètre).
- Section « Contre-lecture » : entrées 1 à 4 égales octet pour octet ; entrée 5 changée aux seuls endroits de la
  section 1 ; entrée 6 ajoutée.
- `prereg.problemes` : `[]` sur le candidat 1 et sur le candidat 2.
- Garde 1 (expressions lues par l'arbre syntaxique : « Module de l'addendum 2 \(sha256\) : `([0-9a-f]{64})` » et
  « Tests du module \(sha256\) : `([0-9a-f]{64})` ») : sur le candidat 2, une seule empreinte chacune, `96727076…`
  et `f9136b6d…`, les mêmes que sur le candidat 1.

## Constats détaillés

### VE-M-01 (information) — Entrée 7 : exacte ; suffisante à trois conditions

- **Fait.** L'entrée 7 prévue est exacte (section 4). Elle dit « Texte final : le candidat 2 et cette entrée ».
- **Conditions.**
  1. Les deux verdicts sont « scellable ». Un verdict « scellable après corrections » qui touche le texte du candidat
     2 rendrait cette phrase fausse : il faudrait un candidat 3, un script et un élément d'en-tête neufs, et une
     nouvelle vérification de l'écart.
  2. Les deux rapports et leurs compagnons entrent au plan de versement, aux chemins cités : le plan v2 (35 lignes)
     n'en a aucun (`grep` : 0 ligne).
  3. Les chevrons sont remplis par l'empreinte du compagnon de chaque rapport et par le verdict écrit en tête de
     chaque rapport. L'entrée remplie est comparée par programme à la forme relue : seuls les quatre chevrons
     changent, espaces normalisés.
- **Correction.** Aucune dans le texte.

### VE-M-02 (information) — « tout le texte » dans le texte final

- **Fait.** L'élément « Candidat 2 » dit : « par le script … qui écrit tout le texte, cet élément compris ». Dans le
  candidat 2, c'est exact. Dans le texte final, le script n'écrit pas l'entrée 7. L'entrée 7 le dit (« Texte final :
  le candidat 2 et cette entrée »). Un lecteur qui rejoue le script obtient `5d5e5aa8…`, puis retrouve le texte final
  en ajoutant l'entrée 7. Pas de contradiction.
- **Précision possible, sans obligation.** L'entrée 7 n'est pas encore écrite : la préciser ne coûte rien au candidat
  2. Mots exacts : remplacer « Texte final : le candidat 2 et cette entrée. » par « Texte final : le candidat 2,
  octet pour octet, suivi de cette entrée, ajoutée ensuite. ». Si la session la retient, la forme relue change : le
  dire au vérificateur « rejeu et versement » (ou à un vérificateur neuf) avant d'écrire le texte final. Sinon, garder
  la forme relue.

### VE-M-03 (information) — Script du texte final

- **Pièce.** `…/addendum2-p3/candidat/ecrire_texte_final_addendum2_v1.py` (`1f3933f84bb8cacacdb185b848d3fa01a0fa86340c5a6c3c40c51a019f20322d`),
  hors consigne, lue comme une donnée.
- **Essai sur copies** (`journaux/texte-final-essai.log`). Avec une entrée 7 d'essai bien formée : sortie
  `6d3103c3…` = candidat 2 suivi de l'entrée, égale à celle de mon outil. Chevrons non remplis : refus, code 1, rien
  écrit. Entrée 7 bien formée mais au texte changé (« deux sous-agents » sans « neufs ») : acceptée, code 0. Le
  script contrôle la forme, pas l'égalité avec la forme relue.
- **Citation.** Le script n'est ni cité dans l'entrée 7 ni au plan v2. Ce n'est pas nécessaire : « le candidat 2 et
  cette entrée » suffit à refaire le texte final.
- **Recommandation.** Faire la comparaison de VE-M-01, condition 3, dans ce script ou juste avant. Facultatif : verser
  ce script et l'entrée remplie près des brouillons, comme pour les candidats.

### VE-M-04 (information) — Journaux et outils des contre-lectures 6 et 7

- Le texte cite les rapports par chemin versé et empreinte. Chaque rapport cite ses journaux et ses outils par
  empreinte, sous des chemins du bloc-notes. Le plan v2 ne les verse pas (les contre-lectures 1 à 5 non plus).
- Aucune action nécessaire avant le scellement. Facultatif : verser les dossiers `outils/` et `journaux/` de ces deux
  vérifications sous `prereg/contre-lectures/`, à côté de leurs rapports.

### VE-M-05 (information) — Tête du dépôt changée pendant mon travail

- Début : `98a95de77af50be9947e4c812a01aa2b5d21cb61`. Fin : `49b482fa0d7ef001fda46a9178f25551ffd941a0`, commit du
  2026-10-20 à 21:57:07 UTC, « R-296 et GO-2026-10-20-10 : lecture « double comptabilité » ajoutée à P3b (décision
  de Lazar) ». Il change seulement `registres/decisions.md` et `registres/go.md` (`journaux/tete-depot.log`).
- `src/controle_ia/prereg.py`, `gardes.py` et `scellement.py` : inchangés entre les deux têtes. `git status
  --porcelain` : vide au début et à la fin. Je n'ai rien écrit dans le dépôt.

## R1 et intégrité

- Aucune donnée du run, aucune sortie de lecture, aucun texte d'action, ni les consignes privées. Aucune grandeur de
  B1 ni de B2. Le module n'a été ni importé ni exécuté.
- Aucun fichier compilé écrit : aucun `__pycache__` sous mon dossier, `candidat/` ni `module-v4/` ; aucun fichier de
  `src/controle_ia/__pycache__` plus récent que mon début.
- Originaux intacts : mêmes empreintes au début et à la fin (`journaux/fin.txt`). Rejeu et essais faits sur des
  copies (`copies/`, `rejeu/`, `essai/`).
- Un essai de mon outil a duré trop longtemps (comparaison caractère par caractère sur un artefact) : arrêté par ses
  deux PID (28436 et 2299), puis l'outil a été corrigé (premier écart localisé directement). Sur le candidat 2, son
  journal est identique avant et après la correction.

## Reproductions

Interpréteur de la consigne, `PYTHONDONTWRITEBYTECODE=1`, chemins absolus :

- mots exacts : `python -I -B outils/mots_exacts_ecart_v1.py <rapport VC1> <candidat 1> <candidat 2> <élément> <script 2>` ;
- épreuve de l'outil : `python -I -B outils/artefacts_outil_v1.py outils/mots_exacts_ecart_v1.py <mêmes cinq> essai` ;
- rejeu : `python -I -B copies/ecrire_candidat2_addendum2_v1.py copies/P3-addendum2-audit-verdict-v1-candidat1.md copies/ligne-candidat2-addendum2-v1.md rejeu/candidat2-rejoue.md` ;
- garde 1, validateur, entrée 7 (depuis la racine du dépôt, `PYTHONPATH=src`) : `python -B outils/garde1_problemes_entree7_v1.py <module> <candidat 1> <candidat 2> outils/entree7-prevue-consigne.md essai` ;
- empreintes et plan : `python -I -B outils/empreintes_ecart_v1.py <candidat 1> <candidat 2> <plan v2> outils/entree7-prevue-consigne.md <fichiers…>`.

## Fichiers rendus (chacun avec son compagnon `.sha256`)

| fichier | sha256 |
|---|---|
| `outils/mots_exacts_ecart_v1.py` | `8a268a6729d7f0a2078d67ebf8c72ee561d37b5bce84f5f100e4ff2c52e179b6` |
| `outils/artefacts_outil_v1.py` | `0b4a54e06fb6cba3622333f8a61b6979af4a546fb1684e5212c4862008078fc7` |
| `outils/garde1_problemes_entree7_v1.py` | `6afcbd3045fab99de818727fd6db5411dcae3f7bae3ae57d209e03c11b9c763b` |
| `outils/empreintes_ecart_v1.py` | `60d1633a034c436b377ed2c2e7d769eed5f3827549136027b367d35b46ef7e1c` |
| `outils/entree7-prevue-consigne.md` (= `essai/entree7-chevrons.md`) | `b362b2cdca94cf1c500b97248a5ce9e949bd83ffb1cf02d852415ffabd9ecf42` |
| `journaux/mots-exacts-ecart.log` | `799652b0506faa5453c0685b1764c4ae1ca623c0793bd4dcb5e591f4619d6bfa` |
| `journaux/epreuve-outil-artefacts.log` | `a3fc48f5680c782b0f24596c707ed7044f682f4e3ceb0e604c1e4e6cc640a107` |
| `journaux/rejeu-script-candidat2.log` | `8533f9cec2047a6c404ccc5e551f010740132c3e65b4ff08a66e0c8de81c831f` |
| `journaux/garde1-problemes-entree7.log` | `adb5e906ac04ff9e119a4accebb047cda1850f58764aed5956650243267ff29e` |
| `journaux/empreintes-ecart.log` | `d19ae40a8e9ea44dad720e86a0cebe2b8b7f44b47e9f17421bceac260e048f09` |
| `journaux/texte-final-essai.log` | `5598008a35256262d55c7be34ffdfa95f9a86b292822708fffe71a1e6b1d72f3` |
| `journaux/tete-depot.log` ; `journaux/fin.txt` | `148fbbac6aa6a1b072d6a6e1ad943c4e91ff6fa469232a88c690aa386e627c01` ; `f1d761d43ff81ea78b346681e079473e3fe04f9345d6a47d246f290acb588db2` |
| `journaux/git-head-debut.txt` ; `journaux/git-head-fin.txt` ; `journaux/git-status-debut.txt` et `-fin.txt` (vides) | `e3194cbc…9a83` ; `094298cc…5691` ; `e3b0c442…b855` |
| `rejeu/candidat2-rejoue.md` (= candidat 2) ; `rejeu/candidat1-altere.md` (essai de refus) | `5d5e5aa83c57d37e6406ea1d57e87bc841c8e69e22a4918324a36b2b877bc247` ; `e569d507…d71f` |
| `essai/entree7-essai.md` ; `essai/texte-final-essai.md` = `essai/texte-final-par-script-essai.md` (essais, pas des candidats) | `67c06cf1…b318` ; `6d3103c3be7a42571a86db48e7fd97ae871ad5556e9d2c5ddbf9eb02332acb6d` |
| `essai/entree7-alteree.md` ; `essai/texte-final-altere-essai.md` (essai d'acceptation, VE-M-03) | `24ef7b1c…cf09` ; `96173d47…513a` |
| `copies/` : candidat 1, candidat 2, élément, script 2, script du texte final | `9900a721…6b0e`, `5d5e5aa8…c247`, `7e106f17…8568`, `51c7bd1b…5943`, `1f3933f8…322d` |
