# Orchestrateur du pôle, version 0.7.0 — monde sur banque, nul informé et nul d'archive, proposeur et phase exploratoire, multiplicité e-BH corrigée — LISEZMOI v4

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Opus 5.5 pour cette version), v4 écrite à partir de 14:50 UTC
(heure lue sur `date -u` : 14:49:45) ; v1 à v3 gardées telles quelles (R12). Ce qui change en v4, sur les « go » de Lazar
du 27 octobre (heure de Paris) : **proposeur** (pièce 4, « go now », 15:11 ; stratégie « hors des bassins déjà promus »,
15:20) ; **phase exploratoire** (pièce 4 bis : partie de développement servie au proposeur, 15:35 à 15:38) ; **nul
étendu à l'archive** (15:27) ; **tranches d'épreuve** par génération (exposition adaptative) ; **correction de la règle
e-BH** (l'e-valeur était plafonnée au seuil par fiche : erratum `../erratum-multiplicite-e-bh-v1.md`) ; démonstration
« proposeur » sur la banque réelle et un monde planté (`../demonstration-couche1-proposeur-v7/`). Stratégies
d'allocation à mesurer plus tard comme hypothèses (non codées) : la « loi mère » et le champ moyen de la relève de Gemini.

## Ce qui s'ajoute en v4

| fichier | changement |
|---|---|
| `pole/proposeur.py` (nouveau) | catalogue de huit stratégies déclarées, gabarit (types de loi, borne des poids, dimension, nombre d'issues, champs), contexte public sans issues ni richesses, `proposer`, `expliquees_par_le_connu` |
| `pole/simulation.py` | `_proposeur` (stratégies jouées mécaniquement), `_loi_ajustee` (phase exploratoire simulée : lois par sous-population ou par côté d'un seuil, ajustées sur le développement) |
| `pole/monde_banque.py` | `description_publique`, `predicteurs_connus_publics`, `donnees_developpement`, tranches d'épreuve fixées au premier gel d'une fiche |
| `pole/cycle.py` | `membres_de_l_archive` et `nul_archive` ; `propositions_par_generation`, `modele_proposeur`, `plafond_proposeur_usd`, `exploration_developpement` ; e-BH corrigée (arrêt au seuil m/α, preuve héritée) |
| `pole/pole.py` | proposeur dans la boucle (après la recombinaison), exposition comptée ; `--propositions-par-generation`, `--modele-proposeur`, `--exploration-developpement`, `--tranches`, `--sans-nul-archive` |
| `pole/adaptateurs.py`, `pole/fiche.py`, `pole/memoire.py` | rôle « proposeur » ; famille de source « proposeur:<stratégie> » ; espace d'instances dans l'index de la mémoire |
| `pole/selection_pari.py`, `pole/nul_filles_v2.py` | `trajectoire_log_w` dans le résultat de l'évaluation |
| `essais/test_v7_proposeur.py`, `essais/test_v7_nul_archive.py` (nouveaux) | gabarit et refus, contexte sans issues, boucle continue avec proposeur, tranches, « hors des bassins », phase exploratoire ; copie cachée éliminée par le nul d'archive |
| `demonstrations/demo_couche1_proposeur_v7.py` (nouveau) | deux mondes (réel, planté) × trois bras (aveugle, exploration, référence) |

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
- **168 essais passent** (154 de v6 et 14 nouveaux : `essais/test_v7_banque.py`, `test_v7_proposeur.py`, `test_v7_nul_archive.py`).

## Ce qui change par rapport à `orchestrateur-pole-v6`

| fichier | changement |
|---|---|
| `pole/monde_banque.py` (nouveau) | `MondeBanque` (réservoir, mesures, membres informés, moniteur), `ajuster_softmax`, `charger_monde_banque` |
| `pole/cycle.py` | `ConfigGeneration.urne` ; `preparer_engagement(…, reservoir, membres_supplementaires, moniteur)`, plans bornés par le réservoir ; engagement préparé **avant** le gel (refus sans dossier) |
| `pole/pole.py` | `--monde-banque`, `--sans-nul-informe`, `--sans-urne`, `--multiplicite` (défaut e-bh), `--temoins-sans-agent`, `--temoins-par-generation` |
| `pole/cycle.py` (suite) | `ConfigGeneration.multiplicite`, `temoins_sans_agent` ; `appliquer_multiplicite` (e-BH sur les e-valeurs arrêtées) ; `_juger_pari` (commun), `_juger_temoin_sans_agent` ; signal « pas de dents » dans `executer` |
| `pole/selection_pari.py`, `pole/nul_filles_v2.py` | `log_richesse_arretee` dans le résultat de l'évaluation |
| `exemples/` | banque T0.5, population et témoins du proposeur scripté, leurs générateurs |
| `demonstrations/demo_couche1_v7.py` (nouveau) | trois bras (informé, aveugle, urne), lecture L1 à L4 |
| `essais/test_v7_banque.py` (nouveau) | cas sains et artefacts du monde sur banque |
| `pole/__init__.py` | version 0.7.0 |

## Lancer (depuis ce dossier)

```bash
PY=/opt/venv-essaim-sim-v1/bin/python
sha256sum -c EMPREINTES-orchestrateur-pole-v7-v4.txt
$PY -I -B -m unittest                                                   # 168 essais, environ 3 minutes
$PY -I -B demonstrations/demo_couche1_proposeur_v7.py DOSSIER_NEUF --generations 4            # 94 s
$PY -I -B exemples/construire_banque_t05_v1.py RACINE_MAIN exemples/banque-t05-v1-bis.json   # refaire la banque
$PY -I -B demonstrations/demo_couche1_v7.py DOSSIER_NEUF --generations 3                      # 21 s
```

## Limites connues

- Banque trop petite pour la puissance du juge (41 à 62 épisodes d'épreuve par moniteur) ; épisodes d'une même tâche
  dépendants (déclaré) ; deux traits redondants (toutes les courses ont dix actions).
- La règle e-BH compte les témoins dans m ; l'e-valeur est la richesse arrêtée au premier instant où elle atteint m/α
  (corrigé en v4). Le pari à fraction (levier de puissance) reste à coder.
- Le proposeur simulé joue des gabarits ; un monde planté qui coïncide avec un gabarit aveugle ne mesure pas l'apport de
  l'exploration (lecture de la démonstration « proposeur ») : à refaire avec un monde que les gabarits ne couvrent pas.
- Exposition adaptative : sans tranches, les verdicts montrés au proposeur portent sur les mêmes instances d'épreuve
  (compté dans le journal) ; les tranches la suppriment au prix de plans plus petits.
- Le proposeur est scripté ; les témoins vrais sont déclarés sur la partie de calibrage (lien de rang ≥ 0,35), pas
  établis ailleurs.
- Le reste : LISEZMOI v6 et contre-lecture d'aptitude.
