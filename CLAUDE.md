# Contrôle boîte blanche des menaces diffuses — consignes permanentes

Dépôt du programme de Lazar (directeur). Tu l'exécutes selon le brief v2.
Langue : français, tutoiement avec Lazar, quasi aucun acronyme (développe les termes).
La continuité vit dans les fichiers, jamais dans la mémoire de conversation.

## Documents qui font foi
- `docs/brief-claude-code-programme-complet-v2.md` — prime pour l'exécution (missions, phases, portes, arrêts).
- `docs/programme-controle-ia-v2.md` — prime sur le fond (hypothèses, expériences, portes).
- `docs/etat-de-l-art-controle-ia-v1.md` — pris, ouvert, à battre ; aucun chiffre opposable avant vérification (R7).
- Empreintes : `docs/sha256sums-lancement-v2.txt` ; brief v1 remplacé, archivé sans modification : `docs/brief-claude-code-phase0-v1.md`.
- Toute nouvelle version transmise par Lazar remplace la précédente, qui reste archivée dans `docs/`.
- Décisions de Lazar sur les nœuds qui fixent la lecture du programme (en attendant une version nouvelle) : `docs/decisions/` (N-003, N-004 : énoncés retenus de T et L ; N-007, N-008 : H2 reformulée, bases ajoutées, critère de G1 sans F1 ; N-005, N-006 : HC1 à destination libre, porte GC réécrite, HC5 ; P-008 : trois affirmations du programme corrigées, sections 3 et 6 ; N-013 : revendications précisées après le niveau 2 de l'état de l'art — HC1, HC3, HC4, HC5, HC2b renommée, H5, H6, H7).

## Dépôt distant
Dépôt de travail : `https://github.com/lciric/controle-ia-travail` (privé), branche `main`, dès que Lazar a renommé l'ancien `lciric/controle-ia` et l'a repassé en privé (N-016, R-115). Pousser à chaque passation.
**Ne jamais pousser ce dépôt vers `lciric/controle-ia`** : ce nom sera la copie expurgée publique, régénérée par `scripts/depot_expurge.py`. Tout lancement d'instance passe `DEPOT_URL=https://github.com/lciric/controle-ia-travail.git` : les scripts scellés gardent l'ancien défaut.

## Phase en cours
Phase 0 — instruments (M0 : 5 octobre → 1er novembre 2026) ; porte de sortie G0.
État vivant, tâches ouvertes, GO en attente, décisions et dépenses : `registres/etat.md`.

## Routine de reprise — au début de CHAQUE session (R14)
1. `cd docs && sha256sum -c sha256sums-lancement-v2.txt` ; puis `python -m controle_ia.scellement verifier-arbre .` (avec `PYTHONPATH=src`).
2. Lire `registres/etat.md` et la dernière passation dans `registres/passations/` (la plus récente par nom).
3. Appliquer les défauts échus : toute décision « proposer avec recommandation » sans réponse depuis 48 heures prend son défaut ; le consigner dans `registres/decisions.md` et `registres/etat.md`.
4. Inventorier les instances de calcul actives (Vast.ai : `vastai show instances`) ; toute instance sans tâche en cours s'arrête par son identifiant (R10) et se consigne dans `registres/arrets.md`.
5. Lancer les tests : `python -m pytest -q`. Puis reprendre à la « prochaine action » de la dernière passation.

## Passation — à la fin de CHAQUE session (R14)
- Écrire `registres/passations/AAAA-MM-JJ-HHMM.md` (heure UTC) : fait, reste, réserves, prochaine action, instances actives. La sceller ; ne jamais la réécrire.
- Mettre à jour `registres/etat.md`, committer, pousser.

