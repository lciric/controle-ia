# Tour III.2 — Critique de méthode des propositions B, D et E (par A)

**Statuts.** Les contenus des pièces 1 à 3 sont RAPPORTÉS (brouillons non scellés) ; les inspections de la pièce 4 sont OBSERVÉES-NON-AUDITÉES ; mes analyses, duels et conditions sont des HYPOTHÈSES. Je n'ai audité ni dépôt, ni code, ni PDF. Les pièces 1 et 2 sont des extraits : les critères PB-1 à PB-14 et la table gelée de P3-bis ne sont pas fournis ; je ne les reconstitue pas.

**Pièce C** : absente (jamais lancée) ; rien n'est dit sur elle.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **« Scores déterministes, donc seul le lancement est un degré de liberté » — faux par omission d'un degré de liberté documenté.** B conclut que l'antériorité de T0.7 ne protège que la décision de lancer l'étape A. Or la pièce 2 (RAPPORTÉ, l. 924-940) dit que la garde d'ouverture de l'étape A lit les clés *permises* `SCELLEMENT-JEUX-T07-JD/-JC/-JA` et que « l'ensemble présent fixe `sondes_lues` ». Quelles sondes sont notées à l'étape A dépend donc de quelles lignes de jeux ont été scellées avant son ouverture. Si le verdict de P3-bis est connu (option (b)), la session mère peut sceller ou ne pas sceller un jeu *selon* ce que le témoin positif a vu — par exemple n'ouvrir que la famille qui a « vu ». C'est un canal de sélection sur l'instrument lui-même, pas sur la décision de lancer. L'argument de B va dans le bon sens, mais sa « condition pour changer d'avis » (figer la seule décision de lancer) est insuffisante : il faudrait aussi figer l'ensemble des clés de jeux avant le scellement de P3-bis. Même remarque pour la relance autorisée après `R11-arret` (« relance une fois sur la même carte », pièce 2) : décider de relancer ou de déclarer un nœud est un choix qu'un verdict connu peut orienter.

2. **Le mécanisme de chiffrement proposé ne protège contre rien de ce que B a lui-même identifié.** B nomme la session mère comme canal de fuite, puis propose une clé « dérivée de l'entropie de P3-bis et d'un sel inscrit dans le registre ». L'entropie figure en clair dans la ligne de commande de lecture (pièce 1, point 3 : `--entropie 1733988…`) et le registre est écrit par la session mère. La clé est donc connue de l'acteur dont on veut se protéger. De plus, B oublie un fichier : la sortie standard de `lecture` (pièce 1, point 3 : redirigée vers `traces/p3bis-<run>/sortie-lecture-v1.txt`) *imprime* `issue_mecanique` ; c'est un canal textuel aussi lisible que les JSON. Un contrôle de fermeture qui ne couvre pas les traces et les codes de sortie est incomplet.

3. **Asymétrie (a)/(c) mal décrite.** B dit que (a) « ne peut pas créer de nœud irréversible » tandis que (c) le peut. Or la pièce 1 (RAPPORTÉ, QO-1 (a)) dit que la levée par mot de Lazar « rend alors T0.7 impossible sur 7b sous son texte ». L'irréversibilité est la même ; seule diffère la nature du déclencheur (humain vs calendaire). B transforme une différence de gouvernance en différence de risque.

4. **Faits recopiés avec un sens changé.** B présente « sous l'hypothèse nulle, 0,014 » comme « taux de fausses alertes » par épisode. Dans la pièce 1 (point 10), ce 0,014 sort d'une *simulation* (20 000 répliques, seuil aléatoire gardé), pas d'une mesure sur les honnêtes. B présente l'emplacement B comme « contrôle de longueur » : ce n'est vrai que si la règle d'ajustement égalise A et B, ce que le texte traite comme conditionnel (réserve « longueur de B différente »). Les effectifs « ≈ 200 messages de colludeurs » sont un chiffre sans source ni mention « illustratif » (règle 4) ; avec 100 épisodes de collusion, 2 colludeurs et jusqu'à 4 messages publics par agent (3 tours + 1 final, RAPPORTÉ), l'ordre de grandeur serait plutôt 800 (illustratif), ce qui change la lecture de la « résolution limitée ».

