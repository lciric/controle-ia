# Contre-lecture du préenregistrement P-041, examen final au protocole de Bailey (v1)

31 octobre 2026, 09:53 UTC. Contre-lecteur neuf (Opus 4.6, fourche de session-depot), qui n'a pas écrit le brouillon (R2). Aucune dépense, aucun commit, aucun appel payant.

- **Brouillon relu** : `prereg/P-041-examen-final-v1.md`, empreinte `216d86300f819a53327bc3760e1ebd350fe885dd8037cbb45aecd9035cc9af0f`
- **Documents croisés** :
  - `docs/decisions/proposition-P-041-organisme-coevolutif-attaque-defense-v3.md` (`72aec5322c61490d…`) — sections 2 et 5
  - `docs/notes/anteriorite-P-041-v1/verification-bailey-2412.09565-v1.md` (`31eb1dde…`) — vérification du protocole Bailey sur PDF
  - `docs/decisions/decision-N-053-v1.md` — invariant N-053 (lignes 42-44)
  - `docs/decisions/decision-N-056-v1.md` — bases boîte blanche (ii) cascade, (iii) dernier état
  - `prereg/gabarit-preregistrement-v1.md` — gabarit des sections obligatoires

## Verdict

**9 points à traiter, dont 5 à corriger avant scellement et 4 à préciser.** Aucune erreur factuelle sur Bailey ; les références de pages sont fidèles à la vérification. Les problèmes portent sur le protocole du bras de base, la cohérence interne du texte, et le cadrage de l'expérience dans G1.

---

## Points à corriger (avant scellement)

### CL-1. Ambiguïté majeure sur le réentraînement du bras de base (ligne 65)

Le brouillon écrit : « Nombre d'époques de réentraînement identique au nombre de générations de l'arène, pour un budget comparable. »

Chez Bailey (p. 11, vérification §(1)), la défense est réentraînée **à chaque époque** de la boucle adversaire : l'attaquant et le défenseur alternent pendant plus de 70 époques. Si l'arène a produit, par exemple, 5 générations, le bras de base n'aurait que 5 réentraînements, soit un protocole radicalement différent de Bailey, avec beaucoup moins d'adaptation.

**Deux lectures possibles** ; l'une est un écart au protocole, l'autre une phrase mal rédigée :
- (a) Le bras de base suit Bailey fidèlement (réentraînement à chaque époque, 70-100 fois) et la phrase sur les « générations de l'arène » est superflue → la supprimer.
- (b) Le bras de base est réentraîné seulement autant de fois que l'arène a eu de générations → c'est un écart majeur à Bailey qu'il faut justifier explicitement (avantage ou désavantage pour la base ? comparaison loyale ?).

**Recommandation** : adopter (a), supprimer la phrase « Nombre d'époques de réentraînement identique au nombre de générations de l'arène, pour un budget comparable » et écrire : « La défense du bras de base est réentraînée à chaque époque de la boucle adversaire, comme chez Bailey (p. 11). »

### CL-2. Asymétrie entre les bras non justifiée (lignes 63-69)

Le bras arène a une défense **figée** (pas de réentraînement) ; le bras de base a une défense **réentraînée** à chaque époque (protocole de Bailey). Cette asymétrie est par conception — la v3 de P-041 l'énonce clairement (section 2 : « Défense figée, sortie de l'arène ») et le principe est « l'avantage du terrain sert à apprendre ; l'attaque joue en dernier pour mesurer ».

Mais le brouillon ne dit pas **pourquoi** cette asymétrie est légitime. L'arène a un avantage (entraînée sur des familles synthétiques à paramètres déclarés), mais un désavantage (ne peut pas s'adapter aux attaques spécifiques du 8B). La base a l'avantage inverse (s'adapte, mais ne connaît pas la structure des familles).

**Recommandation** : ajouter, dans le plan d'analyse ou en tête de la section « Données », un paragraphe de justification de l'asymétrie, citant la v3.

