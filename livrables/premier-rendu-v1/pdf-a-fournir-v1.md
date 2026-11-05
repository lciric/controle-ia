# PDF et pages à me fournir — v1

Rédigé le 2026-10-04. Raison : arxiv.org (et openreview.net, lesswrong.com, huggingface.co, doi.org…) sont refusés par la politique réseau de l'environnement, et le budget de recherches web de la session est épuisé.
**Comment me les donner** : un zip par niveau, téléversé dans la conversation. Pour arXiv, garde le nom avec la version, par exemple `2607.08066v1.pdf` (le lien `arxiv.org/pdf/2607.08066` télécharge la dernière version : note laquelle). Pour une page web, enregistre-la en PDF (« Imprimer → Enregistrer en PDF ») avec l'adresse visible.
À réception, j'empreinte chaque fichier (SHA-256), je le range dans `docs/sources/pdf/` et je cite chaque chiffre avec sa page (R6, R7).
Les identifiants marqués ✱ viennent de ma mémoire, pas d'un résultat vu dans cette session : si l'identifiant ne correspond pas au titre, c'est le titre qui fait foi.

## Niveau 1 — bloquant (nœuds de décision N-003 à N-006, bascule NARCBench, environnement (a)) — 13 PDF

| ☐ | Identifiant | Titre | Pourquoi |
|---|---|---|---|
| ☐ | 2607.08066 | Persuasion Attacks Can Decrease Effectiveness of CoT Monitoring | collision papier C (HC1, HC3, HC5) |
| ☐ | 2508.07805 | Can You Trick the Grader? Adversarial Persuasion of LLM Judges | nouveau : déplacement continu des juges par technique (HC1) |
| ☐ | 2606.07897 | Pander Score: A Continuous Measure of Sycophancy as Epistemic Deference | nouveau : déférence continue (HC1) |
| ☐ | 2606.10456 | The Distributed Detectability Band Against Marginal-Preserving Attacks | lemme et théorème négatif ; lire les preuves |
| ☐ | 2604.01151 | Detecting Multi-Agent Collusion Through Multi-Agent Interpretability (NARCBench) | papier B ; agrégation en coupe ou séquentielle ; chiffres de transfert |
| ☐ | 2609.03035 | You Can't Escape Your Own Activations: Evaluation Awareness and Multi-Agent Monitoring | papier B, H8, HC2b |
| ☐ | 2606.08892 | Diffuse AI Control on Fuzzy Tasks (Terekhov, Gulcehre, Hebbar, Benton) | base de l'environnement (a) : code et données ? |
| ☐ | 2607.06503 | Doomed from the Start: Early Abort of LLM Agent Episodes via a Recall-Controlled Probe Cascade | nouveau : sondes séquentielles sur agents (H2) |
| ☐ | 2512.03109 | E-valuator: Reliable Agent Verifiers with Sequential Hypothesis Testing | périmètre de H2 |
| ☐ | 2605.27690 | TRACES | observateur séparé ou activations de l'agent : pivot de H2 |
| ☐ | 2605.18549 | Probe Trajectories | H2 |
| ☐ | 2606.07054 | TRACE: Trajectory Reasoning through Adaptive Cross-Step Evidence Aggregation for LLM Agents | base TRACE-lite de G1 (F1, rappel) |
| ☐ | 2607.06807 | When Agents Go Rogue: Activation-Based Detection of Malicious Behaviors in Multi-Agent Systems | nouveau : boîte blanche multi-agents (papier B) |

## Niveau 2 — état de l'art, section 6, et bases chiffrées — 34 PDF

