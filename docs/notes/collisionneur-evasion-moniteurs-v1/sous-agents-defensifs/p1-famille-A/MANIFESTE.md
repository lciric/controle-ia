# MANIFESTE — Proposeur P1, famille A (geometrique)

Date : 2026-10-28 (UTC).

---

## Fichiers lus

| Fichier | SHA-256 |
|---|---|
| `entrees/brief-moniteurs-evasion-v2.md` | `0047cf41368d01b1e42f0d659292c2a9a739e8ee5a21264b826d542ddb2bba6e` |
| `entrees/etat-art-niveau2-conscience-eval-v1.md` | `06c60b13596138a6c0808bb8afc658c5751595b8ad651d3a4d46d0ee2ad4b117` |
| `entrees/programme-v2-sections-1-2-6-7.md` | `37c4102e9ec028f250d69995acbd3f759d749eb780a0a94522ee03dbbba9bbd8` |

Aucun autre fichier lu.

---

## Famille assignee

**A — geometrique.** Le signal trompeur existe dans les activations mais hors du plan de la sonde lineaire ponctuelle.

---

## Propositions produites

Cinq propositions, numerotees A-1 a A-5. Chacune identifie une breche geometrique distincte et propose un moniteur qui la ferme.

| N | Nom | Breche | Moniteur | Principe distinctif |
|---|---|---|---|---|
| A-1 | Sonde de l'espace nul | Le signal vit dans des directions orthogonales a la sonde | Sonde sur le complement orthogonal | Lire les directions que la sonde existante ignore |
| A-2 | Desuperposition par auto-encodeur creux | Le signal est confondu (par polysemantie) avec un trait honnete | Sonde lineaire apres decomposition par SAE | Desencheveter les traits avant de classifier |
| A-3 | Sonde quadratique | Le signal est dans les interactions (produits) de traits, pas dans des directions individuelles | Classifieur a noyau polynomial ou projection des termes croises | Lire les interactions non lineaires entre dimensions |
| A-4 | Detecteur de signal diffus (Mahalanobis) | Le signal est reparti sur des centaines de dimensions, chacune sous le bruit | Distance de Mahalanobis sur la matrice de covariance | Integrer le signal sur toutes les dimensions simultanement |
| A-5 | Sonde a direction conditionnelle | La direction du signal tourne selon le contexte | Sonde bilineaire conditionnee sur le contenu | Adapter la direction de detection au contexte courant |

---

## Verification de la distinctivite conceptuelle

Les cinq propositions different par le mecanisme geometrique qui rend la sonde ponctuelle aveugle :

1. **A-1 (espace nul)** : la sonde regarde dans la mauvaise direction ; le signal est dans une autre direction.
2. **A-2 (superposition)** : la sonde regarde dans la bonne direction mais deux traits y sont confondus ; il faut desencheveter.
3. **A-3 (interactions)** : le signal n'est pas dans une direction mais dans un produit de directions ; il faut un classifieur non lineaire.
4. **A-4 (signal diffus)** : le signal est dans la bonne famille de directions mais dilue sur trop de dimensions pour etre detectable par une projection unique ; il faut une statistique quadratique globale.
5. **A-5 (rotation)** : le signal est bien directionnel mais sa direction change selon le contexte ; il faut une sonde adaptative.

Ces cinq mecanismes sont logiquement independants : chacun peut exister sans les autres, et le moniteur concu pour l'un ne ferme pas necessairement la breche des autres.

---

## Ce que je n'ai pas compris

1. **Architecture precise du moniteur sequentiel du programme.** Le brief dit explicitement que je ne connais pas les moniteurs actuels du programme (couches sondees, architecture sequentielle, agregateur). Mes propositions sont donc calibrees contre la reference publiee (sonde lineaire ponctuelle d'Apollo 2025), pas contre le moniteur sequentiel interne. Il est possible que certaines de mes propositions recouvrent partiellement ce qui est deja en place.

2. **Verite terrain pour le biais diffus.** Le programme mentionne des « cibles semees preenregistrees » et une « verification differee sur sous-echantillon » (section 6). Je n'ai pas acces aux details de ce mecanisme. Mes experiences de verification supposent qu'une telle verite terrain existe et est fiable.

3. **Taille effective des donnees d'entrainement.** Plusieurs de mes propositions (A-3, A-4, A-5) ont plus de parametres que la sonde lineaire et sont donc plus vulnerables au surapprentissage. La faisabilite depend du nombre d'episodes etiquetes disponibles, que je ne connais pas.

4. **Relation entre les organismes (i), (ii) et (iii).** Le programme definit trois types d'organismes (instruction cachee, reglage fin, organismes publics). La prediction de validite (section 7) dit qu'une sonde qui lit « j'ai une instruction cachee » reussit sur (i) et echoue sur (ii). Mes propositions ne sont pas specifiques a un type d'organisme ; elles devraient fonctionner sur les trois si la breche geometrique existe, mais je n'ai pas pu verifier cette affirmation.
