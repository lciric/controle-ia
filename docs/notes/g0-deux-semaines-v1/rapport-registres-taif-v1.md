# Rapport — trois tables par script pour l'entretien avec le Transformative AI Fund — v1

- **Auteur** : développeur neuf (sous-agent), consigne `docs/notes/g0-deux-semaines-v1/consigne-developpeur-registres-taif-v1.md`.
- **Heure** : 2026-11-05, de 16:35 à 16:55 UTC environ (`date -u`).
- **Règles tenues** : aucune cellule saisie à la main (tout vient du script) ; toute cellule sans source est vide ; aucune
  estimation ; aucune lecture de `diag/` ni des résultats de `runs/` (manifestes seulement) ; aucun fichier existant
  modifié ; aucun `.sha256` écrit ; aucun commit, aucune poussée, aucun réseau, aucune dépense. Réserve : pendant le
  travail, un autre processus de la session a pris deux « instantanés (non scellés) » qui comprennent mes fichiers
  (commits `965a1e9f` et `c70c27ff`) ; ce n'est pas un geste de ce développeur.

## 1. Fichiers produits et empreintes (sha256, `sha256sum`, sans compagnon)

| fichier | sha256 |
|---|---|
| `scripts/registres_taif_v1.py` (926 lignes) | `f9e61ffb9d7fe7d81d402f52d92902ed189110d28b606500c27f9283c1b7f001` |
| `tests/test_registres_taif_v1.py` (238 lignes, 8 essais) | `9b0d4207f6c6f60dc003503a8eda23dfc867e18d1f310bcd3edd1231331c66ba` |
| `livrables/registres-taif-v1/promis-livre-v1.md` | `a2bbb9fe0009a6c3b8788cc2bd8c143712948f64099828f8abed23c04be8571b` |
| `livrables/registres-taif-v1/calibration-v1.md` | `b4d7968a3677e0e472579368e41c3d3b52f7b757eecc7b20e13e3fd5ce915ed6` |
| `livrables/registres-taif-v1/cout-par-resultat-v1.md` | `b16af955b8970b757a48cc8d45ba28422cf426994fc880b765bf89c43cb3f54a` |
| `livrables/registres-taif-v1/sources-v1.json` | `ab17c95cf1c9f2afc2724eb772c94c8d8629ff70a16eda7d54965b630ba6786c` |

Commande : `timeout 900 nice -n 10 python3 -I scripts/registres_taif_v1.py` (jour lu par `date -u`, jour seul ; `--jour`
pour le fixer). Deux lancements donnent les mêmes octets (vérifié par `diff -r`). Essais : `python -m pytest -q
tests/test_registres_taif_v1.py` → 8 passés (cas sain ; idempotence ; verdict sans compagnon → refusé ; verdict altéré →
refusé ; préenregistrement sans compagnon → refusé ; dépense sans GO → signalée ; cellule sans source → vide ; filtre des
montants). La suite complète du dépôt a été lancée en parallèle (`--ignore` de ce test) ; son résultat est dans la
réponse finale.

## 2. Comptes

| table | lignes | cellules vides | contenu |
|---|---|---|---|
| `promis-livre-v1.md` | 31 | 83 sur 248 | 8 critères de G0 (programme v2, G1 et papier C comptés à part) ; candidature : 7 puces de la section 6 + la phrase « Gate G0 » ; 6 périodes de la section 7 ; 9 livrables et critères de succès de la section 8 |
| `calibration-v1.md` | 181 | 370 sur 1 810 | 30 préenregistrements scellés lus (brouillons et gabarit exclus ; `SPARKS-…-brouillon8.md`, sans compagnon, est un brouillon donc exclu) ; 11 verdicts scellés ; 45 manifestes |
| `cout-par-resultat-v1.md` | 190 | 1 049 sur 2 280 | 14 runs décisifs (manifeste `decisif` vrai), 153 GO de type calcul, 23 lignes « dépense sans GO cité sur la ligne » |

Sources : 88 fichiers lus, chacun avec son empreinte dans `sources-v1.json` (`fichiers_lus`) ; chaque cellule non vide y
renvoie à un chemin, des numéros de ligne et l'empreinte du fichier (`cellules`) ; 34 signalements (23 dépenses sans GO
cité sur la ligne, 11 lignes qui citent un GO sous forme abrégée « GO-06 », non résolue par le script).

Issues de la table de calibration : 42 confirmées ; 3 réfutées ; 7 non concluantes ; 9 non atteintes ; 2 non déclenchées
(P9 de T0.4) ; 4 contradictoires (lignes citées, non tranchées) ; 17 citées par aucun verdict ; 31 lues au registre des
décisions (T0.3, R-025 : « 31/31 prédictions confirmées », aucun verdict scellé) ; 15 « non encore lues » (convergence
v1, run `20261101-160323` fait, aucun verdict) ; 53 sans run décisif cité par un manifeste.

