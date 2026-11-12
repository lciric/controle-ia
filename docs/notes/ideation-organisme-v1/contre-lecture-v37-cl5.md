# Contre-lecture CL5 du différentiel v36 → v37 de la prise « idéation » (orchestrateur du pôle v7)

Contre-lecteur neuf (règle R2) : Opus 5.5. Je n'ai écrit ni le code (auteur : une session servie par Fable 5.1) ni les
relectures précédentes. Relevés `date -u` : début vers 23:37, fin vers 23:55 UTC, le 28 octobre 2026.

Conditions : aucun réseau, aucune clé, aucun appel payant. Lu : `relecture-v37/` seulement, plus le kit d'agent installé
dans `venv-pole` (comment il passe la consigne). Le seul « Argon » joué est un script local (`outils-cl5/argon_factice.py`)
qui consigne ce qu'il reçoit. `pole/…`, `demonstrations/…` et `essais/…` désignent l'arbre `v37/orchestrateur-pole-v7/`.

## Verdict : **lançable après corrections**

Ce que la v37 apporte tient :
- le bras reste rejouable après un échec qui n'a lancé aucun processus ;
- une course réelle sans Argon est refusée ;
- les plafonds par défaut sont ceux du devis v7 bis ;
- la taille des pièces est bornée à 800 000, consignée, et un dépassement arrête toujours, sans jamais tronquer.

**Trois majeurs, aucun bloquant :**
- **CL37-01** : Argon proposeur joue toujours **après** Opus et Fable. Son contrôle porte sur 41 caractères, pas sur la
  consigne de ≈ 600 000. Une panne liée à la taille arrive donc après la passe 1 payée côté Claude (démontré).
- **CL37-02** : dans le bras, un appel de contrôle d'Argon qui **a coûté** est scellé « rien envoyé, rien dépensé ». Ce
  coût sort du journal et du plafond, et les relances sont illimitées (démontré).
- **CL37-03** : la somme des plafonds Claude en deux passes (41,4) dépasse le total (40). Le relais du devis (réserve de
  10 par appel) refuse tout appel au-delà de 30 dollars dépensés. Aucune garde ne vérifie cette cohérence : le dernier
  juge peut être refusé après 30 dollars dépensés (démontré sur le compteur et sur le cœur).

CL37-01 se corrige en quelques lignes, ou par une répétition payée de la commande d'Argon. CL37-03 se corrige par une
option du devis. CL37-02 peut attendre la v38 si le bras ne se joue qu'après elle.

## 1. Comptes vérifiés

**Empreintes.**
- `sha256sum -c EMPREINTES-orchestrateur-pole-v7-v37.txt` : **144 sur 144 conformes**, avant et après la relecture.
- Les compagnons `EMPREINTES-…-v37.txt.sha256` et `LISEZMOI-…-v37.md.sha256` sont conformes.
- Aucun fichier créé ni modifié dans `v37/` ni dans `v36/` : vérifié par `find -newer` et par l'absence de `__pycache__`.

**Différentiel.**
- `diff -rq` v36 ↔ v37 : seuls changent `pole/ideation.py`, `pole/adaptateurs.py`, `demonstrations/ideation_v1.py` et
  `essais/test_v7_ideation.py`.
- `diff-v36-v37.patch` est conforme à l'arbre : mêmes 201 lignes ajoutées ou retirées.

**Essais.**
- Commande demandée lancée sous `env -i`, sur une copie (`outils-cl5/copie-essais/`, car les essais écrivent dans
  `essais/_tmp`).
- Résultat : **320 essais, 320 réussis**, « OK », 187,4 s, code 0 (`outils-cl5/essais-sortie.txt`). Conforme au LISEZMOI.

**Mutations** (`outils-cl5/mutations.py`) : dix-neuf défauts réintroduits un par un dans une copie neuve, puis
`essais.test_v7_ideation` relancé (sorties : `mutations-sortie.txt` et `-bis.txt`).
- **Tuées (7)** : M2, M4, M9, M10, M14, M18, M19.
- **Survivantes (12)** : M1, M3, M5, M6, M7, M8, M11, M12, M13, M15, M16, M17.
- Une erreur de ma part, corrigée : nommer « M5-argon… » le dossier d'une copie fait échouer à tort
  `essais:690`, car l'essai cherche « argon » dans le chemin absolu. J'ai renommé les copies et rejoué M4 à M8.

