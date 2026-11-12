# Consigne : code du remède (a) de T0.7 — règle « au-dessus du plancher » par différence appariée (préparé, non fusionné) — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-10 à 18:36 UTC (heure relevée par `date -u`). **Préparation réversible, en attente du mot de Lazar** (nœud de R-2270, R-2271) : rien n'est fusionné dans `main`, rien ne remplace le code contre-lu tant que Lazar n'a pas choisi (a). Tu es un sous-agent **neuf**, développeur ; tu n'as écrit ni T0.7, ni son module, ni l'audit. Tu lis T0.7 : tu es exclu ensuite de tout rôle de lecteur de P3-bis.

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

**Exception à la règle 4, dans l'arbre `/home/user/wt-t07-plancher-v2` seulement** (branche `prep/t07-plancher-v2-v1`, depuis `fecbbcfe` ; extraction réduite) : `git add`, `git commit` de tes seuls fichiers neufs, `git push -u origin prep/t07-plancher-v2-v1` (retentatives 2, 4, 8, 16 s) ; garde des secrets à 0 avant chaque commit (`git diff --cached | grep -cE '(sk-ant-[A-Za-z0-9]|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|hf_[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{12})'` = 0, enchaîné par `&&`) ; message terminé par `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. **Aucun fichier existant modifié** (R12 : fichiers neufs `*_v2.py`/`*_v3.py`). Mutations sur copies avec `-o pythonpath=` et import tracé (R-2246). Bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/dev-plancher-v2/`. Python : `/home/user/controle-ia-travail/.venv/bin/python`. Aucun appel de modèle, aucune donnée réelle, aucune dépense. Sceller : `PYTHONPATH=/home/user/controle-ia-travail/src /home/user/controle-ia-travail/.venv/bin/python -m controle_ia.scellement sceller CHEMIN`.

## À lire (dans `/home/user/controle-ia-travail/`, empreintes à vérifier)
- Note v2 `docs/notes/g0-deux-semaines-v1/t07-module-v2/erreur-premiere-espece-lectures-decisives-t07-v2.md` (`5ccf0940…`), section « Changements au module », et prototype `docs/notes/g0-deux-semaines-v1/t07-module-v2/erreur-premiere-espece-t07-v1/remede_a_prototype_v1.py` (`3e488d70…`) ; note v1 (`8e996ab0…`).
- Module : `src/controle_ia/t07/plancher_v1.py`, `lecture_v1.py` (l. ≈ 860-880), `lecture_v2.py` (`etape_b`, l. ≈ 1055-1070 ; `exiger_configuration`), `lectures_t07_v1.py` (l. 101, 299), `criteres_v1.py`, `src/controle_ia/sondes/evaluation.py`.
- Candidat 1 de T0.7 et sa configuration v5 (dans ton arbre).

## Mandat
1. `src/controle_ia/t07/plancher_v2.py` : comparaisons par tâches (effectifs quelconques, ex aequo), aires tirées, `comparer_difference_au_plancher` (intervalle percentile par blocs de tâches de « aire de la sonde − quantile du plancher », les aires du plancher recalculées à chaque tirage ; même garde des tirages dégénérés > 1 % ; rend les clés actuelles plus `difference` et `au_dessus_du_plancher` = borne basse > 0) ; égalité au bit près à `evaluation.aire_sous_courbe` sur des tirages (essai).
2. `src/controle_ia/t07/lecture_v3.py` (`lecture_jeux_v3`, `etape_b` qui remplace l'appel de la règle, `exiger_configuration` qui exige `methode_plancher`) et `src/controle_ia/t07/lectures_t07_v2.py` (lectures de validité à 95 % : même défaut) ; `criteres_v1.etat_pour_sonde` inchangé (sens de `bas` déclaré).
3. Configuration v6 (`methode_plancher` = `"difference_appariee_percentile"`), écrite dans ton bac à sable puis versée au rapport.
4. Essais `tests/test_t07_plancher_v2_*.py` (R5 : cas sain et artefact pour chaque garde ; la règle neuve reproduit les décisions du prototype sur ses mondes de référence) ; banc de mutations ; `tests/test_t07*.py` rejoués (issues inchangées).
5. Rejoue en petit la simulation sous le nul conditionnel **avec le module** (pas le prototype) sur deux cellules dures (plafond, directions étalées ; 64 et 36 tâches) : taux égaux à ceux du prototype aux erreurs de simulation près.
6. Commit, push ; rapport scellé `docs/notes/g0-deux-semaines-v1/t07-module-v2/rapport-developpeur-plancher-v2-v1.md` : commit, empreintes des fichiers neufs, essais, banc, rejeu, et **ce que le texte de T0.7 doit changer** (sections, phrases), sans l'écrire.

## Rapport final à la mère
Commit, empreintes, essais, banc, rejeu, changements de texte à faire, points ouverts.
