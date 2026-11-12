# LISEZMOI — commandes externes v3 de Kimi et d'Argon pour le tour fermé, étage 1 (TF-01)

Rédigé le 2 novembre 2026, de 23:00 à 23:26 UTC (heures de `date -u`), par un sous-agent développeur de session-depot.
**Rien n'est scellé, rien n'est commis, rien n'a été lancé de payant ; aucun appel réseau, aucun modèle, aucune clé.**
Dépôt privé `lciric/controle-ia-travail`, branche `outils/commandes-tour-ferme-v1`, dossier neuf
`docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1/` ; aucun fichier existant du dépôt modifié.

## But

Le tour fermé, étage 1 (organisme d'idéation, dépôt public `ideation-organism`, commit `53aef4a` : lanceur
`orchestrator/demonstrations/tour_ferme_v63.py`, cœur `orchestrator/pole/tour_ferme_v63.py`) appelle Kimi et Argon par des
**commandes externes** (`AdaptateurCommandeExterne`, `orchestrator/pole/adaptateurs.py`). Outre le rôle `proposeur_ideation`,
Kimi joue l'**expérimentateur** de l'étage de tests de mort (`ROLE_POLE=experimentateur_test`) et Argon le **vérificateur**
(`ROLE_POLE=lecteur_test`, témoin jamais décisif ; `pole/adaptateurs.py:25`, `ROLES_ETAGE_TESTS` ;
`pole/tests_de_mort_v5.py`, `ROLE_EXPERIMENTATEUR`, `ROLE_LECTEUR`). **Défaut TF-01 (bloquant)** : les commandes de la
version 2 (`commande_kimi_v2.py`, sha256 `644dbb39…` ; `commande_argon_v56_nuit_v2.py`, `221df610…`) portaient
`ROLES = ("proposeur_ideation", "juge_ideation")` et sortaient en code 2 pour ces deux rôles ; la garde des rôles du lanceur
(`exiger_roles_joues`) ne voit que les rôles de l'adaptateur, pas ceux de la commande : le premier appel de l'étage aurait
arrêté la course. La version 3 corrige cela, et seulement cela.

## Fichiers du dossier

