# Note d'antériorité — P-041 (attaque et défense en organisme coévolutif, avantage du terrain à la défense) — lecteur neuf — v1

30 octobre 2026, rédigée de 16:05 à 16:45 UTC environ. Auteur : sous-agent lecteur neuf (Claude Opus 5.5), qui n'a écrit ni P-041 ni aucune pièce de conception du programme. Aucun commit.

- **Pièce vérifiée** : `docs/decisions/proposition-P-041-organisme-coevolutif-attaque-defense-v1.md`, empreinte `254b178270f11123c4bf0c24ead0855c982550730c54bcba0924a39c6d04ca9b` (contrôlée avec son `.sha256`).
- **Affirmation du directeur à vérifier** : « les composantes existent séparément ailleurs, mais n'ont jamais été réunies ».
- **PDF versés** : `docs/sources/pdf/anteriorite-P-041-v1/`, 66 PDF, chacun avec un `.sha256` à nom nu ; les 66 contrôles `sha256sum -c` passent ; les 66 fichiers sont de type `application/pdf`.
- **Règles appliquées** : R7 (rien d'opposable sans PDF empreinté et page citée ; ce qui n'a pas été lu sur PDF est marqué « non lu ») ; R8 (une zone vierge est une question ; la limitation d'un papier n'est pas un trou du champ ; les zones séduisantes sont vérifiées plus durement).
- Les pages citées sont les pages du fichier PDF (première page = 1), pas la pagination imprimée des revues.

## 0. Grille de lecture

Les huit composantes de la demande :

- **C1** défense coévolutive contre des attaques évolutives, en sûreté et en contrôle des intelligences artificielles ;
- **C2** défense informée de la recette de l'attaque (entraînement adverse, robustesse certifiée, attaques adaptatives, transfert à des menaces imprévues) ;
- **C3** attaque dans l'espace des activations avec défense informée ;
- **C4** algorithmes coévolutifs : pathologies (cyclage, désengagement, surspécialisation) et remèdes (archives, tournoi maître, concepts de solution) ;
- **C5** protocoles de contrôle avec équipes rouge et bleue, surveillance ;
- **C6** jeux de Stackelberg et avantage du défenseur ;
- **C7** auto-jeu et coévolution ouverte d'agents fondés sur des grands modèles de langage ;
- **C8** évaluation sur familles tenues à l'écart conçues par des tiers, et **C8b** mesure de la boucle elle-même (fausses promotions, juge figé ou dérivant).

Les cinq composantes du test de combinaison demandé (au moins trois à la fois) :

- **K1** coévolution attaque–défense : tours répétés où chaque camp s'adapte au dernier état de l'autre ;
- **K2** défense informée : **[p]** paramètres ou recette de l'attaque connus de la défense ; **[é]** la défense ne voit que des échantillons d'attaque ; **[c]** la défense connaît une classe de menace déclarée et calcule elle-même l'attaque dans cette classe ;
- **K3** attaque dans l'espace des activations : sans crochet, attaque ou perturbation adverse sur les activations d'un vrai modèle ; **[d]** seule la défense lit les activations, l'attaque reste en entrée ; **[l]** niveau des lois (distributions synthétiques ou espace des traits), qui est le niveau visé par P-041 (« attaque au niveau des lois sur activations synthétiques ») ;
- **K4** mesure sur familles tenues à l'écart conçues par des tiers ; **[m]** tenues à l'écart mais conçues par les mêmes auteurs ; « côté attaque » : ce sont des moniteurs tenus à l'écart, non des familles d'attaque ;
- **K5** barrière certifiée sur une classe déclarée (garantie démontrée) ; **[g]** garantie d'une autre nature (à l'équilibre, de convergence, ou borne de généralisation).

Les noms de revues et de conférences cités (NeurIPS, ICLR, ICML, TMLR, JAIR, JMLR, KDD, GECCO, IJCAI, AISTATS, COLM, ECTA) sont des noms propres de lieux de publication ; les noms d'attaques et de bancs (GCG, PAIR, TAP, AutoDAN, MAD, ImageNet-UA…) sont des noms propres d'artefacts.

## 1. Verdict R8

**Collision partielle.** Toutes les composantes existent et sont vérifiées sur PDF. Contrairement à l'affirmation du directeur, **plusieurs paires et trois triplets sont déjà réunis** dans des travaux publiés. **Aucun travail lu ne réunit quatre des cinq composantes K**, ni n'associe la barrière certifiée (K5) à la coévolution (K1) ou à l'attaque dans les activations (K3), ni ne réunit coévolution, activations et familles de tiers (K1+K3+K4). Niveau : 66 PDF lus (5 en entier, 8 pour le corps entier, 53 sur pages ciblées) et 186 citants examinés sur titre (181 distincts), dont 14 sur résumé et 4 sur PDF ; la recherche n'est pas exhaustive (section 7).

### 1.1 Table des combinaisons

