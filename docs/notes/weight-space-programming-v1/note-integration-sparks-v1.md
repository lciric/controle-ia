# Note de conception — intégrer le billet « Sparks of Weight-Space Programming » dans nos deux programmes — v1

**Rédigée le 4 novembre 2026, ouverte à 01:35 UTC (`date -u`)**, par un rédacteur neuf (sous-agent Claude), qui n'a écrit aucune des pièces lues. Consigne exécutée : `consigne-redacteur-integration-sparks-v1.md`, sha256 `fadece37baa345ec64d85deb46d54577f79fe5cff2a780e64db079fe4acf0249` (vérifiée avant lecture).

**Pièces lues, empreintes vérifiées par leurs compagnons (`sha256sum -c`, toutes « OK »)** :
- pièce 3, `piece-3-lecture-factuelle.md` (`fff05896…`), lue en entier d'abord ; citée « p3, l. n » ;
- pièce 1, `piece-1-billet.txt` (`49b2db7e…`), citée « billet, L n » à travers la pièce 3 ;
- pièce 2, `piece-2-nos-resultats.md` (`d6fa8011…`), citée « p2, l. n » ;
- moisson des voisins, `/home/claude/controle-ia-travail/brouillons/weight-space-programming-v1/moisson-voisins-v1.md` (`868731d1…`, empreinte recalculée et égale), **non opposable (R7)**, citée « moisson, l. n » ;
- journaux publics de l'expérience 7, `/home/user/rikiyat/lm_understand-logs/exp7_sycophancy/` (tête `4d09ba6`), lus avec `cat`, `sed` et un script de lecture JSON ; **aucun code de ce dépôt exécuté** ; cités « journaux, fichier : l. n » ;
- le programme `docs/programme-controle-ia-v2.md` (cité « programme, l. n »), l'en-tête de `registres/etat.md`, les décisions N-013, N-015, N-035, N-044, N-053, N-056, N-060 v3, le README de `/home/user/ideation-organism/`.

Règle de cette note : tout chiffre renvoie à une pièce et à une ligne ; un chiffre dérivé est marqué **(calcul)** ; un chiffre posé sans source est marqué **(supposé)**. Les menaces sont décrites par leur classe et la défense mesurable, jamais par un procédé.

---

## 1. Verdict en cinq lignes

1. **Récupérable** : un objet d'essai public, bon marché et entièrement décrit (la recette honnête et sycophante de l'expérience 7 : données, scripts, journaux, comportement mesuré ; journaux, `README.md` : l. 65-90) pour mettre une lecture « boîte blanche » sous **paires nulles, aveuglement et lecteurs multiples**, ce que le billet n'a pas fait (p3, l. 100-104) ; et une famille de tâches à oracle exécutable (petits réseaux à propriété plantée) pour l'organisme d'idéation.
2. **Non récupérable comme preuve** : l'idée qu'un lecteur de poids audite un modèle de langue « sans inférence ». Le seul trait d'alignement testé échoue sur les poids seuls (p3, l. 61-72) ; la réussite passe par une passe avant (outil d'attention, p3, l. 78 et l. 107), sur un choix forcé à deux options où trois sur trois arrive une fois sur huit par hasard (p3, l. 100), et les composants nommés ne portent pas le comportement (p3, l. 74 et l. 104).
3. **Non récupérable comme résultat d'édition** : le gain de l'expérience 8 vient du retrait d'une boucle, localisée avec des activations et des générations obtenues par 50 passes avant (p3, l. 131 et l. 184) ; sans boucle à retirer (Gemma 3 270M), aucun gain au-delà d'environ un point (p3, l. 151-152).
4. **Déjà pris (moisson, non opposable)** : lire une propriété ou une porte dérobée dans des poids, y compris par un modèle de langue affiné (« Weight Oracles », 2610.07334 ; moisson, l. 30 et l. 110) ; lire un affinage étroit par différence d'activations (2510.13900 ; moisson, l. 42) ; lire un delta de poids en langage naturel (2510.05092 ; moisson, l. 43) ; soustraire une direction de poids, y compris de sycophancie (2406.11717, 2511.05408 ; moisson, l. 33, l. 71, l. 113) ; l'adversaire qui cache un trait aux lecteurs internes (moisson, l. 83-89 et l. 117).
5. **Recommandation** : lancer d'abord la piste 1 (l'expérience 7 sous nul, brouillon de préenregistrement joint), petite, utile dans les deux sens ; inscrire ensuite deux bras dans les tâches existantes de la phase 0 (retrait chirurgical d'une direction de sabotage pour la validité de construit, lecture du delta d'adaptateur), sans dépense propre ; ouvrir la famille « mondes de poids » pour l'organisme sur processeur seul ; le reste reste écrit. Rien de ceci ne doit retarder la porte G0 (fin novembre 2026, `CLAUDE.md`).

