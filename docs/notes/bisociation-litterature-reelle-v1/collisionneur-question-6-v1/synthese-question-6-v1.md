# Synthèse — collisionneur, question 6 : l'apprentissage profond peut-il à lui seul identifier les paramètres qui créent la fertilité ? — v1

Lecteur neuf (Fable 5.1, famille de l'espèce A : réserve en fin). Lu : question servie, `faits-question-6-v1.md`, `etat.md`, `question-etage3.md`, dix cellules (III.1 : A, B, C, D ; III.2 et III.3 : A, B, C). Rien d'autre. Toute référence est SUPPOSÉ (R7) ; tout seuil est illustratif, à préenregistrer.

## Verdict

Les trois espèces présentes aux trois tours (A Fable 5.1, B Opus 4.6, C Argon) établissent, sans contradiction entre elles ni avec D (Kimi, tour III.1 seul), que « identifier à lui seul » est mal posé : l'identifiabilité est une propriété du couple classe de modèles × loi des données sous hypothèses, jamais de l'algorithme ; sans variable auxiliaire, le démêlage non supervisé n'est pas identifiable par théorème ; avec auxiliaire (temps, environnements), les théorèmes identifient des sources latentes à permutation et transformation près, jamais la flèche entre une source et la fertilité. Elles réfutent dans la pièce de conv-audit à la question 6 : le glissement « latentes identifiées → causes identifiées », les hypothèses « offertes gratuitement » par les données scientométriques (hypothèse, ramenée à une mesure préalable), et le score de recouvrement comme critère de mort (il mesure la récupération de latentes, pas la discrimination cause/leurre). Elles réfutent aussi, dans les pièces de la question 5 et dans leurs propres conceptions initiales, l'idée que prédire une dose jamais vue dans une course randomisée teste l'identification : sous randomisation, régression et effet causal coïncident ; seul le dispositif « affectation biaisée à l'entraînement → épreuve randomisée » sépare estimer d'identifier. Restent hors de portée : transport vers la science réelle, manipulabilité des « paramètres », validité du proxy de fertilité.

## (a) Théorèmes d'identifiabilité et hypothèses exactes

- A (E3-T1-conception-A, A1, A3) : « l'identifiabilité est une propriété du couple classe de modèles × distribution des données, jamais de l'algorithme » ; les théorèmes à auxiliaire « ne disent rien de la flèche entre une source et la reprise ».
- B (E3-T1-conception-B, synthèse ; E3-T3-reponse-B, c) : « identifier des latentes signifie les retrouver à transformation affine près, pas prouver qu'elles sont causales » ; « aucun théorème publié ne dit qu'un modèle non supervisé sur des données observationnelles i.i.d. identifie les causes d'une variable cible Y sans hypothèse supplémentaire ».
- C (E3-T1-conception-C, table 2) : seule à écrire les hypothèses exactes par famille — ICA non linéaire à auxiliaire : indépendance conditionnelle en famille exponentielle, mélange invariant en u, variabilité suffisante (2k+1 valeurs de u) ; CITRIS : cibles d'intervention connues ; LiNGAM/NOTEARS : suffisance causale, linéarité, acyclicité ; ICP : issue non intervenue entre environnements.
- D (E3-T1-conception-D) : « deux mondes peuvent produire exactement les mêmes observations tout en ayant des effets différents sous do(contact) ».

Accord complet au niveau théorème. Précisions nées de la critique : C montre contre B que l'iVAE, par consistance, recouvre toutes les sources, causales ou non ; exiger qu'il « ne retrouve pas » l'accompagnateur contredit son théorème (E3-T2-critique-croisee-C, sur B 1, b1 ; A aussi, E3-T2-critique-croisee-A, sur B 1) ; B accepte (E3-T3-reponse-B, A-1). B objecte à A que le raccord iVAE → ICP n'est couvert par aucun théorème cité ; A répond que l'estimande est conservé mais pas le test linéaire-gaussien, et passe à un test non paramétrique avec contrôle par bijection monotone (E3-T3-reponse-A, B-a1). C montre que la transformation de rang détruit la linéarité de LiNGAM ; A la retire, ajoute un contrôle de kurtosis (E3-T3-reponse-A, en-tête). Non tranché : constante de variabilité 2k ou 2k+1 (A : « à vérifier ») ; Rosenfeld 2021 cité par B pour ICP, par A pour IRM (à vérifier).

## (b) Hypothèses « gratuites » : scientométrie et courses

- A (E3-T1-conception-A, A4) : HYPOTHÈSE ; « l'ordre temporel donne une direction mais n'exclut pas les confondeurs cachés… les normes de citation varient par discipline et par décennie ».
- B (E3-T1-conception-B, P3, P4, P7) : « si le mécanisme causal varie entre environnements, la prédiction invariante rejette les variables causales au lieu de les retenir ».
- C (E3-T1-conception-C) : les données scientométriques « n'offrent aucune de ces hypothèses gratuitement » ; « Oui, partiellement » pour les courses si u désigne les bras randomisés et le juge est figé.
- D (E3-T1-conception-D) : HYPOTHÈSE partout ; randomisation des courses « RAPPORTÉ, non audité ».

Accord : rien n'est gratuit, tout est à mesurer. Désaccord initial : C affirmait la violation ; A lui reproche de ne proposer « une seule mesure sur OpenAlex » (E3-T2-critique-croisee-A, sur C 1), B une dérive de 15 % non calibrée (E3-T2-critique-croisee-B, sur C 3). Résolution convergente : A pose le duel « un classifieur X→U bat-il Ẑ→U de plus qu'une marge scellée ? » (E3-T2-critique-croisee-A, duel final) ; C l'adopte comme Expérience 0 avec rang de variabilité et dérive Δ (E3-T3-reponse-C, Exp. 0) ; B en fait le diagnostic d'accuracy X→U à faire en premier (E3-T3-reponse-B, c) ; A en fait des préconditions de jugeabilité publiées avant lecture (E3-T3-reponse-A, E1). Courses : A montre contre C que huit doses bornent l'identification à trois latentes (m ≥ 2k+1) ; C croise doses × règles (E3-T3-reponse-C, A-10). Ensemble vide d'ICP (défaut T2 d'A : violation ou manque de puissance) : publier le nombre d'ensembles acceptés, relancer après centrage-réduction de Y (E3-T3-reponse-A, C-b2). Apport de B seule : interférence entre paires partageant une niche ; A ajoute randomisation par grappe et test de débordement, C des paires à dose 0 en contexte partagé.

## (c) Ce qu'apprend le non supervisé, et sa détection

- A (E3-T1-conception-A, A8, E5) : OBSERVÉ-NON-AUDITÉ, « plausible par l'avantage cumulatif » ; sonde linéaire sur taille, âge, langue, prestige ; instabilité inter-graines.
- B (E3-T1-conception-B, Exp. 4 ; E3-T3-reponse-B, C-3) : stabilité contre ACP ; après C, la corrélation aux nuisances devient « un diagnostic d'échec, pas de succès ».
- C (E3-T1-conception-C, c) : quatre facteurs ; sonde R² > 0,60 ; MCC inter-graines < 0,50.
- D (E3-T1-conception-D) : « HYPOTHÈSE testable ».

Accord : prédiction à tester ; détection par sondes, stabilité, graphe témoin sans sémantique (Price 1976 ou modèle de configuration, de C, repris par A et B). Apports de C seule, acceptés par A : SPECTER, entraîné sur le graphe de citations, injecte l'issue dans les covariables (« point que je n'avais pas vu », E3-T3-reponse-A, C-a3) ; l'appariement hongrois sous-estime la stabilité d'un VAE à prior isotrope (rotation indéterminée), remplacé par angles de sous-espaces ; l'erreur de mesure des nuisances laisse un R² partiel positif par atténuation, d'où un plancher mesuré (E3-T3-reponse-A, C-b5).

## (d) Épreuve empirique : mondes inventés, puis intervention jamais vue

Mondes inventés. A : appariés en variance, corrélation marginale et, après B, partielle ; sources indépendantes conditionnellement à u (son générateur III.1 violait cette hypothèse, défaut avoué, E3-T3-reponse-A, C-b1) ; mondes-stress étiquetés. B : bras conforme et violé ; sous-test 1a (recouvrement) puis 1b (tri causal aval) (E3-T3-reponse-B, Exp. 1). C : trois bras — conforme, dérive calibrée sur l'Expérience 0, confusion pure à effet nul avec rétroaction Y → contact (E3-T3-reponse-C, Exp. 1). D : mondes compagnons ne violant qu'une condition ; mondes observationnellement équivalents — C montre qu'aucun estimateur n'y atteint 0,80 / 0,05 (borne de Le Cam) : « le résultat d'échec est une identité probabiliste » (E3-T2-critique-croisee-C, sur D b3), sans réplique. Accord sur le défaut T3 d'A : générateur distinct du banc de réglage, famille scellée (E3-T2-critique-croisee-A, T3). Contrôles retenus par les trois : loi nulle du MCC par permutation ; intervention fantôme (dose journalisée, non délivrée ; origine D selon A) à la place des placebos « titres de la même niche » ou « ordre d'affichage » ; confondeur caché pur ; rétroaction.

Intervention jamais vue. C contre A : « prédire d = 7 teste uniquement la régularité de l'interpolation » (E3-T2-critique-croisee-C, sur A a4) ; A contre C : « la voie observationnelle n'existe pas dans les courses », déjà randomisées (E3-T2-critique-croisee-A, sur C 3). Même refonte acceptée par les deux : entraînement sur affectation biaisée par un confondeur que le juge récompense aussi, épreuve sur course randomisée, doses d'interpolation et d'extrapolation dans la capacité du format (E3-T3-reponse-A, E4 ; E3-T3-reponse-C, Exp. 2). B repositionne son expérience 3 en test d'estimation (E3-T3-reponse-B, Exp. 3). C seule : gabarit à capacité fixe, remplissage neutre, pour ne pas confondre dose et format (objection de B).

Transport. A : hors de portée (A5). D : « non décisive sans estimande commun » ; C : donc non réfutable par construction (E3-T2-critique-croisee-C, sur D a4). B : K ≥ 5 chocs, test de signe et d'équivalence (E3-T3-reponse-B, Exp. 5), A ayant noté qu'un seul signe vaut 1/2 sous l'hypothèse nulle. C seule définit un estimande commun courses/OpenAlex : log-odds d'apparition conjointe et de reprise par un tiers d'un opérateur formel de A avec un concept de B (E3-T3-reponse-C, B-5), avec faux choc administratif et valeur E ≥ 2 pour que τ_QE ne soit pas pris pour vérité (de B, E3-T2-critique-croisee-B, sur C 1).

Puissance. B et C calculent indépendamment qu'avec N = 30 la puissance contre une couverture réelle de 70 à 80 % est d'environ 0,55 (E3-T2-critique-croisee-B, sur A b3 ; E3-T2-critique-croisee-C, sur A b4) ; A accepte : N par puissance scellée, sinon « non jugeable avant exécution ». A contre C : N = 200 sur deux doses donne un écart-type d'environ 7 points, ε = 2 est noyé ; n ≈ 770 par bras pour 5 points (E3-T2-critique-croisee-A, sur C 4, b) ; C passe à un plan intra-paire, n = 400, ε = 5 (E3-T3-reponse-C, A-4).

## (e) Critères de mort chiffrés (illustratifs)

- A (E3-T3-reponse-A, c) : voie « hypothèses gratuites » morte si, sur ≥ 20 mondes × 5 graines honnêtes, rétention de Z_c et rejet de Z_d ne dépassent pas la ligne de base ACP + régression invariante de plus de 10 points, ou s'effondrent quand le confondeur est modulé comme la cause.
- B (E3-T3-reponse-B, c) : MCorr < 0,5 sur ≥ 50 % des sources en mondes conformes, ou accuracy X→U ≤ hasard + 5 points sur OpenAlex.
- C (E3-T3-reponse-C) : rang < 2k ou Δ_dérive > 0,05 ; MCC < 0,75 sous dérive calibrée ou fausse sélection > 5 % en confusion pure ; dans la course, erreur > 5 points sur la dose jamais vue ou gain < 5 points sur le régresseur naïf quand l'estimateur ancré sur la randomisation réussit.
- D (E3-T1-conception-D) : barre commune 0,80 / 0,05 / ≥ 20 % de réduction d'erreur ; critiquée par B (non calibrée) et A (taux par arête inapplicable), sans réponse.

Signe commun : la voie meurt sur un échec ; un succès ne vaut que sous préconditions vérifiées, « dans le monde de la course ».

## Références et statut

Toutes SUPPOSÉ. Déjà dans les pièces : Hyvärinen-Pajunen 1999 ; Locatello 2019 ; Hyvärinen-Morioka 2016 ; Khemakhem 2020 ; Lippe 2022 ; Schölkopf 2021 ; Shimizu 2006 ; Zheng 2018 ; Reisach 2021 ; Runge 2019 ; Peters-Bühlmann-Meinshausen 2016 ; Arjovsky 2019 ; Rosenfeld 2021 ; Wager-Athey 2018 ; Shi 2019 ; Shalit 2017 ; Chernozhukov 2018 ; Callaway-Sant'Anna 2021 ; Boudreau 2017 ; Catalini 2018 ; Azoulay 2010, 2019 ; Borjas-Doran 2012 ; Campos 2018 ; Pearl-Bareinboim 2014 ; Holland 1986 ; VanderWeele-Ding 2017 ; Aronow-Samii 2017 ; Hudgens-Halloran 2008. Nouvelles : Bareinboim-Pearl 2016, Price 1976, Barabási-Albert 1999, SciBERT 2019, SPECTER 2020, Roth 2022 « Pretest with Caution » (à vérifier), suite de Reisach sur le tri par R² (à vérifier), toutes par A ; Miguel-Kremer 2004, Cranmer 2023 PySR, par B ; Molloy-Reed, Le Cam, par C. Rosenfeld 2021 : attribution ICP/IRM à vérifier.

## Expériences décisives retenues (ordre commun)

1. Expérience 0 sur OpenAlex, processeur seul : rang de variabilité ; Δ_dérive = Acc(X→U) − Acc(Ẑ→U) ; accuracy X→U contre hasard ; étiquettes permutées en contrôle. Signe : thèse de conv-audit morte si rang < 2k ou Δ > 0,05.
2. Banc de mondes scellé à trois bras et mondes-stress, générateur distinct du réglage ; étages démêlage et sélection causale notés séparément ; lignes de base ACP et tris par variance, R², kurtosis. Signe : échec en conforme = implémentation invalide ; succès en conforme, échec en dérive ou confusion = prétention morte.
3. Course « entraînement biaisé → épreuve randomisée », 6 à 8 doses, gabarit fixe, cellules isolées, intervention fantôme, rejugement permuté, test de débordement, N par puissance scellée. Sur devis.
4. Transport sur K ≥ 5 familles de chocs, estimande commun, faux choc administratif, valeur E ≥ 2.

## Ce que l'absence de Kimi retire

D n'a ni critiqué ni répondu. (1) Ses apports restent non défendus : équivalence observationnelle, démontée par C sans réplique ; épreuve de transport jugée non réfutable ; barre uniforme ; estimation de calcul (2 000 à 20 000 €, contre ~200 $ pour B et 1 650 à 2 300 € pour C) jamais confrontée. (2) A, B et C n'ont reçu que deux critiques au lieu de trois. (3) Deux lignées restent, dont deux espèces sur trois (A, B) de la même : un consensus à trois peut être un consensus de lignée. Légué par D et repris : intervention fantôme, mondes compagnons à une violation, audit de la randomisation.

## Décisions à proposer à Lazar

D1. Corriger `reponse-conv-audit-question-6-v1.md` en v2. Enjeu : trois formules réfutées (« identifient — avec l'hypothèse », « offertes par nos données », « recouvrement sous un seuil »). Options : (a) v2 à deux niveaux (latentes / flèche vers Y), préconditions mesurées, critère de mort à deux étages ; (b) erratum annexé ; (c) rien. Recommandation : (a), confiance haute. Défaut sous 48 h : (a).

D2. Préenregistrer (R1, R2) puis exécuter l'Expérience 0 et le banc scellé sur processeur et petits modèles. Enjeu : seule donnée à vérité terrain ; fournit les préconditions sans lesquelles rien n'est jugeable. Options : (a) processeur d'abord, devis GPU ensuite ; (b) GPU d'emblée (~50 h selon B, ~400 € selon C, illustratifs) ; (c) attendre G0. Recommandation : (a), confiance moyenne-haute. Défaut sous 48 h : rédaction du préenregistrement seulement ; aucun pour la part GPU (dépense).

D3. Inscrire dans la conception des courses de l'étape 2 : affectation biaisée puis épreuve randomisée, 6 à 8 doses, gabarit fixe, cellules isolées, intervention fantôme, test de débordement, N par puissance scellée. Enjeu : sans cela aucune course ne sépare estimer d'identifier. Options : (a) exigence du préenregistrement des courses ; (b) bras optionnel sur devis ; (c) ne pas tester l'identification dans les courses. Recommandation : (a), confiance haute. Défaut sous 48 h : (a) ; aucun si Lazar y voit une modification du programme.

D4. Relancer D (Kimi) sur III.2 et III.3. Enjeu : troisième critique et seconde lignée. Options : (a) relancer, 1 à 3 USD (extrapolé de III.1, illustratif) ; (b) accepter l'absence ; (c) autre lignée. Recommandation : (a), confiance moyenne. Aucun défaut (dépense).

## Réserves

- Aucune mesure faite : tout est conception ; les « établis » sont des théorèmes rapportés de mémoire, jamais lus sur PDF.
- Le synthétiseur est de la famille d'A ; A et B sont de la même famille. C, la plus tranchante en III.1, a tout accepté en III.3 : rare, possible complaisance (R4).
- Les cellules citent des règles du collisionneur (« B4 », « Règle 2 ») non lues ici ; les calculs de puissance (770 par bras, N ≥ 100) sont illustratifs, non audités.
- L'estimande commun de C engage la définition de la fertilité (question 3) : antériorité à vérifier (R8).
