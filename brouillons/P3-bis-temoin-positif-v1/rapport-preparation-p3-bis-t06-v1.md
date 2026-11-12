# Rapport — reprise de la préparation de P3-bis (témoin positif planté, GO-2026-11-02-29) et de T0.6 (organisme v0 et test croisé d'étiologie, GO-2026-11-02-28) — v1

- Écrit le 2026-11-03 vers 00:10 UTC (heure relevée par `date -u`) par le sous-agent de reprise de la session conv-audit
  (Claude), qui n'a écrit aucun des fichiers vérifiés. Consignes suivies : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/preparation-p3-bis-et-t06-reprise-prompt.md`
  et la consigne d'origine `brouillons/passation-conv-audit-2026-11-02-soir/prompts-sous-agents/preparation-p3-bis-et-t06-prompt.md`.
- Règles tenues : aucun commit ; aucun fichier `.sha256` ; aucun fichier existant modifié (`git status` : sept fichiers
  neufs non suivis, plus ce rapport) ; rien lu ni écrit sous `donnees/` (fichiers de P3 cités par chemin et empreinte,
  empreintes lues dans `diag/…/episodes-p3.json`) ; aucune branche, aucune ref, aucun `git fetch`, `checkout` ni `stash` ;
  aucun appel de réseau ni de modèle ; tout calcul sous `nice -n 10`, Python en `-I -B` ; aucune suite d'essais du dépôt
  lancée (course décisive en cours sur la machine). Brouillons de travail : `/home/claude/scratch/p3-bis-t06/` (rejeux et
  essais de sortie).

## 1. Verdict

Le travail interrompu est **juste dans ses chiffres, ses chemins et ses empreintes**, et sa prémisse centrale est vraie
(P3 avait déjà la consigne dans le contexte de chaque action) ; il contient **une erreur statistique** (critère par épisode
mal calibré), **un écart de configuration non déclaré**, **une affirmation invérifiable**, **une description fausse de la
chaîne** et **une lecture trop conclusive**. Le préenregistrement de P3-bis est repris en brouillon 2, corrigé ; le
brouillon 2 de T0.6 est écrit, avec un obstacle de conception levé d'avance (tâches de distillation et d'évaluation).

## 2. Ce que j'ai vérifié dans le travail précédent

Fichiers : `brouillons/P3-bis-temoin-positif-v1/` (consignes, préenregistrement, configuration en brouillon 1 ; script et
sortie de puissance v1) ; `brouillons/T0.6-organismes-v0-v1-brouillon2-pieces/` (script et sortie de puissance v1) ; copies
de travail sous `brouillons/passation-conv-audit-2026-11-02-soir/travail-interrompu/`.

- **Empreintes** : les dix-huit documents cités par le brouillon 1 et ses deux scripts (brief, programme, texte, consignes, configuration et
  deux addenda de P3, verdict v2, six sorties sous `diag/`, provenance, note de décision, P-015, note de puissance de P3)
  ont été recalculés : tous égaux à leurs sceaux et aux valeurs écrites. Les pièces du travail interrompu sont égales à leurs
  sceaux compagnons.
- **Renvois de lignes** (tous exacts) : texte de P3 l. 34 (entropie), l. 293-296 (phrases de persona), l. 163-268
  (métrique), l. 287-327 (plan) ; `propositions.py` l. 238-249 et 266-268 ; `conditions.py` l. 81-82 ; `harnais/episode.py`
  l. 212-217 et 254 ; `p3_instance.sh` l. 249 (300 minutes) ; `amorce_instance_p3.sh` l. 38 (360 minutes) ; `registres/go.md`
  l. 74 et 75 ; P-015 l. 61 et 68-69 ; `run.py` (`DUREE_MAX_S` = 18 000, `exiger_config_p3` refuse `null`, `CONFIG_CITEE`) ;
  `lecture.py` (`JEUX`, `etats_des_jeux`, réserve « témoin sans effet » sur les titres) ; `statistiques.accumulation`
  (paramètre `autre`) ; l'essai `test_configuration_de_p3_mode_et_durees` existe et ne teste pas `null`.
