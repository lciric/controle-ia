# État de l'art consolidé — Contrôle boîte blanche des menaces diffuses

**Version 1 — 4 octobre 2026** — synthèse de trois revues d'antériorité du 14 septembre 2026 : (1) revue du programme initial ; (2) revue du papier C (corruption et usurpation des moniteurs) ; (3) revue des papiers A et B, hypothèse par hypothèse.

---

## 0. Statut de provenance — à lire avant tout usage

- Tout ce qui suit vient de revues automatisées : **provenance par transcription, non opposable**. Aucun chiffre n'entre dans un préenregistrement ou un papier sans vérification sur la source primaire (PDF empreinté, chemin + SHA-256).
- La plupart des références de 2026 sont des préprints non relus par des pairs ; plusieurs, parus dans les trois mois précédant les revues, ont une provenance incertaine.
- ⚠ marque un point que les revues n'ont pas pu vérifier directement.
- Les probabilités d'originalité sont des jugements calibrés au 14 septembre 2026, pas des garanties ; le champ produit plusieurs préprints pertinents par mois.
- Les revues ne concordent pas toujours (section 9) : en cas de divergence, la source primaire tranche.

---

## 1. Synthèse en une page

**Ce qui tient (revendicable).** Lemme d'additivité interne (aucune formalisation sur activations de modèle) ; taxe de déplacement rhétorique → obfuscation (aucune comparaison de coût publiée) ; g bénin comme critère de recette d'un moniteur ; loi de déférence comme coefficient continu ; environnement de curation de données comme jeu de contrôle ; matrice de transfert d'attaque sur panel de sondes ; politique de riposte comme canal de fuite ; marge asymétrique d'une intervention non spécifique en boîte blanche ; statistique spatio-temporelle temps × agents.

