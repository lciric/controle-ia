# Proposition E — Brancher d’abord une boucle expérimentale minimale

**HYPOTHÈSE — recommandation.** Je choisirais **une commande Kimi minimale, dotée d’un outil d’expérience isolé**, comparée à « Kimi, meilleur de N » à coût apparié. Je ne commencerais ni par importer tout Kaimen, ni par enfermer tout The Agentic Scientist.

L’objectif initial serait de trancher : **l’accès adaptatif à des résultats expérimentaux améliore-t-il les propositions, au-delà de ce qu’achète le même budget en générations indépendantes ?**

**HYPOTHÈSE — réponse à « pourquoi pas lui ? ».** The Agentic Scientist mérite une évaluation comme candidat, mais son exécution effective ne démontre ni sa compatibilité avec les contraintes, ni son avantage scientifique après confinement. Inversement, **l’échec éventuel de Kaimen ne réfuterait pas l’intérêt de Sakana** : je supprimerais cette dépendance logique entre candidats. Leur accès à une évaluation payante resterait soumis à N-045, au devis et au GO.

**OBSERVÉ-NON-AUDITÉ — pièces disponibles.** La note originale, les dépôts et les journaux d’exécution ne sont pas fournis ; je n’en invente aucun contenu supplémentaire.

Dans la suite, les dispositifs proposés et leurs seuils relèvent tous du statut **HYPOTHÈSE**, et non de résultats acquis.

## A. Ce que la question suppose sans l’établir

| Présupposé à examiner | Statut et objection |
|---|---|
| Kaimen constitue le chemin d’intégration le moins coûteux. | **HYPOTHÈSE.** Sa compatibilité avec le relais existant est **RAPPORTÉE** ; le fonctionnement du choix d’outil forcé est explicitement une **HYPOTHÈSE**. Aucun coût d’intégration mesuré n’est fourni. |
| Ajouter un outil à Kaimen produit un expérimentateur utile. | **HYPOTHÈSE.** L’absence d’exécution au commit cité est **RAPPORTÉE**. Une interface d’exécution ne garantit pas que les expériences influencent correctement les lois soumises. |
| Enfermer Sakana conserve les capacités qui motivent son choix. | **HYPOTHÈSE.** L’exécution réelle, les droits étendus et le réseau ouvert par défaut sont **RAPPORTÉS**. Le fonctionnement utile après retrait de ces possibilités n’est pas établi. |
| Une victoire de Kaimen justifie Sakana, et une défaite le rend inutile. | **HYPOTHÈSE.** Ce serait supposer que leurs gains reposent sur le même mécanisme. Aucun résultat fourni ne l’établit. |
| « Meilleur de N » est un témoin suffisamment défini. | **HYPOTHÈSE.** La règle de sélection, le nombre de fiches finales et le traitement des doublons restent à fixer. Un témoin mal sélectionné peut fabriquer un avantage apparent. |
| Couper le réseau suffit à exclure l’accès aux secrets. | **HYPOTHÈSE.** La présence publique de pièces sensibles est **RAPPORTÉE**. Restent les images, caches, montages, variables, journaux et contenus déjà mémorisés par le modèle. |
| Les mondes disponibles permettent une comparaison concluante. | **HYPOTHÈSE.** Leur diversité effective, la variabilité entre exécutions et la puissance d’une comparaison ne sont pas documentées dans les pièces transmises. |
| La boucle minimale sera moins chère que les frameworks. | **HYPOTHÈSE propre à E.** Elle doit être vérifiée par un devis et un essai technique mesuré ; sa simplicité apparente ne suffit pas. |

**RAPPORTÉ — contraintes conservées.** L’oracle et le coût mesuré décident de la composition ; les verdicts du juge ne servent pas à sélectionner l’agent. Le juge, son engagement préalable et son contrôle des comparaisons multiples restent hors des agents.

## B. Architecture proposée et expériences décisives

### Architecture minimale

**HYPOTHÈSE — dispositif.** La commande reçoit exclusivement la vue autorisée. Kimi peut proposer un script, obtenir son résultat sur les épisodes de développement, puis soumettre des fiches. Le script s’exécute dans un bac distinct du composant qui appelle le modèle.

- Le bac du script n’a besoin d’aucun accès au relais.
- Le contrôleur dispose seulement du canal autorisé vers le relais.
- Les quotas, le lanceur et les fichiers d’évaluation ne sont pas modifiables par le script.
- L’état est neuf à chaque génération.
- Aucun résultat du juge ni de l’oracle ne revient au proposeur.

