# Confrontation avec le projet précédent de Lazar (sycophancie, Llama 3.1 8B Instruct) — v1

Session 14, 2026-10-20 vers 10:15 UTC (R-266). Demande de Lazar (R-265, point 3 ; branche C du brainstorm sur la suite de
P3, `docs/notes/brainstorm-suite-P3-v1/note-decision-suite-P3-v1.md`, option C3 : « confronter la recette du plancher au
code de ton projet antérieur »). Dépôt lu en lecture seule : `lciric/sycophancy-construct-validity`, commit
`5ee1d23d5cd6599a4bc858e9659fb2eeaa6a3fe2` (aucune écriture).

## Verdict

La confrontation de recette demandée n'est pas possible : ce dépôt ne contient **aucun plancher de sondes aléatoires**, et
le code de sa sonde n'y est pas versionné. Il apporte en revanche trois leçons qui touchent directement nos sondes
génériques, P3b et P4-instrument.

## Ce que le dépôt contient (et ne contient pas)

- `code/02_probing_extraction.py` et `code/01_caa_polarity_test.py` : textes de remplacement ; la sonde (régression de
  Ridge sur le comportement jugé) et le test de direction CAA ont tourné dans un carnet qui n'est pas dans le dépôt.
- `README.md` l. 85 et `TRACEABILITY.md` l. 87 : les mesures de la sonde étaient des ajustements sur l'entraînement et ne
  sont pas rapportées.
- Aucune trace de direction aléatoire, de plancher, de témoin apparié en covariance (recherche par mots dans `code/`,
  `README.md`, `TRACEABILITY.md`). Le plancher de P3 est donc propre à ce programme (`src/controle_ia/premier_test_ia/`,
  `src/controle_ia/sondes/`), et la branche C3 du brainstorm tombe.

## Trois leçons pour nos sondes

1. **Lire n'est pas causer, et plusieurs extractions donnent des directions presque orthogonales** (`README.md`, section
   « Geometry », l. 38 : CAA, histoires contrastées, Ridge et autoencodeur parcimonieux donnent des directions
   « quasi orthogonales », sans matrice de cosinus conservée). Une sonde générique entraînée sur un concept voisin peut donc
   manquer la direction propre à l'organisme : c'est l'hypothèse « instrument mal aligné » de P3b (sonde oracle) et de la
   revue de la littérature.
2. **Le signal lu vit hors de l'autoencodeur parcimonieux public** pour ce même modèle (`README.md` l. 40 : 86,8 % de la
   variance dans le résidu de reconstruction ; corrélation projection–comportement ρ = 0,684 sur les activations brutes,
   0,212 sur la reconstruction, 0,696 sur le résidu ; réserve d'ajustement sur l'entraînement). Une voie de détection par
   les caractéristiques de cet autoencodeur (celle de l'audit d'objectifs cachés d'Anthropic) risque d'être faible sur
   Llama 3.1 8B : à dire à la revue de la littérature et au choix de P3b.
3. **Le point de décision** (`code/07_decision_point.py`, docstring) : la divergence entre conditions se fait aux tout
   premiers jetons de la réponse (« token 0-1 »). Pour P3b, le signal de l'organisme peut se trouver ailleurs que dans le
   champ du coût (début de l'action) : P3b doit fixer d'avance les empans lus, sans en essayer plusieurs après coup.

Et une mise en garde de méthode, déjà dans les consignes du programme : la circularité extraction–évaluation (`README.md`
l. 84) et l'ajustement sur l'entraînement (l. 85). La sonde de tromperie de P3 a été choisie par départage entre 9
candidates sur 15 à 1,0 sur 120 exemples de validation (note du brainstorm) : même risque de saturation. P3b doit
entraîner sa sonde oracle en validation croisée groupée par tâche, sur des tâches disjointes de l'évaluation.

## Chiffres

Les nombres ci-dessus sont ceux du dépôt cité, recopiés tels qu'écrits (README, commit cité) ; ils ne sont pas de l'état
de l'art (R7 ne s'applique pas à un dépôt du programme de Lazar), et aucun n'entre dans un préenregistrement sans renvoi.
