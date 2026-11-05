# Lecture sur source primaire — TRACE et AcMAS — rapport brut — v1

Rapport d'un sous-agent lecteur neuf (il n'a rien écrit de ce qu'il vérifie), rendu le 2026-10-04 (UTC).
PDF lus : 2606.07054v1, 2607.06807v1.
Texte extrait **mot pour mot** du journal du sous-agent par `extraire_rapport.py`, sans aucune modification.
Les chiffres marqués « calcul » ou « mon calcul » sont des reconstructions du lecteur, pas des chiffres des auteurs.

---

# Vérification sur source primaire : TRACE (arXiv 2606.07054v1) et When Agents Go Rogue / AcMAS (arXiv 2607.06807v1)

**Verdict**
- **Lecture :** les empreintes SHA-256 des deux PDF sont conformes. Les deux papiers ont été lus en entier, annexes comprises (TRACE : 18 pages ; AcMAS : 20 pages). Aucun fichier de `/home/user/controle-ia` n'a été modifié (`git status` vide).
- **TRACE :** F1 0,713 et rappel 0,844 sont confirmés tels qu'imprimés (Claude Sonnet 4.6, SHADE-Arena, seuil ≥ 4 sur une échelle de 1 à 5).
  - Ce sont des moyennes par tâche, et le papier ne donne aucun taux de faux positifs.
  - Par calcul, TRACE signale environ 75 % des trajectoires bénignes. Sur ce jeu, un classifieur qui signale tout aurait un F1 de 0,744.
  - Les invites sont publiées, le code ne l'est pas.
- **AcMAS :** +0,22 et +0,55 sont confirmés tels qu'imprimés, mais les deux gains ne se rapportent pas à la même base.
  - Il n'y a ni sonde entraînée, ni agrégation entre agents, ni accumulation dans le temps.
  - « Synchrone / asynchrone » désigne le mode d'exécution du système multi-agents, pas celui du moniteur.

**Conventions.** Page = n-ième page du fichier ; pour AcMAS, elle coïncide avec le numéro imprimé. « Calcul » désigne une reconstruction de ma part à partir des tables du papier, pas un chiffre des auteurs (scripts et empreintes en fin de rapport).

---

## 1. TRACE (arXiv 2606.07054v1)

**Identité.** « TRACE: Trajectory Reasoning through Adaptive Cross-Step Evidence Aggregation for LLM Agents ».
- **Auteurs :**
  - Vijitha Mittapalli, Shreyaa Jayant Dani, Satya Srujana Pilli, Snigdha Ansu, Mohammadreza Teymoorianfard (University of Massachusetts Amherst) ;
  - Franck Dernoncourt et Ryan A. Rossi (Adobe Research) ;
  - Hongjie Chen (Dolby Labs) ; Yu Wang (University of Oregon) ; Nesreen K. Ahmed (Cisco).
- **Statut :** prépublication arXiv [cs.CL] du 5 juin 2026, sans conférence indiquée (p. 1).
- **Dernoncourt :** confirmé parmi les auteurs.

