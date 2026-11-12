# Contre-lecture du registre des prédictions v2 — v1

Contre-lecteur neuf (règle R2), qui n'a écrit ni la v1 ni la v2. Modèle : Fable 5.2 (`claude-fable-5-2`).
Heures (`date -u`) : début 12:34 UTC, fin 12:37 UTC, le 10 novembre 2026. Branche courante : `claude/upbeat-cray-dmauvv`.

## Verdict

**Bon pour impression avec retouches.** Les comptes sont intacts, aucun taux, aucun résultat de la mesure unanime, page 3
identique à la v1, PDF complet. Deux retouches sont nécessaires avant impression (E1, E2 : le complément d'antériorité rend
deux phrases fausses ou périmées, dont une contredit la page 1), une troisième est recommandée (E3). La v2 est scellée :
les retouches font une v3 (nouveau nom, R12), pas une réécriture.

## Empreintes vérifiées (toutes conformes à la demande)

| fichier | sha256 (début) |
|---|---|
| `registre-predictions-une-page-v2.html` | 65ecb3ca (égal au compagnon) |
| `livrables/registre-predictions-une-page-v2.pdf` | 6bc76238 (égal au compagnon) |
| `registre-predictions-une-page-v1.html` | d9baa678 |
| `reponses-mere-registre-predictions-v1.md` (`origin/main`) | 9639b715 |
| `reponses-bras-registre-predictions-v1.md` | 85292df7 |
| `complement-anteriorite-registre-predictions-v1.md` | 9f756d07 |
| `prereg/preenregistrement-mesure-unanime-v15.md` | 3a1651f4 |

