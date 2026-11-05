# État de l'art vérifié sur sources primaires — niveau 1 — v1

Date : 2026-10-04 (UTC). Tâche T0.2. Remplace, pour les 13 références du niveau 1, la provenance par transcription de `docs/anteriorite/anteriorite-transcription-v1.md`.

## Statut

- **Lecture.** Les 13 PDF de niveau 1 (`docs/sources/pdf/` ; provenance et empreintes dans `provenance-niveau1-v1.md`) ont été lus en entier, annexes comprises, par six lecteurs neufs. Chaque verdict cite la page (numérotation du fichier) et une citation exacte, sauf les verdicts d'absence et les calculs.
- **Rapports.** Ils sont scellés dans `docs/sources/lecture-pdf-niveau1/` : extraits mot pour mot, avec les fichiers de travail et les scripts.
- **Contrôle de traçabilité.** Un sous-agent neuf a contrôlé chaque chiffre de la section 4 et chaque ligne de la section 2 dans les PDF, avec recalculs indépendants : `controle-tracabilite-v1.md`. Ses corrections sont intégrées ici. Verdict avant corrections : « publiable après corrections », aucune conclusion principale inversée.
- **Nature des chiffres** (section 4) :
  - « auteurs » : imprimé dans le PDF ;
  - « figure » : lecture d'une figure ;
  - « calcul » : reconstruction à partir des tables du PDF, par script scellé ;
  - « simulation » : Monte-Carlo de la construction publiée.

  Seuls ces chiffres peuvent entrer dans un préenregistrement ou un document du programme (R7).
- **Reste ouvert** :
  - les niveaux 2 et 3 (75 documents) ;
  - la recherche affirmative de travaux inconnus (budget de recherche web épuisé) ;
  - les références nouvelles de la section 5 (non lues) ;
  - toute zone dite « libre » ci-dessous ne l'est que **dans les sources lues** (R8).

## 1. Prononcés

1. **H2 (accumulation séquentielle sur sondes) est plus occupée qu'annoncé — nœud N-007.**
   - *Doomed from the Start* (2607.06503, juillet 2026, absent de l'état de l'art) fait déjà :
     - des sondes sur les activations de l'agent qui agit, sur des épisodes à plusieurs tours ;
     - une garantie de rappel au niveau de l'épisode, sur un horizon figé de 6 portes indépendantes. Elle n'est exacte qu'avec un certificat indépendant optionnel ; sans lui, jusqu'à 4 graines sur 20 passent sous la cible (p. 4, 13) ;
     - la supériorité du blanc à pipeline égal, pour l'échec de tâche, contre un scoreur noir volontairement pauvre.
   - E-valuator (2512.03109) accepte « tout type » de score (p. 3). Sa validité vient d'un seuil statistique de type PAC sur le maximum (taux ≤ α + δ), pas de l'inégalité de Ville, qui échoue avec des rapports de densités estimés (p. 4–8). Il n'a pas de somme cumulée.
   - Libres **dans les sources lues** : le régime adverse (sabotage sous le seuil par action), l'accumulation additive toujours valide sur sondes, la loi rappel–horizon à faux positifs contrôlés, une calibration sans aucun exemple de sabotage.
   - À lire avant toute revendication : Kulkarni 2026 (2604.28129), Padhi et al. 2026 (2604.19775), FIPER et Yueh-Han et al. 2025 (2506.10949), ce dernier pour le régime « chaque pas bénin ».