| fichier | rôle |
|---|---|
| `commande_kimi_v3.py` | commande externe de Kimi (relais local 8804), v2 + quatre changements |
| `commande_argon_v56_nuit_v3.py` | commande externe d'Argon : sous-commande `appeler` (relais local 8805), v2 + quatre changements ; sous-commande `servir` **inchangée** |
| `registre_depense_cumulee_v1.py` | copie à l'identique du registre partagé (sha256 `8ba92066…`, même empreinte) : les commandes l'importent depuis leur propre dossier (`-I` n'ajoute pas le dossier du script) |
| `test_commandes_tour_ferme_v3.py` | 51 essais `pytest`, sans réseau (faux relais local en processus, port éphémère), sans clé |
| `mutations_commandes_tour_ferme_v3.py` | banc de 23 mutations ciblées, chacune tuée par la suite |
| `diff-kimi-v2-v3.patch`, `diff-argon-v2-v3.patch` | `diff -u` v2 → v3 (les v2 ne sont pas dans l'arbre du dépôt : copies de session-depot, empreintes ci-dessus) |
| `EMPREINTES-commandes-tour-ferme-v1.txt` | `sha256sum` de chaque fichier du dossier (elle-même exclue) |

## Différences v2 → v3 (les mêmes pour les deux commandes ; `diff -u` joint)

Règle R12 : nouvelle version = nouveau nom ; les v2 restent inchangées.

1. **Rôles** : `ROLES = ("proposeur_ideation", "juge_ideation", "experimentateur_test", "lecteur_test")`.
2. **Sortie maximale et minimale par rôle**, fonction neuve `bornes_de_sortie(role, args)` : `proposeur_ideation` →
   `--max-sortie-proposeur` / `--sortie-min-jetons` ; tout autre rôle (`juge_ideation`, `experimentateur_test`) →
   `--max-sortie-court` / `--sortie-min-jetons` ; `lecteur_test` → options neuves `--max-sortie-lecteur` (défaut 1 000) et
   `--sortie-min-jetons-lecteur` (défaut 200 : le vérificateur rend une seule ligne `VERDICT: … ; chiffre: … ; ligne: …`,
   sous un plafond de session de 0,10 USD). Dans la v2, `max_tokens_permis` (Kimi) et le test `mt < args.sortie_min_jetons`
   (Argon) lisaient le minimum général ; en v3 ils lisent `mini`, rendu par `bornes_de_sortie`.
3. **Dernière ligne** : le champ `role` est rendu sur toute sortie (il l'était déjà après la réservation du registre ; il
   l'est maintenant aussi sur un refus de réglage, code 2, où il vaut ce que portait `ROLE_POLE`, et sur un refus de plafond de
   session, code 4) ; le champ `version` vaut `commande-kimi-v3` / `commande-argon-v56-nuit-v3` ; le champ `envoye` est
   conservé tel quel (`false` quand rien n'est parti).
4. **En-tête** (différences numérotées, historique de la v2 gardé en dessous) et lignes d'usage.

Rien d'autre ne change : mêmes gardes (plafond de session au pire cas, porte « environnement » `ETAPE_POLE` +
`PLAFOND_ETAPE_USD`, garde cumulée et garde d'étape du registre, écart de modèle servi, codes de sortie 0, 2, 3, 4, 5, 6),
même registre, même protocole vers les relais locaux (`/v1/chat/completions` sur 8804, `/appel` sur 8805), jamais de
mandataire, aucune clé lue.

Diff Kimi : 111 lignes de `diff -u`, 50 lignes `+`/`−` ; diff Argon : 112 lignes, 60 lignes `+`/`−` (en-têtes compris).

**Sous-commande `servir` d'Argon (le relais 8805) : inchangée.** La section du fichier entre `# --- relais (sous-commande
`servir`)` et `# --- commande (sous-commande `appeler`)` (8 536 octets) est **identique octet pour octet** à celle de la v2
(vérifié par programme à la livraison), et les constantes qu'elle lit (`HOTE`, `COLLISIONNEUR_DEFAUT`, `SHA_COLLISIONNEUR`,
`PRIX`, `MAX_OCTETS_CORPS`, `pire_cas`, `maintenant`) sont inchangées : aucune reprise ajoutée (`attentes=(0,)`), mêmes codes
402 (plafond du relais), 429 (nombre d'appels), 413 (corps trop grand), 411 (`Content-Length` exigé), 403, 400, mêmes
journaux, même empreinte exigée du collisionneur. Le relais est un **instrument gelé d'une autre expérience (A1-v3)** : il
continue d'être servi depuis le fichier qui le sert aujourd'hui, pas depuis ce dossier. Seule la constante `VERSION`, partagée
par les deux sous-commandes, change de nom (visible dans le champ `version` de `GET /relais/etat` et l'en-tête `Server` si l'on
servait depuis ce fichier). Remarque : `COLLISIONNEUR_DEFAUT` est calculé trois dossiers au-dessus du fichier
(`…/espece-seule-v1/collisionneur_v7.py`) ; depuis ce dossier il ne pointe sur rien, donc `servir` depuis ce fichier exigerait
`--collisionneur` explicite (laissé tel quel : hors du périmètre de la v3).

## Ce que la commande fait pour chaque rôle (défauts des options ; barème prudent)

Barème prudent : Kimi 2 USD par million de jetons en entrée et 10 en sortie, un jeton d'entrée ≥ un octet du corps JSON
(+ 1 024 octets de marge), donc une consigne ASCII de N caractères compte ≈ N + 1 119 octets ; Argon 10 et 50 USD par million,
entrée = caractères / 3 (formule `cout_pire_cas` du collisionneur v7, SUPPOSÉE). `max_tokens` = min(sortie maximale du rôle,
ce que le reste du plafond de session paie après l'entrée) ; sous la sortie minimale, **refus sans envoi, code 4**. La
« limite de caractères » est la taille de consigne ASCII au-delà de laquelle la commande refuse (sortie à son minimum) ; la
« sortie pleine jusqu'à » est la taille jusqu'à laquelle `max_tokens` vaut la sortie maximale entière.

| rôle | `ROLE_POLE` | plafond de session (`PLAFOND_SESSION_USD`, annexe A) | sortie maximale (jetons) | sortie minimale | limite de caractères | sortie pleine jusqu'à |
|---|---|---|---|---|---|---|
| Kimi proposeur | `proposeur_ideation` | `plafonds_session.proposeur` ≥ 0,50 (A.5) | 65 536 (`--max-sortie-proposeur`) | 4 096 (`--sortie-min-jetons`) | 228 402 (à 0,50) | jamais à 0,50 : 65 536 jetons coûtent 0,655 USD ; `max_tokens` ≈ 49 800 pour une consigne courte |
| Kimi expérimentateur | `experimentateur_test` | reste de la borne de 0,80 USD de la carte | 16 000 (`--max-sortie-court`) | 4 096 | 378 402 (à 0,80) ; 28 402 (reste 0,10) | 318 882 (à 0,80) |
| Kimi lecteur (permis, non joué par l'étage) | `lecteur_test` | 0,10 | 1 000 (`--max-sortie-lecteur`) | 200 (`--sortie-min-jetons-lecteur`) | 47 883 | 43 883 |
| Kimi juge (permis, non joué par le tour fermé) | `juge_ideation` | — | 16 000 | 4 096 | — | — |
| Argon proposeur | `proposeur_ideation` | `plafonds_session.proposeur` ≥ 0,50 | 32 000 (`--max-sortie-proposeur`) | 1 000 (`--sortie-min-jetons`) | 135 000 (à 0,50) | jamais à 0,50 : 32 000 jetons coûtent 1,60 USD ; `max_tokens` ≈ 9 990 pour une consigne courte |
| Argon vérificateur | `lecteur_test` | 0,10 (`BUDGET_LECTEUR_USD_DEFAUT`) | 1 000 (`--max-sortie-lecteur`) | 200 (`--sortie-min-jetons-lecteur`) | **27 000** | 15 000 (à 20 000 caractères : 666 jetons, assez pour une ligne) |
| Argon expérimentateur (permis, non joué) | `experimentateur_test` | — | 4 000 (`--max-sortie-court`) | 1 000 | 225 000 (à 0,80) | 180 000 |
| Argon juge (permis, non joué) | `juge_ideation` | — | 4 000 | 1 000 | — | — |

Taille attendue de la consigne du vérificateur (`consigne_lecteur`, v5) : préenregistrement court + vue des exécutions (au
plus 3 exécutions × (3 000 caractères de queue de sortie standard + 1 500 de début de sortie d'erreur + métadonnées), soit
≈ 15 000 à 20 000 caractères au plus) + texte fixe ≈ 1 500 : sous la limite de 27 000, à vérifier sur les premières fiches
(réserve 3 ci-dessous).

Dans tous les cas, l'expérimentateur de Kimi reçoit la consigne entière sans troncature ; c'est le plafond de session (reste de
la borne) qui borne `max_tokens`, jamais la consigne.

## Commandes exactes pour la configuration v3 du tour fermé

Chemins absolus **chez la fille** (`/home/user/controle-ia-travail/…`) ; interpréteur du dépôt, `-I -B` comme en production ;
`{REGISTRE}` et l'argument qui suit `--plafond-cumule-usd` sont substitués par le lanceur (annexe A.6 :
`<SORTIE>/registre-depense-cumulee-v1.jsonl` et `50`). `--modele` doit être égal à `proposeurs[fournisseur].modele`
(sinon `MODELE_DEMANDE_POLE` ≠ `--modele` → code 2 avant tout envoi). Les options sont toutes écrites, même à leur défaut,
pour que l'empreinte de la configuration (A.2) les gèle.

`fournisseurs.kimi.commande` :

```json
["/home/user/controle-ia-travail/.venv/bin/python", "-I", "-B",
 "/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1/commande_kimi_v3.py",
 "--url-relais", "http://127.0.0.1:8804", "--modele", "kimi-k3.1-pro",
 "--registre", "{REGISTRE}", "--plafond-cumule-usd", "50",
 "--max-sortie-proposeur", "65536", "--max-sortie-court", "16000", "--sortie-min-jetons", "4096",
 "--max-sortie-lecteur", "1000", "--sortie-min-jetons-lecteur", "200", "--delai-s", "1750"]
```

`fournisseurs.argon.commande` :

```json
["/home/user/controle-ia-travail/.venv/bin/python", "-I", "-B",
 "/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1/commande_argon_v56_nuit_v3.py",
 "appeler", "--url-relais", "http://127.0.0.1:8805", "--modele", "gemini-4-argon",
 "--registre", "{REGISTRE}", "--plafond-cumule-usd", "50",
 "--max-sortie-proposeur", "32000", "--max-sortie-court", "4000", "--sortie-min-jetons", "1000",
 "--max-sortie-lecteur", "1000", "--sortie-min-jetons-lecteur", "200", "--delai-s", "1750"]
```

Avec, pour chacun : `"type": "commande_externe"`, `"porte_plafond": {"type": "environnement"}` (les commandes lisent
`ETAPE_POLE=tour_ferme_v63` et `PLAFOND_ETAPE_USD` = la part du relais, `44.00` ou `6.00`, et appliquent la garde d'étape du
registre), et `exiger_modele_servi` tel que le lanceur l'exige. Le manifeste de la course porte l'empreinte de chaque
argument qui est un fichier (`description()` de l'adaptateur) : celles de `EMPREINTES-commandes-tour-ferme-v1.txt`.
Le relais Kimi 8804 (`relais_kimi_v3.py`) et le relais Argon 8805 (`servir`, servi depuis son fichier actuel) sont lancés par
l'opérateur, avec leur clé dans leur seul environnement, avant la course ; leurs plafonds propres (second barrage) doivent
couvrir les parts (44 et 6 USD).

## Essais rejoués (commande et comptes exacts)

```
cd /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp nice -n 10 /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider test_commandes_tour_ferme_v3.py
```

Résultat du 2 novembre 2026, 23:08 UTC (arbre de travail de session-depot, même dossier) : **51 passés, 0 échoué, 30 s**
(Python 3.13.18, pytest 9.1.1, bibliothèque standard seulement). Ce que couvrent les essais, pour chacune des deux commandes
(paramètre `kimi` / `argon`) :

- chaque rôle permis accepté (4 rôles × 2) : code 0, dernière ligne conforme à `lire_derniere_ligne` et `controle_modele`
  de l'adaptateur (`texte`, `cout_usd` réel > 0, `modele_servi` = modèle demandé), champs `role`, `version`, `envoye: true`,
  `max_tokens` égal à celui reçu par le faux relais, registre `debut` puis `fin` (code 0, statut `ok`, même coût) ;
- rôle inconnu (`juge`, `verificateur`, `experimentateur`, vide, `lecteur`, absent) → code 2, `envoye: false`, rien reçu
  par le relais, aucun registre écrit ;
- `MODELE_DEMANDE_POLE` différent → code 2 (variable absente : permis, cas sain) ;
- `PLAFOND_SESSION_USD` absent, vide, non numérique, nul, négatif, `nan`, `inf` → code 2 ;
- `ETAPE_POLE` sans `PLAFOND_ETAPE_USD` (et l'inverse, et un plafond illisible) → code 2 ; les deux présents → code 0 et
  `etape` au registre ;
- consigne vide → code 2 ; `--url-relais` hors boucle locale → code 2 ; `--registre` ou `--plafond-cumule-usd` absent →
  code 2 (argparse, `required`) ;
- sortie maximale choisie selon le rôle (options explicites 3 000 / 2 000 / 500, plafond large) : `max_tokens` reçu par le
  faux relais ; défauts de l'annexe (16 000 / 4 000 pour le court, 1 000 pour le lecteur) ;
- sortie minimale du lecteur : entre 200 et le minimum général, le lecteur passe et l'expérimentateur, au même plafond, est
  refusé ; sous 200, refus sans envoi ; `--sortie-min-jetons-lecteur 10` fait passer (c'est bien cette option qui est lue) ;
- vérificateur à 0,10 USD, consigne courte → code 0, `max_tokens` ≤ 1 000 (= 1 000), pire cas ≤ 0,10 ; consigne de 60 000
  caractères → code 4, `envoye: false`, rien envoyé, rien réservé ;
- expérimentateur au reste de la borne : 0,80 → sortie courte entière ; 0,02 → code 4 sans envoi ;
- registre cumulé plein (49,99 USD réglés par un autre fournisseur) → code 4 « garde cumulée », rien réservé ; plafond
  relevé → code 0 ; registre illisible → code 4 ; garde d'étape (`PLAFOND_ETAPE_USD=0.001`) → code 4, `6.00` → code 0 ;
- aucune clé : des chaînes témoins posées sous `GEMINI_API_KEY`, `KIMI_API_KEY`, `MOONSHOT_API_KEY`, `ANTHROPIC_API_KEY`
  dans l'environnement de la commande n'apparaissent ni dans la requête au relais (corps, en-têtes ; aucun en-tête
  `Authorization`, `x-api-key`, `x-goog-api-key`), ni dans la dernière ligne, ni sur la sortie d'erreur ; le source de
  Kimi ne contient ni `API_KEY` ni `Authorization` ; les fonctions `appeler`, `principal`, `rendre`, `verifier_url`,
  `plafond_etape`, `bornes_de_sortie` d'Argon non plus ; `ROLES` et `VERSION` des deux modules ;
- relais Argon (`servir`, vrai gestionnaire `fabriquer_gestion`, appelant factice, doublure minimale du collisionneur) :
  402 et 429 rendus et lus par `appeler` v3 en code 4, `envoye: false` ; 411 et 413 rendus à des en-têtes écrits à la main ;
  `/relais/etat` dit « aucune reprise », clé absente, 1 appel ; journal sans texte ; `servir` refuse un collisionneur à
  empreinte différente avant toute clé, et refuse sans `GEMINI_API_KEY`.

Incident d'essai, corrigé avant la livraison : une première version de l'essai des codes 411 et 413 laissait la connexion
ouverte sur un échec ; contre un relais muté qui lirait un corps absent (mutation A12), le relais restait bloqué en lecture
et la suite avec lui (processus arrêtés par leur PID, R10). L'essai ferme maintenant toujours la connexion (`finally`).

Non couvert (comme en v2) : le délai dépassé (code 6), le 502 « modèle servi différent » du relais Kimi (éprouvé par
`test_gardes_mini_course_v2.py` sur la v2, code inchangé), le dépassement de réserve (idem).

## Banc de mutations

```
cd /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp nice -n 10 /home/user/controle-ia-travail/.venv/bin/python -I -B mutations_commandes_tour_ferme_v3.py
```

Le banc copie le dossier, applique une mutation (motif trouvé exactement une fois, sinon il s'arrête), joue la suite avec
`-x` ; le cas sain (dossier non muté) doit passer d'abord (R5). Résultat du 2 novembre 2026 (23:20 à 23:26 UTC) :
**cas sain passé (51 essais, 30 s) ; 23 mutations tuées sur 23 jouées ; code 0 ; 5 min 25 s en tout**.

| id | fichier | mutation | sort | suite | durée |
|---|---|---|---|---|---|
| K1 | `commande_kimi_v3.py` | rôle lecteur_test retiré de ROLES | tuée | 1 failed, 3 passed in 2.33s | 2.6 s |
| K2 | `commande_kimi_v3.py` | sortie minimale du lecteur ignorée (minimum général à sa place) | tuée | 1 failed, 3 passed in 2.33s | 2.6 s |
| K3 | `commande_kimi_v3.py` | sortie maximale du lecteur ignorée (sortie courte à sa place) | tuée | 1 failed, 25 passed in 15.52s | 15.8 s |
| K4 | `commande_kimi_v3.py` | champ envoye perdu sur le refus du plafond de session | tuée | 1 failed, 32 passed in 20.26s | 20.5 s |
| K5 | `commande_kimi_v3.py` | sortie minimale non appliquée (envoi sous le minimum) | tuée | 1 failed, 32 passed in 19.71s | 20.0 s |
| K6 | `commande_kimi_v3.py` | plafond de session absent toléré (défaut 1e9 à la place de nan) | tuée | 1 failed, 12 passed in 7.67s | 8.0 s |
| K7 | `commande_kimi_v3.py` | version v2 rendue | tuée | 1 failed in 0.67s | 0.9 s |
| K8 | `commande_kimi_v3.py` | contrôle de MODELE_DEMANDE_POLE retiré | tuée | 1 failed, 10 passed in 6.31s | 6.6 s |
| K9 | `commande_kimi_v3.py` | champ role absent de la ligne de refus (code 2) | tuée | 1 failed, 8 passed in 5.23s | 5.5 s |
| K10 | `commande_kimi_v3.py` | porte « environnement » incomplète tolérée (ETAPE_POLE seul) | tuée | 1 failed, 14 passed in 9.23s | 9.5 s |
| K11 | `commande_kimi_v3.py` | plafond cumulé du registre remplacé par 1e9 | tuée | 1 failed, 40 passed in 24.66s | 25.0 s |
| A1 | `commande_argon_v56_nuit_v3.py` | rôle experimentateur_test retiré de ROLES | tuée | 1 failed, 6 passed in 4.08s | 4.3 s |
| A2 | `commande_argon_v56_nuit_v3.py` | sortie minimale du lecteur ignorée (minimum général à sa place) | tuée | 1 failed, 29 passed in 17.73s | 18.0 s |
| A3 | `commande_argon_v56_nuit_v3.py` | sortie maximale du lecteur ignorée (sortie courte à sa place) | tuée | 1 failed, 29 passed in 17.81s | 18.1 s |
| A4 | `commande_argon_v56_nuit_v3.py` | champ envoye perdu sur le refus du plafond de session | tuée | 1 failed, 33 passed in 20.95s | 21.2 s |
| A5 | `commande_argon_v56_nuit_v3.py` | sortie minimale non appliquée (envoi sous le minimum) | tuée | 1 failed, 33 passed in 20.11s | 20.4 s |
| A6 | `commande_argon_v56_nuit_v3.py` | plafond de session absent toléré (défaut 1e9 à la place de nan) | tuée | 1 failed, 13 passed in 8.09s | 8.4 s |
| A7 | `commande_argon_v56_nuit_v3.py` | version v2 rendue | tuée | 1 failed, 4 passed in 2.98s | 3.2 s |
| A8 | `commande_argon_v56_nuit_v3.py` | contrôle de MODELE_DEMANDE_POLE retiré | tuée | 1 failed, 11 passed in 7.06s | 7.3 s |
| A9 | `commande_argon_v56_nuit_v3.py` | champ role absent de la ligne de refus (code 2) | tuée | 1 failed, 9 passed in 5.75s | 6.0 s |
| A10 | `commande_argon_v56_nuit_v3.py` | porte « environnement » incomplète tolérée (ETAPE_POLE seul) | tuée | 1 failed, 15 passed in 9.90s | 10.2 s |
| A11 | `commande_argon_v56_nuit_v3.py` | plafond cumulé du registre remplacé par 1e9 | tuée | 1 failed, 41 passed in 25.19s | 25.4 s |
| A12 | `commande_argon_v56_nuit_v3.py` | le relais (servir) tolère un corps sans Content-Length (411 perdu) | tuée | 1 failed, 49 passed in 34.62s | 34.9 s |

## Réserves et défauts portés ailleurs (non corrigés ici : ce n'est pas le code de ce dossier)

1. **TF-02 (porté à conv-audit)** : `AdaptateurCommandeExterne.lancer` rend **tout code ≠ 0 en statut « erreur »** (sauf un
   refus R-764 que la ligne dit elle-même), et `lancer` de l'étage v5 (`tests_de_mort_v5.py`, ≈ l. 341-415) **arrête l'étage**
   (`EtageInterrompu`) sur toute session dont le statut n'est pas « ok », hors « budget_depasse ». Donc un **refus sans envoi
   de la commande (code 4 : pire cas au-dessus du plafond de session, garde cumulée, garde d'étape, 402 ou 429 du relais)
   arrête la course**, alors que l'annexe A dit, pour l'expérimentateur et le vérificateur, « budget_depasse » → fin des tours
   de la carte. Cas concrets : (a) reste de la borne de 0,80 USD de la carte sous ≈ 0,04 USD + entrée (4 096 jetons de sortie
   minimale à 10 USD par million ; par exemple 0,103 USD pour une consigne de 30 000 caractères) : la garde de l'étage ne
   compte que l'entrée (`prix_caractere_usd`), la commande refuse en code 4 ; (b) consigne du vérificateur au-delà de 27 000
   caractères à 0,10 USD ; (c) part d'un relais épuisée (402/429). Remède possible, côté commande (hors périmètre, à décider) :
   rendre ces refus en code 0 avec `cout_usd` = plancher et un texte vide… ce qui serait lu « ok » avec un texte vide, pas
   « budget_depasse » : seul l'adaptateur ou l'étage peut distinguer un refus sans envoi d'une erreur. À conv-audit.
2. `lecteur_test` est aussi permis à Kimi et `experimentateur_test` à Argon (comme `ROLES_PERMIS` de l'adaptateur) : la
   commande ne sait pas quel relais est censé jouer quel rôle ; c'est le lanceur (`roles_reels`) qui route. Pas un défaut, dit.
3. Taille réelle de la consigne du vérificateur non mesurée ici (aucune fiche réelle sous la main) : limite 27 000 caractères
   à 0,10 USD (sortie 200 jetons). À lire sur `traces-lecteur/consigne.md` des premières fiches ; si elle dépasse, relever
   `BUDGET_LECTEUR_USD_DEFAUT` demande un nœud (modification du code gelé).
4. `COLLISIONNEUR_DEFAUT` d'Argon relatif au dossier du fichier : `servir` depuis ce dossier exige `--collisionneur` (voir
   plus haut) ; le relais 8805 reste servi depuis son fichier actuel.
5. Les v2 ne sont pas dans l'arbre du dépôt privé (`find` sans résultat) : les diffs joints partent des copies de
   session-depot, empreintes `644dbb39…` et `221df610…` vérifiées avant fabrication (script de fabrication par remplacements
   exacts, chaque motif trouvé une seule fois).
6. Aucun fichier `.sha256` n'a été créé (consigne de la tâche) : le scellement du dossier revient à session-depot.
