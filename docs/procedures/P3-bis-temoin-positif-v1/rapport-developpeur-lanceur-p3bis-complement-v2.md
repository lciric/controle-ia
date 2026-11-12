# Rapport complémentaire du développeur du lanceur de P3-bis : contre-lecture différentielle (CD-01, CD-04, CD-05), borne de création, écrivain du journal des ouvertures (D-1 à D-4) — v2

- **Auteur** : le développeur du lanceur (Claude Opus 5.5, `claude-opus-5-5`), même fil que le rapport v1
  (`rapport-developpeur-lanceur-p3bis-v1.md`, `748568cbd7a72a2fe02eb7cedeb9981f9f6fb76bff230f20526dbfefa8799e34`) et le
  complément v1 (`rapport-developpeur-lanceur-p3bis-complement-v1.md`,
  `59e1da14e62f79e95755e54f1a9adf06b2ca80e990996dfc65e8f15db22eb14a`, gardé tel quel, R12).
- **Consignes** : (1) message de la mère après la contre-lecture différentielle
  (`brouillons/P3-bis-temoin-positif-v1/contre-lecture-differentielle-code-v2-chaine-v1.md`, sur `main`,
  `011942534477d65627b961f09e814c2fe0693d44b7d525633466fd4a918c00d9`, vérifiée ; R-2099) : CD-01 au code, CD-05 aux clones
  de la chaîne, borne de création du 18 novembre (R-2097, brouillon 10 `9038a015…`), CD-04 (seuil de la répétition finale
  mesuré), bancs et répétition jouet rejoués ; (2) message suivant (R-2103) : corrections de l'écrivain du journal
  (D-1 à D-4, clé `RENDEZ-VOUS-P3BIS-N`) **dans le même commit de code que CD-01**, chacune avec son essai R5, puis l'essai de
  concordance rejoué en copiant le script du rapport, contre mon code et contre le lecteur de T0.7 au commit `8dc1cb09`, lu
  par `git show` (exception explicite à l'interdit des fichiers de T0.7, limitée à ce rejeu). Pièces lues par `git show main:`
  et vérifiées : rapport de concordance
  `docs/notes/g0-deux-semaines-v1/concordance-journal-p3bis-t07-v1/rapport-concordance-journal-v1.md`
  (`c867a1b225fd94a02747fdfcf55580f4821f84bab5ea4658c69e0eb9916df335`), son script `essai_concordance_journal_v1.py`
  (`b30c9db7317e62fcfbf4f48a89927f33d69e86592f6243efbcfa6337e0808cef`), décision R-2103 de `registres/decisions.md`.
- **Heures** (`date -u`, heures des commits) : CD-01 commité à 07:51:58 ; chaîne (jalon 13) à 08:02:10 ; message R-2103 lu
  vers 08:07 ; commit du code à 08:26:12 ; rejeu de concordance de 08:26:58 à 08:27:31 ; essai de fermeture au commit du
  code de 08:30:54 à 08:40:00 ; bancs et répétition jouet de 08:31:47 à 08:47:33 ; liste ciblée de 08:40:00 à 09:02:19 (1 339 s) ; ce rapport
  ensuite.
- **Interdits tenus** : aucun `vastai` réel, aucune création, aucune dépense, aucun appel externe ; ni fetch ni push ;
  commits locaux sur `prep/p3bis-lanceur-v1` seulement ; épingles `A_EPINGLER` non remplies ; `registres/go.md` et
  `.claude/hooks/garde_calcul.py` intouchés ; garde des secrets à 0 avant chaque commit ; aucun refus de classifieur pendant
  cette passe. Fichiers de T0.7 : lus **seulement** par le rejeu de concordance (copie par `git show` des quatre fichiers du
  lecteur au commit `8dc1cb09`, empreintes vérifiées par le script), aucun ouvert autrement. **Deux manquements à la règle 9
  à déclarer** (section 6, écarts 1 et 2).

## Verdict

- **Commit du code proposé : `a1de39151ebae29138a389829751397074239615`** (jalon 14 ; ne touche que `src/` et `tests/` ;
  descend de `43266bd4`, qui porte CD-01) : CD-01 et les corrections D-1, D-2, D-3, D-4 et la clé de rendez-vous, chacune
  avec un cas sain et au moins un artefact ; les 33 essais neufs du journal font 15 échecs contre l'écrivain d'avant (les
  artefacts mordent) et passent tous contre le nouveau.
- **Essai de concordance rejoué** (écrivain `a1de3915`, lecteur `8dc1cb09`) : **47 lignes écrites, 45 lues telles quelles,
  2 refusées (toutes deux attendues par les textes), 0 mal interprétée, aucune discordance** ; constantes égales des deux
  côtés, clé de rendez-vous comprise. La base (`02217f1c`) est reproduite à l'identique du rapport (44 / 3 / 0, D01).
- **Essai de fermeture v2 au commit du code** : CONFORME (`brouillons/P3-bis-temoin-positif-v1/essai-fermeture-p3bis-v2-sortie-v3.txt`,
  `57d3467c7b7d700932da64ac449ca6a6dd9aed9fda1eee64d88c79f531382c78`). **Liste ciblée v2 au commit du code**, clone partiel
  avec `docs/sources/` présent (1 688 fichiers suivis) : **531 passed** (N de la liste v2), aucun essai sauté.
- **Bancs** : 144 + 58 + 99 + 46 + 42 = **389 cas, 0 non conforme** ; **répétition jouet conforme** (21 étapes et
  vérifications, 579 s) ; deux essais de développeur neufs (bloc `verifier-arbre` du scellement : 3 cas ; garde de place de la
  répétition finale : 3 cas), 0 non conforme.
- **CD-04** : seuil de la répétition finale fixé à **12 692 612 ko** = mesure 11 644 036 ko + marge écrite 1 048 576 ko
  (section 4).

## Commits (branche `prep/p3bis-lanceur-v1`, locaux, après `776b26cb`)

| commit | jalon | contenu |
|---|---|---|
| `43266bd4` | 12 | code : CD-01 (`exclure_localement`) et ses 5 essais ; dépassé comme « commit du code » par son descendant `a1de3915` |
| `58d60660` | 13 | chaîne : borne de création du 18 novembre ; clones en extraction partielle (CD-05) ; seuil de la finale « à mesurer » ; bancs ; sortie v2 de l'essai de fermeture au commit `43266bd4` ; copie du brouillon 10 |
| **`a1de3915`** | 14 | **code** : écrivain du journal (D-1 à D-4, clé) et ses 33 essais ; **commit du code proposé** |
| `8ad29273` | 15 | sortie v3 de l'essai de fermeture au commit `a1de3915` ; rejeu de l'essai de concordance |
| (suivant) | 16 | CD-04 (seuil), journaux du développeur v3, deux essais de développeur, ce rapport, scellés |

## 1. Code : le commit `a1de3915`

`src/controle_ia/premier_test_ia/ouverture_p3bis_v2.py` (`1361382e669f26d5568c81044e160c7fc122f4264832ffb70ec8d9b4714d2a13`),
code de l'autre développeur, modifié sur ordre ; le paragraphe « Corrections de l'écrivain du journal » de sa docstring dit
les règles.

| point | correction | essais (fichier) : cas sain | artefacts |
|---|---|---|---|
| CD-01 | `exclure_localement` refuse, motif écrit, rien d'écrit, si la racine git trouvée n'est pas la racine donnée, si c'est un arbre lié (`.git` fichier), ou si le fichier d'exclusion tombe hors de `<racine>/.git` | `..._exclusion_v1.py` (5) : racine d'un clone, motif écrit une fois | sous-dossier d'un dépôt (deux profondeurs) ; arbre lié ; `fermer_run` sur un sous-dossier refusé avant toute écriture ; hors de tout dépôt. Dossier temporaire, `GIT_CEILING_DIRECTORIES` |
| D-1 | (i) `exiger_format_journal` : dates non décroissantes (un recul rend le journal hors format, `ligne-mal-formee`) ; (ii) `exiger_horloge`, appelée par `ouvrir` juste après la prise de l'horloge et avant toute lecture des registres, et par `inscrire` : horloge antérieure à la date de la **dernière ligne** du journal → `HorlogeEnArriere` (sous-classe de `JournalImpossible`), **refus sans ligne, code 2**, rien d'ouvert ; date égale permise ; dernière ligne hors format (illisible, vide, sept cellules…) **tenue pour antérieure** (`instant_de_la_derniere_ligne` rend `None`) : le refus `ligne-mal-formee` suit, avec sa ligne | `..._journal_v1.py` : journal à dates égales ; ouverture à la même seconde que la dernière ligne ; `inscrire` à la même seconde | recul d'une seconde (format) ; horloge une seconde avant (Python) et horloge réelle en arrière en ligne de commande (`_main` → 2, « REFUS : horloge … ») ; après une ouverture, horloge en arrière : refus sans ligne et non `deja-ouverte` datée en arrière ; dernière ligne hors format datée après l'horloge : refus de format, puis l'horloge se compare à la ligne neuve ; `inscrire` d'une ligne datée avant la dernière |
| D-2 | `pleine-anticipee` refusée dès que `SCORES-T07` et `SONDES-T07` sont inscrites et conformes (`chemin_normal` vide), avant tout autre examen du mode : code **`ni-scores-ni-ouvrir`**, motif écrit « … le mode suit le registre, jamais l'opérateur (D-2, R-2103) » ; `pleine` reste permise (chemin normal « rendez-vous sans objet », ou complément de la réduite) | branche 2 sans lignes de T0.7 ; lignes inscrites mais non conformes (compagnon autre) : branche 2 permise | S06a (« ouvrir pleinement » + lignes conformes) ; sans décision ; E-9 (réduite, puis « ouvrir pleinement », lignes conformes : seul le complément `pleine` passe) |
| D-3 | fichier vide (0 octet) hors format ; `inscrire` n'écrit l'en-tête que dans un journal **absent**, jamais dans un fichier vide, qui reste donc hors format à toute tentative suivante ; formes refusées : toutes celles du tableau D-3 du rapport, CRLF seul admis | journal tel qu'écrit et en-tête seul (LF et CRLF) ; journal absent | les 16 formes du tableau (ligne vide au milieu, en fin ; sans saut final ; espace en tête ; séparation alignée ; `OUVERTURE` à paquets, appui ou motif hors forme ; `REFUS` à motif hors liste, sans code, à appui hors forme ; date impossible ; mode, clé inconnus ; ordre interdit ; dates décroissantes) et le fichier vide ; journal vidé après une ouverture : jamais de seconde ouverture |
| D-4 | `SCELLEMENT-T07` **et** `GARDE-ADAPTEE-T07-P3BIS` doivent citer `prereg/T0.7-sondes-v0-v1.md` (`PREREG_T07`), sinon `garde-adaptee-absente`, motif « … attendu (D-4, R-2103) » | les deux lignes au bon chemin : réduite ouverte | même texte (même empreinte) sous `prereg/T0.7-autre-v1.md`, cité par les deux lignes, par `SCELLEMENT-T07` seule, par la garde seule |
| clé | `RENDEZ_VOUS = RENDEZ-VOUS-P3BIS-([1-9][0-9]*)`, égal au motif du lecteur | `-1`, `-9`, `-10`, `-123` lus | `-01` et `-0` au registre des préalables : `cle-inconnue` (comme chez le lecteur) ; `-007`, `-`, `-1a` hors motif |

**Essais existants changés** (fichier de l'autre développeur, dans la liste v2 ; leur nombre ne change pas, 73) :
`tests/test_premier_test_ia_ouverture_p3bis_v2.py`, deux attentes qui codaient l'ancienne règle : fichier vide (accepté
avant R-2103, refusé désormais) et « numéro 01 » (`rendez-vous-non-consecutif` avant, `cle-inconnue` désormais).

**Comptes** (au commit `a1de3915`) : `test_premier_test_ia_ouverture_p3bis_v2.py` 73, `..._exclusion_v1.py` 5,
`..._journal_v1.py` 33, `test_premier_test_ia_ouverture_p3bis_v1.py` compris : **158 passed** ; fichiers qui importent le
module (`test_premier_test_ia_lecture_p3bis_gardes_v1.py`, `test_script_p3bis_v2.py`) : 16 passed. **Contre l'écrivain
d'avant** (`43266bd4`, copie hors de l'arbre) : 15 des 33 essais du journal échouent (chaque correction est prise en défaut),
18 passent (cas sains et formes déjà refusées).

