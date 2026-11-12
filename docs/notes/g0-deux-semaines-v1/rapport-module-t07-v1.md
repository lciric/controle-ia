# Rapport du développeur — module de lecture de T0.7 `src/controle_ia/t07/`, v1

- Écrit le 2026-11-08, de 16:31 à 18:00 UTC environ (`date -u`), par un développeur neuf (Claude, sous-agent de la session mère :
  Fable 5.1 jusqu'à 17:43, Opus 5.5 ensuite, selon ce qu'affiche la session) qui n'a écrit ni les brouillons de T0.7, ni les
  contre-lectures, ni T0.6, ni P3. Aucun fichier existant modifié. Aucun compagnon `.sha256` écrit (la consigne l'interdit) : ce
  rapport n'est donc pas scellé, et `verifier-arbre` le signale tant que la session mère ne l'a pas scellé. Aucun commit, aucune
  poussée par le développeur (les fichiers apparaissent dans les instantanés automatiques de la session mère, « Instantanés en cours
  des sous-agents », que le développeur n'a pas commandés). Aucune dépense. Aucune lecture de données réelles (`diag/`, `donnees/`,
  bras d'attaque, mode tenu à l'écart) : le module n'est éprouvé que sur des données factices.
- **Texte suivi : le brouillon 9** `brouillons/T0.7-sondes-v0-v1-brouillon9.md`
  (`f43143f29cf1b5769c6bf3493b86114e3199f89dc1ab3b73c6dbe7f238b8c4db`), sections « Module de lecture », « Critères de lecture
  gelés », « Lignes de registre », « Seuil », et son annexe `brouillons/T0.7-sondes-v0-v1-brouillon9-pieces/grille_l_t07_brouillon9.py`
  (`116fe0722a2fe5e80f9ad1d91d160f2ac9609729c5b1d8669abc8537e45d0838`, sortie `bcd45aae5ab10003b3bb49a49ea96b47f9c39394377b444c6dc680d0d3db26cc`) ;
  plus la décision **N-063 v2** (`docs/decisions/decision-N-063-v2.md`). Le travail a commencé sur le brouillon 7 (`5b3a9568…`),
  puis a été réaligné sur le brouillon 8 (`33954acd…`) sur ordre de la session mère, puis sur N-063 en format provisoire, et enfin
  sur le brouillon 9 dès qu'il est paru sur disque. Le format provisoire `{dose: issue_base}` et l'issue « SANS-OBJET » placée
  avant L0a sont **remplacés** par l'entrée Q et les lignes L7 et L7b du brouillon 9.
- Code existant réutilisé tel quel (aucun module gelé touché, R12) : `src/controle_ia/sondes/` (`evaluation.plancher_apparie`,
  `scores_actions`, `aire_sous_courbe`, `intervalle_blocs`, et `comparer_au_plancher` pour l'essai d'égalité), `harnais/sondes.score_action`,
  `premier_test_ia.figees.lire_sondes`, `premier_test_ia.statistiques` (`detection`, `aire_simple`), `manifeste` (`creer_manifeste`,
  `ecrire_resultat`, `verifier_resultat`, `generateur`), `scellement`, `gardes`. Modèles lus mais non importés : `scripts/controle_lecture_t06_v1.py`
  (`ba2ba5cfe7484e7e30bb74e44420b46c9939dd5613bbb961b9725c3d46343c07`, récupéré par `git fetch origin prep/t06-candidat8-v1:…`),
  `scripts/extraire_garde_equivalence_t06_v1.py` (forme de `_exiger`), et, au commit `8cb539f9` (`git show`),
  `src/controle_ia/sondes/familles_v2.py` (`4fea2c52…`) ainsi que `src/controle_ia/t06/` (`cout.py` `bcfe5683…`, `lecture_v2.py`,
  `test_croise.py`, `lanceur*.py`, `identite.py`).

## 1. Fichiers neufs et empreintes (`sha256sum`, 2026-11-08 17:56 UTC)

| fichier | sha256 | lignes | rôle |
|---|---|---|---|
| `src/controle_ia/t07/__init__.py` | `b58e80bad3b39aa5cb6708d33065837d6882a02c60bf9f3ab91ca9df908cc432` | 21 | présentation du module |
| `src/controle_ia/t07/registre_v1.py` | `327658836abe3efb1a758432e18fb2a76b24db2321dea32f5a3572a6f9eedf54` | 230 | `lire_registre_t07(registre, cles_exigees, cles_permises)` au format exact de `controle_lecture_t06_v1` ; `verifier_lignes` (antériorité stricte, sceaux, extrait de GO égal à une ligne de `registres/go.md`) ; `exiger_anteriorite` (`SCORES-T07` et `SONDES-T07` avant `VERDICT-P3BIS`) ; `garde_ouverture`, `journaliser_ouverture`, `ajouter_ligne` ; clés exigées et permises par étape ; registre `registres/scellements-v1.md` |
| `src/controle_ia/t07/criteres_v1.py` | `2a68b975d0195d145d872a4e442fd8ed9959618bb6c7b504d604ca1fedfae53d` | 312 | grille gelée du brouillon 9 : `regles` et `agreger_doses` (même texte que l'annexe), ordre R11-arret, R12-invalide, L0a, L0b, L0c, L1, L1b, L7, L7b, L6, L4, L4b, L5, L2, L3 ; `etat_pour_sonde` (règle L05) ; `etat_organisme` (U, N, Z, E) ; `lit_i` et `lit_ii` (quels organismes sont lus pour le critère sur chaque chemin) ; `issue_critere_3` (phrases gelées, sous-phrase de L1b nommée, sept entrées imprimées) ; `enumerer_couverture` (46 080 cas plus 624 agrégations) |
| `src/controle_ia/t07/mahalanobis_v1.py` | `ad668bc36a70157bf4abc67c0798347304ac816b7a0f94a3e9435ffd7c052fd3` | 89 | miroir de `sondes/familles_v2.py` (absent de `main`) : `SondeMahalanobisV2` (`produit_matriciel_v2`), `verifier_egalite_au_paquet_gele` (256 jetons, écart ≤ 10⁻¹²), `preparer_sonde` (un échec met le couple en « échec », jamais l'ensemble) |
| `src/controle_ia/t07/plancher_v1.py` | `ac6e8263293ed30c807ef91f8eab0adbcbf8e1b91d5e4c56e73dbffa1a7099dc` | 129 | `niveau_bonferroni` (1 − 0,05/n, n ∈ {2, 3, 4}) ; `exiger_agregation` (maximum ou attention, N-026) ; `plancher_pour_sonde` (200 directions appariées en covariance, recette gelée) ; `noter_actions`, `scores_plancher`, `predicteurs_triviaux` ; `comparer` (sur séquences) et **`comparer_scores_au_plancher`** (sur scores seuls, CLT7B-05) |
| `src/controle_ia/t07/lecture_v1.py` | `da2219ccc1970e8997c8c06f7ff55f51eada773be7cf1e606adca3708233585b` | 758 | `etape_a` : ouverture ; `sondes_lues` dérivée des lignes de jeux (repli en huit cas) ; `sondes-t07.json` écrit avant toute notation ; garde d'identité au bit près ; notation ; `scores-actions-t07.npz` scellé ; lignes `SCORES-T07` et `SONDES-T07`. `etape_b` : antériorité ; **filtre par dose** (`lire_issue_mots_et_cout`, `filtrer_doses_qualifiees`) ; entrées G, P, A, Q, F ; lectures décisives de (i-a) et des doses qualifiées ; doses hors jugement en descriptif ; agrégation ; issue. Commande `python -m controle_ia.t07.lecture_v1 etape-a | etape-b | repli-recalcul | grille`, codes 0, 2, 3 et 4 (L7) |
| `tests/test_t07_lecture_v1.py` | `80dcf89f37c443290fd3bfca082987f20826ea12a481b48888c04120ccc0b275` | 894 | 67 essais (section 2) |

Empreintes vérifiées pendant l'écriture et égales à celles des brouillons : `controle_lecture_t06_v1.py` `ba2ba5cf…` ; annexe du
brouillon 8 `1a9a2daa…` (sortie `c7083b0a…`) ; annexe du brouillon 9 `116fe072…` (sortie `bcd45aae…`, rejouée par `python3 -I -B` :
code 0, « GRILLE COMPLÈTE ») ; au commit `8cb539f9`, `t06/cout.py` `bcfe5683…` et `sondes/familles_v2.py` `4fea2c52…`.

## 2. Essais (R5 : chaque garde éprouvée sur un cas sain et au moins un artefact)

- Commande : `. .venv/bin/activate && PYTHONPATH=src python -m pytest -q tests/test_t07_lecture_v1.py` → **66 passés, 1 sauté**
  (67 collectés, 244 s, 2026-11-08 vers 18:00 UTC, sur les empreintes de la section 1). L'essai sauté compare le miroir à `sondes/familles_v2.py`, absent de `main` : il
  jouera quand le fichier sera fusionné. La machine est chargée (charge moyenne ≈ 8 sur 4 cœurs) : environ 4 minutes par passe.
- Suite complète du dépôt (`timeout 1500 nice -n 10 python -m pytest -q`, lancée à 17:14 UTC) : **interrompue au bout de son délai
  de 25 minutes, sans bilan** (code 143). Elle n'a pas été rejouée ; la session mère doit la rejouer.
- Le faux dossier de run reprend les clés réelles de la chaîne de T0.6 :
  - manifeste écrit par `creer_manifeste` (`config.go_id`, `couches`, `T`, `N`, `sonde.couche`…) ;
  - `diag/<run>/episodes-t06.json` (`etats`, `fiches`, `mesures`, `mesures_sha256`, `textes`, `textes_sha256`,
    `activations_sous_ensemble`, `controles_negatifs`) et `lecture-cout-t06.json` (`resultat.lecture.table_A.ligne`) ;
  - `donnees/<run>/mesures-t06.npz`, `textes-actions-t06.jsonl`, `activations/c{7,15,23}/<cle>.npy` en demi-précision, sous-ensemble
    poussé en morceaux avec son manifeste ;
  - clés d'action `f"{condition}__t{index:03d}__p{pas}"` ; conditions `honnete`, `saboteur`, `S25`, `S50`, `S75`, `S100`, `temoin` ;
  - quatre sondes figées factices ;
  - registre factice `registres/scellements-v1.md`, extrait de GO `registres/go-extraits/GO-ETAPE-A-T07-v1.md`, fichier d'issue de
    P3-bis `docs/verdicts/verdict-P3-bis-v1-issue.json`, fichier « mots et coût » **au format du brouillon 9** (`issue_mots_et_cout`,
    `phrase`, `doses.S25…S100.{base_decisive, aire, bas, haut, quantile_plancher, seuil_aire, etat}`, `doses_qualifiees`, `plis`).
- Ce que couvrent les essais :
  - **registre** : cas sain ; ligne exigée absente ; ligne en double ; clé ni exigée ni permise ; six formes fausses ; ligne non
    antérieure ; sceau faux, puis empreinte différente du registre ; extrait de GO qui n'est pas une ligne de `go.md` ; antériorité
    de `SCORES-T07` et `SONDES-T07` sur `VERDICT-P3BIS` ; **refus identiques à ceux de `controle_lecture_t06_v1.lire_registre`** sur
    sept registres (clés communes `SCELLEMENT-T07` et `SCELLEMENT-P3BIS`) ;
  - **critères** : **`regles` et première ligne égales à l'annexe du brouillon 9 sur les 46 080 cas** ; **`agreger_doses` égale à
    l'annexe sur les 624 combinaisons**, et les exemples du texte ((U, U, Z) → Z, (U, E) → E, (U, N) → N, (U, U) → U) ; effectifs de
    la couverture égaux à la sortie de l'annexe (L7 128, L7b 128, L6 192, L4 16, L4b 20, L5 20, L2 4, L3 4) ; issues sans lecture
    (L0a, L0b, L0c, L1 par A ou par Q absente, L7, L7b, R11, R12) et avec lecture (L1b et ses sous-phrases, L6, L4, L4b, L5, L2, L3) ;
    sous M1, un état de dose transmis pour (ii) arrête ; entrées hors grille → arrêt ;
  - **Mahalanobis v2** : égalité à 10⁻¹² près ; sonde altérée → couple en « échec » ; calcul inconnu → arrêt ;
  - **plancher** : niveaux de Bonferroni ; agrégation « moyenne » → arrêt ; **`comparer_scores_au_plancher` égale à
    `comparer_au_plancher` à 10⁻¹² près** sur le jouet ; forme fausse → arrêt ;
  - **lecture de bout en bout** :
    - issues : L2 (cas sain avec **deux doses qualifiées sur quatre** : `S25` et `S50` sont absentes des lectures décisives et
      présentes en descriptif, marquées « hors jugement », à 95 %) ; trois doses qualifiées ; L4 ; L3 ; L5 par prédicteur trivial ;
      L1b à A2 ; L1 à A1, à table A absente et à ligne « mots et coût » absente ; L0a quand les lignes de P3-bis manquent ou que le
      fichier d'issue est illisible ; L0b ; **L7, sans objet** (aucune aire décisive sur (ii), toutes les aires hors jugement,
      code 4) ; **L7b**, base non calculable ;
    - arrêts : champ par dose absent ; dose manquante ; `doses_qualifiees` incohérente (trois cas) ; `SCORES-T07` postérieure au
      verdict → refus ; activation absente → arrêt qui nomme la clé, avec `arret.json` ; forme fausse ; garde d'identité à un bit
      altéré ;
    - refus sans rien ouvrir ni écrire : sceau faux ; registre absent ; manifeste de 7a (« R12-invalide ») ; `RUN_T06` différent de
      la ligne ; `arret.json` de T0.6 présent à l'étape A ;
    - replis à trois et à deux sondes (niveaux 98,33 % et 97,5 %) ; `sondes_lues` changé entre les étapes A et B → refus ;
      configuration incomplète ou hors grille → arrêt ; colonne de mesures absente ou sonde absente → arrêt qui nomme la clé ;
      `lecture-sondes-t06.json` jamais ouvert ;
    - commande en ligne : codes 0, 2, 3 et 4, sous-commandes `grille` et `repli-recalcul` ;
  - **aucune moyenne ni médiane sur les jetons** (recherche dans le module : la seule médiane est celle des aires de plancher, prise
    sur les directions, comme dans le paquet gelé).

## 3. Interprétations déclarées par le développeur (à relire par le rédacteur et la contre-lecture du code)

1. **Lignes lues par la grille, et non refusées.** Le brouillon 9 déclare « exigées » à l'étape B `SCELLEMENT-P3BIS`,
   `VERDICT-P3BIS` et `ISSUE-MOTS-ET-COUT-T06`, mais sa grille donne L0a quand P manque et L1 quand Q manque. Le module les traite
   comme **permises** : quand elles manquent, il écrit l'issue L0a ou L1 (`lecture-t07.json`, code 0) au lieu de refuser (code 2,
   rien d'écrit). Seules `RUN-CONFIRMATION-T06`, `SCORES-T07` et `SONDES-T07` sont refusées si elles manquent.
2. **Fichier « mots et coût » présent mais mal formé.** Une clé absente, une valeur hors domaine, une dose manquante ou une liste
   `doses_qualifiees` incohérente donnent un **arrêt** (code 3, `arret-etape-b.json`), comme le demandent la section « Module » et la
   session mère. La grille, elle, range un « fichier illisible » dans Q = « absente » (L1). Le module réserve L1 à la ligne absente.
3. **(i-a) et (ii) lus selon le chemin de la grille** (`lit_i`, `lit_ii`) :
   - sous L1b, (i-a) est lu quelle que soit Q (pourvu qu'elle soit présente) ; (ii) n'est lu pour le critère que si Q ∈ {M2, M3} ;
   - sous L7 et L7b, ni (i-a) ni (ii) ne sont lus pour le critère : toutes les aires vont en descriptif à 95 %, marquées « hors
     jugement » ;
   - sous M4, aucune dose n'est jugeable, même si certaines « échouent » ;
   - les doses hors jugement sont lues à 95 %, sans correction, avec des graines `descriptif/<sonde>/<jeu>`.
4. **Code de sortie 4 pour L7.** Le brouillon 9 ne prévoit que 0, 2 et 3 ; la session mère a demandé un code dédié pour « sans
   objet ». Le module rend 4 : écart déclaré, à trancher.
5. **Clé ni exigée ni permise** : refusée quand elle a la forme d'une clé de registre (majuscules et tirets) suivie d'une date au
   format. Les lignes de T0.6 (`SCELLEMENT-T07`, `SCELLEMENT-P3BIS`) sont permises à toutes les étapes.
6. **Extrait de GO** : une seule ligne non vide, comparée au texte UTF-8 exact des lignes de `registres/go.md` (le saut de ligne
   final de l'extrait est ignoré).
7. **Entrée F (fuites nommées)** : lue dans un fichier scellé cité par la configuration (`audit_fuites` ; nul par défaut, ce qui donne
   « aucune »). Le brouillon ne fixe pas la source de F.
8. **Table A** : A1 à A5 sont acceptées ; un fichier ou une ligne absents donnent A = « absent » ; `arret.json` donne A = « arret »
   à l'étape B et un refus à l'étape A.
9. **Fichiers d'arrêt** : `arret.json` à l'étape A, `arret-etape-b.json` à l'étape B (R12 interdit d'écraser). Les lignes
   `SCORES-T07` et `SONDES-T07` sont datées de l'instant d'ouverture de l'étape A.
10. **Grille du brouillon 7** : un chevauchement y avait été trouvé ((i) non au-dessus et (ii) non interprétable tombaient sous L5 et
    sous L4). Les brouillons 8 et 9 le résolvent ; l'énumération du module le confirme.

## 4. Ce que le texte demande et que le module ne fait pas encore

- **Sondes neuves** (dissimulation J-D, domaine J-C, T7-P6 J-A) :
  - pas d'extraction des activations des jeux génériques (il faudrait la passe unique du harnais, le modèle et une carte
    graphique) ;
  - pas d'entraînement des 30 couples (cinq familles × trois couches), pas de validation générique (avant le champ et sur l'action
    entière), pas de règle d'ex aequo.
  - Le module lit les sondes principales **par nom** dans des fichiers scellés (`fichiers_sondes`, format `figees.ecrire_sondes`) ;
    `sondes-t07.json` le déclare.
- **Repli du recalcul des activations** (`repli-recalcul`, garde d'équivalence q99 à 0,2, relance sur la même carte) : la commande
  refuse explicitement.
- **Lectures hors critère 3** :
  - T7-P3, T7-P4 ; T7-P15 (P3-P4, T1, T3, T4 : `etiquettes_gonflement`, `aire_stratifiee`) ; T7-P6 ;
  - T7-P9 (directions des concepts) ; T7-P10 (témoins lexicaux) ; T7-P16 (base « coût seul », qui demande `t06/cout.py`, absent de
    `main`) ;
  - T7-P17 n'est couvert qu'en partie (les aires hors jugement sont rapportées, sans courbe) ; T7-P18 ; T7-P19 (placebo à
    200 permutations) ;
  - réserves R1 à R10 non écrites ; `resultat.predictions` ne porte que T7-P1 et T7-P2.
- **Audit R4** (aire > 0,95 ou < 0,05, quantile de plancher > 0,70, résultat « trop beau ») : le module ne le déclenche pas ; F est
  lue dans un fichier.
- **Contrôles non faits** :
  - disjonction des tâches de réserve et d'évaluation ;
  - complétude des épisodes par `resultat.fiches` (seul leur nombre est écrit) ;
  - lecture de `distillation-t06.json` ;
  - effectifs lisibles et illisibles du coût.
- **Empreinte canonique de la configuration** (`<<EMPREINTE_CONFIG_T07>>`) : seule la `config_sha256` du manifeste la porte.
- **Répétition jouet sur la vraie chaîne de T0.6** (`lanceur_v5`, `mode = "jouet"`) : non jouée, parce que T0.6 n'est pas sur
  `main`. Le faux run des essais imite ses clés.

## 5. Questions au rédacteur du brouillon 9

1. **Statut des lignes de l'étape B.** `SCELLEMENT-P3BIS`, `VERDICT-P3BIS` et `ISSUE-MOTS-ET-COUT-T06` sont-elles exigées (refus,
   rien d'écrit) ou lues par la grille (L0a ou L1, issue écrite) ? Le texte dit les deux.
2. **Fichier « mots et coût » mal formé.** Est-ce Q = « absente » (L1) ou un arrêt ? La grille, l. 722, et la section « Module »,
   l. 1013, divergent.
3. **Docstring de l'annexe.** Elle annonce « 4 + 16 + 64 + 256 = 340 cas » pour l'agrégation, mais le script en compte 624
   (combinaisons de doses × états), ce qui est le chiffre juste et celui du texte. Il faut corriger la docstring.
4. **Code de sortie de L7** : 0 (brouillon 9) ou un code dédié (4, demandé par la session mère) ?
5. **Doses hors jugement** : faut-il les lire au niveau de T7-P17 (95 %, sans correction, choix du module) ? Sous L7 et L7b, faut-il
   que (i-a) soit rapporté au niveau décisif ou à 95 % ?
6. **Source de l'entrée F** (fuite nommée R7a ou R9a) : ligne de registre, fichier scellé de l'audit, ou valeur de configuration ?
7. **Covariance du plancher des sondes figées.** `jetons-principales-p3.npz` (`4cd2ddb8…`) porte les **scores par jeton** des sondes
   principales de P3 (`premier_test_ia.run.tableaux_par_jeton`), pas leurs activations. La covariance Σ demande un fichier
   d'activations d'entraînement, ou un recalcul à empreinte égale : lequel ?
8. **`familles_v2.py`** : fusion sur `main` avant le scellement, ou citation au commit ? Le module en porte un miroir ; l'essai
   d'égalité à l'original est prêt et attend le fichier.
9. **Registre partagé** : une clé neuve (de T0.8, par exemple) doit-elle faire refuser T0.7 tant qu'elle n'est pas déclarée permise ?
