# Journal des corrections — consigne v3 corrigée, v1, du jeu de phrases des concepts de T0.7

- **Objet** : `docs/procedures/consigne-concepts-sans-lien-T0.7-v3-corrigee-v1.md` (empreinte dans son compagnon) = la v3
  (`f3b9b4a8ebbc69ed10bbdccef414f48cf298c0727b88c25190ff43ad1d0b3af2`, intacte, R12) + les 38 couples de la contre-lecture
  R2 (`prereg/contre-lectures/consigne-concepts-sans-lien-T0.7-v3-cl1.md`,
  `8245a980cf688f9ce5e56524308da2bf20331c94395c4f2b99084cc950a292e5`, égale à son compagnon) + les décisions de la mère de
  R-2183.
- **Rédacteur** : celui de la v3 (Claude Opus 5.5, sous-agent de la session mère) ; aucune phrase du jeu lue. Travail le
  2026-11-10 de 11:09:03 à environ 11:12 UTC (heures relevées par `date -u`).
- **Méthode** : les 38 couples ont été lus **par programme** dans la contre-lecture (blocs « texte actuel » et « texte
  corrigé ») et appliqués dans leur ordre à une copie de la v3 ; chaque « texte actuel » a été trouvé exactement une fois
  (B-1e : quatre fois, toutes en section 1, vérifié sur la v3). Puis les corrections de la mère et le traitement du résidu,
  appliqués de même (chaque texte remplacé trouvé une fois).

## Couples de la contre-lecture

| couple | sort | note |
|---|---|---|
| B-1a | appliqué | section 1 sans la liste des défauts passés |
| B-1b | appliqué | titre de la section 7 sans rang de tour |
| B-1c | appliqué | |
| B-1d | appliqué | ⌈n / 10⌉ rétabli (avec A-11) |
| B-1e | appliqué (4 occurrences) | renvois `[v2 § 1]` ôtés de la section 1 |
| B-1f | appliqué | **décision de la mère (R-2183)** : la section 7.3 n'est plus remise au lecteur |
| B-1g | appliqué | bornes de la remise au lecteur : `## 7. ` à `### 7.3 ` ; écart au v2 déclaré en section 6 |
| B-1h | appliqué | statut de Q6 ôté de la question |
| B-1i | appliqué | statut de Q6 dit hors de la remise |
| B-1j | appliqué | la commande du lecteur ne dit rien des tours ni de la règle |
| A-1a | appliqué | clés des réponses et rapport du lecteur nommés (noms de fichiers ensuite rendus neutres, voir résidu) |
| A-1b | appliqué | |
| A-2a | appliqué | E9, phrase neutre neuve (niveau à bulle) : rejouée |
| A-2b | appliqué | E12, phrase du concept neuve (sans mot de nombre) : rejouée |
| A-2c | appliqué | jetons 23/23, 21/23, 21/21, 25/26, écart maximal 0,087 : **confirmés** au rejeu |
| A-3a | appliqué | annexe C `chats` + 39 entrées |
| A-3b | appliqué | annexe C `geographie` + 24 entrées |
| A-3c | appliqué | |
| A-4a | appliqué | paires gardées sous les contrôles du v2 à l'assemblage |
| A-4b | appliqué | `amont_tour3` : empreinte de la v2 pour les pièces des deux premiers tours |
| A-4c | appliqué | |
| A-5 | appliqué | bloc `exemples` à quatre lignes E9 à E12, N5 à N8 |
| A-6a, A-6b, A-6c | appliqués | C6 inchangé, dit tel |
| A-7 | appliqué | faute de consigne avant l'écrivain : version suivante, pas un échec du tour |
| A-8a, A-8b, A-8c | appliqués | accord au brouillon 21 de T0.7 (R15, instant de fermeture, session de l'inscription) ; textes du brouillon 21 repris de la contre-lecture, non relus par moi |
| A-9 | appliqué | fichiers et clés du second lecteur de Q4, passages suivants en `-p2`, `-p3` (R12) |
| A-10a, A-10b, A-10c | appliqués | C13 (b) défini pour une moyenne nulle, mesure (d) des signes d'écriture, « couverte » défini |
| A-11 | appliqué | |
| M-1, M-2, M-3, M-4 | appliqués | |

**Couples écartés : aucun.**

## Corrections de la mère (R-2183) et résidu

- **Règle d'acceptation retirée de la remise au lecteur** : par B-1f et B-1g ; l'écart aux deux premiers tours (qui
  recevaient toute la section 7 de la v2) est **déclaré** en section 10, réserve 6, et en section 6 (B-1g) ; à porter en
  provenance.
- **`hairball` retiré du noyau de `chats`** : appliqué **par l'annexe C** (entrées `hairball`, `hairballs` ajoutées à la
  ligne `chats`), non par une modification de l'annexe B. Raison : l'annexe B doit rester égale à l'octet à celle de la v2
  (garde de C0, section 6, point 2) et les paires gardées de `meteo` et `sports` ont été contrôlées contre elle ; par
  l'annexe C, `hairball` ne compte plus pour la présence du concept et est interdit dans la phrase du concept (C15), ce
  qui est l'effet voulu ; il reste interdit dans les phrases neutres et les autres concepts (C7), ce qui ne coûte rien.
  Écrit aussi en section 4.1 et dans l'en-tête de l'annexe C. **Si la mère veut la lettre** (entrée ôtée de l'annexe B),
  il faut alors réécrire la garde d'égalité de C0 (« égale à la v2 sauf `hairball` ») : point à trancher, défaut : par
  l'annexe C.
- **Résidu « noms de fichiers en `-v3` » dans la remise au lecteur : traité.** Les sections 7.1 et 7.2 nomment
  désormais `echantillon.json`, `remise-au-lecteur.md`, `reponses.json` et `rapport.md` ; la mère copie à l'octet les
  fichiers versionnés vers ces noms dans le dossier du lecteur, et retour, empreintes vérifiées et consignées (section 9,
  étape 5) ; la clé n'y est plus nommée ; « les 14 paires » devient « les paires des concepts du lot » (le nombre disait
  que deux concepts seulement étaient lus). Ajout au point 12 du script : le fichier d'échantillon ne porte aucune mention
  de tour, de version, de concept ni de consigne. **Vérifié par programme** sur la remise au lecteur extraite avec les
  bornes neuves : aucune occurrence de « tour », « v2 », « v3 », « inchang », « échec », « 56 », « seuil », « non
  conforme », « rapportée », « acceptation ».
