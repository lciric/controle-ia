# Consigne : rédiger le candidat de T0.7 (brouillon 22 + contre-lectures orchestrées + ordre brouillon 5 + marqueurs) — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-10 à 16:16 UTC (heure relevée par `date -u`). Destinataire : un **rédacteur neuf**, qui n'a écrit ni T0.7 (brouillons 1 à 22), ni son module, ni ses ordres, ni leurs contre-lectures. Ayant lu T0.7, il est exclu ensuite de tout rôle de lecteur de P3-bis.

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

Exception à la règle 4 : aucune. Tu n'écris que sous `brouillons/` (noms neufs : `brouillons/T0.7-sondes-v0-v1-candidat1.md` et ses pièces sous `brouillons/T0.7-sondes-v0-v1-candidat1-pieces/`) et dans ton bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/t07-candidat/`. Aucun commit, aucun appel de modèle, aucune dépense. Sceller : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller CHEMIN`.

## À lire (empreintes à vérifier)
- `brouillons/T0.7-sondes-v0-v1-brouillon22.md` (`8b84cba5…`), son journal, son script (méthode).
- Contre-lectures orchestrées : `prereg/contre-lectures/T0.7-sondes-v0-v1-brouillon22-cl-orchestree-v1.md` (`47537dfa…`) et couples `…-cl-orchestree-v1-couples.json` (`4c940714…`).
- Ordre : `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon5.md` (`d0b75d16…`) et sa contre-lecture `prereg/contre-lectures/ordre-execution-etape-a-t07-v1-brouillon4-cl1.md` (`88ea9f06…`, CLE-09, CLE-12).
- Configuration : `brouillons/T0.7-sondes-v0-v1-brouillon19-pieces/configuration-t07-v4.json` (`3d19b08c…`) ; `src/controle_ia/t07/lecture_v2.py` (`exiger_configuration`, calcul de l'empreinte canonique de la configuration s'il en existe un).
- Registre : R-2241, R-2246, R-2249, R-2255, R-2258, R-2259, R-2260 ; `registres/go.md` (GO-2026-11-10-04, GO-2026-11-10-06).

## Mandat (couples appliqués par un script à toi, nom neuf ; chaque « ancien » une fois)
1. **Couples des contre-lectures orchestrées** : CLO-01, CLO-02, CLO-04 à CLO-10 tels qu'écrits ; **CLO-03 non appliqué** (option (a) de GARDES-CODE-01, R-2249) ; CLO-08 (section gelée, liste d'arrêt) déclaré avec la lecture de la mère (R-2249 : précision, pas de nœud).
2. **CLE-09** : minuterie écrite « au plus 12 h, bornée par la dépense » (`HMAX` de l'ordre brouillon 5) là où le texte dit « création + 12 h » ; devis de l'étape A recopié de l'ordre brouillon 5 (cité par chemin et empreinte) ; **réserve CLE-12** écrite (une minuterie qui tombe pendant l'étape A détruit une étape ouverte ; marge ≈ 1,1 h ; durée jamais mesurée).
3. **Essais versés avant C7** (« Accord au code ») : CLC-04 (commit `31b55c92393173d01153e4c8a5a9f0d69365ce81`, `tests/test_t07_ouvrir_reel_concepts_v1.py` `6192a821…`, R-2246) et GARDES-CODE-01 (commit `2c8ab779ca6df361d562e120ba34045be675853a`, `tests/test_t07_tirages_degeneres_v1.py` `c68fd68f…`, R-2255) ; `ATT` « 346 passed, 2 skipped, 4 xfailed » (Python 3.13.16 et 3.11.17).
4. **Marqueurs remplis** :
   - `ENTROPIE_T07` = `141327499974890102043551261780374423878` (R-2259) ;
   - `EMPREINTE_CONFIG_T07` : écris la configuration finale `brouillons/T0.7-sondes-v0-v1-candidat1-pieces/configuration-t07-v5.json` = v4 avec `entropie` remplie (et rien d'autre changé, sauf ce que l'ordre brouillon 5 exige : dis-le un par un) ; vérifie que `lecture_v2.exiger_configuration` la passe ; scelle-la ; le marqueur reçoit le chemin **final** que nomme l'ordre brouillon 5 (copie sous `prereg/`, faite par la mère au scellement, octets égaux) et l'empreinte (celle que le module ou l'ordre appelle « canonique » : dis laquelle) ;
   - `EMPREINTE_ORDRE_EXECUTION_ETAPE_A_T07` = `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon5.md`, `d0b75d161e80efbd4b1e5e6ca8f2cc49476bf90801cae57617b2cc553a92108b` ;
   - `GO_ETAPE_A_T07` = « `GO-2026-11-10-06` (extension de `GO-2026-11-10-04` à la variante B, voie nominale ; 20 USD au total sous les deux lignes) » ;
   - `ESSAI_CLC04_T07` = point 3 ;
   - **`MOT_LAZAR_P064` et `MOT_LAZAR_P065` restent** (la mère les remplit après l'échéance de 17:13 UTC, par la ligne du registre qui constate le défaut).
5. Section « Contre-lecture » : entrées des contre-lectures orchestrées et de l'ordre ; statut « candidat 1 » ; en-tête décrivant ce candidat ; C7 laissé à la règle (fixé par la mère juste avant le scellement).
6. **Sections gelées** : seul CLO-08 les touche ; vérifie par programme que tout le reste des sections gelées est égal à l'octet au brouillon 22 ; **aucune hypothèse, prédiction, signe ni seuil ne change** ; sinon arrête-toi (nœud).
7. `controle_ia.prereg.problemes` ne doit plus relever que `MOT_LAZAR_P064` et `MOT_LAZAR_P065`.

## Sorties (scellées ; brouillon 22 intact)
`brouillons/T0.7-sondes-v0-v1-candidat1.md`, couples, script, journal, configuration v5. Rapport final : chemins, empreintes, couples, marqueurs restants, questions.
