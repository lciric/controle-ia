# Consigne : rédiger l'addendum 1 de P3-bis (écart de la garde du crédit) — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-11 à 23:32 UTC (heure relevée par `date -u`). Destinataire : un **rédacteur neuf** (Claude Opus 5.5), qui n'a écrit ni P3-bis, ni sa chaîne, ni le lanceur d'écart, et **qui ne lit pas T0.7**.

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

Exception à la règle 4 : aucune. Tu n'écris que `brouillons/P3-bis-temoin-positif-v1/P3-bis-addendum-1-garde-credit-v1-brouillon1.md` (et son sceau) et ton bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/p3bis-addendum1/`. Aucun commit.

## À lire
Registre R-2386, R-2394 à R-2399 (mot de Lazar, verbatim, en R-2399) ; texte scellé `prereg/P3-bis-temoin-positif-v1.md` (`76ab66ce…`) : seulement ses passages sur le crédit (`grep -n crédit`) et sa liste d'arrêt ; lanceur d'écart `docs/procedures/P3-bis-temoin-positif-v1/lancer_p3bis_v2_ecart1_v1.sh` et rapport `docs/notes/g0-deux-semaines-v1/p3bis-ecart1-v1/rapport-ecart1-lanceur-v1.md`, au commit `e13df72b94510fba947a2262fa2274624bef7da4` de la branche `prep/p3bis-ecart1-credit-v1` (`git show`).

## Mandat
Addendum court (1 à 2 pages), sur le modèle des addenda de P3 (`prereg/P3-addendum-lecture-complementaire-v1.md`) : objet ; mot de Lazar recopié ; **ce qui change** (garde du crédit seule : recharge automatique active, constatée par Lazar, et crédit présent > 0 ; citer chaque passage du texte scellé concerné, ligne et phrase) ; **ce qui ne change pas** (hypothèse, prédiction, métrique, seuil, plan, critères de lecture, autres arrêts, plafond de 80 USD et surveillance de la dépense cumulée, GO, date) ; moyen (lanceur d'écart, chemin, empreinte `dc33635f…` en entier, commit, essais R5 cités par chemin et empreinte, aval inchangé) ; conditions d'emploi (empreinte vérifiée avant le lancement, joué depuis le dossier de la chaîne où `lancer_p3bis_v2.sh` reste égal à S) ; **réserve au verdict** (« garde du crédit levée par écart, R-2399 ») et risque résiduel (une recharge automatique en défaut pendant la course : la surveillance et la liste d'arrêt s'appliquent) ; aucun chiffre non sourcé. Scelle le brouillon. Rapport : chemin, empreinte, questions.