## 2. Tableau des constats repris

« Discriminant » veut dire qu'au moins un essai échoue quand le défaut est réintroduit.

| constat | verdict | preuve | endroit |
|---|---|---|---|
| **CL36-01** bras perdu sans envoi | **corrigé en partie** | Commande introuvable, puis clé dans l'environnement : `manifeste-bras-non-joue-N` écrit, relance permise. Essai discriminant (M2 tuée) ; démontré aussi en S4bis. Après une dépense **du juge**, le bras est verrouillé (essai `test_bras_en_panne`, coût 0,2 compté). **Mais** un contrôle qui a coûté est scellé « rien dépensé » et laissé relançable (CL37-02). Le coût 0 sur commande introuvable n'est couvert par aucun essai (M3 survit), ni la condition d'écriture de `reponse.md` (M15 survit). | `ideation.py:1064-1066, 1164-1165, 1207-1216` ; `adaptateurs.py:440-442` |
| **CL36-02** contrôle d'Argon proposeur | **corrigé en partie** | Le contrôle a lieu avant la passe 1. Démontré en S1 : contrôle à t, consigne d'Opus écrite à t + 0,07 s. Son coût entre au journal et au plafond externe (`cout_externe_usd` 0,302 = 0,002 + 0,3 ; `cout_appels_de_controle_externes_usd` 0,002). **Mais** Argon reste joué après Opus et Fable, et son contrôle ne porte pas sur la taille (CL37-01). **Aucun essai** (M7 et M16 survivent). | `ideation_v1.py:366-371` ; `ideation.py:758-760` |
| **CL36-03** Argon obligatoire | **corrigé** | Le cœur refuse avant tout écrit si le juge **ou** le proposeur externe manque (lecture `:723-725`). L'essai couvre « sans proposeur » (M4 tuée), pas « sans juge » (M5 survit). Le lanceur refuse avant les appels de contrôle, après des vérifications locales seulement, donc sans dépense (lecture `:359-361`). Aucun essai (M6 survit). | `ideation.py:723-725` ; `ideation_v1.py:359-361` |
| **CL36-04** plafonds | **corrigé pour les défauts ; garde absente** | Défauts conformes au devis v7 bis (lecture `:70-73, 216-219`). L'essai ne vérifie que Fable proposeur (M11 survit). Le cœur **n'exige pas** que les plafonds par session tiennent dans le total (CL37-03). | `ideation_v1.py:70-73, 216-219` |
| **CL35-07** devis contre lanceur | **essai en partie** | `--commande-externe` seul : discriminant (M19 tuée). Commande avec `--juge-externe` seul, hors bras : aucun essai (M17 survit). `--variable-transmise GEMINI_API_KEY` : essai seulement sur l'adaptateur, et avec un autre nom de clé. | `essais:851-867` |
| **CL35-08** code 1 | **essai discriminant** | M18 tuée : moteur non armé → 2, sans trace. | `essais:862-866` |
| **CL35-09** réglages du kit | **essai en partie** | `--delai-session-s 0` : discriminant (M14 tuée). `reglages_kit` et `delai_session_s` au manifeste : aucun essai. | |
| **CL35-10** version de l'outil | **aucun essai** | Inchangé. | `ideation_v1.py:164-183` |
| **CL35-13** petit-enfant | **essai toujours non discriminant** | M1 (`killpg` → `kill`) survit, en 62 s. L'essai accepte désormais un processus zombie comme mort, mais ne borne toujours pas la durée. | `essais:538-568` |
| **CL35-14** sceau de l'attestation | **essai toujours non discriminant** | M13 survit : l'attestation « non scellée » de l'essai est aussi incomplète. | `essais:693-697` |

**Mineurs CL36-05 à 12** (non revendiqués) : 05 corrigé en partie (M1, M12, M13 survivent) ; 06, 07, 10, 11, 12
inchangés ; 08 toujours présent (S1 : commande appelée, `cout_fictif: true`) ; 09 élargi (CL37-04).

