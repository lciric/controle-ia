# Consigne : contre-lecture différentielle de P3-bis — code corrigé v2 et chaîne de session — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-10 (`date -u`), autonomie de 12 heures (R-2088). Destinataire : **le contre-lecteur Fable qui a rendu la contre-lecture du code de P3-bis** (`brouillons/P3-bis-temoin-positif-v1/contre-lecture-code-p3bis-v1.md`, `7a074ad1…`, R-2076) ; il continue, toujours **sans lire aucun fichier de T0.7**.

## Interdits

Ceux de `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` (`1ee3b370…`), en entier, **règle 9 comprise** (aucune recherche récursive sans exclure les chemins interdits ; `git grep` avec exclusions). Nommément : jamais `diag/*/lecture-sondes-t06.json` ni `diag/20261109-070232-t06-reel/lecture-sondes-t06.json` ; jamais la lecture B ni `donnees/lecture-b-7a-quarantaine-v1` ; aucun `diag/`, `runs/` ni donnée de 7a, ni `essai/t06-explo-v3` ; jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; jamais l'étiqueteur ; jamais `extraire_mesures_epreuve_t06_v1.py` ; aucun fichier de T0.7. Aucun appel externe, aucune dépense, aucun `vastai` réel, aucune écriture git, aucune action dans `/home/user/wt-p3bis-lanceur` (le développeur peut y revenir).

## Lieu des essais

Arbre détaché à toi, en extraction partielle : `git -C /home/user/controle-ia-travail worktree add --no-checkout --detach /home/user/wt-p3bis-cl 776b26cb5758c464c04ab15c246f3d36050ae205`, puis `git -C /home/user/wt-p3bis-cl sparse-checkout set --no-cone '/*' '!/docs/sources/' '!/docs/notes/bras-attaque/'`, puis `git -C /home/user/wt-p3bis-cl checkout --detach 776b26cb5758c464c04ab15c246f3d36050ae205`, puis `test ! -e /home/user/wt-p3bis-cl/docs/notes/bras-attaque` ; à la fin, `git -C /home/user/controle-ia-travail worktree remove --force /home/user/wt-p3bis-cl`. `df -h /home/user` avant ; sous 3 Go libres, n'extrais pas et dis-le.

## À lire

- Ta contre-lecture (`7a074ad1…`) ; texte `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon9.md` (`eb65773f…`) ; décision `docs/decisions/decision-N-066-v1.md`.
- Code corrigé : branche `prep/p3bis-code-v2` (commit du code proposé `02217f1c`, tête `5238b2b0`), compte rendu `brouillons/P3-bis-temoin-positif-v1/compte-rendu-developpeur-code-p3bis-v2.md` (`f6c93bc5…`), sortie de l'essai de fermeture v2 (`06e84ff7…`).
- Chaîne de session : branche `prep/p3bis-lanceur-v1` (tête `776b26cb`, qui contient le code corrigé par fusion), rapports `docs/procedures/P3-bis-temoin-positif-v1/rapport-developpeur-lanceur-p3bis-v1.md` (`748568cb…`) et `…-complement-v1.md` (`59e1da14…`).
- Noms et interface : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/noms-communs-p3bis-v2.md` ; GO : `registres/go.md`, `GO-2026-11-10-02` (R-2077).

## Points à juger

1. **Différentiel du code** (`e86a6f32` → `02217f1c`) : chaque CP-01 à CP-17 réglé, réglé avec un reste, ou non ; régressions ; essais R5 neufs (cas sain et artefact) ; l'incident de `.git/info/exclude` (R-2085) ne peut plus se reproduire.
2. **Chaîne de session** : les contrôles de ton point 6 sont-ils tous écrits et éprouvés (cas sain et artefact) ; arrêts par identifiant ; arrêt à 80 USD ; code 5 ; récupération par la branche de calcul, jamais `main` ; aucune sortie en clair hors de la classe 1 ; les dix-neuf écarts du développeur et l'écart du complément (« motif du dépliage ») : acceptables, à corriger, ou au texte.
3. **Bouchons restants** dans le banc des contrôles (tokeniseur, gardes de `run_v2`, exécution des 531 essais, essai de fermeture rejoué) : la répétition finale au candidat les joue-t-elle bien tous pour de vrai ?
4. **Essais** : rejoue une fois les cinq bancs et la répétition jouet sur ton arbre (≈ 15 min), et la liste ciblée v2 si le temps le permet (≈ 20 min) ; comptes, durées, heures `date -u`.
5. **Ce qui reste avant le scellement** de P3-bis (marqueurs du brouillon 9 ou 10 que code et chaîne permettent de remplir ; épingles `A_EPINGLER` ; recompte de `TESTS_ATTENDUS_P3BIS` sous Python 3.11).

## Sortie

`brouillons/P3-bis-temoin-positif-v1/contre-lecture-differentielle-code-v2-chaine-v1.md`, scellé : verdict en une ligne ; table des défauts CD-01… (bloquant, à corriger, mineur ; fichier, ligne ; correction) ; points 1 à 5. Réponse courte : chemin, empreinte, verdict, bloquants.
