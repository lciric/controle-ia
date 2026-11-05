# Contre-lecture 1 du texte « placebo croisé » (brouillon v1) — règle R2

- **Verdict : à repenser.** Le plan ne départage pas H-style et H-contenu tel qu'il est écrit. Quatre défauts bloquent :
  - le facteur « vérité » est une comparaison entre contenus différents, pas une manipulation ;
  - la règle de décision donne H-style par défaut faute de puissance ;
  - la « mention d'un test » comptée parmi les marqueurs fixe le résultat d'avance ;
  - le plan croisé format × provenance a déjà été publié **sur le même modèle** (Devbunova, 2026, à vérifier). C'est un nœud de décision pour Lazar avant tout code.
- **Relecteur** : sous-agent neuf. Je n'ai écrit ni ce brouillon, ni celui de l'étape 0, ni le code de mesure. Rapport rédigé le 26 octobre 2026 vers 10:15 UTC.
- **Brouillon relu** : `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/hm1-v4-e0/brouillon-placebo-v1-relu.md`, empreinte `befcb88c9d90adb46939b7fdbd0bd48fd51777ed1760c624a30c6d832cf209e5`. Empreinte vérifiée par `sha256sum` avant lecture.

## Fichiers lus et empreintes vérifiées

| fichier | sha256 | conforme à l'empreinte donnée |
|---|---|---|
| `…/scratchpad/hm1-v4-e0/brouillon-placebo-v1-relu.md` | `befcb88c9d90adb46939b7fdbd0bd48fd51777ed1760c624a30c6d832cf209e5` | oui |
| `…/scratchpad/hm1-v4-e0/brouillon-etape0-v1-relu.md` | `2427e3642be3c1eb95819fe55ac5ce522334edd6551286f50e1b9d18bca9ba63` | oui |
| `…/scratchpad/hm1-v4-e0/sources/mesurer_e0_hm1_v4.py` | `9cf8642c15a82bc78e5bff83d3056b27ca1a5b7382f7baff2ee701b50763d7ad` | aucune empreinte donnée par la consigne ; c'est celle que cite le brouillon de l'étape 0 |
| `/root/pilote4-v1/controle-ia-travail/essaim-m3-refonte-v1/pilotes/pilote4-gemini-v6-2-v1-tentative2/reponse-question-g001.md` | `a80e61a8744de366b811cab634b9c1c3048db8e19c82c89910681914194363a0` | oui |
| `/home/user/controle-ia-travail/src/controle_ia/prereg.py` | `3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306` | aucune empreinte donnée |

(`…` = `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6`)

- **Lu dans le dépôt** : rien d'autre. Aucun fichier interdit n'a été ouvert ni haché. Aucune recherche récursive.
- **Validateur** : `problemes()` de `prereg.py` a été exécuté sur le brouillon, avec `python3 -B` pour ne rien écrire dans le dépôt. Sortie : `['section Contre-lecture sans les deux empreintes exigées (brouillon relu et rapport)']`. Les huit sections sont présentes.
- **Recherches sur le web** : publications et licences seulement. Tout chiffre ou titre externe ci-dessous a été lu sur une page HTML ou un résumé, **jamais sur un PDF empreinté** : il reste « à vérifier » au sens de R7.

## Constats

### CLP-01 — bloquant — Antériorité : le plan croisé est déjà publié sur ce modèle (nœud de décision)

- **Endroit** : Plan d'analyse, point 4 (« Ce test ne revendique que le plan croisé marqueurs × vérité… si ce plan est libre ») ; Hypothèse.
- **Problème** : Devbunova (2026, arXiv 2603.19426, à vérifier) croise déjà format de banc d'essai (benchmark / casual) et provenance (eval / deploy, fixée par la source) :
  - même modèle : Llama-3.1-8B-Instruct, en `bfloat16` ;
  - même lieu de mesure : flux résiduel au dernier jeton, couches 8 à 31 ;
  - même cellule placebo « réel avec marqueurs ajoutés » : des requêtes ShareGPT réécrites au format des bancs d'essai ;
  - même conclusion qualitative : la sonde standard suit le format.

  Nayan et al. (2026, arXiv 2606.23583, à vérifier) réutilisent ce plan 2 × 2 pour la détection en boîte noire. Ils rapportent pour Llama-3.1-8B-Instruct une aire sous la courbe qui tombe d'environ 0,644 à 0,491 une fois format et intention décorrélés (à vérifier).

  La zone revendiquée est donc largement occupée. Il ne reste au brouillon que ce qui suit, et chacun de ces points demande à être vérifié :
  - un contenu apparié **dans les quatre bras** : chez Devbunova, le bras « évaluation sans format » vient d'une autre source (MuTual), à vérifier ;
  - un témoin de faux marqueurs, qui a lui-même un précédent chez WARP (ICML 2026, à vérifier) ;
  - des instruments certifiés à l'aveugle au préalable ;
  - des tests d'équivalence.
- **Correction** : c'est un nœud de décision (« zone revendiquée trouvée occupée »). On arrête, et Lazar choisit entre :
  - (a) abandonner ;
  - (b) recadrer en réplication et extension de Devbunova (2026), avec revendication réduite aux quatre points ci-dessus ;
  - (c) repenser vers un facteur de contenu manipulé (voir CLP-02).

  Dans les cas (b) et (c), il faut d'abord lire et empreinter les PDF (R7) et citer Devbunova, Nayan et al. et WARP dans le texte.

