# Contrôle boîte blanche des menaces diffuses
## Du sabotage étalé dans le temps au sabotage distribué dans l'essaim — et à la corruption du moniteur

**Programme de recherche — v2 — 4 octobre 2026** (remplace la v1 du 14 septembre 2026)

---

## 0. Ce qui change depuis la v1

**Architecture.** Trois papiers au lieu d'un papier principal plus un papier dérivé : **A — le temps** (mono-agent), **C — l'instrument** (corruption et usurpation du moniteur), **B — l'essaim**. Le papier C, d'abord prévu comme dérivé conditionnel, est promu papier à part entière : la revue d'antériorité lui attribue les deux meilleurs scores d'originalité du programme, il est léger en calcul, il réutilise P3, et il ne dépend pas du succès de A.

**Décisions de fond (14 septembre 2026).**
1. Sondes à agrégation **max ou attention** sur les tokens, jamais moyenne ni médiane : ces dernières sont évadables par apprentissage par renforcement sur les poids, max et attention résistent.
2. Colonne vertébrale théorique : **lemme d'additivité interne + théorème négatif** (dommage porté par la marginale des scores contre dommage porté par leur corrélation) — le même objet mathématique dans le temps (A) et entre agents (B).
3. **Plan 2 × 2 accès × agrégation** pour la porte G1 : {boîte noire, boîte blanche} × {par action, séquentiel}, pour ne pas confondre le gain de l'accès interne avec celui de l'accumulation.
4. Reformulations imposées par les revues : H2 (l'application aux sondes ; le séquentiel boîte noire existe déjà), H3 (la domination de la courbe boîte blanche), H4 (seul le compromis diversification/coordination survit), H8 (prédire la robustesse par la validité), HC2 (robustesse sous attaque par contenu boîte noire ; l'immunité absolue est réfutée).
5. Ajouts : test de **transposition token → action** de la robustesse d'agrégation ; **invariants de protocole** (section 9) ; riposte = **quatre politiques + deux ablations** ; **usurpation stylistique** comme famille d'attaque nommée, avec sa prédiction propre.

**Défauts appliqués faute de contre-ordre.**
- D-a : A et C en parallèle, B ensuite.
- D-b : lemme tenté seul ; la question d'un co-auteur en analyse séquentielle est revisitée à G1.
- D-c : G1 en critère disjonctif — rappel à 1 % de faux positifs supérieur avec intervalle de confiance à 95 %, **ou** + 5 points de F1.
- D-d : papier B visé NeurIPS 2027, repli ICLR 2028.
- D-e : environnement « curation de données » sous porte G3, non ouvert.

**Re-datation (4 octobre 2026).** La phase 0 prévue au 15 septembre n'a pas démarré et la date d'entrée en cohorte est incertaine. Le calendrier est désormais exprimé en mois relatifs depuis le lancement (**M0 = 5 octobre 2026**) et ne dépend plus de l'admission ; le budget de calcul de la bourse, s'il arrive, accélère les phases 2 et 3 sans changer leur ordre.

---

## 1. Positionnement

En une phrase : agrégation **séquentielle** (dans le temps et entre agents) de scores de **sondes internes** pour détecter les **menaces diffuses** en évaluation de contrôle, y compris quand l'attaquant est une **population d'agents à poids partagés** — et mesure de la **corruptibilité** des moniteurs eux-mêmes.

La question unique des trois papiers : **que mesure vraiment un moniteur, et sa mesure survit-elle à l'adversaire ?** — à la fragmentation dans le temps (A), à la corruption de l'instrument (C), à la fragmentation entre agents (B). C'est la question de validité de construit de P3, portée au contrôle.

---

## 2. Les trois papiers

