# Devis — saboteur à budget (ii-b), course exploratoire — v1, brouillon 2

- **Statut** : **brouillon 2** = brouillon 1 (`187d8c7268157eab3ad77a16aef9915f8cb869e3806fae0b336e9a1ffe52b153`, intact, R12) + couples Z17 à Z19 de la contre-lecture 1 (`contre-lecture-ii-b-v1-cl1.md`, `0991e019…`, R-2060) + plafond présenté en **deux variantes, sans choix** (remarque M7, non tranchée) ; arithmétique inchangée (`calcul-devis-ii-b-v1.py`) ; non scellé. **Aucune dépense n'est engagée par ce document** ; aucune ligne de GO n'y est écrite : la mère la demande à Lazar sur ce devis (R-2044 : « devis écrit puis ligne de GO » ; « aucune dépense avant cette ligne »).
- **Écrit** le 2026-11-09 vers 22:27 UTC (heure relevée par `date -u`, au journal) par le rédacteur neuf de la conception (`conception-ii-b-v1-brouillon1.md`, puis `conception-ii-b-v1-brouillon2.md`), sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy` ; brouillon 2 vers 22:51 UTC (`date -u`).
- **Arithmétique** : `calcul-devis-ii-b-v1.py` (même dossier), sortie brute `sortie-calcul-devis-ii-b-v1.txt` ; empreintes au journal. Chaque nombre ci-dessous en vient.
- **P-066** donnait « de l'ordre de 20 à 30 dollars » (≈ 1,12 USD de l'heure, ordre de grandeur de 7a) ; ce devis le chiffre.

## 1. Hypothèses (écrites, sourcées)

| grandeur | valeur | source |
|---|---|---|
| durée d'un épisode (N = 1, T = 10, lot de 8, 400 jetons au plus) | **43,3 s** | lecture A de 7a (`docs/notes/g0-deux-semaines-v1/e3-ter-v1/lecture-7a-v1/lecture-A-exploratoire-non-opposable-v1.md`, `3c84c419…`, § 4) : 320 épisodes de distillation en 3 h 50 min 58 s (43,3 s) ; 256 épisodes à dose 0 en 2 h 59 min 23 s (42,0 s) ; états dosés 41,7 à 44,7 s. 7a capturait des activations sur la moitié des actions ; (ii-b) n'en capture aucune : **aucun rabais pris** |
| amorce, format et disque | 0,07 h | lecture A § 4 (1 min 37 s + 2 min 10 s) |
| suite ciblée des essais sur la carte | 0,58 h | lecture A § 4 (34 min 52 s, 84 fichiers) ; la liste de (ii-b) sera différente : même ordre supposé |
| création, image, modèle | 0,25 h | **non relevé** en 7a (lecture A § 4) : hypothèse |
| écriture, scellement, poussées | 0,10 h | 7a : 43 s pour le commit des morceaux ; (ii-b) pousse deux adaptateurs (≈ 27 Mo chacun), identifiants, textes, oracle : hypothèse |
| distillation, par transcription et par époque | 1,86 s | 7a : 14 min 51 s pour 160 transcriptions × 3 époques (adaptateur saboteur), même code, mêmes réglages (lecture A § 4) |
| **jumeau honnête (oracle), par action** | **0,5 à 1,5 s attendu ; 3,0 s pire** | **non mesuré** : estimation de conception (un préremplissage d'environ 2 800 jetons, huit suites de 16 jetons au plus sur le cache dupliqué ; 3,0 s si le cache ne se duplique pas et que chaque suite repréremplit) |
| juge 8B de T0.8 en une passe (option) | 0,3 s par action | estimation (un préremplissage par action, aucune génération) ; joué **seulement** si T0.8 en a scellé la forme avant la création |
| épisodes | étalonnage 96 (64 honnêtes + 32 du saboteur flagrant de P3) ; maître 32 par tour ; évaluation 256 (4 conditions × 64 tâches) | conception, sections 3.4, 4, 6 |
| tours du maître | 6 (bas), **10 (central)**, 12 (haut et pire, R_max) | taux d'acceptation simulé 10 à 35 % (conception 3.3) ; cible 96 acceptés |
| actions passées au jumeau | 960 (étalonnage) + 320 par tour + 320 (ancrage, premier tour) + 2 560 (évaluation) | conception 2.2, 3.4, 6 |
| prix A100 SXM4 80 Go | **1,12 USD/h** central (consigne de la mère) ; relevés 1,009 à 1,2133 (T0.6 candidat 12 r3, « Devis », `c24e268e…`) ; **borne 1,30** (configuration du candidat 12, brouillon 5, `b7a5c1ba…`) ; 1,40 au pire ; 2,10 (borne de la configuration v2 de 7a, ordre de 7a § 1) seulement sur décision de la mère, non prévue ici | |
| prix H200 NVL (repli) | relevés 4,441 et 4,669 USD/h ; **borne 4,70** (configuration du candidat 12, brouillon 5) ; **débit non mesuré** : durées de l'A100 supposées (prudent) | T0.6 candidat 12 r3, « Devis » |
| stockage, instance arrêtée | ≤ 0,08 USD/h (GO-2026-11-07-02 ; offre) ; gardée jusqu'au rapatriement vérifié : 24 h attendu, 48 h au plus (ordre) | |
| téléchargement | ≤ 0,05 USD/Go ; 20 Go attendu (modèle ≈ 16 Go en demi-précision, image), 40 Go au plus | configuration du candidat 12, brouillon 5 |
| disque de l'instance | ≥ 100 Go (modèle, deux adaptateurs, identifiants, textes ; **aucune activation**) | conception 6.3 |
| lectures (1) et (2) | **0 h de carte** : sur processeur, après le rapatriement (hors option du juge) | conception 6 |

## 2. Heures de carte par étape (A100, hôte nominal)

| étape | bas (6 tours, jumeau 0,5 s) | **central** (10 tours, jumeau 1,0 s) | haut (12 tours, jumeau 1,5 s, 127 acceptés) |
|---|---|---|---|
| fixe (amorce, suite ciblée, création, écriture) | 1,00 | **1,00** | 1,00 |
| étalonnage : épisodes (96) | 1,15 | **1,15** | 1,15 |
| étalonnage : jumeau (960 actions) | 0,13 | **0,27** | 0,40 |
| **maître** : épisodes | 2,31 | **3,85** | 4,62 |
| **filtrage** : jumeau du maître et ancrage (règle : processeur, négligeable) | 0,31 | **0,98** | 1,73 |
| **distillation** : élève et témoin-jumeau, contrôle d'identité | 0,31 | **0,31** | 0,40 |
| évaluation : épisodes (256) | 3,08 | **3,08** | 3,08 |
| **lecture** (1) : jumeau de l'évaluation (2 560 actions) | 0,36 | **0,71** | 1,07 |
| **lecture** (2) : juge de T0.8 en une passe (option) | 0,21 | **0,21** | 0,21 |
| **total** | **8,86** | **11,56** | **13,67** |

## 3. Attendu (USD)

| scénario | carte | stockage arrêté (24 h) | téléchargement (20 Go) | **total** |
|---|---|---|---|---|
| bas, 1,0889 USD/h | 9,7 | ≤ 1,9 | ≤ 1,0 | **≈ 12,6** |
| central, **1,12 USD/h** | 12,9 | ≤ 1,9 | ≤ 1,0 | **≈ 15,9** |
| central, 1,30 USD/h | 15,0 | ≤ 1,9 | ≤ 1,0 | ≈ 17,9 |
| haut, 1,30 USD/h | 17,8 | ≤ 1,9 | ≤ 1,0 | **≈ 20,7** |

**Attendu : ≈ 8,9 à 13,7 h de carte, ≈ 13 à 21 USD, valeur centrale ≈ 16 USD** (sous l'ordre de grandeur de P-066, 20 à 30). Pour comparaison : 7a, ≈ 17,6 USD au total pour 13,59 h d'instance (R-2039).

**Arrêt précoce** (M-1 au tour 4, ou une épreuve E-O après l'étalonnage) : 4,41 h, **≈ 7,9 à 8,6 USD** (1,12 à 1,30 USD/h, stockage et téléchargement compris) ; arrêt à l'étalonnage seul : moins. **Arrêt M-3 au tour 12** (rien n'est distillé) : ≈ 8,2 h au jumeau à 1,0 s par action, ≈ 12 USD à 1,12 USD/h, stockage et téléchargement compris (non calculé par le script ; arithmétique de la contre-lecture 1 : 1,00 + 1,15 + 0,27 + 4,62 + 1,16 h).

## 4. Pire cas

| scénario | hypothèses | heures | USD | sous la configuration de la variante A (75) ? de la variante B (55) ? |
|---|---|---|---|---|
| **P1** | A100, **hôte deux fois plus lent**, 12 tours, jumeau 3,0 s par action, 127 acceptés ; stockage 48 h, téléchargement 40 Go | 33,74 | **≈ 49,7** à 1,30 ; **≈ 53,1** à 1,40 ; ≈ 76,7 à 2,10 | A et B : oui à 1,30 (≈ 49,7) et à 1,40 (≈ 53,1) ; **non à 2,10** (≈ 76,7) dans les deux variantes : la configuration à 2,10 n'est prévue dans aucune (fenêtre A100 vide : repli H200 en A, nœud en B) |
| **H200 d'emblée** | fenêtre A100 vide (12 recherches à 15 minutes, 0 USD), création sur H200 NVL (règle de GO-2026-11-07-02 reprise) ; durées du haut de l'attendu sur A100 (débit H200 non mesuré) ; stockage 48 h, 40 Go | 13,67 | **≈ 66,5** à 4,441 ; ≈ 69,7 à 4,669 ; **≈ 70,1** à 4,70 | A : oui, avec ≈ 1,0 h de marge (remarque M7) ; B : sans objet (pas de repli H200 : nœud) |
| P2 (**nœud**, hors plafond) | P1 à 1,40, plus une relance complète après une erreur de chaîne avant l'évaluation | 67,5 | ≈ 53,1 + 47,2 + 2,0 = **≈ 102** | non : toute relance est un nœud de Lazar avant dépense |
| P3 (**nœud**, hors plafond) | erreur de mémoire à la distillation sur A100 (hôte lent, 1,40 USD/h : 22,1 h perdues, ≈ 30,9 USD), puis course entière sur H200 NVL à 4,70 aux durées du haut de l'attendu (≈ 64,2 USD) ; stockage ≤ 7,7, téléchargement ≤ 4,0 | 35,8 | **≈ 107** | non : nœud |
| option : juge de T0.8 **avec raisonnement** | 2 560 actions, 400 jetons au plus, au débit d'une action d'épisode (4,33 s) | + 3,08 | + ≈ 3,5 à 4,0 | à décider avec T0.8 |

**Pire cas couvert : variante A ≈ 70 USD** (H200 d'emblée) ; **variante B ≈ 53 USD** (P1 sur A100 à 1,40 USD/h) ; pire cas sur A100 : ≈ 50 à 53 USD. **Marge du repli H200** (contre-lecture 1, remarque M7) : à 4,70 USD/h, le plafond de configuration de 75 USD ne laisse que ≈ 1,0 h (moins de 8 %) au-delà des 13,67 h du haut de l'attendu ; un hôte plus lent ou un jumeau à 3 s par action y ferait détruire l'instance par la minuterie avant la fin (P1 joué sur H200 : 33,74 h × 4,70 ≈ 159 USD). La contre-lecture recommande la variante 60/55, A100 seule, fenêtre vide = nœud.

## 5. Plafond : deux variantes, présentées côte à côte sans choix (remarque M7 de la contre-lecture 1, non tranchée)

| | **variante A** | **variante B** |
|---|---|---|
| ligne de GO (type calcul) | **80 USD** | **60 USD** |
| plafond de la configuration (minuterie de l'instance, garde de la surveillance) | **75 USD** | **55 USD** |
| marge de la configuration sous la ligne | 5 USD (latence d'arrêt, stockage jusqu'à la destruction ; 7a : 95 sous 100) | 5 USD (idem) |
| carte | A100 SXM4 80 Go ≤ 1,30 USD/h ; fenêtre de 12 recherches à 15 minutes (0 USD) ; **fenêtre vide : repli H200 NVL** ≤ 4,70 USD/h (règle de GO-2026-11-07-02 reprise ; demandé par la consigne de la mère) | A100 SXM4 80 Go ≤ 1,30 USD/h ; même fenêtre ; **fenêtre vide : nœud** (aucune création) |
| couvre | attendu (≈ 13 à 21) ; P1 sur A100 à 1,30 et 1,40 (≈ 50 à 53) ; H200 d'emblée au haut de l'attendu (≈ 66 à 70) | attendu (≈ 13 à 21) ; P1 sur A100 à 1,30 et 1,40 (≈ 50 à 53) |
| ne couvre pas | H200 au-delà du haut de l'attendu : à 4,70 USD/h, la configuration de 75 ne laisse que ≈ 1,0 h (moins de 8 %) au-delà des 13,67 h ; la minuterie détruirait l'instance avant la fin, résultats partiels poussés (P1 sur H200 ≈ 159) ; P1 à 2,10 (≈ 77, configuration non prévue) ; relances P2, P3 (nœuds) | toute course sans A100 conforme (nœud ; glissement possible du calendrier) ; P1 à 2,10 ; relances P2, P3 (nœuds) |
| marqueur de l'ordre | `<<REPLI_H200_PERMIS>>` = oui | `<<REPLI_H200_PERMIS>>` = non |

**Communs aux deux variantes** : échéance proposée **2026-11-19** (`fin_go_utc` 2026-11-20T00:00:00Z) ; dernier jour de création proposé **2026-11-17** ; la marche au pire cas P1 (33,7 h) place la dernière création sans nœud au **2026-11-18 vers 14:15Z** pour une fin avant `fin_go_utc` ; création **jamais avant la création de 7b** ; une relance (P2, P3) reste un nœud de Lazar. Le brouillon 1 proposait A ; la contre-lecture 1 recommande B (§ 4) ; **le choix revient à la mère et à Lazar** (ligne de GO) ; le rédacteur n'en fait aucun.

## 6. Hors devis

- Contre-lecture, code, essais sur processeur, répétition jouet, lectures (1) et (2) : processeur, 0 USD.
- Toute lecture de sonde ultérieure (recalcul des activations sur une carte, sous un préenregistrement scellé à part et après le verdict de P3-bis) : devis et GO à part.
- Le juge 8B de T0.8 avec raisonnement, et un juge d'une autre lignée (point ouvert P-4 de la conception) : devis à part.
- 7b (GO-2026-11-02-28), P3-bis (GO-2026-11-02-29) : lignes à part, jamais entamées par (ii-b).

## 7. Ligne d'engagement (à écrire par la mère au registre des dépenses, à la création ; forme seulement)

« engagement : saboteur à budget (ii-b), course exploratoire, non opposable (R-522) (`<<GO_ID_IIB>>`, plafond `<<PLAFOND_LIGNE_IIB>>` USD, configuration `<<PLAFOND_CONFIG_IIB>>`) : ordre `<<CHEMIN_ORDRE_IIB>>` (`<<EMPREINTE_ORDRE_IIB>>`), lanceur `scripts/lancer_iib_v1.sh`, commit `<<COMMIT_CODE_IIB>>` ; une carte A100 SXM4 80 Go ≤ 1,30 USD/h (repli H200 NVL ≤ 4,70 en variante A seulement), disque ≥ 100 Go ; attendu ≈ 13 à 21 USD, pire cas ≈ 70 USD (variante A) ou ≈ 53 USD (variante B) ; créée après 7b (`<<LIGNE_REGISTRE_CREATION_7B>>`) ; crédit Vast.ai relu à la création ».