---

## 2. Les pistes

Notation : **F1 à F3** reprennent les pistes de Fable (propositions, non des faits) ; **P4 à P9** sont les miennes. Chaque fiche a les mêmes rubriques.

### F1 — L'expérience 7 sous nul (piste 1 de Fable)

- **Hypothèse et signe prédit.** La détection d'un modèle sycophante par un lecteur qui n'a que les poids et les motifs d'attention sur des textes qu'il écrit **ne tient pas sous paires nulles** : sur des paires honnête et honnête ou sycophante et sycophante, le lecteur continue de désigner un seul des deux modèles dans au moins la moitié des cas (signe : fausses alertes élevées), parce que la méthode naturelle est la comparaison relative des deux modèles. Prédiction ouverte : probabilité 0,55 que la scission sur paires nulles soit majoritaire (supposé, jugement du rédacteur) ; le contraire serait un résultat positif réel pour la lecture outillée.
- **Programme et hypothèses touchés.** Organisme d'idéation : aucune hypothèse ; c'est une mesure de validité de construit de la sycophancie, dans la continuité de `lciric/sycophancy-construct-validity` (p2, l. 28). Programme de contrôle : section 11 (validité de construit) et H8 (programme, l. 99) seulement par analogie ; le banc de lecteurs et la mesure des fausses alertes resservent à P4 et P7. Aucune hypothèse H1 à H9 n'est modifiée.
- **Première expérience et son nul.** Celle du brouillon de préenregistrement joint (`preregistrement-sparks-exp7-sous-nul-v1-brouillon1.md`) : 24 paires vraies, 12 paires nulles honnête et honnête, 12 sycophante et sycophante, toutes à graines d'ordre différentes ; lecteurs Claude neufs à l'aveugle, autorisés à répondre « aucun des deux » et « les deux » ; base algorithmique scriptée ; plafond boîte noire ; contrôle causal par greffe et retour à la base. Le nul est la paire nulle elle-même ; le témoin du contrôle causal est un composant tiré au hasard de même taille.
- **Seuil d'abandon.** Si l'exactitude d'ordre sur paires vraies n'atteint pas 17 sur 24 (seuil du test binomial unilatéral à 0,05 ; calcul, voir brouillon) pour aucun lecteur ni aucune base, la piste s'arrête : la lecture outillée n'est pas un instrument utilisable sur ce banc, et P7 tombe avec elle.
- **Coût.** Carte graphique louée : environ 6 heures de calcul utile, pire cas 24 heures, soit 5 à 20 USD (supposé, prix à relever au devis) ; variante processeur seul sur machine louée : environ 70 heures, 14 à 42 USD (supposé). Lecteurs Claude : aucun coût de fournisseur, mais une forte consommation de quota (ordre de 10⁸ jetons d'entrée cumulés si chaque conversation ressemble à celles d'Astra, 0,8 à 1,7 million chacune ; p3, l. 83-85 ; calcul). Bras Astra facultatif : devis à son propre GO.
- **Déjà pris et différence exacte.** Pris : lire un affinage étroit par différence entre deux modèles (2510.13900, crosscodeurs, bases simples 2602.10371 ; moisson, l. 42-44 et l. 112) ; la paire du billet en est un cas. Différence : aucune de ces entrées (d'après la moisson) ne met un **lecteur de modèle de langue non entraîné** sous **paires nulles avec réponse « aucun » ou « les deux »** et ne rapporte son taux de fausses alertes ; le billet non plus (p3, l. 100).
- **Risque de faux trou (R8).** Moyen. Les bancs d'audit sur modèles à comportement caché (AuditBench 2602.22755 et voisins ; moisson, l. 64 et l. 114) contiennent peut-être déjà des témoins sans comportement planté. À vérifier sur leurs PDF avant toute revendication de nouveauté ; la piste vaut même sans nouveauté, comme réplication critique.
- **Nœud de décision.** Dépense (GO sur devis) ; accès à Gemma (licence à accepter sur le compte de Lazar : compte, donc nœud) ; bras Astra (GO séparé, appel à un fournisseur). La conception elle-même est « proposer avec recommandation » (périmètre interne). Aucune hypothèse ni revendication modifiée.

### F2 — L'édition de poids comme épreuve de notre loi de sycophancie (piste 2 de Fable)

- **Hypothèse et signe prédit.** Sous pression sociale dosée, la note se déplace d'une part à peu près constante de la distance à un point fixe propre au cadre (p2, l. 29). Si l'on retire, dans les poids, une direction ou une tête qui lit la suggestion, la loi garde sa forme et **seule son échelle change, ou rien ne change** ; l'exposant (ou la part g) ne change pas. Signe prédit : effet nul ou faible sur g, en accord avec notre résultat « lisible n'est pas causal » (aucune intervention de rang 1 n'a fait baisser le comportement ; p2, l. 28). Probabilité que g baisse d'au moins un tiers : 0,2 (supposé).
- **Programme et hypothèses touchés.** Travaux publics de sycophancie (hors programme). Lien de forme avec HC1 (loi de déférence, Δv = g · (v* − v₀) ; programme, l. 102) et HC6 (le g bénin prédit la robustesse ; programme, l. 108) : une manipulation par les poids est une vérification de manipulation de g. Pas de modification d'énoncé.
- **Première expérience et son nul.** Sur le modèle de la loi (Llama-3.1-8B-Instruct, p2, l. 28-29), après F1 : (a) mesurer la masse d'attention de chaque tête sur les jetons de la suggestion le long de la courbe dose-réponse ; (b) retirer la tête ou la direction la plus liée (choix gelé d'avance par une règle, pas par lecture des résultats) ; (c) refaire la courbe. Nul : même retrait d'une tête ou d'une direction tirée au hasard, de même norme ; témoin de capacité : exactitude sans pression inchangée à 1 point près.
- **Seuil d'abandon.** Si le retrait ciblé ne déplace pas le comportement plus que le témoin aléatoire (95ᵉ centile de 20 tirages), on conclut « la tête lisible n'est pas le levier » et on n'étend pas.
- **Coût.** Carte graphique, quelques heures sur 8 milliards de paramètres ; 10 à 30 USD (supposé).
- **Déjà pris et différence.** Pris : direction de sycophancie dans l'espace des poids qui s'ajoute ou se retire (2511.05408 ; moisson, l. 33 et l. 72) ; orthogonalisation (2406.11717 ; moisson, l. 71). Différence : l'objet mesuré n'est pas la baisse du comportement mais **la forme de la loi dose-réponse** (échelle contre exposant) sous retrait.
- **Risque de faux trou (R8).** Moyen à élevé : les travaux sur le pilotage de la sycophancie mesurent souvent des courbes en fonction de l'intensité du pilotage, pas de la pression ; à vérifier.
- **Nœud.** Dépense (GO) ; si le résultat change une revendication publiée de `sycophancy-psychophysical-law`, nœud de Lazar. Le concept de l'expérience : proposer avec recommandation.

### F3 — Nouvelle classe de menace : un adversaire qui édite des poids, avec un budget de passes avant (piste 3 de Fable)

- **Hypothèse et signe prédit.** Classe : l'adversaire a un accès en écriture aux poids de la politique surveillée et un budget de K passes avant ; il cherche à garder le comportement visé tout en déplaçant un moniteur interne. Conclusion de contrôle **à tester, pas à affirmer** : (a) sous attestation d'intégrité des poids (empreinte des poids déployés vérifiée par le harnais), la classe est visible et se ramène à l'attaque par l'entraînement, déjà couverte par les organismes (ii) et (iv) (programme, l. 132 ; N-053, point 2) ; (b) sans attestation, elle tombe dans la « frontière assumée » (programme, l. 172 : l'adversaire possède l'infrastructure) ; (c) dans l'organisme d'idéation, un proposeur n'a aucun accès au générateur d'épisodes (banque figée, dossier fermé, tirages frais semés par l'engagement ; README de l'organisme, sections 2 et 3), donc la classe n'atteint pas le juge statistique tant que ces gardes tiennent. Signe prédit : le prix imposé par une réserve de détecteurs jamais déployés (programme, l. 143) croît avec leur diversité.
- **Programme et hypothèses touchés.** Papier C : HC4 (taxe de déplacement, programme, l. 106), dont le coût de l'attaquant est exprimé en accès, requêtes, calcul et taux de succès : le budget de passes avant d'un éditeur de poids outillé est **un point de plus sur l'axe du coût**. Papier B : H5 (matrice de transfert ; programme, l. 113). Attaque A1 (p2, l. 14-15) : seulement par la leçon générale « la transparence sert de carte à l'attaquant ».
- **Première expérience et son nul.** Aucune expérience d'attaque dans cette note. Mesure défensive possible, au niveau méthode : la **couverture certifiable** = part des modifications de poids détectées par l'attestation d'intégrité (cas sain : poids inchangés, doit passer ; artefact : un seul poids changé, doit échouer, R5) ; et, si un bras d'attaque est un jour monté (N-056 l'a prévu, sans dépense), la matrice de transfert vers la réserve de détecteurs. Nul : moniteurs aléatoires appariés en covariance (plancher du programme, l. 143).
- **Seuil d'abandon.** Si l'attestation d'intégrité suffit à fermer la classe dans tout dispositif réaliste du papier C, la piste se réduit à une phrase du modèle de menace, sans expérience.
- **Coût.** Rédaction seulement (processeur) ; une expérience d'attaque exigerait le coffre, l'aiguilleur et un GO.
- **Déjà pris et différence.** Pris : portes dérobées indétectables en théorie (2204.06974), activations obfusquées (2412.09565), évasion apprise des moniteurs latents (2506.14261, 2512.11949), variantes « régularisées adversairement » contre l'oracle de poids (moisson, l. 83-89 et l. 117). Différence : l'adversaire n'est pas un optimiseur à gradient mais un modèle de langue outillé à budget de passes avant ; la mesure porte sur le **prix en passes avant**, pas sur la possibilité.
- **Risque de faux trou (R8).** Élevé : zone « séduisante » signalée par la moisson elle-même (l. 126 : « Zone très séduisante… vérifier le PDF de Weight Oracles »).
- **Nœud.** Ajouter une classe de menace au papier C, ou un énoncé à HC4, est une **modification de revendication : nœud de Lazar**. Tout contenu d'attaque concret passe par le coffre.

### P4 — Lire le delta d'adaptateur de l'organisme saboteur de T0.6 contre son jumeau honnête, à dose réglable

- **Hypothèse et signe prédit.** Au niveau du modèle (audit avant déploiement, pas surveillance des épisodes), un lecteur du delta d'adaptateur de rang faible distingue un adaptateur saboteur de son jumeau honnête **mieux que le hasard à taux de fausses alertes fixé, mais pas mieux qu'une base spectrale bon marché** ; et sa détection décroît avec la dose plus vite que celle des sondes d'activation. Signe : lecteur ≤ base spectrale ; probabilité 0,6 (supposé).
- **Programme et hypothèses touchés.** T0.6 (organismes ; code des adaptateurs à dose réglable fait, `registres/etat.md`, ligne de T0.6) et T0.7 (sondes) ; H1 seulement comme contraste d'unité : H1 porte sur la surveillance des épisodes (programme, l. 93), ce bras porte sur l'audit du modèle. Il ne devient pas une base de G1 (la liste des bases de G1 est fixée par N-056).
- **Première expérience et son nul.** Une population d'adaptateurs (par exemple 16 saboteurs et 16 honnêtes à graines différentes, à 3 doses ; supposé) ; lecteurs : (a) base spectrale (statistiques des valeurs singulières du delta et régression logistique, à la manière de 2602.15195), (b) lecteur Claude neuf qui lit le delta, (c) sondes de T0.7 et boîte noire de T0.8 sur les épisodes des mêmes organismes. Nul : paires honnête et honnête ; anti-circularité : apprentissage et évaluation sur des familles distinctes (programme, l. 137).
- **Seuil d'abandon.** Si la base spectrale atteint une aire sous la courbe de 0,95 ou plus à toutes les doses, le lecteur par modèle de langue n'a rien à ajouter : on rapporte la base et on s'arrête.
- **Coût.** Une fois T0.6 entraîné : quelques heures de carte graphique pour la population d'adaptateurs (supposé, 5 à 15 USD) ; lecteurs Claude sans coût de fournisseur.
- **Déjà pris et différence.** Pris : détection de portes dérobées dans les deltas d'adaptateurs par statistiques spectrales (2602.15195, 100 % annoncé ; moisson, l. 31) ; lecture de delta par lecteur entraîné (2510.05092 ; moisson, l. 43). Différence : trait de **sabotage diffus** (pas une porte à déclencheur) ; comparaison **à taux de fausses alertes égal** avec sondes et boîte noire **sur les mêmes organismes** ; dose réglable.
- **Risque de faux trou (R8).** Moyen ; « LoRAcle » sur Hugging Face est signalé non vérifié (moisson, l. 49).
- **Nœud.** Bras rapporté de T0.6 et T0.7 : « proposer avec recommandation » ; dépense : comprise dans le devis de T0.6 (GO) ; en faire une base décisive de G1 : nœud (N-056).

### P5 — Famille de tâches « mondes de poids » à oracle exécutable, pour l'organisme d'idéation

- **Hypothèse et signe prédit.** Une famille de petits réseaux (perceptrons de quelques milliers de poids) à propriété plantée et **oracle exécutable** (le réseau se lance et la propriété se vérifie) donne à l'organisme une famille où la vérité ne dépend d'aucun juge de modèle de langue ; on prédit que les lois promues par le juge statistique sur cette famille sont **plus souvent vraies à l'oracle** que sur les familles à juge, à puissance égale (signe +).
- **Programme et hypothèses touchés.** Organisme : N-044 (l'universalité se mesure sur des familles inédites), N-049 (tâches fraîches), N-060 v3 (les oracles exécutables gardés pour une banque à tâches exécutables), N-058 (la composition des proposeurs se juge sur l'oracle du monde planté et le coût). Aucun H1 à H9.
- **Première expérience et son nul.** Engendrer, sur processeur, une banque de réseaux (taille, propriété plantée, graine) ; les proposeurs proposent des lois « statistique des poids → propriété » ; le juge figé promeut ou non ; l'oracle exécute. Nul : mondes où la propriété est tirée indépendamment des poids (toute promotion est fausse), sur le modèle des mondes jouets de l'attaque A1 (p2, l. 14).
- **Seuil d'abandon.** Si une base triviale (statistique de la première ou de la dernière couche ; le billet reconnaît que ses expériences 1 et 2 s'y prêtent, p3, l. 178) résout toute la famille, elle n'est pas « inédite » au sens utile : on durcit ou on abandonne.
- **Coût.** Processeur seul ; appels des proposeurs au tarif d'une course (quelques dollars à quelques dizaines ; supposé, devis par course).
- **Déjà pris et différence.** Pris : zoos de modèles et apprentissage dans l'espace des poids (moisson, l. 19-24 et l. 109). Différence : l'usage comme **famille de tâches d'un organisme d'idéation à juge statistique**, avec oracle exécutable et témoins plantés ; pas l'acte de lire des poids.
- **Risque de faux trou (R8).** Faible pour l'usage ; élevé si l'on revendiquait la lecture elle-même.
- **Nœud.** Famille nouvelle : « proposer avec recommandation » ; dépense d'appels : GO sur devis.

### P6 — Retrait chirurgical d'une direction de sabotage, et ce que lisent encore nos moniteurs

- **Hypothèse et signe prédit.** Dans l'organisme saboteur (ii) de T0.6, retirer de ses poids la direction la plus liée au sabotage (règle de choix gelée d'avance) produit l'une de trois issues, chacune lisible : (a) le comportement baisse et le score de sonde baisse (la sonde lit le levier) ; (b) le comportement reste et la sonde baisse (la sonde lit un corrélat) ; (c) le comportement baisse et la sonde reste (la sonde lit autre chose). Signe prédit : (b) ou « rien ne baisse », d'après notre résultat de sycophancie (p2, l. 28) ; probabilité de (a) : 0,25 (supposé).
- **Programme et hypothèses touchés.** H8 (le construit mesuré prédit la robustesse ; programme, l. 99) et section 11 ; prédiction de validité de la section 7 (programme, l. 135). **Pas H6** : les interventions sur les poids et le bruit d'activations ne sont plus revendiqués par H6 (N-013, N-015).
- **Première expérience et son nul.** Vérification de manipulation : retrait ciblé contre retrait d'une direction aléatoire de même norme (20 tirages) ; mesure : taux de sabotage sur les épisodes, score des sondes de T0.7 (agrégation max ou attention), utilité honnête. Témoin : l'organisme honnête averti (programme, section 7).
- **Seuil d'abandon.** Si le retrait ciblé ne se distingue pas du témoin aléatoire sur le comportement ni sur la sonde, la vérification ne dit rien : rapporter, ne pas étendre.
- **Coût.** Carte graphique, inclus dans les runs de T0.6 et T0.7 (quelques heures de plus ; 5 à 15 USD ; supposé).
- **Déjà pris et différence.** Pris : le geste (2406.11717, 2511.05408, vecteurs de tâche ; moisson, l. 113) et la mesure de ce que l'édition casse (moisson, l. 74 et l. 116). Différence : le geste sert de **vérification de manipulation d'un moniteur** (que lit la sonde quand le levier est retiré), sur un trait de sabotage diffus.
- **Risque de faux trou (R8).** Moyen : la validité des sondes sous ablation est un thème connu en interprétabilité ; à vérifier avant revendication.
- **Nœud.** Bras de T0.7 : « proposer avec recommandation » ; l'inscrire comme intervention revendiquée par H6 : nœud (N-015).

