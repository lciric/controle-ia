# Contre-lecture CL7 du différentiel v39 → v40 — prise « idéation », porte PACE, garde appariée (orchestrateur du pôle v7)

Contre-lecteur neuf (règle R2) : Opus 5.5. Je n'ai écrit ni le code (lignée conv-audit, Fable 5.1) ni les relectures
précédentes (CL6 comprise). Relevés `date -u` : début **02:20 UTC**, fin **02:53 UTC**, le 29 octobre 2026. Aucun
réseau, aucune clé, aucun appel payant. Le seul « Argon » joué est `outils-cl7/argon_factice.py`, local, qui consigne
chaque appel dans un journal ; les sessions Claude sont celles du moteur simulé, mises « au pire cas » (coût = plafond) par
`outils-cl7/lanceur_pire.py`. `pole/…`, `demonstrations/…`, `essais/…` désignent l'arbre `v40/orchestrateur-pole-v7/` ;
tout a été exécuté sur des copies (`cl7/copie-essais/`). « Démontré » : exécuté par moi ; « à la lecture » : non exécuté.

## Verdict : **lançable** aux réglages du devis v7 quinquies (aucun bloquant de lancement) ; **aucune relance** avant une décision de Lazar (CL40-01) et deux corrections courtes (CL40-02, CL40-03)

1. **Premier lancement, démontré (S1).** Aux défauts du lanceur (= devis v7 quinquies), tout au plafond côté Claude et
   côté Argon, seconde passe avec matériau attesté : le lanceur accepte ; la course dépense 40,00 côté Claude et 7,5 chez
   Argon ; le bras, joué ensuite, dépense 3,7 ; **Argon au total 11,2 ≤ 11,6**, classement à trois juges écrit. Les
   chiffres du devis concordent avec le code (somme Claude 40,0 ; somme externe 11,2 contrôle du bras compris ; 51,6).
   CL39-01 est corrigé.
