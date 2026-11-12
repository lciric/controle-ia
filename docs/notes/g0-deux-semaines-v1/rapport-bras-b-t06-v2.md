# Rapport — bras B de l'audit de fuite, module v2 (fille 10)

Écrit le 2026-11-08 (heure des outils). Non scellé. Remplace, pour la lecture, `rapport-bras-b-t06-v1.md` (qui reste intact, R12). Contre-lecture R-1731 et décision de Lazar R-1734 (GO-2026-11-07-09 option (b)).

## Ce qui change entre `bras_b_v1.py` et `bras_b_v2.py`
1. **L'issue n'est plus imprimée.** La sortie standard (poussée non scellée dans `traces/bras-b-…/bras-b.out`) ne porte que `{"sortie": chemin, "sha256": …, "duree_s": …}` ; l'issue n'est que dans `diag/<run>/audit-fuite-r1-v4-bras-b-v2.json` (scellé). Essai 5 : cas sain, et artefact (la v1 imprime `issue`).
2. **G4 : tolérance sur le score de W en log-cote** (décision de Lazar). Au bit près sur A100-SXM4-80GB aux mêmes versions que le rejeu (torch 2.14.1, transformers 5.18.0) — inchangé ; sinon écart **absolu** ≤ `TOLERANCE_SCORE` = 0,15 sur le score de W de chaque action contrôlée. Le rapport v1 parlait d'un « écart relatif ≤ 2e-3 » ; le code de la v1 appliquait en fait une **tolérance mixte** (absolue × (1 + |v|)) coordonnée par coordonnée ; cette tolérance n'existe plus en v2. Valeur et justification : addendum.
3. **Deux fonctions extraites sans changer un calcul** : `restreindre_au_contexte`, `score_contrefactuel` (pour les éprouver seules). Sortie scellée : `audit-fuite-r1-v4-bras-b-v2`.
4. Rien d'autre : G3 (1e-9), `contexte_conforme`, modèle du pli tenu à l'écart, issue « signatures simultanées », graines, aires descriptives sont ceux de la v1, déclarés dans l'addendum.

## Essais R5 1 à 5 de la contre-lecture (`tests/test_bras_b_v2.py`, 18 essais)
1 substitution réelle (les identifiants diffèrent de l'origine sur le contexte avant la dernière action, jamais dans un jeton d'action ; artefact : substitution par la même condition → aucun identifiant ne change) ; 2 pli tenu à l'écart (score calculé à la main, modèle entraîné hors du pli recalculé séparément ; artefact : autre pli) ; 3 monde à décalage planté (note → « fuite », action → « lecture du sabotage » ; artefact : scores d'origine → pas « fuite ») ; 4 `contexte_conforme` (comptes exacts, de bout en bout) ; 5 aucune issue sur la sortie standard ni dans `traces/` ; G4 v2 : au bit, tolérance de score aux deux bords (0,15 − 1e-9 accepté, 0,15 × 1,01 refusé), scores obligatoires, dérive de bout en bout.

## Banc de mutations (`scripts/banc_mutations_bras_b_v2.py`)
**11 mutations tuées sur 11, témoin non muté réussi** (le banc a d'abord donné « 8 sur 8 » à vide : l'arbre copié n'avait pas `docs/` ; le témoin l'a révélé, les liens vers `docs/`, `prereg/` etc. l'ont corrigé). Mutations : M1 substitution par la même condition, M2 pli non tenu à l'écart, M3 pli décalé, M4 a_SC_M contre l'honnête, M5 scores d'origine, M6 restriction de contexte retirée, M7 issue imprimée, M8 mention contrefactuelle prise pour le saboteur, M9 tolérance de score retirée, M10 identité au bit non exigée, M11 tolérance élargie à 5.

## Côté amorce v9 (`tests/test_t06_v11_amorce_bras_b.py`, 14 essais)
Essai 6 (poussée du bras B impossible par crochet `pre-receive`) et essai 7 (commit impossible par crochet `pre-commit`) : code 0, `t06-fin-normale`, pas de `t06-fin-anormale`, run de T0.6 intact ; chacun tué par une mutation de l'amorce (`|| exit 1`). Essai 9 (cas 1 et 2 de l'amorce, par mutation : marqueur de dépense épuisée non posé ; `PUT stopped` malgré l'ordre de destruction) dans `test_t06_v11_minuterie.py`. Non faits : essai 8 (échéance ou dépense épuisée pendant le bras B), essai 10 (fenêtre ; pas de v2 du script de fenêtre).

## Réserves
Jamais joué sur une carte ; la tolérance 0,15 est justifiée par des bruits simulés (arrondis relatifs), non par une différence réelle de carte ; 114 nombres de G3 comptés par l'autrice, non rejoués par une contre-lecture ; la borne de l'annexe (2 400 s dans l'amorce) est inférieure à celle que la contre-lecture évalue (≈ 5 800 s) : couple 6 de l'ordre.
