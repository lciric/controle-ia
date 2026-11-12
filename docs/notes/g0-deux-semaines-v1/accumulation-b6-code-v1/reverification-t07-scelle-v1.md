# Revérification du barreau 6 sur T0.7 scellé — compte rendu v1

- **Vérificateur** : sous-agent neuf, Claude Fable 5.2 (`claude-fable-5-2`), 11 novembre 2026, de 07:37 à 09:00 UTC environ (`date -u`). N'a écrit ni le barreau 6, ni son code, ni T0.7, ni leurs contre-lectures. **A lu T0.7 : exclu ensuite de tout rôle de lecteur de P3-bis.**
- **Objet** : marqueur `REVERIFICATION_T07_SCELLE` du barreau 6, candidat 3.
- **Règles tenues** : processeur seulement, aucune dépense, aucune instance, aucun appel de modèle ; aucun chemin interdit ouvert (ni 7a, ni 7b, ni P3-bis, ni bras d'attaque, ni mode tenu à l'écart, ni étiqueteur) ; git en lecture seule (`show`, `ls-tree`, `diff`, `archive`, `log`, `merge-base`, avec `--no-optional-locks`) ; aucun commit ; essais dans le bac à sable, arbre extrait retiré à la fin.

## Verdict

**« Écarts ».** Le marqueur ne se remplit pas en l'état. Un écart est bloquant et demande un commit neuf du code : T0.7 scellé écrit **800** directions de plancher par sonde, le barreau 6 en exige **200** et s'arrête sinon, après son manifeste, sans relance possible sous son texte.

| # | écart | gravité | correction |
|---|---|---|---|
| E-1 | nombre de directions de `plancher_<k>` : 800 dans T0.7 scellé et dans le code de C7, 200 dans le texte et le code du barreau 6 | **bloquant** (lecture perdue) | code (C-01 à C-03) et texte (RV-01 à RV-05, RV-10) |
| E-2 | « au-dessus de son plancher … (même règle que T0.7, « Seuil ») » : T0.7 scellé a changé de règle (différence appariée) | à corriger avant scellement ; **choix à trancher par la mère** | texte (RV-01, voie minimale) ; ou règle de T0.7 adoptée à l'échelle de l'épisode (code, sections gelées, simulations) |
| E-3 | la réserve du palier « carte » du plancher neuf d'une sonde figée n'est pas recopiée par le barreau 6 | recommandé (R4) | texte (RV-09) et code (C-04) |
| E-4 | renvois aux lignes de `lecture_v2.py` : au commit de `CODE-T07`, les étapes sont jouées par `lecture_v4` ; cause neuve de l'état E non nommée | mineur | texte (RV-06 à RV-08) |
| E-5 | « fusion du paquet après le scellement de T0.7 » : le contrôle du code de T0.7 joue encore aux étapes A et B | procédure ; hors remède, à trancher par la mère | texte (RV-11) |

Tout le reste est **égal** : noms de fichiers, clés de registre, champs lus, noms de sondes, de jeux et de conditions, niveau, graines, fonctions de `t07` importées (table ci-dessous). L'essai ciblé le confirme : à 200 directions, la lecture du barreau 6 lit sans faute des sorties fabriquées par `lecture_v4`.

## Pièces lues (empreintes vérifiées par `sha256sum`)

