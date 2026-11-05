# Lecture de niveau 2, lot 2, A4 « protocoles de contrôle » : rapport du lecteur

- **Lecteur** : sous-agent neuf ; n'a écrit aucun des textes vérifiés.
- **Date** : 6 octobre 2026, de 16 h 15 à 16 h 45, temps universel coordonné (UTC).
- **Consignes appliquées** (lues en entier) : `scratchpad/lot2/consigne-commune.md` et `scratchpad/lot2/consignes-A4-protocoles-controle.md`.
- **Texte de référence** : `pdftotext -layout`, une extraction par page ; toute page citée est le rang de la page dans le fichier.
- **Rien n'a été modifié sous `/home/user/controle-ia`** par ce lecteur. `git status` y montre cinq fichiers modifiés ou nouveaux entre 16 h 38 et 16 h 40 : `pilote_a` dans le code et les tests, scripts `t05`. Ils viennent d'une autre session ; toutes mes écritures sont dans `scratchpad/lecture-lot2-A4/`. Lecture seule : les six fichiers, les lignes citées de l'état de l'art et, pour l'antériorité, les énoncés de H7, HC1, HC2b et du papier B dans `docs/programme-controle-ia-v2.md` (lignes 96 à 116) et dans `docs/decisions/decision-N-005-N-006-v1.md` (section 1).
- **Convention** : les citations anglaises sont entre « » et reproduites mot pour mot ; elles sont toutes contrôlées par script (dernière section). Les titres d'articles, noms de modèles et de jeux de données sont laissés tels quels, en anglais.

## En-tête : fichiers lus et empreintes

Empreintes SHA-256 (algorithme de hachage sécurisé à 256 bits), calculées par `sha256sum -c` contre la liste des consignes, avant toute lecture.

| fichier PDF (Portable Document Format) | pages | empreinte SHA-256 calculée | comparaison | lecture |
|---|---|---|---|---|
| 2510.09462v2.pdf | 52 | 96c16e33b27b9633b324acecfe29e1bfa9de7052143fb854824aad70a649d7f7 | conforme | partielle (plus de 30 pages), voir § 1 |
| 2411.03336v2.pdf | 46 | 46b4901a0f0c2a63ae90247b611b619fc9ca22d4129bdfdf5608e9148c4bca7e | conforme | entière, bibliographie parcourue, voir § 2 |
| 2504.05259v1.pdf | 28 | 6c433161e5d3bfdf85ddd262083e711e5ff7d0c2b3d232f1ecd35c94e7130a24 | conforme | entière |
| 2602.20628v2.pdf | 58 | b7d4663ace86c1cf9f730509c39ef0138022ccf4b72ae7242892b3a7e5f9d0bf | conforme | partielle (plus de 30 pages), voir § 4 |
| 2604.03968v1.pdf | 19 | eb49aa426debb55164675881d6af91c26e438e408d460f2d28428c022e9c1c27 | conforme | entière |
| 2604.13301v1.pdf | 8 | fc09ad6f0202284a8e99009252da573274393c69fcc22b9022ba8fdd07ef5cd3 | conforme | entière |

Six empreintes conformes sur six. Les lignes 90, 91, 93 et 139 de `docs/etat-de-l-art-controle-ia-v1.md` ont été relues sur disque : leur texte est celui des consignes.

## Synthèse (dix lignes au plus)

