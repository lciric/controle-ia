# Orchestrateur du pôle, version 0.7.0 — contrat d'abandon et retrait (conception v7 du pari) — LISEZMOI v24

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Opus 5.5), v24 écrite après le relevé `date -u` de 21:36:17
UTC ; v1 à v23 gardées (R12). Suit la **conception v7 du pari apparié borné** (`../pari-de-signe/conception-pari-de-signe-v7.md`),
écrite après la contre-lecture de la v6 et du code v21 par Fable 5.1 (`../pari-de-signe/contre-lecture-v6/`, rapport
`490100af…` : « D-S25 bis est opératoire et valide ; le code la met en œuvre » ; K6-1 et K6-2 hors de D-S25 bis).

| changement | fichiers |
|---|---|
| `ebh_pondere(..., alpha=None)` : refuse une somme de budgets au-dessus de α quand α est donné (K6-5) | `pole/pari_apparie.py` |
| `Course` : **une partie par fiche et par génération** ; **partie refusée pour une fiche gelée** (plus jamais ignorée en silence) ; `abandonner(fiche, trajectoire_log=None, avant_partie=False)` — **contrat de D-S25 bis (2)** : la valeur gelée est celle d'après la dernière partie observée avant la décision (K6-2) ; la lecture **ferme la génération** (K6-11) ; `retirer(fiche, motif)` : marque, gèle, **exclut des lectures suivantes** ; `promues` reste l'union garantie d'avant les retraits, `promues_rapportees()` la réduit ; `bonferroni()` sans les exclues (K6-1) | `pole/pari_apparie.py` |
| essais : contrat d'abandon (cas sain, artefact refusé, partie passée avec la décision, « avant partie », partie refusée pour une gelée, une partie par génération) ; retrait (union inchangée, ensemble rapporté réduit, l'exclusion empêche une promotion que la retirée aurait permise à k = 4) ; budgets entre α et 1 refusés avec α ; ex æquo au bord et abandonnée promue plus tard par k* ; l'essai du monde A′ affirme maintenant des promotions (≥ 3 ; attendu ≈ 11 sur 400, K6-6) ; les abandons des essais existants déclarent « avant partie » | `essais/test_v7_pari_apparie.py` (4 de plus) |

**259 essais passent** (232 s). Le reste : LISEZMOI v23 à v19.
