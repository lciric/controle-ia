# Consigne — contre-lecture du socle de preuves de l'entretien, v3 — v1

- **Session mère** (`session_01VJdZpSMxSdk2SJ1ScmdfNv`). Tu es un sous-agent **neuf**, contre-lecteur au sens de R2, **d'un autre modèle que le rédacteur** (Opus 5.5) : N-052. Dépôt `/home/user/controle-ia-travail` (`main`), `PYTHONPATH=src`, `.venv/bin/python`. Sceller : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller CHEMIN`. Français ; heures par `date -u`. Bac à sable : `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/<ton-nom>/`.
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

## Interdits propres à cette tâche
Cloison du bras (R-2152, R-2170) : aucun document de la session du bras ; rien sur le mode tenu à l'écart. Aucune sortie scellée non lue (rien sous `donnees/`, aucune branche `donnees/…`, aucune quarantaine). Texte pour un jury : aucun chiffre sans source scellée ; **aucun taux de calibration** (R-2185 ; nombres bruts seulement, R-2195) ; niveau méthode pour toute attaque (R-607).

## À lire (vérifie les empreintes)
`brouillons/entretien-taif-v3/socle-preuves-entretien-v3.md` (`b9377f1d…`) et son journal (`2276733f…`) ; la v2 (`socle-preuves-entretien-v2.md`, `3f078bca…`) et la contre-lecture de la v1 (`socle-preuves-entretien-v1-contre-lecture-v1.md`, `48c7fcc2…`) ; les lignes R-2133, R-2156, R-2177, R-2180 à R-2190 et R-2191 à la dernière du registre ; chaque source citée par le socle.

## Ce que tu vérifies
Pour chaque affirmation : source existante, empreinte juste, sens exact (ni plus fort, ni plus faible) ; corrections du niveau 3 de l'état de l'art bien portées (B3 de R-2177 : quatre corrections du socle v2 ; collisions et occupations partielles de R-2180, R-2181) ; voies d'ouverture du témoin positif (normale et au rendez-vous, R-2133) ; entretien visé le 27 (R-2130) ; état à jour (GO-2026-11-10-10 inscrit, R-2206 ; lecture large de GO-07, R-2207 ; nombres bruts sans taux) ; réserves à côté des résultats.

## À écrire
`prereg/contre-lectures/socle-preuves-entretien-v3-cl1.md`, scellé : verdict (« utilisable pour l'entretien », « après corrections » avec couples exacts, ou « non utilisable »), constats CLS-01… Aucun commit. Rapport final : verdict en trois lignes, bloquants, chemin et empreinte.
