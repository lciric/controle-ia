# Consigne : texte court préenregistré du barreau 6 — « accumuler bat le score action par action » — brouillon 1 — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-10 à 15:36 UTC (heure relevée par `date -u`). Mot de Lazar recopié en R-2175, verbatim : « Accumuler bat le score action par action Non : rien n'est préenregistré pour cela avant le 27 : je veux le faire aussi » ; décision de la mère : « texte court préenregistré (barreau 6 de l'échelle), lu sur des scores déjà prévus, sans dépense nouvelle ; tout point qui toucherait H1, G1 ou le mode tenu à l'écart (N-054, N-055, N-056) est remonté comme nœud avant scellement ». Destinataire : un **rédacteur neuf** qui n'a écrit ni T0.6, ni T0.7, ni T0.8, ni P3-bis, ni le rapport des prémisses. Tu lis T0.7 : tu es exclu ensuite de tout rôle de lecteur de P3-bis.

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

Exception à la règle 4 : aucune. Tu n'écris que sous `brouillons/accumulation-barreau6-v1/` et dans ton bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/barreau6/`. Aucun commit, aucun appel de modèle, aucune dépense. **R7** : aucun chiffre de l'état de l'art sans PDF empreinté, page citée ; **R8**. Sceller : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller CHEMIN`. Gabarit : `prereg/gabarit-preregistrement-v1.md` ; le texte doit passer `controle_ia.prereg.problemes` (marqueurs exceptés).

## À lire (empreintes à vérifier)
- Rapport des prémisses `docs/notes/rapports-directeur/premisses-trace-interne-v1.md` (`2638558e…`), barreau 6 ; registre R-2171, R-2175.
- T0.7 brouillon 22 (`brouillons/T0.7-sondes-v0-v1-brouillon22.md`, `8b84cba5…`) : scores par action (`scores-actions-t07.npz`), agrégations par épisode, lignes `SCORES-T07`, `SONDES-T07`, ordre des lectures, interdit de la moyenne sur les jetons ; T0.6 scellé (`prereg/T0.6-organismes-v0-v1.md`, `ef31feff…`) pour les épisodes et les doses ; base (A) scellée (`72b067d5…`).
- Programme : `docs/programme-controle-ia-v2.md` (H1, H2, G1) et décisions `docs/decisions/` N-007, N-054, N-055, N-056 (lues pour **éviter** d'y toucher : G1 doit battre les bases (ii) cascade et (iii) dernier état ; H1a porte la revendication ; mode tenu à l'écart).
- État de l'art : `docs/sources/lecture-pdf-niveau2/rapport-lot3-Ab-accumulation-agregation-v1.md` (`fca3f01c…`).

## Mandat
1. Énoncé : sur les épisodes et les doses de 7b, avec les sondes et scores **déjà prévus** par T0.7 (aucun calcul neuf sur activations, aucune sonde neuve), un score **accumulé sur l'épisode** (agrégateur fixé d'avance, jamais une moyenne sur les jetons d'une sonde de production) sépare-t-il saboteur et honnête mieux que le **meilleur score action par action** (maximum par épisode, ou règle fixée d'avance) ? Prédiction chiffrée et signe, métrique, seuil, plan d'analyse, critères gelés, liste d'arrêt (R1).
2. **Ordre** : scellé avant toute ouverture des scores de l'étape A (`SCORES-T07`) et avant la création de 7b si possible ; lu après les lectures de T0.7, jamais avant ; rien vers le lecteur du verdict de P3-bis.
3. **Frontière** : écris en tête ce que ce texte **ne dit pas** sur H1, G1 et le mode tenu à l'écart ; si l'énoncé, l'agrégateur ou la lecture touchent la revendication de H1a, les bases de N-056 ou un mode de sabotage, **arrête-toi et écris le nœud** (options, recommandation) au lieu de trancher.
4. Puissance par dose aux effectifs de 7b, par un script à nom neuf versé avec sa sortie.
5. Marqueurs pour ce qui manque (commit du code de lecture, clé du registre, par exemple `SCELLEMENT-ACCUMULATION-B6` ; marque `T07` ou autre : dis laquelle et vérifie qu'elle ne fait pas refuser la garde de T0.7, `registre_v1.classer_cle_inconnue`).

## Sorties (noms neufs, scellées)
`brouillons/accumulation-barreau6-v1/accumulation-barreau6-v1-brouillon1.md`, journal, script et sortie de puissance. Rapport final : chemins, empreintes, nœuds pour Lazar, questions pour la mère.
