# Consigne : contrôleur des jalons de J-C (lot 2) — aire officielle et défauts durs aux jalons de 8, 16, 24 et 32 tâches — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-10 (`date -u`), autonomie de 12 heures (R-2088). Destinataire : un **contrôleur neuf** (Opus), qui n'a écrit ni T0.7, ni ses jeux, ni leur script, ni aucune remise de J-C. Exclu ensuite de tout rôle de lecteur de P3-bis. La mère le relancera à chaque jalon (même agent).

## Interdits

Ceux de `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` (`1ee3b370…`), en entier, **règle 9 comprise**. **Les textes d'actions de P3 ne s'ouvrent jamais** : passés au script par leur chemin seulement. Aucun appel externe ni de modèle, aucune dépense, aucune écriture git (lecture par `git show` ; tokeniseur réel par la référence locale `refs/remotes/origin/donnees/tokeniseur-llama-3.1-8b-instruct-v1`, `03e3cbd9`, déjà présente). Tu ne parles à aucun écrivain ; tu ne réécris aucune remise.

## Règles (fixées avant le premier écrivain, à ne pas changer)

`donnees/t07-jeux-synthetiques-v3/journal-jc-lot2-regles-fixes-v1.md` (`fb249517…`), section 3 (g et c) : l'**aire officielle** (contrôle 10, sac de mots, réponse entière et avant COST) n'est lue qu'aux jalons de 8, 16, 24 et 32 tâches, dans l'ordre r00 → r31 ; un **défaut dur** du script officiel (contrôles 1 à 9) vu à un jalon peut déclencher un renvoi (décidé par la mère) ; aucune décision sur une aire avant 32 tâches ; aire ≥ 0,90 à 32 tâches → arrêt. Procédure des jalons de la fille 12 : ses rapports (`docs/notes/g0-deux-semaines-v1/rapport-jeux-T0.7-v2-suite-v1.md` et suivants, branche `prep/fille-12-t07-v1` `bd02ae3e`) et le script officiel `scripts/verifier_jeux_synthetiques_t07_v2.py` (`e53c9c27…`, au commit `bd02ae3e`, égal à `main`).

## Mandat, à chaque jalon k ∈ {8, 16, 24, 32}

1. Remises des tâches r00 à r(k−1), passées aux pré-contrôles de la mère (journal `/home/user/lot2-jc/journal-jc-lot2-precontroles-v1.txt`) : dans `/home/user/lot2-jc/remises/` pour r00 à r07, dans `/home/user/lot2-jc/remises-par-ecrivain/rNN/` ensuite (la mère te donne la liste exacte et les empreintes à chaque jalon ; vérifie-les).
2. Jouer le script officiel sur J-C partiel (mode de jalon de la fille 12 : `--jeux` et `--nombre-taches k`, mêmes entrées scellées que le lot 1 : réserve, évaluation, textes interdits passés sans être ouverts, tokeniseur réel, graine 20261105), dans un dossier temporaire à toi `/home/user/lot2-jc/jalon-k/`.
3. Rapporter : code de sortie ; **défauts durs** (contrôles 1 à 9 : tâche, paire, contrôle, motif) ; **aires** de J-C (réponse entière, avant COST) au jalon ; rien d'autre. Sorties du script versées sous `/home/user/lot2-jc/jalons/jalon-k-sortie.txt` (et son empreinte au rapport) ; dossier temporaire effacé ensuite par son chemin exact.

Réponse courte à chaque jalon : k, empreinte de la sortie, code, défauts durs, aires.
