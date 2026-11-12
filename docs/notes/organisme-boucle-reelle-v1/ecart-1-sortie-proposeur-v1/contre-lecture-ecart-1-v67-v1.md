# Contre-lecture (R2) — écart 1 de la course réelle de l'organisme, option 2 : code v67, configuration v8, texte v2

**Verdict : scellable après corrections.** Deux corrections de texte, courtes, sans effet sur le code, la configuration, les
blocs gelés ni les critères de lecture (liste bloquante, section 1). Le code v67, la garde 24, la configuration v8, les bornes
de dépense et les refus du lanceur tiennent tels quels ; rien à refaire de ce côté.

- **Contre-lecteur** : sous-agent neuf, Claude Fable 5.2 (`claude-fable-5-2`), session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv` ;
  n'a écrit aucun des fichiers lus. Le rédacteur et développeur est Claude Opus 5.5 : même famille, autre modèle.
- **Date** : 12 novembre 2026, fin à 13:30 UTC (`date -u`). Aucun appel payant, aucune machine, aucune clé lue, rien écrit
  dans `registres/`. Travail dans des arbres jetables, jamais dans le clone principal.
- **Objet** : branche `prep/organisme-v66-ecart1-sortie-v1`, tête `8c78bc5dae856b3bd357dbe5fdf87971813ab52e`, dossier
  `docs/notes/organisme-boucle-reelle-v1/ecart-1-sortie-proposeur-v1/` ; décisions R-2422, R-2423, R-2426 ; ligne
  GO-2026-11-12-06 de `registres/go.md` (`main`).

## 0. Pièces lues (empreintes recalculées)

| pièce | empreinte sha256 | constat |
|---|---|---|
| `ecart-1-brouillon-2.md` | `2a23fe121a11…` | égale à l'annonce |
| `preenregistrement-boucle-reelle-organisme-v1-v2-brouillon1.md` | `fbdb14d32a26…` | égale |
| `../preenregistrement-boucle-reelle-organisme-v1-v1.md` (texte scellé v1) | `46d7545b489a…` | égale |
| `configuration-v8/configuration-boucle-reelle-v8.json` | `eb6262890927…` | égale ; octets égaux à `exemples/configuration-boucle-reelle-v8.json` de l'arbre v67 |
| `configuration-v7/configuration-boucle-reelle-v7.json` | `e45f3a7199c5…` | égale |
| `../code-v66/configuration-v6/configuration-boucle-reelle-v6.json` | `4743ddbe4d29…` | égale |
| `code-v67/organisme-v67-contre-7e415cb.patch` | `195e4e63b480…` | égale ; appliqué sur `7e415cba`, il donne l'arbre de `ab53b7f4` à l'octet |
| `code-v67/organisme-v67-boucle-reelle-v1.bundle` | `8bfcd5936285…` | égale ; `git bundle verify` réussi |
| paquet v65 (`origin/prep/organisme-v65-v1`, `code-v65/organisme-v65-boucle-reelle-v2.bundle`) | `4660197e4ee5…` | égale |
| paquet v66 (`code-v66/organisme-v66-boucle-reelle-v1.bundle`) | `84ab119f0b3e…` | égale |
| rapport de la coupure (`origin/donnees/course-organisme-v66-poste-local-v1`, `course-v66/rapport-course-v66-poste-local-v2.md`) | `89b97faf2c7e…` | égale ; 46 714 jetons de sortie dont 46 711 de raisonnement, 1 552,967 s, code 5, garde 13, 0,481706 USD (l. 23-25, 75) |
| `verifications-v2/` (dix fichiers) | compagnons | 38 compagnons du dossier recalculés, 0 écart |

Reconstruction : clone neuf de `https://github.com/lciric/ideation-organism`, paquets v65, v66, v67 vérifiés et tirés dans
l'ordre : têtes `cef5ea60`, `7e415cba`, **`ab53b7f482df5149d9f672f40e04220dffb4173a`** ; `94bfd92` en est ancêtre ; **497
fichiers suivis** ; `git diff --name-status 7e415cba ab53b7f4` : cinq fichiers ajoutés, aucun modifié ni retiré.

