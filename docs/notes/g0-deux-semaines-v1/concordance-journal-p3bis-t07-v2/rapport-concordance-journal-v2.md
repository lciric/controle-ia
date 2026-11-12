# Concordance du journal des ouvertures de P3-bis avec le lecteur de T0.7, rejouée sur les commits finaux (préalable P-9) — rapport v2

Écrit le 2026-11-11 à partir de 13:46 UTC (heure relevée par `date -u`) par un **agent neuf** (Claude Opus 5.5,
`claude-opus-5-5`), sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`. Je n'ai écrit ni P3-bis, ni T0.7, ni
leur code, ni leurs contre-lectures, ni le rapport v1. **J'ai lu des fichiers de T0.7 : je suis exclu ensuite de tout rôle de
lecteur de P3-bis.**

- Consigne : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-concordance-journal-p3bis-t07-p9-v1.md`
  (`38a3b3396a28e97e19443ce47958cb19b7bec6e5749f0e7aace736c82f2bc231`, vérifiée par `sha256sum` avant lecture) ; interdits
  communs v2 recopiés dedans, tenus (détail en fin de rapport).
- Lu : rapport v1 (`c867a1b2…`) et son script (`b30c9db7…`), sceaux vérifiés ; candidat 1 de P3-bis (`9a56a657…`, égal à son
  compagnon : en-tête, code cité, plan, point 8, préalable P-9) ; contre-lecture `845c4de5…` (égale à son compagnon ; C-1 à
  C-4) ; texte scellé de T0.7 `prereg/T0.7-sondes-v0-v1.md` (`d7d180ec…`, égal à son compagnon : section « Module »,
  entrées, et « Accord au code », point 17 ; section « Écrits exigés par P3-bis », (d), lecture du journal) ; R-2103 et R-2113
  de `registres/decisions.md` (trouvées par `git grep -n 'D-1' -- registres/decisions.md`) ; la ligne `CODE-T07` et
  `registres/code-t07/CODE-T07-v2.json` (`d5eb0b66…`).

## Verdict

**Aucune discordance** entre l'écrivain (`5e457525`, modules `ouverture_p3bis_v3` et `ouverture_p3bis_v2`) et le lecteur de
T0.7 (C7 `b4cd9953`) : 126 lignes écrites lues telles quelles, 16 refusées comme les deux textes le prévoient, 0 mal
interprétée ; mêmes acceptations et mêmes lignes sur les 61 états du fichier ; un écart de traitement hors concordance
(journal non UTF-8, **O-1**) est signalé à la mère pour qualification.

Les quatre discordances de la v1 (D-1 à D-4) ne tiennent plus aux commits finaux (section 4). Le témoin muté (lecteur faussé à
dessein) est détecté par l'essai : 42 discordances de lecture et 6 désaccords de sondes relevés (section 2).

## 1. Pièces, bacs à sable et empreintes

Chaque côté est extrait **dans son propre bac** par `git archive <commit> src | tar -x -C <bac>`. L'empreinte de chaque
fichier extrait est comparée à celle du `git show` au même commit, à la valeur attendue écrite dans le script et au compagnon
au commit, quand il existe. L'écrivain et le lecteur tournent chacun dans **son propre processus** (`python -I`), qui n'ajoute
à son chemin d'import que son bac ; le script le vérifie (`__file__` de chaque module sous le bac). Le processus de l'écrivain
ne charge aucun module `controle_ia.t07` ; celui du lecteur ne charge aucun module `controle_ia.premier_test_ia` (listes
imprimées dans la sortie brute).

