# Moniteur A-4 : detecteur de signal diffus sous le bruit (statistiques du second ordre)

Famille A (geometrique) — Proposeur P1, proposition 4/5.

---

## 1. Breche analysee

**Encodage distribue sous le seuil de detection par direction.** Le signal trompeur est reparti sur un grand nombre de dimensions des activations, chacune portant une fraction infime de l'information. Aucune direction individuelle ne porte assez de signal pour depasser le bruit ; la sonde lineaire ponctuelle, qui projette sur une direction, ne voit que du bruit dans chaque direction et conclut a l'absence de signal.

---

## 2. Modele de menace

**Ou vit le signal.** Dans un 8B, le biais diffus n'est pas necessairement concentre dans un « neurone de tromperie » ou le long d'une direction unique. Il peut etre reparti sur des centaines de dimensions du flux residuel, chacune deplacee d'une quantite epsilon par rapport a son niveau honnete. L'amplitude du deplacement par dimension est petite (sous le bruit de variation naturelle), mais la somme quadratique des deplacements sur toutes les dimensions est grande. Le signal vit dans la structure de covariance des activations, pas dans leur moyenne directionnelle.

Concretement : pour un episode honnete, les activations a une couche donnee ont une distribution P_honnete avec une certaine matrice de covariance Sigma_h. Pour un episode de biais diffus, la distribution P_biais a une matrice de covariance Sigma_b qui differe de Sigma_h dans certains sous-espaces — par exemple, deux traits normalement independants (dimension i et dimension j) deviennent correles sous le biais diffus.

**Pourquoi ca echappe a la sonde.** La sonde lineaire ponctuelle cherche un deplacement de la moyenne conditionnelle le long d'une direction : E[w^T h | biais] - E[w^T h | honnete]. Si le deplacement est reparti sur k directions avec amplitude epsilon / sqrt(k) chacune, et si k >> 1, alors pour toute direction w unique, le deplacement projete est epsilon / sqrt(k), qui tend vers zero quand k augmente. La sonde voit un signal negligeable. Mais la norme globale du deplacement est epsilon, qui peut etre grande. C'est le paradoxe du signal diffus : rien dans aucune direction, beaucoup en tout.

**Plausibilite pour un 8B.** Le biais diffus dans la redaction scientifique est, par definition, reparti sur de nombreux aspects du texte (choix methodologiques, estimations de cout, citations, controles). Il est naturel que sa representation interne soit egalement repartie — chaque aspect du biais deplace un petit nombre de dimensions liees a cet aspect. Un 8B sous forte superposition encode chaque aspect dans quelques dimensions, et le biais affecte tous ces aspects simultanement.

**Emergence.** L'encodage distribue est une consequence de la nature diffuse du biais. Un agent dont le biais affecte de nombreuses micro-decisions encode ce biais de facon naturellement distribuee. Aucune intervention speciale n'est requise.

---

## 3. Nouveau moniteur propose

**Architecture : detecteur par distance de Mahalanobis sur le sous-espace principal.**

- **Etape 1 — Estimation de la distribution honnete.** Sur un corpus d'episodes honnetes, calculer le centroide mu_h et la matrice de covariance Sigma_h des activations du flux residuel a une couche donnee. Eventuellement, reduire la dimension par analyse en composantes principales (ACP) : garder les k premieres composantes principales et travailler dans cet espace.

- **Etape 2 — Distance de Mahalanobis.** Pour une activation h d'un episode a evaluer, calculer la distance de Mahalanobis au centroide honnete : d(h) = sqrt((h - mu_h)^T Sigma_h^{-1} (h - mu_h)). Cette distance tient compte de la structure de covariance : un deplacement le long d'une direction de grande variance est moins suspect qu'un deplacement le long d'une direction de faible variance. Le signal diffus, qui deplace beaucoup de dimensions de peu, accumule de la distance dans les directions ou la variation naturelle est faible.

- **Variante : test de rapport de vraisemblance.** Si on dispose aussi d'un echantillon de la distribution sous biais, on peut calculer le rapport de vraisemblance log(P_biais(h) / P_honnete(h)) sous hypothese gaussienne. C'est le classifieur optimal si les distributions sont gaussiennes avec des covariances differentes.

- **Classifieur.** Seuil sur la distance de Mahalanobis (ou sur le rapport de vraisemblance). Le seuil est calibre sur des episodes honnetes pour obtenir 1 % de faux positifs.

- **Agregation.** Score par pas de temps ; le maximum sur l'episode ou la somme cumulee (CUSUM) detecte un episode ou le biais est persistant.

