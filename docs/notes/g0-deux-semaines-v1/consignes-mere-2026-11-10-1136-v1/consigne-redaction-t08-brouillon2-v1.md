# Consigne : rédiger le brouillon 2 de T0.8 (bases boîte noire v0), base (A) désormais scellée à part — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-10 à 14:05 UTC (heure relevée par `date -u`), autonomie de 12 heures (R-2201) sous accord général (GO-2026-11-10-05, GO-2026-11-10-09). Destinataire : un **rédacteur neuf**, qui n'a écrit ni T0.8 (brouillon 1), ni sa contre-lecture, ni la base (A) « mots et coût ». Tu ne lis aucun fichier de T0.7 au-delà de ce que T0.8 cite déjà (pas de `src/controle_ia/t07/`, pas de brouillon de T0.7).

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

Exception à la règle 4 : aucune. Tu n'écris que sous `brouillons/` (noms neufs) et dans ton bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/t08-b2/`. Sceller : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller CHEMIN`. Aucun commit, aucun appel de modèle, aucune dépense.

## À lire (empreintes à vérifier)
- `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon1.md` (`ca26763a…`) et son journal.
- Contre-lecture 1 : `prereg/contre-lectures/T0.8-bases-boite-noire-v0-v1-brouillon1-cl1.md` (`21499f7c…`) : 44 couples, bloquants B-1 à B-3, décisions DB8-1 à DB8-8.
- Base (A) scellée : `prereg/T0.8-base-A-mots-et-cout-v1.md` (`72b067d5…`) et la ligne `SCELLEMENT-T08-BASE-A` de `registres/scellements-v1.md`.
- Registre `registres/decisions.md` : R-2165, R-2175, R-2186, R-2193, R-2209, R-2211, R-2214, R-2216 ; décision `docs/decisions/` N-029 et N-061 (Liars' Bench, SHADE-Arena à T0.8, NARCBench au bras descriptif de T0.7 ; devis avant GO par ligne).

## Mandat
1. Appliquer les **44 couples** de la contre-lecture 1 par **un script à toi** (nom neuf), chaque « ancien » trouvé une fois ; les sections gelées touchées, déclarées une par une ; aucune hypothèse, prédiction, signe ni seuil ne change sans nœud (arrête-toi et signale-le).
2. **Base (A)** : tout ce que la base (A) « mots et coût » scellée fixe désormais (DB8-1 (a), R-2175, R-2216) est retiré de T0.8 et remplacé par un renvoi au texte scellé (chemin, empreinte, ligne de registre) ; rien ne la contredit ni ne la redouble ; douze traits (CLBA-04 (a), R-2211).
3. **Décisions DB8** : appliquer les défauts et décisions du registre (DB8-2 (a), DB8-3, DB8-6, DB8-8 défauts ; DB8-7 selon R-2193 ; **DB8-4** : base (iv), Liars' Bench, SHADE-Arena et juge Qwen reportés, écrits comme reportés avec ce qu'il faudrait pour les reprendre, N-061 cité ; **DB8-5** : plafond de 120 USD au-dessus du seuil de 60 de GO-2026-11-10-09, écrit « retour à Lazar avant toute course », devis à jour en marqueur `<<GO_T08>>`).
4. **B-1** (contrôle de l'adaptateur pour les surveillants appris) : renvoi au texte de validité de l'adaptateur (`brouillons/validite-adaptateur-v1/validite-adaptateur-preenregistrement-v1-brouillon3.md`, D-1 (b), GO-2026-11-10-07) pour ce qu'il couvre ; ce qui reste propre à T0.8, écrit et chiffré.
5. Marqueurs restants listés à l'en-tête ; `controle_ia.prereg.problemes` vérifié.

## Sorties (noms neufs, scellés ; brouillon 1 intact)
`brouillons/T0.8-bases-boite-noire-v0-v1-brouillon2.md`, `…-brouillon2-couples-v1.json`, `…-brouillon2-faire-v1.py`, `…-brouillon2-journal-v1.md` (couples, écarts, questions Q-n avec recommandation, devis à jour). Rapport final : chemins, empreintes, nombre de couples, marqueurs restants, questions pour la mère.
