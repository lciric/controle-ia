# Consigne — essai CLC-04 de T0.7 (« quatre concepts en mode réel » par `ouvrir`) — v1

- **Session mère** (`session_01VJdZpSMxSdk2SJ1ScmdfNv`), écrite le 2026-11-10 à 13:37 UTC (heure relevée par `date -u`). Tu es un sous-agent **neuf**, développeur d'essais. Tu n'as écrit ni T0.7, ni son module, ni ses contre-lectures. Tu lis le code de T0.7 : tu es exclu ensuite de tout rôle de lecteur de P3-bis.
- **Arbre** : `/home/user/wt-t07-clc04`, branche `prep/t07-essai-clc04-v1`, partie du commit `39bb7ba8` de `main` ; arbre **réduit** (`src/`, `tests/`, `scripts/`, fichiers de la racine, `registres/go.md`) ; ne change pas l'extraction. **Exception à la règle 4, dans cet arbre seulement** : `git add` et `git commit` des seuls fichiers neufs de la tâche, puis `git push -u origin prep/t07-essai-clc04-v1` (retentatives après 2, 4, 8, 16 s) ; rien d'autre (ni `checkout`, ni `fetch`, ni `merge`, ni `rebase`, ni `reset`). Avant chaque commit, la garde des secrets doit être à 0 : `git diff --cached | grep -cE '(sk-ant|sk-[A-Za-z0-9]{20,}|ghp_|hf_[A-Za-z0-9]{20,}|AKIA)'` doit rendre 0. Fin de chaque message de commit : la ligne `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.
- **Bac à sable** : `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/clc04/` (`--basetemp`, `TMPDIR`, copies mutées). Python : `/home/user/controle-ia-travail/.venv/bin/python`, `PYTHONPATH=src` depuis l'arbre. Sceller : `PYTHONPATH=/home/user/controle-ia-travail/src /home/user/controle-ia-travail/.venv/bin/python -m controle_ia.scellement sceller CHEMIN`. Disque serré (≈ 4,8 Go libres) : nettoie le bac à sable à la fin. Français ; heures par `date -u`.
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

## Tâche
1. Lire : `docs/notes/g0-deux-semaines-v1/t07-module-v2/contre-lecture-code-t07-option-c-courte-v1.md` (dans `/home/user/controle-ia-travail/`, `7a327462…`), ligne **CLC-04** et § de la mutation m13 ; `src/controle_ia/t07/lecture_v2.py` (`ouvrir`, l. ≈ 440-560 ; `lire_jeux_et_phrases`) ; les essais `tests/test_t07_option_c_concepts_v1.py` (dont `test_trois_concepts_en_mode_reel_refus_quatre_exiges`, qui donne le minimum à la main), `tests/test_t07_corrections_cl1_v1.py`, `tests/test_t07_sondes_neuves_v1.py` et leurs bancs (fixtures).
2. Écrire **un seul fichier neuf** `tests/test_t07_ouvrir_reel_concepts_v1.py` qui passe **par `ouvrir`**, configuration en **mode réel**, étape A complète, ligne des phrases des concepts antérieure à la fermeture :
   - **artefact** : phrases de **trois** concepts → refus motivé (le motif du minimum de quatre apparaît dans les motifs ou l'arrêt que rend `ouvrir`) ;
   - **cas sain** : phrases de **quatre** concepts → ce motif est absent, phrases lues (état « lues ») ;
   - si possible, **contre-épreuve** : même artefact en mode jouet (`mode` ≠ `reel`, minimum 1) → pas de refus de minimum.
   Réutilise les fixtures existantes par import (comme le font les autres fichiers `test_t07_*`) ; **aucun changement sous `src/`** ni dans un fichier d'essai existant (R12).
3. **Mutation m13** : dans une **copie** de `src/` sous ton bac à sable (jamais dans l'arbre), remplace à `lecture_v2.py` `4 if config["mode"] == "reel" else 1` par `1`, joue ton fichier avec `PYTHONPATH` pointé sur la copie : il doit **échouer** (mutation tuée). Joue-le aussi sur la copie non mutée : il doit passer. Écris les deux codes de sortie.
4. Joue ensuite, dans l'arbre, `tests/test_t07*.py` et `tests/test_verifier_jeux_synthetiques_t07_v2.py` (`-p no:cacheprovider --basetemp` au bac à sable) ; rapporte passés, sautés, échecs attendus (`xfail`) et échecs, avec le nom de chaque échec.
5. Commit (fichier d'essai seul), push ; vérifie et écris : `git diff --quiet 37485ce50601b7d7ff9035bc34c734ec689ca731 HEAD -- src` (code 0 exigé : `src/` égal au commit contre-lu) et `git diff --stat 37485ce50601b7d7ff9035bc34c734ec689ca731 HEAD -- tests` (liste attendue : `tests/test_lanceur_durable_v5_a1v4.py` et ton fichier).
6. **Rapport** : `/home/user/controle-ia-travail/docs/notes/g0-deux-semaines-v1/t07-module-v2/rapport-essai-clc04-v1.md`, scellé (seul chemin d'écriture hors de ton arbre et du bac à sable) : commit et empreinte du fichier d'essai, résultats des points 3 à 5, écarts, points ouverts.

## Rapport final à la mère
Chemins, empreintes, commit poussé, verdict en une ligne (« CLC-04 levé » ou non), points ouverts.
