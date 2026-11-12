# P3-bis, écart 1 (R-2399) — vérification courte des corrections (lanceur v2, brouillon 2 de l'addendum) — v1

- Vérificateur : le contre-lecteur de `P3-bis-ecart1-contre-lecture-v1.md` (`9b1013dbfe479a7b1cbcbe36fe88598b68037c24657f8d2f577789a908a9f33e`),
  sous-agent, **Claude Fable 5.2** (`claude-fable-5-2`). Aucune lecture de T0.7, aucun appel à l'outil de location
  réel, aucun appel de modèle, aucune dépense, aucun commit.
- Écrit le 2026-11-12 à 00:02 UTC (heure relevée par `date -u`), sur demande de la session mère.
- Écrit : ce fichier et son compagnon ; bac à sable sous
  `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/p3bis-ecart1-cl/` (second arbre détaché,
  `arbre2`, extraction partielle au commit v2, mêmes quatre chemins ; il y reste, comme le premier).

## Verdict

**Scellable.** C1 et C2 sont appliqués à la lettre dans le lanceur v2, A1 à A7 dans le brouillon 2 ; toutes les
empreintes citées sont exactes ; rien d'autre ne change.

## 1. Lanceur v2

- `docs/procedures/P3-bis-temoin-positif-v1/lancer_p3bis_v2_ecart1_v2.sh` au commit
  `f3ff571d85b67770c2c8e53468fe918cda1d4310` = `2e294e5a64086806591cdd0724561d7a8d7fdaab464705c22f9b92687d6607fb`,
  compagnon conforme. Le commit est sur `prep/p3bis-ecart1-credit-v1` (local et `origin`, relevé sans `fetch`),
  enfant de `e13df72b`, lui-même enfant de S.
- `git diff --name-status e13df72b f3ff571d` : ajouts seulement (lanceur v2, essais v2, journal, rapport v2,
  `sorties-essais-v2/`). De S au commit v2 : aucun fichier modifié ni retiré. Au commit v2, le lanceur d'origine
  (`029bdb5c…`) et le lanceur v1 (`dc33635f…`) sont inchangés. Arbre gelé (douze `CHEMINS_GELES`) identique entre le
  commit du code `5e457525` et le commit v2 (`git diff --quiet`, code 0).
- `diff` du v1 au v2, cinq blocs, rien d'autre :

| Bloc | Contenu | Constat |
|---|---|---|
| `2,3c2,6` | en-tête : « lanceur d'écart v2 », heure, v1 gardé et jamais joué pour une création, C1 et C2 cités avec la contre-lecture `9b1013db…` | en-tête seul |
| `53c56`, `59c62` | usage sous le nom neuf | conforme |
| `210c213` | C1 | **égal caractère pour caractère au couple de la contre-lecture** |
| `227c230` | C2 : `round(v, 2) > 0` | égal au couple |

- Essais v2 (`essais_ecart1_lanceur_p3bis_v2.sh`, `e9a8dc69f39aa41e69209136db97aa9c2a1ab00400ca947c804934eabdaf0762`) :
  ne diffèrent des essais v1 que par l'en-tête, le nom du lanceur joué, la dernière ligne attendue de E5 et les cas
  E14 et E15. **Rejoués en entier** dans mon arbre (de 23:58:49 à 00:02:02 UTC, `date -u`) : code 0, dernière ligne
  « ESSAIS DU LANCEUR D'ÉCART 1 DE P3-BIS : CONFORMES », quinze cas, aucun « NON CONFORME » ; journal rejoué égal au
  journal versé (`5ee8246ebfee9b6a71676ad06d5a330db4bdc24a1af81a9e7eb08fa651e98952`) hors heures, durées et commit
  factice ; consoles **E5, E14, E15** et E9 rejouées identiques aux consoles versées.
- Témoin versé (essais v2 joués sur le v1) : E14 y crée, comme attendu ; les échecs suivants en découlent (l'instance
  factice créée reste sur le faux compte). Lu, non rejoué.
- **Essai de mon bac à sable, rejoué sur le lanceur v2 réel** (copie jouée des essais, faux outil) :

