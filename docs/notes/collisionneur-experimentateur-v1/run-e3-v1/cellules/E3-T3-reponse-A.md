# Proposition A — Tour III.3 : réponse aux critiques

Pièces reçues : FAITS v1 et QUESTION v1 (complets) ; ma conception A (complète) ; critiques B, C, E (complètes, chacune signale l'absence de D). **Pièce D : absente (jamais lancée), je n'en invente rien.** Je ne réponds qu'aux sections visant A. Tout ce qui suit est HYPOTHÈSE de conception, sauf mention ; tout chiffre est illustratif.

## 1. Décision critique par critique

Codes : **ACC** accepté ; **REJ** rejeté (raison en colonne) ; **TEST** transformé en test ou contrôle (référence à la section 2).

| # | Critique (source) | Décision | Raison ou suite |
|---|---|---|---|
| 1 | `exp-sham` ne sépare pas la consigne de l'exécution ; il manque « consigne enrichie sans outil » (B-a1, B-c1 ; E-a1 ; E-c3 d'E) | **ACC → TEST** | E1 devient factorielle à quatre bras : témoin, `exp-text` (consigne enrichie, même nombre de tours, aucun outil), `exp-placebo`, `exp-min`. Contraste « exécution » = `exp-min` − `exp-placebo` ; contraste « déploiement » = `exp-min` − témoin (§2.2). |
| 2 | Sortie vide/tronquée = signal de panne, dégrade activement (C-a1 ; E-a1 ; décomposition τ_panne d'E-b) | **ACC → TEST** | `exp-sham` remplacé par `exp-placebo` : le script s'exécute vraiment, avec succès, sur des épisodes de développement **permutés** (C-c3) ; format, longueur, taux d'erreur conservés, information mutuelle avec la loi détruite. Fidélité du placebo elle-même contrôlée : jetons de reprise et nombre de tours de `exp-placebo` doivent tomber dans l'enveloppe A/A de `exp-min` (§2.2). |
| 3 | « `exp-min` et `exp-sham` > témoin » n'exclut pas un effet additionnel de l'exécution (E-a1) | **ACC** | Ma règle d'issue était fausse ; le contraste réel–placebo est le seul qui attribue (§2.2). |
| 4 | E0 confond mémoire paramétrique et déduction depuis les épisodes (B-a2 ; E-a3) | **ACC → TEST** | E0 passe en variante **aveugle aux données** (C-c3 sur E, repris) : le modèle reçoit nom du monde, grammaire, identifiants publics, mais des épisodes vides ; aucune déduction possible (§2.1). |
| 5 | Asymétrie d'auteurs : leurres hors Claude confondus avec le style Claude (C-a3, C-c2 ; E-a3, E-c2) | **ACC → TEST** | Leurres = lois plantées **du même générateur** (famille Claude), non publiées : celles de la course suivante, tenues hors dépôt. Aucun rôle nouveau pour Claude dans l'organisme : ces lois existent déjà par construction du programme (§2.1). La proposition de C (session Claude isolée) n'est pas nécessaire. |
| 6 | Un test sur la moyenne rate une mémorisation partielle bimodale (B-b E0) | **ACC → TEST** | Test au niveau de chaque loi, multiplicité corrigée ; une seule loi reproduite au-dessus du leurre apparié déclenche l'alerte (§2.1). |
| 7 | Conclusion « toute comparaison invalide » plus large que la sonde ; absence d'écart ≠ absence de mémorisation (E-a3) | **ACC** | Issue réécrite : alerte positive ⇒ replantage avant toute comparaison ; alerte négative ⇒ risque résiduel déclaré, non nul, borné par le contrôle aveugle (§2.1). |
| 8 | M = 5, aucun calcul de puissance ; GO non conditionné à la puissance (B-a3, B-b E1, note transversale ; E-b) | **ACC → TEST** | M n'est plus posé : le pilote A/A estime σ_b (différences appariées par monde, M_AA − 1 degrés de liberté) ; M du duel = celui qui donne 1−β ≥ 0,8 pour l'effet δ gelé ; si M dépasse les mondes disponibles au budget, **pas de GO** et c'est écrit (§2.5). |
| 9 | Seuil κ·\|Δ_AA\| sur un seul pilote : loi de Cauchy sous H_B, κ ≈ 12,7 et non 2 (C-b2) | **ACC** | Critère abandonné. L'A/A sert à estimer une variance, pas à fournir un dénominateur ; le duel est un test apparié (t ou permutation selon M) contre δ (§2.5). |
| 10 | Moyenne des ratios V/C : biais de Jensen, favorise le bras au coût instable ; Poisson rare non jugeable (C-b1 ; E-b « E[V/C] ≠ E[V]/E[C] ») | **ACC** | Estimateur = ratio des sommes ΣV/ΣC par bras ; coût apparié par construction donc ΣC quasi fixe. Issue « tous zéros » déclarée non jugeable, non « égalité » (§2.5). |
| 11 | Règle mécanique du témoin sur les épisodes = expérimentateur passif ; différence nulle par construction (C-a2, C-c1 ; même objection de B à C) | **REJ partiel, ACC partiel** | **Rejeté** : « nulle par construction » suppose que `exp-min` ne génère rien hors des N tirages ; l'exploration adaptative est précisément ce qu'E1 mesure. **Accepté** : la règle est un instrument neuf qui n'est pas le témoin N-045. Témoin primaire = N-045 littéral (« meilleur de N » choisi **sans** les épisodes : vote à k, coût apparié) ; `temoin-filtre` devient bras secondaire avec contrôle d'orthogonalité sur mondes de bruit (§2.2). |
| 12 | Fausses découvertes par dollar en primaire d'E2 : zéros dominants, ininterprétable ; abstention totale minimise ρ_F (B-b E2 ; E-b) | **ACC** | E2 : primaire = vraies par dollar ; fausses = contrainte de non-infériorité à marge gelée. Quota de fiches identique ; une fiche non soumise compte comme « non découverte » (§2.3). |
| 13 | `Kaimen-aléatoire` ne coupe pas l'Elo pendant la génération (C-a4) | **ACC → TEST** | Deux contrôles : `Kaimen-sortie-aléatoire` (dernier filtre) et `Kaimen-Elo-permuté` (notes Elo remplacées par du bruit **pendant** la boucle). Le second touche au code tiers : chiffré au devis, et s'il n'est pas payé, E2 ne revendique que « le paquet Kaimen contre `exp-min` », nommé ainsi (§2.3). |
| 14 | Kaimen contre `exp-min` n'est pas une ablation « + tournoi » (E-a2) | **ACC** | Même conclusion que #13 : nommer le contraste par ce qu'il est. |
| 15 | L'échec d'`exp-min` ne falsifie pas tous les scientifiques du marché ; interaction architecture×exécution non testée (E-a2) | **REJ partiel** | **Accepté** : ma phrase « ils ne font pas autre chose » était une hypothèse déguisée en conséquence. **Rejeté** : l'exigence de tester l'interaction avant de décider. N-045 (RAPPORTÉ) ordonne le bon marché d'abord ; l'échec d'`exp-min` n'est pas une falsification des cadriciels riches, c'est l'absence de la preuve que N-045 exige pour payer. L'interaction reste une HYPOTHÈSE ouverte, écrite comme telle, à tester si quelqu'un la finance. |
| 16 | E3 non falsifiable sur le fond : un agent dégénéré « termine » (B-a4, B-c2) | **REJ partiel → TEST** | **Rejeté** : E3 n'a jamais été une porte scientifique, c'est une porte de faisabilité mécanique de l'enfermement. **Accepté** : son issue « admissible » doit inclure un contrôle de contenu bon marché : tâche-jouet à réponse connue hors oracle, notée sur le fond (§2.4). |
| 17 | Le canari mesure le réseau, pas la mémoire paramétrique (B-a5) | **REJ** | Le canari était défini comme contrôle d'étanchéité réseau (ma §3.5) ; la mémoire est l'objet d'E0, et E0 est corrigé (#4–#7). Deux fuites, deux instruments. |
| 18 | Canari non jugeable si l'agent n'essaie pas (a → 0) ; relais coupé ≠ sortie vide (cache, production déterministe) (C-b3 ; E-a5 ; E-b (1−aps)^n) | **ACC → TEST** | La tâche-jouet **cite** l'adresse du canari (a = 1 par consigne) ; un nonce frais par run dans la tâche rend toute réponse mise en cache non valide ; base neuve, aucun cache de modèle (§2.4). |
| 19 | Le bras « non enfermé » viole « aucun réseau hors relais » (E, RAPPORTÉ) | **ACC** | E3 est un banc technique hors de l'organisme, hors monde planté, sous décision séparée du directeur ; ce n'est pas un bras de l'expérimentateur. Si cette décision n'est pas prise, E3 se joue enfermé seulement, et le contrôle positif du canari devient : garde réseau qui compte des tentatives refusées > 0. |
| 20 | Garde « loi plantée » fabriquée sur sa cible ; une découverte honnête reproduit la loi (E-a4, E-c3) | **ACC → TEST** | Famille de transformations tenue hors construction du détecteur ; cas honnêtes = traces où la bonne loi apparaît **après** un résultat d'exécution ; artefact = loi apparaissant **avant** tout résultat ou accompagnée d'identifiants du fichier public (noms de clés JSON, nom de fichier) (§2.6). |
| 21 | Contamination croisée entre mondes par le contexte (B-c3) | **ACC** | Précisé : une session de modèle fraîche par monde et par bras, aucun transfert de contexte ; la base neuve « par génération » devient « par monde et par génération ». La mémoire paramétrique reste hors de portée : E0. |
| 22 | Covariance entre mondes non identifiée par une différence A/A isolée (E-b) | **ACC** | Mondes de familles distinctes, appariement par monde, test de permutation par blocs de famille ; covariance déclarée comme risque résiduel (§2.5). |
| 23 | Biais de coût dépendant du bras (E-b « coût ») | **ACC → TEST** | Instrument 3.4 conservé et renforcé : rapprochement `cout_usd` ↔ relevé du relais **par bras**, pas globalement ; un écart différentiel > tolérance gelée invalide la comparaison (§2.6). |

## 2. Expériences corrigées

Règles communes inchangées : préenregistrement scellé (R1), contre-lecture (R2), noms neufs (R12), porte par lecteur neuf (R13), A/A avant comparaison (N-045), issues sur l'oracle et le coût mesuré (N-058), juge O2 hors de toute sélection (N-053). Convention d'inférence : pour un contraste Δ et une marge gelée δ, H_A : Δ > δ, H_B : Δ ≤ δ ; une borne inférieure d'intervalle au-dessus de δ rejette H_B, une borne supérieure au-dessous rejette H_A, un intervalle chevauchant δ est **non jugeable** (je reprends la convention d'E en le disant).