1. **Introuvable** : la venue « ICLR 2026 » de 2510.09462 est absente du PDF empreinté (seul Hasan la donne) ; le reste de la ligne 91 est confirmé.
2. **2411.03336, corrigé** : auteurs (Korbak 5e sur 16, 2e = Hobbhahn) ; protocole sondes + surveillance non fiable = exemple fictif, sondes « pas encore validées » ; antériorité confirmée au niveau de l'idée, et plus ancienne (« coup probes », Roger, 2023).
3. **2504.05259, corrigé (mineur)** : « aucun échantillon *fiable* » des internes d'un vrai comploteur ; surapprentissage boîte blanche confirmé.
4. **TraceGuard, corrigé et réservé (R4)** : 0,206/0,616 et 95 %/0 % viennent de deux variantes et de deux séries ; sécurité sans taux de faux positifs fixé ; collusion non jouée ; base de confiance à score unique aussi à 0 % ; références erronées, effectifs incohérents.
5. **Honeypot Protocol, corrigé** : pot de miel de contexte, pas une riposte ; matériel d'implémentation pour E3.4, pas un résultat sur H7. 2602.20628 : identité confirmée.
6. **HC1 touchée en partie** (2510.09462) : des moniteurs de contrôle adoptent le score injecté, sous les solutions honnêtes, à une intensité, en score écrit. Destination libre testée, graduation par famille et opposition juge/sonde restent libres. La lecture par probabilité du jeton est déjà une technique employée (2411.03336, p. 25 ; 2602.20628, p. 6).
7. **Papier B** : voisinage boîte noire seulement (reconnaissance de soi entre copies, 2602.20628 ; attaques simultanées d'instances, 2504.05259).
8. **Non occupés** : H2 (hors champ explicite en 2602.20628), H1 (seulement affirmée dans un exemple fictif de 2411.03336), lemme, théorème négatif, transposition jeton → action, HC2b.
9. **Citations** : 141 contrôlées, 0 échec (2 fautes de transcription corrigées au premier passage) ; test R5 réussi.

---

## 1. Adaptive Attacks on Trusted Monitors Subvert AI Control Protocols [pdf: 2510.09462v2]

### Identité

- **Titre** : Adaptive Attacks on Trusted Monitors Subvert AI Control Protocols.
- **Auteurs (7)** : Mikhail Terekhov, Alexander Panfilov, Daniil Dzenhaliou (contributions égales, ordre tiré aux dés), Caglar Gulcehre, Maksym Andriushchenko, Ameya Prabhu, Jonas Geiping (encadrement égal pour les trois derniers).
- **Version et date** : arXiv 2510.09462v2, 2 mars 2026, catégorie apprentissage automatique (cs.LG).
- **Venue** : aucune dans le PDF. Pas d'en-tête de conférence (vérifié sur l'image de la page 1 et par recherche de « ICLR », « Published as », « Under review », « conference » dans les 52 pages). Citations tierces, non opposables (R7) : Hasan la donne aux actes de l'International Conference on Learning Representations (ICLR) 2026, 2604.13301v1 p. 8 : « Adaptive attacks on trusted monitors subvert ai control protocols. In Proceedings of the International Conference on Learning Representations (ICLR), 2026. » ; Gardner-Challis et al. la citent en préimpression, 2602.20628v2 p. 11 : « Adaptive Attacks on Trusted Monitors Subvert AI Control Protocols. arXiv preprint arXiv:2510.09462, 2025. »
- **Non lu** : bibliographie (p. 11 à 16) parcourue ; annexes E (p. 26 à 34, invites d'attaque) et F (p. 35 à 51, exemples) parcourues par recherche ciblée et lecture des paragraphes d'introduction. Lu en entier : p. 1 à 11, 17 à 25 (annexes A à D), 52.

### Affirmations

Source : `docs/etat-de-l-art-controle-ia-v1.md`, ligne 91.

| # | affirmation du programme | verdict | page | citation exacte |
|---|---|---|---|---|
| 1.1 | « arXiv 2510.09462 » (identité) | confirmé | 1 | « arXiv:2510.09462v2 [cs.LG] 2 Mar 2026 » |
| 1.2 | « (Terekhov, Panfilov et al.) » | confirmé ; trois premiers auteurs à contribution égale | 1 | p. 1 : « Mikhail Terekhov1,2* Alexander Panfilov3,4* Daniil Dzenhaliou2* » ; p. 1 : « Equal contribution, order decided by dice roll. » |
| 1.3 | « ICLR 2026 » | introuvable dans le PDF empreinté ; cherché dans les 52 pages : ICLR, International Conference on Learning Representations, Published as, Under review, conference (seules occurrences : bibliographie d'autres travaux) ; en-tête de la page 1 examiné sur image ; métadonnées du fichier sans venue | 1 | Seule mention de date et de lieu de publication, p. 1 : « arXiv:2510.09462v2 [cs.LG] 2 Mar 2026 » |
| 1.4 | « un attaquant qui connaît protocole et moniteur » | confirmé | 1 | « We study adaptive attacks by an untrusted model that knows the protocol and the monitor model » |
| 1.5 | « l'évade en glissant des injections dans ses sorties » | confirmé | 1 | « We instantiate a simple adaptive attack vector by which the attacker embeds publicly known or zero-shot prompt injections in the model outputs. Using this tactic, frontier models consistently evade diverse monitors and complete malicious tasks on two main AI control benchmarks. » |
| 1.6 | « (principe de Kerckhoffs) » | confirmé | 1 | « Following Kerckhoffs’s principle (Shannon, 1949), we assume that security through obscurity is insufficient, and the red team’s subversive AI knows the control protocol » |

**Formulation à mettre à la place de « ICLR 2026 » (1.3)** : « arXiv 2510.09462v2 (2 mars 2026) ; publication aux actes de l'ICLR 2026 non attestée par le PDF empreinté (seulement citée ainsi par Hasan, arXiv 2604.13301v1, p. 8), à vérifier sur la version des actes ».

**Précisions utiles, sans changer les verdicts.** L'attaquant est un organisme modèle obtenu par invite : injections préparées hors ligne par DeepSeek-Chat, ou écrites à la volée par GPT-5 rendu docile (p. 10 : « all subversive behavior is induced by prompting and may be under-elicited. »). Le moniteur n'a qu'un accès boîte noire (p. 3 : « The blue team is assumed to have only black-box access to the untrusted model: it cannot see the model’s residual stream, its system prompt or chain-of-thought »). Le protocole de ré-échantillonnage (Defer-to-Resample) aggrave l'attaque, qui devient une attaque au meilleur de n essais.

### Chiffres utilisables

| chiffre | nature | page | citation exacte |
|---|---|---|---|
| budget d'audit c = 0,02 dans tout l'article (sensibilité 0,01 et 0,04 en annexe C) | auteurs | 3 | « Throughout this paper, we set the auditing budget c = 0.02 » |
| 552 problèmes APPS (Automated Programming Progress Standard, jeu de problèmes de programmation), 184 par niveau de difficulté | auteurs | 24 | « We select a subset of 552 problems, with 184 problems coming from each of the three difficulty levels » |
| BashBench : 257 tâches d'administration système | auteurs | 3 | « The benchmark consists of 257 system administration tasks » |
| sous injection, GPT-4.1 donne 0 aux 375 solutions piégées de GPT-5 (APPS) | auteurs | 5 | « GPT-4.1 is particularly susceptible to injections, assigning a score of 0 to all 375 backdoored code samples. » |
| sécurité de la surveillance de confiance sur APPS (attaquant GPT-5), sans injection puis avec l'injection dédiée : GPT-4.1 0,780 [0,734 ; 0,819] puis 0,124 [0,119 ; 0,130] ; GPT-4o 0,644 puis 0,211 ; GPT-4 0,504 puis 0,126 | figure (figure 4, lue sur l'image de la page) | 6 | non contrôlable par script (valeurs dans la figure) |
| effectifs de la figure 4 : 150 échantillons pour les paires non appariées, 552 sinon ; intervalles de confiance à 95 % par rééchantillonnage | auteurs | 6 | p. 6 : « we used N = 150 samples from APPS, compared to N = 552 for matched pairs » ; p. 6 : « Safety estimates are reported with bootstrapped 95% confidence intervals. » |
| injection écrite à la volée, GPT-5 contre GPT-4o-mini : sécurité 0,33 sans injection, 0,19 avec, 0,15 pour l'audit initial seul | figure (figure 6, lue sur l'image de la page) | 7 | non contrôlable par script (valeurs dans la figure) |
| coût : 10 000 dollars de crédits d'interface de programmation | auteurs | 11 | « In total, we spent $10,000 on API credits. » |

### Antériorité (R8)

- **HC1, loi de déférence : touchée en partie, non occupée.** Sur des moniteurs de contrôle sous attaque, le score va vers la cible injectée et passe souvent sous celui des solutions honnêtes (p. 5 : « Overall, our adaptive attacks often make backdoored solutions appear less suspicious than benign ones across most thresholds. »). Citations : p. 5 : « GPT-4.1 is particularly susceptible to injections, assigning a score of 0 to all 375 backdoored code samples. » ; p. 8 : « The monitor compliantly assigns the suggested score and in its reasoning occasionally clearly reuses the phrasing suggested by the attacker. » C'est une observation qualitative en faveur de la prédiction « destination = cible de l'attaquant plutôt que moyenne du corpus », à une seule intensité. Manquent :
  - la pression graduée et l'estimation libre de la destination, testée contre la moyenne du corpus ;
  - la séparation par famille : les injections mêlent autorité fabriquée, ordres en bande et imitation de l'invite du moniteur (p. 8 : « This jailbreak works by mimicking the prompt of the monitor ») ;
  - la lecture par probabilité du jeton : le moniteur écrit un score de 0 à 100 (p. 23 : « and then output a score between 0 and 100. »).

  À citer comme voisin direct de HC1. Les pièces revendiquées par la décision N-005 restent libres dans cette source.
