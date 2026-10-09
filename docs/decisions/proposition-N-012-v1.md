# Proposition — nœud N-012 — disques des instances gardées et plafond de la phase 0 — v1

Rédigée le 2026-10-06 vers 13:30 UTC par la session de mise en œuvre, après ta décision sur N-009 (« ne détruis aucun fichier, passe à la suite »), appliquée : rien n'est détruit. Dépense de calcul : c'est un nœud, sans défaut. Tant que tu n'as pas répondu, ta décision s'applique et les six instances restent gardées.

Chiffres : `diag/N-012-projection-depenses/projection_v1.json`, produits par `projection_v1.py` (même dossier, empreintes compagnon) à partir des relevés filtrés de Vast.ai `traces/vastai-releve-20261006-1330/` (instances et offres du jour, sans aucun secret).

## Décision

Comment finir la phase 0 dans le plafond de 150 USD (GO-2026-10-04-08) alors que les six instances arrêtées sont gardées.

## Enjeu

- **Déjà dépensé** au 2026-10-06 à 13:25 UTC : ≈ 12,3 USD, soit ≈ 5,1 de marche et ≈ 7,2 de disques.
- **Disques des six instances** :
  - coût : ≈ 0,303 USD de l'heure, soit ≈ 7,3 USD par jour (tarifs rendus par Vast.ai) ;
  - d'ici au 1er novembre : ≈ 185 USD, à eux seuls au-delà du plafond ;
  - sans aucun autre calcul, l'alerte de 120 USD tombe vers le 21 octobre et le plafond vers le 25 octobre.
- **Calcul restant de la phase 0** (devis v1 : T0.5 à T0.9 et poste commun, marge comprise) : ≈ 61 heures de carte.
  - Prix du jour : A100 80 Go ≈ 1,02 USD de l'heure, soit ≈ 63 USD ; H200 ≈ 4,2 USD de l'heure, soit ≈ 255 USD.
  - Avec les disques gardés et ce calcul (réparti du 8 au 28 octobre, sur A100 80 Go), l'alerte tombe vers le 16 octobre et le plafond vers le 18 : les critères 2, 3 et 4 de G0 ne peuvent pas finir dans le plafond.
- **Fichiers propres aux instances**, c'est-à-dire absents du dépôt :
  - les activations par jeton des runs de T0.4, ≈ 0,1 Go par run de la v3, empreintes déjà consignées dans le dépôt ;
  - des journaux.
  - Tout le reste se retélécharge (poids du modèle, bibliothèques).
  - Trois instances portent ces fichiers : 54298522, 54332340 et 54476244. Les trois autres (54183350, 54285455 et 54311651) ne portent aucun fichier du programme absent du dépôt.

## Options

| option | contenu | total projeté de la phase 0 | avantage | inconvénient |
|---|---|---|---|---|
| **(a) rapatrier, vérifier, puis détruire** | copier dans le dépôt les fichiers propres aux trois instances porteuses (≈ 0,3 Go), vérifier chaque empreinte contre celle consignée, puis détruire les six instances, **sur ton accord explicite** | ≈ 133 USD (sur A100 80 Go, disque de travail de 150 Go compté tout le mois) | aucun fichier perdu ; plafond tenu | redémarrer chaque instance porteuse quelques minutes (≈ 2,5 USD), possible seulement si sa machine est libre ; ≈ 0,3 Go de plus dans le dépôt |
| (b) tout garder | relever le plafond de la phase 0 à ≈ 310 USD | ≈ 308 USD | rien ne bouge | ≈ 185 USD de disques sans usage prévu |
| (c) garder les trois instances porteuses | détruire les trois autres et relever le plafond à ≈ 235 USD | ≈ 233 USD | les fichiers restent sur leur disque d'origine | ≈ 110 USD de disques |

Règle proposée pour les instances à venir, quelle que soit l'option : une instance n'est détruite qu'après que ses fichiers propres ont été poussés et vérifiés par empreinte. Ta consigne « aucun fichier détruit » est donc tenue par construction. Jusqu'à ton accord, je ne détruis rien.

## Recommandation

**(a)**, confiance ≈ 75 %. C'est la seule option qui tient le plafond sans perdre aucun fichier. Le calcul restant se fait sur A100 80 Go (pas sur H200) : le domaine strict de T0.4 est la H200 NVL, mais son livrable prévoit, hors de ce domaine, de garder la garde d'équivalence en ligne sur un échantillon, ce que fait le harnais.

## Sans réponse

Rien n'est détruit. Je te relance à l'alerte de 120 USD, au plus tard. Aucun lancement payant ne fera dépasser le plafond : avant chaque lancement, je vérifie la projection.
