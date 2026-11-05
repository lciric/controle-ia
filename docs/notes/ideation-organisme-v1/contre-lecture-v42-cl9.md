# Contre-lecture CL9 du différentiel v41 → v42 — prise « idéation » (orchestrateur du pôle v7) et devis v7 sexies

Contre-lecteur neuf (règle R2) : Opus 5.5. Je n'ai écrit ni le code (lignée conv-audit) ni les relectures précédentes
(CL8 comprise). Relevés `date -u` : début **05:29 UTC**, fin **05:54 UTC**, le 29 octobre 2026. Aucun réseau, aucune clé,
aucun appel payant. Le seul « Argon » joué est un faux local qui consigne chaque appel : `outils-cl9/argon_factice.py`
(celui de CL8, inchangé) et `outils-cl9/argon_factice_cl9.py` (étendu : `tarif_tout`, chaque appel facturé au tarif donné,
entrée et sortie, jamais borné au plafond). Les sessions Claude sont celles du moteur simulé, mises au pire cas (coût =
plafond) par `lanceur_pire.py` (repris de CL8). Tout a tourné sur des copies (`cl9/copie/`). `pole/…` et
`demonstrations/…` désignent l'arbre `v42/orchestrateur-pole-v7/`. « Démontré » : exécuté par moi ; « à la lecture » :
non exécuté.

## Verdict

**Le code v42 : correct sur ce qu'il corrige.** Les huit constats de CL8 sont corrigés, et tous mes scénarios le
montrent. **Mais aucune des trois options du devis v7 sexies n'est lançable telle qu'écrite.**

| option du devis v7 sexies | le lanceur accepte ? | pire cas au plafond (démontré) | au taux du devis ou au barème du code (démontré) | verdict |
|---|---|---|---|---|
| **(a)** `--budget-controle-externe-usd 3.0`, externe 12,1 | **oui, à 846 caractères près** (1 199 154 ≤ 1 200 000) ; refusée sans dépense si la question réelle fait 2 000 caractères | Claude **40,00**, Argon **11,7** (contrôle 3,0 + passes 2 × 2,5 + contrôle du bras 0,2 + juge 3,5), total **51,7** ≤ 52,1, classement à trois juges | **la passe 2 d'Argon (plafond 2,5) dépasse son plafond** : 2,51 au taux du devis, 2,78 au barème haut. Course arrêtée après la passe 2 d'Argon. Claude 0,4, Argon 6,95 et 7,68, **aucun classement**, relance impossible (SORTIE existe) | **non lançable** (CL42-01) |
| **(b)** `--taille-max-pieces 650000` | **non** : la garde refuse (1 099 145 > 1 000 000), avant tout appel, rien payé | — | — | **non lançable** (CL42-02) |
| **(c)** barème d'Argon confirmé, `--taille-max-consigne-externe 1200000` | oui | Claude **40,00**, Argon **11,2**, total **51,2**, classement à trois juges | au taux du devis, le contrôle d'Argon coûte 2,73 > 2,5 : refusé, **2,73 comptés**, Claude 0, tentative non relançable. Au barème haut : 3,00 comptés, même issue | **lançable sous une condition chiffrée** : barème d'Argon ≤ ≈ 2,08 × 10⁻⁶ dollar par caractère d'entrée (≈ 8,3 dollars par million de jetons à 4 caractères par jeton), sortie comprise pour les passes (CL42-01) |

1. **Ce que la v42 corrige, démontré.** 396 essais sur 396, deux exécutions. Les douze scénarios de CL8, rejoués, donnent
   les chiffres annoncés par l'auteur. CL41-01 à 08 sont corrigés (§ 3). Sur les douze survivants de CL8, neuf sont
   maintenant tués.
2. **Constat principal neuf : CL42-01, majeur, démontré.** La garde de taille de la course se règle sur le plafond du
   **contrôle** d'Argon. Mais la passe 2 d'Argon a un plafond de 2,5 et reçoit presque la même consigne (1,10 à 1,14 million
   de caractères contre 1,20 million). Monter le contrôle à 3,0 (option a) n'est utile que si le contrôle coûte plus de 2,5.
   Or, dans ce cas, la passe 2 coûte aussi plus de 2,5. Le seul intervalle où (a) aide va de 2,085 à 2,263 × 10⁻⁶ dollar
   par caractère, et seulement avec une sortie presque nulle. Avec huit fiches réelles en sortie, au rapport sortie/entrée
   du barème du code, cet intervalle est **vide**.
3. **La borne de 12 000 caractères par fiche (CL42-04)** n'est pas une simple marge de calcul. Elle change le protocole de
   deux façons : la consigne des proposeurs dit maintenant la borne, et une fiche plus longue est refusée entière. Il n'y
   a pas de troncature : les juges voient exactement la fiche écrite. La borne vaut aussi pour les témoins. C'est à dire
   et à faire trancher par Lazar.
