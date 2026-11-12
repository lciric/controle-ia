# Consigne : contre-lecture 1 (R2) du texte court du barreau 6 (« accumuler bat le score action par action »), brouillon 1 — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-10 à 16:11 UTC (heure relevée par `date -u`). Tu es un sous-agent **neuf**, contre-lecteur, d'un autre modèle que le rédacteur (Opus 5.5) : N-052. Tu n'as écrit ni ce texte, ni T0.6, T0.7, T0.8, P3-bis. Tu lis T0.7 : tu es exclu ensuite de tout rôle de lecteur de P3-bis. **Tu ne lis ni `docs/verdicts/verdict-agregation-r1-v4-v1.md`, ni aucune sortie de `agregation-r1-v4`** (le texte du préenregistrement `prereg/agregation-r1-v4-v1.md` est permis).

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

Exception à la règle 4 : aucune. Bac à sable : `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/cl-barreau6/` (scripts depuis des copies, `python -I`). Aucun appel de modèle, aucune dépense. Sceller : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller CHEMIN`.

## À lire (empreintes à vérifier)
- `brouillons/accumulation-barreau6-v1/accumulation-barreau6-v1-brouillon1.md` (`a2d81863…`), journal, scripts et sorties de puissance et d'essai des clés ; et les fichiers que la section « Contre-lecture » du texte nomme.
- Registre : R-2171, R-2175, R-2257 ; décisions N-007, N-054, N-055, N-056 (`docs/decisions/`).

## Mandat
1. Préenregistrement complet (R1) : hypothèse, prédiction chiffrée et signe, métrique, seuil, plan, critères gelés, liste d'arrêt ; chaque état d'une sonde a une règle écrite, sans cas non couvert.
2. Aucun calcul neuf sur activations, aucune sonde neuve, aucune moyenne sur les jetons d'une sonde de production ; seuls les scores déjà écrits par T0.7 sont lus ; renvois à T0.7 (brouillon 22) exacts.
3. Ordre : scellé strictement avant `SCORES-T07`, lu après `lecture-t07.json`, rien vers le lecteur de P3-bis ; registre propre `ACCB6` qui ne gêne pas la garde de T0.7 (rejoue l'essai des clés depuis une copie).
4. Rejoue la puissance depuis une copie ; les conclusions écrites (« non établi à cette puissance » probable) suivent-elles des sorties ?
5. Frontière H1/H1a, H2, G1, mode tenu à l'écart : tenue ? Les deux nœuds N-B6-1 et N-B6-2 sont-ils bien posés, et n'y en a-t-il pas d'autre ?
6. **Verdict** : « scellable après les mots de Lazar et corrections » (couples exacts `{ancien, nouveau}`) ou « non ».

## Sortie
`prereg/contre-lectures/accumulation-barreau6-v1-brouillon1-cl1.md`, scellé ; constats CLA-n. Rapport final : chemin, empreinte, verdict en une ligne, constats bloquants.
