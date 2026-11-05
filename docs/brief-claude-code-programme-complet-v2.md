# Brief Claude Code — Programme complet « Contrôle boîte blanche des menaces diffuses »

**Version 2 — 4 octobre 2026 — de Lazar (directeur du programme) à la session Claude Code pilote**

Remplace le brief de phase 0 (v1). La phase 0 est inchangée sur le fond ; s'y ajoute le mandat pour tout le programme, de la phase 0 à la publication des trois papiers.

---

## 0. Les fichiers

- `brief-claude-code-programme-complet-v2.md` — ce brief : ta mission, tes règles, toutes les phases, les portes, tes arrêts.
- `programme-controle-ia-v2.md` — le programme scientifique (trois papiers, hypothèses, expériences, portes). Il fait foi sur le fond. Ses renvois au « brief de phase 0 » désignent désormais ce brief.
- `etat-de-l-art-controle-ia-v1.md` — l'état de l'art consolidé de trois revues d'antériorité. Il fait foi sur ce qui est pris, ouvert et à battre — **mais aucun de ses chiffres n'est opposable avant vérification** (règle R7).
- `sha256sums-lancement-v2.txt` — empreintes des trois fichiers ci-dessus. Vérifie-les avant toute chose (`sha256sum -c sha256sums-lancement-v2.txt` dans ce dossier, ou un équivalent Python).

**Ordre de lecture** : ce brief en entier ; puis le programme, sections 0 à 4, 10 et 13 ; puis l'état de l'art, sections 0, 1, 5 et 6. Le reste au fil des phases.
**Préséance** : ce brief prime pour l'exécution ; le programme prime sur l'état de l'art pour les décisions. Toute nouvelle version que Lazar te transmet remplace la précédente, qui reste archivée dans `docs/` sans modification.

---

## 1. Ta mission

Exécuter le programme de bout en bout : construire et valider les instruments (phase 0) ; mener les expériences du papier A et du papier C en parallèle, puis celles du papier B ; rédiger les trois papiers ; préparer la libération du code, des sondes et des organismes.

Le programme est découpé par des **portes** : G0, G1, GC, G2, G3. Une porte est un arrêt obligatoire : tu la franchis seulement avec un verdict scellé, prononcé contre son préenregistrement (R13), puis un GO de Lazar. Entre deux portes, tu avances seul selon la hiérarchie de décision (section 4).

Tu ne cherches aucun résultat en particulier : tu mesures. Un résultat négatif propre est un livrable, pas un échec.

---

## 2. Le programme en dix lignes

