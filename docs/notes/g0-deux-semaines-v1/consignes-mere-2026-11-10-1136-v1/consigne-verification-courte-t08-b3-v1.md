# Consigne : vérification courte du différentiel du brouillon 2 au brouillon 3 de T0.8 — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-10 à 14:46 UTC (heure relevée par `date -u`). Tu es un sous-agent **neuf**, vérificateur, d'un autre modèle que le rédacteur (Opus 5.5) ; tu n'as écrit ni T0.8, ni ses contre-lectures, ni la base (A), ni le texte de validité de l'adaptateur. Tu ne lis aucun fichier de T0.7.

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

Exception à la règle 4 : aucune. Bac à sable : `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/verif-t08-b3/` (scripts exécutés depuis des copies, `python -I`). Aucun appel de modèle, aucune dépense. Sceller : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller CHEMIN`.

## À lire (empreintes à vérifier)
- `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon3.md` (`947994e4…`), couples (`d5f780bb…`), script, journal (`b6f5dd83…`) ; brouillon 2 (`46d8dab5…`).
- Vérification courte du brouillon 2 : `prereg/contre-lectures/T0.8-bases-boite-noire-v0-v1-brouillon2-verification-courte-v1.md` (`d9c6d3e7…`).
- Texte de validité de l'adaptateur (pièce HD) : `brouillons/validite-adaptateur-v1/validite-adaptateur-preenregistrement-v1-brouillon3.md` (`defd8ef0…`) ; base (A) scellée `prereg/T0.8-base-A-mots-et-cout-v1.md` (`72b067d5…`) ; registre R-2243, R-2245, R-2247.

## Mandat
1. Rejoue le script sur une copie du brouillon 2 : empreinte après les 14 couples VTC seuls `472b9638…`, puis brouillon 3 à l'octet.
2. **Couples CQ6-01 à CQ6-18** (lecture des épisodes du témoin distillé honnête, point 8 bis) et R3-01 à R3-15 : un par un, conformes ? Aucun signe, seuil ni critère de lecture ne change-t-il ? P8-11 (ligne neuve, descriptive, sans signe, en section gelée) : acceptable comme description fixée d'avance, ou nœud ? L'ordre de lecture (après les tables D et F, règles fixées avant toute sortie de la pièce HD, rien vers le lecteur du verdict de P3-bis) tient-il ? Les champs lus sont-ils bien les seuls champs d'action, jamais l'adaptateur ni une ligne VA ?
3. Concordance avec le texte de validité (noms de fichiers et de lignes `SORTIES-HD-VADAPT`, formes des fichiers) et avec la base (A).
4. **Verdict** : « gelable » ou « gelable après corrections » (couples exacts) ou « nœud » (lesquels).

## Sortie
`prereg/contre-lectures/T0.8-bases-boite-noire-v0-v1-brouillon3-verification-courte-v1.md`, scellé ; constats VT3-n. Rapport final : chemin, empreinte, verdict en une ligne, constats bloquants.
