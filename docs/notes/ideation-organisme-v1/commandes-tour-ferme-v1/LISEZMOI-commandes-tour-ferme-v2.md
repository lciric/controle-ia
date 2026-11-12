# LISEZMOI — commandes externes v4 de Kimi et d'Argon pour le tour fermé, étage 1 (B1, causes de refus)

Rédigé du 2 novembre 2026, 23:53 UTC, au 3 novembre, 01:08 UTC (heures de `date -u`), par un sous-agent
développeur de session-depot. **Rien n'est scellé, rien n'est commis, rien n'a été lancé de payant ; aucun réseau hors de la
boucle locale, aucun modèle, aucune clé, aucun fichier `.sha256` créé.** Arbre `wt-commandes-tf` (branche
`outils/commandes-tour-ferme-v1`, tête `18fdeaae`), dossier `docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1/`.
Fichiers neufs seulement (R12) : les v3, leurs essais, leur banc, leurs diffs, `LISEZMOI-commandes-tour-ferme-v1.md`,
`EMPREINTES-commandes-tour-ferme-v1.txt` et `registre_depense_cumulee_v1.py` sont inchangés
(`sha256sum -c EMPREINTES-commandes-tour-ferme-v1.txt` : 8 OK après le travail).

## But

La contre-lecture neuve des commandes v3 (`contre-lecture-v3/contre-lecture-commandes-tour-ferme-v3-v1.md`, sha256
`6b4eac8b1e367785…`) les juge « conformes après corrections », avec un bloquant : **B1**, la garde d'étape du registre partagé
était jugée sous le seul nom `ETAPE_POLE=tour_ferme_v63`, commun aux deux relais, alors que leurs parts diffèrent (44 USD pour
Kimi, 6 USD pour Argon) ; le vérificateur d'Argon aurait été refusé (code 4, lu « erreur », arrêt de la course) dès ≈ 5,95 USD
dépensés par Kimi dans l'étape (expérience E1). La version 4 corrige B1, ajoute une **cause de refus lisible par programme**
sur toute sortie en code 4 (pour la version 64 de l'étage chez conv-audit, qui lira un code 4 « rien envoyé » comme
« budget_depasse »), aligne Kimi sur Argon pour les refus 402 et 429 du relais (mineur 2) et donne à Argon une dernière ligne
JSON sur un refus d'argparse (mineur 1). Les six essais demandés par l'important I2 sont ajoutés, et les douze mutations de la
contre-lecture sont rejouées contre la nouvelle suite.

## Fichiers neufs du dossier

| fichier | sha256 | rôle |
|---|---|---|
| `commande_kimi_v4.py` | `10afdab57a2aedae…` | commande externe de Kimi (relais local 8804) : v3 + quatre changements |
| `commande_argon_v56_nuit_v4.py` | `5c6d5149586cbb20…` | commande externe d'Argon, sous-commande `appeler` (relais local 8805) : v3 + quatre changements ; `servir` identique |
| `test_commandes_tour_ferme_v4.py` | `38517a78dbbe4306…` | 87 essais `pytest` (la suite v3 transposée, plus B1, I2, argparse, causes), faux relais local, sans clé |
| `mutations_commandes_tour_ferme_v4.py` | `57139250b5b0a444…` | banc de 64 mutations (23 du banc v3 et 12 de la contre-lecture, transposées ; 29 neuves) |
| `diff-kimi-v3-v4.patch` | `6e24d4d39cf301c7…` | `diff -u` v3 → v4 de Kimi (169 lignes, 106 lignes `+`/`−`) |
| `diff-argon-v3-v4.patch` | `13556a91c16c3fba…` | `diff -u` v3 → v4 d'Argon (181 lignes, 112 lignes `+`/`−`) |
| `LISEZMOI-commandes-tour-ferme-v2.md` | (voir les empreintes) | ce fichier |
| `EMPREINTES-commandes-tour-ferme-v2.txt` | — | `sha256sum` de chacun des fichiers neufs ci-dessus (elle-même exclue) |

Le registre partagé reste `registre_depense_cumulee_v1.py`, sha256 `8ba92066b358ffb8…` (identique, contrôlé par un essai). Les
empreintes entières sont dans `EMPREINTES-commandes-tour-ferme-v2.txt` (`sha256sum -c` dans le dossier).

Vérification des diffs (v3 + diff = v4) : copies des v3 dans un dossier vide, `patch -p0 < diff-…-v3-v4.patch`, puis
`cmp` avec les v4 : **égal** pour Kimi et pour Argon ; de même avec `patch FICHIER diff` (cible explicite).

## Différences v3 → v4

Règle R12 : nouvelle version = nouveau nom ; les v3 restent inchangées. Les deux commandes sont fabriquées depuis les v3 par
remplacements exacts (chaque motif trouvé une seule fois). Le détail, numéroté, est en tête de chaque fichier.

**Kimi (`commande_kimi_v4.py`, `VERSION = "commande-kimi-v4"`)**

