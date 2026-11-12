# Proposition B — Tour III.2 : critique croisée de méthode

**Pièces reçues.** A, D, E sont présentes et analysées ci-dessous. C est absente (déclaré par l'arbitre). Les pièces transmises sont des conceptions non scellées ; je les traite comme **RAPPORTÉES**. Mes lectures critiques sont des **HYPOTHÈSES** sauf mention contraire. Tout chiffre que j'avance est marqué **illustratif** s'il ne vient pas des faits.

---

## Sur la proposition A

### (a) Défauts de méthode

**1. D1 confond « entrée gelée » et « non-influence ».** A propose un audit mécanique (D1) qui classe chaque entrée de l'étape A de T0.7 en « gelée par le texte », « lue au registre » ou « décidée par un humain après scellement ». Si aucune entrée n'est de la troisième classe, A conclut que l'antériorité à protéger est `SCELLEMENT-T07 < VERDICT-P3BIS` plutôt que `SCORES-T07 < VERDICT-P3BIS`, et fonde sur ce résultat la recommandation (b′). Or le classement « zéro entrée humaine » ne couvre pas le canal pertinent : la décision de **lancer** 7b elle-même, de la **relancer** après un arrêt, ou de la **différer** indéfiniment est humaine et postérieure au scellement de T0.7. Cette décision conditionne l'existence même de `SCORES-T07`. Si le résultat de P3-bis est connu (« non vu »), Lazar pourrait retarder 7b, réparer la chaîne puis relancer — ce qui n'est pas une entrée de l'étape A, mais une décision sur la tenue de l'étape A. Le duel D1 est donc **vrai par construction** pour la question qu'il pose, et **muet** sur la question qui motive la garde.

**2. (b′) crée une circularité temporelle non testée.** A exige que `SCELLEMENT-T07` précède `VERDICT-P3BIS`, puis propose que T0.7 b15 supprime le refus de l'étape A après `VERDICT-P3BIS`. Mais T0.7 b15 serait écrit après que (b′) ait été adoptée — et son contenu serait donc conditionné par le choix (b′). Cela revient à réécrire la règle pour justifier son propre assouplissement, sans qu'aucune expérience ne puisse falsifier cette circularité. R12 autorise une version nouvelle, mais ne dispense pas de montrer que le nouveau texte protège ce que l'ancien protégeait.

**3. L'argument « un ‹ non vu › permet de réparer la chaîne avant 7b » (section recommandation, dernier paragraphe) confond l'utilité d'un signal précoce avec la neutralité de ce signal sur T0.7.** Si « non vu » est connu avant le scellement de T0.7, le choix de réparer la chaîne *avant* de sceller T0.7 est lui-même une influence sur T0.7, même si aucune entrée gelée de l'étape A ne change : le texte de T0.7 pourrait être amendé pour anticiper le « non vu ». L'argument de A suppose implicitement que T0.7 est déjà scellé au moment où « non vu » arrive, ce qui est incompatible avec la condition « SCELLEMENT-T07 avant VERDICT-P3BIS ».

**4. E1 (collusion jouée contre consigne reçue) est un bon duel, mais sa variable confondante principale n'est pas nommée.** Le tri « propre / non propre » repose sur la règle d'audit réimplémentée (votes sur la cible, message privé, non `flagged`). Un épisode « non propre » peut l'être parce que le 8B a refusé de jouer, ou parce qu'il a mal joué (vote erroné, absence de privé). Ces deux causes ne produisent pas les mêmes activations : un refus explicite (« I cannot assist with deception ») est un texte très différent d'une tentative maladroite. Le contrôle négatif (honnêtes propres contre honnêtes non propres) ne couvre pas cette confusion : les honnêtes ne sont pas classés propre/non propre par la même règle.

**5. E2 : la cellule C1′ est sous-spécifiée.** A propose un texte de colludeur relu sous la consigne d'un **autre scénario** (même rôle, autre cible, longueur appariée à ± 5 %). Mais « longueur appariée à ± 5 % » est **illustratif** et ne contrôle pas la structure sémantique : la consigne d'un autre scénario peut porter un domaine, des noms et des rôles incompatibles avec le texte relu. Le score de C1′ pourrait alors diverger de C1 simplement parce que le modèle détecte une incohérence contexte-texte, sans rapport avec la consigne de collusion. Un contrôle négatif qui sépare « incohérence » de « absence de collusion » manque.

### (b) Conditions de perte de puissance ou de non-jugeabilité

| Mesure/critère | Condition de perte de puissance | Paramètre clé |
|---|---|---|
| E1, aire propre/non propre | Effectif du groupe « non propre » < 10 (reconnu par A). Mais aussi : si la proportion de propres est très élevée (> 0,95, **illustratif**), le groupe non propre est petit et l'intervalle par blocs dégénère (> 1 % de tirages à une seule classe). Le seuil de 0,2 de « non jouée » ne couvre pas ce cas intermédiaire. | n_non_propre, proportion de tirages dégénérés |
| E2, différence C1 − C2b appariée par scénario | Si la variance intra-scénario du score est grande relativement à l'effet de contexte, l'intervalle par blocs avec bloc = scénario sera large. Avec 50 scénarios CORE × 2 réplicats, le nombre de blocs est 50 ; un effet δ tel que δ/σ_bloc < 0,4 (**illustratif**) ne sera pas détecté à 80 % de puissance. | σ_bloc, δ_contexte, nombre de scénarios |
| C1′ comme contrôle | Si le domaine de l'autre scénario est identique (ex. deux scénarios « business strategy »), C1 − C1′ peut être petit par artefact de ressemblance, pas par absence d'effet de préfixe. La distribution des domaines dans le jeu conditionne la puissance du contrôle. | diversité inter-scénarios des domaines |
| D1 (audit mécanique) | A le présente comme un duel, mais il n'y a pas de distribution probabiliste : c'est un inventaire déterministe. La « puissance » est 1 ou 0 selon la complétude de la liste des entrées. Une entrée omise (ex. : la décision de lancer 7b) rend le duel vrai par construction sans falsifier l'hypothèse pertinente. | complétude de l'inventaire |

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Contrôle de position pour l'échange de consigne.** A reconnaît (section « condition de changement d'avis ») que si les consignes diffèrent de plus de 20 % en jetons, la relecture change surtout les positions. Mais ce contrôle n'est pas dans le plan d'analyse : il est dans une clause de sortie. Sans mesure systématique de l'écart de longueur consigne honnête / consigne de colludeur **avant** la lecture, on ne sait pas si le duel E2 est interprétable.