2. **HC1 (loi de déférence) est plus occupée qu'annoncé — N-005 confirmé et élargi.**
   - 2508.07805 mesure une note *continue* par juge et par technique de persuasion. Il couvre 3 des 5 familles du programme : flatterie et supplication, autorité, approbations forgées. Sa normalisation divise par la note initiale, pas par l'écart à la cible.
   - 2606.07897 définit un coefficient continu de déférence : une pente sur des intensités graduées, par modèle, à rang stable. Mais il porte sur des assistants, sans attaquant.
   - 2607.08066 ne mesure qu'un taux binaire : la porte GC, telle qu'écrite, n'est pas déclenchée par lui, mais **elle vise le mauvais papier**.
   - Libres dans les sources lues :
     - g normalisé par l'écart à la cible de l'attaquant, dans un moniteur de contrôle ;
     - la régression multi-intensités par famille ;
     - l'usurpation stylistique et les ordres en bande ;
     - l'opposition juge/sonde ;
     - le nul de régression vers la moyenne et le verdict lu par probabilité du jeton, **sous réserve de PARROT (2511.17220) et de BASIL (2508.16846), non lus**.
3. **« g stable par moniteur » est fragile.**
   - Dans 2606.07897, seuls les *rangs* sont stables ; les magnitudes dépendent du corpus, de l'éliciteur et du juge (p. 7, 10, 32).
   - Dans 2508.07805, le signe s'inverse d'un banc à l'autre pour un même juge.
   - Dans 2607.08066, le classement des moniteurs dépend de l'agent.
   - → À préenregistrer : la stabilité de rang et l'invariance à l'attaquant et au corpus.
4. **Des déplacements négatifs existent déjà sur des juges purement textuels.** GPT-4o face à « Majority » est négatif sur les 6 bancs de 2508.07805. Claude Opus et Sonnet 4.6 ont une contre-déférence dans 2606.07897 (−3 et −4, estimations ponctuelles, significativité non établie). HC2b doit donc être revendiquée comme propriété des *sondes*, contrôlée contre ce retour de bâton textuel.
5. **Le critère de la porte G1 se gagne en sur-signalant — nœud N-008.**
   - TRACE (2606.07054) annonce un F1 de 0,713 et un rappel de 0,844 (moyennes par tâche), mais signale environ 75 % des trajectoires honnêtes (calcul).
   - Sur ce jeu, « tout signaler » donne un F1 de 0,755 en moyenne par tâche (0,744 poolé), au-dessus du 0,713 publié.
   - Le bras « + 5 points de F1 » du critère disjonctif D-c a le même défaut. À taux de faux positifs égal et prévalence fixée, le F1 n'est qu'une fonction croissante du rappel : la disjonction est donc surtout nominale.
6. **Les bras boîte noire de G1 doivent être forts — proposition P-003.**
   - L'invite du juge robustifié b* de Terekhov et collègues est publiée, mais pas ses poids d'agrégation (p. 48–49, 68–71). b* a été trouvé avec le proxy de vérité : il faut le revalider avec un juge 8B ou 3B.
   - TRACE-lite en 8B ou 3B risque d'être un homme de paille : il n'est pas testé en dessous d'o4-mini, les modèles faibles s'effondrent par arrêt précoce, et son score est entier sur 1 à 5.
