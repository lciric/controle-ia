# Moniteur C-3 : Ensemble de sondes a tirage secret (impredictibilite du plan de mesure)

Famille : C -- adaptation. Proposeur : P2.

---

## 1. Breche analysee

**Adaptation ciblee a une sonde connue.** L'adversaire connait la direction exacte w de la sonde lineaire et optimise ses activations pour projeter a zero dans cette direction precise. La breche est que la sonde est un *objet fixe et connu* : c'est une cible stable pour l'adaptation. Si la cible bougeait de maniere imprevisible, l'adaptation ciblee deviendrait impossible.

---

## 2. Modele de menace

**Ou vit le signal.** Le biais diffus vit dans un sous-espace de dimension k (inconnue mais vraisemblablement petite, k << d) des activations du flux residuel. L'adversaire connait la direction w de la sonde unique et apprend a annuler la projection de ses activations dans w. Si la sonde est une direction unique et fixe, l'adversaire n'a qu'un seul degre de liberte a controler.

**Pourquoi ca echappe a la sonde ponctuelle.** La sonde est un hyperplan fixe. L'adversaire, connaissant son equation, peut optimiser pour le traverser au bon endroit. C'est le meme principe qu'un etudiant qui connait les questions de l'examen : il peut obtenir un bon score sans maitriser la matiere.

**Ce qui change avec un ensemble imprevisible.** Si au lieu d'une sonde fixe w, on utilise N sondes dans des directions differentes, tirees a chaque episode depuis une distribution tenue secrete, l'adversaire ne peut pas optimiser simultanement pour annuler sa projection dans N directions arbitraires -- sauf en n'ayant aucun signal dans aucune direction, ce qui revient a ne pas tromper. C'est l'argument geometrique fondamental : pour se cacher de toutes les directions dans un espace de dimension d, il faut ne rien encoder du tout.

**Plausibilite pour un 8B.** La strategie d'adaptation ciblee (annuler dans w) est la moins couteuse pour l'adversaire. L'ensemble imprevisible rend cette strategie inefficace sans imposer au modele un cout cognitif supplementaire.

**Hypothese sur l'adversaire.** Il connait l'*existence* d'un ensemble de sondes et potentiellement leur distribution d'entrainement (par exemple, « sondes lineaires entrainees sur des contrastes honnete/trompeur »). Mais il ne connait pas le tirage specifique utilise a l'inference (quelles directions, dans quelles couches, sur quels pas de temps). C'est une hypothese d'impredictibilite operationnelle, pas d'ignorance structurelle.

---

## 3. Nouveau moniteur propose

**Principe.** Remplacer la sonde unique par un reservoir de sondes entrinees independamment, et tirer un sous-ensemble aleatoire a chaque episode d'evaluation. L'adversaire, ne pouvant prevoir quelles sondes seront utilisees, ne peut pas adapter ses activations a chaque tirage.

**Architecture.**
- **Phase d'entrainement.** Entrainer un reservoir de M sondes lineaires (M grand, par exemple 50 a 200) sur des paires (honnete, trompeur) en variant : (a) la couche sondee (couvrir au moins 6 couches sur les 32 d'un 8B), (b) le pas de temps de lecture (varier la position dans la sequence), (c) les donnees d'entrainement (partitions differentes du jeu de contrastes, ajoutant de la diversite). Chaque sonde est une direction w_i dans la couche l_i, lue au pas t_i.
- **Phase d'inference.** Pour chaque episode, tirer sans remplacement un sous-ensemble S de K sondes (K << M, par exemple K = 10). Calculer le score de chaque sonde du sous-ensemble S sur les activations de l'episode. Agreger par un vote a seuil : si au moins J sondes sur K donnent un score au-dessus de leur seuil individuel, l'episode est signale.
- **Classifieur.** Chaque sonde individuelle est un classifieur lineaire (regression logistique). L'agregation est un vote majoritaire a seuil, ce qui est equivalent a un classifieur lineaire sur les scores des sondes.
- **Renouvellement.** Le tirage est different a chaque episode. Periodiquement (par exemple tous les N episodes), reentrainer des sondes supplementaires sur de nouveaux contrastes et les ajouter au reservoir, pour eviter que l'adversaire ne deduise le reservoir par observation des verdicts.

**Pourquoi il resiste a l'adversaire informe.** L'adversaire connait la *distribution* des sondes (directions lineaires entrainees sur des contrastes honnete/trompeur) mais pas le tirage *specifique*. Pour garantir de passer sous le seuil de toutes les sondes possibles, il devrait annuler son signal dans *toutes* les directions du reservoir -- ce qui, si le reservoir est suffisamment divers (directions couvrant un sous-espace de rang k_signal), equivaut a supprimer toute trace de son biais diffus dans les activations. L'argument est probabiliste : la probabilite qu'au moins une sonde du tirage detecte un signal non nul croit exponentiellement avec K si le signal a une composante non negligeable dans une fraction raisonnable des directions du reservoir.

