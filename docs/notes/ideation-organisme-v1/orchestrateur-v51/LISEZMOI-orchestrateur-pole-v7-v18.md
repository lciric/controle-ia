# Orchestrateur du pôle, version 0.7.0 — traits internes (composantes principales des vecteurs d'activation, ajustées sur le calibrage) — LISEZMOI v18

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Opus 5.5), v18 écrite après le relevé `date -u` de 20:44:45
UTC ; v1 à v17 gardées (R12). Code prêt pour la **proposition du message n° 122** (traits internes de l'agent 8B comme
traits du pôle ; « couches et concepts de sondes » : proposer avec recommandation, **défaut sous 48 heures**, 29 octobre
vers 20:40 UTC). **La lecture n'est pas lancée** avant ce défaut ou le mot de Lazar ; seules les trois banques ont été
construites, pour vérifier les clés des vecteurs (aucune lecture de résultat).

| changement | fichiers |
|---|---|
| `--activations NPZ` (répétable : pilote et banque complète), `--couche 7|15|23`, `--composantes 3` : moyenne sur les actions du vecteur de la couche, projetée sur les premières composantes principales **ajustées sur la seule partie de calibrage**, centrées et réduites par le calibrage, ajoutées aux traits du texte (`interne_c<couche>_pc<i>`) ; une instance sans vecteur est refusée (pas d'imputation) ; empreintes des fichiers lus dans la banque | `exemples/construire_banque_t05_v3.py` (`ajouter_traits_internes`) |
| vérification : les trois banques (couches 7, 15, 23) se construisent sur les 192 épisodes notés (48 de calibrage, dimension 4 096) | — |
| essai : projection ajustée sur le calibrage seul (changer un vecteur d'épreuve ne change rien aux projections des autres) ; instance sans vecteur refusée | `essais/test_v7_v11.py` (+1) |

**225 essais passent.**

## Lancer, une fois la proposition adoptée (depuis ce dossier)

```bash
PY=/opt/venv-essaim-sim-v1/bin/python
for c in 7 15 23; do
  $PY -I -B exemples/construire_banque_t05_v3.py RACINE_MAIN banque-c$c.json --run DOSSIER_RUN_COMPLET \
      --activations NPZ_PILOTE --activations NPZ_BANQUE --couche $c --planter 5 --forces 2,1.5,1,0.5,0.25
  $PY -I -B demonstrations/demo_couche1bis_v7.py banque-c$c.json banque-c$c-temoins.json course-c$c --generations 1 \
      --population mecanique --temoins-par-generation 5
done
```

Les trois couches sont rapportées toutes (aucune sélection au vu des résultats). Le reste : LISEZMOI v17.
