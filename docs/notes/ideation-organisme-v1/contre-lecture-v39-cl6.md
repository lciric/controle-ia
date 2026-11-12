# Contre-lecture CL6 du différentiel v37 → v39 — prise « idéation », porte PACE, garde appariée (orchestrateur du pôle v7)

Contre-lecteur neuf (règle R2) : Opus 5.5. Je n'ai écrit ni le code (session servie par Fable 5.1) ni les relectures
précédentes. Relevés `date -u` : début 00:46, fin 01:40 UTC, le 29 octobre 2026. Aucun réseau, aucune clé, aucun appel
payant ; le seul « Argon » joué est `outils-cl6/argon_factice.py`, local, qui consigne chaque appel. `pole/…`,
`demonstrations/…` et `essais/…` désignent l'arbre `v39/orchestrateur-pole-v7/`. « Démontré » : exécuté par moi ;
« à la lecture » : non exécuté.

## Verdict : **non lançable en l'état** ; lançable après une décision de Lazar sur les plafonds d'Argon et trois corrections courtes

1. **Bloquant de lancement, sans dépense (CL39-01).** Avec les réglages du devis v7 quater (deux passes, contrôle d'Argon à
   2,5), le lanceur refuse avant tout appel : « somme des plafonds externes 11.00 > total externe 9.0 » (démontré, S1). Le
   devis écrit « somme 8,9 » en comptant ce contrôle à 0,2 ; à 2,5, elle vaut 2,5 + 2 × 2,5 + 3,5 + 0,2 = 11,2. De plus,
   la somme du code omet le contrôle du bras : un réglage accepté (contrôle 0,5, somme 9,0) laisse le bras refusé au pire
   cas, sans aucun classement (démontré, S2). Recommandé : total d'Argon 11,2 à 11,6, tenable au pire cas (démontré, S9).