Les empreintes courtes des pièces citées page 2 (c91a3b4e, 05e896da, 9ce91ba1, b9a07230, 42180088, c8a00b3f, 5916e62e,
070a6dd4, 0b35494b, 1407e460, 9086a420, 8e267952, 26a3ff72, 1f6a6da2, a5ac6632, 0f10881b, dece9980, 9f7830b9, bc53b746)
sont recalculées sur disque et conformes. Non recalculables sur cette branche : `88418df0` et `fb6c2f34` (fichiers du
bras absents ici ; la v2 le dit page 2 : « non vérifiées par lecture »), `54c5713d` (hors du dépôt), `7d19704d`,
`a745adc5`, `320463e6`, `aaf43f95`, `7dade9ef` (inchangées depuis la v1, hors de l'objet).

## Les sept contrôles

1. **Différence v1 → v2, page 1** : conforme sur le fond. Les lignes des comptes ne figurent pas dans la différence :
   31/0/0, 32/2/1, 33/7/6, 96/9/7, 33/11/6, 26/7/6 inchangés, ainsi que toutes les lignes de la table des séries. Aucun
   taux (les seuls « % » de la v2 sont des seuils, page 2 : 5 %, 97,5 %, 1 %). Changements hors des trois annoncés : voir E9.
2. **Définitions de la page 2** : treize lignes relues contre les lignes citées. Conformes, sauf E5, E6, E7.
   B1 : les trois prédictions (`E_sf`, `D`, `M`, l. 152-154) correspondent bien aux trois objets de la l. 124-125.
3. **Phrase d'antériorité** : exacte au regard de la pièce de la mère (sauf E4, E10) ; périmée au regard du complément (E1, E2).
4. **M1 et M4** : fidèles aux lignes 139-142 et 167-170 ; aucun nombre de résultat (page 2 ne reprend que les seuils 1 % et
   5 % de l'énoncé). Réserve E8 sur la fourchette de la page 1.
5. **Ligne « mesure unanime »** : inchangée depuis la v1 ; heures de course, empreinte du verdict, « non lu » ; aucun résultat.
   Page 2 : « hors de la pièce (cloison) », aucun résultat.
6. **Page 3** : identique à la v1 ; seule la classe de la balise change (`page2` → `page2 page3`).
7. **PDF** : 3 pages, A4 paysage, polices incorporées ; texte extrait égal au texte du HTML (aux coupures de mots et au pied
   de page près) ; rendu des trois pages regardé : rien de coupé, aucune table tronquée. Page 1 très dense mais lisible.

## Table des écarts

| n° | gravité | lieu | écart | retouche |
|---|---|---|---|---|
| E1 | importante | page 2, table d'antériorité, ligne T0.3 | « la pièce note « pas de verdict scellé » » : contredit la page 1, qui cite ce verdict (`bc53b746`, l. 10, 12, 25). Le verdict existe, scellé, hors de `main`. | voir « Phrases à changer », 2 |
| E2 | importante | page 1 (« étiqueteur non couvert par la pièce ») ; page 2 (ligne « Étiqueteur, phase 1 ») | périmé : le complément établit que le préenregistrement est scellé avant le versement des données de la lecture. | voir « Phrases à changer », 1 et 3 |
| E3 | moyenne | page 2, dernier bloc ; page 1, « Préenregistré, pas encore couru » | « Aucun résultat de ces séries n'existe » est plus fort que la source (« aucune course décisive de ces séries n'a eu lieu ») : la pièce du bras (l. 15-17) rapporte une simulation S1 de la courbe dose-réponse, courue à 11:06:16 UTC sous une note de conception scellée, que la v2 passe sous silence. De plus la courbe figure sous le titre « Préenregistré » alors que son texte est un brouillon non scellé. | écrire « Aucune course décisive de ces séries n'a eu lieu ; une simulation de la courbe (S1) a couru sous sa note de conception scellée, sans résultat rapporté ici » ; page 1 : « courbe dose-réponse de l'organisme : pas encore préenregistrée (brouillon) » |
| E4 | mineure | page 1, phrase d'antériorité | ponctuation fautive « (… l. 477-478), ; non établis » | supprimer la virgule |
| E5 | mineure | page 2, P-R1 | renvoi « l. 31 » : la ligne 31 est un chapeau ; W et G sont définis l. 32 (erreur reprise de la pièce de la mère) | « l. 32, 43 » |
| E6 | mineure | page 2, « C1 à C3 (autres sens) » | « critères cités au seul registre » : la mère ne dit pas « critères » (elle dit « seuils » pour R-1817) et son « seulement au registre » tient à ce qu'elle n'ouvre pas les fichiers de l'étiqueteur. Non vérifié ici (registre interdit). | « Étiqueteur : sens relevé au registre des décisions seulement, ses fichiers n'étant pas ouverts par la pièce » |
| E7 | mineure | page 2, M1, M4, C1 à C3 | guillemets : majuscule initiale ajoutée (M1, M4), point final ajouté dans la citation (M4) ; « Δ_W(10) > 0 » etc. recomposés de deux cellules de table. Fond exact. | sortir le point des guillemets ; acceptable sinon |
| E8 | mineure, à vérifier par qui a le droit | page 1, ligne « mesure unanime » (inchangée depuis la v1) | « M1, 0,05 à 0,12 fausse alerte par épisode » : cette fourchette n'est pas dans les lignes 139-142 (qui donnent 0,0725 et 0,077 sous indépendance, « au-dessus de α = 5 % »). Je n'ai pas le droit de lire le reste du texte ; la note de page 2 dit « lignes 139-142 et 167-170 seulement ». | donner la ligne qui porte la fourchette, ou aligner la page 1 sur la page 2 (« au-dessus de 5 % ») |
| E9 | mineure | page 1 | changements hors des trois annoncés : titre, ligne d'état (les empreintes courtes des contre-lectures disparaissent), « Noms de code : lexique, page 2 » ajouté aux Mots, marge haute 5 → 4 mm, interligne 1,13 → 1,08, glose « saboteurs sans consigne » de T0.6 retirée. Sans effet sur le fond. | aucune ; à déclarer dans la note de version |
| E10 | mineure | page 1, « non établis sur `main` » | la mère dit « non établi sur `main` » pour les trois textes d'analyse seulement ; pour les deux premières courses d'A1-v3 elle dit « non établi » sans restriction. La page 1 tait aussi « établi par le registre seul » (rejeu), dit page 2. | voir « Phrases à changer », 1 |
| E11 | mineure | pages 1 et 2 | noms nouveaux non définis : « R1-R2 » (qui heurte « critères R1 à R8 » de la page 1), « A1-v3 », « `main` », « session-dépôt », « session du bras ». | une ligne au lexique |
| E12 | mineure | page 1, en-tête | « v2 à contre-lire » | citer cette contre-lecture dans la version suivante |
| E13 | information | page 1, « règle du bras d'attaque (`88418df0`) et témoin de Bailey (`fb6c2f34`), scellés » | la réserve « données relayées, non vérifiées par lecture » n'est dite qu'en page 2. | ajouter « (relayé, page 2) » si la place le permet |

## Phrases à changer pour tenir compte du complément (`9f756d07`)

Faits du complément recontrôlés ici, sur la branche courante seulement : `c53a03a7` (10 novembre, 09:31:54 UTC) et
`d858b66f` (8 novembre, 00:17:23 UTC, « R-1744 : préenregistrement de l'épreuve de l'étiqueteur scellé ») sont ancêtres
de la tête courante et **non** de `origin/main` ; le verdict de l'étiqueteur cite bien `16aef7a0` à sa ligne 111 ;
00:17:23 → 14:41:50 font 14 h 24 min. Non recontrôlé : la date de `16aef7a0` (branche `donnees/`, interdite).
**Limite à garder dans le texte** : le complément établit que le scellement précède le *versement des données*, pas le
*début de la course* (« heure exacte de la course non relevée »). Ne pas écrire « établi » sans cette précision.

1. **Page 1, « Ce que le registre établit ».** Remplacer
   « …par les lignes que donne la pièce de la mère (`reponses-mere-registre-predictions-v1.md` § 3, `9639b715` ; page 2),
   sauf deux exceptions connues, le nul v9 (…) et B1 de P3 (…), ; non établis sur `main` : l'heure de scellement des trois
   textes d'analyse R1-R2 et les deux premières courses d'A1-v3 ; étiqueteur non couvert par la pièce ; réfutations… »
   par
   « …par les lignes que donnent la pièce de la mère (`reponses-mere-registre-predictions-v1.md` § 3, `9639b715`) et son
   complément (`9f756d07`) ; page 2), sauf deux exceptions connues, le nul v9 (…) et B1 de P3 (…) ; étiqueteur :
   préenregistrement scellé avant le versement des données de sa lecture, heure de course non relevée ; non établis :
   l'heure de scellement des trois textes d'analyse R1-R2 (sur `main`) et les deux premières courses d'A1-v3 ;
   réfutations… ».