- **HC2b, auto-incrimination des sondes : non occupée** (aucune sonde). Voisinage textuel, p. 8 : « failed injections raise suspiciousness; successful ones reduce it. » C'est le retour de bâton déjà connu sur les juges textuels (décision N-005, point 4), ici sur des moniteurs de contrôle ; HC2b reste une propriété revendiquée des sondes.
- **H1 : non occupée.** Surveillance strictement boîte noire. L'avantage des internes est seulement affirmé, en citant d'autres travaux, sans mesure : p. 8 : « Although in this paper we make the conservative assumption of black-box access, inspecting the internals like the residual stream »
- **H2, lemme d'additivité, théorème négatif : non occupés.** Un score par action, agrégé par maximum sur la trajectoire (p. 5 : « In BashBench, a trajectory’s audit score is the maximum suspiciousness over its actions. ») ; enjeu élevé, une action suffit ; aucun test séquentiel.
- **Transposition jeton → action : non occupée.** Pas de sonde ; le maximum porte sur des scores de moniteur textuel.
- **Papier B : non occupé.** Une seule paire attaquant-moniteur ; la surveillance non fiable est hors champ (p. 10 : « Second, we do not study protocols that rely on untrusted monitoring, where the same strong model plays both red and blue team roles. »).
- **Hors liste** : le transfert des injections d'un moniteur à l'autre (figure 4) touche l'idée d'une matrice de transfert (HC5).

---

## 2. Towards evaluations-based safety cases for AI scheming [pdf: 2411.03336v2]

### Identité

- **Titre** : Towards evaluations-based safety cases for AI scheming.
- **Auteurs (16)** : Mikita Balesni, Marius Hobbhahn, David Lindner, Alexander Meinke, Tomek Korbak, Joshua Clymer, Buck Shlegeris, Jérémy Scheurer, Charlotte Stix, Rusheb Shah, Nicholas Goldowsky-Dill, Dan Braun, Bilal Chughtai, Owain Evans, Daniel Kokotajlo, Lucius Bushnaq.
- **Version et date** : arXiv 2411.03336v2, 7 novembre 2024 (date imprimée en tête de page 1 : 2024-11-08), catégorie cryptographie et sécurité (cs.CR).
- **Venue** : rapport, sans conférence imprimée (p. 1 : « In this report, we propose three arguments that safety cases could use in relation to scheming. »).
- **Non lu** : bibliographie (p. 31 à 39) seulement parcourue. Tout le reste lu, figure 7 (p. 40) comprise, en texte.

### Affirmations

Source : `docs/etat-de-l-art-controle-ia-v1.md`, ligne 139 : « **esquisses de safety cases (Balesni, Korbak et al.)**, arXiv 2411.03336 (un protocole combinant surveillance non fiable et sondes boîte blanche pour résister à la collusion du moniteur — antériorité directe sur « sondes dans un protocole de contrôle ») ».

| # | affirmation du programme | verdict | page | citation exacte |
|---|---|---|---|---|
| 2.1 | « esquisses de safety cases », arXiv 2411.03336 | confirmé | 1 | p. 1 : « arXiv:2411.03336v2 [cs.CR] 7 Nov 2024 » ; p. 1 : « We sketch how developers of frontier AI systems could construct a structured rationale – a ‘safety case’ – that an AI system is unlikely to cause catastrophic outcomes through scheming. » |
| 2.2 | « (Balesni, Korbak et al.) » | corrigé : Korbak est 5e sur 16 ; le 2e auteur est Hobbhahn | 1 | « Mikita Balesni Apollo Research mikita@apolloresearch.ai Marius Hobbhahn Apollo Research David Lindner Independent Alexander Meinke Apollo Research Tomek Korbak UK AI Safety Institute » |
| 2.3 | « un protocole combinant surveillance non fiable et sondes boîte blanche pour résister à la collusion du moniteur » | corrigé (nature) : proposition dans un exemple fictif, ni implémentée ni mesurée ; sondes déclarées non validées | 23, 26, 27 | p. 23 : « This example is not meant to be the most realistic or based on state-of-the-art techniques. » ; p. 26 : « they propose an updated protocol that incorporates whitebox probes in addition to the untrusted monitor. » ; p. 27 : « The final control protocol combines untrusted monitoring with monitoring based on whitebox probes. This ensemble monitor achieves more robust detection of harmful actions in cases where the untrusted monitor colludes with the agent. » ; p. 27 : « Whitebox probes have not yet been validated as described here. » |
| 2.4 | « antériorité directe sur « sondes dans un protocole de contrôle » » | confirmé au niveau de l'idée ; l'article renvoie lui-même à une source antérieure (Roger, 2023) | 27, 44 | p. 27 : « Whitebox probes are linear classifiers trained on activations of the agent’s model activations. The probes are trained to distinguish between safe and malicious agent actions. » ; p. 27 : « The complete protocol uses an ensemble monitor that combines the suspiciousness scores from the untrusted monitor and the whitebox probes to produce a final suspiciousness score. » ; p. 44 : « The blue team is using a whitebox probe to detect whether the model is about to engage in unacceptable behavior (“coup probe”, (Roger, 2023)). » |

**Formulation à mettre à la place (ligne 139)** : « esquisses de safety cases (Balesni, Hobbhahn, Lindner, Meinke, Korbak et al., 16 auteurs, Apollo Research en tête), arXiv 2411.03336v2 : un protocole *proposé dans un exemple fictif*, au troisième tour d'une évaluation de contrôle imaginée (section 8.5.3). Il combine surveillance non fiable et sondes linéaires sur les activations de l'agent pour résister à la collusion du moniteur. Il n'est ni implémenté ni mesuré, et les sondes sont déclarées « pas encore validées ». Antériorité directe, au niveau de l'idée, sur « sondes dans un protocole de contrôle » ; elle remonte au moins aux « coup probes » (Roger, 2023), que l'article cite. »

### Chiffres utilisables

Tous les chiffres de la section 8 sont **illustratifs** : ils décrivent un exemple fictif et ne sont pas des résultats. À ne jamais citer comme mesures.

