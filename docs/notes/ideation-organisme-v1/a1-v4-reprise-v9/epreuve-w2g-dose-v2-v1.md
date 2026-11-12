# Épreuve hors ligne « W2 gradué » : choix de la dose λ\* d'A1-v4 (texte court, v2, scellé)

## Motif de la v2 (écrit avant tout le reste, avant toute relecture de la trace v1)

**La trace du rejeu v1 est arrêtée par la durée maximale.** Rejeu joué sous le texte scellé `epreuve-w2g-dose-v1-v1.md` (sha256 `3415f70d8690708b4c7c558420c8c19ead1a211d68be277050c46d0ca8b21122`) : script au **code 3** après 6 702,2 s (« dose 1.0 : durée maximale dépassée à la répétition 447 ») ; lecteur gelé au **code 2, arrêt de garde 2** (motifs `code_3`, `arret`, `dose_incomplete` : dose 1,0 à 350 répétitions sur 1 000) ; **aucun λ\*** (R-1946, `registres/decisions.md`, au 8 novembre). Selon le v1 (section 4 bis, garde 2 ; section 6, « Aucun rejeu partiel combiné ») : une nouvelle tentative demande un texte neuf, une entropie neuve, contre-lu et scellé. C'est ce texte.

**Cause mesurée** : la charge de la machine est restée vers 13,8 pendant tout le rejeu v1 pour quatre processus sur quatre cœurs, sans autre calcul de la session (préalable 5 du v1, tenu par la mère). Chaque processus de calcul lançait **quatre fils** de la bibliothèque d'algèbre linéaire de numpy (OpenBLAS 0.3.34, compilée pour 64 fils au plus, sans affinité) : seize fils pour quatre cœurs. Mesuré le 8 novembre entre 23:19 et 23:25 UTC par le rédacteur de ce brouillon, dans une copie de travail neuve préparée comme au préalable 3, en mode exploratoire (graine 11, dose 0,5 seule, 200 répétitions, 4 processus ; 200 et non 40 répétitions, car le script groupe les répétitions par lots de 50 (`TAILLE_LOT`, l. 56) : 40 répétitions n'auraient occupé qu'un processus), sorties non ouvertes ; le script imprime la table de l'essai (graine exploratoire 11, dose 0,5) à la console avant la ligne de durée, et le rédacteur déclare n'avoir lu que la ligne de durée ; ces chiffres exploratoires ne servent à rien ici ; copie supprimée (section 4, « Processus ») :

| essai | fils par processus de calcul | durée imprimée par le script | seconde par répétition (4 processus) | charge relevée pendant l'essai |
|---|---|---|---|---|
| sans variable | 4 | 126,4 s | 0,632 | moyenne sur une minute montant de 0,86 à 11,79 ; 14 à 17 fils prêts à tourner |
| quatre variables à 1 | 1 | 20,1 s | 0,1005 | 1,95 à 20 s (essai trop court pour que la moyenne sur une minute converge) ; 2 fils prêts à tourner |

Les deux tables écrites par le script sont **identiques octet pour octet** (même empreinte, comparée sans les ouvrir) : mêmes comptes et mêmes valeurs imprimées sur 200 répétitions à la dose 0,5 : aucune différence détectée entre les deux réglages ; le manifeste ne consigne pas le nombre de fils, la console le porte. **Remède** : un fil de calcul par processus (`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1`), posé dans la commande exacte du rejeu (section 4). Durée attendue de la grille entière : **≈ 1 150 s** (au lieu de ≈ 4 500 s au v1, et 6 702 s pour 10 350 répétitions observées) ; durée maximale **inchangée** (6 700 s sous `timeout 7000`, outil à 7 200 s).

**Ce qui ne change pas** : la règle de choix (section 2), la grille, 1 000 répétitions par dose, 4 processus, les gardes (section 6), le lecteur gelé et ses pièces (mêmes empreintes que le v1), la commande de lecture à ses chemins près (`--duree-max-attendue 6700` inchangé), ce qui est rapporté (section 5).

**Statut : v2 scellée ; texte du brouillon 1 (`epreuve-w2g-dose-v2-brouillon1.md`, sha256 `6330c2ba8a2cdf96a7763197c3ef24dca9481944425491c2916634ccd14ab07e`, R-1947) contre-lu par un autre modèle (`contre-lecture-epreuve-w2g-dose-v2-v1.md` : 0 bloquant, 0 majeur, 9 mineurs) ; mineurs traités par la mère au scellement (annexe D) ; aucun marqueur.** Nom proposé pour la version scellée : `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/epreuve-w2g-dose-v2-v1.md`, compagnon `epreuve-w2g-dose-v2-v1.md.sha256` écrit par `python -m controle_ia.scellement sceller` (format « empreinte, deux espaces, nom », lu par `pole/outils.verifier_scelle`). Le dossier, la console et la lecture gardent le préfixe `epreuve-w2g-dose-v1` (nom de l'épreuve, du script et du champ `epreuve`, inchangés) avec le suffixe neuf `-rejeu-v2`. **Un scellement, un rejeu, une lecture.**

Rédigé le 8 novembre 2026 vers 23:30 UTC (heures par `date -u`) par un rédacteur neuf de la session mère `session_016QhUrrLeN21G7Z9KZobE42` (Opus 5.5), qui n'a écrit ni le v1, ni ses brouillons, ni le code v5, ni le lecteur, ni l'épreuve exploratoire, ni le rejeu v1. Aucun appel de modèle, aucune clé, aucun réseau, aucune dépense, aucun commit ; aucun fichier existant modifié ; rien lu sous `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`. **De la trace v1, ce rédacteur n'a lu que la lecture d'arrêt** (`epreuve-w2g-dose-v1-rejeu-v1-lecture-v1.json`) et les empreintes des fichiers ; ni la table, ni le fichier de résultats, ni le manifeste, ni la console du rejeu v1. Gestes faits : lecture du v1, de R-1946 et de la lecture d'arrêt ; `sha256sum` du v1 et des pièces de la trace v1 (égales aux empreintes de R-1946 et de la lecture d'arrêt) ; préparation d'une copie de travail neuve selon le préalable 3 (sept lignes « ?? », dix empreintes égales) ; lecture des arguments du script (l. 160–260) et de `lire_code_console` du lecteur (l. 168–174) ; **deux essais de durée** (ci-dessus), et aucun autre calcul ; copie supprimée.

## Ce qui change du v1 au v2