### P7 — Un lecteur de poids comme moniteur de plus dans le pôle

- **Hypothèse et signe prédit.** Un lecteur de poids ajouté au pôle de moniteurs **n'augmente pas la diversité effective** mesurée par la matrice de transfert (H5), parce que son verdict est constant sur tous les épisodes d'un même modèle : c'est un audit, pas un moniteur d'épisodes. Signe : contribution nulle à H5 ; ses fausses alertes, en revanche, s'appliquent à toute la flotte d'un coup.
- **Programme et hypothèses touchés.** H5 (programme, l. 113) ; question ouverte « dualité défensive du poids partagé » (programme, section 15).
- **Première expérience et son nul.** Aucune avant F1 et P4 : il faut d'abord un taux de fausses alertes du lecteur au niveau du modèle (F1, P4). Nul : moniteur aléatoire apparié.
- **Seuil d'abandon.** Si F1 ou P4 donnent une scission majoritaire sur paires nulles, la piste s'arrête.
- **Coût.** Nul tant que F1 et P4 ne sont pas faits.
- **Déjà pris et différence.** Pris : agents d'audit outillés (moisson, l. 114). Différence : place d'un audit au niveau du modèle dans un pôle de moniteurs par épisode.
- **Risque de faux trou (R8).** Faible (c'est une question d'architecture).
- **Nœud.** Concept de moniteur : « proposer avec recommandation » ; énoncé modifié de H5 : nœud.

