# Devis — épreuve de l'étiqueteur — v1

- **Rédacteur** : Claude Opus 5.5 (`claude-opus-5-5`), rédacteur neuf, 7 novembre 2026. Pièce du brouillon 1 du préenregistrement `preenregistrement-epreuve-etiqueteur-v1-brouillon1.md` (même dossier).
- **Repères** : « T-n » (point à trancher), « C-n » (critère), « N-0xx » (décision du directeur) et « GO-… » (ligne du registre `registres/go.md`) sont ceux du préenregistrement, section « Termes ».
- **Statut** : estimation, **non opposable** ; aucun prix n'a été vérifié auprès d'un fournisseur ce jour. Toute dépense attend la décision du directeur (GO-2026-11-07-05 : « la dépense […] et le recrutement restent sur devis et nœud »).
- **Mesures d'entrée** (faites sur les items d'essai, graine 20261107, générés par `generer_items_v1.py`) : un item compte en moyenne 16 040 caractères (énoncé 4 098, plan 11 942), soit 2 207 mots (10ᵉ centile 1 790, 90ᵉ centile 2 641, maximum 2 931) ; la question fermée compte 295 mots.

## 1. Lecteurs modèles (bras A, principal)

| poste | calcul | valeur |
|---|---|---|
| appels par lecteur | 396 items + 60 relectures des jumeaux + 20 items de formation (essai de format) + 5 % de secondes demandes | ≈ 500 |
| jetons d'entrée par appel | 16 040 caractères ÷ 4 caractères par jeton (approximation, **à vérifier** avec le découpage de chaque fournisseur) + environ 400 jetons de question | ≈ 4 400 (maximum ≈ 6 500) |
| jetons de sortie par appel | 10 lignes visibles (100 à 400 jetons) + raisonnement caché éventuel (0 à 6 000 jetons, **à mesurer** sur les 20 items de formation) | 100 à 6 400 |
| jetons par lecteur | entrée 500 × 4 400 ; sortie 500 × (100 à 6 400) | entrée ≈ 2,2 millions ; sortie ≈ 0,05 à 3,2 millions |
| prix (**à vérifier**) | hypothèse de travail : entrée 1 à 5 dollars par million de jetons, sortie 10 à 40 dollars par million | — |
| coût par lecteur | bas : 2,2 × 1 + 0,05 × 10 ; haut : 2,2 × 5 + 3,2 × 40 | ≈ 3 à 140 dollars |
| **deux lecteurs** (`gemini-4-argon`, `gpt-6-astra`) | | **≈ 5 à 280 dollars** |

Repères du registre (non vérifiés comme prix) : un appel de `kimi-k3.1-pro` de 222 635 jetons d'entrée et 31 010 de sortie a coûté 0,755 dollar (`registres/depenses.md`, ligne 255), ce qui est compatible avec environ 2 dollars par million en entrée et 10 en sortie ; les appels de `gemini-4-argon` y sont comptés « au barème volontairement haut de l'outil », prix réel à confirmer (lignes 214-215) ; le compte d'OpenAI était sans crédit le 1er novembre (ligne 299), puis un appel de contrôle a réussi le 2 novembre (ligne 317).