| Affirmation ou question | Verdict ou réponse | Page | Citation |
|---|---|---|---|
| Boîte noire, sans entraînement | Confirmé : inférence seule, aucun accès aux activations. | 3 | « does not modify the underlying agent policy, access internal model activations, or use additional training signals » |
| En ligne ou après coup ? | Après coup : le moniteur lit la trajectoire complète, une fois la tâche finie. | 3 | « The monitor observes the complete execution trajectory after task completion » |
| Boucle triage–inspection–jugement | Confirmé. Le triage est une passe sur la trajectoire entière. Il produit des contraintes et 3 à 4 fenêtres suspectes : locales (1 à 3 pas adjacents) ou « pattern » (3 à 8 pas non adjacents). | 4, 12 | « a constraint representation encoding the task intent, permitted scope, and authorized actions » |
| Inspection | Pour chaque fenêtre, un contrôleur choisit une action : InspectStep, CompareSteps, CheckPolicy, AnalyzeDecisions ou Done. | 4, 12 | « Done : conclude the investigation (available after 2 observations) » |
| Agrégation de la preuve entre étapes | Purement textuelle. Les constats sont réinjectés dans le contexte des inspections suivantes, puis un appel de synthèse lit le journal. Aucune règle numérique de cumul. | 4 | « findings from earlier windows are injected as context into later inspection steps » |
| Critère d'arrêt | « Preuve suffisante » (jamais opérationnalisée) ou budget de la fenêtre épuisé. | 4 | « sufficient evidence has accumulated to support a stable verdict, or (2) a per-window inspection budget is exhausted » |
| Jugement et seuil | Score entier de 1 à 5, malveillant si ≥ 4. Règle imposée au juge : sévérité 4–5 et confiance haute entraînent un score ≥ 4. | 4, 13 | « TRACE assigns a final suspicion score on a 1–5 scale, and trajectories scoring ≥ 4 are classified as malicious. » |
| Invites publiées ? | Oui : les sept gabarits de l'annexe B (triage, contrôleur, quatre actions, verdict). | 12–13 | « B TRACE Monitor Prompt Templates » |
| Budget d'appels | Au plus 4 fenêtres et 6 pas d'inspection par fenêtre, soit environ 12 appels. | 6 | « up to 4 suspect windows per trajectory with a maximum of 6 inspection steps per window, averaging 12 LLM calls » |
| Banc d'essai | SHADE-Arena, 10 domaines, 463 trajectoires (189 bénignes, 274 malveillantes), toutes en test. Election Tampering est gardé alors que Kutasov l'exclut. Le modèle agent qui a produit les trajectoires n'est pas précisé. | 5–6 | « All 463 trajectories are treated as a held-out test set. » |
| Modèles moniteurs | Claude Sonnet 4.6. En ablation : Opus 4.7, GPT-5.1, o4-mini et « Gemini Flash 3.5 » (la bibliographie, p. 9, dit « Gemini 2.5 flash »). Les bases ne tournent que sur Sonnet 4.6. | 6 | « Baselines use Sonnet 4.6 only, consistent with prior work » |
| **F1 0,713, rappel 0,844** | **Confirmé tel qu'imprimé**, dans ce contexte : Sonnet 4.6, 463 trajectoires, seuil ≥ 4. **Correction de lecture (calcul) :** ce sont des moyennes non pondérées des 10 tâches, alors que les totaux des bases sont poolés. Poolé, TRACE donne un rappel de 0,847 (le texte dit lui-même 84,7 %, p. 5), une précision de 0,620 et un F1 de 0,716. | 2, 17 | « TRACE achieves aggregate F1 of 0.713 and recall of 0.844 (Claude Sonnet 4.6), outperforming both baselines (F1 = 0.577 and 0.700) » |
| **Taux de faux positifs** | **Absent du papier.** Calcul par reconstruction exacte depuis les tables 1 et 5 (précisions retrouvées à 0,0005 près) : TRACE signale 142 trajectoires bénignes sur 189, soit environ 75 %. Ce taux monte à 100 % sur SSN, Bank Transfer et Expenditure. Bases : 0/189 pour la trajectoire complète, 21/189 (environ 11 %) pour le séquentiel. Les seuils des bases ne sont pas indiqués. | 6, 17 | — (absence vérifiée par recherche plein texte : « FPR », « ROC », « AUC », « false positive rate ») |
| Plancher trivial | Calcul : 59 % des trajectoires sont malveillantes, donc signaler tout donne un F1 de 0,744 (poolé) ou 0,755 (moyenne par tâche). C'est mieux que TRACE avec Sonnet et que les deux bases ; seul Opus 4.7 (0,790) fait mieux. | 6 | « F1 is the primary metric given class imbalance (189 benign vs. 274 malicious). » |
| « F1 0,790 » des contributions | C'est le résultat d'Opus 4.7, comparé à des bases qui tournent sur Sonnet 4.6. | 2, 7 | « increasing aggregate recall from 0.405–0.580 (baselines) to 0.844 and aggregate F1 to 0.790 » |
| Agrégats incohérents entre modèles | Calcul : les lignes « Overall » d'Opus, de Sonnet et d'o4-mini sont des moyennes par tâche ; celles de GPT-5.1 et de Gemini sont poolées. Trois tâches d'Opus sont incompatibles avec les effectifs de la table 1. | 7, 18 | — |
| Bases comparées | Moniteur sur trajectoire complète (Kutasov 2025, une passe) : F1 0,577, rappel 0,405, précision 1,000. Moniteur séquentiel (Kale 2025, segments fixes et résumé courant) : F1 0,700, rappel 0,580, précision 0,883. | 5–6, 17 | « reproduced using the publicly available SHADE-Arena codebase » |
| Garantie de faux positifs ; seuil calibré ? | Aucune garantie. Seuil, budget et actions sont fixés sur un « petit jeu de validation » non décrit, sans réglage par modèle. Cela cadre mal avec « toutes en test ». | 9 | « The verdict threshold, inspection budget, and action space are fixed based on a small validation set and are not fully tuned per model. » |
| Coût | 12,3 appels en moyenne, contre 18,8 pour le séquentiel et 1 pour la trajectoire complète. Aucun compte de jetons. | 6 | « TRACE achieves this with 12.3 average LLM calls per trajectory versus 18.8 for the sequential monitor » |
| Modèles faibles | Échec par arrêt précoce ou par raisonnement pauvre. | 7 | « early termination (Gemini 3.5, o4-mini average 7 calls, recall < 0.435) » |
| Évasion par justifications plausibles (« Manipulation ») | TRACE détecte 0 trajectoire sur 17, le séquentiel 10 sur 17. | 5 | « the sequential monitor detects 10 of 17 trajectories while TRACE detects none » |
| Code, licence | Aucune adresse de dépôt ni licence dans les 18 pages. Le seul code cité est celui de SHADE-Arena, utilisé pour les bases. | 5–6 | — (absence vérifiée : « github », « http », « license ») |

