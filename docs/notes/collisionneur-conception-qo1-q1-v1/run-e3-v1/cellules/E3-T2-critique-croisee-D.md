**Statuts.** Tout ce qui provient des pièces, y compris leurs déclarations de vérification, est traité comme **RAPPORTÉ** ; je n’ai audité ni dépôt ni exécution. Mes analyses sont des **HYPOTHÈSES** méthodologiques, non des résultats. Je ne propose pas de nouvelle expérience décisive : les contrôles ci-dessous sont ceux qui conditionnent la validité des duels reçus.

## Sur la proposition A

### (a) Défauts de méthode

1. **D1 ne teste pas le canal qui décide sa recommandation.** L’audit classe les *entrées* de l’étape A, mais pas les décisions de lancer, abandonner, relancer, réparer ou publier une course. Même si toutes les entrées sont gelées et si les scores sont une fonction déterministe de données figées, connaître le verdict de P3-bis peut modifier la disponibilité et la sélection des résultats de T0.7. Le contrôle positif sur l’étape B vérifie seulement que l’auditeur sait repérer une entrée déjà nommée, pas que son inventaire est exhaustif.

2. **La recommandation (b′) repose donc sur une implication non démontrée** : « aucune entrée humaine » n’implique pas « `SCELLEMENT-T07` suffit ». A affirme ensuite qu’un « non vu » connu tôt permettrait de réparer avant de payer 7b. C’est précisément une décision conditionnée par le résultat, que D1 ne mesure pas. Elle peut être souhaitable pour économiser une course, mais elle contredit l’affirmation selon laquelle la date de connaissance ne change rien au rapport avec T0.7.

3. **E1 conditionne sur une variable post-instruction.** « Épisode propre » dépend de messages, votes et drapeaux produits après la consigne. La comparaison propre/non propre mêle donc conduite, difficulté du scénario, obéissance générale, longueur et déroulement de l’épisode. Les deux hypothèses ne sont pas exclusives : une sonde peut lire à la fois la réception de la consigne et quelque chose associé à la collusion jouée. Un résultat nul ne falsifie que sa détectabilité à la puissance atteinte.

4. **C1′ n’est pas un contrôle pur de l’artefact de préfixe.** Changer de scénario change aussi la cible, le contenu sémantique et le canal privé. C2a peut créer un contexte incohérent — consigne honnête avec coordination privée conservée — dont l’effet n’est pas nécessairement celui de la consigne seule. Les contrastes proposés estiment des effets de **contextes complets** sur le score, pas des parts de consigne, de texte ou d’intention.

5. **Fuite d’apprentissage possible dans E1/E2.** Pour S-C, H et les bases apprises sur CORE, A ne précise pas que les messages analysés doivent être notés hors pli, avec sélection de la sonde et de la base sur des groupes disjoints. Les relectures d’un même message ne créent pas de nouvelles unités indépendantes. La base de métadonnées ajoutée par A doit suivre les mêmes plis et la même agrégation, sans quoi elle sera optimistement ou pessimistement biaisée.

### (b) Conditions probabilistes de perte de puissance ou de non-jugeabilité

- **Sélection de T0.7.** Soit \(V\) le verdict de P3-bis, \(L\) l’indicateur de lancement/aboutissement et \(Y\) une issue de T0.7. Si \(P(L=1\mid V)\) dépend de \(V\), et si \(V\) et \(Y\) partagent une qualité instrumentale latente, alors  
  \[
  \mathbb E[Y\mid L=1]\neq \mathbb E[Y].
  \]
  Les \(Y\) des courses non lancées ne sont pas identifiables sans hypothèse de sélection. Le décompte D1 des entrées gelées n’estime ni \(P(L\mid V)\), ni \(P(\text{relance}\mid V)\), ni \(P(\text{publication}\mid V)\).

- **PB-1/PB-2 et transport de puissance.** La puissance calculée sur P3 ne se transporte que si persistent la loi du plancher, son quantile, la variance des estimateurs et la dépendance intra-tâche. Si le coefficient de corrélation intra-scénario tend vers un, le nombre effectif d’unités tend vers le nombre de scénarios, non vers le nombre de messages. Une erreur type calculée au niveau message sous-estime alors la variance et les intervalles deviennent trop étroits.

- **E1.** Un contraste apparié par scénario exige une positivité locale : \(0<P(\text{propre}\mid G=g)<1\) pour suffisamment de scénarios. Si chaque scénario est presque toujours propre ou presque toujours non propre, le contraste intra-scénario est non estimable, même avec dix positifs et dix négatifs au total. Des erreurs de classification de l’audit « propre » peuvent en outre atténuer l’aire jusqu’au plancher.

