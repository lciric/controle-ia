# Rapport de rédaction — A1-v3, troisième course sur hôte durable : texte v3 (brouillon 1) et lanceur durable, v1

Rédacteur-développeur neuf, 4 novembre 2026, de 07:53 à 08:30 UTC (heures relevées par `date -u`). Consigne
`consigne-redacteur-a1-v3-v3-hote-durable-v1.md`, sha256 `0ebbf927d026c26395545bbd3a717690f9d0d8fd570077f2d59ab13c757b52fb`
(vérifiée avant lecture). Je n'ai écrit ni les textes v1 et v2, ni leurs contre-lectures, ni le code gelé, ni les ordres des
courses. Aucun commit, aucun `.sha256`, aucun fichier existant modifié, rien sous `donnees/` ni `/home/claude/coffre-*`, aucune
sortie des courses lue, aucune location, aucun appel de modèle, aucune clé lue ni affichée, aucune dépense, rien poussé.

**Verdict.** Le brouillon 1 de la v3 et le lanceur durable sont écrits. Le lanceur gelé accepte le bloc du plan (seule la clé
`go` change). Il refuse le texte tant que restent ses deux marqueurs. 49 essais jouets passent. Trois choses bloquent le
scellement : l'audit A9 de la seconde course (non écrit), la ligne de GO-2026-11-04-06 à recopier sur `canal/conv-audit-n04`, et une
décision de Lazar sur le coût de la machine, qui peut au pire faire dépasser le montant du GO.

## 1. Fichiers (sha256 à la remise, 08:23 UTC)

| fichier | sha256 |
|---|---|
| `docs/notes/ideation-organisme-v1/a1-v3-troisieme-course/preenregistrement-attaque-goodhart-v3-v3-brouillon1.md` (2 147 lignes) | `6e65136aa23c7aae8b64bb142a5aa07a81811720b53e96ea5a6e1c57d0f7b78e` |
| `src/controle_ia/hote_durable_a1_v3.py` (neuf, 869 lignes, bibliothèque standard seule) | `5b853fde8987a472a191f769415068ecc15f1da8a042767bba4229dd5c29e0b1` |
| `scripts/amorce_hote_durable_a1_v3_v1.sh` (neuf) | `962bf6cb6542574cdaeba2bfa6075c1b914199c35fff7cd9df23fa812fc2d41b` |
| `tests/test_hote_durable_a1_v3.py` (neuf, 49 essais) | `b4a14beee5ad24e20f1305e7c93255e8a929c2f9ecb6a7ce5153ef77b40f9a88` |
| bloc-notes `…/scratchpad/v3b1/assembler_v3b1.py` | `e3156f4567b468c994b1b2640718d8fa37ef7d5bdd650f8435895e3b9e0062ff` |
| bloc-notes `…/scratchpad/v3b1/epreuve_v3b1.py` | `5f2e7ad2c5ade6cdb34247553d2e7e2fe48fd1a99a6cb0991277170c34fc40e2` |
| bloc-notes `…/sorties/epreuve-v3b1.json` | `5896c9df46cb1ace53a54e4a94a4064dc03c0bb26c50f577eb05f7b8d8ac0348` |
| bloc-notes `…/sorties/diff-v2-vers-v3-brouillon1.txt` | `111f64337c6723d9038b4918e4b584e005114fe9a8ac6b328b4e4caccf28c198` |
| bloc-notes `…/sorties/essais-hote-durable.txt` | `91497eee7e0156f1a2a189e5cd043ffdbc872362988a51ed89e49d0c8d521d90` |

Le bloc-notes est `/tmp/claude-0/-home-user/4a4722d4-e39d-57bd-bde3-e6a99e2eecdf/scratchpad/v3b1/`. Il n'est pas durable : le
contre-lecteur refait la différence par `diff -u` de la v2 scellée vers le brouillon.

Le directeur a committé un instantané du module (`a364e947`) pendant que je l'écrivais. Cet instantané est intermédiaire. Le rendu
est le fichier sur disque, avec l'empreinte ci-dessus.

## 2. Ce qui change de la v2 à la v3