5. **La matrice 2×2 de Q1 est vraie par construction dans une cellule et confondue dans deux autres.** B suppose que C4 isole « la consigne seule ». Mais la cellule C4 telle que la pièce 4 la propose (RAPPORTÉ) inclut le canal privé « pour symétrie avec C1 ». Donc C1 − C2 et C4 vs C3 changent *tous deux* consigne et canal privé. La case « le canal privé, pas la consigne seule, porte le signal » n'est pas identifiable avec ces quatre cellules ; la case « incohérent, audit R4 » n'est pas incohérente : elle est compatible avec une sonde qui lit la présence d'un historique privé (présent dans C4, absent dans C2). Seul un plan où consigne et canal varient séparément (voir E) sépare les deux.

6. **Fuite construction/évaluation non traitée.** B reprend la base des mots du brouillon sans mentionner que sa pénalité est choisie sur CORE et appliquée à STEGO (pièce 4, B4, OBSERVÉ-NON-AUDITÉ), ce qui rend « au-delà des mots » quasi acquis sur STEGO. Un duel qui conclut « lecture interne » sur STEGO via D3 est, dans cet état, vrai par construction.

### (b) Conditions de perte de puissance ou d'injugeabilité

- **Différence d'aires C1 − C2 (appariée par scénario).** Soit \(p_k = P(s_{C_k} > s_{C_3})\). L'aire est un rang : si \(p_1 = p_2 = 1\) (séparation parfaite dans les deux cellules), alors \(\widehat{A}_{C_1} - \widehat{A}_{C_2} \equiv 0\) quel que soit le déplacement des scores bruts. Le duel 1 de B est injugeable dès que la sonde sature, ce que l'attente N2 du brouillon (aires ≥ 0,99 sur STEGO pour les gros modèles) rend plausible. Il faut une statistique sur les scores (différence de scores normalisés) à côté de la différence d'aires.
- **Intervalles par blocs.** Avec \(m = 20\) blocs (STEGO), le percentile-bootstrap d'une statistique de rang a une couverture inférieure au nominal ; la borne basse « strictement positive » rejette trop souvent. Condition : \(m \le 20\) et corrélation intra-bloc \(\rho > 0\) (deux réplicats, deux colludeurs, plusieurs mains) → variance sous-estimée d'un facteur proche de \(1/(1+(n_b-1)\rho)\) (illustratif).
- **Duel 3 (proportion propre).** \(H_A : p \ge 0{,}5\), \(H_B : p < 0{,}2\) ne sont pas exhaustives ; pour \(n = 100\) épisodes, \(\widehat{p} \sim \mathrm{Bin}(100,p)/100\), écart type ≈ 0,05 à \(p = 0{,}45\) : la zone \([0{,}2;0{,}5[\) absorbe une fraction non négligeable des cas. B ne dit pas ce que la matrice 2×2 devient sous « partiellement jouée ».
- **C3 contre C3 « ≈ 0,50 ».** Un demi-partage des témoins n'a pas de loi fixée si la partition n'est pas gelée ; sans graine et sans règle de partition, la valeur attendue n'est pas 0,50 exactement (dépend de la stratification par scénario).

### (c) Contrôles négatifs dont l'absence serait fatale

- **Répétition à contexte identique, dans un lot différent** : mesure le plancher de bruit de \(|s(x,c)-s(x,c)|\) en bf16 (la garde d'identité du brouillon ne couvre que la passe principale, pas les passes C2/C4).
- **Échange entre deux consignes honnêtes** (témoin → témoin d'un autre réplicat) : loi nulle du « tout changement de contexte » ; sans elle, C1 − C2 > 0 ne dit pas que le changement est spécifique à la collusion.
- **Honnête contre honnête apparié (siège, tour, scénario)** : aire attendue ≈ 0,5 ; absence fatale pour interpréter J-b.
- **Prédicteur de métadonnées** (siège, tour, longueur du message) agrégé comme la sonde : B ne le mentionne pas ; sans lui, la case « le texte domine » peut être « la position domine ».

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Même omission que B sur `sondes_lues`.** D affirme que l'ordre protège « la non-contingence de la production des scores ». Il ignore que le *périmètre* des scores produits (quelles sondes de jeux JD/JC/JA) dépend de clés scellées *avant* l'ouverture de l'étape A (pièce 2, RAPPORTÉ). La non-contingence que D décrit n'existe que si ces clés sont elles-mêmes figées avant tout verdict ; D ne l'exige pas dans sa condition de bascule vers (b).

2. **Le duel QO-A n'est pas une inférence forte.** « Les gardes implémentent-elles la machine d'états ? » est un essai logiciel (R5) ; aucune des deux issues ne falsifie une hypothèse sur une loi de probabilité. D le reconnaît (« pour les chemins testés ») mais le présente comme duel. Il manque le test différentiel d'E : deux exécutions à issues scientifiques différentes doivent produire des sorties autorisées *identiques* ; sans cela, les codes de sortie (fact : lecture « échec », ligne 2 = run sans résumé) peuvent révéler une ligne de la table.

3. **Le duel QO-B est P3-bis lui-même, avec des critères que D n'a pas.** D écrit « Seuil : exactement les critères PB gelés » puis « E′ et plusieurs seuils sont absents ». Un duel dont le seuil n'est pas dans les pièces n'est pas évaluable ici ; c'est honnête, mais le livrable ne contient alors qu'une liste de métriques sans issue falsifiante vérifiable.

4. **Duel Q1-B : « même contexte » n'existe pas entre un colludeur et un honnête.** Le siège (nom, position dans l'ordre de parole) diffère par construction ; les messages publics antérieurs dans l'historique sont les mêmes, mais la consigne de siège (nom) change. D ne nomme pas le siège comme facteur ; son « texte de colludeur contre texte honnête dans le même contexte » confond texte et siège, sauf si la cellule C4 est construite avec la consigne du colludeur *réattribuée au nom de l'honnête* — ce que ni la pièce 4 ni D ne spécifient.

5. **Les négatifs de J-b ne sont pas propres.** D (comme les autres) utilise « honnêtes des mêmes épisodes de collusion » comme négatifs. Ces agents lisent, dans l'historique public, les arguments des colludeurs ; s'ils sont persuadés, leur activation se déplace vers la classe positive. J-a (témoins) n'a pas ce défaut. D ne prévoit pas la comparaison J-a / J-b comme diagnostic de contamination.

6. **Point correct que je reprends en le disant** : D note que le 0,014 est une simulation, pas un taux de fausses alertes mesuré ; et que « déclarer l'écart » sous (b) ne rétablit pas la cécité. Je m'appuie sur ces deux points.

### (b) Conditions de perte de puissance ou d'injugeabilité

- **Critère PB-1 « borne basse > quantile 0,95 du plancher »** : les 200 directions \(w \sim \mathcal{N}(0, \Sigma)\) sont tirées de la covariance des jetons d'entraînement et notées sur les mêmes épisodes que la sonde. Si le texte planté déplace les activations le long d'une direction de forte variance de \(\Sigma\), les directions aléatoires captent une part \(\propto w^\top \Sigma_{\text{eff}} w\) de l'effet : le quantile 0,95 monte *avec* l'effet. La pièce 1 (point 10) chiffre ce cas : plancher à 0,65 ou 0,70 → aire minimale détectable 0,7124 ou 0,7624. Le critère perd sa puissance précisément quand l'effet planté est « gros et diffus ». D cite la puissance mais pas ce couplage.
- **Critère par épisode \(k \ge 6\)** : le seuil est le maximum des scores honnêtes (ordre statistique de rang \(n_H = 60\)). Si la longueur générée \(L\) des actions sous A dépasse stochastiquement celle sous H, alors \(E[\max_{t \le L} s_t]\) croît avec \(L\) sans signal conceptuel, et \(P(k \ge 6)\) sous le nul vrai n'est plus 0,014. Les longueurs de *consigne* sont égalisées (pièce 1, point 2) ; rien dans les extraits ne contrôle la longueur *générée*. Non jugeable sans ce contrôle.
- **Duel Q1-B, gain sur les mots** : si la base lexicale est apprise sur CORE et lue sur STEGO (pièce 4, B4), la loi de son aire sur STEGO est celle d'un classifieur hors domaine, centrée près de 0,5 : le gain est positif par construction. D le signale ; il faut l'écrire comme condition de refus de D3.
- **Faux positifs « au seuil retenu »** : avec \(n_{\text{neg}} = 40\) (J-d STEGO) et \(\alpha = 0{,}05\), le seuil est le 2ᵉ plus haut score négatif ; la variance de l'estimateur du quantile \(1-\alpha\) domine celle du taux de détection ; non jugeable sous \(n_{\text{neg}}\,\alpha < 5\) (illustratif).

### (c) Contrôles négatifs dont l'absence serait fatale

- **Comparaison J-a vs J-b pour la même sonde** (contamination des honnêtes d'épisodes de collusion).
- **Longueur générée par emplacement (A, T, B, H)** dans P3-bis, et aire conditionnelle à la longueur ; sans cela le critère par épisode est injugeable.
- **Répétition à contexte identique entre lots** (D l'exige, mais ne dit pas qu'un écart non nul rend ses « scores identiques » inatteignables : il faut une tolérance gelée).
- **Deux consignes honnêtes échangées** (D l'a : bon ; son absence serait fatale au duel Q1-A).

---

## Sur la proposition E

### (a) Défauts de méthode

1. **\(D_C = E|\Delta|\) a un biais positif sous le nul.** Si \(\Delta = s(x,c_{\text{coll}}) - s(x,c_{\text{hon}})\) a une loi centrée mais non dégénérée (bruit numérique de lot, bf16, ordre de calcul), \(E|\Delta| > 0\) et croît avec l'écart type du bruit. \(H_A : D_C \le \delta_C\) ne peut être tenue que si \(\delta_C\) est calibré sur la loi de \(|\Delta|\) à contexte *identique* — ce qu'E prévoit comme contrôle, mais sans dire que \(\delta_C\) doit en être dérivé. Sans cette dérivation, \(\delta_C\) est un paramètre libre choisi avant lecture mais sans ancrage : le duel devient une décision arbitraire.

2. **Le plan factoriel est juste mais sous-spécifié sur les cellules hors politique.** E déclare certaines combinaisons « artificielles » et « diagnostiques ». Mais la sonde S-C est apprise sur des activations produites sous contextes naturels (C1 et honnêtes) ; appliquée à un contexte jamais vu (consigne honnête + canal privé de collusion), elle est évaluée hors du support d'entraînement. Le plancher apparié (200 directions, Σ des jetons d'entraînement) est lui aussi hors support. Ce n'est pas une fuite, c'est un décalage de covariable : les aires de ces cellules n'ont pas le même étalonnage que les autres, et E ne demande pas un plancher recalculé sur Σ de chaque cellule.

3. **L'« instruction privée honnête » est le meilleur contrôle proposé par les trois propositions — et il n'est pas construit.** E ne dit ni son contenu, ni sa longueur appariée, ni qui l'écrit (un sous-agent neuf, règle R2 ?), ni si elle est jouée (générée) ou seulement relue. Si elle est seulement relue (texte honnête sous consigne honnête + instruction privée ajoutée), elle est hors politique comme C2 ; si elle est jouée, c'est une nouvelle génération (coût non chiffré, E le reconnaît).

4. **Duel « discrimination restante » : \(G\) compare deux détecteurs à seuils calibrés séparément.** Deux seuils calibrés sur 40 ou 100 négatifs ont chacun une variance d'ordre statistique ; la différence de taux de détection hérite des deux. E ne dit pas que les seuils doivent être calibrés sur un jeu *disjoint* de celui où le taux de détection est mesuré (sinon fuite calibration/évaluation ; avec J-d STEGO : 40 témoins, impossible de séparer).

5. **QO-1 : l'expérience de fermeture est la seule des trois qui soit un vrai test différentiel.** Je m'en sers en le disant : « sorties scientifiques secrètement différentes » → sorties autorisées identiques. Défaut : E ne liste pas les sorties autorisées à partir des faits (codes de sortie, empreintes, `resume.json`, `sondes-figees.json`, pièce 1 point 6) ; or les *empreintes* des fichiers fermés diffèrent nécessairement entre deux issues (sha256 de `lecture-p3bis.json`). Une empreinte ne révèle rien si l'espace des issues est grand, mais avec cinq valeurs possibles (« vu », « non vu », « non tranché », « échec », « non lu ») et un fichier dont le reste est déterministe, l'empreinte permet une attaque par dictionnaire si le reste du fichier est reconstructible. E devrait exclure ce cas ou exiger un sel dans le fichier scellé.

6. **E omet, comme B et D, le degré de liberté `sondes_lues`** (clés JD/JC/JA, pièce 2). Sa phrase « choix des sondes, abandon opportuniste » le nomme en général sans le rattacher à la garde qui le rend possible.

### (b) Conditions de perte de puissance ou d'injugeabilité

- **Duel « contexte »** : avec agrégation par le maximum sur les jetons, \(s = \max_t s_t\) est une statistique d'extrême ; \(\Delta\) est la différence de deux maxima dont les argmax peuvent différer. Sa loi est un mélange : masse près de 0 quand le jeton maximal et son activation sont peu touchés, queue lourde sinon. L'intervalle par scénario (50 blocs CORE) d'une moyenne de mélange à queue lourde a une couverture dégradée ; le test « borne haute ≤ δ_C » (falsification de H_B) perd sa puissance quand la queue domine la variance. Condition : kurtosis de \(\Delta\) élevé — à mesurer sur la répétition à contexte identique.
- **Invariance pratique** : si la sonde sature (\(s\) borné par la normalisation gelée sur CORE et distribution des scores de colludeurs collée au bord), \(|\Delta|\) est comprimé vers 0 par l'échelle, non par l'invariance : H_A « vraie » par plafonnement. Condition : proportion de scores C1 au-dessus du 99ᵉ centile de l'échelle gelée > 0,2 (illustratif).
- **Duel « discrimination restante »** : taux de détection à 5 % de fausses alertes, \(n_{\text{neg}} = 40\) → seuil = 2ᵉ ordre statistique ; \(\mathrm{Var}(\widehat{TD})\) inclut \(\mathrm{Var}(\widehat{q}_{0{,}95})\), qui pour 40 observations est de l'ordre de celle d'un quantile extrême : injugeable. Pour \(n_{\text{neg}} = 100\) (J-d CORE), à 1 % le seuil est le maximum : même conclusion (la pièce 4, M5, le signale).
- **Instruction privée honnête** : si sa longueur en jetons \(L_{\text{priv}}\) n'est pas appariée à celle du canal privé de collusion, l'effet mesuré est \(\beta_{\text{instr}} + \beta_{L}(L_{\text{coll}} - L_{\text{priv}})\) ; sans appariement, non identifiable.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Répétition à contexte identique entre lots** (E l'a ; fatal s'il manque : c'est la loi de \(|\Delta|\) sous le nul).
- **Instruction privée honnête appariée en longueur** (E l'a sans construction ; fatal s'il manque pour toute phrase « consigne de collusion » plutôt que « consigne privée »).
- **Calibration des seuils sur un jeu disjoint** (E ne l'a pas ; fatal pour \(G\)).
- **Plancher recalculé par cellule** (E ne l'a pas ; fatal pour comparer des aires entre cellules de supports différents).

---

## Ce que je tire des trois, en le disant

- Des trois, seul E propose un test de fermeture falsifiable (différentiel) ; B et D testent des artefacts (chiffrement, machine d'états) qui ne réfutent rien sur l'information transmise. Aucun des trois ne nomme la garde `sondes_lues` (pièce 2), qui est, à ma lecture, le canal concret par lequel un verdict connu de P3-bis changerait T0.7 sans toucher à ses scores.
- Sur Q1, B et D croient qu'une ou deux cellules suffisent ; la pièce 4 (M2) montre qu'elles confondent consigne et canal ; E a la bonne structure (factorielle) mais pas les seuils ni les contrôles de bruit qui la rendent jugeable. Aucun des trois ne traite le siège comme facteur, ni la contamination des honnêtes de J-b, ni la longueur générée dans P3-bis.
- Point commun non contestable : dans ce banc, l'étiquette *est* l'instruction ; toute sonde qui lit l'instruction est juste par construction. Les trois le disent ; aucune cellule proposée ne mesure une intention.

FIN-DE-CELLULE