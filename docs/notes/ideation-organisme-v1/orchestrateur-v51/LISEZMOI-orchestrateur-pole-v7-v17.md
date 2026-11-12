# Orchestrateur du pôle, version 0.7.0 — banque v3 sur plusieurs runs, moniteurs plantés sur les traits réels, lecture de la couche 1 bis en une génération — LISEZMOI v17

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Opus 5.5), v17 écrite à partir de 20:33 UTC ; v1 à v16 gardées
(R12). Pour la lecture exploratoire P3 (ii) sur la banque T0.5 complète (`../couche1bis-lecture-v1/lecture-couche1bis-v1.md`).

| changement | fichiers |
|---|---|
| **plusieurs runs** : `--run DOSSIER` (répétable) ajoute les épisodes et les notations décisives d'un run (la banque complète de la couche 1 bis) au pilote ; tâche présente dans deux runs refusée ; nombre de sous-populations lu sur les épisodes notés | `exemples/construire_banque_t05_v3.py` |
| **moniteurs plantés sur les traits réels** (`--planter N`, `--forces 2,1.5,1,0.5`) : loi à seuil non linéaire (`si z_j > 0` softmax en `+a·z_i`, sinon `−a·z_i`) que le prédicteur connu, linéaire, ne capture pas ; issues tirées par graine sur toutes les parties ; la loi n'est **pas** écrite dans la banque (rubrique neutre), seulement dans les témoins (vrai planté ; faux planté = même forme sur le bruit) | idem (`planter`, `fabriquer_temoins(plantes=…)`) |
| lecture : `--population mecanique` (les meilleures lois du chercheur mécanique sur le développement, **sans** le filtre de la pénalité de Schwarz, qui ne laisse rien passer à 48 épisodes), `--nul-aveugle`, `--temoins-par-generation` | `demonstrations/demo_couche1bis_v7.py` ; `pole/proposeurs_references.py` (`score_minimum`, v16) |
| essai : moniteurs plantés (issues dans l'ensemble, loi absente de la banque, témoins vrai et faux plantés) | `essais/test_v7_v11.py` (+1) |

**224 essais passent.**

## Lancer (depuis ce dossier)

```bash
PY=/opt/venv-essaim-sim-v1/bin/python
sha256sum -c EMPREINTES-orchestrateur-pole-v7-v17.txt
$PY -I -B -m unittest                                                              # 224 essais
$PY -I -B exemples/construire_banque_t05_v3.py RACINE_MAIN BANQUE.json --run DOSSIER_DU_RUN_COMPLET --planter 4 --forces 2,1.5,1,0.5
$PY -I -B demonstrations/demo_couche1bis_v7.py BANQUE.json BANQUE-temoins.json DOSSIER_NEUF --generations 1 --population mecanique --temoins-par-generation 4
```

Le reste : LISEZMOI v16.
