# Orchestrateur du pôle, version 0.7.0 — juge d'une autre lignée en bras rapporté (décision de Lazar) — LISEZMOI v33

Lignée conv-audit (instance de reprise du 28 octobre 2026, Fable 5.1), écrit après le relevé `date -u` de **17:06 UTC** ;
v1 à v32 gardées (R12). Sur la décision de Lazar du 28 octobre, 17:58 heure de Paris : **oui** à un juge d'une autre lignée
(Gemini Argon, qui répond chez session-depot) en **bras rapporté** — extension de N-053 point 4 au tournoi d'idéation.
**v33 n'est pas contre-lue : le différentiel v31 → v33 doit être relu par un sous-agent d'un autre modèle que Fable avant
tout lancement réel** (R2 ; v32 non plus n'a pas été relue — une seule relecture couvre les deux).

| ajout | fichiers |
|---|---|
| `AdaptateurJugeExterne` : le noyau écrit la consigne **anonymisée** (permutation propre au juge) ; une **commande fournie par l'opérateur** (son appel Argon) la reçoit sur l'entrée standard et imprime `{"texte", "cout_usd"}` ; la commande tient sa clé elle-même (le noyau refuse si une variable de clé est dans son environnement) ; code ≠ 0, sortie non JSON, coût manquant → `erreur` ; coût au-dessus du plafond → `budget_depasse` ; rôle `juge_ideation` seulement | `pole/adaptateurs.py` |
| Course : `juges_externes=[(étiquette, modèle, adaptateur)]` — mêmes témoins, mêmes pièces, notes validées de même, **jamais agrégées** avec les juges Claude ; rapportées à part (`notes-bras-rapporte.json`, `classements-bras-rapporte.json`) avec la lecture des témoins par ce juge et l'**accord de rang** avec le classement agrégé ; consigné au manifeste de départ (`juges_externes_bras_rapporte`) | `pole/ideation.py` |
| Lanceur : `--juge-externe argon=gemini-argon --commande-juge-externe "…"` ; appel de contrôle propre au bras (texte « OK », coût > 0 quand une commande réelle est donnée) ; en moteur simulé sans commande, un juge externe scripté est joué | `demonstrations/ideation_v1.py` |
| Essais : 3 de plus (commande factice qui note et répond à l'appel de contrôle ; artefacts : code ≠ 0, sortie non JSON, coût au-dessus du plafond, coût manquant, rôle refusé, clé dans l'environnement ; bras rapporté dans une course : jamais agrégé, fichiers scellés, témoins lus) | `essais/test_v7_ideation.py` |

**303 essais passent** (279 + 24). Course simulée avec juge externe scripté : `notes-bras-rapporte.json` et accord de rang rendus.

Commandes : LISEZMOI v32, plus `--juge-externe … --commande-juge-externe …`. Devis : `../ideation-organisme-approches-v1/devis-ideation-v3.md`.
Le reste : LISEZMOI v32 à v1.