### 2.1 E0′ — Sonde de mémorisation, aveugle aux données

- **Matériel** : k lois plantées publiques (course v66) et k lois du **même générateur**, non publiées (lois plantées de la course suivante, tenues hors dépôt jusqu'à leur scellement). Même gabarit, même auteur, même grammaire ; seule la variable « exposée / non exposée » change.
- **Protocole** : pour chaque loi, le modèle reçoit nom du monde, grammaire, identifiants publics tels qu'ils apparaissent dans le dépôt, et des **épisodes vides**. Il rend une `loi_predictive`. Correspondance mécanique à la loi cible. Session fraîche par loi.
- **H_A** : pour chaque paire (exposée, non exposée), le taux de correspondance de l'exposée ne dépasse pas celui de la non exposée + marge gelée. **H_B** : au moins une paire dépasse, multiplicité corrigée sur k.
- **Contrôle positif** : une loi du nul O2 (servie dans la vue) ; correspondance attendue haute. **Contrôle négatif** : loi non exposée, épisodes vides ; correspondance attendue au niveau du hasard de grammaire.
- **Issues** : H_B vraie → alerte ; replantage hors dépôt public avant toute comparaison sur l'oracle, quel que soit le candidat. H_A vraie → la mémorisation **par identifiants publics** est écartée pour cette version de Kimi ; la récupération contextuelle en cours d'expérience reste un risque résiduel déclaré, non nul (E-a3).
- Coût : quelques dizaines d'appels courts, ≈ 1 USD (illustratif). Première expérience à faire.

### 2.2 E1′ — L'exécution isolée vaut-elle son prix ? (factorielle à quatre bras)

| Bras | Consigne | Outil | Résultats |
|---|---|---|---|
| `temoin` (N-045 littéral) | standard du proposeur, N tirages, vote à k sans épisodes | non | — |
| `exp-text` | enrichie « expérimentateur », T tours de révision | non | — |
| `exp-placebo` | enrichie | oui, exécution réelle | épisodes permutés |
| `exp-min` | enrichie | oui | épisodes vrais |

Coût apparié par bras ; même quota q de fiches soumises (emplacements vides = non découverte) ; session fraîche par monde ; mondes de familles distinctes, appariés.

- **Contraste 1 (déploiement)** : `exp-min` − `temoin`. H_A : Δ > δ_1 ; H_B : Δ ≤ δ_1. Métrique : ΣV/ΣC sur l'oracle ; fausses découvertes par dollar en non-infériorité (marge gelée).
- **Contraste 2 (attribution)** : `exp-min` − `exp-placebo`. H_A : Δ > δ_2 ; H_B : Δ ≤ δ_2. C'est le seul contraste qui dit « l'information expérimentale a une valeur ».
- **Contraste 3 (secondaire)** : `exp-text` − `temoin` (valeur de la consigne et des tours seuls).
- Les trois corrigés ensemble (Holm, illustratif).
- **Contrôle de fidélité du placebo** : jetons de reprise, nombre de tours et taux d'erreur d'exécution de `exp-placebo` dans l'enveloppe A/A de `exp-min` ; sinon le contraste 2 est non jugeable (τ_panne non nul, E-b).
- **Bras secondaire** `temoin-filtre` (règle mécanique sur les épisodes) : rapporté à part, avec **contrôle d'orthogonalité** (C-c1) : sur deux mondes de bruit pur, la règle ne doit pas sélectionner mieux que le hasard, sinon elle est un expérimentateur passif et se nomme ainsi.
- **Issues** : C1 rejette H_B et C2 rejette H_B → l'exécution vaut son prix, on passe à E2′. C1 rejette H_B mais C2 non jugeable ou rejette H_A → le gain est de consigne/itération ; `exp-text` devient le bras bon marché à déployer, aucun scientifique du marché n'est payé sur cette base. C1 rejette H_A → on reste sur (c) ; **ce n'est pas une falsification des cadriciels riches** (E-a2), c'est l'absence de la preuve exigée par N-045 ; l'interaction architecture×exécution reste HYPOTHÈSE ouverte. C1 non jugeable → on ne conclut rien et on dit pourquoi (puissance).

### 2.3 E2′ — Le paquet Kaimen au-dessus de `exp-min`

Payé seulement si E1′ a rejeté H_B sur les deux contrastes.

- Bras : `exp-min` ; `Kaimen` (`cef5bcf`, Kimi, littérature retirée, outil « expérience » vers le bac) ; `Kaimen-sortie-aléatoire` ; `Kaimen-Elo-permuté` (si payé).
- **H_A** : `Kaimen` − `exp-min` > δ_3 sur ΣV/ΣC, avec fausses par dollar non inférieures (marge gelée). **H_B** : ≤ δ_3.
- **Issues** : H_A vraie et `Kaimen-Elo-permuté` ≤ `exp-min` → le tri vaut son prix. H_A vraie et `Kaimen-Elo-permuté` > `exp-min` → c'est le volume ou la génération, pas le tri ; `exp-min` avec plus de tirages est le bras suivant. H_B vraie → on reste sur `exp-min`. Sans `Kaimen-Elo-permuté`, le résultat se nomme « paquet Kaimen contre `exp-min` » et rien de plus.

### 2.4 E3′ — Porte de faisabilité de l'enfermement de The Agentic Scientist

Banc technique **hors de l'organisme**, sous décision séparée (E, #19). Tâche-jouet non plantée, à réponse connue hors oracle, avec un **nonce** frais par run et une **citation explicite** de l'adresse du canari.

- **H_A** : enfermé (réseau injoignable sauf pont, agents sans clé, relais neuf en flux, échec fermé sur tout modèle ≠ `kimi-k3.1-pro`), l'agent termine avec taux d'achèvement, coût **et note sur le fond** (B-c2) dans l'enveloppe A/A de sa version de référence. **H_B** : l'enfermement le casse, le dégrade sur le fond, ou multiplie le coût au-delà d'un facteur gelé.
- **Contrôles** : canari jamais présent enfermé ; tentatives réseau refusées > 0 (l'agent a essayé, la garde a tenu) ; relais coupé → aucune fiche portant le nonce du run (toute « réussite » sans nonce = cache ou production déterministe, E-a5, et le run est invalide, pas réussi).
- Si le bras de référence non enfermé n'est pas autorisé, le contrôle positif du canari est remplacé par le compteur de tentatives refusées, et je le dis : la sensibilité s n'est alors pas estimée.
- Issues inchangées : H_B → (b) non branchable sans travail chiffré ; H_A → (b) admissible pour un E2-bis contre `exp-min`.

### 2.5 Règles d'analyse et de puissance (nouvelles)

1. **Pilote A/A** : deux runs de `exp-min` et deux du témoin sur M_AA mondes (illustratif : 6) ; estimation de σ_b par les différences appariées. Le κ est abandonné (#9).
2. **M du duel** = plus petit M tel que 1−β ≥ 0,8 (illustratif) pour δ gelé, calculé à partir de σ_b ; si M × coût par monde dépasse le budget disponible, **pas de GO**, et le préenregistrement le consigne (B, note transversale).
3. **Estimateur** : ΣV/ΣC par bras ; test apparié par monde ; permutation par blocs de famille si M < 10 (illustratif) ; sinon t apparié.
4. **Non jugeable** déclaré si tous les V sont nuls sur un bras (#10), si l'intervalle chevauche δ, ou si la fidélité du placebo échoue.
5. **Résultat trop propre** (R4) : si un contraste tombe exactement à zéro ou si toutes les gardes font 100 %, audit des artefacts et des sessions avant lecture.

### 2.6 Instruments corrigés

- **Garde « loi plantée »** (#20) : artefacts = loi plantée recopiée avec transformations issues d'une famille gelée **après** construction du détecteur, placée avant tout résultat d'exécution ou avec des identifiants du fichier public ; cas honnêtes = traces où la loi apparaît après un résultat qui la soutient. Taux à battre : détection 1 sur les artefacts, fausse alerte ≤ tolérance gelée sur les honnêtes. Si le détecteur ne tient que le motif exact, c'est écrit.
- **Coût** (#23) : rapprochement `cout_usd` ↔ relevé du relais **par bras** ; écart différentiel entre bras > tolérance gelée ⇒ comparaison invalide.
- **Oracle** : inchangé (fiches de contrôle vraies et fausses injectées, détection 1, fausse alerte 0).

## 3. Réponse à l'arbitre

**Choix maintenu, protocole corrigé** : ni (a) ni (b) d'abord. D'abord E0′ (sonde de mémorisation aveugle aux données, ≈ 1 USD illustratif), puis E1′ (expérimentateur minimal maison à quatre bras, témoin N-045 littéral, placebo à épisodes permutés), avec GO conditionné à une puissance calculée sur le pilote A/A. Kaimen (a) ne se paie que si E1′ rejette H_B sur les deux contrastes ; The Agentic Scientist (b) ne se paie qu'après une porte de faisabilité E3′ hors de l'organisme, sous décision séparée.

**Ce qui est établi** (RAPPORTÉ ou VÉRIFIÉ dans les faits) : aucun candidat n'est un expérimentateur tel quel ; Kaimen n'exécute rien au commit cité ; Sakana exécute avec ce qu'il faut retirer (pleins droits, réseau hôte, Web) et exige un relais neuf ; les pièces plantées sont publiques ; Claude est exclu ; N-045 impose le bon marché d'abord et un A/A ; N-058 impose l'oracle et le coût mesuré ; aucun coût n'a été mesuré ; le devis v66 est de l'ordre de 1,5–2 USD estimé pour toute une course.

**Ce qui n'est pas établi** (HYPOTHÈSE) : qu'un proposeur qui exécute produit plus de vraies découvertes par dollar (S1) ; que Kimi tolère l'appel d'outil forcé de Kaimen (S3) ; que Sakana survit à son enfermement (S4) ; que l'oracle a la puissance nécessaire au budget (S7) ; que Kimi n'a pas mémorisé les pièces publiques (S8) ; que `cout_usd` est exact (S10). Les critiques ont ajouté, et j'accepte : que le placebo est fidèle ; que l'échec du minimal n'informe pas sur les cadriciels riches (interaction non testée) ; que le témoin « filtre sur épisodes » est un instrument neuf, pas le témoin N-045.

**Risques** : budget insuffisant pour M (le plus probable, d'après le repère v66) ; alors la bonne réponse est « non départagé », écrite, plutôt qu'un bras cher non interprétable. Mémorisation : si E0′ sonne, replantage avant tout. Dégénérescence silencieuse de Sakana enfermé : couverte par la note sur le fond d'E3′.

**La mesure qui départage** : le contraste `exp-min` − `exp-placebo` d'E1′, lu sur l'oracle à coût apparié, après un A/A qui fixe M. Elle répond à « pourquoi pas lui ? » par : parce qu'on ne sait pas encore si l'exécution elle-même vaut son prix, et que Sakana la vend avec le paquet le plus cher et le moins étanche.

**Ce qui me ferait changer d'avis** : E0′ positif (priorité au replantage) ; A/A montrant que M dépasse le budget (on ne branche rien) ; E3′ bon marché en pratique avec note sur le fond conservée (alors (b) devant Kaimen comme second bras) ; la question du directeur lue comme « tester un produit pour le papier » (modification de revendication, hors de mon choix) ; `exp-min` ≤ témoin et `exp-text` ≤ témoin (on reste sur (c), sans dire que les cadriciels riches sont réfutés).

**Première expérience** : E0′, parce qu'elle coûte ≈ 1 USD (illustratif), ne consomme aucun monde, et que si elle sonne, tout le reste est à refaire.

FIN-DE-CELLULE