La table « avant → après ; raison » est la section 0.7 du brouillon : 21 lignes. Elle a été appliquée par 25 remplacements, chaque
ancre présente une seule fois (`assembler_v3b1.py`). Le différentiel retire 18 lignes de la v2, toutes nommées par la section 0.7 :
titre, graine, renvoi « un scellement, une course », GO, dossier de sortie, commande exacte, ligne `go:`, notes du bloc, section 11,
section 13 (points 3 et 9), titre et n° 3 de la section 14. Tout le reste est ajouté. Voici l'essentiel :
- **Section 0.5 bis** (neuve) : faits de la seconde course (rapport de la fille `b7231983…` et additif 1 `a3ec41f6…`). Elle
  contient aussi la cause : limite d'usage de la session, puis reprise du conteneur, donc lanceur arrêté hors de ses codes. On y
  trouve encore la dépense de 48,49583 USD, l'état scellé `fd66feb7…` non lu, la règle de la section 8, GO-2026-11-04-06 (ligne 244
  de `main`), l'hôte durable, la lecture des trois courses et l'absence de relance de la v1 ou de la v2.
- **Graine neuve** : l'empreinte du texte v3. Les cartes de la seconde course ne sont pas rejouées.
- **Section 8, « Troisième course (v3) »** : l'hôte durable et sa liste d'arrêt (création, préparation, garde sans session,
  plafonds de la machine, fin propre, destruction par identifiant, reprise du conteneur). Elle dit aussi ce que deviennent les
  points (1) à (4) de la v2.
- **Section 4** : GO, source du registre, chemins de l'hôte et commande exacte (seuls l'hôte, les chemins, le GO et le texte
  changent). **Section 12** : nouvelle puce sur le coût de la machine. **Section 13** : point 7 quater, et la règle de lecture
  ajoutée aux points 3 et 9.
- **Deux marqueurs** : `AUDIT_A9_SECONDE` et `COMMIT_LANCEUR_DURABLE` (annexe B).

Inchangés, vérifiés par programme : le bloc `empreintes-du-code` (égal caractère pour caractère), le bloc `plan-gele` hors de
`go:`, le devis, les hypothèses, les prédictions, les critères, les audits et la configuration.

## 3. Essais

Toutes les commandes ont tourné sous `timeout 900 nice -n 10`.

- **Lanceur gelé** (`epreuve_v3b1.py` ; arbre `9776ed0` extrait par `git archive` ; compagnon simulé en mémoire) :
  - `lire_plan` accepte le bloc ; seule la clé `go` diffère de la v2 ; le devis est égal.
  - `lire_preenregistrement` refuse le texte sans compagnon (« non scellé »), puis avec ses marqueurs (« marqueur(s) non
    rempli(s) »).
  - Marqueurs remplis par des valeurs factices, le texte est accepté : 73 empreintes vérifiées, entropie égale à l'empreinte et
    au moins 2⁶⁴, plan égal.
  - Une empreinte altérée dans le bloc est refusée (« code différent du code gelé »).
  - **GO** : la garde de `main` accepte GO-2026-11-04-06 sur le registre de `main`. Le lecteur gelé refuse ce même registre
    (« GO-2026-10-24-07 en double »). Il accepte la ligne seule à 400 USD, échéance 2026-11-18.
- **Lanceur durable, mode jouet** : 49 essais passés en 35 s, plus les 37 de `tests/test_garde_calcul.py`. Le monde jouet
  comprend :
  - un dépôt privé nu à quatre branches, avec la vraie garde de `main` ;
  - un dépôt public à deux commits ;
  - un relais factice qui sert `/relais/etat` ;
  - un lanceur factice qui refuse toute variable de clé dans son environnement ;
  - un Vast simulé par fichier.

  Chaque garde est éprouvée sur un cas sain et sur un artefact :

  | garde | cas sain | artefacts |
  |---|---|---|
  | GO | ligne factice ; registre réel de `main` avec ses 17 doublons, extension admise | absent ; autre GO ; autre type ; autre auteur ; avant ou après la validité ; 399 USD ; « ≈ » ; révoqué ; doublon sans « extension » ; extension à 450 USD |
  | offre | sans carte, 0,12 USD/h | carte ; prix 0,41, booléen ou nul ; mémoire ; fiabilité ; offre absente ou en double |
  | création par l'outil `vastai` | réponse lue | valeurs des secrets masquées dans l'erreur ; valeur à espace refusée ; la vérification seule ne crée rien ; secrets absents du journal et du fichier de Vast |
  | inventaire | champs filtrés | `extra_env` jamais montré |
  | machine, cas sain | versée, chaque empreinte de la liste égale au fichier versé, aucun secret, détruite | — |
  | fin propre | code 3 du lanceur : versée, détruite | — |
  | plafonds de la machine | — | 80 h ramenées à 1 s, puis dépense : course arrêtée par son identifiant, versée, détruite |
  | reprise du conteneur | état déjà « versé » : destruction seule | aucun lanceur relancé, branche « interrompue » |
  | refus avant la course | — | texte faux ; commit hors de la lignée du code gelé ; pièce fausse ; registre à doublon ou sans la ligne ; `--verifier-seulement` en code 2 ; GO sur la machine ; port pris. Pour chacun : rien ne part, branche « refus », détruite |
  | relais | mort une fois, puis relancé | — |
  | fuite de la clé dans un journal | — | rien versé, machine arrêtée et non détruite |
  | branche déjà présente | — | rien écrasé, machine arrêtée |
  | identifiant illisible | — | aucun geste |
  | amorce | — | variable absente ou autre GO : code 2 |