4. **Défauts réintroduits.** J'en ai réintroduit 49. 39 sont tués et 10 survivent à la suite entière : M28, N28 et V27
   (déjà déclarés incertain, équivalent et presque équivalent par CL8), plus 7 sur le code neuf (W03, W07, W28, W30, W35,
   W35b, W36). Quatre de ces sept sont de vrais trous d'essais (§ 7).

**Avant le lancement.** Lazar choisit (c), session-depot confirme le barème d'Argon (sans dépense), et la condition porte
aussi sur les passes, sortie comprise. Ou bien (a) corrigé : plafond des passes d'Argon relevé avec le contrôle (au barème
haut du code, la passe 2 coûte ≈ 3,2 ; Argon ≈ 13,5, total ≈ 53,5, une dépense neuve). Et dans tous les cas, CL42-04 est
dit au devis.

## 1. Comptes vérifiés

- **Empreintes** (05:29) : `sha256sum -c EMPREINTES-orchestrateur-pole-v7-v42.txt` → **154 sur 154 conformes**. Les
  compagnons de la liste et du LISEZMOI v42 sont conformes. Liste v42 : `637028fc…` ; LISEZMOI : `78df10a6…` ; ce sont bien
  les empreintes citées par le devis. Liste v41 : 152 sur 152. Devis v7 sexies : `bab9d04b923a6162…` (conforme à l'annonce).
  Relevé de début de 534 fichiers : `outils-cl9/empreintes-debut.txt`.
- **Différentiel** : `diff -rq v41 v42` → changent `pole/ideation.py`, `demonstrations/ideation_v1.py`,
  `essais/test_v7_ideation.py` ; s'ajoutent la liste d'empreintes et le LISEZMOI v42. Le patch fourni, appliqué à une
  copie de la v41 (`patch -p5`), redonne exactement la v42 (démontré, `diff -r` vide).
- **Essais** : `env -i PATH=… HOME=… python3 -B -m unittest discover -s essais -t . -p 'test_*.py'`, deux exécutions
  simultanées sur deux copies : **Ran 396 tests in 223,1 s, OK** et **Ran 396 tests in 221,7 s, OK**, code 0
  (`outils-cl9/essais-sortie-1.txt`, `-2.txt`). Les 16 essais neufs sont bien `TestV42` dans `test_v7_ideation`. Aucun
  processus survivant (`ps`). La suite laisse 15 dossiers temporaires sous `essais/_tmp` (4 Mo, sans gravité ; je les ai
  retirés des copies).

## 2. Scénarios de CL8 rejoués sur la v42 (démontré)

Outils : `outils-cl9/scenarios_cl9.py` (S1 à S11 de CL8, inchangés sur le fond, plus les D-*), `scenario_fenetre.py`
(S12) et `sonde_repli_silencieux.py` (S14). Sorties : `simulee/<scénario>/rapport.json`.

| scénario | v42 (démontré) | annonce de l'auteur |
|---|---|---|
| **S1** pire cas, réglages du devis v7 quinquies, pièces de 2 000 | code 0 ; Claude **40,00** (8 sessions) ; Argon course 7,5 ; bras 3,7 (contrôle **41 caractères** à 0,2 + juge 3,5) ; **Argon 11,2** ; classement à trois juges ; contrôle d'Argon **103 167** caractères | concorde |
| **S2** Argon « KO » au contrôle (0,15) ; contrôles Claude 0,2, 0,01, 0 | **Claude 0** dans les trois cas ; tentatives 1 et 2 relançables, la troisième non (« 3 tentatives », 11,65 > 11,6) ; quatrième refusée sans rappeler Argon. Argon cassé sans coût lisible : 2,5 comptés, Claude 0, non relançable | concorde |
| S3 SIGTERM pendant le contrôle d'Argon | code 2 ; processus morts ; tentative : **Claude 0** (v41 : 0,02), externe 2,5, non relançable (13,7 > 11,6) | — |
| S3b SIGTERM pendant le contrôle du bras | code 2 ; processus morts ; `bras-tentative-1.json` 0,2, relançable | — |
| S4, S4b SIGTERM, SIGHUP pendant la passe d'Argon | code 2 ; processus morts ; externe 5,0 ; Claude 0,02 | — |
| S5 taille du contrôle | contrôle 139 167 ≥ passe 2 réelle (76 820 ; 42 623). Remarque : avec des champs de 1 500 et de 3 000, les fiches de l'Argon factice dépassent 12 000 et sont **toutes refusées**, si bien que la passe 2 ne porte plus de grosses fiches | — |
| **S5b** listes de 60 éléments | fiches d'Argon refusées ; passe 2 réelle 42 623 ≤ contrôle 139 167 ; (a) casse sous le contrôle : refus au contrôle d'Argon, **Claude 0**, 2,5 comptés ; (b) aucune taille entre contrôle et passe 2 : course complète | concorde |
| S6 consigne du juge (pièce de juge de 100 000) | consigne du juge 243 781 ; contrôle du bras 41 ; bras code 0 | — |
| S7 refus avant contrôle | `--max-tours 3`, SORTIE existante, NaN, +∞ : refus, aucun dossier de contrôle | — |
| S8 SIGTERM au bras après envoi | code 2 ; processus morts ; manifeste du bras 3,7 ; `classement-sans-bras.json` écrit ; relance refusée | — |
| S9, S9b | inchangés par rapport à CL8 : bras à 0,1 sans l'option, Argon 11,1 ; refus du cœur après contrôles : tentative scellée (Claude 1,0, externe 2,5), non relançable | — |
| **S10** petit et grand (consigne du juge 246 478) au barème haut | contrôle court 41 caractères à 0,0001 et 0,100 ; juge au plafond 3,5 ; **classement à trois juges** dans les deux barèmes ; Argon 11,0 et 11,1 | concorde |
| **S11** contrôle du bras qui rend des notes | n'a plus d'objet : l'Argon factice en mode « notes » plante sur la consigne courte (plafond 0,2 compté, tentative relançable) ; puis le bras normal écrit le classement à trois juges | concorde |
| **S12** interruption entre SORTIE et manifeste de départ | essai 1 : code 2, aucune SORTIE, tentative-1 relançable ; essai 2 : **code 0** ; aucun dossier `…depart-en-cours…` laissé | concorde |
| `sonde_tailles.py` (CL8) | contrôle aux réglages du devis **1 199 154** (2,725 au taux du devis ; 2,998 au barème haut) ; maximum 1 599 149 ; S1 103 151 ; consigne du juge au maximum du gabarit borné 1 377 526 | concorde |
| `sondes_nan.py` (CL8) | **0 acceptation fautive** ; sortie identique à celle de la v41 | — |
| `sonde_relais_relance.py` (CL8) | motif « relais gardé (hypothèse) : 36,6 < 37 ; relais relancé à neuf (devis, point 4) : 37,0 ≥ 37,0, la garde du relais accepterait » | concorde |

## 3. CL41-01 à 08

| constat | verdict | preuve |
|---|---|---|
| **CL41-01** contrôle du bras sous 0,2 | **corrigé, avec deux effets neufs** (CL42-01, CL42-05) | contrôle court de 41 caractères (S1, S6, S10) ; garde sans dépense, côté course (D-base et D-b : `refus-taille-1.json` scellé, ni Argon ni Claude appelés, pas de SORTIE) et côté bras (essai ; W02 et W29 tués) ; `--budget-externe-usd` transmis au bras (W09 et W10 tués) ; classement « sans juge externe » écrit dès qu'une tentative est non relançable, payée ou non jouée (W11, W12, W13, W33 tués). Restes : W07 et W30 survivent (§ 7) ; un refus de taille au bras n'écrit aucun classement ; un échec du classement de repli est silencieux (CL42-06) |
| **CL41-02** contrôle d'Argon ≈ 1,46 million | **corrigé pour la taille ; change le protocole** (CL42-04) | 1 199 154 (sonde) ; 1 199 146 avec mes fichiers ; W14 à W18 et W34 tués ; tailles écrites au manifeste de départ et au journal. Le coût reste au-dessus de 2,5 au taux du devis, d'où les options du devis (§ 4) |
| **CL41-03** contrôle qui finit par la vraie tâche | **corrigé** (reste à vérifier sur Argon réel) | ce que reçoit la commande finit par « Fin du matériau. Réponds exactement OK, sans rien d'autre. » ; matériau entre délimiteurs (W19, W20 tués) |
| **CL41-04** message « avant tout envoi » faux | **corrigé** | le contrôle est court, le message redevient vrai. Le verrou du contrôle non court n'est atteignable qu'en essai, puisque la production envoie toujours un contrôle court (W23, W24 tués) |
| **CL41-05** relais gardé ou relancé à neuf | **corrigé** | sonde : les deux hypothèses sont écrites au motif et au champ `relance_relais_relance_a_neuf` (W25 tué) |
| **CL41-06** SORTIE sans manifeste de départ | **corrigé** | S12 ; W26 et W27 tués. Restes : W28 (course concurrente, déclarée non traitée, survit). SORTIE est maintenant créée en mode **0700** par `mkdtemp`, contre 0755 avant (`stat`, S1) : sans gravité si un seul compte lit |
| **CL41-07** Claude contrôlé avant Argon | **corrigé** | S2, S3, S5b (a), D-c : Claude 0 quand Argon échoue au contrôle (W21 tué) |
| **CL41-08** un essai par trou | **corrigé pour les neuf trous** | N03, N04, N07, N08, N13, V12, V20, V34, V36 tués (§ 7). M28, N28 et V27 survivent, comme l'auteur l'annonce |

## 4. Les options du devis v7 sexies, aux tailles du devis (démontré)

Scénarios `D-<option>-<tarif>` (`scenarios_cl9.py`). Réglages : pièce de 750 000 caractères, matériau de 350 000,
question de 19 caractères, huit fiches, seconde passe, Argon proposeur et juge, défauts du lanceur pour le reste. Course
puis bras. Les sessions Claude sont au plafond. Trois tarifs pour Argon :
- « plafond » : chaque session coûte son plafond (le pire cas du devis) ;
- « devis » : 2,5 dollars pour 1,1 million de caractères d'entrée (le taux que le devis suppose) ;
- « haut » : barème le plus haut du code, 10 et 50 dollars par million de jetons d'entrée et de sortie, 4 caractères par
  jeton.

Le faux Argon ne borne jamais son coût au plafond. Le noyau compte le coût déclaré, même au-dessus du plafond.

| scénario | contrôle d'Argon | passe 1 | passe 2 | Claude | Argon | issue |
|---|---|---|---|---|---|---|
| D-base-plafond (devis v7 quinquies) | **refus de garde** (1 199 146 > 1 000 000), avant tout appel | — | — | 0 | 0 | `refus-taille-1.json` scellé ; pas de SORTIE |
| **D-a-plafond** | 1 199 146 car., 3,0 | 752 491 car., 2,5 | 1 104 533 car., 2,5 | **40,00** | **11,7** (dont bras 3,7) | code 0 ; classement à trois juges ; sommes du code : externe 11,7 ≤ 12,1 |
| **D-a-devis** | 2,725 (≤ 3,0) | 1,710 | **2,510 > 2,5 : `budget_depasse`** | 0,4 | **6,95** | code 2 après la passe 2 d'Argon ; **aucun classement** ; SORTIE écrite (manifeste de fin) : relance refusée « SORTIE existe » |
| **D-a-haut** | 2,998 (≤ 3,0) | 1,902 | **2,782 > 2,5** | 0,4 | **7,68** | même issue |
| D-a-plafond-q2000 (question de 2 000 caractères) | **refus de garde** (1 201 127 > 1 200 000) | — | — | 0 | 0 | refus sans dépense |
| **D-b-plafond** | **refus de garde** (1 099 145 > 1 000 000) | — | — | 0 | 0 | refus sans dépense |
| **D-c-plafond** | 2,5 | 2,5 | 2,5 | **40,00** | **11,2** | code 0 ; classement à trois juges ; la garde du bras vaut **1 200 000**, « donnée à la course » |
| D-c-devis | **2,725 > 2,5 : refusé** | — | — | 0 | **2,73** | tentative scellée, non relançable (13,93 > 11,6) |
| D-c-haut | **2,998 > 2,5 : refusé** | — | — | 0 | **3,00** | même issue (14,20 > 11,6) |

**Les chiffres du devis contre le code.**
- Ce qui concorde : 1 199 154 caractères ; 2,73 au taux du devis ; 3,00 au barème haut ; garde par défaut 1 000 000 à 2,5,
  1 200 000 à 3,0 et 1 400 000 pour le juge ; somme externe de (a) 11,7, marge 0,4, total 52,1 ; juge au plus ≈ 1,38 million ;
  Argon d'abord ; contrôle du bras court ; classement « sans juge externe ».
- Ce qui ne concorde pas :
  - (b) « pour rester sous 2,5 » : c'est vrai au taux du devis (2,498), mais la garde du code compte au prix prudent
    (2,5 × 10⁻⁶ par caractère). Elle refuse donc (b) (CL42-02).
  - (a) « recommandé » : la passe 2 n'est pas couverte (CL42-01).
  - Point 3 du devis, « 1 400 000 pour le juge » : c'est faux sous (c), où le bras reprend 1 200 000 (CL42-05).
  - Point 6, « aucune course payée ne reste sans classement » : c'est faux en D-a-devis et D-a-haut (la course elle-même
    s'arrête après dépense). C'est faux aussi après un refus de taille au bras, et quand le classement de repli échoue
    (CL42-06).
- Les 1 199 154 caractères valent pour une question de 19 caractères et une seule pièce. Sous (a), la marge est de
  **846 caractères** : la question réelle et les noms des pièces décident (D-a-plafond-q2000).

## 5. La borne de 12 000 caractères par fiche (démontré, `outils-cl9/sonde_fiche_12000.py`)

- **Où elle s'applique.** Dans `valider_fiche_ideation`, après le caviardage et le retrait des espaces. On mesure la fiche
  en JSON indenté à 1, dans une liste, échappements compris. La règle vaut pour toutes les fiches : passe 1 et passe 2,
  proposeurs Claude et Argon, et **témoins** (`charger_temoins` appelle la même fonction).
- **Ce qui arrive à une fiche plus longue.** Elle est **refusée entière**, avec le motif « fiche trop longue : N caractères
  servis > 12000 » dans `fiches-refusees.json`. Les autres fiches de la même réponse sont gardées. **Aucune troncature** :
  une fiche acceptée est identique au brut, hors champs internes et hors retrait des espaces de bord (règle ancienne).
  **Les juges voient donc la fiche écrite.** Un témoin trop long fait refuser la course dans `verifier_reglages`, avant
  tout appel (« témoin verbeux » de 12 textes de 1 100 caractères : 14 061 caractères, refusé).
- **Où elle mord.**
  - Douze textes de 928 caractères en moyenne passent (11 997). Douze textes de 950 sont refusés (12 261).
  - Trois champs à 3 000 passent (9 684). **Quatre champs à 3 000 sont refusés (12 683)**, alors que chaque champ respecte
    sa propre borne de 3 000.
  - Les guillemets et les retours à la ligne comptent double. 6 000 caractères de texte qui en contiennent beaucoup
    donnent 9 681 caractères servis.
  - Les fiches réelles relevées par CL8 (3 000 à 5 000 caractères) passent largement.
- **Cela change-t-il la mesure ?** Oui, de deux façons.
  1. La **consigne des proposeurs change** : « Bornes (une fiche qui les dépasse est refusée) : … 12000 caractères au plus
     par fiche (JSON compris) ». Le traitement donné aux proposeurs n'est donc plus le même que dans les devis antérieurs.
  2. La **règle d'admission change** : l'ensemble jugé, les taux de refus par proposeur et donc le classement peuvent
     changer. Un proposeur prolixe (Fable en passe 2, par exemple) perd des fiches entières.

  Les juges, eux, ne voient pas une fiche différente de celle qui a été écrite.
- **Faut-il le sceller et le dire ?** Je n'ai trouvé aucun préenregistrement de la course d'idéation dans `prereg/` du
  dépôt (la course « propose et classe seulement ») : ce n'est donc pas un écart à R1. En revanche, c'est un **changement
  du protocole de la course**. Il porte sur la consigne et l'admission, témoins compris. Il est consigné au manifeste de
  départ (`taille_max_fiche_servie`) et dit dans les « restes » du LISEZMOI, mais le devis v7 sexies le présente comme une
  règle de calcul de marge « à confirmer ». Il faut le dire comme un changement de protocole, au devis, et le faire
  trancher par Lazar.
  - Option sans changement de protocole : garder 12 000 comme marge du contrôle **sans refuser**. Le reste « passe 2 plus
    grosse que le contrôle » redevient alors un reste déclaré, borné par 8 × 44 163 au pire (fiche de la v41, listes bornées).
  - La phrase « 12 000 caractères au plus par fiche » de la consigne n'est gardée par aucun essai (W35b survit).

## 6. Les trois essais de la v41 modifiés

| essai | modification | affaiblit-il ce qu'il vérifiait ? |
|---|---|---|
| `test_controle_a_la_taille_reelle_de_la_passe_2_et_ordre_d_argon` | fiche maximale = 12 000 (au lieu de « > 13 × 3 000 ») ; la grosse fiche d'Argon passe de quatre à trois champs de 3 000 | **Localement oui** : la passe 2 « réelle » n'est plus éprouvée près de la borne (fiche de 9 684), et l'écart couvre 8 × 2 300 caractères. **C'est compensé** par `test_cl41_02_fiche_bornee_et_marge_realiste`, qui joue huit fiches exactement à 12 000. W17 et W18 sont tués par les deux essais. Pas de perte nette |
| `test_controle_du_bras_porte_la_consigne_du_juge` | inversé : le contrôle reçu vaut exactement 41 caractères, et la consigne du juge n'est envoyée qu'au juge | Non : c'est le choix (B) voulu. L'essai vérifie toujours que la consigne du juge reçue est la consigne en attente. W22 (retour au contrôle long) est tué |
| `test_relancable_calcule_avec_un_controle_claude_paye` | Argon « OK » à 0,15 d'abord ; l'échec vient du second contrôle Claude (« KO », payé) | Non : mêmes sommes (40,02 ; 40,40), coût externe 0,15 vérifié, relance refusée sans rappeler Argon, borne à trois. Le cas v41 (Argon « KO » après les contrôles Claude) n'existe plus ; le cas neuf (Argon « KO » d'abord) est couvert par `test_cl41_07` (W21 tué) |

