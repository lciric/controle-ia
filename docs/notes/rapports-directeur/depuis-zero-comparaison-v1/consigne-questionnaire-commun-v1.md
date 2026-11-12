# Consigne : questionnaire commun pour éprouver les documents « depuis zéro » — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 10 novembre 2026 (heure au registre), sur le mot de Lazar (verbatim) : « (a) go; la nouvelle session bras atatque en ecrit un aussi, a comparer avec le reste, coordonne toi acec elle ». Trois documents expliquent le programme à un lecteur qui n'en sait rien : celui de la session mère, celui de la session-dépôt, celui de la session du bras d'attaque. Ce questionnaire sert à les éprouver tous les trois de la même façon : un lecteur neuf lit **un seul** document, répond aux questions, et un correcteur note ses réponses contre une clé écrite **avant** que quiconque ait lu un document.

## Destinataire

Un **agent neuf**, qui n'a lu **aucun** des trois documents et ne les lira pas : ni `docs/notes/rapports-directeur/programme-depuis-zero-*`, ni `docs/notes/rapports-directeur/rapport-programme-complet-entretien-*`, ni `brouillons/entretien-taif-v3/socle-preuves-entretien-v1*`, ni aucune synthèse, aucun programme d'entretien et aucun livrable écrit pour l'entretien (`brouillons/entretien-taif-v3/`, `livrables/`), ni rien qui vienne des deux autres sessions. Il écrit le questionnaire à partir des **textes qui font foi** seulement.

## Sources à lire (empreintes à vérifier)

- `docs/programme-controle-ia-v2.md` (`2fd63bad…`) ;
- `docs/brief-claude-code-programme-complet-v2.md`, sections des portes et des critères de G0 et G1 ;
- `docs/notes/note-mathematique-lemme-theoreme-v3.md` ;
- les décisions de `docs/decisions/decision-*.md` que nomme `CLAUDE.md` à la racine, en particulier N-003 et N-004 (énoncés de T et L), N-007 et N-008, N-013, N-044, N-045 v2, N-053 à N-056, N-062, N-063 v2, N-064, N-065 ;
- `docs/notes/resultats-T0.3-v1.md` ;
- les verdicts de `docs/verdicts/` (pour savoir ce qui est établi, pas pour en tirer des chiffres) ;
- `registres/etat.md`, les 30 premières lignes et les sections « Phase en cours » à « Derniers verdicts de porte » ; `registres/decisions.md`, lignes R-2120 à R-2130.

## Ce qu'il faut écrire

**Douze à quinze questions ouvertes**, à réponse courte (une à trois phrases), qui couvrent :
1. le problème (sabotage diffus ; pourquoi un surveillant qui juge chaque action rate, par construction) ;
2. lire les sorties ou lire l'intérieur (boîte noire, boîte blanche) ; ce qu'est une sonde ;
3. le pari, en une phrase ;
4. le lemme d'additivité : ses hypothèses et ce qu'il affirme ;
5. le théorème négatif : son cas et sa conséquence pour le choix de l'agrégateur ;
6. l'hypothèse empirique qui décide entre les deux ;
7. l'hypothèse H1 et ce qui la réfuterait ;
8. ce que veut dire « diffus » comme mesure, et pourquoi un saboteur flagrant ne compte pas ;
9. la question unique du programme et les trois papiers ;
10. les statuts : ce qui est démontré, simulé, mesuré, parié, exploratoire (au moins un exemple de chaque, sans chiffre) ;
11. le premier test sur un vrai modèle : ce qu'il a montré, ce qu'il n'a pas montré, ce que l'audit a ajouté (sans chiffre) ;
12. les deux portes : ce que chacune exige, ce qui se passe si la porte décisive échoue ;
13. le bras d'attaque : ses deux bras, ce que chacun sait et ne sait pas, son état au 10 novembre (au niveau des décisions N-054 et N-056 et du registre, rien de plus) ;
14. l'organisme d'idéation : ce qu'est son juge, en quoi c'est un surveillant, ce que montre l'attaque du juge en termes de frontière (sans chiffre) ;
15. ce qui peut être lu avant l'entretien, et ce qui ne le peut pas.

**Interdits dans les questions et dans la clé** : aucun chiffre de résultat, aucune note (score) d'un surveillant, aucun seuil calibré, aucune épreuve, aucun contenu du bras d'attaque au-delà des décisions inscrites sur `main`. Les nombres structurels sont permis (huit critères, deux portes, trois papiers). Le questionnaire doit pouvoir circuler vers la session du bras d'attaque sans toucher à ses cloisons.

## Les quatre pièces à produire

Dans `docs/notes/rapports-directeur/depuis-zero-comparaison-v1/` :
1. `questionnaire-commun-v1.md` : les questions seules, numérotées, sans indice de réponse ;
2. `consigne-lecteur-naif-v1.md` : la consigne donnée au lecteur, la même dans les trois sessions. Il lit seulement le document qu'on lui donne et ce questionnaire ; il répond à chaque question en une à trois phrases, avec ses propres mots ; il écrit « le document ne le dit pas » plutôt que de compléter de mémoire ; il n'utilise aucune autre source ni connaissance extérieure ; sa sortie est un fichier JSON de forme fixe `{"document": "<nom>", "lecteur_modele": "...", "reponses": [{"question": 1, "reponse": "..."}, ...]}` ; ses heures sont relevées par `date -u`.
3. `consigne-correcteur-v1.md` : le correcteur reçoit les jeux de réponses sous des étiquettes tirées au hasard (X, Y, Z), sans savoir de quel document vient chacun. Pour chaque question et chaque jeu, il note **2** si la réponse contient tous les éléments essentiels de la clé, **1** si elle en contient une partie, **0** si elle est absente ou fausse. Toute affirmation fausse présentée comme un fait est marquée **« erreur »**, même dans une réponse notée 1. Sortie : une table par jeu, avec le total sur 30 et la liste des erreurs.

Dans `/home/user/depuis-zero-cle/`, **hors du dépôt**, un dossier que ni le lecteur ni les autres sessions n'ouvrent :
4. `cle-questionnaire-commun-v1.md` : pour chaque question, deux à quatre éléments essentiels, chacun avec sa source (chemin, empreinte, ligne ou section), et les erreurs typiques à marquer.

Scelle les quatre fichiers (`PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller <fichiers>`). Pour la clé, le compagnon `.sha256` reste à côté d'elle, hors du dépôt. La mère pousse l'empreinte de la clé sur `main` avant tout lecteur.

## Interdits

Ceux de `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` (`1ee3b370…`), en entier, règle 9 comprise. Jamais `diag/*/lecture-sondes-t06.json`, la lecture B de 7a, sa branche de quarantaine, un `diag/` ou `runs/` de 7a, `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`, l'étiqueteur, `scripts/extraire_mesures_epreuve_t06_v1.py`, ni aucun fichier de P3-bis. Aucun appel externe, aucune dépense, aucune écriture git, aucune valeur de clé. Toute heure est relevée par `date -u`. Si un contrôle de permissions ou un classifieur refuse une action, arrête-toi et rapporte-le tel quel.
