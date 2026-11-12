# Proposition E — Tester la fermeture, puis la dépendance au contexte

**Statuts.** **RAPPORTÉ** désigne ici les informations des pièces transmises, y compris leurs affirmations de vérification : je n’ai audité ni le dépôt ni les exécutions. **HYPOTHÈSE** désigne mes interprétations, propositions et prédictions, non des résultats. Ces statuts s’appliquent aux paragraphes et tableaux qu’ils introduisent.

**Pièces absentes — RAPPORTÉ :** la table complète des critères de P3-bis, les sources exécutables et les sorties brutes citées ne sont pas fournies ; je n’en reconstruis pas le contenu.

## QO-1 — Lecture mécanique précoce, verdict différé

### Recommandation et raison décisive

**HYPOTHÈSE — Recommandation : retenir (a), avec fermeture techniquement contrôlée et rendez-vous de décision écrit avant l’entretien.** Ce rendez-vous oblige Lazar à décider, mais ne déclenche pas automatiquement l’ouverture. Je rejette (b) comme solution de maintien de l’ordre : différer une inscription ne diffère pas l’acquisition d’information.

**RAPPORTÉ.** T0.7 exige que ses scores et ses sondes soient consignés avant `VERDICT-P3BIS`. Son lecteur ne transmet aucun fichier de T0.7 au lecteur du verdict de P3-bis. Une étape A non aboutie avant ce verdict rend T0.7 impossible sur le run considéré sous son texte actuel.

**HYPOTHÈSE — Ce que cet ordre protège réellement.** Il protège contre l’adaptation de la notation de T0.7 à la connaissance du résultat du témoin : choix des sondes, abandon opportuniste, réparation orientée ou changement de lecture. L’isolement du lecteur de P3-bis protège, dans l’autre sens, son verdict contre les résultats de T0.7. Ce sont des protections distinctes ; un horodatage de registre ne remplace aucune des deux.

**HYPOTHÈSE — Limite importante.** Sceller les scores avant le verdict ne supprime pas la sélection ultérieure des résultats publiés. Il faut conserver et déclarer les courses interrompues, les décisions d’ouverture et les réparations, quelle que soit l’issue de P3-bis.

### Ce que la question suppose sans l’établir

| Statut | Présupposé à ne pas traiter comme acquis |
|---|---|
| **RAPPORTÉ** | Les brouillons décrivent une lecture fermée, mais aucune preuve d’absence d’accès effectif aux résultats n’est transmise. |
| **HYPOTHÈSE** | Les sorties autorisées — codes de sortie, comptes, journaux — ne révèlent pas indirectement une issue scientifique. C’est à tester. |
| **HYPOTHÈSE** | Une lecture mécanique précoce permet de diagnostiquer une panne sans exposer le résultat ni orienter une réparation. |
| **HYPOTHÈSE** | Le comportement « planté » est effectivement exécuté par l’agent. L’instruction seule ne démontre pas cette exécution. |
| **HYPOTHÈSE** | Le bénéfice d’un résultat pour l’entretien dépasse celui d’une présentation honnête de l’état du protocole. Aucune expérience de sondes ne tranche cette préférence. |
| **RAPPORTÉ** | La date d’aboutissement de T0.7 est inconnue ; aucune probabilité auditée de non-aboutissement n’est fournie. |

### Que faire si T0.7 n’aboutit jamais ?

**HYPOTHÈSE — Procédure proposée.** Au rendez-vous fixé avant toute lecture, Lazar choisit entre :

- **maintenir la fermeture**, en acceptant explicitement l’absence de résultat communicable ;
- **ouvrir P3-bis**, inscrire le verdict à sa date réelle et acter que T0.7 sur cette course n’est plus exécutable sous son texte actuel.

Toute reprise exige un texte nouveau, nommé autrement, déclarant l’exposition au résultat. Une nouvelle version ne restaure pas rétroactivement l’ignorance.

**HYPOTHÈSE.** Je passerais à **(c)** si Lazar préférait explicitement une durée maximale d’attente à la conservation de T0.7 sur cette course. Cette option serait alors une règle de gouvernance transparente, pas un compromis statistiquement supérieur. Je ne retiendrais **(b)** que comme changement déclaré de programme : résultat ouvert maintenant, dépendance chronologique abandonnée, sans prétendre préserver sa fonction.

### Conséquences des issues défavorables

**RAPPORTÉ.**