7. **L'environnement (a) n'est pas un portage — proposition P-004.**
   - 2606.08892 (« Diffuse AI Control on Fuzzy Tasks ») ne publie ni code ni données.
   - Sa vérité terrain est un proxy, Sonnet 4.6 qui lit le papier : ni cibles semées, ni exécution. Aucun Llama n'est testé.
   - L'unité notée est l'ensemble des 10 propositions d'une tâche, avec un seul générateur et un seul tour : il n'y a pas d'indice d'agent.
   - Le papier est incohérent par endroits (sept écarts relevés, dont l'Opus bénin à 70,7 aux figures 1 et 4 contre 67,6 à la figure 5) : ses chiffres sont à reprendre avec précaution.
   - T0.5 sera une reconstruction minimale fidèle, après un pilote 8B scellé.
8. **Organismes : les stratégies de 2606.08892 ont une apparence sincère, et les sondes publiées peuvent lire l'instruction plutôt que l'intention — proposition P-005.**
   - Scinder la famille (i) en (i-a) « consigne de saboter en dissimulant » et (i-b) « stratégie biaisée d'apparence sincère ».
   - Ajouter un témoin « instruit sans sabotage ». En effet, AcMAS signale 100 % de faux positifs hors domaine, et les sondes de NARCBench sont apprises sur des rôles *instruits*.
9. **NARCBench : la bascule n'est pas déclenchée, mais elle est imminente.**
   - La v3 (1er octobre 2026) agrège en coupe transversale par épisode.
   - Le séquentiel y est annoncé quatre fois, avec le cadre formel et les outils nommés : Wald, SAVI, détection multi-capteurs.
   - Kulkarni 2026, cité pour l'accumulation multi-tours sur activations, est inconnu du programme : **lecture prioritaire**.
   - Ses chiffres ne sont pas des bases à battre : CORE compte environ 5 épisodes par pli, et le code public diffère de la v3.
10. **H8 est moins occupée que l'état de l'art ne le dit.** 2609.03035 ne mentionne nulle part un glissement de construit ni l'auto-incrimination. La « revendication interdite » correspondante (section 5 de l'état de l'art v1) n'a plus de source.
11. **Papier B.**
    - AcMAS (2607.06807, ICML 2026) *se dit* le premier cadre de détection par activations en multi-agents (p. 10). C'est contredit par Golechha et Garriga-Alonso (NeurIPS 2025 : détecteurs boîte blanche par agent dans un jeu multi-agents, cité par NARCBench p. 3) et par NARCBench lui-même. On le cite sans lui reconnaître ni revendiquer de primauté.
    - La statistique spatio-temporelle reste libre dans les sources lues.
    - La domination boîte blanche de H3 n'est pas acquise : dans NARCBench, un juge Claude Sonnet 5 amorcé par quelques exemples (et informé de la menace) fait 20 sur 20 sans faux positif sur STEGO.
12. **Théorème négatif : 2606.10456 revendique la version boîte noire dans le temps, mais son énoncé est vide et faux pour sa propre construction — N-003 renforcé.**
    - **Énoncé vide.** La Proposition 1 (p. 3) ne vaut que contre une attaque « à budget de furtivité nul », qui suppose une marginale *empirique* égale à la marginale continue. C'est impossible : la distance de Kolmogorov-Smirnov vaut au moins 1/(2T). Le raisonnement ne suit pas non plus.
    - **Construction.** La copule gaussienne autorégressive ne préserve que la loi de chaque pas. Dans son propre dispositif (simulation), la moyenne a une puissance unilatérale à 1 % de 0,019–0,021 à δφ = 0,09, son point phare (≈ 2α), et de 0,168 à δφ = 0,40 (≈ 17α). Le max a une puissance sous α (inégalité de Slepian).
    - **Chiffres.** Ils viennent d'un seul tirage, alors que le PDF annonce un rééchantillonnage, absent du code. La remontée de 0,68 à 0,98 présentée comme réelle est synthétique (d'après le code).
    - **Ce qui manque.** La version correcte n'y est pas : invariance de la loi du multi-ensemble (classe C), sous-groupes de permutations, impossibilité sans structure, axe des agents, activations, processus e. Seule une remarque informelle sur le multi-ensemble (p. 1) la frôle : niveau « adjacent ».
    - **Conséquence.** Notre T doit être énoncé dans la classe C, et l'énoncé du programme (section 3) corrigé de même. Le papier peut être cité comme antécédent défectueux, jamais sa Proposition 1 comme un théorème.
13. **La règle « max ou attention, jamais la moyenne » ne peut pas s'appuyer sur Probe Trajectories (2605.18549).**
    - La stabilité du max y est mesurée face au bruit, pas face à un adversaire, et elle est en partie construite (le max cumulé est monotone).
    - L'évaluation se fait par validation croisée sur les jeux de test.
    - Des variantes autres que « Pool » y atteignent une AUROC ≈ 0,95 (annexe I, p. 28).
    - Elle repose sur RL-Obfuscation (niveau 2, non lu).

## 2. Corrections à apporter à l'état de l'art v1