- **Pièces gelées**, lues dans des clones partiels du bloc-notes : la commande d'Argon `221df610…`, le registre de dépense
  `8ba92066…`, le collisionneur `c9725f02…` et la configuration `e5306c47…` sont égaux aux empreintes du lanceur durable.
- **Ce qui n'a pas été éprouvé** : rien n'a tourné sur Vast. Ne sont pas éprouvés la recherche d'offres sans carte, la création par
  `vastai`, l'image, l'installation de numpy, la clé d'instance `CONTAINER_API_KEY` pour la destruction, ni le relais réel. Le
  mode sonde (course factice sur une vraie machine) recommandé en section 13 n'est pas codé.

## 4. Devis

- **Argon** : 400 USD de plafond, inchangé. La seconde course a coûté 48,50 USD pour 620 appels en 1 h 43, soit environ
  0,078 USD et 10 s par appel. À ce taux :

  | appels | cas | dépense |
  |---|---|---|
  | ≈ 1 054 | attendu aux taux d'A1 | ≈ 82 USD |
  | 2 112 | attendu haut du code | ≈ 165 USD |
  | 3 072 | maximum | ≈ 240 USD |

  Le devis du texte gelé (0,062 USD par appel, 65 à 190 USD) reste celui du plan.
- **Temps** : environ 4,6 h attendues (1 054 appels à 10 s, plus 1,65 h de rejeux). Environ 7,5 h à l'attendu haut du code à
  10 s, 25 h à 40 s. 35,8 h au pire. Garde de 72 h du lanceur ; la machine se coupe à 80 h.
- **Machine** : 0,40 USD/h au plus. Attendu de 0,5 à 10 USD (4,6 à 26 h à 0,10 à 0,40 USD/h). Plafond 32 USD.
- **Total attendu** : environ 85 à 175 USD. Au pire, 400 USD d'appels plus 32 USD de machine dépassent le montant du GO.
  **Décision de Lazar demandée** : extension, GO à part pour la machine, ou plafond plus bas avec un GO au même montant.

## 5. Dix points pour un contre-lecteur neuf

1. **Règle d'admission.** La troisième course exige une cause d'infrastructure établie par un audit A9 de la seconde course.
   Cet audit n'existe pas : il est porté comme marqueur. Est-ce suffisant, et l'audit peut-il se faire sans lire de réponses ?
2. **Le delta, et rien d'autre.** Les 18 lignes retirées et les ajouts correspondent-ils exactement à la section 0.7 ? Les blocs du
  code et du plan, le devis, les critères et les audits sont-ils intacts ?
