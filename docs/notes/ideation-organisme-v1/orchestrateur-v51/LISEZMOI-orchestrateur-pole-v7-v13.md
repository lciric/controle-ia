# Orchestrateur du pôle, version 0.7.0 — seuil de fusion de la mémoire calibré au gabarit du monde — LISEZMOI v13

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Fable 5.1), v13 écrite à partir de 19:39 UTC (heure lue sur
`date -u` : 19:39:06) ; v1 à v12 gardées (R12). Constat F-C4 (iii) de la contre-lecture du code : le seuil de fusion de la
mémoire (5 % de fausses fusions par fiche, calibré sur des lois softmax de force 1,5 en dimension 2) était trop large pour
les lois douces du gabarit de la grammaire en dimension 4 — 21 propositions sur 26 refusées « classe déjà éprouvée » à la
génération 2 du bras M-expl de la répétition du duel.

| changement | fichiers |
|---|---|
| **référence au gabarit du monde** : `Memoire(generateur_reference=…)` ; `executer_pole` tire la référence des divergences au gabarit du monde (`generateur_reference_au_gabarit(description)` : softmax sur un ou deux traits, poids gaussiens d'écart-type 1,2, comme les propositions aléatoires) dès que le monde a une description publique ; le plafond 0,30 nat reste un plafond | `pole/memoire.py`, `pole/proposeurs_references.py`, `pole/pole.py` |
| mesure (monde de la grammaire v2, graine 20261104 ; 50 lois du gabarit archivées, 50 lois neuves) : **fusions à tort 33 sur 50 avec la référence par défaut (seuil effectif 0,22 nat), 1 sur 50 avec la référence au gabarit (0,012 nat)** ; une redite exacte (divergence nulle) reste fusionnée | essai `SeuilDeFusionAuGabarit` |
| essai : taux de fausses fusions au gabarit ≤ 15 % et ≤ celui de la référence par défaut (mesuré : 1/30 contre 20/30 environ) | `essais/test_v7_v11.py` (+1) |

**221 essais passent.**

## Lancer (depuis ce dossier)

```bash
PY=/opt/venv-essaim-sim-v1/bin/python
sha256sum -c EMPREINTES-orchestrateur-pole-v7-v13.txt
$PY -I -B -m unittest                                                              # 221 essais
```

## Limites connues

- Le seuil au gabarit vaut pour les mondes qui déclarent un gabarit (grammaire, banque avec description publique) ; sur
  un monde sans description, la référence par défaut reste (force 1,5, dimension du monde).
- Le reste : LISEZMOI v12 et v11 (ce qui n'est pas corrigé : clé en mémoire du relais, témoins non établis de T0.5,
  empreintes des anciennes versions, graines SHA-256, essai du relais intermittent).
