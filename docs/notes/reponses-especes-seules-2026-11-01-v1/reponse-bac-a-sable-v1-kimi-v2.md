# Vérification non circulaire — analyse méthodologique

## 0. Portée et distinction préalable

La circularité n’est pas une propriété absolue d’un outil : elle est relative à une **base de confiance** et à la proposition que l’on prétend établir. Quatre propositions doivent être séparées :

1. **Identité** : les octets relus sont ceux soumis à l’exécution.
2. **Provenance** : ces octets proviennent des sources, dépendances et outils déclarés.
3. **Non-ingérence** : l’artefact ou son environnement de production n’a pas pu modifier le vérificateur, ses références ou son verdict.
4. **Validité sémantique** : le verdict mesure la propriété recherchée, et non seulement la satisfaction d’un contrôle particulier.

Empreintes, constructions reproductibles, journaux, attestation, diversité et canaris ne couvrent pas ces quatre propositions de la même façon.

La citation d’Avalon vise précisément le cas où l’outil de hachage appartient au même domaine potentiellement influençable que l’objet contrôlé ; elle n’implique pas qu’une empreinte calculée dans un domaine indépendant soit inutile (pièce 4, § 4, « Pratiques de l’annexe K », citation de la p. 76). Les « 25 environnements » constituent un constat empirique rapporté, non un taux généralisable de sondage (pièce 4, même section, p. 79).

L’état probant des pièces est limité : la v48 n’a exercé aucun `bwrap` réel et ses essais reposent sur des exécuteurs factices (pièce 1, en-tête et « Ce qui n’est pas vérifié en réel ») ; le devis machine n’a encore ni loué de machine ni écrit les scripts décrits (pièce 2, § 6, « Pas fait ») ; la synthèse N12–N13 est « tenue sous condition » et nécessite un erratum avant de servir, même si sa carte nomme le risque de circularité (pièce 3, « Verdict en une phrase » et carte N12).

---

## Q1 — Base de confiance minimale et effet d’une micro-VM

### Mécanisme

La base de confiance minimale est l’ensemble des composants dont l’altération pourrait modifier **sans détection** l’exécution mesurée, les éléments de preuve ou le verdict. Elle comprend, selon la proposition visée :

- le matériel, le microcode, le micrologiciel et les services du fournisseur, sauf hypothèse explicite les excluant du modèle de menace ;
- l’hyperviseur ou VMM, le noyau hôte et les interfaces de virtualisation ;
- le noyau invité, le bac, sa politique de montage, ses limites et l’environnement d’exécution ;
- la chaîne de construction lorsque l’on tire une conclusion de provenance ;
- le canal d’entrée du vérificateur, y compris ses formats, décodeurs et analyseurs : recevoir un artefact « comme donnée » ne rend pas son traitement sans confiance ;
- le composant qui calcule les empreintes, les références attendues, le vérificateur, sa politique et ses seuils gelés ;
- les clés et mécanismes de fraîcheur, de signature ou d’ajout à un journal externe, si l’on s’appuie sur eux contre l’altération ou le rejeu.

L’agent, le code produit, les processus du bac et les sorties non validées peuvent rester **hors de la base de confiance**, parce qu’ils sont précisément les objets non fiables. Une chaîne de compilation ne peut être exclue que si aucune conclusion de provenance ne repose sur elle.

La machine jetable sans secret réduit surtout les conséquences de confidentialité et de persistance. Elle ne garantit pas l’intégrité d’un verdict : une machine sans secret peut encore produire des mesures ou des journaux non fiables. Les décisions R-533 et la destruction après série décrivent le cycle de vie, non une racine de vérité (pièce 2, en-tête et § 2.6).

### `bwrap`, gVisor, Firecracker/Kata

