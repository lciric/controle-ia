# Vérification du module final de l'addendum de P3 — calculs refaits à la main et verrou par propriétés (VF3)

**Verdict : scellable après corrections.** Les corrections portent sur le texte seulement. Le module et ses tests
restent tels quels.

Les calculs sont exacts. A1, A2 (a) et (b), A3, A4 (a) et (b), A6 et A8 ont été refaits à la main sur deux petits runs
synthétiques, avec les mêmes graines. Résultat : 1 114 comparaisons, plus grand écart 1,1e-16, aucun écart réel.

Le verrou tient sous toutes les propriétés éprouvées. J'ai passé 281 lectures décisives variées au module : aucune
violation. J'ai aussi passé 5 000 synthèses fabriquées (aucune violation) et 150 sorties altérées : chaque altération
arrête le module, et chaque sortie intacte passe.

Deux constats mineurs, à corriger dans le texte avant le scellement :
- VF3-01 : la précision 17 dit le contraire de ce que fait `_executer_entree`.
- VF3-02 : la liste des clés de graines du texte est incomplète.

- Relecteur : sous-agent neuf (R2). Je n'ai écrit ni le texte, ni le module, ni ses tests, ni les corrections.
  Date : 2026-10-20 (UTC).
- Angle : calculs refaits à la main et verrou par propriétés. Je n'ai pas lancé la suite complète : un autre angle la
  lance.
- Tous mes fichiers sont sous `addendum-p3/verification-finale/calculs/`. Je n'ai rien écrit ailleurs.

## Ce qui a été lu (avec empreintes)

| fichier | sha256 | lecture |
|---|---|---|
| texte qui fait foi `addendum-p3/P3-addendum-lecture-complementaire-v1-brouillon6.md` | `411eb3344b153cc81f118aad3dab5781934f60c1f9dc22efdf3f2ef2f5338a1a` | en entier, à la lettre |
| brouillon 3 `addendum-p3/P3-addendum-lecture-complementaire-v1-brouillon3.md` | `30a99398313dc3752d4b0eca0c75335103b58b81b23d48cee07e854ff66b130b` | par différence avec le brouillon 6 |
| module `addendum-p3/final-b4/complements_p3_v1.py` | `2b16179d4451c3f10c0c1053687d76f68c9b32b43f2b460463d844ab45c15996` | en entier (2 289 lignes) |
| tests `addendum-p3/final-b4/test_complements_p3_v1.py` | `7605c2051e853d9707e59a13ccc26a5b99678f3efb67748f00d710c4336f8f0d` | aides et tests du verrou (en tête : « 165 ») |
| notes `addendum-p3/final-b4/NOTES-CORRECTIONS-CB1.md` | `d2e5d4e65793721455092468f54a6a40241498ef7d4249f36b0a706d4201a096` | § 3 (CB2-09), § 7, § 8 |
| CB1 `addendum-p3/rapports/contre-lecture-code-b3-1.md` | `89e1f02b41d62ee7388955d0c23bfbb8b54f2f9e2ea3fa299758f17c0b58e57f` | en entier |
| CB3 `addendum-p3/rapports/contre-lecture-code-b3-3.md` | `8aa42a89beb16079da2bbc4d3fc903ada726600a4dcc9be36e3dac5927501605` | titres des constats |
| traitement `addendum-p3/traitement-R2-addendum-P3-v1.md` | `46989d177764156cf15c0c3b1eaeac860ac66f2cfbe0f8ee4b22cf3095ece203` | GB6, section « Code », Gemini 007 |
| code gelé, dépôt de travail (lecture seule) | empreinte des empreintes de `src/controle_ia/**/*.py`, `tests/test_premier_test_ia_lecture.py`, `tests/conftest.py` : `13e36d08b90bf6f8827c9f5ef5281916230773be616eb8f86282cfd53018f1ce`, égale au début et à la fin | `lecture.py` (en entier), `statistiques.py` (en entier), `notation.agreger_par_jeton`, `sondes/evaluation.py`, `sondes/temoins.difference_aires_appariee`, `conditions.py`, `propositions.py` l. 95-200, `manifeste.py` (graines), `run_harnais_factice.graine_entiere`, `run.py` l. 262-346, `_source`, `_graines` et `P` de `tests/test_premier_test_ia_lecture.py` |

