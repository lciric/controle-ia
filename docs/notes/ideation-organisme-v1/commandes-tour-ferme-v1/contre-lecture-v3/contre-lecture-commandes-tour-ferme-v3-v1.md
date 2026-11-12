# Contre-lecture (règle R2) des commandes externes v3 de Kimi et d'Argon — tour fermé, étage 1

Contre-lecteur neuf (Fable 5.1), le 2 novembre 2026, de 23:29 à 23:50 UTC (heures de `date -u`) ; le conteneur a redémarré
vers 23:42 UTC, sans perte (notes et arbre relus ; seules les mutations C9 à C12 ont été rejouées). Je n'ai écrit ni le code
ni les essais lus. Rien commis, rien scellé, aucun `.sha256` créé ni modifié, aucun fichier de l'arbre modifié (mes mutations
et expériences tournent sur des copies dans `contre-lecture-commandes-tf/mut/dossier/`), aucun réseau hors boucle locale,
aucun appel de modèle, aucune instance ; Python sous `nice -n 10`.

Objet : dossier `docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1/` de l'arbre `wt-commandes-tf` (branche
`outils/commandes-tour-ferme-v1`, tête `9dbe15a1`), contre le contrat du dépôt public `ideation-organism` (commit `53aef4a`,
lecture seule) et l'annexe A du brouillon 5 du préenregistrement (lignes 745 à 871).

## 1. Verdict

**Conformes après corrections précises — une correction bloquante (B1) avant toute course payante** : les quatre changements
v2 → v3 sont exacts et minimaux, le relais `servir` est identique octet pour octet, 51 essais passent et 23 mutations sur 23 sont
tuées ; mais, dans la configuration v3 (même `ETAPE_POLE=tour_ferme_v63` pour les deux relais, `PLAFOND_ETAPE_USD` = la part,
44 ou 6 USD, même registre partagé), **la garde d'étape du registre refuse le vérificateur d'Argon (code 4) dès que Kimi a
dépensé ≈ 5,95 USD dans l'étape**, ce que l'adaptateur lit « erreur » et l'étage comme un arrêt : la course s'arrêterait vers la
sixième ou septième carte testée, sur 31,7 attendues. Vérifié par lecture du code et par expérience (E1, section 5).

## 2. Bloquants

**B1 — Garde d'étape du registre partagée entre les deux fournisseurs sous un seul nom d'étape, avec des parts différentes.**

- Fichiers et lignes : `commande_kimi_v3.py` l. 189-190 et `commande_argon_v56_nuit_v3.py` l. 349-350 (`reg.reserver(...,
  etape=etape, plafond_etape_usd=plafond_dur)`), avec `registre_depense_cumulee_v1.py` l. 79-100 (`etat` : `par_etape` indexé
  par la seule valeur `etape`, tous fournisseurs confondus) et l. 139-144 (garde 2 : `réglé + engagé de l'étape + pire cas ≤
  plafond dur`). L'en-tête du registre (l. 15-16) le dit : « la garde 2 porte sur les deux fournisseurs ensemble (même
  registre), comme le noyau » — c'était vrai du noyau v56 (un plafond d'étape commun) ; ce n'est plus vrai du lanceur v63.
