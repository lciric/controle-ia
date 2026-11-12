**Statuts.** Les contenus des propositions et des pièces sont **RAPPORTÉS**, sans audit de ma part. Mes analyses d’identifiabilité, les conditions ci-dessous et les contrôles proposés sont des **HYPOTHÈSES**, non des résultats. Les formules précisent ce que les estimateurs peuvent, ou ne peuvent pas, distinguer.

## Sur la proposition A

### (a) Défauts de méthode

- **D1 mesure une liste d’entrées, pas l’absence de canal causal.** Même si toutes les entrées de l’étape A sont classées « gelées », restent possibles l’abandon ou la relance de 7b, une réparation conditionnée au verdict, ou le choix des lignes de jeux présentes avant l’étape A. Or la pièce 2 rapporte que l’ensemble des lignes `JD/JC/JA` présentes fixe `sondes_lues` : ce choix doit lui-même entrer dans l’audit. Le contrôle négatif sur l’étape B est insuffisant : y retrouver la dépendance explicitement écrite à P3-bis ne teste pas l’exhaustivité du classement de l’étape A.
- **(b′) protège donc un ordre de registre, pas nécessairement une ignorance.** L’affirmation qu’apprendre « non vu » avant 7b et réparer « n’est pas une influence » est circulaire : c’est précisément une décision conditionnée au résultat. Elle peut être préférable pour éviter une dépense inutile, mais elle change le programme et doit être traitée comme telle. Inversement, sous (a), la chaîne n’est pas *connue* comme invalidée avant le verdict : elle est seulement mécaniquement évaluée, sans lecture.
- **Le témoin positif ne réhabilite pas directement le nul de P3.** Un « vu » peut provenir de la consigne plantée, de mentions lexicales, du coût ou d’autres corrélats de l’emplacement. Un « non vu » mélange comportement non exécuté, effet trop faible, plancher mal transporté et chaîne aveugle. Surtout, détecter un comportement planté dans P3-bis n’établit pas que le nul de P3 sur un autre organisme et une autre distribution était seulement un problème de puissance.
- **E1 confond conduite et difficulté de scénario.** « Propre » contre « non propre » varie aussi avec le scénario, les refus, la longueur, les votes et la réussite générale de l’épisode. Le contrôle honnêtes-contre-honnêtes ne supprime que les confusions communes aux deux rôles.
- **E2 n’isole pas les facteurs annoncés.** C2a peut associer consigne honnête et coordination privée collusive ; C4 change simultanément texte, consigne, privé et compatibilité texte-contexte ; C1′ change aussi la cible et la cohérence sémantique. Enfin, les hypothèses « contexte » et « texte » ne sont pas exclusives — A le reconnaît — donc E2 ne satisfait pas son propre format de duel.
- **La base de métadonnées est utile mais incomplètement spécifiée.** Sans apprentissage dans les mêmes plis, regroupement par scénario et chaîne d’agrégation identique, elle peut être soit optimiste, soit artificiellement faible.

### (b) Conditions probabilistes de perte de puissance ou de non-jugement

Soit \(S\) le scénario, \(X\) le texte, \(C\) le contexte complet, \(M\) les métadonnées, \(U\) l’indicateur « propre », \(R\) le score et \(Y\) le rôle.

- Pour tout contraste \(\Delta\) — différence d’aires ou différence appariée de scores — l’unité indépendante effective est le scénario, non le message. Si
  \[
  |\Delta|\lesssim \operatorname{SE}_{\mathrm{bloc}}(\widehat\Delta),
  \]
  l’intervalle ne permet ni détection ni invariance pratique. Un résultat dans le plancher ne falsifie une trace de conduite que si la borne haute exclut aussi les effets jugés pertinents.