### CL-3. Contradiction « pas un test » / « deux tests » (lignes 51 et 91)

La section « Seuil » (ligne 51) dit : « Cet examen n'est pas un test d'hypothèse au sens classique ». La section « Corrections pour comparaisons multiples » (ligne 91) dit : « Correction de Bonferroni (**deux tests**, α = 0,025 par test) ».

La correction de Bonferroni peut s'appliquer à des intervalles de confiance simultanés sans que ce soit un test formel. Mais le mot « tests » contredit la section « Seuil ».

**Recommandation** : remplacer « deux tests, α = 0,025 par test » par « deux intervalles simultanés, niveau nominal α/2 = 0,025 par intervalle ».

### CL-4. Cadrage de l'expérience dans G1 absent

N-056 (lignes 38-45) exige que G1 batte, en plus de chaque moniteur boîte noire, les deux bases boîte blanche : (ii) la cascade de portes et (iii) la sonde sur le dernier état. Le brouillon ne compare qu'à la base « instances seules ».

Ce n'est pas nécessairement un oubli — l'examen final est une sous-expérience de G1, pas G1 elle-même — mais le brouillon ne le dit nulle part.

**Recommandation** : ajouter en tête du préenregistrement ou dans la section « Hypothèse » une phrase de cadrage : « Cet examen est une sous-expérience de G1 ; il mesure un des contrastes (arène contre base « instances seules ») ; les autres contrastes exigés par G1 (bases (ii) cascade et (iii) dernier état, moniteurs boîte noire) font l'objet de préenregistrements distincts. »

### CL-5. Éléments « à fixer avant scellement » non résolus (lignes 14, 45, 71)

Trois éléments restent ouverts :
- Le juge d'évasion (StrongREJECT ou équivalent, ligne 45) : doit être fixé.
- Le jeu d'entrées bénignes (ligne 71) : doit être fixé.
- Le préenregistrement de l'arène (ligne 14) : dépendance non encore scellée.

Les deux premiers **doivent** être résolus au scellement (noms, versions, empreintes). Le troisième est une dépendance externe ; il suffit de noter que l'examen final ne peut pas être lancé avant que cette dépendance soit remplie.

**Recommandation** : fixer StrongREJECT (version, commit du dépôt public) et le jeu bénin (nom, taille, source) au scellement. Ajouter dans la liste d'arrêt : « L'arène n'a pas produit de défense valide → l'examen final est reporté. »

---

## Points à préciser (recommandés mais non bloquants)

### CL-6. Protocole de mesure du débordement non détaillé (ligne 47)

