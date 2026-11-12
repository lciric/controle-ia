# Fiche de lancement — rejeu de la cellule de juge redéfinie sur les 180 notations (120 textes) du pilote de T0.5 — v2

Écrite par un sous-agent de la lignée « session-depot » le 29 octobre 2026 (UTC), sous **GO-2026-10-29-04** (plafond
4 USD). Elle complète le devis `devis-rejeu-juges-v2.md` (même dossier) et tient lieu de préenregistrement (R1) : le
module `src/controle_ia/environnements/noter_rejeu_juges_v2.py` la reçoit par `--prereg` et en contrôle la forme
(sections exigées par `prereg.py`), le sceau et les citations ci-dessous. Le script de l'instance en lit les chemins
avant toute installation. **Rien n'est lancé par ce document.** Un marqueur reste, à remplir par la session : le
commit du code d'analyse (entre chevrons). Tant qu'il reste, ni le scellement (`prereg.sceller_prereg`) ni le lanceur
ni le script de l'instance n'acceptent la fiche. Corrigée le 29 octobre après la contre-lecture R2 (section
« Contre-lecture »).

Origine : lecture gelée et audit R4 du premier rejeu (`../rejeu-juges-v1/lecture-et-audit-r4-v1/lecture-rejeu-juges-v1.md`,
`8799f7d3800db7444a693677c3d7dfbb3b3e283becc41c88ae063748a877f9b8`) : aucune cellule à H_A ; meilleure, 8B « verdict
d'abord », 157 sur 180 ; échelles mal tenues, demi-points lus vers le bas par les jetons de tête, troncatures.

## Citations (une seule occurrence de chaque intitulé ; lues par le module et par le script de l'instance)

