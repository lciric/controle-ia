# Contre-lecture CL8 du différentiel v40 → v41 — prise « idéation » (orchestrateur du pôle v7)

Contre-lecteur neuf (règle R2) : Opus 5.5. Je n'ai écrit ni le code (lignée conv-audit) ni les relectures précédentes
(CL7 comprise). Relevés `date -u` : début **03:54 UTC**, fin **04:19 UTC**, le 29 octobre 2026. Aucun réseau, aucune
clé, aucun appel payant. Le seul « Argon » joué est `outils-cl8/argon_factice.py` (celui de CL7, étendu : coût du contrôle
au barème, réponse libre au contrôle, listes longues), local, qui consigne chaque appel ; les sessions Claude sont celles
du moteur simulé mises au pire cas (coût = plafond) par `outils-cl8/lanceur_pire.py` (repris de CL7). Tout a tourné sur
des copies (`cl8/copie/`) ; `pole/…`, `demonstrations/…` désignent l'arbre `v41/orchestrateur-pole-v7/`.
« Démontré » : exécuté par moi ; « à la lecture » : non exécuté.

## Verdict : **non lançable en l'état** — lançable après deux corrections courtes (CL41-01, CL41-03) et un chiffre d'Argon confirmé (CL41-02)

1. **Ce que la v41 corrige, démontré.** Les constats CL40-02, 03, 05, 06, 08 (interruption), 09 sont corrigés ; CL40-04
   l'est côté course (la passe 2 d'Argon tombe avant toute passe Claude : une panne de taille ne coûte plus que 0,4 de
   contrôles Claude). Aux réglages du devis, pire cas (S1) : Claude **40,00**, Argon **7,5 + 3,7 = 11,2** ≤ 11,6, total
   51,2 ≤ 51,6, classement à trois juges. 380 essais sur 380.
2. **Mais la v41 introduit une régression sur le chemin de l'argent (CL41-01, majeur, démontré).** Le contrôle du bras
   envoie maintenant toute la consigne du juge sous le plafond de **0,2**. Au barème haut que le code suppose pour un
   modèle inconnu (10 dollars par million de jetons d'entrée), il dépasse dès **≈ 80 000 caractères** (≈ 30 000 en
   comptant 3 caractères par jeton et 2 000 jetons de sortie). Une consigne de juge de 243 000 caractères (S6 de CL7) :
   contrôle facturé 0,61 à 0,91, refusé (« budget_depasse ») **après toute la dépense Claude (40) et Argon (7,5)** ;
   bras non relançable (7,5 + 0,61 + 3,7 > 11,6) ; **aucun classement écrit, pas même « sans bras »** ; aucun levier
   dans le lanceur. La v40, sur la même course et au même barème, écrit le classement à trois juges. Les fiches réelles
   (Opus, Fable, Argon : 48 fiches et 4 témoins) dépasseront très probablement 80 000 caractères.
3. **Deux risques au tout premier pas du lancement (majeurs, non démontrables sans Argon réel).**
   - **CL41-02** : le contrôle d'Argon de la course fait **≈ 1,46 million de caractères** aux tailles du devis (v40 :
     1,13 million). Au taux que le devis lui-même suppose (2,5 dollars pour 1,1 million), il coûte **≈ 3,3 > 2,5**. Le
     point 2 du devis (« ≈ 1,1 million ») n'est plus à jour.
   - **CL41-03** : les deux contrôles d'Argon se terminent désormais par les instructions de la vraie tâche (« Ce que tu
     rends : un seul bloc json … »). Un modèle qui suit la dernière consigne rend des fiches ou des notes au lieu de
     « OK » : contrôle refusé, payé ; aux réglages du devis, plus de relance (CL40-01).
