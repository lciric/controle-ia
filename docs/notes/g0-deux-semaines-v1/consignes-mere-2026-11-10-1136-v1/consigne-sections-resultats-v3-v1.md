# Consigne — sections de résultats v3 pour le dossier d'entretien — v1

- **Session mère** : nouvelle instance (reprise du 2026-11-10 ; brief `registres/passations/brief-successeur-mere-2026-11-10-v1.md` § 5 point 11 ; demande `registres/passations/demande-successeur-dossier-fusionne-v2-2026-11-10-v1.md`). Tu es un sous-agent **neuf** (rédacteur). Dépôt `/home/user/controle-ia-travail` (`main`), `PYTHONPATH=src`, interpréteur `.venv/bin/python`. Sceller : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller CHEMIN`.
- Français, presque aucun sigle ; toute heure par `date -u`. Bac à sable : `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/<ton-nom>/`.
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

## Objet
Les sections de résultats v2 ont été **interrompues** par le quota (non scellées, à ne pas tenir pour rendues) : `docs/notes/rapports-directeur/resultats-pour-documents-v2/section-resultats-programme-v2.html` et `section-resultats-organisme-v2.html`. Écris la **v3**, sous un nom neuf, dans `docs/notes/rapports-directeur/resultats-pour-documents-v3/` : `section-resultats-programme-v3.html`, `section-resultats-organisme-v3.html`, un registre des affirmations `registre-affirmations-v3.md` (chaque chiffre ou affirmation → chemin et empreinte, R6) et un journal `journal-v3.md`. Les v2 servent de point de départ, vérifiées point par point ; elles restent intactes.

## Contenu attendu
Celui de la consigne v2 (R-2179) : décisions du 10 novembre ; correction sur le témoin d'adaptateur (dose 1 seulement, note 2a `premisses-trace-interne-v1-point-2a.md`) ; A1-v4 (verdict officiel scellé, R-2111) ; code v65 de l'organisme (R-2177, rendu non encore contre-lu : le dire) ; collision Qu, Chen, Wang (R-2177) ; corrections de l'état de l'art vérifiées sur PDF. **Plus** : rendus de l'état de l'art arrivés depuis (R-2180 à R-2190) et les décisions de Lazar prises entre-temps (R-2175, R-2182, R-2130 : entretien visé le 27). Lis ces lignes par `grep -n '^| R-2\(1[0-9][0-9]\) ' registres/decisions.md`.
- **Aucun taux de calibration**, sous aucune forme (R-2185).
- **Aucun résultat** de la mesure unanime, de la lecture B de 7a, des sondes de 7a, ni du bras d'attaque au-delà des décisions inscrites au registre de `main`.
- Une affirmation qui n'a pas de source scellée est retirée, pas adoucie. Ce qui est en cours est dit « en cours », avec sa date visée (calendrier R-2177).
- Les réserves de chaque résultat sont écrites à côté de lui. La réponse d'Argon à la question mère v3 ne peut être citée qu'avec la mention que sa consigne n'a pas été versée (R-2191).

## Fin
Scelle les quatre fichiers. Aucun commit. Rapport final à la mère : chemins, empreintes, verdict en une ligne, ce que tu as retiré des v2 et pourquoi.
