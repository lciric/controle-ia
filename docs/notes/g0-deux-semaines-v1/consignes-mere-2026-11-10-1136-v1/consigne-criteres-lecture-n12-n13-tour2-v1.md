# Consigne — critères de lecture du tour 2 N12-N13 (collisionneur v8), à sceller avant toute ouverture — v1

- **Session mère** : nouvelle instance (reprise du 2026-11-10). Tu es un sous-agent **neuf** (rédacteur Opus). Dépôt `/home/user/controle-ia-travail` (`main`), `PYTHONPATH=src`, interpréteur `.venv/bin/python`. Sceller : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller CHEMIN`. Dépôt public de l'organisme, cloné en lecture : `/home/user/ideation-organism` (tête `6510199`). Français, presque aucun sigle ; toute heure par `date -u`. Bac à sable : `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/<ton-nom>/`. **Disque serré** : aucune copie lourde.
- **Demande de Lazar (verbatim)** : « ecir smoi le programme complet exhaustif avce toutes les couchhes et mecanismes prevus pour l'org » puis « precise bine dans le programme toutes nos idees hypotheses resultats proposiitons pour que rien de notre brinstorm ne soit perdu ».
- **Interdits communs, recopiés mot pour mot (`docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md`, `1ee3b370…`)** :

# Interdits communs aux sous-agents de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy` (10 novembre 2026, v2)

Écrit le 2026-11-09 vers 22:00 UTC (heure relevée par `date -u`). Recopié mot pour mot dans chaque consigne de cette série.

**v2** (R-2086) : v1 recopiée à l'identique (`851028fc…`), plus la règle 9 ; écrite après deux accès mécaniques par recherche récursive (R-2064, R-2086).


1. **Fichiers et branches qu'on n'ouvre jamais** (ni lecture, ni affichage, ni copie, ni passage à un script, ni `git show`, ni `git ls-tree`, ni `git fetch`) :
   - `diag/*/lecture-sondes-t06.json` de tout run, et nommément `diag/20261109-070232-t06-reel/lecture-sondes-t06.json` (DT-4 : rien avant le verdict scellé de P3-bis) ;
   - la lecture B de la course 7a et la branche `donnees/lecture-b-7a-quarantaine-v1` (R-2041, R-2048) ;
   - tout `diag/` et tout `runs/` de la course 7a (`20261109-070232-t06-reel`) et la branche `essai/t06-explo-v3`, sauf permission écrite dans la consigne ;
   - `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` (le bras d'attaque n'est pas le mandat de la mère : N-056, R-2045, R-2047) ;
   - les items, clés et réponses de l'étiqueteur (branche `prep/etiqueteur-v2-lecture-interrompue-reprise-v1`).
