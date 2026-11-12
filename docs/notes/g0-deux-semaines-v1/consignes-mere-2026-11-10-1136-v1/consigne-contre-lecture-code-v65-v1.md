# Consigne — contre-lecture du code v65 de l'organisme d'idéation — v1

- **Session mère** : nouvelle instance (reprise du 2026-11-10). Tu es un sous-agent **neuf**, contre-lecteur au sens de R2, **d'un autre modèle que l'auteur** (Opus 5.5) : N-052. Dépôt `/home/user/controle-ia-travail` (`main`), `PYTHONPATH=src`, interpréteur `.venv/bin/python`. Sceller : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller CHEMIN`. Français ; toute heure par `date -u`. Bac à sable : `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/<ton-nom>/`. **Disque serré** (≈ 2,8 Go libres) : pas de copie lourde, `--basetemp` dans ton bac à sable, nettoie-le à la fin.
- **Interdits communs, recopiés mot pour mot (`docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md`, `1ee3b370…`)** :

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
Tu n'as écrit ni le code v65, ni sa consigne, ni le code des versions précédentes de l'organisme. L'auteur est Opus 5.5 ; tu es d'un autre modèle (N-052). Le contre-lecteur précédent a été coupé par le quota sans rendu.
## Pièces
- Code à relire : arbre `/home/user/organisme-v65-cl` (dépôt public de l'organisme), branche locale `prep/organisme-v65-boucle-reelle-v2`, commit `cef5ea60ea22a9bb46a2b0be761972672a4c2ede`, parent `94bfd92`. Lis-le par `git diff 94bfd92 cef5ea60` et les fichiers ; **dans cet arbre seulement**, tu peux lancer les essais et le banc de mutations (rien d'autre n'y est écrit ; aucun commit, aucun push, aucun réseau).
- Rendu du développeur, extrait du commit `ef51f1e8` de `prep/organisme-v65-v1` dans `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/code-v65-v1/` : `rapport-developpeur-organisme-v65-v1.md` (`f84c1430…`), suite, mutations, essai à blanc, `blocs-pour-le-texte-v65.md`, passation ; chaque fichier a son `.sha256` : vérifie-les.
- Consigne du développeur : `docs/notes/organisme-boucle-reelle-v1/consigne-developpeur-organisme-v65-v1.md` (`2dc207e7…`).
## Ce que tu vérifies
Chaque exigence M1 à M5 de la consigne (ligne de code, essai qui la tient) ; gardes de dépense et de GO, gardes 17 à 22 : cas sain et artefact (R5), aucun repli silencieux ; rejoue la suite (le développeur annonce « 232 passed, 3 skipped, 160 subtests passed ») et le banc (« 38 tuées sur 38 ») ; l'essai à blanc (9 étapes) ; ce qui ne peut être joué qu'avec `bwrap` (garde 22, M0) et ce qui reste donc non éprouvé ; la question du dossier du texte scellé (`orchestrator/prereg/` du dépôt public, ou v66) : donne ton avis.
## À écrire
`docs/notes/organisme-boucle-reelle-v1/code-v65/contre-lecture-code-v65-v2.md` dans `/home/user/controle-ia-travail` (nom neuf : la v1 interrompue n'a jamais été versée), scellé : verdict (« utilisable pour la course », « après corrections » avec la liste exacte, ou « non utilisable »), constats CLV65-01… Aucun commit. Rapport final : verdict en trois lignes, bloquants, chemin et empreinte.
