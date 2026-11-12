# Ordre d'épreuve E3 ter — galop d'essai de la garde d'équivalence (99ᵉ centile) sur une carte, v1, brouillon 2

- **Statut** : brouillon 2, reçu du sous-agent rédacteur de la session mère (`session_016QhUrrLeN21G7Z9KZobE42`), 8 novembre 2026 ≈ 15:20 UTC ; remplace le brouillon 1 (`69a1c969…`, gardé, R12) après la contre-lecture cl1 (`contre-lecture-ordre-e3-ter-v1-cl1.md` : 3 bloquants, 7 majeurs, 8 mineurs, tous appliqués, table en fin de texte) et les décisions de la mère (R-1840 : **option D**, plafond 16 USD, ligne de GO séparée, chaîne v13). **Non scellé, non commis, aucune ligne de GO encore.** La mère remplit `<<COMMIT_V13>>`, `<<COMMIT_E3TER>>`, `<<GO_E3TER>>`, `<<FIN_GO_E3TER>>`, puis seconde contre-lecture (R2), scellement, ordre remis à une fille d'exécution.
- **Déclencheur** : point E3-6 du compte rendu d'E3 bis (R-1769 ; R-1784 ; décision (b) de Lazar consignée à R-1825, point 4) : la garde d'équivalence version 3 (99ᵉ centile, tolérance 0,2) n'a contrôlé aucune action dans les six états d'évaluation d'E3 bis ; le contre-lecteur de l'ordre de course (couple O2) exige que la mère règle ce point avant toute création d'instance de la course (marqueur `<<REGLEMENT_E3_6>>`). Mot de Lazar, session mère, 8 novembre ≈ 14:05 UTC, verbatim : « (b) exiger d'abord un galop d'essai plus grand qui l'exerce — un run d'instance de plus (quelques USD, quelques heures), puis relecture. : go » ; R-1825 fixe « dimensionné pour ≥ 5 actions contrôlées attendues par état » ; R-1830 : « coûter le moins possible ». Lazar, 15:10 UTC : « le vrai goulot est la course de dose-réponse, lance-la now » : le galop part aujourd'hui.
- **Nature** : galop d'essai (R5) d'une garde d'arrêt : **cas sain sur carte** ; les **artefacts** sont tenus par les cinq essais processeur de la suite ciblée, jouée d'office sur l'instance même avant le run (§ 3). Aucune donnée décisive n'en sort : rien de ce run n'alimente une lecture de T0.6, de P3 ou de G0. Sondes, aires, coûts et tests croisés qu'écrit la chaîne ne sont **pas lus** (§ 4).

## 0. Pourquoi un galop, et pourquoi E3 bis n'a rien contrôlé en évaluation

La garde tire, **par tâche**, un générateur neuf (`g["tache/<identifiant>"]`, `t06/lanceur.py` l. 266–270) : les pas contrôlés sont les mêmes pour toutes les conditions et tous les états d'adaptateur. À E3 bis (4 tâches, T = 4), il n'y avait donc que **16 paires (tâche, pas) indépendantes**, tirées à 5 % : probabilité qu'aucune ne soit retenue = 0,95¹⁶ ≈ **0,44**. Le rejeu du tirage sur le manifeste d'E3 bis (`runs/20261108-065822-t06-reel/manifeste.json`, `e9f0cbb4…`) le confirme : 0 pas retenu sur 16 (plus petit tirage 0,075). Le « 0 action contrôlée dans les six états » est l'issue la plus probable du tirage, pas un défaut du code ; mais il laisse la garde version 3 (99ᵉ centile) **jamais exercée avec adaptateurs injectés** (aucune action contrôlée dans les six états d'évaluation, dose 0 injectée comprise) ; sur la carte, elle n'a lu que 6 actions du modèle de base pendant la génération des données de distillation (3 paires sur 60, rejeu du tirage sur le manifeste d'E3 bis `e9f0cbb4…`), sans arrêt, contrôle négatif « non concluant ». La course (64 tâches, T = 10 : 640 paires, ≈ 32 contrôlées, probabilité de moins de 10 ≈ 10⁻⁶) la jouera à dose 1 dans tous les états.

