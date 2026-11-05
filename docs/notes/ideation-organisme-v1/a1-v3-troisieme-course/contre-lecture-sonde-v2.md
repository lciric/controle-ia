# Contre-lecture du mode sonde de l'hôte durable d'A1-v3, v2

Je suis un contre-lecteur neuf. Je n'ai écrit aucune des pièces, ni la contre-lecture de la v1. J'ai travaillé le 4 novembre 2026,
de 12:38 à 12:45 UTC (`date -u`), en lecture seule : aucun réseau, aucune location, aucune clé, aucune dépense, aucun commit.

**Verdict : lançable après corrections.** Deux corrections majeures, toutes deux courtes :
- le contrôle à T0 + 60 min ne peut pas détruire une machine encore listée après son échéance ;
- la borne de 0,43 USD n'est pas mécanique quand la machine démarre tard.

Les corrections de la v1 sont faites dans le code, sauf m1 et m2 (partielles) et f1 (contredit l'additif). Trois défauts moyens
touchent la minuterie dans un vrai conteneur. J'en ai démontré un hors des essais du rédacteur.

## Empreintes vérifiées (compagnons, depuis le dossier de chaque fichier ; `HEAD` = `e86ec61d`)

| pièce | sha256 |
|---|---|
| `consigne-contre-lecture-sonde-v2.md` | OK (compagnon) |
| `src/controle_ia/sonde_hote_durable_a1_v3_v2.py` | `a514904f…` OK |
| `scripts/amorce_sonde_hote_durable_a1_v3_v2.sh` | `0a2e05ac…` OK |
| `tests/test_sonde_hote_durable_a1_v3_v2.py` | `359a7aa5…` OK |
| `rapport-redaction-v3-v1-additif-2.md` | `0eec292c…` OK |
| `essais-sonde-v2.txt` | `3c3f5a8c…` OK (égale à la section 4 de l'additif) |
| `contre-lecture-sonde-v1.md` | `07ba1356…` OK |

## 1. Points de la v1 : état dans le code (lignes du module v2, sauf mention)

| point | état | où |
|---|---|---|
| M1 minuterie | **corrigé** (réserves m-a à m-d) | `MINUTERIE` l. 111-130 ; minuterie lancée avant le clonage l. 143-145 ; conteneur gardé en vie l. 158 ; `fin` attrape `Exception` l. 529 ; `se_detruire` l. 548-575 |
| M2 `-y` | **corrigé** | l. 230, ligne pour l'état l. 306 ; essai l. 163-172 |
| M3 `VAST_API_KEY` | **corrigé** | exigée l. 184-185 ; transmise au seul `vastai` l. 195 ; masquée l. 186-192 ; passée dans `env -i` (additif, section 6) |
| m1 dépense | **partiel** | comptée depuis le départ du conteneur (l. 371-378) ; versement borné (l. 74, 586-587) ; mais le démarrage en 10 min au plus (l. 71) n'est tenu par rien (M-B) |
| m2 jamais démarrée | **partiel** | état écrit l. 286-296 ; signe de vie l. 481-490 ; `controler` l. 309-345 ; la branche « après l'échéance » ne joue pas à T0 + 60 (M-A) ; dépend toujours d'une session (limite d'usage, R-1481) |
| m3 réponse | **corrigé** | l. 233-250 ; marqueur l. 282-285 ; seconde location refusée l. 259-260 |
| m4 commande | **partiel** | `COMMIT_PRIVE`, sous-commande `offre` (l. 609-622), `mkdir … \|\| exit`, `&&` : faits ; contrôles mal placés (M-A) ; f-c |
| m5 clonage | **corrigé** (f-d) | l. 151-154 ; `fetch` partiel de `main` l. 421-422 ; versements orphelins l. 452-479 |
| m7 R5 | **corrigé pour la liste de la v1** | amorce jusqu'à `exec` (essai l. 348) ; destruction refusée (l. 487) ; `URLError` et `TimeoutExpired` (l. 462-470) ; espace (l. 163) ; réponses (l. 143-153) ; `DUREE_MAX_S` (l. 55, 444-445). Restent les trous m-c et m-d |
| f1 sorties | **partiel** | l. 204-206 : en cas d'échec, la sortie d'erreur est lue, et sa première ligne masquée est écrite (f-a) |
| f2 liste commune | **corrigé** | l. 76-77 ; amorce l. 16 ; essai l. 65 |
| f3 message | **corrigé** | l. 487, 509-510 |
| f4 branches | **corrigé** | l. 61-64, 406 |
| f5 mesures versées | **corrigé** | l. 80, 146, 154, 157, 492-501. Le journal de la minuterie n'est versé qu'avec sa ligne de départ (m-d) |
| f6 `--storage 30` | **corrigé** dans la commande | non vérifiable hors réseau sur 1.8.3 |
| f7 `GO_ID` | **corrigé** | l. 261-262 ; commande, section 6 |
| f8 étiquette | **corrigé** | minuterie l. 116-122 ; machine l. 553-558 ; pilote l. 326-328 ; instances protégées l. 67, 117, 228, 317, 544. Repli écrit sans contrôle de l'étiquette : f-b |

m6 : tranché par Lazar (R-1484) ; hors de ma liste.

## 2. Minuterie

- **Lancée en tout premier, sans Python, détachée.** Oui. Avant elle ne viennent que des affectations, la lecture ou l'écriture de
  l'échéance, puis `base64 -d` (l. 140-145). Seuls `bash`, `date`, `sleep`, `grep` et `curl` servent.
- **Sortie du processus principal.** La minuterie n'y survit **pas** dans un conteneur. À la mort du processus de numéro 1, le
  noyau tue tout l'espace de processus, `setsid` compris.
  - Démonstration : `unshare -pf` ; le fils `setsid` meurt, alors que le même fils survit hors d'un tel espace.
  - Le dessin compense ce défaut sur le chemin normal : le principal vit jusqu'à l'échéance + 10 min (l. 158).
  - Les essais du rédacteur tournent hors d'un espace de processus. Ils attendent la minuterie *après* la sortie du principal
    (essais l. 266-270), ce qu'un conteneur ne permettrait pas.
- **Reprise du conteneur.** L'échéance d'origine est bien gardée sur disque (l. 143).
  - Si la reprise a lieu après l'échéance + 10 min et sans amorce (clonage raté), le principal sort aussitôt : la minuterie est
    tuée avant son `DELETE` (m-b).
  - Démontré dans un espace de processus : le journal porte la seule ligne de départ, sans aucun `DELETE`.
  - La démonstration est dans `/tmp/claude-0/-home-user/4a4722d4-e39d-57bd-bde3-e6a99e2eecdf/scratchpad/cl-sonde-v2/demo/demo_reprise.py`.
- **Machine arrêtée.** Un arrêt tue la minuterie : le repli Python « versement non vérifié » (l. 569-572) ou le repli `PUT
  stopped` de la minuterie elle-même. Le commentaire de la l. 569, « la minuterie détruira à l'échéance », est faux (m-a).
- **`curl` absent.** Rien ne le vérifie. L'étiquette reste vide, puis le `DELETE` et le `PUT` rendent « HTTP » vide.
  - La minuterie l'écrit et sort, sans geste ni alarme.
  - L'image `python:3.13-bookworm` (bâtie sur `buildpack-deps`) devrait contenir `curl`, mais c'est à vérifier (m-c).
- **Écart déclaré (destruction quand l'étiquette est illisible).** Il est sûr : aucun chemin ne peut viser une autre instance.
  - La minuterie et la machine ne visent que `CONTAINER_ID`. Cette valeur est posée par Vast et absente du corps, contrôlée en
    chiffres, et les trois instances protégées sont exclues.
  - Le corps refuse les espaces et les guillemets, ce qui empêche toute injection d'un `-e`.
  - Le pilote ne vise que `new_contract`, après contrôle de l'étiquette et des instances protégées.

## 3. Borne de 0,43 USD

Elle n'est vraie que si le conteneur démarre dans les 10 min. On a alors 0,40 × (600 + 1200 + 1500 + 600) / 3600 = 0,433 USD, en
supposant qu'une instance « exited » ne facture plus le calcul (f-f).

- **Démarrage tardif (M-B).** La minuterie compte depuis le départ du conteneur, non depuis la création.
  - Exemple : le conteneur part à T0 + 35 min et pousse son signe de vie avant le contrôle de T0 + 40. La minuterie détruit alors
    à T0 + 80, et le conteneur sort à T0 + 90.
  - Cela fait environ 0,6 USD, au-dessus du plafond de 0,50 USD.
- **Machine jamais démarrée et pilote coupé par la limite d'usage.** Aucune borne mécanique : au plus prudent 0,40 USD/h, soit
  environ 9,6 USD par jour, jusqu'à une reprise.
- **Pilote vivant.** Le contrôle de T0 + 40 détruit la machine faute de signe de vie : borne d'environ 0,27 USD.

## 4. Secrets

- **Ce qui atteint la machine.**
  - `GH_TOKEN` par `--env` : visible dans les métadonnées de Vast et par `docker inspect` ; accepté pour la seule sonde (R-1484).
  - `CONTAINER_API_KEY`, posée par Vast. Elle ne passe que dans l'en-tête de `curl` et dans `ClientVast`.
  - Aucune clé de modèle : la liste est littérale (l. 165-168) et gardée trois fois.
  - `VAST_API_KEY` n'est passée qu'au sous-processus `vastai` du pilote.
- **Masquage.**
  - Journaux du pilote : `GH_TOKEN` et `VAST_API_KEY`.
  - Machine : `GH_TOKEN`, `CONTAINER_API_KEY` et `VAST_API_KEY`.
  - Contrôle des fuites avant le versement (`fuites`).
  - Aucun `set -x`. La minuterie jette les corps et les erreurs de `curl`.
- **Sorties de `vastai`.** En cas de succès, la sortie standard est lue, jamais affichée. En cas d'échec, la sortie d'erreur est
  lue, et la première ligne de sortie standard + erreur (160 caractères, masquée des deux seules clés du pilote) va dans le message
  de refus, donc au journal (f-a).

## 5. Essais rejoués (commande exacte de la consigne)

**120 passés** en 135,66 s, code 0. Le décompte par fichier (`--collect-only`) donne 52 + 19 + 49. La sortie versée porte 157 essais,
garde de calcul comprise (37) : 157 − 37 = 120, soit des comptes **égaux**. Ma sortie est dans
`/tmp/claude-0/-home-user/4a4722d4-e39d-57bd-bde3-e6a99e2eecdf/scratchpad/cl-sonde-v2/essais.txt`.

## 6. Commande de l'additif 2

Elle est juste sur les points demandés :
- `COMMIT_PRIVE` et `OFFRE` sont posés ;
- `env -i` passe `GO_ID`, `PATH`, `HOME`, `LANG`, `GH_TOKEN` et `VAST_API_KEY` ;
- `GO_ID=GO-2026-11-04-09` est en tête ;
- `-y` est dans le code ;
- `--verifier-seulement` passe avant la création, et les étapes sont enchaînées.

Elle est **incomplète** sur les contrôles. Celui de T0 + 60 min tombe avant la borne de T0 + 65 min du code (M-A). Les variables
`$D` et `$COMMIT_PRIVE` ne survivent pas d'un appel de shell à l'autre (f-c).

## Points (une ligne chacun)

- **M-A (majeure) — le contrôle de T0 + 60 ne peut pas détruire après l'échéance.** La branche « encore listée après l'échéance »
  exige T0 + 55 + 10 = **T0 + 65 min** (l. 289, 333). À T0 + 60, une machine listée avec signe de vie rend le code 0
  (« attendre »), et aucun contrôle ne suit. Correction : contrôler à T0 + 40 et T0 + 70 (ou plus tard), et traiter le code 0 avec
  instance listée comme « recontrôler ».
- **M-B (majeure) — démarrage en 10 min au plus « écrit », jamais tenu.** La borne de 0,43 USD est fausse dans un démarrage tardif
  (jusqu'à environ 0,6 USD, plus que le plafond de 0,50) et absente dans le cas « jamais démarrée, pilote coupé ». Correction : le
  pilote pose dans le corps une échéance absolue `ECHEANCE_UTC_S` (création + 600 + durée + 1500), et la minuterie prend le minimum
  des deux. Écrire aussi que le cas « jamais démarrée » reste borné par une session, non par la machine.
- **m-a (moyenne) — l'arrêt tue la minuterie.** Sur le repli « versement non vérifié » (l. 569-572) et sur le repli `PUT stopped`
  de la minuterie, l'instance reste arrêtée (stockage facturé) jusqu'à une session. Le commentaire de la l. 569 est faux.
  Correction : sonde factice, donc détruire même sans versement, ou laisser Python sortir sans geste et la minuterie détruire.
- **m-b (moyenne) — reprise après l'échéance + 10 min : la minuterie est tuée avant son `DELETE`.** Démontré dans un espace de
  processus. Correction : après la boucle de la l. 158, `wait` borné sur le numéro de la minuterie, ou destruction faite par le
  principal lui-même quand l'échéance est passée.
- **m-c (moyenne, R5) — `curl` non vérifié.** Absent, la minuterie ne fait rien, sans alarme. Correction : `command -v curl` au
  départ, installation avec `git`, sinon repli par `python3 -c` (urllib) ; alarme écrite ; essai avec un `PATH` sans `curl`.
- **m-d (moyenne) — la vraie sonde n'éprouve pas la minuterie.** Sur le chemin normal, Python détruit vers le départ + 23 min, et
  la minuterie ne tire jamais. Les essais tournent hors d'un espace de processus. La leçon de R-1477 (une garde s'éprouve par un
  tir réel) reste ouverte pour la vraie course. Proposition : un mode de sonde où Python verse sans geste et où la minuterie
  détruit, avec une marge raccourcie (environ 0,05 USD de plus), et des essais sous `unshare -pf`.
- **f-a (faible) — sortie d'erreur lue en cas d'échec.** La première ligne est écrite (l. 204-206), ce qui contredit la l. 207 et
  l'additif (sections 1 et 2, M3, f1). Seules deux clés sont masquées, pas celles des autres instances que `show instances` peut
  rendre. Correction : n'écrire que le code.
- **f-b (faible) — repli de la ligne d'état (l. 306).** `destroy … -y` sans contrôle de l'étiquette : renvoyer plutôt à
  `controler`.
- **f-c (faible) — commande.** `D` et `COMMIT_PRIVE` sont à réécrire en clair dans le contrôle ; `nice -n 10` manque au contrôle.
- **f-d (faible) — clonage.** `blob:none` suivi du `checkout` de tout l'arbre au commit télécharge toutes ses données (environ
  2,4 Go selon la v1), et ce `checkout` est hors du `timeout 600`. Un `sparse-checkout` de `scripts/` et `src/controle_ia/`
  suffirait.
- **f-e (faible) — crochets d'essai lus en production.** `RACINE_SONDE`, `API_VAST`, `SONDE_MARGE_S` et `SONDE_VIE_APRES_S`
  (l. 140-142) sont lus sans contrôle. Ils sont inertes, car absents du corps, mais un `MARGE` non numérique casserait le
  script.
- **f-f (faible, réserve) — « exited » sans calcul facturé.** C'est supposé (état constaté en R-1482, facturation non vérifiée ;
  R-1481 bornait prudemment au plein prix).
- **f-g (faible) — `--storage 30`.** Le sens sur `vastai` 1.8.3 n'est pas vérifiable hors réseau.