| Mécanisme | Ce qui change | Ce qui ne change pas |
|---|---|---|
| Bac de type `bwrap` | Isolation principalement fondée sur des mécanismes du noyau hôte partagé. | Le noyau hôte et une partie importante de l’environnement d’exécution restent communs au domaine de production et aux mesures prises sur cet hôte. |
| gVisor | Interposition d’un noyau applicatif en espace utilisateur, réduisant certaines interfaces directement exposées au noyau hôte. | Le noyau hôte, l’hôte et le fournisseur restent dans la base de confiance ; compatibilité et performances dépendent de la charge. |
| Micro-VM Firecracker ou conteneur à isolation VM de type Kata | Déplacement de la frontière principale vers une VM avec noyau invité distinct et interface matérielle virtuelle plus étroite. | L’hôte, le VMM, le matériel et souvent le plan de contrôle du fournisseur restent Trusted Computing Base. Si le vérificateur tourne dans la même VM ou dépend de mesures fournies par le même domaine, la circularité logique demeure. |

Une micro-VM change donc la **frontière d’isolation et les modes de défaillance communs**, mais pas la nécessité d’une racine de vérification indépendante. Elle ne transforme pas à elle seule une preuve produite localement en preuve extérieure.

**Conditions de validité :** version et configuration exactement mesurées, vérificateur hors du domaine contrôlé par l’artefact, références indépendantes, et adéquation du modèle de menace au fournisseur retenu.

**Ce qui réfuterait le gain de classe :** la démonstration qu’un composant commun non examiné — hôte, VMM, plan de contrôle, canal ou vérificateur — peut encore modifier simultanément les deux environnements et leurs preuves. Les pièces ne permettent pas de trancher la faisabilité de Firecracker ou Kata sur la CPX32 décrite.

Références générales : NIST SP 800-190 pour la distinction conteneurs/isolation [S9] ; Agache et al. pour l’architecture et les objectifs de Firecracker [S8].

---

## Q2 — Séparation production/vérification et canaux résiduels

### Correction conceptuelle du canal proposé

Un vérificateur qui ne reçoit **que des empreintes** ne peut vérifier que la correspondance avec des empreintes déjà connues. Il ne peut ni relire le contenu ni reproduire l’exécution sans recevoir aussi les octets, une preuve vérifiable, ou un accès indépendant à ceux-ci.

L’empreinte doit être calculée à la frontière fiable sur les octets effectivement reçus. Une empreinte produite dans le bac est seulement une déclaration supplémentaire du bac. Le témoin de série de la plomberie lie une archive à une série et limite confusion et rejeu accidentel, mais il est explicitement non secret : il n’authentifie pas une machine compromise (pièce 2, § 2.1 et garde G10, § 4).

### Fuites restantes, par mécanisme

| Canal | Mécanisme | Pertinence lorsque l’optimiseur ne voit que le verdict |
|---|---|---|
| Contenu de l’artefact | Les données elles-mêmes influencent l’analyse et le verdict. | Canal principal : il ne disparaît pas avec le hachage. |
| Taille, nombre, types, noms, ordre | Métadonnées visibles avant ou pendant le traitement. | Comptent si elles modifient le verdict, les ressources, ou une décision ultérieure visible par l’optimiseur. |
| Temps, retries, fermetures de connexion | Le transport et l’ordonnanceur révèlent un comportement ou créent un retour implicite. | Peu pertinents pour l’optimiseur s’ils sont strictement inobservables et sans effet sur le verdict ; importants sinon. |
| Consommation de ressources et erreurs | Durée, mémoire, échecs partiels ou messages enrichissent le signal de retour. | Un verdict détaillé ou des erreurs adaptatives donnent davantage de feedback qu’un résultat strictement fixe. |
| Verdict répété | Chaque réponse constitue une observation permettant une adaptation ultérieure. | C’est le canal intentionnel central : même binaire, il reste un signal d’optimisation lorsque les essais sont adaptatifs. |
| État partagé | Cache, dépôt, journal ou configuration modifiables relient indirectement production et vérification. | Réfute la séparation si cet état peut changer les références ou le verdict. |

La normalisation des métadonnées ou un ordonnancement extérieur fixe peuvent réduire certains canaux, sans supprimer le canal du contenu ni celui du verdict. La formule d’Avalon « every model-visible channel is a leak channel » doit être lue comme une règle de revue des interfaces, non comme une preuve que tout canal est exploitable dans tout protocole (pièce 4, § 4, p. 80).