| Combinaison | Réunie ? | Où (fichier, pages) | Niveau |
|---|---|---|---|
| K1+K2[p] | **oui** | Dalvi et collègues 2004 : « information complète », la défense connaît tous les paramètres de l'adversaire, jeu répété (`Dalvi-2004-…`, p. 3–4, 8–9) ; Terekhov et collègues 2026 : la défense voit les invites et les scores de l'équipe rouge et se réoptimise contre une base croissante d'attaques (`2606.08892v2`, p. 6–7, 25, 28) ; Wang 2019, double oracle (`Wang-2019-…`, p. 1–2) | PDF |
| K1+K2[é] | **oui, fréquent** | MAGIC (`2602.01539v2`, p. 5–7) ; AgentSafeEvo (`2610.19422v1`, p. 4–7) ; EvoSafety (`2605.13411v1`, p. 3–7) ; RvB (`2601.19726v1`, p. 3–6, 13) ; Self-RedTeam (`2506.07468v4`, p. 1–2) ; Bailey et collègues (`2412.09565v2`, p. 11) ; Ziegler et collègues (`2205.01663v5`, p. 4) ; MART (`2311.07689v1`, p. 1) | PDF |
| K1+K3 | **oui** | Bailey et collègues : plus de 70 tours alternés, l'attaquant optimise des activations obscurcies, le défenseur réentraîne une sonde sur les activations de toutes les attaques précédentes (`2412.09565v2`, p. 3, 11–13) | PDF |
| K1+K4 | **oui, fréquent** | MAGIC, attaques non vues PAIR, TAP, GCG, AutoDAN (`2602.01539v2`, p. 9–10) ; AgentSafeEvo, quatre bancs tiers (p. 8) ; EvoSafety, méthode d'attaque jamais vue et bibliothèque tenue à l'écart (p. 7–8) ; RvB, quatre bancs externes (p. 7–8) ; Self-RedTeam, 14 bancs (p. 1, 6) ; DuoGuard, six bancs (`2502.05163v2`, p. 1–2) ; EvoDefense (`2605.31140v1`, p. 6–8) ; Digital Red Queen, guerriers humains tenus à l'écart (`2601.03335v1`, p. 1, 5–6) | PDF |
| K1+K5 | **non trouvée** | Seules des garanties d'une autre nature : sécurité garantie *si* l'équilibre est atteint (Self-RedTeam p. 1–3 ; MAGIC p. 4) ; convergence vers l'équilibre (DuoGuard p. 1–2) ; archive à progrès monotone (de Jong 2004, p. 1–2) | PDF (absence dans les lus) |
| K2+K3 | **oui** | Casper et collègues (`2403.05030v6`, p. 4–5) ; Sheshadri et collègues (`2407.15549v3`, p. 3–4) ; Bailey et collègues (p. 11–13) ; Chaudhary et Barez (`2505.14300v2`, p. 2–3) | PDF |
| K2+K4 | **oui, fréquent** | Casper et collègues (p. 6–7, 9) ; Sheshadri et collègues (p. 5–6) ; Dai, Mahloujifar et Mittal 2022 (`2204.13779v3`, p. 1–2, 7) ; Dai et collègues 2025 (`2502.04248v1`, p. 1–3, 6) ; Adversarial Déjà Vu, défense nourrie des « compétences » extraites de 32 articles d'attaque et testée sur les attaques publiées après une date de coupure (`2510.21910v3`, p. 1–2) ; Constitutional Classifiers (`2501.18837v1`, p. 1–3, 7, 10–11) ; Storf et collègues (`2603.00829v2`, p. 1–2) | PDF |
| K2+K5 | **oui** | Cohen et collègues (`1902.02918v2`, p. 1) ; Wong et Kolter (`1711.00851v3`, p. 1) ; au niveau des lois : Gao et collègues, détecteur minimax quasi optimal sur des ensembles d'incertitude déclarés (`1805.10611v1`, p. 1), Barni et Tondi, jeu de test d'hypothèses (`1304.2172v1`, p. 1) | PDF |
| K3+K4 | **oui** | Casper ; Sheshadri ; Chaudhary et Barez (bancs MAD et Sleeper Agents, p. 2–3) ; MechAudit-40, 40 mécanismes d'attaque publiés avec exclusion complète (`2609.06612v1`, p. 1–2) ; Constitutional Classifiers++ (`2601.04603v1`, p. 1–2, 4) ; sondes de Gemini (`2601.11516v4`, p. 1–3) | PDF |
| K3+K5 | **non trouvée** | Indices non lus sur PDF : « Feature-Space Smoothing » (arXiv 2601.16200, résumé seulement : certificat sur la similarité des traits sous perturbation de l'*entrée*) ; projet « Verifiably Robust Conformal Probes » du King's College de Londres (offre d'emploi, aucune publication trouvée) | question ouverte |
| K4+K5 | **non trouvée au sens strict** | Une borne (pas un certificat) sur le passage d'une classe source à une classe cible, évaluée sur des attaques de tiers (Dai et collègues 2022, p. 1–2, 7) ; un théorème analogue avec attaques tenues à l'écart (Dai et collègues 2025, p. 3, 6) | PDF |
| **K1+K2+K3** | **oui** | Bailey et collègues, section 3.5 (p. 11–13) ; K2 au sens « échantillons » (activations de toutes les attaques passées), la recette de l'attaque restant fixe | PDF |
| **K2+K3+K4** | **oui** | Casper et collègues (p. 1–2, 6–7, 9 : 18 attaques de Kaufmann et collègues tenues hors de l'entraînement) ; Sheshadri et collègues (p. 1, 5–6) ; Chaudhary et Barez (p. 2–3) | PDF |
| **K1+K2+K4** | **oui avec K2[é]** ; **non trouvée avec K2[p]** | Avec échantillons : MAGIC, AgentSafeEvo, EvoSafety, RvB, Self-RedTeam, EvoDefense (pages ci-dessus). Avec paramètres ou recettes : Dalvi 2004 et Terekhov 2026 n'ont pas K4 ; Adversarial Déjà Vu n'a pas K1 ; Dai et collègues 2025 n'ont K1 qu'au sens d'une suite d'attaques non adaptatives | PDF |
| K1+K3+K4 | **non trouvée** | Le jeu itéré de Bailey et collègues n'est pas évalué sur des familles de tiers ; leur table 1 (p. 42) porte sur des sondes non réentraînées | PDF (absence dans les lus) |
| Tout triplet contenant K5 | **non trouvé** | Plus proches : Dai et collègues 2022 (K2[c]+K4+K5[g]) ; Gao et collègues et Barni et Tondi (K2[c]+K3[l]+K5[g], sans coévolution) | PDF |
| En contrôle : K1+K2[p]+C4+C5+C6 | **oui** | Terekhov, Gulcehre, Hebbar et Benton 2026 : jeu de Stackelberg à somme nulle (p. 3), algorithme itératif de point-selle « selon le paradigme de l'entraînement adverse » contre une base croissante d'attaques, avec des invites bénignes témoins et la vérification que les anciennes attaques ne réapparaissent pas (p. 6–7, 25–28), dix cycles (p. 28) | PDF |
| En contrôle : K1+C5+K4[m] | **oui** | Async Control : trois tours, la défense reçoit les épisodes mais pas les invites de l'attaque, l'attaque joue en dernier ; environnement tenu à l'écart et environnements hors distribution conçus par les mêmes auteurs (`2512.13526v1`, p. 1–5, 8–9) | PDF |
| Au niveau des lois : K1+K3[l] | **oui, hors sûreté** | Réseaux génératifs adverses (`1406.2661v1`, p. 1) ; Lipizzaner, coévolution de populations de générateurs et de discriminateurs (`1811.12843v1`, p. 1) | PDF |
| Quatre composantes K ou plus | **non trouvée** | — | PDF lus et citants examinés |

### 1.2 Ce que cela veut dire pour la phrase du directeur

« Existent séparément » : vrai. « Jamais réunies » : **faux** pour K1+K2, K1+K3, K1+K4, K2+K3, K2+K4, K2+K5, K3+K4 et pour les triplets K1+K2+K3 et K2+K3+K4 ; faux aussi pour l'arène coévolutive en contrôle avec défense informée des recettes (Terekhov et collègues 2026). **Vrai, au niveau de ce qui a été lu**, pour la combinaison complète, pour tout assemblage contenant un certificat (K5) avec K1 ou K3, et pour K1+K3+K4.

Lecture R8 de ces absences, à vérifier plus durement parce que la zone est séduisante :

1. **Le certificat n'existe que pour des classes simples** : boules de norme (Cohen et collègues p. 1 ; Wong et Kolter p. 1) ou boules de lois (Gao et collègues p. 1). Au niveau des lois sur activations synthétiques visé par P-041, la « barrière minimax sur la classe déclarée » est un problème de test d'hypothèses robuste déjà traité (Gao et collègues p. 1 ; Barni et Tondi p. 1 ; Huber 1965 non lu). La nouveauté éventuelle serait l'assemblage, pas la barrière.
2. **Le champ du contrôle s'interdit délibérément l'« avantage du terrain » à la défense.** L'attaque joue en second et connaît le protocole (Terekhov, Panfilov et collègues, `2510.09462v2`, p. 1, 3, 10 : « l'attaquant joue en second et s'adapte ») ; Async Control laisse l'attaque jouer en dernier (p. 2, 5) et range l'amélioration itérative de la défense parmi les raisons de **surestimer** la défense (p. 13) ; Ctrl-Z accorde un dernier pas d'optimisation à l'attaque avant l'évaluation finale (`2504.10374v1`, p. 4). Dans les jeux de sécurité de la lignée de Tambe, l'avantage du défenseur est l'engagement (il joue en premier, l'attaquant l'observe) (`1401.3888v1`, p. 1–2), pas l'information. Une défense qui joue en second et informée n'est donc pas un trou : c'est une structure d'information que le champ évite pour garder une estimation prudente. P-041 la compense par des familles tenues à l'écart, mais ces familles sont fixes, non adaptatives à la barrière finale.
3. **La mesure sur familles de tiers est déjà la norme** dans les articles de coévolution en sûreté des grands modèles de langage (ligne K1+K4). Ce qui n'a pas été trouvé, c'est le protocole propre au programme : familles conçues par des instances de fournisseurs différents, scellées avant la boucle et lues une seule fois. C'est une discipline de procédure, pas une composante scientifique revendicable en soi.

## 2. Corrections et réserves sur ce que le dépôt affirme

1. **SafeCoEvo n'est pas une coévolution attaque–défense.** Sa « coévolution » unit deux composants de *défense*, un harnais de sûreté et un garde, sur un flux de déploiement ; aucun attaquant n'évolue (`2609.36580v2`, p. 1–4, 9). La liste d'occupants du préambule de P-041 (« Zone occupée … »), reprise dans la ligne P-041 de `registres/decisions.md`, et la réponse d'Argon à la question-mère v3 (« occupants … SafeCoEvo, AgentSafeEvo, EvoSafety [VÉRIFIÉ, Pièce C § 2] ») sont à corriger sur ce point.
2. **« Terekhov et collègues » désigne deux articles distincts.** La coévolution rouge–bleue (base croissante d'attaques, point-selle) est dans `2606.08892v2` (contrôle diffus, p. 6–7, 25–28) ; `2510.09462v2` étudie une attaque adaptative selon le principe de Kerckhoffs, sans coévolution (p. 1–3, 10).
3. **EvoSafety** est le nom du cadre de `2605.13411v1`, intitulé « Model-Agnostic Lifelong LLM Safety via Externalized Attack-Defense Co-Evolution » (p. 1). La défense n'y reçoit que des attaques passées (une banque de mémoire), pas les compétences de l'attaque (p. 6).
4. **Signe du transfert hors classe (P-041, section 1, point 6).** P-041 cite « Kang et collègues 2019 » pour « l'entraînement adverse contre un modèle de menace transfère mal à un autre ». Le PDF v4 de cet article (Kaufmann, Kang, Sun et collègues) écrit que l'entraînement adverse en norme Lp *augmente* la robustesse aux attaques imprévues, tout en restant distinct de la robustesse Lp (`1908.08016v4`, p. 8). Tramèr et Boneh soutiennent la formulation de P-041 : aucune garantie hors du type entraîné, et parfois une vulnérabilité accrue (`1904.13000v2`, p. 1). Casper et collègues trouvent que l'entraînement adverse en norme Lp rend la plupart des points de contrôle plus vulnérables aux attaques de Kaufmann et collègues (`2403.05030v6`, p. 7, 9). Le signe publié est donc **mitigé** ; la citation de Kang et collègues à l'appui de « transfère mal » est inexacte sur le PDF v4.
5. **L'hypothèse « défense héritée moins bonne qu'une défense repartie de zéro »** a un antécédent direct hors coévolution. Dai, Cianfarani et collègues comparent l'ajustement continu d'une défense à mesure qu'arrivent de nouvelles attaques avec un réentraînement de zéro. Sur CIFAR-10, l'ajustement régularisé fait mieux ; sur ImageNette et CIFAR-100, le départ de zéro fait mieux. La régularisation améliore aussi la robustesse aux attaques tenues à l'écart (`2502.04248v1`, p. 6). L'« oubli coévolutif » est une pathologie répertoriée (`2004.04647v1`, p. 9). La réserve d'antériorité de P-041 sur cette hypothèse se confirme : la zone est partiellement occupée.
6. **Trois des quatre bases de P-041 existent déjà chez les occupants.** « Défense évoluant seule contre un attaquant figé » : MAGIC « Defender-only » (p. 12), AgentSafeEvo « Static-AT » (p. 7, 10), Self-RedTeam « Defender-Only » (p. 2). « Redémarrage à budget égal » : Dai et collègues 2025 (p. 6). « Barrière théorique sans évolution » : non trouvée comme base dans un article coévolutif.
7. **Les diagnostics de pathologies sont déjà employés.** Évaluation croisée des générations d'attaquants et de défenseurs (MAGIC p. 10–11 ; AgentSafeEvo p. 9) ; efficacité de chaque garde contre les attaques de tous les tours passés (RvB p. 7) ; dernière sonde contre les attaques de tous les tours (Bailey et collègues p. 13) ; transfert aux moniteurs des tours précédents (Async Control p. 2). Pathologies observées : oscillation sans équilibre (Dalvi et collègues p. 9), dégradation après plusieurs itérations (R-Zero p. 7), effondrement (SPIRAL p. 3, 8–9), effondrement de la diversité de l'attaquant (`2606.09701v2`, p. 1), effondrement de mode dans la génération d'attaques (`2605.09684v1`, p. 1).
8. **Dates des classiques non lus.** Rosin et Belew est daté de 1996 dans `1506.05082v2` (p. 3) et de 1997 dans `2108.03156v1` (p. 2) et chez Nolfi et Pagliuca (p. 2–3). Ce sont des transcriptions secondaires, non opposables (R7) ; le PDF de 1997 n'a pas pu être téléchargé (section 7).
9. **« Barrière universelle » et vocabulaire.** Aucun occupant ne revendique une barrière certifiée universelle. « Universel » qualifie l'attaque chez les Constitutional Classifiers (« universal jailbreaks », `2501.18837v1`, p. 1) ; Madry et collègues parlent de modèles « en un certain sens, universels » contre une classe d'adversaires du premier ordre (`1706.06083v4`, p. 1). Ces sens sont à distinguer de celui de P-041.

## 3. Par composante : travaux les plus proches

**C1 — défense coévolutive contre attaques évolutives.**
- Occupants vérifiés (attaque et défense coévoluent) : MAGIC (p. 1, 4–7) ; AgentSafeEvo (p. 1–7) ; EvoSafety (p. 1–7) ; RvB, jeu itéré sans entraînement, la défense ne voit que les journaux d'attaque (p. 1–6, 13) ; Self-RedTeam (p. 1–3) ; DuoGuard (générateur contre *classifieur*, p. 1–5) ; CEMMA (générations, archive, p. 1–4) ; MART (p. 1) ; Ziegler et collègues (trois tours, p. 4) ; « Learning to Attack and Defend » (p. 1) ; ACEA (tours avec indications, p. 1) ; EvoDefense (coévolution faible, p. 1–8).
- En contrôle : Terekhov et collègues 2026 (`2606.08892v2`) et Async Control. Hors des grands modèles de langage : coévolution attaque–défense en cybersécurité (O'Reilly et collègues, `2004.04647v1`, p. 1, 8–10, 12) ; classification adverse en jeu répété (Dalvi et collègues 2004).
- Ce qu'ils ne réunissent pas : aucun n'attaque au niveau des lois sur activations ; aucun ne donne de certificat ; la défense voit des échantillons, sauf Dalvi (paramètres) et Terekhov 2026 (invites rouges).
- Non-occupant : SafeCoEvo (voir la section 2).

**C2 — défense informée.**
- Point-selle min-max sur une classe déclarée (Madry et collègues p. 1–2) ; certificats (Cohen et collègues p. 1 ; Wong et Kolter p. 1) ; attaques adaptatives (Tramèr et collègues 2020, p. 1 : elles « ne peuvent pas être automatisées ») ; transfert hors classe (Tramèr et Boneh p. 1 ; Kaufmann et collègues p. 1, 8 ; Dai et collègues 2022, borne source → cible, p. 1–2, 7).
- Défense informée des *recettes* de familles : Adversarial Déjà Vu (p. 1–2) ; Terekhov 2026 (p. 25, 28). Information complète sur les paramètres : Dalvi et collègues (p. 3–4). Jeux de prédiction : Brückner et collègues (p. 1).

**C3 — attaque dans l'espace des activations.**
- Défense informée : entraînement adverse latent (Casper et collègues ; Sheshadri et collègues) ; réentraînement itéré des sondes (Bailey et collègues p. 11–13) ; entraînement du modèle contre une sonde figée (Bailey et collègues p. 25) ; ensemble de détecteurs conçu d'après l'analyse des attaques (Chaudhary et Barez p. 2–3, 8).
- Attaque seule : Neural Chameleons (p. 1–2) ; RL-Obfuscation (p. 1, 3–5).
- Au niveau des lois : VOS, valeurs aberrantes synthétiques dans l'espace des traits pour entraîner un détecteur, sans adversaire (p. 1–2, 6) ; réseaux génératifs adverses et Lipizzaner (p. 1).
- Ne réunissent pas : la notion de « familles paramétrées de lois sur activations », la coévolution et la mesure sur familles de tiers.

**C4 — pathologies et remèdes coévolutifs.**
- Sur PDF : de Jong 2004 (archive à progrès monotone ; le concept de solution doit être choisi d'abord, p. 1–2) ; Yo et de Jong (p. 1) ; Nolfi et Pagliuca 2025 (progrès local, historique et global ; le progrès global s'estime contre des adversaires issus d'expériences indépendantes ; courbes courant contre ancêtres ; tournoi maître ; essais croisés, p. 1–3) ; Alcaraz-Herrera et Cartlidge (cyclage, surspécialisation, désengagement et leurs causes ; archives, p. 1–3) ; O'Reilly et collègues (p. 9) ; Casas (source secondaire, p. 3–4).
- Les primaires de 1995–2012 ne sont **pas lus** (section 7). Les remèdes que P-041 propose de préenregistrer (archive, tournoi maître, courant contre ancêtres, Pareto) sont standard.

**C5 — contrôle.** Greenblatt et collègues 2023 : itération rouge–bleu sur le même ensemble de problèmes, sans séparation entraînement/validation, ce que les auteurs signalent comme risque de surajustement (p. 6) ; ils appellent une validation tenue à l'écart (p. 17). Ctrl-Z (p. 2, 4) ; protocoles de lisibilité (p. 3) ; Async Control ; MonitoringBench (p. 1–3) ; Pinto 2026 sur le transfert entre lignées (p. 1) ; RSI Control (p. 1). ControlArena n'a pas d'article (non lu).

**C6 — Stackelberg et avantage du défenseur.** Korzhyk et collègues (p. 1–3, 6) ; « Games for AI Control », meneur–suiveur où le bleu mène (p. 1, 4–5) ; Terekhov 2026, Stackelberg à somme nulle (p. 3) ; Wang 2019, double oracle (p. 1–2) ; MAGIC, équilibre parfait en sous-jeux (p. 4) ; Self-RedTeam, somme nulle (p. 1–3) ; DuoGuard, minimax et convergence (p. 1–5). Tambe 2011 n'est **pas lu** (livre).

**C7 — auto-jeu de grands modèles de langage.** Absolute Zero (p. 1, 3) ; R-Zero (p. 1, 7) ; SPIRAL (p. 1, 3, 8–9) ; Digital Red Queen (p. 1–2, 4–6), le seul de ce groupe qui mesure la généralité contre des adversaires conçus par des tiers (guerriers humains).

**C8 — familles de tiers et mesure de la boucle.**
- Familles de tiers : voir la ligne K4 de la table 1.1. Kaufmann et collègues (ImageNet-UA, p. 1, 5) ; MechAudit-40 (p. 1–2) ; Adversarial Déjà Vu (coupure temporelle, p. 1–2) ; Constitutional Classifiers (participants externes, p. 2, 7).
- Mesure de la boucle (C8b) :
  - verdicts certifiés de non-régression sur une suite de promotions, même face à un juge adverse (`2609.17560v1`, p. 1–3) ;
  - dérive de l'évaluateur (`2609.32267v1`, p. 1) ;
  - tâches d'épreuve et domaine de méta-évaluation réservés (Hyperagents, p. 6–7) ;
  - vérité vérifiable plutôt que juge (ACEA, p. 1) ;
  - second juge pour écarter le surajustement de l'évaluateur (EvoSafety, p. 8).
- **Non trouvé** : un article coévolutif qui mesure le taux de fausses promotions sur des témoins. Les « invites témoins » de Terekhov 2026 servent de contrainte dans la perte, non de mesure (p. 7, 25).

## 4. Table par travail

Composantes : voir la grille de la section 0. Lecture : « en entier » ; « corps en entier » (annexes par recherche plein texte) ; « pages ciblées » (résumé, méthode, résultats, et recherche plein texte).

| # | Référence | Fichier | Empreinte SHA-256 | Composantes réunies | Pages lues ou citées | Lecture |
|---|---|---|---|---|---|---|
| 1 | Barni et Tondi 2013, « Binary Hypothesis Testing Game with Training Data » (IEEE Transactions on Information Theory, version arXiv) | `1304.2172v1.pdf` | `ddd976363fb41fe353e19d5838ec5d46ccc73b162abea8aa2957cf516bac7598` | K2[c] ; K3[l] ; K5[g] (équilibre asymptotique, région d'indiscernabilité) ; C6 | 1–2 | pages ciblées |
| 2 | Korzhyk, Yin, Kiekintveld, Conitzer et Tambe 2011, « Stackelberg vs. Nash in Security Games » (JAIR 41) | `1401.3888v1.pdf` | `ac99b152327bbb0472fd791cf9b02f0982e891753039f87a09a3b6df2a2f5e2b` | C6 (défenseur meneur qui s'engage, attaquant qui observe) ; K2 non (incertitude bayésienne sur l'attaquant) | 1–3, 6 | pages ciblées |
| 3 | Goodfellow et collègues 2014, « Generative Adversarial Nets » | `1406.2661v1.pdf` | `ff5819e3a7b713c3bd3107b7de3d51fe0a347aa5d8444f0efdcf2345ef0a8b63` | K1 (générateur contre discriminateur, entraînement simultané) ; K3[l] ; C6 (minimax) | 1 | pages ciblées |
| 4 | Casas 2015, « A review of landmark articles in the field of co-evolutionary computing » (rapport, source secondaire) | `1506.05082v2.pdf` | `cb6bd913e2a66d5dc43fa265e2ee6c1e6cd3b4181573c95d03192075c8bf3c7a` | C4 (temple de la renommée, tournoi maître, Pareto, cyclage, perte de gradient : par transcription) | 1–5 | en entier |
| 5 | Madry et collègues 2018, « Towards Deep Learning Models Resistant to Adversarial Attacks » | `1706.06083v4.pdf` | `cbf9bf68f543aa351c3ea6aac7b159d58860b0993df2f9b8f938d8594b2601e1` | K2[c] (point-selle min-max sur une classe d'adversaires bien définie) | 1–2 | pages ciblées |
| 6 | Wong et Kolter 2018, « Provable Defenses against Adversarial Examples via the Convex Outer Adversarial Polytope » | `1711.00851v3.pdf` | `2ca0b1bb96a4726ead00d8ff494a7da630c6ecefd44abe01f699cc9570d312dd` | K2[c] ; K5 (garantie prouvée sur une boule de norme ; détection garantie de tout exemple adverse de la classe) | 1 | pages ciblées |
| 7 | Gao, Xie, Xie et Xu 2018, « Robust Hypothesis Testing Using Wasserstein Uncertainty Sets » (NeurIPS) | `1805.10611v1.pdf` | `0298e446546550b6072c6551a1523a3e1004c1f5938b72ab12093f357957cedf` | K2[c] ; K3[l] ; K5[g] (détecteur minimax quasi optimal sur des ensembles d'incertitude déclarés) | 1 | pages ciblées |
| 8 | Schmiedlechner, Ng Zhi Yong, Al-Dujaili, Hemberg et O'Reilly 2018, « Lipizzaner » | `1811.12843v1.pdf` | `fc2eb44391fe9aa62346f6d430165dbc042a5e4721de7571e46f621247ecc426` | K1 (populations de générateurs et de discriminateurs) ; K3[l] ; C4 (robuste aux effondrements) | 1 | pages ciblées |
| 9 | Cohen, Rosenfeld et Kolter 2019, « Certified Adversarial Robustness via Randomized Smoothing » | `1902.02918v2.pdf` | `a03d92f572f076e35e8edf84471580805acf2f422e0736e29828798f5d3bb995` | K5 (certificat en norme L2) | 1 | pages ciblées |
| 10 | Tramèr et Boneh 2019, « Adversarial Training and Robustness for Multiple Perturbations » | `1904.13000v2.pdf` | `b45f282a1233335d0e1ee466468efd5d1ffba8e17778781219fefedf0d8b7209` | K2[c] (plusieurs types de perturbation) ; hors classe : aucune garantie, compromis démontré | 1 | pages ciblées |
| 11 | Yo et de Jong, « A Comparison of Evaluation Methods in Coevolution » (arXiv 2019) | `1905.08723v1.pdf` | `4c282c5e7de6e5b2f57baf75f56578baf6dc786bd4d3e05fbbd11a3897d8fcf2` | C4 (le concept de solution d'abord ; méthodes d'évaluation) | 1 | pages ciblées |
| 12 | Kaufmann, Kang, Sun et collègues, « Testing Robustness Against Unforeseen Adversaries » (v4 2023 ; v1 Kang et collègues 2019) | `1908.08016v4.pdf` | `492d821182a8bfc7ba9c2844d0b158ef235a1b86be292b22f1846e12d1d7bcd4` | K4 (attaques imprévues, ImageNet-UA) ; K2[c] évalué | 1, 5, 8 | pages ciblées |
| 13 | Tramèr, Carlini, Brendel et Madry 2020, « On Adaptive Attacks to Adversarial Example Defenses » | `2002.08347v2.pdf` | `b52d176d8d47f876d35fbbca0ad8576e3256af8ee0754360c02c9028968b2983` | K2 côté attaque (attaques adaptatives, non automatisables) | 1 | pages ciblées |
| 14 | O'Reilly, Toutouh, Pertierra et collègues 2020, « Adversarial Genetic Programming for Cyber Security » | `2004.04647v1.pdf` | `3369fcf605299317c565e32acba5a7855f2a51b80cec4ad46279f5ef1eea48c4` | K1 (coévolution attaque–défense en cybersécurité) ; C4 (pathologies, remèdes, concepts de solution) | 1, 8–10, 12 | pages ciblées |
| 15 | Alcaraz-Herrera et Cartlidge 2021, « Substitution of the Fittest » (ECTA) | `2108.03156v1.pdf` | `c090b4d7b0f6d79473272b915c855b21c915c613305de76292857043dfac9363` | C4 (cyclage, surspécialisation, désengagement, causes ; archives ; archive de Pareto appliquée à la coévolution attaque–défense de réseaux, citée) | 1–9 | en entier |
| 16 | Du, Wang, Cai et Li 2022, « VOS: Learning What You Don't Know by Virtual Outlier Synthesis » (ICLR) | `2202.01197v4.pdf` | `92e6a874f9946e8e4cb465057c593393da250f4502123a113cac2323b6c9c557` | K3[l] (valeurs aberrantes synthétiques dans l'espace des traits, non adverses) ; K2 ; K4 au sens de données hors distribution publiques | 1–2, 6 | pages ciblées |
| 17 | Dai, Mahloujifar et Mittal 2022, « Formulating Robustness Against Unforeseen Attacks » (NeurIPS) | `2204.13779v3.pdf` | `fc4864b03e1a9b1f7bcf62433de2934edac4cb80eab4298a3240305173fd6b82` | K2[c] (modèle de menace source) ; K4 (cibles StAdv, Recolor, conçues par d'autres) ; K5[g] (borne sur l'écart source → cible) | 1–3, 7 | pages ciblées |
| 18 | Ziegler et collègues 2022, « Adversarial training for high-stakes reliability » (NeurIPS) | `2205.01663v5.pdf` | `acdc30e4cd2cfcc0fe7a13ca67fe51c4fd42ada52a8cee86267eb3bb535f4b49` | K1 (trois tours) ; K2[é] ; K4[m] (prestataires humains) | 1–4 | pages ciblées |
| 19 | Ge et collègues 2023, « MART: Improving LLM Safety with Multi-round Automatic Red-Teaming » | `2311.07689v1.pdf` | `ccb4158b60bd3c0d5ee9963cfa610dd27f3a1bcf41758a37d29bd09058c151df` | K1 (quatre tours) ; K2[é] | 1 | pages ciblées |
| 20 | Greenblatt, Shlegeris, Sachan et Roger 2023, « AI Control: Improving Safety Despite Intentional Subversion » | `2312.06942v5.pdf` | `999f7a92bb8c085799e68f3d88f491ad8a334f862ccf5b286e5c2766677864c0` | C5 ; itération rouge–bleu sans séparation entraînement/validation (reconnu p. 6) ; validation tenue à l'écart demandée (p. 17) | 5–6, 17 | pages ciblées |
| 21 | Samvelyan et collègues 2024, « Rainbow Teaming » | `2402.16822v3.pdf` | `48c8c7d9e4c93ddeb9e643941721d76eebd93751b70a45614f9887dea4f3f277` | C4 (archive qualité-diversité) ; données synthétiques pour la robustesse | 1–2 | pages ciblées |
| 22 | Casper, Schulze, Patel et Hadfield-Menell 2024/2025, « Defending Against Unforeseen Failure Modes with Latent Adversarial Training » (TMLR) | `2403.05030v6.pdf` | `46ad7a229298459cfd5ba4f70dd1fb76e9d2aea94b0ce8e5730b94909d84af93` | K2[c] ; K3 ; K4 (18 attaques de Kaufmann et collègues ; exemples humains de Ziegler et collègues) | 1–10 | corps en entier |
| 23 | Sheshadri et collègues 2024/2025, « Latent Adversarial Training Improves Robustness to Persistent Harmful Behaviors in LLMs » (TMLR) | `2407.15549v3.pdf` | `8297b3c9986e0851aa30fda56fd71a98bf1763c4754876cff20a0e5b0f6d2182` | K2[c] ; K3 ; K4 (PAIR, préremplissage, AutoPrompt, GCG, many-shot) | 1–6 | pages ciblées |
| 24 | Griffin, Thomson, Shlegeris et Abate, « Games for AI Control » (v2 2026) | `2409.07985v2.pdf` | `698f0db6e87bd78689c122afe5cb60dd7795e6aec38ae730ce4725781b6d9871` | C5 ; C6 (meneur–suiveur, équilibre de Stackelberg multi-objectif) | 1, 4–5 | pages ciblées |
| 25 | Bailey, Serrano, Sheshadri et collègues 2024/2025, « Obfuscated Activations Bypass LLM Latent-Space Defenses » | `2412.09565v2.pdf` | `9c23a613c5c7e3a213a60eca7cb990b4b7d6e0510db30584736aa021dfb944e9` | K1 (plus de 70 tours alternés) ; K2[é] (toutes les activations des attaques précédentes) ; K3 ; C4 (archive, évaluation contre tous les tours passés) | 1–3, 11–14, 25, 27–29, 42 | pages ciblées |
| 26 | Sharma et collègues 2025, « Constitutional Classifiers » | `2501.18837v1.pdf` | `9eeb537ebf4bf47a76284f5c82fe37c6c71f5ca57d93dedc7a9a269beb3c1a7e` | K2[c] (constitution = classe déclarée) ; K4 (405 participants externes ; 5 681 tentatives tenues à l'écart) | 1–3, 7, 10–11 | pages ciblées |
| 27 | Dai, Cianfarani, Bhagoji, Sehwag et Mittal 2025, « Adapting to Evolving Adversaries with Regularized Continual Robust Training » | `2502.04248v1.pdf` | `2dfd052dea60c7e5903ab41c7f919c2dd6e95efc2208bbd09bd17a5b57f452cb` | K1 partiel (suite d'attaques nouvelles, attaquant non adaptatif) ; K2[c] ; K4 ; K5[g] (théorème 3.1) ; héritage contre départ de zéro | 1–3, 6 | pages ciblées |
| 28 | Deng, Yang, Zhang, Wang et Li, « DuoGuard » (AISTATS 2026) | `2502.05163v2.pdf` | `101d05bbd6e190cd6f62b2a1c953f8208050742d0129033b06163f09e010f7fe` | K1 (générateur contre classifieur) ; C6 (minimax, convergence vers l'équilibre de Nash) ; K4 (six bancs) | 1–2, 4–5 | pages ciblées |
| 29 | Bhatt et collègues 2025, « Ctrl-Z: Controlling AI Agents via Resampling » | `2504.10374v1.pdf` | `5f802d679344fe5e15d1edd50e96245f3bdc054e69d1ff0880b077d173549211` | K1 (itératif, équipes non cloisonnées, dernier pas à l'attaque) ; C5 | 2, 4 | pages ciblées |
| 30 | Zhao et collègues 2025, « Absolute Zero » | `2505.03335v3.pdf` | `6217ccee964c70e42fba116004ae23400c11d2ecc687c37aed062c3689098e18` | C7 (proposeur–résolveur) ; alerte de sûreté | 1, 3 | pages ciblées |
| 31 | Chaudhary et Barez, « Beyond Black-Box Obfuscation » (COLM 2026) | `2505.14300v2.pdf` | `01dc8a2a0ab0760dd3cd900640cada1ae33f297e9941e344ee5dd69276cb9462` | K2 (défense conçue d'après l'analyse des attaques) ; K3 ; K4 (MAD, Sleeper Agents) | 1–3, 8 | pages ciblées |
| 32 | Liu, Jiang, Liang et collègues, « Chasing Moving Targets… » (Self-RedTeam, ICML 2026) | `2506.07468v4.pdf` | `5b91f47742db1900e60b982046cbce5e08cdd6e561073468037f69af171d15b6` | K1 ; K2[é] ; C6 (somme nulle, garantie à l'équilibre) ; C7 ; K4 (14 bancs) | 1–3, 6 | pages ciblées |
| 33 | Gupta et Jenner, « RL-Obfuscation » (v4 2026) | `2506.14261v4.pdf` | `4b0960622664e77d888974955b29f9c0e5913266392caeecac2b844f011e244c` | K3 (attaque) ; K4 côté attaque (moniteurs non vus) | 1, 3–5 | pages ciblées |
| 34 | Liu, Yu, Liu et collègues, « SPIRAL » (ICLR 2026) | `2506.24119v3.pdf` | `800adadf52c98736517c362e18cb1786d48538c2f53c6ec2391fd3763e01e610` | C7 (auto-jeu à somme nulle) ; C4 (effondrement) | 1, 3, 8–9 | pages ciblées |
| 35 | Huang et collègues, « R-Zero » (ICLR 2026) | `2508.05004v4.pdf` | `5e577e627e4d6501544955922257313ca2cd94fbc3c7715cfa0dd200cfe9d139` | C7 (challenger–résolveur) ; C4 (dégradation après plusieurs itérations) | 1, 7 | pages ciblées |
| 36 | Terekhov, Panfilov, Dzenhaliou et collègues, « Adaptive Attacks on Trusted Monitors Subvert AI Control Protocols » (v2 2026) | `2510.09462v2.pdf` | `96c16e33b27b9633b324acecfe29e1bfa9de7052143fb854824aad70a649d7f7` | C5 ; attaque en second selon Kerckhoffs ; pas de coévolution | 1–3, 8–10 | pages ciblées |
| 37 | Dabas et collègues, « Adversarial Déjà Vu » (ICLR 2026) | `2510.21910v3.pdf` | `f5897a3e972bd25bbf8ec4503aa097a10e7af29d4cc31c98ca3faa7c396bbc86` | K2[p] (compétences extraites de 32 articles d'attaque) ; K4 (coupure temporelle : attaques postérieures) | 1–2 | pages ciblées |
| 38 | McGuinness, Serrano, Bailey et Emmons 2025, « Neural Chameleons » | `2512.11949v1.pdf` | `e0f8ddfff6e75d835995886a630a5d077ed871c28599f710b41c96efc949e3ee` | K3 (attaque) ; K4 côté attaque (moniteurs non vus) | 1–2 | pages ciblées |
| 39 | Cooper Stickland, Michelfeit et collègues 2025, « Async Control » (institut britannique de sûreté de l'intelligence artificielle) | `2512.13526v1.pdf` | `bcbce5108d56d8c0399527c65588b52e2931931df9157a5b79498de635586368` | K1 (trois tours) ; K2 refusé explicitement (épisodes sans les invites ; l'attaque joue en dernier) ; C5 ; K4[m] ; C4 (transfert aux moniteurs précédents) | 1–15 | corps en entier |
| 40 | Kumar, Bahlous-Boldi, Sharma, Isola, Risi, Tang et Ha 2026, « Digital Red Queen » | `2601.03335v1.pdf` | `30a5dc45af4f16a8675cf4a2629bd23d5c475bea7acbba890a16e16745ae1d70` | K1 ; C4 (historique, évite le cyclage) ; C7 ; K4 (guerriers humains tenus à l'écart) | 1–2, 4–6 | pages ciblées |
| 41 | Cunningham, Wei et collègues 2026, « Constitutional Classifiers++ » | `2601.04603v1.pdf` | `ba8ec6570a41c42554ac89b9869020a2356cead5bdcf2618fc9c6208a89afdb5` | K2[c] ; K3[d] (sondes linéaires) ; K4 (plus de 1 700 heures d'équipes rouges) | 1–2, 4 | pages ciblées |
| 42 | Kramár, Engels et collègues 2026, « Building Production-Ready Probes For Gemini » | `2601.11516v4.pdf` | `c4a36db54c9d679a718a0e35b9cad09fa628d81f6174bb6e1d8c6b26a063d8bf` | K3[d] ; recherche évolutive (AlphaEvolve) de sondes et d'attaques, séparément ; K4 (évasions préexistantes) | 1–3, 8–12 | pages ciblées |
| 43 | Huang, Yan, Liu et collègues 2026, « RvB: Automating AI System Hardening via Iterative Red-Blue Games » | `2601.19726v1.pdf` | `53a465a479fc1887e724b424a749910eb09251be49c966a5a639c65d890e7e44` | K1 ; K2[é] ; K4 (quatre bancs externes) ; C4 (efficacité inter-tours, pas d'oubli) | 1–15 | en entier |
| 44 | Wen, He, Qi et collègues 2026, « MAGIC » | `2602.01539v2.pdf` | `793d32725d82e364f0ecbb0be994694d2aca20f8daf8391e6583be58f067540e` | K1 ; K2[é] ; C6 (équilibre parfait en sous-jeux) ; K4 (PAIR, TAP, GCG, AutoDAN) ; C4 (évaluation croisée) ; base « défense seule » | 1–12 | corps en entier |
| 45 | Sreevatsa, Prasanna et collègues 2026, « Basic Legibility Protocols Improve Trusted Monitoring » | `2602.10153v1.pdf` | `f66620e8c00d705e2d1cf4aa2e55e7e925f036e7c7007847bf29a269dc10dc3b` | K1 (optimisation itérative rouge et bleue) ; C5 | 3 | pages ciblées |
| 46 | Storf, Barton-Cooper, Peters-Gill et Hobbhahn 2026, « Constitutional Black-Box Monitoring for Scheming in LLM Agents » | `2603.00829v2.pdf` | `d8ffcbd352abd9c6bd9aeb1ded6d337689ae980980960fdd8de12bd3d1fd775d` | K2[c] (spécifications → données synthétiques) ; K4 (7 500 trajectoires ControlArena) ; C5 | 1–2 | pages ciblées |
| 47 | Shi, Wang, Yang, Wang et Chang 2026, « CEMMA » | `2603.01784v1.pdf` | `bc4a3212aebce517ed7d91716e64eb72777655b72b615008b14a26e45c5c1ead` | K1 (générations) ; C4 (archive évolutive) ; K4 partiel | 1–4 | pages ciblées |
| 48 | Zhang, Zhao, Yang et collègues 2026, « Hyperagents » | `2603.19461v1.pdf` | `92f9a73b43699c08c6000f7d4f1b68bec9fd872d217467fe4a1127e2f7981f1e` | C8b (tâches d'épreuve tenues à l'écart, domaine réservé de méta-évaluation) ; archive | 1–2, 5–7 | pages ciblées |
| 49 | Jotautaitė, Martinez, Matthews et Tracy 2026, « MonitoringBench » | `2605.09684v1.pdf` | `35bb09b49f85578e4cfddeec16c9ae101a51b5d618196a4b29a1722b89b831f5` | C5 ; K4 côté attaque (10 moniteurs tenus à l'écart) ; C4 (effondrement de mode) | 1–3 | pages ciblées |
| 50 | Zhang, Li, Liu et collègues 2026, « Model-Agnostic Lifelong LLM Safety via Externalized Attack-Defense Co-Evolution » (EvoSafety) | `2605.13411v1.pdf` | `a81514c51c33b6f8def74bb6df11c5f733cfe256bbc21768f607a3dc0e0029c0` | K1 ; K2[é] ; C4 partiel (bibliothèque et banque externes) ; K4 ; C8b partiel (second juge) | 1–11 | corps en entier |
| 51 | Li, Hou, Wei, Guo et Lu 2026, « EvoDefense » | `2605.31140v1.pdf` | `29c8ffd960d8ece9df75eb95329afc23509729e904819dbafb5d90d24305367a` | K1 faible ; K2[é] ; K4 | 1–9 | corps en entier |
| 52 | Terekhov, Gulcehre, Hebbar et Benton 2026, « Diffuse AI Control on Fuzzy Tasks » | `2606.08892v2.pdf` | `aea0f2d192f3744f0a5827b2fbb106f5a4b7cd33eee8bde30ea139ba8a09759a` | K1 ; K2[p] (invites et scores de l'équipe rouge) ; C4 (base croissante d'attaques, témoins, Pareto) ; C5 ; C6 (Stackelberg à somme nulle) | 1–10, 25–28 | corps en entier |
| 53 | Bullwinkel, Kim, Minnich et Russinovich 2026, « Learning to Attack and Defend » | `2606.09701v2.pdf` | `f295fe11edb3800e0da7488c4a1eb561e5109b84d9ab4defe473d5145daa7042` | K1 (co-entraînement) ; C4 (effondrement de la diversité de l'attaquant) | 1 | pages ciblées |
| 54 | Pinto 2026, « Calibration-Family Overfit » | `2607.06596v3.pdf` | `63181efe25f4115bdb8652aad12f6bdeade2f9e27f3c61811161e9278b885c8e` | C5 ; K4 (matrice de transfert entre lignées) | 1 | pages ciblées |
| 55 | Guo, Shi, Zhang et Tourani 2026, « MechAudit-40 » | `2609.06612v1.pdf` | `268a0f2ee28987e6c59bd9c291bfb918c5b4ea3bc0e37f9a96435108617bdb89` | K3[d] ; K4 (40 mécanismes publiés, exclusion complète ; adversaires non adaptatifs) | 1–2 | pages ciblées |
| 56 | Shen, Toyoda et Leung 2026, « ACEA » | `2609.08256v1.pdf` | `ebd653ec8563f491336fe5111d387f87ed64aa8d9ba2b9c8a15c5e2906b589d1` | K1 (tours) ; C8b (vérité vérifiable plutôt que juge) | 1 | pages ciblées |
| 57 | Balachandran 2026, « Pay Only for Disagreement » | `2609.17560v1.pdf` | `ef318a961de7d5f237b7bdca063b7441d3cab00522bc0e6baec383603af2d11f` | C8b (verdicts certifiés de non-régression sur une suite de promotions ; juge adverse admis) | 1–4 | pages ciblées |
| 58 | Mondal, Banik, Apurba et Al Mahmud 2026, « When Can Old Evaluations Certify a New Model? » | `2609.32267v1.pdf` | `8654e1185de1b3160eb4d30d50d5bcf428e41e5439f868fad58ef1849bf1a118` | C8b (dérive de l'évaluateur) | 1 | pages ciblées |
| 59 | Cheng, Hu, Ma et collègues 2026, « SafeCoEvo » | `2609.36580v2.pdf` | `e0df2463da8c5a9aaaa819d79f08606618f3318823a0cc78f9ecbcf940a05d3a` | K1 non (coévolution de deux composants de défense) ; K4 (quatre scénarios non vus) | 1–9 | corps en entier |
| 60 | Wang, Wen, Qi et collègues 2026, « AgentSafeEvo » | `2610.19422v1.pdf` | `4812c7037c4c4363f4fe7ebbcf027e2f286341446dbd503e20bd8a4b72715bac` | K1 ; K2[é] ; K4 (bancs d'agents tiers) ; C4 (évaluation croisée) ; base attaquant figé | 1–11 | corps en entier |
| 61 | Zhou et Sehwag 2026, « RSI Control » | `2610.27735v2.pdf` | `4df85cb0d8be236eabb3d3daccbc3c25ed2192eb63e932335a4bf2dea4bb1078` | C5 (sabotage dans l'amélioration récursive) | 1 | pages ciblées |
| 62 | Brückner, Kanzow et Scheffer 2012, « Static Prediction Games for Adversarial Learning Problems » (JMLR 13) | `Bruckner-Kanzow-Scheffer-2012-static-prediction-games-JMLR.pdf` | `6e7ea7256d52b0919a12dbb11314eac6a6370902b5ce7138f85ada9b7df5f8d1` | C6 (jeu de prédiction, équilibre de Nash) ; K2 | 1 | pages ciblées |
| 63 | Dalvi, Domingos, Mausam, Sanghai et Verma 2004, « Adversarial Classification » (KDD) | `Dalvi-2004-adversarial-classification-KDD.pdf` | `4c2b326adfa4fe72a7598f857ee03af34e26848e258f310416ca21b891a7eb0c` | K1 (jeu répété) ; K2[p] (information complète) ; C6 ; C4 (oscillation sans équilibre) | 1–10 | en entier |
| 64 | Wang 2019, « Adversarial Machine Learning with Double Oracle » (IJCAI, consortium doctoral) | `Wang-2019-adversarial-ML-double-oracle-IJCAI.pdf` | `1bce2f903be0f2cab00d6231e64736a0f78520c8f30fed3555b1622d95137e66` | K1 (double oracle itératif) ; K2[p] (la défense connaît la stratégie mixte de l'attaquant) ; C4 (population, stratégie mixte) ; C6 | 1–2 | en entier |
| 65 | de Jong 2004, « The Incremental Pareto-Coevolution Archive » (GECCO, LNCS 3102) | `deJong-2004-IPCA-GECCO.pdf` | `07e89a1f9dc1cdbc57a5e587daff0dfc730b5326f4a55f690bf73d081e5281bb` | C4 (archive à amélioration monotone ; concept de solution) | 1–2 | pages ciblées |
| 66 | Nolfi et Pagliuca 2025, « Global progress in competitive co-evolution » (Frontiers in Robotics and AI 11) | `frontiers-2024-global-progress-competitive-coevolution.pdf` | `601e3a711ecd73bd76e5cafc736b6ea00505eb851fa79f9c9892fe9afce00b88` | C4 (progrès local, historique, global ; courant contre ancêtres ; tournoi maître ; champions ; essais croisés) | 1–3 | pages ciblées |

## 5. Recherche explicite d'un travail réunissant au moins trois composantes

Requêtes, toutes d'octobre 2026 : coévolution, sondes d'activation et obscurcissement ; équipe rouge et équipe bleue en contrôle avec tours itérés ; entraînement adverse coévolutif avec archive de Pareto ; certificat pour sondes ou moniteurs d'activation ; recherche évolutive de protocoles et de moniteurs ; double oracle en apprentissage adverse ; test d'hypothèses robuste et jeux de détection ; synthèse de valeurs aberrantes dans l'espace des traits ; coévolution de moniteurs et de politiques d'attaque en contrôle ; plus les citations ascendantes (section 6).

Résultat :
- trois triplets trouvés : K1+K2+K3, K2+K3+K4, et K1+K2+K4 au sens « échantillons » ;
- un quintuplet hors K (K1+K2[p]+C4+C5+C6, Terekhov 2026) ;
- aucun quadruplet K ;
- aucun triplet contenant K5.

Le moteur de recherche a deux fois répondu qu'il ne trouvait pas d'article réunissant coévolution, sondes d'activation et réentraînement par générations au-delà de Bailey et collègues. Ces réponses de moteur ne valent que comme indice (R7) ; seule la lecture des PDF ci-dessus est opposable.

## 6. Citations ascendantes

**Méthode.** Interface de programmation de Semantic Scholar, `https://api.semanticscholar.org/graph/v1/paper/arXiv:<id>/citations?fields=title,year,externalIds,abstract&limit=100`, interrogée vers 16:25 UTC avec reprises après refus pour excès de requêtes.

**Cinq travaux sources**, choisis comme les plus proches :

| Source | Citants obtenus |
|---|---|
| Bailey et collègues 2412.09565 | 54 |
| Terekhov et collègues 2606.08892 | 1 (article récent) |
| Casper et collègues 2403.05030 | 96 |
| Async Control 2512.13526 | 22 |
| Dai et collègues 2204.13779 | 13 (la notice de Semantic Scholar paraît partielle) |

Au total, 186 lignes, 181 titres distincts. Les réponses brutes sont restées dans le répertoire de travail de la session, non versées ; leur liste complète est en annexe A.

**Examen.** Les 186 titres ont été lus ; 14 résumés ont été lus dans les métadonnées ; 4 citants ont été téléchargés et lus sur PDF : `2502.04248v1`, `2510.21910v3`, `2609.06612v1`, `2601.04603v1`. `2607.06596v3`, citant d'Async Control, a aussi été lu (trouvé par recherche web).

**Citants pertinents.**
- Lus sur PDF :
  - Dai et collègues 2025 : antécédent de l'hypothèse d'héritage (section 2, point 5) ;
  - Adversarial Déjà Vu : K2[p]+K4 ;
  - MechAudit-40 : K3[d]+K4 ;
  - Constitutional Classifiers++ : K2[c]+K3[d]+K4.
- Lus sur résumé seulement, **non opposables** :
  - 2601.16200, « Feature-Space Smoothing » : certificat au niveau des représentations, sous perturbation de l'entrée ;
  - 2603.23171, « Activation Watermarking » : moniteur d'activations rendu aléatoire par une clé secrète contre l'attaquant adaptatif ;
  - 2603.06594, « A Coin Flip for Safety » : les juges automatiques tombent près du hasard sous les décalages propres au travail d'équipe rouge ;
  - 2609.36490 : un modèle apprend à éviter un moniteur latent à partir du seul retour des verdicts ;
  - 2605.03095 : casser puis reconstruire une défense au niveau des représentations ;
  - 2604.14251 : cascade de moniteurs avec garanties sur le risque et le budget ;
  - 2505.24369 : entraînement adverse itératif en boucle fermée ;
  - 2409.20089 : entraînement adverse par ablation d'une direction de refus dans le flux résiduel ;
  - 2610.22292 : entraînement adverse continu pour l'honnêteté ;
  - 2609.19587 : équipe rouge contre des classifieurs bloquants en production.

**Aucun citant n'annonce la combinaison K1+K3+K4 ou une combinaison avec K5** ; deux résumés (2603.23171, 2604.14251) portent des garanties qui restent à lire sur PDF.

## 7. Ce qui reste à vérifier, et ce qui n'a pas été lu sur PDF

**Non lu sur PDF.** Hôte refusé par la politique réseau de la session, ou pas de PDF libre trouvé :
- Rosin et Belew 1997 (direct.mit.edu, refus 403) ;
- Cliff et Miller 1995 (pas de PDF libre trouvé ; une revue des courbes « courant contre ancêtres » est sur eprints.soton.ac.uk, refus 403) ;
- Watson et Pollack 2001 (eprints.soton.ac.uk, refus 403) ;
- Ficici 2004, thèse (hôte de Brandeis non résolu ; gpbib.cs.ucl.ac.uk, connexion coupée, pour Ficici 2005) ;
- Popovici, Bucci, Wiegand et de Jong 2012 (pas de PDF libre trouvé) ;
- Tambe 2011 (livre) ;
- Paruchuri et collègues 2008 (u.cs.biu.ac.il, connexion coupée) ;
- Brückner et Scheffer 2011, version KDD (personal.utdallas.edu, échec de vérification du certificat ; la vérification n'a pas été contournée ; remplacé par Brückner, Kanzow et Scheffer 2012) ;
- Shlapentokh-Rothman et collègues 2021, coévolution d'attaques et de parades sur catalogues publics (dspace.mit.edu, fichier vide) ;
- Garcia, Lugo, Hemberg et O'Reilly 2017, archive de Pareto en coévolution attaque–défense de réseaux, connu seulement par `2108.03156v1` (p. 2) et `2004.04647v1` (p. 12) ;
- Huber 1965 ;
- Kirch et collègues 2024 ;
- « The Oversight Game » (arXiv 2510.26752 : jeu coopératif d'après un résumé de moteur de recherche) ;
- ControlArena (pas d'article) ;
- billets de l'institut britannique de sûreté de l'intelligence artificielle sur sa recherche évolutive d'attaques contre moniteurs ;
- billet sur les cotes Elo de LinuxArena.

Hôtes à autoriser si Lazar veut ces primaires : direct.mit.edu, eprints.soton.ac.uk, dl.acm.org, demo.cs.brandeis.edu, gpbib.cs.ucl.ac.uk, u.cs.biu.ac.il, cs.utexas.edu.

**Reste à vérifier.**
1. Les annexes non parcourues de MAGIC, AgentSafeEvo, EvoSafety, Bailey et collègues, Terekhov 2026 (hors annexe G) et Async Control.
2. La littérature de cybersécurité coévolutive, détecteurs contre anomalies (table 1 de `2004.04647v1`, p. 12 ; aucun article lu) : un triplet K1+K4 avec détecteurs y est plausible.
3. Les jeux de détection sous adversaire pleinement actif (Tondi, Merhav et Barni ; monographie de Barni et Tondi 2021) et le test d'hypothèses robuste depuis Huber 1965 : c'est la littérature la plus proche de la « barrière minimax au niveau des lois ».
4. Les citations ascendantes de MAGIC, AgentSafeEvo, EvoSafety, Gao et collègues 2018 et Barni et Tondi, non interrogées.
5. Les deux résumés porteurs de garanties (2603.23171, 2604.14251) et 2601.16200, à lire sur PDF.
6. Le recensement est arrêté au 30 octobre 2026 ; des travaux d'octobre 2026 peuvent manquer.

**Lectures partielles.** 53 PDF sont lus sur pages ciblées. Une composante marquée absente pour eux l'est **dans les pages lues et par recherche plein texte** (mots-clés : coévolution, itération, tours, archive, tenu à l'écart, non vu, certificat, garantie, activation, sonde), pas sur lecture intégrale.

## 8. Méthode et traçabilité

**Téléchargement.** Les PDF ont été téléchargés le 30 octobre 2026 entre 16:11 et 16:31 UTC, depuis arXiv (version la plus récente, lue sur la page de résumé) et cinq sites d'éditeurs ou d'auteurs :
- miroir de York pour GECCO 2004 ;
- frontiersin.org ;
- homes.cs.washington.edu ;
- jmlr.org ;
- ijcai.org.

Chaque fichier a été contrôlé par `file --mime-type` puis scellé par `sha256sum f > f.sha256`.

**Contrôle croisé.** 20 des PDF étaient déjà dans `docs/sources/pdf/` ; leurs octets sont identiques à ceux du nouveau dossier :
- 2412.09565v2, 2504.10374v1, 2506.14261v4 ;
- 2510.09462v2, 2512.11949v1, 2512.13526v1 ;
- 2601.11516v4, 2601.19726v1, 2602.01539v2 ;
- 2603.00829v2, 2603.19461v1, 2605.09684v1 ;
- 2605.13411v1, 2605.31140v1, 2606.08892v2 ;
- 2607.06596v3, 2609.17560v1, 2609.32267v1 ;
- 2609.36580v2, 2610.19422v1.

**Téléchargement erroné.** Un PDF téléchargé sous un mauvais identifiant (1811.08788v1, article de physique sans rapport, pris pour Lipizzaner) a été supprimé avec son empreinte dès la lecture de sa première page. Lipizzaner est 1811.12843v1.

**Lecture.** Le texte a été extrait page par page avec `pdftotext`, dans le répertoire de travail de la session, non versé ; les scripts de téléchargement, d'extraction et de recherche n'ont pas été versés non plus. Les pages citées renvoient aux pages du PDF. Les résumés de moteur de recherche n'ont servi qu'à localiser des articles ; aucune affirmation de cette note n'en dépend sans renvoi à un PDF et une page, sauf les éléments explicitement marqués « non lu » ou « résumé seulement ».

**Hors périmètre.** Aucune lecture des branches `donnees/*` et `quarantaine/*`, ni de `prereg/`, `diag/`, `src/` et `docs/notes/bras-attaque/`.

## Annexe A — citants examinés (Semantic Scholar, 30 octobre 2026, vers 16:25 UTC)

Colonne « Source citée » : identifiant arXiv du travail dont la ligne est un citant.

| Source citée | Année | arXiv | Titre du citant |
|---|---|---|---|
| 2204.13779 | 2026 | — | Data-Centric Challenges, Techniques, and Impacts: A Survey on Image Data Perturbation |
| 2204.13779 | 2026 | 2607.06109 | RoME: Robust Mixture of Low-Rank Experts against Multiple Adversarial Perturbations |
| 2204.13779 | 2026 | — | Weaponizing Reflectivity for Pointcloud Deception with Forged Invisible Geometries |
| 2204.13779 | 2025 | 2504.11034 | Defending Against Frequency-Based Attacks with Diffusion Models |
| 2204.13779 | 2025 | 2502.04248 | Adapting to Evolving Adversaries with Regularized Continual Robust Training |
| 2204.13779 | 2024 | 2406.03143 | ZeroPur: Succinct Training-Free Adversarial Purification |
| 2204.13779 | 2024 | 2405.01349 | Position: Towards Resilience Against Adversarial Examples |
| 2204.13779 | 2024 | 2403.05030 | Defending Against Unforeseen Failure Modes with Latent Adversarial Training |
| 2204.13779 | 2023 | 2310.12793 | OODRobustBench: a Benchmark and Large-Scale Analysis of Adversarial Robustness under Distribution Shift |
| 2204.13779 | 2023 | 2302.10980 | MultiRobustBench: Benchmarking Robustness Against Multiple Attacks |
| 2204.13779 | 2023 | — | OODRobustBench: benchmarking and analyzing adversarial robustness under distribution shift |
| 2204.13779 | 2022 | — | Learner Knowledge Levels in Adversarial Machine Learning |
| 2204.13779 | None | — | Position Paper: Beyond Robustness Against Single Attack Types |
| 2403.05030 | 2026 | 2610.22292 | CAT-alyzing Honesty: Continuous Adversarial Training for Transferable LLM Honesty |
| 2403.05030 | 2026 | 2610.13928 | AI Models Can Provably Hide Arbitrary Capabilities |
| 2403.05030 | 2026 | 2610.10345 | SLDR: Defending Against Malicious Fine-tuning via Selective Layers Recovery and Dynamic Routing |
| 2403.05030 | 2026 | 2609.36862 | Safer Content or Firmer Refusals? A Hybrid Perturbation Defense for Alignment under Harmful Fine-tuning |
| 2403.05030 | 2026 | 2609.16204 | Decoy Direction Optimization: A Post-Hoc Defense Against LLM Abliteration |
| 2403.05030 | 2026 | 2608.05045 | Gradient Immunity: Null-Space Resistance to Malicious Fine-Tuning |
| 2403.05030 | 2026 | 2607.28959 | Efficient LLM Adversarial Training via Low-Rank Defense and Circuit-Guided Surrogates |
| 2403.05030 | 2026 | 2607.18454 | Estimating Rare Events in Language Models with Proper Evaluation |
| 2403.05030 | 2026 | 2607.07918 | Efficient Safety Alignment of Language Models via Latent Personality Traits |
| 2403.05030 | 2026 | 2608.14797 | Beyond Tokens: A Survey on Decoding Methods for Large Language and Vision-Language Models |
| 2403.05030 | 2026 | 2606.16349 | From Refusal Geometry to Safety Geometry: Harmfulness--Refusal Coupling under Dynamic Adversarial Fine-Tuning |
| 2403.05030 | 2026 | 2606.07970 | Defending Against Malicious Finetuning by Scaling Train-time Adversarial Attacks |
| 2403.05030 | 2026 | 2606.04168 | When Autoregressive Consistency Hurts Safety Alignment |
| 2403.05030 | 2026 | 2605.12813 | REALISTA: Realistic Latent Adversarial Attacks that Elicit LLM Hallucinations |
| 2403.05030 | 2026 | 2605.11161 | Interpretability Can Be Actionable |
| 2403.05030 | 2026 | 2605.08496 | Latent Personality Alignment: Improving Harmlessness Without Mentioning Harms |
| 2403.05030 | 2026 | 2607.01239 | Breaking Safety at the Token Boundary: How BPE Tokenization Creates Exploitable Gaps in LLM Alignment |
| 2403.05030 | 2026 | 2604.24350 | Unveiling the Backdoor Mechanism Hidden Behind Catastrophic Overfitting in Fast Adversarial Training |
| 2403.05030 | 2026 | 2604.24332 | Mitigating Error Amplification in Fast Adversarial Training |
| 2403.05030 | 2026 | 2604.12817 | Understanding and Improving Continuous Adversarial Training for LLMs via In-context Learning Theory |
| 2403.05030 | 2026 | 2604.10403 | Latent Instruction Representation Alignment: defending against jailbreaks, backdoors and undesired knowledge in LLMs |
| 2403.05030 | 2026 | — | AdvBDGen: A Robust Framework for Generating Adaptive and Stealthy Backdoors in LLM Alignment |
| 2403.05030 | 2026 | 2603.00498 | Antibody: Strengthening Defense Against Harmful Fine-Tuning for Large Language Models via Attenuating Harmful Gradient Influence |
| 2403.05030 | 2026 | 2602.16977 | Fail-Closed Alignment for Large Language Models |
| 2403.05030 | 2026 | 2602.15238 | Closing the Distribution Gap in Adversarial Training for LLMs |
| 2403.05030 | 2026 | 2602.12418 | Sparse Autoencoders are Capable LLM Jailbreak Mitigators |
| 2403.05030 | 2026 | 2602.08813 | Robust Policy Optimization to Prevent Catastrophic Forgetting |
| 2403.05030 | 2026 | 2602.06911 | TamperBench: Systematically Stress-Testing LLM Safety Under Fine-Tuning and Tampering |
| 2403.05030 | 2026 | 2602.05228 | Surgery: Mitigating Harmful Fine-Tuning for Large Language Models via Attention Sink |
| 2403.05030 | 2026 | 2603.06594 | A Coin Flip for Safety: LLM Judges Fail to Reliably Measure Adversarial Robustness |
| 2403.05030 | 2026 | 2601.16200 | Feature-Space Smoothing: Certified Robustness of Deep Representations |
| 2403.05030 | 2026 | 2601.17037 | AMVICC: A Novel Benchmark for Cross-Modal Failure Mode Profiling for VLMs and IGMs |
| 2403.05030 | 2026 | — | Prioritizing Feasible and Impactful Actions to Enable Secure AI Development and Use in Biology |
| 2403.05030 | 2026 | 2601.04603 | Constitutional Classifiers++: Efficient Production-Grade Defenses against Universal Jailbreaks |
| 2403.05030 | 2025 | 2512.10150 | Unforgotten Safety: Preserving Safety Alignment of Large Language Models with Continual Learning |
| 2403.05030 | 2025 | 2512.04144 | RippleBench: Capturing Ripple Effects Using Existing Knowledge Repositories |
| 2403.05030 | 2025 | 2511.05914 | Designing Incident Reporting Systems for Harms from General-Purpose AI |
| 2403.05030 | 2025 | 2510.27062 | Consistency Training Helps Stop Sycophancy and Jailbreaks |
| 2403.05030 | 2025 | 2510.21910 | Adversarial Déjà Vu: Jailbreak Dictionary Learning for Stronger Generalization to Unseen Attacks |
| 2403.05030 | 2025 | 2510.14301 | A Guardrail for Safety Preservation: When Safety-Sensitive Subspace Meets Harmful-Resistant Null-Space |
| 2403.05030 | 2025 | 2510.10265 | Backdoor Collapse: Eliminating Unknown Threats via Known Backdoor Aggregation in Language Models |
| 2403.05030 | 2025 | 2510.01342 | Fine-Tuning Jailbreaks under Highly Constrained Black-Box Settings: A Three-Pronged Approach |
| 2403.05030 | 2025 | 2509.03787 | Evaluating the Robustness of Retrieval-Augmented Generation to Adversarial Evidence in the Health Domain |
| 2403.05030 | 2025 | 2508.07172 | Gradient Surgery for Safe LLM Fine-Tuning |
| 2403.05030 | 2025 | 2508.09190 | Multi-Level Safety Continual Projection for Fine-Tuned Large Language Models without Retraining |
| 2403.05030 | 2025 | 2506.24068 | STACK: Adversarial Attacks on LLM Safeguard Pipelines |
| 2403.05030 | 2025 | 2506.16078 | Probing the Robustness of Large Language Models Safety to Latent Perturbations |
| 2403.05030 | 2025 | 2506.12707 | SecurityLingua: Efficient Defense of LLM Jailbreak Attacks via Security-Aware Prompt Compression |
| 2403.05030 | 2025 | 2506.11938 | Improving Large Language Model Safety with Contrastive Representation Learning |
| 2403.05030 | 2025 | 2506.08473 | AsFT: Anchoring Safety During LLM Fine-Tuning Within Narrow Safety Basin |
| 2403.05030 | 2025 | 2506.00676 | SafeTuneBed: A Toolkit for Benchmarking LLM Safety Alignment in Fine-Tuning |
| 2403.05030 | 2025 | 2505.24369 | Adversarial Preference Learning for Robust LLM Alignment |
| 2403.05030 | 2025 | 2505.24445 | Learning Safety Constraints for Large Language Models |
| 2403.05030 | 2025 | 2505.19397 | Are Time-Series Foundation Models Deployment-Ready? A Systematic Study of Adversarial Robustness Across Domains |
| 2403.05030 | 2025 | 2505.16559 | CTRAP: Embedding Collapse Trap to Safeguard Large Language Models from Harmful Fine-Tuning |
| 2403.05030 | 2025 | 2505.16947 | MixAT: Combining Continuous and Discrete Adversarial Training for LLMs |
| 2403.05030 | 2025 | 2503.01345 | Same Question, Different Words: A Latent Adversarial Framework for Prompt Robustness |
| 2403.05030 | 2025 | 2502.20968 | Beware of Your Po! Measuring and Mitigating AI Safety Risks in Role-Play Fine-Tuning of LLMs |
| 2403.05030 | 2025 | 2502.19537 | No, of course I can! Refusal Mechanisms Can Be Exploited Using Harmless Fine-Tuning Data |
| 2403.05030 | 2025 | 2502.16366 | A Generative Approach to LLM Harmfulness Mitigation with Red Flag Tokens |
| 2403.05030 | 2025 | 2502.11853 | StructTransform: A Scalable Attack Surface for Safety-Aligned Large Language Models |
| 2403.05030 | 2025 | 2502.11910 | Adversarial Alignment for LLMs Requires Simpler, Reproducible, and More Measurable Objectives |
| 2403.05030 | 2025 | 2502.06470 | A Survey of Theory of Mind in Large Language Models: Evaluations, Representations, and Safety Risks |
| 2403.05030 | 2025 | 2502.04204 | "Short-length" Adversarial Training Helps LLMs Defend "Long-length" Jailbreak Attacks: Theoretical and Empirical Evidence |
| 2403.05030 | 2025 | 2502.02260 | Position: Adversarial ML for LLMs Is Not Making Any Progress |
| 2403.05030 | 2025 | 2502.05209 | Model Tampering Attacks Enable More Rigorous Evaluations of LLM Capabilities |
| 2403.05030 | 2025 | 2501.18100 | Panacea: Mitigating Harmful Fine-tuning for Large Language Models via Post-fine-tuning Perturbation |
| 2403.05030 | 2025 | 2501.17148 | AxBench: Steering LLMs? Even Simple Baselines Outperform Sparse Autoencoders |
| 2403.05030 | 2025 | 2501.10639 | Latent-space adversarial training with post-aware calibration for defending large language models against jailbreak attacks |
| 2403.05030 | 2024 | 2410.13211 | Estimating the Probabilities of Rare Outputs in Language Models |
| 2403.05030 | 2024 | 2410.09760 | Targeted Vaccine: Safety Alignment for Large Language Models Against Harmful Fine-Tuning via Layer-Wise Perturbation |
| 2403.05030 | 2024 | 2410.08811 | PoisonBench: Assessing Large Language Model Vulnerability to Data Poisoning |
| 2403.05030 | 2024 | 2410.04332 | Gradient Routing: Masking Gradients to Localize Computation in Neural Networks |
| 2403.05030 | 2024 | 2410.02760 | Erasing Conceptual Knowledge from Language Models |
| 2403.05030 | 2024 | 2409.20089 | Robust LLM safeguarding via refusal feature adversarial training |
| 2403.05030 | 2024 | 2409.18169 | Harmful Fine-tuning Attacks and Defenses for Large Language Models: A Survey |
| 2403.05030 | 2024 | 2409.07985 | Games for AI Control: Models of Safety Evaluations of AI Deployment Protocols |
| 2403.05030 | 2024 | 2409.03274 | Recent Advances in Attack and Defense Approaches of Large Language Models |
| 2403.05030 | 2024 | 2409.01586 | Booster: Tackling Harmful Fine-tuning for Large Language Models via Attenuating Harmful Perturbation |
| 2403.05030 | 2024 | 2408.10682 | Towards Robust Knowledge Unlearning: An Adversarial Framework for Assessing and Improving Unlearning Robustness in Large Language Models |
| 2403.05030 | 2024 | 2408.09600 | Antidote: Post-fine-tuning Safety Alignment for Large Language Models against Harmful Fine-tuning |
| 2403.05030 | 2024 | 2407.15549 | Latent Adversarial Training Improves Robustness to Persistent Harmful Behaviors in LLMs |
| 2403.05030 | 2024 | 2406.11096 | The Potential and Challenges of Evaluating Attitudes, Opinions, and Values in Large Language Models |
| 2403.05030 | 2024 | 2406.02619 | Unelicitable Backdoors in Language Models via Cryptographic Transformer Circuits |
| 2403.05030 | 2024 | 2405.17130 | Explaining the role of Intrinsic Dimensionality in Adversarial Training |
| 2403.05030 | 2024 | 2405.15589 | Efficient Adversarial Training in LLMs with Continuous Attacks |
| 2403.05030 | 2024 | 2405.14577 | Representation Noising: A Defence Mechanism Against Harmful Finetuning |
| 2403.05030 | 2024 | 2402.09063 | Soft Prompt Threats: Attacking Safety Alignment and Unlearning in Open-Source LLMs through the Embedding Space |
| 2403.05030 | 2024 | 2402.08787 | Rethinking machine unlearning for large language models |
| 2403.05030 | 2024 | 2402.01109 | Vaccine: Perturbation-aware Alignment for Large Language Model |
| 2403.05030 | 2024 | 2401.14446 | Black-Box Access is Insufficient for Rigorous AI Audits |
| 2403.05030 | 2026 | — | Probing the Safety Robustness of LLMs in Latent Space |
| 2403.05030 | 2025 | — | Enhancing the Robustness of Vision-Language Foundation Models by Alignment Perturbation |
| 2403.05030 | 2025 | — | MULBERE: Multilingual Jailbreak Robustness Using Targeted Latent Adversarial Training |
| 2403.05030 | None | — | M ODEL M ANIPULATION A TTACKS E NABLE M ORE R IGOROUS E VALUATIONS OF LLM C APABILITIES |
| 2403.05030 | 2026 | — | From Refusal Geometry to Safety Geometry: Harmfulness-Refusal Coupling under Dynamic Adversarial Fine-Tuning |
| 2412.09565 | 2026 | 2610.30727 | Faithful Latent Harm Monitors Work No Better Than the Models Own Behaviour at a Matched False Alarm Rate |
| 2412.09565 | 2026 | 2610.18408 | Prompt-Injection Probes Learn the Conversation, Not Just the Injection |
| 2412.09565 | 2026 | 2610.15883 | What the Model Cannot See: Covert and Provable Text Invisibility in LLMs |
| 2412.09565 | 2026 | 2610.03055 | hacktrace: behavior-supervised detection of reward hacking during code generation |
| 2412.09565 | 2026 | 2609.36490 | LLMs Learn to Evade Latent Monitors from Prior Feedback Alone |
| 2412.09565 | 2026 | 2609.34771 | When Do Model Internals Help? Exploring the Role of Representation Engineering in LLM Safety |
| 2412.09565 | 2026 | 2609.27996 | Your Model Is Leaking: Covert Information Transfer through LLM Residual Streams |
| 2412.09565 | 2026 | 2609.26175 | EADC: Evaluation of Advanced and Deep-level Compliance in Large Language Models |
| 2412.09565 | 2026 | 2609.23700 | When the Agent Becomes the Kernel: A Systematization of Security on the Path to AI-Native Operating Systems |
| 2412.09565 | 2026 | 2609.21996 | A Lie Detector Test for Language Models: Reading Knowledge a Model Won't Reveal |
| 2412.09565 | 2026 | 2609.06612 | MechAudit-40: White-Box Auditing across 40 LLM Attack Mechanisms |
| 2412.09565 | 2026 | 2608.29458 | Reference-Grafting Matches Fine-Tuning at Eliciting Sandbagged Capabilities |
| 2412.09565 | 2026 | 2608.25697 | LMSM: LLM Security Framework Inspired by Linux Security Modules |
| 2412.09565 | 2026 | 2608.21664 | Measuring Activation Control in Large Language Models |
| 2412.09565 | 2026 | 2608.04928 | Does Out-of-Sight Equal Out-of-Mind in CoT Monitorability? |
| 2412.09565 | 2026 | 2608.00583 | A False Average: Pooled CoT-Monitor Accuracy Conceals a Reasoning-Dependent Fragility |
| 2412.09565 | 2026 | 2607.20379 | Train the Model, Not the Reader: Decodability Supervision for Verifiable Activation Explanations |
| 2412.09565 | 2026 | 2607.13087 | GDM AI Control Roadmap |
| 2412.09565 | 2026 | 2608.07514 | Open Technical Problems in Open-Weight AI Model Risk Management |
| 2412.09565 | 2026 | 2606.29646 | Fuzzing Large Language Models to Elicit Hidden Behaviours |
| 2412.09565 | 2026 | — | Selective semantic state editing for private edge-cloud inference in SLMs |
| 2412.09565 | 2026 | 2606.09411 | Now You (Still) See Me: Detecting Evasive Steganographic Payloads in LLMs |
| 2412.09565 | 2026 | 2606.09563 | PRISM: Recovering Instruction Sets from Language Model Activations |
| 2412.09565 | 2026 | 2606.08044 | When Behavioral Safety Evaluation Fails: A Representation-Level Perspective |
| 2412.09565 | 2026 | 2605.27958 | Pressure-Testing Deception Probes in LLMs: Scaling, Robustness, and the Geometry of Deceptive Representations |
| 2412.09565 | 2026 | 2605.03095 | Revisiting JBShield: Breaking and Rebuilding Representation-Level Jailbreak Defenses |
| 2412.09565 | 2026 | 2604.18970 | Mechanistic Anomaly Detection via Functional Attribution |
| 2412.09565 | 2026 | 2604.14865 | Segment-Level Coherence for Robust Harmful Intent Probing in LLMs |
| 2412.09565 | 2026 | 2604.14251 | Calibrate-Then-Delegate: Safety Monitoring with Risk and Budget Guarantees via Model Cascades |
| 2412.09565 | 2026 | 2603.29038 | Trojan-Speak: Bypassing Constitutional Classifiers with No Jailbreak Tax via Adversarial Finetuning |
| 2412.09565 | 2026 | 2603.23171 | Adaptively Robust LLM Monitoring via Activation Watermarking |
| 2412.09565 | 2026 | 2602.15515 | The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes |
| 2412.09565 | 2026 | 2602.08877 | Stress-Testing Alignment Audits With Prompt-Level Strategic Deception |
| 2412.09565 | 2026 | 2602.06911 | TamperBench: Systematically Stress-Testing LLM Safety Under Fine-Tuning and Tampering |
| 2412.09565 | 2025 | 2512.11949 | Neural Chameleons: Language Models Can Learn to Hide Their Thoughts from Unseen Activation Monitors |
| 2412.09565 | 2025 | 2511.22662 | Difficulties with Evaluating a Deception Detector for AIs |
| 2412.09565 | 2025 | — | Detecting Multi-Turn Jailbreak Attacks in Large Language Models via Linear Probes |
| 2412.09565 | 2025 | 2511.06626 | Spilling the Beans: Teaching LLMs to Self-Report Their Hidden Objectives |
| 2412.09565 | 2025 | 2511.00554 | Red-teaming Activation Probes using Prompted LLMs |
| 2412.09565 | 2025 | 2510.21531 | Probe-based Fine-tuning for Reducing Toxicity |
| 2412.09565 | 2025 | 2509.10682 | LLM in the Middle: A Systematic Review of Threats and Mitigations to Real-World LLM-based Systems |
| 2412.09565 | 2025 | 2507.12691 | Benchmarking Deception Probes via Black-to-White Performance Boosts |
| 2412.09565 | 2025 | 2507.09406 | Adversarial Activation Patching: A Framework for Detecting and Mitigating Emergent Deception in Safety-Aligned Transformers |
| 2412.09565 | 2025 | 2507.01786 | Probing and Steering Evaluation Awareness of Language Models |
| 2412.09565 | 2025 | 2506.24068 | STACK: Adversarial Attacks on LLM Safeguard Pipelines |
| 2412.09565 | 2025 | 2506.14261 | RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors? |
| 2412.09565 | 2025 | 2506.10805 | Detecting High-Stakes Interactions with Activation Probes |
| 2412.09565 | 2025 | 2506.06414 | Benchmarking Misuse Mitigation Against Covert Adversaries |
| 2412.09565 | 2025 | 2505.14300 | Beyond Black-Box Obfuscation: Mechanistic Analysis and Defense of White-Box Monitors |
| 2412.09565 | 2025 | 2505.13763 | Language Models Are Capable of Metacognitive Monitoring and Control of Their Internal Activations |
| 2412.09565 | 2025 | 2504.08192 | SAEs Can Improve Unlearning: Dynamic Sparse Autoencoder Guardrails for Precision Unlearning in LLMs |
| 2412.09565 | 2025 | 2502.11853 | StructTransform: A Scalable Attack Surface for Safety-Aligned Large Language Models |
| 2412.09565 | 2026 | — | D2-Monitor: Dynamic Safety Monitoring for Diffusion LLMs via Hesitation-Aware Routing |
| 2412.09565 | None | — | A False Average: Chain-of-Thought Monitors Collapse Where They Are the Only Defense |
| 2512.13526 | 2026 | 2610.34064 | Back to Basics: Formal Analysis Hints Improve Weak-to-Strong Monitoring |
| 2512.13526 | 2026 | 2610.26935 | How Intervention History Changes AI Agent Sabotage on Subsequent Tasks |
| 2512.13526 | 2026 | 2610.07089 | Towards a Unified Misuse Monitoring Benchmark |
| 2512.13526 | 2026 | 2610.04914 | Monitorability Disposition in Large Reasoning Models |
| 2512.13526 | 2026 | 2610.03818 | Control OSWorld: An AI Control Environment for GUI Computer Use Agents |
| 2512.13526 | 2026 | 2609.30217 | Instrumental Monitor Evasion Emerges Under Ordinary Task Pressure |
| 2512.13526 | 2026 | 2609.19587 | Red-Teaming Auto Mode: Improving Blocking Classifiers Against Malign Coding Agents |
| 2512.13526 | 2026 | 2609.27857 | ChronosAttack: Adversarial Tool Scheduling Attacks on LLM Agents |
| 2512.13526 | 2026 | 2607.19321 | ResearchArena: Evaluating Sabotage and Monitoring in Automated AI R&D |
| 2512.13526 | 2026 | 2607.14570 | Democratizing Agent Deployment Safety: A Structural Monitoring Approach |
| 2512.13526 | 2026 | 2607.06596 | Calibration-Family Overfit: Why Trusted Sabotage Monitors Don't Transfer Across Lineages |
| 2512.13526 | 2026 | 2607.05163 | Open Problems in AI Incident Governance |
| 2512.13526 | 2026 | 2607.02514 | Distributed Attacks in Persistent-State AI Control |
| 2512.13526 | 2026 | 2606.20663 | DrugBench: Evaluating AI Control Protocols for Medication Harm Mitigation |
| 2512.13526 | 2026 | 2606.05647 | Coding with "Enemy": Can Human Developers Detect AI Agent Sabotage? |
| 2512.13526 | 2026 | 2605.24216 | Agent-ToM: Learning to Monitor Autonomous LLM Agents via Theory-of-Mind Reasoning |
| 2512.13526 | 2026 | 2605.16626 | SLEIGHT-Bench: A Benchmark of Evasion Attacks Against Agent Monitors |
| 2512.13526 | 2026 | 2605.15377 | Ensemble Monitoring for AI Control: Diverse Signals Outweigh More Compute |
| 2512.13526 | 2026 | 2604.15384 | LinuxArena: A Control Setting for AI Agents in Live Production Software Environments |
| 2512.13526 | 2026 | 2604.11072 | Hodoscope: Unsupervised Monitoring for AI Misbehaviors |
| 2512.13526 | 2026 | 2604.11806 | Detecting Safety Violations Across Many Agent Traces |
| 2512.13526 | 2025 | 2512.22154 | Practical challenges of control monitoring in frontier AI deployments |
| 2606.08892 | 2026 | 2610.03818 | Control OSWorld: An AI Control Environment for GUI Computer Use Agents |
