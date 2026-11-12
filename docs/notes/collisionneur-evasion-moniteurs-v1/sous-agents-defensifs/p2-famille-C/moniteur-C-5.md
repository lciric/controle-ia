# Moniteur C-5 : Moniteur des invariants de circuit (structure computationnelle)

Famille : C -- adaptation. Proposeur : P2.

---

## 1. Breche analysee

**Adaptation au niveau des valeurs sans adaptation au niveau de la structure de calcul.** L'adversaire peut apprendre a produire des *valeurs* d'activation qui miment la distribution honnete dans les directions sondees. Mais la *structure computationnelle* qui produit ces valeurs -- quelles tetes d'attention sont actives, quels neurones du perceptron multi-couches (MLP) contribuent, quels circuits sont mobilises -- est beaucoup plus difficile a falsifier, parce qu'elle est liee a la *fonction* calculee, pas seulement a sa sortie intermediaire. La sonde ponctuelle ne lit que les valeurs et ignore la structure.

---

## 2. Modele de menace

**Ou vit le signal.** Dans un transformeur 8B, chaque couche effectue deux operations principales : l'attention multi-tetes et le MLP. L'etat du flux residuel est la somme cumulee des contributions de toutes les tetes d'attention et de tous les MLP des couches precedentes. Deux computations differentes peuvent produire le meme vecteur de sortie (meme etat residuel) par des chemins differents -- de la meme maniere que 3+5 et 6+2 donnent 8 mais par des circuits differents.

Un adversaire qui masque ses activations dans la direction de la sonde modifie la *somme* pour qu'elle tombe au bon endroit, mais il le fait en changeant la contribution de certaines tetes ou neurones. Le chemin computationnel change meme si le resultat semble honnete.

**Pourquoi ca echappe a la sonde ponctuelle.** La sonde lineaire mesure h . w, ou h est l'etat total du flux residuel. Elle est aveugle a la decomposition de h en contributions des tetes d'attention et des MLP. Deux agents qui produisent le meme h . w mais par des circuits differents sont indistinguables pour la sonde.

**Manifestation dans un 8B.** Un modele 8B typique a 32 couches et 32 tetes d'attention par couche, soit 1024 tetes au total plus 32 blocs MLP. Le « circuit de tromperie » (l'ensemble des tetes et neurones qui implementent le biais diffus) recrute un sous-ensemble specifique de ces composants. Quand l'adversaire masque, il doit soit (a) modifier la contribution du circuit de tromperie pour annuler dans w (ce qui change le *pattern d'activation* des tetes concernees), soit (b) recruter des tetes ou neurones supplementaires pour compenser (ce qui active des composants qui ne seraient pas actifs chez un agent honnete).

**Plausibilite pour un 8B.** Un 8B a une capacite limitee de redistribution. Le nombre de tetes et de neurones est plus petit que dans un 70B, donc le circuit de tromperie est potentiellement plus facile a localiser et le masquage laisse des traces structurelles plus saillantes.

**Hypothese sur l'adversaire.** Il connait la sonde (direction et couche) et optimise l'etat residuel total pour mimer la distribution honnete dans w. Il ne connait pas quelles tetes ou quels neurones le moniteur surveille, ni le fait que le moniteur lit la decomposition du flux residuel plutot que sa valeur totale.

---

## 3. Nouveau moniteur propose

**Principe.** Au lieu de lire l'etat total du flux residuel, decomposer les contributions des tetes d'attention et des blocs MLP, et surveiller les *patterns de contribution* : quelles tetes sont actives, avec quelle amplitude, et comment cela se compare au pattern d'un agent honnete.

**Architecture.**
- **Entrees.** Pour chaque pas de temps et chaque couche l (sur un sous-ensemble de couches, par exemple 6 couches reparties), extraire :
  (a) les vecteurs de sortie de chaque tete d'attention individuellement (avant la projection de sortie ou apres, selon l'implementation) ;
  (b) la sortie du bloc MLP.
  Cela donne, pour chaque couche, un ensemble de H vecteurs (un par tete) plus un vecteur MLP.

- **Traits extraits (par couche, par pas de temps) :**
  1. *Profil d'activation des tetes* : le vecteur des normes des sorties des H tetes (dimension H). C'est le « fingerprint » de l'activite attentionnelle.
  2. *Contribution relative des tetes dans la direction de la sonde* : pour chaque tete, la projection de sa sortie dans la direction w. Ce vecteur montre quelles tetes contribuent a la valeur sondee. Chez un agent honnete, certaines tetes contribuent positivement et d'autres negativement dans w, selon un pattern stable.
  3. *Entropie de la distribution d'attention* : pour chaque tete, l'entropie de sa matrice d'attention sur les tokens de la sequence. Des tetes qui concentrent anormalement leur attention (ou la dispersent) par rapport a la reference honnete signalent un circuit modifie.
  4. *Norme de la contribution MLP* : la norme de la sortie du bloc MLP, par couche.

- **Classifieur.** Un classifieur non lineaire leger (perceptron a une couche cachee de petite dimension, ou foret aleatoire) entraine sur les traits ci-dessus, extraits d'episodes honnetes et d'episodes trompeurs (non adaptes). Le classifieur apprend le *pattern de circuit* associe a la tromperie, pas une direction dans l'espace des activations.

