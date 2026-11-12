# Consigne : erreur de première espèce des lectures décisives de T0.7 (audit symétrique, R4) — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-10 à 16:41 UTC (heure relevée par `date -u`). Motif : la simulation sous le nul du barreau 6 (`brouillons/accumulation-barreau6-v1/nul-accumulation-b6-v1.txt`, `512108e3…`, et diagnostic `dcf8abd5…`) trouve l'intervalle percentile par blocs à 2 000 tirages **anti-conservateur dans la queue de 0,625 %** (1,7 à 2 fois le nominal quand le signal est fort) ; T0.7 lit ses lectures décisives avec `sondes.evaluation.intervalle_blocs` (percentile) à `tirages_aire` = 2 000 et `niveau_decisif` = 0,9875 ; rien ne mesure son taux réel. Destinataire : un **analyste neuf**, qui n'a écrit ni T0.7, ni son module, ni le barreau 6. Tu lis le code de T0.7 : tu es exclu ensuite de tout rôle de lecteur de P3-bis.

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

Exception à la règle 4 : aucune. Bac à sable : `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/nul-t07/`. Aucune donnée réelle (ni 7a, ni 7b, ni P3) : lois simulées seulement. Aucun appel de modèle, aucune dépense. Disque ≈ 5 Go, CPU partagé : borne ta simulation (au plus ≈ 45 min de calcul). Sceller : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller CHEMIN`.

## À lire
- `brouillons/T0.7-sondes-v0-v1-candidat1.md` (`1718f2a0…`) : « Métrique », « Seuil », « Plan d'analyse », « Critères de lecture gelés » (règle exacte d'une lecture décisive : aire, borne basse, plancher apparié, quantile du plancher, niveau, nombre de sondes, Bonferroni) ; configuration v5 (`brouillons/T0.7-sondes-v0-v1-candidat1-pieces/configuration-t07-v5.json`).
- Code gelé : `src/controle_ia/sondes/evaluation.py` (`intervalle_blocs`, plancher), `src/controle_ia/t07/lecture_v1.py` et `lecture_v2.py` (là où la lecture décisive est décidée), `src/controle_ia/t07/plancher_v1.py`.
- Simulation du barreau 6 (scripts `nul_accumulation_b6_v1.py`, `diagnostic_nul_b6_v1.py`, sorties) pour la méthode.

## Mandat
1. Écris la règle de décision **exacte** d'une lecture décisive de T0.7, telle que le code la joue (avec les numéros de ligne).
2. Simule sous le nul de cette règle (sonde **non** meilleure que le plancher, au sens exact du texte), **en appelant les fonctions du code gelé** (pas une réimplémentation), aux effectifs du texte (64 et 36 tâches, actions par tâche, nombre de sondes lues, niveau 0,9875), pour plusieurs forces de signal commun (aire du plancher basse, moyenne, haute, jusqu'à ≈ 0,94) : taux de fausse décision par sonde et de famille, intervalles de Clopper-Pearson ; à 2 000 tirages, puis à 10 000.
3. Conclusion : le niveau annoncé est-il tenu ? Sinon, de combien, dans quelles cellules, et quel remède minimal (tirages, niveau, autre méthode d'intervalle) le rétablit, **sans changer de code** si possible (clés de configuration) ; effet du remède sur la puissance, chiffré aux mêmes lois.
4. Ne recommande rien qui change une hypothèse, une prédiction ou un seuil : si le remède l'exigerait, dis-le comme nœud.

## Sorties
`docs/notes/g0-deux-semaines-v1/t07-module-v2/erreur-premiere-espece-lectures-decisives-t07-v1.md` (note), script et sorties sous `docs/notes/g0-deux-semaines-v1/t07-module-v2/erreur-premiere-espece-t07-v1/`, scellés. Rapport final : chemins, empreintes, verdict en une ligne (« niveau tenu » ou « dépassé de … »), remède recommandé.
