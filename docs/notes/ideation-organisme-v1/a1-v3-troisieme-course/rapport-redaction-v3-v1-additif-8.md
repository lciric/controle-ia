# Additif 8 au rapport de rédaction v3 — sonde v8 : refus sur la sortie d'erreur et nouvel essai sur « no_such_ask »

Même rédacteur-développeur, du 4 novembre 2026 à 23:39 UTC au 5 novembre à 00:12 UTC (`date -u`). Le conteneur a
redémarré vers 23:45 UTC, pendant la suite complète : les fichiers étaient sur disque, et la suite a été relancée.

**Faits constatés par la fille** (23:35 et 23:38 UTC), relayés par le directeur :
- Avec la v7, la création rend « illisible (longueur 0) » et rien n'est créé.
- Un essai sur une offre inexistante (identifiant 1) le confirme : avec `--raw`, `vastai` 1.8.3 écrit ses refus sur la **sortie
  d'erreur**, avec le **code 0** et une sortie standard vide. Le message prend la forme
  `{'success': False?, 'error': True, 'msg': 'error 404/3603: no_such_ask  Instance type by id 1 is not available.'}` (115
  caractères).
- La longueur de `--args` (8 000 caractères) n'y change rien.
- Trois fois sur trois, l'offre visée disparaît de la liste juste après la tentative.

Version 8 à noms neufs (R12) : les v1 à v7 sont inchangées. Elle porte **seulement** les points (a) à (c) de la demande. Mêmes
interdits : aucun commit, aucun `.sha256`, aucune location, aucune clé lue, aucune dépense.

**Verdict.** La v8 lit le refus là où `vastai` l'écrit, même avec le code 0. Sur « no_such_ask », elle essaie l'offre conforme
suivante, jusqu'à cinq essais en tout, sans marqueur. **126 essais de la sonde v8 passent.** Résultat de l'ensemble : section 3.

## 1. Fichiers neufs (sha256 : section 4)

Copies renommées de la v7 (étiquette `sonde-a1-v3-v8`, branches `donnees/sonde-hote-durable-a1-v3-v8…`, dossier
`/root/sonde-a1-v3-v8`, fichiers `sonde-v8-*`), puis modifiées :
- `src/controle_ia/sonde_hote_durable_a1_v3_v8.py` ;
- `scripts/amorce_sonde_hote_durable_a1_v3_v8.sh` (seuls les noms changent) ;
- `tests/test_sonde_hote_durable_a1_v3_v8.py` : 126 essais, soit les 113 de la v7 (deux attentes adaptées) et 13 neufs.

## 2. Ce qui change, et rien d'autre (diff exact : section 5)

**(a) Lecture des deux sorties.** `creer` capture la sortie standard **et** la sortie d'erreur. `lire_reponse_de_creation` les lit
dans cet ordre :
1. il catégorise la sortie standard ;
2. si elle est illisible, il catégorise la sortie d'erreur ;
3. si les deux sont illisibles, la catégorie est « illisible », avec les deux longueurs et le code.

Règles de lecture :
- **Le code de sortie ne décide jamais seul :** un code 0 sans contrat est un refus.
- **Texte mal formé** (comme `'success': False?`) : `_champs_par_motif` en extrait `error`, `msg` et `success` par motif. Rien
  d'autre que la catégorie et ces deux champs, tronqués et masqués, n'est écrit.
- **Certificat :** les mots du certificat restent cherchés dans la sortie d'erreur. Un certificat refusé, avec une sortie standard
  illisible, donne toujours « appel non parvenu à Vast (certificat) ».

**(b) Nouvel essai sur « no_such_ask ».**
- La nouvelle classe `RefusNoSuchAsk` est une sous-classe de `RefusVastSansCreation` : elle ne pose pas de marqueur.
- Sur ce refus, `louer` essaie au plus **4 autres** offres conformes (`ESSAIS_NO_SUCH_ASK` = 5 en tout), par prix croissant.
- Chaque offre est revérifiée par `verifier_offre_sonde`.
- Pour chaque essai, `louer` recalcule la garde de dépense (`verifier_plafond`), l'échéance absolue et le corps. Si la garde refuse
  une offre plus chère, `louer` s'arrête avant l'appel, sans marqueur.
- Le journal écrit chaque essai (« essai n/N : offre, prix, dépense, longueurs ») et chaque refus.
- Au cinquième « no_such_ask », ou après la dernière offre conforme, le refus est final, sans marqueur.
- Toute autre réponse arrête la boucle :
  - une erreur Vast avec `success` faux ou un certificat : sans marqueur ;
  - une réponse illisible, une erreur sans `success` faux ou un délai : avec marqueur.
- L'état écrit l'offre réellement louée.

**(c) Essais.**
- Cas sain : un contrat sur la sortie standard, avec un avertissement sur la sortie d'erreur.
- Artefacts :
  - un refus sur la sortie d'erreur avec le code 0 (forme exacte de la fille, et forme Python bien formée) ;
  - un refus sur la sortie standard (`invalid_args`) ;
  - un refus sur la sortie d'erreur avec le code 1 (`insufficient_credit`, jeton masqué) ;
  - deux flux vides : illisible.
- `no_such_ask` puis un contrat au deuxième essai : les offres 100 puis 101, l'état à 0,06 USD/h, aucun marqueur.
- Cinq `no_such_ask` : exactement cinq appels (offres 100 à 104), refus final, aucun marqueur.
- Deux offres conformes seulement : deux essais ; l'offre avec carte n'est jamais essayée.
- Erreur autre que `no_such_ask` : un seul appel, sans marqueur ; illisible : un seul appel, avec marqueur.
- Garde de dépense recalculée : la seconde offre dépasse le plafond, donc arrêt avant son appel.

