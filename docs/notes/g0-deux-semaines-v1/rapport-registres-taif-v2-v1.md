# Rapport — registres pour le fonds, version 2 (quatre tables par script) — v1

- **Auteur** : développeur neuf (sous-agent, modèle Claude Fable 5.1), consigne L5 de la session mère.
- **Heure** : 2026-11-05, de 21:05 à 22:35 UTC environ (`date -u` : 2026-11-05 22:09:52 UTC à la régénération des tables).
- **Règles tenues** : aucune cellule ni aucun compte saisi à la main (tout vient du script) ; toute cellule sans source est
  vide ; aucune estimation dans un total relevé ; aucune lecture de `diag/`, de `donnees/` ni des résultats de `runs/`
  (manifestes seuls) ; aucun fichier existant modifié (script v1, essais v1, `livrables/registres-taif-v1/`, rapport v1
  intacts ; compagnons `.sha256` vérifiés : `scripts/registres_taif_v1.py`, les quatre sorties v1, le rapport v1, tous
  conformes) ; aucun `.sha256` écrit ; aucun commit, aucune poussée, aucun réseau, aucune clé, aucune dépense.
- **Constat préalable** : `livrables/registres-taif-v1/page-fonds-v1-brouillon1.md` est absent du dépôt (`find` sur tout
  l'arbre : rien) ; le total qui remplira son marqueur `<<TOTAL_DEPENSES_PHASE0>>` est écrit seul dans `sources-v2.json`
  (clé `total_depenses_phase0`) ; la page n'a pas été touchée.

## 1. Fichiers produits et empreintes (sha256, `sha256sum`, sans compagnon)

| fichier | sha256 |
|---|---|
| `scripts/registres_taif_v2.py` (1 472 lignes) | `6721f2ee6c18933c527ed77fcaa33b656f55863e7a90e129a6125027b6d24c5e` |
| `tests/test_registres_taif_v2.py` (535 lignes, 19 essais) | `8caadc2277ba448f4f5499ab0e0e7473378952c1c6589f169b127e376dbf9902` |
| `livrables/registres-taif-v2/promis-livre-v2.md` | `b95a140277d69cf18f2baefc56ac5ebe6e9f5fad0c7f2c0b5c6b275ed30f34b9` |
| `livrables/registres-taif-v2/calibration-v2.md` | `346632046f7c85185afd307252872035011e8c1501b33e9e8290c5246f45702e` |
| `livrables/registres-taif-v2/cout-par-resultat-v2.md` | `2fadff71bfdebdb3a1da1a2584bf5f95e25809465c19d914dd5f86f12583baa2` |
| `livrables/registres-taif-v2/total-depenses-v2.md` | `94e0dbd6eeb86e686a607b685bebd2578a48c64e6ec88dd521611e45ce1a4d18` |
| `livrables/registres-taif-v2/journal-depenses-v2.txt` | `f2343501c5419ae6dc07cd3af01706960d0f339378a36465726aca73bbab5ba7` |
| `livrables/registres-taif-v2/sources-v2.json` | `83475f147a6f7deb62f954908129078c118af18364d6eaae19d1301fa8cb860e` |

Commande : `PYTHONPATH=src timeout 900 nice -n 10 python scripts/registres_taif_v2.py --sortie livrables/registres-taif-v2`
(jour lu par `date -u`, jour seul). **Déterminisme vérifié** : un second lancement vers un dossier neuf donne les mêmes
octets pour les six fichiers (`diff -r` vide).

Essais : `python -m pytest -q tests/test_registres_taif_v2.py` → **19 passés** (les 8 essais de la v1 repris et adaptés aux
noms v2, plus 11 essais nouveaux, un sain et un artefact par règle changée, section 3). Suite entière du dépôt, lancée une
fois par lots de fichiers d'essais sous `timeout 900 nice -n 10` : SUITE_ENTIERE_RESULTAT.

## 2. Comptes (ceux du script, cités tels quels)

`sources-v2.json`, clé `comptes` :

```
{"promis-livre-v2": 31, "calibration-v2": 181, "cout-par-resultat-v2": 190, "total-depenses-v2": {"par_go": 108, "par_tache": 8},
 "preregs_lus": 30, "verdicts_lus": 11, "manifestes_lus": 45,
 "calibration": {"total": 181,
   "par_issue": {"confirmée": 41, "contradictoire": 2, "mixte (plusieurs identifiants, issues différentes)": 1, "non atteinte": 6,
                 "non citée par le verdict": 12, "non concluante": 7, "non déclenchée": 2,
                 "non encore lue (run décisif fait, aucun verdict scellé)": 15, "rapportée sans verdict (descriptive)": 3,
                 "registre des décisions (sans verdict scellé)": 31, "réfutée": 3, "sans objet": 5,
                 "sans run décisif cité par un manifeste": 53},
   "tranchees": 51, "confirmees": 41, "refutees": 3, "non_concluantes": 7, "sans_objet": 5,
   "taux_confirmation": "41 / 51 = 0,804", "taux_confirmation_valeur": 0.8039}}
```

Le même bloc, calculé depuis les lignes de la table rendue (`compter_issues_table_md` relit le texte markdown de
`calibration-v2.md`, colonne « issue »), est écrit en fin de `calibration-v2.md` (« Comptes par issue ») : total **181**,
tranchées **51**, taux de confirmation parmi les tranchées **41 / 51 = 0,804** ; « sans objet » **5**, à part, hors
numérateur et hors dénominateur. Le désaccord relevé par la lecture à la main (rapport v1 : 183 lignes dont 2 « non
déclenchées », table : 181 sans) ne peut plus se produire : le rapport ne cite que le bloc du script, et le bloc vient de
la table.

Dépenses (`sources-v2.json`, clés `total_depenses_phase0` et `total_depenses_phase0_detail`) : **`"636,82"`** ;
`{"releve_usd": "636,82", "lignes_sommees": 124, "estime_usd_a_part": "83,20", "lignes_estimees": 46, "lignes_non_sommees": 171}`.
Signalements : 205 (171 « dépense non sommée », avec la raison ; 23 « dépense sans GO cité sur la ligne » et 11 « GO cité
sous forme abrégée » repris de la table 3). Raisons du journal : montants de contexte seulement (prix unitaire, cumul,
plafond, devis, crédit, reste, attendu, pire cas, autre projet) 142 ; plusieurs montants 17 ; plusieurs montants en gras 7 ;
ligne hors entrée 2 ; fourchette 1 ; relevé partiel 1 ; reprise d'un montant déjà consigné 1.

Fichiers lus : 88, chacun avec son empreinte dans `fichiers_lus` ; verdicts et préenregistrements scellés vérifiés contre
leur compagnon (un compagnon absent ou différent arrête le script, essais `test_verdict_sans_compagnon_refuse`,
`test_verdict_altere_refuse`, `test_preregistrement_sans_compagnon_refuse`).

## 3. Les changements de règle et leurs essais

**Changement 1 — comptes alignés sur la table.** `compter_issues_table_md(texte_md)` relit l'en-tête de la table rendue,
repère la colonne « issue » (garde d'arrêt si elle manque), classe chaque ligne de données par catégorie
(`categorie_issue` : préfixe de l'issue → catégorie ; « réfutée (non conforme) » et « réfutée (contraire) » → réfutée ;
« contradictoire (…) » → contradictoire ; « registre des décisions, … » → registre des décisions (sans verdict scellé) ;
etc.) et calcule total, tranchées (confirmée + réfutée + non concluante) et taux. `construire` rend la table, la relit,
puis lui ajoute le bloc. Essais : `test_comptes_recalcules_depuis_la_table_rendue` (sain : les comptes de
`sources-v2.json` sont ceux que l'essai recalcule depuis le texte ; artefact : une ligne ajoutée au texte de la table
change le compte recalculé ; artefact : table sans colonne « issue » → `GardeArret`), `test_categories_de_compte`.

**Changement 2 — table de lecture du verdict avant les mots-clés.** `issue_pour_verdict` lit d'abord
`issue_table_de_lecture` sur tout le verdict : les tables markdown sont reconstruites avec leur en-tête
(`tables_du_fichier`) ; une ligne dont la première cellule est l'identifiant (après suppression du gras, d'une virgule
et d'une parenthèse : « **R8, durée** » → R8) donne l'issue par sa colonne d'issue (en-têtes, par ordre de préférence :
issue, verdict, statut, conclusion, lecture, résultat, conforme, « réfutation … atteinte ? ») ; « oui » / « non » en tête
de cellule se lisent conforme / non conforme (à l'envers sous « réfutation atteinte ? » : non = prédiction tenue) ; sans
colonne d'issue, les autres cellules sont lues par mots-clés ; une table recopiée du préenregistrement (en-tête
« réfutation » ou « prédiction », sans colonne d'issue) n'est pas une table de lecture. Un identifiant de bras
(« Rk-5 », « Rd-6 ») se lit aussi « R5 », « R6 » (`motif_id`), et « [A2] » entre crochets est une référence de pièce,
pas une prédiction. À défaut de ligne de table : mots-clés dans la prose (tête de 40 lignes, section « Verdict », tout le
texte), lue par paragraphes et par segments (« ; » ou fin de phrase), chaque segment classé à part, le code en ligne
retiré ; à défaut encore : « sans objet » lu dans une cellule de table qui cite l'identifiant (seule lecture permise
hors tête de ligne). Une ligne de prédiction à plusieurs identifiants (« Rk-7, Rk-8 ») donne une issue par identifiant
(`issue_pour_prediction`), « mixte (…) » si elles diffèrent. Essais : `test_table_de_lecture_prime_sur_les_mots_cles`
(sain : prose « P2 non concluant : ne s'applique pas ; les deux sont conformes » contre table « oui » → confirmée par la
ligne de table ; artefact : sans ligne de table → « non concluante » par mots-clés, lecture de la v1),
`test_oui_non_bras_et_non_atteint`, `test_table_recopiee_du_prereg_ignoree`,
`test_colonne_refutation_atteinte_lue_a_l_envers`, `test_plusieurs_identifiants_sur_une_ligne`.

**Changement 3 — « sans objet ».** `ISSUES` porte `(r"sans objet", "sans objet")` avant « non établi » et « non atteint »
(« sans objet (cible non établie) » se lit sans objet) ; la catégorie compte à part et n'entre ni au numérateur ni au
dénominateur. Essai : `test_sans_objet_distinct_de_non_atteinte` (sain : « P7 : sans objet (cible non établie) » → sans
objet, A7 lu dans une cellule de table ; artefact : « P8 : non atteint » → non atteinte ; comptes : sans objet 2,
tranchées 1, taux 1 / 1).

**Changement 4 — quatrième table, analyseur strict des dépenses** (`jetons_montants`, `analyser_ligne_depense`,
`analyser_depenses_strict`). Chaque jeton « n USD » d'une ligne est classé : prix unitaire (par heure, par Go, par jour) ;
hors dépense (proposition portant cumul, plafond, enveloppe, crédit, solde, reste, alerte, devis, pire cas, attendu,
projection, minimum, exigé, paiement, recharge, tarif, prix, dossier, poste, seuil, autre projet, non imputé ; « x / plafond » ;
montant collé à un identifiant de GO ; résultat d'une formule « = » ou d'un produit « × » ; « conseillés », « d'ici »,
« de crédits ») ; relevé partiel (« premier relevé », « cumulés », « déjà imputé », « en cours ») ; fourchette
(« 4,4 à 6,7 USD ») ; estimé (« ≈ », « ≤ », « environ », « au plus », « estimé », « borne », « de marche », « de carte »,
« comptés au pire cas ») ; relevé (montant nu). Règles : R1 prix et hors dépense ne sont jamais des dépenses ; R2 aucun
jeton restant → journal « montants de contexte seulement » ; R3 un seul jeton restant → relevé ou estimé selon sa classe,
partiel et fourchette → journal ; R4 plusieurs jetons restants → le montant unique en gras vaut total de la ligne
(convention du registre), sinon un relevé unique dont le contexte immédiat dit « relevé », « facture », « réel », « exact »
remplace les estimations de la même ligne (compté une fois), sinon journal « plusieurs montants » ; un titre de ligne
« inscrit à la clôture », « bilan », « récapitulatif », « rappel » → journal « reprise ». La table à 9 colonnes est lue
dans sa colonne « coût (USD) » (« ≈ » → estimé). Une ligne qui dit remplacer une estimation par un relevé (« remplace
l'estimation », « corrige l'estimation », « relevé exact : », « facture relue : ») sort de la colonne « estimé » les
estimations antérieures du même GO (comptée une fois, journal « estimation remplacée par le relevé de la l. N »).
Totaux par GO (périmètre et plafond lus dans `registres/go.md`), par tâche de la phase 0 (`T0.x` ou `Px` nommée sur la
ligne, sinon dans le périmètre du GO) et global, chacun avec le nombre et les numéros des lignes sommées, estimées et non
sommées. Essais : `test_depenses_strict_registre_sain_totaux_connus` (registre factice : relevé 36,97279 sur 6 lignes,
estimé 3,14 sur 2, journal 4 lignes avec leurs raisons, buckets par GO, par tâche, GO abrégé),
`test_depenses_strict_artefacts_par_regle` ((a) ligne ambiguë à deux montants → journal, rien sommé ; (b) « ≈ », « ≤ »,
« environ », « au plus » → colonne estimé ; (c) estimation remplacée par un relevé, sur la même ligne et d'une ligne à
l'autre → comptée une fois, estimé 0 ; (c') sans mention de remplacement, l'estimation reste en colonne estimé, jamais
dans le relevé ; (d) deux montants en gras, fourchette, premier relevé, reprise → journal ; (e) prix, cumul, plafond,
crédit, devis, montant collé à un GO, « x / plafond », formule → jamais sommés ; (f) montant unique en gras parmi des
composantes → total de la ligne, sans gras → journal), `test_total_depenses_cle_sources_et_journal`.

