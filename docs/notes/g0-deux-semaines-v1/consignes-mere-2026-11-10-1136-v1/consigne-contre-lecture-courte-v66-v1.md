# Consigne : contre-lecture courte du différentiel v65 → v66 de l'organisme (boucle réelle) — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-10 à 13:43 UTC (heure relevée par `date -u`). Tu es un sous-agent **neuf**, contre-lecteur de code, **d'un autre modèle que le développeur de la v66** (Opus 5.5) : N-052. Tu n'as écrit ni la v65, ni la v66, ni la contre-lecture de la v65.

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

**Exception à la règle 4, dans l'arbre `/home/user/organisme-v65-cl` seulement** (branche `prep/organisme-v66-boucle-reelle-v1`, tête `7e415cbaaa3ff602db43a44dad6b4307c08352c7`) : essais ciblés, banc de mutations et essai à blanc permis (`--basetemp`, `TMPDIR` et toute sortie dans ton bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/cl-v66/`) ; toute mutation se fait sur une copie, jamais dans l'arbre ; aucun `checkout`, `commit`, `push`, `fetch`. Le registre `registres/go.md` du dépôt de travail se lit en lecture seule. Ne nettoie que ton bac à sable ; **ne touche à aucun autre dossier de `/tmp`** (un balayage de `/tmp` a été refusé au développeur par un classifieur : on ne le refait pas). Aucun appel de modèle, aucune dépense. Sceller : `PYTHONPATH=/home/user/controle-ia-travail/src /home/user/controle-ia-travail/.venv/bin/python -m controle_ia.scellement sceller CHEMIN`.

## À lire (dans `/home/user/controle-ia-travail/`, empreintes à vérifier)
- Rapport du développeur v66 : `docs/notes/organisme-boucle-reelle-v1/code-v66/rapport-developpeur-organisme-v66-v1.md` (`f6433d38…`), patch `docs/notes/organisme-boucle-reelle-v1/code-v66/organisme-v66-contre-cef5ea6.patch`, sorties de la suite, du banc et de l'essai à blanc, blocs pour le texte, dossier `configuration-v6/`.
- Contre-lecture de la v65 : `docs/notes/organisme-boucle-reelle-v1/code-v65/contre-lecture-code-v65-v2.md` (`c4ddfc7f…`) : constats CLV65-01 à CLV65-10.
- Consigne du développeur v66 : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-developpeur-organisme-v66-v1.md` (`264e8a08…`).
- `.claude/hooks/garde_calcul.py` (`lire_go`, règle des extensions, R-389) pour l'équivalence du lecteur de GO.

## Mandat
1. Pour chaque constat CLV65-01 à CLV65-10 : la correction le lève-t-elle, au code et par un essai sur un cas sain et sur un artefact ? Rejoue ce qu'il faut (suite des neuf fichiers, banc, essai à blanc) et compare aux sorties versées.
2. **Écart déclaré par le développeur** (génération 2 : un écart de membres d'archive lu C4 et non C5) : conforme au texte ou non ? Recommandation.
3. Lecteur du registre des GO : équivalent à `garde_calcul.lire_go` sur le vrai registre et sur des artefacts ; GO-2026-11-08-02 et GO-2026-11-10-10 (part « organisme ») lus à 45 USD, montants supérieurs refusés.
4. Ajoute au moins quatre mutations à toi sur les gardes neuves (23, 7, 22) et rapporte leur sort.
5. Dis ce qui n'est pas éprouvable sans `bwrap` et ce qu'il faudra jouer sur la machine de la course.
6. **Verdict** : « utilisable pour la course », « après corrections » (constats numérotés CLV66-n, chacun avec ce qu'il faut) ou « non ».

## Sortie
`docs/notes/organisme-boucle-reelle-v1/code-v66/contre-lecture-code-v66-courte-v1.md`, scellé ; rien d'autre hors du bac à sable. Rapport final : chemin, empreinte, verdict en une ligne, constats bloquants.
