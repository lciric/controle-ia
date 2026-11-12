# Consigne — contre-lecture 1 de « validité de l'adaptateur », brouillon 2, avec levée des dépendances de T0.7 — v1

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

## Rôle et exclusions
Tu n'as écrit ni ce texte, ni T0.6, ni T0.7, ni P3-bis, ni la note 2a. Tu lis T0.7 : tu es exclu ensuite de tout rôle de lecteur de P3-bis.
## À lire (vérifie les empreintes)
`brouillons/validite-adaptateur-v1/validite-adaptateur-preenregistrement-v1-brouillon2.md` (`be0851f5…`) et son journal (`d4f503d2…`) ; brouillon 1 (`022f75e2…`) ; `docs/notes/rapports-directeur/premisses-trace-interne-v1-point-2a.md` (`2db916aa…`) et `premisses-trace-interne-v1.md` (`2638558e…`) ; `prereg/T0.6-organismes-v0-v1.md`, `prereg/T0.6-organismes-config-7b-v1.json` ; `brouillons/T0.7-sondes-v0-v1-brouillon21.md` (`f7dcb226…`) ; lignes GO-2026-11-10-07 et -09 de `registres/go.md` ; R-2168, R-2175, R-2194.
## Ce que tu fais
1. Contre-lecture complète au sens de R1 et R2 (hypothèses, prédictions, seuils, plan, critères gelés, liste d'arrêt, devis sous 30 USD et coupures).
2. **Lève les sept dépendances marquées « (T0.7, non vérifié) » et les deux marqueurs** `<<CHAMP_OUVERTURE_T07>>` et `<<CHAMP_EMPREINTES_DIRECTIONS_T07>>` : pour chacun, la ligne exacte de T0.7 qui le fixe, ou « non fixé par T0.7 » avec ce qu'il faudrait.
3. Avis sur Q-1 à Q-5 du journal ; pour Q-2, lis les gardes de création d'instance des lanceurs de 7b et de P3-bis cités par T0.6 et P3-bis (code seulement) et dis si une instance du témoin bloquerait leur création.
## À écrire
`prereg/contre-lectures/validite-adaptateur-preenregistrement-v1-brouillon2-cl1.md`, scellé : verdict, couples ancien → nouveau pour chaque correction, table des neuf levées, constats CLVA-01… Aucun commit. Rapport final : verdict en trois lignes, bloquants, chemin et empreinte.