2. **Secrets** : ne jamais lire, afficher ni copier une valeur de clé ; jamais `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ`, même avec la sortie jetée.
3. **Aucun appel** de modèle ni d'interface externe (Argon, Claude, autres), aucune location d'instance, aucun `vastai`, aucune dépense.
4. **Git** : aucun `checkout`, `switch`, `reset`, `stash`, `commit`, `push`, `fetch`, `merge`, `rebase`, ni modification de l'index ; les autres commits se lisent par `git show <commit>:<chemin>` seulement (ils sont déjà dans le clone local). Rien n'est écrit hors des chemins de sortie nommés dans la consigne.
5. **Essais** : ne pas lancer la suite complète (la session mère la fait tourner) ; des essais ciblés sont permis.
6. **Refus** : si un contrôle de permissions ou un classifieur refuse une action ou une réponse, s'arrêter sur ce point et le rapporter tel quel ; ni contournement, ni reformulation, ni transfert.
7. **Heures** : toute heure écrite est relevée par `date -u` et dite telle.
8. **Rapport final à la mère** : chemins écrits, empreintes sha256, verdict en une ligne, points ouverts ; **aucune valeur numérique tirée d'une sonde de 7a** (il ne doit d'ailleurs y en avoir aucune sous vos yeux).
9. **Recherches et parcours** : aucune recherche récursive (`grep -r`, `rg`, `find … -exec`, motif `**` ou `*/` développé par l'interpréteur) sur un dossier qui contient un chemin interdit sans l'exclure explicitement ; en pratique, chercher avec `git grep` et des exclusions de chemins (`git grep -n MOTIF -- . ':(exclude)docs/notes/bras-attaque' ':(exclude)scripts/extraire_mesures_epreuve_t06_v1.py' ':(exclude)diag' ':(exclude)runs'`) ou dans une liste de fichiers nommés ; `verifier-arbre` et tout outil qui hache un arbre entier ne se lancent que sur un arbre où `docs/notes/bras-attaque/` n'est pas extrait.

## Interdits propres à cette tâche (en plus)
- **Cloison du bras d'attaque (R-2152, R-2170)** : tu n'ouvres aucun document de la session du bras, en particulier ni `docs/notes/rapports-directeur/dossier-entretien-27-novembre-v1/pieces-bras-v1/` (s'il existe), ni « organisme depuis zéro v4 », ni « programme depuis zéro v5 », ni la branche `claude/compassionate-meitner-d4ryyk`, ni `docs/notes/bras-attaque/`. Rien sur le **mode tenu à l'écart** (N-054) au-delà de son existence.
- **Sorties scellées jamais lues** (R1 : on n'ouvre pas une sortie avant le scellement de ses critères de lecture) : tu ne lis **aucune cellule** de collisionneur ni aucune réponse de modèle **non encore synthétisée**, en particulier rien sous `donnees/` ni sur les branches `donnees/…` (collisionneur v8 : tour 2 N12-N13, convergence v3, sélection, bac à sable ; collisionneur v9 du 2 novembre). Tu les **listes** comme « payées, scellées, non lues » à partir du registre, avec chemin, commit et dépense. Tu lis les **synthèses scellées** qui en existent.
- **Niveau méthode seulement (R-607)** : aucune recette opérationnelle d'attaque contre un moniteur ou un juge ; une idée d'attaque se décrit par sa classe et son but, jamais par son mode d'emploi.
- Tout chiffre ou toute affirmation renvoie à un chemin et une empreinte (R6), ou à une ligne R- du registre ; ce qui n'a pas de source est dit « sans source » et n'est pas affirmé. Ne confonds jamais « codé », « décidé », « prévu », « fermé », « proposé non tranché », « idée non retenue ».

## Rôle
Rédacteur neuf des **critères de lecture**. Tu n'ouvres **aucune cellule** du run (`run-n12-n13-tour2-e3-v1/`) : tu travailles seulement sur les entrées du tour et sur les pièces déjà lues. Un lecteur différent appliquera tes critères.

## À lire
- Critères du tour 1 : `docs/notes/ideation-organisme-v1/course-2/collisionneur-n12-n13-v1/criteres-lecture-n12-n13-v1.md` (`71b63584…`) ; synthèse v2 du tour 1 `synthese-n12-n13-v2.md` (`f0340581…`) ; erratum.
- Entrées du tour 2, sur la branche `donnees/collisionneur-v8-runs-v2` (déjà récupérée dans le clone ; exception à la règle 4 : `git show origin/donnees/collisionneur-v8-runs-v2:<chemin>` permis pour ces **trois** fichiers seulement) : `donnees/collisionneur-v8-runs-v1/n12-n13-tour2/question.md`, `…/faits.md`, `…/balayage-faits.txt` (vérifie leurs compagnons).
- Registre : R-946, R-957, R-959, R-964, R-965, R-1036, R-1039, R-1050, R-2199.

## À écrire
`docs/notes/ideation-organisme-v1/course-2/collisionneur-n12-n13-v1/criteres-lecture-n12-n13-tour2-v1.md`, scellé : mêmes garde et structure que le tour 1, adaptés au tour 2 (cinq espèces A à E, l'espèce B servie par Opus 4.6 et déclarée, R-1050 ; question ciblée sur les neuf divergences ; section à part « pistes générales consensuelles et pistes originales », R-964 ; **section à part sur la couche 4** : ce que les espèces disent de la forme d'une ouverture, de l'essai « preuve formelle contre suite bon marché » et de toute idée de **génération** de mathématiques nouvelles, demandée par Lazar, R-2199). Aucun commit. Rapport final : chemin, empreinte.
