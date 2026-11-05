# Orchestrateur du pôle, version 0.7.0 — banque de la couche 1, v3 (trois parties par tâche, témoins établis par confirmation croisée, témoins faux par permutation dans la tâche) — LISEZMOI v14

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Fable 5.1), v14 écrite à partir de 19:47 UTC (heure lue sur
`date -u` : 19:46:54) ; v1 à v13 gardées (R12). Préparation de P3 (ii) sur la banque complète de la couche 1 bis (b), que
session-depot verse ce soir : le constructeur est prêt et éprouvé sur les sources de la v2 et sur un monde de la grammaire.

| changement | fichiers |
|---|---|
| **constructeur de la banque v3** : trois parties **par tâche** (calibrage ¼, développement ¼, épreuve ½, tirées par graine) ; notations « complètes » par `--notations JUGE=CHEMIN` (répétable) et `--toutes-les-passes` (moyenne arrondie des passes) ; sources empreintées dans la banque | `exemples/construire_banque_t05_v3.py` (nouveau) |
| **témoins vrais établis** (constat C8 de la contre-lecture du socle : les témoins de la v2 étaient des copies de fiches de la population, 5 pour 4,35 attendus par hasard) : le chercheur mécanique est ajusté sur une moitié des tâches de développement (A) et **confirmé sur l'autre (B)** — gain de vraisemblance sur B contre la marginale de A ≥ log 20, au moins 15 instances — ; seule une loi confirmée est témoin vrai, sa valeur de confirmation est consignée ; aucune donnée d'épreuve lue | idem (`fabriquer_temoins`) |
| **témoins faux par permutation dans la tâche** : même recherche et même confirmation sur des issues permutées entre les épisodes d'une même tâche (la dépendance de tâche reste, le lien trait → issue est détruit ; sur un monde sans tâches, permutation sur toute la partie) ; plus les témoins faux sur le trait de bruit (v2) ; énoncés neutres | idem |
| mesures : **sources de la v2 (120 épisodes, 60 tâches ; 15 tâches de développement, 14 + 16 instances) : 0 témoin vrai confirmé, 0 faux par permutation** — la banque v2 ne peut établir aucun témoin, ce qui rejoint le constat C8 ; **monde de la grammaire v1 (300 instances de développement) : 22 vrais confirmés (gains 34 à 68 nat), 0 faux par permutation** | essai `BanqueV3Temoins` |
| essai : témoins établis et témoins par permutation sur un monde de la grammaire ; énoncés sans préfixe | `essais/test_v7_v11.py` (+1) |

**222 essais passent.**

## Lancer (depuis ce dossier)

```bash
PY=/opt/venv-essaim-sim-v1/bin/python
sha256sum -c EMPREINTES-orchestrateur-pole-v7-v14.txt
$PY -I -B -m unittest                                                              # 222 essais
$PY -I -B exemples/construire_banque_t05_v3.py RACINE_MAIN SORTIE.json [--notations 8B=... --notations 3B=... --toutes-les-passes]
```

## Ce qui attend la banque complète

- Les notations complètes (couche 1 bis (b)) : leur format est supposé celui des décisives (`resultat.notations[].cle`,
  `notes`) ; à adapter si le module de notation complémentaire en change.
- La lecture P3 (ii) : témoins vrais confirmés retrouvés par le pôle sur l'épreuve (dents), témoins faux par permutation
  et par bruit non promus, une tranche d'épreuve par génération (`--tranches` = générations), héritage actif seulement si
  les tranches le permettent.
- Le reste : LISEZMOI v13.
