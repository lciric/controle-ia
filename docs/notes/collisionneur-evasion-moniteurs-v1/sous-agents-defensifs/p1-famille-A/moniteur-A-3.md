# Moniteur A-3 : sonde quadratique (interactions de traits)

Famille A (geometrique) — Proposeur P1, proposition 3/5.

---

## 1. Breche analysee

**Encodage non lineaire par interaction de traits.** Le signal trompeur n'est porte par aucune direction individuelle des activations mais par le produit (l'interaction) de deux ou plusieurs traits. Chaque trait pris isolement est ambivalent ; c'est leur conjonction qui distingue le biais diffus du comportement honnete. Un classifieur lineaire, qui ne lit que des projections sur des directions, est structurellement aveugle aux interactions.

---

## 2. Modele de menace

**Ou vit le signal.** Dans le flux residuel d'un 8B redigeant des propositions scientifiques, deux composantes A et B des activations sont, prises separement, presentes dans des contextes honnetes : par exemple, A pourrait encoder « le budget est mentionne » et B « la methodologie est critiquee ». Mais la conjonction A et B — le budget est mentionne pour justifier une critique methodologique qui oriente vers un protocole plus couteux et moins rigoureux — est un marqueur de biais diffus. Le signal trompeur vit sur une variete de dimension au moins 2, definie par le produit h_i * h_j de deux (ou plus) composantes des activations. Geometriquement, c'est une surface quadratique (un paraboloide, une selle) dans l'espace des activations, pas un demi-espace.

**Pourquoi ca echappe a la sonde.** Une sonde lineaire calcule w^T h + b, une fonction affine des activations. Elle ne peut pas representer le terme h_i * h_j. Si le signal trompeur est dans ce terme croise, la sonde lineaire ne le voit pas, quel que soit le choix de w. C'est une limite structurelle, pas un probleme d'entrainement.

**Plausibilite pour un 8B.** Les reseaux de neurones apprennent des representations ou l'information est souvent encodee dans des interactions entre dimensions, pas seulement dans des directions individuelles (c'est le principe meme du perceptron multi-couches). Dans un 8B sous pression de superposition, ou les dimensions sont reutilisees, l'encodage par interaction est une facon efficace de stocker de l'information supplementaire sans occuper de nouvelle direction. Un biais diffus — qui depend du contexte (sujet de la proposition, phase de redaction) — est un bon candidat pour un encodage conditionnel (« biais si et seulement si contexte X et action Y »), donc non lineaire.

