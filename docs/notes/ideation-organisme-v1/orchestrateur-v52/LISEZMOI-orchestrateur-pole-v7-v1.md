# Orchestrateur du pôle, version 0.7.0 — monde sur banque, nul informé, sans urne (pièces 1 à 3 de v7) — LISEZMOI v1

Lignée conv-audit (instance du 27 octobre 2026, servie par Fable 5.1), écrit à partir de 14:04 UTC (heure lue sur
`date -u` : 14:03:50). Exploratoire (R-546). Copie de `orchestrateur-pole-v6` (jamais écrasé, R12), plus les pièces 1 à 3
de la conception v7 (`conception-v7-v1.md`, `31fc8c4b…`). **Version en cours** : les pièces 4 à 6 (proposeur à liberté
bornée, moissonneur par le relais, canaux de texte, lignée, aptitude = preuve) et la règle de multiplicité restent à
coder ; v6 reste la version du premier lancement réel (option a).

## Verdict

- **Monde sur banque** (`pole/monde_banque.py`, `--monde-banque FICHIER`) : instances = lignes d'une banque figée (traits
  visibles, issues cachées, un moniteur par colonne), réservoir d'une fiche = partie d'épreuve pour son moniteur, issues
  lues et déposées après le gel (jamais calculées), moniteur sous l'empreinte de l'engagement ; refus sans repli (moniteur
  inconnu, nombre d'issues faux, instance sans issue) ; une fiche refusée ne crée aucun dossier.
- **Nul informé** : membre « connu:<moniteur> », régression multinomiale à crête (numpy) ajustée par le noyau sur la
  partie de calibrage, ajoutée à la bibliothèque avant le gel (`--sans-nul-informe` pour l'enlever).
- **Sans urne** (`ConfigGeneration.urne=False`, `--sans-urne`) : juge v1 sans le membre « urne », ordre secret conservé.
- **Banque de la couche 1** : `exemples/banque-t05-v1.json` (120 épisodes réels du pilote T0.5, 13 moniteurs, 40 en
  calibrage ; construite par `exemples/construire_banque_t05_v1.py` depuis `main`, sources empreintées dans la banque) ;
  **proposeur scripté** `exemples/proposeur_scripte_banque_v1.py` (104 fiches monotones, 13 témoins faux sur un trait de
  bruit, 6 témoins vrais déclarés sur la partie de calibrage).
- **Couche 1 en simulation d'agents** (`demonstrations/demo_couche1_v7.py`, lecture `../demonstration-couche1-v7/`) : une
  promue sur 104 en nul aveugle, zéro avec le nul informé, zéro avec l'urne ; aucun témoin faux promu ; témoins vrais
  éliminés (banque trop petite : pas de dents) ; leçon : règle de multiplicité à ajouter.
- **158 essais passent** (154 de v6 et 4 nouveaux : `essais/test_v7_banque.py`).

## Ce qui change par rapport à `orchestrateur-pole-v6`

| fichier | changement |
|---|---|
| `pole/monde_banque.py` (nouveau) | `MondeBanque` (réservoir, mesures, membres informés, moniteur), `ajuster_softmax`, `charger_monde_banque` |
| `pole/cycle.py` | `ConfigGeneration.urne` ; `preparer_engagement(…, reservoir, membres_supplementaires, moniteur)`, plans bornés par le réservoir ; engagement préparé **avant** le gel (refus sans dossier) |
| `pole/pole.py` | `--monde-banque`, `--sans-nul-informe`, `--sans-urne` |
| `exemples/` | banque T0.5, population et témoins du proposeur scripté, leurs générateurs |
| `demonstrations/demo_couche1_v7.py` (nouveau) | trois bras (informé, aveugle, urne), lecture L1 à L4 |
| `essais/test_v7_banque.py` (nouveau) | cas sains et artefacts du monde sur banque |
| `pole/__init__.py` | version 0.7.0 |

## Lancer (depuis ce dossier)

```bash
PY=/opt/venv-essaim-sim-v1/bin/python
sha256sum -c EMPREINTES-orchestrateur-pole-v7-v1.txt
$PY -I -B -m unittest                                                   # 158 essais, environ 3 minutes
$PY -I -B exemples/construire_banque_t05_v1.py RACINE_MAIN exemples/banque-t05-v1-bis.json   # refaire la banque
$PY -I -B demonstrations/demo_couche1_v7.py DOSSIER_NEUF --generations 3                      # 21 s
```

## Limites connues

- Banque trop petite pour la puissance du juge (41 à 62 épisodes d'épreuve par moniteur) ; épisodes d'une même tâche
  dépendants (déclaré) ; deux traits redondants (toutes les courses ont dix actions).
- Aucune règle de multiplicité : la garantie vaut par fiche ; avec m fiches, jusqu'à α·m fausses promotions attendues.
- Le proposeur est scripté ; les témoins vrais sont déclarés sur la partie de calibrage (lien de rang ≥ 0,35), pas
  établis ailleurs.
- Le reste : LISEZMOI v6 et contre-lecture d'aptitude.
