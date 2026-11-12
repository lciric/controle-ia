# Proposition A — Tour III.1 : quel expérimentateur brancher d'abord

Pièces reçues : FAITS v1 (empreinte affichée, contenu complet) et QUESTION v1 (complète). Aucune proposition B–E n'est visible à ce tour (conception à l'aveugle) : je ne les commente pas.

## 0. Réponse courte

**Choix : autre chose, puis (a), et (b) seulement après une porte de faisabilité séparée.**

Concrètement : avant tout scientifique du marché, brancher un **expérimentateur minimal** (nom de travail illustratif : `exp-min`) fait des pièces que l'organisme possède déjà : le proposeur Kimi tel qu'il passe par le relais v3, l'exécuteur `bwrap` déjà éprouvé pour les tests de mort, et une boucle courte « proposer → lancer un script sur les épisodes de développement → réviser → rendre N fiches ». Aucun tournoi, aucune littérature, aucun agent de code. Le témoin est l'option (c) de la note (« Kimi, meilleur de N » ou « vote à k », à coût apparié), qui est exactement le témoin exigé par N-045.

Raison centrale : la question demande *quel candidat* brancher, alors que le fait établi par la note elle-même (RAPPORTÉ, §3) est qu'**aucun candidat n'est un expérimentateur tel quel**. Les deux options exigent de construire un outil d'exécution isolé (a) ou un enfermement neuf (b) ; une fois construits, ce qu'on mesure n'est plus « Co-Scientist » ni « The Agentic Scientist » mais « un modèle Kimi qui exécute sur les épisodes de développement, plus un paquet de machinerie tierce » (tournoi Elo pour Kaimen ; agents de code à pleins droits et ablations pour Sakana). Ces paquets sont des variables confondues avec la seule variable que le directeur veut en réalité tester : **l'accès à l'exécution change-t-il les vraies et fausses découvertes par dollar, lues sur l'oracle ?** `exp-min` isole cette variable au coût le plus bas ; Kaimen devient ensuite son ablation « + tournoi » ; The Agentic Scientist devient « + agents de code », payé seulement si son enfermement passe une porte mécanique.

Confiance dans ce choix : 0,6 (estimée, subjective, illustrative). Ce qui la ferait tomber est à la section 6.

## 1. (a) Ce que la question suppose sans que ce soit établi

