# Contre-lecture R2 n° 5 — `prereg/brouillon-G0-grille-lecture-v6.md` — v1

- Contre-lecteur : sous-agent neuf ; je n'ai écrit ni la grille (v1 à v6), ni ses contre-lectures (CL1 à CL4), ni aucune des preuves qu'elle lit. Modèle : Claude Sonnet 5.5 (identifiant `claude-sonnet-5-5`), lancé par la session principale du dépôt.
- Début 2026-10-29 22:46:37 UTC (`date -u`) ; fin : dernière ligne. Commandes sous `LC_ALL=C.UTF-8` (`locale -a | grep -i -c -E "^c\.utf-?8$"` = 1), GNU grep 3.11, Python 3.13. Lecture et essais seulement : aucun fichier du dépôt modifié hors ce rapport, aucun commit. Essais synthétiques sous `/tmp/claude-0/-home-user/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad/cl5/` (hors dépôt, non scellés).
- **Réserve de famille** : l'auteur de la v6 est un Opus de la même famille que moi (Claude) ; le contre-lecteur d'une autre famille prévu (Fable 5.1) a atteint sa limite d'usage. Je suis un autre modèle que l'auteur, mais j'ai été lancé par la session principale du dépôt, donc très probablement de la lignée « session-depot » : l'exigence « autre modèle **et** autre lignée » de la v6 (l. 1019-1024) n'est donc remplie qu'à moitié ; voir CL5-15. J'ai lu d'autant plus durement.
- Fichiers interdits (`prereg/P3-consignes-v1.md`, `donnees/`, `diag/*/traces`, branches `donnees/*`, `quarantaine/*`, `canal/*`, toute « carte des hypothèses ») : jamais ouverts. La table de dépendance et le mémo de conv-audit que cite la v6 (l. 24-28) vivent sur une branche `canal/*` : je n'ai pas pu les lire.

**Scellable après corrections.** Aucun bloquant, quatre majeurs, onze mineurs. Les dix-huit constats de CL4 sont tous portés dans le texte, aux lignes annoncées, mais le « négatif gelant » garde trois trous qui laissent encore masquer ou durcir un gel sans passer par Lazar (CL5-01 à CL5-03), et une clause R4 non traitée durcit les critères 6 et 7 (CL5-04).

## Empreintes vérifiées (`sha256sum`, depuis le dossier du fichier pour les compagnons)

| fichier | empreinte | compagnon |
|---|---|---|
| `prereg/brouillon-G0-grille-lecture-v6.md` (objet) | `33a41c58e7aa7dd1e179fd77aa305243993d1c3ed2a3e6dcd64b78b4072ac1aa` | `sha256sum -c` : OK |
| `prereg/brouillon-G0-grille-lecture-v5.md` | `c073e26aa9e3ac8b1a9fb2fde786133093ec6dc2137d47a880ffdd49e53137e2` | OK |
| `prereg/contre-lectures/brouillon-G0-grille-lecture-v5-cl4.md` | `01718af162853cd52e5094bb4130a3fc2da963ed4c6b8f62b38b4482a45a888f` | OK (égale à celle que cite la v6, l. 23) |
| `docs/brief-claude-code-programme-complet-v2.md` (l. 190-201) | `9261932a11f29e8643175bc6e150d5455067f58a3cb1e57dca99e02cb17aa3b2` | `cd docs && sha256sum -c sha256sums-lancement-v2.txt` : trois OK |
| `registres/decisions.md` (vivant ; l. 978 R-750, l. 993 R-765, l. 1020 R-792) | `4074a4b8294657085e5615039343f5af108a3cccbcb5de062139e99d390785af` | fichier vivant, sans compagnon |
| `src/controle_ia/prereg.py` | `3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306` | — |

`diff <(sed -n '190,201p' brief) <(sed -n '179,190p' v6 | sed 's/^> \{0,1\}//')` : aucune différence, les huit critères sont mot pour mot ceux du brief. Les lignes R-750, R-765, R-792 lues par `grep -n "^| R-… "` : citations de la v6 conformes (R-792 dit les dix-huit constats appliqués, aucun refusé, D-G0-14 et DIV-1 à DIV-4 ouverts).

## Ce qui est vérifié et tient