## 7. Défauts réintroduits

Outil : `outils-cl9/mutations_cl9.py` (moteur de CL7 et CL8). Une copie neuve par défaut. Chaque remplacement est vérifié
unique avant le jeu. Premier passage sur `test_adaptateurs` et `test_v7_ideation` (ou sur les six modules du juge apparié
pour N28). Chaque survivant est confirmé sur la suite entière : 396 essais, OK, 281 à 293 secondes chacun.

| groupe | réintroduits | tués | survivants à la suite entière |
|---|---|---|---|
| 12 survivants de CL8, réexprimés sur la v42 | 12 | **9** : N03, N04, N07, N08, N13, V12, V20, V34, V36 | M28 (reconstitution incertaine), N28 (équivalent), V27 (presque équivalent) |
| CL41-01 garde, plafond externe, classement de repli (W01, W02, W04 à W13, W29, W30, W32, W33, W36) | 17 | 14 | **W07** (origine « option » jamais écrite par le lanceur : la chaîne lanceur → manifeste → bras n'est pas essayée de bout en bout ; l'essai du bras injecte la valeur à la main) ; **W30** (NaN admis au bras : l'essai NaN est vide, car il échoue sur « le bras a déjà été joué » avant d'atteindre la vérification) ; **W36** (classement de repli réécrit : aucun essai ne fait deux replis) |
| CL41-01 garde à l'égalité (W03) | 1 | 0 | **W03** (`>` devient `>=` : borne non éprouvée à l'égalité ; sans effet pratique) |
| CL41-02 bornes de fiche, marge (W14 à W18, W34, W35, W35b) | 8 | 6 | **W35** (presque équivalent : mon défaut laissait la phrase vérifiée) ; **W35b** (la borne de 12 000 retirée de la consigne des proposeurs : non vue) |
| CL41-03, 04, 05, 07 (W19 à W25, W31) | 8 | 8 | — |
| CL41-06 (W26 à W28) | 3 | 2 | **W28** (seconde vérification de SORTIE retirée : course concurrente, déclarée non traitée) |
| **total** | **49** | **39** | **10** |

