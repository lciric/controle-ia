# Synthèse du brainstorm défensif — questions candidates du texte III (mesure de l'universalité) — v1

Lecteur neuf, auteur d'aucune pièce lue. Date : 30 octobre 2026.

**Pièces lues, et seulement elles** (dossier `donnees/collisionneur-texte-III-v1/`) : `question-texte-III-envoi-v3.md` ; `criteres-lecture-texte-III-v1.md` (appliqués tels quels) ; `faits-texte-III-v2.md` ; les douze cellules `run-texte-III-e3-v2/cellules/E3-T{1,2,3}-*-{A,B,C,D}.md` ; la réponse d'Argon seul, champ `texte` de la dernière ligne de `/root/ideation-v1/argon-texte-III-v1/reponse-argon-v1.json` (modèle servi : `gemini-4-argon`, fin normale, aucune erreur).

**Notation des sources.** « A1 » = cellule A au tour 1 (conception), « A2 » = critique croisée, « A3 » = réponse aux critiques ; de même pour B, C, D. « Argon seul » = la réponse isolée. Les chiffres marqués « illustratif » ne viennent pas des pièces ou y sont eux-mêmes illustratifs ; « dérivé » = recalculé ici à partir d'une formule des faits.

**Réserves de lecture, avant tout.**
- R-1. Identité du modèle B : la consigne de synthèse dit « Claude Opus 4.6 » ; le fait 13 (VÉRIFIÉ, `collisionneur_v5.py`, ligne 58) dit `claude-opus-5-5`. Divergence non résolue ici (je n'ouvre pas le code). Je désigne la cellule par « B » seulement.
- R-2. Lignées : C et Argon seul sont le même modèle (`gemini-4-argon`) que la **première source** des données de départ (28 familles) ; A et B sont de la lignée Claude, celle de la **seconde source** (Opus 5.5) et du lecteur d'appariement (Sonnet 5.5, fait 6). Seul D (Kimi) est hors des deux lignées. Tout avis du collisionneur sur « quelle convention d'appariement se défend » est donc donné en partie par les parties elles-mêmes.
- R-3. Aucune référence bibliographique citée dans les pièces (Chao 1984 et 1987, Good 1953, Fienberg 1972, Cormack 1989, Chao et collègues 2001 et 2014, Link 2003, Haberman 1974, Otis et collègues 1978, Chapman 1951) n'a été vérifiée : toutes sont non opposables (règle R7) et à contrôler sur document empreinté avant tout usage.

---

## 1. Conformité au périmètre

Règle appliquée (critère 2) : une pièce qui décrit une famille, un comportement d'agent ou un moyen, même à titre d'illustration ou de justification, ou qui anticipe ce que concevront les instances du bloc 4, est écartée et comptée. Ligne de partage que j'ai suivie pour être constant : **sort** un passage qui nomme une *modalité* d'un moyen ou une *dimension de contenu* des familles ; **reste** un passage qui ne parle que d'un événement statistique (score sous le seuil, sélection conditionnée par la sortie de la défense) ou d'une base de comparaison côté défense.

| Pièce | Verdict | Passages (par leur place) |
|---|---|---|
| A1 | Dans le périmètre | Bloc 3, Q5, « piège » : met en garde contre la description de l'usage de l'information par le régime informé, sans la faire. Conservé. |
| A2 | Dans le périmètre | Sur C, défaut 4 : cite le palier 2 de C1 pour en critiquer le biais de sélection. Conservé. |
| A3 | Dans le périmètre | « Étalon d'appariement » : déclare n'en décrire aucun contenu. Conservé. |
| B1 | Dans le périmètre | Section (c), instrument 2 : bases triviales côté défense (moniteur à un seul trait, classificateur de perplexité). Ce sont des bases à battre de la défense, pas un comportement d'agent. Conservé. |
| B2 | Dans le périmètre | — |
| B3 | Dans le périmètre | — |
| **C1** | **Écartée, comptée (1)** | Bloc 1(b), point 3 (« cloisonnement », de la défense vers l'évaluation) : la justification nomme une modalité de contournement d'un moniteur. Bloc 4, ligne 1, option B : nomme des axes de contenu selon lesquels stratifier les consignes des instances, ce qui anticipe ce qu'elles concevront. Le palier 2 du bloc 1(b) (« région sous le seuil ») reste, seul, du côté statistique. |
| C2 | Dans le périmètre | Sur B, (b) 3 : « familles aveugles aux sondes » désigne une composante d'un mélange de lois, sans contenu. Conservé. |
| C3 | Dans le périmètre, à la limite | Tableau (a), ligne C-04, et page (c), question 4 : le palier informé « sélectionne statiquement le pire paramétrage sous les seuils connus ». Événement statistique sans modalité : conservé, mais la formulation ne doit pas passer dans le texte III. |
| D1 | Dans le périmètre | — |
| D2 | Dans le périmètre | — |
| D3 | Dans le périmètre | — |
| **Argon seul** | **Écartée, comptée (2)** | Bloc 4, point 1, option B et recommandation hybride : donne en exemple des paramètres concrets de construction des familles demandées aux instances. Bloc 3, question 4, « risque hors périmètre » : nomme une modalité de moyen. |

**Bilan** : 2 pièces écartées sur 13 (C1, Argon seul). Conséquences : la position de C au tour 1 n'entre dans aucun compte (C est lue par C3, qui révise tout et reste dans le périmètre) ; Argon seul, déjà hors du « commun » par le critère 6, n'est rappelé que « pour mémoire » dans les blocs 1 à 4, sans entrer dans aucun compte. **Lecture indulgente possible** (si le directeur juge ces passages dans le périmètre) : C1 n'apporterait que la question « zone aveugle des refus », abandonnée par C3 elle-même ; Argon seul apporterait deux questions propres (fidélité distributionnelle du banc simulé dans l'espace des activations ; transfert des seuils du modèle de 8 milliards vers celui de 70 milliards), à reposer alors depuis une source conforme.

**Signalements des critères 4 et 5** (n'écartent pas) :
- Statuts changés ou mal employés : A1 (a), le fait 1 (VÉRIFIÉ) est dit « RAPPORTÉ par la décision N-056 » avant correction ; C2, des citations d'autres cellules marquées « OBSERVÉ-NON-AUDITÉ » ; C3, page (c) point 6, « Kimi et Gemini, VÉRIFIÉ point 13 » présentés comme lignées tierces, alors que le fait 13 ne vérifie que la liste des modèles et que Gemini est la lignée de la première source ; D1, Q1 et Q5, « cinq familles scellées (RAPPORTÉ) » alors que le fait 4 rapporte cinq **instances** (corrigé en D3) ; Argon seul, ancrage, des propositions propres marquées « RAPPORTÉ », et bloc 4 point 1, une corrélation « observée » marquée VÉRIFIÉ sans fait correspondant ; Argon seul, bloc 2, des propriétés de bancs (format, licence, étiquetage) affirmées sans statut alors que le fait 11 les tient pour HYPOTHÈSE.
- Calculs : B3, convention grossière, le texte dit « Chapman = 36,7 » alors que le calcul affiché donne 37,16 (29 × 25 / 19 − 1). C3, page (c) point 1, rappelle « 36,8 ou 38,9 » et « 36,7 ou 38,7 » sans apparier chaque valeur à sa convention. Toutes les autres pièces disent leur convention (m = 18 ou m = 19).
- Estimateur sans ses hypothèses (non jugeable en l'état) : C3, duel 1, « Chapman-Min » (borne inférieure par rééchantillonnage du minimum des dix Chapman par paire) ; B1, « approche bayésienne » citée sans hypothèse.
- Incohérence restée après le tour 3 : A3, « test de faisabilité arithmétique », multiplie la borne à zéro échec par l'effet de plan 1 + (g − 1)ρ, formule que A2 (sur C, défaut 6) jugeait inadaptée à une borne à zéro échec (il faut compter les grappes indépendantes, ce que C3 et D3 adoptent).

---

## 2. Bloc 1 — préalables

### 2(a) Définition opérationnelle de l'universalité

| Source | Définition recommandée (classe, quantificateur, statistique) |
|---|---|
| A3 | Principal : **pour toute** famille de la classe observée scellée, s(f) ≥ τ, au grain le plus fin (pire cas, vérifiable par rejeu). Complément séparé : **enveloppe** de la part d'échec sur la population capturable, la borne haute supposant que toute la masse manquante échoue. L'énoncé « avec confiance 1 − α, part d'échec ≤ ε sous la loi du mécanisme » n'est préenregistré que s'il passe un test de faisabilité. Prédiction scellée notée par score strictement propre comme engagement réfutable. |
| B3 | Principal : **proportion** — avec confiance 1 − α, la part de la population de familles où la défense échoue est inférieure à ε ; écart vues/tenues à l'écart comme diagnostic seulement. |
| C3 | « (τ, ε, couverture minimale)-universelle » sur le support des familles découvrables (probabilité de capture non nulle) : (1) borne inférieure de la couverture d'incidence au-dessus d'un minimum, **et** (2) borne supérieure de la proportion de **grappes** indépendantes en échec ≤ ε. |
| D3 | Classe finie exhaustivement testée : chaque famille satisfait le critère. Familles découvertes : **proportion**, avec confiance 1 − α, conditionnelle à la loi, au mécanisme de découverte, à l'unité d'échantillonnage et au critère déclarés ; **abstention** sans plan d'échantillonnage qui défende cette loi. |
| Argon seul (pour mémoire) | Proportion d'échec bornée par la proportion observée plus la masse manquante de Good-Turing, toute la masse manquante comptée en échec. |

- **Verdict du critère 1 : divergente.** Aucune paire de modèles ne retient la même classe, le même quantificateur et la même statistique comme définition principale (A3 : pour-tout sur la classe observée ; B3 : proportion sur la population ; C3 : proportion sur des grappes plus condition de couverture ; D3 : proportion conditionnelle avec abstention). B3 et D3 partagent le quantificateur et la statistique, mais pas la classe (D3 conditionne explicitement à l'unité du plan et au mécanisme, et s'abstient sinon). Options au format décision : section 7, décision 1.
- **Convergences** (A3, B1, C3, D1 et D3 ; Argon seul dans le même sens) : « universelle sur la classe déclarée » est un énoncé conditionnel ; « robuste à l'inconnu » n'est définissable que relativement à un mécanisme de découverte déclaré ; la zone à capture nulle (refus commun) est hors de toute garantie, et l'énoncé doit le dire par écrit. L'écart vues/tenues à l'écart n'est pas une définition (A3, B3, D3), parce qu'il confond surajustement et déplacement de difficulté (C2 sur B, D2 sur A).
- **Ma recommandation** : poser dans le texte III deux énoncés distincts, jamais fusionnés : (i) le pire cas sur la classe observée scellée (vérifiable par rejeu, A3, D3) ; (ii) une proportion conditionnelle à une unité d'échantillonnage déclarée par le plan, avec abstention obligatoire (D3), et la borne de la masse manquante rapportée en enveloppe (A3) plutôt qu'insérée dans la borne (critique de D2 et B2 contre la définition pondérée par la couverture). Confiance : moyenne.

### 2(b) Régime d'information

- **Convergences** : chaque palier est rapporté séparément et scellé avant le suivant (A1, C3, D1) ; budgets fixés avant ouverture des scellés (A1, D1) ; aucun retour par famille vers les concepteurs, aucune révision de seuil après lecture (A1, B1, D1) ; lot de calibration des seuils disjoint du lot qui mesure les fausses alertes (critique A2 acceptée par B3 et C3, reprise par A3) ; l'écart entre paliers n'est interprétable qu'à familles, budget et statistique identiques, avec une double exécution à information identique comme loi nulle (A3, C3, D3, sur la critique D2).
- **Divergences** :
  - contenu du palier informé : A1 (jusqu'au code et aux poids) et C3 (seuils et poids figés) contre B1 (protocole et familles vues, **pas** les poids) ;
  - nature des paliers : échelle ordinale (A1) ou catégories (A3, après D2) ;
  - le banc informé et les concepteurs des familles tenues à l'écart : B3 les sépare explicitement après A2 ; D1 interdit au banc informé les graines, contenus et clés d'appariement des familles scellées ;
  - sélection sur la sortie de la défense au palier informé : critiquée par A2 et D2 (l'ensemble évalué dépend alors de la défense et l'énoncé par proportion tombe) ; C3 la garde en séparant éléments de sélection et éléments de score.
- **Budget** : B3, 400 éléments par famille pour ± 0,05 (illustratif ; 100 corrigés après A2) ; C3, 50 éléments de sélection et 50 de score au palier informé (illustratif) ; A1, nombre d'éléments par famille fixé par simulation pour que l'erreur-type par famille soit sous la moitié de l'écart entre familles.
- **Ma recommandation** : régime par catégories (A3), comparaison seulement à familles et budget fixés (A3, D3), lots de calibration et de mesure disjoints. Laisser hors du texte III toute description de ce que fait le banc informé de son information (A1, piège de Q5). Confiance : élevée sur les interdits, moyenne sur la place du palier informé dans le texte III.

### 2(c) Nombre de familles, par simulation

- **Convergences** : les seuils 29, 59 et 149 du fait 9 sont repris par tous, avec la réserve du fait 9 (tirage indépendant selon la loi qui définit ε) ; la garantie dépend du mécanisme de découverte, et la simulation ne démontre la calibration que **conditionnellement** au générateur (A1, B1, D1) ; modèle à deux niveaux (difficulté par famille, puis éléments) et grappes de familles proches (A1, B1, D1).
- **Correction acceptée** : la dépendance se traite en comptant des **grappes** indépendantes, non en divisant par l'effet de plan d'une moyenne (A2 sur C ; accepté par C3 ; D3 va plus loin). **D3** : l'unité indépendante est définie par le plan avant mesure, et des familles issues d'une même instance restent une grappe sauf validation préenregistrée. Conséquence que je dérive : avec cinq instances, si chaque instance est une grappe, au plus cinq unités indépendantes ; la borne à zéro échec ne donne alors rien d'utile (cinq unités réussies bornent ε à environ 0,45 à 95 %, dérivé de la formule du fait 9).
- **Faisabilité** : A3, avec une estimation du nombre de familles d'environ 37 à 39 (fait 8), ε = 0,05 (59 familles) est hors d'atteinte même en observant toute la population, et ε = 0,10 ne tient que sans dépendance ; C2 (sur D) : une garantie à quatre strates demanderait 344 familles (dérivé, juste) ; B2 : avec une corrélation intra-grappe forte, 29 familles en valent environ 50.
- **Règle d'arrêt séquentielle** : martingale de test par valeurs électroniques (A1), mélange de Ville (B1), dépense d'α (D1). C2 montre que la propriété de surmartingale casse si l'ordre d'arrivée est autocorrélé ; A2 rappelle que la dépense d'α suppose une information maximale fixée. A3 garde la règle à titre d'HYPOTHÈSE, sous contrôle d'arrivée groupée, sinon plan à effectif fixe ; D3 exige le taux de fausse certification à chaque temps d'arrêt.
- **Ma recommandation** : imposer avant tout préenregistrement le test de faisabilité (A3, contrôle C2), mais en comptant des grappes (D3) ; déclarer d'avance l'unité indépendante ; retirer ε = 0,05 sauf apport de familles nouvelles indépendantes. Confiance : élevée sur l'arithmétique, moyenne sur le choix de l'unité.

### 2(d) Familles encore inconnues

- **Vérification** : les quatre valeurs du contexte sont exactes pour A1, B1, D1 et D3 (Argon seul de même) : 38,89 et 36,84 (Lincoln-Petersen), 38,68 et 36,70 (Chapman).
- **Convergence au tour 3** : les deux calculs bruts mélangent les unités (n₁ en unités de la première source, n₂ en unités de la seconde) ; aucun n'est défendable tel quel (A1, C2 sur B, D1, D3, B3 après critique). Recodages cohérents, refaisables : **grain grossier** n₁ = 28, n₂ = 24, m = 18 → Lincoln-Petersen 37,33, Chapman 37,16 ; **grain fin** n₁ = 29, n₂ = 25, m = 19 → Lincoln-Petersen 38,16, Chapman 38,00 (A1, D3 ; C3 pour Chapman). Comptage brut à battre : 34 ou 35.
- **Recommandations** : A1 et A3, grain grossier pour l'estimation du nombre, grain fin pour la mesure par famille, les deux en sensibilité ; B1 défendait m = 19 avec n₁ = 28, **abandonné** en B3 pour le grain grossier plus le grain fin en parallèle ; C3, enveloppe [37,16 ; 38,00] ; D3, deux scénarios qui ne forment pas un intervalle de confiance, la scission fine étant une imputation d'unité ; Argon seul (pour mémoire), grain grossier par composantes connexes. **Fait nouveau (A2, constat transversal, repris par C3 et D3)** : le sens 1 → 2 de la non-bijectivité peut venir du lecteur, qui est de la lignée de la seconde source ; m = 18 contre m = 19 sont alors deux hypothèses sur le lecteur, à tester par un étalonnage.
- **Sens des biais (accord, A1, C2, D1)** : dépendance positive et hétérogénéité gonflent m et font sous-estimer le nombre ; faux appariements → sous-estimation ; appariements manqués → surestimation. B1 inversait le signe dans son duel 1 (relevé par A2, C2, D2 ; corrigé en B3).
- **Estimateurs multi-sources (accord au tour 3)** : borne inférieure de Chao (version incidence, Chao2 ; 37,56 à deux sources, A1, dérivé) ; modèles log-linéaires **parcimonieux** (termes de lignée déclarés d'avance, un ou deux degrés de liberté), parce que la table à 31 cellules pour environ 38 familles est creuse et que les estimateurs du maximum de vraisemblance peuvent ne pas exister (C2, accepté par A3 et B3) ; classes latentes et approche bayésienne en **sensibilité seulement**, parce que l'hétérogénéité rend le nombre non identifiable à nombre fini de sources (C2 sur D, accepté par D3) ; Good-Turing pour la masse manquante en **version incidence**, la formule d'abondance d'A1 (couverture 0,69) étant retirée en A3 après C2. Chao2 perd sa propriété de borne inférieure sous faux négatifs d'appariement (C2 sur B, repris par A3 et B3).
- **Indépendance** : non testable à deux sources (A1, D1 ; B1 le tentait, corrigé en B3 après A2, C2, D2). Contrôles exigés : deux listes d'un même modèle (dépendance maximale), captures de Bernoulli indépendantes sur population connue (A2, D2 ; repris par B3, C3, D3).
- **Refus commun** : accord des cinq sources : strate à capture nulle, invisible pour tout estimateur ; l'estimation porte sur la population capturable. Les journaux de refus mesurent la censure et ne sont pas une source de capture (A1, D1, C2 ; B3 l'accepte après avoir dit le contraire en B1).
- **Population non fermée** : estimer le nombre à une date donnée, la courbe d'accumulation et la masse manquante (A1, D1) ; test de fermeture comme diagnostic, jamais comme preuve (A3, D3).
- **Ma recommandation** : rapporter les deux recodages comme scénarios, ne plus citer les valeurs brutes 36,7 et 36,8 ; borne de Chao2 et modèle log-linéaire parcimonieux à cinq sources, après étalonnage du lecteur ; énoncé restreint à la population capturable. Confiance : élevée.

---

## 3. Bloc 2 — données de départ recommandées

| Donnée | A | B | C3 | D | Accord |
|---|---|---|---|---|---|
| (i) Bancs publics | Trois nommés (SHADE-Arena, ControlArena, Liars' Bench) comme familles extérieures, après mesure du recouvrement par date ; indépendance faible (le programme les a lus) | **Un seul**, après vérification de la licence et de l'étiquetage | Trois (ControlArena, SHADE-Arena, Liars' Bench), **30 trajectoires** (illustratif) pour un test de transport ; licence et étiquetage HYPOTHÈSE | **Trois au plus**, après audit (version, licence, provenance, schéma, étiquetage, exposition publique) | 4 sur 4 : propriétés inconnues, audit avant usage ; seul le nom est VÉRIFIÉ (fait 10) |
| (ii) Journaux de refus | Censure, pas capture | B1 : source de capture ; **B3 : censure seulement** | Censure (C2 contre B1) ; taux de refus de base sur questions neutres | Censure ; indépendance faible | 4 sur 4 au tour 3 : censure seulement |
| (iii) Propositions brutes d'une course précédente | Troisième occasion de capture, déclarée dépendante ; test de stabilité dans le temps | Troisième source, indépendance douteuse | Non traité | Source possible, qui ne corrige pas une dépendance commune | 3 sur 3 qui en parlent : source supplémentaire **dépendante** |

- Données brutes plutôt que résumés : accord (A1, D1), parce que l'appariement doit pouvoir être refait par un tiers et que les résumés faussent le compte des familles vues une seule fois.
- MonitoringBench et SLEIGHT-Bench : aucune source conforme ne les décrit ; A1, B1 et D1 disent ne pas les connaître. Aucun format ni aucune licence n'est attesté pour aucun banc : tout reste HYPOTHÈSE (fait 11).
- Divergence : l'indépendance des bancs publics, faible pour A1 et D1, « de conception » pour Argon seul (pour mémoire).
- Ma recommandation : (ii) pour mesurer la censure, (iii) comme source dépendante déclarée, (i) seulement après l'audit de D3, et jamais dans la liste scellée de G1 sans décision à part (décision N-061). Confiance : moyenne.

---

## 4. Bloc 3 — questions candidates (dédoublonnées)

Versions finales du tour 3 pour A, B, C, D ; tour 1 seulement pour le chiffre quand le tour 3 renvoie au tour 1. Application du critère 3 : une **simulation à vérité connue seule n'est pas une validation extérieure** (D2 le dit contre B ; la question définit la validation extérieure comme familles conçues hors du programme, prédictions scellées confrontées à des mesures, ou revue extérieure). Une question fusionnée est retenue si au moins une de ses sources donne une validation extérieure chiffrée et un piège nommé.

### Q-I. Estimer le nombre de familles capturables et la masse manquante à partir de plusieurs sources dépendantes, sous appariement non bijectif
- Fusion de : A3-Q1 (estimation avec cinq sources, ordre tiré au sort, prédiction scellée du gain de la dernière), B3-Q1 (borne de Chao2 multi-sources), C3-Q1 (enveloppe de capture-recapture sous graphe biparti), D3-Q2 (estimation du nombre à une date donnée sur vérité connue).
- Avantage : exploite les cinq sources prévues (fait 4), qui rendent les interactions estimables (A1) ; part d'une anomalie VÉRIFIÉE (m = 18 contre 19).
- Piège : table creuse et estimateurs inexistants (C1 repris par C2) ; appariement unique ou non aveugle qui injecte la dépendance à mesurer (A1) ; strate à capture nulle présentée comme absente (D3) ; source finale non échangeable (D2 sur A).
- Validation extérieure chiffrée : prédiction scellée du gain de la dernière source, intervalle à 90 % (illustratif, A1, A3) ; inclusion de **15 familles extérieures** de bancs publics dans l'intervalle de couverture, plus couverture ≥ 90 % sur 2 000 mondes (illustratifs, C3). B3 et D3 : simulation seule.
- Risque hors périmètre : faible (A1, B1, C3, D3 ; illustratif) ; borné par l'usage des seules tables d'incidence.
- Sort : **retenue** (A, C). Les versions de B3 et D3 seules ne l'auraient pas été.

### Q-II. Mesurer l'erreur d'appariement des lecteurs et la propager dans l'estimation
- Fusion de : B3-Q4, C3-Q3, D3-Q3 ; A3 l'intègre au plan (« étalon d'appariement »).
- Avantage : le fait 6 montre un lecteur unique, de la lignée d'une source ; c'est le préalable de tout estimateur, et l'origine du 1 → 2 devient testable (A2, C3).
- Piège : accord entre lecteurs pris pour justesse (D2) ; kappa inadapté à un graphe non bijectif (A2) ; lecteurs de même lignée (B1) ; énumération de « tous les appariements plausibles » qui diverge (C2 sur D).
- Validation extérieure chiffrée : trois lecteurs de fournisseurs différents, accord au niveau des liens ≥ 0,80 (illustratif, B3) ; 10 paires identiques permutées et 10 scissions connues insérées à l'aveugle, erreur < 5 % (illustratifs, C3) ; double lecture extérieure de 100 % des liens (illustratif, D1, D3).
- Risque : faible (B3, C3, D3 ; illustratif).
- Sort : **retenue**.

### Q-III. Borner la part d'échec quand les familles sont découvertes et non tirées
- Fusion de : A3-Q2 (enveloppe sur la masse manquante), B3-Q3 (sensibilité de la borne à zéro échec au biais de découverte), C3-Q2 (correction par post-stratification selon la fréquence de capture).
- Avantage : attaque le point faible du fait 9 (tirage indépendant non satisfait) ; c'est le cœur de l'énoncé d'universalité.
- Piège : poids de Horvitz-Thompson fondés sur le nombre de sources qui captent une famille, tronqué et non identifiant (C2, D2 ; A3 retire cette pondération) ; non-identifiabilité du lien découverte-difficulté (C1, B2) ; strate à capture nulle.
- Validation extérieure chiffrée : cinq lots extérieurs scellés ; chiffre déjà connu : borne haute à zéro échec ≥ 0,08 (A3, dérivé, juste) ; au moins 20 familles extérieures bornent ε à environ 0,14 (A1, dérivé, juste) ; lot scellé de 15 familles tenues à l'écart (illustratif, C3), soit ε ≈ 0,18 à zéro échec (dérivé ici). B3 : simulation seule.
- Risque : faible (A1, B1, C3 ; illustratif).
- **Divergence interne non résolue** : corriger (C3, par post-stratification), encadrer sans corriger (A3, enveloppe), ou s'abstenir (D3). C3 la transforme en duel (signe de la différence de puissance).
- Sort : **retenue** (A, C).

### Q-IV. Valider la borne d'universalité sous variance à deux niveaux, dépendance et arrêt séquentiel ; dimensionner le plan
- Fusion de : A3-Q4 (règle d'arrêt sous arrivée groupée), B3-Q5 (puissance selon le nombre de familles et d'éléments), D3-Q1 (borne d'universalité avec abstention) ; le test de faisabilité d'A3 et le contrôle de C2 s'y rattachent.
- Avantage : dit d'avance quels énoncés sont atteignables (ε = 0,05 ne l'est pas, A3) et économise le calcul sur le modèle de 70 milliards (A1).
- Piège : compter sorties ou éléments comme familles indépendantes (D3) ; martingale cassée par l'autocorrélation (C2) ; modèle bêta-binomial mal spécifié sous loi bimodale (C2 sur B).
- Validation extérieure chiffrée : revue par un statisticien extérieur, couverture simulée ≥ 0,93 pour 0,95 nominal (illustratif, A1) et jeu public à dépendance connue (A3) ; 29 ou 59 unités réussies (fait 9, D3) ; ≥ 30 familles pour confronter la variance prédite (illustratif, B1).
- Risque : faible (A1, B1, D3 ; illustratif).
- Sort : **retenue** (A, D).

### Q-V. Mesurer la transportabilité d'une prédiction scellée des familles vues vers les familles tenues à l'écart
- Fusion de : A3-Q3 (score strictement propre contre une référence, sans attribuer la cause), B3-Q2 (écart vues/tenues à l'écart, distinguable ou non du déplacement de difficulté).
- Avantage : directement réfutable par une prédiction scellée.
- Piège : écart confondu avec la différence de difficulté entre mécanismes de découverte (C2, D2) ; loi nulle contaminée par la calibration des seuils (B2) ; prédiction dégénérée « calibrée » (B2).
- Validation extérieure chiffrée : **≥ 15 familles extérieures** (illustratif, B1, B3) ; marge 0,02 sur le score de Brier (illustratif, A3).
- Risque : faible (A1, B1 ; illustratif).
- Sort : **retenue**, avec la réserve écrite que la cause d'un écart reste non attribuable sans covariable de difficulté indépendante de la défense (HYPOTHÈSE qu'elle existe, A3).

### Q-VI. Tester le transport vers des données extérieures (bancs publics) et leur contamination
- Fusion de : C3-Q5, D3-Q4. Parente de Q-V, distincte par la source des données.
- Avantage : seules données conçues hors du programme.
- Piège : recouvrement avec l'entraînement, non identifiable par un test interne (D3) ; loi de découverte différente, qui empêche de calibrer Good-Turing (A2, D2) ; étiquetage construit après observation (D1).
- Validation extérieure chiffrée : test d'échangeabilité sur **30 trajectoires brutes** avant déscellement (illustratif, C3) ; D3 : trois bancs au plus, audit de 100 % des champs, seuil fixé après audit et avant mesure (pas de seuil chiffré).
- Risque : moyen (D1, D3), faible (C3) ; illustratifs.
- Sort : **retenue** par C3 seule ; la version de D3 seule ne l'aurait pas été. Dépend de propriétés de bancs non vérifiées (fait 11).

### Q-VII. Mesurer l'écart entre évaluation aveugle et évaluation informée
- Fusion de : A3-Q5, C3-Q4, D3-Q5.
- Avantage : la décision N-056 impose déjà les deux versions (fait 1).
- Piège : budgets ou familles différents (D1) ; sélection sur la sortie de la défense (A2, D2) ; paliers lus comme une échelle (D2).
- Validation chiffrée : séparation 50/50 entre éléments de sélection et de score sur 20 familles (illustratif, C3) ; intervalle à 95 %, taille fixée par la puissance (D3) ; A3 sans chiffre. Validation surtout interne au plan.
- Risque : **moyen** (A1, C1 avant écart, C3), faible (D3) ; c'est la seule question où le risque d'être jugée hors périmètre tient au contenu même.
- Sort : **retenue de justesse** (chiffre de C3) ; je recommande de ne pas la mettre dans le texte III (section 7, décision 4).

**Pour mémoire, écartées avec leur pièce (critère 2)** : C1-Q4 (zone aveugle des refus, abandonnée aussi par C3) ; Argon seul Q1 à Q3 (jumelles de Q-I, Q-II, Q-III), Q4 (fidélité distributionnelle du banc simulé) et Q5 (transfert de seuils de 8 vers 70 milliards), non jugées.

**Classement des questions retenues** (poids : cœur de l'énoncé d'universalité, nombre de sources, validation extérieure, risque de périmètre) :
1. Q-III, borne de la part d'échec sous découverte non aléatoire (A, B, C ; extérieure : A, C ; risque faible).
2. Q-I, nombre de familles capturables et masse manquante (A, B, C, D ; extérieure : A, C ; risque faible).
3. Q-IV, validation et faisabilité de la borne (A, B, D ; extérieure : A ; risque faible) : elle décide quels énoncés de Q-III sont atteignables.
4. Q-II, erreur d'appariement (B, C, D, et A dans le plan ; risque faible) : c'est la **première expérience** pour A3, C3 et D3, mais une question étroite, qui peut entrer comme exigence de Q-I.
5. Q-V, transportabilité d'une prédiction scellée (A, B).
6. Q-VI, transport vers les bancs publics (C, D ; dépend du fait 11).
7. Q-VII, aveugle contre informé (A, C, D ; risque de périmètre moyen).

---

## 5. Bloc 4 — organisation des cinq instances

| Point | Accord | Désaccord |
|---|---|---|
| Consigne | Noyau identique, scellé par empreinte (A3, B3, C3, D3) | Variations : de format seulement (A3) ; aucune (B3 ; C3 après abandon des deux passes) ; variations préenregistrées et analysables permises (D3) |
| Fuites | Contextes isolés ; chaque sortie hachée et scellée avant lecture d'une autre ; journal horodaté (les quatre) | Niveau d'isolement : opérateurs distincts (A1), tiers de confiance sans réseau (B3), séquestre chiffré (C3), comptes, stockages et coordinateurs séparés (D3) |
| Appariement | Au moins trois lecteurs, aveugles à la source, de lignées distinctes des sources ; étalon à vérité connue (copie permutée, listes sans lien, relations 1 → 2 connues) ; liens multiples permis (A3, B3, C3, D3) | Propagation : matrice de confusion dans la vraisemblance (A3, C3), taux de faux liens (B3), intervalle par appariement cohérent plus dispersion entre scénarios (D3) ; la combinaison des lecteurs par imputation multiple est abandonnée (C2, A3) |
| Indépendance | Les sorties ne prouvent pas l'indépendance des corpus d'entraînement (D1, D3 ; HYPOTHÈSE chez A3) ; termes de lignée dans un modèle log-linéaire parcimonieux ; contrôle positif par deux exécutions d'un même modèle (A3, B3, C3, D3) | Étalonnage sur une énumération neutre : utilisable comme a priori ou proxy (A3) contre simple hypothèse de modèle (D2, D3) |
| Sources multiples | Comptage brut, borne de Chao2, log-linéaire parcimonieux, sensibilités ; Chapman par paire en comparaison (les quatre) | Validation en retirant une source : seulement sur modèle parcimonieux (C2, D3) |
| Refus | Enregistré tel quel, jamais reformulé (fait 14) ; traité comme censure, jamais comme capture vide (les quatre) | **Remplacement** : substitut prédéclaré d'une autre lignée (A3) ou deux instances de réserve (B3), contre aucun remplacement traité comme source équivalente, pour éviter de sélectionner les sources sur leur permissivité (A2 contre C1, puis C3, D3) |

- Point ajouté par C3 (accepté sur le fond en réponse à A2) : les cinq instances doivent être de lignées disjointes de celles des deux sources de départ, ou ces deux sources confinées aux familles vues. Avec la réserve R-2, cela vaut aussi pour les lecteurs.
- Ma recommandation sur le désaccord du refus : exécuter un substitut s'il est prédéclaré, mais l'analyser à part, avec et sans lui, et ne jamais le compter comme source équivalente (D3). Confiance : moyenne.

---

## 6. Critiques croisées (tour 2) et réponses (tour 3)

**Acceptées (principales)**
- A : sa « couverture » mesurait la puissance (C2) → fausse certification bornée par α, puissance et largeur séparées ; pondération de Horvitz-Thompson retirée (C2, D2) ; formule de Good-Turing d'abondance retirée (C2) ; imputation multiple abandonnée (C2) ; loi nulle par scission contaminée (B2) → deux lots scellés tirés de la même loi ; prédiction notée par score strictement propre (B2) ; test de fermeture et étalon d'appariement ajoutés (B2).
- B : signe du biais de Lincoln-Petersen inversé dans le duel 1 (A2, C2, D2) ; duel 2 circulaire (A2, C2, D2) ; test d'indépendance à deux sources impossible, et contrôle par partition erroné (A2, C2, D2) ; unités mélangées avec m = 19 (A2, C2, D2) ; budget par famille faux d'un facteur 4 (A2) ; kappa inadapté (A2) ; journaux de refus pris pour une source de capture (C2, D2).
- C : duels non exclusifs (A2, D2) → statistique de bascule unique ; sous-dimensionnement (A2, B2) → 40 familles ; attribution erronée d'un modèle de population ouverte (A2) ; effet de plan appliqué à une borne à zéro échec (A2, B2) ; incertitude de la couverture non propagée (A2, B2, D2) ; consignes en deux passes et remplacement de 7 à 5 instances abandonnés (A2, B2, D2).
- D : « cinq familles » au lieu de cinq instances (A2) ; duels vrais par construction (A2, B2, C2) ; borne binomiale exacte sous dépendance ; familles effectives non définies → unité fixée par le plan ; garantie stratifiée retirée de la définition principale (C2 : 344 familles pour 4 strates).

**Rejetées ou acceptées en partie**
- A3 rejette la prémisse de B2 (moins de 10 familles tenues à l'écart), HYPOTHÈSE de B, mais accepte le calcul de puissance préenregistré ; elle rejette pour moitié B2 sur la fusion d'unités (la fusion ne sert qu'à l'estimation du nombre).
- C3 rejette A2 sur son ancrage (citation des modèles du collisionneur), tout en acceptant le fond (lignées disjointes).
- D3 rejette en partie B2 sur le bloc 2 (des recommandations existaient) ; le test de fermeture est « rejeté comme preuve, transformé en diagnostic ».

**Dissensus irréductibles transformés en expériences**
1. Chao2 contre Chapman à petit effectif hétérogène et dépendant (A3, B3, C3, D3 : duel 1 de chacun ; C3 avec une statistique de bascule unique).
2. Corriger, encadrer ou s'abstenir face au biais de découverte (C3 duel 2 : signe de la différence de puissance ; A3 duel 3 : enveloppe ; D3 : abstention obligatoire), avec le contrôle d'un monde bimodal où la masse rare échoue (C2).
3. Proportion contre pire cas (B3 duel 2 : puissance à 60 familles ; D3 duel 2 : règle d'écart contre règle de proportion).
4. Origine du 1 → 2 : lecteur ou taxonomie (A2 transversal → étalonnage du lecteur en C3 et D3).
5. Indépendance des sources : modèle d'hétérogénéité seul contre modèle avec termes de lignée (B3 duel 3).
6. Fermeture de la population : courbe d'accumulation datée (A3, D3).
7. Effet du régime d'information : double exécution à information identique (A3, C3, D3).

**Première expérience** (convergence des quatre réponses) : sur processeur seulement, un monde simulé à vérité connue (environ 38 familles, cinq sources, appariement non bijectif, erreurs de fusion et de scission, captures dépendantes par lignée ; A3, B3, D3), précédé de l'étalonnage du lecteur (C3, D3). C3 propose de ré-apparier tout de suite les 28 et 25 familles existantes par des lecteurs d'autres lignées.

---

## 7. Recommandation pour le texte III

**Verdict.** Retenir une question principale (fusion de Q-III et Q-IV) et une question seconde (fusion de Q-I et Q-II). Laisser hors du texte III le régime aveugle contre informé (Q-VII) et le transport vers les bancs publics (Q-VI), le premier pour son risque de périmètre, le second parce que les propriétés des bancs restent des hypothèses (fait 11). Q-V peut entrer comme validation de la question principale.

**Question principale (proposée, niveau méthode).** « Une défense est évaluée sur des familles découvertes par un nombre fini de sources dépendantes, et non tirées au hasard. Propose la méthode qui permet d'affirmer devant un tiers une borne sur la part de familles où elle échoue : (1) l'unité d'échantillonnage indépendante, déclarée par le plan avant toute mesure ; (2) l'énoncé autorisé, avec sa classe, son quantificateur et sa statistique, en séparant le pire cas sur la classe observée scellée de la proportion sous la loi du mécanisme de découverte ; (3) le traitement de la masse non découverte et de la strate à capture nulle ; (4) le test de faisabilité qui retire un énoncé inatteignable, et la règle d'abstention ; (5) la validation : prédictions scellées confrontées aux familles tenues à l'écart, et contrôles sur mondes simulés à vérité connue (monde sans masse manquante, monde bimodal où la masse rare échoue, défense constante). » Sources : A3, B3, C3, D3. Chiffres d'appui : 29, 59 et 149 (fait 9) ; borne haute ≥ 0,08 à zéro échec avec 34 familles observées sur environ 37 à 39 (A3, dérivé) ; 15 à 20 familles extérieures (illustratif, A1, C3).

**Question seconde (proposée).** « Propose la méthode pour estimer, avec ses hypothèses explicites, le nombre de familles capturables et la masse manquante à partir de cinq sources dont l'appariement est non bijectif et fait par des lecteurs faillibles : mesure des faux liens, des liens manqués et des erreurs de grain sur un étalon à vérité connue ; propagation dans l'estimation ; modèles parcimonieux et bornes inférieures ; test de fermeture ; prédiction scellée de l'apport de la dernière source ouverte. » Sources : A3, B3, C3, D3. Chiffres d'appui : recodages cohérents 37,16 et 38,00 (Chapman ; faits 7 et 8, dérivé) ; étalon de 10 + 10 paires, erreur < 5 % (illustratif, C3) ; accord au niveau des liens ≥ 0,80 (illustratif, B3).

**À trancher par le directeur**

*Décision 0 — périmètre.* Décider si C1 et Argon seul restent écartés. Enjeu : deux questions propres à Argon seul. Options : (a) écart strict, comme ici (avantage : règle constante ; inconvénient : on perd deux pistes) ; (b) lecture indulgente (avantage : deux pistes de plus ; inconvénient : précédent sur « même à titre d'illustration »). Recommandation : (a), et reposer plus tard la piste « fidélité du banc simulé » depuis une source conforme si elle est voulue. Confiance : moyenne. Défaut sous 48 heures : (a).

*Décision 1 — énoncé d'universalité (critère 1 : divergente).* Choisir ce que le texte III impose ou fait comparer. Enjeu : ce que le tiers pourra vérifier. Options : (a) pire cas sur la classe observée scellée, plus enveloppe de la masse manquante (A3) : vérifiable par rejeu, mais muet hors de la classe ; (b) proportion avec confiance sous la loi du mécanisme, avec abstention (B3, D3) : dit quelque chose de la population, mais n'est atteignable qu'avec assez d'unités indépendantes ; (c) double condition, couverture minimale et proportion de grappes (C3) : complète, mais insère une quantité estimée et reste muette sur la masse à capture nulle (D2). Recommandation : (a) comme énoncé principal, et (b) seulement si le test de faisabilité passe ; le texte III demande de comparer les trois sur un estimand commun. Confiance : moyenne. Défaut : cette recommandation.

*Décision 2 — unité indépendante et cible ε.* Fixer ce qui compte comme unité indépendante. Enjeu : selon D3, des familles d'une même instance forment une grappe ; avec cinq instances, au plus cinq unités, d'où une borne d'environ 0,45 à zéro échec (dérivé). Options : (a) unité = instance : prudent, mais aucune proportion utile ; (b) unité = famille, sous validation préenregistrée de l'indépendance à l'intérieur d'une instance, avec repli sur (a) en cas d'échec : utile si la validation passe, et elle peut échouer ; (c) plus d'instances : seule voie vers ε = 0,10, mais elle demande une dépense, donc un devis et un GO. Recommandation : (b) avec repli sur (a), et ε = 0,05 retiré dès maintenant (59 familles de plus que la population estimée, A3). Confiance : moyenne. Défaut : (b) et retrait de 0,05.

*Décision 3 — refus d'une instance.* Choisir le sort d'une instance qui refuse. Options : (a) substitut prédéclaré, compté comme source (A3, B3) : garde cinq sources, mais sélectionne sur la permissivité (A2) ; (b) aucun remplacement compté, analyses avec et sans substitut (C3, D3) : pas de biais de sélection, mais moins de puissance. Recommandation : (b). Confiance : moyenne. Défaut : (b).

*Décision 4 — régime aveugle contre informé dans le texte III.* Options : (a) l'inclure (avantage : mesure déjà imposée par N-056 ; inconvénient : risque de périmètre moyen, A1, C3) ; (b) le garder comme mesure interne du plan, hors du texte III (avantage : texte sûr ; inconvénient : la course n'apportera rien sur ce point). Recommandation : (b). Confiance : moyenne. Défaut : (b).

*Décision 5 — lignées des lecteurs et des instances.* La lignée des lecteurs est une condition de méthode, pas un choix ouvert (réserve R-2) : lecteurs et instances hors des lignées Argon et Opus, ce que les cinq sources demandent. Le choix concret des fournisseurs relève de la décision de compte et de dépense : à soumettre avec le devis.

Ce qui reste HYPOTHÈSE dans toute la page : fermeture de la population, indépendance et échangeabilité des instances, existence d'une covariable de difficulté indépendante de la défense, propriétés des bancs publics, transport d'une dépendance mesurée sur une tâche neutre.
