# Proposition E — Réponse aux critiques et conception corrigée

**Statuts.** Les dispositions des brouillons restent **RAPPORTÉES**, non auditées ici. Les critiques conservent leur statut d’**HYPOTHÈSES** méthodologiques ; les accepter ne les transforme pas en résultats. Mes décisions, corrections et protocoles ci-dessous sont des **HYPOTHÈSES** de conception. Les valeurs nouvelles proposées sont marquées **illustratives** : elles devront être adoptées ou remplacées avant scellement.

**Pièce C absente — RAPPORTÉ :** critique jamais lancée ; aucun contenu ne lui est attribué.

## A. Réponses aux critiques visant E

### Critiques de A

| Critique | Décision et conséquence |
|---|---|
| **A-a1 — Biais positif de \(E|\Delta|\) sous bruit numérique** | **Acceptée sur le bruit ; rejetée sur l’obligation de déduire toute marge pratique du bruit.** La pertinence scientifique et la résolution numérique sont distinctes. Je conserve une marge d’effet fixée à l’avance, mais rends le duel non interprétable si la répétabilité ne permet pas de la résoudre. Le bruit ne devient pas une « dépendance au contexte ». |
| **A-a2 — Cellules hors support ; recalcul obligatoire de \(\Sigma\) par cellule** | **Acceptée sur le hors-support ; rejetée sur le remède obligatoire.** Recalculer les directions à partir de chaque cellule d’évaluation change le comparateur et ne restaure pas un support naturel. Je conserve les directions issues de l’apprentissage, les applique aux mêmes cellules que la sonde et rapporte leurs déplacements appariés. Cela ne rend pas les cellules naturelles ni leurs étalonnages interchangeables. |
| **A-a3 — Privé honnête non construit** | **Acceptée.** Sa construction, son auteur, son appariement et son statut de relecture sont précisés ci-dessous. Sans contrôle valide, aucune attribution spécifique à la collusion plutôt qu’à la confidentialité. |
| **A-a4 — Calibration et évaluation de \(G\)** | **Acceptée comme besoin de spécification.** Ma proposition mentionnait une calibration indépendante, mais ne donnait pas la partition. Je retire le gain de détection à faible taux de fausses alertes comme duel principal ; il reste descriptif lorsque les effectifs le permettent. |
| **A-a5 — Empreintes révélatrices et inventaire des interfaces** | **Acceptée et transformée en test.** Un hash de contenu prévisible n’est pas un mécanisme de confidentialité. Les empreintes des résultats en clair ne sont plus exposées au coordinateur avant levée dans la variante renforcée. |
| **A-a6 — Canal concret `sondes_lues`** | **Acceptée.** Je rattache explicitement le risque aux clés `SCELLEMENT-JEUX-T07-JD/-JC/-JA`. Leur ensemble présent fixe le périmètre de notation, selon la pièce 2, **RAPPORTÉ**. Il faut tracer leur fixation, pas seulement invoquer abstraitement le « choix des sondes ». |
| **A-b — Queues lourdes et normalisation saturante** | **Acceptée pour la fragilité des intervalles ; rejetée comme conséquence nécessaire de ma normalisation.** Une transformation affine ne plafonne pas les scores. Je l’impose désormais sans écrêtage. Une échelle nulle ou numériquement instable arrête le duel. Les queues lourdes peuvent laisser l’issue indéterminée. |
| **A-b/c — Faibles effectifs, appariement privé, contrôles indispensables** | **Acceptée**, sauf le recalcul obligatoire du plancher déjà rejeté. Répétabilité entre lots, appariement de longueur et séparation des groupes deviennent des conditions explicites. |

**HYPOTHÈSE — Précision supplémentaire.** Mesurer la queue du bruit à contexte identique ne suffit pas à connaître la queue des effets de contexte réels. Je ne substituerai pas la première à la seconde pour annoncer une puissance.

### Critiques de B