- **E2.** La règle « borne basse de l’effet au-dessus de la borne haute de l’artefact » perd sa puissance lorsque la variance de l’estimateur de \(C1-C1'\) est grande : presque aucun effet réel ne peut alors franchir le critère. Sous une sonde en maximum, si les longueurs \(L\) diffèrent selon le rôle, des jetons de même loi marginale produisent néanmoins des maxima de lois différentes ; l’aire peut donc s’écarter de \(0{,}5\) sans signal comportemental. Le plancher ne corrige ce phénomène que s’il reproduit la loi de longueur et d’agrégation du jeu effectivement évalué.

### (c) Contrôles négatifs indispensables

- Pour **D1/(b′)** : deux verdicts synthétiques substitués à entrées figées, avec enregistrement des lancements, abandons, relances et publications. Le jouet de registre proposé ne contrôle que la garde, pas cette sélection.
- Pour **E1/E2** : scores hors pli par domaine ; permutations d’étiquettes à l’intérieur de strates scénario–longueur–siège–tour ; répétition à contexte strictement identique ; invariance obligatoire de la base des mots quand le texte est inchangé.
- Pour attribuer un effet à la **consigne plutôt qu’au préfixe** : un préfixe témoin ne changeant ni rôle ni contenu privé, avec positions contrôlées. C1′, en l’état, ne remplit pas cette fonction.

## Sur la proposition B

### (a) Défauts de méthode

1. **B identifie le bon canal, puis emploie un critère qui ne le teste pas.** Après avoir repéré la décision de lancer l’étape A, il déclare que figer toutes les entrées falsifierait \(H_B\). Cela ne fige ni le lancement, ni l’abandon, ni la relance. Sa recommandation (a) repose ainsi sur un scénario jugé plausible, non sur le duel annoncé.

2. **L’asymétrie entre (a) et (c) est mal établie.** Sous (a), le mot du directeur peut également rendre T0.7 impossible sur 7b ; sa traçabilité ne le rend pas réversible. Le chiffrement proposé ne garantit pas la confidentialité si la session mère possède l’entropie, la clé ou les droits suffisants. Un journal d’accès ne prouve pas la non-lecture : copie, accès privilégié et journalisation incomplète restent possibles.

3. **La matrice 2×2 de Q1 n’identifie pas ses trois facteurs.** \(C1-C2\) change consigne et privé ; \(C4-C3\) change aussi le texte, l’épisode et l’historique. « Non détecté » n’est pas « absent ». La cellule « texte domine » peut donc résulter d’un manque de puissance sur C4, et celle « canal privé » peut provenir d’une interaction consigne–texte. Les issues censées falsifier \(H_B\) ne le font pas : un effet du texte et un effet de la consigne peuvent coexister. Cela viole l’exigence d’hypothèses exclusives.

4. **Le duel sur la collusion jouée laisse un troisième état.** Les hypothèses \(\geq 0{,}5\) et \(<0{,}2\) ne couvrent pas la zone intermédiaire, pourtant prévue par le brouillon. L’espérance de votes cible « au hasard » dans les témoins n’est pas établie et dépend des options de chaque scénario.

5. **La base des mots reste insuffisamment spécifiée.** Sans la correction par étage et par plis demandée dans la contre-lecture, « au-delà des mots » sur STEGO peut être vrai par construction : une base entraînée sur CORE peut simplement mal transférer.

### (b) Conditions probabilistes de perte de puissance ou de non-jugeabilité

- **Fermeture.** Si \(V\) est l’issue scientifique et \(O\) les sorties autorisées, une confidentialité probabiliste exige \(O\perp V\). Dès que les lois des codes, comptes ou durées diffèrent selon \(V\), un classifieur peut obtenir une aire supérieure à \(0{,}5\), même sans ouverture du fichier. Zéro incident dans une batterie finie ne borne pas ce risque hors de son support.

- **Matrice 2×2.** Lorsque les intervalles des trois aires et de \(C1-C2\) couvrent simultanément les effets nuls et les effets pertinents, les quadrants ne sont pas identifiables. Les intervalles calculés au niveau message deviennent trop optimistes si la dépendance intra-scénario est forte.

- **Proportion d’épisodes propres.** Si l’intervalle de \(\hat p\), estimé avec regroupement par scénario, contient les deux seuils, aucun des deux états du duel n’est tranché. Le taux de votes attendu sous le nul doit être \(\pi_g=P(\text{vote cible}\mid G=g,\text{témoin})\), non une constante supposée ; s’il varie fortement entre scénarios, une moyenne non appariée confond scénario et collusion.

- **Détection à fausses alertes fixées.** Si le nombre effectif de négatifs indépendants est inférieur à la résolution nécessaire au quantile de calibration, le seuil est dominé par un maximum empirique et les taux de détection ont une variance trop grande pour le duel.

### (c) Contrôles négatifs indispensables

- Une tentative réelle de lecture par copie et par utilisateur privilégié, accompagnée d’une substitution du résultat dans les journaux et les durées ; sans elle, ni chiffrement ni journal ne valident la fermeture.
- Une cellule maintenant le privé constant pour isoler la consigne, et une comparaison de C4 à des textes honnêtes du **même épisode et du même historique**, pas seulement à C3. Le contrôle C3 contre C3 ne suffit pas.
- Une base lexicale et une base de métadonnées évaluées hors pli, avec la même chaîne d’agrégation ; sans elles, « lecture interne » et la matrice consigne/privé/texte sont non jugeables.

## Sur la proposition C

Pièce C absente, statut « jamais lancée » ; je n’en invente ni ne critique le contenu.

## Sur la proposition E

### (a) Défauts de méthode

1. **La batterie de fermeture mesure surtout des fuites littérales.** « Présence d’informations réservées » ne suffit pas : une sortie peut ne contenir aucun nombre scientifique tout en modifiant la probabilité a posteriori du verdict. Le contrôle positif volontairement non protégé éprouve la détection d’une fuite grossière, pas nécessairement celles des exceptions, comptes ou temps d’exécution.

2. **La portée de l’ignorance préservée reste sous-spécifiée.** La batterie est honnêtement limitée à ses scénarios, mais la recommandation QO-1 porte sur le déploiement réel. Elle ne teste pas non plus la politique de lancement, de relance et de publication après ouverture. Le rendez-vous de décision est une règle de gouvernance, pas une garantie statistique contre la sélection.

3. **Le plan factoriel ne transforme pas les scores en états mentaux.** E le reconnaît, mais ses phrases de « discrimination restante » restent vulnérables à l’historique public, au scénario et à l’origine du texte. Une consigne honnête associée à un privé de collusion, ou un texte honnête placé dans un historique de collusion, mesure une intervention artificielle sur le lecteur ; ce n’est pas une observation naturelle de conduite.

4. **Les deux seuils \(\delta_C,\delta_G\) ne sont pas encore opérationnels.** Sans règle gelée indépendante des résultats, ils peuvent être choisis de façon à rendre les duels faciles ou impossibles. « La meilleure vérification mécanique préspécifiée » introduit aussi une sélection : si ce choix et l’évaluation utilisent les mêmes groupes, le gain estimé subit un biais du vainqueur.

5. **\(D_C\) n’est pas une mesure de perte ou de gain de détection.** Une translation commune des scores sous un nouveau contexte peut produire une grande différence absolue appariée tout en laissant l’aire et le taux de détection inchangés.

### (b) Conditions probabilistes de perte de puissance ou de non-jugeabilité

- **Fermeture.** Le paramètre pertinent est la distinguishabilité des lois \(P(O\mid V=v)\), par exemple l’aire d’un prédicteur de \(V\) fondé sur \(O\), ou une information mutuelle \(I(V;O)\). Si la batterie contient \(N\) essais indépendants et qu’une fuite survient avec probabilité \(p\), zéro fuite observée a encore probabilité \((1-p)^N\) : cela n’exclut pas les fuites rares. Un estimateur d’information mutuelle sur petit échantillon est en outre biaisé sans correction et protocole de calibration.

- **Duel \(D_C\).** Si l’échelle de normalisation estimée sur CORE est proche de zéro, instable entre domaines ou calculée avec les données d’évaluation, \(D_C\) devient respectivement explosive, non transportable ou optimiste. Si quelques scénarios concentrent les grandes variations, la moyenne appariée peut être positive alors que la médiane des effets par scénario est nulle ; une conclusion globale serait alors non représentative des scénarios.

- **Duel \(G\).** Si la sélection de la meilleure base, la calibration des seuils et l’estimation de \(G\) partagent les mêmes groupes, \(\widehat G\) est biaisé positivement. Si le nombre effectif de négatifs après regroupement est trop faible pour estimer le quantile de fausses alertes, les deux taux de détection deviennent instables et les intervalles peuvent couvrir toute la zone décisionnelle.

- **Discrimination sous contexte contrôlé.** Sans recouvrement des distributions de longueur, siège, historique et scénario entre classes, l’estimateur de \(G\) mesure un mélange de transport hors support et de signal résiduel. Les contrôles de métadonnées réduisent ce problème uniquement pour les variables effectivement modélisées.

### (c) Contrôles négatifs indispensables

- Pour la fermeture : une substitution du verdict qui conserve artificiellement fichiers et messages littéraux, mais fait varier comptes, exceptions et durées, afin de tester les fuites distributionnelles ; une variante de fuite subtile doit servir de contrôle positif, pas seulement la variante totalement non protégée.
- Pour P3-bis : des épisodes avec **instruction plantée mais comportement non exécuté**, rapportés séparément. Sans eux, un positif peut valider la lecture de la consigne ou du texte plutôt que celle du comportement.
- Pour \(G\) : sélection des bases, calibration et évaluation sur groupes disjoints, plus permutations de rôle à l’intérieur de strates scénario–longueur–siège–tour. Les contrôles déjà proposés par E — contexte identique, privé honnête, invariance lexicale — sont nécessaires mais ne remplacent pas ceux-ci.

**Conséquence méthodologique.** Sur QO-1, ni la déterminité des scores ni l’inventaire des entrées ne suffisent : le paramètre vulnérable est la politique de lancement, de relance et de publication conditionnée par \(V\). Sur Q1, les cellules peuvent estimer des effets d’interventions contextuelles sur un score ; la matrice de B et les interprétations causales de A ne permettent pas d’en déduire des parts d’« intention ».

FIN-DE-CELLULE