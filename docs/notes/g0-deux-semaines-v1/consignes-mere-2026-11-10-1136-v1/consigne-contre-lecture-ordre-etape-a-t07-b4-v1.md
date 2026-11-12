# Consigne : contre-lecture (R2) de l'ordre d'exécution de l'étape A de T0.7, brouillon 4 — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-10 à 15:36 UTC (heure relevée par `date -u`). Tu es un sous-agent **neuf**, contre-lecteur, d'un autre modèle que le développeur (Opus 5.5) : N-052 ; tu n'as écrit ni T0.7, ni son module, ni ses ordres, ni leurs contre-lectures. Tu lis T0.7 : tu es exclu ensuite de tout rôle de lecteur de P3-bis.

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

Exception à la règle 4 : aucune dans le dépôt. Tu peux rejouer des commandes de l'ordre **sur des dépôts jouets ou un clone neuf dans ton bac à sable** `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/cl-ordre-b4/` (aucune instance, aucun `vastai`, aucune clé, aucune dépense). Disque serré (≈ 5 Go) : nettoie à la fin. Sceller : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller CHEMIN`.

## À lire (empreintes à vérifier)
- `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon4.md` (`d5047be2…`) ; brouillon 3 (`b053a220…`) pour comparaison ; rapport `docs/notes/g0-deux-semaines-v1/t07-module-v2/rapport-essai-degeneres-et-ordre-b4-v1.md` (`88a318d9…`).
- Script `scripts/etape_a_t07_variante_b_v2.sh` (et son essai, sa répétition `docs/notes/g0-deux-semaines-v1/t07-module-v2/repetition-jouet-variante-b-v3/`) ; `src/controle_ia/t07/code_t07_v1.py` ; `registres/code-t07/CODE-T07-v1.json`.
- Contre-lectures : `docs/notes/g0-deux-semaines-v1/t07-module-v2/contre-lecture-code-t07-v3-differentiel-court.md` (`d0fe9053…`, O-1 à O-6), `docs/notes/g0-deux-semaines-v1/t07-module-v2/contre-lecture-code-t07-option-c-courte-v1.md` (`7a327462…`), `prereg/contre-lectures/T0.7-sondes-v0-v1-brouillon22-cl-orchestree-v1.md` (`47537dfa…`, CLO-08).
- T0.7 brouillon 22 (`brouillons/T0.7-sondes-v0-v1-brouillon22.md`, `8b84cba5…`), sections « Module », « Calcul et dépense », liste d'arrêt ; registre R-2153, R-2220, R-2229, R-2231, R-2241, R-2246, R-2249, R-2255 ; `registres/go.md` (GO-2026-11-10-04, GO-2026-11-10-06).

## Mandat
1. L'ordre est-il **exécutable tel quel** par la session qui en aura la charge (commandes, arguments du script v2, marqueurs, ordre des gestes, échéances) ? Chaque O-1 à O-6 : réglé, porté, ou reste (et est-ce bloquant) ?
2. Dépense : `ANT0` sous les deux lignes de GO, garde-fou `ANT0` ≤ 4,5 USD, `HMAX`, minuterie et destruction par identifiant (R10) : le plafond de 20 USD tient-il dans tous les cas, échec de la session compris ?
3. C7, S7, `CODE-T07-v2.json` : cohérents avec `code_t07_v1.py` (contrôles 1 à 3, DF-02) et le script (l. 130-140) ? `ATT` (« 346 passed, 2 skipped, 4 xfailed », mesurée sous Python 3.13) : le risque 3.11 est-il dit, et la conséquence d'un écart (arrêt avant le modèle ?) exacte au script ?
4. Cloison : rien du bras d'attaque, rien de 7a, registres nommés seulement (O-5) ; le filtre d'inventaire `t06…`/`t07…` (CLO-08) ; T0.7 cité par la ligne `SCELLEMENT-T07` seulement.
5. Les sept constats S-n pour une v3 du script : l'un d'eux est-il bloquant pour l'étape A ?
6. **Verdict** : « scellable » ou « après corrections » (couples exacts `{ancien, nouveau}`, ancien unique) ou « non ».

## Sortie
`prereg/contre-lectures/ordre-execution-etape-a-t07-v1-brouillon4-cl1.md`, scellé ; constats CLE-n. Rapport final : chemin, empreinte, verdict en une ligne, constats bloquants.
