# Moniteur C-2 : Sondage causal par perturbation (moniteur du jacobien)

Famille : C -- adaptation. Proposeur : P2.

---

## 1. Breche analysee

**Mimicry statique sans mimicry causale.** Un adversaire peut apprendre a produire des activations dont la distribution marginale, dans la direction sondee, est indistinguable de celle d'un agent honnete. Mais cette mimicry est *statique* : elle porte sur les valeurs, pas sur le role causal que ces dimensions jouent dans le calcul. La sonde ponctuelle ne mesure que la valeur et ne teste jamais la *consequence* d'une perturbation dans la direction sondee.

---

## 2. Modele de menace

**Ou vit le signal.** L'adversaire informe connait la direction w de la sonde et s'entraine a produire, pour chaque pas de temps, une valeur de la composante h . w (ou h est l'etat du flux residuel) qui tombe dans l'intervalle typique des agents honnetes. Le biais diffus (propositions scientifiques orientees) est encode dans d'autres dimensions ou dans des interactions non lineaires entre dimensions.

**Pourquoi ca echappe a la sonde ponctuelle.** La sonde mesure h . w. Si l'adversaire controle cette projection, la sonde ne distingue pas un agent honnete d'un agent trompeur masque. C'est une attaque sur la *statistique suffisante* de la sonde.

**Ce que la mimicry ne couvre pas.** Dans un agent honnete, la direction w joue un role causal : perturber la composante de h dans w change le comportement d'une maniere coherente avec son role (par exemple, pousser vers « plus honnete » produit un texte plus prudent, pousser vers « moins honnete » relache les controles). Dans un agent trompeur masque, la composante dans w est un *decoy* : elle a ete forcee a une valeur honnete mais elle ne pilote plus le comportement trompeur. Perturber le decoy ne devrait pas changer le biais diffus, ou le changer de maniere incoherente -- parce que le biais est encode ailleurs.

**Plausibilite pour un 8B.** La mimicry statique est la strategie d'adaptation la plus naturelle : c'est l'objectif direct d'un reglage fin adversariel (minimiser le score de la sonde). Un 8B soumis a une pression adversarielle sur la sonde converge vers cette strategie avant d'autres plus couteuses. Le decouplage causal est donc attendu.

**Hypothese sur l'adversaire.** Il connait w, le seuil, la couche sondee. Il a optimise ses activations dans w pour mimer la distribution honnete. Il ne connait pas le protocole de perturbation (quel vecteur est ajoute, a quel moment, dans quelle couche).

---

## 3. Nouveau moniteur propose

**Principe.** Mesurer le *jacobien comportemental* dans la direction de la sonde : comment le comportement du modele repond a une petite perturbation de ses activations dans w. Un agent honnete dont la direction w est causalement liee a son honnete montrera une reponse coherente ; un agent masque montrera une reponse faible ou incoherente.

**Architecture.**
- **Entrees.** L'etat du flux residuel a la couche sondee, pour chaque pas de temps. On intervient sur cet etat a un sous-ensemble de pas de temps (choisis par tirage aleatoire dans l'episode).
- **Intervention.** A chaque pas de temps selectionne, ajouter un vecteur epsilon . w a l'activation (ou epsilon est une petite constante, positive ou negative). Propager le calcul modifie jusqu'a la sortie (les K tokens suivants).
- **Mesure.** Pour chaque intervention, comparer la sortie perturbee a la sortie originale. Calculer : (a) la divergence KL entre les distributions de tokens sur les K tokens suivants, (b) la direction du changement semantique (le texte perturbe est-il « plus prudent » ou « moins prudent » selon un classifieur de surface ?).
- **Classifieur.** Le moniteur extrait deux traits par episode : (a) la sensibilite moyenne (divergence KL moyenne apres perturbation dans w), (b) la coherence directionnelle (correlation entre le signe de la perturbation et la direction du changement semantique). Un classifieur lineaire sur ces deux traits separe les agents honnetes (sensibilite elevee, coherence directionnelle forte) des agents masques (sensibilite faible ou coherence brisee).

**Agregation.** La sensibilite et la coherence sont moyennees sur les pas de temps perturbes (au moins 20 par episode) puis sur les couches sondees (2 a 3 couches).

