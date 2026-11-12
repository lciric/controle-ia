# Contre-lecture (règle R2) des commandes externes v4 de Kimi et d'Argon — tour fermé, étage 1

Contre-lecteur neuf (Opus 5.5), le 3 novembre 2026, de 01:10 à 01:46 UTC (heures de `date -u`). Je n'ai écrit ni le code, ni
les essais, ni le banc. Rien commis, aucun `git fetch`, aucun `.sha256` créé ni modifié, aucun fichier de l'arbre modifié
(`git status` propre avant et après), rien sous `donnees/`, aucun réseau hors de 127.0.0.1, aucun modèle, aucune instance ;
Python sous `nice -n 10` ; aucun processus laissé (vérifié par `ps`). Mes copies, scripts et sorties sont dans
`/tmp/claude-0/-home-user/70605ed3-c649-5b49-861d-ab74970b173c/scratchpad/contre-lecture-commandes-v4/`.

Objet : `docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1/` de l'arbre `wt-commandes-tf` (branche
`outils/commandes-tour-ferme-v1`, tête `ad8dcaad`), contre le contrat du dépôt public `ideation-organism` à `63ed933` (lecture
seule ; export local par `git archive` pour exécuter l'adaptateur v64 sur de vraies sorties) et l'annexe A du brouillon 6.

## 1. Verdict

**Conformes après corrections précises** — 0 bloquant (B1 corrigé, rejoué à `tour_ferme_v64`), 2 importants hors du code des v4 (limites propres des relais et registre illisible lus « fin des tours » par la v64 sans garde de l'orchestrateur : constat A.6 bis chiffré avant le GO), 7 mineurs.

## 2. Bloquants

Aucun.

## 3. Importants

**I1 — Les limites propres des relais (402 de leur plafond, 429 de leur nombre d'appels) sont lues « budget_depasse » sans
aucune garde de l'orchestrateur ; la v4 rend ce cas silencieux chez Kimi aussi (il arrêtait la course en v3).**

- Fait : Kimi v4 l. 300-304 (402 ou 429 signé par le relais → code 4, `envoye: false`) et Argon v4 l. 457-459 (tout 402 ou 429,
  depuis la v2) ; `adaptateur_commande_v64.py` l. 123-128 → « budget_depasse », coût 0, `rien_envoye` ; `AdaptateurEtageV64`
  (`pole/tour_ferme_v64.py` l. 778-783) n'arrête que si la dépense du relais **vue par l'étage** atteint la part, et cette
  dépense (`self.depense`, l. 753 et 773) ne compte ni le proposeur ni un refus (coût 0) ; l'étage v5 rend « fin des tours »
  (l. 409, 477-479) ou « non concluant » (l. 630-631). Rien dans l'orchestrateur ne connaît `--max-appels` ni `--plafond-usd`
  d'un relais. Rejoué (section 6, [E]) : 429 du relais Argon passé par l'adaptateur de l'étage → « budget_depasse », aucun arrêt.
- Conséquence : toutes les cartes et tous les témoins restants de la génération (trois bras, deux étages chacun) finissent sans
  exécution ; l'arrêt ne vient qu'au proposeur suivant (l. 586-588, bras réel de la génération suivante). **À la génération 3,
  aucun proposeur ne suit : la course finit en code 0 et la lecture gelée lit des cartes vidées** (« non concluant », compté
  par T4). A.6 bis (brouillon 6, l. 857) le dit et demande à session-depot de rendre ces limites inatteignables (plafond ≥ part,
  sans autre usage ; appels ≥ 1 731 pour Kimi, ≥ 147 pour Argon) ; le LISEZMOI v2 (l. 177-179) dit seulement « plafonds propres
  couvrant les parts » : rien sur le nombre d'appels, l'usage exclusif, la réserve minimale ni les prix. Aux défauts, la course
  serait touchée : `--max-appels` vaut 64 par défaut au relais Kimi (`relais_kimi_v3.py` l. 139), quand les 31,7 cartes et
  témoins du devis font ≈ 98 sessions de Kimi à 3 tours par carte et ≈ 383 à 12 (brouillon 6, l. 577), et la ligne d'usage
  d'Argon (v4 l. 123) écrit `--max-appels 50` (< 147 ; ≈ 35 appels au devis, ≈ 58 à 54,9 cartes et témoins testés).
- Deux pièges du relais Kimi pour le plafond : il réserve `max(--reserve-par-appel, pire cas)` (l. 537), défaut 0,40 USD (l. 141) :
  avec `--plafond-usd 44` tout juste, il refuse dès 43,60 USD réglés tout appel dont le pire cas est sous 0,40 USD, quand la garde
  d'étape du registre accepte encore jusqu'à ≈ 43,84 USD (expérimentateur à pire cas 0,16) ; et il compte au prix le plus fort
  les jetons hors de `prompt_tokens` et `completion_tokens` (l. 247-249), que la commande ne compte pas.
- Correction précise (A, sans code, nécessaire dans tous les cas ; recommandée, confiance élevée) : écrire au constat A.6 bis
  (ou au LISEZMOI) et appliquer au lancement — **relais Kimi 8804** : instance neuve pour la course, sans autre usage pendant
  la course, `--max-appels` ≥ 1 731, `--plafond-usd` ≥ 44 + `--reserve-par-appel` (≥ 44,40 au défaut ; une marge d'environ
  1 USD couvre aussi les jetons hors compte), `--prix-entree 2 --prix-sortie 10` et `--prix-cache` ≤ 2 (le barème de la
  commande) ; **relais Argon 8805** (servi depuis la v2) : instance neuve, non partagée avec A1-v3, `--plafond-usd` ≥ 6 (même
  pire cas que la commande), `--max-appels` ≥ 147 ; relever `GET /relais/etat` des deux relais avant le premier appel (appels
  et dépense à zéro, bornes) et le joindre au constat. (B, durcissement facultatif, v5) : refus propres des relais (402, 429) en
  code 3 dans les deux commandes, pour qu'une limite mal réglée arrête au lieu de vider ; coût : une v5, ses essais, une
  contre-lecture courte.

**I2 — Un registre illisible est lu de même « fin des tours », sans garde de l'orchestrateur (probabilité faible).**

- Fait : `RegistreIllisible` ou `OSError` du registre → code 4, `envoye: false`, `cause_refus = registre_illisible` (Kimi l. 266-270,
  Argon l. 425-429) → « budget_depasse » (rejoué, [V]) ; la v64 ne lit jamais le registre (aucune occurrence hors de la
  substitution du chemin, `demonstrations/tour_ferme_v64.py` l. 292). Conséquence identique à I1.
- Probabilité : aucun chemin normal des commandes ne produit une ligne illisible (écritures sous verrou exclusif, appels en
  série, arrêt par l'adaptateur en `SIGKILL`) ; il faut une modification extérieure de `<SORTIE>/registre-depense-cumulee-v1.jsonl`,
  un verrou illisible ou une erreur d'écriture du disque — que les écritures propres de l'étage avant chaque appel
  (`consigne.md` scellée, v5 l. 351) rencontreraient le plus souvent d'abord.
- Correction précise, au choix : (a) v5 : `registre_illisible` en code 3 (arrêt), une ligne par commande et un essai ;
  (b) sans code : l'écrire au constat A.6 bis comme résidu accepté, avec cette raison. Recommandation : (b) pour cette course si
  aucune v5 n'est faite pour I1 (B) ; sinon (a) dans la même v5. Confiance moyenne.

## 4. Mineurs

1. `tour_ferme_v63` reste écrit dans le LISEZMOI v2 (table l. 106-115, phrase l. 171-173) et dans la suite (`ETAPE`, l. 52), quand
   le lanceur v64 passe `tour_ferme_v64` (l. 84). Sans effet sur le code (toute valeur non vide est acceptée ; rejoué à
   `tour_ferme_v64`) ; le constat doit écrire `tour_ferme_v64/kimi` et `tour_ferme_v64/argon`.
2. Le LISEZMOI v2 ne donne pas la clé neuve de la configuration (A.6) : `fournisseurs.kimi.prix_entree_usd_par_million_jetons = 2`
   (`--prix-entree 2`) et `fournisseurs.argon.… = 10` (`PRIX[0]`, Argon l. 158). Absente : refus du lanceur, code 2 (bruyant).
   La vérification préalable v64 compte trois caractères par jeton ; la commande de Kimi compte un jeton par octet (plus 1 024
   et la sortie minimale) : c'est elle qui refuse d'abord, même lecture.
3. `cause_refus` n'est ni lue ni gardée par la v64 (`adaptateur_commande_v64.py` l. 125-128 remplace le motif ; les traces de
   l'étage ne la portent pas) : au relevé scellé, une fin de tours par `plafond_session` ne se distingue pas d'une fin par
   `relais_max_appels` ou `registre_illisible` ; seuls les refus des relais laissent une trace au registre (`fin`, code 4,
   1e-6). À porter à conv-audit (garder la cause au motif) ; rien à changer dans les commandes.
4. Quatre de mes six mutations survivent (section 6) : signature du relais relâchée (X1), signature exacte « relais-kimi-v3 »
   (X2), corps tronqué à 300 octets avant la signature (X3), clé non suffixée pour le seul proposeur (X6). Le code livré est
   juste sur les quatre points (rejoué : refus signé « relais-kimi-v4 » et corps de ≈ 490 octets, forme réelle de
   `relais_kimi_v3.py` l. 544, lus comme refus du relais ; les deux proposeurs sous leur clé suffixée), mais la suite ne les
   tient pas : son corps signé (`REFUS_SIGNE_KIMI`, l. 54) fait 91 octets et ne porte que « relais-kimi-v3 », et aucun essai ne
   joue le proposeur avec `ETAPE_POLE`. Trois cas à ajouter à la prochaine version ; X2 et X3 iraient du côté sûr (code 3, arrêt).
5. Réserve 2 du développeur (Kimi : erreur de l'amont relayée, `envoye: false` et coût plancher alors que l'appel est parti) :
   code 3, donc arrêt ; sans effet sur la lecture v64 ; d'accord pour la remettre.
6. A.6 bis demande qu'aucune commande ne refuse avant dépense une session de l'expérimentateur « à quelques centimes » ; la
   commande de Kimi refuse (code 4, `plafond_session`) une consigne longue en fin de borne (≈ 28 400 caractères à 0,10 USD) :
   c'est la lecture voulue par TF-02 (a) (fin des tours) ; à écrire ainsi au constat plutôt que « aucun refus ».
7. Les chemins absolus du LISEZMOI (`/home/user/controle-ia-travail/docs/notes/…/commandes-tour-ferme-v1/…`) n'existent pas
   encore dans l'arbre principal (branche non versée) : à vérifier chez la fille, empreintes v4 comprises, avant de geler la
   configuration (A.2).

## 5. Table « sortie de la v4 → lecture par la v64 »

Lignes : `adaptateur_commande_v64.py` (AC), `adaptateurs.py` gelé (AD), `pole/tour_ferme_v64.py` (TF), `tests_de_mort_v5.py`
(V5), `demonstrations/tour_ferme_v64.py` (LA). Chaque ligne « rejoué » l'a été par l'adaptateur v64 sur une vraie sortie (section 6).

| sortie de la v4 | lecture v64 | expérimentateur ou vérificateur | proposeur | ce qui empêche une morsure en cours d'étage |
|---|---|---|---|---|
| code 4 `plafond_session` | « budget_depasse », coût 0, rien envoyé (AC l. 123-128) — rejoué | fin des tours de la carte (V5 l. 409, 477-479) ; témoin « non concluant » (V5 l. 630-631) ; aucun arrêt (TF l. 778-783) | arrêt (TF l. 586-588) | sans objet : lecture voulue (TF-02 a), borne par carte |
| code 4 `garde_etape` | idem — rejoué | idem | arrêt | **couverte** : pire cas avant chaque étage (TF l. 862-863 → `Compteur.verifier_parts_avant_etage` l. 279-284 : part restante ≥ cartes × 0,80 ou × 0,1), dépenses du proposeur et de l'étage au compteur (l. 925-927, 886), bornes par carte tenues par l'étage (V5 l. 461-470 ; une session de vérificateur à 0,1 par carte, l. 627) : le registre, neuf et au même compte, ne peut pas passer la part au milieu d'un étage ; résidu : planchers 1e-6 et arrondis à 6 décimales |
| code 4 `garde_cumulee` | idem — rejoué | idem | arrêt | **couverte** : parts de somme = plafond (LA l. 187), plafond de la configuration = plan (l. 289-291), `--plafond-cumule-usd` substitué à 50, registre dans une sortie qui doit être vide (l. 408, l. 292) : bornée par les deux gardes d'étape |
| code 4 `registre_illisible` | idem — rejoué | idem, **silencieux** | arrêt | **aucune** (I2) |
| code 4 `relais_plafond` | idem — rejoué (Argon ; Kimi signé « relais-kimi-v4 ») | idem, **silencieux** | arrêt | **aucune** dans l'orchestrateur ; ne mord pas si I1 (A) est appliqué |
| code 4 `relais_max_appels` | idem — rejoué (Argon ; Kimi signé, corps de 493 octets) | idem, **silencieux** | arrêt | **aucune** (I1) |
| code 2 (dont refus d'argparse, ligne JSON chez les deux) | « erreur », coût 1e-6 compté (AD l. 760) — rejoué | arrêt de l'étage (V5 l. 411-412) | arrêt | — |
| code 3 (relais absent, interface, 400/403/411/413, Kimi 402/429 non signés) | « erreur » — rejoué (relais absent ; 429 de l'amont) | arrêt | arrêt | — |
| code 5, modèle servi différent ou refus dit | « refus » R-764 (AD l. 755-759) — rejoué | arrêt, sortie mise à l'écart | arrêt | — |
| code 5, autre (tronqué, vide, usage absent, dépassement de réserve) | « erreur » | arrêt | arrêt | — |
| code 6 (délai, signal) | « erreur », pire cas compté — rejoué | arrêt | arrêt | — |
| sans dernière ligne, ou délai de l'adaptateur | « erreur », plafond compté (`cout_inconnu`) | arrêt | arrêt | — |
| code 0 | « ok », `modele_servi` recopié (v56) — rejoué | — | — | — |

Aucune sortie en code 4 ne porte `modele_servi` ni `refus` : le contrôle du modèle de la classe gelée ne la change pas en
« refus », et la v64 la lit bien (`envoye` est le booléen faux sur les six causes).

## 6. Ce que j'ai rejoué

Sous `env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp nice -n 10` ; commandes sous `/usr/bin/python3 -I -B` (3.13.18) sauf
la suite à son défaut ; outils sous `/home/user/controle-ia-travail/.venv/bin/python` (3.13.18, pytest 9.1.1).

1. **Diff v3 → v4** (`patch/`) : `patch -o` des copies v3 (`bb303f50…`, `95fa4064…`) avec les deux `.patch` → `cmp` **égal** à
   chaque v4. Diff indépendant du code hors docstring du module (`code_sans_doc.py`, arbre syntaxique) : Kimi — `VERSION`, trois
   constantes, trois fonctions (`etape_du_registre`, `cause_du_registre`, `refus_du_relais`), deux `cause_refus` au plafond de
   session, clé et `diag`, cause d'un refus du registre, corps d'erreur lu en entier et code 4 pour un 402 ou 429 signé ; Argon —
   `VERSION`, trois constantes, deux fonctions, deux causes, clé et `diag`, cause du registre, cause des 402 et 429, refus
   d'argparse ; rien d'autre. 106 et 112 lignes changées (comme le LISEZMOI). Bloc `servir` (marqueur du relais compris, celui
   de la commande exclu) : **8 573 octets, identique en v2 (`221df610…`), v3 et v4** ; zone entre la docstring et le bloc
   identique v3/v4 hors `VERSION` ; dans `principal`, seul change le `try` autour de `parse_args`.
2. **Empreintes** : `EMPREINTES-commandes-tour-ferme-v2.txt` 7 OK, `…-v1.txt` 8 OK, les 22 compagnons `.sha256` du dossier et de
   `contre-lecture-v3/` OK ; registre `8ba92066…` inchangé.
3. **Suite** : `… .venv/bin/python -B -m pytest -q -p no:cacheprovider test_commandes_tour_ferme_v4.py` → **87 passés, 52,25 s**
   (01:21:37 à 01:22:30) ; même commande avec `PY_COMMANDES=/usr/bin/python3` (lu l. 41) → **87 passés, 54,50 s** (01:22:36 à
   01:23:31). Pièces : `pytest-v4-depot.txt`, `pytest-v4-usr-bin.txt`.
4. **Rejeu B1 et lecture v64** (`scripts/rejeu_v4_v1.py`, sortie `rejeu-v4.txt`, 01:30:18 à 01:30:23, **0 échec**) : copies
   hors de l'arbre, deux faux relais en processus (`ThreadingHTTPServer` sur 127.0.0.1, port libre), listes de commandes **lues
   telles quelles dans le LISEZMOI v2** (chemin de la copie, adresse du faux relais, puis la substitution du lanceur :
   `{REGISTRE}` et `--plafond-cumule-usd`), `ETAPE_POLE=tour_ferme_v64`.
   - Témoin v3 (registre R0) : Kimi v3 proposeur règle 5,95 USD (consigne de 2 960 000 caractères) → Argon v3 `lecteur_test`
     à 0,10, part 6.00 : **code 4, « garde d'étape (tour_ferme_v64) : 5.9500 réglés … > plafond dur 6.00 »** : B1 se voit.
   - v4 (R1) : Kimi v4 règle 5,95 USD, clé `tour_ferme_v64/kimi` → Argon v4 `lecteur_test`, part 6.00 : **code 0**, clé
     `tour_ferme_v64/argon`, requête reçue ; deux clés distinctes au registre.
   - v4 (R2) : Argon v4 proposeur règle 5,95 USD (pire cas 5,975 ≤ 6) → Argon `lecteur_test`, part 6.00 : **code 4,
     `cause_refus = garde_etape`**, « garde d'étape (tour_ferme_v64/argon) : 5.9500 réglés … », `envoye: false`, coût 1e-6,
     rien reçu par le relais ; Kimi expérimentateur sous une part de 1.00 : code 0 (la dépense d'Argon n'y entre pas).
   - Idempotence : `ETAPE_POLE=tour_ferme_v64/argon` → même clé (refus `garde_etape`, les 5,95 comptent ; à part 44.00 : code 0),
     jamais `…/argon/argon` ; `tour_ferme_v64/kimi` → inchangée. Garde cumulée commune : Kimi, plafond cumulé 6 → code 4
     `garde_cumulee` (« 5.9512 réglés … ») alors que sa propre clé n'a que 0,0008 USD.
   - Adaptateur v64 (`AdaptateurCommandeExterneV64`, modèle servi exigé, porte « environnement » réelle) sur de vraies sorties :
     les six causes → « budget_depasse », coût 0, `rien_envoye` ; Kimi 429 de l'amont non signé → code 3, « erreur » ; codes 2
     (Kimi et Argon, option inconnue : coût 1e-6, pas `cout_inconnu`), 3 (relais absent), 6 (délai) → « erreur » ; 5 (modèle
     servi différent) → « refus » ; 0 → « ok », modèle servi recopié.
   - Adaptateur de l'étage et compteur : `garde_etape` et 429 du relais rendus à l'étage sans arrêt ; dépense vue par l'étage à la
     part → `ArretTour` ; `Compteur` après 5,95 USD d'Argon → arrêt avant un étage de 4 cartes (0,05 < 0,40) ; à 5,50 → joué.
5. **Mes mutations** (`scripts/mes_mutations_v1.py`, sortie `mes-mutations.txt`, 01:33:05 à 01:37:23 ; copies dans `mut/`,
   motif présent une fois exactement, suite livrée avec `-x`) :

   | id | fichier | mutation | sort |
   |---|---|---|---|
   | X1 | Kimi | signature relâchée : toute chaîne `relais` vaut refus du relais | **SURVIT** (87 passés) |
   | X2 | Kimi | signature exacte « relais-kimi-v3 » | **SURVIT** (87 passés) |
   | X3 | Kimi | corps d'erreur tronqué à 300 octets avant la signature | **SURVIT** (87 passés) |
   | X4 | Argon | `OSError` du registre lue `garde_cumulee` | tuée (`test_registre_illisible_code_4[argon]`) |
   | X5 | Argon | refus d'argparse rendu en code 4 (que la v64 lirait « budget_depasse ») | tuée (`test_arguments_obligatoires_absents_code_2[argon]`) |
   | X6 | Kimi | clé d'étape non suffixée pour le seul proposeur | **SURVIT** (87 passés) |

   Banc livré (64 mutations, ≈ 27 min) **non rejoué**, selon la consigne.
6. **Réserve 1** (`relais_kimi_v3.py` lu par `git show main:…`, `d54ed2bc…` ; `relais_kimi_v4.py`, `67f36951…`) : la marque
   `"relais": VERSION` (« relais-kimi-v3 », « relais-kimi-v4 ») est sur `_refuser` (l. 476-480 : 400, 403, 411, 413), sur les
   refus de `Compteur.admettre` (l. 538-544 : 429 `--max-appels`, 402 plafond ; `compteur.etat()` n'a pas de clé `relais`, la
   marque n'est pas écrasée) et sur ses propres 502 ; une réponse de l'amont non 200 est relayée avec son statut et son corps
   tels quels (l. 566, 599, 616 ; en-tête l. 30-31), sans la marque. **L'interprétation est juste** : seul un refus
   rédigé par le relais n'a rien envoyé ; un 429 ou 402 de Moonshot (compte sans crédit, débit) est parti vers l'amont et doit
   arrêter (code 3), ce qu'il fait (rejoué). Le préfixe « relais-kimi- » couvre les deux versions du relais.

## 7. Non vérifié

- Aucun relais réel (8804, 8805), aucun modèle ; les paramètres de lancement prévus des relais ne m'ont pas été donnés (I1).
- Le lanceur v64 n'a pas été joué de bout en bout avec ces commandes : j'ai exécuté ses pièces (adaptateur v64, porte
  « environnement », adaptateur de l'étage, compteur), pas `jouer_etage_1`. La configuration v3 (aucun fichier fourni) et la
  valeur de `proposeurs[…].modele` n'ont pas été lues : `--modele` est égal aux deux identifiants nommés par la commande.
- Banc de 64 mutations non rejoué ; « 64 sur 64 tuées » est la parole du LISEZMOI.
- Jetons hors `prompt_tokens`/`completion_tokens` chez Moonshot (I1, second piège) : non observés.
- Commandes v4 sous les chemins du LISEZMOI chez la fille : absentes de l'arbre principal aujourd'hui (mineur 7).

## 8. Fichiers lus et empreintes

Dossier contre-lu (`wt-commandes-tf`, `ad8dcaad`) : `commande_kimi_v4.py` `10afdab5…` ; `commande_argon_v56_nuit_v4.py`
`5c6d5149…` ; `test_commandes_tour_ferme_v4.py` `38517a78…` ; `mutations_commandes_tour_ferme_v4.py` `57139250…` (lu, non joué) ;
`diff-kimi-v3-v4.patch` `6e24d4d3…` ; `diff-argon-v3-v4.patch` `13556a91…` ; `LISEZMOI-commandes-tour-ferme-v2.md` `80370160…` ;
`EMPREINTES-commandes-tour-ferme-v2.txt` `dfd10027…` ; `registre_depense_cumulee_v1.py` `8ba92066…` ; `commande_kimi_v3.py`
`bb303f50…` ; `commande_argon_v56_nuit_v3.py` `95fa4064…` ; `contre-lecture-v3/contre-lecture-commandes-tour-ferme-v3-v1.md`
`6b4eac8b…`. Copie v2 d'Argon (bloc `servir`) : `scratchpad/commandes-nuit-v1/commande_argon_v56_nuit_v2.py` `221df610…`.
Dépôt privé (`main`, `fa3b0658`) : `relais_kimi_v3.py` `d54ed2bc…` ; `relais_kimi_v4.py` `67f36951…`.
Contrat (`ideation-organism`, `63ed933`) : `pole/adaptateur_commande_v64.py` `adb73287…` ; `pole/adaptateurs.py` `a1a8ede8…`
(l. 602-775) ; `pole/adaptateurs_v56.py` `d36c79b2…` ; `pole/tour_ferme_v64.py` `35a8294e…` ; `pole/tests_de_mort_v5.py`
`da524871…` ; `demonstrations/tour_ferme_v64.py` `98c1a1a2…` ; `demonstrations/attaque_goodhart_v2.py` `58609e0c…` (l. 233-250) ;
`prereg/preenregistrement-tour-ferme-v1-brouillon6.md` `cdcb4470…` (l. 17, 468, 577-588, 849-857).
Mes pièces (dossier du rapport) : `scripts/rejeu_v4_v1.py` `5b9eff2d…` ; `rejeu-v4.txt` `51f08e64…` ; `scripts/mes_mutations_v1.py`
`382605db…` ; `mes-mutations.txt` `f4ad5d5d…` ; `pytest-v4-depot.txt` `f7b35bfc…` ; `pytest-v4-usr-bin.txt` `2eab9a4d…` ;
`code_sans_doc.py` `c02c8b3e…` ; `bloc_servir.py` `b9be096f…`.