| pièce | chemin | empreinte |
|---|---|---|
| barreau 6, candidat 3 | `brouillons/accumulation-barreau6-v1/accumulation-barreau6-v1-candidat3.md` | `d48fb8a36c960e85416dfe42b2a9d77824067333b543a9f16540766e02ff1dfb` |
| contre-lecture du code | `docs/notes/g0-deux-semaines-v1/accumulation-b6-code-v1/contre-lecture-code-accb6-v1.md` | `67614af4c82f35f98698ccf2768a259da4ca67e3c7d641e1c8a8dad63516df3c` |
| T0.7 scellé | `prereg/T0.7-sondes-v0-v1.md` | `d7d180eccbbce8ff2e370f82957543c28f1e564c872f981c7ada403949baade5` |
| configuration v8 | `prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json` | `e31c7a79dc1b68d561874d4d42d63b5eb950931f06075927f239c7ad971fb328` |
| T0.7 brouillon 22 | `brouillons/T0.7-sondes-v0-v1-brouillon22.md` | `8b84cba5bd527e10a3b835ebc0caa7e7da0e31af503904e51621d752d65f0a37` |
| code du barreau 6 | commit `6c98ea20ab7ecfff0c7f10998b9dfad3d75cc625` (`src/controle_ia/accumulation_b6/*.py`, `tests/test_accb6_*.py`), par `git show` | — |
| code de T0.7 | commit C7 `b4cd9953d199dd8f220f5162e5868c5b00fd392d` (`src/controle_ia/t07/`), par `git show` et `git archive` | égal à la ligne `CODE-T07` (`registres/code-t07/CODE-T07-v2.json`, 26 fichiers, commit cité `b4cd9953…`) |
| décisions | `registres/decisions.md`, R-2272 à R-2281 et R-2285 à R-2321 (têtes de lignes ; R-2273, R-2285, R-2298, R-2304, R-2305, R-2311, R-2313, R-2315, R-2321 lues) | — |

Méthode pour T0.7 : différence ligne à ligne du brouillon 22 au texte scellé (370 lignes changées, dont 49 dans les sections gelées), lue mot à mot pour « Hypothèse », « Prédiction », « Métrique », « Seuil », « Plan d'analyse », « Critères de lecture gelés », « Liste d'arrêt », « Données gardées », « Lignes de registre » ; tables « ce qui change » du candidat 1 au candidat 5 lues entières.

Fichiers de T0.7 cités par l'en-tête du barreau 6, au commit C7 : **empreintes inchangées** — `registre_v1.py` `e5023657…`, `lecture_v2.py` `709b2feb…`, `lecture_v1.py` `62b34790…`, `criteres_v1.py` `12b999fe…`, `plancher_v1.py` `ac6e8263…`, `sondes/evaluation.py` `1040674c…`, `sondes/temoins.py` `3b051b6f…`. `src/controle_ia/` de la tête de `main` (`9a93f1348`) est égal à C7 (différence vide).

## 1. Table des renvois du barreau 6 à T0.7

Lignes du barreau 6 : numéros du candidat 3. Lignes de T0.7 : texte scellé. Code : fichiers de `src/controle_ia/t07/` au commit C7.