- Commit du code d'analyse : `5f13293a3d30c3a5b0c6b44274044a79a111a88a`
- Configuration du rejeu (empreinte canonique) : `186220d4ed000bf21c3a3597a1d5166b48653dbc75dd43aa0ed55cdd73fdcaaa`
- Chemin de la configuration du rejeu : `docs/notes/couche-2-preparation-v1/rejeu-juges-v2/config-rejeu-juges-v2.json`
- Run du pilote rejoué : `20261012-105125-t05-pilote-reel`
- Chemin du manifeste du pilote rejoué : `runs/20261012-105125-t05-pilote-reel/manifeste.json`
- Épisodes du pilote rejoué : `45616303dc740b66c42095cd5317a8ddd63e89123e64dd86490e43429c7cd15c`
- Chemin des épisodes du pilote rejoué : `diag/20261012-105125-t05-pilote-reel/episodes.json`
- Chemin de l'arrêt du pilote rejoué : `diag/20261012-105125-t05-pilote-reel/arret.json`
- Run des notations rejouées : `20261017-193648-t05-notations-reel`
- Manifeste des notations rejouées : `9f143f7c1c9fd9d75f21807a0fa41035ae7110abe686fc7819130d3f6b435d38`
- Chemin du manifeste des notations rejouées : `runs/20261017-193648-t05-notations-reel/manifeste.json`
- Notations rejouées du 8B : `b103835bcd3bfc3117a53e335be6f37a1259102cc2a2a134acfc6e114cb3f1c4`
- Chemin des notations rejouées du 8B : `diag/20261017-193648-t05-notations-reel/notations-8B-decisives.json`
- Notations rejouées du 3B : `51548526c7590231b76473c2b4c9e619a092616b5f948830e735c466b037adab`
- Chemin des notations rejouées du 3B : `diag/20261017-193648-t05-notations-reel/notations-3B-decisives.json`
- Tâches du pilote : `287e83485cba550098b80db809589398d8f2826c02dfa9cc2719a1063795d5aa`
- Chemin des tâches du pilote rejoué : `donnees/t05-pilote-v1/taches-pilote-60-v1.json`
- Consigne du verdict d'abord à échelles : `9bb0af347d29bacdc0aa1b870d1fd9f9f9d57c5f3e6039cd539f38b9fd2dd216`
- Entropie : `37114382722285754842192283631495258186` (celle du pilote et des notations rejouées, reprise telle quelle)
- Tests attendus : `226` (suite ciblée du script de l'instance : `tests/test_noter_rejeu_juges_v2.py`,
  `test_noter_rejeu_juges_v1.py`, `test_noter_pilote_a.py`, `test_pilote_a.py`, `test_manifeste.py`,
  `test_scellement.py`, `test_prereg.py` ; dernière ligne « N passed[, M warning(s)] in X s », rien d'autre ; compte
  du 29 octobre, après les corrections de la contre-lecture R2 : 219 relus, plus 5 essais du contre-lecteur et 2
  essais de l'auteur)

Les citations du pilote, des notations rejouées, des tâches et de l'entropie sont celles de la fiche v1
(`7b6b89d9f7808760047d9c8135856c05a4ee1f199b85ad85792ed8a1c7f7509a`), acceptées par les gardes du module au run v1 du
29 octobre ; le rédacteur ne les a pas revérifiées contre les fichiers (`runs/` et `donnees/` hors de sa lecture) : **à
vérifier par la session (`sha256sum -c`) avant le scellement.** Configuration et consigne : empreintes recalculées par
`lancer_pilote_a.empreinte_config` et par le module (`EMPREINTE_CONSIGNE_V2`).

## Hypothèse

Question d'instrument, sans signe recherché (R3). Pour la cellule redéfinie « verdict-echelles » du juge 8B
(décisive), sur les 180 notations décisives du pilote, qui portent sur 120 textes (60 notés deux fois) :
- H_A : au moins 0,99 des scores sont finis et appuyés ;
- H_B : moins de 0,99 ; la cellule n'est pas encore celle de la banque.

La cellule du 3B (même variante) est **descriptive** : elle ne tourne que si le temps restant couvre sa durée maximale,
et sa lecture ne décide rien (critère non décisif).

Cellule redéfinie (décision de Lazar, GO-2026-10-29-04) :
- **verdict d'abord** : l'invite b0 du pilote, suivie de la consigne v2 (empreinte citée) ;
- **l'échelle de chaque critère écrite à côté de lui** : la consigne donne, pour chaque critère, la ligne
  « NOM (lo to hi): <integer> » (par exemple « BALANCE (0 to 3): <integer> », « REDUNDANCY_PENALTY (-2 to 0):
  <integer> »), et la phrase « Only these values are allowed: a whole number from the lower to the upper bound written
  next to the criterion, both bounds included. No half points, no decimals, no fractions, no value outside the
  criterion's own scale, and nothing else on the line. » ;
- **valeurs admises seules** : à la lecture, une valeur compte seulement si elle est un entier de l'échelle propre du
  critère, suivi d'une fin de ligne (section « Métrique ») ;
- génération bornée au bloc : chaque réponse s'arrête dès que la ligne du dixième critère est close, ou à son jeton de
  fin, ou à 256 jetons.

## Prédiction chiffrée et signe attendu

Aucune issue n'est visée. Repères (v1, RAPPORTÉS : `lecture-rejeu-v1.json`, `63b28eaf…`, cellule 8B « verdict
d'abord ») : 157 sur 180 finis et appuyés (107 sur 120 textes), dont 21 à note écrite non admise (19 fois « 4 hors de
[0, 3] », 8 notes non entières), qui ne seraient plus appuyés sous la définition v2 si le juge les écrivait encore ; 8
blocs inachevés (notes sans nom de critère) ; 137 sur 180 finis à la note écrite.
- **8B (décisif).** SUPPOSÉ : k entre 150 et 180 sur 180. L'échelle écrite à côté de chaque critère vise la cause
  dominante ; les blocs sans noms de critère et les sorties de format restent possibles. Probabilité de H_A
  (k ≥ 179) estimée à ≈ 0,3, sans fondement mesuré ; H_B plus probable. H_A ne peut pas être tranchée sur 120 textes
  (120 sur 120 donne une borne basse de 0,969) : le rejeu peut réfuter H_A, pas l'établir.
- **3B (descriptif).** SUPPOSÉ : k entre 110 et 170 (v1 : 115, notes hors échelle dominantes).
- **Contrôle de l'instrument.** SUPPOSÉ « aligné » : chaque note écrite admise a été tirée de la loi même que la
  lecture rend (température 1, loi entière).
- **Audit R4.** SUPPOSÉ : peu de déclencheurs ; « trop favorable : n sur n » possible si H_A.
- **Accord** (mesure, jamais critère : réserve (i) de conv-audit). SUPPOSÉ : 0,7 à 0,9 des critères (v1 : 0,74).
- **Rythmes.** SUPPOSÉS (devis, § 3) : 8B ≈ 6 s par notation (18 minutes) ; 3B ≈ 3,7 s (11 minutes).

