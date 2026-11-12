# Consigne : essai de la garde « tirages dégénérés » (GARDES-CODE-01), puis ordre d'exécution de l'étape A de T0.7, brouillon 4 — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-10 à 14:57 UTC (heure relevée par `date -u`). Tu es un sous-agent **neuf**, développeur. Tu n'as écrit ni T0.7, ni son module, ni ses ordres d'exécution, ni leurs contre-lectures. Tu lis T0.7 : tu es exclu ensuite de tout rôle de lecteur de P3-bis.

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

**Exception à la règle 4, dans l'arbre `/home/user/wt-t07-degeneres` seulement** (branche `prep/t07-essai-degeneres-v1`, partie de `06deda58` de `main` ; extraction réduite : `src/`, `tests/`, `scripts/`, `brouillons/`, racine, `registres/go.md`) : `git add` et `git commit` des seuls fichiers neufs de la partie 1, puis `git push -u origin prep/t07-essai-degeneres-v1` (retentatives 2, 4, 8, 16 s) ; garde des secrets à 0 avant chaque commit (`git diff --cached | grep -cE '(sk-ant-[A-Za-z0-9]|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|hf_[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{12})'` doit rendre 0 ; la commande enchaîne par `&&`) ; fin de chaque message : `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. Bac à sable : `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/dev-t07-ordre-b4/`. **Toute mutation se fait sur une copie de `src/` et se joue avec `-o pythonpath=` et une trace de l'import réel** (R-2246 : `pyproject.toml` met `src` en tête). Disque serré (≈ 5 Go libres) : nettoie ton bac à sable à la fin. Python : `/home/user/controle-ia-travail/.venv/bin/python`. Sceller : `PYTHONPATH=/home/user/controle-ia-travail/src /home/user/controle-ia-travail/.venv/bin/python -m controle_ia.scellement sceller CHEMIN`.

## Partie 1 — essai GARDES-CODE-01 (avant tout le reste)
Lire : `/home/user/controle-ia-travail/prereg/contre-lectures/T0.7-sondes-v0-v1-brouillon22-cl-orchestree-v1.md` (`47537dfa…`), ligne GARDES-CODE-01 ; brouillon 22 de T0.7 (`brouillons/T0.7-sondes-v0-v1-brouillon22.md`, `8b84cba5…`), « Module de lecture » l. ≈ 2427-2438 et liste d'arrêt l. ≈ 1864 ; `src/controle_ia/t07/lecture_v1.py` l. ≈ 860-880 et le paquet gelé `src/controle_ia/sondes/`.
Écrire **un seul fichier neuf** `tests/test_t07_tirages_degeneres_v1.py` : **artefact** (jeu dont une seule tâche porte les positifs → plus de 1 % de tirages dégénérés → la lecture concernée passe en « échec », motif écrit, **les autres lectures continuent**) et **cas sain** à côté ; aucun changement sous `src/`. Mutation qui retire ou affaiblit la reprise de l'arrêt, jouée sur une copie : l'essai doit échouer. Joue ensuite `tests/test_t07*.py` et `tests/test_verifier_jeux_synthetiques_t07_v2.py` (`-p no:cacheprovider --basetemp` au bac à sable) ; commit, push ; écris `git diff --quiet 37485ce50601b7d7ff9035bc34c734ec689ca731 HEAD -- src` (code 0 exigé).

## Partie 2 — ordre d'exécution de l'étape A (variante B), brouillon 4
Lire : `/home/user/controle-ia-travail/docs/procedures/ordre-execution-etape-a-t07-v1-brouillon3.md` (`b053a220…`) ; contre-lecture courte `docs/notes/g0-deux-semaines-v1/t07-module-v2/contre-lecture-code-t07-v3-differentiel-court.md` (`d0fe9053…`, O-1 à O-6) ; rapport `docs/notes/g0-deux-semaines-v1/t07-module-v2/rapport-complementaire-5-option-c-v1.md` (`e58be6c9…`, script v2, point 8) ; contre-lecture courte `docs/notes/g0-deux-semaines-v1/t07-module-v2/contre-lecture-code-t07-option-c-courte-v1.md` (`7a327462…`, CLC-03, CLC-08) ; `scripts/etape_a_t07_variante_b_v2.sh` ; registre R-2153, R-2220, R-2229, R-2231, R-2241, R-2246, R-2249 ; `registres/go.md` (GO-2026-11-10-04, GO-2026-11-10-06).
Écrire `/home/user/controle-ia-travail/docs/procedures/ordre-execution-etape-a-t07-v1-brouillon4.md` (seul chemin d'écriture hors de ton arbre et du bac à sable ; scellé ; brouillons 1 à 3 intacts), qui :
- porte O-1 à O-6 tels que le script v2 les règle (et dit ce qui reste) ; O-4 : `ANT0` = dépense inscrite sous les deux lignes ;
- porte l'option (c) des concepts (passage « sans concepts », `PERIMETRE` sans `CONCEPTS`) et la règle de C7 (R-2231 : C7 = commit de `main` dont `src/` égale `37485ce5` et dont `tests/` égale celui de S7 ; `CODE-T07-v2.json`) ;
- borne le filtre d'inventaire aux étiquettes `t06…` et `t07…` (CLO-08, R-2249) ;
- écrit `ATTENDU` (ligne attendue des essais) **mesurée dans un clone fait comme celui de l'instance** (O-1 : `--single-branch --branch main` ou la méthode exacte du script), après ta partie 1 et sur ta branche ; si la place disque ne le permet pas, écris le marqueur `<<ATTENDU_ESSAIS_T07>>` avec la commande exacte et dis pourquoi ;
- cite T0.7 par la ligne `SCELLEMENT-T07`, jamais par son empreinte.
Si le script v2 doit changer, **ne le modifie pas** : écris le constat et la correction proposée (une version v3 éventuelle est une décision de la mère).

## Rapport final à la mère
Partie 1 : commit, empreinte de l'essai, issue (cas sain, artefact, mutation), compte des essais. Partie 2 : chemin et empreinte de l'ordre brouillon 4, `ATTENDU` ou marqueur, ce qui reste ouvert. Points ouverts. Rapport scellé aussi sous `docs/notes/g0-deux-semaines-v1/t07-module-v2/rapport-essai-degeneres-et-ordre-b4-v1.md`.