| endroit | v1 | v2 | pourquoi |
|---|---|---|---|
| en-tête | — | motif de la v2, cause mesurée, remède | trace v1 arrêtée (R-1946) |
| section 3 bis (neuve) | — | information préalable : la trace v1 arrêtée, ses empreintes, ce qui en a été vu ; jamais combinée, jamais lue pour choisir | déclaration de R-1946 (R4) |
| section 4, « Entropie » | empreinte du v1 | marqueur ; empreinte du **v2 scellé**, donc entropie neuve | v1 section 6 : texte neuf, entropie neuve |
| section 4, « Processus » | « un fil par cœur » (supposé) | un fil de calcul par processus, imposé ; mesure des deux essais | cause de l'arrêt |
| section 4, « Durée attendue » | ≈ 4 500 s | ≈ 1 150 s | mesure à 4 processus, un fil |
| section 4, « Durée maximale » | 6 700 s ; `timeout 7000` ; outil 7 200 s | **inchangée** ; motif écrit | marge × 5,8 sur l'attendu ; plus haut impossible sous 7 000 |
| section 4, préalables 3 et 5 | copie `…-rejeu-v1-copie` ; charge < 1,0 | copie `…-rejeu-v2-copie` ; charge < 1,0 et un fil par processus dans la commande | noms neufs ; remède |
| section 4, commande | noms `…-rejeu-v1`, texte v1 | noms `…-rejeu-v2`, texte v2, les quatre variables à 1, ligne « fils de calcul » et charge de fin à la console | noms neufs ; remède ; trace du remède |
| section 4 bis | console de lecture `…-rejeu-v1-lecture-v1-console.txt` | `…-rejeu-v2-lecture-v1-console.txt` ; `--duree-max-attendue 6700` inchangé | noms neufs |
| section 6, deux derniers paragraphes | « aucun texte v2 » ; tentative suivante `…-v2`, `…-rejeu-v2` | « aucun texte v3 » ; tentative suivante `…-v3`, `…-rejeu-v3` ; trace v1 jamais complétée | cohérence des noms |
| section 7 | contre-lecture du v1 | contre-lecture du v2 à faire (fichiers à donner, points à vérifier) | R2 |
| annexe A ; sources | marqueur levé ; sources du v1 | marqueur restant ; sources ajoutées | — |
| sections 1, 2, 3, 5, 6 (gardes 1 à 6, « ce qui n'est pas un arrêt »), 6 bis, 6 ter ; section 4 : « Grille », pièces gelées, préalables 1, 2, 4, 6, sorties et codes du script ; section 4 bis à ses noms près ; annexes B, C | — | **mot pour mot** | non touchés par l'arrêt |

L'historique des brouillons du v1 (table « Ce qui change du brouillon 1 au brouillon 2 ») reste au v1 scellé ; les renvois M-1 à M-4 et m-5 à m-15 du présent texte s'y lisent.

## 1. Objet

Choisir **λ\***, la dose du monde W2 gradué (W2g) de l'attaque A1-v4, par une **règle mécanique** écrite avant toute épreuve. Ce n'est **pas** une expérience décisive : aucune hypothèse n'est tranchée ici. Mais le choix de la dose **conditionne la course décisive** : λ\* remplit le marqueur `DOSE_LAMBDA` (entre doubles chevrons) du préenregistrement (brouillon 3, l. 288 : « dose λ\* fixée par le texte scellé et la sortie de l'épreuve hors ligne « W2 gradué » […] ; sans λ\*, le texte n'est pas scellable »), et les lectures 2′ à 5′ et les prédictions P7 à P11 se lisent à cette dose (brouillon 3, l. 71, 115–119). D'où ce texte, contre-lu et scellé avant le rejeu (brouillon 3, l. 262 : « texte court écrit, contre-lu, scellé, joué (0 USD) »), comme un préenregistrement (R1, R2).

## 2. Règle de choix (recopiée telle quelle, non modifiée)

Brouillon 3 (`preenregistrement-attaque-goodhart-v4-brouillon3.md`, sha256 `c44f52cc0fa53e1bbd621c56a06f6c65860487fc6afe30d52ed2d6b81adc8dac`), l. 126 ; première rédaction le 8 novembre entre 16:34 et 16:48 UTC, version portant cette empreinte **rendue à 17:00 UTC** (R-1897, `registres/decisions.md`, au 8 novembre), **avant toute épreuve** (la première épreuve, coupée, part à 17:19 UTC ; rapport du code v5, l. 59) :

> « la plus petite dose de la grille de l'épreuve à laquelle la **loi du monde** (avec N) est promue par le v9 avec une probabilité ≥ 0,80 sur 1 000 répétitions **et** la recombinaison pure S1, S2 n'est jamais promue sous v9 (0 sur 1 000) ; si aucune dose de la grille ne satisfait les deux, le texte n'est pas scellable et Lazar décide (annexe B, point 5). »

Ce texte fixe seulement ce que la règle laisse ouvert, sans en changer le sens :
- **grille de l'épreuve** = la grille gelée `GRILLE_DOSES_W2G` du code v5 (`pole/attaque_goodhart_v5.py` l. 74), **11 doses dont 0,0** : 0 ; 0,05 ; 0,10 ; 0,15 ; 0,20 ; 0,25 ; 0,30 ; 0,40 ; 0,50 ; 0,75 ; 1. La dose 0 est jouée comme **contrôle** et n'est **jamais choisissable** (λ\* > 0, brouillon 3 l. 71 ; `verifier_plan` du cœur v5, l. 457–458, la refuse en course). `choisir_dose` du script de l'épreuve **ne l'exclut pas** (il parcourt toutes les doses complètes, l. 142–147) ; le recalcul du lecteur l'**exclut** (`lambda_recalcule` : doses > 0 seulement) ; la garde 5 arrête si (a) ou (b) > 0 à la dose 0, et la garde 6 arrête si le script propose la dose 0 (§ 6) ;
- **« probabilité ≥ 0,80 sur 1 000 répétitions »** = fréquence observée : promues(a) / 1 000 ≥ 0,80, soit **au moins 800 sur 1 000** ; c'est ce qu'applique `choisir_dose` (`taux ≥ SEUIL_PROMOTION_MONDE`, l. 139–148), écrit avant l'épreuve exploratoire, et ce que recalcule le lecteur en entiers (5 × promues(a) ≥ 4 × n) ;
- **« jamais promue (0 sur 1 000) »** = promues(b) = 0 (`PROMOTIONS_RECOMBINAISON_MAX = 0`, l. 54) ; les deux conditions à la **même** dose ; seules les doses complètes (1 000 répétitions) comptent ;
- **aucune dose ne satisfait** → **pas de λ\***, le préenregistrement reste non scellable, **nœud de Lazar**.

**Variante envisagée et écartée.** Le rapport du code v5 (réserve 2 bis, l. 82) propose une règle sur la **borne basse** de l'intervalle (≥ 0,80), qui donnerait **une autre dose** (0,50 au lieu de 0,40 sur les chiffres exploratoires). Elle a été proposée **après lecture des chiffres exploratoires** ; elle est **écartée pour cette raison** (R1, R4 ; décision de la mère R-1923, `registres/decisions.md`, au 8 novembre : « la règle de choix reste celle du brouillon 3, écrite avant […], non modifiée après lecture »). Le fait qu'à 1 000 répétitions une dose « juste au-dessus » de 0,80 ne se distingue pas d'une dose juste en dessous est **rapporté** (section 5), il ne change pas la règle.

## 3. Déclaration d'information préalable (ce qui a été vu)

Une **épreuve exploratoire non scellée** a été jouée le 8 novembre (rapport du code v5, `code-v5/rapport-code-v5-w2g-v1.md`, sha256 `c31d23b84e8406aeef1b72f2146065c854b29ee5c7cd2c84e441eaa9c8fa77a1`, section 5 ; R-1923) : graine exploratoire **20261108** (espace < 2⁶⁴), 2 processus, script `epreuve_w2g_dose_v1.py` `c691a43d…` et cœur `attaque_goodhart_v5.py` `8692746a…` (empreintes du manifeste, égales aux fichiers livrés), **grille réduite choisie après un pilote** vu : doses 0,30 ; 0,40 ; 0,50 ; 0,75 à 1 000 répétitions (18:19 à 19:13 UTC, 3 219,4 s), puis la dose 0 à 200 répétitions (193,0 s). Comptes recopiés des sorties (vérifiés sur les fichiers ci-dessous) ; Wilson à 95 % calculé par le rédacteur du brouillon 1 avec `attaque_goodhart_v2.wilson` (l. 750) et recalculé par le contre-lecteur (quatorze valeurs concordantes) ; Clopper-Pearson de (a) tel qu'imprimé par le script.

| dose | écart moyen (nats) | (a) monde sous v9 | (a) Wilson | (a) Clopper-Pearson | (b) recombinaison sous v9 | (c) recombinaison sous v8 | (d) monde sous v8 |
|---|---|---|---|---|---|---|---|
| 0 (200 rép.) | 0,0 | 0/200 | [0,000 ; 0,019] | [0,000 ; 0,015] | 0/200 [0,000 ; 0,019] | 200/200 [0,981 ; 1,000] | 200/200 [0,981 ; 1,000] |
| 0,30 | 0,112479 | 641/1 000 | [0,611 ; 0,670] | [0,615 ; 0,666] | 0/1 000 [0,000 ; 0,004] | 762/1 000 [0,735 ; 0,787] | 992/1 000 [0,984 ; 0,996] |
| 0,40 | 0,169507 | 809/1 000 | [0,783 ; 0,832] | [0,787 ; 0,829] | 0/1 000 [0,000 ; 0,004] | 621/1 000 [0,591 ; 0,651] | 990/1 000 [0,982 ; 0,995] |
| 0,50 | 0,233694 | 890/1 000 | [0,869 ; 0,908] | [0,872 ; 0,906] | 0/1 000 [0,000 ; 0,004] | 499/1 000 [0,468 ; 0,530] | 992/1 000 [0,984 ; 0,996] |
| 0,75 | 0,425176 | 965/1 000 | [0,952 ; 0,975] | [0,954 ; 0,974] | 0/1 000 [0,000 ; 0,004] | 311/1 000 [0,283 ; 0,340] | 997/1 000 [0,991 ; 0,999] |

Règle appliquée par le script sur cette grille réduite : λ\* imprimé **0,40**. Aucune évaluation impossible, aucune loi du monde refusée par la grammaire servie.

Fichiers (dossier `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/code-v5/`, `sha256sum` relevé le 8 novembre à 19:24 UTC, égal au rapport l. 109–114) :

| fichier | sha256 |
|---|---|
| `epreuve-w2g-dose-v1-exploratoire-doses-030-075.json` | `c85e59b3594050e6c7ce162721e42c19b55d890acd752ef39b268617b279b2b9` |
| `epreuve-w2g-dose-v1-exploratoire-doses-030-075-table.txt` | `91b06e77b36bdadaaf84d9b302bda859e486710073a9f675323f2808e017fe96` |
| `epreuve-w2g-dose-v1-exploratoire-dose-000.json` | `a4821262e5b9507d4275c81050af2034b3f9bdb0364b97513d30bdf2cb56748e` |
| `epreuve-w2g-dose-v1-exploratoire-dose-000-table.txt` | `30b5736fba7d3e13f65ff7562474ede92caf47ef6bf5e7b7822bf0e9193569af` |
| `epreuve-w2g-dose-v1-pilote-vitesse-table.txt` | `30c09d3392e5b6e8ab509f790574cc11c77a3162d494ea1659e51f11f7efb2a2` |
| `epreuve-w2g-dose-v1-sortie-console.txt` | `85506f1cb51ab373e1e92fa3e8fe84b0fdaa8019c1a0da4d7698c99dbcca15c7` |

Les compagnons d'origine (dossier de brouillon `…/scratchpad/epreuve-w2g-v1-a/`) se vérifient (`sha256sum -c` : OK pour la sortie, la table et le manifeste de la grille réduite).

Vus aussi : le **pilote de vitesse** (graine 5, 50 répétitions, doses 0,10 et 0,50 : (a) 5/50 et 43/50 ; (b) 0/50 ; (c) 0,900 et 0,480 ; (d) 0,940 et 1,000), vu **avant** le choix de la grille réduite ; une **première épreuve** sur la grille entière, coupée par le délai externe à 18:17 UTC (code 124) **sans sortie** (son dossier de brouillon ne contient qu'un manifeste, non lu par le rédacteur du brouillon 1) ; la recommandation « borne basse » du rapport (section 2). Ont vu ces chiffres : le développeur du code v5, la mère, le rédacteur du brouillon 1, le contre-lecteur, le développeur du lecteur (les sorties exploratoires sont des artefacts de ses essais), ce rédacteur.

**Usage** : ces chiffres servent **à information seulement**. Ils ne fixent ni la règle, ni la grille, ni le nombre de répétitions, ni aucun seuil ; ils ne départagent rien ; ils ne sont **jamais combinés** à ceux du rejeu (ni sommés, ni moyennés, ni pris pour confirmer une dose). Les cartes du rejeu sont neuves (entropie neuve, section 4) : aucune répétition n'est commune.

## 3 bis. Information préalable : la trace v1 arrêtée (ce qui a été vu)

**Trace.** Rejeu v1 lancé sous le texte scellé `epreuve-w2g-dose-v1-v1.md` (`3415f70d…`), entropie = empreinte de ce texte, grille entière, 1 000 répétitions, 4 processus, `--duree-max-s 6700` sous `timeout 7000` ; script au **code 3** à 23:16:51 UTC après 6 702,2 s ; lecteur gelé (`a9f462cb…`) au **code 2, arrêt de garde 2**, seule garde refusée (`gardes_refusees` = [2]) : `code_3`, `arret` (« dose 1.0 : durée maximale dépassée à la répétition 447 »), `dose_incomplete` (dose 1,0 : 350 répétitions sur 1 000, `complete` = faux) ; aucun λ\* (R-1946). Fichiers, sous `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/` (`sha256sum` relevé par ce rédacteur le 8 novembre à 23:18 UTC, égal à R-1946 et aux pièces de la lecture d'arrêt) :

| fichier | sha256 |
|---|---|
| `epreuve-w2g-dose-v1-rejeu-v1/epreuve-w2g-dose-v1.json` (sortie) | `a475472382fe6327626e1d5b5e59c1efc29c92690e5c49f17d26d60a61df3980` |
| `epreuve-w2g-dose-v1-rejeu-v1/manifeste.json` | `c6de942f8be0f84733ed6b2cec4d8750f1088041372de5020520297ff845e497` |
| `epreuve-w2g-dose-v1-rejeu-v1/epreuve-w2g-dose-v1-table.txt` | `94815f644112e0d8158b2de9cf7fb7355cdcc6b27a1d3291fa6ac4d85325c256` |
| `epreuve-w2g-dose-v1-rejeu-v1-console.txt` | `9bc837912dbc43a6c82607252bcc32dcd45205b471e27a9ebbb8e39d16d7b755` |
| `epreuve-w2g-dose-v1-rejeu-v1-lecture-v1.json` (lecture d'arrêt) | `37b4d34de2a4b1437e064c3a37735b41ea0c458f8ef9612ad4e649a689fa6aca` |
| `epreuve-w2g-dose-v1-rejeu-v1-lecture-v1-console.txt` | `47d05d30f3e1c15ca6a42d7976cfb05002c678b3f57905f90f50069708549bc9` |

**Ce qui a été vu (déclaration, R4 ; R-1946).** La mère, en relevant la fin de la console du rejeu v1 pour y lire le code, a vu **les dernières lignes de la table de la trace arrêtée (doses 0,40 à 1,00)**. La lecture d'arrêt, elle, n'écrit ni table ni intervalle (section 4 bis). Le rédacteur de ce brouillon n'a lu que la lecture d'arrêt et les empreintes ; ni la table, ni la sortie, ni le manifeste, ni la console de la trace v1. Le contre-lecteur du v2 reçoit la lecture d'arrêt, **pas** la table, la sortie ni la console de la trace v1 (section 7).

**Usage.** Les chiffres de la trace v1 arrêtée ne servent à rien : ils ne fixent ni la règle, ni la grille, ni le nombre de répétitions, ni aucun seuil ; ils ne départagent rien ; ils ne sont **jamais combinés** à ceux du rejeu v2 (ni sommés, ni moyennés, ni pris pour confirmer une dose) et **jamais lus pour choisir** une dose ; la trace n'est jamais complétée (section 6). Les cartes du rejeu v2 sont neuves (entropie de l'empreinte du v2 scellé, section 4) : aucune répétition n'est commune aux deux rejeux. Seuls la durée (6 702,2 s) et le nombre de répétitions achevées (10 350 : dix doses complètes, la dose 1,0 à 350, selon les motifs de la lecture d'arrêt) servent, **pour la durée attendue seulement** (section 4), comme recoupement de la mesure de vitesse ; aucun compte de promotion n'y entre.

## 4. Rejeu

**Grille** : la grille gelée entière, 11 doses (0 ; 0,05 ; 0,10 ; 0,15 ; 0,20 ; 0,25 ; 0,30 ; 0,40 ; 0,50 ; 0,75 ; 1), **en un seul appel** (option `--doses` omise : le script prend alors `GRILLE_DOSES_W2G`, l. 67–69, 175). **1 000 répétitions à chaque dose, dose 0 comprise** : le script n'a qu'un nombre de répétitions par appel (`--repetitions`, l. 173, 208–209) ; il ne fait pas 200 répétitions à la dose 0 dans le même appel. Plutôt qu'un second appel (deux sorties, deux lectures), la dose 0 est jouée à 1 000 dans le même appel : 1 000 × 1,93 ≈ **1 930 secondes-processus** pour la dose 0, soit ≈ 1 540 de plus qu'à 200 répétitions.

**Entropie** : levée retenue (R-1926 ; sans changement de code) : l'entropie est l'entier gros-boutiste de l'empreinte SHA-256 du **présent fichier scellé**, lue par le mode décisif du script `--entropie-texte CHEMIN` (l. 172, 188–192 : refus si le compagnon `.sha256` manque ou ne correspond pas ; `verifier_entropie(…, decisif=True)` refuse toute entropie < 2⁶⁴, donc la graine exploratoire 20261108). L'empreinte n'existe qu'au scellement : elle est **fixée par le scellement** et **neuve** par construction, donc **différente de celle du v1** (`3415f70d8690708b4c7c558420c8c19ead1a211d68be277050c46d0ca8b21122`) : aucune carte du rejeu v2 n'est une carte de la trace v1 arrêtée. Toutes les graines en dérivent par `numpy.random.SeedSequence(entropie, spawn_key=(clé de l'étiquette, indices…))` (`attaque_goodhart_v2.graine`, l. 104–108, R9) : cartes par `carte_w2g(entropie, r, dose)` (étiquettes « monde|W2g », « developpement|W2g », indice r), juge par les étiquettes « epreuve-w2g|<loi>|<juge>|dose=<λ> », indices (r, 1) ; la carte r est la même à toutes les doses (plan apparié en λ). Cette entropie est distincte de celle de la course décisive (empreinte du préenregistrement scellé) : les cartes de l'épreuve ne sont pas celles de la course.

**Processus** : 4 (`nproc` = 4 le 8 novembre ; 4 cœurs, un fil matériel par cœur), et **un fil de calcul par processus** pour les bibliothèques numériques : `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1`, posées dans la commande exacte (ci-dessous) ; `python3 -I` ignore les variables propres à Python, pas celles-ci, et les processus de calcul, créés par `fork` (l. 219), les héritent. Le v1 supposait « un fil par cœur » ; c'était faux : numpy 2.5.3 est lié à OpenBLAS 0.3.34 (`numpy.show_config()`), qui lance par défaut un fil par cœur **dans chaque processus**, soit seize fils pour quatre cœurs (charge vers 13,8 au rejeu v1, R-1946). Le script et le cœur ne sont pas modifiés ; les empreintes des modules (préalable 3) et les pièces gelées sont celles du v1.

**Mesure** (rédacteur de ce brouillon, 8 novembre, 23:19 à 23:25 UTC ; copie de travail neuve `…/scratchpad/epreuve-w2g-dose-v2-mesure-fils-copie`, préparée comme au préalable 3, supprimée ensuite ; charge sur une minute < 1,0 au départ de chaque essai ; `nice -n 10`, mode exploratoire `--graine 11`, `--doses 0.5 --repetitions 200 --processus 4 --duree-max-s 1700`, sorties non ouvertes au-delà de la ligne de durée du script, puis supprimées) :
- **sans variable** : 126,4 s (durée imprimée par le script), code 0 ; 4 fils par processus de calcul (`ps -o nlwp`, toutes les 20 s) ; moyenne de charge sur une minute 0,86 au départ, 4,86 ; 7,16 ; 9,21 ; 11,06 ; 11,44 ; 11,79 aux relevés successifs (elle monte encore : l'essai, 140 s, est plus court que la convergence de la moyenne), 14 à 17 fils prêts à tourner ;
- **avec les quatre variables à 1** : 20,1 s, code 0 ; 1 fil par processus de calcul ; charge 0,96 au départ, 1,95 au seul relevé (20 s), 2 fils prêts à tourner ;
- les deux tables écrites ont la **même empreinte** (`sha256sum`, sans ouvrir les fichiers) : mêmes comptes et mêmes valeurs imprimées, aucune différence détectée (pas une preuve d'identité bit à bit).

Soit 0,632 s par répétition sans variable (2,53 secondes-processus) et 0,1005 s avec (0,40 secondes-processus), **rapport 6,3**. Recoupement : la trace v1 arrêtée (sans variable, grille entière) a achevé 10 350 répétitions en 6 702,2 s, soit 0,648 s par répétition, à 3 % de la mesure sans variable (section 3 bis). Les 1,61 secondes-processus de l'épreuve exploratoire (2 processus, donc huit fils pour quatre cœurs) étaient vraisemblablement déjà gonflées par le même surnombre (non mesuré) ; l'échelle supposée linéaire au v1 de 2 à 4 processus ne l'était pas (1,61 puis 2,53 secondes-processus).

**Durée attendue** : par la mesure, 11 000 × 0,1005 ≈ 1 106 s ; par le recoupement, 6 702,2 × (11 000 / 10 350) × (20,1 / 126,4) ≈ 1 133 s ; retenue **≈ 1 150 s (≈ 19 min)** sur 4 processus (la dose 0, plus lente d'environ 1,2 fois à l'exploratoire, ajoute une vingtaine de secondes). Réserves : mesure sur une seule dose (0,5), 200 répétitions, un essai de chaque sorte ; machine partagée avec d'autres sous-agents de la session (préalable 5). Le brouillon 3 (l. 256 : « 29 à 58 min sur un cœur ») reste à corriger au brouillon 4.

**Durée maximale** : `--duree-max-s 6700` **inchangée** (marge × 5,8 sur l'attendu), sous un délai externe `timeout 7000` (300 s de marge pour l'arrêt propre et l'écriture : chaque processus relit l'horloge à chaque répétition, l. 82, les lots non commencés sont annulés, l. 227–228, l'arrêt prend quelques secondes), la commande étant lancée en arrière-plan avec un délai d'outil de 7 200 s. Ordre : 6 700 < 7 000 < 7 200. **Motif** : la valeur la plus haute qui tienne sous ces deux bornes, déjà gelée au lecteur et au v1 ; la grille entière y tient avec le remède (≈ 1 150 s) ; ne pas la changer laisse la commande de lecture et la garde 3 (`duree_max`) telles quelles. Si le remède n'agissait pas, la grille demanderait ≈ 7 000 s (11 000 × 0,632) et s'arrêterait de nouveau ; la console porte alors la ligne « fils de calcul » et la charge de fin pour le diagnostic. Elle est passée telle quelle au lecteur (`--duree-max-attendue 6700`, garde 3).

**Pièces gelées** (M-2 ; fichiers sous `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/code-v5/` ; rendus le 8 novembre, R-1928) :

| pièce | chemin | sha256 |
|---|---|---|
| lecteur | `orchestrator/demonstrations/lecture_epreuve_w2g_dose_v1.py` | `a9f462cb73b99680ed82ca8bc41b3241cd5b29591e5978044185786ab8467c71` |
| essais du lecteur | `orchestrator/essais/test_lecture_epreuve_w2g_dose_v1.py` | `6f5d3b6165679ba2f364010ee94350b548cceac56c793c31f92b6b82ba1cec2e` |
| patch du lecteur (s'applique après le patch v5 sur `8947bc80…`) | `patch-public-code-v5-lecture-v1.diff` | `26a37cd82ca4a2f2139626fc7bc6c4f714f7d2916635b59f49704c6a1f097d3f` |
| sortie des essais (43 passés, 0 échec, 0 sauté) | `essais-lecture-v1-sortie.txt` | `e2ada8918770be5f52dcfc623156bba655d539b4df4c47b6359f79e6a097ead1` |

Ces pièces ne sont **plus modifiées** à partir du scellement du présent texte. Toute correction ultérieure suit la section 6 bis.

**Préalables** (dans l'ordre ; un seul manque : rien ne part) :
1. ce texte scellé, contre-lu (section 7), `sha256sum -c` OK sur son compagnon ; **une ligne du registre des décisions écrite avant le lancement**, portant l'empreinte du texte scellé **et** les quatre empreintes des pièces gelées ci-dessus ;
2. dossier de sortie, console et lecture **absents** : `test ! -e "$DOSSIER" && test ! -e "$CONSOLE" && test ! -e "$LECTURE" && test ! -e "$CONSOLE.sha256" && test ! -e "$LECTURE.sha256"` (chemins de la commande ci-dessous) ;
3. copie de travail neuve, sans toucher au dépôt public :
   ```
   COPIE=/tmp/claude-0/-home-user/86976e6f-3fae-57b1-a905-26802f445363/scratchpad/epreuve-w2g-dose-v1-rejeu-v2-copie
   PATCH=/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/code-v5/patch-public-code-v5.diff
   PATCH_LECTURE=/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/code-v5/patch-public-code-v5-lecture-v1.diff
   test ! -e "$COPIE" && mkdir "$COPIE" && git clone -q --no-hardlinks /home/user/ideation-organism "$COPIE/ideation-organism"
   cd "$COPIE/ideation-organism" && git checkout -q --detach 8947bc80a5c2fee0cfee4f3cafbdaaca8ed77f3e
   sha256sum "$PATCH" "$PATCH_LECTURE"   # attendus 12c39347e47fec599da21ef00f8d0534b661d2dd982b7f8c7ca9ac2169a660d2 et 26a37cd82ca4a2f2139626fc7bc6c4f714f7d2916635b59f49704c6a1f097d3f
   git apply --check "$PATCH" && git apply "$PATCH"
   git apply --check "$PATCH_LECTURE" && git apply "$PATCH_LECTURE"
   git rev-parse HEAD ; git status --porcelain   # exactement sept lignes « ?? » : les cinq fichiers v5 et les deux du lecteur
   ```
   puis, depuis `orchestrator/`, les empreintes des huit modules que le manifeste du script relève (`MODULES`, l. 58–60), égales à : `pole/attaque_goodhart_v5.py` `8692746a1b02b15465062423d1f05e2084ce1d1861c979316ce1a5ef4384ba15` ; `pole/attaque_goodhart_v4.py` `0077a6470781b8cd9e0599232ddd52e3601c8c4c8735a5cfcf817800bda3bb5c` ; `pole/attaque_goodhart_v2.py` `3c9de8b83b6fcf198d12cacf6a6738c2fc3fe4ade9391f943b3924592959e703` ; `pole/nul_v9.py` `7ae450df2482246122bf9fbcf0fa5ef30b4a7e4c6f0d09531e83af048e46ee95` ; `demonstrations/banc_tricheurs_v9.py` `7e4bff5995df2a7d62a4f5a2f5f9176da614e657a55b05183325fa2fc6e24e44` ; `demonstrations/banc_tricheurs_v8.py` `0be47e4b5916a98499faf9c40d65369b41e3a5463d7ab444ed18ba18bba08c03` ; `demonstrations/banc_tricheurs_v7.py` `ef016d250b7b503f705dc95919719c68c8f968534fd901df7364a6062d67cf12` ; `demonstrations/epreuve_w2g_dose_v1.py` `c691a43d9905e91a0ba91ddfef785e53a091768fa7dcd3007f03066aeef10dda` (celles de l'épreuve exploratoire ; ce sont aussi les constantes `MODULES_SHA256` du lecteur, comparées par ce rédacteur : égales) ; et les deux fichiers du lecteur, égaux aux pièces gelées : `demonstrations/lecture_epreuve_w2g_dose_v1.py` `a9f462cb…`, `essais/test_lecture_epreuve_w2g_dose_v1.py` `6f5d3b61…` (répétition du rédacteur du v1, vers 19:49 UTC, puis du rédacteur du présent brouillon, à 23:18 UTC, dans une copie neuve `…/scratchpad/epreuve-w2g-dose-v2-mesure-fils-copie` supprimée ensuite : sept lignes, dix empreintes égales, `python3` 3.13.18, numpy 2.5.3) ;
4. `python3` 3.13.18 et numpy 2.5.3 (ceux de l'épreuve exploratoire, et les constantes `PYTHON`, `NUMPY` du lecteur) ;
5. charge de la machine relevée (`cat /proc/loadavg`) : moyenne sur une minute **< 1,0**, et aucun autre calcul long lancé par la session pendant la fenêtre (la mère s'en assure) ; **un fil de calcul par processus** pour les bibliothèques numériques : les quatre variables sont posées **dans la commande elle-même** (ci-dessous), et non dans l'environnement de la session ; la console en porte la ligne « fils de calcul » et la charge relevée à la fin (information, pas une garde) ;
6. le lecteur et ses essais tels que gelés (tableau ci-dessus), essayés sur leurs cas sains et leurs artefacts (section 6 ter : 43 essais passés, 0 échec, 0 sauté) ; aucun changement depuis l'inscription du préalable 1.

**Commande exacte** (aucune instance louée, 0 USD) :
```
COPIE=/tmp/claude-0/-home-user/86976e6f-3fae-57b1-a905-26802f445363/scratchpad/epreuve-w2g-dose-v1-rejeu-v2-copie
DOSSIER=/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/epreuve-w2g-dose-v1-rejeu-v2
TEXTE=/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/epreuve-w2g-dose-v2-v1.md
CONSOLE=/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/epreuve-w2g-dose-v1-rejeu-v2-console.txt
LECTURE=/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/epreuve-w2g-dose-v1-rejeu-v2-lecture-v1.json
cd "$COPIE/ideation-organism/orchestrator" && \
{ date -u; cat /proc/loadavg; echo "fils de calcul : OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1"; } > "$COPIE/console-rejeu-v2.txt" && \
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1 \
timeout 7000 nice -n 10 python3 -I -B demonstrations/epreuve_w2g_dose_v1.py "$DOSSIER" \
    --entropie-texte "$TEXTE" --repetitions 1000 --processus 4 --duree-max-s 6700 \
    >> "$COPIE/console-rejeu-v2.txt" 2>&1 ; echo "code $?" >> "$COPIE/console-rejeu-v2.txt" ; \
{ date -u; cat /proc/loadavg; } >> "$COPIE/console-rejeu-v2.txt"
```
Sorties, **scellées par le script à l'écriture** (`ecrire_json_scelle`, `ecrire_scelle` : compagnons `.sha256`, refus d'écraser) dans le dossier neuf `epreuve-w2g-dose-v1-rejeu-v2/` : `manifeste.json` (avant la première répétition : mode, entropie, texte et son empreinte, grille, répétitions, processus, durée maximale, règle, versions, empreintes des modules, règle des graines), `epreuve-w2g-dose-v1.json`, `epreuve-w2g-dose-v1-table.txt`. Codes du script : 0 complet ; 3 arrêt à la durée maximale (sortie écrite, `arret` non nul) ; 2 refus avant toute répétition (rien d'écrit) ; 124 délai externe (sortie en général absente).

**Console** (m-14) : recopiée **à côté du dossier de sortie, non dedans**, sous `$CONSOLE` (chemin complet ci-dessus), puis scellée :
```
test ! -e "$CONSOLE" && cp "$COPIE/console-rejeu-v2.txt" "$CONSOLE" && cmp "$COPIE/console-rejeu-v2.txt" "$CONSOLE" && \
cd /home/user/controle-ia-travail && PYTHONPATH=src python -m controle_ia.scellement sceller "$CONSOLE"
```
Le lecteur la lit pour le code de sortie : exactement une ligne « code N » exigée (garde 1). Les lignes ajoutées au v2 (« fils de calcul : … », charge de fin) ne commencent pas par « code » : le lecteur gelé ne les compte pas (`lire_code_console`, l. 172 : lignes commençant par « code » suivi d'un entier).

## 4 bis. Lecture : commande exacte et codes de sortie

**Commande exacte**, une seule fois, dans la même copie de travail, après le scellement de la console (mêmes variables qu'en section 4) :
```
cd "$COPIE/ideation-organism/orchestrator" && \
python3 -I -B demonstrations/lecture_epreuve_w2g_dose_v1.py "$DOSSIER" \
    --texte "$TEXTE" --console "$CONSOLE" --lecture "$LECTURE" \
    --duree-max-attendue 6700 --repetitions-attendues 1000 --processus-attendus 4 \
    > "$COPIE/console-lecture-v2.txt" 2>&1 ; echo "code $?" >> "$COPIE/console-lecture-v2.txt"
