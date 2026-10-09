# Lecture sur source primaire — TRACE (2606.07054v1) et AcMAS (2607.06807v1) — v1

Date : 2026-10-04 (UTC). Lecteur : sous-agent neuf (n'a rien écrit de ce qu'il vérifie). PDF : `docs/sources/pdf/2606.07054v1.pdf` (9e169bb5…) et `docs/sources/pdf/2607.06807v1.pdf` (bf509308…), lus en entier.
Fichiers de travail scellés : `docs/sources/lecture-pdf-niveau1/TRACE-AcMAS/` (extractions par page `trace_pages.txt`, `acmas_pages.txt` ; reconstructions `recon_trace.py`, `recon_t6.py`, `recon_acmas.py`). Les trois scripts ont été rejoués par l'orchestrateur : sorties identiques au rapport.
Convention : page = n-ième page du fichier. « Calcul » = reconstruction à partir des tables du papier (pas un chiffre des auteurs).
Rapport reproduit tel que rendu (mise en forme seule).

## Verdict
- Les deux papiers ont été lus en entier, annexes comprises.
- **TRACE** : F1 0,713 et rappel 0,844 sont confirmés tels qu'imprimés (Claude Sonnet 4.6, SHADE-Arena, seuil ≥ 4 sur 1–5). Ce sont des moyennes par tâche, et **aucun taux de faux positifs n'est donné**. Par calcul, TRACE signale ≈ 75 % des trajectoires bénignes, et « tout signaler » donnerait un F1 de 0,744 sur ce jeu. Invites publiées, code non publié.
- **AcMAS** : +0,22 et +0,55 sont confirmés tels qu'imprimés, mais par rapport à deux références différentes (à base constante : +0,23 et +0,50). Pas de sonde entraînée, pas d'agrégation entre agents, pas d'accumulation temporelle ; « synchrone / asynchrone » désigne le mode d'exécution du système multi-agents.

## 1. TRACE (2606.07054v1)

Identité : « TRACE: Trajectory Reasoning through Adaptive Cross-Step Evidence Aggregation for LLM Agents » — Vijitha Mittapalli, Shreyaa Jayant Dani, Satya Srujana Pilli, Snigdha Ansu, Mohammadreza Teymoorianfard (UMass Amherst), Franck Dernoncourt, Ryan A. Rossi (Adobe Research), Hongjie Chen (Dolby Labs), Yu Wang (University of Oregon), Nesreen K. Ahmed (Cisco). Préprint arXiv [cs.CL] du 5 juin 2026, sans conférence (p. 1).