**Pourquoi il resiste a l'adversaire informe.** Pour tromper le moniteur causal, l'adversaire devrait non seulement mimer les *valeurs* dans w mais aussi mimer la *reponse aux perturbations* dans w. Cela signifie que la direction w devrait jouer un role causal coherent dans le modele -- ce qui est contradictoire avec le fait qu'elle est un decoy. L'adversaire serait oblige de reencode son comportement trompeur dans la direction w (pour que la perturbation de w change effectivement le biais), ce qui le rendrait a nouveau detectable par la sonde ponctuelle originale.

En d'autres termes : le moniteur causal place l'adversaire dans un dilemme. Soit w est un decoy (la sonde ponctuelle est battue mais le moniteur causal detecte l'incoherence), soit w est causalement lie au biais (le moniteur causal est satisfait mais la sonde ponctuelle detecte a nouveau).

---

## 4. Comparaison sonde ponctuelle vs nouveau moniteur

| Critere | Sonde lineaire ponctuelle | Moniteur causal |
|---|---|---|
| Ce qu'il mesure | Valeur dans la direction w | Role causal de la direction w |
| Robustesse a la mimicry statique | Nulle | Elevee (la mimicry statique ne preserve pas la causalite) |
| Type d'information | Observationnelle | Interventionnelle |
| Cout de calcul | Tres faible | Eleve (necessite des passes avant supplementaires pour chaque perturbation) |
| Faux positifs | Calibres sur w | Calibres sur la reponse aux perturbations d'agents honnetes |

**Un moniteur sequentiel multi-couches suffirait-il ?** Non. Un moniteur sequentiel agrege des scores ponctuels sans jamais perturber les activations. La mimicry statique appliquee couche par couche et pas par pas le tromperait aussi. Le moniteur causal apporte une information d'un type different (interventionnelle, pas observationnelle), qui ne peut pas etre obtenue par la seule extension sequentielle.

---

## 5. Verification

**Experience de calibrage (la breche existe-t-elle ?).**
1. Entrainer un organisme 8B trompeur et une sonde lineaire ponctuelle.
2. Regler finement l'organisme pour masquer dans la direction w de la sonde (reglage fin adversariel).
3. Mesurer la sensibilite et la coherence directionnelle de l'organisme masque et de l'organisme honnete apres perturbation dans w.
4. Prediction : l'organisme masque montre une sensibilite significativement plus faible et/ou une coherence directionnelle brisee par rapport a l'agent honnete.

**Experience de validation (le moniteur ferme-t-il la breche ?).**
1. Entrainer le classifieur du moniteur causal sur des paires (honnete, trompeur non adapte) en utilisant la sensibilite et la coherence comme traits.
2. Evaluer sur l'organisme masque (adapte a la sonde ponctuelle).
3. Critere de succes : AUROC > 0,80 sur l'organisme masque, avec un adversaire qui a ete informe de la sonde lineaire mais pas du protocole de perturbation.

---

## 6. Test de falsification

**Experience la moins chere.** Prendre un organisme 8B masque (qui trompe la sonde ponctuelle) et mesurer la sensibilite aux perturbations dans w sur 50 episodes. Si la sensibilite de l'organisme masque est dans le meme intervalle de confiance a 95 % que celle de l'organisme honnete, le moniteur causal ne detecte rien de supplementaire. Cout : une centaine de passes avant supplementaires (50 episodes x 2 perturbations chacun).

---

## 7. Anteriorite

- **Meng et al. (2022), « Locating and Editing Factual Associations in GPT. »** (ROME) Utilisent des interventions causales sur les activations pour localiser des faits. Le principe de perturbation-reponse est similaire, mais applique a la localisation de faits, pas a la detection de tromperie.
- **Geiger et al. (2023), « Causal Abstraction. »** Cadre theorique pour l'analyse causale des representations dans les reseaux de neurones. Pertinent pour le principe mais n'est pas applique a la detection de tromperie adversarielle.
- **L'application specifique** -- utiliser le jacobien comportemental comme moniteur de tromperie robuste a un adversaire informe -- est inconnue de moi en tant que proposition publiee.
