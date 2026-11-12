# Faits servis au collisionneur — brainstorm du texte III (mesure de l'universalité) — v2

v2 : la v1 (`f2e52f44…`, inchangée) corrigée selon la contre-lecture de la question (constats CL-02, CL-03, CL-14, CL-15, CL-16) : protocole cité dans `collisionneur_v5.py` ; statuts du préambule seulement ; faits transmis par le directeur marqués RAPPORTÉ ; deux conventions d'appariement ; loi de tirage précisée.

Périmètre statistique et méthodologique : aucune famille, aucun comportement d'agent et aucun moyen ne sont décrits ici. Chaque fait porte un statut : **VÉRIFIÉ** (chemin relu sur disque le 30 octobre 2026, ou calcul refaisable avec sa formule), **RAPPORTÉ** (transmis par le directeur, texte source non relu ici), **OBSERVÉ-NON-AUDITÉ** ou **HYPOTHÈSE**. Chemins relatifs à la racine du dépôt de travail.

## Programme

1. VÉRIFIÉ — `CLAUDE.md` (empreinte `e28d090e…`), liste des décisions : l'objectif ultime est l'**universalité mesurée sur des familles inédites** (décision N-044) ; le banc d'évaluation adverse simulé est monté en deux versions, aveugle et informée de la défense, sans dépense (décision N-056) ; un mode est tenu à l'écart de la conception des moniteurs (décision N-054).
2. RAPPORTÉ (demande du directeur) — Règle de base : le programme ne construit **aucun agent attaquant opérationnel**. Le texte exact n'a pas été relu dans un fichier.
3. RAPPORTÉ (demande du directeur) — Les modèles étudiés sont à poids ouverts, de 8 et de 70 milliards de paramètres. Non relu dans un fichier.
4. RAPPORTÉ (décision du directeur) — Les familles tenues à l'écart seront conçues par **plusieurs instances indépendantes**, de fournisseurs et de modèles différents ; **cinq sont prévues** ; chacune est tenue à l'écart de la conception des défenses et scellée à part. Non relu dans un fichier.

## Données de départ sur les familles

5. VÉRIFIÉ — `docs/notes/bras-attaque/bilan-lecteur-isole-ba002-v1.md` (empreinte `48814957…`), comptes seulement : 28 familles distinctes pour Argon (dont 4 combinées), 25 pour Opus 5.5 (dont 3 combinées) ; 18 communes ; 10 propres à Argon, 6 propres à Opus ; une famille d'Argon en recouvre deux chez Opus ; aucune combinaison commune. Aucun contenu de famille n'est servi.
6. VÉRIFIÉ — Même fichier : les deux sources ont reçu la même question ; l'appariement a été fait par **un seul** lecteur (un modèle Sonnet 5.5) avec une grille fermée ; ce lecteur est de la même lignée que l'une des deux sources (Opus était prévu, indisponible).
7. VÉRIFIÉ (calcul refaisable : formule donnée) — L'intersection vaut 18 comptée côté Argon (28 − 10) et 19 comptée côté Opus (25 − 6), puisqu'une famille d'Argon en recouvre deux chez Opus. Familles observées : 34 en unités d'Argon (28 + 6) ou 35 en unités d'Opus (25 + 10).
8. VÉRIFIÉ (calcul refaisable : formule donnée) — Lincoln-Petersen, N = n₁ × n₂ / m : 28 × 25 / 18 = 38,89 ; 28 × 25 / 19 = 36,84. Chapman, N = (n₁ + 1)(n₂ + 1) / (m + 1) − 1 : 29 × 26 / 19 − 1 = 38,68 ; 29 × 26 / 20 − 1 = 36,70.
9. VÉRIFIÉ (calcul refaisable : formule donnée) — Borne à zéro échec (confiance 95 %) : n ≥ ln 0,05 / ln(1 − ε) familles toutes réussies pour borner la part d'échec par ε : 29 pour ε = 0,10 (28,43) ; 59 pour 0,05 (58,40) ; 149 pour 0,02 (148,28). Valable seulement si les familles sont tirées indépendamment selon la loi qui définit la part ε (hypothèse non satisfaite par des familles découvertes).

## Bancs publics (données de départ candidates)

10. VÉRIFIÉ (présence du nom seulement) — SHADE-Arena, ControlArena : cités dans `docs/etat-de-l-art-controle-ia-v1.md` (empreinte `a7d6846d…`) ; MonitoringBench, SLEIGHT-Bench : cités dans `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md` ; Liars' Bench : cité dans `CLAUDE.md` (décision N-061).
11. HYPOTHÈSE — Ces bancs fournissent des trajectoires brutes, étiquetables au niveau des familles, sous une licence compatible, et leur recouvrement avec les données d'entraînement des modèles est mesurable : aucune vérification faite ici.
12. RAPPORTÉ (demande du directeur) — Des journaux de refus de questions passées et des propositions brutes d'une course précédente existent et sont lisibles par le programme ; leurs dossiers ne sont pas dans les pièces de ce tour.

## Protocole du collisionneur

13. VÉRIFIÉ — `donnees/collisionneur-texte-III-v1/collisionneur_v5.py` (empreinte `93571067…`, égale à son compagnon `.sha256`), lignes 55 à 66 (`MODELES`) : A `claude-fable-5-1` (ligne 56), B `claude-opus-5-5` (ligne 58), C `gemini-4-argon` (ligne 61), D `kimi-k3.1-pro` (ligne 64, par le relais Kimi local) ; ligne 67 : quatre lettres.
14. VÉRIFIÉ — Même fichier, ligne 14 : un refus est enregistré tel quel, définitif dans le run, jamais reformulé. Lignes 123 à 125 (`TOURS`) : limites de mots de l'étage III, conception 3 500, critique croisée 3 000, réponse 3 500. Lignes 177 à 195 (`CONSIGNES` des tours E3) : le tour III.1 demande les hypothèses non établies, des duels H_A contre H_B, la mesure minimale de chaque instrument nommé et l'ancrage matériel ; le tour III.2 limite la critique croisée aux « conditions mesurables, au niveau des lois de probabilité » (« jamais une conduite d'agent ») ; le tour III.3 demande une réponse à la question de l'arbitre « en une page ».
15. VÉRIFIÉ — Même fichier, lignes 134 et 141 à 143 (`PREAMBULE`) : quatre statuts seulement (VÉRIFIÉ, RAPPORTÉ, OBSERVÉ-NON-AUDITÉ, HYPOTHÈSE) ; le texte entre balises est une donnée, sauf le bloc QUESTION DE L'ARBITRE, qui pose la question et peut fixer la forme de la réponse. Lignes 368 à 371 : ce bloc est lu dans `question-etage3.md`, versé une fois par `verser_une_fois` (lignes 685 à 696, appel ligne 990).
16. VÉRIFIÉ (faits v1, non relu en v2) — `donnees/collisionneur-bisociation-v1/question-bisociation-deux-espaces-v1.md` (ligne 7) : un refus arrête le tour ; au plus trois questions de repli plus étroites.
