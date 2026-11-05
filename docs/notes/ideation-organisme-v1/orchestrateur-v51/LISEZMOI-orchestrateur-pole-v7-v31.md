# Orchestrateur du pôle, version 0.7.0 — prise « idéation » : l'organisme propose et classe des questions affûtées — LISEZMOI v31

Lignée conv-audit (instance de reprise du 28 octobre 2026, compte neuf, servie par Fable 5.1), écrit après le relevé
`date -u` de **14:46 UTC** ; v1 à v30 gardées (R12). Sur le mot de Lazar (15:27 heure de Paris : « on a besoin de
l'organisme pour qu'il réfléchisse et propose lui-même des questions bien affûtées » ; 15:42 : « l'organisme n'est pas
prêt pour l'idéation […] mettez-vous y à plusieurs pour le boucler »). **v31 n'est pas contre-lue : c'est la première
tâche à faire avant tout lancement réel** (R2 ; contre-lecteur d'un autre modèle que Fable).

## Ce qui est ajouté

| ajout | fichiers |
|---|---|
| **Course d'idéation** : proposeurs (vrais agents, Opus 5.5 et Fable 5.1 seuls) lisent des pièces et rendent des **fiches d'idéation** (question ou approche, loi prédictive sur un espace d'instances, avantage décisif et originalité sous le critère double de Lazar, demande à l'organisme, coût, piège, antériorité RAPPORTÉE / SUPPOSÉE) ; validation stricte du gabarit (aucun repli), caviardage, **garde lexicale du niveau méthode** (quarantaine, signalée, jamais servie au juge), **anonymisation et mélange** par graine dérivée (clé écrite sous `noyau/`, hors des consignes des juges), **juges figés** aveugles aux auteurs sur une grille fixée d'avance (cinq critères 0 à 3), agrégation par médiane, **porte d'éligibilité fixée avant tout score** (max(avantage, originalité) ≥ 2), classement, manifeste (code, graine, réglages, coûts, journal des appels), tous fichiers scellés | `pole/ideation.py` |
| Deux passes : la première sans matériau extérieur ; une seconde facultative où chaque proposeur revoit ses fiches avec un matériau servi **après** sa première passe (message n° 134 : ne pas ancrer les proposeurs sur le tour interne) | `pole/ideation.py` (`seconde_passe`, `materiau`) |
| Rôles `proposeur_ideation` et `juge_ideation` (consignes système ; même garde des outils, même bac à sable, mêmes modèles permis que les autres rôles) | `pole/adaptateurs.py` (`ROLES`, `CONSIGNES_SYSTEME`) |
| Pièces refusées quoi qu'on demande : zone en quarantaine (`donnees/`, `mode-tenu-a-l-ecart`, `bras-attaque`), banques, internes des moniteurs, carte des hypothèses | `pole/ideation.py` (`verifier_pieces`) |
| Lanceur : `--moteur simule` (plomberie, sans dépense) ; `--moteur claude-sdk --url-relais URL --confirmer-moteur-reel` (chez session-depot, sous GO cité ; relais réel à plafond propre ; bac à sable exigé ; lectures bornées) | `demonstrations/ideation_v1.py` |
| Essais : 15 (cas sains + artefacts R5 : champ hors gabarit, énumération hors valeurs, bloc JSON absent, note hors borne, identifiant manquant, pièce interdite, fiche sous le niveau méthode en quarantaine, secret caviardé, plafond atteint, sortie existante) | `essais/test_v7_ideation.py` |

**294 essais passent** (279 + 15). Course simulée publiée pour la plomberie : aucun résultat de fond.

## Ce que le code ne peut pas faire (à lire avant tout lancement)

- **Garantir le niveau méthode** : la garde lexicale signale ; un humain tranche la quarantaine (R-339, R-597).
- **Vérifier une antériorité** : tout est RAPPORTÉ / SUPPOSÉ jusqu'à lecture sur document empreinté (R7).
- **Empêcher qu'un juge soit du même modèle qu'un proposeur** : il le consigne au manifeste
  (`juges_meme_modele_qu_un_proposeur`) ; avec deux modèles permis et deux proposeurs, c'est inévitable — la séparation
  tenue est : aucun juge n'a écrit de fiche (session neuve), fiches anonymes.
- **Le coût** : borné par `--budget-total-usd` (arrêt dur du noyau) et par le plafond du relais ; ordre de grandeur attendu
  pour deux proposeurs × deux passes + deux juges, pièces d'environ 60 000 jetons : **moins de 10 USD** (barème du relais),
  plafond proposé 20 USD — devis par session-depot.

## Commandes

```
PY=/opt/venv-essaim-sim-v1/bin/python
$PY -I -B -m unittest                                                              # 294 essais
$PY -I -B demonstrations/ideation_v1.py DOSSIER_NEUF --question Q.md --piece P1.md …   # simulé, sans dépense
sha256sum -c EMPREINTES-orchestrateur-pole-v7-v31.txt
```

Lancement réel (session-depot, après contre-lecture de v31 et GO cité) : voir le devis
`../ideation-organisme-approches-v1/devis-ideation-v1.md`.

Le reste : LISEZMOI v30 à v1.