**Conditions de validité :** schéma de sortie borné, références non accessibles en écriture au producteur, absence d’état partagé modifiable, observation externe des seuls messages prévus, et vérificateur capable de traiter les artefacts comme entrées non fiables.

**Ce qui réfuterait la non-circularité :** une dépendance du verdict à un état non relu contrôlé par la production, ou la possibilité pour celle-ci d’altérer la référence, le journal de décision ou le code du vérificateur.

L’antériorité conceptuelle des canaux de confinement et des canaux cachés est notamment Lampson, 1973 [S1].

---

## Q3 — Empreintes, constructions reproductibles, journaux et attestation

### Ce que chaque mécanisme établit

| Mécanisme | Proposition effectivement soutenue | Limite principale |
|---|---|---|
| Empreinte calculée hors du bac | Les octets reçus ou relus correspondent à une valeur déterminée. | Ne prouve ni leur provenance ni leur exécution. Sans ancrage indépendant, elle ne fait que constater l’état présenté. |
| Journal chaîné ou signé hors du domaine de production | Cohérence et ordre d’un ensemble d’événements, avec fraîcheur si un défi externe est utilisé. | Un journal fidèle d’événements faux reste fidèlement faux. |
| Construction reproductible | Une même source et un environnement déterminé produisent les mêmes octets. | Ne prouve ni l’exécution effective, ni l’innocuité, ni la correction sémantique. Une construction malveillante peut être parfaitement reproductible. |
| Journal des appels système | Événements observés depuis un point d’instrumentation déterminé. | Sa couverture dépend du point d’observation ; produit dans le domaine non fiable, il est altérable et potentiellement incomplet. Il ne décrit pas tout le calcul interne. |
| Réexécution indépendante | Concordance comportementale ou d’empreintes dans un second domaine, pour des entrées et une sémantique définies. | Exige déterminisme ou protocole statistique ; deux exécutions peuvent partager la même erreur de spécification. |
| Attestation distante | Un ensemble de mesures lié à une identité de plate-forme et à une fraîcheur cryptographique. | Ne prouve généralement qu’un état mesuré, souvent au démarrage, et non l’exactitude de chaque exécution ultérieure ni la justesse des valeurs de référence. |

Constructions reproductibles et journaux d’appels système ne suffisent donc pas, à eux deux, à établir « ce qui a tourné est ce qui a été relu ». Il manque une liaison externe entre : artefact, environnement mesuré, instance d’exécution, fraîcheur, entrées, sorties et verdict. Sur les constructions reproductibles, voir Lamb et Zacchiroli [S6] ; sur le modèle général evidence/appraisal de l’attestation, RFC 9334 [S7].

### Attestation matérielle

Elle n’est pas logiquement obligatoire si l’hôte et le fournisseur sont explicitement acceptés dans la base de confiance. Elle devient pertinente lorsque la prétention est de réduire cette confiance. Sa validité suppose notamment :

- une racine matérielle reconnue et une chaîne de certificats vérifiable ;
- un défi frais empêchant le rejeu ;
- des mesures couvrant les composants dont dépend le verdict ;
- des valeurs de référence obtenues indépendamment ;
- une interprétation limitée à ce que la technologie mesure réellement.

**Prix :** les pièces ne documentent ni capacité d’attestation ni tarif correspondant pour la CPX32. Leur prix de **0,0577 EUR/h HT** concerne la machine courante seule (pièce 2, § 1.2). Toute capacité nécessitant une instance ou une offre différente demanderait un relevé séparé ; aucun supplément chiffré ne peut être déduit des pièces.

**Ce qui réfuterait la preuve :** composant non mesuré mais capable de modifier l’exécution, absence de fraîcheur, références provenant du producteur, ou écart entre l’état attesté et l’état réellement utilisé.

---

## Q4 — Redondance diverse

### Gain possible

Deux bacs d’implémentations différentes peuvent détecter des divergences de comportement et éviter qu’un défaut propre à une implémentation détermine seul le verdict. Leur accord n’est toutefois probant que si :

