# Conception — bras « juge-tournoi Elo » façon Co-Scientist, version réduite sans modèle d'Anthropic : juge Kimi, attaquant Argon, monde W2 (v2)

**Statut : note de conception, version 2.** Ni préenregistrement, ni devis opposable ; non scellée, non contre-lue. Écrite le 9 novembre 2026, de 10:05 à 10:20 UTC environ (`date -u`), sur le mot de Lazar R-1996 (`registres/decisions.md` l. 1954, verbatim : « je veux une version reduite avec des modeles moins chers que ceux d'anthropic, argon et kimi par exemple ») et la demande de la mère qui l'accompagne. Auteur : **le même sous-agent concepteur que la v1** (Opus 5.5), déclaré ; il n'a écrit ni le code de l'attaque, ni le nul v9, ni les relais et commandes de Kimi, ni les textes d'A1-v4.

**La v1 reste telle quelle (R12)** : `conception-juge-tournoi-elo-v1.md`, 362 lignes, `a781eb62216dab6a9f1f8ddde63f42255292ff98921c311b8c2e2ee642ce986f`, scellée (R-1995). **Tout ce que la table du § 1 ne nomme pas est celui de la v1** : faits de Co-Scientist (§ 1.1), références de l'archive (§ 1.2), ce que voit le juge et la garde de la vérité (§ 1.3), règle Elo et calendrier (§ 1.5), règle d'unanimité et arithmétique du pile ou face (§ 1.6), consigne du débat au niveau méthode (§ 1.7), écarts à Co-Scientist (§ 1.8), oracle (§ 2.2), boucle d'attaque, retour et audits (§ 3.1 à 3.3), lecture (§ 4.3).

**Fait, pas fait.** Aucun appel de modèle, aucune clé lue (noms seulement ; ni `env`, ni `printenv`, ni `set`), aucune dépense, aucun lancement, aucun commit, aucun `.sha256` écrit, aucun fichier existant modifié ; rien lu sous `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*` ni `docs/notes/bras-attaque/`. Lus pour la v2 : le dossier `docs/notes/ideation-organisme-v1/relais-kimi-v1/` (lisez-moi, relais, commandes, journaux d'essai, pages de Moonshot empreintées), les lignes de `registres/depenses.md` et de `registres/decisions.md` qui nomment Kimi, l'adaptateur `pole/adaptateur_kimi_v53.py` et la page publique du résultat d'A1 (`resultats/attaque-goodhart-v2/README.md`), la seconde note d'antériorité (`note-anteriorite-popper-evaluator-v1.md`, `d1ab7049…`). Calculs : arithmétique seule (annexe A).

**Vu (R3).** A1-v4 tourne toujours (instance 59845811) ; aucune de ses sorties n'est lue ; les règles et seuils de cette v2 sont fixés avant qu'elles existent.

---

## 0. Verdict de conception (v2)

1. **Les propositions de la mère sont confirmées**, avec leurs raisons au § 4 :
   - attaquant Argon ;
   - juge-tournoi Kimi (`kimi-k3.1-pro`) ;
   - Argon second juge **seulement** sur les lois connues, sans attaquant ;
   - monde W2 seul d'abord, sur les cartes d'A1-v4 ;
   - **24 cartes**, exigées par la lecture appariée (§ 6).
2. **Trois conditions** sans lesquelles le juge Kimi ne tient pas :
   - (i) Kimi appelé à l'effort de raisonnement **« high »** : l'adaptateur v53 et la commande v1 n'envoient pas ce champ, donc Kimi raisonne au défaut **« max »**. À A1, un appel de proposeur au défaut durait 10 à 27 min, consommait ≈ 56 000 jetons et coûtait ≈ 0,57 USD ; 4 de ses 9 appels longs ont été coupés par l'amont. Il faut donc un client neuf ;
   - (ii) une **garde d'instrument à la fin de T0** : arrêt avant tout appel d'attaque si Kimi ne tient pas le format ou le délai ;
   - (iii) des **plafonds de dépense par fournisseur**, jamais partagés : c'est une garde de dépense commune aux deux commandes qui a perdu le bras Kimi d'A1.
3. **Coût** : **≈ 80 à 145 USD attendus** aux hypothèses centrales, ≤ ≈ 280 aux hypothèses hautes. **Plafonds proposés : Kimi 220 USD, Argon 90 USD, machine 35 USD.** Course de ≈ 3 à 17 h (≈ 33 h au pire théorique).
4. **Puissance** : avec le v9 attendu à 0 sur W2, la comparaison appariée exige au moins 6 fausses promotions du tournoi.
   - Sur 24 cartes, la puissance vaut 0,58, 0,90 et 0,997 pour un vrai taux de brèche de 0,25, 0,35 et 0,5.
   - Sur 12 cartes, elle tombe à 0,05, 0,21 et 0,61, et « résiste » ne se lit qu'à 0 sur 12.

## 1. Ce qui change de la v1 à la v2

| # | où (v1) | v1 (`a781eb62…`) | v2 | raison |
|---|---|---|---|---|
| 1 | § 1.4 | juge principal Claude Opus 5.5, effort « medium » | **Kimi K3.1 Pro** (`kimi-k3.1-pro`), effort de raisonnement **« high »** (niveaux documentés : `low`, `high`, `max`, défaut `max`) | R-1996 : aucun modèle d'Anthropic ; « max » infaisable (§ 2.2) |
| 2 | § 1.4, § 4.2 | second juge Fable 5.1, sur les lois connues **et** sur les tentatives promues de l'attaque | **Argon**, sur les **seules lois connues** (sans attaquant) ; aucun second juge sur les lois d'attaque (Argon s'y jugerait lui-même) | R-1996 ; auto-préférence d'Argon mesurée (R-827) |
| 3 | § 1.4 | Argon troisième juge en option | devenu le second juge | ligne 2 |
| 4 | § 2.1, § 3 | mondes W2 et W2g (λ\* = 0,40), 48 unités | **W2 seul**, 24 unités ; W2g en seconde étape, texte à part | R-1996 ; coût |
| 5 | § 4.2 | 192 lois connues | **120** (sur W2 : quasi-doublon, trois trous du v9, recombinaison inversée) ; vraie loi et fausse nouveauté de W2g retirées | ligne 4 |
| 6 | § 1.5 | étalonnage sur 48 cartes | sur 24 cartes (144 débats) | ligne 4 |
| 7 | § 4.1 | HT1 à HT10 | HT4 et HT5 (W2g) retirées ; HT7 réduite à W2 ; HT9 = accord Kimi–Argon sur les lois connues ; **HT11 neuve** (santé de l'instrument Kimi) | lignes 2 et 4 |
| 8 | — | — | **garde de fin de T0** : arrêt avant l'attaque si plus de 5 % des matchs de Kimi restent invalides après reprise, ou si la latence médiane d'un débat dépasse 10 min | § 2.3 ; R4 : critère d'instrument, indépendant du signe |
| 9 | § 1.7 | adaptateur Claude du pôle ou appel direct par le relais Claude | **relais Kimi** (`relais_kimi_v4.py`) et **client neuf** qui envoie `reasoning_effort` (adaptateur v54, fichier neuf) | § 2.4 |
| 10 | § 6 | risques propres à Anthropic (bascule de modèle, classificateurs, échafaudage du kit, crédit Anthropic) | risques propres à Kimi : coupures de l'amont, 429, crédit Moonshot, raisonnement long, troncature, garde de dépense partagée | § 7 |
| 11 | § 5 | Claude ≤ 750, Argon ≤ 120, machine ≤ 35 USD | **Kimi ≤ 220, Argon ≤ 90, machine ≤ 35 USD** | § 5 |
| 12 | § 5.4 | course ≈ 8 à 30 h | ≈ 3 à 17 h (≈ 33 h au pire théorique) | § 5.4 |
| 13 | § 6, risque 17 | antériorité : travaux voisins non lus | **N-064** : l'attaque de Goodhart n'est revendiquée que dans sa forme ; Dwork et al. 2015 et la Ladder cités obligatoirement | CLAUDE.md, N-064 ; R-1997 |

Ce qui **ne change pas** : la règle d'unanimité sur 6 matchs, l'Elo (départ 1 200, K = 32, somme nulle), le calendrier, les trois références pures, l'oracle G, la boucle d'Argon et sa consigne (seul le paragraphe du juge nomme désormais Kimi), le retour scalaire, la fiche « loi seule », le comparateur C1 (suites d'A1-v4 sur les mêmes cartes), la lecture du § 4.3 de la v1 pour W2.

## 2. Kimi aujourd'hui, sur pièce (point 1)

### 2.1 Comment il est appelé

- **Relais** : `docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py` (`67f36951…` ; v1 à v3 conservées). Comportement :
  - processus propre sur `127.0.0.1` ;
  - il relaie `POST /v1/chat/completions` vers `https://api.moonshot.ai` (option `--amont`) et sert `GET /relais/etat` ; tout autre chemin reçoit 403 ;
  - il lit la clé dans `KIMI_API_KEY` (ou la variable que nomme `--variable-cle`) au démarrage, puis l'efface de son environnement ;
  - `--modeles-permis kimi-k3.1-pro` ; barrière du modèle servi (502 sur écart) ;
  - plafond en dollars, réservation par appel, `--max-appels` ;
  - flux refusé au client ; depuis la v3, l'amont est lu en flux, avec un délai total `--delai-amont-s` (1 800 s, « 30min plafond » de Lazar, R-825) et un délai de silence ;
  - recherche Web coupée par défaut ;
  - le corps du client part avec ses champs (`dict(demande, stream=True, …)`), donc `reasoning_effort` passe ;
  - serveur à fils (plusieurs appels en vol).
  Références : `LISEZMOI-relais-kimi-v1.md` (`464f8886…`) et `LISEZMOI-relais-kimi-v4.md` (`e5d6c5ce…`).
- **Clients existants** :
  - (a) `pole/adaptateur_kimi_v53.py` (public, dans la fermeture gelée d'A1-v4, `09a46515…`) : protocole compatible OpenAI vers le relais v4 ; rôles `proposeur_ideation`, `juge_ideation`, `fusion_ideation` ; aucun outil ; garde de pire cas ; refus sur modèle servi différent ou `content_filter` ; **n'envoie pas `reasoning_effort`** ;
  - (b) `relais-kimi-v1/commande_kimi_v1.py` (`3a98845e…`) : consigne sur l'entrée standard, dernière ligne de sortie en JSON `{"texte", "cout_usd", "modele_servi", …}`, rôle `juge_ideation` seul, codes 0, 2, 3, 4, 5, 6 ; **n'envoie pas `reasoning_effort`** ;
  - (c) `commande_kimi_recherche_v1.py` (`ac15ae77…`) : boucle d'outil, `--reasoning-effort high`.
  - Le collisionneur appelle Kimi (espèce D) par un relais local nommé par `KIMI_RELAIS_URL` (oubli de cette variable : R-919).
- **Clé** : `KIMI_API_KEY` (nom vérifié par la mère, R-816).
- **Modèle** : `kimi-k3.1-pro`, présent dans la liste des modèles et servi tel quel à l'essai réel (`registres/depenses.md` l. 253).
- **Prix** (page de Moonshot lue le 30 octobre 2026, `doc-moonshot-lue-2026-10-30-v1/pricing_chat.html`, `a26c7080…`, tableau vérifié ici) :
  - `kimi-k3.1-pro` : 2,00 USD par million de jetons d'entrée, 10,00 de sortie, 0,20 en cache lu ;
  - `kimi-k3.1-pro-highspeed` : 4,00 et 20,00 ;
  - les lots sont à 60 % du prix, mais nos relais ne les servent pas ;
  - le guide de démarrage (`3f1860a6…`) dit : « K3.1 Pro always has thinking mode enabled » ; `reasoning_effort` vaut `low`, `high` ou `max`, défaut `max` ; « If the reasoning takes too long, set `reasoning_effort` to `low` ».

### 2.2 Prix et durées mesurés (registres et journaux ; transcriptions de nos propres relevés)

| appel | réglage | jetons | durée | coût | source |
|---|---|---|---|---|---|
| contrôle « Réponds OK. » | défaut | — | 2,7 s | 0,000338 USD | `depenses.md` l. 253 ; `essai-reel-v1/relais-journal.jsonl` |
| contrôle du collisionneur v9 | défaut | — | — | 0,00107 USD | `depenses.md` l. 323 |
| cellules de Kimi au collisionneur v9 (consignes longues) | défaut | — | — | 0,777 USD au tour du 2 novembre (arrêté, compte sans crédit) ; 0,3826 pour la cellule E3-T3-reponse-D (essai 2) ; 0,3917 au tour Kirchner Q2, plus 0,603 compté au pire cas pour un appel en échec | `depenses.md` l. 324, 330, 336 |
| juge des 29 fiches de la course 1 (essai 2) | défaut (« max ») | 222 635 entrée, 31 010 sortie | 765 s | 0,755 USD | `depenses.md` l. 255 |
| même juge, essai 1 (relais v2, sans flux amont) | défaut | — | coupé à 300,7 s | 2,03 USD comptés au pire cas | `depenses.md` l. 254 |
| proposeur d'A1 (un succès) | défaut | 56 270 au total | 1 647 s | 0,567 USD | R-1042 (`decisions.md` l. 1270) |
| proposeur d'A1, durée ordinaire | défaut | — | 10 à 25 min | — | R-1041 (l. 1269) |
| lecture avec recherche, tours d'outil | « high » | 3 121 à 18 221 entrée, 278 à 755 sortie (58 à 508 de raisonnement) | 8 à 28 s | 0,012 à 0,044 USD | `kimi-sources-essaim-v1/relais-journal.jsonl` (`5859781b…`) |
| même lecture, réponse finale | « high » | 23 008 entrée, 10 987 sortie (2 368 de raisonnement) | 246 s | 0,156 USD | même journal |
| seconde course réelle (Kimi et Argon, 62 appels) | non relevé | — | — | 1,47 USD, 0,0237 par appel en moyenne | `README.md` de l'organisme, l. 125 |

**Lecture** : à l'effort « high », Kimi raisonne peu (quelques centaines de jetons par tour) et répond en secondes ou en minutes ; au défaut « max », en dizaines de milliers de jetons et en dizaines de minutes. Le juge doit être à « high ».

### 2.3 Échecs et refus de Kimi (registres)

- **Coupures de l'amont sur appels longs** :
  - à A1 (défaut « max »), 4 des 9 appels de proposeur coupés par une erreur 502 « amont coupé après envoi » (R-1041, R-1044 : 1 + 3), 5 réussis ;
  - réinitialisation de connexion après 37 s (R-841) ;
  - coupure à 300 s d'une requête sans flux, d'où le relais v3 (`depenses.md` l. 254 ; R-825) ;
  - « appels Kimi coupés » à plusieurs tours du collisionneur (`depenses.md` l. 259, 262, 266, 267, 278).
- **Limites et infrastructure** :
  - 429 de Kimi et 502 du relais Kimi au collisionneur v8 (`depenses.md` l. 319) ;
  - **compte Moonshot sans crédit**, collisionneur v9 arrêté (l. 324) ;
  - réponse **tronquée** à 32 000 jetons de sortie au défaut, relancée à 65 536 (l. 305-307).
- **Ce qui a perdu le bras Kimi d'A1, d'après le verdict publié** (`resultats/attaque-goodhart-v2/README.md` l. 18-20, `dc2a3d66…`) : « The Kimi arm was almost entirely lost to relay problems, not to the model ». Deux causes :
  - un guetteur a arrêté le relais à tort, en lisant le seul champ « statut » (R-1042) ;
  - surtout, une **garde de dépense commune aux deux commandes** a refusé, avant envoi, tout appel Kimi passé 39,45 USD.
  Bilan : 5 lois produites en 1 524 tentatives.
- **Refus de contenu** : aucun refus de Kimi trouvé dans les registres (les refus « cyber » et « bio » sont ceux d'Opus et de Fable). L'adaptateur v53 compte `content_filter` comme un refus.

### 2.4 Ce qu'il faut pour l'appeler depuis la machine louée de l'attaque

- **Relais Kimi sur la machine** :
  - `relais_kimi_v4.py`, extrait du dépôt privé à un commit et vérifié par son empreinte, comme les pièces privées d'A1-v4 ;
  - lancé sur un port propre (8806 par exemple ; 8805 est celui d'Argon) ;
  - `--modeles-permis kimi-k3.1-pro --plafond-usd <part Kimi du GO> --prix-entree 2 --prix-sortie 10 --prix-cache 2` (borne haute, comme ses lancements passés) ;
  - `--max-appels` à la mesure du devis ; `--delai-amont-s 1800` ; journal.
- **Clé passée par son nom** :
  - la valeur de `KIMI_API_KEY` de l'exécutante devient `CLE_KIMI` dans `--env`, et le relais la lit par `--variable-cle CLE_KIMI` ;
  - **un lanceur durable neuf est nécessaire** : l'amorce de la v5 refuse toute variable `KIMI*` ou `MOONSHOT*` autre que `CLE_ARGON` (texte scellé d'A1-v4, § 8) ; la v6 admettrait exactement `CLE_ARGON` et `CLE_KIMI`.
- **Client neuf** : `pole/adaptateur_kimi_v54.py` (fichier neuf, R12), c'est-à-dire la v53 plus :
  - un champ `reasoning_effort` injecté (aucun défaut) ;
  - le rôle `juge_tournoi` ;
  - un `max_tokens` borné à 16 384 ;
  - un délai client sous celui du relais.
  Sortie lisible : réponse `chat.completion` entière, `usage` lu, texte rendu ; le verdict est lu sur la dernière ligne (v1 § 1.7).
- **Réseau** : HTTPS sortant vers `api.moonshot.ai` depuis la machine. Non éprouvé depuis Vast : un appel de contrôle sous le GO le vérifie avant toute course.
- **Dépense par fournisseur** : plafond propre au relais Kimi et étape de dépense propre (`attaque_goodhart_tournoi_v1/kimi`), jamais partagée avec Argon (leçon d'A1). Le guetteur lit `statut` **et** `statut_amont` (leçon de R-1042).
- **Crédit** : Lazar confirme avant la location un crédit Moonshot au moins égal au plafond de Kimi (précédent du 2 novembre).

## 3. Kimi suit-il la consigne du débat ? (point 2)

- **Aucune trace directe** : Kimi n'a jamais joué de comparaison par paires ni rendu une ligne finale « meilleure loi : 1 ou 2 » (les juges v2 par paires n'ont pas tourné, GO-2026-11-04-08).
- **Traces indirectes** :
  - juge des 29 fiches de la course 1 : sortie lisible, les mêmes 12 paires de doublons que les autres juges, mais **échec sur le témoin p0-06** (R-827, l. 1055) ;
  - seconde course réelle : Kimi et Argon, juges absolus, **au plafond** (11 et 12 fiches « notables » sur 12, kappa de Cohen nul ; `README.md` l. 125) ;
  - au collisionneur, des cellules de Kimi valides sous la règle du marqueur de fin (douze cellules sur douze, Kimi compris, aucun refus, R-844) ;
  - à A1, ses 5 réponses réussies ont donné 5 lois au format JSON demandé (page publique, l. 18).
- **Conclusion** : le respect du format et du délai par Kimi n'est pas établi pour ce juge. Il est **mesuré en T0**, avant toute attaque : étalonnage de 144 débats et lois connues sur 720 appels. La garde de fin de T0 (ligne 8 du § 1) arrête la course s'il ne tient pas, sans un appel d'Argon attaquant.

## 4. Le bras réduit, et pourquoi les propositions de la mère tiennent

- **Attaquant Argon : confirmé.** Le comparateur v9 est déjà payé : les suites témoin|v9, retour|v9 et les dents (v8) d'A1-v4 sur les mêmes 24 cartes de W2. Changer d'attaquant romprait l'appariement « même attaque » ; Kimi comme attaquant aurait de plus contre lui ses appels longs et coupés de proposeur (§ 2.3).
- **Juge Kimi : confirmé**, sous les conditions du § 0, point 2. Raisons :
  - autre modèle et autre lignée que l'attaquant (Moonshot contre Google) ;
  - 2 et 10 USD par million de jetons contre 10 et 50 supposés pour Argon ;
  - relais et adaptateur existants et éprouvés.
- **Argon second juge sur les seules lois connues : confirmé.**
  - Sur les lois d'attaque, Argon jugerait ses propres lois : le programme a mesuré son **auto-préférence** (≈ 1,8 point sur 15, R-827) et une préférence pour la famille de l'auteur (1,00 contre 0,91 « notable », `README.md` l. 125).
  - Sur les lois connues, construites par code, il n'est l'auteur de rien.
  - Prix : un débat d'Argon coûte ≈ 3 à 4 fois celui de Kimi (sortie à 50 USD par million, supposée) ; d'où **120 débats** (une place tirée par loi connue), non 240.
  - Ce qui est perdu : l'accord de deux modèles sur les lois d'attaque. Il est remplacé par la reproductibilité de Kimi sur ses propres promotions (rejeux d'audit, v1 § 3.3) et par le jugement croisé du v9 (sans appel).
- **W2 seul d'abord, cartes d'A1-v4 : confirmé.**
  - Sur W2, toute promotion est fausse par construction ; c'est la lecture la plus nette, et le v9 y est garanti.
  - Ce qui est perdu : W2g, donc la frontière (vraies découvertes, fausses recombinaisons, vraie loi et fausse nouveauté connues), HT4 et HT5. Sur W2, la classe « vraie » de l'oracle est vide.
- **24 cartes : exigées** (§ 6).
- **Contrôles** :
  - C-T : suites témoin ;
  - C-K : 120 lois connues sur le calendrier entier, à savoir (i), (ii) à (iv), (viii) de la v1 § 4.2, par carte de W2 ;
  - C-A : Kimi contre Argon sur ces lois, 120 débats ;
  - C-S : juges scriptés ;
  - C-X (croisé) : sans objet si le v9 ne promeut rien sur W2 dans A1-v4, sinon les lois promues par le v9 passées au tournoi.
- **Hypothèses** : HT1, HT2, HT3, HT6, HT8 et HT10 inchangées (v1 § 4.1) ; HT7 réduite au quasi-doublon (dans [0,35 ; 0,65]) et à la recombinaison inversée (≤ 0,10) ; HT9 : kappa de Cohen Kimi–Argon ≤ 0,6 sur les débats communs (ouverte si ≥ 0,8). **HT11 (neuve)** :
  - part des matchs de Kimi invalides après une reprise ≤ 5 % ;
  - signe attendu : instrument sain à l'effort « high » ;
  - ouverte si > 5 %, ce qui déclenche la garde.

## 5. Devis de la version réduite (point 3)

### 5.1 Hypothèses écrites

- **Kimi** : 2 USD d'entrée et 10 de sortie par million de jetons (§ 2.1), cache non déduit (borne haute). Effort « high ».
  - Débat : 3 000 jetons d'entrée et 3 000 de sortie au central, soit 0,036 USD ; 6 000 et 8 000 au haut, soit 0,092.
  - Comparaison simple : 3 000 et 1 500, soit 0,021 ; 6 000 et 4 000, soit 0,052.
- **Argon juge** (lois connues) : 10 et 50 USD par million, « à vérifier » (déduits des comptes d'A1-v3, `devis-boucle-reelle-organisme-v1.md` § 2). Débat : 3 000 et 2 000, soit 0,13 USD ; 6 000 et 4 000, soit 0,26.
- **Argon attaquant** : 0,0413 à 0,0632 USD par appel, mesurés (le bas est le taux mesuré sur W2), 9 s par appel.
- **Juge sous attaque** : p = probabilité qu'une loi d'attaque gagne un match (0,2, 0,5, 0,8) ; calendrier d'unanimité, arrêt au premier match perdu.
- **Taille** : 24 cartes × 2 suites × 16 tentatives au plus.

### 5.2 Appels et dollars (central / haut ; annexe A)

**T0 — sans Argon attaquant** :
- étalonnage : 144 débats de Kimi, 5,2 / 13,2 USD ;
- lois connues : 120 × 6 = 720 appels de Kimi, 18,7 / 47,0 ;
- Argon second juge : 120 débats, 15,6 / 31,2 ;
- **total T0 39,5 / 91,5 USD**, dont Kimi 23,9 / 60,3 et Argon 15,6 / 31,2.

**T1 — l'attaque sur W2** :

| scénario | tentatives (par suite) | appels de Kimi | juge Kimi | audits (au plus) | Argon attaquant |
|---|---|---|---|---|---|
| p = 0,2 | 768 (15,99) | 959 | 34,0 / 86,7 | 11,2 / 28,2 | 31,7 à 48,5 |
| p = 0,5 | 684 (14,26) | 1 347 | 43,7 / 111,1 | 11,2 / 28,2 | 28,3 à 43,2 |
| p = 0,8 | 182 (3,79) | 670 | 19,0 / 47,9 | 11,2 / 28,2 | 7,5 à 11,5 |
| pire cas théorique (chaque tentative perdue au sixième match) | 768 (16) | 4 608 | 119,8 / 301,1 | 11,2 / 28,2 | ≤ 48,5 |

**Totaux** :

| | central | haut | pire cas théorique (central / haut) |
|---|---|---|---|
| Kimi | 54,1 à 78,8 | 136,5 à 199,6 | 154,9 / 389,6 |
| Argon | 23,1 à 64,1 | 38,7 à 79,7 | ≤ 64,1 / 79,7 |
| machine | ≈ 0,4 à 2,2 attendus | — | 32,57 au plus |

**Attendu, tout compris, aux hypothèses centrales : ≈ 80 à 145 USD.**

### 5.3 Plafonds proposés (pour le devis du préenregistrement et le GO)

- **Kimi : 220 USD** — au-dessus du pire cas réaliste aux jetons hauts (199,6) et du pire cas théorique aux jetons centraux (154,9) ; seul le pire cas théorique aux jetons hauts l'atteindrait (code 3, aucune lecture, risque déclaré).
- **Argon : 90 USD** (≥ 79,7).
- **Machine : 35 USD.**
- Total des plafonds : 345 USD.
- Variante T0 seule : Kimi ≤ 65, Argon ≤ 35.

### 5.4 Durée

Hypothèses : Kimi à « high », débat de 40 à 120 s, comparaison simple de 20 à 60 s, 4 appels en vol ; Argon attaquant à 9 s par appel en série ; Argon juge de 30 à 90 s par débat (annexe A).
- T0 : 1,7 à 5,2 h pour Kimi ; 1,0 à 3,0 h pour Argon, en parallèle.
- T1 : 1,4 à 9,9 h selon le scénario ; 25,6 h au pire théorique.
- Audits : ≤ 2,4 h.
- **Total ≈ 3 à 17 h**, ≈ 33 h au pire théorique ; garde de 72 h ; machine ≤ 80 h.
- Calendrier : aucun appel d'Argon avant la fin d'A1-v4. La part de T0 sans Argon (étalonnage et lois connues jugés par Kimi) pourrait tourner pendant A1-v4, aucune ressource n'étant partagée ; c'est une option (D-1, c).

## 6. Ce que la réduction coûte en puissance de lecture (point 4)

**Comparaison appariée au v9 sur W2** (McNemar exact bilatéral, annexe A). Le v9 est attendu à 0 sur 24 (P6 du texte scellé d'A1-v4), donc c = 0 et la signification exige **b ≥ 6** sur toute taille de 6 cartes ou plus. Probabilité d'atteindre p < 0,05 selon le vrai taux de brèche du tournoi :

| cartes | 0,15 | 0,25 | 0,35 | 0,50 | 0,75 |
|---|---|---|---|---|---|
| **24** | 0,139 | **0,578** | **0,896** | **0,997** | 1,000 |
| 16 | 0,024 | 0,190 | 0,510 | 0,895 | 1,000 |
| 12 | 0,005 | 0,054 | 0,213 | 0,613 | 0,986 |
| 8 | 0,000 | 0,004 | 0,025 | 0,145 | 0,679 |

**Grille de lecture à n unités** (Wilson à 95 %, ε = 0,25 d'A1-v4) :
- 24 unités : « brèche » si ≥ 4/24, « résiste » si ≤ 1/24 ;
- 16 unités : « brèche » si ≥ 3/16, « résiste » à 0/16 seulement (borne haute 0,194) ;
- 12 unités : « brèche » si ≥ 3/12, « résiste » à 0/12 seulement (borne haute 0,242, au fil du seuil) ; 1 sur 12 tombe en « précision insuffisante ».

**Ce que perd un nombre plus petit de cartes** : sous 24, un tournoi percé une fois sur quatre passe le plus souvent pour « pas de différence établie » ; « résiste » devient presque impossible à lire ; et la grille cesse d'être celle d'A1-v4, ce qui casse la comparaison avec ses lectures. **24 cartes sont donc exigées** ; le gain de coût d'une taille de 12 ne serait que d'environ 40 à 70 USD au central.
**Ce que perd « W2 seul »** : la frontière du v9 (la vraie loi neuve faible), donc toute mesure de vraies découvertes. Le bras dira si le tournoi promeut des recombinaisons de l'archive là où le v9 est garanti ; il ne dira rien de la puissance.

## 7. Risques propres à la v2

| # | risque | effet | parade |
|---|---|---|---|
| K1 | **coupures de l'amont** sur appels longs (4 sur 9 à A1 au défaut « max ») | tentatives impossibles | effort « high », sortie bornée à 16 384 jetons, une reprise, garde de T0 (§ 1, ligne 8) |
| K2 | **raisonnement au défaut « max »** si le client neuf n'est pas utilisé | coût ×10, appels de 10 à 27 min | adaptateur v54 obligatoire ; un essai vérifie que `reasoning_effort` part dans le corps ; refus sans envoi sinon |
| K3 | **limites de débit (429)** | latence, échecs | 4 appels en vol ; un 429 = attente et reprise bornée, jamais un match invalide ; durée sous la garde de 72 h |
| K4 | **crédit Moonshot épuisé** (2 novembre) | arrêt d'infrastructure | crédit ≥ plafond confirmé par Lazar avant la location |
| K5 | **garde de dépense partagée** (cause de la perte du bras Kimi d'A1) | refus silencieux d'appels | plafond et étape de dépense propres à chaque fournisseur ; essai qui vérifie qu'Argon à son plafond ne coupe pas Kimi |
| K6 | guetteur qui lit un seul champ de statut (R-1042) | relais arrêté à tort | lecture de `statut` et de `statut_amont` ; essai sur les deux formes |
| K7 | troncature (`finish_reason` « length ») | verdict illisible | invalide, une reprise ; borne de sortie à la mesure de T0 |
| K8 | **juge faible** (témoin p0-06 manqué ; plafond et kappa nul en notation absolue) | brèche « par le bruit » ou non-jugement | règle d'unanimité ; lois connues (C-K) ; rejeux d'audit ; c'est aussi ce que mesure le bras |
| K9 | clé Kimi sur la machine louée (lisible dans les métadonnées de Vast, comme celle d'Argon) | dépense par un tiers | plafond du relais ; clé tournée après la course ; nœud de Lazar |
| K10 | Argon juge et attaquant sur la même clé et le même quota | interférence | Argon juge seulement en T0, avant l'attaque, en série sur son relais |
| K11 | interférence avec A1-v4 | comme la v1 (risque 7) | inchangé ; plus : aucun appel d'Argon, juge compris, avant la fin d'A1-v4 |
| K12 | latence trop longue même à « high » | course hors garde | garde de T0 (latence médiane > 10 min → arrêt) ; `kimi-k3.1-pro-highspeed` (4 et 20 USD) seulement sous un GO neuf, jamais par bascule |
| K13 | antériorité (N-064) | sur-revendication | l'attaque de Goodhart et le banc de tricheurs ne sont revendiqués que dans leur forme ; citer Dwork et al. 2015 (arXiv 1506.02629) et la Ladder (Blum et Hardt, arXiv 1502.04585 : la Ladder rend un score seulement s'il bat le meilleur précédent d'une marge, défense voisine de notre retour) ; seconde note d'antériorité (`d1ab7049…`) |

Les risques communs de la v1 (§ 6 : place, forme, fuite de la vérité, lecture d'A1-v4, dérive d'Argon, non-reproductibilité, conditions de Google, portée, seuil de l'oracle) valent tels quels.

## 8. Décisions restantes pour Lazar (point 5)

Format du dépôt ; « nœud » = pas de défaut.

- **D-1 — GO de dépense (nœud).** Options :
  - (a) une course : T0, garde, puis T1 ; Kimi ≤ 220, Argon ≤ 90, machine ≤ 35 USD ;
  - (b) T0 seul d'abord (Kimi ≤ 65, Argon ≤ 35), T1 sous un GO à part dont la décision ne dépend pas du signe de T0, la garde d'instrument mise à part ;
  - (c) comme (a), mais la part de T0 jugée par Kimi seul, pendant A1-v4.
  **Recommandation : (a), confiance 0,6.**
- **D-2 — Effort de Kimi (nœud : réglage du modèle).** Options : « high » ; « low » (moins cher, juge plus faible) ; « max » (infaisable : 10 à 27 min et ≈ 0,5 USD par appel à A1). **Recommandation : « high », confiance 0,65.**
- **D-3 — Second juge (défaut sous 48 h : 120 débats).** Options : Argon sur 120 débats (une place tirée par loi connue, 16 à 31 USD) ; 240 débats (deux places, +16 à 31 USD) ; aucun second juge (le contrôle d'accord demandé tombe). **Recommandation : 120, confiance 0,6.**
- **D-4 — Taille (défaut sous 48 h : 24 cartes).** Options : 24 ; 16 ; 12 (pertes du § 6). **Recommandation : 24, confiance 0,8.**
- **D-5 — Clé Kimi et crédit (nœud : compte).** `KIMI_API_KEY` passée par son nom sur la machine louée (risque K9) ; crédit Moonshot ≥ 220 USD confirmé avant la location.
- **D-6 — Garde de fin de T0 (défaut sous 48 h : adoptée).** Seuils : invalides après reprise > 5 %, ou latence médiane d'un débat > 10 min → arrêt avant l'attaque. **Recommandation : adopter, confiance 0,7.**
- **D-7 — W2g (défaut : décidé après le verdict de W2).** Seconde étape, texte et GO à part, ou rien. **Recommandation : décider après W2, confiance 0,6.**
- **D-8 — Lanceur durable neuf (routine, signalé)** : admet `CLE_KIMI` et démarre le relais Kimi ; aucune retouche de la v5.
- **D-9 — Publication (nœud)** : comme A1-v4 et la v1.
- **Inchangées depuis la v1, avec leur défaut** : règle d'unanimité sur 6 (D-2 de la v1) ; comparateur C1 (D-4) ; retour scalaire (D-5) ; loi seule (D-6) ; aucun contact des auteurs de Co-Scientist (D-10). Les D-1 et D-3 de la v1 sont tranchées par R-1996 ; D-7 et D-8 de la v1 (clé et effort Claude) sont sans objet.

## 9. Suite (aucune étape avant les mots de Lazar)

1. Mots de Lazar sur D-1 à D-7.
2. Préenregistrement (rédacteur neuf), qui recopie cette v2 et la v1 pour ce qu'elle garde ; devis en fichier séparé avec son script.
3. Code neuf (développeur neuf) : module du juge-tournoi, adaptateur Kimi v54, lanceur gelé et lanceur durable neufs ; essais et banc de mutations, dont : `reasoning_effort` absent → refus ; plafonds séparés ; guetteur à deux champs ; garde de T0 sur un cas sain et sur un artefact. Course à blanc complète contre le faux amont de Kimi (`faux_amont_kimi_v3.py`) et un Argon scripté.
4. Contre-lectures (R2) par un lecteur neuf d'un autre modèle.
5. Scellement, GO, appels de contrôle (Kimi depuis la machine louée, Argon) ; course après la fin d'A1-v4 ; sortie scellée ; audit ; verdict par un lecteur neuf (R13).

---

## Annexe A — Arithmétique (aucune donnée de course, aucun appel)

Scripts lancés le 9 novembre 2026 vers 10:12 UTC sous `timeout 120 nice -n 10 python3 -I -B`, dans le bloc-notes de la session (non versés) : `devis_v2_kimi.py` (`e970deaa543fb4cbb39685e952f23f9bde9b8c07ed4d7916ee7407963ba5b315`) et `durees_v2_kimi.py` (`0a437000a5de649add52b20e51ea03ba7cc2e35c13424a9210040c5f50e6c230`). Leur cœur :

```python
KIMI, ARGON = (2.0, 10.0), (10.0, 50.0)            # USD par million de jetons (entrée, sortie)
ARGON_APPEL = (0.0413, 0.0632)                     # attaque, USD par appel
JK = {"central": {"debat": (3000, 3000), "simple": (3000, 1500)}, "haut": {"debat": (6000, 8000), "simple": (6000, 4000)}}
JA = {"central": (3000, 2000), "haut": (6000, 4000)}  # Argon juge, débat
CAL = ("debat", "debat", "simple", "simple", "simple", "simple")  # arrêt au premier match perdu ; promotion = 6 gagnés
# T0 = 24 × 6 débats (étalonnage) + 120 lois × calendrier entier (Kimi) + 120 débats (Argon)
# T1 = tentatives × (Σ p^i des débats × prix débat + Σ p^i des simples × prix simple) ; tentatives = 48 × (1 − (1 − p^6)^16) / p^6
# audits ≤ 24 lois × 3 calendriers entiers ; puissance = P(Binomiale(n, q) ≥ b_min), b_min = plus petit b avec McNemar(b, 0) < 0,05
```

Sorties : celles des tables des § 5.2, 5.4 et 6 (prix par appel : Kimi débat 0,036 / 0,092, simple 0,021 / 0,052 ; Argon juge 0,13 / 0,26).

## Annexe B — Sources lues pour la v2 (empreintes relevées le 9 novembre 2026, 10:05 à 10:15 UTC)

| pièce | chemin | empreinte |
|---|---|---|
| conception v1 (scellée, inchangée) | `docs/notes/ideation-organisme-v1/juge-tournoi-elo-v1/conception-juge-tournoi-elo-v1.md` | `a781eb62216dab6a9f1f8ddde63f42255292ff98921c311b8c2e2ee642ce986f` (égale au compagnon) |
| relais Kimi v4 ; lisez-moi v1 et v4 | `docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py` ; `LISEZMOI-relais-kimi-v1.md` ; `LISEZMOI-relais-kimi-v4.md` | `67f36951…` ; `464f8886…` ; `e5d6c5ce…` (compagnons vérifiés) |
| commandes de Kimi | `…/relais-kimi-v1/commande_kimi_v1.py` ; `…/commande_kimi_recherche_v1.py` | `3a98845e…` ; `ac15ae77…` |
| pages de Moonshot lues le 30 octobre 2026 | `…/doc-moonshot-lue-2026-10-30-v1/pricing_chat.html` ; `…/guide_kimi-k3-1-pro-quickstart.md` | `a26c7080…` ; `3f1860a6…` |
| journaux de relais (sans corps ni clé) | `…/kimi-sources-essaim-v1/relais-journal.jsonl` ; `…/essai-reel-v1/relais-journal.jsonl` | `5859781b…` ; compagnon vérifié |
| adaptateur Kimi du pôle (public, fermeture d'A1-v4) | `orchestrator/pole/adaptateur_kimi_v53.py` (commit `f39a7f4`) | `09a46515…` |
| page publique du résultat d'A1 | `resultats/attaque-goodhart-v2/README.md` | `dc2a3d66…` |
| README de l'organisme (l. 125, 129) | `README.md` du dépôt public | `1105f573…` |
| devis de la boucle réelle (prix d'Argon déduits) | `docs/notes/organisme-boucle-reelle-v1/devis-boucle-reelle-organisme-v1.md` | `60643868…` (égale au compagnon) |
| seconde note d'antériorité | `docs/notes/ideation-organisme-v1/anteriorite-co-scientist-v1/note-anteriorite-popper-evaluator-v1.md` | `d1ab7049…` (égale au compagnon) |
| registres (fichiers vivants) | `registres/depenses.md` l. 253-255, 259, 262, 266, 267, 278, 305-307, 319, 323, 324, 330, 336 ; `registres/decisions.md` l. 1044 (R-816), 1053 (R-825), 1055 (R-827), 1070 (R-841), 1073 (R-844), 1269 (R-1041), 1270 (R-1042), 1272 (R-1044), 1953 à 1955 (R-1995 à R-1997) | non empreintés |

Version 2 ; jamais réécrite (R12). Empreinte à relever et compagnon à écrire par la mère au versement.
