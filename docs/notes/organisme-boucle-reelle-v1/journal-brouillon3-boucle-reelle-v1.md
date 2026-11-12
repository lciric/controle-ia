# Journal du brouillon 3 du préenregistrement de la course réelle de l'organisme (code v66, configuration v6) — v1

- **Rédacteur** : Claude Opus 5.5 (`claude-opus-5-5`), rédacteur du brouillon 2 (R-2253), sous-agent de la session mère
  `session_01VJdZpSMxSdk2SJ1ScmdfNv`. Je n'ai écrit ni la contre-lecture 1 ni ses couples.
- **Ordre** : message de la mère du 10 novembre 2026 (R-2253) ; même consigne
  (`consigne-redaction-prereg-course-v66-b2-v1.md`, `bfdc52ad2309636e42f28cc565a8e4e9c1a94c1b89a229224b4c000f90f9ac6d`,
  revérifiée) et mêmes interdits communs v2.
- **Heures** (temps universel, relevées par `date -u`, 10 novembre 2026) : début 15:14:15 ; couples écrits à partir de
  15:18:42 ; script final joué à 15:21:52 ; journal écrit à partir de 15:22 (heure de fin dans le rapport à la mère).
- **Aucune dépense, aucun appel de modèle, aucun réseau, aucun commit, aucune commande git autre que `git show`,
  `git ls-files` sur un chemin nommé et `git grep` sur `registres/decisions.md` seul.** Arbre de l'organisme lu par
  `git show` seulement ; aucun essai lancé. Fichiers ouverts en plus des entrées : `relais_kimi_v3.py` (dépôt de travail,
  fichier nommé), `commande_kimi_v6.py` et `commande_argon_v56_nuit_v6.py` (dossier de course), et, par `git show`,
  `pole/adaptateurs.py`, `pole/tests_de_mort*.py` (constantes) et `pole/tour_ferme_v64.py` (bornes). Aucun refus de
  permission ni de classifieur. Brouillons 1 et 2 intacts (`736e3fd6…`, `f87ad0e4…`, avant et après).

## 1. Entrées vérifiées et sorties

Entrées : brouillon 2 `f87ad0e40f1b2941e66d343bfb4b5eeaaefa22a3e2eeb448f852900de112b8a7` ; rapport de la contre-lecture 1
`prereg/contre-lectures/preenregistrement-boucle-reelle-organisme-v1-brouillon2-cl1.md`
`90ba927ec9ec390026f3d2dbbab2fe32f1e8ff8bb553f49a15842ce5e420395c` ; couples `…-cl1-couples.json`
`a555f82c659907b273e47b913f0c48a4231a66115883c58d201383c0128ca514` (égaux à leurs compagnons) ; R-2253 lu au registre.

| fichier (`docs/notes/organisme-boucle-reelle-v1/`) | sha256 |
|---|---|
| `preenregistrement-boucle-reelle-organisme-v1-brouillon3.md` | `04598de62300185806975ae5df5fcdd054557f9a46b935e40d7d3479c240ec23` |
| `couples-brouillon3-boucle-reelle-v1.json` | `c1c5f4f5a723f80dfacf128c229de32d68f2a8c07d27a1688a2c21570698b262` |
| `faire-brouillon3-boucle-reelle-v1.py` | `93c2aea44591e5fc0e2e7809a5aa1f2341f4fd8600f01a4591612444be1a2dc9` |
| `journal-brouillon3-boucle-reelle-v1.md` | ce fichier (empreinte à son compagnon) |

Commande (depuis `/home/user/controle-ia-travail`) : `.venv/bin/python -I -B docs/notes/organisme-boucle-reelle-v1/faire-brouillon3-boucle-reelle-v1.py --depot /home/user/controle-ia-travail --brouillon3 docs/notes/organisme-boucle-reelle-v1/preenregistrement-boucle-reelle-organisme-v1-brouillon3.md --couples docs/notes/organisme-boucle-reelle-v1/couples-brouillon3-boucle-reelle-v1.json` → code 0 ; rejouée d'abord dans mon bac à sable, même brouillon à l'octet.

