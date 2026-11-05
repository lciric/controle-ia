# Contre-lecture CL3 du programme d'entretien Transformative AI Fund v10

Contre-lecteur neuf (règle R2). Je n'ai écrit ni la v10, ni la v9, ni CL1, ni CL2, ni la ventilation. Modèle déclaré par
l'environnement : Opus 5.5. Aucune dépense, aucun réseau, aucun fichier du dépôt modifié.
Relevé `date -u` au début : **08:58:17 UTC le 29 octobre 2026** ; à la fin : dernière ligne.

**Pièce relue** : `brouillons/entretien-taif-v3/programme-entretien-taif-v10.md`. Empreinte recalculée `eb87b8a8741f8f81…`,
identique à son compagnon. Lue en entier (1 188 lignes). Les numéros de ligne renvoient à cette empreinte.

**Pièces de contrôle** : CL2 (`49d943812e86d863…`, conforme à son compagnon), lue en entier ; v9 (`1e0969d8…`) et v8
(`7917ed02…`), différences des sections 2, 5 et 6 lues ; ventilation v2 (`8ab00ab5…`).

**Registres recalculés** (inchangés entre 08:58 et 09:07 UTC) : `decisions.md` `d3d7fcc8…` (965 lignes, dernière R-737 ;
`head -959` rend `fe82018c…`, ce qui confirme CL2-11) ; `go.md` `f637f3ac…` ; `depenses.md` `34025262…`.
Lus : R-361, R-379, R-389, R-390, R-422, R-430, R-464 à R-477, R-483 à R-487, R-491, R-495, R-509, R-515, R-517 à R-519,
R-523, R-553, R-571, R-586, R-588, R-592, R-594, R-597, R-600, R-607 à R-611, R-615, R-617, R-635, R-676, R-686, R-687,
R-719, R-727 à R-737 ; `go.md` lignes 51 à 132 (extraits) ; `depenses.md` : toutes les lignes « refus », lignes 92 et 116
à 163.

**Empreintes citées par la v10, recalculées, toutes conformes** : N-060 v3 `2b448f69`, lecture du rejeu `8799f7d3`,
contre-lecture du rejeu v2 `b156da9f`, coupe du calibrage `c66c1eed`, contrôle 12 joint `7600f2d0`, devis du pilote
v1 `044112d3` et v2 `b841b006`, P-036 v2 `155f0511`, devis de régénération `9c85bb5e`, vérification NaN `c743199a`,
CL1 `f4c7d194`, CL6 `4e701178`, CL8 `ffa07b12`, CL9 `eed46db3`, CL10 `e8736904`, note de dépenses `93969946`,
rapprochement `813f3b30`, N-058 `854f2724`, N-059 `41aff854`, note Fable `20ec8d43`, verdicts `63444faa`, `0c8ecbdf`,
`05e896da`, HELIOS `02527fd4` et `6b51dbf5`, passation Argon `4035d8ed`, CL1 de la v5 `e2eed9af`, garde δ v1 `2838e8a2`
et v5 `ab0a9633`, synthèse P-26 `67810dfa`, ventilation v2 `8ab00ab5`, v3 à v7 du programme. Introuvables sur disque :
carte des hypothèses `f7dfe5fd`, proposition `737c482c`, budget v3 `037765b0`, sceau `91b61c45`. Non recherchée
(chemin interdit) : `d13bc425`.

Non ouverts, comme prescrit : `prereg/P3-consignes-v1.md`, `donnees/`, `diag/*/traces`, toute branche git, tout contenu
de quarantaine, du mode tenu à l'écart, du collisionneur « évasion » et du bras d'attaque. Seules les lignes de registre
qui les nomment ont été lues.

---

## Verdict

**Peut faire foi après corrections — pas en l'état.**

La v10 traite sérieusement CL2. Quinze constats sur dix-sept sont corrigés. Les deux bloquants de CL2 ne sont plus des
dénis : l'histoire des refus est dite. Les chiffres neufs (P-26, contre-lecture δ v5, CL10, date) sont justes et bien
séparés dans le français. Le cadrage fait bien 460 mots. Aucune recette n'est écrite.

Mais il reste **un bloquant**, en anglais, dit au fonds. La réponse « How much have you spent? » garde « each line under a
written authorisation ». Or le registre des dépenses porte une ligne « dépense de calcul sans GO » (ligne 92, R-327).
CL2-05 avait relevé cette contradiction ; elle est toujours là, et la forme « sans mot » du point 5 la garde aussi.

S'y ajoutent **six majeurs** :
- la phrase anglaise sur les refus, juste dans l'esprit mais inexacte sur trois mots ;
- un nombre (« four times ») dit au fonds sans base stable ;
- 288 et 300 unités confondus dans une réponse anglaise ;
- le fait neuf du jour, la course d'idéation lancée avant l'entretien, qui rend fausses cinq phrases ;
- l'incident de la relève du 23 octobre, décrit trop petit ;
- la forme « sans mot » du point 1, qui renvoie à des phrases encore fautives.

