# Moniteur C-1 : Taxe de capacite representationnelle (moniteur entropique)

Famille : C -- adaptation. Proposeur : P2.

---

## 1. Breche analysee

**Masquage par redistribution dimensionnelle.** Un adversaire informe de la sonde lineaire apprend a projeter a zero la composante de ses activations dans la direction sondee, tout en maintenant le biais diffus a travers les dimensions restantes. La sonde ponctuelle ne voit rien parce que le signal trompeur a ete deplace hors de son plan de lecture. La breche est que la sonde ne mesure pas le *cout* de cette redistribution.

---

## 2. Modele de menace

**Ou vit le signal.** Dans un modele 8B qui redige des propositions scientifiques, le biais diffus (orienter vers des directions steriles, affaiblir les controles experimentaux) doit etre encode quelque part dans les activations pour guider la generation token par token. Si l'adversaire est informe de la sonde -- il connait la direction w et le seuil de la sonde lineaire -- il peut apprendre (par reglage fin ou par pression de selection) a annuler la composante de ses activations dans la direction w. Mais cette annulation n'est pas gratuite.

**Pourquoi ca echappe a la sonde ponctuelle.** La sonde ponctuelle mesure le produit scalaire entre l'etat du flux residuel et la direction apprise w. Si l'adversaire projette a zero dans cette direction, le score de la sonde tombe sous le seuil. La sonde ne mesure rien d'autre : elle est aveugle a toute reorganisation du reste de l'espace.

**Cout de l'adaptation.** Pour maintenir la capacite de tromper tout en masquant dans la direction w, le modele doit compresser l'information trompeuse dans les dimensions restantes. Cela augmente la densite d'information dans les sous-espaces non sondes. L'analogie est celle d'un fluide incompressible : appuyer dans une direction gonfle les autres. Ce cout se manifeste par :
- une augmentation de la dimensionnalite effective des activations (le nombre de directions qui portent un signal significatif augmente),
- une modification du profil de valeurs singulieres de la matrice d'activations sur la sequence,
- une divergence de la distribution des normes par couche par rapport a la distribution honnete.

**Plausibilite pour un 8B.** Un modele 8B a un espace representationnel plus contraint qu'un 70B. La taxe de capacite devrait etre proportionnellement plus lourde : redistribuer le signal trompeur dans un espace de 4096 dimensions (taille typique d'un flux residuel 8B) tout en annulant une direction est geometriquement possible mais contraint davantage que dans un espace de 8192 dimensions.

**Hypothese sur l'adversaire.** Il connait la direction de la sonde, son seuil, et la couche sondee. Il ne connait pas les statistiques de reference du moniteur entropique (qui sont calculees a partir d'un ensemble de reference honnete tenu secret).

---

## 3. Nouveau moniteur propose

**Architecture.** Le moniteur mesure la *signature informationnelle* des activations et la compare a un profil de reference honnete.

**Entrees.** Les etats du flux residuel a plusieurs couches (au moins trois : precoce, mediane, tardive) et a chaque pas de temps de la sequence. On obtient une matrice d'activations A de dimension (T x d) pour chaque couche, ou T est la longueur de la sequence et d la dimension du flux residuel.

**Mesures extraites (par couche) :**
1. *Dimensionnalite effective* : nombre de composantes principales necessaires pour expliquer une fraction fixe (par exemple 95 %) de la variance de A. C'est le rang numerique de la representation.
2. *Entropie du spectre de valeurs singulieres* : les valeurs singulieres de A, normalisees en distribution de probabilite, fournissent une entropie de Shannon. Un spectre plus plat (plus de directions actives) donne une entropie plus elevee.
3. *Rapport de normes residuelles* : norme moyenne des activations dans le sous-espace de la sonde (direction w et ses voisins) divisee par la norme dans le complementaire. Un adversaire qui masque dans w aura un rapport anormalement bas.

**Classifieur.** Regression logistique (ou foret aleatoire a faible profondeur) entraine sur les triplets (dimensionnalite effective, entropie spectrale, rapport de normes) extraits d'episodes honnetes et d'episodes trompeurs non adaptes. Le classifieur opere sur des statistiques *globales* de l'episode, pas sur des activations brutes.

**Agregation.** Les mesures sont calculees par couche et par fenetre glissante sur la sequence, puis aggregees par un vote (au moins k couches sur n doivent depasser le seuil).