| # | Supposition implicite | Statut | Pourquoi ce n'est pas établi |
|---|---|---|---|
| S1 | Un proposeur qui expérimente produit plus de vraies découvertes par dollar qu'un proposeur qui n'expérimente pas | HYPOTHÈSE | Aucune mesure dans les faits ; le repère de coût (course v66 ≈ 1,5–2 USD estimé pour tout) et les coûts par génération (1,3–12 USD estimé pour Kaimen) disent que le prix de l'expérimentation est de 7 à 500 fois (estimé) une session de proposeur ; le bénéfice, lui, n'a pas de chiffre |
| S2 | Kaimen et The Agentic Scientist sont des expérimentateurs | RAPPORTÉ, contredit par la note | Kaimen n'exécute rien au commit `cef5bcf` ; Sakana exécute, mais avec ce qu'il faut précisément retirer (pleins droits, réseau hôte, Web) |
| S3 | Kaimen tourne sur `kimi-k3.1-pro` (choix d'outil forcé par nom) | HYPOTHÈSE | Non éprouvé (§7 des faits) ; si l'appel d'outil échoue, le bras (a) ne coûte rien et ne mesure rien |
| S4 | The Agentic Scientist survit à son enfermement (relais neuf en flux, réseau coupé, agents sans clé) en restant lui-même | HYPOTHÈSE | Lecture en flux non vérifiée agent par agent ; réglage de l'adresse de base par fichiers de configuration non vérifié ; aucune évaluation tierce |
| S5 | « Coût apparié » est bien défini | RAPPORTÉ comme point ouvert | À coût égal, les bras ne soumettent pas le même nombre de fiches, donc pas la même multiplicité au juge ; la note laisse deux options |
| S6 | La porte « (a) bat le témoin ⇒ on passe à (b) » est informative sur (b) | HYPOTHÈSE | (a) et (b) ne partagent pas la variable testée : si (a) échoue parce que le tournoi sans littérature est inerte, cela ne dit rien d'un agent de code ; si (a) réussit, cela ne dit pas que la machinerie de (b) ajoute quoi que ce soit |
| S7 | L'oracle a assez de puissance au budget envisageable pour voir une différence entre bras | HYPOTHÈSE | Aucun pilote A/A n'a été fait ; la variance du nombre de vraies découvertes par génération est inconnue ; avec des générations à plusieurs dollars, on paie peu de répétitions |
| S8 | Le modèle Kimi n'a pas mémorisé les lois plantées | HYPOTHÈSE | Les pièces sont publiques dans `lciric/ideation-organism` (RAPPORTÉ, vérifié par le concepteur par `git ls-files`/`git ls-remote`) ; « aucun Web » coupe la lecture en ligne, pas la mémoire d'entraînement d'un modèle du marché. Un oracle contaminé par mémorisation rendrait toute la comparaison nulle, quel que soit le candidat |
| S9 | Les épisodes de développement portent assez d'information pour qu'une expérience y apprenne quelque chose | HYPOTHÈSE | La structure (description publique, grammaire, épisodes de dev) est RAPPORTÉE ; leur informativité pour des expériences, non |
| S10 | Le coût `cout_usd` rendu par la commande externe est fiable | RAPPORTÉ comme champ lu ; HYPOTHÈSE sur son exactitude | Jamais rapproché d'une facturation ; N-058 juge « sur le coût mesuré », donc l'instrument de coût doit être lui-même vérifié |

## 2. (b) Expériences décisives, en duel

Toutes sous préenregistrement scellé (R1), contre-lu (R2), nom de version neuf (R12), verdict de porte par lecteur neuf (R13), pilote A/A avant toute comparaison (N-045). Issues toujours lues sur l'oracle et le coût mesuré (N-058), jamais sur le verdict du juge ; le juge O2 reste en place et sa décision n'entre dans aucune sélection (N-053).

### E0 — Sonde de mémorisation (préalable, sans idée scientifique, bon marché)

- **H_A** : `kimi-k3.1-pro` ne peut pas reproduire les lois plantées à partir de leurs identifiants ou d'indices publics (nom de fichier, nom du monde, préambule du texte scellé).
- **H_B** : il les reproduit au-dessus du niveau d'une loi-leurre.
- **Métrique** : taux de correspondance (mécanique, sur la forme `loi_predictive`) entre la réponse du modèle et la loi plantée, pour k lois plantées publiques **et** k leurres de même gabarit jamais publiés, écrits par un auteur hors Claude et hors Kimi.
- **Seuil** (préenregistré, illustratif) : correspondance sur les plantées ≤ correspondance sur les leurres + marge fixée d'avance ; sinon alerte.
- **Contrôle négatif** : les leurres. Contrôle positif : une loi « connue » (du nul O2) que le modèle est censé connaître par la vue servie.
- **Issues** : si correspondance plantée > leurres, H_A est falsifiée et **toute comparaison sur l'oracle avec Kimi est invalide** tant que les mondes ne sont pas replantés hors des dépôts publics ; si égale, H_B est falsifiée pour cette version de Kimi et ces mondes.

### E1 — L'exécution isolée vaut-elle son prix ? (`exp-min` contre témoin (c))

- **H_A** : à coût apparié, `exp-min` produit plus de vraies découvertes par dollar et pas plus de fausses découvertes par dollar que « Kimi, meilleur de N ».
- **H_B** : la différence est dans l'enveloppe du pilote A/A (le coût des jetons dépensés en code n'est pas récupéré sur l'oracle).
- **Métrique primaire** : vraies découvertes par dollar sur l'oracle ; secondaires : fausses découvertes par dollar, fausses promotions, coût par rôle.
- **Seuil** : différence supérieure à κ fois l'écart A/A, κ fixé dans le préenregistrement (illustratif : κ = 2) ; unité de réplication = **le monde planté**, pas la génération, pour que la statistique porte sur des mondes et non sur des tirages du même monde.
- **Contrôle négatif 1** : A/A, deux runs de chaque bras. **Contrôle négatif 2 (essentiel)** : un bras **exécuteur-fictif** (`exp-sham`, illustratif) où l'outil est présent, la consigne identique, mais le bac renvoie une sortie vide ou tronquée. Il sépare « avoir le mot *expérience* dans la consigne » de « recevoir un résultat ».
- **Règle de multiplicité** : même nombre de fiches soumises par bras ; le témoin choisit les siennes par une règle mécanique sur les épisodes de développement (première option de la note). Raison : la fausse promotion dépend de la multiplicité ; la tenir fixe rend les fausses promotions comparables. La seconde option (multiplicité propre, lue sur l'oracle) devient analyse secondaire préenregistrée.
- **Issues** : `exp-min` ≤ témoin → H_A falsifiée pour ce coût et cette famille de mondes, et **on ne branche aucun scientifique du marché** : ils coûtent tous plus et ne font pas autre chose sur ce point. `exp-min` > témoin **et** `exp-sham` ≤ témoin → H_B falsifiée, l'exécution a une valeur mesurée. `exp-min` > témoin et `exp-sham` > témoin aussi → l'effet vient de la consigne, pas de l'exécution ; ni H_A ni H_B ne sont tranchées proprement, on révise la consigne du témoin et on recommence (R4 : un résultat positif suspect s'audite autant qu'un négatif).

### E2 — Le tournoi de Kaimen ajoute-t-il quelque chose au-dessus de l'exécution ?

Ne se paie que si E1 a falsifié H_B.

- **H_A** : Kaimen `cef5bcf` sur Kimi, outils de littérature retirés, un seul outil « expérience » vers l'exécuteur isolé (bras (a) de la note), bat `exp-min` à coût apparié, en particulier sur les fausses découvertes par dollar (ce que le tri interne est censé améliorer : ce qu'il **soumet**, pas ce qui survit).
- **H_B** : Kaimen = `exp-min` + un surcoût de jetons de tournoi sans gain sur l'oracle.
- **Métrique** : fausses découvertes par dollar (primaire ici), vraies découvertes par dollar (secondaire).
- **Contrôle négatif** : **Kaimen à tri aléatoire** : même boucle, même dépense, mais le choix des fiches soumises tiré au hasard parmi les hypothèses produites, Elo ignoré. Il sépare « générer plus et trier » de « trier bien ».
- **Issues** : Kaimen ≤ `exp-min` → H_A falsifiée, on reste sur `exp-min` et on s'épargne les retouches de code tiers. Kaimen > `exp-min` **et** Kaimen-aléatoire ≤ `exp-min` → H_B falsifiée, le tri vaut son prix. Kaimen-aléatoire > `exp-min` aussi → c'est le volume, pas le tri ; `exp-min` avec plus de tirages (moins cher) est le bon bras suivant.

### E3 — Porte de faisabilité de l'enfermement de The Agentic Scientist

C'est la réponse directe à « pourquoi pas lui ? ». Ce n'est pas une expérience d'idéation : elle se joue sur un **monde-jouet non planté**, hors oracle, hors juge, et ne consomme pas de monde planté.

- **H_A** : enfermé (réseau injoignable sauf le pont vers le relais, agents sans clé, relais neuf en flux refusant tout modèle autre que `kimi-k3.1-pro`, phases réduites à l'investigation), The Agentic Scientist termine la tâche-jouet avec un taux d'achèvement et un coût comparables (dans l'enveloppe A/A) à sa version non enfermée sur la même tâche.
- **H_B** : l'enfermement le casse (échec, boucle, dégénérescence) ou en change le coût d'un facteur fixé d'avance (illustratif : > 2).
- **Métrique** : taux d'achèvement, coût mesuré par run, nombre d'appels de l'agent à des ressources refusées (compté par les gardes).
- **Contrôle négatif** : un relais volontairement cassé doit produire un **échec fermé** (aucune fiche, aucun coût caché) ; si l'agent « réussit » malgré un relais cassé, c'est qu'il a trouvé une autre route, et l'enfermement est faux.
- **Issues** : H_B vraie → (b) n'est pas branchable sans travail supplémentaire chiffré ; on le note et on s'arrête là. H_A vraie → (b) devient un bras admissible pour un E2-bis (« + agents de code » contre `exp-min`), à coût apparié, avec les mêmes contrôles qu'E2.

Pourquoi E3 ne vient pas en premier : le travail de construction (démon Docker, image dérivée, relais en flux, pont de prise Unix) est un coût certain, payé avant toute information sur S1. Si E1 falsifie H_A, ce coût est perdu. Si E1 falsifie H_B, E3 reste utile et n'a rien perdu à attendre.

## 3. (c) Pour chaque instrument nommé : la mesure minimale qui dirait s'il fonctionne

### 3.1 L'outil d'exécution « neuf et isolé » et ses gardes

L'instrument n'est pas l'outil lui-même mais la chaîne de gardes listée par la note (réseau injoignable sauf relais, aucune variable de clé dans le bac, modèle servi = `kimi-k3.1-pro`, aucun binaire `claude`/`codex`, vue sans verdict, recherche de la loi plantée dans fichiers et journaux, plafonds par session, base neuve à chaque génération).

- **Cas honnêtes appariés** : pour chaque garde, au moins un run propre (illustratif : 20 par garde) où rien n'est à détecter.
- **Artefacts injectés** : pour chaque garde, un run où l'écart est planté par l'opérateur, pas par le modèle : un script qui tente `connect()` vers une adresse hors relais ; une variable `*_API_KEY` posée dans l'environnement ; une demande de modèle `claude-*` au relais ; un fichier de travail contenant la loi plantée recopiée avec variations de forme (espaces, renommage de variables, ordre des termes) ; une session qui dépasse le plafond.
- **Taux à battre** : détection = 1 sur chaque artefact (une garde qui rate un artefact unique est refusée) ; fausses alertes ≤ un seuil préenregistré sur les cas honnêtes (illustratif : 0 sur 20, car une fausse alerte invalide une génération payée).
- **Vérification mécanique à battre** : la garde « loi plantée » par motif exact est le niveau plancher ; l'artefact à variations de forme sert à montrer si elle vaut mieux qu'un `grep`. Si elle ne détecte que le motif exact, dire qu'elle ne détecte que le motif exact.
- **Résultat trop propre** : si toutes les gardes font 100 % / 0 % du premier coup, R4 impose de vérifier que les artefacts étaient bien posés (un artefact mal posé donne une détection « parfaite » sans rien détecter).

### 3.2 Le témoin « Kimi, meilleur de N »

- **Mesure minimale** : le pilote A/A. Deux runs du témoin, mêmes mondes, même N, même règle mécanique de choix des fiches. L'écart entre les deux fixe l'enveloppe de bruit de toute l'expérience.
- **Seuil** : si l'écart A/A dépasse la différence qu'on espère voir dans E1 (fixée d'avance), l'instrument n'a pas la résolution nécessaire : on augmente le nombre de mondes ou on réduit l'ambition avant de dépenser sur un bras cher.
- **Second instrument de N-045** : « un modèle, vote à k, coût apparié ». Je recommande de préenregistrer **lequel des deux** est le témoin primaire (meilleur de N par règle mécanique, car il n'introduit pas d'agrégation à concevoir) et de garder l'autre en secondaire.

### 3.3 La lecture sur l'oracle (vraies et fausses découvertes par dollar)

- **Mesure minimale** : sur un monde planté où l'on connaît la réponse, injecter mécaniquement des fiches vraies et fausses (issues de la loi plantée et de leurres) et vérifier que l'oracle les classe comme attendu : détection des vraies = 1, fausses alertes = 0 sur ces fiches de contrôle. C'est un test de l'appariement fiche ↔ loi plantée, pas du modèle.
- **Puissance** : rapporter, à partir de l'A/A, le nombre de mondes nécessaire pour voir l'effet préenregistré ; ce nombre fait partie du devis.

### 3.4 La mesure de coût (`cout_usd` dans la ligne JSON)

- **Mesure minimale** : rapprocher, sur l'essai court du devis, la somme des `cout_usd` rendus avec le relevé du relais (jetons d'entrée et de sortie × prix). Écart toléré préenregistré (illustratif : 5 %). N-058 juge « sur le coût mesuré » : si cet instrument ment, tout le reste ment.

### 3.5 L'enfermement de The Agentic Scientist (sans réseau, sans Web)

- **Mesure minimale** : un **canari** : poser, à une adresse joignable depuis le réseau hôte mais non depuis le bac, un fichier portant une fausse « loi plantée » unique et jamais publiée ; lancer l'agent non enfermé puis enfermé sur la même tâche-jouet ; compter les apparitions du canari dans ses fichiers et journaux. Non enfermé, le canari **doit** pouvoir apparaître (sinon le test ne prouve rien) ; enfermé, il ne doit jamais apparaître.
- **Taux** : détection du canari non enfermé > 0 sur un nombre de runs fixé ; enfermé = 0. Plus la garde réseau mécanique (compteur de tentatives de connexion refusées) qui doit être > 0 pour l'agent enfermé qui essaie, prouvant que c'est la garde, et non l'absence d'essai, qui protège.

## 4. Risques, par option

**`exp-min` (mon choix)**. (i) C'est du code neuf du programme, donc sans évaluation tierce non plus ; mais il est court, nommé, et ne porte aucun défaut Claude/OpenAI caché. (ii) Il ne « répond pas à la question du directeur » si celle-ci est lue comme « quel produit du marché » ; il y répond si elle est lue comme « pourquoi pas celui qui exécute ». (iii) Risque de boucle courte trop pauvre : si Kaimen bat `exp-min` en E2 grâce au tri, c'est le résultat attendu de l'expérience, pas un échec de la méthode. (iv) Même menace de Goodhart que les autres : l'expérimentateur ne reçoit jamais verdict, oracle, tranche du test de mort ni tirages frais (les gardes de 3.1 s'appliquent).

**(a) Kaimen**. Retouches de code tiers (outils, schéma, consignes) ; valeurs Claude par défaut qui survivent à une fusion partielle (le relais les refuse, mais en échec fermé, donc en générations perdues, pas en fuite) ; choix d'outil forcé par nom non éprouvé sur Kimi (S3) ; fidélité : privé de littérature ce n'est plus Co-Scientist, et le nom du bras doit le dire.

**(b) The Agentic Scientist**. Exécution à pleins droits et clés lisibles par les agents ; réseau hôte par défaut avec les pièces plantées publiques : c'est le seul candidat pour qui une **fuite de l'oracle** est le comportement par défaut, pas un accident ; incident rapporté d'un agent modifiant le protocole d'évaluation ; relais neuf en flux à écrire et à éprouver ; coût estimé 3,6–21 USD par génération plus machine ; projet « Alpha », sans évaluation tierce. Et la même perte de fidélité qu'(a) : enfermé et réduit à l'investigation, ce n'est plus l'article des auteurs.

**(c) seul, sans expérimentateur**. Ne teste jamais S1 ; mais c'est l'issue correcte si E1 falsifie H_A.

**Risque transversal, le plus grave** : S8. Si Kimi a mémorisé les pièces publiques, aucun des trois chemins ne mesure quoi que ce soit, et le défaut ne se voit pas sans E0.

## 5. (d) Ancrage matériel

- **Modèles** : l'organisme fixe `kimi-k3.1-pro` par le relais v3 (liste exacte, échec fermé) ; aucun modèle à poids ouverts n'est dans les faits, et en admettre un exigerait d'élargir la liste du relais, donc une décision hors de ce tour. Argon (`gemini-4-argon`) reste témoin, jamais décisif. Claude : aucun rôle, y compris pour écrire les leurres d'E0 (à confier à un auteur hors Claude et hors Kimi, humain ou Argon en rôle de rédaction seulement).
- **Calcul** : `exp-min` et (a) n'exigent que l'exécuteur `bwrap` existant plus le **pont** de la prise Unix du bac vers le relais (préalable déjà listé par la note), dépendances installées hors ligne. (b) exige en plus un démon Docker, une image dérivée, un réseau interne sans route, un relais neuf en flux ; machine estimée par la note 0,45–1,1 EUR par génération.
- **Coûts (illustratifs, aucun mesuré)** :
  - E0, sonde de mémorisation : quelques dizaines d'appels courts, ≈ 1 USD (illustratif).
  - Gardes de 3.1 et instruments 3.3–3.4 : essai court chiffré par le devis ; ≈ 2–5 USD (illustratif).
  - E1 : `exp-min` ≈ 2 à 5 fois (illustratif) une session de proposeur, soit bien sous les 1,3–12 USD estimés pour Kaimen ; trois bras (`exp-min`, `exp-sham`, témoin) × A/A × M mondes ; pour M = 5 (illustratif) ≈ 20–60 USD (illustratif).
  - E2 (Kaimen + Kaimen-aléatoire) : à partir des 1,3–12 USD estimés par génération, ≈ 50–200 USD (illustratif) pour le même M.
  - E3 (porte Sakana, monde-jouet) : ≈ 20–100 USD (illustratif) plus le temps de construction, qui est le vrai prix.
  - Le « go collisionneur ≤ 15 USD » (R-2380) couvre ce tour de collisionneur, pas ces expériences : chacune relève d'un devis et d'un GO séparés.
- **Devis fondé sur l'essai court** : les prix de jetons de la note sont « à vérifier » ; le devis réel se lit sur le relevé du relais de l'essai court (3.4), pas sur ces chiffres.

## 6. La mesure qui départage, et ce qui me ferait changer d'avis

**La mesure qui départage** : E1, lue sur l'oracle à coût apparié, avec le bras exécuteur-fictif. Elle tranche « l'exécution vaut-elle son prix ? » avant que le choix entre Kaimen et Sakana ait un sens.

**Je changerais d'avis si** :
1. E0 montre une mémorisation : alors la priorité n'est plus le choix d'un expérimentateur mais le replantage des mondes hors dépôt public ; toute comparaison attendrait.
2. L'A/A montre une enveloppe de bruit plus large que l'effet espéré au budget disponible : alors on ne branche rien et on dit pourquoi (puissance), ce qui vaut mieux qu'un bras cher non interprétable.
3. E3 est bon marché en pratique (le relais en flux et le réseau coupé tiennent en un essai court mesuré, canari à zéro) : alors (b) devient le second bras à la place de Kaimen, parce qu'il apporte des ablations déjà codées et que son « + agents de code » est une variable plus proche de ce que le directeur demande que le tournoi de Kaimen.
4. La question du directeur est en réalité « tester un produit du marché pour le papier, pas pour l'oracle » : alors c'est une modification de revendication (§5 des faits), à soumettre au directeur, et mon choix ne s'applique pas.
5. `exp-min` perd contre le témoin en E1 **et** `exp-sham` aussi : c'est l'issue qui falsifie ma propre proposition ; on reste sur (c), et la note l'avait prévu.

FIN-DE-CELLULE