L'estimand du débordement est « écart entre le rappel sur les familles de l'arène (classe déclarée et familles tenues à l'écart) et le rappel sur les activations du 8B ». Mais comment les activations « des familles de l'arène » sont-elles produites ? Par le générateur de l'arène ? Par un jeu de test séparé ? En activations synthétiques ou induites par le modèle ?

**Recommandation** : préciser la source des données de la mesure de débordement (le rappel sur les familles est probablement synthétique, mesuré sur le banc de l'arène ; le rappel sur le 8B est induit par l'optimiseur ; l'écrire).

### CL-7. Seuil du bras de contrôle — justification (lignes 106, 116)

Le seuil de 5 points de rappel pour le bras de contrôle « identiques réétiquetés » est un garde-fou, pas un test. Cependant, pour n = 200 entrées adverses et un rappel autour de 50 %, l'écart type de la différence entre deux sous-ensembles est d'environ 5 points (√(2 × 0,5 × 0,5 / 200) × 100 ≈ 5,0). Un écart de 5 points arrive donc par hasard avec une probabilité non négligeable (~32 % sous l'hypothèse de variance binomiale).

**Recommandation** : justifier le seuil de 5 points (est-ce un seuil large pour ne déclencher l'arrêt que sur un problème grave, ou est-il calibré sur une probabilité de fausse alerte ?). Ou le resserrer.

### CL-8. Précondition non couverte dans la liste d'arrêt (ligne 26)

L'hypothèse de travail « L'arène a produit une défense jugée valide par sa propre porte » est nécessaire mais non couverte par la liste d'arrêt. Si l'arène échoue à sa propre porte, l'examen final ne peut pas avoir lieu.

**Recommandation** : ajouter dans la liste d'arrêt : « L'arène n'a pas franchi sa propre porte → examen final reporté, pas annulé. »

### CL-9. Principe « l'attaque joue en dernier » non explicité

La v3 (section 2) énonce : « L'avantage du terrain sert à apprendre ; l'attaque joue en dernier pour mesurer. » Le brouillon mesure le rappel « sur la dernière attaque seulement » (ligne 40), ce qui est cohérent avec ce principe, mais ne le cite pas. Le principe donne la raison du choix de la métrique « dernière attaque ».

**Recommandation** : ajouter une phrase dans la section « Métrique » citant ce principe de la v3.

---

## Points conformes (vérifiés)

| # | Point vérifié | Source | Statut |
|---|---|---|---|
| 1 | Rappel à 1 % de fausses alertes, calculé sur la dernière attaque | Bailey p. 12, légende figure 8a ; vérification §(1) | conforme |
| 2 | Suffixe de plongement universel | Bailey p. 7, 9 ; vérification §(2) | conforme |
| 3 | ≥ 70 époques | Bailey p. 11 ; vérification §(1) | conforme |
| 4 | Objectif double (nuisance + camouflage, équation 1 p. 5) | Bailey p. 5 ; vérification §(2) | conforme |
| 5 | « optimiseur d'entrées adverses » (pas « sur les activations ») | vérification, nuance mineure : l'attaque opère sur les plongements d'entrée | conforme |
| 6 | Base « instances seules » au sens de Bailey (p. 11, 42) | vérification §(3) : la défense ne connaît que les instances | conforme |
| 7 | Signe non contraint (R-879, R-880) | `registres/decisions.md` R-879, R-880 | conforme |
| 8 | Invariant N-053 couvert (hypothèses de travail l. 28 et liste d'arrêt l. 119) | `decision-N-053-v1.md` l. 42-44 | conforme |
| 9 | R3 respecté (aucun run visant un signe positif) | le signe est non contraint, la prédiction P-EF1 dit « non contraint » | conforme |
| 10 | R9 respecté (graines par SeedSequence, 128 bits, dérivées par tâche, dans le manifeste) | section « Graines » | conforme |
| 11 | Intervalles de Clopper-Pearson à 95 % pour des proportions | correct pour un estimateur binomial | conforme |
| 12 | Échantillons disjoints pour calibration du seuil et mesure du rappel | bonne pratique | conforme |
| 13 | Bras de contrôle « identiques réétiquetés » pour estimer la variance | bonne pratique | conforme |
| 14 | Gabarit complet (toutes les sections du gabarit sont présentes) | `prereg/gabarit-preregistrement-v1.md` | conforme |
| 15 | Section « Contre-lecture » contient « À REMPLIR » | attendu pour un brouillon pré-contre-lecture | conforme |
| 16 | Demi-largeur ~7 points pour n = 200, rappel 50 % (Clopper-Pearson 95 %) | calcul vérifié : intervalle [0,43 ; 0,57] | conforme |

---

## Résumé

| Catégorie | Nombre |
|---|---|
| À corriger (avant scellement) | 5 (CL-1 à CL-5) |
| À préciser (recommandés) | 4 (CL-6 à CL-9) |
| Conformes | 16 |

Le point le plus grave est CL-1 (ambiguïté sur le réentraînement du bras de base) : si la phrase est lue telle qu'elle est écrite, le bras de base ne suit pas le protocole de Bailey, ce qui invalide la comparaison. Ce point doit être résolu en priorité.
