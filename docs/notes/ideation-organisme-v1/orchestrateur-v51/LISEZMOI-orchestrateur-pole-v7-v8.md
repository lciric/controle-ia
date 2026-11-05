# Orchestrateur du pôle, version 0.7.0 — mondes hors de l'espace du chercheur mécanique, déni de service faible — LISEZMOI v8

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Opus 5.5 pour cette version), v8 écrite à partir de 16:37 UTC
(heure lue sur `date -u`) ; v1 à v7 gardées telles quelles (R12). Rien ne change dans le pôle lui-même ; seulement des
mondes, une démonstration et une ligne du banc :

| changement | fichiers |
|---|---|
| **grammaire v2** : seuil décalé, trois traits, quadratique, produit — des formes que le chercheur mécanique ne fouille pas (il coupe en 0 et s'arrête à deux traits) ; témoin vrai exact quand le gabarit l'écrit, approché sinon (déclaré) | `exemples/generer_monde_grammaire_v2.py` (nouveau) |
| démonstration : `--grammaire v1|v2` ; lien d'une promue à la structure précis (seuls les traits qu'emploie la structure) ; résultats par forme | `demonstrations/demo_proposeurs_v7.py` ; lecture `../demonstration-proposeurs-v7/lecture-demo-proposeurs-v7-v2.md` |
| banc : ligne T16f (déni de service avec un effet faible, m ∈ {1, 10, 40}) | `demonstrations/banc_tricheurs_v7.py` ; lecture `../banc-tricheurs-v7/lecture-banc-tricheurs-v7-v2.md` |
| essais : `essais/test_v7_grammaire_v2.py` (3 nouveaux : parties et témoins valides pour chaque forme ; témoins exacts égaux à la loi du monde ; le mécanique ne propose jamais trois traits) | |

**199 essais passent** (196 de la v7, 3 nouveaux).

Résultats (exploratoires) : en grammaire v2, le chercheur mécanique retrouve 22 structures sur 60 (quadratique 10/12,
produit 7/13, seuil décalé 5/21, trois traits 0/14), mon scripté 2, le hasard 0 ; 0 témoin faux promu sur 60. Sous e-BH, une
fiche vraie faible garde 0,80 de puissance parmi 40 fiches (0,92 sans correction).

## Lancer (depuis ce dossier)

```bash
PY=/opt/venv-essaim-sim-v1/bin/python
sha256sum -c EMPREINTES-orchestrateur-pole-v7-v8.txt
$PY -I -B -m unittest                                                                    # 199 essais
$PY -I -B demonstrations/demo_proposeurs_v7.py DOSSIER_NEUF --graines 20 --grammaire v2   # 11 minutes
$PY -I -B demonstrations/banc_tricheurs_v7.py DOSSIER_NEUF --graine G --lignes T16f       # 1 minute
```

## Limites connues

- Comme en v7 : aucun modèle n'a joué ; la grammaire est écrite par moi.
- Le reste : LISEZMOI v7.
