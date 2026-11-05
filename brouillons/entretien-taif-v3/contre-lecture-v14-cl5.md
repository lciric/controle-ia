# Contre-lecture CL5 — section 7 bis du programme d'entretien TAIF v14

Contre-lecteur neuf (R2), sous-agent Fable 5.1, sans part à l'écriture de la v14. Écrit après le relevé `date -u` de
**10:32:04 UTC le 29 octobre 2026**. Objet : `brouillons/entretien-taif-v3/programme-entretien-taif-v14.md`
(`4f8024c092aef39efb0bad1ae1b954a39609d13b21d672478ccd52bc73bce950`, vérifiée), section 7 bis (lignes 1089 à 1134) : la table,
les deux paragraphes et le texte anglais « à dire ». Rien d'autre de la v14 n'est jugé ici ; ses sections 2, 3 et 8 ont servi de
sources de comparaison.

Périmètre respecté : aucun fichier de `prereg/P3-consignes-v1.md`, `donnees/`, `diag/*/traces`, aucune branche `donnees/*` ni
`quarantaine/*`, aucun contenu de « carte des hypothèses » (seule la présence de son empreinte dans les registres a été
cherchée par motif). Pas de réseau, pas de commit, aucun fichier existant modifié ; ce rapport et son compagnon sont les seuls
fichiers écrits.

## Verdict

**Peut être dite après corrections, pas en l'état.** Un bloquant : les deux paragraphes et le texte anglais présentent au
présent, comme faits, trois choses qui n'ont pas eu lieu (théorie « vérifiée sur données réelles », « éprouvée contre un
adversaire », questions « préenregistrées »), ce que la v14 elle-même dément en section 2 et au front B. Huit majeurs : trois
lignes de la table décrivent mal ce que la candidature contenait déjà (théorie, instruments vérifiés, universalité), deux
chiffres sont incomplets ou périmés devant un financeur (≈ 12 USD du pôle sans les ≈ 156 USD de pilotes ; « temps, pas
calcul » contredit par la section 8), « les trois papiers restent le plancher » est faux au palier de 58 630, la lecture
« extension sur le scénario ambitieux » est affirmée alors que la v14 la dit « à confirmer », et la carte des hypothèses est
citée « non retrouvée sur disque » dans un texte destiné au financeur. Les citations de la candidature sont exactes mot pour
mot (une référence de section à corriger) ; les dates et numéros de décision sont exacts ; l'arithmétique de l'enveloppe est
juste.

## 1. Vérifications faites

**Empreintes.** `sha256sum -c` sur les douze compagnons de `livrables/candidature-ea-funds-v1/` : tous `OK`. Empreintes
citées en tête de la 7 bis conformes : `candidature-v2.md` `dbe24ac0…`, `proposal-v1.md` `2f1e0864…`, `budget-v2.md`
`c5be1402…`, `tracabilite-proposal-v1.md` `3dfe04ec…`, `demande-option-c-ventilation-v2.md` `8ab00ab5…`,
`decision-N-060-v3.md` `2b448f69…`, note de dépenses `depenses-cumul-2026-10-28-v1.md` `93969946…`. La proposition v2
envoyée (`737c482c…`) et le budget v3 (`037765b0…`) ne sont pas sur disque, comme la 7 bis le dit.

**Citations attribuées à la candidature** (toutes lues sur les fichiers versés) :

| citation de la table | où elle est | exacte ? |
|---|---|---|
| « an additivity lemma, and a negative theorem » | `proposal-v1.md` § 1 (ligne 26) et `candidature-v2.md`, Summary (ligne 37) ; le § 3 de la proposition titre « a lemma, a negative theorem, and the pivotal question » | mot pour mot ; **section fausse** (§ 1, pas § 3) — CL14-10 |
| « adaptive attacks, including fine-tuning and RL against the probe » | `candidature-v2.md`, Project goals, ligne 45 | mot pour mot |
| « replication on a second model family » | `candidature-v2.md`, ligne 104 ; `proposal-v1.md`, ligne 279 | mot pour mot |
| « seeded ground truth », validation humaine | `candidature-v2.md`, ligne 45 (« pre-registered seeded ground truth ») ; budget « Human expert validation of ground truth » | mot pour mot |
| « must beat the best black-box baseline » | `candidature-v2.md`, ligne 45 ; `proposal-v1.md`, ligne 112 | mot pour mot |