- les exécutions sont indépendantes avant comparaison ;
- la propriété comparée est définie, avec traitement explicite du non-déterminisme ;
- le comparateur et la politique d’accord sont extérieurs aux deux bacs ;
- les causes de divergence sont distinguées des simples différences légitimes d’environnement.

Contre un optimiseur adaptatif, le dispositif ne supprime pas le signal : l’optimiseur peut apprendre le prédicat d’acceptation conjoint. Le gain plausible est une diminution des acceptations dues à certains défauts spécifiques, au prix éventuel de davantage de rejets ou de verdicts non concluants. Aucun gain chiffré n’est établi par les pièces.

Deux implémentations sur le même hôte ne constituent pas deux racines de confiance. Noyau hôte, matériel, fournisseur, chaîne de compilation, spécification, comparateur ou références communs restent des sources de défaillances corrélées.

### Antériorité et portée

- **Thompson, 1984** : la confiance ne peut pas se fonder uniquement sur la relecture du source lorsque la chaîne qui produit et interprète ce source est elle-même compromise [S2].
- **Wheeler, 2005** : la double compilation diverse vise le problème particulier du compilateur de confiance, sous des conditions d’indépendance et de reproductibilité ; elle ne constitue pas une preuve générale d’étanchéité de bac [S3].
- **Programmation en N versions, Avižienis, 1985** : diversité de conception pour tolérer des fautes [S4].
- **Knight et Leveson, 1986** : les fautes de versions développées séparément ne sont pas nécessairement indépendantes ; l’accord ne se convertit donc pas directement en probabilité de correction [S5].

La part de calcul répétée correspond à plusieurs passages, mais le coût total comprend aussi adaptation, canonicalisation, analyse des désaccords et maintien des deux environnements. Aucun devis pour cette redondance n’est servi.

**Ce qui réfuterait le gain :** des contrôles plantés non détectés par les deux implémentations, une corrélation élevée des erreurs, ou un comparateur commun capable d’absorber la divergence sans la signaler.

---

## Q5 — Canaris et mesure du sondage

### Validité de la mesure

Un canari journalisé mesure les **contacts observés avec certains leurres**, dans une couverture d’instrumentation donnée. Il ne mesure pas directement l’intention, ni l’ensemble du sondage de la plate-forme.

Sa validité dépend :

- d’une définition préenregistrée de l’événement : simple présence dans une énumération, lecture de contenu et utilisation effective n’ont pas la même spécificité ;
- d’une journalisation hors du domaine de l’artefact ;
- de placements et de leurres non connus de celui-ci ;
- de contrôles positifs prouvant que le capteur se déclenche et de contrôles négatifs prouvant qu’il ne se déclenche pas spontanément ;
- d’un corpus d’artefacts honnêtes représentatif, exécuté dans le même environnement ;
- d’une distinction entre exécutions répétées d’un même artefact et artefacts réellement indépendants.

Un artefact qui touche un canari peut être éliminé par une règle de conformité sans que cela fournisse une estimation générale du sondage. Inversement, l’absence de contact vaut **« aucun événement observé »**, non « absence de sondage ».

### Seuil éliminatoire gelé

Le seul seuil générique qui n’invente pas un taux de fausses alertes est : **élimination dès le premier événement appartenant à une classe d’accès strictement interdite, définie avant l’exécution et validée par les contrôles du capteur**. Il s’agit d’une règle binaire de non-conformité, pas d’une mesure quantitative de fréquence.

Pour des événements moins spécifiques, aucun seuil chiffré universel n’est défendable sans mesure de référence. Le taux de fausses alertes sur artefact honnête est **inconnu dans les pièces** ; il s’estime par la proportion d’artefacts honnêtes indépendants signalés, accompagnée d’un intervalle d’incertitude et d’une analyse des regroupements par artefact. Un capteur imparfaitement couvert peut simultanément produire peu de fausses alertes et manquer beaucoup d’événements.

### Mesure complémentaire

Une mesure experte distincte est l’évaluation sur un **oracle fonctionnel indépendant et tenu en réserve**, complétée par :