## 3. Ce que le script a relié

- **Porte G0** : les huit critères viennent de la ligne « Porte G0 » du programme (`docs/programme-controle-ia-v2.md`
  l. 180) ; l'état (prouvés 1 et 5, restent 2, 3, 4, 6, 7, 8) de `registres/etat.md` l. 162 ; la date promise de la
  table des périodes du programme (l. 255) ; le glissement de `registres/etat.md` l. 144 (fin novembre, N-027) et de la
  ligne N-027 du registre des décisions (l. 462) ; la cause par tâche du segment « Reste : » de la table de la phase 0.
- **Pièces** : critère 1 → `docs/verdicts/verdict-T0.4-critere-1-G0-v3.md` (`63444faa…`) ; critère 5 → manifeste du run
  `20261004-080257-t03` (`c9bba5e1…`), cité par la ligne d'état de T0.3 (aucun verdict scellé pour T0.3).
- **Candidature, section 6** : les puces sont reliées aux tâches de la phase 0 par des règles écrites dans le script
  (`REGLES_CANDIDATURE`, mot anglais → tâche) ; l'état est le texte en gras de la colonne « état » de la table.
- **Calibration** : prédiction = ligne de la table de la section « Prédiction chiffrée et signe attendu » (ou puce
  `- **ID**`) ; seuil = lignes de la section « Seuil » qui citent l'identifiant (vide si la section cite d'autres
  identifiants et pas celui-ci ; première ligne si la section n'en cite aucun) ; verdict = fichier de `docs/verdicts/`
  qui cite le chemin du préenregistrement (version la plus récente) ; issue = mots-clés lus d'abord dans la ligne de la
  table de lecture du verdict dont la première cellule est l'identifiant, sinon dans les 40 premières lignes, la
  section « Verdict », puis tout le texte hors tables ; contre-lectures = entrées « Contre-lecture k (…) ».
- **Coût** : run → instance par la ligne du registre des arrêts qui cite le run ; montant = montants des lignes du registre
  des dépenses citant le run ou l'instance (lignes de table d'abord, puces sinon ; engagements exclus ; prix par heure,
  cumuls, plafonds, crédits, « enveloppe », « au plus », montants collés à un identifiant de GO exclus ; « 4,30 / 12 USD »
  lu comme 4,30 dépensés). Une ligne à plusieurs montants retenus n'est pas tranchée : cellule vide, montants listés.
  Par GO : somme des montants uniques (ou en gras) des lignes constatées qui citent le GO.
- **Négatifs (R4)** trouvés par le script : T0.4 v1 (critère 1 « non concluant », verdict v1 l. 3 ; P2 non concluante) et
  v2 (« non prouvé par ce run », verdict v2 ; P4 contraire) dans la calibration et la table 1 (C6-3) ; T0.5 bras « math »
  (verdict de revalidation v2 l. 18 : « nœud », panne de mémoire) : lignes Rk-1 à Rk-8 de la calibration, Rk-1
  contradictoire ; tir SPARKS v9 « boucle » : table 3, ligne GO-2026-11-05-02, colonne « arrêts » (`registres/arrets.md`
  l. 80) ; runs arrêtés par leurs gardes : table 3, colonne « arrêts » des runs `20261005-102042` et `20261005-144628`.

## 4. Ce que le script n'a pas pu relier