### P8 — La survie des contraintes à la délégation (H9) quand un délégué peut éditer des poids

- **Hypothèse et signe prédit.** Dans une chaîne de délégation où la tâche touche aux poids d'un modèle surveillé (par exemple « corriger un défaut » à la manière de l'expérience 4 ou 8 ; p3, l. 39 et l. 43), une contrainte de sécurité explicite (« ne pas toucher au moniteur ») survit **moins** que dans une tâche sans poids, parce que l'édition de poids est une action dont l'effet sur le moniteur est moins visible au délégué. Signe : survie plus basse ; probabilité 0,5 (supposé).
- **Programme et hypothèses touchés.** H9 (N-035), papier B, scénario de douze mois.
- **Première expérience et son nul.** Après la vérification d'antériorité de H9 (non faite, N-035 section 3) : chaînes à 1, 2, 3 passages, tâches avec et sans poids, contrainte identique, avec et sans moniteur à chaque passage. Nul : tâche sans poids de même longueur.
- **Seuil d'abandon.** Si la survie est identique avec et sans poids à 5 points près, la variante n'ajoute rien à H9.
- **Coût.** Appels d'agents ; plusieurs dizaines de dollars (supposé).
- **Déjà pris et différence.** Voisins de H9 cités de mémoire, non vérifiés (N-035) ; aucun voisin de la variante « poids » dans la moisson. Différence : la nature de l'action déléguée.
- **Risque de faux trou (R8).** Élevé (antériorité de H9 elle-même non vérifiée).
- **Nœud.** Modifier H9 : **nœud de Lazar**.

