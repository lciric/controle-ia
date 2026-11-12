# Contre-lecture du code — addendum 2 de P3 — texte face au code — v1

**Verdict : scellable après corrections.** Le module applique le brouillon 2 phrase par phrase : chaque règle normative a
sa ligne (table plus bas). Les recalculs à la main sur un petit jeu synthétique tombent juste : `E_sf`, `D`, `E0`, la part,
`M`, les comptes, M7, M8 et `A_80`, intervalles compris (exacts par énumération ; réplique indépendante des tirages égale
au bit près). Aucun écart de nombre, de réserve ni de verrou. Deux choses restent à faire avant le scellement :

- une règle que le module a dû trancher seul, parce que le brouillon 2 se contredit (gardes 7 et 9 pour une entrée « en
  échec » ou « non calculable ») ; le brouillon 3 la tranche autrement (CC-texte-01) ;
- des tests manquent pour quatre règles écrites ; les quatre mutants qui les cassent passent les 42 tests
  (CC-texte-02 à CC-texte-04), et 28 autres `raise` du module ne sont jamais déclenchés (CC-texte-05).

Contre le brouillon 2, le code n'a pas à changer ; les tests, si. Constats : cinq mineurs, quatre pour information.

## Cadre

- Contre-lecteur : sous-agent neuf (R2), angle « texte face au code ». Je n'ai écrit ni le texte, ni le module, ni ses
  tests, ni la contre-lecture 1, ni son traitement.
- Texte qui fait foi : brouillon 2,
  `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/addendum2-p3/P3-addendum2-audit-verdict-v1-brouillon2.md`,
  sha256 `641b36c2d8b77ca78c6f9bdd151cc3a3cc38a468e4f2a307e01e94354f651615` (recalculée, égale). Lus pour le contexte :
  brouillon 1, contre-lecture 1, traitement, vérification des corrections du brouillon 2.
- Module : sha256 `0b991450d107ee16b484a568d91f95ca232b5079d42ae17b6c52ec2bd23369cf` ; tests : sha256
  `ecbb897293b690b37e0f086c86ca575b97c0a6bfedcec69f56849023afa8bfd3`, 42 tests (`def test_` compté : 42) ; notes du
  module lues. Travail sur une copie :
  `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/addendum2-p3/revue-texte/copie/` (mêmes
  empreintes). L'original n'a pas été touché.
- Code gelé lu : `lecture.py` en entier, `statistiques.py` en entier, `conditions.py`, `manifeste.py`, `prereg.py`,
  `sondes/evaluation.py`, `gardes.etat_git`, `scellement.verifier`, `harnais/validation_reelle.py` l. 55-100 et
  210-250, `run.py` l. 70-90 et 313-329. Empreintes des six modules cités en tête du texte : égales au disque.
- [PA] : liste d'arrêt, précisions, table du verrou (plan, point 5). [V] : section 7. [P] : l. 150-162.
- **Non lu** : `prereg/P3-consignes-v1.md`, tout texte d'action, toute clé ; aucune donnée du run ni sortie de lecture
  (`donnees/20261019-230011-p3-reel/`, `diag/` de ce run : jamais ouverts). **Aucune grandeur de B1 ni de B2 calculée sur
  le réel** : tous mes calculs portent sur des tables synthétiques (écrites ici, ou produites par les aides du fichier de
  tests). B3 refait seulement sur les nombres arrondis que le texte cite déjà.
- Dépôt en lecture seule : `git status --porcelain --untracked-files=all` vide avant et après chaque lancement (empreinte
  `e3b0c442…`). La tête du dépôt a avancé pendant la revue (`2dc36382…` puis `34dbf1d4…`), par une autre session.
- Suite de tests sur la copie, depuis la racine du dépôt (commande de la consigne) : **42 passed in 54.09s**.

## Phrases normatives du brouillon 2 et lignes du module

« = » : conforme ; « + » : ajout du module là où le texte se tait (sans effet sur un nombre ni une réserve) ; « CC » :
constat. Lignes : brouillon 2 (b2) et module (m).

### En-tête, entrées, statut