- **Promesses sans pièce** (26 sur 31) : G0-2, G0-3, G0-4, G0-6, G0-7, G0-8 (critères restants : aucun verdict, cause
  citée) ; C6-1 (état de l'art : aucun verdict scellé, l'état « niveau 1 fait ; niveau 2 fait » est relié), C6-5 (602
  tests : aucune pièce lue par le script), C6-6 (brouillons de G1 et du papier C : `brouillons/` n'est pas une source),
  C6-7 (« about $20 » : non relié au registre des dépenses), C6-G0 ; C7-1 à C7-6 et C8-1 à C8-9 (échéances futures :
  l'état « à venir » ou « en cours » vient seulement de la date).
- **Prédictions sans verdict scellé** (19 préenregistrements, 100 lignes) : T0.3 (31, lues au registre des décisions
  R-025) ; convergence v1 (15, run fait, « non encore lue ») ; T0.5 revalidation v1 (7, run arrêté avant lecture) ;
  SPARKS v1 (7) et addendum 1 (12) ; P-041 examen final v1, v2 et malléabilité v1 à v3 (14) ; gradient étape 1 v2, v3,
  v4, v9 (8) ; échelle v2 et v9 (2) ; H-M1 v1 à v3 (3). Le verdict de l'échelle v10 ne cite le préenregistrement que
  dans sa table d'empreintes : relié (1 ligne « section entière », issue « non citée par le verdict »).
- **Prédictions citées par aucun verdict** (17) : P3-addendum v1 (A1 à A5…), Rk-3, Rk-4, Rd-6, Rk-7 de la revalidation
  v2, etc. ; **contradictoires** (4) : Rk-1 (verdict l. 18 « non conforme » contre l. 26 « conforme »), deux lignes de
  l'addendum 2 de P3, une de l'addendum 1.
- **Runs sans instance ni montant** : P3 (`20261019-230011`), notations (`20261017-193648`, deux montants 5,3 et 8,23),
  pilote (relié à 4,89 par l. 65), rejeu des juges v2, convergence : la ligne du registre des arrêts ne cite pas le run,
  ou la ligne des dépenses porte plusieurs montants.
- **Négatifs non reliés par les tables** (à lire dans les registres) : A1-v3, courses 1 et 2 interrompues par
  l'infrastructure (`registres/decisions.md` l. 1331 R-1103, l. 1421 R-1463, l. 1436 R-1478 ; `registres/arrets.md`
  l. 76) ; R1 arrêté par sa garde de fidélité puis relancé v2, v3, v4 (`registres/arrets.md` l. 70 ; `registres/etat.md`
  l. 165 ; `registres/decisions.md` l. 1247 R-1019) : ces lignes ne citent ni run décisif ni GO sous la forme complète.
- **GO abrégés** (11 lignes, « GO-06 », « GO-08 », « GO-10 ») : non résolus, signalés.

## 5. Les dix cellules qu'un lecteur extérieur vérifiera d'abord

| n° | table, ligne, colonne | valeur | source (chemin, ligne, sha256) |
|---|---|---|---|
| 1 | promis, G0-1, pièce | `docs/verdicts/verdict-T0.4-critere-1-G0-v3.md` | verdict l. 3, `63444faa4ce2…` (empreinte compagnon vérifiée) |
| 2 | promis, G0-5, pièce | `runs/20261004-080257-t03/manifeste.json` | manifeste, `c9bba5e1f5f8…` ; état `registres/etat.md` l. 162 |
| 3 | promis, G0-2, glissement | « fin novembre 2026, critères inchangés (N-027) … Reste : … » | `registres/etat.md` l. 144 et l. 155 ; `registres/decisions.md` l. 462 |
| 4 | calibration, T0.4 v3, P4 | confirmée | `docs/verdicts/verdict-T0.4-critere-1-G0-v3.md` l. 109 (table de lecture) |
| 5 | calibration, T0.5 pilote, P5 | réfutée | `docs/verdicts/verdict-T0.5-pilote-v1.md` l. 249 |
| 6 | calibration, P3, P3-P3 | réfutée | `docs/verdicts/verdict-P3-premier-test-i-a-v2.md` l. 14 |
| 7 | calibration, T0.3, P1.1 (et les 30 autres) | « registre des décisions, R-025 : 31/31 prédictions confirmées » | `registres/decisions.md` l. 34 (aucun verdict scellé) |
| 8 | calibration, T0.5 revalidation v2, Rk-1 | contradictoire (l. 18 / l. 26) | `docs/verdicts/verdict-T0.5-revalidation-v2.md` |
| 9 | coût, run `20261006-114025-validation-reelle`, montant | 2,67 USD, 1 verdict, 2,67 USD par verdict | `registres/depenses.md` l. 42 ; instance par `registres/arrets.md` |
| 10 | coût, GO-2026-10-04-08, montant | 2,96 USD (4 lignes sommées, 3 non tranchées, 13 engagements) | `registres/depenses.md` l. 7, 8, 9, 31 |

Et la ligne « (sans GO) l. 92 » de la table 3 : dépense de calcul sans GO par la relève de Gemini (montants lus 6,01 et
6,42, non tranchés), `registres/depenses.md` l. 92.

## 6. Trois risques

1. **L'issue d'une prédiction est une lecture par mots-clés**, pas une lecture du sens : un « conforme » cité dans une
   phrase négative, ou un identifiant partagé entre versions (P2 de T0.4 v1, v2, v3), peut donner une issue fausse ou une
   contradiction. Chaque issue cite ses lignes ; les 4 contradictions et les 17 « non citées » sont à lire à la main
   avant l'entretien.
2. **Les montants viennent d'un registre en prose** : les règles d'exclusion (prix horaire, cumul, plafond, crédit) sont
   écrites dans le script et peuvent manquer un cas ; les sommes par GO peuvent compter deux fois une dépense recopiée
   (table et puce du même jour ne sont dédoublonnées que pour les runs) ou manquer une dépense citée sous un GO abrégé.
   Aucun total n'est opposable sans relecture des lignes citées.
3. **Les liaisons promesse → tâche → pièce sont des règles de mots** (`REGLES_CRITERES_G0`, `REGLES_CANDIDATURE`) : une
   promesse mal appariée (la section 6 est en anglais, la table d'état en français) hériterait d'un état ou d'une pièce
   d'une autre tâche. Les 31 lignes de la table 1 se relisent en quelques minutes ; les liaisons sont dans
   `sources-v1.json`.
