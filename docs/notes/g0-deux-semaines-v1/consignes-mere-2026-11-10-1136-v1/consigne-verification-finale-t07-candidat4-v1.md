# Consigne : vérification finale du candidat 4 de T0.7, de l'ordre brouillon 8 et du différentiel de code `7e23a554..a621dcd3` — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-11 à 05:22 UTC (heure relevée par `date -u`). Tu es un sous-agent **neuf**, d'un autre modèle que le rédacteur et le développeur (Opus 5.5) : N-052 ; tu n'as écrit ni T0.7, ni son code, ni ses ordres, ni aucune de leurs contre-lectures ou vérifications. Ayant lu T0.7, tu seras exclu ensuite de tout rôle de lecteur de P3-bis.

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

Exception à la règle 4 : aucune, sauf un arbre clairsemé à toi pour les essais du code (ci-dessous) : `git worktree add --no-checkout --detach /tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/verif-finale-t07/arbre a621dcd3b929ce3ebd615fa852d4a7f5c103071d`, `git sparse-checkout init --no-cone`, lignes `/*`, `!/*/`, `/src/`, `/tests/`, `/scripts/` dans le fichier de `git rev-parse --git-path info/sparse-checkout`, `git checkout --detach a621dcd3…` ; retiré à la fin (`git worktree remove --force`). Bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/verif-finale-t07/` ; pytest avec `--basetemp` dans ce bac (disque ≈ 2 Go). Aucun appel de modèle, aucune dépense, aucun `rm -rf`. Sceller ta sortie par `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller <fichier>`. Le conteneur redémarre parfois : écris ta sortie tôt et complète-la au fil de l'eau.

## À lire (empreintes à vérifier)
- Décisions R-2311 à R-2314 de `registres/decisions.md` (ces lignes) ; R-2285 (mot de Lazar).
- Vérification courte du candidat 3 `prereg/contre-lectures/T0.7-sondes-v0-v1-candidat3-verification-courte-v1.md` (`cfeeae9c…`, couples VC3-A à VC3-D).
- Contre-lecture courte `docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/contre-lecture-courte-corrections-plancher-v3-v1.md` (`6f376911…`) ; rapport v3 du code `…/rapport-code-plancher-v3-v3.md` (`be2c86e2…`), répétition jouet v4 (résumé `c36839fe…`, journal `98412f28…`), bancs v5 et du script v4, au même dossier.
- Candidat 3 (`1b9b75f0…`) et candidat 4 `brouillons/T0.7-sondes-v0-v1-candidat4.md` (`cad20c1d…`) et ses pièces (couples `0c74d25a…`, script, journal) ; ordre brouillon 7 (`d799a01b…`) et brouillon 8 `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon8.md` (`24dc8df6…`) et son script.

## Mandat A — texte et ordre
1. Rejoue les scripts du candidat 4 (sur une copie du candidat 3) et de l'ordre 8 (sur une copie du brouillon 7) : textes à l'octet.
2. G4-01, G4-02 égaux aux couples VC3-A, VC3-B ; G4-03 (arrêt technique) dans le périmètre de R-2285 ? lectures confirmées par R-2314 (2) bien écrites ? Aucun autre changement gelé (par programme).
3. VC3-C, VC3-D appliqués tels quels à l'ordre ; script v4 (`4b17d1f0…`) et commit `a621dcd3` cités partout où il faut ; plus aucune mention « en cours » non historique.
4. **P14** : R-2314 (4) le restreint au **nombre de lignes** des mesures de 7b (script qui n'imprime qu'un entier ; aucune colonne lue, aucune ventilation). L'ordre 8 dit « colonne `jetons_notes` seule » : écris le **couple exact** qui l'aligne sur R-2314 (4), pour l'ordre et pour le candidat s'il en parle.
5. 26 empreintes du module au commit `a621dcd3`, configuration v8 `0f32c6de…`, nombres de CLC-P3-01 (400 et 1 591 exemples ; 4,3 et 1,3 ; 0,5 % et 1 %) renvoyés à leurs pièces (R6).

## Mandat B — code `7e23a554..a621dcd3` (contre-lecture courte)
6. Lis la différence (`git diff 7e23a554 a621dcd3`) : `lecture_v4 controle-avant-ouverture` (lecture seule ? une faute hors garde rend-elle bien le code 2 ?), `revision_au_cache` durcie (cas sain non refusé à tort ?), script v4 (étape 8 avant toute ouverture ; formes sûres sous `set -u` ; `CPU_ESSAI` refusé hors essai), essais neufs (comportement, non miroir).
7. Depuis ton arbre : `PYTHONPATH=<arbre>/src /home/user/controle-ia-travail/.venv/bin/python -m pytest -q -o pythonpath= --basetemp=<bac>/pytest-tmp tests/test_t07_plancher_v3_*.py` (import tracé ; si un essai lit la configuration v8 hors de l'extraction, pose une copie non suivie et déclare-le) ; quelques mutations neuves sur copies.

## Verdict
« scellable » (une fois C7 fixé par la mère, `ATT` mesuré et CODE-T07 écrit) ou « après corrections » (couples exacts) ou « nœud » ; et pour le code : « sans défaut bloquant » ou la liste.

## Sortie
`prereg/contre-lectures/T0.7-sondes-v0-v1-candidat4-verification-finale-v1.md`, scellé ; constats VF4-n. Rapport final : chemin, empreinte, verdicts, couples, ton modèle.