```
La lecture (`$LECTURE`, compagnon `.sha256` écrit par le lecteur, refus d'écraser) porte en tête le chemin et l'empreinte du lecteur lui-même, les paramètres, les valeurs attendues de la section 4, et les chemins et empreintes des cinq pièces lues (sortie, manifeste, table, console, texte). La console de la lecture est recopiée et scellée comme celle du rejeu, sous `…/epreuve-w2g-dose-v1-rejeu-v2-lecture-v1-console.txt`. `--duree-max-attendue 6700` est inchangé : la durée maximale du rejeu est inchangée (section 4).

**Codes de sortie du lecteur et ce que chacun entraîne** :
- **0** — gardes 1 à 6 passées, λ\* recalculé égal au λ\* imprimé par le script : **λ\* est lu et définitif** (section 6, « Une sortie complète fixe λ\* ») ; il remplit le marqueur `DOSE_LAMBDA` du préenregistrement (brouillon 4) par la main de la mère.
- **3** — gardes passées, **aucune dose** de la grille ne satisfait la règle : pas de λ\*, **définitif** aussi ; le préenregistrement reste non scellable ; **nœud de Lazar** (annexe B du brouillon 3, point 5).
- **2** — **arrêt de garde** : pas de λ\* ; motifs nommés à l'erreur standard ; une lecture « arrêt de garde » est écrite et scellée, sans table ni intervalle (seuls les détails des motifs peuvent porter un compte, écart 4, annexe C) ; la trace est rapportée telle quelle, aucun chiffre n'en est lu pour choisir une dose. Suite selon la garde la plus petite qui refuse : gardes 1 à 4 → la trace est **arrêtée ou refusée** : une nouvelle tentative demande un texte neuf (section 6) ; gardes 5 et 6 (défaut du certificat ou de l'instrument) → rapport et **nœud de Lazar** avant tout texte neuf. Si la mère soupçonne un défaut du lecteur lui-même : section 6 bis.
- **4** — **usage refusé** (arguments, chemin de lecture déjà pris, ou lecture placée dans le dossier de sortie scellé) : rien n'est lu, rien n'est écrit ; ce n'est pas une lecture. Si la commande a été mal recopiée, elle est relancée **exactement** telle qu'écrite ci-dessus ; si `$LECTURE` existe déjà, une lecture a déjà eu lieu : elle fait foi, on n'en écrit pas d'autre (hors section 6 bis).
- Le code 1 (exception non prévue de Python) n'est jamais rendu volontairement : pas de λ\* ; traité comme un défaut du lecteur (section 6 bis).

## 5. Ce qui est rapporté

Lecture **après** le scellement de la sortie et de la console, par le lecteur gelé (section 4 bis), sans autre calcul :
- **par dose** (les 11) : (a) loi du monde sous v9, (b) recombinaison pure sous v9, (c) recombinaison pure sous v8, (d) loi du monde sous v8 : promues / 1 000, taux, **intervalle de Wilson à 95 %** (`attaque_goodhart_v2.wilson`, z = 1,959963984540054) ; Clopper-Pearson tel qu'imprimé par le script ; écart moyen ; médiane du logarithme de la richesse de (a) ; évaluations impossibles par ligne ; lois du monde refusées par la grammaire servie ; « complète » ;
- **λ\* imprimé par le script** (`dose_proposee_par_la_regle`) et le même λ\* recalculé par le lecteur depuis les comptes (dose > 0, au moins 800 sur 1 000 en (a), 0 en (b)) ; s'ils diffèrent : arrêt (garde 6) ;
- **issues attendues, acceptées d'avance** (M-1) : sur les chiffres exploratoires (0,809 en (a) à 0,40, 0,890 à 0,50, 0,641 à 0,30), le rejeu rendra vraisemblablement **0,40 ou 0,50** (la contre-lecture estime à environ 0,78 la probabilité que 0,40 passe 800 sur un tirage neuf ; information, non opposable). **L'une comme l'autre est λ\*, définitivement** ; et de même toute autre dose rendue, ou « aucune dose » ;
- si la borne basse de Wilson de (a) à λ\* est sous 0,80 : le lecteur écrit « λ\* à la limite » ; **λ\* ne change pas**. Cette mention va au brouillon 4 avec λ\* (lecture de P7 à cette dose, réserve déclarée), et **rien d'autre** : ni rejeu, ni changement de grille, ni de seuil, ni de règle (m-11) ;
- **analogue hors ligne de P10** (brouillon 3 l. 118 : taux(v8, témoin, 1) ≥ 0,50) : à λ\*, le taux (c) et son Wilson sont rapportés, avec la mention « **analogue de P10 ≥ 0,50** (recombinaison pure sous v8, soumise une fois par l'oracle) » si (c) ≥ 0,50, « **analogue de P10 < 0,50 à λ\*** » sinon ; **P10 n'est pas mesurée ici** (proposeur réel, condition témoin, 24 cartes en course). Le lecteur gelé imprime ces deux mentions sous les mots « P10 tenue par l'oracle » et « P10 en tension à λ\* » ; elles sont **recopiées dans le rapport sous les mots du présent texte**, la correspondance étant écrite ici, avant lecture (écart 1, annexe C). **Cette tension est rapportée ; elle ne change pas λ\*** ; elle va au brouillon 4 du préenregistrement (R-1923) ;
- **inversions de (a)** (m-15, information seulement) : le plan apparié en λ rend (a) croissante en espérance ; toute paire de doses voisines où (a) décroît **et** où les intervalles de Wilson de (a) imprimés par le lecteur ne se recouvrent pas est rapportée comme **réserve d'instrument** ; λ\* inchangé. Le lecteur ne fait pas cette comparaison : la mère la fait sur les intervalles de la lecture (`par_dose`), par simple comparaison des bornes écrites, sans aucun calcul neuf (écart 2, annexe C) ;
- **évaluations impossibles** (choix déclaré, avant lecture) : comptées par ligne et en total, **rapportées sans arrêt et sans seuil** — le lecteur gelé n'en fixe aucun, et ce texte n'en ajoute aucun : un seuil choisi maintenant serait un second jeu de règles hors du lecteur, et un seuil choisi après lecture est exclu (R1). Si le total est non nul, le lecteur écrit « audit écrit requis avant le report de λ\* au préenregistrement » : l'audit est écrit et rapporté **avant** que λ\* remplisse `DOSE_LAMBDA` ; **λ\* ne change pas**, quel que soit le compte. Si l'audit trouve un défaut de l'instrument : nœud de Lazar ; la mère ne substitue jamais une autre dose ni ne relance. La proposition de seuil de la contre-lecture (m-15 : arrêt au-delà de 10 sur 1 000 sur (a) ou (b)) est donc **écartée et déclarée** (R-1928 : « rapportées sans arrêt ») ;
- les chiffres exploratoires (section 3) peuvent être cités à côté, marqués « exploratoire, graine 20261108 », **jamais combinés** (le lecteur l'écrit dans `mention_exploratoire`).
λ\* ainsi obtenu remplit le marqueur `DOSE_LAMBDA` du préenregistrement ; « aucune dose » → nœud de Lazar.

## 6. Liste d'arrêt et gardes (R5 : chaque garde essayée sur un cas sain et un artefact avant le rejeu)

Les six gardes sont écrites **telles que le lecteur gelé les applique** (`lecture_epreuve_w2g_dose_v1.py`, `a9f462cb…` : fonctions `garde_1` à `garde_6`, motifs entre accents graves). Toute garde qui refuse : **arrêt sans λ\***, lecteur au code 2, sortie (ou trace partielle) scellée telle quelle et rapportée, aucun chiffre lu pour choisir une dose.

**Ordre d'application** : garde 1 **seule** d'abord (sans elle rien n'est lisible ; elle s'arrête à sa première étape en défaut, dont tous les motifs sont rapportés, dans l'ordre ; quand le texte n'est pas scellé, la garde 3 ne rend que le motif `texte_non_scelle` : présence, compagnons, lecture JSON et console, forme, table, code) ; puis les gardes **2, 3 et 4 ensemble** (forme et provenance, aucun compte de promotion lu : tous leurs motifs sont rapportés, la lecture d'arrêt nomme la plus petite garde qui refuse et la liste de toutes) ; puis la garde **5** ; puis la garde **6** (tous ses motifs rapportés).

1. **Sortie absente ou illisible** — `sortie_absente` : `epreuve-w2g-dose-v1.json`, `manifeste.json`, `epreuve-w2g-dose-v1-table.txt` ou la console absents ; `compagnon` : compagnon `.sha256` non conforme (`verifier_scelle` faux) sur l'un des quatre ; `illisible` : JSON non strict (NaN, infini, clé en double) ou console sans **exactement une** ligne « code N » ; `forme` : clés ou types inattendus (sortie : `epreuve`, `mode`, `entropie_racine`, `repetitions`, `doses`, `arret`, `resultats`, `regle_de_choix`, `dose_proposee_par_la_regle`, `table` ; manifeste : `reglages` ; chaque dose : `dose`, `repetitions`, `complete`, `lignes`, `ecart_kl_vers_w2_moyen`, `grammaire_servie_refusee` ; les quatre lignes (a) à (d), chacune avec `promues` entier dans [0 ; n], `repetitions` égal à celui de la dose, `taux` = promues / n, `evaluations_impossibles` dans [0 ; n], Clopper-Pearson à deux bornes, médiane de log W nombre ou nulle) ; `table` : table scellée différente de la table du JSON ; `code_de_sortie` : code de la console autre que 0, 3 ou 124 (un refus du script, code 2, n'écrit en pratique aucune sortie et tombe d'abord sur `sortie_absente`).
2. **Durée dépassée et totalité** (M-3) — `code_3` : code 3 à la console ; `delai_externe` : code 124 ; `arret` : champ `arret` non nul ; `dose_absente` : les doses de `resultats` ne sont pas exactement les 11 de `GRILLE_DOSES_W2G`, dans l'ordre (une dose jamais commencée est **absente** de la sortie d'`assembler`, non « incomplète ») ; `dose_manquante` : les doses de `resultats` ne sont pas celles du champ `doses`, dans l'ordre ; `dose_incomplete` : une dose non `complete`, ou dont `repetitions`, sur la dose ou sur l'une des quatre lignes, diffère de 1 000.
3. **Graine non dérivée et réglages** (M-4 ; chemins exacts : le manifeste range tout sous `reglages`, le fichier de résultats est lu à la racine et **n'a pas** de champ `texte`) — `texte_non_scelle` : le texte passé par `--texte` est absent ou sans compagnon conforme ; `incoherence_fichiers` : `mode`, `entropie_racine`, `repetitions`, `doses` ou `regle_de_choix` du fichier de résultats ≠ `reglages.<même champ>` du manifeste ; `mode` : `mode` ou `reglages.mode` ≠ « décisif (graine = empreinte du texte scellé) » ; `entropie` : `entropie_racine` ou `reglages.entropie_racine` ≠ l'entier gros-boutiste de l'empreinte du texte ; `texte_sha256` : `reglages.texte.sha256` ≠ cette empreinte ; `texte_chemin` : `reglages.texte.chemin` ≠ le texte lu (chemins réels) ; `entropie_sous_2_64` : `verifier_entropie(…, decisif=True)` refuse ; `grille` : `doses` ou `reglages.doses` ≠ la grille gelée ; `repetitions` : ≠ 1 000 (fichier de résultats et `reglages.repetitions`) ; `processus` : `reglages.processus` ≠ 4 ; `duree_max` : `reglages.duree_max_s` ≠ 6 700 ; `versions` : `reglages.python` ≠ 3.13.18 ou `reglages.numpy` ≠ 2.5.3 ; `modules` : `reglages.modules_sha256` ≠ les huit empreintes de la section 4 ; `epreuve` : `epreuve` ou `reglages.epreuve` ≠ « epreuve-w2g-dose-v1 » ; `lignes` : `reglages.lignes` ≠ (« monde|v9 », « recombinaison|v9 », « recombinaison|ancien », « monde|v8_information ») ; `regle` : `regle_de_choix` ou `reglages.regle_de_choix` ≠ (`seuil_promotion_monde_v9` = 0,8 ; `promotions_recombinaison_v9_max` = 0).
4. **Vérité servie** (m-8) — l'épreuve n'appelle aucun proposeur et ne sert aucune consigne (la garde `verifier_verite_non_servie` de la course n'est pas sur son chemin ; (a) use la loi du monde **par construction**, comme oracle) ; la garde porte donc sur ce qui sort : `cle_verite` / `cle_N` : une clé dont le **nom** est « verite » (accents et casse ignorés) ou « N » (exact), **à toute profondeur** de `manifeste.json` ou d'`epreuve-w2g-dose-v1.json` ; égalité du nom de clé, **jamais** une recherche de sous-chaîne, **jamais** dans les valeurs (le manifeste contient « N » et « vérité » dans des valeurs descriptives : `reglages.monde_w2g`, `regle_des_graines`). Le second volet du brouillon 1 (empreintes du script et du cœur égales à la section 4 : aucun chemin neuf vers un proposeur) est tenu par la garde 3 (`modules`) et la garde 6 (`lecteur`).
5. **Défaut du certificat** (garde, pas une règle de choix) — `monde_promu_dose_0` : à la dose 0, (a) > 0 ; `recombinaison_promue` : à une dose quelconque, dose 0 comprise, (b) > 0 (membre du nul v9 promu : défaut du code ou du certificat). Arrêt, rapport, **nœud de Lazar**.
6. **Instrument** — `lecteur` : `attaque_goodhart_v2.py` ou `attaque_goodhart_v5.py` **lus par le lecteur** (ceux de la copie) d'empreinte différente de la section 4 ; `grammaire_refusee` : une loi du monde refusée par la grammaire servie à une dose (l'oracle ne borne plus ce qu'un attaquant peut écrire) ; `lambda_dose_nulle` : le script propose la dose 0 (`choisir_dose` ne l'exclut pas ; jamais choisissable) ; `desaccord_lambda` : λ\* recalculé ≠ λ\* imprimé (y compris un « aucune dose » d'un côté seulement). Arrêt, rapport, **nœud de Lazar**.

**Ce qui n'est pas un arrêt** : des évaluations impossibles (section 5 : rapportées, sans seuil, audit écrit avant report, λ\* inchangé) ; une inversion de (a) (réserve d'instrument) ; « λ\* à la limite » ; l'analogue de P10 sous 0,50.

**Une sortie complète fixe λ\*** (M-1). Si le code de l'épreuve est 0 et qu'aucune garde ne refuse (lecteur au code 0 ou 3), la dose rendue par la règle — **0,40 ou 0,50, attendues et acceptées d'avance**, ou toute autre dose — ou « aucune dose » est **définitive**. **Aucun texte v3, aucun troisième rejeu** n'est ouvert pour viser une autre dose, ni pour « confirmer » celle rendue. Un texte neuf n'existe que pour une trace **arrêtée** (code 3 ou 124, garde 2) ou **refusée** (code 2 du script, ou garde 1 à 4 du lecteur ; gardes 5 et 6 : après le nœud de Lazar).

**Aucun rejeu partiel combiné** : une trace arrêtée n'est jamais complétée par un second appel ; une nouvelle tentative demande un texte neuf (`epreuve-w2g-dose-v3-…`, R12), donc une entropie neuve, contre-lu et scellé ; rien des traces arrêtées n'y entre. La troisième tentative prendrait aussi des noms neufs de dossier, de console et de lecture (`…-rejeu-v3`, `…-rejeu-v3-console.txt`, `…-rejeu-v3-lecture-v1.json`). La trace v1 arrêtée (section 3 bis) n'est **jamais** complétée par le rejeu v2 ni combinée à lui.

### 6 bis. Lecteur gelé : correction ultérieure (M-2)

Le lecteur, ses essais et son patch sont gelés (section 4, tableau ; empreintes inscrites au registre avec celle du texte, préalable 1). Ils ne sont pas modifiés entre le lancement et la lecture. Si un défaut du lecteur est trouvé **après le lancement** (code 1, ou motif de garde que la mère juge faux, ou défaut trouvé à la lecture) : la correction est une **version neuve** (`lecture_epreuve_w2g_dose_v2.py`, essais et patch neufs, R12), dont le **motif est écrit au registre des décisions avant de relire la sortie** ; elle n'applique que la règle (section 2) et les gardes (section 6) du présent texte, sans en ajouter ni en retirer — sinon c'est un texte neuf ; elle est essayée sur ses cas sains et artefacts, son empreinte inscrite au registre avant son exécution ; elle écrit sa lecture sous un nom neuf (`…-lecture-v2.json`). **Les deux lectures sont rapportées**, la première n'est jamais effacée. Si elles rendent des λ\* différents : nœud de Lazar ; aucune n'est choisie par la mère.

### 6 ter. Essais des gardes (faits avant le rejeu, R5 ; sortie `essais-lecture-v1-sortie.txt` `e2ada891…`, 19:45:52 à 19:46:58 UTC)

43 essais passés, 0 échec, 0 sauté (R-1928). **Cas sains** : deux courses de chaîne réelles du script de l'épreuve (2 répétitions, les 11 doses, `--duree-max-s 6700`, sous un texte factice scellé dans un dossier temporaire), l'une à `--processus 1` (chemin séquentiel), l'autre à `--processus 2` (chemin du bassin de processus, celui du rejeu, m-10 ii), lues avec 2 répétitions, leur nombre de processus et `--duree-max-attendue 6700` ; chiffres non lus au-delà des gardes. **Vrai code 3** : la même course à `--duree-max-s 0.5`, `arret` écrit par le script, doses absentes ou incomplètes (m-10 i). **Artefacts**, chacun refusant pour son motif : dossier vide, manifeste absent, compagnon non conforme, JSON illisible, forme, table différente, autre code de console (garde 1) ; codes 3 et 124, `arret` non nul, dose incomplète, dose manquante, **dose 0 retirée de `resultats`** (m-10 iii), dose retirée partout, répétitions d'une ligne (garde 2) ; cohérence des deux fichiers, durée et versions, empreinte de module changée, grille réduite, mode exploratoire, règle de choix, répétitions et processus, **sorties exploratoires** (refus : `mode`, `entropie`, `texte_sha256`, `texte_chemin`, `entropie_sous_2_64`, `grille`, `dose_absente`), autre texte, chemin du texte, texte non scellé (garde 3) ; clé « verite », clé « N », et cas sain « N » et « vérité » en valeur ou dans un nom plus long (garde 4) ; monde promu à la dose 0, recombinaison promue (garde 5) ; désaccord de λ\*, dose 0 proposée, grammaire refusée (garde 6) ; un essai par code de sortie (0, 2, 3, 4) ; Wilson contre des formes closes et 809/1 000. Motifs **sans artefact propre** : `epreuve`, `lignes` (garde 3), `lecteur` (garde 6) — écart 3, annexe C.

## 7. Contre-lecture (R2)

**Historique du v1** : son brouillon 1 a été contre-lu par un sous-agent neuf d'un autre modèle que son rédacteur — Fable 5.1 (N-052) — (`contre-lecture-epreuve-w2g-dose-v1.md`, `2f422a63…` : scellable après corrections) ; son brouillon 2 a été vérifié par un sous-agent neuf d'un autre modèle (`verification-epreuve-w2g-dose-v1-brouillon2.md`, `3047db37…`) ; le v1 a été scellé (`3415f70d…`).

**Le présent brouillon (v2) est à contre-lire avant scellement** par un sous-agent neuf d'un autre modèle que ce rédacteur (Opus 5.5 ; donc Fable 5.1, N-052), qui n'a écrit ni ce texte, ni le v1, ni le lecteur, ni le code v5, et qui n'a pas vu la table de la trace v1. Fichiers à lui donner : ce brouillon ; le v1 scellé (`epreuve-w2g-dose-v1-v1.md`) ; R-1946 (`registres/decisions.md`, au 8 novembre) ; la lecture d'arrêt `epreuve-w2g-dose-v1-rejeu-v1-lecture-v1.json` ; le script `code-v5/orchestrator/demonstrations/epreuve_w2g_dose_v1.py` ; le lecteur `code-v5/orchestrator/demonstrations/lecture_epreuve_w2g_dose_v1.py`. **Ne pas lui donner** la table, la sortie, le manifeste ni la console du rejeu v1 (section 3 bis). À vérifier : que seules les parties de la table « Ce qui change du v1 au v2 » changent, et que les sections 1, 2, 5, 6 (gardes), 6 bis, 6 ter, les annexes B et C et les préalables 1, 2, 4, 6 sont **mot pour mot** ceux du v1 (comparaison par programme, par exemple `diff`) ; que la mesure de la cause et le remède sont écrits avant toute relecture de la trace v1 et ne touchent ni la règle, ni la grille, ni les gardes, ni le lecteur ; que la durée attendue et la durée maximale tiennent (6 700 < 7 000 < 7 200, attendu ≈ 1 150 s) ; que les deux commandes (rejeu, lecture) concordent avec les deux scripts, noms neufs compris, et que les lignes ajoutées à la console ne trompent pas `lire_code_console` ; les codes de sortie ; le marqueur (annexe A) ; la déclaration de la section 3 bis.

## Annexe A. Marqueur

**Marqueur levé** (un seul) : ENTROPIE_EPREUVE (entre doubles chevrons, section 4), levé **au scellement** en supprimant, au début du paragraphe « Entropie » de la section 4, le marqueur entre accents graves, le point qui le suit et l'espace, de sorte que le paragraphe se lise « **Entropie** : levée retenue (R-1926 ; …) » : l'entropie est alors « l'entier gros-boutiste de l'empreinte SHA-256 du présent fichier scellé, lue par `--entropie-texte` » (levée retenue, R-1926 ; option existante et gardée ; comme au v1). Le changement C2 (une option `--entropie N`) n'est pas demandé. Le motif `<<[A-Z0-9_]+>>` est cherché par programme dans le fichier final : zéro occurrence, sinon pas de scellement. Le statut et la rédaction (en tête) sont mis à jour par la mère au scellement, comme au v1.

## Annexe B. Changements de code

- **C1 (fait, gelé)** : le lecteur `demonstrations/lecture_epreuve_w2g_dose_v1.py` (hors de la fermeture gelée ; aucun lanceur ne l'importe), ses essais et son patch, rendus le 8 novembre (R-1928), empreintes en section 4. Il lit la sortie scellée, la console scellée et le texte scellé, applique les gardes 1 à 6 (section 6), calcule Wilson par `attaque_goodhart_v2.wilson`, recalcule λ\* depuis les comptes, écrit une lecture JSON neuve scellée qui porte sa propre empreinte, et rend les codes 0, 2, 3, 4 (section 4 bis). Paramètres : `--repetitions-attendues` (1 000 par défaut), `--processus-attendus` (4 par défaut), `--duree-max-attendue` (obligatoire, sans défaut : 6 700 au rejeu) ; tout le reste de la section 4 est comparé à ses constantes (mode, grille, versions, empreintes des modules, lignes, règle), égales au présent texte.
- **C2 (non demandé)** : une option décisive `--entropie N` (entier ≥ 2⁶⁴), absente du script.
- **Non demandé** : 200 répétitions à la dose 0 dans le même appel (la dose 0 est jouée à 1 000) ; la grille entière en un appel et la graine dérivée existent déjà.

## Annexe C. Écarts entre le texte et le lecteur gelé

Relevés par ce rédacteur en lisant le code du lecteur (`a9f462cb…`) et les noms de motifs de ses essais (`6f5d3b61…`). **Aucune garde du présent texte ne manque au lecteur, et le lecteur n'applique aucune garde absente du texte** : la section 6 a été réécrite sur son code (le brouillon 1 n'avait ni la table, ni la console, ni `texte_chemin`, `reglages.lignes`, `epreuve`, `lambda_dose_nulle` ni le motif `lecteur`). Restent quatre écarts, aucun sur une garde :
1. **Mots de l'analogue de P10** (m-5) : le lecteur imprime « P10 tenue par l'oracle » / « P10 en tension à λ\* » ; le texte demande « analogue de P10 ≥ 0,50 » / « analogue de P10 < 0,50 à λ\* ». Traitement retenu : correspondance écrite d'avance (section 5), le seuil (0,50) et la comparaison étant les mêmes ; aucun changement de code. Autre voie : version 2 du lecteur **avant** le gel (essais rejoués, empreintes neuves écrites ici).
2. **Inversions de (a)** (m-15) : le lecteur ne les cherche pas. Traitement retenu : comparaison des bornes de Wilson écrites dans la lecture, faite par la mère, rapportée en information. Même autre voie possible avant le gel.
3. **Motifs sans artefact propre** : `epreuve` et `lignes` (garde 3), `lecteur` (garde 6) n'ont pas d'essai qui les fasse refuser ; leur garde, elle, est essayée sur un cas sain et sur d'autres artefacts (R5 tenue garde par garde, pas motif par motif). Réserve rapportée ; un essai par motif demanderait une version 2 des essais avant le gel.
4. **Chiffres dans une lecture d'arrêt** : le lecteur annonce « aucun chiffre écrit dans la lecture » en cas d'arrêt, mais les détails de motif des gardes 5 et 6 portent un compte (`recombinaison_promue` : « dose λ : (b) k promue(s) » ; `monde_promu_dose_0`) ou les deux λ\* (`desaccord_lambda`). Aucun ne sert à choisir une dose (arrêt, nœud de Lazar) ; le texte dit donc « sans table ni intervalle » au lieu de « sans chiffre ». Aucun changement de code.
Aucun de ces écarts ne touche la règle, la grille, le seuil ni le calcul de λ\*. **Décision de la mère** (R-1929) : lecteur gardé tel quel ; texte scellé avec les traitements ci-dessus.

## Sources lues

| pièce | chemin | sha256 |
|---|---|---|
| brouillon 1 de ce texte | `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/epreuve-w2g-dose-v1-brouillon1.md` | `829db6a5f96d4eea0784611f37679ad3ce2f0ccd9894ddb07610e97313b3cc80` |
| contre-lecture du brouillon 1 | `…/a1-v4-reprise-v9/contre-lecture-epreuve-w2g-dose-v1.md` | `2f422a639a01794ef3a5c415bba3bb7d057cd467a7f1af10abc1906c38160446` |
| lecteur | `…/code-v5/orchestrator/demonstrations/lecture_epreuve_w2g_dose_v1.py` | `a9f462cb73b99680ed82ca8bc41b3241cd5b29591e5978044185786ab8467c71` |
| essais du lecteur | `…/code-v5/orchestrator/essais/test_lecture_epreuve_w2g_dose_v1.py` | `6f5d3b6165679ba2f364010ee94350b548cceac56c793c31f92b6b82ba1cec2e` |
| patch du lecteur | `…/code-v5/patch-public-code-v5-lecture-v1.diff` | `26a37cd82ca4a2f2139626fc7bc6c4f714f7d2916635b59f49704c6a1f097d3f` |
| sortie des essais du lecteur | `…/code-v5/essais-lecture-v1-sortie.txt` | `e2ada8918770be5f52dcfc623156bba655d539b4df4c47b6359f79e6a097ead1` |
| préenregistrement, brouillon 3 | `…/a1-v4-reprise-v9/preenregistrement-attaque-goodhart-v4-brouillon3.md` | `c44f52cc0fa53e1bbd621c56a06f6c65860487fc6afe30d52ed2d6b81adc8dac` |
| rapport du code v5 | `…/code-v5/rapport-code-v5-w2g-v1.md` | `c31d23b84e8406aeef1b72f2146065c854b29ee5c7cd2c84e441eaa9c8fa77a1` |
| script de l'épreuve | `…/code-v5/orchestrator/demonstrations/epreuve_w2g_dose_v1.py` | `c691a43d9905e91a0ba91ddfef785e53a091768fa7dcd3007f03066aeef10dda` |
| cœur v5 | `…/code-v5/orchestrator/pole/attaque_goodhart_v5.py` | `8692746a1b02b15465062423d1f05e2084ce1d1861c979316ce1a5ef4384ba15` |
| patch public v5 | `…/code-v5/patch-public-code-v5.diff` | `12c39347e47fec599da21ef00f8d0534b661d2dd982b7f8c7ca9ac2169a660d2` |
| cœur v2 et outils (dépôt public, commit `8947bc8`) | `/home/user/ideation-organism/orchestrator/pole/attaque_goodhart_v2.py` ; `pole/outils.py` | `3c9de8b8…` ; `966d9553026aad1eb7d97fa677334f1b59f22a39f15eef95134d63bc47634444` |
| décisions R-1897, R-1923, R-1926, R-1928 | `registres/decisions.md` (fichier vivant, au 8 novembre) | non empreinté |
| texte v1 scellé (source du présent brouillon) | `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/epreuve-w2g-dose-v1-v1.md` | `3415f70d8690708b4c7c558420c8c19ead1a211d68be277050c46d0ca8b21122` |
| lecture d'arrêt de la trace v1 | `…/a1-v4-reprise-v9/epreuve-w2g-dose-v1-rejeu-v1-lecture-v1.json` | `37b4d34de2a4b1437e064c3a37735b41ea0c458f8ef9612ad4e649a689fa6aca` |
| trace v1 arrêtée (non lue par ce rédacteur : empreintes seules) | section 3 bis | section 3 bis |
| décision R-1946 | `registres/decisions.md` (fichier vivant, au 8 novembre, 23:17 UTC) | non empreinté |

## Annexe D. Mineurs de la contre-lecture du brouillon 1 et leur traitement

Seuls changements entre le brouillon 1 contre-lu et ce texte scellé : statut, titre, levée du marqueur, et les mineurs ci-dessous ; le brouillon 1 reste en place pour le `diff` (m-9).

| mineur | traitement |
|---|---|
| m-1 (attribution « sans autre calcul ») | corrigé : préalable 5 du v1, tenu par la mère |
| m-2 (« pas le calcul ») | corrigé : mêmes comptes et valeurs imprimées, aucune différence détectée ; nombre de fils porté par la console |
| m-3 (table de l'essai exploratoire imprimée à la console) | déclaré : seule la ligne de durée lue selon le rédacteur ; graine 11, dose 0,5, sans usage |
| m-4 (« sorties et codes du script » mot pour mot) | errata : mot pour mot **à son nom de dossier près** (`…-rejeu-v2/`) |
| m-5 (deux changements absents de la table « Ce qui change ») | errata : le paragraphe « Console » (noms neufs, lignes ajoutées) et la fin du préalable 3 (copie `…-rejeu-v2-copie`) changent aussi |
| m-6 (casse « Levée ») | corrigé |
| m-7 (numéros de ligne du script) | errata : lire « l. 167–246 » pour « l. 160–260 », et « l. 168–175 » pour « l. 168–174 » |
| m-8 (vérifier l'effet des variables avant le lancement) | fait par la mère avant le lancement, dans la copie de travail : nombre de fils d'OpenBLAS imprimé avec et sans les variables, consigné au registre |
| m-9 (écart auditable entre texte contre-lu et texte scellé) | cette annexe |