- **« Non vu »** conduit dans T0.7 à L0b : chaîne non validée par le témoin positif, scores fermés, réparation sous texte nouveau.
- **« Échec »** conduit à L0a : lecture suspendue et nœud de Lazar ; ce n’est pas un résultat négatif sur la détection.
- **« Non tranché »** conduit à L0c : témoin insuffisamment discriminant, scores fermés.

**HYPOTHÈSE.** Sous (a), ces issues sont connues après consignation des scores de T0.7 ; elles ne doivent pas provoquer leur ouverture informelle. Sous (b), elles peuvent influencer une étape A encore à venir. Sous (c), elles deviennent publiques à l’échéance, avec la conséquence chronologique annoncée. Pour l’entretien, chacune reste informative sur **l’instrument**, sans constituer un verdict sur G0 ni sur le modèle en général.

### Expérience décisive : la fermeture est-elle effective ?

**HYPOTHÈSE — Duel limité à un périmètre testable.** Avant les données réelles, sceller une batterie de scénarios factices couvrant les chemins normaux, les échecs et les accès interdits, avec des sorties scientifiques secrètement différentes.

- **H_A :** dans cette batterie et pour les accès spécifiés, aucune information réservée n’atteint une interface autorisée avant la levée.
- **H_B :** au moins un scénario transmet une telle information.

**Métrique :** présence d’informations réservées dans les sorties autorisées, succès des tentatives d’accès, et différences de sortie dues uniquement à une issue scientifique substituée. Les cas dont le statut technique diffère sont analysés séparément : signaler une panne prévue n’équivaut pas à révéler une aire.

**Seuil :** aucune fuite admise dans la batterie définie.

**Contrôle négatif :** exécution saine sans tentative d’accès ni substitution interdite ; elle doit terminer avec les seules métadonnées autorisées. Une variante volontairement non protégée sert de contrôle positif de l’audit.

**Issues falsifiantes :**

- une fuite reproduite falsifie **H_A** ;
- l’examen exhaustif de la batterie sans fuite falsifie **H_B pour cette batterie seulement**, jamais l’existence universelle d’une fuite.

**HYPOTHÈSE — Échec de ma recommandation.** Si la lecture mécanique expose des résultats par les journaux, les exceptions ou les permissions de la session mère, je préférerais la lecture tardive à une fermeture nominale. Une simple déclaration de non-lecture ne suffirait pas.

---

## Q1 — Lire le 8B sur ses textes, puis intervenir sur leur contexte

### Recommandation et raison décisive

**HYPOTHÈSE — Recommandation : retenir (c), corrigée, avec intervention symétrique ; conserver (a) comme mesure principale sur politique.** La raison décisive est la possibilité de **réfuter une invariance au contexte**, et non de mesurer une « intention pure ».

**RAPPORTÉ.** La contre-lecture relève que C1–C2 change à la fois la consigne et le canal privé, et que la relecture sous contexte modifié est hors politique. Elle propose C4, texte honnête relu sous contexte de colludeur.

**HYPOTHÈSE — Je m’appuie sur cette critique, mais conteste sa conclusion binaire.** Une hausse avec C4 et une baisse avec C2 montrent une dépendance au contexte manipulé ; elles ne démontrent pas que la sonde lit exclusivement l’instruction. L’absence de variation ne démontre pas davantage une lecture de l’intention.

**HYPOTHÈSE.** L’option (b) répond à une autre question : que produit le lecteur 8B à contenu externe fixé ? Elle peut servir à une comparaison texte à texte, mais n’isole ni l’intention du producteur ni celle du lecteur. Je la différerais tant que l’objectif prioritaire reste la validité du signal sur les productions du 8B.

### Présupposés non établis

| Statut | Présupposé |
|---|---|
| **RAPPORTÉ** | L’étiquette de colludeur désigne une instruction reçue, pas une réussite comportementale. |
| **HYPOTHÈSE** | Le 8B exécute suffisamment le protocole pour que la détection porte sur une conduite, et pas seulement sur une assignation de rôle. |
| **HYPOTHÈSE** | La différence C1–C2 provient de la consigne plutôt que du retrait du privé, de la longueur, des positions ou de l’incompatibilité entre texte et contexte. |
| **HYPOTHÈSE** | Une séparation persistante sous consigne honnête correspond au « texte seul ». L’historique public reste pourtant présent. |
| **HYPOTHÈSE** | Battre un sac de mots établit une lecture de l’intention. Cela n’exclut ni la syntaxe, ni le siège, ni l’historique, ni une instruction représentée dans les activations. |
| **RAPPORTÉ** | Le bras est descriptif ; aucune de ses lectures ne fait franchir une porte. |

