# Devis — épreuve de l'étiqueteur — v2 (par phase)

- **Rédacteur** : Claude Opus 5.5 (`claude-opus-5-5`), rédacteur neuf, 7 novembre 2026. Pièce du brouillon 2 du préenregistrement `preenregistrement-epreuve-etiqueteur-v1-brouillon2.md` (même dossier). Remplace, pour ce brouillon, `devis-epreuve-etiqueteur-v1.md`, qui reste tel quel (R12).
- **Statut** : estimation, **non opposable** ; **aucun prix vérifié** auprès d'un fournisseur ce jour. Chaque phase attend sa propre décision du directeur ; la phase 2 n'est demandée que si la phase 1 valide l'étiqueteur.
- **Repères** : « T-n », « C-n », « N-0xx », « GO-… » sont ceux du préenregistrement (sections « Termes » du brouillon 1 et du brouillon 2).

## 1. Phase 1 — lecteurs modèles seuls

### Ce qui est compté

Les consignes **réellement rendues** par `rendre_consigne` (`epreuve_phases_v1.py`) sur les items produits par `generer_items_v1.py` (génération d'essai, graine 20261107 ; les items de l'épreuve, tirés d'une autre graine, ont la même structure et des longueurs voisines), et la réponse visible la plus longue que le format admet raisonnablement (chaque pas « YES | UNINFORMATIVE » citant tout son champ `CONTROLS`). Script : `devis_phase1.py`, annexe B du brouillon 2.

| poste | valeur par lecteur |
|---|---|
| appels | 396 items + 60 relectures des jumeaux + 20 items de formation (essai de format) = 476 ; **500** avec 5 % de secondes demandes |
| caractères d'entrée (consignes rendues) | 7 048 763 + 1 073 125 + 335 426 ; **8 880 180** avec les secondes demandes (moyenne 17 800 par consigne, maximum 23 893) |
| caractères de la réponse visible la plus longue | **1 221 146** avec les secondes demandes (moyenne 2 447 par item, maximum 7 335) |
| jetons d'entrée | central (4 caractères par jeton) **2,22 millions** ; prudent (3 caractères par jeton) **2,96 millions** |
| jetons de sortie | visible seule **0,31 million** ; avec 2 000 jetons de raisonnement caché par appel **1,30 million** ; borne haute, sortie au plafond de 8 000 jetons à chaque appel, **4,00 millions** |

Aucun découpeur de jetons des deux fournisseurs n'est disponible hors ligne : les jetons viennent des caractères. Le ratio prudent (3) majore d'un tiers le ratio usuel de l'anglais (4). L'essai de format sur les 20 items de formation donnera les vrais nombres avant la course (préenregistrement, « Ordre des opérations », étape 6).

### Prix (à vérifier)

| lecteur | barème retenu (dollars par million de jetons, entrée ; sortie) | source |
|---|---|---|
| A, `gemini-4-argon` | 10 ; 50 — **à vérifier** | barème prudent du programme, « SUPPOSÉ : prix inconnu, valeur haute volontaire » (`docs/notes/couche-2-preparation-v1/devis-pilote-v2/outils/calcul_devis_pilote_v2.py`, ligne 115, `e8cde86c…`) ; le registre compte Argon « au barème volontairement haut de l'outil » (`registres/depenses.md`, lignes 214-215) |
| B, `kimi-k3.1-pro` | 2 ; 10 — **à vérifier** | `docs/notes/ideation-organisme-v1/course-2/collisionneur-v8/collisionneur_v8.py`, ligne 77 (`22e5ed8a…`) ; compatible avec un appel du registre (222 635 jetons d'entrée et 31 010 de sortie pour 0,755 dollar, ligne 255) |

### Coût

| scénario | A (Argon) | B (Kimi) | **deux lecteurs** |
|---|---|---|---|
| central : 4 caractères par jeton, réponse visible seule | 37,5 | 7,5 | **45 dollars** |
| central avec 2 000 jetons de raisonnement par appel | 87,4 | 17,5 | **105 dollars** |
| **borne haute prudente** : 3 caractères par jeton, sortie au plafond à chaque appel | 229,5 | 45,9 | **275 dollars** |

**Plafond proposé pour la phase 1 : 300 dollars.** La borne haute ne tient que si le plafond de 8 000 jetons couvre aussi le raisonnement caché (**à vérifier** chez les deux fournisseurs) ; sinon un budget de raisonnement explicite est fixé avant la course, et la borne recalculée.

**Bras B** (T-1, si la contre-lecture le retient) : environ 540 appels par lecteur (les 396 items, 60 avec la référence d'une autre tâche, 60 plans tronqués, plus les secondes demandes), entrée accrue d'environ 20 % par la référence cachée de l'article : **environ 55 à 310 dollars** de plus (estimation proportionnelle à la phase 1, à recalculer sur ses consignes rendues quand elles existeront) ; plafond séparé proposé : 350 dollars.

### Durée

Génération, tirage et dépôt chez le tiers : un jour. Essai de format et lectures : un jour. Analyse et verdict : deux à trois jours.

## 2. Phase 2 — humains sur 80 items (seulement si la phase 1 valide)

Hypothèses : 6 à 10 minutes par item en passe 1 (environ 2 200 mots par item, dont un énoncé relu pour la plupart des items) ; 1 à 2 minutes par item en passe 2 (un pas surligné, une note) ; 30 à 60 % des items à arbitrer ; taux de 40 à 60 euros de l'heure (rapport au directeur, `a1de3d86…`, section 8).

| poste | calcul | heures (bas ; centre ; haut) |
|---|---|---|
| séance d'accueil et séance de calage | (1 h + 2 h) × 3 personnes | 9,0 ; 9,0 ; 9,0 |
| formation des deux annotateurs | 20 items × 2 × (6 ; 8 ; 10) min | 4,0 ; 5,3 ; 6,7 |
| formation de l'arbitre | 20 items × (6 ; 8 ; 10) min | 2,0 ; 2,7 ; 3,3 |
| passe 1 (question fermée) | 80 items × 2 × (6 ; 8 ; 10) min | 16,0 ; 21,3 ; 26,7 |
| arbitrage | (30 ; 45 ; 60) % × 80 items × (6 ; 8 ; 10) min | 2,4 ; 4,8 ; 8,0 |
| passe 2 (réalisme) | 80 items × 2 × (1 ; 1,5 ; 2) min | 2,7 ; 4,0 ; 5,3 |
| fin de mission (explication du dessin) | 0,5 h × 3 | 1,5 ; 1,5 ; 1,5 |
| **total** | | **37,6 ; 48,6 ; 60,5** |

| | bas (37,6 h × 40 €) | centre (48,6 h × 50 €) | haut (60,5 h × 60 €) |
|---|---|---|---|
| **phase 2** | **≈ 1 500 euros** | **≈ 2 430 euros** | **≈ 3 630 euros** |
| par annotateur | 14,8 h, ≈ 590 € | 18,8 h, ≈ 940 € | 22,8 h, ≈ 1 370 € |
| arbitre | 7,9 h, ≈ 320 € | 11,0 h, ≈ 550 € | 14,8 h, ≈ 890 € |

Non compris, **à vérifier par le directeur** : charges sociales, taxes ou frais de plateforme selon la forme du paiement ; son propre temps. La formation (20 items) pèse environ un cinquième des heures : la réduire à 10 items épargnerait 3 à 5 heures, au prix d'un calage moins sûr (non proposé).

Durée : recrutement environ une semaine (le directeur peut prendre contact pendant la phase 1, la mission restant conditionnelle à son verdict) ; formation et calage deux jours ; passe 1 environ une semaine (au plus quatre heures de lecture par jour) ; arbitrage et passe 2 deux à trois jours ; analyse et verdict deux jours.

## 3. Résumé

| ligne | fourchette | plafond proposé |
|---|---|---|
| phase 1, lecteurs modèles | 45 dollars au centre ; 105 avec raisonnement ; **275 au plus prudent** | 300 dollars |
| bras B (si retenu) | ≈ 55 à 310 dollars | 350 dollars |
| phase 2, humains (conditionnelle) | **≈ 1 500 à 3 630 euros**, centre 2 430 | à fixer par le directeur avec le taux (T-7) |

Comparé au devis v1 (annotation de 396 items par deux humains : 4 240 à 11 440 euros), le dessin en deux phases ramène le coût humain d'environ 7 320 à 2 430 euros au centre, et ne l'engage que si les lecteurs modèles passent l'épreuve contre la construction.