Sorties : `outils-cl9/mutants/mutations-premier-passage.json`, `mutations-complet.json` et une sortie par défaut ;
résumés dans `outils-cl9/mutations-premier-passage-sortie.txt` et `mutations-complet-sortie.txt`. L'auteur annonçait 25
tués sur 25. Je confirme ses neuf trous et ses défauts du même type. Mes défauts W03, W07, W28, W30, W35b et W36 ne
figurent pas dans sa liste.

## 8. Constats neufs

### CL42-01 — majeur (bloquant pour l'option (a), défaut sous 48 heures du devis) — La garde de taille de la course se règle sur le plafond du contrôle d'Argon ; la passe 2 d'Argon, plafond 2,5, n'est pas couverte

**Endroit.**
- Lanceur : `taille_max = idn.taille_max_consigne_par_defaut(args.budget_controle_externe_usd)`.
- Cœur : `verifier_reglages`, où la garde porte sur la seule consigne de contrôle.
- Budgets : `BUDGET_EXTERNE_PROPOSEUR = 2.5` pour chaque passe d'Argon.

**Défaut** (démontré, D-a-devis et D-a-haut, § 4). La consigne de passe 2 réelle fait 1,10 à 1,14 million de caractères,
contre 1,20 million pour le contrôle. Avec (a), le contrôle est couvert jusqu'à 3,0, mais pas la passe 2.
- Au taux du devis, le contrôle passe (2,73) et la passe 2 coûte 2,51 > 2,5. Le statut est `budget_depasse` et la course
  s'arrête.