2. **Contrôle « même contexte, même texte, score identique ».** A le mentionne pour E2 (« contexte strictement identique ») mais ne précise pas le seuil de tolérance. Une égalité au bit près des identifiants ne garantit pas une égalité au bit près des scores si le contexte change la longueur du préfixe et donc le cache KV. Il faut que ce contrôle soit mesuré et qu'un écart non nul soit borné, sinon C1 − C2b inclut un bruit de relecture.

3. **Base de métadonnées (longueur, siège, tour).** A la propose, ce qui est bien. Mais elle n'est pas dans le brouillon de la pièce 3, et A ne dit pas si elle doit être gelée avant STEGO. Si elle est apprise après lecture de STEGO, la comparaison est biaisée.

---

## Sur la proposition D

### (a) Défauts de méthode

**1. La recommandation QO-1 (a avec « sortie humaine préspécifiée ») ne spécifie pas ce que Lazar décide *sur la base de quoi*.** D dit que Lazar « devrait pouvoir décider, par écrit, soit de poursuivre l'attente, soit d'abandonner T0.7 ». Mais sous (a), les lectures mécaniques sont faites et fermées. Lazar décide-t-il en voyant les codes de sortie et les comptes ? Si oui, ces métadonnées pourraient révéler indirectement une issue (ex. : un nombre élevé d'épisodes à score au-dessus du seuil visible dans `resume.json`). D reconnaît que les sorties autorisées pourraient révéler une issue (tableau des présupposés, ligne 2), mais ne transforme pas cette reconnaissance en contrôle concret.

**2. Le duel QO-A est une vérification d'implémentation, pas une expérience falsifiable au sens probabiliste.** La « métrique » est une matrice de scénarios synthétiques ; le « seuil » est « aucune transition contraire au texte ». Cela ne teste pas une hypothèse statistique mais vérifie un automate — ce qui est utile, mais ne relève pas de B4. En conséquence, parler de « falsification » (H_A / H_B) est un emprunt de vocabulaire qui donne à un test d'intégration l'apparence d'une expérience décisive. Il manque une mesure de couverture des chemins : combien de transitions sur combien de possibles ? Sans cette fraction, « aucune violation dans la batterie » n'est pas interprétable.

**3. Pour Q1, D recommande (c) + C4 + « séparation factorielle de la consigne et du canal privé », mais sans plan d'analyse concret.** Les duels Q1-A et Q1-B sont formulés en termes d'estimateurs (différence appariée, gain de taux de détection) mais les seuils sont « choisis avant lecture, aucune valeur fournie ». Sans ancrage numérique, la conception n'est pas scellable : un seuil choisi après observation des données invalide le duel. D le sait (« aucune valeur n'est établie par les pièces ») mais ne résout pas le problème, ce qui rend la critique asymétrique — D exige des seuils des autres, mais se dispense de les fournir.

