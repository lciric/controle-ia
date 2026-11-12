# Garde des secrets du versement `code-organisme-94bfd92` : un faux positif, traité par une exception étroite — v1

Session-dépôt, 10 novembre 2026, 11:03 UTC. Complète `LISEZMOI.md` (`e552c7eb…`), qui reste tel quel (R12).

- **Constat** : la garde standard de la session (huit motifs, compte des lignes) compte 1 ligne dans le diff de ce versement.
  C'est `orchestrator/pole/caviardage.py`, qui contient, écrit comme expression régulière, le motif d'en-tête d'une clé
  privée au format texte. Ce module **reconnaît** les clés pour les masquer ; ce n'est pas une clé. Le même module, avec
  le même motif, est déjà suivi sur `main` : `docs/notes/ideation-organisme-v1/orchestrateur-v51/pole/caviardage.py`.
- **Exception** : `garde-secrets-exception-caviardage-v1.sh`, scellé. Il ne neutralise ce motif que lorsqu'il suit
  immédiatement le texte littéral `[A-Z ]*`, c'est-à-dire sous sa forme d'expression régulière ; les huit motifs comptent
  partout ailleurs. Le script ne contient lui-même aucune correspondance.
- **Épreuves (règle 5)** : sur le cas sain, le diff de ce versement, il rend 0. Il rend 1 sur chacun des quatre artefacts :
  - un en-tête de clé RSA ;
  - un en-tête nu ;
  - le motif sous forme d'expression régulière suivi, sur la même ligne, d'un vrai en-tête ;
  - un jeton factice d'un autre type.
- **Portée** : ce versement seul. La garde standard reste celle de tous les autres commits de la session.