**Le cas « A1-v3 du 5 novembre » du registre réel.** Les lignes d'A1-v3 datées du 5 novembre (`registres/depenses.md`,
`d85469f386db…`, l. 358 à 362 : sondes v9 et v10 de l'hôte durable ; l. 371 : troisième course) ne portent que des bornes
et des estimations (« borne au plus 0,0504 USD », « dépense ≤ 0,037 USD », « estimation de la machine 0,0186 », « coût de
la machine au plus 5,02 USD (≤ 35) ») : elles vont en colonne « estimé » (l. 358, 359, 361, 362, 371), jamais au relevé ;
aucune d'elles ne dit remplacer une estimation par un relevé. Le cas « estimation puis relevé » d'A1-v3 que le registre
porte réellement est la paire l. 326 (« premier relevé du relais … 6 appels, 0,35 USD », GO-2026-11-02-21) / l. 328
(« 41 appels, 4,25 USD au compte du relais 8805 ») : la classe « relevé partiel » envoie la l. 326 au journal et seul le
relevé final 4,25 est sommé (une fois) ; la règle de remplacement explicite est écrite dans le script et éprouvée sur un
registre factice (essai (c)). Si la session mère visait une autre ligne, elle est à nommer : le script ne devine pas.

## 4. Lignes dont l'issue change entre `calibration-v1.md` et `calibration-v2.md`

