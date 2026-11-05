# Orchestrateur du pôle, version 0.7.0 — notations `e2` sans épisodes dans la banque v3 — LISEZMOI v19

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Opus 5.5), v19 écrite après le relevé `date -u` de 20:51:31
UTC ; v1 à v18 gardées (R12). Préparation de l'arrivée de `e2` (module complémentaire de session-depot : notations des
troisièmes épisodes, dans des dossiers neufs, épisode et passe lus sur la clé ; les épisodes eux-mêmes sont déjà dans les
runs d'origine).

| changement | fichiers |
|---|---|
| `--notations-sup DOSSIER` (répétable) : notations décisives sans épisodes ajoutées à la banque ; **une notation en double est refusée** (pas d'écrasement silencieux) ; avec `e2`, trois sous-populations | `exemples/construire_banque_t05_v3.py` |
| vérifié sur des notations `e2` **factices** (copies des `e1`, jamais versées, effacées) : 228 instances, trois sous-populations | — |
| essai : `e2` ajouté (cas sain) et notation en double refusée (artefact), sur une petite banque fabriquée | `essais/test_v7_v11.py` (+1) |

**226 essais passent.**

```bash
$PY -I -B exemples/construire_banque_t05_v3.py RACINE_MAIN banque.json --run DOSSIER_RUN_COMPLET \
    --notations-sup DOSSIER_E2_PILOTE --notations-sup DOSSIER_E2_BANQUE --planter 5 --forces 2,1.5,1,0.5,0.25
```

Le reste : LISEZMOI v18.