Rejeux (Python 3.13 de l'environnement de travail, `POLE_ESSAI_BAC_REEL_NON_JOUE=1`, hors réseau payant) :

- Suite des dix fichiers de la section 12.3 du texte v2 : **408 passés, 5 sautés, 418 sous-essais, code 0** (394,6 s) ; les
  cinq sauts sont ceux de `verifications-v2/sortie-suite-v67-v1.txt` (vrai bac à sable non joué ici).
- Banc `essais/mutations_boucle_reelle_v67.py --processus 4` : **151 tuées pour la raison attendue sur 151, code 0**
  (banc v66 porté 38 + 26 + 69 = 133 ; neuves v67 18 sur 18).
- `verifications-v2/verifier-lanceur-v67-texte-v2-v1.py` rejoué sur mes copies (arbre v67 reconstruit, texte v2, texte v1,
  configurations v8, v7, v6, `registres/go.md` de `origin/main`, héritage `93dcf51715f7…`) : sortie **identique à l'octet** à
  `sortie-verifier-lanceur-v67-v1.txt`, bilan « tout tient ».

## 1. Liste bloquante (corrections exactes)

**B1 — l'en-tête du texte v2 ne peut pas être scellé tel quel.** `preenregistrement-boucle-reelle-organisme-v1-v2-brouillon1.md`,
l. 1 et l. 3 : le titre dit « (écart 1, brouillon) » et le statut « **brouillon du texte v2, non scellé, non contre-lu.** » ;
l. 10-11 : « Il devient le texte scellé […] après sa contre-lecture (R2) et une vérification courte du différentiel ». Scellé
à l'octet, le texte se dirait lui-même non contre-lu, et aucune ligne ne nommerait sa contre-lecture (la section 15, inchangée,
ne nomme que celles du v1). Correction :

- l. 1 : remplacer « v2 (écart 1, brouillon) » par « v2 (écart 1) ».
- l. 3 : remplacer « **Statut : brouillon du texte v2, non scellé, non contre-lu.** » par « **Statut : texte v2, candidat au
  scellement (R1) ; contre-lu (R2) par un sous-agent neuf, Claude Fable 5.2, verdict « scellable après corrections », rapport
  `docs/notes/organisme-boucle-reelle-v1/ecart-1-sortie-proposeur-v1/contre-lecture-ecart-1-v67-v1.md` (empreinte à son
  compagnon, à recopier ici) ; corrections B1 et B2 portées.** »
- l. 10-11 : remplacer « après sa contre-lecture (R2) et une vérification courte du différentiel v1 → v2 » par « si la
  vérification courte du différentiel entre le brouillon 1 (`fbdb14d3…`) et ce candidat le dit conforme ».

**B2 — la note de l'écart est citée sans empreinte (R6).** Même fichier, l. 82 (section « Écart 1 », puce « Décision ») :
`ecart-1-brouillon-2.md` est nommé sans empreinte, alors que les chiffres de dépense de la section (39,00 ; 32,30 ; 6,70 ;
1,35) n'ont pas d'autre source écrite (brouillon 2, section 5, qui renvoie au brouillon 1, sections 6 et 8). Correction :
après le chemin du brouillon 2, ajouter « (`2a23fe121a11…`, empreinte entière à son compagnon ; calcul de la dépense :
`ecart-1-brouillon-1.md`, `6e18fc335d4d…`, section 8) » — ou l'empreinte du brouillon suivant si la remarque N3 y est portée.

Rien d'autre ne bloque. Ces deux corrections ne touchent ni les trois blocs gelés, ni les sections 12.3, 12.4, 13 et 16 :
la vérification hors ligne du lanceur (section 0) reste valable ; il suffit de la rejouer sur le candidat.

## 2. Réponses aux six questions

### (1) Le différentiel v66 → v67 se limite-t-il au délai passé à l'adaptateur ? — Oui.

- Cinq fichiers neufs, 1 608 lignes ; aucun fichier v66 ni antérieur modifié (`git diff --name-status`).
- `pole/adaptateur_commande_v67.py`, l. 85-98 : `commandes_v67` est `commandes_v64` (`pole/adaptateur_commande_v64.py`,
  l. 157-169) à une différence près, l. 95 : `delai_s=float(f["delai_s"])` passé à `AdaptateurCommandeExterneV64` ; la garde
  24 est jouée d'abord (l. 87).