## 3. Essais (`timeout 900 nice -n 10`, aucun réseau)

- `tests/test_sonde_hote_durable_a1_v3_v8.py` : **126 passés**.
- Ensemble (v8 à v1, lanceur durable, garde de calcul), relancé après le redémarrage : **713 passés sur 715**, aucun sauté,
  en 1 229 s (`…/sorties/essais-sonde-v8.txt`, `3d0a422bd5e161c7386beb949fcec00a4fc05260086c4792e4592c6f51f7a6cd`).
  Deux échecs, l'un et l'autre traités :
  - **essai v8 des longueurs** : son attente venait de la v7 (« --args N caractères ») ; la v8 écrit les longueurs à chaque essai
    (« --args N, --env M, commande K »). J'ai adapté l'attente.
  - **`tests/test_garde_calcul.py`, cas « hors de sa période » à demain** : la suite a passé minuit UTC. Les essais calculent
    « aujourd'hui » à leur collecte (le 4 novembre), et la garde à l'exécution (le 5). La ligne datée du 5 est donc devenue
    valide. Ce n'est pas un défaut de la sonde ; le fichier, qui existait déjà, n'est pas modifié.
- Après la correction : `tests/test_sonde_hote_durable_a1_v3_v8.py` et `tests/test_garde_calcul.py` rejoués, **163 passés**
  (126 + 37) (`…/sorties/essais-sonde-v8-reprise.txt`, `862ff22335325d3455793ab7fc8cc31427cff851bb19f34017f4b1902a7f6747`).
  Les 552 autres essais de l'ensemble avaient passé et ne dépendent d'aucun fichier modifié.

## 4. Empreintes à la remise

Relevées le 5 novembre 2026 à 00:11 UTC.

| fichier | sha256 |
|---|---|
| `src/controle_ia/sonde_hote_durable_a1_v3_v8.py` (933 lignes) | `4a635eb8aa058ab9e7053ce8aa2660272a59e02b1b03ceff5d6c51c5877c71a9` |
| `scripts/amorce_sonde_hote_durable_a1_v3_v8.sh` | `d58bb8cb8633250046f7aa3e588df6cbb48db2310db2f4e52998d32a436cb3e2` |
| `tests/test_sonde_hote_durable_a1_v3_v8.py` (126 essais) | `675d870460ba91a1d9539806fccdc8d29978676e36a12f415f477b831a6cd6dd` |
| bloc-notes `sorties/diff-sonde-v7-vers-v8-brut.txt` | `a0c886395484f154d176c04172cb494c5c5b08ad602a6b3a71f4d82676cfc43d` |
| bloc-notes `sorties/diff-sonde-v7-vers-v8-hors-renommage.txt` (330 lignes) | `47f1ee191a65d570049aa32912e7ecda167f910c81665d50d17bef9389c7f243` |
| bloc-notes `renommage-v7-v8.sed` | `5db99fc74e076e54c7614cd4a84351a983a6a47ccc80f5df2fc613b0a1d6c6d4` |

Ce fichier ne porte pas sa propre empreinte : elle est donnée avec la remise. Les instantanés versés pendant le travail sont
intermédiaires ; seules ces empreintes valent pour le rendu.

## 5. Diff exact par rapport à la v7

Les diffs sont dans le bloc-notes `/tmp/claude-0/-home-user/4a4722d4-e39d-57bd-bde3-e6a99e2eecdf/scratchpad/v3b1/sorties/` :
- `diff-sonde-v7-vers-v8-brut.txt` : renommages compris ;
- `diff-sonde-v7-vers-v8-hors-renommage.txt` : la v7 renommée par `…/v3b1/renommage-v7-v8.sed`, comparée à la v8.

Le second ne contient que (a) à (c) :
- **Module :**
  - le paragraphe de tête ;
  - `ESSAIS_NO_SUCH_ASK` ;
  - la classe `RefusNoSuchAsk` ;
  - `creer`, réécrit : deux sorties, certificat, lecture de la réponse ;
  - `categoriser_reponse`, qui se replie sur `_champs_par_motif` ;
  - la fonction neuve `_champs_par_motif` ;
  - `lire_reponse_de_creation`, avec les deux flux et « no_such_ask » distinct d'« erreur Vast » ;
  - dans `louer`, la vérification seule à part et la boucle des essais, qui remplace l'appel unique.
- **Amorce :** aucune ligne.
- **Essais :** deux attentes adaptées (« illisible (sortie standard » ; longueurs écrites à chaque essai) et les 13 essais
  neufs.

## 6. Commande exacte pour la fille

C'est celle de l'additif 6 (section 6), avec `v8` à la place de `v6` :
- dossier `/home/user/hors-clone-sonde-a1-v3-v8` ;
- fichier `sonde_hote_durable_a1_v3_v8.py` ;
- journal `journal-location-sonde-v8.log` ;
- même `env -i`, avec `HTTPS_PROXY`, `SSL_CERT_FILE` et `REQUESTS_CA_BUNDLE`.

`offres.json` doit contenir plusieurs offres conformes : la boucle les y prend. Il faut le lire juste avant `louer`, puisque les
offres sans carte disparaissent vite. L'additif 7 vaut toujours : `controler` à toute heure.