| Réponse, code de l'outil | Obtenu |
|---|---|
| `{"credit": 6.0}`, 1 | code 2, aucune création, aucune ligne d'écart dans `lancement.txt` |
| vide, 1 | code 2, aucune création |
| `{"credit": 6.0}`, 3 | code 2, aucune création |
| `{"credit": 50.0}`, 1 | code 2, aucune création |
| `{"credit": 0}`, `{"credit": -2.5}`, `{"credit": 0.004}`, 0 | code 3, aucune création |
| `{"credit": "six"}`, `{"credit": NaN}`, 0 | code 2, aucune création |
| `{"credit": 0.006}`, `{"credit": 6.0}`, `{"credit": 50.0}`, 0 | code 0, création factice |

## 2. Brouillon 2 de l'addendum

`brouillons/P3-bis-temoin-positif-v1/P3-bis-addendum-1-garde-credit-v1-brouillon2.md` =
`4e188814b52736edb6f690931b25e6c0d9cdaede20b23490d50aa5461c5ca537` (compagnon conforme). Relu par `diff` contre le
brouillon 1 (`0cf6c08b…`).

| Couple | État |
|---|---|
| A1 (nom, empreinte, commit, essais du v2 ; v1 jamais joué pour une création) | appliqué (« Moyen », conditions d'emploi 1 et 2) |
| A2 (règle neuve et première ligne de la table : outil en échec, au centime) | appliqué ; la deuxième ligne de la table porte aussi « au centime », cohérent |
| A3 (bloc 9 : outil en échec, code 2, même si sa réponse se lit) | appliqué |
| A4 (« par analogie », autre cas du texte) | appliqué |
| A5 (l. 2009-2011, deux fois ; GO l. 1940-1941) | appliqué |
| A6 (forme du scellement au statut ; points ouverts remplacés par les réponses (a), (b), (c)) | appliqué ; les réponses reprennent la contre-lecture sans la déformer |
| A7 (« alors que la recharge automatique tient le solde au-dessus de zéro ») | appliqué |

Empreintes citées, toutes recalculées et exactes : lanceur v2 `2e294e5a…`, v1 `dc33635f…`, origine `029bdb5c…` ;
rapports `19c13a84…` et `0162617a9e561d532bdbfc470b66e5836c4294084d36c3916c61a23663e3d002` ; essais `e9a8dc69…`,
journal `5ee8246e…` ; consoles de `sorties-essais-v2/` : E1 `68d47f87…`, E5 `738a1647…`, E14 `f4152abf…`, E15
égale à E1 (vrai), E8 `d31ac955…`, E9 `8f574e6b…` ; témoin : script `b6dbc70c…`, journal `e23fb874…` ; registre
au commit `af712f39…` = `3842d8115f236326ee22a7e8719433f208180c2dc57e90b1e43b74755460979a` ; contre-lecture
`9b1013db…` ; brouillon 1 `0cf6c08b…` ; texte scellé `76ab66ce…`. « 15 cas », « deux commits au-dessus de S, ajouts
seulement » : exacts. R-2404 et R-2406 lues : l'addendum les rapporte fidèlement, dont « vérifié par la mère : aucun
module de T0.7 ne parcourt `prereg/` par motif » (constat de la mère, que je n'ai pas pu refaire).

Hors couples, le brouillon 2 ne change que la forme (listes, phrases coupées), l'en-tête (dates, registre, contre-lecture
citée), et ajoute trois précisions sans effet sur la règle : la phrase sur les quatre lignes du texte où paraissent
« crédit » et « recharge » ; « un arbre de la branche d'écart convient » ; la réserve « vaut pour toute la course dès
qu'une création s'est faite sous l'écart ». Aucune ne déborde de R-2399 ni de la contre-lecture.

## 3. Remarque pour le scellement (ne change pas le verdict)

Le titre et la ligne « Statut » disent « brouillon 2, non scellé ». Si la mère les ajuste en versant le texte sous
`prereg/P3-bis-addendum-1-garde-credit-v1.md`, seules ces deux mentions devraient changer, et l'entrée du registre
devrait dire que le texte scellé est le brouillon 2 (`4e188814…`) à ces deux mentions près ; sinon, le sceller tel quel.