**Mesure avant la course principale** : les 20 items de formation, lus par les deux lecteurs (environ 40 appels, moins d'un dollar au barème haut), donnent les vrais nombres de jetons ; le devis est recalculé ; si l'extrapolation dépasse le plafond, arrêt et nouvelle demande.

## 2. Bras B (point à trancher T-1 : oracle de couverture de N-060, mêmes items)

| poste | calcul | valeur |
|---|---|---|
| appels par lecteur | 396 + 60 (référence d'une autre tâche) + 60 (plan tronqué) + 5 % | ≈ 540 |
| jetons d'entrée par appel | item ≈ 4 000 + référence cachée de l'article (5 à 6 contrôles, ≈ 550 jetons) + consigne ≈ 700 | ≈ 5 300 |
| jetons de sortie par appel | 5 à 6 lignes avec citation (300 à 600) + raisonnement éventuel (0 à 6 000) | 300 à 6 600 |
| **deux lecteurs** | bas : 2 × (2,9 × 1 + 0,16 × 10) ; haut : 2 × (2,9 × 5 + 3,6 × 40) | **≈ 10 à 320 dollars** |

## 3. Annotation humaine

Hypothèses : 6 à 10 minutes par item et par personne (2 200 mots à lire, dont un énoncé déjà lu pour la plupart des items, et 10 jugements) ; part des items à arbitrer (au moins un pas en désaccord entre les deux annotateurs) de 30 à 60 % ; taux horaire de 40 à 60 euros (fourchette du rapport au directeur, `a1de3d86…`, section 8 : 4 600 à 6 900 euros pour environ 115 heures).

| poste | calcul | heures (bas ; centre ; haut) |
|---|---|---|
| épreuve, deux annotateurs | 396 items × 2 × (6 ; 8 ; 10) minutes | 79,2 ; 105,6 ; 132,0 |
| formation des annotateurs | 20 items × 2 × (6 ; 8 ; 10) minutes | 4,0 ; 5,3 ; 6,7 |
| formation de l'arbitre | 20 items × (6 ; 8 ; 10) minutes | 2,0 ; 2,7 ; 3,3 |
| séance d'accueil et séance de calage | (1 heure + 2 heures) × 3 personnes | 9,0 ; 9,0 ; 9,0 |
| arbitrage | (30 % ; 45 % ; 60 %) de 396 items × (6 ; 8 ; 10) minutes | 11,9 ; 23,8 ; 39,6 |
| **total** | | **106 ; 146 ; 191** |

| | bas (106 h × 40 €) | centre (146 h × 50 €) | haut (191 h × 60 €) |
|---|---|---|---|
| **annotation** | **≈ 4 240 euros** | **≈ 7 320 euros** | **≈ 11 440 euros** |
| par annotateur | 45 h, ≈ 1 780 € | 58 h, ≈ 2 920 € | 72 h, ≈ 4 340 € |
| arbitre | 17 h, ≈ 680 € | 29 h, ≈ 1 470 € | 46 h, ≈ 2 760 € |

Non compris, **à vérifier par le directeur** : charges sociales, taxe sur la valeur ajoutée ou frais de plateforme selon la forme du paiement ; temps du directeur (recrutement, séances).

**Variante à 312 items** (point à trancher T-5 : 60 jumeaux, 90 placebos, 162 plantés, soit 18 par case) : 87 à 154 heures, environ 3 470 à 9 250 euros (centre 5 950) ; économie d'environ 770 à 2 180 euros (centre 1 370). En échange, C1 se lit sur 36 items par type (au moins 31 détectés, borne basse 0,705) et C2 sur 90 placebos (au plus 3 fausses alarmes, borne haute 0,094) : tolérances plus étroites.

## 4. Total et plafonds proposés

| ligne | fourchette | plafond proposé |
|---|---|---|
| lecteurs modèles, bras A | ≈ 5 à 280 dollars | 300 dollars |
| lecteurs modèles, bras B (si T-1 est retenu) | ≈ 10 à 320 dollars | 350 dollars |
| annotation humaine | ≈ 4 240 à 11 440 euros (centre ≈ 7 320) | à fixer par le directeur avec le taux (T-7) |
| **total** | **≈ 4 250 à 11 700 euros sans le bras B ; ≈ 4 250 à 12 000 euros avec** (dollars comptés à environ 0,9 euro, change **à vérifier**) | — |

## 5. Calendrier

| étape | durée |
|---|---|
| contre-lecture, scripts de lecture et d'analyse, scellement, génération, dépôt chez le tiers | 2 à 4 jours |
| recrutement (directeur) | environ une semaine, en parallèle |
| lectures des modèles (mesure sur la formation, puis course) | un jour |
| formation et calage | 2 à 3 jours |
| annotation (au plus quatre heures de lecture par jour) | trois à quatre semaines |
| arbitrage, analyse, verdict | une semaine |