1. **Clé d'étape propre au fournisseur (B1)** : la clé passée à `reg.reserver` est `ETAPE_POLE` suivie de `/kimi` (fonction
   `etape_du_registre`) ; idempotent : si `ETAPE_POLE` finit déjà par `/kimi`, rien n'est ajouté (forme du lanceur d'A1-v3,
   `etape_du_fournisseur` : `attaque_goodhart_v3/kimi`). Le champ `etape` de la dernière ligne garde la valeur reçue ; le
   champ neuf `etape_registre` porte la clé passée (celle de la ligne `debut` du registre). Garde cumulée inchangée (les deux
   fournisseurs ensemble, même registre, `--plafond-cumule-usd`).
2. **`cause_refus` sur toute sortie en code 4, et sur elle seule** (table plus bas). Garde d'étape et garde cumulée lèvent la
   même exception (`PlafondCumule`) : elles sont distinguées par le **préfixe du message** (`cause_du_registre`). Raison (dite
   en tête du fichier) : le message est rédigé par la décision elle-même, sous le verrou exclusif du registre, alors qu'une
   comparaison refaite par la commande avant `reserver` lirait le registre hors du verrou (l'autre commande peut l'écrire
   entre-temps) ; le registre est gelé (`8ba92066…`, contrôlé par la suite), donc les préfixes « garde d'étape ( » (l. 143) et
   « garde cumulée : » (l. 137) ne bougent pas ; la garde cumulée est jugée la première, elle gagne si les deux refuseraient ;
   les deux contrôles d'entrée de la garde cumulée (« plafond cumulé invalide », « pire cas invalide ») sont `garde_cumulee`.
   Les deux cas sont éprouvés contre le vrai registre (bout en bout et sur chaque message possible).