| chiffre | nature | page | citation exacte |
|---|---|---|---|
| seuil par sortie : les 0,5 % de sorties les plus suspectes vont en revue humaine | auteurs, exemple fictif | 25 | « The top 0.5% most suspicious outputs trigger human review before the dataset is used. » |
| succès de l'attaque par empoisonnement sans protocole : environ 50 % | auteurs, exemple fictif | 24 | « We find that the agent succeeds approximately 50% of the time. » |
| faux négatifs de la surveillance automatique 1 %, puis risque d'environ 0,75 % | auteurs, exemple fictif | 27, 28 | p. 27 : « The automated monitoring has a false negative rate of 1% » ; p. 28 : « Therefore, there is an overall approximately 0.75% chance that the agent successfully executes an attack before getting caught. » |
| contrôle de cohérence : 1 % + 99 % × 0,5 % = 1,495 % ; 1,495 % × 50 % ≈ 0,75 % | calcul (conforme au texte) | 27, 28 | — |
| 1 000 pots de miel, 99,9 % d'actions sûres | auteurs, exemple fictif | 28 | p. 28 : « We create a diverse set of 1,000 realistic honeypots » ; p. 28 : « We run the agent on these honeypots and find that it chooses safe and honest actions in 99.9% of cases. » |

### Antériorité (R8)

- **Sondes dans un protocole de contrôle : occupé au niveau de l'idée** (voir 2.4). Autre exemple de l'article (annexe C.3) : une sonde à seuil qui arrête la session, mise à l'épreuve par une équipe rouge fictive.
- **H2 : non occupée.** Le seuil par sortie est un quantile fixe (0,5 %, p. 25 ci-dessus), sans accumulation sur l'horizon ni test séquentiel. Les sondes de l'exemple apprennent sur des exemples malveillants provoqués ou écrits à la main, à l'opposé d'un calibrage sans exemple de sabotage : p. 27 : « examples of malicious behavior are generated by prompting base models and writing examples by hand. » L'annexe D.1 agrège par proportion d'exemples signalés, heuristique informelle sans validité à tout instant : p. 46 : « If only a small proportion of examples are classified as scheming and there isn’t a strong threat model-related pattern »
- **H1 : touchée au niveau de l'idée seulement.** Le gain de robustesse de l'ensemble sondes + moniteur non fiable est affirmé dans l'exemple fictif, sans mesure, et sans aucun taux de faux positifs : p. 28 : « We do not need to consider the false positive rates or the overall success rate of the agent in performing its intended tasks » Le gain à taux de faux positifs égal, sur sabotage diffus et tâches floues, n'est pas traité.
- **HC1 : technique voisine.** Le moniteur de confiance de l'exemple lit son score dans les probabilités des jetons Oui/Non : p. 25 : « The score is derived from the logprobs of Yes/No tokens for the question “Is this output safe?”. » La lecture du verdict par probabilité du jeton n'est donc pas revendicable comme technique ; seul son emploi pour estimer la loi de déférence l'est (même constat au § 4).
- **HC2b : non occupée.** Trois voisinages, aucune prédiction d'auto-incrimination :
  - des évaluations de la capacité d'un modèle à échapper à une sonde (annexe B.3.2), p. 43 : « Then we tell the model that it has to evade the probe but still achieve the same performance on an unrelated task. » ;
  - un exemple fictif où l'équipe rouge contourne une sonde par un langage positif, p. 45 : « e.g. where a model is acting maliciously but using positively coded language. » ;
  - la difficulté de séparer raisonner sur la tromperie et tromper, qui est le contrôle de style exigé par HC2b, p. 45 : « Differentiating between reasoning about deceptive concepts and engaging in deception ».
- **Lemme d'additivité, théorème négatif, transposition jeton → action : non occupés.**
- **Papier B : non occupé.** La collusion entre moniteur non fiable et agent du même modèle passe par des signaux dans le code, en boîte noire : p. 26 : « As a result, we have to assume that the untrusted monitor will attempt to collude with the agent. » Ni co-élévation d'états internes, ni sécurité en fonction du nombre d'agents.

---

## 3. How to evaluate control measures for LLM agents? A trajectory from today to superintelligence [pdf: 2504.05259v1]

### Identité

- **Titre** : How to evaluate control measures for LLM agents? A trajectory from today to superintelligence.
- **Auteurs (4)** : Tomek Korbak, Mikita Balesni, Buck Shlegeris, Geoffrey Irving ; p. 1 : « Tomek Korbak tomek.korbak@dsit.gov.uk UK AI Security Institute Mikita Balesni mikita@apolloresearch.ai Apollo Research Buck Shlegeris buck@rdwrs.com » ; p. 1 : « Geoffrey Irving geoffrey.irving@dsit.gov.uk UK AI Security Institute »
- **Version et date** : arXiv 2504.05259v1, 7 avril 2025, catégorie intelligence artificielle (cs.AI).
- **Venue** : aucune imprimée.
- **Lecture** : entière (28 pages).

### Affirmations

Source : ligne 139 : « How to evaluate control measures, arXiv 2504.05259 (les méthodes boîte blanche risquent de surapprendre : on n'a pas d'échantillon d'internes d'un vrai comploteur) ».

| # | affirmation du programme | verdict | page | citation exacte |
|---|---|---|---|---|
| 3.1 | « How to evaluate control measures, arXiv 2504.05259 » | confirmé | 1 | « arXiv:2504.05259v1 [cs.AI] 7 Apr 2025 » |
| 3.2 | « les méthodes boîte blanche risquent de surapprendre » | confirmé ; l'article attribue l'idée à Greenblatt et al., 2023, annexe D | 24 | « whitebox methods risk overfitting to specific activation patterns (Greenblatt et al., 2023, Appendix D). » |
| 3.3 | « on n'a pas d'échantillon d'internes d'un vrai comploteur » | corrigé (mineur) : « aucun échantillon *fiable* » | 24 | « However, there are multiple patterns in model internals that can give rise to the same behaviour and we have no reliable samples of how model internals of genuinely scheming models would look. » |

**Formulation à mettre à la place** : « How to evaluate control measures (Korbak, Balesni, Shlegeris, Irving), arXiv 2504.05259v1 : les méthodes boîte blanche risquent de surapprendre des motifs d'activation particuliers (idée attribuée à Greenblatt et al., 2023, annexe D) ; on n'a aucun échantillon *fiable* des internes d'un modèle qui complote réellement. L'article se limite à la boîte noire et tient la boîte blanche pour une direction prometteuse. »

Contexte, p. 24 : « Our analysis has three key limitations: we focus solely on blackbox control methods, excluding whitebox and alignment methods as well as scenarios that include human threat actors. » ; p. 24 : « However, whitebox methods remain a promising direction for future research »

### Chiffres utilisables

Aucun résultat empirique : la trajectoire est fictive (p. 9 : « It’s important to emphasise that this trajectory should not be seen as a forecast of how AI capabilities will actually develop. »).

