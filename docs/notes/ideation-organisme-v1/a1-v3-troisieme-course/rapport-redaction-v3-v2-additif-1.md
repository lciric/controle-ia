# Additif 1 au rapport de rédaction v3, v2 (`rapport-redaction-v3-v2.md`, `569a2371…`) — lanceur durable v3, brouillon 3, épreuve du versement

Même rédacteur-développeur, 5 novembre 2026, de 07:18 à 07:30 UTC (heures relevées par `date -u`). Demande de la mère (07:18 UTC),
après la contre-lecture n° 4 (`contre-lecture-n4-v1/contre-lecture-n4-texte-v3-v1.md`, `b524b41c…`, « scellable après couples » ;
9 couples, `couples-contre-lecture-n4-v1.json`, `462a8ea2…`) et le fait qu'elle a vérifié : sur l'image `python:3.13-bookworm`,
`/usr/bin/python3` est **Python 3.11.2** (sonde v10, `faits-hote.json` de `donnees/sonde-hote-durable-a1-v3-v10`, `e53876b5`),
l'interpréteur de l'image, `/usr/local/bin/python3`, étant 3.13. Mêmes interdits : aucun commit, aucune poussée, aucun `.sha256`,
aucun réseau, aucune location, aucune clé lue. Le travail en cours a été fait dans un miroir du bloc-notes
(`…/scratchpad/lv2-a1v3/miroir/`) ; seuls les fichiers finis ont été copiés au dépôt (demande de la mère, 07:23 UTC). Le module et
l'amorce v3, écrits d'abord au dépôt puis déplacés au miroir avant d'être finis, ont pu figurer dans un instantané de la mère.

**Verdict.** Le lanceur durable v3 = la v2 plus **C1** (le relais, la commande d'Argon et la course sous Python 3.13), **C2** (pas
de course sans signe de vie vérifié) et **C3** (versement de la reprise depuis une copie de nom neuf). **227 essais passent**
(v1 : 49, v2 : 82, v3 : 96), aucun sauté. Le brouillon 3 = brouillon 2 + les 9 couples de la contre-lecture + 10 couples du rédacteur,
ligne 545 intacte. Le script d'épreuve du versement est prêt pour la mère ; je l'ai éprouvé en local (`file://`) seulement.

## 1. Fichiers et empreintes

| fichier (dépôt privé) | sha256 |
|---|---|
| `src/controle_ia/hote_durable_a1_v3_v3.py` | `916a3c85dca3be5bc961b3a4893d6e02751f744fab010987f74dcc6594762fa2` |
| `scripts/amorce_hote_durable_a1_v3_v3.sh` | `e37bfde5f1aa30df1b294855ec0ec58973ce77549cdfd6fb28ae6f3705a293dd` |
| `tests/test_hote_durable_a1_v3_v3.py` (96 essais) | `2f7e929172b5f37f495d23427707b351cf0125cf6eed9c20309befe78cb3c8ef` |
| `docs/notes/ideation-organisme-v1/a1-v3-troisieme-course/preenregistrement-attaque-goodhart-v3-v3-brouillon3.md` | `a92166b8f24af01916a92453ad18c763e9d0f7c9d1d4515b7fe96b98f7fbe3fe` |
| `…/a1-v3-troisieme-course/couples-brouillon3-v3-v1.json` | `2e0f742ad199967e29dbb5f7080f23edd00a276bcd729b89ce73e361b271b79c` |
| `…/a1-v3-troisieme-course/appliquer-couples-brouillon3-v1.py` | `c38471a06a7e8846dd8db9e7c8d205c5e56792bc2a2a9900ec3ce931873b4a89` |
| `…/a1-v3-troisieme-course/sortie-appliquer-couples-brouillon3-v1.txt` | `e45a3356fad59bfbaf8674aecc4fa1395126d4629eb33a494f97405549cf1d13` |
| `…/a1-v3-troisieme-course/epreuve-versement-v1.sh` | `e7076f6985074781d41ff1efba009408da5c19b934d2acd92a00ff8cef4cccb1` |
| `…/a1-v3-troisieme-course/diff-lanceur-v2-vers-v3-hors-renommage.txt` | `4dcafa22aabb3abf4e8e041f20a75e11a2b4f78be0e38e745421ca5caf19085e` |
| bloc-notes `…/scratchpad/lv2-a1v3/sorties/essais-lanceur-v1-v2-v3.txt` | `0c6453e21f9f932abecd9a9d29abf9de2bd8928ac1cf3dbeaa50bcbe30fe5f61` |

