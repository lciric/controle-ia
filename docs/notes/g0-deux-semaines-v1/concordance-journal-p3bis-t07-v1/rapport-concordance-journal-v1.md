# Concordance du journal des ouvertures de P3-bis (écrivain) avec le lecteur de T0.7 — rapport v1

Écrit le 2026-11-10 entre 08:04 et 08:15 UTC (heures relevées par `date -u`), par un agent neuf (Opus 5.5) de la session mère
`session_01QPDgKgACWyCkCN8HjqwNXy`. Je n'ai écrit ni le code de P3-bis, ni celui de T0.7, ni leurs textes, ni leurs
contre-lectures. J'ai lu des fichiers de T0.7 : je suis **exclu ensuite de tout rôle de lecteur de P3-bis**.

- Consigne : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/consigne-concordance-journal-p3bis-t07-v1.md`
  (`042ba58ab141d9971f8632b4a75d12eac583d57e4128afd33e68b4487adc9360`, vérifiée avant lecture).
- Interdits communs v2, règle 9 comprise : `…/interdits-communs-v2.md`
  (`1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f`, vérifiée avant lecture). Tenus : aucun fichier ni
  aucune branche interdits ouverts ; aucune recherche récursive (un `git grep` sur deux fichiers nommés à un commit, des
  `grep` sur des fichiers nommés) ; aucune écriture git dans le dépôt de travail ; aucun appel externe ; aucune dépense.
- Script d'essai : `docs/notes/g0-deux-semaines-v1/concordance-journal-p3bis-t07-v1/essai_concordance_journal_v1.py`
  (`b30c9db7317e62fcfbf4f48a89927f33d69e86592f6243efbcfa6337e0808cef`, scellé).

## Verdict

**Concordance tenue pour toute ligne que l'écrivain écrit dans l'ordre du temps. Une discordance réelle : des dates
décroissantes.** 47 lignes écrites par l'écrivain dans 38 scénarios couvrent les trois modes d'ouverture, les dix-sept codes
de refus de la liste fermée, `deja-ouverte` et les cas E-3, E-8 et E-9. Résultat : 44 lignes lues telles quelles, 0 mal
interprétée, 3 refusées. Une seule de ces trois lignes est un refus prévu par les deux textes (journal hors format écrit à la
main, nœud). Les deux autres forment la discordance **D-1** : l'écrivain écrit une date antérieure à celle de la ligne
précédente sans rien relever, et T0.7 refuse alors le journal entier (nœud, sans remède dans un registre en ajout seul).

Les deux textes donnent le même format (en-tête, six cellules, clés, modes, appui, paquets, codes, ordre des ouvertures), à
une exception près : la règle « dates non décroissantes », que seul T0.7 porte (brouillon 20, « Accord au code », point 11).
S'y ajoutent trois écarts de règle sans effet sur les lignes bien écrites : **D-2** (croisement E-8 non tranché),
**D-3** (tolérance de forme différente des deux côtés) et **D-4** (chemin du texte cité par la garde adaptée). Je n'ai rien
corrigé.

## Pièces et copie

| rôle | fichier | commit | sha256 |
|---|---|---|---|
| écrivain | `src/controle_ia/premier_test_ia/ouverture_p3bis_v2.py` | `02217f1c` (`prep/p3bis-code-v2`) | `330915f67402e097c2581fee0de2ed6950954f2c071356df19b27980bb5f5bb3` (égale à son compagnon au commit) |
| dépendance de l'écrivain | `src/controle_ia/scellement.py`, `src/controle_ia/premier_test_ia/__init__.py` | `02217f1c` | `93beeb1c…`, `c72da160…` |
| lecteur | `src/controle_ia/t07/journal_p3bis_v1.py` | `8dc1cb09` (`prep/t07-module-v2`) | `389f68080545956c108631233e5ae89d88d7061bf493bb65d32144d47aa191a4` (aucun compagnon au commit) |
| importé par le lecteur | `src/controle_ia/t07/registre_v1.py`, `src/controle_ia/t07/__init__.py` | `8dc1cb09` | `914b8f374ce8f8bc6550d03c34c5f6c2a97ac93b8ce44da24fd88229185ffca0`, `553bd9d2…` |
| usager du lecteur (appui comparé aux lignes citées) | `src/controle_ia/t07/garde_adaptee_v1.py` | `8dc1cb09` | `7ff571d7b1f06db94043545bfe178a066613ddd734aacca1cf3ef52ba0b511de` |
| communs | `src/controle_ia/__init__.py`, `src/controle_ia/gardes.py` | les deux commits, mêmes octets (vérifié) | `e3b0c442…`, `a83c48ce…` |
| texte de l'écrivain | `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon10.md` | `main` | `9038a015c5756a289bebd2f08b1c33b1f2a26eb829bb2c4bc2afec04648fd1f9` |
| choix du code | `brouillons/P3-bis-temoin-positif-v1/compte-rendu-developpeur-code-p3bis-v2.md` | `main` | `f6c93bc51111ed10b93602bb6d7a85bab8b855bc548564fe13957793c6b75e33` |
| texte du lecteur | `brouillons/T0.7-sondes-v0-v1-brouillon20.md` | `main` | `9ef671ac08ba79a43fa4fecfb7740bc6b5769587741ae378dc2935a02caf69da` |

Le script copie ces fichiers par `git show <commit>:<chemin>` dans `/home/user/concordance-journal-tmp/src/` et vérifie chaque
empreinte. Il refuse un import venu d'ailleurs que ce dossier. Il ouvre un dépôt git jetable `…/depot`
(`GIT_CEILING_DIRECTORIES` posé sur le dossier temporaire) et y fabrique deux jeux de paquets jouets (`run-a`, `run-b`) avec
les fonctions mêmes de l'écrivain (`fermer_run`, `paquet_lectures`, `sceller`). Chaque scénario a son banc : registre des
préalables, registre des scellements, décisions et fichiers cités, tous scellés. L'écrivain y écrit par
`ouvrir(…, instant=…)`. L'essai passe le paramètre d'instant (réservé aux essais, CP-08) et des dates postérieures au
rendez-vous du 2026-11-20T12:00:00Z (`DATE_RENDEZ_VOUS`). Le lecteur lit ensuite le journal par `lire_journal_p3bis`.

Chaque ligne écrite reçoit l'un de trois verdicts :
- **lue telle quelle** : mêmes valeurs de clé, date, instant, mode, appui, paquets et motif que celles que l'écrivain relit
  lui-même dans sa ligne (`lire_ligne_journal`), et même sens : une ouverture du même mode, ou jamais une ouverture ;
- **refusée** : le lecteur lève `JournalFautif` ;
- **mal interprétée** : un champ ou le sens diffère.

Pour les scénarios à ouvertures, l'essai joue aussi la vue de T0.7 à l'étape B. Il compare l'appui de chaque ligne `reduite`
et `pleine` aux lignes citées (`controler_reduite`, `controler_pleine`), calcule les codes de `garde_etape_b` sans
`VERDICT-P3BIS` et cherche la réserve R14.

Passage retenu : 2026-11-10, de 08:03:15 à 08:03:18 UTC, avec `/home/user/controle-ia-travail/.venv/bin/python -I`
(Python 3.13.18, numpy 2.4.6). Code de sortie 0 : chaque tentative a donné à l'écrivain l'issue visée avec le nombre de
lignes visé. Un premier passage, de 08:00:22 à 08:00:23 UTC, a joué une version antérieure du script, sans les constantes ni
les sondes de lignes écrites à la main. Ses 291 lignes de scénarios sont identiques à celles du second passage, hors
empreintes des paquets, tirées par un sel neuf. Le dossier temporaire a été effacé par son chemin exact après chaque passage.

## 1. Chaque type de ligne, écrit puis lu

« = » veut dire « lue telle quelle » ; l'abréviation « l. » renvoie à la ligne du fichier journal.

| scénario | tentatives de l'écrivain (issue, code de la ligne de commande) | lignes écrites | lecteur de T0.7 | vue de T0.7 à l'étape B (sans `VERDICT-P3BIS`) |
|---|---|---|---|---|
| S01 chemin normal | `pleine` → ouverture (0) ; `pleine` → `deja-ouverte` (2) ; `reduite` → `deja-ouverte` (2) ; mode `totale` → erreur d'appel (1) ; sortie déjà présente → erreur d'appel (1) | 3 (l. 3 à 5) ; les deux erreurs d'appel n'écrivent rien | 3 = : une ouverture `pleine`, deux refus jamais pris pour des ouvertures | appui de la `pleine` conforme ; aucun code ; pas de R14 |
| S02 branche 1 | `reduite` sous « ouvrir » → ouverture ; `pleine-anticipee` sous « ouvrir » → `ni-scores-ni-ouvrir` ; `pleine` sans `SCORES-T07` → `ligne-absente` (E-3) ; `pleine` après `SCORES-T07` et `SONDES-T07` → ouverture (complément) | 4 | 4 = | appuis `reduite` et `pleine` conformes ; aucun code ; R14 (réduite l. 3) |
| S03 branche 2 | `pleine-anticipee` sous « ouvrir pleinement » → ouverture | 1 | = (ouverture `pleine-anticipee`) | code `anticipee` (nœud) |
| S04 E-9 | « ouvrir », `reduite` → ouverture ; puis « ouvrir pleinement », `pleine-anticipee` → ouverture (complément, appui `RENDEZ-VOUS-P3BIS-2=…`) | 2 | 2 = (ordre `reduite` puis `pleine-anticipee` permis des deux côtés) | appui de la réduite conforme ; codes `anticipee` et `attente-pleine` (le premier, nœud, décide : `premier_code`) |
| S05 E-8 | `reduite` sous « ouvrir » **après** `SCORES-T07` et `SONDES-T07` → ouverture ; `pleine` → ouverture | 2 | 2 = | appuis conformes ; aucun code ; pas de R14 (réduite après la fin de l'étape A) |
| S06a E-8 | `pleine-anticipee` sous « ouvrir pleinement », `SCORES-T07` et `SONDES-T07` déjà inscrites → ouverture | 1 | = | code `anticipee` (nœud : T0.7 ne lit plus 7b) |
| S06b E-8 | même banc que S06a, `pleine` demandée → ouverture (« chemin normal (rendez-vous sans objet) ») | 1 | = | appui conforme ; aucun code (T0.7 lit 7b) |
| S07 E-9, ajout | `reduite` (`run-a`) → ouverture ; `pleine` sur d'autres paquets (`run-b`) → `paquet-faux`, cellule `paquets` à deux empreintes ; `pleine` (`run-a`) → ouverture | 3 | 3 = (le refus à deux empreintes n'est jamais une ouverture ; T0.7 ne lit pas `paquets`) | appuis conformes ; aucun code ; R14 |
| R01 à R17a (22 bancs) | un refus chacun : `registre-absent`, `ligne-absente`, `ligne-double`, `ligne-mal-formee` (date d'écrit mal formée ; décision sans « Date : » ; décision datée avant le rendez-vous), `sceau-faux` (empreinte autre ; fichier cité absent), `compagnon-absent`, `date-posterieure`, `cle-inconnue`, `rendez-vous-non-consecutif`, `rendez-vous-non-croissant`, `ligne-apres-decision-finale`, `ni-scores-ni-ouvrir` (`pleine` sans rien ; `reduite` sous « ouvrir pleinement »), `decision-maintenir`, `garde-adaptee-absente` (aucune ligne ; texte autre que `SCELLEMENT-T07`), `garde-adaptee-posterieure` (garde après la ligne « ouvrir » ; `SCELLEMENT-T07` à la date de cette ligne), `paquet-faux` (paquets absents, cellule `-`) | 22, une chacune, appui présenté écrit ou `-` | 22 = (jamais une ouverture) | — |
| R04b | journal hors format (ligne à cinq cellules écrite à la main) → `ligne-mal-formee`, ligne neuve écrite après la fautive | 1 (l. 4) | **refusée** : le journal entier (« ligne 3 : 5 cellules, six attendues : nœud ») | — ; **attendu** par les deux textes (P3-bis b10, liste d'arrêt : « T0.7 le lit comme un écart (nœud) ») |
| N04 (E-3 (c)) | extraction en échec simulée **après** la ligne `OUVERTURE-P3BIS` → arrêt (1), la ligne reste | 1 | = (ouverture `pleine` : sens prudent tenu) | appui conforme |
| N05 | journal présent et vide (0 octet) avant la tentative ; `pleine` → ouverture (en-tête écrit) | 1 | = après l'écriture ; **avant**, le lecteur refuse le fichier vide (D-3) | appui conforme |
| D01 | horloge en arrière : `reduite` → `ni-scores-ni-ouvrir` à 12:00:00, puis `pleine` → ouverture à 11:00:00 le même jour | 2 | **les deux refusées** : « ligne 4 : date … antérieure à la ligne précédente … : nœud » ; l'écrivain se relit sans objection | — (journal illisible pour T0.7) → **D-1** |
| D02 | deux tentatives à la même seconde | 2 | 2 = (dates égales permises par le lecteur) | appui conforme |
| D04 | `reduite` : `SCELLEMENT-T07` et garde adaptée citant un autre texte que `prereg/T0.7-sondes-v0-v1.md` → ouverture | 1 | = | code **`appui-faux`** (« la ligne GARDE-ADAPTEE-T07-P3BIS cite 'prereg/T0.7-autre-v1.md' … ») → **D-4** |

Tous les codes de la liste fermée sont exercés, et chacun est le premier défaut relevé. Toutes les lignes de refus portent un
motif `code : texte` d'un code de la liste ; aucun code neuf. L'appui écrit pour chaque mode a la forme du texte :
- `pleine` : `SCORES-T07=… SONDES-T07=…` ;
- `reduite` : `RENDEZ-VOUS-P3BIS-N=… GARDE-ADAPTEE-T07-P3BIS=…` ;
- `pleine-anticipee` : `RENDEZ-VOUS-P3BIS-N=…`, N étant la dernière ligne de rendez-vous, avec l'empreinte qu'écrit la
  ligne citée.

`garde_adaptee_v1` le juge conforme dans tous les cas, sauf D04. Une ouverture `pleine-anticipee` n'est jamais prise pour une
`pleine` : `_o(journal, "pleine")` l'exclut, et le code `anticipee` sort à toute date.

**Lignes sans journal (E-3 (b)).** Trois cas n'écrivent aucune ligne, comme le texte le dit :
- **N01**, dossier `registres/` absent : `JournalImpossible` (code 2). Le lecteur trouve le journal absent, soit « aucune
  ouverture ».
- **N02**, chemin du journal occupé par un dossier : `JournalImpossible` (code 2). Le lecteur lève `JournalFautif` (« pas un
  fichier ») : rien n'est ouvert d'un côté, nœud de l'autre ; cohérent.
- **Erreurs d'appel de S01** (mode inconnu, sortie déjà présente) : arrêt (code 1), journal inchangé.

E-8 et E-9 ne produisent aucun autre cas sans ligne : un complément sur d'autres paquets écrit sa ligne `paquet-faux` (S07).

## 2. Les deux textes comparés (format écrit au brouillon 10 de P3-bis, format lu au brouillon 20 de T0.7)

- **Origine.** T0.7 b20 recopie le format « de P3-bis brouillon 8 (`477f1f5d…`) » (section « Module », entrées). J'ai
  vérifié que le bloc « journal des ouvertures » du brouillon 8
  (`brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon8.md`, `477f1f5d3dde8fd2…`) et celui du
  brouillon 10 sont **égaux mot pour mot**, espaces normalisés (2 543 caractères chacun, du titre du bloc à « ordre
  interdit) ; »).
- **En-tête** : les deux mêmes lignes dans les deux textes et dans les deux modules (constante `ENTETE_JOURNAL` égale).
- **Cellules** : six, dans le même ordre, sans `|` ni saut de ligne dans une cellule.
- **Clés** : `OUVERTURE-P3BIS` et `REFUS-OUVERTURE-P3BIS` ; seules les premières sont des ouvertures. Mêmes clés aux deux
  modules.
- **Dates** : `AAAA-MM-JJTHH:MM:SSZ`, UTC ; même motif et même format aux deux modules. **Écart** : T0.7 b20, « Accord au
  code », point 11 (l. 2511-2512), porte « dates du journal non décroissantes » (CT-11, `journal_p3bis_v1.py` l. 95). P3-bis
  b10, plan, point 8, n'en dit rien, et l'écrivain ne le vérifie ni à l'écriture ni à la relecture (`exiger_format_journal`,
  l. 722-750) → D-1.
- **Mode** : trois valeurs identiques ; pour un refus, le mode demandé (les deux textes).
- **Appui** : même formule, mot pour mot (b20 l. 2119-2122 ; b10 l. 866-870). Les motifs de clé de rendez-vous dans l'appui
  sont égaux (`RENDEZ-VOUS-P3BIS-[1-9][0-9]*`).
- **Paquets** : `<sha256 du paquet des lectures> <sha256 du paquet du run>`, ou `-` pour un refus sans lecture des paquets
  (même sens dans les deux textes). T0.7 ne lit pas cette cellule.
- **Motif** : `-` pour une ouverture ; pour un refus, « code de la liste fermée … suivi de ` : ` et d'un texte libre ».
  b20 renvoie à la liste de b8, égale aux dix-sept codes de b10, dans le même ordre ; T0.7 ne lit pas cette cellule.
- **Ordre permis des ouvertures** : identique. Même table au lecteur (`SUIVANTS_PERMIS`) et à l'écrivain (l. 740-749,
  « ordre interdit »).
- **Statut du fichier** : registre vivant en ajout seul, sans compagnon. Un journal absent vaut « aucune ouverture » au
  lecteur (b20 « Accord au code », point 6), et l'écrivain le crée à sa première tentative. Le **fichier vide** n'est réglé par
  aucun texte → D-3.
- **Forme vérifiée par T0.7** : b20 dit « en-tête, six cellules, clé, date, mode, ordre ». P3-bis b10, liste d'arrêt
  (l. 1132-1134), dit d'un journal hors format : « T0.7 le lit comme un écart (nœud) ». Les exemples qu'elle donne (cellule
  en trop ou en moins, clé ou mode inconnus) sont bien contrôlés par T0.7. D'autres formes que l'écrivain tient pour hors
  format passent chez T0.7 → D-3.
- **Hors du journal, vu en passant** (constantes comparées par l'essai) : la clé de rendez-vous au registre des préalables est
  lue `RENDEZ-VOUS-P3BIS-([0-9]+)` par l'écrivain et `RENDEZ-VOUS-P3BIS-([1-9][0-9]*)` par le lecteur. D'après le code, non
  essayé : une ligne `RENDEZ-VOUS-P3BIS-01` serait refusée des deux côtés, mais sous deux motifs différents
  (`rendez-vous-non-consecutif` chez l'écrivain, « clé inconnue » chez le lecteur). Sans effet sur le journal.

## 3. Discordances et corrections proposées (rien n'est corrigé ici)

**D-1 — dates décroissantes (réelle ; rare ; conséquence irrémédiable).**
- **Constat.** L'écrivain date chaque ligne par l'horloge (`int(time.time())`, l. 1197) et n'exige pas que cette date suive
  celle de la dernière ligne. Il se relit d'ailleurs sans objection (D01 : « 2 ligne(s), aucun refus »). Le lecteur refuse
  le journal entier dès qu'une date recule.
- **Quand cela arrive.** Il suffit d'une horloge en arrière, ou de deux tentatives faites depuis deux machines aux horloges
  décalées, la seconde datée avant la première.
- **Conséquence.** T0.7 rend un nœud sur 7b. Comme le journal n'est jamais corrigé, ce nœud ne se lève pas.
- **Correction proposée, côté écrivain** :
  (i) dans `exiger_format_journal`, une date antérieure à celle de la ligne précédente rend le journal hors format
  (`ligne-mal-formee`), comme chez le lecteur ;
  (ii) dans `ouvrir`, avant toute écriture, une horloge antérieure à la date de la dernière ligne donne un **refus sans
  ligne**, code 2, rien d'ouvert, comme le journal impossible à écrire (CP-06). Une ligne de refus datée de cette horloge
  briserait elle-même la règle.
- **Correction proposée, au texte de P3-bis** (plan, point 8, format) : ajouter « dates non décroissantes » pour rejoindre
  T0.7 b20.
- **Côté lecteur** : rien ; la règle est prudente.

**D-2 — croisement E-8 non tranché : sous « ouvrir pleinement », deux lignes possibles aux effets opposés pour T0.7.**
- **Constat.** Une décision « ouvrir pleinement » est inscrite, et `SCORES-T07` et `SONDES-T07`, conformes, le sont aussi.
  L'écrivain ouvre alors au choix de l'opérateur :
  - `pleine-anticipee` (S06a) : T0.7 rend un nœud et ne lit plus 7b ;
  - `pleine` (S06b, « chemin normal (rendez-vous sans objet) ») : T0.7 lit 7b normalement et ne voit pas la décision de
    Lazar. `garde_etape_b` ne lit les décisions que pour l'appui des réduites.
- **Ce que disent les textes.** P3-bis b10 permet les deux : plan, point 8, choix (d), et « le rendez-vous tombe si
  `SCORES-T07` et `SONDES-T07` sont inscrites avant sa date ». Il ne dit rien du cas où elles le sont après la décision.
  T0.7 b20 tient « ouvrir pleinement » pour « le mot de Lazar qui ferme T0.7 sur 7b ». Le sort de 7b dépend donc du mode
  tapé, non d'une règle écrite.
- **Options** (à trancher par la mère, puis Lazar s'il le faut, car la liste fermée des codes pourrait changer) :
  - **(a) au texte de P3-bis et côté écrivain** : dès que `SCORES-T07` et `SONDES-T07` sont conformes et antérieures,
    `pleine-anticipee` est refusée et l'ouverture se fait en `pleine`. T0.7 garde 7b, que l'ordre protège déjà (scores avant
    le verdict). Aucun code de la liste ne nomme ce refus : il faut un code neuf ou une règle écrite.
  - **(b) au texte de P3-bis et côté écrivain** : sous une dernière décision « ouvrir pleinement », `pleine` est refusée. Le
    journal porte toujours le mot de Lazar, mais 7b est perdue pour T0.7 sans nécessité.
  - **(c) côté lecteur et au texte de T0.7** : l'étape B tient une dernière décision « ouvrir pleinement » pour un nœud, quel
    que soit le mode écrit.
- **Recommandation** : (a), confiance moyenne. Elle garde 7b là où l'ordre suffit à la cécité et rend l'issue indépendante
  de l'opérateur.

**D-3 — tolérance de forme différente des deux côtés (mineure ; l'écrivain n'écrit jamais ces formes).** Sondes faites sur un
journal copié puis retouché (sortie de l'essai) :

| état du fichier | écrivain (`lire_journal`) | lecteur de T0.7 |
|---|---|---|
| fichier vide (0 octet) | 0 ligne, accepté (traité comme absent) | `JournalFautif` (nœud) |
| ligne vide au milieu ; ligne vide en fin ; sans saut de ligne final ; espace en tête d'une ligne | refus `ligne-mal-formee` | accepté (interprétation déclarée au module : ligne vide ignorée ; lignes nettoyées de leurs espaces) |
| `OUVERTURE` à paquets `-`, à appui `-`, à motif autre que `-` ; `REFUS` à motif hors de la liste fermée, sans code, à appui hors forme | refus `ligne-mal-formee` | accepté : T0.7 ne contrôle pas `appui`, `paquets` ni `motif` ; l'appui d'une `reduite` ou d'une `pleine` est jugé ensuite par `garde_adaptee_v1` (`appui-faux`) |
| fins de ligne CRLF | accepté | accepté (les deux lisent par `read_text`, qui ramène CRLF à LF) |
| séparation de table alignée, date impossible, mode inconnu, clé inconnue, ordre interdit | refus | `JournalFautif` |

Ces états ne naissent que d'une main ou d'une écriture interrompue. Quand le journal est vide, l'écrivain accepte ce que T0.7
refuse ; dans les autres cas, T0.7 lit sans nœud un journal que P3-bis déclare hors format, à rebours de la liste d'arrêt du
brouillon 10.

Il y a aussi une particularité propre à l'écrivain, sans effet pour T0.7. Un journal sans saut de ligne final est refusé
(`ligne-mal-formee`), puis `inscrire` ajoute le saut avant la ligne neuve (l. 783). La faute de format disparaît donc à la
tentative suivante.

Corrections proposées :
- **au texte**, un seul prédicat écrit dans les deux textes (b10, plan, point 8 ; b20, « Module ») : forme exacte de chaque
  ligne, aucune ligne vide, saut de ligne final, cellules `appui`, `paquets` et `motif` à leur forme, et sort du fichier vide ;
- **côté lecteur** : appliquer ce prédicat en entier, sans repli tolérant ;
- **côté écrivain** : tenir un fichier vide pour hors format (`ligne-mal-formee`), sens prudent, puisqu'un fichier vidé
  remettrait aussi à zéro la garde `deja-ouverte`.

**D-4 — texte cité par la garde adaptée (mineure, risque faible).**
- **Écrivain** : il exige que la ligne `GARDE-ADAPTEE-T07-P3BIS` cite le même couple (chemin, empreinte) que
  `SCELLEMENT-T07` (l. 1012), quel que soit le chemin.
- **Lecteur** : il exige en plus le chemin `prereg/T0.7-sondes-v0-v1.md` (`garde_adaptee_v1.py` l. 132 ; b20, G2 (iii)).
- **Conséquence** : si `SCELLEMENT-T07` citait un autre chemin, l'écrivain ouvrirait en `reduite` et T0.7 rendrait
  `appui-faux` (nœud, D04). La ligne `SCELLEMENT-T07` étant celle de T0.7, ce cas suppose une erreur d'inscription.
- **Correction proposée** : côté écrivain et au texte de P3-bis (b10, « qui cite le texte scellé de T0.7 »), nommer le chemin
  `prereg/T0.7-sondes-v0-v1.md`.

## Observations sans discordance

- **E-3** : chaque cas non nommé est rangé sous un code de la liste fermée, et T0.7 ne lit pas ces codes.
- **E-3 (c)**, extraction en échec après la ligne : la ligne d'ouverture reste, et T0.7 la lit comme une ouverture (sens
  prudent).
- **E-8, réduite après la fin de l'étape A** (S05) : la ligne est lue telle quelle, l'étape B passe et R14 est absente. Le
  lancement compte comme un lancement à ouverture réduite pour G3 et G4 (prudent).
- **E-9** : l'ordre `reduite` puis `pleine-anticipee` est permis des deux côtés. Un complément sur d'autres paquets laisse un
  refus `paquet-faux`, jamais pris pour une ouverture.
- **Cellule `paquets` d'un refus** (lu au code, non essayé) : l'écrivain écrit `-` quand un seul des deux paquets a été relu
  (l. 1159), alors que le texte dit « `-` si les paquets n'ont pas été lus ». Sans effet pour T0.7, qui ne lit pas cette
  cellule.

## Limites

- Les fonctions sont jouées en Python, sans passer par la ligne de commande. Les codes de sortie indiqués (0, 1, 2) sont lus
  dans `_main`.
- L'instant est passé en paramètre. La voie de l'horloge réelle n'est pas jouée, mais D01 imite son recul.
- Côté T0.7, seules les règles pures sont jouées (`lire_journal_p3bis`, `controler_reduite`, `controler_pleine`,
  `garde_etape_b`, `reserve_r14`), au commit `8dc1cb09`. `lecture_v2.ouvrir` et l'étape A avec `VERDICT-P3BIS` ne le sont
  pas.
- Le code est pris aux commits nommés ; un commit postérieur de l'un ou l'autre module demande de rejouer le script.

## Refus rencontrés

Aucun : ni contrôle de permissions ni classifieur n'a refusé d'action.
