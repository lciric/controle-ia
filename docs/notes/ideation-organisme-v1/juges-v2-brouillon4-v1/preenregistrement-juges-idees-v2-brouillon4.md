# Préenregistrement — étage des juges d'idéation, version 2 : le protocole par paires discrimine-t-il là où l'ancien sature ? (brouillon 4)

Statut : **brouillon 4, non scellé, non contre-lu, non scellable en l'état : B10 reste ouvert** (section 4 : le contrôle de
diagnosticité, joué avec la batterie figée et la batterie tenue à l'écart, refuse les matériaux de ce texte ; le lanceur refuse donc
tout lancement sur eux). 5 couples de la contre-lecture v3 appliqués et changements du brouillon 4, section 16 ; contre-lecture du
brouillon 3 : `/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/juges-v2-contre-lecture-v3/contre-lecture-preenregistrement-juges-idees-v2-v3.md`
(sha256 `ca288aa15a8845b14758d5c263ae7f5e891b54a2c125f74f3598f3796f563625`) et ses 5 couples `couples-contre-lecture-juges-idees-v2-v3.json`
(`80119546fec70e378b290a685245909e8f02a9fa53be7875e44ba7b9685d65a9`) ; contre-lecture du brouillon 2 :
`prereg/contre-lecture-preenregistrement-juges-idees-v2-v2.md` (sha256 `8b91ab570df978d05f6cbe38f1f0e2e33d5f78b238c8f54c334d61c195b74999`) et
ses 12 couples (`e20cdc1f1d77fe0176b53e926338cdc57e381df4f96328871f3405aa0599592c`) ; contre-lecture du brouillon 1 :
`prereg/contre-lecture-preenregistrement-juges-idees-v2-v1.md` (sha256 `1dc3c1943c5322731efa7deedd97e9cce7fe7746f6cec268bc05c3f980d43977`) et ses
40 couples (`ad48ba2f40287b9a46b79e5e64a243880d0b72b2e95cde06b3dbfc111e55d79a`).
Rédigé le 4 novembre 2026, de 02:22 à 02:40 puis de 05:23 à la fin indiquée au rapport (UTC, heures de `date -u` ; une pause de
la limite d'usage entre les deux) par un concepteur-développeur neuf, qui n'a écrit ni l'étage des juges existant, ni le protocole
v2, ni ses brouillons 1 à 3, ni leurs contre-lectures ; aucun appel de modèle, aucune clé, aucun réseau, aucun commit, aucun
compagnon `.sha256`. Code (R12, fichiers déjà neufs au brouillon 1, modifiés ici, branche `prep/juges-v2-brouillon4` partie de
`faff48b`) : `pole/juges_idees_v2.py`, `demonstrations/validation_juges_idees_v2.py`, `essais/test_juges_idees_v2.py`,
`essais/mutations_juges_idees_v2.py` ; empreintes, essais et banc au rapport (`prereg/rapport-redaction-juges-idees-v2-brouillon4.md`),
empreintes du code au bloc de la section 11, où se trouve aussi le **marqueur du commit** qui portera ce code. **GO : `GO-2026-11-02-32`** (calcul,
60 USD, accordé par Lazar le 2 novembre 2026, échéance le 16 novembre ; `registres/go.md` du dépôt de travail : lu le 4 novembre
2026 à 05:41 UTC sur cette machine, sha256 `233626047f497362976e2e4c3d570f70d9dab2b4c155a91ea980e524d4b8c1ea`, ligne 220 ; **réserve** : ce
fichier-là porte deux lignes `GO-2026-10-24-07` (lignes 53 et 54), et `configuration_v56.verifier_go_v56` le refuse en entier
(« identifiant GO-2026-10-24-07 en double »), à 60 USD comme à 59 et 61 ; le brouillon 3 avait vérifié le registre de la branche
(ligne 78, `45d56fa0…`) ; le registre que lira le lanceur est à désigner, section 13). Deux marqueurs
restent, celui du commit (section 11) et celui du relevé de l'épreuve des commandes (bloc `releve-epreuve`, section 4), et le lanceur refuse tout texte qui en porte encore un (comme tout marqueur entre doubles chevrons) ; il refuse aussi un texte sans le bloc du relevé (brouillon 4, I11). L'empreinte de la configuration (ligne `configuration_sha256` du bloc `plan-gele`,
sha256 du fichier tel que passé à `--configuration`) reste à produire sans marqueur : le lanceur la refuse tant qu'elle n'est pas une empreinte, puis tant qu'elle diffère du fichier ; la section 13 ordonne les trois pièces. Le scellement se fait sur une version contre-lue, renommée `prereg/preenregistrement-juges-idees-v2-vN.md` (N ≥ 1, sans
« brouillon ») ; l'entropie des graines de la course est l'empreinte de ce fichier-là.

## 1. Question et motivation

**Question.** Sur des fiches dont la qualité est connue par construction (témoins plantés), le protocole v2 des juges —
comparaisons par paires à l'aveugle avec preuve citée, ancres, budget de notables, règle de famille — **discrimine-t-il** les
bonnes fiches des mauvaises, **là où l'ancien protocole sature** (« notable » donné presque partout) ?

