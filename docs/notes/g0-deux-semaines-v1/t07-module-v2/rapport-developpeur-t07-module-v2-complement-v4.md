# T0.7, module de lecture v2 — rapport complémentaire 4 du développeur (variante B, ordres brouillons 2 et 3, contre-lecture différentielle DF-01 à DF-08)

- **Auteur** : le développeur du module (sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, Claude Opus 5.5) ; arbre
  `/home/user/wt-t07`, branche `prep/t07-module-v2`.
- **Écrit** le 2026-11-10, de 09:05 à 09:55 UTC (`date -u`).
- **Consignes** : (1) message de la mère (R-2112) : ordre d'exécution de l'étape A en **variante B**, brouillon 2, avec devis,
  et répétition du bloc de l'instance sur une racine locale en jouet ; puis R-2115 : `GO_VARIANTE_B_T07` = **GO-2026-11-10-06** ;
  (2) contre-lecture différentielle du code de `1f77b34d` à `dc4cab9d` (`docs/notes/g0-deux-semaines-v1/t07-module-v2/contre-lecture-code-t07-v2-differentiel.md`,
  `dd794e2e9e14f4dc4b2b9eecfb36819ac494dda50aaa9642c8fe2f026166709b`, empreinte vérifiée, lu en entier) : DF-01 à DF-04,
  `raises=` des trois xfail, artefacts du repli ; commit neuf, essais, répétition jouet v2, poussée de la branche.
- **Interdits tenus** : aucun `lecture-sondes-t06.json` ouvert (celui des runs jouets compris) ; aucune donnée de 7a ; aucune
  valeur de clé ; aucun appel externe, aucune dépense ; recherches par `git grep` sur des chemins nommés ou exclusions (règle 9) ;
  garde des secrets à 0 avant chaque commit. Le rapport de contre-lecture est lu à son chemin dans l'arbre de la mère (lecture
  seule, chemin donné par la mère).

## 1. Verdict

L'ordre d'exécution de la variante B est écrit, **brouillon 3** (`b053a220…`), avec `GO-2026-11-10-06` rempli. Son script
d'instance a été **répété en jouet sur une racine locale** : le premier passage a trouvé un défaut, corrigé ; le passage au commit
`8ae9fc44` est conforme. Les défauts DF-01 à DF-04, DF-06 et DF-08 sont corrigés, avec les artefacts du repli. Suite de T0.7
(14 fichiers) : **324 passés, 1 sauté, 3 échecs attendus** ; répétitions v2 (normale et repli) en code 0. Commit du code à citer
dans `CODE-T07` : **`8ae9fc44`** (section 8), après la contre-lecture courte de ce différentiel (R-2104).

## 2. Commits

| commit | jalon | contenu |
|---|---|---|
| `5c93af19` | 12 | repli en deux temps (première forme), script de l'instance, script de répétition locale |
| `87536cbc` | 13 | script corrigé par la répétition locale (passage 1 en défaut, passage 2 conforme) |
| `0d945fdb` | 14 | ordre, brouillon 2 (variante B), scellé `a0d75ce1…` |
| **`8ae9fc44`** | **15** | **corrections DF-01 à DF-04, DF-06, DF-08 ; artefacts du repli ; script aligné** |
| `a4880428` | 16 | ordre, brouillon 3, scellé `b053a220…` ; répétitions au commit `8ae9fc44` |
| (ce rapport) | 17 | rapport complémentaire 4, scellé |

## 3. Ordre d'exécution, variante B

| brouillon | chemin | empreinte | état |
|---|---|---|---|
| 2 | `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon2.md` | `a0d75ce14cdc402945c0f015bb85bfb6af20cfe16adf74eb2a417fa87073292a` | gardé (R12) ; script `eea99808…`, `GO_VARIANTE_B_T07` en marqueur |
| **3** | `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon3.md` | **`b053a2207006c49d7aca8d8e5975d7539857474d98591368088cda1fc2a1b484`** | **à contre-lire** ; script `99e4c926…`, GO-2026-11-10-06, DF-01, DF-02, DF-04 |