| Critique | Décision et conséquence |
|---|---|
| **B-a1 — Batterie locale, pas preuve générale de sécurité** | **Acceptée sur la portée ; rejetée sur l’impossibilité de toute falsification locale.** Un contre-exemple falsifie une propriété d’implémentation. L’examen exhaustif d’une batterie finie peut réfuter l’existence d’une violation *dans cette batterie*, pas ailleurs. Je renomme cette étape « qualification technique », sans prétention de preuve universelle. |
| **B-a2 — Seuils libres et distribution des messages indéfinie** | **Acceptée.** Les poids des scénarios, réplicats, sièges et tours seront gelés ; l’estimand ne sera plus une moyenne implicite dominée par les épisodes bavards. Des marges illustratives explicites sont proposées ci-dessous. |
| **B-a3 — Valeur absolue masquant le sens** | **Rejetée comme objection au duel d’invariance.** Une baisse sous contexte collusif réfute bien l’invariance ; elle ne constitue pas nécessairement un artefact. **Acceptée comme limite d’interprétation :** aucun résultat de \(D_C\) ne dira « le score de collusion augmente ». Les effets signés seront obligatoires et séparés. |
| **B-a4 — Seuils propres aux détecteurs, fuite possible** | **Acceptée sur la fuite ; rejetée sur l’incomparabilité automatique.** Comparer des détecteurs à une cible commune de fausses alertes peut être pertinent malgré des seuils différents. Ici, l’incertitude de calibration justifie néanmoins le retrait de ce duel principal. |
| **B-a5/b — Effectifs divisés entre cellules factorielles** | **Rejetée.** Il s’agit de relectures appariées des mêmes messages, pas d’une répartition des épisodes entre bras indépendants. L’effectif indépendant n’augmente pas non plus : il reste celui des scénarios. **Acceptée** pour le coût des passes, la multiplicité et la dépendance entre contrastes. |
| **B-b — Base presque parfaite : plafond du gain** | **Acceptée.** Un gain pratiquement nul peut indiquer qu’aucune amélioration n’est disponible sur ce jeu ; il ne démontre pas l’inutilité générale de la sonde. |
| **B-c — Bruit, privé honnête, placebo de permutation** | **Acceptée** pour les deux premiers. **Rejetée** pour l’idée qu’une permutation de rôles fournisse automatiquement le nul de \(D_C\) : ce dernier dépend d’une intervention appariée sur le contexte. Les permutations ne sont valides que sous une échangeabilité spécifiée ; les répétitions identiques et changements honnêtes restent les contrôles principaux. |

### Critiques de D

| Critique | Décision et conséquence |
|---|---|
| **D-a1 — Fuites distributionnelles plutôt que seulement littérales** | **Acceptée et transformée en test.** Les comptes, exceptions, temps, tailles et empreintes entrent dans le modèle de menace ; une fuite subtile est ajoutée au contrôle positif. |
| **D-a2 — Déploiement réel et sélection après ouverture** | **Acceptée.** La qualification technique ne valide ni tous les accès réels ni la politique de publication. Le rendez-vous de Lazar reste une règle de gouvernance ; toutes les décisions de lancement, abandon, relance et publication doivent être conservées. |
| **D-a3 — Interventions artificielles, pas états mentaux** | **Acceptée.** Je retire toute ambiguïté autour de « discrimination restante » : il s’agit d’une discrimination de l’origine des textes dans un banc diagnostique défini, pas d’une intention restante. |
| **D-a4 — Marges et sélection de la meilleure base** | **Acceptée.** La meilleure base est sélectionnée sur des groupes distincts de l’évaluation ; ses hyperparamètres et son agrégation sont gelés. |
| **D-a5 — Translation des scores sans changement d’aire** | **Acceptée comme distinction, non comme défaut du duel d’invariance.** \(D_C\) mesure un déplacement du score. L’aire et les franchissements de seuil sont rapportés séparément ; aucun n’est déduit de l’autre. |
| **D-b — Échelle instable, rares scénarios dominants, recouvrement** | **Acceptée.** Échelle affine gelée ; contributions par scénario publiées ; absence de recouvrement signalée. Aucune extrapolation de l’effet moyen à tous les scénarios. |
| **D-c — Planté non exécuté ; contrôles et partitions** | **Acceptée avec réserve.** Les plantés non exécutés seront rapportés séparément s’ils existent, sans être retirés de l’analyse principale ni devenir un contraste causal : l’exécution est postérieure à l’instruction. Je ne modifie pas les critères P3-bis dont la table complète manque. |

