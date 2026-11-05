# Erratum — synthèse de lecture du collisionneur N12-N13, v1 → v2 — v1

## En-tête

- **Lecteur de l'erratum** : sous-agent neuf, modèle **Claude Fable 5.1** (`claude-fable-5-1`) — même modèle que l'espèce A et que le lecteur de la v1 (dit en tête, critère 18). Je n'ai écrit ni les critères, ni la question, ni les faits, ni la synthèse v1, ni la relecture d'Opus, ni aucune cellule. Je ne décide rien, ne recommande rien, ne classe pas les espèces ; je ne modifie aucun fichier existant, ne scelle rien, ne commets rien ; aucun appel payant ni réseau ; aucune clé lue. Consigne appliquée : `consigne-erratum-synthese-n12-n13-v1.md` (`84a5d48f…`), point par point (RN-01 à RN-17, puis points 1 à 13).
- **Dates** (`date -u`) : début 09:38:26 UTC ; empreintes recalculées 09:39:25 UTC ; fin de la lecture complète 09:50:42 UTC ; 1er novembre 2026. Heure d'écriture et d'assemblage : voir la section « Longueurs et empreintes » en fin de fichier.
- **Lu en entier** : la consigne ; les critères N12-N13 et ceux du tour 1 des nœuds ; la synthèse v1 ; la relecture d'Opus (empreinte attendue `c05949af…`, vérifiée) ; la question v2 ; les faits v1 (887 lignes, six pièces, par morceaux) ; `etat.md` ; les douze cellules du run `run-n12-n13-e3-v1` (chacune égale à son compagnon, `sha256sum -c` : 12 OK) ; `docs/decisions/decision-N-053-v1.md` (point 5, cité par N-058). **Non lu** : `annexe-tour-2-n12-n13-v1.md` et tout fichier « annexe-tour-2 » ; `donnees/mode-tenu-a-l-ecart-v1`, `donnees/collisionneur-evasion-moniteurs-v1`, `donnees/bras-attaque-*`, `quarantaine/`, `donnees/runs/`, `diag/`, `prereg/P3-consignes-v1.md` ; les autres dossiers de `donnees/` ; les deux PDF.
- **Méthode** : chaque constat de la relecture est confronté aux cellules et aux pièces ; verdict **confirmé** / **infirmé** / **non tranchable** avec la raison ; correction = texte exact de remplacement, cité en annexe (original, puis remplacement) et appliqué par le script `appliquer-erratum-n12-n13-v1.py` (scratchpad de la session, non versé), qui vérifie que chaque chaîne originale est trouvée exactement une fois dans la v1 et s'arrête sans rien écrire sinon ; code de retour rapporté en fin de fichier. Les numéros de ligne « l. n » renvoient à la v1 ; « pièce N, l. n » aux faits v1 ; « X-Tn » aux cellules (T1 conception, T2 critique croisée, T3 réponse).

## Table des empreintes SHA-256 (recalculées par script le 1er novembre 2026 à 09:39 UTC ; recopiées, jamais retapées)

| Fichier | SHA-256 |
|---|---|
| `docs/notes/ideation-organisme-v1/course-2/collisionneur-n12-n13-v1/consigne-erratum-synthese-n12-n13-v1.md` (égale au compagnon) | `84a5d48f9d3eaf7d7f12c0072f80c204e1271048057d1d596a74c9ba60ea903e` |
| `…/collisionneur-n12-n13-v1/criteres-lecture-n12-n13-v1.md` (égale au compagnon) | `71b63584563eb6fc6cb7880ade286e31596c49583d2f7615f0b279cebff3c589` |
| `…/collisionneur-noeuds-v1/criteres-lecture-noeuds-v12-tour1-v1.md` | `22edbf4751c205f6760a136963bfaebcede773bfdc3300e923ad8e5df4e3a529` |
| `…/collisionneur-n12-n13-v1/synthese-n12-n13-v1.md` (égale au compagnon) | `b1d28f0d43245c3534d469f38e77bf4e14da2a70f39f4f1bd76a0b42c96b8cb4` |
| `scratchpad/relecture/relecture-opus-synthese-n12-n13-v1.md` (attendue `c05949af…`) | `c05949af2b93f6af4facec06009a89da9b05b033b1e401edfc1de6fcba51d2a7` |
| `donnees/collisionneur-n12-n13-v1/question-collisionneur-n12-n13-couches-recompense-v2.md` | `9faee0aadf01b4837fa67df414ed4552519d80c6c31c9326976c27e391de6986` |
| `donnees/collisionneur-n12-n13-v1/faits-n12-n13-v1.md` | `ccec9e944f9ea29bb7fd3c301489b256b3f0c48a4e66d5058007f9a23288677e` |
| `donnees/collisionneur-n12-n13-v1/run-n12-n13-e3-v1/etat.md` | `55488b3bd0e2c54bc946719b6b3a1f186b5f146c375761e8736cc6b75ebee5ab` |
| `…/cellules/E3-T1-conception-A.md` | `29f447f4723e1b19d00bf76f4d3f3ff2b934bf029ffc599df3722c1b846d1380` |
| `…/cellules/E3-T1-conception-B.md` | `4d1ddae8667aebddefd1a9d2b25d754b32ba80799bbf32e0f00aa56642f6f4ae` |
| `…/cellules/E3-T1-conception-C.md` | `6a08690ad4bc9cbe134341b294f1837136eae78e4e70790209026ef1bcc3b8e7` |
| `…/cellules/E3-T1-conception-D.md` | `0d81aa4bff6a11b1ce090104997a7ee2c2b62dbe5ce58f25aac61459034ef658` |
| `…/cellules/E3-T2-critique-croisee-A.md` | `833d4522e07c797296dac4bb5eeb6b9f0d2adeb0c2baeeec4b167f3b8a90a0f0` |
| `…/cellules/E3-T2-critique-croisee-B.md` | `b0779fe0afe7493f9a64ea3cfdd3ac9d3a5cafd28cae9e0b4e232d234d333869` |
| `…/cellules/E3-T2-critique-croisee-C.md` | `086996f154c869f2ba2bb1e327cc7d7391fe1ec2a3a2036e852869c2ca53d1f5` |
| `…/cellules/E3-T2-critique-croisee-D.md` | `040c404eccf2cb062ea4230e10911a9fada32dd265d0f03ae4103f30e73a199a` |
| `…/cellules/E3-T3-reponse-A.md` | `2ed08f6fe91e2d9fd655f946818183d942939ca2ff0edd91bba3352fc46e78cd` |
| `…/cellules/E3-T3-reponse-B.md` | `f81f771150c1188df897e1680a9057e1d86db2958831f16437366fde6db97c15` |
| `…/cellules/E3-T3-reponse-C.md` | `ef992475e9a4dd0b419459a4462f077c757852d469d9ae65fe8256918ee79470` |
| `…/cellules/E3-T3-reponse-D.md` | `61cad26929d813c5061ed7e1396fb570902eea3428477664303e64e98e0161e9` |
| `docs/decisions/decision-N-053-v1.md` | `2204256d744288be2708578c0fdc8c44c62a29b70b2727ed7e31ec142d1cdeae` |

## 1. Règles écrites (RN-01, RN-02, RN-03)

### 1.1 Accords (critères 7, 10 et 11 du tour 1 ; critères 3 et 12 de N12-N13)