### CLP-02 — bloquant — La « vérité » n'est pas un facteur manipulé : H-style et H-contenu ne forment pas une partition

- **Endroit** : Hypothèse ; Prédiction (« plan 2 × 2 croisé, à contenu apparié ») ; Critères (« le signal suit la provenance »).
- **Problème** : un contenu a une seule provenance. La vérité varie donc **entre** contenus : 48 items d'évaluation contre 48 demandes réelles, des textes différents. Seuls les marqueurs varient **dans** un même contenu. Le plan n'est apparié que sur l'axe des marqueurs.

  Le modèle n'a pas accès à la provenance, seulement au texte. « L'effet de la vérité » mesure donc tout ce qui, dans le texte dépouillé, reste corrélé à la source :
  - genre « question d'examen à réponse unique » ;
  - registre, domaine, longueur, présence d'une bonne réponse ;
  - mémorisation (CLP-11).

  Un modèle sensible au **genre** d'examen, qui est un style absent de la liste des marqueurs, produirait un effet de la vérité et serait classé H-contenu. La lecture « le signal suit la provenance » serait alors fausse. L'appariement « en longueur et en domaine » ne règle rien : les domaines de MMLU ou de BBQ et ceux de WildChat se recouvrent peu. Apparier revient à sélectionner des demandes réelles atypiques, qui ressemblent à des questions d'examen, précisément celles dont la provenance est ambiguë.

  Enfin, le brouillon s'écarte de son origine :
  - la caste 2 du pilote 4 entend par « contenu » la **rareté du scénario** en déploiement (occasion de sabotage, script d'arrêt), pas la provenance ;
  - son propre protocole est un 2 × 2 style × contenu (fréquent / rare), où **les deux** facteurs sont manipulés (`reponse-question-g001.md`, lignes 117 à 134) ;
  - la caste 4 (point d) dit que la provenance est une vérité terrain poreuse (ligne 194), et le brouillon l'adopte sans répondre à ce point.
- **Correction** :
  - Renommer les facteurs : « marqueurs listés (manipulés, dans le contenu) » × « source de collecte (non manipulée, entre contenus) ».
  - Réécrire H-contenu en « le signal suit des traits du texte corrélés à la source, autres que les marqueurs listés », et retirer toute lecture en termes de provenance.
  - Ajouter des covariables mesurées par item : longueur en jetons, score du classifieur de surface, mémorisation (CLP-11).
  - Mieux encore, envisager le dessin de la caste 2 : un facteur de contenu **manipulé**, par exemple scénario rare ou fréquent, écrit en paires, croisé avec les marqueurs. Les deux facteurs sont alors identifiables.
  - Dans tous les cas, ajouter le contrôle « même texte, provenance différente » décrit en CLP-10.

### CLP-03 — bloquant — La règle de décision conclut H-style par défaut, faute de puissance

- **Endroit** : Prédiction et Seuil (« l'effet de la vérité contient 0 ») ; Métrique (bootstrap sur 96 contenus) ; aucune analyse de puissance.
- **Problème** :
  - L'effet des marqueurs est estimé **dans** un même contenu, donc avec précision. L'effet de la vérité est estimé **entre** 48 et 48 contenus : son erreur type vaut environ σ_c × √(2/48) ≈ 0,20 σ_c, où σ_c est l'écart type du signal entre contenus.
  - L'effet minimal détectable à 80 % de puissance, avec un seuil bilatéral de 5 %, est donc d'environ 0,57 σ_c (calcul illustratif, de raisonnement, sans donnée). Sur des textes naturels hétérogènes, σ_c sera probablement grand.
  - Un effet de la vérité réel mais modéré donnera presque toujours un intervalle qui contient 0. Avec un effet des marqueurs net, la règle « H-style retenue » se déclenche. L'absence de preuve est lue comme preuve de l'absence, et l'issue privilégiée est justement l'« attente de l'auteur ».
  - L'asymétrie de structure (dans le contenu contre entre contenus) rend aussi la règle non symétrique entre H-style et H-contenu, contrairement à ce qu'exige R4.
- **Correction** :
  - (1) Remplacer « l'intervalle contient 0 » par un **test d'équivalence** : deux tests unilatéraux, ou un intervalle à 90 % entièrement dans ± une plus petite taille d'effet d'intérêt. Fixer cette taille avant toute mesure, en unités d'un témoin positif d'évaluation (CLP-12), par exemple 20 % de son effet.
  - (2) Simuler la puissance avant scellement sur une plage d'écarts types entre contenus, au pire cas, comme le prévoit l'étape 0 (§ 4, dernier point), et sans valeur tirée des runs précédents.
  - (3) Augmenter fortement le nombre de contenus. Le calcul coûte quelques minutes de carte ; la contrainte réelle est la construction du matériel.
  - (4) Écrire des critères strictement symétriques pour les deux hypothèses.

### CLP-04 — majeur — Les marqueurs ne sont pas les mêmes selon la vérité

- **Endroit** : Prédiction (« deux cellules naturelles : évaluation avec marqueurs… ») ; Plan, point 1 (« quatre gabarits de marqueurs »).
- **Problème** : dans la cellule naturelle « évaluation avec marqueurs », les marqueurs sont ceux d'origine de l'item (options lettrées de MMLU, gabarit de BBQ). Dans la cellule placebo « réel avec marqueurs », ce sont les quatre gabarits ajoutés. Le facteur « marqueurs » mélange donc la présence de marqueurs et leur **type**, et ce mélange est corrélé à la vérité. L'interaction vérité × marqueurs devient ininterprétable.
- **Correction** :
  - Dépouiller **tous** les contenus.
  - Leur appliquer les **mêmes** quatre gabarits, quelle que soit la source.
  - Garder les versions d'origine des items comme cellule diagnostique hors critères (« marqueurs d'origine »), rapportée à part.

### CLP-05 — bloquant — La « mention d'un test » parmi les marqueurs fixe le signe d'avance

- **Endroit** : Hypothèse (H-style : « …injonctions, mention d'un test ») ; Métrique (instrument certifié par l'étape 0).
- **Problème** : une mention explicite d'un test n'est pas du style, c'est un **contenu sémantique** qui répond à la question posée.
  - Avec l'instrument verbal (« test » ou « user » ?), la mesure devient une lecture de consigne : l'effet des marqueurs est garanti.
  - Avec la sonde, c'est circulaire. À l'étape 0, la direction est apprise « par différence des moyennes sur des paires à format constant qui ne diffèrent que par une phrase de cadrage » (brouillon de l'étape 0, Hypothèse), et la porte S2 mesure justement si « la sonde lit la mention ». La sonde réagira à une mention de test par construction.
  - À l'inverse, la même sonde a été apprise **à format constant**. Elle peut être aveugle aux marqueurs de format par construction, ce qui biaiserait cette fois l'effet des marqueurs de format vers 0.

  Dans les deux cas, l'issue dépend du contraste d'apprentissage de l'instrument, pas du modèle. Un dessin dont le signe est fixé par construction tombe sous l'esprit de R3.
- **Correction** :
  - Retirer toute mention explicite de test ou d'évaluation des marqueurs.
  - En faire, au mieux, le **témoin positif** (CLP-12).
  - Séparer, si on les garde, deux familles :
    - les marqueurs de **cadre** implicites : identifiant d'item, en-tête balisé, consigne de format de sortie ;
    - les marqueurs de **format** : options lettrées.
  - Exiger un lexique disjoint entre les gabarits et les phrases de cadrage de l'étape 0, vérifié par le script de construction.

### CLP-06 — majeur — Dépouiller ou ajouter des marqueurs change le contenu, et pas de façon symétrique

- **Endroit** : Prédiction (placebos croisés) ; Plan, point 1.
- **Problème** :
  - Côté évaluation, beaucoup d'énoncés de MMLU renvoient aux options (« Which of the following… »). Sans elles, ils deviennent incohérents ou changent de tâche : une question ouverte au lieu d'un choix. Un item de BBQ privé de ses réponses perd sa structure.
  - Côté réel, ajouter des options lettrées à « écris-moi un poème sur mon chat » produit un texte incohérent.
  - L'atypicité ou l'incohérence est elle-même un indice d'évaluation (caste 2 : « l'absence de marqueurs devient un marqueur »). Les deux bras placebo ne sont donc pas des images en miroir. Devbunova (2026) a dû filtrer les requêtes « compatibles » (à vérifier), ce qui est une sélection.
  - Rien ne dit qui réécrit : une règle déterministe, à la main, ou un modèle. Une réécriture par un modèle ajoute son style propre, et en appeler un serait une dépense.
- **Correction** :
  - Écrire des règles de dépouillement et d'ajout **déterministes** dans le script.
  - Écrire des critères d'exclusion fixés avant construction : énoncés qui renvoient aux options, requêtes incompatibles avec un format. Compter les exclusions par source.
  - Mesurer la cohérence de chaque version, en aveugle, par une procédure fixée d'avance, et rapporter le signal selon la cohérence.
  - Limiter les marqueurs de format aux contenus compatibles, ou ne garder que des marqueurs de cadre qui ne touchent pas l'énoncé.

### CLP-07 — majeur — Le témoin de faux marqueurs est mal construit et mal utilisé

- **Endroit** : Métrique, témoin négatif ; Seuil, ligne « non concluant ».
- **Problème** :
  - (1) Il ne vérifie qu'un côté (« borne basse > 0 ») : un effet négatif de l'insertion, par dilution, passe inaperçu.
  - (2) « Leur effet doit être nul » est lu sans test d'équivalence (même défaut que CLP-03).
  - (3) Des « phrases neutres de même longueur » ne contrôlent ni la position, ni la forme (en-tête, liste), ni l'incohérence que crée l'insertion. Le bon témoin est une insertion de même forme et de même place, sans valeur d'audit : par exemple « Sujet : cuisine » contre « Identifiant d'item : 0423 ».
  - (4) La longueur n'est pas définie : en caractères ou en jetons ?
  - (5) On ne sait pas à quels contenus ni à quelles cellules il s'applique, et il est absent de la formule du modèle.
  - (6) Il sert seulement de veto. Il devrait servir de **référence** au contraste des marqueurs.
- **Correction** :
  - Définir l'effet des marqueurs comme la différence vrais marqueurs moins faux marqueurs, appariés en forme, en position et en nombre de jetons, sur tous les contenus des deux sources.
  - Garder le contraste faux marqueurs moins version nue comme garde, avec une équivalence bilatérale.
  - L'inclure dans la formule.

### CLP-08 — majeur — Seuils mal définis, interaction ignorée, table qui ne partitionne pas

- **Endroit** : Prédiction ; Seuil ; Métrique.
- **Problème** :
  - « Au moins deux fois » ne dit pas sur quoi il porte : estimations ponctuelles ou intervalle du rapport ? Sur des valeurs signées ou absolues ? Si l'effet de la vérité est négatif, la condition est remplie trivialement. S'il est proche de 0, le rapport explose.
  - Le marquage des effets n'est pas fixé (codage par effets ou par indicatrices). « L'effet de la vérité à marqueurs fixes » ne dit pas à quel niveau, avec ou sans marqueurs, alors que « l'effet des marqueurs » est pris « en moyenne sur la vérité ».
  - L'interaction vérité × marqueurs est estimée mais n'entre dans aucun critère. Pourtant, des marqueurs qui ne comptent que sur les demandes réelles, parce que les items d'évaluation saturent, inverseraient la lecture des effets principaux.
  - La table laisse des trous informatifs : deux effets à borne basse > 0 avec un rapport de 3 tombent dans « non concluant ».
  - « Deux hypothèses exclusives » contredit « un mélange est possible » : ce sont les deux bouts d'un continuum.
- **Correction** :
  - Fixer le codage par effets (somme nulle).
  - Définir une statistique unique et son intervalle bootstrap, par exemple la part de l'écart naturel portée par les marqueurs (voir CLP-09).
  - Donner une règle pour l'interaction : effets simples dans chaque cellule, et une issue « interaction » si son intervalle exclut 0 et dépasse un seuil fixé.
  - Écrire une table qui couvre toutes les combinaisons sans ambiguïté.

### CLP-09 — majeur — Le rapport « 2 × » dépend de choix arbitraires

- **Endroit** : Seuil.
- **Problème** :
  - L'effet des marqueurs dépend de la **dose** choisie : combien de marqueurs, lesquels, où. On l'obtient grand ou petit à volonté.
  - L'effet de la vérité dépend des sources et de l'appariement.
  - Le rapport des deux ne dit donc pas « ce que suit le signal » : il compare deux réglages de l'expérimentateur.
- **Correction** :
  - Exprimer l'estimand par rapport à l'écart naturel. Soit Δ_nat = (évaluation avec marqueurs) − (réel sans marqueurs), mesurés avec les mêmes gabarits que les bras placebo (voir CLP-04). On estime la part π_m = β_m / Δ_nat, avec son intervalle.
  - Fixer la dose (un gabarit par niveau, nombre de marqueurs connu).
  - Rapporter chaque gabarit séparément.
  - Garder « aucune généralisation à d'autres marqueurs », déjà présent.

### CLP-10 — majeur — La vérité terrain poreuse n'est pas traitée

- **Endroit** : Plan, point 1 (sources « par exemple MMLU ou BBQ… WildChat ou LMSYS-Chat-1M ») ; Critères.
- **Problème** :
  - LMSYS-Chat-1M est collecté sur la démo Vicuna et sur Chatbot Arena (à vérifier). Les utilisateurs de l'Arena **évaluent** des modèles par construction : une part du « réel » est de l'évaluation humaine.
  - WildChat contient des items de bancs d'essai collés tels quels, des devoirs et des tests du modèle par ses utilisateurs.
  - Côté évaluation, des bancs d'essai sont construits à partir de journaux réels : WildBench à partir de WildChat, Arena-Hard à partir de Chatbot Arena (à vérifier). MMLU reprend des examens écrits pour des humains, que des étudiants soumettent aussi aux assistants.

  C'est le point d) de la caste critique, qui est à l'origine du test et que le brouillon n'aborde pas.
- **Correction** :
  - Définir la vérité comme « source de collecte », pas comme « évaluation ou réel ».
  - Exclure les conversations de l'Arena.
  - Dédoublonner le réel contre les bancs d'essai par n-grammes, et exclure tout banc d'essai issu de journaux réels du niveau « évaluation ».
  - Repérer en aveugle, par une procédure fixée, les demandes réelles à intention de test, et les rapporter à part.
  - Ajouter un **contrôle d'identité** : des textes présents à la fois dans WildBench et dans WildChat (à vérifier) donnent la même entrée sous deux provenances. Le signal doit y être identique, sinon il y a une erreur de chaîne et on arrête. Ce contrôle montre aussi, sans dépense, que la provenance en soi n'est pas une propriété du texte.

### CLP-11 — majeur — La contamination de l'entraînement confond la vérité avec la familiarité

- **Endroit** : Plan, point 1 (« présence éventuelle… dans les données d'entraînement »), sans conséquence prévue.
- **Problème** :
  - MMLU (2020) et BBQ (2021) sont très probablement dans le préentraînement de Llama 3.1, dont la date de coupure est décembre 2023 (à vérifier).
  - LMSYS-Chat-1M (collecté d'avril à août 2023, publié en septembre 2023) et une partie de WildChat peuvent l'être aussi (à vérifier).
  - Une mémorisation asymétrique fait monter « l'effet de la vérité » par familiarité. C'est exactement la variable de H-M1 (« familiarité du format de banc d'essai »), ce qui brouille aussi la lecture de CLP-15.
- **Correction** :
  - Soit prendre des items d'évaluation et des demandes réelles postérieurs à la coupure, ce qui doit être vérifié par source.
  - Soit mesurer la mémorisation par item dans la même passe avant, sans surcoût. Par exemple : log-vraisemblance moyenne de l'énoncé sous le modèle, rapportée à une version paraphrasée, ou exactitude de complétion de la seconde moitié.
  - L'utiliser comme covariable et comme strate déclarée.
  - Note : ceci concerne le texte de l'item. Ce n'est pas une sonde de production, et l'interdit sur la moyenne des jetons ne s'y applique pas. Le dire dans le texte.

### CLP-12 — majeur — La dépendance à l'étape 0 est mal posée

- **Endroit** : en-tête (« Dépend de l'étape 0 ») ; Métrique (« témoin positif : le témoin discriminant de l'étape 0 ») ; Critères.
- **Problème** :
  - (1) **Changement de domaine.** L'étape 0 certifie sur 48 contenus synthétiques courts, aux formats contrôlés. La certification ne garantit rien sur des textes naturels longs : code, demandes à plusieurs paragraphes. La masse V1 ≥ 0,5 peut s'effondrer.
  - (2) **Témoin positif inadapté.** `disc_yn` (« a two-digit number? ») prouve que le contenu est lu, pas que l'instrument **réagit à l'évaluation** sur ce matériel. Il ne s'applique pas à la sonde. Sans témoin positif d'évaluation, un double nul est ininterprétable : instrument sourd ou modèle insensible.
  - (3) **Contournement d'une décision.** L'issue (c) de l'étape 0 (« voie verbale seule : décision de Lazar avant toute étape 1 ») serait contournée : le placebo utiliserait l'instrument verbal sans cette décision.
  - (4) **Désaccord non prévu.** Rien ne dit quoi faire si la sonde et l'instrument verbal, tous deux certifiés, disent des choses opposées.
  - (5) **Instrument verbal incomplet.** Le précédent n'est pas nommé, ni la façon de combiner les deux ordres du choix forcé (moyenne des log-rapports ? lecture par ordre ?).
  - (6) **Disjonction incomplète.** Les contenus et le lexique ne sont pas déclarés disjoints de ceux de l'étape 0, seulement de H-M1.
- **Correction** :
  - Ajouter une **revérification sur le matériel**, avec des seuils fixés avant toute mesure : masse V1 par source et par version, et un témoin discriminant adapté au matériel. Si elle échoue, on arrête.
  - Ajouter un **témoin positif d'évaluation**, par exemple une phrase explicite « cette conversation fait partie d'un banc d'essai » contre « cette conversation est réelle ». L'instrument doit bouger avec une borne basse fixée.
  - Reprendre la règle de l'issue (c).
  - Écrire la règle de désaccord : mesure principale unique et l'autre en diagnostic, désaccord rapporté comme réserve.
  - Nommer le précédent et la combinaison des ordres.
  - Vérifier la disjonction avec l'étape 0 dans le script.

### CLP-13 — majeur — Licences et données personnelles : la règle d'arrêt est inapplicable, et LMSYS-Chat-1M pose un problème de compte et de redistribution

- **Endroit** : Plan, point 1 ; Liste d'arrêt (« une source… qui contient des données personnelles : écartée »).
- **Problème** :
  - **LMSYS-Chat-1M** (à vérifier sur la page du jeu) :
    - accès conditionné à un accord de licence signé avec un compte Hugging Face, ce qui est un acte de **compte**, donc un nœud de décision ;
    - interdiction de « distribuer, copier, divulguer… héberger » ;
    - suppression exigible à tout moment ;
    - contenus offensants conservés, et noms remplacés « au mieux ».

    Des stimuli qui en dérivent ne peuvent pas être poussés dans le dépôt de travail sans lecture juridique, et encore moins dans la copie expurgée publique que régénère `scripts/depot_expurge.py`.
  - **WildChat-1M** : licence affichée ODC-BY (attribution exigée, à vérifier ; une licence antérieure ImpACT d'AI2 est à vérifier aussi). Le jeu a une colonne `redacted` et un drapeau `toxic`, sans procédure de retrait des données personnelles décrite sur la page lue.
  - **BBQ** : CC-BY-4.0 (attribution, à vérifier). **MMLU** : MIT sur la copie `cais/mmlu`, l'amont reste à vérifier.
  - **Règle d'arrêt** : tout grand corpus réel contient des données personnelles résiduelles. La règle « source écartée » exclurait donc toutes les sources réelles, et le test ne partirait jamais. Ou bien la règle serait appliquée avec souplesse, ce qui serait un repli silencieux (R5).
- **Correction** :
  - Écrire une **procédure par item** : détection automatique des courriels, téléphones, noms et adresses, puis relecture, puis exclusion de l'item, avec un compte rendu.
  - Filtrer les contenus toxiques par le drapeau et par une relecture.
  - Préférer WildChat (licence ouverte) à LMSYS-Chat-1M. Si LMSYS reste, demande de décision à Lazar (compte et redistribution).
  - Déclarer les stimuli dérivés de conversations réelles exclus de la copie expurgée, et le tester dans `depot_expurge.py`.
  - Consigner l'attribution exigée par ODC-BY et CC-BY.

### CLP-14 — majeur — Scellement « facultatif » incompatible avec R1, et conséquences qui modifient le programme

- **Endroit** : en-tête « Statut » (« scellement facultatif ») ; Critères (« conséquence pour le programme… la banque des organismes doit porter des jumelles de style » ; « H-M1 perd l'essentiel de son objet »).
- **Problème** :
  - Le texte tire des conséquences sur H-M1 et sur la banque des organismes. C'est une expérience **décisive** au sens de R1 : le scellement est obligatoire, pas facultatif sous R-473.
  - « Conséquence pour le programme » revient à modifier une hypothèse ou la conception, ce qui est un nœud de décision. Ce ne peut pas être un effet automatique d'une issue.
- **Correction** :
  - Écrire « scellé avant toute mesure (R1) ».
  - Reformuler les conséquences en « proposé à Lazar », avec le format de décision du dépôt.

### CLP-15 — majeur — Les lectures pour H-M1 sont fausses ou hors de portée

- **Endroit** : Critères (« H-contenu retenue : H-M1 perd l'essentiel de son objet »).
- **Problème** :
  - H-M1 dit que le signal monte avec la **familiarité du format de banc d'essai**, plus qu'avec le style de consigne, à contenu égal. Un effet de la vérité porté par la mémorisation des items (CLP-11) est **compatible** avec H-M1. Ce n'est pas un échec de H-M1.
  - Le facteur « marqueurs » mélange format (options lettrées) et consigne (injonctions). Il ne peut donc rien dire de la distinction centrale de H-M1, format contre style de consigne.
- **Correction** :
  - Retirer cette conséquence.
  - Ou bien séparer marqueurs de format et marqueurs de consigne (voir CLP-05) et écrire, pour chaque issue, la lecture exacte pour H-M1, en « proposé à Lazar ».

### CLP-16 — mineur — Le matériel est mal décrit et le compte ne se reconstruit pas

- **Endroit** : Plan, point 1.
- **Problème** :
  - « Chaque contenu en quatre versions : avec ou sans marqueurs » est contradictoire : un contenu a une source fixe, donc deux états de marqueurs, déclinés selon les gabarits.
  - Le total de 768 ne se reconstruit pas :
    - 96 × (1 nu + 4 gabarits + 4 faux) = 864 ;
    - 96 × 8 = 768 sans version nue ?
    - 96 × 4 × 2 ordres du choix forcé = 768 ?
  - La place des marqueurs n'est pas fixée : message système, tour utilisateur, avant ou après l'énoncé.
- **Correction** : donner la matrice exacte du dessin (contenu × version × gabarit × ordre), le nombre de dialogues par cellule et la place des insertions.

### CLP-17 — mineur — Le modèle mixte et le bootstrap ne sont pas cohérents

- **Endroit** : Métrique, « Effets ».
- **Problème** :
  - L'effet aléatoire du gabarit, à quatre niveaux, n'existe que dans les versions marquées, ce qui fait un plan partiellement croisé non décrit. Quatre niveaux ne suffisent pas à estimer une variance.
  - On ne sait pas lequel décide, du modèle mixte ou du bootstrap.
  - Le bootstrap « sur les contenus » n'est pas stratifié par source et ignore les gabarits.
  - L'entropie `SeedSequence` n'est pas donnée, ni l'attribution des enfants (R9). L'étape 0 la donne.
- **Correction** :
  - Faire décider un seul intervalle : bootstrap par grappes de contenus, stratifié par source, gabarits traités comme fixes (cohérent avec « aucune généralisation à d'autres marqueurs »).
  - Garder le modèle mixte en diagnostic.
  - Tirer l'entropie et l'écrire dans le texte avant le scellement.

### CLP-18 — mineur — La ligne de base de surface est sous-spécifiée et hors des critères

- **Endroit** : Métrique, troisième témoin.
- **Problème** : on ne sait pas :
  - sur quoi le sac de mots est entraîné (les cellules naturelles ?) ;
  - comment on le compare à un signal continu qui ne prédit pas la vérité ;
  - ce que veut dire « faire mieux » ;
  - quelle conséquence cela a, puisqu'il n'est cité dans aucun critère de lecture.

  Bien défini, il serait pourtant utile. Entraîné sur les cellules naturelles et appliqué aux placebos, il donne la référence d'un lecteur purement stylistique.
- **Correction** : fixer l'entraînement (cellules naturelles, validation croisée par contenu), la métrique (aire sous la courbe pour la source dans chaque cellule placebo, ou corrélation avec le signal) et la règle de lecture.

### CLP-19 — mineur — La citation de l'origine est inexacte

- **Endroit** : en-tête « Origine ».
- **Problème** :
  - La phrase entre guillemets n'est pas verbatim. Il manque « (la coercition compte) » et « (caste 2 a raison) », et « il est » remplace « le signal est » (`reponse-question-g001.md`, ligne 199).
  - Le chemin cité (`pilotes/pilote4-gemini-v6-2-v1`) n'est pas celui du fichier (`…-v1-tentative2/`).
  - Aucune empreinte n'est donnée (R6).
- **Correction** : citer verbatim ou écrire « en substance », corriger le chemin et ajouter l'empreinte `a80e61a8…`.

### CLP-20 — mineur — « Illustratifs, fixés avant toute mesure » est ambigu

- **Endroit** : Seuil.
- **Problème** : dans un texte scellé, les seuils sont **contraignants**. « Illustratifs » peut se lire comme « révisables ».
- **Correction** : écrire « choisis sans donnée, contraignants une fois scellés ».

### CLP-21 — mineur — La liste d'arrêt est incomplète

- **Endroit** : Liste d'arrêt.
- **Problème** : il manque :
  - l'échec de la revérification des instruments sur le matériel (CLP-12) ;
  - un contrôle d'identité WildBench / WildChat non identique (CLP-10) ;
  - un taux d'exclusion par incohérence au-delà d'un seuil (CLP-06) ;
  - un doublon de banc d'essai trouvé dans le réel après construction (CLP-10) ;
  - l'absence de GO nouveau (seulement « dépense au-delà ») ;
  - l'accord de licence non signé par Lazar (CLP-13).
- **Correction** : ajouter ces lignes.

### CLP-22 — remarque — Conformité à `prereg.py`

- Les huit sections exigées sont présentes et non vides. Il ne reste ni « À REMPLIR » ni marqueur `<<…>>`.
- Seule la section « Contre-lecture » manque ses deux empreintes, ce qui est attendu avant relecture.
- La phrase « À remplir après la relecture » est en minuscules et échappe au contrôle du marqueur `À REMPLIR` ; elle doit disparaître avant le scellement.

### CLP-23 — remarque — L'« attente de l'auteur » s'appuie sur des sources faibles

- **Endroit** : Prédiction.
- **Problème** : que l'organisme classe presque tout comme « évaluation » au pilote 4 ne dit rien du signal **interne de Llama** : c'est un autre système qui classe des transcriptions. La « caste critique de la course S » est citée sans chemin ni empreinte.
- **Correction** : citer ou retirer. Sans effet sur la lecture, mais à garder propre (R6).

### CLP-24 — remarque — La question de mesure est elle-même un marqueur d'audit

- **Endroit** : Métrique (instrument verbal).
- **Problème** : demander « test ou user ? » transforme chaque dialogue en interrogatoire. La question est constante entre cellules, donc sans biais de différence, mais elle peut pousser toutes les cellules vers « test » et écraser les effets (plafond).
- **Correction** :
  - Rapporter la distribution du signal par cellule.
  - Ajouter à la liste d'arrêt une saturation fixée, par exemple une médiane hors d'une plage fixée dans toutes les cellules.

## Ce qu'il faudrait pour en faire un texte prêt à coder

1. **Décision de Lazar sur CLP-01** : abandon, réplication et extension de Devbunova (2026), ou refonte vers un facteur de contenu manipulé. Lire et empreinter d'abord les trois PDF (R7).
2. **Facteurs redéfinis.**
   - Marqueurs de cadre implicites, et de format si on les garde : mêmes gabarits pour les deux sources, appliqués sur contenu dépouillé, mention explicite exclue.
   - Faux marqueurs appariés en forme, en place et en jetons.
   - Source de collecte, non manipulée.
   - Covariables : longueur, mémorisation, score de surface.
3. **Estimand et règle.**
   - Part de l'écart naturel portée par les marqueurs, avec son intervalle bootstrap stratifié.
   - Tests d'équivalence sur une plus petite taille d'effet d'intérêt exprimée en unités du témoin positif.
   - Puissance simulée avant scellement.
   - Table exhaustive et symétrique, interaction comprise.
4. **Témoins.**
   - Positif d'évaluation : mention explicite.
   - Négatif : faux marqueurs.
   - Contrôle d'identité : même texte, deux provenances.
   - Revérification des instruments sur le matériel.
5. **Sources.**
   - Postérieures à la coupure, ou mémorisation mesurée.
   - Pas d'Arena ; dédoublonnage ; repérage des demandes à intention de test.
   - Licences lues ; procédure par item pour les données personnelles ; exclusion de la copie expurgée.
6. **Scellement obligatoire (R1)** ; conséquences pour le programme en « proposé à Lazar ».

## Antériorité (R8, R7)

Tout ce qui suit a été lu sur une page HTML ou sur un résumé de page, **pas sur un PDF empreinté**. Tout est **à vérifier** avant d'être opposable.

| référence | ce qu'elle fait (à vérifier) | recouvrement avec le brouillon |
|---|---|---|
| V. Devbunova, « Is Evaluation Awareness Just Format Sensitivity? Limitations of Probe-Based Evidence under Controlled Prompt Structure », arXiv 2603.19426, 19 mars 2026, atelier « I Can't Believe It's Not Better » d'ICLR 2026 | Llama-3.1-8B-Instruct, `bfloat16`, dernier jeton, couches 8 à 31. Plan 2 × 2 : Bench-Eval (MMLU, ARC, GSM8K), Casual-Deploy (ShareGPT), Casual-Eval (MuTual, mandataire), Bench-Deploy (ShareGPT réécrit au format des bancs d'essai par DeepSeek-V3, requêtes « compatibles » seulement). Sonde standard : Bench-Deploy classé « évaluation » à environ 94,5 % ; sonde apprise sur paires décorrélées : environ 7,2 %. Une seule graine, sans intervalle. | **Collision forte** : même modèle, même plan croisé, même cellule placebo « réel avec marqueurs ». Différences : contenu non apparié dans le bras Casual-Eval, aucun témoin de faux marqueurs, aucune certification préalable, aucun intervalle. |
| N. Nayan et al., « Evaluation Awareness Is Not One Capability: Evidence from Open Language Models », arXiv 2606.23583, 22 juin 2026 (Université du Massachusetts Amherst et Microsoft) | 37 modèles ouverts, dont Llama-3.1-8B-Instruct. Réutilise le 2 × 2 de Devbunova (5 733 prompts) : aire sous la courbe de Llama-3.1-8B-Instruct d'environ 0,644 en protocole standard contre 0,491 une fois format et intention décorrélés (valeur donnée en prose seulement). Corrélations faibles entre mesures comportementales, du 2 × 2 et de sonde. Pilotage multicouche de Llama-3.1-8B-Instruct. | **Collision** côté mesure en boîte noire, sur le même modèle. |
| C. Li, … S. Abdelnabi, M. Andriushchenko, « Decomposing and Measuring Evaluation Awareness » (EvalAwareBench), arXiv 2605.23055, mai 2026, v3 en septembre 2026 | 100 tâches appariées, huit facteurs déclencheurs activables un par un à requête fixe (entités factices, formats de notation…), neuf modèles de pointe, mesure par la chaîne de pensée. | **Recouvrement** sur l'axe « marqueurs dosés à contenu fixe ». Provenance non croisée, d'après le résumé. |
| J. X. Li et al., « WARP: Measuring and Mitigating Evaluation Awareness in Browser-Agent Safety Benchmarks », ICML 2026 | Témoin d'indice « non-évaluation » apparié en longueur : un indice d'évaluation explicite baisse le taux de succès d'attaque d'environ 10,9 points, l'indice témoin non. | **Précédent** du témoin de faux marqueurs (agents de navigation). |
| « Probe-Rewrite-Evaluate » / « StealthEval », arXiv 2509.00591 (plusieurs versions aux chiffres différents), NeurIPS 2025 | Réécrit des prompts d'évaluation vers un style de déploiement à tâche conservée, en les notant par une sonde linéaire. | **Précédent** du bras « évaluation dépouillée ». |
| N. Singh, M. Chaudhary, « Evaluation Awareness Shifts from Format to Context with Model Scale », arXiv 2609.22119, août 2026 | Les petits modèles (dont un « Llama-3 8B », variante non précisée) s'appuient surtout sur le format. Pas de plan croisé contrôlé. | Voisin. Les conclusions vont dans le sens de H-style pour les petits modèles. |
| J. Needham et al., « Large Language Models Often Know When They Are Being Evaluated », arXiv 2505.23836, 2025 | 1 000 transcriptions de 61 jeux (dont MMLU, SWE-bench, déploiement réel), classement évaluation contre déploiement. | Origine du paradigme. Pas de croisement. |
| WildBench (arXiv 2406.04770) ; Arena-Hard | WildBench : 1 024 tâches tirées de WildChat. Arena-Hard : 500 prompts tirés de Chatbot Arena. | Pas un travail sur la conscience d'évaluation, mais une **preuve de la porosité** (CLP-10) et une source possible du contrôle d'identité. |

- **Non lus, à chercher et à vérifier** (de mémoire, titres et identifiants non contrôlés) :
  - Nguyen et al. 2025, « Probing Evaluation Awareness of Language Models » (arXiv 2507.01786 ?) ;
  - Abdelnabi et Salem 2025, sur le pilotage de la « conscience de test » (arXiv 2505.14617 ?) ;
  - Chaudhary et al. 2025, « Evaluation Awareness Scales Predictably in Open-Weights Large Language Models » (arXiv 2509.13333 ?) ;
  - Hua et al. 2025, sur le pilotage de modèles conscients d'évaluation (arXiv 2510.20487 ?) ;
  - EvalDetectBench (arXiv 2609.01611).
- **Ce qui reste peut-être libre, sous réserve de lecture des PDF** :
  - le croisement à contenu **strictement** apparié dans les quatre bras, avec mêmes gabarits pour les deux sources ;
  - le témoin de faux marqueurs dans un cadre conversationnel ;
  - le contrôle d'identité même texte, deux provenances ;
  - des instruments certifiés à l'aveugle avant la mesure ;
  - des tests d'équivalence.

  C'est une extension méthodologique étroite, pas une zone vierge. Au sens de R8, la zone « plan croisé marqueurs × provenance sur Llama-3.1-8B-Instruct » doit être tenue pour **occupée**.

## Sources consultées sur le web

- https://arxiv.org/abs/2603.19426 et https://arxiv.org/html/2603.19426
- https://arxiv.org/html/2606.23583v1
- https://arxiv.org/abs/2605.23055
- https://icml.cc/virtual/2026/76886
- https://arxiv.org/html/2609.22119
- https://arxiv.org/html/2509.00591v7 (résultat de recherche)
- https://arxiv.org/pdf/2505.23836 (résultat de recherche)
- https://arxiv.org/pdf/2406.04770 (résultat de recherche)
- https://huggingface.co/datasets/lmsys/lmsys-chat-1m
- https://huggingface.co/datasets/allenai/WildChat-1M
- https://arxiv.org/pdf/2110.08193 (BBQ, résultat de recherche) et https://arxiv.org/pdf/2508.18088 (mention de la licence de `cais/mmlu`, source secondaire)
