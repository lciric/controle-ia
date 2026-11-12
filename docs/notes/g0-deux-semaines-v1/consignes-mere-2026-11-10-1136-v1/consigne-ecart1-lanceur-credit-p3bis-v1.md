# Consigne : P3-bis, écart 1 — lanceur dont la seule garde du crédit change (R-2399) — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-11 à 23:17 UTC (heure relevée par `date -u`). Destinataire : un **développeur neuf** (Claude Opus 5.5), qui n'a écrit ni P3-bis, ni sa chaîne, ni les bancs corrigés, et **qui ne lit pas T0.7**.

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

**Exception à la règle 4, et elle seule** : arbre de travail **à toi** (`git worktree add`, sous `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/p3bis-ecart1/`), branche neuve `prep/p3bis-ecart1-credit-v1` partie de **S** `8f8df8b2726a69568b4d4a54bae16188e7f1b3d0` (branche `scellement/p3bis-v2`) : `git add -- <fichiers nommés>`, `git commit`, `git push origin prep/p3bis-ecart1-credit-v1` (retentatives ; garde des secrets à 0). Jamais `main`, jamais `scellement/*`. Aucun appel à l'outil de location réel : seulement le faux outil des bancs.

## L'écart (R-2399, mot de Lazar : « (b) Un écart écrit au texte scellé, qui tient la recharge automatique pour équivalente à la garde. : go »)
Dans le texte scellé (`prereg/P3-bis-temoin-positif-v1.md`, `76ab66ce…`), la garde « crédit exigé à la création : ≥ 20 USD plus 10 heures du prix des instances nommées en marche ; recharge automatique » (point 6 (ii) de « Ce que le code et la chaîne doivent changer » ; liste d'arrêt) est remplacée, **pour cette seule garde**, par : **recharge automatique active (constatée par Lazar) et crédit présent strictement positif**. Rien d'autre ne change.

## Mandat
1. Écris `docs/procedures/P3-bis-temoin-positif-v1/lancer_p3bis_v2_ecart1_v1.sh` = copie de `docs/procedures/P3-bis-temoin-positif-v1/lancer_p3bis_v2.sh` **au commit S**, dont ne changent que :
   (a) le contrôle de soi (l. 95 environ : `"lancer_p3bis_v2.sh=$0"`) devient la comparaison de `$H/lancer_p3bis_v2.sh` (le lanceur d'origine, resté dans le dossier) à sa copie versée à S : la chaîne d'origine reste entière et vérifiée ;
   (b) la garde du crédit (bloc 9, l. 189-198 environ) : la ligne officielle du module commun (`verifications_p3bis_v2.py credit`) est toujours écrite au journal ; son code 3 (« crédit insuffisant ») ne bloque plus : le lanceur relit le crédit présent, exige qu'il soit **strictement positif** (sinon code 3, « crédit nul ou négatif : pas de création »), et écrit une ligne fixe `écart 1 (R-2399) : garde du crédit remplacée par la recharge automatique du compte (mot de Lazar) ; crédit présent > 0 exigé` au journal et dans `lancement.txt` ; tout autre code reste un arrêt (crédit illisible : code 2) ;
   (c) l'en-tête : une note d'écart en tête (R-2399, addendum 1), l'usage du nom neuf ;
   rien d'autre (vérifie-le par `diff`, liste chaque ligne changée).
2. **Aval** : vérifie que le contrôle à cinq minutes, la surveillance, la récupération et la destruction acceptent les traces de ce lanceur (s'ils relisent l'empreinte du lanceur ou l'étiquette de `lancement.txt`, dis exactement quoi, et ce qu'il faut ; **ne change aucun autre script** ; s'il faut en changer un, arrête-toi et écris-le).
3. **Essais R5** (bac à sable, faux outil de location des bancs, aucun appel réel) : cas sain (crédit 6 USD, instance nommée en marche : la garde passe sous l'écart, ligne d'écart écrite) ; artefacts : crédit 0 (refus, code 3) ; crédit illisible (code 2) ; lanceur d'origine absent ou modifié dans le dossier (refus du contrôle de soi) ; et la répétition jouet ou un passage équivalent jusqu'à la création factice et au contrôle à cinq minutes avec ce lanceur, si c'est faisable sans changer d'autre script.
4. Commit sur ta branche : le lanceur d'écart et son compagnon (sceau), tes essais et leurs sorties (sous `docs/notes/g0-deux-semaines-v1/p3bis-ecart1-v1/`, noms neufs, scellés) ; rapport `rapport-ecart1-lanceur-v1.md` (commit, empreinte du lanceur d'écart, lignes changées, aval, essais).

## Sortie
Rapport final à la mère : branche, commit, empreinte du lanceur d'écart, verdict en une ligne, ton modèle.