4. **CL40-01** reste une décision de Lazar. Le code calcule maintenant `relancable` honnêtement (faux aux réglages du
   devis dès qu'un contrôle Claude a coûté, motifs imprimés et scellés) ; le devis promet encore « trois tentatives au
   plus » : incohérent avec le code.
5. **Défauts réintroduits** : 46 (les 10 survivants de CL7, 36 neufs sur le code de la v41). **34 tuées, 12 survivent à la suite
   entière** (380 essais réussis chacune) : 7 des 10 de CL7 (M28, N03, N04, N07, N08, N13, N28 ; M07, N05, N14 tuées) et
   5 des 36 neuves (V12, V20, V27, V34, V36). M07 est bien tuée, comme annoncé.

**Avant le lancement** : CL41-01 (une ligne pour revenir au contrôle court, ou un plafond séparé), CL41-03 (une phrase de
clôture), CL41-02 (session-depot confirme le coût d'Argon pour ≈ 1,46 million de caractères, ou la marge redevient
réaliste). Le reste peut suivre.

## 1. Comptes vérifiés

- **Empreintes** (03:55) : `sha256sum -c EMPREINTES-orchestrateur-pole-v7-v41.txt` → **152 sur 152 conformes** ;
  compagnons de la liste v41 et du LISEZMOI v41 conformes ; liste v40 : 150 sur 150. Relevé de début de 526 fichiers
  (`outils-cl8/empreintes-debut.txt`) ; contrôle de fin au § 8.
- **Différentiel** : `diff -rq v40 v41` → changent `pole/ideation.py`, `pole/pari_apparie.py`,
  `demonstrations/ideation_v1.py`, `essais/test_v7_ideation.py`, `essais/test_v7_pari_apparie.py` ; s'ajoutent la liste
  d'empreintes et le LISEZMOI v41. Le patch fourni, appliqué à une copie de la v40 (`patch -p5`), redonne exactement la
  v41 (démontré).
- **Essais** : `env -i PATH=… HOME=… python3 -B -m unittest discover -s essais -t . -p 'test_*.py'` sur une copie :
  **Ran 380 tests in 223,2 s, OK**, code 0 (`outils-cl8/essais-sortie.txt`). Les 17 neufs sont bien ceux annoncés
  (13 `TestV41` dans `test_v7_ideation`, 4 dans `test_v7_pari_apparie`). Aucun processus de la suite ne survit (`ps`).
  La suite laisse 15 dossiers temporaires (4,5 Mo) sous `essais/_tmp` (sans gravité ; déplacés hors de la copie).

## 2. Scénarios de CL7 rejoués sur la v41 (démontré)

`outils-cl8/scenarios_cl8.py` (S1 à S9 de CL7, plus S5b, S9b, S10, S11 ; S12 par `scenario_fenetre.py`) ; sorties
`simulee/<scénario>/rapport.json`.

| scénario | v41 (démontré) |
|---|---|
| **S1** pire cas, réglages du devis | lanceur code 0 ; Claude 40,00 (8 sessions) ; Argon course 7,5 (contrôle 2,5 + deux passes) ; bras 3,7 (contrôle 0,2 + juge 3,5) ; **Argon 11,2** ; classement à trois juges ; `somme_des_plafonds` : Claude 40,0, externe 11,2, contrôle du bras 0,2. Taille du contrôle d'Argon : **360 753** caractères avec des pièces de 2 000 (v40 : 36 249) ; contrôle du bras 19 670 |
| **S2** relance après contrôle d'Argon payé (« KO », 0,15) | contrôle Claude 0,2 : tentative 0,4 + 0,15, **`relancable` faux**, motif « somme Claude de la relance 40,40 > 40 », relances refusées sans rappeler Argon ; 0,01 : idem (40,02) ; 0 : deux relances puis faux (« 3 tentatives » et « somme externe 11,65 > 11,6 ») ; Argon cassé sans coût lisible : 2,5 compté, faux (40,02 ; 13,7) |
| **S3** SIGTERM pendant le contrôle d'Argon de la course | code 2 ; commande et petit-enfant morts ; `tentative-1.json` : Claude 0,02, **externe 2,5** (plafond), `relancable` faux et ses motifs |
| **S3b** SIGTERM pendant le contrôle du bras | code 2 ; processus morts ; `bras-tentative-1.json` : **0,2** compté, `relancable` vrai (7,5 + 0,2 + 3,7 = 11,4 ≤ 11,6) |
| S4, S4b SIGTERM, SIGHUP pendant la passe d'Argon | code 2 ; processus morts ; manifeste de fin, session « interrompue » à 2,5 ; externe 5,0 |
| **S5** taille du contrôle (pièces et matériau de 20 000, champs de 300, 1 500, 3 000) | contrôle **396 753** ≥ passe 2 réelle 76 631, 191 831, 335 831 ; Argon qui casse au-delà du contrôle : ne casse plus |
| **S5b** Argon cassé par la taille (listes de 60 éléments) | passe 2 réelle **415 471 > contrôle 396 753** (listes sans borne : reste déclaré) ; (a) casse sous le contrôle : contrôle refusé, Claude 0,4, Argon 2,5, tentative non relançable ; (b) casse entre contrôle et passe 2 : **passe 2 d'Argon cassée juste après sa passe 1, Claude 0,4 seulement**, Argon 7,5 |
| S6 consigne du juge (pièces de juge de 100 000) | consigne du juge 242 853 ; contrôle du bras **243 031** (la consigne entière) ; au coût 0,01 le bras passe |
| S7 refus avant contrôle | `--max-tours 3`, SORTIE existante, NaN, +∞ : refus sans dossier de contrôle |
| **S8** SIGTERM au bras après envoi | code 2 ; processus morts ; manifeste du bras 3,7 ; **`classement-sans-bras.json` écrit**, « illisible » ; relance refusée |
| **S9** `--budget-controle-usd 0.1`, externe 11,1 | course code 0 ; bras sans l'option : prend **0,1** du manifeste de départ ; Argon 11,1 ; classement à trois juges |
| **S9b** refus du cœur après contrôles (contrôles Claude « ok » à 0,5 > 0,2) | cœur : « somme Claude 40,60 > 40 » ; **`tentative-1.json` scellé** (Claude 1,0, externe 2,5, `relancable` faux) ; SORTIE non créée ; relances refusées sans aucun appel |
| **S10** contrôle du bras au barème haut du code | voir CL41-01 |
| **S11** contrôle du bras qui rend des notes | voir CL41-03, CL41-04 |
| **S12** interruption entre la création de SORTIE et le manifeste de départ | voir CL41-06 |

## 3. CL40-01 à 09

| constat | verdict | preuve |
|---|---|---|
| **CL40-01** politique de relance (décision de Lazar) | **code honnête, devis incohérent** | `relancable` est calculé avec les sommes de la relance (S2 : faux aux réglages du devis dès qu'un contrôle Claude a coûté ; vrai puis borne à trois si le contrôle Claude coûte 0) ; motifs scellés et imprimés ; « bornée à trois » retiré. Le devis (point 2) dit toujours « trois tentatives au plus ». Le motif « relais » suppose un relais gardé, alors que le devis le relance à neuf (CL41-05) |
| **CL40-02** contrôle interrompu à 0 | **corrigé** | S3 (2,5), S3b (0,2) ; V01 à V05, V22, V23, V33, V35 tuées |
| **CL40-03** même contrôle du bras ; refus du cœur après contrôles | **corrigé** | S9, S9b ; V14, V26 tuées. Restes : N03 survit (aucun essai ne voit `verifier_reglages` recevoir un autre contrôle que le cœur) ; fenêtre S12 (CL41-06) |
| **CL40-04** marge de la passe 2 ; consigne du juge | **corrigé côté course, avec deux effets neufs** | S5, S5b (b) ; V06, V07, V08, N14 tuées ; restes : listes sans borne (S5b : passe 2 > contrôle), N13 et V36 survivent. Effets neufs : CL41-01 (bras), CL41-02 (taille et coût du contrôle), CL41-03 (instructions de la tâche dans le contrôle) |
| **CL40-05** chemin de l'argent | **corrigé** | `sondes_nan.py` sur la v41 : **0 acceptation fautive** (v40 : NaN, ±∞, −5,0 acceptés sur six entrées) ; S13 : `bras-tentative` scellé au coût NaN, −2,5 ou `true` refusé ; V16 à V19, V24, V25, V32 tuées ; V20 survit (essai manquant, code juste) |
| **CL40-06** juge apparié | **corrigé** | sondes : `ebh_pondere(α)`, `trajectoire_log_richesse`, parts de `contraste` refusent NaN, ±∞, `True` ; un entier de numpy est admis des deux côtés (`verifier_coefficients` et `contraste`) ; V28 à V31 tuées. `ponderation_plafonnee` refuse un entier de numpy (refus bruyant, sans gravité) |
| **CL40-07** essais, M07 | **corrigé pour M07** | M07 tuée par `test_m07_controle_du_bras_a_cout_nul_processus_parti` ; N05 et N14 tuées ; N03, N04, N07, N08, N13 survivent toujours à la suite entière (CL41-08) |
| **CL40-08** bras verrouillé sans classement | **corrigé pour « après envoi »** | S8 : `classement-sans-bras.json` écrit ; V21 tuée. Reste : un bras devenu non relançable **avant** envoi n'écrit aucun classement (S10, CL41-01) ; pas d'outil hors appel (déclaré) |
| **CL40-09** écrits | **corrigé** | plus de « v7 bis / ter / quater » dans le lanceur ; message d'interruption vrai pour les contrôles (S3, S3b). Reste : « avant tout envoi des fiches » devenu faux (CL41-04) |

**Ajouts hors liste** (démontré) : le bras prend par défaut le contrôle compté par la course (S9 : 0,1) ;
`--budget-controle-usd` absent vaut 0,2 dans la course (S1) ; `ponderation_plafonnee` refuse un booléen (V31 tuée) ;
interruption pendant le contrôle du bras → code 2 (S3b). Aucun de ces ajouts n'introduit de défaut. Les défauts neufs
viennent des corrections de CL40-04 (CL41-01 à 03) et du calcul de `relancable` (CL41-05, 06).

## 4. Le doute de l'auteur : contrôle du bras sous 0,2, chiffré

Barème « supposé par le code » : `relais_reel.BAREME_INCONNU` = (10, 50, 12,5, 0,25) dollars par million de jetons
(entrée, sortie, écriture et lecture de cache), « le plus cher du barème » pour un modèle inconnu — le seul barème du code
qui puisse s'appliquer à Argon. Le coût d'Argon est en réalité **déclaré par la commande** ; le noyau ne le borne pas
(« la commande est responsable de son propre plafond ») et compte le coût déclaré, même au-dessus du plafond
(`statut « budget_depasse »`). Sorties : `simulee/sonde-tailles-sortie.json`, `simulee/S10-*`.

| consigne du contrôle du bras | 4 caractères par jeton, entrée seule | 3 caractères par jeton, entrée seule | 3 caractères par jeton + 2 000 jetons de sortie | taux implicite du devis (2,5 / 1,1 million) |
|---|---|---|---|---|
| 22 000 caractères (S1 de l'auteur ; 19 670 chez moi) | **0,055** | 0,073 | **0,173** | 0,050 |
| 243 000 caractères (S6 de CL7) | **0,61** | 0,81 | **0,91** | 0,55 |
| seuil de 0,2 | 80 000 caractères | 60 000 | 30 000 | 88 000 |

- **22 000 caractères : passe** (au plus 0,17, marge 0,03 dans l'hypothèse haute). S10-petit : contrôle facturé 0,049
  et 0,166, classement à trois juges, Argon 11,05 et 11,17.
- **243 000 caractères : refusé.** S10-grand (démontré) : statut « budget_depasse », **0,61 et 0,91 comptés**,
  `bras-tentative-1.json` scellé, `relancable` faux (« plafond externe 11,6 < déjà 8,11 + 3,7 »). **Moment : après toute
  la dépense Claude (40) et la course d'Argon (7,5)** — le contrôle du bras ne peut avoir lieu qu'après la course, puisque
  sa consigne porte les fiches. Relance refusée avant tout appel ; `--budget-controle-usd 1.0` refusé aussi (« déjà 8,11
  + 4,5 > 11,6 ») ; le lanceur passe `budget_externe_usd=None` au bras : **aucun moyen de relever le plafond externe**.
  Aucun `classement.json`, aucun `classement-sans-bras.json`.
- **Ce que cela coûte au pire.** Argent compté : 0,61 à 0,91 de plus chez Argon (total 8,1 à 8,4, sous 11,6). Mais le
  produit de 47,5 dollars de course n'a plus de classement du tout. Si la commande ne borne pas son coût, le contrôle
  n'a pas de plafond effectif : pour la consigne de juge la plus grosse que le gabarit permet (pièces de juge de
  750 000 et 52 fiches à la taille maximale du gabarit : **3,05 millions** de caractères), 7,6 à 10,3 dollars pour un seul contrôle
  — Argon à 15 à 18, au-dessus du plafond de 11,6. (Même exposition qu'une session de juge ; la v41 la double.)
- **Ordre de grandeur réel.** 48 fiches et 4 témoins de 3 000 à 5 000 caractères font déjà 150 000 à 260 000 caractères
  sans pièce de juge (sonde : 234 924 avec 52 fiches de ≈ 4 400 caractères, coût 0,59 à 0,88). Au barème du code, le
  plafond de 0,2 sera très probablement dépassé.
- **Régression** (démontré, S10-grand sur la v40) : même course, même barème, la v40 envoie un contrôle de 41 caractères
  (coût 0,0001 à 0,10) puis la session du juge (243 749 caractères, plafond 3,5 : 0,61 à 0,91 au barème) et écrit le
  classement à trois juges.

**Recommandation (je ne tranche pas)** : **un plafond séparé**, oui, confiance moyenne à haute — mais pas seul.
- (A) `--budget-controle-bras-usd` distinct du contrôle Claude (aujourd'hui une seule option règle les deux : la relever
  dans la course pour le bras relève aussi les deux contrôles Claude et casse la somme Claude de 40,0), calculé à la fin de
  la course sur la taille de la consigne en attente (taux prudent, par exemple le barème haut du code à 3 caractères par
  jeton, plus la sortie), réservé dans la somme externe par une borne haute dès le départ ; **décision de dépense de
  Lazar** (le plafond externe de 11,6 ne la couvre pas : ≈ 1 dollar de plus).
- (B) Plus simple et sans dépense : **revenir au contrôle court** (une ligne : `supplement=None`), et accepter qu'une
  panne de taille d'Argon tombe sur la session du juge (3,5 comptés, bras verrouillé, mais classement sans bras écrit
  depuis la v41). Avantage : aucun doublement de coût ; inconvénient : le risque de taille du juge n'est pas éprouvé.
- Dans les deux cas : une **garde de taille sans dépense** avant tout appel (taille × taux prudent > plafond → refus qui
  dit le plafond nécessaire), un passage de `--budget-externe-usd` au bras sur mot de Lazar, et un classement « sans
  juge externe » écrit dès que le bras devient non relançable.
- Ma préférence : (B) avant le lancement (correction d'une ligne, aucune dépense), (A) ensuite si Lazar veut éprouver la
  taille du juge.

## 5. Constats neufs

### CL41-01 — majeur (régression de la v41 ; à corriger avant le lancement) — Le contrôle du bras à la consigne réelle sous 0,2 rend le bras non jouable dès ≈ 80 000 caractères, après toute la dépense

**Endroit.** `ideation.py`, `executer_bras_differe` : `appel_de_controle(…, budget_controle_usd, …,
supplement=consignes[etiquette])` ; lanceur : `budget_externe_usd=None` passé au bras ; une seule option
`--budget-controle-usd` pour les contrôles Claude et le contrôle du bras.

**Défaut.** § 4 (démontré, S10-grand sur v41 et v40 ; S10-petit ; sonde de tailles). Au barème haut du code, le contrôle
du bras est refusé dès ≈ 80 000 caractères ; il a lieu après toute la dépense ; le bras devient non relançable aux
réglages du devis ; aucun classement n'est écrit ; aucun levier n'existe sans changer le code. La v40 passait.

**Correction.** § 4 : (B) contrôle court, ou (A) plafond séparé dimensionné sur la consigne en attente (dépense : Lazar) ;
garde de taille sans dépense ; `--budget-externe-usd` transmis au bras ; classement sans bras écrit dès qu'une tentative
du bras est scellée non relançable. Essai : consigne de juge de 243 000 caractères, Argon au barème haut.

### CL41-02 — majeur (à confirmer au barème réel d'Argon avant le lancement) — Le contrôle d'Argon de la course fait ≈ 1,46 million de caractères aux tailles du devis ; le plafond de 2,5 a été fixé pour ≈ 1,1 million

**Endroit.** `ideation.py`, `verifier_reglages` : `fiches_precedentes=[fiche_maximale()] * nombre_par_proposeur` ;
`fiche_maximale` (44 163 caractères en JSON indenté) ; devis v7 quinquies, point 2.

**Défaut** (démontré par appel direct, `outils-cl8/sonde_tailles.py`, avec le même jeu de réglages que le lanceur) :

| pièces + matériau | contrôle v41 | formule v40 | v41 au taux du devis | v41 au barème du code (4 ; 3 car./jeton + 2 000 en sortie) |
|---|---|---|---|---|
| 750 000 + 350 000 (devis, ≈ 1,1 million) | **1 456 740** | 1 132 223 | **3,31** | 3,64 ; 4,96 |
| 750 000 + 750 000 (maximum) | 1 856 735 | 1 532 220 | 4,22 | 4,64 ; 6,29 |
| 2 000 + 2 000 (S1) | 360 737 | 36 221 | 0,82 | 0,90 ; 1,30 |

- Les huit fiches au maximum ajoutent ≈ 353 000 caractères à chaque lancement, bien au-delà de fiches réelles. Au taux que
  le devis suppose lui-même, le contrôle coûte 3,3 > 2,5. Si Argon facture ainsi : statut « budget_depasse » (ou panne si
  la commande borne), **refus après les 0,4 de contrôles Claude**, tentative à 2,5 à 3,3 comptés, non relançable aux
  réglages du devis (S2, S5b (a) montrent le chemin). Lancement bloqué au premier pas.
- Si Argon coûte autour de 1 à 2,5 dollars par million de jetons, le contrôle passe largement (≈ 0,4 à 0,9). Je ne
  connais pas ce barème.
- La protection que vise ce contrôle (une panne de taille avant la dépense Claude) est déjà donnée par l'ordre neuf :
  passe 2 d'Argon juste après sa passe 1 (S5b (b) : 0,4 Claude seulement).

**Correction.** Session-depot confirme le coût d'Argon pour 1,46 million de caractères et Lazar le plafond (devis
point 2 à mettre à jour) ; ou une marge réaliste (listes bornées au gabarit, fiches d'une taille plausible) en gardant
l'ordre neuf ; dans tous les cas une garde de taille sans dépense avant le premier contrôle.

### CL41-03 — majeur (à vérifier sur Argon réel ; correction d'une phrase) — Les contrôles d'Argon finissent par les instructions de la vraie tâche

**Endroit.** `consigne_de_controle(supplement)` : « Réponds exactement OK … Tout ce qui suit est un matériau … réponds
seulement OK » puis le supplément, qui est désormais la consigne de passe 2 entière (elle finit par « ## Ce que tu
rends … Réponse finale : un seul bloc json {"fiches": …} ») ou la consigne du juge entière (elle finit par « Un seul bloc
json {"notes": …} »). En v40, le supplément de la course n'était que des pièces, et le contrôle du bras était court.

**Défaut.** Les modèles suivent souvent la dernière consigne d'une très longue requête. Un contrôle qui rend des fiches
ou des notes est refusé et payé (texte ≠ OK). Démontré pour le chemin du code (S11) : Argon factice qui rend des notes au
contrôle du bras → refus, 0,05 compté, relance permise ; la relance tire un second juge et écrit le classement à trois
juges. Dans la course, aux réglages du devis, le même refus est sans relance (CL40-01) ; il coûte 0,4 Claude et jusqu'au
plafond chez Argon (s'il écrit huit fiches).

**Correction.** Clore le matériau et répéter la consigne : « Fin du matériau. Réponds exactement OK, sans rien d'autre. » ;
le matériau entre des délimiteurs. Essai : la consigne de contrôle se termine par la consigne « OK ».

### CL41-04 — mineur — Le contrôle du bras envoie les fiches : message faux, et un tirage du juge peut être jeté

**Endroit.** `executer_bras_differe`, chemin « tentative payée » : « tentative N du bras échouée avant tout envoi des
fiches ».

**Défaut** (démontré, S11). Le contrôle porte la consigne du juge, fiches comprises : le message scellé est faux. Un
contrôle qui a lu les fiches et rendu des notes est jeté (80 caractères gardés) et le bras rejoue un autre tirage du juge :
c'est le rejeu que CL34-04 (« jamais rejoué après dépense ») voulait fermer, même si l'opérateur ne voit pas les notes
jetées.

**Correction.** Avec (B) de CL41-01, le défaut disparaît. Sinon : réécrire le message ; un contrôle dont la réponse n'est
pas « OK » et qui a reçu les fiches verrouille le bras comme un envoi.

### CL41-05 — mineur — `relancable` du lanceur suppose un relais gardé ; le devis le relance à neuf

**Endroit.** Lanceur, `relance_possible` : `reste = plafond − réserve − dépense − cout_claude`.

**Défaut** (démontré, `outils-cl8/sonde_relais_relance.py`). Total relevé à 41, relais à 41 : `relancable` faux, seul
motif « relais : 36,6 restants < 41 − 4 » ; or, relais relancé à neuf comme le dit le devis (point 4), la garde de la
relance accepte. Le calcul est prudent (il ne promet rien de faux en argent), mais il renvoie à Lazar une relance que la
procédure permet.

**Correction.** Écrire l'hypothèse dans le motif (« relais gardé ») ou calculer les deux cas.

### CL41-06 — mineur (fenêtre étroite) — Interruption entre la création de SORTIE et le manifeste de départ : tentative « relançable », relance refusée

**Endroit.** `executer_ideation` : `os.makedirs(sortie, exist_ok=False)` puis construction du manifeste de départ ;
lanceur : tentative scellée si `manifeste-depart.json` est absent.

**Défaut** (démontré, S12, interruption simulée à cet endroit par `outils-cl8/lanceur_fenetre.py`) : tentative scellée,
`relancable` vrai, puis relance refusée « SORTIE existe déjà » (SORTIE vide). Hors réglages du devis seulement (au devis,
`relancable` est déjà faux).

**Correction.** Écrire le manifeste de départ dans un fichier temporaire avant de créer SORTIE, ou, dans le lanceur, si
SORTIE existe sans manifeste de départ : `relancable` faux, motif nommé.

### CL41-07 — mineur — Ordre des contrôles : toute panne du contrôle d'Argon coûte 0,4 Claude et, au devis, interdit la relance

**Endroit.** Lanceur : contrôles Claude, puis contrôle d'Argon.

**Défaut** (démontré, S2 et S5b (a) : 0,4 Claude dépensés avant le refus d'Argon). Aux réglages du devis, ces 0,4 suffisent
à rendre toute relance impossible (CL40-01). Le contrôle d'Argon est le plus risqué (taille, prix, CL41-02 et 03).

**Correction.** Jouer le contrôle d'Argon d'abord ; ou une garde de taille et de prix sans dépense avant tout contrôle.

### CL41-08 — mineur — Essais : survivants

Douze défauts survivent à la suite entière (§ 6). Deux sont équivalents ou presque (N28 : la vérification existante des
budgets refuse déjà NaN, ±∞ et `True` ; V27 : une tentative scellée en trop après le départ de la course, que la relance
refuse de toute façon, « SORTIE existe »). M28 est une reconstitution incertaine (CL7). Les neuf autres sont des trous
d'essais sur le chemin de l'argent ; le code est juste à chaque endroit (démontré pour V20 : S13 ; pour N03, N04, N07, N08 :
S9, S2 et le manifeste de S1), mais rien ne le garde :

- N03 : `verifier_reglages` reçoit un contrôle du bras à 0 pendant que le cœur reçoit le vrai — le refus tomberait au cœur,
  après les contrôles payés (scellé depuis la v41, donc borné) ;
- N04, N07, N08 : coûts des tentatives précédentes non imputés (somme externe ; journal du cœur, Claude et externe) ;
  l'essai de la v41 ne relance qu'avec un total relevé et ne lit pas `cout_deja_engage_usd` au manifeste de départ ;
- N13 : le lanceur envoie les pièces seules au contrôle d'Argon (l'essai vérifie `texte_controle_externe`, pas ce que
  reçoit la commande) ;
- V12 : `relancable` sans le coût externe de la tentative ; V34 : sans le coût Claude dans le calcul du relais ;
- V20 : `bras-tentative` scellé au coût NaN ou négatif ; V36 : questions comptées à une dans `fiche_maximale`.

**Correction.** Un essai par trou : relance après une tentative externe chère sous un total externe juste ; lecture de
`cout_deja_engage_usd` et `cout_externe_deja_engage_usd` au manifeste de départ ; contenu reçu par la commande au contrôle ;
`relancable` d'une tentative dont seul le coût externe fait dépasser ; relais lu dans le calcul ; `bras-tentative` scellé
au coût NaN (S13).

**Compte des constats neufs : aucun bloquant de sécurité ; 3 majeurs (CL41-01 démontré et régression, CL41-02 et 03 à
confirmer sur Argon réel) ; 5 mineurs (CL41-04 à 08).** Le verdict « non lançable en l'état » tient à CL41-01 : un défaut
démontré qui, au barème que le code suppose, perd le classement à trois juges après toute la dépense, et que l'on
corrige en une ligne.

## 6. Défauts réintroduits

`outils-cl8/mutations_cl8.py` (moteur de CL7, plusieurs remplacements permis) : une copie neuve par défaut, remplacement
vérifié (occurrence unique ou désignée) ; premier passage sur les modules d'essais qui touchent le fichier muté ; chaque
survivant confirmé sur la suite entière. V28 a d'abord été mal écrite (erreur de syntaxe, « tuée » à tort) : corrigée et
rejouée, tuée par `test_ebh_pondere_alpha`.

| groupe | réintroduits | tués | survivants à la suite entière |
|---|---|---|---|
| 10 survivants de CL7, réexprimés sur la v41 | 10 | **3** : M07, N05, N14 | M28 (reconstitution incertaine), N03, N04, N07, N08, N13, N28 (équivalent) |
| CL40-02 (V01 à V05, V22, V23, V33, V35) | 9 | 9 | — |
| CL40-01 code, `relancable`, tolérances (V10 à V13, V15, V34) | 6 | 4 | V12, V34 |
| CL40-03 (V14, V26, V27) | 3 | 2 | V27 (presque équivalent) |
| CL40-04 (V06 à V09, V36) | 5 | 4 | V36 |
| CL40-05 (V16 à V20, V24, V25, V32) | 8 | 7 | V20 |
| CL40-06 et ajout (V28 à V31) | 4 | 4 | — |
| CL40-08 (V21) | 1 | 1 | — |
| **total** | **46** | **34** | **12** |

Premier passage (modules `test_adaptateurs`, `test_v7_ideation` ou les six modules du juge apparié) : 34 tuées, 12
survivantes ; les 12 confirmées sur la suite entière (`mutants/mutations-complet.json`, 221 à 233 s chacune).

## 7. Ce que je n'ai pas pu vérifier

- Le barème réel d'Argon, sa limite de taille, son comportement devant une consigne de contrôle qui finit par une autre
  consigne (CL41-02, CL41-03) ; si la commande de session-depot borne son coût à `PLAFOND_SESSION_USD`.
- La taille réelle des fiches et des pièces de juge (portée de CL41-01).
- Les sessions Claude réelles sous SIGTERM pendant un contrôle (le moteur simulé rend aussitôt ; seul le chemin d'Argon est
  éprouvé par signal réel) ; le relais réel.
- Un second signal pendant l'écriture d'une tentative ou du classement sans bras.
- La politique de relance (CL40-01) et toute dépense : décisions de Lazar.

## 8. Fin de relecture

- Empreintes après relecture (04:19 UTC) : liste v41 152 sur 152 conformes, compagnons conformes ; liste v40 150 sur 150 ;
  les 526 fichiers de `v40/` et `v41/` identiques au relevé du début (`outils-cl8/empreintes-debut.txt` contre
  `empreintes-fin.txt`, `cmp` sans écart) ; aucun `__pycache__` dans les arbres relus.
- Processus : aucun processus de mes scénarios, mutations ou essais actif (`ps`) ; les commandes et petits-enfants des
  scénarios d'interruption ont été vérifiés morts. (Deux processus `sim_garde_v2.py` d'une autre relecture tournent sur la
  machine : pas les miens, non touchés.)

## 9. Fichiers produits

Sous `relecture-v41/cl8/` :
- `contre-lecture-v41-cl8.md` (ce rapport) ;
- `outils-cl8/` : `argon_factice.py` (étendu : `bareme_controle`, `controle_repond_notes`, `listes_longues`),
  `lanceur_pire.py`, `scenarios_cl8.py` (S1 à S11), `scenario_fenetre.py` et `lanceur_fenetre.py` (S12),
  `sonde_tailles.py`, `sonde_relais_relance.py` et sa sortie, `sondes_nan.py` et `sondes-nan-v41-sortie.txt`,
  `mutations_cl8.py`, `mutants/` (sorties par mutation, `mutations-premier-passage.json`, `mutations-complet.json`),
  `mutants-v28/`, `mutations-premier-passage-sortie.txt`, `mutations-complet-sortie.txt`, `essais-sortie.txt`,
  `empreintes-debut.txt`, `empreintes-fin.txt` ; `herite-cl7/` : les sorties de CL7 copiées avec ses outils (non
  produites par moi) ; `scenarios.py`, `mutations.py`, `garde_puissance.py` : outils de CL7 inchangés ;
- `simulee/` : un dossier par scénario (pièces, configurations et journal d'Argon, sorties, `rapport.json`),
  `S10-petit/`, `S10-grand/`, `S10-grand-sur-v40/`, `S12-fenetre-makedirs-manifeste/`, `S13-bras-tentative-nan/`,
  `sonde-tailles/` et `sonde-tailles-sortie.json`, `nan-v41/`, `essais-_tmp-reste-de-la-suite/` ;
- `copie/` : copies de v40 et v41 sur lesquelles tout a tourné (à supprimer à volonté) ; `diff-calcule.patch`.