| phrase (b2) | lignes (m) | état |
|---|---|---|
| Entropie de P3 (l. 11) | `ENTROPIE_P3` l. 67 ; garde 1 l. 1190 ; manifeste l. 1436-1438 | = |
| Empreintes du module et des tests lues dans ce texte (l. 12-13 ; garde 1) | expressions l. 70-71 ; l. 1196-1208 | = : octets du texte en ASCII (apostrophe et espaces simples), les expressions reconnaissent les lignes une fois les marqueurs remplis |
| Table « Entrées » [MR] … [ML], empreintes citées (l. 30-42) | `ENTREES` l. 79-98 ; garde 2 l. 1216-1233 | = : neuf chemins et neuf empreintes égaux au texte (comparaison mécanique) |
| [A] et [MA] cités, non lus (l. 43-44) | absents de `ENTREES` | = |
| [J] chargé par le chargeur gelé, jamais lu ensuite ; [T] haché, jamais décodé (l. 39-40) | `charger_source` (garde 6) ; aucune lecture de `source["jetons"]` ni des textes | = (tests « tables par jeton » et « textes non UTF-8 ») |
| Code gelé réutilisé, arbre égal au commit cité (l. 46-52) | imports l. 52-60 ; `exiger_code_cite` l. 1210 | = : aucun import de `docs/procedures/P3-addendum-v1/` |
| Emplacement hors de l'arbre gelé (l. 53-56) | `CHEMIN_MODULE`, `CHEMIN_TESTS` l. 63-64 ; `docs` exclu de `CHEMINS_GELES` | = |
| Statut non décisif (l. 57) | `decisif=False` l. 1437 ; `STATUT` l. 72 | = |
| Périmètre : ni sonde, ni activation, ni texte, ni score par jeton, ni bras « moyenne » (l. 69-73) | rien de tel dans le module | = |
| Formes = booléens de l'instance, non recalculés (l. 105-107) | `_tables` l. 374-387 (colonnes booléennes de [S], `run.py` l. 327-328) | = |

### Métrique

| phrase (b2) | lignes (m) | état |
|---|---|---|
| Run source par `charger_source` (l. 147-148) | garde 6 l. 1386-1394 | = |
| Colonnes de [S] lues ; `noms_sondes`, `scores` pour la garde 7 seulement (l. 149-150) | `_tables` l. 379-387 ; l. 817-819 | = |
| [L] vérifiée par `verifier_resultat` (l. 150-151) | l. 1297 | = |
| Clés lues entrée par entrée ; `etablie` pour P3-P1 seulement ; entrée non calculable ou en échec : « non lu » (l. 151-159) | `lire_la_lecture` l. 684-752 ; `CLES_EFFET` l. 123 ; `_etat_entree` l. 231-237 | = ; + contrôle des types (l. 706-709, 728-729, 736-737) |
| `P3-P4.<p>.conforme` et `intention.<p>.T<k>.etabli` seulement si la table du verrou les consulte (l. 158-159) | l. 745-750 | = (voir CC-texte-07) |
| M1 : toutes les actions, coût lisible = fini et > 0, nuls et illisibles comptés (l. 162-164) | `lp.couts_par_tache` l. 415 ; `cout_de_tache` ; comptes de `effet_cout_apparie` | = |
| M2 : forme présente si la colonne est vraie ; « sans aucune forme » = cinq colonnes fausses (l. 166-168) | `_a_forme` l. 395-400 | = |
| M3 : NaN dans une copie de la colonne, `couts_par_tache(t_R, c, "cout_R")`, deux conditions ; comptes propres (l. 170-175) | `table_restreinte` l. 403-408 ; `couts_restreints` l. 411-415 ; `comptes_restriction` l. 418-430 | = ; + comptes `actions`, `nulles_d_origine` |
| M4 : `d_R(t)`, `E_R`, `effet_cout_apparie(…, 10 000, 0,95)`, « non calculable » sous deux tâches (l. 177-184) | `differences_par_tache` l. 433-443 ; `effet_restreint` l. 466-475 | = |
| M5 : `D`, `E0`, `part` sur `T_sf` ; une matrice ; dégénérés > 1 % : « échec » ; part descriptive ; « instable » ; libellés signés (l. 186-193) | `part_des_formes` l. 478-513 ; `libelle_D` l. 276-282 | = ; + `E0 = 0` : part « non calculable » (l. 498-499) |
| M6 : médiane des `d_∅(t)`, médiane de chaque ligne tirée ; comptes et quantiles de `d_∅` et `d_sf` (l. 195-198) | `mediane_par_tache` l. 516-534 | = |
| M7 : tâches sans forme dans les deux conditions, actions entières (l. 200-202) | `effet_taches_sans_forme` l. 537-548 | = |
| M8 : tâches avec action lisible portant `f` et action lisible sans forme ; `e(t)`, `g`, tirage (l. 204-209) | `ecart_de_forme` l. 551-573 | = |
| M9 : table par tâche, identifiants seuls (l. 211-212) | `table_par_tache` l. 576-591 | = |
| M10 : `w = (haut − bas) / 2` ; `z`, `z80` par `NormalDist` ; aire au seuil ; `A_80` ; même formule aux hypothèses écrites ; distances basse et haute ; exclusions (l. 214-232) | `quantiles_normaux` l. 644-647 ; `puissance_du_nul` l. 650-667 | = : aucune puissance à l'aire observée, aucun intervalle de `A_80`, aucune différence « seuil moins aire » |

