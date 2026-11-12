# Préenregistrement — mini-course d'idéation réelle, Kimi et Argon seuls, nuit du 1er au 2 novembre 2026, v2

- Auteur : sous-agent de session-depot (rédacteur des pièces et de ce texte), à la demande de session-depot ; exécution par
  session-depot. Aucun appel payant, aucun appel réseau vers un modèle, rien de scellé ni de commis par le rédacteur.
- **Version 2** = version 1 (`preregistrement-mini-course-kimi-argon-v1.md`, brouillon relu
  `2b73102b58a41e6913ad46396c5e9c1a36a9dbbea02b0c9184c952202cb7e487`, gardé sans modification, R12), avec les corrections
  de la contre-lecture (section « Contre-lecture », traitement de CLM-01 à CLM-13).
- Date (UTC) : 2026-11-01 ; version 1 écrite à partir de 21:04 ; version 2 à partir du relevé `date -u` de 21:35.
- Commit du dépôt au moment de la rédaction : `e5ccf955` ; `donnees/` est ignoré par git sur `main` : les empreintes de la
  section « Pièces gelées » font foi ; le commit au lancement est relu par l'orchestrateur (manifeste R9) et porté au registre.
- Documents qui font foi (chemin + empreinte) :
  - devis : `docs/notes/devis-mini-course-kimi-argon-nuit-v1/devis-mini-course-kimi-argon-nuit-v1.md`,
    `18e8495f4e29f4d00fb466293cdbfdfeb633e2c9b5ccef4ac4910dcb2f649f37` — **scénario B** et adaptations 1 à 6 ;
  - ligne de GO : `registres/go.md`, **GO-2026-11-01-12** (type « calcul », plafond « 10 USD », échéance 2026-11-02, accordé par
    Lazar ; scénario B, démonstration non décisive, préenregistrement scellé et contre-lu avant lancement, trace publique
    agrégée seulement, dossier du run sous `donnees/`) ;
  - rapport de contre-lecture : `docs/notes/mini-course-kimi-argon-v1/contre-lecture-mini-course-kimi-argon-v1.md`,
    `a35eac7076c3be63f29ad67e3cebe0e7c1d785e3d5b0a106e18243c7e73cfac0` (scellé) ;
  - orchestrateur v56 : copie identique, fichier pour fichier, à l'archive `CODE-orchestrateur-pole-v7-v56.zip`
    (`29b1b38cfee5e279a06c947fdf1f855628b574e81e44c2d7e48a029151c1b24c`), listée dans
    `EMPREINTES-orchestrateur-v56-copie-v1.txt` (pièce gelée) ;
  - règles R1 à R14 de `CLAUDE.md`.

## Nature et hypothèse

**Démonstration non décisive, sans signe visé (R3).** Aucun chiffre de cette course ne va vers un papier, une porte ou une
décision scientifique. Aucune hypothèse du programme (H1 à H9) n'est testée.

Question, purement descriptive : **la chaîne de l'orchestrateur v56 tourne-t-elle de bout en bout, pour une génération, avec
Kimi (`kimi-k3.1-pro`) et Argon (`gemini-4-argon`) seuls, sous le plafond du GO, sans qu'aucune fiche ni consigne ne sorte du
dossier privé du run ?** On rapporte comment elle tourne (comptes par étape, juges, accord), jamais si les idées sont bonnes.

