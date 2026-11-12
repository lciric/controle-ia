# Faits servis — question-6-identification-collisionneur-v1.md (pièces de conv-audit, copiées mot pour mot de canal/conv-audit-n04, empreintes vérifiées) — v1

Assemblé par session-depot le 31 octobre 2026. Pièces à attaquer, pas des faits établis ; chaque référence reste à vérifier (R7).

## Pièce : question-5-causes-v1.md (sha256 8dfc74a332de8147…)

# Question 5 — identifier par apprentissage profond les paramètres qui créent la fertilité — v1

Mots directs de Lazar (30 octobre 2026, 18:10 heure de Paris), transcrits sans reformulation de fond :

« [Sur : le modèle doit passer par un petit nombre de traits nommés, puis ablation ; ou entraîner libre puis extraire la loi par régression symbolique ; distinguer prédire et causer :] oui, testons les deux. [Sur : pour les paramètres qui créent, il faut des quasi-expériences — chercheurs qui changent de laboratoire, conférences qui mettent deux niches en présence, expériences humaines contrôlées comme Derex et Boyd :] on ne peut pas identifier par apprentissage profond les paramètres qui créent la fertilité ? »

Consigne de forme (de Lazar) : « Je souhaite une version plus approfondie de cette tâche, pas une version plus longue. Avant de la reformuler : (1) indiquez ce qu'un expert du domaine ferait ici, et que je ne demande pas ; (2) précisez les données brutes qu'il utiliserait au départ, au lieu de celles déjà analysées ; (3) indiquez les méthodes et outils spécifiques qu'il utiliserait ; (4) expliquez ce qui, en dehors de vous ou de moi, permettrait de vérifier la validité du résultat. Ensuite, reformulez ma demande pour qu'elle réponde précisément à cette exigence. »

Contexte minimal : questions 1 à 4 jointes. Toute référence citée de mémoire est à marquer SUPPOSÉ. Niveau méthode ; aucune décision n'est prise par le répondant.

## Pièce : reponse-conv-audit-question-5-v1.md (sha256 a47ba91677ee9f31…)

# Réponse de conv-audit à la question 5 (identifier par apprentissage profond les paramètres qui créent la fertilité) — v1

conv-audit, 30 octobre 2026 (Fable 5.1, 18:15 heure de Paris), transcrite sans modification de fond. Références de mémoire : SUPPOSÉ.

**Position.** Non, pas avec des données d'observation seules : un réseau entraîné sur les citations apprend ce qui accompagne la reprise, pas ce qui la provoque (« voir » contre « faire », Pearl). Il faut une source d'intervention ou une hypothèse écrite. Trois voies : nos courses (interventions contrôlées), les expériences naturelles de la littérature, l'invariance entre environnements. L'apprentissage profond sert dans chacune, n'en remplace aucune.