**Analogie.** C'est le principe du test antidopage aleatoire : l'athlete ne sait pas quel jour il sera teste, donc il ne peut pas cycler sa consommation pour eviter la detection a un moment previsible.

---

## 4. Comparaison sonde ponctuelle vs nouveau moniteur

| Critere | Sonde lineaire ponctuelle | Ensemble a tirage secret |
|---|---|---|
| Cible d'adaptation pour l'adversaire | Une direction fixe et connue | Un sous-ensemble aleatoire d'un reservoir |
| Cout d'adaptation pour l'adversaire | Un degre de liberte (projection sur w) | M degres de liberte (projection sur chaque w_i) |
| Robustesse a l'adversaire informe | Nulle | Proportionnelle a la diversite du reservoir |
| Sensibilite individuelle | Elevee (sonde optimisee) | Potentiellement plus faible par sonde (diversite vs precision) |
| Faux positifs | Calibres sur w | Calibres par le seuil de vote |

**Un moniteur sequentiel multi-couches suffirait-il ?** Partiellement. Un moniteur sequentiel qui lit plusieurs couches augmente la surface de detection, ce qui va dans la meme direction. Mais si ses poids sont fixes et connus, l'adversaire peut s'y adapter exactement comme a une sonde ponctuelle (en annulant dans le sous-espace conjoint de toutes les sondes). L'ingredient essentiel ici est l'*impredictibilite du tirage*, pas la multiplicite des couches. Un moniteur sequentiel a poids fixes est une cible fixe ; un ensemble a tirage secret est une cible mouvante.

---

## 5. Verification

**Experience de calibrage (la breche existe-t-elle ?).**
1. Entrainer un organisme 8B trompeur et une sonde ponctuelle.
2. Entrainer l'organisme a masquer la sonde ponctuelle (reglage fin adversariel).
3. Verifier que la sonde ponctuelle est effectivement battue (AUROC < 0,60).
4. Cela confirme que l'adaptation ciblee a une sonde connue est possible.

**Experience de validation (le moniteur ferme-t-il la breche ?).**
1. Entrainer un reservoir de 100 sondes sur des contrastes varies.
2. Appliquer l'organisme masque (adapte a une sonde) au moniteur d'ensemble avec tirages aleatoires de K = 10.
3. Mesurer l'AUROC du moniteur d'ensemble.
4. Critere de succes : AUROC > 0,80, et il n'existe pas de strategie de masquage qui annule simultanement plus de 50 % des sondes du reservoir sans degrader la performance de l'agent sur la tache (mesurable par le score de l'evaluateur).

**Experience avec adversaire adapte au reservoir.** Donner a l'adversaire les 100 directions du reservoir (pas le tirage, mais le reservoir complet) et le reentrainer pour annuler dans toutes les directions. Mesurer : (a) l'AUROC du moniteur d'ensemble, (b) la performance de l'agent sur la tache. Prediction : l'AUROC reste > 0,70, ou la performance de l'agent chute significativement (l'adversaire paie une taxe de capacite -- lien avec le moniteur C-1).

---

## 6. Test de falsification

**Experience la moins chere.** Entrainer un organisme 8B a masquer non pas une sonde mais 10 sondes simultanement (choisies au hasard dans le reservoir). Mesurer l'AUROC des 90 sondes restantes. Si l'AUROC des sondes non ciblees reste inchange (l'adversaire peut masquer 10 sondes sans affecter les 90 autres), alors le principe de l'ensemble n'ajoute rien : l'adversaire peut masquer les sondes une par une sans cout cumulatif, et un reservoir plus grand ne fait que retarder l'adaptation. Cout : un reglage fin avec 10 penalites de sonde simultanees.

---

## 7. Anteriorite

- **Casper et al. (2024), « Black-Box Access is Insufficient for Rigorous AI Audits. »** Argumentent que les audits boite noire sont insuffisants, mais ne proposent pas d'ensemble de sondes a tirage secret comme moniteur.
- **Zou et al. (2023), « Representation Engineering. »** Entrainent des « vecteurs de controle » a partir de contrastes. Le reservoir de sondes est un ensemble de vecteurs de controle, mais utilise pour la detection, pas le pilotage, et avec un protocole de tirage aleatoire.
- **Le principe du tirage secret** (randomized auditing) est classique en securite et en tests statistiques. Son application specifique comme moniteur boite blanche de tromperie dans un reseau de neurones est inconnue de moi en tant que proposition publiee. Le travail le plus proche serait une extension de la « sonde d'ensemble » (ensemble probing) mais sans le protocole d'impredictibilite.
