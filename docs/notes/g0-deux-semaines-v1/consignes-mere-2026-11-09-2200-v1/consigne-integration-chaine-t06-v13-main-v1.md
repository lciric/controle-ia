# Consigne : intégration de la chaîne T0.6 v13 dans `main` (bloquant B1 de la contre-lecture 3, R-2053) — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-09 vers 22:30 UTC (`date -u`). Destinataire : un **développeur neuf**, qui n'a écrit ni T0.6, ni T0.7, ni P3-bis, ni la chaîne, et n'est pas le lecteur exploratoire de 7a.

## Contexte

La contre-lecture 3 de T0.6 candidat 12 r3 (`prereg/contre-lectures/T0.6-organismes-v0-v1-candidat12-r3-cl3.md`, `3930d4f9…`, remarque B1) établit que la chaîne v13 (`src/controle_ia/t06/`, `scripts/lancer_t06_v13.sh`, `scripts/amorce_instance_t06_v11.sh`, `scripts/tests-cibles-t06-v3.txt`, …) est au commit `1609a4bf` (tête de `origin/prep/t06-explo-v2`) et **pas sur `main`** ; or le lancement préenregistré exige un commit de scellement S ancêtre d'`origin/main` qui contient l'amorce v11, et `exiger_code_cite` compare le commit cité à S sur tout l'arbre gelé. Ancêtre commun de `main` et de la branche : `067654576a21` (5 novembre) ; 67 commits côté branche, 672 côté `main`. Par les seuls noms de chemins, la fusion n'apporte aucun chemin sous embargo.

## Lieu de travail

