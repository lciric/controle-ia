# Consigne — socle de preuves de l'entretien, v4 (corrections de la contre-lecture) — v1

- **Session mère** (`session_01VJdZpSMxSdk2SJ1ScmdfNv`). Tu es un sous-agent **neuf** (rédacteur Opus) ; tu n'as écrit ni le socle v1 à v3, ni sa contre-lecture. Dépôt `/home/user/controle-ia-travail` (`main`), `PYTHONPATH=src`, `.venv/bin/python`. Sceller : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller CHEMIN`. Français ; heures par `date -u`. Bac à sable : `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/<ton-nom>/`.
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

## Interdits propres
Cloison du bras (R-2152, R-2170) : aucun document du bras, aucune branche du bras ni de la session-dépôt (rien ne s'y lit ni ne s'y liste) ; rien sur le mode tenu à l'écart ; aucune sortie scellée non lue ; **aucun taux de calibration** (nombres bruts 33, 7, 6 seulement, R-2195) ; niveau méthode (R-607).
## Objet et sources
Écrire `brouillons/entretien-taif-v3/socle-preuves-entretien-v4.md` et son journal `socle-preuves-entretien-v4-journal.md` (v3 intacte, R12) : socle v3 (`b9377f1d…`) + les 50 couples C01 à C50 de `prereg/contre-lectures/socle-preuves-entretien-v3-cl1.md` (`3a1df795…`), **appliqués par programme** (chaque texte ancien présent une fois, arrêt sinon). Les couples d'état (C01 à C33 notamment) sont à **relever au moment de l'application** contre `registres/decisions.md` jusqu'à sa dernière ligne et `registres/go.md` (GO-2026-11-10-10 inscrit R-2206 ; base (A) scellée R-2216 ; validité de l'adaptateur b3 R-2210 ; lecture large de GO-07 R-2207 ; CLBA-04 (a) R-2211 ; consigne d'audit b3 R-2212 ; code v65 contre-lu, v66 en cours R-2215 ; sections v4 R-2217 ; réponses pour le registre des prédictions R-2218). Points ouverts du contre-lecteur : « monté, rien n'a encore tourné » (§ 2.5, bras) ne peut être revérifié : remplace-le par « état du bras non vérifiable par la mère (cloison) » ; la synthèse de l'état de l'art niveau 3 reste provisoire : dis-le là où elle est citée.
## Rendu
Les deux fichiers scellés ; aucun commit. Rapport final : chemins, empreintes, couples appliqués et modifiés (raison), statuts relevés, ce qu'un vérificateur court doit relire.
