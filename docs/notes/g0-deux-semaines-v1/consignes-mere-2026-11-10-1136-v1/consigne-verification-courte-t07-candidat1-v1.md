# Consigne : vérification courte du candidat 1 de T0.7 (différentiel du brouillon 22) — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-10 à 16:39 UTC (heure relevée par `date -u`). Tu es un sous-agent **neuf**, vérificateur, d'un autre modèle que le rédacteur (Opus 5.5) : N-052 ; tu n'as écrit ni T0.7, ni son module, ni ses ordres, ni leurs contre-lectures. Tu lis T0.7 : tu es exclu ensuite de tout rôle de lecteur de P3-bis.

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

Exception à la règle 4 : aucune. Bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/verif-t07-candidat1/` (scripts depuis des copies, `python -I` ; essais ciblés permis avec `--basetemp` au bac à sable). Aucun appel de modèle, aucune dépense. Sceller : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller CHEMIN`.

## À lire (empreintes à vérifier)
- `brouillons/T0.7-sondes-v0-v1-candidat1.md` (`1718f2a0…`) et `brouillons/T0.7-sondes-v0-v1-candidat1-pieces/` (couples `f73c5882…`, script, journal, configuration v5) ; brouillon 22 (`8b84cba5…`).
- Couples orchestrés `prereg/contre-lectures/T0.7-sondes-v0-v1-brouillon22-cl-orchestree-v1-couples.json` (`4c940714…`) et rapport (`47537dfa…`) ; ordre `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon5.md` (`d0b75d16…`) et sa contre-lecture (`88ea9f06…`).
- Registre R-2241 à R-2262 ; `registres/go.md`.

## Mandat
1. Rejoue le script du candidat sur une copie du brouillon 22 : candidat à l'octet ; CLO égaux au fichier `4c940714…` ; CLO-03 absent.
2. **Couples C1, un par un** : fidèles aux décisions (R-2249, R-2255, R-2258, R-2260, R-2262) ? Aucun ne touche une section gelée hors CLO-08 (vérifie par programme) ; aucun signe, seuil ni critère changé.
3. Marqueurs remplis : valeurs exactes (entropie R-2259 ; configuration v5 : recalcule l'empreinte canonique par `python -m controle_ia.t07.lecture_v2 empreinte-config` ou la fonction, et le sha256 du fichier ; ordre `d0b75d16…` ; GO ; essais CLC-04 et GARDES-CODE-01 : commits, empreintes, présence dans `main`) ; `exiger_configuration` passe la v5.
4. **Grille** : rejoue `grille_l_t07_brouillon17.py` (là où le texte la cite) sur le candidat ; égale à la sortie versée ?
5. **`LECTURES_7A_T07`** : le registre porte-t-il, après R-2067, une lecture de 7a qu'il faudrait ajouter ? (`git grep -n "7a" -- registres/decisions.md` ; ne suis aucun renvoi vers un chemin interdit.)
6. **Verdict** : « scellable » (une fois `MOT_LAZAR_P064` et `MOT_LAZAR_P065` remplis) ou « après corrections » (couples exacts).

## Sortie
`prereg/contre-lectures/T0.7-sondes-v0-v1-candidat1-verification-courte-v1.md`, scellé ; constats VC1-n. Rapport final : chemin, empreinte, verdict en une ligne, constats bloquants.
