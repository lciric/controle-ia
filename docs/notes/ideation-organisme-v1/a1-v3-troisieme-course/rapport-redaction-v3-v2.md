# Rapport de rédaction v3, v2 — lanceur durable v2 et brouillon 2 du texte v3 (troisième course d'A1-v3)

Rédacteur-développeur neuf : il n'a écrit ni le texte v3, ni le lanceur v1, ni les sondes. 5 novembre 2026, de 06:22 à 06:54 UTC
(heures relevées par `date -u`), après un redémarrage du conteneur (rien d'antérieur n'existait de ce travail). Consigne :
`consigne-developpeur-lanceur-durable-v2-v1.md` (sha256 `75aa4841…`, sans compagnon), et deux messages de la mère (06:22 :
reprise ; 06:42 : Argon rendu, risque de la clé, cas HTTP 402, lignes de GO par registre). Interdits tenus : aucun `.sha256`
écrit, aucun fichier existant modifié, aucun commit ni poussée de ma part (la mère a committé des instantanés non scellés de mes
fichiers : `c263b0fc`, `074d1256`, `add136a3`), rien écrit sous `donnees/`, aucun réseau, aucune location, aucun appel de modèle,
aucune clé lue ; toute commande sous `timeout 900 nice -n 10`.

**Verdict.** Le lanceur durable v2 loue une machine Vast **à une carte** (« gpu », une carte, au plus 0,40 USD/h) sous
**GO-2026-11-05-03**, la course restant sous **GO-2026-11-04-06** ; il porte les corrections des sondes v2 à v10 sur la location,
l'inventaire, la minuterie, le registre des GO et le versement (section 2, liste fermée). **131 essais passent** (82 de la v2, 49
de la v1 rejoués), aucun sauté. Le brouillon 2 du texte v3 = brouillon 1 + 10 couples appliqués par script ; la ligne 545 est
intacte. **Le cas HTTP 402 à solde nul n'est pas établi sans risque** : la commande d'Argon gelée n'a pas pu être relue ici
(section 5).

## 1. Fichiers et empreintes

| fichier (dépôt privé, sauf mention) | sha256 |
|---|---|
| `src/controle_ia/hote_durable_a1_v3_v2.py` (856 lignes) | `b8287d52b3cca962ecb4e4c64e5137f43069179311461c0e47f72d513b02486f` |
| `scripts/amorce_hote_durable_a1_v3_v2.sh` | `33e87f4568564096e0696e252be9814adec0d140949dc15cd0fe8f191cf5b425` |
| `tests/test_hote_durable_a1_v3_v2.py` (711 lignes, 82 essais) | `06deeed7312df8d750eb4f6bfbfda27e8bae60952d748c4a0cbc0a0240973148` |
| `docs/notes/ideation-organisme-v1/a1-v3-troisieme-course/couples-brouillon2-v3-v1.json` | `e1be43e28367211a7ab86299e80dc335cc4b38e432ae7430979fbd89911bc96d` |
| `…/a1-v3-troisieme-course/appliquer-couples-brouillon2-v1.py` | `d66ea27f21b9b59d281f4100a4ab0cd5e99b4ba53ad3b1a714be49c8bc1d7dd9` |
| `…/a1-v3-troisieme-course/sortie-appliquer-couples-brouillon2-v1.txt` | `13a874d31deaf39b4192dbe2055be015d8dade83d1ea9a70863f8e9515372788` |
| `…/a1-v3-troisieme-course/preenregistrement-attaque-goodhart-v3-v3-brouillon2.md` (2 148 lignes) | `86ad379b4ebf45b505bc5597501a09a773a37686749b2b41b0c1089f0f91ee1e` |
| bloc-notes `…/scratchpad/lv2-a1v3/sorties/essais-lanceur-v1-et-v2.txt` | `eaae879f737dfb4309f1816d9604070959707274a59d27cc9654eaf46f28d53d` |

Source vérifiée avant tout : brouillon 1 `6e65136a…` ; compagnons des pièces vérifiés depuis leur dossier (lanceur v1, sonde v10,
amorces, essais, additifs). Ce rapport ne peut pas porter sa propre empreinte.