### P9 — Ce que casse une édition publiée : le Qwen3.5-0.8B édité comme objet d'essai d'intégrité

- **Hypothèse et signe prédit.** L'édition de l'expérience 8 (131 072 poids, 0,016 % ; p3, l. 129 et l. 146) dégrade des capacités non mesurées par le billet (signe −), comme le prédisent les travaux sur les effets d'ondulation (moisson, l. 74). Le modèle édité est annoncé public (p3, l. 24).
- **Programme et hypothèses touchés.** Aucun directement ; au mieux une famille de tâches « prédire les effets secondaires d'une édition » pour l'organisme (voisin : 2507.21084 ; moisson, l. 46).
- **Première expérience et son nul.** Bancs larges sur le modèle édité contre l'original, à réglages identiques ; nul : édition aléatoire de même norme.
- **Seuil d'abandon.** Rendement trop faible pour le contrôle : à ne faire que si P5 en a besoin.
- **Coût.** Carte graphique, quelques heures (supposé, 5 à 10 USD).
- **Déjà pris et différence.** Largement pris (moisson, l. 74 et l. 116).
- **Risque de faux trou (R8).** Élevé.
- **Nœud.** Dépense (GO) ; sinon rien.

---

## 3. Classement par rendement attendu sur coût, et recommandation