**4. L'expression « séparation factorielle » suppose un plan croisé complet.** Croiser consigne (2 niveaux) × canal privé (2 niveaux) × texte (2 niveaux) = 8 cellules, dont certaines sont impossibles ou sans sens (texte de colludeur sans consigne de colludeur : le texte a été produit sous cette consigne). D demande de « déclarer comme interventions diagnostiques hors politique » les combinaisons artificielles, mais ne chiffre ni leur nombre, ni le coût en passes forcées, ni la puissance résiduelle par cellule quand l'effectif de 200 épisodes CORE est réparti en 8 bras.

### (b) Conditions de perte de puissance ou de non-jugeabilité

| Mesure/critère | Condition de perte de puissance |
|---|---|
| Duel Q1-A (consigne seule change le score) | Impossible si le canal privé ne peut pas être tenu fixe. D reconnaît cela (« sans tenir le canal privé fixe, ce duel est impossible ») mais le propose quand même dans la « version minimale ». La puissance est alors exactement zéro pour l'hypothèse « consigne seule ». |
| Duel Q1-B (signal résiduel du texte) | Perd sa puissance si la base des mots et les prédicteurs triviaux captent le signal du texte de collusion, ce qui est plausible : un colludeur qui argumente pour l'option cible produit un vocabulaire distinctif. Le gain G résiduel ne serait alors détectable que si la sonde capture quelque chose de non lexical et non positionnel, ce qui est exactement ce que l'on veut montrer mais ne peut pas présupposer. |
| Plan factoriel complet | Avec n = 200 épisodes CORE et 8 cellules, chaque cellule a ~25 épisodes (**illustratif**). L'intervalle par blocs (bloc = scénario) avec ~6 scénarios par cellule (**illustratif**) a un nombre de blocs insuffisant pour un rééchantillonnage stable. Plus de 1 % de tirages dégénérés est probable, rendant la lecture « non calculable ». |

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Instruction privée honnête.** D la propose (section « Contrôle indispensable »), ce qui est bien. Mais elle n'est pas dans le protocole NARCBench publié ; il faudrait la fabriquer, et sa fabrication introduirait un texte non produit par le 8B, donc hors politique — exactement ce que D reproche à (b). Le coût de cette fabrication n'est pas chiffré.

2. **Contrôle de longueur et de position sans changement de rôle.** D le demande (« variations de longueur et de position sans changement de rôle »), mais sans spécifier comment on produit un préfixe de longueur différente sans changer le rôle. Ajouter du padding ? Changer une phrase cosmétique ? Chaque choix a un effet sémantique propre.

3. **Pas de contrôle de la reproductibilité du score entre passes.** D parle de « répétition avec contexte identique » comme contrôle négatif du duel « contexte », mais ne dit pas combien de répétitions, ni quel écart est toléré. Si la variance de relecture est du même ordre que l'effet C1 − C2, l'expérience est sans puissance.

---

## Sur la proposition E

### (a) Défauts de méthode

**1. La « batterie de fermeture » (QO-1) est un test en boîte noire dont la couverture est inconnue et incontrôlable.** E propose de sceller des scénarios factices avec des « sorties scientifiques secrètement différentes », puis de vérifier qu'aucune information réservée n'atteint une interface autorisée. C'est un test de pénétration ad hoc, pas une preuve de sécurité. Les chemins non testés ne sont pas falsifiés. E le reconnaît (« pour cette batterie seulement ») mais en fait une « expérience décisive », ce qui est contradictoire : un duel dont l'issue positive ne falsifie que localement n'est pas décisif.