- Arbre de travail **isolé** : `/home/user/integ-t06`, branche locale `prep/integration-t06-v13-main-v1`, partie de `ff3e9a09` (= `main`). Tu ne touches **jamais** `/home/user/controle-ia-travail` (arbre de la mère, où d'autres sous-agents travaillent), sauf pour y appeler l'interpréteur `/home/user/controle-ia-travail/.venv/bin/python` (environnement en cours d'installation : attendre que `…/.venv/bin/python -c "import torch, transformers, pytest"` réussisse).
- Permis dans `/home/user/integ-t06` seulement : `git merge`, `git add`, `git commit`, `git diff`, `git show`, `git log`, sur la branche `prep/integration-t06-v13-main-v1`. **Interdits** : `fetch`, `push`, `checkout`/`switch` d'une autre branche, `reset --hard` sur autre chose que ta propre branche, `rebase`, `stash`, toute action sur la branche `main` locale ou distante.

## Interdits (recopiés de `interdits-communs-v1.md`, même dossier)

1. **Fichiers et branches qu'on n'ouvre jamais** (ni lecture, ni affichage, ni copie, ni passage à un script, ni `git show`, ni `git ls-tree`, ni `git fetch`) : `diag/*/lecture-sondes-t06.json` de tout run, et nommément `diag/20261109-070232-t06-reel/lecture-sondes-t06.json` ; la lecture B de la course 7a et la branche `donnees/lecture-b-7a-quarantaine-v1` ; tout `diag/` et tout `runs/` de la course 7a (`20261109-070232-t06-reel`) et la branche `essai/t06-explo-v3` ; `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; les items, clés et réponses de l'étiqueteur (branche `prep/etiqueteur-v2-lecture-interrompue-reprise-v1`). Si la fusion fait apparaître un de ces chemins, **arrêter sans committer** et le signaler.
2. Secrets : jamais une valeur de clé ; jamais `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ`. Garde des secrets à 0 avant ton commit : `git diff --cached | grep -c -E 'sk-ant-api03-[A-Za-z0-9_-]{40,}|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[baprs]-|PRIVATE[ ]KEY|sk[-]proj-|AIza[0-9A-Za-z_-]{35}|sk[-][A-Za-z0-9]{40,}'`.
3. Aucun appel de modèle ni d'interface externe, aucune location, aucun `vastai`, aucune dépense, aucun réseau.
4. Refus d'un contrôle de permissions ou d'un classifieur : s'arrêter sur ce point, le rapporter tel quel ; ni contournement, ni reformulation.
5. Heures relevées par `date -u`.

## Travail

1. `git -C /home/user/integ-t06 merge --no-ff --no-commit 1609a4bf2c1572f72bb8542d81d963ac6a8481c4`.
2. **Conflits**, règles :
   - `registres/**` : garder la version de `main` en entier ; compter les lignes que la branche avait et que `main` n'a pas (numéros R-… seulement, au rapport) ; ne rien y ajouter.
   - fichier scellé (compagnon `.sha256`) : la version gardée doit égaler son compagnon ; s'il y a deux versions scellées différentes d'un même nom, arrêter et le signaler (R12).
   - code et essais (par exemple `.claude/hooks/garde_calcul.py`, `tests/test_cibles_invisibles_v1.py`) : union qui garde les deux comportements, sans comportement neuf ; chaque résolution décrite au rapport (lieu, deux versions, choix, raison).
   - aucune autre modification de fichier que la résolution des conflits.
3. **Contrôles avant commit** :
   - les fichiers de la chaîne v13 égaux à `1609a4bf` : `git diff --quiet 1609a4bf -- src/controle_ia/t06 scripts/lancer_t06_v13.sh scripts/amorce_instance_t06_v11.sh scripts/tests-cibles-t06-v3.txt` et les neuf empreintes du point 15 de `brouillons/T0.6-organismes-v0-v1-candidat12-r3.md` ;
   - liste, par catégorie, de ce qui diffère entre `1609a4bf` et l'arbre fusionné **dans le périmètre gelé** d'`exiger_code_cite` (tout l'arbre hors `prereg`, `brouillons`, `registres`, `docs`, `diag`, `runs`, `donnees`, `livrables`, `papiers`, `traces`, `CLAUDE.md` ; vérifier la liste exacte dans `src/controle_ia/harnais/validation_reelle.py`) ;
   - `PYTHONPATH=src python -m controle_ia.scellement verifier-arbre .` dans `/home/user/integ-t06` (seule l'orpheline `consigne-argon-question-mere-v3.txt.sha256` est attendue).
4. Commit de fusion sur `prep/integration-t06-v13-main-v1`, message : « Intégration de la chaîne T0.6 v13 (1609a4bf) dans main (B1, R-2053) », terminé par les deux lignes :
   `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`
   `Claude-Session: https://claude.ai/code/session_01QPDgKgACWyCkCN8HjqwNXy`
5. **Suite ciblée v3**, sur l'arbre fusionné, exactement comme l'amorce v11 la joue (lire `scripts/amorce_instance_t06_v11.sh` autour de la l. 488 : liste lue dans `scripts/tests-cibles-t06-v3.txt`, `PYTHONPATH=src python -m pytest -q -p no:cacheprovider --color=no …`), avec l'interpréteur de `.venv` de la mère, depuis `/home/user/integ-t06`. Relever passés / échoués / sautés et comparer à 2 022. Pour chaque échec : cause, et classement (a) artefact de fusion, (b) défaut connu (R-2042 : `premier_test_ia/run_v2.py::executer` → `charger_invite` non examiné par l'inventaire), (c) neuf. **Ne modifier ni code ni essai pour faire passer** : proposer la correction au rapport (texte, fichier, nom neuf si R12 l'exige ; l'empreinte de la liste v3 est en dur dans l'amorce v11).
6. **Essai à blanc des gardes** autant que possible hors ligne : `exiger_code_cite` (commit cité = ton commit de fusion, HEAD = le même, puis HEAD = un commit qui ne toucherait qu'un fichier de `docs/` : doit passer ; un commit qui toucherait `src/` : doit refuser), en travaillant dans un clone temporaire de `/home/user/integ-t06` fait sous `/tmp` (pas dans le dépôt) ; dire ce qui n'a pas pu être joué (préenregistrement non scellé).

## Sorties

- Le commit de fusion (local, non poussé) et un second commit sur la même branche avec le rapport `docs/notes/g0-deux-semaines-v1/integration-t06-v13-main-v1/rapport-integration-v1.md` et son compagnon `.sha256` : conflits et résolutions, contrôles, compte des essais et échecs classés, essai à blanc des gardes, ce qui reste avant le scellement de T0.6.
- Réponse finale à la mère : identifiants des deux commits, empreinte du rapport, compte des essais (passés / échoués / sautés), échecs classés, corrections proposées.
