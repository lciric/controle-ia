# Consigne : audit symétrique (R4) du verdict de P3 — règle « au-dessus du plancher » — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-10 à 23:54 UTC (heure relevée par `date -u`). Mot de Lazar (R-2285) : « l’audit du verdict de P3, qui a été lu avec la même règle que T0.7 […] : go ». Motif : l'audit de T0.7 (R-2270, R-2271) trouve que la règle « borne basse de l'aire de la sonde > quantile du plancher » fait 4 à 9 fois le nominal de fausses lectures quand le plancher porte un signal commun ; la même règle a servi aux sondes de P3. Tu es un **analyste neuf** : tu n'as écrit ni P3, ni son verdict, ni T0.7, ni les audits de T0.7. Ayant lu T0.7 et P3, tu es exclu ensuite de tout rôle de lecteur de P3-bis.

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

Exception à la règle 4 : aucune. Bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/audit-p3/` (`OPENBLAS_NUM_THREADS=1`, calcul borné à ≈ 60 min). **Seules les données de P3 sont permises** (ni 7a, ni 7b, ni P3-bis) ; si une pièce de P3 se trouve sous un chemin interdit, ne l'ouvre pas et dis-le. Aucun appel de modèle, aucune dépense. Sceller : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller CHEMIN`.

## À lire (empreintes à vérifier)
- Verdict de P3 : `docs/verdicts/verdict-P3-premier-test-i-a-v2.md` (`05e896da…`) et ses fichiers de travail ; préenregistrement de P3 (cité par le verdict) ; code gelé de P3 (`src/controle_ia/premier_test_ia/` au commit `7a54d431d89745839220f882b41b13e8c62ecfdd` : `statistiques`, `figees`, `conditions`).
- Audits de T0.7 : `docs/notes/g0-deux-semaines-v1/t07-module-v2/erreur-premiere-espece-lectures-decisives-t07-v1.md` (`8e996ab0…`) et `…-v2.md` (`5ccf0940…`), avec leurs scripts (méthode, prototype du remède).

## Mandat
1. Écris la règle exacte que P3 a appliquée à ses lectures décisives (numéros de ligne du code gelé et du texte) : est-ce la même que celle de T0.7 (borne basse percentile de l'aire de la sonde comparée au quantile d'un plancher de directions tirées) ? Effectifs, niveau, nombre de directions, multiplicité.
2. Simule sous le nul de P3 (lois supposées, aux effectifs et réglages de P3, **en appelant son code gelé**) : taux de fausse lecture par sonde et pour la conclusion du verdict, selon la force du signal commun du plancher ; Clopper-Pearson.
3. Si les scores de P3 sont au dépôt sous un chemin permis : rejoue sur eux la règle de P3 (doit retrouver le verdict) et la règle du remède (a) (différence appariée, prototype `remede_a_prototype_v1.py`) ; dis si les conclusions du verdict tiennent, en chiffres.
4. **Tu ne réécris pas le verdict** : tout changement de conclusion est une réserve ou un nœud pour Lazar, écrit comme tel.

## Sortie
`docs/notes/g0-deux-semaines-v1/audit-p3-regle-plancher-v1/audit-verdict-p3-regle-plancher-v1.md` et pièces, scellés. Rapport final : chemin, empreinte, verdict de l'audit en une ligne (« conclusions tenues », « tenues avec réserve » ou « en question »), chiffres clés.