### Analyses, règles communes, graines

| phrase (b2) | lignes (m) | état |
|---|---|---|
| B1 et B2 par la même fonction ; écarts : quatre conditions × cinq formes ; B3 : deux sondes, aucun tirage (l. 234-239) | `analyse_contraste` l. 594-625, appelée l. 1151-1152 ; `ecarts_de_forme` l. 628-639 ; `analyse_b3` l. 670-679 | = |
| Intervalles percentiles 2,5 % et 97,5 %, 10 000 tirages (l. 242-243) | `TIRAGES`, `NIVEAU` l. 102-103 ; `_intervalle` l. 240-244 | = |
| Forme absente : « sans objet », générateur non consommé (l. 244-245) | l. 618-620 ; l. 635-637 | = |
| Tâches triées ; une matrice par clé (l. 246-248) | l. 483, 520, 559 ; `_tirages_des_taches` l. 247-251 | = (réplique indépendante égale au bit près, plus bas) |
| Plancher de la garde 7 : sondes `<p>-plancher-k` de [SF] (l. 249) | l. 831 | = |
| Graines : une `SeedSequence` par clé, entropie de P3, 47 clés, ordre écrit (l. 250-258) | `cles_addendum2` l. 345-351 ; `_rng` l. 336-340 ; manifeste l. 1436-1438 | = : liste reconstruite depuis le texte seul égale à celle du module, ordre compris |
| Aucune moyenne ni médiane sur les jetons (l. 259-260) | moyennes sur les actions (`cout_de_tache`) ou sur les tâches | = |
| Forme de la sortie ; clés interdites retirées, nombres gardés (l. 261-264) | `_Controles` l. 904-925 ; `_calcul` l. 324-333 ; `_sans_cles_interdites` l. 285-291 | = |

### Seuil

| phrase (b2) | lignes (m) | état |
|---|---|---|
| Moins de deux tâches : « non calculable », contrôle « non lu » (l. 268-269) | `NonCalculable` l. 179 ; `_borne` l. 928-935 | = |
| Repères 0, log10 3 = 0,47712125471966244, `A_80_écrit_max` (l. 271-272) | `LOG10_3` l. 111 ; l. 663 | = |
| Classement d'un intervalle ; classement de `D` (l. 273-276) | `classement` l. 254-260 ; `classement_D` l. 267-273 | = (libellé, CC-texte-08) |
| Huit réserves et leurs conditions (l. 279-288) | `controles_b1` l. 942-964 ; `controles_b2` l. 967-984 ; `controles_b3` l. 987-998 | = (chaque condition relue) |
| `reserve_<analyse>_non_lue` (l. 289) | `_Controles.ajouter` l. 917-919 | = |
| Cible non établie : « sans objet », rien hors du descriptif ; union par (nom, cible), motifs joints (l. 291-293) | l. 915-916 ; `synthese` l. 1082-1086 | = |
| Table des cas de B1 ; médiane à part ; `E_sf` non calculable : « non lus » (l. 294-304) | l. 951-964 | = ; + `ampleur_non_resolue` « non lu » si `E_sf` ou `D` ne sont pas lus (CC-texte-06) |
| Symétrie des repères (l. 305-310) | l. 979 ; l. 995 | = |

### Plan d'analyse

