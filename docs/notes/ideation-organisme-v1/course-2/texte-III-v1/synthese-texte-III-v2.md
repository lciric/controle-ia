# Synthèse du brainstorm défensif — questions candidates du texte III (mesure de l'universalité) — v2

Lecteur neuf, auteur d'aucune pièce lue. Date : 30 octobre 2026. Remplace la v1 pour la lecture ; la v1 (`synthese-texte-III-v1.md`, empreinte `28cc9bc3…`) reste inchangée.

**Pièces lues, et seulement elles** (dossier `donnees/collisionneur-texte-III-v1/`) : `question-texte-III-envoi-v3.md` ; `criteres-lecture-texte-III-v1.md` (appliqués tels quels, sauf la décision 0 du directeur sur le critère 2) ; `faits-texte-III-v2.md` ; les douze cellules `run-texte-III-e3-v2/cellules/E3-T{1,2,3}-*-{A,B,C,D}.md` ; la réponse d'Argon seul, champ `texte` de la dernière ligne de `/root/ideation-v1/argon-texte-III-v1/reponse-argon-v1.json` (modèle servi : `gemini-4-argon`, fin normale, aucune erreur). Aucune pièce nouvelle n'a été lue pour la v2.

**Notation des sources.** « A1 » = cellule A au tour 1 (conception), « A2 » = critique croisée, « A3 » = réponse aux critiques ; de même pour B, C, D. « Argon seul » = la réponse isolée. Les chiffres marqués « illustratif » ne viennent pas des pièces ou y sont eux-mêmes illustratifs ; « dérivé » = recalculé ici à partir d'une formule des faits. **Marque de scellement** : tout passage hors du niveau méthode est désigné par sa place et remplacé par « [détail scellé, branche donnees/bras-attaque-texte-III-v1] » ; je n'ai pas ouvert cette branche.

