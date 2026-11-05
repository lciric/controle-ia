# Antériorité par énoncé — lectures sur PDF de niveau 2 (lots 1 à 3) — v1

Compilation par un compilateur neuf, sans lecture de PDF (format de document portable) : chaque verdict est celui d'un lecteur neuf, avec ses pages (R7). « Libre » ou « non fait » veut dire « non trouvé dans les sources lues », jamais « trou du champ » (R8).

## En tête : ce qu'il faut voir d'abord

**1. Aucun verdict « occupe en entier » dans les 24 rapports.**

**2. Pièces listées comme « revendiquées » par les décisions de Lazar et trouvées déjà publiées, en tout ou en partie :**

- **HC1, « le verdict lu par probabilité du jeton » (N-005, l. 52) — publié comme technique.** Juges : Panickssery et al. 2404.13076 p. 2 et Wataoka et al. 2410.21819 p. 4 (lot2-C1a : « la lecture du verdict d'un juge par la probabilité des jetons est occupée » ; « Il ne peut pas être revendiqué seul ») ; moniteurs de contrôle : 2411.03336 p. 25 (lot2-A4 : « pas revendicable comme technique ; seul son emploi pour estimer la loi de déférence l'est »), 2602.20628 p. 6 (lot2-A4), 2410.21514 p. 26, 67 (lot2-A3), 2411.17693 p. 19, 21 (lot3-Aa : « cet instrument seul n'est pas revendicable »), 2608.16190 p. 3 (lot2-B1, « méthode voisine ») ; assistants et modèles qui répondent : PARROT 2511.17220 p. 4, Sicilia et al. 2410.14746 p. 3, 2606.14037 p. 14 (lot1-HC1-voisins), 2601.13433 p. 1-6 (lot2-C2a) ; suffixes optimisés contre des juges : 2402.14016 p. 3, 5, 6 (lot2-C2b) ; sondes au niveau du jeton de note d'un juge : 2608.25869 p. 6 (lot3-Ca) ; recommandée comme pratique : 2606.07612 p. 25 (lot2-A2b).
- **HC1, « la régression sur plusieurs intensités par famille » (N-005, l. 51) — intensités graduées publiées, sans régression ni gain.** 2606.14037 p. 12-14 (trois intensités, deux familles) et Sicilia et al. p. 4 (deux intensités et une nulle) (lot1-HC1-voisins) ; Koo et al. 2309.17012 p. 8, 14, 15 (intensité d'une fausse majorité) (lot2-C1a) ; 2601.13433 p. 1-6 (quatre niveaux d'autorité, réponse monotone) (lot2-C2a) ; 2402.14016 (un à quatre mots optimisés) et 2504.18333 (échelle de sophistication) (lot2-C2b) ; 2410.21514 p. 7 (trois niveaux d'agressivité, sur humains) (lot2-A3). La régression elle-même n'est trouvée dans aucune source.
- **HC1 et porte GC, « la destination libre ĉ, testée contre la cible de l'attaquant et contre la moyenne du corpus, par famille, dans des moniteurs de contrôle » (N-005, l. 50 et 63) — « partiellement occupée » selon lot1-GC-reseaux, combinaison libre.** Attracteur libre estimé par moindres carrés, hors attaque : Probine et al. 2606.18276 p. 5-7, 15-17 ; forme à destination imposée, en cadre adverse : Abedini et al. 2603.15809 p. 10, 48 (lot1-GC-reseaux : « Verdict pour la porte GC : partiellement occupée ») ; tests catégoriels de destination : PARROT p. 12 (lot1-HC1-voisins), 2605.23970 p. 4, 8 (lot2-C2a) ; question « la destination suit-elle la cible ? » sur un juge de qualité, hors contrôle : 2608.25869 p. 2, 6, 7 (lot3-Ca, lecture « voisin » retenue ; contre-indice faible pour ĉ = v*). Porte GC non déclenchée selon lot1-GC-reseaux et lot3-Ca.
- **HC5, « la matrice de transfert des attaques de corruption » (N-006) — occupée en partie entre sondes seulement.** 2609.36490 p. 3, 4, 6, 8 (lot3-Cc : « occupe en partie » la matrice entre sondes ; « voisin » si la matrice vise juges et sondes) ; hésitation pour MonitoringBench 2605.09684 p. 31 (lot3-Cd) ; transfert d'injections entre moniteurs, 2510.09462 (lot2-A4, « touche l'idée »).
- **HC5, « le quorum hétérogène en type d'accès, juges génératifs et sondes internes » (N-006) — occupé en partie au sens faible.** 2603.13791 p. 7-9, 12, 41 (lot3-Cc : trois juges incités et une sonde sur un encodeur séparé, jamais l'agent ; « la lecture dure est « occupe en partie » ») ; version textuelle (actions et chaîne de pensée) : 2505.23575 p. 6 (lot2-C1b).
- **H2, énoncé retenu (N-007) — occupé en partie, jamais en entier.** SafeDream 2604.16824 p. 4, 5, 14, 17 (lot3-Ab, « occupe en partie » en lecture dure : scores tirés des états internes, cumulés par somme de Page, base bénigne) ; quatre sources du lot 1 en occupent des morceaux (lot1-H2-voisins : Kulkarni 2604.28129, Kaur, Padhi et al. 2604.19775, FIPER 2510.09459 « occupé pour le seuil » du calibrage sans exemple d'échec, Yueh-Han et al. 2506.10949) ; 2605.31593 et 2607.02514 « en partie, en boîte noire » (lot2-B1). La conjonction de l'énoncé reste libre.
- **T (N-003)** : 2607.11751 (lot3-Ab) occupe en partie la seule moitié négative, **qui n'est pas revendiquée** ; « voisin » pour les quatre pièces revendiquées.
- **L (N-004)** : l'énoncé adverse complet sur scores de sondes, revendiqué, n'est occupé par aucune source ; 2608.02698 p. 5 (lot2-B1) l'occupe « en partie, en boîte noire et par des outils classiques » (puissance de tout test bornée par une fonction de la divergence totale, sous décomposition additive ; « l'auteur ne revendique pas les inégalités »).

**3. Autres verdicts « occupe en partie »** (énoncés sans pièce revendiquée dans les décisions consultées) : H6 par 2412.01784 (lot3-Ac, lecture A) ; H7, mécanisme, par 2609.36490 (lot3-Cc) ; H5 par 2605.15377 (thèse qualitative en boîte noire, lot2-B1) et par 2609.36490 (instrument, lot3-Cc) ; HC3 par 2508.19461 (composante 1, lot3-Ca) et 2603.12277 (versant stylistique sur le modèle attaqué, lot2-C3a) ; H8 par 2605.27958 (lot2-A2b) ; H3, pendant boîte noire, par 2607.07368 (lot2-B1).

**4. Décisions consultées** : N-003/N-004, N-005/N-006, N-007/N-008 et P-008. La décision N-013 (`docs/decisions/decision-N-013-v1.md`), apparue pendant la compilation (17 h 49, temps universel coordonné), n'a pas été lue.

## Méthode et échelle

- Verdicts compilés sur l'échelle de la consigne : « occupe en entier », « occupe en partie », « voisin », « contre-indice », « ne touche pas » ; le terme du lecteur est cité entre guillemets quand il diffère.
- Lots 1 et 2 : les lecteurs notent souvent par composante (« occupé », « partiellement », « libre dans cette source »). « Occupe partiellement », « occupé pour … », « partielle » sont rangés « occupe en partie » ; « touché(e) partiellement » ou « touché(e) en partie » sans occupation (par exemple lot2-A1 : « touchée partiellement, jamais occupée ») sont rangés « voisin » ; « contre-indice » quand le lecteur l'écrit.
- La ligne « autres sources » regroupe, par énoncé, les sources que le lecteur ne range ni comme occupantes ni comme voisines : il écrit « ne touche pas », « non occupé » sans décrire de contact, ou ne traite pas l'énoncé.
- Après chaque table, trois lignes au plus : ce qui reste revendicable, puis les désaccords entre lecteurs ou avec la recherche affirmative.
- Rapports : « lot1-X » = `rapport-X-v1.md` ; « lot2-X » et « lot3-X » = `rapport-lot2-X-….md` et `rapport-lot3-X-….md` dans `docs/sources/lecture-pdf-niveau2/`.

## H1 — gain de la boîte blanche sur la boîte noire, sabotage diffus, à faux positifs égaux