3. **Refus du relais 402 et 429 en code 4 — changement de comportement** : un 402 (plafond du relais) ou un 429 (nombre
   d'appels du relais) rédigé **par le relais Kimi lui-même** sortait en code 3 ; il sort en code 4, `envoye: false`, coût
   plancher (1e-6), `cause_refus` `relais_plafond` ou `relais_max_appels`. **Interprétation à confirmer (réserve 1)** : le relais
   Kimi signe ses propres refus (corps JSON portant `relais` = `relais-kimi-v3`, `relais_kimi_v3.py`, `_refuser` et refus de
   `Compteur.admettre`) mais transmet tels quels le statut et le corps d'une erreur de l'amont (en-tête l. 30-31) ; un 402 ou
   429 **non signé** (erreur de Moonshot relayée : limite de débit, ou compte sans crédit comme le 2 novembre, HTTP 429,
   addendum 3 à la passation `2026-11-02-2006`) garde le comportement de la v3 (code 3), pour qu'un compte épuisé arrête la
   course au lieu d'être lu « budget_depasse ». Fonction `refus_du_relais`.
4. **Version, en-tête, ligne d'usage.** Rien d'autre ne change (gardes, bornes de sortie par rôle, pire cas, protocole).

**Argon (`commande_argon_v56_nuit_v4.py`, `VERSION = "commande-argon-v56-nuit-v4"`)**

1. **Clé d'étape propre au fournisseur (B1)** : `ETAPE_POLE` suivie de `/argon`, idempotent ; `etape` et `etape_registre`
   comme chez Kimi.
2. **`cause_refus` sur toute sortie en code 4** : même règle et même raison que chez Kimi. Le relais Argon (`servir`) ne
   transmet jamais un statut de l'interface (une erreur de Gemini lui revient en réponse 200 portant `echec`) : tout 402 ou 429
   reçu est un refus du relais lui-même, déjà rendu en code 4 depuis la v2 ; la v4 y ajoute la cause.
3. **Dernière ligne JSON sur un refus d'argparse pour `appeler`** (mineur 1) : code 2, `{"texte": "", "cout_usd": 1e-06,
   "version", "erreur", "envoye": false, "role"}` (`role` = `ROLE_POLE` s'il est donné), comme Kimi ; sans dernière ligne,
   l'adaptateur comptait le plafond de session en `cout_inconnu`. Pour `servir`, le refus d'argparse est relevé tel quel.
4. **Version, en-tête, lignes d'usage.** Rien d'autre ne change.

**Sous-commande `servir` d'Argon : identique à la v3 au comportement près, et octet pour octet hors la constante `VERSION`**
(vérifié par programme à la livraison et par l'essai `test_bloc_servir_identique_a_la_v3`) : le bloc compris entre la
ligne-marqueur du relais (comprise) et celle de la commande (exclue) fait 8 573 octets, identique dans la v2
(`221df610…`), la v3 et la v4 ; entre les imports et ce bloc, la seule ligne qui change est `VERSION` ; les fonctions qu'il
appelle ou lit (`pire_cas`, `maintenant`, `charger_collisionneur`, `statut_et_cout`, `fabriquer_gestion`, `servir`) ont le
même source ; dans `principal`, le sous-analyseur `servir` et son aiguillage sont inchangés, et un refus d'argparse pour
`servir` donne le même code, la même sortie standard (vide) et la même sortie d'erreur que la v3 (essai
`test_servir_refus_d_argparse_inchange_depuis_la_v3`). Le relais 8805 est un instrument gelé d'A1-v3 : il est et restera
servi depuis `commande_argon_v56_nuit_v2.py` ; la v4 ne sert qu'en `appeler`.

## Ce que fait la commande pour chaque rôle (défauts des options ; barème prudent)

Inchangé depuis la v3, sauf la clé d'étape et la cause de refus. Barème prudent : Kimi 2 USD par million de jetons en entrée et
10 en sortie, un jeton d'entrée ≥ un octet du corps JSON (+ 1 024 octets de marge) ; Argon 10 et 50 USD par million, entrée =
caractères / 3 (formule `cout_pire_cas` du collisionneur v7, SUPPOSÉE). `max_tokens` = min(sortie maximale du rôle, ce que le
reste du plafond de session paie après l'entrée) ; sous la sortie minimale : refus sans envoi, code 4, `plafond_session`.
Limites (consigne ASCII) égales au tableau du LISEZMOI v1 et à l'expérience E4 de la contre-lecture
(`contre-lecture-v3/experiences.txt`, sha256 `7ef6eddae54c2254…`) ; recalculées le 3 novembre avec les fonctions des v4,
même méthode (sortie de session-depot, hors dépôt :
`/tmp/claude-0/-home-user/70605ed3-c649-5b49-861d-ab74970b173c/scratchpad/commandes-tf-v4/sorties/limites-v4.txt`, sha256
`7d1f60ac6ea6f2d8…`).

| rôle | `ROLE_POLE` | plafond de session | sortie maximale | sortie minimale | limite de caractères | sortie pleine jusqu'à | clé d'étape au registre (`ETAPE_POLE=tour_ferme_v63`) |
|---|---|---|---|---|---|---|---|
| Kimi proposeur | `proposeur_ideation` | `plafonds_session.proposeur` ≥ 0,50 | 65 536 | 4 096 | 228 402 (à 0,50) | jamais à 0,50 ; `max_tokens` 49 756 pour une consigne courte | `tour_ferme_v63/kimi`, part 44.00 |
| Kimi expérimentateur | `experimentateur_test` | reste de la borne de 0,80 USD de la carte | 16 000 | 4 096 | 378 402 (à 0,80) ; 28 402 (reste 0,10) | 318 882 (à 0,80) | `tour_ferme_v63/kimi`, part 44.00 |
| Kimi lecteur (permis, non joué) | `lecteur_test` | 0,10 | 1 000 | 200 | 47 883 | 43 883 | `tour_ferme_v63/kimi` |
| Kimi juge (permis, non joué) | `juge_ideation` | — | 16 000 | 4 096 | — | — | `tour_ferme_v63/kimi` |
| Argon proposeur | `proposeur_ideation` | `plafonds_session.proposeur` ≥ 0,50 | 32 000 | 1 000 | 135 000 (à 0,50) | jamais à 0,50 ; `max_tokens` 9 993 pour une consigne courte | `tour_ferme_v63/argon`, part 6.00 |
| Argon vérificateur | `lecteur_test` | 0,10 | 1 000 | 200 | **27 000** | 15 000 (à 20 000 caractères : 666 jetons) | `tour_ferme_v63/argon`, part 6.00 |
| Argon expérimentateur (permis, non joué) | `experimentateur_test` | — | 4 000 | 1 000 | 225 000 (à 0,80) | 180 000 | `tour_ferme_v63/argon` |
| Argon juge (permis, non joué) | `juge_ideation` | — | 4 000 | 1 000 | — | — | `tour_ferme_v63/argon` |

Avec la v4, la part de 6 USD d'Argon ne compte que la dépense d'Argon dans l'étape, et celle de 44 USD de Kimi celle de Kimi ;
la garde cumulée (50 USD) compte toujours les deux.

## Causes de refus (code 4 : rien envoyé)

Toute sortie en code 4 porte `envoye: false`, un coût fini strictement positif (le plancher, 1e-6), `version`, `role` et
`cause_refus` ; aucune autre sortie ne porte `cause_refus`. La version 64 de l'étage peut lire « code 4 » comme
« budget_depasse » et `cause_refus` comme la raison.

| `cause_refus` | quand | `erreur` commence par | registre |
|---|---|---|---|
| `plafond_session` | le pire cas de l'appel, à la sortie minimale du rôle, passe `PLAFOND_SESSION_USD` (premier contrôle : `max_tokens` sous la sortie minimale ; second : pire cas recalculé au-dessus du plafond) | « pire cas au-dessus du plafond de session » | rien écrit |
| `garde_etape` | réglé + engagé **du fournisseur dans l'étape** (clé `ETAPE_POLE/<fournisseur>`) + pire cas > `PLAFOND_ETAPE_USD` | « garde d'étape (<clé>) : » | rien écrit |
| `garde_cumulee` | réglé + engagé **des deux fournisseurs** + pire cas > `--plafond-cumule-usd` ; aussi plafond cumulé invalide ou pire cas invalide (contrôles d'entrée de cette garde) | « garde cumulée : », « plafond cumulé invalide », « pire cas invalide » | rien écrit |
| `registre_illisible` | ligne illisible ou non conforme, dossier du registre absent, fichier ou verrou illisible (`RegistreIllisible`, `OSError`) | « registre … », « dossier du registre absent », ou le message système | rien écrit |
| `relais_plafond` | HTTP 402 rédigé par le relais lui-même (son plafond, second barrage) | « HTTP 402 : » | `debut` puis `fin` à 1e-6, code 4 |
| `relais_max_appels` | HTTP 429 rédigé par le relais lui-même (son nombre d'appels) | « HTTP 429 : » | `debut` puis `fin` à 1e-6, code 4 |

Chez Kimi, un 402 ou un 429 sans la signature du relais (erreur de l'amont transmise) reste en code 3, sans `cause_refus`
(réserve 1). Les autres codes sont inchangés : 0 conforme ; 2 réglage, entrée ou option refusés ; 3 relais ou interface ;
5 réponse non conforme (dont modèle servi différent, `modele_servi` rendu) ; 6 délai dépassé ou interruption (coût = pire
cas réservé).

## Commandes exactes pour la configuration v3 du tour fermé

Chemins absolus **chez la fille** ; interpréteur **`/usr/bin/python3`** (mineur 4 de la contre-lecture : stable, hors du dépôt ;
3.13.18 ici ; les deux commandes ne lisent que la bibliothèque standard et passent toute la suite sous lui) ; `-I -B` comme en
production. `{REGISTRE}` et l'argument qui suit `--plafond-cumule-usd` sont substitués par le lanceur (annexe A.6 :
`<SORTIE absolue>/registre-depense-cumulee-v1.jsonl` et `50`). `--modele` doit être égal à `proposeurs[fournisseur].modele`
(sinon `MODELE_DEMANDE_POLE` ≠ `--modele` → code 2 avant tout envoi). Toutes les options sont écrites, même à leur défaut, pour
que l'empreinte de la configuration (A.2) les gèle.

`fournisseurs.kimi.commande` :

```json
["/usr/bin/python3", "-I", "-B",
 "/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1/commande_kimi_v4.py",
 "--url-relais", "http://127.0.0.1:8804", "--modele", "kimi-k3.1-pro",
 "--registre", "{REGISTRE}", "--plafond-cumule-usd", "50",
 "--max-sortie-proposeur", "65536", "--max-sortie-court", "16000", "--sortie-min-jetons", "4096",
 "--max-sortie-lecteur", "1000", "--sortie-min-jetons-lecteur", "200", "--delai-s", "1750"]
