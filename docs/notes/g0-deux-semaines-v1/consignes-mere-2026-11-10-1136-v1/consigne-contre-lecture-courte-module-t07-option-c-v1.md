# Consigne — contre-lecture courte du module T0.7 option (c) (différentiel 8ae9fc44..37485ce5) — v1

- **Session mère** (`session_01VJdZpSMxSdk2SJ1ScmdfNv`). Tu es un sous-agent **neuf**, contre-lecteur de code, **d'un autre modèle que le développeur** (Opus 5.5) : N-052. Tu n'as écrit ni T0.7, ni le module, ni ses contre-lectures. Tu lis T0.7 : tu es exclu ensuite de tout rôle de lecteur de P3-bis.
- Arbre : `/home/user/wt-t07-module-v2` (branche `prep/t07-module-v2`, poussée, tête `41648f2e`) ; **exception à la règle 4** : dans cet arbre seulement, essais ciblés, banc de mutations et répétition jouet permis, `--basetemp` et `TMPDIR` dans ton bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/<ton-nom>/` ; aucun commit, aucun `checkout`, aucun `push`, aucun `fetch`. Disque serré : nettoie à la fin. Sceller : `PYTHONPATH=src /home/user/controle-ia-travail/.venv/bin/python -m controle_ia.scellement sceller CHEMIN`. Français ; heures par `date -u`.
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

## À lire
- Rapport du développeur : `docs/notes/g0-deux-semaines-v1/t07-module-v2/rapport-complementaire-5-option-c-v1.md` (`e58be6c9…`), banc `banc-mutations-t07-option-c-v1.json` (`0b54c163…`), répétition `repetition-jouet-variante-b-v3/` (résumé `6c6f2c8d…`, journal `7ca315da…`), script `scripts/etape_a_t07_variante_b_v2.sh` (`e68d3306…`).
- `git diff 8ae9fc44 37485ce5 -- src tests scripts` ; R-2153, R-2155, R-2166, R-2183 ; `brouillons/T0.7-sondes-v0-v1-brouillon21.md` (`f7dcb226…`, passages sur l'option (c), R15, T7-P9, plancher de concept, ordre de l'étape A).
- Contre-lecture courte précédente : `docs/notes/g0-deux-semaines-v1/t07-module-v2/contre-lecture-code-t07-v3-differentiel-court.md` (`d0fe9053…`).
## Ce que tu vérifies
1. Chaque exigence de R-2166 : ligne de code, essai sain, artefact (R5).
2. Les deux gardes neuves et le défaut corrigé du script v2 (`registres/go.md` recopié) ; rejoue les essais `tests/test_t07*.py` et `tests/test_verifier_jeux_synthetiques_t07_v2.py`, le banc (12 mutations) et la répétition si le disque le permet.
3. **Miroir de `familles_v2`** : le commit `8cb539f9` est maintenant présent dans le dépôt local (récupéré par la mère depuis `prep/t06-ordre-course-v2`, il **n'est pas** atteignable depuis `main`) : rejoue `tests/test_t07_lecture_v1.py::test_mahalanobis_miroir_egal_a_familles_v2_au_commit_8cb539f9` et dis s'il passe ; puis donne ton avis sur la voie pour l'instance (rendre `8cb539f9` atteignable depuis `main` par une fusion qui ne change pas l'arbre, ou mesurer la ligne d'essais dans un clone de l'instance, ou autre).
4. Points ouverts 2 à 4 du rapport (R15 écrite seulement si les scores sont ouverts ; lecture du « plancher de concept gardé au manifeste » ; docstring périmée).
## À écrire
`docs/notes/g0-deux-semaines-v1/t07-module-v2/contre-lecture-code-t07-option-c-courte-v1.md`, scellé : verdict (« `CODE-T07` inscriptible au commit `37485ce5` », « après corrections » avec la liste exacte, ou « non inscriptible »), constats CLC-01… Aucun commit. Rapport final : verdict en trois lignes, bloquants, chemin et empreinte.
