# Consigne : vérification courte en différentiel du brouillon 2 de T0.8 (bases boîte noire v0) — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-10 à 14:28 UTC (heure relevée par `date -u`). Tu es un sous-agent **neuf**, vérificateur, d'un autre modèle que le rédacteur (Opus 5.5) ; tu n'as écrit ni T0.8, ni sa contre-lecture 1, ni la base (A). Tu ne lis aucun fichier de T0.7 au-delà de ce que T0.8 cite.

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

Exception à la règle 4 : aucune. Bac à sable : `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/verif-t08-b2/` (scripts exécutés depuis des copies, `python -I`). Aucun appel de modèle, aucune dépense. Sceller : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller CHEMIN`.

## À lire (empreintes à vérifier)
- `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon2.md` (`46d8dab5…`), couples et éditions (`19b629c8…`), script, journal (`6d5d1853…`) ; brouillon 1 (`ca26763a…`).
- Contre-lecture 1 : `prereg/contre-lectures/T0.8-bases-boite-noire-v0-v1-brouillon1-cl1.md` (`21499f7c…`).
- Base (A) scellée : `prereg/T0.8-base-A-mots-et-cout-v1.md` (`72b067d5…`).
- Registre : R-2175, R-2186, R-2193, R-2211, R-2216, R-2243.

## Mandat
1. Rejoue le script sur une copie du brouillon 1 : empreinte intermédiaire `7110a230…` après les 44 couples, puis brouillon 2 à l'octet.
2. **Éditions E-10 à E-27 dans les sections gelées**, une par une : nécessaire (imposée par la base (A) scellée, par un couple ou par une décision du registre) ? Change-t-elle une hypothèse, une prédiction, un signe, un seuil ou un critère de lecture ? Si oui, est-ce un nœud de Lazar (modification d'hypothèse ou de critère) ? Chaque édition jugée : conforme, à corriger (couple), ou nœud.
3. Concordance avec la base (A) : rien ne la redouble ni ne la contredit (douze traits, M2, coût normalisé, BA-L).
4. Garde neuve (contrôle d'identité de M2, tolérance 1·10⁻⁶) : écrite avec un cas sain et un artefact ?
5. Devis (attendu ≈ 17 à 30 USD, pire ≈ 57, ≈ 114 avec une relance, plafond 120) : recalculable depuis le texte ?
6. **Verdict** : « gelable après corrections » (couples exacts) ou « nœud » (lesquels).

## Sortie
`prereg/contre-lectures/T0.8-bases-boite-noire-v0-v1-brouillon2-verification-courte-v1.md`, scellé ; constats VT-n. Rapport final : chemin, empreinte, verdict en une ligne, constats bloquants.
