# Consigne : synthèse du tour du collisionneur sur l'expérimentateur de l'organisme — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-11 à 16:16 UTC (heure relevée par `date -u`). Destinataire : un **lecteur neuf**, qui n'a écrit ni la note de conception, ni la question, ni aucune cellule, ni opéré le tour.

## Interdits, recopiés mot pour mot (`docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md`, `1ee3b370…`)

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

Exception à la règle 4 : aucune. Tu n'écris que `docs/notes/collisionneur-experimentateur-v1/synthese-v1.md` (scellé) et ton bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/synthese-exp/`. Aucun appel de modèle, aucune dépense.

## À lire
`docs/notes/collisionneur-experimentateur-v1/faits-v1.md` (`9337032a…`), `docs/notes/collisionneur-experimentateur-v1/question-v1.md` (`7ea507f1…`), les douze cellules `docs/notes/collisionneur-experimentateur-v1/run-e3-v1/cellules/*.md` (sceaux à vérifier), `docs/notes/collisionneur-experimentateur-v1/depense-et-incidents-v1.md` ; pour le contexte, la note de conception `docs/notes/ideation-organisme-v1/experimentateur-v1/note-conception-experimentateur-v1.md` (`7df9afc4…`) et le modèle de synthèse du 9 novembre `docs/notes/collisionneur-conception-qo1-q1-v1/synthese-v1.md`. Registre : R-2368, R-2370, R-2372, R-2379, R-2389.

## Mandat
1. Position de chaque espèce (A Fable 5.1, B Opus 4.6, C Argon, E Astra ; D Kimi absent) au premier tour, ce que la critique croisée change, réponse finale : choix (Kaimen d'abord / The Agentic Scientist d'abord / autre), raisons, risques, mesure qui départagerait, ce qui ferait changer d'avis.
2. **Ce qui converge, ce qui diverge**, et les arguments neufs par rapport à la note de conception (surtout sur la question de Lazar : « pourquoi pas The Agentic Scientist ? »).
3. Faiblesses du tour (absence de Kimi, plafonds de sortie bas, ancrage de la question) et leur effet possible.
4. **Recommandation du lecteur** à la mère, avec confiance ; dis ce que la mère doit soumettre à Lazar (format de décision : décision en une phrase, enjeu, options avec avantage et inconvénient, recommandation et confiance).

## Sortie
`synthese-v1.md` scellé ; rapport final : chemin, empreinte, recommandation en une ligne, ton modèle.