- **En-tête** : statut, journaux, section 9 étape 1 (contre-lecture faite) mis à jour.

## Rejeu des exemples (E9 et E12 modifiés ; E10 et E11 rejoués aussi)

Tokeniseur réel (`tokenizer.json` `79e3e522…`, `tokenizer_config.json` `177c7b61…`, `special_tokens_map.json` `6f38c737…`,
pris par `git show` au commit `03e3cbd9`), `tokenizers` 0.23.2, `transformers` 5.18.0, hors ligne :
- jetons 23/23, 21/23, 21/21, 25/26 ; écart relatif maximal 0,087 ; 20 à 22 mots ;
- C4 : `jetons_message_utilisateur(fmt, "", phrase, 128)["jetons_texte"]` = compte nu = `_ids` pour les huit phrases
  (`FormatChat`, `date_string` « 26 Jul 2024 », `empans.py` `58043c95…`, `formats.py` `98dbfa9b…`) ;
- alphabet fermé, aucune majuscule hors du premier caractère, ni ` ,` ni ` .` ; aucun mot de l'annexe A ; aucun mot de
  l'annexe B dans une phrase neutre ; un mot du noyau et aucun mot d'un autre concept ni de l'annexe C corrigée dans chaque
  phrase du concept ; aucune suite commune de quatre ni de trois mots dans une paire ; aucun mot de nombre (pluriels
  compris) ; distance d'édition en mots d'au moins 18 entre eux, 16 aux exemples de la v2, aucune suite commune de six
  mots : la note de la section 5 reste exacte.
- Annexe C corrigée : bien formée, sans doublon, disjointe de l'annexe A et des lexiques des autres concepts ;
  **173 entrées pour `chats`** (132 + 39 de A-3a + 2 pour `hairball`) et **58 pour `geographie`** (34 + 24) ; noyau libre
  (une entrée est couverte dès qu'une de ses formes est à l'annexe C) : 10 sur 19 pour `chats`, 47 sur 58 pour
  `geographie` (seuil de C0 : 8). Annexes A et B et ligne de format égales à la v2 (comparées).
- Structure : marqueurs de la section 5 et cinq blocs présents une fois chacun ; bornes `## 1. `, `## 2. `, `## 7. `,
  `### 7.3 ` présentes une fois chacune.

## Laissés sans couple (constats « sans couple » de la contre-lecture)

- Liste fermée des mots de nombre de C13 sans pluriels (`thousands`, `hundreds`, `dozens`) : **non traitée** (elle est
  celle du v2 ; les exemples n'en portent plus) ; à reprendre par la mère si elle le veut avant le scellement définitif.
- Équilibre des `the` non dit à l'écrivain (C13 (b) le mesure seulement) : **non traité** ; la règle « no "the" that points
  to one particular object » y pourvoit en partie.
- Erratum « six points » → « sept » (R-2183) : il porte sur le fichier de la contre-lecture, que je n'écris pas.
- Brouillon 21 de T0.7 (citer l'empreinte de la consigne corrigée ; réserve 5) : hors de ce texte, à la mère.

## Gestes déclarés, interdits tenus, refus

- Lus : la contre-lecture v3-cl1 (en entier) ; `registres/decisions.md`, R-2183 ; la v2 pour ses annexes et son bloc
  `exemples` (par programme) ; mes fichiers v3. Rien d'autre sous `donnees/`. Aucune phrase du jeu lue.
- Jamais ouverts : tous les chemins des interdits communs v2. Aucune recherche récursive ; aucun `env`, `printenv`, `set`,
  `export -p`, `/proc/*/environ` ; aucun appel externe, aucune dépense ; aucune écriture git ; suite d'essais non lancée.
- Écrits : la consigne corrigée, ce journal et leurs compagnons `.sha256` ; copies de travail dans le bloc-notes.
- **Refus rencontrés** : aucun.