## 2. Essai de concordance rejoué

Copie du script du rapport, changée en quatre points seulement, tous écrits en tête de la copie et versés en différentiel
(`brouillons/P3-bis-temoin-positif-v1/concordance-journal-rejeu-v1/`) : (1) écrivain lu au commit `a1de3915` avec son
empreinte (lecteur inchangé, `8dc1cb09`, quatre fichiers aux empreintes du rapport) ; (2) issues visées de D01, S06a, D04
et N05 changées selon R-2103 ; (3) la lecture du fichier vide par l'écrivain dans N05 prise dans un `try` (elle refuse
désormais ; sinon l'essai s'arrête) ; (4) un scénario ajouté, R08b (`RENDEZ-VOUS-P3BIS-01`). Dossier neuf du bloc-notes,
`GIT_CEILING_DIRECTORIES` posé par le script ; interpréteur en `-I -B`.

| | base (`02217f1c`, script tel quel) | rejeu (`a1de3915`) |
|---|---|---|
| lignes écrites | 47 | 47 (D01 : une de moins ; R08b : une de plus) |
| lues telles quelles | 44 | **45** |
| refusées | 3 (R04b, attendue ; D01 l. 3 et l. 4, **non attendues**) | **2** (R04b et N05, attendues des deux côtés) |
| mal interprétées | 0 | 0 |
| discordances | D01 | **aucune** |
| constantes | une différente (clé de rendez-vous au registre) | **toutes égales** |
| D01 (horloge en arrière) | ouverture datée avant la ligne précédente ; T0.7 refuse le journal entier | **refus sans ligne** (code 2) ; T0.7 lit la seule ligne du refus |
| S06a (E-8 croisé) | ouverture `pleine-anticipee` (T0.7 : nœud sur 7b) | **refus `ni-scores-ni-ouvrir`** ; T0.7 : jamais une ouverture ; le complément `pleine` (S06b) reste |
| D04 (autre chemin) | réduite ouverte ; T0.7 : `appui-faux` | **refus `garde-adaptee-absente`** |
| N05 (fichier vide) | écrivain : 0 ligne, ouverture ; T0.7 refuse le fichier avant | **refus `ligne-mal-formee`** des deux côtés |
| R08b (`-01`) | — | refus `cle-inconnue`, ligne lue telle quelle |

