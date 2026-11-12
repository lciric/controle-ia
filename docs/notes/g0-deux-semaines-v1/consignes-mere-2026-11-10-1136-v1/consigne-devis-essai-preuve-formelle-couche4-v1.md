# Consigne — devis et dessin de l'essai « preuve formelle contre suite bon marché » (couche 4, pas (b) de R-2199) — v1

- **Session mère** (`session_01VJdZpSMxSdk2SJ1ScmdfNv`). Tu es un sous-agent **neuf** (rédacteur Opus) ; tu n'as écrit ni les questions ni les synthèses N12-N13. Dépôt `/home/user/controle-ia-travail` (`main`), `PYTHONPATH=src`, `.venv/bin/python`. Sceller : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller CHEMIN`. Français ; heures par `date -u`. Bac à sable : `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/<ton-nom>/`.
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

## Interdits propres
Cloison du bras (R-2152, R-2170) ; aucune sortie scellée non lue (rien sous `donnees/`, aucune cellule de collisionneur) : tu lis les **synthèses** seulement ; aucun appel de modèle, aucune installation réseau, aucune dépense : tu écris un **devis**, pas une course.
## Objet
Décision de Lazar N12 (b) (R-959) : couches 3 et 4 fermées jusqu'aux résultats de l'étape 2, sauf un **essai sur processeur « preuve formelle contre suite bon marché »**, sur devis d'appels de sous-agents. Mot de Lazar (R-2199) : (a) lecture du tour 2 (faite), **(b) devis de cet essai, puis GO**, (c) ensuite la note de conception du pilier « génération ». Écris le **brouillon 1 du dessin et du devis** de l'essai, prêt à devenir un préenregistrement (R1) après contre-lecture et GO.
## À lire
- `docs/notes/ideation-organisme-v1/course-2/collisionneur-n12-n13-v1/synthese-n12-n13-tour2-v1.md` (`6ef6bc2e…`), en particulier la section sur la couche 4 (forme d'une ouverture, points de l'essai tenus par au moins trois espèces, désaccords, dépense) ; `synthese-n12-n13-v2.md` (`f0340581…`) ; registre R-920, R-946, R-957, R-959, R-2199 et les lignes suivantes.
- Le programme complet de l'organisme v2 (`docs/notes/rapports-directeur/programme-organisme-complet-v1/programme-organisme-complet-v2.md`, `dffe0b63…`), § 2.5 (couche 4) et partie II famille MAT (8 entrées).
- Vérifie ce qui est installé (Lean, mathlib, autre vérificateur) **sans réseau** : `which lean lake` et équivalents ; dis-le.
## Contenu attendu
1. Question exacte de l'essai ; hypothèse et prédiction chiffrée avec signe ; métrique (rappel par classe d'erreurs, fausses alertes sur preuves saines, coût apparié) ; seuil ; issues écrites d'avance (R3 : aucune issue n'est visée).
2. Banque : plantée par un tiers, découverte et confirmation séparées ; contrôles de fidélité de la formalisation (énoncé voisin prouvé, spécification altérée, énoncés sains renotés) ; qui formalise (modèle d'une autre famille que la suite, ou opérateurs) — désaccord des espèces à trancher : donne options et recommandation.
3. Bras : vérification par Lean (ou autre) contre « suite bon marché » (définir) ; puissance réglée sur les paires discordantes.
4. **Devis** par élément (appels de sous-agents : modèle, jetons, prix publics que tu cites avec leur source ou que tu marques « à vérifier » ; outillage ; durée), attendu et pire cas, plafond et coupures ; aucune dépense avant GO de Lazar.
5. Ce que l'essai décide et ne décide pas (N12 (b) : la couche 4 reste fermée jusqu'aux résultats de l'étape 2 ; points à la limite relevés par le lecteur du tour 2 : ouverture sur le seul essai, suite bon marché comme standard, bornage attribué au directeur — à ne pas reprendre).
6. Lien vers le pas (c) : ce que l'essai apprendra pour un pilier de **génération** de mathématiques nouvelles (les espèces n'en ont rien dit).
## À écrire
`brouillons/couche4-essai-preuve-formelle-v1/essai-preuve-formelle-devis-v1-brouillon1.md` et `…-journal-v1.md`, scellés. Aucun commit. Rapport final : chemins, empreintes, devis attendu et pire cas, décisions à poser à Lazar (format : décision ; enjeu ; options ; recommandation et confiance ; défaut).