- **Accord indépendant** : même position en T1, sur la même sous-question (l'unité du critère 12), chez au moins deux espèces, avec au moins une raison commune qui n'est pas vraie par construction. « Large » = trois ou quatre espèces ; accord à quatre = réserve R4 (critère 10).
- **Exclus** : (i) une position que la question impose ou cite — options listées, chiffres, décisions servies (critère 11), position de la pré-collision (critère 3 : « vrai par construction, pas un accord ») ; (ii) une position dont la seule raison commune est celle que la question donne ; (iii) une raison commune comptée comme un accord à part (double compte) ; (iv) une espèce qui ne tient la position qu'en T3 : c'est une convergence (critère 8), pas un accord ; (v) un lien N12-N13 : « tout lien est apport » (critère 13), pas un accord.
- **Accords sous cette règle** (quatre, tous larges) :
  - **N° 1 — N12 (1)**, A, B, C, D : ce qui est couvert par N-045 (composition et sélection apprises, instruments locaux entraînés par le noyau) contre ce qui ne l'est pas (écriture de code hors catalogue : moniteurs, opérateurs ; preuve formelle). Raison commune : la pièce 1, énoncé 1 (l. 71–75) décrit une composition dans un espace d'instruments existants ou entraînés, non l'écriture de code. Réponse littérale à la sous-question : « en partie » (A-T1 A2 ; D-T1 « Réponse courte »), « non » (B-T1 S1 et Verdict ; C-T1 (a) 1, pour la couche 3). Réserve R4.
  - **N° 2 — N12 (2), couche 4**, A, B, C, D : l'empreinte atteste l'identité ou l'antériorité d'un texte, pas la validité d'une preuve ; l'apport de la couche 4 est une vérification de propriété (A-T1 A5 ; B-T1 N12-E2 H_B et « Points de désaccord » 2 ; C-T1 (a) 2 ; D-T1 table N12, 5e ligne). Sous-raison factuelle commune à A et C : les coquilles de Damani (pièce 5, § 1.3, l. 656–659). Réserve R4 ; en T3, convergence vers le même comparateur (accord trop propre, inchangé).
  - **N° 3 — N13 (1)**, A, B, C, D : (c1) est la seule forme à contrefactuel ; (c3) n'est recevable que comme sous-produit de son bras collectif (A-T1 A10 ; B-T1 « Ce que N13 gagnerait à distinguer » 3 et « Ordre proposé » 5 : « N13-E2 conditionnelle à N13-E1 » ; C-T1 Duel 3 et (d) 2 ; D-T1 § 4 « synthèse »). Raison commune : la cause collective n'est pas établie, il faut le bras apparié (pièce 4, § 1.8 réserve 1, l. 427 ; A-T1 A7 ; B-T1 S6 ; C-T1 (a) 4 ; D-T1 table N13, 2e ligne) — raison non vraie par construction, puisque la question affirme l'inverse (« importerait le défaut »). Réserves : R4 ; effet d'ordre ((c1) présentée la première et avec le plus de détail) ; même pièce lue. B tient la position dès T1 (la v1 disait « rejoint en T3 »), avec une objection propre sur (c3) (RN-04).
  - **N° 4 — N13 (3)**, A, C, D : l'apport distinct de Damani est un chantier de mesure (métriques Brier, ECE, AUROC, extraction par phrase ajoutée) utilisable sans entraînement ; l'apport de l'entraînement reste à prouver contre les signaux bon marché (A-T1 A12 et E5 ; C-T1 (d) 2 et Duel 4 ; D-T1 § 4 « chantier de mesure distinct » et E13-4). Raison commune : pièce 5, § 3 (b) (l. 822–832 : « oui pour la mesure, sans entraînement »). Réserve « même pièce lue ». B place l'entraînement en premier (B-T1 N13-E3, « Ordre proposé » 1) et cède en T3 (convergence, famille 4).
- **Positions communes non comptées** : N12 (3) « étape 2 d'abord » à quatre — position de la pré-collision citée par la question (critère 3) et option de la question ; raisons partiellement communes (A-T1 A4 et B-T1 « Ce que N12 gagnerait à attendre » : l'expérience décisive exige l'étape 2 ; B et C : N-045 § 4) ; la réserve « effet d'ordre » tombe avec l'accord (RN-10). N13 (1) « (c2) écartée » à quatre — la raison commune est celle de la question (pas d'oracle, budget fixe, composition ≠ bisociation). N13 (3) « l'entraînement RLCR ne concerne qu'un juge local » (A-T1 A12 ; C-T1 (a) 6 ; D-T1 § 4 « n'entraîner aucun modèle de frontière » ; B par construction de N13-E3 sur un modèle de 7–8 milliards) — conséquence directe de N-045 énoncé 8 (décision servie, l. 116). N13 (2) « le signalement n'entre dans aucune récompense » : A et D dès T1 (A-T1 E3 ; D-T1 E13-1 et § 4), mais raisons différentes (A : lecture extensive de l'énoncé 8 ; D : une récompense du signalement « peut entraîner la métrique ») : pas de raison commune, non compté.
- **Liens 1, 3 et 6 (point 12)** : aucun n'est un accord. **Lien 1** : la dépendance de (c1) et (c3) à l'étape 2 est dans la question (vrai par construction) ; en T1, seuls B (S11 ; N13-E1 « requiert l'étape 2 » ; N12-E1) et C (Duels 1 et 3 logés dans l'étape 2) lient les deux nœuds à l'étape 2 ; A (E3 hors ligne, qui « peut la précéder », A-T3 « L'expérience à faire en premier ») et D (« pilote isolé », D-T3 § 3) ne le font pas pour N13 : la v1 (« quatre espèces ») était inexacte. **Lien 3** : l'usage des coquilles de Damani par A (A5, E2) et C ((a) 2, Duel 2) est la sous-raison factuelle de l'accord n° 2 ; le compter à part doublerait. **Lien 6** : D parle de la forme de la couche 4 (« vérificateur externe, sans imposer une couche 4 autonome », D-T1 « Réponse courte ») ; C de l'étanchéité du bac à sable de la couche 3, vérifiée de l'extérieur (C-T1 (c) instrument 2 ; pièce 4, l. 548) : deux objets, pas une position commune.
- **Décompte** : v1 « 7 dont 5 larges » → v2 **4, tous larges** (trois à quatre espèces, un à trois). Sous la lecture plus large de la v1 (positions communes comptées malgré le critère 3 et la raison de la question), on obtiendrait 7 ; la différence tient entièrement à la règle, qui est maintenant écrite.

### 1.2 Apports seuls (critère 12 du tour 1 ; critère 13 de N12-N13)

- **Règle** : option manquante, pire cas, lien ou pièce proposés par une seule espèce en T1 et jamais repris par une autre ; gardé s'il n'est pas réfuté en T2 (« contesté » ≠ « réfuté ») ; **retiré** s'il est né d'une critique (c'est une convergence, critère 8) ou repris par une autre espèce (c'est un accord ou une convergence).
- **Liste nominative après retrait** : 1 A E3′/E3′′ (diffusion sans entraînement) ; 2 A troisième mécanisme (contraction du raisonnement) ; 4 B risque inverse (coût d'opportunité d'un organisme figé, S3) ; 5 B calendrier (S4) ; 6 B l'oracle de N-058 ne mesure pas le signalement (S10) ; 8 C transposabilité du crédit plat aux petits effectifs ((a) 6) ; 9 C circularité du bac à sable ((a) 3 ; contesté par B-T2 sur C c3, maintenu C-T3 C2) ; 10 D résidu mesurable dans l'étape 2 (table N12) ; 11 D règle « non évaluable » (§ 3 table) ; **12 D (ajouté)** risque de la couche 3 : effets indirects, bac à sable non prouvé correct, déplacement du problème (table N12, 4e ligne) ; **13 B (ajouté, RN-04)** (c3) « circulaire », le motif d'Avalon n'étant pas diffus. **Retirés** : 3 A « faux trilemme » (substance tenue en T1 par B, C, D : accord n° 3) ; 7 B N13-E2a (né de A-T2 sur B a6 : famille 2) ; le risque de A (violation de N-053) n'était pas dans la liste de la v1 mais la l. 84 le disait « apport seul » : repris par C-T2 sur A (a1) comme prémisse du dilemme, il est la prémisse de la divergence n° 1. Le triple partage de D (omission fautive / non dû / non-action) est repris par A-T3 E4′ et B-T3 E2b (après C-T2 sur A c3 et D-T2 sur A c2) : convergence ; seule la règle « non évaluable » reste à D.
- **Les quatre risques de la couche 3 (l. 84)** : A (N-053) — repris, non apport seul ; B (coût d'opportunité) — apport seul n° 4 ; C (circularité) — apport seul n° 9 ; D (effets indirects) — apport seul n° 12, absent de la liste de la v1.
- **Répartition corrigée** : onze, **A 2, B 4, C 2, D 3** (v1 : A 3, B 4, C 2, D 2).

### 1.3 Cessions et divergences résolues (critères 8 et 9 du tour 1)

- **Cession** : une espèce adopte en T2 ou T3 ce qu'une *autre* espèce a porté. Une espèce qui applique sa propre critique à son propre dessin ne cède pas : « A sur lui-même » (famille 1, E3″ ≥ 3 graines) est retiré. « D l'avait » (famille 7, l. 131) est **infirmé** : D-T3 § 1 accepte explicitement la critique de B (« canaris et plancher initial insuffisamment spécifiés (B) — Acceptée — Le pré-test vérifie que le modèle de départ signale assez… ») ; D-T1 n'avait qu'un pilote de bruit, pas un pré-test de signalement. La cession de D est donc valide. **Cessions : 39 → 38.**
- **Divergence résolue** : parmi les cessions, celle qui change la position d'une espèce sur l'une des six sous-questions (critère 9 : « options différentes sur le même nœud », l'unité étant la sous-question) ; une cession sur un paramètre de méthode (estimateur, appariement, cible d'un instrument) reste une convergence. Toutes les divergences résolues sont donc aussi des cessions ; le chevauchement est déclaré. **Retenues (4)** : B, premier test = recalibration post-hoc (N13 (3), famille 4) ; C, (c2) écartée « par incompatibilité de protocole » (N13 (1), famille 13) ; C, témoins d'intégrité retirés de la récompense d'héritage (N13 (2), famille 6) ; B, bras « récompense du signalement » reclassé en intervention (N13 (2), famille 6). **Reclassées en convergences de méthode (2)** : D, appariement sur la performance supprimé (famille 8) ; A, E4 reposée sans contrat (famille 2). **Divergences résolues : 6 → 4.**
- **Divergences non résolues** : 9, inchangées ; l'étiquette « jamais » de la n° 5 est retirée (aucune espèce ne la porte, RN-11).

## 2. Table des verdicts — constats RN-01 à RN-17 de la relecture

| Constat | Ce que dit la v1 (citation, ligne) | Ce que disent les cellules ou les pièces (renvoi) | Verdict | Correction (annexe) |
|---|---|---|---|---|
| **RN-01** décompte des accords | l. 34 : « **7**, dont **5 larges** » ; n° 5 « B rejoint en T3 » ; n° 6 « cause collective non établie comme prémisse commune [4] » ; l. 162 lien 3 « accord indépendant » | Règle § 1.1. Sur le n° 5, B tient la position dès T1 (B-T1 « Ordre proposé » 5 : « N13-E2 conditionnelle à N13-E1 » ; point 3) : accord à quatre, non convergence. Le n° 6 est la raison du n° 5 (double compte). N° 3 : critère 3 (pré-collision citée) ; n° 4 : raison de la question ; n° 7 : conséquence de N-045 énoncé 8 (A-T1 A12 ; C-T1 (a) 6 ; D-T1 § 4). Liens 1, 3, 6 : pas des accords (§ 1.1) | **Confirmé** (décompte non reconstructible ; double compte du n° 6 ; n° 3, 4, 7 vrais par construction) ; **nuance sur le n° 5** : les cellules placent B en T1, ce que ni la v1 ni la relecture ne disaient | R03, R10, R18, R23, R32, R33, R34, R35, R56, R57, R58 ; décompte : 4, tous larges |
| **RN-02** apports seuls | l. 38 : « **11** » ; l. 84 : « Chacun est un **apport seul**, non réfuté » (quatre risques) ; l. 163 : risque de A « contesté » ; l. 196 : faux trilemme « apport initial de A et accord large » ; l. 200 : E2a « né de la critique d'A » | § 1.2 : faux trilemme = accord n° 3 (B-T1 Ordre 5 ; C-T1 Duel 3 ; D-T1 § 4) ; E2a = famille 2 (A-T2 sur B a6) ; risque de A repris par C-T2 sur A (a1) ; risque de D : D-T1 table N12, 4e ligne (« ni l'absence d'effets indirects, ni la correction du bac à sable, ni l'impossibilité de déplacer le problème ») ; triple partage de D repris (A-T3 E4′ ; B-T3 E2b) | **Confirmé** | R07, R17, R40, R41, R42 ; onze : A 2, B 4, C 2, D 3 |
| **RN-03** cessions, divergences résolues | l. 35 : « **39** cessions » ; l. 174 : « A sur lui-même (E3″ : ≥ 3 graines) » ; l. 131 : « D l'avait : « plancher ou plafond… » » ; l. 36 : « **6** » divergences résolues | « A sur lui-même » : A-T2 note transversale → A-T3 E3″, même espèce : pas une cession. « D l'avait » : D-T3 § 1 (« Acceptée ») est une cession ; D-T1 n'a qu'un pilote de bruit. Règle de sélection § 1.3 | **Confirmé** pour « A sur lui-même » et pour le chevauchement non déclaré ; **infirmé** pour « D l'avait » (D cède bien) ; **38** cessions, **4** divergences résolues | R04, R05, R28, R29, R36 |
| **RN-04** objection de B sur (c3) | l. 114 : « B y vient de fait » ; l. 116 : « contrefactuel traité par les quatre (… B « circulaire » …) » ; absente des divergences et des apports | B-T1 « Ce que N13 gagnerait à distinguer » 2 : « séduisante mais circulaire … le motif Avalon n'est pas du sabotage diffus au sens du programme (un seul point de décision, pas de dommage accumulé). On risque de mesurer une omission simple … et de conclure que nos sondes « fonctionnent » sur un cas plus facile que la cible » ; S8 ; « Points de désaccord anticipés » 1. T3 : maintenue, B-T3 III « établi » 2 (« Le motif Avalon n'est pas du sabotage diffus … « Naturel » ne signifie pas « valide écologiquement » »). Pièce 4 § 3.2, l. 496–497 : « Diffuse : en partie », « Menace : non établie » ; § 3.6, l. 522 : « Cas d'étude utilisable ? Non en l'état ». A-T1 A6 et C-T1 (a) 5 partagent la lecture de la pièce sans en tirer la conséquence sur (c3) ; personne ne la critique en T2 | **Confirmé** ; rétablie comme **apport seul n° 13** (B seul la tire sur (c3) ; non reprise, non réfutée, maintenue en T3), non comme divergence (en T3 les quatre tiennent (c3) comme sous-produit : pas d'options différentes) | R20, R23, R24, R42 |
| **RN-05** « N-045 ne couvre pas la génération d'instruments neufs » | l. 65 : « *composition/sélection apprise* (couvert) contre *génération d'instruments neufs* et *vérification formelle* (non couvert) » ; critère 5 appliqué à A seul (l. 67) ; B et C recodées « couverture partielle » | Pièce 1 : énoncé 1, l. 72–73 (« instrument local entraîné par le noyau (sonde, adaptateur) »), l. 74 (« la règle d'agrégation ») ; énoncé 5, l. 103 (« sondes et adaptateurs entraînés à t, utiles à t+1 ») ; énoncé 6 (ii), l. 109–110 (« l'organisme entraîne lui-même … un adaptateur »). Cellules : le non-couvert est plus étroit — A-T1 A2 (« moniteurs neufs à la demande », « code des échanges ») ; B-T1 S1 (« réécrire un moniteur, … règle d'agrégation par du code exécuté » ; « N-045 apprend la sélection parmi des pièces existantes ») ; C-T1 (a) 1 (« synthèse de code ou d'opérateurs … hors du catalogue ») ; D-T1 table (« synthèse de code nouveau, … preuve Lean »). B omet les instruments entraînés et contredit l'énoncé 1 sur la règle d'agrégation (à la limite, comme A) ; B-T2 sur C (Duel 1) le corrige lui-même (« N-045 apprend déjà l'agrégation, VÉRIFIÉ ») ; C cite l'énoncé 6 (ii) (Duel 1 H_A) et D les instruments locaux (table N12) : exacts. Réponses littérales : B « non » (S1 HYPOTHÈSE ; Verdict), C « non » pour la couche 3 ((a) 1), « couvre l'adaptation structurelle sûre » ((d) 1) | **Confirmé** | R08, R11, R12, R43, R44 |
| **RN-06** fait saillant « (c1) est le témoin qui manque, (c3) son sous-produit, (c2) tombe par le dessin » | l. 109 (A seul cité pour « *le* bras ») ; l. 113 : « trois espèces conditionnent le rejet de (c2) au dessin » ; l. 114 ; l. 34 | « Témoin qui manque » : A-T1 A7 seul. Troisième bras : D-T1 E13-1 dès T1 (« Bras : non entraîné, récompense individuelle, récompense collective ») ; A-T3 E3″ (poids gelés) ; B-T3 A-4 (bras non entraîné) ; C-T3 C6 (témoin mono-agent). Pièce 4 : témoin manquant = run mono-agent à calcul égal (l. 421) ; cause concurrente = tout entraînement sans récompense du signalement (l. 427). (c2) « contingent » : A-T3 (c), B-T2 sur C a3, C-T3 C5 ; D ne le dit pas (D-T1 table N13 ; D-T3 § 3) — la v1 l'attribuait déjà à trois espèces | **Confirmé en partie** : la v1 attribuait bien la formule à A et le rejet contingent de (c2) à A, B, C ; elle ne disait pas que la forme à deux bras n'est tenue par personne en T3 ni que D avait le troisième bras dès T1 | R19, R23 |
| **RN-07** « cause collective non établie » chez C et D | l. 114 : « par les quatre » ; tables C et D (l. 109–110) sans renvoi à cette prémisse | C-T1 (a) 4 : « **HYPOTHÈSE** (non établie) pour la cause collective … aucun témoin d'entraînement mono-agent apparié … un seul run » ; D-T1 table N13, 2e ligne : « La récompense collective est la cause de cette érosion. **HYPOTHÈSE**. Avalon ne fournit pas de run d'entraînement mono-agent apparié ; un entraînement générique sans récompense du signalement reste une explication concurrente » | **Infirmé** : la prémisse est tenue par les quatre en T1 (A A7, B S6, C (a) 4, D table N13) ; ce n'était pas une inférence du lecteur, mais la v1 ne donnait pas les renvois ; le double compte (RN-01) reste | R21, R22, R23 (renvois ajoutés) |
| **RN-08** « seule pièce sans dépense » | l. 236 : « **Sans dépense de carte** ; appels de sous-agents non chiffrés par A, B, D » ; l. 177 : « le post-hoc fait jeu égal ou mieux hors domaine (pièce 5, l. 725) » ; l. 241 : « sur paires déjà produites … **Sans dépense** : la seule pièce de ce type » | (i) Critère 13 : « sans dépense » (processeur, lecture, PDF versé) / « avec dépense » (carte, appel payant) ; D-T1 § 4 chiffre la phase « contrôles mécaniques, mutations et premiers tests Lean » : « CPU seul … environ 50–500 € » ; A, B : heures d'agent non chiffrées ; C : « quelques dollars d'appels ». Aucune cellule ne dit qui appelle ni si l'appel est payant. (ii) Pièce 5, Table 1, moyennes hors domaine (l. 690–696) : RLCR AUROC 0,68, Brier 0,21, ECE 0,21 contre classifieur BCE 0,58 / 0,27 / 0,24 et classifieur Brier 0,60 / 0,32 / 0,33 ; l. 725 : SimpleQA et GSM8K seulement. C-T1 (d) 2 et C-T3 § 2.3 disent « sur plusieurs jeux hors domaine » ; B-T2 sur D E13-4 « sur certains jeux » : aucune espèce ne porte la formule générale ; elle est du lecteur de la v1. (iii) Pièce 5, l. 667 : le classifieur post-hoc est initialisé depuis Qwen2.5-7B et entraîné ; l. 832 : « Le papier ne fournit aucune méthode de recalibration sans entraînement ». C-T1 Duel 4 H_A (« Platt / isotonique ou classifieur léger ») s'appuie sur le « fondement factuel » de la Table 1 ; (d) 2 : « la simple recalibration post-hoc des log-probabilités (qui fait jeu égal ou mieux … dans le papier même de Damani) » : C présente Platt comme appuyé par Damani ; B-T3 III fonde « Platt d'abord » sur le coût (« quelques minutes de processeur ») ; D ne l'affirme pas. (iv) A-T1 (d) : « coût marginal nul **hors extraction des confiances** » ; A-T1 E5 : « extraction par phrase ajoutée » ; C-T3 § 4 : « extraire … les log-probabilités » : aucune cellule n'établit que les confiances sont journalisées | **Confirmé** pour (i) (catégorie hors critère ; statut des appels **non tranchable** sur les cellules ; D chiffrait), (ii) (formulation du lecteur, inexacte sur les moyennes), (iii) (C à la limite, critère 8 ; B et D non) et (iv) (non établi) | R08, R31, R37, R45, R46, R48, R50 |
| **RN-09** divergence n° 1 et N-053 | l. 249 : « C-T2 (a1) … viole N-053 … A-T3 : troisième voie … « HYPOTHÈSE de lecture à faire confirmer par Lazar » » ; aucune pièce nommée ; l. 135 : « Le bras « récompense du signalement » de B (T1) n'est pas un score de moniteur » | Pièce 2, l. 171–173 (N-053 point 5 : « aucun score de moniteur ni de juge n'entre dans un signal d'entraînement ou de sélection de l'agent ») ; N-053 v1, l. 42–44 : « hors bras d'attaque déclaré ; il vaut aussi pour la piste « organisme » (N-045) ». A-T3 E1′ : sorties « branchées sur l'étage de filtrage des fiches seulement » ; « la composition elle-même reste sélectionnée sur oracle et coût seuls » ; rien sur l'entrée des fiches filtrées dans un entraînement (N-045, énoncés 4 et 6 (ii)). B-T1 N13-E1 : « une petite récompense pour le signalement ajoutée à la récompense collective » ; mécanisme de détection non précisé ; la seule détection que B définit est mécanique (B-T1 (c) : « l'outil de signalement a-t-il été appelé dans le délai ? ») | **Confirmé** (pièce nommée) ; **non tranchable** sur A-T3 (le texte ne dit pas si les fiches filtrées entrent dans un entraînement) ; mécanisme de B : appel d'outil, par inférence du lecteur (signalée) | R30, R51 |
| **RN-10** effet d'ordre sur N12 (3) | l. 99 : « la question offre elle-même cette option … et la pré-collision la porte (vrai par construction) : **réserve « effet d'ordre »** » | Sous la règle § 1.1 (critère 3), la position n'est pas comptée en accord ; la réserve tombe avec l'accord ; la non-indépendance à l'égard de la pré-collision est notée (reprises B, C) | **Pris acte** ; la réserve tombe avec l'accord | R18, R56 |
| **RN-11** divergences 4, 5, 6, 7 ; codes « Q2, N4 » ; « jamais » | l. 252–255 ; l. 37 « vérificateur externe / jamais » | Raisons : A-T1 (c) (précaution « puisque A7 ») ; B-T1 point 1 ; D-T1 E13-2 et § 4 ; C-T3 C7. Couche 4 : A-T3 E2′ ; C-T3 Duel 2 corrigé (« Lean 4 est adopté pour les seuls lemmes critiques de Q2 et N4 ») ; D-T1 « Réponse courte » (« sans imposer une couche 4 autonome ») ; B-T1 Ordre 6. « Q2 », « N4 » : codes de la pré-collision (pièce 3 : Q2 § 1 (c) et § 2, l. 215, 253 ; N4 § 5, l. 307 « Une impossibilité : la défense universelle … » ; C-T1 Duel 2 : « bornes théoriques du programme (Q2, N4, règles de score) ») — pas le nœud N4 de la v12. Première expérience : A-T3 « L'expérience à faire en premier » ; B-T3 III ; C-T3 § 4 ; D-T3 § 3. Invariant : C-T3 C2 renvoie à « Question N12 » et à Avalon p. 76 ; aucune pièce des faits ne le porte ; la question (§ N12 Contexte) définit la couche 3 « sous bac à sable ». « Jamais » : aucune cellule ne l'emploie pour la couche 4 (D : « vérificateur externe … sans imposer une couche 4 autonome ») | **Confirmé** | R06, R52, R53, R54, R55 |
| **RN-12** pièce du lecteur et classements | l. 240 : « je le note pour la veille » ; l. 129 : « La plus complète » ; l. 225 : « c'est la plus prudente » | Critère 17 ; aucune espèce ne propose la lecture d'Agrawal comme pièce (citée comme fait d'Avalon par A, B, C) ; « la plus prudente » est un jugement de A-T2 sur D (en-tête), repris par le lecteur | **Confirmé** | R27, R47, R49, R59 |
| **RN-13** « 4 reprises » ; « bornes » | l. 41 : « **4** reprises » ; l. 69 : liste de ce qui est gelé, sans les bornes | Reprises de la conclusion : B-T1 S4 et « Synthèse transversale » ; C-T1 (d) 1 (« rester fermée pour les douze mois »). Critiques du fondement : A-T1 A5 (« l'empreinte scelle un texte, pas la validité ») ; D-T1 table N12 (« ne constitue pas une preuve de faible valeur ») ; C-T1 (a) 2 critique aussi « on scelle par empreinte ». « Bornes » : aucune cellule ne nomme les bornes parmi ce qui est gelé ; « borne » n'y apparaît qu'au sens mathématique (B-T1 N12-E2 ; C-T1 Duel 2 ; C-T2 sur D) — grep sur les douze cellules | **Confirmé** | R09, R13 |
| **RN-14** paramètres de conception (sécurité) | l. 79–80 (C : « Python restreint à arbre syntaxique filtré, même harnais isolé » ; D : « générateur informé dès le départ de la grammaire du catalogue ») ; l. 107–110 (dessins de E3/E3″, N13-E1, Duel 3, E13-1 : affinage, modèle, graines, plan factoriel, attribution r_i / Σ r_i, quantile) ; l. 117–118 (forme de la récompense collective ; canal ; règle d'escalade) ; l. 183 (famille 10 : « somme ou moyenne ») ; l. 194 (plan 2 × 4 de E3′) | Classe (a) : entraînement de l'organisme sous récompense collective ; classe (b) : génération de code par l'organisme dans la couche 3 | **Confirmé** ; les cinq passages sont remplacés par des renvois (fichier, section) ; **un passage de plus** remplacé : l. 81 (garde de C : somme de contrôle, filtre d'appels système, m = 50 tentatives) ; les autres passages examinés sont listés en § 4 | R14, R15, R16, R19, R20, R21, R22, R25, R26, R38, R39 |
| **RN-15, RN-16, RN-17** | — | — | **Pris acte** ; aucune correction | — |

## 3. Points 1 à 13 « qui exigent les cellules »

| Point | Réponse sur les cellules (renvoi) |
|---|---|
| 1 B sur (c3) | T1 : « séduisante mais circulaire », motif non diffus, risque de valider les sondes sur un cas plus facile (B-T1 « Ce que N13 gagnerait à distinguer » 2 ; S8 ; « Points de désaccord » 1) ; T3 : maintenue (B-T3 III « établi » 2). Rétablie en apport seul n° 13 (RN-04). |
| 2 prémisse chez C et D | C-T1 (a) 4 ; D-T1 table N13, 2e ligne : tenue explicitement (RN-07 infirmé). |
| 3 accord n° 7 | A-T1 A12 (ii) et C-T1 (a) 6 citent N-045 énoncé 8 ; D-T1 § 4 « n'entraîner aucun modèle de frontière » sans citer l'énoncé ; B conçoit N13-E3 sur 7–8 milliards sans l'énoncer. Composition A, C, D (B par construction) ; raison = décision servie → non compté (§ 1.1). |
| 4 réponse littérale de B et C à N12 (1) | B : « non » (S1 : couverture = HYPOTHÈSE ; « N-045 apprend la sélection, pas la génération ») ; S1 cite l'énoncé 1 (modèle par rôle, ordre, agrégation, budget) mais omet « instrument local entraîné par le noyau » et les énoncés 5, 6 (ii) ; B-T2 sur C (Duel 1) reconnaît que l'agrégation est apprise. C : « non » pour la couche 3 ((a) 1), en citant l'énoncé 1 avec « LOCAL:<identifiant> » et l'énoncé 6 (ii) (Duel 1 H_A : « adaptateur interne entraîné par l'instrument (B) ») ; (d) 1 : « N-045 couvre l'adaptation structurelle sûre ». |
| 5 fiches filtrées → entraînement (A-T3 E1′) | Non dit : E1′ branche les moniteurs sur « l'étage de filtrage des fiches seulement » et garde la composition « sélectionnée sur oracle et coût seuls » ; rien sur un affinage nourri par ces fiches. **Non tranchable** sur la cellule. |
| 6 détection du signalement dans le bras de B | Non précisée pour le terme de récompense (B-T1 N13-E1) ; la seule détection définie par B est mécanique (B-T1 (c) : appel de l'outil dans le délai). Inférence du lecteur, signalée dans la v2. |
| 7 règle des divergences résolues ; 39 cessions | § 1.3 : 38 cessions (« A sur lui-même » retiré ; « D l'avait » infirmé, D-T3 § 1 cède) ; 4 divergences résolues. |
| 8 dépense des appels de sous-agents (couche 4) | A : « heures d'agent et de scelleur tiers », non chiffré ; B : « quelques jours de travail d'agent », non chiffré ; C : « 0 $ en calcul GPU, quelques dollars d'appels » ; D : « CPU seul … environ 50–500 € » (D-T1 § 4). Qui appelle et à quel prix : **non tranchable** sur les cellules. |
| 9 Platt établie par Damani ? confiances journalisées ? | C : à la limite (Duel 4 « fondement factuel » ; (d) 2) ; B : argument de coût ; D : non. Journalisation : aucune cellule ne l'établit ; A-T1 (d) « hors extraction des confiances » ; C-T3 § 4 « extraire ». |
| 10 codes « Q2, N4 » | Codes de la pré-collision (pièce 3) : Q2 théorie du juge (§ 1 (c), § 2), N4 borne d'impossibilité (§ 5) ; C-T1 Duel 2 et instrument 3 (« lemmes du programme (Q2, Q4, N4) ») ; C-T3 Duel 2 corrigé. Pas le nœud N4 de la v12. |
| 11 « bornes » | Aucune espèce ne les nomme parmi ce qui est gelé (grep ; sens mathématique seulement). |
| 12 liens 1, 3, 6 | Aucun n'est un accord (§ 1.1). |
| 13 heure de début de lecture | Hors de ma portée (journal de session-depot) ; mes propres heures : 09:38:26 (début), 09:50:42 (fin de lecture). |

## 4. RN-14 : passages examinés

- **Remplacés par des renvois** (annexe) : l. 79 (C, couche 3 ; R14) et l. 79 garde (R15) ; l. 80 (D ; R16) ; l. 107 (A ; R19) ; l. 108 (B ; R20) ; l. 109 (C ; R21) ; l. 110 (D ; R22) ; l. 117 (R25) ; l. 118 (R26) ; l. 183 (R38) ; l. 194 (R39). Les positions, raisons, pires cas et pièces restent ; seuls les mécanismes (forme de l'attribution du crédit, algorithme et modèle d'entraînement, plan factoriel et effectifs, génération et isolation du code) deviennent des renvois (fichier, section).
- **Examinés et gardés** (ni classe (a) ni classe (b), ou exigés par les critères) : l. 42 (classes hors niveau, sans recette) ; l. 60 (citation de N-045) ; l. 77 (A : filtre de fiches — point de gouvernance N-053, objet de la divergence n° 1) ; l. 78 (B : critère de détection, comparateurs statistiques, sans mécanisme de génération) ; l. 115 (critère 10 : mesure du signalement, exigée) ; l. 126–129 (précautions : mesure, seuil, qui lit — exigées par le critère 11 ; paramètres de mesure, non d'entraînement) ; l. 133, 135 ; l. 143–146 (entraînement de calibration d'un juge local : classe distincte, non collective) ; l. 174–186 hors familles 10 (paramètres statistiques génériques) ; l. 235–239 (pièces : « deux bras, k ≥ 2–3 graines » — dessin générique que la question nomme elle-même). Aucun autre passage de la v1 ne reproduit un paramètre des classes (a) ou (b).

## 5. Décompte corrigé (v1 → v2)

| Catégorie | v1 | v2 |
|---|---|---|
| Accords indépendants | 7, dont 5 larges | **4**, tous larges (n° 1, 2, 3 à quatre ; n° 4 à trois) |
| Positions communes non comptées (vrai par construction) | — | 3 (N12 (3) ; N13 (1) (c2) ; N13 (3) juge local) + 1 sans raison commune (N13 (2) signalement hors récompense) |
| Cessions | 39 | **38** |
| Divergences résolues | 6 | **4** (+ 2 reclassées en convergences de méthode) |
| Divergences non résolues | 9 | 9 (étiquette « jamais » retirée) |
| Apports seuls | 11 (A 3, B 4, C 2, D 2) | **11** (A 2, B 4, C 2, D 3) : − faux trilemme, − N13-E2a, − risque N-053 de A ; + risque de D, + objection de B sur (c3) |
| Inexactitudes, à la limite | A 1 (+1) ; B 1 (+1 renvoi) ; C 0 (+1 renvoi) ; D 0 | A 1 (+1) ; B 1 (+1 renvoi, +1 à la limite) ; C 0 (+1 renvoi, +1 à la limite) ; D 0 |
| Reprises de la pré-collision | 4 | 2 reprises, 2 critiques |
| Pièces sans dépense | 1 (N13 (3)) | 1 ou 2, selon le statut des appels d'agents (non tranché) |

## 6. Ce que le lecteur n'a pas pu faire

- Trancher sur les cellules : le statut (sans / avec dépense) des appels de sous-agents pour le test de la couche 4 (point 8) ; si les fiches filtrées par les moniteurs neufs de A entrent dans un entraînement (point 5) ; le mécanisme exact du terme « récompense du signalement » de B (point 6, inférence signalée).
- Confronter l'heure de début de lecture du lecteur de la v1 au journal de session-depot (point 13).
- Tenir la v2 sous la borne de longueur sans resserrer fortement les corrections : les textes de la v2 sont compacts et renvoient à cet erratum pour le détail (règles, raisons des accords, raisons des divergences) ; la v2 a été réécrite quatre fois pour respecter « ≤ v1 + 800 mots ».
- Vérifier quoi que ce soit sur les PDF (non ouverts) : tout chiffre d'Avalon ou de Damani est recoupé sur les pièces 4 et 5 (ligne), jamais sur le PDF.

## 7. Longueurs, code de retour et empreintes (calculés par script à l'assemblage, Sun Nov  1 10:24:45 UTC 2026)

- Script : `appliquer-erratum-n12-n13-v1.py` (scratchpad de la session), 59 remplacements, chaque chaîne originale trouvée exactement une fois dans la v1 ; **code de retour : 0**. Remplacements resserrés en six passes pour tenir la borne de longueur.
- Longueur : v1 11441 mots (`wc -w`) / 12247 (découpage Python) ; v2 12163 / 13038 ; borne v1 + 800 = 12241 / 13047 : respectée (v2 = v1 + 722 mots `wc`).
- Empreintes : `synthese-n12-n13-v1.md` `b1d28f0d43245c3534d469f38e77bf4e14da2a70f39f4f1bd76a0b42c96b8cb4` ; `synthese-n12-n13-v2.md` `f0340581766c5fb4d97a0ccb06f0cf1738a15228385b332ee602e93a0be28f0a` ; cet erratum : empreinte calculée par session-depot au scellement.

## Annexe — remplacements exacts appliqués à la v1 (original cité, puis remplacement)

Source : `synthese-n12-n13-v1.md`, SHA-256 `b1d28f0d43245c3534d469f38e77bf4e14da2a70f39f4f1bd76a0b42c96b8cb4` ; 59 remplacements, chacun trouvé exactement une fois ; appliqués le 2026-11-01 10:23:17 UTC par `appliquer-erratum-n12-n13-v1.py`.

### R01 — E00 — titre (l. 1)

**Original (v1) :**

```text
# Synthèse de lecture — collisionneur séparé N12 et N13 (couches 3 et 4 de l'organisme ; récompense collective), tour unique (E3-T1, E3-T2, E3-T3) — v1
```

**Remplacement (v2) :**

```text
# Synthèse de lecture — collisionneur séparé N12 et N13 (couches 3 et 4 de l'organisme ; récompense collective), tour unique (E3-T1, E3-T2, E3-T3) — v2

**Note de version (v2, 1er novembre 2026, 10:23 UTC).** V1 (`b1d28f0d…`) intégrale plus les remplacements de l'erratum `erratum-synthese-n12-n13-v1.md` (script ; chaque chaîne originale trouvée exactement une fois), (motif : relecture d'Opus 5.5, consigne scellée). Lecteur : sous-agent neuf, **Claude Fable 5.1** (modèle de l'espèce A et du lecteur de la v1), lecture achevée à 09:50:42 UTC. Décompte réécrit sous règle ; objection de B sur (c3) rétablie ; paramètres de conception remplacés par des renvois (RN-14) ; classements retirés. Empreintes de la v1 conservées ; la v1 reste (R12).
```

### R02 — E01 — empreintes complétées (l. 25)

**Original (v1) :**

```text
    - `E3-T3-reponse-D.md` : `61cad26929d813c5061ed7e1396fb570902eea3428477664303e64e98e0161e9`.
```

**Remplacement (v2) :**

```text
    - `E3-T3-reponse-D.md` : `61cad26929d813c5061ed7e1396fb570902eea3428477664303e64e98e0161e9`.
- **Empreintes ajoutées en v2** (`sha256sum`, 1er novembre 2026, 09:39 UTC) : `synthese-n12-n13-v1.md` : `b1d28f0d43245c3534d469f38e77bf4e14da2a70f39f4f1bd76a0b42c96b8cb4` ; `relecture-opus-synthese-n12-n13-v1.md` : `c05949af2b93f6af4facec06009a89da9b05b033b1e401edfc1de6fcba51d2a7` ; `consigne-erratum-synthese-n12-n13-v1.md` : `84a5d48f9d3eaf7d7f12c0072f80c204e1271048057d1d596a74c9ba60ea903e` ; `docs/decisions/decision-N-053-v1.md` : `2204256d744288be2708578c0fdc8c44c62a29b70b2727ed7e31ec142d1cdeae` ; `erratum-synthese-n12-n13-v1.md` : empreinte calculée par session-depot au scellement.
```

### R03 — E02 — décompte, accords (l. 34)

**Original (v1) :**

```text
| Accords indépendants (T1, même position, raison commune, ≥ 2 espèces) | **7**, dont **5 larges** (3 ou 4 espèces) | N12 (1) couverture partielle de N-045 [4, large] ; N12 (2) couche 4 : l'empreinte ne prouve pas la validité [4, large] ; N12 (3) étape 2 d'abord [4, large] ; N13 (1) (c2) écartée [4, large, mais vrai par construction pour la raison] ; N13 (1) (c3) n'est recevable qu'avec le contrefactuel de (c1) [3 en T1 : A, C, D ; B rejoint en T3] ; N13 (1) cause collective non établie comme prémisse commune [4, large] ; N13 (3) l'entraînement RLCR ne concerne qu'un juge local, jamais la frontière [A, C, D]. |
```

**Remplacement (v2) :**

```text
| Accords indépendants (règle écrite, § « Règle de comptage ») | **4**, tous larges (3 à quatre espèces, 1 à trois) | n° 1 N12 (1) ligne de partage couvert / non couvert [A, B, C, D] ; n° 2 N12 (2) couche 4, l'empreinte ne prouve pas la validité [A, B, C, D] ; n° 3 N13 (1) (c1) seule forme à contrefactuel, (c3) sous-produit [A, B, C, D, B dès T1] ; n° 4 N13 (3) Damani = chantier de mesure, entraînement à prouver [A, C, D] (raisons : sections et erratum). **Non comptés** (vrai par construction) : N12 (3) étape 2 d'abord [4 ; critère 3] ; N13 (1) (c2) écartée [4 ; raison de la question] ; N13 (3) RLCR pour un juge local seulement [A, C, D ; N-045 énoncé 8]. |
```

### R04 — E03 — décompte, cessions (l. 35)

**Original (v1) :**

```text
| **39** cessions individuelles (une espèce, un point), regroupées en **13 familles** |
```

**Remplacement (v2) :**

```text
| **38** cessions individuelles (une espèce cède à une autre, un point ; « A sur lui-même » retiré de la famille 1), regroupées en **13 familles** |
```

### R05 — E04 — décompte, divergences résolues (l. 36)

**Original (v1) :**

```text
| Divergences résolues en T3 (cession avec raison) | **6** | B : premier test = recalibration post-hoc et non entraînement RLCR ; C : (c2) écartée « par incompatibilité de protocole » et non « par inférence logique » ; C : témoins d'intégrité retirés de la récompense d'héritage ; D : appariement sur la performance supprimé ; A : E4 reposée sans contrat ; B : bras « récompense du signalement » reclassé en intervention. |
```

**Remplacement (v2) :**

```text
| Divergences résolues en T3 (règle : § Règle de comptage ; comptées aussi parmi les cessions) | **4** | B : premier test = recalibration post-hoc et non entraînement RLCR (N13 (3)) ; C : (c2) écartée « par incompatibilité de protocole » et non « par inférence logique » (N13 (1)) ; C : témoins d'intégrité retirés de la récompense d'héritage (N13 (2)) ; B : bras « récompense du signalement » reclassé en intervention (N13 (2)). Reclassées en convergences de méthode : D (appariement supprimé) ; A (E4 sans contrat). |
```

### R06 — E05 — décompte, divergences non résolues (l. 37)

**Original (v1) :**

```text
ouverture de la couche 4 (classe d'erreurs / vérificateur externe / jamais)
```

**Remplacement (v2) :**

```text
ouverture de la couche 4 (classe d'erreurs / lemmes critiques / vérificateur externe d'abord / au coût d'opportunité nul)
```

### R07 — E06 — décompte, apports seuls (l. 38)

**Original (v1) :**

```text
| Apports seuls (une source, non réfutés en T2) | **11** | § « Apports seuls ». |
```

**Remplacement (v2) :**

```text
| Apports seuls (une source, jamais repris, non réfutés en T2) | **11** (A 2, B 4, C 2, D 3) | § « Apports seuls » (trois retirés, deux ajoutés). |
```

### R08 — E07 — décompte, inexactitudes (l. 39)

**Original (v1) :**

```text
**A : 1 (+ 1 à la limite) ; B : 1 (+ 1 renvoi de section) ; C : 0 chiffre (+ 1 renvoi de section répété) ; D : 0**
```

**Remplacement (v2) :**

```text
**A : 1 (+ 1 à la limite) ; B : 1 (+ 1 renvoi de section, + 1 à la limite, critère 5) ; C : 0 chiffre (+ 1 renvoi de section répété, + 1 à la limite, critère 8) ; D : 0**
```

### R09 — E08 — décompte, reprises de la pré-collision (l. 41)

**Original (v1) :**

```text
**4** reprises de la position de la pré-collision « pas en douze mois » (vrai par construction, non comptées en accord)
```

**Remplacement (v2) :**

```text
**2** reprises de « pas en douze mois » (B-T1 S4 ; C-T1 (d) 1) et **2** critiques de son fondement (A-T1 A5 ; D-T1 table N12) (vrai par construction, non comptées)
```

### R10 — E09 — règle de comptage insérée (avant l. 47)

**Original (v1) :**

```text
## Vrai par construction (jamais compté en accord)
```

**Remplacement (v2) :**

```text
## Règle de comptage (v2 ; critères 7 à 13 du tour 1, 3 et 12 de N12-N13 ; détail : erratum, § 1)

**Accord** : même position en T1 sur la même sous-question, au moins deux espèces, une raison commune non vraie par construction (exclus : vrai par construction, raison comptée à part, espèce rejoignant en T3, lien N12-N13). **Cession** : adoption en T2 ou T3 de ce qu'une *autre* espèce a porté. **Divergence résolue** : cession changeant une position de sous-question. **Apport seul** : une espèce en T1, jamais repris, non réfuté en T2.

## Vrai par construction (jamais compté en accord)
```

### R11 — E10 — N12 (1), lecture (l. 65)

**Original (v1) :**

```text
**Lecture.** Accord large à quatre sur la même ligne de partage — *composition/sélection apprise* (couvert) contre *génération d'instruments neufs* et *vérification formelle* (non couvert) — avec un vocabulaire presque identique
```

**Remplacement (v2) :**

```text
**Lecture.** Accord large à quatre (n° 1) sur la même ligne de partage — *composition et sélection apprises, instruments locaux entraînés* (couvert : pièce 1, énoncés 1, 5, 6 (ii)) contre *code hors catalogue* et *vérification formelle* (non couvert) — « en partie » (A, D), « non » (B, C), recodées en v1 sans le dire, avec un vocabulaire presque identique
```

### R12 — E11 — N12 (1), critère 5 symétrique (l. 67)

**Original (v1) :**

```text
« code » et « forme » ne sont pas synonymes, je le note sans trancher. Aucune espèce n'attribue à N-058
```

**Remplacement (v2) :**

```text
« code » et « forme » ne sont pas synonymes, je le note sans trancher. **Même règle pour B** : S1 à la limite (§ Inexactitudes) ; C et D exacts. Aucune espèce n'attribue à N-058
```

### R13 — E12 — N12 (1), critère 6, bornes (l. 69)

**Original (v1) :**

```text
C-17 : les quatre disent qu'il n'est pas servi
```

**Remplacement (v2) :**

```text
Aucune espèce ne nomme les « bornes » que la question gèle avec le noyau et les gardes. C-17 : les quatre disent qu'il n'est pas servi
```

### R14 — E13 — N12 (2), ligne C, couche 3 (l. 79, RN-14 b)

**Original (v1) :**

```text
| **C** | Synthèse d'opérateurs de détection hors catalogue ; T3 : « fonctions de caractéristique nouvelles sur les traces », Python restreint à arbre syntaxique filtré, même harnais isolé pour les deux bras (C-T3 C2, Duel 1 corrigé). |
```

**Remplacement (v2) :**

```text
| **C** | Synthèse d'opérateurs de détection hors catalogue (C-T1 (a) 1) ; T3 : fonctions de caractéristique nouvelles sur les traces ; mécanisme : renvoi `E3-T3-reponse-C.md`, § (a) C2, § (b) Duel 1 corrigé. |
```

### R15 — E14 — N12 (2), ligne C, garde (l. 79, RN-14 b)

**Original (v1) :**

```text
| Somme de contrôle calculée hors du bac à sable, filtre d'appels système (C-T1 (c) 2) ; T3 : pré-test d'étanchéité par m = 50 tentatives plantées (illustratif), éliminatoire, séparé du duel (C-T3 C1). |
```

**Remplacement (v2) :**

```text
| Vérification d'étanchéité tenue hors du bac à sable (pièce 4, l. 548) ; T3 : pré-test éliminatoire séparé du duel ; mécanisme : renvoi `E3-T1-conception-C.md`, § (c) instrument 2 ; `E3-T3-reponse-C.md`, § (a) C1. |
```

### R16 — E15 — N12 (2), ligne D, couche 3 (l. 80, RN-14 b)

**Original (v1) :**

```text
| **D** | Fabrication de moniteurs pour des menaces plantées « non représentées dans le catalogue » (D-T1 § 3 table) ; T3 : bras « générateur informé dès le départ de la grammaire du catalogue » comme comparateur, coût compté une fois (D-T3 § 1, § 2 E12-1). |
```

**Remplacement (v2) :**

```text
| **D** | Fabrication de moniteurs pour des menaces plantées « non représentées dans le catalogue » (D-T1 § 3 table) ; T3 : comparateur « contraint au catalogue » précisé, coût compté une fois ; mécanisme : renvoi `E3-T3-reponse-D.md`, § 1 et § 2 E12-1. |
```

### R17 — E16 — N12 (2), risques de la couche 3 (l. 84)

**Original (v1) :**

```text
Chacun est un **apport seul**, non réfuté en T2. Le risque de C est le seul adossé à un fait servi (pièce 4, l. 548, l. 550) ; celui de A est le seul adossé à une décision servie (pièce 2, l. 171–173).
```

**Remplacement (v2) :**

```text
Ceux de B, C et D sont des **apports seuls**, non réfutés en T2 (C contesté par B-T2 c3, maintenu) ; celui de A, repris par C-T2 sur A (a1), est la prémisse de la divergence n° 1. Le risque de C est le seul adossé à un fait servi (pièce 4, l. 548, l. 550) ; celui de A, à une décision servie (pièce 2, l. 171–173).
```

### R18 — E17 — N12 (3), lecture (l. 99)

**Original (v1) :**

```text
**Lecture.** Accord large à quatre : étape 2 d'abord ; la couche 4 se teste à part, sur processeur, sans ouvrir de couche. **Réserve R4** : accord à quatre ; de plus, la question offre elle-même cette option (« d'abord réaliser l'étape 2 ») et la pré-collision la porte (vrai par construction) : **réserve « effet d'ordre »** au sens du critère 12. Les raisons diffèrent, ce qui atténue la réserve : dépendance logique (A), coût et calendrier (B), ordre des dépenses de N-045 (C), nécessité d'un résidu mesurable (D).
```

**Remplacement (v2) :**

```text
**Lecture.** Position commune à quatre : étape 2 d'abord ; la couche 4 se teste à part, sur processeur. **Non comptée en accord** : position de la pré-collision citée par la question (critère 3) ; la réserve « effet d'ordre » tombe avec l'accord. Raisons en partie communes : l'expérience décisive exige l'étape 2 (A-T1 A4 ; B-T1), N-045 § 4 (B, C), résidu mesurable (D).
```

### R19 — E18 — N13 (1), ligne A (l. 107, RN-14 a)

**Original (v1) :**

```text
| **A** | **(c1) et (c3) ne sont pas exclusives** : le bras collectif de (c1) *est* le générateur de (c3), le bras individuel son contrefactuel ; « faux trilemme » (A-T1 A10). (c2) non traitée en T1 autrement que par la question. Traduction de « collectif / individuel » pour notre organisme, qui « n'apprend pas par gradient » (pièce 4, l. 542) : **niveau d'attribution du crédit** — score d'ensemble rendu à toutes les parties contre score par bras sur oracle (A-T1 A11) ; forme : E3, voie hors ligne d'abord (affinage sur réponses filtrées, N-045 § 4), modèle ouvert 7–8 milliards servi `LOCAL:`, récompense tirée de l'oracle seul (A-T1 E3). | « (c1) et (c3) ne s'excluent pas… (c2) est exclue par le dessin actuel de la course 2 (pas d'oracle), ce qui est contingent, pas logique » (A-T3 (c) N13 (1)). E3″ avec unité « trajectoire d'une partie », quantile d'acceptation apparié, ≥ 3 graines, bras poids gelés, règle d'escalade vers le renforcement en ligne (A-T3 E3″). | La cause collective n'est pas établie : pas de témoin mono-agent apparié (pièce 4, l. 421, l. 427), un seul run (l. 429), 20 % de déroulés mono-agents (l. 375) ; (c1) « est exactement le témoin qui manque à Avalon : ce n'est pas un bras de plus, c'est *le* bras » (A-T1 A7). | Pire cas : la voie hors ligne manque de pression et l'absence d'écart n'est pas informative (B-T2 sur A) ; garde : critère d'informativité (score oracle de tâche a bougé dans les deux bras) et règle d'escalade gelée (A-T3 E3 B-a). | E3″ : **avec dépense** (dizaines d'heures de carte par bras, illustratif) ; préalable E3′′ à N = 1 (p₀) : inférence, **dépense faible**. |
```

**Remplacement (v2) :**

```text
| **A** | **(c1) et (c3) ne sont pas exclusives** : le bras collectif de (c1) *est* le générateur de (c3), le bras individuel son contrefactuel ; « faux trilemme » (A-T1 A10) ; (c2) non traitée autrement que par la question ; « collectif / individuel » traduit en niveau d'attribution du crédit (A11) ; dessin de E3 : renvoi `E3-T1-conception-A.md`, § (b) E3. | Inchangée ; (c2) exclue par le dessin actuel de la course 2, « contingent, pas logique » (A-T3 (c)) ; E3″ corrigée (renvoi : `E3-T3-reponse-A.md`, § (b) E3″). | La cause collective n'est pas établie (pièce 4, l. 375, 421, 427, 429) ; (c1) « est exactement le témoin qui manque à Avalon » (A-T1 A7 ; formule de A seul). | Pire cas : voie hors ligne sans pression, absence d'écart non informative (B-T2 sur A) ; garde : critère d'informativité, règle d'escalade gelée (A-T3). | E3″ : **avec dépense** (illustratif) ; préalable E3′′ à N = 1 (p₀) : inférence, **dépense faible**. |
```

### R20 — E19 — N13 (1), ligne B (l. 108, RN-14 a ; RN-04)

**Original (v1) :**

```text
| **B** | **(c1) seule fournit un contrefactuel propre** ; elle ne vaut que si la question causale est ouverte — et elle l'est (S6 HYPOTHÈSE) ; (c3) « séduisante mais circulaire » : le motif d'Avalon n'est pas du diffus (un point de décision, pas de dommage accumulé ; pièce 4, l. 496) ; (c2) « mal appariée… je la considère comme écartée » (B-T1 « Ce que N13 gagnerait à distinguer » 2–4). N13-E1 : renforcement en ligne, deux bras + bras « récompense du signalement » (B-T1 N13-E1). | (c1) via N13-E1 avec k ≥ 2 graines, bras non entraîné, canaris « à ne pas signaler », scénarios disjoints, récompenses appariées en variance, N identique (B-T3 II) ; (c3) conditionnelle à N13-E1 (B-T1 Ordre 5, maintenu B-T3 III). |
```

**Remplacement (v2) :**

```text
| **B** | **(c1) seule fournit un contrefactuel propre**, si la question causale est ouverte — elle l'est (S6 HYPOTHÈSE) ; (c3) « séduisante mais circulaire » : le motif d'Avalon n'est pas du diffus (pièce 4, l. 496) ; N13-E2 (c3) « conditionnelle à N13-E1 » dès T1 (« Ordre proposé » 5) ; (c2) « mal appariée… écartée » (B-T1 points 2–4). N13-E1 : deux bras plus un bras « récompense du signalement » (renvoi : `E3-T1-conception-B.md`, § N13-E1). | (c1) via N13-E1 corrigée (renvoi : `E3-T3-reponse-B.md`, § II) ; (c3) conditionnelle à N13-E1 (B-T3 III) ; objection « motif non diffus » maintenue (B-T3 III, « établi » 2). |
```

### R21 — E20 — N13 (1), ligne C (l. 109, RN-14 a ; RN-07)

**Original (v1) :**

```text
| **C** | **(c2) rejetée** « par inférence logique » ; **(c1) et (c3) fusionnées** en un « pré-pilote contrôlé à l'étape 2 », plan factoriel 2 × 2 (crédit individuel / collectif × K = 1 / K = 3), N = 4 agents (illustratif), modèle 8 milliards + adaptateur, affinage hors ligne (C-T1 Duel 3) ; « jamais comme signal d'entraînement unique de l'organisme » (C-T1 (d) 2). | (c2) écartée « par incompatibilité de protocole », non « par inférence logique » (C-T3 C5) ; attribution isolée à information et effectif constants : r_i contre moyenne des r_j, témoin mono-agent en 3e bras (C-T3 C6) ; aucun scénario de signalement pendant l'entraînement (C7) ; k = 3 graines, pré-test p₀ ∈ [0,40 ; 0,90], seuil unique 15 points (C8) ; « ne jamais utiliser la récompense collective plate comme signal d'entraînement de production » (C-T3 (c) 3). | Transposabilité du crédit plat aux petits effectifs = HYPOTHÈSE : « triangle inconfortable », lots de 200 à 800 groupes de K = 16 (pièce 4, l. 373, l. 375, l. 420) ; à 8 fusions par bras, « le bruit d'un avantage collectif plat domine » (C-T1 (a) 6). |
```

**Remplacement (v2) :**

```text
| **C** | **(c2) rejetée** « par inférence logique » ; **(c1) et (c3) fusionnées** en un « pré-pilote contrôlé à l'étape 2 » croisant le crédit et la garde d'héritage de N-045 § 5 (renvoi : `E3-T1-conception-C.md`, § (b) Duel 3) ; « jamais comme signal d'entraînement unique de l'organisme » (C-T1 (d) 2). | (c2) écartée « par incompatibilité de protocole », non « par inférence logique » (C-T3 C5) ; attribution à information et effectif constants, témoin mono-agent en 3e bras, aucun scénario de signalement pendant l'entraînement, graines, pré-test p₀, seuil unique (renvoi : `E3-T3-reponse-C.md`, § (a) C6 à C8, § (b) Duel 3 corrigé) ; « ne jamais utiliser la récompense collective plate comme signal d'entraînement de production » (C-T3 (c) 3). | La cause collective n'est pas établie (C-T1 (a) 4 ; pièce 4, § 1.7–1.8) ; transposabilité du crédit plat aux petits effectifs = HYPOTHÈSE (pièce 4, l. 373–375, 420 ; C-T1 (a) 6). |
```

### R22 — E21 — N13 (1), ligne D (l. 110, RN-14 a ; RN-07)

**Original (v1) :**

```text
E13-1 (effet spécifique) et E13-2 (utilité) séparées ; signalement « hors récompense », « contrainte de sécurité rapportée séparément, non une monnaie d'échange » (D-T1 E13-1, E13-2). | Même position ; monde planté « à contributions additivement attribuables » : r_i par agent, R = Σ r_i identique pour tous dans le bras collectif ; comparaison à pas d'entraînement et budget fixés d'avance, sans appariement sur la performance (D-T3 § 1, § 2 E13-1) ; plancher absolu de signalement gelé, dont le franchissement interdit l'intégration (D-T3 E13-2). | « Le canal d'apprentissage doit être fixé avant toute analogie causale » (Avalon entraîne des poids partagés par gradient ; notre organisme peut apprendre par règles de reconduction) (D-T1 table N13). |
```

**Remplacement (v2) :**

```text
E13-1 (effet spécifique, trois bras dont un non entraîné dès T1) et E13-2 (utilité) séparées ; signalement « hors récompense », « contrainte de sécurité rapportée séparément, non une monnaie d'échange » (D-T1 E13-1, E13-2). | Même position ; attribution du crédit et comparaison à pas et budget fixés d'avance, sans appariement sur la performance (forme : renvoi `E3-T3-reponse-D.md`, § 1 et § 2 E13-1) ; plancher absolu de signalement gelé, dont le franchissement interdit l'intégration (D-T3 E13-2). | La cause collective n'est pas établie (D-T1 table N13, 2e ligne) ; « le canal d'apprentissage doit être fixé avant toute analogie causale » (D-T1 table N13). |
```

### R23 — E22 — N13 (1), lecture (c1)/(c3) (l. 114 ; RN-01, RN-04, RN-06, RN-07)

**Original (v1) :**

```text
- **(c1)/(c3)** : accord large en T1 (A, C, D) sur « (c3) n'est recevable que comme sous-produit du bras collectif de (c1), le bras individuel étant son contrefactuel » ; B y vient de fait (N13-E2 « conditionnelle à N13-E1 »). **Réserve « effet d'ordre »** (c1 est présentée la première et avec le plus de détail) et **réserve R4** (quatre). La raison commune — *la cause collective n'est pas établie* — est tirée du même paragraphe des faits (pièce 4, l. 427 ; § 1.8 réserve 1) par les quatre : accord indépendant sur la prémisse, mais lue dans la même pièce.
```

**Remplacement (v2) :**

```text
- **(c1)/(c3)** : accord large à quatre dès T1 (n° 3) (B dès T1, « Ordre proposé » 5, contre la v1 ; son objection « circulaire », non reprise ni réfutée, est l'apport seul n° 13). Réserves « effet d'ordre » (c1 première et la plus détaillée) et R4. La raison commune — *la cause collective n'est pas établie* — est tenue par les quatre en T1 (A-T1 A7 ; B-T1 S6 ; C-T1 (a) 4 ; D-T1 table N13), lue au même paragraphe (pièce 4, l. 427) : raison de l'accord, pas accord à part. **Forme de (c1)** : en T3 nul ne tient deux bras seuls (D dès T1, E13-1 ; A E3″ ; B A-4 ; C C6) ; la pièce 4 nomme le témoin manquant (l. 421) et la cause concurrente (l. 427).
```

### R24 — E23 — N13 (1), critère 10 (c3) (l. 116 ; RN-04)

**Original (v1) :**

```text
- **Critère 10, (c3)** : contrefactuel traité par les quatre (A A10 ; B « circulaire » ; C fusion ; D « sous-produit »).
```

**Remplacement (v2) :**

```text
- **Critère 10, (c3)** : contrefactuel traité par les quatre (A A10 ; B Ordre 5 ; C fusion ; D « sous-produit »). L'objection « circulaire » de B porte sur autre chose : le motif d'Avalon n'est pas une menace diffuse (pièce 4, § 3.2, l. 496–497 ; § 3.6, l. 522), lecture que A (A6) et C ((a) 5) partagent sans conclure sur (c3).
```

### R25 — E24 — N13 (1), traduction de la récompense collective (l. 117, RN-14 a)

**Original (v1) :**

```text
- **Traduction de « récompense collective » pour notre organisme** : A (niveau d'attribution du crédit, A11), C (moyenne des r_j, C-T3 C6), D (R = Σ r_i, D-T3) convergent en T3 vers « la récompense collective est une fonction connue des récompenses individuelles, à information égale » (demandé par A-T2 sur C a4 et A-T2 sur D a4). B l'adopte en partie (« récompenses appariées en variance », B-T3 D-§a 3). **Convergence née de la critique.** Le point que la question laisse ouvert — l'organisme n'apprend pas par gradient (pièce 4, l. 542), donc à quoi s'applique « l'avantage collectif » — est tranché différemment : A et C sur un adaptateur local entraîné hors ligne ; B sur un renforcement en ligne de deux bras à 7 milliards ; D laisse le canal à fixer.
```

**Remplacement (v2) :**

```text
- **Traduction de « récompense collective » pour notre organisme** : A, C et D convergent en T3 vers une définition commune de l'attribution du crédit à information égale (A-T2 sur C a4, sur D a4) ; B l'adopte en partie (B-T3 D-§a 3). **Convergence née de la critique.** Forme : renvois `E3-T3-reponse-A.md`, § (a) E3 ; `E3-T3-reponse-C.md`, § (a) C6 ; `E3-T3-reponse-D.md`, § 1 E13-1. Le canal d'apprentissage (l'organisme n'apprend pas par gradient, pièce 4, l. 542) diffère : A-T1 E3 ; B-T1 N13-E1 ; C-T1 Duel 3 ; D le laisse à fixer.
```

### R26 — E25 — N13 (1), intensité d'optimisation (l. 118, RN-14 a)

**Original (v1) :**

```text
- **Intensité d'optimisation** : B-T2 sur A (E3) objecte que l'affinage hors ligne peut manquer de pression pour faire apparaître l'insularité (Avalon : CISPO, épisodes de 2 à 5 heures, lots de 200 à 800 groupes — pièce 4, l. 373–375) ; D-T2 sur C fait la même objection au Duel 3. A-T3 répond par un critère d'informativité et une règle d'escalade ; C-T3 par un gain de tâche minimal de +15 points (illustratif).
```

**Remplacement (v2) :**

```text
- **Intensité d'optimisation** : B-T2 sur A (E3) objecte que la voie bon marché peut manquer de pression pour faire apparaître l'insularité (Avalon : épisodes de 2 à 5 heures, lots de 200 à 800 groupes — pièce 4, l. 373–375) ; D-T2 sur C, même objection au Duel 3. A-T3 répond par un critère d'informativité et une règle d'escalade gelée (renvoi : `E3-T3-reponse-A.md`, § (b) E3″) ; C-T3 par un gain de tâche minimal (C7).
```

### R27 — E26 — N13 (2), ligne D, classement retiré (l. 129 ; RN-12)

**Original (v1) :**

```text
| La plus complète ; incomplète sur (iii) au sens strict. |
```

**Remplacement (v2) :**

```text
| Précaution en mesure, seuil gelé (valeurs non fixées) ; incomplète sur (iii) au sens strict. |
```

### R28 — E27 — N13 (2), lecture, éléments nés de la critique (l. 131 ; RN-03)

**Original (v1) :**

```text
En T3, trois éléments deviennent communs, chacun **né de la critique**
```

**Remplacement (v2) :**

```text
En T3, trois éléments deviennent communs, les deux premiers **nés de la critique**
```

### R29 — E28 — N13 (2), lecture, D accepte, A et D dès T1 (l. 131 ; RN-03)

**Original (v1) :**

```text
(2) pré-test du signalement du modèle de départ, « préalable absolu » (B-T2 sur A c2 ; B-T2 sur C c2 → A-T3 E3 B-c2, C-T3 C8 ; D l'avait : « plancher ou plafond de signalement rend le pilote non jugeable ») ; (3) le signalement n'entre dans aucune récompense (A-T1, D-T1 ; C-T3 C7 ; B garde un bras d'intervention mais le sort des contrôles).
```

**Remplacement (v2) :**

```text
(2) pré-test du signalement du modèle de départ, « préalable absolu » (B-T2 sur A c2 ; B-T2 sur C c2 → A-T3 E3 B-c2, C-T3 C8 ; D l'accepte de B, D-T3 § 1) ; (3) le signalement n'entre dans aucune récompense — A et D dès T1 (A-T1 E3 ; D-T1 E13-1, § 4), raisons différentes ; C le rejoint (C-T3 C7) ; B garde un bras d'intervention mais le sort des contrôles.
```

### R30 — E29 — N13 (2), critère 11, bras de B (l. 135 ; RN-09)

**Original (v1) :**

```text
Le bras « récompense du signalement » de B (T1) n'est pas un score de moniteur ; il n'est pas contraire à N-053 au sens de la pièce 2 (l. 171–173).
```

**Remplacement (v2) :**

```text
Le bras « récompense du signalement » de B (T1) : B ne dit pas comment le terme détecte un signalement ; sa seule détection définie est mécanique (appel de l'outil, B-T1 (c)) ; sous cette lecture (inférence du lecteur), il n'est pas un score de moniteur ni contraire à N-053 (pièce 2, l. 171–173).
```

### R31 — E30 — N13 (3), lecture, portée du fait de Damani (l. 148 ; RN-08)

**Original (v1) :**

```text
même s'il repose sur un fait servi commun (pièce 5, l. 725 : le classifieur post-hoc bat RLCR sur SimpleQA et GSM8K) que C a introduit en T1 et que B et D reprennent en T2/T3 en le disant.
```

**Remplacement (v2) :**

```text
même s'il repose sur un fait servi commun (pièce 5, l. 725 : le classifieur post-hoc bat RLCR sur SimpleQA et GSM8K) que C a introduit en T1 et que B et D reprennent en T2/T3 en le disant ; sur les moyennes hors domaine (Table 1, l. 692–696) RLCR reste devant ; le post-hoc de Damani est un classifieur entraîné (l. 667), non une recalibration de Platt (l. 832) ; « recalibration d'abord » tient au coût (B-T3 III), non à la pièce 5.
```

### R32 — E31 — N13 (3), apport distinct (l. 150 ; RN-01)

**Original (v1) :**

```text
A et C citent la même raison (frontière jamais entraînée, N-045 énoncé 8) : accord indépendant.
```

**Remplacement (v2) :**

```text
A, C et D s'accordent sur « chantier de mesure, entraînement à prouver » (accord n° 4, pièce 5, § 3 (b)) ; « RLCR seulement pour un juge local » (A A12 ; C (a) 6 ; D § 4) découle de N-045 énoncé 8 : non compté.
```

### R33 — E32 — lien 1 (l. 160 ; RN-01)

**Original (v1) :**

```text
1. **« L'étape 2 est le préalable commun aux deux nœuds »** — A (E1 n'existe pas hors de l'étape 2 ; E3″ hors ligne peut la précéder : A-T3 « L'expérience à faire en premier »), B (« Tout le reste… requiert l'étape 2 opérationnelle », B-T3 III), C (Duels 1 et 3 logés dans l'étape 2 ; C-T1 (d)), D (étape 2 sur N-045, pilotes isolés : D-T3 § 3). Quatre espèces ; réserve R4.
```

**Remplacement (v2) :**

```text
1. **« L'étape 2 est le préalable commun aux deux nœuds »** — en T1, B (S11 ; N12-E1) et C (Duels 1 et 3) ; A (E3 hors ligne « peut la précéder », A-T3) et D (pilote isolé, D-T3 § 3) ne lient pas N13 à l'étape 2. La dépendance à l'étape 2 étant dans la question : lien rapporté, pas un accord.
```

### R34 — E33 — lien 3 (l. 162 ; RN-01)

**Original (v1) :**

```text
Deux espèces, raison commune : accord indépendant.
```

**Remplacement (v2) :**

```text
Deux espèces : sous-raison de l'accord n° 2 chez A et C, pas un accord à part.
```

### R35 — E34 — lien 6 (l. 165 ; RN-01)

**Original (v1) :**

```text
Lien 3 ↔ 4 par deux espèces, non repris par A ni B.
```

**Remplacement (v2) :**

```text
Deux objets (D : forme de la couche 4 ; C : étanchéité du bac à sable, pièce 4, l. 548) : lien rapporté, pas un accord.
```

### R36 — E35 — famille 1, A sur lui-même (l. 174 ; RN-03)

**Original (v1) :**

```text
| B (A-5), C (C8 : k = 3), D (§ 1 « Unité d'inférence »), A sur lui-même (E3″ : ≥ 3 graines) |
```

**Remplacement (v2) :**

```text
| B (A-5), C (C8 : k = 3), D (§ 1 « Unité d'inférence ») ; A applique sa propre critique à E3″ : pas une cession |
```

### R37 — E36 — famille 4, raison (l. 177 ; RN-08)

**Original (v1) :**

```text
| Isoler la composante de calibration de l'effet de l'entraînement ; dans Damani même, le post-hoc fait jeu égal ou mieux hors domaine (pièce 5, l. 725). |
```

**Remplacement (v2) :**

```text
| Isoler la composante de calibration de l'effet de l'entraînement ; dans Damani même, le classifieur post-hoc fait jeu égal ou mieux sur certains jeux hors domaine (pièce 5, l. 725), non sur les moyennes (l. 692–696). |
```

### R38 — E37 — famille 10 (l. 183, RN-14 a)

**Original (v1) :**

```text
| 10 | Récompense collective = fonction connue (somme ou moyenne) des récompenses individuelles, à information et effectif égaux | A-T2 sur C (a4), sur D (a4) | C (C6), D (§ 1 E13-1 : R = Σ r_i), B (variance appariée) | Sinon le bras individuel reçoit un signal plus riche, pas seulement mieux attribué. |
```

**Remplacement (v2) :**

```text
| 10 | Définition commune de l'attribution du crédit collectif, à information et effectif égaux (forme : renvois `E3-T3-reponse-C.md`, § (a) C6 ; `E3-T3-reponse-D.md`, § 1 E13-1 ; `E3-T3-reponse-B.md`, § I D-§a 3) | A-T2 sur C (a4), sur D (a4) | C (C6), D (§ 1 E13-1), B (variance appariée) | Sinon le bras individuel reçoit un signal plus riche, pas seulement mieux attribué. |
```

### R39 — E38 — apport 1 (l. 194, RN-14)

**Original (v1) :**

```text
1. **A — E3′ / E3′′ : diffusion sans entraînement**, plan canal partagé / muet × N ∈ {1, 2, 4, 8}, séparant diffusion (taux par run baisse), coordination (par agent baisse, par run constant) et canal (A-T1 E3′ ; A-T3 E3′′, après C-T2 b1/c1 et D-T2 b).
```

**Remplacement (v2) :**

```text
1. **A — E3′ / E3′′ : diffusion sans entraînement**, par inférence seule, en faisant varier l'effectif et le canal, pour séparer diffusion (taux par run baisse), coordination (par agent baisse, par run constant) et canal (plan : renvoi `E3-T1-conception-A.md`, § (b) E3′ ; `E3-T3-reponse-A.md`, § (b) E3′′, après C-T2 b1/c1 et D-T2 b).
```

### R40 — E39 — apport 3, faux trilemme (l. 196 ; RN-02)

**Original (v1) :**

```text
3. **A — « faux trilemme »** : (c1) et (c3) ne sont pas exclusives (A-T1 A10). Repris en substance par C (fusion) et D (sous-produit) sans attribution ; je le compte en apport initial de A et accord large.
```

**Remplacement (v2) :**

```text
3. **A — « faux trilemme »** (A-T1 A10) : retiré ; la substance est tenue en T1 par B (conditionnelle), C (fusion) et D (sous-produit) : accord n° 3, dont « faux trilemme » n'est que le mot de A.
```

### R41 — E40 — apport 7, N13-E2a (l. 200 ; RN-02)

**Original (v1) :**

```text
7. **B — N13-E2a** : prédiction de l'omission *avant* le point de décision (tour t−1), que la vérification mécanique ne peut pas faire (B-T3 I A-6). Né de la critique d'A (« la cible utile est la prédiction avant le point de décision », A-T2 sur B a6) ; B l'opérationnalise seul.
```

**Remplacement (v2) :**

```text
7. **B — N13-E2a** : prédiction de l'omission *avant* le point de décision (B-T3 I A-6) : retiré ; né de la critique d'A (A-T2 sur B a6), c'est la famille 2 ; B l'opérationnalise seul.
```

### R42 — E41 — apports 11 à 13 et bilan (l. 204 ; RN-02, RN-04)

**Original (v1) :**

```text
11. **D — distinguer omission fautive, absence d'obligation, simple non-action ; marquer « non évaluable » plutôt que laisser un juge créer les étiquettes** (D-T1 table N13 ; § 3 table « Détecteur de signalement omis »). Repris partiellement par A-T3 E4′ (cas « C vrai, signalement non dû ») et B-T3 E2b, sans la règle « non évaluable ».
```

**Remplacement (v2) :**

```text
11. **D — règle « non évaluable »** (D-T1 § 3 table) ; le triple partage fautif / non dû / non-action (D-T1 table N13), repris par A-T3 E4′ et B-T3 E2b, est une convergence.
12. **D — risque de la couche 3** : effets indirects, bac à sable non prouvé correct, déplacement du problème (D-T1 table N12). Non repris, non réfuté.
13. **B — (c3) « circulaire »** : le motif d'Avalon n'est pas diffus (B-T1 point 2 ; S8) ; pire cas : valider les sondes sur un cas plus facile que la cible ; maintenu en T3 (B-T3 III, « établi » 2) ; pièce 4, § 3.2, l. 496–497 (« Diffuse : en partie », « Menace : non établie »), § 3.6, l. 522 ; A (A6) et C ((a) 5) partagent la prémisse sans la conséquence ; non réfuté.
```

### R43 — E42 — inexactitudes B, en-tête (l. 215 ; RN-05)

**Original (v1) :**

```text
**B (1 ferme, 1 renvoi).**
```

**Remplacement (v2) :**

```text
**B (1 ferme, 1 renvoi, 1 à la limite).**
```

### R44 — E43 — inexactitudes B, ajout (l. 217 ; RN-05)

**Original (v1) :**

```text
Le chiffre est exact mais figure en § 3 (b) 3 (l. 827) ; le § 1.11 (l. 749) dit seulement que les intervalles sont des bootstrap sur exemples. Renvoi de section.
```

**Remplacement (v2) :**

```text
Le chiffre est exact mais figure en § 3 (b) 3 (l. 827) ; le § 1.11 (l. 749) dit seulement que les intervalles sont des bootstrap sur exemples. Renvoi de section.
- B-T1 S1 : « règle d'agrégation par du code », « sélection parmi des pièces existantes » dans le non-couvert, contre l'énoncé 1 (l. 72–74) et les énoncés 5, 6 (ii). À la limite (critère 5, symétrique de A) ; précisé par B-T2 sur C.
```

### R45 — E44 — inexactitudes C, en-tête (l. 219 ; RN-08)

**Original (v1) :**

```text
**C (0 chiffre inexact ; 1 renvoi répété ; 1 affirmation hors des faits).**
```

**Remplacement (v2) :**

```text
**C (0 chiffre inexact ; 1 renvoi répété ; 1 affirmation hors des faits ; 1 à la limite).**
```

### R46 — E45 — inexactitudes C, ajout (l. 222 ; RN-08)

**Original (v1) :**

```text
C est seulement incohérent avec lui-même.
```

**Remplacement (v2) :**

```text
C est seulement incohérent avec lui-même.
- C-T1 Duel 4 (« fondement factuel ») et (d) 2 : recalibration de Platt donnée pour établie par Damani ; le post-hoc de la pièce 5 est un classifieur entraîné (l. 667), sans « méthode de recalibration sans entraînement » (l. 832). À la limite (critère 8).
```

### R47 — E46 — inexactitudes D, classement retiré (l. 225 ; RN-12)

**Original (v1) :**

```text
D n'avance presque aucun chiffre : c'est la plus prudente, comme A-T2 le relève (« D est la plus prudente sur les statuts »), au prix d'une conception « laissée en paramètres ouverts » (A-T2 sur D, en-tête).
```

**Remplacement (v2) :**

```text
D n'avance presque aucun chiffre ; A-T2 sur D (en-tête) la dit « la plus prudente sur les statuts » et « laissée en paramètres ouverts » : jugement de A, rapporté.
```

### R48 — E47 — pièces, couche 4 (l. 236 ; RN-08)

**Original (v1) :**

```text
| **Sans dépense de carte** ; appels de sous-agents non chiffrés par A, B, D ; C : « 0 $ en calcul GPU, quelques dollars d'appels ». Conclusion bornée à la banque (A, D). |
```

**Remplacement (v2) :**

```text
| **Sans carte** (hors critère 13) ; appels d'agents non chiffrés par A et B ; C : « quelques dollars d'appels » ; D : « CPU seul… 50–500 € » (D-T1 § 4) ; statut non tranché sur les cellules. Conclusion bornée à la banque (A, D). |
```

### R49 — E48 — pièces, Agrawal (l. 240 ; RN-12)

**Original (v1) :**

```text
| Hors portée ; je le note pour la veille, sans recommander. |
```

**Remplacement (v2) :**

```text
| Hors portée (PDF non versé) ; aucune espèce ne la propose comme pièce. |
```

### R50 — E49 — pièces, N13 (3) (l. 241 ; RN-08)

**Original (v1) :**

```text
| Calcul sur paires déjà produites par les courses, contre l'oracle planté ; montre si un entraînement RLCR a un objet | **Sans dépense** : la seule pièce de ce type sur les six sous-questions, et les quatre y convergent (réserve R4). |
```

**Remplacement (v2) :**

```text
| Calcul sur paires déjà produites, contre l'oracle planté, **après extraction des confiances** (A-T1 (d) ; C-T3 § 4) — aucune cellule n'établit qu'elles sont journalisées ; montre si un entraînement RLCR a un objet | **Sans dépense** pour le calcul ; seule pièce de ce type si les appels d'agents de N12 (2) sont une dépense ; les quatre y convergent (réserve R4). |
```

### R51 — E50 — divergence 1 (l. 249 ; RN-09)

**Original (v1) :**

```text
« HYPOTHÈSE de lecture à faire confirmer par Lazar ». C ne répond pas. **Nœud de lecture d'une décision**, pas de méthode.
```

**Remplacement (v2) :**

```text
« HYPOTHÈSE de lecture à faire confirmer par Lazar ». C ne répond pas. **Pièce qui trancherait** : N-053, point 5, cité par la pièce 2 (l. 171–173 : « signal d'entraînement **ou de sélection** de l'agent »), plus un fait absent de A-T3 E1′ : les fiches filtrées entrent-elles ensuite dans un entraînement (N-045, énoncés 4, 6 (ii)) ? **Nœud de lecture d'une décision**, pas de méthode.
```

### R52 — E51 — divergence 4 (l. 252 ; RN-11)

**Original (v1) :**

```text
4. **Nature de la précaution de N13 (2)** : mesure dans tout bras (A) ; prérequis causal (B) ; plancher et chute maximale gelés, arrêt hors du bac à sable (D) ; C passe de « conception de la récompense » à « cloisonnement ». Convergence sur trois éléments (voir table), divergence sur le reste ; aucune ne nomme qui lit.
```

**Remplacement (v2) :**

```text
4. **Nature de la précaution de N13 (2)** : mesure dans tout bras (A : cause collective non établie, A-T1 (c)) ; prérequis causal (B : sinon S6 supposée sans test, B-T1 point 1) ; plancher et chute maximale gelés, arrêt hors du bac à sable (D : le signalement n'est pas « une monnaie d'échange », E13-2) ; C passe à « cloisonnement » (C7). En litige : nature du seuil (jugeabilité A, décision C, arrêt D, aucun B) ; prérequis (B) ou mesure dans tout bras (A, C, D) ; nul ne nomme qui lit.
```

### R53 — E52 — divergence 5 (l. 253 ; RN-11)

**Original (v1) :**

```text
5. **Forme d'une ouverture de la couche 4** : restreinte à une classe d'erreurs mesurée (A) ; lemmes critiques seulement (C : Q2, N4) ; vérificateur externe, jamais couche autonome (D) ; « quand le coût d'opportunité est nul » (B).
```

**Remplacement (v2) :**

```text
5. **Forme d'une ouverture de la couche 4** : classe d'erreurs mesurée (A, E2′) ; lemmes critiques seulement (C-T3 Duel 2 corrigé : « Q2 et N4 » sont des codes de la pré-collision, pièce 3, l. 215, 253, 307, non le nœud N4 de la v12) ; vérificateur externe d'abord, « sans imposer une couche 4 autonome » (D-T1) ; « quand le coût d'opportunité est nul » (B-T1 Ordre 6). Aucune ne dit « jamais ».
```

### R54 — E53 — divergence 6 (l. 254 ; RN-11)

**Original (v1) :**

```text
6. **Première expérience** : E3′′ + E5′ (A) ; Platt puis N13-E3 (B) ; pilote A/A + p₀ + audit de calibration à froid (C) ; E0 pilote de jugeabilité (D). Convergence sur « sans entraînement, processeur ou inférence seule », divergence sur l'objet (signalement de départ : A, C, D ; calibration des juges : B, C).
```

**Remplacement (v2) :**

```text
6. **Première expérience** : E3′′ + E5′ (A : règle d'arrêt de E3″, coût marginal nul) ; Platt puis N13-E3 (B : hors étape 2, minutes de processeur) ; pilote A/A + p₀ + audit à froid (C : ligne de base des duels) ; E0 (D : ne pas financer un duel illisible). Compléments, non exclusions, tous sans entraînement ; divergence sur l'objet mis en premier (signalement de départ : A, C, D ; calibration des juges : B, C).
```

### R55 — E54 — divergence 7 (l. 255 ; RN-11)

**Original (v1) :**

```text
7. **Exécution d'opérateurs générés hors du bac à sable comme contrôle (B contre C).** B-T2 sur C (c3) ; C-T3 C2 : rejet partiel, « interdit par l'invariant du noyau gelé ». Non tranché.
```

**Remplacement (v2) :**

```text
7. **Exécution d'opérateurs générés hors du bac à sable comme contrôle (B contre C).** B-T2 sur C (c3) ; C-T3 C2 : rejet partiel, « interdit par l'invariant du noyau gelé ». Aucune pièce des faits ne porte cet invariant (C renvoie à la question, § N12 « Contexte », et à la pièce 4, l. 548) ; B veut mesurer ce que l'isolation coûte. Tranchable par la définition de la couche 3 (Lazar), non sur les faits.
```

### R56 — E55 — accords trop propres, N12 (3) (l. 263)

**Original (v1) :**

```text
- N12 (3) : « étape 2 d'abord » à quatre — option de la question et position de la pré-collision (effet d'ordre).
```

**Remplacement (v2) :**

```text
- N12 (3) : « étape 2 d'abord » à quatre — position de la pré-collision citée par la question : non comptée (critère 3).
```

### R57 — E56 — accords trop propres, N13 (1) (l. 264)

**Original (v1) :**

```text
- N13 (1) : « (c3) sous-produit de (c1) » à quatre — (c1) présentée la première et la plus détaillée (effet d'ordre) ; « (c2) écartée » à quatre pour la raison que donne la question (vrai par construction).
```

**Remplacement (v2) :**

```text
- N13 (1) : « (c3) sous-produit de (c1) » à quatre dès T1 — (c1) présentée la première et la plus détaillée (effet d'ordre) ; « (c2) écartée » à quatre pour la raison que donne la question (vrai par construction, non comptée).
```

### R58 — E57 — accords trop propres, prémisse (l. 265)

**Original (v1) :**

```text
- N13 (1) prémisse : « la cause collective n'est pas établie » à quatre, lue au même paragraphe (pièce 4, § 1.8 réserve 1).
```

**Remplacement (v2) :**

```text
- N13 (1) prémisse : « la cause collective n'est pas établie » à quatre, lue au même paragraphe (pièce 4, § 1.8 réserve 1) — raison de l'accord n° 3, non comptée à part.
```

### R59 — E58 — critère 17 (l. 272 ; RN-12)

**Original (v1) :**

```text
elle ne recommande rien, ne classe pas les espèces, et ne dit pas laquelle
```

**Remplacement (v2) :**

```text
elle ne recommande rien, ne classe pas les espèces (classements de la v1 retirés), et ne dit pas laquelle
```


FIN-DE-ERRATUM
