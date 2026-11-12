# Consigne : contre-lecture courte de la correction des bancs de P3-bis (chaîne épinglée) — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-11 à 14:38 UTC (heure relevée par `date -u`). Destinataire : un **contre-lecteur neuf, Claude Fable 5.2** (autre modèle que le développeur, Claude Opus 5.5), qui n'a écrit ni P3-bis, ni son code, ni sa chaîne, ni aucune contre-lecture de P3-bis, et **qui ne lit pas T0.7**.

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

Exception à la règle 4 : `git worktree add` d'arbres **détachés** sous ton bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/p3bis-bancs-cl/` (extraction partielle : aucun chemin interdit sur disque), pour jouer les bancs ; aucun commit, aucune poussée. Tu n'écris que `docs/notes/g0-deux-semaines-v1/p3bis-regle-plancher-v1/contre-lecture-courte-bancs-epingles-p3bis-v1.md` (nom neuf, scellé) et ton bac à sable.

## Objet (R-2367)
Branche `prep/p3bis-bancs-epingles-v1` : correction `68ded698ce1bbfd8815d7b7ab28557775e4d2e5b` (trois bancs de `docs/procedures/P3-bis-temoin-positif-v1/` — `essais_controles_p3bis_v2.sh`, `essais_recuperation_p3bis_v2.sh`, `repetition_jouet_p3bis_v2.sh` — et leurs compagnons), rapport `6283b129…` (`docs/notes/g0-deux-semaines-v1/p3bis-regle-plancher-v1/rapport-bancs-epingles-p3bis-v1.md`, `a4020e30…`) ; base : commit du code `5e4575259478af3611e2c7fb1313342912caf484` ; consigne du développeur `consigne-correction-bancs-epingles-p3bis-v1.md` (`2748d944…`).

## Mandat
1. Le diff ne fait que ce que la consigne demande : remplacer `^K=.*$` (ou `^PY=.*`) quelle que soit la valeur, une occurrence exigée ; artefacts « épingle restée » (K34, R01e) fabriqués en remettant `A_EPINGLER` dans la copie ; **aucun autre cas changé**, aucune garde affaiblie (compare cas par cas au commit du code).
2. Rejoue au moins le banc des contrôles et celui de la récupération contre la chaîne épinglée de `scellement/p3bis-v1` (`a3116ff529587121b283259b404684e07f9806f2`, deux fichiers par `git show`) : « cas non conformes : 0 », même nombre de cas ; et un artefact de ton choix qui doit casser.
3. Les « scripts éprouvés » des journaux : chaque script sous une seule empreinte ; les bancs corrigés, éprouvés contre la chaîne épinglée, sont compatibles avec la répétition finale (même empreinte des contrôles `c3684087…` et de la récupération `3b21c80c…`).
4. Réserve du développeur (gardes de construction des artefacts éprouvées sur leur seul cas sain) : bloquante ou non ?

## Sortie
Rapport scellé : verdict en une ligne (« citable au scellement : commit `68ded698` » ou motif), constats numérotés avec preuve. Rapport final : chemin, empreinte, verdict, ton modèle.