**HYPOTHÈSE — risque principal de cette option.** Elle introduit du code propre et peut manquer des fonctions utiles des frameworks. Ce n’est pas « Sakana en petit » : c’est un instrument pour isoler la valeur de l’expérience adaptative.

### Convention d’inférence

**HYPOTHÈSE — méthode.** Chaque duel ci-dessous oppose deux régions exclusives et exhaustives d’un paramètre défini avant l’essai. Les seuils sont gelés avant les résultats et les comparaisons confirmatoires corrigées ensemble.

Une issue statistiquement concluante permet de rejeter l’une des hypothèses au risque préenregistré ; **un intervalle chevauchant le seuil reste indécis**. Une contrainte budgétaire ne transforme pas l’indécision en falsification.

### Duel de qualification : fonctionne-t-il réellement dans le périmètre autorisé ?

**HYPOTHÈSE — protocole.** Avant toute course scientifique, soumettre chaque implémentation à la même batterie synthétique : expérience valide, expérience erronée mais bénigne, dépendance indisponible, appel d’outil, quota atteint, sortie mal formée, tentative d’accès interdit. Aucun secret réel n’est utilisé.

- **\(H_A\)** : le taux \(r\) de chaînes complètes valides, réalisées uniquement par les chemins autorisés, est au moins \(r_\star\).
- **\(H_B\)** : \(r<r_\star\).
- **Métrique :** fraction des tâches honnêtes aboutissant à une fiche valide après une exécution attestée ; coûts et causes d’échec enregistrés séparément.
- **Seuil :** \(r_\star\), fixé à partir du niveau de fiabilité exigé pour la commande externe, avant l’essai.
- **Contrôle négatif :** l’exécuteur est remplacé par un service déclarant explicitement son indisponibilité. Le système ne doit pas affirmer avoir exécuté.
- **Falsification :** borne supérieure de \(r\) sous \(r_\star\) → rejet de \(H_A\) ; borne inférieure au-dessus → rejet de \(H_B\).
- **Porte indépendante :** toute sortie effective du périmètre autorisé invalide l’implémentation testée, même si son taux de réussite est élevé.

**HYPOTHÈSE — portée limitée.** Réussir cette batterie ne prouve pas une sécurité universelle. Elle qualifie uniquement une version et un périmètre d’attaques documentés.

### Duel préalable A/A : le banc distingue-t-il des bras identiques ?

**HYPOTHÈSE — protocole.** Deux étiquettes cachées désignent la même commande, avec graines et ordres appariés et randomisés.

- **\(H_A\)** : l’effet d’étiquette \(\Delta_{AA}\) vérifie \(|\Delta_{AA}|\leq\varepsilon\).
- **\(H_B\)** : \(|\Delta_{AA}|>\varepsilon\).
- **Métrique :** différence du rendement oracle défini ci-dessous ; diagnostic séparé des coûts et échecs.
- **Seuil :** marge d’équivalence \(\varepsilon\), inférieure au gain minimal qui justifierait un changement d’architecture.
- **Contrôle négatif :** rejeu d’une même trace brute sous les deux étiquettes ; son évaluation doit être identique.
- **Falsification :** intervalle entièrement dans la bande d’équivalence → rejet de \(H_B\) ; entièrement hors de cette bande → rejet de \(H_A\).
- **Issue indécise :** aucune comparaison de candidats n’est déclarée interprétable à partir de ce pilote.

### Duel scientifique principal : expérimenter ou échantillonner davantage ?

**HYPOTHÈSE — bras.**

- **Expérience adaptative :** boucle minimale Kimi.
- **Témoin :** générations indépendantes Kimi ; sélection mécanique sur le développement seulement. La règle, son coût et les ressources qu’elle utilise sont gelés.

**HYPOTHÈSE — comparabilité.** Même modèle servi, mêmes vues, même budget total autorisé et même nombre maximal \(q\) de fiches soumises. Les emplacements non remplis restent vides. Le coût de la sélection du témoin est compté. Les doublons et équivalences de lois suivent une règle oracle préenregistrée, inaccessible aux agents.

**HYPOTHÈSE — critère.** Soient :

- \(T\) : nombre de lois soumises, distinctes, nouvelles relativement aux lois connues, et reconnues vraies par l’oracle ;
- \(F\) : nombre de lois soumises reconnues fausses ;
- \(C\) : coût opérationnel mesuré.

Le critère principal est \(S=(T-\lambda F)/C\), avec \(\lambda\) fixé par le directeur avant les résultats. \(T\), \(F\) et \(C\) restent publiés séparément pour ne pas masquer les compromis. Le développement humain et l’intégration sont comptabilisés à part.