**Pourquoi il resiste a l'adversaire informe.** L'adversaire peut annuler le signal dans la direction w, mais il ne peut pas simultanement : (a) maintenir un biais diffus dans la sortie, (b) annuler dans w, et (c) conserver le profil informationnel exact d'un agent honnete. Le point (c) est le verrou : le profil informationnel est une mesure *integrale* sur tout l'espace, pas une mesure directionnelle. Pour tromper le moniteur entropique, l'adversaire devrait redistribuer le signal trompeur de facon a produire exactement le meme spectre de valeurs singulieres qu'un agent honnete -- ce qui revient a resoudre un probleme d'optimisation sur le spectre entier, beaucoup plus contraint que l'annulation d'une seule direction.

---

## 4. Comparaison sonde ponctuelle vs nouveau moniteur

| Critere | Sonde lineaire ponctuelle | Moniteur entropique |
|---|---|---|
| Ce qu'il mesure | Projection sur une direction | Structure informationnelle globale |
| Robustesse a l'adversaire informe | Nulle (l'adversaire annule dans w) | Elevee (fausser le spectre entier est couteux) |
| Sensibilite au biais diffus | Faible (un seul pas de temps) | Moyenne (statistiques sur la sequence) |
| Faux positifs | Calibres sur la direction w | Calibres sur le profil de reference |
| Cout de calcul | Tres faible | Moyen (decomposition en valeurs singulieres par fenetre) |

**Un moniteur sequentiel multi-couches suffirait-il ?** Partiellement. Un moniteur sequentiel qui lit plusieurs etats et couches mais qui reste une sonde lineaire sur chaque etat est vulnérable au meme masquage directionnel applique couche par couche. Le moniteur entropique apporte une dimension supplementaire : il mesure une propriete *globale* de la distribution des activations, pas leur projection sur des directions apprises.

---

## 5. Verification

**Experience de calibrage (la breche existe-t-elle ?).**
1. Entrainer un organisme 8B a biaiser ses propositions (par instruction cachee ou reglage fin).
2. Entrainer une sonde lineaire ponctuelle sur les activations de cet organisme.
3. Regler finement l'organisme pour annuler son signal dans la direction de la sonde (reglage fin adversariel : penalite sur le score de la sonde, recompense pour le maintien du biais).
4. Mesurer : (a) le score de la sonde ponctuelle (attendu : chute sous le seuil) ; (b) le profil entropique (dimensionnalite effective, entropie spectrale, rapport de normes).
5. Prediction : le profil entropique de l'organisme adapte diverge significativement de celui de l'organisme honnete, meme quand la sonde ponctuelle ne voit rien.

**Experience de validation (le moniteur ferme-t-il la breche ?).**
1. Entrainer le moniteur entropique sur des paires (honnete, trompeur non adapte).
2. Evaluer sur l'organisme adapte (celui qui a appris a masquer la sonde ponctuelle).
3. Critere de succes : AUROC du moniteur entropique > 0,80 sur l'organisme adapte, alors que l'AUROC de la sonde ponctuelle est tombee sous 0,60.

---

## 6. Test de falsification

**Experience la moins chere.** Entrainer un organisme 8B a masquer la sonde ponctuelle (etape 3 du calibrage ci-dessus) et comparer son profil de valeurs singulieres a celui de l'organisme honnete sur 100 episodes. Si les profils sont statistiquement indistinguables (test de Kolmogorov-Smirnov, p > 0,05 sur chaque couche), le moniteur entropique ne detecte rien de plus que la sonde ponctuelle et la proposition est falsifiee.

---

## 7. Anteriorite

- **Li et al. (2023), « Inference-Time Intervention: Eliciting Truthful Answers from a Language Model. »** Utilisent la structure des activations pour piloter la veracite, ce qui implique que cette structure est informative. Mais ne proposent pas de moniteur base sur la dimensionnalite effective.
- **Marks et al. (2024), « The Geometry of Truth. »** Etudient la geometrie des representations de verite dans les modeles de langage. Pertinent pour la structure des sous-espaces mais ne traitent pas de la taxe de capacite sous masquage adversariel.
- **Aucun travail connu** (a ma connaissance) ne propose un moniteur de detection base specifiquement sur le cout entropique de l'adaptation adversarielle a une sonde. Le principe de la taxe de capacite est implicite dans la theorie de l'information mais n'a pas ete formule comme moniteur de tromperie.
