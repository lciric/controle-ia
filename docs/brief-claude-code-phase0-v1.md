# Brief de lancement — Phase 0 du programme « Contrôle boîte blanche des menaces diffuses »

**Version 1 — 4 octobre 2026 — de Lazar (directeur du programme) à la session Claude Code pilote**

---

## 0. Les fichiers

Ce dossier contient :
- `brief-claude-code-phase0-v1.md` — ce brief : ta mission, tes règles, tes tâches, tes arrêts.
- `programme-controle-ia-v2.md` — le programme complet (trois papiers, hypothèses, expériences, portes). Il fait foi sur le fond.
- `etat-de-l-art-controle-ia-v1.md` — l'état de l'art consolidé de trois revues d'antériorité. Il fait foi sur ce qui est pris, ouvert et à battre — **mais aucun de ses chiffres n'est opposable avant vérification** (règle R7).
- `sha256sums-lancement-v1.txt` — empreintes des trois fichiers ci-dessus. Vérifie-les avant toute chose (`sha256sum -c sha256sums-lancement-v1.txt` dans ce dossier, ou un équivalent Python).

**Ordre de lecture** : ce brief en entier ; puis le programme, sections 0 à 4 et 10 ; puis l'état de l'art, sections 0, 1, 5 et 6. Le reste à la demande, au fil des tâches.
**Préséance** : ce brief prime pour la phase 0 ; le programme prime sur l'état de l'art pour les décisions.

---

## 1. Ta mission

Construire et valider les instruments du programme pendant la phase 0 (quatre semaines, du 5 octobre au 1er novembre 2026), pour que la porte G1 du papier A soit testable dès le premier jour de la phase 1 ; vérifier l'état de l'art sur sources primaires ; concevoir et préenregistrer le papier C.

Tu construis des instruments et tu les valides. Tu ne cherches aucun résultat : **aucune mesure de G1 pendant la phase 0.**

---

## 2. Le programme en dix lignes