## 3. Taille des pièces (`--taille-max-pieces`)

- **Plafond dur tenu quoi qu'on passe**, au cœur : entier, non booléen, dans [1, 800 000] (`ideation.py:713-715`) ;
  démontré en S3 (900 000 refusé, code 2) ; essai discriminant (M9 tuée). Le lanceur n'a pas de borne propre
  (`type=int`) ; `lire_pieces` n'a pas de plafond dur à elle (`:208`), mais seul `executer_ideation` lui passe un réglage.
- **Tailles servies au manifeste** de départ : `taille_max_pieces` et `taille_pieces_servies` {proposeurs, juges,
  matériau} (`:786-788`) ; démontré en S1 (650 000 ; 500 000 / 0 / 0), en caractères après caviardage. La taille de la
  consigne entière n'est pas consignée (la consigne est scellée dans les traces).
- **Dépassement : arrêt, jamais troncature** (`:215-216` ; M10, troncature silencieuse, tuée). L'arrêt tombe avant tout
  appel **du cœur**, mais **après** les contrôles Claude et Argon du lanceur (S2, S3 : CL37-04).
- **Le plafond porte sur chaque lot, pas sur la consigne** (CL37-06).

## 4. Constats neufs

### CL37-01 — majeur — Argon proposeur joue après Opus et Fable ; son contrôle n'éprouve pas une grosse consigne

**Endroit.**
- `ideation.py:739` : `tous_proposeurs` liste Claude d'abord, puis les externes ;
- `ideation.py:857-861, 869-873` : boucles des deux passes ;
- `ideation_v1.py:367-371` : contrôle sur une consigne de 41 caractères, sous le rôle `juge_ideation`, au plafond 0,2.

**Défaut.** Démontré en S5, avec une commande factice qui répond au contrôle mais sort en code 3 au-delà de 100 000
caractères, comme le ferait un quota de jetons ou une taille de requête :
- le journal donne `opus ok 0,4 ; fable ok 0,4 ; argon erreur, 2,5 compté, coût inconnu` ;
- la course s'arrête, code 2, et `S5/` est consommé.

En réel, la passe 1 de Claude est payée à ce moment-là (plafonds 5 + 10). Avec le corpus primaire, les pannes les plus
probables d'Argon sont celles que la taille provoque : quota, taille de requête, délai de 900 s. Le contrôle ne les
touche pas. De plus, le contrôle passe sous `ROLE_POLE=juge_ideation` (journal de S1). Si la commande aiguille selon le
rôle, la voie « proposeur » n'est pas éprouvée.

**Correction.**
- Jouer les proposeurs externes **en tête** de chaque passe. Le confinement est inchangé, car Argon ne voit jamais les
  fiches des autres. En prime, son dossier ne côtoie plus les réponses Claude de la même passe (CL36-07).
- Faire le contrôle d'Argon sous le rôle `proposeur_ideation`.
- Ajouter au devis une répétition payée de la commande d'Argon sur la consigne scellée de la course simulée
  (≈ 604 000 caractères, au plus 2,5 dollars) avant la course.
- Essai : une commande qui échoue sur une grosse consigne → aucun appel Claude de proposition.

### CL37-02 — majeur — Bras : un contrôle d'Argon qui a coûté est scellé « rien envoyé, rien dépensé »

**Endroit.**
- `ideation.py:1150-1154` : le coût du contrôle n'entre au journal qu'après un succès ;
- `ideation.py:1207-1216` : `rien_envoye` est lu sur ce journal ;
- message en `:1215`.

**Défaut.** Démontré en S4 et S4bis :
- la commande, joignable, rend « KO » au contrôle, avec un coût de 0,15 ;
- `manifeste-bras-non-joue-1.json` est scellé avec `cout_total_usd: 0.0`, `controle: {}` et le message « rien envoyé,
  rien dépensé ; relance permise » ;
- la relance joue le bras ; le journal final donne 0,402 (contrôle 0,002 + juge 0,4) ;
- les 0,15 ne figurent nulle part, ni dans le plafond externe ;
- les relances sont illimitées.