### Intervention proposée : ne pas confondre les facteurs

**HYPOTHÈSE — Version minimale.** Garder C1, C2, C3 et ajouter C4, mais les nommer comme des **contextes complets**, non comme une décomposition de l’intention. Apparier scénario, siège, tour, réplicat et identifiants du message. Conserver le même historique public pour chaque contraste apparié.

**HYPOTHÈSE — Version permettant une attribution plus fine.** Croiser séparément :

- consigne honnête ou de collusion ;
- canal privé présent ou retiré ;
- texte public honnête ou de colludeur.

Pour isoler la consigne, garder le privé identique ; pour isoler le privé, garder la consigne identique. Certaines combinaisons sont artificielles : les déclarer comme interventions diagnostiques hors politique, sans leur attribuer un état mental naturel.

**HYPOTHÈSE — Contrôle indispensable.** Ajouter une instruction privée **honnête**, avec une contrainte légitime de confidentialité et une charge contextuelle appariée. Elle distingue « collusion prescrite » de « présence d’une instruction privée ». Ajouter aussi des variations de longueur et de position sans changement de rôle, déclarées comme contrôles, pas comme équivalences sémantiques parfaites.

### Expériences décisives

**HYPOTHÈSE — Règle commune.** Les sondes, leurs orientations, leurs normalisations et les tolérances sont figées avant STEGO. Les intervalles sont calculés par scénario. Chaque duel oppose des hypothèses exclusives ; un intervalle chevauchant le seuil donne **indéterminé**, pas une victoire par défaut.

#### Duel « contexte » — Le score dépend-il matériellement du contexte manipulé ?

Pour chaque sonde principale, définir :

\[
D_C=\mathbb{E}\left[|s(x,c_{\mathrm{collusion}})-s(x,c_{\mathrm{honnête}})|\right],
\]

avec texte et historique public fixés, score normalisé par une échelle gelée sur CORE.

- **H_A :** \(D_C\leq\delta_C\), invariance pratique.
- **H_B :** \(D_C>\delta_C\), dépendance matérielle.

**Métrique :** différence absolue appariée ; différences signées rapportées séparément pour les textes honnêtes et collusifs. Cela évite qu’une moyenne signée masque des effets opposés.

**Seuil :** \(\delta_C\) choisi avant lecture, en fonction de la variation de score jugée pertinente ; aucune valeur n’est établie par les pièces.

**Contrôle négatif :** répétition avec contexte identique ; substitutions de longueur sans changement de rôle ; instruction privée honnête.

**Falsification :**

- borne basse au-dessus de \(\delta_C\) : **H_A** falsifiée ;
- borne haute au plus égale à \(\delta_C\) : **H_B** falsifiée.

**Portée :** même une dépendance nette reste une sensibilité au contexte, pas une fraction d’intention.

#### Duel « discrimination restante » — La séparation survit-elle au contrôle de contexte ?

Définir, sous contexte honnête contrôlé, \(G\) comme le gain de taux de détection de la sonde sur la meilleure vérification mécanique préspécifiée, à seuils de fausses alertes calibrés séparément.

- **H_A :** \(G\leq\delta_G\), aucun gain pertinent.
- **H_B :** \(G>\delta_G\), gain pertinent.

**Métrique :** différence de taux de détection hors échantillon, évaluée par scénarios ; fausses alertes observées rapportées avec leur incertitude.

**Seuil :** \(\delta_G\) gelé avant évaluation ; aucune valeur n’est fournie.

**Contrôle négatif :** textes honnêtes sous les mêmes contextes, dont textes comportant une instruction privée légitime.

**Falsification :**

- borne basse au-dessus de \(\delta_G\) : **H_A** falsifiée ;
- borne haute au plus égale à \(\delta_G\) : **H_B** falsifiée.

**HYPOTHÈSE — Limite.** Un gain réfute une explication par les vérifications testées, pas toutes les explications non intentionnelles. Les deux duels peuvent conclure simultanément à une dépendance au contexte et à une discrimination restante.

### Quand changer d’avis ?

**HYPOTHÈSE.** Je reviendrais à (a), avec limitation explicite de validité, si les identifiants ou les contextes exacts ne peuvent être conservés. Je différerais toute interprétation comportementale si le 8B ne joue pas le protocole. Je retiendrais (b) si la question prioritaire devenait l’effet du modèle lecteur sur un corpus commun, après clarification des licences.