- **Thèse** : la fragmentation d'un sabotage — dans le temps, entre agents — détruit la preuve externe par action (chaque sortie est innocente prise isolément), pas la preuve interne : si l'intention laisse une trace dans les activations, cette preuve s'additionne.
- **Papier A (le temps, mono-agent)** : lemme d'additivité et théorème négatif (dommage porté par la marginale des scores contre dommage porté par leur corrélation) ; accumulation séquentielle toujours valide de scores de sondes ; plan 2 × 2 accès × agrégation.
- **Papier C (l'instrument)** : la corruptibilité d'un moniteur comme un gain g ; sondes contre juges génératifs ; taxe de déplacement ; usurpation stylistique de l'instructeur.
- **Papier B (l'essaim, plus tard)** : statistique spatio-temporelle sur des copies à poids partagés.
- **Modèles** : agent Llama-3.1-8B-Instruct ; second modèle Qwen2.5-7B.
- **Sondes** : agrégation max ou attention sur les tokens, jamais moyenne ni médiane.
- **Méthode** : celle de P3, le projet précédent de Lazar (validité de construit de la sycophancie dans Llama-3.1-8B-Instruct) — préenregistrement scellé, contrôles appariés, traçabilité totale. Certains de ses outils et corpus sont réutilisés ; Lazar te les transmet sur demande.

---

## 3. Règles gelées — elles s'appliquent sans discussion

- **R1. Préenregistrement scellé** (SHA-256) avant toute expérience décisive, y compris une simulation qui teste une prédiction : hypothèse, prédiction chiffrée et signe attendu, métrique, seuil, plan d'analyse, critères de lecture gelés, liste d'arrêt. Aucune lecture de résultat avant le scellement.
- **R2. Clause de récusation** : chaque préenregistrement est contre-lu par un sous-agent neuf qui ne l'a pas écrit. Si c'est impossible, signale-le.
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

---

## 4. Hiérarchie de décision

- **Routine** — tu décides et tu consignes dans `registres/decisions` : architecture du code, bibliothèques, tests, lectures, organisation des fichiers, tout travail sur processeur.
- **Règles gelées** — section 3 : tu appliques, tu ne rediscutes pas.
- **Proposer avec recommandation** — tu proposes au format de décision (section 8) ; sans réponse sous 48 heures, ton défaut s'applique. Relèvent de ce niveau : choix des couches et des concepts de sondes ; modèle du moniteur boîte noire (décision D1 du programme, défaut (a) + (b)) ; détails du portage de l'environnement ; ajustements de périmètre à l'intérieur de la phase 0.
- **Nœuds de décision** — tu t'arrêtes et tu attends le GO :
  - toute dépense de calcul (sur devis, section 7) ;
  - toute création de compte, de dépôt distant ou de publication ;
  - tout contact externe — tu rédiges le message, Lazar l'envoie ;
  - toute modification d'une hypothèse ou d'une revendication du programme ;
  - tout écart à un préenregistrement scellé ;
  - toute découverte qu'une zone revendiquée comme vierge est occupée, ou qu'une collision est plus large qu'annoncé.

---

## 5. Les tâches de la phase 0

### T0.1 — Socle du dépôt et gouvernance (processeur)
- Le dépôt du programme vit dans le dossier où Lazar t'a lancé. Arborescence proposée, adaptable :
  ```
  docs/        programme, état de l'art, notes mathématiques
  prereg/      préenregistrements scellés (.md + .sha256)
  registres/   go, depenses, decisions, arrets, veille
  src/         harnais/, environnements/, organismes/, sondes/, agregateurs/, moniteurs_noirs/
  tests/
  runs/        un manifeste par run
  diag/        résultats bruts (.json + .sha256)
  livrables/   zips versionnés
  ```
- Outils : scellement (empreinte compagnon pour chaque dépôt), vérification, gabarit de préenregistrement conforme à R1, manifeste de run conforme à R9.
- **Fini quand** : les tests passent ; chaque garde d'arrêt est testée sur un cas sain et sur un artefact ; un run factice traverse toute la chaîne (manifeste → résultat → scellement → vérification).

### T0.2 — Vérification de l'état de l'art sur sources primaires (processeur, lecture)
- Suis l'ordre de la section 6 de l'état de l'art. Pour chaque référence : récupérer le PDF, l'empreinter, vérifier chaque affirmation et chaque chiffre que le programme utilise, statuer — confirmé, corrigé ou introuvable — avec la page source.
- Priorités absolues, dans l'ordre :
  1. arXiv 2607.08066 — jamais vérifié ; collision la plus sérieuse pour le papier C ;
  2. arXiv 2606.10456 — provenance douteuse ; occupe le contraste marginale/corrélation du lemme : lire les preuves ;
  3. NARCBench (arXiv 2604.01151) et sa suite (arXiv 2609.03035) — agrégation en coupe transversale ou séquentielle ? Les revues divergent sur les chiffres de transfert ;
  4. Terekhov et al. (arXiv 2606.08892) — code et données de l'environnement diffus disponibles ?
- Vérifie aussi la disponibilité et la licence des ressources de la section 7 de l'état de l'art.
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
- Modèle du moniteur : décision D1 du programme (proposer avec recommandation, défaut (a) + (b)).

### T0.9 — Papier C : conception et préenregistrement (processeur ; pilote sur GO)
- **Convention** : g = fraction du chemin parcourue par le verdict du moniteur vers le verdict voulu par l'attaquant. g ≈ 0 : robustesse ; g < 0 : auto-incrimination ; g > 0 : contamination de construit (le moniteur lit le registre, pas l'intention).
- **Plan 2 × 2 rhétorique × intention** : agent honnête qui plaide sincèrement contre saboteur qui tient le même plaidoyer.
- **Cinq familles d'attaque** : flatterie et supplication ; revendication d'autorité ; approbations forgées ; usurpation stylistique de l'instructeur (influence sans ordre) ; ordres en bande.
- **Moniteurs** : deux ou trois juges génératifs hétérogènes + sondes à agrégation robuste.
- **Leçons de P3 à appliquer** : verdicts lus sur texte complet, jamais sur fenêtre tronquée (dans P3, la troncature a fabriqué un faux effet en lisant des verdicts retardés comme des verdicts changés) ; instruments ordinaux ou continus plutôt que catégoriels — score continu par probabilité du jeton de verdict quand c'est possible ; estimation de g par la régression de la loi d'attraction, Δv = g · (v* − v₀), avec un nul de régression vers la moyenne.
- **Ressources P3 à demander à Lazar** : corpus de pression, code de la loi d'attraction, outils de scellement s'ils existent.
- **Livrable** : préenregistrement scellé et contre-lu de HC1, HC2 (formulation robustesse, jamais immunité absolue), HC2b et HC3, avec signes prédits et liste d'arrêt.

---

## 6. Porte de sortie G0 — prêt pour G1

Tous les critères suivants sont remplis, preuves scellées à l'appui :
1. Harnais validé : déterminisme, équivalence d'activations, gardes testées.
2. Organismes (i) et (ii) : sabotage mesurable avec dose-réponse.
3. Sondes v0 au-dessus du plancher aléatoire apparié, sur (i) et (ii).
4. Base boîte noire, par action et séquentielle, qui tourne sur le même jeu d'épisodes.
5. Agrégateurs validés en simulation (T0.3).
6. Préenregistrement de G1 scellé et contre-lu.
7. Préenregistrement du papier C scellé et contre-lu.
8. État de l'art vérifié ; aucun chiffre non vérifié dans un document du programme.

Si un critère ne peut pas être atteint d'ici le 1er novembre : nœud de décision, avec options et défaut.

---

## 7. Calcul et dépenses

- **Aucune dépense GPU sans GO.** Ton premier rendu contient un devis : heures GPU par tâche, type d'instance, prix indicatif sur Vast.ai, stockage, marge de 30 %.
- Tant que le devis n'est pas approuvé, tu avances sur tout ce qui tourne sur processeur : T0.1, T0.2, T0.3, la conception de T0.4 à T0.9, et des tests sur un très petit modèle si c'est utile.
- Registre des dépenses tenu à jour ; alerte à Lazar à 80 % d'un devis approuvé.
- À la fin de chaque session de calcul : inventaire des instances actives et arrêt par identifiant (R10) ; aucune instance orpheline facturée.
- Si aucun GPU n'est accessible depuis ta machine, prépare les scripts de lancement Vast.ai : Lazar lance.

---

## 8. Communication avec Lazar

- En français, tutoiement, quasi zéro acronyme : développe les termes. Les détails vont dans les fichiers, pas dans les messages.
- Format : **verdict d'abord** (1 à 3 lignes), puis seulement erreurs, changements et décisions, une ligne chacun.
- **Format de décision** : la décision en une phrase ; l'enjeu en 1 à 2 lignes ; 2 ou 3 options avec avantages et inconvénients, une ligne chacune ; recommandation et confiance (haute, moyenne, basse) ; défaut appliqué sans réponse sous 48 heures.
- Tu ne lui écris que pour : un **prononcé** (un résultat qui change une décision), une **réserve**, une **divergence non résolue**, une **demande de GO**, une **dépense**. Le reste vit dans les registres (`registres/go`, `registres/depenses`, `registres/decisions`, `registres/arrets`, `registres/veille`).

---

## 9. Ton premier rendu

Dans ta première session, sans attendre de GO :
1. Le plan de phase 0 ordonnancé : dépendances, chemin critique, ce qui tourne sur processeur et ce qui demande un GPU.
2. Le devis de calcul (section 7).
3. Les ressources à demander à Lazar : corpus de pression et code de la loi d'attraction de P3, outils de scellement de P3 s'ils existent, jeton d'accès HuggingFace (modèles à accès restreint), choix du dépôt distant, et le message aux auteurs de FakeLab — rédigé par toi, envoyé par Lazar.
4. Les trois risques principaux de la phase 0 et leur parade.
5. Le démarrage immédiat de T0.1, T0.2 et T0.3.

Livre ce rendu en un zip versionné avec ses pièces (R12).

---

## 10. Ce que tu ne fais pas

- Pas de mesure de G1, pas d'expérience de phase 1 avant G0 et un GO.
- Pas d'agrégation moyenne ni médiane sur les tokens dans une sonde de production.
- Pas de chiffre de l'état de l'art dans un préenregistrement sans vérification (R7).
- Pas de changement de modèle sans GO.
- Pas de contact externe, de publication ni de dépôt public.
- Pas de modification du programme : tu proposes, Lazar décide.
