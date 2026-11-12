# Contre-lecture R2 n° 1 — `prereg/brouillon-G0-grille-lecture-v2.md` — v1

- Contre-lecteur : sous-agent neuf (Fable 5.1). Je n'ai écrit ni la v1, ni la v2, ni l'un des deux avis, ni la synthèse du collisionneur, ni aucune preuve lue par la grille. Début 2026-10-29 10:57 UTC, fin : dernière ligne. Commit `ca85f399`. Ni réseau, ni commit, aucun interdit ouvert.
- Objet : v2, `aa47f6fc637b67e4fd2679491f660cda3e79ad99394f4d49f94511c1df42857e` (recalculée). Lus : v1 `320af9b0…`, avis Fable `3c2c8c55…`, avis conv-audit n° 199 (extrait de `refs/canal-local/conv-audit`, empreinte recalculée `0b31ae24…`, égale à la l. 17), synthèse repli `527f5853…`, constat d'état non scellé, brief v2 l. 106-201 (`9261932a…` ; `sha256sums-lancement-v2.txt` OK ; `verifier-arbre` : intact). Les 18 empreintes citées par la v2 que j'ai recalculées sont conformes ; `registres/decisions.md` a bougé (`6898559c…`) : l. 462 = N-027, l. 978 = R-750 (« 31 janvier : go » présent), l. 989 = R-761.

## Verdict

**Scellable après corrections.** Aucun constat bloquant ; sept majeurs (CLG-01 à 07), huit mineurs. Les huit critères sont recopiés mot pour mot (comparés au brief l. 190-201) ; aucune ligne n'en change le texte ; aucune règle n'est taillée sur l'état du 29 octobre (les critères 1 et 5, seuls pourvus, reçoivent les lectures les plus strictes). Les deux avis sont appliqués point par point. L'agrégation est sûre. Les corrections portent sur la mécanique des commandes, les sous-états, le défaut des points à un seul avis et la symétrie R4.

## 1. Fidélité aux critères

Aucun écart hors des points étiquetés. Trois lignes non étiquetées tirent un état d'une décision en vigueur plutôt que du texte du critère, sans le changer ; la source est à nommer dans la colonne « état si échec » : M-3.2 (l. 300, P-015 (b)), M-4.4 (l. 342, brief T0.8), F-7.1 (l. 435, livrable T0.9 et N-005/N-006 l. 97, vérifié). Pour le sous-état de F-7.1, voir CLG-05.

## 2. Application des deux avis

| avis | point | v2 |
|---|---|---|
| Fable § 1 | fausse citation critère 5 ; P4-instrument ; TRACE-lite et règle du coût ; F-2.3 sous D-G0-2 ; F-3.1 Bonferroni ; HC2b justifiée ; critère 8, deux pièces créées ; garde P-007 dans T0.6-T0.8 | l. 37, 368-390 (D-G0-10) ; 303, 315-318 (D-G0-11) ; 343-344, 357-360 (D-G0-12) ; 262-272 ; 304 (P3 l. 274-275 vérifié) ; 435 ; 455-458 ; 228-234 |
| Fable § 2, points 1-7 | version non autorisée ; M-0.4 et clone complet ; F-6.1 mécanique ; `C_lecture` ; lecture tardive ; sept jours ; ligne citée | l. 176-183 ; 40, 160-163, 197, 519 ; 407 ; 130-132 ; 133-135, 526 ; 507-508 ; 107 |
| Fable § 3 | D-G0-1 à 9 | annexe B, chacune reprise |
| Fable § 4, points 1-8 | listes de contrôle ; dossier ; clone ; script ; repli ; citations ; annexe A séparée ; M-0.2 sur la grille, gabarit | l. 192-200 et fiches ; 155-157 ; 160 ; 465 ; 529-553 ; 26-28 ; 46 ; 142-144, annexe A |
| conv-audit 3 (a) (b) (c) | mot de Lazar seul ; D-G0 tous tranchés ; cause nommée | l. 126-128, 520 ; 138-141 ; 176-180 |
| conv-audit 4 | D-G0-2 chiffré ; D-G0-3 part avant lecture ; D-G0-4 liste ; D-G0-6 ; D-G0-9 | l. 268 ; 349 ; 413-415 ; 153 ; 473-474 |
| conv-audit 5 | « 0,99 » ; `d5ac34db` | l. 44, 351-356 (vérifié, l. 10-18) ; annexe D |