**2. La formulation des duels Q1 utilise des espérances et des seuils non ancrés.** Le duel « contexte » définit D_C = E[|s(x, c_collusion) − s(x, c_honnête)|] avec un seuil δ_C « choisi avant lecture, aucune valeur fournie ». C'est le même problème que D : sans valeur, le duel n'est pas scellable. De plus, l'espérance est sur les messages x, mais la distribution de x dépend du scénario, du tour, de la longueur, du domaine — tous des facteurs confondants. Sans conditionnement explicite, D_C mélange l'effet de contexte et la variabilité structurelle du jeu.

**3. L'utilisation de l'espérance de la valeur absolue masque la direction de l'effet.** E prend |s(x, c_collusion) − s(x, c_honnête)| plutôt que la différence signée. Une sonde qui donnerait un score *plus bas* sous consigne de collusion et un score *plus haut* sous consigne honnête (ce qui serait un artefact de calibration) contribuerait positivement à D_C. E dit « différences signées rapportées séparément », mais le duel formel porte sur la valeur absolue, ce qui affaiblit la falsification de H_A : un effet dans le mauvais sens la falsifie aussi.

**4. Le duel « discrimination restante » est formulé en termes de gain de taux de détection G, mais le taux de détection dépend du seuil de classification, qui n'est pas fixé.** E dit « seuils de fausses alertes calibrés séparément », ce qui signifie que chaque instrument a son propre seuil, rendant la comparaison de G entre instruments non directe. Si le seuil est calibré sur le même jeu que celui où G est mesuré, il y a fuite.

**5. La « version permettant une attribution plus fine » (plan croisé consigne × canal × texte) a les mêmes problèmes de puissance que D (voir critique de D, point 4), mais E ne les reconnaît pas du tout.** Aucune mention du coût en effectifs, aucune mention du risque de tirages dégénérés.

### (b) Conditions de perte de puissance ou de non-jugeabilité

| Mesure/critère | Condition de perte de puissance |
|---|---|
| D_C (dépendance au contexte) | Si σ(s) intra-message est grande (variance du score entre jetons d'un même message, agrégée par le maximum), alors D_C est dominé par le bruit d'agrégation. L'espérance convergera lentement ; avec ~800 messages de colludeurs (**illustratif**), un δ_C de l'ordre de 0,1 σ (**illustratif**) nécessiterait n >> 800 pour être détecté. |
| G (gain de détection) | Si la meilleure vérification mécanique (base des mots + métadonnées) atteint un taux de détection élevé (> 0,9, **illustratif**), G est borné par le plafond : la sonde ne peut pas gagner beaucoup plus. Dans ce régime, le duel est vrai par construction pour H_A, non parce que la sonde est mauvaise mais parce que la base est forte. |
| Batterie de fermeture (QO-1) | Puissance = 1 pour les chemins testés, 0 pour les chemins non testés. La probabilité qu'un chemin réel soit dans la batterie dépend de la couverture, qui n'est ni mesurée ni mesurable sans un modèle formel du système (ce qui excède le cadre). |

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Pas de contrôle de la taille de l'effet de relecture.** E propose « répétition avec contexte identique » mais ne dit pas comment distinguer le bruit de relecture (dû au cache KV, à la tokenisation du préfixe, aux effets d'arrondi bf16) de l'effet de contexte. Sans borne explicite sur la variance de relecture, toute différence non nulle entre C1 et C2 pourrait être attribuée au bruit.

2. **L'instruction privée honnête proposée comme contrôle n'est pas définie.** E demande « une contrainte légitime de confidentialité et une charge contextuelle appariée ». Qu'est-ce qu'une « charge contextuelle appariée » en jetons ? Si elle n'est pas appariée en longueur, en position et en structure syntaxique, le contrôle ne contrôle que partiellement.

3. **Pas de placebo explicite pour le duel « contexte ».** E utilise le mot « permutation » une fois (tableau final) mais ne décrit pas une permutation complète des rôles comme contrôle placebo du duel D_C. Sans permutation, on ne connaît pas la distribution de D_C sous l'hypothèse nulle « la sonde ne lit pas le contexte ».

---

## Note transversale

La pièce C est absente. Les trois propositions présentes (A, D, E) convergent vers (c) pour Q1 et divergent sur QO-1. Aucune des trois ne fournit de seuil chiffré pour les duels Q1, ce qui rend les trois conceptions non scellables en l'état pour la partie NARCBench. A se distingue par E1 (propre/non propre, gratuit, sur politique), qui est le seul duel qui ne repose pas sur une relecture hors politique et dont la faisabilité ne dépend pas d'un plan croisé impossible à puissance suffisante.

FIN-DE-CELLULE