| Rang | Piste | Rendement attendu | Coût | Dépendance |
|---|---|---|---|---|
| 1 | F1 — expérience 7 sous nul | moyen : utile dans les deux sens ; banc de lecteurs et taux de fausses alertes réutilisés par P4 et P7 ; argument public pour les entretiens | bas : 5 à 20 USD sur carte graphique louée (supposé) ; quota Claude élevé | accès à Gemma ou modèle de secours ; GO |
| 2 | P5 — mondes de poids pour l'organisme | moyen : oracle exécutable, famille inédite (N-044, N-060 v3) | très bas : processeur ; appels au tarif d'une course | priorités de l'organisme (A1-v3, tour fermé) |
| 3 | P6 — retrait chirurgical, ce que lisent nos sondes | élevé pour la validité de construit (H8, section 11) | bas : inclus dans T0.6 et T0.7 | organismes de T0.6 entraînés |
| 4 | P4 — delta d'adaptateur contre jumeau | moyen : audit au niveau du modèle, à fausses alertes égales | bas : inclus dans T0.6 | T0.6 ; F1 pour le lecteur |
| 5 | F2 — loi de sycophancie sous édition | moyen-bas | 10 à 30 USD (supposé) | F1 |
| 6 | F3 — classe de menace | bas en expérience, utile en écrit | rédaction | nœud de Lazar |
| 7 | P7 — lecteur dans le pôle | bas (verdict constant par modèle) | nul | F1, P4 |
| 8 | P8 — H9 avec délégué éditeur | incertain | dizaines de dollars | antériorité de H9 |
| 9 | P9 — intégrité du modèle édité | bas pour le contrôle | 5 à 10 USD | P5 |