2. **Page 2, table d'antériorité, ligne « T0.3, simulation ».** Remplacer « établi (texte au commit de 08:02:47, course à
   08:02:57, le 4 oct.) ; la pièce note « pas de verdict scellé » » par « établi (texte au commit de 08:02:47, course à
   08:02:57, le 4 oct.) ; verdict scellé (`bc53b746`) hors de `main` (commit `c53a03a7`, 10 nov., 09:31:54 UTC), que la
   pièce, qui ne lit que `main`, ne voit pas ». Troisième colonne : « l. 79 ; complément, point 1 ».
3. **Page 2, table d'antériorité, ligne « Étiqueteur, phase 1 ».** Remplacer « **non couvert** : la pièce n'ouvre pas ses
   fichiers ; son verdict (`9f7830b9`) ne donne pas d'heure de scellement » par « hors de la pièce ; établi par les commits :
   compagnon du préenregistrement au commit `d858b66f` (8 nov., 00:17:23 UTC), données de la lecture versées au commit
   `16aef7a0` (8 nov., 14:41:50 UTC), que le verdict cite (`9f7830b9`, l. 111) ; heure exacte de la course non relevée ».
   Troisième colonne : « complément, point 2 ».
4. **Page 2, chapeau de la table d'antériorité.** Après « …les heures de course qui l'établissent. » ajouter « Deux
   compléments hors de `main` (T0.3, étiqueteur) : `complement-anteriorite-registre-predictions-v1.md` (`9f756d07…`). »
   En-têtes : « État d'après la pièce de la mère et son complément » ; « Ligne de la pièce, ou complément ».