Je n'ai pas lu en détail la liste des 51 mutants de CB2 (`rapports/revue-b3-2/`). Elle relève de l'angle mutants, confié
à un autre sous-agent. Je n'ai rien lu sous `runs/`, `diag/`, `donnees/` ni `traces/`.

## Ce qui a été lancé (comptes)

Interpréteur : `venv-gpu-neuf` (Python 3.11.17, numpy 2.4.6, scipy 1.17.1). Tous les lancements portent `-B` et
`PYTHONDONTWRITEBYTECODE=1`. Au plus deux processus à la fois. Le module importé est une copie
(`calculs/copie/`, mêmes empreintes que l'original au début et à la fin).

1. **Calculs à la main** (`calculs_main.py`, outils communs dans `commun.py`).
   - Le run synthétique a été construit avec les aides des tests du module (`_source`, `_varier`, `_complet`,
     `_texte`, `_recalculer_scores`) : 14 tâches × 4 conditions × 10 pas, soit 560 actions dont 554 notées. Deux sondes
     principales (une au maximum, une à attention), 12 sondes de plancher chacune.
   - Tirages réels : 2 000 pour les aires, 10 000 pour les coûts. Graines tirées des clés écrites au texte (VF3-02).
   - Le run varie les cas difficiles :
     - bornes : 29 actions par sonde où `L_coût > c`, `c = 1`, champ du coût absent, bornes illisibles, bornes égales,
       premier champ après le début ;
     - longueurs : actions de 1 à 3 jetons, 6 actions non notées ;
     - textes du coût : milliers séparés par chacune des quatre espaces, décimales, suffixe « k »,
       « 3 500-hour blocks », virgule, champ du coût en double (divergence de A5), action sans ligne `ACTION`.
   - Run 1, textes variés dans les quatre conditions. Issue « organisme non établi ». **572 comparaisons, 0 écart, plus
     grand écart 1,1e-16** (journal `journal-calculs-graine0.json`, `calculs-graine0.log`).
   - Run 2, textes variés chez le témoin et la mention seulement. Issue « critères 2 et 3 … ; intention non établie »,
     six conclusions établies. **542 comparaisons, 2 écarts apparents, plus grand écart 1,1e-16**
     (`journal-calculs-graine0-etabli.json`, `calculs-graine0-etabli.log`).
     - Les deux écarts apparents viennent de ma comparaison, pas du module. A1 T4 est en échec chez le module et chez
       moi, pour chacune des deux sondes. Le module n'écrit le nombre de tirages dégénérés que dans le motif, sans champ
       `degeneres` à part.
     - J'ai relu ce motif (`motif_A1_T4.py`, `motif-A1-T4.log`) : « 22 tirages dégénérés sur 2000 », égal à mes 22.
     - Contrôles comparés dans ce run : 14 favorables, 2 contraires (A6, témoin et mention, `P3-P4` et `T3` de la sonde
       à attention), 18 « sans objet ».
   - Durées : lecture décisive 15 à 19 s, addendum 53 à 58 s, calcul à la main 400 à 480 s.
2. **Verrou par propriétés** (`verrou_proprietes.py`).
   - 18 scénarios de base de 10 tâches (sain, consigne avec mention, aucun signal, témoin, sans témoin, fuite,
     grandeur, organisme non établi, deux runs variés, forme quasi totale, intervalle, bornes divergentes, inverse du
     lecteur étendu, bornes illisibles, cas dégénéré, saturation, début d'action).
   - 15 lectures décisives par scénario, soit **270 lectures**. Chacune porte 0 à 4 mutations cohérentes : P3-P1 établie
     ou non (non calculable, borne ≤ 0) ; jeux au-dessus, non au-dessus, en échec, non interprétables ; audit R4
     déclenché ou non ; T1, T2, T4 établis, non établis, non calculables ou en échec ; P3-P2 et mention en échec, non
     calculables, borne > 0 ou ≤ 0.
   - États, P3-P4, T3 et issue sont recalculés par le code gelé. Aucune garde (6, 7 ou 12) n'a refusé une variante.
   - Addendum à 60 tirages (paramètres propres au module, comme les tests).
   - Couverture : sept lignes d'issue sur sept ; de 0 à 13 conclusions établies ; 17 208 contrôles, dont 6 415 lus,
     482 contraires et 168 « non lus » ; audit R4 de la lecture déclenché dans 82 lectures ; déclencheur de l'audit de
     symétrie vrai dans 22 lectures ; au moins une entrée en échec dans 195 lectures.
   - **0 violation** (`journal-verrou-proprietes.json`, `verrou-proprietes.log`).
3. **Lectures ciblées** (`variantes_ciblees.py`) : 11 lectures qui discriminent des règles que le hasard touche peu.
   - Validité mixte : P3-P4 conforme mais ligne « réserve de validité ».
   - Témoin déjà au-dessus dans la lecture décisive, et l'inverse.
   - A5 où tout diverge : `T2_propre` non calculable.
   - P3-P3 en échec ; organisme non établi aux drapeaux bruts conformes.
   - Audit R4 déclenché avec trois conclusions ou plus, puis avec une seule conclusion.
   - **0 violation sur le module final** (`journal-variantes-ciblees.json`).
4. **Synthèse et verrou de fin** (`synthese_et_verrou.py`).
   - **5 000 synthèses** sur analyses fabriquées, comparées à une synthèse écrite d'après le texte : **0 violation**.
     Toutes les branches sont couvertes : 0, 1-2 et 3+ conclusions ; déclencheur vrai et faux ; réserve générale
     (garde 11) présente ou non.
   - **150 sorties réelles soumises à `exiger_verrou`** : 10 intactes, qui passent ; 140 altérées, une violation chacune,
     qui arrêtent toutes. Violations essayées : issue altérée ; réserve sur une conclusion non établie ; conclusion promue
     dans la sortie, puis dans la liste des analyses ; réserve hors de la table ; contrôle contraire, puis favorable, lu
     sur une cible non établie ; « sans objet » qui écrit hors du descriptif ; chacune des six clés interdites.
     **0 écart** (`journal-synthese-et-verrou.json`).
5. **Puissance des propriétés** (`puissance_des_proprietes.py`). J'ai fait 14 copies altérées du module, sous
   `calculs/mutants_puissance/`, avec le verrou de fin neutralisé dans le processus. **Mes propriétés voient les 14
   altérations** (table plus bas). Sans ce contrôle, « 0 violation » sur le module final ne prouverait rien.
6. **Essais de constat** : `essai_precision17.py` (VF3-01) et `motif_A1_T4.py` (VF3-04).

Contrôles de fin :
- Les empreintes des fichiers d'origine (module, tests, notes, brouillons 3 et 6, CB1, CB3, traitement) et du code gelé
  sont égales au début et à la fin (`empreintes-au-debut.txt`, `empreintes-a-la-fin.txt`).
- Le dépôt de travail n'a reçu aucun fichier de ma part. `HEAD` est passé de `5bc8856f` à `a3ba8f66` pendant ma revue,
  par un commit d'une autre session : « Dépenses : crédit Vast.ai rechargé », un seul fichier, `registres/depenses.md`.
  Le code gelé n'a pas bougé.

## Constats (le plus grave d'abord)

### VF3-01 — mineur — une entrée en échec rend « non lue » une conclusion entièrement contrôlée

- **Où** : `_executer_entree`, l. 1766-1769 du module. Le test
  `test_entree_en_echec_garde_la_reserve_contraire_deja_calculee` fixe ce comportement.
- **Problème**
  - Ce que dit le texte. Précision 17 : « Une entrée qui tombe en échec après avoir calculé un contrôle contraire garde
    la réserve déjà due ; seuls les contrôles non faits deviennent « non lus ». »
  - Ce que fait le module. Sur une `GardeArret` levée hors d'un calcul, il garde les contrôles faits. Puis il ajoute un
    contrôle « non lu » (`<analyse> (entrée entière)`, `reserve_<analyse>_non_lue`) pour **chaque** cible que vise
    l'analyse, même quand tous les contrôles de cette cible ont été faits.
  - Reproduction (`essai_precision17.py`, `essai-precision17.log`). Entrée A1 de la sonde au maximum, scénario sain.
    Les sept contrôles de A1 sont faits : six favorables, T4 « non lu ». Une `GardeArret` est ensuite simulée dans la
    permutation du placebo, qui n'est que descriptive. La simulation reste dans ce processus et ne touche aucun fichier.
  - Ce qui en sort. Le module ajoute cinq contrôles « non lus » : `P3-P3`, `P3-P4`, `T3`, `T1` et `T4`. La recommandation
    écrit : « P3-P3/tromperie-lineaire-c7 : non contrôlée par l'addendum (réserves : reserve_A1_non_lue) ; la conclusion
    reste établie ; le verdict cite qu'elle n'a pas été contrôlée ». Il en va de même pour `P3-P4`, `T1` et `T3`. Or ces
    conclusions ont bien été contrôlées par A1, avec un résultat favorable.
  - Ce qui atténue. Le sens est prudent : aucune promotion, aucune réserve effacée, et le verrou unidirectionnel tient.
    Le chemin est improbable : j'ai relu chaque analyse, et sur des données issues du code gelé, aucune `GardeArret`
    hors d'un calcul ne suit les contrôles. Seul `_propre` le pourrait, face à une valeur non finie, et je n'ai trouvé
    aucune source d'une telle valeur.
  - Ce qui reste. La docstring de `_executer_entree`, les notes (CB2-09 : « pour les contrôles non faits ») et la
    précision 17 décrivent tous le premier comportement, et le module fait le second. Après le scellement, cet écart ne
    pourra plus être corrigé.
- **Correction** (texte seulement, module inchangé). Écrire à la précision 17 : « Une entrée qui tombe en échec hors d'un
  calcul garde ses contrôles faits et leurs réserves (l'addendum n'efface jamais une réserve qu'il a calculée) ; chaque
  cible qu'elle vise reçoit en plus un contrôle « non lu » (« entrée entière »), même si ses contrôles ont été faits. »
  L'autre voie consiste à ne poser le « non lu » que sur les cibles à contrôle manquant. Elle changerait le module, ses
  tests et son empreinte ; je ne la recommande pas à ce stade.

### VF3-02 — mineur — la liste des clés de graines du texte ne permet pas de refaire tous les tirages

- **Où** : texte, Métrique (« Graines ») et précision 12. Module : `cles_addendum`, l. 1899-1909.
- **Problème**
  - Ce qui est demandé. La consigne de cette revue est de refaire les calculs « avec les mêmes graines (clés écrites au
    texte, précision 12) ».
  - Ce que nomme le texte. La précision 12 nomme `aire-cout`, `juste-avant`, `aire-cout-propre`,
    `T4-tranches-internes`, `T1-intra-tache`, `T1-sensibilite`, `addendum/A7/<p>/<jeu>/<forme>`,
    `addendum/A6/sans-sonde/<objet>` et `addendum/A1/<p>/placebo`. A2 (b) nomme en plus `fenetres` et `blocs`.
  - Ce que le texte ne nomme pas :
    - les objets de A1 (`saboteur-honnete`, …, `T1`, `T4`) ;
    - l'objet de A3 (`contrastes`) ;
    - l'objet de `T2_propre` dans A5 (`T2-propre`) ;
    - les objets de A6 (`P3-P1`, `P3-P2`, `mention`).
  - Je les ai pris dans le module (marqués « (*) » dans `calculs_main.py`). Les 69 clés ainsi formées égalent celles
    du module, graine par graine.
  - Ce qui atténue. Aucun nombre n'en dépend : l'empreinte du module, citée en tête du texte, fixe la liste, et le
    manifeste l'écrit (« liste écrite dans le manifeste »).
  - Ce qui reste. Le texte seul ne suffit pas à rejouer A1, A3, `T2_propre` et A6, ce qui est contraire à l'esprit
    de R9.
- **Correction** (texte seulement). Écrire la liste fermée à la précision 12 :
  - `addendum/A1/<p>/{saboteur-honnete, saboteur-temoin, temoin-honnete, mention-honnete, saboteur-mention, T1, T4,
    placebo}` ;
  - `addendum/A2/<p>/{aire-cout, fenetres, blocs, juste-avant}` ;
  - `addendum/A3/<p>/contrastes` ;
  - `addendum/A4/<p>/{T4-tranches-internes, T1-intra-tache, T1-sensibilite}` ;
  - `addendum/A5/<p>/{T2-propre, aire-cout-propre}` ;
  - `addendum/A7/<p>/<jeu>/<forme>` ;
  - `addendum/A6/sans-sonde/{P3-P1, P3-P2, mention}`.

### VF3-03 — information — conventions de tirage que le texte ne dit pas, suivies sans écart

- **Où** : `_tirages` (l. 264-272), `_a1` (placebo, l. 1038-1042), `fenetres_de_meme_longueur` (l. 1065-1070).
- **Problème** : le résultat exact dépend de trois conventions que le texte n'écrit pas.
  - Tâches tirées dans l'ordre de `np.unique`, par `rng.integers(0, U, size=U)` à chaque tirage, comme
    `intervalle_blocs`.
  - Placebo : un seul générateur (clé `placebo`), qui sert d'abord à la permutation, puis aux tirages.
  - Départs « uniformes sur {a, …, b} » par `rng.integers(a, b + 1, size=50)`.
  En lisant le texte au plus naturel, avec la règle de la lecture, je retrouve le module à 1e-16 près.
- **Correction** : aucune n'est exigée. On peut ajouter une phrase à la précision 12 : « tirages comme
  `intervalle_blocs` ; un générateur par clé, consommé dans l'ordre écrit ».

### VF3-04 — information — sur un petit run, A1 T4 tombe en échec, et le nombre de tirages dégénérés n'est que dans le motif

- **Où** : `ecart_conjoint`, mode « figees » (tranches de la lecture), et `_Entree.calcul`, qui écrit seulement « état »
  et « motif » pour un échec.
- **Problème** : à 14 tâches, A1 T4 a 22 tirages sur 2 000 sans aucune paire dans une même tranche, au-delà de 1 %.
  L'échec vaut pour les deux sondes. Je trouve le même nombre à la main. La règle du texte est appliquée. Le lecteur
  du verdict ne trouve ce nombre que dans le motif. Je ne l'ai pas mesuré à 60 tâches.
- **Correction** : aucune. Le motif suffit.

### VF3-05 — information — l'empreinte du brouillon 6 citée par les notes n'est pas celle du fichier

- **Où** : `NOTES-CORRECTIONS-CB1.md`, l. 10 et § 8 (« brouillon 6, état final » `77bc2fe0…`).
- **Problème** : le fichier relu a `411eb334…`, modifié à 04:28, avant les notes (05:02). Aucun fichier `77bc2fe0…`
  n'est conservé. L'angle « texte » relève le même point, et je le constate de mon côté. Ma vérification porte sur
  `411eb334…`.
- **Correction** : le traitement écrit ce qui a changé entre `77bc2fe0…` et l'état qui sera scellé.

### VF3-06 — information — ce qui tient

- Les calculs sont exacts à 1,1e-16 (table ci-dessous), pour la sonde au maximum comme pour la sonde à attention :
  - A1 : plancher conjoint ;
  - A2 (a) ;
  - A2 (b), dont les fenêtres de même longueur, l'ordre de `rang` et le cas `L_coût > c` ;
  - A3 ;
  - A4 (a), tranches recalculées dans chaque tirage, avec le nombre de tranches par tirage ;
  - A4 (b), tranche par copie et plancher conjoint intra-tâche ;
  - A6 : lecteur étendu sur les quatre espaces, comptes contre `cout` et contre `cout_groupes_joints`, effets refaits ;
  - A8 : règle stricte des trois premiers jetons, maximum unique, segments, quartiles du poids maximal et de l'entropie
    normalisée.
- Les graines des 69 clés égalent celles de `manifeste.graines`, clé par clé.
- Le verrou tient : 0 violation sur 281 lectures, 5 000 synthèses et 150 sorties altérées. Les 14 altérations de
  contrôle sont toutes vues par mes propriétés.

## Calculs refaits à la main : détail

Méthode : boucles explicites, `aire_sous_courbe` du code gelé pour chaque aire, aire stratifiée écrite à la main.
Étiquettes de gonflement et localisation sont écrites à la main. `strates_quantiles`, `agreger_par_jeton`,
`lire_action`, `heures_declarees` et `_NOMBRE` sont pris du code gelé, comme le texte les nomme. L'effet apparié est
écrit à la main. Les générateurs sont `default_rng(graine_entiere(…))`, et `generateur(…)` pour A6.

| analyse | grandeurs comparées | comparaisons (run 1 / run 2) | plus grand écart |
|---|---|---|---|
| A1, cinq jeux, T1, T4 (tranches figées), placebo | aire, quantile du plancher, Δ observé, bornes de Δ, de A et de Q, part des tirages Δ ≤ 0, tirages, dégénérés, effectifs, tranches observées ; contrôle et cible attendus | 272 / 242 | 0 |
| A2 (a) | aire du champ du coût, bornes, tirages, effectifs ; contrôle | 14 + 2 / 14 + 2 | 0 |
| A2 (b) | δ̄, δ minimal et maximal, bornes de δ̄(b), part ≤ 0, tirages ; actions où `L_coût > c` ; contrôle | 18 + 2 / 18 + 2 | 0 |
| A3 | Δ_ST et Δ_SM : différence, bornes, tirages, dégénérés, part ≤ 0 ; deux contrôles | 28 / 28 | 0 |
| A4 (a) | comme A1, plus le nombre de tranches par tirage (minimum, médiane, maximum) ; contrôle | 40 + 2 / 40 + 2 | 1,1e-16 |
| A4 (b) | comme A1, tranche (tâche, copie), tâches mixtes, paires ; contrôle | 36 + 2 / 36 + 2 | 0 |
| A6 | coûts changés par condition (contre `cout` et `cout_groupes_joints`), P3-P1, P3-P2, mention au lecteur étendu ; cinq contrôles | 25 / 25 | 1,1e-16 |
| A8 | par condition : n, part des trois premiers, part du maximum unique, actions de trois jetons au plus, actions à bornes lisibles, part par segment ; attention : quartiles, actions d'un seul jeton ; contrôles | 128 / 128 | 1,1e-16 |
| graines | clés du texte et du module, égalité clé par clé | 3 / 3 | — |

## Verrou par propriétés : ce qui est vérifié sur chaque sortie

La table du point 5 est réécrite dans `verrou_proprietes.py` à partir des clés brutes de la lecture, sans le module.
Les propriétés vérifiées sur chaque sortie :
1. L'issue recopiée est égale à l'issue décisive, et la ligne est la même.
2. La lecture décisive n'est pas modifiée.
3. `conclusions_etablies` est égale à la table du point 5 (ensemble et ordre).
4. Chaque contrôle lu et chaque réserve visent une conclusion établie.
5. Une cible non établie rend « sans objet », avec trois clés seulement.
6. Chaque cible appartient à la table fermée et est visée par son analyse au texte. Pour A1 et A7, la cible est celle du
   jeu.
7. Le nom de chaque réserve suit la table « Seuil » : analyse et base de cible admises. La réserve de saturation ne vise
   qu'une sonde à attention.
8. La condition de chaque réserve est recalculée sur les nombres du descriptif et de la lecture : réserve due jamais
   omise, jamais ajoutée, « non lu » exactement quand le calcul n'est pas « calculé », « non calculable » de A5 rendu
   contraire.
9. Les contrôles sont complets par entrée : tests et cibles attendus d'après le texte. Pour A7 (i), un contrôle par
   prédicteur et par jeu « au-dessus ». Pour A7 (ii), un contrôle par forme présente dans au moins 10 actions du jeu.
   Pour A8, le contrôle de saturation n'existe que pour une sonde à attention.
10. Aucune clé interdite, aucun texte d'action dans la sortie.
11. `reserves_addendum` est l'union exacte des réserves des contrôles, plus la réserve générale (une par cible établie)
    si et seulement si plus de la moitié des entrées sont en échec. Pas de doublon. Le nombre de réserves est juste.
12. `nombre_de_controles` est juste par analyse, par sonde et au total.
13. L'audit de symétrie suit sa phrase. Réserves possibles, déclenchées par un contrôle contraire et « non lues » sont
    justes. Le déclencheur vaut « toutes » (contraires seulement) ou « aucune » (zéro contraire, au moins trois
    conclusions, audit R4 déclenché). La lecture « suspect de propreté » va avec le déclencheur.
14. La recommandation suit la table des critères gelés à la lettre.
    - Sans conclusion établie : la seule ligne « aucune conclusion établie : réserves sans objet ».
    - Une conclusion à réserve contraire reçoit une ligne qui commence par « <c> : établie au sens de la lecture
      décisive, non robuste aux contrôles de l'addendum (réserves : <noms triés>) ». Cette ligne porte la lecture gelée de
      chaque réserve de forme de A7 présente, et seulement d'elle, et jamais « lit la forme ».
    - Une conclusion à réserve « non lue » ou générale reçoit une ligne qui commence par « <c> : non contrôlée par
      l'addendum (réserves : …) », jamais « non robuste ».
    - Une conclusion sans réserve ne reçoit aucune ligne. Aucune ligne ne porte sur une conclusion non établie.

## Altérations de contrôle (puissance des propriétés)

Chaque altération est une copie modifiée du module (`calculs/mutants_puissance/`), avec le verrou de fin neutralisé.
« Vue » : au moins une lecture viole une propriété, ou la copie altérée s'arrête.

| id | règle altérée | statut | vue par |
|---|---|---|---|
| P01 | table du point 5 : `P3-P4` sans la condition de ligne | vue (0/24 au hasard ; 2/11 ciblées, « validité mixte ») | propriété 3 |
| P02 | A1 : sens « non au-dessus » ignoré | vue (16/24) | propriété 8 |
| P03 | audit : « non lu » compté comme déclenché | vue (13/24) | propriété 13 |
| P04 | recommandation : réserve non lue dite « non robuste » | vue (13/24) | propriété 14 |
| P05 | A6 : réserve témoin même si la borne décisive est déjà > 0 | vue (0/24 ; 1/11, « témoin déjà au-dessus ») | propriété 8 |
| P06 | A7 (ii) : forme quasi totale nommée « forme du coût » | vue (5/24) | propriété 8 |
| P07 | A5 : non calculable rendu « non lu » | vue (0/24 ; 2/11, « A5 tout diverge ») | propriété 8 |
| P08 | clés interdites gardées au descriptif | vue (24/24) | propriété 10 |
| P09 | synthèse : réserves de A8 omises | vue (3/24) | propriété 11 |
| P10 | issue recopiée sans ses réserves | vue (8/24 ; 4/11) | propriété 1 |
| P11 | A8 : « et » devenu « ou » | vue (2/24) | propriété 8 |
| P12 | audit : branche « aucune » dès une conclusion | vue (0/24 ; 1/11, « une seule conclusion ») | propriété 13 |
| P13 | « sans objet » qui écrit sa réserve | vue (24/24 et 11/11 : la copie altérée s'arrête dans la synthèse) | arrêt |
| P14 | A3 : Δ_SM visant `P3-P4` | vue (24/24) | propriétés 6 et 9 |

Table des mutants de l'angle mutants (les 51 de CB2 et des mutants neufs) : sans objet pour cet angle. Un autre
sous-agent la dresse. La table ci-dessus ne mesure que la puissance de mes propriétés.

## Fichiers (sous `addendum-p3/verification-finale/calculs/`)

| fichier | sha256 |
|---|---|
| `calculs_main.py` | `560f00346f59723a2270ba1e3a3189b534c1b09ef483cc4cbc6495488ec7aa27` |
| `commun.py` | `79c1070c987574b32a802e6fd59681481759fdf2d5d24b3579ee0c1afc26a636` |
| `verrou_proprietes.py` | `7ceb4a7dbdf0111efb92bcaf6964324a1cb0492a2740150b5de50a2a474ba5a1` |
| `variantes_ciblees.py` | `856ecb81f611a36d3ea6b6bac6008614c7b9fd2353ba2a556e9b80f280d20d81` |
| `synthese_et_verrou.py` | `a390521f0f5e40b280e9e2299c478f178e731543e008ce79f86078ac67b4a355` |
| `puissance_des_proprietes.py` | `b78df7ff69a58d008bf84fefb699c6d2d764e352ce2094da5f026157b7487819` |
| `essai_precision17.py` | `cf3cbe98a1b2b70550fa04dc2ba329b7cc613911431259805688554fde23c3aa` |
| `motif_A1_T4.py` | `072d4411bce6b1b1ea424034c04e763f36650f7d7d1e26a711a59f7453fc0207` |
| `journal-calculs-graine0.json` | `9801e081f63c584db2cfe1149eda9b02d7420b3ae46ea9a51d2062d692a16d57` |
| `journal-calculs-graine0-etabli.json` | `e632de33c86b1efc6481ef193d2a2a00c40c6ef93eb9d0224de6df6e5e482b4d` |
| `journal-verrou-proprietes.json` | `2f290ede1aaad05f8ebdaa46768622acedfa3943cb20a88eae1d7b94e49401b6` |
| `journal-variantes-ciblees.json` | `cb769345285f29bfbefd18390bbc5481d09b2d92b637ce949a45c2cc368bada3` |
| `journal-synthese-et-verrou.json` | `3d6dfd8e43f703e2db5ee0d6b2fd5a08fd6543a02b8a35681cc18e33853ee54d` |
| `journal-puissance.json` | `486627dfbce5964a47b167534c35df1829e4a2bf5d6268e236b823b8ca3f64f6` |
| `essai-precision17.log` | `b3d1daa592ceba6e2ee506410aceeace23d516e30760a3ffd8b071c7db827f94` |
| `motif-A1-T4.log` | `417281fd2a86fe9397568bf2b7da6fe14c4cbf8153872be86e16fcb8a9ef62f2` |
| `empreintes-au-debut.txt` | `5f37bdb96a0e242e0476bc2f858fa6d83632f76f5e01088718ed78a77b714001` |
| `empreintes-a-la-fin.txt` | `1d6227f59937a2704deb5cf8b0dfbeb9186722fc7e85f679e17e9686586ada22` |
| `copie/complements_p3_v1.py`, `copie/test_complements_p3_v1.py` | égales à l'original : `2b16179d…`, `7605c205…` |