- Fait : `demonstrations/tour_ferme_v63.py` l. 63 (`ETAPE = "tour_ferme_v63"`) et l. 272 (`portes[n].transmettre(ETAPE,
  plan["parts"][n])`) donnent aux deux commandes le **même** `ETAPE_POLE` et un `PLAFOND_ETAPE_USD` **différent** (`44.00`
  pour Kimi, `6.00` pour Argon : `adaptateurs_v56.py` l. 70) ; `substituer_commandes` (`attaque_goodhart_v2.py` l. 233-250)
  leur donne le **même** registre (`<SORTIE>/registre-depense-cumulee-v1.jsonl`). À chaque appel du vérificateur, la commande
  d'Argon compare donc `dépense de Kimi + dépense d'Argon dans l'étape + pire cas` à 6,00 USD. Kimi dépense jusqu'à 44 USD dans
  la même étape (proposeur : 3 sessions ≤ 0,50 ; expérimentateur : ≤ 0,80 par carte, avant chaque appel du vérificateur). Le
  refus (`PlafondCumule`, code 4, `envoye: false`, rien envoyé) est lu par `AdaptateurCommandeExterne.lancer` comme « erreur »
  (`adaptateurs.py` l. 740-744 : tout code ≠ 0 hors refus R-764) et par `lancer` de l'étage v5 (`tests_de_mort_v5.py`
  l. 408-412) comme `EtageInterrompu` : arrêt de la course entière, le reste des 50 USD inemployé, aucun résultat par défaut de
  plafond — ce que la décision de Lazar du 2 novembre (18:26-18:29 UTC) exclut.
- Expérience E1 (copie, faux relais, section 5) : registre vide → Kimi expérimentateur accepté ; 5,95 USD réglés par Kimi sous
  l'étape `tour_ferme_v63` → Argon `lecteur_test`, plafond 0,10, `PLAFOND_ETAPE_USD=6.00` : **code 4, « garde d'étape
  (tour_ferme_v63) : 5.9501 réglés + 0.0000 engagés + pire cas 0.0503 > plafond dur 6.00 USD : appel refusé », rien reçu par
  le relais** ; témoin : même appel avec `PLAFOND_ETAPE_USD=44.00` → code 0. La suite d'essais ne le voit pas : `test_garde_d_etape_code_4`
  ne joue qu'un fournisseur à la fois.