**Ce que la table dit « absent » et qui est, ou n'est pas, dans la candidature :**

- *Pôle scientifique automatique* : absent comme objet de recherche ; la candidature dit « I set the questions and take every
  decision ; execution … is done by AI agents » (ligne 62). « absent : les agents exécutent » est juste.
- *Collisionneur multi-modèles* : absent ; la candidature nomme la faiblesse qu'il répond (« these reviewers share a model
  family, so their errors may be correlated », ligne 62) avec, pour parade, la validation humaine budgétée. Juste, mais la
  parade budgétée existait (voir CL14-19).
- *Mesures à coût nul* : absentes ; le fichier de scores de P3 réel date du 19 octobre. Juste.
- *H9, délégation* : aucun mot « delegation » dans les deux textes. Juste.
- *Instruments vérifiés* : **présent** dans la candidature — « bit-identical replay » du harnais, « agreement of the production
  path with a higher-precision reference path, sensitivity to an injected defect, and tested guards » (proposition § 6,
  ligne 191) ; « dose 0 reproduces the base model bit for bit » (ligne 193) ; « every stop guard is tested on a healthy case and
  on an artefact » (§ 5). Le « absent » est faux — CL14-04.
- *Théorie* : la proposition § 3 avait déjà un théorème négatif « by invariance » couvrant « every G-invariant statistic
  (maximum, mean, sum, count above a threshold) », deux classes d'attaque C et K, les garanties locales (scan, CUSUM,
  co-élévation) et « the theorem also says when monitoring based on marginals must fail ». Le « lemme sur une statistique » est
  faux — CL14-03.
- *Universalité* : la candidature prévoyait la réplication des **moniteurs** sur une seconde famille de **modèles** (scénario
  ambitieux) et « transfer is measured, never assumed » (§ 9). N-044 porte sur l'**organisme** et des familles de **tâches**
  inédites. Objets différents — CL14-05.