| source | verdict du lecteur | composantes faites | composantes non faites | pages | rapport |
|---|---|---|---|---|---|
| 2606.17478v1 (STATEWITNESS) | voisin ; **contre-indice partiel** | comparaison à 1 % et 5 % de faux positifs, deux cibles, sept jeux dont une sous-performance sur instruction ; à 1 %, la boîte noire devance (0,502 contre 0,379 et 0,326) | sabotage diffus, tâches floues, agrégation sur trajectoire, faux positifs sur épisodes honnêtes de la même tâche, sonde à agrégation robuste, intervalles ; contre-indice affaibli (calibrage hors tâche, auto-évaluation chez Gemma, agrégé GPT-OSS 0,430 contre 0,352) | 7, 8, 16, 24, 28, 32 | lot3-Ac |
| 2509.21344v2 | **contre-indice (portée)** | de hautes performances de sondes viennent des positions qui portent l'évidence textuelle ; sans elle, la sonde tombe au hasard (sous-performance) ou presque (biais, 0,57) | aucun moniteur boîte noire mesuré ; aucune comparaison à faux positifs égaux ; gain relatif ni mesuré ni exclu | 3, 8, 9 | lot3-Cb |
| 2604.14865v1 | **contre-indice faible** | le classifieur textuel bat la sonde à faibles faux positifs dans le domaine générique (74,00 contre 66,50) ; égalité en biologie, sonde devant en chimie | capacités inégales des deux côtés ; pas d'agent | 7, 8 | lot3-Ab |
| 2610.04575v1 | voisin ; **contre-indice faible** | lecture de l'agent avant l'action ; aucun gain de la sonde sur l'observable à 5 % sur AgentDojo (−0,0263 [−0,0789 ; 0]) ; gains hors agents (+0,2649) | sabotage diffus ; garantie | 2, 4, 5, 7, 8 | lot3-Aa |
| 2512.07810v1 | voisin (« le voisin le plus direct de H1, sans l'occuper ») | énoncé général blanc > noir pour la sous-performance, qualitatif, sur réponses nettes ; contre-résultat : les sondes manquent Oak (sabotage étroit agentique) | mesure à faux positifs égaux ; tâches ouvertes | 17 | lot2-A3 |
| 2506.10805v4 | voisin (« touchée partiellement », forme de la comparaison) | sondes contre moniteurs boîte noire, y compris à 1 % ; résultat défavorable aux sondes (43 % contre 55 %) | sabotage, trajectoire ; objet « enjeux élevés » | 10 | lot2-A1 |
| 2507.12691v3 | voisin (« touchée partiellement ») | métrique du gain blanc-sur-noir sur réponses isolées ; gain négatif sur le code à porte dérobée | sabotage étalé, tâches floues | 8, 9 | lot2-A1 |
| 2602.14161v2 | voisin (« touchée partiellement ») | blanc contre noir à faux positifs bénins appariés, sous changement de distribution | entrées lues au dernier jeton, pas des actions d'agent ni un sabotage | 4 | lot2-A1 |
| 2504.20271v1 | voisin (« touchée marginalement ») | sondes contre sortie promptée du même modèle, en aire sous la courbe | faux positifs fixés ; sabotage | — | lot2-A1 |
| 2504.10374v1 ; 2605.26047v2 | voisin (menace pour H1 et H2) | découper l'attaque en étapes rend chaque action moins suspecte (boîte noire) | activations | 1, 5 ; 22 | lot2-A1 |
| 2411.03336v2 | voisin (« au niveau de l'idée seulement ») | sondes dans un protocole de contrôle, exemple fictif | mesure, faux positifs | 28 | lot2-A4 |
| 2601.11516v4 | voisin (« touchée, non occupée ») | sondes comparables aux classifieurs Gemini Flash et Pro, sur entrées, erreur pondérée | agent, faux positifs égaux | 3 | lot2-A2a |
| 2605.18918v1 (ESLD) | voisin (« non occupée, mais voisine la plus nette des quatre ») | sonde sur les activations d'un garde contre le verdict généré du même garde : +16,4 points ; « À citer comme antériorité de « sonde contre juge sur le même modèle, hors attaque » » | pas à faux positifs égaux ; injections explicites ; moniteur lu, pas l'agent | 5, 9 | lot2-C3a |
| 2505.06311v2 ; 2604.22888v1 | voisin | états internes contre boîte noire sur ordres explicites (exactitude) ; F1 à seuil non donné | faux positifs fixés ; agent | 6 ; 6 | lot2-C3a |
| 2603.13791v1 | voisin | sonde-lecteur 0,901 contre juge boîte noire 0,837 ; à entrée égale, gain propre +0,032 (calcul) | activations de l'agent (lecteur séparé) ; sabotage diffus | 1, 10, 38 | lot3-Cc |
| 2602.22303v1 | voisin | un signal d'origine interne appris domine des moniteurs boîte noire à 5 % et 1 % | activations ou sondes ; sabotage diffus | 8, 10, 11, 16 | lot3-Be |
| 2607.13087v1 | voisin | prémisse affirmée (lire les activations aide à inférer l'intention) ; « plus spéculatif » = opinion, pas contre-indice | toute mesure | 5, 20, 25 | lot3-Ac |
| 2608.02698v1 | voisin (« conception seulement ») | sonde comme oracle, valeurs fictives | toute mesure | 7 | lot2-B1 |
| 2508.19461v1 ; MonitoringBench 2605.09684v1 ; SLEIGHT-Bench 2605.16626v2 | voisin de contexte | comparateurs et environnements boîte noire (vrais positifs à 1 % de faux positifs) | activations ; trajectoires d'agent réel (bancs synthétiques ou réécrits) | 9 ; 29, 61 ; 3, 9 | lot3-Ca ; lot3-Cd |
| 2604.16824v1 (SafeDream) | voisin faible | comparaison non appariée | — | 7 | lot3-Ab |
| autres sources | ne touche pas | — | — | — | lot2-A2a (2602.15515), lot2-A2b (2509.26238, 2605.27958, 2502.03407 : « l'écart blanc/noir n'apparaît pas », p. 10 ; 2511.00554), lot2-A3 (2604.16286, 2511.09904, 2410.21514), lot2-A4 (2510.09462, 2504.05259), lot2-C1a, lot2-C1b (2503.11926, 2302.12173, 2505.23575), lot2-C2a, lot2-C2b (2603.29403), lot2-C3a (2603.12277), lot2-C3b, lot3-Aa (2411.17693), lot3-Ac (2412.01784), lot3-Be (2608.19161), lot3-Ca (2608.25869), lot3-Cb (2508.05625), lot3-Cc (2609.36490), lot3-Cd (2607.06596) |

- **Reste revendicable** : la mesure du gain des activations sur la boîte noire, à faux positifs égaux, sur du sabotage diffus de tâches floues, n'est faite dans aucune source lue.
- **Contre-indices à garder** : 2606.17478 (partiel), 2509.21344 (portée), 2604.14865 et 2610.04575 (faibles).
- **Désaccords** : lot3-Ac ramène « voisin fort ; contre-indice » (recherche affirmative) à « voisin ; contre-indice partiel » pour 2606.17478 ; lot3-Aa ramène « occupe en partie » à « voisin » pour 2610.04575.

## H2 — accumulation additive toujours valide de scores de sondes de l'agent qui agit, sous un moniteur par action à 1 % (énoncé N-007)

| source | verdict du lecteur | composantes faites | composantes non faites | pages | rapport |
|---|---|---|---|---|---|
| 2604.16824v1 (SafeDream) | **occupe en partie** (lecture dure retenue ; lecture « voisin fort » possible) | scores tirés des états internes d'un modèle, cumulés de façon additive par somme de Page, base estimée sur le bénin ; signal d'un tour isolé faible (0,517) | garantie toujours valide ; calibrage sans exemple d'attaque ; sondes de l'agent qui agit (le modèle lu est la victime d'un utilisateur) ; seuil par action à 1 % ; rappel selon l'horizon ; sabotage | 4, 5, 14, 17 | lot3-Ab |
| 2604.28129v1 (Kulkarni) | **occupe en partie** (« occupe partiellement quatre composantes ») | activations du modèle en conversation ; somme additive (dérive cumulée) ; tours niables un à un ; détection précoce croissante avec la durée du pivot | toujours valide ; seuil par action à 1 % ; calibrage sans exemple ; contexte privé ; contre-indice : les conversations réelles longues sont plus dures | 3, 4, 5, 7, 11, 12, 15, 19, 20, 21 | lot1-H2-voisins |
| 2604.19775v2 (Kaur, Padhi et al.) | **occupe en partie** (« occupe partiellement deux composantes ») | sondes linéaires sur les activations de l'agent qui agit (succès ou échec d'un pas) ; pensées ReAct visibles | accumulation ; toujours valide ; seuil 1 % ; horizon ; sabotage | 3, 4, 7 | lot1-H2-voisins |
| 2510.09459v2 (FIPER) | **occupe en partie** (« occupé pour le seuil » ; « partiellement » ailleurs) | calibrage du seuil sur épisodes réussis seuls ; somme sur fenêtre glissante ; borne de fausse alarme uniforme sur un horizon fini, par prédiction conforme | processus e ou martingale ; seuil par action à 1 % ; rappel selon l'horizon ; contexte privé ; contre-indice : somme cumulée confondue avec la longueur | 2, 6, 7, 9, 10, 20, 21 | lot1-H2-voisins |
| 2506.10949v2 (Yueh-Han et al.) | **occupe en partie** (« le régime « chaque pas bénin » ») | régime « chaque sous-tâche bénigne », moniteur séquentiel textuel meilleur que le moniteur pas à pas | sondes ; seuil 1 % ; garantie | 1, 6 | lot1-H2-voisins |
| 2605.31593v1 ; 2607.02514v2 | **occupe en partie, en boîte noire** | somme des k plus forts scores à l'échelle des comptes, signalement croissant avec l'activité cumulée ; seuils calibrés sur exécutions honnêtes seules | sondes ; garantie toujours valide ; précaution : attaques graduelles réussies concentrées sur une ou deux demandes de fusion | 6, 9 ; 4, 7, 30, 31 | lot2-B1 |
| 2605.26047v2 | **contre-indice** (« non occupée ; résultat contraire à verser au dossier ») | en boîte noire, l'audit après k coups baisse la sécurité pour tout k > 1 quand le moniteur voit déjà l'historique | sondes ; garantie | 4, 24 | lot2-A1 |
| 2509.21344v2 | **contre-indice** sur la clause « contexte privé compris » ; voisin pour le seuil à 1 % calibré sans exemple | lire le contexte privé donne à la sonde le texte qui dit le comportement ; rappel à 1 % de 0,00 à 0,04 après retrait de l'évidence | accumulation ; garantie ; horizon ; trajectoire agentique | 4, 5, 6, 9 | lot3-Cb |
| 2607.06596v3 | voisin ; **contre-indice conditionnel** | un seuil calibré sur une famille donne de 0 à 94 % de faux positifs réels pour 1 % visé sur une autre ; sans objet si calibrage et déploiement portent sur le même agent (1,3 % pour 1 %) | sondes ; accumulation ; horizon | 12, 13, 21 | lot3-Cd |
| 2610.04575v1 | voisin ; **contre-indice de portée limitée** (tenue du calibrage) | lecture de l'agent avant l'action ; seuil par statistique d'ordre sur unités négatives seules ; seuil certifié non tenu en test (18,67 % pour 10 %) | accumulation additive ; garantie toujours valide ; moniteur par action à 1 % ; rappel selon l'horizon ; calibrage sans exemple d'attaque | 1, 3, 5, 6, 7, 8, 10 | lot3-Aa |
| 2602.22303v1 | voisin ; contre-indice faible examiné et **non retenu** | signal interne élevé tout au long de la trajectoire ; « au moins un appel » ; longueur sans lien avec la détection (facteurs de Bayes inférieurs à 0,2), mais longueur ≠ horizon du sabotage | sondes ; accumulation toujours valide ; seuil à 1 % ; calibrage sans sabotage | 31, 32 | lot3-Be |
| 2411.17693v1 | voisin, avec réserve | squelette séquentiel boîte noire (crédence bayésienne, additive en log-cotes, gain avec la longueur) ; erreurs qui s'accumulent et décalibrent | sondes ; garantie ; calibrage sans sabotage ; seuil 1 % | 2, 6, 7, 9, 19 | lot3-Aa |
| 2410.21514 (Benton et al.) | voisin (« le plus proche de H2 parmi les sept, sans l'occuper ») | interactions nécessaires pour attraper ; audit 1 % par commit ; attaquant qui répartit le bogue | sondes ; test toujours valide ; seuil par action ; rappel selon l'horizon | 8, 17, 26, 49 | lot2-A3 |
| 2504.10374v1 (Ctrl-Z) ; 2605.06455v2 (PrefixGuard) ; 2005.07821v1 | voisin (« touchée partiellement ») | audit après trois coups, seuils pris sur l'honnête ; alerte au premier franchissement calibrée sur trajectoires réussies (conforme, 10 %) ; statistique cumulée par pas sans exemple d'attaque | sondes ; garantie toujours valide ; sabotage par l'agent | 7, 19, 22, 33 ; 3, 6 ; 2, 5 | lot2-A1 |
| 2505.23575v3 (Arnav et al.) | voisin (« touché en partie, un élément ») | seuil par réponse calibré à 1 % sur réponses bénignes | conjonction de l'énoncé | 4, 15 | lot2-C1b |
| 2608.02657v2 ; 2606.22864v1 | voisin (contacts) | sonde à chaque tour sur les états de l'agent qui agit, seuil fixe 0,5 ; seuil par étape à 1 % sur données propres (résultat déclaré non interprétable) | accumulation ; garantie ; calibrage sans exemple | 4, 7 ; 8, 12, 16 | lot2-C3b |
| 2403.17710v5 | voisin (contact) | seuil calibré sur 100 exemples propres pour ≤ 1 % (3,4 % observés), texte par texte | cumul | 12 | lot2-C2b |
| 2505.06311v2 ; 2603.12277v6 ; 2605.18918v1 | voisin (« voisinages faibles ») | plusieurs instructions dans un document ; conviction progressive dans le modèle attaqué ; contrôles séquentiels indépendants | sondes de l'agent qui agit ; accumulation toujours valide | 15 ; 28 ; 8 | lot2-C3a |
| 2607.13087v1 | voisin | problème nommé (menaces diffuses), détection sur deux couches, incrimination par signalements répétés | moniteur par action à 1 % ; accumulation ; lecture toujours valide ; calibrage sans sabotage ; sondes | 8, 9, 14, 20, 33 | lot3-Ac |
| MonitoringBench 2605.09684v1 ; SLEIGHT-Bench 2605.16626v2 | voisin | seuil par action à 1 % sur actions honnêtes mises en commun, agrégé par le max (6,7 à 17,4 % de faux positifs par trajectoire) ; seuil par session sensible à la source de calibration (10 à 20 points) | accumulation ; sondes ; horizon | 4, 7, 17, 25 ; 6, 7, 9 | lot3-Cd |
| 2607.11751v1 ; 2604.14865v1 | voisin ; voisin faible | calibrage sur bénin seul (moniteur à une classe : 6 % à 1 %) ; moyenne mobile dans un échange | accumulation sur trajectoire ; garantie | 11, 13 ; 23 | lot3-Ab |
| 2608.02698v1 ; 2607.07368v1 | voisin (idée proposée non réalisée ; précaution) | test séquentiel entre sessions et calibrage conforme proposés ; scores par commit positivement dépendants | toute mesure | 4, 9 ; 45, 65 | lot2-B1 |
| 2508.19461v1 ; 2603.13791v1 | voisin de contexte ; voisin faible | moniteur séquentiel boîte noire déjà acquis ; échec par dilution sur longue trajectoire | seuil par action ; accumulation | 9, 10 ; 33 | lot3-Ca ; lot3-Cc |
| 2606.17478v1 | ne touche pas (voisin lointain pour le seul calibrage) | leçon : calibrer sur un corpus bénin hors tâche fausse les sondes, ce qui plaide pour des épisodes honnêtes de la même tâche | — | 7, 19, 30 | lot3-Ac |
| autres sources | ne touche pas | — | — | — | lot2-A1 (2506.10805, 2507.12691), lot2-A2a, lot2-A2b, lot2-A3 (2604.16286, 2511.09904, 2512.07810), lot2-A4, lot2-C1a, lot2-C2a, lot2-C2b (2504.18333), lot3-Ac (2412.01784), lot3-Be (2608.19161), lot3-Ca (2608.25869), lot3-Cb (2508.05625), lot3-Cc (2609.36490) |

- **Reste revendicable** : la conjonction de l'énoncé N-007 — accumulation additive toujours valide de scores de sondes de l'agent qui agit, actions sous un moniteur par action à 1 %, rappel croissant avec l'horizon, contexte privé, calibrage sur épisodes honnêtes sans exemple de sabotage — n'est occupée par aucune source ; chacune de ses composantes est approchée ailleurs.
- **Désaccords** : lot3-Ab relève SafeDream de « voisin fort » (recherche affirmative) à « occupe en partie » ; lot3-Aa ramène 2610.04575 et 2411.17693 de « occupe en partie » à « voisin ».

## L — lemme d'additivité, énoncé adverse (N-004)

| source | verdict du lecteur | composantes faites | composantes non faites | pages | rapport |
|---|---|---|---|---|---|
| 2608.02698v1 | **occupe en partie** (« En partie, en boîte noire et par des outils classiques ») | puissance de tout test bornée par une fonction de la divergence totale, sous décomposition additive ; borne supérieure seulement ; l'auteur ne revendique pas les inégalités | énoncé adverse sur scores de sondes ; aucun résultat mesuré (valeurs fictives) | 5 | lot2-B1 |
| 2208.07610v2 | voisin (outils) | garantie toujours valide par martingale positive (Ville) ; critère GROW à la place de la puissance ; rapport de vraisemblance invariant optimal | puissance de la statistique terminale fonction de (B, n₀, α) seulement ; effet du calendrier ; prix chiffré de la garantie (« ce chiffrage serait une contribution du programme ») ; budget total ; observations seulement indépendantes et de même loi | 2, 3, 6, 7, 8, 26 | lot1-lemme |
| 2601.20022v2 | voisin | délai optimal Θ(γ) contre un adversaire couvert stationnaire ; dommage total borné ; optimalité de Page au sens de Lorden ; « détecteur de rupture nécessaire avant un seuil de dommage » : partiel | budget total ; adversaire non stationnaire ou adaptatif ; garantie en probabilité ou toujours valide ; détecteurs e | 1, 2, 4, 8-12 | lot1-lemme |
| 2607.11751v1 | voisin | agrégation « alarme si l'une » : 1 − (1 − α)^K sous indépendance (Proposition 2) ; selon le lecteur, la borne de l'union ne montre pas l'effondrement du max (L2) | énoncé additif ; garantie | 10, 16 | lot3-Ab |
| 2610.04575v1 ; 2411.17693v1 | voisin | relation classique ligne → unité (illustration non probante pour L2) ; taux de mauvaise conduite optimisé contre la défense, attaquant sans mémoire | énoncé adverse ; budget total | 2-4, 11 ; 5, 7, 21, 42 | lot3-Aa |
| MonitoringBench 2605.09684v1 ; SLEIGHT-Bench 2605.16626v2 | voisin | tactiques de répartition (attaque étalée sur plus de trois fichiers ou pas) et moniteur pas à pas au max ; un découpage entre deux sessions, paire notée par le max, seconde moitié notée bien plus bas (sens compatible avec L2) | statistique additive ; budget ; sondes ; aucun chiffre par niveau de répartition | 4, 29, 42, 45, 58 ; 5 | lot3-Cd |
| 2604.16824v1 (SafeDream) ; 2604.14865v1 | voisin faible | détection avant le dommage par Page, arbitrage délai / fausses alarmes ; maximum contre moyenne de K fenêtres | énoncé adverse | 5, 8 ; 22 | lot3-Ab |
| 2510.07192v1 ; 2602.20628v2 | voisin (analogie ; heuristique) | nombre absolu de documents, répartition non neutre ; bits de collusion additifs côté attaquant | énoncé statistique | 6, 23 ; 30 | lot2-A3 ; lot2-A4 |
| 2607.07368v1 ; 2607.13087v1 | voisin (précaution ; menace nommée) | scores par commit positivement dépendants ; attaque étalée dans l'espace et le temps | énoncé statistique | 45, 65 ; 4, 8 | lot2-B1 ; lot3-Ac |
| autres sources | ne touche pas | — | — | — | lot2-A1 (« L, HC1 : non touchés »), lot2-A2a, lot2-A2b, lot2-C1a, lot2-C1b, lot2-C2a, lot2-C2b, lot2-C3a, lot2-C3b, lot3-Ac (2606.17478, 2412.01784), lot3-Be, lot3-Ca, lot3-Cb, lot3-Cc, lot3-Cd (2607.06596) |

- **Reste revendicable** : l'énoncé adverse complet (invariances exactes, borne toujours valide, coût du report, détection à temps, validité sous dépendance) appliqué aux scores de sondes ; les outils sont publiés et à citer comme classiques.
- **Désaccords** : lot3-Aa ramène 2610.04575 et 2411.17693 (« occupe en partie » pour « 3 » dans la recherche affirmative) à « voisin » ; lot3-Ab abaisse SafeDream à « voisin faible » pour L.

## T — théorème négatif (N-003)

| source | verdict du lecteur | composantes faites | composantes non faites | pages | rapport |
|---|---|---|---|---|---|
| 2607.11751v1 | **occupe en partie, seulement la moitié négative, non revendiquée** ; « voisin » pour les pièces revendiquées | un moniteur qui ne voit que des fragments localement bénins et indiscernables est aveugle (borne en variation totale) ; germe du côté K : variation totale conjointe grande quand les marges locales sont petites | sous-groupes de permutations et unification temps × agents ; classe C ; distinction C/K ; garanties locales face à un attaquant adaptatif ; activations réelles | 2, 3, 10 | lot3-Ab |
| 2005.07821v1 | voisin (« touché partiellement, sous forme de remarque ») | chaque statistique cumulée est aveugle à une attaque qui préserve ce qu'elle accumule | théorème ; activations | 5 | lot2-A1 |
| 2605.26047v2 | voisin (« touché partiellement, sur un autre axe ») | le bon agrégateur (max ou min) dépend des corrélations entre ré-échantillonnages, que l'attaquant peut choisir | théorème ; données synthétiques seulement | 7 | lot2-A1 |
| 2605.31593v1 ; 2608.02698v1 ; 2606.09931v1 | voisin (empirique ; classique ; conceptuel) | le renommage disperse l'attaque entre groupes ; sous un débit dissimulé, aucun test boîte noire ne bat le hasard ; une borne de fuite d'information n'implique pas une borne de dommage | pièces revendiquées | 8 ; 5 ; 1 | lot2-B1 |
| 2602.20628v2 | voisin | dépendance entre scores ; max | pièces revendiquées | 23, 33 | lot2-A4 |
| 2609.36490v1 | voisin, pour le seul volet « attaquant adaptatif » | attaquant qui s'adapte aux verdicts | statistique invariante par permutation ; garantie locale séquentielle ; agents multiples | 2 | lot3-Cc |
| 2604.16824v1 (SafeDream) | voisin faible | permuter les tours fait tomber l'aire de 0,908 à 0,633 | pièces revendiquées | 17 | lot3-Ab |
| 2403.17710v5 ; 2607.13087v1 | voisin lointain | perte de perplexité adverse pour passer sous un seuil ; menace d'étalement nommée | énoncé statistique | 5 ; 4, 8 | lot2-C2b ; lot3-Ac |
| autres sources | ne touche pas | — | — | — | lot2-A2a, lot2-A2b, lot2-A3, lot2-C1a, lot2-C1b, lot2-C2a, lot2-C3a, lot2-C3b, lot3-Aa, lot3-Ab (2604.14865), lot3-Ac (2606.17478, 2412.01784), lot3-Be, lot3-Ca, lot3-Cb, lot3-Cc (2603.13791), lot3-Cd |

- **Reste revendicable** : les quatre pièces de N-003 (unification temps × agents par sous-groupes de permutations, distinction C/K, garanties locales face à un attaquant adaptatif, transposition aux activations réelles).
- **Désaccords** : lot3-Ab précise le « occupe en partie (énoncé 4) » de la recherche affirmative (moitié négative seulement) ; lot3-Cc ramène 2609.36490 de « occupe en partie le volet attaquant adaptatif de 5 » à « voisin ».

## Tr — transposition jeton → action

| source | verdict du lecteur | composantes faites | composantes non faites | pages | rapport |
|---|---|---|---|---|---|
| 2412.09565v2 | **contre-indice partiel** (« borne « max robuste » ») | des moniteurs au max sur la séquence ont un rappel quasi nul sous suffixe d'embedding | niveau action ; trajectoire | 22 | lot2-A2a |
| 2512.11949 | **contre-indice partiel** | « attention-based monitors mitigate but do not eliminate evasion » | niveau action | 7, 11 | lot2-A2a |
| 2511.00554v1 | **contre-indice** (« touche sa prémisse ») | une sonde à attention cède en partie à un attaquant boîte noire par contenu | niveau action | 3 | lot2-A2b |
| 2507.12691v3 | **contre-indice** (au niveau jeton) | sous dilution, la moyenne résiste et le max se dégrade | niveau action ; adversaire entraîné | 8, 15 | lot2-A1 |
| 2609.36490v1 | voisin ; **contre-indice limité** | une sonde à mise en commun par attention est évadée au niveau d'une réponse (0,25 ; 0,04) | max ; action ; trajectoire ; accumulation ; l'attaque n'est pas une dilution de contenu | 8, 9, 15 | lot3-Cc |
| 2506.14261v4 | voisin (« non occupée », source du constat jeton) | max et attention sans évasion utile sous apprentissage par renforcement, nocivité seulement | niveau action | 10 | lot2-A2a |
| 2601.11516v4 ; 2602.15515v2 | voisin | MultiMax gonfle les faux positifs en contexte long (82,14 %) et la moyenne dilue (99,13 % de faux négatifs) ; sondes à moyenne contournées par dilution, un tour | niveau action ; déroulé en cours | 12, 19 ; 4, 7 | lot2-A2a |
| 2506.10805v4 ; 2504.20271v1 ; 2504.10374v1 | voisin (« niveau jeton seulement » ; « marginalement ») | comparaison d'agrégations en performance ; max utile aux autoencodeurs parcimonieux, nuisible aux activations brutes ; max sur sous-commandes en boîte noire | niveau action ; adversaire | 4 ; 6, 12 ; 22 | lot2-A1 |
| 2604.14865v1 | voisin (« pas un contre-indice au sens strict ») | K meilleures fenêtres contre maximum dans un échange : 80,96 contre 70,11 à faibles faux positifs ; le maximum paie en faux positifs bénins, pas en robustesse adverse | action ; trajectoire ; attaquant | 8, 10, 16, 23 | lot3-Ab |
| 2607.11751v1 | voisin | « alarme si l'une » (type maximum) au niveau trajectoire, boîte noire ; moniteur à une classe invariant à l'ordre (0,873) | sondes ; attaquant adaptatif | 10, 14, 15 | lot3-Ab |
| 2508.19461v1 ; 2603.13791v1 | voisin | robustesse dépendante de l'agrégation (séquentiel cède à l'injection répétée, hiérarchique résiste) ; sonde sur un seul jeton, échec par dilution (19 faux négatifs sur 50) | agrégations de sondes ; attaquant adaptatif | 25 ; 8, 33, 37 | lot3-Ca ; lot3-Cc |
| 2607.02514v2 ; 2512.07810v1 ; 2604.22888v1 ; 2403.17710v5 | voisin | max contre moyenne par demande de fusion (juge) ; difficulté nommée, non étudiée ; max sur fenêtres sans robustesse ; perplexité par fenêtres, max | sondes au niveau de l'action | 30 ; 43 ; 6 ; 12 | lot2-B1 ; lot2-A3 ; lot2-C3a ; lot2-C2b |
| autres sources | ne touche pas | — | — | — | lot2-A2b (2509.26238, 2605.27958, 2502.03407, 2606.07612), lot2-A4, lot2-C1a, lot2-C1b, lot2-C2a, lot2-C3b, lot3-Aa (2610.04575 : voisin lointain, sonde moyenne à 0 sur 38 positifs à 5 %, p. 1), lot3-Ac (2606.17478 : moyenne des jetons ; 2412.01784 ; 2607.13087), lot3-Be, lot3-Ca (2608.25869), lot3-Cb, lot3-Cd |

- **Reste revendicable** : la transposition au niveau de l'action et de la trajectoire, face à un attaquant adaptatif, n'est faite nulle part.
- **Prémisse affaiblie** : max sous suffixe d'embedding (2412.09565), attention atténuée sans éliminer l'évasion (2512.11949), attention évadée en boîte noire (2511.00554) ou après réglage (2609.36490), max dégradé sous dilution (2507.12691).
- **Désaccords** : aucun entre lecteurs ; lot3-Ab confirme « voisin » pour 2604.14865 (recherche affirmative, « 5 »).

## H6 — marge asymétrique des interventions non spécifiques

| source | verdict du lecteur | composantes faites | composantes non faites | pages | rapport |
|---|---|---|---|---|---|
| 2412.01784v3 | **occupe en partie** (lecture A, retenue) ; voisin (lecture B) | bruit gaussien sur tous les poids ou sur des adaptateurs ; balayage d'intensité ; la performance du modèle qui sous-performe monte quand celle du modèle standard baisse ; tests de Welch et Benjamini-Hochberg ; huit modèles, trois modes ; usage en détection | paraphrase, ré-échantillonnage, remise à zéro du contexte, bruit d'activations ; sabotage d'agent sur tâches floues ; marge moyenne à intensité fixée (le papier mesure un maximum sur tirages) ; usage défensif | 2, 4, 5, 6, 9, 10, 17, 19 | lot3-Ac |
| 2607.13087v1 | voisin (intention) ; **risque de collision** | marge asymétrique énoncée comme but ; interventions candidates nommées (limiter durée, mémoire ou communication, paraphraser, ré-échantillonner, remettre à zéro) ; « activement étudiées » | aucune mesure ; praticabilité « pas encore claire » | 6, 18, 21, 29 | lot3-Ac |
| 2411.17693v1 | voisin | réécriture « Edit Untrusted », une intensité, ciblée : portes dérobées de 13,4 % à 0,9 % par tentative ; utilité de 47,4 à 38,1 | intervention non spécifique | 4, 24, 41 | lot3-Aa |
| 2609.36490v1 | voisin (côté attaque seulement) | retirer toutes les démonstrations (remise à zéro du contexte) supprime l'attaque ; 10 % de verdicts faux laissent 87 % de la modification | utilité honnête sous ces interventions ; courbe d'intensité ; paraphrase, ré-échantillonnage, bruit d'activations | 7, 18, 23, 24 | lot3-Cc |
| autres sources | ne touche pas | — | — | — | lot3-Ab, lot3-Ac (2606.17478), lot3-Be, lot3-Ca, lot3-Cb, lot3-Cc (2603.13791), lot3-Cd, lot3-Aa (2610.04575) ; les rapports des lots 1 et 2 ne traitent pas H6 |

- **Reste revendicable** : la marge moyenne défensive à intensité fixée, pour les interventions listées, sur du sabotage d'agent ; l'existence d'une intensité où une perturbation non ciblée casse le comportement caché avant la compétence est publiée pour le bruit sur les poids (2412.01784).
- **À lire** : Clymer et al. (perturbation d'activations, cité par 2412.01784) pour la composante « bruit d'activations » (piste non vérifiée, lot3-Ac).
- **Désaccords** : lot3-Ac confirme le « occupe en partie » de la recherche affirmative quant aux composantes, en le subordonnant à la lecture de H6 ; il déplace le risque de collision de 2607.13087 de H2 vers H6 et H3.

## H8 — la validité du construit prédit la robustesse

| source | verdict du lecteur | composantes faites | composantes non faites | pages | rapport |
|---|---|---|---|---|---|
| 2605.27958v1 | **occupe en partie** | lien entre ce que capte la sonde (régime de consigne, corrélats de style) et sa fragilité au style, hors attaque | robustesse adverse prédite par le construit ; axe intention contre conscience d'évaluation | 7 | lot2-A2b |
| 2609.36490v1 | voisin (deux lectures) | la facilité d'évasion dépend de la façon dont la différence des moyennes retrouve la direction de la sonde (0,389 contre 0,119 au hasard) ; forte dispersion par concept | axe intention contre conscience d'évaluation | 22, 23, 24 | lot3-Cc |
| 2509.21344v2 | voisin (« occupe en partie » écartée) | établit ce que lisent les sondes (évidence textuelle plutôt que « cognition ») | construit mesuré indépendamment, puis robustesse adverse prédite | 1, 9 | lot3-Cb |
| 2606.07612v1 | voisin (prémisse seulement) | validité de construit : faux positifs de 87 à 100 % sur sarcasme, « Wrong Answers Only », contrefactuel et récitation | mesure de robustesse adverse | 22 | lot2-A2b |
| 2607.06596v3 | voisin | la non-transférabilité vient de la signature stylistique de famille captée ; l'angle entre directions prédit le transfert, causalement | robustesse adverse ; sondes d'activations | 19, 20 | lot3-Cd |
| 2604.14865v1 ; 2511.00554v1 | voisin | construit « mots-clés contre intention » relié aux faux positifs bénins ; motifs d'échec lexicaux | robustesse adverse prédite | 24 ; 6, 7 | lot3-Ab ; lot2-A2b |
| autres sources | ne touche pas | — | — | — | lot2-A2b (2609.24967), lot3-Aa, lot3-Ab (SafeDream, 2607.11751), lot3-Ac, lot3-Be (2602.22303 : piste p. 29 ; 2608.19161), lot3-Ca, lot3-Cb (2508.05625), lot3-Cc (2603.13791), lot3-Cd (MonitoringBench, SLEIGHT-Bench) |

- **Reste revendicable** : la prédiction de la robustesse adverse par un construit mesuré d'abord, sur l'axe intention contre conscience d'évaluation.
- **Désaccords** : lot3-Cb écarte la lecture « occupe en partie » pour 2509.21344.

## HC1 — loi de déférence à destination libre (N-005)

Pièces revendiquées par N-005 : (a) destination libre ĉ testée contre la cible v* et la moyenne du corpus, par famille, dans des moniteurs de contrôle sous attaque ; (b) régression sur plusieurs intensités par famille ; (c) verdict lu par probabilité du jeton ; (d) opposition juge / sonde.

| source | verdict du lecteur | composantes faites | composantes non faites | pages | rapport |
|---|---|---|---|---|---|
| 2404.13076v1 (Panickssery et al.) | **occupe en partie** (« partiel ») | (c) : « la lecture du verdict d'un juge par la probabilité des jetons est occupée » ; « Il ne peut pas être revendiqué seul » | (a), (b), (d) ; moniteurs de contrôle | 2 | lot2-C1a |
| 2410.21819v2 (Wataoka et al.) | **occupe en partie** (« partiel ») | (c), même occupation | (a), (b), (d) | 4 | lot2-C1a |
| 2411.03336v2 | voisin (« technique voisine ») ; (c) jugée non revendicable comme technique | un moniteur de confiance lit son score dans les probabilités « Oui » / « Non » : « La lecture du verdict par probabilité du jeton n'est donc pas revendicable comme technique ; seul son emploi pour estimer la loi de déférence l'est » | phénomène de déférence | 25 | lot2-A4 |
| 2602.20628v2 | voisin (« technique de lecture par jetons déjà employée, phénomène absent ») | différence de logits des jetons « YES » et « NO » | pression graduée ; loi de déférence | 6 | lot2-A4 |
| 2411.17693v1 | **occupe en partie** (instrument seulement) ou voisin, deux lectures | verdict d'un moniteur de contrôle lu comme score continu par les probabilités « yes » / « no » ; « Dans les deux cas, cet instrument seul n'est pas revendicable » | (a), (b), (d) | 19, 21 | lot3-Aa |
| 2511.17220v2 (PARROT) | **occupe en partie** (« partiellement » : (a) catégoriel, (c) sur un assistant ; le lecteur conclut « Aucune pièce (a) à (d) n'est donc « occupée » » en entier, elles sont « partiellement approchées ») | destination testée de façon catégorielle ; probabilité des étiquettes sur la réponse d'un assistant ; famille autorité seulement | (b) (une intensité) ; (d) | 4, 9, 12 | lot1-HC1-voisins |
| 2410.14746v1 (Sicilia et al.) | **occupe en partie** (« partiellement » pour (b) et (c), sur un assistant ; pièces « partiellement approchées ») | deux intensités et une condition nulle, sans régression ni gain ; probabilité implicite des jetons de la réponse | (a), (d) ; effet de l'intensité petit, de signe non constant (calcul) | 3, 4, 6 | lot1-HC1-voisins |
| 2606.14037v1 (Kim et Flanigan) | **occupe en partie** (« partiellement » pour (b), (c) « à la marge » ; pièces « partiellement approchées ») | trois intensités × deux familles, gradient monotone (« source la plus proche de la grille familles × intensités ») ; premier jeton comme covariable | régression, gain, destination ; (d) | 4, 12-14 | lot1-HC1-voisins |
| 2606.18276v1 (Probine et al.) | **occupe en partie** (« Partiellement occupée : seule la composante « destination libre estimée sans l'imposer » est présente ») | attracteur libre b estimé par moindres carrés, qui domine l'ancrage initial ; biais inné, sans attaque | intensités graduées, attaque, familles, moniteurs de contrôle, probabilité du jeton | 3-7, 15-17 | lot1-GC-reseaux |
| 2603.15809v1 (Abedini et al.) | **occupe en partie** (forme à destination imposée) | « poids du conseil » à destination imposée (le prior de l'attaquant), en théorie, en cadre adverse entre grands modèles de langage | destination libre et le reste de la pièce | 10-16, 48 | lot1-GC-reseaux |
| 2608.25869v1 | voisin (lecture retenue ; « occupe en partie » possible) ; **contre-indice faible, non concluant** pour ĉ = v* | juge génératif déplacé par une valeur imposée ; valeur de l'ancre variée (1,0 à 3,9) ; probabilités des jetons de note (sondes) ; nul « plafond » testé ; dans une sonde, la destination est le chiffre voisin (4), pas l'ancre ; contrepoids : pente 0,267 compatible avec un suivi partiel | moniteur de contrôle, attaquant, familles, intensités graduées, régression, moyenne du corpus, (d) | 2, 4, 6, 7 | lot3-Ca |
| 2508.19461v1 | voisin (lecture retenue ; « occupe en partie » possible) | moniteurs de contrôle sous attaque, plusieurs familles, deux dosages grossiers ; destination qualitative : la note 1 visée par l'attaquant ; « à citer à côté de 2607.08066 » | ĉ, moyenne du corpus, régression, comparaison des destinations, probabilité du jeton (mesure en aire sous la courbe) | 13, 15, 25 | lot3-Ca |
| 2510.09462v2 | voisin (« touchée en partie, non occupée » ; « voisin direct de HC1 ») | moniteurs de contrôle qui adoptent le score injecté, sous les honnêtes, une intensité, score écrit | pression graduée, destination libre contre moyenne, familles, probabilité du jeton ; « Les pièces revendiquées par la décision N-005 restent libres dans cette source » | 5, 8, 23 | lot2-A4 |
| 2505.23575v3 (Arnav et al.) | voisin (« touché en partie ») | déplacement de moniteurs de contrôle par la rhétorique de l'agent (capture à 1 % de faux positifs, score verbal) ; « À ajouter aux sources « citées comme publiées » de HC1 » | ĉ libre, régression, probabilité du jeton, loi par famille | 1, 6, 7, 8, 13 | lot2-C1b |
| 2601.13433v4 (Who Endorsed It?) | voisin | une famille graduée sur quatre niveaux d'autorité, réponse monotone ; logits lus sur les options : « plusieurs intensités par famille » et « lecture par probabilité du jeton » présents pris isolément | gain, destination, nul ; le modèle influencé répond, il ne juge pas | 1-6 | lot2-C2a |
| 2605.23970v1 ; 2509.26072v2 ; 2604.21564v2 | voisin | décomposition directionnelle du déplacement (test catégoriel de destination) ; verdict binaire déplacé par des indices, un niveau par condition ; pression croissante sur cinq tours, destination fixée | (a), (b), (c), (d) | 4, 8 ; 3, 5 ; 16-18 | lot2-C2a |
| 2402.14016v2 | voisin (« contact partiel, n'occupe pas ») | intensité graduée (un à quatre mots optimisés) ; verdict lu par les probabilités des jetons de note | suffixe optimisé, destination imposée ; ni familles ni moniteur | 3, 5, 6 | lot2-C2b |
| 2403.17710v5 ; 2505.13348v1 ; 2504.18333v1 | voisin (contacts) | probabilité du jeton comme objectif d'attaque ; sape visant la probabilité de décision ; échelle ordinale de sophistication, familles dont l'autorité | (a), (b), (d) | 2 ; 2 ; 3, 4 | lot2-C2b |
| 2309.17012v3 (Koo et al.) | voisin (« adjacent, précurseur ») | intensité variée d'une fausse majorité (85 %, 0 %, 50-85 %) sur des juges, famille des approbations forgées, choix binaire | régression, destination libre, moniteurs, (d) | 8, 14, 15 | lot2-C1a |
| 2402.10669v5 (Chen et al.) ; 2403.04957 (Liu et al.) | voisin (« adjacent ») | autorité par fausses références, une intensité, bascule binaire ; ordres en bande à cible explicite, sans juge | (a), (b), (c), (d) | 3 ; 1, 5 | lot2-C1a |
| 2410.21514 (Benton et al.) | voisin | pression graduée (trois niveaux d'agressivité) sur des humains, destination imposée ; verdict d'un moniteur lu en log-probabilité de « Yes », pour une autre question | (a), (b) sur moniteur, (d) | 7, 26, 67 | lot2-A3 |
| 2604.16286v2 ; 2511.09904 ; 2602.15222v1 ; 2604.22082 | voisin ; voisin lointain | persuasion à un niveau ; justifications ; biais de modèle de récompense | pièce revendiquée | 38 ; 6, 7 ; 5 ; 42 | lot2-A3 |
| 2608.16190v1 ; 2605.31593v1 | voisin (méthode voisine ; en marge) | verdict lu dans les logits du jeton de décision ; fausses approbations dans le contexte du juge, attrapées à 82 % | pièce revendiquée | 3 ; 8, 9 | lot2-B1 |
| 2606.07612v1 | voisin | notation pondérée par les probabilités des jetons recommandée comme pratique | pièce revendiquée | 25 | lot2-A2b |
| 2502.01534v3 ; 2601.09923v3 | voisin (contacts faibles) | log-probabilités du choix du juge pour calibrer un biais ; vérificateurs en faux et vrais positifs | pièce revendiquée | 19 ; 25 | lot2-C1b ; lot2-C3b |
| 2508.16846v6 (BASIL) | ne touche pas (« n'occupe aucune pièce ») | trois formulations de force différente à petite échelle, sans en faire des intensités ; apporte des contrôles (condition « tiers », log-cote, postérieur bayésien) | (a), (b), (c), (d) | 6, 9, 10, 13 | lot1-HC1-voisins |
| MonitoringBench 2605.09684v1 | voisin ; **contre-indice faible et qualitatif** | tactique « persuasion et camouflage d'erreur » ; « couverture » à une seule intensité (note d'Opus 4.5 de 9,3 à 4,9-5,2 sur 10) ; les attaques réussissent mieux sans justification verbeuse (sous un prompt qui demande de s'en méfier) | intensités graduées, probabilité du jeton, régression, ĉ, test cible / moyenne, g par famille, rang, (d) | 7, 8, 18, 20, 39, 44 | lot3-Cd |
| SLEIGHT-Bench 2605.16626v2 ; 2607.13087v1 ; 2610.04575v1 | voisin | catégories qui recoupent quatre familles, taux binaires par essai ; menace nommée (débrider, persuader, embrouiller le moniteur) ; log-cotes d'un modèle de 14 milliards | (a), (b), (c), (d) | 4, 5 ; 23, 36 ; 5 | lot3-Cd ; lot3-Ac ; lot3-Aa |
| autres sources | ne touche pas | — | — | — | lot2-A1 (« L, HC1 : non touchés »), lot2-A2a (2601.11516 : réécriture sans pression graduée, p. 10 ; 2602.15515 : juge biaisé comme récompense, p. 24), lot2-A2b (2509.26238, 2605.27958, 2502.03407, 2511.00554), lot2-C2b (2603.29403 : piste CALM, Ye et al. 2024, « à lire avant toute revendication », p. 14, 30), lot2-C3a, lot3-Ab, lot3-Ac (2606.17478, 2412.01784), lot3-Be, lot3-Cb (2508.05625, p. 15), lot3-Cc, lot3-Cd (2607.06596, p. 3) |

- **Reste revendicable** : (a) ĉ libre testée contre v* et la moyenne du corpus, par famille, dans des moniteurs de contrôle sous attaque (porte GC non déclenchée, combinaison libre) ; (b) la régression sur plusieurs intensités ; (d) l'opposition juge / sonde. (c) n'est plus revendicable comme technique, seulement comme emploi pour estimer g et ĉ.
- **À lire avant toute revendication** (pistes signalées, non lues) : Panin (décision N-005), CALM (Ye et al. 2024, lot2-C2b), Kaur 2025 et 2509.16533 (lot2-C2a), Za et al. 2026 (lot3-Ac).
- **Désaccords** : lot3-Ca ramène le « occupe en partie » de la recherche affirmative à « voisin » pour 2608.25869 et 2508.19461 ; lot3-Aa donne deux lectures pour 2411.17693 ; lot3-Cd juge que 2607.06596 ne touche pas HC1, contre la pertinence HC1 avancée par la recherche affirmative.

## HC2 — robustesse des sondes à l'attaque par contenu (g_sonde ≈ 0)

| source | verdict du lecteur | composantes faites | composantes non faites | pages | rapport |
|---|---|---|---|---|---|
| 2511.00554v1 (Blandfort et Graham) | **contre-indice** (« collision partielle ») | évasion partielle par pur contenu, en boîte noire, d'une sonde « enjeux élevés » à attention : 48,9 % des tentatives de faux négatif, 63,6 % sur la seconde moitié des lots ; contredit l'état de l'art v1, l. 155 et 157, pour ce concept | textes entièrement écrits par l'attaquant (hors politique) ; seuil fixe à 0,5 ; concept « enjeux élevés », pas tromperie | 3, 6, 7, 11 | lot2-A2b |
| 2601.11516v4 | **contre-indice** (« en tension ») | réécriture narrative : faux négatifs de la sonde retenue de 8,58 % à 42,46 %, MultiMax de 8,12 % à 22,97 %, contre 20,65 % pour Gemini 2.5 Flash ; « Adversarial attacks remain challenging for all methods » | agent ; agrégation sur trajectoire | 12, 13 | lot2-A2a |
| 2509.21344v2 | voisin ; **contre-indice indirect** (inférence) | le score moyen est porté par les positions de l'évidence textuelle ; une sonde qui lit le texte peut a priori être déplacée par du texte ajouté ; lecture inverse à citer aussi | aucune attaque par contenu ; aucune mesure de g ; agrégation robuste (moyenne seulement) | 1, 3, 5, 29 | lot3-Cb |
| 2609.36490v1 | voisin ; **contre-indice faible** | par consigne seule, verdict inchangé mais score continu déplacé (∆z de 0,26 à 0,80) et alignement d'environ dix fois le hasard ; un réglage léger suffit ensuite à l'évasion | attaque par contenu (sortie imposée) ; l'agrégation robuste est sans effet contre une modification uniforme | 5, 9, 17, 23 | lot3-Cc |
| 2603.13791v1 | voisin | sonde sur un lecteur du texte (configuration que HC2 exclut) ; 0,847 sous chaîne de pensée trompeuse | sonde lisant l'agent ; attaque | 10, 38 | lot3-Cc |
| 2604.14865v1 | voisin | robustesse au contenu chiffré une fois le modèle affiné ; au hasard sans adaptateur | attaque adaptative | 9, 27 | lot3-Ab |
| autres sources | ne touche pas | — | — | — | lot2-A2b (2606.07612 : aucune attaque), lot3-Aa, lot3-Ab (SafeDream, 2607.11751), lot3-Ac, lot3-Be, lot3-Ca, lot3-Cb (2508.05625), lot3-Cd ; les autres rapports du lot 2 ne traitent pas HC2 |

- **Reste revendicable** : la robustesse sous attaque par contenu d'une sonde lisant l'agent, avec agrégation robuste, mesurée par g (jamais l'immunité absolue).
- **Contre-indices à garder** : 2511.00554 et 2601.11516 montrent déjà une évasion partielle par contenu de sondes ; 2509.21344 et 2609.36490 rendent g_sonde ≈ 0 moins probable.
- **Désaccords** : lot3-Cb ramène « voisin fort, contre-indice » (recherche affirmative) à « voisin (pas fort), contre-indice indirect » pour 2509.21344.

## HC2b — auto-incrimination de l'agent qui tente de manipuler, contrôlée contre le style

| source | verdict du lecteur | composantes faites | composantes non faites | pages | rapport |
|---|---|---|---|---|---|
| 2602.15515v2 | **contre-indice** (« touchée en partie de signe contraire ») | les politiques obfusquées ont des scores de tromperie plus bas que les honnêtes | contrôle du style | 6 | lot2-A2a |
| 2509.21344v2 | voisin ; **contre-indice indirect** sur la version contrôlée contre le style | des sondes de tromperie réagissent à des textes qui discutent la tromperie ; sans évidence textuelle, elles tombent au hasard ou presque | agent qui tente de manipuler ; contraste « tente / ne tente pas » à style égal | 5, 8, 13, 29 | lot3-Cb |
| 2609.36490v1 | voisin ; **contre-indice faible** | la tentative d'évasion rend les activations anormales (99,3 % signalées par un détecteur générique), mais un entraînement adverse efface cette signature | sonde d'intention ; contrôle du style | 6, 7, 19, 21 | lot3-Cc |
| 2602.22303v1 | voisin ; **collision de vocabulaire** confirmée ; contre-indice (recadrage) examiné, non opposable aux sondes | un signal venu de l'agent qui poursuit une tâche cachée le trahit pendant l'exécution (« self-incrimination » = appel d'outil appris, 264 occurrences) | signal passif lu par des sondes ; contrôle du style ; manipulation d'un moniteur | 2, 3, 9, 12, 15 | lot3-Be |
| 2505.23575v3 (Arnav et al.) | voisin (« touché en partie, versant texte ») | l'instruction de discrétion fait monter la capture de tous les moniteurs ; « témoin à contrôler » | sonde | 7 | lot2-C1b |
| 2507.12691v3 | voisin (« touchée partiellement, si HC2b vise la sonde lue pendant un déni ») | sonde lue sur la dénégation après relance ; fait moins bien que la moyenne simple | manipulation d'un moniteur | 6 | lot2-A1 |
| 2502.03407v1 | voisin (« antécédent le plus proche de « plaider incrimine » dans ce lot ») | sonde lue après un démenti « No » imposé : séparation presque parfaite | tentative de manipuler ; contrôle du style | 9 | lot2-A2b |
| 2605.27958v1 ; 2511.00554v1 ; 2609.24967v2 | voisin | la sonde signale la consigne trompeuse même quand la réponse reste exacte ; des mots déclencheurs font monter le score (sens inverse) ; voisinage textuel | tentative de manipuler le moniteur ; sonde de l'agent | 9 ; 6 ; 24 | lot2-A2b |
| 2512.11949 | voisin (« touchée à la marge ») | un déclencheur améliore légèrement la sonde sur modèle de base ; sur modèle entraîné, la tentative fait baisser le score | méta-moniteurs | 1, 11, 23 | lot2-A2a |
| 2512.07810v1 ; 2510.09462v2 ; 2411.03336v2 | voisin | confondant de style documenté, auto-incrimination par incitation boîte noire en échec ; retour de bâton textuel (« failed injections raise suspiciousness ; successful ones reduce it ») ; trois voisinages | sonde de l'agent qui manipule | 15, 17 ; 8 ; 43, 45 | lot2-A3 ; lot2-A4 |
| 2603.12277v6 ; 2608.02657v2 ; 2606.22864v1 | voisin (pertinents pour le contrôle du style) | des sondes entraînées sur les seules balises répondent au style ; instruction de suppression sans effet (1,000 et 0,956) ; corrélats de surface | auto-incrimination | 1 ; 6 ; 16 | lot2-C3a ; lot2-C3b |
| 2601.13433v4 ; 2606.17478v1 | voisin ; voisin lointain | vecteur « expertise » dans le flux résiduel du modèle influencé (pilotage) ; les activations d'un agent qui trompe l'utilisateur portent un signal (0,920 et 0,911), sans contrôle du style | sonde de l'agent manipulateur ; moniteur | 6 ; 1, 7 | lot2-C2a ; lot3-Ac |
| 2508.05625v1 | voisin (faible) ; zone libre « dans cette source seulement » (R8) | stratégie rhétorique décodable dans un modèle lecteur tiers, tour par tour | activations du persuadeur ; contraste « tente / ne tente pas » ; contrôle du style | 1, 3, 5, 15 | lot3-Cb |
| 2603.13791v1 | voisin | la sonde « s'active fortement » sur une chaîne de pensée assainie (0,74) ; des raisonnements honnêtes complexes ressemblent à de l'assainissement (17 cas) | sonde sur l'agent ; contrôle du style | 6, 11, 33, 41 | lot3-Cc |
| 2607.06596v3 | ne touche pas l'énoncé ; utile pour son contrôle de style | des têtes linéaires captent la signature stylistique de la famille productrice (2,6 fois le hasard) | — | 20 | lot3-Cd |
| autres sources | ne touche pas | — | — | — | lot2-A2b (2606.07612, 2509.26238), lot2-B1 (2605.29178 : la sonde est la cible du sabotage, p. 12), lot2-C1b (2502.03052, p. 4), lot2-C2a (2509.26072, 2605.23970, 2604.21564), lot2-C2b, lot3-Aa, lot3-Ab, lot3-Ac (2412.01784, 2607.13087), lot3-Be (2608.19161), lot3-Ca, lot3-Cd (MonitoringBench, SLEIGHT-Bench) |

- **Reste revendicable** : l'auto-incrimination comme propriété des sondes de l'agent qui tente de manipuler, contrôlée contre le style (N-005, prédiction 4) ; le mot « self-incrimination » est pris pour un signal comportemental appris (2602.22303).
- **Contre-indices à garder** : 2602.15515 (signe contraire), 2509.21344 et 2609.36490 (signature effaçable ou portée par le texte).
- **Désaccords** : lot3-Cb ramène « voisin fort » (recherche affirmative) à « voisin faible » pour 2508.05625 ; lot2-A2b corrige « soutient HC2b » en « ne teste pas HC2b » pour 2605.27958.

## HC3 — ordres en bande et usurpation stylistique

| source | verdict du lecteur | composantes faites | composantes non faites | pages | rapport |
|---|---|---|---|---|---|
| 2508.19461v1 | **occupe en partie** (composante 1) | des ordres en bande insérés par l'agent déplacent un juge génératif de contrôle (trajectoire entière ; séquentiel si l'injection est répétée) ; l'échafaudage hiérarchique résiste | détection sous protocole « contenu = données » ; usurpation stylistique séparée ; sondes | 11, 25, 30 | lot3-Ca |
| 2603.12277v6 | **occupe en partie** (« partielle ») | à argument constant, ôter le style du faux raisonnement fait tomber le succès de 61 % à 10 % sur le modèle attaqué ; le style seul déplace le rôle perçu, en représentation | influence sans ordre avec effet sur le comportement (spéculée) ; cible juge ou moniteur ; g par dose-réponse ; sonde lisant l'agent auteur | 4, 18, 19, 22, 32, 33 | lot2-C3a |
| SLEIGHT-Bench 2605.16626v2 | voisin (hésitation avec « occupe en partie » pour l'usurpation stylistique) ; **contre-indice possible, à trancher** | un débridage « miroir du prompt » échappe à cinq moniteurs sur six (Gemini le prend) ; confusion de rôle sans délimiteurs, levée par des balises | distinction ordres / usurpation ; protocole « contenu = données » explicite ; g ; sondes | 4, 5, 6, 20, 29, 34, 36-41 | lot3-Cd |
| 2601.09923v3 ; 2505.22852v1 | voisin | la séparation à double modèle rend impossibles les actions injectées hors plan pour un agent exécutant ; résidu (« branch steering ») | juge moniteur : « la couverture des ordres en bande de HC3 … reste à établir » | 7, 12 | lot2-C3b |
| 2505.06311v2 | voisin | détection des ordres en bande élevée mais pas quasi certaine hors domaine (96,90 %), une exécution, sans attaquant adaptatif | juge moniteur ; protocole | 6, 14 | lot2-C3a |
| 2608.25869v1 | voisin lointain (composante 3 seulement) | une consigne d'ignorer les métadonnées laisse un déplacement résiduel (−0,457 contre −0,429) ; nul en tâche catégorielle | ordres en bande ; usurpation ; sondes | 7, 8 | lot3-Ca |
| 2302.12173v2 ; 2502.01534v3 ; 2403.04957 | voisin | les applications confondent données et instructions ; le style comme canal de biais ; famille « ordres en bande » fondée (cible explicite, pas de juge) | moniteur | 1, 6 ; — ; 1, 5 | lot2-C1b ; lot2-C1a |
| 2607.13087v1 | voisin | menace nommée (débrider, persuader ou embrouiller le moniteur) | mesure | 23, 36 | lot3-Ac |
| autres sources | ne touche pas | — | — | — | MonitoringBench 2605.09684 (débridage hors champ, p. 9) et 2607.06596 (lot3-Cd), lot3-Aa, lot3-Ab, lot3-Ac (2606.17478, 2412.01784), lot3-Be, lot3-Cb, lot3-Cc ; les rapports lot2-A1 à lot2-B1 ne traitent pas HC3 |

- **Reste revendicable** : la détection des ordres en bande sous protocole « contenu = données » pour un juge génératif, et le g résiduel de l'usurpation stylistique sans ordre sur un juge ou un moniteur ; « les ordres en bande déplacent les juges génératifs » est acquis (2508.19461 ; HC3 doit préciser l'échafaudage).
- **Désaccords** : lot3-Ca confirme le « occupe en partie » de la recherche affirmative, avec une nuance (le moniteur hiérarchique résiste) ; lot2-C3a demande de nuancer « versant stylistique vierge » (état de l'art v1, l. 242).

## HC4 — taxe de déplacement : déplacer une sonde coûte bien plus que déplacer un juge

| source | verdict du lecteur | composantes faites | composantes non faites | pages | rapport |
|---|---|---|---|---|---|
| 2609.36490v1 | **contre-indice partiel** (axes calcul, requêtes, succès) ; voisin pour le reste | contre une sonde lisant l'agent, le contexte seul n'évade pas ; mais avec droit de réglage : rang 1, une époque, 1 500 pas (calcul), 32 verdicts binaires, 96 % d'évasion sur des sondes jamais vues ; l'axe accès va dans le sens de HC4 | juge génératif ; rhétorique ; coût de calcul chiffré par les auteurs ; transfert entre architectures faible | 2, 3, 4, 6, 20 | lot3-Cc |
| 2509.21344v2 | **contre-indice indirect, faible** | face à un organisme qui agit sans verbaliser, les sondes ne détectent plus rien : évasion sans obfuscation d'activations | coût d'attaque ; l'évasion a demandé un affinage | 9, 26, 28 | lot3-Cb |
| 2503.11926v1 | voisin | obfuscation sous pression d'optimisation, côté chaîne de pensée | activations | 1, 36 | lot2-C1b |
| 2508.19461v1 | voisin (côté juge seulement) | déplacement du juge par simple consigne, accès par interface | côté sonde ; obfuscation d'activations | 7, 18 | lot3-Ca |
| 2607.13087v1 | voisin (jugement sans chiffre) | obfusquer ses activations « semble bien plus difficile » que tromper la chaîne de pensée ou les actions | coût, accès, requêtes, taux | 25 | lot3-Ac |
| autres sources | ne touche pas | — | — | — | lot3-Cd (MonitoringBench et SLEIGHT-Bench : coûts côté juge seulement ; 2607.06596), lot3-Cc (2603.13791 : coûts de défenseur), lot3-Aa, lot3-Ab, lot3-Ac (2606.17478, 2412.01784), lot3-Be, lot3-Ca (2608.25869), lot3-Cb (2508.05625) ; les autres rapports du lot 2 ne traitent pas HC4 |

- **Reste revendicable** : l'écart de coût mesuré dans un même cadre (sonde contre juge) ; l'axe accès (contexte seul contre poids) reste appuyé, mais l'écart « de plusieurs ordres de grandeur » est rendu moins probable sur les axes calcul, requêtes et succès pour un attaquant qui peut régler le modèle.
- **Désaccords** : lot3-Cc précise la « menace HC4 » de la recherche affirmative en « contre-indice partiel, pas sur l'accès ».

## HC5 — contre-mesures : paraphrase de confiance, quorum par type d'accès, matrice de transfert (N-006)

| source | verdict du lecteur | composantes faites | composantes non faites | pages | rapport |
|---|---|---|---|---|---|
| 2603.13791v1 (DeceptGuard) | **occupe en partie, au sens faible** (le quorum) | trois juges incités (un seul modèle de base) et une sonde, combinés par un méta-classifieur appris, conçus pour la défaillance d'un moniteur ; présentés comme des régimes d'observabilité distincts | sonde lisant l'agent (elle lit un encodeur séparé) ; matrice de transfert ; paraphrase ; attaque adaptative ; « voisin » si HC5 exige des sondes lisant l'agent | 7, 8, 9, 12, 41 | lot3-Cc |
| 2609.36490v1 | **occupe en partie** la matrice de transfert (entre sondes seulement) ; voisin pour le quorum et la paraphrase | matrice d'attaques entre trois architectures de sondes ; ensemble de sondes et détecteur hors distribution évalués comme défenses | juge génératif, donc quorum par type d'accès ; paraphrase ; attaques de corruption par contenu ; « voisin » si la matrice vise juges et sondes | 3, 4, 6, 8 | lot3-Cc |
| MonitoringBench 2605.09684v1 | voisin (hésitation avec « occupe en partie » pour la matrice) | attaques optimisées contre trois moniteurs puis évaluées sur dix tenus à l'écart ; transfert directionnel entre deux moniteurs (figure non lue) | matrice ; attaques de corruption du jugement ; quorum ; sondes ; paraphrase | 1, 5, 9, 31 | lot3-Cd |
| 2602.22303v1 | voisin (« occupe en partie » examinée et écartée) | quorum de deux signaux d'origines différentes (auto-signalement et juge boîte noire) par la règle « ou » ; défense la plus dure à casser | sondes internes dans le quorum ; paraphrase ; matrice | 11, 12, 16, 39 | lot3-Be |
| 2505.23575v3 | voisin | quorum par type d'accès en version textuelle (actions et chaîne de pensée, hybride) | forme N-006 (juges et sondes) | 6 | lot2-C1b |
| 2610.04575v1 | voisin | fusion tardive d'une sonde interne et d'un observateur boîte noire | quorum ; attaques de corruption ; matrice | 5 | lot3-Aa |
| 2510.09462v2 | voisin | transfert des injections entre moniteurs (figure 4) : « touche l'idée d'une matrice de transfert » | sondes ; quorum | — | lot2-A4 |
| 2508.19461v1 | voisin | l'échafaudage hiérarchique (le juge ne lit que des résumés) résiste à l'injection ; consigne de « fort a priori » contre la déférence à l'humain | quorum par type d'accès ; matrice ; paraphrase isolée | 10, 15, 34 | lot3-Ca |
| 2403.04957 ; 2502.01534v3 ; 2502.03052v2 | voisin (paraphrase) | paraphrase testée contre les ordres en bande et contournée par attaque adaptative (85 % de la performance retrouvée) ; paraphrase générique sans effet ; transfert d'attaques entre modèles | pièce revendiquée | 7 ; 10 ; 9 | lot2-C1a ; lot2-C1b |
| SLEIGHT-Bench 2605.16626v2 ; 2607.06596v3 ; 2607.13087v1 | voisin | six moniteurs de trois fournisseurs, ensemble de prompts suggéré non testé, empoisonnement par refus ; matrices de transfert entre familles recommandées ; paraphrase de confiance (Greenblatt et al. 2024) | quorum par type d'accès ; matrice de transfert d'attaques de corruption | 7, 8, 34 ; 1, 22, 26 ; 25 | lot3-Cd ; lot3-Ac |
| 2605.15377v2 | ne touche pas (« n'occupe ni le quorum par type d'accès ni la matrice de transfert ») | douze moniteurs sur GPT-4.1-mini, juges génératifs ; aucun membre à accès interne | — | 4, 7, 8, 11 | lot2-B1 |
| autres sources | ne touche pas | — | — | — | lot3-Ab, lot3-Ac (2606.17478, 2412.01784), lot3-Be (2608.19161, p. 6), lot3-Ca (2608.25869), lot3-Cb (2508.05625, p. 8 ; 2509.21344) ; les autres rapports du lot 2 ne traitent pas HC5 |

- **Reste revendicable** : le quorum par type d'accès au sens fort (juges génératifs et sondes lisant l'agent) et la matrice de transfert des attaques de corruption entre juges et sondes ; « ce qui tranche » selon lot3-Cc : la définition de « type d'accès » et le périmètre de la matrice dans HC5.
- **Désaccords** : lot3-Cc confirme « au sens faible » le « occupe en partie » de la recherche affirmative pour 2603.13791 ; lot3-Be écarte cette lecture pour 2602.22303 ; lot2-B1 juge levable la réserve de N-006 (l. 89) pour 2605.15377.

## HC6 — le g bénin prédit la robustesse

| source | verdict du lecteur | composantes faites | composantes non faites | pages | rapport |
|---|---|---|---|---|---|
| MonitoringBench 2605.09684v1 | voisin | écart entre attaques élicitées et affinées ; calcul du lecteur : le taux sur attaques faibles classe les moniteurs (Spearman 0,94) mais prédit mal l'effondrement relatif (0,43 sur six moniteurs) — « barre à battre pour HC6 » | g sur pression bénigne ; prédiction à partir d'une mesure bénigne | 1, 9, 23 | lot3-Cd |
| 2607.06596v3 | voisin ; **contre-indice faible, par analogie** | une mesure bénigne (distance entre distributions honnêtes) ne prédit pas la chute de détection hors famille | g sous pression bénigne ; attaque optimisée | 20 | lot3-Cd |
| 2609.36490v1 | voisin ; indice mixte, non concluant | déplacement non optimisé par modèle contre effondrement sous attaque (Spearman +0,8 sur quatre modèles, calcul) | puissance (n = 4) | 23 | lot3-Cc |
| 2508.19461v1 | voisin lointain | prédicteur de la fiabilité par l'écart de capacité (mesuré sur MMLU-Pro, banc de questions à choix multiples) ; une aire ≥ 0,9 contre agents non avertis n'annonçait pas l'effondrement sous détournement | g bénin | 11, 14 | lot3-Ca |
| autres sources | ne touche pas | — | — | — | lot3-Ac (2607.13087 : recette par évaluation adverse), lot3-Cd (SLEIGHT-Bench), lot3-Ca (2608.25869), lot3-Aa, lot3-Ab, lot3-Be, lot3-Cb, lot3-Cc (2603.13791) ; les rapports des lots 1 et 2 ne traitent pas HC6 |

- **Reste revendicable** : la prédiction de l'effondrement sous attaque optimisée par le g mesuré sous pression bénigne ; il devra faire mieux que le simple taux sur attaques faibles (MonitoringBench).
- **Désaccords** : aucun ; lot3-Cd confirme que MonitoringBench « touche l'esprit de HC6 sans prédire à partir de g » (recherche affirmative).

## H3 — courbe de sécurité selon le nombre d'agents N, à budget de sabotage constant

| source | verdict du lecteur | composantes faites | composantes non faites | pages | rapport |
|---|---|---|---|---|---|
| 2607.07368v1 (Makins et al.) | **occupe en partie** (« le pendant boîte noire ») | effet de fragmentation : plus les agents coordonnés sont nombreux (K = 1, 3, 9), moins les moniteurs par instance détectent ; moniteur conjoint non déployable | co-élévation interne ; boîte blanche | 1, 2, 8 | lot2-B1 |
| 2608.19161v1 | voisin (« occupe en partie » examinée et écartée) | moniteur boîte blanche évalué pour N = 25 à 100 ; pilotage boîte blanche contre boîte noire, en moyenne sur N | détecteur boîte noire ; paire de courbes en N ; budget constant (fraction de cartel fixe, colluders plus nombreux) | 7, 8, 9, 10 | lot3-Be |
| 2605.29178v1 | voisin (boîte noire) | effet de taille d'équipe (deux à quatre) non isolable | courbe en N | 29 | lot2-B1 |
| 2607.11751v1 | voisin | balayage K ∈ {2, 3, 5, 10} à charge fixe, boîte noire, résultats irréguliers | boîte blanche | 16 | lot3-Ab |
| 2607.13087v1 | voisin ; **risque de collision** | simulation d'attaque distribuée annoncée, surveillance propre à chaque agent | courbe en N ; comparaison blanc / noir ; budget constant | 32 | lot3-Ac |
| autres sources | ne touche pas | — | — | — | lot3-Be (2602.22303 : agent unique), lot3-Cd, lot3-Ca, lot3-Cb, lot3-Cc, lot3-Aa, lot3-Ab (SafeDream, 2604.14865), lot3-Ac (2606.17478, 2412.01784) ; les autres rapports des lots 1 et 2 ne traitent pas H3 |

- **Reste revendicable** : les deux courbes de sécurité en N (boîte blanche, boîte noire) à budget total de sabotage constant.
- **Désaccords** : lot3-Be ramène le « occupe en partie (H3) » de la recherche affirmative à « voisin » pour 2608.19161 ; lot3-Ac déplace vers H3 le risque de collision de 2607.13087.

## H4′ — diversification des agents contre la coordination

| source | verdict du lecteur | composantes faites | composantes non faites | pages | rapport |
|---|---|---|---|---|---|
| 2608.19161v1 | voisin (faible) | paires hétérogènes (familles différentes, adaptateurs sur données neutres) ; surveillance plus basse (0,854 contre 0,993) | coût de coordination de la diversification ; diversification par personas ; compromis chiffré | 5, 8 | lot3-Be |
| 2607.13087v1 | voisin (volet coordination seulement) | contenir l'attaquant en limitant coordination et communication | diversification ; décorrélation des signatures internes ; compromis chiffré | 4, 8, 18, 21 | lot3-Ac |
| autres sources | ne touche pas | — | — | — | lot3-Aa, lot3-Ab, lot3-Ac (2606.17478, 2412.01784), lot3-Be (2602.22303), lot3-Ca, lot3-Cb, lot3-Cc, lot3-Cd ; les rapports des lots 1 et 2 ne traitent pas H4′ |

- **Reste revendicable** : la diversification des agents par décorrélation des signatures internes et son compromis chiffré.
- **Désaccords** : aucun.

## H5 — nombre × diversité des moniteurs

| source | verdict du lecteur | composantes faites | composantes non faites | pages | rapport |
|---|---|---|---|---|---|
| 2605.15377v2 (Koran et al.) | **occupe en partie** (« thèse qualitative de H5 occupée en boîte noire ») | « la diversité, pas l'échelle » pour des moniteurs génératifs | inter-familles ; non génératifs ; trajectoires d'agents ; transfert d'attaque | 1, 7 | lot2-B1 |
| 2609.36490v1 | **occupe en partie** (l'instrument ; deux lectures) | matrice de transfert d'une attaque sur un panel de trois sondes : la diversité d'architecture vaut contre les organismes entraînés sur une architecture, pas contre la modification amplifiée | loi sécurité(M) ; mesure de diversité effective ; variation de M | 8 | lot3-Cc |
| 2607.06596v3 | voisin (hésitation avec « occupe en partie ») | matrice « famille de calibration × famille évaluée » ; mise en commun bornée ; l'alignement géométrique prédit le transfert, causalement | M moniteurs sous attaque ; matrice d'attaques ; sondes sur l'agent | 1, 19, 21, 22 | lot3-Cd |
| 2608.16190v1 ; 2607.02514v2 | voisin | ensembles entre neuf lignées, sans gain à compétence égale ; ensembles entre types de moniteurs avec un signal non génératif | transfert d'attaque (proposition du programme, absente de l'article) | 1, 8 ; 10, 34 | lot2-B1 |
| MonitoringBench 2605.09684v1 ; SLEIGHT-Bench 2605.16626v2 | voisin | 564 des 2 644 trajectoires échappent aux treize moniteurs ; union ≈ 78,7 % contre ≈ 70 % (calcul) ; angles morts différents selon la lignée (lecture de figure) | sécurité selon M ; diversité mesurée ; sondes | 7, 40 ; 36-41 | lot3-Cd |
| 2603.13791v1 ; 2508.19461v1 ; 2602.22303v1 | voisin | moyenne 0,921, combinaison apprise 0,934, maximum 0,941 ; hybride de deux échafaudages d'un même modèle ; complémentarité de deux défenses | M variable ; diversité ; matrice | 10, 37 ; 14 ; 39 | lot3-Cc ; lot3-Ca ; lot3-Be |
| 2607.13087v1 | voisin lointain | un moniteur d'une autre famille « pourrait réduire la collusion » | matrice ; panel de sondes | 24, 25 | lot3-Ac |
| autres sources | ne touche pas | — | — | — | lot3-Be (2608.19161 : un seul moniteur), lot3-Aa, lot3-Ab, lot3-Ac (2606.17478, 2412.01784), lot3-Ca (2608.25869), lot3-Cb ; les autres rapports des lots 1 et 2 ne traitent pas H5 |

- **Reste revendicable** : la loi sécurité(M) et la diversité effective mesurée par transfert d'attaque sur un panel de sondes ; la thèse qualitative est occupée en boîte noire (2605.15377) et l'instrument l'est en partie entre sondes (2609.36490).
- **Désaccords** : lot3-Cd ramène « voisin fort » (recherche affirmative) à « voisin » pour 2607.06596 ; lot2-B1 note que « mesurer la diversité effective par transfert d'attaque » n'est pas dans 2608.16190.

## H7 — riposte et fuite d'information

| source | verdict du lecteur | composantes faites | composantes non faites | pages | rapport |
|---|---|---|---|---|---|
| 2609.36490v1 | **occupe en partie** (le mécanisme ; deux lectures) | le verdict comme canal de fuite ; dépendance causale de l'attaque aux verdicts (dz de 11,7 à 0 puis −11,8 selon la part de verdicts inversés) ; dose-réponse avec le nombre de verdicts ; verdicts bruités à 10 % : 87 % de la modification conservée | information mutuelle ; comparaison de politiques de riposte ; pente d'adaptation sur plusieurs tours ; lecture dure : les deux points ne soutiennent pas une loi linéaire en information mutuelle | 1, 7, 24 | lot3-Cc |
| 2602.22303v1 | voisin (faible) | pentes d'adaptation d'une équipe rouge automatique contre cinq défenses | politique de riposte ; fuite mesurée | 43, 45 | lot3-Be |
| MonitoringBench 2605.09684v1 | voisin | l'agent de reconnaissance reçoit la note et l'explication d'un moniteur et s'en sert (82,7 % contre 73,5 %, confondu avec l'outil et le budget) | politique de riposte ; information mutuelle | 4, 6, 27 | lot3-Cd |
| SLEIGHT-Bench 2605.16626v2 ; 2508.19461v1 ; 2607.13087v1 | voisin (qualitatif) ; voisin lointain | « chaque tentative échouée est elle-même suspecte » (argument) ; la connaissance de la surveillance par l'agent dégrade la fiabilité ; cloisonner l'information sur les protocoles | toute mesure de riposte ou de fuite | 3 ; 25 ; 17 | lot3-Cd ; lot3-Ca ; lot3-Ac |
| 2604.13301v1 (Honeypot) | ne touche pas (« pas un résultat sur H7 ») | pot de miel de contexte posé avant toute détection | riposte ; adaptation ; fuite | 1, 4, 5 | lot2-A4 |
| autres sources | ne touche pas | — | — | — | lot3-Aa (2411.17693 : corrélation discrétion / score, p. 9), lot3-Ab, lot3-Ac (2606.17478, 2412.01784), lot3-Be (2608.19161 : attaquant non adaptatif), lot3-Ca (2608.25869), lot3-Cb, lot3-Cc (2603.13791) ; les autres rapports du lot 2 ne traitent pas H7 |

- **Reste revendicable** : la pente d'adaptation prédite par la fuite d'information et sa dépendance à la politique de riposte ; le mécanisme (verdict = canal de fuite) est publié (2609.36490).
- **Désaccords** : lot3-Cc confirme le « occupe en partie (H7) » de la recherche affirmative, limité au mécanisme ; lot2-A4 corrige « Matériel de H7 » pour le protocole Honeypot.

## Statistique de population (papier B) — co-élévation d'états internes entre copies

| source | verdict du lecteur | composantes faites | composantes non faites | pages | rapport |
|---|---|---|---|---|---|
| 2608.19161v1 | voisin (la lecture « occupe en partie » tombe) | lecture d'états internes de copies d'un même modèle pour détecter une coordination | statistique de population ou co-élévation ; sondes (l'anomalie lue est surtout celle du code injecté) | 2, 4, 7 | lot3-Be |
| 2608.02698v1 | voisin | population de 4, 8 et 16 agents prévue sans mesure ; cite NARCBench (détection de collusion multi-agents par activations) : « le pendant boîte blanche n'est pas vierge selon cette source » | toute mesure (valeurs fictives) | 3, 6 | lot2-B1 |
| 2606.09931v1 | voisin ; objection conceptuelle | l'interprétabilité ne voit que des traits lisibles | mesure | 3, 4 | lot2-B1 |
| 2607.11751v1 | voisin | vue de coordination entre fragments (1,000) ; parallélisme des longueurs entre agents | états internes (textes seulement) | 4, 13 | lot3-Ab |
| 2607.13087v1 | voisin lointain | cohérence entre contextes pour l'incrimination (comportement) | co-élévation d'états internes | 6 | lot3-Ac |
| autres sources | ne touche pas | — | — | — | lot3-Cb (2508.05625 : « population-wide » = tendances d'un jeu de données, p. 6), lot3-Aa, lot3-Ab, lot3-Ac (2606.17478, 2412.01784), lot3-Be (2602.22303), lot3-Ca, lot3-Cc, lot3-Cd |

- **Reste revendicable** : la co-élévation d'états internes entre copies, lue par des sondes ; le pendant boîte blanche de la détection de collusion n'est pas vierge (NARCBench, cité par 2608.02698).
- **Désaccords** : aucun entre lecteurs ; la recherche affirmative rangeait 2608.19161 pour cet énoncé, ce que lot3-Be ramène à « voisin ».

## Papier B, énoncé non précisé par le lecteur (lots 1 et 2)

| source | verdict du lecteur | composantes faites | composantes non faites | pages | rapport |
|---|---|---|---|---|---|
| 2504.10374v1 (Ctrl-Z) | voisin (« touché partiellement, hors activations ») | surveillance par une copie non fiable du même modèle ; collusion par signal convenu ; contre-mesures (pots de miel, paraphrase) | états internes ; co-élévation ; nombre d'agents | 8 | lot2-A1 |
| 2605.26047v2 ; 2504.20271v1 | voisin (« touché faiblement ») | copies d'un même modèle et corrélation de leurs scores, en boîte noire ; un moniteur qui partage les poids pourrait colluder | états internes ; mesure | — ; 15 | lot2-A1 |
| 2602.20628v2 | voisin (« voisinage le plus proche, boîte noire ») | reconnaissance de soi entre copies, deux rôles | état interne | 3, 35 | lot2-A4 |
| 2504.05259v1 | voisin (modèle de menace conceptuel) | attaques simultanées ; collusion de sortie | mesure | 16, 19 | lot2-A4 |
| 2609.24967v2 | voisin (« papier B seulement ») | collusion comportementale entre deux instances d'un même modèle ; environnement utile | mesure interne | 9 | lot2-A2b |
| 2504.18333v1 | voisin (« contact partiel », boîte noire) | robustesse d'un comité selon sa taille (3, 5, 7) et le mélange d'architectures ; chiffres sous réserve | états internes | 7 | lot2-C2b |
| 2608.02657v2 ; 2601.09923v3 | voisin (contact ; contact faible) | une sonde d'un modèle lit les traces d'autres modèles ; redondance de modèles indépendants | co-élévation | 6 ; 17, 26 | lot2-C3b |
| 2502.01534v3 ; 2309.17012v3 ; 2404.13076v1 ; 2410.21819v2 | voisin (« voisinage » ; « adjacent ») | juge qui favorise un modèle apparenté ; biais égocentrique ; attaquant = défenseur ; familiarité par perplexité | collusion mesurée sur états internes | 4, 7 ; — ; 7 ; — | lot2-C1b ; lot2-C1a |
| 2511.09904 ; 2410.21514 | voisin (rien de mesuré) | collusion en travail futur ; modèle de menace « fermer les yeux » | mesure | 10 ; 5 | lot2-A3 |
| autres sources | ne touche pas | — | — | — | lot2-A2a (« L, T, papier B : non touchés »), lot2-A4 (2411.03336, p. 26 ; 2510.09462, p. 10), lot2-C2a, lot2-C3a |