Le brouillon 3 n'était pas demandé : le brouillon 2, scellé, citait le script `eea99808…`, que les corrections DF-01 et DF-02
changent (écart déclaré).

- **Création** d'une instance A100 SXM4 80 Go neuve par la fille (filtre de la chaîne de T0.6 : fiabilité ≥ 0,98, débit ≥
  500 Mb/s, CUDA ≥ 13,0 ; 100 Go de disque ; `python:3.11-bookworm` ; mode « args »), après la poussée vérifiée de 7b ;
  commande précédée de `GO_ID=GO-2026-11-10-06` (garde de calcul) ; **minuterie** de l'instance : destruction par son
  identifiant à création + 12 h ; H200 seulement après un mot de Lazar, hors de cet ordre.
- **Le script de l'instance** (`scripts/etape_a_t07_variante_b_v1.sh`, `99e4c926…`) : clone partiel du code au commit S7
  (descendant de C7, arbre gelé égal) ; registres et fichiers cités recopiés de `main` (les quatre lignes de jeux et de
  concepts, journaux du script) ; **sortie de 7b par refspec explicite**, fichiers nommés seulement (manifeste, épisodes,
  distillation, adaptateurs, mesures, textes, sous-ensemble ; `diag/<run>/` jamais listé ; `lecture-sondes-t06.json` jamais
  descendu, objet manquant du clone partiel) ; essais ; puis **`CODE-T07`, repli (garde d'abord), passe à blanc, étape A** ;
  poussées sur `donnees/t07-etape-a-v1` ; « stopped » demandé ; la fille vérifie la poussée et **détruit par l'identifiant**.
- **Marqueurs** du brouillon 3 (dix, une occurrence chacun) : `ID_SESSION_FILLE`, `EMPREINTE_CONFIG_T07`, `LIGNE_SCELLEMENT_T07`,
  `DEPENSE_ANTERIEURE_USD`, `RUN_T06_7B`, `BRANCHE_7B`, `COMMIT_CODE_T07`, `COMMIT_SCELLEMENT_T07`, `CHEMIN_CONFIG_T07`,
  `LIGNE_ESSAIS_T07`. Remplis : `GO_VARIANTE_B_T07` = GO-2026-11-10-06 ; plafond 20 USD.

### 3.1 Devis de la variante B (A100 ≤ 1,30 USD de l'heure ; recalcul des activations, puis étape A)

| Phase | Attendu (h) | Pire cas (h) | Source |
|---|---|---|---|
| Création, démarrage, image | 0,10 | 0,30 | E2 (R-1689 : démarrage en file 17 min) |
| Clone partiel, registres, sortie de 7b | 0,10 | 0,45 | E2 (R-1687 : clonage partiel 10 s) ; borne de l'amorce de T0.6 (900 s) |
| Paquets | 0,15 | 0,50 | installation bornée à 3 600 s ; non mesuré à part, **supposé** |
| Modèle (≈ 16 Go) | 0,10 | 1,00 | ≥ 500 Mb/s : ≈ 0,07 h ; pire : débit dix fois plus bas (E2 : ≈ 10 Mb/s reçus) |
| Essais de T0.7 (14 fichiers) | 0,30 | 0,60 | mesuré ici : 803 s (4 cœurs partagés) |
| Repli (garde, recalcul, garde d'équivalence) | 0,10 | 0,40 | brouillon 19 : 576 épisodes × 0,45 s ≈ 0,07 h (**supposé** même longueur que P3) ; une relance R11 au pire |
| Passe à blanc | 0,10 | 0,20 | échantillon |
| Étape A | 2,00 à 3,50 | 4,00 à 7,00 | brouillon 19, « Calcul et dépense » ; pire : hôte deux fois plus lent |
| Poussées | 0,10 | 0,30 | ≤ 2 Go |
| **Total** | **3,2 à 4,7** | **7,8 à 10,8** | |

**Attendu ≈ 5,4 à 7,4 USD** (carte et disque ≈ 4,2 à 6,1 ; téléchargement borné à 24 Go × 0,05 = 1,20 ; disque après l'arrêt
≤ 0,08 USD de l'heure). **Pire cas ≈ 11,4 à 15,3 USD.** Plafond de GO-2026-11-10-06 : 20 USD ; la minuterie (création + 12 h)
borne la carte à ≈ 15,6 USD, soit ≤ 17,7 USD tout compris. Compte rendu à 10 USD ; arrêt dès que cumul + un quart d'heure ≥ 20.
Le brouillon 19 (≈ 4 à 5 USD, pire ≈ 9 à 10) ne comptait ni les essais, ni la passe à blanc, ni l'étape A à son devis propre.

### 3.2 Répétition locale du script de l'instance (mode jouet)

`scripts/repetition_jouet_variante_b_t07_v1.py` : course 7b jouet (chaîne de T0.6 de `1609a4bf`, entropie 1), dépôt distant
local (`main` C7, S7, H avec `CODE-T07` et `GO-LECTURE-T07` ; branche de 7b telle que l'amorce v11 la pousse, avec un
`lecture-sondes-t06.json` factice), puis **le script joué tel quel par `bash`, sous `env -i`**, en essai local (`ESSAI_LOCAL=1` :
racine, dépôt et interpréteur locaux, essais réduits à un fichier, ni minuterie, ni Vast, ni modèle descendu).

| passage | script | heures (UTC) | code | résultat |
|---|---|---|---|---|
| 1 | `f75fec22…` | 09:12:38 à 09:13:32 | 3 | **défaut trouvé** : fichiers suivis à S7 hors de l'extraction partielle (tâches citées par la configuration de 7b), recopiés puis retirés par git au changement de branche ; en réel, les tâches de T0.5 et des jeux versés avant S7 l'auraient été aussi ; repli en R11, traces poussées |
| 2 | `eea99808…` | 09:15 à 09:22 | 0 | corrigé (chemin ajouté à l'extraction partielle avant la recopie) ; trois commits poussés |
| **3** | **`99e4c926…`** (`8ae9fc44`) | **09:35:50 à 09:37:29** | **0** | essais 20 passés ; `CODE-T07 conforme` (18 fichiers, `src/controle_ia/` égal au commit, arbre propre) ; **repli : garde d'ouverture d'abord, « recalcul fait »**, garde d'équivalence (21 actions, écart 0), rapport scellé à côté des activations ; passe à blanc tenue ; étape A code 0 ; trois commits ; `SCORES-T07`, `SONDES-T07` au registre poussé ; `src`, `tests` inchangés ; `lecture-sondes-t06.json` **ni dans l'arbre, ni descendu** ; **artefact** (branche déjà poussée) : code 2, repli non joué |

Pièces : `repetition-jouet-variante-b-v1/` (passages 1 et 2) et `repetition-jouet-variante-b-v2/` (passage 3), sous
`docs/notes/g0-deux-semaines-v1/t07-module-v2/`, compagnons. Non répétés (réel seulement) : minuterie et Vast, installation
des paquets, descente du modèle, carte.

## 4. Contre-lecture différentielle : défaut par défaut

| id | état | ce qui est fait (commit `8ae9fc44`) | essais (cas sain ; artefact) |
|---|---|---|---|
| **DF-01** | **corrigé** | `repli_etapes_v1.repli` : **garde d'ouverture de l'étape A** (journalisée : lignes, sceaux, GO, refus de la course 7a, `CODE-T07`, garde adaptée) **avant tout recalcul** ; recalcul **sous un nom daté** `activations-repli-<date>/`, renommé `activations/` après la garde d'équivalence (rien n'est écrasé) ; **rapport scellé à côté des activations** (empreinte des activations) ; **reprise** sur un recalcul couvert, sans recalculer ; **relance R11** sous un nom daté neuf. `lecture_v2 repli-recalcul`, `repli-seul` et `etape-a-apres-repli` passent par là | garde puis recalcul puis reprise ; garde refusée (ligne manquante) → rien calculé, puis relance ; course 7a refusée avant tout calcul ; équivalence en échec puis relance sous un nom neuf ; reprise refusée (sans rapport, activations retouchées) ; commandes |
| **DF-02** | **corrigé** | `CODE-T07` **exigée et contrôlée à l'étape B** (`code_t07_exige` vrai), **dans la passe à blanc** (avant tout, refus code 2) et **avant le repli** (garde) ; `controler_code` exige en plus que **tout `src/controle_ia/`** de l'arbre exécuté égale le commit cité (`git diff` vide : paquets importés) et que l'arbre de travail y soit **propre** (`git status`) ; le script exporte `PYTHONDONTWRITEBYTECODE=1` | étape B saine, puis module retouché → refus ; passe à blanc : absente → refus, conforme → tenue, retouché → refus ; paquet importé changé après C7 → refus ; fichier non suivi → refus |
| **DF-03** | **corrigé** | jeu vidé par le rejeu du contrôle 9 alors que son concept est lu : `GardeArret` nommée (« vidé par le rejeu »), `arret.json`, code 3 | rejeu vidant J-D et J-C → arrêt nommé, `arret.json` ; sain : étapes A des autres essais |
| **DF-04** | **corrigé** | la passe à blanc juge la **mémoire de la notation** : 4 × largeur × jetons notés (`mesures-t06.npz`, sceau vérifié, colonne `jetons_notes` seule), × 2 copies, ≤ 0,8 du disponible ; mesures illisibles → arrêt | besoin écrit, tenue ; notation de 40 Gio → arrêt ; mesures absentes → arrêt « non estimable » |
| DF-05 | **non fait** (non demandé) | motif de l'échec de T7-P6 dans l'index des scores | — |
| **DF-06** | **corrigé** | `raises=` : `AssertionError` (CT-01), `JournalFautif` (cas sain de (xv), CT-11) | les trois échouent comme attendu |
| DF-07 | **à l'ordre** | brouillon 3 : passe à blanc tenue, au même commit et à la même configuration, avant l'étape A (script) ; au texte : règle du rejeu et nom du journal du script | — |
| **DF-08** | **corrigé** | `scripts/repetition_jouet_t07_v2.py` lit l'entropie dans les graines du manifeste | répétitions v2 : `entropie_manifeste` = [1] |

**Artefacts du repli demandés** (`tests/test_t07_repli_etapes_v1.py`) : identité à dose 0 en échec (logits de la base perturbés)
→ arrêt R11 ; texte décodé différent → arrêt ; clé différente → arrêt ; relance après un refus de la garde et après un échec de
la garde d'équivalence ; cas sains : recalcul conforme (égalité au bit près dans `test_t07_repli_recalcul_v1.py`, répétition repli
v3), reprise.

**Essai existant retouché (déclaré)** : `test_sous_commande_de_lecture_v2` (`tests/test_t07_passe_blanc_v1.py`) : le run du modèle
qu'il crée reçoit les mesures de la course factice, que la passe lit désormais (DF-04).

## 5. Essais (heures par `date -u`)

| run | heures (UTC) | résultat |
|---|---|---|
| `tests/test_t07_*.py`, **14 fichiers**, commit `8ae9fc44` | 09:35:48 à 09:49:12 | **324 passés, 1 sauté, 3 échecs attendus**, 803 s |
| répétition jouet v2, entropie 1, chemin normal | 09:37:57 à 09:38:47 | T0.6 0, étape A 0, étape B 0 ; 84 actions, 7 sans mot exclues des témoins ; T7-P10 : dissimulation au-dessus de son témoin, domaine R8 ; issue L1b ; `repetition-jouet-v5/` |
| répétition jouet v2, entropie 1, repli (`repli-recalcul`, garde d'abord) | 09:38:49 à 09:39:33 | codes 0 ; **252 activations recalculées égales au bit près** ; issue L1b ; `repetition-jouet-repli-v3/` |
| répétition locale du script de l'instance | 09:35:50 à 09:37:29 | conforme (section 3.2) |

Ligne attendue de la suite (pour `LIGNE_ESSAIS_T07`, à mesurer dans l'environnement de l'instance) : « 324 passed, 1 skipped,
3 xfailed » dans cette session (Python 3.13.18).

## 6. `CODE-T07` : commit à citer et fichiers à inscrire

Commit **`8ae9fc44df4599af1e036e979af46aa8fa8f6185`** ; arbre `src/controle_ia` à ce commit `013a273b4d47c45e20355b754bd82489f90181f0`
(tout `src/controle_ia/` est contrôlé contre le commit, DF-02). Fichier écrit par `python -m controle_ia.t07.code_t07_v1 ecrire
/home/user/wt-t07 8ae9fc44 <sortie>` (18 fichiers ; à sceller, puis ligne `CODE-T07` par la mère, après la contre-lecture courte de
ce différentiel et la répétition à ce commit, faite) :

| fichier | sha256 |
|---|---|
| `src/controle_ia/t07/__init__.py` | `553bd9d29b56f0923859da2d3a63fadf9891c4274b9bb23fc367496e77e5a61e` |
| `src/controle_ia/t07/code_t07_v1.py` | `52f44ce039d63813cf406b4827d3bf369f2523831dd58f01101a49520cdf01ec` |
| `src/controle_ia/t07/controle_jeux_v1.py` | `27cf1fba9584f41632af4b352b048ecf46e8cc53695499385dd8c8eddc92a3ae` |
| `src/controle_ia/t07/criteres_v1.py` | `12b999fecce093372a29fb70d8c11eb7fe965f34c8746a31b399baaecc5ae8c5` |
| `src/controle_ia/t07/donnees_p3_t07_v1.py` | `acf02303b98157411dd30881d19ec9457423afdc7c27ef4e9342823234030cf4` |
| `src/controle_ia/t07/garde_adaptee_v1.py` | `7ff571d7b1f06db94043545bfe178a066613ddd734aacca1cf3ef52ba0b511de` |
| `src/controle_ia/t07/journal_p3bis_v1.py` | `f83f03d54accc0ac189e05c2f3e865b27ecb817f6c9366836d6e38d016826f73` |
| `src/controle_ia/t07/lecture_v1.py` | `62b34790346123924c275c4e2021ea31db26837c5b7840e9e047d272a54c9678` |
| `src/controle_ia/t07/lecture_v2.py` | `39c56e4b11d915775b47242b63ab1d1c2f56218b38ffc7621d9c3d83bff296f9` |
| `src/controle_ia/t07/lectures_t07_v1.py` | `05328122cdeeedc49b92985df3d9ec41ae668ede8771de3248a10ae3696b4abd` |
| `src/controle_ia/t07/mahalanobis_v1.py` | `b28163062aa8d39cf3894b327a7446f63d50d4f1394eac894b16b4da8ff962f9` |
| `src/controle_ia/t07/passe_blanc_v1.py` | `ff84d2450d5b4a4b39db8ca7d042805a8efd8261349d0608de0e65442fdab578` |
| `src/controle_ia/t07/plancher_v1.py` | `ac6e8263293ed30c807ef91f8eab0adbcbf8e1b91d5e4c56e73dbffa1a7099dc` |
| `src/controle_ia/t07/registre_v1.py` | `914b8f374ce8f8bc6550d03c34c5f6c2a97ac93b8ce44da24fd88229185ffca0` |
| `src/controle_ia/t07/repli_etapes_v1.py` | `26a6b52151a29f3b65ba4c48027a3ed70890f71fc262ca16bba3e51531dfaff2` |
| `src/controle_ia/t07/repli_recalcul_v1.py` | `9ceabbcb56cacde0cad6e849a36884139b0175bdf20af5e34cf4514d9da3fe1d` |
| `src/controle_ia/t07/repli_v1.py` | `7ae5862da1c867d99cbbdfa0c2350a238920c314a8924254abaf368dd335223a` |
| `src/controle_ia/t07/sondes_neuves_v1.py` | `d4d354e769de279235a202b1ac803b6b508bb12a374f48d0352db13daaab9bc7` |

## 7. Autres fichiers et empreintes (commit `8ae9fc44`, sauf mention)

| fichier | sha256 |
|---|---|
| `scripts/etape_a_t07_variante_b_v1.sh` | `99e4c92611c2f161249499816c29fbba52553165a33fb3b3e86c47a7fdbc6a0f` |
| `scripts/repetition_jouet_variante_b_t07_v1.py` | `60efaeee93c0aa3a72e25e548bb626bd51d6c1688d262089a85d51d0ca297e0b` |
| `scripts/repetition_jouet_t07_v2.py` | `4ff49aafabff0d07749449afd73c933f82210a0ce15026aa329c8474781c8584` |
| `tests/test_t07_repli_etapes_v1.py` | `a4988bea9b102ad49dda3423faa16486275780d2c11ec552506116fa80bdd9c8` |
| `tests/test_t07_code_t07_v1.py` | `fd8fcc996ec2f2dbaa896ebcec9e6b0cbd240cbe190085f543ec44b9919e5a5c` |
| `tests/test_t07_passe_blanc_v1.py` | `17049124f6f3d23a0c727b88d75874109cbd17dc5bbcf09f51d04842c2b0a2a5` |
| `tests/test_t07_controle_jeux_v1.py` | `239da09985d1e0de6b0e5433b4d397e8b0c07babee2a4633903475d2aec5615f` |
| `tests/test_t07_corrections_cl1_v1.py` | `10bec781dac57866dd237be12734cc047bff248fb2b0963747ff809f0d71e254` |
| `tests/test_t07_lecture_v2.py` | `58afcf9b90da76de4c11ac2eddf8e544516bab5880a38de5ba96bc0240fd0bac` |
| ordre, brouillon 2 (`0d945fdb`) | `a0d75ce14cdc402945c0f015bb85bfb6af20cfe16adf74eb2a417fa87073292a` |
| ordre, brouillon 3 (`a4880428`) | `b053a2207006c49d7aca8d8e5975d7539857474d98591368088cda1fc2a1b484` |
| répétition locale, passage 3 : journal, résumé, journal de l'instance | `10d88306…`, `79802413…`, `f8d56518…` |
| répétition v2 normale (`repetition-jouet-v5/`) : journal, résumé | `472226ac…`, `3346f95f…` |
| répétition v2 repli (`repetition-jouet-repli-v3/`) : journal, résumé | `ce50cbb9…`, `e19c7c71…` |

## 8. Reste et points pour la mère

1. Contre-lecture courte du différentiel `dc4cab9d..8ae9fc44` (DF-01 à DF-04, repli garde d'abord, script de l'instance), puis
   `CODE-T07` au commit `8ae9fc44` (section 6) et contre-lecture du brouillon 3 de l'ordre.
2. Brouillon 21 : règle du repli (garde d'abord, nom daté, reprise couverte, relance), `CODE-T07` aux étapes A et B et sur tout
   `src/controle_ia/`, rejeu du contrôle 9 (jeu vidé : arrêt), mémoire de la notation, nom du journal du script des jeux.
3. DF-05 non fait (mineur) ; DF-07 porté à l'ordre.
4. `LIGNE_ESSAIS_T07` à mesurer dans l'environnement de l'instance (Python 3.11) ou à accepter de la session.