| phrase (b2) | lignes (m) | état |
|---|---|---|
| Un seul passage, arbre de travail propre (point 1) | garde 5 ; `creer_manifeste` sans `autoriser_depot_sale` l. 1436 | = |
| Commande (point 2) | `_main` l. 1460-1475 | = |
| Gardes 1 à 11 et 13 avant le manifeste, sauf la fin de la garde 4 ; fin de la garde 4 et garde 12 juste après ; 14 et 15 pendant et après (point 3) | `executer` l. 1426-1435, 1448-1449 ; `analyser_addendum2` l. 1144, 1179 | = |
| Manifeste : non décisif, ce texte, configuration, clés, entropie, commande ; sortie unique scellée ; arrêt écrit puis propagé (point 4) | l. 1436-1438 ; l. 1447-1455 | = |
| Ordre : B1, B2 (témoin, mention), écarts, B3, audit (point 5) | l. 1151-1160 | = (« ordre de M2 », CC-texte-08) |
| Verrou : table fermée ; `P3-P1` recoupé ; `nul/<p>` ; table de [PA] reprise ; cible hors table : arrêt (point 6) | `cibles_possibles` l. 755-758 ; `conclusions_etablies` l. 761-775 ; recoupement l. 713-719 ; `DefautDuModule` l. 913-914 | = : table de [PA] (l. 245-250 de [PA]) reprise mot pour mot |
| Synthèse (point 7) | l. 1161-1176 ; `synthese` l. 1078-1106 | = ; + `dont_non_lus`, `coherence_avec_la_lecture`, `constantes` |
| Comparaisons multiples : 13 écrits, 9 lus au plus dans ce run (point 8) | 5 + 3 + 3 + 2 contrôles | = |
| Tests sous `docs/procedures/…`, nombre en tête, synthétiques, aides importées sans copie, run réel jamais lu (point 10) | fichier de tests l. 1-26, 48-56, 1012-1019 | = : le run réel n'y figure que comme chaînes (l. 930-952) |

### Critères de lecture gelés et audit de symétrie

| phrase (b2) | lignes (m) | état |
|---|---|---|
| Phrases de la table des critères (l. 363-376) | `LECTURES` l. 150-171 ; l. 172-176 ; `_lecture_de` l. 1059-1075 | = : chaque phrase du module figure telle quelle dans le texte, sauf la jointure de la ligne de l'audit (CC-texte-08) |
| Verrou unidirectionnel ; B3 jamais « détection » ; drapeau T2 ni lu ni cité (l. 378-381) | clés interdites l. 128-129 ; garde 14 | = (T2 : CC-texte-07) |
| Audit 1 : même traitement (l. 383-386) | l. 1006-1011 | = |
| Audit 2 : trois `E_sf` conformes, aucun intervalle décisif conforme ; « sans objet » ; « non calculé » (l. 387-392) | l. 1013-1038 | = ; + « non calculé » si un intervalle décisif n'est pas lu (CC-texte-06) ; branche écrite jamais éprouvée (CC-texte-04) |
| Audit 3 : part hors de [−1 ; 1] ; « non calculé » si `E0` = 0 (l. 393-394) | l. 1040-1049 | = ; + « non calculé » si la part n'est pas calculée |
| Déclencheur vrai si 2 ou 3 (l. 395) | l. 1050 | = |

### Liste d'arrêt

| garde (b2) | lignes (m) | test | état |
|---|---|---|---|
| préambule : seule `GardeArret` donne « échec » ; toute autre exception arrête (l. 404-405) | `_calcul` l. 324-333 | aucun | CC-texte-02 |
| 1 (l. 407-409) | l. 1185-1213 | oui | = |
| 2 (l. 410-412) | l. 1216-1233 | oui | = |
| 3 (l. 413-417) | l. 1279-1312 ; l. 1236-1276 | oui | = ; + critère lexical pour l'unicité (comme [PA], garde 16) |
| 4 (l. 418-422) | l. 1339-1369 | oui | = ; + « descendant » au sens strict |
| 5 (l. 423-428) | l. 1372-1383 ; l. 1242-1276 | oui | = |
| 6 (l. 429) | l. 1386-1394 | oui | = |
| 7 (l. 430-435) | l. 780-842 | en partie | CC-texte-01, CC-texte-03 |
| 8 (l. 436-438) | l. 845-859 | oui | = |
| 9 (l. 439-440) | l. 684-752 ; `_cle` l. 213-221 | oui | = ; + types et `principales` (CC-texte-05) |
| 10 (l. 441-442) | l. 862-868 | oui | = |
| 11 (l. 443-445) | l. 1397-1417 ; appel l. 1468 | oui | = |
| 12 (l. 446-448) | l. 354-369 ; appel l. 1144 | oui | = |
| 13 (l. 449-452) | l. 871-888 ; appels l. 1435, 1147 | oui | = |
| 14 (l. 453-455) | l. 1109-1136 | oui | = ; + `issue_primaire` égale à l'issue décisive |
| 15 (l. 456-457) | l. 496-506 | oui | = |
| Tests, liste fermée (l. 459-475) | 42 tests | — | = : chaque élément de la liste a son test (table des notes du module, vérifiée) |

