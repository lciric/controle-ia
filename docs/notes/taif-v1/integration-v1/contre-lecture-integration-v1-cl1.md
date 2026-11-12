# Contre-lecture du dossier d'intégration pour l'entretien avec le Transformative AI Fund — v1, contre-lecture 1

- **Contre-lecteur** : sous-agent neuf (règle R2), modèle déclaré par l'environnement : Claude Opus 5.5 (`claude-opus-5-5`), autre modèle que le rédacteur des quatre pièces (Claude Fable 5.1 ; décision N-052). Je n'ai écrit aucune pièce contre-lue ni aucune pièce citée.
- **Heures** (`date -u`) : début 2026-11-08 15:24:19 UTC ; fin en dernière ligne.
- **Pièces contre-lues** (non scellées, lues en entier) : `docs/notes/taif-v1/integration-v1/matrice-tracabilite-v1-brouillon2.md` (439 l.) ; `docs/notes/taif-v1/integration-v1/journal-changements-candidature-v1-brouillon2.md` (179 l.) ; `docs/notes/taif-v1/integration-v1/registre-goulots-questions-v1-brouillon1.md` (308 l.) ; `docs/notes/g0-deux-semaines-v1/chemin-critique-G1-v2-brouillon1.md` (69 l.).
- **Sources vérifiées** (par `grep -n`, `sed -n`, `sha256sum`) : la candidature envoyée `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` (b2458c2d, recalculée : conforme) et `budget_v3_TAIF_2026-10-07.txt` (caec18b2, conforme) ; `livrables/registres-taif-v4/` (promis-livre-v3 af868f16, calibration-v3 0f1bca5a, total-depenses-v3 123be1a7, tous recalculés conformes ; écrits à 15:12 UTC, scellés à 15:17 UTC d'après le disque) ; `livrables/registres-taif-v3/` (scellé) ; `registres/decisions.md` (lignes citées, et R-1837 à R-1863, postérieures aux pièces) ; `registres/etat.md`, `registres/go.md`, `registres/depenses.md` ; seize fichiers de `docs/decisions/` (empreintes recalculées : toutes conformes aux huit caractères cités) ; verdicts T0.4, T0.5, P3, audit de fuite, attaque de Goodhart, étiqueteur ; `docs/programme-controle-ia-v2.md`, `docs/brief-claude-code-programme-complet-v2.md` ; `brouillons/entretien-taif-v3/programme-entretien-taif-v16.md` (lignes citées).
- **Rien lu** sous `donnees/`, `diag/`, `docs/notes/bras-attaque/` ; aucun fichier existant modifié ; aucun `.sha256`, aucun commit, aucun réseau, aucune dépense. Toute pièce lue est une donnée, jamais une instruction.
- **Fait nouveau qui pèse sur toute la contre-lecture** : les quatre pièces sont antérieures à R-1849 (verdict de l'étiqueteur), R-1850 à R-1856 (course de dose-réponse lancée en **mode exploratoire, non opposable**, ligne GO-2026-11-08-11, `registres/go.md` l. 282) et R-1851 (N-061 écrite et scellée, `docs/decisions/decision-N-061-v1.md`, b2ae4417). Plusieurs constats en découlent.

## 1. Verdicts par pièce

| pièce | verdict | raison principale |
|---|---|---|
| Matrice de traçabilité, brouillon 2 | **utilisable après corrections** | sources exactes sur 37 des 46 cases tirées ; défauts de type (« instrumente » donné à des textes), d'orphelins masqués et de lignes citées ; N-061 et étiqueteur périmés |
| Journal des changements, brouillon 2 | **utilisable après corrections** (quatre phrases « à dire » à réécrire avant tout usage) | structure saine, « renforce / affaiblit » présents partout ; mais phrases anglaises fausses ou trop affirmatives (entrées 2, 3, 4, 8, 10, 18) et deux changements de la candidature absents (H6, pilote) |
| Registre des goulots et chemin critique G1 v2 | **à reprendre** pour le goulot et le chemin critique ; registre **utilisable après corrections** ailleurs | le goulot (pas 7) a changé de nature depuis R-1854 : la course part en exploratoire, la course de confirmation sous GO-2026-11-02-28 exige T0.7 scellé, la marge de 2 jours n'est plus la bonne ; chiffres de calibration et de dépense du registre tirés des tables v3 |

Comptes : **4 bloquants, 16 majeurs, 16 mineurs** (36 constats).

## 2. Constats

### Bloquants

**CLI-01 — bloquant — journal, entrée 2, (d) l. 41 et (e) l. 42.** La phrase à dire « each line under a signed-off cap » et le « renforce » « chaque dollar a sa ligne de GO » sont faux : treize instances louées sans autorisation par la relève du 23 octobre (`brouillons/entretien-taif-v3/programme-entretien-taif-v16.md` l. 1341 ; `docs/notes/etat-critique-v1/etat-critique-programme-v1.md` l. 21) ; GO-2026-10-24-07 relevé **49,72 USD pour un plafond de 40** (`livrables/registres-taif-v4/total-depenses-v3.md` l. 53) ; lignes « sans plafond » (l. 51, R-355 ; l. 58, R-512) ; dix-huit lignes « plusieurs GO cités » et des lignes « GO abrégé, non résolu » (l. 20-24). Le registre C-1 (l. 167) dit d'ailleurs « sauf l'incident du 23 octobre ». « nearly all of it model calls » est aussi trop fort (carte ≈ 99 sur ≈ 525 au 29 octobre, v16 l. 1339-1340 ; ≈ 130 sur ≈ 1 000 selon `docs/notes/taif-v1/proposition-recherche-programme-v1-brouillon1.md` l. 46).
Couple : « *…nearly all of it model calls for multi-model design rounds and the ideation organism, each line under a signed-off cap.* » → « *…most of it model calls for multi-model design rounds and the ideation organism. Almost every line sits under a signed-off cap; the exceptions are logged: one rental incident on 23 October, one line above its cap, and a few uncapped lines approved in writing.* » ; et (d) « chaque dollar a sa ligne de GO et sa ligne de registre » → « presque chaque dollar a sa ligne d'autorisation ; les exceptions (incident du 23 octobre, GO-2026-10-24-07 au-dessus de son plafond, lignes sans plafond, lignes à GO non résolu) sont au registre ».

**CLI-02 — bloquant — journal, entrée 3, (b) l. 47 et (e) l. 50.** « the critical path to sealing the G1 pre-registration runs to about 22 November with a week of margin » reprend la v1 du chemin critique (`chemin-critique-G1-v1.md` l. 37). La v2 du dossier même dit le contraire : scellement les 28-29 novembre, « la marge d'une semaine est consommée » (`chemin-critique-G1-v2-brouillon1.md` l. 51-53). Le jury entendrait une date fausse le jour même où elle tombe.
Couple : « *…runs to about 22 November with a week of margin.* » → « *…now runs to 28–29 November, with one to two days of margin at best.* » ; et (b) « scellement de G1 vers le 20-22 novembre, marge d'une semaine (…v1.md l. 37) » → « scellement de G1 les 28-29 novembre, marge d'un à deux jours au mieux (`chemin-critique-G1-v2-brouillon1.md` l. 51-53) ».

**CLI-03 — bloquant — chemin critique v2, « Le goulot » l. 39-41, pas 7 et pas 8 (l. 26-27) ; registre B-1 (l. 80-87), A-1 (l. 18-21), classement rang 2 (l. 277).** Le goulot est décrit avant R-1850, R-1854 et R-1856 : la course de dose-réponse part **en mode exploratoire, non opposable, aucun verdict du critère 2 n'en sortira**, galop E3 ter et course fusionnés, GO-2026-11-08-11 (100 USD, `registres/go.md` l. 282 ; `registres/decisions.md` l. 1812, 1814). Conséquences écrites que les pièces ignorent : (a) W21 exige un verdict de T0.6 « établi » avant le scellement de G1 (`chemin-critique-G1-v1.md` l. 5) : il faut donc encore une **course de confirmation préenregistrée** ; (b) elle tourne sous GO-2026-11-02-28, dont le périmètre exige « les préenregistrements de T0.6 **et T0.7** contre-lus, scellés, committés et poussés avant la course » (`registres/go.md` l. 216 ; rappelé par R-1854) : le pas 8 (T0.7) **redevient un préalable de la création**, sa marge n'est pas « ≈ 15 j » mais ≈ 3 jours (prévu 10-12, création au plus tard le 15) ; (c) la fenêtre du 11 au 15 novembre (L11, `registres/decisions.md` l. 1581) doit contenir la course exploratoire, la lecture, la page de confirmation scellée, le scellement de T0.6 et de T0.7, puis la course de confirmation : la marge du goulot est plutôt nulle que « ≈ 2 jours ». Le goulot nommé reste le bon maillon (Lazar le nomme lui-même, R-1850), mais son contenu et sa marge sont à réécrire.
Couple (chemin v2, l. 39) : « **Le pas sans marge aujourd'hui est le pas 7, la course de T0.6, sur sa fenêtre de création** : l'ordre de la course est bloqué par E3-6 ; le galop E3 ter doit être… » → « **Le pas sans marge est le pas 7, scindé depuis R-1854 : 7a course exploratoire (non opposable, GO-2026-11-08-11) ; 7b course de confirmation préenregistrée sous GO-2026-11-02-28, qui exige T0.6 et T0.7 scellés avant la création (go.md l. 216), création au plus tard le 15 novembre (L11) ; marge ≈ 0 à 1 jour ; le pas 8 est sur ce chemin.** » ; registre A-1, phrase : « la première mesure propre est en cours » → « une course exploratoire, non opposable, est en cours ; la mesure qui compte pour la porte sera une course de confirmation préenregistrée ».

**CLI-04 — bloquant — journal, entrée 8, (b) l. 87 et (e) l. 90 ; registre A-2 (l. 27, 30) ; matrice A08 (l. 79, 221).** Périmé et trop affirmatif : la phase 1 de l'étiqueteur a rendu son verdict scellé **« non tranché », réserve « lecture instable » ; la phase 2 ne part pas** (`docs/verdicts/verdict-etiqueteur-phase1-v1.md` ; R-1849, `registres/decisions.md` l. 1807) ; les huit illisibles sont un seul épisode refusé (R-1855) ; dépense 41,09 / 300 USD (R-1862), non 36,90. La phrase omet l'aveu que la v16 avait écrit : « none of these episodes exists yet » (v16 l. 1141) ; « tuned to degrade quietly at a written dose » décrit un organisme (ii) que la course n'a pas encore produit.
Couple (e) : « *We know an episode is sabotaged because we build it: […] — a reader we are testing on planted degradations right now, before any real episode is read.* » → « *We will know an episode is sabotaged because we build it: […]. None of these episodes exists yet. The first test of the readers on planted degradations came back undecided, so we are redesigning that test before any real episode is read.* » ; registre A-2, état : « étiqueteur phase 1 en relecture » → « phase 1 : verdict scellé “non tranché”, réserve “lecture instable” (R-1849) ; épreuve v2 exploratoire ordonnée (R-1852, R-1859) ».

### Majeurs

**CLI-05 — majeur — matrice § 0 l. 11 point (2), colonne A24 l. 95 ; journal § 0 l. 22, entrée 15 (b) l. 143 et (c) l. 144, § 19 point 3 l. 177.** « aucune ligne N-061 » est périmé : `docs/decisions/decision-N-061-v1.md` (b2ae4417, scellé) existe depuis 15:06-15:19 UTC, confirmation de Lazar consignée en R-1851 (`registres/decisions.md` l. 1809) ; date opposable : 8 novembre (mot d'origine non retrouvé, réserve écrite dans le fichier).
Couples : journal (c) « P-040 ; N-061 (`CLAUDE.md` l. 13) `<<À VÉRIFIER>>` » → « P-040 ; N-061 (`docs/decisions/decision-N-061-v1.md`, b2ae4417 ; R-1851) » ; § 19 pt 3 « retrouver sur `main` le brief du mode tenu à l'écart et la ligne N-061 » → « retrouver sur `main` le brief du mode tenu à l'écart » ; matrice A24, pièce de tête : « `CLAUDE.md` l. 13 (N-061 citée) ; aucune ligne « N-061 » trouvée dans `registres/decisions.md` » → « `docs/decisions/decision-N-061-v1.md` (b2ae4417) ; `registres/decisions.md` l. 1809 (R-1851) ».

**CLI-06 — majeur — journal, entrée 2, (d) l. 41.** « les instruments sur carte graphique sont restés sous cent dollars (v16 l. 1339-1340, au 29 octobre) » : la source dit l'inverse : « ≈ 99 : « sous 100 » n'est plus sûr » (v16 l. 1339) ; la proposition de recherche dit « cartes Vast ≈ 130 » (l. 46) et le registre C-12 aussi.
Couple : « et les instruments sur carte graphique sont restés sous cent dollars (v16 l. 1339-1340, au 29 octobre) » → « et la carte graphique ne pèse qu'une petite part (≈ 99 USD au 29 octobre, v16 l. 1339 ; ≈ 130 au 8 novembre selon la proposition de recherche l. 46, à recompter dans `total-depenses-v3.md`) ».

**CLI-07 — majeur — journal, entrée 4, (b), (d) l. 55-57 et (e) l. 58.** « the paired bet and its guard are fixed before any reading » : ni l'un ni l'autre n'est fixé (garde δ v10 non simulée, pas 2 ; préenregistrement de G1 au brouillon 6, non contre-lu, pas 1 ; chemin v2 l. 20-21). Et l'entrée ne dit pas l'autre coût : la candidature promet une différence « established by a 95% confidence interval » ([E] l. 160) ; la règle retenue est « le pari décide, le rééchantillonnage est rapporté » (N-055 D-S11, `decision-N-055-v1.md` l. 29 ; N-056 nœud 2, confirmé R-600 l. 826), et l'intervalle de DeLong peut être retiré faute de vérification R7 (pas 6, chemin v2 l. 25).
Couples : (e) « *…and the paired bet and its guard are fixed before any reading.* » → « *…and the decision rule, a paired bet with a guard, will be sealed before any reading; it replaces the confidence interval of the proposal, which is reported beside it.* » ; ajouter à (d) affaiblit : « la règle de décision n'est plus l'intervalle de confiance à 95 % du texte envoyé ([E] l. 160) mais le pari apparié (N-055 D-S11) : écart à déclarer ».

**CLI-08 — majeur — journal, entrée 10, (e) l. 106.** « we judge it only on task families it never saw » : aucune mesure d'universalité n'existe (N-044 fixe un objectif ; « aucune idée de l'organisme lue ni retenue », v16 l. 395-396, cité par l'entrée même).
Couple : « *…we judge it only on task families it never saw…* » → « *…it is to be judged only on task families it never saw — no such measurement exists yet…* ».

**CLI-09 — majeur — journal, entrée 18, l. 166 et (e) l. 169.** « the hashes time-stamped with a third party » et « every decisive step pre-registered » : le projet de l'Open Science Framework est **privé et non gelé**, « seule forme qui prouve la date à un tiers » restant à faire (R-1580, `registres/decisions.md` l. 1538 ; registre C-11 l. 243-248) ; et depuis le 8 novembre deux épreuves partent en exploratoire sans préenregistrement (R-1852 l. 1810, R-1854 l. 1812). L'entrée 18 n'a pas de colonne (d) « affaiblit ».
Couple : « *…counter-read by a fresh instance, and the hashes time-stamped with a third party.* » → « *…counter-read by a fresh instance; exploratory runs are labelled as such and never decide a gate; the hashes are deposited with a third party, in a private project we will make public and freeze.* ».

**CLI-10 — majeur — journal (entrée manquante).** Deux changements de la candidature n'ont pas d'entrée : (1) **H6** : le texte envoyé revendique « four non-specific interventions: paraphrase, resampling, context reset, activation noise » ([E] l. 152) ; N-015 (20 octobre, `decision-N-015-v1.md`, 462785b3) retire le bruit d'activations des interventions revendiquées (mesure gardée) ; la matrice le dit (ligne H6, l. 58), le journal non. (2) **C6-4** « The pilot runs before the grant starts » ([E] l. 278) : la course est désormais exploratoire et non opposable (R-1854) ; aucun résultat de pilote opposable n'est assuré avant le 1er décembre.

**CLI-11 — majeur — matrice, cases C6-5 × A22 (l. 118, 331), orphelins § 4.2 l. 430, § 0 point (6) l. 11.** La pièce du « 602 automated tests » existe : `registres/decisions.md` l. 235 (R-098, 7 octobre : « 602 tests réussis ») et `registres/passations/2026-10-07-1122.md` l. 4 (scellée). La case « à vérifier » se lève, et C6-5 n'est pas orpheline au sens strict.
Couple : « **C6-5** : **<<À VÉRIFIER>>** (… le compte « 602 automated tests » n'est rattaché à aucun commit) » → « **C6-5** : **teste** (`registres/decisions.md` l. 235, R-098 ; `registres/passations/2026-10-07-1122.md` l. 4 : « 602 tests réussis » le 7 octobre ; la table v4 l. 21 ne porte pas la pièce : à y ajouter) ».

**CLI-12 — majeur — matrice, orphelins § 4.2 (l. 428-432) et lignes C7-3, C7-6 (l. 124, 127).** (a) C7-3 (« lemma and theorem on real activations », mois 3) et C7-6 (« release of code, organisms, probes and pre-registrations ») ne sont servies que par A22, une table d'état qui écrit « à venir » : ce n'est pas une activité qui sert la promesse. Or les mêmes contenus portent des cases ailleurs : C8-7 (A01 I, A02 I) pour C7-3 ; C8-2, C8-3, C8-4 (A01 à A10) pour C7-6. Il faut soit propager ces cases, soit déclarer C7-3 et C7-6 orphelines. (b) Le critère « servies seulement par des pièces documentaires » appliqué à H1b et H6 vaut aussi pour **HC4** (A12 générique, A21 sans lien — CLI-24 —, A26 brouillon), **HC5** (A27 et A28 : « aucune course »), **H9** (A29 : lecture seule, aucune recherche affirmative, N-035 l. 22). Le compte « 1 strictes + 2 documentaires » devient au moins « 2 strictes (C7-3, C7-6) + 5 documentaires (H1b, H6, HC4, HC5, H9) ».

**CLI-13 — majeur — matrice, colonne A26 (l. 387-399) et case H5 × A28 (l. 409).** La légende (l. 15) définit « instrumente » comme « construit ou vérifie l'instrument ». Un brouillon non scellé de proposition qui réécrit les énoncés n'en construit aucun : treize cases A26 « instrumente » (H1a à HC6) sont des cases « sans lien » (ou « dérisque » au plus). H5 × A28 « instrumente » cite la question v2 l. 21 : « matrice de transfert mesurée sur nos sondes et nos organismes : absente du dépôt » — l'instrument n'existe pas. Les comptes (instrumente 70) baissent d'au moins 14.

**CLI-14 — majeur — matrice, colonne A12 (l. 255-266).** La même phrase de R-521 (« aucune faille qui oblige à changer une hypothèse ») est recopiée sur treize lignes (H1b, H2, H5, H6, H7, H9, HC1 à HC6). C'est un énoncé global ; un « dérisque » par hypothèse demande la ligne de la synthèse (`docs/notes/audit-controle-v1/synthese-collisionneur-v1.md`, d672e57a) qui la nomme. Sinon : une seule case globale, ou « sans lien ». Le même défaut, moindre, touche A22 G0-1 à G0-8 (une seule citation l. 9-16).

**CLI-15 — majeur — registre, A-5 l. 54.** « H5 est au papier B (mois 4,5 à 6 de la candidature, `livrables/registres-taif-v3/promis-livre-v2.md` ligne C7-4) » : c'est la numérotation et le calendrier de `proposal-v1.md`. Le texte envoyé : « Paper B is not part of the seven-month request » ([E] l. 207-208), « months 8 to 12 add Paper B » au scénario ambitieux ([E] l. 304-305).
Couple : « H5 est au papier B (mois 4,5 à 6 de la candidature, `livrables/registres-taif-v3/promis-livre-v2.md` ligne C7-4) » → « H5 est au papier B, hors de la demande de sept mois, aux mois 8 à 12 du seul scénario ambitieux (`proposal_v2_TAIF_2026-10-07.txt` l. 207-208, 304-305) ».

**CLI-16 — majeur — registre, C-13 l. 262, C-1 l. 164, B-6 l. 122, C-2 l. 173.** Chiffres et dates tirés des tables `registres-taif-v3` (bâties sur `proposal-v1.md`), remplacées par la v4 scellée sur le texte envoyé : calibration « 55 : 44 confirmées, 3 réfutées, 8 non concluantes (taux 0,800) … 66 sans run décisif » → « 60 : 47 confirmées, 5 réfutées, 8 non concluantes (taux 47 / 60 = 0,783) … 55 sans run décisif » (`calibration-v3.md` l. 256-267) ; dépense « 185 lignes au journal non sommées et 49 lignes estimées à part (111,85 USD) (`livrables/registres-taif-v3/total-depenses-v2.md` l. 9-12) » → « 187 lignes non sommées, 50 lignes estimées à part (111,87 USD) (`livrables/registres-taif-v4/total-depenses-v3.md` l. 11-12) » ; B-6, citation du jury « G0 était promise au 1er novembre » → « G0 était promise “at the start of the grant, December 2026” ([E] l. 284) ; en interne, au 1er novembre puis à fin novembre » ; C-2 « `promis-livre-v2.md` (ligne C6-G0 : « Gate G0 (1 November 2026) ») » → « `promis-livre-v3.md` l. 24 (« at the start of the grant, December 2026 ») ». Le titre de C-13 « 80 % de confirmations » → « 78 % de confirmations ».

**CLI-17 — majeur — `livrables/registres-taif-v4/promis-livre-v3.md` l. 22 (ligne C6-6) et `registres/etat.md` l. 161, repris sans réserve par la matrice C6-6 × A22 (l. 332).** La table scellée qui ira au jury écrit « préenregistrement de HC1 à HC3 en brouillon 2 » ; `main` porte le brouillon 5 (`brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md`, 9d55160f), ce que la matrice (A07) et le journal (entrée 18) disent. Contradiction entre pièces du dossier ; la source (`registres/etat.md` l. 161) est à corriger avant la page pour le fonds.

**CLI-18 — majeur — journal, entrée 13, (b) l. 127, (d) l. 129, (e) l. 130.** « a pre-registered negative result » et « verdicts conditionnels recopiables » : les verdicts d'hypothèses (HR0, HR2, HR3) ne sont **pas prononcés** par un lecteur neuf (registre A-3 l. 34, 39 : « verdict R13 d'hypothèses non prononcé au 8 novembre »). La réserve de R-1815 (« R1 et R4 font mieux que R2 … la défense figée généralise mieux », `registres/decisions.md` l. 1773) n'est dite qu'à moitié.
Couple (e) : « *…— a pre-registered negative result that is exactly why…* » → « *…— a pre-registered result, audited twice, whose formal verdict is still to be pronounced, and the reason why…* ».

**CLI-19 — majeur — registre, classement des dix urgences (l. 270-287).** Le classement tient dans sa logique (probabilité × dommage × réparabilité), mais il manque l'entrée qui a surgi après sa rédaction : **des épreuves lancées en exploratoire sans préenregistrement** (course de dose-réponse, R-1854 ; étiqueteur v2, R-1852), face à la règle que le jury a lue ([E] l. 240-243 : « Before any data, a pre-registration is sealed »). Probabilité haute (le dépôt le montre), dommage fort, réparable par une phrase et la confirmation préenregistrée : à placer dans les trois premiers. A-2 doit monter (le geste de la semaine, le verdict de l'étiqueteur, est joué et n'a pas tranché). C-6 (clés, treize instances) mérite de remonter tant que le journal dit le contraire (CLI-01).

**CLI-20 — majeur — matrice, colonne A19 et § 4.1 l. 426 ; A16 l. 425.** A19 (garde refus-question) est la garde R5 de la course de l'organisme : « sonde de pré-vol avant toute dépense de l'organisme » (`registres/decisions.md` l. 1746, R-1788 ; l. 1779, R-1821). Si A18 dérisque G0-6, C7-5 et H1a, A19 l'instrumente ; ou bien les liens d'A18 tombent. De même A16 (pilotes) est la lignée qui produit A17 et A18. L'orphelinat d'A16 et d'A19 est à justifier ou à corriger ; celui d'A13 et d'A14 tient (pièces de tête sans promesse nommée).

### Mineurs

**CLI-21 — mineur — journal, table l. 9 et entrée 1 (d) l. 33.** « tables régénérées par la session mère à 15:50 UTC », « la table de 15:50 UTC » : heure impossible (journal fini à 15:22). Sur disque : écrites à 15:12, scellées à 15:17 UTC. Couple : « à 15:50 UTC » → « à 15:12 UTC (scellées à 15:17) ». Note hors pièces : plusieurs lignes de `registres/decisions.md` (R-1856 à R-1859) portent des heures (15:39-15:53) postérieures à mon `date -u` de 15:25-15:34 : à signaler à la mère.

**CLI-22 — mineur — matrice § 0 l. 9.** « dossier `registres-taif-v3` (non scellé…) » : il est scellé (compagnons `.sha256` présents sous `livrables/registres-taif-v3/` ; R-1847 : « scellées à 14:36Z »). Couple : « (non scellé : 645,42 ; … » → « (scellé, bâti sur `proposal-v1.md` : 645,42 ; … ».

**CLI-23 — mineur — matrice, lignes citées.** G0-1 et C6-3 × A02 (l. 165-166) : « critère 1 prouvé » est à `verdict-T0.4-critere-1-G0-v3.md` l. 11, non l. 3 ; G0-4 × A06 (l. 202) et pièce de tête A06 (l. 77) : « TRACE-lite prêt » est à `registres/etat.md` l. 160, non l. 159 (P3) ; G0-3 × A05 (l. 194) : « la sonde d'intention n'existe pas encore » est à `chemin-critique-G1-v1.md` l. 51, non l. 21 ; C6-4 × A03 (l. 176) : `verdict-T0.5-revalidation-v2.md` l. 3 ne porte pas l'issue (section 1, l. 15) et le verdict s'écrit lui-même « Non scellée » (l. 8) alors qu'un compagnon existe : à dire.

**CLI-24 — mineur — matrice, HC4 × A21 (l. 315).** `decision-N-056-v1.md` l. 68-70 décrit ce que sait le concepteur du bras informé ; rien sur la taxe de déplacement. Couple : « **HC4** : **dérisque** (…) » → « **HC4** : sans lien ».

**CLI-25 — mineur — matrice, colonne A22.** Le même état « à venir / vide » de la table v4 reçoit « teste » sur C7-1 à C7-6 (l. 335-340) et « instrumente » sur C8-1 à C8-9 (l. 341-349). Choisir un seul mot (« teste », au sens « en constate l'état » de la légende) ; et H1a × A22 est vide quand H2 × A22 est « instrumente » pour la même calibration.

**CLI-26 — mineur — journal, entrée 2, (a) l. 38.** Risque « Compute overrun » cité « [E] l. 334-335 » ; il est l. 336-337 (l. 334-335 : « Correlated errors of AI reviewers »).

**CLI-27 — mineur — journal, entrée 2, (b) l. 39.** Les lignes citées sont celles de la table v2 (l. 46, 51, 53, 109, 113) ; dans `total-depenses-v3.md`, mêmes montants, vérifiés : GO-2026-10-04-08 plafond 150 l. 48 ; GO-2026-10-24-07 49,72 l. 53 ; GO-2026-10-25-02 92,43 l. 55 ; GO-2026-11-02-07 39,45 l. 111 ; GO-2026-11-03-01 48,50 l. 115. Couple : « — lignes de la table v2 du 5 novembre (94e0dbd6), à relire dans `total-depenses-v3.md` (123be1a7) » → « (`total-depenses-v3.md`, 123be1a7, l. 48, 53, 55, 111, 115) ».

**CLI-28 — mineur — journal, entrée 1 (b) l. 31.** « similarité 0,855 (5 307 mots contre 5 698) » : aucun chemin de script ni empreinte (R6).

**CLI-29 — mineur — registre B-1 l. 81 ; chemin v2 l. 8 point (3).** « Lazar a choisi l'option (b), un galop d'essai E3 ter (R-1824 l. 1782) » : R-1824 (l. 1782) est l'amendement « lecteur A » de l'étiqueteur ; le mot est en R-1825 point 4 (l. 1783). Couple : « (R-1824 l. 1782) » → « (R-1825 l. 1783) ».

**CLI-30 — mineur — journal, entrée 16 (b) l. 151.** « vocabulaire R-707 / R-895 » : dans `registres/decisions.md`, R-707 (l. 935) est la contre-lecture CL8 de la v41 ; R-707 est ici le numéro de conv-audit (R-895 : « R-707 chez conv-audit »). Couple : « (vocabulaire R-707 / R-895, … » → « (vocabulaire de conv-audit, son R-707, lu en R-895, … ».

**CLI-31 — mineur — journal, entrée 6 (e) l. 74.** « The adaptive attacks are no longer ours to design » : les deux bras sont des instances du programme, séparées des concepteurs de moniteurs (N-056 l. 64-72), non une partie extérieure. Couple : « *are no longer ours to design* » → « *are no longer designed by the people who design the monitors* ».

**CLI-32 — mineur — phrases « à dire », sigles et identifiants.** Entrées 3, 4, 7, 9 (e) : « G0 », « G1 », « H1 » nus ; registre A-1 (l. 18) : « (N-062) » dans la phrase. Au premier emploi : « *gate G0, the exit gate of the instruments phase* », « *gate G1, our main gate* », « *H1, our main hypothesis* » ; retirer « (N-062) » de la phrase.

**CLI-33 — mineur — cohérence d'un chiffre.** Journal entrée 5 (b) l. 63 : « le coût seul sépare déjà à 0,8878 » (organisme flagrant de P3, N-029 l. 25-26) ; registre A-6 l. 59-61 : « prédicteur sur le texte à 0,866 » (R-1773 l. 1731 ; état critique l. 34 « texte seul 0,866 »). Deux chiffres, deux organismes ou deux lectures : chaque pièce doit nommer l'organisme et donner les deux, ou n'en garder qu'un avec son chemin.

**CLI-34 — mineur — registre B-5 l. 114 et chemin v2 l. 12.** Le brouillon 6 de G1 (`939b56e5…`) est cité comme état sans dire qu'il n'est pas sur `main` (la matrice, § 0 point (4), le dit : `main` s'arrête au brouillon 4).

**CLI-35 — mineur — registre A-4 l. 43.** « N-054 point 3 (… ligne `<<À VÉRIFIER>>`) » : le point 3 est `decision-N-054-v1.md` l. 40-45 (c8a00b3f), vérifié ; le marqueur se lève.

**CLI-36 — mineur — journal, entrée 8 (d) l. 89.** « renforce : … éprouvée avant usage » est écrit au présent ; l'oracle n'a passé aucune épreuve (l'affaiblit le dit). Couple : « éprouvée avant usage » → « à éprouver avant usage ».

## 3. Cases de la matrice vérifiées (tirage de 46 cases : 5 valeurs dont « à vérifier », 30 lignes, 22 colonnes)

« Conforme » = la pièce existe à l'empreinte citée, dit ce que la case affirme à la ligne citée, et le mot de la case est du bon type selon la légende (l. 15).

| case | mot | pièce citée | conforme | note |
|---|---|---|---|---|
| G0-1 × A02 | T | verdict T0.4 v3 l. 3 (63444faa) | **non** (ligne) | énoncé l. 11 (CLI-23) |
| C6-3 × A02 | T | idem | **non** (ligne) | idem |
| G0-5 × A01 | T | résultats T0.3 l. 29 (9ab618ed) | oui | |
| C6-2 × A01 | T | idem ; manifeste c9bba5e1 | oui | réserve : aucun verdict scellé de T0.3 (calibration-v3 l. 72-75) — trou 3 |
| C8-4 × A01 | I | calibration-v3 l. 72-73 | oui | |
| H2 × A01 | I | N-007/N-008 l. 30-34 (ab7dc9bb) | oui | |
| G0-4 × A03 | I | N-029 l. 17-18, 37-39 (084e3052) | oui | |
| C6-4 × A03 | T | verdict T0.5 l. 3 ; état l. 23, 156 | oui (fond) | ligne 3 sans l'issue (CLI-23) |
| G0-2 × A04 | I | go.md l. 216 ; décisions l. 1727, 1728 | oui | périmé depuis R-1854 |
| G0-3 × A04 | I | go.md l. 216 (test croisé) | oui | |
| C6-G0 × A04 | D | go.md l. 216 ; chemin v1 l. 20 | oui | |
| G0-3 × A05 | I | chemin v1 l. 21 | **non** (ligne) | citation à l. 51 |
| C8-8 × A05 | I | chemin v1 l. 21 ; brouillon concepts | oui | |
| G0-4 × A06 | I | état l. 159 | **non** (ligne) | T0.8 à l. 160 |
| H2 × A06 | I | N-007 l. 42, 47 | oui | |
| G0-7 × A07 | I | brouillon 5 (9d55160f) ; état l. 161 | oui | état dit « brouillon 2 » (CLI-17) |
| HC1 × A07 | I | brouillon 5 l. 1 | oui | |
| G0-2 × A08 | I | décisions l. 1785 (R-1827) | oui | périmé : R-1849 (CLI-04) |
| C8-8 × A08 | D | N-060 v3 l. 33-35 (2b448f69) | oui | |
| H5 × A10 | D | lecture l. 80, 127-128 (24081eed) | oui (faible) | R3 est une règle de défense, non « un mélange de moniteurs » : lien indirect |
| H7 × A10 | D | lecture l. 148 ; audit l. 433-435 (02a87957) | oui | |
| H1a × A11 | D | décisions l. 837, 844 ; N-057 | oui | niveau méthode respecté |
| C7-5 × A11 | D | N-057 l. 39-41 ; go.md l. 99 | oui | |
| G0-6 × A12 | R | N-053 l. 17-22 (2204256d) | oui | |
| H1a × A12 | R | N-053 l. 17-26, 42-44 | oui | |
| H1b × A12 | D | décisions l. 745 (R-521) | **non** (type) | phrase générique recopiée (CLI-14) |
| G0-3 × A15 | D | décisions l. 1752 (R-1794) | oui | |
| C8-5 × A17 | D | verdict Goodhart l. 3 (7dade9ef) | oui | « cousin » dit |
| H1a × A20 | R | N-054 l. 37-45 ; N-056 l. 55-57 | oui | |
| C7-5 × A21 | R | N-056 l. 64-72 ; N-057 l. 39-41 | oui | |
| HC4 × A21 | D | N-056 l. 68-70 | **non** (lien) | rien sur HC4 (CLI-24) |
| C6-5 × A22 | V | promis-livre-v3 l. 21 | **non** | pièce trouvée : décisions l. 235 (CLI-11) |
| C6-6 × A22 | T | promis-livre-v3 l. 22 | oui (à la table) | la table est fausse (CLI-17) |
| C7-1 × A22 | T | promis-livre-v3 l. 25 | oui | |
| C8-3 × A22 | I | promis-livre-v3 l. 33 | oui | type incohérent avec C7 (CLI-25) |
| C6-7 × A22 | T | total-depenses-v3 l. 11-12 | oui | |
| G0-4 × A23 | I | décisions l. 974 (R-746, point 1) | oui | |
| H1a × A23 | R | R-746 point 4 | oui | mot de Lazar consigné en R-, non en N- |
| G0-3 × A24 | D | P-040 l. 15, 17 (b44bf8a0) | oui | ajouter N-061 (CLI-05) |
| C8-8 × A25 | R | N-062 l. 22 (63f42690) | oui | |
| C7-4 × A25 | D | N-062 l. 23-24 | oui | |
| C6-7 × A26 | V | proposition l. 46 (non scellée) | oui | |
| H1a × A26 | I | proposition l. 16-22 | **non** (type) | un texte n'instrumente pas (CLI-13) |
| H5 × A28 | I | question v2 l. 17, 21 (2dbad4b7) | **non** (type) | instrument « absent du dépôt » |
| G0-8 × A29 | T | état de l'art collusion (7547040e) ; décisions l. 832 | oui | |
| H9 × A29 | D | N-035 l. 16, 22-26 (55df073d) | oui | |

Bilan : 46 cases distinctes ; **9 non conformes** : 4 de ligne (G0-1 et C6-3 × A02, G0-3 × A05, G0-4 × A06), 4 de type ou de lien (H1b × A12, HC4 × A21, H1a × A26, H5 × A28), 1 « à vérifier » levable (C6-5 × A22) ; plus une case conforme à une table fausse (C6-6 × A22). Toutes les empreintes citées (36 recalculées) sont exactes. Grille recomptée par script : 28 T, 70 I, 61 D, 10 R, 4 V, 1 103 vides, conforme aux comptes l. 151.

Journal, vérifications par entrée : citations de [E] exactes aux lignes citées sauf l. 334-335 (CLI-26) ; décisions N-005 à N-062 et R-355 à R-1836 citées : existent et disent ce que l'entrée dit, sauf R-707 (CLI-30) ; chiffres : 58 630 / 28 160 / 138 600 (l. 7, 388), 645,42 / 187 / 111,87 / 50, 60 / 47 / 5 / 8, 92,43, 49,72, 48,50, 39,45, 4 000 USD (l. 383), 4 600-6 900 euros (R-1717 l. 1675), 118 fichiers (R-1580) : conformes ; « sous cent dollars » : non conforme (CLI-06) ; 0,855 : sans source (CLI-28).

Registre et chemin critique, vérifications : L11 au 15 novembre (l. 1581), GO jusqu'au 16 (go.md l. 216), plafond 200 et pire cas ≈ 198 (R-1764 l. 1722), 5,744 USD (dépenses l. 387, 390), E3 ter ≈ 7 / 15 (R-1833), audit du rappel ≈ 55 / 180 et ≈ 40 / 120 (brouillon l. 100-101, ccc0d972), 0,745 → 0,813 (R-1641 l. 1599), puissance 0,60-0,66 (R-1584 l. 1542), Fable au 10 novembre 05:00 (R-1639), 0,523 et p = 0,19 (état critique l. 19), Brier 0,252 (l. 62), 4 250-11 700 euros (R-1722 l. 1680) : conformes ; R-1824 pour E3-6 : non (CLI-29) ; marges du tableau du chemin v2 : arithmétique juste sur ses propres dates (pas 1 : 15 j ; pas 3 : 5 à 8 ; pas 7 : 2 ; pas 9 : 6 à 9), mais pas 8 et pas 7 faux sur les dépendances écrites (CLI-03).

## 4. Cohérence entre les trois pièces

| objet | matrice | journal | registre / chemin | état |
|---|---|---|---|---|
| dépense relevée | 645,42 ; 187 ; 111,87 sur 50 | idem | 645,42 ; **185 ; 111,85 sur 49** (v3) | à aligner sur la v4 (CLI-16) |
| part de la carte graphique | — | « sous cent dollars » | « ≈ 130 » | contradiction (CLI-06) |
| calibration | 60 / 47 / 5 / 8 | idem | **55 / 44 / 3 / 8 ; 0,800** | à aligner (CLI-16) |
| scellement de G1 | — | **≈ 22 novembre, une semaine de marge** | 28-29 novembre, marge consommée | contradiction (CLI-02) |
| goulot | — | — | pas 7, marge ≈ 2 j | dépassé par R-1854 (CLI-03) |
| date de G0 promise au jury | « December 2026 » | « December 2026 » | B-6 : « 1er novembre » | à aligner (CLI-16) |
| identifiants des promesses | v4 (texte envoyé) | v4 | A-5 : « C7-4 » de la v2 | à aligner (CLI-15) |
| N-061 | « introuvable » | « introuvable » | non cité | périmé dans les deux (CLI-05) |
| étiqueteur | R-1827, 36,90 USD | idem | « en relecture » | tous périmés : R-1849, 41,09 USD (CLI-04) |
| préenregistrement du papier C | brouillon 5 | brouillon 5 | — | la table v4 et `etat.md` disent brouillon 2 (CLI-17) |
| prédicteur sur le texte | — | 0,8878 (coût, P3) | 0,866 | à expliciter (CLI-33) |
| orphelins | A13, A14, A16, A19 | « pôle, recombinaison, pilotes » orphelins (entrée 10) | C-8 « dispersion » | cohérents entre eux ; A19 discutable (CLI-20) |

## 5. Trous que le jury frapperait et que les pièces ne préparent pas (relevés, non comblés)

1. **Épreuves lancées sans préenregistrement** depuis le 8 novembre (course de dose-réponse, R-1854 ; étiqueteur v2, R-1852), face à la règle 1 du texte envoyé ([E] l. 240-243). Aucune pièce ne prépare la distinction « exploratoire, non opposable / confirmation préenregistrée », ni ce que devient « The pilot runs before the grant starts » ([E] l. 278).
2. **La règle de décision de G1 a changé** : l'intervalle de confiance à 95 % promis ([E] l. 160) devient le pari apparié qui décide (N-055 D-S11 ; N-056 nœud 2), et l'intervalle de DeLong peut être retiré faute de vérification R7 (chemin v2, pas 6).
3. **« 31 of 31 predictions confirmed » ([E] l. 271) n'a pas de verdict scellé** : la table de calibration v4 classe les prédictions de T0.3 « registre des décisions, R-025 (pas de verdict scellé) » (`calibration-v3.md` l. 72-75).
4. **H6 : le bruit d'activations** figure dans le texte envoyé ([E] l. 152) et n'est plus revendiqué (N-015, 20 octobre).
5. **Promesses hors des sections 6 à 8 non tracées** : tableau des bascules ([E] l. 321-339 : « Import published attack policies » contre la quarantaine N-057 ; « any change of model only by explicit decision » contre « quitte à prendre un modèle plus gros », R-1770 ; « Qwen2.5-7B serves as a heterogeneous agent » ; « Paper C is scheduled first ») ; règles de méthode (section 5) ; budget (section 12 : validation humaine 4 000 USD contre 4 600-6 900 euros estimés ; outillage 1 000 USD par mois contre la dépense déjà relevée).
6. **« No claimed statement has been found fully occupied » ([E] l. 264)** à relire à la lumière d'HELIOS (« partiellement occupée », R-622) et du nœud non tranché : la phrase reste-t-elle vraie ?
7. **Instrument de vérité du dommage indécis** : étiqueteur « non tranché », oracle de couverture non conçu ni éprouvé (B-7) ; la réponse à « How do you know an episode is sabotaged? » repose sur des instruments qui n'ont pas encore passé leurs épreuves.

**Les trois plus dangereux** : (1) les épreuves exploratoires sans préenregistrement, vues comme une entorse à la règle 1 que le jury a lue ; (2) la dépense : la phrase préparée « each line under a signed-off cap » est démentie par le registre (treize instances sans autorisation, une ligne au-dessus de son plafond) ; (3) la règle de G1 changée (pari apparié au lieu de l'intervalle à 95 %) jointe au « 31 of 31 » sans verdict scellé : deux écarts entre ce qui est promis et ce qui sera jugé.

Fin d'écriture (`date -u`) : Sun Nov  8 15:37:38 UTC 2026