- Bilan : Claude 0,4, Argon 6,95 (barème haut : 7,68), aucun classement, relance refusée parce que SORTIE existe.

L'argent reste sous les plafonds totaux, mais la course est perdue. Calcul de l'intervalle utile :
- (a) n'aide que si le contrôle coûte entre 2,5 et 3,0, soit un prix d'entrée compris entre 2,085 et 2,502 × 10⁻⁶ dollar
  par caractère ;
- la passe 2 tient dans 2,5 jusqu'à 2,263 × 10⁻⁶ avec une sortie presque nulle ;
- avec huit fiches réelles en sortie (≈ 32 000 caractères) au rapport sortie/entrée du barème du code (cinq fois), la
  passe 2 ne tient que jusqu'à ≈ 1,93 × 10⁻⁶. **L'intervalle utile est vide.**

Au barème haut du code, la passe 2 coûte ≈ 2,84 en entrée et ≈ 0,4 en sortie, soit ≈ 3,2. Le défaut ne se voit qu'avec un
faux Argon qui facture au tarif : au pire cas « plafond » (D-a-plafond), tout passe.

**Correction.**
- Code : régler la taille par défaut sur le **plus petit plafond** des sessions d'Argon qui reçoivent cette consigne
  (contrôle et passe 2), avec une provision pour la sortie, ou garder aussi la passe 2 contre son propre plafond. Essai :
  `--budget-controle-externe-usd 3.0` seul doit être refusé sans dépense.
