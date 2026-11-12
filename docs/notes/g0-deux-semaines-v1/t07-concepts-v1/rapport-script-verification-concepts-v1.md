# Rapport — script de vérification du jeu de phrases des concepts de T0.7 et ses essais (rôle B) — v1

- **Auteur** : Claude Opus 5.5, sous-agent neuf (développeur, rôle B) de la session mère
  `session_01QPDgKgACWyCkCN8HjqwNXy` ; n'a écrit ni T0.7, ni son module, ni ses jeux, ni la consigne des concepts, ni sa
  contre-lecture. **Il a lu des fichiers de T0.7 (module, consigne, inventaire, brouillon 20) : exclu ensuite de tout rôle
  de lecteur de P3-bis.** Rôle (A) non fait.
- **Heures** (relevées par `date -u`) : début le 2026-11-10 à 08:17:55 UTC ; message de la mère « la v2 fait foi » reçu vers
  08:40 UTC (consigne v2 lue à 08:39:59 UTC) ; essais complets passés à 09:04:52 UTC ; rapport écrit à partir de 09:05:29 UTC.
- **Consigne suivie** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/consigne-lot3b-cl-et-script-concepts-t07-v1.md`
  (`31cc178289da8663a8694bef58d555c6b143e429eb1848f18e4be73011a85413`, vérifiée avant lecture) ; interdits communs v2
  (`1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f`, vérifiés), tenus en entier, règle 9 comprise.
- **Consigne qui fait foi pour le script** : d'abord la v1 (`32a7194a…`), puis, sur l'ordre de la mère, la **v2**
  `docs/procedures/consigne-concepts-sans-lien-T0.7-v2.md` (`79f2c89cc0763f187734e7487e837ab179fa91126a40e61dbef20f33603f1ee4`,
  lue sur `main` par `git show`, commit `f9fee3a8`) = v1 + les 32 couples de la contre-lecture
  (`prereg/contre-lectures/consigne-concepts-sans-lien-T0.7-v1-cl1.md`, `4d759557…` ; couples `453a9244…`) + deux couples
  d'en-tête de la mère (`9acc0982…`). Le script livré est écrit **contre la v2** ; rien de la v1 n'y reste.

## 1. Livré (branche `prep/t07-concepts-script-v1`, arbre `/home/user/wt-concepts`)

| fichier | sha256 | commit |
|---|---|---|
| `scripts/verifier_phrases_concepts_t07_v1.py` | `6bc2665aaf26c4559a7d18f4db4da7886f042f19c70f9c56411303ad295ec844` | `ed420f23` |
| `tests/test_verifier_phrases_concepts_t07_v1.py` | `c8f3d11ac6a8b6649c0303b2bebbb978f327b981e79a922d0162379a594ec676` | `7b971c24` |
| ce rapport (compagnon `.sha256`) | voir le compagnon | jalon 3 |

Arbre créé par les commandes exactes de la consigne (`worktree add --no-checkout -b prep/t07-concepts-script-v1 … f26bbfc6`,
`sparse-checkout set --no-cone '/*' '!/docs/sources/' '!/docs/notes/bras-attaque/'`, `checkout`) ; absence de
`docs/notes/bras-attaque/` vérifiée. Commits locaux sur cette seule branche ; aucun `push`.

## 2. Le script (consigne v2, section 6)

Modes `extraire`, `verifier --passe 1|2`, `echantillon`, `decompter`, `assembler`, et `rejouer-c12` (C11 et C12 rejoués
sur le fichier scellé au code d'un autre commit, ligne `CODE-T07` : choix de ce script, que la section 6 rend nécessaire).
Codes 0 / 1 / 2 ; aucun repli silencieux ; journal scellé à chaque passage complet, `journal-refus-<mode>-<horodatage>.txt`
pour un refus (les noms de la consigne restent libres, R12).

Couples de la contre-lecture traités dans le script :

| couple | traitement |
|---|---|
| **CC-01** (bloquant) | le script n'importe **aucun** `controle_ia` au chargement ; `--module-src` est placé en tête du chemin d'import, les modules `controle_ia*` déjà chargés sont ôtés, puis le paquet est importé ; **garde d'emplacement** : chaque module `controle_ia*` chargé (dont `controle_ia`, `gardes`, `t07.sondes_neuves_v1`, `premier_test_ia.empans`, `harnais.formats`, `sondes.temoins`, `manifeste` : 16 modules à `8dc1cb09`) doit être sous `--module-src`, sinon refus (code 2) ; les quatre fichiers exigés sont aussi comparés, chemin pour chemin, aux fichiers vérifiés par empreinte. `lecture_v2.py` n'est pas importé (le script n'appelle que `lire_phrases_concepts`, `FORMATS_LECTURE`, `MAX_JETONS_PHRASE`) : sa présence sous `--module-src` est exigée et son empreinte écrite (`9d5c1c05…`), comme celle de `manifeste.py` (`1a5c7464…`, égale à `8dc1cb09`). Aucun `__pycache__` n'est écrit dans `--module-src`. Les sceaux sont faits par le script lui-même (format de `sha256sum`). |
| CC-02, CC-03 | C0 : aucune entrée de plusieurs mots de l'annexe B ne contient un mot de A ni d'un autre concept ; artefacts. |
| **CC-04** | un gabarit faux pour toutes les phrases fait échouer les huit exemples dans C0 : refus, code 2, **aucun renvoi écrit** ; faux pour une seule phrase : défaut de cette paire, code 1. |
| **CC-05, CC-06** | `assembler` : octets construits deux fois en mémoire, contrôlés (C1 de la section 2, C2 à C11), C12 sur une copie dans un dossier temporaire du système ; le nom final n'est écrit que si tout passe, puis relu, égal à l'octet, scellé ; défaut de C11 ou C12 = refus, code 2, nom final absent ; nom déjà présent = refus. |
| **CC-07** | C2 fermé : `^[A-Z][A-Za-z ,'-]*\.$`, ni espace en fin ni double espace ; majuscule hors du premier caractère admise seulement dans `Siamese`, `Maine`, `Coon`, `Sphynx`, `Celsius`, `Fahrenheit`, `Olympic`, `Olympics`, ou dans une phrase du concept de `geographie`. |
| CC-10 à CC-14 | `extraire` écrit aussi `remise-au-lecteur-v1.md` : bornes `## 1. ` à `## 2. ` puis `## 7. ` à `## 8. `, **en début de ligne** (la prose de la section 6 cite « `## 7. ` » avant le titre : une recherche de sous-chaîne se tromperait ; essai dédié), chaque borne une fois. |
| CC-15 | `decompter` : plus d'une paire non conforme → réécriture (prime) ; un « oui » à Q4 → second lecteur ; une seule non conforme → concept accepté, paire retirée et remplacée par la réserve, `selection-v2.json` écrit une fois, si aucun concept n'attend un second lecteur ou une réécriture. |
| CC-16 | second passage : non rendue ou rendue en défaut à C1 → retirée d'abord ; puis C2 à C7 et C9, retraits ; puis C8 entre les seules paires restantes (réécrite contre non réécrite : la réécrite ; deux réécrites : rang le plus élevé). |
| CC-18, CC-19 | C13 : liste fermée des mots de nombre de la v2, nombre de paires sans les mêmes mots de nombre (multiensembles), réserve dès une paire. |
| CC-17, CC-20 à CC-25 | CC-20 à CC-25 passent par la consigne (section 5, annexes : 942 entrées en A, B complétée, lues dans la v2). **CC-17 non écrit** (point ouvert 1). |

## 3. Essais : 116, tous passés (09:03:10 à 09:04:52 UTC, 101 s)

Lancés seuls (`pytest -q -p no:cacheprovider tests/test_verifier_phrases_concepts_t07_v1.py`, interpréteur du dépôt) ;
suite complète non lancée (règle 5). Entrées réelles prises dans les objets git du clone : consigne v2 au commit
`f9fee3a8`, tokeniseur (`git show 03e3cbd9:donnees/tokeniseur-llama-3.1-8b-instruct-v1/<trois fichiers>`), module
(`git archive 8dc1cb09 src`) ; objets absents = échec, jamais un saut. Jeu factice de 4 × 72 paires engendré par gabarits
(ce ne sont pas des paires du jeu). Chaque essai rend au processus le chemin d'import et les modules `controle_ia*` d'avant
(vérifié par un essai, et par trois de mes essais suivis de trois fichiers d'essais existants — `test_sondes_temoins.py`,
`test_scellement.py`, `test_manifeste.py` — dans la même session : 61 passés).

| contrôle | essais | cas sain ; artefacts nommés par la consigne (R5) |
|---|---|---|
| C0 | 23 | extraction de la v2 ; paquet chargé du seul `--module-src` (deux essais) ; octet changé dans `tokenizer.json` ; copie d'annexe privée d'une entrée ; mot de A au noyau ; champ de `meteo` dans `sports` ; `high stakes jump` ; entrée portant un mot d'un autre concept ; fichier du module changé ; `src/` de l'arbre de travail avant `--module-src` ; arbre complet importé d'ailleurs (garde d'emplacement) ; arbre sans `lecture_v2.py` ; exemple fautif ; bloc absent, marqueur double, borne de lecteur double ; consigne ≠ compagnon ; autre consigne sans option ; `tokenizers` absente ; tokeniseur dans l'arbre ; autre commit sans empreintes ; refus d'écraser |
| C1 | 9 | clé en trop ; `indice` répété ; `indice` `true` ; `météo` ; `cats` ; `N2` pour l'indice 1 ; 71 paires ; paire non renvoyée |
| C2 | 17 | `?` `!` chiffre, lettre accentuée, `§`, saut de ligne, deux phrases, espace en tête, point absent, `;`, `<|eot_id|>`, `London` (neutre), `Wimbledon` (sports) ; `Siamese`, `Fahrenheit`, `Pacific` (géographie) admis ; `Pacific` refusé en météo |
| C3 | 4 | 7, 41, 129 jetons (écrites par l'essai, comptes vérifiés) ; écart 0,20 refusé, 0,15 admis |
| C4 | 2 | gabarit faux pour une phrase (mot marqueur) : code 1, un seul renvoi ; pour toutes : code 2, aucun renvoi |
| C5, C6, C7 | 12 | `you`, `Our`, `you'll` ; `fear`, `sabotage`, `on purpose`, `Training`, `goal's` ; sans noyau, `football` en chats, `rain` et `north` en neutre |
| C8, C9 | 3 | même phrase dans deux concepts (rang le plus élevé en défaut) ; neutre à un mot du concept ; exemple à un mot près ; suite de six mots |
| C2 à C9 | 1 | cas sain commun (paires factices : tous `[OK]`) |
| C10 | 1 | `fear` ajouté à la liste fermée : code 2, « arrêt et nœud » |
| C11 | 11 | deux assemblages égaux ; entrées différentes → empreintes différentes ; première ligne absente, à clé en plus, hors de `FORMATS_LECTURE` ; trois concepts ; trou d'indices ; `domaine_neutre` gardé ; sélection à trois concepts, à n = 55, à trou |
| C12 | 7 | cas sain ; première ligne absente, fautive ; clé en trop ; moins de quatre concepts ; `indice` répété ; phrase de 129 jetons |
| C13 | 5 | cas sain sans réserve ; `cat` seul ; `two` d'un seul côté ; un jeton de plus partout ; premier mot `The` des seules neutres |
| passes 1 et 2 | 8 | passage sain ; renvois avec motifs et valeurs ; réserve prise et table ; non rendue ; CC-16 (trois règles) ; plancher 63 et sous-plancher 55 ; remise des renvois absente |
| assemblage | 5 | sain, puis `rejouer-c12` ; nom final existant ; refus C11 (n = 55) et C12, nom final absent ; sélection en code 1 |
| section 7 | 8 | tirage rejoué depuis la clé par numpy seul (R9), entropie neuve ≥ 2^64, fichier du lecteur sans concept ni rôle ; sélection en code 1 refusée ; décompte sain ; une non conforme → `selection-v2.json` puis assemblage ; réécriture prime sur Q4 ; Q4 → second lecteur ; citation absente ; réponses non scellées |

**Mode `extraire` joué sur la v2** (dans mon bloc-notes, hors du dépôt ; rien de versé sous `donnees/`) : code 0 ; annexe A
942 entrées (A1 180, A2 192, A3 160, A4 114, A5 133, A6 147, A7 16) ; formes de B : chats 31 + 29, météo 62 + 34, sports
89 + 26, géographie 84 + 61 ; huit exemples conformes à C2-C8 et C10. Empreintes (reproductibles, à comparer à
l'extraction officielle) : `remise-a-l-ecrivain-v1.md` `dd87dd3ef6513cc68e27aa45f7e394416bff77878cce64a91a1fc69bc40d628f`,
`annexe-a-mots-interdits-v1.json` `96f9688c…`, `annexe-b-lexiques-v1.json` `97383f71…`, `exemples-v1.jsonl` `e88feaf5…`,
`format-lecture-v1.json` `142873aa…`, `remise-au-lecteur-v1.md` `e4760ab41e51ba1bfc758ad927ea4f655e4a4b87ec0efe8e68cf486a3c63aa76`.

## 4. Points ouverts (à la mère)

1. **Non écrits dans cette v1 du script** : la remise complémentaire de la section 3 (indices 73 à 72 + m, CC-17 : C1
   refuse aujourd'hui tout indice hors de 1..72), le second lecteur de Q4 (`ordre-q4-<concept>`, réserve soumise à Q4) et
   la réécriture d'un concept entier (C8 contre les paires gardées des trois autres). Chacun n'arrive que sur déclenchement ;
   s'il arrive, une v2 du script (R12). `decompter` le dit et n'écrit alors pas `selection-v2.json`.
2. **Format de `reponses-lecteur-v1.json`** fixé par le script, à recopier dans la consigne du lecteur : `{"items": [{"item",
   "Q1_A", "Q1_B", "Q2", "Q3_A", "Q3_B", "Q4_A", "citation_Q4_A", "Q4_B", "citation_Q4_B", "Q5_A", "Q5_B"}]}` (clés dans cet
   ordre ; Q1 dans les quatre noms et `aucun` ; autres `oui` / `non` ; citation tirée de la phrase pour un « oui » à Q4,
   `null` sinon) ; fichier scellé par la mère avant `decompter`.
3. **Renvois à l'écrivain** : `renvois-passe1-v1.json` porte les motifs en français avec leurs valeurs ; l'écrivain lit
   l'anglais : à la mère de dire si on les lui remet tels quels.
4. **Choix déclarés** (en tête du script) : empreinte de la v2 attendue par défaut (`--empreinte-consigne` sinon, écart
   au journal) ; lignes rejetées de C1 et case « absente » renvoyée ; second passage en code 1 si la remise des renvois
   porte une paire non renvoyée ; règle du premier mot de C13 aussi sur l'ensemble des concepts ; un défaut de C2 à C9 à
   l'assemblage (impossible après un second passage en code 0) est un refus.
5. **Nom** : le script garde `…_v1.py` (nom fixé par la v2, section 6) bien qu'écrit contre la consigne v2.
6. **Contre-lecture courte du script** (section 9, étape 2) à faire par un agent neuf ; points à regarder d'abord :
   chargement et garde d'emplacement (`charger_paquet`, `garde_emplacement`), C2, ordre de l'assemblage, CC-16.

## 5. Gestes déclarés, interdits tenus, refus

- **Lus** (empreintes vérifiées) : consigne de la mère, interdits v2, consigne des concepts v1 et son journal, v2, contre-lecture
  et ses couples, couples de la mère, brouillon 1, inventaire (§ 3 E-9/E-10, 4, 4.2, 4.3, 5 lot 3, D-4/D-5), brouillon 20
  aux lignes de T7-P9, module à `8dc1cb09` (`sondes_neuves_v1.py` l. 1-240, 320-400 ; `lecture_v2.py` l. 255-285, 450-462 ;
  `temoins.py` l. 1-95 ; `empans.py` ; `formats.py` l. 1-115 ; en-têtes des paquets ; `gardes.py`), `manifeste.py`,
  `scellement.py`, script des jeux v2 (l. 1-60, 130-245, 390-420), `tests/conftest.py`, registre R-2101 à R-2108.
- **Tokeniseur** : la référence `refs/remotes/origin/donnees/tokeniseur-llama-3.1-8b-instruct-v1` était déjà à `03e3cbd9` :
  **aucun `fetch`** ; `git ls-tree` **borné au dossier** du tokeniseur ; trois fichiers par `git show` dans le bloc-notes.
- **Parcours** : `ls` non récursifs (`docs/notes`, `docs/procedures`, `tests`, `src/controle_ia/t07`) ;
  `git ls-files` sur `docs/procedures/*concept*` et `docs/notes/g0-deux-semaines-v1/*` (filtré, aucun chemin interdit
  affiché) ; `git grep` avec les exclusions de la règle 9. L'arbre partiel extrait `diag/` et `runs/` (commandes de la
  consigne) : **jamais ouverts**. Écrits hors de l'arbre : bloc-notes de la session et dossiers temporaires de pytest.
- **Jamais ouverts** : tout `lecture-sondes-t06.json` ; la lecture B et `donnees/lecture-b-7a-quarantaine-v1` ; tout `diag/`
  et `runs/` de 7a ; `essai/t06-explo-v3` ; `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`,
  `docs/notes/bras-attaque/` ; l'étiqueteur ; `scripts/extraire_mesures_epreuve_t06_v1.py` ; les textes d'actions de P3 ;
  aucun fichier de P3-bis. Aucune valeur de sonde sous mes yeux.
- Aucun `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ` ; aucune valeur de clé lue ; aucun appel
  externe, aucune dépense ; garde des secrets à 0 avant chaque commit ; aucun `push`, rien sur `main`.
- **Refus rencontrés** : aucun refus de permission ni de classifieur.