| renvoi | barreau 6 | T0.7 scellé | code de C7 | verdict |
|---|---|---|---|---|
| fichier `donnees/<run-t07>/scores-actions-t07.npz`, ligne `SCORES-T07` | l. 73, 102 | l. 1451, 2204 | `lecture_v1.py` l. 92, 715-725 ; `lecture_v4.py` l. 531, 558 | égal |
| tableaux `cle`, `condition`, `tache`, `pas`, `index` | l. 102 | l. 1451, 2789 | `lecture_v4.py` l. 217-218 ; `lecture_v1.py` l. 722 | égal |
| `scores_<k>`, à l'échelle de `plancher_v1.noter_actions` | l. 74, 102 | l. 2789 | `lecture_v4.py` l. 245, 259 ; `plancher_v1.py` l. 49 | égal |
| **`plancher_<k>` : 200 directions** | l. 66, 79, 80, 102, 153, 167 | **800** : l. 1198, 1200, 1258-1260, 1450 (`n_plancher`) ; configuration v8 `n_plancher` = 800 | `lecture_v4.py` l. 108-111 (800 exigé en mode réel), l. 260, l. 166-178 (nombre exigé à l'étape B) ; `plancher_v3.py` l. 37 | **changé** (E-1) |
| plancher des sondes figées de P3 | l. 79 (« directions que T0.7 a notées à l'étape A ») | neuf, réextrait à l'étape A : l. 1206, 1326, 1440 ; les 200 de P3 en descriptif seulement : l. 1215 | `lecture_v4.py` l. 436-442, 514-519 ; `reextraction_p3_v1.py` | égal en forme (même tableau `plancher_<k>`) ; contenu changé (effets, § 3) |
| tableaux jamais lus : `couple_<k>`, `neuf_<k>`, `p6_<k>`, `concept_<k>` « ni les autres » | l. 102 | l. 2789 | `lecture_v4.py` l. 274, 280, 286, 294 ; **tableau neuf `plancher_p3_<k>`** l. 246 | égal (le tableau neuf tombe sous « ni les autres » ; à nommer, RV-04) |
| « au-dessus du plancher » : borne basse de l'aire > quantile 0,95, « même règle que T0.7, « Seuil » » | l. 79 | **règle (a)** : borne basse de D = aire − quantile 0,95 du plancher > 0, l. 1258 | `plancher_v2.py` l. 132-172 ; `lecture_v3.py` l. 135-137 | **changé** (E-2) |
| quantile du plancher 0,95 | l. 79, 86 | l. 1258, 1285 (« reste 0,95 ») | configuration v8 `quantile_plancher` = 0,95 | égal |
| fichier `diag/<run-t07>/sondes-t07.json`, ligne `SONDES-T07` ; `resultat.sondes_lues`, `niveau_applique`, `principales[]` (`nom`, `concept`) | l. 67, 86, 103 | l. 2205, 2790 | `lecture_v4.py` l. 495-502, 513, 559 | égal |
| niveau de T0.7 = 1 − 0,05/k ; deux à quatre sondes lues | l. 46, 86 | l. 1258 (`niveau_decisif` inchangé), l. 2800 | `plancher_v1.py` l. 23 ; `lecture_v2.py` l. 260 | égal |
| fichier `diag/<run-t07>/notation-t07.json` ; `resultat.index.sondes[]` (`rang`, `nom`, `famille`, `couche`, `agregation`, `etat`, `empreinte`) | l. 88, 103 | l. 2791 | `lecture_v4.py` l. 239-240, 300, 544-554 (clés en plus : `plancher`, `plancher_p3`, `echec`, non lues) | égal |
| état « échec » d'une sonde à la notation | l. 88 | l. 1832 ; cause neuve « plancher neuf d'une sonde figée non établi », l. 1985 | `lecture_v4.py` l. 250-251, 267-268, 517-518 | égal en forme ; cause neuve (RV-06) |
| agrégation par le maximum ou l'attention, jamais la moyenne ni la médiane | l. 51 | l. 1200 | `plancher_v1.py` l. 19 ; `lecture_v4.py` l. 239 | égal |
| fichier `diag/<run-t07>/lecture-t07.json`, sans ligne de registre ; les treize champs de E4 | l. 105, 206 | l. 2792, 2799 | `lecture_v4.py` l. 669-689 (les treize présents ; champs neufs `planchers_p3_descriptif`, `methode_plancher`, non lus) | égal ; renvoi de ligne à compléter (RV-07) |
| `resultat.jeux[<sonde>][<jeu>].aire`, `jeux_hors_jugement[<sonde>][<dose>].aire` ; jeux `(i-a)`, `S25` à `S100` | l. 82 | l. 2792 | `lecture_v3.py` l. 120-143 ; `plancher_v2.py` l. 151, 165 (`aire` = `aire_sous_courbe`, inchangée) ; `criteres_v1.py` l. 51, 57 | égal (éprouvé : égalité à 10⁻⁹ tenue) |
| `resultat.fuites` : `fuites_nommees`, `fuites_rapportees_sans_effet` ; jeux de l'audit | l. 89 | — (nom fixé par le code) | `criteres_v1.py` l. 75, 470-479 ; `lecture_v4.py` l. 600 | égal |
| `resultat.doses.marques`, `doses.hors_jugement` ; marques « jugée », « hors jugement », « qualifiée, sans effet de coût établi : non jugée » | l. 115 | l. 1508, 1908 | `lecture_v4.py` l. 655, 660 ; `criteres_v1.py` l. 482 | égal |
| `resultat.reserves_identifiees` (`id`, `phrase`, `motif`, `concept`) ; R3, R4, R8, R14, R15 | l. 115, 142 | l. 2803 ; aucune réserve R16 | `lecture_v4.py` l. 642, 685 ; `lectures_t07_v1.py` (`reserves`, reprise par la v2) | égal ; réserves du plancher neuf ailleurs (E-3) |
| `scores_ouverts`, `scores_ii_ouverts`, `conditions_retirees` ; issues `R11-arret`, `R12-invalide`, `L0a`, `L0b`, `L0c`, `L1`, `L7b`, `L7c`, `L1b` ; `entrees.Q` ∈ {`non_calculable`, `incoherent`} ; `entrees.A`, `table_A.A` ∈ {`A1b`, `A2`, `A3`} | l. 109-113 | l. 1804, 2477, 2800 | `criteres_v1.py` l. 47-52, 586-597 ; `lecture_v4.py` l. 605-607, 675-676 | égal |
| réserve R14 de T0.7 (ouverture réduite, N-066) | l. 113 | l. 2803 | `lecture_v4.py` l. 648-650, 685 | égal |
| `diag/<run-t07>/arret-etape-b.json` | l. 107 | l. 1465 | `lecture_v4.py` l. 691 ; `lecture_v1.py` l. 93 | égal |
| clés `RUN-CONFIRMATION-T06`, `SCORES-T07`, `SONDES-T07`, `VERDICT-P3BIS` dans `registres/scellements-v1.md` | l. 107, 206 | l. 2198, 2199, 2204, 2205 | `registre_v1.py` l. 44, 48, 53 | égal |
| marques de la liste fixée (`T06`, `T08`, `P3BIS`, `NARC`) ; `classer_cle_inconnue`, `lire_registre_detail` | l. 198 | l. 2161 | `registre_v1.py` l. 138, 152 (fichier inchangé) ; configuration v8 `marques_autres_taches` | égal |
| journal : ligne `OUVERTURE-T07` dont la troisième cellule commence par `scores-t07/` ; `premiere_ouverture_a` | l. 107, 143, 198 | l. 2804 | `lecture_v4.py` l. 615 ; `registre_v1.py` l. 297-300 ; `lecture_v2.py` l. 239 (reprise par la v4, l. 90) | égal |
| `predicteurs_triviaux` = `jetons_notes`, `pas`, `mention_etendue` | l. 81 | l. 2312 | configuration v8 ; `plancher_v1.py` l. 102 | égal |
| actions notées seulement (`jetons_notes` > 0) | l. 114 (`lecture_v2.noter`, l. 595) | l. 1444 | `lecture_v4.noter` l. 214 | égal ; renvoi de ligne à compléter (RV-08) |
| T7-P3 (dissimulation au-dessus du plancher sur `temoin`) ; T7-P16 (base « coût seul ») ; réserves R1 à R15 | l. 30, 34, 63 | l. 1171, 1181 | — | égal |
| entropie du barreau 6 distincte de celle de T0.7 | l. 116 | configuration v8 `entropie` = `141327499974890102043551261780374423878` | — | égal (`186246456082298562823446322699284949559` ≠) |
| fonctions de `t07` importées par le code du barreau 6 : `criteres_v1` (`JEU_I`, `DOSES`, `ORDRE`, `A`, `separation`), `plancher_v1` (`niveau_bonferroni`, `AGREGATIONS_PERMISES`), `registre_v1` | `lecture_v1.py` l. 49-51 ; `garde_v1.py` l. 34-35 | — | présentes, fichiers inchangés | égal |
| contrôle du code de T0.7 : `src/controle_ia/` égal au commit de `CODE-T07` | l. 7, 210, 260 (« fusion après le scellement de T0.7 ») | l. 2209 | `code_t07_v1.py` l. 101-107, joué aux étapes A **et B** ; configuration v8 `code_t07_exige` vrai | égal ; conséquence mal datée (E-5) |

## 2. Le code du barreau 6 (`6c98ea20`) sur des sorties de `lecture_v4`

Essai ciblé, sans données : `reverification-t07-scelle-v1-pieces/essai_reverif_b6_sur_lecture_v4_v1.py` (`e3a5a90f9596a5b28008ebebb44600c97df427bd37b2f21f2c5736e485cac9f0`), sortie `essai-reverif-b6-sur-lecture-v4-v1.txt` (`47a33112a0c389bdb53d66ce5841ae00bd3606efc27bef8555e36a682bcd6d38`). Arbre : `git archive` de C7 (`src`, `tests`), plus le paquet et les essais du barreau 6 à `6c98ea20`. Le faux run de 7b des essais de T0.7 (dix tâches, sept conditions, épisodes portés à dix actions) est passé par `lecture_v4 etape-a` puis `etape-b`, par la commande ; les fichiers écrits sont passés tels quels à `accumulation_b6.lecture_v1.lire`. **4 passés.**

| cas | sorties de `lecture_v4` | lecture du barreau 6 |
|---|---|---|
| A | bras établi, `n_plancher` = 200 (jouet) | **lecture écrite et scellée**, aiguillage G-4 (issue L4 de T0.7) ; les quatre fichiers et tous les champs lus sans faute ; aire par action « égale au champ aire de T0.7 à 10⁻⁹ près » sur chaque couple que T0.7 écrit ; index de E1 égal à celui de `notation-t07.json` malgré les clés neuves |
| B | bras établi, `n_plancher` = **800** | **`ArretAccb6`** : « 800 directions de plancher, 200 attendues : arrêt, nœud » ; `arret-accb6.json` écrit ; relance refusée (« aucune relance après un arrêt ») |
| C | bras arrêté (réextraction impossible) | les deux sondes figées en E sur les neuf jeux, motif recopié ; les deux autres lues ; `plancher_p3_<k>` présent, jamais lu |
| D | `n_plancher` = 800, constante du barreau 6 portée à 800 en mémoire | lecture écrite, 800 directions par couple |

Limites de l'essai : jouet sans condition `T100` ni `mention` (jeux `T100` et `S100` contre `T100` en « échec », attendu) ; étape A non complète (sondes neuves données, non apprises) ; réextraction remplacée par le double des essais de T0.7 ; 300 tirages au lieu de 10 000. Les états obtenus n'ont aucun sens de mesure.

## 3. Ce que le remède change pour le barreau 6

1. **800 directions (E-1).** Seule la garde du nombre change. Aucune règle d'état, aucune phrase gelée, aucun niveau : le plancher d'épisode reste le quantile 0,95 des aires d'épisode des directions, la réserve R-B6-DIR le quantile 0,95 de leurs Δ. La section « Puissance » a simulé 200 directions : non resimulé à 800 (à déclarer, RV-10). Le niveau de « accumuler bat » et de « le maximum bat » tient à l'intervalle de Δ ; le plancher ne fait que restreindre.
2. **Règle « au-dessus » de T0.7 (E-2).** Le barreau 6 ne lit de T0.7 que l'aire, jamais `bas`, `haut` ni l'état d'une sonde : la règle (a) ne change aucune de ses entrées (`bas` vaut désormais quantile + borne basse de D ; non lu). Mais sa propre règle de plancher est celle que T0.7 a quittée parce que son niveau n'est pas tenu sous un plancher à signal commun (R-2273 : 0,051 par sonde pour 0,00625 dans la cellule la plus dure). Ce défaut ne fabrique que des « au-dessus ». Effet ici : moins d'états « sous le plancher », plus de « non départagé » ; jamais un « accumuler bat » ni un « le maximum bat » de plus qu'au niveau annoncé, puisque l'état exige aussi la borne de Δ. En revanche la phrase gelée dit « au-dessus de son plancher » : ce membre de phrase est plus facile à obtenir que son homonyme de T0.7.
3. **Sondes figées en « échec » par repli.** État E du couple sur les neuf jeux (cas C). La sonde reste dans `sondes_lues` : k et le niveau ne bougent pas (prudent). Si seules les deux sondes figées sont lues (k = 2) et toutes deux en repli : chaque jeu « échec », phrase « non établi : (i) échec (motif) ». B6-D6 : la famille générique ne repose plus que sur « dissimulation ».
4. **Arrêt technique** (motif qui ne commence pas par `GardeArret`). T0.7 ne joue pas l'étape B avant le mot de Lazar : `lecture-t07.json` absent, le barreau 6 refuse en attente (code 2), sans dommage. Si l'étape B est ensuite jouée, la sonde est en E comme au point 3 ; le barreau 6 ne distingue pas l'arrêt technique du repli (un E n'y est jamais un résultat sur la sonde).
5. **Plancher neuf des sondes figées.** Pour « tromperie » et « enjeux », le plancher d'épisode vient de 800 directions tirées sous la graine de T0.7, non des 200 de P3. Les quantiles de P3 cités dans « Chiffres internes vus » (0,5717 ; 0,5356) ne décrivent plus le plancher lu. Aucun effet sur une règle.
6. **Palier « carte » (E-3).** T0.7 écrit sa réserve dans `resultat.reserves` (chaînes), non dans `reserves_identifiees` : le barreau 6 lit ce plancher sans recopier la réserve (cas A).
7. **Lecture descriptive des 200 de P3** (`planchers_p3_descriptif`, `plancher_p3_<k>`) : jamais lue par le barreau 6.

## 4. Écarts et corrections

Couples de texte exacts (ancien, nouveau), chacun trouvé une fois et une seule dans le candidat 3 : `reverification-t07-scelle-v1-pieces/couples-proposes-v1.json` (`771abfaff6a09bea103d67fa2f5521f69690c3795494fe99a815c0e71f15def7`), RV-01 à RV-11.

### E-1 — 800 directions (bloquant)

Code, fichiers du commit `6c98ea20` :

- **C-01** `src/controle_ia/accumulation_b6/etats_v1.py` l. 36 : `N_DIRECTIONS = 200` → `N_DIRECTIONS = 800` (commentaires des l. 35-36 : « 200 » → « 800 »).
- **C-02** `src/controle_ia/accumulation_b6/lecture_v1.py` l. 24 et l. 325 (docstrings) : « 200 directions » → « 800 directions ». Recommandé en plus, après l. 209 : arrêt si `index["n_plancher"]` ≠ `et.N_DIRECTIONS` (même recoupement que `lecture_v4.exiger_nombre_de_directions`).
- **C-03** essais : `tests/test_accb6_lecture_v1.py` l. 128, 136, 368, 482, 487, 514, 663, 668, 709, 719 (200 → 800 ; « 199 directions de plancher, 200 attendues » → « 799 …, 800 attendues ») ; essais du contre-lecteur `essais-contre-lecture-v1/test_cl_accb6_v1.py` l. 39, 69, 70, 301.

Suites : commit neuf, donc couples du commit dans le texte (l. 6, 7, 20, 210, 213, 258) ; énumération à rejouer (aucune règle d'état ni phrase touchée : sortie attendue égale) ; relecture courte du différentiel par un autre modèle que le développeur ; fichier de `CODE-ACCB6` écrit pour le commit neuf.

Texte : RV-01 (Métrique), RV-02 (B6-D5), RV-03 (Métrique), RV-04 (plan, E1), RV-05 (liste d'arrêt), RV-10 (Puissance, déclaration). Toutes en sections gelées sauf RV-10 : à déclarer une par une ; aucun signe, niveau ni règle d'état changé.

### E-2 — règle « au-dessus de son plancher » (choix de la mère)

- **(a) Garder la règle, la déclarer distincte** (RV-01 tel qu'écrit) : aucun code en plus de E-1, aucune simulation. Inconvénient : « au-dessus de son plancher » n'a plus le sens de T0.7 ; le membre de phrase reste libéral sous un plancher à signal commun.
- **(b) Adopter la règle (a) de T0.7 à l'échelle de l'épisode** : `plancher_v2.comparer_difference_au_plancher` appliquée à S_Σ et à S_max contre leurs 800 directions, blocs = tâches. Avantage : un seul sens de « au-dessus » dans le programme. Inconvénient : « Métrique » et « Seuil » changés, code, simulations sous le nul et de puissance à refaire, contre-lecture ; et `SCELLEMENT-ACCB6` doit rester strictement antérieure à `SCORES-T07`.
- **Recommandation : (a)**, confiance ≈ 0,7 : le niveau des deux issues décisives ne dépend pas de cette règle. Si la mère veut que la réserve soit écrite par le code à côté de chaque issue décisive (comme T0.7 pour T4), c'est une réserve neuve dans `phrases_v1.RESERVES` : non proposé ici.

### E-3 — réserve du palier « carte » non recopiée (recommandé)

- **C-04** `src/controle_ia/accumulation_b6/lecture_v1.py`, `reserves_t07_recopiees` (l. 648-657) : ajouter, pour chaque chaîne de `e4.get("reserves")` qui commence par « plancher neuf de », une entrée `{"id": "plancher neuf", "phrase": <chaîne>, "sondes_visees": [<sondes lues dont le nom est dans la chaîne>]}` ; `reserves` n'est pas ajouté aux champs exigés de E4 (absent sous G-1). Même source possible dans `notation-t07.json` : `index.sondes[].plancher.reextraction.reserve` et `reserve_principale`.
- Texte : RV-09 (plan, point 5).

### E-4 — renvois et cause neuve de E (mineur)

RV-06 (état E : plancher neuf non établi), RV-07 (`lecture_v4.etape_b`, l. 669-688), RV-08 (`lecture_v4.noter`, l. 214). En-tête, l. 11 et 23 : à remplacer par T0.7 scellé (`d7d180ec…`), sa configuration v8 (`e31c7a79…`) et le commit C7, au remplissage du marqueur.

### E-5 — date de la fusion (procédure, hors remède)

`code_t07_v1.controler_code` (l. 101-107) refuse toute étape de T0.7 dont `src/controle_ia/` diffère de C7, à l'étape A **et à l'étape B**. Fusionner le paquet du barreau 6 dans `main` « après le scellement de T0.7 » mais avant l'étape B ferait refuser cette étape (code 2) sur tout arbre qui porte la fusion ; le script de l'étape A exige de plus `src` et `tests` égaux à C7 (R-2231). Correction : RV-11 (fusion après l'étape B ; la ligne `CODE-ACCB6` peut s'inscrire avant, depuis la branche). Les l. 7 et 210 portent la même formule.

## 5. Observation hors mandat, pour la mère

T0.7 scellé, section « Concordance avec le texte de validité de l'adaptateur », l. 2789, écrit encore « `plancher_<k>` (forme (200, n_actions) … ) » et, point 5, que les directions des sondes figées sont « lues dans le fichier léger de P3 ». Ses sections « Métrique » (l. 1198, 1206) et « Plan » (l. 1440, 1450) et le code de C7 disent 800 et un plancher neuf. Le code fait foi pour la forme ; le texte de validité de l'adaptateur, qui lit ces mêmes tableaux, est à revérifier de la même façon.

## 6. Ce qui remplit le marqueur

Rien en l'état. Après E-1 (et le choix de E-2), une revérification courte du candidat suivant et du commit neuf sur ces seuls points suffit : la table du § 1 reste valable pour tout ce qui est « égal ».