**Dates et numéros de décision** (en-têtes lus dans `docs/decisions/`, lignes lues dans `registres/decisions.md` et
`registres/go.md`) : N-035 (22 octobre, H9, sous réserve d'antériorité) ✓ ; N-044 (mot de Lazar 25 octobre 00:05 Paris =
24 octobre 22:05 UTC, transcrite le 24 à 23:50 UTC : « 24 octobre » tient en UTC) ✓ ; N-045 (25) ✓ ; N-049, N-050, N-052, N-053
(26) ✓ ; N-054 (26, mode non chiffré avant G1, G1 par mode, mode tenu à l'écart) ✓ ; N-055 (27, pari apparié D-S1 à D-S12) ✓ ;
N-056 (27 : bases boîte blanche (ii) et (iii), gain de H1 par mode, bras (A) tenu à l'écart « aveugle aux moniteurs » et (B)
« informé », lignes 67-68) ✓ ; N-057 (28, cellules en quarantaine conservées et scellées) ✓ ; N-058, N-059 (28) ✓ ; N-060 v3 (29,
01:48 UTC ; « deux lecteurs de deux familles de modèles autres que celles des moniteurs évalués (ni Llama ni Qwen) », « oracle
de couverture contre la référence cachée », ligne 21-25) ✓ ; R-611 (28, pipeline opérationnel des étages 1-2 gelé jusqu'à une
revue de sécurité externe) et GO-2026-10-28-04 (type « décision », même objet) ✓ ; R-679 (29, régénération des sondes de P3
« identique au bit près », 1,76 USD) ✓ ; R-704 (29, rejeu des juges, 1,92 USD) ✓ ; R-733 (29, garde δ = 0,05, K_h = 10) ✓ ;
R-741 (29, lentilles, processeur, sans dépense) ✓ ; R-746 (29 : (1) juge texte préparé, (5) G1 par famille d'organismes, (6)
critère de bascule « 8B trop faible ») ✓ ; R-738, R-740 (29, course d'idéation visée le jour même) ✓. Carte des hypothèses :
première trace au registre le 28 octobre (R-612, R-619), cohérente avec la date citée.

**Montants.** Ventilation v2, section 2 : E1 7 500, E2 4 000, E3 5 000, E7 12 000, E8 6 000, sous-total 34 500, réserve 3 450,
extension 37 950, total 176 550 = 138 600 + 37 950 ✓ ; « pas de E4 à E6 » ✓ ; « ordres de grandeur, non des devis » = réserve 1 ✓.
« ≈ 12 USD » = 6,24 + 5,89 = 12,13 (`depenses.md`, lignes 199 et 206) ✓ mais incomplet (CL14-06). « 3,68 USD » = 1,76 + 1,92 ✓
(un rejeu v2 engagé à 10:05 UTC sous 5 USD, ligne 233, non encore consigné en dépense). « ≈ 255 USD du 24 au 29 » :
179,9 + 20,31 + 54,55 = 254,76 (section 8) ; mais le run v1 du repli de G0 (3,19 USD, 09:35 UTC, ligne 231) précède
l'écriture de la v14 et le run v2 (6,83 USD, 10:26 UTC, ligne 234) la suit d'une minute : **≈ 258 à l'écriture, ≈ 265 à 10:26
UTC** (CL14-12).

## 2. Constats

Gravité : **bloquant** (faux ou invérifiable devant le financeur), **majeur** (inexact, incomplet ou contradictoire avec la
v14), **mineur** (précision).

### Bloquant

**CL14-01 — Trois affirmations au présent pour des choses non faites** (paragraphe « Pourquoi c'est bien plus ambitieux »,
lignes 1112-1115 ; texte anglais, lignes 1128-1131). « **vérifiée sur données réelles** à coût nul » : aucune des mesures T0 à
T5 n'est scellée ni lue (front B : « rien ne permet d'affirmer … en cours de préenregistrement » ; section 2 : « aucune mesure du
front B lue »). « **éprouvée contre un adversaire gouverné** » : aucun organisme saboté, aucune sonde au-dessus d'une base
(section 2, « ce qui n'existe pas encore »). Anglais : « It is now a theory … **tested** on data we already hold, **challenged**
by a governed adversary …, **driven** by an automated research pole **judged** on task families it never saw » et « every new
question **is** preregistered » : même défaut, et c'est le défaut que CL1-02 avait déjà corrigé ailleurs dans ce programme.
Phrases corrigées :
- français : « Le programme se présente désormais comme une théorie du contrôle des moniteurs : … ; **à vérifier** sur données
  réelles à coût nul ; **à éprouver** contre un adversaire gouverné … ; et **à porter** par un dispositif qui pose lui-même ses
  questions, … **jugé** sur des familles de tâches qu'il n'aura jamais vues. » ; « toute question nouvelle **entrera** par un
  préenregistrement scellé et contre-lu avant toute lecture (R1, R2) ».
- anglais : « It is now a theory of what monitors cannot see, **to be tested** on data we already hold, **to be challenged** by a
  governed adversary that includes attack modes our monitor designers never saw, and **to be driven** by an automated research
  pole **that will be judged** on task families it never saw during design. … The gates are frozen and every new question
  **will be preregistered and sealed before any reading**. »

### Majeurs

**CL14-02 — « Les trois papiers restent le plancher » / « The three papers remain the floor »** (lignes 1115-1116, 1130). Le
plancher envoyé (58 630, sept mois) finance les papiers C et A seulement ; le papier B entre au scénario ambitieux (ventilation
v2, section 1 ; candidature : « minimal, 7 months, papers A and C only »). Dit à côté des paliers, c'est une contradiction qu'un
évaluateur relève aussitôt. Phrase corrigée : « Les trois papiers restent le cœur de ce qui est livré ; au palier de 58 630,
seuls les papiers A et C sont financés. » / « The three papers remain the core deliverable; the 58,630 floor funds papers A and C
only. »

**CL14-03 — Ligne « Théorie des moniteurs », colonne « plus ambitieux parce que »** : « on passe d'un lemme sur une statistique à
ce que chaque moniteur ne peut pas voir ». La proposition § 3 énonçait déjà, par invariance, l'aveuglement de « every G-invariant
statistic (maximum, mean, sum, count above a threshold) », l'impossibilité sous échangeabilité, les garanties locales et les
classes C et K ; elle disait « the theorem also says when monitoring based on marginals must fail ». Le gain réel est ailleurs :
une carte de ce que chaque statistique suppose sur l'agent, hypothèse par hypothèse, avec lemmes prouvés, là où la candidature
avait un lemme et un théorème sur une famille de statistiques invariantes. Phrase corrigée : « on passe d'un lemme et d'un
théorème sur les statistiques invariantes à une carte, hypothèse par hypothèse, de ce que chaque moniteur suppose sur l'agent et
de l'écart qui le rend aveugle ».

**CL14-04 — Ligne « Instruments vérifiés », colonne « candidature » : « absent »**. Faux : la proposition § 6 revendiquait déjà le
harnais validé par « bit-identical replay », l'accord avec un chemin de référence, la sensibilité à un défaut injecté et des gardes
testées ; « dose 0 reproduces the base model bit for bit » ; § 5 : gardes testées sur cas sain et artefact. Un évaluateur qui a la
proposition sous les yeux y verra une survente du neuf. Cellule corrigée : « présent pour le harnais (rejeu au bit près, § 6) » ;
colonne « ajouté depuis » : « étendu aux sondes de P3 (régénérées au bit près, R-679), aux juges (rejeu, R-704) et aux
directions des sondes (lentilles, R-741) ».

**CL14-05 — Ligne « Universalité »** : la candidature cite « replication on a second model family » (réplication des
**moniteurs** sur une seconde famille de **modèles**, inchangée, au scénario ambitieux à 138 600 — la table le dit elle-même à la
dernière ligne) ; N-044 et N-049 portent sur l'**organisme** et des familles de **tâches** inédites. La ligne met face à face
deux objets différents et laisse entendre que la réplication est remplacée par mieux. Cellules corrigées : « candidature » :
« réplication des moniteurs sur une seconde famille de modèles (inchangée, scénario ambitieux) ; rien sur l'organisme » ;
« ajouté depuis » : « universalité de l'organisme mesurée sur des familles de tâches jamais vues à la conception, vivier, tâches
fraîches (N-044, N-049) » ; « plus ambitieux » : « une seconde question d'universalité, sur l'organisme, en plus de la
réplication des moniteurs ».

**CL14-06 — Ligne « Pôle scientifique automatique » : « deux lancements (≈ 12 USD) »**. Exact pour (a) et (a) bis, mais la note
de dépenses `93969946…` (section 1) compte aussi « pilotes de l'organisme écrit par Gemini … ≈ 156,3 USD » (24-26 octobre, sept
runs), et la ventilation v2 justifie E7 par ces « quatre pilotes … ≈ 156 USD en trois jours ». Dit au financeur, « ≈ 12 USD »
pour justifier 12 000 est un chiffre incomplet, et il contredit la ventilation qu'il cite. Cellule corrigée : « pilotes de
l'organisme (≈ 156 USD, 24-26 octobre) et deux lancements réels du pôle (≈ 12 USD, 27 octobre) ».

**CL14-07 — « Tout le reste de la table coûte du temps, pas du calcul : mesures à coût nul, porte G1 durcie, vérité du dommage,
H9 »** (lignes 1123-1124) et cellules « temps, pas calcul » des lignes « Porte G1 » et « Vérité du dommage ». La section 8 de la
même v14 chiffre les banques de G1 à ≈ 410 à 2 090 USD et les lectures de la vérité du dommage à ≈ 133 au pilote, ≈ 1 000 à
10 000 épisodes (SUPPOSÉ) ; N-056 et R-746 (bases (ii), (iii), G1 par mode et par famille, K_h = 10, ≥ 288 unités par mode)
font grossir ces banques. Ce calcul est **couvert par les lignes envoyées** (carte graphique 12 000, outillage 12 000), il n'est
pas nul. Phrase corrigée : « Tout le reste de la table coûte surtout du temps ; le calcul qu'il entraîne (banques de G1,
lectures de la vérité du dommage) tient dans les lignes déjà envoyées du scénario ambitieux (section 8). » Cellules : « temps ;
calcul couvert par les lignes envoyées ».

