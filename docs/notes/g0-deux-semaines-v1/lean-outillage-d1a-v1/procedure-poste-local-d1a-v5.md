# Essai Lean, D-1a — procédure du poste local — v5

- **Pour** : la session mère, qui en tire la consigne de la session locale (Claude Code sur l'ordinateur de Lazar).
- **Écrit par** : l'auteur du harnais (Opus 5.5).
- **Sources** : décision R-2323, contre-lecture `contre-lecture-courte-machine-harnais-d1a-v4.md` (`918662a7…`), section finale.
- **Code** : branche `prep/lean-outillage-d1a-v5`, commit `795fc074c200ea47e8aa9b9e88bae2222473adb5`, non fusionné.
  - Module : `controle_ia.lean_essai.minuterie_v5`.
  - Pilote : `scripts/lean_essai_d1a_v5/piloter_poste_v5.sh`.
- **Statut** : rien de ceci n'a tourné contre l'interface réelle de Hetzner ; les essais tournent sur un faux transport.
  - Cette procédure ne vaut qu'après la contre-lecture courte du tour 5, et sous une consigne neuve de la mère.

## Rôles et règle d'or

- **Session locale** : clone du dépôt, jeton `HCLOUD_TOKEN` dans son environnement (lu par son nom, jamais affiché ni écrit),
  SSH vers la machine. Elle seule crée.
- **Session mère** : dans le nuage, sans SSH, avec son propre `HCLOUD_TOKEN`. Elle lit et détruit par identifiant. Elle
  n'exécute aucun code de la branche : seulement des requêtes de l'interface, dont la forme est donnée en annexe.
- **Lazar** : relaie entre les deux sessions, qui ne se parlent pas.
- **Règle d'or** :
  - aucune création avant que la mère ait prouvé le même projet et le droit d'écrire, puis armé ses deux tâches ;
  - une seule création ; jamais de recréation.
  - La commande refuse d'elle-même une seconde machine sous le même GO : le drapeau `--mot-de-lazar` n'existe plus.

## 0. Prérequis du poste (session locale)

1. **Dépôt** :
   - clone de `https://github.com/lciric/controle-ia-travail`, jamais `lciric/controle-ia` ;
   - branche de travail à soi, au nom fixé par la consigne, partie du commit ci-dessus ;
   - **toutes les commandes se lancent depuis la racine du clone**.
   - La racine du dépôt est déduite de l'emplacement du module ; `--depot RACINE` la force.
2. **Outils** :
   - Python 3.11 ou plus récent : les essais v5 passent sous 3.11 et 3.13 ; la minuterie n'utilise que la bibliothèque
     standard ;
   - `git`, `ssh`, `ssh-keygen`.
3. **Jeton** : `HCLOUD_TOKEN` est posé par Lazar dans l'environnement de la session. C'est un jeton en lecture et écriture
   du projet de l'essai. Jamais `env`, `printenv` ni affichage.
4. **Ordinateur sur secteur, veille coupée** jusqu'à la destruction.
   - Sous macOS : `caffeinate -i -w <PID de la minuterie>`, lancé détaché après L6.
   - La minuterie locale est un garde-fou de second rang : elle meurt avec l'ordinateur. La mère est le garde-fou de fond.
5. **Notation** :
   - `MV5` désigne `PYTHONPATH=src python3 -B -m controle_ia.lean_essai.minuterie_v5` ;
   - `V` désigne le dossier versé `docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1` ;
   - tout fichier passé à `--journal` ou à `--sortie` porte un nom neuf (R12).

## 1. Avant la création

### L1 (locale) — préparer

```
MV5 preparer --go GO-2026-11-10-13 --heure-limite-creation <T_LIM> --heure-tache-mere <H>
```

- `T_LIM` (heure limite de création) et `H` (heure absolue de la première tâche de la mère) sont fixés par la consigne, en
  ISO 8601 UTC.
- **Refus** :
  - `T_LIM` déjà passée ;
  - `H` moins de 2 heures après `T_LIM`, ou plus de 47 heures après maintenant ;
  - GO invalide ;
  - machine déjà inscrite sous ce GO, au journal des créations ou au registre des dépenses.
- **Fichier écrit** : `V/rattrapage-machine-d1a-<jeton12>-v1.json`. Il contient :
  - le jeton ;
  - les étiquettes fixes `essai=lean`, `pas=d1a`, et le nom `lean-outillage-d1a` ;
  - l'heure de préparation et l'heure limite de création : la création est prévue entre les deux ;
  - `H`, `H + 24 h`, et l'échéance de la minuterie au plus tard, `H − 1 h` ;
  - **les deux messages des tâches de la mère**, et les commandes de destruction du poste.

### L2 (locale) — clé SSH et pare-feu étiquetés

```
ssh-keygen -t ed25519 -N "" -C lean-outillage-d1a -f <dossier hors du dépôt>/cle-lean-d1a
MV5 acces-creer --rattrapage V/rattrapage-machine-d1a-<jeton12>-v1.json \
    --cle-publique <dossier hors du dépôt>/cle-lean-d1a.pub --ip-poste <adresse IPv4 publique du poste, donnée par Lazar>
```

- **Objets créés** (gratuits) : une clé SSH et un pare-feu, tous deux nommés `lean-outillage-d1a-<jeton12>`.
  - Étiquettes : `essai`, `pas`, `go`, `creation=<jeton>`.
  - Le pare-feu porte les règles d'installation : SSH depuis le seul poste.
- **Fichier écrit** : `V/acces-machine-d1a-<jeton12>-v1.json` (identifiants et empreinte de la clé).
- **Refus** : une clé privée, une clé sur plusieurs lignes, une adresse qui n'est pas une IPv4 seule.
- La clé privée ne va jamais dans le dépôt ni dans une ligne de commande.

### L3 (locale) — pousser avant toute création

- Committer et pousser les deux fichiers sur la branche du poste.
- Donner à Lazar, pour la mère :
  - la branche et le commit ;
  - le jeton ;
  - les identifiants de la clé et du pare-feu, et l'empreinte de la clé.
- `creer-et-armer` vérifie lui-même que le fichier de rattrapage est suivi par git, égal à `HEAD`, et contenu dans une branche
  distante. Sinon, il refuse avant tout appel.

### M1 à M6 (mère) — s'armer avant la création

- **M1 — lire** : relire les deux fichiers poussés (`git fetch` de la branche du poste) et noter leurs empreintes.
- **M2 — même projet** : par son propre jeton,
  - `GET /v1/ssh_keys?label_selector=creation%3D<jeton>` doit rendre une seule clé, de même identifiant et de même
    empreinte que le fichier d'accès ;
  - `GET /v1/firewalls?label_selector=creation%3D<jeton>` doit rendre un seul pare-feu, de même identifiant.
  - **Sinon : arrêt, aucune création** (les deux jetons ne voient pas le même projet).
- **M3 — droit d'écrire** :
  - `POST /v1/firewalls` avec `{"name": "preuve-ecriture-mere-<jeton12>", "labels": {"essai": "lean", "preuve": "mere"}}` ;
  - puis `DELETE /v1/firewalls/<identifiant rendu>` ;
  - puis `GET` du même identifiant, qui doit rendre 404.
  - C'est gratuit. Un 401 ou un 403 : **arrêt, aucune création**.
- **M4 — destruction à blanc** : `GET /v1/servers?label_selector=essai%3Dlean%2Cpas%3Dd1a` et
  `GET /v1/servers?name=lean-outillage-d1a` doivent ne rendre aucun serveur.
- **M5 — armer deux tâches** : deux tâches programmées uniques (`send_later` de la session mère), **à heure absolue**.
  - La première à `H`, avec le message `taches_mere[0].message` du fichier de rattrapage, recopié tel quel.
  - La seconde à `H + 24 h`, avec `taches_mere[1].message`.
  - Chaque message se suffit : requêtes par étiquettes et par nom, destruction par identifiant après contrôle du nom,
    absence par deux lectures, arrêt sur 401 ou 403, inscription dans `registres/arrets.md`, mot à Lazar, jamais de
    recréation.
  - Noter les identifiants des tâches.
- **M6 — signaler** : dire à Lazar « armée », avec les identifiants des tâches, `H` et `H + 24 h`. Lazar transmet à la session
  locale. **Sans ce mot, aucune création.**

## 2. Création (session locale)

### L4 — juste avant

- `MV5 inventaire` doit rendre « aucun serveur de l'essai ».
- L'heure doit être avant `T_LIM`.
- Le mot « armée » doit être reçu.

### L5 — création détachée

```
MV5 creer-et-armer --go GO-2026-11-10-13 --rattrapage V/rattrapage-machine-d1a-<jeton12>-v1.json \
    --type ccx33 --lieu <lieu du devis> --cle-ssh <identifiant> --pare-feu <identifiant> --deja-depense-usd 0 \
    --journal V/journal-creation-d1a-<jeton12>-v1.jsonl --detache --sortie V/sortie-creation-d1a-<jeton12>-v1.log
```

- **Ce que rend la commande** : tout de suite, le PID du processus détaché et le fichier de sortie. Le processus tourne dans
  une session à lui ; aucun outil ne le coupe au milieu du rattrapage (CLC4-04).
- **Ce que fait le processus**, dans l'ordre :
  1. contrôles :
     - fichier poussé, heure limite, GO ;
     - seconde machine refusée ;
     - type dans la liste du devis (`ccx23`, `ccx33`, `cx53`) ;
     - taux d'au moins 1,25 ;
     - devis ;
  2. intention écrite **avant** l'appel de création ;
  3. création ; si la réponse se perd, recherche par l'étiquette pendant 10 minutes, et destruction de tout serveur trouvé ;
  4. minuterie détachée : échéance `min(création + 48 h, H − 1 h)` ;
  5. **contrôle de sa survie** : PID vivant **et** première ligne « garder » en 60 secondes ; sinon, destruction immédiate
     du serveur par son identifiant.
- **Attendre** la fin du processus (`kill -0 <PID>` toutes les 15 secondes, 15 minutes au plus), puis lire la sortie.
- **Fin normale** : la dernière ligne est un objet JSON avec `identifiant`, `echeance`, `minuterie.pid`,
  `minuterie.fichier_pid` et `minuterie.journal`.
- **Toute autre fin** (ligne « ARRÊT », « RATTRAPAGE À REFAIRE » ou « DESTRUCTION REFUSÉE DURABLEMENT », processus encore
  vivant après 15 minutes, sortie vide) : section 4.

### L6 — dans la minute

```
MV5 verifier-minuterie --fichier-pid <minuterie.fichier_pid> --journal-minuterie <minuterie.journal>
```

- Il doit rendre `"conforme": true`, code 0. Le contrôle passe par `/proc` sous Linux, par `kill -0` et `ps -ww -p` sous
  macOS.
- Sinon : `MV5 detruire --identifiant <N> --journal <neuf>`, puis `MV5 inventaire`, arrêt, compte rendu.

### L7 — pousser et signaler

- Pousser : le journal des créations, le fichier PID, le journal et la sortie de la minuterie, la sortie et le journal de la
  création.
- Donner à Lazar, pour la mère : l'identifiant, l'échéance et le PID.

## 3. Pendant le travail (session locale)

- **Ordre** : `piloter_poste_v5.sh avant …`, puis `MV5 acces-couper --rattrapage … --ip-poste …` et
  `MV5 verifier-coupure --serveur N --pare-feu F --journal <neuf>`, puis `piloter_poste_v5.sh apres …`.
- **À chaque reprise de session, et au moins toutes les heures** : `MV5 verifier-minuterie … --journal-minuterie …`.
  - Non conforme : attendre 2 minutes (l'ordinateur sort peut-être de veille) et refaire.
  - Encore non conforme : `MV5 detruire --identifiant N`, puis arrêt.
- Ne jamais renommer le serveur ni toucher à ses étiquettes : un serveur renommé échappe à tous les garde-fous (R10).
- **Machine injoignable** : `MV5 inventaire`. Si le serveur est absent (la mère ou la minuterie l'a détruit) :
  **ne pas recréer**, compte rendu.

## 4. Fin anormale de la création (session locale)

1. `MV5 detruire --pas d1a --journal <neuf>` tout de suite.
   - Code 0 : lire `detruits`.
   - **Code 3** : Lazar détruit à la main, par l'identifiant, dans la console.
   - Code 4 : refaire.
2. `MV5 inventaire` doit rendre « aucun serveur de l'essai ».
3. **Quinze minutes plus tard**, refaire 1 et 2 : une création tardive reste possible.
4. Compte rendu à Lazar ; aucun second essai.

## 5. Fin normale

1. **Locale** : `MV5 detruire --identifiant N --journal <neuf>`. Code 3 : destruction à la main.
2. **Locale** : `MV5 inventaire` doit rendre « aucun serveur de l'essai », avec `ips_primaires_non_attribuees` vide. Sinon,
   le signaler sans rien supprimer.
3. **Locale** : `MV5 acces-supprimer --rattrapage …` supprime la clé et le pare-feu, après contrôle de leur nom.
4. **Locale** : `MV5 verifier-minuterie …`.
   - Si la minuterie vit encore, l'arrêter par son PID (`kill <PID>`, R10).
   - Normalement, elle s'arrête seule dès que l'absence est constatée par deux lectures ; elle solde alors le journal des
     créations.
5. **Locale** : pousser toutes les pièces. Lazar prévient la mère.
6. **Mère** :
   - relire par son propre jeton (M4) ;
   - inscrire l'arrêt dans `registres/arrets.md` ;
   - alors seulement, désarmer ses tâches, ou les laisser tourner : elles ne trouveront rien.

## 6. Codes de sortie de `minuterie_v5`

| Code | Sens |
|---|---|
| 0 | Fait. |
| 1 | Arrêt : refus, ou serveur créé puis détruit. Lire le message. |
| 2 | Usage. |
| **3** | **Destruction refusée durablement (401 ou 403)** : le serveur est peut-être allumé ; le détruire à la main par son identifiant. |
| **4** | **Rattrapage à refaire** : `detruire --pas d1a` maintenant, puis quinze minutes plus tard. |

## 7. Réserves

- **Aucun appel réel n'a été fait.** La forme `location`, les statuts et les étiquettes ne sont éprouvés que sur un faux
  transport. Les premières lectures réelles sont M2 et M4, faites par la mère.
- **La minuterie locale meurt avec l'ordinateur** (veille, extinction, redémarrage).
  - Si la session locale meurt pendant `creer-et-armer --detache`, le processus détaché continue.
  - Si l'ordinateur s'éteint, la mère détruit à `H`, puis à `H + 24 h` si la première tâche a échoué.
- **Coût au pire**, garde-fous locaux morts : la machine vit au plus jusqu'à `H` (47 heures après la préparation), ou
  `H + 24 h` si la première tâche échoue, soit 71 heures.
  - Cela fait environ 30 USD pour `ccx33`, en extrapolant le pire cas à 48 heures de la contre-lecture (20,19 USD, prix le
    plus haut du relevé, taux 1,25). Ce chiffre n'est pas vérifié ici.
  - Si les deux tâches de la mère échouent aussi, plus rien ne borne la dépense (contre-lecture, question 3).
- **Le fichier de rattrapage ne prouve pas que la mère l'a lu.** C'est le mot « armée » (M6), relayé par Lazar, qui ouvre
  la création ; la commande ne peut pas le vérifier.

## Annexe — forme des requêtes de la mère

Le jeton est lu par son nom. Il n'apparaît ni à l'écran ni dans une ligne de commande : l'en-tête est passé sur l'entrée
standard de `curl` (`-H @-`), et `printf` est une commande interne du shell. Les réponses se lisent pour leurs identifiants et
leurs noms seulement.

```
API=https://api.hetzner.cloud/v1
printf 'Authorization: Bearer %s\n' "$HCLOUD_TOKEN" | curl -sS -H @- "$API/servers?label_selector=essai%3Dlean%2Cpas%3Dd1a"
printf 'Authorization: Bearer %s\n' "$HCLOUD_TOKEN" | curl -sS -H @- "$API/servers?name=lean-outillage-d1a"
printf 'Authorization: Bearer %s\n' "$HCLOUD_TOKEN" | curl -sS -X DELETE -H @- "$API/servers/<identifiant>"
printf 'Authorization: Bearer %s\n' "$HCLOUD_TOKEN" | curl -sS -X POST -H @- -H 'Content-Type: application/json' \
    -d '{"name": "preuve-ecriture-mere-<jeton12>", "labels": {"essai": "lean", "preuve": "mere"}}' "$API/firewalls"
```

- **Avant tout `DELETE`** : relire le serveur (`GET $API/servers/<identifiant>`) et vérifier que son nom est exactement
  `lean-outillage-d1a`.
- **Absence** : `GET $API/servers/<identifiant>` rend 404, **et** l'identifiant manque aux deux listes.