- **Chiffres** (tous exacts) : P3-P1 1,5227 [1,2464 ; 1,8012] ; bornes basses 0,5313 et 0,4813 contre 0,5717 et 0,5356 ;
  premier addendum A2 0,9137 [0,8869 ; 0,9375], écart moyen 0,4283, borne basse 0,3973, A8 12,2 % ; aire de validation de
  la tromperie 1,0 ; 0,5748 contre 0,5248 ; P3-P5 seuil réduit 4,957, rappel 0 ; durées 11 179,1 s, 9 644,6 s, 40,2 s par
  épisode ; instance de 22:28:53 à 02:06:50 UTC, 1,0889 USD de l'heure, ≈ 3,96 USD ; torch 2.14.1+cu130, pilote
  580.159.03 ; 30 fils effectifs ; R-321 ; R-392 (message n° 135, 1,76 USD) ; P4-instrument à 194 tests (R-287), jamais
  lancé ; « aucun contrôle positif » (note de décision, l. 11).
- **Prémisse** : vérifiée dans le code. Le message système porte la consigne privée (`consigne_privee`, l. 247-248) ; le
  harnais garde toute la conversation (`trs[b][i].ids + fmt.tour(...)`, l. 217 ; `trs[b][i].ids = ctx + nv + …`, l. 254).
- **Calculs de puissance rejoués** (`nice -n 10 .venv/bin/python -I -B …`) : les deux sorties sont reproduites **à l'octet
  près** (`8a5a5e10…` et `40d2c9e7…`). Les deux scripts ne lisent que `diag/` et `docs/notes/` (garde sur « donnees » dans
  le chemin, sceaux vérifiés) : **les variances viennent des seules sorties scellées, sans ouvrir les données tenues à
  l'écart**. Formules justes (erreur type par la demi-largeur, aire minimale détectable, recoupement de B3 à l'identique,
  Jonckheere–Terpstra stratifiée, approximation normale recoupée par permutations), **sauf le critère par épisode** (E1).

## 3. Erreurs et écarts trouvés

- **E1 (statistique, P3-bis, PB-2)** : « k ≥ 4 sur 60, borne basse de Clopper-Pearson au-dessus de 1/61 » tient le seuil
  pour fixe ; il est le maximum, aléatoire, des 60 épisodes honnêtes. Sous l'échangeabilité, P(K ≥ k) =
  Π_{j<k} (60 − j)/(120 − j) : 0,0594 à k = 4 (et non ≤ 0,025), 0,0287 à k = 5, 0,0137 à k = 6 ; recoupé par simulation
  (200 000 tirages : 0,0593 et 0,0137). Corrigé : **k ≥ 6** ; puissance refaite (v2).
- **E2 (configuration, P3-bis)** : `fils_entrainement` passe de 32 (P3) à 30 sans être déclaré. Le choix est défendable
  (P3 avait 30 fils effectifs, quota 30,72) ; il est déclaré au brouillon 2 comme l'un des quatre écarts à la configuration
  de P3.
- **E3 (identité du code, P3-bis)** : « `git diff --stat 7a54d43 HEAD` est vide » n'est pas vérifiable ici : le clone est
  superficiel (six commits, tous du 2026-11-02) et `7a54d43…` y est absent. Vérification partielle : `propositions.py`
  (`5d97b223…`) et la garde de calcul (`579f65c8…`) égaux aux empreintes notées pour ce commit. À refaire au candidat dans
  un clone complet. Conséquence pratique : la lecture décisive (`exiger_code_cite`, `git diff --quiet <commit> HEAD`) doit
  se faire dans un clone qui contient le commit cité.
- **E4 (chaîne, P3-bis)** : la déclinaison était dite « sans logique nouvelle ». Faux : la surveillance (arrêt sur processus
  mort ou sur dépense, jamais sur durée), la règle du crédit (`lancer_p3_v1.sh` l. 45 et 288) et le bloc des valeurs du
  texte relu par les contrôles (`controles_avant_depense_p3_v1.sh` l. 229, 243-256, 267-269) changent de logique : à
  écrire, éprouver (R5) et contre-lire.