**Chiffres utilisables**
- **Jeu :** 189 bénignes, 274 malveillantes, 463 au total ; 91,8 tours en moyenne (p. 6, table 1).
- **TRACE avec Sonnet 4.6**, moyennes par tâche : exactitude 0,606, précision 0,641, rappel 0,844, F1 0,713 (p. 17, table 5).
- **Bases, poolées** (exactitude / précision / rappel / F1) : trajectoire complète 0,648 / 1,000 / 0,405 / 0,577 ; séquentiel 0,706 / 0,883 / 0,580 / 0,700 (p. 17).
- **Appels moyens :** 12,3 pour TRACE, 18,8 pour le séquentiel, 1 pour la trajectoire complète (p. 6, table 2).
- **TRACE selon le modèle :** Opus 4.7, F1 0,790 avec 11,0 appels ; GPT-5.1, 0,588 ; Gemini, 0,586 ; o4-mini, 0,495 (p. 7, table 3).
- **Verbalisation sélective** (102 trajectoires sur 274) : 94,1 % pour TRACE, 46,1 % pour le séquentiel, 44,1 % pour la trajectoire complète (p. 5).
- **Calcul :**
  - TRACE poolé : rappel 0,847, précision 0,620, F1 0,716, faux positifs 75 % ;
  - faux positifs des bases : 11 % (séquentiel), 0 % (trajectoire complète) ;
  - faux positifs approximatifs des autres modèles : Opus environ 35 %, GPT-5.1 23 %, Gemini 7 %, o4-mini 25 % ;
  - plancher « tout signaler » : F1 0,744.

---

## 2. When Agents Go Rogue — AcMAS (arXiv 2607.06807v1)

