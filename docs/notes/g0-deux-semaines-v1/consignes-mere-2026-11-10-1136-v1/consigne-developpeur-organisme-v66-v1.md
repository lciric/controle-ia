# Consigne — code v66 de l'organisme d'idéation (corrections de la contre-lecture du code v65) — v1

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

## Rôle et exceptions
Développeur neuf ; tu n'as écrit ni la v65, ni sa contre-lecture. **Exceptions à la règle 4** : dans l'arbre `/home/user/organisme-v65-cl` (clone du dépôt public de l'organisme, branche locale `prep/organisme-v65-boucle-reelle-v2`, tête `cef5ea60…`), tu crées la branche locale `prep/organisme-v66-boucle-reelle-v1` à partir de `cef5ea60` et tu y committes (jamais de `push`, jamais de réseau, jamais de dépôt public touché). Aucun appel de modèle, aucune dépense, aucune instance.
## Sources
- Contre-lecture : `/home/user/controle-ia-travail/docs/notes/organisme-boucle-reelle-v1/code-v65/contre-lecture-code-v65-v2.md` (`c4ddfc7f…`, Fable, « utilisable pour la course après corrections »).
- Consigne et rapport du développeur v65 : `docs/notes/organisme-boucle-reelle-v1/consigne-developpeur-organisme-v65-v1.md` (`2dc207e7…`) ; rendu extrait dans `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/code-v65-v1/` (dont `rapport-developpeur-organisme-v65-v1.md`, `blocs-pour-le-texte-v65.md`).
## À faire (noms neufs, R12 : rien de la v65 n'est écrasé)
1. **CLV65-01** : la lecture ne rend C1 que si les fausses plantées ont été jugées ; tout autre cas a sa ligne (non jugeable, nœud), avec cas sain et artefact.
2. **CLV65-02** : jugements écrits au relevé au fil de l'étage (un arrêt ne masque plus une brèche) ; héritage refusé lu avec « C4 (partielle) » ; branche « empreinte lue ≠ écrite » atteignable et éprouvée.
3. **CLV65-03** : la vue réellement servie aux proposeurs de la génération 2 est vérifiée par empreinte au moment du service ; mutation « ne sert que K1 » tuée.
4. **CLV65-04** : un essai sur artefact pour chaque garde sans essai citée (garde 7 réécrite, appel de la garde 21, branche réelle du lanceur jusqu'au chargement de la configuration, gardes secondaires de dépense, d'héritage, de jeu, de lecture) ; les 20 mutations du contre-lecteur rejouées, toutes tuées pour la raison attendue ou déclarées équivalentes avec preuve.
5. **CLV65-05** : reprendre la moitié « ni servies » de la garde 7 de la v64, ou dire pourquoi non.
6. **CLV65-06** : la mutation `N-bac-factice` tuée aussi quand `bwrap` est présent.
7. **CLV65-07** : le lecteur du registre des GO de la v66 applique **la même règle que la garde de calcul du dépôt de travail** (`.claude/hooks/garde_calcul.py`, `lire_go`) : une ligne qui répète un identifiant n'est admise que si elle est une extension (périmètre commençant par « extension », même type, accordée par Lazar, accordée après la première, échéance non plus lointaine), sinon refus ; essais sur le vrai `registres/go.md` (lecture seule) et sur des artefacts ; GO-2026-11-08-02 (45 USD) et GO-2026-11-10-10 (enveloppe 120 USD, part organisme 45) doivent être lus.
8. **CLV65-08** : aligner le relevé sur les mesures promises par le brouillon du texte (recherche de la loi plantée chez l'expérimentateur et le vérificateur, membre dominant du nul, empreinte d'engagement, intervalles de Wilson, jetons), ou lister précisément ce que le texte doit retirer.
9. **CLV65-09, CLV65-10** : garde 22 qui vérifie l'utilisateur réel du bac (ou réserve écrite si impossible sans `bwrap`) ; chemins de la configuration et pièces présents ou relatifs.
10. Dossier du texte scellé : garder `orchestrator/prereg/` (copie locale à l'octet de l'exemplaire du dépôt de travail ; pousser au dépôt public reste une décision de Lazar).
## Rendu
Commits sur `prep/organisme-v66-boucle-reelle-v1` ; paquet git (`git bundle`) et patch contre `cef5ea60` versés dans `/home/user/controle-ia-travail/docs/notes/organisme-boucle-reelle-v1/code-v66/` avec rapport `rapport-developpeur-organisme-v66-v1.md`, suite et banc rejoués, essai à blanc ; chaque fichier scellé. Aucun commit dans le dépôt de travail. Rapport final : commit, empreintes, comptes d'essais et de mutations, ce qui reste non éprouvé sans `bwrap`.
