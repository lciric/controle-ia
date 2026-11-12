# Consigne : brouillon 4 de la consigne de l'audit des fuites de T0.7 (remplissage des marqueurs sur le texte scellé) — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-11 à 13:28 UTC (heure relevée par `date -u`). Destinataire : un **agent neuf**, qui n'a écrit ni T0.7, ni ses contre-lectures, ni son module, ni les brouillons 1 à 3 de cette consigne, ni leur contre-lecture. Tu lis T0.7 : tu seras exclu ensuite de tout rôle de lecteur de P3-bis, et de tout rôle d'auditeur ou de contre-lecteur de l'audit des fuites.

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

Exception à la règle 4 : aucune (`git show` d'un commit déjà présent permis, dont `c7484c43` de la branche de données du découpeur). Tu n'écris que sous `brouillons/T0.7-audit-fuites-v1/` (noms neufs : `T0.7-consigne-audit-fuites-v1-brouillon4.md`, `…-brouillon4-pieces/`) et dans ton bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/audit-fuites-b4/`. Aucun commit, aucune dépense. Sceller chaque sortie (`PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller <fichier>`).

## Ce qui fonde ce travail (registre)
R-2203, R-2212 (brouillon 3, Q14), R-2238 (découpeur), R-2321 (T0.7 scellé : `prereg/T0.7-sondes-v0-v1.md`, `d7d180eccbbce8ff2e370f82957543c28f1e564c872f981c7ada403949baade5`).

## À lire (empreintes à vérifier)
- `brouillons/T0.7-audit-fuites-v1/T0.7-consigne-audit-fuites-v1-brouillon3.md` (compagnon) et son journal ; brouillon 2 ; contre-lecture 1 (chemin au § 14.1).
- Texte scellé de T0.7 et, pour comparaison, `brouillons/T0.7-sondes-v0-v1-brouillon21.md` et `…-brouillon22.md`.

## Mandat (couples appliqués par un script à toi ; chaque « ancien » une fois)
1. **`LIGNE_AUDIT_FUITES_T07_B22`** : le brouillon 22 a été dépassé par le texte scellé. Remplis le marqueur par programme selon la règle écrite sous le § 2.1, **sur le texte scellé** (chemin et sha256 du texte scellé ; deuxième cellule de la ligne `AUDIT-FUITES-T07` citée en bloc, à l'octet ; sha256 de cette cellule seule, sans fin de ligne ; troisième et quatrième cellules ; couples « ancien → nouveau » qui la séparent de la cellule du brouillon 21, calculés par programme) ; dis si la ligne du texte scellé est égale à l'octet à celle du brouillon 22 ; titre du § 2.1 et note de remplissage ajustés (« texte scellé » au lieu de « brouillon 22 »).
2. **§ 2.2 et § 2.3** (recopiés du brouillon 21) : compare chaque passage au texte scellé, par programme ; s'il diffère, recopie le passage du texte scellé, avec son couple et le sha256 neuf ; liste tout passage introuvable (arrêt et question).
3. **`CHEMIN_DECOUPEUR`** (R-2238) : dossier `donnees/decoupeur-llama-3.1-8b-instruct-0e9e39f2-v1/` du commit `c7484c43657a2ce22d76af33efd06aaa11a6aafa`, extrait par `git archive` sur la machine de l'auditeur ; les trois sha256 recalculés par `git show` et comparés à R-2238 et aux compagnons du commit.
4. Annexe B : dis si elle reste (comparaison) ou devient sans objet ; § 14.2 : laisse `RAPPORT_CONTRE_LECTURE_2` (la mère la commande) et mets à jour son objet (différentiel du brouillon 3 au brouillon 4, remplissages, conformité de la ligne scellée à R-2203).
5. Statut du brouillon 4 en tête (qui, quand, d'où) ; défaire tes couples redonne le brouillon 3 à l'octet ; seul marqueur restant : `RAPPORT_CONTRE_LECTURE_2`.

## Sortie
Brouillon 4, couples, script, journal, scellés ; rapport final : chemins, empreintes, égalité de la ligne entre le brouillon 22 et le texte scellé, passages changés, questions, ton modèle.