## (1) Ce qu'un expert ferait, et que Lazar ne demande pas
- Écrire le graphe causal supposé (contacts, structure commune, désaccord, taille, âge, mode, financement, reprise) et les flèches inconnues.
- Prendre nos courses comme laboratoire : paires au hasard contre par la règle (randomisation) ; 0, 2, 5, 10 titres dans le tableau minimal (dose de contact) ; courbe dose-réponse mesurée sur la survie aux tests de mort et la reprise entre générations.
- Exploiter les expériences naturelles (différence de différences, contrôle synthétique) : décès de chercheurs étoiles (Azoulay, Graff Zivin et Wang 2010), déménagements, conférences annulées en 2020, financements imposant l'interdisciplinarité, fusions de revues.
- Apprentissage profond là où il est causal : découverte de structure sur séries multicouches (PCMCI de Runge, NOTEARS, versions avec interventions) ; prédiction invariante entre sous-domaines, décennies, pays (Peters, Bühlmann et Meinshausen 2016 ; Arjovsky 2019) ; effets hétérogènes (forêts causales d'Athey et Wager, Dragonnet, TARNet) sous « pas de facteur caché » avec analyse de sensibilité (valeurs E).
- Distinguer causalité dans le modèle (ablation) et dans le monde (prédire l'effet d'une intervention jamais vue).
- Simuler : modèle d'agents étalonné, substitut neuronal, interventions in silico, confrontation aux expériences naturelles ; régression symbolique sur la fonction causale.
- Préenregistrer des effets signés et chiffrés, avec placebo et contrôle négatif.

## (2) Données brutes
Panel des chercheurs d'OpenAlex (affiliations par année, coauteurs), décès de chercheurs étoiles (Azoulay) ; programmes de conférences et annulations 2020 ; bases de financement (NSF, ERC, CORDIS) ; fusions et créations de revues ; nos courses (journal des affectations, verdicts, tests de mort par génération) ; expériences humaines publiées (Derex et Boyd 2016 ; Mason et Watts) ; environnements nombreux (même hypergraphe par sous-domaine, décennie, pays).

## (3) Méthodes et outils
Randomisation et dose dans nos courses ; différence de différences et contrôle synthétique avec tendances préalables, placebos, contrôles négatifs ; PCMCI, NOTEARS ; prédiction causale invariante, minimisation du risque invariant ; forêts causales, réseaux à deux têtes, apprentissage double robuste, valeurs E ; modèle d'agents, substitut, régression symbolique ; transition de phase par intervention sur la dose comparée à la courbe d'observation.

## (4) Vérification hors de nous
Prédiction d'une intervention jamais vue réalisée à la course suivante ; expériences naturelles indépendantes du modèle ; reproduction sur d'autres domaines et décennies ; courses randomisées étiquetées par les tests de mort.

## Reformulation
« Identifier les paramètres qui créent la fertilité. 1. Graphe causal supposé. 2. Trois voies avec hypothèses écrites : (a) interventions randomisées dans nos courses avec courbe dose-réponse préenregistrée ; (b) expériences naturelles par différence de différences et contrôle synthétique ; (c) invariance entre environnements exploitée par apprentissage profond, découverte de structure, effets hétérogènes sous analyse de sensibilité. 3. Modèle d'agents étalonné et substitut neuronal, régression symbolique. 4. Transition de phase par intervention sur la dose de contact comparée à l'observation. 5. Validité : prédire correctement l'effet d'une intervention jamais vue, confirmé par une expérience naturelle indépendante ; sinon corrélat, pas cause. »

## Pièce : reponse-fable-independante-question-5-v1.md (sha256 9170d230aca80767…)

# Réponse indépendante — question 5 : identifier par apprentissage profond les paramètres qui *créent* la fertilité — v1

- Répondant : sous-agent neuf et indépendant (n'a lu que `question-5-causes-v1.md` et, pour le contexte, les questions 1 à 4 ; aucune réponse, relecture ni revue lue ; rien lu sous `donnees/`).
- Modèle : Claude Fable 5.1 (`claude-fable-5-1`).
- Date : 2026-10-30 17:20 UTC (`date -u`).
- Statut : niveau méthode ; aucune décision prise. Références : « vérifiée (existence) » = titre et lieu de publication retrouvés par recherche web ce jour, contenu non vérifié sur PDF empreinté (R7 : aucun chiffre opposable) ; « SUPPOSÉ » = citée de mémoire.

## Verdict court

Oui, à une condition qui n'est pas d'apprentissage profond : un réseau peut *estimer* des effets causaux, il ne peut pas *fournir* ce qui les identifie. Sans intervention, expérience naturelle ou hypothèse d'invariance explicite, le modèle le plus profond apprend les paramètres qui accompagnent la fertilité (sélection, mode, prestige, survivants), jamais ceux qui la créent. « Peut-on ? » devient « quelle variation exogène possédons-nous ? » ; l'apprentissage profond sert ensuite à absorber les confondeurs à haute dimension (texte, réseau) et à estimer des effets hétérogènes et non linéaires — la forme même d'une « transition de phase ».

## (1) Ce qu'un expert ferait, et que la question ne demande pas

1. **Écrire l'estimande avant le modèle** : le « traitement » (mettre deux niches en présence : comment, à quelle dose, à quelle date), l'« unité » (paire de niches, chercheur, papier), le « résultat » (fertilité, définie en question 3, mesurée sans savoir si la paire a réussi), la quantité visée (effet moyen, effet au seuil, dose-réponse). Sans cela, « les paramètres qui créent » n'est pas estimable.
2. **Dessiner le graphe causal et nommer les confondeurs**, observés (prestige, financement, mode, proximité, langue) et *non observés* : ce sont eux qui décident la stratégie d'identification, pas la taille du modèle.
3. **Traiter l'interférence** : un pont entre A et B change C ; l'hypothèse d'unités indépendantes (SUPPOSÉ : Rubin) est violée ; estimateurs sous interférence de réseau (SUPPOSÉ : Aronow et Samii 2017 ; Hudgens et Halloran 2008).
4. **Distinguer trois sens de « peut-on »** : (a) effet d'un paramètre manipulable — oui, si variation exogène ; (b) structure causale entre paramètres — seulement jusqu'à une classe d'équivalence ; (c) paramètres latents « qui créent » appris de bout en bout — apprentissage de représentations causales, avec résultats d'impossibilité sans interventions ni environnements multiples (Schölkopf et al. 2021, « Toward causal representation learning », vérifiée (existence)).
5. **Mesurer la fertilité par un canal que le traitement ne touche pas autrement** : des citations futures sont aussi causées par la visibilité des auteurs ; préférer, par exemple, la réutilisation d'un objet mathématique précis dans une troisième niche.
6. **Analyse de sensibilité** à la confusion non mesurée (SUPPOSÉ : bornes de Rosenbaum ; « E-value », VanderWeele et Ding 2017), publiée avec l'estimation.
7. **Contrôle négatif** : un résultat que le traitement ne peut pas causer (fertilité *antérieure* à la rencontre) ; un effet trouvé là mesure la sélection.

## (2) Données brutes qu'il prendrait au départ

Pas les distances déjà calculées (Sourati-Evans, cité en question 1), ni les scores de nouveauté déjà agrégés, mais :

- **Trajectoires d'affiliation auteur–institution–date** (OpenAlex, Microsoft Academic Graph) : déplacements, décès, départs forcés — le matériau des expériences naturelles.
- **Texte intégral et historique de versions** (arXiv, PubMed Central, bioRxiv) : proxy des confondeurs latents (ce qu'un auteur savait, suivait, imitait), condition pour que l'apprentissage profond serve à la causalité (SUPPOSÉ : Veitch, Sridhar, Blei 2020 ; Keith, Jensen, O'Connor 2020).
- **Programmes et listes de participants de conférences**, avec annulations, déplacements, fusions de sessions (variation exogène de « mise en présence »).
- **Dossiers de financement avec score et seuil** (NIH RePORTER, ERC, ANR si accessible) : discontinuité de régression sur « projet interdisciplinaire financé ou refusé de justesse ».
- **Plans d'étage et déménagements universitaires** (Catalini 2018, « Microgeography and the direction of inventive activity », vérifiée (existence)).
- **Événements historiques datés** : morts prématurées de chercheurs centraux (Azoulay, Graff Zivin, Wang 2010, « Superstar Extinction », vérifiée (existence)) ; effondrement de l'URSS (Borjas et Doran 2012, vérifiée (existence)) ; expulsions sous le nazisme (SUPPOSÉ : Waldinger 2010, 2012).
- **Journaux d'exécution de l'organisme** : paire proposée, proposeur, juge figé, date, résultat du test de mort — seule expérience dont nous contrôlons le mécanisme d'affectation.
- **Mondes inventés à loi génératrice connue** : seules données où « créer » a une vérité terrain.

## (3) Méthodes et outils

**A. Interventions (le seul « créer » sans hypothèse).**
- Expérience randomisée dans l'organisme : paires de niches tirées entre bras (règle « loin en domaine, proche en concept », tirage aléatoire, règle inverse), juges figés, fertilité jugée par un juge *autre* que celui qui a servi à choisir. Elle isole l'effet de la *règle*, pas la fertilité dans la science humaine.
- Expériences humaines : symposium où la proximité des participants est tirée au sort (Boudreau et al. 2017, *Review of Economics and Statistics*, vérifiée (existence)) ; connectivité partielle de groupes en laboratoire (Derex et Boyd 2016, *PNAS*, vérifiée (existence)). Réplicable à petite échelle (école d'été aux binômes randomisés).

**B. Expériences naturelles (quasi-expériences).**
- Différences de différences et événements échelonnés (déménagements, décès, arrivées) avec estimateurs robustes à l'hétérogénéité des dates (SUPPOSÉ : Callaway et Sant'Anna 2021 ; de Chaisemartin et D'Haultfœuille 2020).
- Discontinuité de régression au seuil de financement ; discontinuité géographique (étage, bâtiment).
- Variables instrumentales : l'arrivée d'un chercheur d'une niche B dans un laboratoire de niche A, instrumentée par un choc extérieur (fermeture d'un institut, politique de visas).
- Appariement et contrôle synthétique (SUPPOSÉ : Abadie) pour les paires de niches « témoins » évoquées en question 4 : il faut des témoins *avant la date*, choisis par une règle gelée.
- Ce que l'apprentissage profond ajoute : **apprentissage double orthogonalisé** (Chernozhukov et al. 2018, *Econometrics Journal*, vérifiée (existence)) — le réseau prédit traitement et résultat à partir du texte et du réseau de citations, l'effet est estimé sur les résidus ; **forêts causales** pour l'hétérogénéité (SUPPOSÉ : Wager et Athey 2018) ; réseaux à deux têtes sous confusion observée (SUPPOSÉ : TARNet, Shalit, Johansson, Sontag 2017 ; DragonNet, Shi, Blei, Veitch 2019). Ils estiment une **courbe dose-réponse** (effet selon la distance ou la densité de canal) ; une « transition de phase » y est une non-linéarité à seuil, testable par un seuil préenregistré.

**C. Invariance (quand on n'a ni intervention ni choc).**
- Prédiction causale invariante (Peters, Bühlmann, Meinshausen 2016, *Journal of the Royal Statistical Society B*, vérifiée (existence)) : on découpe les données en « environnements » (disciplines, pays, décennies, régimes de publication) ; les paramètres dont la relation avec la fertilité reste la même dans tous les environnements sont candidats causaux ; les autres sont des accompagnateurs. Variantes profondes : SUPPOSÉ « Invariant Risk Minimization » (Arjovsky et al. 2019), avec des résultats négatifs connus quand les environnements sont trop semblables (SUPPOSÉ : Rosenfeld et al. 2021).
- Hypothèse à expliciter et à discuter : les mécanismes de confusion changent d'un environnement à l'autre, le mécanisme causal non. En science des sciences, cette hypothèse est fragile (les normes de citation changent par discipline *et* la fertilité aussi) ; l'expert la testerait par un environnement tenu à l'écart, choisi avant l'analyse.
- Découverte de structure (SUPPOSÉ : PC, FCI, NOTEARS) : utile pour proposer des hypothèses, jamais pour conclure ; sort une classe d'équivalence, pas un graphe.

**D. Régression symbolique ou petits traits nommés (les deux pistes de Lazar).** Elles produisent une *loi descriptive* lisible, pas une loi causale ; elles deviennent causales seulement si la loi est ajustée sur des données où la variation est exogène (A ou B) ou validée par invariance (C). Le bon protocole : apprendre la loi sur les données observationnelles, puis la *mettre à l'épreuve* sur les expériences naturelles (prédit-elle le sens et l'ordre de grandeur de l'effet d'un choc qu'elle n'a pas vu ?).

**Antériorités en science des sciences** (observationnelles sauf A et B ; toutes SUPPOSÉ) : Fortunato et al. 2018 (*Science*, revue de champ) ; Uzzi et al. 2013 et Wang, Veugelers, Stephan 2017 (nouveauté et citations) ; Rzhetsky, Foster, Evans 2015 (simulation de choix d'expériences) ; Jaffe, Trajtenberg, Henderson 1993 contre Thompson et Fox-Kean 2005 (un résultat qui change avec le groupe témoin) ; Myers 2020 (élasticité des sujets aux incitations). « Les ponts créent-ils ou accompagnent-ils ? » reste ouvert : aucune étude citée ne randomise la *distance conceptuelle* elle-même.

## (4) Ce qui permettrait de vérifier, hors de Lazar et hors de nous

1. **Vérité terrain plantée** : dans les mondes inventés, un paramètre qui *cause* la fertilité et un qui *l'accompagne* (corrélé par un confondeur commun) ; l'estimateur doit retenir le premier et rejeter le second, taux d'erreur préenregistrés (R5 : cas sain et artefact).
2. **Tests placebo** : date de traitement fictive, résultat antérieur au traitement, niche jumelle non exposée ; un effet trouvé là est un échec consigné.
3. **Recalibrage sur un résultat publié** : retrouver, depuis les données brutes, le *signe* d'un effet connu (Azoulay 2010 ; Borjas-Doran 2012) ; sinon la chaîne n'est pas prête.
4. **Prédiction hors environnement, scellée** : les paramètres déclarés causaux doivent prédire la fertilité dans un environnement (discipline, période) jamais vu, après la coupure temporelle déjà prévue dans le programme ; prédiction chiffrée et signée avant lecture (R1).
5. **Intervention prospective dans l'organisme** : si un paramètre est déclaré causal, le manipuler dans le bisociateur et observer la fertilité sous juge figé indépendant ; c'est la seule vérification qui ne dépend d'aucune hypothèse d'observation.
6. **Réanalyse indépendante** : données brutes, code et préenregistrement empreintés (R6), remis à un analyste extérieur qui applique le plan gelé ; convergence ou divergence consignée.
7. **Bornes de sensibilité publiées** : la force de confusion nécessaire pour annuler l'effet, comparée à celle des confondeurs mesurés.

## Reformulation de la demande

« Déterminer si l'apprentissage profond peut identifier les paramètres qui *créent* la fertilité d'un croisement entre niches, en trois étapes : (i) définir l'estimande (unité, traitement, dose, résultat mesuré indépendamment du traitement, hypothèse d'interférence) et le graphe causal avec confondeurs observés et non observés ; (ii) inventorier les sources d'identification — interventions randomisées dans l'organisme et expériences humaines (Boudreau 2017, Derex-Boyd 2016), expériences naturelles sur données brutes d'affiliation, de conférences, de financement et de localisation (Azoulay 2010, Borjas-Doran 2012, Catalini 2018), invariance entre environnements (Peters-Bühlmann-Meinshausen 2016) — et dire pour chacune quel paramètre elle identifie et à quel prix ; (iii) n'employer l'apprentissage profond que comme estimateur sous identification donnée (apprentissage double orthogonalisé, forêts causales, réseaux à deux têtes, prédiction invariante), avec courbe dose-réponse et seuil préenregistré pour la « transition de phase », les pistes « traits nommés puis ablation » et « régression symbolique » étant éprouvées sur des chocs exogènes qu'elles n'ont pas vus. Livrer, avant tout calcul : tableau estimande × source d'identification × estimateur × hypothèse à défendre ; revue d'antériorité en inférence causale et en science des sciences marquant ce qui est vérifié sur PDF ; protocole de validation en sept points (vérité plantée, placebos, recalibrage, prédiction hors environnement scellée, intervention prospective, réanalyse externe, bornes de sensibilité). »

## Pièce : relecture-fable-reponse-5-v1.md (sha256 77a48dd23c772992…)

# Relecture indépendante de `reponse-conv-audit-question-5-v1.md` (identifier par apprentissage profond les paramètres qui créent la fertilité) — v1

Relecteur : sous-agent neuf (règle R2), n'ayant écrit ni la réponse ni les questions. Modèle : Fable 5.1 (claude-fable-5-1). Date (`date -u`) : Fri Oct 30 17:21:58 UTC 2026 (début de rédaction ; l'horloge du conteneur diffère de celle qui date les fichiers, qui portent 18:10 à 18:15 ; la rédaction a été reprise après une limite d'usage).

Lu : `question-5-causes-v1.md`, `question-1-chapelles-v1.md`, `question-2-niches-v1.md`, `question-3-fertilite-v1.md`, `question-4-apprendre-v1.md`, `reponse-conv-audit-question-5-v1.md` (objet de la relecture, empreinte `a47ba916…e58ae0442`). Non lu : les autres `reponse-*`, les `relecture-*`, `revue-biblio-*`, tout `donnees/`. Aucune dépense, aucune opération git.

Incident de lancement : au démarrage, le fichier à relire était absent du dossier (vérifié par `ls`, `find` sur tout le disque et attente ; règle R11). Il est apparu ensuite ; la relecture porte sur la version d'empreinte ci-dessus.

Niveaux de vérification : **V-session** = page éditeur ou arXiv lue en ligne pendant cette relecture (aucun PDF empreinté, donc rien d'opposable au sens de R7) ; **SUPPOSÉ** = cité de mémoire, à vérifier avant tout usage dans un préenregistrement ou un papier.

## Verdict (une ligne)

Réponse juste dans sa position (observer n'est pas intervenir), tenue en forme et en longueur, mais elle se contredit sur le rôle de la découverte causale observationnelle, passe sous silence le problème de transport entre nos courses et la science réelle, et sa reformulation n'a aucun critère de mort chiffré : à corriger avant usage.

## (a) Les quatre points et la reformulation sont-ils tenus, sans allonger ?

Oui pour la forme : une page, quatre rubriques, une reformulation. Deux réserves de fond :

- Le point (4) « vérification hors de nous » n'est pas hors de nous. Trois des quatre items (prédiction à la course suivante, courses randomisées, tests de mort) sont produits par l'organisme lui-même, avec ses juges figés. Seuls « expériences naturelles indépendantes » et « reproduction sur d'autres domaines et décennies » sont externes. Voir RL5-06.
- La reformulation est une liste de moyens (graphe, trois voies, modèle d'agents, transition, validité), non une demande reformulée « pour répondre précisément à l'exigence » : elle ne dit pas quel paramètre, quelle intervention, quel résultat chiffré tuerait l'hypothèse. Voir RL5-08.

## (b) Affirmations, références, antériorités

### Références citées — état de vérification

| Référence dans la réponse | Attribution | Statut |
|---|---|---|
| Azoulay, Graff Zivin et Wang 2010 (décès de chercheurs étoiles, « Superstar Extinction », *Quarterly Journal of Economics*) | Correcte | SUPPOSÉ (de mémoire ; attribution cohérente avec la littérature) |
| Peters, Bühlmann et Meinshausen 2016 (prédiction causale invariante, *Journal of the Royal Statistical Society B*) | Correcte | SUPPOSÉ |
| Arjovsky 2019 (minimisation du risque invariant, avec Bottou, Gulrajani, Lopez-Paz ; prépublication arXiv, jamais publiée en revue à ma connaissance) | Correcte, mais citer « Arjovsky 2019 » seul est incomplet | SUPPOSÉ |
| Athey et Wager (forêts causales ; Wager et Athey 2018 *Journal of the American Statistical Association* ; Athey, Tibshirani et Wager 2019 *Annals of Statistics* pour les forêts généralisées) | Correcte, année absente | SUPPOSÉ |
| PCMCI de Runge (Runge, Nowack, Kretschmer, Flaxman et Sejdinovic 2019, *Science Advances*) | Correcte | SUPPOSÉ |
| NOTEARS (Zheng, Aragam, Ravikumar et Xing 2018, *NeurIPS*) | Correcte | SUPPOSÉ |
| Dragonnet (Shi, Blei et Veitch 2019, *NeurIPS*), TARNet (Shalit, Johansson et Sontag 2017, *ICML*) | Correcte | SUPPOSÉ |
| Derex et Boyd 2016, *PNAS*, « Partial connectivity of cultural groups promotes cultural diversity and complex problem-solving » | Correcte | V-session (page PubMed Central PMC4801235 ; titre et année confirmés) |
| Mason et Watts (2012, *PNAS*, « Collaborative learning in networks ») | Correcte, année absente | SUPPOSÉ |
| Valeurs E (VanderWeele et Ding 2017, *Annals of Internal Medicine*) | Non attribuée dans la réponse | SUPPOSÉ |
| « Voir » contre « faire » (Pearl) | Correcte | SUPPOSÉ |

Aucune référence inventée ou mal attribuée détectée. Deux imprécisions : « Arjovsky 2019 » sans coauteurs ni statut de prépublication ; Athey-Wager et Mason-Watts sans année.

### Affirmations fausses ou trop fortes

- RL5-01 (**majeur**) — « Non, pas avec des données d'observation seules » puis, trois lignes plus bas, « découverte de structure (PCMCI, NOTEARS) » qui sont précisément des méthodes sur données d'observation seules. La réponse se contredit. La formulation juste : on peut identifier des causes sur données d'observation seules *sous des hypothèses non testables* (suffisance causale, c'est-à-dire aucun facteur caché ; fidélité ; pour NOTEARS, bruit additif et sensibilité à l'échelle des variables) ; ces hypothèses doivent être écrites et, en science des sciences, sont presque toujours fausses (prestige, financement, mode sont des facteurs cachés qui touchent à la fois le contact et la reprise). Le « non » doit devenir « seulement sous hypothèses écrites et attaquées ».
- RL5-02 (**majeur**) — « Apprentissage profond là où il est causal : PCMCI, NOTEARS ». Ni l'un ni l'autre n'est de l'apprentissage profond : PCMCI est une procédure de tests d'indépendance conditionnelle (famille Peter-Clark adaptée aux séries temporelles), NOTEARS une optimisation continue d'un graphe acyclique, linéaire dans sa version de base. Lazar demande explicitement « par apprentissage profond » ; la réponse glisse d'« apprentissage profond » à « méthodes causales » sans le dire. Il faut l'écrire : l'apprentissage profond n'identifie rien par lui-même ; il sert d'estimateur de fonction (réseaux à deux têtes, substitut) à l'intérieur d'un schéma d'identification qui vient d'ailleurs (randomisation, expérience naturelle, hypothèse d'invariance).
- RL5-03 (**modéré**) — NOTEARS cité sans ses faiblesses connues : sur données d'observation il ne peut distinguer que la classe d'équivalence de Markov, et ses bons résultats sur simulations tiennent largement à un artefact d'échelle des variances (« varsortabilité » : Reisach, Seiler et Weichwald 2021, *NeurIPS*, « Beware of the simulated DAG » — V-session, page arXiv 2102.13647). Sur un hypergraphe de citations où les variances croissent avec l'âge et la taille des niches, cet artefact est garanti. « Versions avec interventions » est vague : nommer (par exemple DCDI, Brouillard et al. 2020 — SUPPOSÉ) ou retirer.
- RL5-04 (**modéré**) — « Conférences annulées en 2020 » comme expérience naturelle : en 2020 tout a été annulé en même temps, il n'y a pas de groupe témoin contemporain, seulement une variation de calendrier (conférences tenues en janvier-février contre mars-juin), et la pandémie touche aussi l'issue (reprise) par d'autres canaux. L'expérience naturelle propre existe déjà : Campos, Leon et McQuillin 2018, *Economic Journal*, « Lost in the storm : the academic collaborations that went missing in Hurricane Isaac » (annulation d'une seule conférence de science politique ; V-session, billet et page de résumé).
- RL5-05 (**mineur**) — « Fusions de revues » : événement rare, mal daté, et la revue n'est pas la niche ; peu exploitable. « Financements imposant l'interdisciplinarité » : l'expérience naturelle documentée porte sur l'orientation des sujets par appels ciblés (Myers 2020, *American Economic Journal : Applied Economics*, « The elasticity of science » — SUPPOSÉ), pas sur l'interdisciplinarité imposée.

### Antériorités manquées

- RL5-09 (**majeur**) — Les expériences naturelles de la science des sciences qui portent *exactement* sur les trois leviers que Lazar cite (changement de laboratoire, mise en présence de niches, expérience contrôlée) existent et ne sont pas nommées :
  - chercheurs qui changent de laboratoire : Catalini 2018, *Management Science*, « Microgeography and the direction of inventive activity » (désamiantage du campus de Jussieu, laboratoires déplacés au hasard ; V-session, page éditeur) ;
  - deux communautés mises en présence : Borjas et Doran 2012, *Quarterly Journal of Economics* (effondrement de l'Union soviétique, mathématiciens soviétiques et américains — SUPPOSÉ) ; Moser, Voena et Waldinger 2014, *American Economic Review* (émigrés allemands — SUPPOSÉ) ;
  - canal de communication coupé (le cœur de la question 2) : Iaria, Schwarz et Waldinger 2018, *Quarterly Journal of Economics*, « Frontier knowledge and scientific production : evidence from the collapse of international science » (Première Guerre mondiale — SUPPOSÉ) ; Agrawal et Goldfarb 2008 (réseau Bitnet — SUPPOSÉ) ;
  - mort d'une étoile qui *ouvre* une niche aux entrants, version la plus proche de « niches qui ne se parlent pas » : Azoulay, Fons-Rosen et Graff Zivin 2019, *American Economic Review*, « Does science advance one funeral at a time ? » (SUPPOSÉ) ; la réponse cite seulement le papier de 2010 sur la productivité des collaborateurs ;
  - expérience de terrain randomisée sur la mise en contact de chercheurs : Boudreau, Brady, Ganguli, Gaule, Guinan, Hollenberg et Lakhani 2017, *Review of Economics and Statistics*, « A field experiment on search costs and the formation of scientific collaborations » (V-session, page IDEAS/RePEc) ; Lane, Ganguli, Gaule, Guinan et Lakhani 2021, *Strategic Management Journal*, « Engineering serendipity » (SUPPOSÉ). Ce sont les « Derex et Boyd » de la science réelle ; leur absence est l'oubli le plus coûteux.
- RL5-10 (**modéré**) — Découverte causale sur données scientométriques : je ne connais pas de travail qui applique PCMCI ou NOTEARS à un hypergraphe de citations pour en extraire les causes de la reprise ; les travaux proches sont des simulations étalonnées (Rzhetsky, Foster, Foster et Evans 2015, *PNAS*, déjà cité dans la question 4 ; Lazer et Friedman 2007, *Administrative Science Quarterly*, pour l'effet de la structure du réseau sur l'exploration — SUPPOSÉ) et des travaux de causalité à la Granger. Zone apparemment vierge, donc question, pas trou (règle R8) : vérifier par une recherche dédiée avant de la revendiquer, et se demander pourquoi les économistes de la science, qui connaissent ces outils, ne les ont pas employés (réponse probable : facteurs cachés et non-stationnarité, voir RL5-11).

## (c) Ce qu'un expert aurait dit et qui manque

- RL5-11 (**majeur**) — Transport. L'expert aurait séparé trois questions que la réponse fond en une : (i) ce qui cause la fertilité *dans nos courses* (identifiable par randomisation, mais vrai de nos agents et de nos juges) ; (ii) ce qui cause la fertilité *dans la science réelle* (expériences naturelles) ; (iii) à quelles conditions (i) se transporte vers (ii). La question (iii) est le problème de transportabilité (Pearl et Bareinboim 2011, 2014 — SUPPOSÉ) ; il exige d'écrire quels mécanismes sont supposés communs aux deux mondes et quels nœuds diffèrent (par exemple : nos agents n'ont ni carrière, ni financement, ni prestige). Sans cela, « prédire l'effet d'une intervention jamais vue à la course suivante » prouve une causalité dans le monde de la course, pas dans le monde. La réponse l'effleure (« causalité dans le modèle contre dans le monde ») mais sa reformulation l'oublie.
- RL5-12 (**majeur**) — Manipulabilité. « Les paramètres qui créent la fertilité » mélange deux natures de variables : des variables manipulables (dose de contact, choix de la paire, calendrier) et des attributs non manipulables de la paire (distance de domaine, âge des niches, structure mathématique commune). Pour les secondes, « pas de causalité sans manipulation » (Holland 1986 — SUPPOSÉ) : on ne peut qu'estimer comment l'effet d'une intervention manipulable *varie* selon ces attributs (modération, effets hétérogènes), ce qui est le vrai usage des forêts causales et des réseaux à deux têtes. La réponse cite les bons outils sans dire que c'est pour cela qu'ils servent. Conséquence pratique : la question de Lazar devient « quelles interventions manipulables, et sous quels attributs de la paire, augmentent la fertilité ? », ce qui est testable.
- RL5-13 (**modéré**) — Mesure de l'issue. En littérature réelle, « fertilité » sera mesurée par un proxy (citations, nouveauté à la Uzzi, reprise) ; une cause identifiée sur le proxy n'est pas une cause de la fertilité si le proxy a ses propres causes (effet Matthieu, visibilité des revues). L'expert exigerait un modèle de mesure ou au moins deux proxys indépendants. Lien avec la question 3, non fait.
- RL5-14 (**modéré**) — Survivants et témoins. La question 4 a établi le principe des témoins (paires comparables jamais rencontrées). La réponse 5 l'oublie : tout panel observationnel de « ponts » est un panel de survivants ; le graphe causal du point (1) doit contenir un nœud « sélection » et les expériences naturelles doivent être exploitées sur l'ensemble des paires à risque, pas sur celles qui ont produit un pont.
- RL5-15 (**mineur**) — Outils modernes de différence de différences : avec adoptions échelonnées (déménagements, décès à des dates différentes), l'estimateur à effets fixes classique est biaisé ; nommer les estimateurs robustes (Callaway et Sant'Anna 2021 ; Goodman-Bacon 2021 — SUPPOSÉ). Le contrôle synthétique exige une longue période préalable, ce qui limite son usage à des niches anciennes.
- RL5-16 (**mineur**) — Puissance. Aucun ordre de grandeur du nombre de paires ou de courses nécessaires ; les effets d'expérience naturelle en science des sciences sont de l'ordre de 5 à 10 % sur des milliers d'unités (SUPPOSÉ, ordre de grandeur). Avec quelques dizaines de paires par bras dans nos courses, seule une dose-réponse très forte sera visible.

## (d) Confusions

- Causalité dans le modèle contre dans le monde : la distinction est énoncée (point 1, dernier tiret) mais non appliquée (RL5-11). L'ablation d'un trait dans un réseau entraîné sur les citations dit ce que le réseau utilise, pas ce qui cause la reprise ; la régression symbolique « sur la fonction causale » n'est causale que si la fonction a été apprise sous intervention.
- Invariance : RL5-17 (**modéré**) — Utiliser sous-domaines, décennies et pays comme « environnements » suppose que le mécanisme causal de la reprise est *le même* dans tous et que seuls les facteurs non causaux varient. Or la non-stationnarité du mécanisme (pression à publier, bases de données, taille des équipes) est précisément ce que la science des sciences documente d'une décennie à l'autre ; prendre les décennies comme environnements viole l'hypothèse d'invariance au lieu de l'exploiter. De plus la minimisation du risque invariant a des contre-exemples connus où elle n'est pas meilleure qu'une régression ordinaire (Rosenfeld, Ravikumar et Risteski 2021, *ICLR*, « The risks of invariant risk minimization » — SUPPOSÉ). La prédiction causale invariante de Peters et al. exige en outre que l'issue elle-même ne soit pas intervenue entre environnements, ce qui est douteux quand les pratiques de citation changent.
- Identification : RL5-18 (**modéré**) — Les forêts causales, Dragonnet et l'apprentissage double robuste *estiment* un effet déjà identifié sous « pas de facteur caché » ; ils n'identifient pas « quels paramètres créent ». La réponse les range sous « découverte » par juxtaposition. Les valeurs E quantifient la robustesse à un facteur caché pour un effet donné, pas la validité de la découverte de structure. Le graphe causal du point (1) est le bon point d'entrée, mais il doit être écrit *avant* de choisir l'estimateur, et chaque flèche inconnue doit recevoir une méthode d'identification nommée, sinon aucune.

## (e) La reformulation est-elle testable, avec critère de mort chiffré ?

- RL5-08 (**majeur**) — Non. Le seul critère est « prédire correctement l'effet d'une intervention jamais vue, confirmé par une expérience naturelle indépendante ; sinon corrélat, pas cause ». Il manque : la grandeur prédite (effet de la dose de contact sur le taux de survie aux tests de mort, en points) ; le signe ; la tolérance (intervalle de prédiction préenregistré et seuil au-delà duquel on déclare l'échec) ; la ligne de base à battre (un modèle purement prédictif, sans structure causale, prédit-il aussi bien l'intervention jamais vue ? s'il fait aussi bien, la structure causale n'apporte rien) ; le témoin négatif (une intervention préenregistrée comme sans effet doit donner zéro) ; et la règle d'arrêt (combien de courses, combien d'échecs). « Confirmé par une expérience naturelle » est inopérant tant que l'on n'a pas dit quelle grandeur commune aux deux mondes est comparée (RL5-11).
- Proposition de critère minimal, à chiffrer par Lazar : « l'hypothèse “la dose de contact cause la fertilité” est morte si, sur N courses préenregistrées, l'effet d'une dose jamais testée (par exemple 7 titres après 0, 2, 5, 10) sort de l'intervalle de prédiction à 90 % du modèle causal dans plus de k cas sur N, ou si le modèle purement prédictif entraîné sur les mêmes courses fait aussi bien à ε près ». N, k, ε à fixer avant la première course ; témoin négatif obligatoire (règle R5).
- Transition de phase : RL5-19 (**modéré**) — « Transition de phase par intervention sur la dose comparée à la courbe d'observation » n'est pas testable avec quatre doses (0, 2, 5, 10) : un seuil et une sigmoïde lisse y sont indiscernables. Il faut au moins six à huit doses resserrées autour du seuil supposé, un critère préenregistré de comparaison des deux formes (par exemple rapport de vraisemblance ou facteur de Bayes avec seuil), et une réserve explicite : « transition de phase » au sens de la question 3 n'a pas encore reçu de définition opératoire.

## Tableau des constats

| Code | Gravité | Objet |
|---|---|---|
| RL5-01 | majeur | Contradiction « non sans intervention » contre PCMCI/NOTEARS observationnels ; hypothèses non testables non écrites |
| RL5-02 | majeur | PCMCI et NOTEARS présentés comme apprentissage profond ; glissement sur la question posée |
| RL5-03 | modéré | NOTEARS sans ses limites (classe d'équivalence, varsortabilité) ; « versions avec interventions » vague |
| RL5-04 | modéré | Conférences annulées en 2020 : pas de témoin ; Campos, Leon et McQuillin 2018 est l'expérience propre |
| RL5-05 | mineur | Fusions de revues et financements interdisciplinaires : leviers mal choisis |
| RL5-06 | modéré | Point (4) : trois vérifications sur quatre sont internes à l'organisme |
| RL5-08 | majeur | Reformulation sans critère de mort chiffré, sans ligne de base, sans témoin négatif |
| RL5-09 | majeur | Expériences naturelles et de terrain exactement sur les leviers de Lazar non citées (Catalini, Borjas-Doran, Iaria et al., Azoulay et al. 2019, Boudreau et al.) |
| RL5-10 | modéré | Découverte causale sur scientométrie : zone apparemment vierge à traiter comme question (R8) |
| RL5-11 | majeur | Transport entre nos courses et la science réelle absent de la reformulation |
| RL5-12 | majeur | Manipulable contre non manipulable ; la question devient une question de modération |
| RL5-13 | modéré | Issue mesurée par proxy ; cause du proxy ≠ cause de la fertilité |
| RL5-14 | modéré | Survivants et témoins (question 4) oubliés dans le graphe causal |
| RL5-15 | mineur | Différence de différences échelonnée : estimateurs robustes à nommer |
| RL5-16 | mineur | Aucun ordre de grandeur de puissance |
| RL5-17 | modéré | Décennies comme environnements : viole l'invariance ; limites connues de la minimisation du risque invariant |
| RL5-18 | modéré | Estimation d'effet confondue avec identification et découverte |
| RL5-19 | modéré | Transition de phase indiscernable avec quatre doses |

(Le code RL5-07 n'est pas attribué.)

## Ce que je garderais tel quel

La position d'ouverture (voir contre faire) ; l'idée de prendre les courses comme laboratoire randomisé avec dose de contact ; la liste des trois voies ; l'exigence d'effets signés et chiffrés avec placebo et contrôle négatif ; Derex et Boyd, Mason et Watts comme modèles d'expérience contrôlée. Le squelette est bon ; ce sont les hypothèses d'identification, le transport et le critère de mort qui manquent.

## Pièce : reponse-conv-audit-question-6-v1.md (sha256 afdb9f9dbf9ed8a8…)

# Réponse de conv-audit à la question 6 (identification des causes de la fertilité par apprentissage profond) — v1

conv-audit, 30 octobre 2026 (Fable 5.1, 21:36–21:45 heure de Paris), transcrite sans modification de fond. Références de mémoire : SUPPOSÉ.

**Position.** L'identification n'est pas une propriété de l'algorithme mais du couple données + hypothèses. Sans hypothèse ni supervision, le démêlage non supervisé est impossible (Locatello et collègues 2019) et l'analyse en composantes indépendantes non linéaire n'est pas identifiable (Hyvärinen et Pajunen 1999) : un réseau non supervisé sur des citations trouve des facteurs (taille, âge, prestige, langue), pas des causes, et pas les mêmes à la graine suivante. Mais les mêmes théorèmes disent quelles hypothèses rendent l'identification possible, et plusieurs sont offertes par nos données : ordre temporel des citations, multiplicité des environnements (sous-domaines, décennies, pays), décalages parcimonieux de mécanismes, bruit non gaussien. Sous ces hypothèses, l'analyse en composantes indépendantes avec variable auxiliaire (Hyvärinen et Morioka 2016 ; Khemakhem 2020) et l'apprentissage de représentations causales temporelles (Lippe 2022 ; Schölkopf 2021) identifient — pas « à lui seul » : avec l'hypothèse, écrite et testable.

## (1) Ce qu'un expert ferait, et que Lazar ne demande pas
Table des théorèmes d'identifiabilité (hypothèse exacte ; ce qui est identifié : latentes, structure, paramètres) ; vérification hypothèse par hypothèse sur nos données ; épreuve de chaque méthode sur des mondes inventés à causes plantées (notre générateur à vérité plantée ; score de recouvrement des facteurs vrais, stabilité entre graines) ; traque des artefacts (ordre des variances, Reisach 2021 ; échelle ; popularité) ; fermeture par une intervention jamais vue (dose de contact) réalisée dans la course suivante ; transport écrit d'avance et éprouvé sur les expériences naturelles.

## (2) Données brutes
Mondes inventés à causes plantées ; OpenAlex découpé en environnements naturels (sous-domaine, décennie, pays, revue), événements ordonnés dans le temps ; nos courses (affectations randomisées, doses, verdicts, tests de mort) ; expériences naturelles (rencontres randomisées de Boudreau 2017, mobilité, décès, financements).

## (3) Méthodes et outils
Analyse en composantes indépendantes non linéaire avec variable auxiliaire ; apprentissage de représentations causales temporelles ; découverte de structure sous non-gaussianité (LiNGAM) et sur séries (PCMCI) ; prédiction causale invariante ; score de recouvrement sur mondes inventés ; estimation d'effets sous structure identifiée (forêts causales, réseaux à deux têtes) ; prédiction d'intervention dans la course.

## (4) Vérification hors de nous
Les théorèmes (publics) ; les mondes inventés et les bancs publics de démêlage ; la course suivante qui réalise l'intervention prédite ; les expériences naturelles indépendantes.

## Reformulation
« Déterminer sous quelles hypothèses, satisfaites par nos données, l'apprentissage profond, non supervisé compris, identifie les paramètres qui créent la fertilité. 1. Table des théorèmes d'identifiabilité. 2. Vérification de chaque hypothèse sur les données scientométriques et sur nos courses. 3. Épreuve de chaque méthode sur des mondes inventés à causes plantées (recouvrement, stabilité, artefacts). 4. Sur données réelles : identification sous hypothèses vérifiées, puis prédiction de l'effet d'une intervention jamais vue, réalisée dans la course suivante ; transport éprouvé sur les expériences naturelles. 5. Critère de mort : recouvrement sous un seuil fixé d'avance, ou échec de la prédiction d'intervention ; alors la méthode estime, elle n'identifie pas. »
