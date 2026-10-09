# Premier rendu — phase 0 — v1

Date : 2026-10-04 (UTC). Dépôt : `controle-ia` (local au conteneur ; paquet git complet joint, en attendant un dépôt distant).

## Verdict
- Le socle T0.1 est en place et testé.
- La recherche d'antériorité n'est que partielle : budget de recherches web épuisé, arxiv.org refusé. Elle révèle pourtant déjà trois revendications à repositionner et deux énoncés à corriger : quatre nœuds de décision.
- Aucune dépense ; aucun GPU ne sera utilisé avant ton GO.

## Pièces
| Pièce | Contenu |
|---|---|
| `rapport-anteriorite` → `docs/anteriorite/anteriorite-transcription-v1.md` | rapport de recherche d'antériorité (niveau transcription, non opposable) |
| `docs/sources/ressources-code-v1.md` | disponibilité et licence des dépôts de code, vérifiées au commit (source primaire) |
| `docs/notes/note-mathematique-lemme-theoreme-v1.md` | démarrage de T0.3 : énoncés précis du lemme et du théorème négatif, plan de simulation |
| `plan-phase0-v1.md` | plan ordonnancé, dépendances, chemin critique, processeur ou GPU |
| `devis-v1.md` | devis détaillé de la phase 0 (≈ 69 h GPU avec marge, plafond demandé 150 USD) et ordres de grandeur du programme (≈ 1 200 à 2 700 USD) |
| `ressources-a-demander-v1.md` | ce qu'il me faut de toi, par urgence |
| `pdf-a-fournir-v1.md` | liste des PDF et pages à me fournir, sur arXiv et ailleurs, en trois niveaux |
| `message-fakelab-v1.md` | message aux auteurs de FakeLab, prêt à envoyer (titre à vérifier avant envoi) |
| `risques-v1.md` | trois risques de la phase 0, trois du programme, avec parades |
| `decisions-v1.md` | nœuds de décision N-001 à N-006 et propositions P-001, P-002, D1, D2, D3 au format de décision |
| `registres/` | état, GO, dépenses, décisions, arrêts, veille, première passation |

## Ce que T0.1 contient
- Les outils de scellement, de manifeste de run (graines par `SeedSequence`) et de préenregistrement.
- Une garde de calcul : aucun lancement payant sans GO consigné, aucun arrêt par motif de ligne de commande.
- 52 tests, chaque garde testée sur un cas sain et sur un artefact.
- Un run factice rejoué au bit près.
- `CLAUDE.md`, la routine de reprise et la passation.