| Ligne de l'état de l'art v1 | Correction | Source |
|---|---|---|
| NARCBench : « Rose, Cullen, Kaplowitz, Schroeder de Witt — Oxford / NYU » | Six auteurs : Rose, Cullen, Abdelnabi, Torr, Kaplowitz, Schroeder de Witt ; Oxford, ELLIS Tübingen, UCL ; pas de NYU ; v3 du 1er octobre 2026 | 2604.01151v3 p. 1 |
| NARCBench : « détection d'anomalie distribuée » | Cadrage v3 : test d'hypothèse composite à sous-groupe inconnu ; « distributed detection » ne sert plus qu'à classer les méthodes | p. 2, 12, 14 |
| NARCBench : « partage de tromperie » | « Deception Split » est un *écart* (2 plus hauts moins 2 plus bas) | p. 13 |
| Transfert zéro-shot « 0,60–0,86 ou 0,73–0,93 » | 0,73–0,93 pour Llama-3.1-70B seulement ; Qwen3-32B 0,48–0,88 ; DeepSeek-R1-32B 0,58–0,86 ; GPT-OSS-20B 0,56–0,72 (3 familles seulement) ; « 0,60–0,86 » introuvable en v3 | p. 24–25 |
| « juge textuel au niveau du hasard » | Vrai pour les juges non amorcés. Claude Sonnet 5 amorcé et informé de la menace : 20/20, sans faux positif (essai sur 20 + 20 parties) | p. 40–41 |
| 2609.03035 : « AUROC ≈ 0,91–1,00 » ; glissement de construit ; auto-incrimination ; « revendication interdite » de la section 5 | Simmons mixte ≤ 0,80 ; le rappel au seuil fixe chute avec le retour du score (0,95 → 0,41 ; 0,96 → 0,55) ; aucun glissement de construit ni auto-incrimination dans le PDF, donc la revendication interdite correspondante perd sa source ; équipe distincte (Truth Audit Labs) qui construit sur NARCBench | 2609.03035v1 p. 1, 3, 6, 14–15 |
| 2607.08066 : « 5 stratégies prescrites » | Contredit : les invites de l'agent ne prescrivent aucune stratégie ; il n'y a que 9 classes a posteriori | 2607.08066v1 p. 14, 7 |
| 2607.08066 : « jusqu'à 45 % contre 6 % » | Points absolus (figure), pour le seul moniteur Claude 3.7 Sonnet face au seul agent GPT-4.1, avec CoT ; le « ≈ 6 % » de la p. 2 est un *niveau* d'approbation, pas une baisse | p. 1, 2 ; figure 5, p. 8 |
| 2607.08066 : « + 9,5 % » | + 9,5 points sur des moyennes non pondérées de 9 cellules agent × moniteur (reconstruction du lecteur, recalculée par le contrôle) ; l'accès du moniteur au carnet est confondu avec la conscience qu'a l'agent d'être lu | p. 5, 14 |
| 2607.08066 : « projet LASR 2025 », version « Persuade Me If You Can » | Introuvables dans le PDF (auteurs : LASR Labs, Google DeepMind, UCL) | p. 1 |
| 2508.07805 : « Findings d'EMNLP 2025 » | Lieu introuvable dans le PDF | p. 1 |
| TRACE : « F1 0,713 ; rappel 0,844 » ; « complément boîte noire exact de H2 » | Confirmés tels qu'imprimés, mais ce sont des moyennes par tâche, sans taux de faux positifs (calcul : environ 75 %). « Exact » est faux : agrégation textuelle hors ligne, sans garantie | 2606.07054v1 p. 2, 3, 4, 17 |
| E-valuator : auteurs ; « par processus e » | Bonnie Berger manque. Validité par seuil PAC sur le maximum (taux ≤ α + δ), pas par l'inégalité de Ville (qui échoue empiriquement, p. 7–8) ; pas de somme cumulée ; « tout type » de score accepté (p. 3) | 2512.03109v2 p. 1, 3–8, 10 |
| TRACES : « observateur séparé » | Confirmé : Llama-3.1-8B et Qwen3-4B relisent hors ligne les trajectoires d'autres agents. Aucune garantie de faux positifs | 2605.27690v2 p. 4, 5, 8, 9 |
| Probe Trajectories : « le max stable, la moyenne oscille » | Confirmé, mais la stabilité du max cumulé est construite (monotone) et mesurée face au bruit, pas face à un adversaire. Analyse du lecteur : cela ne justifie le max qu'*à l'intérieur* d'une action | 2605.18549v1 p. 3–5, 28 |
| 2606.10456 : « The Distributed Detectability Band » ; « provenance douteuse » ; « preuves élémentaires » | Titre complet « … Against Marginal-Preserving Attacks » (le README du code porte un autre titre). Deux auteurs sans affiliation (adresses personnelles), relecteurs non nommés (« three reviewer-mandated gates »), v2 du 13 juin 2026. Proposition 1 vide de contenu, preuve fautive. Proposition 2 (b) correcte en substance pour le test du rapport de vraisemblance à horizon fixe ; (c) correcte pour l'autocorrélation sur l'échelle gaussienne | 2606.10456v2 p. 1, 3–4 |
| 2606.10456 : « traces entièrement synthétiques » ; « puissance → 1 » | Le PDF annonce des traces réelles sur « 120 benign goals » (p. 8) et présente la figure 7c comme une concaténation d'épisodes réels (p. 10). **D'après le dépôt** (commit b35f238 : `gpu/gen_real_traces.py`, `gpu/results/real_traces.json`, `experiments/exp_realdata_detect.py`) : scores bénins d'un moniteur Llama-3.2-3B, 16 objectifs tirés avec remise, 7 valeurs distinctes, attaque toujours synthétique, remontée 0,68 → 0,98 synthétique. « Puissance → 1 quand T → ∞ » : Proposition 2 (c), asymptotique, sans vitesse | p. 4, 8, 10 ; dépôt b35f238 |
| 2606.10456 : « 0,688 (SPRT) avec H = 2,0 » ; « 0,62 → 0,86 » | H n'est pas indiqué au point de puissance (p. 7 ; le tableau 3, p. 8, porte « H = 2.0 », origine probable de l'erreur). **D'après le code** : un seul tirage (le PDF annonce un rééchantillonnage, p. 5, absent du code), H = 1,5 sans effet sur les scores, puissance vraie ≈ 0,53 (simulation du lecteur). La courbe de la figure 6b et le JSON donnent 0,635 → 0,847 ; le texte (p. 7) et la légende (p. 9) disent 0,62 → 0,86 | p. 5, 7–9 ; dépôt b35f238 |
| 2606.10456 : « Monitor A au hasard » | Faux pour leur construction : moyenne ≈ 2α à δφ = 0,09 et ≈ 17α à δφ = 0,40 (simulation) ; max < α. Le 0,048 rapporté est la moyenne | p. 6–7 ; tableau 2, p. 7 |
| Environnement (a) : « base : le jeu de Terekhov et al., porté en 8B » | Ni code ni données publiés ; aucun Llama testé ; vérité = proxy (Sonnet 4.6 qui lit le papier). « Évaluer des interventions d'entraînement » est corrigé : l'entraînement est une hypothèse de modélisation, jamais exécuté | 2606.08892v2 p. 2–5, 9, 15–19 |
| `docs/sources/ressources-code-v1.md` (nos propres sources) : « en concaténant les épisodes jusqu'à T_eff = 400 » | La remontée est synthétique (bénin et attaque générés), pas une concaténation d'épisodes réels. À corriger dans une v2 de ce fichier | rapport 2606.10456, section 3 |

