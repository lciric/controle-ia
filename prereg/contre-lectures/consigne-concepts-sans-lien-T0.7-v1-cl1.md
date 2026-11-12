# Contre-lecture R2 n° 1 — consigne v1 du jeu de phrases des concepts de T0.7

- **Objet** : `docs/procedures/consigne-concepts-sans-lien-T0.7-v1.md`
  (`32a7194ae7097a132a3b37c161b31fbcafec0ee32998a909d875823e54e17bec`, égale à son compagnon) et son journal
  (`36fcc1fd7628a5d4bd4d9416bf6d8b0d49ae29fb896f5b5e76a579bf7c2d626f`).
- **Contre-lecteur** : Claude Fable 5.2, sous-agent neuf de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy` ; autre modèle
  que le rédacteur (Opus 5.5) ; n'a écrit ni T0.7, ni son module, ni ses jeux, ni cette consigne. **Il a lu des fichiers de
  T0.7 : exclu ensuite de tout rôle de lecteur de P3-bis.** Rôle (A) seulement ; le rôle (B) n'est pas fait.
- **Consigne suivie** : `…/consignes-mere-2026-11-10-0500-v1/consigne-lot3b-cl-et-script-concepts-t07-v1.md`
  (`31cc178289da8663a8694bef58d555c6b143e429eb1848f18e4be73011a85413`, vérifiée avant lecture) ; interdits communs v2
  (`1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f`, vérifiés), tenus en entier, règle 9 comprise.
- **Heures** (relevées par `date -u`) : début le 2026-11-10 à 08:17:48 UTC ; couples écrits à 08:27:19 UTC ; rédaction de
  ce texte commencée à 08:27:44 UTC. Clone : `main`, commit `60e8c0e5`.
- **Couples** : `prereg/contre-lectures/consigne-concepts-sans-lien-T0.7-v1-cl1-couples-v1.json`
  (`453a9244d4083c1bbc8075e102c47a08e6d1c7f666ea903e2d3d951bdd794180`), 32 couples `{id, section, motif, ancien, nouveau}` ;
  chaque `ancien` se trouve **une seule fois** dans la consigne ; les 32 appliqués à la suite donnent un texte où les
  annexes, les exemples, les marqueurs de la section 5 et la table des contrôles restent bien formés (contrôlé par
  programme, en mémoire).

## Verdict (une ligne)

**Accord au module exact ; consigne scellable après traitement des couples : un bloquant (CC-01), quatre groupes majeurs
(CC-04 ; CC-05 et CC-06 ; CC-07 à CC-09 ; CC-10 à CC-14), les autres recommandés ; aucune objection aux décisions de la
mère de R-2105.**

## 1. Ce qui a été lu et rejoué

| pièce | empreinte | lu |
|---|---|---|
| consigne v1 et journal | `32a7194a…`, `36fcc1fd…` | en entier |
| brouillon 1 de la consigne | `acc7bdfb…` | en entier |
| inventaire des jeux | `c9910a54…` | sections 3, 4 (en-tête), 4.2, 4.3, 5 (lots 2 à 4, calendrier), 6, 7, 8 |
| `t07/sondes_neuves_v1.py` au commit `8dc1cb09` (`git show`) | `b1c59783…` | l. 58-69, 164-220, 330-372 |
| `t07/lecture_v2.py` au commit `8dc1cb09` (`git show`) | `9d5c1c05…` | l. 255-285, 445-465 |
| `sondes/temoins.py`, `premier_test_ia/empans.py`, `harnais/formats.py` (égaux sur `main` et à `8dc1cb09`, empreintes des deux côtés relevées) | `3b051b6f…`, `58043c95…`, `98dbfa9b…` | l. 1-140 ; l. 1-61 ; l. 1-110 |
| `manifeste.py` (égal sur `main` et à `8dc1cb09`) | `1a5c7464…` | l. 35-56 |
| `scripts/verifier_jeux_synthetiques_t07_v2.py` | `e53c9c27…` | l. 140-176, 398-413 |
| `harnais/validation_reelle.py` | — | l. 83-87 |
| brouillon 20 de T0.7 | `9ef671ac…` | les lignes citées par la consigne (179, 243, 866-876, 992, 1076-1084, 1119-1126, 1374-1380, 1409, 1418-1432, 1756, 1822-1828, 2021-2026, 2061, 2472-2490, 2536) |
| consigne v3 des jeux | `d9de50a6…` | plan et section 0 |
| `registres/decisions.md` | — | lignes R-168, R-2100 à R-2105 |
| tokeniseur, commit `03e3cbd9`, trois fichiers (`git show`, en mémoire) | `79e3e522…`, `177c7b61…`, `6f38c737…` | chargé en mémoire pour rejouer les exemples |

**Rejoué en mémoire** (interpréteur du dépôt, `PYTHONPATH=src`, option `-B`, script sur l'entrée standard, rien d'écrit
hors des deux sorties) : annexe A, 776 entrées (A1 166, A2 148, A3 123, A4 100, A5 96, A6 127, A7 16), toutes de la forme
`[a-z]+( [a-z]+)*`, sans doublon ; annexe B, formes par concept et partie 32 + 29, 62 + 24, 89 + 16, 84 + 27, sans
doublon ; A ∩ B vide ; lexiques deux à deux disjoints ; aucune entrée de plusieurs mots de B ne contient un mot de A ni
d'un autre concept ; un seul bloc de chaque nom, un seul marqueur de début et de fin. Huit exemples : jetons du
tokeniseur réel 18/17, 16/16, 15/14, 18/18, 17/17, 18/17, 16/16, 17/18 (écart relatif maximal 0,067), 13 à 16 mots,
distance d'édition en mots de 4 à 11 dans la paire et d'au moins 4 entre exemples ; garde de
`jetons_message_utilisateur(fmt, "", phrase, 128)` passée et `jetons_texte` égal au compte nu pour les seize phrases
(gabarit rendu par `transformers` 5.18.0 depuis l'objet du tokeniseur et le gabarit de `tokenizer_config.json`,
`date_string` « 26 Jul 2024 »). **Les chiffres du journal du rédacteur (section 3) sont confirmés.**

## 2. Accord au module (commit `8dc1cb09`)

Conforme, point par point :

- `lire_phrases_concepts` (l. 330-352) : lignes vides ignorées ; première ligne de clés exactement `{format_lecture}`,
  valeur dans `FORMATS_LECTURE` (l. 68) ; chaque ligne suivante de clés exactement `concept`, `indice`, `phrase_concept`,
  `phrase_neutre`, les trois textes non vides ; `exiger_concept_sans_affect` sur chaque nom ; au moins `min_concepts`
  concepts, au moins deux paires par concept. La section 2 de la consigne le dit sans erreur ; l'appel à quatre concepts
  en mode réel est bien à `lecture_v2.py` l. 459.
- `indice` : ni type ni unicité contrôlés ; seul usage, le tri (l. 359). La consigne l'exige entier non booléen, unique,
  de 1 à n sans trou (C1, C11, C12) : juste et suffisant.
- `Extracteur.phrase` (l. 208-220) : `message_utilisateur` → `jetons_message_utilisateur(self.fmt, "", texte, 128)`,
  texte rogné, tronqué sans refus à `MAX_JETONS_PHRASE` (l. 69 ; `empans.py` l. 60) ; `phrase_seule` → `_ids` du texte
  rogné, sans borne. La borne de 40 jetons et le contrôle de 128 (C3, C12) écartent la troncature.
- Noms sans accents : `exiger_concept_sans_affect` les accepte ; les essais du module emploient déjà `meteo` et
  `geographie` (`tests/test_sondes_temoins.py` l. 67, 87) ; rien dans `src/` ni `tests/` au commit n'attend une forme
  accentuée (`git grep` borné).
- Renvois de lignes de la consigne vérifiés : tous justes, **sauf** `[jeux l. 172-175]` (fonction aux lignes 173-176 :
  CC-20).

**Défaut bloquant (CC-01, CC-02, CC-03)** : la section 6 lance le script avec `PYTHONPATH=src`. Or
`src/controle_ia/t07/` de `main` ne contient ni `sondes_neuves_v1.py` ni `lecture_v2.py` (liste du dossier au commit
`60e8c0e5`) : le paquet `controle_ia` de l'arbre de travail est trouvé le premier, l'import du module échoue, ou bien C4,
C10 et C12 jouent un autre code que celui dont C0 a vérifié les empreintes — un repli silencieux (R5). Couple : paquet
importé du seul `--module-src`, garde sur l'emplacement de chaque module importé, artefact.

## 3. Contrôles C0 à C13 : fermeture et vérifiabilité

| contrôle | jugement | couples |
|---|---|---|
| C0 | fermé ; artefacts présents ; deux gardes ajoutées (emplacement du paquet ; entrée de plusieurs mots inemployable) | CC-02, CC-03 |
| C1 | fermé ; contredit la remise complémentaire de la section 3 (indices 73 et suivants) | CC-17 |
| C2 | **non fermé** : « ASCII imprimable » admet `;`, `:`, guillemets, `$`, `%`, un point d'abréviation et la chaîne d'un jeton spécial du tokeniseur (lue comme jeton spécial malgré `add_special_tokens=False`) ; aucun contrôle mécanique des noms propres alors que 4.2 interdit « tout lieu nommé » | CC-07, CC-08, CC-09 |
| C3 | fermé, vérifiable | — |
| C4 | fermé ; **artefact contradictoire avec C0** (un gabarit faux pour toutes les phrases arrête à C0, code 2, avant tout code 1) | CC-04 |
| C5, C6, C7 | fermés, vérifiables ; dépendent des annexes (section 4) | CC-23, CC-24, CC-25 |
| C8 | fermé ; règle de conflit incomplète au second passage | CC-16 |
| C9, C10 | fermés, vérifiables | — |
| C11 | **ordre fautif** : le fichier final est écrit avant ses contrôles ; code de sortie non dit | CC-05, CC-06 |
| C12 | fermé une fois CC-01 traité ; le rejeu au commit de `CODE-T07` est bien prévu | CC-01 |
| C13 | rapporté ; « mots de nombre » sans liste ni mesure par paire | CC-18, CC-19 |

Chaque contrôle a son artefact (R5) ; après les couples, aucun n'en manque.

## 4. Annexes A et B

- **Doublons, recouvrements** : aucun (section 1).
- **Annexe A, ampleur (point ouvert 2)** : l'ampleur est justifiée, les listes étant remises à l'écrivain ; un trou sur un
  mot direct coûte plus qu'une entrée de trop. **Trous constatés**, sur des notions que la prose de la consigne nomme
  elle-même : « le plan » (4.3, Q4) sans `plan` ; « un résultat » (4.1) sans `result`, `success`, `fail` ; l'argent sans
  `buy`, `sell`, `worth`, `value` ; la valence sans `good`, `bad`, `best`, `worst` ; le danger sans `safe`, `warning`,
  `severe` ; l'épreuve sans `check`, `verify` ; le domaine des agents sans `analysis`, `method`, `task`, `report`,
  `sample`, `error`, ni `network`, `laptop`, `online` (le domaine neutre N3 y invite). Couples CC-23-A1 à CC-23-A6 :
  166 entrées ajoutées (A passerait à 942 : A1 180, A2 192, A3 160, A4 114, A5 133, A6 147, A7 16) ; aucune n'est dans
  l'annexe B ni dans un exemple. **Recommandés, à la décision de la mère** : chacun se prend ou se laisse seul.
- **Annexe B** : `mouser` au noyau de `chats` contredit « pas de chasse » (CC-24). Mots manquants qui laissent un concept
  entrer dans la phrase d'un autre ou dans une phrase neutre : saisons (`spring`, `season`), `team`, `game`, `exercise`,
  reliefs et eaux courants (`peak`, `slope`, `forest`, `harbor`, `stream`, `pond`…) : CC-25 (B passerait à 416 formes).
- **Laissé à la mère, sans couple** : le noyau de `meteo` porte `storm`, `thunderstorm`, `lightning`, `gale`, `hail`
  (« temps ordinaire » ?) ; le lexique de `sports` porte `race`, `tournament`, `league`, `touchdown`, `tackle` (le sport
  porte la compétition par nature ; la consigne l'atténue, elle ne l'ôte pas) ; Q4 n'en juge que sur échantillon.
- **Homographes refusés par construction** (« dans aucun sens ») : `wind` (instruments à vent, N6), `score` (partition,
  N6), `dummy` (mannequin, N4), `tears`, `rich`, `comfortable`, `watch`, `monitor`, et `spring` si CC-25 est pris : coût
  en renvois seulement, absorbé par la réserve.

## 5. Renvois, réserve, plancher

Règles nettes et mécaniques (un renvoi, retrait au second défaut, sélection par indice de remise, plancher 56 déclaré
sans étalonnage). Trois cas non décidés rendus vérifiables : deux paires réécrites en conflit entre elles, paire renvoyée
non rendue (CC-16), indices de la remise complémentaire (CC-17).

## 6. Contre-vérification à l'aveugle

- **Tirage et clé** : entropie neuve, `manifeste.graines` et `generateur` (signatures vérifiées, l. 37-55), clés nommées,
  empreinte de la clé consignée avant le lecteur : conforme à R9 et à la méthode du lot 2.
- **Défaut majeur (CC-10 à CC-14)** : le lecteur reçoit « les sections 1 et 7 de cette consigne » sans extraction ; en
  ouvrant le fichier il voit les exemples, les annexes et la table des contrôles, que la section 0 lui interdit. Couples :
  `remise-au-lecteur-v1.md` extraite par programme et scellée, chemins fermés nommés dans sa consigne.
- **Questions** : fermées, réponses à clés fixes, citation exigée pour Q4 ; aucun fichier de P3-bis donné, et le lecteur
  le déclare : conforme à l'écrit (a) [b20 l. 1424-1431].
- **Règle d'acceptation** : une paire jugée non conforme restait dans le fichier scellé ; priorité non dite entre « plus
  d'une non conforme » et « un oui à Q4 » ; sort de l'ancienne remise d'un concept réécrit non dit : CC-15 (recommandé).
- **Portée du seuil, à déclarer dans la provenance** (calcul, non une mesure) : avec 7 paires tirées et une tolérance
  d'une paire, un concept dont une paire sur dix est fautive est accepté environ 85 fois sur 100, une sur cinq environ
  58 fois sur 100 (loi binomiale, approximation du tirage sans remise). L'échantillon écarte un jeu grossièrement fautif,
  il ne certifie pas un taux bas ; seuil « sans étalonnage », déjà dit par la consigne.
- **Q1 à choix unique** : une phrase du concept qui toucherait deux concepts n'est pas vue par Q1 ; C7 et CC-25 le
  couvrent en partie. Pas de couple : une Q1 à réponses multiples durcirait la règle « plus d'une non conforme → concept
  réécrit » sans étalonnage.

## 7. Points ouverts du rédacteur et décisions de la mère (R-2105)

1. **Listes remises à l'écrivain** : d'accord (précédent de la consigne v3, section 0, vérifié). Les blocs sont remis
   sans la prose qui dit leur format : une phrase ajoutée à la section 5 (CC-21).
2. **Ampleur de l'annexe A** : gardée, et complétée (section 4).
3. **Seuils sans étalonnage** : acceptables comme choix déclarés ; portée du « 6 sur 7 » à écrire (section 6).
4. **Côté neutre commun** : réserve 2 juste, mais incomplète. Les quatre directions partagent le même terme neutre (huit
   domaines d'objets d'intérieur) : elles ont une composante commune, et leurs lectures ne sont pas indépendantes. La
   phrase du brouillon 20 « une ou deux au-dessus sont attendues par le seul hasard » (l. 1122-1124) suppose des lectures
   à peu près indépendantes : si une direction passe son plancher, les autres ont plus de chances de le passer avec elle.
   **À porter par la mère au texte de T0.7 ou à la provenance** ; aucun changement de la consigne.
5. **D-4** : le registre concorde (R-2101, proposée à 07:52 UTC ; R-2102, mot « (a) go » lu comme réponse à D-4, « à
   corriger par Lazar ») ; R-2104 nomme DS-3 bis à part, ce qui va dans le sens de la lecture de la mère. La marche en
   cas de correction (section 2) est cohérente : aucun contrôle ne dépend du format, C4 éprouve les deux chemins.
6. **Commit du module** : règle de rejeu de C12 au commit de `CODE-T07` juste ; CC-01 lie l'import à l'arbre vérifié.
7. **Contre-lecture courte du script** : confirmée par la mère ; elle doit porter d'abord sur CC-01 (emplacement des
   modules importés), C4 et l'ordre d'écriture de l'assemblage.

Décisions de R-2105 (annexes remises, annexe A étendue gardée, noms sans accents, réserves déclarées, contre-lecture du
script, contre-lecteur d'un autre modèle) : **aucune objection**.

## 8. Table des couples

| couples | objet | poids |
|---|---|---|
| CC-01, CC-02, CC-03 | paquet `controle_ia` importé du seul `--module-src` ; gardes et artefacts de C0 | **bloquant** (CC-01) |
| CC-04 | C4 : artefact et code de sortie accordés à C0 | majeur |
| CC-05, CC-06 | assemblage : contrôles avant l'écriture du nom final ; code 2 pour C11 et C12 | majeur |
| CC-07, CC-08, CC-09 | C2 : alphabet fermé, majuscules ; règle en français et en anglais | majeur |
| CC-10 à CC-14 | remise au lecteur extraite par programme, chemins fermés | majeur |
| CC-15 | acceptation : paire non conforme retirée ; priorité ; concept réécrit | recommandé |
| CC-16, CC-17 | cas de conflit et de renvoi non décidés ; indices de la remise complémentaire | recommandé |
| CC-18, CC-19 | C13 : liste fermée des mots de nombre, mesure par paire | recommandé |
| CC-20 | renvoi de lignes corrigé | forme |
| CC-21, CC-22 | section 5 : format des listes ; chasse et soin vétérinaire | recommandé |
| CC-23-A1 à CC-23-A6 | annexe A complétée, par catégorie (indépendants) | recommandé, à la décision de la mère |
| CC-24 | `mouser` ôté du noyau de `chats` | recommandé |
| CC-25-meteo, -sports, -geographie | annexe B, champs complétés (indépendants) | recommandé, à la décision de la mère |

**Si des couples des annexes sont pris**, le journal du rédacteur (comptes de la section 3) ne vaut plus pour elles : les
comptes neufs sont à écrire au traitement, et le développeur du script (rôle B) reçoit les couples retenus. Les huit
exemples passent tous les contrôles avec les 32 couples appliqués (alphabet, majuscules, annexes complétées, mots de
nombre : rejoué en mémoire).

## 9. Gestes déclarés, interdits tenus, refus

- **Jamais ouverts** : tout `lecture-sondes-t06.json` ; la lecture B et `donnees/lecture-b-7a-quarantaine-v1` ; tout
  `diag/` et `runs/` de 7a ; `essai/t06-explo-v3` ; `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`,
  `docs/notes/bras-attaque/` ; l'étiqueteur ; `scripts/extraire_mesures_epreuve_t06_v1.py` ; les textes d'actions de P3 ;
  aucun fichier de P3-bis. Aucune valeur de sonde de 7a sous mes yeux.
- **Gestes à déclarer** (noms seulement) : `git status --short` au début (il parcourt l'arbre de travail ; un seul nom
  affiché, sans rapport ; aucun contenu ouvert) ; listes non récursives de `docs/procedures`, de `prereg/contre-lectures`,
  de `src/controle_ia/t07/` et des 80 premiers noms de `docs/notes/g0-deux-semaines-v1/` ; `git ls-tree --name-only`
  **borné au dossier** `donnees/tokeniseur-llama-3.1-8b-instruct-v1/` du commit `03e3cbd9` ; `git branch -a --list` sur
  le seul motif du tokeniseur ; `git grep` sur le commit `8dc1cb09`, borné à `src`, `tests` et un script nommé ; lecture
  du premier couple de `T0.7-sondes-v0-v1-brouillon20-cl1-couples-v1.json` pour la forme du fichier de couples.
- **Tokeniseur** : la consigne de la mère ne nomme sa lecture que pour le rôle (B) ; je l'ai lu par `git show`, en
  mémoire, sans `fetch` ni écriture (règle 4 des interdits), pour rejouer les exemples. Déclaré.
- Aucune recherche récursive sur un dossier qui contient un chemin interdit ; aucun `env`, `printenv`, `set`,
  `export -p` ni `/proc/*/environ` ; aucun appel externe, aucune dépense ; aucune écriture git ; la suite d'essais n'a pas
  été lancée. Écrit : ce texte, le fichier de couples et leurs deux compagnons `.sha256`, rien d'autre.
- **Refus rencontrés** : aucun refus de permission ni de classifieur.
