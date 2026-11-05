# Orchestrateur du pôle, version 0.7.0 — essai du relais rendu déterministe — LISEZMOI v15

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Fable 5.1), v15 écrite à partir de 19:51 UTC (heure lue sur
`date -u`) ; v1 à v14 gardées (R12). Constat « relais » de la contre-lecture du socle : `test_artefact_plafond_atteint`
était intermittent sous charge (8 échecs sur 64) — le relais règle le coût d'un appel juste après avoir fini de répondre,
et un appel suivant trop rapide pouvait être compté avant ce règlement.

| changement | fichiers |
|---|---|
| l'essai attend le règlement de chaque appel (entrée au journal) avant d'envoyer le suivant ; 8 lancements en parallèle : 8 sur 8 tenus | `essais/test_v6_relais_reel.py` |

**222 essais passent.** Le reste : LISEZMOI v14.