- Correction proposée (précise, à décider par session-depot ; code v63 gelé, à ne pas toucher) — option A, recommandée :
  **version 4 des deux commandes**, un changement unique : la clé d'étape passée au registre devient `étape/fournisseur`
  (`etape=None if etape is None else f"{etape}/kimi"` dans Kimi, `.../argon` dans Argon, à l'appel de `reg.reserver` ; le champ
  `etape` de la dernière ligne reste `tour_ferme_v63`), avec un essai neuf à deux fournisseurs sur le même registre (Kimi à
  5,95 USD dans l'étape, Argon à 6,00 accepté ; Argon à 5,95, Argon refusé) et une mutation qui retire le suffixe ; la garde
  cumulée (50 USD, les deux ensemble) ne change pas. Option B, sans code : donner à Argon un registre **distinct** dans la
  configuration (argument `--registre` sans le jeton `{REGISTRE}`, chemin absolu hors de `SORTIE`) — la garde cumulée n'est
  alors plus partagée (le `Compteur` du noyau tient toujours 50 USD et les parts), et le chemin figé par l'empreinte de la
  configuration doit exister chez la fille ; moins propre. Option C : registre v2 à garde 2 par (étape, fournisseur) — change
  aussi l'import des deux commandes, donc une v4 de toute façon. Dans tous les cas : nouvelle contre-lecture courte de la v4,
  banc rejoué, empreintes refaites avant d'écrire la configuration v3 (A.2 gèle les chemins des fichiers de commande).

## 3. Importants

**I1 — TF-02 (porté à conv-audit par le rédacteur) est bien vivant en v63 et plus probable que le LISEZMOI ne le dit.**
`etage_entre_generations_v57.py` l. 69-82 appelle `executer_tests_de_mort(..., **reglages)` avec les réglages de
`pole/tour_ferme_v63.py` l. 810-812 (`budget_test_usd`, `budget_lecteur_usd`, sans `prix_caractere_usd`) : la seule garde
d'entrée de l'étage (`tests_de_mort_v5.py` l. 468) est donc **inactive** (`None`), et le seul contrôle avant envoi est celui de
la commande, au pire cas (un jeton par octet, 2 USD par million, sortie minimale 4 096 jetons = 0,041 USD). Limites recalculées
(E4) pour l'expérimentateur de Kimi : 378 402 caractères à 0,80 USD de reste, ≈ 178 400 à 0,40, 78 402 à 0,20, 28 402 à 0,10.
Or la consigne de l'expérimentateur grossit avec l'historique (jusqu'à 200 000 caractères de tranche servis par fiche, 20 000
de script et 2 × 20 000 de sorties par exécution : `tests_de_mort_v2.py` l. 141-142 et 186) tandis que le reste de la carte
baisse au coût réel (≈ un jeton pour 3 à 4 caractères) : l'écart entre les deux comptes fait qu'une carte à consigne longue
(100 000 à 300 000 caractères au tour 3 ou 4) heurte le code 4 → « erreur » → arrêt de la course. Côté vérificateur : limite
27 000 caractères à 0,10 USD (sortie 200 jetons) ; vue typique ≈ 17 000 à 21 000 (3 exécutions × (3 000 + 1 500 + métadonnées),
JSON indenté par `section_servie`, préenregistrement court), mais jusqu'à 20 lignes `RESULTAT:` de 300 caractères par
exécution (`MAX_LIGNES_RESULTAT`, `TAILLE_MAX_LIGNE_LECTEUR`, estimation) portent le pire cas vers ≈ 35 000 à 38 000 : refus
possible. Ce n'est pas corrigeable dans la commande sans déclarer un coût faux (seul un code 0 à `cout_usd` ≥ plafond serait lu
« budget_depasse », et il entrerait au compteur). **Nœud à trancher avant le GO** (adaptateur ou étage : lire un refus sans envoi
de l'expérimentateur ou du vérificateur comme « fin des tours de la carte », ou accepter l'arrêt en l'écrivant au
préenregistrement et à la liste d'arrêt). Le rédacteur l'a vu ; je précise la cause (`prix_caractere_usd` absent) et l'ordre de grandeur.

**I2 — Huit de mes douze mutations survivent à la suite (section 5)** : C3, C4 (`cout_usd` = 0 sur code 4, contrat « coût fini
> 0 aussi sur un échec » — l'adaptateur compterait alors le plafond de session en `cout_inconnu`), C6 (Kimi : `envoye` vrai sur
un 402/429 du relais), C7 et C8 (délai dépassé rendu en code 3 ; gestionnaires de signaux retirés — le LISEZMOI déclare le code 6
non couvert ; mes expériences E2 et E3 montrent que le code livré fait ce qu'il dit), C9 et C10 (**contrôle du modèle servi
retiré** dans les deux commandes : aucun essai ne fait répondre le faux relais sous un autre identifiant, `reglage["servi"]` n'est
jamais posé ; l'adaptateur garde sa propre barrière, `exiger_modele_servi=True` dans `ideation_v8.adaptateurs_reels_v56`, mais
la barrière de la commande, qui rend `modele_servi` et le code 5, n'est pas éprouvée ici), C11 (Argon : la correction v2 CLM-02
« coût d'un échec = pire cas réservé » n'est pas éprouvée dans cette suite — le LISEZMOI renvoie aux essais v2, acceptable mais à
dire). Demande : six essais de plus (modèle servi différent → code 5 et `modele_servi` rendu, pour les deux ; `cout_usd` > 0
sur chaque code 4 ; Kimi 402 → `envoye: false` ; délai → code 6 ; signal → code 6 ; Argon `cout_origine = pire_cas` → coût =
pire réservé), travail de routine, sans GO.

## 4. Mineurs

1. `commande_argon_v56_nuit_v3.py` l. 413-438 : une option refusée par `argparse` (faute de frappe dans la configuration,
   `--registre` absent) sort en code 2 **sans dernière ligne JSON** (E5 : sortie standard vide), là où Kimi en rend une
   (`lire_arguments` dans le `try`, l. 151 et 166-167). Conséquence : plafond de session compté `cout_inconnu` au premier
   appel, « erreur », arrêt — sans dépense réelle. Comportement v2 inchangé ; à aligner en v4 si une v4 est faite.
2. Codes inégaux sur un refus du relais : Kimi rend 3 sur 402/429 (l. 221), Argon 4 (l. 380) ; `envoye: false` et coût plancher
   dans les deux cas (E6) ; l'adaptateur lit « erreur » dans les deux cas.
3. En-tête de `registre_depense_cumulee_v1.py` (l. 1-10) : « mini-course », « 10 USD », commandes `commande_kimi_v2.py` /
   `commande_argon_v56_nuit_v1.py` — texte périmé, fichier gardé identique à dessein (`8ba92066…`) ; la phrase « garde 2 … les
   deux fournisseurs ensemble » est la racine de B1.
4. Interpréteur (point 7 de la commande) : les deux commandes n'importent que la bibliothèque standard (vérifié : `argparse`,
   `json`, `math`, `os`, `signal`, `sys`, `urllib`, `fcntl`, `uuid`, `datetime`, `hashlib`, `importlib`, `threading`, `time`,
   `http.server`). `.venv/bin/python` est un lien vers `/usr/local/bin/python3` (3.13.18), le dossier `.venv/` est ignoré par
   git et a été recréé aujourd'hui à 22:46 UTC : son existence et sa cible chez la fille ne sont pas garanties, et c'est sa
   cible qui entre au manifeste (`description()` empreinte chaque argument qui est un fichier). `/usr/bin/python3` (3.13.18
   aussi, celui du 1er novembre) est le choix sûr : stable, présent partout, hors du dépôt. Recommandation : écrire
   `/usr/bin/python3` dans les deux commandes de la configuration v3 (le LISEZMOI, l. 108 et 119, propose `.venv/bin/python`).