La v3 est une copie renommée de la v2 (comme les sondes successives), puis modifiée ; la v2 et la v1 sont inchangées (R12). Elle
reprend, comme la v2, le code de la v1 et de la sonde v10 : `COMMIT_PRIVE` doit porter `hote_durable_a1_v3.py`,
`hote_durable_a1_v3_v3.py`, `sonde_hote_durable_a1_v3.py` et `sonde_hote_durable_a1_v3_v10.py` (l'amorce v3 le vérifie).

## 2. Ce qui change, et rien d'autre (différentiel hors renommage : `diff-lanceur-v2-vers-v3-hors-renommage.txt`)

| point | ce que fait la v3 | essais (cas sain / artefact) |
|---|---|---|
| **C1** interpréteur | `reglages()` : `python_relais` et `python_course` = `/usr/local/bin/python3` (chemin absolu) ; `env_relais` : `/usr/local/bin` d'abord. Amorce : `/usr/local/bin/python3` doit répondre 3.13, sinon code 2 (destruction immédiate) ; `/usr/bin/python3`, chemin de la configuration gelée pour la commande d'Argon, devient un lien vers lui s'il n'est pas 3.13 (après les installations), puis doit répondre 3.13 ; versions avant et après au journal de l'amorce (versé) ; numpy installé par l'interpréteur de l'image ; `exec` par lui. Hôte : `verifier_interpreteurs` relit la version du relais, de la course et de `/usr/bin/python3`, l'écrit au journal, refuse sinon (rien ne part). | réglages v3 / v2 (`/usr/bin/python3`, `/usr/bin` d'abord : artefact de départ) ; machine, versions au journal / relais, course ou configuration en 3.11 : refus, rien ne part ; amorce, lien fait et versions écrites / image en 3.11, lien impossible : code 2 |
| **C2** signe de vie | `signe_de_vie` rend vrai seulement si la poussée est vérifiée par `ls-remote` ; sinon `Refus` avant la course (« signe de vie non vérifié par ls-remote (C2) »), versé sur la branche de refus, puis destruction : jamais une course détruite en marche par `controler` à T0 + 30 min. | cas sain de la machine (signe poussé, course partie) / branche du signe déjà là, poussée non vérifiée : rien ne part ; la v2, même cas, lance la course (artefact de départ) |
| **C3** reprise | `verser` : la copie de travail du versement s'appelle `…-versement-interrompue-v1` pour la branche `…-interrompue-v1`, `…-versement` sinon. | reprise après une poussée finale manquée (copie `…-versement` restée) : versée, détruite / la v2 y bute (R12) et arrête la machine (artefact de départ) ; copie neuve déjà là : arrêt (R12) |

Aucun autre changement : mêmes GO, offre, minuterie, versement « partie de `main` », gardes de la v2.

## 3. Essais (`timeout 900 nice -n 10`, aucun réseau, dans le miroir du bloc-notes)

- `tests/test_hote_durable_a1_v3.py` (v1), `tests/test_hote_durable_a1_v3_v2.py` (v2), `tests/test_hote_durable_a1_v3_v3.py` (v3) :
  **227 passés (49 + 82 + 96), aucun sauté, en 233 s** ; sortie `essais-lanceur-v1-v2-v3.txt` (`0c6453e2…`).
- Les 96 essais de la v3 = les 82 de la v2, renommés, et 14 neufs (C1 : 8, dont les réglages et le chemin du relais ; C2 : 3 ; C3 : 3).
- Défaut trouvé et corrigé pendant la dérivation des essais : le renommage global « v2. » → « v3. » avait aussi renommé, dans le
  monde jouet, `commande_argon_v56_nuit_v2.py` (nom gelé) ; deux essais échouaient (« relais sorti en code 2 ») ; le nom est
  rétabli et le différentiel des essais ne porte plus que les renommages voulus (contrôle par `diff`).
- Épreuve du versement, en local seulement : dépôt nu `file://` qui admet les filtres, `main` à 600 Ko de fichiers ; cas sain
  (copie de 224 Ko : clone partiel effectif ; poussée vérifiée par `ls-remote` ; branche partie de `main`) ; seconde passe :
  « déjà présente (R12) », code 2 ; adresse `lciric/controle-ia` : refusée avant tout appel, code 2.

## 4. Brouillon 3

`appliquer-couples-brouillon3-v1.py` (sortie à côté) : empreintes du brouillon 2 (`86ad379b…`) et des couples de la contre-lecture
(`462a8ea2…`) vérifiées ; les 9 couples du contre-lecteur, dans leur ordre, puis les 10 du rédacteur ; chaque « ancien » unique au
moment de son application ; ligne 545 intacte ; 19 lignes modifiées, 3 ajoutées (2 148 → 2 151 lignes). Couples du rédacteur :
noms de fichiers du lanceur durable v2 → v3 (paragraphe de tête, section 8, section 13 point 7 quater, section 14) ; « lanceur v2 »
→ « lanceur durable v3 » dans les deux passages neufs du contre-lecteur qui désignent le lanceur durable (section 4, ligne 570 ;
section 13, `controler`) — les autres « lanceur v2 » du texte désignent `demonstrations/attaque_goodhart_v2.py` et restent ; C1 et
C2 dans « Préparation sur la machine », C3 dans « Reprise du conteneur » (section 8) ; une ligne de tête ; quatre lignes en 0.7
(points 23 à 26 : couples et noms, C1, C2, C3 ; avant → après ; raison).

## 5. Épreuve du versement, pour la mère

Depuis sa session (accès par le mandataire, aucun jeton dans la commande), dans le dossier de la course :
`timeout 900 nice -n 10 bash epreuve-versement-v1.sh /tmp/epreuve-versement-a1-v3-v1` (dossier neuf). Réussie si la dernière
ligne dit « ÉPREUVE RÉUSSIE » (poussée vérifiée par `ls-remote`, branche `essai/a1-v3-versement-epreuve-v1` partie de `main`) ;
la taille de la copie (Ko) dit si le clone partiel tient contre GitHub. La branche jetable reste : sa suppression est un geste de
la mère (commande écrite en tête du script).

## 6. Ce qu'un contre-lecteur doit regarder en premier

1. C1 change un fichier système de la machine (`/usr/bin/python3` devient un lien vers 3.13) : aucun outil Debian n'est employé
   après (installations faites avant) ; le lien survit à une reprise du conteneur ; la commande d'Argon gelée a tourné sous 3.13
   dans les courses précédentes (contre-lecture n° 4, point 15).
2. C1, chemin de la configuration gelée : je n'ai pas relu la configuration gelée (`e5306c47…`, absente du conteneur) ; le chemin
   `/usr/bin/python3` vient du commentaire de l'amorce v1 et de la contre-lecture ; si la configuration lançait la commande par
   `python3` (chemin de recherche), le chemin de la course (`/usr/local/bin` d'abord) suffit aussi.
3. C2 rend la course dépendante d'une poussée vers GitHub avant le départ : une panne de GitHub à ce moment donne un refus (machine
   détruite, quelques centimes) au lieu d'une course.
4. C3 : une seconde reprise après un versement de reprise manqué bute sur la copie `…-versement-interrompue-v1` et arrête la machine
   (données gardées sur son disque, R12) : c'est voulu, et c'est écrit.
5. L'épreuve du versement doit passer contre GitHub **avant** la location (risque du rapport, section 6, point 5).

## 7. Commande de la location

Celle du rapport (`rapport-redaction-v3-v2.md`, section 7), avec les seuls noms du lanceur v3 : `hote_durable_a1_v3_v3.py` à la
place de `hote_durable_a1_v3_v2.py` (copie des quatre modules et appels `offre`, `louer`, `controler`, `facturation`), et
`D=/home/user/hors-clone-a1-v3-troisieme-v3` (neuf, R12) ; journal `journal-location-a1-v3-troisieme-v3.log`.
