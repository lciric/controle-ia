# Consigne : rédiger le brouillon 2 du préenregistrement de la course réelle de l'organisme (code v66, configuration v6) — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-10 à 14:29 UTC (heure relevée par `date -u`), autonomie de 12 heures (R-2201). Destinataire : un **rédacteur neuf**, qui n'a écrit ni le brouillon 1, ni le code v65 ou v66, ni leurs contre-lectures.

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

Exception à la règle 4 : lecture seule de l'arbre `/home/user/organisme-v65-cl` (branche `prep/organisme-v66-boucle-reelle-v1`, tête `7e415cba…`) par `git show` ; aucun essai à lancer. Tu n'écris que sous `docs/notes/organisme-boucle-reelle-v1/` (noms neufs) et dans ton bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/prereg-course-v66/`. Aucun commit, aucun appel de modèle, aucune dépense. Sceller : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller CHEMIN`.

## À lire (empreintes à vérifier)
- `docs/notes/organisme-boucle-reelle-v1/preenregistrement-boucle-reelle-organisme-v1-brouillon1.md` (`736e3fd6…`), devis (`docs/notes/organisme-boucle-reelle-v1/devis-boucle-reelle-organisme-v1.md`), puissance (`docs/notes/organisme-boucle-reelle-v1/puissance-boucle-reelle-v1*.py`, `sorties-puissance-v1/`), essai à blanc v1.
- Code v66 : rapport `docs/notes/organisme-boucle-reelle-v1/code-v66/rapport-developpeur-organisme-v66-v1.md` (`f6433d38…`), **blocs pour le texte** `docs/notes/organisme-boucle-reelle-v1/code-v66/blocs-v66/blocs-pour-le-texte-v66.md` (`9933ee11…`), configuration `docs/notes/organisme-boucle-reelle-v1/code-v66/configuration-v6/`.
- Contre-lectures : v65 `docs/notes/organisme-boucle-reelle-v1/code-v65/contre-lecture-code-v65-v2.md` (`c4ddfc7f…`) ; **v66** `docs/notes/organisme-boucle-reelle-v1/code-v66/contre-lecture-code-v66-courte-v1.md` (`a2880368…`) : CLV66-01 à CLV66-07.
- Registre : R-1738, R-2206, R-2215, R-2220, R-2234, R-2243 ; `registres/go.md` lignes GO-2026-11-08-02 et GO-2026-11-10-10 ; décisions N-058 (composition jugée sur l'oracle planté et le coût, jamais sur le verdict du juge), N-064, N-065 par `git grep`.

## Mandat
Brouillon 2 par **couples** appliqués par un script à toi (comme les autres préenregistrements), puis :
1. Porter les **blocs v66** au texte (code v66 `7e415cbaaa3ff602db43a44dad6b4307c08352c7`, configuration v6 `4743ddbe…`, lancement en superutilisateur avec `--utilisateur-bac 64097`, `--releve-sha256` exigé, gardes 23 et 7 dans la liste d'arrêt, mesures précisées : Wilson, jetons, échos de la loi).
2. **CLV66-01** (arrêt de la garde 18 en génération 2 lu C5 seul) : clause à la section 8, comme le recommande la contre-lecture ; **CLV66-02** (relevé sans `lecture_selection` ou sans `archives_de_jugement["2"]`) : clause à la ligne C1 ; écris-les de façon que la lecture gelée ne puisse pas les contourner.
3. **CLV66-04** (génération 1 sans carte lisible → course complète lue C1, fermeture de la boucle non éprouvée) : la phrase de résultat doit le dire ; si cela change un critère de lecture, **arrête-toi sur ce point** et écris-le comme question pour Lazar (nœud), avec options et recommandation.
4. **GO** (CLV66-07) : les conditions écrites citent une ligne de GO **neuve à identifiant neuf** que Lazar doit inscrire (code v66 contre-lu, configuration v6, machine `bwrap` validée par l'essai à blanc `--bac reel`, préenregistrement scellé, 45 USD : 40 de modèles, 5 de machine) ; marqueur `<<GO_COURSE_V66>>`. Ni GO-2026-11-08-02 ni GO-2026-11-10-10 ne suffisent tels qu'écrits.
5. Points pratiques de la contre-lecture v66 : `--collisionneur` explicite pour le relais Argon ; empreinte du `registres/go.md` copié sur la machine notée au rapport de course ; six points à jouer sous `bwrap` (section 6 de la contre-lecture) comme préalables écrits.
6. Sections gelées : tout couple qui les touche déclaré un par un ; **aucune hypothèse, prédiction, signe ni seuil ne change** sans nœud.

## Sorties (noms neufs, scellées ; brouillon 1 intact)
`docs/notes/organisme-boucle-reelle-v1/preenregistrement-boucle-reelle-organisme-v1-brouillon2.md`, couples, script, journal (questions Q-n avec recommandation). Rapport final : chemins, empreintes, nombre de couples, marqueurs restants, nœuds pour Lazar.