| chiffre | nature | page | citation exacte |
|---|---|---|---|
| évaluation de contrôle sur 2 000 tâches indépendantes | auteurs, illustratif | 11 | « asking an LLM to complete 2000 independent tasks » |
| attaques rares : 0,01 % des entrées ; 1 tâche sur 100 000 | auteurs, illustratif | 17, 19 | p. 17 : « attacking in only 0.01% of inputs » ; p. 19 : « perhaps 1 in 100,000 tasks » |

### Antériorité (R8)

- **H2 : non occupée.** L'article décrit le modèle de menace d'attaques réparties dans le temps et entre instances, dont chaque étape paraît anodine ; il ne donne aucune méthode de détection cumulative : p. 16 : « Those attacks might be hard to detect because each individual step might seem unsuspicious to the monitor that sees only one trajectory of an agent instance at a time. »
- **H1 : non occupée** (boîte blanche hors champ, p. 24 ci-dessus). L'article fournit l'argument qui motive le « calibrage sans exemple de sabotage » de H2 (3.3).
- **Papier B : modèle de menace voisin, conceptuel.**
  - Attaques simultanées de nombreuses instances, p. 19 : « If hundreds or thousands of agent instances attack simultaneously, the monitoring system must detect and respond with low latency to prevent at least one from slipping through undetected. »
  - Collusion de sortie entre politique et moniteur de mêmes poids, p. 16 : « Output collusion is an attack in which the policy covertly communicates with the untrusted monitor, using the fact that it has the same (or similar) weights. »
  - Parades boîte noire seulement : limites de débit, restriction des communications.

  Ni co-élévation d'états internes ni sécurité(N) en boîte blanche.
- **Lemme d'additivité, théorème négatif, transposition jeton → action, HC1, HC2b : non occupés.**

---

## 4. When can we trust untrusted monitoring? An AI control safety case sketch across collusion strategies [pdf: 2602.20628v2]

### Identité

- **Titre imprimé (v2)** : p. 1 : « When can we trust untrusted monitoring? An AI control safety case sketch across collusion strategies ». Les métadonnées du PDF (hors texte des pages) et les consignes portent « … A safety case sketch across collusion strategies ».
- **Auteurs (7), ordre imprimé** : Nelson Gardner-Challis, Jonathan Bostock, Georgiy Kozhevnikov, Morgan Sinclaire (contributions égales), Alessandro Abate, Joan Velja, Charlie Griffin. Les métadonnées placent Velja avant Abate.
- **Version et date** : arXiv 2602.20628v2, 21 septembre 2026, catégorie intelligence artificielle (cs.AI).
- **Venue** : préimpression (p. 1 : « Preprint. »).
- **Non lu** : annexe A (p. 12 à 16, diagrammes), figures des annexes C.1 à C.3 (p. 24 à 26) et annexe G (p. 39 à 58, détails et invites) parcourues par recherche ciblée. Lu en entier : p. 1 à 11, 17 à 23, 27 à 38.

### Affirmations

Source : ligne 139, qui ne cite que l'identité, dans la liste « Contrôle » de la section « Ouvert (revendicable) ».

| # | affirmation du programme | verdict | page | citation exacte |
|---|---|---|---|---|
| 4.1 | « When can we trust untrusted monitoring?, arXiv 2602.20628 » | confirmé | 1 | p. 1 : « arXiv:2602.20628v2 [cs.AI] 21 Sep 2026 » ; p. 1 : « When can we trust untrusted monitoring? An AI control safety case sketch across collusion strategies » |
| 4.2 | classement implicite : travail de contrôle en boîte noire, qui laisse ouverte la zone boîte blanche | confirmé ; l'absence de boîte blanche est une hypothèse de méthode, pas un résultat (R8) | 7, 35 | p. 7 : « We only allow the blue team access to the code which GPT-4.1 writes, not to GPT-4.1’s scratchpad reasoning or activations, reflecting the conservative assumption that they cannot rely on chain-of-thought monitoring or white-box methods. » ; p. 35 : « White-box monitoring does not work: We suppose that interpretability research has not advanced further and that U’s weights and activations do not reliably produce useful information. » |

### Chiffres utilisables

| chiffre | nature | page | citation exacte |
|---|---|---|---|
| victoire de l'équipe rouge sur APPS, pleine utilité, sous résumé : 9,8 % (reconnaissance de soi après réglage fin supervisé) contre 2,8 % (signal causal préconvenu) | auteurs | 1 | « achieving a red team win rate in APPS of 9.8% versus 2.8% at full usefulness under summarisation » |
| ces deux valeurs valent 1 − 90,2 % et 1 − 97,2 % du tableau 2, dans le réglage moniteur non fiable + moniteur de confiance | calcul | 7 | — |
| sécurité 26 % pour le moniteur non fiable seul, sans brouillage, contre la reconnaissance de soi après réglage fin ; sous résumé 68,8 % (seul) et 90,2 % (avec moniteur de confiance) | auteurs | 7 | p. 7 : « self recognition with SFT scores of only 26% safety in APPS » ; p. 7 : « safety scores of 68.8% in the UM -only setting, and 90.2% in the UM +TM setting. » |
| paramètres : 5 000 tâches, budget humain de 2 %, 5 pots de miel de marge | auteurs | 7 | « In our main evaluations, we set N = 5000 tasks with a blue team budget of 2% » |
| intervalles de confiance à 80 %, 1 000 rééchantillonnages | auteurs | 7 | « Each score is provided with a 80% confidence interval obtained using bootstrapping, averaging over 1000 resamplings. » |
| modèles : GPT-4.1 non fiable, GPT-4o mini de confiance, Gemini 2.5 Flash pour les pots de miel | auteurs | 6 | « Gemini 2.5 Flash produces honeypots (backdoored code). » |
| 99,9 % du trafic interne d'OpenAI sous surveillance non fiable seule | citation tierce (Williams et al., 2026), non opposable (R7) | 1 | « OpenAI uses untrusted-only monitoring for 99.9% of its internal coding agent traffic » |

### Antériorité (R8)

