# Contre-lecture complète du lanceur durable v3 d'A1-v3 (troisième course), confronté au texte scellé v3 — v1

Contre-lecteur neuf (R2) : je n'ai écrit ni le texte, ni le lanceur, ni les sondes, ni aucune contre-lecture précédente.
5 novembre 2026, de 09:36 à 10:05 UTC (heures relevées par `date -u`). Consigne :
`docs/notes/ideation-organisme-v1/a1-v3-troisieme-course/consigne-contre-lecture-complete-lanceur-v3-v1.md` (sha256 `00cf74d3…`,
compagnon vérifié). Interdits tenus : aucun commit, aucun `.sha256`, aucun fichier existant modifié, rien sous `donnees/` ni
`/home/claude/coffre-*`, aucun réseau, aucune location, aucune clé lue, aucune dépense ; commandes sous `timeout 900 nice -n 10`.
Lecture indépendante : je n'ai pas lu les fichiers du second lecteur (texte), posés dans le même dossier.

## Verdict

**Lançable après corrections — de l'ordre de course seulement ; aucune correction de code n'est exigée avant la location.**
Le code au commit `bb35e87f` fait ce que le texte scellé v3 (`c697d0df…`) écrit, sans point bloquant : 96 essais v3 rejoués passés ; 7 artefacts de plus, joués par moi sur le chemin de code v3, tous refusés comme attendu.
L'ordre doit corriger son préalable 2 (motif `ls-remote` aveugle à 3 branches sur 4) et ajouter deux écritures que le texte exige (Argon seul ; crédit d'Argon) ; une lecture sans dépense de la commande d'Argon gelée (clés de `/relais/etat`) est recommandée avant la location.

## Pièces vérifiées

- Commit `bb35e87f0e7825b2225f2ade1177da428f78352e` présent, sur `main` ; chaque fichier y a l'empreinte de son compagnon et égale
  l'arbre de travail :
  - `src/controle_ia/hote_durable_a1_v3_v3.py` `916a3c85dca3be5bc961b3a4893d6e02751f744fab010987f74dcc6594762fa2` (907 lignes)
  - `scripts/amorce_hote_durable_a1_v3_v3.sh` `e37bfde5f1aa30df1b294855ec0ec58973ce77549cdfd6fb28ae6f3705a293dd` (67 lignes)
  - `tests/test_hote_durable_a1_v3_v3.py` `2f7e929172b5f37f495d23427707b351cf0125cf6eed9c20309befe78cb3c8ef` (834 lignes)
  - `src/controle_ia/hote_durable_a1_v3.py` (v1) `5b853fde8987a472a191f769415068ecc15f1da8a042767bba4229dd5c29e0b1`
  - `src/controle_ia/sonde_hote_durable_a1_v3_v10.py` `37b70a0646874e3769a9e45ccf1438121f2126aecc8307234c3cc590f122b81c`
  - `src/controle_ia/sonde_hote_durable_a1_v3.py` `f7c7f79ba974dd1e38743265caf88f09ce7d4d96ea4676f6d66e75cc9ebca69d`
- `diff-lanceur-v2-vers-v3-hors-renommage.txt` `4dcafa22…` (compagnon égal) : refait ici depuis `hote_durable_a1_v3_v2.py` et
  `amorce_hote_durable_a1_v3_v2.sh` au même commit, renommés par `sed` : mêmes 96 lignes changées, plus la seule ligne `VERSION`
  (renommage). Rien d'autre ne change entre v2 et v3 que C1, C2 et C3.
- Texte `/home/user/ideation-organism/orchestrator/prereg/preenregistrement-attaque-goodhart-v3-v3.md` `c697d0df…` (compagnon égal,
  égal aussi à `08ad8f35`) : lus sections 0.5 bis, 0.7, 4 (GO, registre, sortie, commande exacte, bloc `plan-gele`), 8
  (« Troisième course (v3) »), 11 (bloc des empreintes), 13 (points 3, 7, 7 ter, 7 quater, 8, 9).