**Contrôles du script** : CLC-01 à CLC-09 appliqués tels qu'écrits, chaque texte ancien trouvé une fois ; **empreinte après eux
seuls : `b19db56e58302d57ee3d1aa114a6038f9aceb54b93b233930da513d7b4846cc6`, égale à celle de la contre-lecture et de R-2253** ;
puis 23 couples B3 ; section 16 (blocs lus par le lanceur) égale à l'octet à celle du brouillon 2 ; marqueurs restants exactement
ceux de la section 3 ; aucune des tournures périmées listées (« attend la décision de Lazar », « nœud NL-1 » en renvoi,
« six préalables », « Du texte : à faire », …) ne reste.

## 2. Couples : 32 (9 de la contre-lecture 1, tels qu'écrits ; 23 du rédacteur)

| id | section | gelée | constat | objet |
|---|---|---|---|---|
| CLC-01 | 12.4 | non | CLB-01, CLB-02, CLB-08 | tel qu'écrit |
| CLC-02 | 12.4 | non | CLB-01 | tel qu'écrit |
| CLC-03 | 12.3 | non | CLB-02, CLB-05 | tel qu'écrit |
| CLC-04 | 8 | **oui** | CLB-03 | tel qu'écrit (décision de la mère) |
| CLC-05 | 8 | **oui** | CLB-06 | tel qu'écrit |
| CLC-06 | 10 | **oui** | CLB-07 | tel qu'écrit |
| CLC-07 | 10 | **oui** | CLB-07 | tel qu'écrit |
| CLC-08 | 8 | **oui** | CLB-09 | tel qu'écrit |
| CLC-09 | 8 | **oui** | CLB-09 | tel qu'écrit |
| B3-01 | titre | non | brouillon 3 | titre |
| B3-02 | en-tête | non | CLB-04 ; R-2253 | statut, marqueurs restants, ce qui précède toute course |
| B3-03 | en-tête | non | brouillon 3 | rédacteur |
| B3-04 | en-tête | non | brouillon 3 | heures |
| B3-05 | en-tête | non | R-2253 | consigne et message |
| B3-06 | en-tête | non | CLB-04 (2) ; NL-2 | ligne de GO neuve, mot de Lazar, empreinte du registre après inscription (marqueurs) |
| B3-07 | en-tête | non | brouillon 3 | registre : R-2253 |
| B3-08 | Documents | non | CLB-05 | contre-lecture 1, ses couples, relais Kimi |
| B3-09 | Documents | non | brouillon 3 | pièces versées |
| B3-10 | 0 | non | CLB-04 (3) | point 6 : issue du cas à la ligne C1 |
| B3-11 | 0 | non | CLB-04 (3) | point 8 : ce qui reste |
| B3-12 | 3 | non | CLB-11 | garde 22 : identité réglée sur l'exécuteur sondé |
| B3-13 | 8 | **oui** | CLB-04 (4) ; NL-1 | ligne C1 : issue du cas, mot et issue en marqueurs |
| B3-14 | 8 | **oui** | CLB-04 (4) | V-8 : renvoi à la ligne C1 |
| B3-15 | 10 | **oui** | CLB-11 | garde 22 : lettre de l'identité et de l'ordre |
| B3-16 | 11 | non | CLC-03 | préalables : renvoi sans nombre |
| B3-17 | 11 | non | CLB-04 (5) | renvoi à la ligne C1 |
| B3-18 | 12 | non | CLB-04 (6) ; Q-4 ; R-2253 | 12.1 (GO de la course) ; 12.2 réécrite ; validateur qui fait foi |
| B3-19 | 12 | non | CLB-05 ; R-2253 | relais : `--max-appels` (calcul), prix, plafonds égaux, commandes |
| B3-20 | 13 | non | CLB-04 (2) ; NL-2 | mot de Lazar (marqueur) |
| B3-21 | 13 | non | CLB-10 ; R-2253 | machine louée sous la ligne, validée à blanc avant tout appel payant ; texte nommé |
| B3-22 | 14 | non | CLB-04 (5) | renvoi à la ligne C1 |
| B3-23 | 15 | non | CLB-04 (7) ; Q-4 | entrée de la contre-lecture 1 ; vérification courte à faire ; contre-lectures du code |

