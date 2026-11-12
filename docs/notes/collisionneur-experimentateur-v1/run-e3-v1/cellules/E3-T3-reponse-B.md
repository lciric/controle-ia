# Proposition B — Tour III.3 : réponse aux critiques

---

## (a) Réponse à chaque critique adressée à B

J'organise les critiques par source (A, C, E), en les numérotant telles qu'elles apparaissent dans les pièces reçues.

---

### Critiques de A

**A-1. Le juge entre dans le critère de comparaison (exp. 4 et 5) — violation de N-058.**

**Acceptée.** C'est le défaut le plus grave de mon dessin initial. J'avais défini « vraie découverte » comme « loi *promue* dont l'oracle confirme la vérité ». Or N-058 (RAPPORTÉ) est explicite : la composition des proposeurs se juge sur l'oracle et le coût, *jamais* sur le verdict du juge. Conditionner à la promotion fait entrer le juge dans la sélection du bras. A a raison de noter que la puissance du juge dépend de la multiplicité, donc du bras — créant un confondant. **Correction :** la métrique primaire porte désormais sur les fiches *soumises*, évaluées directement par l'oracle, sans conditionnement à la promotion. Les promotions deviennent un diagnostic séparé, non décisif pour le choix du bras. Voir exp. 4 corrigée ci-dessous.

**A-2. Exp. 4 et 5 : deux tests sur les mêmes runs sans correction.**

**Acceptée.** Deux hypothèses testées sur le même jeu de données sans correction de multiplicité gonflent l'erreur de type I globale. **Correction :** exp. 5 est fusionnée dans exp. 4 comme critère secondaire (voir dessin corrigé), et les deux critères sont déclarés dans le préenregistrement avec une correction (Bonferroni sur 2 critères, ou un critère composite unique — voir exp. 4 corrigée).

**A-3. Exp. 5 n'est pas en inférence forte (B4).**

**Acceptée.** « Pas significativement supérieur » n'est pas falsifiable par l'absence de signification. Il manque une marge de non-infériorité. **Correction :** le critère secondaire de fausses découvertes est reformulé comme un test de non-infériorité avec marge gelée Δ_F (voir exp. 4 corrigée).

**A-4. A/A avec « même graine fixée » sous-estime la variance.**

**Acceptée.** Si la graine locale fixe tout sauf la stochasticité du modèle distant, le pilote mesure une variance tronquée. **Correction :** le pilote A/A utilise des graines *différentes* entre les deux runs, de sorte que les tirages locaux (épisodes, ordres) diffèrent aussi. Cela capture la variance opérationnelle réelle.

**A-5. Contrôle négatif de l'exp. 3 réglable à volonté.**

**Acceptée.** Le « proposeur avec consigne dégradée » est un choix de l'expérimentateur, donc le contrôle réussit par construction. **Correction :** la dégradation est fixée mécaniquement et préenregistrée : retirer une fraction gelée ρ (illustratif : ρ = 50 %) des épisodes de développement fournis au proposeur. Aucun ajustement post hoc.

**A-6. Contrôle négatif de l'exp. 1 teste la barrière, pas l'appel de fonctions.**