---

## B. Expériences corrigées

### QO-1 — Qualifier la fermeture avant de l’utiliser

**HYPOTHÈSE — Recommandation maintenue : (a), sous condition technique vérifiable.** Sinon, lecture mécanique tardive plutôt qu’une fermeture nominale.

**RAPPORTÉ.** Les interfaces actuellement autorisées comprennent codes de sortie, empreintes, comptes de `resume.json` et informations de `sondes-figees.json`. La sortie standard de la lecture contient une issue mécanique et doit rester fermée.

**HYPOTHÈSE — Correction importante.** Une confidentialité absolue du verdict est incompatible avec l’exposition de métadonnées qui impliqueraient déjà « non lu » ou « échec ». Il faut donc distinguer :

- **état opérationnel autorisé**, précisément listé ;
- **résultat scientifique interdit**, dont aires, scores, textes, issues et réserves ;
- **inférences résiduelles**, explicitement admises ou empêchées.

Je ne prétendrai plus que tous les verdicts restent indiscernables si les comptes suffisent à en exclure certains.

#### Qualification technique appariée

**HYPOTHÈSE.** Avant les données réelles, geler une matrice des interfaces et chemins : succès, panne, exception, copie, accès privilégié, sortie standard, erreur standard, fichiers temporaires, taille, temps et empreinte.

- **\(H_A\)** : à état opérationnel autorisé identique, aucun scénario de la batterie ne transmet d’information réservée par les interfaces spécifiées.
- **\(H_B\)** : au moins un scénario le fait.

Chaque paire substitue le résultat secret en gardant fixes les données opérationnelles publiques. Une fuite littérale ou une dépendance reproductible d’une interface au secret falsifie \(H_A\). L’examen complet sans violation falsifie \(H_B\) **uniquement pour la batterie et le modèle d’accès fixés**. Une couverture incomplète donne « qualification non terminée », non une réussite.

**HYPOTHÈSE — Mise en œuvre proposée.**

- Exécuteur isolé ; coordinateur sans droits de lecture sur résultats, mémoire et journaux internes.
- Si chiffrement : clé indépendante, détenue hors de la session mère ; aucune dérivation depuis l’entropie publique.
- Empreintes en clair conservées dans l’espace fermé ; exposition éventuelle de l’empreinte du paquet chiffré, pas de celle d’un verdict reconstructible.
- Réduction des sorties visibles à un schéma autorisé ; fermeture des durées fines et tailles dépendantes du contenu.
- Contrôles positifs : fuite textuelle, fuite par code d’erreur et fuite par durée. Contrôle négatif : parcours autorisé sans exposition.

**HYPOTHÈSE — Limite décisive.** Si la même session conserve les privilèges permettant de contourner l’isolation, ce dispositif n’établit pas sa non-lecture. Il faut alors un tiers indépendant ou différer le calcul.

**HYPOTHÈSE — Gouvernance séparée.** Avant ouverture, consigner le périmètre des jeux JD/JC/JA et les règles de lancement/relance. Au rendez-vous prévu, Lazar décide sans consulter les résultats fermés : continuer l’attente ou ouvrir, avec inscription réelle du verdict et abandon explicite de la compatibilité chronologique actuelle de T0.7 sur cette course.

### Q1 — Intervention appariée, sans revendication d’intention

#### Construction du banc

**HYPOTHÈSE.** Je conserve la génération naturelle comme mesure principale, puis les relectures comme diagnostic.