2. **Pas de bloquant de lancement**, mais **trois majeurs** (démontrés), qui portent tous sur ce qui suit un échec :
   - **CL40-01** : aux réglages du devis, **aucune relance n'est possible** après un contrôle payé qui échoue (la somme
     Claude vaut exactement 40,0 ; tout coût de contrôle imputé la fait passer au-dessus) ; la tentative scellée dit
     pourtant « relançable », et le devis promet « trois tentatives au plus ». L'essai de la v40 ne passe que parce que le
     contrôle Claude simulé coûte 0 ;
   - **CL40-02** : un contrôle **interrompu** (SIGTERM, SIGINT, exception de l'adaptateur), dans la course ou dans le bras,
     est scellé **à 0 dollar** au lieu de son plafond (2,5 chez Argon), contrairement au devis (point 3) et au message
     du lanceur ;
   - **CL40-03** : un refus du cœur **après** les contrôles payés n'est consigné nulle part, et la relance n'est pas
     bornée ; le lanceur et le cœur ne comptent pas le même contrôle du bras dès que `--budget-controle-usd` < 0,2
     (hors réglages du devis : chemin démontré, Argon payé deux fois sans trace).
3. **CL39-01 à 12** : corrigés **01, 03, 04, 07, 08, 10, 11 (sauf des restes d'écrits), 12** ; **en partie 02** (CL40-01,
   CL40-03), **05** (contrôles : CL40-02), **06** (marge sous-estimée, consigne du juge non éprouvée : CL40-04) et **09**
   (liste de CL6 complète ; restes, et même famille dans le chemin de l'argent : CL40-05, CL40-06).
4. **Défauts réintroduits** : 58 (les 21 survivantes de CL6 reconstituées, 37 neufs sur ce qu'ajoute la v40).
   **48 tuées, 10 survivent à la suite entière** (§ 6). Des 21 survivantes de CL6, **19 sont tuées** ;
   M07 survit (annoncée tuée par le LISEZMOI v40), M28 survit (reconstitution incertaine).
5. **Suite d'essais de la v40** : **363 essais, 363 réussis**, 214 s, code 0 (annoncé 363 = 340 + 23 : exact).
6. **Porte PACE** : la garde a désormais un **cas sain et un artefact qui se séparent** (bruit 0,02, 600 unités : témoin
   honnête validé 99 %, tricheur 0 %, mes graines) ; dans le monde par défaut, la garde reste **sans puissance** aux
   tailles du pilote (honnête 1 à 3 %), ce que la v40 rapporte désormais honnêtement.

**Avant toute relance** : CL40-01 (décision de Lazar), CL40-02, CL40-03. Le reste peut suivre.

## 1. Comptes vérifiés

- **Empreintes** : `sha256sum -c EMPREINTES-orchestrateur-pole-v7-v40.txt` → **150 sur 150 conformes** (02:21) ;
  compagnons de la liste v40 et du LISEZMOI v40 conformes. Rien de créé ni modifié dans `v39/` ou `v40/` (contrôle de fin
  au § 8).
- **Différentiel** (`diff -rq v39 v40`) : changent `pole/ideation.py`, `pole/pari_apparie.py`, `pole/porte_pace.py`,
  `demonstrations/ideation_v1.py`, `demonstrations/porte_pace_v1.py` et quatre modules d'essais ; s'ajoutent la liste
  d'empreintes et le LISEZMOI v40. Le patch fourni correspond.
- **Essais** (point 7) : `env -i … python3 -B -m unittest discover -s essais -t . -p 'test_*.py'` sur une copie :
  **Ran 363 tests in 213,98 s, OK**, code 0 (`outils-cl7/essais-sortie.txt`). Les 23 essais neufs sont bien ceux du
  différentiel (TestV40 : 7 ; TestValeursNonFiniesV40 : 9 ; GardeV40 : 4 ; MutationsV40 : 3).
- **Ordre des modules (CL39-12)** : `test_v7_ideation` puis `test_adaptateurs` → 65 essais, OK (démontré).
- **Démonstration PACE** (graine 20261029, n_dev 40, 120, 400 ; 67 s) : les chiffres de CL6 sont reproduits (sous la
  nulle à 120 : PACE 32,0 % de suites avec une fausse validation contre 0,5 % ; témoin à 40 : 90 % contre 50 %) ;
  puissance de la garde : honnête validé 0,0 % (40), 1,0 % (120), 3,0 % (400) ; tricheur refusé 100 %
  (`simulee/porte-pace-demo-v40-sortie.txt`).

## 2. CL39-01 en particulier : réglages du devis v7 quinquies, pire cas

Scénario S1 (`outils-cl7/scenarios.py S1-devis-pire-cas`, sortie `simulee/S1-devis-pire-cas/rapport.json`) : défauts du
lanceur, seconde passe avec matériau et attestation scellée, juge externe Argon ; chaque session Claude rend son plafond,
chaque appel d'Argon rend `PLAFOND_SESSION_USD`.

| quantité | devis v7 quinquies | code (manifeste de départ) | pire cas exécuté |
|---|---|---|---|
| somme Claude | 0,4 + 2 × (5 + 9,3) + 4 + 7 = 40,0 | `claude` 40,0 ; `total_claude` 40,0 | 40,00 (8 sessions) |
| somme Argon | 2,5 + 2 × 2,5 + 3,5 + 0,2 = 11,2 | `externe_avec_controle_du_bras` 11,2 ; `total_externe` 11,6 | course 7,5 + bras 3,7 = **11,2** |
| total | 51,6 | 40 + 11,6 | 51,2 dépensés au pire cas |

- Le lanceur accepte (code 0), la course écrit « en attente du bras », le bras (code 0) écrit `classement.json` à trois
  juges, lisible ; le bras lit `plafond_externe_usd` 11,6 et `cout_externe_deja_compte_course_usd` 7,5.
- Marge 0,4 : elle couvre exactement deux contrôles du bras refusés et payés (7,5 + 0,4 + 3,7 = 11,6), à la lecture.
- Le contrôle du bras entre dans la somme de `verifier_reglages` et du cœur (mutations N01, N02 tuées).
- Ce qui ne tient pas (CL40-01, CL40-03) : la relance après un échec, et la cohérence lanceur/cœur hors du défaut 0,2.

## 3. CL39-01 à 12

| constat | verdict | preuve | endroit |
|---|---|---|---|
| **CL39-01** somme d'Argon, contrôle du bras | **corrigé** | S1 (§ 2) ; N01, N02 tuées ; reste : le lanceur ne passe pas `budget_controle_bras_usd` au cœur (CL40-03, N03 survit) | `ideation.py:758, 858` ; lanceur `:441` |
| **CL39-02** contrôle refusé non consigné, relance non bornée | **en partie** | S2 : `tentative-N.json` scellé avec les coûts Claude et externe, plafond compté quand le coût est inconnu (2,5), borne à trois tenue quand le contrôle Claude coûte 0 ; mais aucune relance possible aux réglages du devis (CL40-01), un contrôle interrompu est scellé à 0 (CL40-02), un refus du cœur après les contrôles n'est pas consigné (CL40-03) ; N04, N05, N07, N08 survivent | lanceur `:424-473` |
| **CL39-03** garde du relais sans la dépense | **corrigé** | `verifier_relais` : relance après 0,4 refusée, relais neuf accepté (sonde ; essai) ; M15, N22 tuées ; reste NaN (CL40-05) | lanceur `:256-270` |
| **CL39-04** bras interrompu après envoi | **corrigé** | S8 : SIGTERM pendant la session du juge d'Argon → manifeste du bras, 3,7 comptés (contrôle 0,2 + plafond 3,5), `consigne_envoyee` « argon », relance refusée ; commande et petit-enfant morts ; N16, N17 tuées. Reste mineur : aucun classement, pas même « sans bras » (CL40-08) | `ideation.py:1316-1325, 1372-1374` |
| CL39-05 SIGTERM, SIGHUP | **en partie** | S4 (SIGTERM) et S4b (SIGHUP) pendant la passe d'Argon : code 2, manifeste de fin, session comptée 2,5 (« interrompue »), commande et petit-enfant morts ; N15, N18, N19 tuées. Mais pendant un **contrôle** : 0 compté (CL40-02) | lanceur `:300-316` ; `ideation.py:935-944` |
| CL39-06 contrôle à la plus grosse consigne | **en partie** | S5 : la marge (4 000 caractères × 8) est dépassée dès des champs de 300 caractères ; Argon qui casse au-delà de la taille du contrôle → passe 2 cassée après 14,7 dépensés chez Claude ; S6 : consigne du juge d'Argon 3,4 fois la taille du contrôle ; N13, N14 survivent (CL40-04) | `ideation.py:765-771` |
| CL39-07 refus après les contrôles | **corrigé pour les deux cas cités** | S7 : `--max-tours 3` et SORTIE existante refusés sans dossier de contrôle ; N11, N12 tuées. Autre refus après contrôles : CL40-03 | lanceur `:424` ; `ideation.py:722` |
| CL39-08 régression du simulé | **corrigé** | essai (code 0) ; N20 tuée | lanceur `:89` |
| **CL39-09** valeurs non finies | **corrigé pour la liste de CL6 ; restes** | `sondes_nan.py` : les 13 entrées sondées de la liste refusent NaN, ±∞ et booléen, cas sain inchangé (v39 : 35 acceptations fautives sur ces entrées ; v40 : 0) ; N23 à N34 tuées sauf N28 (équivalente) ; restes et nouveaux endroits : CL40-05, CL40-06 | `pari_apparie.py` |
| CL39-10 garde PACE sans cas sain | **corrigé** | § 5 : cas sain et artefact séparés (99 % contre 0 %, mes graines) ; puissance rapportée ; M34 à M36, N35 à N37 tuées | `porte_pace.py`, démonstration |
| CL39-11 code mort, écrits | **corrigé, restes d'écrits** | aucune définition en double (arbre syntaxique) ; docstrings citées par CL6 réécrites ; restent « devis v7 bis / ter / quater » dans le lanceur (CL40-09) | lanceur `:23, 70, 232, 245` |
| CL39-12 essais | **corrigé** | ordre sain (65 essais OK) ; motif du sceau vérifié ; délai borné (M26 tuée en 65 s) | essais |

## 4. Constats neufs

### CL40-01 — majeur (devis et code ; décision de Lazar avant toute relance) — Aux réglages du devis, aucune relance n'est possible après un contrôle payé

**Endroit.** Lanceur `:427-441` (imputation des tentatives à la somme), `:470` (`relancable`) ; devis v7 quinquies,
points 1, 2 et 4.

**Défaut.** S2 (démontré ; `simulee/S2-relance-apres-controle-argon-paye/rapport.json`) : Argon répond « KO » au
contrôle, coût 0,15.

| coût du contrôle Claude (par modèle) | essai 1 | essais 2 à 4 | tentatives scellées |
|---|---|---|---|
| 0,2 (plafond) | contrôle refusé, 0,4 Claude + 0,15 Argon scellés, « relançable » | refus : « somme des plafonds Claude **40.40** > total 40.0 » | 1 |
| 0,01 (réel faible) | idem, 0,02 + 0,15 | refus : « somme des plafonds Claude **40.02** > 40.0 » | 1 |
| 0 (moteur simulé seul) | idem | deux relances, puis refus « 3 tentatives » | 3 |
| 0,01, Argon cassé sans coût lisible | 2,5 compté (plafond) | refus : somme Claude 40,02 | 1 |

- La somme Claude du devis vaut **exactement** 40,0 ; toute tentative qui a coûté côté Claude la fait dépasser. Or le
  moteur réel exige un coût de contrôle > 0 (`exiger_cout`) : **en réel, la première relance est toujours refusée**.
- Côté Argon, une tentative à son plafond (2,5) porte la somme externe à 13,7 > 11,6 : refus aussi.
- Pour relancer, il faut relever `--budget-total-usd` (et le relais, dont la garde exige alors plafond − 4 ≥ total − 4 :
  le relais à 40 du devis, point 4, refuse un total de 40,4), ou passer `--tolerer-somme-plafonds`, qui **désarme les deux
  sommes à la fois** (CL39-01 l'avait déjà relevé).
- Le fichier scellé dit `relancable: true` et le devis « trois tentatives au plus » : l'un et l'autre sont faux aux
  réglages du devis. L'essai `test_tentatives_de_controle_scellees` ne passe que parce que le contrôle Claude simulé coûte 0.

Le refus protège l'argent (aucun dépassement). Le défaut est la promesse et la procédure : l'opérateur bloqué n'a qu'une
issue documentée, qui désarme les gardes.

**Correction.**
- **Décision de Lazar** (dépense) : (a) « tout échec de contrôle payé = un mot de Lazar » ; le code écrit
  `relancable: false` dès que la somme ne passerait plus, et le devis retire « trois tentatives » ; (b) prévoir la marge :
  Claude 40 + 3 × 0,4 de contrôles (41,2), Argon 11,6 + 2 × 2,5 (16,6), relais relevé d'autant ; (c) ne pas rejouer à la
  relance les contrôles Claude déjà réussis (les lire dans la tentative). Recommandation : (a), confiance moyenne ; (c)
  si les relances doivent rester courantes.
- **Code** : calculer `relancable` avec les sommes de la relance ; séparer les deux tolérances ; un essai avec un contrôle
  Claude payé (> 0).

### CL40-02 — majeur — Un contrôle interrompu est scellé à 0 dollar, dans la course comme dans le bras

**Endroit.** Lanceur `:461-471` (`lecture_e = getattr(e, "lecture", None) or {}`) ; `ideation.py:640-679`
(`appel_de_controle`, qui perd aussi les lectures des modèles déjà contrôlés) ; `ideation.py:1296-1309` (bras).

**Défaut.**
- **S3** (démontré) : SIGTERM au lanceur pendant le contrôle d'Argon (consigne de 36 249 caractères envoyée) → code 2,
  commande et petit-enfant arrêtés, mais `tentative-1.json` porte `cout_externe_usd: 0.0` ; le lanceur imprime
  « sessions en cours comptées au plafond ». Plafond de cette session : 2,5 (la marge d'Argon est de 0,4).
- **S3b** (démontré) : SIGTERM pendant le contrôle du bras → `bras-tentative-1.json` « 0.0000 USD comptés »,
  `relancable: true`.
- À la lecture : une exception de l'adaptateur pendant un contrôle (pas un `ControleRefuse`) suit le même chemin ; si
  elle frappe le second modèle Claude, le coût du premier, déjà payé, est perdu aussi (`controle` n'est pas encore assigné).

C'est la promesse du devis v7 quinquies (point 3) et de CL39-05 non tenue sur le chemin des contrôles, avec une mention
scellée fausse (même nature que CL39-04).

**Correction.** Dans `appel_de_controle`, entourer `adaptateur.lancer` : toute exception compte le plafond de la session
(`cout_inconnu`) et lève `ControleRefuse` avec la lecture accumulée ; même chose dans le bras ; essais avec SIGTERM pendant
chacun des deux contrôles.

### CL40-03 — majeur (code ; hors réglages du devis) — Refus du cœur après les contrôles payés : rien n'est consigné, relance non bornée ; le lanceur et le cœur ne comptent pas le même contrôle du bras

**Endroit.** Lanceur `:441` (`budget_controle_bras_usd=args.budget_controle_usd` donné à `verifier_reglages`) et
`:474-490` (appel du cœur **sans** ce paramètre : défaut 0,2) ; le `try` de la v40 (`:449-471`) ne couvre que les
contrôles.

**Défaut.** S9 (démontré) : `--budget-controle-usd 0.1 --budget-externe-usd 11.1`. `verifier_reglages` compte 0,1 pour le
contrôle du bras et accepte (11,1) ; les contrôles sont payés (Claude 0,2, Argon 2,5) ; le cœur compte 0,2 et refuse
(« somme des plafonds externes 11.20 > total externe 11.1 ») avant de créer SORTIE. Aucun `tentative-N.json`, aucune
SORTIE ; la relance identique repaie les contrôles (Argon 5,0 au total, sans trace), et ainsi de suite.

Le même chemin s'ouvre, à la lecture, pour tout refus du cœur avant `os.makedirs(sortie)` que `verifier_reglages` ne voit
pas : en particulier une somme Claude recalculée avec le coût **réel** des contrôles, qui dépasserait 40 si un contrôle
Claude rendait plus que son plafond avec un statut « ok » (SUPPOSÉ : comportement du kit non vu).

**Correction.** Passer `budget_controle_bras_usd` au cœur ; étendre la capture des tentatives jusqu'à l'écriture du
manifeste de départ (toute exception avant que SORTIE existe scelle une tentative avec les coûts des contrôles) ; essai
inverse (N03 survit aujourd'hui).

### CL40-04 — mineur (majeur si la limite d'Argon est proche de la taille du matériau) — CL39-06 : la marge sous-estime la passe 2, et la consigne du juge n'est jamais éprouvée

**Endroit.** `ideation.py:765-771` (`marge_fiche_caracteres=4000` × `nombre`) ; bras : contrôle de 41 caractères.

**Défaut.**
- S5 (démontré ; pièces 20 000 et matériau 20 000 caractères, 8 fiches d'Argon) : contrôle 72 249 caractères ; passe 2
  d'Argon 76 631 (champs de 300 caractères), 191 831 (1 500), 335 831 (3 000, le maximum permis par champ). Une fiche
  validée n'a pas de taille maximale calculable (liste d'antériorités sans borne).
- Argon factice qui casse au-delà de la taille du contrôle : contrôle et passe 1 passent, **14,7 dépensés chez Claude**,
  puis la passe 2 d'Argon casse (plafond 2,5 compté) ; arrêt sans classement. C'est le scénario S6 de CL6, intact.
- Sans matériau, la seconde passe n'ajoute aucune marge (condition `seconde_passe and materiau_lu`).
- S6 (démontré ; pièces de juge de 100 000 caractères) : consigne du juge d'Argon dans le bras 242 834 caractères, 3,4 fois
  le contrôle de la course ; le contrôle du bras n'envoie que la consigne courte. Une panne de taille y donne un
  classement « sans juge externe, illisible », après toute la dépense Claude.
- N13 (contrôle sur les pièces seules) et N14 (marge d'une seule fiche) survivent à la suite entière.

**Correction.** Jouer **la passe 2 d'Argon juste après sa passe 1**, avant toute passe Claude : elle ne dépend que de ses
propres fiches et du matériau, et l'échec de taille tombe alors avant la dépense Claude, sans deviner une marge. Pour le
bras, éprouver le contrôle à la taille de la consigne du juge (consigne en attente déjà scellée) ou l'écrire comme risque
accepté. Un essai qui vérifie le contenu du contrôle.

### CL40-05 — mineur (latent) — Même famille « pas un nombre » dans le chemin de l'argent, dont un paramètre ajouté par la v40

**Endroit.** `ideation.py:708-760` et `:778-870` (`budget_controle_bras_usd` jamais vérifié) ; lanceur `:256-270`
(`verifier_relais`), `:150-162` (`lire_tentatives_controle`).

**Défaut** (démontré, `outils-cl7/sondes-nan-v40-sortie.txt`) :

| entrée | acceptée à tort | effet |
|---|---|---|
| `verifier_reglages(budget_controle_bras_usd=…)` (et le cœur) | NaN, −∞, −5,0 | somme externe NaN (garde désarmée) ; −5,0 fait passer 11,2 de plafonds sous un total de 6,0 |
| `verifier_relais` : `depense_usd` | NaN, −∞ | garde du relais désarmée |
| `verifier_relais` : `plafond_usd` | NaN, +∞ | idem |
| `verifier_relais` : `reserve_par_appel_usd` | NaN, −∞, booléen | idem |
| `lire_tentatives_controle` | coût NaN, coût −2,5 ; fichier sans sceau | un coût négatif réduit l'imputation ; un fichier supprimé lève la borne de trois |

Par le lanceur, `--budget-controle-usd` NaN ou négatif est refusé **par accident** (il alimente aussi
`cout_controles_prevu_usd`, vérifié). L'état du relais vient du relais local du noyau ; les tentatives sont écrites par le
lanceur avec `allow_nan=False`. Aucun chemin de production démontré.

**Correction.** `_fini` et refus nommé pour `budget_controle_bras_usd` (≥ 0), les trois champs du relais ; vérifier le
sceau de chaque `tentative-N.json` et refuser un coût non fini ou négatif ; essais avec cas sain.

### CL40-06 — mineur (latent) — Restes dans le juge apparié

Démontré (`sondes_nan.py`) : `ebh_pondere(alpha=NaN, +∞ ou True)` accepte des budgets de somme 0,9 (garde de la somme
désarmée ; `Course` vérifie α avant, donc latent) ; `trajectoire_log_richesse`, `evaluer` et la part d'une cellule dans
`contraste` acceptent `True` comme 1 ; `verifier_coefficients` refuse un coefficient entier de numpy que `contraste` admet
(incohérence de `_fini` contre `isinstance(a, (int, float))`). Correction : `_exiger_fini` sur α dans `ebh_pondere` ;
`_exiger_valeur` dans `trajectoire_log_richesse` ; `_exiger_fini` sur les parts ; un seul prédicat.

### CL40-07 — mineur — Essais : affirmations du LISEZMOI et trous

- Le LISEZMOI v40 annonce « un essai chacune » pour les 21 survivantes de CL6, dont M07 : M07 survit à la suite entière
  (§ 6). L'essai cité (`test_tentative_payee_imputee_et_non_lance`) ne peut pas la tuer : le coût 0,15 > 0 suffit déjà à
  écarter « rien envoyé ». Seule une exception pendant le contrôle du bras (coût 0, processus parti) la distingue — c'est
  aussi le chemin de CL40-02.
- Survivantes neuves : N03 (CL40-03), N04, N05, N07, N08 (imputation des tentatives à la somme et au cœur), N13, N14
  (CL40-04). N28 est équivalente (la vérification existante des budgets refuse déjà NaN, ∞ et `True`).
- L'essai des tentatives ne passe que grâce à un contrôle Claude simulé gratuit (CL40-01).

### CL40-08 — mineur — Bras verrouillé après envoi : aucun classement, et aucun outil pour l'écrire

S8 (démontré) : après une interruption pendant la session du juge d'Argon, la course ne porte que les notes des deux
juges Claude ; ni `classement-sans-bras.json` ni moyen de l'écrire (le bras refuse toute nouvelle exécution). La dépense
Claude (≈ 40) reste sans classement, même marqué illisible. Correction : écrire le classement à deux juges marqué « sans
juge externe » sur ce chemin aussi, ou une commande qui l'écrit sans appel.

### CL40-09 — mineur — Écrits

- Lanceur : « devis v7 bis » (`:232`), « v7 ter » (`:23, 245`), « v7 quater » (`:70`) ; le devis en vigueur est v7 quinquies.
- Message d'interruption du lanceur : « sessions en cours comptées au plafond » — faux pour les contrôles (CL40-02).
- LISEZMOI v40 : « 7 % à 400 » (simulation de la garde seule) ; la démonstration publiée donne 3,0 % à n_dev = 400 ; mes
  graines : 7 % (garde de 400 unités, n_dev = 120). Préciser de quelle mesure il s'agit.

**Compte des constats neufs : aucun bloquant de lancement, 3 majeurs (CL40-01 à 03), 6 mineurs (CL40-04 à 09).**

## 5. Porte PACE : la garde a-t-elle un cas sain ?

- **Oui, et il se sépare de l'artefact.** `GardeV40.test_garde_discrimine_quand_elle_a_ses_unites` ; reproduit avec mes
  graines (`outils-cl7/garde_puissance.py`, 100 suites par ligne, racine 7000029) :

  | réglage | témoin honnête validé | tricheur validé |
  |---|---|---|
  | monde par défaut, m = 20, 120 unités | 3 % | 0 % |
  | monde par défaut, garde 400 unités | 7 % | 0 % |
  | monde par défaut, garde 1 000 unités | 38 % | 0 % |
  | δ = 0,10, 120 unités | 11 % | 0 % |
  | δ = 0,10, 400 unités | 68 % | 0 % |
  | cas sain de l'essai : bruit 0,02, 600 unités, m = 5 | **99 %** | **0 %** |
  | bruit 0,02, 120 unités, m = 5 | 14 % | 0 % |

- **Un témoin honnête passe-t-il ?** Dans le cas sain construit, oui (99 %) ; dans le monde par défaut et aux tailles du
  pilote, presque jamais (1 à 3 %). La v40 le dit (LISEZMOI, docstring, ligne « puissance de la garde » de la
  démonstration) ; la lecture « la garde est un instrument de mille unités » est cohérente avec mes chiffres (38 % à
  1 000 ; 42 % annoncé). Pour G1, δ = 0,10 change beaucoup (68 % à 400) : la puissance doit être simulée avec le bruit
  réel des écarts avant le scellement, comme la v40 le recommande.
- Régime « tricheur » : écarts tirés comme en v39 (même formule), graines des régimes d'avant inchangées (ordre gardé) ;
  la démonstration reproduit les chiffres de CL6.
- Bras de référence, sans sélection : inchangé (à la lecture).

## 6. Défauts réintroduits

`outils-cl7/mutations.py` : une copie neuve par défaut, remplacement vérifié (occurrence unique ou désignée). Premier
passage sur les modules d'essais qui touchent le fichier muté ; chaque survivante confirmée sur la suite entière
(`mutants/mutations-complet.json`).

Les 21 survivantes de CL6 sont reconstituées d'après leur description au § 6 de CL6 (son script n'était pas fourni) ;
pour M28 (« ex-M15 », sans description), ma version — sceau de la consigne en attente non vérifié — est une supposition.

| groupe | tuées | survivantes à la suite entière |
|---|---|---|
| 21 survivantes de CL6 | **19** : M09, M12 à M22, M26, M29 à M31, M34 à M36 | **M07** (« rien envoyé » sans condition de processus), **M28** (reconstitution incertaine ; l'empreinte attestée couvre presque tout, sauf une consigne modifiée puis attestée) |
| CL39-01, 02, 03, 07, 08 (N01 à N12, N20 à N22) | N01, N02, N06, N09 à N12, N20 à N22 | N03, N04, N05, N07, N08 (CL40-01, CL40-03) |
| CL39-04, 05, 06 (N13 à N19) | N15 à N19 | N13, N14 (CL40-04) |
| CL39-09 (N23 à N34) | N23 à N27, N29 à N34 | N28 (équivalente) |
| CL39-10 (N35 à N37) | toutes | — |

**Total : 58 réintroduites, 48 tuées, 10 survivantes à la suite entière** (premier passage : 48 tuées, 10 survivantes ; les 10 confirmées sur la suite entière, 363 essais réussis chacune). Des 21 de CL6 : 19 tuées, 2 survivent.

## 7. Ce que je n'ai pas pu vérifier

- La commande réelle d'Argon : barème d'une requête de ≈ 1,1 million de caractères (le plafond de 2,5 du contrôle), quotas,
  limite de taille réelle (portée de CL40-04), durée.
- Les sessions Claude réelles sous SIGTERM (le kit et son sous-processus) ; le comportement du kit quand une session
  dépasse son plafond avec un statut « ok » (CL40-03, SUPPOSÉ).
- La garde du relais contre le vrai relais (`relais_reel.py`) : éprouvée en appel direct de `verifier_relais` seulement.
- Un second signal pendant l'écriture du manifeste de fin (à la lecture : `KeyboardInterrupt` levé au milieu d'une écriture
  scellée).
- L'extrait de l'article PACE et la note (R7) ; la taille réelle du matériau et des pièces de juge ; le GO.

## 8. Fin de relecture

- Empreintes après relecture (02:53 UTC) : `sha256sum -c EMPREINTES-orchestrateur-pole-v7-v40.txt` : 150 sur 150 conformes ; compagnons conformes ; les 518 fichiers de `v39/` et `v40/` identiques au relevé du début (`outils-cl7/empreintes-debut.txt` contre `empreintes-fin.txt`) ; aucun `__pycache__` dans les arbres relus.
- Processus : aucun processus de mes scénarios ni d'essais actif (0 trouvé par `ps`) ; les commandes et petits-enfants des scénarios d'interruption ont été vérifiés morts.

## 9. Fichiers produits

Sous `relecture-v40/cl7/` :
- `contre-lecture-v40-cl7.md` (ce rapport) ;
- `outils-cl7/` : `argon_factice.py` (Argon local, journal de chaque appel), `lanceur_pire.py` (moteur simulé au pire
  cas), `scenarios.py` (S1, S2, S3, S3b, S4, S4b, S5, S6, S7, S8, S9), `sondes_nan.py` et ses sorties v39 et v40,
  `garde_puissance.py` et sa sortie, `mutations.py`, `mutants/` (sorties par mutation, `mutations-premier-passage.json`,
  `mutations-complet.json`), `essais-sortie.txt`, `mutations-complet-sortie.txt`, `empreintes-debut.txt`,
  `empreintes-fin.txt`, `temps-*.txt` ;
- `simulee/` : un dossier par scénario (pièces, configurations d'Argon, journal d'Argon `argon-journal.jsonl`, sorties de
  course, `rapport.json`), `porte-pace-demo-v40-sortie.txt`, `nan-v39/`, `nan-v40/` ;
- `copie-essais/` : copies de v39 et v40 sur lesquelles tout a tourné (à supprimer à volonté).