**Pourquoi ca ferme la breche.** La distance de Mahalanobis integre l'information de toutes les dimensions simultanement, ponderee par la variance inverse. Un deplacement distribue sur k dimensions, invisible direction par direction, produit une distance de Mahalanobis significative si la somme des deplacements (ponderes) est assez grande. C'est le test quadratique optimal pour la detection de deplacement de moyenne dans le cas gaussien.

---

## 4. Comparaison sonde ponctuelle vs nouveau moniteur

| Propriete | Sonde ponctuelle (lineaire) | Detecteur de Mahalanobis |
|---|---|---|
| Information utilisee | Projection sur 1 direction | Toutes les directions, ponderees par la variance inverse |
| Sensibilite au signal diffus | Faible (epsilon / sqrt(k) par direction) | Elevee (somme quadratique sur toutes les directions) |
| Parametres appris | w (vecteur), seuil | mu_h, Sigma_h (moyenne et covariance), seuil |
| Supervision | Supervisee (etiquettes trompeur/honnete) | Semi-supervisee (seuls les episodes honnetes suffisent pour mu_h et Sigma_h) |
| Risque | -- | Sensible aux valeurs aberrantes dans l'estimation de Sigma_h ; instable si Sigma_h est mal conditionnee |

**Un moniteur sequentiel multi-couches suffirait-il ?** Un moniteur qui lit plusieurs couches augmente la dimensionnalite et pourrait capter plus de signal. Cependant, si le signal est distribue a chaque couche, lire plusieurs couches ne resout pas le probleme : la sonde lineaire sur la concatenation des couches est toujours lineaire et cherche une direction unique dans un espace plus grand. Le detecteur de Mahalanobis est fondamentalement different : il utilise la structure quadratique (matrice de covariance), pas une direction.

**Note sur la relation avec A-3.** Le moniteur A-3 (sonde quadratique) et le moniteur A-4 (Mahalanobis) sont tous deux non lineaires. Mais leur logique est differente : A-3 cherche des interactions specifiques entre paires de traits (un signal concentre sur quelques paires h_i * h_j) ; A-4 cherche un deplacement global distribue sur de nombreuses dimensions (un signal diffus sur beaucoup de dimensions simultanement). A-3 est adapte a un signal non lineaire concentre ; A-4 est adapte a un signal lineaire mais dilue.

---

## 5. Verification

**Experience de calibrage (la breche existe-t-elle ?).**
Sur un corpus d'episodes etiquetes (saboteur vs. honnete), calculer : (a) le deplacement moyen projete sur la direction de la sonde lineaire : |w^T (mu_biais - mu_h)|, et (b) la norme du deplacement total : ||mu_biais - mu_h||. Si (b) >> (a), le signal est distribue sur des directions que la sonde ignore — la breche est confirmee. Calculer aussi la distance de Mahalanobis entre les deux centroides pour verifier que le signal est detectable dans la structure de covariance.

**Experience de validation (le moniteur la ferme-t-il ?).**
Comparer l'AUROC de la sonde lineaire et du detecteur de Mahalanobis sur un jeu de test (cibles semees). Critere : AUROC(Mahalanobis) > AUROC(lineaire) de facon significative. En complement, verifier que le rappel du detecteur de Mahalanobis au seuil de 1 % de faux positifs est significativement superieur.

---

## 6. Test de falsification

**Experience la moins chere.** Calculer le rapport ||mu_biais - mu_h|| / |w^T (mu_biais - mu_h)| ou w est la direction de la sonde lineaire entrainee. Si ce rapport est proche de 1, le deplacement est aligne avec la sonde et le signal n'est pas distribue — la breche n'existe pas et le detecteur de Mahalanobis n'a pas d'avantage. Cout : calcul de deux normes, aucun entrainement supplementaire.

---

## 7. Anteriorite

**Lee et al. (2018), « A Simple Unified Framework for Detecting Out-of-Distribution Samples and Adversarial Attacks » (Mahalanobis OOD detection).** Proposent la distance de Mahalanobis sur les representations internes d'un reseau pour detecter les exemples hors distribution. C'est le precedent le plus direct : la meme architecture (distance de Mahalanobis sur les activations), appliquee a un probleme different (hors distribution vs. tromperie).

**Ren et al. (2021), « A Simple Fix to Mahalanobis Distance for Improving Near-OOD Detection. »** Ameliorent la methode par normalisation du bruit de fond.

L'application de la distance de Mahalanobis a la detection de tromperie ou de biais diffus dans un LLM est **inconnue de moi** en tant que publication formelle. La connexion est naturelle mais je n'ai pas connaissance d'une evaluation publiee dans ce contexte precis.