| côté | fichier | commit | sha256 | compagnon au commit |
|---|---|---|---|---|
| écrivain (nommé par la consigne) | `src/controle_ia/premier_test_ia/ouverture_p3bis_v3.py` | `5e457525` | `4a54a437e4a6031b1890f0f5f0261cf1141e72aee82d456d9fcd5483946693e9` | égal |
| écrivain (nommé par le plan, point 8 : `ouverture_p3bis_v2 ouvrir`) | `src/controle_ia/premier_test_ia/ouverture_p3bis_v2.py` | `5e457525` | `1361382e669f26d5568c81044e160c7fc122f4264832ffb70ec8d9b4714d2a13` (celle du commit `a1de3915`) | égal |
| dépendances de l'écrivain | `src/controle_ia/scellement.py` ; `gardes.py` ; `__init__.py` ; `premier_test_ia/__init__.py` | `5e457525` | `93beeb1c…` ; `a83c48ce…` ; `e3b0c442…` ; `c72da160…` | aucun |
| lecteur | `src/controle_ia/t07/journal_p3bis_v1.py` | C7 `b4cd9953` | `f83f03d54accc0ac189e05c2f3e865b27ecb817f6c9366836d6e38d016826f73` | aucun ; égale à `CODE-T07-v2.json` |
| importé par le lecteur | `src/controle_ia/t07/registre_v1.py` ; `t07/__init__.py` | C7 | `e50236574fbcd7e48ea3005eadc8bdb68d2c753d10028db7f2c365648a843cec` ; `553bd9d2…` | aucun ; égales à `CODE-T07-v2.json` |
| usager du lecteur (vue de T0.7) | `src/controle_ia/t07/garde_adaptee_v1.py` | C7 | `7ff571d7b1f06db94043545bfe178a066613ddd734aacca1cf3ef52ba0b511de` (inchangée depuis la v1) | aucun ; égale à `CODE-T07-v2.json` |
| communs | `src/controle_ia/__init__.py`, `gardes.py` | les deux | mêmes octets aux deux commits (vérifié) | aucun |
| ligne `CODE-T07` | `registres/code-t07/CODE-T07-v2.json` | `main` | `d5eb0b665df187d158fa84deff733b0f382fc309510163625f7aaea1ae9a692c` = cellule de la ligne ; champ `commit` = `b4cd9953…` | `.sha256` égal |

Les modules de T0.7 n'ont pas de compagnon `.sha256` à C7. Leur référence est donc le fichier de la ligne `CODE-T07`. Les
quatre empreintes y sont égales.

**v3 contre v2.** Dans le même bac, seules les fonctions `_main` et `commandes_des_lectures` diffèrent, et aucune constante de
module (comparaison par `inspect.getsource`, imprimée). Le journal est donc écrit par le même code dans les deux modules. Les
deux ont été joués ; leurs sorties sont égales à l'octet, une fois masqués les empreintes des paquets et le nom du module.

**Ce qui change depuis la v1.**
- Écrivain : de `02217f1c` (`330915f6…`) à `a1de3915`, D-1 à D-4 corrigés (commit `a1de3915`, R-2113), puis `5e457525`.
  L'arbre gelé n'y change que par des ajouts, et `ouverture_p3bis_v2.py` y garde l'empreinte de `a1de3915`.