## 3. Verdicts par référence

Détail affirmation par affirmation, avec page et citation, dans les rapports :

| Référence | Rapport scellé | Bilan |
|---|---|---|
| 2607.08066v1 | `rapport-papierC-v1.md` | existence et date confirmées ; taux binaire ; « 5 stratégies prescrites » contredit ; « 45 / 6 » requalifié ; code : https://github.com/cerdwin/persuasion-evals (lien caché, p. 2), licence inconnue |
| 2508.07805v1 | `rapport-papierC-v1.md` | 14 juges (4 seulement dans le tableau principal), 7 techniques, note de 0 à 5 ; inflation relative à la note originale ; ni dose-réponse ni régression ; code annoncé sans adresse |
| 2606.07897v2 | `rapport-papierC-v1.md` | définition par pente en log-cotes ; 18 assistants ; rangs stables, magnitudes non ; données CC-BY-4.0 et code MIT |
| 2606.10456v2 | `rapport-2606.10456-v1.md` | Proposition 1 vide et fausse pour la construction ; nombreux écarts entre papier et code ; chiffres d'un seul tirage ; pas de licence ; version correcte (classe C) absente |
| 2604.01151v3 | `rapport-papierB-NARCBench-Das-v1.md` | coupe transversale par épisode ; séquentiel annoncé quatre fois, non réalisé ; code public différent de la v3 ; chiffres non utilisables comme bases à battre |
| 2609.03035v1 | `rapport-papierB-NARCBench-Das-v1.md` | équipe distincte ; scores par tour, sans accumulation ; ni construit ni auto-incrimination ; papier fragile (feuilles de résultats « fournies ») |
| 2606.08892v2 | `rapport-2606.08892-v1.md` | 73 citations sur 73 confirmées (72 par script, 1 sur l'image de la page) ; boîte noire, modèles fermés ; ni code ni données ; sept incohérences internes |
| 2607.06503v2 | `rapport-H2-voisins-v1.md` | sondes de l'agent, multi-tours, garantie de rappel par épisode (certificat optionnel) ; portes indépendantes, horizon figé |
| 2512.03109v2 | `rapport-H2-voisins-v1.md` | séquentiel boîte noire, validité PAC ; cadre non adverse |
| 2605.27690v2 | `rapport-H2-voisins-v1.md` | observateur séparé ; temporel > statique ; pas de garantie |
| 2605.18549v1 | `rapport-H2-voisins-v1.md` | série temporelle par token sur une chaîne de pensée ; max ≫ moyenne en AUROC (régime « gabarits », borne diagnostique) ; ni agent ni garantie |
| 2606.07054v1 | `rapport-TRACE-AcMAS-v1.md` | chiffres confirmés tels qu'imprimés ; faux positifs non rapportés (≈ 75 % par calcul) |
| 2607.06807v1 | `rapport-TRACE-AcMAS-v1.md` | détection par activations, agent par agent ; ni séquentiel ni agrégation entre agents ; gains à base non constante ; primauté auto-revendiquée et contredite |

## 4. Table des chiffres vérifiés

Empreintes des PDF : `docs/sources/pdf/provenance-niveau1-v1.md`. Nature : A = auteurs (imprimé), F = lecture de figure, C = calcul, S = simulation.

| Chiffre | Sens | PDF | Page | Nature |
|---|---|---|---|---|
| 24,4 % → 33,9 % (+ 9,5 points) | acceptation ajustée moyenne (9 cellules non pondérées), justification seule puis justification + chaîne de pensée | 2607.08066v1 | 5 | A (C pour les 9 cellules) |
| 95,5 / 97,5 / 98,8 % ; 7,5 / 5,0 / 1,3 % | bases bénigne et maligne (Gemini 2.5 Flash / GPT-4.1 / Claude 3.7 Sonnet) | 2607.08066v1 | 4 | A |
| 40 tâches, 4 domaines | banc | 2607.08066v1 | 2–3 | A |
| ≈ 35 points | baisse moyenne d'approbation avec un vérificateur d'une autre famille. Agent GPT-4.1, avec CoT, moyenne des 3 moniteurs ; pour Claude, le vérificateur « autre famille » est le modèle de l'agent. Le texte dit « approximately 35% » | 2607.08066v1 | 6, 8 | F |
| 14 juges ; 7 techniques ; échelle de 0 à 5 | dispositif | 2508.07805v1 | 4–5, 12, 19 | A |
| 23 / 22 / 20 / 18 / 16 / 11 / 7 sur 24 | cas où la note moyenne monte (Reciprocity / Consistency / Identity / Authority / Flattery / Majority / Pity). 24 cas = 4 juges × 6 bancs ; toute hausse compte, sans seuil de bruit | 2508.07805v1 | 5–6 | A |
| 18 modèles ; 349 propositions ; 11 172 invites | dispositif | 2606.07897v2 | 1–2, 5, 24 | A |
| 137,9 / 138, τ = 0,97 | stabilité des rangs (conversationnel) | 2606.07897v2 | 10, 32–33 | A |
| AUROC 1,00 (CORE, meilleure méthode) ; TRANSFER 0,73–0,93 (Llama-3.1-70B) | détection de collusion. Réserve d'effectif : 36 épisodes collusifs + 50 témoins, validation par domaine exclu (≈ 5 épisodes par pli) | 2604.01151v3 | 12, 15, 24–25, 32 | A |
| rappel 0,38 à 1 % de faux positifs (TRANSFER, Deception Split) ; 1,00 (STEGO, Activation Alignment) | point opérationnel (courbes ROC de Llama-3.1-70B) ; à recalculer par le programme | 2604.01151v3 | 15 | A |
| juge faible Haiku 4.5 ; r = 0,55 global ; par générateur de 0,00 (GPT-5.4) à 0,46 (GPT-OSS-20B), 0,14 pour Opus 4.6 | qualité du juge faible | 2606.08892v2 | 4–5 (figure 3) | A (F par générateur) |
| g = 34,7 à w = 85,3 (Opus subversif) contre 70,7 (Opus bénin) | effet de l'attaque contre b0. La figure 5 (p. 6) donne 67,6 pour l'Opus bénin : incohérence interne | 2606.08892v2 | 2, 5–6 | A |
| F1 0,713 ; rappel 0,844 | TRACE (moyennes par tâche, Sonnet 4.6, seuil ≥ 4) | 2606.07054v1 | 2, 4, 17 | A |
| 189 bénignes, 274 malveillantes, 463 trajectoires | jeu de TRACE | 2606.07054v1 | 6 | A |
| ≈ 75 % de faux positifs (142/189) ; « tout signaler » F1 0,755 (moyenne par tâche) et 0,744 (poolé) | TRACE (`TRACE-AcMAS/recon_trace.py`, recalculé indépendamment) | 2606.07054v1 | 6, 17 | C |
| AcMAS F1 0,93–0,95 (synchrone), 0,92–0,94 (asynchrone) ; faux positifs 0,04–0,07 | détection par activations en multi-agents. Seuil choisi en maximisant le F1 ; 100 % de faux positifs sans trace bénigne du domaine cible (p. 20) | 2607.06807v1 | 6, 18, 20 | A |
| 34,7 à 60,2 % (TextCraft) et 24,7 à 54,9 % (WebShop) de tokens économisés à 90 % de rappel cible, selon le modèle | cascade de sondes ; 60,2 et 54,9 sont les « strongest settings » des auteurs | 2607.06503v2 | 1, 5 | A |
| AUROC max / moyenne / dernier token : 94,44 / 49,96 / 60,11 (R1-Llama-8B) | agrégation sur une chaîne de pensée (sondes entraînées sur gabarits, nocivité ; « diagnostic upper bound », p. 4) | 2605.18549v1 | 4–5 | A |
| « Any monitor whose decision rule depends only on F̂att (i.e., a marginal feature) has detection power equal to its false-positive rate against any zero-stealth-budget attack. » | Proposition 1, à citer comme revendication, pas comme théorème | 2606.10456v2 | 3 | A |
| moyenne : puissance unilatérale à 1 % de 0,019–0,021 et AUC du max 0,486 (δφ = 0,09) ; moyenne 0,168 et AUC du max 0,302 (δφ = 0,40) ; T = 300, 40 000 + 40 000 trajectoires | la construction publiée ne rend pas les statistiques de marginales aveugles. Simulation du lecteur, rejouée par l'orchestrateur (sortie archivée) et réimplémentée indépendamment par le contrôle (0,172 / 0,300 à δφ = 0,40) | 2606.10456v2 (dépôt b35f238) | — | S |

## 5. Références nouvelles à lire (trouvées dans les bibliographies), par priorité

1. **H2, Tr, papier B.** Kulkarni 2026, arXiv 2604.28129, « Latent adversarial detection: Adaptive probing of LLM activations for multi-turn attack detection » (cité par NARCBench pour l'accumulation multi-tours).
2. **H2.** Padhi et al. 2026, arXiv 2604.19775, « From Actions to Understanding: Conformal Interpretability of Temporal Concepts in LLM Agents ».
3. **H2.** Römer et al. 2025 (FIPER, NeurIPS), « Failure Prediction at Runtime for Generative Robot Policies » (alarmes calibrées sur les succès) ; Yueh-Han et al. 2025, arXiv 2506.10949 (moniteurs séquentiels légers, régime « chaque pas bénin »).
4. **HC1.** PARROT, arXiv 2511.17220 (variation de confiance par vraisemblance du jeton sous pression d'autorité), à rehausser ; BASIL, arXiv 2508.16846 ; Sicilia et al., arXiv 2410.14746.
5. **Environnement (a), H1.** Les auteurs de 2606.08892 jugent le monitoring moins prometteur en s'appuyant (p. 2) sur Hebbar 2025, Gasteiger et al. 2025 et Gan et al. 2026 (ASMR-Bench, arXiv 2604.16286). Ils citent aussi Ryd et al. (arXiv 2604.22082), Wang et al. (arXiv 2602.15222, le plus proche selon eux), CTRL-ALT-DECEIT (arXiv 2511.09904) et Benton et al. 2024 (arXiv 2410.21514).
6. **Théorème négatif entre agents.** Addario-Berry et al. 2010, « On Combinatorial Testing Problems ».
7. **Papier B.** Golechha et Garriga-Alonso 2025 (NeurIPS, détection boîte blanche dans un jeu multi-agents). Pour H3 (régimes de collusion indétectable) : Pang et al. 2026 (Codetta) ; Schroeder de Witt 2026, arXiv 2606.09931 ; Vaikuntanathan et Zamir 2026.
8. **H2.** Wu, Zhou, Bates, Jaakkola 2025, « Thought calibration » (EMNLP) ; PrefixGuard, arXiv 2605.06455.
9. **Tr.** Kramár et al. 2026, arXiv 2601.11516 ; Taufeeque et al. 2026, arXiv 2602.15515.
10. **Papier B, H8, HC2b.** Shi, Zhang, Yang 2026, arXiv 2609.24967 ; Haskins, Chughtai, Engels 2026 ; Nguyen et al. 2025.
11. **Papier C.** Zeng et al. 2024 (« How Johnny can persuade… ») ; Koo et al., arXiv 2309.17012 ; Chen et al., arXiv 2402.10669 ; Arnav et al., arXiv 2505.23575 ; Lin et al., arXiv 2502.03052 ; Panickssery et al., arXiv 2404.13076 ; Wataoka et al., arXiv 2410.21819 ; Li et al., arXiv 2502.01534 ; Liu et al., arXiv 2403.04957 ; Greshake et al., arXiv 2302.12173 ; Baker et al., arXiv 2503.11926.

## 6. Décisions issues de la lecture

Au format de décision dans `livrables/anteriorite-niveau1-v1/decisions-v2.md`.
- Nœuds : N-003 (renforcé), N-005 (élargi), N-007 (H2, conditionné aux lectures de la section 5), N-008 (critère de G1).
- Propositions : P-003 (bras boîte noire de G1), P-004 (environnement (a)), P-005 (famille (i) scindée et témoin « instruit sans sabotage »).