**Constat qui motive** (README principal, ligne du « second real round », sha256 du README lu
`a5e6b8622fbd7b319d74a01b9d2208c13a1e89dc17cdc37c4f1d99db6dd4b298`, ligne 125) : au second tour réel du 1er novembre 2026
(Kimi et Argon, 12 fiches), 11 fiches sur 12 « notables » (un juge 12 sur 12, l'autre 11 sur 12), accord brut 0,92, kappa de
Cohen nul. Ces chiffres sont ceux du dépôt public ; la trace agrégée est privée (sha256
`091ff9edefec3faa411ae786a28595c5d3648e1b7aa4c425d290a3e64544338a`), non relue ici.

**Diagnostic** (code cité à l'empreinte `c4c6ab12dc471eef078c116a4205a22d9b498da720ce71e37a0a6edae6c4239b` de
`pole/juges_croises_v53.py`) : (i) « notable » est une conjonction d'items de forme (`lire_verdict`, ligne 48) que toute fiche bien
rédigée satisfait, puisque le proposeur reçoit justement ce gabarit ; (ii) le jugement est absolu, une fiche seule, sans
référence de qualité connue ni plafond au nombre de notables ; (iii) rien n'oblige le juge à toucher le fond : ni dossier de
faits, ni preuve demandée ; (iv) au plafond, le classement (`classement`, lignes 117 à 127) départage par l'identifiant ; (v)
`kappa_cohen` (lignes 133 à 140) rend 1 quand l'accord attendu vaut 1, si bien que deux juges toujours « notable » paraîtraient en
accord parfait (`mesures_v54.kappa_cohen_v54` corrige, la lecture de la course ne l'emploie pas) ; (vi) au second tour, chaque
fiche avait un juge de sa propre famille. Ce diagnostic est un raisonnement sur le code et sur des propriétés connues des juges
fondés sur des modèles de langage (indulgence du jugement absolu, biais de position, préférence pour le texte long et pour sa
propre famille) ; aucun chiffre de la littérature n'est avancé.

**Ce que l'expérience compare.** Les deux protocoles, **sur les mêmes fiches, avec les mêmes juges et la même information** :
pour les lots témoins, l'ancien protocole reçoit sa consigne figée (pièce privée de la course 2), puis le dossier du lot, puis la
fiche ; le v2 reçoit sa consigne figée, le dossier et deux fiches. Sans le dossier, aucun protocole ne pourrait savoir qu'une
loi est fausse ou déjà établie : l'insérer dans l'ancien protocole isole l'effet du protocole de celui de l'information (écart
assumé à la reproduction exacte du second tour, section 10). **Bras sans dossier** (décision de Lazar, GO-2026-11-02-32) : le
juge A juge aussi les 30 témoins d'évaluation par l'ancien protocole **sans dossier** (consigne figée puis fiche seule, octet
pour octet la forme de l'entrée du second tour) ; ce bras sépare l'effet du protocole (v2 contre ancien, même dossier) de l'effet
du dossier sur l'ancien protocole (ancien avec dossier contre ancien sans dossier).

## 2. Hypothèses

- **H1 (l'ancien sature par construction).** Servi avec le même dossier, l'ancien protocole donne « notable » à presque tous
  les témoins, bons comme mauvais : sa part de notables reste haute et ses notes ne séparent pas bons et mauvais.
- **H2 (le v2 discrimine).** Le choix forcé entre deux fiches, adossé à une citation vérifiée de la fiche choisie et du
  dossier, fait remonter les lois vraies et neuves au-dessus des lois fausses, des redites, des affirmations vraies par
  définition, des textes longs sans affirmation réfutable et des prédictions de signe contraire à leur hypothèse.
  **H2b (lecture des tables).** En particulier, les lois fausses — la seule classe que les tables seules réfutent — sont classées
  sous les bonnes lois.
- **H3 (le v2 est fiable).** Sa discrimination se reproduit sur un second tirage (autre graphe de paires, autres ordres,
  autres identifiants), n'est pas pilotée par la position de présentation, et un juge d'une autre famille départage lui aussi
  les paires qui opposent une bonne et une mauvaise fiche.
- **H0, écrites d'avance.** (a) Le v2 ne discrimine pas mieux que le hasard : les juges ne lisent pas le dossier, ou tranchent
  par la forme ; (b) l'ancien ne sature pas sur ces témoins : le plafond du second tour tenait aux fiches réelles (l'ancien ne
  sature pas même sans dossier) ou à l'absence de dossier (il sature sans dossier, pas avec) — le bras sans dossier départage
  les deux branches ; (c) le v2 discrimine mais de façon instable, pilotée par la position, ou propre à un juge.

## 3. Prédictions chiffrées et signées (ouvertes dans les deux sens ; elles ne décident pas l'issue)

Juge A = Argon (`gemini-4-argon`), tirage 1, sur les 30 témoins d'évaluation (15 bons, 15 mauvais), sauf mention. « Aire » =
aire sous la courbe ROC (courbe des taux de vrais et de faux positifs) des notes entre bons et mauvais témoins (égalités comptées
pour moitié).

| | prédiction | justification | sens contraire possible, et ce qu'il dirait |
|---|---|---|---|
| P1 | ancien avec dossier : part de notables ≥ 0,80 | le second tour (11 sur 12) ; les témoins sont rédigés au même standard de forme | < 0,80 : le dossier suffit à l'ancien pour refuser des fiches ; H0(b) |
| P2 | ancien avec dossier : aire ≤ 0,65 | au plafond, presque toutes les notes sont égales | > 0,65 : l'ancien départage avec l'information ; H0(b) |
| P3 | v2 : aire ≥ 0,80 | choix forcé, citation du dossier exigée ; vérifier un nombre contre une table est à la portée d'un juge capable | < 0,80 : le juge ne lit pas la table ou ne la compare pas ; H0(a) |
| P4 | v2 − ancien : différence d'aire ≥ +0,15 | P3 et P2 | < +0,15 : le gain tient à l'information, pas au protocole |
| P5 | v2 : faux notables ≤ 0,10 et vrais notables ≥ 0,30 ; ancien : faux notables ≥ 0,70 | plancher des ancres et budget ; plafond de l'ancien | v2 > 0,10 : le plancher des ancres ne protège pas ; vrais < 0,30 : ancres inversées ou budget trop serré |
| P6 | kappa des paires mélangées (A contre B) ≥ 0,40 ; kappa de l'ancien ≤ 0,20 ou non défini | deux juges qui discriminent s'accordent sur ce qui départage | < 0,40 : la discrimination est propre à un juge (descriptif : sur des paires mélangées, ce kappa vaut à peu près (2p − 1)² pour deux juges indépendants justes à p) |
| P7 | Spearman entre tirages ≥ 0,50 et aire du tirage 2 ≥ 0,80 | plafond de la corrélation de rangs à 0,751 pour deux classes de 15 ordonnées au hasard à l'intérieur (`plafond_spearman_binaire`) | < 0,50 : notes instables même entre classes |
| P8 | part des victoires de la fiche présentée en premier dans [0,40 ; 0,60] et taux de bascule ≤ 0,40 | ordres tirés au hasard ; la bascule mêle biais de position et incertitude sur les paires de même qualité | hors bornes : préférence de position (D5 en tolère plus, section 6) |
| P9 | texte long : rang moyen v2 < 0,5 ; notable à l'ancien | la consigne v2 dit que la longueur ne compte pas ; l'ancien juge la forme | rang ≥ 0,5 : biais de longueur du juge |
| P10 | redites d'une loi établie : rang moyen v2 < 0,5 | la consigne nomme la nouveauté ; les lois établies sont au dossier | ≥ 0,5 : la nouveauté n'est pas vérifiée (classe difficile : la redite est **vraie**) |
| P11 | juge B (Astra), ancien avec dossier : part de notables ≥ 0,80 | même raison que P1 | < 0,80 : le plafond dépend du juge |
| P12 | ancien **sans dossier** (A) : part de notables ≥ 0,80 et aire ≤ 0,65 | le second tour (11 fiches sur 12 « notables », sans dossier) ; sans dossier, aucune fiche ne peut être sue fausse ou redite | < 0,80 : le plafond du second tour ne se reproduit pas sur ces témoins, même dans ses conditions ; H0(b), première branche |
| P13 | effet du dossier sur l'ancien (A) : part de notables avec dossier moins part sans dossier ≥ −0,10 | l'ancien juge la forme ; le dossier change peu ses verdicts | < −0,10 : le dossier suffit à l'ancien pour refuser des fiches ; H0(b), seconde branche |
| P14 | lois fausses contre bonnes (v2, A) : aire ≥ 0,75 | H2b : la table réfute le chiffre affirmé ; un juge qui ne lit que les tables y arrive (aire 0,991, D1b 20 fois sur 20) ; sur ces matériaux, des juges de surface y gagnent encore (aire des lois fausses jusqu'à 0,758, section 4 : B10 ouvert) | < 0,75 : le juge ne vérifie pas les nombres ; un succès de D1 viendrait des autres classes |
| P15 | prédictions de signe contraire (classe que la consigne ne nomme pas en propre) : rang moyen v2 < 0,5 | la consigne demande un signe compatible avec le dossier | ≥ 0,5 : le juge ne lit que l'hypothèse (portée, section 10) |
| P16 | juge B, paires mélangées : exactitude ≥ 0,75 | B est un juge capable d'une autre famille | < 0,75 : la discrimination dépend du juge ; avec D6 non tenu, H0(c) |

Le code évalue chacune (`predictions_v2`) ; leur succès ou leur échec est rapporté, jamais lu comme issue.

## 4. Plan

**Matériaux (témoins plantés), gelés avant la course.** `juges_idees_v2.construire_materiaux(20261102)` (jeu « mondes-v4 ») :
**trois mondes** à loi plantée dans le domaine du programme — `monde-1` (agent de code, moniteur qui classe « suspect »),
`monde-2` (agent de navigation, moniteur à score de suspicion), `monde-3` (agent d'assistance qui rédige des courriels et gère
un agenda, moniteur qui classe « hors mandat ») —, chacun de 3 000 épisodes simulés (douze ou treize caractéristiques
indépendantes, alerte tirée selon une loi logistique plantée, avec une interaction), tirés de nouveau jusqu'à ce que le dossier
montre nettement chaque vérité (`contraintes_monde` : effet vrai ≥ 5 points entre niveaux extrêmes, effet nul ≤ 1,5 point entre
niveaux, y compris pour une caractéristique graduée sans effet, interaction ≥ 6 points ; et, dans monde-2 et monde-3, une **table 3**
où l'effet d'une caractéristique ordinale d'effet vrai diffère d'au plus 3 points entre la catégorie nommée et les autres ;
tentatives retenues : 23, 34, 98 ; simulation inchangée depuis le brouillon 3).
Chaque monde donne un **dossier** (contexte, deux lois déjà établies, deux ou trois tables de taux à lignes numérotées D01… ;
brouillon 4 : **une ligne par caractéristique**, voir plus bas) et **douze fiches** au format du tour fermé (titre, hypothèse,
prédiction, signe, métrique, test de mort) :

| rôle | classe | monde-1 | monde-2 | monde-3 | qualité |
|---|---|---|---|---|---|
| évaluation | loi vraie absente des lois établies, chiffres honnêtes du dossier (une graduée croissante, une décroissante, une catégorie contre les autres, une de deux groupes sur une caractéristique peu plausible a priori, une interaction) | 5 | 5 | 5 | bonne |
| évaluation | loi fausse bien rédigée, **jumelle d'une bonne loi** d'évaluation du même monde, du même gabarit et du même type de caractéristique (mêmes variantes de rédaction, mêmes nombres écrits ; seule la caractéristique change ; la table montre ≤ 1,5 point, ou, pour une interaction, ≤ 3 points de différence) : graduée (jumelle de la graduée croissante), de deux groupes (jumelle de la binaire), ou interaction (jumelle de la bonne interaction) | 2 (graduée, deux groupes) | 2 (interaction, deux groupes) | 3 (graduée, interaction, deux groupes) | mauvaise |
| évaluation | redite d'une loi établie, en d'autres mots (vraie, chiffres honnêtes) | 1 | 1 | 1 | mauvaise |
| évaluation | prédiction de signe contraire à une hypothèse vraie | 1 (hypothèse décroissante) | 1 (hypothèse croissante, prédiction décroissante) | 1 (hypothèse décroissante) | mauvaise |
| évaluation | affirmation vraie par définition (le moniteur alerte quand il classe « suspect ») | 1 | 0 | 0 | mauvaise |
| évaluation | texte long sans affirmation réfutable | 0 | 1 | 0 | mauvaise |
| ancre bonne | loi vraie neuve graduée | 1 | 1 | 1 | bonne |
| ancre mauvaise | loi fausse de deux groupes, appariée à un point près (comme au brouillon 3) | 1 | 1 | 1 | mauvaise |

**Gabarits, a priori, sens, ampleur, rédaction, place dans le dossier (contre-lectures v1, B1 ; v2, B8 et M12 ; v3, B10).** Les
matériaux du brouillon 1 (`c3eeb559…`) séparaient les classes par le gabarit et l'a priori ; ceux du brouillon 2 (`59737a16…`) par
l'ampleur et les seuils annoncés ; ceux du brouillon 3 (`2ee2f2e4…`, appariés à un point près) par quatre traits que son rédacteur
n'avait pas contrôlés (contre-lecture v3, B10) : le rapport du seuil d'abandon au seuil de prédiction (seuils recalculés sur
l'écart décalé d'un point : D1 13 fois sur 20, D1b 14), le rang de la caractéristique dans le dossier (caractéristiques sans
effet écrites en fin de bloc), le nombre de lignes du dossier qui la nomment (la table croisée la répétait sur 13 lignes) et la
longueur moyenne des mots. Les matériaux de ce texte (jeu « mondes-v4 », mêmes caractéristiques, même loi plantée, mêmes
interactions et tables 3, mêmes tirages que le brouillon 3) **retirent par construction** :
(1) **lois fausses jumelles** — chaque loi fausse d'évaluation est la copie d'une bonne loi d'évaluation du même monde, du même
gabarit et du même type de caractéristique (même nombre de niveaux), sur le même flux de graines (mêmes variantes de rédaction) et
avec les mêmes nombres écrits (taux, écarts, seuils) ; seule la caractéristique change : tout trait du seul texte de la fiche qui
ne dépend pas de la caractéristique prend la même valeur sur la loi fausse et sur sa jumelle (sept paires) ;
(2) **seuils pairs** — seuil de prédiction pair, seuil d'abandon égal à sa moitié exacte, pour toutes les fiches sauf la définition
(90 et 45) : le rapport abandon/prédiction vaut 0,5 et la parité du seuil de prédiction est la même partout ;
(3) **dossier à une ligne par caractéristique** — chaque caractéristique est nommée sur une seule ligne de la table 1 (ses niveaux
sur la même ligne) ; les tables croisées et les lois établies la désignent par le numéro de cette ligne (« la caractéristique de la
ligne D07 ») : une seule ligne du dossier nomme chaque caractéristique ;
(4) **ordre de la table 1 tiré par graine** (tâche `materiaux|<monde>|ordre-table1`, puis `…|<t>`) jusqu'à ce que les rangs
moyens (absolus, et relatifs au bloc de même nombre de niveaux) des caractéristiques des bonnes fiches, des mauvaises et des lois
fausses d'évaluation soient à 0,5 rang (0,1 en relatif) près dans chaque monde (`_rangs_equilibres`) ;
(5) **texte long aux mots ordinaires** (la version des brouillons 2 et 3 était faite de mots longs) ;
(6) **méthode de Wilson nommée par toutes les fiches** (la métrique de l'interaction la nomme aussi).
**Reste au hasard** : tout trait qui dépend de la caractéristique elle-même (son nom, ses mots, son rang tiré dans la tolérance de
(4)), et tout trait qui compare les **huit bonnes lois sans jumelle** aux **sept qui en ont une** (taux honnêtes tirés par la
simulation : par exemple la part de nombres ronds) ; et, pour D1, les classes qui ne sont pas des lois fausses (redites, signes
contraires, définition, texte long), dont le texte diffère par nature. C'est ce que mesurent les deux batteries ci-dessous. Une
caractéristique d'effet vrai reste sans fiche dans chaque monde ; chaque caractéristique porte une étiquette d'a priori fixée dans
le code avant toute course.

**Contrôle de forme** (`controle_forme`, avant tout appel) : dix-neuf indices de forme (brouillon 4 : parité du seuil de
prédiction, rapport abandon/prédiction, rang de la caractéristique dans le dossier, nombre de lignes qui la nomment, longueur
moyenne des mots, ajoutés aux quatorze du brouillon 3) et le vocabulaire, chacun borné dans [0,35 ; 0,65] **sur deux
comparaisons** — bons contre mauvais témoins d'évaluation (D1) et bonnes lois contre lois fausses (le sous-ensemble de D1b) —, sinon
refus ; un indice illisible pour une fiche (aucun seuil, aucune caractéristique) ne compte pas pour elle. Sur les matériaux de ce
texte : **conformes** ; sur ceux des brouillons 3, 2 et 1 : refusés.

| indice | ce texte : bons contre mauvais | ce texte : bonnes lois contre lois fausses |
|---|---|---|
| longueur | 0,527 | 0,481 |
| chiffres | 0,422 | 0,429 |
| gabarit_gradue | 0,500 | 0,514 |
| caracteristique_binaire | 0,467 | 0,386 |
| a_priori_plausible | 0,520 | 0,543 |
| sens_croissant | 0,493 | 0,400 |
| ecart_affirme | 0,496 | 0,481 |
| seuil_prediction | 0,520 | 0,505 |
| seuil_abandon | 0,520 | 0,505 |
| interaction | 0,533 | 0,457 |
| signe_negatif | 0,567 | 0,600 |
| mots_distincts | 0,502 | 0,495 |
| pourcentage_max | 0,482 | 0,586 |
| pourcentage_min | 0,569 | 0,586 |
| seuil_pair | 0,500 | 0,500 |
| rapport_abandon | 0,500 | 0,500 |
| rang_dossier | 0,523 | 0,533 |
| lignes_dossier | 0,500 | 0,500 |
| longueur_mots | 0,469 | 0,452 |
| vocabulaire : mot le plus séparateur (présent dans au moins 3 témoins et absent d'au moins 3) | « autres » 0,633 (70 mots) | « type » 0,633 (60 mots) |

**Contrôle de diagnosticité** (`controle_diagnosticite`, avant tout appel) : le plan v2 du juge A au tirage 1 (graphe, ordres,
identifiants, entrées servies, lecture des réponses, Bradley et Terry) est joué sur 20 graines fixes (`Graines(20261102000 + k)`)
par des juges scriptés qui ne lisent aucune table, en **deux batteries** soumises aux **mêmes règles** :
- **batterie figée** (66 juges) : les 25 juges du brouillon 3 (forme, a priori, gabarit, sens, longueur, chiffres,
  ampleur et seuils annoncés, interaction, signe, vocabulaire, plus haut pourcentage, ordre des identifiants, position, et leurs
  contraires et combinaisons) et, brouillon 4, les **traits de la contre-lecture v3** (rang de la caractéristique dans le dossier,
  lignes qui la nomment, rang relatif, pourcentages présents dans le dossier, nombres ronds, cohérence arithmétique, centre des taux,
  écart relatif, rapport seuil/écart, **rapport abandon/prédiction**, **longueur moyenne des mots**, longueur du nom, débuts de titre,
  longueur du titre, « tirés de la même façon », Wilson, mots des lois établies) et la parité du seuil, chacun dans les deux sens,
  et six combinaisons ; le juge « dossier sans tables » (la forme, plus les lois établies, le contexte et la cohérence interne) ;
- **batterie tenue à l'écart** (56 juges, `VARIANTES_TENUES_A_L_ECART`) : 26 traits écrits par le rédacteur
  **avant toute construction ou lecture des matériaux de ce texte** (virgules, « environ », place du premier chiffre, somme des
  pourcentages, unité du plus haut, mots du titre, longueurs de la prédiction, du test de mort et de la métrique, majuscules, mots
  longs, « niveau », mots du nom, dernière ligne et étendue des lignes qui le nomment, plus petit nombre, répétitions du nom, seuil
  sur plus bas taux, parités de l'écart et de l'abandon, « épisodes », nombres distincts, rapport hypothèse/prédiction, nom en
  « nombre », niveau haut « élevé », place du premier pourcentage), chacun dans les deux sens, et quatre combinaisons ; fichier
  scellé le 4 novembre 2026 à 02:27:55 UTC (sha256 `a1999ca5fb8d44aad90a7893257c1ce1e4c81d21ebb76f8c47018c6f2efbe122`), recopié à l'octet dans le cœur entre deux
  repères (essai `test_batterie_tenue_a_l_ecart_scellee`) ; joué **une seule fois** sur les matériaux de ce texte, sans retouche
  des matériaux avant ni après (rapport, section 3) ; aucun trait commun avec la batterie figée ;
- un **juge témoin**, « lecteur des tables », qui ne lit que le texte servi et relit les taux et l'écart que l'hypothèse attribue au
  dossier contre les lignes des tables (`verifier_par_les_tables`, tolérance 1,5 point).
Règles (gelées depuis le brouillon 3, inchangées) : chaque juge de surface, de l'une ou l'autre batterie, tient D1 dans au plus
2 courses sur 20 avec une aire moyenne au plus 0,62 (sauf « dossier sans tables » : rapporté, non borné), et D1b dans au plus 2
courses sur 20 avec une aire moyenne des bonnes lois contre les lois fausses au plus 0,62 ; le témoin tient D1b dans au moins 90 %
des courses — sinon refus.

**Sur les matériaux de ce texte : refusés (29 motifs) — B10 n'est pas levé.** Le lecteur des tables tient D1b
20 fois sur 20 (aire des lois fausses 0,991) ; le juge
« dossier sans tables » tient D1 19 fois sur 20 (aire 0,750) et D1b
0 fois. Les juges qui enfreignent les règles se rangent en deux groupes :

(a) **par l'aire** (aire moyenne au-dessus de 0,62 : un trait de surface sépare réellement ces matériaux) :

| batterie | juge | D1 sur 20 | aire moyenne | D1b sur 20 | aire des lois fausses |
|---|---|---|---|---|---|
| figée | « -ronds » | 1 | 0,614 | 14 | 0,758 |
| tenue à l'écart | « -virgules » | 6 | 0,673 | 2 | 0,579 |
| tenue à l'écart | « +parite_de_l_abandon » | 1 | 0,560 | 5 | 0,675 |
| tenue à l'écart | « -episodes » | 0 | 0,470 | 0 | 0,629 |
| tenue à l'écart | « +nombres_distincts » | 5 | 0,604 | 6 | 0,668 |
| tenue à l'écart | « +parite_de_l_ecart,+derniere_ligne » | 4 | 0,641 | 3 | 0,605 |

(b) **par le compte seul** (aires moyennes sous 0,62, D1 ou D1b tenu 3 à 6 fois sur 20) : le **juge de la pièce** — tous les juges
dont le trait est constant sur ces matériaux (par construction : rapport abandon/prédiction, lignes du dossier, parité du seuil,
Wilson, cohérence arithmétique, étendue des lignes ; 12 juges identiques, 10 de la batterie figée et
2 de la batterie tenue à l'écart, qui tirent au hasard chaque comparaison) :
D1 2, aire 0,522 ; D1b 3, aire 0,518 ; et :

| batterie | juge | D1 sur 20 | aire moyenne | D1b sur 20 | aire des lois fausses |
|---|---|---|---|---|---|
| figée | « -nombres_presents » | 2 | 0,513 | 4 | 0,539 |
| figée | « +centre_taux » | 0 | 0,511 | 4 | 0,615 |
| tenue à l'écart | « +somme_pourcentages » | 0 | 0,511 | 4 | 0,615 |
| tenue à l'écart | « +unite_du_plus_haut » | 2 | 0,554 | 3 | 0,620 |
| tenue à l'écart | « -majuscules » | 3 | 0,603 | 3 | 0,598 |
| tenue à l'écart | « +parite_de_l_ecart » | 3 | 0,615 | 0 | 0,559 |
| tenue à l'écart | « +place_du_premier_pourcent » | 3 | 0,584 | 3 | 0,606 |

**Le compte de la règle et le hasard (constat du brouillon 4).** Un juge qui tire chaque comparaison à pile ou face (pièce
indépendante, 200 courses par jeu) tient D1 dans 10 courses sur 200 et D1b dans 15 sur 200, sur les matériaux de ce texte comme sur
ceux du brouillon 3 : 5 à 7,5 % par course. La règle « au plus 2 courses sur 20 » est alors enfreinte par un juge **qui ne voit
rien** avec une probabilité d'environ 25 % (D1 ou D1b) ; avec une centaine de juges de traits presque nuls, elle l'est presque
sûrement par quelques-uns. Le compte sur 20 graines ne distingue donc pas un trait qui sépare d'un juge qui tire au hasard ; l'aire
moyenne, oui (le juge de la pièce est à 0,52). Ce constat ne change pas la règle (gelée) : il est porté au directeur (rapport,
section 8, décision 1). Les quatre traits de la contre-lecture v3 sont retirés : leurs juges ne dépassent ni le compte ni l'aire,
sauf ceux qui sont devenus le juge de la pièce (rapport abandon/prédiction, lignes du dossier).

| juge (batterie figée) | D1 sur 20 | aire moyenne | D1b sur 20 | aire des lois fausses |
|---|---|---|---|---|
| « +ratio_abandon » | 2 | 0,522 | 3 | 0,518 |
| « +rang_dossier » | 0 | 0,532 | 0 | 0,548 |
| « -rang_dossier » | 0 | 0,460 | 0 | 0,451 |
| « +rang_relatif » | 0 | 0,553 | 1 | 0,579 |
| « -rang_relatif » | 0 | 0,448 | 0 | 0,433 |
| « +lignes_dossier » | 2 | 0,522 | 3 | 0,518 |
| « -longueur_mots » | 0 | 0,544 | 0 | 0,537 |
| « +longueur_mots » | 0 | 0,461 | 0 | 0,471 |
| « seuil » | 1 | 0,536 | 0 | 0,532 |
| « ampleur » | 0 | 0,516 | 0 | 0,496 |
| « taux_haut » | 0 | 0,477 | 0 | 0,598 |
| « ordre » | 1 | 0,464 | 1 | 0,465 |
| « position » | 0 | 0,500 | 0 | 0,500 |

`verifier_materiaux` relit la vérité de chaque fiche sur les tables (chiffres affirmés, sens de la prédiction, champ « signe », table 3
pour les interactions fausses). Empreinte des matériaux : bloc `plan-gele` (`materiaux_sha256`, `14849fdbdd634ea3abaedf660de2b53f60e3c06458d468e39509d9ec2ba22219`) ; le lanceur les
reconstruit et refuse tout écart, puis joue les deux contrôles ; il **refuse ces matériaux-ci**. Gabarits écrits par un modèle de
la famille Claude : aucun juge de cette famille sur les témoins. **Limites** : les deux batteries ne couvrent que les traits qu'elles
nomment ; la batterie tenue à l'écart a été écrite par le rédacteur qui a ensuite accordé les matériaux à la batterie figée (pas
par un autre) ; les seuils du contrôle (2 courses sur 20, 0,62, 90 %) restent des choix du rédacteur du brouillon 3.

**Juges** (GO-2026-11-02-32, qui nomme les deux et exclut Kimi : trop cher et trop lent pour des comparaisons par paires, 5 appels
réussis sur 621 à A1, `registres/etat.md` du dépôt de travail, ligne 6, sha256 lu `f425a6842d3d711f419670517895f4a0c609b23b60d37873cdf4f31633f637cd`) :
A = Argon (`gemini-4-argon`, famille gemini, commande externe, relais 8805, à un seul fil) ; B = Astra (`gpt-6-astra`, famille gpt,
commande 8807). Chacun passe par sa commande de la configuration (`demonstrations/ideation_v8.adaptateurs_reels_v56`, commande
externe v56 avec modèle servi exigé) ; budget par appel = `plafonds_session.juge`, au moins deux fois le prix de plan le plus haut
(1,00 USD, refus sinon), et au moins le budget minimal accepté par chaque commande pour l'entrée la plus longue et deux fois le coût par appel le plus haut, tous deux relevés à l'épreuve (vérifié par la session qui prépare la configuration ; sinon chaque appel sort en code 4 ou dépasse son budget) ; modèle servi contrôlé à chaque appel (A2), y compris quand la commande v56 rend le statut « refus » pour un
autre modèle servi (section 8). **Épreuve de la commande Astra 8807** (elle n'a jamais servi ; elle est chez la machine qui porte les
clés : la fille neuve de session-depot, où Lazar a posé les clés Kimi et Astra, `registres/decisions.md` du dépôt de travail, R-1294 et R-1301 ; à faire avant le scellement par session-depot, et à recopier ici : nombre d'appels, modèle servi, coût et durée par appel,
codes de sortie vus et dernière ligne imprimée pour chacun (sur un code 5, la ligne dit-elle `modele_servi` et `refus` ?), identifiant exact du modèle servi, admis par `modele_conforme` ou par la liste explicite `modeles_servis_permis` de la configuration (un suffixe de date n'est admis que sous la forme `-AAAAMMJJ`), budget de session minimal accepté et pire cas réservé par appel pour l'entrée de comparaison la plus longue (9 057 caractères sur les matériaux de ce texte, brouillon 4) et pour l'entrée la plus longue de l'ancien protocole, réglages `--effort` et `--reflexion` d'Astra tels que la configuration les fixe ; et, pour Argon dans le rôle de juge, jamais mesuré sur une comparaison (A1 l'a mesuré en proposeur), deux ou trois appels sur l'entrée de comparaison la plus longue : coût, durée, sortie tronquée ou non sous `--max-sortie-court`, pire cas réservé ; Argon ne porte aucun réglage d'effort (défaut de l'interface : n° 294 de session-depot, sha256 `81e601fad368cbf06e8cce0ff30b79f97c5063f5bc263db042356e7bea2878c5`, section 4, TF-04) ; la dépense de l'épreuve est inscrite au registre des dépenses, sous le GO que le directeur désigne, hors du compteur de la course ; brouillon 3 (contre-lecture v2, B9 et I9) : pour chaque commande, la table des codes vérifiée sur l'adaptateur réel — code 3 au plancher (relais arrêté : connexion refusée), code 3 au pire cas réservé (une erreur de l'interface, si elle se présente ; sinon la ligne du code lue), code 4 au plancher (un refus du plafond propre du relais, provoqué en réglant `--plafond-usd` sous le pire cas d'un appel), code 3 au plancher sur un corps de plus de 4 000 000 octets (HTTP 413 : la ligne d'erreur dit-elle « HTTP 413 » ? si non, la forme exacte est recopiée et le motif `_REQUETE` du cœur doit la reconnaître, sinon nouveau texte) — sans appel au modèle pour les trois derniers ; le pire cas réservé d'Argon pour l'entrée de comparaison la plus longue de ce texte (9 057 caractères, environ 0,23 USD au barème prudent de la commande) mesuré). Relevé à faire avant le scellement et à recopier dans le bloc `releve-epreuve` ci-dessous, à la place de son marqueur
(section 13). Le bloc porte au moins trois clés que le lanceur lit (brouillon 4, contre-lecture v3, I11, I12, M17) :
`prix_comparaison_argon_usd` (coût moyen d'une comparaison d'Argon mesuré à l'épreuve), `ligne_erreur_413_argon` et
`ligne_erreur_413_astra` (ligne d'erreur d'un 413 provoqué, recopiée telle que la commande l'écrit sur sa sortie d'erreur) ; le
reste du relevé suit, en clair. **Le lanceur refuse** (mode réel, vérification seule comprise) un texte sans ce bloc, avec son
marqueur, sans ces clés, avec un prix d'Argon au-delà de `prix_epreuve_juge_a_max_usd` (0,074 USD, bloc `plan-gele`) ou avec une
ligne de 413 que le motif `_REQUETE` du cœur ne reconnaît pas dans ses 300 premiers caractères (ceux que l'adaptateur garde).
**Règle du prix (I12)** : 276 comparaisons d'Argon sont requises (section 12) ; au-delà de (24 − 6,89 / 2) / 276 = 0,0745 USD par
comparaison, la marge d'incidents de la part de 24 USD tombe sous la moitié de celle du devis (6,89 USD) ; aucune réduction du plan
n'est écrite d'avance : **arrêt avant toute course et nouveau texte** (ou un GO qui déplace les parts, rapport, section 8).

<!-- releve-epreuve : début -->
À REMPLIR (relevé de l'épreuve des commandes, section 13, point 2 ; le lanceur refuse le texte tant que ce marqueur reste)
<!-- releve-epreuve : fin -->

**Étapes** (fixées par le code, `etapes_v2` ; structure citée par le bloc `plan-gele`, valeurs fixes recopiées), dans l'ordre :

| phase | juge | protocole | fiches ou paires | appels | règle de projection (section 8) |
|---|---|---|---|---|---|
| décisive A | A | ancien avec dossier, tirage 1 | 30 témoins d'évaluation, une fiche par appel | 30 | toutes les étapes de la phase doivent tenir dans la part de A, sinon arrêt |
| décisive A | A | v2, tirage 1 | par lot, graphe 3-régulier tiré au hasard sur les 12 fiches (18 paires), **deux ordres** par paire | 108 | idem |
| décisive A | A | v2, tirage 2 | nouveau graphe, nouveaux ordres, nouveaux identifiants | 108 | idem |
| sans dossier (A) | A | ancien **sans dossier** | les 30 témoins d'évaluation, entrée de la forme du second tour (consigne figée puis fiche) ; **juste après la phase décisive de A** (brouillon 3, I7) | 30 | toute la phase doit tenir, sinon non jouée |
| décisive B | B | v2, tirage 1 | paires **mélangées** (une bonne, une mauvaise) du graphe du tirage 1 de A, au plus 13 par lot, un ordre tiré indépendamment de ceux de A | 24 à 36 sur 60 graines simulées ; 32 à la graine 20261102 ; au plus 39 | étape par étape (les comparaisons de B passent avant son ancien protocole) |
| décisive B | B | ancien avec dossier, tirage 1 | 30 témoins d'évaluation | 30 | étape par étape |
| réel (descriptif) | B ; A | ancien | fiches réelles où le juge est admis (règle de famille), sans dossier | ≤ 13 ; ≤ 13 | idem |
| réel (descriptif) | B ; A | v2 | un cycle sur ces fiches, un ordre | ≤ 13 ; ≤ 13 | idem |

Le juge B ne voit que des paires mélangées : son rôle est de **départager lui aussi** ce qui départage, et son budget ne couvre pas
tout le graphe ; ce choix de paires par les étiquettes connues n'existe qu'en validation (en production, les paires ne se
choisissent pas sur la qualité ; déclaré). Les ancres sont servies à l'aveugle comme les autres fiches.

**Lot réel.** Les 12 fiches du second tour, privées, tenues par la session qui détient les clés, sont une pièce de la
configuration (`piece_lot_reel`), avec la question de la course (`piece_question`), servie comme dossier du v2 ; elles ne sont lues
que descriptivement (aucun seuil, aucune issue) ; les fusions comptent les familles de leurs parents (toutes, si elles ne sont pas
dites) ; un identifiant de la forme des témoins (« monde-k-nn ») est refusé. Elles passent la garde A4 de la configuration avant
tout appel ; sinon refus.

**Protocole v2, pour chaque comparaison** : consigne figée v2 (`CONSIGNE_PAIRE_V2`, empreinte au bloc `plan-gele`, inchangée depuis
le brouillon 1), dossier, deux fiches anonymes « présentée en premier » et « présentée en second ». Réponse : `{"comparaison":
{preferee, critere, citation_fiche, citation_dossier}}` ; valide seulement si l'identifiant est l'un des deux, le critère dans la
liste (vérité, nouveauté, contenu, prédiction), la citation de la fiche trouvée telle quelle (après normalisation typographique)
dans la fiche **choisie** et **absente de l'autre**, de 15 à 300 caractères, et, quand le dossier a des lignes de faits, la
citation du dossier trouvée telle quelle (10 à 300 caractères). Une comparaison nulle est comptée, jamais lue comme victoire.

**Note continue** : force de Bradley et Terry avec effet de position (`ajuster_bt` : P(première gagne) = σ(θ₁ − θ₂ + γ),
crêtes 0,5 et 0,5, forces centrées, arrondies à 10⁻⁹), ajustée par lot sur les comparaisons valides d'un juge et d'un tirage.
**Verdict** (`verdicts_lot`) : « notable » = parmi les ⌈0,25 × 10⌉ = 3 premières fiches d'évaluation du lot **et**
strictement au-dessus du milieu des forces des deux ancres ; ancres inversées → aucun notable dans le lot ; égalité à la limite
du budget → aucune des fiches à égalité. **Ancien protocole** : `juges_croises_v53.lire_verdict` (items de la configuration,
« notable » = tous vrais), note continue = part d'items vrais.

**Graines (R9).** `graines_v53.Graines(entropie)` : `SeedSequence(entropie, spawn_key=(cle_de_tache(tâche),))`, entropie =
`int(SHA-256 du texte scellé, 16)` ; tâches : `graphe|<lot>|tirage-<t>`, `ordres|<lot>|tirage-<t>|<juge>`, `paires-b|<lot>`,
`ordre-ancien|<lot>|<juge>|tirage-<t>`, `ordre-ancien-sans-dossier|<lot>|<juge>`, `anonymisation|<juge>|tirage-<t>|<lot>|<fiche>`,
`anonymisation-sans-dossier|<juge>|<lot>|<fiche>`, `graphe|reel|<juge>`, `ordres|reel|<juge>` ; matériaux : `Graines(20261102)`,
tâches `materiaux|<monde>|tentative-<k>` et `materiaux|<monde>|fiche-<k>` ; contrôle de diagnosticité : `Graines(20261102000 + k)`,
k = 0…19 (propriété des matériaux, fixée). Tout est écrit au manifeste de la course.

**Lancement** (après scellement, épreuve d'Astra et configuration) :
`python3 -I -B demonstrations/validation_juges_idees_v2.py SORTIE_NEUVE --preenregistrement prereg/preenregistrement-juges-idees-v2-vN.md --configuration CONF --moteur reel --confirmer-moteur-reel --registre-go registres/go.md --go GO-2026-11-02-32`
(d'abord avec `--verifier-seulement` : toutes les gardes, contrôles des matériaux, plafonds accusés, aucun appel, aucune écriture
dans la sortie).

<!-- plan-gele : début -->
```
juge_a: etiquette=juge-a, fournisseur=argon, modele=gemini-4-argon, famille=gemini, prix_usd=0.062, secondes=8-40
juge_b: etiquette=juge-b, fournisseur=astra, modele=gpt-6-astra, famille=gpt, prix_usd=0.5, secondes=10-120
correspondance_auteurs: kimi=kimi, argon=gemini
graine_materiaux: 20261102
materiaux_sha256: 14849fdbdd634ea3abaedf660de2b53f60e3c06458d468e39509d9ec2ba22219
consigne_paire_sha256: 6978f0a4778edd87f9059606420577c167a1ff8db2053ab56507d20a355039b4
piece_consigne_ancienne: consigne_juge
piece_question: question_course_2
piece_lot_reel: lot_reel_juges_idees_v2
plafond_usd: 60
plafond_juge_a_usd: 24
plafond_juge_b_usd: 36
duree_max_h: 48
configuration_sha256: (relevée avant le scellement, section 13 ; le lanceur refuse toute valeur qui n'est pas une empreinte)
go: GO-2026-11-02-32
version_plan: validation-juges-idees-v2-plan-4
jeu_de_mondes: mondes-v4
temoins_par_classe: 15
degre: 3
tirages_a: 2
degre_reel: 2
paires_b_max_par_lot: 13
part_budget: 0.25
ridge_forces: 0.5
ridge_position: 0.5
seuils: alpha=0.05, alpha_reproduction=0.1, plafond_ancien_min=0.8, delta_aire_min=0.15, biais_premier_max=0.15, validite_min=0.85, presents_ancien_min=27, pertes_max_part=0.15, paires_b_min=20
politique_relais: code3=attente 15,30,60,120,300,600,1200,1800 s sans limite de nombre; delai_code6=comme code3, hors des echecs couteux de suite; code4=arret refus_de_budget; requete_400_403_411_413=arret; panne_hors_decisives_h=6; panne_decisives=aucune (garde 48 h); echec_couteux=perte, attente 30,60,120,300 s, reprises_max=2, echecs_couteux_max=5; pertes_max_part=0.15; cout_plancher_usd=1e-05
prix_epreuve_juge_a_max_usd: 0.074
```
<!-- plan-gele : fin -->

`consigne_paire_sha256` est l'empreinte de la consigne v2 (inchangée depuis le brouillon 1) ; `materiaux_sha256` est l'empreinte des
matériaux de ce brouillon (jeu « mondes-v4 », refusés par le contrôle de diagnosticité : B10) ; `prix_epreuve_juge_a_max_usd` est le prix
maximal d'une comparaison d'Argon mesuré à l'épreuve (I12, section 4) ; si la contre-lecture fait changer les matériaux ou la consigne, elles changent, et le
lanceur refuse l'écart (à recalculer au scellement, avec le bloc de la section 11). `configuration_sha256` n'est pas une empreinte tant
que la configuration n'existe pas : le lanceur refuse le texte (« 64 caractères hexadécimaux »). Plafond : exactement 60 USD
(GO-2026-11-02-32) ; parts : 24 USD pour Argon, 36 USD pour Astra, au large du pire cas requis du plan (section 12). `duree_max_h` est une
garde contre une boucle folle, jamais une coupe de la mesure (règle prise sur les mots de Lazar du 2 novembre 2026, 18:26 UTC,
`registres/decisions.md`, R-1276, ligne 1240) : 48 heures, huit fois la durée haute du devis ; c'est aussi, dans les phases décisives,
la seule borne d'une attente sur le relais (section 8). `politique_relais` gèle les valeurs de la section 8. Les noms de pièces
(`consigne_juge`, `question_course_2`, `lot_reel_juges_idees_v2`) sont ceux que la configuration devra porter ; la configuration est
préparée par la session qui tient les clés.

## 5. Métriques, taille et puissance

**Métriques** (`mesurer`, depuis le seul journal) : aire et test de Mann et Whitney unilatéral (loi exacte sans égalité,
approximation normale corrigée sinon) par protocole, par juge et par tirage ; aire des bonnes lois contre les lois fausses (D1b) ;
différence appariée des aires v2 − ancien (DeLong, unilatéral ; variance nulle → p = 0 si la différence est positive, dit) ; bras
sans dossier (A) : part de notables, aire et Mann et Whitney, effet du dossier sur l'ancien (part de notables et aire, avec dossier
moins sans dossier ; DeLong bilatéral, descriptif) et gain total (aire v2 moins aire de l'ancien sans dossier ; DeLong unilatéral, descriptif) ; part de
notables, faux notables (mauvais témoins notables), vrais notables ; kappa de Cohen sur les verdicts de l'ancien (convention v54 :
non défini si l'accord attendu vaut 1) ; **exactitude du juge B** sur ses paires mélangées (part des comparaisons valides où il
choisit la bonne fiche, test binomial unilatéral exact) ; kappa des choix par paire entre A et B sur ces paires (chaque jugement de
A, un par ordre, en regard du jugement de B ; issue orientée par l'empreinte de l'identifiant, sans lien avec la classe ; le juge B
ne voyant que des paires mélangées, il n'existe aucun kappa « sur les paires de même qualité ») ; fidélité test-retest (aire du
tirage 2 ; Spearman entre forces des deux tirages, avec son plafond binaire 0,751) ; biais de position (part des
victoires de la première présentée sur les deux tirages de A, taux de bascule compté par tirage et par paire, effet γ par lot) ;
part des comparaisons valides et motifs ; rang centile moyen par classe ; complétude (appels prévus, répondus, perdus
définitivement, non joués, par phase et par juge) ; pertes, attentes et dépense du relais par juge (coûts connus, inconnus,
incidents).

**Taille.** 30 témoins d'évaluation (15 bons, 15 mauvais : GO-2026-11-02-32) dont 7 lois fausses ; 6 ancres. **Puissance**
(modèle binormal : mauvais ~ N(0, 1), bons ~ N(√2·Φ⁻¹(aire), 1) ; test de Mann et Whitney unilatéral, loi exacte ; 20 000
répétitions par case, graine 20261102 ; reproduire :
`python3 -I -B demonstrations/validation_juges_idees_v2.py --puissance --graine 20261102 --repetitions 20000 --graines-plan 60`,
sortie gardée hors dépôt, empreinte au rapport) :

**D1** (Mann et Whitney unilatéral exact au niveau 0,05 ; puissance = part des répétitions où D1 est tenu) :

| bons contre mauvais | U critique (aire critique) | niveau exact | aire 0,50 | aire 0,65 | aire 0,70 | aire 0,75 | aire 0,80 | aire 0,85 | aire 0,90 |
|---|---|---|---|---|---|---|---|---|---|
| 10 contre 10 | 73 (0,730) | 0,0446 | 0,045 | 0,284 | 0,440 | 0,611 | 0,782 | 0,910 | 0,979 |
| 12 contre 12 | 102 (0,708) | 0,0444 | 0,044 | 0,329 | 0,501 | 0,689 | 0,854 | 0,951 | 0,992 |
| 14 contre 14 | 135 (0,689) | 0,0469 | 0,049 | 0,380 | 0,571 | 0,757 | 0,900 | 0,976 | 0,998 |
| 15 contre 15 | 153 (0,680) | 0,0488 | 0,053 | 0,410 | 0,611 | 0,791 | 0,927 | 0,985 | 0,999 |
| 16 contre 16 | 173 (0,676) | 0,0469 | 0,050 | 0,417 | 0,628 | 0,815 | 0,938 | 0,988 | 1,000 |
| 18 contre 18 | 215 (0,664) | 0,0485 | 0,050 | 0,459 | 0,683 | 0,856 | 0,960 | 0,994 | 1,000 |
| 20 contre 20 | 262 (0,655) | 0,0482 | 0,047 | 0,500 | 0,723 | 0,888 | 0,973 | 0,997 | 1,000 |

**D4** (tirage 2, niveau 0,10) **et D1 avec D4** (tirages indépendants de même aire vraie), à 15 contre 15 :

| à 15 contre 15 | aire 0,50 | aire 0,65 | aire 0,70 | aire 0,75 | aire 0,80 | aire 0,85 | aire 0,90 |
|---|---|---|---|---|---|---|---|
| D4 (U ≥ 145, aire ≥ 0,644, niveau exact 0,0936) | 0,094 | 0,544 | 0,736 | 0,880 | 0,964 | 0,994 | 1,000 |
| D1 et D4 | 0,004 | 0,223 | 0,448 | 0,697 | 0,894 | 0,979 | 0,998 |

**D1b** (15 bonnes lois contre 7 lois fausses ; U ≥ 77 sur 105, aire ≥ 0,733, niveau exact 0,0455) :

| aire 0,50 | aire 0,70 | aire 0,75 | aire 0,80 | aire 0,85 | aire 0,90 |
|---|---|---|---|---|---|
| 0,046 | 0,426 | 0,602 | 0,771 | 0,900 | 0,975 |

**D6** (exactitude du juge B, test binomial unilatéral exact au niveau 0,10 ; puissance exacte, sans simulation) :

| comparaisons valides de B | k critique | niveau exact | p = 0,65 | p = 0,70 | p = 0,75 | p = 0,80 | p = 0,85 | p = 0,90 |
|---|---|---|---|---|---|---|---|---|
| 20 | 14 | 0,0577 | 0,417 | 0,608 | 0,786 | 0,913 | 0,978 | 0,998 |
| 24 | 16 | 0,0758 | 0,526 | 0,725 | 0,879 | 0,964 | 0,994 | 1,000 |
| 28 | 18 | 0,0925 | 0,616 | 0,809 | 0,932 | 0,985 | 0,998 | 1,000 |
| 32 | 21 | 0,0551 | 0,551 | 0,772 | 0,920 | 0,983 | 0,998 | 1,000 |
| 36 | 23 | 0,0662 | 0,629 | 0,837 | 0,954 | 0,993 | 1,000 | 1,000 |
| 39 | 24 | 0,0998 | 0,736 | 0,906 | 0,980 | 0,998 | 1,000 | 1,000 |

**Le plan joué par des juges scriptés** (« bruite », sans biais de position, juste avec la probabilité donnée sur une paire de
qualités différentes et au hasard sur une paire de même qualité ; ancien protocole indulgent ; même juge A et B ; 60 graines de
course par ligne ; même commande ; **recalculé pour ce brouillon 4** sur les matériaux « mondes-v4 » et la politique du relais de la
section 8) — c'est la puissance du **plan** (graphe 3-régulier, deux ordres, ancres, tirage 2, paires mélangées de B), pas celle d'un
juge réel, dont l'exactitude par comparaison est inconnue :

| exactitude par comparaison | issues (sur 60) | D1 | D4 | D5 | D6 | D1b | aire v2 moyenne (décile bas) | exactitude de B moyenne | paires de B (min ; moyenne ; max) |
|---|---|---|---|---|---|---|---|---|---|
| 0,60 | I1 3, I3 44, I4 13 | 0,267 | 0,433 | 1,000 | 0,350 | 0,267 | 0,637 (0,556) | 0,591 | 24 ; 29,8 ; 36 |
| 0,65 | I1 17, I3 19, I4 24 | 0,683 | 0,750 | 1,000 | 0,583 | 0,483 | 0,717 (0,600) | 0,645 | 24 ; 29,8 ; 36 |
| 0,70 | I1 33, I3 10, I4 17 | 0,833 | 0,917 | 1,000 | 0,767 | 0,717 | 0,778 (0,653) | 0,698 | 24 ; 29,8 ; 36 |
| 0,75 | I1 46, I3 4, I4 10 | 0,933 | 0,967 | 1,000 | 0,867 | 0,850 | 0,828 (0,720) | 0,742 | 24 ; 29,8 ; 36 |
| 0,80 | I1 57, I3 1, I4 2 | 0,983 | 1,000 | 1,000 | 0,967 | 0,900 | 0,873 (0,804) | 0,797 | 24 ; 29,8 ; 36 |
| 0,85 | I1 60 | 1,000 | 1,000 | 1,000 | 1,000 | 0,967 | 0,908 (0,840) | 0,843 | 24 ; 29,8 ; 36 |
| 0,95 | I1 60 | 1,000 | 1,000 | 1,000 | 1,000 | 1,000 | 0,974 (0,942) | 0,944 | 24 ; 29,8 ; 36 |

Lecture. À 15 contre 15, D1 seul a une puissance de 0,927 à une aire vraie de 0,8 (0,924 sur 200 000 répétitions, recalcul de la contre-lecture v2 ; l'écart est du bruit de simulation) (au moins 0,9, comme le demande GO-2026-11-02-32 ; 0,782 à 10 contre 10) et de 0,985 à 0,85 ; D1 avec D4, 0,894 à 0,8 (juste sous 0,9) et 0,979 à 0,85 (tables analytiques inchangées depuis le brouillon 2, recalculées à l'identique). Le plan joué conclut I1 dans 46 courses sur 60 quand le juge est juste à 0,75 par comparaison (aire v2 moyenne 0,828), 57 sur 60 à 0,80, 60 sur 60 à 0,85 (brouillon 3, sur ses matériaux : 56, 58 et 60 sur 60) ; à 0,60, I1 dans 3 courses sur 60. La variance du plan creux (graphe 3-régulier, ancres, deux ordres) s'ajoute à celle de l'échantillon de témoins : le décile bas de l'aire v2 est à 0,720 quand la moyenne vaut 0,828 (à 0,75). D6 est mesurable dans toutes les courses simulées (24 à 36 paires mélangées pour B, au moins 20 exigées) ; D5 est tenu partout (juges sans biais de position). D1b, à 15 contre 7, est moins puissant (0,771 à une aire de 0,8 ; tenu dans 51 courses sur 60 à 0,75 par comparaison) : un T0 ne prouve pas que les tables ne sont pas lues. Sortie : `puissance-b4.json` du rédacteur, hors dépôt, sha256 `87226dc64d3b1cb7b65bba83afccee13f61309d074327fd2e3bee92ba7e37569`.

## 6. Critères de lecture gelés et issues écrites d'avance

Calculés par `lire_validation` sur les mesures, sans autre lecture. Juge A, témoins d'évaluation, sauf mention.

| critère | définition | seuil |
|---|---|---|
| D1 | aire v2, tirage 1 : Mann et Whitney unilatéral exact | p < 0,05 (à 15 contre 15 sans égalité : U ≥ 153 sur 225, aire ≥ 0,68) |
| D2 | part de notables de l'ancien avec dossier, tirage 1 (« l'ancien sature ») | ≥ 0,80 |
| D3 | aire v2 − aire ancien (tirage 1), DeLong unilatéral | ≥ 0,15 et p < 0,05 |
| D4 | la discrimination se reproduit au tirage 2 : Mann et Whitney unilatéral exact | p < 0,10 (reproduction d'un effet que D1 a établi ; aire ≥ 0,644 à 15 contre 15) |
| D5 | biais de position : écart de la part des victoires de la première présentée à 0,5 (deux tirages) | ≤ 0,15 (au plus 30 % des comparaisons tranchées par la position) |
| D6 | juge B : exactitude sur ses paires mélangées, test binomial unilatéral exact contre 0,5 | p < 0,10 ; « non mesuré » sous 20 comparaisons valides de B ou sous 0,85 de validité |
| D7 | part de notables de l'ancien **sans dossier** (bras sans dossier : « l'ancien sature dans les conditions du second tour ») | ≥ 0,80 ; « non mesuré » si le bras rend moins de 27 verdicts lisibles sur 30 |
| D1b | aire v2 des 15 bonnes lois contre les 7 lois fausses (tirage 1) : Mann et Whitney unilatéral exact | p < 0,05 (qualificatif : lecture des tables) |

**Validité de l'instrument** (sinon I0) : phase décisive de A allée à son terme (chaque appel prévu répondu ou perdu
définitivement selon la règle de la section 8) ; au plus 15 % de ses appels prévus perdus définitivement par le relais (jamais
comptés comme réponses du juge), sinon I0 « infrastructure » ; part des comparaisons valides de A ≥ 0,85 à chaque tirage (sur les
réponses ; les pertes n'y entrent pas) ; au moins 27 verdicts lisibles de l'ancien avec dossier sur 30 (une perte définitive de l'un de ces 30 appels y compte comme un verdict manquant : au-delà de trois, c'est I0, même sous la règle des 15 %). **Course tuée** (règle écrite d'avance, brouillon 3, contre-lecture v2, I8) : le journal est écrit au fil de l'eau (`journal-au-fil-juges-idees-v2.jsonl` de la sortie, une ligne JSON vidée et synchronisée sur disque par réponse, perte, attente, étape, projection, arrêt de juge et phase ; scellé à la fin, que la course aille à son terme ou s'arrête) ; un signal de fin ou une interruption de l'orchestrateur est un arrêt de la course comme les autres (`ArretInterruption` : journal partiel, mesures et lecture « partielle » scellés) ; un processus tué sans rien sceller (machine redémarrée, conteneur repris) donne **I0 « infrastructure »** : le journal au fil de l'eau est la seule trace, scellé tel quel par le lecteur, la dépense est relue au registre des commandes de la sortie, et aucune relance n'a lieu sans GO de Lazar (une relance est une course nouvelle, sur un texte nouveau, comme la seconde course d'A1-v3, GO-2026-11-03-01).

**Issues, dans cet ordre :**
- **I0 — non jugeable** : la validité ne tient pas (ou arrêt de la course dans la phase décisive de A). Aucune conclusion sur les
  protocoles ; suite : diagnostic de l'instrument (relais, consigne, citations), nouveau texte. Un arrêt de la course **après** la phase décisive de A (A2 d'un juge, plafond, garde de durée, étiquette interdite) n'est pas I0 par lui-même : l'issue est lue par `lire_validation` sur le journal partiel scellé ; la cause de l'arrêt (champ « arret » de la lecture) et les étapes non jouées (`etapes_non_jouees` des mesures) sont dites avec l'issue.
- **I3 — le v2 ne fait pas mieux au seuil gelé** : D1 non tenu (à 15 contre 15, une aire vraie de 0,8 laisse D1 non tenu dans 7 % des tirages, une aire de 0,9 dans 0,1 % : I3 exclut une aire vraie de 0,9, pas une aire de 0,8 ; section 5). I3a si D2 tenu (les deux protocoles échouent :
  l'outil n'est pas la bonne réponse ou les juges ne lisent pas le dossier) ; I3b sinon (l'ancien n'est même pas au plafond). Suite :
  ne pas adopter le v2 ; examiner les réponses brutes (critère, citations) avant toute retouche.
- **I4 — le v2 discrimine mais n'est pas fiable** : D1 tenu et l'un de D4, D5, D6 (mesuré) non tenu ; les critères manquants sont
  nommés. Suite : pas d'adoption en l'état ; plus de comparaisons ou autre juge, sur nouveau texte.
- **I1 — le v2 discrimine là où l'ancien sature** : D1, D4, D5, D6 (ou non mesuré) tenus et D2 tenu ; I1a si D3 tenu (gain mesuré
  sur l'ancien), I1b sinon. Suite : proposer à Lazar l'adoption du v2 pour le prochain tour (nœud : modification de l'instrument),
  avec les réserves de la section 10.
- **I2 — le v2 discrimine, l'ancien ne sature pas ici** : comme I1 mais D2 non tenu ; I2a / I2b selon D3. Suite : la lecture du
  bras sans dossier dit quelle branche de H0(b) tient (S1 : l'information manquait ; S3 : les témoins ne reproduisent pas le
  plafond du second tour) ; aucune conclusion sur les fiches réelles.

**Lecture du bras sans dossier** (gelée ; jointe à l'issue, ne la change jamais) : S0 « non mesuré » si D7 n'est pas mesuré ;
S1 « le dossier lève le plafond de l'ancien » si D7 est tenu et D2 non tenu ; S2 « l'ancien sature avec et sans dossier » si D7
et D2 sont tenus ; S3 « l'ancien ne sature pas même sans dossier » si D7 n'est pas tenu (avec D2 tenu, l'incohérence est dite en
réserve). Descriptifs joints : effet du dossier sur l'ancien et gain total (section 5).

**Lecture des tables** (gelée ; jointe, ne change jamais l'issue) : T1 si D1b est tenu (« lecture des tables établie ») ; T0 s'il ne
l'est pas ; T- s'il n'est pas mesurable ou si l'issue est I0. T1 ne se lit comme une lecture des tables que sur des matériaux que le
contrôle de diagnosticité admet ; ceux de ce brouillon ne le sont pas (des juges scriptés qui ne lisent pas les tables y gagnent
encore, section 4 : B10) : aucune course n'a lieu sur eux. Un I1 ou un I2 avec T0 dit que la discrimination vient
des classes lisibles sans les tables (redites, définition, texte long, signe contraire), pas de la vérification des nombres.

**Réserves écrites d'avance** : D6 non mesuré → « accord du juge B non mesuré » joint à I1, I2, I4 ; tout juge arrêté (panne, part,
refus de budget ou de requête, réponses inexploitables) → nommé, avec la phase et ce qui n'a pas été joué ; part du premier entre 0,10 et 0,15 d'écart à 0,5 →
« préférence de position modérée, absorbée par les deux ordres » ; S3 avec D2 tenu → incohérence dite.

## 7. Audit de symétrie (R4), écrit d'avance

Déclencheurs (`audit_symetrie`), symétriques : aire v2 ≥ 0,98 ou ≤ 0,55 ; Spearman ≥ 0,98 ou ≤ 0,30 ; kappa des paires ≥ 0,90
ou ≤ 0 ; exactitude de B ≥ 0,98 ou ≤ 0,55 ; part de notables de l'ancien = 1 ou ≤ 0,20 ; aucune bascule sur au moins 30 paires vues
dans les deux ordres, ou bascule ≥ 0,75 ; et, pour l'instrument, plus de 5 % de pertes définitives dans une phase, ou un juge
arrêté. Un déclencheur, quel que soit son sens, impose **la même liste** de vérifications, faite par un lecteur neuf avant que
l'issue ne soit lue : recalcul indépendant depuis le journal scellé ; six réponses brutes tirées au hasard par juge et par
protocole ; garde A4 rejouée sur chaque entrée (aucune étiquette de classe, de rôle, d'auteur) ; modèle servi conforme à chaque
appel et appels répondus et pertes égaux au plan, cause par cause ; empreinte des matériaux et contrôles de forme et de
diagnosticité rejoués ; ordres de présentation conformes ; résultat par classe (un résultat porté par une seule classe, par
exemple les textes longs, est dit) ; pertes et attentes du relais relues (aucune perte lue comme une réponse ; reprises dans la
borne). L'issue n'est pas changée par l'audit ; ses constats sont des réserves.

## 8. Liste d'arrêt et règles du relais (chaque garde essayée sur un cas sain et un artefact, R5 ; essais nommés au rapport)

- **Avant tout appel et toute écriture (code 2)** : texte hors du dossier `prereg/` ou d'un autre nom, brouillon, non scellé, à
  marqueur, code ≠ code gelé, fermeture incomplète ; plan non conforme (clés, valeurs fixes dont la politique du relais, consigne v2
  ≠ code, plafond > 60 USD — le GO exige ensuite le montant exact —, parts non positives ou hors du plafond, durée maximale nulle
  ou négative, juges d'une même étiquette, famille ou relais, juge de la famille des gabarits) ; graine ou option de plan en ligne de
  commande ; configuration d'une autre empreinte ; GO autre, absent, d'un autre montant, d'un autre type, échu ou révoqué ; variable
  de clé dans l'environnement ; budget par appel sous deux fois le prix de plan le plus haut ; matériaux d'une autre empreinte, vérité
  connue non établie, forme qui sépare les classes (quatorze indices et le vocabulaire, sur les témoins d'évaluation et sur le
  sous-ensemble de D1b), classement possible sans les tables (diagnosticité : un juge de surface tient D1 ou D1b, ou le lecteur des
  tables ne tient pas D1b), étiquette
  interdite ; pièce absente ou altérée ; lot réel qui ne passe pas la garde A4 ; consigne figée de l'ancien juge refusée par la garde
  A4 des témoins ; relais absent ; dépense requise (phases décisives et bras sans dossier, au prix du plan) au-dessus de la part d'un
  juge ou du plafond ; durée haute du devis au-dessus de 48 heures ; porte de plafond qui n'accuse pas sa part.
- **Statuts du relais, jamais lus comme une réponse du juge** (`classer_resultat`, `appeler`), selon la table des codes de la commande
  Argon réelle (`commande_argon_v56_nuit_v2.py`, relais 8805 ; n° 294 de session-depot, § 3, sha256
  `81e601fad368cbf06e8cce0ff30b79f97c5063f5bc263db042356e7bea2878c5`, et n° 287, `registres/decisions.md`, R-1277) — le relais ne reprend
  rien (une seule tentative) ; la commande Astra a la même table (adaptateur `pole/adaptateurs.py`, l. 721-775 : tout code non nul est
  rendu « erreur », le code lu dans le motif ; l'épreuve la vérifie, section 4). **Une panne du relais n'est jamais une issue : attente
  puis reprise, journal écrit sur disque à chaque pas.**
  - modèle servi absent ou différent sur une réponse « ok », ou statut « refus » que la commande v56 rend pour un autre modèle servi
    (événements `commande.modele_servi`, `commande.modele_servi_absent`, `commande.modele_demande_inconnu`) : **arrêt de la course
    au premier appel** (A2 : aucune bascule sans mot de Lazar) ; un identifiant servi que la configuration admet par sa liste explicite
    `modeles_servis_permis` (par exemple daté à tirets) est admis par le cœur comme par l'adaptateur (brouillon 3, I7) ;
  - refus du modèle lui-même (`commande.refus`) : réponse du juge, **inexploitable** (comparaison nulle ou verdict illisible), jamais
    une victoire, jamais reprise ;
  - **code 3 à coût connu** — au plancher (relais injoignable, rien parti) **comme au pire cas réservé** (toute erreur de l'interface,
    quota de Google compris, `envoye=true`) : **passager** ; le même appel est attendu puis repris (15, 30, 60, 120, 300, 600, 1 200 puis
    1 800 s entre deux tentatives), **sans limite de nombre et sans compte d'échecs de suite** ; le pire cas déclaré est compté dans la
    dépense (jamais dans le prix observé), borné par la part du juge et le plafond ; chaque attente est une ligne du journal ;
  - **code 4** (plafond propre du relais, HTTP 402 ; nombre d'appels du relais, HTTP 429 ; pire cas au-dessus du budget par appel ;
    registre) : **jamais passager** → arrêt nommé « refus de budget » au premier appel, sans attente ; si le budget de l'appel était déjà
    borné par le reste de la part (ou du plafond), c'est la part (ou le plafond) qui est atteinte ; prévenu par les relevés d'avant la
    course (section 13) ;
  - **code 3 au plancher portant HTTP 400, 403, 411 ou 413** (refus de requête du relais, déterministe pour cette entrée ; brouillon 4,
    M17 : « HTTP » suivi, à au plus 16 caractères, de l'un de ces codes, « HTTP 413 », « HTTP Error 413 », « HTTP/1.1 413 » ; l'épreuve
    recopie la ligne réelle, que le lanceur confronte au motif) : arrêt nommé
    « refus de requête » au premier appel, sans attente (aucune entrée de ce plan n'approche les 4 000 000 octets du relais) ;
  - **délai** (code 6 de la commande, ou délai de 1 800 s de l'adaptateur ; brouillon 4, contre-lecture v3, I10) : **passager**, comme
    un code 3 — le même appel est attendu puis repris (mêmes attentes), son coût (déclaré, ou budget de l'appel compté s'il est
    inconnu) entre dans la dépense, jamais dans le prix observé, borné par la part du juge et le plafond (un délai à coût inconnu
    compte au moins 1,00 USD : la part arrête la série, jamais une boucle sans dépense) ; **jamais compté dans les cinq échecs
    coûteux de suite** ;
  - **échec coûteux** (code 3 sans dernière ligne, code 5 réponse non conforme ou prompt bloqué,
    commande muette au plafond de session compté, appel facturé au-dessus du plafond de session, code 2, tout autre échec) : l'appel est
    **perdu**, son coût compté (jamais dans le prix observé), une attente suit (30, 60, 120 puis 300 s : relais à un fil), puis il est
    **repris en fin d'étape** (même entrée, mêmes identifiants), au plus deux fois ; au-delà, **perte définitive** ; cinq échecs coûteux de
    suite d'un juge : juge **en panne** ;
  - **horloge de panne** (brouillon 3, I6) : elle part du **premier échec de la série en cours** et revient à zéro sur une réponse,
    et, brouillon 4 (M18), au début de chaque phase (avec le compte des échecs coûteux de suite : une série ouverte dans une phase
    décisive ne se prolonge pas dans la suivante) ;
    **hors des phases décisives** (bras sans dossier, phases du lot réel), 6 heures sans réponse depuis ce premier échec : juge en panne ;
    **dans les phases décisives (A et B), aucune panne par la durée** : seule la garde de 48 heures de la course (boucle folle) borne
    l'attente ;
  - **règle écrite d'avance pour les comparaisons perdues** : une perte définitive manque au journal des réponses, comme une
    comparaison nulle elle n'entre pas dans l'ajustement de Bradley et Terry ; elle est comptée à part (complétude, pertes par
    cause) ; au-delà de 15 % des appels prévus de la phase décisive de A, arrêt de la course et I0 « infrastructure ».
- **Pendant la course (code 3 ; journal, mesures et lecture « partielle » scellés, journal au fil de l'eau scellé)** : plafond de dépense
  de 60 USD (aucun appel dont le budget ne tient plus dans le reste) ; durée de 48 heures (garde contre une boucle folle) ; A2 ;
  étiquette interdite dans une entrée ; interruption de l'orchestrateur (SIGTERM, SIGHUP — brouillon 4, M19 —, clavier ; l'appel en
  vol est compté au bilan à son budget, coût inconnu) ; et, **dans la phase décisive de A
  seulement**, tout arrêt de A : projection de la phase au-delà de la part de A (au prix observé : moyenne des réponses à coût connu dès
  trois réponses, prix du plan avant), part de A atteinte, refus de budget ou de requête, A en panne (cinq échecs coûteux de suite),
  pertes définitives au-delà de 15 %, plus de la moitié de réponses inexploitables sur les 20 dernières.
- **Arrêt d'un juge seulement (jamais de la course, consigné, réserve)** hors de la phase décisive de A : juge en panne, part atteinte,
  refus de budget ou de requête → ses étapes suivantes ne sont pas jouées, celles de l'autre juge continuent ; plus de la moitié de
  réponses inexploitables sur les 20 dernières → ses étapes restantes de la phase ne sont pas jouées. Projection avant chaque étape :
  phase de B étape par étape (une étape qui ne tient pas dans la part de B n'est pas jouée, la suivante est examinée) ; bras sans dossier
  et phases descriptives : toute la phase du juge doit tenir, sinon elle n'est pas jouée.
- **Ordre des phases** (brouillon 3, I7) : phase décisive de A, puis bras sans dossier (A, sur le relais d'Argon encore chaud), puis
  phase décisive de B, puis phases du lot réel ; un arrêt de la course pendant B (A2 de B, garde de durée) ne fait plus perdre le bras.
  Un A2 de B arrête toujours la course (règle A2 inchangée ; la contre-lecture v2 propose de n'arrêter que B : décision du directeur,
  rapport, section 8, décision 2).

## 9. Lectures préalables déclarées

Avant le brouillon 1, son rédacteur a joué des courses **à blanc** (juges scriptés, aucun appel) et des simulations du plan, et
en a lu les sorties : elles ont servi à choisir le plan (graphe 3-régulier, paires mélangées pour B, critère de reproduction plutôt
que corrélation de rangs pour D4, biais de position par la part du premier plutôt que par la bascule). La contre-lecture
(`prereg/contre-lecture-preenregistrement-juges-idees-v2-v1.md`) a joué d'autres courses à blanc (juges scriptés, dont un juge qui
ne lit aucune table) et des calculs de puissance, sans appel de modèle ni donnée réelle ; elle a écrit P12 et P13. Pour le
brouillon 2, son rédacteur a joué, sur le code de ce brouillon-là : le contrôle de diagnosticité sur les deux jeux de matériaux, les
tables de puissance et le plan joué par des juges scriptés (section 5), et les courses à blanc du rapport (plafond, parfait, bruité,
biaisé de position, juge en panne) ; il les a lues avant d'écrire D1 (test seul, pour la puissance de 0,9 demandée), D4 et D6 (niveau
0,10), D5 (0,15), D6 (exactitude de B), P14 à P16, les seuils du contrôle de diagnosticité (2 courses sur 20, aire moyenne 0,62) et la politique du relais. Pour ce brouillon 3, le rédacteur a écrit les règles neuves du contrôle de diagnosticité (D1b au plus 2 fois sur 20 et aire des lois fausses au plus 0,62 pour tous les juges qui ne lisent pas les tables ; témoin à 18 sur 20, écrit ensuite « 90 % des courses », même valeur à 20 graines, pour qu'un essai puisse le jouer sur 4 graines) avant de jouer ce contrôle sur les matériaux neufs ; mais il a **retouché les matériaux après des mesures**, sans toucher aux seuils, dans cet ordre : (1) un premier jeu apparié par l'écart seul passait le contrôle de diagnosticité ; (2) un calcul à côté du contrôle (plus haut pourcentage écrit : aire 0,17 sur les témoins d'évaluation, 0,05 sur le sous-ensemble de D1b, venue des variantes de rédaction et du niveau des taux affirmés) l'a fait apparier aussi la rédaction et centrer les taux sur le taux moyen, et ajouter cet indice et ce juge au contrôle ; (3) le contrôle a alors refusé le jeu (« seuil de prédiction le plus bas » : D1 4 fois sur 20, aire 0,644 : les bonnes lois annonçaient des seuils plus petits), d'où l'effet de 0,45 de la bonne loi graduée croissante (un premier essai, ramener à 0,45 les deux lois établies ordinales, a été abandonné : le calcul de surface y trouvait les seuils hors des bornes, aire 0,344) ; (4) il a refusé le suivant (« plus haut pourcentage écrit » : aire des lois fausses 0,625), d'où le centrage des taux de chaque loi fausse sur ceux de sa bonne loi appariée ; le cinquième jeu, celui de ce texte, est conforme. Ces retouches ont été guidées par des juges qui ne lisent pas les tables, sur des propriétés de surface, sans aucune réponse de juge réel ; elles sont dites ici pour que la contre-lecture puisse chercher un trait que ce processus aurait laissé. Il a aussi joué les courses à blanc du rapport et recalculé le plan joué de la section 5 sur ces matériaux et cette politique du relais. Pour ce brouillon 4, le rédacteur a, dans cet ordre (heures UTC du 4 novembre) : lu la contre-lecture v3, ses couples et ses sondes ;
**écrit et scellé la batterie tenue à l'écart** (02:27:55, sha256 `a1999ca5…`) avant toute construction ou lecture des matériaux
neufs ; écrit les matériaux « mondes-v4 » (jumelles, seuils pairs, une ligne par caractéristique, ordre tiré) et joué la seule
batterie figée (batterie tenue à l'écart masquée) ; **retouché les matériaux après ces mesures**, règles et seuils du contrôle
inchangés : (1) ordre de la table 1 d'abord tiré au hasard, puis tiré jusqu'à l'équilibre des rangs (le juge « rang » tenait D1 7
fois sur 20) ; (2) texte long réécrit en mots ordinaires (« longueur moyenne des mots ») ; (3) lois établies désignées par leur
ligne (« lignes du dossier » : D1 3 fois sur 20, par les redites) ; (4) jumelles des lois fausses graduées : quatre choix
possibles (bonne loi croissante ou décroissante, monde-1 et monde-3) joués sur la batterie figée, le moins séparé retenu (la
croissante dans les deux mondes) ; (5) Wilson nommé par la métrique de l'interaction (« -wilson » : D1 4 fois sur 20) ; (6) dix
graines de matériaux (20261102 à 20261111, celle du texte comprise) jouées sur la batterie figée pour voir si le reste tenait au
hasard (une refusée par la construction, quatre par le contrôle de forme, cinq par la diagnosticité avec 6 à 24 motifs, juges
différents d'une graine à l'autre) — **aucune autre n'a été retenue** : la graine reste 20261102, celle des brouillons précédents ; (7) mesuré le juge de la pièce sur
200 courses (section 4). La batterie tenue à l'écart a ensuite été jouée une fois sur les matériaux de ce texte (05:33 à 05:37,
dans une passe d'essais du lanceur ; puis de nouveau, à l'identique, 05:37 à 05:41, sortie au rapport) ; rien n'a été retouché
depuis. Il a aussi recalculé le plan joué de la section 5. Aucune donnée réelle n'a été vue ; les 12 fiches réelles
n'ont pas été lues ; aucun appel de modèle n'a été fait. Ces courses à blanc ne disent rien des juges réels.

## 10. Portée (ce que l'expérience ne dit pas)

- Rien sur la qualité des idées réelles : le lot réel est décrit, pas jugé.
- Les témoins sont des gabarits dans trois mondes plantés, servis avec un dossier de faits ; les fiches réelles n'ont ni dossier
  de ce type ni vérité connue. Un succès dit que le protocole **peut** faire départager quand l'information existe, pas qu'il
  départage les fiches réelles.
- Deux juges (Argon, Astra) : rien sur Kimi ni sur Claude comme juges. Le rôle de B est réduit (un tirage, paires mélangées).
- L'ancien protocole est rejoué avec le dossier inséré sur les témoins (ce n'est pas l'entrée exacte du second tour) et, par le
  juge A seul, sans dossier (la forme de l'entrée du second tour, à la consigne et aux items de la configuration près ; un juge,
  Argon, au lieu de Kimi et Argon).
- La consigne v2 nomme exactement les familles de défauts plantées (loi contredite, redite, affirmation vraie par définition,
  texte sans affirmation réfutable), la longueur, et demande un signe compatible avec le dossier ; elle a été écrite par l'auteur des
  témoins. La comparaison porte sur des protocoles complets, consigne comprise : un succès ne dit rien des défauts que la consigne ne
  nomme pas (la classe « signe contraire » n'y est nommée qu'à travers le critère de prédiction).
- Les matériaux retirent par construction ce que la section 4 nomme (jumelles, seuils pairs, une ligne par caractéristique, rangs
  équilibrés) ; ils **ne sont pas** inséparables par tout trait de surface : six juges des deux batteries y séparent encore les
  classes par l'aire, et le contrôle les refuse (B10 ouvert) ; aucun contrôle par juges scriptés ne couvre plus que les traits qu'il
  nomme. D1 mesure
  la lecture du contenu (dossier ou fiche) ; D1b mesure la lecture des tables (aucun juge de surface, un juge témoin qui ne lit que les
  tables : section 4). Chaque loi fausse d'évaluation est la jumelle d'une bonne loi du même monde : une paire « loi fausse, bonne
  loi jumelle » peut se présenter avec des hypothèses identiques sauf la caractéristique ; seule la table les départage.
- Plan creux (graphe 3-régulier) : une fiche qui ne rencontre que des fiches de sa classe garde une force peu informative ; les
  ancres peuvent s'inverser dans un lot.
- D4 et D6 sont jugés au niveau 0,10 (reproduction et accord, une fois D1 établi au niveau 0,05) : un juge dont la discrimination ne
  se reproduit pas du tout passe D4 une fois sur dix ; c'est le prix d'un plan qui ne conclut pas I4 par manque de puissance.
- Les gabarits sont écrits par un modèle de la famille Claude ; aucun juge de cette famille ici, mais une familiarité de style
  entre gabarits et juges d'autres familles n'est pas mesurée.
- Coût du v2 en production : par lot de n fiches et degré d, n·d appels par juge et par tirage (deux ordres) contre n pour
  l'ancien ; non évalué ici au-delà du devis.

## 11. Code gelé

Fermeture des imports du chemin réel (`FICHIERS_GELES` du lanceur, mesurée par l'essai `Fermeture`, inchangée depuis le
brouillon 1 : 62 fichiers) ; le lanceur refuse un bloc qui ne la couvre pas exactement ou dont une empreinte diffère du fichier
présent. Empreintes de l'arbre de rédaction (arbre de travail `prep/juges-v2-brouillon4` parti de `faff48b`, quatre fichiers modifiés),
relevées à la composition de ce texte (heure au rapport) ; commit qui portera ce code : À REMPLIR

(le lanceur refuse le texte tant que ce marqueur reste ; les empreintes sont à relever de nouveau sur l'arbre à sceller).

<!-- empreintes-du-code : début -->
```
bc5e9c98acff41b97487e2345d33768c8cdf41f0ededf8b2eed0bf842c889845  demonstrations/ideation_v2.py
4212d4c9d014a265847d4c4ed87a8cd804fdafa73f85fd8947874d63fca1c36d  demonstrations/ideation_v4.py
1894f250264eaaccbf891dfa255e71dc587fe415c8d21e283391203a2fe73444  demonstrations/ideation_v5.py
4c302e5b97b229d5b3edd9e9a427f1e50796c10f7081f63132165ffeef854ba4  demonstrations/ideation_v6.py
7b90e65e1308b1c230b3f804743cfc42b9dc571d93b73ed6c5f3f8c9d2b481b2  demonstrations/ideation_v7.py
2e2be8d72c548e183b94c14de20c971f241f998f54f64c5281b2427fdd64e9d1  demonstrations/ideation_v8.py
3b314d9173fa498429bd95e8d78be19904f85cf32b492c3aecbb08f8fda04bc5  demonstrations/validation_juges_idees_v2.py
f7341b965ddba1e0fb21b44d9068f59650d5c77e3175f2b6b7ca879219fa5c9b  pole/__init__.py
09a46515ff30a99f360fcbc7d4c613c35cb511439a5b6c249327e477fdee4ada  pole/adaptateur_kimi_v53.py
a1a8ede8d38884a28365ee797dcd3018dbf09ea1baefa3f57cfcb3281c529c99  pole/adaptateurs.py
d36c79b272af450b8d67313f44068743d80f0204bcedbd30f5d879829c945a17  pole/adaptateurs_v56.py
a856cdaa37e8fb1f3b873ef2c0d9aa439ee0a8838f5ee9a2910cb3c0dcf8007f  pole/aiguilleur_v53.py
962eb8ce22d5af1bf59970e9ef9cab15620edef4d5e9746161bc302e97c2af02  pole/bisociateur_v53.py
20d938b2dcafcd4bb7c9777a0182a3590b390a146a8375590905741ea0e250f8  pole/bisociateur_v54.py
d9521311a96384494871e9f9fcd4b4554548b9f45fdc28e8e75ca30d4c54d22f  pole/bisociateur_v55.py
cefc7e76322b8f8266ec77f31ecb06bf1ea21633ab5dec1e1b91dc62e4374345  pole/budget_v53.py
220d25e6ce5a7eed008c095ef1a9f66e84b4e98f801dfee2f74bdda02ba5ac62  pole/budget_v54.py
3a672aceeeee3cf83cd4e46ca461fdbaf3acd0a9552be24d2566627ce6b7c13e  pole/budget_v56.py
78abfd4731218e20538418608ebebaca3364206ef6d014b7a34829a3c9fd7e85  pole/caviardage.py
f8a70c8f71c380689b2979e3c212d09379ceee1973465b2b207b493cbd73c380  pole/coffre_v53.py
ef10fe044608fda51d5cd4b3b855da677845be83d1367ca3aa33fe45337e33fd  pole/coffre_v55.py
ef72ffbf6b5ba546fb5e509502b59f0d9ac4f78772dcb9570ef36086639f4a78  pole/configuration_v53.py
3424ca7fa8911e5c2656cb56632f7d74c958008b9366af0ac45e6a62e4d16d66  pole/configuration_v54.py
2e6237c0a8b1c823fa17ddd6c680357a59ec4030bfbe9ac6ba970a700a864071  pole/configuration_v55.py
122405228d6ec550b2120114e87a1e70bcc74c14eee17342605d8402bd015d6b  pole/configuration_v56.py
8f2d035828df913d8fa92e1b7d0c8e41ac73e8416e60f3b674753c27f5c61237  pole/course2_v53.py
ac1980d04eb88d8fbb9a073902e47146ab9eadd3375a41cd72835fa5acf20342  pole/course2_v54.py
ee6a861e7f8db32a9545372a51f902389cdbea809b0ba354e621a3681e541a70  pole/course2_v55.py
14f655696876afc8453ec5237236b3f9daf8d87844c4acc9d5189b3e61b310f1  pole/course2_v56.py
62fd284519278382592a4684e9d4ecd32baad5e11491c256ef64ee844f08d087  pole/dossier_ferme.py
d568d25bf7d96011cfdcda12e7bc2c1933a61827b237f8c8c363b4055122ad4b  pole/etage_entre_generations_v53.py
86a6bec00c3fee9b4ea510cf8dad8d899b9c96adef1e5ae4f8a8281d658143e5  pole/etage_entre_generations_v54.py
865bd7e5734618a2e989bdd14726ff7db53e014963cbc93b48be1892c7ab4dd9  pole/etage_entre_generations_v55.py
f0c80e2d9801d4a928574f7f442e2950c2d130d77015b30102911bfa87dd6eba  pole/etage_entre_generations_v56.py
7cfcf8329c66c7a37ceb2992cc96e21aedbfa0a10525467672794090a128eda6  pole/fiches_v53.py
1ab0796dd5d9de14ea84953b0307a065572bc300ebe45209ca207d7880bbaebf  pole/fiches_v54.py
3abd0e19a8f16cc1c2a8f2590ea04831a7d9ba25c02129fb881b87be3983f390  pole/garde_outils.py
83b54b816b3277d97f5340ad4a316094a492bc2090c782b3e134092a97ca1edf  pole/gardes_e0_v54.py
e46c5cd0a301c89830d97c098ee52b33ead6b01cafe15ab8454e6b7957c54db1  pole/gardes_e0_v55.py
921e59f23753666d6367678447edf4ee2964dc6ec3d382aefa8582b996e123b9  pole/gardes_e0_v56.py
7eb838958b28c7b7a5ee20177dfc3d0c194002b99b2382e019fe7d91c3090dc0  pole/graines_v53.py
67d2ad3591b21601ece4101154138f532ba519024761beb8c9738181f8f3fefc  pole/ideation_v2.py
c4c6ab12dc471eef078c116a4205a22d9b498da720ce71e37a0a6edae6c4239b  pole/juges_croises_v53.py
402fb1ba48a0701267de093c3a70d608b27d5e274f96fae7644bae8dc5e528c3  pole/juges_idees_v2.py
43b01b43b1ec347ff02b456975d74c17e7a0e974e9b95e9ba4935bdb895f31a0  pole/memoire_v53.py
8f3f57fc98972fbcf6aefb27fd37298ac67f249cd295c7127b47ab8e77626c08  pole/mesures_v54.py
35d9a996aaacf6d61e84762a2173e73e3c1a90eda730cce122a0f321b038d0e1  pole/moisson.py
711a32679164bd63605f0bcc2a96f37d53260c479004d04d887d8228ac7d431b  pole/noyau_v54.py
ca0f2dda980777da9c549519c6b15994309722353b22f88d117e95aa2c2d4035  pole/noyau_v55.py
eb5a003e8f23b0882e5588fe537e8b65b890f0d7d19560896be4e85a0731543b  pole/noyau_v56.py
966d9553026aad1eb7d97fa677334f1b59f22a39f15eef95134d63bc47634444  pole/outils.py
ec6c2cf64d0c9a3bcb3484f2bc58ca986c89e97829bd45fdb96cbc42bf094fef  pole/pari_apparie.py
77056684e5d1b2149521878da396d51bb3f16834de85ca9e86acdc7e1998592d  pole/prepilote_v54.py
e91e07e4f3bf67cd5106129586048abb3b06284eb9812f8e4da4082087859f05  pole/prepilote_v55.py
dfce55061c65b5ae7526161c54be17005ddef631cb539463cd2c23b32b87b087  pole/prepilote_v56.py
0657eec8e0b1a3d2a3f57f37aad59c34554a2352be4e42ed2c3395e9e94fe2b5  pole/protocole_outils.py
b5a76343e458cf8fb91ee1928244f9cb65d50c27ab9b1bae91c21a5c82349da3  pole/relais.py
1b90b020287e575b5564508f9ba33b87bbc051c1015f4198e6b6e648d50ee153  pole/relais_reel.py
620225973d68670a56ca913cdd02709fa576fa43e1393d166915ea67c1d7c3bb  pole/suivi_roles_v54.py
1a8267fea6d147b070d697ccd2c9d33f2514be6fcba106dca8ca123be1cb7403  pole/tableau_v53.py
363a3725885da08412f25b28defba7a8d204d883c3637f1de1df83686d93a41a  pole/tests_de_mort_v2.py
ea05eb55f9d179501fb091d25298deaf36cd66ad16fd65bdca4dcf5e4ba74bba  pole/tests_de_mort_v3.py
```
<!-- empreintes-du-code : fin -->

## 12. Devis

**Prix et durées, avec leurs sources (R6).** Argon : **0,062 USD et 7,6 s par appel**, mesurés sur 526 appels d'A1 sur un fil
(`registres/decisions.md` du dépôt de travail, ligne 1230, R-1266, sha256 du registre lu le 3 novembre à 01:32 UTC
`39ef7ecb153ae4af4d599886eecd02d0b6ce7a01e2e59932f7fc75ce01090201` ; le registre ne fait que croître : les lignes citées y ont été relues, puis de nouveau, inchangées, par la contre-lecture v2 le 3 novembre 2026 vers 05:30 UTC, à `2d8d07f5fd7d69a873f3cc72b25022c1d912ba10755e2968d9aea7f13ad068e8` ; empreinte à relever encore au scellement) ; ces appels n'étaient pas des comparaisons (une entrée de
comparaison porte la consigne, le dossier et deux fiches : 7 520 à 9 057 caractères, 8 242 en moyenne sur les 198 paires possibles des trois lots, matériaux de ce texte, brouillon 4 ; le même calcul donne 8 644 à 10 675 sur ceux du brouillon 3, dont le texte disait 8 565 à 10 654) ; borne de durée du plan 8 à 40 s (celle du plan (b′) d'A1, `pole/attaque_goodhart_v3.py`, ligne 91 au commit `66dbcf1`, ligne 112 au commit `3e7ca5c`).
Astra (`gpt-6-astra`) : **non mesuré** (prix « 10/50 supposé » par million de jetons d'entrée et de sortie, `registres/decisions.md`,
ligne 1215, R-1251 ; taux de devis 0,25 USD par appel du plan A1-bis, `pole/attaque_goodhart_v3.py` au commit `66dbcf1`, lignes 84-85, sha256 `b821bdb73a2829a41d519800859bbf10216254ca97228b5a179438eed38a1c6a` ; au commit `3e7ca5c`, ce fichier vaut `cb9cffe77fb858bf279c41881638edecba0166b034a05d44c2f62e2b25a45df3` et porte les mêmes valeurs aux lignes 105-106) :
le plan prend une **borne prudente de 0,50 USD par appel** (deux fois le taux d'A1-bis ; au prix supposé, 0,50 USD couvre environ
3 000 jetons d'entrée et 9 000 jetons de sortie, raisonnement compris) et 10 à 120 s par appel ; l'épreuve (section 4) le mesure ;
la course projette au prix observé.

| phase | juge | appels | USD au prix du plan | requis ? |
|---|---|---|---|---|
| décisive A | Argon | 246 | 15,25 | oui (sinon arrêt avant tout appel) |
| sans dossier (A) | Argon | 30 | 1,86 | oui |
| décisive B, comparaisons | Astra | 24 à 36 (32 à la graine 20261102 ; au plus 39) | 12,00 à 18,00 (16,00 à la graine 20261102 ; au plus 19,50) | oui |
| décisive B, ancien | Astra | 30 | 15,00 | oui |
| réel, ancien | Astra ; Argon | ≤ 13 ; ≤ 13 (lot de substitution : 12 ; 6) | ≤ 6,50 ; ≤ 0,81 | non : jouée si sa projection tient |
| réel, v2 | Astra ; Argon | ≤ 13 ; ≤ 13 (12 ; 6) | ≤ 6,50 ; ≤ 0,81 | non |

**Requis** : Argon 276 appels, 17,11 USD (part 24 : 1,4 fois) ; Astra au plus 69 appels, 34,50 USD au plus à la borne prudente
(part 36) ; total requis au plus 51,61 USD ≤ 60. **Maximum** (lot réel de 13 fiches toutes admises pour A, 39 paires mélangées) :
Argon 302 appels, 18,72 USD ; Astra 95 appels, 47,50 USD à la borne prudente — au-dessus de sa part : les phases réelles d'Astra ne
sont alors pas jouées (règle de projection, section 8), jamais un arrêt. **Attendu** (graine 20261102 : 32 comparaisons de B ; lot réel de substitution de 12 fiches, 6 admises pour A) : au taux d'A1-bis (0,25 USD par appel
d'Astra), 39,36 USD, toutes phases jouées ; à la borne prudente (0,50), 48,86 USD, les deux phases réelles d'Astra non
jouées (au-dessus de l'attendu de 30 à 43 USD écrit au GO-2026-11-02-32, sous le plafond : la borne est prudente, pas mesurée) ; dans tous les cas ≤ 60 USD par construction (parts portées au relais par la porte de plafond, compteur à parts). Les
incidents du relais s'ajoutent, comptés dans la dépense et dans la part du juge, jamais dans le prix observé : échecs coûteux, coûts inconnus comptés au plafond de session (`plafonds_session.juge`, au moins 1,00 USD), et **pire cas réservé de chaque code 3 au pire cas** (brouillon 3, B9) ; aucun compte d'échecs de suite n'arrête un juge sur des codes 3. **Marge d'incidents d'Argon** : 24 − 17,11 = 6,89 USD, soit 29 tentatives au pire cas réservé de l'entrée de comparaison la plus longue (9 057 caractères : environ 3 020 jetons à 10 USD par million, plus 4 000 jetons de sortie à 50 USD par million, ≈ 0,230 USD ; barème prudent de la commande, n° 294, section 4 ; à mesurer à l'épreuve) ; avec les attentes de la section 8, cela couvre environ 11,6 heures d'erreurs continues de l'interface dans la phase décisive de A (4 125 s pour les huit premières attentes, puis 21 × 1 800 s) ; au-delà, le bras sans dossier, projeté sur ce qui reste de la part, n'est pas joué (S0 ; course à blanc du rapport à 25 pires cas : I1a, S0, T1, rejouée par la contre-lecture v3) ; au-delà d'environ 24 − 15,25 = 8,75 USD d'incidents pendant la phase décisive de A, la part de A est atteinte et la phase décisive s'arrête (I0 « part ») : la seule borne qui reste est le plafond exact du GO, nommée et proposée au directeur (rapport, point 3). Astra : marge de 36 − 34,50 = 1,50 USD à la borne prudente ; au-delà, ses étapes suivantes ne sont pas jouées (étape par étape), jamais un arrêt de la course. **Règle du prix mesuré (brouillon 4, I12)** : au-delà de 0,074 USD par comparaison d'Argon mesuré à l'épreuve, le lanceur refuse le texte (section 4) ; un délai (code 6) est désormais attendu et repris, son coût compté dans la même marge (section 8). **Pire cas de la course : 24 + 36 = 60 USD**, par construction (compteur à parts, portes de plafond, registre des commandes).

**Durée** (séquentielle, bornes du plan, sans attente sur le relais) : 0,88 à 6,07 heures pour le plan de la course à blanc de référence, toutes phases (plan maximal : 0,94 à 6,52 heures) ;
garde de 48 heures contre une boucle folle, jamais une coupe de la mesure ; délai par appel de la commande externe : 1 800 s
(`AdaptateurCommandeExterne.DELAI_COMMANDE_S`), garde contre un appel bloqué ; attentes du relais en sus (code 3 : 15 s à 1 800 s entre deux tentatives, sans limite de nombre) ; panne d'un juge déclarée après 6 heures depuis le premier échec de sa série, **hors des phases décisives seulement**.

**Options écartées, pour mémoire** (GO-2026-11-02-32 a tranché) :

| juges | pourquoi pas |
|---|---|
| Argon (A) + Kimi (B) | exclu par GO-2026-11-02-32 : coût et durée (0,35 USD et 600 à 1 500 s par appel au plan A1-bis, `pole/attaque_goodhart_v3.py`, lignes 82-83 au commit `66dbcf1`, lignes 103-104 au commit `3e7ca5c`) et fiabilité du relais Kimi à A1 (5 appels réussis, 616 en échec, `registres/etat.md`, ligne 6) |
| Kimi (A) | idem ; en séquence, les 246 appels de la phase décisive de A prendraient 41 à 103 heures aux bornes du plan A1-bis |
| Argon (A) + Opus 5.5 (B) | famille de l'auteur des gabarits des témoins : refusé par le code |

## 13. Avant la course

Dans l'ordre :
1. **B10 d'abord** : décision du directeur sur la règle du contrôle de diagnosticité (rapport, section 8, décision 1), puis matériaux
   neufs ou règle neuve sur un brouillon 5, avec une batterie tenue à l'écart écrite par un autre que celui qui accorde les matériaux ;
   puis contre-lecture neuve (R2) du delta (matériaux, batteries, délai passager, relevé de l'épreuve, règle du prix, M17 à M20), du
   module, des essais, du banc et du lanceur. Le registre des GO que lira le lanceur est désigné (réserve du statut : celui de cette
   machine est refusé par `verifier_go_v56`, « GO-2026-10-24-07 en double »).
2. **Épreuve des commandes** (section 4) par la session qui tient les clés (la fille neuve de session-depot, `registres/decisions.md`,
   R-1294 et R-1301), sous le GO que le directeur désigne ; relevé recopié dans la section 4 à la place de la phrase qui l'annonce et de son marqueur. Si le coût moyen d'une comparaison d'Argon mesuré à l'épreuve dépasse 0,074 USD (276 appels requis : la marge d'incidents de la part de 24 USD tomberait sous la moitié de 6,89 USD), ou si la ligne d'erreur d'un 413 provoqué n'est pas reconnue par le motif `_REQUETE` du cœur, nouveau texte (rapport du brouillon 3, décisions 3 et 4).
3. Configuration préparée par la session qui tient les clés (commandes `argon` et `astra` avec porte de plafond,
   `plafonds_session.juge` ≥ 1,00 USD et au moins ce que l'épreuve demande, `modeles_servis_permis` si l'épreuve voit un identifiant servi
   daté autrement que `-AAAAMMJJ`, pièces `consigne_juge`, `question_course_2`, `lot_reel_juges_idees_v2`) ; son empreinte (sha256 du fichier tel que passé à `--configuration`) écrite à la
   ligne `configuration_sha256` du bloc `plan-gele` ; la session qui tient les pièces vérifie que la consigne figée de l'ancien juge passe
   la garde A4 des témoins (`exiger_entrees`).
4. Relevé des réglages propres du relais 8805, `--plafond-usd` et `--max-appels`, avec le réglé et l'engagé à l'heure du relevé (leurs
   refus, HTTP 402 et 429, sortent en code 4 au plancher : n° 294 de session-depot, section 3), et vérification qu'ils laissent la part
   d'Argon et tous les appels prévus, reprises et tentatives au pire cas comprises (au moins 276 appels et 24 USD, plus les tentatives
   de la marge d'incidents, section 12).
5. Ordonnancement : aucune autre course n'emploie le relais Argon pendant celle-ci (relais à un seul fil : un second appel attend et
   peut expirer en code 6) — A1-v3, scellé (`registres/decisions.md`, R-1301), et sa seconde course (GO-2026-11-03-01) emploient le même
   relais : les courses ne se chevauchent pas ; GO-2026-11-02-32 échoit le 16 novembre ; hôte gardé vivant pendant toute la course (la
   première course d'A1-v3 s'est arrêtée par l'infrastructure, conteneur repris : GO-2026-11-03-01).
6. Recalcul des empreintes du bloc `plan-gele` et du bloc de la section 11 sur l'arbre à sceller ; essais et banc de mutations rejoués
   sur cet arbre ; commit écrit à la place du marqueur de la section 11 ; `--verifier-seulement` ; GO de Lazar au plafond exact du texte
   (GO-2026-11-02-32, 60 USD) ; scellement, commit, poussée ; puis la course chez session-depot, une seule fois ; sortie scellée avant
   lecture. La lecture gelée est prononcée par un lecteur neuf (R13), puis soumise à Lazar.

## 14. Couples de la contre-lecture v1 : appliqués, refaits, et changements propres au brouillon 2

Section gardée telle que le brouillon 2 l'a écrite (« ce brouillon » y désigne le brouillon 2). Les 40 couples
(`prereg/couples-contre-lecture-juges-idees-v2-v1.json`, numérotés dans l'ordre du fichier) ont été écrits
pour le texte du brouillon 1 et les décisions connues alors (GO-2026-11-02-24, 20 témoins, juge B à confirmer). GO-2026-11-02-32 a
tranché depuis (juges, taille, parts) : un couple est **appliqué tel quel** quand son texte nouveau est repris au mot près (ou
précisé sans changer son sens), **appliqué, adapté** quand son sens est repris avec les valeurs de GO-2026-11-02-32 ou du code de ce
brouillon, **refait** quand ce brouillon le remplace par autre chose, pour la raison dite.

| couple | objet | sort | raison |
|---|---|---|---|
| C1 | statut du texte | refait | des couples sont refaits, pas tous appliqués ; le brouillon 2 n'est pas contre-lu |
| C2 | marqueurs restants | refait | la consigne ne permet de marqueurs que pour le GO, la configuration, les empreintes du code et l'épreuve d'Astra : GO-2026-11-02-32 nomme Astra (plus de marqueur MOT_DE_LAZAR_ASTRA) ; les matériaux rééquilibrés sont dans le code et leur empreinte est écrite (plus de marqueur MATERIAUX_SHA256) ; les sources du devis sont écrites avec chemin, ligne et empreinte (plus de marqueur SOURCES_DU_DEVIS) ; les réglages `--effort` et `--reflexion` sont à recopier avec l'épreuve (marqueur EPREUVE_ASTRA_8807, qui remplace REGLAGES_DES_JUGES) |
| C3 | lignes de `kappa_cohen` | tel quel | |
| C4 | bras sans dossier | adapté | 30 témoins (15 contre 15) et GO-2026-11-02-32 au lieu de 20 et du « 2 novembre » |
| C5 | H0(b) en deux branches | tel quel | |
| C6 | P11, P12, P13 | tel quel | P11 précisé « ancien avec dossier » |
| C7 | gabarits et a priori (B1) | refait | le couple décrivait le défaut et laissait l'empreinte en marqueur ; ce brouillon rééquilibre les matériaux (trois mondes, lois fausses graduées sur des caractéristiques plausibles, bonnes lois de deux groupes sur des caractéristiques peu plausibles, sens équilibré par une loi décroissante neuve par monde et par la classe « signe contraire »), étend le contrôle de forme à six indices bornés des deux côtés et ajoute le contrôle de diagnosticité (section 4) |
| C8 | Astra hors du périmètre écrit du GO (B6) | refait | GO-2026-11-02-32 nomme Argon et Astra et exclut Kimi : plus de nœud, plus de marqueur |
| C9 | A2 sur le statut « refus » de la commande v56 | tel quel | |
| C10 | table des étapes | adapté | 30 témoins, trois lots, au plus 39 paires pour B (13 par lot), comparaisons de B avant son ancien protocole, règle de projection par phase |
| C11 | tâches de graines du bras sans dossier | tel quel | |
| C12 | GO de la commande de lancement | refait | GO-2026-11-02-32 (la ligne de 60 USD inscrite plus tôt pour cette course « n'est pas utilisée », dit GO-2026-11-02-32) |
| C13 | `materiaux_sha256` | refait | empreinte calculée sur les matériaux rééquilibrés, au lieu d'un marqueur |
| C14 | plafond 60 USD, parts 24 et 36, durée 48 h | tel quel | |
| C15 | `go` du bloc `plan-gele` | refait | GO-2026-11-02-32 |
| C16 | paragraphe sous le bloc | refait | empreinte des matériaux écrite ; GO-2026-11-02-32 ; politique du relais gelée |
| C17 | métriques du bras sans dossier | tel quel | |
| C18 | kappa des paires (I5) | adapté | D6 devient l'exactitude de B (test binomial) ; le kappa des paires reste descriptif (P6), avec sa relation (2p − 1)² et l'absence de kappa « sur les paires de même qualité » |
| C19 | bascule par tirage et par paire (M3) | tel quel | |
| C20 | puissance à 0,9 | refait | recalcul par ce code (graine 20261102, 20 000 répétitions) à 15 contre 15, D1 réduit au test (section 5) |
| C21 | « quelle que soit la taille » (M2) | refait | sans objet : D1 n'a plus de seuil d'aire |
| C22 | portée d'une issue négative | refait | 15 contre 15 : 7 % et 0,1 % (section 5 et I3) |
| C23 | D6 et D7 | adapté | D7 à 27 verdicts lisibles sur 30 ; D6 redéfini (exactitude de B, niveau 0,10, au moins 20 comparaisons valides) |
| C24 | validité : pertes du relais | adapté | 27 verdicts lisibles sur 30 ; une perte est un échec coûteux repris deux fois en fin d'étape ; ce qui n'a pas été envoyé est attendu et repris, jamais perdu (section 8) |
| C25 | I3 « au seuil gelé » | tel quel | portée chiffrée à 15 contre 15 |
| C26 | suite de I2 | tel quel | |
| C27 | lecture du bras, S0 à S3 | adapté | réserve « accord du juge B non mesuré » au lieu de « accord entre juges non mesuré » (D6 redéfini) |
| C28 | plafond au-dessus de 60 USD refusé | tel quel | |
| C29 | liste d'arrêt avant tout appel | adapté | complétée : budget par appel, dépense requise par juge, contrôle de diagnosticité, politique du relais dans les valeurs fixes |
| C30 | statuts du relais pendant la course (B2) | refait | code 4 (plafond de session, registre, 402, 429) attendu et repris comme un relais injoignable, et non arrêt « dépense » : 429 est passager, et le compteur à parts arrête déjà tout appel qui ne tient plus dans le plafond ou dans la part ; attente sans borne par appel et panne après 6 h sans réponse, au lieu de 30 minutes par appel ; échec coûteux repris en fin d'étape, au plus deux fois ; arrêt d'un juge seulement hors de la phase décisive de A — pour qu'une panne ne rende pas la course non concluante par défaut de conception (mots de Lazar, GO-2026-11-02-32) |
| C31 | lectures préalables | adapté | complété par celles de ce brouillon (section 9) |
| C32 | portée | adapté | trois mondes, deux juges, matériaux rééquilibrés, limite de D1b, D4 et D6 au niveau 0,10 |
| C33 | sources du devis (M4) | refait | sources écrites (chemin, ligne, empreinte) ; prix de Kimi cité au plan A1-bis du code |
| C34 | table du devis | refait | nouvelles tailles : 276 appels requis d'Argon, au plus 69 d'Astra |
| C35 | total | refait | idem |
| C36 | maximum | refait | idem ; borne prudente d'Astra à 0,50 USD par appel |
| C37 | durée | refait | nouvelles bornes (0,88 à 6,07 heures) |
| C38 | option retenue | refait | GO-2026-11-02-32 a tranché |
| C39 | Argon et Kimi | refait | GO-2026-11-02-32 a exclu Kimi |
| C40 | avant la course | adapté | repris (consigne de l'ancien juge passée à la garde A4 des témoins, relais Argon libre), complété par l'épreuve d'Astra ; GO-2026-11-02-32 au lieu du mot de Lazar sur Astra |

**Changements propres au brouillon 2** (au-delà des couples) :
1. Juges Argon et Astra, parts de 24 et 36 USD, plafond de 60 USD, garde de 48 heures, tout depuis GO-2026-11-02-32 ; budget par appel
   au moins deux fois le prix de plan le plus haut ; borne prudente d'Astra à 0,50 USD par appel (non mesuré).
2. Trois mondes, 15 bons et 15 mauvais témoins d'évaluation ; classe « signe contraire » (point I2 de la contre-lecture : un défaut que
   la consigne ne nomme pas en propre) ; P14, P15, P16.
3. Contrôle de forme à six indices (sens de la loi ajouté), bornés des deux côtés ; contrôle de diagnosticité par six juges de forme et
   un juge « dossier sans tables » ; D1b qualificatif et lecture des tables T1, T0, T-.
4. D1 réduit au test (p < 0,05) ; D4 au niveau 0,10 ; D5 à 0,15 ; D6 redéfini : exactitude de B, test binomial au niveau 0,10, mesuré
   à partir de 20 comparaisons valides et 0,85 de validité.
5. Ordre des phases : les comparaisons de B avant son ancien protocole ; règle de projection propre à chaque phase (tout ou arrêt pour
   la phase décisive de A, étape par étape pour B, toute la phase ailleurs).
6. Statuts du relais classés à chaque appel (B2) : rien d'envoyé attendu et repris ; échec coûteux perdu puis repris au plus deux fois ;
   panne ; règle écrite d'avance des comparaisons perdues ; arrêt d'un juge seulement hors de la phase décisive de A.
7. Gardes du lanceur (B7) : chacune essayée sur un cas sain et sur un artefact, une mutation par garde (rapport, section 4).
8. Indicateur descriptif « au plafond » aligné sur D2 (0,80, point M6) ; identifiant réel de la forme des témoins refusé (point M5).

## 15. Couples de la contre-lecture v2 : appliqués, refaits, et changements propres au brouillon 3

Les 12 couples (`prereg/couples-contre-lecture-juges-idees-v2-v2.json`, numérotés dans l'ordre du fichier) ont été appliqués par script,
dans l'ordre, chaque « ancien » présent une seule fois au moment de son application ; le texte obtenu (668 lignes, sha256
`bf68deb47a58364efcbcc3d9f1e89e8795172d0dd96d04531052ae90e227c167`) est égal à l'aperçu de la contre-lecture ; ce brouillon part de lui.

| couple | objet | sort | raison |
|---|---|---|---|
| C1 | source du taux d'A1-bis (M8) | tel quel | |
| C2 | borne de durée du plan (b′) (M8) | tel quel | |
| C3 | source du coût de Kimi (M8) | tel quel | |
| C4 | empreinte de `registres/decisions.md` (M9) | tel quel | relu de nouveau à 08:35 UTC : `1b1042fca63917e103e5780b7f5ee13e290c9ab4dbc161e4bf5e5aeedd6efa3e`, lignes 1215, 1230, 1240, 1257, 1258, 1264, 1265 inchangées ; à relever encore au scellement |
| C5 | machine qui tient la clé d'Astra | tel quel | |
| C6 | contenu de l'épreuve (I9) | refait | sens repris en entier ; le marqueur de l'épreuve d'Astra est remplacé par une phrase de relevé (consigne : un seul marqueur, celui du commit) ; ajoutés : la table des codes vérifiée sur chaque commande (code 3 au plancher et au pire cas, code 4 provoqué, 413 provoqué, sans appel au modèle pour ces trois) et le pire cas réservé d'Argon pour l'entrée la plus longue de ce texte (10 654 caractères, le dossier de monde-2 et de monde-3 porte une table 3) |
| C7 | `plafonds_session.juge` (section 4) | tel quel | |
| C8 | `plafonds_session.juge` (section 13) | refait | la section 13 est réécrite en liste ordonnée (I9, M16) ; le sens du couple y est, point 3 |
| C9 | ordonnancement avec A1-v3 et relevés du relais 8805 (M16, I9-d) | refait | même sens, section 13 points 4 et 5, complété par la seconde course d'A1-v3 (GO-2026-11-03-01, inscrite depuis) |
| C10 | arrêt après la phase décisive de A (M14) | tel quel | |
| C11 | pertes de l'ancien protocole (M14) | tel quel | suivi de la règle d'une course tuée (I8) |
| C12 | puissance de D1 (M13) | tel quel | |

**Changements propres au brouillon 3** (au-delà des couples) :
1. **B8** — matériaux « mondes-v3 » (empreinte `2ee2f2e4517b25116ca3c48826acdecf93f17226bfe31ddec58d3cfa58dbba58`) : lois fausses appariées à une bonne loi (écart, rédaction, centre
   des taux), deux interactions fausses contredites par une table 3, sens et champ « signe » répartis (M12), redites et signes contraires
   rédigés comme une bonne loi, effet de la bonne loi graduée croissante porté à 0,45 ; contrôle de forme à quatorze indices et au
   vocabulaire, sur les témoins d'évaluation **et** sur le sous-ensemble de D1b ; contrôle de diagnosticité à 23 juges de surface tenus à
   D1 et à D1b, et un témoin positif (« lecteur des tables ») tenu à réussir ; matériaux du brouillon 2 (`59737a16…`) refusés.
2. **B9** — politique du relais selon la table des codes de la commande réelle : code 3 au plancher comme au pire cas attendu et repris
   sans limite de nombre, pire cas compté ; code 4 et refus de requête : arrêts nommés, sans attente ; attente après un échec coûteux ;
   aucune panne par la durée dans les phases décisives (seule la garde de 48 heures) ; marge d'incidents d'Argon écrite au devis.
3. **I6** — horloge de panne partie du premier échec de la série en cours, remise à zéro sur une réponse.
4. **I7** — bras sans dossier juste après la phase décisive de A ; identifiants servis admis par la configuration (`modeles_servis_permis`)
   admis aussi par le contrôle A2 du cœur ; la question « A2 de B : arrêt de B seulement ? » est portée au directeur (rapport).
5. **I8** — journal au fil de l'eau sur disque, scellé à la fin ; interruption convertie en arrêt de la course avec journal ; règle d'une
   course tuée (I0 « infrastructure », aucune relance sans GO).
6. **I9** — épreuve étendue (C6), section 13 ordonnée (relevés, configuration, ordonnancement).
7. **M10** constantes mortes retirées ; **M11** redite lue par les mots propres de la loi établie ; **M15** porte de plafond absente :
   refus nommé ; un seul marqueur, celui du commit, refusé par le lanceur comme les marqueurs entre doubles chevrons.
8. Section 5 : le plan joué par des juges scriptés recalculé sur ces matériaux et cette politique ; les tables analytiques (D1, D4, D1b, D6)
   ne dépendent pas des matériaux et restent celles du brouillon 2.

## 16. Couples de la contre-lecture v3 : appliqués, et changements propres au brouillon 4

Les 5 couples (`couples-contre-lecture-juges-idees-v2-v3.json`, `80119546…`) ont été appliqués par script, dans l'ordre, chaque
« ancien » présent une seule fois au moment de son application ; le texte obtenu (833 lignes, deux marqueurs, sha256
`a36e7e481b577f233ada27300e6a7ebf19f29aba3cc7b88bf25a62834c825f65`) est égal à l'aperçu de la contre-lecture ; ce brouillon part de lui.

| couple | objet | sort | raison |
|---|---|---|---|
| C1 | statut et marqueurs | tel quel, puis complété | le statut est réécrit pour le brouillon 4 ; la phrase du couple (deux marqueurs, `configuration_sha256` = sha256 du fichier) y est, plus le refus d'un texte sans bloc du relevé |
| C2 | marqueur du relevé de l'épreuve (I11) | refait | même sens : le marqueur est dans un bloc `releve-epreuve` que le lanceur exige et lit (clés), au lieu d'une phrase seule |
| C3 | seuil de prix d'Argon et forme du 413 (I12, M17) | tel quel, puis complété | la règle est aussi au code (lanceur : `prix_epreuve_juge_a_max_usd`, ligne de 413 confrontée au motif) et au devis (section 12) |
| C4 | `configuration_sha256` = sha256 du fichier | tel quel | |
| C5 | marge d'incidents : S0 avant I0 | tel quel | |

**Changements propres au brouillon 4** (au-delà des couples) :
1. **B10** (non levé) — matériaux « mondes-v4 » (empreinte `14849fdbdd634ea3abaedf660de2b53f60e3c06458d468e39509d9ec2ba22219`) : lois fausses jumelles, seuils pairs, dossier à une ligne par
   caractéristique (tables croisées et lois établies par numéro de ligne), ordre de la table 1 tiré jusqu'à l'équilibre des rangs,
   texte long aux mots ordinaires, Wilson partout ; contrôle de forme à dix-neuf indices ; contrôle de diagnosticité à deux batteries
   (figée : 66 juges ; tenue à l'écart, scellée avant les matériaux : 56 juges) sous les mêmes règles ;
   matériaux refusés (29 motifs ; six juges par l'aire) ; constat : le compte « au plus 2 sur 20 » est enfreint par
   un juge à pile ou face dans environ un jeu de matériaux sur quatre.
2. **I10** — délai (code 6 ou de l'adaptateur) passager : attendu et repris comme un code 3, coût compté, borné par la part, jamais dans
   les cinq échecs coûteux de suite.
3. **I11** — bloc `releve-epreuve` exigé par le lanceur (mode réel et vérification seule), marqueur unique tant qu'il manque, clés lues.
4. **I12** — règle du prix d'Argon mesuré : au-delà de 0,074 USD par comparaison, refus du texte (arrêt, nouveau texte).
5. **M17** motif de refus de requête élargi, lignes de 413 du relevé confrontées au motif ; **M18** série d'échecs remise à zéro par
   phase ; **M19** SIGHUP converti comme SIGTERM, appel en vol compté au bilan, essai par un vrai signal pendant une vraie commande ;
   **M20** essai borné de la garde de durée dans la boucle d'attente et mutation ; **M21** le rapport compte les retouches exactement ;
   **M22** le n° 294 n'est toujours pas sur cette machine : non recopié (rapport, section 8).
6. Section 5 : plan joué recalculé sur ces matériaux et cette politique ; tables analytiques inchangées. Section 12 : longueurs
   d'entrée et pire cas réservé recalculés ; marge d'incidents inchangée (6,89 USD, 29 tentatives).