5. **Page 2, note « Source ».** Ajouter le complément (chemin et sha256 entier
   `9f756d079c35d555cc25fc400681e2d6c5a180b6e69f23827b8a4b2f6f1d2071`) à côté de la pièce de la mère.

## Fichiers ouverts

En entier : la v2 (HTML) ; la différence v1 → v2 (la v1 n'est lue que par `diff`) ; la pièce de la mère
(`git show origin/main:…`) ; la pièce du bras ; le complément ; le PDF (`pdfinfo`, `pdffonts`, `pdftotext`, rendu en
images dans le dossier temporaire de la session).
Par lignes seulement : `prereg/preenregistrement-mesure-unanime-v15.md` l. 139-142 et 167-170 ;
`prereg/P3-addendum2-audit-verdict-v1.md` l. 115, 124-126, 150-156 ; `docs/verdicts/verdict-P3-premier-test-i-a-v2.md`
l. 476-478 ; `prereg/T0.5-pilote-8B-v1.md` l. 101, 107-108, 122 ; `docs/verdicts/verdict-T0.5-pilote-v1.md` l. 49 ;
`docs/decisions/decision-N-057-v1.md` l. 32-33, 42-43 ; `docs/decisions/decision-N-054-v1.md` l. 40-42 ;
`prereg/agregation-r1-v4-v1.md` l. 83-84, 91, 154-156 ; `docs/verdicts/verdict-agregation-r1-v4-v1.md` l. 3, 71-73 ;
`prereg/R1-addendum-relance-v4.md` l. 9-11 ; `prereg/analyse-par-episode-v1.md` l. 14, 25, 159 ;
`prereg/preenregistrement-attaque-goodhart-v3-v4.md` l. 764-765 ; `docs/verdicts/verdict-validation-nul-v9-v1.md` l. 7,
13, 26, 32 ; `docs/notes/ideation-organisme-v1/validation-nul-v9-v1/audit-verdict-validation-nul-v9-v1.md` l. 27 ;
`prereg/analyse-principale-r1-r2-v1.md` l. 31-36, 43 ; `docs/verdicts/verdict-analyses-r1-r2-relance-v4-v1.md` l. 9 ;
`docs/verdicts/verdict-etiqueteur-phase1-v1.md` l. 111.
Empreinte seule, contenu non lu : `prereg/analyse-blanche-noire-v3.md`, `prereg/addendum-1-gardes-analyses-r1-v4-v1.md`,
`docs/verdicts/verdict-T0.3-simulation-lemme-theoreme-v1.md`, les trois brouillons de la v1 et leurs trois contre-lectures
(pour identifier `aeb45c39` : c'est `contre-lecture-registre-predictions-une-page-v1.md`), les deux compagnons de la v2.
Métadonnées de commit seulement : `d858b66f`, `c53a03a7` (ancêtres de la tête courante).

## Réserves de cette contre-lecture

- Les deux fichiers de décision et la note d'audit du nul v9 ne sont ni des préenregistrements ni des verdicts ; je n'en ai
  lu que les lignes citées par la page 2, parce que le contrôle 2 les demande.
- Non ouverts, donc non vérifiés : `registres/decisions.md` (renvois R-1817, R-1849 et lignes de la mère), les fichiers du
  bras, tout le reste du préenregistrement v15, la source de la page 3 (identité à la v1 seulement).
- La l. 115 de `P3-addendum2-audit-verdict-v1.md` porte un résultat de P3 déjà publié en page 1 ; aucun résultat fermé lu.
- Le dossier temporaire de la session contenait déjà des fichiers d'autres agents ; j'y ai écrit `p1.txt`, `p2.txt`,
  `p3.txt` et `pg-1.png` à `pg-3.png` sans vérifier d'abord si ces noms existaient : des fichiers de même nom ont pu être
  écrasés. Aucun autre fichier de ce dossier n'a été ouvert.
- Aucun compagnon `.sha256` créé pour ce fichier (un seul fichier de sortie permis) : à sceller par la session-dépôt.