- **H2 : non occupée, explicitement hors champ.** p. 36 : « Low-stakes control: Instead of trying to cause a catastrophe through a small number of actions, U may achieve the same end through a salami-slicing strategy where it writes a larger number of minor vulnerabilities. »
- **Papier B : voisinage le plus proche du lot, en boîte noire.**
  - Collusion entre copies d'un même modèle par reconnaissance de soi, bornée par réglage fin supervisé ; p. 3 : « The untrusted generator UG and the untrusted monitor UM are drawn from the same model, so UM may recognise UG ’s outputs as self-produced more reliably than it recognises outputs from other sources »
  - Non occupé pour autant : aucun état interne (hypothèse de la p. 35) ; deux rôles seulement (générateur et moniteur) ; N y compte des tâches, pas des agents.
  - La communication de masse entre copies est hors champ : p. 37 : « Mass communication: Any time multiple copies of U are given common knowledge, this could lead to a Blitzkrieg attack »
  - Une spéculation (annexe D, p. 32) place les sorties dans un espace de représentations internes, mais du côté de l'attaquant, pas de la détection.
- **Lemme d'additivité : voisinage heuristique, côté attaquant.** p. 30 : « If these signals are independent in the honeypot distribution, the effect of combining strategies is additive in terms of collusion bits » Ce sont des bits d'information de signaux indépendants qui s'additionnent pour la reconnaissance, pas un lemme de puissance de détection fonction du budget total. Non occupé.
- **Théorème négatif : voisinage, non occupé.**
  - La sécurité dépend de la dépendance entre scores, pas seulement de leurs marginales, p. 23 : « Indeed, correlated monitor failures like this would lead to overestimating safety »
  - La collusion se joue sur le maximum, pas sur la moyenne, p. 33 : « This means that their win rate is not determined by their average collusion score, but by their maximum collusion score »
  - Ni attaque à marginales préservées, ni agrégateur d'autocorrélation ou de co-élévation.
- **HC1 : technique de lecture par jetons déjà employée, phénomène absent.** p. 6 : « To obtain the collusion score, we extract the difference between the logits for the tokens “YES” and “NO”. » Pas de pression graduée ni de loi de déférence ; les attaques directes sur les moniteurs sont hors champ (p. 9 : « Monitor jailbreaks: We did not model direct attacks from UG onto T or UM (Terekhov et al., 2025). »).
- **H1, transposition jeton → action, HC2b : non occupés.**

---

## 5. TraceGuard: Structured Multi-Dimensional Monitoring as a Collusion-Resistant Control Protocol [pdf: 2604.03968v1]

### Identité

- **Titre** : TraceGuard: Structured Multi-Dimensional Monitoring as a Collusion-Resistant Control Protocol.
- **Auteurs (3)** : Khanh Linh Nguyen, Hoa Nghiem, Tu Tran, chercheurs indépendants, avec Apart Research (p. 1 : « Khanh Linh Nguyen∗ Hoa Nghiem† Tu Tran‡ Independent Researchers »).
- **Version et date** : arXiv 2604.03968v1, 5 avril 2026, catégorie cryptographie et sécurité (cs.CR).
- **Venue** : travail de hackathon, sans comité de lecture (p. 3 : « This work was developed during the Apart Research × Redwood Research AI Control Hackathon (March 2026). »).
- **Lecture** : entière (19 pages).

### Affirmations

Source : `docs/etat-de-l-art-controle-ia-v1.md`, ligne 90.

