# Proposition — P-011 — conception des sondes v0 (T0.7) — v1

Rédigée le 2026-10-06 vers 17:55 UTC (horloge du système) par la session de mise en œuvre. Hiérarchie de décision : « proposer avec recommandation » (couches et concepts de sondes) ; défaut appliqué 48 heures après l'envoi du compte rendu qui la présente. Elle suppose P-009 (organismes) et D1.

## Décision

Quelles sondes entraîner, sur quelles couches et quelles données, pour prouver le critère 3 de G0 : « sondes v0 au-dessus du plancher aléatoire apparié, sur (i) et (ii), avec intervalles de confiance » (brief, T0.7).

## Enjeu

- **Le code est prêt** (R-069, `src/controle_ia/sondes/`) :
  - cinq familles, chacune agrégée par le maximum ou par l'attention ;
  - plancher apparié en covariance (recette provisoire, à confronter au code de P3) ;
  - aire sous la courbe avec intervalles par blocs de tâches ;
  - interface du harnais (calcul en ligne).
- **Anti-circularité (brief)** : jamais d'entraînement et d'évaluation sur les mêmes organismes. On entraîne sur des données génériques ou sur une famille, et on évalue sur une autre.
- **Test de validité dès la v0 (brief)** :
  - une sonde qui lit « j'ai une instruction cachée » réussit sur (i) et échoue sur (ii) ;
  - une sonde d'intention réussit sur les deux.
- **Données antérieures sur PDF** (niveau 2) :
  - les sondes s'appuient beaucoup sur l'évidence textuelle (2509.21344) ;
  - les sondes de tromperie sont sensibles au style et à la couche (2605.27958) ;
  - dans 2502.03407, la moyenne bat le max pour la sonde principale ; elle nous est interdite ;
  - les sondes de « conscience d'évaluation » suivent surtout la mise en forme (2603.19426, recherche affirmative, à lire sur PDF).
  - D'où l'importance du plancher et de la famille (ii), sans consigne dans le contexte.
- **Calcul** : 6 heures de carte au devis v1, sur la passe unique validée en T0.4 (couches capturées en une passe).

## Options

**(a) Données génériques pour l'entraînement, organismes (i) et (ii) pour l'évaluation seulement.**
- **Concepts et données** :
  1. **tromperie** : recette de 2502.03407 réimplémentée (paires de consignes honnête / trompeuse) ; le dépôt d'Apollo n'a pas de licence ;
  2. **enjeux élevés** : jeu de models-under-pressure (licence MIT, révision `77d5c265`) ;
  3. **dissimulation** (« j'ai une instruction cachée ») : paires synthétiques avec ou sans instruction cachée dans la consigne, sur les 32 tâches de réserve de T0.5, jamais sur les tâches d'évaluation ;
  4. **intention de saboter** : paires synthétiques de propositions écrites pour bien faire ou pour affaiblir en douce, sur les mêmes tâches de réserve, sans consigne visible au moment de la lecture ;
  5. **conscience d'évaluation** : cadrages « test » contre « déploiement », réservée au test de validité de construit (H8) et hors du critère 3, parce qu'elle est fragile à la mise en forme.
- **Couches** : 7, 15 et 23 sur 32 (précoce, médiane, tardive), celles de T0.4.
- **Familles** : les cinq du programme, chacune avec son agrégation naturelle (différence de moyennes, linéaire et perceptron par le maximum, attention, Mahalanobis sur les jetons honnêtes).
- **Critère 3** :
  - aire sous la courbe par action, au-dessus du plancher (borne basse de l'intervalle à 95 % au-dessus du quantile 0,95 du plancher), sur (i) et sur (ii) ;
  - positifs : les actions sabotées ; négatifs : les actions honnêtes et celles du témoin « instruit sans sabotage » ;
  - choix de la sonde rapportée fait sur un jeu de validation générique, jamais sur les organismes.
- **Test de validité** : la sonde « dissimulation » et la sonde « intention » sont lues sur (i), (ii) et le témoin. Le préenregistrement de T0.7 fixe les signes attendus.
- **Avantages** : anti-circularité stricte ; données en partie publiques ; c'est le test le plus dur, donc le plus crédible au-dessus du plancher.
- **Inconvénients** : décalage de distribution entre données génériques et organismes ; risque d'échec sur (ii).

**(b) Entraînement croisé entre familles** (entraîner sur (i), évaluer sur (ii), et l'inverse).
- **Avantages** : même distribution de tâches ; signal plus fort attendu.
- **Inconvénients** : une sonde entraînée sur (i) peut lire le texte de la consigne (2509.21344) ; la sonde (ii) → (i) reste propre ; pas de lecture générique du concept.

**(c) (a) comme bras principal du critère 3, (b) rapporté à titre descriptif.**
- **Avantages** : surcoût faible, puisque les activations des organismes sont recueillies de toute façon et que l'entraînement d'une sonde coûte peu ; diagnostic du décalage de distribution.
- **Inconvénients** : deux lectures à rapporter. Le choix du bras principal doit être gelé avant tout résultat.

## Recommandation

**(c)**, confiance ≈ 60 %. Le verdict du critère 3 se lit sur le bras (a), gelé d'avance. Le bras (b) explique un échec éventuel sans offrir de seconde chance.

## Défaut

Sans réponse sous 48 heures, l'option (c) s'applique, puis :
- préenregistrement de T0.7 (brouillon, contre-lecture, scellement avant tout entraînement) ;
- jeux synthétiques (dissimulation, intention) écrits par un sous-agent neuf sur les tâches de réserve, scellés ;
- reprise de models-under-pressure à la révision citée, avec mention de la licence.