Aucun refus. Imprécision sans effet : CLG-15.

## 3. Mécanique, exécutée au commit `ca85f399`

- **Clone** : `git rev-parse --is-shallow-repository` = `true` (243 commits). M-0.4 y échoue : `git log -- prereg/T0.4-validation-modele-reel-v3.md.sha256 | tail -1` rend `43bd450d` (2026-10-27) ; `merge-base --is-ancestor 43bd450d ce54afd5` rend 1. L'exigence du clone complet (l. 160-163, 519) est nécessaire ; l'état (arrêt) est sans ambiguïté.
- **M-0.1** : OK sur verdict T0.4 v3, préenregistrements T0.4 v3 et T0.3, lecture T0.3 (.md, .json), manifeste et grille T0.3, deux contre-lectures T0.4 v3 ; 171 PDF de `docs/sources/pdf/` ont un compagnon.
- **M-0.2** : empreintes rendues pour T0.4 v3 et T0.3. Sur la v2 : `GardeArret` « Contre-lecture sans les deux empreintes », seul manque ; les huit sections exigées sont reconnues (les `##` du gabarit de l'annexe A deviennent des sections : sans effet).
- **M-0.3** : sur les cinq rapports existants (T0.4 v3 × 2, T0.3 × 3), la neutralité s'écrit « Je n'ai écrit ni … » : `n'ai pas écrit` ne la trouve jamais ; `neuf` la trouve, et trouve aussi « neuf scénarios » (CL1 l. 206). `scellable` : trouvé partout. Traitement des remarques : section « Contre-lecture » de T0.4 v3 conforme.
- **M-0.4** : manifeste du run A : `preenregistrement` = `{chemin, sha256 4f711cd3…}`, `cree_le` 2026-10-06T11:40:27, `commit` `ce54afd5…` : les clés existent.
- **M-0.5, F-1.x** sur le verdict T0.4 v3 : empreinte l. 4 et 29 ; neutralité l. 3 (par `auteur ni`) ; « Critère 1 de G0 : prouvé » l. 11 ; les trois composantes l. 11, section « 1. Verdict » ; « Réserves au sens de la table : aucune » l. 13. Le motif F-1.1 ne peut pas rendre la branche « non prouvé » (CLG-04).
- **M-0.7** : `sections()` existe ; `bool(s.get('Liste d\'arrêt'))` = `True` sur T0.4 v3 ; `grep -i "liste d'arrêt"` sur le verdict : 0 ligne → (β) « absent » ou « sans objet », la grille ne dit pas lequel (CLG-12).
- **M-2.2** : `grep -n "critère 2" prereg/P3-premier-test-i-a-v1.md` rend l. 122 seulement ; **la l. 431, citée comme modèle, écrit « critères 2 et 3 de G0 » et n'est pas trouvée** (CLG-03).
- **M-5.2** : rend `7474743a…`, `d73ac469…`, `True` ; `grille_sha256` = `5609f920…`. **M-5.3** : run cité l. 1 de `lecture.md`. **F-5.1** : le `...` écrit comme `collections.Counter(p['verdict'] for p in d['resultat']['lecture']['predictions'].values())` rend `{'confirmée': 31}`. **F-5.2** : `grep -i audit` rend l. 5 (en-tête) et l. 39 « déclenché : False ». **F-5.3** : R-025 (l. 34) dit « Réserve écrite : vérifications de l'instrument en majorité » ; la phrase entre guillemets l. 384 n'y figure pas (CLG-13).
- **F-6.1, F-7.0** : premières lignes des brouillons 3 (G1) et 5 (papier C) conformes ; `ls prereg/G1-*`, `prereg/papier-C-*`, `docs/verdicts/verdict-P4-instrument-*` : rien (état, pas lecture). **M-8.2** : 34 lignes sur le niveau 1.
- Sources citées par les fiches (P-007, P-011, P-015, N-005/N-006, N-029, N-026, brief T0.7, P3) : lignes conformes.

## 4. Latitudes

Aucune issue de porte n'est à la main du lecteur. Restent des jugements de fiche (F-2.2, M-3.4, F-3.3, F-8.2) fermés par la règle l. 158-159 (→ non concluant) ; à rendre mécaniques (CLG-10). « Le même audit qu'un négatif trop propre » (l. 508) n'est défini nulle part (CLG-06). « Rapportée en réserve si le lecteur la rencontre » (l. 157-158) est un hasard, pas une règle (CLG-01).

## 5. Compatibilité avec la clause recommandée

Compatible : sous-états (l. 101-107), champs (α) et (β) (l. 113-115), même suite pour « non franchie » et « non concluante » (l. 488-492), aucune version après un négatif par liste d'arrêt (l. 180-182), même grille à la seconde lecture (l. 549-550). Pour Lazar, hors défaut de la grille : (1) le point commun 3 du collisionneur (« réfuté par résultat scellé, jamais retenté ») est plus large que la clause (a) et que D-G0-7, qui ne ferment qu'après un négatif par liste d'arrêt (choix 1) ; (2) la clause (b) requalifie « absent » en « négatif » : la grille le permet sans rien décider, à condition que son propre mot « négatif » ne couvre que des résultats (CLG-05).

## 6. Points D-G0-1 à 12

Tous étiquetés dans le corps et indexés en annexe B ; aucun « à décider » sans numéro. D-G0-1 à 9 ont une option commune, donc un défaut au 15 novembre ; **D-G0-10, 11, 12 n'en ont pas** (l. 608-609) : si Lazar se tait, la grille est non scellable par construction (CLG-02). D-G0-1, qui fixe la règle du défaut, ne peut pas s'appliquer à elle-même : à trancher explicitement.

- **D-G0-10** : oui à l'option Fable — aucune « réfutée », toutes « confirmée », audit R4 `déclenché : False` ou scellé ; commande de comptage écrite dans F-5.1 ; confiance élevée.
- **D-G0-11** : **réserve** — le critère dit « au-dessus du plancher » ; un témoin positif n'infirme pas une sonde au-dessus, il n'éclaire qu'un nul ; l'ordre de P-015 (b) se contrôle dans le préenregistrement de T0.7 (citation de P-015 exigée en M-0) et son absence est un écart signalé ; confiance moyenne.
- **D-G0-12** : **réserve** (Fable) — N-029, décision de Lazar postérieure au brief T0.8, fixe « ce que la base contient » sans TRACE-lite ; l'exiger ajouterait une base que la route décidée n'a pas retenue ; confiance élevée.

## 7. Symétrie R4

Asymétrique : l. 509 ne traite que le « trop beau » (→ non concluant sans audit) ; un négatif trop propre sans audit reste « non tenu — négatif », définitif sous la clause (a) s'il vient d'une liste d'arrêt. La Métrique l. 107 ne rétablit la symétrie que si la table de la preuve prévoit l'audit dans les deux sens. Correction : CLG-06.

## Constats

| n° | gravité | ligne | constat | correction proposée |
|---|---|---|---|---|
| CLG-01 | majeur | 155-158 | le dossier est écrit par la session ; rien ne vérifie qu'il est complet ; une version négative omise ne serait vue que par hasard | M-0.8 : `ls prereg/<préfixe>-*-v*.md docs/verdicts/*<préfixe>*` par critère (préfixes gelés dans la grille : T0.4, T0.6, T0.7, T0.8, T0.3, G1, papier-C, P4-instrument, état de l'art) comparé au dossier ; pièce scellée absente du dossier → « non concluant » (pièces concurrentes, l. 184) |
| CLG-02 | majeur | 608-609, 622-624 | D-G0-10 à 12 sans défaut | un défaut par point (§ 6), soumis avec D-G0-1 |
| CLG-03 | majeur | 256 | `critère 2` ne trouve pas « critères 2 et 3 » (P3 l. 431) | `grep -n -i "crit[èe]res\? 2\b"` ; même précaution pour « critère 1 » et « (i) » / « (ii) » |
| CLG-04 | majeur | 222 | `Critère 1 de G0 : prouvé` ne peut rendre ni « non prouvé » ni « non concluant » | `grep -n "Critère 1 de G0 :"` puis le mot qui suit ; 0 ligne → non tenu — absent |
| CLG-05 | majeur | 435, 464, 466 | « non tenu — négatif » pour des manques (hypothèse absente, priorité ou cellule sans statut) alors que l. 105 réserve « négatif » à une lecture gelée négative ; le repli en dépend | F-7.1, M-8.2, F-8.1 → « non tenu — invalide » ; garder « négatif » pour M-8.3, F-8.2, F-8.3 (conclusions d'un contrôle scellé) |
| CLG-06 | majeur | 507-509 | R4 : « trop beau » seul ; « même audit » indéfini | l. 509 : « résultat suspect de propreté au sens de sa propre table, positif ou négatif, sans audit scellé : non concluant » ; l. 508 : « réserve « preuve récente » ; aucun audit par le lecteur ; signalé pour audit R4 après lecture » |
| CLG-07 | majeur | 196, 198 | neutralité : `n'ai pas écrit` ne trouve aucune pièce existante ; `neuf` trouve des nombres | `head -5 <rapport> \| grep -i "sous-agent neuf\|contre-lecteur neuf\|n'ai \(pas \)\?écrit\|ne suis l'auteur\|auteur ni"` |
| CLG-08 | mineur | 341, 382 | commandes en `...` | les écrire ; F-5.1 : `python -c "import json,collections;d=json.load(open('<lecture.json>'));print(collections.Counter(p['verdict'] for p in d['resultat']['lecture']['predictions'].values()))"` |
| CLG-09 | mineur | 383 | « non déclenché » demande d'interpréter « déclenché : False » | `grep -n "déclenché : False" <lecture.md>` |
| CLG-10 | mineur | 258, 302, 306, 467 | jugements résiduels | F-2.2 : « vérité terrain » dans la section « Métrique » (`sections()`) ; M-3.4 : motifs `covariance`, `même agrégation`, `mêmes actions` ; F-3.3 : nom de la sonde du verdict `grep` dans la liste du préenregistrement ; F-8.2 : « l'article imprime » sur la même ligne |
| CLG-11 | mineur | 435 | `grep "HC2"` trouve HC2b | `grep -n "HC2\b"` |
| CLG-12 | mineur | 200 | (β) « absent » ou « sans objet » ? | « sans objet » si (α) absent ou critère sans run ; « absent » si (α) présent et verdict muet |
| CLG-13 | mineur | 384 | citation de R-025 inexacte | recopier « Réserve écrite : vérifications de l'instrument en majorité » |
| CLG-14 | mineur | 477-478 | périmètre du critère 8 « gelé avec la grille » mais « annexe du dossier » (écrit après) | en annexe de la grille scellée, ou fichier scellé avant le 15 novembre cité par empreinte |
| CLG-15 | mineur | 126, 49, 499 | « lecture unique » lisible contre la seconde lecture du repli ; l'identité de suite est attribuée à l'avis Fable sur la grille, qui la juge seulement « sûre » (§ 2) | « unique pour l'échéance du 30 novembre » ; citer l'avis Fable sur le repli |

Non vérifié : clause de conv-audit `62cc6fbf…` ; contre-lectures de T0.3 et T0.4 au-delà des lignes citées ; brouillons au-delà de leur première ligne.

Fin de rédaction : voir la ligne suivante (`date -u`).
Fin de rédaction : 2026-10-29 11:06:30 UTC.
