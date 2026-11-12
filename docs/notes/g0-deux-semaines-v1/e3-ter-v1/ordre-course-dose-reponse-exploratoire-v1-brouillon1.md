# Ordre — course de dose-réponse de T0.6, **run exploratoire** v1 (galop de la garde d'équivalence fusionné), brouillon 1

> **EXPLORATOIRE, NON OPPOSABLE (R-522) : aucun verdict de porte, aucun chiffre de dossier n'en sort ; la lecture de confirmation sera préenregistrée.** Toute courbe, table ou nombre issu de ce run porte la mention « exploratoire » et ne peut être cité ni dans un préenregistrement comme prédiction tirée du résultat, ni dans un papier, ni dans un verdict de G0.

- **Statut** : brouillon 1, reçu du sous-agent rédacteur de la session mère (`session_016QhUrrLeN21G7Z9KZobE42`), 8 novembre 2026 ≈ 15:35 UTC. **Non scellé, non commis, aucune ligne de GO encore.** Il succède au brouillon 2 de l'ordre du galop E3 ter (`ordre-e3-ter-garde-equivalence-v1-brouillon2.md`, gardé, R12 : le galop y est fusionné) et applique les corrections de la contre-lecture cl1 du galop (`contre-lecture-ordre-e3-ter-v1-cl1.md`, table § 12). La mère remplit `<<COMMIT_V13>>`, `<<COMMIT_EXPLO>>`, `<<GO_COURSE_EXPLO>>`, `<<FIN_GO_EXPLO>>`, puis contre-lecture (R2), scellement de l'ordre (l'ordre, pas un préenregistrement), ordre remis à une fille d'exécution.
- **Déclencheur** : mots de Lazar, session mère, 8 novembre 2026 : ≈ 15:10 UTC « le vrai goulot est la course de dose-réponse, lance-la now » ; ≈ 15:22 UTC « Course de dose-réponse, lance-la now : pas de prereg, c'est au stade exploratoire ». Le point E3-6 d'E3 bis (R-1769 ; R-1784 ; décision (b) de Lazar consignée à R-1825, point 4) est réglé **par ce run même** : la garde d'équivalence y est exercée de fait (§ 3). Changement de périmètre consigné par la mère (R-1840 et suivants).
- **Objectif de calendrier** : lancement ce soir, 8 novembre, si la chaîne v13 est verte et la ligne de GO inscrite.

## 0. Ce que ce run est, et n'est pas

- **Il est** : la course de dose-réponse du candidat 12 (organisme (ii) par adaptateur de rang faible à dose réglable, six états S25/S50/S75/S100/T100/dose 0, 64 tâches d'évaluation, T = 10, distillation sur les 32 tâches de réserve, activations enregistrées, test croisé d'étiologie et couples descriptifs si le lanceur les joue : oui, `lanceur_v5` joue `test-croise` et `couple-descriptif` après les épisodes, journal d'E3 bis l. 39–53), jouée **sans préenregistrement**, en régime exploratoire, avec la garde d'équivalence échantillonnée à 0,5 au lieu de 0,05.
- **Il n'est pas** : la lecture de confirmation des critères 2 et 3 de G0. Celle-ci sera un **run neuf**, graines neuves, préenregistré (candidat 12 ou sa suite), contre-lu, scellé avant lecture, avec la fraction de la course (0,05) ou celle que ce run aura justifiée.
- **Ce qui en sort** : des **comptes** (garde, contrôle négatif, durées, dépense) qui règlent E3-6 et dimensionnent la chaîne ; des **courbes et tables marquées exploratoires** (dose–réponse, test croisé) qui servent à écrire le préenregistrement de confirmation (puissance, seuils, règle du contrôle négatif à T = 10), jamais à le remplacer.

## 1. Cadre

| Élément | Valeur |
|---|---|
| Pièces du candidat (citées, **non modifiées**) | préenregistrement candidat 12, révision 2 : `brouillons/T0.6-organismes-v0-v1-candidat12-r2.md`, `0d6bf1c47f6bd282d4c4a2a7a7503c977f2068a4c02ccd2d705142f64b9b63f7` (commit `8cb539f9`, branche `prep/t06-ordre-course-v2`) ; configuration de la course : `docs/notes/g0-deux-semaines-v1/config-t06-reel-v1-brouillon5.json`, `b7a5c1baeee13f7589b296fb166180515422ebc8c7eff703994bb5b6835ae527` ; devis v3 : `docs/notes/g0-deux-semaines-v1/devis-T0.6-dose-reponse-v3.md`, `10965742f1d82ddb25239e4860c345b17dd4c2a1a1685d3abcacc20cfe6d00d3` |
| Chaîne | **La chaîne v12 n'accepte que GO-2026-11-06-01 et GO-2026-11-07-08** en épreuve, et exige `go_id = GO-2026-11-02-28`, `plafond_usd = 200` et un préenregistrement en course (`scripts/lancer_t06_v12.sh` l. 82–84, 156 ; `session_v11.py` l. 24–37 ; `configuration_v5.py` l. 16–38 et `configuration.py` l. 120–123 ; `amorce_instance_t06_v10.sh` l. 233–239) : ce run se joue sur la chaîne v13 (`scripts/lancer_t06_v13.sh`, `src/controle_ia/t06/session_v12.py`, `configuration_v6.py`, `scripts/amorce_instance_t06_v11.sh`, noms neufs) dont la seule différence est la ligne de GO passée par `GO_ID` et vérifiée contre `registres/go.md`, le plafond d'épreuve étant celui de la ligne (plus de borne à 8 USD), et `PREREG_ABSENT=1` permis sous toute ligne de calcul valide autre que celle de la course (rapport du développeur `rapport-chaine-t06-v13-v1.md`, § 4 et réserve 2 : six fichiers neufs, `lanceur_v6.py` compris, 95 essais R5 verts, livrés dans `livrables/chaine-t06-v13-v1.zip`, `98f7d4cd…`) ; contre-lue (R2) et déposée sur `7822a65b` avant le scellement de cet ordre : `<<COMMIT_V13>>`. La liste figée des essais sur l'instance (v2) ne contient pas `tests/test_t06_chaine_v13.py` : ces 95 essais sont joués sur processeur par la mère avant la création, dernière ligne citée au compte rendu |
| Code (commit d'épreuve) | `<<COMMIT_EXPLO>>` sur la branche `prep/t06-explo-v1` (`T06_BRANCHE_CODE`) = `7822a65b` + chaîne v13 (`<<COMMIT_V13>>`) + la configuration exploratoire et son compagnon + `registres/go.md` portant la ligne `<<GO_COURSE_EXPLO>>`, rien d'autre (vérifié par `git diff --name-only`, comme `c01d29ea` pour E3 bis) ; code de la garde identique à l'octet à `7822a65b` et à `a5c0e298` (E3 bis a joué `c01d29ea` ; `git diff --stat a5c0e298 7822a65b` vide sur `harnais/`, `t06/lanceur.py`, `lanceur_v5.py`) |
| Branche poussée (R12) | `essai/t06-explo-v1` = `T06_BRANCHE`, branche poussée par l'instance (`essai/…` exigé) ; jamais `main`, jamais `prep/t06-course-v12` ; une branche `essai/…` neuve par instance |
| Carte | A100 SXM4 80 Go, `prix_max_usd_h` **1,30** pendant la fenêtre de GO-2026-11-07-02 (12 recherches toutes les 15 minutes, 0 USD), puis **2,10** par une v2 de la configuration (R12) si la liste est vide (8 novembre 05:34Z : vide ; moins chère conforme 2,069) ; **pas de repli H200** dans ce run exploratoire (coût ×3, non justifié hors préenregistrement) ; étiquette d'offre neuve `t06-explo` |
| GO | ligne séparée de `registres/go.md`, type calcul, inscrite par la mère sous GO-2026-11-08-05 **avant son échéance (8 novembre ≈ 18:09Z)** : `<<GO_COURSE_EXPLO>>`, **plafond demandé 100 USD** (§ 8) ; GO-2026-11-02-28 (200 USD) n'est **pas** entamé : il reste à la lecture de confirmation préenregistrée |
| Dépense antérieure | `T06_DEPENSE_EPREUVES_ANTERIEURES_USD` = **0** (ligne séparée ; les 5,744 USD d'E2, E3, E3 bis restent sous leurs lignes, `registres/depenses.md` l. 385, 387, 390) ; pour une seconde instance, la facture relevée de la première |
| Mode | `reel`, `PREREG_ABSENT=1`, `T06_TESTS_ARGS` non défini, `T06_TESTS_ATTENDUS` vide (dernière ligne relevée et citée) |
| Pièces interdites | `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` jamais lus ; aucune pièce scellée modifiée |

## 2. Configuration exploratoire

**Une configuration, une instance** (l'amorce joue une configuration par instance, après la suite ciblée obligatoire). Fichier à créer sur `prep/t06-explo-v1`, avec compagnon : `docs/notes/g0-deux-semaines-v1/e3-ter-v1/config-t06-course-explo-v1.json` = copie de `config-t06-reel-v1-brouillon5.json` (`b7a5c1ba…`) avec, **et seulement avec**, ces champs changés :

| Champ | Candidat 12 (brouillon 5) | Exploratoire | Pourquoi |
|---|---|---|---|
| `fraction_equivalence` | 0,05 | **0,5** | garde exercée de fait : 64 × 10 = 640 paires (tâche, pas) indépendantes, les mêmes dans les six états → **320 actions contrôlées attendues par état dosé**, 1 280 à dose 0 (4 conditions), distillation 32 × 5 = 160 générateurs × 10 = 1 600 paires, 800 retenues, **1 600 actions contrôlées** (les deux conditions partagent le générateur) ; probabilité de moins de 10 contrôlées par phase ≈ 0 |
| `go_id` | GO-2026-11-02-28 | `<<GO_COURSE_EXPLO>>` | ligne séparée |
| `plafond_usd` | 200 | **100** | plafond de la ligne |
| `calendrier` | fin du 16 novembre | `dernier_jour_creation` 9 novembre, `fin_go_utc` = `<<FIN_GO_EXPLO>>` | égal à l'échéance de la ligne (l'amorce l'exige) |
| `carte.course.prix_max_usd_h` | 1,30 | 1,30 (v1), 2,10 (v2 si fenêtre vide) | § 1 |
| `carte.relance` (H200) | présente | **retirée** ou prix 0 `<<À VÉRIFIER : forme acceptée par configuration_v6>>` | pas de repli H200 |
| `offre.etiquette` | — | `t06-explo` | inventaire par étiquette sans confusion |

Tout le reste est celui du candidat 12 : T = 10, lot 8, `max_nouveaux` 400, six états, 64 tâches d'évaluation (`76cdeace…`), 32 tâches de réserve pour la distillation (`8d20a698…`), 480 pas, couches 7/15/23, familles descriptives, Mahalanobis `produit_matriciel_v2`, `tolerance_equivalence` 0,2, `statistique_equivalence` `q99`, `actions_min_controle_negatif` 10, `positions_min_controle_negatif` 4, `fraction_min_controle_negatif` 0,95, sondes figées de P3 et textes de P3 tels que la configuration les cite. **Aucune valeur de lecture n'est changée** : ce qui est exploratoire, c'est le statut du run, pas sa mesure.

Surcoût de la fraction 0,5 : la capture des activations pendant la génération porte sur la moitié des actions au lieu d'un vingtième ; la passe unique est jouée pour tous les épisodes dans les deux cas ; surcoût estimé ≤ 10 % du temps de génération et mémoire de capture par lot `<<À VÉRIFIER par le développeur v13 : pic de mémoire à lot 8, T = 10, fraction 0,5, A100 80 Go>>`.

## 3. R5 : la garde d'équivalence exercée de fait

- **Cas sain** (carte, ce run) : sens « passage » des deux sous-gardes, avec adaptateurs injectés, à T = 10, sur ≈ 320 actions contrôlées par état dosé : attendu « conforme » pour les six états et la distillation, ou l'un des deux arrêts lus d'avance (§ 6).
- **Artefacts** (processeur, joués **sur l'instance même** par la suite ciblée obligatoire avant le run, liste `scripts/tests-cibles-t06-v2.txt`, empreinte `417f637e…` écrite en dur dans l'amorce) : `tests/test_harnais_lots.py` — `test_garde_d_equivalence_sur_relecture_desalignee` (l. 93 : inéquivalence réelle → arrêt), `test_controle_negatif_zone_generee_artefact` (l. 103), `test_controle_negatif_de_phase` (l. 127), `test_controle_negatif_sain_et_aveugle` (l. 169), `test_defaut_d1_injecte_dans_les_positions_decodees` (l. 177). La dernière ligne de la suite est citée au compte rendu ; un échec arrête l'instance avant le run.
- **Limite écrite** : l'arrêt n'est pas observé sur la carte à adaptateurs injectés ; il l'est sur processeur. Un arrêt observé sur carte (configurations à tolérance 10⁻⁹ et 10⁶, une instance chacune) reste possible sur devis et nœud ; pas dans cet ordre.

## 4. Ce que l'on lit à la fin, et ce que cela décide

Tout est lu **après** scellement du `diag/` et du manifeste sur la branche d'essai, par des scripts de lecture sur processeur ; chaque sortie porte « EXPLORATOIRE, NON OPPOSABLE (R-522) » dans son nom et son en-tête.

**A. Comptes (règlent E3-6, dimensionnent la chaîne)** — script neuf `scripts/extraire_garde_equivalence_t06_v1.py` (lecture de ces seules clés, essais sur un `diag/` factice cas sain et artefact, écrit et contre-lu avant la création) : dans `diag/<run>/episodes-t06.json`, `fiches[k].equivalence` regroupées par `fiches[k].phase` (l'extracteur v1, l. 39 et 54, lit `etats[<état>].equivalence`, clé que la chaîne n'écrit jamais : `etats` ne porte que `adaptateur`, `dose`, `empreinte` ; à ne pas utiliser) : actions contrôlées (`len(equivalence.actions)`), plus grand `ecarts_q99` et plus grand `ecarts` par couche, tolérance ; `controles_negatifs[<état>]` (`comparables`, `passent`, `courtes`, `echecs`, `fraction`, `min_des_maxima`, `lecture`) ; `diag/<run>/distillation-t06.json` → `controle_negatif_donnees` seul (aucun écart par action n'y est écrit : `comparables + courtes` tient lieu de nombre d'actions contrôlées). Durées par étape (journal `PROGRES`), pic de mémoire, dépense relevée. **Décide** : la ligne du registre qui remplit `<<REGLEMENT_E3_6>>` ; la fraction de la lecture de confirmation (0,05 si tout est conforme ; sinon nœud) ; la règle du contrôle négatif à T = 10 si la lecture (ii) du § 6 survient ; les heures réelles pour le devis de la confirmation.

**B. Courbes et tables exploratoires (servent à écrire la confirmation, jamais à la remplacer)** — par l'extracteur de mesures de la chaîne (`extraire_mesures_epreuve_t06_v1.py` pour tout sauf la garde) : courbe dose–réponse (aire par état S25…S100, T100, dose 0 par condition, plancher aléatoire apparié, intervalles par les tirages de la configuration), coût par condition, tables du test croisé et des couples descriptifs (trois couches). **Décide**, pour le préenregistrement de confirmation : la puissance (nombre de tâches, de tirages), les seuils gelés, la forme de la courbe attendue (monotone ou non), les couches lues. **Ne décide pas** : les critères 2 et 3 de G0, qui restent ceux du programme et du candidat ; aucun seuil ne sera posé « juste au-dessus » d'un résultat exploratoire (R3) ; une courbe trop propre déclenche le même audit qu'une courbe plate (R4).

**Non lu dans ce run** : rien n'est interdit à la lecture, mais rien n'est opposable ; la lecture de B se fait après celle de A, et toute lecture est consignée (qui, quand, quoi) dans `registres/decisions.md`, pour que le préenregistrement de confirmation puisse écrire ce que ses auteurs savaient.

## 5. Étapes (fille d'exécution)

0. **Préalables de la mère** : chaîne v13 contre-lue (`<<COMMIT_V13>>`) ; branche `prep/t06-explo-v1` avec la configuration, son compagnon et la ligne `<<GO_COURSE_EXPLO>>` dans `registres/go.md` (`<<COMMIT_EXPLO>>`, ancêtre de `refs/remotes/origin/prep/t06-explo-v1`) ; script `extraire_garde_equivalence_t06_v1.py` écrit et contre-lu ; cet ordre scellé ; ligne d'engagement dans `registres/depenses.md` (« exploratoire, R-522 »).
1. **Contrôles** : d'abord, sans rien créer, `GO_ID=<<GO_COURSE_EXPLO>> T06_REGISTRE_GO="$REGGO" bash scripts/lancer_t06_v13.sh --verifier-go-seulement 100` (code 0 attendu) ; puis `W=$(mktemp -d)` ; `env -i … GO_ID=<<GO_COURSE_EXPLO>> T06_BRANCHE_CODE=prep/t06-explo-v1 T06_REGISTRE_GO="$REGGO" T06_DEPENSE_EPREUVES_ANTERIEURES_USD=0 T06_BRANCHE=essai/t06-explo-v1 bash scripts/lancer_t06_v13.sh controles-epreuve "$W/explo" "$COMMIT" "$CFG"` (`$REGGO` : registre d'un clone de `main` ; `$COMMIT` = `<<COMMIT_EXPLO>>` ; `$CFG` = chemin de la configuration) → attendu code 0, « CONTRÔLES D'ÉPREUVE CONFORMES … plafond 100 USD … mode reel ». Tout autre code → arrêt.
2. **Création**, sur le modèle de l'ordre scellé d'E3 bis (`docs/procedures/ordre-fille-6-t06-e3bis-v3.md` l. 40–50) : `env -i … VAST="$VAST" GO_ID=<<GO_COURSE_EXPLO>> T06_REGISTRE_GO="$REGGO" T06_DEPENSE_EPREUVES_ANTERIEURES_USD=0 T06_BRANCHE=essai/t06-explo-v1 T06_TESTS_ATTENDUS= bash scripts/lancer_t06_v13.sh creation auto course 0 "$W/explo"` qui IMPRIME la commande (garde de calcul rejouée, `GO_ID=<<GO_COURSE_EXPLO>>`) ; la fille l'exécute **une seule fois**, sans valeur de clé affichée ; `apres-creation` est appelé par cette commande ; puis `surveillance <ID> "$W/explo"` en tâche de fond. Fenêtre à 1,30 : 12 recherches à 15 minutes ; vide → compte rendu à la mère, qui décide la v2 à 2,10 (jamais la fille seule).
3. **Suite ciblée** : jouée d'office par l'amorce avant le run (liste v2, 1 914 essais attendus ; E3 bis : liste v1, 1 878 en 4 009,6 s) ; ≈ 1,1 à 1,3 h, comptée au devis.
4. **Run** : surveillance par le journal ; aucune lecture de résultat pendant le run ; l'amorce arrête l'instance en fin de run (code 0) ou sur arrêt consigné (code 1, `diag/<run>/arret.json`), traces poussées sur `essai/t06-explo-v1`. Le bras B de l'audit de fuite (GO-2026-11-07-04) **n'est pas joué** dans ce run exploratoire `<<À VÉRIFIER : l'amorce v10 le lance-t-elle d'office après la course ? si oui, la v13 doit le débrayer sous la ligne exploratoire>>`.
5. **Rapatriement** : `git fetch origin essai/t06-explo-v1` (refspec explicite) ; `diag/<run>`, `runs/<run>/manifeste.json`, journal, `lancement.txt`, compagnons vérifiés (`verifier-arbre`).
6. **Destruction par identifiant** (R10) si l'amorce ne l'a pas faite ; inventaire avant et après par champs filtrés de `vastai show instances --raw` (identifiant, étiquette, état, prix, durée), **jamais le brut affiché** ; instances 58936096, 58936099, 58936100 jamais touchées.
7. **Lecture A puis B** (§ 4) sur processeur, par la mère ou un lecteur qu'elle désigne ; **compte rendu** (§ 7).

Consignes permanentes : clés par leur nom seulement (`VAST_API_KEY`), jamais `env`/`printenv`/`set`/`export -p`/`/proc/*/environ` ; garde des secrets à 0 avant tout commit ; `git fetch` toujours avec refspec explicite ; aucun appel de modèle, aucune autre dépense ; **la fille n'engage aucune dépense sans le mot écrit de Lazar dans sa propre session** (GO-2026-11-08-05, `registres/go.md` l. 276 ; R-1819) — sauf si elle est la fille clés 2 et agit avant ≈ 21:34Z sous GO-2026-11-08-09 (l. 280), sur cet ordre scellé et la ligne de GO inscrite ; la ligne est inscrite par la mère avant l'échéance de GO-2026-11-08-05 (≈ 18:09Z).

## 6. Arrêts

- Offre hors seuils, carte autre que l'A100 80 Go, prix > `prix_max_usd_h` : pas de création.
- Dépense cumulée > plafond de la ligne (100) : la garde de dépense de la chaîne arrête (heure de dépense épuisée calculée à la création) ; destruction par identifiant ; compte rendu. **Aucune coupe au temps** (GO-2026-11-02-28 : « aucun budget de temps qui coupe une étape ») ; durée au-delà du pire cas : compte rendu à la mère, sans destruction hors de la garde de dépense.
- `GardeArret` : arrêt du run, sans relance par la fille ; résultat rapporté avec message et phase. Deux lectures écrites d'avance : (i) « activations de génération ≠ passe unique » : inéquivalence réelle à la tolérance 0,2 (défaut de chaîne ou de tolérance) ; (ii) « aveugle au décalage d'un jeton » : le 99ᵉ centile du contrôle négatif ne voit pas le décalage sur les actions courtes à contexte long (`activations.py` l. 157–160, 171–173 : centile pris sur le contexte non décalé suivi de la zone générée décalée ; à T = 10, une action d'au moins 4 positions décodées mais courte devant son contexte peut « échouer » ; au-delà de 5 % des comparables d'une phase, la phase s'arrête) ; on rapporte `echecs`, `comparables`, `courtes`, `min_des_maxima`. Dans les deux cas : nœud de Lazar avant toute relance (tolérance, règle du contrôle négatif à T = 10, ou développeur). Ce second arrêt n'est pas un défaut du run : c'est ce que la confirmation rencontrerait.
- Erreur de mémoire ou de chaîne avant le premier épisode d'évaluation : compte rendu ; relance = nœud (dépense cumulée).
- Suite ciblée en échec : l'amorce arrête avant le run ; compte rendu, sans relance.

## 7. Compte rendu de la fille (nombres seuls, ≤ 300 mots)

Comptes A du § 4 pour les six états et la distillation ; dernière ligne de la suite ; arrêt oui/non, message, phase ; durées par étape ; prix de l'offre, durée de carte, dépense relevée (carte, stockage, téléchargement), identifiant créé et détruit, commit de la branche d'essai, empreintes des `diag/` et du manifeste ; écarts à l'ordre. **La fille ne lit pas B** : courbes et tables sont lues par la mère après les comptes.

## 8. Devis

Bases : devis v3 de la course (`10965742…`) et E3 bis (`registres/depenses.md` l. 390, journal) : calcul 12,3 à 17,9 h de carte pour la course (distillation, 576 épisodes d'évaluation × 10 pas, test croisé), divers 1,84 h (installation 0,10, clonage 0,02, suite 1,14, fin de run 0,25 ; bras B 0,33 retiré ici) ; surcoût de la fraction 0,5 ≤ 10 % de la génération (≈ +0,5 à 1 h) ; stockage arrêté jusqu'à la lecture des comptes (48 h × 0,0417 ≈ 2) ; téléchargement 1 à 2.

| Scénario | Heures de carte | USD à 1,30 (fenêtre) | USD à 2,07 (prix du 8 novembre) |
|---|---|---|---|
| **Attendu** (une instance, hôte nominal) | 14,5 à 20,5 | ≈ 22 à 31 | ≈ 33 à 46 |
| Pire P1 : hôte 2× plus lent | ≈ 38 à 41 | ≈ 53 à 57 | ≈ 82 à 88 |
| Pire P2 : P1 + relance complète après erreur avant tout épisode d'évaluation (**nœud**, hors plafond demandé) | + ≈ 22 | ≈ 86 | ≈ 134 |

**Instances** : **une seule** pour le cas nominal ; la configuration du candidat tient sur une A100 de 80 Go (E3 bis : pic mesuré, même code, lot 8 ; T = 10 et fraction 0,5 à vérifier par le développeur). Une **seconde instance** n'arrive que (a) si la fenêtre à 1,30 est vide : même ordre, configuration v2 à 2,10, décision de la mère, 0 USD perdu ; (b) sur relance après erreur : nœud de Lazar, ligne nouvelle. **Plafond demandé pour `<<GO_COURSE_EXPLO>>` : 100 USD** : couvre l'attendu et le pire cas P1 au prix du jour ; P2 est un nœud. **Variante minimale** (si Lazar préfère un galop avant la course) : le brouillon 2 du galop E3 ter (4 tâches, T = 10, fraction 0,5, ≈ 4 à 7 USD attendus, plafond 16) — il règle E3-6 mais ne donne aucune courbe ; variante intermédiaire : 16 tâches d'évaluation tirées des 64 (fichier de tâches neuf à sceller, 160 paires, 80 contrôlées par état, ≈ 5 à 7 h, ≈ 15 à 20 USD à 2,07, plafond 40), courbe exploratoire à faible puissance. **Recommandation** : la course entière (64 tâches), une instance, plafond 100 ; confiance 0,65 ; raison : Lazar veut la course maintenant, et la confirmation préenregistrée a besoin de la vraie taille pour calculer sa puissance.

## 9. Ce qui suit le run

1. Lecture A par la mère ; ligne de `registres/decisions.md` qui règle E3-6 (six états : actions contrôlées, écart q99 maximal, tolérance, lecture du contrôle négatif ; distillation : bilan ; essais processeur : dernière ligne de la suite ; référence à ce run, commit, empreintes). Elle remplit `<<REGLEMENT_E3_6>>` de l'ordre de course de confirmation.
2. Lecture B, consignée ; **aucun chiffre de B dans un préenregistrement comme prédiction** : le préenregistrement de confirmation (candidat 12 r3 ou suivant) écrit sa prédiction depuis le programme et P3, cite ce run comme « exploratoire, vu par les auteurs », et fixe la puissance d'après les heures et les variances **de forme** observées, non d'après le signe.
3. Contre-lecture (R2), scellement, GO sur GO-2026-11-02-28 (200 USD, échéance 16 novembre : à prolonger si besoin, nœud), course de confirmation : run neuf, graines neuves, verdict par lecteur neuf (R13).
4. Si arrêt (i) ou (ii) : nœud de Lazar avant toute confirmation.

## 10. Marqueurs restants (à remplir par la mère avant la contre-lecture)

`<<COMMIT_V13>>` (chaîne v13 contre-lue, `PREREG_ABSENT=1` permis sous la ligne exploratoire, plafond = ligne) ; `<<COMMIT_EXPLO>>` (commit d'épreuve sur `prep/t06-explo-v1`) ; `<<GO_COURSE_EXPLO>>` (ligne de GO, plafond 100) ; `<<FIN_GO_EXPLO>>` (échéance de la ligne = `calendrier.fin_go_utc`). Deux `<<À VÉRIFIER>>` pour le développeur v13 : forme de la configuration sans repli H200 ; pic de mémoire à fraction 0,5 ; et un pour l'amorce : bras B débrayé. `<<REGLEMENT_E3_6>>` appartient à l'ordre de course de confirmation.

## 11. Ce qui distingue cet ordre d'un préenregistrement, écrit pour qu'on ne s'y trompe pas

Il n'a ni hypothèse, ni prédiction chiffrée, ni seuil, ni plan d'analyse gelé, ni verdict ; il a un périmètre, une configuration citée à l'octet, des gardes, un devis, une liste d'arrêts et une règle de lecture. Il est scellé pour que l'on sache ce qui a été lancé, pas pour rendre son résultat opposable. R1 reste entière pour la lecture de confirmation.

## 12. Corrections de la contre-lecture cl1 du galop reprises ici

| Remarque | Reprise dans cet ordre |
|---|---|
| CLE3T-01, -03 | chaîne v13 `<<COMMIT_V13>>` ; commit d'épreuve `<<COMMIT_EXPLO>>` sur `prep/…` ; branche `essai/…` = branche poussée ; garde identique à l'octet (`a5c0e298`, `7822a65b`, E3 bis a joué `c01d29ea`) |
| CLE3T-02 | une configuration par instance ; suite ciblée d'office comptée ; artefacts par les essais processeur (option D) |
| CLE3T-04 | dépense antérieure 0, ligne séparée |
| CLE3T-05, -06 | « jamais exercée avec adaptateurs injectés » ; clés exactes de lecture, extracteur v1 écarté pour la garde, `distillation-t06.json` → `controle_negatif_donnees`, script neuf contre-lu |
| CLE3T-07 | deux lectures d'avance de l'arrêt du cas sain (§ 6) |
| CLE3T-08 | commandes `controles-epreuve` / `creation auto course 0` / `surveillance`, variables `T06_*`, `$REGGO` |
| CLE3T-09 | devis refait sur le devis v3 et E3 bis, suite comptée, pire cas, plafond couvrant P1 |
| CLE3T-10 | mot de Lazar dans la session de la fille (R-1819), exception fille clés 2, ligne inscrite avant 18:09Z |
| CLE3T-11, -12 | paires et actions distinguées ; « moins de 10 contrôlées » |
| CLE3T-13, -14 | message exact ; `arret.json` et « arrêt consigné pendant le run » |
| CLE3T-15 | aucune coupe au temps |
| CLE3T-16 | inventaire par champs filtrés de `vastai show instances --raw`, jamais le brut |
| CLE3T-17 | « reçu du sous-agent rédacteur » ; (R-1769 ; R-1784 ; R-1825, point 4) |
| CLE3T-18 | 1,30 d'abord, 2,10 ensuite ; étiquette d'offre neuve |