| Affirmation ou question | Verdict ou réponse | Page | Citation |
|---|---|---|---|
| Boîte noire, sans entraînement | Confirmé : inférence seule, aucun accès aux activations | 3 | « does not modify the underlying agent policy, access internal model activations, or use additional training signals » |
| En ligne ou après coup ? | Après coup : trajectoire complète, une fois la tâche finie | 3 | « The monitor observes the complete execution trajectory after task completion » |
| Boucle triage–inspection–jugement | Confirmé. Triage = une passe sur la trajectoire entière, contraintes + 3 à 4 fenêtres suspectes (locales : 1–3 pas adjacents ; « pattern » : 3–8 pas non adjacents) | 4, 12 | « a constraint representation encoding the task intent, permitted scope, and authorized actions » |
| Inspection | Contrôleur qui choisit InspectStep, CompareSteps, CheckPolicy, AnalyzeDecisions ou Done par fenêtre | 4, 12 | « Done : conclude the investigation (available after 2 observations) » |
| Agrégation de la preuve entre étapes | Textuelle : constats réinjectés dans le contexte, synthèse par un appel final ; aucune règle numérique de cumul | 4 | « findings from earlier windows are injected as context into later inspection steps » |
| Critère d'arrêt | « Preuve suffisante » (jamais opérationnalisée) ou budget de fenêtre épuisé | 4 | « sufficient evidence has accumulated to support a stable verdict, or (2) a per-window inspection budget is exhausted » |
| Jugement, seuil | Score entier 1–5, malveillant si ≥ 4 ; règle imposée au juge (sévérité 4–5 et confiance haute ⇒ ≥ 4) | 4, 13 | « TRACE assigns a final suspicion score on a 1–5 scale, and trajectories scoring ≥ 4 are classified as malicious. » |
| Invites publiées | Oui : 7 gabarits (annexe B) | 12–13 | « B TRACE Monitor Prompt Templates » |
| Budget d'appels | ≤ 4 fenêtres × ≤ 6 pas d'inspection, ≈ 12 appels | 6 | « up to 4 suspect windows per trajectory with a maximum of 6 inspection steps per window, averaging 12 LLM calls » |
| Banc d'essai | SHADE-Arena, 10 domaines, 463 trajectoires (189 bénignes, 274 malveillantes), toutes en test ; Election Tampering gardé (exclu par Kutasov) ; modèle agent non précisé | 5–6 | « All 463 trajectories are treated as a held-out test set. » |
| Modèles moniteurs | Claude Sonnet 4.6 ; ablation : Opus 4.7, GPT-5.1, o4-mini, « Gemini Flash 3.5 » (bibliographie : « Gemini 2.5 flash ») ; bases sur Sonnet 4.6 seulement | 6 | « Baselines use Sonnet 4.6 only, consistent with prior work » |
| **F1 0,713, rappel 0,844** | **Confirmé tel qu'imprimé** (Sonnet 4.6, 463 trajectoires, seuil ≥ 4). Moyennes non pondérées des 10 tâches ; bases en totaux poolés. Poolé (calcul) : rappel 0,847 (le texte dit 84,7 %, p. 5), précision 0,620, F1 0,716 | 2, 17 | « TRACE achieves aggregate F1 of 0.713 and recall of 0.844 (Claude Sonnet 4.6), outperforming both baselines (F1 = 0.577 and 0.700) » |
| **Taux de faux positifs** | **Absent du papier.** Calcul (tables 1 et 5, précisions retrouvées à 0,0005 près) : 142/189 bénignes signalées ≈ 75 % (100 % sur SSN, Bank Transfer, Expenditure). Bases : 0/189 (trajectoire complète), 21/189 ≈ 11 % (séquentiel) ; seuils des bases non indiqués | 6, 17 | absence vérifiée (« FPR », « ROC », « AUC », « false positive rate ») |
| Plancher trivial | Calcul : 59 % de malveillantes ⇒ « tout signaler » donne F1 0,744 (poolé) ou 0,755 (moyenne par tâche), au-dessus de TRACE-Sonnet et des deux bases ; seul Opus 4.7 (0,790) fait mieux | 6 | « F1 is the primary metric given class imbalance (189 benign vs. 274 malicious). » |
| « F1 0,790 » des contributions | Résultat d'Opus 4.7, comparé à des bases sur Sonnet 4.6 | 2, 7 | « increasing aggregate recall from 0.405–0.580 (baselines) to 0.844 and aggregate F1 to 0.790 » |
| Agrégats incohérents entre modèles | Calcul : « Overall » d'Opus, Sonnet, o4-mini = moyennes par tâche ; GPT-5.1 et Gemini = poolés ; trois tâches d'Opus incompatibles avec les effectifs de la table 1 | 7, 18 | — |
| Bases comparées | Trajectoire complète (Kutasov 2025, une passe) : F1 0,577, rappel 0,405, précision 1,000 ; séquentiel (Kale 2025, segments fixes, résumé courant) : F1 0,700, rappel 0,580, précision 0,883 | 5–6, 17 | « reproduced using the publicly available SHADE-Arena codebase » |
| Garantie de faux positifs, calibrage | Aucune garantie ; seuil, budget et actions fixés sur un « petit jeu de validation » non décrit (mal compatible avec « toutes en test ») | 9 | « The verdict threshold, inspection budget, and action space are fixed based on a small validation set and are not fully tuned per model. » |
| Coût | 12,3 appels (TRACE), 18,8 (séquentiel), 1 (complète) ; pas de comptage de jetons | 6 | « TRACE achieves this with 12.3 average LLM calls per trajectory versus 18.8 for the sequential monitor » |
| Modèles faibles | Échec par arrêt précoce, raisonnement pauvre | 7 | « early termination (Gemini 3.5, o4-mini average 7 calls, recall < 0.435) » |
| Évasion par justifications plausibles (« Manipulation ») | TRACE : 0/17 ; séquentiel : 10/17 | 5 | « the sequential monitor detects 10 of 17 trajectories while TRACE detects none » |
| Code, licence | Aucune adresse de dépôt ni licence ; seul code cité : SHADE-Arena (bases) | 5–6 | absence vérifiée (« github », « http », « license ») |