**Réserves de lecture, avant tout.**
- R-1. Identité du modèle B : la consigne de synthèse dit « Claude Opus 4.6 » ; le fait 13 (VÉRIFIÉ, `collisionneur_v5.py`, ligne 58) dit `claude-opus-5-5`. Divergence non résolue ici (je n'ouvre pas le code). Je désigne la cellule par « B » seulement.
- R-2. Lignées : C et Argon seul sont le même modèle (`gemini-4-argon`) que la **première source** des données de départ (28 familles) ; A et B sont de la lignée Claude, celle de la **seconde source** (Opus 5.5) et du lecteur d'appariement (Sonnet 5.5, fait 6). Seul D (Kimi) est hors des deux lignées. Tout avis du collisionneur sur « quelle convention d'appariement se défend » est donc donné en partie par les parties elles-mêmes.
- R-3. Aucune référence bibliographique citée dans les pièces (Chao 1984 et 1987, Good 1953, Fienberg 1972, Cormack 1989, Chao et collègues 2001 et 2014, Link 2003, Haberman 1974, Otis et collègues 1978, Chapman 1951, Wilks, Wald, Lan-DeMets, O'Brien-Fleming, Rosenbaum, Heckman) n'a été vérifiée : toutes sont non opposables (règle R7) et à contrôler sur document empreinté avant tout usage.
- R-4. Argon seul n'a été soumis à aucune critique croisée. Quand je dis qu'une critique du tour 2 « vaut par analogie » pour Argon seul, c'est ma lecture : la critique visait une proposition jumelle d'une autre cellule, pas Argon seul.
- R-5. Critère 6 : Argon seul compte désormais dans les convergences et divergences descriptives (consigne du directeur), mais reste hors du verdict « commun » du critère 1, que la décision 0 ne modifie pas.

---

## 0. Ce qui change entre la v1 et la v2

1. **Décision 0 du directeur, lecture indulgente** : C1 et Argon seul, écartés en v1 par le critère 2, sont réintégrés au niveau méthode. Leurs blocs 1, 2 et 4 comptent dans les convergences et divergences. Leurs questions candidates entrent au bloc 3 : C1-Q1 à Q3 et Argon seul Q1 à Q3 rejoignent des questions fusionnées ; Argon seul Q4 et Q5 deviennent Q-VIII et Q-IX ; C1-Q4 est jugée et non retenue.
2. Les quatre passages hors du niveau méthode ne sont ni recopiés ni paraphrasés : ils sont désignés par leur place et remplacés par la marque de scellement (section 1).
3. Signalements ajoutés pour les pièces réintégrées (section 1), dont une incohérence d'Argon seul Q3 : 25 familles ne peuvent pas certifier ε = 0,10 (dérivé).
4. La section 7 intègre les décisions 1 à 4 du directeur (options (c), (c), (a), (a)). Les deux questions sont réécrites en conséquence, la définition d'une instance indépendante est fixée, et il reste trois points à trancher : la fidélité du banc simulé, le transfert de 8 vers 70 milliards, et la cible ε avec le devis.
5. Le classement du bloc 3 passe de sept à neuf questions retenues. Q-VII (aveugle contre informé) n'est plus déconseillée, puisque la décision 4 l'inclut.
6. Inchangés : réserves R-1 à R-3, vérification des calculs, verdict « divergente » du critère 1 sur la définition (tranchée depuis par le directeur), et l'ensemble des acceptations et rejets des tours 2 et 3.

---

## 1. Conformité au périmètre

Règle (critère 2) : une pièce qui décrit une famille, un comportement d'agent ou un moyen, même à titre d'illustration ou de justification, ou qui anticipe ce que concevront les instances du bloc 4, est écartée et comptée. **Décision 0 du directeur** : lecture indulgente ; les pièces concernées sont réintégrées au niveau méthode, et seuls les passages en cause restent scellés. Ligne de partage, inchangée depuis la v1 : **sort** un passage qui nomme une *modalité* d'un moyen ou une *dimension de contenu* des familles ; **reste** un passage qui ne parle que d'un événement statistique (score sous le seuil, sélection conditionnée par la sortie de la défense) ou d'une base de comparaison côté défense.

| Pièce | Verdict | Passages (par leur place) |
|---|---|---|
| A1 | Dans le périmètre | Bloc 3, Q5, « piège » : met en garde contre la description de l'usage de l'information par le régime informé, sans la faire. Conservé. |
| A2 | Dans le périmètre | Sur C, défaut 4 : cite le palier 2 de C1 pour en critiquer le biais de sélection. Conservé. |
| A3 | Dans le périmètre | « Étalon d'appariement » : déclare n'en décrire aucun contenu. Conservé. |
| B1 | Dans le périmètre | Section (c), instrument 2 : bases triviales côté défense. Conservé. |
| B2, B3 | Dans le périmètre | — |
| **C1** | **Deux passages hors périmètre ; réintégrée au niveau méthode (décision 0)** | (1) Bloc 1(b), point 3 (« cloisonnement »), premier tiret, justification entre parenthèses : [détail scellé, branche donnees/bras-attaque-texte-III-v1]. (2) Bloc 4, tableau, ligne 1, option B, contenu de la parenthèse : [détail scellé, branche donnees/bras-attaque-texte-III-v1]. Le reste de la pièce est au niveau méthode. Le palier 2 du bloc 1(b) (« région sous le seuil ») reste du côté statistique, à ne pas reprendre dans le texte III. |
| C2 | Dans le périmètre | Sur B, (b) 3 : composante d'un mélange de lois, sans contenu. Conservé. |
| C3 | Dans le périmètre, à la limite | Tableau (a), ligne C-04, et page (c), question 4 : sélection par le palier informé décrite comme événement statistique, sans modalité. Conservé ; la formulation ne doit pas passer dans le texte III. |
| D1, D2, D3 | Dans le périmètre | — |
| **Argon seul** | **Deux passages hors périmètre ; réintégrée au niveau méthode (décision 0)** | (1) Bloc 4, point 1, ligne « Options », option (B), contenu de la parenthèse : [détail scellé, branche donnees/bras-attaque-texte-III-v1]. (2) Bloc 3, question 4, point 4 « Risque hors périmètre », proposition qui suit le tiret : [détail scellé, branche donnees/bras-attaque-texte-III-v1]. Le palier 2 du bloc 1(b) est conservé au même titre que celui de C1. |

**Bilan** : 2 pièces sur 13 contiennent des passages hors périmètre (C1, Argon seul), soit 4 passages ; les deux sont comptées puis réintégrées sur décision du directeur, et les passages sont scellés.

**Signalements des critères 4 et 5** (n'écartent pas) :
- Statuts changés ou mal employés :
  - A1 (a) : le fait 1 (VÉRIFIÉ) est dit « RAPPORTÉ par la décision N-056 » avant correction.
  - C1 : statuts empilés sur des hypothèses (« HYPOTHÈSE … (VÉRIFIÉ, RAPPORTÉ) ») ; Q₁ = 16 et Q₂ = 18 marqués VÉRIFIÉ alors qu'ils sont dérivés ; la décision N-056 reformulée « sans dépense adaptative » ; des confiances marquées « (illustratif) ».
  - C2 : des citations d'autres cellules marquées « OBSERVÉ-NON-AUDITÉ ».
  - C3, page (c) point 6 : « Kimi et Gemini, VÉRIFIÉ point 13 » présentés comme lignées tierces, alors que Gemini est la lignée de la première source.
  - D1 : « cinq familles scellées (RAPPORTÉ) » pour cinq **instances** (corrigé en D3).
  - Argon seul : des propositions propres marquées « RAPPORTÉ » dans l'ancrage ; au bloc 4 point 1, une corrélation « observée » marquée VÉRIFIÉ sans fait correspondant ; au bloc 2, des propriétés de bancs (format, licence, étiquetage) affirmées sans statut alors que le fait 11 les tient pour HYPOTHÈSE ; « 59, illustratif » pour un chiffre du fait 9 (VÉRIFIÉ).
- Calculs :
  - B3, convention grossière : le texte dit « Chapman = 36,7 » alors que le calcul affiché donne 37,16.
  - C3, page (c) point 1 : les valeurs ne sont pas appariées à leur convention.
  - **Argon seul, Q3** : la validation demande de certifier ε = 0,10 à 95 % sur 25 familles tenues à l'écart. Or même à zéro échec, 25 familles ne bornent ε qu'à environ 0,113 (dérivé de la formule du fait 9) ; il en faut 29.
  - Toutes les pièces disent leur convention (m = 18 ou m = 19).
- Estimateurs sans leurs hypothèses (non jugeables en l'état) : C3, duel 1, « Chapman-Min » ; B1, « approche bayésienne » ; Argon seul, moyennage bayésien de modèles avec a priori de Dirichlet-Laplace (bloc 4, point 5), dont l'a priori n'est pas justifié.
- Formules critiquées au tour 2 qui valent par analogie pour Argon seul (R-4) :
  - masse manquante de Good-Turing en version abondance, Q₁ / Σ nₖ (C2 contre A) ;
  - effet de plan appliqué à la borne à zéro échec (A2 et B2 contre C) ;
  - pondération de Horvitz-Thompson par probabilités de capture estimées (C2 et D2 contre A) ;
  - combinaison des lecteurs par imputation multiple (C2 contre A).
- Incohérence restée après le tour 3 : A3, « test de faisabilité arithmétique », multiplie la borne à zéro échec par l'effet de plan qu'A2 jugeait inadapté ; C3 et D3 comptent les grappes.

---

## 2. Bloc 1 — préalables

### 2(a) Définition opérationnelle de l'universalité

| Source | Définition recommandée (classe, quantificateur, statistique) |
|---|---|
| A3 | Principal : **pour toute** famille de la classe observée scellée, s(f) ≥ τ, au grain le plus fin (pire cas, vérifiable par rejeu). Complément séparé : **enveloppe** de la part d'échec sur la population capturable, la borne haute supposant que toute la masse manquante échoue. L'énoncé (ε, α) n'est préenregistré que s'il passe un test de faisabilité. |
| B3 | **Proportion** : avec confiance 1 − α, part de la population de familles en échec < ε ; écart vues/tenues à l'écart comme diagnostic. |
| C1 | Quatre options sans choix explicite ; l'option 4 pondère par la couverture estimée. Thèse : sans pénalité pour la masse manquante, « robuste à l'inconnu » confond absence de découverte et absence de vulnérabilité. |
| C3 | « (τ, ε, couverture minimale)-universelle » sur le support des familles découvrables : (1) borne inférieure de confiance de la couverture d'incidence au niveau 1 − α₁ ≥ minimum déclaré, **et** (2) borne supérieure de confiance de la proportion de **grappes** indépendantes en échec au niveau 1 − α₂ ≤ ε ; α = α₁ + α₂. L'énoncé est déclaré en échec sur le contrôle où une strate à capture nulle concentre les échecs. |
| D3 | Classe finie exhaustivement testée : chaque famille satisfait le critère. Familles découvertes : **proportion**, conditionnelle à la loi, au mécanisme, à l'unité d'échantillonnage et au critère déclarés ; **abstention** sinon. |
| Argon seul | Option retenue : proportion d'échec bornée par la proportion observée **plus** la masse manquante de Good-Turing, toute la masse manquante comptée en échec ; « universelle sur la classe déclarée » ignore cette masse, « robuste à l'inconnu » l'intègre. |

- **Verdict du critère 1 : divergente**, inchangé. Aucune paire de modèles distincts ne retient la même classe, le même quantificateur et la même statistique ; C1 et C3 sont le même modèle, et Argon seul est hors du « commun » (critère 6). **Tranché par le directeur : option (c), double condition** (section 7).
- **Convergences** (A3, B1, C1, C3, D1, D3, Argon seul : 5 modèles sur 5) : « robuste à l'inconnu » n'est définissable que relativement à un mécanisme de découverte déclaré ; la zone à capture nulle est hors de toute garantie.
- **Famille d'idées « pénaliser par la masse manquante »** : A3 (enveloppe en nombre de familles), C1 et C3 (couverture d'incidence), Argon seul (masse de Good-Turing additionnée). L'idée est commune, mais les statistiques diffèrent.
- **Critiques qui pèsent sur l'option (c)** :
  - D2 : la masse non couverte peut être toute en échec, donc l'énoncé doit dire par écrit qu'il est muet sur elle ; C3 l'a fait.
  - B2 : la couverture est mesurée sous la loi de découverte, pas sous la loi de difficulté.
  - A2 et B2 : une couverture estimée insérée sans son incertitude ; C3 corrige par une borne de confiance et un partage de α.
- **Ma recommandation (v1)** était l'option (a) ; elle est remplacée par la décision du directeur. La section 7 dit ce que la question doit alors exiger.

### 2(b) Régime d'information

- **Convergences** :
  - chaque palier rapporté séparément et scellé avant le suivant (A1, C1, C3, D1, Argon seul) ;
  - budgets fixés avant ouverture (A1, D1, Argon seul) ;
  - aucun retour vers les concepteurs, même agrégé, avant le rapport unique (A1, B1, C1, D1, Argon seul) ;
  - lots de calibration des seuils et de mesure des fausses alertes disjoints (A2, accepté par B3 et C3, repris par A3) ;
  - écart entre paliers interprétable seulement à familles, budget et statistique identiques, avec une double exécution à information identique comme loi nulle (A3, C3, D3) ;
  - trois paliers au moins, de l'aveugle à l'accès en lecture aux paramètres figés (A1 en six niveaux, C1, C3, Argon seul).
- **Divergences** :
  - contenu du palier le plus informé : poids et seuils compris pour A1, C1, C3 et Argon seul (4 modèles sur 5), contre « pas les poids » pour B1 ; D1 dit seulement « défense figée, protocole et seuils selon le palier » ;
  - nature des paliers : échelle (A1, C1, Argon seul) ou catégories (A3, après D2) ;
  - sélection conditionnée par la sortie de la défense au palier informé : critiquée par A2 et D2 (l'énoncé par proportion tombe) ; C3 la garde en séparant éléments de sélection et éléments de score ; Argon seul la propose sans cette séparation (la critique d'A2 vaut par analogie) ;
  - réutilisation des familles tenues à l'écart : interdite (A1, D1), ou permise sous budget d'accès à confidentialité différentielle (Argon seul).
- **Interdits de partage** :
  - des familles tenues à l'écart vers les concepteurs : accord des cinq sources ;
  - de la défense vers l'évaluation : C1 interdit en plus de partager certaines pièces d'entraînement et de consigne de la défense (justification : [détail scellé, branche donnees/bras-attaque-texte-III-v1]) ;
  - D1 interdit au banc informé les graines, contenus et clés d'appariement des familles scellées.
- **Budget** : B3, 400 éléments par famille pour ± 0,05 (illustratif) ; C1, 100 éléments et 20 pas séquentiels par élément (illustratifs) ; C3, 50 + 50 au palier informé (illustratif) ; Argon seul, budget en familles, éléments, longueur et passes du modèle.
- **Recommandation** (adaptée à la décision 4, qui met le régime dans le texte III) : catégories plutôt qu'échelle ; comparaison à unités et budget fixés ; éléments de sélection et de score disjoints ; double exécution comme loi nulle ; aucune description de l'usage que le banc fait de l'information (A1, piège de Q5). Confiance : élevée sur les interdits.

### 2(c) Nombre de familles, par simulation

- **Convergences** :
  - les seuils 29, 59 et 149 du fait 9, avec leur réserve, sont repris par les cinq sources ;
  - la garantie est conditionnelle au mécanisme de découverte (A1, B1, C1, D1, Argon seul) ;
  - modèle à deux niveaux et grappes de familles proches (A1, B1, C1, D1, Argon seul) ;
  - **découverte biaisée par la visibilité** nommée explicitement (A1 duel 3, B1, C1, Argon seul).
- **Pondération de Horvitz-Thompson** : proposée par A1, C1 et Argon seul ; retirée par A3 et transformée en post-stratification par C3, après C2 et D2 (le nombre de sources qui captent une famille est tronqué et n'identifie pas sa probabilité d'inclusion). La même critique vaut par analogie pour Argon seul.
- **Dépendance** : compter des **grappes** indépendantes, non diviser par l'effet de plan d'une moyenne (A2 sur C1, accepté par C3 ; vaut par analogie pour la formule d'Argon seul).
  - D3 : l'unité indépendante est définie par le plan, et les familles d'une même instance forment une grappe sauf validation préenregistrée.
  - Conséquence dérivée, centrale pour la décision 2 : avec g instances comptées comme unités, la borne à zéro échec à 95 % vaut environ 0,45 pour g = 5, 0,26 pour 10, 0,14 pour 20, 0,10 pour 29, et 0,05 pour 59.
- **Faisabilité** : avec environ 37 à 39 familles estimées, ε = 0,05 est hors d'atteinte en comptant des familles (A3) ; garantie stratifiée : 344 familles pour quatre strates (C2, dérivé juste) ; 29 familles en valent environ 50 sous forte corrélation (B2).
- **Arrêt séquentiel** : martingales de test (A1), mélange de Ville (B1), rapport de vraisemblance séquentiel ou dépense d'α (C1, D1), frontières d'O'Brien-Fleming (Argon seul). C2 : la surmartingale casse si l'ordre d'arrivée est autocorrélé ; A2 : la dépense d'α suppose une information maximale fixée. A3 garde la règle à titre d'HYPOTHÈSE sous contrôle d'arrivée groupée ; D3 exige la fausse certification à chaque temps d'arrêt.
- **Analyses de sensibilité** : C1 borne la confusion entre visibilité et vulnérabilité par un paramètre de type Rosenbaum (référence à vérifier). B2 objecte que deux niveaux de visibilité seulement donnent peu de puissance.
- **Ce que la simulation suppose** : Argon seul, l'absence d'un mode isolé à capture nulle et à performance nulle ; c'est exactement le contrôle exigé par C2 et D2.
- **Recommandation** : test de faisabilité avant tout préenregistrement, en comptant des grappes (D3) ; unité indépendante déclarée d'avance, qui sera l'instance selon la décision 2. Confiance : élevée sur l'arithmétique.

### 2(d) Familles encore inconnues

- **Vérification** : les quatre valeurs du contexte sont exactes (A1, B1, C1, D1, D3, Argon seul) : 38,89 et 36,84 (Lincoln-Petersen), 38,68 et 36,70 (Chapman).
- **Convergence** : les calculs bruts mélangent les unités ; aucun n'est défendable tel quel (A1, C1, C2, D1, D3, B3 après critique, Argon seul). Recodages cohérents et refaisables :
  - grain grossier n₁ = 28, n₂ = 24, m = 18 → Lincoln-Petersen 37,33, Chapman 37,16 ;
  - grain fin n₁ = 29, n₂ = 25, m = 19 → Lincoln-Petersen 38,16, Chapman 38,00 ;
  - comptage brut à battre : 34 ou 35.
- **Recommandations par source** :
  - grain grossier : A1 et A3 (pour l'estimation du nombre ; grain fin pour la mesure par famille), C1 (« seule cohérente » faute de redécoupage), Argon seul (composantes connexes, invariant à l'ordre des sources) ;
  - les deux en parallèle : B3 (après avoir défendu m = 19 avec n₁ = 28 en B1) ;
  - enveloppe des deux : C3 ;
  - deux scénarios qui ne forment pas un intervalle de confiance : D3.
  - Le grain grossier est le premier choix de 4 modèles sur 5 (A, B3, C1, Argon seul). Le constat d'A2, repris par C3 et D3, tient toujours : le sens 1 → 2 peut venir du lecteur, de la lignée de la seconde source.
- **Sens des biais** (accord des cinq sources) : dépendance positive et hétérogénéité font sous-estimer le nombre ; faux appariements le font sous-estimer, appariements manqués surestimer. Le signe inversé de B1 est corrigé en B3.
- **Estimateurs multi-sources** :
  - borne de Chao en version incidence (37,56 à deux sources ; A1, C1) ;
  - modèles log-linéaires **parcimonieux** à termes de lignée (C2, accepté par A3 et B3), parce que la table est creuse ; Argon seul propose un moyennage bayésien de modèles régularisé ;
  - classes latentes et bayésien en sensibilité seulement (C2 sur D, accepté par D3) ;
  - Good-Turing en version incidence (A3 après C2 ; la formule d'abondance de C1 et d'Argon seul tombe sous la même critique) ;
  - Chao2 perd sa propriété de borne inférieure sous faux négatifs d'appariement (C2).
  - C1 rattache par erreur les modèles log-linéaires de population fermée à un modèle de population ouverte (A2) ; corrigé en C3.
- **Indépendance** : non testable à deux sources (A1, D1). Argon seul propose, à partir de trois sources, des tests conditionnels sur des sous-tables restreintes aux familles vues par une troisième source. Contrôles exigés : deux listes d'un même modèle, et captures de Bernoulli indépendantes (A2, D2 ; repris par B3, C3, D3).
- **Refus commun** : accord des cinq sources : strate invisible, estimation restreinte à la population capturable, journaux de refus pour mesurer la censure. Deux nuances :
  - C1 : la taille de la strate n'est bornable que par les journaux ou par construction hors modèle ;
  - Argon seul : se servir de sources hors modèles commerciaux comme sources non censurées. Il ne dit pas comment leur indépendance serait établie.
- **Population non fermée** : estimation à une date donnée, courbe d'accumulation et masse manquante (A1, D1, Argon seul) ; processus de Pitman-Yor pour le taux d'innovation (C1, Argon seul) ; test de fermeture comme diagnostic (A3, D3).
- **Recommandation** : inchangée depuis la v1. Deux recodages en scénarios, borne de Chao2 et modèle log-linéaire parcimonieux après étalonnage du lecteur, énoncé restreint à la population capturable. Confiance : élevée.

---

## 3. Bloc 2 — données de départ recommandées

| Donnée | A | B | C1 | C3 | D | Argon seul | Accord |
|---|---|---|---|---|---|---|---|
| (i) Bancs publics | 3 nommés, familles extérieures après mesure du recouvrement par date ; indépendance faible | **1** après vérification | 3 (ControlArena, SHADE-Arena, Liars' Bench), familles extérieures **et** source de capture supplémentaire ; « indépendance de conception » ; mise au format 2 à 3 jours-personne (illustratif) | 3, **30 trajectoires** (illustratif) | **≤ 3** après audit | 3, « source zéro » extérieure fixe ; contamination élevée → test de mémorisation ; mise au format moyenne à élevée (rejouer sur 8 et 70 milliards pour extraire les activations) | 6 sur 6 : propriétés non vérifiées, audit avant usage |
| (ii) Journaux de refus | Censure | B1 capture → **B3 censure** | Taux de censure par fournisseur | Censure ; taux de base sur questions neutres | Censure | Censure ; non étiquetés | 6 sur 6 au dernier état : censure seulement |
| (iii) Propositions brutes d'une course précédente | Source dépendante déclarée | Source, indépendance douteuse | **Priorité 1**, source de capture à coût quasi nul | — | Source qui ne corrige pas une dépendance commune | Source « à mécanisme distinct » si produite par des équipes humaines (HYPOTHÈSE) | Divergence : dépendante (A, B, D) contre indépendance possible (C1, Argon seul) |

- Ordre de priorité : C1 classe (iii), (ii), (i) ; A1 recommande (iii) puis (i) ; B1 recommande (ii), (iii), (i) ; D et Argon seul ne classent pas.
- Données brutes plutôt que résumés : accord (A1, C1, D1, Argon seul), parce que les résumés faussent le compte des familles vues une seule fois et empêchent un ré-appariement par un tiers.
- MonitoringBench et SLEIGHT-Bench : aucune source ne les décrit ; A1, B1, C1, D1 et Argon seul s'abstiennent explicitement.
- **Divergence principale** : l'indépendance des bancs publics, forte « de conception » pour C1 et Argon seul, faible pour A1 et D1 (le programme les a lus ; le caractère public ne prouve rien).
- Recommandation inchangée : (ii) pour mesurer la censure, (iii) comme source dépendante déclarée, (i) seulement après l'audit de D3, et jamais dans la liste scellée de G1 sans décision à part (décision N-061). Confiance : moyenne.

---

## 4. Bloc 3 — questions candidates (dédoublonnées)

Versions finales du tour 3 pour A, B, C, D ; tour 1 pour C1 et Argon seul (sans tour suivant). Critère 3 : une **simulation à vérité connue seule n'est pas une validation extérieure** (D2) ; une question fusionnée est retenue si au moins une source donne une validation extérieure chiffrée et un piège nommé.

### Q-I. Estimer le nombre de familles capturables et la masse manquante à partir de plusieurs sources dépendantes, sous appariement non bijectif
- Fusion de : A3-Q1, B3-Q1, C1-Q1, C3-Q1, D3-Q2, Argon seul Q1.
- Avantage : exploite les sources multiples, qui rendent les interactions estimables ; part d'une anomalie VÉRIFIÉE (m = 18 contre 19) ; donne directement la condition de couverture de la décision 1 (C3).
- Piège : table creuse et estimateurs inexistants (C1, C2, Argon seul) ; appariement unique qui injecte la dépendance (A1) ; strate à capture nulle prise pour absente (D3) ; source finale non échangeable (D2).
- Validation extérieure chiffrée :
  - prédiction scellée du gain de la dernière source, intervalle à 90 % (illustratif, A1, A3) ;
  - **15 familles extérieures** dans l'intervalle de couverture, à ± 10 % (illustratif, C1 ; repris en C3 avec une couverture ≥ 90 % sur 2 000 mondes) ;
  - au moins **30 familles extérieures** de 2 bancs, recouvrement prédit à ± 15 % (illustratif, Argon seul).
- Risque hors périmètre : faible (A1, B1, C1, C3, D3, Argon seul ; illustratif).
- Sort : **retenue**.

### Q-II. Mesurer l'erreur d'appariement des lecteurs et la propager dans l'estimation
- Fusion de : B3-Q4, C3-Q3, D3-Q3, Argon seul Q2 ; A3 l'intègre au plan.
- Avantage : le fait 6 montre un lecteur unique de la lignée d'une source ; c'est le préalable de tout estimateur, et l'origine du 1 → 2 devient testable (A2, C3).
- Piège : accord pris pour justesse (D2) ; kappa inadapté à un graphe non bijectif (A2 ; vaut par analogie pour Argon seul Q2) ; lecteurs de même lignée (B1) ; imputation multiple sur des lecteurs déterministes (C2 ; vaut pour Argon seul Q2) ; seuil arbitraire de fusion ou de scission (Argon seul) ; énumération combinatoire (C2 sur D).
- Validation extérieure chiffrée :
  - accord au niveau des liens ≥ 0,80 avec trois lecteurs (illustratif, B3) ;
  - 10 paires permutées et 10 scissions connues, erreur < 5 % (illustratifs, C3) ;
  - 40 schémas abstraits dont 10 doublons et 10 disjoints, κ ≥ 0,75 (illustratifs, Argon seul) ;
  - double lecture extérieure de 100 % des liens (D3).
- Risque : faible (B3, C3, D3, Argon seul ; illustratif).
- Sort : **retenue**.

### Q-III. Borner la part d'échec quand les familles sont découvertes et non tirées
- Fusion de : A3-Q2, B3-Q3, C1-Q2, C3-Q2, Argon seul Q3.
- Avantage : attaque la réserve du fait 9 ; c'est le cœur de l'énoncé d'universalité (condition (2) de la décision 1).
- Piège : poids de Horvitz-Thompson tronqués (C2, D2 ; Argon seul Q3 nomme lui-même leur variance extrême) ; lien découverte-difficulté non identifiable (C1, B2) ; strate à capture nulle.
- Validation extérieure chiffrée :
  - borne haute ≥ 0,08 à zéro échec (A3, dérivé) ;
  - ≥ 20 familles extérieures → ε ≈ 0,14 (A1, dérivé) ;
  - 15 familles tenues à l'écart → ε ≈ 0,18 à zéro échec (C3 ; dérivé ici) ;
  - 20 familles rares ou tenues à l'écart, écart de rappel ≤ 15 % (illustratif, C1) ;
  - 25 familles tenues à l'écart, 100 éléments, τ = 0,85, ε = 0,10 (illustratifs, Argon seul ; **inatteignable tel quel**, voir section 1).
- Risque : faible (A1, B1, C1, C3, Argon seul ; illustratif).
- Divergence interne : corriger (C3), encadrer (A3), s'abstenir (D3). C3 la transforme en duel.
- Sort : **retenue**.

### Q-IV. Valider la borne d'universalité sous variance à deux niveaux, dépendance et arrêt séquentiel ; dimensionner le plan
- Fusion de : A3-Q4, B3-Q5, D3-Q1, C1-Q3 (partie sur la puissance séquentielle à deux niveaux) ; s'y rattachent le test de faisabilité d'A3, le contrôle de C2 et le calcul de C1 et d'Argon seul au bloc 1(c).
- Avantage : dit d'avance quels énoncés sont atteignables ; économise le calcul sur 70 milliards (A1, C1).
- Piège : compter sorties ou éléments comme unités indépendantes (D3) ; martingale cassée par l'autocorrélation (C2) ; regards multiples (C1) ; modèle bêta-binomial mal spécifié (C2).
- Validation extérieure chiffrée :
  - revue par un statisticien extérieur, couverture ≥ 0,93 pour 0,95 nominal (illustratif, A1) ;
  - jeu public à dépendance connue (A3) ;
  - 29 ou 59 unités (fait 9, D3) ;
  - **10 familles extérieures** à 200 éléments, arrêt séquentiel vers 40 éléments, même décision que l'échantillon complet dans ≥ 95 % des cas (illustratifs, C1).
- Risque : faible (A1, B1, D3) ; moyen pour la partie sur les paliers de C1 (illustratif).
- Sort : **retenue**.

### Q-V. Mesurer la transportabilité d'une prédiction scellée des familles vues vers les familles tenues à l'écart
- Fusion de : A3-Q3, B3-Q2.
- Avantage : directement réfutable.
- Piège : écart confondu avec la différence de difficulté (C2, D2) ; loi nulle contaminée par la calibration (B2) ; prédiction dégénérée (B2).
- Validation : ≥ 15 familles extérieures (illustratif, B1, B3) ; marge 0,02 de score de Brier (illustratif, A3).
- Risque : faible (illustratif).
- Sort : **retenue**, cause d'un écart non attribuable sans covariable de difficulté (HYPOTHÈSE).

### Q-VI. Tester le transport vers des données extérieures (bancs publics) et leur contamination
- Fusion de : C3-Q5, D3-Q4. Parente de Q-V et de Q-VIII.
- Avantage : seules données conçues hors du programme.
- Piège : recouvrement avec l'entraînement non identifiable par un test interne (D3) ; loi de découverte différente (A2, D2) ; étiquetage construit après observation (D1).
- Validation : 30 trajectoires brutes avant déscellement (illustratif, C3) ; D3 sans seuil chiffré.
- Risque : moyen (D1, D3), faible (C3) ; illustratifs.
- Sort : **retenue** par C3 seule ; dépend du fait 11 (HYPOTHÈSE).

### Q-VII. Mesurer l'écart entre évaluation aveugle et évaluation informée
- Fusion de : A3-Q5, C1-Q3 (partie sur les paliers), C3-Q4, D3-Q5.
- Avantage : la décision N-056 impose déjà les deux versions.
- Piège : budgets ou familles différents (D1) ; sélection sur la sortie de la défense (A2, D2) ; paliers lus comme une échelle (D2) ; dérive vers une conception adaptative (C1).
- Validation chiffrée : 50/50 sélection et score sur 20 familles (illustratif, C3) ; 10 familles extérieures à 200 éléments (illustratif, C1) ; intervalle à 95 %, taille fixée par la puissance (D3).
- Risque : **moyen** (A1, C1, C3), faible (D3). L'élément qui la borne : le passage d'un régime à l'autre ne change que les poids d'échantillonnage ou un filtrage statique sur une grille fixe (C1), à unités et budget identiques (A3, D3).
- Sort : **retenue** ; **dans le texte III par la décision 4**.

### Q-VIII. Mesurer la fidélité statistique du banc simulé (nouvelle, Argon seul Q4)
- Énoncé au niveau méthode : quels critères de divergence distributionnelle, dans l'espace des activations des modèles de 8 et 70 milliards et dans celui des sorties textuelles, permettent de valider qu'un banc simulé couvre le domaine de sensibilité des sondes et des moniteurs.
- Avantage : c'est la seule question qui porte sur la moitié « banc » de l'objet du texte III ; elle respecte la règle « aucun agent opérationnel » tout en mesurant le risque d'un banc trop simple (Argon seul).
- Piège :
  - en grande dimension, les distances (écart moyen maximal, Wasserstein) souffrent de la malédiction de la dimension et peuvent valider des lois dégénérées (Argon seul) ;
  - les trajectoires publiques suivent leur propre loi, donc un écart ne distingue pas « banc pauvre » de « loi extérieure différente » (critique d'A2 et D2 contre B et C, par analogie) ;
  - contamination d'entraînement (C1, Argon seul bloc 2) ;
  - coût de rejouer les trajectoires sur 8 et 70 milliards (Argon seul bloc 2).
- Validation extérieure chiffrée : **500 éléments simulés contre 500 trajectoires de bancs publics** ; un discriminateur d'origine dans l'espace de représentation de la sonde, aire sous la courbe bornée ou déficit de couverture ≤ 0,10 (illustratifs, Argon seul). Réserve : la quantité bornée par 0,10 est ambiguë dans la pièce (aire sous la courbe ou déficit).
- Risque hors périmètre : moyen (Argon seul ; illustratif). Raison donnée : [détail scellé, branche donnees/bras-attaque-texte-III-v1]. L'élément qui la borne : ne traiter que des métriques de divergence sur des vecteurs d'activation et des scores déjà extraits.
- Sources : Argon seul (une seule) ; parentes : Q-VI (C3, D3) et l'usage des bancs publics comme familles extérieures (A1, C1).
- Sort : **retenue** (piège nommé, validation chiffrée). Elle dépend du fait 11 et d'une dépense de rejeu (devis).

### Q-IX. Calibrer l'agrégation séquentielle et transférer ses seuils de 8 vers 70 milliards (nouvelle, Argon seul Q5)
- Énoncé au niveau méthode : comment calibrer une règle d'arrêt et d'agrégation séquentielle combinant sondes internes et moniteurs à texte seul, et estimer la loi de transfert de ses seuils du modèle de 8 milliards vers celui de 70 milliards sans consommer les familles tenues à l'écart.
- Avantage : réduit le calcul sur 70 milliards en se servant du modèle de 8 milliards comme variable de contrôle (estimateur de multi-fidélité) (Argon seul).
- Piège : inflation du taux d'erreur de la famille de tests à chaque pas de la séquence ; rupture de la corrélation entre 8 et 70 milliards sur certaines familles (Argon seul) ; arrêt optionnel sous dépendance (C2, par analogie).
- Validation extérieure chiffrée : loi d'échelle préenregistrée sur les familles vues, puis vérification scellée sur **20 familles tenues à l'écart** exécutées sur 70 milliards ; erreur de prédiction du seuil qui garantit un taux de fausses alertes ≤ 0,01 inférieure à 0,005 (illustratifs, Argon seul).
- Risque hors périmètre : faible (Argon seul ; illustratif). **Risque d'être hors sujet : élevé (mon jugement)** : la question porte sur la calibration de la défense entre tailles de modèle, non sur l'universalité entre familles. Elle consomme 20 familles tenues à l'écart, à décompter de la lecture unique (décision N-050).
- Sources : Argon seul (une seule).
- Sort : **retenue** au sens du critère 3 ; je recommande de la sortir du texte III (section 7, décision 6).

### Non retenue

**C1-Q4. Borner le risque résiduel dû aux familles censurées par les refus communs des sources.**
- Avantage : mesure un biais que la capture-recapture ignore (C1).
- Piège nommé par C1 : non-identifiabilité dans la zone de refus.
- Validation proposée : 30 entrées de journaux converties en schémas abstraits, écart ≤ 0,10 (illustratifs, C1).
- Risque : élevé (C1).
- Sort : **non retenue**. La validation n'est pas extérieure : les schémas seraient conçus par le programme, ni indépendants ni tenus à l'écart (A2, B2, D2). Son auteur l'abandonne en C3 (ligne C-11). L'objet reste couvert, en négatif, par la clause « strate à capture nulle hors garantie » de Q-III.

### Classement des questions retenues

Poids : cœur de l'énoncé d'universalité, nombre de sources, validation extérieure, risque, et désormais les décisions du directeur.

1. **Q-III**, borne de la part d'échec (A, B, C, Argon seul) : condition (2) de la décision 1.
2. **Q-I**, couverture et nombre capturable (A, B, C, D, Argon seul) : condition (1) de la décision 1.
3. **Q-IV**, faisabilité et dimensionnement (A, B, C1, D) : fixe le nombre d'instances de la décision 2.
4. **Q-VII**, aveugle contre informé (A, C, D) : imposée par la décision 4 ; risque moyen à borner.
5. **Q-II**, erreur d'appariement (B, C, D, Argon seul, A dans le plan) : première expérience, exigence intégrée à Q-I.
6. **Q-VIII**, fidélité du banc simulé (Argon seul) : seule question sur le banc ; une source ; dépend du fait 11.
7. **Q-V**, transportabilité d'une prédiction scellée (A, B) : élément de validation.
8. **Q-VI**, transport vers les bancs publics (C, D) : dépend du fait 11.
9. **Q-IX**, transfert de 8 vers 70 milliards (Argon seul) : hors du sujet de l'universalité.

---

## 5. Bloc 4 — organisation des instances

| Point | Accord | Désaccord |
|---|---|---|
| Consigne | Noyau identique, scellé (A3, B3, C3, D3) | Variations de format seulement (A3) ; aucune (B3, C3) ; variations préenregistrées permises (D3) ; **deux passes ou quota hybride** avec une part de consigne variée selon des axes déclarés (C1, Argon seul ; axes : [détail scellé, branche donnees/bras-attaque-texte-III-v1]). Critique d'A2, B2 et D2 contre les deux passes de C1 : contamination de la seconde par la première, corrélation de capture par conception ; abandon par C3. La critique vaut par analogie pour le quota hybride d'Argon seul. |
| Fuites | Contextes isolés ; sorties hachées et scellées avant toute lecture croisée ; journal horodaté (les cinq) | Niveau d'isolement : opérateurs distincts (A1), tiers sans réseau (B3), séquestre chiffré (C1, C3), comptes et stockages séparés (D3), comptes séparés sans rétention chez les fournisseurs et déchiffrement après l'empreinte de la défense (Argon seul) |
| Appariement | Au moins trois lecteurs aveugles à la source, de lignées distinctes des sources ; étalon à vérité connue ; liens multiples permis (A3, B3, C1, C3, D3, Argon seul) | Méthode : panel seul (A, B, D) ; treillis de subsomption (C1, C3) ; plongements et regroupement hiérarchique, puis graphe d'adjacence probabiliste (Argon seul ; B1 l'avait cité comme option). Propagation : matrice de confusion dans la vraisemblance (A3, C3), taux de faux liens (B3), scénarios séparés (D3), Monte-Carlo sur le graphe (Argon seul) ; imputation multiple abandonnée (C2, A3) |
| Indépendance | Les sorties ne prouvent pas l'indépendance des corpus (D1, D3 ; HYPOTHÈSE chez A3, B1) ; termes de lignée dans un modèle parcimonieux ; contrôle positif par deux exécutions d'un même modèle | Étalonnage sur une énumération neutre utilisé comme a priori (A3, C1, Argon seul, qui ajoute une divergence de Jensen-Shannon entre distributions de jetons) contre simple hypothèse de modèle (D2, D3) |
| Sources multiples | Comptage brut, Chao2, log-linéaire parcimonieux, sensibilités ; Chapman par paire en comparaison | Retrait d'une source à la fois : sur modèle parcimonieux seulement (C2, D3 ; C1 le proposait sans restriction) ; moyennage bayésien de modèles (Argon seul) |
| Refus | Enregistré tel quel, jamais reformulé (fait 14) ; censure, jamais capture vide (les cinq) | **Remplacement compté** : A3 (substitut d'une autre lignée), B3 (deux réserves), C1 (sept instances pour absorber deux refus), Argon seul (réserve d'un sixième fournisseur, plus une classe latente « censurable ») ; **contre** : C3, D3 (sélection sur la permissivité, A2). **Tranché par le directeur : remplacement compté** (décision 3) |

- C3, accepté sur le fond : les instances doivent être de lignées disjointes de celles des deux sources de départ, ou ces sources confinées aux familles vues. Avec R-2, cela vaut aussi pour les lecteurs.

---

## 6. Critiques croisées (tour 2) et réponses (tour 3)

**Acceptées (principales)**
- A :
  - sa « couverture » mesurait la puissance (C2) → fausse certification bornée par α ;
  - Horvitz-Thompson retiré (C2, D2) ;
  - Good-Turing d'abondance retiré (C2) ;
  - imputation multiple abandonnée (C2) ;
  - loi nulle par scission remplacée par deux lots de même loi (B2) ;
  - score strictement propre (B2) ;
  - test de fermeture et étalon ajoutés (B2).
- B :
  - signe du biais de Lincoln-Petersen (A2, C2, D2) ;
  - duel 2 circulaire ;
  - test d'indépendance à deux sources et contrôle par partition erronés ;
  - unités mélangées avec m = 19 ;
  - budget par famille faux d'un facteur 4 (A2) ;
  - kappa inadapté (A2) ;
  - journaux de refus pris pour une source de capture (C2, D2).
- C (critiques visant C1) :
  - duels non exclusifs (A2, D2) ;
  - sous-dimensionnement (A2, B2) ;
  - attribution erronée d'un modèle de population ouverte (A2) ;
  - effet de plan sur une borne à zéro échec (A2, B2) ;
  - couverture sans incertitude (A2, B2, D2) ;
  - deux passes et passage de 7 à 5 instances abandonnés (A2, B2, D2) ;
  - conversion humaine des refus abandonnée (A2, B2, D2) ;
  - palier informé transformé en sélection et score disjoints (A2, D2).
- D :
  - « cinq familles » corrigé en cinq instances (A2) ;
  - duels vrais par construction (A2, B2, C2) ;
  - binomiale exacte sous dépendance → unité fixée par le plan ;
  - garantie stratifiée retirée (C2).

**Rejetées ou acceptées en partie**
- A3 rejette la prémisse de B2 (moins de 10 familles tenues à l'écart), qui est une HYPOTHÈSE de B ; elle rejette pour moitié B2 sur la fusion d'unités.
- C3 rejette A2 sur l'ancrage, tout en acceptant le fond (lignées disjointes).
- D3 rejette en partie B2 sur le bloc 2 ; le test de fermeture est « transformé en diagnostic ».

**Argon seul** : aucune critique ne le visait (R-4). Critiques qui valent par analogie : Horvitz-Thompson (C2, D2) ; Good-Turing d'abondance (C2) ; effet de plan (A2, B2) ; imputation multiple et kappa (C2, A2) ; quota hybride de consignes (A2, B2, D2 contre C1) ; a priori tiré d'une tâche neutre (D2) ; remplacement d'instance (A2 ; tranché depuis par le directeur).

**Dissensus irréductibles transformés en expériences**
1. Chao2 contre Chapman à petit effectif (duel 1 de A3, B3, C3, D3).
2. Corriger, encadrer ou s'abstenir face au biais de découverte (C3 duel 2, A3 duel 3, D3), avec le monde bimodal de C2.
3. Proportion contre pire cas (B3 duel 2, D3 duel 2).
4. Origine du 1 → 2 (A2 → étalonnage du lecteur en C3 et D3).
5. Indépendance des sources : modèle d'hétérogénéité seul contre modèle à termes de lignée (B3 duel 3).
6. Fermeture (A3, D3).
7. Effet du régime d'information : double exécution (A3, C3, D3).

**Première expérience** (convergence des quatre réponses) : sur processeur seulement, l'étalonnage du lecteur, puis un monde simulé à vérité connue (environ 38 familles, sources multiples, appariement non bijectif, captures dépendantes par lignée).

---

## 7. Recommandation pour le texte III (révisée après les décisions du directeur)

**Verdict.** Le texte III porte deux questions :
- une **question principale** : une borne d'universalité en double condition (couverture minimale et proportion d'unités en échec), sur des unités qui sont des **instances indépendantes**, mesurée séparément en régime aveugle et en régime informé ;
- une **question seconde** : la couverture et le nombre de familles capturables, estimés à partir de ces instances, substituts compris, sous un appariement faillible.

Q-II et Q-V y entrent comme exigences. Restent à trancher : Q-VIII (fidélité du banc simulé, décision 5), Q-IX (décision 6, à sortir selon moi) et la cible ε (décision 7). C1-Q4 n'est pas retenue.

**Décisions du directeur intégrées (30 octobre 2026)**
- D0, lecture indulgente : C1 et Argon seul réintégrés, passages scellés.
- D1, option (c) : double condition, couverture minimale et proportion.
- D2, option (c) : plus d'instances, sur devis.
- D3, option (a) : substitut prédéclaré compté comme source.
- D4, option (a) : le régime aveugle contre informé entre dans le texte III.

**Question principale (réécrite, niveau méthode).** « Une défense est évaluée sur des familles conçues par des instances indépendantes déclarées d'avance, chacune tenue à l'écart de la conception de la défense ; ces familles sont découvertes, non tirées au hasard. Propose la méthode qui permet d'affirmer devant un tiers, au niveau de confiance 1 − α avec α = α₁ + α₂, et seulement sur le support des familles découvrables (probabilité de capture non nulle), l'énoncé double suivant : (1) la borne inférieure de confiance, au niveau 1 − α₁, de la couverture d'incidence atteint un minimum déclaré ; (2) la borne supérieure de confiance, au niveau 1 − α₂, de la proportion d'unités indépendantes en échec ne dépasse pas ε. Ta méthode doit préciser : (a) la définition d'une instance indépendante, et la règle préenregistrée qui fusionne en une seule unité des instances trouvées dépendantes ; (b) le critère d'échec d'une unité, déclaré avant toute mesure ; (c) le nombre d'unités nécessaire pour ε et α donnés, le test de faisabilité qui retire un énoncé inatteignable, et la règle d'abstention ; (d) ce que l'énoncé n'autorise pas, écrit comme tel : la masse non couverte et la strate à capture nulle ; (e) le traitement d'une instance qui refuse et de son substitut prédéclaré, compté comme source, avec la mesure du biais de sélection que ce remplacement peut introduire ; (f) la mesure de l'énoncé séparément en régime aveugle et en régime informé de la défense, à unités, budget et statistique identiques, avec des éléments de sélection et de score disjoints et une double exécution à information identique comme loi nulle, sans décrire l'usage que le banc fait de l'information ; (g) la validation : prédictions scellées confrontées aux familles tenues à l'écart, et contrôles sur mondes simulés à vérité connue (monde sans masse manquante, monde où la masse à faible capture concentre les échecs, défense constante). »
- Sources : C3 pour la définition ; A3, B3, D3 pour la faisabilité, l'abstention et les contrôles ; A3, C3, D3 pour (f).
- Chiffres d'appui :
  - seuils 29, 59 et 149 (fait 9) ;
  - en unités = instances, borne à zéro échec à 95 % de 0,45 (g = 5), 0,26 (10), 0,14 (20), 0,10 (29), 0,05 (59) (dérivé) ;
  - validation de C3 : 15 familles tenues à l'écart, 50/50 sélection et score sur 20 familles (illustratifs).

**Question seconde (réécrite).** « Propose la méthode pour estimer, avec ses hypothèses explicites, la couverture d'incidence et sa borne inférieure de confiance (condition (1) de la question principale), ainsi que le nombre de familles capturables, à partir des sorties de g instances indépendantes déclarées, substituts prédéclarés compris et comptés comme sources, dont l'appariement est non bijectif et fait par des lecteurs faillibles. Précise : (a) l'unité de compte des familles et le traitement des fusions et des scissions ; (b) la mesure des faux liens, des liens manqués et des erreurs de grain sur un étalon à vérité connue, avec des lecteurs de lignées distinctes de toutes les instances et des deux sources de départ, et sa propagation dans l'estimation ; (c) des modèles parcimonieux, des bornes inférieures et des termes de dépendance par lignée, avec un contrôle positif par deux exécutions d'un même modèle ; (d) le traitement d'un refus comme censure de la source refusante, et l'effet de son substitut sur l'estimation ; (e) un test de fermeture ; (f) une prédiction scellée de l'apport de la dernière source ouverte, dans un ordre tiré au sort. »
- Sources : A3, B3, C3, D3, Argon seul.
- Chiffres d'appui :
  - recodages de Chapman 37,16 et 38,00 (dérivés) ;
  - étalon de 10 + 10 paires, erreur < 5 % (illustratif, C3) ;
  - accord au niveau des liens ≥ 0,80 (illustratif, B3) ;
  - 15 familles extérieures (illustratif, C1, C3) ou ≥ 30 (illustratif, Argon seul).

**Définition d'une instance indépendante, que la question doit exiger (décision 2)**
Une instance compte comme unité indépendante si, déclaré avant toute exécution :
1. elle est un modèle d'un fournisseur et d'une lignée distincts de toute autre instance, des deux sources de départ, des lecteurs d'appariement et des concepteurs de la défense, avec une provenance documentée (même base, dérivé ou distillation = même lignée ; l'exhaustivité de cette documentation est HYPOTHÈSE) ;
2. elle s'exécute dans un contexte, sous des comptes, avec un stockage et un coordinateur propres, sans exposition à une autre sortie avant scellement ;
3. elle reçoit le noyau de consigne commun scellé ;
4. sa sortie est scellée par empreinte avant toute lecture ;
5. son indépendance n'est pas présumée : contrôle positif par deux exécutions d'un même modèle, termes de lignée dans le modèle log-linéaire, et règle préenregistrée qui fusionne en une grappe deux instances trouvées dépendantes ;
6. ses familles forment une seule grappe (D3), et un critère d'échec de la grappe est déclaré d'avance.

Un substitut (décision 3) doit remplir les mêmes conditions.

**Devis à écrire** (nœud de dépense, GO requis, aucune dépense avant) : nombre g d'instances visé et ε qu'il permet (table ci-dessus), coût par instance, lignées disponibles. Le nombre de lignées réellement disjointes est une HYPOTHÈSE et peut rester sous 29.

**Réserves sur les décisions prises** (conséquences à surveiller ; je ne rouvre pas les choix)
- D1 (c) : l'énoncé est muet sur la masse non couverte (D2), ce que (d) rend explicite. La couverture est mesurée sous la loi de découverte, pas sous la loi de difficulté (B2).
- D3 (a) : le remplacement peut sélectionner les sources sur leur permissivité (A2). Garde-fous compatibles avec le choix :
  - liste ordonnée des substituts, scellée avant le premier appel ;
  - taux de refus de base sur des questions neutres (C2, C3) ;
  - analyse de sensibilité sans substitut, rapportée en plus, sans changer le compte.
- D4 (a) : risque de périmètre moyen (A1, C1, C3). Les bornes de (f) sont obligatoires, et aucune formulation de C1, C3 ou Argon seul sur la sélection au palier informé n'est reprise.

**À trancher par le directeur**

*Décision 5 — fidélité du banc simulé (Q-VIII) dans le texte III.*
- Enjeu : c'est la seule question sur la moitié « banc » de l'objet du texte III.
- Option (a), question tierce : couvre le banc, mais une seule source, dépend du fait 11 et d'une dépense de rejeu.
- Option (b), exigence de validation dans la question principale : texte plus court, mais traitement plus superficiel.
- Option (c), hors du texte III : texte plus sûr, mais le banc n'est pas validé par la course.
- Recommandation : (a), sous condition de l'audit des bancs (liste de D3), avec la borne « métriques de divergence sur des représentations déjà extraites ». Confiance : moyenne.
- Défaut sous 48 heures : (a).

*Décision 6 — transfert de 8 vers 70 milliards (Q-IX).*
- Option (a), dans le texte III : économie de calcul, mais hors du sujet de l'universalité, et elle consomme 20 familles tenues à l'écart (décision N-050).
- Option (b), vers un autre texte ou un préenregistrement de calibration de la défense : sujet propre, mais délai.
- Recommandation : (b). Confiance : moyenne.
- Défaut sous 48 heures : (b).

*Décision 7 — cible ε avec le devis.*
- Enjeu : en unités = instances, ε = 0,10 demande 29 instances indépendantes réussies, et ε = 0,05 en demande 59 (dérivé).
- Option (a), garder 0,05 : ambitieux, probablement inatteignable faute de lignées (HYPOTHÈSE).
- Option (b), ε fixé par le g du devis, et 0,05 non préenregistré tant que g < 59 : énoncé atteignable, mais garantie plus faible.
- Recommandation : (b). Confiance : moyenne.
- Défaut sous 48 heures : (b).

*Condition de méthode, non ouverte* : lecteurs et instances hors des lignées Argon et Opus (R-2). Le choix des fournisseurs se fait avec le devis.

**Reste HYPOTHÈSE** :
- la fermeture de la population ;
- l'indépendance réelle des instances au-delà de leur déclaration ;
- le nombre de lignées disjointes disponibles ;
- une covariable de difficulté indépendante de la défense ;
- les propriétés des bancs publics ;
- le transport d'une dépendance mesurée sur une tâche neutre.