**Reste au lecteur** (sondes de tolérance, inchangé de mon côté, à la charge du développeur de T0.7 selon R-2103 : « appliqué
en entier par le lecteur ») : ligne vide au milieu ou en fin, absence de saut final, espace en tête, cellules `appui`,
`paquets`, `motif` hors forme : l'écrivain refuse, le lecteur `8dc1cb09` accepte. Le fichier vide est désormais refusé des
deux côtés. Fichiers : copie `essai_concordance_journal_v1_rejeu_a1de3915.py` (`9c2926e3…`), différentiel
`ecart-script-rejeu-a1de3915-v1.diff` (`12a3612c…`), sorties `sortie-base-02217f1c-v1.txt` (`c87e879f…`) et
`sortie-rejeu-a1de3915-v1.txt` (`3e2fada3…`).

## 3. Essai de fermeture et liste ciblée au commit du code

Script `bloc-notes/essai-et-liste-a1de3915.sh` (non versé) : clone partagé de `/home/user/controle-ia-travail` à la branche
`prep/p3bis-lanceur-v1`, **extraction partielle** aux motifs de la chaîne (CD-05), extraction de `a1de3915`, absence des
quatre chemins interdits vérifiée ; `docs/sources/` présent (1 688 fichiers suivis), le compte de la liste vaut donc.

