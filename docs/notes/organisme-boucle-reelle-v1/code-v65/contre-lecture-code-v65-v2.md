# Contre-lecture du code v65 de l'organisme d'idéation (plus petite course réelle de la boucle complète) — v2

- **Contre-lecteur** : sous-agent neuf de la session mère (reprise du 10 novembre 2026), modèle Claude Fable 5.2 (`claude-fable-5-2`), autre modèle que l'auteur (Claude Opus 5.5) : N-052. Je n'ai écrit ni le code v65, ni sa consigne, ni aucune version précédente de l'organisme. La v1 de cette contre-lecture (lecteur coupé par le quota) n'a jamais été versée ; je ne l'ai pas lue.
- **Heures** (temps universel, relevées par `date -u`, 10 novembre 2026) : début 11:52 ; suite rejouée 11:56:06 → 11:58:44 ; banc rejoué 11:59:33 → 12:04:57 ; essai à blanc rejoué 12:02:35 → 12:03:15 ; mes mutations 12:05:30 → 12:16:10 ; rapport écrit à partir de 12:16.
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-contre-lecture-code-v65-v1.md`, sha256 `67b086ce70137faa85b3679ffc48f62718fbe8a13b8f4cc0b09a0816044cbbfa`, égale à son compagnon. Interdits communs v2 suivis : aucun fichier interdit ouvert, aucune recherche récursive, aucune variable d'environnement lue ni affichée, aucun appel de modèle, aucun réseau, aucune dépense, aucun commit.
- **Aucune dépense.** Rien n'a été écrit dans l'arbre de l'organisme (`git status` vide, tête `cef5ea60…` avant et après).

## 0. Verdict

**« Utilisable pour la course après corrections ».** Le cœur fait ce que la consigne demande pour M1 à M4, la suite et le banc annoncés se rejouent à l'identique, l'essai à blanc aussi. Mais la **lecture gelée (M5) peut prononcer C1 sans qu'aucune fausse ait été jugée**, **un arrêt peut masquer une brèche** (contre la section 8 du brouillon), la vue servie à la génération 2 n'est vérifiée par rien, et plusieurs gardes de la v65 n'ont pas d'essai sur un artefact (R5). Rien de cela ne touche une dépense ; tout se corrige hors ligne.

**Liste exacte des corrections exigées avant le scellement du texte** (détail en section 3) :

1. CLV65-01 — la lecture exige que les lois plantées attendues soient présentes et jugées ; sinon elle ne prononce pas C1.
2. CLV65-02 — un arrêt ne masque plus une brèche : jugements écrits au relevé avant les tests de mort ; héritage refusé lu « C4 (partielle) ».
3. CLV65-03 — la vue réellement servie aux proposeurs de la génération 2 entre au relevé et dans P6.
4. CLV65-04 — essais sur artefact (et mutations) pour les gardes de la v65 qui n'en ont pas, dont la garde 7 réécrite et la branche réelle du lanceur.
5. CLV65-05 — la moitié « ni servies » de la garde 7 (`exiger_sans_temoin` de la v64) est reprise, ou son abandon est écrit au texte.
6. CLV65-06 — le banc de mutations doit pouvoir rendre 38 sur 38 sur la machine à `bwrap`.

**Conditions hors du code, à régler avant le lancement** : CLV65-07 (le registre des GO réel est refusé par le lanceur), CLV65-08 (mesures promises par le brouillon et absentes du relevé : texte ou code à aligner), CLV65-09 et CLV65-10 (machine, configuration).

Comme les fichiers v65 ont été livrés (paquet et patch poussés sur `prep/organisme-v65-v1` du dépôt de travail), une correction demande des noms neufs (R12) : v66. La décision revient à la mère.

## 1. Ce que j'ai rejoué

Interpréteur `/home/user/controle-ia-travail/.venv/bin/python -I -B` ; dossiers temporaires dans mon bac à sable (`TMPDIR`, `--basetemp`), retirés ensuite.

| pièce | annonce du développeur | ce que j'obtiens |
|---|---|---|
| empreintes des dix fichiers neufs (commit `cef5ea60…`, parent `94bfd92`) | table de la section 8 du rapport | égales, une à une |
| rendu du développeur (32 fichiers et leurs compagnons) | — | 32 sur 32 conformes ; rapport `f84c1430…` |
| suite touchée (`POLE_ESSAI_BAC_REEL_NON_JOUE=1`, six fichiers d'essais) | « 232 passed, 3 skipped, 160 subtests passed » | **`232 passed, 3 skipped, 160 subtests passed in 157.92s (0:02:37)`**, code 0 ; les trois sautés sont les essais du vrai bac à sable |
| banc de mutations v65 | « 38 tuées sur 38 » | **`38 tuées sur 38 mutations`**, code 0 |
| essai à blanc, 9 étapes (script du rendu, `2ffc22d7…`) | codes 2, 0, 0, 3, 0, 3, 2, 2, 0 | mêmes codes, mêmes messages ; lecture C1 puis C5 |
| décisions du relevé à blanc (cartes, lois plantées, retenues, membres, lecture de la sélection) | — | **égales** à celles du relevé du développeur ; constats, audits et mesures de l'oracle de la lecture égaux |
| blocs du texte (`preparer_boucle_reelle_v65.py`) | `382e74dd…`, héritage `93dcf517…` | égaux à l'octet |
| empreintes des commandes v6 (commit `12f9e0e3…`, lues par `git show`) | `88930930…`, `5eae1a04…`, `8ba92066…` | égales |
| lois du jeu (`jeu_du_dessin`) contre `lois_du_dessin` du script de puissance (`a2afcdd3…`) | identiques | identiques (lecture ligne à ligne) |

Constat (a) du développeur confirmé : le relevé n'est pas reproductible à l'octet (le mien `ebc63251…`, le sien `ffd36ec4…`), décisions égales.

Sorties de mon bac à sable (non versées, retirées à la fin) : suite `acfc13f5…`, banc `98673c3c…`, mes mutations `825c6bb2…`.

## 2. Exigences M1 à M5, gardes : ligne de code, essai qui la tient

Lignes de `orchestrator/pole/boucle_reelle_v65.py` (cœur), `pole/lecture_boucle_reelle_v65.py` (lecture), `demonstrations/boucle_reelle_v65.py` (lanceur) ; essais de `essais/test_boucle_reelle_v65.py` et `essais/test_lecture_boucle_reelle_v65.py`.

| exigence | code | essai sain | essai sur artefact | avis |
|---|---|---|---|---|
| **M1** héritage de départ scellé, garde 17 | cœur 246-269 (`lire_heritage_depart`, empreinte lue avant le contenu par `lire_scelle_verifie`) | `HeritageDepart.test_sain_accepte` | autre empreinte, sceau faux, K1 altérée, loi plantée dedans, statut | **tenue**. Sans essai : version ou génération autre (ma mutation X09 survit). En mode réel la garde est câblée ligne 360 du lanceur, après la construction des rôles : non atteinte ici (section 4) |
| **M2** jeu planté lu dans le texte, garde 19 | cœur 108-205 ; classe couverte 139-169 | jeu lu à l'octet, fichier à blanc égal au dessin, formes couvertes | loi changée, jeu incomplet ou en trop, quatre fausses hors classe, bloc en double | **tenue**. `classe_couverte` est conforme à la docstring de `nul_v8.py` et plus stricte qu'elle (mélange imbriqué refusé). Sans essai : loi hors de la grammaire servie (X10 survit) |
| **M3** jugement avec l'archive, garde 18 | cœur 307-332 ; garde ligne 320 | défaut de la v64 reproduit puis corrigé (4 membres, aucun promu) ; seuil hors famille | jugée sans archive ; archive plus petite | **tenue**. Le nombre de membres est mesuré sur la bibliothèque réellement construite (`a_blanc_v59.juger_carte`, ligne 180), pas sur l'archive passée : la garde ne peut pas être satisfaite par construction |
| **M4** bras réel seul (garde 20), génération 2 complète, copies (garde 21) | cœur 275-280, 509-510, 357-378, 530-551 | bras réel ; la génération 2 lit la sélection ; copies | autre bras, trois générations, héritage altéré (arrêt), héritage d'un autre contenu (C4), copie non retenue | **tenue pour le jugement** (archive, membres, copies). **Non tenue pour la vue servie** : CLV65-03 |
| **M5** lecture gelée C1 à C6, A1 à A4 | lecture 86-129, 57-83, 132-182 | C1 sain, A1 d'office | chaque issue et chaque audit sur un relevé altéré ; ordres C4/C2 et C3/C6 | **à corriger** : CLV65-01, CLV65-02 |
| commandes v6, configuration v5 | lanceur 188-212 ; `exemples/configuration-boucle-reelle-v5.json` | `ConfigurationV5.test_sain` | commande altérée, part, plafond, GO, machine, commande lancée | **tenue** ; voir CLV65-10 |
| gardes de dépense | `tour_ferme_v64.Compteur` (inchangé) ; cœur 290-296 et 399 | parts suffisantes | arrêt avant l'appel sous la part ; arrêt au plafond ; étape 6 de l'essai à blanc | **tenue**. Sans essai : plafond restant avant l'appel (X08), coût compté quand l'appel s'arrête (X07) |
| aucun appel sans GO cité | cœur 283-287 et 508 ; lanceur 341-346 et 361 | `test_go` | GO absent, incomplet ; cœur sans GO | **tenue dans le cœur** ; au niveau du lanceur, tenue d'après ma sonde (section 4), sans essai dans la suite |
| garde 22 | lanceur 218-236, 349, 365 | versions 0.9 et 1.0 | version absente, 0.8, utilisateur 0 ou absent | fonctions tenues ; câblage et sonde **non éprouvés ici** ; CLV65-09 |
| bac à sable, garde 3 | `a_blanc_v59.choisir_executeur` (inchangé) | non joué (pas de `bwrap`) | `bwrap` absent : code 2, aucun repli (essai et étape 1) | artefact tenu, cas sain à jouer sur la machine |

## 3. Constats

Gravité : **B** bloque le scellement tant que non corrigé ; **C** à corriger ou à écrire au texte ; **m** mineur ; **i** information.

### CLV65-01 (B) — la lecture prononce C1 sans qu'aucune fausse ait été jugée

`lire_criteres` ne vérifie pas que les lois plantées attendues sont au relevé ni qu'elles ont été jugées. Sur le relevé sain de la course à blanc, altéré dans mon bac à sable :

| altération | issue rendue | A1 « fausses_log_w_max_au_plus_0 » |
|---|---|---|
| F1 à F4 toutes refusées au gardien, jamais jugées | **C1** | vrai |
| F1 à F4 absentes du relevé de la génération 2 | **C1** | vrai |
| F1 à F4 absentes des deux générations | **C1** | vrai |
| aucune copie alors que 11 cartes sont retenues | **C1** | — |
| une seule copie au lieu de quatre | **C1** | — |
| relevé complet mais `generations_jouees` = [1] ; aucun étage au relevé | **C1** | — |

« Aucune fausse promue » est alors vrai à vide, et l'audit A1 laisse passer un log W absent (lecture 153 : `is None or …`). C'est un repli silencieux (R5) sur le critère principal P1. Le risque réel est faible (le gardien est déterministe et F1 à F4 l'ont passé à blanc), mais la lecture est gelée par le texte : elle doit refuser.

**Correction** : avant toute issue autre que C5, la lecture exige V1 à V4, T-ELIM et T-MAL en génération 1, F1 à F4 dans les deux générations, chaque fausse et chaque copie passée au gardien et jugée (membres d'archive égaux aux membres attendus, log W maximal présent), et un nombre de copies égal au plus petit de quatre et du nombre de retenues de la génération 1 ; sinon C5 « relevé incomplet », cause écrite. Un essai sain et un artefact par condition ; une mutation par condition.

### CLV65-02 (B) — un arrêt peut masquer une brèche

Brouillon, section 8, ligne C5 : « si le relevé partiel montre déjà une fausse ou une copie promue, ou une lecture de sélection en écart, C2 ou C4 s'écrit aussi […] : un arrêt ne masque jamais une brèche ». Deux trous.

(a) **Les jugements ne sont écrits au relevé qu'après les deux étages de tests de mort** (cœur 453-473, après les appels des lignes 439-447). Un arrêt entre le jugement et la fin des étages laisse un relevé sans une seule loi jugée. Vu deux fois : étape 6 de l'essai à blanc (arrêt « part restante sous le pire cas de l'étage ») et ma course `--scenario-experimentateur fabrique` (contre-calcul en désaccord, garde 10) : 12 cartes et 10 lois plantées jugées, **0 carte et 0 loi plantée au relevé**, journal réduit à l'arrêt. Une fausse promue par le juge dans cette génération serait perdue, et la lecture dirait C5 sans « C2 (partielle) ». C'est le cas le plus probable d'arrêt d'une course réelle (session de l'expérimentateur, part d'un relais).

(b) **Un héritage refusé n'est pas lu comme un écart de lecture.** `lire_heritage` lève avant que `lecture_selection` soit écrit (cœur 533-543) ; la lecture rend C5, `aussi` vide (ma sonde S10 ; l'essai `test_artefact_heritage_altere_refuse` vérifie C5 mais pas `aussi`). Or « empreinte lue ≠ écrite » est la première condition de C4. Dit autrement : avec `boucle_fermee_v59.lire_heritage`, le champ « lu » est l'écho de l'empreinte attendue (v59, ligne 193), donc la branche « empreinte lue ≠ écrite » de la lecture ne peut pas se produire dans une course ; l'écart réel devient toujours un arrêt muet sur C4.

**Correction** : écrire les jugements (cartes et lois plantées, promotions, log e, membres) au relevé dès la sortie de `juger_v65`, avant les étages, les verdicts s'y ajoutant ensuite ; consigner le refus de l'héritage dans `lecture_selection` (empreinte attendue, motif) et faire écrire « C4 (partielle) » à la lecture. Essais : un arrêt pendant l'étage avec une fausse promue (artefact par `archive_des_plantees` ne convient pas, la garde 18 arrête avant : passer par un relevé partiel construit) ; l'héritage altéré avec `aussi` vérifié. Sinon, écrire au texte que ces deux cas se lisent C5 seul, ce qui affaiblit la section 8.

### CLV65-03 (C) — la vue servie à la génération 2 n'est vérifiée par rien

`lecture_selection.vue` est recalculée dans `jouer_boucle` (cœur 536-540) à partir de l'héritage lu ; ce que `jouer_generation` sert réellement (cœur 392-395) n'entre pas au relevé. Ma mutation X19 (la génération 2 ne sert que K1 aux proposeurs) **survit** aux deux fichiers d'essais v65, et la lecture rend C1. P6 (« vue = {K1} ∪ retenues ») et le point (ii) de la génération 2 (brouillon 3.7) sont donc vérifiés sur une recopie, pas sur le contexte servi. La consigne demandait un essai prouvant que « le contenu de l'héritage entre dans ce qu'elle reçoit » : il est prouvé pour l'archive de jugement et les copies, pas pour la vue.

**Correction** : écrire au relevé, par génération, les identifiants des lois du contexte réellement servi (et l'empreinte du contexte) ; P6 les compare ; un essai sain, un artefact, une mutation.

### CLV65-04 (C) — gardes et contrôles de la v65 sans essai sur un artefact (R5)

Mes vingt mutations, jouées chacune contre les deux fichiers d'essais v65 entiers : **17 survivent**, 3 sont tuées (X17 audit A3, X18 fausse découverte réelle, X20 seuil de T-ELIM).

| mutation | ce qui est retiré | portée |
|---|---|---|
| X01 | garde 7 réécrite dans la v65 (cœur 451 : loi plantée dans la sélection) | **garde d'arrêt sans essai** : les essais de la v64 portent sur `tour_ferme_v64.jouer_generation`, que la v65 ne joue plus |
| X04 | appel de `exiger_copies_de_la_selection` dans la boucle (cœur 538) | la fonction est essayée, son câblage non |
| X05, X06 | refus du bac factice en mode réel ; toute la branche réelle du lanceur (324-359) | **aucun essai de la suite ne joue `principal` en mode réel** |
| X07, X08 | coût d'un appel de proposeur qui s'arrête ; plafond restant avant l'appel | gardes de dépense secondaires |
| X09, X10 | version et génération de l'héritage de départ ; grammaire des lois du jeu | gardes 17 et 19, conditions secondaires |
| X11, X12 | empreinte du relevé donnée au lecteur ; empreinte du monde | programme de lecture |
| X13 | relecture de la sélection de la génération 2 | fin de boucle |
| X14 | plafonds, montant et durée strictement positifs | plan gelé |
| X15, X16 | champs « contre-calcul égal » et « bac réel partout » de A1 | audit A1 |
| X02, X03 | familles séparées, dans le cœur ou dans le lanceur | redondance voulue : chacune seule survit ; le cas artefact tient (`--familles-a-blanc a,a` : code 2, joué à la main) mais n'est pas dans la suite v65 |
| X19 | voir CLV65-03 | |

**Correction** : un essai sur artefact et une mutation pour X01, X04, X05, X07 à X16 ; pour la branche réelle, des essais de `principal` avec le dossier des textes remplacé (ce que fait ma sonde, section 4) : sans `--go`, autre GO, montant autre, configuration d'une autre empreinte, bac factice, option de plan en ligne de commande.

### CLV65-05 (C) — garde 7 reprise à moitié

La v64 appelle `exiger_sans_temoin` avant chaque génération et à la relecture finale (aucun identifiant de loi plantée dans l'archive ni dans la vue ; `tour_ferme_v64.py` 1106 et 1134). La v65 ne l'appelle pas ; elle ne garde que le contrôle de la sélection (cœur 451) et un champ d'audit après coup (`vue_g2_sans_loi_plantee`, sous C1 seulement). Le brouillon (section 10) dit reprendre la garde 7 : « lois plantées jamais retenues ni servies ». L'écart n'est pas dit dans le rapport du développeur. **Correction** : rappeler `exiger_sans_temoin` avec les identifiants des lois plantées avant la génération 2 et à la relecture finale, ou l'écrire au texte.

### CLV65-06 (C) — le banc ne peut pas rendre 38 sur 38 sur la machine à `bwrap`

La mutation `N-bac-factice` n'est tuée que par `test_artefact_bwrap_absent_refus_code_2_sans_repli`, sauté dès que `bwrap` est présent ; le banc impose `POLE_ESSAI_BAC_REEL_NON_JOUE=1` à ses essais (banc, fonction `essayer`), ce qui saute aussi l'essai du vrai bac ; et une passe où tout est sauté compte « survit ». Sur la machine de la course, la commande du bloc (`essais/mutations_boucle_reelle_v65.py --processus 4`, pièce M7) rendra donc 37 sur 38, code 1. Lu dans le code, non joué (pas de `bwrap` ici). **Correction** : tuer cette mutation par un essai qui tourne dans les deux cas (`which` injecté), ou par l'essai du vrai bac sans la variable.

### CLV65-07 (C, hors code) — le registre des GO réel est refusé par le lanceur

`verifier_go_v56("GO-2026-11-08-02", registres/go.md, 45)` sur le registre de `main` du dépôt de travail : **`GoRefuse : registre des GO : identifiant GO-2026-10-24-07 en double`**. Le registre porte 17 identifiants en double (lignes d'extension réutilisant un identifiant, du 24 octobre au 4 novembre) ; `configuration_v53.lire_registre_go` les refuse. Sur une copie dédoublonnée dans mon bac à sable, la ligne du GO est acceptée à 45 USD (accordée le 8 novembre, échéance le 30, par Lazar) et refusée à 40 et à 50. Le refus va dans le sens sûr (code 2), mais la commande du bloc (`--registre-go CHEMIN/registres/go.md`) ne passera pas telle quelle. **À décider par la mère** : quel fichier de registre la course cite (un extrait scellé, comme les courses précédentes ont dû le faire), et l'écrire dans les commandes du texte.

### CLV65-08 (C, texte ou code) — mesures promises par le brouillon et absentes du relevé v65

- Section 7, point 6 : recherche de la loi plantée « dans les consignes et contextes servis aux proposeurs, à l'expérimentateur et au vérificateur ». Le code ne cherche que chez les proposeurs (cœur 398), comme la v64.
- Section 7, point 7 : par loi, « membre dominant du nul » et « empreinte d'engagement ». Ni l'un ni l'autre n'est au relevé ni au journal de la v65 (la v64 gardait l'empreinte au journal, champ `juge`) ; l'audit A2 (« vérifier ses membres », « classer ») en a besoin. Les graines sont au bilan.
- Section 5 : intervalles de Wilson, jetons d'entrée et de sortie : absents de la lecture et du relevé.
- La mesure de la v64 « lignes de la tranche présentes dans les contextes servis » a disparu sans être dite.

Un préenregistrement ne doit promettre que ce que le code mesure : ajouter ces champs en v66 ou retirer ces phrases du texte.

### CLV65-09 (C) — garde 22 : ce qu'elle vérifie vraiment

- `exiger_machine` vérifie que l'argument `--utilisateur-bac` est donné et non nul, pas que le bac tourne sous cet utilisateur. `preparer_bac` et `choisir_executeur` n'emploient l'utilisateur dédié que si le lanceur tourne en superutilisateur (`os.geteuid() == 0`) ; lancé sous un autre compte, le bac tourne sous ce compte et la garde passe. À écrire dans les commandes du texte (lancement en superutilisateur), ou à vérifier sur la description du bac.
- Ordre du mode réel : les portes de plafond sont transmises aux relais (`roles_reels`, lanceur 353) **avant** la garde 17 (360) et la sonde du bac (365). Aucun appel payant ne précède la sonde, la lettre de la garde 22 est tenue ; un refus tardif laisse seulement une porte posée. Mieux vaudrait lire l'héritage et sonder le bac avant.

### CLV65-10 (i) — configuration v5 : ce que son empreinte gèle

Les commandes v6 y sont nommées par des **chemins absolus** `/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1/…`, qui n'existent pas sur `main` (les fichiers vivent sur la branche `outils/commandes-tour-ferme-v1`). L'empreinte de la configuration est au plan gelé : sur la machine de la course, les commandes doivent se trouver exactement à ces chemins, et les pièces `pieces/…` à côté de la configuration (absentes de l'arbre de l'organisme : `lire_configuration_v56` refuse ici, six pièces manquantes). Tout changement de chemin change l'empreinte, donc le texte. Le plafond de 5 USD de la machine n'est tenu par aucun code (dit par le développeur).

### CLV65-11 (m) — programme de lecture

La phrase de résultat ne dit pas le mode : une course à blanc à exécuteur factice rend « Issue C1 : la chaîne garde », le mode n'étant écrit que dans un champ à part. `--sans-oracle` retire sans le dire la mesure P7 et la fausse découverte réelle « en tête ». `--releve-sha256` est facultatif (le lecteur de R13 doit la donner). La fausse découverte d'une carte réelle n'entre pas dans la phrase.

### CLV65-12 (i) — réponses aux questions posées au contre-lecteur

- **Classe couverte** : les quatre formes de `classe_couverte` sont dans la classe de la docstring du nul v8 ; `melange_aveugle` seul est bien un mélange linéaire avec une loi fixe (`selection_pari.py` 162-164). Deux bords non fermés, sans effet sur le jeu du dessin : une puissance ou une inclinaison hors de la boîte [−60 ; 60] du membre log-linéaire, bornée seulement par la grammaire servie ; un mélange à poids nul sur la loi d'archive (alors loi fixe, couverte trivialement).
- **Marge de A1 (10⁻⁶)** : raisonnable pour F1 à F3 (classe linéaire, W ≤ 1 par construction aux arrondis près). Pour F4 (membre log-linéaire, dominance « au second ordre près, sans preuve »), un dépassement minime ferait tomber le champ d'audit sans être une brèche : à dire dans le rapport si cela arrive. À blanc, le plus grand vaut −0,174.
- **Ordre de la lecture** : C5, C4, C2, C3, C6, C1, conforme à la section 8 ; T-ELIM « non concluant » se lit C6, lecture stricte de P4, acceptable.

### CLV65-13 (m) — divers

- Si une fausse ou une copie est promue en génération 2, la v65 joue son test de mort (étage des lois plantées) ; le brouillon ne teste en génération 2 que les cartes réelles promues. Dépense minime, cas de brèche seulement.
- En arrêt, le lanceur écrit lui-même une phrase d'issue dans le rapport (« non jugeable (arrêt) : la lecture gelée dit C5… ») alors que le cœur « ne lit aucune issue ».
- Une exception entre la fin des gardes et le début de la boucle (écriture du manifeste) sort en erreur brute, ni code 2 ni code 3 ; le dossier des sessions du mode réel n'est jamais retiré.
- Le rapport du développeur dit une heure de fin fausse (dite dans sa passation).

## 4. Ce qui ne peut être joué qu'avec `bwrap`, et ce qui reste donc non éprouvé

Joué ici, par une sonde de mon bac à sable (dossier des textes remplacé, texte d'essai scellé, configuration à doublures de commandes, registre dédoublonné, aucun appel) : la branche réelle du lanceur **jusqu'au chargement de la configuration**. Tous code 2, avec le bon motif : sans `--go` ; autre GO ; registre réel (doublons) ; texte à 50 USD contre un registre à 45 ; bac factice en mode réel ; option de plan en ligne de commande ; configuration d'une autre empreinte ; sans `--confirmer-moteur-reel`.

**Non éprouvé sur cette machine** :

1. garde 3, cas sain, et garde 22 entière en situation : lecture de `bwrap --version` réelle, sonde réussie, utilisateur dédié effectif, dossier racine en 0700 ;
2. `test_sain_bac_reel_essai_a_blanc` (v65) et les deux essais réels de la v64 et de la v59 ; l'essai à blanc `--bac reel` ;
3. la suite du mode réel après le chargement de la configuration : pièces, garde 15 (machine jetable, environnement réel), construction des adaptateurs et des commandes externes, portes de plafond des relais, **garde 17 en mode réel**, `--verifier-seulement` ;
4. l'étage des tests de mort au moteur réel (refus de l'exécuteur factice par l'étage, fichier témoin, groupe de contrôle mémoire, filtre d'appels système) ;
5. le banc de mutations sur la machine (CLV65-06) et la suite sous numpy 2.5.3 (M7) ;
6. tout appel aux relais et aux commandes v6 : rien n'a été lancé, à dessein.

## 5. Le dossier du texte scellé : mon avis

**Garder le dossier fixé `orchestrator/prereg/` de l'organisme ; y copier le texte scellé, à l'octet. Pas de version qui accepte un autre dossier.**

- C'est l'usage : ce dossier porte déjà les textes scellés de l'organisme et leurs contre-lectures (nul v8, tour fermé, attaque de Goodhart).
- Un emplacement fixe est une garde plus forte qu'un chemin passé en option : nom imposé, sceau, aucun marqueur, code gelé conforme, le tout au même endroit que le code qu'il gèle.
- La racine des graines est l'empreinte du texte : la copie doit être l'exemplaire scellé du dépôt de travail, octet pour octet, sous le nom `preenregistrement-boucle-reelle-organisme-v1-v<N>.md`. L'exemplaire qui fait foi (R1) reste celui du dépôt de travail, committé et poussé avant la course, ce qui le date.
- La copie locale sur la machine de la course n'est pas une publication. **La pousser sur le dépôt public en est une : nœud de décision de Lazar**, qui peut venir après la course. Le manifeste notera alors « arbre modifié » (fichier non suivi) : à dire dans le rapport.
- Une v66 est de toute façon nécessaire pour les corrections de la section 0 ; je ne recommande pas d'y ajouter un second dossier.

## 6. Points ouverts pour la mère

- Décider v66 (noms neufs) pour les corrections 1 à 6, puis une contre-lecture courte du différentiel.
- Décider du fichier de registre cité par la course (CLV65-07).
- Aligner le brouillon et le code sur les mesures (CLV65-08), et écrire au texte le lancement en superutilisateur avec utilisateur dédié (CLV65-09) et les chemins des commandes (CLV65-10).
- Rejouer sur la machine à `bwrap` les six points de la section 4.
