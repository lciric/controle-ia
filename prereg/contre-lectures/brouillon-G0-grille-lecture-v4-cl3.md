# Contre-lecture R2 n° 3 — `prereg/brouillon-G0-grille-lecture-v4.md` — v1

- Contre-lecteur : sous-agent neuf (Fable 5.1). Je n'ai écrit ni la v1, ni la v2, ni la v3, ni la v4 de la grille, ni CL1, ni CL2, ni l'un des avis (Fable, conv-audit), ni la synthèse du collisionneur, ni aucune preuve que la grille lit. Début 2026-10-29 (`date -u` au lancement, vers 12:05 UTC) ; fin : dernière ligne du fichier. Clone **superficiel** (`git rev-parse --is-shallow-repository` = `true`) au commit `1d20f56c25deba09e308aed8c46472023f809a41` ; ni réseau, ni commit. Toutes mes commandes sous `LC_ALL=C.UTF-8` (`locale -a | grep -i -c -E "^c\.utf-?8$"` = 1).
- Fichiers interdits : `prereg/P3-consignes-v1.md` jamais ouvert ; rien dans `donnees/`, `diag/*/traces`, ni dans les branches `donnees/*` ou `quarantaine/*`. J'ai ouvert `diag/20261004-080257-t03/lecture.{md,json}` (lecture mécanique scellée de T0.3, hors `traces`) pour essayer les commandes du critère 5 ; `src/controle_ia/prereg.py` ; des lignes citées de P3 (`prereg/P3-premier-test-i-a-v1.md`), de P-007, P-009, P-011, P-015, N-005/N-006, N-026, N-029 et de la synthèse repli (l. 146-163) pour vérifier les [EXISTANT] ; les verdicts de `docs/verdicts/` et `brouillons/papier-C-…-brouillon5.md` pour essayer les motifs.

## Empreintes des fichiers lus (`sha256sum`, recalculées)

| fichier | empreinte |
|---|---|
| `prereg/brouillon-G0-grille-lecture-v4.md` (objet) | `a005651d21080342641bdecdde7640b8e1204391245bdb01ec8fd91affcbbe88` |
| `prereg/contre-lectures/brouillon-G0-grille-lecture-v3-cl2.md` | `2ef445ccb27a1c549cc22e17c1a96e8a5e30572212bec4bae12166697bd778ee` |
| `docs/brief-claude-code-programme-complet-v2.md` | `9261932a11f29e8643175bc6e150d5455067f58a3cb1e57dca99e02cb17aa3b2` |
| `docs/programme-controle-ia-v2.md` | `2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c` |
| `registres/decisions.md` (vivant, au moment de ma lecture) | `e4dbf68b27623932856dda1edd95239df657ae3955f68484af71b9422c9c4722` |

Le registre a bougé depuis la v4 (qui cite `95ae6c76…`) ; les lignes citées tiennent toujours : l. 34 R-025, l. 462 N-027, l. 978 R-750, l. 993 R-765, l. 1008 R-780 (vérifiées par `grep -n "^| <numéro> "`). Les dix-sept empreintes de pièces citées par la v4 que j'ai recalculées (T0.4 v3, T0.3, P3, P-007, P-009, P-015, P-011, N-026, N-029, N-007/N-008, N-005/N-006, synthèse niveau 2, rejeu des juges, synthèse repli, v3, CL1, v2) sont toutes égales aux huit premiers caractères cités.

## Verdict global