- **Essai différentiel de fermeture v2** : 546 s (sous charge : bancs en parallèle), code 0, **CONFORME** ; 18 lignes
  `CONFORME — …`, aucune `NON CONFORME` ; durées 11,32 à 19,28 s, plus grand écart entre issues substituées 7,96 s (seuil
  30 s) ; longueurs comprimées : plage totale 11 octets, plus grande plage d'une issue 8. Sortie
  `essai-fermeture-p3bis-v2-sortie-v3.txt` (`57d3467c…`), nom neuf : la v2 (`ea969ed6…`, au commit `43266bd4`) reste (R12).
- **Liste ciblée v2** (`scripts/essais-cibles-p3bis-v2.txt`, inchangée) : 08:40:00 – 09:02:19, code 0, **531 passed in 1337.00s**, aucun essai sauté (`-rs`) ; dossier temporaire 1 811 908 ko à la fin.
- **Liste au commit `43266bd4`** : arrêtée par moi vers 40 % (≈ 08:19), devenue sans objet avec le commit `a1de3915` ;
  aucun compte n'en est tiré.

## 4. Chaîne (jalon 13 et ce jalon)

- **Borne de création du 18 novembre** (R-2097) : constante `BORNE_CREATION=2026-11-18` dans `lancer_p3bis_v1.sh` et
  `verifications_p3bis_v1.py`, appliquée **en plus** de l'échéance du GO (23 novembre) ; jour UTC postérieur : « aucune
  création, relance comprise ». Essais : module commun (18 sain ; 19 et 23 refusés par la borne ; 24 « hors de la
  validité » ; constante retirée : artefact) et lanceur (L06 à L06d, L07 : 18 sain, 19 et 23 refusés, passage du 18 au 19).
  La valeur du texte « aucune création, relance comprise, après le 18 novembre 2026 » est exigée au brouillon 10 (19/19
  valeurs) ; le brouillon 9 l'ignore (écart déclaré, inchangé).