| | **A — le temps** | **C — l'instrument** | **B — l'essaim** |
|---|---|---|---|
| Problématique | Le monitoring par action échoue par construction sur le sabotage diffus : chaque action est innocente prise isolément. | Le moniteur est une surface d'attaque : plutôt que passer sous le radar, l'attaquant le déplace. Quelles architectures résistent, et peut-on mesurer la corruptibilité avant déploiement ? | Les attaques distribuées battent les moniteurs par-instance, et le moniteur global est indéployable. L'accès interne rétablit-il l'avantage, et comment décroît-il avec le nombre d'agents ? |
| Thèse | La fragmentation détruit la preuve externe, pas la preuve interne : l'accumulation séquentielle de scores de sondes détecte, avec une garantie de faux positifs toujours valide, ce que le max par action rate. | La corruptibilité est un gain mesurable ; les juges génératifs ont g > 0, structuré par famille d'attaque ; les sondes à agrégation robuste ont g ≤ 0 sous attaque par contenu ; fermer le canal rhétorique impose une taxe chiffrée ; le g bénin prédit la robustesse. | Des copies partagent leurs poids, donc leurs signatures internes co-varient : une statistique spatio-temporelle rend l'essaim plus détectable que l'agent isolé ; se décorréler coûte à l'attaquant de la capacité de coordination. |
| Figure-titre | Plan 2 × 2 accès × agrégation ; rappel en fonction de l'horizon. | g par moniteur et par famille d'attaque ; taxe de déplacement. | Sécurité en fonction de N, boîte blanche contre boîte noire. |
| Hypothèses | H1, H2, L, T, H6, Tr, H8 | HC1 à HC6 (dont HC2b) | H3, H4′, H5, H7 |
| Calendrier | M1–M2 ; papier vers M3 | M1–M3 ; papier vers M4 | M3–M6 ; papier en M7 |

---

## 3. Thèse centrale : additivité interne, lemme et théorème négatif

**Additivité interne.** La fragmentation détruit la preuve *externe* par action : chaque sortie est défendable isolément. Si l'intention laisse une trace interne à chaque contribution, la preuve *interne* s'additionne — le long du temps pour un agent, entre agents pour un essaim.

**Lemme (candidat, papier A).**
Hypothèses : (a) chaque action de sabotage déplace l'espérance du score de sonde d'au moins δ > 0 — le dommage passe par la **marginale** ; (b) le budget total de sabotage B = Σδ est borné et le dommage cumulé est une fonction croissante de B ; (c) la variance des scores honnêtes est estimable sur épisodes honnêtes.
Énoncé : pour un processus e de mélange au risque α, la puissance de détection ne dépend que de B et de la variance — pas de la répartition du sabotage sur les agents ni sur les pas de temps.

Deux précautions à traiter dans l'énoncé :
- la notion de puissance n'est pas la même sous garantie toujours valide et au sens du test séquentiel de Wald (Koning & Grünwald, arXiv 2208.07610) ;
- un adversaire couvert qui connaît la contrainte de faux positifs peut imposer un délai de détection d'ordre Θ(γ) si l'on ne contraint que la furtivité *par action* (arXiv 2601.20022) — d'où l'hypothèse (b), qui borne le budget *total*.

**Théorème négatif (papiers A et B).** Si le dommage passe par la **corrélation** à marginale préservée, toute statistique fondée sur les marginales (max, moyenne, somme cumulée) a une puissance égale au taux de faux positifs ; il faut un agrégateur d'**autocorrélation** (dans le temps) ou de **co-élévation** (entre agents). C'est le même objet mathématique dans les deux papiers : l'indexation agnostique (section 4) n'est pas une commodité de rédaction, le mode d'échec et sa parade se transposent tous les deux.

**Hypothèse empirique pivot.** Sur des organismes réalistes, le sabotage déplace-t-il la marginale des scores (δ > 0) ? Si oui, le lemme s'applique ; sinon, le théorème négatif dicte l'agrégateur. Les deux issues sont publiables.

**Antériorité à vérifier en priorité.** arXiv 2606.10456 occupe la version boîte noire et synthétique du contraste marginale/corrélation (provenance douteuse, preuves élémentaires). Différenciation : vraies activations de modèle, invariance au budget total, indexation unifiée temps/agents.

---

## 4. Cadre formel

**Jeu de contrôle** G = (E, π_B, π_R). L'environnement E produit des épisodes ; les actions a_{i,t} sont indexées par agent i ∈ {1…N} et pas t ∈ {1…T}. L'équipe rouge choisit une politique π_R sous budget de sabotage B, visant un dommage cumulé ≥ θ. L'équipe bleue observe des caractéristiques φ(a_{i,t}) incluant les activations internes h_ℓ, calcule un score par action s(a), et dispose d'agrégateurs A_temps (somme cumulée, processus e), A_pop (co-élévation), A_spatio-temporel (les deux), d'un budget d'audit b et d'interventions d'intensité λ.