2. **Trois majeurs** (démontrés) :
   - CL39-02 : un contrôle refusé (jusqu'à 2,5 chez Argon) n'est consigné nulle part, et la relance n'est pas bornée ;
   - CL39-03 : la garde du relais ignore la dépense déjà faite, donc à la relance le dernier juge peut être refusé (pire cas) ;
   - CL39-04 : une interruption pendant la session du juge du bras est scellée « avant tout envoi des fiches », puis
     rejouée (à corriger avant le bras seulement).
3. **CL37-01 à 09** : corrigés à l'endroit annoncé, avec des restes, 01 (passe 1), 02 (contrôle), 03 (cœur) et 08 ; en
   partie 04, 05, 07 et 09 ; 06 non codé (déclaré). Sur 38 défauts réintroduits, 17 sont détectés et 21 survivent à la
   suite entière (§ 6).
4. **Défaut NaN (« pas un nombre ») : correction exacte mais incomplète.** Même famille, latente (à la lecture, aucun chemin de production ne
   sert de valeur non finie) : `verifier_coefficients` et `contraste` (NaN → +1), `ebh_pondere` (un NaN dérange le tri :
   fausses promotions), `Course.ajouter_trajectoire`, `trajectoire_log_sans_remise`, `borne_basse`, `evaluer`. La porte
   PACE vérifie tout.
5. **Porte PACE** : bien un bras de référence, sans sélection. Ses essais séparent cas sain et artefact, sauf pour la
   garde : le cas sain y manque, et notre garde refuse aussi un témoin honnête (démontré).

**Avant la course** : CL39-01 (code et devis), CL39-02, CL39-03. **Avant le bras** : CL39-04. Le reste peut suivre.

## 1. Comptes vérifiés

- **Empreintes** (`sha256sum -c EMPREINTES-orchestrateur-pole-v7-v39.txt`) : 149 sur 149 conformes avant (00:46) et après
  (§ 7) ; compagnons v38 et v39 conformes ; rien de créé ni modifié dans `v39/` ou `v37/`.
- **Différentiel** (`diff -rq`, listes d'empreintes v38 contre v39) : la v38 change `ideation.py`, `adaptateurs.py`, le
  lanceur et `test_v7_ideation.py` ; la v39 change `pari_apparie.py` et son essai, et ajoute la porte PACE, sa démonstration
  et ses essais.
- **Essais** : commande demandée, sous `env -i`, sur une copie. **340 essais, 340 réussis**, 206,2 s, code 0
  (`outils-cl6/essais-sortie.txt`). Conforme au LISEZMOI v39.
- **Démonstration PACE** (graine 20261029) : les trois chiffres du LISEZMOI v39 sont reproduits (32,0 % contre 0,5 % ;
  témoin à 50 % contre 90 % ; tricheur refusé par notre seul bras) (`simulee/porte-pace-demo-sortie.txt`).

## 2. CL37-01 à 09

« Tuée » : au moins un essai échoue quand le défaut est réintroduit (§ 6).

| constat | verdict | preuve | endroit |
|---|---|---|---|
| **CL37-01** Argon en tête, contrôle à la taille réelle | **corrigé pour la passe 1** | Argon en premier à chaque passe (S2, S6 ; M01 tuée) ; contrôle sous `proposeur_ideation` (M03 tuée), sur les pièces : 188 210 caractères contre 190 333 en passe 1 (S2 ; M02 tuée) ; coût compté (M04 tuée). Restent CL39-06, CL39-02, CL39-08 | `ideation.py:934` ; `ideation_v1.py:393-399` |
| **CL37-02** contrôle du bras qui a coûté | **corrigé pour le contrôle ; reste la session du juge** | Coût du contrôle refusé compté (M06 tuée) ; tentatives payées scellées, au plus trois (M08, M10 tuées) ; imputation au plafond présente mais non éprouvée (M09 survit) ; « rien envoyé » seulement sans processus (M07 survit, quasi équivalente hors moteur simulé). Une interruption ou une exception pendant le juge passe pour « avant envoi » (CL39-04) | `ideation.py:1280-1290, 1322, 1381-1387, 1444-1462` |
| **CL37-03** somme des plafonds, relais | **corrigé au cœur pour Claude ; trois trous** | Somme Claude refusée au cœur (M11 tuée). Sans essai : somme externe au cœur (M12 survit) ; sommes de `verifier_reglages` (M13, M14 survivent) ; garde du relais (M15 survit). La garde ignore la dépense déjà faite (CL39-03). La somme externe omet le contrôle du bras, et le devis compte faux (CL39-01) | `ideation.py:749-759, 941-959` ; `ideation_v1.py:378-387` |
| **CL37-04** refus avant les contrôles | **corrigé en partie** | `verifier_reglages` avant tout contrôle (lecture `ideation_v1.py:368` puis `:389` ; S1 : aucun appel) ; `math.isfinite` partout ; défaut 750 000. Rien de cela n'est éprouvé (M16 à M19 survivent). Deux refus tombent encore après les contrôles (CL39-07) | `ideation.py:707-763, 904-914` |
| **CL37-05** essais | **en partie** | Tuées : ex-M3, ex-M5, ex-M8, ex-M7 et ex-M16 (par M04, M05), médiane ; sceau faux tuée par effet de bord (CL39-12) ; cinq survivent (§ 6) ; chemin relatif corrigé (lecture `essais:694`) | `essais/test_v7_ideation.py` |
| **CL37-06** taille des consignes, jetons | **non codé (déclaré)** | Aucune taille de consigne au journal. Comptage en jetons reporté au devis (point 5) | — |
| **CL37-07** interruption | **corrigé pour SIGINT seulement** | S4 : SIGINT (interruption clavier) arrête la commande et son petit-enfant ; SIGTERM (`kill PID`, l'arrêt par identifiant de R10) les laisse vivants, sans manifeste de fin (CL39-05). Aucun essai (M20 survit) | `adaptateurs.py:455-460` |
| **CL37-08** délais | **corrigé, sans essai** | 3 600 et 1 800 (lecture `adaptateurs.py:33, 377` ; `ideation_v1.py:221-222, 315`). M21 et M22 survivent | |
| **CL37-09** écrits | **en partie** | LISEZMOI v38 réécrit ; restent les écrits de CL39-11 | |

## 3. Constats neufs

### CL39-01 — bloquant de lancement (devis) et majeur (code) — Somme d'Argon : le devis compte faux, le code omet le contrôle du bras

**Endroit.** Devis v7 quater, point 1 ; `ideation_v1.py:223-224, 376` ; `ideation.py:751-759` (`verifier_reglages`),
`:946-959` (cœur, champ `externe_sans_controle_du_bras`), `:1346-1349` (bras).

**Défaut.**
- **S1** (démontré) : réglages du devis → code 2, « somme des plafonds externes 11.00 > total externe 9.0 » ; aucun appel.
- **S2** (démontré) : `--budget-controle-externe-usd 0.5` → somme 9,0 acceptée ; Argon déclare son plafond à chaque
  session ; course complète (`cout_externe_usd` 5,5) ; bras refusé : « plafond externe 9.0 insuffisant avant tout appel :
  déjà 5.5 + contrôles et sessions 3.7 ». Ni classement ni manifeste du bras : la dépense Claude resterait sans classement.
- Le lanceur passe `budget_externe_usd=None` au bras (`:343`) : aucune option ne relève ce plafond.
- `--tolerer-somme-plafonds` lèverait le refus, mais désarme aussi la somme Claude.

**Correction.**
- **Code** : ajouter le contrôle du bras à `somme_externe`, au moins une fois, au mieux `MAX_TENTATIVES_BRAS` fois. Le
  faire dans `verifier_reglages` et au cœur, et séparer les tolérances Claude et externe.
- **Devis** (décision de Lazar : dépense) :
  - (a) contrôle d'Argon ≤ 0,3 (0,3 + 5 + 3,5 + 0,2 = 9,0) : rien de plus, mais une requête de cette taille peut coûter
    davantage (SUPPOSÉ : barème d'Argon non vu), et le contrôle serait refusé ;
  - (b) proposeur Argon à 1,4 par passe : une session peut être coupée après la dépense Claude ;
  - (c) total d'Argon à 11,2 (général 51,2), ou 11,6 pour couvrir trois contrôles du bras : garde les plafonds du devis ;
    S9 (démontré) : tout au plafond, course puis bras à 7,5 + 3,7 = 11,2, classement écrit ; 2,2 à 2,6 dollars de plus,
    sous GO.
- **Recommandation** : (c), confiance moyenne.

### CL39-02 — majeur — Un contrôle refusé n'est consigné nulle part ; la relance n'est pas bornée

**Endroit.** `ideation_v1.py:389-399` (`ControleRefuse` non traité, il remonte à l'`except` général de `:262-266`, qui
imprime le motif seul) ; `ideation.py:672-674`.

**Défaut.** S5 (démontré) : commande factice qui casse au-delà de 1 000 caractères (quota simulé), contrôle plafonné à 0,5.
- Code 2. L'adaptateur compte le plafond (« coût inconnu, plafond de session compté »), mais aucun fichier ne le porte.
- La relance dans la même SORTIE est permise ; un second contrôle est payé.
- Au défaut du devis (2,5), chaque tentative peut coûter 2,5 chez Argon hors de tout compte, alors que le plafond externe
  du bras se calcule sur le seul compte du cœur. Les contrôles Claude (0,4) ne sont comptés que par le relais (à la lecture).

C'est CL37-02 transposé au chemin de la course, avec un plafond de 2,5 au lieu de 0,2.

**Correction.**
- Capturer toute exception après le premier contrôle.
- Sceller `SORTIE-controle/tentative-N.json` (lectures, coûts, plafond si le coût est inconnu).
- Au lancement, lire ces tentatives, imputer leurs coûts aux totaux Claude et externe, borner à trois ; essai inverse.

### CL39-03 — majeur (pire cas, même nature que CL37-03) — La garde du relais ignore la dépense déjà faite

**Endroit.** `ideation_v1.py:378-387`.

**Défaut.** La garde compare `plafond − réserve` à `total − plus petit juge`, sans `depense_usd`, que porte pourtant
l'état du relais. Banc R1 (démontré sur le vrai `Compteur` de `relais_reel.py` et le vrai cœur, chaque session dépensant
son plafond) :
- **relais neuf** : course complète à 40,00 ;
- **relance après une tentative qui a payé 0,4 de contrôles** : la garde passe (elle lit 0,4 et l'ignore) ; le cœur lance
  le juge Opus à 36,00 à son journal ; le relais le refuse (402) à 36,40 ; arrêt sans classement.

La relance contre le même relais est le chemin attendu après CL39-02 ou CL39-07.

**Correction.** Refuser si `plafond − réserve − dépense < total − plus petit juge` (une ligne ; éprouvée sur R1 : relance
refusée, relais neuf accepté), ou relancer le relais à chaque tentative. Consigner l'état lu au manifeste.

### CL39-04 — majeur (avant le bras) — Interruption pendant la session du juge du bras : scellée « avant tout envoi », sans son coût, rejouable

**Endroit.** `ideation.py:1396` (envoi) ; `ideation.py:1455-1462` (classement de l'échec).

**Défaut.** S8 (démontré) : Argon reçoit la consigne du juge (14 177 caractères, fiches comprises), puis SIGINT.
- `bras-tentative-1.json` est scellé avec « tentative 1 du bras échouée avant tout envoi des fiches, 0.0100 USD
  comptés » et `relancable: true` ;
- la relance renvoie la consigne (deux envois au total) et écrit le classement.

Trois fautes : une mention scellée fausse ; une session non comptée (jusqu'à 3,5) ; un rejeu après dépense, contraire à
CL34-04. Une exception de l'adaptateur pendant la session suit le même chemin (démontré, S8bis : `OSError` après
réception de 12 363 caractères → même message, relançable).

**Correction.** Marquer `consigne_envoyee` juste avant `adaptateur.lancer("juge_ideation", …)`. Ensuite, tout échec compte
le plafond (coût inconnu) et verrouille le bras (manifeste du bras, ou classement sans bras). Essai.

### CL39-05 — mineur — SIGTERM laisse Argon vivant, sans manifeste de fin ; une session interrompue n'est pas comptée

**Endroit.** `adaptateurs.py:455-460` ; `ideation.py:1157-1167`.

**Défaut.** S4 (démontré) :
- **SIGINT** : la commande et son petit-enfant sont arrêtés ; mais le manifeste de fin compte 0,01 (contrôle seul), sans
  la session interrompue.
- **SIGTERM** : l'orchestrateur meurt (code −15) ; la commande et son petit-enfant restent vivants (je les ai arrêtés par
  identifiant) ; aucun manifeste de fin. Sessions Claude sous SIGTERM : non vérifiées.

**Correction.** Gestionnaire de SIGTERM et SIGHUP qui lève `KeyboardInterrupt` dans le lanceur ; plafond compté pour une
session interrompue ; essai avec SIGTERM.

### CL39-06 — mineur (portée selon la taille du matériau, inconnue ici) — Le contrôle « à la taille réelle » n'éprouve que la passe 1

**Endroit.** `ideation_v1.py:397` (`supplement=verif["texte_pieces"]`).

**Défaut.**
- Tailles dans S2 : contrôle 188 210 caractères, passe 1 190 333, passe 2 427 377 (×2,27 : pièces, matériau, fiches).
- S6 (démontré) : un Argon qui casse au-delà de 300 000 caractères passe le contrôle et la passe 1, puis casse en passe 2,
  après la passe 1 Claude (en réel : jusqu'à 14,3). Arrêt, plafond de 2,5 compté.
- Avec `--taille-max-pieces 750000` par lot, la passe 2 peut atteindre ≈ 1,5 million de caractères.

**Correction.** Servir au contrôle la plus grosse consigne que l'externe recevra : pièces, plus le matériau s'il est
attesté, plus une marge pour ses fiches. Consigner la taille de chaque consigne au journal (CL37-06).

### CL39-07 — mineur — Deux refus du cœur tombent encore après les contrôles

**Endroit.** `ideation_v1.py:215` (`--max-tours` non borné) ; `ideation.py:896-897, 978`.

**Défaut.** S7 (démontré) : une SORTIE existante (`FileExistsError`) et `--max-tours 3` (refus du cœur) tombent après le
contrôle d'Argon, dont le coût n'est consigné nulle part (CL39-02).

**Correction.** Avant les contrôles : SORTIE absente, `max_tours` ≤ 2.

### CL39-08 — mineur — Régression : la répétition simulée avec un proposeur externe, sans commande, échoue

**Endroit.** `ideation_v1.py:88` (égalité stricte avec la consigne de contrôle), à rapprocher de `ideation.py:630-636`.

**Défaut.** S3 (démontré) : v39 → code 2, « appel de contrôle refusé pour gemini-argon : texte '```json…' ≠ OK » ; même
commande sur une copie de la v37 → code 0.

**Correction.** `consigne.startswith(idn.APPEL_DE_CONTROLE_CONSIGNE)` ; un essai.

### CL39-09 — mineur (latent) — Valeurs non finies ailleurs dans le juge apparié

Détail au § 4.

### CL39-10 — mineur — Porte PACE : la garde n'a pas de cas sain, et refuse aussi un témoin honnête

Détail au § 5.

### CL39-11 — mineur — Code mort et écrits

- **`ideation.py:766-867`** : une première définition de `executer_ideation`, morte, que la seconde (`:870`) remplace.
  Elle porte deux noms non définis (`cout_controles_prevu_usd`, `cout_controles_externes_prevu_usd`) et le `return` de
  `verifier_reglages` (démontré par l'arbre syntaxique).
- **`ideation.py`** : `:44-46` « ses notes ne sont jamais agrégées » (faux depuis la v36) ; `:8` « moyenne » ;
  `:773, 877` « v36 » ; `:1071` « Claude puis externes » (l'inverse depuis la v38).
- **Lanceur** : `:22-23` (1800, 900, 650000) ; `:218` (« devis v7 bis ») ; `:38-41` muet sur « relance permise ».
- **LISEZMOI v38** annonce un essai « plafond diminué » qui n'existe pas (M09 survit).

**Correction.** Supprimer la définition morte ; réécrire ces écrits.

### CL39-12 — mineur — Essais

- **Dépendance d'ordre**, préexistante (v37 aussi, démontré) : `test_v7_ideation` puis `test_adaptateurs` → trois échecs
  (`test_adaptateurs.py:113` trouve `claude_agent_sdk` chargé) ; `discover` ne passe que par l'ordre alphabétique.
- **Sceau faux** : `essais:845-851` ne vérifie pas le motif du refus ; M25 n'est tuée que par une assertion ultérieure.
- **Essai du délai** : durée toujours non bornée (M26 survit, en 72 s).

**Compte des constats neufs : 1 bloquant de lancement (CL39-01, volet devis ; volet code majeur), 3 majeurs (CL39-02 à
04), 8 mineurs (CL39-05 à 12).**

## 4. Défaut NaN : la correction est-elle complète ?

**La correction elle-même est exacte.** `trajectoire_log_garde` refuse NaN, ±∞, les non-nombres et les booléens
(`pari_apparie.py:99-101`). L'essai couvre NaN, +∞, −∞, None, "0.1" et True, plus un cas sain (M32 tuée).

**Elle n'est pas complète.** Effets démontrés en appel direct (`outils-cl6/sondes_nan.py`, `ebh_nan.py`) :

| fonction | entrée non finie | effet | atteignable en production (à la lecture) |
|---|---|---|---|
| `verifier_coefficients` (`:48-60`) | constante NaN | acceptée (±∞ refusés) | non : l'empreinte canonique de `construire` (`engagement_apparie.py:84` ; `outils.py:21`, `allow_nan=False`) lève `ValueError` — refus par accident, non nommé |
| `contraste`, `contraste_plafonne` (`:63-71, 214-216`) | constante ou coefficient NaN ; coefficient ±∞ | v = **+1**, le plus favorable ; douze unités → **promue** à l'instant 7 | non, même raison (`monde_banque_scores.py:150`) |
| `ebh_pondere` (`:221-236`) | e-valeur NaN | tri dérangé : [0 ; NaN ; 3,0] → **trois fiches retenues au lieu d'aucune** ; 17 416 familles sur 54 108 énumérées retiennent à tort une fiche finie | non : `Course.lire` ne reçoit que des trajectoires finies d'`evaluer` |
| `Course.ajouter_trajectoire` (`:389-397`) | +∞ ; NaN en cours de route | +∞ → **promue** ; NaN ignoré sans erreur | non, même raison |
| `trajectoire_log_sans_remise` (`:105-120`) | NaN, +∞, hors [−1 ; 1] | NaN → −690 puis empoisonne μ ; +∞ → NaN ; 5,0 accepté (favorable) | aucun appelant dans `pole/` |
| `borne_basse` (`:178-201`) | NaN ; 5,0 | −0,98 ; **0,99** (favorable) | rapportée seulement (`engagement_apparie.py:180`) |
| `evaluer` (`:147`) | α ou m NaN | seuil NaN : jamais promue, sans erreur | non : α_c vérifié (`engagement_apparie.py:109`) |
| porte PACE (`porte_pace.py:107-149, 223, 278`) | gain réel, δ, α, λ, issues, écarts | tous refusés, erreur nommée | gain réel et δ sans essai (M34, M36) |

**Journaux des duels passés** (le LISEZMOI v39 demande de les relire) : à la lecture, seul `monde_banque_scores.py:164-167`
sert des écarts à la garde, différences de fractions de scores vérifiés finis (`:66`) ; je n'ai trouvé aucun chemin vers
un écart NaN. Journaux non vus.

**Correction.** Une fonction `_fini(x)` et un refus nommé à chaque entrée : constante, coefficients et v avant la borne
(`contraste`) ; `log_e` (`ebh_pondere`) ; trajectoire (`ajouter_trajectoire`) ; valeurs (`sans_remise`, `borne_basse`) ;
α et m (`evaluer`). Chacune avec son essai et son cas sain. `ebh_pondere` décide : à faire avant toute lecture de G1.

## 5. Porte PACE

- **Bras de référence, à la lecture** : aucun appelant dans `pole/` hors essais et démonstration ; décisions dans l'ordre
  d'entrée, sans rang ; référence fixe (écart à PACE marqué [INFÉRÉ]). L'invariant N-053 est tenu ; la protection reste
  documentaire (rien n'empêche un futur appelant de choisir sur `validee`).
- **Fidélité à l'article** : non vérifiable ici (extrait et note hors périmètre, R7) ; la réduction à
  `trajectoire_log_richesse(v, (λ,))` est éprouvée par un essai.
- **Essais : cas sain et artefact séparés** pour les issues, les longueurs, α, λ, les jeux vides, le budget, les doublons et
  m (M33, M37 tuées). Lacunes :
  - gain réel et δ non finis (M34, M36 survivent) ;
  - e-BH (Benjamini-Hochberg sur e-valeurs) contre arrêt par candidat (M35 survit) ;
  - **la garde n'a pas de cas sain.** `test_garde_bloque_le_tricheur_que_pace_valide` (`essais/test_v7_porte_pace.py:184-192`)
    prend pour cas sain le régime « gain », qui n'a pas de garde.
- **Puissance de la garde** (démontré, `outils-cl6/garde_cas_sain.py`, 200 suites par ligne) : garde active, témoin
  honnête de gain 0,35, écarts d'espérance nulle. Part des suites où notre bras valide le témoin :

  | instances | témoin honnête avec garde | tricheur | témoin honnête sans garde |
  |---|---|---|---|
  | 40 | 0 % | 0 % | 48 % |
  | 120 | 2 % | 0 % | 100 % |
  | 400 | 8 % | 0 % | 100 % |

  Dans ce monde simulé, la garde n'a presque aucune puissance. Le refus du tricheur ne montre donc pas qu'elle
  discrimine. La phrase du LISEZMOI v39 « refusé par notre garde » est exacte, mais trompeuse sans ce pendant.
- **Correction (CL39-10).** Ajouter un régime « honnête avec garde » à `simuler_suite`, à la démonstration et à l'essai ;
  rapporter la puissance de la garde à côté du refus du tricheur.

## 6. Défauts réintroduits

`outils-cl6/mutations.py` : une copie neuve par défaut, remplacement vérifié. On lance d'abord les modules d'essais qui
touchent le fichier muté, puis on confirme chaque survivante sur la suite entière (`mutations-complet-sortie.txt`).

« ex-Mn » : même cible que la mutation n de CL5, d'après sa description (son script n'est pas dans mon périmètre). Erreur
de ma part, corrigée : mon premier sous-ensemble plaçait `test_adaptateurs` après `test_v7_ideation`, ce qui échoue sans
mutation (CL39-12) ; cinq « tuées » à tort, rejouées dans l'ordre sain.

| verdict | réintroductions |
|---|---|
| **tuées (17)** | CL37-01 : M01 à M05 ; CL37-02 : M06, M08, M10 ; CL37-03 : M11 ; CL37-05 : M23 (ex-M5), M24 (médiane), M25 (sceau faux, par effet de bord), M27 (ex-M3), M38 (ex-M8) ; v39 : M32 (garde NaN), M33 (écarts vérifiés par PACE), M37 (témoin planté compté) |
| **survivantes à la suite entière (21)** | CL37-02 : M07, M09 ; CL37-03 : M12 à M15 ; CL37-04 : M16 à M19 ; CL37-07 : M20 ; CL37-08 : M21, M22 ; survivantes de CL5 : M26 (ex-M1), M28 (ex-M15), M29 (ex-M6), M30 (ex-M11), M31 (ex-M17) ; PACE : M34 à M36 |

Pour CL37-01 à 08 (M01 à M22) : 9 tuées, 13 survivantes. Les essais de la v38 tiennent CL37-01 et le cœur de CL37-02 ;
ils n'éprouvent ni les sommes externes, ni la garde du relais, ni l'ordre « réglages avant contrôles », ni les plafonds
non finis, ni l'interruption, ni les délais.

## 7. Fin de relecture, et ce que je n'ai pas pu vérifier

- **Empreintes après relecture** (01:38 UTC) : 149 sur 149 conformes, code 0 ; compagnons conformes ; les 506 fichiers du
  périmètre relu identiques au début ; aucun `__pycache__`.
- **Non vérifié** : la commande réelle d'Argon (coût d'une requête de cette taille, donc l'option (a) de CL39-01 ;
  quotas ; durée) ; les sessions Claude réelles sous interruption ou SIGTERM ; l'extrait de l'article PACE et la note
  (R7) ; les journaux des duels passés ; la taille du matériau réel (portée de CL39-06) ; les devis v2 à v7 ter et le GO.

## 8. Fichiers produits

Sous `relecture-v39/` : ce rapport ; `outils-cl6/` (Argon factice, scénarios, sondes NaN, bancs e-BH, relais, bras
interrompu et garde, mutations et sorties, `copie-essais/` à supprimer à volonté) ; `simulee/` (`prep/`, S1 à S9, R1 et
leurs sorties). Aucun processus laissé actif (vérifié par `ps`).
