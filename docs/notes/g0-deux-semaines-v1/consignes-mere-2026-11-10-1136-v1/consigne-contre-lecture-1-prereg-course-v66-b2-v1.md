# Consigne : contre-lecture 1 (R2) du brouillon 2 du préenregistrement de la course réelle de l'organisme — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-10 à 14:52 UTC (heure relevée par `date -u`). Tu es un sous-agent **neuf**, contre-lecteur, d'un autre modèle que le rédacteur (Opus 5.5) : N-052. Tu n'as écrit ni ce texte, ni le code v65 ou v66, ni leurs contre-lectures.

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

Exception à la règle 4 : lecture seule de l'arbre `/home/user/organisme-v65-cl` (tête `7e415cba…`) par `git show`, et `--verifier-seulement` ou essais ciblés **depuis une copie** de cet arbre dans ton bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/cl-prereg-course-v66/` (sans `bwrap`, sans aucun appel de modèle). Aucune recherche par motif sur `docs/notes/` sans exclure `docs/notes/bras-attaque/`. Sceller : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller CHEMIN`.

## À lire (empreintes à vérifier)
- `docs/notes/organisme-boucle-reelle-v1/preenregistrement-boucle-reelle-organisme-v1-brouillon2.md` (`f87ad0e4…`), couples (`43ba74e9…`), script, journal (`ff364a2c…`) ; brouillon 1 (`736e3fd6…`).
- Code et contre-lectures : `docs/notes/organisme-boucle-reelle-v1/code-v66/` (rapport, blocs, configuration v6, contre-lecture courte `a2880368…`), `docs/notes/organisme-boucle-reelle-v1/code-v65/contre-lecture-code-v65-v2.md`.
- Registre : R-1738, R-2206, R-2215, R-2234, R-2243, R-2248 ; `registres/go.md` (GO-2026-11-08-02, GO-2026-11-10-10) ; N-058, N-064 par `git grep` dans `docs/decisions/`.

## Mandat
1. Le texte est-il un préenregistrement complet (R1) : hypothèse, prédiction chiffrée et signe, métrique, seuil, plan d'analyse, critères de lecture gelés, liste d'arrêt ? Les 17 couples en sections gelées (B2-18 à B2-34) sont-ils des alignements sur le code gelé, sans changement d'hypothèse, de seuil ni de signe ?
2. Chaque garde et chaque arrêt annoncé existe-t-il au code v66 (nomme l'essai, cas sain et artefact) ? Les vérifications V-1 à V-8 du lecteur du verdict sont-elles faisables sur le relevé brut et sans contournement par la lecture gelée ?
3. Commandes de la section 12.4 et préalables de 12.3 : exacts contre le lanceur et la configuration v6 (plafonds par relais, `--releve-sha256`, `--utilisateur-bac 64097`, `--collisionneur`, copie de `registres/go.md` et son empreinte) ; rejoue `--verifier-seulement` depuis une copie si possible.
4. Les deux nœuds (NL-1 issue C1 sans carte retenue ; NL-2 ligne de GO neuve) sont-ils bien posés, et n'y en a-t-il pas d'autre caché ?
5. Q-4 du journal (titres numérotés refusés par `controle_ia.prereg`) : quel validateur fait foi pour ce texte (lanceur de l'organisme ou `controle_ia.prereg`) ?
6. **Verdict** : « scellable après les mots de Lazar et corrections » (couples exacts) ou « non scellable » (bloquants).

## Sortie
`prereg/contre-lectures/preenregistrement-boucle-reelle-organisme-v1-brouillon2-cl1.md`, scellé ; constats CLB-n. Rapport final : chemin, empreinte, verdict en une ligne, constats bloquants.