**CL14-08 — Enveloppe affirmée alors que sa lecture est « à confirmer »**. La 7 bis pose « 176 550 = 138 600 + 37 950 » comme
acquis ; la section 8 de la v14 dit que le « go » de 11:28 portait sur « plancher plus extension » (v1, ≈ 86 130) et que la
portée sur le scénario ambitieux est « à confirmer » (ventilation v2, section 5, point 3 ; « Points à trancher », point 3,
« confiance moyenne »). Tant que Lazar n'a pas confirmé, la 7 bis ne peut pas être dite telle quelle. Phrase corrigée (à dire
seulement après son mot) : inchangée ; **sans mot**, la forme « sans chiffre » du point 3 : « the extension is named and costed,
which we can walk you through ». À ajouter en tête de la 7 bis : « *à dire seulement si Lazar a confirmé la lecture
« extension sur le scénario ambitieux » (section 8, point 3).* »

**CL14-09 — « carte des hypothèses, 28 octobre (`f7dfe5fd…`, non retrouvée sur disque) »** (ligne 1099) dans un texte destiné à
être dit au financeur. La pièce qui porte tout le « retournement d'ambition » (section 1) est citée par une empreinte qu'aucun
fichier du dépôt de travail ne porte ; la v14 elle-même la dit « absente du disque » (« Ce que la v11 n'a pas pu vérifier ») et
R-757 « citée par existence seulement ». Un évaluateur demandera à la voir. Au minimum, nommer où elle est ; avant l'entretien
(décalé, R-744), la verser sur `main` avec son compagnon et vérifier l'empreinte (R11). Cellule corrigée : « carte des
hypothèses, 28 octobre (`envois/theorie-v1/carte-des-hypotheses-v1/`, branche de canal de conv-audit, `f7dfe5fd…`, **à verser
sur `main` et à vérifier avant l'entretien**) ».

### Mineurs

**CL14-10 — « (proposition, § 3) »** (ligne 1099) : la citation mot pour mot est au § 1 de la proposition (et au résumé de la
candidature) ; le § 3 n'a que les intitulés « Additivity lemma (L) » et « Negative theorem (T) ». Corrigé : « (proposition, § 1 ;
candidature, résumé) ».

**CL14-11 — « sous un frein extérieur »** (ligne 1101) : la revue externe n'existe pas encore (section 8 : « la revue externe
n'a pas avancé » ; taux et évaluateur à fixer par Lazar, E1). Le frein actuel est intérieur (R-611, GO-2026-10-28-04) et
conditionné à une revue à commander. Corrigé : « sous une porte intérieure qui attend une revue externe encore à commander
(E1) ».

**CL14-12 — « ≈ 255 USD du 24 au 29 »** (ligne 1104) : ≈ 258 à l'écriture de la v14 (run v1 du repli de G0, 3,19 USD, consigné
09:35 UTC), ≈ 265 à 10:26 UTC (run v2, 6,83 USD) ; le chiffre bouge d'heure en heure. Corrigé : « ≈ 265 USD du 24 au 29 (10:26
UTC) » ou, à l'oral, la forme de la section 8 : « a few hundred dollars ».

