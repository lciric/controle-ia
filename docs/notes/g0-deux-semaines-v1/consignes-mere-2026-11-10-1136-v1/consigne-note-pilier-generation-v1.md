# Consigne : note de conception du pilier « génération » de la couche 4 (mathématiques nouvelles pour le contrôle, l'alignement et l'interprétabilité mécaniste) — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-10 à 14:11 UTC (heure relevée par `date -u`). Pas (c) de l'ordre de Lazar (R-2199 : « (a), puis (b), puis (c) à partir de ce qu'on aura appris ») ; (a) fait (R-2226), (b) dessiné et vérifié (brouillon 3, R-2240 ; GO de l'outillage en attente). Destinataire : un **rédacteur neuf**, qui n'a écrit ni la synthèse du tour 2, ni le dessin de l'essai Lean, ni le programme de l'organisme. **Ce texte est une proposition : un nœud chez Lazar** ; N12 (b) (R-959) garde les couches 3 et 4 fermées jusqu'aux résultats de l'étape 2 : rien n'est ouvert, rien n'est lancé, aucune dépense.

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

Exception à la règle 4 : aucune. Tu n'écris que sous `docs/notes/ideation-organisme-v1/pilier-generation-v1/` et dans ton bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/pilier-generation/`. Aucun commit, aucun appel de modèle ni d'interface, aucun réseau. Sceller : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller CHEMIN`.

## Règles de fond
- **R7** : aucun chiffre de l'état de l'art sans PDF empreinté au dépôt, page citée ; sinon, le dire « non vérifié » et sans chiffre. **R8** : une zone qui paraît vierge est une question, pas un trou ; les antériorités probables (systèmes de preuve automatique, formalisation automatique, agents de recherche mathématique) sont nommées comme **questions à vérifier**, sans affirmation.
- Ne rien revendiquer : la note dit ce qu'il faudrait mesurer pour pouvoir dire qu'un résultat est **neuf**, **vrai** et **utile** au contrôle, à l'alignement ou à l'interprétabilité mécaniste.

## À lire (empreintes à vérifier)
- Registre `registres/decisions.md` : R-920, R-959 (N12 (b), N13), R-2199, R-2226, R-2230, R-2236, R-2240 ; `docs/decisions/decision-N-044-v1.md`, `decision-N-045-v2.md`, `decision-N-064-v1.md` (O2 resserrée, e-valeurs, POPPER, Ladder) et N-065 (organisme comme second terrain du papier C) par `git grep -n "N-065" -- registres/decisions.md`.
- Synthèse du tour 2 : `docs/notes/ideation-organisme-v1/course-2/collisionneur-n12-n13-v1/synthese-n12-n13-tour2-v1.md` (`6ef6bc2e…`).
- Essai Lean : `brouillons/couche4-essai-preuve-formelle-v1/essai-preuve-formelle-devis-v1-brouillon3.md` (`717259ed…`), contre-lecture 1 et vérification courte sous `prereg/contre-lectures/essai-preuve-formelle-devis-v1-*`.
- Programme de l'organisme v3 : `docs/notes/rapports-directeur/programme-organisme-complet-v1/programme-organisme-complet-v3.md` (`bbde32b7…`), couche 4 et ce qui touche aux juges ; inventaire des idées v4 (`docs/notes/rapports-directeur/programme-organisme-complet-v1/inventaire-idees-organisme-v4.md`).

## Mandat : note de conception (proposition), en français, sans acronyme non développé
1. **Objet** : ce que le pilier produirait (conjectures, lemmes, démonstrations, contre-exemples) et pour quelles questions du programme (contrôle, alignement, interprétabilité mécaniste) ; trois à cinq exemples de questions **du programme lui-même** où un énoncé formel aiderait, chacun avec ce qu'il changerait.
2. **Chaîne** : proposeurs → formalisation → Lean comme arbitre (avec ce que l'essai de (b) mesure de ses classes d'erreurs) → juge de nouveauté → juge d'utilité → relecture humaine ; pour chaque maillon : entrée, sortie, garde, mode d'échec connu (formalisation infidèle, énoncé trivial ou vide, théorème déjà connu reformulé, triche de Goodhart sur l'arbitre).
3. **Mesures** : comment savoir qu'un énoncé est **neuf** (banque d'énoncés connus plantés, contamination, recherche d'antériorité), **vrai** (Lean, contrôles de fidélité), **utile** (critère lié à une hypothèse du programme) ; oracle planté et coût, jamais le verdict d'un juge seul (N-058) ; ce qui est préenregistrable.
4. **Dépendances** : ce qu'il faut de l'essai de (b) (classe d'erreurs, coût, cloison), de l'étape 2 (N12 (b)), du papier C (juges sous attaque, N-065) ; ce qui ne peut pas commencer avant.
5. **Coûts** : ordres de grandeur seulement, chaque hypothèse de prix nommée et non vérifiée, aucun devis.
6. **Risques et ce qu'on ne dira pas.**
7. **Décisions pour Lazar**, au format : décision en une phrase ; enjeu ; 2 ou 3 options (avantage, inconvénient) ; recommandation et confiance ; défaut (aucun si dépense ou ouverture de couche).

## Sorties (noms neufs, scellées)
`docs/notes/ideation-organisme-v1/pilier-generation-v1/note-conception-pilier-generation-v1.md` et `…-journal-v1.md` (sources lues avec empreintes, affirmations et leur renvoi, questions ouvertes). Rapport final : chemins, empreintes, décisions proposées en une ligne chacune.