- **Sécurité** = inf sur π_R de P(alerte avant que le dommage cumulé n'atteigne θ).
- **Utilité** = performance sur la tâche honnête sous π_B.
- **Indexation agnostique** : tout agrégateur opère sur le multi-ensemble {(i, t)} ; N = 1 et N = k sont le même objet mathématique.

**Corruption (papier C).** Verdict du moniteur v ∈ [0, 1], ordinal ou continu ; v₀ = verdict sans attaque ; v* = verdict voulu par l'attaquant. Loi de déférence : Δv = g · (v* − v₀), g estimé par régression sur plusieurs intensités de pression, avec un nul de régression vers la moyenne comme dans P3.
Convention : g = fraction du chemin parcourue vers le verdict voulu par l'attaquant.
- g ≈ 0 : robustesse.
- g < 0 : auto-incrimination — plaider incrimine.
- g > 0 sans accès aux poids : contamination de construit — le moniteur lit le registre, pas l'intention.

Comme la sycophancie dans P3 : la corruptibilité est un gain, pas une chose.

---

## 5. Hypothèses

Probabilités d'originalité calibrées au 14 septembre 2026, à reconfirmer par la vérification sur sources primaires (brief de phase 0, tâche T0.2).

### Papier A — le temps
- **H1 — gain blanc-sur-noir** (0,55). À agrégation égale et à taux de faux positifs égal, un moniteur fondé sur les activations détecte plus de sabotage diffus sur tâches floues qu'un moniteur boîte noire. Revendicable : la mesure spécifique diffus/flou ; le gain blanc-sur-noir en général est établi.
- **H2 — accumulation séquentielle sur sondes** (0,50). L'accumulation séquentielle toujours valide de scores de sondes détecte des sabotages dont chaque action reste sous le seuil ; le rappel croît avec l'horizon. Revendicable : l'application aux sondes internes ; le squelette séquentiel boîte noire existe.
- **L — lemme d'additivité** (0,75). Section 3.
- **T — théorème négatif** (compté avec L ; la version boîte noire synthétique est occupée, à vérifier). Section 3.
- **H6 — marge asymétrique** (0,66). Il existe une intensité d'intervention non spécifique (paraphrase, ré-échantillonnage, remise à zéro de contexte, bruit d'activations) où le succès d'attaque chute significativement plus vite que l'utilité honnête.
- **Tr — transposition token → action** (angle mort identifié, non calibré). La robustesse des agrégations max et attention, établie au niveau token, tient-elle au niveau action et trajectoire sous accumulation séquentielle, face à un attaquant adaptatif ?
- **H8 — la validité prédit la robustesse** (0,40). Le construit réellement mesuré par une sonde (intention contre conscience d'évaluation) prédit sa robustesse adverse. Le glissement de construit sous pression est déjà décrit ; la prédiction ne l'est pas.

### Papier C — l'instrument
- **HC1 — loi de déférence** (0,75). Δv = g · (v* − v₀), g stable par moniteur génératif, structuré par famille d'attaque.
- **HC2 — robustesse des sondes** (0,65 ; 0,15 dans la version « immunité absolue », abandonnée). Sous attaque par contenu boîte noire, g_sonde ≈ 0 pour une sonde à agrégation robuste.
- **HC2b — auto-incrimination** (0,70). Tenter de manipuler augmente le score de sonde. Contrôle obligatoire du style : les sondes captent souvent des corrélats de surface.
- **HC3 — usurpation** (0,55, l'originalité est portée par le versant stylistique). Les ordres en bande déplacent les juges génératifs mais déclenchent une détection quasi certaine sous le protocole « contenu = données » ; l'usurpation stylistique de l'instructeur garde un g résiduel positif sur les juges, nul sur les sondes.
- **HC4 — taxe de déplacement** (0,85). Obtenir sur une sonde le déplacement que la rhétorique obtient gratuitement sur un juge exige l'obfuscation d'activations, pour un coût supérieur de plusieurs ordres de grandeur (accès, requêtes, calcul, taux de succès).
- **HC5 — contre-mesures** (0,60). Paraphrase de confiance et quorum hétérogène, mesurés par une matrice de transfert des attaques de corruption.
- **HC6 — le g bénin prédit la robustesse** (0,80). Le g mesuré sur des corpus de pression bénins prédit l'effondrement sous attaque optimisée : critère de recette d'un moniteur avant déploiement.

### Papier B — l'essaim
- **H3 — courbe sécurité(N)** (0,45). À budget de sabotage constant, la courbe boîte blanche domine la boîte noire et décroît plus doucement avec N. Les courbes boîte noire sont publiées.
- **H4′ — compromis diversification/coordination** (la H4 d'origine est occupée, 0,30 ; seule cette partie reste revendicable). Diversifier les agents (personas, réglages fins) décorrèle leurs signatures internes mais réduit leur capacité de coordination ; le compromis est chiffrable.
- **H5 — nombre × diversité des moniteurs** (0,70). La sécurité croît avec le nombre M de moniteurs seulement via la diversité effective, mesurée par une matrice de transfert d'attaque sur un panel de sondes.
- **H7 — riposte et fuite** (0,68). La pente d'adaptation de l'équipe rouge dépend de la politique de riposte et est prédite par la fuite d'information (information mutuelle entre l'état de détection et les observations de l'équipe rouge).

---

## 6. Environnements

Critère directeur : **flou à la relecture, vérifiable en aval** (vérité terrain différée).

- **(a) Propositions d'expériences — papier A, phases 0 à 2.** Des agents rédigent et révisent des propositions d'expériences d'apprentissage automatique, notées par un évaluateur faible de confiance sur rubrique structurée. Sabotage diffus : biais systématique subtil (orienter vers des directions stériles, affaiblir les contrôles, gonfler les choix coûteux), réparti sur de nombreuses propositions. Vérité terrain : cibles semées préenregistrées + vérification différée sur sous-échantillon. Base : le jeu de Terekhov et al. (arXiv 2606.08892), porté en 8 milliards de paramètres. Exigence : décomposable en contributions (i, t) qui resservent telles quelles quand N = k.
- **(b) Pipeline de code multi-rôles — papier B, phase 3.** Codeur, testeur, relecteur ; portes dérobées fragmentées sur plusieurs commits, chaque diff restant innocent. Bases : FakeLab (Makins et al., sur demande aux auteurs) ou Iterative VibeCoding (Hills et al., cadre ControlArena, état persistant), portés en poids ouverts.
- **(d) Curation de données — extension sous porte G3.** Empoisonnement diffus par des exemples individuellement plausibles ; vérité différée = comportement d'un modèle aval entraîné sur les données curées. Ne s'ouvre que si un proxy de vérité différée fiable et bon marché est validé.
- **Transfert concentré.** En fin de phase 1, le moniteur séquentiel est testé sur un cadre de sabotage concentré (ControlArena) — une figure de robustesse, pas un chantier.

---

## 7. Organismes modèles

- **(i) Instruction cachée** dans le message système.
- **(ii) Réglage fin léger (LoRA)** inculquant la politique de sabotage sans aucune instruction à l'inférence (par distillation de contexte depuis la famille (i)).
- **(iii) Organismes publics de l'institut britannique de sécurité de l'IA** (sandbagging, dont un imitant Llama-3.1-8B-Instruct, verrouillés par mot de passe), si la licence le permet — gain de temps et comparabilité.

**Prédiction de validité.** Une sonde qui lit en réalité « j'ai une instruction cachée » réussit sur (i) et échoue sur (ii) ; une sonde d'intention réussit sur les deux.
**Contrôles croisés.** Organisme honnête averti de la surveillance (aucune mission) ; saboteur en régime simulé « non observé » — pour dissocier conscience d'évaluation et intention (alimente H8).
**Anti-circularité.** Une sonde n'est jamais entraînée et évaluée sur les mêmes organismes : entraînement sur données génériques (recettes publiées) ou sur une famille, évaluation sur une autre.

---

## 8. Moniteurs

**8.1 Sondes.** Agrégation sur les tokens : max ou attention uniquement. Familles : linéaire, différence de moyennes, petit perceptron, sonde à attention, Mahalanobis (non supervisée). Concepts : tromperie, enjeux élevés, dissimulation, conscience d'évaluation, auto-préservation. Plancher obligatoire : sonde aléatoire appariée en covariance (style P3) — une sonde qui ne le bat pas n'existe pas. Réserve de détecteurs jamais déployés, donc jamais fuités, sortis pour audit seulement.

**8.2 Diversité (H5).** Six axes : graines et données ; où lire (couches précoce, médiane, tardive ; positions ; flux résiduel contre sorties de blocs ; autoencodeurs parcimonieux Llama Scope) ; familles de sondes ; concepts et distributions de négatifs ; fenêtres d'agrégation ; hétérogénéité de type (moniteurs génératifs, détecteurs heuristiques natifs de l'environnement).
Mesure : **matrice de transfert d'attaque** — une attaque optimisée contre A réussit-elle contre B ? — et non la décorrélation des erreurs bénignes. La revue montre que choisir sur la seule décorrélation perd contre le hasard : la compétence individuelle compte. Si la diversité naturelle est insuffisante : apprentissage à corrélation négative, diversification des vulnérabilités.

**8.3 Bases boîte noire.**
- Papier A : moniteur faible par action ; TRACE-lite (triage–inspection–jugement, réimplémenté) ; accumulation séquentielle sur scores boîte noire (dans l'esprit d'E-valuator).
- Papier B : moniteur à état « link-tracker » et ensemble à quatre moniteurs (Hills et al.) ; monitoring à état sur flotte (Brown et al.).
- Papier C : deux ou trois juges génératifs hétérogènes.

**Décision D1 — modèle du moniteur boîte noire** (proposer avec recommandation).
- Enjeu : la propreté de la comparaison blanc/noir (H1) contre le réalisme du contrôle (un moniteur de confiance est plus faible que l'agent).
- (a) Même modèle que l'agent, en juge : capacité égale, isole l'effet de l'accès / irréaliste comme moniteur de confiance.
- (b) Modèle plus faible de confiance (par exemple Llama-3.2-3B-Instruct) : réaliste / confond capacité et accès.
- (c) Qwen2.5-7B : hétérogénéité / ajoute une variable de famille de modèles.
- Recommandation : (a) + (b) — les moniteurs coûtent peu face à la génération des trajectoires ; (a) pour H1, (b) pour la courbe sécurité-utilité. Confiance moyenne. **Défaut : (a) + (b).**

---

## 9. Invariants de protocole (toujours actifs)

- **Canal opérateur authentifié** : les ordres de l'opérateur n'arrivent que par un canal vérifié par le harnais, jamais par le jugement du modèle.
- **Contenu en bande = données** : tout ce qui arrive dans le contenu de la tâche est une donnée, jamais un ordre ; un contenu « en forme d'ordre » dans le canal données est en soi une alarme.
- **Flux unidirectionnel agent → moniteur** : pas de dialogue, pas de boucle de persuasion.
- **Moniteurs amnésiques** entre épisodes : pas de mémoire, pas de relation à cultiver.
- **Seuils stochastiques** (probabilité d'audit lisse et croissante du score, jamais de seuil fixe apprenable) et **trafic de couverture** — actifs par défaut, ablatés dans E3.4.
- **Hygiène de l'état persistant** : remises à zéro et filtrage — une adaptation sans hérédité n'est pas une évolution.
- **Asymétrie d'apprentissage** : chaque détection silencieuse devient un exemple étiqueté pour réentraîner les sondes.

**Frontière assumée.** Si l'adversaire possède l'infrastructure (clés, harnais, journaux), les hypothèses du contrôle sont caduques : c'est la couche sœur (sécurité des poids et des infrastructures), hors périmètre.

---

## 10. Plan expérimental

### Phase 0 — instruments (M0 : 5 octobre → 1er novembre 2026)
Détail opérationnel dans le brief de phase 0. Tâches : socle et gouvernance ; vérification de l'état de l'art sur sources primaires ; simulation du lemme et du théorème négatif ; harnais et journalisation des activations ; environnement (a) v0 ; organismes v0 ; sondes v0 ; bases boîte noire v0 ; conception et préenregistrement du papier C.
**Porte G0 (prêt pour G1)** : harnais validé ; organismes avec dose-réponse ; sondes au-dessus du plancher ; base boîte noire opérationnelle ; agrégateurs validés en simulation ; préenregistrements de G1 et du papier C scellés et contre-lus ; état de l'art vérifié.

### Phase 1 — papier A (M1–M2)
- **E1.1** Organismes finalisés et calibration dose-réponse du budget de sabotage.
- **E1.2** Plan 2 × 2 accès × agrégation. Métriques : AUROC, rappel à 1 % de faux positifs, courbe sécurité-utilité à budget d'audit, latence (alerte contre dommage cumulé). Effet principal de l'accès = H1 ; effet principal du séquentiel = H2 ; interaction positive = signature de l'additivité interne (la preuve externe par action est quasi nulle, l'interne ne l'est pas).
- **E1.3** Lemme sur données réelles : la puissance ne dépend-elle que du budget total quand la fragmentation varie ? Test de la condition δ > 0.
- **E1.4** Théorème négatif en semi-synthétique : scores honnêtes réels + structure de corrélation injectée à marginale préservée.
- **E1.5** Attaques adaptatives : (a) par contenu (consigne de rester sous le seuil, persona) ; (b) pondérales (réglage fin, puis apprentissage par renforcement au niveau action, sous GO) — test Tr.
- **E1.6** Marge asymétrique (H6). Base : Ctrl-Z.
- **E1.7** Transfert concentré (ControlArena).
- **Porte G1 (fin M2)** : boîte blanche séquentielle contre meilleure boîte noire (TRACE-lite ou séquentiel boîte noire), critère disjonctif D-c. Échec → résultat négatif publié + bascule H8 dominante.
- Livrable : papier A (arXiv + atelier), vers M3.

### Piste C — papier C (M1–M3, en parallèle de la phase 1)
- **EC.1** g des juges génératifs : cinq familles d'attaque (flatterie et supplication ; revendication d'autorité ; approbations forgées ; usurpation stylistique de l'instructeur ; ordres en bande) × plusieurs intensités ; verdicts ordinaux ou continus, lus sur texte complet.
- **EC.2** Sondes sous les mêmes attaques, plan 2 × 2 rhétorique × intention (agent honnête qui plaide sincèrement contre saboteur qui tient le même plaidoyer) : signe de g_sonde (HC2, HC2b).
- **EC.3** Usurpation : ordres en bande sous protocole « contenu = données » contre usurpation stylistique (HC3).
- **EC.4** Taxe de déplacement, côté obfuscation par réutilisation des codes d'obfuscation d'activations publiés, portés sur 8B (HC4).
- **EC.5** Contre-mesures : paraphrase de confiance, quorum hétérogène, matrice de transfert des attaques de corruption (HC5).
- **EC.6** g bénin contre robustesse sous attaque optimisée (HC6).
- **Leçons de P3 appliquées** : jamais de fenêtre tronquée pour lire un verdict (dans P3, la troncature a fabriqué un faux effet en lisant des verdicts retardés comme des verdicts changés) ; instruments ordinaux ou continus plutôt que catégoriels (le catégoriel était plat là où l'ordinal tranchait) ; nul de régression vers la moyenne dans l'estimation de g ; score continu par probabilité du jeton de verdict quand c'est possible.
- **Porte GC (fin M2)** : si g_sonde > 0 sans accès aux poids → le papier change de titre (contamination de construit), il ne disparaît pas ; si la collision arXiv 2607.08066 couvre déjà la loi de déférence → recentrage sur HC4 et HC6.
- Livrable : papier C (arXiv + atelier, puis conférence courte), vers M4.

### Phase 2 — papier B (M3–M4)
- **E2.1** Division du travail rouge, avec et sans planificateur (réplication de l'effet de fragmentation, vue interne).
- **E2.2** Collusion par canaux explicites contre coordination par poids partagés ; défenses-ingrédients : paraphrase, brouillage des canaux.
- **E2.3** Statistiques inter-agents ; les agrégateurs de NARCBench (alignement d'activations, pic de suspicion) sont assumés comme base, pas comme concurrents.
- **Porte G2 (fin M4)** : effet de fragmentation répliqué et statistique de population supérieure à l'agrégation par agent. Sinon : recentrage sur le temporel N = 1.

### Phase 3 — papier B (M4,5–M6)
- **E3.1** Statistique spatio-temporelle contre séquentiel par agent seul et contre coupe transversale (position NARCBench) — le cœur vierge.
- **E3.2** Diversification adverse → compromis décorrélation/coordination (H4′) ; transfert des sondes entre variantes ; Qwen2.5-7B comme agent hétérogène.
- **E3.3** Figure M × diversité + matrice de transfert d'attaque (H5).
- **E3.4** Riposte : quatre politiques (visible immédiate, différée randomisée, silence-puis-frappe, pot de miel) comparées par pente de sélection et fuite mesurée ; deux ablations (seuil stochastique contre fixe ; trafic de couverture contre sans) (H7).
- Bases à battre : link-tracker, ensemble à quatre moniteurs, monitoring à état sur flotte.
- **Porte G3** : ouverture de l'environnement (d) seulement si un proxy de vérité différée est validé.
- Livrable : papier B, rédaction en M7.

---

## 11. Validité de construit (transversale)

À chaque phase : panel contrastif de sondes (intention de saboter, dissimulation, conscience d'évaluation, enjeux élevés) et contrôles croisés de la section 7. Prédiction centrale (H8) : ce que mesure vraiment la sonde prédit sa robustesse adverse — une sonde de conscience d'évaluation s'effondre quand l'attaquant apprend à paraître détendu ; une sonde d'intention résiste mieux. Continuité directe avec P3 : contrôles appariés en covariance et en énergie comme plancher, et « mesurer ce que mesure la mesure » comme signature du programme.

---

## 12. Méthode (héritée de P3)

Préenregistrement scellé (SHA-256) avant toute expérience décisive ; contre-lecture par une instance qui ne l'a pas écrit ; aucun run visant un signe positif ; traitement symétrique des résultats suspects de propreté, listes d'arrêt obligatoires ; toute garde d'arrêt testée sur un cas sain et sur un artefact, aucun repli silencieux ; tout chiffre traçable (chemin de fichier + empreinte) ; la provenance par transcription n'est pas opposable — y compris les chiffres des revues d'antériorité ; discipline anti-faux-gap : un interstice est une question, et la limitation d'un papier n'est pas un trou du champ sans recherche affirmative.

---

## 13. Critères de succès et bascules pré-engagées

**Succès.** (1) Lemme et théorème négatif démontrés et testés sur activations réelles, avec le plan 2 × 2 (A) ; (2) loi de déférence et taxe de déplacement (C) ; (3) courbe sécurité(N) et compromis diversification/coordination (B) ; (4) un verdict de validité de construit valable même si H1 échoue.

**Bascules.**
- G1 échoue → résultat négatif publié + H8 dominante.
- Publication externe du cœur séquentiel sur sondes (équipe Oxford/NYU de NARCBench, équipe boîte blanche de l'institut britannique) → bascule vers l'épidémiologie de population et la curation de données.
- g_sonde > 0 → papier C sur la contamination de construit.
- 8B trop faible sur l'environnement (a) → rubrique simplifiée (changement de modèle seulement sur GO).
- Élicitation rouge insuffisante → import des politiques d'attaque publiées.
- Pas de proxy de vérité différée → environnement (d) abandonné sans coût.

---

## 14. Ressources et calendrier

**Modèles** : Llama-3.1-8B-Instruct (agents, sondes), Qwen2.5-7B (hétérogénéité, transfert), un moniteur de confiance plus faible (décision D1).
**Outils** : TransformerLens, harnais maison, ControlArena en réutilisation.
**Calcul** : Vast.ai, aucune dépense sans GO sur devis ; budget de la bourse s'il arrive.

| Période | Contenu |
|---|---|
| M0 (5 oct. → 1er nov. 2026) | Phase 0, porte G0 |
| M1–M2 | Phase 1 (A) en parallèle de la piste C (EC.1 à EC.3) ; G1 et GC en fin de M2 |
| M3 | Rédaction de A ; piste C (EC.4 à EC.6) ; début de la phase 2 |
| M3–M4 | Phase 2 (B), G2 ; rédaction de C (vers M4) |
| M4,5–M6 | Phase 3 (B), G3 |
| M7 | Rédaction de B → NeurIPS 2027 (repli ICLR 2028) ; libération du code, des organismes et des sondes |

---

## 15. Questions ouvertes

- Co-auteur en analyse séquentielle pour le lemme (revisité à G1).
- Dualité défensive du poids partagé : une copie prise en flagrant délit = toute la flotte corrigée d'un coup ; quantifiable comme valeur d'un flagrant délit ?
- Budget de fuite formalisé (borner l'information mutuelle de la politique de riposte) — antériorité à vérifier avant revendication.
- Jeu complet N attaquants × M défenseurs.
- Universalité des signatures entre familles de modèles (prudence : la forme mesurée dans P3 n'a pas transféré de Llama à Qwen).
- Déployabilité : l'argument vaut pour les laboratoires, qui ont un accès interne natif à leurs agents ; limite assumée pour les agents tiers.

---

## 16. Veille active

Hebdomadaire, rapportée seulement si elle change une revendication : suites de NARCBench (l'équipe a annoncé les tests toujours valides comme prochaine étape), équipe boîte blanche de l'institut britannique, versions de ControlArena, blog de Redwood Research, blog d'alignement d'Anthropic, et toute suite de arXiv 2607.08066 et 2606.10456.