## Règles gelées — sans discussion
- R1 Préenregistrement scellé (hypothèse, prédiction chiffrée et signe, métrique, seuil, plan d'analyse, critères de lecture gelés, liste d'arrêt) avant toute expérience décisive, simulation comprise ; aucune lecture de résultat avant scellement.
- R2 Chaque préenregistrement est contre-lu par un sous-agent neuf qui ne l'a pas écrit ; lui donner explicitement les fichiers à lire ; sinon le signaler.
- R3 Aucun run visant un signe positif.
- R4 Symétrie : un résultat suspect de propreté, positif ou négatif, déclenche le même audit ; trop beau = réserve.
- R5 Toute garde d'arrêt testée sur un cas sain et sur un artefact ; aucun repli silencieux.
- R6 Tout dépôt reçoit une empreinte compagnon `.sha256` ; tout chiffre d'un document renvoie à un chemin et une empreinte.
- R7 Provenance par transcription non opposable : aucun chiffre de l'état de l'art sans vérification sur PDF empreinté, page citée.
- R8 Anti-faux-gap : zone vierge = question ; limitation d'un papier ≠ trou du champ ; zones vierges séduisantes vérifiées plus durement.
- R9 Graines par `numpy.random.SeedSequence` (numpy ≥ 1.25), dérivées par tâche, consignées dans un manifeste par run (configuration et empreinte, versions, graines, commit).
- R10 Arrêts par PID ou identifiant d'instance, jamais par motif de ligne de commande.
- R11 Fichier qui semble vide ou absent : vérifier sur disque et par empreinte avant de le déclarer absent.
- R12 Versions dans les noms ; nouvelle version = nouveau nom ; on n'écrase jamais ; livrables d'une tâche en zip versionné.
- R13 Verdict de porte prononcé par un sous-agent neuf (ni auteur du préenregistrement ni de l'analyse), qui applique les critères gelés ; scellé, puis soumis à Lazar pour GO.
- R14 Chaque session commence par la routine de reprise et finit par une passation.

## Hiérarchie de décision
- Routine (tu décides, tu consignes dans `registres/decisions.md`) : code, bibliothèques, tests, lectures, fichiers, tout travail sur processeur.
- Proposer avec recommandation (défaut appliqué après 48 heures) : couches et concepts de sondes, portage des environnements, périmètre interne d'une phase, D1, D2, D3.
- Nœuds de décision (arrêt, attendre le GO) : porte ; toute dépense de calcul (devis par phase) ; compte, dépôt distant, soumission, publication ; contact externe (tu rédiges, Lazar envoie) ; modification d'hypothèse ou de revendication ; écart à un préenregistrement scellé ; zone revendiquée trouvée occupée ou collision plus large ; déclencheur de bascule.

## Outils du dépôt
- Environnement : `python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements-cpu.txt` ; `PYTHONPATH=src`.
- Tests : `python -m pytest -q`.
- Sceller / vérifier : `python -m controle_ia.scellement sceller|verifier FICHIER…` ; `… verifier-arbre .`.
- Manifeste de run et résultats rattachés : `src/controle_ia/manifeste.py` ; préenregistrements : `src/controle_ia/prereg.py`, gabarit `prereg/gabarit-preregistrement-v1.md`.
- Run factice de bout en bout : `python -m controle_ia.run_factice`.
- Garde de calcul et de R10 : `.claude/hooks/garde_calcul.py`, activée par `.claude/settings.json` ; tout lancement d'instance payante doit citer un GO valide de `registres/go.md` (`GO_ID=GO-AAAA-MM-JJ-NN …`).

## Arborescence
`docs/` documents qui font foi, notes, sources ; `prereg/` préenregistrements scellés ; `registres/` état, go, dépenses, décisions, arrêts, veille, passations ; `src/controle_ia/` code ; `tests/` ; `runs/` un manifeste par run ; `diag/` résultats bruts scellés ; `papiers/A|B|C/` ; `livrables/` zips versionnés.

## Communication avec Lazar
Verdict d'abord (1 à 3 lignes), puis erreurs, changements, décisions, une ligne chacun. Format de décision : décision en une phrase ; enjeu ; 2 ou 3 options (avantage, inconvénient) ; recommandation et confiance ; défaut sous 48 heures.
Écrire seulement pour : prononcé, réserve, divergence non résolue, demande de GO, dépense. Le reste vit dans les registres.

## Interdits
Franchir une porte sans verdict scellé et GO ; dépenser sans GO sur devis ; moyenne ou médiane sur les tokens dans une sonde de production ; chiffre non vérifié dans un préenregistrement ou un papier ; changer de modèle sans GO ; contacter, soumettre, publier, ouvrir un dépôt public ; modifier le programme (tu proposes, Lazar décide).