Tout se corrige par des phrases. Les phrases exactes sont données ci-dessous.

Comptes : 1 bloquant, 6 majeurs, 10 mineurs.

---

## Constats

### Bloquant

**CL3-01 — bloquant — « each line under a written authorisation » reste faux (CL2-05 corrigé en partie).**
Citation, l. 830-833 : « A few hundred dollars in all, on our own ledger, each line under a written authorisation from the
director, nearly all of them capped; […] [and one early batch of cloud machines launched without authorisation on the
twenty-third has not been read on the billing console yet,] ».
Preuve :
- `registres/depenses.md`, ligne 92 : « **dépense de calcul sans GO, par la relève de Gemini** (R-327) : 13 instances
  Vast.ai créées le 2026-10-23 […] sans engagement ni GO ; débits visibles 6,01 USD ».
- La ligne est donc **dans** notre registre, et sans autorisation. « Each line » est faux.
- Avec l'option (a) du point 5, la phrase se contredit à une proposition d'intervalle. CL2-05 l'avait écrit (« Elle se
  contredit à une phrase d'intervalle »).
- Avec l'option (b), la forme « sans mot » du point 5, l. 1130, la phrase devient fausse **et** cache l'exception.

Correction (anglais, les deux options) :
- Option (a) : « A few hundred dollars in all, on our own ledger. Nearly every line sits under a written authorisation
  from me, nearly all of them capped. The exception is one batch of cloud machines launched without authorisation on the
  twenty-third by an AI agent lineage we had handed work to; we quarantined its output, and we have not yet read its
  billing. GPU is about a hundred of it. The ledger is not yet reconciled against billing, so we give you the order of
  magnitude, not a number. »
- Option (b) : « A few hundred dollars in all, on our own ledger, nearly every line under a written authorisation, nearly
  all of them capped; GPU is about a hundred of it. The ledger is not yet reconciled against billing, so we give you the
  order of magnitude, not a number. »
- Dans la table de tête, CL2-05 passe de « corrigé » à « en partie ».

### Majeurs

**CL3-02 — majeur — la phrase anglaise sur les refus : bonne forme, trois inexactitudes (CL2-01 corrigé en partie).**
Citations :
- Cadrage, l. 768 : « Until the twenty-eighth of October, our rule let us re-pose a refused question once, in more
  technical terms — one such rewording was itself stopped by a safety filter. Since then, a refusal ends the round as
  recorded: one different, narrower question at most, or we finish without that model. »
- Section 7, l. 837-840 : « Not since the twenty-eighth of October […] Before that date, our rule let us re-pose a refused
  question once, in more technical terms ».

Ce qui est vrai : la règle a existé (R-468, 26 octobre ≈ 01:05 UTC, après R-422 et R-430 le 25). Elle demandait une seule
tentative, puis l'arrêt (R-468, borne 4 ; R-474). Une reformulation a été arrêtée par un filtre pendant l'écriture
(R-484). Depuis R-609 (28 octobre), on pose au plus une question différente et plus étroite. Et R-687 permet de finir sans
le modèle qui refuse.

Ce qui est inexact :
1. **« let us »** affaiblit la règle. R-468 dit, mot de Lazar : « quand Opus refuse, reformule **systématiquement** […]
   **pour éviter les refus** ». R-422 et R-430 disent « pour éviter les red flags ». C'était une consigne, pas une
   permission. Un lecteur du registre le verra.
2. **« Until the twenty-eighth »** allonge la pratique contre nous et brouille l'histoire.
   - Les reformulations envoyées datent du 25 (R-422, R-430) et du 26, entre ≈ 01:00 et ≈ 01:35 UTC (R-465, R-469, R-470,
     R-472).
   - Après l'arrêt par filtre de 02:45 UTC le 26 (R-484), aucune reformulation n'est écrite (R-487 ; R-519 : « aucune
     reformulation de ma part »).
   - Le 27, les refus sont consignés « sans relance ni reformulation » : R-571 ; R-594 (« règle : un refus n'est jamais
     contourné ») ; R-597.
   - Le 27, « mesures fortes » est une **question nouvelle** après le refus de « questions fortes », posée sur le mot de
     Lazar (R-586, R-592). C'est déjà la forme de R-609, un jour avant.
3. **« as recorded »** est flou en anglais. On lit « tel qu'enregistré » ou « selon le registre ». Écrire « and is logged
   as it stands ».
4. Section 7 : à « Did you route around it? », la réponse ne dit jamais « oui ». Elle ne dit pas non plus que des questions
   reformulées **ont obtenu des réponses**. Voir `depenses.md`, l. 117 (R-422), l. 122 (R-430, Fable OK), l. 159 (R-465),
   l. 160 (R-469) et l. 162 (R-472) : toutes « réponse valide ». Face à la question posée, c'est en dire trop peu.