- Devis : retirer (a) ou la compléter par `--budget "proposeur_ideation|gemini-argon=…"`. Au barème haut, la passe 2
  demande ≈ 3,3, d'où Argon ≈ 13,5 et total ≈ 53,5 : une dépense neuve, décision de Lazar. Mieux : (c), après
  confirmation du barème, sans dépense.
- Enfin, la condition de (c) doit couvrir les passes, sortie comprise, pas seulement le contrôle.

### CL42-02 — majeur pour le devis, sans risque d'argent — L'option (b) est refusée par le code

**Défaut** (démontré, D-b-plafond). Avec des pièces de 650 000, la consigne de contrôle fait 1 099 145 caractères, au-delà
de la garde par défaut (1 000 000). Le refus tombe avant tout appel, rien n'est payé. Le devis calcule (b) au taux du devis
(2,498 < 2,5) ; la garde, elle, compte au prix prudent du code. À noter aussi : `--taille-max-pieces` borne chaque lot
séparément (pièces, matériau, pièces de juge), pas leur somme.

**Correction.** Retirer (b), ou la chiffrer au prix de la garde : pièces ≤ ≈ 550 000 avec le matériau de 350 000, ou
`--taille-max-consigne-externe` donné avec elle (ce qui revient à (c)).

### CL42-03 — mineur — La marge de (a) est de 846 caractères ; les 1 199 154 du devis valent pour une question de 19 caractères

