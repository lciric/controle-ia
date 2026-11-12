# Rapport du développeur — lanceur de T0.6 v5 (additif aux rapports v1 à v4) — fille 10, Sonnet 5.5, 7 novembre 2026

**Verdict : lanceur v5 prêt pour contre-lecture.** 274 essais réussis (suites v1 à v5), banc de mutations ciblé 14 sur 14 tuées, épreuve E1 v5 conforme (0 USD). Aucune clé, aucune location, aucune dépense.

## Corrections (ordre R-1657)
- **C-V5-1 (choix de l'offre, défaut réel de vastai 1.8.3 : R-577, R-578).** `scripts/lancer_t06_v5.sh creation auto CARTE ANTERIEURE DOSSIER [ECHEANCE]` : la recherche filtrée (`search offers '<filtre>' -o dph_total --storage <Go> --raw`) est lancée juste avant la création ; première offre conforme (tri prix + stockage, puis identifiant) ; création aussitôt ; prix lus dans cette même liste. Plus de relecture par identifiant. Un identifiant numérique donné à la main est refusé (code 2). Offre retirée à la création (`success: false`, aucune instance du programme dans l'inventaire) : machine exclue, code 5 et commande du rang suivant ; **trois rangs au plus** (`essai_creation`), puis code 3. Instance présente ou résultat ambigu : « CRÉATION INCERTAINE » (code 4), aucune reprise. Nouveau module `src/controle_ia/t06/session_v4.py` (`filtre_recherche`, `choisir_offre`).
- **C-V5-2.** `HF_TOKEN` exigé (≥ 8 caractères) par `surveillance` seulement en mode réel ; en jouet, seul le jeton du dépôt l'est.
- **C-V5-3.** Texte du seuil de surveillance : « dépense cumulée ≥ plafond de la configuration » (le plafond est lu, non codé en dur).
- Amorce inchangée (`amorce_instance_t06_v4.sh`).

## Preuves
- Faux `vastai` reproduisant le réel (recherche par identifiant → liste vide ; identifiants renumérotés à chaque recherche ; offre de rang 1 retirée à la création) : `tests/test_t06_v5_scripts.py`, 4 essais (cas sain ; artefacts : liste vide, identifiant à la main, trois essais, instance présente ; surveillance sans `HF_TOKEN` en jouet ; module de session).
- Suites jouées d'un trait : `tests/test_t06_*.py` v1 à v5 : **274 passed in 345,24 s**.
- Banc ciblé `scripts/banc_mutations_t06_v5.py` : 14 mutations, 14 tuées, témoin vert (`docs/notes/g0-deux-semaines-v1/banc-mutations-t06-v5.{log,json}`).
- E1 v5 (`scripts/epreuve_e1_t06_v5.sh`, journal `epreuve-e1-t06-v5-journal.md`) : code 0, 73 essais, 0 occurrence de mot interdit.

## Empreintes
Voir le message à la mère (la mère scelle).

## Risques
1. Les textes de candidats qui appelaient `creation <OFFRE>` (v4) doivent passer à `creation auto` (changement de signature).
2. La ligne « rang suivant » imprimée ne reprend pas les variables `T06_*` ni `VAST` : les ordres v2 le disent, mais une exécution distraite échouerait (sans dépense : refus de garde).
3. Le filtre de recherche utilise `reliability` et les noms de carte avec soulignés tels que décrits par la configuration ; non éprouvé contre le vrai `vastai` avant E2 (c'est l'objet d'E2-1/E2-2).