- **Table « Ce que la v6 corrige »** : les dix-huit lignes (B1, M1 à M6, m1 à m11) renvoient à des lignes v6 qui portent bien le changement annoncé (vérifiées une à une, table ci-dessous). `diff v5 v6 | grep -E '^[0-9]'` : aucun bloc de changement hors ces dix-huit points, la mise à jour de « D-G0-13 » en « D-G0-14 » (l. 303, 305, 1072, 1074, 1116) et les en-têtes ; sauf une mise à jour oubliée (CL5-13).
- **Tables Markdown (M1)** : script de compte des cellules (blocs de code exclus, `\|` retiré, chaque ligne comparée à l'en-tête de sa table) : v6 → 154 lignes de table, 0 au mauvais compte ; v5 → `296 : 7 cellules pour 5 ; 300 : 6 pour 5 ; 464 : 6 pour 5` (les trois lignes de CL4). Le symbole `|` est échappé dans les cellules modifiées (l. 400, 404, 577).
- **Annexe G, M-0.3** : les quatorze lignes essayées sont reproduites (par exemple `T0.4-rapport-contre-lecture-3-v1.md` l. 294 → « Non scellable », neg=1 ; l. 296 → « À corriger avant le scellement » ; l. 167 → « scellable » ; `T0.3-rapport-contre-lecture-1-v1.md` l. 29 → « Scellable après corrections », neg=0, imprévu=0 ; CL3 l. 20 et CL4 l. 9 → « À corriger avant scellement »).
- **Script M-8.3** : extrait tel quel du fichier ; sain → code 0 ; document absent, colonne `statut` absente, en-tête avec BOM, ligne vide, valeur hors en-tête, `statut` « Confirmé » → code 3 sans ligne imprimée avant l'erreur ; absent de sa ligne → code 1 ; introuvable avec « l'article imprime » → conforme. Les quatre cas « non tenus » de CL4 rendent maintenant 3.
- **D-G0-2 (c)** : le motif de CL4 rend 0 sur « Doses non nulles : 1,5 ; 3 » (essayé) ; `DOSE` rend 1 ; « 0,1 ; 0 », « 0,1 ; 0,0 », « 0,1 et 0,3 », « 0,1 ; voir la section Métrique » rendent 0.

## Table « constat CL4 → corrigé → ligne v6 »

| constat CL4 | corrigé ? | ligne v6 (vérifiée) | résidu |
|---|---|---|---|
| **B1** négatif gelant, précédence, section 2 | **oui, avec trous** | 215-253 (Métrique), 272-274 (δ), 354-379 (section 2), 955-961, 1092-1093 | CL5-01, CL5-02, CL5-03, CL5-05, CL5-10, CL5-11, CL5-12 |
| **M1** `\|` non échappés | oui | 400, 404, 577 | — |
| **M2** M-0.3, faux « conforme » sur citation | oui, motif à angles morts | 326-328, 387-391, 400, 1148-1151 | CL5-06, CL5-07 |
| **M3** « bras principal » non ancré | oui | 568-571, 577, 580, 582 | CL5-08 (mot « attention ») |
| **M4** validation du script M-8.3 | oui | 798-866 | CL5-09 (espaces) |
| **M5** clause R4 « absente » durcit 6 et 7 | oui pour cette clause ; la clause jumelle « contient » reste non restreinte | 898-902 | **CL5-04** |
| **M6** (β) lu par jugement | oui | 264-268, 392-394, 404, 1144-1147 | **CL5-02** (effets) |
| m1 ligne du point 8 | oui | 106 | — |
| m2 sortie partielle | oui | 775, 802-804, 859-865 | — |
| m3 D-G0-2 (c), une seule dose | oui (écart justifié) | 537-541 | CL5-08 (espace insécable) |
| m4 cascades 2, 3, 4, 8 | oui | 545-549, 586-593, 665-669, 788-796 | CL5-12 |
| m5 annexe B, D-G0-13 | oui | 1092 | — |
| m6 options marquées | oui | 1082, 1085, 1086, 1087 | — |
| m7 départage par ascendance | oui | 368-372, 1092 | — |
| m8 « la dernière » / « tel quel » | oui | 44, 1179 | — |
| m9 gras résiduel de M-4.4 | oui (essayé : `sed` rend le chemin sur sept formes) | 631 | — |
| m10 pluriel de M-0.7 | oui (« Listes d'arrêt déclenchées : non » prise) | 392-394, 404 | — |
| m11 contre-lecteur d'un autre modèle | oui dans le texte (exigence écrite) ; **non remplie par le présent rapport** | 1019-1031 | CL5-15 |

Aucune correction annoncée n'est absente du texte. Aucun constat de CL4 n'est resté sans correction ; les résidus ci-dessus sont des défauts nouveaux ou des défauts de l'application.

## Constats

### CL5-01 — majeur — un « non concluant » de M-0.3 retire-t-il le caractère gelant ? (B1, cas 5)

Lignes v6 : 218-220, 213, 242-244, 400.
Défaut : la condition (2) du négatif gelant exige « P passe M-0.1 à M-0.6 ». M-0.3 a désormais trois issues (conforme, « invalide », « non concluant » pour forme imprévue, ligne non désignée ou `<l>` > 10). Le texte ne dit pas si un « non concluant » de M-0.3 est un « passe ». Lu à la lettre, il ne l'est pas : un négatif par liste d'arrêt, dont la preuve est par ailleurs intègre, perd son caractère gelant à cause de la **typographie de la ligne de verdict du rapport de contre-lecture**, qu'il ne contrôle pas. C'est le mécanisme que B1 cas 5 décrivait (un défaut de forme masque un négatif) : la v6 a changé « invalide » en « non concluant » pour M-0.3, mais la condition (2) laisse le défaut intact. La fiche ne dit rien non plus de F-1.1 : « forme imprévue » du prononcé n'est pas un négatif prononcé (condition (4)).
Essai : `IMPREVU_CL` et `VERDICT_CL` appliqués à `Scellable : non` → imprévu = 1 (non concluant) ; le négatif qui en dépendrait n'est plus gelant selon la lettre de (2).
Correction : écrire (2) en termes d'états : « P ne rend « absent » ni « invalide » à M-0.1 à M-0.6 et aucune ligne de la fiche ne la rend « invalide » ; un « non concluant » de M-0.3 ou de F-1.1 ne retire pas le caractère gelant : il est rapporté en réserve, avec la ligne citée » (ou l'inverse, mais l'écrire) ; en faire un point de D-G0-14 (a).

### CL5-02 — majeur — (β) « absent » dissout silencieusement le gel par liste d'arrêt (B1, cas 1-2 ; M6)

Lignes v6 : 222, 264-268, 404, 1144-1147, 224-225.
Défaut : le « négatif gelant par liste d'arrêt » exige (β) = « oui », lu **uniquement** par la ligne de forme ancrée `ARRET_BETA` (`$` en fin de ligne). Une omission ou une annotation du rédacteur du verdict n'a « aucun effet sur l'état » (l. 404) mais fait basculer (β) en « absent », donc le négatif en « table » (si une ligne de table le porte) ou en négatif de sorte indéterminée (si le seul fondement est la liste d'arrêt). R-765 (« jamais retenté ») perd alors son objet sans qu'aucune règle écrite le dise.
Essais (`grep -c -i -E "$ARRET_BETA"`) :
- 1 : « Liste d'arrêt déclenchée : oui », « - **Liste d'arrêt déclenchée** : non », « Liste d'arrêt déclenchée : Oui. », « Liste d'arrêt déclenchée: non » ;
- **0** : « Liste d'arrêt déclenchée : oui (condition 2) », « … : oui — condition 2 », « … : oui, condition 2 », « … : non (aucun arrêt) », « > Liste … : oui », « 1. Liste … : oui », « Liste d'arrêt déclenchée (condition 3) : oui », une ligne terminée par une tabulation, une ligne en fin `\r\n`, et « Liste d'arrêt déclenchée : oui » (espace insécable avant les deux-points, typographie française) ;
- sur `docs/verdicts/*.md` : 11 fichiers, **0** ligne de forme dans chacun (comptes seulement) : aujourd'hui, aucun verdict scellé ne peut porter un négatif gelant par liste d'arrêt, le critère 5 non plus (`lecture.md` est produit par du code gelé).
Cas voisin non écrit : (β) = « oui » (la liste d'arrêt a joué et « conclut négativement », l. 1146-1147) avec un prononcé non négatif, ou de forme imprévue : (4) n'est pas satisfaite, rien n'est dit.
Correction : (i) pour un verdict qui prononce un négatif, à (α) « présent » et (β) « absent » : sous-état « non concluant » (forme imprévue, ligne citée), (δ) = « indéterminé » rapporté, et le cas porté à Lazar dans D-G0-14 ; (ii) même traitement de (β) = « oui » sans prononcé négatif ; (iii) soit lire (β) comme les pointeurs R4 (le dossier désigne la ligne, le lecteur la contrôle), ce qui permet de lire les verdicts déjà scellés ; soit tolérer une annotation en fin de ligne (`(oui|non)([^a-zé]|$)`) et remplacer l'espace insécable par `[  ]` ; (iv) écrire noir sur blanc que, pour les verdicts scellés avant la grille, la branche « liste d'arrêt » est inatteignable.

### CL5-03 — majeur — négatif par table suspect de propreté : durcissement non porté à Lazar (B1, cas 1)

Lignes v6 : 224-225, 231-234, 213, 242-243, 1093.
Défaut : D-G0-14 (c) règle le seul négatif **par liste d'arrêt** avec audit R4 sans rapport scellé (défaut : gelant). Pour le négatif **par table**, les conditions (1) à (4) ne mentionnent pas R4. Lu à la lettre, un négatif par table suspect de propreté, sans audit scellé, est donc un négatif gelant par table, qui gèle le critère pendant le report (D-G0-13 (a)), alors que son sous-état rapporté est « non concluant » par R4 (rang 3). La v5 ne gelait pas ce cas (« non concluant », pas de gel) ; la v6 le durcit sans le dire et sans option pour Lazar. C'est exactement ce que CL4 reprochait à la précédence de la v5, dans l'autre sens.
Correction : ajouter un point D-G0-14 (d) : « négatif par table avec audit R4 sans rapport scellé ». Recommandation : défaut = non gelant tant que l'audit n'est pas scellé (R-765 ne dit « jamais retenté » que pour la liste d'arrêt ; un gel est irréversible dans la grille scellée), autre option = gelant comme (c) ; confiance faible (0,4) ; et écrire la condition dans (4).

### CL5-04 — majeur — la clause « contient R4 ou symétrie » durcit les critères 6 et 7 (cas du bloc M5)

Lignes v6 : 896-897 (clause non restreinte), 898-902 (clause restreinte), 900-902 (l'affirmation « elle ne durcit ni le critère 6 ni le critère 7 »).
Défaut : CL4 M5 a fait restreindre la clause « R4 absente » aux preuves à run. La clause jumelle, juste avant, ne l'est pas : « Préenregistrement qui contient `R4` ou `symétrie` … sans les deux lignes désignées au dossier : non concluant ». Or les préenregistrements de G1 et du papier C contiennent ces mots et n'ont aucun verdict (donc aucune « ligne du verdict qui dit l'audit déclenché ou non », section 1 (b)) : la clause est inapplicable et rend « non concluant » les critères 6 et 7, ce que la phrase l. 900-902 prétend éviter. L'affirmation de non-durcissement est fausse pour cette clause.
Essai : `grep -c -i -E 'R4|symétrie'` → `brouillons/G1-preenregistrement-v1-brouillon3.md` 3 lignes ; `brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md` 6 lignes ; `prereg/gabarit-preregistrement-v1.md` 1 ligne (tout préenregistrement bâti sur le gabarit en contient). Brouillons seulement, non scellés : essai de motif, pas lecture de G0.
Correction : restreindre aussi la première clause (et la phrase « Audit déclenché … sans rapport scellé » si elle vise un verdict) aux preuves à run, critères 1 à 5, comme l. 898-899 ; réécrire l. 900-902 pour couvrir les deux clauses.

### CL5-05 — mineur — (β) et (δ) sont par preuve, les critères 2 et 3 sont par famille

Lignes v6 : 264-268, 222-225, 507-508 (« un seul préenregistrement couvrant (i) et (ii) est recevable »).
Défaut : la ligne de forme est unique par verdict (« une seule ligne », une seule valeur distincte). Dans une preuve qui couvre (i) et (ii), « oui » peut venir de la liste d'arrêt jouée sur (ii) alors que le négatif est celui d'une ligne de table de (i) : « ce négatif vient de la liste d'arrêt » (l. 221-222) ne peut pas être lu. Sur-gel possible (un négatif par table traité en négatif par liste d'arrêt, donc gelé au premier verdict).
Correction : une ligne de forme par famille quand le critère est par famille (« Liste d'arrêt déclenchée (i) : oui »), ou (β) « absent » pour les preuves à plusieurs familles et un seul « oui ».

### CL5-06 — mineur — M-0.3 : angles morts de `VERDICT_CL` et `IMPREVU_CL`, du côté « conforme »

Lignes v6 : 387-391, 400.
Essais (`grep -o -i -E "$VERDICT_CL" | head -1`, `grep -c -i -E "$NEG_CL"`, `grep -c -i -E "$IMPREVU_CL"`) :
- **faux « conforme »** (première forme = « scellable », neg = 0, imprévu = 0) : « Non encore scellable. », « Pas du tout scellable en l'état. », « Le texte ne peut pas être scellable tel quel. », « Jamais scellable. », « Verdict : le brouillon est loin d'être scellable. » ; une négation non contiguë à « scellable » n'est vue ni par `VERDICT_CL` ni par `IMPREVU_CL` (qui ne regarde qu'après) ;
- **faux « conforme »** par le point : « 1. Verdict global : scellable sauf B1. », « Verdict sur `prereg/brouillon-G0-grille-lecture-v6.md` : scellable sous réserve des corrections. », « Scellable (v6.md) sauf B1 » rendent imprévu = 0, parce que `^[^.]*` et `[^.]{0,40}` s'arrêtent au premier point (numérotation, nom de fichier) ;
- **faux « conforme »** par le vocabulaire : « Scellable si D-G0-14 est tranché. », « Scellable à condition de corriger B1. », « Scellable mais avec un bloquant (B1). », « Scellable en l'état, toutefois un majeur reste ouvert. », « Scellable après corrections : à corriger avant scellement. » ;
- **faux « non concluant »** : « Scellable après corrections ; pas de bloquant, trois majeurs. » (imprévu = 1 sur « pas ») ;
- **trou de la commande** : sur une ligne sans aucune forme, `… | head -1 | grep -c -i -E "NEG_CL"` rend 0, comme pour « Scellable » : la ligne « aucune forme → non concluant » n'est tenue que si le lecteur regarde la forme avant de lire le compte.
Correction : tester d'abord que la forme n'est pas vide (`… | head -1 | grep -c .` = 1) ; ajouter à `IMPREVU_CL` une négation **avant** la forme, `(\bnon\b|\bpas\b|\bjamais\b|\bni\b)[^.]{0,30}scellable`, et les mots `si|condition|mais|toutefois|cependant` après ; remplacer `[^.]` par `[^.;]` après avoir retiré les noms de fichier (`sed -E 's/[A-Za-z0-9_\/-]+\.[a-z]{2,4}//g'`) ou exiger que la ligne **commence** par la forme (`^[*# -]*(forme)`), ce que l'annexe C exige déjà mais que le motif ne vérifie pas.

### CL5-07 — mineur — M-0.3 : la ligne de verdict est désignée par le dossier, sans contre-contrôle ; « scellé après la grille » n'a pas de commande

Lignes v6 : 326-328, 400, 1307-1309 (annexe G : « rend conforme si on la désigne »).
Défaut : le dossier est écrit par la session, qui peut désigner une ligne favorable (la l. 167 de `T0.4-rapport-contre-lecture-3-v1.md` rend « conforme », essayé). La protection est la recopie dans le verdict, c'est-à-dire un contrôle humain ; aucun contrôle mécanique ne signale qu'une autre ligne du même rapport **commence** par une forme négative (ici l. 294 et 296). Et la limite `<l>` ≤ 10 vaut « pour un rapport scellé après la grille » sans qu'une commande dise comment le savoir.
Correction : ajouter `grep -n -i -E '^[*# -]*(non[- ]scellable|pas (encore )?scellable|à corriger avant)' <rapport>` : toute ligne qui commence par une forme de `NEG_CL` hors de la ligne désignée est rapportée, et rend « non concluant » si la ligne désignée est conforme ; pour « scellé après la grille », `git merge-base --is-ancestor <commit de la grille scellée> <commit du .sha256 du rapport>` (code 0).

### CL5-08 — mineur — autres motifs modifiés : faux positifs et faux négatifs résiduels

- **`BRAS_P`, M-3.3, F-3.3** (l. 568-582) : faux « conforme » : « Bras principal : sonde générique, sans agrégation, attention à la dérive » rend premier compte 1 (le mot courant « attention » est pris pour l'agrégation), second 0, `;` = 0 (essayé). Faux « non concluant » : « Bras principal : agrégation maximum » (premier compte 0), « Bras principal (gelé d'avance) : … » (ligne de forme = 0), « 1. Bras principal : … » (0). Correction : exiger `(agr(é|e)gation|pooling) (max|attention)\b`.
- **`DOSE`, D-G0-2 (c)** (l. 537-541) : faux « présent » : « Doses non nulles : 0,1 ; 3 fois » (1). Faux « absent » : espace insécable ou insécable fine avant le point-virgule (« 0,1 ; 0,3 » → 0), typographie française courante ; « 0.1 ; 0.3 » → 0 (voulu, virgule exigée). Correction : ` ?` → `[   ]?` ; accepté en l'état pour le reste. L'élargissement de CL4 aux doses ≥ 1 est justifié (voir section « Les trois écarts »).
- **`ARRET_BETA`** : faux « absent » par une double ligne légitime (un verdict qui recopie les deux formes du gabarit) → deux valeurs distinctes (`non oui`, essayé), (β) « absent ». Voir CL5-02 pour les annotations.
- **M-4.4** (l. 631) : tenu ; essayé sur sept formes, dont « **Agrégateur séquentiel :** `…` », « Agrégateur séquentiel: », chemin avec « : » dans un span de code.

### CL5-09 — mineur — script M-8.3 : espaces valides au contrôle, fautifs à l'emploi

Lignes v6 : 827-833, 842-858.
Défaut : la validation utilise `.strip()` pour juger une cellule non vide, mais `chiffre_ecrit`, `source` et `document` sont ensuite employés non nettoyés. Une cellule `0,55␠` (espace final) passe la validation, puis le motif exige un espace après le chiffre.
Essai : ligne `Valeur 0,55.` ; table `c1  s  "0,55 "  docs/doc2.md  1  confirmé` → `M-8.3 absent de sa ligne c1 docs/doc2.md 1`, code **1** (un « négatif du critère 8 » pour un espace) ; sans l'espace → code 0. Cellule `document` = « ␠docs/doc2.md » → code 3 (conservateur). Le `statut` « Confirmé » est refusé (code 3), conservateur aussi.
Correction : `r = {k: (v or "").strip() for k, v in r.items() if k is not None}` après la validation, ou refuser toute cellule dont `strip()` diffère de la valeur (code 3).

### CL5-10 — mineur — D-G0-14 : format de décision et voie de dérogation

Lignes v6 : 1093, 232-234, 1086, 1102-1103.
Défauts : (i) la ligne n'a ni « enjeu » ni 2 ou 3 options pour chaque sous-point (CLAUDE.md, « Format de décision ») : (a) n'a qu'une option écartée d'avance (« à rejeter »), (b) n'en a aucune ; (ii) l'écart (a) de la v6 aux propositions de CL4 (un négatif par liste d'arrêt reste gelant malgré une pièce concurrente) n'est dit que dans la section « Contre-lecture » (l. 1009-1011) : l'annexe B, que Lazar lit, ne l'offre pas comme option alors qu'il fixe le gel en présence de pièces concurrentes ; (iii) (c) dit qu'un audit qui nomme un défaut d'instrument « est porté à Lazar (nœud) » : mais la grille scellée est gelée (R12), et la règle de version (l. 354-361) déclare toute version suivante non recevable « même autorisée » ; aucune voie écrite ne permet à la décision de Lazar d'avoir un effet sur la lecture, sinon une nouvelle version de la grille avant l'ouverture ; (iv) le délai n'est pas dit (le défaut d'échéance de la grille est le 2026-11-15 après mot sur D-G0-1 ; CLAUDE.md parle de 48 heures).
Correction : (i) ajouter l'enjeu et, pour (a), l'option « non concurrente exigée des deux sortes » (CL4 B1 (i)), pour (b) l'option « précédence de la v5 » ; (iii) écrire « sans effet sur la lecture ; toute dérogation exige une décision de Lazar qui modifie R-765 et une nouvelle version de la grille, avant l'ouverture de la lecture » ; (iv) dire « défaut au 2026-11-15, sous réserve du mot sur D-G0-1 ».

### CL5-11 — mineur — l'écart (a) est plus large que sa raison

Lignes v6 : 222-223, 1009-1011.
Défaut : la raison donnée de l'écart est « une pièce concurrente scellée **après coup** défairait R-765 » ; la règle est plus large : « une pièce concurrente ne le retire pas », même une pièce concurrente **antérieure** au négatif par liste d'arrêt (qui n'est pas un nouvel essai). Une preuve positive, de nom différent, scellée avant, voit son critère lu sur la pièce négative.
Correction : borner l'effet aux pièces dont le `.sha256` est postérieur (ordre d'ascendance, comme l. 369-372) au verdict négatif ; les pièces concurrentes antérieures restent rapportées sans effet sur le gel. À défaut, dire pourquoi la règle large est voulue.

### CL5-12 — mineur — critère 3 : verdict de P4-instrument absent, « absent » ou « invalide » ?

Lignes v6 : 566-567, 579, 587-589, 599.
Défaut : la cascade l. 587-588 met en rang 1 « absent » quand « une preuve attendue est absente après R11 (M-0.1) » (correction de CL4 m4) ; le verdict de P4-instrument figure dans les « Preuves attendues » (l. 566-567) ; or M-3.5 et le défaut de D-G0-11 rendent un P4-instrument absent « non tenu — invalide » (l. 579, 588-589, 599). Les deux lignes rendent deux sous-états différents pour le même fait ; la précédence les départage (rang 1), mais le texte de D-G0-11 dit l'inverse. Sans effet sur le gel (la condition (2) lit « invalide » en toutes lettres), effet sur le sous-état rapporté.
Correction : à l. 587-588, « une preuve attendue **autre que P4-instrument** est absente », ou à M-3.5 « absent ».

### CL5-13 — mineur — annexe B, ligne D-G0-1 : renvoi non mis à jour

Ligne v6 : 1080.
Défaut : « grille scellée ≤ 2026-11-15 avec D-G0-1 à 13 tranchés ou échus » ; le corps (l. 303), l'annexe B (l. 1072, 1074) et l'annexe C (l. 1116) disent D-G0-1 à D-G0-14. Un lecteur qui applique la ligne de D-G0-1 tient D-G0-14 pour facultatif.
Correction : « D-G0-1 à 14 ».
Essai : `grep -n -E 'D-G0-1 à 13' brouillon-G0-grille-lecture-v6.md` → l. 1080 seule.

### CL5-14 — mineur — DIV-1 à DIV-4

Lignes v6 : 1095-1104, 24-28, 303-308, 1116.
Constats (la table de dépendance et le mémo sont sur une branche `canal/*` que je n'ai pas le droit d'ouvrir : je n'ai pas vérifié leurs lignes 11, 14, 41, 130, 224, 227 ; les colonnes « table v4 / mémo » ne sont donc pas contre-lues, seulement la colonne « grille v6 » et la cohérence interne) :
- La grille est **scellable sans les trancher** : le régime de scellement (l. 303-308) ne dépend que de D-G0-1 à D-G0-14 ; le lecteur de G0 ne reçoit que la grille et le dossier (l. 322), donc l'écart avec la table n'affecte pas la lecture.
- DIV-1 est déjà l'« autre option » de D-G0-13 (variante v3 : tout négatif de la première lecture gelé, l. 1092) ; la poser deux fois est inutile. Mais sa colonne « à décider » ajoute « la grille et la table doivent dire la même chose **avant scellement** » : précondition cachée, absente du régime de l. 303-308 et de l'annexe C point 1. Soit la retirer, soit l'ajouter à l'annexe C.
- DIV-2 : la troisième option (table : verdict scellé pour 1 à 5, valeur copiée et classe) n'est pas dans D-G0-8, dont les options sont deux autres ; si Lazar la choisit, M-0.5, F-4.x et F-5.x changent (la v6 le dit) : il faut alors une v7 et une contre-lecture avant le 2026-11-15, ce que l'annexe C ne prévoit pas.
- DIV-3 est qualifiée « compatible » ; elle est plus : la grille ne dit pas si, après un arrêt, la même lecture reprend (même `C_lecture`, même fichier d'ouverture) ou si une nouvelle ouverture est permise, ni si le seuil du 2027-01-31 court pendant l'arrêt. Une nouvelle ouverture aurait un `C_lecture` plus tardif (coupure des preuves, l. 297-301). Recommandation : en faire un point D-G0-15, défaut « la même lecture reprend, même `C_lecture`, la session consigne la durée de l'arrêt ».
- DIV-4 : posée sans divergence ; rien à dire.

### CL5-15 — mineur — la présente contre-lecture ne décharge pas m11

Lignes v6 : 1019-1024, 338-341, 922.
Défauts : (i) la v6 exige un contre-lecteur « d'un autre modèle que l'auteur … et d'une autre lignée que la session-depot » ; je suis un autre modèle (Sonnet 5.5 contre Opus) mais lancé depuis la session-depot : l'exigence « autre lignée » n'est pas remplie. La v6 prévoit (l. 1022-1024) que la session consigne et porte à Lazar le choix entre attendre et sceller avec cette réserve : à faire. (ii) La liste des interdits de lecture (l. 338-341, 922) ne contient pas `canal/*`, alors que les contre-lecteurs en reçoivent l'interdiction et que la v6 cite, en tête (l. 24-28), un fichier d'une branche `canal/*` ; un lecteur de G0 qui suivrait la liste de la grille pourrait ouvrir la branche. Correction : ajouter `canal/*` à la liste, ou dire pourquoi elle n'y est pas.

## Réponses aux sept critères de la demande

1. **CL4 corrigé ?** Voir la table : dix-huit constats portés aux lignes annoncées, aucune correction absente. Résidus : voir CL5-01 à CL5-15.
2. **B1.** *Cohérence avec la section 2 et R-765* : oui sur l'architecture. Le « négatif gelant » est défini au niveau de la preuve (l. 215-234), la précédence ne décide plus du gel (l. 236-238, 362-368), « il ne choisit pas » vaut pour le sous-état rapporté (l. 250-251, 377-379) tandis que le gel par liste d'arrêt est lu sur (δ), conformément à « jamais retenté ». Les cinq cas de CL4 Q4 : cas 1 → (c), défaut gelant ; cas 2 → (δ) rapporte le négatif de (i) malgré l'« absent » de (ii) ; cas 3 → pièces concurrentes : non concluant pour le sous-état, gelant seulement par liste d'arrêt ; cas 4 → le négatif d'un niveau non fixé ne gèle rien (l. 227, 251-252) ; cas 5 → plus de « invalide » par défaut de forme, mais voir CL5-01. *Un négatif par liste d'arrêt peut-il encore être masqué ?* Oui, par trois chemins : un « non concluant » de M-0.3 (CL5-01), une ligne (β) mal formée ou absente (CL5-02), et, pour une preuve à deux familles, une attribution fausse de (β) (CL5-05). *Un négatif contre un seuil non fixé d'avance peut-il geler ?* Non, tel qu'écrit (l. 227-228, 251-252) ; le seul cas voisin est le négatif par table suspect de propreté, qui gèle faute de règle (CL5-03).
3. **D-G0-14.** Bien formé pour (c) (avantage et inconvénient écrits, confiance 0,5, défaut écrit) ; (a) et (b) sans vraie option, sans enjeu, délai non dit, voie de dérogation absente : CL5-10. Applicable à la lettre pour (a), (b), (c) ; non applicable au cas du négatif par table avec R4 (CL5-03).
4. **Les trois écarts.** Voir section suivante.
5. **Motifs.** CL5-02, CL5-06, CL5-08, CL5-09 ; `|` échappé : vérifié (154 lignes, 0 au mauvais compte).
6. **Ce que la v6 a pu casser.** Renvois de lignes de la table de tête : tous exacts. Annexes B à G : ligne D-G0-1 non mise à jour (CL5-13) ; annexe A : le tableau a bien 13 colonnes avec (δ) (compté) ; cascades « États » alignées (m4), sauf le conflit du critère 3 (CL5-12) ; les critères 6 et 7 n'ont pas de cascade pour « non concluant » de M-0.3 (l. 723-724, 746) : renvoi implicite à la Métrique, à écrire en une phrase.
7. **DIV-1 à DIV-4.** CL5-14.

## Les trois écarts de la v6 aux propositions de CL4

- **(a) négatif par liste d'arrêt gelant malgré une pièce concurrente** : *justifié sur le fond* (sinon une pièce de nom différent scellée après coup défait « jamais retenté ») ; *trop large* (CL5-11) ; *non offert à Lazar dans l'annexe B* (CL5-10).
- **(b) première forme de la ligne désignée** : *justifié par l'essai*. `T0.4-rapport-contre-lecture-3-v1.md` l. 294 : « **Non scellable en l'état.** … le brouillon me paraît scellable » : `grep -o … | wc -l` rend 2 formes, la première (« Non scellable ») est la bonne. Reproduit. Risque restant : la deuxième phrase n'est pas lue et `IMPREVU_CL` a des angles morts (CL5-06).
- **(c) `DOSE` élargi aux décimales ≥ 1** : *justifié et reproduit*. Motif de CL4 sur « Doses non nulles : 1,5 ; 3 » → 0 ; `DOSE` → 1. Restes : espace insécable, « 3 fois » (CL5-08).

## Ce que je n'ai pas vérifié

- DIV-1 à DIV-4 contre la table de dépendance et le mémo (branche `canal/*`, interdite).
- L'empreinte `6c00b7fd…` du script M-8.3 citée à l'annexe G (je n'ai pas le fichier d'essai de l'auteur) : j'ai extrait le script du texte de la v6 et l'ai essayé.
- Le script M-0.8 (a) et (b), M-0.4, M-0.6, les sept jours, les motifs non modifiés par la v6 (CL3 et CL4 les ont reproduits).
- Le rendu dans un afficheur GFM : le compte de cellules (`\|` retiré) et la règle GFM fondent la vérification des tables.
- Les verdicts scellés de `docs/verdicts/` n'ont pas été lus : seuls les comptes `grep -c` de la ligne de forme (β) l'ont été.

Fin de rédaction : 2026-10-29 23:01 UTC (`date -u` : 23:00:29 avant cette dernière édition).