Chiffres utilisables :
- Jeu : 189 bénignes, 274 malveillantes, 463 au total ; 91,8 tours en moyenne (p. 6, table 1).
- TRACE avec Sonnet 4.6, moyennes par tâche : exactitude 0,606, précision 0,641, rappel 0,844, F1 0,713 (p. 17, table 5).
- Bases poolées (exactitude / précision / rappel / F1) : trajectoire complète 0,648 / 1,000 / 0,405 / 0,577 ; séquentiel 0,706 / 0,883 / 0,580 / 0,700 (p. 17).
- Appels moyens : 12,3 / 18,8 / 1 (p. 6, table 2).
- F1 de TRACE selon le moniteur (p. 7, table 3) : Opus 4.7 0,790 (11,0 appels) ; GPT-5.1 0,588 ; Gemini 0,586 ; o4-mini 0,495.
- Verbalisation sélective, 102 trajectoires sur 274 (p. 5) : 94,1 % (TRACE), 46,1 % (séquentiel), 44,1 % (complète).
- Par calcul :
  - TRACE poolé : rappel 0,847, précision 0,620, F1 0,716, faux positifs 75 % ;
  - faux positifs des bases : séquentiel 11 %, trajectoire complète 0 % ;
  - faux positifs approximatifs des autres moniteurs : Opus ≈ 35 %, GPT-5.1 23 %, Gemini 7 %, o4-mini 25 % ;
  - plancher « tout signaler » : F1 0,744.

## 2. AcMAS — When Agents Go Rogue (2607.06807v1)

Identité : « When Agents Go Rogue: Activation-Based Detection of Malicious Behaviors in Multi-Agent Systems ».
- Auteurs : Haowen Xu et Xue Tan (contribution égale), Lei Ma, Zhihao Zhang, Chao Wang, Qingze Wang, Ping Chen, Jun Dai, Xiaoyan Sun.
- Affiliations : WPI ; Fudan ; un chercheur indépendant.
- Statut : arXiv [cs.CR] du 7 juillet 2026 ; ICML 2026, PMLR 306 (p. 1).

