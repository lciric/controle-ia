# Consigne : vérification courte du candidat 2 du barreau 6 (différentiel du brouillon 2) — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-10 à 20:29 UTC (heure relevée par `date -u`). Tu es un sous-agent **neuf**, vérificateur, d'un autre modèle que le rédacteur (Opus 5.5) ; tu n'as écrit ni ce texte, ni son code, ni sa contre-lecture 1. Tu lis T0.7 : tu es exclu ensuite de tout rôle de lecteur de P3-bis. **Tu ne lis ni le verdict ni aucune sortie de `agregation-r1-v4`.**

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

Exception à la règle 4 : aucune ; le code se lit par `git show 5ee8a4ac8712221a31599e2a92dfbae981cc5704:<chemin>`. Bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/verif-b6-c2/` (scripts depuis des copies, `python -I`). Aucun appel de modèle, aucune dépense. Sceller : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller CHEMIN`.

## À lire (empreintes à vérifier)
- `brouillons/accumulation-barreau6-v1/accumulation-barreau6-v1-candidat2.md` (`0716d3d5…`) ; candidat 1 (`b8bbea6a…`) ; brouillon 2 (`9f070e31…`) ; couples, scripts et journaux des deux candidats.
- Contre-lecture 1 `prereg/contre-lectures/accumulation-barreau6-v1-brouillon1-cl1.md` (`c13cbdde…`) ; rapports du code `docs/notes/g0-deux-semaines-v1/accumulation-b6-code-v1/` (rapport `2a6880e4…`, compléments `02d837c9…`, `94226fc8…`) ; registre R-2265, R-2268, R-2272 à R-2277.

## Mandat
1. Rejoue les scripts des candidats 1 puis 2 sur une copie du brouillon 2 : candidat 2 à l'octet.
2. Couples CP-01 à CP-19, C1-01 à C1-17, C2-01 à C2-09 : chacun fidèle à sa source (rapport du code, décisions de Lazar et de la mère) ; ceux qui touchent des sections gelées : un par un, aucun signe, seuil, niveau, état décisif ni ordre de séquence changé ? Si l'un en change un, c'est un constat bloquant.
3. Le texte et le code au commit `5ee8a4ac` disent-ils la même chose (états, phrases, gardes, non-relance, contrôle `CODE-ACCB6`) ? Rejoue l'énumération depuis une copie (`git show`) : sortie `3bde500f…`.
4. Marqueurs : seul `REVERIFICATION_T07_SCELLE` reste ; valeurs remplies exactes (R-2265, R-2274, R-2276).
5. **Verdict** : « scellable une fois `REVERIFICATION_T07_SCELLE` remplie » ou « après corrections » (couples exacts).

## Sortie
`prereg/contre-lectures/accumulation-barreau6-v1-candidat2-verification-courte-v1.md`, scellé ; constats VB6-n. Rapport final : chemin, empreinte, verdict en une ligne, constats bloquants.