**Défaut** (démontré, D-a-plafond-q2000). Une question de 2 000 caractères porte la consigne à 1 201 127 caractères.
Résultat : refus sans dépense. Le nombre et les noms des pièces jouent aussi, par leurs en-têtes « ## Pièce : … ».

**Correction.** Avant le GO, mesurer la consigne de contrôle avec les vrais fichiers. Le refus ne coûte rien, mais il
bloque le lancement prévu.

### CL42-04 — majeur (protocole ; à dire au devis, décision de Lazar) — La borne de 12 000 caractères par fiche change la consigne des proposeurs et la règle d'admission

Voir § 5 (démontré). Il n'y a ni troncature ni écart entre la fiche écrite et la fiche jugée. Mais la consigne change, une
fiche plus longue est refusée entière, et les témoins sont soumis à la même règle. Quatre champs à 3 000 sont refusés,
alors que chacun respecte sa propre borne. La phrase de la consigne qui dit la borne n'est gardée par aucun essai (W35b).

**Correction.** Le dire au devis comme un changement de protocole, et faire choisir Lazar : (i) garder la règle, la
nommer, rapporter les refus pour taille par proposeur et ajouter un essai sur la phrase de la consigne ; ou (ii) garder 12
000 comme marge du contrôle seulement, sans refuser.

### CL42-05 — mineur — Garde du bras : sous (c), elle reprend la taille donnée à la course ; un refus de taille au bras n'écrit aucun classement

**Défaut** (démontré pour l'origine, journal du bras D-c-plafond : 1 200 000, « donnée à la course » ; l'effet est à la
lecture et dans l'essai de l'auteur, à 200 000).
- Sous (c), une consigne de juge entre 1,2 et 1,4 million est refusée au bras. Le devis dit 1,4 million (point 3).
- Le refus de taille au bras ne compte aucune tentative et n'écrit aucun classement sans bras. La seule issue est de
  relever la taille.
- La chaîne lanceur → manifeste → bras n'est pas essayée (W07 survit).

**Correction.** Une option propre au bras, ou bien dire au devis que la valeur de la course vaut pour le juge. Écrire
aussi le classement sans bras si Lazar renonce au juge externe. Ajouter un essai de bout en bout par le lanceur.

### CL42-06 — mineur (règle R5) — L'échec du classement de repli est silencieux

**Endroit.** `sans_bras_non_relancable` rattrape toute exception et l'écrit dans `journal["classement_sans_bras_impossible"]`.
Mais le journal a déjà été scellé (`manifeste-bras-non-joue-N.json` ou `bras-tentative-N.json`) et n'est plus réécrit.

**Défaut** (démontré, S14, `sonde_repli_silencieux.py` : panne simulée de `_classer` à la troisième tentative non jouée).
Le code de sortie est 2. Le message dit « plus de relance sans un mot de Lazar ». Il n'y a ni `classement-sans-bras.json`,
ni **aucun fichier ni message qui dise l'échec du repli**. Le même chemin avale le refus d'écrasement si un classement sans
bras existe déjà (voir W36).

