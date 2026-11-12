# Consigne — module de lecture T0.7 v2, option (c) des concepts — reprise du travail interrompu — v1

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
Développeur neuf. Tu n'as écrit ni T0.7, ni ses contre-lectures, ni le travail interrompu que tu reprends.

## Exceptions aux interdits (règle 4)
Tu travailles dans l'arbre `/home/user/wt-t07-module-v2` (branche `prep/t07-module-v2`, tête `88e80ba0`, déjà extraite ; `docs/notes/bras-attaque/` n'y est pas extrait). Dans **cet arbre seulement**, tu peux modifier `src/`, `tests/`, `scripts/`, `docs/notes/g0-deux-semaines-v1/t07-module-v2/`, et faire des `git add` / `git commit` sur cette branche. Jamais `push`, `fetch`, `checkout`, `reset`, `rebase`, `stash`. Jamais de dossier `.essais-tmp` ni de fichier temporaire dans un commit (le commit interrompu `13e7f85a` en avait versé ; `88e80ba0` les a retirés). Lance les essais avec `PYTHONPATH=src`, `--basetemp` dans ton bac à sable.

## Objet
R-2166 (lis-la : `grep -n '^| R-2166 ' /home/user/controle-ia-travail/registres/decisions.md`) : l'option (c) des concepts **exige un changement du module** : la clé `SCELLEMENT-CONCEPTS-T07` passe des clés exigées aux clés **permises** (`src/controle_ia/t07/registre_v1.py`, ≈ l. 67) ; jeux génériques lus sans condition ; phrases des concepts lues **seulement** si leur ligne de registre précède la fermeture ; T7-P9 « non lue » et réserve R15 quand elles ne le sont pas ; plancher de concept gardé au manifeste. La ligne `CODE-T07` citera le commit neuf (plus `8ae9fc44`).
Le développeur précédent a été coupé par le quota au commit `13e7f85a` (« TRAVAIL INTERROMPU ») : `git diff a4352e6a 88e80ba0 -- src tests scripts` montre son état partiel (`lecture_v2.py`, `lectures_t07_v1.py`, `registre_v1.py`, `tests/test_t07_option_c_concepts_v1.py`, `tests/test_t07_repli_etapes_v1.py`, `scripts/etape_a_t07_variante_b_v2.sh`). Ce travail **n'est pas rendu** : vérifie-le ligne par ligne contre les exigences, complète-le, corrige-le.

## À lire
1. R-2153, R-2155, R-2166, R-2183 dans `registres/decisions.md`.
2. `brouillons/T0.7-sondes-v0-v1-brouillon21.md` (`f7dcb226…`) : passages sur l'option (c), la clé `SCELLEMENT-CONCEPTS-T07`, R15, T7-P9, le plancher de concept, l'ordre de l'étape A variante B (cherche par `grep -n` dans ce seul fichier).
3. Les rapports du module sous `docs/notes/g0-deux-semaines-v1/t07-module-v2/` (rapport complémentaire 4 au commit `a4352e6a`) et la contre-lecture courte `contre-lecture-code-t07-v3-differentiel-court.md` (`d0fe9053…`).
4. `docs/procedures/consigne-concepts-sans-lien-T0.7-v3.md` (consigne v3 corrigée des concepts, `ea5fe3f0…` ; vérifie l'empreinte).

## À faire
- Chaque garde touchée : un cas sain et un artefact (R5) ; aucun repli silencieux.
- Essais ciblés du module T0.7 (tous les `tests/test_t07*` et ceux que tes changements touchent) ; banc de mutations du module s'il existe (dis lequel).
- Script `etape_a_t07_variante_b_v2.sh` : nom neuf (le v1 reste intact, R12), répétition à blanc s'il en existe une (sans réseau, sans GPU).
- Commits sur `prep/t07-module-v2`, messages en français, terminés par la ligne `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.
- Rapport scellé : `docs/notes/g0-deux-semaines-v1/t07-module-v2/rapport-complementaire-5-option-c-v1.md` (ce qui était fait dans le travail interrompu, ce que tu as corrigé, liste des exigences de R-2166 avec ligne de code et essai, commandes et comptes d'essais, commit final proposé pour `CODE-T07`).

## Rapport final à la mère
Commit final, empreinte du rapport, comptes d'essais, verdict en une ligne (« prêt pour contre-lecture courte » ou non), points ouverts.