**Comparabilité avec la v1 (contre-lecture R2, CLR2-05).** Sur un même texte, la masse v2 est au plus la masse v1, à
chaque critère : la v2 exige la fin de ligne après la valeur, compte l'espace après les deux-points et ne lit plus les
jetons de tête. La consigne a aussi changé. **Aucun écart entre le k de la v2 et les 157 de la v1 ne se lit donc comme
un effet de la consigne, ni comme une amélioration ou une dégradation de l'instrument** : seul compte le critère gelé,
appliqué à la v2. Le choix de compter l'espace est mesuré sur les textes de la v1 : 1 720 lignes sur 1 720 des blocs
complets ont une espace après les deux-points, chez le 8B comme chez le 3B (contre-lecture R2, outil `formes_v1.py`) ;
il ne pénalise que des écritures que la lecture écrite stricte refuse aussi (« ␣** », « ␣- » sur une échelle
positive).

## Métrique

**Lecture par la probabilité du jeton de verdict, valeurs admises seules** (module, `lire_par_probabilite_v2`). D-S13
est close sur son texte comme en v1 (fiche v1, section « Métrique ») : score continu (une espérance), sans ex æquo.

Pour chaque critère de la rubrique H.4 :
- la lecture se fait après les deux-points de la **dernière occurrence** du critère dans le bloc. Les deux formes se
  lisent : « NOM (lo to hi): v » et « NOM: v » (`_LIGNE_V2`). Rien n'est retiré après les deux-points : ni
  astérisque, ni soulignement ;
- chaque valeur admise v de [lo, hi] a sa suite de jetons c, encodée à partir du jeton qui porte le premier caractère
  après les deux-points (séparateur compris, comme v1 ; position de décision : la première où ces suites divergent) ;
- la probabilité de v est **P(c entière) × P(fin de ligne | c)** : le produit des probabilités conditionnelles de tous
  les jetons de c depuis ce jeton (l'espace commune comprise), fois la somme des probabilités des jetons terminaux après
  c. Jetons terminaux : ceux qui ne portent que des espaces, des tabulations et au moins un saut de ligne, plus les
  jetons de fin de tour (`jetons_terminaux`) ;
- donc **aucune lecture par les jetons de tête** : « 2.5 », « 10 », « 3/5 », « 3** », « 4 » sur [0, 3] ne comptent pour
  aucune valeur admise ;
- les lois sur le chemin écrit viennent d'une passe principale ; celles hors du chemin, du cache des clés et valeurs
  rogné à la longueur commune puis prolongé des seuls jetons de v. Égalité avec des passes complètes vérifiée **en
  simple précision** (modèle jouet à 1e-4 près ; contre-lecture R2 : 1,2e-5, vocabulaire du vrai tokeniseur). **Au
  réel (bfloat16), les deux chemins numériques diffèrent de l'ordre de 1e-2 sur le logarithme de la masse** (jusqu'à
  0,16 sur des logits très contrastés ; probabilités renormalisées à moins de 1,5e-3 : contre-lecture R2, CLR2-04),
  sans correction : seule une masse à la limite de 0,5 peut en être changée ;
- masse admise M : somme de ces probabilités ; loi renormalisée sur les valeurs admises ; note lue : l'espérance ;
  score lu : 100 × max(0, somme des dix espérances) / 33. **Jamais de moyenne ni de médiane sur des jetons.**

**Score fini et appuyé** d'une notation (même définition que v1, M redéfinie ci-dessus) : les trois conditions
réunies, sinon aucun score (jamais imputé), motif consigné :
- fenêtre complète : les dix critères apparaissent dans la réponse ; la lecture porte sur le bloc qui va du début de la
  réponse à la fin de la ligne où le dixième apparaît pour la première fois ;
- les dix positions existent : critère présent, valeur écrite après les deux-points ;
- à chacune des dix positions, M ≥ 0,5 (`masse_min_appui` ; exigé au réel par le module).

