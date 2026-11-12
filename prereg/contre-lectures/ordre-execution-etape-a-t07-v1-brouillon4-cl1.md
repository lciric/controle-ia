# Contre-lecture (R2) de l'ordre d'exécution de l'étape A de T0.7, variante B, brouillon 4 — cl1

Contre-lecteur neuf, sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, modèle Fable 5.2 (`claude-fable-5-2`), d'un
autre modèle que le développeur (Opus 5.5 ; N-052). Je n'ai écrit ni T0.7, ni son module, ni ses ordres, ni leurs contre-lectures.
J'ai lu T0.7 (brouillon 22) : exclu ensuite de tout rôle de lecteur de P3-bis. Consigne :
`docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-contre-lecture-ordre-etape-a-t07-b4-v1.md`
(`63c5f3b7cf3c3f8e71840ed52605c23bbfd1bcf13312cc64839e13d8dc46d91c`, vérifiée par `sha256sum`). Heures relevées par `date -u`, le
2026-11-10 : début 15:36:24 UTC, rapport écrit à partir de 16:08 UTC.

Pièces lues, empreintes vérifiées par `sha256sum` : ordre brouillon 4 (`d5047be2…`), brouillon 3 (`b053a220…`), rapport du
développeur (`88a318d9…`), script `scripts/etape_a_t07_variante_b_v2.sh` (`e68d3306…`, lu en entier), `src/controle_ia/t07/code_t07_v1.py`
(`52f44ce0…`), `registres/code-t07/CODE-T07-v1.json` (`9ef4ede7…`), contre-lecture courte v3 (`d0fe9053…`), contre-lecture courte
de l'option (c) (`7a327462…`, CLC-03, CLC-08), contre-lecture orchestrée du brouillon 22 (`47537dfa…`, GARDES-CODE-01,
CONCORDANCE-01, CLO-08, CLO-09), brouillon 22 de T0.7 (`8b84cba5…` : écrits (b), liste d'arrêt l. 1897-1900, « Calcul et dépense »,
« Module », points 14 à 20 et « Ordre d'exécution »), `registres/go.md` (l. 294 et 296), `registres/decisions.md` (R-2112, R-2115,
R-2153, R-2220, R-2229, R-2231, R-2241, R-2246, R-2249, R-2255, R-2256), `.claude/hooks/garde_calcul.py`,
`src/controle_ia/t06/session_v2.py` l. 88-114 et `session_v7.py` l. 30-45 (garde d'offre de la chaîne de T0.6).

## Verdict

**Scellable après corrections** : douze couples `{ancien, nouveau}` (§ 7), chaque « ancien » présent une seule fois (vérifié par
programme). **Aucun constat bloquant** : l'ordre est exécutable tel quel pour tout ce que j'ai pu rejouer sans clé ni instance.
**Trois constats majeurs à appliquer avant le scellement** : CLE-01 (le prix du téléchargement et celui du stockage de l'offre
ne sont pas bornés, alors que le devis et la minuterie les supposent), CLE-02 (la mère ne reçoit ni l'identifiant ni l'échéance
si la session de la fille tombe), CLE-04 (recopie des lignes d'ouverture dans le journal de `main` avant toute relance, exigée
par T0.7, point 19). **`ATT` est retrouvée sous Python 3.11.17** (§ 3) : le risque S-2 est réduit à la construction carte de
`torch`. Le plafond de 20 USD ne tient pas « dans tous les cas » par la seule mécanique : il tient par la minuterie si son
`DELETE` aboutit, sinon par la fille, sinon par la mère (§ 2) ; l'ordre doit le dire (CLE-03).

## 1. Exécutable tel quel ? O-1 à O-6

Rejoué dans mon bac à sable (clones neufs faits par `git clone --shared --no-checkout --single-branch --branch main` du dépôt
local, et dépôts jouets ; rien d'écrit dans le dépôt ; bac à sable effacé à la fin par son chemin exact) :

| Geste de l'ordre | Rejeu | Issue |
|---|---|---|
| § 4.1, clone de la fille (registres nommés) | extraction partielle rejouée | six fichiers extraits, tous nommés ; aucun `registres/index-bras-attaque*` ; `registres/go-extraits/` absent de `main` aujourd'hui, sans effet |
| § 4.1, comptes des douze clés, périmètre, compte des chemins interdits, compte des dépenses | rejoués sur `main` `709d16fc` | « PERIMETRE conforme (JD,JA) », `0`, `0` (aucune ligne d'engagement encore : P8 l'attend) |
| § 4.1, P9 et P12 (code, script, arbres, six chemins de la configuration) | rejoués avec S7 = C7 = `709d16fc` et la configuration v4 | « code et script conformes », « ATT valable pour S7 » : arbres `tests/` `79230a58…` et `src/` `744a9e16…` à `709d16fc` |
| § 4.1, P4, P5 et P6 | lignes jouets (`GO-LECTURE-T07`, `SCELLEMENT-T07`, `CODE-T07`) | trois messages « conforme » ; artefact (extrait d'une autre ligne de GO) pris par l'empreinte |
| § 4.4, `HMAX` | calculé pour `ANT0` de 0 à 4,6 et deux prix | `ANT0` = 4,5 à 1,30 USD/h : 39 323 s ≥ 39 240, création permise ; `ANT0` = 4,6 : refus ; coût à `ECH` ≤ 19,9 USD |
| § 4.4, garde de calcul | lecture du crochet | la commande passe parce que **la ligne (A) écrit les deux identifiants de GO en clair** ; `GO_ID=$GO` seul ne suffirait pas (le crochet lit le texte) : la ligne (A) en tête du bloc est donc nécessaire, comme l'ordre le prescrit |
| § 4.4, arguments | comparés au script l. 12 et 27-28 | neuf, même ordre (`S7 C7 RUN6 CFG BR BR7B 'ATT' ECH PER`) |
| § 4.6, vérification de la poussée | dépôt jouet à morceaux : cas sain, puis artefact (compagnon d'un morceau faux, morceau manquant) | `OK` partout au cas sain ; `ÉCART` sur le manifeste à l'artefact ; clés et dates seules pour `SCORES-T07` et `SONDES-T07` |
| Étapes 2, 3 et 6 du script | clone neuf, mêmes motifs, registres et fichiers cités, journaux des jeux, essais sous Python 3.11 | § 3 |
| Étape 9 du script (`CODE-T07`) | § 3 | cas sain et trois artefacts |
| Marqueurs | comptés | dix, une occurrence chacun, avant et après les douze couples |

Non rejoué (réel seulement) : `vastai` (inventaire, recherche, création, journaux, destruction), le passage du script en
base64 par `--args` (même montage que le lanceur de T0.6, mais avec un argument entre apostrophes, `'$ATT'`, ce que T0.6 ne
faisait pas : si Vast le découpait, le script sortirait par « T07 REFUS : neuf arguments attendus », voir CLE-05), P2 (aucune
course 7b), les étapes 4, 5, 7, 8 et 10 à 13 du script, le `DELETE` de la minuterie avec la clé d'une instance, le git de
l'image (2.43 ici).

| Point | État | Bloquant ? |
|---|---|---|
| **O-1** ligne d'essais | **réglé** : essais avant le modèle (script l. 203-214) ; `ATT` mesurée par le développeur dans un clone partiel à branche unique sous 3.13, **retrouvée par moi sous 3.11.17** ; P12 lie `ATT` aux arbres de S7. Reste : construction carte de `torch`, avertissements (S-1). | non |
| **O-2** taille | **réglé** par le script (borne avant toute ouverture, découpage) ; § 5 bis conforme au script l. 216-283. Au périmètre `JD,JA`, la part des sondes neuves est d'environ 0,42·10⁹ octets (mon calcul sur la formule, avec les valeurs de l'ordre de grandeur du § 5 bis : largeur 4 096, trois couches, 200 planchers ; non lues dans la configuration) : la borne de 2·10⁹ tient largement. Reste : borne jamais confrontée à une sortie réelle. | non |
| **O-3** minuterie | **réglé** pour le texte (§ 4.7) et le journal des `DELETE` ; **une phrase du § 6 reste fausse** si le `DELETE` échoue (CLE-03) ; la mère ne peut tenir son rappel que si elle reçoit `ECH` (CLE-02). | non, couples |
| **O-4** dépense antérieure | **réglé** : `ANT0` sous les deux lignes, P8, `HMAX`. | non |
| **O-5** registres | **réglé** : registres nommés des deux côtés ; `interdit()` refuse `registres/index-bras-attaque*`. Reste S-3, tenu par le compte du § 4.1 (rejoué : 0). | non |
| **O-6** | **réglé** : en-tête ; `exit 2` sur l'écart d'encodage et sur une borne de minuterie trop courte ; journaux des jeux recopiés (rejoué : un journal présent). | non |

## 2. Dépense : le plafond de 20 USD

- Arithmétique du § 6 refaite : 3,01 à 4,51 h attendues, 7,90 à 10,90 h au pire ; 5,2 à 7,1 USD attendus, 11,6 à 15,5 USD au
  pire : exact. `ANT0` ≤ 4,5 USD ⇔ `20 − ANT0` ≥ 15,5 : exact. Les deux lignes de GO (l. 294, 296) disent bien « 20 USD,
  non cumulé » ; la ligne (A) et le bloc du § 4.5 comptent sous les deux.
- **Ce qui tient le plafond, cas par cas** : (1) conteneur vivant à `ECH` et `DELETE` accepté : la minuterie, coût ≤ 19,9 USD ;
  (2) fin du script (`FIN` ou `ARRET`) : l'état « stopped » tue la minuterie, le disque court à ≤ 0,08 USD de l'heure, **sans
  borne mécanique** ; (3) `DELETE` refusé cinq fois (jamais répété avec la clé d'une instance) : la carte continue à 1,30 USD
  de l'heure, sans borne mécanique ; (4) sortie par « T07 REFUS » ou identifiant d'instance illisible (script l. 27, 34, 42,
  71) : pas de minuterie du tout. Dans (2) à (4), seule la fille, puis la mère à `ECH`, tiennent le plafond. Marge à `ECH` :
  3,2 USD à `ANT0` = 0 (2,4 h de carte, 40 h de disque) ; 0,1 USD à `ANT0` = 4,5 (cinq minutes de carte).
- **Échec de la session de la fille** : le journal vit dans son dossier ; la mère n'a ni `ID` ni `ECH` si rien ne lui est
  envoyé après la création. → **CLE-02**.
- **Prix non bornés** : la sélection du § 4.3 ne regarde ni `inet_down_cost`, ni `inet_up_cost`, ni `storage_total_cost` ;
  le devis suppose 0,05 USD par Go (1,20 USD) et 0,08 USD de l'heure, et `HMAX` retranche 1,20 et 0,10 en dur. La chaîne de
  T0.6 refuse une offre hors de ces bornes (`session_v2.py` l. 104-109). → **CLE-01**.
- R10 : destruction par `ID` (fille) et par `CONTAINER_ID` (minuterie) ; aucun arrêt par motif.

## 3. C7, S7, `CODE-T07-v2.json`, `ATT`

- **Cohérence** : P6 et P9 de l'ordre, le script (l. 134-137 : tête = S7, C7 ancêtre, `git diff --quiet C7 S7 -- src tests`,
  S7 ancêtre de `main`) et `code_t07_v1.py` (forme ; ligne antérieure à la première ouverture ; commit cité ancêtre de la tête ;
  fichiers du module au commit et importés égaux à la liste ; DF-02 : `git diff` et `git status` de `src/controle_ia/`) disent
  la même chose. `37485ce5` est ancêtre de `main` ; `src/` de `main` lui est égal.
- **Rejeu** (clone neuf à extraction partielle du script, Python 3.11.17, `PYTHONDONTWRITEBYTECODE=1`, C7 jouet `f61f1081`
  ancêtre de la tête, `src` et `tests` égaux) : `code_t07_v1 ecrire` rend 18 fichiers aux mêmes empreintes que
  `CODE-T07-v1.json` ; ligne absente → refus, code 2 ; ligne inscrite → « CODE-T07 conforme », **y compris depuis une branche
  neuve un commit après S7** (comme après l'étape 10) ; artefacts pris : fichier non suivi sous `src/controle_ia/t07/`, paquet
  importé retouché, compagnon du fichier cité faux. Le contrôle P6 de la fille passe sur ce jouet.
- **Constat, sans correction** : le script ne compare pas le commit cité par `CODE-T07` à son argument C7 ; seul P6 de la
  fille le fait. Sans danger (les deux contrôles exigent un arbre `src/` égal), à savoir.
- **`ATT` sous Python 3.11** (décision de la mère, R-2255 : « à remesurer sous 3.11 si la place le permet ») : environnement
  `python3.11 -m venv`, versions figées de `requirements-cpu.txt` et `pypandoc_binary` (`numpy` 2.4.6, `scipy` 1.17.1, `pytest`
  9.1.1, `transformers` 5.18.0, `torch` 2.14.1+cpu depuis l'index processeur de PyTorch) ; clone neuf, motifs des étapes 2 et 3
  du script, tête `709d16fc` (`tests/` `79230a58…`, `src/` `744a9e16…`) ; commande exacte de la l. 206, `TZ=UTC`, configuration
  git globale vide (`GIT_CONFIG_GLOBAL=/dev/null`), dossier personnel vide ; de 15:46:49 à 16:03:50 UTC.
  **Résultat : code 0, `346 passed, 2 skipped, 4 xfailed`** (1 019,6 s), égale à `ATT` ; les deux sauts et les quatre échecs
  attendus sont ceux que nomme le § 11 bis ; aucun avertissement ; `essais.err` vide ; `src` et `tests` non écrits ;
  `essais-liste.txt` `bd49a36795b15228a9cfde88b411b98ae842223e35fbb75e57eebe04dcb26415`, **égale à celle du développeur** (mêmes 17
  fichiers) ; `essais.txt` `9d7e8e6c4d82640a260695b298df8f83a7f19218375448a4ef5ed625154e85c8` (pièces non versées, effacées).
  Analyse de syntaxe sous 3.11 des 181 fichiers `*.py` de `src/` et des essais de T0.7 : aucune erreur.
  **Limite déclarée** : mon clone partage les objets du dépôt local (`--shared`) au lieu d'être un clone partiel de GitHub ;
  le profil des sauts est le même (`061ac380` absent du dépôt local, branche `origin/prep/t06-candidat8-v1` non reprise), mais
  l'atteignabilité depuis `main` seul n'est prouvée que par la mesure du développeur. Les deux mesures se complètent ; aucune
  ne joue la construction carte de `torch`.
- **Le risque est-il dit, la conséquence exacte ?** Oui : § 10.2 et § 13 S-2 disent 3.13 contre 3.11 ; § 5.6 et § 7 disent
  « arrêt de code 2, après les paquets, avant le modèle, rien d'ouvert », ce que fait le script (l. 214 ; `BRANCHE_PRETE` = 0 :
  rien de poussé, aucune ligne d'ouverture écrite, relance propre). Deux précisions : le coût d'un écart est sous-estimé dans
  la table 0 bis (CLE-10) ; `essais.txt` meurt avec l'instance, la fille ne voit que la ligne (S-10 ci-dessous).

## 4. Cloison

- **Bras d'attaque, 7a** : rien dans les motifs d'extraction (script l. 103-118) ni dans le clone de la fille ; `interdit()`
  couvre les sept motifs ; `lecture-sondes-t06.json` exclu des motifs, jamais listé, deux contrôles de présence. Le dossier
  `docs/notes/g0-deux-semaines-v1/` est extrait en entier sur l'instance : ses noms de premier niveau (`git ls-tree`) ne
  portent que le « bras B » de l'audit de fuite de T0.6, pas le bras d'attaque.
- **Registre partagé** : `registres/scellements-v1.md` porte aujourd'hui quatre lignes, dont deux de T0.8 (`SCELLEMENT-T08-BASE-A`,
  `GEL-T08`) ; l'étape 3 recopie leurs fichiers (rejoué, sans effet sur les essais). Une ligne future d'une autre tâche qui
  citerait un chemin interdit arrêterait l'instance (code 2) ; le compte du § 4.1 l'arrête avant la création, sans dépense.
- **Filtre d'inventaire** : `startswith(("t06", "t07"))`, conforme au couple CLO-08 et à R-2249 ; lecture stricte de P10
  (toute `t06…`, celle de 7b comprise, bloque en variante B) cohérente avec l'écrit (b) 2 (« seulement si l'instance de 7b ou
  son disque n'est plus disponible »). **Condition** : le brouillon 22 lu porte encore « instance du programme déjà sur le
  compte » (l. 1899) ; l'ordre cite la ligne corrigée. Il n'est vrai que si le texte scellé porte CLO-08 (CLE-09).
- **T0.7 cité par `SCELLEMENT-T07` seulement** : tenu ; aucune empreinte de T0.7 dans l'ordre (`8b84cba5` : 0 occurrence).

## 5. Les sept constats S-n : aucun ne bloque l'étape A

| id | Mon jugement |
|---|---|
| S-1 | non bloquant, mais **cause la plus probable d'un lancement perdu** : un seul avertissement de la construction carte de `torch` change la ligne ; aucun filtre d'avertissements dans `pyproject.toml`. Ni ma mesure ni celle du développeur ne le couvrent. Si la mère rouvre le script, c'est la première correction à faire. |
| S-2 | **réduit** par ma mesure (§ 3). |
| S-3 | non bloquant : aucun registre ne cite 7a ; les lignes prévues du registre des préalables de P3-bis citent le texte de T0.7 ; compte du § 4.1 rejoué. |
| S-4, S-7 | non bloquants (libellé, cosmétique). |
| S-5 | hors du script ; tranché par la mère (R-2255). |
| S-6 | non bloquant ; au périmètre `JD,JA` la marge est large (§ 1, O-2). |

Constats de plus sur le script, pour une v3, **non bloquants** :

- **S-8** : les trois « T07 REFUS » (l. 27, 34, 42) sortent par `exit 2`, avant la minuterie, sans demander « stopped », sans
  date : invisibles au filtre du § 4.5. Tenu en attendant par CLE-05.
- **S-9** : après cinq `DELETE` en échec, la minuterie pourrait demander l'état « stopped » (voie que l'amorce de T0.6 emploie
  en fin de run), ce qui couperait la carte.
- **S-10** : sur un écart de la ligne d'essais, `essais.txt` n'est ni poussé ni journalisé ; écrire au journal les lignes
  `SKIPPED`, `XFAIL`, `FAILED`, `ERROR` rendrait l'écart lisible sans remesure.
- **S-11** : la garde du repli écrit `OUVERTURE-T07` au début de `repli-seul`, la poussée ne vient qu'après le recalcul
  (l. 357-365) : une instance perdue dans l'intervalle emporte la ligne. Tenu en attendant par CLE-04.

## 6. Constats

| id | gravité | constat | suite |
|---|---|---|---|
| **CLE-01** | **majeur** (dépense) | § 4.3 : l'offre est choisie sans borne sur le prix du téléchargement (`inet_down_cost`, `inet_up_cost`) ni sur celui du stockage (`storage_total_cost`), que le devis (§ 6) et `HMAX` (§ 4.4) supposent à 0,05 USD par Go et 0,08 USD de l'heure. À 0,20 USD par Go, 24 Go coûtent 4,8 USD : la marge sous 20 USD disparaît sans qu'aucun relevé le voie. La chaîne de T0.6 garde ces deux bornes. | couples 1 et 2 |
| **CLE-02** | **majeur** (plafond si la fille tombe) | § 4.4 et § 4.7 : la mère « pose le rappel » et « fait détruire par l'identifiant écrit au journal », mais le journal est dans le dossier de la fille et le compte rendu (§ 8) n'arrive qu'à la fin. | couple 3 |
| **CLE-03** | à corriger | § 6 : « la carte ne peut pas dépasser `20 − ANT0 − 1,30` tant que le conteneur vit » est faux si le `DELETE` échoue. | couple 4 |
| **CLE-04** | **majeur** (tenue du périmètre) | T0.7, « Accord au code », point 19, demande que toute ligne `OUVERTURE-T07` écrite sur l'instance, « y compris avant un arrêt », soit recopiée dans le journal de `main` « avant toute relance sur une instance neuve », et renvoie à cet ordre (« à juger par la contre-lecture de l'ordre »). Le § 9 ne dit la recopie qu'en suite d'une étape menée au bout ; le § 7 permet une création neuve « quand la cause est levée » sans cette condition. Le module ferme le périmètre et juge l'antériorité de `CODE-T07` sur la première ligne du journal (`lecture_v2.py` l. 239-310, 489-503) : sans recopie, la relance fixe un autre instant. Cas voisin non écrit : instance perdue après l'écriture de la ligne et avant sa poussée (S-11). | couple 5 |
| **CLE-05** | mineur | § 4.5 : une sortie « T07 REFUS » n'a ni date ni minuterie ni demande d'arrêt ; le filtre ne la montre pas ; aucune règle pour une instance muette. | couples 6 et 7 |
| **CLE-06** | mineur | P10 demande les deux jetons « présents (par le nom) » sans donner la commande : risque d'un geste improvisé qui afficherait l'environnement. | couple 8 |
| **CLE-07** | mineur | P7 fait « relever » le journal de P3-bis sans commande, alors que le § 2.6 interdit à la fille d'en lire le contenu. | couple 9 |
| **CLE-08** | information | `ATT` retrouvée sous Python 3.11.17 (§ 3). | couple 10 |
| **CLE-09** | concordance, pour le candidat de T0.7 (aucun couple dans l'ordre) | (a) l'ordre cite la ligne d'arrêt corrigée par CLO-08 : le texte scellé doit la porter ; (b) T0.7 écrit « minuterie : destruction à la création + 12 h » ; l'ordre écrit `ECH` = création + `HMAX`, `HMAX` ≤ 12 h, plus court dès que `ANT0` > 3,1 USD à 1,30 USD de l'heure : écrire « au plus 12 h, bornée par la dépense » ; (c) T0.7 porte le devis du brouillon 3 (3,2 à 4,7 h ; 7,8 à 10,8 h ; 5,4 à 7,4 USD ; 11,4 à 15,3 USD ; « ≤ 17,7 USD tout compris ») ; le brouillon 4 dit 3,0 à 4,5 h ; 7,9 à 10,9 h ; 5,2 à 7,1 USD ; 11,6 à 15,5 USD ; ≤ 16,8 USD à `ECH` pour `ANT0` = 0 ; (d) les passages cités entre guillemets à l'en-tête de l'ordre (« instance A100 SXM4 80 Go ≤ 1,30 USD de l'heure […] ») sont des résumés, pas des citations à l'octet. | mère, au candidat |
| **CLE-10** | mineur | Table 0 bis, O-1 : « ≤ 1 h, attendu 0,15 h payées en cas d'écart » ne s'accorde ni au § 6 (0,6 h attendue, 1,85 h au pire avant la fin des essais) ni à S-1. | couple 11 |
| **CLE-11** | mineur | Sources : le registre porte une quatrième ligne (`GEL-T08`) depuis l'écriture. | couple 12 |
| **CLE-12** | information | Une minuterie qui tombe pendant l'étape A détruit une étape ouverte : nœud de dépense (écrit (b) 6), relance seulement sur un mot de Lazar. La durée réelle de l'étape A n'a jamais été mesurée ; la passe à blanc n'estime que l'extraction. Marge entre le pire cas du devis et 12 h : 1,1 h. Rien à corriger dans l'ordre ; à savoir avant le lancement. | — |

## 7. Couples exacts (appliqués en séquence ; chaque « ancien » unique au moment de son application)

Vérifié par programme sur `d5047be2…` : douze couples, chacun sur une seule ligne ; empreinte du texte après les douze :
`f3256fd603e3d2c330245c9c4850b9a84064603bb9daee4fad46f7d8b9915de5` ; les dix marqueurs y restent, une occurrence chacun. Copie
en JSON, hors dépôt, pour la mère :
`/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/cl-ordre-b4/couples-cle-ordre-b4-v1.json`
(`cf2e4c982133e2ad662c7e67bd5eafe80ae783e32ec98e6cda42f524d1643fa5`). L'en-tête de l'ordre (« Non contre-lu. ») reste à mettre à
jour par la mère.

**Couple 1** — CLE-01 ; § 4.3, sélection de l'offre.

- ancien : and float(x.get("gpu_ram",0))>=79000]
- nouveau : and float(x.get("gpu_ram",0))>=79000 and 0<=float(x.get("storage_total_cost",9))<=0.08 and 0<=float(x.get("inet_down_cost",9))<=0.05 and 0<=float(x.get("inet_up_cost",9))<=0.05]

