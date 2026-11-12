# Contre-lecture R2 n° 4 du texte v3 d'A1-v3 (brouillon 2) et du lanceur durable v2 — courte, sur le delta

Contre-lecteur neuf : il n'a écrit ni le texte v2, ni le texte v3, ni le lanceur, ni les sondes, ni une contre-lecture
précédente. 5 novembre 2026, de 06:55 à 07:20 UTC (heures relevées par `date -u`). Consigne :
`consigne-contre-lecture-n4-texte-v3-v1.md` (sha256 `d1322529…`, compagnon vérifié). Interdits tenus : aucun commit, aucun
`.sha256`, aucun fichier existant modifié, rien sous `donnees/` ni `/home/claude/coffre-*`, aucun réseau, aucune location, aucune
clé lue, aucune dépense ; commandes sous `timeout 600 nice -n 10`.

**Verdict : scellable après couples.**
Aucun bloquant dans le texte : le delta v2 → v3 ne touche que ce que la section 0.7 et l'en-tête déclarent ; hypothèses,
prédictions, métriques, critères gelés et audits sont inchangés. Neuf couples sont à appliquer (`couples-contre-lecture-n4-v1.json`) : deux passages périmés disent encore « décision de Lazar demandée avant le scellement », et le risque HTTP 402 est mal décrit. Il faut aussi deux vérifications sans location avant le scellement (Python de `/usr/bin/python3` sur l'image ; versement et jeton), car le commit du lanceur s'écrit dans le texte au scellement.

## Pièces vérifiées

- Texte v2 scellé : **absent** de `prereg/` du dépôt privé (chemin de la consigne) ; trouvé, par empreinte (R11), dans le dépôt de
  l'organisme `/home/user/ideation-organism/orchestrator/prereg/preenregistrement-attaque-goodhart-v3-v2.md` : `2a29f593…`,
  compagnon égal.
- Brouillon 2 `86ad379b…` ; brouillon 1 `6e65136a…` (compagnon égal) ; rejoué dans le bloc-notes : brouillon 1 + les dix couples
  par le script du rédacteur = brouillon 2 **à l'octet**.
- Rapport v2 `569a2371…` ; lanceur v2 `b8287d52…`, amorce v2 `33e87f45…`, essais v2 `06deeed7…` ; lanceur v1 `5b853fde…` et sonde
  v10 `37b70a06…` (compagnons égaux) ; tous les compagnons du dossier de la troisième course égaux.
- Essais v2 rejoués : **82 passés** en 85 s (Python 3.13.18 du `.venv`).

## Points (gravité : bloquant / à corriger / note)

**Question 1 — delta v2 → v3**
1. Note — 24 morceaux de différence, tous dans des sections que nomme la section 0.7 (points 1 à 22) : en-tête, 0.4, 0.5 bis, 0.7, section 4, `go:` du bloc `plan-gele`, sections 8, 9, 11, 12, 13, 14, annexe B, empreintes. Aucun dans les sections 1, 2, 3, 5, 6 et 7 : hypothèses, prédictions, métriques, critères gelés et audits sont inchangés.
2. À corriger (couples 4 et 5) — sections 12 et 13, point 3 : la machine y est encore « sous le même GO » (GO-2026-11-04-06), au plus 32 USD, avec « décision de Lazar demandée avant le scellement ». Or la décision est prise : GO à part pour la machine (GO-2026-11-05-03 ; GO-2026-11-05-04). Scellé tel quel, le texte poserait une condition de scellement non remplie. La borne réelle est 32,57 USD.
3. À corriger (couple 8) — section 4, registre de la troisième course : « décision du directeur à prendre avant le scellement ». La copie est faite : commit `0aa04b5c` du 4 novembre à 08:27 UTC sur `canal/conv-audit-n04`.
4. Note (couple 6) — section 0.5 bis : la phrase « le lanceur durable, qui ne connaît que ce texte et GO-2026-11-04-06 » oublie GO-2026-11-05-03, que la v2 lit pour la machine.
5. Note (couple 7) — section 13, point 7 quater : la sonde d'hôte « sous le même GO » relève désormais de GO-2026-11-05-03, car GO-2026-11-04-06 ne porte plus que les appels à Argon.
6. Note — le titre dit encore « version 3, brouillon 1 ». C'est la convention de la v2, scellée sous le titre « version 2, brouillon 1 » : aucun couple.

**Question 2 — le lanceur v2 applique-t-il le texte ?**
7. Note — oui pour l'essentiel :
   - location à une carte sous `GO_ID=GO-2026-11-05-03`, montant exact de 35 USD ;
   - course sous GO-2026-11-04-06 (400 USD), revérifiée sur la machine ;
   - préparation, garde, plafonds de 80 h et de 32 USD, fin propre, secrets, versement « partie de `main` » refusé si la branche existe ;
   - destruction si la poussée est vérifiée, arrêt sinon ; reprise sans relance.
8. À corriger (couple 9) — le lanceur ajoute une règle que le texte ignore. La session lance `controler` à T0 + 40 min ; si la branche de signe de vie `…-troisieme-signe-de-vie-v1` manque à T0 + 30 min, `controler` détruit la machine. Le point 7 quater dit au contraire « puis plus rien de la session ». Le couple 9 déclare cette règle ; la correction de code C2 en ferme le cas limite.
9. À corriger (code C2) — la poussée du signe de vie peut échouer (« son échec est écrit, la préparation continue »). La course part alors quand même, et `controler` détruit à T0 + 40 min une course en marche : course perdue, appels déjà payés. Il faut refuser le départ sans signe de vie vérifié, avec un essai sur un cas sain et un sur un artefact.
10. Note (R5) — chaque garde neuve a son cas sain et son artefact (82 essais passés). Deux trous :
    - les refus d'installation de `git` et de numpy ne sont jamais essayés (`SAUTER_INSTALLATION=1`) ;
    - la mort de l'hôte en pleine course n'est pas essayée : la course continue orpheline, rien n'est versé, puis la minuterie détruit la machine et ses données à l'échéance (« fin brutale acceptée »).

**Question 3 — ce qui peut faire perdre la course ou l'argent**
11. Note — borne :
    - calcul : 0,40 × 293 100 s ÷ 3 600 = **32,57 USD ≤ 35 USD** ;
    - rien n'est encore imputé sous GO-2026-11-04-09 ni sous GO-2026-11-05-03 (`registres/depenses.md`) : les sondes v9 et v10 sont sous GO-2026-11-05-01 (≤ 0,08 USD) ;
    - la borne ignore la bande passante (`inet_up_cost`, `inet_down_cost`), qu'aucune offre ne filtre : quelques centimes attendus.
12. Note — destruction sur refus de l'amorce : bonne (code 2, ou amorce absente du clone, puis plus rien, même à une reprise ; essais passés). Tout autre code de sortie attend l'échéance (au plus 32,57 USD), sauf si `controler` voit l'absence de signe de vie.
13. Note — boucle de redémarrage : peu à craindre ici. `python:3.13-bookworm` (bâtie sur `buildpack-deps:bookworm`) porte `curl`, `git`, `setsid`, `timeout` et `base64`. La minuterie a un repli par `python3`, et une reprise relit l'échéance sur le disque.
14. Note — numpy 2.5.3 existe (c'est celle du Python 3.13.18 système de ce conteneur). Son installation par `pip` sur Vast n'a jamais tourné ; un échec donne le code 2, donc une destruction immédiate, pour quelques centimes.
15. **À corriger avant le scellement (vérifier d'abord)** — `/usr/bin/python3` sur `python:3.13-bookworm` est très probablement le Python 3.11 de Debian, tiré par `mercurial` de l'image de base. L'amorce ne crée le lien que s'il manque.
    - Ce qui tournerait dessus : le relais (`python_relais = "/usr/bin/python3"`) et, d'après l'amorce, la commande d'Argon de la configuration gelée.
    - Ce qui a tourné jusqu'ici : les courses précédentes ont fait tourner ce relais et cette commande sous 3.13, car ce type de conteneur a `/usr/bin/python3` = 3.13.18.
    - Vérification, sans location : lire `usr_bin_python3` dans `faits-hote.json` de la sonde v10 (`donnees/sonde-hote-durable-a1-v3-v10`, `e53876b5`).
    - Si c'est 3.11 : correction C1, ou preuve que `commande_argon_v56_nuit_v2.py` se compile et sert sous 3.11.
    - Risque si rien n'est fait : refus avant la course, puis lanceur à changer après le scellement, ce qui est un écart (nœud de Lazar) ; ou instrument changé sans le déclarer.
16. À corriger (vérification, sans code) — versement « partie de `main` » par clone superficiel, partiel et clairsemé : plausible (le parent est sur le serveur), mais jamais joué contre GitHub ; la sonde v10 versait sur une branche orpheline.
    - Épreuve gratuite depuis une session : la même suite `git`, avec une branche jetable.
    - Expiration du jeton GitHub, lue sans l'afficher : elle doit tomber après T0 + 82 h.
17. À corriger (code C3) — poussée non vérifiée : le texte promet « données gardées, la session décide », mais aucune voie ne les récupère.
    - Pas d'accès en ligne de commande : le conteneur est lancé par `--entrypoint`.
    - Toute relance rejoue la reprise, qui refuse le versement (`…-versement` existe déjà, R12) et arrête de nouveau la machine.
    - Après l'échéance, la minuterie détruit la machine dès la relance.
    - En pratique, une poussée finale manquée perd donc la course.
18. Note — offre la moins chère sur un hôte particulier : tout échec réseau après l'envoi revient en code 3 au pire cas (≈ 1,6 USD comptés) et rapproche l'arrêt au plafond. Aucun débit minimal n'est filtré ; changer les critères d'offre serait un changement du texte.

**Question 4 — HTTP 402 à solde nul**
19. À corriger (couple 1) — la table des codes du texte (section 4) contredit le couple 7 du brouillon 2. Selon cette table, toute erreur de l'interface, y compris un 429 de Google, revient en **code 3 au pire cas** ; seuls les 402 et 429 du relais lui-même donnent un code 4. Un 402 de Gemini suit donc ce chemin :
    - aucune dépense réelle, mais chaque appel en attente est compté ≈ 1,6 USD (≈ 33,9 USD par heure) ;
    - la course s'arrête **au plafond** (code 3 du lanceur, nature « plafond », aucun taux lu) après au plus ≈ 12 h ;
    - c'est un arrêt d'infrastructure, sans résultat.
    Le brouillon 2 dit au contraire « attend sans fin… jusqu'à 72 h ou aux plafonds de la machine ». Le correctif du rapport v2 (section 5) reste incomplet : il omet ce comptage au pire cas.
20. Note (couple 2, à prendre ou à laisser) — les deux conduites proposées par le rapport v2 (section 5) :
    - **conduite (a)** : précaution hors de la liste d'arrêt, pas un nœud. Lazar, seul à voir le solde, confirme avant la location un crédit d'au moins 400 USD, ou une recharge automatique active ; la fille l'écrit au journal de la location.
    - **conduite (b)** : changement de la liste d'arrêt (nœud de Lazar). Elle contredit « la garde n'arrête jamais la course sur un compte d'échecs » et la règle des guetteurs, et ne ferait gagner qu'environ 5 USD de machine : non recommandée.
    - La consigne de R-1539, « lire 402 comme un arrêt », n'a pas été codée, et c'est juste ainsi.

**Question 5 — clé d'Argon actuelle**
21. À corriger (couple 3) — le risque déclaré est juste mais incomplet :
    - la clé passe bien par son nom de variable (`CLE_ARGON="$GEMINI_API_KEY_2"`, R-1540) et elle est masquée partout ;
    - il manque l'exploitant de la machine, un tiers maître du conteneur (environnement, disque, mémoire), qui peut lire la clé comme le jeton GitHub ; or ce jeton écrit sur le dépôt privé, dont `registres/go.md` de `main`, que lisent les gardes ;
    - il manque aussi l'exposition déjà faite dans la transcription d'une session (R-1540) ;
    - et un tiers qui tient la clé peut user le crédit commun, donc provoquer le 402 ;
    - la rotation des deux secrets après la course est prévue (R-1539, R-1540).

**Question 6 — lignes de GO par registre**
22. Note — exactes, sans doublon, lisibles par les gardes :
    - `main` : GO-2026-11-04-06 en ligne 244 (400 USD) et GO-2026-11-05-03 en ligne 251 (35 USD), une ligne chacun, acceptés par la garde de `main` (essai sur le registre réel). `main` compte 17 doublons, que la garde admet et dont le lanceur v2 n'a pas besoin.
    - `canal/conv-audit-n04` à `740f49e2` : ligne 82 égale à l'octet à la ligne 244 de `main`, 74 identifiants, 0 doublon ; `740f49e2` est la tête du canal, donc dans la fenêtre de 200 commits.
    - GO-2026-11-05-04 n'est lu par aucune garde.

## Couples (`couples-contre-lecture-n4-v1.json`, neuf ; chaque « ancien » unique dans le brouillon 2 ; appliqués à blanc dans l'ordre, chaque « ancien » encore unique ; marqueurs et ligne 545 intacts)

1. Section 8, risque HTTP 402 : code 3 au pire cas, puis arrêt au plafond en au plus ≈ 12 h, sans dépense réelle (point 19).
2. Section 8 : précaution hors de la liste (crédit d'au moins 400 USD confirmé par Lazar) ; conduite (b) non retenue (point 20).
3. Section 8, « Création » : risque de la clé complété (point 21).
4. Section 12 : machine sous GO-2026-11-05-03, au plus 32,57 USD, aucune décision pendante (point 2).
5. Section 13, point 3 : idem (point 2).
6. Section 0.5 bis : le lanceur connaît aussi GO-2026-11-05-03 (point 4).
7. Section 13, point 7 quater : sonde d'hôte sous GO-2026-11-05-03 (point 5).
8. Section 4 : registre du canal recopié, `0aa04b5c` (point 3).
9. Section 13, point 7 quater : contrôles du pilote déclarés (point 8).

## Corrections de code (une ligne chacune ; R12 : un lanceur v3 sous des noms neufs, puis couples sur les noms de fichiers du texte)

- C1 (si `usr_bin_python3` ≠ 3.13) — amorce : faire de `/usr/bin/python3` l'interpréteur 3.13 de la course, ou refuser ; écrire les deux versions au journal ; un essai sur un cas sain et un sur un artefact.
- C2 — `preparer` : refuser le départ si le signe de vie n'est pas vérifié par `ls-remote` (cas sain : signe poussé ; artefact : poussée refusée, donc rien ne part).
- C3 — reprise après une poussée manquée : verser par une copie de nom neuf (pas `…-versement`, qui existe déjà) vers la branche `…-interrompue-v1`, avec le code de sortie de la course déjà écrit ; ou écrire au texte qu'une poussée finale manquée perd les données.

## Empreintes

- `docs/notes/ideation-organisme-v1/a1-v3-troisieme-course/contre-lecture-n4-v1/couples-contre-lecture-n4-v1.json` :
  `462a8ea266df41341254f7c332489acd040f3552c6ca6f56c897f37d082482c3`.
- Bloc-notes, hors dépôt : script des couples `…/scratchpad/cl-n4/outils/couples.py` `09c4c4ef…` ; sortie des essais
  `…/scratchpad/cl-n4/essais-v2.txt` `1b94b506…` ; brouillon 2 + couples, appliqué à blanc `3900c0bf…`.
- Ce rapport ne peut pas porter sa propre empreinte.

## Non vérifié

La commande gelée `commande_argon_v56_nuit_v2.py`, la configuration gelée, la sortie de la sonde v10 (`e53876b5`) et le rapport de la fille (`b95bf21e`) sont absents de ce conteneur, et le réseau est interdit. Le chemin d'un 402 est donc tiré de la table du texte, et la version de `/usr/bin/python3` de ce qu'on sait de l'image.