Un contrôle qui dépasse son délai suit le même chemin : l'adaptateur compte le plafond de 0,2, puis il est perdu (constaté
à la lecture). Il n'y a pas de fuite : la consigne de contrôle ne porte aucune fiche. Mais un chiffre scellé est faux, ce
que R6 et le registre des dépenses interdisent.

Réponse à la question (01) : un échec après une dépense **du juge** verrouille le bras ; un échec après une dépense **du
contrôle** ne le verrouille pas et n'est pas compté.

**Correction.**
- Faire porter par l'exception d'`appel_de_controle` la lecture et son coût, puis l'ajouter au journal (le plafond si le
  coût est inconnu) avant toute décision.
- `rien_envoye` n'est vrai que si aucun processus n'a été lancé : commande introuvable, ou clé dans l'environnement.
- Sinon, écrire `bras-tentative-N.json` avec le coût. Ce coût s'impute au plafond externe des tentatives suivantes (au plus
  deux) et est repris au manifeste final.
- Essai inverse : contrôle « KO » à 0,15 → coût au manifeste et plafond diminué d'autant.

### CL37-03 — majeur (devis et garde absente) — Le dernier juge peut être refusé après 30 dollars dépensés

**Endroit.**
- devis v7 bis, point 3 ;
- `ideation.py:803-806` : la seule garde compare la dépense plus le plafond de la session au total, session par session ;
- `relais_reel.py:146-150` : réserve par appel.

**Défaut.** Démontré par `outils-cl5/plafonds_pire_cas.py` (sortie `plafonds-pire-cas-sortie.txt`).
- **Deux passes** (le devis compte Argon « 2,5 par passe ») : les plafonds Claude totalisent 0,4 + 2 × (5 + 10) + 7 + 4 =
  **41,4 > 40**. Si chaque session dépense son plafond, le cœur s'arrête **avant le juge Opus**, à 37,4 dépensés, sans
  classement ni bras.
- **Relais `--plafond-usd 40 --reserve-par-appel 10`** : tout appel est refusé (402) dès 30,01 dépensés. Le cœur, lui,
  lance le juge Fable jusqu'à 33 et le juge Opus jusqu'à 36. Entre 30 et 36, la session part, le relais la refuse, et la
  course s'arrête.

Mon estimation (SUPPOSÉE : barème du relais, 4 caractères par jeton, sorties de 15 000 à 40 000 jetons) met Claude
avant le dernier juge vers 11 à 18 dollars, loin de 30. Mais le haut de l'attendu du devis (36 au total) l'en approche.
Réponse à la question (04) : non, rien ne vérifie la cohérence entre plafonds par session, total et relais.

**Correction (devis), deux options :**
- (a) `--reserve-par-appel 4` : les sessions sont séquentielles. Un appel au-delà de la réserve est seulement journalisé,
  et peut porter le relais au-dessus de 40 du seul excédent du dernier appel. **Recommandée**, confiance moyenne.
- (b) Fable proposeur à 9,3, pour que la somme tienne dans 40. Cela ne règle pas l'écart avec le relais.

**Correction (code).** Le lanceur lit l'état du relais avant la course (`plafond_usd` et `reserve_par_appel_usd` y
sont) et refuse si `plafond − réserve` < total − plus petit plafond de juge ; le cœur consigne au départ la somme des
plafonds (contrôles et passes compris) et la refuse au-delà du total, sauf drapeau.

### CL37-04 — mineur — Les refus du cœur tombent après les contrôles, celui d'Argon compris ; défaut de 400 000 ≠ devis

**Endroit.**
- `ideation_v1.py:223-224` : défaut de 400 000 ;
- `ideation_v1.py:363-371` : contrôles avant `executer_ideation` ;
- `ideation.py:716-719` : `b < 0` laisse passer une valeur non numérique.

**Défaut.** Démontré, code 2 dans chaque cas :
- S2 : option oubliée, « pièces trop longues (500000 > 400000) » ;
- S3 : 900 000 ;
- S6 : `--budget-externe-usd nan`, refusé seulement à l'écriture du manifeste.

Dans les trois cas, les dossiers de contrôle Claude et Argon existent, et la commande factice a reçu son contrôle. En
réel, cela coûte au plus 3 × 0,2, consigné nulle part. S2bis : la relance dans la même SORTIE est permise.