Comparaison ligne à ligne (mêmes 181 lignes, même ordre, mêmes numéros : la table commence à la ligne 9 des deux
fichiers). 24 lignes changent d'issue ; 1 ligne (153) ne change que son identifiant affiché (« Rk-7 » → « Rk-7, Rk-8 »,
issue inchangée « sans run décisif ») ; les 156 autres sont identiques. Verdict P3 : `docs/verdicts/verdict-P3-premier-test-i-a-v2.md`
(`05e896daed17…`) ; T0.4 v1 : `docs/verdicts/verdict-T0.4-critere-1-G0-v1.md` (`fb9919f9c4d7…`) ; T0.4 v3 :
`docs/verdicts/verdict-T0.4-critere-1-G0-v3.md` (`63444faa4ce2…`) ; revalidation T0.5 v2 :
`docs/verdicts/verdict-T0.5-revalidation-v2.md` (`f98b56841d2c…`).

| ligne | préenregistrement # prédiction | issue v1 → v2 | verdict, ligne(s), ce qui fonde la lecture v2 |
|---|---|---|---|
| 25, 26 | P3-addendum-lecture-complementaire-v1 # A2 (a), (b) | contradictoire (confirmée l. 310 / non atteinte l. 316, 317) → non citée par le verdict | P3 v2 : les lignes 310, 316, 317 citent « [A2] », référence de pièce (addendum 2), pas la prédiction A2 (lecture à la main v1, note 1.1 : « confusion de sections ») ; aucune autre ligne ne cite A2 |
| 32 | P3-addendum-lecture-complementaire-v1 # A6 | contradictoire (confirmée l. 277 / non établie l. 279) → contradictoire (confirmée l. 277, 279 / sans objet l. 277, 279) | P3 v2 l. 277-279, un paragraphe : « un seul vise une conclusion établie : « A6 P3-P1 » » et « les quatre autres contrôles de A6 sont « sans objet » (cibles … non établies) » ; changement 3 (« sans objet » avant « non établi ») ; contradiction gardée, jamais tranchée |
| 33, 34, 35 | P3-addendum-lecture-complementaire-v1 # A7 (i), (ii), (iii) | non citée par le verdict → sans objet | P3 v2 l. 290 : « \| `reserve_A7_forme_du_cout` \| sans objet (A7 ne vise que des conclusions de sonde ; aucune établie) \| » (cellule de table citant A7) |
| 43 | P3-addendum2-audit-verdict-v1 # B2 | non atteinte → non concluante | P3 v2 l. 473, table l. 468 « réfutation écrite atteinte ? » : « **non tranchée** : la réfutation écrite ne peut pas être lue » → non tranchée = non concluante |
| 44 | P3-addendum2-audit-verdict-v1 # B3 | non atteinte → sans objet | P3 v2 l. 474 : « sans objet (aucune réfutation possible ; « B3 n'est pas une prédiction ») » |
| 46 | P3-premier-test-i-a-v1 # P3-P2 | confirmée → rapportée sans verdict (descriptive) | P3 v2 l. 499-500 : « P3-P2 rapportée sans verdict, aucune réserve » ; l. 562 : « Descriptifs de la lecture rapportés sans verdict … P3-P2 » (la v1 lisait « établie » de P3-P1 sur la même ligne 499) |
| 48 | P3-premier-test-i-a-v1 # P3-P4 | non atteinte → contradictoire (sans objet l. 17, 19 / non atteinte l. 17, 19) | P3 v2 l. 17 : « P3-P4 et P3-P7 (sans objet, … » ; l. 19 : « … appartient à la ligne « P3-P4 conforme », non atteinte » ; deux segments d'un même paragraphe, rapportés |
| 49 | P3-premier-test-i-a-v1 # P3-P7 | non atteinte → sans objet | P3 v2 l. 17 : « P3-P4 et P3-P7 (sans objet, … » |
| 50, 51 | P3-premier-test-i-a-v1 # P3-P5, P3-P6 | non atteinte → rapportée sans verdict (descriptive) | P3 v2 l. 501-502 : « P3-P5 et P3-P6 rapportées sans verdict, le témoin a l'effet de manipulation attendu » (phrase coupée par un retour à la ligne, lue entière ; la v1 lisait « sans objet » de P3-P4 sur la même ligne 501) |
| 106 | T0.4-validation-modele-reel-v1 # P4 | confirmée → non atteinte | T0.4 v1 l. 124, table l. 118 « id \| issue observée \| lecture \| justification » : « \| P4 \| Phase de production non jouée. \| **non atteint** \| » (la v1 lisait « conformes » de P0, P1, P3 sur la ligne 5) |
| 110 | T0.4-validation-modele-reel-v1 # P8 | confirmée → non atteinte | T0.4 v1 l. 128 : « \| P8 \| Stockage et relecture … non joués. \| **non atteint** \| » |
| 111 | T0.4-validation-modele-reel-v1 # P9 | confirmée → non atteinte | T0.4 v1 l. 129 : « \| P9 \| … \| **non déclenché en logique** (conforme pour cette phase) ; **non atteint en production** \| » (« non atteint » précède « non déclench » dans l'ordre des mots-clés ; la cellule dit les deux) |
| 122 | T0.4-validation-modele-reel-v2 # P9 | confirmée → non déclenchée | T0.4 v3 l. 114 (verdict le plus récent citant le préenregistrement v2), table l. 99 « id \| valeur recalculée \| seuil ou règle \| lecture gelée \| lecture du code \| accord » : « \| P9 \| … \| non déclenché \| `audit_symetrie` : non déclenché \| oui \| » (colonne « lecture gelée » préférée à « accord ») |
| 136 | T0.4-validation-modele-reel-v3 # P9 | confirmée → non déclenchée | même ligne 114 du verdict v3 |
| 154 | T0.5-revalidation-equivalence-pilote-v2 # Rk-1 | contradictoire (réfutée (non conforme) l. 18 / confirmée l. 26) → confirmée | revalidation v2 l. 55, 56, table l. 53 « critère \| … \| conforme » : « \| R1, garde saine \| … \| 0,1354 \| ≤ 0,2 \| oui \| », « \| R1, marge \| … \| ≤ 0,15 \| oui \| » (le « non conforme » de la l. 18 qualifie le bras par R8) |
| 156 | … # Rk-3 | non citée par le verdict → confirmée | revalidation v2 l. 58 : « \| R3, repère \| … \| 2 × q99 ≤ 0,2 à chaque couche \| oui \| » |
| 157 | … # Rk-4 | non citée par le verdict → confirmée | revalidation v2 l. 59 : « \| R4, rejeu du lot 0 \| … \| vrai \| identité au bit près \| oui \| » |
| 158 | … # Rk-5 | non concluante → confirmée | revalidation v2 l. 60 : « \| R5, domaine \| … \| 160 ; 140 ; 4 752 ; 4 752 \| ≥ 40 ; … \| oui \| » (cas de référence de la consigne ; la l. 39 « R2 ou R5 non concluant : ne s'applique pas » n'est plus lue avant la table ; l. 273 « Rk-5 : 160 actions comparées attendues ; 160 observées » concorde) |
| 159 | … # Rd-6 | non citée par le verdict → confirmée | revalidation v2 l. 61 : « \| R6, chemin … \| … \| C1 ≤ 3e-3 ; C2 ≥ 95 %, au moins 10 ; C3 conforme \| oui \| » (« Rd-6 » lu « R6 ») |
| 160 | … # Rk-7, Rk-8 | non citée par le verdict → mixte (Rk-7 : confirmée l. 62 ; Rk-8 : réfutée (non conforme) l. 63) | revalidation v2 l. 62 : « \| R7, mémoire \| … \| 24,02 Gio \| ≤ 70 Gio \| oui \| » ; l. 63 : « \| **R8, durée projetée …** \| … \| ≤ 7 800 s \| **non** (dépassement de 289,62 s, soit 3,71 %) \| » ; la ligne du préenregistrement (l. 82) porte les deux identifiants |