- **CD-05** : les clones des contrôles, de la récupération et de la répétition finale se font en extraction partielle
  (`'/*' '!/docs/notes/bras-attaque/' …`), suivie d'un essai d'absence (`REFUS … extrait sur disque`, code 2) ; le
  scellement ne joue plus `verifier-arbre .` sur le dépôt : il vérifie les trois fichiers neufs par leur sceau, extrait S par
  `git archive` des seuls dossiers scellés, chemins interdits exclus par pathspec, vérifie leur absence et joue
  `verifier-arbre` sur cette extraction, avant toute poussée. Essais : bancs des contrôles (K00 sain, K36 artefact : la
  ligne d'extraction neutralisée → refus) et de la récupération (R00, R16), avec un témoin **fabriqué**
  `docs/notes/bras-attaque/temoin-banc.txt` dans leurs dépôts synthétiques ; **essai de développeur neuf du bloc du
  scellement** (le scellement n'est joué que par la répétition finale) : bloc extrait tel quel (13 lignes, une seule
  changée : `PYTHONPATH`), sur un dépôt synthétique à témoins fabriqués : sain (arbre intact), exclusion retirée (refus, S
  non poussé), fichier scellé altéré (échec de `verifier-arbre`, S non poussé) : 3 cas conformes.
- **CD-04** : fait. La répétition finale clone le dépôt, en fait un dépôt nu, joue la copie du scellement (qui extrait S par
  `git archive` pour `verifier-arbre`, puis l'efface), puis les contrôles (un second clone, l'essai de fermeture, le
  tokeniseur, la liste ciblée sous le `basetemp` par défaut de pytest, dans `/tmp`, même disque). J'ai rejoué les mêmes
  commandes au commit `a1de3915` (clones partagés d'un dépôt superficiel : les objets sont copiés à chaque clone) et relevé
  l'essai et la liste toutes les 10 s :

  | pièce | ko | relevé |
  |---|---|---|
  | dépôt (clone partagé, extraction partielle) | 4 168 320 | `du`, dont `.git` 1 641 732 |
  | dépôt nu `distant.git` | 1 558 424 | `du` |
  | extraction du scellement (`git archive`, chemins interdits exclus ; effacée avant les contrôles) | 2 404 304 | liste de l'archive, blocs de 4 Kio |
  | clone des contrôles (depuis le dépôt nu, extraction partielle) | 4 087 844 | `du`, dont `.git` 1 561 252 |
  | dossier temporaire de la liste ciblée v2 | 1 811 908 | `du` final (pic relevé 1 808 724) |
  | dossier de l'essai de fermeture | 17 540 | pic relevé |

  Pic pendant les contrôles : 4 168 320 + 1 558 424 + 4 087 844 + 1 811 908 + 17 540 = **11 644 036 ko** (pendant le
  scellement : 8 131 048 ko). Marge écrite : **1 048 576 ko** (1 Gio) : cache du tokeniseur (non mesuré : aucun appel
  externe ici), pics de l'essai entre deux relevés, croissance de S sur `a1de3915` (texte, journaux : quelques Mo), écart
  entre `du` et `df`. **Seuil : `PLACE_MIN_KO=12692612`** (`repetition_finale_p3bis_v1.sh`, brouillon 3, mesure écrite en
  tête). Les écritures d'autres sessions pendant la répétition ne sont pas couvertes. Essai R5 de la garde sur une copie
  (épingles neutralisées, `DEPOT` absent, trois lignes changées) : place sous le seuil → refus avant toute écriture ; seuil
  non fixé → refus ; seuil sous la place → la garde laisse passer : 3 cas conformes. **Place libre aujourd'hui** :
  12 560 260 ko à 09:06, mes dossiers effacés : la répétition finale **refuserait** (il manque ≈ 132 000 ko) ; à libérer au
  candidat (consigne de la mère). Place regardée avant chaque passage (4,6 à 10,8 Go libres) ; **pendant** les passages
  parallèles, elle est descendue à 3 056 452 ko au plus bas (relevé toutes les 10 s ; mes clones de mesure, les bancs et
  d'autres sessions) : au-dessus des 3 000 000 ko de la consigne, mais ≈ 2,9 Gio, près de la limite. Déclaré.

## 5. Bancs et répétition jouet (après le commit du code)

| banc | heures | durée | cas | non conformes | journal |
|---|---|---|---|---|---|
| module commun | 08:31:47 – 08:31:57 | 10 s | 144 | 0 | `banc-verifications-p3bis-v1-dev.log` |
| lanceur | 08:31:57 – 08:32:59 | 62 s | 58 | 0 | `banc-lanceur-p3bis-v1-dev.log` |
| surveillance | 08:32:59 – 08:33:30 | 31 s | 99 | 0 | `banc-surveillance-p3bis-v1-dev.log` |
| récupération | 08:33:30 – 08:35:10 | 100 s | 46 | 0 | `banc-recuperation-p3bis-v1-dev.log` |
| contrôles | 08:35:10 – 08:37:54 | 164 s | 42 | 0 | `banc-controles-p3bis-v1-dev.log` |
| répétition jouet | 08:37:54 – 08:47:33 | 579 s | 21 étapes et vérifications | 0 | `repetition-jouet-p3bis-v1-dev.log` |

Journaux dans `journaux-developpeur-v3/` (les v1 et v2 restent, R12), avec les deux essais de développeur et leurs scripts.
La récupération et la répétition jouet emploient le vrai `ouverture_p3bis_v2.py` de l'arbre (`lectures-fermees`, lectures
décisives réelles) ; aucune ne touche `ouvrir`, que les corrections D-1 à D-4 changent : celles-ci sont éprouvées par les
essais du code (section 1) et le rejeu de concordance (section 2).

## 6. Écarts et réserves, déclarés

1. **Règle 9, passes antérieures** : j'ai joué `verifier-arbre .` à la racine de mon arbre (où `docs/notes/bras-attaque/`
   est extrait) aux jalons 5 et 7 et lors de vérifications de la première passe. L'outil a haché ces fichiers sans rien en
   afficher d'autre que « arbre intact ». Plus rien de tel depuis la consigne.
2. **Règle 9, cette passe** : pour mesurer l'extraction du scellement (CD-04), un `git ls-tree -r -l` sur `docs prereg runs
   diag livrables registres/passations` au commit `a1de3915` dont **l'exclusion était fautive** (filtre `awk` sur le mauvais
   champ) : noms et tailles des fichiers de `docs/notes/bras-attaque/` et des dossiers de la course 7a sont passés dans une
   somme `awk`, **sans affichage** (seuls trois totaux imprimés) et sans lecture de contenu. Mesure refaite par `git archive`
   aux exclusions par pathspec, comme le scellement (seule valeur retenue).
3. **D-2, code choisi** : aucun code de la liste fermée ne nomme ce refus ; j'ai pris `ni-scores-ni-ouvrir`, déjà le code
   des « modes demandés que le registre n'autorise pas » de ce module, et écrit la règle au motif. Un code neuf changerait la
   liste fermée du texte (et de T0.7, qui ne lit pas cette cellule) : à la mère.
4. **D-2, lignes inscrites mais non conformes** : lecture littérale de « inscrites et conformes » ; sous « ouvrir
   pleinement », `pleine-anticipee` reste permise si `SCORES-T07` ou `SONDES-T07` sont inscrites sans être conformes
   (essai sain écrit). À confirmer au brouillon 11.
5. **D-3, en-tête** : un fichier vide ne reçoit plus d'en-tête ; la ligne de refus y est écrite seule, et le journal reste hors
   format à toute tentative suivante (nœud, jamais de remise à zéro de `deja-ouverte`). Choix prudent, déclaré. Inchangé : un
   journal sans saut de ligne final est refusé puis `inscrire` ajoute le saut avant la ligne neuve (particularité notée par
   le rapport, sans effet pour T0.7).
6. **D-1, sens de « dernière ligne »** : la dernière ligne du fichier, non la plus tardive ; si elle est hors format, elle est
   tenue pour antérieure même si une ligne plus haute porte une date plus tardive (le journal est alors déjà hors format pour
   les deux lecteurs). D-1 (i) ajouté au format, puisque le lecteur refuse ce recul : sans lui, l'écrivain se relirait sans
   objection (D01 de la base).
7. **D-4** : la ligne de la garde adaptée est elle aussi exigée au chemin (le lecteur l'exige) ; ses deux fautes portent le
   même code.
8. **Essais neufs hors de la liste ciblée v2** : `..._exclusion_v1.py` (5) et `..._journal_v1.py` (33) ne sont pas dans la
   liste v2 (gardée, 531) ; une liste v3 qui les porterait (531 + 38) changerait N et l'empreinte de l'instance : à la mère
   (voisin de CD-06).
9. **Docstring du module** : elle cite encore le brouillon 9 comme texte qui fait foi ; seul le paragraphe des corrections
   (R-2103) est ajouté. Les règles D-1 à D-4 sont à porter au brouillon 11.
10. **Absence vérifiée, motif `diag/*/lecture-sondes-t06.json*`** : exclu de chaque extraction (motif de l'extraction
    partielle, pathspec du scellement), mais l'essai d'absence ne nomme que les quatre chemins (`docs/notes/bras-attaque`,
    les deux dossiers de la course 7a, l'extracteur) ; le seul fichier de ce nom connu est sous un dossier exclu et vérifié.
    Vérifier le motif lui-même demanderait un parcours développé par l'interpréteur (règle 9) ou `git ls-files` : non fait.
11. **Liste au commit `43266bd4`** arrêtée (section 3) ; sortie v2 de l'essai gardée, v3 neuve.
12. **Nettoyage** : cette fois, l'effacement de mes dossiers temporaires par leur chemin exact a été accepté ; effacés : clones
    et dossiers d'essai des passes précédentes et de celle-ci (dans le bloc-notes : `b2-recuperation`, `v2-recup-1`,
    `final2-recuperation`, `final3-*`, `final4-*`, `v2-rep-jouet`, `pt-cd01`, `pt-final2` à `pt-final4`, `mesure-cd04`,
    `mesure-a1de3915`, `liste-v2-cd01`, `liste-v2-a1de3915`, `essai-fermeture-cd01`, `essai-fermeture-a1de3915`, dossiers
    des deux rejeux de concordance et des deux essais de développeur). Restent des scripts et sorties texte du bloc-notes
    (quelques Mo). Un dossier `pytest-t07` du bloc-notes (01:40, qui n'est pas à moi) et un processus `pytest` de T0.7
    (PID 5426, pas à moi, vu par `ps` seulement) n'ont pas été touchés. La liste au commit `43266bd4` a été arrêtée par
    l'outil d'arrêt des tâches de fond, par son identifiant de tâche (jamais par motif, R10).
13. **Copie du brouillon 10** dans `brouillons/` de ma branche (jalon 13), octet pour octet celui de `main` (`9038a015…`),
    pour les bancs.

## 7. Fichiers et empreintes (au commit de ce rapport)

| fichier (sous `docs/procedures/P3-bis-temoin-positif-v1/` ou chemin donné) | changé depuis le complément v1 (`776b26cb`) | sha256 |
|---|---|---|
| `lancer_p3bis_v1.sh` | oui | `54a6020a667e6a092a9978d69d43b8fcab944cfe9374f591ae20c6459f0d433b` |
| `verifications_p3bis_v1.py` | oui | `08661404b74c5b0440297c94b67222793a7ee377b3256b87df0eab68da9390b0` |
| `controles_avant_depense_p3bis_v1.sh` | oui | `e1591d9d9c0141442204594452fe9df5adc3cc779c561afb7c78ec9df4ff2c67` |
| `surveiller_p3bis_v1.sh` | non | `dbaa6a62986f149741fce12e7165e0de6df5ca456e6d07badf78b91ddf2a122e` |
| `controle_cinq_minutes_p3bis_v1.sh` | non | `51411159616708fa45056cf95c536ab602496fe726706442ad1016a88a08153d` |
| `recuperation_p3bis_v1.sh` | oui | `0c967fe8e1749aa1936c24b78787147d8ceec1290f5125bee8d174c007c1cde5` |
| `detruire_p3bis_v1.sh` | non | `d44c97ea480127088a5976d62db4fa18fd3ffd978c86fe16f2ea6c60d11fc4d0` |
| `sceller_p3bis_v1.sh` | oui | `5f038fbb903b9719463f05180592aa5f50c36ade6a130804877c6843eaf3d8f3` |
| `repetition_jouet_p3bis_v1.sh` | non | `85096b6877e5560ee01e240aa9c0946010888aaefaf3cad0adc62ce720b792a7` |
| `repetition_finale_p3bis_v1.sh` | oui | `beccd8191e41e040cc3616522a45a7724c60e2a9e8509cdf6bda45a4eed6f540` |
| `essais_verifications_p3bis_v1.py` | oui | `ff0d34dae8a50e77c09b7000fb28d3eedeec0cb2f7de3369270b127b5f23e17e` |
| `essais_lanceur_p3bis_v1.sh` | oui | `88e17234ee8083f015422123e66725de2622822c25cc61398def6d93c859c6f5` |
| `essais_surveillance_p3bis_v1.sh` | non | `ed6474302300e66ec90755542aee08e2f2addcf221325fed48cfb74be1083636` |
| `essais_controles_p3bis_v1.sh` | oui | `3141664dda25237c56e108694a50303d99246ff37a0938f432cd02e494d70c1e` |
| `essais_recuperation_p3bis_v1.sh` | oui | `b91701490358e395da09e3ae28be5fee1985c11fae7c618043c9176dbe006fbb` |
| `journaux-developpeur-v3/banc-controles-p3bis-v1-dev.log` | neuf | `ca989f7fddf8586e1c655c2c4649e6a5359b6171e64d41931d465e628c3fb35c` |
| `journaux-developpeur-v3/banc-lanceur-p3bis-v1-dev.log` | neuf | `6478d3e605069089fb361a762aaa2172f1fd96347e8f9846bff53b8d7355481d` |
| `journaux-developpeur-v3/banc-recuperation-p3bis-v1-dev.log` | neuf | `b9d166892b93ee8cc342003cf234f3c348f8b7d0292ffb1dead92fbc09c079d4` |
| `journaux-developpeur-v3/banc-surveillance-p3bis-v1-dev.log` | neuf | `959d72cfa261609bcba554d75fe8d76a914e430c8764dec2802b5e77156f65de` |
| `journaux-developpeur-v3/banc-verifications-p3bis-v1-dev.log` | neuf | `c145d21b346f54e9a86df60613fa9936b8ced4bfaad4146d4075d5344c549ac4` |
| `journaux-developpeur-v3/essai-bloc-verifier-arbre-scellement-v1-dev.log` | neuf | `73c31bee9b850c17c8dc36928b7dd3fef152ebf9f08dc340b30ed33a36ff0442` |
| `journaux-developpeur-v3/essai-seuil-repetition-finale-v1-dev.log` | neuf | `19b667fd1e21298bde8a85a8c84f1e1b194b82a6b65a215ce736767491f34e82` |
| `journaux-developpeur-v3/essai_bloc_verifier_arbre_scellement_v1.sh` | neuf | `500fe0c240889df03dbb0dcdcb7fe1350c074919a139010d08c6b0235ed7e3ef` |
| `journaux-developpeur-v3/essai_seuil_repetition_finale_v1.sh` | neuf | `93186a290cf161a873654936926538338e99b1ae55874c88ea4d396907200be6` |
| `journaux-developpeur-v3/repetition-jouet-p3bis-v1-dev.log` | neuf | `0168dbd21fb5fa6ddcd6d7d2a154b4f6a7428761082e7f2dfc71366c634a07ca` |
| `src/controle_ia/premier_test_ia/ouverture_p3bis_v2.py` | oui | `1361382e669f26d5568c81044e160c7fc122f4264832ffb70ec8d9b4714d2a13` |
| `tests/test_premier_test_ia_ouverture_p3bis_v2.py` | oui | `8ba89a7bb5b8cedfa1acbec2383f81317eea3a70229158f00ce19bc3779b6e78` |
| `tests/test_premier_test_ia_ouverture_p3bis_v2_exclusion_v1.py` | neuf | `259454a38e4888a866a4fe1ab09d82dd2609f0f44ad6d10ad5595ca5a98f5389` |
| `tests/test_premier_test_ia_ouverture_p3bis_v2_journal_v1.py` | neuf | `3ef82a97a266c6082ee517bca648d8e30870bd3e2ae9765aae74ef76ea4a979a` |
| `brouillons/P3-bis-temoin-positif-v1/essai-fermeture-p3bis-v2-sortie-v2.txt` | neuf | `ea969ed6f5b56251d8afc4ba4b1b3fd3b1878e43b436666b4872ea1181f0cfc9` |
| `brouillons/P3-bis-temoin-positif-v1/essai-fermeture-p3bis-v2-sortie-v3.txt` | neuf | `57d3467c7b7d700932da64ac449ca6a6dd9aed9fda1eee64d88c79f531382c78` |
| `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon10.md` | neuf | `9038a015c5756a289bebd2f08b1c33b1f2a26eb829bb2c4bc2afec04648fd1f9` |
| `brouillons/P3-bis-temoin-positif-v1/concordance-journal-rejeu-v1/essai_concordance_journal_v1_rejeu_a1de3915.py` | neuf | `9c2926e3bbb08d5e2f78cec57c0eeaa81209cb72585fec70c61a0984074bfd41` |
| `brouillons/P3-bis-temoin-positif-v1/concordance-journal-rejeu-v1/ecart-script-rejeu-a1de3915-v1.diff` | neuf | `12a3612cbf8a6c55b5470d1d155b7a9726c1a87195733c240117c1498bea314c` |
| `brouillons/P3-bis-temoin-positif-v1/concordance-journal-rejeu-v1/sortie-base-02217f1c-v1.txt` | neuf | `c87e879fd1173920632c811f40887f51d9d170983c7f73ed341bb6ab444009a3` |
| `brouillons/P3-bis-temoin-positif-v1/concordance-journal-rejeu-v1/sortie-rejeu-a1de3915-v1.txt` | neuf | `3e2fada31983e82c1b90aed64bc210b24e292a9de3182f6d847b1e3fb13a37b4` |

Chaque fichier a son compagnon `.sha256` (R6) ; ce rapport est scellé à part.

## Ce qui reste

- À la mère : retenir `a1de3915` comme `COMMIT_CODE_P3BIS` (au brouillon 11 et à l'épingle `CODE_RELU`), citer la sortie v3
  de l'essai de fermeture (`57d3467c…`) ; trancher les écarts 3, 4, 8 ; porter D-1 à D-4 au texte.
- Côté T0.7 (R-2103) : lecteur strict ; rejouer la concordance sur les commits finaux des deux côtés (la copie versée se
  rejoue en changeant le commit du lecteur et ses empreintes).
- Au candidat : épingles `A_EPINGLER` (13), place disque (CD-04 : 12 692 612 ko libres exigés), CD-02, CD-03.
