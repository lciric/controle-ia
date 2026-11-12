# Contre-lecture bornée du delta — préenregistrement « épreuve de l'étiqueteur du sabotage flou », brouillon 5

- **Contre-lecteur** : Claude Opus 5.5 (`claude-opus-5-5`), sous-agent neuf (R2). Je n'ai écrit ni le préenregistrement, ni son code, ni les deux contre-lectures précédentes, ni leurs couples.
- **Heures** (temps universel, `date -u`) : 7 novembre 2026, de 23:42:44 à 23:56:01.
- **Objet** : arbre `/home/user/wt-etiqueteur`, branche `prep/epreuve-etiqueteur-v1`, commit `be3bd7f14161c7b43f1244fa4e1cc7955108e18d` (arbre propre avant et après) ; brouillon 5 `f66a3e9d5a64e021b20db747dd8bd02e905523a2d0c9981c2a6fa4a649af3ea7`, comparé au brouillon 4 `4f186d8e9e435d64598d9f0b2b39a646e46934913cb27f39d7dc92a447687db5` ; `lire_items_phase1_v3.py` `3fc929873042ed627f5a9aedfa33ca6a03b75e192340c28573459bc7457cff08` ; `analyser_phase1_v3.py` `7c0555b4647a3e1e2c314b4e934345522cb72995712a789e044e81e77373fb9f` ; essais `0c76527c33e19c0a3886418379d7f2ac24e7c6bc451ce204d1a8fd13bef42925` et `734d7bcfd306d9d7064e541a1afc1aa15b86a48968469ca6e51c0b1e3f564182` ; `appliquer_couples_brouillon5_v1.py` `028b29d149651149bc9e9c819e4b491dcbba98b0f38305beeb01395cb36f4142` ; journal `b4cd9f67ef304b58c4d540975574705e9ddb3921d3e299195e594aec4139f714` ; devis v4 `6c93a8d128c8d180dd8bdfe4b35d65ca36f04b4d14b6b390eb781fa08cd29291`.
- **Ce qui fait foi pour ce qui était exigé** : contre-lecture du delta du brouillon 4 `1537b3ce86a6d499dd8811fdabbc1697237fcca2854d1a925e957a9fa0b4ec75` (bloquants D1 et D2, remarques R1 à R13) et ses 19 couples `8a533705a569c42816bae75f42941a2b06f9f9b0ae8a6d9212ddc186f854c0b9` ; GO-2026-11-07-07 (plafond de la phase 1 : 300 dollars) et GO-2026-11-07-10 (l'oracle de N-060 v3 décide à la porte, l'étiqueteur est rapporté à côté), `registres/go.md` lignes 267 et 270, lus sur `origin/main` au commit `e2f2caca8` (`3dd12d62fd9dc1b3d382c25a02e0903e651ae079056d80968b366d7b2664dfc4`) ; la référence locale `main` est en retard et ne les porte pas.
- **Rendus** : ce rapport ; `couples-contre-lecture-delta-brouillon5-v1.json` (11 couples, 13 occurrences ; chaque « ancien » présent exactement `n` fois au brouillon 5, sans chevauchement ; même format que les couples précédents).

## Verdict

**Scellable après couples. Aucun bloquant.** D1 et D2 sont levés pour les défauts constatés ; les 19 couples sont appliqués à l'octet (brouillon 5 et journal reproduits à l'identique) ; le plafond vaut 300 partout et le seuil du feu vert est juste ; R1 à R4 sont traités au code ; le `--max-appels` du relais de Kimi est écrit. Les 11 couples corrigent trois affirmations devenues inexactes, écrivent deux chemins résiduels du masquage et ajoutent à l'ordre des opérations ce que les points ouverts exigent.