**Dépendances.** La v2 reprend le code éprouvé de la sonde v10 (client de Vast du pilote, catégorie de la réponse de création,
vérification d'offre, `ls-remote` sous mandataire) et la séquence de la v1 sur la machine. Le commit du dépôt privé passé à la
location (`COMMIT_PRIVE`) doit donc porter **quatre** modules : `hote_durable_a1_v3.py`, `hote_durable_a1_v3_v2.py`,
`sonde_hote_durable_a1_v3.py`, `sonde_hote_durable_a1_v3_v10.py` (l'amorce v2 refuse de partir s'il en manque un). En fichier
seul (`python3 -I -B …`), la v2 charge la v10 par son chemin et reprend **son** objet `h` : une seule classe `Refus` (essai
`test_fichier_seul_une_seule_classe_refus_et_offre`).

## 2. Liste fermée des corrections portées (une ligne par point ; additif d'origine)

**Location (pilote)**
1. M2 (additif 2) : `vastai destroy instance <ID> -y` partout où le pilote détruit.
2. M3 (additif 2) : `VAST_API_KEY` exigée par son nom (`env -i`), transmise au seul sous-processus `vastai`, masquée.
3. f1 (additif 2), f-a (additif 3) : aucune sortie brute de `vastai` écrite ; le code seul, ou la catégorie de la réponse.
4. f2 (additif 2) : liste des clés de modèle interdites commune au module et à l'amorce (`MOTIF_AMORCE`), **sans** `CLE_ARGON`.
5. f6 (additif 2), f-g (additif 3) : `--storage 30` dans la recherche (R-1527 : prix de la recherche = prix facturé).
6. f7 (additif 2) : `GO_ID=GO-2026-11-05-03` en tête de la ligne de location, exigé par `louer`.
7. m3 (additif 2), m-1 (additif 4) : marqueur « création incertaine » ; seconde location refusée ; gardes d'avant l'appel sans marqueur.
8. m4 (additif 2) : sous-commande `offre` (la moins chère des conformes) ; `louer` refuse une offre qui ne l'est pas.
9. M-1 (additif 4) : délai de `vastai` rendu en refus sans ligne de commande ni environnement ; marqueur posé.
10. f-4 (additif 4) : `vastai --version` = 1.8.3 exigé par la commande (section 7).
11. v5 (b) (additif 5) : mémoire réelle relevée par l'amorce (`MemTotal`), versée ; sous 2 Go, rien ne part.
12. v6 (a) (additif 6) : variables du mandataire transmises si présentes, aucune autre, valeurs masquées.
13. v6 (b) (additif 6) : certificat refusé = appel non parvenu à Vast, sans marqueur.
14. v7 (a) (additif 7) : réponse de création catégorisée (contrat, « no_such_ask », erreur de Vast, illisible) ; `error` et `msg` seuls, tronqués, masqués.
15. v7 (c) (additif 7) : longueurs de `--args`, `--env` et de la commande écrites au journal.
16. v8 (a) (additif 8) : sortie standard puis sortie d'erreur ; le code de sortie ne décide jamais seul.
17. v8 (b) (additif 8) : sur « no_such_ask », au plus 4 autres offres conformes par prix croissant, chacune revérifiée, borne recalculée.
18. v9 (a) (additif 9) : offre `resource_type` « gpu » (« disk » refusé), `num_gpus` = 1, `cpu_ram` ≥ 8 000 Mo, cœurs ≥ 4, disque ≥ 30, fiabilité ≥ 0,98, prix ≤ 0,40 USD/h.
19. v9 (c) (additif 9) : recherche `num_gpus=1 … cpu_ram>=8 …` (Go dans la requête, 8 000 Mo dans la réponse brute).
20. m2 (additif 2) : état écrit à la création (`.etat.json`) et ligne pour `registres/etat.md` ; signe de vie attendu avant T0 + 30 min.
21. f-b (additif 3) : la ligne pour `registres/etat.md` renvoie à `controler`, jamais à un `destroy` direct.

**Inventaire**
22. M-A (additif 3) : `controler` rend 5 (« recontrôler ») tant que la machine est listée ; contrôles à T0 + 40 min et après l'échéance finale.
23. f-6 (additif 4), v7 (b) (additif 7) : délai ou échec de `ls-remote` (variables du mandataire transmises) = code 6, jamais « pas de signe de vie ».
24. m2 (additif 2) : sans signe de vie à T0 + 30 min, `controler` détruit par l'identifiant, avec `-y`, puis vérifie par l'inventaire.
25. f8 (additif 2) : étiquette contrôlée par la minuterie, la machine et le pilote ; 58936096, 58936099, 58936100 jamais touchées.
26. v10 (b) (additif 10) : sous-commande `facturation` (quatre champs seulement : `actual_status`, `dph_total`, `disk_usage`, `storage_cost`).
27. M3 et v6 (a) appliqués à `inventaire` : client du pilote, champs filtrés de la v1 (jamais l'environnement des machines).

**Minuterie**
28. M1 (additif 2) : minuterie lancée en tout premier (`setsid`, sans Python), `DELETE` avec la clé d'instance, échéance gardée sur disque.
29. M-B (additif 3) : échéance absolue posée par le pilote (`ECHEANCE_UTC_S`) ; la minuterie prend le minimum ; course bornée en conséquence.
30. m-a (additif 3), partie minuterie : le `DELETE` recommence chaque minute jusqu'à la fin de vie, jamais de `PUT stopped`, puis ALARME.
31. m-b (additif 3) : le processus principal ne sort qu'après la fin de la minuterie (au plus 5 min après la fin de vie).
32. m-c (additif 3) : `curl` exigé par l'amorce ; la minuterie passe par `python3` s'il manque, avec une ALARME.
33. m-2, f-1 (additif 4) : amorce et chaque `apt-get` sous `timeout` borné par la fin de vie ; `curl` installé après la minuterie.
34. f-2 (additif 4) : la borne de dépense compte l'attente finale (`cout_maximal_usd`).
35. f-d (additif 3), m5 (additif 2) : clone partiel (`--filter=blob:none --depth 1`) et `sparse-checkout` de `scripts` et `src/controle_ia`, sous `timeout`.
36. f-e (additif 3) : crochets d'essai contrôlés (racine absolue, adresse en `https://`, durées entières et bornées par les valeurs réelles).
37. m1 (additif 2) : durée et coût de la machine comptés depuis le départ du conteneur.

**Registre des GO**
38. v9 (b) (additif 9) : GO vérifié par le pilote, par la machine et par l'amorce ; en v2, deux GO à montant exact (35 et 400 USD).
39. v10 (a) (additif 10) : canal pris en clone partiel sur 200 commits, commit vérifié sur la branche, fichiers lus par `git show` **avec** l'aide d'identification, aucun doublon.

**Versement**
40. m5 (additif 2) : aucun clone entier de `main` (son arbre pèse 2,4 Go, 14 565 fichiers) ; signe de vie sur une branche orpheline.
41. m1 (additif 2) : versement borné (4 poussées, attente constante de 60 s, délais `git` de 240 s : au pire 2 880 s, sous la réserve d'1 h).
42. M1 (b) (additif 2) : `fin` et le geste sur la machine attrapent toute exception, puis le geste a lieu.
43. f5 (additif 2) : journaux du démarrage (départ, échéance, minuterie, amorce, mémoire) copiés dans le dossier versé avant le scellement.

**Non portés, et pourquoi.** m-a (additif 3), « aucun arrêt nulle part, destruction même sans versement » : le texte v3 (section 8,
inchangée) garde l'**arrêt** quand la poussée n'est pas vérifiée ou qu'un secret est trouvé (données réelles, non factices), et
quand la destruction est refusée ; l'arrêt arrête aussi la minuterie (écrit au journal). v10 (a), « garde du commit du canal » :
le texte (section 4) dit « garde de `main` » sur la copie ; la v2 garde la garde de `main`. m-d (tir de la minuterie), f3, f4
(noms de branches de la sonde), m6 : propres à la sonde. v10 (b), ligne `nvidia-smi` : hors des cinq domaines. v5 (a) : retirée
par la v9.

**Adaptations à la vraie course (aucun additif).** (A) Deux GO : machine GO-2026-11-05-03 (35 USD exactement), course
GO-2026-11-04-06 (400 USD exactement). (B) `CLE_ARGON` permise dans le corps et masquée partout (la sonde la refusait :
`ClientPiloteV2.creer`). (C) Échéance de la minuterie = création + 10 min + 80 h + 1 h ; borne de dépense au prix maximal :
0,40 × 81,42 h = **32,57 USD ≤ 35 USD** ; la garde de l'hôte (80 h, 32 USD, texte) arrête la course au moins 1 h avant. (D) Amorce
en refus (code 2) ou absente du clone : destruction **immédiate** demandée à la minuterie (fichier `a1v3-detruire-maintenant`),
puis rien n'est plus lancé, même à une reprise ; sans cela, une machine refusée attendrait 81 h. (E) `controler` après l'échéance
finale : code 7, **aucun geste** (machine arrêtée, données possibles ; la session décide). (F) numpy introuvable : l'amorce refuse
(la course en a besoin ; la sonde ne faisait que le mesurer). (G) Versement « partie de `main` » (texte) par un clone superficiel,
partiel et clairsemé (`--sparse`, puis le seul dossier versé).

## 3. Essais (`timeout 900 nice -n 10`, aucun réseau)

- `tests/test_hote_durable_a1_v3.py` (v1, inchangé) et `tests/test_hote_durable_a1_v3_v2.py` : **131 passés** (49 + 82), aucun
  sauté, en 144 s ; sortie `essais-lanceur-v1-et-v2.txt` (`eaae879f…`).
- Gardes neuves, chacune sur un cas sain et un artefact (R5) : GO de la machine (registre factice et registre réel de `main` au
  2026-11-05 / autre GO, absent, 34 USD, montant approché, hors période des deux côtés, autre auteur, révocation) ; clés de modèle
  (`CLE_ARGON` admise / `GEMINI_API_KEY`, `RR_…_API_KEY_…`) ; offre à une carte (GTX 1070 / volume « disk », offre « sans
  carte » de la v1 ; et la v1 refuse l'offre « gpu » : artefact de départ) ; client v2 (`CLE_ARGON` admise et masquée / le client
  de la sonde la refuse ; autre clé refusée avant l'appel) ; `louer` (état, ligne, aucun secret / onze artefacts, aucun appel) ;
  « no_such_ask » puis contrat ; erreur de Vast sans marqueur, illisible avec marqueur ; `controler` (codes 0, 1, 2, 3, 5, 6, 7) ;
  `facturation` ; fichier seul ; script de démarrage (chemin sain / amorce en refus, reprise après refus, clone impossible,
  étiquette autre, instance protégée, identifiant illisible, `DELETE` 403, échéance absolue passée) ; amorce (jusqu'à `exec` / dix
  artefacts, `curl` absent) ; machine (cas sain : branche partie de `main`, signe de vie, journaux du démarrage, liste juste,
  destruction / neuf refus avant la course, branche déjà présente, fuite, exception du versement, destruction refusée puis arrêt,
  arrêt refusé, étiquette autre, reprise, coût depuis le départ du conteneur, course bornée par l'échéance).
- Hors de mes essais : sondes v1 à v10 et garde de calcul non rejouées (inchangées ; additif 10 : 1 001 passés).

## 4. Lignes de GO à présenter, et où (pour que les gardes passent, sans doublon)

| registre | lignes exigées | qui les lit | état constaté (lecture seule, sans réseau) |
|---|---|---|---|
| `registres/go.md` de **`main`** (au lancement chez la fille, puis sur la machine) | **GO-2026-11-05-03** (calcul, Lazar, **35 USD** exactement sur la ligne et sur toute extension, valide du 2026-11-05 au 2026-11-18, non révoqué) et **GO-2026-11-04-06** (calcul, Lazar, **400 USD** exactement, jusqu'au 2026-11-18, non révoqué) | `louer` (garde de `main` + montant) ; la machine (`preparer`, mêmes contrôles) | les deux présentes (lignes 251 et 244), acceptées au 2026-11-05 par la garde de `main` (essai sur le registre réel) ; les 17 doublons de `main` ne gênent pas (la garde les admet en extension, R-389 ; la v2 ne les refuse pas sur `main`) |
| `registres/go.md` de **`canal/conv-audit-n04`** au commit `COMMIT_REGISTRE` | **GO-2026-11-04-06** recopiée octet pour octet ; **aucun identifiant en double** dans tout le fichier ; commit à moins de 200 commits de la tête du canal | la machine (copie passée au lanceur gelé, contrôlée par la garde de `main`) ; puis le lecteur gelé (`--registre-go`) | tête locale `740f49e2` (2026-11-05 02:02Z) : ligne 82 = ligne 244 de `main` à l'octet, aucun doublon. GO-2026-11-05-03 et GO-2026-11-05-04 **ne sont pas nécessaires** sur le canal ; si on les y recopie, une seule fois chacune |

GO-2026-11-05-04 (type « décision », Argon rendu) n'est lu par aucune garde. Toute ligne neuve ajoutée au canal après
`COMMIT_REGISTRE` ne compte pas : seul le fichier à ce commit est copié.

## 5. Refus HTTP 402 à solde nul (fait 3 de la mère)

- **Lu (code gelé `9776ed0`, extrait du bloc-notes `…/scratchpad/v3b1/arbre-9776ed0/`)** : `pole/attaque_goodhart_v3.py:75-83`
  et `arreter_sur_refus_de_budget` (298-321) : un **code 4** de la commande d'Argon (« budget sans envoi », dont 402 et 429 du
  relais) lève `ArretAttaque`, **sans aucune tentative de plus** (arrêt « refus_de_budget », loin du plafond) ; un **code 3**
  (« relais ou interface ») **attend** 15, 30, 60, 120 puis 300 s, tentative non consommée, **au plus 30 min cumulées par
  tentative** (`ATTENTE_MAX_PAR_TENTATIVE_S`, lignes 86-95 et 394-432), puis la tentative est comptée échouée (cause « relais »,
  sans bascule de modèle) et la course passe à la suivante ; `relais_perdu_h: aucun` (texte, ligne 124) : **aucun arrêt sur le
  cumul des attentes**.
- **Imprécision du brouillon 2, à corriger par couple à la contre-lecture n° 4 (non appliqué, R12)** : dans le couple 7, « et
  attend sans fin sur un code 3 (relais ou interface ; `relais_perdu_h: aucun`) » → « et, sur un code 3 (relais ou interface),
  attend 15, 30, 60, 120 puis 300 s, au plus 30 min par tentative, puis compte la tentative échouée (cause « relais », sans
  bascule) et passe à la suivante, sans arrêt sur le cumul (`relais_perdu_h: aucun`) » ; et « Si c'est le code 3, la course attend
  sans dépense d'Argon jusqu'à la garde de 72 h du lanceur ou aux plafonds de la machine (80 h, 32 USD), sans résultat. » → « Si
  c'est le code 3, la course use ses tentatives à 30 min chacune, sans dépense d'Argon, jusqu'à la fin du plan ou à la garde de
  72 h du lanceur (avant les plafonds de la machine, 80 h et 32 USD), sans résultat. »
- **Non lu** : la commande gelée `commande_argon_v56_nuit_v2.py` (`221df610…`) — absente de ce conteneur (pas dans l'arbre de
  travail, ni dans les références git locales, ni dans le bloc-notes), et aucun réseau. Je ne sais donc pas si un 402 **de
  l'interface Gemini** est rendu par le relais en 402 (puis code 4 : arrêt propre) ou en panne d'interface (code 3 : attente).
- **Conséquence si code 3** : la course use chaque tentative en 30 min d'attente sans dépense d'Argon (402 = rien servi), puis
  passe à la suivante, jusqu'à la fin du plan ou à la garde de 72 h du lanceur, sans résultat ; si chaque code 3 est compté au
  pire cas, le compteur peut aussi atteindre le plafond (arrêt « plafond » comptable). Dépense réelle bornée par la machine
  (≤ 32,57 USD au prix maximal).
- **Écrit** au brouillon 2 comme risque déclaré (couple 7, section 8, « Garde, sans session ») ; aucune règle d'arrêt ajoutée.
- **Conduite proposée au directeur** (aucune n'est codée) : (a) **avant la location**, la fille relève le solde prépayé de
  l'interface Gemini et l'écrit au journal de la location ; la course ne part que si le solde couvre le plafond (400 USD) ou au
  moins le devis haut — sans code, recommandée ; (b) **garde du lanceur v2** (neuve) : si le journal du relais montre trois statuts
  402 consécutifs **de l'amont**, arrêt de la course par son identifiant (TERM, puis KILL), arrêt d'infrastructure
  « solde_argon_nul », puis fin propre — à écrire seulement après lecture du format du journal de la commande gelée, et c'est un
  changement de la liste d'arrêt du texte (section 8 : « la garde n'arrête jamais la course sur un compte d'échecs ») : nœud de
  Lazar ; (c) première étape dans tous les cas : relire `commande_argon_v56_nuit_v2.py` (`221df610…`, branche
  `donnees/recuperation-collisionneur-v8-v1`) pour le chemin d'un 402 de l'amont.

## 6. Ce qu'un contre-lecteur neuf doit regarder en premier (dix points)

1. **Dépendances et import en fichier seul** : la v2 reprend des classes de la sonde v10 ; `COMMIT_PRIVE` doit porter les quatre
   modules ; une seule classe `Refus` en fichier seul (section 1).
2. **Écarts voulus aux corrections des sondes, où le texte prime** : arrêt (et non destruction) si la poussée n'est pas vérifiée,
   si un secret est trouvé ou si la destruction est refusée ; garde de `main` sur la copie du canal ; `controler` sans geste après
   l'échéance (code 7).
3. **Échéance et borne** : 81 h 10 min après la création ; 32,57 USD au prix maximal pour 35 USD d'enveloppe (« même enveloppe
   que GO-2026-11-04-09, non cumulée ») : la dépense déjà imputée à cette enveloppe (sondes) est à soustraire, non vérifiée ici.
4. **Destruction immédiate sur refus de l'amorce** (mécanisme neuf, sans additif) : seul le code 2 la déclenche ; une machine dont
   le Python meurt d'un signal avant la course attend l'échéance (borne : 32,57 USD) ou le `controler` d'une session.
5. **Versement « partie de `main` »** en clone superficiel, partiel et clairsemé : éprouvé en local (`file://`, filtres admis),
   jamais contre GitHub ; une **sonde courte du lanceur v2** (texte, section 13, point 7 quater) le montrerait.
6. **Signe de vie** : branche neuve `donnees/attaque-goodhart-v3-a1v3-troisieme-signe-de-vie-v1`, absente du texte ; elle doit ne
   pas exister avant la location (R12), et la fille doit lancer `controler` après T0 + 30 min.
7. **Texte** : la section 8 garde « aucune carte (`num_gpus` = 0) », « 8 Go de mémoire » et « destruction refusée → arrêt » ; le
   couple 4 déclare la substitution en tête de liste sans toucher la liste ; la phrase « le lanceur durable, qui ne connaît que ce
   texte et GO-2026-11-04-06 » (ligne 569) reste, alors que la v2 lit aussi GO-2026-11-05-03 pour la machine (à juger : couple ou
   non, sous la contre-lecture n° 4).
8. **HTTP 402** (section 5) : chemin non établi dans la commande gelée ; conduite à décider avant la course ; la phrase « attend
   sans fin » du couple 7 est imprécise (30 min au plus par tentative) : couple correctif proposé en section 5.
9. **Clé d'Argon** (R-1539, couple 6) : clé actuelle, lisible dans les métadonnées chez Vast et par toute clé du compte, dont la
   clé d'instance posée dans chaque conteneur (R-1533) ; la minuterie emploie cette clé d'instance ; rotation après la course.
10. **Registres** (section 4) : `COMMIT_REGISTRE` (candidat : `740f49e2…`, ligne à l'octet, aucun doublon) à moins de 200 commits
    de la tête du canal au départ de la machine ; GO-2026-11-05-03 lu sur `main` seulement.

## 7. Commande exacte de la location, pour la fille (non jouée)

Préalables : texte v3 scellé, committé et poussé (`COMMIT_PUBLIC`, `SHA_TEXTE`) ; lanceur v2 et ses trois dépendances committés
sur `main` du dépôt privé (`COMMIT_PRIVE`) ; `COMMIT_REGISTRE` choisi (section 4) ; branches `donnees/attaque-goodhart-v3-a1v3-
troisieme-v1`, `…-refus-v1`, `…-interrompue-v1` et `…-signe-de-vie-v1` absentes ; Argon seul (point 7 ter) et, si le directeur
retient la conduite 5 (a), solde Gemini relevé, écrits au journal de la location ; `vastai --version` = 1.8.3. La clé d'Argon :
la variable de la v1 est `GEMINI_API_KEY_2` ; si la clé actuelle (R-1539) est dans une autre variable, remplacer ce seul nom.

```
COMMIT_PRIVE=<hash complet (40) du commit de main qui porte la v2, la v1, la sonde v10 et la sonde v1>
COMMIT_PUBLIC=<hash complet (40) du commit public qui porte le texte v3 scellé>
SHA_TEXTE=<empreinte (64) du texte v3 scellé, égale à son compagnon>
COMMIT_REGISTRE=<hash complet (40) du commit de canal/conv-audit-n04 retenu (candidat : 740f49e2b27344b3188f9aba20b5f0115c3468ab)>
[ "$(vastai --version 2>/dev/null)" = "1.8.3" ] || { echo "vastai 1.8.3 exigé"; exit 2; }
D=/home/user/hors-clone-a1-v3-troisieme-v2; mkdir "$D" || exit 2                      # neuf (R12)
cd /home/user/controle-ia-travail && git fetch -q origin main \
 && git show origin/main:registres/go.md > "$D/registre-go-main.md" \
 && git show origin/main:.claude/hooks/garde_calcul.py > "$D/garde_calcul_main.py" \
 && for f in hote_durable_a1_v3.py hote_durable_a1_v3_v2.py sonde_hote_durable_a1_v3.py sonde_hote_durable_a1_v3_v10.py; do
      git show "$COMMIT_PRIVE:src/controle_ia/$f" > "$D/$f" || exit 2; done \
 && timeout 300 vastai search offers 'num_gpus=1 rentable=true reliability>=0.98 cpu_cores_effective>=4 cpu_ram>=8 disk_space>=30 dph_total<=0.40' -o dph_total --storage 30 --raw > "$D/offres.json" \
 && OFFRE=$(python3 -I -B "$D/hote_durable_a1_v3_v2.py" offre --offres "$D/offres.json") \
 && for V in "--verifier-seulement" ""; do
      GO_ID=GO-2026-11-05-03 env -i GO_ID=GO-2026-11-05-03 PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 \
        HTTPS_PROXY="${HTTPS_PROXY:-}" SSL_CERT_FILE="${SSL_CERT_FILE:-}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-${SSL_CERT_FILE:-}}" \
        CLE_ARGON="$GEMINI_API_KEY_2" GH_TOKEN="$CONTROLE_IA_GITHUB_TOKEN" VAST_API_KEY="$VAST_API_KEY" timeout 900 nice -n 10 \
        python3 -I -B "$D/hote_durable_a1_v3_v2.py" louer --go GO-2026-11-04-06 --go-machine GO-2026-11-05-03 \
          --registre-main "$D/registre-go-main.md" --garde-main "$D/garde_calcul_main.py" --offres "$D/offres.json" \
          --offre "$OFFRE" --commit-prive "$COMMIT_PRIVE" --commit-public "$COMMIT_PUBLIC" --sha-texte "$SHA_TEXTE" \
          --commit-registre "$COMMIT_REGISTRE" --journal-local "$D/journal-location-a1-v3-troisieme-v2.log" $V || exit 2
    done
```

Ensuite, la ligne « LIGNE POUR registres/etat.md » du journal va dans `registres/etat.md` ; puis `controler` à T0 + 40 min, et
après l'échéance finale (heures dans `"$D/journal-location-a1-v3-troisieme-v2.log.etat.json"`), avec le même `env -i` (sans
`CLE_ARGON` ni `GO_ID`) : `python3 -I -B "$D/hote_durable_a1_v3_v2.py" controler --etat "$D/journal-location-a1-v3-troisieme-v2.log.etat.json"
--journal-local "$D/journal-controle-a1-v3-troisieme-v2.log"` ; `facturation` de même, à tout moment. Code 5 : recontrôler ; 6 :
recontrôler ; 7 : la session décide (aucun geste) ; 1 : consigner dans `registres/arrets.md`.

## 8. Réserves

- Le rapport de la fille sur la sonde v10 (`b95bf21e`) n'a pas été lu : la référence locale de `canal/fille-2026-11-04` date du
  4 novembre (`97fb0681`) et le réseau est interdit ; source suivie : R-1527.
- La minuterie, l'amorce et le versement de la v2 n'ont jamais tourné sur Vast ; seuls leurs équivalents de la sonde v10 l'ont
  fait (R-1527). La partie « course » de la machine est celle de la v1, rejouée en jouet seulement.