**Acceptée.** Un modèle interdit est bloqué par la liste d'autorisation, quel que soit le support de l'appel de fonctions. Le contrôle ne vérifie pas ce qu'on veut savoir (compatibilité fonctionnelle). **Correction :** le contrôle négatif est remplacé par une requête portant le bon modèle (`kimi-k3.1-pro`) mais avec un schéma d'outil *intentionnellement malformé* (nom d'outil absent du registre). Le relais doit laisser passer la requête (bon modèle), mais le modèle doit échouer à appeler l'outil — vérifiant ainsi que le test de compatibilité mord réellement sur l'appel de fonctions.

**A-7. Contrôle négatif de l'exp. 2 (pont coupé) mesure la dépendance au relais, pas l'enfermement.**

**Acceptée.** Qu'un agent échoue sans relais prouve qu'il a besoin du modèle, pas que le réseau est fermé. **Correction :** le contrôle négatif est : agent avec pont actif, consigne qui exige de télécharger une URL externe ; l'accès doit échouer *et* être tracé dans les journaux réseau du bac (iptables log ou équivalent `bwrap`).

**A-8. Instrument 5 : monotonie n'est pas un critère de validité.**

**Acceptée.** La non-monotonie de score(N) lu sur l'oracle est un résultat (sur-ajustement du sélecteur), pas un défaut de la règle. Et N=1 = proposeur seul est vrai par construction. **Correction :** le test de l'instrument 5 est remplacé par une vérification que le sélecteur mécanique bat le tirage aléatoire de M parmi N (proposition retenue de A ; je m'en sers). Si le sélecteur ne bat pas le tirage, il est mort et le témoin n'a pas de sens.

**A-9. Confondant principal non fixé : la multiplicité.**

**Transformée en test.** La règle de multiplicité est préenregistrée dans le dessin corrigé : les deux bras soumettent exactement q fiches, q gelé. Le témoin utilise son sélecteur mécanique pour choisir q parmi N ; le scientifique soumet ses q meilleures selon son classement interne. Cela contrôle la multiplicité mais confond la qualité de la sélection — point identifié par C (C-1) que je traite plus bas.

---

### Critiques de C

**C-1. Violation de N-058 et O2 dans exp. 4 et 5 (même que A-1).**

**Acceptée** — voir réponse à A-1.

**C-2. Confusion entre erreur du juge et erreur du proposeur dans exp. 5.**

**Acceptée en partie.** C a raison que la vue servie ne contient pas le verdict du juge, donc le proposeur ne peut pas « optimiser ce que le juge accepte » au sens strict. Mon attribution à « Goodhart via la boucle expérimentale » était trop forte. **Cependant**, le mécanisme par lequel un scientifique qui exécute des expériences sur les épisodes de développement produit des lois qui collent mieux à l'échantillon (et donc passent plus facilement un juge fondé sur le même échantillon) reste une possibilité — c'est du sur-ajustement classique, pas une attaque stratégique. **Correction :** le critère secondaire est reformulé comme « taux de fausses soumissions (fiches soumises dont l'oracle dit qu'elles sont fausses) » — sans conditionnement à la promotion. L'attribution causale à un mécanisme particulier est retirée ; seul le taux observable est mesuré.

**C-3. Contradiction de l'instrument 3 (pont prise Unix dans `bwrap` donne accès au LLM au code exécuté).**

**Acceptée.** C'est une erreur d'architecture dans mon dessin. Dans l'option (a), le superviseur Kaimen appelle le relais ; seul l'outil « expérience » exécute du code dans `bwrap`. Si le code dans `bwrap` peut atteindre le relais Kimi via la prise Unix, le script généré par le modèle peut appeler le LLM en boucle fermée, contournant les plafonds et faussant la mesure. **Correction :** le pont prise Unix n'est *pas* monté dans le bac `bwrap` de l'option (a). Le code dans le bac n'a accès à aucun réseau ni à aucune prise. Le pont n'est nécessaire que pour l'option (b) (The Agentic Scientist), où l'agent lui-même a besoin d'appeler le modèle. Pour (a), le superviseur Kaimen tourne *hors* du bac et appelle le relais normalement ; seuls les scripts d'expérience sont exécutés dans le bac, sans accès au relais.

**C-4. Instrument 5 : score par dollar décroissant par construction.**

**Acceptée.** Si le score est V/C(N) et que V sature (le monde a un nombre fini de lois vraies), V/C décroît avec N par construction. Mon test de monotonie était mal spécifié. **Correction :** l'instrument 5 est redéfini (voir A-8 ci-dessus) : le sélecteur mécanique est comparé au tirage aléatoire, pas testé pour la monotonie.

**C-5. Sous-alimentation de l'exp. 4 sur M = 3 mondes — impossibilité mathématique.**

**Acceptée.** C démontre que pour M = 3 paires, la plus petite p-value unilatérale d'un test non paramétrique est (1/2)³ = 0,125 > 0,05. Il est *mathématiquement impossible* de rejeter au seuil 0,05 avec 3 mondes en non paramétrique. Même avec un test t à 2 ddl, la puissance est faible. **Correction :** le nombre de mondes M est déterminé par un calcul de puissance préenregistré, fondé sur la variance estimée du pilote A/A (exp. 3). Le calcul de puissance fixe M tel que la probabilité de rejeter sous l'effet minimal δ dépasse 0,80 (illustratif). Si le M requis dépasse le budget, c'est une issue légitime : « non jugeable à ce budget ». Je ne fixe plus M = 3 par défaut.

**C-6. Seuil binomial de l'exp. 2 (n = 5 ne sépare pas p = 0,50 de p = 0,70).**

**Acceptée.** La démonstration de C est correcte. **Correction :** n est augmenté selon un calcul de puissance. Pour séparer p = 0,70 de p = 0,50 au risque 0,05, il faut environ n ≥ 25 essais (illustratif, test binomial exact). Si le coût de 25 runs d'investigation dépasse le budget, cette exp. est reportée et (b) est déclarée « faisabilité non établie ».

**C-7. Contrôle négatif d'exécution fantôme (exp. 1) : le superviseur peut ignorer l'outil.**

**Transformée en test.** Le contrôle proposé par C (jeton secret du noyau que le superviseur doit inclure dans son journal) est un bon test de l'utilisation réelle de l'outil. **Ajout :** chaque appel de l'outil « expérience » injecte un nonce aléatoire dans la réponse ; le journal d'audit du superviseur est vérifié pour la présence de ce nonce. Si absent, la boucle est comptée comme échouée.

**C-8. Contrôle négatif d'exfiltration par encodage (instrument 4) : `grep -F` trop faible.**

**Acceptée.** Un `grep -F` ne couvre que la chaîne exacte. **Correction :** la garde inclut au minimum : chaîne exacte, chaîne avec espaces normalisés, variables renommées selon un dictionnaire gelé de synonymes, et encodage base64. Le plancher est ce `grep` élargi ; la garde complète (embeddings sémantiques) est un second temps, mentionné mais non requis pour la porte.

**C-9. Contrôle négatif de monde nul (sans loi nouvelle découvrable).**

**Acceptée.** Absent de mon dessin. **Ajout :** un monde nul (les lois connues épuisent la grammaire, aucune loi nouvelle n'est vraie) est inclus dans le plan d'exp. 4. Sur ce monde, tout V > 0 est un artefact et tout F est le plancher de base.

---

### Critiques de E

**E-1. Le critère de sélection réintroduit le juge.**

**Acceptée** — même que A-1 et C-1.

**E-2. Les hypothèses changent entre énoncé et décision (utilité pénalisée vs gain brut ; variance vs scores ; non-infériorité manquante).**

**Acceptée.** Mon dessin initial mélangeait les unités entre les expériences et ne posait pas de marge de non-infériorité pour les fausses découvertes. **Correction :** voir dessin corrigé, critère unique S = V/C sur les fiches soumises (critère primaire), taux de fausses soumissions F/(V+F) comme critère secondaire avec marge Δ_F, les deux préenregistrés.

**E-3. La monotonie du témoin n'est pas garantie.**

**Acceptée** — même que A-8 et C-4.

**E-4. Les contrôles proposés testent autre chose (barrière vs compatibilité, pont vs isolement, consigne dégradée, borne inférieure).**

**Acceptée** — chaque point traité individuellement aux critiques correspondantes de A (A-6, A-7, A-5).

**E-5. Portée du GO.**

**Acceptée.** Le budget « go collisionneur ≤ 15 USD » (R-2380) couvre la délibération du collisionneur, pas l'exécution des expériences proposées. Toute dépense d'expérimentation est soumise à un devis et un GO séparés.

**E-6. Recalcul oracle en masquant les verdicts de promotion — contrôle négatif manquant.**

**Transformée en test.** L'analyse primaire est désormais indépendante des promotions (réponse à A-1). En complément, un test de sensibilité compare la décision de sélection du bras avec et sans les verdicts de promotion : si la décision change, c'est un signal que le critère n'est pas suffisamment séparé du juge.

**E-7. Mondes sans loi nouvelle + soumissions nulles — contrôle négatif pour les fausses promotions.**

**Acceptée** — même que C-9.

**E-8. Lots où le score de développement est indépendant de la vérité oracle — contrôle du témoin.**

**Transformée en test.** Un monde « bruit pur » (épisodes de développement sans structure, loi vraie aléatoire indépendante des épisodes) est ajouté. Sur ce monde, le sélecteur mécanique du témoin ne devrait pas battre le tirage aléatoire. S'il le bat, il y a fuite ou artefact.

---

## (b) Expériences corrigées

### Exp. 1 — Compatibilité fonctionnelle Kaimen ↔ relais Kimi v3

- **H_A** : Kaimen `cef5bcf` complète ≥ p★ (illustratif : p★ = 0,80) de ses boucles (superviseur → outil « expérience » → fiche valide avec nonce du noyau dans le journal) sur n essais (n fixé par calcul de puissance, illustratif : n ≥ 20).
- **H_B** : Le taux de boucles complètes est < p★.
- **Contrôle négatif** : même boucle avec schéma d'outil malformé (nom absent du registre), modèle correct. Doit échouer à appeler l'outil mais le relais ne doit pas bloquer la requête. Vérifie que le test mord sur l'appel de fonctions, pas sur la barrière.
- **Vérification du nonce** : chaque appel de l'outil injecte un nonce ; le journal du superviseur est scanné pour le nonce. Absence = boucle échouée même si une fiche est produite.
- **Falsification** : borne inférieure de Clopper-Pearson > p★ → rejette H_B. Borne supérieure < p★ → rejette H_A.

### Exp. 2 — Enfermement de The Agentic Scientist

- **H_A** : L'agent produit ≥ p★ de fiches convertibles sur n essais (n fixé par calcul de puissance, illustratif : n ≥ 25).
- **H_B** : Taux < p★.
- **Contrôle négatif** : agent avec pont actif, consigne exigeant le téléchargement d'une URL externe. L'accès doit échouer *et* être tracé (log iptables/seccomp dans le bac).
- **Falsification** : mêmes bornes de Clopper-Pearson.

### Exp. 3 — Pilote A/A

- **H_A** : Deux runs du même bras, *graines différentes*, mêmes mondes, produisent |S₁ − S₂| < δ_AA (δ_AA préenregistré, illustratif : 20 % de la moyenne).
- **H_B** : La différence ≥ δ_AA ; la métrique n'est pas stable pour ce nombre de mondes.
- **Contrôle négatif** : deux bras intentionnellement différents (proposeur complet vs proposeur privé de ρ = 50 % des épisodes de développement, ρ gelé). Doit produire |S₁ − S₂| > δ_AA, sinon le banc ne discrimine pas un effet de cette taille.
- **Contrôle positif** (ajout) : un monde où une loi nouvelle est accessible par construction à un proposeur naïf (loi très simple non couverte par les lois connues). Le banc doit la détecter comme V > 0.
- **A/A par bras** (ajout E) : un A/A séparé pour le bras scientifique (si exp. 1 passe), car la variance d'une boucle multi-tours n'est pas celle d'un tirage indépendant.
- **Nombre de mondes** : déterminé par un calcul de puissance préenregistré, fondé sur σ estimé du pilote (si le pilote ne fournit pas assez de mondes pour estimer σ, le résultat est « non jugeable à ce budget »).
- **Falsification** : les deux conditions (A/A serré ET contrôle négatif séparé) doivent être remplies pour passer à exp. 4.

### Exp. 4 (fusionnée avec l'ancienne exp. 5) — Scientifique vs témoin

- **Critère primaire** : S = V_soumis / C (vraies découvertes parmi les fiches *soumises* à l'oracle, divisées par le coût en dollars). Aucun conditionnement à la promotion. Le juge O2 tourne en parallèle comme témoin mais ne détermine pas le choix du bras.
- **Critère secondaire** : taux de fausses soumissions τ = F_soumis / (V_soumis + F_soumis), avec test de non-infériorité : H_A : τ_scientifique − τ_témoin ≤ Δ_F (Δ_F gelé, illustratif : 0,10) ; H_B : τ_scientifique − τ_témoin > Δ_F. Correction de multiplicité (Bonferroni/2) sur les deux critères.
- **Multiplicité** : les deux bras soumettent exactement q fiches (q gelé). Le témoin sélectionne q parmi N par son sélecteur mécanique. Le scientifique soumet ses q meilleures par classement interne.
- **Mondes** : M mondes plantés préenregistrés, plus un monde nul (aucune loi nouvelle vraie), plus un monde « bruit pur » (épisodes sans structure). M fixé par calcul de puissance fondé sur exp. 3.
- **H_A** : borne inférieure de l'IC de ΔS = S_scientifique − S_témoin > 0 ET H_A du critère secondaire tient (non-infériorité).
- **H_B** : borne supérieure de ΔS ≤ 0 OU H_B du critère secondaire tient (infériorité sur les fausses).
- **Falsification** : H_A falsifiée si ΔS ≤ 0 dans l'IC ; H_B falsifiée si ΔS > 0 dans l'IC. Si l'IC chevauche 0 : non jugeable — demande plus de mondes ou de budget.
- **Conséquence** : si H_B tient → pas de scientifique ; si H_A tient → brancher (a) en v67 puis considérer (b) ; si non jugeable → budget insuffisant, rapporté comme tel.

### Instruments corrigés

| # | Instrument | Correction principale |
|---|---|---|
| 1 | Relais Kimi v3 | Contrôle négatif : schéma d'outil malformé (pas modèle interdit) |
| 2 | Exécuteur `bwrap` | Pas de pont prise Unix pour (a) ; le code n'a aucun accès réseau |
| 3 | Pont prise Unix | Réservé à (b) uniquement ; non monté pour (a) |
| 4 | Garde loi plantée | `grep` élargi : chaîne normalisée, synonymes gelés, base64 |
| 5 | Témoin « meilleur de N » | Comparé au tirage aléatoire de M parmi N ; monotonie retirée |

---

## (c) Réponse à la question de l'arbitre : ce qui est établi, ce qui ne l'est pas, et l'expérience à faire en premier

### Ce qui est établi

1. **Aucun candidat n'est prêt à l'emploi** (RAPPORTÉ, §3 des faits). Kaimen n'exécute rien ; The Agentic Scientist exécute mais à pleins droits avec réseau ouvert. Les deux demandent des adaptations.
2. **L'option (a) est moins chère à tester** (RAPPORTÉ, §4). Kaimen sur le relais v3 existant évite un relais neuf, un conteneur Docker durci, un pont réseau. La surface d'attaque est plus petite.
3. **Le témoin « meilleur de N » est le comparateur correct** selon N-045 (RAPPORTÉ) : le bon marché d'abord, le cher sur preuve.
4. **La contrainte N-058 interdit de conditionner la sélection du bras aux promotions du juge.** Toute métrique de comparaison doit porter sur les fiches soumises évaluées par l'oracle, pas sur les lois promues. (Correction majeure de mon dessin initial, acceptée suite aux critiques de A, C et E.)
5. **Trois mondes sont mathématiquement insuffisants** pour un test non paramétrique au seuil 0,05 (démontré par C). Le nombre de mondes doit être fixé par un calcul de puissance.

### Ce qui n'est pas établi

1. **Compatibilité fonctionnelle Kaimen ↔ Kimi** (HYPOTHÈSE, §7). L'appel de fonctions forcé par nom sur `kimi-k3.1-pro` n'a jamais été testé. Si ça ne marche pas, l'avantage principal de (a) disparaît.
2. **Faisabilité de l'enfermement de The Agentic Scientist** (HYPOTHÈSE). Les agents `pi`/`opencode` peuvent échouer sans réseau. Leur lecture en flux (qui exigerait un relais neuf) n'est pas vérifiée non plus.
3. **Variance inter-runs de la métrique** (HYPOTHÈSE). Sans pilote A/A, on ne sait pas si le banc discrimine un effet de la taille attendue, ni combien de mondes il faut.
4. **Difficulté des mondes plantés** (HYPOTHÈSE). Le verdict de la course v66 n'est pas rendu. Si les mondes sont triviaux, tout proposeur les résout et aucun scientifique n'est utile.
5. **Coûts réels** (ESTIMÉS, §4). Toutes les estimations couvrent deux ordres de grandeur. Le devis de l'exp. 4 dépend du pilote.

### L'expérience à faire en premier

**Exp. 1 : compatibilité fonctionnelle Kaimen ↔ relais Kimi v3.**

*Raison :* c'est la porte la moins chère (< 1 USD illustratif, quelques dizaines d'appels API) et la plus discriminante. Si l'appel de fonctions ne passe pas, tout le plan séquentiel (a)-puis-(b) change : soit on adapte le client (coût inconnu), soit on teste directement (b), soit on reste au proposeur simple. Le résultat de cette seule expérience restructure l'arbre de décision.

*En parallèle, si budget :* lancer exp. 2 (enfermement Agentic Scientist) car son résultat conditionne l'option de repli. Les deux expériences ensemble coûtent illustrativement < 5 USD en appels API et qualifient ou disqualifient les deux candidats techniquement, avant toute dépense de course.

*Ensuite :* exp. 3 (pilote A/A), qui fixe σ et donc M pour l'exp. 4. Si le pilote montre que le banc ne discrimine pas à budget raisonnable, la réponse correcte est « la question est prématurée — attendons des mondes plus difficiles ou un budget plus large ».

FIN-DE-CELLULE