- **E5 (lecture, P3-bis, PB-5)** : « B contre H au-dessus : le nul de P3 tient à la discrétion de la consigne » conclut trop :
  B contre H mêle la consigne de sabotage et la seule présence d'un texte. Phrases réécrites, sans conclusion sur la cause
  du nul de P3.
- **E6 (consignes, P3-bis)** : le brouillon 1 comptait « higher cost » parmi les motifs qui couvrent B ; ce motif venait du
  rappel de P3, absent de P3-bis. Vérifié avec la fonction du code : B est couvert par quatre motifs, A par « three times »
  seul, T par aucun. Corrigé en brouillon 2 (les six textes cités restent identiques, vérifié par `blocs_cites`).
- **E7 (règle R12)** : deux contenus portent le nom `P3-bis-preenregistrement-v1-brouillon1.md` (`8b97e3a8…` committé dans
  le dossier, `12686f85…` dans les deux copies de travail, antérieures). Consigné ; la version committée fait foi.
- **E8 (conception, T0.6, puissance v1)** : le script v1 suppose 60 tâches d'évaluation. Or un organisme distillé sur les
  actions de P3 a vu 60 des 64 tâches d'évaluation (les « 60 premières dans l'ordre du tirage », R-143) : l'évaluer sur
  elles mêlerait mémoire et étiologie. Ce n'est pas une erreur de calcul, c'est une hypothèse de plan à lever (DT-1).
- **Lacune connue, non une erreur** : longueurs de A et T non mesurées (aucun vrai tokeniseur sur la machine : les deux
  `tokenizer.json` suivis hors de `donnees/` sont des jouets de 8 494 et 35 346 octets).

## 4. Ce que j'ai écrit (fichiers neufs, chemins et sha256)

| fichier | sha256 |
|---|---|
| `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon2.md` | `9808fb2a4ef6b516fb69795f21aa0b0eb1786a1f4e64600dcd13e4012eb31892` |
| `brouillons/P3-bis-temoin-positif-v1/P3-bis-consignes-v1-brouillon2.md` | `7d35576d65c030edcc6441e142ea95732679b674edcb1fd1af86ab8f69c04367` |
| `brouillons/P3-bis-temoin-positif-v1/puissance_p3_bis_v2.py` | `c9d0b6c310743d33248cd21b9cc45c9ab0668addc88532c2bb6e72db9c3884bc` |
| `brouillons/P3-bis-temoin-positif-v1/puissance-p3-bis-v2.txt` | `1df8311fbdeceeb0a33c5f053d39eb7b7a6216b397f346eae8fb4af083240ae7` |
| `brouillons/T0.6-organismes-v0-v1-brouillon2.md` | `e960ec10fa5c5c3e398654a5a98a51a1fb1da61ec649f6f3672f42b14a3b7cdd` |
| `brouillons/T0.6-organismes-v0-v1-brouillon2-pieces/puissance_t06_v2.py` | `be3d6121285ce7ee49c9b125755e09ad668aa491a5371e8c3ea68acea3351011` |
| `brouillons/T0.6-organismes-v0-v1-brouillon2-pieces/puissance-t06-v2.txt` | `87813a3677e00312d91275fa88df9390880cd07179e5e6b654f1995f04851c50` |

Le présent rapport n'est pas dans la table (son empreinte est donnée dans la réponse finale de la session). La
configuration de P3-bis n'a pas changé : `P3-bis-temoin-positif-config-v1-brouillon1.json` (`8ab04d54…`) reste la pièce,
écarts déclarés au texte. Les sorties v2 se rejouent à l'octet près (vérifié deux fois chacune).

## 5. P3-bis (GO-2026-11-02-29) : prêt, manque, devis