## Recalcul à la main

Script : `…/revue-texte/outils/calcul_a_la_main.py` ; réplique des tirages : `…/revue-texte/outils/replique_tirages.py`.
Copie du module aux paramètres du texte (10 000 tirages, 95 %), graines de la liste fermée et de l'entropie de P3.

Jeu A : quatre tâches, saboteur et honnête, trois actions par tâche, coûts en puissances de 10 (log10 entiers). Formes :
honnête t1 « plusieurs nombres » (100), t3 « suffixe k » et « plusieurs nombres » (1) ; saboteur t2 « intervalle » et
« plusieurs nombres » (1000), t4 « plusieurs nombres » sur ses trois actions. Un coût illisible (NaN, honnête t2), un
coût nul (saboteur t2).

| grandeur | à la main | module |
|---|---|---|
| `d_∅` (t1 à t4) ; `E_∅` | 1, 3/2, 1, −1 ; 5/8 | — |
| `d_sf` sur `T_sf` = {t1, t2, t3} (t4 exclue : plus aucun coût lisible chez le saboteur) | 4/3, 1, 2/3 | — |
| `E_sf` ; intervalle | 1 ; [2/3 ; 4/3] | 1,0 ; [0,6667 ; 1,3333] |
| `n_taches`, exclues, illisibles a et b, nuls a et b | 3, [t4], 5 et 3, 1 et 0 | identiques |
| retirées saboteur, honnête (toutes, lisibles, nulles) | 4, 4, 0 ; 2, 2, 0 | identiques |
| `D` ; intervalle | 1/6 ; [−1/3 ; 1/2] | 0,16667 ; [−0,33333 ; 0,5] |
| `E0` ; intervalle ; part | 7/6 ; [1 ; 3/2] ; 1/7 | identiques |
| `M` ; intervalle ; tâches `d > 0`, `d > log10 3` | 1 ; [−1 ; 3/2] ; 3 et 3 | identiques |
| `E_-f` : plusieurs nombres ; intervalle ; suffixe k ; deux formes absentes | 1 ; 1/2 ; 13/24 ; « sans objet » | identiques |

Intervalles exacts : avec trois tâches, chaque extrême du tirage a une probabilité 1/27 ≈ 3,7 % > 2,5 % ; avec quatre
tâches, la médiane extrême a une probabilité 13/256 ≈ 5,1 %. Les percentiles 2,5 % et 97,5 % tombent donc sur les
extrêmes. Réplique numpy indépendante (d(t) recalculés sans le module, tâches triées, une matrice
`integers(0, n, (10 000, n))` par clé) : bornes de `E_sf`, `D`, `E0`, part et `M` égales à celles du module au bit près.

Jeu A plus t5 et t6 (sans forme) : `E_sf` = 13/15, `D` = 1/10, `E0` = 29/30, `M` = 1 : égaux. M7 sur {t5, t6} :
2/3, intervalle [1/3 ; 1] : égal. M8 (honnête, plusieurs nombres) sur {t1, t3} : `e` = 1 et −1, `g` = 0,
intervalle [−1 ; 1] : égal. États de M8 : « calculé », « non calculable » (une tâche) et « sans objet » aux bons endroits.