Seconde cause du point E3-6 : l'extracteur v1 (`scripts/extraire_mesures_epreuve_t06_v1.py` l. 39, 54) lit `etats[<état>].equivalence`, clé que la chaîne n'écrit jamais (`etats` ne porte que `adaptateur`, `dose`, `empreinte`) ; le bloc était « absent » quel que soit le tirage (§ 4).

Ce que la garde fait (`src/controle_ia/harnais/episode.py` ; code de la garde identique à l'octet à `7822a65b`, branche `prep/t06-course-v12`, et à `a5c0e298`, tête de la branche d'E3 bis dont le run a joué `c01d29ea` ; vérifié par `git diff --stat a5c0e298 7822a65b`) : pour chaque action retenue, (1) **équivalence** : les activations captées pendant la génération et celles d'une passe unique sur l'épisode complet doivent coïncider à chaque couche, 99ᵉ centile de l'écart < tolérance, sinon `GardeArret` immédiat (« activations de génération ≠ passe unique ») ; (2) **contrôle négatif de phase** : décalée d'un jeton dans la zone générée, la même comparaison doit **dépasser** la tolérance pour ≥ 95 % des actions comparables (≥ 4 positions) ; sous 10 actions comparables la phase est « non concluant » et rien ne s'arrête. Le galop doit montrer le sens « passage » sur la carte avec adaptateurs injectés ; le sens « arrêt » est montré par les essais processeur (§ 3).

## 1. Cadre

