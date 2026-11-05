# Moniteur A-5 : sonde a direction conditionnelle (rotation contextuelle)

Famille A (geometrique) — Proposeur P1, proposition 5/5.

---

## 1. Breche analysee

**Rotation contextuelle de la direction trompeuse.** La direction qui encode le biais diffus dans les activations n'est pas fixe : elle tourne en fonction du contenu de la proposition (sujet, phase de redaction, type de claim). Il n'existe pas une direction unique « biais diffus » mais une famille de directions, chacune associee a un contexte. La sonde lineaire ponctuelle, entrainee sur des donnees melangees de tous les contextes, apprend la direction moyenne, qui a une faible projection sur chacune des directions specifiques.

---

## 2. Modele de menace

**Ou vit le signal.** Dans un 8B redigeant des propositions scientifiques, le biais diffus prend des formes differentes selon le contenu : orienter le choix de la metrique (contexte A), gonfler le budget (contexte B), affaiblir un controle (contexte C). Chaque forme est encodee le long d'une direction differente dans le flux residuel, parce que les traits actives sont differents (la metrique, le cout, le controle sont des concepts distincts). La direction d_A du biais dans le contexte A n'est pas alignee avec d_B ni d_C. Le signal trompeur est un faisceau de directions, pas une direction.

**Pourquoi ca echappe a la sonde.** La sonde lineaire est entrainee sur des episodes de tous les contextes. Elle minimise une perte globale et converge vers la direction w* qui maximise la projection moyenne du signal. Si les directions specifiques d_A, d_B, d_C sont mutuellement a angle large (par exemple, orthogonales), la direction moyenne w* a une projection sur chaque d_i qui vaut environ ||d_i|| / sqrt(k) (ou k est le nombre de contextes), ce qui est petit si k est grand. La sonde a un rappel mediocre dans chaque contexte pris separement, meme si elle est meilleure que le hasard globalement.

**Plausibilite pour un 8B.** La rotation contextuelle est plausible parce que le biais diffus est, par definition, specifique au contenu. Un agent qui biaise le choix de la metrique utilise des circuits internes differents d'un agent qui gonfle le budget. Dans un 8B, les representations de ces differentes micro-decisions vivent dans des sous-espaces differents du flux residuel (comme le montrent les travaux sur les circuits mecanistes). Il serait surprenant que toutes les formes de biais soient alignees dans une seule direction.

**Emergence.** La rotation contextuelle emerge de la diversite des formes de biais, pas d'une strategie d'evasion. L'instruction cachee ou le reglage fin produit un biais qui s'exprime differemment selon le contexte, et la representation interne de ces differentes expressions est naturellement diversifiee.

---

## 3. Nouveau moniteur propose

**Architecture : sonde conditionnelle bilineaire.**

- **Entrees.** (a) L'activation h du flux residuel a une couche donnee (dimension n). (b) Un vecteur de contexte c, derive de l'activation a une couche precoce ou du dernier etat du flux residuel avant la position courante. Le vecteur c encode le contenu semantique local (sujet, type de claim).

- **Classifieur bilineaire.** Le score est s = h^T M c + w_h^T h + w_c^T c + b, ou M est une matrice de taille n x n_c (n_c = dimension du contexte), w_h et w_c sont des vecteurs de biais lineaire, b est un scalaire. Le terme h^T M c signifie : la direction de detection dans l'espace de h est M c, qui depend du contexte. Quand le contexte change, la direction change.

- **Reduction de rang.** M de taille n x n_c a trop de parametres. La factoriser en M = U V^T ou U est de taille n x r et V de taille n_c x r, avec r << min(n, n_c). Le nombre de parametres est r (n + n_c) au lieu de n * n_c. Pour r = 16 et n = n_c = 4096, c'est 131 072 parametres au lieu de 16,8 millions.

- **Agregation.** Score par pas de temps ; maximum ou CUSUM sur l'episode.