5. `servir` : seule la constante `VERSION` partagée change (champ `version` de `GET /relais/etat`, en-tête `Server`), annoncé ;
   le relais 8805 reste servi depuis son fichier actuel, donc sans effet pour la course. `COLLISIONNEUR_DEFAUT` relatif au
   dossier (l. 104) ne pointe sur rien depuis ce dossier : dit par le rédacteur, hors périmètre.
6. Kimi, l. 223-226 : un délai de **connexion** (URLError portant `TimeoutError`) sortirait en code 3 au pire cas, non 6 ;
   théorique sur la boucle locale (le relais absent donne « connexion refusée », code 3, `envoye: false`).
7. Kimi, l. 171-173 : `"max_tokens": n or maxi` — avec `--sortie-min-jetons-lecteur 0` un `n` nul reboucle sur `maxi` ; sans
   effet aux défauts (200). Aucune correction demandée.

## 5. Ce que j'ai rejoué

Toutes les commandes depuis le dossier de l'arbre (lecture) ou ma copie (`…/contre-lecture-commandes-tf/mut/dossier/`),
sous `env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp nice -n 10`, interpréteur `/home/user/controle-ia-travail/.venv/bin/python`
(3.13.18, pytest 9.1.1).

1. **Diff v2 → v3** (`patch/`) : `patch -p0` des copies v2 (`644dbb39…`, `221df610…`, empreintes vérifiées) avec les deux
   `.patch` du dossier, puis `cmp` avec les v3 : **identiques** pour Kimi et pour Argon. Diff indépendant (`diff -u`) : 50 et
   60 lignes `+`/`−`, comme le LISEZMOI. Hors en-tête, Argon ne change que `VERSION`, `ROLES`, `bornes_de_sortie` (neuve),
   quatre lignes de `appeler`, deux options d'`argparse` ; Kimi de même. Section `servir` d'Argon (entre les deux marqueurs
   `# --- relais` et `# --- commande`) : **8 536 octets, identique octet pour octet** à la v2 ; codes 402, 429, 411, 413, 403,
   400, `attentes=(0,)`, `MAX_OCTETS_CORPS = 4_000_000` (l. 107) : inchangés. `registre_depense_cumulee_v1.py` : `cmp` égal à la
   copie `8ba92066…`.