**CL14-13 — « 3,68 USD au registre »** (ligne 1108) : exact pour les dépenses consignées ; un rejeu des juges v2 est engagé à
10:05 UTC sous un plafond de 5 USD (`depenses.md`, ligne 233). Corrigé : « 3,68 USD consignés ; un rejeu v2 en cours sous 5 USD ».

**CL14-14 — « H9, délégation … N-035, 22 octobre … une question de plus pour le papier B »** : N-035 entre H9 « sous la réserve
d'antériorité de la section 3 » (aucune recherche affirmative faite). Corrigé : « une question de plus pour le papier B, sous
réserve d'antériorité (N-035, section 3) ».

**CL14-15 — « matrice « statistique × classe » et vérification formelle à faire »** (ligne 1099) et E3 : la vérification formelle
(Lean) n'apparaît dans aucune décision ni piste (grep de `docs/decisions/` et du registre : rien) ; elle n'existe que comme ligne
de la ventilation v2. Corrigé : « matrice « statistique × classe » (piste 1 de la section 3 bis) ; vérification formelle
**proposée** au budget (E3), non décidée ».

**CL14-16 — Ligne « 70B, seconde famille, attaques par renforcement … scénario envoyé, 138 600 »** : le contenu du scénario
ambitieux envoyé (138 600) n'est connu ici que par la transcription de la ventilation v2 ; le budget versé sur disque
(`budget-v2.md`) dit 146 300 pour le même périmètre. Rien à changer dans la phrase ; réserve à garder (déjà dans « Ce que la v11
n'a pas pu vérifier »). À ajouter en tête de la 7 bis : « montants du scénario ambitieux envoyé pris de la ventilation v2, le
budget v3 n'étant pas sur disque ».

**CL14-17 — « toujours écrite avant les données »** (ligne 1106) : des données existent déjà (180 épisodes du pilote, banques
sous GO-2026-10-28-02) ; ce qui est garanti, c'est le scellement **avant toute lecture** (R-733, N5 : « tout sceller avant le
pilote ; ne pas lire f_A avant G1 »). Corrigé : « une porte plus dure, scellée avant toute lecture ».