- des mutations contrôlées du vérificateur ou des artefacts de test pour mesurer son taux de détection ;
- une comparaison entre environnements et vérificateurs non visibles pendant l’optimisation ;
- la courbe de performance en fonction du nombre de verdicts adaptatifs reçus.

Ces mesures testent si l’artefact satisfait la propriété sémantique hors des contrôles connus, plutôt que seulement s’il a touché tel leurre. Leur réfutation serait un oracle dérivé des mêmes hypothèses que le vérificateur principal, ou une fuite des cas de réserve dans le processus d’optimisation.

Le préenregistrement scellé avant session et le refus d’un seuil non chiffré fournissent un précédent organisationnel pour ce gel (pièce 1, tableau « Ce que fait la v48 », lignes « préenregistrement court » et « lecture mécanique »). L’exigence d’éprouver chaque garde sur cas sain et artefact figure dans la plomberie (pièce 2, § 4).

---

## Q6 — Suites publiques et lecture de leurs résultats

Aucune suite publique n’est nommée dans les pièces servies. Les suivantes sont des **suites de projet ou de noyau**, pas des certifications générales d’étanchéité.

| Cible | Suite publique, auteurs, année et identifiant | Portée |
|---|---|---|
| `bubblewrap` | **bubblewrap upstream test suite**, Bubblewrap contributors, sans date, dépôt vivant à figer par commit ; `containers/bubblewrap`, répertoire `tests` : https://github.com/containers/bubblewrap/tree/main/tests | Régressions et comportements du programme dans une version/configuration donnée. Pas une preuve contre toute violation de confinement. |
| gVisor | **gVisor syscall tests**, gVisor Authors, sans date ; `google/gvisor`, `test/syscalls` : https://github.com/google/gvisor/tree/master/test/syscalls ; essais complémentaires sous https://github.com/google/gvisor/tree/master/test | Surtout compatibilité des appels et comportements attendus ; le passage d’une suite de compatibilité ne démontre pas l’isolation de sécurité. |
| Firecracker | **Firecracker integration tests — security**, Firecracker Authors, sans date ; `firecracker-microvm/firecracker`, `tests/integration_tests/security` : https://github.com/firecracker-microvm/firecracker/tree/main/tests/integration_tests/security ; cadre général : https://github.com/firecracker-microvm/firecracker/tree/main/tests | Contrôles liés à la version et à l’environnement d’exécution du projet ; validité limitée à l’hôte, au noyau, à la configuration et aux propriétés testées. |
| Mécanismes Linux communs | **Linux Test Project**, LTP contributors, sans date ; identifiant `linux-test-project/ltp` : https://github.com/linux-test-project/ltp. **Linux kernel selftests (kselftest)**, Linux kernel community, sans date : https://www.kernel.org/doc/html/latest/dev-tools/kselftest.html | Couverture de mécanismes noyau utiles aux configurations étudiées. Ce ne sont pas des suites de certification de `bwrap`, gVisor ou Firecracker. |

Lecture recevable des résultats :

- commit de la suite, version du bac, noyau, architecture et configuration associés ;
- distinction entre réussites, échecs, essais ignorés et échecs attendus ;
- présence de contrôles positifs et négatifs ;
- reproduction sur l’environnement effectivement utilisé ;
- conclusion limitée à la propriété et à la couverture de chaque test.

Un échec valide peut réfuter une propriété précise dans cette configuration. Une réussite ne réfute pas l’existence d’un défaut hors couverture. La suite CL16/CL17 annoncée — **547 essais en environ 340 s** pour CL17 et **517 en 346 s** pour CL16 — est un repère de coût de la suite interne, non une suite publique d’étanchéité (pièce 2, § 1.1).

---

## Q7 — Ordre de dépendances et coûts illustratifs

### Ordre qui ressort des pièces

Cet ordre est une exposition des dépendances, non une recommandation :