**Sections gelées touchées par le rédacteur** : trois couples, aucun ne change une hypothèse, une prédiction, un signe, un
seuil ni une issue. B3-13 : la fin de la ligne C1 garde le même contenu (l'issue du cas attend Lazar), mise sous la forme que
le candidat remplira (mot verbatim et issue en marqueurs) ; B3-14 : renvoi ; B3-15 : lettre de la garde 22 conforme au code
(CLB-11).

**Calcul de CLB-05** (section 12.3, point 6) : devis, section 3.4, « chaîne cassée », 37 cartes testées (17 en génération 1,
12 + 8 en génération 2) ; un appel par session de commande externe (devis, section 3.3 ; `AdaptateurCommandeExterne.lancer`
lance la commande une fois par session ; `commande_kimi_v6.py` sans reprise interne). Kimi : 2 + 37 × 12
(`TOURS_MAX_PAR_FICHE` = 12, `tests_de_mort_v2.py` l. 139, importée par l'étage v5 depuis la v4 ; borne de 0,80 USD par
carte, `tour_ferme_v64.py`) = **446**. Argon : 2 + 37 × 1 (une session de vérificateur par carte, étage v5) = **39**. Prix : devis,
section 2 (Kimi 2 et 10 USD par million de jetons ; Argon 10 et 50, fixés dans la commande v6, l. 234).

## 3. Marqueurs restants (tous remplis par les mots de Lazar) et textes prêts pour le candidat (CLB-04)

| marqueur | occurrences | où | se remplit par |
|---|---|---|---|
| `GO_COURSE_V66` | 5 | en-tête (lignes de GO), 12.1 (ligne D1, D2, D3), 12.4 (commande), 13, 16 (bloc `plan-gele-v66`, ligne `go`) | l'identifiant de la ligne neuve, `GO-AAAA-MM-JJ-NN`, le même partout |
| `MOT_LAZAR_NL2` | 2 | en-tête, section 13 | le mot de Lazar, verbatim, suivi de « reçu le AAAA-MM-JJ vers HH:MM UTC (heure relevée par `date -u`) » |
| `EMPREINTE_GO_MD_APRES_NL2` | 1 | en-tête | sha256 de `registres/go.md` juste après l'inscription de la ligne |
| `MOT_LAZAR_NL1` | 1 | section 8, ligne C1 | le mot de Lazar, verbatim, avec l'heure relevée |
| `NOEUD_C1_SANS_RETENUE` | 1 | section 8, ligne C1 | le texte de l'option choisie (ci-dessous) |

**NL-1, textes prêts** (options du journal du brouillon 2, section 5) :
- option (a) : `NOEUD_C1_SANS_RETENUE` → « l'issue reste C1, avec la phrase en tête ; la proposition de plusieurs générations
  qu'elle ouvre nomme la fermeture de la boucle comme non éprouvée ». Rien d'autre.
- option (b), recommandée (0,6) : `NOEUD_C1_SANS_RETENUE` → « l'issue est C7 « la chaîne garde, boucle non éprouvée »
  (ligne C7, lue avant C1) » ; plus trois couples :
  1. insérer, juste avant la ligne qui commence par `| C1 | P1, P4 et P6 tenues, **et** V-1 à V-7 tenues`, la ligne :
     `| C7 | conditions de C1 tenues (P1, P4, P6 ; V-1 à V-7) **et** aucune carte réelle retenue en génération 1 (V-8) | **« la chaîne garde, boucle non éprouvée »** | les parties (a) et (b) de H-boucle tiennent (vraies survivantes, fausses refusées dans les deux générations) ; la partie (c) n'est pas éprouvée sur un contenu (sélection de la génération 1 vide : P5 sans copie, P6 sur {K1}) ; ouvre la proposition au directeur d'une course qui éprouve (c), non celle de plusieurs générations sur la foi de cette course ; ne dit rien de la classe non couverte ni des données réelles ; le programme gelé rend C1 dans ce cas, le lecteur du verdict écrit C7 (V-8) |`
  2. section 9 : « déclenché d'office si C1 (l'issue » → « déclenché d'office si C1 ou C7 (l'issue » (le programme lance déjà
     A1, qui lit C1) ;
  3. V-8 : « phrase en tête et issue de ce cas, ligne C1 » → « phrase en tête et issue C7 (ligne C7) ».
- option (c) : aucun texte prêt (dessin changé : texte neuf).

**Passages à régler au candidat en même temps** (ne dépendent pas des mots de Lazar, mais sont vrais du brouillon seulement) :
1. titre : « …, brouillon 3 » → « …, version {N} » ;
2. statut (bloc qui va de « **Statut : brouillon 3, non scellé » à « (section 12.1). ») → texte proposé : « **Statut : texte
   scellé du préenregistrement (R1), version {N}.** Brouillons 1 à 3 gardés intacts (`736e3fd6…`, `f87ad0e4…`, `04598de6…`) ;
   contre-lu (contre-lecture 1 du brouillon 2, puis vérification courte du différentiel jusqu'à ce texte : section 15) ;
   mots de Lazar sur NL-1 et NL-2 portés (sections 8 et 13) ; aucun marqueur ; passé au lanceur de l'organisme depuis une
   copie, validateur qui fait foi (section 12.2). **Aucune course réelle avant** : le dépôt de ce texte scellé et sa copie à
   l'octet dans l'arbre de l'organisme (section 12.2, point 4) ; les préalables sur la machine à `bwrap` (section 12.3). » ;
3. section 0, point 8 : retirer la proposition « **avant le scellement** : … différentiel ; » et écrire « ce texte est
   contre-lu et scellé (section 15) » ;
4. section 12.2, points 1 à 3 : au passé (mots portés ; contre-lecture et vérification courte faites), la phrase du
   validateur qui fait foi gardée telle quelle ;
5. section 15 : le paragraphe « **Vérification courte du différentiel jusqu'au texte candidat** : à faire… » devient son
   entrée (consigne, brouillon relu et son empreinte, rapport et son empreinte, traitement) ;
6. en-tête : rédacteur du candidat, heures, consigne, arbres (`main` du moment), registre (lignes neuves).

Puis : passage au lanceur depuis une copie (`--verifier-seulement`), vérification courte du différentiel, scellement.

## 4. Ce qui attend Lazar

- **NL-1** (issue C1 sans carte retenue) : options et recommandation inchangées (journal du brouillon 2, section 5 ;
  textes prêts ci-dessus). Aucun défaut (changement de critère).
- **NL-2** (ligne de GO neuve, 45 USD) : la ligne proposée au journal du brouillon 2, avec les précisions de CLB-10 (R-2253) :
  « machine jetable à bwrap **louée sous cette ligne, validée par l'essai à blanc --bac reel avant tout appel payant** » ;
  « préenregistrement de la course scellé (`preenregistrement-boucle-reelle-organisme-v1-v<N>.md`) » ; le fournisseur de
  la machine, si Lazar veut le garder (GO-2026-11-10-10 nommait Hetzner CPX32). Pas de barre verticale ; périmètre qui ne
  commence pas par « extension ». À lui dire aussi (CLB-13, sans nœud) : le registre des GO entier et les clés des deux
  relais seront posés sur la machine louée ; trois lignes de GO de 45 USD nommeront l'organisme, non cumulables par le seul
  mot de la ligne neuve.
- **Option non recommandée, dite à Lazar** (R-2253, CLB-03) : exiger P2 pour C1 serait un changement de critère ; le texte
  écrit le comportement du programme gelé (CLC-04).

## 5. Questions pour la mère

- **Q-1 (pire cas du devis)** : le devis (section 3.4) compte les fausses promues en génération 2 seulement ; si F1 à F4
  étaient promues **aussi en génération 1**, il y aurait 41 cartes testées (Kimi 494 appels et 33,80 USD, au-dessus de sa
  part de 33 ; Argon 43). Ce cas est une brèche déjà lisible avant l'étage (jugements écrits au relevé dès la sortie du juge) :
  un arrêt de plafond ou un refus du relais y donnerait C5 et « C2 (partielle) », jamais un masque. **J'ai écrit les nombres
  du devis (446, 39), comme décidé.** Recommandation : les garder et le dire au rapport de course (confiance 0,7).
- **Q-2 (prix du cache de Kimi)** : le relais Kimi exige `--prix-cache`, absent du devis ; je l'ai posé au prix d'entrée (2),
  qui ne sous-compte jamais. Recommandation : garder.
- **Q-3 (CLB-11)** : deux couples de lettre (B3-12, B3-15), hors des décisions nommées par la mère ; conformes au code et sans
  effet sur une issue. Recommandation : garder.
- **Q-4 (marqueurs neufs)** : pour suivre « les phrases qui dépendent des mots de Lazar restent en marqueurs », j'en ai
  ajouté trois (`MOT_LAZAR_NL2`, `EMPREINTE_GO_MD_APRES_NL2`, `MOT_LAZAR_NL1`) ; le lanceur refuse le texte tant qu'un seul
  reste. Recommandation : garder.