**Emergence.** L'encodage non lineaire n'est pas une strategie de l'agent : c'est une propriete de la representation apprise par le modele de base. Le reglage fin ou l'instruction cachee ne fait que deposer le biais dans la representation existante. La forme non lineaire de ce depot est une consequence de l'architecture du transformeur (les couches d'attention et les couches MLP produisent des interactions non lineaires entre traits).

---

## 3. Nouveau moniteur propose

**Architecture : sonde quadratique.**

- **Entrees.** Le meme etat du flux residuel h (vecteur de dimension n) a une couche donnee.

- **Extension quadratique.** Construire le vecteur etendu h_ext = [h ; vech(h h^T)] ou vech extrait la partie triangulaire superieure du produit exterieur h h^T. Ce vecteur contient les n composantes originales plus les n(n+1)/2 termes croises. Pour n = 4096, c'est environ 8,4 millions de termes — trop pour un classifieur dense. Deux reductions possibles :
  - (a) **Noyau quadratique.** Ne pas construire h_ext explicitement mais utiliser un classifieur a noyau polynomial de degre 2 : k(h, h') = (h^T h' + 1)^2. Le classifieur est lineaire dans l'espace du noyau mais quadratique dans l'espace des activations.
  - (b) **Projection aleatoire des termes croises.** Projeter les termes croises sur un espace de dimension reduite (d << n^2) par une matrice aleatoire fixe (schema de Johnson-Lindenstrauss) puis entrainer un classifieur lineaire sur le vecteur projete.

- **Classifieur.** Lineaire sur la representation etendue (noyau ou projection). Le seuil est fixe pour 1 % de faux positifs.

- **Agregation.** Score par pas de temps ; agregation sur l'episode par maximum ou par somme cumulee (CUSUM), mais le coeur de la proposition est la sonde quadratique, pas l'agregation.

**Pourquoi ca ferme la breche.** La sonde quadratique lit les termes d'interaction h_i * h_j que la sonde lineaire ignore. Si le biais diffus est encode dans ces interactions, la sonde quadratique le detecte.

---

## 4. Comparaison sonde ponctuelle vs nouveau moniteur

| Propriete | Sonde ponctuelle (lineaire) | Sonde quadratique |
|---|---|---|
| Fonction de decision | w^T h + b (affine) | h^T Q h + w^T h + b (quadratique) |
| Capacite de detection | Demi-espaces | Surfaces quadratiques (ellipsoides, hyperboloides) |
| Nombre de parametres | n + 1 | n(n+1)/2 + n + 1 (ou moins avec projection) |
| Risque de surapprentissage | Faible | Eleve si non regularise ; reduit par le noyau ou la projection |

**Un moniteur sequentiel multi-couches suffirait-il ?** Non. Un moniteur sequentiel qui lit plusieurs couches mais applique un classifieur lineaire a chaque couche reste aveugle aux interactions au sein d'une meme couche. Si le signal est dans h_i * h_j a la couche L, lire d'autres couches ne le revele pas (sauf si une couche ulterieure linearise l'interaction, ce qui est possible mais non garanti). L'apport de la sonde quadratique est de lire les interactions a la couche ou elles vivent.

**Mise en garde.** La sonde quadratique a beaucoup plus de parametres que la sonde lineaire. Le risque de surapprentissage est le principal obstacle. La regularisation (L2 forte, projection aleatoire, noyau a faible rang) est indispensable. Si le signal d'interaction est faible, le surapprentissage peut faire croire a une detection qui n'existe pas — d'ou l'importance du test de falsification.

---

## 5. Verification

**Experience de calibrage (la breche existe-t-elle ?).**
Sur un jeu de donnees d'activations etiquetees (saboteur vs. honnete), mesurer l'AUROC d'un classifieur lineaire et d'un classifieur quadratique (noyau polynomial de degre 2). Si l'AUROC du classifieur quadratique est significativement superieur, il y a du signal dans les interactions que le lineaire rate — la breche est confirmee. Utiliser une validation croisee stricte (k-fold) pour ecarter le surapprentissage.

**Experience de validation (le moniteur la ferme-t-il ?).**
Sur un jeu de test non vu (cibles semees), mesurer le rappel du couple (sonde lineaire + sonde quadratique) vs. la sonde lineaire seule, au meme taux de faux positifs (1 %). Critere : le rappel du couple est significativement superieur.

---

## 6. Test de falsification

**Experience la moins chere.** Entrainer un classifieur lineaire sur h et un classifieur quadratique sur h (noyau polynomial degre 2), avec la meme regularisation relative et le meme jeu d'entrainement. Comparer leurs AUROC en validation croisee. Si l'AUROC quadratique n'est pas significativement superieur au lineaire (test de DeLong sur les courbes ROC), la breche « encodage par interaction » n'existe pas dans ces donnees et le moniteur A-3 n'apporte rien. Cout : aucun materiel supplementaire, juste un classifieur a noyau sur les activations deja extraites.

---

## 7. Anteriorite

**Classifieurs a noyau sur les activations internes.** L'utilisation de noyaux polynomiaux ou RBF sur les representations de reseaux de neurones est classique en apprentissage automatique. **Alain et Guillaume (2017), « Understanding intermediate layers using linear classifier probes »** utilisent des sondes lineaires ; la generalisation aux sondes non lineaires est mentionnee comme extension mais rarement evaluee sur la tromperie.

**Burns et al. (2023), « Discovering Latent Knowledge in Language Models Without Supervision » (CCS/Contrast-Consistent Search).** Utilisent une sonde non lineaire (reseau a une couche) pour decouvrir des representations de verite. Cependant, leur objectif est la verite factuelle, pas la tromperie deliberee ou le biais diffus.

L'application d'une sonde quadratique a la detection de tromperie ou de biais diffus dans un LLM est **inconnue de moi** en tant que publication formelle.