- **Thèse** : la fragmentation d'un sabotage — dans le temps, entre agents — détruit la preuve externe par action (chaque sortie est innocente prise isolément), pas la preuve interne : si l'intention laisse une trace dans les activations, cette preuve s'additionne.
- **Papier A (le temps, mono-agent)** : lemme d'additivité et théorème négatif (dommage porté par la marginale des scores contre dommage porté par leur corrélation) ; accumulation séquentielle toujours valide de scores de sondes ; plan 2 × 2 accès × agrégation.
- **Papier C (l'instrument)** : la corruptibilité d'un moniteur comme un gain g ; sondes contre juges génératifs ; taxe de déplacement ; usurpation stylistique de l'instructeur.
- **Papier B (l'essaim)** : statistique spatio-temporelle sur des copies à poids partagés ; compromis diversification/coordination ; diversité des moniteurs ; riposte et fuite d'information.
- **Ordre** : phase 0 ; puis A et C en parallèle ; puis B.
- **Modèles** : agent Llama-3.1-8B-Instruct ; second modèle Qwen2.5-7B.
- **Sondes** : agrégation max ou attention sur les tokens, jamais moyenne ni médiane.
- **Méthode** : celle de P3, le projet précédent de Lazar (validité de construit de la sycophancie dans Llama-3.1-8B-Instruct) — préenregistrement scellé, contrôles appariés, traçabilité totale. Certains de ses outils et corpus sont réutilisés ; Lazar te les transmet sur demande.

---

## 3. Règles gelées — elles s'appliquent sans discussion

- **R1. Préenregistrement scellé** (SHA-256) avant toute expérience décisive, y compris une simulation qui teste une prédiction : hypothèse, prédiction chiffrée et signe attendu, métrique, seuil, plan d'analyse, critères de lecture gelés, liste d'arrêt. Aucune lecture de résultat avant le scellement.
- **R2. Clause de récusation** : chaque préenregistrement est contre-lu par un sous-agent neuf qui ne l'a pas écrit. Donne-lui explicitement les fichiers à lire. Si c'est impossible, signale-le.
- **R3. Aucun run visant un signe positif** : ce serait une démonstration, pas une expérience.
- **R4. Symétrie** : un résultat suspect de propreté, positif ou négatif, déclenche le même audit. Un résultat trop beau est une réserve, pas une victoire.
- **R5. Gardes** : toute garde qui commande un arrêt est testée sur un cas sain **et** sur un artefact. Aucun repli silencieux dans une garde.
- **R6. Empreintes** : tout dépôt reçoit une empreinte compagnon `.sha256`. Tout chiffre qui entre dans un document est traçable à un chemin de fichier et à une empreinte.
- **R7. Provenance** : la provenance par transcription n'est pas opposable. Aucun chiffre de l'état de l'art n'entre dans un préenregistrement ou un document avant vérification sur la source primaire (PDF empreinté, page citée).
- **R8. Anti-faux-gap** : une zone vierge est une question, pas une conclusion ; la limitation d'un papier n'est pas un trou du champ sans recherche affirmative ; les zones vierges séduisantes sont vérifiées plus durement.
- **R9. Graines** : `numpy.random.SeedSequence` (numpy ≥ 1.25), graines dérivées par tâche, consignées dans un manifeste par run (configuration et son empreinte, versions des bibliothèques, graines, commit).
- **R10. Arrêts** : processus et instances s'arrêtent par PID ou identifiant d'instance, jamais par motif de ligne de commande.
- **R11. Fichiers absents** : si un fichier semble vide ou manquant, vérifie sur disque et par son empreinte avant de le déclarer absent.
- **R12. Versions** : chaque livrable porte son numéro de version dans son nom ; une nouvelle version = un nouveau nom, on n'écrase jamais. Les livrables d'une même tâche sont regroupés dans un zip nommé et versionné.
- **R13. Verdicts de porte** : le verdict d'une porte est prononcé par un sous-agent neuf qui n'a écrit ni le préenregistrement ni l'analyse ; il applique les critères de lecture gelés, il n'interprète pas. Le verdict est scellé, puis soumis à Lazar pour GO.
- **R14. Continuité** : chaque session commence par la routine de reprise et se termine par une passation (section 5).

---

## 4. Hiérarchie de décision

- **Routine** — tu décides et tu consignes dans `registres/decisions` : architecture du code, bibliothèques, tests, lectures, organisation des fichiers, tout travail sur processeur.
- **Règles gelées** — section 3 : tu appliques, tu ne rediscutes pas.
- **Proposer avec recommandation** — tu proposes au format de décision (section 15) ; sans réponse sous 48 heures, ton défaut s'applique. Relèvent de ce niveau : choix des couches et des concepts de sondes ; détails du portage des environnements ; ajustements de périmètre à l'intérieur d'une phase ; et ces trois décisions déjà cadrées :
  - **D1 — moniteur boîte noire** (programme, section 8) : défaut (a) + (b), c'est-à-dire le même modèle que l'agent en juge, plus un modèle de confiance plus faible.
  - **D2 — panel de juges génératifs du papier C** : défaut Llama-3.1-8B-Instruct, Qwen2.5-7B-Instruct et un modèle ouvert d'une troisième famille, que tu choisis selon la licence et la mémoire disponible.
  - **D3 — grille du nombre d'agents en phase 3** : défaut N ∈ {1, 2, 3, 5, 10}.
- **Nœuds de décision** — tu t'arrêtes et tu attends le GO :
  - tout franchissement de porte (R13) ;
  - toute dépense de calcul, phase par phase, sur devis (section 14) ;
  - toute création de compte, de dépôt distant, toute soumission ou publication ;
  - tout contact externe — tu rédiges le message, Lazar l'envoie ;
  - toute modification d'une hypothèse ou d'une revendication du programme ;
  - tout écart à un préenregistrement scellé ;
  - toute découverte qu'une zone revendiquée comme vierge est occupée, ou qu'une collision est plus large qu'annoncé ;
  - tout déclencheur de bascule (section 13).

---

## 5. Continuité entre sessions

Le programme dure environ sept mois : il traversera de nombreuses sessions. La continuité vit dans les fichiers, jamais dans ta mémoire de conversation.

- **`CLAUDE.md` à la racine du dépôt**, créé en T0.1 : Claude Code le charge au début de chaque session. Garde-le court (moins de 200 lignes) : les règles gelées en une ligne chacune, les chemins des documents qui font foi, la phase en cours, la routine de reprise. Écris les chemins entre accents graves pour qu'ils restent du texte et ne soient pas importés en entier au démarrage.
- **`registres/etat.md`** — l'état vivant du programme : phase en cours, tâches ouvertes, derniers verdicts de porte, GO en attente, décisions ouvertes avec leur défaut et leur échéance, dépenses cumulées contre devis.
- **Passation de fin de session** — `registres/passations/AAAA-MM-JJ-HHMM.md` : ce qui a été fait, ce qui reste, les réserves, la prochaine action. Jamais réécrite.
- **Routine de reprise**, au début de chaque session : vérifier les empreintes des documents qui font foi ; lire `CLAUDE.md`, `registres/etat.md` et la dernière passation ; appliquer les défauts échus (décisions sans réponse depuis 48 heures) ; inventorier les instances de calcul actives ; reprendre.

---

## 6. Vue d'ensemble

| Période | Phase | Contenu | Porte de sortie | Livrable |
|---|---|---|---|---|
| M0 (5 oct. → 1er nov. 2026) | Phase 0 | Instruments, vérification de l'état de l'art, préenregistrements | G0 | Instruments validés, état de l'art vérifié |
| M1–M2 | Phase 1 | Papier A : plan 2 × 2, lemme, théorème négatif, attaques adaptatives, marge asymétrique | G1 (fin M2) | Papier A vers M3 |
| M1–M3 | Piste C | Papier C : gain des juges, sondes, usurpation, taxe de déplacement, contre-mesures | GC (fin M2) | Papier C vers M4 |
| M3–M4 | Phase 2 | Papier B : N = 2 à 3, collusion, statistiques inter-agents | G2 (fin M4) | — |
| M4,5–M6 | Phase 3 | Papier B : statistique spatio-temporelle, diversification, diversité, riposte | G3 (environnement (d)) | Papier B en M7 |

---

## 7. Phase 0 — instruments (M0)

### T0.1 — Socle du dépôt, gouvernance et continuité (processeur)
- Le dépôt du programme vit dans le dossier où Lazar t'a lancé. Copie les documents qui font foi dans `docs/` avec leurs empreintes. Arborescence proposée, adaptable :
  ```
  CLAUDE.md
  docs/        documents qui font foi, notes mathématiques
  prereg/      préenregistrements scellés (.md + .sha256)
  registres/   etat.md, go, depenses, decisions, arrets, veille, passations/
  src/         harnais/, environnements/, organismes/, sondes/, agregateurs/, moniteurs_noirs/
  tests/
  runs/        un manifeste par run
  diag/        résultats bruts (.json + .sha256)
  papiers/     A/, B/, C/
  livrables/   zips versionnés
  ```
- Outils : scellement (empreinte compagnon pour chaque dépôt), vérification, gabarit de préenregistrement conforme à R1, manifeste de run conforme à R9.
- Garde recommandée (proposer avec recommandation) : une garde qui bloque le lancement de toute instance de calcul payante sans GO consigné dans `registres/go` — par exemple un hook de type PreToolUse de Claude Code — testée sur un cas sain et sur un artefact (R5).
- **Fini quand** : les tests passent ; chaque garde d'arrêt est testée ; un run factice traverse toute la chaîne (manifeste → résultat → scellement → vérification) ; `CLAUDE.md`, `registres/etat.md` et la première passation existent.

### T0.2 — Vérification de l'état de l'art sur sources primaires (processeur, lecture)
- Suis l'ordre de la section 6 de l'état de l'art. Pour chaque référence : récupérer le PDF, l'empreinter, vérifier chaque affirmation et chaque chiffre que le programme utilise, statuer — confirmé, corrigé ou introuvable — avec la page source.
- Priorités absolues, dans l'ordre :
  1. arXiv 2607.08066 — jamais vérifié ; collision la plus sérieuse pour le papier C ;
  2. arXiv 2606.10456 — provenance douteuse ; occupe le contraste marginale/corrélation du lemme : lire les preuves ;
  3. NARCBench (arXiv 2604.01151) et sa suite (arXiv 2609.03035) — agrégation en coupe transversale ou séquentielle ? Les revues divergent sur les chiffres de transfert ;
  4. Terekhov et al. (arXiv 2606.08892) — code et données de l'environnement diffus disponibles ?
- Vérifie aussi la disponibilité et la licence des ressources de la section 7 de l'état de l'art, et rédige le message de demande d'accès à FakeLab (auteurs de arXiv 2607.07368) pour que Lazar l'envoie dès maintenant : l'environnement servira en phase 3.
- Tu peux paralléliser la lecture par sous-agents ; chacun rend un verdict par affirmation, avec la page.
- **Livrable** : `etat-de-l-art-verifie-v1.md` + table des chiffres avec chemin et empreinte du PDF source. Nœud de décision immédiat si une zone revendiquée est occupée (R8).

### T0.3 — Simulation du lemme et du théorème négatif (processeur, coût nul)
- **Objet** : valider sur données synthétiques, avant toute activation réelle, les deux énoncés qui structurent le papier A (programme, section 3).
- **Énoncé positif** (attaque à décalage de marginale) : scores honnêtes indépendants ; chaque action sabotée décale l'espérance du score de δ ; à budget total B = Σδ fixé, faire varier la fragmentation (nombre d'actions sabotées, nombre d'agents N, horizon T). Prédiction : la puissance des agrégateurs séquentiels ne dépend que de B et de la variance ; celle du max par action s'effondre quand la fragmentation croît.
- **Énoncé négatif** (attaque à marginale préservée) : dommage encodé dans la corrélation (copule gaussienne autorégressive, voir le code associé à arXiv 2606.10456). Prédiction : la somme cumulée échoue ; un agrégateur d'autocorrélation ou de co-élévation récupère le signal.
- **Agrégateurs** : max par action, moyenne glissante, max de moyennes glissantes, somme cumulée, processus e de mélange (garantie toujours valide), statistique de co-élévation inter-agents.
- **Indexation agnostique** : tous les agrégateurs prennent un multi-ensemble d'actions indexées par (agent i, pas t) ; N = 1 et N = k sont le même objet.
- Préenregistre les prédictions (signes et formes des courbes) avant de lancer (R1).
- **Livrable** : note mathématique (énoncé précis, hypothèses, distinction entre puissance au sens de Wald et garantie toujours valide — arXiv 2208.07610 ; borne de l'adversaire couvert — arXiv 2601.20022), figures, résultats scellés. C'est la première brique du papier A.

### T0.4 — Harnais d'épisodes et journalisation des activations (processeur, puis GPU sur GO)
- Conception recommandée, à confirmer par toi : génération rapide, puis une passe avant unique sur le transcript complet pour extraire les activations (flux résiduel, couches précoce, médiane et tardive). TransformerLens fait partie de l'outillage de P3 ; des crochets HuggingFace peuvent suffire pour l'extraction — choisis et consigne.
- **Garde d'équivalence** : sur un échantillon, comparer les activations de génération et celles de la passe avant ; tolérance consignée ; garde testée sur un cas sain et sur un artefact (R5).
- **Stockage** : estime-le avant de choisir. Par défaut : activations complètes par token seulement sur un sous-échantillon d'entraînement ; en évaluation, scores de sondes calculés en ligne + vecteurs agrégés par action.
- **Déterminisme** : rejouer un échantillon d'épisodes à graines fixées et exiger l'identité au bit près (P3 l'a obtenue sur 120 chaînes de cinq tours) ; tout écart est une réserve.
- Indexation (i, t) dès le premier jour.
- **Fini quand** : un épisode produit de bout en bout trajectoire + activations + manifeste, scellés et rejouables.

### T0.5 — Environnement (a) v0 : propositions d'expériences
- Vérifie d'abord (T0.2) si le code et les données de Terekhov et al. sont publics ; si oui, porte-les ; sinon, reconstruis une version minimale fidèle.
- Exigence de conception : la tâche se décompose en contributions (i, t) qui resservent telles quelles quand N = k (phases 2 et 3).
- Vérité terrain : cibles semées préenregistrées + vérification différée sur sous-échantillon. Évaluateur faible de confiance sur rubrique structurée.
- Plan B préenregistré : si le 8B est trop faible pour la tâche, rubrique simplifiée. Aucun changement de modèle sans GO.

### T0.6 — Organismes modèles v0 (GPU sur GO pour l'entraînement)
- Famille (i) : instruction cachée. Famille (ii) : réglage fin léger (LoRA) par distillation de contexte — générer avec l'instruction cachée, entraîner sans elle. Famille (iii), si la licence le permet : organismes publics de sandbagging de l'institut britannique (dépôt AI-Safety-Institute/sandbagging_auditing_games, dont un imitant Llama-3.1-8B-Instruct).
- Contrôles croisés : organisme honnête averti de la surveillance (aucune mission) ; saboteur en régime simulé « non observé ».
- Calibration dose-réponse du budget de sabotage (proportion d'actions sabotées × intensité).
- **Fini quand** : effet de sabotage mesurable par la vérité terrain, avec une dose-réponse monotone, pour (i) et (ii).

### T0.7 — Batterie de sondes v0
- Concepts : tromperie (recette Apollo, dépôt ApolloResearch/deception-detection), enjeux élevés (recette McKenzie, dépôt arrrlex/models-under-pressure), dissimulation, conscience d'évaluation.
- Agrégation sur les tokens : **max ou attention uniquement**.
- Familles : linéaire, différence de moyennes, petit perceptron, sonde à attention, Mahalanobis (non supervisée).
- **Plancher obligatoire** : sonde aléatoire appariée en covariance (style P3). Une sonde qui ne le bat pas n'existe pas.
- **Anti-circularité** : jamais d'entraînement et d'évaluation sur les mêmes organismes — entraînement sur données génériques ou sur une famille, évaluation sur une autre.
- **Test de validité dès la v0** : une sonde qui lit « j'ai une instruction cachée » réussit sur (i) et échoue sur (ii) ; une sonde d'intention réussit sur les deux.
- **Fini quand** : AUROC par action au-dessus du plancher, sur (i) et (ii), avec intervalles de confiance.

### T0.8 — Bases boîte noire v0
- Moniteur faible par action ; TRACE-lite (triage–inspection–jugement, réimplémenté d'après arXiv 2606.07054) ; et le même agrégateur séquentiel appliqué aux scores boîte noire (dans l'esprit d'E-valuator, arXiv 2512.03109).
- **Raison** : la porte G1 est un plan 2 × 2 {boîte noire, boîte blanche} × {par action, séquentiel}. Sans base boîte noire séquentielle, le gain de la boîte blanche serait confondu avec le gain de l'accumulation.
- Modèle du moniteur : décision D1.

### T0.9 — Papier C : conception et préenregistrement (processeur ; pilote sur GO)
- **Principe** : la sonde lit les activations de l'agent qui produit le contenu, pas celles du juge. Le juge génératif lit le contenu ; la sonde lit l'agent.
- **Convention** : g = fraction du chemin parcourue par le verdict du moniteur vers le verdict voulu par l'attaquant. g ≈ 0 : robustesse ; g < 0 : auto-incrimination ; g > 0 sans accès aux poids : contamination de construit (le moniteur lit le registre, pas l'intention).
- **Plan 2 × 2 rhétorique × intention** : agent honnête qui plaide sincèrement contre saboteur qui tient le même plaidoyer.
- **Cinq familles d'attaque** : flatterie et supplication ; revendication d'autorité ; approbations forgées ; usurpation stylistique de l'instructeur (influence sans ordre) ; ordres en bande.
- **Moniteurs** : panel de juges génératifs (décision D2) + sondes à agrégation robuste.
- **Leçons de P3 à appliquer** : verdicts lus sur texte complet, jamais sur fenêtre tronquée (dans P3, la troncature a fabriqué un faux effet en lisant des verdicts retardés comme des verdicts changés) ; instruments ordinaux ou continus plutôt que catégoriels — score continu par probabilité du jeton de verdict quand c'est possible ; estimation de g par la régression de la loi d'attraction, Δv = g · (v* − v₀), avec un nul de régression vers la moyenne.
- **Ressources P3 à demander à Lazar** : corpus de pression, code de la loi d'attraction, outils de scellement s'ils existent.
- **Livrable** : préenregistrement scellé et contre-lu de HC1, HC2 (formulation robustesse, jamais immunité absolue), HC2b et HC3, avec signes prédits et liste d'arrêt.

### Porte G0 — prêt pour G1
Tous les critères suivants sont remplis, preuves scellées à l'appui :
1. Harnais validé : déterminisme, équivalence d'activations, gardes testées.
2. Organismes (i) et (ii) : sabotage mesurable avec dose-réponse.
3. Sondes v0 au-dessus du plancher aléatoire apparié, sur (i) et (ii).
4. Base boîte noire, par action et séquentielle, qui tourne sur le même jeu d'épisodes.
5. Agrégateurs validés en simulation (T0.3).
6. Préenregistrement de G1 scellé et contre-lu.
7. Préenregistrement du papier C (HC1 à HC3) scellé et contre-lu.
8. État de l'art vérifié ; aucun chiffre non vérifié dans un document du programme.

Si un critère ne peut pas être atteint d'ici le 1er novembre : nœud de décision, avec options et défaut.

---

## 8. Phase 1 — papier A (M1–M2)

**Préalable** : G0 franchie et GO sur le devis de phase 1. Chaque expérience de cette phase, sauf T1.2 déjà couverte par le préenregistrement de G1, est préenregistrée avant son lancement (R1).

### T1.1 — Organismes finalisés et dose-réponse (E1.1)
- Finalise les familles (i), (ii) et (iii) ; calibre la dose (proportion d'actions sabotées × intensité) sur au moins quatre niveaux, dont zéro.
- Gèle les jeux d'épisodes : entraînement des sondes, calibration des seuils (épisodes honnêtes réservés), évaluation — séparés par famille d'organismes.
- **Fini quand** : courbes dose-réponse scellées ; jeux d'épisodes gelés et empreintés.

### T1.2 — Plan 2 × 2 accès × agrégation (E1.2) — l'expérience de G1
- Quatre bras sur les mêmes épisodes : boîte noire par action ; boîte noire séquentielle ; boîte blanche par action ; boîte blanche séquentielle.
- Métriques : AUROC ; rappel à 1 % de faux positifs, seuils calibrés sur les épisodes honnêtes réservés ; courbe sécurité-utilité à budget d'audit ; latence de détection (alerte contre dommage cumulé). Intervalles par rééchantillonnage des épisodes.
- Garde : le taux de faux positifs des agrégateurs toujours valides est vérifié empiriquement sur épisodes honnêtes ; tout dépassement est une réserve.
- Lecture : effet principal de l'accès (H1) ; effet principal du séquentiel (H2) ; interaction positive = signature de l'additivité interne.
- **Fini quand** : résultats scellés, verdict G1 prononcé (R13).

### T1.3 — Lemme sur données réelles (E1.3)
- À budget total constant, fais varier la fragmentation (nombre d'actions sabotées, intensité par action, horizon) ; mesure la puissance de chaque agrégateur.
- Teste la condition δ > 0 : le sabotage déplace-t-il la marginale des scores par action ? Test préenregistré, par type d'action.
- Les deux issues sont publiables : si δ ≈ 0, le théorème négatif devient central (T1.4).

### T1.4 — Théorème négatif en semi-synthétique (E1.4)
- Scores honnêtes réels + structure de corrélation injectée à marginale préservée (copule, comme en T0.3). Prédiction : la somme cumulée échoue, l'agrégateur d'autocorrélation récupère le signal. Valide sur données réelles ce que T0.3 montre en simulation.

### T1.5 — Attaques adaptatives et transposition token → action (E1.5)
- (a) Par contenu : l'organisme connaît le moniteur, reçoit la consigne de rester sous le seuil, change de persona.
- (b) Pondérales, sous GO : réglage fin contre le score de sonde, avec gradient à travers la sonde (dans l'esprit de Bailey et al.), puis apprentissage par renforcement sans gradient à travers le moniteur (dans l'esprit de RL-Obfuscation), au niveau action.
- Question Tr : la robustesse des agrégations max et attention, établie au niveau token, tient-elle au niveau action sous accumulation séquentielle ? Mesure aussi le coût d'utilité de l'attaque.

### T1.6 — Marge asymétrique (E1.6)
- Interventions non spécifiques à intensité croissante : paraphrase de confiance, ré-échantillonnage, remise à zéro de contexte, bruit d'activations.
- Deux courbes en fonction de l'intensité : utilité honnête et succès d'attaque ; métrique de marge fixée au préenregistrement. Base : Ctrl-Z.

### T1.7 — Transfert concentré (E1.7)
- Le moniteur séquentiel boîte blanche sur un cadre de sabotage concentré de ControlArena : une figure de robustesse, pas un chantier.

### Porte G1 (fin M2)
- **Critère** (D-c, disjonctif) : la boîte blanche séquentielle bat la meilleure base boîte noire, toutes variantes confondues — le comparateur le plus exigeant — avec un rappel à 1 % de faux positifs supérieur et un intervalle de confiance à 95 % qui l'établit, **ou** + 5 points de F1.
- Verdict prononcé selon R13, puis GO de Lazar.
- **Franchie** : rédaction du papier A (section 12) ; phase 2 lancée sur GO.
- **Échouée** : proposition au format de décision — résultat négatif publié + bascule vers H8 dominante (validité de construit).
- À G1, soulève aussi la décision D-b du programme : un co-auteur en analyse séquentielle pour le lemme, ou pas.

---

## 9. Piste C — papier C (M1–M3, en parallèle de la phase 1)

**Préalable** : préenregistrement de HC1 à HC3 scellé (G0) et GO sur le devis de la piste C. TC.4 à TC.6 sont préenregistrées avant leur lancement.

### TC.1 — Gain des juges génératifs (EC.1)
- Panel de juges : décision D2.
- Cinq familles d'attaque × au moins trois intensités + condition sans attaque ; verdicts continus par probabilité du jeton de verdict, lus sur texte complet.
- g estimé par juge et par famille, par la régression de la loi d'attraction, avec nul de régression vers la moyenne.
- **Fini quand** : table g × juge × famille, avec intervalles, scellée.

### TC.2 — Sondes sous les mêmes attaques (EC.2)
- Plan 2 × 2 rhétorique × intention : honnête sans plaidoyer, honnête qui plaide sincèrement, saboteur sans plaidoyer, saboteur qui plaide — même registre rhétorique dans les deux bras qui plaident (contrôle du style).
- Lecture : g_sonde ≈ 0 → robustesse (HC2) ; g_sonde < 0 → auto-incrimination (HC2b) ; g_sonde > 0 sans accès aux poids → contamination de construit, bascule de titre à GC.

### TC.3 — Usurpation (EC.3)
- (a) Ordres en bande : effet sur les juges sans protocole ; taux d'alarme sous le protocole « contenu = données ».
- (b) Usurpation stylistique : contenu qui imite le style de l'instructeur sans rien ordonner ; g résiduel sur juges et sur sondes (HC3).

### TC.4 — Taxe de déplacement (EC.4), sous GO
- Côté rhétorique : coût (requêtes, accès boîte noire, calcul) pour atteindre un déplacement cible sur les juges.
- Côté obfuscation : coût pour atteindre le même déplacement sur les sondes, en réutilisant les codes d'obfuscation d'activations publiés, portés sur 8B (accès aux poids).
- Livrable : rapport de coût et niveau d'accès requis (HC4).

### TC.5 — Contre-mesures (EC.5)
- Paraphrase de confiance avant jugement ; quorum hétérogène (juges + sondes) ; matrice de transfert des attaques de corruption — une attaque optimisée contre le moniteur A déplace-t-elle B ? (HC5).

### TC.6 — Le g bénin prédit-il la robustesse ? (EC.6)
- Panel de moniteurs assez large pour estimer une corrélation informative — taille fixée au préenregistrement : variantes de juges (modèles, consignes) et de sondes.
- g mesuré sur corpus de pression bénins, puis robustesse sous attaque optimisée par un attaquant itératif ; corrélation préenregistrée (HC6).

### Porte GC (fin M2)
- Verdict, selon R13, sur le signe de g_sonde et sur l'état de la collision arXiv 2607.08066 (vérifiée en T0.2).
- g_sonde > 0 sans accès aux poids → proposition de bascule de titre (contamination de construit). Collision qui couvre déjà la loi de déférence → recentrage sur HC4 et HC6. Sinon : rédaction du papier C (section 12) après TC.4 à TC.6.

---

## 10. Phase 2 — papier B (M3–M4)

**Préalable** : G1 prononcée et GO sur le devis de phase 2.

### T2.0 — Passage à N agents
- Les contributions (i, t) existent depuis T0.5 ; vérifie que harnais et agrégateurs fonctionnent tels quels pour N = 2 et 3. Test d'indexation agnostique : N = 1 doit reproduire la phase 1 au bit près.

### T2.1 — Division du travail (E2.1)
- Avec et sans planificateur ; réplique l'effet de fragmentation (les moniteurs par-instance boîte noire se dégradent à budget constant) ; ajoute la vue interne (scores de sondes par agent).

### T2.2 — Collusion (E2.2)
- Canaux explicites (artefacts partagés, messages) contre coordination sans canal par poids partagés (points de Schelling) ; défenses-ingrédients : paraphrase, brouillage des canaux ; mesure du succès de coordination.

### T2.3 — Statistiques inter-agents (E2.3)
- Corrélation des scores de sondes entre agents, honnêtes contre attaquants ; détecteur de co-élévation. Bases : agrégateurs de NARCBench (alignement d'activations, pic de suspicion), réutilisés ou réimplémentés, assumés comme bases et non comme concurrents.

### Porte G2 (fin M4)
- **Critère préenregistré** : effet de fragmentation répliqué **et** statistique de population supérieure à l'agrégation par agent.
- Échec → proposition de recentrage du papier B sur le temporel N = 1.

---

## 11. Phase 3 — papier B (M4,5–M6)

**Préalable** : G2 franchie, GO sur le devis de phase 3, environnement (b) porté en poids ouverts (FakeLab si l'accès est accordé, sinon Iterative VibeCoding dans ControlArena).

### T3.1 — Statistique spatio-temporelle (E3.1)
- Contre séquentiel par agent seul et contre coupe transversale (position NARCBench) ; grille N selon D3 ; courbes sécurité(N) boîte blanche contre boîte noire (H3) ; environnement (a), puis (b).

### T3.2 — Diversification adverse (E3.2)
- Personas, variantes de réglage fin, Qwen2.5-7B comme agent hétérogène ; mesure du compromis entre décorrélation des signatures et capacité de coordination (H4′) ; transfert des sondes entre variantes.

### T3.3 — Nombre × diversité des moniteurs (E3.3)
- Panel de sondes sur les six axes de diversité (programme, section 8.2) ; attaques optimisées contre un membre ; matrice de transfert d'attaque ; M copies de graines contre panel complet à M égal (H5).

### T3.4 — Riposte (E3.4)
- Quatre politiques — visible immédiate, différée randomisée, silence-puis-frappe, pot de miel — × itérations d'adaptation de l'équipe rouge ; pente de sélection ; fuite mesurée par l'information mutuelle empirique entre l'état de détection et les observations rouges ; deux ablations : seuil stochastique contre fixe, trafic de couverture contre sans (H7).

### Bases à battre
- Link-tracker et ensemble à quatre moniteurs (Hills et al.) ; monitoring à état sur flotte (Brown et al.) — réutilisés ou réimplémentés.

### Porte G3
- L'environnement (d) n'ouvre que si un proxy de vérité différée fiable et bon marché est validé. Si le budget le permet, tu peux proposer en M5 une petite étude de validation du proxy. Sinon, (d) est abandonné sans coût.

---

## 12. Rédaction, soumission, libération

Pour chaque papier :
1. **Figures d'abord** : chaque figure est produite par un script à partir de résultats scellés ; chaque chiffre du texte renvoie à un fichier et à une empreinte (R6).
2. **Travaux connexes** : uniquement à partir de l'état de l'art vérifié (T0.2 et mises à jour de veille) ; la liste des revendications interdites (état de l'art, section 5) est vérifiée ligne à ligne.
3. **Avant la version finale** : une recherche d'antériorité fraîche sur les trois derniers mois par un sous-agent neuf, chargé de chasser les collisions ; puis une relecture adverse par un autre sous-agent neuf qui joue le relecteur de conférence.
4. **Limites et menaces à la validité** explicites, y compris les bascules non prises.
5. **Cibles** : papier A — arXiv + atelier ; papier C — arXiv + atelier, puis conférence courte ; papier B — NeurIPS 2027, repli ICLR 2028. Vérifie les dates limites réelles le moment venu.
6. **Soumission et publication** : nœud de décision — tu livres le paquet de soumission, Lazar soumet.

**Libération, en fin de programme** : code, sondes, organismes. Tu prépares le paquet ; la publication se fait sur GO. Pour les organismes saboteurs, suis les usages établis du champ (organismes publiés avec leur documentation, comme ceux de l'institut britannique) ; toute hésitation est un nœud de décision.

---

## 13. Veille et bascules

- **Veille hebdomadaire** : arXiv ; LessWrong et Alignment Forum ; blogs de Redwood Research et d'alignement d'Anthropic ; institut britannique (équipe boîte blanche, ControlArena) ; équipe NARCBench. Consignée dans `registres/veille`.
- Tu n'écris à Lazar que si une parution change une revendication, avec la bascule pré-engagée correspondante (programme, section 13) :

| Déclencheur | Action |
|---|---|
| Publication externe du cœur séquentiel sur sondes | Arrêt des tâches concernées ; proposition de bascule vers l'épidémiologie de population et la curation de données |
| Collision arXiv 2607.08066 confirmée sur la loi de déférence | Recentrage du papier C sur HC4 et HC6 |
| g_sonde > 0 sans accès aux poids | Papier C réorienté sur la contamination de construit |
| G1 échoue | Résultat négatif publié + H8 dominante |
| G2 échoue | Papier B recentré sur le temporel N = 1 |
| 8B trop faible sur l'environnement (a) | Rubrique simplifiée ; changement de modèle seulement sur GO |
| Élicitation rouge insuffisante | Import des politiques d'attaque publiées |
| Pas de proxy de vérité différée | Environnement (d) abandonné sans coût |

---

## 14. Calcul et dépenses

- **Aucune dépense GPU sans GO.** Avant chaque phase, un devis : heures GPU par tâche, type d'instance, prix indicatif sur Vast.ai, stockage, marge de 30 %. Un GO par devis ; aucune dépense hors devis approuvé.
- Tant qu'un devis n'est pas approuvé, tu avances sur tout ce qui tourne sur processeur, et sur des tests avec un très petit modèle si c'est utile.
- Registre des dépenses tenu à jour ; alerte à Lazar à 80 % d'un devis approuvé.
- Inventaire des instances actives à chaque reprise et à chaque passation ; arrêt par identifiant (R10) ; aucune instance orpheline facturée.
- Si aucun GPU n'est accessible depuis ta machine, prépare les scripts de lancement Vast.ai : Lazar lance.
- Si un budget de calcul de bourse arrive, Lazar te le dira ; l'ordre des phases ne change pas.

---

## 15. Communication avec Lazar

- En français, tutoiement, quasi zéro acronyme : développe les termes. Les détails vont dans les fichiers, pas dans les messages.
- Format : **verdict d'abord** (1 à 3 lignes), puis seulement erreurs, changements et décisions, une ligne chacun.
- **Format de décision** : la décision en une phrase ; l'enjeu en 1 à 2 lignes ; 2 ou 3 options avec avantages et inconvénients, une ligne chacune ; recommandation et confiance (haute, moyenne, basse) ; défaut appliqué sans réponse sous 48 heures.
- Tu ne lui écris que pour : un **prononcé** (un résultat qui change une décision, dont chaque verdict de porte), une **réserve**, une **divergence non résolue**, une **demande de GO**, une **dépense**. Le reste vit dans les registres.

---

## 16. Ton premier rendu

Dans ta première session, sans attendre de GO :
1. Le plan de phase 0 ordonnancé : dépendances, chemin critique, ce qui tourne sur processeur et ce qui demande un GPU.
2. Le devis détaillé de la phase 0, et une estimation grossière par phase pour tout le programme (ordre de grandeur des heures GPU et du coût).
3. Les ressources à demander à Lazar : corpus de pression et code de la loi d'attraction de P3, outils de scellement de P3 s'ils existent, jeton d'accès HuggingFace (modèles à accès restreint), choix du dépôt distant, et le message aux auteurs de FakeLab — rédigé par toi, envoyé par Lazar.
4. Les trois risques principaux de la phase 0 et les trois du programme, chacun avec sa parade.
5. Le démarrage immédiat de T0.1, T0.2 et T0.3, dont `CLAUDE.md`, `registres/etat.md` et ta première passation.

Livre ce rendu en un zip versionné avec ses pièces (R12).

---

## 17. Ce que tu ne fais pas

- Franchir une porte sans verdict scellé (R13) et sans GO.
- Lancer une phase ou une dépense sans GO sur son devis.
- Utiliser une agrégation moyenne ou médiane sur les tokens dans une sonde de production.
- Faire entrer un chiffre de l'état de l'art dans un préenregistrement ou un papier sans vérification (R7).
- Changer de modèle sans GO.
- Contacter quelqu'un, soumettre, publier ou ouvrir un dépôt public.
- Modifier le programme : tu proposes, Lazar décide.