**Complétude**, **contrôle de l'instrument** (probabilité brute de la note écrite, p × M, sous 0,001), **lectures en
échec de l'instrument**, **audit R4** : définitions et fonctions de v1 (`lire_cellule`, importée), appliquées à la cellule
« verdict-echelles » de chaque juge. La note écrite est lue **strictement** (`lecture_ecrite_v2`) : admise seulement si
la ligne porte, après les deux-points, un entier canonique de l'échelle, et rien d'autre qu'espaces ; c'est l'événement
même que M mesure.

**Accord** (mesure, jamais critère) : sur les notations où note écrite stricte et lecture donnent toutes deux un score,
part des critères où la valeur la plus probable égale la note écrite ; écart absolu des scores sur 100.

**Descriptifs** : arrêts de la génération (« bloc clos », « fin », « budget ») ; lignes écrites sous la forme à
échelle ; finis sans appui ; finis écrits ; masses minimale et maximale ; rythmes (secondes par notation, passes,
jetons générés, pic de mémoire).

## Seuil

- Complétude, cellule décisive (8B) : **0,99**.
  - Lecture ponctuelle sur les 180 notations : **H_A si k ≥ 179** ; H_B sinon.
  - « Tranchée » sur les 120 passe-0 (Wilson à 95 %) : H_B tranchée si **k0 ≤ 116** ; H_A jamais tranchée.
- Appui : M ≥ **0,5** à chaque position.
- Contrôle de l'instrument : part improbable (probabilité brute) ≤ **0,02**.
- Lectures en échec de l'instrument : au plus **0,02 × n**.
- Accord : ≥ 0,90 « concordant », sinon « discordant » ; descriptif, aucune décision.

## Plan d'analyse

1. Récupération de la branche `calcul/rejeu-juges-v2`, contrôle des sceaux et du rattachement au manifeste.
2. Lecture par la commande `python -m controle_ia.environnements.noter_rejeu_juges_v2 --lire <run>`, et par elle seule,
   y compris après un arrêt (phases écrites et scellées lues ; statuts du résumé, sinon de l'arrêt, sinon d'aucun
   fichier ; champ `source`). Elle écrit `diag/<run>/lecture-rejeu-v2.json`, scellé ; champ `lecture_decisive` : la
   lecture de la cellule du 8B.
3. Pour chaque cellule écrite : complétude (k, n, k0 sur 120, intervalles, H_A ou H_B, tranchée ou non), instrument,
   échecs, descriptifs, audit R4 (déclencheurs, vingt notations tirées par la clé `audit-r4/<juge>/verdict-echelles`),
   accord, rythme, rôle (« décisive » ou « descriptive »). Cellule non écrite : « non mesurée », avec son statut.
4. Audit R4 de chaque cellule où un déclencheur se lève : la session relit les notations tirées ; le résultat est une
   réserve consignée, jamais une autre lecture.
5. Compte rendu à Lazar : verdict d'abord (la cellule du 8B tient-elle H_A ?), puis les réserves (i) et (ii)
   ci-dessous, puis la cellule descriptive du 3B.

## Critères de lecture gelés

1. **Score fini et appuyé** : la définition de la section « Métrique », sans autre tolérance (ni troncature tolérée,
   ni note ramenée à la borne, ni critère imputé, ni jeton de tête).
2. **Complétude** : H_A si k / n ≥ 0,99, H_B sinon, **pour la cellule du 8B seule** ; « tranchée » sur les 120 passe-0.
   La cellule du 3B est lue de la même façon, mais **descriptive** : elle ne décide rien, et son absence
   (« non-commencé ») n'est pas un écart.
3. **Instrument** : « désaligné » ou lectures en échec au-delà de 0,02 × n : la cellule se lit « non concluant », jamais
   tranchée ; audit R4 déclenché ; lecture brute consignée.
4. **Audit R4, symétrique** : déclencheurs de v1 (n sur n ; masses toutes au-dessus de 0,99 ; cellule à 0 ou presque ;
   masses toutes sous 0,01 ; scores écrits sans score appuyé au-delà de 0,05 × n ; scores appuyés à note écrite non
   admise au-delà de 0,02 × n ; instrument désaligné ; lecture en échec) ; vingt notations tirées par la graine de la
   clé de la cellule, dérivée de l'entropie (R9), avant toute lecture.
5. **Réserve (i) de conv-audit** : l'accord entre la lecture et la note écrite **n'est pas un critère de H_A**, seulement
   une mesure. Un accord faible ne retire pas H_A ; un accord fort ne la donne pas.