**À corriger avant scellement** — non scellable en l'état. **Un bloquant** (l'annexe B, index normatif des défauts, garde les défauts de la v3 pour D-G0-11 et D-G0-13 et contredit le corps qui applique CL2), **cinq majeurs** (motif « scellable » qui lit « n'est pas scellable » comme « Scellable » ; motifs cassés par la typographie du dépôt ; aucune précédence écrite entre sous-états ; préenregistrement sans clause R4 non traité ; annexe C point 6 sans les formes que les contrôles exigent), **neuf mineurs**. Le corps de la v4 est fidèle à CL2, à R-750 et à R-765 ; les huit critères sont mot pour mot ceux du brief ; les comptes que la table de tête annonce (92 pièces, 69 contre-lectures ; 0 négatif et 0 + 4 + 11 doutes pour M-8.3 ; trois verdicts de T0.4 inchangés, guillemets pris) sont **reproduits**, mais l'annexe F censée les porter est celle de la v3 et ne les contient pas.

## Critère 1 — fidélité aux critères N-027 : **tenu**

- `diff` entre le brief l. 190-201 et la v4 l. 90-101 (préfixe `> ` retiré) : identiques. Les huit titres de fiches (l. 313, 344, 397, 445, 506, 537, 561, 583) sont identiques, mot pour mot, aux lignes 192-199 du brief (comparés un à un).
- l. 103-105 : N-027, R-750 et R-765 sont bien présentés comme des décisions de calendrier et de repli qui ne changent aucun critère (N-027 l. 462 : « critères inchangés » ; vérifié).
- Les opérationnalisations qui pourraient durcir ou assouplir un critère (témoin P4-instrument, D-G0-11 ; deux doses, D-G0-2 ; périmètre « chiffres externes seulement », D-G0-9 ; TRACE-lite, D-G0-12 ; « validés », D-G0-10 ; domaine, D-G0-5) sont toutes étiquetées [À DÉCIDER] et renvoyées à Lazar, avec la source de l'exigence nommée (brief T0.x, décision en vigueur) et non le texte du critère. Aucune ligne ne reformule un critère.

## Critère 2 — application de CL2 : **partiellement tenu**

Vérifié sur le texte de la v4 seule (je n'ai pas lu la v3 : la colonne « ligne v3 » n'est pas contrôlée).

| constat | appliqué dans le corps ? | la table l. 45-51 dit-elle vrai ? |
|---|---|---|
| CLG2-01 | **oui** : Métrique l. 122 ; champ (γ) l. 138-140 ; section 2 l. 219-223 (exception de D-G0-7 pendant le report) et l. 224-228 ; critère 8 l. 608, 610, 624-627 ; Repli l. 749-751 ; script M-8.3 l. 629-666 avec bornes, doute → non concluant | **en partie** : « exécuté (annexe F) » — l'annexe F (l. 906-978) ne mentionne ni M-8.3, ni ses comptes (0 occurrence de « M-8.3 » dans l'annexe) ; j'ai reproduit : `grep -F` rend 3, 8, 11 pour « 0,5 », « 12 », « 8B » sur programme + brief ; le script rend 0 négatif et 15 doutes (= 0 + 4 + 11) |
| CLG2-02 | **oui** : l. 222-223 et l. 227-228 (seul le négatif par liste d'arrêt, (β) = « oui », est gelé au verdict de la première lecture) | **non pour l'annexe B** : la ligne D-G0-13 (l. 852) garde le défaut de la v3 « (a), (b), (c) » avec (b) « statut reporté tel quel », et range la règle de CL2 en « autre option » ; elle dit encore « à contre-lire en CL2 » |
| CLG2-03 | **oui** : M-3.2 l. 415 et M-3.5 l. 418 portent le même état sous chaque option ; D-G0-11 l. 430-441 défaut « condition » ; preuves attendues l. 408-409 | **non pour l'annexe B** : la ligne D-G0-11 (l. 850) garde « **réserve** » en défaut et « condition » en autre option |
| CLG2-04 | **oui** : `PRONONCE_1` l. 320 avec `[*«" ]*` ; filet `LARGE_1` l. 321-322 et l. 328 | **en partie** : la table dit « annexe C point 6 : prononcé une seule fois dans le verdict » ; l'annexe C point 6 (l. 873-879) exige la forme « Critère k de G0 : … » mais **ne dit pas « une seule fois »** (`grep -n "une seule fois"` : l. 48, 152, 840 seulement). L'essai « guillemets pris » n'est pas dans l'annexe F ; reproduit par moi (point 4 ci-dessous) |
| CLG2-05 | **oui** : motif (m4) l. 298-300, commande de la section 2 l. 232 | oui |
| CLG2-06 | **oui** : un motif par contrôle (F-3.4 l. 422, F-7.2 l. 576, D-G0-2 l. 379-389, M-3.3 l. 416, M-4.4 l. 464, F-3.1 l. 419), « non concluant si le motif échoue » écrit | **en partie** : « formes exigées ajoutées en annexe C point 6 » — l'annexe C ne contient ni « Doses non nulles : d1 ; d2 » (l. 385), ni « Agrégateur séquentiel : `<chemin>` au commit `<sha>` » (l. 464), ni la forme des fichiers d'identifiants de F-3.4 (l. 422), ni le fait que la ligne « Bras principal » porte l'agrégation et sépare les sondes par « ; » (l. 416, 419). « Essayés … (annexe F) » : absent de l'annexe F |
| CLG2-07 | **oui** : `find` l. 265 avec `prereg/contre-lectures`, branche `case` l. 269, exclusion `*G0-grille-lecture*`, (m2) par nom de base l. 296-297 | **en partie** : « exécuté (annexe F) : 23 → 92 » — l'annexe F dit toujours **23** (l. 916). Reproduit par moi : 92 pièces, 69 sous `prereg/contre-lectures/`, et les 69 sont chacune nommées par nom de base dans au moins une autre pièce inventoriée (69/69) |

Conclusion : les sept corrections sont dans le corps ; deux des trois majeurs sont **annulés par l'annexe B** (bloquant, point 1) ; la table renvoie quatre fois à une annexe F qui est celle de la v3 (point 7).

## Critère 3 — cohérence des [GELÉ], [À DÉCIDER], [EXISTANT] : **partiellement tenu**

- [EXISTANT] : tout ce que j'ai pu vérifier sur disque est exact : T0.4 v3 `4f711cd3…` ; P3 l. 228-230 (plancher apparié, même agrégation, mêmes actions), l. 272-275 (borne basse strictement supérieure au quantile 0,95 ; Bonferroni 97,5 %), l. 429 (« non interprétable »), l. 436 (sonde hors bras principal ne compte pas) ; P-011 l. 39-42 et 57 ; P-007 l. 22-24 (99e centile ≤ 0,2) ; P-015 l. 50-52, 61, 68 ; N-005/N-006 l. 97 ; N-029 § 1 (juge par action, prédicteur sur les traits du texte) et § 2 l. 42 (« Critère 4 de G0 … inchangé ») ; N-026 (bras « moyenne » de diagnostic) ; R-025 l. 34 (« Réserve écrite : vérifications de l'instrument en majorité ») ; R-750 l. 978 et R-765 l. 993 (citations de la v4 l. 30-34 exactes, à « (commun aux trois modèles) » près, omis sans changer le sens) ; synthèse repli l. 146-163 (douze choix). La convention l. 63-64 (« vérifié sur disque ») est honorée pour la v4 par la v2/CL1 et par moi, pas par l'auteur de la v4 (l. 18, dit).
- [À DÉCIDER] : chaque point a un défaut en annexe B sauf D-G0-1 (voulu). **Mais** l'annexe B contredit le corps pour D-G0-11 et D-G0-13 (point 1) ; D-G0-7 (l. 846) ne reprend pas l'exception pendant le report que le corps écrit l. 219-223 (point 10) ; D-G0-3, D-G0-6, D-G0-7, D-G0-8 n'ont aucune « autre option » (format de décision de CLAUDE.md : 2 ou 3 options ; point 14).
- [GELÉ] : marqueurs bien placés ; la seule entorse à « aucun constat d'état » est traitée au critère 7.

