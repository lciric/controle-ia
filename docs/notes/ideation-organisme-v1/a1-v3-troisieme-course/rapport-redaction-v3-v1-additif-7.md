# Additif 7 au rapport de rédaction v3 — sonde v7 : réponse de création catégorisée, `ls-remote` sous mandataire

Même rédacteur-développeur, 4 novembre 2026, de 23:12 à 23:34 UTC (`date -u`).

**Faits constatés par la fille** (23:09 et 23:11 UTC), relayés par le directeur :
- avec la v6, l'appel atteint Vast : le défaut de certificat est corrigé ;
- mais `louer` rend deux fois « CREATION_INCERTAINE : réponse illisible » ;
- aucune instance n'est créée (inventaire filtré), et l'offre visée disparaît ensuite de la liste, deux fois sur deux ;
- la cause est inconnue.

Version 7 à noms neufs (R12) : les v1 à v6 sont inchangées. Elle porte **seulement** les points (a) à (d) de la demande. Mêmes
interdits : aucun commit, aucun `.sha256`, aucune location, aucune clé lue, aucune dépense.

**Verdict.**
- La réponse de `vastai create` est désormais écrite au journal sous une catégorie sûre. Une prochaine tentative dira donc la
  cause (offre prise, image, disque, solde…) sans rien écrire d'autre.
- « no_such_ask » et « erreur Vast » avec `success` faux ne posent plus de marqueur.
- Un échec de `ls-remote` rend le code 6, jamais une destruction.
- **113 essais de la sonde v7 passent.** Résultat de l'ensemble : section 3.

## 1. Fichiers neufs (sha256 : section 4)

Copies renommées de la v6 (étiquette `sonde-a1-v3-v7`, branches `donnees/sonde-hote-durable-a1-v3-v7…`, dossier
`/root/sonde-a1-v3-v7`, fichiers `sonde-v7-*`), puis modifiées :
- `src/controle_ia/sonde_hote_durable_a1_v3_v7.py` ;
- `scripts/amorce_sonde_hote_durable_a1_v3_v7.sh` : seuls les noms changent ;
- `tests/test_sonde_hote_durable_a1_v3_v7.py` : 113 essais, soit les 95 de la v6, dont un adapté, et 18 neufs.

## 2. Ce qui change, et rien d'autre (diff exact : section 5)

**(a) Réponse de création catégorisée** (`categoriser_reponse`, `lire_reponse_de_creation`).

Le texte de la sortie standard de `vastai create` est lu de trois façons, dans cet ordre :
- en entier, en JSON, puis en représentation Python (`ast.literal_eval`, lecture de littéraux seulement) ;
- puis ligne par ligne, depuis la fin, de la même façon.

Le premier dictionnaire trouvé donne la catégorie :

| catégorie | condition | ce qui est écrit | marqueur |
|---|---|---|---|
| **contrat** | `success` vrai et `new_contract` entier | « réponse de création : contrat N » | aucun (location faite) |
| **no_such_ask** | « no_such_ask » dans `error` ou dans `msg` | `error` et `msg` seuls | **aucun** (Vast : rien créé) |
| **erreur Vast** | `success` faux | `error` et `msg` seuls | **aucun** (Vast : rien créé) |
| erreur Vast sans `success` faux | tout autre dictionnaire | `error` et `msg` seuls | posé |
| **illisible** | aucun dictionnaire | la longueur seule | posé |

- `error` et `msg` sont tronqués chacun à 200 caractères, puis masqués par toutes les valeurs des secrets du pilote et du
  mandataire, et par le jeton du corps.
- Aucun autre champ de la réponse n'est écrit : par exemple `extra_env`, qui porte le jeton.
- Les deux refus sans marqueur lèvent `RefusVastSansCreation`, une sous-classe de `RefusAvantAppel`.

**(b) `controler`.**
- `branche_existe` transmet à `git ls-remote` les variables du mandataire présentes.
- Un code non nul, un délai dépassé ou un `git` absent lèvent `RefusRecontroler`, et `controler` rend alors le **code 6**
  (« recontrôler »), sans geste.
- Seul un `ls-remote` réussi qui ne trouve pas la branche vaut « pas de signe de vie ».
- Aucune sortie de `git` n'est écrite.

**(c) Longueurs.** Avant l'appel, le journal de location écrit les longueurs en caractères de `--args` (script de démarrage
encodé), de `--env` et de la commande entière. La vérification seule les écrit aussi.

**(d) Essais.**
- Cas sains : contrat en JSON, en JSON indenté, et en représentation Python précédée d'une ligne.
- Un artefact par catégorie :
  - `no_such_ask` (représentation Python) ;
  - erreur Vast `invalid_args` et `insufficient_credit` ;
  - erreur sans `success` faux ;
  - texte libre ;
  - réponse vide.
- Masquage et troncature : jeton et mot de passe du mandataire absents du message ; `extra_env` jamais écrit ; détail borné.
- `louer` : marqueur absent pour contrat, `no_such_ask` et erreur Vast ; marqueur posé pour l'erreur sans `success` faux et pour
  « illisible ». Le texte illisible n'apparaît jamais au journal ; les longueurs y sont écrites.
