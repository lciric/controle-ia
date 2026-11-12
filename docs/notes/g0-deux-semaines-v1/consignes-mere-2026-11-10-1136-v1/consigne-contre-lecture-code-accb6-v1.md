# Consigne : contre-lecture du code de lecture du barreau 6 (`ACCB6`, commit `6c98ea20`) — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-10 à 21:13 UTC (heure relevée par `date -u`). Tu es un sous-agent **neuf**, contre-lecteur de code, **d'un autre modèle que le développeur** (Opus 5.5) : N-052 (VB6-4, R-2278). Tu n'as écrit ni le texte du barreau 6, ni son code, ni ses vérifications. Tu lis T0.7 : tu es exclu ensuite de tout rôle de lecteur de P3-bis. **Tu ne lis ni le verdict ni aucune sortie de `agregation-r1-v4`.**

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

Exception à la règle 4 : le code se lit par `git show 6c98ea20ab7ecfff0c7f10998b9dfad3d75cc625:<chemin>` ; pour jouer essais et banc, extrais **seulement** `src`, `tests` et `scripts` de ce commit par `git archive 6c98ea20… src tests scripts | tar -x -C <ton bac à sable>` (jamais `docs/`) ; mutations sur des copies, jouées avec `-o pythonpath=` et l'import tracé (R-2246). Bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/cl-code-accb6/`. Disque ≈ 4,8 Go : nettoie à la fin. Aucun appel de modèle, aucune donnée réelle, aucune dépense. Sceller : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller CHEMIN` (depuis `/home/user/controle-ia-travail`).

## À lire (empreintes à vérifier)
- Texte joué : `brouillons/accumulation-barreau6-v1/accumulation-barreau6-v1-candidat2.md` (`0716d3d5…`) (un candidat 3 qui ne change que des citations est en cours : ignore-le).
- Rapports du développeur : `docs/notes/g0-deux-semaines-v1/accumulation-b6-code-v1/rapport-developpeur-accb6-v1.md` (`2a6880e4…`), compléments `02d837c9…`, `94226fc8…`, `23c758e7…`.
- Vérifications : `prereg/contre-lectures/accumulation-barreau6-v1-candidat2-verification-courte-v1.md` (`d35055ff…`).

## Mandat
1. Le code fait-il **exactement** ce que dit le texte : entrées (seules celles nommées), calculs (somme et maximum, aires d'épisode, Δ apparié, intervalle par blocs à 10 000 tirages au niveau 1 − 0,05/(2k), plancher d'épisode, prédicteurs triviaux), huit états, séquence, témoins, aiguillage G-1 à G-4, ordre (avant `SCORES-T07`, après `lecture-t07.json`), non-relance, contrôle `CODE-ACCB6`, graines (R9), manifeste, phrases ? Toute divergence est un constat.
2. Chaque garde : cas sain et artefact (R5) ; nomme l'essai.
3. Rejoue les 171 essais, l'énumération v2 (sortie `00088af5…`) et le banc (71 mutations) depuis ta copie ; ajoute **au moins cinq mutations à toi** sur les calculs décisifs et rapporte leur sort.
4. Le paquet ne touche aucun fichier de `src/controle_ia/t07/` ni d'autre paquet ; les clés `ACCB6` n'iraient jamais dans `registres/scellements-v1.md`.
5. **Verdict** : « inscriptible » (`CODE-ACCB6` au commit `6c98ea20`) ou « après corrections » (constats CCB-n, chacun avec ce qu'il faut).

## Sortie
`docs/notes/g0-deux-semaines-v1/accumulation-b6-code-v1/contre-lecture-code-accb6-v1.md`, scellé. Rapport final : chemin, empreinte, verdict en une ligne, constats bloquants.