| Élément | Valeur |
|---|---|
| Chaîne | **La chaîne v12 n'accepte que GO-2026-11-06-01 et GO-2026-11-07-08** (`scripts/lancer_t06_v12.sh` l. 82–84 et 156 ; `session_v11.py` l. 24–37 ; `configuration_v5.py` l. 16–38, plafond d'épreuve ≤ 8 USD ; `amorce_instance_t06_v10.sh` l. 233–239) : E3 ter se joue sur une chaîne v13 (`scripts/lancer_t06_v13.sh`, `src/controle_ia/t06/session_v12.py`, `configuration_v6.py`, `scripts/amorce_instance_t06_v11.sh`, noms neufs) dont la seule différence est la ligne de GO, passée par `GO_ID` et vérifiée contre `registres/go.md`, le plafond d'épreuve étant celui de la ligne ; écrite par un développeur et contre-lue (R2) avant le scellement de cet ordre : `<<COMMIT_V13>>` |
| Code (commit d'épreuve) | `<<COMMIT_E3TER>>` sur une branche `prep/t06-e3ter-v1` (`T06_BRANCHE_CODE`) = `7822a65b` + chaîne v13 contre-lue (`<<COMMIT_V13>>`) + la configuration et son compagnon + `registres/go.md` portant la ligne `<<GO_E3TER>>`, rien d'autre (vérifié par `git diff --name-only`, comme `c01d29ea` pour E3 bis) ; code de la garde identique à celui d'E3 bis |
| Branche poussée (R12) | `essai/t06-e3ter-v1` = `T06_BRANCHE`, branche poussée par l'instance (`lancer_t06_v12.sh` l. 185 : `essai/…` exigé) ; jamais `main`, jamais une branche de la course ; une branche `essai/…` neuve par instance si plusieurs instances (R12) |
| Carte | A100 SXM4 80 Go ; **prix relevé le plus bas d'abord** : `prix_max_usd_h` 1,30 pendant une fenêtre (A100 relevées du 27 octobre au 3 novembre : 1,18–1,21, `registres/depenses.md` l. 209, 321, 325 ; borne de la course), puis 2,10 si aucune offre (E3 bis : 2,069) ; mêmes seuils d'offre que `config-t06-epreuve-e3bis-v3.json` ; étiquette d'offre neuve `t06-e3ter` |
| GO | ligne séparée de `registres/go.md`, type calcul, à créer par la mère sous GO-2026-11-08-05 **avant son échéance (8 novembre ≈ 18:09Z)** : `<<GO_E3TER>>`, plafond **16 USD** (§ 8) |
| Dépense antérieure | `T06_DEPENSE_EPREUVES_ANTERIEURES_USD` = dépense déjà imputée **à la ligne d'E3 ter** : **0** (ligne séparée ; E2 0,627 + E3 1,465 + E3 bis 3,652 = 5,744 USD restent sous GO-2026-11-06-01 et GO-2026-11-07-08, `registres/depenses.md` l. 385, 387, 390) ; pour une seconde instance d'E3 ter, la facture relevée des précédentes |
| Mode | `reel`, `PREREG_ABSENT=1` (galop, pas d'expérience décisive), `T06_TESTS_ARGS` **non défini**, `T06_TESTS_ATTENDUS` vide |
| Pièces interdites | aucune pièce scellée de la course n'est touchée ; `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` jamais lus |

## 2. Dimensionnement retenu

**Une seule configuration** (l'amorce ne joue qu'une configuration par instance), dérivée de `config-t06-epreuve-e3bis-v3.json` (mêmes 4 tâches d'évaluation `e4b3179a…`, 3 tâches de distillation `74567f99…`, mêmes six états S25/S50/S75/S100/T100/dose 0, lot 8, `max_nouveaux` 400) :

| Fichier à créer (`docs/notes/g0-deux-semaines-v1/e3-ter-v1/`, avec compagnon `.sha256`, sur `prep/t06-e3ter-v1`) | T | `fraction_equivalence` | `tolerance_equivalence` | Rôle |
|---|---|---|---|---|
| `config-t06-epreuve-e3ter-v1.json` | **10** | **0,5** | 0,2 | cas sain |

Autres champs : `go_id` = `<<GO_E3TER>>`, `plafond_usd` = **16**, `calendrier.fin_go_utc` = échéance de la ligne `<<FIN_GO_E3TER>>` (l'amorce l'exige égale, `lancer_t06_v12.sh` l. 166, 194 ; amorce l. 392–396), `dernier_jour_creation` = aujourd'hui ou demain, `carte.course.prix_max_usd_h` 1,30 (puis 2,10 par une v2 de la configuration si la fenêtre échoue, R12), `offre.etiquette` `t06-e3ter`, `statistique_equivalence` `q99`, `actions_min_controle_negatif` 10, `positions_min_controle_negatif` 4, `fraction_min_controle_negatif` 0,95 (inchangés : valeurs de la course). `pas_declares` 45 reste juste à T = 10 (unité « transcription »).

**Pourquoi T = 10 et non 4** : T est celui de la course (`config-t06-reel-v1-brouillon5.json`) ; les contextes longs sont ce qui met la passe unique et le contrôle négatif à l'épreuve, et avec T = 4 le tirage à 0,5 ne retient que 8 paires en espérance (probabilité d'en avoir moins de 10 : 0,77 → « non concluant » presque sûr). **Pourquoi 0,5 et non 0,05** : la fraction ne change que la densité de l'échantillon, pas le chemin de code ; au taux de la course il faudrait ≈ 30 tâches × T = 10 (probabilité de moins de 10 : 0,065 ; ≈ 6 h de carte), ce que la course elle-même fera avec ses 64 tâches.

Attendus du tirage (les graines sont tirées **sur l'instance**, `lanceur_v5.py` l. 175–180 : le tirage d'E3 ter n'est pas connu avant la création) :

| Phase | Paires (tâche, pas) indépendantes | Actions contrôlées attendues | Probabilité de moins de 10 contrôlées (borne basse du risque « non concluant » : les courtes s'en retirent) |
|---|---|---|---|
| chaque état dosé (S25…T100) | 4 × 10 = 40 (les mêmes dans chaque état) | 20 | ≈ 3·10⁻⁴ |
| dose 0 (4 conditions) | 40 (× 4 conditions = 160 actions) | 80 | ≈ 0 |
| données de distillation (3 tâches × 5 épisodes × 2 conditions) | 15 générateurs × 10 = 150 (les mêmes dans les deux conditions) | 75 paires, 150 actions | ≈ 0 |

Volume : 36 épisodes d'évaluation × 10 = 360 actions, 30 épisodes de distillation × 10 = 300 actions ; E3 bis en avait 144 + 120 à T = 4. Le critère de R-1825 (≥ 5 attendues par état) est tenu avec 20.

## 3. R5 : cas sain sur carte, artefacts par les essais processeur (option D, R-1840)

- **Cas sain** (carte) : sens « passage » des deux sous-gardes, avec adaptateurs injectés, à T = 10 : attendu « conforme » pour les six états d'évaluation et pour la distillation ; ou l'un des deux arrêts lus d'avance au § 6.
- **Artefacts** (processeur, joués **sur l'instance même** par la suite ciblée obligatoire avant le run, liste `scripts/tests-cibles-t06-v2.txt`, empreinte `417f637e…` écrite en dur dans l'amorce l. 469) : `tests/test_harnais_lots.py` — `test_garde_d_equivalence_sur_relecture_desalignee` (l. 93 : inéquivalence réelle → arrêt), `test_controle_negatif_zone_generee_artefact` (l. 103), `test_controle_negatif_de_phase` (l. 127), `test_controle_negatif_sain_et_aveugle` (l. 169 : les deux sens), `test_defaut_d1_injecte_dans_les_positions_decodees` (l. 177). Le compte rendu cite la dernière ligne de la suite (« N passed in … s ») : un échec de la suite arrête l'instance avant le run (amorce l. 468–488).
- **Limites écrites** : les essais processeur éprouvent le comparateur et le câblage de l'arrêt, pas l'arrêt observé sur la carte à adaptateurs injectés ; seul le cas sain exerce cette phase, dans le sens « passage ». Un arrêt observé sur carte (configurations `tolerance_equivalence` 10⁻⁹ et 10⁶, option B de cl1 : une instance par configuration, ≈ 32 USD) reste possible plus tard, sur devis et nœud ; il n'est pas dans cet ordre.

## 4. Ce que l'on lit, ce que l'on ne lit pas

**Lu** (script de lecture sur processeur, après scellement du `diag/` du run) : dans `diag/<run>/episodes-t06.json`, `fiches[k].equivalence` **regroupées par `fiches[k].phase`** (l'extracteur v1, l. 39 et 54, lit `etats[<état>].equivalence`, clé que la chaîne n'écrit jamais : `etats` ne porte que `adaptateur`, `dose`, `empreinte`, `t06/lanceur.py` l. 250–251 ; à ne pas utiliser) : nombre d'actions contrôlées (`len(equivalence.actions)`), plus grand `ecarts_q99` et plus grand `ecarts` par couche, tolérance ; `controles_negatifs[<état>]` de `episodes-t06.json` (`comparables`, `passent`, `courtes`, `echecs`, `fraction`, `min_des_maxima`, `lecture`) ; pour la distillation, `diag/<run>/distillation-t06.json` → `controle_negatif_donnees` seul (la chaîne n'y écrit aucun écart par action : on rapporte `comparables + courtes` comme nombre d'actions contrôlées, et l'absence d'arrêt) ; script de lecture neuf `scripts/extraire_garde_equivalence_t06_v1.py`, lecture de ces seules clés, essais sur un `diag/` factice (cas sain et artefact, R5), écrit et contre-lu avant la création. En cas d'arrêt : `diag/<run>/arret.json`, message, phase. Durée et dépense.

**Non lu** : sondes, aires, test croisé, couples descriptifs, coûts par condition, textes des épisodes, tout ce qui regarde P3 ou H1. Le galop n'est pas une expérience : lire un signal y serait un run visant un signe (R3). Le `diag/` entier est scellé et gardé sur la branche d'essai ; seul l'extrait de la garde entre au compte rendu.

## 5. Étapes (fille d'exécution)

0. **Préalables de la mère** (avant d'ouvrir la fille) : chaîne v13 contre-lue (`<<COMMIT_V13>>`) ; branche `prep/t06-e3ter-v1` avec la configuration, son compagnon et la ligne `<<GO_E3TER>>` dans `registres/go.md` (`<<COMMIT_E3TER>>`, ancêtre de `refs/remotes/origin/prep/t06-e3ter-v1`) ; script de lecture `extraire_garde_equivalence_t06_v1.py` écrit et contre-lu ; cet ordre scellé.
1. **Contrôles** : `W=$(mktemp -d)` ; `env -i … T06_BRANCHE_CODE=prep/t06-e3ter-v1 T06_REGISTRE_GO="$REGGO" T06_DEPENSE_EPREUVES_ANTERIEURES_USD=0 T06_BRANCHE=essai/t06-e3ter-v1 bash scripts/lancer_t06_v13.sh controles-epreuve "$W/e3ter" "$COMMIT" "$CFG"` (`$REGGO` : registre d'un clone de `main`, obligatoire ; `$COMMIT` = `<<COMMIT_E3TER>>` ; `$CFG` = chemin de la configuration) → attendu : code 0, « CONTRÔLES D'ÉPREUVE CONFORMES … plafond de l'épreuve 16 USD … mode reel ». Tout autre code → arrêt.
2. **Création**, sur le modèle des étapes 1 à 4 de l'ordre scellé d'E3 bis (`docs/procedures/ordre-fille-6-t06-e3bis-v3.md` l. 40–50) : `env -i … VAST="$VAST" T06_REGISTRE_GO="$REGGO" T06_DEPENSE_EPREUVES_ANTERIEURES_USD=0 T06_BRANCHE=essai/t06-e3ter-v1 T06_TESTS_ATTENDUS= bash scripts/lancer_t06_v13.sh creation auto course 0 "$W/e3ter"` qui IMPRIME la commande (garde de calcul rejouée, `GO_ID=<<GO_E3TER>>`) ; la fille l'exécute **une seule fois**, sans valeur de clé affichée ; `apres-creation` est appelé par cette commande ; puis `surveillance <ID> "$W/e3ter"` en tâche de fond. Le « 0 » positionnel est la dépense des tentatives antérieures d'E3 ter elle-même (0 pour la première ; jamais 0 pour une relance accordée par la mère). Aucune offre à 1,30 : compte rendu à la mère, qui décide de la v2 de la configuration à 2,10 (pas de relance de la fille seule).
3. **Suite de tests ciblée sur l'instance** : jouée d'office par l'amorce avant le run (liste `scripts/tests-cibles-t06-v2.txt`, empreinte `417f637e…` écrite en dur, l. 469) ; jamais jouée à ce jour sur une carte (E3 bis a joué la liste v1, 1878 essais en 4009,6 s) ; `T06_TESTS_ATTENDUS` vide : la dernière ligne est relevée et citée au compte rendu ; ≈ 1,1 à 1,3 h par instance, comptée au devis.
4. **Cas sain** : surveillance par le journal (`PROGRES … etape=episodes phase=… actions=…`) ; aucune lecture de résultat pendant le run ; l'amorce arrête l'instance en fin de run (« fin du run », code 0) ou sur arrêt consigné (code 1), traces poussées sur `essai/t06-e3ter-v1`.
5. **Vérification du rapatriement** : branche `essai/t06-e3ter-v1` poussée par l'instance (`git fetch origin essai/t06-e3ter-v1`, refspec explicite) ; `diag/<run>`, `runs/<run>/manifeste.json`, journal, `lancement.txt`, compagnons `.sha256` présents et vérifiés (`verifier-arbre`).
6. **Destruction par identifiant** (R10) si l'amorce ne l'a pas déjà faite, dès le rapatriement vérifié ; inventaire avant et après par champs filtrés de `vastai show instances --raw` (identifiant, étiquette, état, prix, durée), **jamais le brut affiché** (il imprime des variables secrètes) ; instances 58936096, 58936099, 58936100 jamais touchées.
7. **Lecture** (§ 4) sur processeur, à partir des pièces scellées, par `scripts/extraire_garde_equivalence_t06_v1.py` ; **compte rendu** (§ 7).

Consignes permanentes : clés par leur nom seulement (`VAST_API_KEY`), jamais `env`/`printenv`/`set`/`export -p`/`/proc/*/environ` (hors le `env -i …` des commandes de la chaîne, sans affichage) ; garde des secrets à 0 avant tout commit ; `git fetch` toujours avec refspec explicite ; aucun appel de modèle, aucune autre dépense ; la fille n'engage aucune dépense sans le mot écrit de Lazar **dans sa propre session** (GO-2026-11-08-05, `registres/go.md` l. 276 ; R-1819) — sauf si elle est la fille clés 2 et agit avant ≈ 21:34Z sous GO-2026-11-08-09 (l. 280), sur cet ordre scellé et la ligne de GO inscrite ; la ligne d'E3 ter est inscrite par la mère avant l'échéance de GO-2026-11-08-05 (8 novembre ≈ 18:09Z).

## 6. Arrêts

- Offre hors seuils, carte autre que l'A100 80 Go, prix > `prix_max_usd_h` de la configuration : pas de création.
- Dépense relevée > plafond de la ligne (16) : la garde de dépense de la chaîne arrête ; destruction par identifiant, compte rendu.
- `GardeArret` sur le **cas sain** : arrêt du galop, sans relance ; c'est un résultat, rapporté avec le message et la phase. Deux lectures écrites d'avance : (i) « activations de génération ≠ passe unique » : inéquivalence réelle à la tolérance 0,2 (défaut de la chaîne ou de la tolérance) ; (ii) « aveugle au décalage d'un jeton » : le 99ᵉ centile du contrôle négatif ne voit pas le décalage sur les actions courtes à contexte long (`activations.py` l. 157–160, 171–173 : le centile est pris sur le contexte non décalé suivi de la zone générée décalée ; à T = 10 une action d'au moins 4 positions décodées mais courte devant son contexte peut « échouer » ; si plus de 5 % des comparables d'une phase sont dans ce cas, la phase s'arrête) ; on rapporte alors `echecs`, `comparables`, `courtes`, `min_des_maxima` ; dans les deux cas la course (T = 10) est bloquée jusqu'à nœud. Ce second arrêt n'est pas un défaut du galop : c'est exactement ce que la course rencontrerait.
- Suite ciblée en échec sur l'instance : l'amorce arrête avant le run ; compte rendu avec la ligne d'échec, sans relance.
- Toute lecture d'un champ hors § 4 : à consigner comme écart.
- Aucune coupe au temps : la garde de dépense de la chaîne (plafond de la configuration) arrête ; durée de carte au-delà du pire cas du devis : compte rendu à la mère, sans destruction hors de cette garde.

## 7. Compte rendu de la fille (nombres seuls, ≤ 300 mots)

Pour les six états d'évaluation : actions contrôlées, écart q99 maximal par couche (et écart maximal), tolérance, `comparables`/`passent`/`courtes`/`fraction`/`min_des_maxima`/`lecture` ; pour la distillation, bilan seul (`controle_negatif_donnees`) et absence d'arrêt. Dernière ligne de la suite ciblée. Arrêt oui/non, message, phase. Prix de l'offre retenue, durée de carte, dépense relevée (carte, stockage, téléchargement), identifiant d'instance créé et détruit, commit de la branche d'essai, empreintes des `diag/`. Écarts à l'ordre. Rien d'autre.

## 8. Devis (option D)

Bases relevées (E3 bis, `registres/depenses.md` l. 390 et journal) : carte 1,729 h à 2,000 USD/h, stockage 1,810 h à 0,069, téléchargement 17,3 Go à 0,004 ; instance 05:47:22 → 07:35:36 (1,80 h) ; installation ≈ 4 min ; suite 1,11 h ; run 0,56 h pour 264 actions à T = 4 (données de distillation 6,4 min, adaptateurs 2,5 min, épisodes 11,4 min, test croisé et couples 12,3 min ; la lecture du coût a pris moins de 4 s). À T = 10 (660 actions, contextes plus longs) : run du cas sain ≈ 1,4 à 1,9 h (facteur 2,5 sur les actions, 1 à 1,6 sur la longueur). La configuration permet jusqu'à 40 Go à 0,03 USD/Go de téléchargement (1,2 USD au pire).

| Poste | Heures | USD à 1,30 USD/h | USD à 2,07 USD/h |
|---|---|---|---|
| Installation, téléchargement du modèle | 0,1 | 0,1 | 0,2 |
| Suite ciblée (liste v2, d'office) | 1,1–1,3 | 1,4–1,7 | 2,3–2,7 |
| Cas sain (660 actions à T = 10) | 1,4–1,9 | 1,8–2,5 | 2,9–3,9 |
| Stockage, téléchargement | — | 0,3 | 0,3 |
| **Attendu** | 2,7–3,2 h | **≈ 4 à 4,5** | **≈ 6 à 7** |
| Pire cas (hôte 2× plus lent, 2,10 USD/h, téléchargement au maximum) | ≈ 6,4 h | | ≈ 15 |
| **Plafond de la ligne `<<GO_E3TER>>`** | | | **16** |

Dépense antérieure comptée 0 (ligne séparée). Une seconde instance (fenêtre à 1,30 sans offre puis v2 à 2,10, ou relance) reste dans le plafond 16 seulement si la première n'a rien dépensé ; sinon ligne nouvelle sur devis.

## 9. Ce qui suit le galop

1. La mère relit le compte rendu et les pièces scellées ; elle écrit la ligne de `registres/decisions.md` qui établit le règlement d'E3-6 (six états : actions contrôlées, écart q99 maximal, tolérance, lecture du contrôle négatif ; distillation : bilan ; essais processeur d'artefact joués sur l'instance : dernière ligne de la suite ; référence à ce galop, commit et empreintes).
2. Elle remplit `<<REGLEMENT_E3_6>>` de l'ordre de course par le numéro de cette ligne (`grep -c '^| <numéro> |'` = 1 dans le registre de `main`), avec `<<COMMIT_COURSE>>`, `<<CONFIG_COURSE>>`, `<<EMPREINTE_PREREG_T06>>`.
3. Seconde contre-lecture de l'ordre rempli (R2, lecteur neuf), scellement du candidat 12, puis création de la course sous GO-2026-11-02-28 (carte GO-2026-11-07-02).
4. Si le cas sain s'arrête (§ 6, lecture (i) ou (ii)) : pas de course ; nœud de Lazar (tolérance, règle du contrôle négatif à T = 10, ou développeur sur le lanceur, nouvelle version R12, nouveau galop sur devis).

## 10. Marqueurs restants (à remplir par la mère avant la seconde contre-lecture)

`<<COMMIT_V13>>` (chaîne v13 contre-lue) ; `<<COMMIT_E3TER>>` (commit d'épreuve sur `prep/t06-e3ter-v1`) ; `<<GO_E3TER>>` (ligne de GO, plafond 16) ; `<<FIN_GO_E3TER>>` (échéance de la ligne = `calendrier.fin_go_utc`). Le marqueur `<<REGLEMENT_E3_6>>` appartient à l'ordre de course, non à celui-ci.

## 11. Couples de la contre-lecture cl1 appliqués (ancien → nouveau)

| Remarque | Sévérité | Où (brouillon 2) | Application |
|---|---|---|---|
| CLE3T-01 | bloquant | § 1 « Chaîne » | couple appliqué : chaîne v13 (`lancer_t06_v13.sh`, `session_v12`, `configuration_v6`, `amorce_instance_t06_v11.sh`), `<<COMMIT_V13>>` ; option (a) retenue par la mère (R-1840) |
| CLE3T-02 | bloquant | § 2, § 3, § 5 étape 3 | une configuration par instance ; couple l. 67 appliqué (suite d'office, liste v2 `417f637e…`, `T06_TESTS_ATTENDUS` vide) ; le choix laissé à la mère résolu en **D** : artefacts hors carte, tenus par les essais processeur |
| CLE3T-03 | bloquant | § 0, § 1 « Code », « Branche poussée » | trois couples appliqués (garde identique à l'octet `a5c0e298`/`7822a65b`, E3 bis a joué `c01d29ea` ; `<<COMMIT_E3TER>>` sur `prep/t06-e3ter-v1` ; `essai/t06-e3ter-v1` = branche poussée) |
| CLE3T-04 | majeur | § 1 « Dépense antérieure », § 8 | couple appliqué : 0 pour la ligne séparée (5,744 restent sous les deux lignes d'épreuve) |
| CLE3T-05 | majeur | § 0 | couple appliqué : « jamais exercée avec adaptateurs injectés » ; 6 actions du modèle de base à E3 bis |
| CLE3T-06 | majeur | § 0, § 4, § 7 | couple l. 58 appliqué (clés exactes, `distillation-t06.json` → `controle_negatif_donnees`, script `extraire_garde_equivalence_t06_v1.py` contre-lu) ; compte rendu : six états + bilan de la distillation |
| CLE3T-07 | majeur | § 6, § 3, § 9 | couple l. 80 appliqué : deux lectures écrites d'avance ; « conforme attendu » nuancé |
| CLE3T-08 | majeur | § 5 étapes 1–2 | couple l. 66 appliqué : commandes `controles-epreuve` / `creation auto course 0` / `surveillance`, variables `T06_*`, `$REGGO` |
| CLE3T-09 | majeur | § 8 | devis refait sur les bases d'E3 bis, option D, suite comptée, plafond 16, prix 1,30 puis 2,10 |
| CLE3T-10 | majeur | § 5 consignes, § 1 « GO » | couple l. 74 appliqué : mot de Lazar dans la session de la fille (R-1819), exception fille clés 2 sous GO-2026-11-08-09, ligne inscrite avant 18:09Z |
| CLE3T-11 | mineur | § 2 tableau | couple appliqué : 75 paires, 150 actions |
| CLE3T-12 | mineur | § 2 tableau | couple appliqué : « moins de 10 contrôlées (borne basse …) » |
| CLE3T-13 | mineur | § 0 | message exact « activations de génération ≠ passe unique » ; artefact 1 retiré de la carte (D) |
| CLE3T-14 | mineur | § 3, § 6 | artefacts sur carte retirés (D) ; `arret.json` et « arrêt consigné pendant le run » repris pour le cas sain |
| CLE3T-15 | mineur | § 6 | couple appliqué : aucune coupe au temps |
| CLE3T-16 | mineur | § 5 étape 6 | outil hors dépôt supprimé ; inventaire par champs filtrés de `vastai show instances --raw`, jamais le brut affiché |
| CLE3T-17 | mineur | en-tête | couple appliqué : « reçu du sous-agent rédacteur » ; (R-1769 ; R-1784 ; R-1825, point 4) ; la référence « B1 » et le renvoi erroné à l'amendement de l'étiqueteur supprimés |
| CLE3T-18 | mineur | § 1 « Carte », § 2, § 8 | prix 1,30 d'abord puis 2,10 ; étiquette `t06-e3ter` |

Points `<<À VÉRIFIER>>` du brouillon 1 : tous résolus par la cl1 (§ 4 de la contre-lecture) ou par R-1840 ; aucun ne subsiste.
