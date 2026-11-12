# Consigne — contre-lecture 4 de P3-bis (brouillon 11), autre modèle — v1

- **Session mère** : nouvelle instance (reprise du 2026-11-10, brief `registres/passations/brief-successeur-mere-2026-11-10-v1.md`, passation `registres/passations/2026-11-10-1113.md` `64d321cf…`). Tu es un sous-agent **neuf**. Dépôt : `/home/user/controle-ia-travail` (branche `main`), `PYTHONPATH=src`, interpréteur `/home/user/controle-ia-travail/.venv/bin/python`. Sceller un fichier : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller CHEMIN` (compagnon `.sha256`).
- Français, presque aucun sigle. Toute heure écrite est relevée par `date -u` dans la même commande. Bac à sable temporaire : `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/<ton-nom>/` (crée-le), `TMPDIR` et `--basetemp` dedans.
- **Interdits communs, recopiés mot pour mot ci-dessous (`docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md`, `1ee3b370…`)** — ils priment sur toute autre phrase de cette consigne, sauf les exceptions écrites expressément à la section « Exceptions ».

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


## Rôle
Contre-lecteur **neuf** au sens de R2, **d'un autre modèle que le rédacteur** (Opus 5.5) : N-052. Tu n'as écrit ni P3-bis, ni ses brouillons, ni son code, ni ses contre-lectures 1 à 3. Tu n'as **jamais lu T0.7** et tu ne le lis pas.

## À lire
1. `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon11.md` (`409c37ed…` ; vérifie l'empreinte), ses couples `…-brouillon11-couples-v1.json` (`52074c5d…`), son script `…-brouillon11-faire-v1.py`, son journal `…-brouillon11-journal-v1.txt`.
2. Les contre-lectures précédentes dans `brouillons/P3-bis-temoin-positif-v1/` (`contre-lecture-brouillon2-v1/`, `contre-lecture-2-brouillon5-v1.md`, `contre-lecture-3-brouillon6-v1.md`) et les lignes R-2113, R-2167 du registre.
3. `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/noms-communs-p3bis-v2.md`, la ligne GO-2026-11-10-02 de `registres/go.md` et `docs/decisions/decision-N-066-v1.md`.
4. Le code de la chaîne P3-bis cité par le brouillon (lecture seule, par chemin ; essais ciblés permis).

## Ce que tu vérifies
Complétude R1 (hypothèse, prédiction chiffrée et signe, métrique, seuil, plan, critères gelés, liste d'arrêt) ; cohérence interne et avec les décisions citées ; chaque chiffre renvoie à un chemin et une empreinte (R6) ; gardes testées sur cas sain et artefact (R5) ; borne de création du 18 novembre ; disque requis (≥ 12,69 Go pour la répétition finale) ; marqueurs restants et qui les lève ; traitement des constats des contre-lectures 1 à 3.

## À écrire
- `brouillons/P3-bis-temoin-positif-v1/contre-lecture-4-brouillon11-v1.md`, scellé : rôle, modèle, heure, empreintes lues ; **verdict** (« scellable », « scellable après corrections » avec la liste exacte de couples, ou « non scellable ») ; constats CL4-01… (gravité, lieu, preuve, correction). Aucun commit.

## Rapport final à la mère
Verdict en trois lignes, constats bloquants, chemin et empreinte du rapport.