3. **Registre des GO.** La copie se prend sur `canal/conv-audit-n04` à un commit qui porte la ligne recopiée : à faire par le
   directeur, avec une décision du type R-1340. `main` est refusé (17 doublons, dont l'extension de GO-2026-11-04-04). Le double
   contrôle (garde de `main`, puis lecteur gelé) est-il juste ?
4. **Montant.** Le lanceur durable exige 400 USD exactement sur la ligne et sur chaque extension. Écart possible avec le coût de
   la machine (section 4 ci-dessus).
5. **Plafonds de la machine** (80 h, 32 USD). Ce sont une nouvelle cause d'arrêt, placée après la garde de 72 h. Est-ce bien
   « jamais une coupe de la mesure », et bien qualifié comme arrêt d'infrastructure ?
6. **Secrets.** La clé passe par `--env` de `vastai` (forme des amorces antérieures). Elle reste lisible dans les métadonnées de la
   machine chez Vast et dans `/proc` sur la machine. Le loueur de la machine est un tiers. Faut-il une clé d'Argon dédiée, révoquée
   après la course ?
7. **Destruction.** Elle passe par `CONTAINER_ID` et `CONTAINER_API_KEY`, que Vast pose, par l'interface REST : non éprouvé. Si
   c'est refusé, la machine s'arrête ; si l'arrêt est refusé, l'inventaire de la routine R14 prend le relais. Faut-il une sonde
   avant la course ?
8. **Fin propre et reprise.** Le code de sortie est écrit par le parent. La liste est faite avant la copie, sans écriture au
   journal entre les deux. Rien n'est versé si un secret est trouvé. Branche neuve, poussée vérifiée par `ls-remote`. Une reprise
   ne relance jamais rien, y compris quand l'état était déjà « versé ».
9. **Fidélité au plan.** La commande que lance le module (`cmd_course`) est-elle exactement la commande exacte de la section 4 ?
   L'environnement de la course est sans clé ; le relais est lancé sans coquille, avec un identifiant de processus réel.
   `/usr/bin/python3` peut être le Python 3.11 de Debian pour la commande d'Argon (bibliothèque standard seule) ; Python 3.13 et
   numpy 2.5.3 servent pour l'orchestrateur.
10. **« Argon seul »** : la vérification se fait côté fille, avant la location. Sur la machine, seul le port est vérifié ; le quota
    de la clé reste commun avec les autres usages d'Argon.

## 6. Commande exacte pour la fille

À faire après le scellement de la v3, le commit du lanceur durable sur `main`, la ligne recopiée sur `canal/conv-audit-n04` et la
décision sur le montant. `COMMIT_PRIVE`, `COMMIT_PUBLIC`, `SHA_TEXTE` et `COMMIT_REGISTRE` sont des hash complets donnés par le
directeur. `OFFRE` est l'identifiant choisi dans `offres.json`. Le lanceur durable fait les mêmes contrôles que la garde de `main`
(`decider` de `.claude/hooks/garde_calcul.py`).

```
D=/home/user/hors-clone-a1-v3-troisieme-v1; mkdir "$D"            # neuf (R12)
cd /home/user/controle-ia-travail && git fetch -q origin main canal/conv-audit-n04
git show origin/main:registres/go.md > "$D/registre-go-main.md"
git show origin/main:.claude/hooks/garde_calcul.py > "$D/garde_calcul_main.py"
git show "$COMMIT_PRIVE":src/controle_ia/hote_durable_a1_v3.py > "$D/hote_durable_a1_v3.py"
# Argon seul : aucune autre utilisation en cours ni prévue (identifiants, heures), écrit à la main dans $D/journal-location-a1-v3-troisieme-v1.log
timeout 300 vastai search offers 'num_gpus=0 rentable=true verified=true reliability>=0.98 cpu_cores_effective>=4 cpu_ram>=8 disk_space>=30 dph_total<=0.40' -o dph_total --raw > "$D/offres.json"
for V in "--verifier-seulement" ""; do
  CLE_ARGON="$GEMINI_API_KEY_2" GH_TOKEN="$CONTROLE_IA_GITHUB_TOKEN" GO_ID=GO-2026-11-04-06 timeout 900 nice -n 10 \
    python3 -I -B "$D/hote_durable_a1_v3.py" louer --go GO-2026-11-04-06 \
      --registre-main "$D/registre-go-main.md" --garde-main "$D/garde_calcul_main.py" \
      --offres "$D/offres.json" --offre "$OFFRE" --commit-prive "$COMMIT_PRIVE" --commit-public "$COMMIT_PUBLIC" \
      --sha-texte "$SHA_TEXTE" --commit-registre "$COMMIT_REGISTRE" \
      --journal-local "$D/journal-location-a1-v3-troisieme-v1.log" $V || break
done
```

La boucle fait d'abord la vérification seule, puis la location ; elle s'arrête au premier refus (code 2). Ensuite, la session n'a
plus de rôle : identifiant dans `$D/journal-location-a1-v3-troisieme-v1.log.identifiant`, inventaire filtré par
`python3 -I -B "$D/hote_durable_a1_v3.py" inventaire`. Le résultat arrive sur `donnees/attaque-goodhart-v3-a1v3-troisieme-v1`. Il
arrive sur `…-refus-v1` si une garde a refusé avant la course, et sur `…-interrompue-v1` si le conteneur a été repris. Personne ne
lit rien avant le versement.

## 7. Trois risques principaux

1. **Vast n'est pas éprouvé.** Rien ne garantit des offres sans carte, la création, la clé d'instance pour la destruction, ni
   l'image. Remède : une sonde de quelques centimes avant la course, à coder (mode course factice).
2. **La clé d'Argon est confiée à un tiers.** Elle est visible dans les métadonnées de Vast et sur la machine louée. Remède : une
   clé dédiée, plafonnée, révoquée après la course.
3. **Le scellement est bloqué par trois choses** : l'audit A9 de la seconde course (marqueur), le registre accepté par le lecteur
   gelé (ligne à recopier sur `canal/conv-audit-n04`), et le dépassement possible de 32 USD au-delà du GO (décision de Lazar).
