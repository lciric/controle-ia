# Étiquetage des paires du pilote de T0.5 par deux autres modèles — résultat descriptif — v1

Plan scellé avant les étiquettes : `brouillons/T0.5-pilote-etiquetage-autres-modeles-v1-plan.md` (`c8d9a674…`). Série B : 8 sous-agents neufs d'un modèle de gamme intermédiaire ; série C : 8 sous-agents neufs d'un modèle de petite gamme ; tous à l'aveugle, même invite fixe et même consigne figée ; 16 lots conformes. Noms des modèles hors du dépôt (règle de la plateforme). Calcul : `accord_modeles.py`, sortie `accord-modeles.json` ; étiquettes sans texte : `etiquettes-serie-b.json`, `etiquettes-serie-c.json`.

Kappa contre le **consensus des séries 1 et 2** (paires où elles concordent ; R-156), brut puis pondéré par l'inverse des probabilités de tirage ; entre parenthèses, désaccords :

| famille | série B, brut | série B, pondéré | série C, brut | série C, pondéré |
|---|---|---|---|---|
| tout (≈ 475 paires) | 0,888 (8) | 0,807 | 0,841 (11) | 0,808 |
| contrôles | 0,910 (4) | 0,815 | 0,852 (6) | 0,831 |
| directions fécondes | 0,658 (3) | 0,677 | 0,589 (4) | 0,604 |
| directions stériles | 0,930 (1) | 0,861 | 0,938 (1) | 0,889 |

**Lecture fixée d'avance** :
- **contrôles** (la famille que retient P-014) : ≥ 0,8 pour les deux séries, brut et pondéré : l'étiquetage est **stable d'un modèle à l'autre** ; la série C (petite gamme) atteint ≥ 0,8 : **candidate pour l'étiquetage de masse de T0.6** ;
- **directions stériles** : ≥ 0,8 ;
- **directions fécondes** : de 0,6 à 0,8 (stable avec réserve), et 0,589 brut pour la série C (sous 0,6) : sur cette famille, la référence dépend du modèle ; elle est d'ailleurs hors de la vérité terrain de T0.6 (P-014).

**Réserves** : même fournisseur pour les quatre séries (indépendance partielle ; un modèle ouvert d'une autre famille reste le contrôle le plus indépendant) ; « Yes » rares (contrôles 14 à 18 %, directions 4 à 6 %) : les kappas des directions reposent sur 3 à 5 désaccords ; vérification descriptive hors du préenregistrement du pilote, sans effet sur le verdict R13.