## Critère 4 — commandes et motifs : **partiellement tenu**

Essayés sur le dépôt (verdicts T0.4 v1-v3, T0.5, P3 v2 ; CL1, CL2 ; T0.3 ; programme, brief, brouillon 5 du papier C) et sur des lignes synthétiques.

Ce qui rend ce que la grille annonce : `PRONONCE_1` (v1 l. 3 « non concluant », v2 l. 10 « non prouvé », v3 l. 11 « prouvé » ; guillemets « », `**` et `"` pris ; le second `grep -o` rend bien « non prouvé ») ; `LARGE_1` (une espace insécable rend 0 strict et 1 large → non concluant, comme écrit) ; `CRIT_2`, `FAM_I`, `FAM_II` (mêmes prises et mêmes rejets que l'annexe F) ; `NEUTRE` (CL1, CL2, verdict T0.4 v3 : 1 ; brief : 0) ; motif R4 de négation (quatre lignes citées : 1, 1, 0, 1, conformes) ; M-0.7 (`True` sur T0.3 ; l'échappement `\'` passe bien à Python) ; M-5.2 (`7474743a`, `d73ac469`, `True`, `5609f920`), F-5.1 (`Counter({'confirmée': 31})`), F-5.2 (l. 39), M-5.3 ; F-1.2 (`[True, True, True]`) ; F-7.2 (programme 0, brief 0, brouillon 5 : robustesse 1 et second compte 0 ; deux phrases affirmatives synthétiques bien comptées) ; D-G0-2 (a)-(d) (cinq comptes à 1 ; une seule dose → 0) ; F-3.1 (positif et négatif sur lignes synthétiques) ; script M-0.8 (a) (92 ; aucun fichier « carte des hypothèses » dans son périmètre ; `P3-consignes-v1.md` exclu avant ouverture) ; script M-4.3 (doublon, `NaN`, `null`, `true`, épisode hors liste, épisodes sans statistique : tous comptés comme annoncé) ; script M-8.3 (cas sain code 0 ; chiffre absent de sa ligne code 1 ; introuvable sur la ligne citée sans « l'article imprime » → négatif, code 1 ; chiffres nus : 0 négatif, 15 doutes).

Ce qui attrape un faux ou casse (détails et corrections aux points 2, 3, 8, 9, 11, 12) :
- M-0.3 l. 248 : `grep -n -i -o -m1 -E "(non )?scellable( après corrections)?"` sur « Ce brouillon n'est pas scellable » rend `scellable` → lu « Scellable ». **Faux positif dans le sens du « tenu »**.
- M-3.3 l. 416 : « Bras principal : sonde linéaire par différence de moyennes, agrégation max » → second compte 1 → non concluant ; « différence de moyennes » est une famille du brief T0.7 (l. 169).
- M-4.4 l. 464 : `- **Agrégateur séquentiel** : …` (style du dépôt, en gras) → le motif `s(é|e)quentiel ?:` ne prend pas `séquentiel** :` → vide → non concluant. Même défaut pour (c) de D-G0-2 l. 385 : `**Doses non nulles** : 0,1 ; 0,3` → 0.
- M-0.7 l. 252 : `grep -i "liste d'arrêt"` ne prend que l'apostrophe droite ; `NEUTRE` prend les deux (`['’]`).
- Script M-8.3 : une exception (document de la table absent du disque, colonne `ligne` vide) sort avec le code **1**, le même que « au moins un absent ou un négatif » (l. 630-631) ; la ligne de synthèse manque alors.
- F-8.2 l. 610 : la « dernière ligne » attendue `F-8.2 negatifs 0 | F-8.2 doutes 0` ne correspond pas à ce que le script imprime (`M-8.3 absents N | F-8.2 negatifs N | F-8.2 doutes N`).

## Critère 5 — complétude : **partiellement tenu**

- **Aucune précédence écrite entre sous-états** quand plusieurs s'appliquent au même critère. La Métrique l. 120-124 ne l'écrit pas ; les paragraphes « États » des fiches sont des cascades qui contredisent parfois les lignes : critère 3 l. 425-426 finit par « non tenu — absent sinon » alors que M-3.2, M-3.5, F-3.4 rendent « invalide » et F-3.2 « absent » ; une famille (i) négative et une famille (ii) sans ligne donnent « négatif » par la cascade et « absent » par F-3.2. Le porte n'en dépend pas (tout « non tenu » = non franchie), mais **le gel (D-G0-13) et le choix 2 du repli en dépendent** : seul « négatif » gèle. Une preuve « invalide » et négative à la fois doit être « invalide » (la définition de « négatif » exige « intègre et complète », l. 122, mais ce n'est écrit nulle part comme règle de précédence) ; un négatif « suspect de propreté sans audit » doit rester « non concluant » (l. 695-696) et ne pas geler. Point 4.
- **Préenregistrement sans clause R4** : la règle l. 696-697 ne joue que si le préenregistrement contient `R4` ou `symétrie` ; sinon aucun audit n'est exigé et un résultat « trop beau » ne déclenche rien. Point 5.
- Seconde lecture : le verdict de la première lecture est exigé par l'annexe A (l. 808) et par (m4) (l. 299), mais son absence du dossier n'est ni dans la liste d'arrêt ni traitée (le champ (γ) devient incalculable). Point 13.
- Deux négatifs scellés pendant le report sur le même critère : « la pièce qui l'a gelé » (l. 229) n'est pas désignée (la première par date de commit du `.sha256` ?). Point 13.
- Cas couverts, vérifiés : brouillon seul, candidat, preuve après `C_lecture`, préenregistrement sans run ni verdict, verdict sans prononcé, contre-lecture manquante ou « non scellable », auteur non neuf, jeu d'épisodes différent, pièces concurrentes, pièce inventoriée hors dossier, motif hors liste, version non autorisée, clone superficiel, locale, fichier interdit, lecture tardive, lecture anticipée.

## Critère 6 — symétrie R4 : **partiellement tenu**

- Tenu dans la grille : « résultat suspect de propreté, positif ou négatif » → non concluant sans audit scellé (l. 692-697) ; réserve des sept jours « quel que soit le sens du verdict » (l. 698-700) ; Métrique l. 124 ; F-5.2 lit la règle D de T0.3 ; l'asymétrie du gel (seul le négatif gèle, le « tenu » est relu) vient de R-765, pas de la grille, et la v4 l'a ramenée à R-765 (CLG2-02).
- Trou : un « trop beau » n'est audité que si la **preuve** a défini son audit ; un préenregistrement de T0.6, T0.7 ou T0.8 sans clause R4 passe M-0.2 (`prereg.py` ne l'exige pas) et la grille ne le voit pas (point 5).

## Critère 7 — pas de lecture anticipée : **tenu, une réserve mineure**

- Aucun verdict, même partiel, dans la partie gelée ; les états d'avancement ne sont pas cités ; la seule phrase de type « échoueraient M-0.5 » (l. 946-947) est dans l'annexe F, non gelée, retirée au scellement.
- Réserve : le bloc D-G0-3 (l. 491-496) porte un **résultat chiffré** du rejeu des juges de T0.5 (« aucune des six cellules ≥ 0,99 ; 157/180 = 0,87, Wilson 0,82-0,91 »), qualifié « non opposable, motive la décision, n'entre pas dans la règle ». Ce n'est pas une lecture de G0, mais c'est un constat d'état avec chiffres dans un texte destiné au scellement. Point 15.

## Critère 8 — décisions de Lazar (R-750, R-765) : **tenu dans le corps, contredit par l'annexe B**

- Report unique au 31 janvier 2027 : Seuil l. 155-158 (« une seule seconde lecture, finale, … 2027-01-31 à 23:59 UTC … Aucune troisième lecture »), Repli l. 727-728, annexe B l. 859-860 ; fidèle à R-750 (« 31 janvier : go ») et à R-765 (« un seul verdict final »).
- Gel d'un critère échoué pendant le report : section 2 l. 224-233 (D-G0-13 (a) restreint aux négatifs d'une preuve à (α) présent, par liste d'arrêt ou ligne de table gelée, scellés après le premier verdict), champ (γ) l. 138-140, (m4) l. 298-300, Repli l. 749-751. « Échec scellé » lu comme résultat (jamais un manque) : conforme à R-765, à CL2 § 3 et au registre (R-780). La restriction (les négatifs des contrôles de la grille sur le critère 8 ne gèlent pas) est une interprétation, correctement laissée [À DÉCIDER] pour Lazar.
- « Il ne ferme pas la porte en cours de report » : aucune lecture entre les deux (l. 155-158) ; « jamais retenté » : section 2 l. 218-219 et Repli point 4.
- Verdict unique : deux lectures, la seconde finale, cohérent avec « jusqu'au second verdict » de R-765.
- **Mais** l'annexe B l. 852 porte encore le défaut de la v3 pour D-G0-13, dont le (b) que CL2 a montré hors de R-765 ; or c'est la colonne « défaut » de l'annexe B qui s'applique si Lazar ne tranche pas (l. 171-172, l. 834-835). En l'état, le défaut qui s'appliquerait n'est pas celui que le corps décrit. Point 1.

## Corrections demandées

### Bloquant

1. **Annexe B contredit le corps sur deux défauts** (l. 850, l. 852 ; aussi l. 846). Récrire : D-G0-11 défaut **condition** (non tenu — invalide, M-3.2 et M-3.5 ensemble), autre option réserve (CL1 § 6), source « avis Fable grille et CL2 § 4 contre CL1 § 6 » ; D-G0-13 défaut **(a) restreint, (b) règle de D-G0-7 (seul le négatif par liste d'arrêt, (β) = « oui », est gelé au premier verdict), (c)**, autre option = variante v3, source « R-765, CL2 § 3 », en retirant « nouveau (v3) », « à contre-lire en CL2 » et « recommandation de la v3 seule » ; D-G0-7 : ajouter l'exception pendant le report (l. 219-223). Sans cela, la règle l. 171-172 et l. 834-835 fait appliquer, par défaut, des choix que CL2 a rejetés et que le corps ne décrit plus.

### Majeurs

2. **Motif « scellable » de M-0.3** (l. 248) : « n'est pas scellable » et « à corriger avant scellement » sont lus comme « Scellable ». Motif proposé : `(non |pas )?scellable( après corrections)?|à corriger avant scellement`, lecture : première occurrence « Scellable » ou « Scellable après corrections » = conforme ; « non scellable », « pas scellable », « à corriger avant scellement » = non tenu — invalide ; et ajouter en annexe C point 6 la forme exigée d'un rapport de contre-lecture (verdict dans ses dix premières lignes, l'un des trois mots).
3. **Motifs cassés par la typographie du dépôt** (gras `**…** :`, familles de sondes) : M-3.3 l. 416 (« différence de moyennes » → non concluant ; proposé : `sed -E 's/diff(é|e)rence de moyennes//gi' | grep -c -i "moyenne"` = 0, ou motif `agr(é|e)gation[^.]{0,40}moyenne`) ; M-4.4 l. 464 (proposé : `'^[-* ]*agr(é|e)gateur s(é|e)quentiel[* ]*:'`, essayé : rend le chemin avec le gras) ; D-G0-2 (c) l. 385 (proposé : `doses non nulles[* ]*: ?[^;]+;[^;]+`, essayé : 1 avec le gras). Chacun de ces trois faux fait passer une porte « franchie » en « non concluante » sur un préenregistrement correct.
4. **Précédence des sous-états** (Métrique l. 116-124 ; « États » l. 390-391, 425-426, 501-502, 556-557, 579, 621-627) : écrire une règle unique, par exemple « absent, puis invalide, puis non concluant par suspicion R4 (l. 695-696), puis négatif ; les autres « non concluant » cèdent devant tout « non tenu » ; dans un même sous-état, la première ligne de contrôle dans l'ordre de la fiche est citée » ; puis aligner les cascades des fiches sur cette règle (critère 3 : ajouter « invalide » ; F-3.2 et la cascade). Sans cette règle, le lecteur choisit entre sous-états et ce choix décide du gel.
5. **Préenregistrement sans clause R4** (l. 696-697) : ajouter « préenregistrement à (α) présent sans `R4` ni `symétrie` (compte 0) : non concluant pour le critère (ligne citée) », et en annexe C point 6 : « une clause d'audit de symétrie (définition du déclencheur, les deux sens) dans T0.6, T0.7, T0.8 ».
6. **Annexe C point 6 incomplet** (l. 873-879) : ajouter les formes que le corps exige en la citant : prononcé **une seule fois** dans le verdict (F-1.1 l. 328) ; « Doses non nulles : d1 ; d2 [; …] » (l. 385-386) ; « Agrégateur séquentiel : `<chemin du module>` au commit `<sha>` » (l. 464) ; fichiers d'identifiants d'actions, un par ligne, même forme, nommés par les manifestes (F-3.4 l. 422) ; la ligne « Bras principal » porte l'agrégation et sépare les sondes par « ; » (l. 416, 419) ; format de sortie JSON Lines avec les champs `base`, `episode`, `action`, `score` (l. 470-471). Sans ces formes, les auteurs de T0.6 à T0.8 produisent des « non concluant » par construction.

### Mineurs

7. **Annexe F et horodatage hérités de la v3** : l. 908 (commit `9d99f29d`, 11:07-11:16 UTC), l. 916 (« 23 pièces »), l. 979-980 (« Fin de rédaction : 2026-10-29 11:24:45 UTC », antérieure au début de la v4, l. 10 : 11:33 UTC) ; aucune des quatre exécutions que la table l. 45, 48, 50, 51 attribue à l'annexe F n'y figure. Soit consigner ces essais dans l'annexe F de la v4 (commit, heure, comptes : 92/69, 69/69 citées ; 0 négatif, 0 + 4 + 11 doutes ; guillemets ; insécable ; brouillon 5), soit renvoyer la table à cette contre-lecture, qui les reproduit. Corriger la ligne de fin.
8. **Jetons `@L1@` à `@L7@`** non remplacés dans la colonne « ligne v4 » (l. 45-51) : y mettre les lignes de la v4 (par exemple 1 → 122, 138-140, 219-228, 608-610, 624-627, 629-666, 749-751 ; 2 → 222-223, 227-228, 852 ; 3 → 408-409, 415, 418, 430-441, 850 ; 4 → 320-322, 328, 879 ; 5 → 298-300 ; 6 → 379-389, 416, 419, 422, 464, 576 ; 7 → 256-261, 265-274, 296-297).
9. **Script M-8.3, codes de sortie** (l. 630-631, 665) : une exception sort avec le code 1, confondu avec « absent ou négatif ». Entourer le corps d'un `try/except` qui imprime « M-8.3 erreur : … » et sort avec le code 3, et écrire dans la ligne F-8.2 : « sans ligne de synthèse `M-8.3 absents … | F-8.2 negatifs … | F-8.2 doutes …` : non concluant ». Corriger la sortie attendue de F-8.2 (l. 610) pour qu'elle cite la ligne entière.
10. **Annexe B, D-G0-7** (l. 846) : reprendre l'exception pendant le report (l. 219-223), sinon l'index et le corps divergent sur ce point aussi.
11. **M-0.7, apostrophe** (l. 252) : `grep -n -i -E "liste d['’]arr(ê|e)t"`, comme `NEUTRE`.
12. **Annexes C et D stériles** : annexe C point 1 (l. 864) « contre-lecture R2 de cette v3 » → v4 ; annexe D (l. 881-894) est celle de l'auteur de la v3 (l. 883 contredit l. 18-20 ; l. 888-889 cite des empreintes et des lignes d'avant la v4 ; l. 892 « aucun avis ne l'a examinée » est faux depuis CL2) : soit la réécrire au nom de l'auteur de la v4, soit l'intituler « héritée de la v3 » et ajouter les réserves propres à la v4.
13. **Seconde lecture, deux manques** : ajouter à la liste d'arrêt « pour la lecture n° 2, le dossier ne donne pas le verdict scellé de la lecture n° 1 (chemin, empreinte, commit) » ; écrire, section 2 l. 229, que « la pièce qui l'a gelé » est la première par date de commit de son `.sha256` quand plusieurs négatifs existent.
14. **Options manquantes** en annexe B pour D-G0-3, D-G0-6, D-G0-7, D-G0-8 (« — ») : le format de décision exige deux ou trois options ; en écrire une par point (par exemple D-G0-8 : « rapport de fonctionnement de la session suffisant pour 2, 3, 4 »), même pour la rejeter.
15. **Chiffres de T0.5 dans D-G0-3** (l. 491-496) : déplacer le résultat du rejeu des juges dans la note de constat (`docs/notes/porte-g0-grille-v1/constat-etat-preuves-G0-2026-10-29-v1.md`) et ne garder ici que le renvoi ; la grille scellée ne porterait alors aucun résultat.

## Ce que je n'ai pas vérifié

La v3, CL1, l'avis Fable grille, l'avis conv-audit, la synthèse repli hors l. 146-163 et la clause `62cc6fbf…` : non lus. La colonne « ligne v3 » de la table l. 45-51 : non contrôlée. Les brouillons de T0.6 à T0.8, de G1 et du papier C : non lus hors de l'essai F-7.2 sur le brouillon 5. M-0.4 et M-0.6 (dates de commit) : non essayées, clone superficiel. Les comptes « 4 et 11 doutes » par chiffre : reproduits en somme (15), pas chiffre par chiffre (ma table citait des lignes fictives).

Fin de rédaction : voir la ligne suivante (`date -u`).
Fin de rédaction : 2026-10-29 12:16:24 UTC.
