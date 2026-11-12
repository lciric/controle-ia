# Consigne — architecture complète de l'organisme d'idéation : couches, mécanismes, état — v1

- **Session mère** : nouvelle instance (reprise du 2026-11-10). Tu es un sous-agent **neuf** (rédacteur Opus). Dépôt `/home/user/controle-ia-travail` (`main`), `PYTHONPATH=src`, interpréteur `.venv/bin/python`. Sceller : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller CHEMIN`. Dépôt public de l'organisme, cloné en lecture : `/home/user/ideation-organism` (tête `6510199`). Français, presque aucun sigle ; toute heure par `date -u`. Bac à sable : `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/<ton-nom>/`. **Disque serré** : aucune copie lourde.
- **Demande de Lazar (verbatim)** : « ecir smoi le programme complet exhaustif avce toutes les couchhes et mecanismes prevus pour l'org » puis « precise bine dans le programme toutes nos idees hypotheses resultats proposiitons pour que rien de notre brinstorm ne soit perdu ».
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

## Interdits propres à cette tâche (en plus)
- **Cloison du bras d'attaque (R-2152, R-2170)** : tu n'ouvres aucun document de la session du bras, en particulier ni `docs/notes/rapports-directeur/dossier-entretien-27-novembre-v1/pieces-bras-v1/` (s'il existe), ni « organisme depuis zéro v4 », ni « programme depuis zéro v5 », ni la branche `claude/compassionate-meitner-d4ryyk`, ni `docs/notes/bras-attaque/`. Rien sur le **mode tenu à l'écart** (N-054) au-delà de son existence.
- **Sorties scellées jamais lues** (R1 : on n'ouvre pas une sortie avant le scellement de ses critères de lecture) : tu ne lis **aucune cellule** de collisionneur ni aucune réponse de modèle **non encore synthétisée**, en particulier rien sous `donnees/` ni sur les branches `donnees/…` (collisionneur v8 : tour 2 N12-N13, convergence v3, sélection, bac à sable ; collisionneur v9 du 2 novembre). Tu les **listes** comme « payées, scellées, non lues » à partir du registre, avec chemin, commit et dépense. Tu lis les **synthèses scellées** qui en existent.
- **Niveau méthode seulement (R-607)** : aucune recette opérationnelle d'attaque contre un moniteur ou un juge ; une idée d'attaque se décrit par sa classe et son but, jamais par son mode d'emploi.
- Tout chiffre ou toute affirmation renvoie à un chemin et une empreinte (R6), ou à une ligne R- du registre ; ce qui n'a pas de source est dit « sans source » et n'est pas affirmé. Ne confonds jamais « codé », « décidé », « prévu », « fermé », « proposé non tranché », « idée non retenue ».

## Objet
Écrire le **programme complet de l'organisme d'idéation** côté architecture : toutes les couches et tous les mécanismes prévus, chacun avec son état exact (codé — dans quel commit et quelle version ; décidé — par quelle décision ; prévu — par quel texte ; fermé — par quel nœud ; proposé non tranché). Un rédacteur voisin fait en parallèle l'inventaire exhaustif des idées (`docs/notes/rapports-directeur/programme-organisme-complet-v1/inventaire-idees-organisme-v1.md`) : ne le refais pas ; si tu le trouves sur disque à la fin, ajoute des renvois.

## Contenu attendu (structure minimale)
1. Objectif ultime et lien entre les deux lignées (N-044, N-045, R-2152) ; ce que l'organisme n'a pas encore (se concevoir seul, figé après conception, universalité mesurée).
2. **Couches 1 à 4** : définition, état, décisions (couche 3 réécriture de soi sous bac à sable, couche 4 pôle théorie et Lean ; N12 (b), R-959 ; R-2199 : lecture du tour 2 N12-N13, puis devis de l'essai « preuve formelle contre suite bon marché », puis note de conception du pilier « génération » ; écart vérification / génération ; renvoi N3 du pont fiche → loi).
3. **Rôles et pôles** du code (proposeur, juge, expérimentateur, lecteur, vérificateur, aiguilleur, bisociateur, metteur en fusion, moissonneur…), avec fichiers et versions.
4. **Juge statistique** (e-valeurs, nul des lois connues, nul v8 → v9, multiplicité, O2 resserrée N-064), **mondes plantés et oracles** (N-058, N-060), **pont fiche → loi** (D-P1), **tests de mort** et bac à sable (`bwrap`), **tour fermé**, **boucle réelle v65** (préalables : contre-lecture du code, machine à bac à sable, préenregistrement ; GO-2026-11-08-02, 45 USD, 30 novembre).
5. **Attaques et défenses du juge** (A1, A1-bis, A1-v3, A1-v4 : niveau méthode, résultats scellés seulement).
6. **Composition apprise, coût dans le signal, héritage, vivier de tâches fraîches, test final lu une fois** (N-045, N-049, N-050), contre-lecteur (N-052), audit défensif (N-053).
7. **Rôles de l'organisme dans le programme** (N-065 : second terrain du papier C, atelier d'idées, famille de menaces diffuses à trancher).
8. Calendrier, dépenses engagées et GO ouverts pour l'organisme ; nœuds ouverts chez Lazar ; prochain pas de chaque chantier.
Une table finale « mécanisme → état → source ».

## À écrire
- `docs/notes/rapports-directeur/programme-organisme-complet-v1/programme-organisme-complet-v1.md` (source) et sa version `.html` lisible ; si l'outil est disponible sans réseau (Chromium et Playwright sont préinstallés : `require('playwright')` ou Python `playwright` s'il existe), un `.pdf` imprimé depuis le HTML ; sinon dis-le.
- `docs/notes/rapports-directeur/programme-organisme-complet-v1/registre-affirmations-programme-v1.md` (chaque affirmation → source) et `docs/notes/rapports-directeur/programme-organisme-complet-v1/journal-programme-v1.md`.
- Jalons scellés. Aucun commit. Rapport final : chemins, empreintes, nombre de pages, trous.