1. **Gel du sens du verdict.** Définition de la propriété vérifiée, base de confiance, canal, préenregistrement, cas sain/artefact, seuils et critères « non concluant ». Sans cela, les étapes suivantes éprouvent surtout la plomberie.
2. **Prérequis sans location.** Versement du code et des sondes dans git, correction de CL16-01, écriture et essais des scripts et gardes contre faux serveur, lectures gratuites de disponibilité et d’images, correction de la chaîne de dépôt et, pour la production, existence de l’exécuteur distant par lots (pièce 2, § 5, « Avant le GO » ; § 2.7).
3. **S0 — plomberie réelle.** Épreuve de `bwrap` sous l’identité prévue, fermeture réseau couche par couche, G8/G9 avant et après redémarrage, aller-retour d’archive témoin, destruction vérifiée ; aucun code de l’étage n’est nécessaire à cette série (pièce 2, § 1.3 et § 4).
4. **S1 — exécution réelle de la suite.** Passe cgroup v2, redémarrage et contrôles, puis passe cgroup v1 ; suites et sondes, manifestes et résultats scellés. C’est la passe B qui est déclarée décisive pour CL17-étage (pièce 2, § 2.4).
5. **Épreuve de bout en bout de la vérification extérieure.** Empreintes recalculées par le domaine de réception, relecture indépendante des manifestes, réexécution ou reproduction des artefacts lorsque cela fait partie de la prétention, et contrôle que les cas sain/artefact produisent bien les verdicts préenregistrés.
6. **Production P.** Elle dépend en outre de l’exécuteur distant par lots : l’étage actuel est interactif, tandis que les clés restent dans la session et que la machine n’exécute que des lots (pièce 2, § 2.7).

Les suites publiques de Q6 s’insèrent naturellement dans les épreuves de S1 comme éléments de couverture supplémentaires, sans changer leur portée. Une reproduction tierce peut porter sur les résultats scellés de S1 ; tant qu’elle manque, les conclusions restent bornées au domaine qui les a produits. La v48 qualifie déjà ses résultats d’**exploratoires** et non opposables (pièce 1, « Ce qui n’est pas vérifié en réel »).

### Devis machine servi

Hypothèses du devis : heure commencée facturée, TVA et taux de change supposés ; soit **0,0796 USD/h TTC** (pièce 2, § 3).

| Série | Attendu | Pire cas retenu |
|---|---:|---:|
| S0 | 1 h ; **0,08 USD** | 2 h ; **0,16 USD** |
| S1 | 1 h ; **0,08 USD** | 3 h ; **0,24 USD** |
| P | 3 h ; **0,24 USD** | 40 h ; **3,19 USD** |
| Course 2, ensemble du scénario | 6 h ; **≈ 0,48 USD** | 93 h ; **≈ 7,41 USD** |

Source de chaque ligne : pièce 2, §§ 3.1–3.2. La marge du chien de garde ajoute **14 h** et **1,11 USD** au pire cas décrit ; le plafond de GO proposé dans le devis est **10 USD** (pièce 2, § 3.2).

Ces montants ne comprennent ni second vérificateur durable, ni double implémentation, ni attestation particulière, ni audit indépendant. Les coûts de modèles sont également séparés : les plafonds supposés donnent **0,6 USD par fiche**, soit **3,0 USD pour cinq fiches** et **7,2 USD pour douze**, sur une ligne distincte (pièce 2, § 3.1).

### Ce qui peut être différé sans contradiction logique

- L’attestation matérielle peut rester hors du périmètre initial **si** l’hôte et le fournisseur sont explicitement acceptés dans la base de confiance et si la conclusion ne prétend pas s’en affranchir.
- La redondance diverse peut être différée tant qu’aucun gain chiffré n’est revendiqué et que le verdict ne repose pas sur une prétendue indépendance de deux bacs.
- Un score statistique sophistiqué de sondage peut attendre un corpus de calibration ; en revanche, un seuil canari éliminatoire ne peut pas précéder la validation de ses contrôles et de sa fausse-alertabilité.
- L’audit extérieur peut porter après coup sur des artefacts scellés, mais toute prétention de vérification indépendante antérieure à cet audit resterait alors non démontrée.

---

## Synthèse demandée