- **D1** : levé pour le chemin constaté (valeur de clé passée comme nom de variable, sous toutes ses formes) et pour tout argument qui nomme ou porte la clé. **La garantie « dans aucun chemin » n'est pas tenue au sens strict** : sur 46 scénarios à fausse clé, 40 n'écrivent aucun fragment ; 6 écrivent la clé entière **sur la sortie d'erreur seulement** (jamais au manifeste, au journal ni aux réponses) : 4 par une option abrégée et ambiguë écrite avec « = » (`--re=<clé>`, `--relais=<clé>`), 2 par une clé passée à la place d'un chemin. Je ne les compte pas comme bloquants : il faut écrire une valeur de clé dans un argument qui ne la concerne pas, quand le défaut D1 venait d'un seul `$` de trop dans l'argument qui la nomme. Couples CD5-02 à CD5-04 (portée écrite, limite 14, règle d'exécution). **Si la session mère veut zéro chemin résiduel**, le correctif tient en trois lignes (section 1) mais demande une version 4 et une contre-lecture bornée de plus.
- **D2** : levé. Lignes absentes (une seule suffit), en double, d'items ou de lectures inconnus, fichier vide : jamais de verdict ; l'issue écrite est « arrêt : liste d'arrêt (réponses incomplètes ou en double) », avec la liste des écarts. Artefact voisin, hors du périmètre de D2 : **le même fichier passé pour les deux lecteurs rend un verdict** (couple CD5-07).
- **Points ouverts** (prix d'Argon, analyse de la phase 2) : **ne bloquent pas le scellement de la phase 1** ; l'ordre des opérations doit exiger ce que disent les couples CD5-05, CD5-06 et CD5-08 (section 6).

## Ce que j'ai fait

- Vérifié toutes les empreintes compagnons du dossier (aucun écart) et l'annexe C du brouillon 5 contre le disque (20 fichiers, aucun écart ; bloc de la question `1a5021b3…` inchangé).
- Rejoué en environnement vidé (`env -i`) les essais que cite le brouillon 5 : **69 passés** (8,2 s), dont les 33 des versions 3.
- **Reproduit le brouillon 5** dans une copie du dossier (bloc-notes), brouillon 5 et journal ôtés, avec le script d'application tel quel (`--heure-fin 23:40:51`) : brouillon et journal **identiques à l'octet**.
- Écrit des essais neufs, **hors du dépôt** (bloc-notes de la session, dossier `delta-b5/`), sans réseau ni clé réelle, à partir de ceux de la contre-lecture précédente :
  - `essais/enveloppe_reel_v3.py` (`c5d917adf1e4b7aa1ee2fa019cad0ce9c5161c51046dcc71d487f44d3c922173`) : lance `lire_items_phase1_v3.py` **en mode réel**, réseau remplacé par de fausses ouvertures (aucun appel ne sort), deux scénarios ajoutés (jetons non numériques portant la clé ; 400 `API_KEY_INVALID` portant la clé) ;
  - `essais/pilote_d1_v3.py` (`6dfc4a25601f5284e1c2a891f0c0f03cde1a397ebf3f1da9265813df825affe2`) : 46 scénarios ; chaque sortie (sortie standard, sortie d'erreur, tout fichier écrit) cherchée pour la clé entière, ses 34 fragments de 6 caractères et ses fragments de 5 ; résultats `resultats_pilote_d1_v3.txt` (`aaa1cd23a427a1618c0979305ff1ebffdc721746f025a1602cda9b2870aa3238`) ;
  - `essais/d2_v3.py` (`51542dc2b640e0e865399bdcf5c5bff4f151a13f810471d5a44341a6faca00f2`) : 12 cas en appel direct, 2 par la ligne de commande ;
  - `essais/verif_couples_b5.py` (`5de57f310f9f3592665d77a11585d71f3ea67a5df2fd1e456e8fff68c38ee160`) ; `essais/couples_b5.py` (écrit et vérifie mes couples).
- Lu en entier les différences v2 → v3 de la lecture et de l'analyse, les 33 compléments du script d'application, le devis v4 ; recalculé le seuil du feu vert sur `controle_format`.
- Passé le validateur du dépôt (`controle_ia.prereg.problemes`) sur le brouillon 5, puis sur une copie où mes couples sont appliqués : seul reste le marqueur `<<COMMIT_EPREUVE_ETIQUETEUR>>` (à remplacer au scellement).

## 1. D1 : masquage, tous les chemins essayés

Fausse clé de 39 caractères à la forme d'une clé Google, posée par mes essais seuls. Mode réel : fausse clé dans `GEMINI_API_KEY`, sauf mention contraire.

| groupe | scénarios | codes | clé ou fragment de 6 caractères |
|---|---|---|---|
| ceux de la contre-lecture précédente : 503 avec la clé à la position 297 (quatre tentatives) ; 400 avec préfixes, clé coupée, clé sur la frontière des 300 caractères ; 401 (arrêt général) ; coupure de connexion ; exception imprévue au-delà de 295 caractères ; lecture incomplète ; clé dans le modèle servi ; clé dans le texte et le motif de fin ; pannes mêlées avec reprises | 9 | 6, 6, 5, 6, 6, 6, 4, 6, 6 | aucun |
| nouveaux : jetons non numériques portant la clé (exception hors d'une lecture, R3) ; 400 `API_KEY_INVALID` portant la clé (R4) | 2 | 7 ; 5 | aucun |
| pannes mêlées à `--fils-par-lecteur 4` | 1 | 2 (refusé, gelé à 1) | aucun |
| **valeur de clé comme nom de variable** : mode réel ; mode simulé ; `--variable-cle-gemini=<clé>` ; abrégée `--variable=<clé>` ; nom en minuscules | 5 | 2, rien d'écrit | aucun |
| erreurs d'arguments, réel et simulé : valeur au plafond, positionnelle, à l'entropie, au choix de lecture, à `--relais-max-appels` ; formes de `--commit`, `--go`, `--relais-empreinte`, `--relais-kimi` ; `--reel=<clé>`, `--simule=<clé>` ; séparateur `--` | 21 | 2 | aucun |
| clé passée comme chemin, clé connue du script : `--items` en mode réel ; `--items` en mode simulé, variable posée | 2 | 7 | aucun (masquée) |
| **option abrégée et ambiguë avec « = »** : `--re=<clé>`, `--relais=<clé>`, réel et simulé | 4 | 2 | **clé entière, sortie d'erreur** |
| **clé passée comme chemin, clé inconnue du script à ce moment** : `--registre-go` en mode réel (lu avant la clé) ; `--items` en mode simulé sans variable | 2 | 7 | **clé entière, sortie d'erreur** |

Un fragment de 5 caractères relevé au journal de Kimi du scénario « pannes mêlées » est l'horodatage `…556789Z`, qui recoupe le `56789` de la fausse clé : pas une fuite.

**Ce qui est levé** : le défaut constaté au brouillon 4 (valeur de clé passée comme nom, écrite sur la sortie d'erreur en mode réel et au manifeste en mode simulé) ne se reproduit sous aucune forme ; aucune valeur refusée n'est recopiée, sauf dans les deux chemins ci-dessous ; le message d'arrêt de `__main__` et toute exception passent par le masquage ; une exception imprévue hors d'une lecture est saisie et masquée (code 7).

**Ce qui reste** : le script ne peut masquer qu'une valeur qu'il connaît comme clé.
- (a) `Parseur.error` suppose qu'`argparse` cite les valeurs entre apostrophes ; le message « ambiguous option: --re=<valeur> could match … » recopie l'argument entier, hors apostrophes, avant que la clé soit lue (Python 3.13.18).
- (b) une valeur de clé passée à la place d'un chemin est recopiée par le message d'erreur du système : `--registre-go` est lu par `verifier_go` avant `secrets.ajouter` ; en mode simulé sans variable posée, la valeur n'est connue nulle part. La clé de Kimi, qui vit dans le relais, n'est jamais connue du script.

Correctif possible, si la session mère le veut (version 4) : dans `Parseur.error`, `re.sub(r"(--?[\w-]+)=\S*", r"\1=[valeur non recopiée]", message)` avant le reste ; appeler `secrets.ajouter(os.environ.get(a.variable_cle_gemini))` aussitôt après `controler_formes` ; dans le gestionnaire générique de `__main__`, écrire `e.strerror` sans le nom de fichier pour une `OSError`. Je ne l'exige pas : couples CD5-02 (la formule « valeur refusée jamais recopiée », trois fois, prend sa portée exacte), CD5-03 (limite 14) et CD5-04 (règle d'exécution : aucune valeur de clé sur une ligne de commande, options écrites en entier).

## 2. D2 : réponses complètes exigées

`controler_completude` attend, pour chaque lecteur, une ligne « principale » par item de la clé (396) et une ligne « relecture » par jumeau (60), soit 456, ni plus ni moins, les lignes de l'essai de format ignorées ; tout écart arrête avant tout calcul.

| cas (lecteur parfait selon la question) | issue |
|---|---|
| lecture complète (cas sain) | « étiqueteur validé contre la construction » |
| 40 lignes principales ôtées chez A ; 1 principale ôtée chez B ; 1 relecture ôtée chez A | arrêt : « 40 », « 1 », « 1 lignes absentes sur 456 » |
| fichier de A vide ; deux fichiers vides | arrêt : « 456 lignes absentes sur 456 » (une ou deux fois) |
| une ligne en double ; un doublon contradictoire (« ok » et « illisible ») | arrêt : « 1 lignes en double » |
| une ligne d'item inconnu ; une relecture d'un item qui n'est pas un jumeau | arrêt : « lignes d'items ou de lectures inconnus » |
| lignes de l'essai de format mêlées | ignorées ; verdict (sans effet : le fichier final d'une lecture principale n'en porte pas) |
| **le fichier de A passé pour A et pour B** | **verdict** (« validé » ici) : rien ne contrôle le champ `lecteur` des lignes |
| ligne de commande, fichier de A vide | fichier de résultat écrit, issue « arrêt : liste d'arrêt (réponses incomplètes ou en double) » et ses écarts ; **code de sortie 0** |

Le texte (couples CD-04 et CD-05) disait « un item sans ligne de réponse comptant illisible » ; le code est plus strict : toute ligne absente arrête, quelle que soit la règle des 2 %. C'est conforme à CD-04, qui exige aussi le refus d'un fichier incomplet. Le code de sortie 0 sur un arrêt est celui de la v2 pour la règle des 2 % ; l'échange des fichiers est un artefact d'exécution, que l'empreinte des entrées écrite au résultat permet de voir après coup. Couple CD5-07 : contrôle écrit avant l'analyse (empreintes égales aux `sorties` du manifeste, différentes l'une de l'autre, champ `lecteur` conforme) ; code de sortie dit.

## 3. Les 19 couples et les compléments

- **À l'octet** : chaque « ancien » figure `n` fois au brouillon 4 (20 occurrences) ; les empreintes « ancien » et « nouveau » du journal sont égales à celles des couples ; les empreintes des 33 compléments du journal sont égales aux textes du script ; reproduction exacte (section « Ce que j'ai fait »).
- **15 « nouveaux » figurent tels quels au brouillon 5 ; 4 ont été retouchés par des compléments journalisés**, chacun motivé par un correctif de code et sans changer le sens du couple : CD-06 par C5-21 (« le script ne le vérifie pas » devient « vérifié », R1 au code, essai `test_R1_…`) ; CD-11 par C5-22 (402 du relais arrête le lecteur ; `--relais-max-appels` exigé ; ordre d'exécution) ; CD-12 par C5-23 (400 `API_KEY_INVALID` en arrêt général, R4) ; CD-15 par C5-13 (seuil recalculé pour 300 dollars). CD-17 et CD-19 restent entiers, suivis d'un ajout (C5-29 : prix tenté ; C5-31 : traitement).
- **Compléments qui touchent un élément gelé, tous dits** : plafond 400 proposé → 300 accordé (C5-08, C5-09 à C5-12, C5-24 à C5-26) ; seuil du feu vert (C5-13) ; lignes d'arrêt nouvelles (C5-28 : arguments refusés, second lancement, exception imprévue) ; code de sortie 7 (C5-16) ; arrêt du lecteur Kimi sur 402 et arrêt général sur 400 `API_KEY_INVALID` (C5-22, C5-23) ; complétude exigée avant l'analyse (C5-14) ; limite 13 (C5-30). **Aucun seuil, aucune métrique, aucune règle de calcul de C1 à C3 ni de la garde de relecture ne change.** Les chiffres ajoutés (69 essais, 300, 229 et 234, 221 et 292, 394 et 286, 100 et 2 280) sont vérifiés.
- **Le nombre de cinq tentatives par item** est juste : trois erreurs reprises, une demande de format refaite, puis la dernière tentative (boucle de `lire_un`). La formule de CD-11 (« quatre erreurs de transport et deux demandes, compteurs communs à l'item ») peut se lire six ; le nombre écrit (100 et 2 280) est le bon. Sans couple.
- **Trois affirmations du brouillon 5 sont devenues inexactes** : « valeur refusée jamais recopiée » (trois fois ; section 1 : CD5-02) ; le prix d'Argon « à vérifier … au plus tard avant la décision de dépense », décision donnée le 7 novembre peu avant 23:18 sans vérification (CD5-06) ; « contre-lecture du delta suivante » et limite 7 (CD5-09, CD5-10).

## 4. Plafond de 300 dollars et feu vert

- **Partout 300** : texte (statut, tables, garde, devis en bref, ordre des opérations, liste d'arrêt, limite 13), devis v4, code (`PLAFOND_ACCORDE = 300.0`, défaut de `--plafond-dollars`, refus au-delà, essai `test_plafond_accorde_300_cas_sain_et_artefact`). Les mentions de 400 qui restent sont historiques et dites telles (« 400 proposé, accordé ensuite à 300 »), ou désignent le code 400 de l'interface d'Argon.
- **Seuil du feu vert recalculé** sur `controle_format` : extrapolation = coût moyen mesuré par appel × 1,25 × (456 × 1,05 ≈ 479) appels, sommée sur les deux lecteurs, comparée à 300 − F. Le seuil de lecture principale mesurée vaut (300 − F) / 1,25 : **233,9 dollars** pour F = 7,61 (centre du devis v3 : 5,64 + 1,97), **229,0** pour F = 13,69 (haut : 10,04 + 3,65). Le centre passe (1,25 × 176,9 = 221,1 ≤ 292,4) ; le haut donne un feu rouge (1,25 × 315,6 = 394,5 > 286,3). Texte, devis v4 et code concordent.
- La limite 13 dit la conséquence : sous l'hypothèse haute, l'épreuve s'arrête après l'essai de format, sans verdict ni dépense de lecture principale.

## 5. Remarques R1 à R4, relais de Kimi

| remarque | traitement | constat |
|---|---|---|
| R1 second lancement | refus si le plafond diffère de celui de l'essai de format, ou si `--depense-engagee` est inférieure à la sienne ; mêmes entrées, réglages et mode | **traitée** (essai `test_R1_…`, code lu) |
| R2 plafond par défaut | défaut 300, plafond accordé ; tout plafond au-delà refusé | **traitée** autrement que recommandé (option non rendue obligatoire), sans risque : le défaut est désormais le plafond accordé |
| R3 exception hors d'une lecture | saisie dans `lire_tout`, item « illisible » avec motif masqué, manifeste écrit, code 7 | **traitée** ; mais la dépense de ce lancement est **sous-comptée au manifeste** : la réserve d'une tentative interrompue après l'appel n'est jamais réglée (mon scénario : 20 appels d'Argon faits, 0,38 dollar écrit, celui de Kimi). La garde du lancement la compte encore (elle reste réservée) ; c'est le report à un lancement suivant qui la perd. Couple CD5-11 |
| R4 clé invalide en 400 | 400 portant `API_KEY_INVALID` : arrêt général ; autre 400 : erreur ordinaire | **traitée** (essai `test_R4_…` ; mon scénario : code 5, clé masquée) |
| relais, `--max-appels` | texte (CD-11 retouché par C5-22 ; ordre des opérations, C5-25) et devis v4 : 100 puis 2 280, relais relancé avant chaque lancement ; le script exige `--relais-max-appels` ≥ 5 × items en mode réel et l'écrit au manifeste ; 402 arrête le lecteur Kimi | **écrit**. Le script ne peut que croire la valeur déclarée : CD5-04 exige la même valeur au relais et au script |
| R6 fils | `--fils-par-lecteur` gelé à 1 au code | fait |

## 6. Points ouverts : bloquent-ils le scellement de la phase 1 ?

| point | bloque ? | ce que l'ordre d'exécution doit exiger |
|---|---|---|
| **prix d'Argon non vérifié** (barème 10 et 50 dollars par million figé dans le script) | **non** : sceller n'engage aucune dépense, et un barème au-dessus du prix réel ne fait que rendre la garde plus prudente. Le risque est l'inverse (prix réel au-dessus du barème : garde qui sous-compte, dépense réelle au-delà de 300) | couples CD5-05 et CD5-06 : (1) avant l'essai de format, vérification sur la page publique des prix si elle est joignable (par le directeur, ou par un réseau permis sur sa décision) ; un prix publié au-dessus du barème arrête avant tout appel ; (2) **après l'essai de format et avant le second lancement**, contrôle sur le relevé d'usage ou la facture du fournisseur, pour les seuls appels de l'essai de format (clé ou projet dédié) : montant facturé hors taxes au plus égal à la somme des `cout_estime` du lecteur A, jetons facturés égaux aux jetons écrits ; même contrôle pour Kimi ; sinon pas de lecture principale, barème corrigé en version nouvelle, nœud du directeur. Le feu vert du script devient nécessaire, non suffisant. L'essai de format est petit (devis : 7,6 à 25 dollars au barème), ce qui borne l'exposition avant ce contrôle |
| **analyse de la phase 2 non écrite** | **non** : la phase 2 n'existe que si la phase 1 valide ; ses seuils sont écrits dans ce texte et déposés chez le tiers avant toute lecture ; le sous-échantillon est tiré à la génération | couple CD5-08 : script **contre-lu et scellé** (le texte disait « contre-lu ») avant le départ de la phase 2, avant la réception de toute réponse d'annotateur, appliquant les règles et seuils déposés sans les changer ; tout écart est un écart au préenregistrement scellé |

## Remarques non bloquantes

1. **Deux chemins résiduels du masquage** (section 1) : CD5-02, CD5-03, CD5-04 ; correctif de trois lignes possible en version 4.
2. **Même fichier pour les deux lecteurs** : verdict rendu ; contrôle écrit avant l'analyse (CD5-07). Un contrôle du champ `lecteur` dans le code est recommandé à toute version ultérieure.
3. **Code de sortie 0 sur un arrêt de l'analyse** : l'issue écrite est la bonne ; le code ne la dit pas (CD5-07 le dit).
4. **Dépense sous-comptée dans le chemin de R3** (section 5) : CD5-11. Recommandé au code : écrire au manifeste la réserve non réglée et la compter dans la dépense.
5. **`--relais-max-appels` déclaratif** : CD5-04.
6. **Référence locale `main` en retard** sur `origin/main` : les GO de la phase 1 sont sur `origin/main` (`e2f2caca8`) ; la session mère scelle contre ce registre-là.

## Couples (11, 13 occurrences)

| identifiant | objet | correctif de code requis |
|---|---|---|
| CD5-01 | statut | non |
| CD5-02 (3 occurrences) | portée de « valeur refusée jamais recopiée » | non (correctif recommandé) |
| CD5-03 | limite 14 : deux chemins résiduels du masquage | non |
| CD5-04 | ordre des opérations : aucune clé sur une ligne de commande ; même `--max-appels` au relais et au script | non |
| CD5-05 | ordre des opérations : contrôle des prix avant le second lancement | non |
| CD5-06 | prix d'Argon : contrôle en deux temps, sur la facture de l'essai de format | non |
| CD5-07 | ordre des opérations : contrôle des fichiers avant l'analyse ; code de sortie d'un arrêt | non (contrôle du champ `lecteur` recommandé) |
| CD5-08 | analyse de la phase 2 scellée avant son départ | non |
| CD5-09 | limite 7 : trois contre-lectures, portée de la troisième | non |
| CD5-10 | entrée « Contre-lecture » : ce rapport, son empreinte, son verdict | non |
| CD5-11 | liste d'arrêt, R3 : dépense sous-comptée | non (écriture de la réserve recommandée) |

Les chiffres que mes couples ajoutent (46 et 40 scénarios, 20 appels et 0,38 dollar) viennent de mes essais, cités ci-dessus avec leurs empreintes.

## Limites de cette contre-lecture

- **Bornée** : je n'ai relu que les correctifs de D1 et D2, les remarques R1 à R4, le plafond et le feu vert, les couples, les compléments et le devis v4 ; ni le reste du texte, ni le générateur, ni le guide d'annotation.
- Aucun appel réseau : ni prix d'Argon, ni réponse réelle d'une clé invalide chez Google ; relais de Kimi lu par ses réglages dans le texte, non lancé.
- Messages d'`argparse` éprouvés sous Python 3.13.18 seulement ; une autre version peut en recopier d'autres.
- Une seule génération d'essai (graine 20261107, celle des contre-lectures précédentes).

## Interdits tenus

Aucune lecture de `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*` ni `docs/notes/bras-attaque/` ; aucune clé ni variable d'environnement du poste lue (essais en environnement vidé, seules des valeurs factices posées par mes essais) ; aucun appel réseau vers un fournisseur (fausses ouvertures en mode réel) ; aucun commit, aucune poussée, aucun fichier `.sha256` ; aucun fichier existant modifié (arbre propre avant et après, tout lancé avec `-B`) ; seuls fichiers ajoutés au dossier : ce rapport et le fichier des couples. Sorties de travail dans le bloc-notes de la session (`delta-b5/`), hors du dépôt.
