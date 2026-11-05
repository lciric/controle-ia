# Orchestrateur du pôle, version 0.7.0 — prise « idéation » : v37 — taille des pièces réglable (corpus primaire) et relecture CL4 de la v36 portée — LISEZMOI v37

Lignée conv-audit (instance de reprise du 28 octobre 2026, Fable 5.1), écrit après le relevé `date -u` de **23:00 UTC** ;
v1 à v36 gardées (R12). Une seule cause : la décision de Lazar (22:47 heure de Paris) de servir les **sources primaires**
aux proposeurs et aux juges — le corpus primaire v1 (dix extraits, 245 378 caractères) et v2 (huit extraits, 195 361)
portent les pièces des proposeurs à ≈ 579 000 caractères et celles des juges à ≈ 524 000, au-dessus du plafond fixe de
400 000 de `lire_pieces` (v31 → v36).

| changement | détail | fichiers |
|---|---|---|
| `TAILLE_MAX_PIECES` (400 000, défaut inchangé) et `TAILLE_MAX_PIECES_ABSOLUE` (800 000 ≈ 200 000 jetons, plafond dur) | `executer_ideation(…, taille_max_pieces=…)` : entier dans [1, 800 000], sinon `CourseInterrompue` avant tout appel ; appliqué aux trois lots (pièces, matériau, pièces des juges) ; consigné au manifeste de départ avec les tailles servies (`taille_pieces_servies`) | `pole/ideation.py` |
| `--taille-max-pieces N` | lanceur ; le devis v7 bis demande 650 000 | `demonstrations/ideation_v1.py` |
| essai | bornes refusées, pièces trop longues refusées, réglage et tailles au manifeste | `essais/test_v7_ideation.py` |

**Relecture CL4 de la v36** (session-depot, n° 123, « lançable après corrections », aucun bloquant), portée ici aussi :

| constat | correction |
|---|---|
| **CL36-01** un échec du bras sans envoi ni dépense le condamnait | commande introuvable → `erreur` à coût 0 (rien lancé) ; `reponse.md` n'est écrit que si quelque chose a eu lieu ; en cas d'échec **sans envoi ni dépense** (commande introuvable, clé dans l'environnement, contrôle refusé sans coût), `manifeste-bras-non-joue-N.json` scellé, numéroté, bras **relançable** ; refus définitif seulement après une réponse ou une dépense ; essai (introuvable, clé, puis succès) |
| **CL36-02** contrôle d'Argon proposeur après la passe 1 | le lanceur contrôle chaque proposeur externe **avant** la passe 1 des proposeurs Claude ; son coût entre au journal (`cout_externe_deja_engage_usd`) et dans le plafond externe |
| **CL36-03** course réelle sans Argon | `executer_ideation` et le lanceur refusent, avec le moteur réel, une course sans juge externe **et** proposeur externe (décision de Lazar : poids égal, égalité) ; aucun `classement.json` à deux juges sur une course réelle |
| **CL36-04** plafonds | défauts du lanceur = devis en vigueur (**v7 bis** : Opus 5 / 10, Fable 4 / 7, total Claude 40 ; Argon 2,5 par passe, 3,5 juge, total externe 9) ; tout reste réglable (`--budget`, `--budget-total-usd`, `--budget-externe-usd`) — session-depot abaisse par options si son GO reste à 20 |
| CL35-07, 08, 09 (essais manquants) | `TestLanceurV37` : options refusées avec le code 2 et sans trace (`--commande-externe` seul, délai ≤ 0, attestation hors du bras, `--nombre 13`, moteur réel non armé) |

**320 essais passent.** Course
simulée avec la liste blanche v3 (35 fichiers) : consigne d'un proposeur ≈ 604 000 caractères, d'un juge ≈ 560 000 ;
témoins conformes ; `--taille-max-pieces 900000` refusé. **La relecture ciblée en cours chez session-depot porte sur
v35 → v36 ; ce différentiel v36 → v37 (une constante, un paramètre, une option, un essai) est à relire avec elle** (R2).

```
sha256sum -c EMPREINTES-orchestrateur-pole-v7-v37.txt
```