Lectures de la v2 qui diffèrent de la lecture à la main v1 (section 1 de `lecture-a-la-main-calibration-v1.md`), à
l'attention du lecteur : A1, A3, A4, A5, A8, A9 restent « non citée par le verdict » (la lecture à la main les tranche
« non atteinte » par raisonnement sur les l. 277 et 294, qui ne les nomment pas : le script ne lit que ce qui nomme la
prédiction) ; A6 reste contradictoire (la lecture à la main tranche « confirmée, partie P3-P1 ») ; la ligne 160 est
« mixte » et non « réfutée » (Rk-7 tenue, Rk-8 réfutée : les deux sont rapportées) ; la ligne 184 (échelle v10, « section
entière ») reste « non citée par le verdict » (le verdict ne nomme aucun identifiant de prédiction). Ces lignes ne sont
pas dans le taux.

## 5. Lignes qui restent « sans verdict scellé »

- **T0.3** (31 lignes, l. 71 à 101 de `calibration-v2.md`, `prereg/T0.3-simulation-lemme-theoreme-v1.md`) : issue
  « registre des décisions, R-025 (pas de verdict scellé) : … 31/31 prédictions confirmées … » ; aucun fichier de
  `docs/verdicts/` ne cite ce préenregistrement ; comptées à part (catégorie « registre des décisions (sans verdict
  scellé) »), hors du taux.