C'est CL36-09, non corrigé, et élargi par CL36-02. La logique de CL36-04 (défauts égaux au devis) n'a pas été appliquée à
la taille : le devis demande 650 000.

**Correction.**
- Une fonction `verifier_reglages(...)`, appelée par le lanceur avant les contrôles : liste blanche, pièces et tailles,
  attestation, plafonds finis (`math.isfinite`).
- Défaut de 650 000, ou option exigée sur moteur réel.

### CL37-05 — mineur — Douze mutations sur dix-neuf survivent

**Endroit.** `essais/test_v7_ideation.py`.

**Défaut.**
- **M5** (juge externe oublié sur course réelle) survit : c'est exactement le cas de la décision n° 118.
- **M7 et M16** survivent : CL36-02 n'a aucun essai.
- **M8** survit, et la v37 en est la cause. Le dernier bloc de `test_bras_simule_sur_course_reelle_refuse` (`:802-806`)
  est désormais refusé par la garde CL36-03 (pas de juge externe), et non plus par la garde CL35-04 qu'il était censé
  éprouver.
- **M1, M12, M13** survivent, comme en CL4.
- **M3, M6, M11, M15, M17** survivent.
- **Fragilité** : `essais:690` cherche la sous-chaîne « argon » dans un chemin absolu. Démontré : l'essai échoue si le
  dossier de travail contient « argon ».