Montage (scénario B du devis) :
- **une génération**, une case (`statistiques-qui-transferent`, `niveau-methode`) ;
- **deux proposeurs**, six fiches chacun (Kimi, Argon), consigne figée commune (statistiques de détection qui transfèrent,
  niveau méthode : reprise de la piste A de `docs/notes/ideation-organisme-v1/course-2/question-course-2-v1.md`, glossaire et
  repères chiffrés tels qu'ils y sont cités) ;
- **aiguilleur** Argon sur chaque fiche (passeport « niveau méthode » seul vers les juges, A17) ;
- **deux juges** (Kimi, Argon) sur chaque fiche munie d'un passeport, items K1 à K5, verdict « notable » = cinq items vrais ;
  agrégation **unanimité** ;
- **bisociateur, bras « basique » seul**, une paire : deux lecteurs d'étiquettes (Kimi, Argon) sur une liste fermée de 24
  concepts, puis **une fusion** écrite par Argon, aiguillée et jugée par les deux juges ;
- **sans passe « tableau »** (aucun appel, rien d'écrit ; l'étape reste au plan avec un attendu et un plafond nuls) ;
- **deux contrôles** (un par fournisseur, « Réponds seulement par le mot OK », modèle servi exact exigé) avant la course.

## Prédiction chiffrée et signe attendu

**Aucune prédiction de signe** sur les verdicts, l'accord des juges ou l'écart entre familles (R3) : ils sont rapportés, pas
attendus. Attentes de fonctionnement seulement (devis, scénario B), dont l'écart sera rapporté comme tel :

| Rôle | Fournisseur | Appels attendus |
|---|---|---|
| proposeur | Kimi, Argon | 1 + 1 |
| aiguilleur (12 fiches + 1 fusion) | Argon | 13 |
| juges (12 + 1, chacun) | Kimi, Argon | 13 + 13 |
| lecteurs d'étiquettes (12 chacun) | Kimi, Argon | 12 + 12 |
| metteur en fusion | Argon | 1 |
| contrôles | Kimi, Argon | 1 + 1 |
| **total** | Kimi 27, Argon 41 | **68** |

Dépense estimée au devis ≈ 6,4 USD (pire cas × 1,5 ≈ 9,6). **Borne (CLM-02) : 10 USD au plus au barème supposé d'Argon**
(10 et 50 USD par million de jetons, `collisionneur_v7.py:62-63`, SUPPOSÉ) et au barème vérifié de Kimi (2 et 10). Cette borne
tient si chaque appel coûte moins que son pire cas réservé, ce qui suppose : pour Argon, des jetons d'entrée au plus égaux au
nombre de caractères divisé par 3, et des jetons de réflexion bornés par `maxOutputTokens` (SUPPOSÉ, non vérifié chez
`gemini-4-argon`) ; pour Kimi, un jeton d'entrée d'au moins un octet du corps (hypothèse du relais). Un coût lu au-dessus du
pire cas **arrête la course** (`ArretDepassementReserve`). **La facture réelle se relit au tableau de bord de chaque
fournisseur** ; la borne en dollars n'est exacte qu'au barème.

## Métrique

Toutes calculées par le seul agrégateur `trace_agregee_mini_course_v2.py` (pièce gelée), après la course, sur le dossier du run :

- **L1** — `l1.fin` ∈ {`generation_terminee`, `noeud`, `arret_motif_code`, `non_lance`} ; `l1.motif_arret` (classe codée :
  `depassement_reserve`, `plafond_cumule`, `plafond_etape_commande`, `plafond_relais`, `modele_servi_different`,
  `trois_echecs_consecutifs`, `debordement_garde_kimi`, `signal_recu`, `plafond_etape_faux`, `porte_de_plafond`, `noeud_c13`,
  `autre_exception`, `aucun`) ; statut de chaque étape ; C13 ; `l1.l3_l4` (`calcules`, ou `non_calcules_o12` après un arrêt
  ou un nœud). **Le délai de 12 600 s apparaît comme `signal_recu`** (le lanceur écrit le code 124 au journal) (CLM-09).
- **L2** — comptes : fiches proposées par fournisseur (fiches refusées pour leur forme et propositions sans sortie exploitable
  comptées à part) ; classes de l'aiguilleur et refus ; passeports ; exclusions A4 ; fusions écrites, complètes, inachevées ;
  verdicts présents et absents par juge ; fiches étiquetées par lecteur, lectures rejetées, Jaccard moyen (S24) ; rôles arrêtés.
- **L3** — par juge : verdicts lisibles, nombre et part de « notables » ; selon l'unanimité : nombre et part de fiches
  notables ; accord des deux juges sur « notable » : accord brut et kappa de Cohen.
- **L4** — sur les couples (fiche d'un proposeur, juge) lisibles : part de « notables » et X moyen quand le juge est **de la
  famille de l'auteur**, et quand il est **de l'autre famille** ; écarts. **La fusion est exclue de L4** (CLM-13 : elle peut
  naître d'une paire Kimi et Argon).
- Coûts (par fournisseur, rôle, étape ; registre cumulé, contrôles compris), appels par rôle, durées par rôle.

Effectifs : 13 fiches au plus ; **aucun intervalle n'est opposable** ; tout nombre de L3 et L4 est descriptif.

## Seuil

Aucun seuil de décision scientifique. Seuils **de fonctionnement**, fixés dans la configuration gelée et les lanceurs :
- S17 (plafond de la course, noyau) = 10 USD, portée « course », arrêt d'étape 9 USD ; garde cumulée des commandes = 10 USD ;
  plafonds propres des relais : **Kimi 3 USD, Argon 7 USD** (somme 10, CLM-05) ;
- plafonds de session : proposeur 1,80 ; aiguilleur, juge, lecteur 0,25 ; fusion 0,40 USD ;
- S12 = 0,5 ; A3 = 3 échecs consécutifs ; A14 = 0,25 ; délais A3 : 900 s (Kimi 1 800 s) ;
- anti-fuite : **tolérance nulle**.

## Plan d'analyse

- **Pièces** : configuration `configuration-mini-course-kimi-argon-v2.json` (la v1, dont seule change la commande d'Argon) et
  ses six pièces empreintées ; génération `course2_nuit_v1.py` avec l'adaptateur de `course2_nuit_v2.py` ; lanceurs v2 ;
  commande de Kimi `commande_kimi_v2.py` ; commande et relais d'Argon `commande_argon_v56_nuit_v2.py` ; registre cumulé ;
  agrégateur v2 ; recherche des clés (section « Pièces gelées »).
- **Graines (R9)** : racine `20261102`, préfixe `mc1` ; `numpy.random.SeedSequence(racine, spawn_key=(clé de tâche,))`
  (`pole/graines_v53.py`) ; manifeste R9 écrit par l'orchestrateur (`manifeste-depart.json`).
- **Plan de dépense (règle d'A1 du brouillon 10, `budget_v56`)** : proposition (attendu 0,94 ; plafond de relais 2,50 ;
  protégée) ; aiguillage (1,20 ; 2,60 ; protégée) ; juges (1,87 ; 3,00 ; protégée) ; passe « tableau » (0 ; 0 ; sacrifiable,
  rang 2, hors scénario) ; étiquettes (1,87 ; 3,00 ; protégée) ; fusions (0,47 ; 1,10 ; sacrifiable, rang 1).
- **Modèles** : identifiants exacts ; modèle servi exigé égal au modèle demandé ; aucun changement de modèle.
- **Ordre** (`lancer-mini-course-v2.sh`) : vérifications sans écriture (empreintes, préenregistrement v2 et rapport de
  contre-lecture scellés, configuration, gardes R5 rejouées à É0, ligne de GO à exactement 10 USD) ; relais ; contrôles ;
  **course en arrière-plan sous `wait`** ; arrêt des relais ; agrégateur ; épreuve anti-fuite sur le run ; recherche des clés.
  Un signal arrête la course par son PID, puis les relais ; agrégateur et recherche des clés tournent quand même (CLM-01).
- **Lecture** : seul l'agrégateur lit le dossier pour la trace publique. Les fiches restent dans le dossier du run (`donnees/`,
  exclu de la copie publique par `scripts/depot_expurge.py:51`) ; aucune fiche, aucun titre, aucun extrait n'est cité dans un
  registre, une passation ou un message.
- **Lecteur de la trace** : session-depot rapporte L1 à L4 tels que la trace les donne, avec les réserves.

## Critères de lecture gelés

| Critère | Issue | Lecture |
|---|---|---|
| L1 | `generation_terminee`, étapes protégées `jouee`, fusions `jouee` | démonstration **aboutie** |
| L1 | `generation_terminee`, fusions `retiree` | démonstration **aboutie sans fusion** (sacrifice d'A1, consigné) |
| L1 | `noeud` (C13) | démonstration **partielle** ; **L3 et L4 non calculés (O12)** : rien de ce qui a été mesuré n'est ouvert |
| L1 | `arret_motif_code` | démonstration **arrêtée**, motif codé rapporté ; **L3 et L4 non calculés (O12)** (CLM-10) ; aucune relance sans nouveau GO |
| L1 | `non_lance` | aucun appel de course ; cause rapportée (journal du lanceur) |
| L2 | tous comptes | rapportés tels quels ; un écart au tableau des appels attendus est rapporté et expliqué |
| L3 | parts et accord | **descriptifs** (n ≤ 13, aucun intervalle opposable) ; jamais un classement des proposeurs ni des juges |
| L4 | écarts | **rapportés comme réserve** : deux familles seulement, chaque fiche a un juge de sa propre famille ; fusion exclue ; jamais une mesure de complaisance |

**Symétrie (R4)** : déclenchent le même audit avant toute ligne de lecture, dans un sens comme dans l'autre : les deux juges
unanimes sur toutes les fiches (toutes notables, ou aucune) ; kappa égal à 1 ou au plus −0,5 ; zéro appel inexploitable avec des
sorties identiques d'un appel à l'autre ; toutes les fiches `concret` ou toutes `niveau_methode` ; dépense inférieure à 1 USD
ou supérieure à 9 USD. L'audit vérifie les journaux des relais (modèles servis, usages), le registre cumulé et l'absence de
réponse factice ; son résultat est une réserve écrite, jamais une correction des nombres.

## Liste d'arrêt

| Motif | Où il est codé | Effet |
|---|---|---|
| plafond de l'étape atteint (noyau) | `OrchestreV56.appel`, coupure | étape protégée « non mesurée (budget) », nœud C13 ; fusions retirées (sacrifiables) |
| plafond dur de l'étape refusé par le registre des commandes | registre cumulé ; `AdaptateurCommandeExterneNuitV2` | `ArretPlafondEtapeCommande` : arrêt de la course |
| garde cumulée (10 USD au barème) | registre cumulé ; adaptateur v2 | `ArretPlafondCumule` : arrêt de la course |
| plafond propre d'un relais (402) ou nombre d'appels (429) | relais Kimi (3 USD), relais Argon (7 USD) ; adaptateur v2 | `ArretPlafondRelais` : arrêt de la course |
| cumul au-delà de S17 | noyau (`CumulAuDelaDeS17`) | arrêt |
| coût lu au-dessus du pire cas réservé | commandes (`depassement_reserve`) ; adaptateur v2 | `ArretDepassementReserve` : arrêt de la course (CLM-02) |
| modèle servi différent | relais Kimi (502) → commande Kimi ; commande Argon ; adaptateur | `ArretModeleServiDifferent` : arrêt de la course |
| trois échecs consécutifs d'un rôle | `GenerationNuitV1.appel` (A3) | `ArretTroisEchecs` : arrêt de la course |
| débordement de la garde Kimi (S12) | `GenerationNuitV1._aiguiller` (M5) | `ArretDebordementKimi` : arrêt de la course |
| part d'appels inexploitables (A14) | noyau v56 | étape « non mesurée (technique) », nœud |
| signal reçu (TERM, INT, HUP) au lanceur | piège de `lancer-mini-course-v2.sh` → SIGTERM à la course → `ArretSurSignal` | arrêt propre, manifestes écrits, relais arrêtés par PID, trace et recherche des clés faites, code 130 |
| délai de 12 600 s | `timeout -k 120` | comme un signal (SIGTERM au Python), code 124 au journal |
| contrôle en échec | lanceur shell | aucune course (code 3) |
| canari, titre ou six mots d'une fiche dans la trace | agrégateur | trace refusée, rien d'écrit (code 3 de l'agrégateur, 7 du lanceur) |
| clé trouvée dans une sortie | `chercher_cles_v1.py` | alerte, code 6 |
| toute autre exception | partout | arrêt, sans repli ; motif au manifeste de fin |

## Gardes éprouvées et gardes non éprouvées (CLM-03, CLM-12)

**Éprouvées sur un cas sain et sur un artefact, sans réseau** (`test_gardes_mini_course_v1.py`, 16 essais ;
`test_gardes_mini_course_v2.py`, 14 essais ; `repetition_complete_v2.sh`, quatre essais par le vrai lanceur shell v2) :
registre cumulé (plafond cumulé, plafond d'étape, ligne illisible) ; commande Kimi (refus sans envoi au plafond cumulé, porte
incomplète, 502 « modèle servi » converti puis arrêt) ; commande Argon (modèle servi différent, refus du modèle, garde cumulée
puis `ArretPlafondCumule`, dépassement de réserve de bout en bout) ; relais Argon (402 au plafond, 429 au nombre d'appels puis
`ArretPlafondRelais`, 403 modèle non permis, refus de servir sans clé, refus de servir un collisionneur à empreinte différente) ;
adaptateur v2 (dépassement de réserve, modèle servi) ; échec d'Argon compté au pire cas
sans faux dépassement ; trois échecs consécutifs ; débordement de la garde Kimi ; configuration du
scénario B ; ligne de GO (montant, extension, **révocation lue à travers l'extrait**, GO autre que GO-2026-11-01-12) ; pièces
gelées ; spécification non scellée (moteur réel refusé, rien d'écrit) ; trace (canari, titre, six mots, liste blanche ; motifs
v2 ; L3 et L4 non calculés après un arrêt ; fusion exclue de L4) ; recherche des clés (clé plantée trouvée, variable absente
refusée) ; gardes R5 de la v56 rejouées à É0 (22 lignes) ; **piège du lanceur** (`kill -TERM` en pleine course) ; **contrôle en
échec** ; mode `repeter` refusé sans autorité factice.

**Non éprouvées** (réserves) : le format réel du flux de Moonshot et de la réponse de Gemini (imités, pas vus ici ; les mêmes
relais et la même `appeler_gemini` ont servi à l'épreuve du pont) ; le TLS réel des deux fournisseurs et le passage par le vrai
mandataire du conteneur ; les prix réels ; la borne de la réflexion d'Argon par `maxOutputTokens` ; le rapport réel jetons
d'entrée sur caractères ; les durées réelles ; le lancement avec la vraie spécification scellée (la répétition emploie une copie
de ce texte scellée dans le bloc-notes, et le vrai rapport de contre-lecture) ; la recherche des clés **dans le lanceur shell**
quand une clé est réellement présente (éprouvée dans l'outil, pas dans le lanceur) ; le refus d'une étape par la garde d'étape
du registre **au cours d'une course** (éprouvé dans le registre et dans la conversion du motif, pas dans une course).

## Répétition v2 (faite le 1er novembre 2026, 21:43 UTC, sans dépense)

Par le vrai `lancer-mini-course-v2.sh` (mode `repeter`), les vrais relais (relais Kimi vers `api.moonshot.ai`, `servir` donc
`appeler_gemini` vers `generativelanguage.googleapis.com`), derrière un faux mandataire TLS local et une autorité factice, clés
factices, vraie ligne de GO lue (`repetition_complete_v2.sh`) :
- essai 0 : mode `repeter` sans autorité factice : refusé (code 2), aucun dossier créé ;
- essai 1 : course complète, code 0 ; 68 appels au registre (Kimi 27, Argon 41 aux relais ; 2 contrôles, 66 de course) ;
  aucun dépassement ; trace « conforme » ; fiche factice dans `fiches.json` (2 fois), absente de la trace ; épreuve anti-fuite
  sur le run : tout vu ; aucune clé trouvée ; relais arrêtés, ports libres ;
- essai 2 : `kill -TERM` du lanceur après 12 appels : SIGTERM transmis à la course, bilan « signal SIGTERM reçu
  (ArretParSignal) », code 130 en 2 s, course et relais arrêtés, ports libres, trace écrite (`signal_recu`, L3 et L4 non
  calculés), épreuve anti-fuite et recherche des clés faites ; l'appel d'Argon tué en vol reste au registre à son pire cas
  (0,21 USD « engagés », côté prudent) ;
- essai 3 : contrôle d'Argon en échec (modèle servi faux) : code 3, aucune course, relais arrêtés.

**Défauts trouvés par la répétition et corrigés** (avant la répétition qui a réussi) :
1. une variable de mandataire **vide** en minuscules (`https_proxy=`) passée au relais Argon annulait `HTTPS_PROXY` pour urllib :
   `appeler_gemini` se connectait **en direct**. Lors du premier passage de la répétition (21:37 UTC, trois contrôles d'Argon),
   la connexion directe vers `generativelanguage.googleapis.com` a été refusée à la vérification TLS par l'autorité factice ;
   aucune requête HTTP n'a été écrite, aucune clé (factice) envoyée, rien de facturé. Sans effet dans la session réelle (les
   deux variables y sont posées), mais vrai défaut : le lanceur v2 ne transmet que les variables posées ;
2. sur un échec d'Argon, la commande v1 comptait l'arrondi à 8 décimales du relais, qui pouvait dépasser le pire cas réservé de
   moins de 1e-8 et marquer un faux dépassement de réserve (devenu un arrêt en v2) : `commande_argon_v56_nuit_v2.py` compte le
   pire cas réservé exactement (essai ajouté).

## Canaris

- **Une chaîne unique dans chaque consigne figée** (tirée par `SeedSequence(20261102, spawn_key=(clé,))`) : proposeur
  `MC1-PROPOSEUR-c518922b`, aiguilleur `MC1-AIGUILLEUR-b7f5a763`, juge `MC1-JUGE-9e367345`, lecteur `MC1-LECTEUR-30741b8c`,
  metteur `MC1-METTEUR-4ec962f1` ; elles doivent être **absentes de la trace**.
- **Une fiche factice** (`MC1-FICHE-FACTICE-67b8c480`) a été passée en mode simulé et devant le faux mandataire : la trace l'a
  exclue, l'agrégateur l'a vue quand on l'injectait.
- L'agrégateur rejoue sa garde à chaque exécution ; le lanceur v2 appelle aussi l'épreuve `--artefacts-sur-run` sur le run réel
  et l'écrit au journal (CLM-07).

## Trace agrégée

- Écrite par le seul agrégateur v2, dans le dossier du run : `trace-agregee-mini-course-v2.json`, compagnon `.sha256` (R6).
- **Liste blanche de clés et de valeurs** : comptes, statuts, coûts, appels, durées ; verdicts sous identifiant opaque (`v01`…)
  avec la famille de l'auteur, l'origine, et par juge sa famille, « même famille », notable, X ; aucun texte libre (un nom
  d'exception, lettres seules, est la seule chaîne non énumérée).
- **Contrôle par programme** : refus si la trace contient un canari, un titre de fiche ou une suite de six mots tirée d'une fiche.
- La trace n'est copiée vers `docs/notes/mini-course-kimi-argon-v1/` qu'après ce contrôle, par session-depot, sous un nom neuf.

### Pièces gelées

| Pièce (chemin depuis la racine du dépôt) | SHA-256 | Rôle |
|---|---|---|
| `donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/configuration-mini-course-kimi-argon-v2.json` | `4ae5a1e0947d44c1a08548d1b0197bfd96a2264f455189713b06183b2bc83108` | configuration figée v2 (scénario B ; commande d'Argon v2) |
| `donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/pieces/consigne-proposeur-mini-course-v1.md` | `98185e70f5d4bd3f0574b7517858efbec982d6decea0e5493da6abe12e9607b1` | consigne figée du proposeur |
| `donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/pieces/consigne-aiguilleur-mini-course-v1.md` | `4b15b31add9fe8e3ae5a18a309fdc9a7165da3be0533c5240dd9854ba08e14e9` | consigne figée de l'aiguilleur |
| `donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/pieces/consigne-juge-mini-course-v1.md` | `df57bc9117e85b6a032355159a84451c4fe60a5c44793c5986ac6b1a89c45bd9` | consigne figée des juges |
| `donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/pieces/consigne-lecteur-mini-course-v1.md` | `016789aeb9fc4177d865634882e1e5bc18053d0a16b72ccc83c7abbc6fbcb636` | consigne figée des lecteurs d'étiquettes |
| `donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/pieces/consigne-metteur-mini-course-v1.md` | `95b92e325ca95ded574073db8d13dcc8886c475d30dd01317c31fc40b96609e4` | consigne figée du metteur en fusion |
| `donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/pieces/concepts-mini-course-v1.json` | `036de84a297f5c3e402caeb9069e4d8eb9d0d3ec4ef86a5fc6a039022c8b3874` | liste fermée des concepts (bras basique) |
| `donnees/mini-course-kimi-argon-v1/orchestrateur/pole/course2_nuit_v1.py` | `b0506f7eb8ed384d0284b6b3335d93f31fb67c040fa53a932043ab44f1d33286` | génération sans passe tableau, liste d'arrêt (v1) |
| `donnees/mini-course-kimi-argon-v1/orchestrateur/pole/course2_nuit_v2.py` | `5d15660eca9f23b9480cb6bf7a05379859255294d377652231d944170fe69032` | adaptateur v2 : dépassement de réserve et plafonds hors noyau = arrêt |
| `donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/lancer_mini_course_v2.py` | `7a4d1a8a25efdb4020c1e8e57222b2bc1609e5b8ec4d5463bc63d48c3d22720e` | lanceur Python v2 (gardes, moteur réel) |
| `donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/lancer-mini-course-v2.sh` | `7b4374f01b9e76fff93bd029dc444ac899fba890d4d8a9b79ccacb6f03e772df` | lanceur shell v2 (course sous wait, piège, relais 3 et 7 USD) |
| `donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/commande_kimi_v2.py` | `644dbb39003f234db7b5fc295c6b061a0e84720e01ba08322ae1fe7936d9dcbe` | commande externe de Kimi |
| `donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/commande_argon_v56_nuit_v2.py` | `221df610681ed47bf66fbfef21d583006aa3e09a3147e22227faacd98622b851` | commande externe et relais d'Argon (v2) |
| `donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/registre_depense_cumulee_v1.py` | `8ba92066b358ffb8206dea9e70251388c30620484fab1ac578778d9f21e578ff` | garde cumulée au pire cas |
| `donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/trace_agregee_mini_course_v2.py` | `224b0003b38cb33a2de2ba071b4540ecf955598cff2677df10f8b99498eaa3db` | agrégateur v2 de la trace publique |
| `donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/chercher_cles_v1.py` | `5d6f82fc5cc95f9998877852c08835b83df1ba572597303f447cb983cf97cf61` | recherche des clés (valeurs lues dans l'environnement) |
| `donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/EMPREINTES-orchestrateur-v56-copie-v1.txt` | `3c72e4aae6abfdf177776d9fcb177569e3bc156daa7edaf796f33db286c8565b` | copie de l'orchestrateur v56 (archive 29b1b38c…) |
| `docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v3.py` | `d54ed2bce54f5c89e9f078d1a03b5d8159894d6565ae560c3601c1e63ca76239` | relais Kimi local |
| `donnees/espece-seule-v1/collisionneur_v7.py` | `c9725f025407c3ece3e8c16d19cfdfdec078f084a811f0a3b6ea3209be5d98dc` | appeler_gemini (Argon) |
| `.claude/hooks/garde_calcul.py` | `84512d4a1bef0403668000942cf5f5d383aab280bf5a58f6aec328e77f807d59` | garde du dépôt : lecture du registre des GO (CLM-08) |

## Réserves

- **Deux familles seulement** : le juge d'une autre lignée n'est pas imposé par le code ; chaque fiche a un juge de sa propre
  famille ; L4 n'est qu'une réserve.
- **Borne de 10 USD au barème supposé d'Argon**, sous les hypothèses dites plus haut ; facture réelle à relire.
- **Contrôles hors S17** : leurs ≈ 0,01 USD sont dans le registre cumulé, pas dans le plafond du noyau ; le registre et la somme
  des plafonds des relais (10 USD) sont les bornes qui lient.
- **Plafonds souples** des étapes protégées (règle d'A1 du brouillon 10) : bornés en pratique par le registre, les plafonds des
  relais et ceux de chaque appel.
- **Causes d'arrêt prévisibles** : A14 sur l'appel unique de chaque proposeur (une proposition inexploitable donne un nœud) ;
  **troncatures** (CLM-11) : appels courts d'Argon à 4 000 jetons de sortie réflexion comprise (contrôle à 999 ; le devis
  supposait 1 500 en moyenne), appels courts de Kimi à 16 000 ; toute troncature rend l'appel inexploitable (A3, A14, nœud ou
  arrêt), et un contrôle tronqué empêche la course ; plafond du relais Argon (7 USD) au-dessus de l'estimation d'Argon au devis
  (≈ 4,7) mais sous son pire cas × 1,5 (≈ 7,0) : `ArretPlafondRelais` possible.
- **Paramètres du bras « basique »** (exposant 8,5 ; décalage 0,05) : valeurs d'essai du code v56, sans étalonnage.
- **Étiquettes interdites** (A4, mode préfixe, fiche exclue) : une fiche légitime qui écrit « fusion » ou un nom de fournisseur
  est exclue et comptée.
- **Clé d'Argon par un relais local** (`servir`) : le noyau v56 interdit tout nom de clé dans son environnement ; limite connue
  de `/proc/<pid>/environ` des relais, conteneur à un seul utilisateur ; la recherche des clés hérite des clés par son
  environnement (jamais en argument).
- **Lecture du registre des GO** : la lecture de la v56 refuse les lignes d'extension d'autres GO (R-389) ; le lanceur lit le
  registre par la garde du dépôt (gelée), puis relit la seule ligne citée, avec ses révocations, par `verifier_go_v56`.

## Contre-lecture

- Contre-lecteur : sous-agent neuf, auteur d'aucune pièce, 1er novembre 2026 (aucun appel payant ni réseau).
- Brouillon relu : `preregistrement-mini-course-kimi-argon-v1.md`, `2b73102b58a41e6913ad46396c5e9c1a36a9dbbea02b0c9184c952202cb7e487`.
- Rapport : `docs/notes/mini-course-kimi-argon-v1/contre-lecture-mini-course-kimi-argon-v1.md`,
  empreinte `a35eac7076c3be63f29ad67e3cebe0e7c1d785e3d5b0a106e18243c7e73cfac0` (scellé).
- **Verdict : « scellable après corrections »** (un bloquant, trois majeurs, neuf mineurs).

| Constat | Traitement |
|---|---|
| CLM-01 (bloquant) piège inopérant pendant la course | **appliqué** : `lancer-mini-course-v2.sh` (course en arrière-plan sous `wait`, SIGTERM à la course par son PID, relais arrêtés par PID, agrégateur et recherche des clés après un signal, code 130) ; éprouvé par `kill -TERM` du lanceur en pleine course (`repetition_complete_v2.sh`, essai 2) |
| CLM-02 garantie conditionnelle ; dépassement non arrêtant | **appliqué** : borne reformulée (barème supposé, hypothèses, facture à relire) ; `ArretDepassementReserve` (`course2_nuit_v2.py`) ; option « entrée à caractères / 2 » ou plafond cumulé à 9,5 USD **non appliquée** : remplacée par la somme des plafonds des relais à 10 USD (CLM-05) |
| CLM-03 affirmation R5 inexacte | **appliqué** : essais ajoutés (14) et section « Gardes éprouvées et gardes non éprouvées » avec la liste exacte de ce qui ne l'est pas |
| CLM-04 nom du rapport | **appliqué** : `lancer_mini_course_v2.py` et le lanceur shell v2 attendent `contre-lecture-mini-course-kimi-argon-v1.md` (aucune copie nécessaire) |
| CLM-05 plafonds des relais | **appliqué** : Kimi 3 USD, Argon 7 USD |
| CLM-06 clé en argument de `grep` ; outils hors `env -i` | **appliqué** : `chercher_cles_v1.py` (valeurs lues dans l'environnement) ; agrégateur, registre, état des relais sous `env -i` |
| CLM-07 épreuve anti-fuite sur le run réel | **appliqué** : appelée par le lanceur v2, sortie au journal |
| CLM-08 garde du dépôt non gelée | **appliqué** : `.claude/hooks/garde_calcul.py` dans les pièces gelées ; le lanceur v2 exige sa présence dans la table |
| CLM-09 motifs mal étiquetés | **appliqué** : motifs distincts (`plafond_cumule`, `plafond_etape_commande`, `plafond_relais`, `depassement_reserve`) ; le délai est dit « `signal_recu` » en L1, code 124 au journal |
| CLM-10 arrêt et verdicts | **appliqué** : « L3 et L4 non calculés (O12) » en L1 et dans la trace (`l1.l3_l4`) |
| CLM-11 troncatures prévisibles | **appliqué** : réserve ajoutée ; plafonds de sortie **inchangés** (ceux du devis) |
| CLM-12 répétition incomplète | **appliqué** : la répétition v2 passe par le vrai lanceur shell v2 et le vrai chemin `servir` (et `appeler_gemini`), derrière un faux mandataire TLS et une autorité factice ; ce qui reste non vu est listé |
| CLM-13 fusion dans L4 | **appliqué** : fusion exclue de L4 |
| (répétition v2) mandataire vide, arrondi du coût d'un échec d'Argon | **corrigés** : lanceur v2 et `commande_argon_v56_nuit_v2.py` ; configuration v2 (seule la commande d'Argon change) ; voir « Répétition v2 » |