**Couple 2** — CLE-01 ; § 4.3, texte.

- ancien : Au plus **trois** recherches, espacées
- nouveau : Une offre n'est retenue que si son stockage est ≤ 0,08 USD de l'heure et son téléchargement, dans les deux sens, ≤ 0,05 USD par Go (bornes du devis, § 6 ; garde d'offre de la chaîne de T0.6, `src/controle_ia/t06/session_v2.py` l. 104-109) ; un champ absent écarte l'offre. Au plus **trois** recherches, espacées

**Couple 3** — CLE-02 ; § 4.4, rappel daté.

- ancien : la fille l'écrit au journal et le pose dans sa session
- nouveau : la fille l'écrit au journal, le pose dans sa session et **envoie aussitôt à la mère, avant la première surveillance, l'identifiant, `TC`, `HMAX` et `ECH` en date UTC** (sans ce message, la mère ne connaît ni l'instance ni l'échéance si la session de la fille tombe ; à défaut d'identifiant, l'instance se retrouve par son étiquette `t07-b-v1`, § 4.2)

**Couple 4** — CLE-03 ; § 6, plafond.

- ancien : la carte ne peut pas dépasser `20 − ANT0 − 1,30` tant que le conteneur vit.
- nouveau : si le `DELETE` de la minuterie aboutit (jamais répété avec la clé d'une instance réelle, O-3), la carte ne dépasse pas `20 − ANT0 − 1,30` tant que le conteneur vit ; s'il échoue cinq fois, ou après l'état « stopped » (disque ≤ 0,08 USD de l'heure, sans minuterie), le plafond ne tient que par la destruction faite par la fille (§ 4.7) ou, si sa session est tombée, par la mère au rappel de `ECH` (§ 4.4) : à `ANT0` = 0 et 1,30 USD de l'heure, la marge à `ECH` est de 3,2 USD (2,4 h de carte ou 40 h de disque) ; à `ANT0` = 4,5 USD, de 0,1 USD.

**Couple 5** — CLE-04 ; § 7, relance.

- ancien : n'a lieu que sur un écrit de la mère (même GO, devis inchangé), quand la cause est levée.
- nouveau : n'a lieu que sur un écrit de la mère (même GO, devis inchangé), quand la cause est levée, **et après que la mère a recopié à l'octet, dans le journal des ouvertures de `main`, toute ligne `OUVERTURE-T07` ou `REFUS-T07` poussée par l'instance arrêtée** (texte de T0.7, « Accord au code », point 19 : sans elle, la relance fixerait un autre instant de fermeture) ; `PER` de la relance se recalcule au § 4.1, et le module écarte de lui-même une ligne de jeu postérieure à cette première ouverture. **Instance perdue (hôte, minuterie) entre la ligne « CODE-T07 conforme » et la poussée « garde, repli »** : la ligne d'ouverture a pu être écrite sans être poussée ; nœud, aucune relance sans un écrit de la mère qui fixe l'instant de fermeture.

**Couple 6** — CLE-05 ; § 4.5, filtre des journaux.

- ancien : grep -E '^[0-9TZ:-]+ T07 ' | tail -n 20
- nouveau : grep -E '^[0-9TZ:-]+ T07 |^T07 REFUS' | tail -n 20

**Couple 7** — CLE-05 ; § 4.5, attendus.

- ancien : Une ligne `ARRET` : § 7. Une ligne `MINUTERIE` : l'échéance est atteinte (§ 4.7).
- nouveau : Une ligne `ARRET` : § 7. Une ligne `MINUTERIE` : l'échéance est atteinte (§ 4.7). Une ligne `T07 REFUS` (sans date : le script est sorti avant sa minuterie et sans demander l'état « stopped », l. 27, 34 et 42), ou aucune ligne `T07` trente minutes après l'état « running » : destruction par l'identifiant (§ 4.7), compte rendu, nœud.