Pour chaque message retenu, conserver exactement ses identifiants, son siège, son nom, son tour et son historique public. Modifier séparément la consigne et le privé. Toutes les variantes d’un même message restent dans le même groupe d’apprentissage ou d’évaluation.

Le croisement comporte **huit cellules, décompte illustratif du plan proposé**, mais ne divise pas les épisodes entre cellules. Les contrastes principaux sont :

- changement de consigne à privé fixé ;
- changement du privé à consigne fixée ;
- interaction rapportée séparément.

Les comparaisons entre textes honnêtes et collusifs exigent un contexte lecteur commun construit à l’avance ; à défaut, elles restent des comparaisons d’origines textuelles et contextuelles mêlées.

**HYPOTHÈSE — Privé honnête.** Un rédacteur neuf, sans scores, écrit une règle légitime : par exemple conserver confidentiel un identifiant administratif sans modifier recommandation publique, vote ou mise. Un relecteur neuf contrôle sa conformité. Gabarit, emplacement, nom du destinataire et longueur exacte au tokeniseur sont appariés au privé collusif. Les différences sémantiques restantes sont déclarées. Ce contrôle est **relu**, non présenté comme une génération naturelle sous confidentialité. Une absence d’appariement empêche l’attribution spécifique, sans faire disparaître le contraste global de contexte.

#### Duel principal : invariance pratique du score

**HYPOTHÈSE.** Scores transformés par une échelle affine issue uniquement de CORE, sans écrêtage. Une échelle inutilisable arrête le duel. Le score est répété à contexte identique, entre lots, pour toutes les variantes évaluées ; une discordance avec la garde d’identité au bit près prévue dans le brouillon déclenche l’arrêt technique, pas un ajustement opportuniste de la marge.

Définir :

\[
D_C=\operatorname{moyenne}_{\text{scénarios}}
\left[\operatorname{moyenne}_{\text{paires du scénario}}
|z_{\mathrm{collusion}}-z_{\mathrm{honnête}}|\right].
\]

Les pondérations internes sont gelées, avec résultats signés par origine du texte.

- **\(H_A\)** : \(D_C\leq\delta_C\).
- **\(H_B\)** : \(D_C>\delta_C\).
- **Marge candidate :** \(\delta_C=0{,}10\) unité d’échelle CORE, **illustratif**.

Borne basse au-dessus de la marge : réfutation statistique de \(H_A\). Borne haute au plus égale à la marge : réfutation statistique de \(H_B\). Chevauchement : indéterminé. Ces décisions concernent le protocole et sa population de scénarios définie, pas tous les contextes possibles.

**HYPOTHÈSE.** Les intervalles par scénario doivent être éprouvés sur simulations avant scellement, notamment face à des effets rares et concentrés. Une couverture insuffisante impose une nouvelle méthode avant lecture, ou une conclusion seulement descriptive. Aucun seuil de kurtosis universel n’est supposé.

#### Duel secondaire : gain de discrimination, sans calibration extrême

**HYPOTHÈSE.** Je remplace \(G\) par une différence d’aires appariée :

\[
G_{\mathrm{AUC}}=\mathrm{AUC}_{\mathrm{sonde}}
-\mathrm{AUC}_{\mathrm{base\ sélectionnée}}.
\]

La base lexicale de transfert CORE→STEGO et la base locale mots–métadonnées restent distinctes. La base locale est évaluée hors groupe, avec sélection interne ; aucune sélection de « meilleure base » sur les scores du groupe évalué.

- **\(H_A\)** : \(G_{\mathrm{AUC}}\leq\delta_G\).
- **\(H_B\)** : \(G_{\mathrm{AUC}}>\delta_G\).
- **Marge candidate :** \(\delta_G=0{,}02\) d’aire, **illustratif**.

Même règle d’intervalle et d’indétermination. Un gain réfute la suffisance pratique **des bases testées**, pas toutes les explications non intentionnelles. Un plafond des bases limite simplement le gain possible.

