# Proposition C — Tour III.3 : réponse aux critiques et synthèse finale

*Note d'intégrité : La pièce `E3-T2-critique-croisee-D` est absente (statut : jamais lancée) ; je n'en invente pas le contenu.*

---

## (a) Réponse point par point aux critiques visant la proposition C

### Critiques de la proposition A sur C

1. **Deux règles de sélection différentes dans l'Exp. 1 (`Témoin-Filtre` par script mécanique vs `Exp-Minimal` par choix de l'agent).**
   * **Statut : Acceptée.** Confondre l'accès à l'outil interactif et la règle de sélection finale des $M$ fiches viole l'isolation causale. **Correction :** Dans l'Expérience 1 corrigée, *tous* les candidats générés par `Exp-Minimal` au fil de ses sessions passent par le même sélecteur mécanique déterministe que le témoin pour extraire les $M$ fiches soumises. De plus, on rejoue les deux modes de sélection (choix de l'agent vs filtre mécanique) sur les mêmes traces pour mesurer ce facteur séparément.
2. **Le témoin est construit pour sur-ajuster (le max de $N$ sur l'erreur de développement gonfle les fausses découvertes quand $N$ croît).**
   * **Statut : Acceptée.** **Correction :** Le filtre mécanique n'utilise plus l'erreur brute sur l'ensemble des épisodes de développement, mais une validation croisée interne sur les épisodes de développement avec pénalité de complexité (longueur de description de `loi_predictive` gelée). En outre, le quota fixe $M$ est remplacé par un quota *au plus* $M$ (soumission conditionnelle au franchissement d'un seuil de validation interne), évitant que $F = M$ par construction sous le nul.
3. **Le contrôle négatif « sortie constante "aucune anomalie détectée" » injecte une fausse information positive et sa sous-performance ne doit pas être posée comme condition de validité.**
   * **Statut : Transformée en test.** A, B et E convergent sur ce défaut : ce message trompe l'agent au lieu de masquer l'information. J'emprunte à E et B l'idée d'un masquage non trompeur et je transforme ce contrôle en un **duel mécaniste formel** (Expérience 1-bis) opposant `Exp-Minimal` (retours réels) à `Exp-Masqué` (l'outil retourne un message explicite `{"statut": "sortie_masquee_par_protocole"}`, ou des résidus permutés d'un monde indépendant de même format), sans présumer que `Exp-Masqué` doit battre ou perdre contre le témoin sans outil.
4. **Seuil « $+20\%$ et $> 2\sigma_0$ » avec $\sigma_0$ estimé d'un seul A/A à 1 degré de liberté, et manque de puissance à petit budget ($8,40\text{ USD}$ illustratif).**
   * **Statut : Acceptée.** Un estimateur de variance à 1 ddl suit une loi de $\chi^2_1$ inutilisable pour geler un seuil, et un gain relatif explose quand le dénominateur approche zéro. **Correction :** (i) Le critère est formulé en **différence absolue** de rendement sur l'oracle $\Delta Y = Y_{\text{Exp}} - Y_{\text{Témoin}}$ (en vraies découvertes nouvelles hors nul par dollar), et non en pourcentage ; (ii) le pilote de calibration mesure la variance inter-exécutions et inter-mondes $\hat{\sigma}_D$ sur $m_0 \ge 6$ mondes (illustratif) avec A/A par bras à graines *différentes* ; (iii) une **règle d'arrêt de puissance** est ajoutée : le duel principal n'est lancé que si le nombre de mondes $m$ disponible satisfait $m \ge (z_{\alpha} + z_{\beta})^2 \hat{\sigma}_D^2 / \delta^2$ pour la marge d'intérêt $\delta$ gelée ; sinon, le test est déclaré non jugeable avant dépense.
5. **Exp. 2 : hétéroscédasticité construite (2 générations de Sakana contre 50 d'`Exp-Minimal` à budget égal) et issues non exhaustives.**
   * **Statut : Acceptée.** À 2 générations, la variance de l'estimateur du bras cher domine et empêche toute réfutation. **Correction :** L'unité de réplication de l'Expérience 2 est le **monde planté** ($m$ mondes appariés), sur chacun desquels les deux bras reçoivent le budget minimal permettant au moins 1 génération du bras cher, et les issues sont reformulées sous forme de paires de tests unilatéraux couvrant tout l'espace des résultats (victoire nette, infériorité/équivalence sous $\delta$, ou zone d'indécision si la variance observée excède celle du pilote).
6. **« Batterie de mondes de complexité graduée » non spécifiée.**
   * **Statut : Acceptée.** Toute sélection des mondes après lecture des traces crée une fuite entre diagnostic et évaluation. **Correction :** La banque de mondes plantés de l'Expérience 2 est tirée et scellée avant l'Expérience 1 (R1).
7. **Instrument 3 : l'artefact est trop grossier (croissance linéaire sur données périodiques) et confond crash d'outil et rejet scientifique.**
   * **Statut : Acceptée.** **Correction :** Le test de l'instrument sépare désormais (i) le taux de livraison mécanique sans erreur de l'outil $P(I=1)$ (transport, JSON, `bwrap`) et (ii) le taux de rejet conditionnel $P(R=1 \mid I=1)$ sur des lois fausses *localement tangentes* aux premiers épisodes de développement (indistinguables en lecture textuelle zéro-coup mais réfutées par le calcul des résidus sur l'ensemble des épisodes).
8. **Contrôles manquants pointés par A (A/A sur `Exp-Minimal`, monde bruit pur dès l'Exp. 1, déterminisme de l'exécuteur, non-trivialité des épisodes de développement).**
   * **Statut : Acceptée.** Intégrés au tableau des portes et à l'Expérience 1 corrigée.

### Critiques de la proposition B sur C

1. **`Témoin-Filtre` n'est pas le témoin de N-045 (il ajoute un filtre mécanique neuf) et risque d'être surenrichi.**
   * **Statut : Transformée en test.** Les faits (§4, RAPPORTÉ) mentionnent explicitement comme option de méthode : *« le témoin choisit les siennes par une règle mécanique sur les épisodes de développement »*. Toutefois, B a raison de souligner que ce filtre est lui-même un expérimentateur passif. **Correction :** L'Expérience 1 inclut désormais le témoin nu (`Témoin-Aléatoire` ou vote de fréquence sans évaluation sur les épisodes) à côté de `Témoin-Filtre`. Cela permet de mesurer successivement le gain du filtrage mécanique passif (0 jeton) puis le gain marginal de la boucle interactive (`Exp-Minimal`).
2. **Contrôle négatif de l'Exp. 1 biaisé par le message « aucune anomalie détectée ».**
   * **Statut : Transformée en test.** Voir réponse à A.3 ci-dessus (remplacé par `Exp-Masqué`).
3. **Le « monde planté bruit pur » teste le juge O2 et non les candidats si l'on regarde les promotions.**
   * **Statut : Rejetée sur la confusion avec le juge, mais acceptée sur le plancher des soumissions.** Conformément à N-058 (RAPPORTÉ), ma proposition C ne juge jamais les bras sur les promotions du juge O2, mais sur les fiches *soumises* lues sur l'oracle. Cependant, avec un quota strictement égal à $M$, sous bruit pur, tout bras soumet $M$ fiches fausses ($F=M$, comme le prouve E). **Correction :** En autorisant chaque bras à soumettre *entre $0$ et $M$* fiches (seuil d'abstention interne), un monde « bruit pur » (ou loi hors grammaire admissible, comme le suggère B) mesure la capacité d'abstention de l'expérimentateur face au sur-ajustement.
4. **Le protocole de coût égal de l'Exp. 2 confond le nombre de générations et la sélection parmi $50 \times M$ candidats.**
   * **Statut : Acceptée.** En appliquant le même sélecteur mécanique final (corrigé en A.1) aux candidats produits par chaque bras à budget égal, la politique complète (génération + sélection) est évaluée de façon homogène.
5. **Comparaisons multiples entre l'Exp. 1 et l'Exp. 2 conditionnelle.**
   * **Statut : Acceptée.** **Correction :** Le budget d'erreur de première espèce $\alpha$ est réparti séquentiellement (procédure à portes / *gatekeeping* hiérarchique) et l'Expérience 2 est exécutée sur un jeu de mondes disjoint de celui de l'Expérience 1.
6. **Absence de sonde de mémorisation des pièces publiques.**
   * **Statut : Acceptée avec la correction méthodologique de E.** Les pièces de la course v66 étant publiques sur GitHub (§2.5, RAPPORTÉ), la mémoire paramétrique du modèle est un confondant. Mais comme le démontrent B et E contre A, tester les lois publiques contre des leurres arbitraires confond exposition et difficulté. **Correction :** Tous les duels décisifs (Exp. 1 et 2) doivent être exécutés sur des **mondes plantés neufs non publiés** (identifiants opaques, générés hors dépôt public) ; les mondes publics ne servent qu'au débogage mécanique (Porte 0).

### Critiques de la proposition E sur C

1. **La conclusion causale dépasse le contraste (`Témoin-Filtre` exécute déjà des prédictions).**
   * **Statut : Acceptée.** L'ajout du trio (`Témoin-Nu`, `Témoin-Filtre`, `Exp-Minimal`) + `Exp-Masqué` (réponses A.3 et B.1) sépare proprement : (i) le tri mécanique passif, (ii) la réflexion multi-tours sans information empirique, et (iii) la révision guidée par les retours d'exécution.
2. **L'échec de `Exp-Minimal` ne falsifie pas les architectures riches (Sakana/Kaimen) s'il existe une interaction entre architecture et exécution ; et lire les traces pour choisir les mondes crée une fuite.**
   * **Statut : Acceptée sur la fuite et la portée logique.** E a raison : l'échec de `Exp-Minimal` falsifie l'hypothèse qu'une boucle simple suffit, mais ne falsifie pas rigoureusement qu'un agent multi-fichiers ou un tournoi Elo puisse réussir là où une boucle simple échoue. **Correction :** (i) Suppression de toute lecture de traces pour choisir les mondes de la Porte 2 (mondes fixés d'avance) ; (ii) si `Exp-Minimal` échoue contre `Témoin-Filtre`, la conclusion enregistrée est que l'interaction simple ne bat pas le filtrage passif à coût égal ; tester Sakana (b) reste alors une hypothèse d'interaction d'ordre supérieur ouverte, mais qui exige un devis et un GO spécifiques conformément à N-045 (*le bon marché d'abord, le cher sur preuve*).
3. **Multiplicité et erreurs confondues ($F/\$$ comparé à un seuil de FDR, et $V+F=M$ sous quota fixe).**
   * **Statut : Acceptée.** $F/\$$ (taux de soumissions fausses par dollar) et le FDR du juge O2 n'ont pas les mêmes unités, et fixer $V+F=M$ rend $F$ redondant avec $V$. **Correction :** Le quota devient un plafond ($\le M$ fiches soumises par monde et par bras). Chaque fiche soumise est classée par l'oracle en : Vraie découverte nouvelle ($V$, hors loi nulle connue), Redondante avec le nul connu ($N_0$), ou Fausse ($F$). Le critère primaire porte sur $V/\$$ et le critère secondaire sur la proportion empirique de fausses soumissions $F / \max(1, V + N_0 + F)$ évaluée sur les mondes sans loi nouvelle accessible.
4. **Table du juge : les reformulations du nul sont vraies mais ne sont pas des découvertes.**
   * **Statut : Acceptée.** **Correction :** Dans la Porte 0, la règle d'équivalence de l'oracle et le juge O2 sont testés sur des reformulations algébriques exactes des lois connues : elles doivent donner $V = 0$ (comptées dans $N_0$, aucune promotion).

---

## (b) Protocole expérimental corrigé (Portes et Duels en inférence forte)

Toutes les expériences utilisent exclusivement `kimi-k3.1-pro` via le relais v3, sur des **mondes plantés privés neufs** (jamais poussés sur le dépôt public `lciric/ideation-organism`). Unité d'analyse statistique : le **monde planté** ($r = 1, \dots, m$). Sur chaque monde $r$, chaque bras reçoit le même budget $B$ en dollars et soumet au plus $M$ fiches via le même sélecteur mécanique final (validation croisée sur les épisodes de développement avec pénalité de longueur).

### Porte 0 : Qualification mécanique, déterminisme et pilote de puissance (A/A)
1. **Équivalence oracle et nul :** Soumission de 20 (illustratif) reformulations algébriques de lois connues et 20 polynômes interpolateurs sur-appris. Exigence : $100\%$ classés hors de $V$ ($V=0$) par la règle d'équivalence oracle ; taux de promotion par O2 $\le \alpha$.
2. **Déterminisme et étanchéité de `bwrap` :** 10 (illustratif) exécutions répétées du même script doivent produire une sortie identique au bit près ; 10 scripts d'évasion réseau/variables/modèles interdits doivent être bloqués à $100\%$ (échec fermé) ; livraison mécanique de l'outil $P(I=1) \ge 98\%$ (illustratif) sur des requêtes saines.
3. **Pilote A/A par bras et condition de jugeabilité :** Sur $m_0 = 6$ mondes privés (illustratif), deux exécutions indépendantes à graines *différentes* de chaque bras (`Témoin-Filtre` et `Exp-Minimal`) mesurent l'écart-type des différences appariées $\hat{\sigma}_D$ de $Y = V/B$. **Condition de porte :** Pour une marge minimale d'intérêt $\delta > 0$ gelée par le directeur, le nombre de mondes $m$ de l'Expérience 1 doit vérifier $m \ge (z_{1-\alpha/2} + z_{1-\beta})^2 \hat{\sigma}_D^2 / \delta^2$. Si le budget autorisé ne permet pas d'atteindre ce $m$, l'expérience s'arrête avec le statut « **non jugeable au budget alloué** » (aucune fausse réfutation).

### Expérience 1 (et 1-bis) : Duel d'allocation et d'attribution causale
Sur $m$ mondes privés qualifiés par la Porte 0 (plus $m_{\text{nul}}$ mondes où les lois connues épuisent la grammaire pour mesurer les fausses soumissions $F$), quatre bras à budget $B$ égal et même consigne de structuration sont comparés :
* **`Témoin-Nu` (T0) :** $N$ tirages Kimi indépendants, sélection de $\le M$ fiches par vote de fréquence (sans évaluer les prédictions sur les épisodes).
* **`Témoin-Filtre` (TF) :** $N$ tirages Kimi indépendants, sélection des $\le M$ meilleures fiches par le script mécanique de validation croisée sur les épisodes de développement (coût LLM du tri = 0).
* **`Exp-Masqué` (EM) :** Boucle Kimi $\le 5$ tours avec outil `exec_python`, mais la sortie de l'outil est remplacée par des résidus permutés d'un monde indépendant (même format, information empirique nulle sur le monde cible), suivie du même filtre mécanique final.
* **`Exp-Minimal` (E1) :** Même boucle Kimi $\le 5$ tours avec les vrais retours d'exécution de `bwrap` sur les épisodes de développement, suivie du même filtre mécanique final.

**Duels exclusifs (avec intervalle de confiance à $1-\alpha$ sur la moyenne des différences par monde $\Delta Y_{A,B} = \overline{Y_A - Y_B}$ et marge $\delta > 0$ gelée) :**
* **Duel 1.1 (Valeur du filtrage passif) :** $H_A : \Delta Y_{\text{TF, T0}} > \delta$ contre $H_B : \Delta Y_{\text{TF, T0}} \le \delta$. Falsifie l'inutilité du tri mécanique post-hoc si la borne inférieure de l'IC dépasse $\delta$.
* **Duel 1.2 (Valeur politique de la boucle minimale — N-045) :** $H_A : \Delta Y_{\text{E1, TF}} > \delta$ contre $H_B : \Delta Y_{\text{E1, TF}} \le \delta$ (avec contrainte que sur les $m_{\text{nul}}$ mondes nuls, le taux de soumissions fausses $F_{\text{E1}}$ ne dépasse pas $F_{\text{TF}}$ d'une marge $\varepsilon_F$ gelée).
  * Si la borne inférieure de l'IC de $\Delta Y_{\text{E1, TF}}$ dépasse $\delta$ $\implies$ **$H_B$ est falsifiée** : la boucle interactive minimale bat l'échantillonnage filtré à coût égal.
  * Si la borne supérieure de l'IC est $\le \delta$ $\implies$ **$H_A$ est falsifiée** : la boucle minimale ne vaut pas son coût en jetons face au tri mécanique.
* **Duel 1.3 (Attribution mécaniste à l'information d'exécution) :** $H_A : \Delta Y_{\text{E1, EM}} > \eta$ contre $H_B : \Delta Y_{\text{E1, EM}} \le \eta$ ($\eta > 0$ gelé).
  * Si Duel 1.2 valide $H_A$ mais Duel 1.3 valide $H_B$ (borne supérieure $\le \eta$), le gain de `Exp-Minimal` est attribué à la révision multi-tours et non à la lecture des résultats d'exécution (falsifie l'effet propre de l'exécuteur).

### Expérience 2 : Duel architectural (`Exp-Minimal` vs Kaimen (a) ou Sakana (b))
Lancée sur un nouveau lot scellé de $m_2$ mondes privés (calibré pour que chaque monde finance au moins 2 générations du candidat lourd et l'équivalent en dollars du bras de référence gagnant de l'Expérience 1). Même sélecteur final $\le M$.
* **$H_A$ (Gain architectural net) :** $\Delta Y_{\text{Candidat, Réf}} > \delta_{\text{arch}}$ (marge de rentabilité de la dette technique gelée).
* **$H_B$ (Suffisance du bras minimal / Surcharge de cérémonial) :** $\Delta Y_{\text{Candidat, Réf}} \le \delta_{\text{arch}}$.
* Chaque issue (borne inférieure $> \delta_{\text{arch}}$ ou borne supérieure $\le \delta_{\text{arch}}$) falsifie l'hypothèse adverse sans sélection opportuniste post-hoc des mondes.

---

## (c) Réponse à la question de l'arbitre (Une page)

### 1. Ce qui est établi (VÉRIFIÉ ou RAPPORTÉ dans les faits)
* **Contraintes d'architecture et de gouvernance :** L'évaluation des proposeurs se fait exclusivement sur l'oracle des mondes plantés et le coût mesuré, jamais sur le verdict du juge O2 (N-058, RAPPORTÉ). Une voie chère ne doit être payée qu'après avoir battu, à budget égal, un témoin bon marché « meilleur de $N$ », après un pilote de bruit A/A (N-045, RAPPORTÉ). Claude est exclu de tout rôle (VÉRIFIÉ). Les pièces de la course v66 étant suivies sur un dépôt public, aucun accès Web ou réseau hors du relais local n'est permis (RAPPORTÉ).
* **État réel des candidats du marché :** Aucun candidat n'est un expérimentateur prêt à l'emploi (RAPPORTÉ). **Kaimen-Inc/Co-Scientist** (`cef5bcf`) est un tournoi Elo d'idées textuelles qui **n'exécute aucun code** (seuls les outils Web/littérature sont câblés) ; il passe par le relais Kimi v3 existant, mais exige un outil d'exécution neuf et perd sa définition de la nouveauté s'il est privé de littérature (RAPPORTÉ). **The Agentic Scientist / Sakana v3** (`df83138`) exécute réellement du code et fait des ablations, mais via des agents à pleins droits dans Docker avec réseau `host` et Web par défaut, à un coût de $3,6\text{ à }21\text{ USD}$ (estimé) par génération contre $1,5\text{ à }2\text{ USD}$ (estimé) pour toute une course v66, et ses agents (`pi`, `opencode`) requièrent un relais neuf s'ils lisent en flux (RAPPORTÉ).

### 2. Ce qui n'est pas établi (HYPOTHÈSES à tester)
* **La pertinence de la séquence « (a) Kaimen puis (b) Sakana » :** Conditionner l'essai d'un agent de débogage de code (Sakana) à la victoire préalable d'un tournoi Elo textuel greffé d'un outil neuf (Kaimen) repose sur une **HYPOTHÈSE** d'emboîtement infondée : l'échec du tournoi Elo de Kaimen ne falsifierait en rien l'utilité du codage itératif de Sakana.
* **La valeur nette de l'expérimentation interactive à coût égal :** Il n'est pas établi (HYPOTHÈSE) que dépenser le budget en tours de boucle d'exécution produise plus de vraies découvertes par dollar qu'un témoin « Kimi, meilleur de $N$ » dont les $N$ formules indépendantes sont filtrées mécaniquement (pour $0$ jeton LLM) sur les épisodes de développement.
* **La compatibilité technique :** Le support du choix d'outil forcé par nom sur `kimi-k3.1-pro` (requis par Kaimen) et l'obligation du mode flux pour `pi`/`opencode` (Sakana) sont non vérifiés (HYPOTHÈSE).

### 3. Choix recommandé, raisons, risques et ce qui ferait changer d'avis
* **Choix : « Autre chose » en premier** — brancher d'abord un **expérimentateur à boucle minimale maison (`Exp-Minimal`)** utilisable immédiatement sur le relais v3 (sans flux) et le bac `bwrap` existants, comparé à coût égal à la fois au témoin nu (« meilleur de $N$ ») et au témoin à **filtre mécanique sur les épisodes de développement (`Témoin-Filtre`)**, ainsi qu'à un contrôle à sorties masquées (`Exp-Masqué`).
* **Pourquoi pas The Agentic Scientist (Sakana) d'abord ? (Réponse directe à Lazar) :** Parce que brancher Sakana en premier mélange l'hypothèse scientifique (l'itération sur le code aide-t-elle à découvrir les lois ?) avec un lourd chantier d'ingénierie (relais en flux neuf, confinement Docker d'agents à pleins droits ayant déjà modifié leur protocole d'évaluation par le passé) et un coût par génération de $3,6\text{ à }21\text{ USD}$ (estimé) qui réduit drastiquement le nombre de réplications à budget fixe, détruisant la puissance statistique du test. `Exp-Minimal` teste le cœur du mécanisme de Sakana (écrire un script $\to$ exécuter dans `bwrap` $\to$ lire les résidus $\to$ réviser la loi) dès aujourd'hui sur l'infrastructure v66/v67.
* **Pourquoi pas Kaimen d'abord ?** Parce que lui écrire nous-mêmes son moteur d'exécution revient à développer `Exp-Minimal`, tout en y ajoutant le surcoût en jetons ($1,3\text{ à }12\text{ USD}$ estimé) et le bruit d'un superviseur Elo conçu pour de la synthèse bibliographique.
* **Risques :** (1) Puissance statistique insuffisante si la variance inter-mondes domine l'effet (traité par la condition d'arrêt du pilote A/A) ; (2) qu'une boucle simple échoue sur des lois exigeant un échafaudage de code complexe où Sakana aurait réussi (interaction architecture $\times$ exécution).
* **Mesure qui départage et ce qui ferait changer d'avis :** La différence appariée par monde de vraies découvertes nouvelles (hors nul connu, lues sur l'oracle de mondes privés neufs) par dollar dépensé ($\Delta Y = \Delta(V/\$)$), sous plafond de $\le M$ fiches sélectionnées par le même filtre mécanique.
  1. Si `Témoin-Filtre` $\ge$ `Exp-Minimal` (borne supérieure de l'IC de $\Delta Y \le \delta$) : on garde le filtrage mécanique passif sur $N$ tirages ; l'allocation de jetons à la boucle simple est rejetée.
  2. Si `Exp-Minimal` bat `Témoin-Filtre` ET `Exp-Masqué` : la valeur causale de l'exécution interactive est prouvée à bas coût (N-045). On ouvre alors (et seulement alors, sous nouveau devis) le duel architectural contre **Sakana enfermé (b)** s'il faut pousser la complexité du code d'analyse, ou **Kaimen (a)** s'il faut tester le tri par tournoi Elo.

### 4. L'expérience à faire en premier
Exécuter la **Porte 0 puis l'Expérience 1** sur des mondes plantés privés (absents de GitHub) : calibrer la variance par un pilote A/A à graines différentes, vérifier que le nombre de mondes assure la puissance requise pour la marge $\delta$, puis opposer à budget strictement égal `Témoin-Nu`, `Témoin-Filtre`, `Exp-Masqué` et `Exp-Minimal` sur le relais v3 et l'exécuteur `bwrap` existants.

FIN-DE-CELLULE