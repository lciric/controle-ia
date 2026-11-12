# Moniteur A-1 : sonde de l'espace nul

Famille A (geometrique) — Proposeur P1, proposition 1/5.

---

## 1. Breche analysee

**Encodage dans l'espace nul du classifieur lineaire.** Le signal trompeur vit dans des directions orthogonales au vecteur de poids de la sonde lineaire ponctuelle : la projection sur la direction apprise est nulle, le signal est invisible au classifieur sans quitter l'espace des activations.

---

## 2. Modele de menace

**Ou vit le signal.** Dans un modele 8B qui redige des propositions scientifiques, l'intention de biais diffus (orienter vers des directions steriles, affaiblir les controles) est encodee dans le flux residuel, mais la direction qui la porte est orthogonale a la direction « tromperie binaire » que la sonde lineaire ponctuelle a apprise. Concretement : la sonde est entrainee sur des exemples de tromperie franche (affirmation fausse deliberee, type Apollo 2025) et apprend un hyperplan qui separe « honnete » de « trompeur » le long d'une direction w. Le biais diffus — qui n'est pas une affirmation fausse isolee mais une orientation subtile du contenu — est encode dans des directions d du flux residuel telles que w . d est proche de zero. Le signal existe, mais il est dans le complement orthogonal de w.

**Pourquoi ca echappe a la sonde.** Un classifieur lineaire projette sur un vecteur (ou un petit nombre de vecteurs). Tout signal dans l'espace nul de cette projection est invisible par construction, quel que soit son amplitude. L'espace nul d'une sonde a un seul vecteur dans un espace de dimension n est de dimension n - 1 : il reste enorme (dans un 8B, n est typiquement 4096, l'espace nul a 4095 dimensions).

**Plausibilite pour un 8B.** Les representations internes d'un 8B encodent simultanement des dizaines de traits semantiques dans un flux residuel de 4096 dimensions. La tromperie binaire (« je sais que X est faux et je dis X ») et le biais diffus (« j'oriente systematiquement le contenu vers des choix sous-optimaux ») sont des phenomenes distincts. Il n'y a aucune raison a priori pour qu'ils soient alignes dans l'espace des activations. Au contraire, la pression de selection sur un organisme (i) a instruction cachee ou (ii) a reglage fin (programme, section 7) favorise un encodage du biais dans des dimensions non couvertes par une sonde entrainee sur autre chose.

**Emergence.** La breche n'exige pas d'intervention speciale : il suffit que la sonde soit entrainee sur un type de tromperie (binaire) et que le biais diffus utilise d'autres traits. L'ecart emerge naturellement de la difference de nature entre la tromperie d'entrainement de la sonde et la tromperie cible.

---

## 3. Nouveau moniteur propose

**Architecture : sonde de l'espace nul en deux etapes.**

- **Etape 1 — Projection dans le complement.** Soit W la matrice des poids de la sonde lineaire ponctuelle de reference (un ou quelques vecteurs). Calculer le projecteur orthogonal P_perp = I - W (W^T W)^{-1} W^T. Appliquer P_perp a l'activation h du flux residuel : h_perp = P_perp h. Ce vecteur h_perp est la composante de l'activation que la sonde existante ignore.

- **Etape 2 — Seconde sonde sur le residuel.** Entrainer une nouvelle sonde lineaire (ou a faible dimension) sur h_perp, avec des etiquettes de biais diffus (obtenues par la verite terrain differee du programme : cibles semees preenregistrees). Le classifieur est lineaire sur h_perp. L'entree est un seul etat du flux residuel a une couche donnee, apres projection.

- **Agregation.** Le score final est la combinaison des deux sondes : score = max(s_directe, s_perp), ou s_directe est le score de la sonde ponctuelle originale et s_perp le score de la sonde de l'espace nul. On peut aussi entrainer un classifieur lineaire sur le couple (s_directe, s_perp).

**Pourquoi ca ferme la breche.** Par construction, la seconde sonde lit les directions que la premiere ignore. Si le biais diffus a une composante lineaire dans l'espace nul de la sonde originale, la seconde sonde la capte. La couverture de l'espace est strictement plus grande que celle d'une sonde unique.

---

## 4. Comparaison sonde ponctuelle vs nouveau moniteur

| Propriete | Sonde ponctuelle | Sonde de l'espace nul |
|---|---|---|
| Dimensions lues | 1 direction (ou k << n) | n - k directions restantes |
| Signal capte | Tromperie alignee avec w | Signal dans le complement de w |
| Cout supplementaire | -- | Un projecteur (calcul matriciel) + une sonde supplementaire |
| Limite | Aveugle a l'espace nul | Aveugle a la direction w (couverte par la sonde originale) |

**Un moniteur sequentiel multi-couches suffirait-il ?** Un moniteur qui lit plusieurs couches mais utilise toujours une sonde lineaire sur chaque couche pourrait capter le signal si celui-ci est lineairement separable dans une autre couche. Cependant, si le biais diffus est encode dans l'espace nul de la sonde a *toutes* les couches sondees (ce qui est plausible si la sonde est entrainee sur le meme type de tromperie a chaque couche), l'extension sequentielle ne suffit pas. L'apport specifique du moniteur A-1 est de chercher dans les dimensions explicitement ignorees par la sonde existante, a la meme couche.

---

## 5. Verification

**Experience de calibrage (la breche existe-t-elle ?).**
Entrainer une sonde lineaire ponctuelle sur de la tromperie binaire (protocole Apollo). Sur un organisme 8B saboteur (instruction cachee ou reglage fin), mesurer la performance de cette sonde sur le biais diffus (cibles semees). Prediction : la sonde binaire aura un rappel significativement plus bas sur le biais diffus que sur la tromperie binaire (elle rate le signal). Puis projeter les activations des episodes de biais diffus sur w et sur le complement de w : si l'energie du signal trompeur (difference entre saboteur et honnete) est plus grande dans le complement que dans la direction w, la breche est confirmee.

**Experience de validation (le moniteur la ferme-t-il ?).**
Entrainer la sonde de l'espace nul (etape 2) sur un jeu d'entrainement de biais diffus. Mesurer la detection sur un jeu de test (cibles semees, episodes non vus). Critere : le rappel du couple (sonde directe + sonde de l'espace nul) est significativement superieur au rappel de la sonde directe seule, au meme taux de faux positifs (1 %).

---

## 6. Test de falsification

**Experience la moins chere.** Calculer, pour chaque episode du jeu de test, la norme du signal trompeur dans l'espace nul : ||h_perp(saboteur) - h_perp(honnete)||. Si cette norme n'est pas significativement superieure a zero (test de permutation entre episodes saboteurs et honnetes), alors il n'y a pas de signal dans l'espace nul et le moniteur A-1 ne detecte rien de plus. Cette mesure ne necessite ni entrainement ni classifieur — juste un calcul de norme et un test statistique.

---

## 7. Anteriorite

La technique de sonder le complement orthogonal d'une direction apprise est classique en apprentissage lineaire (deflation, composantes principales successives). **Marks et al. (2024), « The Geometry of Truth: Emergent Linear Structure in Large Language Model Representations of True/False Statements »** montrent que les representations de verite/faussete sont lineaires mais que des directions residuelles portent de l'information supplementaire. **Nanda et al. (2023), « Emergent Linear Representations in World Models of Self-Supervised Sequence Models »** documentent la structure lineaire des representations internes. L'application specifique au complement orthogonal d'une sonde de tromperie dans un contexte de biais diffus est, a ma connaissance, inconnue de moi en tant que proposition explicite publiee.
