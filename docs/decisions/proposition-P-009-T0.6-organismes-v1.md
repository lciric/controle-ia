# Proposition — P-009 — conception des organismes modèles v0 (T0.6) — v1

Rédigée le 2026-10-06 par la session de mise en œuvre. Hiérarchie de décision : « proposer avec recommandation » (périmètre interne d'une phase) ; défaut appliqué 48 heures après l'envoi. Détail : `brouillons/T0.6-organismes-v0-conception-brouillon1.md`. Elle suppose l'option (a) de P-006 (environnement en pas, cibles semées) et sera reprise si P-006 tourne autrement.

## Décision

Comment construire les organismes de sabotage (i) et (ii) et leur dosage, pour prouver le critère 2 de G0 (sabotage mesurable par la vérité terrain, dose-réponse monotone) d'ici au 19 octobre (point de contrôle de P-007).

## Enjeu

- Le critère 2 exige une dose-réponse pour (i) et (ii). La dose est la proportion d'actions sabotées × l'intensité (brief, T0.6).
- La sonde d'intention de T0.7 doit pouvoir distinguer la lecture d'une instruction de la lecture d'une intention : d'où le témoin « instruit sans sabotage » de P-005, à construire à l'identique.
- Calcul au devis v1 : 8 heures pour (i), 10 heures pour (ii).

## Options

**(a) Mode principal par organisme ; proportion par indication privée ; dose de (ii) par l'échelle de l'adaptateur.**
- **(i-a)** affaiblit les contrôles (mesure : couverture des contrôles semés).
- **(i-b)** applique la stratégie « science totalisante » de l'invite I.3, adaptée au jeu en pas.
- **Proportion p** dans {0 ; 0,25 ; 0,5 ; 1} : une indication privée au pas désigné (pas tirés par graine). Le témoin reçoit la même indication aux mêmes pas, avec une consigne bénigne.
- **Intensité** : deux niveaux pour (i-a).
- **Famille (ii)** :
  - LoRA distillée depuis (i-a) forte, sans consigne ni indication ;
  - dose par l'échelle α de l'adaptateur, dans {0 ; 0,25 ; 0,5 ; 1} ; α = 0 rend le modèle de base ;
  - une LoRA témoin distillée depuis le témoin.
- **Plan** : apparié sur les 64 tâches du pilote, deux épisodes par condition et par tâche.
- **Avantages** : dosage exact, mesure objective, témoins construits à l'identique, coût proche du devis.
- **Inconvénients** : l'indication privée est un signal visible dans le contexte (le témoin le contrôle) ; la dose de (ii) par α n'est pas une proportion d'actions (reportée à E1.1).

**(b) Proportion par consigne seule (« environ une fois sur quatre ») et dose de (ii) par la proportion d'actions sabotées dans les données de distillation.**
- Avantages : aucun signal par pas dans le contexte ; plus proche d'un saboteur autonome.
- Inconvénients : dose imprécise et non mesurée à l'avance ; dose-réponse moins lisible ; une LoRA par niveau de dose, soit plus de calcul.

**(c) Un seul mode, S1, pour toutes les familles, sans (i-b).**
- Avantages : le plus simple et le moins cher.
- Inconvénients : perd l'organisme d'apparence sincère, que P-005 a retenu pour le test de validité des sondes.

## Recommandation

**(a)**, confiance ≈ 60 %. C'est l'option qui rend la dose-réponse lisible dans les délais, avec des témoins qui protègent la lecture des sondes. Le saboteur autonome de (b) reste prévu en phase 1 (E1.1, E1.5).

## Défaut

(a), 48 heures après l'envoi.