**Correction.** Essai « proposeur sans juge externe » ; un juge externe dans `:802-806` ; essai du lanceur avec une
commande factice (contrôle d'Argon avant toute passe, coût au journal) ; durée bornée dans l'essai du délai ; médiane ≠
moyenne ; attestation complète au sceau faux ; comparaison sur le dossier relatif.

### CL37-06 — mineur — Plafond dur par lot, pas par consigne ; jetons non mesurés

**Endroit.**
- `ideation.py:735-737` : trois lots bornés séparément ;
- `ideation.py:80` et LISEZMOI : « ≈ 200 000 jetons » ;
- devis, point 2.

**Défaut.**
- La consigne de passe 2 additionne pièces, matériau et fiches : jusqu'à 1,6 million de caractères.
- Les 560 000 caractères mesurés pour les juges viennent de fiches simulées, courtes. Une course réelle sert jusqu'à 52
  fiches réelles (SUPPOSÉ : + 100 000 à 200 000 caractères).
- La fenêtre d'Opus 5.5 et de Fable 5.1 est d'un million de jetons (table de la documentation de l'interface, en cache au
  6 octobre, non vérifiée en ligne) : ça tient.
- Mais le ratio de 4 caractères par jeton n'est pas mesuré. Le découpeur en jetons des modèles récents compte 1 à
  1,35 fois plus : les coûts du devis peuvent être bas d'un tiers.

**Correction.**
- Consigner la taille de chaque consigne au journal.
- Compter les jetons des consignes scellées de la course simulée avant le barème de session-depot.

### CL37-07 — mineur — Une interruption de l'opérateur laisse la commande d'Argon vivante

**Endroit.** `adaptateurs.py:438-452` : `start_new_session=True` ; seul le délai arrête le groupe.

**Défaut.** Démontré (`outils-cl5/interruption.py`) :
- SIGINT à l'orchestrateur pendant la commande ;
- l'orchestrateur sort (`KeyboardInterrupt`) ;
- la commande reste vivante ; je l'ai arrêtée par son identifiant de processus.

En réel, la session Argon continuerait de dépenser hors journal. Une interruption est plus probable avec des sessions
pouvant durer 900 s.

**Correction.** `except BaseException: os.killpg(p.pid, SIGKILL); raise` autour de `communicate`.

### CL37-08 — mineur (risque non démontré) — Bornes de temps et de sortie non réévaluées pour 150 000 jetons

**Endroit.** `adaptateurs.py:33` (1 800 s) ; `ideation_v1.py:222` (900 s).

**Défaut.**
- Fable 5.1 est documenté comme pouvant tenir « plusieurs minutes » par requête difficile.
- Un dépassement de délai est un arrêt dur, qui fait perdre la course après la dépense.
- Le juge rend jusqu'à 52 fiches × 5 justifications. Le cœur ne fixe pas la sortie maximale de l'outil. Une troncature
  donne « notes invalides », donc un arrêt, jamais un repli.

**Correction.** Au devis : `--delai-session-s 3600 --delai-commande-s 1800`. Le coût reste borné par le plafond de
session.

### CL37-09 — mineur — Écrits

LISEZMOI :22 « Opus 5 / 10, Fable 4 / 7 » (le code : proposeurs Opus 5 et Fable 10, juges Opus 4 et Fable 7) ; LISEZMOI
:27-28, relecture « en cours sur v35 → v36 », périmé ; LISEZMOI :19 « contrôle refusé sans coût » (le code relance aussi
après un contrôle qui a coûté) ; `ideation.py:686` « v36 » ; `ideation.py:8, 44-46` inchangés (CL36-11) ; lanceur
`:38-41` muet sur « bras non joué, relance permise », qui rend 2 comme un refus définitif. **Correction** : réécrire.

**Compte des constats neufs : 0 bloquant, 3 majeurs (CL37-01 à 03), 6 mineurs (CL37-04 à 09).**

## 5. Le devis v7 bis au regard du code

| point | code | verdict |
|---|---|---|
| Total Claude 40, Argon 9, plafond général 49 | défauts `ideation_v1.py:216-219` | conforme |
| Proposeurs Opus 5 / Fable 10, juges Opus 4 / Fable 7, contrôle 0,2 | `:70-71, 219` | conforme |
| Argon 2,5 par passe, juge 3,5 | `:72-73, 274-276` | conforme. Côté externe, le pire cas tient : 0,2 + 2 × 2,5 + 0,2 + 3,5 = 8,9 ≤ 9 (garde du bras `ideation.py:1122-1125`) |
| Relais `--plafond-usd 40 --reserve-par-appel 10` | hors du code | **incohérent** avec les plafonds par session : coupure à 30 (CL37-03) ; et 41,4 > 40 en deux passes |
| `--taille-max-pieces 650000` | défaut 400 000 | à passer explicitement ; un oubli est refusé après les contrôles (CL37-04) |
| « 320 essais » | — | conforme (démontré) |
| Tailles 604 000 / 560 000 « sous le plafond dur » | le plafond porte sur les lots | vrai des lots ; la consigne des juges grandira avec les fiches réelles (CL37-06) |
| Ordre de lancement | — | **absent du v7 bis** (« le reste des v2 à v7 vaut ») ; v7 absent ici, non vérifiable. À y mettre : répétition de la commande d'Argon à la taille réelle (CL37-01), puis course |

## 6. Ce que je n'ai pas pu vérifier

- **La commande réelle d'Argon** : quota, taille de requête, durée sur ≈ 600 000 caractères, aiguillage par rôle, coût
  déclaré contre facturé.
- **L'outil en ligne de commande réel** : durée et sortie maximale sur 150 000 jetons, comportement sur un refus 402 du
  relais, nombre d'appels par session (des appels simultanés multiplieraient la réserve de 10).
- **Le kit 0.2.174** passe la consigne sur l'entrée standard (`--input-format stream-json`) : aucune limite de longueur
  d'argument ; il borne à 1 Mo chaque message lu de l'outil, ce qu'aucun message attendu n'approche (non vérifié).
- **Barème et jetons** : barème du relais concordant avec la table de la documentation en cache, rien vérifié en ligne ;
  ratio caractères par jeton non mesuré.
- **Le GO par anticipation et les devis v2 à v7** : absents ici, hors de mon périmètre.

## 7. Fichiers produits

Sous `relecture-v37/` : ce rapport ; `outils-cl5/` (Argon factice, préparation, attestation, `scenarios.sh`, mutations et
leurs sorties, pire cas des plafonds, interruption, `essais-sortie.txt`, `copie-essais/` à supprimer à volonté) ;
`simulee/` (S1 nominale ; S2 et S2bis défaut oublié puis relance ; S3 900 000 ; S4 et S4bis contrôle du bras « KO » à
0,15 puis bras joué ; S5 Argon en panne sur grosse consigne ; S6 budget non numérique ; P1 pire cas). Aucun processus
laissé actif (vérifié par `ps`).