**Couple 8** — CLE-06 ; § 4.2, bloc.

- ancien : vastai --version; date -u +%FT%TZ
- nouveau : vastai --version; date -u +%FT%TZ; for v in HF_TOKEN CONTROLE_IA_GITHUB_TOKEN; do [ -n "${!v:-}" ] && echo "$v présent" || echo "$v ABSENT : aucune création"; done

**Couple 9** — CLE-07 ; § 4.1, attendus.

- ancien : `VERDICT-P3BIS` relevés ;
- nouveau : `VERDICT-P3BIS` relevés (comptes seulement ; le journal de P3-bis `registres/ouvertures-p3bis-v1.md` n'est ni affiché ni lu par la fille, § 2.6 : seule sa présence se relève, par `[ -f "$M/registres/ouvertures-p3bis-v1.md" ] && echo présent || echo absent`) ;

**Couple 10** — CLE-08 ; § 0 bis, O-1.

- ancien : interpréteur de la mesure 3.13 contre 3.11 sur l'instance (§ 13, S-2)
- nouveau : interpréteur : ligne **retrouvée sous Python 3.11.17** par la contre-lecture R2 de cet ordre (`prereg/contre-lectures/ordre-execution-etape-a-t07-v1-brouillon4-cl1.md`, § 3 : même ligne, mêmes deux sauts, mêmes quatre échecs attendus, aucun avertissement ; `torch` 2.14.1 en construction processeur) ; restent la construction carte de `torch` et le git de l'image (§ 13, S-1, S-2)

**Couple 11** — CLE-10 ; § 0 bis, O-1.

- ancien : essais joués **après** les paquets (≤ 1 h, attendu 0,15 h payées en cas d'écart)
- nouveau : essais joués **après** les paquets : un écart coûte le démarrage, le clone, les paquets et les essais, soit ≈ 0,6 h attendue et 1,85 h au pire (§ 6), ≤ 2,4 USD de carte, plus le téléchargement des paquets

**Couple 12** — CLE-11 ; Sources.

- ancien : (trois lignes : `SCELLEMENT-JEUX-T07-JD`, `SCELLEMENT-JEUX-T07-JA`, `SCELLEMENT-T08-BASE-A`)
- nouveau : (trois lignes : `SCELLEMENT-JEUX-T07-JD`, `SCELLEMENT-JEUX-T07-JA`, `SCELLEMENT-T08-BASE-A` ; une quatrième, `GEL-T08`, à `709d16fc` : son fichier est recopié sans effet, rejoué par la contre-lecture R2)

## 8. Interdits et écarts déclarés

Tenus. Aucun `lecture-sondes-t06.json` ouvert ; rien de 7a, de la lecture B, du bras d'attaque ni de l'étiqueteur ; aucune valeur
de clé, ni `env` ni équivalent ; aucun appel de modèle, aucun `vastai`, aucune instance, aucune dépense ; aucune valeur de sonde
sous mes yeux. Git dans le dépôt : lecture seule (`rev-parse`, `merge-base --is-ancestor`, `ls-tree` et `ls-files` sur des dossiers
nommés non interdits, `git grep` sur des fichiers nommés, `branch --list` par motif de nom) ; aucun `checkout`, `fetch`, `commit`
ni écriture d'index. Dans le bac à sable seulement : deux clones `--shared` du dépôt local (extraction partielle, sans chemin
interdit), deux dépôts jouets, des commits jouets. Écarts déclarés : (1) installation de paquets depuis PyPI et l'index
processeur de PyTorch pour l'environnement 3.11 (1,6 Go, effacé) ; (2) les 17 fichiers `tests/test_t07_*.py` joués une fois
(essai ciblé, pas la suite complète) ; (3) un `find` sur mon propre clone jouet, pour lister les six fichiers extraits. Aucun
refus de permission ni de classifieur. Seul fichier écrit dans le dépôt : ce rapport et son compagnon.