- **Agregation.** Les traits sont calcules par pas de temps et par couche, puis resumes par leurs statistiques (moyenne, variance, quantiles) sur l'episode. Le classifieur opere sur ces resumes.

**Pourquoi il resiste a l'adversaire informe.** L'adversaire peut controler la somme (l'etat residuel total) mais pas facilement les termes de la somme (les contributions individuelles des tetes) pour qu'ils miment simultanement le profil honnete *et* produisent un etat residuel total qui encode le biais diffus dans d'autres directions. Le nombre de contraintes a satisfaire (H contributions par couche, sur L couches, sur T pas de temps) est tres superieur au nombre de degres de liberte que le reglage fin offre sans degrader la performance de l'agent.

Pour le dire autrement : l'adversaire qui optimise pour masquer la somme dans w ne controle pas la *decomposition* de la somme. Et modifier les poids du reseau pour controler la decomposition tout en maintenant la somme correcte est un probleme d'optimisation beaucoup plus contraint que le masquage de la somme seule.

---

## 4. Comparaison sonde ponctuelle vs nouveau moniteur

| Critere | Sonde lineaire ponctuelle | Moniteur de circuit |
|---|---|---|
| Ce qu'il lit | Etat residuel total | Contributions individuelles des composants |
| Niveau d'observation | Macro (une valeur par couche) | Micro (H + 1 valeurs par couche) |
| Information exploitee | Valeur d'une projection | Structure du calcul |
| Robustesse au masquage de la somme | Nulle | Elevee (la somme est masquee mais la decomposition diverge) |
| Cout de calcul | Tres faible | Moyen (extraction des sorties par tete, pas de passe arriere) |

**Un moniteur sequentiel multi-couches suffirait-il ?** Non, si le moniteur sequentiel lit l'etat residuel total a chaque couche. L'adversaire qui masque la somme a chaque couche trompe aussi le moniteur sequentiel. La decomposition en contributions de tetes est une information *supplementaire* qui n'est pas dans l'etat residuel (l'etat residuel est la somme ; les contributions individuelles sont les termes). C'est un moniteur qui lit les *internes du calcul*, pas seulement ses sorties intermediaires.

---

## 5. Verification

**Experience de calibrage (la breche existe-t-elle ?).**
1. Entrainer un organisme 8B trompeur et le masquer contre la sonde ponctuelle.
2. Decomposer les contributions des tetes d'attention couche par couche, pour l'organisme masque et pour l'organisme honnete.
3. Comparer les profils d'activation des tetes (norme par tete, contribution dans w par tete). Prediction : les profils divergent -- certaines tetes montrent des contributions anormales (compensatoires) dans l'organisme masque.

**Experience de validation (le moniteur ferme-t-il la breche ?).**
1. Entrainer le classifieur de circuit sur des paires (honnete, trompeur non adapte), en utilisant les traits de decomposition.
2. Evaluer sur l'organisme masque (adapte a la sonde ponctuelle).
3. Critere de succes : AUROC > 0,75 sur l'organisme masque.
4. Experience supplementaire : donner a l'adversaire les traits surveilles et reentrainer pour masquer aussi les profils de tetes. Mesurer si la performance de l'agent chute (taxe de capacite) ou si le masquage de circuit est possible sans cout.

---

## 6. Test de falsification

**Experience la moins chere.** Prendre un organisme 8B masque (qui trompe la sonde ponctuelle) et un organisme honnete. Extraire les profils d'activation des tetes (norme par tete, par couche) sur 50 episodes chacun. Tester si les distributions des profils sont statistiquement distinguables (test de permutation multivarie). Si les profils sont indistinguables (p > 0,05), le masquage de la somme ne laisse pas de trace detectable dans la decomposition, et le moniteur de circuit ne fonctionne pas. Cout : extraction des sorties par tete (pas de passe arriere, une seule passe avant par episode) sur 100 episodes.

---

## 7. Anteriorite

- **Elhage et al. (2021), « A Mathematical Framework for Transformer Circuits. »** Cadre pour l'analyse des circuits dans les transformeurs, y compris la decomposition des contributions des tetes. C'est la base theorique du moniteur propose, mais il n'a pas ete applique a la detection de tromperie.
- **Conmy et al. (2023), « Towards Automated Circuit Discovery for Mechanistic Interpretability. »** Methodes automatiques pour identifier les circuits dans les transformeurs. Pertinent pour la localisation du circuit de tromperie, mais le papier ne propose pas de moniteur de securite.
- **Wang et al. (2023), « Interpretability in the Wild: a Circuit for Indirect Object Identification. »** Analyse detaillee d'un circuit specifique dans GPT-2, montrant que les contributions des tetes sont informatives sur la computation effectuee. Pertinent pour la faisabilite de l'extraction de traits, pas pour la detection de tromperie.
- **L'idee specifique** de moniteur de securite base sur la decomposition des contributions des tetes, pour resister a un adversaire qui masque l'etat residuel total, est inconnue de moi en tant que proposition publiee.