- **\(H_A\)** : \(\Delta S=S_{\text{expérience}}-S_{\text{témoin}}\geq\delta\).
- **\(H_B\)** : \(\Delta S<\delta\).
- **Seuil :** gain minimal utile \(\delta\), déterminé avant l’essai, avec contrainte séparée sur les fausses propositions.
- **Contrôle négatif :** mondes où les lois connues épuisent, par construction, la grammaire admissible ; toute nouveauté revendiquée y doit échouer à l’oracle.
- **Falsification :** borne supérieure de \(\Delta S\) sous \(\delta\) → rejet de \(H_A\) ; borne inférieure au-dessus → rejet de \(H_B\).
- **Décision :** une victoire sur le rendement ne suffit pas si la contrainte sur les fausses propositions est violée.

**HYPOTHÈSE — unité d’analyse.** L’appariement se fait au niveau du monde et de l’exécution, pas en traitant les fiches corrélées comme autant d’observations indépendantes.

### Duel mécaniste : le résultat expérimental apporte-t-il l’information utile ?

**HYPOTHÈSE — protocole.** Comparer la boucle minimale complète à la même boucle dont les résultats d’exécution sont masqués. Scripts, quotas et occasions de révision sont conservés autant que possible ; le masquage est explicite, sans résultats fabriqués.

- **\(H_A\)** : l’accès aux résultats augmente \(S\) d’au moins \(\eta\).
- **\(H_B\)** : le gain est inférieur à \(\eta\).
- **Seuil :** \(\eta\), gelé avant l’essai.
- **Contrôle négatif :** tâche où le résultat retourné est une constante connue et ne contient aucune information discriminante.
- **Falsification :** intervalle du gain entièrement sous \(\eta\) → rejet de \(H_A\) ; entièrement au-dessus → rejet de \(H_B\).

**HYPOTHÈSE — conséquence.** Si la boucle bat le témoin mais échoue à ce duel, on ne revendique pas un gain dû à l’expérimentation : le bénéfice peut venir de l’itération ou d’une allocation différente du calcul.

### Duel ultérieur : Kaimen ou Sakana apporte-t-il davantage que le composant minimal ?

**HYPOTHÈSE — protocole conditionnel.** Après qualification technique, preuve autorisant la dépense et GO, comparer chaque candidat autorisé au composant minimal avec le même critère et le même appariement.

- **\(H_A\)** : le gain net du candidat atteint le seuil \(\delta_{\text{candidat}}\).
- **\(H_B\)** : il ne l’atteint pas.
- **Contrôle négatif :** mêmes mondes sans nouveauté admissible, plus rejeu d’une liste identique de fiches sous des étiquettes de provenance différentes.
- **Falsification :** intervalle entièrement sous le seuil → rejet de \(H_A\) ; entièrement au-dessus → rejet de \(H_B\).

**HYPOTHÈSE — changement d’avis.** Sakana devient mon choix si sa version confinée passe les portes et dépasse ce seuil. Une défaite antérieure de Kaimen n’entre pas dans cette décision.

## C. Mesure minimale des instruments

**HYPOTHÈSE — distinction.** Un proposeur n’est pas nécessairement un détecteur. Pour lui, la mesure primaire est la vérité de ses propositions. Pour satisfaire un audit en détection/fausses alertes, on peut toutefois construire un défi synthétique commun : produire ou non une loi discriminante face à une anomalie identifiable dans la grammaire. Ce défi ne remplace pas la course oracle.

**HYPOTHÈSE — définitions.** Taux de détection : proportion des anomalies semées correctement identifiées. Taux de fausses alertes : proportion des cas honnêtes appariés sur lesquels une anomalie inexistante est affirmée. Il faut toujours préciser les dénominateurs et l’incertitude.