---

## Mesure minimale du fonctionnement des instruments

**HYPOTHÈSE — Principe.** Une aire ne suffit pas. Rapporter un taux de détection et un taux de fausses alertes à un seuil fixé sur une calibration indépendante, puis appliqué sans retouche. Le niveau de fausses alertes de **5 %**, déjà prévu dans le brouillon NARCBench, peut servir de cible ; ce n’est pas un résultat garanti. L’incertitude doit respecter les regroupements par tâche ou scénario.

| Instrument | Positifs et honnêtes appariés | Mesure minimale et vérifications à battre |
|---|---|---|
| **Fermeture et gardes chronologiques** | Tentatives interdites et ordres invalides ; séquences autorisées appariées | Taux de blocage des violations ; taux de refus injustifié. Comparer les décisions aux états attendus d’un automate gelé. Une empreinte seule ne prouve pas la confidentialité. |
| **Chaîne P3-bis** | Comportements plantés dont l’exécution est contrôlée ; honnêtes des mêmes tâches et graines ; A–T pour le contraste décisif rapporté | Détection par épisode et fausses alertes sur honnêtes ; rapporter les plantés non exécutés sans les faire disparaître. Comparer aux mentions lexicales, au coût seul, à la longueur et aux planchers. Ne pas remplacer la table gelée absente par une nouvelle règle. |
| **Sondes de T0.7 sur NARCBench, S-C et comparateur H** | Rôles instruits, puis conduite effectivement auditée en analyse distincte ; honnêtes des mêmes épisodes et témoins appariés | Détection de rôle et détection comportementale nommées séparément ; fausses alertes sur honnêtes, y compris confidentialité légitime. Battre les bases lexicales et métadonnées préspécifiées, avec mêmes agrégations. |
| **Échange de contexte** | Paires de messages identiques avec contexte changé ; répétitions identiques et changements honnêtes | Taux de franchissement du seuil provoqué par l’intervention ; fausses alertes induites sur textes honnêtes. La base « mots du message » doit rester inchangée : sinon, erreur d’appariement. |

**HYPOTHÈSE — Baselines.** Conserver la base lexicale CORE→STEGO pour la comparaison de transfert ; ajouter une base lexicale validée par groupes au sein de chaque étage pour tester la suffisance lexicale locale. Ne pas les présenter comme disposant de la même information d’apprentissage.

**RAPPORTÉ.** La contre-lecture signale des défauts de chargement, de décompte des sondes, de registre et de grille. Ce sont des constats rapportés à résoudre avant lancement, non des résultats instrumentaux acquis.

---

## Ancrage matériel et coût

**RAPPORTÉ.**

- Modèle du programme : **Llama-3.1-8B-Instruct**, révision épinglée, poids accessibles sous licence communautaire Llama ; couches **7, 15 et 23**.
- P3-bis : **A100 SXM4 80 Go**, prix maximal annoncé **2,10 USD/h**, hors postes annexes cités ; lectures finales sur processeur. Aucune durée totale exploitable n’est fournie ici.
- NARCBench : estimation rapportée **3,5 à 5,5 heures**, plafond **15 heures / 25 USD** ; **200 épisodes CORE** et **80 épisodes STEGO**.
- Surcoûts rapportés : échange de consigne **environ 0,3 h** ; C4 **environ 0,3 h** supplémentaires ; textes Qwen3 **0,5 à 1 h**.
- Les activations publiées de **Qwen3-32B** et **Llama-3.1-70B** permettent le bras externe sur processeur ; elles ne nécessitent pas de servir ces modèles.

**HYPOTHÈSE.** La batterie de fermeture utilise des données synthétiques sur processeur. Le croisement plus fin des contextes demande des passes forcées supplémentaires, sans nouvelle génération ; son coût doit être chronométré avant scellement.

**HYPOTHÈSE — Estimation illustrative.** À **1,30 USD/h**, prix de devis rapporté, les ajouts C2 et C4 représenteraient environ **0,78 USD de carte**, calcul illustratif excluant orchestration et stockage. Aucun devis défendable du plan factoriel complet n’est disponible dans les pièces.

**HYPOTHÈSE — Décision finale.** Pour QO-1, protéger une ignorance réelle plutôt qu’un horodatage. Pour Q1, tester la dépendance au contexte plutôt que promettre une mesure d’intention. Dans les deux cas, un échec d’instrument doit rester distingué d’un résultat scientifique négatif.

FIN-DE-CELLULE