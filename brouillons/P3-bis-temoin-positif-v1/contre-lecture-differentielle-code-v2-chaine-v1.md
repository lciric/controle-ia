# Contre-lecture différentielle de P3-bis — code corrigé v2 (`02217f1c`) et chaîne de session (`776b26cb`) — v1

- **Contre-lecteur** : celui de la contre-lecture du code (`contre-lecture-code-p3bis-v1.md`, `7a074ad1…`), Claude Fable 5.2 (`claude-fable-5-2`), autre modèle que les deux développeurs (Opus 5.5). Je n'ai écrit ni le code, ni la chaîne, ni les brouillons.
- **Heures** (toutes relevées par `date -u`) : début 2026-11-10 07:17:05 UTC ; arbre détaché créé à 07:17:31 ; cinq bancs de 07:18:12 à 07:21:56 ; répétition jouet de 07:18:12 à 07:27:48 ; liste ciblée v2 de 07:27:58 à 07:44:14 ; arbre et dossiers temporaires retirés à 07:45:08 ; rapport écrit ensuite.
- **Consigne** : `…/consigne-contre-lecture-differentielle-p3bis-code-v2-chaine-v1.md` (`62916a28…`, vérifiée) ; interdits communs v2 (`1ee3b370…`, vérifiés), règle 9 comprise.
- **Interdits tenus** : aucun fichier interdit ouvert ; **aucun fichier de T0.7 lu** (ni brouillon, ni `src/controle_ia/t07/`) ; aucune recherche récursive hors `git grep` sur des fichiers nommés ; aucun appel externe, aucun `vastai` réel (les bancs jouent un faux outil), aucune dépense ; rien dans `/home/user/wt-p3bis-lanceur`. Écritures git : les seules commandes d'arbre détaché que la consigne prescrit (`worktree add`, `sparse-checkout`, `checkout --detach`, `worktree remove`), rien d'autre. **Aucun refus de permissions ni de classifieur.**
- **Lieu** : `/home/user/wt-p3bis-cl`, détaché à `776b26cb`, extraction partielle de la consigne (`docs/sources/` et `docs/notes/bras-attaque/` non extraits, vérifié) ; 9,2 Go libres avant, 9,8 Go après ; arbre retiré à la fin.
- **Lu** : compte rendu du code v2 (`f6c93bc5…`, vérifiée) ; rapports de la chaîne (`748568cb…` et `59e1da14…`, vérifiées) ; sortie de l'essai de fermeture v2 (`06e84ff7…`, vérifiée) ; `ouverture_p3bis_v2.py` (l. 100-400 et 596-1324) ; `essai_fermeture_p3bis_v2.py` (en-tête, règle, constats) ; différences des scripts de l'instance et de la liste v1 → v2 ; de la chaîne : lanceur, récupération, destruction, scellement, répétition finale (entiers), surveillance, contrôles avant dépense et module commun (parties utiles : GO, instances, identifiant, motif, dépense, preuves, blocs 2 à 10) ; en-têtes des cinq bancs et de la répétition jouet ; `registres/go.md` (lignes des deux GO) ; R-2077, R-2085.
- **Empreintes** : les dix fichiers du code v2 sont égaux à leurs compagnons et à `02217f1c` ; l'arbre de `776b26cb` hors `brouillons/` et `docs/` est identique à celui de `02217f1c`.
- **Non vérifié, déclaré** : la concordance du journal des ouvertures avec le lecteur de T0.7 (ce lecteur m'est interdit) ; `controle_cinq_minutes_p3bis_v1.sh` et les corps des bancs, non lus ligne à ligne (joués).

## Verdict

**Conforme sous réserves** : les trois défauts bloquants du code sont réglés et la chaîne de session est écrite et éprouvée ; rien n'est lançable avant le candidat, et deux points de procédure arrêteraient aujourd'hui la répétition finale et le scellement (CD-02, CD-03).

## Essais rejoués

| essai | heures (UTC) | résultat |
|---|---|---|
| banc du module commun (pytest) | 07:18:12 – 07:18:18 | 140 passés |
| banc du lanceur | – 07:18:43 | 56 cas, 0 non conforme |
| banc de la surveillance et du contrôle à cinq minutes | – 07:18:56 | 99 cas, 0 non conforme |
| banc de la récupération et de la destruction | – 07:20:07 | 44 cas, 0 non conforme |
| banc des contrôles avant dépense | – 07:21:56 | 40 cas, 0 non conforme |
| **cinq bancs** | 3 min 44 s | **379 cas, 0 non conforme**, codes 0 (compte du développeur retrouvé) |
| répétition jouet | 07:18:12 – 07:27:48 (576 s) | code 0, dernière ligne « RÉPÉTITION JOUET DE LA CHAÎNE DE P3-BIS : CONFORME », 0 « NON CONFORME » |
| liste ciblée v2 (30 fichiers) | 07:27:58 – 07:44:14 (974,09 s) | **485 passés, 43 échecs, 3 erreurs, 0 sauté** — non opposable, voir ci-dessous |

**Liste ciblée, 46 échecs et erreurs : tous de mon extraction, aucun du code.** L'extraction prescrite retire `docs/sources/`, or `controle_ia/environnements/invites.py` (l. 15) y lit les invites : les 46 portent le message « docs/sources/invites-2606.08892-v1 … absent » (74 occurrences au journal). Aucun ne vient des quatre fichiers d'essais neufs de la v2 ni des essais v1 d'ouverture, de lecture et de fermeture ; trois sont dans `test_premier_test_ia_run_v2.py` (qui appelle `charger_invite`). Le compte de 531 du développeur n'est donc **ni confirmé ni infirmé** ici ; les 95 essais neufs passent. Une liste ciblée ne se compte que sur un arbre où `docs/sources/` est extrait.

Fichier commun `/home/user/controle-ia-travail/.git/info/exclude` : 244 octets, daté 05:42:07, inchangé avant, pendant et après mes essais (la ligne `/x/` de l'incident y est toujours).

## Table des défauts

| # | gravité | fichier, ligne | défaut | correction proposée |
|---|---|---|---|---|
| CD-01 | à corriger | `ouverture_p3bis_v2.py` l. 366-381 | L'incident de `.git/info/exclude` (R-2085) **peut se reproduire** : seul l'essai est protégé (`GIT_CEILING_DIRECTORIES`). `exclure_localement` suit toujours `git rev-parse --git-path info/exclude` : appelée sur un sous-dossier d'un dépôt, ou sur un arbre lié (`worktree`), elle écrit dans le fichier d'exclusion commun du dépôt englobant. Le chemin réel (clone neuf de la récupération) n'est pas touché. | Dans la fonction : refuser si `git rev-parse --show-toplevel` n'est pas la racine donnée, et si le dossier git est celui d'un arbre lié ; essai d'artefact pour chaque cas. Et retirer la ligne `/x/` restée dans le fichier commun (une personne). |
| CD-02 | **bloquant au candidat** (procédure) | `controles_avant_depense_p3bis_v1.sh` bloc 8 ; épingle `PY` | L'environnement de la session ne passe pas le contrôle des versions : rejoué à sec sur `/home/user/controle-ia-travail/.venv`, 9 dépendances sur 10 égales, **`pypandoc_binary` absent** (épinglé 1.17 dans `requirements-donnees.txt`). Avec ce `PY`, le bloc 8 rend KO : ni répétition finale, ni création. Il est aussi en Python 3.13, alors que N se compte sous 3.11. | Construire un environnement Python 3.11 (présent : `/usr/bin/python3.11`) par `requirements-gpu.txt`, l'épingler dans `PY` des contrôles et de la récupération, y compter N. |
| CD-03 | **bloquant au candidat** (procédure) | `sceller_p3bis_v1.sh` l. 81 ; `controles_avant_depense_p3bis_v1.sh` bloc 5 | Le scellement et le bloc 5 lisent `registres/go.md` **de la branche de scellement**. Or la lignée du code (tirée de `main` `04a1b392`) n'a pas la ligne `GO-2026-11-10-02` : zéro ligne à `776b26cb`, le commit `39a3a506` n'en est pas ancêtre. Et fusionner `main` est exclu : 197 fichiers de `src`, `scripts` et `tests` diffèrent, l'arbre gelé changerait. | Sur la branche de scellement, un commit qui porte `registres/go.md` de `main` (et les pièces épinglées), sans aucun chemin de l'arbre gelé ; le dire dans la procédure du candidat. |
| CD-04 | à corriger (procédure) | `repetition_finale_p3bis_v1.sh` l. 29 | La répétition finale refuse sous 12 Go libres ; 9,8 Go libres à 07:45. | Libérer de la place avant le candidat (les dossiers d'essai laissés par le développeur de la chaîne dans son bloc-notes sont à effacer par une personne). |
| CD-05 | à trancher par la mère | `controles_avant_depense_p3bis_v1.sh` l. 297 ; `recuperation_p3bis_v1.sh` l. 86 ; `sceller_p3bis_v1.sh` l. 100 | `verifier-arbre .` est joué sur des clones entiers, où `docs/notes/bras-attaque/` est extrait : l'outil hache ce dossier, ce que la règle 9 des interdits v2 écarte pour les sous-agents. | Clones en extraction partielle sans ce dossier, ou vérification limitée aux chemins utiles (`runs`, `diag`, `traces`, `prereg`, chaîne). |
| CD-06 | mineur | `scripts/essais-cibles-p3bis-v2.txt` | La liste garde trois fichiers d'essais des modules v1 que la chaîne n'emploie plus (reste de CP-15 : l'un importe un module de T0.7 ; l'essai de fermeture v1 ajoute ≈ 3,5 min payées). | Liste v3 sans eux, comme le propose le développeur (E-4), **avant** de compter N ; elle change l'empreinte écrite dans le script de l'instance, donc le commit du code. |
| CD-07 | mineur, au texte | `surveiller_p3bis_v1.sh` l. 68-103 ; `detruire_p3bis_v1.sh` l. 27-28 | Après un code 5, un contrôle à cinq minutes en échec ou tout motif autre que FIN, l'instance reste arrêtée, non détruite, et plus rien ne relève sa dépense de stockage ; toute relance est refusée tant qu'elle est sur le compte (écart 19). | Écrire au texte la règle de sortie (destruction par l'identifiant sur décision, ou lanceur neuf) et qui relève le stockage. |
| CD-08 | mineur | `ouverture_p3bis_v2.py` l. 1131-1142 | `ouvrir --date-paquet` reste fixée par l'appelant ; elle ne commande que la réserve « écrit après la lecture fermée ». | Prendre la date du commit du paquet quand il existe, l'argument seulement à défaut. |
| CD-09 | ouvert | `ouverture_p3bis_v2.py` l. 163-180, 672-791 | Concordance du journal avec le lecteur de T0.7 non vérifiée par moi ; les choix E-3, E-8 et E-9 du développeur (codes des cas non nommés, croisement des modes) en sont les points sensibles. | Relecture par un agent qui a le droit de lire ce lecteur. |

## Point 1 — Différentiel du code (`e86a6f32` → `02217f1c`)

Changements : dix-neuf fichiers ajoutés, un seul modifié (`tests/test_cibles_invisibles_v1.py`, une entrée de `REGISTRE`). Aucun fichier de P3 ni du code v1 n'est touché.

| défaut | état | constat |
|---|---|---|
| CP-01 | **réglé** | trois décisions (l. 152-153, 917-945) ; « ouvrir » sans garde adaptée conforme : refus en tout mode (l. 1108-1118) ; `pleine-anticipee` seulement sous « ouvrir pleinement » ; une seule « ouvrir pleinement » après une ouverture `reduite` lue au journal (l. 962-982) |
| CP-02 | **réglé**, un reste | format exact, six cellules, codes de la liste fermée, ligne vérifiée avant l'écriture, journal relu à chaque tentative, `deja-ouverte` (l. 672-791, 1046-1056) ; reste : CD-09 |
| CP-03 | **réglé** | quatre passages par issue, règle des plages à 16 octets, contrôle « 4 096 zéros » ; sortie versée : plage totale 11, plus grande plage d'une issue 9 |
| CP-04 | **réglé** | 8 octets de longueur, bornes et fin de flux contrôlées (l. 293-312) |
| CP-05 | **réglé** | `durees-lectures-v1.json` écrit dans l'espace fermé avant `fermer` (l. 633-641) |
| CP-06 | **réglé** | `JournalImpossible`, refus, rien d'ouvert (l. 771-790) ; la ligne est écrite avant l'extraction |
| CP-07 | **réglé** | inventaire de l'arbre, chemins ignorés compris ; contrôle « fichier resté en clair » |
| CP-08 | **réglé** | plus d'option `--instant` (l. 1263-1284) ; reste voisin : CD-08 |
| CP-09 | **réglé** | essais d'artefact annoncés présents ; cas sain décisif et chaîne fermée décisive joués (et rejoués ici par le banc de la récupération) |
| CP-10 | **réglé** | inscription au `REGISTRE`, fonction d'essai intacte ; compagnon réécrit à la main (E-2) : acceptable, à consigner |
| CP-11 | **réglé** | motif du dépliage imprimé, motif de `fermer` gardé dans l'espace fermé (l. 642-648) |
| CP-12 | réglé avec un reste | `run_v2.py` et `lecture_p3bis_v1.py` citent encore le brouillon 6 (inchangés, R12) |
| CP-13 | au texte | rien dans le code, comme proposé |
| CP-14 | **réglé** | `SeedSequence(20261110, spawn_key=(i,))`, graines écrites dans la sortie |
| CP-15 | réglé avec un reste | l'essai v2 compare à des chaînes recopiées ; reste : CD-06 |
| CP-16 | **réglé** | accord exigé pour les lignes 2 à 5, sceau vérifié (l. 1249-1259) |
| CP-17 | réglé avec un reste | antériorités strictes ; code 5 pendant un arrêt ; `fermer` seul garde `--entropie` facultative (la chaîne ne l'appelle jamais seul) |

**Régressions** : aucune trouvée. **Essais R5 neufs** : 95 (73, 6, 7, 9), tous passés ici. **Incident R-2085** : non clos dans le code (CD-01).

## Point 2 — Chaîne de session

- **Contrôles du point 6 de ma contre-lecture** : tous écrits, chacun avec cas sain et artefact dans les bancs — GO et révocation, date limite, texte scellé sans marqueur, commit cité et arbre gelé, identité avec P3, essai de fermeture versé puis rejoué, longueurs, compte N et versions, offre et repli, crédit, instances, `DEPOT_URL`, branche absente. Le GO lu est `GO-2026-11-10-02` et la date le 23 novembre (R-2077) : conforme au registre de `main` (ligne 292, plafond « non cumulé », échéance 2026-11-23), contraire au brouillon 9 tant que le brouillon 10 n'est pas écrit.
- **Arrêts par identifiant (R10)** : `vastai stop instance <id>` et `destroy instance <id>` seulement, après la garde `identifiant` (une seule ligne « instance <id> » des traces, hors des instances tolérées) ; aucun arrêt par motif de ligne de commande.
- **Arrêt à 80 USD** : dépense projetée au prochain relevé, dépense antérieure en argument, bornes prises si un relevé est illisible : conforme, prudent.
- **Code 5** : motif `GARDER`, instance arrêtée et gardée, destruction refusée : conforme (CD-07 pour la suite).
- **Récupération** : clone de la seule branche `calcul/p3bis-reel-v[123]`, `main` refusé par le motif de l'argument ; ajouts seulement, aux chemins permis ; lectures fermées avec `--prereg` et `--entropie` ; index relu à deux chemins exactement ; poussée relue.
- **Sorties en clair** : la récupération n'affiche que les lignes de code, l'empreinte du paquet et, sur refus, le motif du dépliage ; les fichiers restés sont comptés, jamais affichés ; les restes sont relevés avec `--ignored`. Rien hors de la classe 1, à CP-13 près (traces, à porter au texte).
- **Les dix-neuf écarts du développeur** :

| # | avis | raison |
|---|---|---|
| 1 GO et date | au texte (brouillon 10), obligatoire | la chaîne refuse le brouillon 9 tel quel |
| 2 ligne d'accord retirée | acceptable | DB-5 (a) |
| 3 modèle `…-v2/` | acceptable | le texte le nomme |
| 4 noms hors du tableau | acceptable | le banc pytest sous `docs/` garde l'arbre gelé intact |
| 5 surveillance qui arrête elle-même | acceptable, au texte | par identifiant ; « processus mort » lu à la fin de l'amorce |
| 6 projection à 80 USD | acceptable, au texte | ne dépasse jamais ; disque supposé compris, hypothèse à écrire |
| 7 repli écrit | acceptable | la ligne du registre reste à la session |
| 8 recharge non contrôlée | au texte | non lisible par la chaîne |
| 9 instances nommées | acceptable | lecture littérale |
| 10 aucun délai | acceptable | mots de Lazar |
| 11 S et N en arguments | acceptable, au texte | « aucun épisode joué » reste à la session |
| 12 formes de citation | au texte | exigées par les contrôles |
| 13 fichier des longueurs | au texte | pièce neuve épinglée |
| 14 commit du paquet par la session | acceptable, au texte | sur la branche de calcul, avance rapide |
| 15 destruction après FIN seulement | acceptable | CD-07 |
| 16 S à six fichiers | acceptable | suppose CD-03 réglé avant S |
| 17 journaux du développeur | acceptable | les canoniques restent à produire |
| 18 `PY` à épingler | **à corriger au candidat** | CD-02 |
| 19 relance après instance gardée | au texte, décision | CD-07 |
| complément : « motif du dépliage » | acceptable, au texte | ne porte que sur l'intégrité du second paquet |
| complément : six fichiers changés sous le même nom | acceptable tant que rien n'est épinglé | noms définitifs au candidat (R12) |

## Point 3 — Bouchons restants

La répétition finale ne change qu'une ligne des contrôles (le clonage) : elle joue donc **pour de vrai** les quatre blocs bouchés dans le banc — vrai tokeniseur, gardes de `run_v2`, liste ciblée « N passed » exact, essai de fermeture rejoué au commit S. Conditions : CD-02, CD-03, CD-04 réglés, et un accès à Hugging Face (appel externe de la mère, avec ses jetons).

Ce que **rien** ne joue avant la course : la création réelle ; le script de l'instance sur une vraie carte (installation de `requirements-gpu.txt`, modèle, run), éprouvé seulement avec un interpréteur factice ; la chaîne fermée sur les sorties d'un vrai run (le banc de la récupération la joue en mode décisif sur un run fabriqué).

## Point 5 — Ce qui reste avant le scellement

1. **Brouillon 10** : GO et date (écart 1), noms v2, formes de citation, écarts à porter au texte des deux développeurs, CP-13, taille réelle du second paquet, code 5, règle de CD-07 ; relu sur l'écart (contre-lecture 4).
2. **Code** : CD-01 ; liste v3 (CD-06) si la mère la retient. L'un ou l'autre change le commit du code : `02217f1c` ne remplit `COMMIT_CODE_P3BIS` que si rien ne bouge.
3. **`TESTS_ATTENDUS_P3BIS`** : à compter sous Python 3.11, environnement de `requirements-gpu.txt`, arbre complet (avec `docs/sources/`), au commit du code retenu ; 531 reste provisoire.
4. **Épingles `A_EPINGLER`** : treize dans les contrôles (candidat, configuration et consignes relus, code relu, essai de fermeture, longueurs attendues, rapports, `PY`), une dans la récupération (`PY`).
5. **Branche de scellement** : tirée du commit du code, avec `registres/go.md` à jour (CD-03), les pièces épinglées, la chaîne et ses journaux, versés avant S.
6. **Journaux canoniques** des cinq bancs et des deux répétitions, rejoués après épinglage ; répétition finale jouée (jamais encore).
7. **Marqueurs** : `ESSAI_FERMETURE_P3BIS` remplissable (sortie `06e84ff7…`, valable tant que le commit du code ne change pas) ; `IDENTITE_CODE_P3BIS` remplissable (quatorze ajouts selon le développeur, non recompté par moi) ; `EMPREINTES_CODE_P3BIS` remplissable, avec l'essai de fermeture v2 et l'amorce v2 en plus ; `CHAINE_P3BIS` après les passages canoniques ; `LONGUEURS_P3BIS`, empreintes des consignes et de la configuration, `PIECES_SUR_MAIN_P3BIS`, `CONTRE_LECTURE_4_P3BIS` : hors du code.
8. **Hors de mon mandat** : la ligne `/x/` du fichier d'exclusion commun ; les dossiers d'essai laissés par le développeur de la chaîne.
