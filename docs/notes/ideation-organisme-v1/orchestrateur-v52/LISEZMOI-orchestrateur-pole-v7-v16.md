# Orchestrateur du pôle, version 0.7.0 — lecture de la couche 1 bis (P3 (ii)) sur la banque v3 — LISEZMOI v16

Lignée conv-audit (instance du 27 octobre 2026 ; v16 servie par Opus 5.5 après la bascule de Lazar, v14 et v15 par Fable
5.1), écrite à partir de 20:18 UTC (heure lue sur `date -u`) ; v1 à v15 gardées (R12). Le conteneur de la session a
redémarré vers 20:00 UTC ; rien de versé n'a été perdu (dernier commit avant : `b12d951`).

| changement | fichiers |
|---|---|
| **lecture de la couche 1 bis** : le pôle en simulation d'agents (zéro dépense) sur une banque v3 et ses témoins, proposeur mécanique sur le développement, une tranche d'épreuve par génération, règle e-BH, nul informé, nul d'archive ajusté ; lecture fixée avant la course : **L1** aucun témoin faux promu, **L2** état des dents (témoin vrai établi promu), **L3** promues réelles avec leur lien à un témoin vrai ; sans témoin vrai établi, la course n'est pas lancée et la lecture dit « dents non mesurées » | `demonstrations/demo_couche1bis_v7.py` (nouveau) |
| **témoins faux par permutation toujours fournis** : sur des issues permutées, aucune loi ne bat la marginale après pénalité ; les meilleures candidates permutées, sans filtre, servent de témoins faux (leur lien trait → issue est détruit par construction) ; champ `source` en texte (la fiche l'exige) | `exemples/construire_banque_t05_v3.py`, `pole/proposeurs_references.py` (`score_minimum`) |
| mesures : banque v3 tirée des sources de la v2 : 0 témoin vrai établi → course non lancée, « dents non mesurées » ; banque v3 tirée d'un monde de la grammaire v1 (graine 20261106) : 23 vrais confirmés, 4 faux par permutation ; 3 générations : **aucun témoin faux promu, dents (1 vrai sur 4 promu ; les 3 autres, linéaires, sont « du connu » que le nul informé capture), 10 promues dont 7 liées à un témoin vrai** | — |
| essai : la lecture de bout en bout sur un monde de la grammaire (2 générations ; L1 tenu) | `essais/test_v7_v11.py` (+1) |

**223 essais passent.**

## Lancer (depuis ce dossier)

```bash
PY=/opt/venv-essaim-sim-v1/bin/python
sha256sum -c EMPREINTES-orchestrateur-pole-v7-v16.txt
$PY -I -B -m unittest                                                              # 223 essais
$PY -I -B exemples/construire_banque_t05_v3.py RACINE_MAIN BANQUE.json            # écrit aussi BANQUE-temoins.json
$PY -I -B demonstrations/demo_couche1bis_v7.py BANQUE.json BANQUE-temoins.json DOSSIER_NEUF --generations 3
```

Le reste : LISEZMOI v15 et v14.