- Pour E1, si \(\Pr(U=1\mid S)\) est proche de zéro ou de un dans presque tous les scénarios, le contraste apparié est non identifiable ; avec moins de dix individus dans une classe, le texte prévoit déjà « non calculable ». Si \(R\perp U\mid(C,S,M)\) mais que la loi de \(S\) diffère selon \(U\), l’aire marginale peut néanmoins dépasser le plancher : elle mesure alors une association de scénario.
- Pour E2, le contraste observé se décompose au mieux en
  \[
  \Delta_{\mathrm{obs}}
  =\Delta_{\mathrm{consigne}}+\Delta_{\mathrm{privé}}
  +\Delta_{\mathrm{position}}+\Delta_{\mathrm{incompatibilité}}
  +\text{interactions}.
  \]
  Sans restrictions supplémentaires, les cellules n’identifient que \(\Delta_{\mathrm{obs}}\). Si la loi de \(C1-C1'\) a une dispersion comparable à celle de \(C1-C2b\), elle ne fournit pas une borne suffisamment précise sur l’artefact ; si les préfixes changent les positions des jetons, l’appariement du texte ne suffit pas.
- Le plancher de P3 n’est un quantile nul transportable que si la loi nulle des scores sous NARCBench coïncide avec celle ayant servi à le calibrer. Sous changement de covariance, de normes ou de dépendance \(Y\)-\(M\), son quantile \(0{,}95\) peut être trop bas ou trop haut, sans défaut de la sonde.

### (c) Contrôles négatifs indispensables

- **QO-1 :** introduire dans un jeu factice une décision post-scellement volontairement cachée, et vérifier que D1 la détecte ; D3 doit aussi comprendre un chemin valide qui *doit passer*, pas seulement des chemins invalides qui doivent refuser.
- **P3-bis :** sans vérification indépendante de l’exécution du comportement planté, « vu » ne peut être interprété que comme détection du plantage ou de ses corrélats. H, les appariements A/T et le placebo restent nécessaires mais ne remplacent pas ce contrôle.
- **Q1 :** répétition bit à bit de chaque cellule sous contexte identique, permutation des étiquettes à l’intérieur des strates de scénario, et instruction privée honnête appariée en charge contextuelle. C1′ seul ne contrôle ni la position ni la confidentialité.

## Sur la proposition B

### (a) Défauts de méthode

- **Le déterminisme des scores est seulement conditionnel.** « Sondes figées + course terminée » ne suffit pas si les jeux effectivement lus, les relances ou la décision de consigner restent ouverts. La démonstration de H_B exige donc de figer tous ces choix, pas seulement les poids des sondes.
- **Le chiffrement proposé ne démontre pas la fermeture.** Une clé dérivée d’une entropie disponible, ou un sel inscrit au registre, peut rester accessible au même acteur. Un journal d’accès prouve au plus qu’un mécanisme de journalisation n’a pas enregistré certaines lectures ; il ne prouve ni l’absence de copie ni l’absence de lecture en mémoire. L’affirmation selon laquelle (a) ne peut créer de nœud irréversible contredit aussi son propre fusible : la levée par Lazar ferme T0.7 sur cette course.
- **Le duel consigne/texte repose sur un estimateur signé inadapté à l’invariance.** Des effets positifs et négatifs peuvent s’annuler alors que chaque score change. De plus, \(C2\) contre \(C3\) au-dessus du plancher ne falsifie pas « la consigne change le score » : contexte et texte peuvent contribuer simultanément.
- **La matrice 2×2 n’a pas les interprétations annoncées.** C4 comprend le privé : « consigne domine » et « canal privé » ne suivent donc pas des cases correspondantes. Une non-détection de C4 peut être un simple défaut de puissance ou une incompatibilité entre texte honnête et contexte de collusion.
- **Le duel sur la collusion jouée n’est pas exhaustif.** La zone intermédiaire est « partiellement jouée », et une estimation près d’un seuil peut rester indéterminée. Le taux de votes témoins « attendu ≈ 0,5 » n’est pas établi : il dépend des options et des préférences honnêtes.
- **L’inférence CORE/STEGO est trop forte.** Ne pas détecter sur STEGO n’établit pas un signal « spécifique à CORE » : changement de loi, puissance et taux de collusion jouée sont des alternatives.
- Les effectifs annoncés d’environ 200 messages par rôle sous-estiment le plan CORE, qui peut en produire davantage ; surtout, la précision reste limitée par les **50 scénarios RAPPORTÉS**, non par le nombre de messages.

### (b) Conditions probabilistes

- Pour QO-1, soit \(V\) le verdict de P3-bis, \(D\) une décision concernant T0.7 et \(I\) l’information antérieure. Il n’y a pas de canal de sélection si
  \[
  \Pr(D=d\mid V,I)=\Pr(D=d\mid I)
  \]
  pour toutes les décisions pertinentes. Une inégalité suffit à rendre l’argument « scores mécaniques » insuffisant.
- Posons \(\Delta_i=s_i(C1)-s_i(C2)\). Le test de B porte sur \(\mu=\mathbb E[\Delta_i]\). Si \(\mu=0\) mais \(\mathbb E|\Delta_i|>0\), la consigne modifie les scores sans que le critère signé ait de puissance pour le détecter.
- Pour C4, une aire vraie proche du plancher et un petit nombre de blocs indépendants laissent la borne haute trop élevée pour conclure « texte dominant ». Les deux lectures de la matrice étant multipliées par sonde, couche et jeu, le risque d’au moins une case « détectée » sous le nul n’est pas celui d’un test isolé ; la multiplicité seulement déclarée ne répare pas cette interprétation dichotomique.
- Si l’audit de propreté a sensibilité \(Se\) et spécificité \(Sp\), la proportion observée vaut approximativement
  \[
  q=Se\,p+(1-Sp)(1-p),
  \]
  où \(p\) est la proportion réellement jouée. Sans estimation de \(Se\) et \(Sp\), les seuils sur \(q\) n’identifient pas les seuils sur \(p\).
- Sur STEGO, si la base lexicale est apprise sur CORE seulement, son erreur de généralisation peut produire un gain positif de la sonde même lorsque celle-ci n’apporte aucune information interne. Le critère « au-delà des mots » devient alors non jugeable.

### (c) Contrôles négatifs indispensables

- **C3 contre C3 est potentiellement vacuous** : les mêmes scores des deux côtés donnent une aire nulle d’information par construction. Il faut une permutation d’étiquettes au niveau scénario, traversant toute la chaîne d’apprentissage, de seuil et d’agrégation.
- L’audit « propre » exige des épisodes synthétiques à issue connue, positifs et négatifs ; les votes témoins ne suffisent pas.
- Pour C1–C4 : répétition strictement identique, privé honnête et variation de longueur sans changement de rôle. Sans eux, aucune case de la matrice n’a l’interprétation causale proposée.
- Pour la fermeture : deux issues scientifiques synthétiques différentes doivent produire exactement les mêmes sorties autorisées, y compris journaux, erreurs et comptes, sous une tentative d’accès disposant des mêmes permissions que la session mère.

## Sur la proposition E

### (a) Défauts de méthode

- **Le factoriel identifie des contrastes de contextes construits, pas des parts naturelles d’intention.** Garder le même privé en changeant la consigne peut créer une contradiction ; changer le texte sous historique fixe peut créer une incompatibilité. E le déclare hors politique, mais l’expression « attribution plus fine » reste trop forte.
- **Les deux duels centraux ne testent pas la condu