6. **Réserve (ii) de conv-audit** : la redéfinition est tirée de l'audit des **mêmes 180 textes**. Ce rejeu vérifie
   l'instrument, pas sa généralisation : un H_A ici ne vaut pas pour des textes neufs. La généralisation se vérifie sur
   textes neufs à la tranche 0 du pilote (GO-2026-10-29-05). Le compte rendu le dit en même temps que le verdict.
7. **Ce que la lecture décide** : si la cellule redéfinie du 8B tient H_A sur ces 180 notations, rien d'autre. Son
   adoption dans la banque est une proposition à Lazar.

## Liste d'arrêt

Avant le manifeste (aucun run créé, code 1 du module) :
- configuration incomplète, à clé inconnue ou hors bornes : variante autre que « verdict-echelles », juge décisif
  absent ou pas en première phase, phase en double, durée hors de ]0 ; durée globale], durée globale au-delà de
  3 600 s, budget de verdict hors de [64 ; 512], appui hors de [0 ; 1] ou **différent de 0,5 au réel**, invite autre
  que b0 ;
- run réel sans fiche (R1) ; run réel sans échéance externe, ou échéance passée ou non finie ;
- fiche non scellée ou non conforme ; commit du code différent de l'arbre gelé ;
- citation absente, en double ou différente : configuration, runs, manifeste et notations rejouées, épisodes,
  **consigne v2** (intitulé « Consigne du verdict d'abord à échelles »), tâches, entropie ;
- invites altérées ; pilote dans un autre état que celui constaté ;
- notations rejouées absentes, non scellées ou rattachées à un autre manifeste ; paramètres des juges différents ;
- demandes et notations désalignées (clé, empreinte de l'ensemble, nombre 180) ; lecture écrite refaite différente du
  score rejoué ; entropie différente de celle du pilote.

Après le manifeste (`arret.json` scellé, puis arrêt) :
- format d'un juge différent de celui du début du pilote ;
- **aucun jeton de fin de ligne** dans le vocabulaire ;
- **encodage des valeurs différent de celui que suppose la lecture** : garde de v1, plus, pour les deux formes de ligne
  et chaque valeur de chaque échelle (94), la valeur en contexte égale à la valeur à part et suivie d'un seul jeton,
  terminal ; « \n » un seul jeton, terminal. **Éprouvée sur le vrai tokeniseur du 8B** (contre-lecture R2, CLR2-06 :
  `tokenizer.json` d'empreinte `79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4`, celle de la révision
  `0e9e39f2` consignée en R-067) : 47 sur 47 et 94 sur 94 valeurs, 204 jetons de fin de ligne ou de fin de tour. Le 3B
  a, à sa révision `0cb88a4f`, le même tokeniseur (R-068) ; la copie publique relue par le contre-lecteur (empreinte
  `6b9e4e7f…`, non empreintée contre la révision) passe aussi, sans faire foi ;
- format, jetons de fin de ligne ou encodage du 3B rechargé hors ligne différents (les fins de tour du modèle chargé,
  qui s'ajoutent à celle du tokeniseur, ne sont pas une différence : elles entrent dans les terminaux de sa lecture) ;
- **cache des clés et valeurs absent**, de longueur inattendue, ou rognage impossible (aucun repli sur des passes
  complètes) ;
- signal TERM (délai externe ou plafond de l'amorce), même avalé par une bibliothèque ;
- toute panne : mémoire, réseau, chargement.

Non-arrêts consignés : phase « échue » (aucun fichier, la suivante commence) ; phase « non-commencé » ; notation sans
score, avec motif.

Chaîne de l'instance : branche de résultats déjà présente ; fiche ou fichier cité absent, ou sceau non conforme ;
marqueur restant dans la fiche ; poussée initiale refusée ; carte indisponible ; tests en échec ou nombre différent de
« Tests attendus » ; **garde d'encodage préalable en échec** (tokeniseurs seuls des juges, avant la suite de tests :
contre-lecture R2, CLR2-06) ; **délai du run sous 45 minutes, c'est-à-dire moins de 58 minutes avant le plafond de
l'amorce** (délai du run = temps restant − 13 minutes ; la phase décisive ne tiendrait plus).

Lanceur : commit absent de `origin/main` ; pièces absentes ou non scellées ; marqueur restant ; commit du code non
ancêtre du commit lancé ; **arbre gelé du commit lancé différent de celui du commit du code** (mêmes chemins que la
garde du module : contre-lecture R2, CLR2-01) ; jeton absent ; garde de calcul refusée (`GO_ID=GO-2026-10-29-04`) ; autre instance sur le
compte ; crédit sous 4,50 USD ; aucune offre conforme (A100 SXM4 80 Go, ≤ 1,43 USD/h, fiabilité ≥ 0,98, CUDA ≥ 13.0,
mémoire vive ≥ 64 Go, téléchargement ≤ 0,01 USD/Go).

## Bornes de temps

- **Phases**, dans l'ordre de priorité de la configuration : 8B, durée maximale 35 minutes (2 100 s) ; 3B, 20 minutes
  (1 200 s). Une phase ne commence que si le temps restant avant l'échéance globale couvre sa durée maximale.
- **Échéance globale** du module : la plus proche de début + 55 minutes (3 300 s, configuration) et de l'échéance
  externe passée par le script de l'instance (délai externe du run moins 6 minutes) ; consignée dans `resume.json` et
  `arret.json`. Dernier lot : ≈ 1,5 minute au pire (SUPPOSÉ) ; il finit avant le TERM.
- **Délai externe du run** : 65 minutes au plus, borné par le temps restant avant le plafond de l'amorce moins
  13 minutes ; sous 45 minutes (moins de 58 minutes avant le plafond de l'amorce), le run ne commence pas.
- **Risque accepté : la phase décisive est « tout ou rien » à 2 100 s** (contre-lecture R2, CLR2-02). Si le 8B dépasse
  35 minutes, aucun fichier n'est écrit et la cellule décisive est perdue (≈ 1,3 USD dépensés) ; la borne n'est pas
  allongée. Calcul : rythme v1 du 8B en verdict d'abord, 6,12 s × 180 ≈ 1 100 s (RAPPORTÉ, `resume.json` v1,
  `a2af5d17…`) ; marge 2 100 / 1 100 ≈ 1,9. Le pire supposé de la v2 (lots au plafond de 256 pas) est ≈ 30 minutes ;
  la lecture des branches par le cache n'a jamais été chronométrée sur A100. Dans ce cas, le 3B ne tournerait pas non
  plus (il lui faudrait 35 + 20 minutes après les chargements).
- **Amorce** : 120 minutes, puis KILL 5 minutes plus tard.
- **Arrêt de l'instance** par la session, par identifiant (R10), dès la fin de l'amorce, au plus tard à la création
  + 8 400 s (heure écrite par le lanceur).
- **Réveils de garde** : la session programme deux réveils d'elle-même dès la création, à la création + 135 et
  + 150 minutes (heures écrites par le lanceur dans `lancement.txt` ; contre-lecture R2, CLR2-09 : la fin au pire de
  l'amorce, KILL compris, tombe à + 130 minutes, et sa poussée ne doit pas être coupée) ; chacun inventorie, arrête par
  identifiant si besoin, consigne dans `registres/arrets.md`.
- **Facture** (devis, § 4) : attendu ≈ 1,5 USD ; pire cas ≈ 3,7 USD ; session perdue, arrêt par le second réveil
  (≈ 152 minutes) ≈ 3,9 USD ; sous le plafond de 4 USD.
- **Seconde instance** (contre-lecture R2, CLR2-07) : permise seulement si la première est perdue par l'hôte avant la
  première ligne `PROGRES` **et a coûté au plus 0,20 USD** (pire de la seconde ≈ 3,7 USD) ; sinon, nouveau GO.

## Manifeste et graines (R9)

Run `AAAAMMJJ-HHMMSS-rejeu-juges-v2-reel`. Le manifeste (`runs/<run>/manifeste.json`, scellé) porte la configuration
et son empreinte, les versions, le commit, cette fiche (chemin et empreinte), la commande, et les **graines**, dérivées
par `numpy.random.SeedSequence` de l'entropie du pilote. Clés : `rejeu-v2/verdict-echelles/<clé du pilote>`, une par
notation et par juge d'une phase (360), plus `modele-jouet`, égale à celle du pilote. Les graines de l'audit R4
(`audit-r4/<juge>/verdict-echelles`) se dérivent de la même entropie, par la même fonction, avant toute lecture.
Résultats : `diag/<run>/rejeu-<juge>-verdict-echelles.json`, `resume.json`, `arret.json` s'il y a lieu, tous scellés
et rattachés au manifeste. Rien n'est écrit dans les dossiers du pilote, des notations rejouées ni du rejeu v1.

## Ce que ce rejeu ne décide pas

- La généralisation de la cellule redéfinie à des textes neufs (réserve (ii) : tranche 0 du pilote).
- L'adoption de la cellule dans la banque : proposition à Lazar après lecture.
- La justesse des juges (ni sensibilité ni spécificité) ; aucun chiffre opposable (R7).
- Aucune lecture de T0.5 ni du rejeu v1 n'est refaite ; le verdict des notations (`d861605c…`) et la bascule vers le
  plan B (N-022) restent tels quels.
- Aucun changement de modèle, d'invite publiée ni de rubrique : la consigne v2 est un ajout déclaré, à l'empreinte
  citée.
- Rien sur le 3B qui décide : sa cellule est descriptive.

## Contre-lecture

- **Contre-lecture 1** : sous-agent neuf (R2), auteur ni du code ni de la fiche, 29 octobre 2026, 07:24 à 08:21 UTC.
  Fichiers donnés : fiche, devis, configuration, module, essais, amorce, script de l'instance, lanceur, fonctions
  importées. Brouillon relu : commit `cff3d90a`, fiche
  `325753691a973c872c609d837d426f78736967274b8c78475d6ed379ed6bba65` (empreintes des huit fichiers dans le rapport).
  Rapport : `contre-lecture-rejeu-juges-v2.md` (bloc-notes de la session, dossier `relecture-rejeu-v2/`, à verser dans
  ce dossier), empreinte `b156da9ff1a3692ef9db17e2352924ce92fc5f8fe76c7d3917ee823455c13fe5`. Verdict : « lançable après
  corrections », aucun bloquant.
- Traitement, par l'auteur, le 29 octobre (une ligne par constat) :
  - CLR2-01, majeur, arbre gelé non contrôlé par le lanceur : **corrigé** ; le lanceur compare l'arbre gelé (chemins de
    `CHEMINS_GELES`) du commit du code et du commit lancé ; banc devant le faux `vastai` : cas sain code 0, code changé
    code 2 sans création.
  - CLR2-02, mineur, phase décisive « tout ou rien » : **risque accepté**, borne inchangée, calcul écrit (« Bornes de
    temps »).
  - CLR2-03, mineur, borne des 45 minutes mal dite : **corrigé** (« moins de 58 minutes avant le plafond de l'amorce »),
    fiche et devis.
  - CLR2-04, mineur, précision en bfloat16 : **écrit** (« Métrique »).
  - CLR2-05, mineur, comparabilité avec la v1 : **écrit** (« Prédiction »), avec la mesure du choix de l'espace.
  - CLR2-06, mineur, garde éprouvée sur un tokeniseur simulé seulement : **écrit** (« Liste d'arrêt ») ; option faite :
    garde d'encodage préalable sur les tokeniseurs seuls, avant la suite de tests de l'instance
    (`--controle-encodage`, essai cas sain et artefact).
  - CLR2-07, mineur, seconde instance floue : **chiffré** (première ≤ 0,20 USD), fiche et devis.
  - CLR2-08, mineur, cinq gardes sans artefact : **corrigé** ; les cinq essais du contre-lecteur versés ; « Tests
    attendus » recomptés.
  - CLR2-09, mineur, premier réveil sur la fin au pire de l'amorce : **corrigé** ; réveils à + 135 et + 150 minutes
    (lanceur, fiche, devis).
  - Constat de l'auteur pendant les corrections (non vu par la contre-lecture, absent en mode jouet) : au réel, le 3B
    rechargé hors ligne porte les fins de tour du modèle en plus de celle du tokeniseur ; le module relu aurait arrêté
    tout le run (phase décisive comprise) sur « encodage chargé hors ligne ≠ » avant toute phase. **Corrigé** : seuls
    les jetons de fin de ligne et le contrôle d'encodage doivent être égaux, et la lecture du 3B prend les terminaux de
    son format chargé ; essai (échoue sur le module relu, passe sur le corrigé).