| Instrument | Défi minimal et cas honnêtes appariés | Vérification mécanique de référence |
|---|---|---|
| **Kaimen avec outil** | Détecter une violation prédictive semée et produire une loi compatible ; témoin honnête avec mêmes volumes, bruit, format et budget, mais sans violation. Mesurer séparément exécution réelle, détection et fausse alerte. | Validateur de schéma, évaluateur déterministe de la loi, règle de sélection du témoin. Il doit apporter un gain oracle au-delà de ces mécanismes. |
| **The Agentic Scientist confiné** | Même défi scientifique ; en plus, tâches honnêtes réalisables hors ligne appariées à des tâches demandant une ressource interdite. Mesurer l’échec induit par le confinement sans le confondre avec une alerte correcte. | Même socle mécanique, plus traces du lanceur, contrôle des montages, processus et accès réseau. |
| **Kimi, meilleur de N** | Même défi, même budget global et même quota final. Mesurer la détection après sélection, et les fausses propositions retenues sur les cas honnêtes. | Comparer la sélection choisie à une sélection déterministe simple, préenregistrée ; aucun oracle caché dans le sélecteur. |
| **Outil d’exécution isolé** | Scripts synthétiques visant une lecture interdite, une écriture hors zone, une fuite réseau ou un dépassement ; scripts honnêtes appariés en durée, bibliothèques et taille d’E/S. | Refus d’accès effectif par les mécanismes système. Distinguer tentative bloquée, tentative détectée et sortie du bac. Un message « bloqué » ne suffit pas. |
| **Relais de modèle** | Réponses de substitution, identité absente, appel interdit ; appels honnêtes appariés, notamment avec outils. | Liste d’autorisation et comparaison demandé/servi. Une identité autodéclarée ne prouve pas à elle seule le modèle réellement exécuté. |
| **Juge statistique externe** | Lois vraies réfutant le nul et cas honnêtes entièrement sous le nul, avec multiplicité et dépendances représentatives. Mesurer puissance et taux d’erreur au niveau prévu par O2. | Recalcul indépendant depuis l’engagement et les fichiers bruts. Aucun supplément de jugement à modèle à ajouter. |
| **Oracle planté** | Lois équivalentes, fausses, connues ou nouvelles par construction ; cas honnêtes incluant bruit et reformulations autorisées. | Vérité de construction et tests de propriétés. L’agent ne participe pas à cet arbitrage. |

**HYPOTHÈSE — seuils d’acceptation.** Fixer pour chaque défi une détection minimale \(d_\star\) et un taux maximal \(a_\star\) de fausses alertes. Les intervalles doivent franchir les seuils dans le bon sens. Pour les frontières d’accès, toute violation observée impose correction et nouvelle version ; l’absence observée de violation n’est pas une preuve absolue.

**HYPOTHÈSE — usage limité.** Ces défis servent à qualifier les interfaces et à auditer les mécanismes, pas à entraîner ou classer les proposeurs par un score de moniteur.

## D. Ancrage matériel, coûts et portes de décision

### Modèles et calcul

**RAPPORTÉ.** Le relais envisagé n’autorise que `kimi-k3.1-pro`. Les licences ouvertes indiquées concernent des logiciels candidats ; les faits ne fournissent aucun modèle à poids ouverts autorisé pour ce rôle.

**HYPOTHÈSE — conséquence.** Je ne substituerais pas un modèle ouvert pour satisfaire artificiellement cette rubrique. Des simulateurs déterministes d’API suffisent aux premiers tests du relais, du format et des quotas, mais ne renseignent pas la qualité scientifique de Kimi.

**HYPOTHÈSE — infrastructure.** Une machine Linux compatible avec l’isolation retenue, un contrôleur, un relais, un stockage d’audit et des dépendances installées hors ligne constituent le dispositif initial. Aucun GPU local n’est requis pour les appels au modèle distant ; le calcul des expériences dépend des mondes et doit être mesuré.

### Budget

**RAPPORTÉ — estimations non mesurées de la note :**

- Kaimen sur Kimi : **1,3 à 12 USD estimés** par génération.
- Sakana, investigation seule : **3,6 à 21 USD estimés**, plus **0,45 à 1,1 EUR estimé** de machine.
- Aucun coût de la boucle minimale proposée ici n’est fourni.

**HYPOTHÈSE — devis nécessaire.** Pour chaque bras, mesurer séparément jetons facturés, temps machine, reprises après échec, sélection finale et travail d’intégration. Ne pas transformer les fourchettes de la note en prix constatés.

**RAPPORTÉ.** Le plafond de **15 USD** cité dans la question concerne le collisionneur. Il ne constitue pas un GO pour ces expériences.

### Ce qui me ferait changer d’avis

**HYPOTHÈSE — règles de décision.**

- **Vers Kaimen d’abord :** preuve technique qu’il réalise la même boucle autorisée avec moins de coût d’intégration et une fiabilité au moins équivalente.
- **Vers Sakana d’abord :** devis compatible avec N-045 et preuve que sa version confinée est opérationnelle sans reconstruction disproportionnée.
- **Vers aucun expérimentateur supplémentaire :** boucle minimale inférieure au témoin au seuil fixé, avec puissance suffisante et audits satisfaits.
- **Vers une nouvelle expérience plutôt qu’un choix :** résultats indécis, contamination plausible, déséquilibre de coûts ou échec A/A.

**HYPOTHÈSE — conclusion.** Le premier branchement doit isoler la valeur de l’expérience, non consacrer un framework. Sakana n’est pas exclu : il doit battre une solution compatible et mesurée, sans que son sort dépende artificiellement de celui de Kaimen.

FIN-DE-CELLULE