**Ce qui est occupé (à citer).** Agrégation inter-agents de scores de sondes en coupe transversale (NARCBench) ; accumulation séquentielle toujours valide en boîte noire (E-valuator) ; effet de fragmentation et courbes boîte noire (Makins, Hills, Brown) ; « la diversité bat le calcul » en boîte noire (Ensemble Monitoring) ; juges génératifs manipulables par la rhétorique (plusieurs travaux, dont une collision ⚠ non vérifiée) ; séparation contrôle/données contre les ordres en bande (CaMeL, hiérarchie d'instructions) ; glissement de construit des sondes sous surveillance annoncée.

**Trois conflits tranchés.** Évasion de sondes par pur contenu : non, seulement une dégradation (section 4.3). Transposition token → action de la robustesse d'agrégation : jamais testée, et bornée par la théorie de l'adversaire couvert (section 2.4). Frontière avec le monitoring à état sur flotte : nette, boîte noire sémantique contre co-élévation interne (section 3.4).

**Collisions à vérifier d'abord.** arXiv 2607.08066 (papier C) ; arXiv 2606.10456 (lemme) ; NARCBench et sa suite (papier B). Ordre complet en section 6.

---

## 2. Papier A — le temps

### 2.1 Occupé (à citer, pas à revendiquer)

- **Goldowsky-Dill, Chughtai, Heimersheim, Hobbhahn (Apollo Research)**, arXiv 2502.03407, ICML 2025 — sondes linéaires de tromperie sur Llama-3.3-70B ; AUROC de 0,96 à 0,999 selon les jeux ; environ 95 à 99 % des réponses trompeuses attrapées à 1 % de faux positifs sur conversation neutre ; les auteurs notent que la moyenne sur les tokens dilue les réponses partiellement trompeuses. → Base mono-action ; motive l'agrégation temporelle et l'abandon de la moyenne.
- **McKenzie, Pawar, Blandfort, Bankes, Krueger, Lubana, Krasheninnikov**, arXiv 2506.10805, NeurIPS 2025 — sondes « enjeux élevés » de performance comparable aux moniteurs génératifs de taille moyenne pour environ six ordres de grandeur de calcul en moins (réutilisation des activations du modèle surveillé) ; AUROC moyen supérieur à 0,91 hors distribution ; plusieurs agrégations comparées, dont une sonde à attention et ⚠ un max de moyennes glissantes. → Agrégation sur une interaction, pas sur une trajectoire multi-étapes.
- **Parrack, Attubato, Heimersheim**, arXiv 2507.12691 — définit le « gain blanc-sur-noir » (moniteur avec accès aux scores de sondes contre moniteur sans) sur sandbagging et délit d'initié, réponses isolées. → La métrique de H1 existe ; pas sur sabotage étalé.
- **Taylor et al. (institut britannique / FAR.AI)**, arXiv 2512.07810 — jeux d'audit du sandbagging : les méthodes fondées sur les internes sont plus prometteuses que la boîte noire, mais leur usage naïf est battu par des comportements introduits par l'équipe rouge ; organismes publics, dont un imitant Llama-3.1-8B-Instruct. → Confirme l'écart ; fournit des organismes réutilisables.
- **Blog de l'institut britannique sur le contrôle boîte blanche** (juillet 2025) et **« The Case for White Box Control »** (LessWrong, 2025) — posent la thèse blanc > noir, sans mesure sur diffus/flou à faux positifs égaux.
- **E-valuator (Sadhuka, Prinster, Fannjiang, Scalia, Regev, Wang)**, arXiv 2512.03109 — transforme tout score de vérificateur boîte noire en règle de décision toujours valide par processus e, avec contrôle des faux positifs à chaque pas. → Squelette séquentiel exact de H2, sans sondes.
- **Probe Trajectories (Chrabąszcz, Szymczyk, Sendera, Trzciński, Cygert)**, arXiv 2605.18549 — score de sonde par token traité comme série temporelle sur une seule chaîne de pensée, caractéristiques de traitement du signal ; le max donne des trajectoires stables là où la moyenne oscille. → Pas de trajectoire agentique, pas de test séquentiel à garantie de faux positifs.
- **TRACE (Mittapalli et al.)**, arXiv 2606.07054 — agrégation de preuves entre étapes en boîte noire (triage–inspection–jugement d'un juge génératif) sur SHADE-Arena ; F1 0,713, rappel 0,844 ⚠ contenu non lu en profondeur. → Complément boîte noire exact de H2.
- **TRACES**, arXiv 2605.27690 — modèle récurrent sur les représentations d'un **observateur séparé** qui lit la trajectoire ; le temporel bat le non-temporel ⚠. → Observateur, pas auto-activations de l'agent qui agit : c'est le pivot de la différenciation.
- **Beyond Linear Probes (Oldfield, Torr, Patras, Bibi, Barez)**, arXiv 2509.26238, ICLR 2026 — « dynamique » au sens de calcul progressif, pas de temporel ; cascade sonde → juge génératif. → Base architecturale seulement.
- **The Distributed Detectability Band (Zhang & Gao)**, arXiv 2606.10456 ⚠ provenance incertaine — tout moniteur fondé sur les marginales a une puissance égale au taux de faux positifs face à une attaque à marginale préservée ; un test séquentiel sur une corrélation de type autorégressif a une puissance qui tend vers 1 ; traces entièrement synthétiques ; preuves élémentaires ; code public. → Occupe le contraste marginale/corrélation en boîte noire synthétique ; affaiblit L et T.
- **Ctrl-Z (Bhatt, Rushing, Kaufman, Tracy, Georgiev, Matolcsi, Khan, Shlegeris — Redwood Research)**, arXiv 2504.10374 — ré-échantillonnage des actions suspectes : succès d'attaque de 58 % à 7 % pour 5 % de coût d'utilité ; meilleur protocole à 72,7 % de sécurité pour 95 % d'utilité (BashBench, 257 tâches ; modèle non fiable GPT-4o mini, modèle de confiance Llama 3.1 8B). → Base de H6 (intervention spécifique, boîte noire).
- **Retrying vs Resampling in AI Control**, arXiv 2605.26047 — compare deux intensités d'intervention, en boîte noire.
- **Fond statistique** — test séquentiel du rapport de vraisemblance de Wald ; optimalité de la somme cumulée (Lorden 1971, Moustakides 1986) ; processus e et inférence toujours valide (Howard, Ramdas, Waudby-Smith) ; **Koning & Grünwald**, arXiv 2208.07610 (la puissance sous garantie toujours valide n'est pas celle de Wald) ; **adversaire couvert en détection de rupture (Ramtin, Nain, Towsley)**, arXiv 2601.20022 (un adversaire qui connaît la contrainte de fausses alarmes peut imposer un délai d'ordre Θ(γ)) ; attaques furtives sur systèmes cyber-physiques qui gardent chaque résidu sous le seuil, arXiv 2005.07821. → Aucun appliqué à des activations de modèle.
- **Pressure-Testing Deception Probes (Kumar)**, arXiv 2605.27958, ACL 2026 — rejette l'hypothèse d'une direction unique (AUROC 0,61 à 0,80 avec une seule direction) ; effondrement sous changement de style, récupéré par augmentation de style (environ 0,98) ; les sondes multidimensionnelles récupèrent le signal ; la sonde détecte très bien le régime de consigne trompeuse. → Occupe une partie de H8 ; soutient HC2b avec une réserve sur les corrélats de surface.
- **You Can't Escape Your Own Activations (Das, Ponde, More, Gupta)**, arXiv 2609.03035 — glissement intention → conscience d'évaluation étudié sous surveillance annoncée (voir 3.1). → Occupe une partie de H8.

### 2.2 Ouvert (revendicable)

- Lemme d'additivité interne sur activations réelles, indexation unifiée temps/agents, condition explicite de non-décorrélabilité dommage/furtivité.
- Accumulation séquentielle toujours valide sur scores de **sondes internes** — explicitement laissée ouverte par NARCBench.
- Plan 2 × 2 accès × agrégation sur sabotage diffus à taux de faux positifs égal.
- Transposition token → action de la robustesse des agrégations max et attention sous accumulation séquentielle.
- Marge asymétrique d'une intervention non spécifique, lue en boîte blanche.
- Prédiction de la robustesse d'une sonde par sa validité de construit.

### 2.3 Bases chiffrées à battre (toutes ⚠ jusqu'à vérification)

| Base | Chiffre | Source |
|---|---|---|
| TRACE (boîte noire, inter-étapes) | F1 0,713 ; rappel 0,844 | arXiv 2606.07054 |
| Ctrl-Z (ré-échantillonnage) | 72,7 % de sécurité à 95 % d'utilité | arXiv 2504.10374 |
| Sondes de tromperie Apollo (mono-action) | AUROC 0,96 à 0,999 | arXiv 2502.03407 |
| Sondes « enjeux élevés » | AUROC moyen > 0,91 hors distribution | arXiv 2506.10805 |

### 2.4 Conflit tranché — l'agrégation

- **Établi** : au niveau token, les sondes à max ou à attention résistent à l'évasion par apprentissage par renforcement sur les poids, sans gradient à travers le moniteur ; la moyenne, la médiane et les scores par token cèdent (RL-Obfuscation, Gupta & Jenner, arXiv 2506.14261).
- **Jamais testé** : la même robustesse au niveau action ou trajectoire, sous accumulation séquentielle.
- **Borne théorique** : un adversaire couvert qui connaît la contrainte de faux positifs peut rendre la somme quasi invisible si l'on ne contraint que la furtivité par action (arXiv 2601.20022 ; analogue cyber-physique arXiv 2005.07821) ; et dommage et furtivité sont décorrélables quand le dommage passe par la corrélation (arXiv 2606.10456).
- **Décision** : agrégation max ou attention par action ; budget total borné dans l'énoncé du lemme ; non-décorrélabilité dommage/furtivité posée comme hypothèse testable ; théorème négatif ajouté ; test de transposition dédié.

---

## 3. Papier B — l'essaim

### 3.1 Occupé (à citer, pas à revendiquer)

- **Makins, Angelini, Shams, Phuong (institut britannique / MATS)**, arXiv 2607.07368 — effet de fragmentation : plus les agents coordonnés sont nombreux, moins les moniteurs par-instance détectent ; ce n'est pas une simple dilution (un moniteur conjoint sur les commits recombinés reste à une suspicion d'environ 0,91, quasi plate en N) ; un planificateur explicite multiplie jusqu'à sept fois la réussite d'attaque ; environnement FakeLab (9 services, 86 tâches bénignes, 4 objectifs d'attaque) partagé sur demande ; défenses boîte noire uniquement ; collusion et moniteur non fiable laissés à plus tard. → Complément attaque exact de la phase 3.
- **Hills, Caspary, Cooper Stickland**, arXiv 2607.02514 — attaques graduelles réparties sur des demandes de fusion successives dans un code persistant (Iterative VibeCoding) ; moniteur à état « link-tracker » ; un ensemble de quatre moniteurs fait passer l'évasion graduelle de 93 % à 47 % pour moins de 2 % de faux positifs ; code dans ControlArena. → Base de l'environnement (b), boîte noire.
- **Brown et al. (Penn / CMU)**, arXiv 2605.31593 — première attaque distribuée multi-agents implémentée, attrapée environ cinq fois moins souvent que les attaques antérieures ; moniteur en ligne à état par regroupement d'embeddings entre transcriptions et comptes : rappel de campagne de 81 à 87 % pour environ 2,4 à 3,1 % de faux positifs, contre 75 % pour un moniteur standard, et détection environ 30 % plus tôt. → Agrégation au niveau flotte, boîte noire.
- **The Best-Laid SCHEMEs**, arXiv 2605.29178 — sabotage coordonné multi-agents ; avertir les agents de la surveillance réduit leur capacité plus que leur détectabilité.
- **NARCBench (Rose, Cullen, Kaplowitz, Schroeder de Witt — Oxford / NYU)**, arXiv 2604.01151 — détection de collusion cadrée comme détection d'anomalie distribuée ; cinq agrégations de scores de sondes entre agents (concaténation triée, alignement d'activations par similarité cosinus, pic de suspicion, partage de tromperie, sonde d'asymétrie) ; AUROC 1,00 en distribution ; transfert zéro-shot ⚠ divergent selon les revues (section 9) ; 0,99 à 1,00 sur collusion stéganographique là où le juge textuel échoue ; tests séquentiels toujours valides cités comme prochaine étape, non réalisés ; code et données publics. → **Occupe la H4 d'origine** ; agrégation en coupe transversale par épisode.
- **Das, Ponde, More, Gupta**, arXiv 2609.03035 — des agents informés de la surveillance de leurs activations, même avec le score du tour précédent, n'échappent pas à la détection (AUROC environ 0,91 à 1,00) ; populations homogènes et mixtes ; coupe transversale par épisode.
- **Ghanem & Keele**, arXiv 2608.02698 — détection de collusion au niveau population, explicitement boîte noire et inter-mandants (information mutuelle entre exécutions, tests de permutation). → Délimite la frontière ; le pendant boîte blanche reste ouvert.
- **Koran, Yun, Tetef, Arnav, Bernabeu-Perez (Yale / SPAR)**, arXiv 2605.15377 — le meilleur ensemble de trois moniteurs diversifiés donne 2,4 fois le gain de trois moniteurs identiques ; 94,6 % des ensembles diversifiés de cinq battent un appel unique à un grand modèle à coût égal ; tous les moniteurs partagent le même modèle de base ; ensembles inter-familles et non génératifs laissés à plus tard ; code public. → Thèse qualitative de H5 occupée en boîte noire.
- **Decorrelation Is Not Complementarity**, arXiv 2608.16190 — la compétence, pas la lignée, gouverne les ensembles de moniteurs ; sélectionner sur la seule diversité perd contre le hasard. → Impose de mesurer la diversité *effective* (transfert d'attaque), pas la décorrélation brute.
- **TraceGuard**, arXiv 2604.03968 — notation structurée à cinq axes, résistante à la collusion (ControlArena) ; scores moyens honnête 0,206 contre attaque 0,616 ; 95 % de sécurité au seuil 0,5 contre 0 % pour une surveillance non fiable à score unique ; boîte noire.
- **Adaptive Attacks on Trusted Monitors (Terekhov, Panfilov et al.)**, arXiv 2510.09462, ICLR 2026 — un attaquant qui connaît protocole et moniteur l'évade en glissant des injections dans ses sorties (principe de Kerckhoffs).
- **Hopman et al. 2025** (« Untrusted AIs Can Exploit Feedback in Control Protocols ») — le raisonnement du moniteur renvoyé en retour permet à l'attaquant d'itérer vers des attaques plus furtives. → Mécanisme de fuite, non formalisé en information mutuelle.
- **Catching AIs Red-Handed** (Greenblatt & Shlegeris, Redwood, 2024) ; **Honeypot Protocol**, arXiv 2604.13301 ; **Games for AI Control** (Griffin et al., 2024 — jeux de Stackelberg, stratégies mixtes). → Matériel de H7.

### 3.2 Ouvert (revendicable)

- Courbe sécurité(N) boîte blanche qui domine la boîte noire et décroît plus doucement.
- Statistique spatio-temporelle (temps × agents) : la combinaison n'existe pas.
- Compromis chiffré entre diversification adverse et capacité de coordination.
- Matrice de transfert d'attaque sur un panel de sondes (couches × familles × concepts × fenêtres).
- Politique de riposte comme canal de fuite mesuré par information mutuelle.
- Environnement de curation de données comme jeu de contrôle. Adjacents seulement : sabotage subtil par des chercheurs automatisés (Anthropic, mars 2025 — Claude 3.7 Sonnet ramène sa performance au niveau d'un modèle plus faible sans hausse de suspicion ; l'orientation des décisions fait chuter la précision des juges d'environ 70 % à 20–35 %) ; empoisonnement par environ 250 documents, quasi constant de 600 millions à 13 milliards de paramètres (Anthropic, institut britannique, Alan Turing Institute, arXiv 2510.07192).

### 3.3 Bases chiffrées à battre (toutes ⚠)

| Base | Chiffre | Source |
|---|---|---|
| Ensemble à quatre moniteurs (link-tracker) | évasion graduelle 93 % → 47 % ; faux positifs < 2 % | arXiv 2607.02514 |
| Monitoring à état sur flotte | rappel de campagne 81–87 % à ~2,4–3,1 % de faux positifs | arXiv 2605.31593 |
| Planificateur (attaque) | réussite d'attaque jusqu'à × 7 | arXiv 2607.07368 |
| Ensembles diversifiés (boîte noire) | gain × 2,4 contre moniteurs identiques | arXiv 2605.15377 |
| Agrégation inter-agents de sondes | AUROC 1,00 en distribution | arXiv 2604.01151 |

### 3.4 Conflit tranché — frontière avec le monitoring à état sur flotte

- Brown et al. agrègent en boîte noire la **similarité sémantique** entre transcriptions et comptes : « les requêtes se ressemblent-elles ? ».
- La statistique de population du programme agrège la **co-élévation des états internes** entre copies : « les états internes montent-ils ensemble ? » — un signal invisible dans le texte (sur la collusion stéganographique, NARCBench rapporte un juge textuel au niveau du hasard contre des sondes quasi parfaites).
- Aucune suite boîte blanche connue de Brown et al.
- **Décision** : le papier B se positionne comme le complément boîte blanche explicite ; l'attaque distribuée de Brown sert de banc d'essai.

---

## 4. Papier C — l'instrument

### 4.1 Occupé (à citer, pas à revendiquer)

- ⚠ **Persuasion Attacks Can Decrease Effectiveness of CoT Monitoring**, arXiv 2607.08066 — persuader un moniteur de chaîne de pensée d'approuver des actions contraires à la politique, par argumentation à l'inférence ; **jamais vérifié directement**. → Collision la plus sérieuse : versant génératif de HC1 et de HC3.
- **Kim et al.**, arXiv 2606.14037 — plan factoriel à trois intensités, 9 modèles, 972 000 réponses ; les modèles suivent davantage les incitations utiles que nuisibles sur les questions factuelles (ratio d'asymétrie 1,58) mais presque également sur les questions morales (1,04). → Dose-réponse en taux de conformité, pas en gain par moniteur.
- **The Silent Judge**, arXiv 2509.26072 — taux de déplacement de verdict (binaire par condition ; par exemple + 30 % d'effet de récence pour un grand modèle).
- **Nogueira et al.**, arXiv 2604.21564 — sycophancie directe de 22 % à 71 %, indirecte de 41 % à 78 % sur cinq tours ; trajectoire non paramétrée en gain.
- **Catalogues de biais** : SycEval ; PARROT, arXiv 2511.17220 ; Who Endorsed It?, arXiv 2601.13433 (autorité par niveau d'expertise) ; Faithful or Fabricated?, arXiv 2605.23970. → Fournissent des familles d'attaque, pas le coefficient.
- **Meincke, Shapiro, Duckworth, Mollick, Mollick, Van den Bulte, Cialdini**, PNAS 2026 — les principes de persuasion font passer la conformité de 35,3 % à 51,3 % sur 126 000 conversations. → Taux binaire.
- **Attaques par suffixes optimisés** (autre modèle de menace, à ne pas confondre avec la pression sociale) : JudgeDeceiver, arXiv 2403.17710 (CCS 2024) ; arXiv 2505.13348 ; arXiv 2402.14016 ; arXiv 2504.18333 ; systématisation arXiv 2603.29403.
- **Évasion de sondes avec accès fort** : **Bailey et al.**, arXiv 2412.09565, ICLR 2026 (sur Llama-3-8B-Instruct, le rappel de sondes de nocivité tombe de 100 % à 0 % à 1 % de faux positifs tout en gardant environ 90 % de contournement ; « taxe d'obfuscation » sur une tâche SQL, croissante avec le nombre de couches obfusquées ; code public) ; **Neural Chameleons (McGuinness, Serrano, Bailey, Emmons)**, arXiv 2512.11949 (auto-obfuscation apprise par réglage fin, généralisée à des concepts non vus) ; **RL-Obfuscation (Gupta & Jenner)**, arXiv 2506.14261 (apprentissage par renforcement sur les poids ; moyenne, médiane et par-token vulnérables ; max et attention robustes).
- **Dégradation sans évasion par pur contenu** : **Blandfort & Graham**, arXiv 2511.00554 ⚠ non lu directement (red-teaming boîte noire par apprentissage en contexte ; le jargon juridique induit des faux positifs, un ton procédural neutre des faux négatifs ; vulnérabilités réduites mais persistantes ; conclut qu'une sonde ne doit pas être un point de contrôle unique à enjeux élevés).
- **Supériorité des sondes hors attaque** : When Benchmarks Lie, arXiv 2602.14161 (à faux positifs bénins égaux, les sondes battent plusieurs classifieurs et juges génératifs sur attaques indirectes et agentiques, sous changement de distribution) ; Goodfire 2025 (sondes contre juge génératif, données propriétaires) ; Tillman & Mossing, arXiv 2504.20271 (une sonde non promptée ne peut pas servir de déclencheur de collusion — germe de l'argument d'immunité, non développé).
- **Détection d'injection par états internes** : InstructDetector, arXiv 2505.06311 ; TaskTracker (Abdelnabi et al.) ; Attention Tracker ; PIShield ; arXiv 2608.02657 ; arXiv 2606.22864 ; ESLD, arXiv 2605.18918 ; RouteGuard, arXiv 2604.22888 ; **Prompt Injection as Role Confusion**, arXiv 2603.12277 (sondes de rôle : l'écart entre rôle architectural et rôle perçu détecte l'injection — le travail le plus proche de l'usurpation stylistique). → Injection en bande couverte ; corruption rhétorique non couverte.
- **Séparation contrôle/données** : hiérarchie d'instructions (Wallace et al., OpenAI) ; CaMeL (Debenedetti et al., Google DeepMind — attaques réussies quasi nulles sur AgentDojo, au prix d'une utilité de 77 % contre 84 % et d'environ 2,8 fois plus de tokens) ; motif du double modèle (Willison) ; spotlighting ; Fides ; arXiv 2601.09923 ; arXiv 2505.22852. → Couvre les ordres en bande de HC3.
- **Contrôle** : TraceGuard ; Adaptive Attacks on Trusted Monitors ; When can we trust untrusted monitoring?, arXiv 2602.20628 ; **esquisses de safety cases (Balesni, Korbak et al.)**, arXiv 2411.03336 (un protocole combinant surveillance non fiable et sondes boîte blanche pour résister à la collusion du moniteur — antériorité directe sur « sondes dans un protocole de contrôle ») ; How to evaluate control measures, arXiv 2504.05259 (les méthodes boîte blanche risquent de surapprendre : on n'a pas d'échantillon d'internes d'un vrai comploteur).
- **Coût d'attaque** (contournement d'alignement, pas évasion de moniteur) : PAIR environ 85 requêtes ; GPTFuzzer environ 45 requêtes ; NOICE environ 85 dollars.

### 4.2 Ouvert (revendicable)

- Gain g continu par moniteur et par famille d'attaque (transposition de la loi d'attraction de P3).
- Opposition sonde/juge point par point sous corruption par contenu.
- Auto-incrimination comme résultat central (seulement effleurée par 2609.03035 et 2605.27958).
- Taxe de déplacement chiffrée.
- g résiduel de l'usurpation stylistique.
- g bénin comme prédicteur de robustesse adverse.
- Matrice de transfert des attaques de corruption ; paraphrase comme contre-mesure à la corruption rhétorique (elle existe comme défense anti-stéganographie, pas contre la persuasion).

### 4.3 Conflit tranché — évasion de sondes par pur contenu

- Toutes les évasions propres publiées exigent des gradients, un réglage fin ou un apprentissage par renforcement sur les poids (Bailey, Neural Chameleons, RL-Obfuscation).
- Le seul travail par pur contenu dégrade sans évader (Blandfort & Graham).
- Les agents informés de la surveillance n'échappent pas (2609.03035).
- **Conditions** : l'évasion est possible quand l'attaquant a accès aux poids ou aux gradients **et** que la sonde agrège par moyenne, médiane ou par token ; la robustesse vaut pour un attaquant boîte noire en contexte, avec une agrégation robuste et des concepts à forte structure linéaire (tromperie, enjeux élevés).
- **Réserve** : les sondes captent souvent le régime de consigne ou des corrélats de surface (2605.27958 ; ⚠ arXiv 2606.07612) — contrôler le style dans toute mesure de HC2b.
- **Décision** : HC2 formulée en robustesse sous attaque par contenu boîte noire, jamais en immunité absolue.

---

## 5. Revendications interdites

Établies ailleurs ; on les cite, on ne les revendique pas :
- « Les sondes battent les juges génératifs » (en général).
- « Les sondes sont immunisées » — réfuté par l'obfuscation à accès fort.
- « Les juges génératifs sont manipulables par la rhétorique » (dont ⚠ 2607.08066).
- « La paraphrase aide » ; « les comités ou ensembles aident » ; « la diversité bat le calcul » (en boîte noire).
- « Les ordres en bande se bloquent par séparation contrôle/données ».
- « La fragmentation casse les moniteurs par-instance ».
- « Le monitoring à état attrape les attaques distribuées » (en boîte noire).
- « La co-élévation de sondes entre agents détecte la collusion ».
- « Un test séquentiel toujours valide sur trajectoires d'agents » (en boîte noire).
- « Le score de sonde comme série temporelle » (sur une chaîne de pensée).
- « Les moniteurs fondés sur les marginales échouent contre les attaques à marginale préservée » (en boîte noire synthétique, ⚠ provenance).
- « Le construit d'une sonde glisse de l'intention vers la conscience d'évaluation sous surveillance annoncée ».

---

## 6. Collisions à vérifier, dans l'ordre

| # | Référence | Ce qu'elle menace | Ce qu'il faut établir |
|---|---|---|---|
| 1 | arXiv 2607.08066 | HC1, HC3 (versant génératif) | Existence, date, contenu exact ; mesure-t-elle un gain continu ou un taux ? |
| 2 | arXiv 2606.10456 | L, T | Provenance, solidité des preuves, nature exacte de l'énoncé ; code réutilisable ? |
| 3 | arXiv 2604.01151 et 2609.03035 | H4, H2, HC2b | Agrégation en coupe transversale ou séquentielle ; chiffres de transfert ; statut de la « prochaine étape » séquentielle |
| 4 | arXiv 2512.03109 | H2 | Périmètre exact (boîte noire seulement ?) |
| 5 | arXiv 2606.08892 | Environnement (a) | Code et données publics ? Licence ? |
| 6 | arXiv 2606.14037 | HC1 | Plan dose-réponse : gain ou taux ? |
| 7 | arXiv 2606.07054, 2605.27690, 2605.18549 | H1, H2 | Contenus non lus en profondeur |
| 8 | arXiv 2506.10805 | H2 | Existence et définition du max de moyennes glissantes |
| 9 | arXiv 2605.15377, 2608.16190 | H5 | Ensembles inter-familles ou non génératifs déjà testés ? |
| 10 | arXiv 2607.07368, 2607.02514, 2605.31593 | H3, bases de B | Chiffres ; accès à FakeLab ; code ControlArena |
| 11 | arXiv 2504.10374 | H6 | 72,7 % comme résultat principal |
| 12 | arXiv 2606.07612, 2511.00554 | H8, HC2 | Contenu, non lu directement |

---

## 7. Codes, données et environnements réutilisables

Disponibilité et licence à vérifier pour chacun.

| Ressource | Usage dans le programme |
|---|---|
| ApolloResearch/deception-detection | Sondes de tromperie (T0.7) |
| arrrlex/models-under-pressure | Sondes « enjeux élevés » (T0.7) |
| aaronrose227/narcbench (GitHub + jeu de données HuggingFace) | Base inter-agents du papier B |
| LukeBailey181/obfuscated-activations | Côté obfuscation de la taxe de déplacement (EC.4) |
| Code de RL-Obfuscation (via OpenReview) | Attaque pondérale au niveau action (E1.5) |
| AI-Safety-Institute/sandbagging_auditing_games | Organismes famille (iii) |
| FakeLab (sur demande aux auteurs de 2607.07368) | Environnement (b) — message à rédiger, Lazar l'envoie |
| ControlArena, BashArena, Iterative VibeCoding | Environnement (b), transfert concentré |
| Multi-Signal-Control-SPAR | Base d'ensembles de moniteurs (H5) |
| Gyyz/distributed_sabotage_frontier | Attaque synthétique à marginale préservée (T0.3, E1.4) |
| ShiJiawenwen/JudgeDeceiver | Base « suffixe optimisé », modèle de menace orthogonal (C) |
| Ctrl-Z / BashBench | Base de H6 |
| Terekhov et al., arXiv 2606.08892 | Environnement (a) — code et données à vérifier |
| PARROT, SycEval, corpus de Meincke et al., plans de Kim et al. | Familles et intensités d'attaque (C) |
| Llama Scope | Autoencodeurs parcimonieux pour Llama-3.1-8B (diversité, H5) |
| SHADE-Arena | Transfert concentré seulement : 5 paires de tâches publiques sur 17, plafond des modèles de pointe autour de 27 % |

---

## 8. Probabilités d'originalité (calibrées au 14 septembre 2026)

| Hypothèse | Papier | Probabilité | Justification en une ligne |
|---|---|---|---|
| H1 gain blanc-sur-noir | A | 0,55 | Établi en général ; pas mesuré sur diffus/flou à faux positifs égaux |
| H2 séquentiel sur sondes | A | 0,50 | Fait en boîte noire (E-valuator) ; reste l'application aux sondes |
| L lemme d'additivité | A | 0,75 | Jamais formalisé sur activations ; sous réserve de la non-décorrélabilité |
| H6 marge asymétrique | A | 0,66 | Courbes connues pour interventions spécifiques, pas en boîte blanche non spécifique |
| H8 validité → robustesse | A | 0,40 | Glissement de construit décrit ; la prédiction ne l'est pas |
| H3 sécurité(N) | B | 0,45 | Courbes boîte noire publiées ; reste la domination boîte blanche |
| H4 co-élévation (d'origine) | B | 0,30 | Occupée par NARCBench ; seul le compromis H4′ survit |
| H5 nombre × diversité | B | 0,70 | Thèse qualitative occupée ; matrice de transfert sur sondes vierge |
| H7 riposte et fuite | B | 0,68 | Exploitation du retour documentée, jamais formalisée en information mutuelle |
| Environnement (d) | B | 0,72 | Aucun jeu de contrôle de curation avec vérité différée |
| HC1 loi de déférence | C | 0,75 | Dose-réponses en taux ; aucun gain stable par moniteur |
| HC2 robustesse des sondes | C | 0,65 (0,15 en immunité absolue) | Opposition sonde/juge sous corruption jamais faite |
| HC2b auto-incrimination | C | 0,70 | Suggérée, jamais posée comme résultat central |
| HC3 usurpation | C | 0,55 | Ordres en bande couverts ; versant stylistique vierge |
| HC4 taxe de déplacement | C | 0,85 | Aucune comparaison de coût publiée |
| HC5 contre-mesures | C | 0,60 | Paraphrase et ensembles connus ; matrice de transfert de corruption neuve |
| HC6 g bénin → robustesse | C | 0,80 | Critère de recette non publié |

---

## 9. Divergences entre revues, à trancher sur source primaire

- **Transfert zéro-shot de NARCBench** : 0,60 à 0,86 selon la première revue ; 0,73 à 0,93 sur Llama-3.1-70B selon les deux autres (peut-être tous modèles confondus contre un seul modèle).
- **Ctrl-Z** : 72,7 % de sécurité à 95 % d'utilité est le résultat principal ; un 83,2 % cité ailleurs correspondrait à une variante.
- **Rappel des sondes Apollo à 1 % de faux positifs** : « 95 à 99 % » ou « plus de 96 % » selon les revues.
- **Max de moyennes glissantes** dans McKenzie et al. : mentionné par une revue, non confirmé par les autres.