**Correction.** Ajouter le motif d'échec du repli au message de l'exception levée et le sceller (fichier
`classement-sans-bras-impossible-N.json`). Essai : `_classer` qui lève.

### CL42-07 — mineur — Essais : sept survivants sur le code neuf

Voir § 7. Les quatre vrais trous :
- W30 : l'essai NaN est vide ; le code est juste, mais rien ne le garde ;
- W07 : chaîne de l'origine de la taille ;
- W35b : phrase de la borne dans la consigne ;
- W36 : second repli.

Les trois autres : W03 (égalité), W28 (course concurrente, déclarée) et W35 (presque équivalent).

**Correction.** Un essai par trou :
- NaN au bras sur une SORTIE fraîche ;
- `--taille-max-consigne-externe` donné au lanceur, puis bras sans l'option ;
- `assertIn("12000 caractères au plus par fiche", …)` ;
- deux tentatives non relançables successives.

**Compte des constats neufs.** Aucun bloquant de sécurité ni de dépense hors plafond total. Trois majeurs : CL42-01
(démontré ; bloquant pour l'option recommandée du devis), CL42-02 (démontré ; option non lançable) et CL42-04 (protocole,
décision de Lazar). Quatre mineurs : CL42-03, 05, 06 et 07.

## 9. Ce que je n'ai pas pu vérifier

- Le barème réel d'Argon, sa limite de taille (en caractères, en octets ou en jetons) et sa réaction à la consigne de
  contrôle neuve (délimiteurs, phrase finale).
- La taille réelle de la question, des pièces, du matériau et des fiches. La garde compte des caractères ; la sortie
  d'Argon (passes, juge) n'est pas comptée par la garde.
- Les sessions Claude réelles et le relais réel. Un second signal pendant l'écriture d'une tentative ou d'un classement de
  repli.
- La course concurrente sur une même SORTIE (W28, déclarée par l'auteur).
- L'effet de la borne de 12 000 sur des proposeurs réels (taux de refus).
- Toute décision de dépense et la politique de relance (CL40-01) : décisions de Lazar.

## 10. Fin de relecture

- **Empreintes** après relecture (05:52 UTC) : liste v42, 154 sur 154 conformes. Les 534 fichiers de `v41/` et `v42/` sont
  identiques au relevé du début (`cmp` entre `outils-cl9/empreintes-debut.txt` et `empreintes-fin.txt`, sans écart).
  Aucun `__pycache__` dans les arbres relus.
- **Processus** : aucun processus de mes essais, scénarios ou défauts n'est actif (`ps`). Les commandes et petits-enfants
  des scénarios d'interruption sont morts (S3, S3b, S4, S4b, S8 : `vivants_apres` faux partout).
- Aucun dépôt git créé. Aucun réseau.

## 11. Fichiers produits

Sous `relecture-v42/cl9/` :
- `contre-lecture-v42-cl9.md` (ce rapport) et son compagnon `.sha256`.
- `outils-cl9/` :
  - outils neufs : `argon_factice_cl9.py`, `scenarios_cl9.py` (D-*), `scenarios_cl9_options.py.part`,
    `sonde_fiche_12000.py`, `sonde_repli_silencieux.py`, `mutations_cl9.py` ;
  - outils de CL8 copiés sans modification : `argon_factice.py`, `lanceur_pire.py`, `scenarios_cl8.py`,
    `scenario_fenetre.py`, `lanceur_fenetre.py`, `sonde_tailles.py`, `sonde_relais_relance.py`, `sondes_nan.py`,
    `mutations_cl8.py`, `mutations.py`, `scenarios.py`, `garde_puissance.py` ;
  - sorties : `essais-sortie-1.txt`, `essais-sortie-2.txt`, `empreintes-debut.txt`, `empreintes-fin.txt`,
    `mutations-premier-passage-sortie.txt`, `mutations-complet-sortie.txt`, `mutants/` (une sortie par défaut, deux
    fichiers JSON de résultats).
- `simulee/` :
  - un dossier par scénario : S1 à S11, `S10-petit`, `S10-grand`, `S12-fenetre`, `S14-repli-silencieux`, et D-base, D-a,
    D-b, D-c sous les trois tarifs (pièces, configurations, journal d'Argon, sorties, `rapport.json`) ;
  - sondes : `sonde-tailles-sortie.json`, `sonde-relais-relance-sortie.json`, `sondes-nan-v42-sortie.txt`,
    `sonde-fiche-12000-sortie.json`.
- `copie/` : copies de la v41, de la v42 (deux) et de la v41 patchée, sur lesquelles tout a tourné (à supprimer à volonté).