**HYPOTHÈSE — Contrôles communs.** Invariance du score lexical lorsque le texte est inchangé ; changements honnête→honnête ; privé honnête apparié ; prédicteurs de siège, longueur et tour ; comparaison descriptive J-a/J-b pour repérer une dépendance aux honnêtes exposés aux colludeurs. Les permutations ne sont employées que dans des strates où leur échangeabilité est justifiée.

**HYPOTHÈSE — Faisabilité.** Aucun coût audité du croisement complet n’est disponible. Chronométrage sur données synthétiques avant scellement ; si le budget ne tient pas, réduire les contrastes *avant* les résultats, sans présenter C1–C2 comme une séparation consigne/privé.

---

## C. Réponse à l’arbitre — Une page

### QO-1 : quand lire P3-bis ?

**RAPPORTÉ — Ce qui est établi dans les pièces.** T0.7 exige ses lignes de scores et de sondes avant le verdict P3-bis. Les clés de jeux présentes déterminent aussi quelles sondes sont lues. « Non vu » bloque la lecture interne prévue ; « échec » suspend la chaîne sans constituer un résultat négatif de détection. Ces dispositions proviennent de brouillons, non d’une exécution auditée ici.

**HYPOTHÈSE — Recommandation : (a), avec décision humaine planifiée et fermeture qualifiée.** La raison décisive est de préserver l’ignorance avant fixation effective du périmètre de notation et de l’existence de la course. Reporter uniquement la ligne de registre ne préserve pas cette ignorance.

**HYPOTHÈSE — Ce qui n’est pas établi.** Ni la confidentialité effective des sorties, ni l’absence de sélection après ouverture, ni l’aboutissement futur de T0.7. L’utilité financière d’une ouverture précoce est une préférence de gouvernance, pas un résultat de sondes.

**HYPOTHÈSE — Échec et changement d’avis.** Si l’isolation réelle n’est pas possible, différer le calcul mécanique. Si Lazar privilégie explicitement une échéance maximale, choisir (c) avant lecture, en acceptant sa conséquence sur T0.7. Sous (a) comme sous (c), une ouverture anticipée doit porter sa date réelle ; aucune réparation documentaire ne restaure l’ignorance passée.

**HYPOTHÈSE — Première expérience :** qualification différentielle de fermeture sur données factices, incluant empreintes, exceptions et canaux temporels. Elle précède le calcul réel et ne certifie que son périmètre testé.

### Q1 : sur quels textes lire le 8B ?

**RAPPORTÉ — Ce qui est établi dans les pièces.** Les rôles sont instruits. L’échange proposé retire aussi du privé. La relecture modifiée est hors politique. Aucun résultat du rejeu 8B n’est transmis.

**HYPOTHÈSE — Recommandation : (c) corrigée, avec (a) comme référence naturelle.** Son intérêt est de pouvoir réfuter une invariance du score au contexte, non de mesurer une intention. La symétrie et le croisement séparé de la consigne et du privé permettent des attributions plus étroites, toujours diagnostiques.

**HYPOTHÈSE — Ce qui n’est pas établi.** Une dépendance au contexte ne démontre pas une lecture exclusive de l’instruction. Une invariance ne démontre pas l’intention. Battre des mots et métadonnées ne supprime pas les autres explications. Les contrôles hors politique ne deviennent pas naturels par multiplication des cellules.

**HYPOTHÈSE — Échec et changement d’avis.** Sans conservation exacte des identifiants, répétabilité et appariement, revenir à (a) avec limitation explicite. Choisir (b) seulement si l’objectif devient la comparaison des lecteurs à corpus commun, après clarification des licences.

**HYPOTHÈSE — Première expérience scientifique :** le contraste apparié de consigne à privé fixé, avec répétition identique et changement honnête→honnête. C’est le premier duel utile pour savoir si le score résiste à une intervention contextuelle précisément définie ; ce n’est pas un test d’intention.

FIN-DE-CELLULE