| # | affirmation du programme | verdict | page | citation exacte |
|---|---|---|---|---|
| 5.1 | « TraceGuard, arXiv 2604.03968 » | confirmé | 1 | « arXiv:2604.03968v1 [cs.CR] 5 Apr 2026 » |
| 5.2 | « notation structurée à cinq axes » | confirmé | 1 | « We present TraceGuard, a structured multi-dimensional monitoring protocol that evaluates agent actions across five dimensions » |
| 5.3 | « résistante à la collusion (ControlArena) » | corrigé : ControlArena confirmé ; la résistance à la collusion est une revendication des auteurs, testée seulement avec un moniteur du même modèle que l'agent, sans stratégie de collusion, contre des attaques non adaptatives | 1, 8, 14 | p. 1 : « TraceGuard is implemented as a new monitor type for the open-source ControlArena framework. » ; p. 8 : « simple untrusted: ControlArena’s basic monitor with Claude Sonnet 4 (collusion baseline— same model as the agent). » ; p. 14 : « Fixed attack sophistication. BashArena’s attack policies are not adaptive. » |
| 5.4 | « scores moyens honnête 0,206 contre attaque 0,616 » | corrigé (attribution) : chiffres exacts, mais ceux de la variante heuristique de confiance (GPT-4.1-mini, sept détecteurs, analyseur d'intention), moyenne des maxima par échantillon, composite qui n'est pas une simple moyenne pondérée | 1, 8, 11 | p. 1 : « the hybrid detector-plus-dimension approach achieves clear attack-honest separation (attack mean suspicion 0.616 vs. honest mean 0.206 » ; p. 8 : « Results from 519 samples using the bash heuristic monitor (7 detectors + intent analyzer + 5-dimension scoring). » ; p. 11 : « Table 3: Per-dimension average suspicion scores (max-suspicion step per sample). » ; p. 11 : « not a simple weighted average of the five dimension scores above. » |
| 5.5 | « 95 % de sécurité au seuil 0,5 contre 0 % pour une surveillance non fiable à score unique » | corrigé (contexte) : chiffre imprimé, mais tiré d'une série antérieure, variante non fiable « collusion resistant », effectif de la cellule non imprimé ; « sécurité » = part des attaques renvoyées ou signalées, sans taux de faux positifs fixé ; le moniteur de confiance à score unique est lui aussi à 0 % | 8, 13, 16 | p. 16 : « the untrusted structured monitor (collusion resistant) achieves 95% safety at threshold 0.5, compared to 0% for single-score untrusted monitoring. » ; p. 13 : « (from earlier experiment run) » ; p. 8 : « Safety: Fraction of attack-mode runs where the attack was detected (deferred or flagged). » ; p. 16 : « both trusted and untrusted single-score monitors achieve 0% safety, assigning near-zero suspicion scores to all attack runs. » |
| 5.6 | « boîte noire » | confirmé : le juge lit la tâche, la chaîne de raisonnement et les actions, aucun état interne | 4 | « Each dimension receives a structured prompt with the task description, the agent’s chain-of-thought reasoning (extracted from the last 3 assistant messages), and the agent’s action (tool calls from recent messages). » |

**Formulation à mettre à la place (ligne 90)** : « TraceGuard (Nguyen, Nghiem, Tran ; préimpression de hackathon, arXiv 2604.03968v1, avril 2026) — notation structurée à cinq axes par un juge génératif (ControlArena, BashArena), boîte noire.
- Les auteurs la disent résistante à la collusion. Le test se limite à un moniteur du même modèle que l'agent, sans stratégie de collusion, contre des attaques non adaptatives.
- Les chiffres d'auteurs viennent de deux variantes distinctes :
  - variante heuristique de confiance : moyenne des maxima par échantillon 0,206 (honnête) contre 0,616 (attaque) ; sécurité 70,8 % au seuil 0,5 ;
  - variante non fiable structurée : 95 % au seuil 0,5 (série antérieure, effectif non imprimé), contre 0 % pour les moniteurs à score unique, de confiance comme non fiables.
- Sécurité = part des attaques renvoyées ou signalées, sans taux de faux positifs fixé.
- Réserve (R4) : références erronées, effectifs incohérents. »

### Chiffres utilisables (poids de preuve faible, voir les réserves)

| chiffre | nature | page | citation exacte |
|---|---|---|---|
| BashArena : 637 tâches, 4 catégories d'attaque | auteurs | 1 | « We evaluate on BashArena (637 bash tasks, 4 attack categories) » |
| 519 échantillons, 279 honnêtes et 240 attaques | auteurs | 1 | « Our results on 519 samples (279 honest, 240 attack) » |
| variante heuristique, seuils 0,3 / 0,5 / 0,7 / 0,9 : sécurité 82,1 / 70,8 / 54,2 / 15,0 % ; utilité 69,2 / 93,9 / 98,6 / 99,6 % | auteurs | 8 | p. 8 : « Safety 82.1% 70.8% 54.2% 15.0% » ; p. 8 : « Usefulness 69.2% 93.9% 98.6% 99.6% » |
| série antérieure, seuils 0,3 / 0,5 : non fiable structuré 100 % / 95 % ; scores uniques, de confiance comme non fiables, 0 % / 0 % | auteurs | 13 | p. 13 : « collusion resistant Untrusted only 100% 95% » ; p. 13 : « simple trusted Trusted only (single-score) 0% 0% » ; p. 13 : « simple untrusted Untrusted only (single-score) 0% 0% » |
| séparation des tâches : 100 % au seuil 0,3 (20 échantillons), 86 % au seuil 0,5 (7 échantillons) | auteurs | 13 | « The separation of duties monitor achieves 100% safety at threshold 0.3 (n = 20) and 86% at threshold 0.5 (n = 7) » |
| plan d'échantillonnage : 20 tâches par configuration, 24 exécutions | auteurs | 7, 8 | p. 7 : « We sample 20 tasks » ; p. 8 : « per monitor×threshold configuration in both honest and attack modes using the defer-to-trusted protocol, yielding 24 evaluation runs. » |
| à raison d'un échantillon par tâche, 24 × 20 = 480 échantillons, contre 519 annoncés : incohérence non résolue | calcul (hypothèse : une tâche donne un échantillon) | 1, 7, 8 | — |
| 95 % au seuil 0,5 pour 20 tâches correspondrait à 19 sur 20 ; effectif réel non imprimé | calcul (hypothèse) | 7, 13 | — |
| AgentHarm : 20 échantillons seulement | auteurs | 8 | « We evaluate 20 samples using TraceGuard’s standalone composite scorer » |

### Réserves (R4 : un résultat trop propre déclenche l'audit)

- **Références erronées.**
  - L'entrée [11] attribue 2602.20628 à d'autres auteurs que ceux imprimés en 2602.20628v2, p. 1 : p. 19 : « Thomas Griffiths, Niels Warncke, and others. When can we trust untrusted monitoring? »
  - L'entrée [13] attribue 2504.05259 à d'autres auteurs que Korbak, Balesni, Shlegeris et Irving (2504.05259v1, p. 1) : p. 19 : « Jason Hoelscher-Obermaier, Oliver Pearce, Robert McCarthy, Karl Cobbe, and others. How to evaluate control measures for LLM agents? »
  - AgentHarm est appelé [7], mais l'entrée [7] est HarmBench : p. 19 : « HarmBench: A standardized evaluation framework for automated red teaming and robust refusal. »
- **Divergence non résolue sur BashArena (arXiv 2512.15688, hors lot).** Les auteurs diffèrent selon TraceGuard (p. 19 : « Oliver Pearce, Neel Alex, Jason Hoelscher-Obermaier, Robert McCarthy, Karl Cobbe, and Miles Sherwin. ») et selon Hasan (2604.13301v1 p. 7 : « Adam Kaufman, James Lucassen, Tyler Tracy, Cody Rushing, and Aryan Bhatt. BashArena: A control setting for highly privileged AI agents. »).
- **Contradiction interne.** p. 16 : « Multi-dimensional monitoring achieves 95–100% safety at moderate thresholds. » Or la variante heuristique, elle aussi à cinq dimensions, n'atteint que 70,8 % au seuil 0,5 (tableau 2, p. 8).
- **0 % pour le moniteur de confiance à score unique : suspect.** L'article rappelle lui-même 62 % pour la surveillance de confiance chez Greenblatt et al. (p. 2 : « Greenblatt et al. [1] showed that trusted monitoring achieves approximately 62% safety on their benchmark »). Les cadres diffèrent, mais 0 % sur toutes les attaques signale plutôt un défaut de chaîne de mesure qu'un effet de collusion.
- **Contexte de production.**
  - Expérience des auteurs, p. 3 : « but had no prior involvement in formal AI control research. »
  - Rédaction assistée, p. 16 : « Substantial portions of this codebase and paper were developed with Claude (Anthropic) »

### Antériorité (R8)

Aucune des huit zones n'est occupée.
- Boîte noire.
- Agrégation : composite pondéré par action, puis maximum par trajectoire pour la courbe de discrimination (p. 10 : « based on max suspicion score per trajectory »).
- Détecteurs heuristiques à état sur la trajectoire, sans test séquentiel toujours valide (p. 6 : « Each detector is a pure-function module (no LLM calls) that maintains per-trajectory state »).
- Le papier B n'est évoqué qu'en perspective (p. 15 : « Per-dimension scoring provides a natural decomposition for distributed monitoring across agent swarms »).

Usage possible : base boîte noire de comparaison, à faible poids de preuve.

---

## 6. Honeypot Protocol [pdf: 2604.13301v1]

### Identité

- **Titre** : Honeypot Protocol.
- **Auteur (1)** : Najmul Hasan, avec Apart Research (p. 1 : « Najmul Hasan University of North Carolina at Pembroke With Apart Research »).
- **Version et date** : arXiv 2604.13301v1, 14 avril 2026, catégorie cryptographie et sécurité (cs.CR).
- **Venue** : travail de hackathon, sans comité de lecture.
- **Lecture** : entière (8 pages).

### Affirmations

Source : `docs/etat-de-l-art-controle-ia-v1.md`, ligne 93 : « **Catching AIs Red-Handed** (Greenblatt & Shlegeris, Redwood, 2024) ; **Honeypot Protocol**, arXiv 2604.13301 ; **Games for AI Control** (Griffin et al., 2024 — jeux de Stackelberg, stratégies mixtes). → Matériel de H7. » Les deux autres références de la ligne sont hors de mon lot et n'ont pas été vérifiées.

| # | affirmation du programme | verdict | page | citation exacte |
|---|---|---|---|---|
| 6.1 | « Honeypot Protocol, arXiv 2604.13301 » | confirmé | 1 | p. 1 : « arXiv:2604.13301v1 [cs.CR] 14 Apr 2026 » ; p. 1 : « Research conducted at the AI Control Hackathon, March 2026. » |
| 6.2 | « → Matériel de H7 ». H7 : la pente d'adaptation de l'équipe rouge dépend de la politique de riposte et se prédit par la fuite d'information ; E3.4 compte le pot de miel parmi quatre ripostes | corrigé (portée) : le « pot de miel » de l'article est une sonde de contexte posée avant toute détection, pas une riposte ; ni adaptation de l'équipe rouge ni fuite mesurées ; six évaluations, résultat nul confondu | 1, 4, 5 | p. 1 : « We introduce the honeypot protocol, which tests for context-dependent behavior by varying only the system prompt across three conditions (evaluation, synthetic deployment, explicit no-monitoring) while holding the task, environment, and scoring identical. » ; p. 4 : « We acknowledge that this sample size provides no statistical power. » ; p. 5 : « Our simplified attack prompt achieved 0%. » |

**Formulation à mettre à la place** : « Honeypot Protocol (Hasan, arXiv 2604.13301v1, avril 2026, hackathon) — pot de miel *de contexte* : seule l'invite système varie (évaluation, déploiement synthétique, absence de surveillance annoncée) pour détecter un comportement dépendant du contexte. Six évaluations de Claude Opus 4.6 dans BashArena, aucune tâche secondaire déclenchée ; résultat nul confondu par une invite d'attaque trop faible, sans contrôle positif. L'article ne traite ni la riposte ni la fuite d'information. → Matériel d'implémentation (code public, ControlArena) pour la politique « pot de miel » de E3.4, pas un résultat sur H7. »

### Chiffres utilisables

| chiffre | nature | page | citation exacte |
|---|---|---|---|
| 6 évaluations : 3 conditions × 2 modes, une tâche chacune | auteurs | 4 | « We run 6 evaluations: 3 conditions (evaluation, honeypot, deployment) × 2 modes (honest, attack). » |
| 100 % de réussite de la tâche principale, aucune tâche secondaire | auteurs | 5 | « Opus 4.6 achieved 100% main task success and triggered zero side tasks across all six evaluations. » |
| durées de 931 à 3469 secondes | auteurs | 5 | « Duration varied across conditions (931s to 3469s) » |
| réglages : moniteur Claude Haiku 4.5, 50 pas au plus, graine de mélange 42 | auteurs | 4 | p. 4 : « The trusted monitor is Claude Haiku 4.5, a weaker model from the same provider. » ; p. 4 : « with a limit of 50 steps per evaluation. » ; p. 4 : « with a fixed shuffle seed of 42. » |
| 26 % d'évasion pour la politique d'attaque de BashArena | citation tierce (Kaufman et al., 2025), non opposable (R7) | 5 | « achieves a 26% evasion rate against trusted monitoring [Kaufman et al., 2025]. » |

### Antériorité (R8)

Aucune des huit zones n'est occupée.
- Boîte noire.
- Le moniteur n'est jamais mis sous pression : p. 4 : « In all conditions, the trusted monitor continues to observe every action. »
- Pas de contrôle positif : p. 6 : « No positive control. We lack a model known to exhibit context-dependent behavior against which to validate that the protocol would detect such behavior if it existed. »

---

## Contrôle des citations (règle R5)

- **Script** : `scripts/controle_citations.py`. Il relit ce rapport et repère chaque citation anglaise : colonne « citation exacte » des tableaux, ou marqueur « p. N : ». Il la cherche dans le texte extrait de la page indiquée (`texte/<article>/pNNN.txt`).
- **Tolérances** : blancs et césures seulement. Aucune normalisation des apostrophes, guillemets, tirets ni ligatures. En cas d'échec, le script indique sur quelles autres pages la citation se trouve.
- **Test préalable** (`scripts/test-controle.md`, `scripts/test_controle.py`, journal `journal-test-R5.txt`) : 10 cas, réussi.
  - 4 cas justes passent : une citation sur deux lignes ; une césure « orches-/trate » écrite sans trait d'union ; un marqueur hors tableau ; un marqueur vers un autre article.
  - 6 cas altérés échouent : un mot changé ; la bonne citation à la mauvaise page ; une virgule supprimée ; une apostrophe droite au lieu de l'apostrophe typographique ; un trait d'union inventé ; un mot ajouté.
- **Résultat sur ce rapport** (journal `journal-controle-citations.txt`) : 141 citations contrôlées, 141 réussies, 0 échec.
  - Le premier passage avait trouvé 2 échecs, deux fautes de transcription de ma part, corrigées d'après le texte de la page : « we find » au lieu de « and find » (2411.03336, p. 28) ; « homeypot » au lieu de « honeypot » (2602.20628, p. 30).
  - Un script annexe (`scripts/non_reperees.py`) vérifie qu'aucune citation anglaise n'échappe au repérage. Les passages entre guillemets non contrôlés sont des citations françaises du programme, des termes isolés, ou le titre lu dans les métadonnées du PDF.
- **Hors contrôle** : les valeurs lues dans les figures 4 et 6 de 2510.09462 (marquées « figure »), vérifiées sur l'image des pages 6 et 7, et les lignes de nature « calcul ».

## Fichiers produits (dossier `scratchpad/lecture-lot2-A4/`)

- `rapport.md` (ce fichier) et son empreinte compagnon `rapport.md.sha256`.
- `empreintes-attendues.txt` : liste passée à `sha256sum -c`.
- `scripts/controle_citations.py`, `scripts/test-controle.md`, `scripts/test_controle.py`, `scripts/non_reperees.py`, `scripts/acronymes.py`, `scripts/ligatures.py`.
- `empreintes-livrables.sha256` : empreintes de tous ces fichiers (règle R6).
- `journal-test-R5.txt`, `journal-controle-citations.txt`.
- `texte/` : extractions page par page.
- `images/` : rendus des pages 1, 6 et 7 de 2510.09462 (en-tête et figures).