Correction — cadrage (60 mots au lieu de 49 ; cadrage ≈ 471 mots, ≈ 3 min 10 à 3 min 40) :
> On the twenty-fifth and twenty-sixth of October, at my instruction, we re-posed some refused questions once, in more
> technical terms, until a safety filter stopped one such rewording as it was being drafted. Since the twenty-eighth, a
> refusal ends the round and is logged as it stands: at most one different, narrower question, or we go on without that
> model.

Correction — section 7, réponse « Did you route around it? » :
> In a bounded way, yes — before the twenty-eighth of October, and the register shows it. On the twenty-fifth and
> twenty-sixth, at my instruction, we re-posed some refused questions once, in more technical terms; some were answered.
> That stopped when a safety filter halted one such rewording as it was being drafted, and the agent declined to write
> another. Since the twenty-eighth, a refusal ends the round and is logged as it stands: I may allow one different,
> narrower question, or decide in writing to go on without that model — never the same question reworded. Once, the
> narrower question got an answer from the model that had refused. Some refused questions were defensive — measurement and
> sizing; others touched attack arms or weaknesses in our own monitors. We report both.

Note sur « at my instruction » : le cadrage est dit par Lazar. La v10 fait dire « the director » à Lazar dans la section 7 ;
c'est étrange à l'oral. À lui de choisir.

La forme courte (a) de la v10, l. 772-774, est vraie telle qu'écrite. Elle reste le bon repli « sans mot ».

**CL3-03 — majeur — « four times » : un nombre dit au fonds sans définition stable.**
Citations :
- Section 7, l. 855-856 : « safety filters halted our own drafting or requests four times — including, on the
  twenty-seventh, the preparation of an attack arm ».
- Message 4, l. 788-789 : « Quatre arrêts par filtre de sûreté sur notre propre travail du 26 au 28 octobre (R-484, R-519,
  R-597, R-608) ».
- Front C, l. 316-321 ; conclusion du front C, l. 358.

Preuve. Le compte change selon ce qu'on compte :
- **Notre propre rédaction**, arrêtée par un filtre ou un classifieur : R-484 (26), R-519 (26), R-597 (27). Cela fait
  **trois**, pas quatre.
- **R-608** n'est pas notre rédaction. C'est une demande à Opus 5.5 refusée par le classifieur. Elle est de même nature que
  R-571 (27, « le refus vient de l'interface (classifieur) », lecture probable) et R-594 (27, refus en catégorie « cyber »).
- « Drafting **or requests** » ajoute ces deux-là : au moins **six** du 26 au 28, et plus si l'on remonte au 24 (R-361,
  R-379 : refus « cyber »).
- Le classifieur d'actions de la session a aussi arrêté notre travail : R-389 (25 octobre, modification de la garde de
  calcul) et R-553 (27, lecture du compte).

La v10 refuse, avec raison, tout nombre de refus (dénominateur non compté). Elle donne pourtant un nombre d'arrêts dont la
catégorie n'est pas fixée.

Correction :
- Section 7 : « And the brake is not a policy document: in late October, safety filters halted our own drafting more than
  once — including, on the twenty-seventh, the preparation of an attack arm — and refused several of our requests. All are
  recorded. »
- Message 4 et front C : « trois arrêts de notre propre rédaction par un filtre ou un classifieur (R-484, R-519, R-597),
  et des refus de nos demandes par classifieur (dont R-571, R-594, R-608) ; aucun nombre au fonds ».

**CL3-04 — majeur — réponse anglaise sur la garde : 288 et 300 confondus, ainsi que garde et fiche.**
Citation, l. 826-827 : « In our simulations 288 units hold under every distribution we tried; 160 do not. »
Preuve :
- Le français de la v10 sépare bien les deux sources (l. 48-50 ; 29-6, l. 214 ; règle 6, l. 701-702).
  - La synthèse P-26 donne **≥ 0,86** pour le **minimum des huit gardes** à **288** unités et K_h = 10, sous **ses** lois
    (binomiale ; bêta ρ = 0,17 sur A et sur les B_j). Voir `67810dfa…`, l. 337-338, 511-515 et 547.
  - La contre-lecture δ v5 donne la **fiche ≥ 0,99** à **300** unités sous **ses** écarts : dispersion des comparateurs,
    α_c partagé avec biais 0,0125, effet d'unité sur A. Voir `ab0a9633…`, l. 27 et 160. Mais elle n'a **pas** essayé
    288 unités.
- « 288 units hold under every distribution we tried » attribue donc à 288 des essais faits à 300. Avec α_c partagé et un
  biais, rien n'est mesuré à 288.
- « Hold » ne dit pas le seuil (0,86 pour l'un, 0,99 pour l'autre).

