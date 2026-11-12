# Consigne — lecture du tour 2 N12-N13 (collisionneur v8) selon ses critères scellés — v1

- **Session mère** (`session_01VJdZpSMxSdk2SJ1ScmdfNv`). Tu es un sous-agent **neuf**. Dépôt de travail `/home/user/controle-ia-travail` (`main`), `PYTHONPATH=src`, `.venv/bin/python`. Sceller : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller CHEMIN`. Français ; heures par `date -u`. Bac à sable : `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/<ton-nom>/`. Disque serré.
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

## Rôle
Lecteur **neuf** : tu n'as écrit ni la question, ni les critères, ni aucune cellule. Modèle : Opus 5.5 (aucune espèce du tour n'était Opus 5.5 : l'espèce B était servie par Opus 4.6, R-1050) — dis-le en tête.
## Pièces (vérifie chaque empreinte)
- **Critères scellés** (ils priment) : `docs/notes/ideation-organisme-v1/course-2/collisionneur-n12-n13-v1/criteres-lecture-n12-n13-tour2-v1.md` (`6bdbfe47…`).
- **Sortie scellée du tour 2**, extraite pour toi sans être ouverte : `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/n12-n13-tour2-sortie/donnees/collisionneur-v8-runs-v1/n12-n13-tour2/` (67 compagnons vérifiés conformes par la mère) ; cellules dans `run-n12-n13-tour2-e3-v1/` ; question `question.md`, faits `faits.md`. Exception à la règle 1 pour ce seul dossier.
- Contexte : synthèse v2 du tour 1 (`synthese-n12-n13-v2.md`, `f0340581…`) ; registre R-920, R-946, R-957, R-959, R-1036, R-1039, R-1050, R-2199.
## À écrire
`docs/notes/ideation-organisme-v1/course-2/collisionneur-n12-n13-v1/synthese-n12-n13-tour2-v1.md`, scellée : application des critères section par section, table des empreintes recalculée par programme, et une section « **couche 4 : ce que les espèces proposent** » (forme d'une ouverture, essai « preuve formelle contre suite bon marché », toute idée de **génération** de mathématiques nouvelles), qui servira aux pas (b) et (c) de R-2199. Aucun commit. Rapport final : chemin, empreinte, verdict en trois lignes, idées sur la couche 4 en une liste courte.