- **Convergence v1** (15 lignes, l. 169 à 183, `prereg/preregistrement-regles-defense-convergence-v1.md`) : « non encore
  lue (run décisif fait, aucun verdict scellé) » ; la lecture scellée et l'audit « trop beau » vivent sous
  `docs/notes/convergence-defense-v1/regles-defense-v1/`, pas sous `docs/verdicts/` ; hors du taux.
- **Sans run décisif cité par un manifeste** (53 lignes) : inchangées.

## 6. Trois risques

1. **La lecture reste une lecture par mots-clés, maintenant plus large.** La table de lecture prime, mais à défaut la
   prose est lue par paragraphes et par segments : un paragraphe long, une citation de l'identifiant dans une parenthèse
   (« (A6) ») ou une colonne d'en-tête inattendue peuvent encore donner une issue fausse ou une contradiction (P3-P4,
   A6). Le rang des colonnes d'issue (« lecture gelée » avant « accord », « conforme ») et la lecture inverse de
   « réfutation atteinte ? » sont des règles écrites, pas des lectures du sens : chaque issue cite ses lignes, et les
   2 contradictoires, 1 mixte, 12 « non citées » sont à lire à la main avant l'entretien.
2. **Le total relevé (636,82 USD, 124 lignes) est une borne par construction, pas le coût de la phase 0.** Il somme ce
   qui est écrit nu et une fois ; les locations de cartes du registre sont presque toutes des estimations
   (« ≈ x USD de marche »), donc en colonne « estimé » (83,20 USD, 46 lignes), et 171 lignes vont au journal, dont 142
   pour contexte seulement et 17 à plusieurs montants (par exemple l. 86, notations, « au plus 8,23 USD » ; l. 92,
   relève de Gemini, 6,01 et 6,42 USD). Deux lignes peuvent encore décrire la même dépense sans que le script le voie
   (par exemple l. 324 et l. 331, « inscrit à la clôture », écartée par le titre ; une reprise sans ce mot serait comptée
   deux fois), et l'attribution par tâche est indicative (« P2 », « P3 » repérés sur la ligne, périmètre du GO sinon).
   Aucun total n'est opposable sans relecture des lignes citées dans `sources-v2.json`.
3. **Les changements modifient le taux affiché par des règles, pas par une relecture des pièces** : recalculé sur la
   table v1 par la même fonction, le taux était 42 / 52 = 0,808 ; il est 41 / 51 = 0,804 dans la v2 (la lecture à la
   main v1 donnait 47 / 59 = 0,797 après ses propres corrections, puis 48 / 59 = 0,814 avec Rk-5). Mouvements : 5
   confirmations gagnées (Rk-1, Rk-3, Rk-4, Rk-5, Rd-6), 6 perdues (P3-P2 ; P4, P8, P9 de T0.4 v1 ; P9 de v2 et v3), 1
   non concluante perdue (Rk-5) et 1 gagnée (B2), 5 « sans objet » hors du dénominateur. Un lecteur extérieur qui
   préfère compter « non déclenchée », « mixte » ou « sans objet » autrement retrouve tout dans le bloc du script ; mais
   le taux lui-même ne doit pas être présenté comme une mesure stable : trois règles de lecture l'ont déplacé, et une
   quatrième (la lecture à la main) le déplace encore.