2. **Empreintes** : `sha256sum -c EMPREINTES-commandes-tour-ferme-v1.txt` : 8 OK ; les 9 compagnons `.sha256` (dont celui du
   fichier d'empreintes, `5acc6604…`) : OK, chacun égal à la ligne correspondante ; revérifié après le redémarrage, dossier
   committé à `9dbe15a1`, arbre propre.
3. **Suite d'essais** (`pytest-sain.txt`) : `cd <dossier> && env -i … python -B -m pytest -q -p no:cacheprovider
   test_commandes_tour_ferme_v3.py` → **51 passés, 0 échoué, 29,72 s** (23:30:19 à 23:30:49 UTC). Faux relais : `HTTPServer(("127.0.0.1", 0))`,
   port éphémère, boucle locale ; les trois adresses hors boucle (`10.0.0.1`, `https`, chemin `/autre`) sont refusées par
   `verifier_url` avant toute connexion ; `test_servir_*` : serveur local, `ProxyHandler({})` ; aucune connexion sortante.
4. **Banc de mutations livré** (`mutations-banc.txt`) : `python -I -B mutations_commandes_tour_ferme_v3.py` → cas sain passé
   (51, 29,8 s), **23 tuées sur 23, code 0**, 23:33:09 à 23:38:26 UTC, rien d'autre lancé pendant ce temps.
5. **Mes mutations** (`mes-mutations.txt`, copie du dossier, même banc réutilisé ; C9 à C12 rejouées après le redémarrage) :

   | id | fichier | mutation | sort |
   |---|---|---|---|
   | C1 | Kimi | `lecteur_test` prend les bornes du proposeur | tuée (1 failed, 25 passed) |
   | C2 | Argon | idem | tuée (1 failed, 29 passed) |
   | C3 | Kimi | `cout_usd` = 0 sur code 4 | **SURVIT** (51 passed) |
   | C4 | Argon | idem | **SURVIT** |
   | C5 | Argon | `envoye` vrai sur un refus 402/429 | tuée (1 failed, 49 passed) |
   | C6 | Kimi | idem | **SURVIT** |
   | C7 | Kimi | délai dépassé → code 3 au lieu de 6 | **SURVIT** |
   | C8 | Kimi | gestionnaires de signaux retirés | **SURVIT** |
   | C9 | Kimi | contrôle du modèle servi retiré | **SURVIT** |
   | C10 | Argon | contrôle du modèle servi retiré | **SURVIT** |
   | C11 | Argon | coût d'un échec pris au chiffre du relais, pas au pire cas réservé | **SURVIT** |
   | C12 | Kimi | garde d'étape débranchée (`plafond_etape_usd=None`) | tuée (1 failed, 14 passed) |

   Les trois mutations demandées par la commande : C1/C2 tuées, C3/C4 survivent, C5 tuée et C6 survit.
6. **Expériences** (`experiences.txt`, `mes_experiences_v1.py`, 23:38:37 à 23:39:03 UTC ; les tracebacks `BrokenPipeError`
   du fichier viennent de mon faux relais lent, qui répond après le départ du client, sans effet) :
   - E1, garde d'étape partagée : voir B1 (code 4 d'Argon après 5,95 USD de Kimi ; témoin à 44,00 → code 0).
   - E2, `--delai-s 1` contre un relais qui répond en 4 s : Kimi et Argon → **code 6**, `cout_usd` = `pire_cas_usd`
     (0,012386 ; 0,05025), `cout_origine: pire_cas`, `envoye: true`, ligne `fin` au registre avec `code: 6`, 1,1 s.
   - E3, SIGTERM puis SIGINT pendant l'appel (relais à 6 s, `--delai-s 30`) : Kimi et Argon → **code 6**, « signal 15 » /
     « signal 2 », coût = pire cas réservé (0,162252 ; 0,20002667), ligne `fin` au registre `code: 6`.
   - E4, limites recalculées avec les fonctions des commandes (`max_tokens_permis` et corps JSON réel ; `pire_cas` d'Argon),
     consigne ASCII : Kimi lecteur 0,10 → 47 883 (sortie pleine jusqu'à 43 883) ; Kimi expérimentateur 0,80 → 378 402 (pleine
     jusqu'à 318 882) ; reste 0,10 → 28 402 ; Kimi proposeur 0,50 → 228 402, `max_tokens` 49 756 pour une consigne courte ;
     Argon vérificateur 0,10 → 27 000 (pleine jusqu'à 15 000) ; Argon expérimentateur 0,80 → 225 000 (180 000) ; Argon
     proposeur 0,50 → 135 000, `max_tokens` 9 993. **Tous égaux au tableau du LISEZMOI** (à main : lecteur Argon
     0,10 − 200 × 50e-6 = 0,09 = N/3 × 10e-6 → N = 27 000 ; expérimentateur Kimi 0,80 − 4 096 × 10e-6 = 0,75904 = (N + 1 119) × 2e-6 →
     N = 378 401, l'octet d'écart vient du chiffre de `max_tokens` dans le corps).
   - E5, option inconnue : Kimi → code 2 avec ligne JSON ; Argon → code 2, sortie standard vide (mineur 1).
   - E6, faux relais Kimi répondant 402 : code 3, `envoye: false`, coût plancher (mineur 2).
7. **Contrat de l'adaptateur** (lecture, `adaptateurs.py` l. 600-775 ; `adaptateurs_v56.py` l. 55-80 et 105-140) : environnement
   minimal (`PATH`, `HOME`, `LANG`, `LC_ALL`, `TMPDIR`, `PLAFOND_SESSION_USD` = `repr(float)`, `ROLE_POLE`, `MODELE_DEMANDE_POLE`,
   `ETAPE_POLE`, `PLAFOND_ETAPE_USD` = `f"{p:.2f}"`) ; les commandes ne lisent que ces cinq variables (plus `GEMINI_API_KEY`
   dans la seule sous-commande `servir`), aucun mandataire (`ProxyHandler({})`), aucun en-tête d'autorisation
   (`test_aucune_cle_lue_ni_transmise`). Dernière ligne : `texte` chaîne, `cout_usd` fini > 0 (plancher 1e-6 dans `rendre`,
   arrondi à 6 ou 8 décimales, jamais nul pour un coût ≥ 1e-6), `modele_servi` = `--modele` exigé pour le code 0 (sinon code 5),
   `envoye` sur toute ligne (codes 2, 4, 5, 6, signaux), `role` et `version` sur toute ligne. `MODELE_DEMANDE_POLE` ≠ `--modele`
   → code 2 ; absent → permis. `ETAPE_POLE` et `PLAFOND_ETAPE_USD` : ensemble ou absents, sinon code 2. Délai `--delai-s 1750` <
   1 800 s de l'adaptateur : la commande rend sa ligne avant l'arrêt du groupe (`os.killpg`) ; un arrêt par l'adaptateur
   laisserait un `debut` sans `fin` au registre, compté au pire cas pour toujours (côté prudent). Les quatre rôles acceptés ;
   pour `lecteur_test` : 1 000 / 200 ; `experimentateur_test` et `juge_ideation` : `--max-sortie-court` / `--sortie-min-jetons`
   (16 000 / 4 096 Kimi, 4 000 / 1 000 Argon) ; proposeur : 65 536 / 4 096 et 32 000 / 1 000 — conformes à l'annexe A.
8. **Commandes du LISEZMOI pour la configuration v3** (l. 105-125) : toutes les options existent dans `argparse` des deux
   commandes (Kimi l. 87-101 ; Argon `appeler` l. 427-437, sous-commande `appeler` en tête), défauts égaux à l'annexe A ;
   `--registre {REGISTRE}` et `--plafond-cumule-usd 50` à la forme attendue par `substituer_commandes` ; `--modele` égal au
   `modele` de `proposeurs` à écrire tel quel. Seule réserve : l'interpréteur (mineur 4) et, bien sûr, B1.

## 6. Non vérifié

- Aucun relais réel (8804, 8805) lancé, aucun modèle : le 502 « modèle servi différent » du relais Kimi et le dépassement de
  réserve (`depassement_reserve`) ne sont pas rejoués ici (code v2 inchangé ; le LISEZMOI renvoie à `test_gardes_mini_course_v2.py`).
- Le lanceur v63 n'a pas été joué de bout en bout avec une configuration v3 (aucun fichier de configuration v3 fourni) : la
  substitution et l'empreinte des arguments au manifeste sont lues, pas exécutées.
- Tailles réelles des consignes de l'expérimentateur et du vérificateur (I1) : estimations à partir des constantes de l'étage,
  pas de fiche réelle sous la main ; nombre de jetons réel par octet chez Kimi : non mesuré (le pire cas en suppose un par octet).
- `TAILLE_MAX_LIGNE_LECTEUR` et `MAX_LIGNES_RESULTAT` : lues dans la v2 (`from .tests_de_mort_v4 import *`, chaîne v2 → v3 → v4
  → v5 non suivie ligne à ligne) ; marquées « estimation » dans I1.

## 7. Fichiers lus et empreintes

Dossier contre-lu (`wt-commandes-tf`, `9dbe15a1`, `sha256sum -c` OK) : `commande_kimi_v3.py` `bb303f50…` ;
`commande_argon_v56_nuit_v3.py` `95fa4064…` ; `registre_depense_cumulee_v1.py` `8ba92066…` ; `test_commandes_tour_ferme_v3.py`
`961d471b…` ; `mutations_commandes_tour_ferme_v3.py` `87ee623c…` ; `diff-kimi-v2-v3.patch` `e0e9c2dd…` ; `diff-argon-v2-v3.patch`
`babc7812…` ; `LISEZMOI-commandes-tour-ferme-v1.md` `a8cc68ae…` ; `EMPREINTES-commandes-tour-ferme-v1.txt` `5acc6604…`.
Copies v2 (`scratchpad/commandes-nuit-v1/`) : `commande_kimi_v2.py` `644dbb39…` ; `commande_argon_v56_nuit_v2.py` `221df610…` ;
`registre_depense_cumulee_v1.py` `8ba92066…`.
Contrat (`/home/user/ideation-organism`, `53aef4a`, lecture seule) : `orchestrator/pole/adaptateurs.py` `a1a8ede8…` (l. 560-790) ;
`pole/adaptateurs_v56.py` `d36c79b2…` (l. 1-170) ; `pole/tests_de_mort_v5.py` `da524871…` (l. 93-186, 249-254, 335-485, 601-631) ;
`pole/tests_de_mort_v2.py` `363a3725…` (constantes l. 133-190, `vue_lecteur` l. 2194-2212) ; `pole/tour_ferme_v63.py`
`9982ae3c…` (l. 124-125, 685-726, 795-830) ; `demonstrations/tour_ferme_v63.py` `33e4c029…` (l. 63, 72, 245-282) ;
`demonstrations/attaque_goodhart_v2.py` `58609e0c…` (l. 233-250) ; `pole/etage_entre_generations_v57.py` `e4bf3681…` (l. 69-84) ;
`pole/protocole_outils.py` `0657eec8…` (l. 170-176) ; `prereg/preenregistrement-tour-ferme-v1-brouillon5.md` `c81aa6ef…`
(l. 745-871, et l. 3, 15-21, 565, 596-597 pour les parts 44 et 6).
Mes fichiers (`scratchpad/contre-lecture-commandes-tf/`) : `pytest-sain.txt`, `mutations-banc.txt`, `mes-mutations.txt`,
`experiences.txt`, `patch/` (v2 patchées), `mut/dossier/` (copie du dossier, `mes_mutations_v1.py`, `mes_experiences_v1.py`).
