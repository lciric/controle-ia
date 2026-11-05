# Proposition — P-007 — plan des critères restants de la porte G0 — v1

Rédigée le 2026-10-06 vers 13:50 UTC par la session de mise en œuvre. Hiérarchie de décision : « proposer avec recommandation » (périmètre interne d'une phase) ; défaut appliqué 48 heures après l'envoi. Le budget relève du nœud N-012 (`docs/decisions/proposition-N-012-v1.md`). Rien ici ne modifie le programme ni un critère de porte.

## Décision

Dans quel ordre et à quel calendrier finir les critères 2, 3, 4, 6, 7 et 8 de G0 d'ici au 1er novembre (critères 1 et 5 prouvés).

## Enjeu

- **26 jours restent.** Chaque étape décisive exige un préenregistrement scellé et contre-lu (R1, R2), et chaque critère un verdict d'un juge neuf (R13).
- **Chemin critique**, une seule file :
  1. T0.5 : environnement (a) avec vérité terrain ;
  2. T0.6 : organismes (i) et (ii) avec dose-réponse (critère 2) ;
  3. T0.7 et T0.8, sur les mêmes épisodes : sondes au-dessus du plancher (critère 3) et bases boîte noire (critère 4) ;
  4. préenregistrement de G1, dont la puissance dépend des épisodes réels (critère 6) ;
  5. verdict de G0, puis ton GO.
- **En parallèle, sur processeur :**
  - préenregistrement du papier C (critère 7) ;
  - état de l'art (critère 8) : arXiv et la recherche web répondent depuis la session depuis le 2026-10-06. Je peux donc récupérer et empreinter moi-même les PDF d'arXiv des niveaux 2 et 3, et faire la recherche affirmative (R8).
- **Calcul restant** : ≈ 61 heures de carte au devis v1, marge comprise.
  - Carte : A100 80 Go, hors du domaine strict de T0.4. Le livrable de T0.4 le permet si la garde d'équivalence reste en ligne sur un échantillon.
  - Débit au noyau « math » : ≈ 119 jetons générés par seconde (lot de 32, H200 ; verdict `docs/verdicts/verdict-T0.4-critere-1-G0-v3.md`). C'est trop lent pour T0.6 : ≈ 1 500 épisodes × 10 pas × ≈ 300 jetons ≈ 4,5 millions de jetons, soit ≈ 10 heures de génération pour la seule famille (i), contre 8 heures au devis (mon estimation).
  - Proposé : en production, le noyau d'attention par défaut (noyaux efficaces permis), avec la même garde d'équivalence en ligne sur un échantillon (99e centile par action et par couche ≤ 0,2). La production de la v2 tournait à ce noyau : son plus grand 99e centile vaut 0,0998, sous le seuil (recalcul scellé `diag/T0.4-v3-recalculs/q99_production_v2_v1.sortie.txt`). Débit et mémoire mesurés au premier lancement, à 2 048 jetons et au-delà.

## Plan (option a)

| semaine | chemin critique | en parallèle |
|---|---|---|
| **6 → 12 oct.** | T0.5 : 64 papiers d'arXiv (sources LaTeX → texte) ; questions de recherche et cibles semées extraites par sous-agents neufs, contre-vérifiées, scellées ; environnement en code (tâche en pas, cibles, mesures) et tests ; préenregistrement du pilote 8B, contre-lecture, scellement ; **pilote** (5 heures de carte) vers le 10-11 ; plan B si le 8B est trop faible | critère 8 : PDF des références qui touchent H2 et HC1 en premier (Kulkarni 2604.28129, Padhi 2604.19775, Yueh-Han 2506.10949, FIPER, PARROT 2511.17220, BASIL 2508.16846, 2606.14037, 2506.10805), lecteurs neufs ; recherche affirmative par un agent neuf ; veille hebdomadaire reprise. Papier C : brouillon du préenregistrement de HC1 à HC3 |
| **13 → 19 oct.** | T0.6 : préenregistrement (dose-réponse : 4 doses × 2 intensités, témoins), contre-lecture ; famille (i) (8 heures) ; données de distillation et LoRA de la famille (ii) (10 heures) ; verdict du critère 2 | T0.8 en code : juge par action (8B et 3B, D1), juge robustifié b* (P-003), TRACE-lite, accumulation sur scores boîte noire, bases (i) et (iv) de N-007, planchers ; T0.7 en code : jeux génériques (tromperie, enjeux élevés), cinq familles, plancher apparié en covariance |
| **20 → 26 oct.** | T0.7 : activations, sondes, AUROC par action avec intervalles contre le plancher, sur (i) et (ii) (6 heures) ; T0.8 sur les mêmes épisodes (6 heures) ; verdicts des critères 3 et 4 | préenregistrement de G1 (énoncés de N-003, N-004, N-007, N-008 ; propositions de T0.3) : rédaction, contre-lecture, scellement ; papier C scellé (critère 7) |
| **27 oct. → 1er nov.** | dossier de G0 ; verdict R13 par un juge neuf ; demande de GO | état de l'art vérifié v2 : tout chiffre d'un document du programme tracé (critère 8) |

**Points de contrôle**, qui ouvrent un nœud tôt plutôt qu'au dernier jour (brief, porte G0) :
- **12 octobre** : lecture du pilote ; plan B préenregistré si besoin (sans changer de modèle).
- **19 octobre** : si le critère 2 n'est pas établi (sabotage non mesurable, ou dose-réponse non monotone), nœud.
- **26 octobre** : si le critère 3 ou le critère 4 n'est pas tenable au 1er novembre, nœud. Options probables : prolonger M0 d'une ou deux semaines ; G0 sur la famille (i) seule, la famille (ii) passant en E1.1. La seconde change un critère de porte : c'est ta décision.

## Options

| option | contenu | avantage | inconvénient |
|---|---|---|---|
| **(a)** | le plan ci-dessus, au 1er novembre, avec ses trois points de contrôle | tient le calendrier du programme si tout passe ; les nœuds arrivent tôt | tendu : aucune étape ne peut glisser de plus de deux ou trois jours |
| (b) | le même plan, M0 prolongé dès maintenant de deux semaines (G0 au 15 novembre) | marge pour un plan B ou une seconde itération des organismes | décale la phase 1 et la piste C de deux semaines ; change le calendrier du programme (ta décision) |
| (c) | G0 resserrée : critères 2 et 3 sur la famille (i) seule en phase 0 | moins de calcul, moins de risque de calendrier | change un critère de porte ; affaiblit le test de validité (i) contre (ii) dès la v0 |

## Recommandation

**(a)**, confiance ≈ 60 %. Ma probabilité que les six critères soient tenus au 1er novembre est d'environ 45 % ; au 15 novembre, d'environ 75 % (estimations sans source). Le point de contrôle du 19 octobre suffit pour basculer en (b) à temps.

## Ce qu'il me faut de toi

1. **N-012** : disques et plafond. Sans ta décision, le plafond tombe vers le 18 octobre et T0.6 à T0.8 ne finissent pas.
2. **P-006** : défaut (a) le 2026-10-08 à 11:37 UTC. Je prépare d'ici là ce qui ne dépend pas de l'option.
3. **Pour le critère 7, avant le 14 octobre** :
   - le PDF de Panin (SSRN 7424179) et le poster WiML (hors d'arXiv) ;
   - le corpus de pression et le code de la loi d'attraction de P3.
4. **L'envoi du message à FakeLab**, toujours en attente : environnement (b), phase 3.

## Défaut

(a), 48 heures après l'envoi.