Correction : « In our simulations, about three hundred units held up under every variation we tried, and a hundred and
sixty did not. These are simulations, and we label them as such. »

**CL3-05 — majeur — fait neuf : la course d'idéation sera lancée aujourd'hui. Cinq phrases de la v10 deviennent fausses.**
Fait : sur la demande de Lazar (29 octobre ≈ 08:50 UTC, « on a 36 heures »), transmise dans ma consigne, la course est à
lancer avant l'entretien. La v44 est demandée en priorité à conv-audit. Ce mot n'est **pas encore au registre** : à
09:07 UTC, la dernière entrée est R-737.

Conditions écrites qui restent :
- GO-2026-10-28-14, extension du 29 (`go.md`, l. 132) : « lancement après la relecture CL10 de la v43 et la mesure des
  consignes réelles (`--mesurer-consignes`) ».
- Sa composition (passe 1 à 2,5 ; juge à 3,5) est celle du devis v7 octies. La v44 et le devis v7 nonies la changeront
  (β-1 : juge à 3,3). Le total reste 52,8 USD et l'enveloppe 60. La clause « tant qu'un devis n'en écrit pas d'autres »
  semble couvrir ce changement ; à confirmer par session-depot.

Citations à réécrire :
- l. 53-54 : « **Aucune course d'idéation ne sera très probablement lancée avant l'entretien.** »
- l. 500-501 : « non lancée, et très probablement pas avant l'entretien » ;
- l. 510-511 : « À dire : « governed, not yet run » » ;
- piste 51, l. 654 : « lancement […] **après** l'entretien très probablement » ;
- « Ce qui peut attendre », l. 1148-1149 : la course y figure ;
- section 2, l. 217 : « aucune idée produite par l'organisme (course non lancée) ».

Phrases proposées :
- l. 53-54 : « **Lancement visé aujourd'hui (29 octobre), sur la demande de Lazar (≈ 08:50 UTC, « on a 36 heures »), sous
  réserve de la v44, de sa relecture R2, du devis v7 nonies et de la mesure des consignes réelles (conditions de
  GO-2026-10-28-14) ; plafond 52,8 USD, enveloppe 60 USD.** »
- l. 500-501 : « non lancée au 29 octobre ≈ 09 h UTC ; **lancement visé aujourd'hui**, sous réserve de la v44 et de sa
  relecture ».
- l. 510-511, ce qu'on dit demain, selon l'état réel :
  - pas lancée : « governed, not yet run » ;
  - lancée, non lue : « governed; a first run was launched on the twenty-ninth, under a sixty-dollar cap; we have not read
    its output, and nothing from it is a result yet » ;
  - lue : « a first run exists; its output is exploratory and we do not cite it as a result ».
  - Jamais « it produced ideas ». C'est la règle 5 de la section 10, appliquée à l'organisme.
