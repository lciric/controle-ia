# Moniteur A-2 : desuperposition par auto-encodeur creux

Famille A (geometrique) — Proposeur P1, proposition 2/5.

---

## 1. Breche analysee

**Superposition tromperie-trait honnete.** La direction qui encode le biais diffus est confondue (par polysemantie) avec un trait honnete du domaine (par exemple « prudence methodologique », « conscience du cout », « scepticisme scientifique »). La sonde lineaire ponctuelle ne peut pas separer les deux signaux parce qu'ils partagent la meme direction dans l'espace des activations.

---

## 2. Modele de menace

**Ou vit le signal.** Un 8B represente des dizaines de concepts dans un espace de 4096 dimensions. La superposition (Elhage et al., 2022) fait que deux traits semantiquement distincts — par exemple « je doute de ce resultat » (scepticisme honnete) et « j'oriente vers une conclusion biaisee » (biais diffus) — peuvent partager la meme direction dans le flux residuel. Les deux activent la meme composante parce que le modele n'a pas assez de dimensions pour les separer.

**Pourquoi ca echappe a la sonde.** La sonde lineaire ponctuelle projette sur une direction. Si cette direction est partagee par un trait honnete frequent (le scepticisme scientifique est normal dans des propositions d'experiences), le classifieur voit du signal positif aussi bien chez l'agent honnete que chez le saboteur. Il y a deux issues, toutes deux mauvaises : (a) le seuil est monte pour reduire les faux positifs, mais alors le rappel chute (la sonde ne detecte plus le biais diffus) ; (b) le seuil est bas, le rappel est bon mais les faux positifs explosent (la sonde signale tout scepticisme comme tromperie). La superposition cree un dilemme precision-rappel fondamental pour tout classifieur lineaire operant sur la representation brute.

**Plausibilite pour un 8B.** La superposition est d'autant plus forte que le modele est petit : un 8B a moins de dimensions qu'un 70B pour representer les memes concepts. La probabilite que « tromperie diffuse » et un trait honnete du domaine scientifique partagent une direction est plus elevee dans un 8B que dans un modele plus grand. C'est un argument quantitatif : l'hypothese de superposition (Elhage et al.) predit que le nombre de traits depasse le nombre de dimensions, et que la superposition augmente avec le ratio traits/dimensions.

**Emergence.** La superposition est une propriete de la representation apprise, pas une strategie deliberee de l'agent. Elle emerge a l'entrainement du modele de base. L'organisme (i) a instruction cachee n'a pas besoin de la construire : elle est deja la.

---

## 3. Nouveau moniteur propose

**Architecture : sonde apres desuperposition par auto-encodeur creux.**

- **Etape 1 — Auto-encodeur creux (Sparse Autoencoder, SAE).** Entrainer un auto-encodeur creux sur les activations du flux residuel a une couche donnee du 8B. Le SAE apprend un dictionnaire de traits monosemantiques : chaque neurone du SAE correspond (idealement) a un seul concept. L'activation brute h est decomposee en une representation creuse z = encodeur(h) ou z a beaucoup plus de dimensions que h mais la plupart sont nulles.

- **Etape 2 — Sonde lineaire sur les traits du SAE.** Entrainer une sonde lineaire sur z (les activations creuses du SAE), avec des etiquettes de biais diffus. Le classifieur est lineaire sur z, ce qui est equivalent a un classifieur non lineaire sur h (puisque z = encodeur(h) est une transformation non lineaire de h).

- **Entrees.** Un seul etat du flux residuel a une couche, comme la sonde ponctuelle. Le cout supplementaire est l'inference du SAE (un passage avant).

- **Agregation.** Score scalaire : la sortie de la sonde sur z. L'agregation sur l'episode (si souhaitee) est la moyenne ou le maximum des scores par pas de temps, mais la proposition ici porte sur la desuperposition, pas sur la sequentialite.

**Pourquoi ca ferme la breche.** Si le trait « biais diffus » et le trait « scepticisme honnete » partagent la meme direction dans h mais sont representes par des neurones distincts dans z (c'est l'objectif du SAE), la sonde sur z peut distinguer les deux. Le dilemme precision-rappel de la sonde brute disparait.

---

## 4. Comparaison sonde ponctuelle vs nouveau moniteur

| Propriete | Sonde ponctuelle | Sonde apres SAE |
|---|---|---|
| Espace de classification | Activations brutes (4096 dim) | Traits creux (>> 4096 dim, creux) |
| Separabilite | Limitee par la superposition | Superposition reduite par le dictionnaire |
| Cout supplementaire | -- | Entrainement du SAE + inference du SAE par pas |
| Risque | -- | Le SAE peut ne pas isoler le trait « biais diffus » si celui-ci n'est pas un trait naturel du modele |

**Un moniteur sequentiel multi-couches suffirait-il ?** Non pour cette breche. La superposition est une propriete geometrique de la representation a chaque couche. Lire plusieurs couches ne desenchevetre pas deux traits superposes dans une meme couche. Il faudrait que le signal soit desuperpose a une autre couche, ce qui est possible mais non garanti. Le SAE apporte une solution geometrique directe : augmenter la dimensionnalite pour separer les traits.

---

## 5. Verification

**Experience de calibrage (la breche existe-t-elle ?).**
Identifier, dans le SAE, les neurones qui s'activent fortement pour des episodes honnetes avec du scepticisme scientifique ET pour des episodes de biais diffus. Si les memes neurones du SAE s'activent dans les deux cas, la desuperposition n'a pas fonctionne (le SAE n'a pas la resolution suffisante). Si des neurones distincts s'activent, la superposition dans l'espace brut est confirmee (les traits etaient confondus en h mais separes en z).

Mesure complementaire : calculer l'AUROC de la sonde lineaire sur h pour separer « scepticisme honnete » de « biais diffus ». Si l'AUROC est proche de 0,5, la sonde brute ne distingue pas les deux — la breche est confirmee.

**Experience de validation (le moniteur la ferme-t-il ?).**
Comparer l'AUROC de la sonde sur h et de la sonde sur z, sur le meme jeu de test (episodes avec scepticisme honnete vs. biais diffus). Critere : AUROC(sonde sur z) > AUROC(sonde sur h) de facon significative, a taux de faux positifs egal (1 %).

---

## 6. Test de falsification

**Experience la moins chere.** Prendre les activations h des episodes de scepticisme honnete et de biais diffus. Calculer leur similarite cosinus moyenne dans l'espace brut (cos(h_sceptique, h_biais)) et dans l'espace creux (cos(z_sceptique, z_biais)). Si les deux cosinus sont egalement eleves (ou egalement bas), le SAE ne desuperpose pas ces deux traits et le moniteur A-2 n'apporte rien. Cout : zero entrainement de sonde, juste des calculs de similarite sur les activations deja extraites.

---

## 7. Anteriorite

**Elhage et al. (2022), « Toy Models of Superposition » (Anthropic).** Etablissent la theorie de la superposition dans les reseaux de neurones.

**Bricken et al. (2023), « Towards Monosemanticity: Decomposing Language Models With Dictionary Learning » (Anthropic) ; Templeton et al. (2024), « Scaling Monosemanticity » (Anthropic).** Montrent que les auto-encodeurs creux decomposent les activations en traits monosemantiques interpretables.

L'idee d'utiliser un SAE comme etape de pretraitement pour ameliorer une sonde de detection est, a ma connaissance, presente dans des discussions techniques (forums, blogs) mais je ne connais pas de publication formelle evaluant cette chaine (SAE + sonde) pour la detection de tromperie. **Inconnue de moi** en tant que publication formelle avec evaluation empirique.