| ☐ | Identifiant | Titre court | Pour |
|---|---|---|---|
| ☐ | 2606.14037 | Kim et al. (plan factoriel, 972 000 réponses) | HC1 |
| ☐ | 2506.10805 | McKenzie et al., sondes « enjeux élevés » | T0.7 ; max de moyennes glissantes |
| ☐ | 2502.03407 | Goldowsky-Dill et al., sondes de tromperie (Apollo) | T0.7 ; bases chiffrées |
| ☐ | 2507.12691 | Parrack, Attubato, Heimersheim, gain blanc-sur-noir | H1 |
| ☐ | 2512.07810 | Taylor et al., jeux d'audit du sandbagging | famille (iii) |
| ☐ | 2605.15377 | Ensemble Monitoring for AI Control | H5, HC5 |
| ☐ | 2608.16190 | Decorrelation Is Not Complementarity | H5 |
| ☐ | 2607.07368 | Makins et al., attaques distribuées, FakeLab | papier B ; message FakeLab |
| ☐ | 2607.02514 | Hills, Caspary, Cooper Stickland, Distributed Attacks in Persistent-State AI Control | papier B ; où est le code ? |
| ☐ | 2605.31593 | Brown et al., Stateful Online Monitoring Catches Distributed Agent Attacks | papier B |
| ☐ | 2504.10374 | Ctrl-Z | H6 ; 72,7 % ou 83,2 % |
| ☐ | 2605.26047 | Retrying vs Resampling in AI Control | H6 |
| ☐ | 2606.07612 | sondes et régime de consigne | H8, HC2b |
| ☐ | 2511.00554 | Blandfort et Graham, red-teaming de sondes | HC2 |
| ☐ | 2605.27958 | Kumar, Pressure-Testing Deception Probes | H8, HC2b |
| ☐ | 2506.14261 | Gupta et Jenner, RL-Obfuscation | Tr |
| ☐ | 2412.09565 | Bailey et al., Obfuscated Activations Bypass LLM Latent-Space Defenses | HC4 |
| ☐ | 2512.11949 | Neural Chameleons | HC4, H5 |
| ☐ | 2208.07610 | Koning et Grünwald | lemme |
| ☐ | 2601.20022 | Ramtin, Nain, Towsley, adversaire couvert | lemme |
| ☐ | 2005.07821 | attaques furtives sur systèmes cyber-physiques | lemme |
| ☐ | 2509.26238 | Beyond Linear Probes | T0.7 |
| ☐ | 2605.29178 | The Best-Laid SCHEMEs | papier B |
| ☐ | 2608.02698 | Ghanem, collusion en boîte noire entre mandants | papier B |
| ☐ | 2604.03968 | TraceGuard | papier B, HC5 |
| ☐ | 2510.09462 | Adaptive Attacks on Trusted Monitors (Terekhov, Panfilov et al.) | papier C, H7 |
| ☐ | 2604.13301 | Honeypot Protocol | H7 |
| ☐ | 2603.12277 | Prompt Injection as Role Confusion | HC3 |
| ☐ | 2602.14161 | When Benchmarks Lie | HC2 |
| ☐ | 2411.03336 | esquisses de safety cases (Balesni, Korbak et al.) | papier C |
| ☐ | 2504.05259 | How to evaluate control measures | papier A |
| ☐ | 2602.20628 | When can we trust untrusted monitoring? | papier C |
| ☐ | 2510.07192 | empoisonnement par ~250 documents | environnement (d) |
| ☐ | 2508.05625 | How Do LLMs Persuade? Linear Probes Can Uncover Persuasion Dynamics | nouveau : HC2, HC2b |

## Niveau 3 — voisins nouveaux et références de second rang — 41 documents