- Ordre `docs/procedures/ordre-fille-a1-v3-troisieme-course-v1.md` `97f712a7…` ; rapports `rapport-redaction-v3-v2.md` `569a2371…`
  et `rapport-redaction-v3-v2-additif-1.md` `22a14024…` ; contre-lecture n° 4 `b524b41c…` ; `epreuve-versement-v1.sh` `e7076f69…` ;
  compagnons égaux.
- Sonde v10 : branche `origin/donnees/sonde-hote-durable-a1-v3-v10` `e53876b5` (`faits-hote.json` : Python 3.13.18,
  `/usr/bin/python3` = 3.11.2, numpy 2.5.3, git 2.39.5, 32,1 Go libres ; journal : signe de vie poussé 42 s après la création) ;
  R-1527.
- Code gelé public : `9776ed0` ancêtre de `08ad8f35` ; les 73 empreintes du bloc `empreintes-du-code` égales aux fichiers de
  `08ad8f35` (73 sur 73) ; lus dans la mesure où l'hôte les appelle : `demonstrations/attaque_goodhart_v3.py` (dossier de sortie
  non vide refusé, variables de clé refusées, `--verifier-seulement` en code 0 sans écriture, codes 0, 2, 3) et
  `pole/attaque_goodhart_v3.py` (journal d'appel, réponses caviardées).
- GO rejoués hors réseau par le code lui-même (`verifier_go`, `verifier_go_exact`), garde de `main` `84512d4a…` :
  `registres/go.md` de `origin/main` (`0770797b`, `7f8721fb…`) : GO-2026-11-04-06 accepté (400 USD, échéance 2026-11-18),
  GO-2026-11-05-03 accepté (35 USD) ; copie du canal à `740f49e2` (`bdd492d1…`) : GO-2026-11-04-06 accepté, aucun doublon,
  ligne 82 égale à l'octet à la ligne 244 de `main` ; refus de tous le 2026-11-19 (hors validité).

## Points (gravité : bloquant / à corriger / note)

**Question 1 — Le code fait-il ce que le texte écrit, et rien d'autre ?**
1. Note — Location conforme (sections 0.5 bis, 8, 13 point 3) : offre « gpu », une carte, ≤ 0,40 USD/h, ≥ 4 cœurs, ≥ 8 000 Mo, ≥ 30 Go, fiabilité ≥ 0,98, prise dans la réponse brute ; GO-2026-11-05-03 (exactement 35 USD) et GO-2026-11-04-06 (exactement 400 USD) par la garde de `main` ; `GO_ID=GO-2026-11-05-03` exigé ; une seule location (marqueurs `.identifiant`, `.creation-incertaine`).
2. Note — Hors du texte, sans effet sur la course : l'offre doit être la moins chère des conformes ; jusqu'à 4 autres offres sur « no_such_ask », chacune revérifiée.
3. Note — Borne de la machine : 0,40 × (600 + 288 000 + 3 600 + 600 + 300) s ÷ 3 600 = 32,57 USD ≤ 35 USD ; rien d'imputé sous GO-2026-11-04-09 ni GO-2026-11-05-03 dans `registres/depenses.md`.
4. Note — Préparation conforme (section 8 ; 7 quater) : C1 vérifié par l'amorce puis par l'hôte, versions au journal ; GO revérifiés sur `main` ; copie du canal ; C2 avant l'extraction des pièces ; pièces gelées ; clone public descendant de `9776ed0` ; texte = empreinte = compagnon ; statut vide ; port 8805 ; relais (410, 9 000, 0 appel, clé présente) ; `--verifier-seulement` en code 0.
5. Note — Commande de la course : celle de la section 4, à l'interpréteur près (`/usr/local/bin/python3` au lieu de `python3`, C1) ; lancée depuis `orchestrator/`, sans coquille, environnement sans variable de clé ; registre et sortie aux chemins `/root/a1-v3-troisieme-v1/…` du texte.
6. Note — Garde conforme : relevé chaque minute, relais mort relancé et jamais arrêté, aucun arrêt sur échecs ni sur dépense d'Argon ; 80 h et 32 USD comptés depuis le départ du conteneur ; arrêt de la course par son groupe de processus (TERM puis KILL). Les 400 USD, 9 000 appels et 72 h sont tenus par le lanceur gelé (bloc `plan-gele` : 400, 72, GO-2026-11-04-06) et par le relais, comme le texte l'écrit.
7. Note — La durée de la course est aussi bornée par « échéance absolue moins 1 h » (M-B, absent du texte). Cette borne ne mord avant 72 h que si le conteneur démarre plus de ≈ 7,9 h après la création ; le contrôle à T0 + 40 min a alors déjà détruit la machine.
8. Note — Fin, versement, destruction et reprise conformes : liste d'empreintes ; contrôle des secrets ; branche neuve partie de `main` ; poussée vérifiée par `ls-remote` ; destruction par `CONTAINER_ID`, sinon arrêt ; reprise sans relance, versée depuis `…-versement-interrompue-v1` (C3).
9. À corriger (léger) — Section 4, « Arbre propre » : `git status --porcelain` doit être copié au journal « juste avant `--verifier-seulement` et juste avant la course » ; le code le relève une seule fois, avant le relais. Écart à la lettre, sans effet probable : `--verifier-seulement` n'écrit rien.
10. Note — `_grep` coupe chaque ligne à 120 caractères : la « sortie de `grep -n` » exigée par le texte est tronquée. Restent le numéro, l'identifiant, la date et le type.
11. À corriger (léger) — `COMMIT_PRIVE` n'est écrit nulle part (journal de location, journal de la machine), et l'hôte n'écrit pas l'empreinte de ses modules. L'audit A9 ne pourra pas établir, depuis la sortie versée, quel code a tourné.

**Question 2 — Chaque garde éprouvée sur un cas sain et sur un artefact (R5)**
12. Note — Essais rejoués (commande de la consigne) : 96 passés en 109,7 s (09:43:42 → 09:45:32 UTC). C1, C2 et C3 ont chacun un cas sain, un artefact et un « artefact de départ » sur la v2, qui montre le défaut corrigé : ces essais prouvent ce qu'ils disent.
13. À corriger (essais) — Plusieurs gardes du chemin v3 n'ont pas d'artefact dans le fichier v3 ; elles ne sont éprouvées que sur leurs copies de la v1 ou de la v2 :
    - empreinte du texte, descendance du code gelé, pièce gelée (`MachineV3.extraire_sources`) ;
    - statut du dépôt public, port pris, `--verifier-seulement` non nul, réglages du relais ;
    - `_pousser` contredit par `ls-remote` (l'essai C2 remplace `_pousser` en entier).
    Je les ai jouées dans le bloc-notes sur le monde jouet v3 importé tel quel : 7 artefacts, 7 refus, puis versement sur la branche de refus et destruction (7 passés en 13,3 s). Les gardes marchent ; il manque les essais scellés.
14. Note — Restent sans essai :
    - `ClientPiloteV3.creer` : délai dépassé avec marqueur, certificat, espace ou guillemet ;
    - cinq « no_such_ask » de suite ;
    - `controler` sur une instance protégée ou en délai dépassé ;
    - repli `python3` de la minuterie ;
    - installations de `git` et de numpy par l'amorce (`SAUTER_INSTALLATION=1` partout ; déjà relevé par la contre-lecture n° 4).
    Leurs équivalents de la sonde v10 ont tourné sur Vast.
15. Note — Essai qui ne prouve rien : `test_borne_de_la_machine_et_versement_borne` calcule 3 × 240 + 4 × (240 + 240 + 60) = 2 880 s sur des constantes. En réalité, `verser` fait 8 appels de `git` avant la boucle de poussée, après l'arrêt de la course et du relais (au plus 2 × 120 s). Si seuls les appels réseau vont au délai, le pire cas fait ≈ 3 100 s, sous la réserve de 3 600 s ; si tous y vont, ≈ 4 300 s. La marge tient en pratique, mais l'essai ne le montre pas.
16. Note — L'essai C1 de l'amorce prouve la logique du lien avec de faux interpréteurs. Il ne prouve pas que Python 3.13, lancé par le lien `/usr/bin/python3`, trouve sa bibliothèque et numpy sur l'image. La machine le vérifie (refus sans dépense sinon), mais par `import sys` seulement, jamais par `import numpy`.

**Question 3 — Ce qui peut faire perdre la course ou l'argent**
17. Note — Boucle de redémarrage : le processus principal ne sort qu'après la fin de vie. Un conteneur relancé par ses arguments, qui redémarre en boucle (R-1530), relit l'échéance d'origine sur le disque et rejoue le `DELETE` : la boucle sert la destruction. `curl`, `git`, `setsid`, `timeout` et `base64` sont présents sur l'image (sonde v10).
18. Note — Sortie sans destruction, trois cas :
    - (a) poussée non vérifiée ou secret trouvé : arrêt voulu par le texte ; le stockage reste facturé, sans durée bornée, hors de la borne (déclaré) ;
    - (b) `ClientVast.detruire` ne lit ni `success` ni l'inventaire après le `DELETE` : un refus rendu en HTTP 200 laisserait vivre la machine jusqu'à la minuterie, toujours sous 32,57 USD ;
    - (c) une exception levée dans les gestionnaires de `principal` (journal impossible : disque plein, sortie standard coupée) tue l'hôte sans versement ni arrêt ; la course continue orpheline et ses données sont détruites à l'échéance, avec une dépense bornée.
19. Note — Destruction d'une course en marche : impossible par le pilote, car C2 interdit toute course sans branche de signe de vie, et un `ls-remote` en échec rend 6, jamais « pas de vie ». La minuterie ne frappe qu'à l'échéance, 1 h après l'arrêt de la course par l'hôte. Essais conformes ; artefact `ls-remote` contradictoire joué ici.
20. À corriger (ordre, sans code) — Machine arrêtée après une poussée manquée (« la session décide ») :
    - redémarrée **après** l'échéance de la minuterie, elle est détruite aussitôt (l'échéance d'origine est relue sur le disque) ;
    - redémarrée avant, la reprise verse sur `…-interrompue-v1`, avec le même jeton.
    C'est la seule voie de récupération, et l'ordre ne l'écrit pas.
21. Note — Taille : aucune borne avant la poussée. Un fichier de plus de 100 Mo (limite de GitHub) ferait échouer toutes les poussées, donc arrêt et données bloquées (point 20). Les tailles attendues (journaux d'appels, réponses caviardées) sont bien en dessous, mais n'ont pas été mesurées ici : l'état de la seconde course reste non lu, comme le texte l'exige.
22. Note — Jeton expiré : le code n'a aucune garde. Un jeton qui échoit pendant la course perd la sortie : versement impossible, et la reprise garde le même jeton. Seule garde : le préalable 3 de l'ordre (échéance après T0 + 82 h ; « sans en-tête : conforme » est faible). R-1551 à R-1555 montrent qu'il a servi.
23. Note — HTTP 402 d'Argon (code 3) : l'hôte n'y touche pas (ni arrêt, ni relance de la course). Le lanceur gelé s'arrête au plafond après au plus ≈ 12 h, d'après le texte ; la machine coûte alors au plus ≈ 5 USD. Conforme au texte, qui ne retient aucune garde de plus. Sa précaution (crédit confirmé par Lazar, écrit au journal) manque à l'ordre (point 31).
24. Note — Autre interpréteur : C1 lance le relais et la course par chemin absolu (3.13) ; `/usr/bin/python3` est lié à lui ; tout est vérifié deux fois, versions au journal ; sinon refus, sans dépense.
25. Note — Dépense bornée :
    - Argon : par le lanceur (400 USD) et par le relais (410 USD, 9 000 appels). Un relais relancé reprend les mêmes réglages ; s'il remet ses compteurs à zéro (non lu), le lanceur reste la borne.
    - Machine : par la minuterie (32,57 USD).
    - Hors borne, déclarés : stockage d'une machine arrêtée ; machine qui ne lance jamais son script (contrôle du pilote).
26. Note — Coup unique : une garde qui refuse **après** le signe de vie laisse `…-signe-de-vie-v1` sur le dépôt (pièces, clone public, relais réel, `--verifier-seulement` réel). Une seconde location du même lanceur ne pourrait plus partir (R12, C2) : il faudrait un lanceur v4 à noms neufs, donc un texte neuf. Ces étapes n'ont jamais tourné sur Vast (la sonde v10 remplaçait la course). L'ordre des étapes est celui que fixe le texte (7 quater). Même effet, rare : un conteneur lent qui pousse son signe de vie juste après la lecture du pilote à T0 + 40 min est détruit avant la course, et la branche reste.
27. Note — `controler` rend 2 (« refus ») sur un échec passager de `vastai` (code non nul), là où `facturation` rend 6 ; joué ici, 2 contre 6. Aucun geste dans les deux cas, mais l'ordre ne dit pas quoi faire d'un 2 : une machine sans signe de vie pourrait ne jamais être recontrôlée.
28. Note — L'ordre lance `louer` sous `timeout 900`, mais cinq créations de 300 s dépasseraient 900 s. Un `SIGTERM` pendant `vastai create` laisserait une instance possible sans marqueur. En pratique, un seul délai dépassé arrête la boucle (avec marqueur), et l'inventaire la verrait.

**Question 4 — Secrets**
29. Note — Aucune valeur de secret n'est écrite :
    - journaux du pilote et de la machine masqués (`CLE_ARGON`, `GH_TOKEN`, `VAST_API_KEY`, variables du mandataire, `CONTAINER_API_KEY`) ;
    - sorties de `vastai` jamais écrites brutes (catégorie et champs masqués) ; inventaire et facturation filtrés ;
    - délai dépassé sans ligne de commande ;
    - `fuites()` cherche chaque valeur dans chaque fichier versé avant la poussée ;
    - amorce et minuterie n'écrivent que des noms ; l'aide de `git` porte `${GH_TOKEN}` en littéral.
30. Note — Hors des journaux, des secrets restent visibles :
    - arguments de `vastai create` chez le pilote ;
    - en-tête `Authorization` dans les arguments de `curl` (minuterie) ;
    - métadonnées de Vast, clé d'instance qui voit le compte, exploitant de la machine.
    Tout cela est déclaré par le texte (R-1533, R-1539, R-1540).

**Question 5 — La commande de location de l'ordre est-elle celle que le code attend ?**
31. À corriger (ordre) — Le texte exige deux écritures au journal de la location, que l'ordre ne demande pas :
    - « Argon seul », avec identifiants et heures (section 8, point (4) ; section 13, 7 ter et 7 quater) ;
    - la confirmation par Lazar d'un crédit d'au moins 400 USD ou d'une recharge (section 8, HTTP 402).
32. Note — Arguments, variables et chemins : exactement ceux que `louer` attend :
    - 11 options requises, puis `--verifier-seulement`, puis rien ;
    - `GO_ID=GO-2026-11-05-03` dans `env -i`, avec `CLE_ARGON`, `GH_TOKEN`, `VAST_API_KEY` et le mandataire ;
    - quatre modules copiés de `COMMIT_PRIVE=bb35e87f` (le commit scellé) : le fichier seul charge ses voisins ;
    - `.etat.json` et `controler` aux bons chemins ; `offre` applique la règle de `louer`.
33. Note — Registre du canal : `COMMIT_REGISTRE=740f49e2` est la tête de `canal/conv-audit-n04` ici ; ligne à l'octet ; aucun doublon ; GO accepté (rejoué). `COMMIT_PUBLIC=08ad8f35` porte le texte et descend de `9776ed0`.
34. À corriger (ordre) — Préalable 2 : `git ls-remote origin 'refs/heads/donnees/attaque-goodhart-v3-a1v3-troisieme-v1*'` ne voit que `…-troisieme-v1` (essai local : 1 branche sur 4). Le motif juste est `'refs/heads/donnees/attaque-goodhart-v3-a1v3-troisieme-*'` (4 sur 4). Par ailleurs, `…-versement-interrompue-v1` est une copie locale, pas une branche.
35. À corriger (ordre) — « Offre disparue : nouvelle recherche, une fois » : refaite telle quelle, la commande s'arrête à `mkdir "$D" || exit 2`, car le dossier existe. Il faut écrire la reprise (dossier neuf, ou recherche seule).
36. À corriger (ordre) — Codes non traités de `controler` : 0, 2 (dont l'échec passager du point 27) et 3. Et le destinataire nommé (`session_01Qi7Gr3s7…`) n'est plus la fille qui louera (R-1552 à R-1555).

**Question 6 — Autres points**
37. À vérifier avant la location, sans dépense (non lisible ici) — Les clés de `/relais/etat` dans la commande gelée `221df610…` : `plafond_usd`, `max_appels`, `appels`, `cle_presente`, `depense_usd`. Si elles diffèrent, l'hôte refuse de partir après le signe de vie (coup unique, point 26). Les arguments de `servir` sont ceux de la première course (ordre v1, section 4). Une lecture de la commande suffit.
38. Note — Commande de création : `--args` de 9 209 caractères et commande de 9 942 (calculées avec des secrets de longueur réelle) ; la sonde v10 est passée à 8 281 et 8 770. Aucune borne de Vast connue, mais cette taille n'a jamais été éprouvée.
39. Note — Une exception de la garde (écriture du relevé, relance du relais) arrête la course (« exception_de_l_hote ») : arrêt d'infrastructure de plus, peu probable, conforme à « jamais un repli silencieux ».

## Corrections de code proposées (liste fermée ; aucune n'est exigée avant la location)

1. `controler` : rendre 6 (recontrôler) sur tout échec de `vastai` (code non nul, certificat), comme `relever_facturation`.
2. `MachineV3.se_detruire` : après `detruire`, relire l'inventaire ; encore listée → `arreter` (sinon la minuterie), écrit au journal.
3. `MachineV3.principal` : gestionnaires d'exception par `_ecrire_sans_echec`, puis `fin()` toujours appelée.
4. `louer` et `MachineV3.principal` : écrire au journal `COMMIT_PRIVE` et l'empreinte des quatre modules et de l'amorce.
5. Juste avant `lancer_course` : relever de nouveau `git status --porcelain` du dépôt public, l'écrire au journal, refuser s'il n'est pas vide.
6. `_grep` : écrire la ligne entière (sortie de `grep -n` du texte).
7. Amorce et `verifier_interpreteurs` : vérifier aussi `import numpy` (version 2.5.3) sous `/usr/local/bin/python3` et sous `/usr/bin/python3`.
8. Essais de la version neuve : les 7 artefacts du point 13, les gardes du point 14, et une durée de versement mesurée avec des `git` lents (point 15).

## Non lu (pièces absentes du conteneur ou exclues)

- Commande d'Argon gelée `commande_argon_v56_nuit_v2.py` (`221df610…`), configuration gelée `e5306c47…` et ses six pièces,
  registre de dépense `8ba92066…`, collisionneur `c9725f02…` : les branches `donnees/recuperation-collisionneur-v8-v1` et
  `canal/session-depot-reprise-n120` sont absentes du conteneur. Restent donc non vérifiés ici :
  - les clés de `/relais/etat` et les arguments de `servir` ;
  - le comportement d'un relais relancé (compteurs repris ou remis à zéro) et la réponse à un HTTP 402 ;
  - le chemin `/usr/bin/python3` écrit dans la configuration (pris du texte et de `faits-hote.json`) ;
  - le besoin de numpy de la commande.
- Rapport de la fille sur la sonde v10 (`b95bf21e`) : non lu ; lus : sa branche de données `e53876b5` et R-1527.
- État de la seconde course : non lu (règle du texte). GitHub : aucun réseau ; branches distantes et jeton non vérifiés.

## Fichiers de ce contre-lecteur (bloc-notes, non versés)

`/tmp/claude-0/-home-user/4a4722d4-e39d-57bd-bde3-e6a99e2eecdf/scratchpad/cl/` :
- `essais_cl/test_artefacts_chemin_v3_cl.py` `a02ed30558340059840a7714cbed854c147123753d92ec744b7652999465a2c2` : 7 passés ;
- `verif_go.py` `467198b5664d26268c8fbab36798686b2f35b3ade84c6f46e1d9c14b9c578c10` ;
- `ctl/essai_controler.py` `f2381653410b0f69d482a6d8a0b8e23f1a32fbbd7e6d7237164a0157afd6efd6` ;
- `longueurs.py` `265a0ad18db8ce2a6dc48e453bbcd96b59e46a2f8b446cd6a54c50aba643a93b`.