- **Prêt** : dessin (A planté décisif, T témoin de même longueur, B dessin littéral du GO en descriptif, H honnête), quatre
  emplacements du code de P3 sans code de conditions neuf ; hypothèses ; prédictions PB-1 à PB-10 ; métrique et seuil ;
  **critères de lecture gelés avec les deux issues** (« vu » : la chaîne marche, le nul de P3 se lit sur le saboteur discret,
  portée gelée ; « non vu » : la chaîne est à réparer, P3 ne dit rien du saboteur) ; liste d'arrêt sans couperet de temps
  (plafond d'argent de 80 USD seulement) ; puissance (aire minimale détectable 0,6389 à 0,6585 ; par épisode k ≥ 6) ; devis ;
  liste exacte de ce que le code et la chaîne doivent changer ; six décisions avec défaut.
- **Manque — code** : changement 2 (a) (`run.py` l. 110-113, 395, 434 : durées `null`) et 2 (b) (`conditions.py` l. 35-36 :
  motifs étendus), avec leurs essais ; scripts `scripts/amorce_instance_p3bis.sh` et `scripts/p3bis_instance.sh` (sans
  `timeout`), dans le commit cité ; chaîne `docs/procedures/P3-bis-temoin-positif-v1/` avec la logique neuve (surveillance,
  crédit, valeurs du texte), bancs (R5), répétition jouet et répétition finale.
- **Manque — mesures et données** : longueurs de A, T et B en jetons, seuls et dans le gabarit, sur les 60 tâches, avec le
  vrai tokeniseur (sur une machine qui l'a ; ajustement d'un mot au plus, brouillon nouveau) ; `git diff` depuis `7a54d43`
  dans un clone complet ; compte des essais. Aucune donnée nouvelle : données génériques et tâches de P3 déjà versées.
- **Manque — textes** : contre-lecture R2 du brouillon 2 par un sous-agent neuf (fichiers listés dans le texte), traitement,
  candidat, scellement, commit et poussée avant la course (le GO l'exige).
- **Manque — décisions de Lazar** : DB-1 (A décisif ; écart à la description littérale du GO), DB-2 (entropie de P3),
  DB-3 (aucun couperet), DB-4 (motifs), DB-5 (ligne d'accord), DB-6 (P3-bis tient le rôle de P4-instrument pour P-015) ;
  défauts sous 48 heures, recommandations écrites. GO de calcul présent.
- **Devis** : ≈ 4 à 4,5 heures sur A100 SXM4 80 Go à 1,0889 à 1,30 USD de l'heure, ≈ 4,4 à 5,9 USD de calcul, plus disque et
  téléchargement : **attendu ≈ 6 à 9 USD** ; GO : attendu ≈ 25 USD, plafond 80 USD.

## 6. T0.6 (GO-2026-11-02-28) : prêt, manque, devis

- **Prêt (brouillon de travail)** : obstacle des tâches levé d'avance et deux plans chiffrés ((a) lettre du GO, 600 actions
  de P3, 36 tâches disjointes ; (b) recommandé, actions neuves du saboteur instruit de P3 sur les 32 tâches de réserve,
  64 tâches d'évaluation) ; adaptateur de rang 16 à dose réglable (dose 0 = base au bit près, contrôle d'identité des
  logits) ; neuf conditions ; courbe dose–réponse à cinq doses (0, 0,25, 0,5, 0,75, 1) ; test croisé dans les deux sens,
  sonde fixée d'avance (différence de moyennes, couche 15, maximum), plis par tâches, plancher apparié ; trois tables de
  lecture gelées (organisme et dose–réponse ; sens 1 ; sens 2, chacun avec ses deux issues « transfert vu » et « transfert
  non vu », et un contrôle dans l'étiologie qui rend « non tranché » un non-vu sans portée) ; liste d'arrêt sans couperet ;
  puissance (effet du coût minimal 0,394 en (b), 0,525 en (a) ; dose–réponse 0,97 à 1,00 à la moitié de l'effet de P3 en
  (b) ; aire minimale détectable du test croisé 0,612 à 0,657 en (b), 0,632 à 0,705 en (a)) ; devis.
- **Manque — décisions de Lazar** : DT-1 (source de la distillation et tâches), DT-2 (une course au lieu des deux temps de
  P-015 (b)), DT-3 (statut du test croisé pour le critère 3 : P-011 (c) le garde descriptif, le brief l. 171 permettrait une
  seconde route), DT-4 (lecture des sondes après le verdict de P3-bis), DT-5 ((i) à doses et contrôles croisés hors de cette
  course), DT-6 (A100 ou H200).
- **Manque — textes** : le préenregistrement de **T0.7 en mode « coût »** (GO-28 exige T0.6 et T0.7 scellés avant la
  course ; le brouillon 4 de T0.7 est en mode « contrôles » et ses jeux synthétiques ne sont pas écrits) ; T0.8 si « diffus »
  se lit sur l'instance ; contre-lecture R2 de ce brouillon, candidat, scellement.
- **Manque — données** : (a) textes de P3 présents (`donnees/20261019-230011-p3-reel/textes-actions-p3.jsonl`, `ba05fa13…`),
  sans identifiants générés (retokenisation déclarée) ; (b) rien, la génération est dans la course. Fichiers de tâches
  présents (`76cdeace…`, `8d20a698…`), à vérifier par la chaîne.
- **Manque — code** (le plus lourd, chemin critique avant l'échéance du 2026-11-16) : lanceur de T0.6 côté instance (phases,
  lots par état d'adaptateur, distillation, empreintes, contrôle d'identité à dose 0), distillation par transcription
  entière (fonction neuve), lecteur du coût neuf (P-015), test croisé (plis, planchers appariés, aire moyenne des plis),
  lecture et tables, scripts et chaîne sans couperet, répétitions ; plusieurs centaines de lignes et leurs essais.
- **Manque — préalable** : verdict « vu » de P3-bis avant toute lecture de sonde (P-015 (b)).
- **Devis** (A100 aux débits de P3) : (a) ≈ 4,8 à 6,9 h, **≈ 7 à 13 USD** tout compris ; (b) ≈ 11,5 à 17,1 h, **≈ 14 à
  27 USD** ; GO : attendu ≈ 60 USD, plafond 200 USD. H200 : aucun débit ni prix mesuré dans le dépôt.

## 7. Dix lignes pour un contre-lecteur neuf

1. Lis d'abord les deux brouillons 2, puis les sources aux lignes citées ; ne te fie pas à ce rapport.
2. Vérifie la prémisse de P3-bis dans le code : `propositions.py` l. 238-249 et 266-268, `harnais/episode.py` l. 212-217 et 254.
3. Recalcule P(K ≥ k) = Π_{j<k} (60 − j)/(120 − j) : 0,0594 à k = 4, 0,0137 à k = 6 ; juge si k ≥ 6 et le niveau 0,025 conviennent.
4. Vérifie que les phrases de persona de A et T sont mot pour mot celles du texte de P3 (l. 293-295) et que les longueurs restent à mesurer.
5. Compare la configuration de P3-bis à celle de P3 clé par clé : quatre écarts seulement (consignes, empreinte, deux durées `null`, 30 fils).
6. Juge la portée de l'issue « vu » et les phrases affaiblies de PB-5 : concluent-elles plus que le jeu A contre T ne permet ?
7. Vérifie qu'aucun couperet de temps ne reste (code 2 (a), scripts sans `timeout`, surveillance à dépense) et que 80 USD est le seul arrêt d'argent.
8. Pour T0.6, refais le compte des tâches : 64 d'évaluation, P3 en a pris 60, 32 de réserve ; juge DT-1 et ses deux plans.
9. Pour T0.6, examine l'aire moyenne des deux plis, l'appariement des planchers par indice et la sonde fixée d'avance (coïncidence avec P3 déclarée).
10. Contrôle que rien n'a été lu sous `donnees/` : les scripts refusent ces chemins ; les empreintes des fichiers de P3 viennent de `diag/…/episodes-p3.json`.