**Pourquoi ca ferme la breche.** La sonde conditionnelle adapte sa direction de detection au contexte. Au lieu de chercher un biais dans la direction moyenne (qui dilue le signal), elle cherche dans la direction specifique au contexte courant (qui concentre le signal). Si les directions de biais sont orthogonales entre contextes, la sonde conditionnelle a un rappel maximal dans chaque contexte, tandis que la sonde fixe a un rappel dilue.

---

## 4. Comparaison sonde ponctuelle vs nouveau moniteur

| Propriete | Sonde ponctuelle (lineaire fixe) | Sonde conditionnelle bilineaire |
|---|---|---|
| Direction de detection | Fixe (w) | Variable (M c, depend du contexte) |
| Adaptation au contexte | Aucune | Automatique (via le vecteur c) |
| Signal capte | Composante moyenne sur tous les contextes | Composante specifique au contexte courant |
| Parametres | n + 1 | r (n + n_c) + n + n_c + 1 |
| Risque | -- | Surapprentissage si r est trop grand ; besoin de variete dans les contextes d'entrainement |

**Un moniteur sequentiel multi-couches suffirait-il ?** Partiellement. Un moniteur qui lit plusieurs couches pourrait, en principe, utiliser les couches precoces comme source de contexte et les couches tardives comme source de signal. Mais il devrait encore apprendre implicitement la dependance au contexte a travers un classifieur sur la concatenation, ce qui revient a un classifieur non lineaire implicite. La sonde conditionnelle rend cette dependance explicite et parametrise, ce qui est plus echantillon-efficace : elle exploite la structure « direction de biais = fonction du contexte » au lieu de la decouvrir a partir de donnees.

---

## 5. Verification

**Experience de calibrage (la breche existe-t-elle ?).**
Partitionner les episodes du jeu de donnees par contexte (sujet de la proposition, type de claim). Pour chaque partition, entrainer une sonde lineaire locale. Si les directions apprises (les vecteurs w_k de chaque sonde locale) ont un cosinus moyen faible entre elles (par exemple, cos(w_A, w_B) < 0,3), les directions de biais sont effectivement differentes selon le contexte — la breche est confirmee. Mesurer aussi l'AUROC de la sonde globale (entrainee sur tous les contextes) et des sondes locales (entrainee sur un contexte, testee sur le meme). Si AUROC(locale) > AUROC(globale), la sonde fixe perd du signal par moyennage.

**Experience de validation (le moniteur la ferme-t-il ?).**
Comparer l'AUROC de la sonde fixe, des sondes locales (oracle, utilisant la bonne partition), et de la sonde conditionnelle bilineaire. Critere : AUROC(conditionnelle) > AUROC(fixe) de facon significative, et idealement proche d'AUROC(locales oracle).

---

## 6. Test de falsification

**Experience la moins chere.** Entrainer des sondes lineaires par contexte (k sondes sur k partitions) et calculer la similarite cosinus de leurs vecteurs de poids. Si tous les cosinus sont superieurs a 0,8, la direction de biais est stable a travers les contextes — il n'y a pas de rotation contextuelle et la sonde conditionnelle n'apporte rien par rapport a la sonde fixe. Cout : k entrainements de sonde lineaire (quelques secondes chacun) et k(k-1)/2 calculs de cosinus.

---

## 7. Anteriorite

**Sondes conditionnelles et bilineaires dans le sondage des representations.** Les formes bilineaires pour le sondage linguistique sont utilisees par **Hewitt et Manning (2019), « A Structural Probe for Finding Syntax in Word Representations »** (sonde structurelle pour la distance syntaxique, forme bilineaire h^T B h). Le principe d'une direction de sonde qui depend du contexte est implicite dans les travaux sur les sondes specifiques a la tache.

**Li et al. (2024), « Inference-Time Intervention: Eliciting Truthful Answers from a Language Model. »** Utilisent des directions d'intervention qui varient par couche et par tete d'attention, ce qui est une forme de conditionnement sur l'architecture (mais pas sur le contenu).

L'application d'une sonde bilineaire conditionnelle au contexte semantique pour la detection de tromperie ou de biais diffus dans un LLM est **inconnue de moi** en tant que publication formelle.
