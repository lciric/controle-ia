# Revérification des corrections de code (R2) — étape 1 « gradient conçu par l'essaim » — commit 5e6876d — v1

- **Relecteur neuf** (R2) : sous-agent qui n'a écrit ni le noyau, ni ses corrections, ni le préenregistrement, ni la
  contre-lecture n° 3. Aucun texte de préenregistrement relu (consigne) ; seul le code est relu.
- **Commit relu : `5e6876d`** (`5e6876de428d9216d175d86aa66ad096047cdf49`, branche `outils/essaim-m3-gradient-v2-travail`,
  d'après le message n° 20 de « session-depot »), arbre des pièces `essaim-m3-refonte-v1/` (sans données). Le diff des
  pièces `diff-4f02bd8-5e6876d-code.patch` (`163752c08ce3…`, compagnon OK) s'applique **à l'envers sans écart** sur cet
  arbre (E0) : le code relu est bien la tête de ce diff. Empreintes des fichiers relus : `travail/sorties/empreintes-code-relu.txt`
  (`boucle.py` `211b73a8…`, `archive.py` `49e068b4…`, `analyse_gradient.py` `9fdeacb9…`, `bac_a_sable.py` `cbd30f34…`,
  `fichiers.py` `8bbc8dfd…`, `garde_fuite.py` `b17d3c82…`, `recherche.py` `8867e183…`, `moisson.py` `6973546e…`,
  `serveur.py` `0a6bd754…`, `cli.py` `0d33b110…`, `appels.py` `72172e2d…`, `tests/test_noyau.py` `6137f924…`,
  collisionneur `213b52ef…`, l'empreinte attendue par `appels.py`).
- **Heure** (UTC, `date -u`) : du 24 octobre 2026, 23:08, au 25 octobre 2026, 00:25.
- **Pièces lues** (compagnons vérifiés, tous OK) : contre-lecture n° 3 (`76f96658ed1e…`), diff, `decisions-lazar-extrait-v1.md`
  (`b8ef839a1952…` : R-371 décision (c) « garde et mesure », R-375 garde approuvée), messages n° 20, 22, 25 de « conv-audit »,
  n° 20 de « session-depot » (`c99b44b286fa…`), `CLAUDE.md`, code et essais de l'arbre, collisionneur.

## VERDICT : **corrections vérifiées avec réserves — dont une réserve bloquante**

Les corrections de code demandées par la contre-lecture n° 3 existent toutes, sauf CE3-17, et chacune a un essai qui
échoue quand on la retire du code (17 mutations sur 18 font échouer l'essai annoncé ; seul le **câblage** de la garde
CE3-04 dans le noyau n'est vérifié par aucun essai). La suite fait foi chez moi comme chez l'auteur : 104 essais réussis,
4 échecs dus seulement à l'absence de la banque réelle, 3 désélectionnés (108 + 3, comme annoncé).

Mais :
- **RV-01 (bloquante)** — la correction de CE3-02 (`reponses_finales` lève une erreur si le fichier manque) repose sur une
  prémisse fausse : le noyau **n'écrit pas** `juge/reponses_test.json` quand l'organisme n'a rien écrit (exception,
  délai dépassé, lien ou tube refusé). La lecture gelée de H-G1 s'arrête alors par une erreur, au lieu de couper la paire ;
  elle s'arrête aussi sur des réponses que le juge accepte (marque d'ordre d'octets). **Rejoué** (E4b, E11).
- **Sept majeures** (RV-02 à RV-08), rejouées chacune : la mémoire de conception reste asymétrique (dossiers vivants des
  rondes lisibles dans A seulement ; avec le même décalage d'utilisateurs, B lit les réponses de A) ; la vue importée
  dans B est lisible par les autres lignées pendant la première ronde ; /tmp, /var/tmp et /dev/shm sont une voie commune
  entre bras, répliques et lignées ; deux lectures de root suivent encore les liens de l'organisme (R-372) et un tube les
  bloque indéfiniment ; sans espace de noms de processus (non exigé en réel), un processus détaché survit ; la garde
  CE3-04 laisse passer les résumés de recherche et les copies courtes, et son refus est un oracle ; les appels encore en
  vol à la fin d'une génération manquent au journal scellé et à la dépense, et la nouvelle garde CE3-07 en fait une
  « anomalie du noyau ».

**Condition** : corriger RV-01 (petite correction, proposée plus bas) — et, recommandé, RV-02 à RV-08 — dans un nouveau
commit, puis une revérification limitée à ces points par un sous-agent neuf, avant le scellement.

Décompte : **1 bloquante, 7 majeures, 5 mineures, 3 de forme** (16 remarques).

---

## Tableau des corrections

« mN » renvoie aux mutations de `sortie-e2-mutations.txt` (correction retirée d'une copie du code, essai annoncé relancé).

| correction | état | preuve |
|---|---|---|
| **CE3-01** mémoire de conception servie à B | **corrigé en partie** | `archive.importer_conception` (l. 161-201), appel dans `boucle.amorcer` (l. 508-515). Rejoué (E1, deux lignées, trois rondes, isolation d'utilisateur) : historique de g000 identique entre A et B hors la clé `importee` ; vue de g000 identique, 63 fichiers, chemins **et contenus** ; même graine ; budget différent par `entrainements_max` seul. L'essai de « conv-audit » échoue sans l'import (m01). Restent : `rondes_conception_max` 3 dans A, 0 dans B (RV-09) ; dossiers vivants des rondes lisibles dans A seulement (RV-02) ; vue importée lisible des autres lignées dans B (RV-03). |
| **CE3-02** rondes comptées comme générations | **corrigé en partie** | `generations_valides` filtre `phase`, `importee`, `invalide` (l. 85). Rejoué en courses simulées (E4a) : A s'arrête à g1, B va à g2 → paire lue à g1 ; avec l'ancien filtre, la génération lue serait 2, absente de A. (b) génération invalidée et (c) lignée sans génération notée valide → paire coupée (essai de l'auteur ; E10). Sans le filtre, l'essai échoue (m02). **Mais** `reponses_finales` (l. 63-76) lève sur des générations valides que le juge traite normalement (RV-01, bloquante). |
| **CE3-03** audit déclenché par l'absence ; sortie gelée | **corrigé, avec réserves** | couverture ≥ 80 % par famille et par bras → paire coupée (`paires_h_g1` l. 183-186 ; m04) ; seuil bas sur les tâches répondues (`exactitude_repondue_par_famille`) ; lignées imposées au seuil haut seul (l. 274-277 ; m05) ; sortie gelée `apres_audit` (l. 241-245 ; m06). Réserves RV-10 : `defaut_paires` mal étiqueté ; seuil bas déclenché par une couverture partielle si l'appelant passe la lignée (E4d, E4e). |
| **CE3-04** (décision (c) : garde et mesure) | **corrigé en partie** | `garde_fuite.py` ; refus dans `recherche.rechercher` (l. 159-166) et quarantaine dans `moisson.telecharger` (l. 299-306), câblés par `boucle._rechercheur` / `_telechargeur` (l. 390-409) ; mesure `recoupements_fuite` et déclencheur d'audit. Rejoué de bout en bout (E5b) : huit mots copiés d'une tâche de test → `REFUSE_FUITE`, recherche non consommée, compté (2). Essais des composants : m07, m08 échouent. **Câblage non essayé** : retiré, toute la suite reste verte (m09, RV-12). Restent : résumés de recherche non filtrés, copies courtes ou altérées ni refusées ni comptées, oracle du refus (RV-07). |
| **CE3-05** conditions extérieures | **corrigé, avec réserves** | HTTP 402 → génération `CREDIT_EPUISE` invalidée, course arrêtée, aussi à l'amorçage (`appels.py` l. 170, `boucle.py` l. 591-595, 731-747 ; m10) ; manifeste : `sources_moisson`, `cle_brave_presente` ; `lancer --depuis` refuse des conditions de moisson différentes (`cli.py` l. 181-193, 229-232 ; m12) ; règle de panne extérieure (> 10 points) rejouée **sur des journaux écrits par le noyau** (E6 : recherches en échec dans A seul → paire coupée ; m11). Réserves : RV-11 (refus de requête de l'organisme compté comme panne, aucun effectif minimal), RV-08 (appels en vol). Le code d'erreur de l'interface d'Anthropic pour un crédit épuisé n'est pas vérifiable ici. |
| **CE3-06** vues de la seule lignée ; utilisateurs par course | **corrigé en partie** | `archive_vue/` 0711, vue de lignée root:groupe 0750, vue déposée 0550/0440, corpus 0750/0640 (`boucle._vue_pour` l. 325-342, `_proteger_lecture_lignee`, `archive.deposer` l. 143-152 ; m13). Dans A, une lignée ne liste ni ne lit la vue d'une autre (E1 : `PermissionError`). `--decalage-uid` validé (E13). Restent : RV-03 (vue importée de B lisible), RV-04 (voie commune /tmp), RV-02 (même décalage permis pour A et B : B lit A), RV-13 (traits non protégés par le code). |
| **CE3-07** dossiers du noyau hors du dossier de l'organisme | **corrigé, avec réserve** | `<travail>.noyau` (root 0700) et `<travail>.corpus` frères de `travail` sous un parent à root 0711 ; noms `noyau`, `corpus` réservés et consignés ; journal des appels absent après des appels → `ANOMALIE_NOYAU` (`boucle.py` l. 529-540, 585-589 ; `archive.deposer` l. 99-107). L'essai de l'auteur (organisme falsificateur) échoue avec l'ancienne disposition (m14). Réserve RV-08 : un appel encore en vol déclenche faussement l'anomalie et arrête la lignée (E8). |
| **CE3-11** garde de temps et moisson | **corrigé (garde)** | `temps_pire_cas` (l. 54-65) : 10 × 60 + 10 × 25 + 4 × 145 + 300 = 1 730 s ; refus en réel, génération et ronde (m15). Non fait dans le code : nombre de cœurs au manifeste (RV-15). |
| **CE3-12** garde de plafond pendant la conception ; raison juste | **corrigé** | `_doit_arreter` sert les deux boucles (l. 731-741) ; « aucune lignée active » (l. 757-759 ; m16). Scénario E9 du rapport n° 3 rejoué (E14) : plafond 0,3 USD → amorçages refusés, raison « aucune lignée active ». |
| **CE3-17** graines ronde k / génération k | **non corrigé dans le code** | `boucle.graine` (l. 309-315) sans la phase : `ordre_train`, `ordre_test`, `organisme` identiques pour c001/g001 et c002/g002 (E7). Sans effet sur l'appariement ; à dire dans la v4 (RV-14). |
| **CE3-18** points de code | **corrigé en partie** | `fin_conception.json` lu borné à 20 000 octets, sans lien ni tube (`fichiers.py` l. 26, `boucle.py` l. 676-687) : corrigé. `sources_moisson` ajouté, mais `"recherche": "arxiv"` reste au manifeste en réel alors que trois ou quatre sources sont servies (E10, RV-15). Redirections de la moisson : laissées au texte (choix de l'auteur), sans objet ici. |
| **R-372** liens symboliques suivis par root | **corrigé en partie** | `fichiers.py` (lecture `O_NOFOLLOW`/`O_NONBLOCK`, même inode, taille bornée ; copie sans lien) utilisé par le dépôt, l'import, les réponses, la métrique, la fin de conception, le successeur, l'entraîneur, la confrontation. Sans le correctif, le noyau muté copie sans fin (m17 : 7,9 Go en 17 min, arrêté par son PID) ou se bloque sur un tube (m18). Restent : `statut_execution.json` et `erreurs.txt` lus en suivant les liens, et un tube y bloque le noyau (RV-05, E3) ; la garantie dépend de l'espace de noms de processus, non exigé en réel (RV-06, E3). |

### Les essais annoncés prouvent-ils ce qu'ils disent ? (sain et artefact, R5)

Oui pour l'essentiel, au niveau où ils sont écrits (mutations m01 à m16 : chaque correction retirée fait échouer son
essai). Limites : le câblage de la garde CE3-04 par le noyau n'est essayé par rien (m09) ; l'essai de CE3-01 compare
les noms de la vue, pas ses contenus (E1 l'a fait : identiques) ; l'essai CE3-06 vérifie des modes, pas une lecture par
une autre lignée (E1 l'a fait), et ne couvre pas la vue importée de B ; l'essai du poseur de liens ne pose aucun lien sur
`statut_execution.json` ni `erreurs.txt` ; l'artefact annoncé du dépôt (« essai en échec ») ne finit pas (m17) ;
`test_ce307…` accepte `FileNotFoundError` comme preuve d'un refus ; le tirage à trois niveaux n'est discriminé par aucun
essai (E15) ; `test_h_g1_couverture…` consacre le comportement de RV-01 (erreur sur fichier absent).

---

## Remarques

### RV-01 — bloquante — La lecture gelée de H-G1 s'arrête sur des générations que le juge traite normalement

- **Fichiers** : `essaim_m3/analyse_gradient.py` l. 63-76 (`reponses_finales` : « CE3-02 : … le fichier d'une génération
  dite valide doit exister (il est écrit à chaque dépôt, même vide) » ; `raise FileNotFoundError` l. 69 ;
  `json.loads(f.read_text(encoding="utf-8"))` l. 70) ; `essaim_m3/noyau/archive.py` l. 118-120 (`reponses_test.json`
  n'est déplacé dans `juge/` que s'il existe) ; `boucle.py` l. 606-626 (le juge lit en `utf-8-sig`, borné à 4 Mo, refuse
  liens et tubes, et compte une absence comme « sans réponse ») ; `tests/test_noyau.py` l. 2414-2416 (l'essai exige
  l'erreur).
- **Défaut** : la docstring est fausse : rien n'écrit `juge/reponses_test.json` « même vide ». Quand l'organisme n'a
  rien écrit (exception, délai dépassé — courant à 1 800 ou 2 400 s —, `reponses_test.json` lien ou tube écarté par
  R-372), la génération reste **valide** (`invalide` faux, statut `EXCEPTION` ou `DELAI_DEPASSE`), le juge la note
  « sans réponse », mais `paires_h_g1` lève `FileNotFoundError` : aucune paire coupée, aucune règle d'un quart, aucune
  lecture. Le bras B, où `entrainer` rend `INDISPONIBLE` à des organismes conçus avec le gradient, est le plus exposé.
  De même, le juge accepte des réponses avec marque d'ordre d'octets (essai `test_organisme_avec_marque…`), l'analyse
  les relit en `utf-8` strict et lève `JSONDecodeError` ; un fichier de plus de 4 Mo est refusé par le juge et relu en
  entier par l'analyse. Une lecture gelée qui s'arrête force un écart au préenregistrement scellé (R1, nœud de décision).
- **Preuve rejouée** : E4b (`sortie-e4-lecture-h-g1.txt`) — organisme qui lève une exception sans gradient : B g000 et
  g001 valides (statut `EXCEPTION`), `juge/reponses_test.json` absent, `score.json` « reponses_test.json absent » ;
  `paires_h_g1` lève `FileNotFoundError`. E11 (`sortie-e11-marque-d-ordre-d-octets.txt`) — réponses écrites en
  `utf-8-sig` : juge 12 réponses lues, score 0,5 ; `reponses_finales` lève `JSONDecodeError`.
- **Correction proposée** : une seule règle de lecture, celle du juge. À chaque dépôt d'une génération notée, le noyau
  écrit et scelle `juge/reponses-lues.json` : le dictionnaire des réponses **retenues par le juge** (`{}` s'il n'en a
  retenu aucune) avec `probleme_reponses` ; `reponses_finales` ne lit que ce fichier (son absence est alors une vraie
  anomalie, et l'erreur est juste) ; `{}` donne une couverture nulle, donc une paire coupée par CE3-03, comptée dans la
  règle d'un quart. Essais : sain (organisme sans réponse → paire coupée « couverture » ; réponses avec marque → lues),
  artefact (fichier effacé → erreur).

### RV-02 — majeure — Mémoire de conception encore asymétrique (dossiers vivants) ; décalage d'utilisateurs égal permis entre A et B

- **Fichiers** : `boucle.py` l. 529-540 (dossiers vivants `travail/<lignée>/cNNN` et `cNNN.corpus` jamais effacés après
  le dépôt) ; `moisson.py` l. 327 (`fichier_texte` : chemin absolu dans le corpus vivant) ; `cli.py` l. 343 (aide de
  `--decalage-uid` : distinct seulement pour des courses simultanées) ; aucune comparaison avec le décalage de la course
  d'origine dans `_imposes_et_especes` ni `lancer`.
- **Défaut** : dans A, les générations notées gardent l'accès aux dossiers vivants de leurs rondes (même utilisateur) ;
  dans B, seule la copie de la vue existe. Un organisme qui garde ses documents par `fichier_texte` (le contrat l'y invite)
  a sa mémoire dans A, pas dans B : écart dans le sens prédit. À l'inverse, si A et B ont le même décalage (le défaut 0),
  B atteint les dossiers vivants de A, y compris les sorties des générations à gradient.
- **Preuve rejouée** : E1 (A g000 relit ses notes de c001 par chemin ; B g000 : `FileNotFoundError`) ; E9 (document de
  conception relu par `fichier_texte` : A oui ; B décalage 100 : `PermissionError`) ; E9b (B décalage 0 : lecture d'un
  fichier de réponses vivant de A réussie ; décalage 100 : refus).
- **Correction proposée** : effacer les dossiers vivants (`travail`, `.noyau`, `.corpus`) après le dépôt et la copie du
  successeur, pour que la mémoire ne passe que par la vue dans les deux bras ; dire au contrat que `fichier_texte` ne vaut
  que pendant la génération ; refuser `--depuis` si le décalage est celui du manifeste d'origine, et corriger l'aide.
  Essais sain et artefact sur les scénarios E9 et E9b.

### RV-03 — majeure — Dans B, la vue importée d'une lignée est lisible par les autres lignées pendant la première ronde

- **Fichiers** : `archive.py` l. 186-199 (`importer_conception` : `archive_vue/<lignée>` créé avec le masque par défaut,
  rondes importées 0555/0444 à root, sans le groupe de la lignée) ; `boucle.py` l. 325-342 (`_vue_pour` ne protège la
  vue d'une lignée qu'à sa première exécution).
- **Défaut** : régression née de CE3-01 et contraire à CE3-06 : avant le premier passage de chaque lignée, sa vue
  importée est lisible par les lignées qui passent avant elle. Les paires d'une réplique ne sont plus étanches dans B.
- **Preuve rejouée** : E1 — dans B, la première lignée de la ronde 1 liste et lit la vue importée de l'autre lignée ;
  dans A, la même tentative est refusée (`PermissionError`).
- **Correction proposée** : importer la vue avec le groupe de la lignée et les modes de `deposer` (0550/0440), et
  protéger `archive_vue/<lignée>` (0750) aussitôt après l'import ; essai : B à deux lignées, refus attendu.

### RV-04 — majeure — Dossiers inscriptibles par tous partagés entre bras, répliques et lignées

- **Fichiers** : `bac_a_sable.py` l. 214-231 (`unshare` : montage, processus, réseau ; ni /tmp privé, ni `--ipc`).
- **Défaut** : /tmp, /var/tmp et /dev/shm (1777) et l'espace des communications entre processus sont communs à tous les
  organismes : une voie hors de toute vue, entre A et B, entre A_1 et A_2, entre lignées. Le contrat promet « sans accès
  hors de son dossier de travail ».
- **Preuve rejouée** : E1, E1b — un fichier de /var/tmp (lié à mon dossier de travail) écrit par les organismes de A est
  lu par ceux de B, et une lignée de A lit ce qu'une autre y a écrit. L'espace des communications entre processus : déduit
  des options d'`unshare`, non rejoué.
- **Correction proposée** : tmpfs privés sur /tmp, /var/tmp, /dev/shm dans l'espace de noms de montage (avant
  l'abaissement des privilèges), `--ipc` ; sortir de /tmp le repli du socket ; essai sain et artefact entre deux courses.

### RV-05 — majeure — R-372 : deux lectures de root suivent encore les liens de l'organisme ; un tube les bloque

- **Fichiers** : `bac_a_sable.py` l. 255-271 (`executer` relit `statut_execution.json` et `erreurs.txt` par leur nom,
  sans `fichiers.lire_fichier_organisme`).
- **Défaut** : ces deux fichiers sont dans le dossier de l'organisme ; leur relecture suit un lien, n'est pas bornée et
  attend sur un tube. Un champ d'un fichier lisible par root seul peut ainsi devenir le statut de la génération, visible
  de la génération suivante ; un tube bloque le noyau sans fin (course perdue).
- **Preuve rejouée** : E3 (organismes d'essai, simulation) : la relecture suit les deux liens ; avec un tube, noyau bloqué
  après 90 s, arrêté par son PID, génération non déposée.
- **Correction proposée** : lire le statut par `lire_fichier_organisme` (taille bornée) et les erreurs par le descripteur
  que le noyau a lui-même ouvert, jamais par le nom ; étendre l'essai du poseur de liens à ces deux noms.

### RV-06 — majeure — La garantie de R-372 dépend de l'espace de noms de processus, non exigé en réel

- **Fichiers** : `boucle.py` l. 273-290 (le mode réel exige utilisateur et réseau, pas `espaces_noms`) ;
  `bac_a_sable.py` l. 164-186 (`_tuer_groupe` ne tue que la session).
- **Défaut** : sans espace de noms de processus, un processus détaché de l'organisme survit à la génération et à la
  course ; les copies de root faites ensuite ne sont plus à l'abri de modifications concurrentes.
- **Preuve rejouée** : E3 — capacités sans espace de noms : un descendant détaché écrit son témoin après la fin de la
  course (arrêté par son PID) ; avec l'espace de noms : aucun survivant.
- **Correction proposée** : en réel, refuser si `espaces_noms` est faux ; essai sain et artefact.

### RV-07 — majeure — CE3-04 : garde et mesure réelles mais partielles

- **Fichiers** : `recherche.py` l. 159-189 ; `moisson.py` l. 299-323 ; `garde_fuite.py` l. 15-16, 23 ; `contrat.py`
  l. 78-79 ; `analyse_gradient.py` l. 147-155.
- **Défaut** : (i) les résultats rendus par la recherche (titres, résumés) ne passent pas par la garde ; (ii) la mesure ne
  compte que ce que la garde refuse : un passage plus court que la fenêtre, ou légèrement modifié, n'est ni refusé ni
  compté, contrairement à « le comptage, lui, reste la mesure » ; (iii) le refus d'un document et l'empreinte écrite dans
  l'index du corpus, lisible par la lignée, renseignent l'organisme sur le contenu de ce document. Le contrat dit plus que
  ce qui est tenu.
- **Preuve rejouée** : E5a, E5b (simulation, moteurs doubles) : refus et comptage de la copie de huit mots ; un résumé
  rendu qui contient une tâche entière passe sans refus ni compte ; l'empreinte figure dans l'index lisible.
- **Correction proposée** : appliquer la garde à chaque notice rendue (retirée et comptée) ; mesure sans refus des
  recoupements plus courts, consignée dans le journal du noyau et comptée dans `recoupements_fuite` et l'audit ; garder
  l'empreinte dans le seul journal du noyau ; écrire au contrat ce qui est réellement refusé.

### RV-08 — majeure — Appels en vol à la fin d'une génération : journal scellé incomplet, dépense sous-comptée, fausse anomalie CE3-07

- **Fichiers** : `serveur.py` l. 65-83 (`__exit__` n'attend pas les fils de service) ; `boucle.py` l. 576-603 et 664
  (dépense lue et journal déposé aussitôt).
- **Défaut** : un appel servi mais non fini quand l'organisme se termine (délai dépassé avec des appels en parallèle)
  continue après la génération ; sa ligne manque au journal scellé et son coût à la dépense totale (plafond et GO
  sous-comptés) ; la détection du 402 et la règle de panne ne le voient pas. S'il n'y a encore aucune ligne, la garde
  CE3-07 invalide la génération comme « anomalie du noyau » et arrête la lignée.
- **Preuve rejouée** : E8 (un appel en vol : `ANOMALIE_NOYAU`, lignée arrêtée, coût absent) ; E8b (deux appels : une ligne
  manque au journal scellé, 0,00552 USD absents du total).
- **Correction proposée** : à la sortie du serveur, cesser d'accepter puis attendre les fils en cours (borne : délai
  maximal d'un appel) avant de lire la dépense et de déposer ; à défaut, journaliser l'appel à son départ et compter
  `n_appels` à son arrivée ; essai sain et artefact.

### RV-09 — mineure — CE3-01 : contexte de B encore distinct de celui de A
- `boucle.py` l. 551, `cli.py` l. 75-77 : `rondes_conception_max` vaut 0 dans B (3 dans A, E1) ; historique marqué
  `importee`, vue de B marquée `impose`. Un organisme qui conditionne sa mémoire à `rondes_conception_max` ne l'utilise pas
  dans B. Correction : passer la valeur du manifeste d'origine (sans conception) ; dire ces marques au contrat.

### RV-10 — mineure — CE3-03 : sortie gelée et déclencheurs à resserrer
- `analyse_gradient.py` l. 241-245 : `apres_audit="defaut_paires"` rend le verdict avec la réserve « sans défaut trouvé »
  et lit la table sans paires coupées (E4d). Le seuil bas sur tâches répondues se déclenche sur une couverture partielle si
  l'appelant passe une paire déjà coupée (E4e) ; aucune fonction gelée ne compose paires, coupes, déclencheurs et lecture.
  Correction : refuser `defaut_paires` tant que les paires ne sont pas recoupées (ou réserve juste) ; une fonction gelée
  unique de lecture, avec son essai.

### RV-11 — mineure — CE3-05 : la règle de panne compte des erreurs de l'organisme
- `analyse_gradient.py` l. 116-144 : tout `ECHEC_API` compte, même un refus de requête causé par l'organisme (HTTP 400 :
  2/10 contre 0/10 → paire coupée, E7) ; aucun effectif minimal (1 sur 1 = 100 points, E6). Correction : causes
  extérieures seules (402, 429, 5xx, connexion, délai) et un minimum d'échecs avant de couper.

### RV-12 — mineure — CE3-04 : câblage non essayé ; effet en simulation
- Retirer le câblage des empreintes dans `boucle._rechercheur` / `_telechargeur` laisse la suite verte (m09). En
  simulation, tout document à phrase d'indice est mis en quarantaine (E1 : 12 sur 12 ; E4c : recoupements 3 et 3) : chaque
  paire simulée déclenche l'audit ; l'essai de moisson de bout en bout ne passe que parce que ses six tâches de test ne
  contiennent pas la phrase. 39 % des fenêtres de test sont aussi dans l'entraînement de la banque simulée (E5a).
  Correction : essai de bout en bout (sain et artefact) ; écarter les fenêtres présentes aussi dans l'entraînement ;
  mesurer la part partagée sur la banque réelle.

### RV-13 — mineure — CE3-06 : les traits ne sont pas protégés par le code
- `cli.py` l. 213-217 met la banque en 0600, rien pour `--traits`. Correction : même traitement (ou refus si lisibles par
  d'autres), défense de second rang pour CE3-06 (b).

### RV-14 — forme — CE3-17 non corrigé dans le code
- `boucle.py` l. 309-315 (E7). La phase dans la clé de dérivation, ou le dire dans la v4.

### RV-15 — forme — Manifeste et temps
- `boucle.py` l. 257 : `"recherche": "arxiv"` reste à côté de `sources_moisson` (E10) ; nombre de cœurs non consigné
  (CE3-11) ; les délais réseau de la garde de temps sont par opération, pas une borne stricte.

### RV-16 — forme — Essais et empreintes
- Artefact du dépôt annoncé « en échec » : copie sans fin (m17) — viser un dossier hors de la destination ; m18 se bloque
  au lieu d'échouer ; `test_ce307…` accepte `FileNotFoundError` ; aucun artefact pour un `--decalage-uid` invalide (la
  garde marche, E13) ; tirage à trois niveaux non discriminé (E15) ; `EMPREINTES-v8.txt` périmé pour 12 fichiers du noyau
  et ne couvre ni `fichiers.py`, ni `garde_fuite.py`, ni `analyse_gradient.py` (R6).

---

## Ce que j'ai rejoué

Tout sous `env -i PATH=/usr/bin:/bin HOME=<travail>/home`, `python -B`, environnement `/opt/essaim-m3-venv-v1`, sur une
copie du code dans `travail/code`, en root, dans un espace de noms de montage privé où `/var/tmp` est lié à
`travail/vartmp` (`travail/scripts/dans_ns.sh`). Simulation seulement ; aucun appel réseau, aucune clé, aucune dépense,
aucune commande git, aucun script de la relève de Gemini. Le vrai `/var/tmp/essaim-m3` ne contient aucune empreinte de
mes racines (vérifié). Processus d'essai arrêtés par leur PID (m17, m18, tube, survivant) ; aucun processus laissé.
Empreintes des sorties : `travail/EMPREINTES-sorties.txt` ; scripts et organismes d'essai :
`travail/EMPREINTES-scripts-et-organismes.txt`.

| essai | objet | sortie (`travail/sorties/`) | empreinte |
|---|---|---|---|
| suite | 104 réussis, 4 échecs (banque absente), 3 désélectionnés | `sortie-pytest-complet.txt` | `18543734…` |
| E0 | diff appliqué à l'envers sans écart | `sortie-e0-diff-inverse.txt` | `b1af153c…` |
| E1, E1b | CE3-01, RV-02, RV-03, RV-04 | `sortie-e1-memoire-conception-et-isolation.txt`, `sortie-e1b-canal-var-tmp-detail.txt` | `1cf69bd8…`, `a2296ea0…` |
| E2 | 18 mutations + notes | `sortie-e2-mutations.txt`, `sortie-e2-mutations-notes.txt` | `0b8c930a…`, `ae79c0d7…` |
| E3 | RV-05, RV-06 | `sortie-e3-r372-lectures-et-survivant.txt` | `03ee0d75…` |
| E4 | CE3-02, RV-01, RV-10 | `sortie-e4-lecture-h-g1.txt` | `fabe2599…` |
| E5a, E5b | CE3-04, RV-07, RV-12 | `sortie-e5a-fenetres-partagees.txt`, `sortie-e5b-garde-fuite.txt` | `972b6dba…`, `62f5099e…` |
| E6 | panne extérieure de bout en bout | `sortie-e6-pannes-exterieures.txt` | `b19a4b33…` |
| E7 | CE3-17, manifeste, RV-11 | `sortie-e7-graines-manifeste-pannes.txt` | `30af1f41…` |
| E8, E8b | RV-08 | `sortie-e8-appel-en-vol.txt`, `sortie-e8b-appel-en-vol-deux-appels.txt` | `0782b4ac…`, `8d1dcfce…` |
| E9, E9b | RV-02 | `sortie-e9-memoire-par-chemin.txt`, `sortie-e9b-lecture-du-bras-A-par-chemin.txt` | `1de673fd…`, `7a2d13af…` |
| E10 | CE3-02 (c), manifeste réel, contrôle positif | `sortie-e10-unitaires.txt` | `2aa8fe01…` |
| E11 | RV-01 (marque d'ordre d'octets) | `sortie-e11-marque-d-ordre-d-octets.txt` | `446c8f8f…` |
| E12 | juge et analyse concordent (cas ordinaires) | `sortie-e12-coherence-juge-analyse.txt` | `084c862d…` |
| E13 | garde du décalage d'utilisateurs | `sortie-e13-decalage-uid.txt` | `c2e68d5a…` |
| E14 | CE3-12 (scénario E9 du n° 3) | `sortie-e14-plafond-conception.txt` | `39c428af…` |
| E15 | tirage à trois niveaux non discriminé | `sortie-e15-mutation-tirage.txt` | `76f8f96c…` |

Nettoyé après les essais : copies mutées, dossiers temporaires de pytest, espaces des organismes (`travail/vartmp`).
Gardés : courses simulées (`travail/exp/runs/`), organismes d'essai (`travail/exp/`), scripts.

## Ce que je n'ai pas pu vérifier

- Les courses réelles, la moisson réelle, la banque réelle (4 essais) et la part de fenêtres de test partagées avec
  l'entraînement dans cette banque (RV-12).
- Le code que renvoie l'interface d'Anthropic pour un crédit épuisé (la garde ne reconnaît que HTTP 402).
- Les capacités de l'hôte retenu (instance sans carte) : espace de noms de processus (RV-06), tmpfs privés (RV-04).
- Le lanceur v2 (décalages par course, protection des traits) : non écrit, hors de la tâche.
- L'espace des communications entre processus (RV-04) et une lecture sans fin par un lien vers un périphérique (RV-05) :
  déduits du code, non rejoués.
- Le commit lui-même par git (aucune commande git) : l'arbre est vérifié par le diff des pièces (E0).
