# README v3 — contre-lecture

Contre-lecteur : sous-agent neuf, qui n'a écrit ni le README v3 ni son journal des changements, en lecture seule, avec les sources données explicitement (note v3, résultats de T0.3, proposition v2, proposition publique v1, CV, LISEZMOI de l'expurgation). Deux passages : le premier sur la version proposée, le second sur la version corrigée. Rapports recopiés tels quels, puis suites données.

## Premier passage (2026-10-08, vers 23:30 UTC)

**Verdict : à corriger avant fusion. 3 majeures, 9 mineures. Les nombres de T0.3 sont exacts.**

**Majeures**

1. « G0, is planned for December 2026, at the start of the grant period » (statut, feuille de route). La phrase est conforme à proposal-v2 §6–7. Elle contredit pourtant `registres/etat.md` l. 6 et 34, et R-094 (confirmé par Lazar le 7 oct. : « G0 au 1er novembre »). Le parcours de lecture renvoie l'évaluateur vers ces registres. La source est hors dépôt, et une date de porte est un nœud. → Garder le 1er novembre, ou consigner d'abord une décision et la citer.
2. L2 : « down to a floor strictly above α ». La note §3 pose un cadre gaussien i.i.d., un seuil exact et un budget réparti également. Le plancher vaut « à n fixé » et tend vers α si n → ∞ avec B√(log n)/n → 0. → « (Gaussian i.i.d. scores, exact threshold, equal split) … strictly above α at fixed n ».
3. T1 : « a test based on it has a power equal to its false-alarm rate » omet la condition que l'aléa du test soit indépendant de l'attaque. T2 : « the attacker adds an independent, uniformly drawn element of H ». « adds » est faux : il s'agit d'une composition. Il manque aussi π_Y ∈ H, et σ doit être indépendante de Y et de l'aléa de l'attaquant, puis appliquée après π_Y (note §4). → « applies its own permutation in H, then an independent uniform element of H ».

**Mineures**

