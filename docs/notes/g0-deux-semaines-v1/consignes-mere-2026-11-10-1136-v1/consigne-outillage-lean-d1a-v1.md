# Consigne : outillage de l'essai Lean, D-1a (machine dédiée isolée, aucun appel de modèle, GO-2026-11-10-13) — v1

Session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, écrite le 2026-11-10 à 23:57 UTC (heure relevée par `date -u`). **Dépense autorisée** : GO-2026-11-10-13 (65 USD au plus ; outillage seul, D-1a ; machine dédiée isolée, D-2 (i) ; destruction par identifiant au plus tard 48 heures après la création ; **aucun appel de modèle**) ; R-2265, R-2285. Tu es un sous-agent **neuf**, développeur et opérateur ; tu n'as écrit ni le dessin de l'essai, ni ses contre-lectures.

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

**Exceptions de cette consigne, et elles seules** : (1) API de Hetzner avec `HCLOUD_TOKEN` lu par son nom (jamais affiché ni écrit), commande de création citant `GO_ID=GO-2026-11-10-13` ; un seul serveur créé par toi, nommé `lean-outillage-d1a`, détruit par son identifiant (R10) avant la fin de ta session de travail et au plus tard 48 heures après sa création ; aucun autre serveur touché (inventaire par identifiants et noms seulement) ; (2) SSH vers ce seul serveur (clé jetable de ton bac à sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/outillage-lean/`) ; (3) **aucune clé de modèle, aucun dépôt du programme, aucun fichier du programme sur la machine** hors le harnais (D-2 (i), CLP-04, VL-05) ; (4) code neuf sur la branche `prep/lean-outillage-d1a-v1` (arbre réduit à créer depuis `main` : `git worktree add --no-checkout`, `git sparse-checkout init --no-cone`, motifs `/*`, `!/*/`, `/src/`, `/tests/`, `/scripts/`, `/brouillons/couche4-essai-preuve-formelle-v1/`, puis `git checkout` ; jamais `docs/notes/bras-attaque/`), poussée de cette seule branche, garde des secrets à 0 avant chaque commit (enchaînée par `&&`) ; **aucune fusion dans `main`** (l'arbre `src/` et `tests/` de `main` doit rester inchangé jusqu'au scellement de T0.7, R-2231). Refus d'un contrôle → arrête-toi et rapporte-le tel quel.

## À lire (empreintes à vérifier)
- Dessin et devis, brouillon 3 : `brouillons/couche4-essai-preuve-formelle-v1/essai-preuve-formelle-devis-v1-brouillon3.md` (`717259ed…`), § 9 (pièces « À REMPLIR »), sections sur la machine, l'isolement (VL-05), les gardes G-L1 à G-L7, A7, A8, A12 ; journal v3 ; vérification courte `prereg/contre-lectures/essai-preuve-formelle-devis-v1-brouillon2-verification-courte-v1.md` (`38e40d21…`) ; contre-lecture 1 (`f565d51c…`).

## Mandat (dans l'ordre)
1. **Sans dépense d'abord** : écris le harnais et l'environnement isolé (code neuf, essais R5 : chaque garde avec un cas sain et un artefact ; l'épreuve d'isolement qui a un sens sur une machine sans dépôt : aucune clé, aucun réseau sortant après l'installation, chaîne et Mathlib en lecture seule, dossier neuf par item, aucune persistance) ; commit, push.
2. **Puis la machine** : un serveur Hetzner (processeur ; type choisi pour tenir 65 USD même à 48 heures ; prix horaire relevé) ; installe Lean et Mathlib à un **commit épinglé** (versions notées), le harnais ; **coupe le réseau sortant** et éprouve l'isolement (cas sain et artefacts) ; mesure ce que le dessin demande (taille de Mathlib, temps de construction et de vérification d'un item jouet, gardes G-L6 et G-L7 sur la chaîne installée) ; **aucun appel de modèle, aucun code écrit par un modèle**.
3. **Détruis le serveur par son identifiant**, vérifie qu'il n'existe plus ; note la durée et le coût.
4. Verse sous `docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1/` (seul chemin d'écriture dans le dépôt hors de ta branche) : rapport `rapport-outillage-d1a-v1.md` avec les valeurs pour les pièces **VERSION-LEAN, COMMIT-MATHLIB, HARNAIS-ET-ISOLEMENT, ESSAIS-R5, MACHINE** (fournisseur, caractéristiques, prix horaire, identifiant), sorties et journaux, scellés ; **proposition de ligne de dépense** pour `registres/depenses.md` et `registres/arrets.md` (la mère l'inscrit).

## Rapport final à la mère
Commit du harnais, vie du serveur (création, destruction, heures, coût), valeurs des pièces, issues des essais R5 et de l'isolement, incidents.