- **Option examinée :** vérificateur sur un domaine distinct, calcul des empreintes à sa frontière, références et verdict hors du contrôle du producteur, complétés par réexécution indépendante. Attestation, diversité et canaris couvrent des propriétés additionnelles, non interchangeables.
- **Confiance :** élevée sur les distinctions conceptuelles ; moyenne sur l’architecture générale ; faible sur sa faisabilité exacte dans l’environnement servi, puisque `bwrap` réel, les scripts et les épreuves S0/S1 ne sont pas encore établis par les pièces.
- **Pire cas :** une défaillance commune de l’hôte, du fournisseur, du canal ou du vérificateur produit des empreintes cohérentes, des journaux cohérents et deux implémentations d’accord, tandis que les canaris restent silencieux.
- **Garde correspondante :** une racine de mesure et de verdict indépendante de ce domaine commun, avec fraîcheur et arrêt « non concluant » sur preuve incomplète. Elle déplace la confiance ; elle ne la supprime pas.
- **Option manquante :** pour certaines classes d’artefacts, éviter l’exécution comme source de preuve — reconstruction déterministe indépendante, ou artefact accompagné d’une preuve vérifiable par un contrôleur minimal. Cette voie déplace la difficulté vers la spécification et le contrôleur ; elle n’est pas générale.
- **Pièce qui trancherait le plus :** un rapport scellé S0/S1 réel, accompagné d’une reproduction externe de bout en bout sur cas sain et artefact. Pour la seule portée théorique d’Avalon, le PDF intégral resterait nécessaire : la pièce 4 est une lecture locale non contre-lue d’un document marqué « still training, under revision ».

## Sources extérieures

- **[S1]** *A Note on the Confinement Problem* — Butler W. Lampson, **1973**, *Communications of the ACM* 16(10). DOI : **10.1145/362248.362389**.
- **[S2]** *Reflections on Trusting Trust* — Ken Thompson, **1984**, *Communications of the ACM* 27(8). DOI : **10.1145/358198.358210**.
- **[S3]** *Countering Trusting Trust through Diverse Double-Compiling* — David A. Wheeler, **2005**, ACSAC. DOI : **10.1109/CSAC.2005.17**.
- **[S4]** *The N-Version Approach to Fault-Tolerant Software* — Algirdas Avižienis, **1985**, *IEEE Transactions on Software Engineering* SE-11(12). DOI : **10.1109/TSE.1985.231893**.
- **[S5]** *An Experimental Evaluation of the Assumption of Independence in Multiversion Programming* — John C. Knight, Nancy G. Leveson, **1986**, *IEEE Transactions on Software Engineering* SE-12(1). DOI : **10.1109/TSE.1986.6312924**.
- **[S6]** *Reproducible Builds: Increasing the Integrity of Software Supply Chains* — Chris Lamb, Stefano Zacchiroli, **2022**, *IEEE Software* 39(2). DOI : **10.1109/MS.2021.3073045**.
- **[S7]** *Remote ATtestation procedureS (RATS) Architecture* — Henk Birkholz, Dave Thaler, Michael Richardson, Ned Smith, Wei Pan, **2023**. Identifiant : **RFC 9334** ; DOI : **10.17487/RFC9334**.
- **[S8]** *Firecracker: Lightweight Virtualization for Serverless Applications* — Alexandru Agache, Marc Brooker, Alexandra Iordache, Anthony Liguori, Rolf Neugebauer, Phil Piwonka, Diana-Maria Popa, **2020**, USENIX NSDI. Identifiant : https://www.usenix.org/conference/nsdi20/presentation/agache.
- **[S9]** *Application Container Security Guide* — Murugiah Souppaya, John Morello, Karen Scarfone, **2017**. Identifiant : **NIST SP 800-190** ; DOI : **10.6028/NIST.SP.800-190**.
- **[S10]** *Reinforcement Learning from Collective Rewards* — Zarov, Course, Hartshorn, Achiron, Roche, Sinha, C. Taylor, R. Taylor, **2026**, document Avalon-M1. Identifiant local du PDF donné par la pièce 4 : SHA-256 **6429a78fab048d8a58a34fdbefe214156a02de53b6b571053c4df934f485fc58** ; citation ici indirecte, PDF non servi.