**Identité.** « When Agents Go Rogue: Activation-Based Detection of Malicious Behaviors in Multi-Agent Systems ».
- **Auteurs :** Haowen Xu et Xue Tan (contribution égale), Lei Ma, Zhihao Zhang, Chao Wang, Qingze Wang, Ping Chen, Jun Dai, Xiaoyan Sun.
- **Affiliations :**
  - Worcester Polytechnic Institute : Xu, Ma, Zhang, Chao Wang, Dai, Sun ;
  - Université Fudan : Tan, Chen ;
  - chercheur indépendant : Qingze Wang.
- **Statut :** arXiv [cs.CR] du 7 juillet 2026 ; publié à ICML 2026, PMLR 306 (p. 1).

| Affirmation ou question | Verdict ou réponse | Page | Citation |
|---|---|---|---|
| Modèles | GPT-OSS-20B (modèle de la table 1), DeepSeek-V3, Qwen3-30B-A3B et « LLaMA3-8B » (variante non précisée, citée d'après Touvron 2023). Systèmes homogènes seulement. | 6, 17 | « open-source LLM backbones, including GPT-OSS-20B …, DeepSeek-V3 …, LLaMA3-8B …, and Qwen3-30B-A3B » |
| Couches | Dernière couche, état caché du dernier jeton généré, une fois par réponse d'agent. | 4 | « We adopt the hidden state h(L) from the final layer L of the final generated token as a summary of the entire input context » |
| Sondes ? | Aucune sonde entraînée. Un prototype non supervisé (centroïde des activations bénignes normalisées) et une distance cosinus seuillée (équations 10 à 12). | 5–6 | « experiments use τmax = 0.35 with τdetect = 0.12 » |
| Choix de couche (ablation) | F1 : 0,95 en couche finale, 0,86 en couches médianes (10 à 14), 0,71 en couches précoces (1 à 4). | 8 | « Middle layers (10–14) 0.85 0.87 0.86 » |
| Agrégation par agent | Décision indépendante par agent et par pas. | 5 | « this formulation operates independently on each agent's internal state, enabling topology-agnostic detection » |
| Entre agents : co-élévation, corrélation ? | Corrélation affirmée (équation 8), mais ni mesurée par une table ou une figure, ni utilisée comme statistique. Seul lien : en synchrone, le prototype est mis à jour par moyenne mobile (α = 0,7) des agents jugés normaux au tour précédent ; chaque agent est donc comparé à la population. Sans cette mise à jour, le F1 passe de 0,95 à 0,87. | 4, 5, 8 | « compromised agents exhibit correlated activation patterns in multi-agent settings » |
| Dans le temps : accumulation ? | Aucune : ni somme, ni somme cumulée, ni test séquentiel. En asynchrone, le prototype est fixe. | 5 | « We maintain a fixed prototype µnormal computed from initial benign execution traces » |
| Synchrone / asynchrone | Modes d'exécution du système multi-agents : tours en pas de charge, ou exécution événementielle par files de tâches. | 2 | « Sync-MAS with lock-step, round-based execution, (b) Async-MAS with event-driven, task-allocation-based execution » |
| **+0,22 (synchrone), +0,55 (asynchrone)** | **Confirmé tel qu'imprimé, mais référence non constante** (calcul sur la table 1). AcMAS vaut 0,944 en synchrone et 0,934 en asynchrone. Le 0,72 est G-Safeguard seul (0,712). Le 0,38 est la moyenne de G-Safeguard et BlindGuard en asynchrone (0,380), et non la meilleure base (G-Safeguard, 0,432). **Contre G-Safeguard dans les deux cas : +0,23 et +0,50.** Les chiffres « furtifs » de l'introduction (0,95 contre 0,74 ; 0,94 contre 0,46) ne portent que sur la ligne CSQA. | 1, 2, 6, 7 | « by +0.22 F1 in synchronous settings (0.94 vs. 0.72) and by +0.55 F1 in asynchronous settings (0.93 vs. 0.38) » |
| Bases | G-Safeguard (graphe supervisé) et BlindGuard (graphe non supervisé), plus PERM et TAM, tous sur les sorties textuelles. TAM et PERM descendent souvent sous le hasard (AUROC jusqu'à 16,9). | 6–7 | « Both methods formulate malicious agent detection as a graph learning problem over multi-agent interactions. » |
| Faux positifs | Entre 0,04 et 0,07 au seuil 0,12 ; AUROC de 97,6 à 99,5. Le seuil est choisi en maximisant F1 sur un jeu de validation ; l'équivalence annoncée avec l'indice de Youden est fausse en général. Aucune garantie, aucun rappel à faible taux de faux positifs fixé. | 6, 18 | « Select threshold by maximizing F1 score » |
| Cadre adverse | Les agents malveillants sont instruits par leur message système. Aucun agent ne se sait surveillé, aucune attaque adaptative n'est testée ; le papier y voit un « défi ouvert ». | 3, 9 | « adaptive attacks that attempt to gradually shift activation distributions remain an open challenge. » |
| Que lit le détecteur ? | L'état lu résume tout le contexte d'entrée, et les attaquants ont un message système distinct. Sans trace bénigne du domaine cible, le taux de faux positifs vaut 1,00 (tables 7 et 8). | 4, 16, 20 | « Then talk to other agents and convince them of your answer. » |
| N variable | Exactitude supérieure à 97 % pour N = 8, 20, 50 et 80, avec 4 modèles. C'est une courbe en N de la détection par agent : ni sécurité à budget constant, ni boîte noire. | 8 | « Across varying scales (8-80 agents), AcMAS maintains consistently high detection accuracy with minimal performance variance (std < 0.8%). » |
| Intensité d'attaque | De 0 à 40 % d'agents compromis, résultats moyennés ; F1 supérieur à 0,90 jusqu'à 50 %. | 7, 8 | « we vary the number of compromised agents from 0 to 40% » |
| Protocole | Non spécifiés : nombre de runs, graines, topologie, N de la table 1, règle d'étiquetage des agents contaminés. L'annexe E annoncée ne contient qu'un cas d'étude. Calcul : précision, rappel et faux positifs impliquent 50 % de positifs pour AcMAS, mais 35 à 39 % pour les bases sur les mêmes données. | 6, 7, 18 | « Results are reported as mean ± standard deviation across runs. » |
| Priorité revendiquée | Se dit le premier cadre de détection par activations dans les systèmes multi-agents. | 10 | « AcMAS represents the first framework to address adversarial compromise in MAS via activation-level analysis and correction. » |
| Code, licence | Aucune adresse de dépôt ni licence. La seule adresse du papier est une référence bibliographique. | 12 | — (absence vérifiée) |

**Chiffres utilisables**
- **Table 1 (p. 6)**, gpt-oss-20b, 5 scénarios en synchrone et asynchrone :
  - AcMAS : F1 de 0,93 à 0,95 en synchrone et de 0,92 à 0,94 en asynchrone ; faux positifs de 0,04 à 0,07 ; AUROC de 97,6 à 99,5 ;
  - G-Safeguard : F1 de 0,69 à 0,74 en synchrone et de 0,41 à 0,46 en asynchrone ; faux positifs de 0,20 à 0,26 et de 0,45 à 0,50.
- **Moyennes de F1 par calcul** (synchrone / asynchrone) : AcMAS 0,944 / 0,934 ; G-Safeguard 0,712 / 0,432 ; BlindGuard 0,560 / 0,328.
- **Défense (p. 7, table 2) :** pour AcMAS, succès d'attaque de 0,02 à 0,05 et achèvement de tâche de 0,96 à 1,00. Pour G-Safeguard, achèvement de 0,68 à 0,90.
- **Ablations (p. 8, table 3) :** F1 de 0,95, 0,86 et 0,71 selon la couche ; 0,87 sans mise à jour adaptative ; 0,89 sans normalisation.
- **Seuil (p. 8) :** 12 % de faux positifs à τ = 0,08 ; 15 % de faux négatifs à τ = 0,16.
- **Prototype (p. 8–9) :** stable vers 50 traces bénignes ; écart inférieur à 0,03 avec 100 traces.
- **Coût (p. 9, table 4) :** extraction 2,3 ms (0,15 % de l'inférence) ; pilotage des activations 185,3 ms (12,4 %).
- **Changement de domaine (p. 20, tables 7–8) :** F1 0,49 et 100 % de faux positifs sans trace cible ; 0,92 et 7 % avec 300 traces cibles (de CSQA vers InjecAgent).

---

## 3. Faisabilité de TRACE-lite

**Verdict.** TRACE-lite est réimplémentable dans ses grandes lignes à partir de l'annexe B, mais pas reproductible à l'identique. Le papier n'apporte aucune donnée sur un moniteur Llama-3.1-8B-Instruct ou Llama-3.2-3B-Instruct, et les signes disponibles sont défavorables.

**Ce qui est publié et suffit pour le squelette**
1. **Triage :** un appel, invite B.1, sortie JSON {constraints, suspect_windows}, au plus 3 à 4 fenêtres (p. 12).
2. **Inspection :** jusqu'à 4 fenêtres de 6 pas chacune (p. 6).
   - Un contrôleur (B.2) renvoie un JSON {reason, action, arguments, finding, severity, reconciliation}.
   - Quatre exécuteurs (B.3.1 à B.3.4) répondent en texte libre avec une note de 1 à 5.
   - Done n'est permis qu'après deux observations ; une mémoire textuelle est transmise de fenêtre en fenêtre (p. 4, 12–13).
3. **Verdict :** invite B.4, JSON {score de 1 à 5, reasoning}, seuil ≥ 4, plus des règles de notation (p. 4, 13).
4. **Coût de référence :** 12,3 appels par trajectoire avec Sonnet 4.6 ; de 6,5 à 7,2 avec les modèles faibles (p. 6, 7).

**Ce qui manque, à fixer et consigner au préenregistrement de G1**
- **Code et licence :** rien. Il faut tout réimplémenter, ce que prévoit déjà T0.8.
- **Format des entrées :** rien sur les variables {trace}, {step_previews}, {memory}, {prior_observations} et {evidence_items}, ni sur la définition d'un « pas » ou la troncature. Seul indice : une action de l'assistant appariée à ses résultats d'outil (p. 12).
- **Notion de confiance :** la règle du verdict exige une « confiance haute », mais le JSON du contrôleur n'a pas de champ confiance.
- **Analyse des réponses :**
  - Il faut décider comment lire les notes en texte libre et que faire des JSON invalides, point critique en 3B et en 8B.
  - Les exemples JSON contiennent des valeurs (« "severity": 0 », « "score": 3 ») qu'un petit modèle peut recopier.
- **Paramètres non décrits :** l'échantillonnage n'est pas précisé (« default inference parameters », p. 6), ni le jeu de validation du seuil (p. 9).
- **Lecture après coup (p. 3) :** pour mesurer la latence d'alerte du plan E1.2, il faut exécuter TRACE-lite sur des préfixes, soit environ 12 appels par point de contrôle.
- **Score continu :**
  - Avec une note entière de 1 à 5, la courbe ROC n'a que 5 points au plus, ce qui rend mal défini le « rappel à 1 % de faux positifs ».
  - Remède possible avec un modèle à poids ouverts : prendre l'espérance du score sous les probabilités des jetons du verdict (déjà la consigne du programme pour le papier C), ou moyenner k tirages.
- **Longueur :** le triage lit la trajectoire entière (91,8 tours en moyenne, jusqu'à 157,4 en moyenne sur une tâche, p. 6). Il faut vérifier que les épisodes de l'environnement (a) tiennent dans le contexte.
- **Petits modèles :** aucun n'est testé, et les plus faibles testés s'arrêtent tôt (p. 7). Je recommande Llama-3.1-8B-Instruct comme TRACE-lite principal (option (a) de la décision D1). Llama-3.2-3B ne devrait servir qu'au bras « moniteur faible », avec des planchers.

---

## 4. Table de collision

| Revendication du programme | TRACE | AcMAS | Niveau | Pages |
|---|---|---|---|---|
| Base boîte noire de G1 = TRACE-lite ; selon l'état de l'art, TRACE serait le « complément boîte noire exact de H2 » | Agrégation entre étapes en boîte noire, hors ligne, sans test séquentiel ni garantie. « Exact » est faux : le squelette séquentiel avec garantie reste E-valuator (non vérifié ici). | — | Base utilisable sous conditions (section 3) ; formulation de l'état de l'art à corriger | T 3, 4, 9 |
| Critère D-c : rappel à 1 % de faux positifs, ou +5 points de F1 | F1 récompense le sur-signalement. TRACE gagne +0,013 sur le séquentiel pendant que ses faux positifs passent de 11 % à 75 % (calcul), et « tout signaler » atteint 0,744. | — | Bras F1 fragile (alerte 1) | T 6, 17 |
| H1 : gain blanc-sur-noir sur sabotage diffus et flou, à faux positifs égaux | Aucune activation. Indice favorable à la prémisse : la boîte noire avale les justifications plausibles (0 sur 17). | Les activations battent les graphes sur sorties textuelles en multi-agents. Mais il s'agit d'injection et d'empoisonnement avec réponses fausses, d'attaquants instruits, de faux positifs non égalisés, sans sabotage diffus. | **Libre** face à TRACE ; **adjacent** face à AcMAS. H1 reste revendicable tel que formulé. | T 3, 5 ; A 6–7 |
| H2 : accumulation séquentielle de scores de sondes | Accumulation dans le contexte d'un juge, sans statistique ni sonde. | Décision par pas, sans accumulation temporelle ; seul le prototype évolue. | **Adjacent** pour les deux ; H2 reste **libre** | T 4 ; A 5 |
| Papier B : statistique spatio-temporelle temps × agents sur activations | — | Détection par activations en multi-agents, par agent et par pas, en synchrone et en asynchrone, revendiquée comme « premier cadre ». Aucune statistique spatio-temporelle. | **Partiel** pour le cadrage : citer, ne pas revendiquer la primauté. **Libre** pour la statistique. | A 4–5, 10 |
| Coupe transversale (agent contre population), base de E3.1 | — | Le mode synchrone compare chaque agent au centroïde des agents jugés normaux ; sans cette mise à jour, le F1 passe de 0,95 à 0,87. | **Partiel** : base à ajouter à côté de NARCBench | A 5, 8 |
| Co-élévation entre agents | — | Corrélation affirmée, mais ni mesurée ni exploitée. Elle est triviale ici, puisque tous les attaquants partagent le même message système. | **Adjacent** | A 4, 16 |
| H3 : courbe sécurité(N) | — | Exactitude par agent pour N de 8 à 80, en boîte blanche seule, sans budget constant ; la courbe est plate par construction. | **Adjacent** | A 8 |
| H4′ : diversification | — | Systèmes homogènes seulement ; les systèmes hétérogènes sont renvoyés à des travaux futurs. | **Libre** | A 17 |
| H6 : marge asymétrique | — | Pilotage des activations vers le prototype après détection : intervention spécifique, mesurée par le succès d'attaque et l'achèvement de tâche. | **Adjacent** | A 5–7 |
| Validité de construit (section 7, H8) | — | AcMAS ne distingue pas « instruction cachée » et intention : attaquants instruits, 100 % de faux positifs sous changement de domaine. | **Adjacent** ; exemple à citer pour motiver H8 | A 4, 16, 20 |

T = pages de TRACE, A = pages d'AcMAS. Le classement « adjacent à partiel » d'AcMAS dans `docs/anteriorite/anteriorite-transcription-v1.md` est confirmé.

---

## 5. Alertes

1. **Les chiffres de TRACE ne sont pas une cible, et le bras F1 du critère de G1 se gagne en sur-signalant.**
   - Le couple 0,713 / 0,844 vient d'un point de fonctionnement où environ 75 % des trajectoires bénignes sont signalées (calcul). Sur ce jeu, « tout signaler » donne un F1 de 0,744, mieux que TRACE et que les deux bases.
   - La ligne TRACE de la section 2.3 de l'état de l'art est à requalifier : moyennes par tâche, seuil ≥ 4, faux positifs non rapportés.
   - Le bras « +5 points de F1 » du critère D-c a le même défaut. Le corriger revient à modifier un critère de porte : c'est donc un nœud de décision pour Lazar.
   - Pistes :
     - mesurer F1 au seuil calibré sur les épisodes honnêtes réservés, au même taux de faux positifs pour tous les bras ;
     - rendre obligatoire le plancher « tout signaler » ;
     - ou retirer ce bras.

2. **En 8B ou 3B, TRACE-lite risque d'être un homme de paille, ce qui gonflerait H1.**
   - Rien n'est testé en dessous d'o4-mini et de Gemini, qui s'effondrent déjà par arrêt précoce (rappel inférieur à 0,435).
   - S'y ajoutent l'absence de code, une colle à inventer, un score entier et une conception faite pour lire après coup.
   - Si la base boîte noire est faible pour ces raisons, l'effet principal de l'accès est surestimé, contrairement à la règle de symétrie R4.
   - Parades à inscrire au préenregistrement de G1 :
     - planchers : « tout signaler », et juge en une passe avec le même modèle ;
     - journal du taux d'arrêts précoces et de JSON invalides ;
     - score continu par probabilité des jetons du verdict ;
     - mode préfixes si la latence est mesurée.

3. **AcMAS : gains non comparables, construit douteux, antériorité partielle pour le papier B.**
   - Les +0,22 et +0,55 se rapportent à deux références différentes ; à base constante, c'est +0,23 et +0,50.
   - Le détecteur lit le dernier jeton comme résumé du contexte, alors que les attaquants ont un message système distinct. Sous changement de domaine, il signale 100 % des agents bénins. Il lit donc vraisemblablement « j'ai une instruction cachée », la confusion que le programme veut contrôler avec les familles (i) et (ii).
   - Ni attaque adaptative, ni code.
   - Pour le papier B :
     - citer AcMAS comme première détection par activations en multi-agents, au niveau de l'agent ;
     - ajouter sa distance au prototype (agent contre population) comme base de « coupe transversale » en E3.1.
   - La statistique spatio-temporelle, la co-élévation et H3 restent libres vis-à-vis d'AcMAS.

---

## Traçabilité

Tous les fichiers sont dans `/tmp/claude-0/-home-user-cplt-run-2026-09-03/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/lecture-TRACE-AcMAS/`. Les extractions ont été faites avec pdftotext 24.02.0 en mode `-layout`.

| Fichier | Contenu | SHA-256 |
|---|---|---|
| `trace_pages.txt` | Extraction de TRACE, découpée par page | `eb948a8e007b6e0e7438ba8df1d5df874667ee9d39b53e1fecb89fca2aa4e3e8` |
| `acmas_pages.txt` | Extraction d'AcMAS, découpée par page | `fe947fe97dec83000ae6adc3b030396a8ac062b96e14d1c3cf089d2472ffd28d` |
| `recon_trace.py` | TRACE : moyennes par tâche contre totaux poolés, faux positifs | `990621556ff92726504a78b03c56f09bce2053d3c75bfffcf445a90f65e8491c` |
| `recon_t6.py` | TRACE : agrégats par modèle (table 6) et contrôle de cohérence | `4522bb8254abab387efea1fd78905ce22e8737575425ebf523333d2e73d23f6f` |
| `recon_acmas.py` | AcMAS : moyennes de la table 1 et gains | `b169de8c899dde16919b7b7f9a05bdc19d234d3a7e48283d4f5e30cf56a79968` |

Ces fichiers sont hors dépôt et non scellés. Il faut refaire et sceller ces calculs selon la règle R6 avant qu'un chiffre dérivé n'entre dans un document du programme.