**CL14-18 — « cellules scellées (N-057, 28) »** : exact, mais la 7 bis ne dit pas qu'elles sont en quarantaine et ne seront
jamais citées à l'entretien (N-057, point 6). Rien à corriger dans la table ; ne pas en dire plus à l'oral que « they exist,
sealed, and await the review ».

## 3. Ce qu'un évaluateur hostile relèverait (au-delà des constats)

1. **L'addition des dépenses.** La table laisse lire ≈ 255 + 12 + 3,68 ≈ 271 USD de dépenses ; la note `93969946…` donnait
   ≈ 450 USD connus au 28 octobre (hors relève du 23, « réel inconnu »), et la candidature disait « about $20 ». Si la 7 bis est
   dite seule, préparer une ligne : « the whole programme has cost a few hundred dollars to date; the twenty dollars of the
   application were the GPU of the preregistered instruments at the time » (formulation de la note, section 2).
2. **E7 justifié par un chiffre qui change selon le document** (≈ 12 ici, ≈ 156 dans la ventilation v2) : CL14-06.
3. **La revue externe (E1, 7 500)** : ni évaluateur identifié, ni taux fixé, ni date ; et l'adversaire scellé (E2, 4 000) ne peut
   être exécuté qu'après elle (R-611). Préparer : « the review gates the adversary; its rate is to be fixed with the reviewer ».
4. **La vérification formelle (E3)** : 5 000 pour une chose que personne n'a décidée ni cadrée (CL14-15) ; dire « proposed ».
5. **Symétrie (R4)** : la 7 bis ne liste que des ajouts. La section 2 de la v14 a deux résultats négatifs neufs (juges 0,87 de
   scores finis ; garde δ presque muette sous ≈ 144 unités). Une ligne de table « Résultats négatifs depuis » (candidature :
   « two honest failures » du harnais ; depuis : 29-2, 29-6) rendrait la table conforme à ce que le programme promet.
6. **« Pipeline offensif gelé » et demande d'argent pour un adversaire** : la cohérence tient (E2 « sous revue »), à condition de
   le dire en une phrase ; sinon cela se lit comme « financez ce que nous nous interdisons ».
7. **La carte des hypothèses** (CL14-09) : « non retrouvée sur disque » est la pire formule possible devant qui finance une
   théorie.
8. **Le triple** (58 630 → 176 550) : la ventilation v2, réserve 2, exige qu'il soit dit « tel quel, avec les paliers, jamais
   glissé » ; la 7 bis ne nomme pas 58 630. Ajouter au paragraphe d'enveloppe : « le formulaire porte 58 630 ».

## 4. Ce que cette contre-lecture n'a pas pu vérifier

- Le mot direct de Lazar « ≈ 10:25 UTC le 29 octobre » (en-tête de la 7 bis) : hors registre au moment de la lecture.
- La proposition v2 envoyée et le budget v3 (`737c482c…`, `037765b0…`) : absents du disque ; toutes les comparaisons portent sur
  les versions versées du 7 octobre, comme la 7 bis l'annonce.
- Le contenu de la carte des hypothèses (interdit ici) ; seule la présence de son empreinte dans les registres a été cherchée.
- Les ≈ 179,9 USD du collisionneur des 24-27 octobre : pris de la note `93969946…`, non resommés ligne à ligne.
- La facturation réelle : tous les montants sont ceux des registres.