- `demonstrations/boucle_reelle_v67.py` contre `boucle_reelle_v66.py` (comparaison ligne à ligne) : en-tête ; import de
  `AC67` ; noms des blocs (`empreintes-du-code-v67`, `plan-gele-v67`, l. 104-105) et messages ; fermeture statique (l. 118-119 :
  lanceur v66 retiré, lanceur v67 et adaptateur v67 ajoutés) ; `verifier_configuration_v67` (l. 282-290) ; `roles_reels_v67`
  (l. 293-330) ; appels l. 510 et 518 ; manifeste (`lanceur`, l. 409 ; `delais_v67`, l. 529) ; préfixes des dossiers
  provisoires. `roles_reels_v67` comparée à `tour_ferme_v64.roles_reels` : seules différences, `AC67.commandes_v67` au lieu de
  `AC.commandes_v64`, `DelaiRefuse` ajouté au refus nommé, clé `commandes` ajoutée aux informations.
- **Dépense** : le budget d'appel ne va qu'aux proposeurs (`plafonds_session.proposeur`, `demonstrations/attaque_goodhart_v2.py`
  l. 212-230) ; l'expérimentateur et le vérificateur gardent leurs bornes gelées dans le code
  (`pole/tour_ferme_v64.py` l. 150-151 : 0,80 et le budget du lecteur par carte). Le code v67 ne touche aucune porte, aucun
  barème, aucune part.
- **Lecture** : `pole/lecture_boucle_reelle_v66.py` et `demonstrations/lire_boucle_reelle_v66.py` inchangés ; ils ne lisent que
  le relevé du cœur, pas le manifeste : les trois clés ajoutées au manifeste n'entrent dans aucun critère.
- Portée réelle, à savoir : le délai de 7 200 s vaut pour **toute** session Kimi (les 444 tours d'expérimentateur au pire
  cas compris), pas pour le seul proposeur. Effet sur la durée seulement ; aucun sur la dépense (bornes en jetons).

### (2) La garde 24 est-elle juste et éprouvée (R5), et refuse-t-elle bruyamment ? — Oui, avec deux angles morts sans effet sous la v8.

- Juste : `verifier_delais_v67` (l. 53-82) exige un délai d'adaptateur nombre JSON fini, > 0, ≤ 7 200 s (l. 61), l'option
  `--delai-s` une seule fois et suivie de sa valeur (l. 65), valeur en chaîne lue en réel fini > 0, marge de 30 s (l. 77).
- Éprouvée : cas sains (`essais/test_boucle_reelle_v67.py` l. 157-170, dont la borne exacte l. 161) et 19 artefacts
  (l. 172-207) ; délai suivi jusqu'à `Popen.communicate` et vraie commande locale tuée au délai de l'adaptateur (l. 313) ;
  mutations N01 à N12 et N17 tuées à mon rejeu. Deux contrôles redondants sans mutation (booléen, `isfinite`) : déclarés au
  brouillon 2, section 3 ; exact.
- Bruyante : `DelaiRefuse` nommé ; au lanceur, `ConfigurationRefusee`, code 2, avant la machine et avant toute porte
  (l. 282-290, 510 ; essai l. 400) ; dans les rôles, `TourRefuse` (l. 311-313). Aucun repli.
