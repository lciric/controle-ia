# Consigne : P3-bis — correction des bancs pour qu'ils jouent contre une chaîne épinglée — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-11 à 14:16 UTC (heure relevée par `date -u`). Destinataire : un **développeur neuf** (Claude Opus 5.5), qui n'a écrit ni P3-bis, ni son code, ni sa chaîne, ni aucune de leurs contre-lectures, et **qui ne lit pas T0.7**.

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

**Exception à la règle 4, et elle seule** : dans un arbre de travail **à toi** (`git worktree add` sous ton bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/p3bis-bancs/`, jamais le dépôt principal), branche neuve `prep/p3bis-bancs-epingles-v1` partie du commit du code `5e4575259478af3611e2c7fb1313342912caf484` : `git add -- <fichiers nommés>`, `git commit`, `git push origin prep/p3bis-bancs-epingles-v1` (retentatives 2, 4, 8, 16 s ; garde des secrets à 0 chaînée par `&&`). Rien d'autre n'est poussé ; jamais `main`.

## Le défaut (R-2367 ; rapport de la session fille, 14:15 UTC)
La phase 2 de P3-bis exige les bancs « rejoués après l'épinglage » (P-6), et `verifications_p3bis_v2.py preuves` refuse un script « éprouvé sous deux empreintes » : les bancs doivent donc tourner contre les contrôles et la récupération **épinglés**. Or :
- `essais_controles_p3bis_v2.sh` (l. 158-161) cherche chaque ligne `^{k}=A_EPINGLER.*$` et exige une occurrence : refus sur des contrôles épinglés (« AssertionError: CANDIDAT_RELU_CHEMIN ») ;
- `essais_recuperation_p3bis_v2.sh` (l. 36-38) : `sed s|^PY=A_EPINGLER.*|PY=$PYB|` ne change plus rien, puis exige deux lignes changées ; son cas R01e attend une épingle non remplie ;
- `repetition_jouet_p3bis_v2.sh` (l. 55) : même `sed` sur `PY`.

## Mandat
1. Corrige ces **trois fichiers sur place** (mêmes noms : le module commun `verifications_p3bis_v2.py`, `JOURNAUX`, et le scellement les nomment ; rien d'autre ne change) pour qu'ils jouent **aussi bien contre une chaîne épinglée que non épinglée** : remplacer la ligne `^{k}=.*$` (ou `^PY=.*`) quelle qu'en soit la valeur, une occurrence exigée ; les cas qui éprouvent la garde « épingle restée » (K…, R01e) fabriquent l'artefact en **remettant** `A_EPINGLER` dans la copie ; tout autre cas inchangé. Compagnons re-scellés pour ces trois fichiers (réécriture directe à la forme de `scellement.sceller`, `<sha256>  <nom>` et fin de ligne : permis par la mère pour ces trois-là, R-2367).
2. **Preuve (R5)** : joue les trois bancs corrigés, dans des racines neuves de ton bac à sable, (a) contre la chaîne au commit du code (non épinglée) et (b) contre une copie épinglée avec les valeurs de `scellement/p3bis-v1` (commit `a3116ff529587121b283259b404684e07f9806f2`, fichiers `controles_avant_depense_p3bis_v2.sh` et `recuperation_p3bis_v2.sh`, pris par `git show`) : dernières lignes conformes, « cas non conformes : 0 » ; même nombre de cas qu'avant ; liste des cas changés. Place : vérifie `df -Pk` avant (≥ 5 Go) ; efface tes racines par leur chemin exact après.
3. `git diff 5e457525 <ton commit>` : seuls ces trois fichiers et leurs compagnons.
4. Rapport `docs/notes/g0-deux-semaines-v1/p3bis-regle-plancher-v1/rapport-bancs-epingles-p3bis-v1.md` (nom neuf, scellé, versé sur ta branche) : commit, empreintes neuves des trois fichiers, diff commenté, sorties des passages (a) et (b) (empreintes), cas changés.

## Sortie
Rapport final à la mère : branche, commit, empreintes, verdict en une ligne, ton modèle.