```

`fournisseurs.argon.commande` :

```json
["/usr/bin/python3", "-I", "-B",
 "/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1/commande_argon_v56_nuit_v4.py",
 "appeler", "--url-relais", "http://127.0.0.1:8805", "--modele", "gemini-4-argon",
 "--registre", "{REGISTRE}", "--plafond-cumule-usd", "50",
 "--max-sortie-proposeur", "32000", "--max-sortie-court", "4000", "--sortie-min-jetons", "1000",
 "--max-sortie-lecteur", "1000", "--sortie-min-jetons-lecteur", "200", "--delai-s", "1750"]
```

Avec, pour chacun : `"type": "commande_externe"` et `"porte_plafond": {"type": "environnement"}` (la porte passe
`ETAPE_POLE=tour_ferme_v63` et `PLAFOND_ETAPE_USD` = la part, `44.00` ou `6.00` ; la v4 juge la part sous
`tour_ferme_v63/kimi` ou `tour_ferme_v63/argon`, sans rien changer au lanceur gelé). Le manifeste porte l'empreinte de chaque
argument qui est un fichier (`description()` de l'adaptateur) : celle de `/usr/bin/python3` (lien vers
`/usr/bin/python3.13`, sha256 `dc9c6efba6e3583b…` ici) et celle de la commande (`EMPREINTES-commandes-tour-ferme-v2.txt`). Le
registre importé par les deux commandes depuis leur dossier n'est pas un argument : son empreinte (`8ba92066…`) est contrôlée
par la suite d'essais et figure dans `EMPREINTES-commandes-tour-ferme-v1.txt`. Les relais Kimi 8804 et Argon 8805 (ce dernier
servi depuis `commande_argon_v56_nuit_v2.py`) sont lancés par l'opérateur, clé dans leur seul environnement, plafonds propres
couvrant les parts.

## Essais (commandes et comptes exacts)

```
cd /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp nice -n 10 /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider test_commandes_tour_ferme_v4.py
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp PY_COMMANDES=/usr/bin/python3 nice -n 10 /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider test_commandes_tour_ferme_v4.py
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp nice -n 10 /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider test_commandes_tour_ferme_v3.py
```

Résultats du 3 novembre 2026 dans l'arbre de session-depot (même dossier ; Python 3.13.18, pytest 9.1.1) :
**v4, commandes sous l'interpréteur du dépôt : 87 passés, 0 échoué, 53 s** (00:38:11 à 00:39:04 UTC) ; **v4, commandes sous
`/usr/bin/python3 -I -B` : 87 passés, 0 échoué, 55 s** (00:39:04 à 00:39:59) ; **v3 sur les v3, inchangée : 51 passés,
0 échoué, 31 s** (01:07:14 à 01:07:45). Faux relais : `ThreadingHTTPServer(("127.0.0.1", 0))`, une requête par connexion,
connexion fermée après la réponse, lecture bornée à 30 s, relais lent toujours libéré en fin d'essai ; aucune connexion
sortante ; processus lancés par les essais arrêtés par leur PID (`send_signal`, `kill`).

Ce que la suite v4 couvre, pour chacune des deux commandes (paramètre `kimi` / `argon`) sauf mention :

- **tout ce que couvrait la v3**, transposé : rôles permis (code 0, dernière ligne conforme, registre `debut` puis `fin`),
  rôles inconnus, `MODELE_DEMANDE_POLE`, `PLAFOND_SESSION_USD` invalides, porte « environnement » incomplète, consigne vide,
  options obligatoires absentes, adresse hors boucle locale, sorties maximale et minimale par rôle et leurs défauts,
  vérificateur à 0,10 USD (consigne courte, consigne de 60 000 caractères), reste de la borne de l'expérimentateur, registre
  plein, registre illisible, garde d'étape, aucune clé lue ni transmise, source sans lecture de clé, relais `servir` (402, 429,
  411, 413, `/relais/etat`, journal sans texte, refus sans clé et sans collisionneur conforme) ;
- **(a) B1** : deux fournisseurs, même registre, même `ETAPE_POLE`, parts différentes — Kimi règle 5,95 USD **par sa
  commande**, puis le vérificateur d'Argon à `PLAFOND_ETAPE_USD=6.00` est **accepté** (code 0 ; clés `tour_ferme_v63/kimi` et
  `tour_ferme_v63/argon` au registre) ; Argon règle lui-même 5,95 USD, puis son vérificateur est **refusé**, code 4,
  `garde_etape`, et Kimi passe sous une part de 1.00 (la dépense d'Argon ne compte pas chez lui) ; idempotence (`E/argon` →
  `E/argon`, jamais `E/argon/argon`, et c'est la même clé que `E` : la dépense de l'une compte dans la garde de l'autre ; seul
  le suffixe du fournisseur lui-même est reconnu : `E/kimi` → `E/kimi/argon` chez Argon) ; garde cumulée commune : Kimi règle
  49,98 USD → Argon refusé, `garde_cumulee` (et Kimi lui-même au-delà), plafond cumulé relevé → Argon passe ;
- **(b) important I2** : modèle servi différent → code 5, `modele_servi` rendu tel que servi ; `cout_usd` fini > 0 sur chaque
  code 4 (toutes les assertions de code 4 passent par une seule fonction qui le contrôle) ; 402 et 429 du relais → code 4,
  `envoye: false`, coût plancher, `cause_refus`, ligne `fin` au registre (et, chez Kimi, 402 et 429 non signés → code 3 sans
  cause) ; délai dépassé (`--delai-s 1`) → code 6 au pire cas réservé ; SIGTERM et SIGINT pendant l'appel → code 6 au pire cas
  réservé, ligne `fin` au registre ; Argon, réponse à `cout_origine = pire_cas` → coût rendu = pire cas réservé exactement,
  aucun dépassement de réserve (et échec de transport rendu par le relais → code 3 au même coût) ; et, chez Kimi, la barrière du
  modèle servi **du relais** (HTTP 502 « modèle servi différent ») → code 5, `modele_servi` = « ecart-signale-par-le-relais »
  (lu par l'adaptateur comme un refus R-764), coût au pire cas réservé ; un autre 502 → code 5 sans `modele_servi` (bloc des
  erreurs HTTP touché par le point 3 de la v4) ;
- **(c)** option refusée par argparse (option inconnue, valeur illisible, option obligatoire absente ; avec ou sans
  `ROLE_POLE` ; chez Argon aussi sans la sous-commande en tête) → code 2 avec dernière ligne JSON ; `servir` : refus d'argparse
  identique à la v3 ;
- **(d)** `cause_refus` présente et juste pour chacune des six causes (y compris les deux contrôles du plafond de session, le
  plafond cumulé invalide, le dossier du registre absent et un dossier à la place du fichier), sur chaque message que le
  registre gelé peut lever, et absente des codes 0, 2, 3 (403 du relais, relais absent), 5 et 6 ;
- l'identité du bloc `servir` avec la v3, l'empreinte du registre partagé, et les deux commandes sous `/usr/bin/python3 -I -B`.

Non couvert (comme en v3) : le dépassement de réserve (coût lu au-dessus du pire cas réservé → code 5,
`depassement_reserve`), code inchangé depuis la v2 et éprouvé sur la v2 d'Argon, de bout en bout, par
`test_gardes_mini_course_v2.py` (copie de session-depot hors dépôt, sha256 `9f226b41…`) ; un relais réel (8804, 8805) ;
un modèle.

## Banc de mutations

```
cd /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp nice -n 10 /home/user/controle-ia-travail/.venv/bin/python -I -B mutations_commandes_tour_ferme_v4.py
```

Le banc vérifie d'abord que chaque motif est présent une fois exactement (sinon il s'arrête), joue le cas sain (dossier non
muté) qui doit passer (R5), puis, pour chaque mutation, copie le dossier (les deux v4, la v3 d'Argon pour l'essai d'identité,
le registre, la suite), applique la mutation et joue la suite avec `-x`. Résultat du 3 novembre 2026 (00:40:07 à 01:06:44 UTC) :
**motifs vérifiés ; cas sain passé (87 essais, 53 s) ; 64 mutations tuées sur 64 jouées ; code 0**, 26 min 37 s en tout.
Un premier passage, lancé avant l'ajout de l'essai du 502 du relais Kimi (62 mutations contre la suite de 86 essais,
00:31:37 à 00:36:37 UTC), a été arrêté par son PID (R10) après 16 mutations, toutes tuées : seul le passage complet
ci-dessous fait foi.

| id | fichier | mutation | sort | suite | durée |
|---|---|---|---|---|---|
| K1 | `commande_kimi_v4.py` | rôle lecteur_test retiré de ROLES | tuée | 1 failed, 3 passed in 2.47s | 2.7 s |
| K2 | `commande_kimi_v4.py` | sortie minimale du lecteur ignorée (minimum général à sa place) | tuée | 1 failed, 3 passed in 2.46s | 2.7 s |
| K3 | `commande_kimi_v4.py` | sortie maximale du lecteur ignorée (sortie courte à sa place) | tuée | 1 failed, 33 passed in 19.29s | 19.6 s |
| K4 | `commande_kimi_v4.py` | champ envoye perdu sur le refus du plafond de session | tuée | 1 failed, 40 passed in 23.60s | 23.9 s |
| K5 | `commande_kimi_v4.py` | sortie minimale non appliquée (envoi sous le minimum) | tuée | 1 failed, 40 passed in 24.13s | 24.4 s |
| K6 | `commande_kimi_v4.py` | plafond de session absent toléré (défaut 1e9 à la place de nan) | tuée | 1 failed, 12 passed in 8.26s | 8.6 s |
| K7 | `commande_kimi_v4.py` | version v3 rendue | tuée | 1 failed in 0.75s | 1.1 s |
| K8 | `commande_kimi_v4.py` | contrôle de MODELE_DEMANDE_POLE retiré | tuée | 1 failed, 10 passed in 6.54s | 6.8 s |
| K9 | `commande_kimi_v4.py` | champ role absent de la ligne de refus (code 2) | tuée | 1 failed, 8 passed in 5.39s | 5.7 s |
| K10 | `commande_kimi_v4.py` | porte « environnement » incomplète tolérée (ETAPE_POLE seul) | tuée | 1 failed, 14 passed in 9.75s | 10.1 s |
| K11 | `commande_kimi_v4.py` | plafond cumulé du registre remplacé par 1e9 | tuée | 1 failed, 50 passed in 29.65s | 29.9 s |
| A1 | `commande_argon_v56_nuit_v4.py` | rôle experimentateur_test retiré de ROLES | tuée | 1 failed, 6 passed in 4.22s | 4.5 s |
| A2 | `commande_argon_v56_nuit_v4.py` | sortie minimale du lecteur ignorée (minimum général à sa place) | tuée | 1 failed, 37 passed in 21.56s | 21.8 s |
| A3 | `commande_argon_v56_nuit_v4.py` | sortie maximale du lecteur ignorée (sortie courte à sa place) | tuée | 1 failed, 37 passed in 22.25s | 22.6 s |
| A4 | `commande_argon_v56_nuit_v4.py` | champ envoye perdu sur le refus du plafond de session | tuée | 1 failed, 41 passed in 25.15s | 25.4 s |
| A5 | `commande_argon_v56_nuit_v4.py` | sortie minimale non appliquée (envoi sous le minimum) | tuée | 1 failed, 41 passed in 24.55s | 24.8 s |
| A6 | `commande_argon_v56_nuit_v4.py` | plafond de session absent toléré (défaut 1e9 à la place de nan) | tuée | 1 failed, 13 passed in 8.27s | 8.5 s |
| A7 | `commande_argon_v56_nuit_v4.py` | version v3 rendue | tuée | 1 failed, 4 passed in 3.10s | 3.4 s |
| A8 | `commande_argon_v56_nuit_v4.py` | contrôle de MODELE_DEMANDE_POLE retiré | tuée | 1 failed, 11 passed in 7.68s | 8.0 s |
| A9 | `commande_argon_v56_nuit_v4.py` | champ role absent de la ligne de refus (code 2) | tuée | 1 failed, 9 passed in 5.83s | 6.1 s |
| A10 | `commande_argon_v56_nuit_v4.py` | porte « environnement » incomplète tolérée (ETAPE_POLE seul) | tuée | 1 failed, 15 passed in 10.62s | 11.0 s |
| A11 | `commande_argon_v56_nuit_v4.py` | plafond cumulé du registre remplacé par 1e9 | tuée | 1 failed, 51 passed in 30.35s | 30.6 s |
| A12 | `commande_argon_v56_nuit_v4.py` | le relais (servir) tolère un corps sans Content-Length (411 perdu) | tuée | 1 failed, 84 passed in 52.86s | 53.2 s |
| C1 | `commande_kimi_v4.py` | lecteur_test prend les bornes du proposeur | tuée | 1 failed, 33 passed in 19.92s | 20.2 s |
| C2 | `commande_argon_v56_nuit_v4.py` | lecteur_test prend les bornes du proposeur | tuée | 1 failed, 37 passed in 21.55s | 21.8 s |
| C3 | `commande_kimi_v4.py` | cout_usd = 0 sur code 4 | tuée | 1 failed, 40 passed in 23.51s | 23.8 s |
| C4 | `commande_argon_v56_nuit_v4.py` | cout_usd = 0 sur code 4 | tuée | 1 failed, 41 passed in 24.99s | 25.3 s |
| C5 | `commande_argon_v56_nuit_v4.py` | envoye vrai sur un refus 402/429 du relais | tuée | 1 failed, 65 passed in 39.40s | 39.7 s |
| C6 | `commande_kimi_v4.py` | envoye vrai sur un refus 402/429 du relais | tuée | 1 failed, 63 passed in 37.65s | 38.0 s |
| C7 | `commande_kimi_v4.py` | délai dépassé rendu en code 3 au lieu de 6 | tuée | 1 failed, 73 passed in 44.85s | 45.2 s |
| C8 | `commande_kimi_v4.py` | gestionnaires de signaux retirés | tuée | 1 failed, 75 passed in 48.01s | 48.3 s |
| C9 | `commande_kimi_v4.py` | contrôle du modèle servi retiré | tuée | 1 failed, 70 passed in 43.55s | 43.8 s |
| C10 | `commande_argon_v56_nuit_v4.py` | contrôle du modèle servi retiré | tuée | 1 failed, 71 passed in 43.74s | 44.1 s |
| C11 | `commande_argon_v56_nuit_v4.py` | coût d'un échec pris au chiffre du relais, pas au pire cas réservé | tuée | 1 failed, 72 passed in 44.80s | 45.1 s |
| C12 | `commande_kimi_v4.py` | garde d'étape du registre débranchée (plafond_etape_usd=None) | tuée | 1 failed, 14 passed in 10.00s | 10.3 s |
| N1 | `commande_kimi_v4.py` | suffixe d'étape retiré à l'appel du registre (clé = ETAPE_POLE) | tuée | 1 failed, 14 passed in 9.54s | 9.9 s |
| N2 | `commande_argon_v56_nuit_v4.py` | suffixe d'étape retiré à l'appel du registre (clé = ETAPE_POLE) | tuée | 1 failed, 15 passed in 10.83s | 11.1 s |
| N3 | `commande_kimi_v4.py` | suffixe d'étape retiré partout (etape_du_registre rend ETAPE_POLE) | tuée | 1 failed, 14 passed in 10.02s | 10.3 s |
| N4 | `commande_argon_v56_nuit_v4.py` | suffixe d'étape retiré partout (etape_du_registre rend ETAPE_POLE) | tuée | 1 failed, 15 passed in 10.80s | 11.1 s |
| N5 | `commande_kimi_v4.py` | suffixe d'étape doublé (idempotence perdue) | tuée | 1 failed, 60 passed in 36.06s | 36.3 s |
| N6 | `commande_argon_v56_nuit_v4.py` | suffixe d'étape doublé (idempotence perdue) | tuée | 1 failed, 61 passed in 36.62s | 36.9 s |
| N7 | `commande_kimi_v4.py` | champ etape de la dernière ligne = clé du registre (valeur reçue perdue) | tuée | 1 failed, 14 passed in 10.01s | 10.3 s |
| N8 | `commande_argon_v56_nuit_v4.py` | champ etape_registre absent de la dernière ligne | tuée | 1 failed, 4 passed in 3.11s | 3.4 s |
| N9 | `commande_kimi_v4.py` | cause : préfixe de la garde d'étape faux (garde d'étape lue garde cumulée) | tuée | 1 failed, 54 passed in 32.01s | 32.4 s |
| N10 | `commande_argon_v56_nuit_v4.py` | cause : garde d'étape et garde cumulée permutées | tuée | 1 failed, 51 passed in 30.70s | 31.0 s |
| N11 | `commande_kimi_v4.py` | cause absente sur le premier contrôle du plafond de session | tuée | 1 failed, 40 passed in 23.57s | 23.9 s |
| N12 | `commande_argon_v56_nuit_v4.py` | cause absente sur le second contrôle du plafond de session | tuée | 1 failed, 47 passed in 27.75s | 28.1 s |
| N13 | `commande_kimi_v4.py` | cause absente sur un refus du registre | tuée | 1 failed, 50 passed in 29.32s | 29.6 s |
| N14 | `commande_argon_v56_nuit_v4.py` | cause : registre illisible lu garde cumulée | tuée | 1 failed, 53 passed in 31.96s | 32.3 s |
| N15 | `commande_kimi_v4.py` | refus 402/429 du relais rendu en code 3 (comportement v3) | tuée | 1 failed, 63 passed in 38.01s | 38.3 s |
| N16 | `commande_kimi_v4.py` | signature du relais ignorée (erreur de l'amont 402/429 rendue en code 4) | tuée | 1 failed, 63 passed in 38.06s | 38.3 s |
| N17 | `commande_argon_v56_nuit_v4.py` | causes 402 et 429 permutées | tuée | 1 failed, 56 passed in 33.35s | 33.6 s |
| N18 | `commande_kimi_v4.py` | causes 402 et 429 permutées | tuée | 1 failed, 56 passed in 33.01s | 33.4 s |
| N19 | `commande_argon_v56_nuit_v4.py` | cause_refus hors du code 4 (sur tout refus HTTP du relais) | tuée | 1 failed, 68 passed in 41.54s | 41.8 s |
| N20 | `commande_argon_v56_nuit_v4.py` | dernière ligne JSON d'argparse retirée (comportement v3) | tuée | 1 failed, 19 passed in 12.38s | 12.7 s |
| N21 | `commande_argon_v56_nuit_v4.py` | dernière ligne JSON d'argparse aussi pour servir (servir changé) | tuée | 1 failed, 27 passed in 15.68s | 16.0 s |
| N22 | `commande_argon_v56_nuit_v4.py` | champ role absent de la ligne d'argparse | tuée | 1 failed, 19 passed in 12.36s | 12.7 s |
| N23 | `commande_argon_v56_nuit_v4.py` | délai dépassé rendu en code 3 au lieu de 6 | tuée | 1 failed, 74 passed in 46.75s | 47.0 s |
| N24 | `commande_argon_v56_nuit_v4.py` | gestionnaires de signaux retirés | tuée | 1 failed, 77 passed in 47.53s | 47.8 s |
| N25 | `commande_kimi_v4.py` | cause fausse sur le second contrôle du plafond de session | tuée | 1 failed, 46 passed in 27.71s | 28.0 s |
| N26 | `commande_argon_v56_nuit_v4.py` | clé d'étape au nom de l'autre fournisseur | tuée | 1 failed, 15 passed in 10.88s | 11.1 s |
| N27 | `commande_kimi_v4.py` | cause : refus du registre toujours garde d'étape | tuée | 1 failed, 50 passed in 30.63s | 31.0 s |
| N28 | `commande_kimi_v4.py` | écart de modèle signalé par le relais (502) perdu : modele_servi non rendu | tuée | 1 failed, 69 passed in 41.72s | 42.0 s |
| N29 | `commande_kimi_v4.py` | 502 du relais rendu en code 3 au lieu de 5 | tuée | 1 failed, 69 passed in 41.93s | 42.2 s |

## Réserves

1. **Point 4 de la commande (Kimi 402 et 429 en code 4) : interprété comme « refus rédigé par le relais lui-même »**, reconnu à
   sa signature (`relais` = `relais-kimi-…` dans le corps JSON). Raison : `relais_kimi_v3.py` (et `relais_kimi_v4.py`)
   transmet tels quels le statut et le corps d'une erreur de l'amont ; or Moonshot répond **429** pour un compte sans crédit
   (2 novembre, collisionneur v9 arrêté). Appliqué à la lettre (tout 402 ou 429 en code 4), un compte épuisé deviendrait un
   code 4 « rien envoyé » lu « budget_depasse » par la version 64 de l'étage : fin des tours de chaque carte au lieu de l'arrêt
   de la course, et une cause `relais_max_appels` fausse. À confirmer par session-depot ; la lecture littérale tient en une
   ligne (c'est la mutation N16 du banc, tuée par l'essai qui joue un 429 non signé). Le relais Argon ne transmet jamais un
   statut de l'interface : la question ne se pose pas chez lui.
2. **Chez Kimi, une erreur de l'amont transmise par le relais (400, 402, 403, 411, 413, 429 non signés) garde `envoye: false`
   et le coût plancher de la v3**, alors que l'appel est parti vers Moonshot et que le relais, lui, la compte au pire cas
   (usage absent). Hors du périmètre de la v4 (comportement v3 inchangé, code 3, donc arrêt de la course) ; à corriger dans une
   version suivante si l'on veut un `envoye` exact.
3. **TF-02 et I1 restent à conv-audit** : la v4 ne change ni l'adaptateur ni l'étage ; c'est la version 64 de l'étage qui lira
   « code 4 » comme « budget_depasse ». La garde d'entrée de l'étage reste inactive en v63 (`prix_caractere_usd` absent) et les
   tailles de consigne de l'expérimentateur et du vérificateur restent à mesurer sur les premières fiches (limites ci-dessus).
4. **Contre-lecture neuve (R2) de la v4 à faire** avant d'écrire la configuration v3 (A.2 gèle les chemins des commandes) :
   je n'ai pas écrit de contre-lecture, et ce LISEZMOI n'en tient pas lieu.
5. Mineurs 3, 5, 6 et 7 de la contre-lecture, non corrigés (hors périmètre) : en-tête périmé du registre (fichier gelé à
   dessein) ; `COLLISIONNEUR_DEFAUT` d'Argon relatif au dossier (`servir` d'ici exigerait `--collisionneur`) ; chez Kimi, un
   délai de **connexion** sortirait en code 3 au pire cas, non 6 ; `"max_tokens": n or maxi` avec une sortie minimale nulle.
6. L'empreinte de `/usr/bin/python3` entre au manifeste (argument fichier) : elle suit le lien `/etc/alternatives/python3` ;
   une mise à jour de l'interpréteur de la machine la changerait (la contre-lecture le jugeait le choix le plus stable).
7. Rien n'est commis ni scellé ; aucun `.sha256` créé ; le scellement du dossier revient à session-depot.
