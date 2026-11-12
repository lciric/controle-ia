# Consigne : contre-lecture de l'écart 1 de P3-bis (addendum 1 et lanceur d'écart) — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-11 à 23:37 UTC (heure relevée par `date -u`). Destinataire : un **contre-lecteur neuf, Claude Fable 5.2** (autre modèle que le développeur et le rédacteur, Opus 5.5), qui n'a écrit aucune pièce de P3-bis, **et qui ne lit pas T0.7**.

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

Exception à la règle 4 : `git worktree add --detach` d'un arbre à toi sous `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/p3bis-ecart1-cl/` (extraction partielle, aucun chemin interdit) pour rejouer des essais ; aucun commit. Tu n'écris que `brouillons/P3-bis-temoin-positif-v1/P3-bis-ecart1-contre-lecture-v1.md` (scellé) et ton bac à sable.

## À relire
- Brouillon 1 de l'addendum : `brouillons/P3-bis-temoin-positif-v1/P3-bis-addendum-1-garde-credit-v1-brouillon1.md` (`0cf6c08bf78b56d1983e93026b9a60b9cab431acee889c4f4fd4d4e446e3bfec`).
- Lanceur d'écart et essais : branche `prep/p3bis-ecart1-credit-v1`, commit `e13df72b94510fba947a2262fa2274624bef7da4` (`lancer_p3bis_v2_ecart1_v1.sh` = `dc33635f…`), comparé à `lancer_p3bis_v2.sh` au commit S `8f8df8b2…` ; rapport et essais sous `docs/notes/g0-deux-semaines-v1/p3bis-ecart1-v1/`.
- Registre R-2386, R-2394 à R-2401 ; texte scellé `prereg/P3-bis-temoin-positif-v1.md` : passages du crédit, liste d'arrêt, critères de lecture ligne 1 (relance), l. 1950-1970, 2280-2295.

## Mandat
1. Le diff ne change que ce que R-2399 permet (garde du crédit, contrôle de soi qui garde le lanceur d'origine vérifié contre S, en-tête) ; aucune autre garde affaiblie ; rejoue au moins E1, E6, E8, E9 avec le faux outil.
2. L'addendum dit juste ce qui change et ce qui ne change pas ; chaque citation du texte scellé exacte ; réserve au verdict écrite.
3. Réponds aux questions du rédacteur : (a) forme du scellement (la mère propose : addendum scellé par son compagnon, versé sous `prereg/P3-bis-addendum-1-garde-credit-v1.md` sur `main` et dans un commit après `e13df72b` sur la branche d'écart, consigné au registre des décisions ; la chaîne accepte-t-elle de lancer depuis une branche qui porte des commits après S ?) ; (b) le lanceur d'écart est-il hors du « code cité » de la ligne 1 des critères (`COMMIT_CODE_P3BIS`) ? ; (c) portée : toute tentative sous ce texte et ce GO.
4. Verdict en une ligne : « scellable » ou « scellable après corrections » (couples exacts) ou « non » (motif).

## Sortie
Rapport scellé ; rapport final : chemin, empreinte, verdict, ton modèle.