4. « Proposition 1 of arXiv 2606.10456 [is] therefore false for the sum in class K ». La phrase suit la note §6. Mais la proposition est énoncée pour une marginale empirique exactement préservée, et elle est donc vide (`rapport-2606.10456-v1.md` §3). → « vacuous as stated; applied by the paper to its own construction (class K), its conclusion fails for the sum ».
5. « Time (one agent) and a swarm (several agents) are then two subgroups » : une configuration n'est pas un sous-groupe. → Parler des permutations du temps par agent et de celles des agents par pas (note §4).
6. Classe K : « under positive dependence » ne s'applique pas au max. En dépendance négative, la somme et l'e-process passent sous α (note §4). → Ouvrir la phrase par « Under positive dependence » et ajouter le cas négatif.
7. Autres conditions omises (note §1–4) : L1 : préciser « in class M » ; L3 : la borne dépend de (B, n₀, F₀, ρ, α) et suppose (V) ; « needs change detectors » est une mise en garde (L3 d), pas un résultat ; L5 suppose B_net = 0 ; T3 exige w·v ≥ c_{n,w,α} et ne couvre pas Page.
8. Simulations (`resultats-T0.3-v1.md`, magnitudes 4–6), à ajouter : φ₀ = 0,5 et T = 300 (φ n'est défini nulle part) ; τ = 0,2, avec n₀ = 200 et 1 000 ; « five highest scores placed consecutively, w = 5 » ; B en unités de σ, et une définition de α.
9. Tiers : « kept only so that the quotation checks can be verified » est faux pour `donnees/`. Ce sont des sorties de T0.5, « à purger avant toute publication du dépôt » (`docs/procedures/T0.5-extraction-v1.md` l. 248). La liste est aussi incomplète (LISEZMOI §2). Hors README, problème majeur : le dépôt est public (vérifié) et sert `livrables/candidature-ea-funds-v1/`, marquée « confidentielle ».
10. Parcours, point 2 : la date, les 8 pages et le calendrier sont exacts (§7). Mais le PDF affiche « Lazar [SURNAME], [position] », « please do not redistribute » et G0 au 1er novembre. → Le signaler, ou publier une v2.
11. Cohérence : « The plan. Three papers » contredit la feuille de route, qui renvoie Paper B au plan à douze mois. « Progress so far » évoque L4, absent de la section théorie, et T4 est omis.
12. Pied de page : `livrables/readme-v3/` n'est pas suivi par git, sans `.sha256` ni copie scellée. R-112 et N-016 sont absents des registres. Le journal parle de « branche », mais le travail est sur `main`.

**Rien trouvé** : contrôle 4 : auteurs, revues, années et rôles conformes, DOI vérifié, correction présente dans le dépôt P3 ; contrôle 7 : aucun contenu interdit ; dans les contrôles 1 à 3 : valeurs et conditions n₀, B, m, φ₁ ; « within the horizon n₀ » (L1) ; mois 1–7, GC, G1 et critères de G0.

## Second passage (2026-10-08, vers 23:40 UTC)

**Reste à corriger : 1 majeure, 6 mineures, 1 style.**

1. **Majeure, L3.** Le README dit « independent or martingale-difference increments, known mean, bounded variance ». La note §1 (V) exige en plus des incréments conditionnellement sous-gaussiens, et σ connu ou majoré. → « under the honest distribution, increments independent or martingale differences, conditionally sub-Gaussian with parameter σ²; known mean; σ known or bounded by a known value ».
2. **Mineure, L4.** Des conditions de la note §3 manquent. → Ajouter « path by path », « with no interference between agents and a fixed number of actions per step », « also when read anytime-valid » et « its threshold assumes agents independent within a step ».
3. **Mineure, T3.** « (scan, Page's CUSUM, co-elevation) » : la note ne couvre que le balayage et la co-élévation. → « (scan, co-elevation) ».
4. **Mineure, T4.** « such as moving the highest scores to the end » : si les ordres relatifs ne sont pas conservés, la domination peut échouer. → « dominated, path by path, … such as an increasing sort, or moving the r highest scores to the end while keeping relative orders ».
5. **Mineure, proposition 1.** L'hypothèse n'est pas énoncée, et la marginale en jeu est empirique (rapport §3, l. 37–38, 72–75). → « …claims that any monitor whose rule depends only on the empirical marginal has a power equal to its false-positive rate when the attack leaves that empirical marginal exactly benign; no attack can do so for a continuous benign distribution, and on the paper's own construction… » (suite inchangée).
6. **Mineure, textes de tiers.** Le paragraphe omet trois éléments, tous suivis par git : le texte complet de 2606.08892 (`docs/sources/invites-2606.08892-v1/extrait.tar`) ; un extrait de 2606.07054 (`docs/sources/invites-2606.07054-v1/extrait.tar`) ; les cartes de modèles (`docs/sources/cartes-modeles-20261006/`). → Les ajouter.
7. **Mineure, journal des changements.** Il n'existe pas de branche `readme-v3` : le travail est sur `main`. N-016, N-017 et R-112 sont absents des registres. Manquent `verification-readme-v3.md`, les `.sha256` et la copie scellée. « avec leurs conditions » et « constat exact » ne seront vrais qu'une fois les points 1 à 6 corrigés. Les autres lignes sont exactes.

**Style.** L2 : « at fixed n » → « at fixed n₀ ». L1 : ajouter « and the rule's parameters ».

**Rien** : In one minute, parcours de lecture (numérotation 1–4), T1, T2, L5, C/K, réglages des simulations.

## Suites données

- Premier passage : points 2 à 8, 10 et 11 appliqués comme proposé (point 10 : la proposition publique v1 est retirée du parcours plutôt que signalée). Point 9 : paragraphe réécrit ; l'exposition du dépôt est consignée en nœud N-016. Point 12 : branche `readme-v3`, registres (R-112, N-016, N-017), copie scellée, empreintes et ce rapport, avant le commit.
- Premier passage, point 1 : **non appliqué**. Le README garde « December 2026 », ce que le financeur a reçu ; l'écart avec `registres/etat.md` et R-094 est consigné en nœud N-017, à trancher par Lazar avant la fusion.
- Second passage : points 1 à 6 et style appliqués mot pour mot. Point 7 : réglé par le commit qui porte ce rapport.