Voisins nouveaux trouvés le 4 octobre :
- 2601.05427 (Gauthier, Bach, Jordan, Anytime Detection of Strategic Deviations in Multi-Agent Systems) ;
- 2607.11751 et 2607.24893 (backdoors distribuées multi-agents) ;
- 2606.20746 (Amplify, Don't Create) ;
- 2604.08608 (Semantic Intent Fragmentation) ;
- 2506.10949 (Monitoring Decomposition Attacks… Sequential Monitors) ;
- 2411.17693 (Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats) ;
- 2609.06966 (MOLE) ;
- 2512.22154 (Practical challenges of control monitoring) ;
- 2605.11135 (Control Charts for Multi-agent Systems) ;
- 2606.07624 (Sequential statistical inference for LLMs) ;
- 2601.04603 (Next-generation Constitutional Classifiers).

Papier C, catalogues et attaques :
- 2509.26072 (The Silent Judge) ;
- 2604.21564 (Nogueira et al.) ;
- 2511.17220 (PARROT) ;
- 2601.13433 (Who Endorsed It?) ;
- 2605.23970 (Faithful or Fabricated?) ;
- 2403.17710 (JudgeDeceiver) ;
- 2505.13348, 2402.14016, 2504.18333, 2603.29403 ;
- 2504.20271 (Tillman et Mossing) ;
- 2505.06311 (InstructDetector) ;
- 2608.02657, 2606.22864, 2605.18918 (ESLD), 2604.22888 (RouteGuard) ;
- 2601.09923, 2505.22852 ;
- ✱ 2410.02736 (CALM, Justice or Prejudice?) ;
- ✱ 2402.10669 (Humans or LLMs as the Judge?) ;
- ✱ 2507.08794 (One Token to Fool LLM-as-a-Judge) ;
- 2505.23575 (CoT Red-Handed).

Fond statistique (lemme, théorème, T0.3) :
- ✱ 1810.08240 (Howard, Ramdas, McAuliffe, Sekhon, confidence sequences) ;
- ✱ 1007.1434 (Arias-Castro, Candès, Plan) ;
- ✱ 2203.03532 (E-detectors) ;
- ✱ 2210.01948 (Game-theoretic statistics and safe anytime-valid inference) ;
- ✱ 2212.07383 (Sequential Kernelized Independence Testing) ;
- Mei 2010, Biometrika (« Efficient scalable schemes for monitoring a large number of data streams ») ;
- Xie et Siegmund 2013, Annals of Statistics (« Sequential multi-sensor change-point detection »).

## Hors arXiv — pages à enregistrer en PDF

| ☐ | Source | Pour |
|---|---|---|
| ☐ | Billet LessWrong « Access to agent CoT makes monitors vulnerable to persuasion » (lesswrong.com/posts/Bvb97FpmxnKKebSjX) — et l'adresse du dépôt de code qu'il donne | 2607.08066 : code, licence |
| ☐ | Version atelier ICML 2025 « Persuade Me If You Can » (openreview.net, identifiant lY3YVJ84kS) | HC1 |
| ☐ | Billet du blog Alignment Science d'Anthropic « Diffuse AI Control on Fuzzy Tasks » (juin 2026), et tout lien vers du code | environnement (a) |
| ☐ | Billet d'Anthropic sur le sabotage subtil par chercheurs automatisés (mars 2025) | environnement (a) |
| ☐ | Billet de l'institut britannique sur le contrôle boîte blanche (juillet 2025) ; « The Case for White Box Control » (LessWrong, 2025) | H1 |
| ☐ | Redwood Research : « How can we solve diffuse threats like research sabotage with AI control? » (Hebbar, avril 2025) ; « Catching AIs red-handed » (2024) | lemme, H7 |
| ☐ | Hopman et al. 2025, « Untrusted AIs Can Exploit Feedback in Control Protocols » | H7 |
| ☐ | Meincke et al., PNAS 2026 (et le préprint « Call Me A Jerk ») | HC1 (chiffres) |
| ☐ | Fiches de licence HuggingFace : meta-llama/Llama-3.1-8B-Instruct, meta-llama/Llama-3.2-3B-Instruct, Qwen/Qwen2.5-7B-Instruct, mistralai/Mistral-7B-Instruct-v0.3 ; organisation sandbagging-games ; jeu aaronrose227/narcbench ; autoencodeurs Llama Scope | licences (D1, D2, T0.6, T0.7) |

## Ce que les PDF ne remplacent pas
Les PDF permettent la vérification sur source primaire (T0.2 proprement dite) et la remontée des bibliographies, mais pas la recherche **affirmative** de travaux inconnus (R8) ni la recherche des papiers qui *citent* une référence.
Pour cela, il faut des recherches web : une session neuve (nouveau budget de 200) suffit pour les zones les plus risquées, dans cet ordre :
1. accumulation séquentielle sur sondes (H2) ;
2. statistique spatio-temporelle et suites de NARCBench (bascule) ;
3. gain continu des juges (HC1) ;
4. sondes contre juges (HC2) ;
5. usurpation stylistique (HC3) ;
6. balayage de récence depuis le 14 septembre.