- `ls-remote` :
  - cas sain sous mandataire : les variables sont transmises, et `AUTRE` ne l'est pas ;
  - branche absente : faux ;
  - code 128 ou `git` absent : `RefusRecontroler` ;
  - `controler` rend 6 sans geste ; un vrai « pas de vie » reste détruit à T0 + 35.

## 3. Essais (`timeout 900 nice -n 10`, aucun réseau)

- `tests/test_sonde_hote_durable_a1_v3_v7.py` : **113 passés**.
- Ensemble (v7 à v1, lanceur durable, garde de calcul) : **589 passés**, aucun sauté, en 1 001 s
  (113 + 95 + 86 + 72 + 66 + 52 + 19 + 49 + 37). Sortie : `…/sorties/essais-sonde-v7.txt`
  (`91dbffccfc950423d5630fae8833e595f43cdd651411b5e384d538238a3e7481`).

## 4. Empreintes à la remise

Relevées à 23:33 UTC.

| fichier | sha256 |
|---|---|
| `src/controle_ia/sonde_hote_durable_a1_v3_v7.py` (854 lignes) | `7ea53d82ea9df9941c8b4013ae92c222a8f069d8e35d62c397d0fbc38d17a8c0` |
| `scripts/amorce_sonde_hote_durable_a1_v3_v7.sh` | `10bc2239cf1fe3907680670b6a38461895260afdb4f6a5943b54135b41c10704` |
| `tests/test_sonde_hote_durable_a1_v3_v7.py` (113 essais) | `ee6a430be86530c8c3ef641c07bcda67d04a02cf4ab57b631777614a6425f9e1` |
| bloc-notes `sorties/essais-sonde-v7.txt` | `91dbffccfc950423d5630fae8833e595f43cdd651411b5e384d538238a3e7481` |
| bloc-notes `sorties/diff-sonde-v6-vers-v7-brut.txt` | `7557b1be95484521bb308dc6d428616599c695323791dc10e11bb3b2c21fe3db` |
| bloc-notes `sorties/diff-sonde-v6-vers-v7-hors-renommage.txt` | `f947901959c7fb33edba2925273b6952d80e9fe1e23bbd042f4ab193d24f6235` |
| bloc-notes `renommage-v6-v7.sed` | `0ca210aa109c7beaf30d5b7d7eee1b0eefca91ddb2ae02ed799b42a6e7a2cc1e` |

Ce fichier ne porte pas sa propre empreinte : elle est donnée avec la remise. Les instantanés versés pendant le travail sont
intermédiaires ; seules ces empreintes valent pour le rendu.

## 5. Diff exact par rapport à la v6

Les deux diffs sont dans le bloc-notes `/tmp/claude-0/-home-user/4a4722d4-e39d-57bd-bde3-e6a99e2eecdf/scratchpad/v3b1/sorties/` :
- `diff-sonde-v6-vers-v7-brut.txt` : renommages compris ;
- `diff-sonde-v6-vers-v7-hors-renommage.txt` : la v6 renommée par le `sed` de `…/v3b1/renommage-v6-v7.sed`, comparée à la v7.

Le second ne contient que les points (a) à (d).

**Module :**
- paragraphe de tête ;
- classes `RefusVastSansCreation` et `RefusRecontroler` ;
- `creer`, qui appelle `arguments_de_creation` et passe les secrets à `lire_reponse_de_creation` ;
- fonctions neuves `arguments_de_creation`, `longueurs_de_creation`, `_champ_sur` et `categoriser_reponse` ;
- `lire_reponse_de_creation`, réécrite ;
- dans `louer`, les lignes « longueurs » et « contrat N » ;
- `controler`, qui attrape `RefusRecontroler` (code 6) ;
- `branche_existe`, réécrite.

**Amorce :** aucune ligne, hors renommage.

**Essais :** le titre, une attente adaptée (« création refusée » devient « erreur Vast ») et les 18 essais neufs.

## 6. Commande exacte pour la fille

C'est celle de l'additif 6 (section 6), avec `v7` à la place de `v6` :
- dossier `/home/user/hors-clone-sonde-a1-v3-v7`, fichier `sonde_hote_durable_a1_v3_v7.py`, journal
  `journal-location-sonde-v7.log` ;
- même `env -i` avec `HTTPS_PROXY`, `SSL_CERT_FILE` et `REQUESTS_CA_BUNDLE`, pour `louer` comme pour `controler`.

La restriction « `controler` seulement après T0 + 70 » de l'additif 6 (section 7) est **levée** : un `ls-remote` qui échoue rend
désormais 6 et ne détruit rien.

**Avant toute nouvelle tentative**, à cause des deux « illisible » de la v6 :
- refaire l'inventaire filtré ;
- retirer le marqueur `.creation-incertaine` de la v6 seulement après avoir constaté qu'aucune instance n'existe, et l'écrire au
  journal.

Le dossier de la v7 est neuf, donc sans marqueur. Le journal de la v7 dira la catégorie de la réponse et les longueurs de la
commande. Si la catégorie est « erreur Vast » avec un `msg` sur la taille des arguments, l'hypothèse « script trop long » se lit
avec les longueurs.