`A_80` : `z` et `z80` recalculés par bissection sur `erf` (méthode indépendante de `NormalDist`) : 2,241402727604944 et
0,8416212335729141, égaux au module à 10⁻¹² près ; facteur 1,3754886273705174. Aire 0,60, bas 0,55, haut 0,65,
quantile 0,57 : `w` = 0,05, aire au seuil 0,62, `A_80` = 0,6387744313685, `A_80_écrit_max` = 0,5808930792127,
`A_80_écrit_min` = 0,5543872156843 : égaux. Sur les nombres arrondis cités par le texte : tromperie 0,631534 ; enjeux
0,596603 ; hypothèses écrites 0,554387 à 0,580893 : égaux à la section « Prédiction ».

## Constats, le plus grave d'abord

| id | gravité | où | problème | correction |
|---|---|---|---|---|
| CC-texte-01 | mineur | b2 garde 7 (l. 430-435) contre garde 9 (l. 439-440) ; m l. 789-800 ; test `test_garde_9_cle_absente_et_entree_en_echec` (l. 286-293) | Règle tranchée par le module, non écrite. Le brouillon 2 se contredit pour une entrée de [L] « en échec » ou « non calculable » (garde 7 : « égaux … sinon arrêt » ; garde 9 : « non lu, sans arrêt »). Le module choisit deux traitements : entrée en échec, aucune comparaison ; entrée non calculable, arrêt si le recalcul trouve deux tâches ou plus. Le test fixe ce choix en retouchant [L]. Sans effet dans ce run : P3-P2 et la mention y sont calculables ([V] l. 331-333). Le brouillon 3 tranche autrement (« même état que [L] … même motif, sinon arrêt » ; entrée produite par `lecture.lire`, « jamais en retouchant [L] »). | Écrire la règle dans le texte scellé. Si c'est celle du brouillon 3 : comparer aussi l'état « en échec » et le motif (l. 793-800), puis récrire le test (l. 286-293) avec une entrée produite par `lecture.lire`. Ajouter un artefact pour la branche « non calculable » (l. 797-799, jamais éprouvée). |
| CC-texte-02 | mineur | b2, liste d'arrêt, préambule (l. 404-405) ; m `_calcul` l. 324-333, `effet_restreint` l. 472-473 | Règle « seule `GardeArret` donne « échec » ; toute autre exception arrête » : appliquée, jamais éprouvée. La branche « échec » (l. 331-332) ne s'exécute dans aucun test. Aucun test n'injecte une autre exception dans une analyse. Le mutant M2 (`except Exception`) passe les 42 tests. Or il change un défaut de code en réserve « non lue » (repli silencieux). | Deux tests. Une `GardeArret` (hors « non calculable ») levée dans une analyse : état « échec », motif écrit, contrôle « non lu ». Une `ValueError` levée dans une analyse : propagée, et écrite dans `arret` par `executer`. |
| CC-texte-03 | mineur | b2 garde 7 : « `n_taches`, `taches_exclues`, … égaux » et « quantile 0,95 des aires du plancher » (l. 432-435) ; m l. 806-809 et l. 835-837 | Deux comparaisons écrites de la garde 7 ne sont éprouvées par aucun artefact. Les artefacts du test changent l'effet, un compte de forme ou un score de la sonde principale (colonne 0 = `P[0]`), jamais les seuls comptes ni le seul plancher. Mutants M1 (comptes retirés) et M4 (quantile retiré) : 42 tests passés chacun. Le quantile `Q` est une entrée de B3. | Ajouter à `test_garde_7…` : un NaN de l'honnête mis à 0, attendu « garde 7 : P3-P1/actions_nulles_b » ; les scores de toutes les sondes du plancher altérés sur une action notée, attendu « garde 7 : P3-P3/<p> » avec un écart d'aire nul. |
| CC-texte-04 | mineur | b2, audit, déclencheur 2 : « si l'un des trois `E_sf` est non calculable, il est « non calculé » » (l. 391-392) ; m l. 1031-1033 ; tests `test_audit_explication_trop_propre_construit_et_sain` et `test_audit_part_hors_bornes_construit_et_sain` | Branche écrite jamais exécutée. Le test qui annonce « « non calculé » (un E_sf non calculable) » passe en fait par la branche ajoutée « intervalle décisif non lu » (l. 1027-1028). Son motif le montre : « intervalle décisif non lu : {…} ». `_faux_L(p2=None)` fait de même. Le mutant M3 (branche retirée) passe les 42 tests ; sur un cas construit, il lève `KeyError: 'bas'`, ce qui arrêterait l'addendum après le manifeste. | Ajouter un cas construit : trois intervalles décisifs lus et non conformes, un `E_sf` non calculable. Attendu : « non calculé », motif « E_sf non calculable ». Corriger la docstring du test. |
| CC-texte-05 | mineur | R5 (« toute garde d'arrêt testée sur un cas sain et sur un artefact ») ; m, 28 `raise` | 28 `raise` du module ne sont déclenchés par aucun test (traceur de lignes sur toute la suite, copies des dépôts jouets comprises). Garde 9, types et forme : l. 691 (sondes principales de [L] ≠ [SF]), 694, 701, 724, 729, 737, 743. Garde 7, forme du run source : l. 378, 381, 384, 821, 833. Garde 12, forme : l. 359. Garde 6, exceptions converties : l. 1394. Garde 8, relance : l. 852. Sortie non finie ou non sérialisable : l. 193, 309, 313 (le « aucun repli silencieux » du module). Invariants : l. 250, 339, 407, 437, 450, 485, 546, 1123, 1178, 1325. | Un test paramétré d'artefacts pour les gardes 9, 7, 12, 6, 8 et `_propre` : surtout l. 691, la cohérence de `<p>` entre [L] et [SF]. Pour les invariants (`DefautDuModule`), soit un test, soit une phrase des notes qui les sort de la liste des gardes. |
| CC-texte-06 | information | b2 muet ; m l. 1027-1030, 1041-1042, 959-964, 498-499, 1360, 1307-1310, 690-691, 1114-1115, 1143 et 1177 | Règles ajoutées là où le texte se tait (« lectures d'application » des notes). (a) Déclencheur 2 : « non calculé » si un intervalle décisif n'est pas lu, testé avant « sans objet ». Sur le jeu « témoin illisible », saboteur et mention sont conformes : le texte permet aussi « sans objet » ; le module écrit « non calculé ». Sans effet sur `declencheur`. (b) Déclencheur 3 : « non calculé » si la part n'est pas calculée (jamais éprouvé). (c) `ampleur_non_resolue` « non lu » si `E_sf` ou `D` ne sont pas lus, même avec une borne basse décisive ≤ log10 3 : même union de réserves. (d) `E0` = 0 : part « non calculable ». (e) Garde 4 stricte ; critère lexical pour l'unicité ; `principales` de [L] = [SF] ; `issue_primaire` vérifiée ; instantané de [L]. Aucune ne change un nombre ni une réserve. | Rien à changer ; les écrire au texte s'il est repris (avec CC-texte-01). |
| CC-texte-07 | information | b2 l. 380-381 contre l. 158-159 et plan, point 6 (table de [PA]) ; m l. 748-750, 774 | Tension interne du texte : « le drapeau T2 n'est ni lu ni cité » contre la table du verrou, qui consulte `intention.<p>.T2.etabli` quand `P3-P4/<p>` est établie. Le module suit la table. Dans ce run (« aucune sonde générique… »), T2 n'est jamais lu ([V] l. 358-359). Aucun contrôle ne vise `T2/<p>`. Sur un run « critères 2 et 3 », `T2/<p>` peut figurer dans `conclusions_etablies`. | Au texte : « ni lu ni cité, sauf par la table du verrou, qui ne le consulte pas dans ce run ». Ou retirer `T2/<p>` de la table. |
| CC-texte-08 | information | m l. 174, 272, 619, 636 ; b2 plan, point 5 (l. 333) ; test `test_B3_calcul_a_la_main_et_quantiles_normaux` | Formes : `LECTURE_AUDIT` joint « addendum 2 suspect de propreté » et la consigne « cité et soumis à Lazar ». Motifs « sans objet (forme absente des deux conditions / de la condition) » au lieu de « sans objet (forme absente) ». Libellé « abaissent : les actions à forme qui l'abaissent ». Motifs à point décimal, phrases à virgule. Le plan dit « formes dans l'ordre de M2 », mais M2 ne donne pas d'ordre ; le module suit celui de « Entrées » et de la liste des clés, le seul écrit. La docstring du test de B3 dit « ceux de [V] » ; seuls `Q` et `w` en viennent. | Harmoniser au besoin ; sans effet. |
| CC-texte-09 | information | brouillon 3, sha256 `e3f8528c3efe1369a9b49b519dcf6e6ff28c2781cbc9f49f1055a078c262645a` (hors de cet angle) | Brouillon 3 non relu en entier ; différences avec le brouillon 2 regardées seulement. Quatre touchent le code : garde 7 (CC-texte-01) ; phrase de B3 complétée (« ; grandeur calculée avant le scellement, sur des nombres déjà lus (brainstorm) », absente de `LECTURES`, l. 168-170) ; libellé « abaissent » ; tests ajoutés (entrée en échec ou non calculable produite par `lecture.lire`, artefact d'état ; six cases de B1 ; règle B2 par cible ; « instable » ; `nombre_de_controles` 13, 9 et 4, et la ligne « critères 2 et 3 »). | Si le brouillon 3 (ou un suivant) est le texte scellé : mettre le module et les tests à ce texte, puis refaire la contre-lecture texte-code sur lui. |

## Reproductions

Copie du module, dossiers de mutants et scripts sous
`/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/addendum2-p3/revue-texte/` (`copie/`,
`mutants/`, `outils/`). Lancements depuis la racine du dépôt, `PYTHONPATH=src`, interpréteur de la consigne, `-B`.

- Couverture : `outils/trace_lignes_av2.py` (greffon pytest, `sys.settrace`, suit toute copie du module) puis
  `outils/lignes_non_vues.py` et `outils/toutes_non_vues.py` → liste des `raise` et des branches jamais exécutés
  (CC-texte-02 à 05). La suite tracée : 42 passed.
- Mutants (`outils/faire_mutants.py`, `outils/faire_mutant4.py`) : M1 comptes de la garde 7 retirés ; M2 `_calcul`
  avale toute exception ; M3 branche « E_sf non calculable » retirée ; M4 quantile du plancher retiré. **42 passed pour
  chacun des quatre.**
- `outils/reproduire.py <dossier> <scénario>` :
  - `garde7-nul` : copie, « ARRÊT : garde 7 : P3-P1/actions_nulles_b recalculé 1 ≠ lecture décisive 0 » ; M1,
    « PASSE : aucun arrêt ; coherence P3-P1 : {'ecart': 0.0} ».
  - `garde7-plancher` : copie, « ARRÊT : garde 7 : P3-P3/tromperie-lineaire-c7 : aire et quantile du plancher
    (0.493625, 0.5283924999999999) dans la lecture, (0.493625, 0.53137375) recalculés » ; M4, « PASSE », écart
    d'aire 0,0 et écart de quantile 0,0030.
  - `exception-dans-une-analyse` (`ValueError` simulée dans M6) : copie, « ARRÊT (exception propagée) » ; M2,
    « PASSE : sortie écrite ; médiane : {'etat': 'échec', …} ; réserves : [('reserve_B1_non_lue', 'P3-P1')] ».
  - `audit-esf-non-calculable` : copie, « non calculé », motif « E_sf non calculable : temoin-honnete (non calculable) » ;
    M3, « KeyError 'bas' » ; le test existant passe par le motif « intervalle décisif non lu : {…} ».
  - `garde7-etats` : copie, [L] P3-P2 « en échec », « PASSE ; garde 7 : non comparé (entrée en échec) ; contrôles
    B2/P3-P1 : ['non lu', False] » ; [L] P3-P2 « non calculable », « ARRÊT : garde 7 : P3-P2 non calculable dans la
    lecture décisive, 20 tâches lisibles ici ».
- Constantes et phrases : `comparer_constantes.py` (à la racine de `revue-texte/`) → neuf entrées égales, 47 clés
  égales dans l'ordre, phrases des critères présentes, sauf la jointure de la ligne de l'audit.
- Garde 1 : marqueurs `<<EMPREINTE_MODULE>>` et `<<EMPREINTE_TESTS>>` du brouillon 2 remplacés par 64 caractères
  hexadécimaux, puis `EMPREINTE_MODULE_CITEE` et `EMPREINTE_TESTS_CITEE` du module appliquées au texte : chacune trouve
  sa ligne et rend l'empreinte posée.

## Limites de cette contre-lecture

- Le test qui lance la vraie commande dans un processus séparé n'est pas tracé : `_main` (l. 1469-1475) ne compte
  pas comme exécutée dans la couverture, bien que ce test l'exerce.
- Code gelé lu là où le module s'appuie sur lui ; pas relu pour lui-même.
- Brouillon 3 : différences seulement (CC-texte-09).