- **Angles morts (mes sondes, non bloquants)** : une commande qui porte `--delai-s 7150` **et**, en plus, `--delai 9999`
  (abréviation admise par `argparse`) ou `--delai-s=9999` est **admise** par la garde, qui lit 7 150 s, alors que la commande
  prendrait 9 999 s. Sans effet sur cette course : la configuration v8 ne porte ni l'une ni l'autre forme, et son empreinte
  est gelée au plan (toute autre configuration est refusée avant la garde 24). À fermer à la prochaine version du code
  (refuser tout élément de la commande qui commence par `--delai`, hors l'option exacte).

### (3) Le texte v2 ne change-t-il que ce que l'écart déclare ? — Oui ; critères de lecture inchangés.

Comparaison ligne à ligne du v1 scellé au brouillon du v2 : 26 blocs de différences, tous dans les lieux déclarés.

- En-tête ajouté (v2 l. 1-14) et section « Écart 1 » insérée (l. 73-106).
- Section 12.3 (v2 l. 655-722) : tête de l'arbre et chaîne des paquets, suite de dix fichiers, banc v67 (151), lanceur v67,
  délais lus au manifeste, options du relais Kimi (`--delai-amont-s 7200 --delai-silence-s 1800`), Argon inchangé.
- Section 12.4 (l. 729-741) : dossier `configuration-v8/`, lanceur v67, texte `…-v1-v2.md`, configuration v8, GO-2026-11-12-06.
- Section 13 : paragraphe du GO (l. 759-767) et ligne inscrite (l. 770), **égale à l'octet** à la ligne GO-2026-11-12-06 de
  `registres/go.md` de `origin/main`.
- Section 16 (l. 829-956) : noms des blocs ; une empreinte remplacée (`demonstrations/boucle_reelle_v67.py`, `d530d81c…`) et
  une ajoutée (`pole/adaptateur_commande_v67.py`, `a1b488b3…`), toutes deux égales aux fichiers de l'arbre ; `go` et
  `configuration_sha256` au plan ; rien d'autre (plafonds, parts, montant, durée, monde, jeu planté, héritage inchangés).
- **Aucune différence** entre les lignes 59 et 606 du v1 (documents qui font foi, sections 0 à 12.2 : hypothèse, dessin,
  prédictions, métriques, seuils, plan d'analyse, critères de lecture gelés, audit de symétrie, liste d'arrêt), ni dans les
  sections 14 et 15. Les 99 empreintes du bloc sont égales au code (vérification hors ligne rejouée).

### (4) Les bornes de dépense tiennent-elles avec un appel de 7 200 s ? — Oui.

- La dépense est bornée en jetons, jamais en durée : `commande_kimi_v6.py` l. 229-233 et 315-335, `max_tokens` =
  min(131 072, ce que paie le plafond de session) ; pire cas réservé au registre avant l'envoi (l. 338), réglé au coût lu ou
  au pire cas (code 6 au délai, l. 376-382). Le relais Kimi réserve le même pire cas sous verrou avant de partir et compte au
  pire cas tout délai dépassé ou flux coupé (`relais_kimi_v3.py`, `d54ed2bce54f…`, l. 81-89, 400-407, 537, 570-595).
- Arithmétique refaite : Kimi 37 × 0,80 + 2 × 1,35 = **32,30 ≤ 33** ; Argon 37 × 0,10 + 2 × 1,50 = **6,70 ≤ 7** ; modèles
  39,00 ≤ 40. **Plus dur que l'annonce** : au plafond de session absolu (1,50 par appel du proposeur, quel que soit le corps),
  Kimi vaut 37 × 0,80 + 2 × 1,50 = 32,60 ≤ 33. Garde C13 avant l'étage de génération 2, au plafond absolu : Kimi reste
  33 − 16,60 = 16,40 ≥ 16,00 ; Argon reste 7 − 4,70 = 2,30 ≥ 2,00.
- Ordre des délais d'un appel Kimi : commande 7 150 s < adaptateur 7 200 s = relais 7 200 s. Le client ne reçoit rien du
  relais avant la fin (flux refusé au client) : le délai de la commande, un délai de lecture de la connexion, vaut bien durée
  totale. Si la commande sort au délai, le relais peut finir l'appel à l'amont : dépense réelle ≤ pire cas déjà compté.
- Silence de 1 800 s : il ne change aucune borne de dépense ; un silence plus long coupe l'appel, compté au pire cas (504).
  L'ouverture de la connexion à l'amont prend le même délai (l. 392-397) : une ouverture pendue attend au plus 1 800 s.
- Machine : remarque N3.

### (5) Le lanceur v67 refuse-t-il les artefacts ? — Oui (rejoué).

Texte v1 : `PreenregistrementRefuse` (bloc `empreintes-du-code-v67` absent), code 2. Configurations v7 et v6 :
`ConfigurationRefusee` (empreinte ≠ `eb6262890927…`), code 2. GO-2026-11-10-11 : `GoAbsent` (autre que celui du texte), code 2.
Cas sain : arrêt à la garde 22 seulement (`bwrap` simulé absent), donc après le texte, le monde, la configuration, le GO, la
garde 24 et la garde 17. Les essais `BlocsNonInterchangeables` (texte v66 refusé par la v67 et l'inverse) passent.

### (6) Le poste a-t-il tout pour reconstruire et lancer ? — Oui, à trois précisions près pour la consigne v4.

- Chaîne complète et vérifiée : clone, paquets v65, v66, v67, tête `ab53b7f4`, 497 fichiers. Le relais Kimi v3 et la
  configuration v6 sont sur `main` ; l'héritage de départ et son compagnon sont dans `code-v66/blocs-v66/`
  (`93dcf51715f7…`, égale à `heritage_depart_sha256` du plan), pas dans `configuration-v8/`, comme sous le v1.
- Options du relais : écrites au texte (l. 687-692 et 710), avec la ligne « relais prêt » à relever (« délai 7200.0 s »,
  « silence 1800.0 s ») ; conforme au format du relais (l. 656-659).
- Précisions : remarques N4 et N5.

## 3. Remarques non bloquantes

- **N1** — garde 24 : deux angles morts (question 2), sans effet sous la configuration v8 gelée.
- **N2** — texte v2, section 13, l. 754-757 : le paragraphe du devis garde « 35,30 (chaîne cassée) », chiffre du devis sous la
  v6 ; la section « Écart 1 » (l. 103-105) donne 39,00 et dit « v1 : 35,30 ». Cohérent avec l'annonce (« dans la section 13,
  le paragraphe du GO et la ligne ») ; une incise « (sous la configuration v8 : 39,00, section Écart 1) » lèverait le doute.
- **N3** — `ecart-1-brouillon-2.md`, section 5 : « ≈ 0,06 EUR par heure » ne suit pas le rapport de course, qui donne
  ≈ 0,059 EUR pour 45 min 9 s (l. 100), soit ≈ 0,078 EUR par heure (≈ 0,09 USD). Le plafond de 5 USD de la machine, tenu par
  aucun code, est atteint vers **54 heures**, avant la garde de 72 heures (le devis dit déjà ≈ 50 heures à 0,10 USD,
  `devis-boucle-reelle-organisme-v1.md` l. 82). Hérité du v1, mais l'écart allonge les appels : la consigne v4 doit faire
  arrêter la machine par son identifiant avant 50 heures. Le texte v2 ne porte aucun prix horaire.
- **N4** — le commit `94bfd92` n'est pas sur la branche par défaut du dépôt public (tête `ef4e202`) ; il est sur
  `prep/organisme-v65-boucle-reelle` et `claude/new-session-7qxayx`. Un clone complet le contient (mon rejeu) ; un clone
  `--single-branch` ou `--depth` échouerait au paquet v65. À dire dans la consigne v4.
- **N5** — les pièces sont sur trois références : paquet v65 sur `prep/organisme-v65-v1` seulement ; paquet v67,
  configuration v8 et texte v2 sur `prep/organisme-v66-ecart1-sortie-v1` seulement (absents de `main` à `3c35d998`).
  La consigne v4 doit nommer ces branches, ou les pièces rejoindre `main`.
- **N6** — en-tête du v2, l. 6-9 : la règle « tout passage qui nomme le code v66 […] se lit code v67 » est large, alors que le
  cœur, la lecture et le lecteur du registre des GO restent v66 ; la section « Écart 1 » (l. 91-92) le dit sans ambiguïté et
  prime. Aucune correction exigée.
- **N7** — réserves du brouillon 2, section 6, confirmées : débit de Kimi mesuré une fois (46 714 / 1 553 s ≈ 30,1 jetons
  par seconde ; 131 072 jetons ≈ 73 minutes) ; délai du relais hors de vue de la garde 24 ; aucun débit d'Argon mesuré.

## 4. Ce que je n'ai pas fait

Vrai bac à sable (`bwrap`) non joué ici : cinq essais sautés, à jouer sur la machine (section 12.3, points 1 et 3).
Aucun appel à un modèle, donc aucun constat sur le débit réel, le flux de l'amont ni les prix. Je n'ai lu aucun `diag/`,
`runs/`, ni rien des dossiers tenus à l'écart.
