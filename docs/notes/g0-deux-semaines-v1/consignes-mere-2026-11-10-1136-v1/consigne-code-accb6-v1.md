# Consigne : code de lecture du barreau 6 (`ACCB6`) et script d'énumération des états et des phrases — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-10 à 17:08 UTC (heure relevée par `date -u`). Tu es un sous-agent **neuf**, développeur ; tu n'as écrit ni le texte du barreau 6, ni T0.7, ni son module. Tu lis T0.7 : tu es exclu ensuite de tout rôle de lecteur de P3-bis. **Tu ne lis ni le verdict ni aucune sortie de `agregation-r1-v4`.**

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

**Exception à la règle 4, dans l'arbre `/home/user/wt-accb6` seulement** (branche `prep/accumulation-b6-code-v1`, depuis `101b458e` ; extraction réduite) : `git add`, `git commit` de tes seuls fichiers neufs, `git push -u origin prep/accumulation-b6-code-v1` (retentatives 2, 4, 8, 16 s) ; garde des secrets à 0 avant chaque commit (`git diff --cached | grep -cE '(sk-ant-[A-Za-z0-9]|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|hf_[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{12})'` doit rendre 0, enchaîné par `&&`) ; fin de chaque message : `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. **Aucun fichier existant modifié** ; **aucune fusion dans `main`** : la mère fusionne **après** le scellement de T0.7 (sinon `src/` de `main` cesserait d'égaler le commit du code de T0.7, R-2231). Mutations seulement sur des copies, avec `-o pythonpath=` et l'import tracé (R-2246). Bac à sable : `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/dev-accb6/`. Python : `/home/user/controle-ia-travail/.venv/bin/python`. Aucun appel de modèle, aucune donnée réelle (ni 7a, ni 7b, ni P3), aucune dépense. Disque ≈ 5 Go : nettoie à la fin. Sceller : `PYTHONPATH=/home/user/controle-ia-travail/src /home/user/controle-ia-travail/.venv/bin/python -m controle_ia.scellement sceller CHEMIN`.

## À lire (dans ton arbre ; empreintes à vérifier)
- `brouillons/accumulation-barreau6-v1/accumulation-barreau6-v1-brouillon2.md` (`9f070e31…`) : tout ce qu'il dit du code (entrées, calculs, états, phrases, gardes, registre `registres/accumulation-b6-v1.md`, clés `ACCB6`, sorties) ; journal v2 ; scripts de puissance et sous le nul (méthode).
- T0.7 candidat 1 (`brouillons/T0.7-sondes-v0-v1-candidat1.md`) et le module `src/controle_ia/t07/` (formes de `scores-actions-t07.npz`, `lecture-t07.json`, `sondes-t07.json`) ; `src/controle_ia/sondes/evaluation.py` (fonctions d'aire et d'intervalle, à **appeler**, pas à réimplémenter, si le texte le dit) ; registre `src/controle_ia/t07/registre_v1.py` (pour vérifier que les clés `ACCB6` ne vont jamais dans `registres/scellements-v1.md`).

## Mandat
1. Paquet neuf `src/controle_ia/accumulation_b6/` (fichiers `*_v1.py`) qui joue **exactement** le texte : lecture des seules entrées nommées, somme et maximum des dix scores d'action, aires d'épisode, Δ apparié par tâche, intervalle par blocs à 10 000 tirages au niveau 1 − 0,05/(2k), plancher d'épisode, prédicteurs triviaux, huit états, séquence (i-a) puis (ii), témoins, aiguillage G-1 à G-4, ordre (scellement avant `SCORES-T07`, lecture après `lecture-t07.json`), graines par `SeedSequence` (R9), manifeste ; chaque garde avec un **cas sain et un artefact** (R5) ; ligne de commande `python -m controle_ia.accumulation_b6.lecture_v1 …`.
2. Script `scripts/enumeration_etats_accb6_v1.py` : énumère tous les cas d'états **et de phrases** de la table du texte, sortie versée ; une ligne par cas, aucun cas sans phrase.
3. Essais `tests/test_accb6_*_v1.py` (jeux synthétiques seulement) ; banc de mutations sur copies ; joue tes essais et ceux de `tests/test_t07*.py` (aucun ne doit changer d'issue).
4. Commit, push ; rapport scellé `/home/user/controle-ia-travail/docs/notes/g0-deux-semaines-v1/accumulation-b6-code-v1/rapport-developpeur-accb6-v1.md` (seul chemin d'écriture hors de ton arbre) : commit proposé pour `COMMIT_CODE_ACCB6`, empreintes des fichiers, sortie de l'énumération, issues des essais et du banc, écarts au texte (le cas échéant, **couples proposés** au texte plutôt qu'un code qui s'en écarte).

## Rapport final à la mère
Commit, empreintes, énumération, essais, banc, couples proposés au texte, points ouverts.