- Lecteur : de `8dc1cb09` à C7. `journal_p3bis_v1.py` y change par le commit `a3539339` (D-3 : prédicat de l'écrivain
  appliqué en entier) et `registre_v1.py` par `13e7f85a` (seulement les listes des clés exigées et permises à l'étape A).
  `garde_adaptee_v1.py` est inchangé.

## 2. Méthode et passages

Script : `essai_concordance_journal_v2.py` (nom neuf ; la v1 est gardée telle quelle). Il reprend la v1 :
- même banc par scénario, avec les registres des préalables et des scellements, les décisions et les fichiers cités scellés ;
- un dépôt git jetable dans le bac à sable, avec deux jeux de paquets jouets faits par les fonctions de l'écrivain ;
- `ouvrir(…, instant=…)`, paramètre réservé aux essais, CP-08 ;
- les mêmes trois verdicts par ligne écrite : lue telle quelle, refusée ou mal interprétée.

« Lue telle quelle » exige les mêmes clé, date, instant, mode, appui, paquets et motif que ceux que l'écrivain relit dans sa
propre ligne, et le même sens : une ouverture du même mode, ou jamais une ouverture.

Il ajoute :
- **l'oracle du texte**. C'est le prédicat du plan, point 8, du candidat 1 de P3-bis, points (i) à (viii) avec le fichier
  vide et le journal absent, **récrit à la main d'après le texte**, sans importer aucun des deux codes. Il est jugé sur
  chaque journal final et sur chaque état du fichier, à côté de l'écrivain (`lire_journal`) et du lecteur
  (`lire_journal_p3bis`). Le texte de T0.7 (point 17) énonce le même prédicat. Lectures déclarées de l'oracle :
  - « espaces de bord » désigne l'espace U+0020 seulement ;
  - les chiffres de la date sont des chiffres ASCII ;
  - un fichier qu'on ne peut pas décoder en UTF-8 est hors format ;
- la **vue de T0.7** à l'étape B, comme en v1 : appui comparé aux lignes citées, codes de `garde_etape_b` sans
  `VERDICT-P3BIS`, réserve R14 ;
- un **témoin muté** (R5). Après la vérification des empreintes, le lecteur est faussé à dessein de deux façons : une ligne
  vide est ignorée (la tolérance du brouillon 19) et un refus est pris pour une ouverture. L'essai doit alors relever des
  discordances.

Passages, tous avec `/home/user/controle-ia-travail/.venv/bin/python -I` (Python 3.13.18, numpy 2.4.6, git 2.43.0) :

| passage | heures (UTC, `date -u`) | code | sortie |
|---|---|---|---|
| **retenu** | 2026-11-11, 13:44:37 → 13:44:40 | 0 | `sortie-essai-concordance-journal-v2.txt` (1 159 lignes) |
| **témoin muté** | 13:44:40 → 13:44:42 | 0 (détecté) | `sortie-temoin-concordance-journal-v2.txt` ; lecteur muté `5527f431…` |
| essais préalables, non versés | 13:42:19 → 13:42:23 ; 13:44:20 | 0 ; 0 | version antérieure du script (sans le témoin pour le premier) ; résultats identiques, hors empreintes des paquets (sel neuf) |

Le code 0 du passage retenu dit deux choses : chaque empreinte est conforme, et chaque tentative non exploratoire a donné à
l'écrivain l'issue visée avec le nombre de lignes visé. Les discordances ne changent pas ce code : elles sont imprimées.

## 3. Résultats

### 3.1 Chaque type de ligne, écrit puis lu (par module de l'écrivain : 50 scénarios, 77 tentatives, 71 lignes)

| groupe | scénarios | ce que l'écrivain fait aux commits finaux | lecteur de T0.7 |
|---|---|---|---|
| ouvertures, chaque mode et chemin | S01 à S05, S07 | comme en v1 : `pleine`, `deja-ouverte` (×2), erreurs d'appel sans ligne ; branche 1 avec `ni-scores-ni-ouvrir`, `ligne-absente` (E-3), puis complément ; branche 2 ; E-9 ; E-8 (réduite après `SCORES-T07`) ; `paquet-faux` sur d'autres paquets | toutes lues telles quelles ; vue : appuis conformes, `anticipee` (S03, S04), `attente-pleine` (S04), R14 où la réduite précède la fin de l'étape A |
| **D-2** | S06a, S06b, S06c, S08 | S06a : `pleine-anticipee` sous « ouvrir pleinement », lignes de T0.7 conformes → **refus `ni-scores-ni-ouvrir`**, puis `pleine` ouvre ; S06b : `pleine` d'emblée ; S06c (lecture littérale, R-2113 : `SCORES-T07` sans compagnon) → `pleine-anticipee` ouverte ; S08 : réduite, « ouvrir pleinement », `pleine-anticipee` refusée, `pleine` ouvre | lues telles quelles ; S06a, S08 : T0.7 lit 7b (aucun code) ; S06c : ouverture `pleine-anticipee` lue comme telle (nœud par le texte de T0.7), et vue refusée par T0.7 au registre (compagnon absent), cohérent |
| les dix-sept codes de refus | R01 à R17a, R08b | un refus chacun, code du premier défaut ; R14b rangé sous `garde-adaptee-absente` (chemin autre, D-4) ; **R08b** : clé `RENDEZ-VOUS-P3BIS-01` → `cle-inconnue` | lues telles quelles, jamais une ouverture ; R08b : T0.7 refuse le registre des préalables (« clé … inconnue : refus ») |
| journal hors format écrit à la main | R04b | refus `ligne-mal-formee`, ligne neuve qui suit | journal refusé (`JournalFautif`), comme les deux textes le prévoient |
| sans ligne (E-3 (b), (c)) | N01, N02, N04 | `registres/` absent ou chemin occupé : `JournalImpossible`, aucune ligne ; extraction en échec : code 1, la ligne reste | N01 : absent, aucune ouverture ; N02 : `JournalFautif` (pas un fichier) ; N04 : ouverture lue (sens prudent) |
| **D-3**, fichier vide | N05 | **hors format** : refus `ligne-mal-formee` avec ligne, **aucun en-tête écrit** ; il reste hors format à la tentative suivante | refusé (en-tête absent) aux deux tentatives, comme les deux textes le prévoient |
| **D-1** | D01, D02, D01b | D01 : horloge en arrière → **`HorlogeEnArriere`, refus sans ligne, code 2** ; D02 : même seconde permise ; D01b (C-2) : dernière ligne hors format, tenue pour antérieure, refus `ligne-mal-formee` daté avant une ligne plus haute | D01 : journal lisible (1 ligne) ; D02 : lu ; D01b : refusé (déjà hors format, puis date qui recule), comme les deux textes le prévoient |
| **D-4** | D04, D04b | D04 : réduite, `SCELLEMENT-T07` et garde citant un autre chemin → **refus `garde-adaptee-absente`** ; D04b (C-4) : voie normale, même chemin autre → `pleine` ouvre (chemin non jugé hors de la branche 1) | D04 : lu, aucune ouverture ; D04b : appui conforme, aucun code (T0.7 ne juge pas ce chemin pour une `pleine`) |
| fins de ligne (C-1) | X01 à X06 | section 3.2 | section 3.2 |
| exploratoire | N06 | journal non UTF-8 : section 5, O-1 | section 5, O-1 |

**Comptes par module** :
- 71 lignes écrites, dont 23 `OUVERTURE-P3BIS` et 48 `REFUS-OUVERTURE-P3BIS` ;
- 63 lues telles quelles, 0 mal interprétée ;
- 8 refusées, toutes dans des journaux rendus hors format à la main ou laissés hors format (R04b, N05 ×2, N06, D01b ×2,
  X05 ×2), refus que les deux textes prévoient ;
- sur les deux modules : 126 lues telles quelles et 16 refusées.

Les dix-sept codes de la liste fermée sont tous exercés. Aucune ligne de refus ne porte un code hors de la liste.

### 3.2 Retour chariot seul et fins de ligne mêlées (C-1 de `845c4de5…`), l'écrivain dans la boucle

| scénario | journal avant la tentative | écrivain | lecteur |
|---|---|---|---|
| X01 | CR seul partout | lit le journal ; `pleine` ouvre ; il ajoute `\n` (le fichier finit par CR, d'où CR LF) puis la ligne ; `deja-ouverte` ensuite | lignes lues telles quelles, ouverture `pleine` ; journal final mêlé, lu |
| X02 | en-tête CRLF puis CR, ligne LF ; puis CR, LF, CRLF en cycle | réduite, refus, `pleine` | toutes lues telles quelles ; appuis conformes ; R14 |
| X03 | CRLF partout | `pleine` ouvre | lue telle quelle |
| X04 | CR seul, **sans fin de ligne finale** | hors format : refus `ligne-mal-formee`, après le saut ajouté ; le journal redevient au format, et `pleine` ouvre | lu ; mêmes lignes |
| X05 | CR suivi de CRLF après l'en-tête (ligne vide) | hors format : refus `ligne-mal-formee` | refusé (ligne vide), comme les deux textes le prévoient |
| X06 | CR seul, dernière ligne à 12:00, horloge à 11:00 | `HorlogeEnArriere`, refus sans ligne : la dernière ligne est lue malgré le CR seul | lu (1 ligne) |

Sondes d'état ajoutées (section 3.3) :
- **lus pareil par les trois juges, mêmes lignes** : CR seul ; LF, CRLF et CR en cycle ; en-tête CRLF et corps CR ; CRLF ;
- **hors format pour les trois** : CR seul sans fin finale ; CR puis CRLF ; LF puis CR ; CR au milieu d'une ligne ; CR après
  le dernier LF.

### 3.3 États du fichier (61 par module : 9 instantanés des scénarios et 52 états écrits à la main)

| classe | nombre | oracle du texte | écrivain (`lire_journal`) | lecteur (`lire_journal_p3bis`) |
|---|---|---|---|---|
| au format | 15 | au format | lu | lu, **mêmes lignes** (oracle compris) |
| journal absent | 1 | absent | 0 ligne | absent (aucune ouverture) |
| hors format | 41 | hors format | refus `ligne-mal-formee` | `JournalFautif` |
| non UTF-8 | 1 | hors format | refus `ligne-mal-formee` | **`UnicodeDecodeError`**, et non `JournalFautif` (O-1) |
| écart du texte aux deux codes | 3 | hors format | lu | lu, mêmes lignes (O-2) |

L'écrivain et le lecteur acceptent et refusent **les mêmes 61 états** et rendent les mêmes lignes quand ils acceptent. Les
états hors format couvrent :
- le fichier : vide ; d'une espace ; d'un seul saut de ligne ; en-tête seul sans saut final ; BOM ; dossier ;
- les lignes : ligne vide ; espace en tête ou après le dernier `|` ; table alignée ; sans saut final ; cinq cellules ;
- les cellules : appui, paquets et motif hors forme (dix variantes) ; date impossible ; seconde 60 ; mode ou clé inconnus ;
- l'ordre : date qui recule ; deux ordres interdits.

Sont au format pour tous les trois : en-tête seul ; dates égales ; refus à appui d'une seule clé ; NUL et U+2028 dans le texte
d'un motif.

## 4. Les discordances de la v1 aux commits finaux

| v1 | tient-elle ? | comment elle a été traitée | preuve à cet essai |
|---|---|---|---|
| **D-1** dates décroissantes | **non** | décision de la mère, R-2103 : refus sans ligne si l'horloge précède la dernière ligne ; écrivain `a1de3915` (R-2113) : `exiger_format_journal` exige des dates non décroissantes (v3 l. 767-803), `exiger_horloge` est appelé dans `ouvrir` avant toute lecture (l. 1291) et dans `inscrire` ; texte : candidat 1, plan, point 8, (vii) et choix (b) ; lecteur inchangé (CT-11, l. 153) | D01 et X06 : refus sans ligne, journal lisible ; sonde « date qui recule » refusée par les trois juges ; reste C-2 (D01b), sens prudent, journal déjà hors format pour les deux |
| **D-2** croisement E-8 | **non** | R-2103, option (a) : le mode suit le registre ; écrivain `a1de3915` : `pleine-anticipee` refusée (`ni-scores-ni-ouvrir`, aucun code neuf) dès que `SCORES-T07` et `SONDES-T07` sont conformes (v3 l. 1186) ; lecture littérale (lignes non conformes : permise) acceptée par la mère (R-2113) ; texte : candidat 1, choix (d) ; lecteur inchangé (une `pleine-anticipee` est un nœud à toute date) | S06a et S08 : refus, puis `pleine`, et T0.7 lit 7b ; S06c : lecture littérale jouée, ouverture `pleine-anticipee` lue telle quelle ; l'issue ne dépend plus du mode tapé quand les lignes sont conformes |
| **D-3** tolérances de forme | **non** | R-2103 : un seul prédicat écrit dans les deux textes, appliqué en entier par le lecteur ; lecteur `a3539339` (dans C7) : `faute_de_cellules`, saut final, aucune ligne vide (l. 86-170) ; écrivain `a1de3915` : fichier vide hors format, jamais d'en-tête écrit dans un fichier vide ; textes : candidat 1, (i) à (viii), et T0.7, point 17 | 61 états : mêmes acceptations, mêmes lignes ; N05 : refus avec ligne, sans en-tête, refusé par T0.7 ; C-1 joué (section 3.2) |
| **D-4** chemin cité par la garde adaptée | **non** | R-2103 : l'écrivain exige `prereg/T0.7-sondes-v0-v1.md` dans `SCELLEMENT-T07` et la garde adaptée sous une dernière décision « ouvrir » (v3 l. 1084), refus `garde-adaptee-absente` ; lecteur inchangé (`garde_adaptee_v1` l. 132) ; texte : candidat 1, choix (a) ; C-4 : non jugé hors de la branche 1 | D04 : refus, aucune réduite au mauvais chemin ne peut s'écrire ; D04b : `pleine` ouverte, que T0.7 ne juge pas sur ce chemin |
| clé `RENDEZ-VOUS-P3BIS-01` (v1, lue au code) | **non** | même motif `[1-9][0-9]*` des deux côtés (R-2103) | R08b : `cle-inconnue` chez l'écrivain, « clé inconnue » chez T0.7 ; constantes égales |

## 5. Observations (aucune n'est une discordance de lecture ; rien n'est corrigé)

**O-1 — journal non UTF-8 : arrêt par une exception imprévue, des deux côtés (écart de traitement, à qualifier par la
mère).** Le fichier ne peut naître que d'une main ou d'une corruption : l'écrivain n'écrit que de l'UTF-8. Le scénario N06
(un octet `0xFF` dans le texte d'un motif) donne ceci :
- **Écrivain.** `lire_journal` le tient pour hors format (`ligne-mal-formee`, l. 812), et la ligne de refus est écrite
  (l. 4). Ensuite, la relecture de `inscrire` (l. 869) lève `UnicodeDecodeError`, qu'elle ne rattrape pas : `except OSError`
  seul, l. 871. `ouvrir` sort alors par cette exception et non par `RefusOuverture`. D'après le code (non joué en ligne de
  commande), cela donne une trace et le code 1, au lieu de « refus, code 2 ». Rien n'est ouvert.
- **Lecteur.** `lire_journal_p3bis` lève `UnicodeDecodeError` (lecture l. 121) au lieu de `JournalFautif`. D'après le code
  lu (non joué), `tenter` de `lecture_v2` (l. 405-411) et `main` de `lecture_v4` ne rattrapent que `GardeArret` : l'étape
  s'arrêterait par une trace, et non par « refus, code 2, nœud » journalisé (T0.7, point 17). Il en va de même à la relecture
  du journal en fin d'étape A (`lecture_v4` l. 533) : seule une `GardeArret` y est consignée dans le fichier d'arrêt
  (l. 561-563).
- **Bilan.** L'acceptation est la même (personne ne lit d'ouverture dans ce fichier, et l'oracle le tient hors format). Seule
  la forme de l'arrêt diffère du texte, des deux côtés.

**O-2 — trois états où la lecture étroite du texte est plus stricte que les deux codes** (même résultat pour l'écrivain et le
lecteur, mêmes lignes) :
- une tabulation au bord d'une cellule ;
- une espace insécable au bord d'une cellule ;
- des chiffres pleine chasse dans la date.

Les deux codes les acceptent (`str.strip()` et `\d` de Python), alors que l'oracle, qui lit « espaces » comme U+0020 et
« AAAA-MM-JJ… » comme des chiffres ASCII, les refuse. Le candidat 1 fixe le prédicat « à la lettre de
`exiger_format_journal` et `lire_ligne_journal` au commit `a1de3915` », et cette lettre est celle des deux codes. Aucun de
ces états n'est écrit par l'écrivain.

**O-3 — renvois périmés aux textes, sans effet.**
- Le texte scellé de T0.7 (point 17) et l'en-tête de `journal_p3bis_v1.py` citent le prédicat de l'écrivain à
  `330915f6…` (`02217f1c`), et non à `1361382e…` ou `4a54a437…`. Les ajouts de l'écrivain depuis (dates non décroissantes,
  fichier vide hors format) étaient déjà refusés par le lecteur : les ensembles acceptés sont égaux (61 états).
- Le plan, point 8, du candidat 1 nomme `ouverture_p3bis_v2 ouvrir` pour la garde. La consigne nomme `ouverture_p3bis_v3`.
  Les deux sont égaux pour le journal, et aucun script de `scripts/*p3bis_v2*` ni de `docs/procedures/P3-bis-temoin-positif-v1/`
  n'appelle `ouvrir` à `5e457525` (`git grep` avec exclusions).

**O-4 — inchangés depuis la v1, sans effet pour T0.7, qui ne lit pas cette cellule.**
- Cellule `paquets` d'un refus quand un seul des deux paquets a été relu : `-` (v3 l. 1251). Le texte dit « `-` si les
  paquets n'ont pas été lus ».
- Particularité de l'écrivain : un journal sans saut final redevient au format après sa ligne de refus (X04).

## 6. Limites

- Les fonctions sont jouées en Python, non par la ligne de commande ; l'instant est passé en paramètre. Les codes de sortie
  sont lus au code (`_main` de l'écrivain, `main` de `lecture_v4`).
- Côté T0.7, seules sont jouées les règles pures : `lire_journal_p3bis`, `lire_prealables`, `lire_decision`,
  `lire_registre_detail`, `verifier_lignes`, `controler_reduite`, `controler_pleine`, `garde_etape_b` et `reserve_r14`.
  `lecture_v2.ouvrir`, `lecture_v4` et l'étape A ne le sont pas.
- La concordance tient par construction en partie : le lecteur recopie le prédicat de l'écrivain. L'oracle récrit à la main
  et le témoin muté sont les contrôles extérieurs.
- Les droits d'accès au fichier n'ont pas été essayés (session `root`).

## Pièces versées (dossier `docs/notes/g0-deux-semaines-v1/concordance-journal-p3bis-t07-v2/`, chacune scellée)

- `essai_concordance_journal_v2.py` (`e39356487c59828071147e42b3e700de728c87cc1aa35fbe03f657f4da8512e1`) ;
- `sortie-essai-concordance-journal-v2.txt` (`87824b5ada18910195169c4e192a693d7f741f503fc18f6f77d883eaccfd2bc7`, passage
  retenu) ;
- `sortie-temoin-concordance-journal-v2.txt` (`1fe930e7be70da242748b1f1bf945d0434b872030b2f9381229955889f6ae006`) ;
- ce rapport.

## Interdits, écarts et refus

- **Interdits tenus.**
  - Aucun fichier ni aucune branche interdits ouverts.
  - Aucune recherche récursive : `git grep` avec exclusions (`diag`, `runs`, `docs/notes/bras-attaque`,
    `scripts/extraire_mesures_epreuve_t06_v1.py`), `grep` sur des fichiers nommés.
  - Aucune écriture git dans le dépôt de travail : lectures par `git show`, `git log`, `git diff --stat`, `git ls-tree`,
    `git archive`.
  - Aucun commit, aucun appel externe, aucune dépense, aucune suite d'essais lancée.
  - Écritures seulement sous ce dossier et sous le bac à sable
    `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/p3bis-p9/`, où vivent les extractions,
    les dépôts git jetables des bancs (`git init`, `GIT_CEILING_DIRECTORIES` posé) et les passages.
- **Écart déclaré.** Au début de la lecture, j'ai écrit une copie de lecture de `ouverture_p3bis_v3.py` (par `git show`) à
  la racine du dossier de brouillon, hors du bac nommé :
  `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/ob_v3_lecture.py`. Je l'ai effacée par son
  chemin exact avant d'écrire quoi que ce soit d'autre.
- **Refus rencontrés.** Aucun : ni contrôle de permissions ni classifieur n'a refusé d'action.