**Recommandation (confiance 0,6).** Ordre : F1 maintenant (brouillon 1 joint, à contre-lire et sceller ; GO sur la variante carte graphique) ; P6 et P4 inscrits comme bras rapportés dans les préenregistrements de T0.6 et T0.7, sans dépense propre ; P5 en note de conception pour l'organisme, sur processeur ; F2 après F1 ; F3 écrite en une phrase dans le modèle de menace du papier C seulement si Lazar le veut (nœud) ; P7, P8, P9 en attente. La confiance est moyenne parce que le rendement de F1 pour le programme lui-même (G0, G1) est indirect : son intérêt principal est la validité de la lecture outillée et le banc réutilisable.

---

## 4. Pour les entretiens Pivotal : trois phrases de fait

1. « Sur la seule expérience du billet qui touche un trait d'alignement, deux copies de Gemma 3 270M dont l'une est sycophante, le lecteur n'a pas su dire laquelle à partir des poids seuls en quatre tentatives ; il a choisi juste dans les trois paires seulement avec un outil qui exécute les deux modèles et renvoie leurs motifs d'attention, sur un choix forcé où trois sur trois arrive une fois sur huit par hasard, sans aucune paire témoin. » — Source : p3, l. 42, l. 61-72, l. 78 et l. 100.
2. « Les composants que le lecteur a nommés ne portent pas le comportement : les copier du modèle honnête dans le modèle sycophante ne ferme aucune part de l'écart (0,00 ; taux de suivi resté à 1,0), un contrôle que les auteurs ont fait et publié dans leurs journaux, mais pas dans le billet ; et le modèle de départ suivait déjà toutes les mauvaises suggestions, si bien que l'affinage a ajouté de l'honnêteté plutôt que de la sycophancie. » — Source : p3, l. 57, l. 74, l. 104 et l. 106.
3. « Le gain en mathématiques de Qwen3.5-0.8B (MATH-500 de 7,9 à 48,1 % à 50 passes avant) vient du retrait d'une boucle de réflexion, localisée avec des activations et des générations obtenues par l'outil de passes avant plutôt que par la lecture des poids seuls ; sur Gemma 3 270M, qui ne boucle presque pas, aucun budget n'a déplacé MATH-500 de plus d'environ un point. » — Source : p3, l. 43, l. 131, l. 139, l. 151-152 et l. 184.