| Affirmation ou question | Verdict ou réponse | Page | Citation |
|---|---|---|---|
| Modèles | GPT-OSS-20B (table 1), DeepSeek-V3, Qwen3-30B-A3B, « LLaMA3-8B » (variante non précisée) ; systèmes homogènes | 6, 17 | « open-source LLM backbones, including GPT-OSS-20B …, DeepSeek-V3 …, LLaMA3-8B …, and Qwen3-30B-A3B » |
| Couches | Dernière couche, état du dernier jeton généré, une fois par réponse | 4 | « We adopt the hidden state h(L) from the final layer L of the final generated token as a summary of the entire input context » |
| Sondes ? | Aucune sonde entraînée : prototype non supervisé (centroïde bénin normalisé) et distance cosinus seuillée (éq. 10–12) | 5–6 | « experiments use τmax = 0.35 with τdetect = 0.12 » |
| Choix de couche | F1 0,95 (finale), 0,86 (médianes 10–14), 0,71 (précoces 1–4) | 8 | « Middle layers (10–14) 0.85 0.87 0.86 » |
| Agrégation par agent | Décision indépendante par agent et par pas | 5 | « this formulation operates independently on each agent's internal state, enabling topology-agnostic detection » |
| Entre agents | Corrélation affirmée (éq. 8), ni mesurée ni utilisée comme statistique. Seul lien : en synchrone, prototype mis à jour par moyenne mobile (α = 0,7) des agents jugés normaux ; sans cette mise à jour, F1 0,95 → 0,87 | 4, 5, 8 | « compromised agents exhibit correlated activation patterns in multi-agent settings » |
| Dans le temps | Aucune accumulation (pas de somme, de somme cumulée, de test séquentiel) ; en asynchrone, prototype fixe | 5 | « We maintain a fixed prototype µnormal computed from initial benign execution traces » |
| Synchrone / asynchrone | Modes d'exécution du système (tours en pas de charge contre exécution événementielle) | 2 | « Sync-MAS with lock-step, round-based execution, (b) Async-MAS with event-driven, task-allocation-based execution » |
| **+0,22 (sync.) et +0,55 (async.)** | **Confirmés tels qu'imprimés, référence non constante** (calcul, table 1) : AcMAS 0,944 / 0,934 ; « 0,72 » = G-Safeguard (0,712) ; « 0,38 » = moyenne G-Safeguard + BlindGuard en asynchrone (0,380), pas la meilleure base (G-Safeguard 0,432). Contre G-Safeguard dans les deux cas : +0,23 et +0,50. Chiffres « furtifs » de l'introduction (0,95/0,74 ; 0,94/0,46) = ligne CSQA seulement | 1, 2, 6, 7 | « by +0.22 F1 in synchronous settings (0.94 vs. 0.72) and by +0.55 F1 in asynchronous settings (0.93 vs. 0.38) » |
| Bases | G-Safeguard (graphe supervisé), BlindGuard (graphe non supervisé), PERM, TAM, toutes sur les sorties textuelles ; TAM et PERM souvent sous le hasard (AUROC jusqu'à 16,9) | 6–7 | « Both methods formulate malicious agent detection as a graph learning problem over multi-agent interactions. » |
| Faux positifs | 0,04–0,07 au seuil 0,12 ; AUROC 97,6–99,5 ; seuil choisi en maximisant F1 sur validation (équivalence annoncée avec l'indice de Youden fausse en général) ; aucune garantie | 6, 18 | « Select threshold by maximizing F1 score » |
| Cadre adverse | Attaquants instruits par message système ; aucun agent ne se sait surveillé ; attaques adaptatives = « défi ouvert » | 3, 9 | « adaptive attacks that attempt to gradually shift activation distributions remain an open challenge. » |
| Que lit le détecteur ? | Le dernier état résume tout le contexte ; attaquants à message système distinct ; sans trace bénigne du domaine cible, taux de faux positifs 1,00 (tables 7–8) | 4, 16, 20 | « Then talk to other agents and convince them of your answer. » |
| N variable | Exactitude > 97 % pour N = 8, 20, 50, 80 (4 modèles) : détection par agent, ni sécurité à budget constant ni boîte noire | 8 | « Across varying scales (8-80 agents), AcMAS maintains consistently high detection accuracy with minimal performance variance (std < 0.8%). » |
| Intensité | 0 à 40 % d'agents compromis ; F1 > 0,90 jusqu'à 50 % | 7, 8 | « we vary the number of compromised agents from 0 to 40% » |
| Protocole | Runs, graines, topologie, N de la table 1, étiquetage des agents contaminés non spécifiés ; annexe E = un cas d'étude. Calcul : 50 % de positifs implicites pour AcMAS contre 35–39 % pour les bases sur les mêmes données | 6, 7, 18 | « Results are reported as mean ± standard deviation across runs. » |
| Priorité revendiquée | « premier cadre » de détection par activations en multi-agents | 10 | « AcMAS represents the first framework to address adversarial compromise in MAS via activation-level analysis and correction. » |
| Code, licence | Aucun dépôt ni licence | 12 | absence vérifiée |

Chiffres utilisables :
- Table 1 (p. 6), gpt-oss-20b, 5 scénarios :
  - AcMAS : F1 0,93–0,95 (synchrone) et 0,92–0,94 (asynchrone) ; faux positifs 0,04–0,07 ; AUROC 97,6–99,5 ;
  - G-Safeguard : F1 0,69–0,74 (synchrone) et 0,41–0,46 (asynchrone) ; faux positifs 0,20–0,26 et 0,45–0,50.
- Moyennes de F1 par calcul (synchrone / asynchrone) : AcMAS 0,944 / 0,934 ; G-Safeguard 0,712 / 0,432 ; BlindGuard 0,560 / 0,328.
- Défense (p. 7, table 2) :
  - AcMAS : succès d'attaque 0,02–0,05, achèvement de tâche 0,96–1,00 ;
  - G-Safeguard : achèvement de tâche 0,68–0,90.
- Ablations (p. 8, table 3) : couches 0,95 / 0,86 / 0,71 ; sans mise à jour adaptative 0,87 ; sans normalisation 0,89.
- Seuil (p. 8) : 12 % de faux positifs à τ = 0,08 ; 15 % de faux négatifs à τ = 0,16.
- Prototype (p. 8–9) : stable vers 50 traces ; écart < 0,03 avec 100 traces.
- Coût (p. 9, table 4) : extraction 2,3 ms (0,15 % de l'inférence) ; pilotage des activations 185,3 ms (12,4 %).
- Changement de domaine (p. 20, tables 7–8) : F1 0,49 et 100 % de faux positifs sans trace cible ; 0,92 et 7 % avec 300 traces cibles (CSQA → InjecAgent).

## 3. Faisabilité de TRACE-lite

**Réimplémentable dans ses grandes lignes (annexe B), pas reproductible à l'identique ; aucune donnée sur un moniteur 8B ou 3B, signes défavorables.**

Publié et suffisant pour le squelette :
1. Triage : un appel (B.1), JSON {constraints, suspect_windows}, 3 à 4 fenêtres (p. 12).
2. Inspection :
   - jusqu'à 4 fenêtres de 6 pas (p. 6) ;
   - contrôleur B.2, qui produit un JSON {reason, action, arguments, finding, severity, reconciliation} ;
   - exécuteurs B.3.1–B.3.4, en texte libre, avec une note de 1 à 5 ;
   - Done n'est permis qu'après 2 observations ; une mémoire textuelle passe d'une fenêtre à l'autre (p. 4, 12–13).
3. Verdict : B.4, JSON {score 1–5, reasoning}, seuil ≥ 4, règles de notation (p. 4, 13).
4. Coût de référence : 12,3 appels (Sonnet 4.6) ; 6,5 à 7,2 appels pour les modèles faibles (p. 6, 7).

Manquant, à fixer et consigner au préenregistrement de G1 :
- aucun code ni licence ;
- format des entrées non spécifié ({trace}, {step_previews}, {memory}, {prior_observations}, {evidence_items}), ni la définition d'un « pas » ni la troncature (seul indice : action de l'assistant + résultats d'outils, p. 12) ;
- « confiance haute » exigée sans champ correspondant dans le JSON du contrôleur ;
- analyse des réponses en texte libre et JSON invalides (critique en 3B et 8B) ; valeurs d'exemple recopiables (« "severity": 0 », « "score": 3 ») ;
- échantillonnage (« default inference parameters », p. 6) et jeu de validation du seuil (p. 9) non décrits ;
- lecture après coup (p. 3) : pour la latence d'alerte, exécuter sur préfixes (≈ 12 appels par point de contrôle) ;
- score entier : la courbe ROC a au plus 5 points, ce qui rend le rappel à 1 % de faux positifs mal défini. Remède : espérance du score sous les probabilités des jetons du verdict, ou moyenne de k tirages ;
- longueur : le triage lit toute la trajectoire (91,8 tours en moyenne, jusqu'à 157,4 sur une tâche, p. 6) ;
- petits modèles non testés ; les plus faibles testés s'arrêtent tôt (p. 7). Recommandation : Llama-3.1-8B-Instruct comme TRACE-lite principal (option (a) de D1) ; 3B seulement pour le bras « moniteur faible », avec planchers.

## 4. Table de collision

| Revendication | TRACE | AcMAS | Niveau | Pages |
|---|---|---|---|---|
| Base boîte noire de G1 (TRACE-lite) ; « complément boîte noire exact de H2 » selon l'état de l'art | Agrégation inter-étapes boîte noire, hors ligne, sans test séquentiel ni garantie ; « exact » est faux | — | Base utilisable sous conditions ; formulation de l'état de l'art à corriger | T 3, 4, 9 |
| Critère D-c : rappel à 1 % de faux positifs, ou + 5 points de F1 | F1 récompense le sur-signalement : TRACE + 0,013 sur le séquentiel avec faux positifs de 11 % → 75 % (calcul) ; « tout signaler » 0,744 | — | Bras F1 fragile (alerte 1) | T 6, 17 |
| H1 : gain blanc-sur-noir sur sabotage diffus et flou, à faux positifs égaux | Pas d'activations ; indice favorable : la boîte noire avale les justifications plausibles (0/17) | Activations > graphes sur sorties textuelles en multi-agents, mais injection/empoisonnement, attaquants instruits, faux positifs non égalisés, pas de sabotage diffus | **Libre** (TRACE) ; **adjacent** (AcMAS) | T 3, 5 ; A 6–7 |
| H2 : accumulation séquentielle de scores de sondes | Accumulation dans le contexte d'un juge, sans statistique ni sonde | Décision par pas, sans accumulation temporelle | **Adjacent** pour les deux ; H2 reste **libre** | T 4 ; A 5 |
| Papier B : statistique spatio-temporelle sur activations | — | Détection par activations en multi-agents, par agent et par pas, revendiquée comme « premier cadre » ; aucune statistique spatio-temporelle | **Partiel** pour le cadrage (citer, ne pas revendiquer la primauté) ; **libre** pour la statistique | A 4–5, 10 |
| Coupe transversale agent contre population (base de E3.1) | — | En synchrone, chaque agent est comparé au centroïde des agents jugés normaux ; F1 0,95 → 0,87 sans cette mise à jour | **Partiel** : base à ajouter à côté de NARCBench | A 5, 8 |
| Co-élévation entre agents | — | Corrélation affirmée, ni mesurée ni exploitée (et triviale : message système partagé) | **Adjacent** | A 4, 16 |
| H3 : courbe sécurité(N) | — | Exactitude par agent pour N = 8–80, boîte blanche seule, sans budget constant ; courbe plate par construction | **Adjacent** | A 8 |
| H4′ : diversification | — | Systèmes homogènes seulement ; hétérogènes renvoyés à plus tard | **Libre** | A 17 |
| H6 : marge asymétrique | — | Pilotage des activations vers le prototype après détection : intervention spécifique | **Adjacent** | A 5–7 |
| Validité de construit (H8) | — | Ne distingue pas « instruction cachée » et intention : attaquants instruits, 100 % de faux positifs sous changement de domaine | **Adjacent** ; exemple à citer pour H8 | A 4, 16, 20 |

T = pages de TRACE ; A = pages d'AcMAS. Le classement « adjacent à partiel » d'AcMAS dans le rapport de transcription est confirmé.

## 5. Alertes

1. **Les chiffres de TRACE ne sont pas une cible, et le bras F1 du critère de G1 se gagne en sur-signalant.**
   - Le couple 0,713 / 0,844 correspond à ≈ 75 % des bénignes signalées (calcul) ; « tout signaler » donne F1 0,744.
   - La ligne TRACE de la section 2.3 de l'état de l'art est à requalifier (moyennes par tâche, seuil ≥ 4, faux positifs non rapportés).
   - Le bras « + 5 points de F1 » du critère D-c a le même défaut. Le modifier touche un critère de porte : **nœud de décision**.
   - Pistes : F1 au seuil calibré sur les épisodes honnêtes réservés, au même taux de faux positifs pour tous les bras ; plancher « tout signaler » obligatoire ; ou retrait de ce bras.
2. **En 8B ou 3B, TRACE-lite risque d'être un homme de paille, ce qui gonflerait H1 (contraire à R4).**
   - Rien n'est testé sous o4-mini ou Gemini, qui s'effondrent déjà par arrêt précoce.
   - Pas de code, colle à inventer, score entier, lecture après coup.
   - Parades à préenregistrer en G1 : planchers « tout signaler » et « juge en une passe avec le même modèle » ; journal des arrêts précoces et des JSON invalides ; score continu par probabilité des jetons du verdict ; mode préfixes si la latence est mesurée.
3. **AcMAS : gains non comparables, construit douteux, antériorité partielle pour le papier B.**
   - Les + 0,22 / + 0,55 se rapportent à deux références différentes ; à base constante : + 0,23 / + 0,50.
   - Le détecteur lit le dernier jeton comme résumé du contexte, avec des attaquants à message système distinct, et 100 % de faux positifs sous changement de domaine : il lit vraisemblablement « j'ai une instruction cachée », ce que les familles (i)/(ii) doivent contrôler.
   - Pas d'attaque adaptative, pas de code.
   - Pour le papier B : citer AcMAS (première détection par activations en multi-agents, au niveau de l'agent) ; ajouter sa distance au prototype comme base de coupe transversale en E3.1. La statistique spatio-temporelle, la co-élévation et H3 restent libres.