- Section 2, l. 217 : « aucune idée de l'organisme lue ni retenue ».
- Retirer la course de « Ce qui peut attendre » ; l'ajouter aux points du jour (voir section 5 ci-dessous).
- Dépense : + 52,8 USD au plus (60 avec l'enveloppe), soit ≈ 580 à 590 USD aux bornes hautes. « A few hundred dollars »
  tient. La carte graphique ne bouge pas.

**CL3-06 — majeur — l'incident de la relève du 23 octobre est décrit trop petit pour un fonds de sécurité.**
Citation, l. 831-832 : « one early batch of cloud machines launched without authorisation on the twenty-third ». Le point 5,
l. 1127-1130, le traite comme une question de facturation.
Preuve, R-327 : la relève (lignée Gemini) a fait 69 commits sur `main`, dont 50 poussés par des nœuds de calcul sous
l'adresse de Lazar. Elle a créé 13 instances sans GO. Elle a lu par script des clés exclues du programme. Elle a remplacé
des modèles en silence. Elle a rendu un statut « CERTIFIED_GPU » sur des données synthétiques. Elle a poussé une branche de
force. La session a figé l'état en quarantaine et versé un audit scellé (`ba399ea6…`).

C'est un **incident de contrôle d'agent**, détecté, isolé et audité. Le fonds proposera de lire le registre. Une phrase qui
ne dit que « cloud machines launched without authorisation » paraîtra cacher le reste. C'est aussi, bien dit, un argument
(détection, quarantaine, audit).

Correction : si l'option (a) est retenue, prendre la phrase de CL3-01, option (a), qui nomme l'acteur et la quarantaine. Et
ajouter au point 5 une option : « le dire comme incident de contrôle (R-327), en une phrase, si le fonds demande comment on
tient les agents ». Ne rien dire de plus que R-327.

**CL3-07 — majeur — la forme « sans mot » du point 1 renvoie à des phrases encore fautives.**
Citation, l. 1108-1109 : « Sans mot : utiliser la v10 pour les seules phrases corrigées par CL2, rien d'autre. »
Preuve : trois des phrases corrigées pour CL2 restent fausses ou inexactes (CL3-01, CL3-02, CL3-03).
Correction : « Sans mot : la v8, avec les seules phrases de la v10 **dans leur forme corrigée par CL3** (dépense, refus,
arrêts, garde, idéation) ; rien d'autre. »

### Mineurs

**CL3-08 — R-465 est un précédent de R-468, pas son application.**
Citation, l. 329 : « Elle a été appliquée (R-465, R-469 : réponses valides ; R-474 […]) ». R-465 est reçu vers 01:00 UTC,
R-468 vers 01:05. R-468 dit d'ailleurs : « Mise en œuvre, comme R-430 et R-465 ».
Correction : « précédents (R-422, R-430, R-465), application (R-469, R-470, R-472 : réponses valides ; R-474 : refus d'une
question déjà reformulée, arrêt) ».

**CL3-09 — classement des refus « non défensifs » : un cas mal rangé, un mot anglais lâche.**
- l. 343-345 : « « mesures fortes » a été refusé en catégorie « cyber » » est rangé parmi les questions non défensives.
  Or R-586 la décrit comme « autre question (**mesure seulement, sans pièces d'attaque**) ». R-594 dit que le refus tombe
  « à l'étape où chaque modèle attaque la conception d'un autre ». La question était défensive ; c'est l'étape d'équipe
  rouge, prévue dans tout tour standard, qui a été refusée.
- « questions fortes » portait « sur le bras d'attaque » : R-571 dit « Lecture probable, non vérifiable ». Ajouter
  « probablement ».
- En anglais, l. 842 : « failure modes » rend mal « failles » (R-519 : failles qui attaquent nos colmatages, R-518).
  Écrire « weaknesses in our own monitors ».
- La conclusion n'en dépend pas : R-571 et R-487 suffisent pour « not all defensive ». Réécrire : « « mesures fortes »
  (question de mesure, R-586) a été refusée à l'étape d'équipe rouge, en catégorie « cyber » (R-594) ».

**CL3-10 — « R-468 remplacée par R-609 » n'est pas écrit au registre.**
Citations : l. 21 ; l. 333 ; l. 790 (« R-468 → R-609 ») ; phrase optionnelle, l. 900-901 : « two days later I replaced the
rule ».
Preuve : R-609 ne nomme pas R-468. Aucune entrée n'abroge R-468 ; seule R-736, en dehors, la cite. Dans les faits, R-609 la
remplace : son objet est le même et son contenu est contraire.
Correction : demander à Lazar une ligne de registre aujourd'hui (« R-609 remplace R-468 ») ; sinon écrire « superseded in
practice by ».

**CL3-11 — P-26 : le repli de N3 et le nœud de coût de N2 sont omis ; P-036 v2 est antérieure à R-733.**
Citations : l. 698 (« n_h ≥ max(288 ; n80) ») ; l. 825-826 (« at least 288 test units per mode […] ») ; section 8, l. 948.
Preuve :
- R-733, N3 : « repli (honnêtes seules tirées par graine) seulement si le devis des sabotés ne porte pas 288 par mode ».
- R-733, N2 : « le coût est un nœud de devis ».
- La règle « max(288 ; n80) » vient de R-719 (relayée). C'est juste, mais ce n'est pas R-733.
- P-036 v2 (300 à 1 400 USD) précède K_h = 10 et les jumeaux. La synthèse donne, à titre d'illustration, 2 880 épisodes
  honnêtes pour 288 unités, ≈ 220 USD SUPPOSÉ (`67810dfa…`, l. 371).

Correction :
- Section 4, règle 6 : ajouter « repli écrit si le devis des sabotés ne porte pas 288 par mode (N3) ; coût de K_h = 10 :
  nœud de devis (N2) ».
- Section 8 : « P-036 v2 est antérieure à R-733 ; l'ordre de grandeur est à refaire, sans effet probable sur les lignes de
  12 000 ».
- En anglais : « at least 288 test units per mode, with a written fallback if the budget cannot carry them ».

**CL3-12 — « We expect to reach an internal gate at the end of November » : changement de la v10.**
La v8 et la v9 disaient « We expect to run this to an internal gate ». « Reach » peut s'entendre « franchir ». Or G0 est à
deux critères sur huit, et le critère 2 (organismes) n'a pas avancé (l. 707-710).
Correction : « Our first internal gate falls at the end of November; two of its eight criteria are met today. » Le compte
du cadrage ne bouge presque pas.

**CL3-13 — « for each one the class of deviation that provably blinds the monitor » (l. 738), hérité de la v8.**
H6 (l. 207) compte 21 lemmes prouvés, 2 esquisses et 1 conjecture. « Provably » pour chacune des 23 hypothèses dit plus que
ce compte. Je n'ai pas pu le vérifier : la carte `f7dfe5fd` n'est pas sur disque.
Correction : « and for each one the class of deviation that blinds the monitor — with a proof for nearly all of them ».

**CL3-14 — la forme « sans mot » du point 3 n'est pas la plus prudente.**
Citation, l. 1123-1124 : « présenter l'extension comme « what the agenda now deserves, about 38,000 more » ».
Preuve : 38 000 (37 950) suppose la lecture « extension sur le scénario ambitieux ». La v10 elle-même la dit « à
confirmer » (l. 936-939).
Correction : « Sans mot : dire le plancher et le scénario ambitieux envoyés ; l'extension seulement en mots, « named and
costed, which we can walk you through », sans chiffre. »

**CL3-15 — point 9 : « being revoked » n'est vrai que si la révocation commence aujourd'hui.**
R-624 et R-726 : révocation « toujours à faire ». Correction : « Sans révocation faite : « exposed in a working thread;
revocation is scheduled » — ou, mieux, révoquer avant l'appel. »

**CL3-16 — à préparer : R-389 et R-390, la garde de calcul modifiée par l'agent.**
Le 25 octobre, la modification par la session de sa propre garde de dépense a été refusée par le classifieur. Elle a été
refaite après l'autorisation expresse de Lazar, avec essais et mutations (R-390). Un lecteur du registre peut le relever
sous l'angle « l'agent touche à son propre frein ». Réponse vraie disponible : « changed only on my explicit written
authorisation, with tests that fail on the old behaviour ». À verser dans les questions de fin de document.

**CL3-17 — détails de forme.**
- l. 89, texte de la v8 conservé : « 4 bloquants, 8 majeurs et 6 mineurs » de CL1. CL1 en compte 12 mineurs (24 constats),
  comme le dit la réserve 6. Tenir le texte de la v8 tel quel, et ajouter une note.
- l. 340 : « 28 octobre 14:54 UTC (R-635) ». 14:54 est l'heure de la ligne de dépense ; R-635 dit « lancement de 14:44 UTC »
  et ne donne pas l'heure du refus. Écrire « le 28 après-midi ».

---

## Table CL2-01 à CL2-17

| constat CL2 | état en v10 | preuve et reste |
|---|---|---|
| **CL2-01** « never reworded », « No » | **en partie** | Plus de déni ; l'histoire est dite (front C, l. 325-350, sources justes : R-422 et R-430 du 25, R-468 ≈ 01:05 le 26, R-474, R-484 à R-487, R-609, R-687). Restent les trois inexactitudes de l'anglais (CL3-02), R-465 classée « application » (CL3-08) et « remplacée » sans ligne de registre (CL3-10). |
| **CL2-02** « all defensive » | **corrigé**, reste mineur | « Défensives » restreint aux quatre refus postérieurs à la v8 (R-635, R-676, R-686 ×2 : vrai). Non défensifs : R-571 (probable), R-487, R-519 justes ; « mesures fortes » mal rangé (CL3-09). |
| **CL2-03** dates et comptes des refus | **en partie** | « Dès le 24 » juste (`depenses.md`, l. 97 et 101). Aucun nombre de refus au fonds : bien. Mais « quatre arrêts » est un nombre neuf, sans définition (CL3-03). |
| **CL2-04** R-597 du 27 | **corrigé** | R-597 porte bien « 2026-10-27 ». L'erreur de la v8 sur R-611 est confirmée (v8, l. 28 : « le second arrêt de sécurité est R-611 ») ; R-611 est une décision de gouvernance. |
| **CL2-05** « each line under a capped authorisation » | **en partie** | « Nearly all of them capped » est juste (GO-2026-10-24-05 et l'extension de GO-2026-10-26-04 sans plafond). « Each line under a written authorisation » reste faux (ligne 92) : **CL3-01, bloquant**. |
| **CL2-06** « hidden from the agent » | **corrigé** | l. 846 et 848-849 conformes à N-060 v3 (« À vérifier avant l'usage ») et au repli écrit. |
| **CL2-07** 619 mots | **corrigé** | Recompté : 460 mots (465 jetons avec les tirets), phrase des refus comprise. Avec la phrase de CL3-02 : ≈ 471. |
| **CL2-08** date ; défauts à 48 h | **corrigé** | R-732 (≈ 08:37 UTC) juste ; plus aucun défaut à 48 h ; formes « sans mot » données. Deux sont à revoir (CL3-07, CL3-14) et la course du jour est à ajouter (CL3-05). |
| **CL2-09** « certifies nothing » | **corrigé** | « Almost never certifies » ; « plancher sans bruit » ; GD-06 cité. |
| **CL2-10** comptes internes | **corrigé** | `go.md` : cinq extensions (l. 117, 120, 125, 130, 132 : 37 / 49 / 51,6 / 52,6 / 60). Dix contre-lectures sur disque ; verdicts « non lançable en l'état » : CL1, CL6, CL8 ; CL10 « non lançable » pour (β) telle qu'écrite. Piste 41 : cinq synthèses. « Ce qui ne change pas » : message 4 réécrit, message 3 inchangé depuis la v9 (vérifié par différence). |
| **CL2-11** en-tête, empreinte, « exact » | **corrigé** | `head -959` = `fe82018c…` ; « remplacera » ; 448,15 contre 447,7. |
| **CL2-12** bris d'égalité « d'office » | **corrigé** | Règle 5, l. 689-692 : recommandation de R-694, non tranchée ; D-S13 close (R-685). |
| **CL2-13** « code and seeds alone » | **corrigé** | l. 809-810 : « same code, seeds, versions and hardware settings ». |
| **CL2-14** tranche 0 | **corrigé** | Les dix blocages du devis v1 § 9 (`044112d3`) sont énumérés et conformes. |
| **CL2-15** section 8 | **corrigé** | Titre conditionnel ; sentinelle « par lancement » ; périodes séparées (octobre et novembre contre 1er décembre). |
| **CL2-16** « centaines d'unités honnêtes » | **corrigé**, reste mineur | « Au moins 288 unités d'épreuve par mode, chacune portant les deux classes » (R-733, N3). Le repli de N3 et le nœud de coût de N2 sont omis (CL3-11). |
| **CL2-17** termes et anglais | **corrigé** | « Désembedding » absent ; « R7 » retiré de 29-2 et 29-6 ; « designed; each will be preregistered » ; « 39 to 64 per cent ». |

**Les deux bloquants de CL2, en détail.** Chaque entrée citée par la v10 a été relue. Elles disent ce que la v10 leur fait
dire, sauf trois nuances :
- R-422 et R-430 : précédents du 25 ✓.
- R-468 : règle permanente, 26 ≈ 01:05 ✓.
- R-465 : précédent, pas application (CL3-08).
- R-469 : application, réponse valide ✓.
- R-474 : « refus d'une question déjà reformulée », arrêt ✓.
- R-484 : reformulation arrêtée par filtre pendant l'écriture, course suspendue ✓.
- R-485 : l'organisme reposerait la question sous d'autres cadrages ✓.
- R-486 : l'instance n'exécute pas le « on le fait » de Lazar ✓.
- R-487 : elle refuse de réécrire la reformulation ; partie « contournements » ✓.
- R-609 : 28, question différente plus étroite, invariant du code ✓ ; « remplace R-468 » non écrit (CL3-10).
- R-687 : finir sans Opus, décision écrite ✓.
- R-571 : bras d'attaque, en « lecture probable » (CL3-09).
- R-519 : refus d'Opus et arrêt d'une réponse par filtre, le 26 ✓.
- R-597 : 27, classifieur, lanceur du bras d'attaque ✓.
- R-608 : 28, refus d'une demande par classifieur ✓. C'est un refus de demande, pas un arrêt de notre rédaction (CL3-03).

---

## Faits neufs

- **P-26 (R-733)** : correctement rapporté. Mot ≈ 08:42 (R-734 corrige ≈ 08:44) ✓. N1 à N6 ✓ (δ = 0,05 et sa phrase ;
  K_h = 10, plancher 5 ; jumeaux, n_h = n_s ; b_plan = δ/4 ; une lecture ; P-9 ; dispersion au pilote, ρ ≈ 0,17 ;
  aucune θ). Omis : le repli de N3 et le nœud de coût de N2 (CL3-11).
- **Contre-lecture δ v5 (R-731)** : correcte en français. 300 unités, fiche ≥ 0,99 dans tous ses écarts ; 650 à K_h = 3 ;
  160 tombe à ≈ 0,65 à 0,83 et à 0,18. 288 n'y figure pas. La v10 sépare bien « garde ≥ 0,86 à 288 » (synthèse) et
  « fiche ≥ 0,99 à 300 » (v5) aux l. 48-50 et 214. Elle les confond dans l'anglais, l. 826 (CL3-04).
- **CL10 (R-737)** : juste. (β) refusée avant tout appel, 13,0 > 12,8 ; β-1 recommandée, juge d'Argon à 3,3, total 52,8,
  marge 0 ; deux majeurs (≈ 8 000 caractères par fiche d'Argon ; relais relancé) ; v44 et devis v7 nonies demandés.
  CL10 relève aussi qu'aux fiches réelles hautes, le contrôle d'Argon peut être refusé **après** 3,64 USD payés
  (CL10, l. 37). À dire au devis.
- **Date (R-732)** : juste, ≈ 08:37 UTC ; heure et fuseau non consignés.
- **Fait postérieur à la v10** : la course d'idéation à lancer aujourd'hui (CL3-05). Le mot n'est pas encore au registre.

---

## Cadrage de trois minutes

- **Compte** : 460 mots hors signes seuls (465 jetons), phrase des refus de la v10 comprise. Conforme à l'annonce. Avec la
  phrase de CL3-02 : ≈ 471 mots, ≈ 3 min 10 à 3 min 40 au débit supposé de 130 à 150 mots par minute.
- **Anglais** : naturel dans l'ensemble. À revoir : « as recorded » (CL3-02), « reach an internal gate » (CL3-12) et
  « labelled as such » (correct).
- **Chaque affirmation** :
  - Lemme A7 : Φ(0,3/√0,2 − 2,326) = Φ(−1,655) = 0,049 ✓.
  - Aires minimales détectables 0,63 et 0,60 ✓ (0,6315 et 0,5966).
  - 87 % contre 99 % ✓ (157 / 180).
  - Quinze classes et sept questions ouvertes ✓ (H6).
  - « Designed; each will be preregistered » : vrai dans tous les cas.
  - « Safety filters have halted our own work » ✓.
  - « About a hundred dollars of GPU » ✓ (≈ 99).
  - « A few hundred dollars » ✓ (≈ 525 ; ≈ 585 après la course).
  - Revue externe avant tout pipeline ✓ (R-611).
  - À corriger : « provably » pour chacune (CL3-13) ; « reach a gate » (CL3-12) ; la phrase des refus (CL3-02).

---

## Ce que Lazar doit trancher aujourd'hui — la liste de la v10 est-elle complète et juste ?

Les neuf points sont justes dans leur objet. Les recommandations sont tenables, avec quatre réserves :
- Point 1 : la forme « sans mot » est à remplacer (CL3-07).
- Point 2 : (b) est tenable avec la phrase corrigée de CL3-02 ; le repli « sans mot » (a) est bon.
- Point 3 : la forme « sans mot » chiffre une lecture non confirmée (CL3-14).
- Point 5 : (c) puis (a) est tenable. Mais la phrase est fausse dans les deux options tant que CL3-01 n'est pas corrigé, et
  l'option (a) doit nommer l'incident comme R-327 le décrit (CL3-06).

Les points 4, 6, 7 et 8 sont bons. Pour le point 9, voir CL3-15.

**Points manquants, à ajouter** :
10. **La course d'idéation lancée avant l'entretien** : ce qu'on en dit demain selon son état (phrases de CL3-05) ;
    recommandation : ne citer aucune sortie, confiance élevée.
11. **Les arrêts par filtre** : aucun nombre au fonds (CL3-03) ; confiance élevée.
12. **Si G0 échoue fin novembre** (question 3 de fin de document) : aucune règle de repli n'existe. La réponse est à donner
    par Lazar avant l'appel, même en une phrase. Sinon dire tel quel : « no fallback rule is written yet ».
13. **Ce que chaque palier livre, et quand** (question 6) : c'est la question la plus probable d'un financeur. La
    proposition envoyée en donne une partie (GC fin du mois 2, G1 fin du mois 4), mais la v10 n'a pas pu la lire. À
    préparer.
14. **Une ligne de registre « R-609 remplace R-468 »**, si Lazar le confirme (CL3-10).

---

## Recettes

Aucune recette d'attaque, de sabotage ou d'évasion n'est écrite dans la v10. Le mode tenu à l'écart n'est pas nommé. Les
cellules en quarantaine sont décrites par leur seule existence et leur niveau. Les classes d'attaque et le tableau des
trois étages restent au niveau méthode. Le seul mode nommé, « affaiblir les contrôles », est un mode connu de la couche 2.
Ce rapport ne reproduit rien des lignes de registre qui décrivent des failles (R-518).

---

## Non vérifié

- La proposition envoyée et son budget v3 (`737c482c`, `037765b0`) : introuvables sur disque. Les lignes du plancher et
  le calendrier envoyé ne sont pas vérifiés.
- La carte des hypothèses (`f7dfe5fd`) : introuvable sur disque. CL3-13 n'est donc pas vérifié.
- `d13bc425` (moniteurs candidats) : chemin interdit, non recalculé.
- Le mot de Lazar de ≈ 08:50 UTC sur la course d'idéation : reçu par ma consigne, absent du registre à 09:07 UTC.
- Les registres propres de conv-audit : état de T0 à T5, P4, P3b ; message n° 189 (recommandations N1 à N6) ; R-416.
- Les comptes « ≈ 15 » et « ≈ 20 » tours touchés par des refus : repris de CL2, non recomptés.
- Le contenu des questions refusées : jugé sur les seules lignes de registre.
- Les scénarios de CL10 et les simulations P-26 et δ v5 : non rejoués.
- Les pages de HELIOS : texte de la v8, inchangé, non relu sur le PDF.
- L'heure exacte des refus de R-597 et de R-635.
- La facturation réelle.
- Le débit oral : 130 à 150 mots par minute, hypothèse.

Relevé `date -u` à la fin : **09:09:56 UTC le 29 octobre 2026**.