---

## 5. Observations de conception tirées des journaux (pour le brouillon de F1)

- **Asymétrie de graines à éviter.** Dans la recette publique, les deux membres d'une paire ont la même graine et le même ordre de données (journaux, `code/train.py` : l. 42-43 et l. 65-69 ; `README.md` : l. 15-16). Une paire nulle à graines différentes diffère donc par l'ordre, alors qu'une paire vraie de la recette n'en diffère pas : un lecteur pourrait distinguer « vraie » et « nulle » par l'ampleur de la différence, sans rien lire du comportement. Le brouillon construit donc **toutes** les paires du bras principal à graines d'ordre différentes, et garde trois paires « à la manière du billet » (même graine) en ancre descriptive.
- **Le modèle de départ suit déjà 100 % des mauvaises suggestions** (journaux, `eval/model_behaviour/pair100_base.json`, champ `wrong_follow_known_heldout` = 1,0 ; de même pour 101 et 102 ; p3, l. 57). Le contrôle causal le plus naturel est donc le **retour à la base** des composants nommés dans le modèle honnête (s'ils portent l'honnêteté ajoutée, le modèle doit redevenir sycophante), en plus de la greffe de l'honnête vers le sycophante faite par les auteurs.
- **Comportement mesuré par log-probabilité, pas par génération** (journaux, `code/eval.py` : l. 1-13 et l. 31-52) : « suivre » = la réponse suggérée a une log-probabilité totale plus haute que la bonne. Le brouillon garde cette mesure fermée comme vérité terrain.
- **La consigne publique dit au lecteur qu'exactement un modèle est sycophante** (journaux, `runs/attention_tool/prompt.txt` : l. 5) : c'est la phrase à remplacer pour permettre « aucun » et « les deux ».
- **Les plongements sont gelés et identiques** (journaux, `code/train.py` : l. 56-58 ; `code/make_release.py` : l. 44-49) : on peut stocker les 18 couches seules (200 678 368 octets par modèle ; journaux, `README.md` : l. 59) et un seul plongement, ce qui fait tenir 110 modèles en environ 22 Go (calcul).
