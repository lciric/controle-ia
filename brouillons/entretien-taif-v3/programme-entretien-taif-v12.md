# Programme pour l'entretien Transformative AI Fund (Lowe Lundin) — v12 (finition)

**Entretien : vendredi 30 octobre 2026** (R-732), **demain** ; heure et fuseau non consignés.

Lignée session-depot, sous-agent déclaré Opus 5.5, auteur des v9 à v11, 29 octobre 2026. Relevé `date -u` au début :
**09:20:01 UTC** ; à la fin : dernière ligne. Applique la contre-lecture CL4 de la v11 (`contre-lecture-v11-cl4.md`,
`6dafcf06…`, sous-agent neuf : « peut faire foi après corrections », 0 bloquant, 1 majeur, 10 mineurs), phrases exactes reprises ;
aucune jugée manifestement fausse. **Registre des décisions relu jusqu'à R-739** : R-737 et avant (`head -965` = `d3d7fcc8…`) ;
**R-738** (mot de Lazar de ≈ 08:50 UTC, course d'idéation visée aujourd'hui) versée à 09:11 UTC, prise en compte par CL4 ;
**R-739** (versement de CL4 ; précise que « v10 (`37fe5c97`) » dans R-738 est le commit de versement, l'empreinte du fichier
étant `eb87b8a8…`). **Remplacera**, sur le mot de Lazar, la v8 (`7917ed02…`, qui fait foi jusque-là) ; v9 (`1e0969d8…`), v10
(`eb87b8a8…`) et v11 (`44c87a57…`) gardées telles quelles (R12).

## Ce que la v12 corrige — les constats de CL4

| constat | gravité | traitement | où |
|---|---|---|---|
| **N-01** la v11 ignore R-738 | majeur | **corrigé** : en-tête ci-dessus ; « inscrit en R-738 » au front E, à la piste 51, au point 10 et dans « non vérifié » ; **point 15 ajouté** : la règle de corpus relayée par R-738 (non confirmée par Lazar dans la session de session-depot) est à trancher avant le lancement — recommandation : extraits actuels aujourd'hui, texte intégral au tour suivant s'il est confirmé ; **rien n'en est dit au fonds** | en-tête ; front E ; piste 51 ; points 10 et 15 |
| **N-02** R-470 « non une application » | mineur | **corrigé** : « extension à Fable, appliquée aussitôt » ; la note de la v11 est marquée inexacte | front C ; en-tête de la v11 conservé |
| **N-03** repli (a) « as recorded » | mineur | **corrigé** : « and is logged as it stands … or go on without that model » | section 5 |
| **N-04** durée du cadrage | mineur | **corrigé** : ≈ 3 min 10 à 3 min 35 pour 470 mots | section 5 |
| **N-05** « redefined it first », « falls at » | mineur | **corrigé** : « so we redefined the judging before use » ; « Our first internal gate is due by the end of November » | section 5 |
| **N-06** « not yet read its billing » | mineur | **corrigé** : « its full billing » (6,01 USD sont lus) | section 7, forme (a) |
| **N-07** « a false certification » | mineur | **corrigé** : « a "certified" label on synthetic data » | section 7 |
| **N-08** quatrième état de la course | mineur | **corrigé** : « lancée puis arrêtée », phrase de CL4 ; « last night » si le lancement glisse après minuit UTC | front E ; point 10 |
| **N-09** question 8, réponse à étoffer | mineur | **corrigé** : réponse de CL4 reprise ; « selon CL3 » retiré (R-389, R-390 vérifiés par CL4) ; idem pour R-379 et R-553 | questions de fin ; front C |
| **N-10** facultatif : « provably » du pitch ; 15 + 7 ≠ 23 | mineur | **fait, sûr** : « in advance and, wherever we can, provably » ; « one comes from our own design » ajouté au cadrage (cohérent avec H6 : 15 + 1 + 7 = 23) ; pour tenir 470 mots, « One result gives the flavour » et « we have » retirés | section 1 ; section 5 |
| Réserve hors v11 (R-738 cite `37fe5c97`) | — | **réglée au registre** par R-739 (commit, non empreinte) | en-tête |

**Cadrage : 470 mots** (≤ 470), même méthode de compte (mots anglais séparés par des espaces, signes seuls exclus).

---

## En-tête de la v11 (conservé)

*(Titre de la v11.)*

**Entretien : vendredi 30 octobre 2026** (R-732), **demain** ; heure et fuseau non consignés.

Lignée session-depot, sous-agent déclaré Opus 5.5, auteur de la v9 et de la v10, 29 octobre 2026. Relevé `date -u` au début :
**09:10:51 UTC** ; à la fin : dernière ligne. Applique la contre-lecture CL3 de la v10 (`contre-lecture-v10-cl3.md`,
`bfc511bf…`, sous-agent neuf, lue en entier), en reprenant ses phrases exactes ; aucune n'a été jugée manifestement fausse ;
deux ajustements de forme sont dits dans la table (CL3-02, CL3-08). **Remplacera**, après une relecture rapide et le mot de Lazar,
la v8 (`7917ed02…`, qui fait foi jusque-là) ; v9 (`1e0969d8…`) et v10 (`eb87b8a8…`) gardées telles quelles (R12). Registre des
décisions relu jusqu'à R-737 (`d3d7fcc8…` à 09:12 UTC) ; aucune entrée nouvelle depuis la v10. *[v12, N-01 : faux — R-738 avait été versée à 09:11:18 UTC.]*

## Ce que la v11 corrige — les dix-sept constats de CL3

| constat | gravité | traitement | où |
|---|---|---|---|
| **CL3-01** « each line under a written authorisation » | bloquant | **corrigé** : phrase de CL3 reprise, deux formes (incident dit, ou non) ; jamais « each line » ; CL2-05 passe à « en partie » en v10 | section 7, « How much have you spent? » ; point 5 |
| **CL3-02** phrase des refus : « let us », « until the 28th », « as recorded », pas de « oui » | majeur | **corrigé** : phrase du cadrage et réponse « Did you route around it? » de CL3 reprises mot pour mot (« In a bounded way, yes — before the twenty-eighth… ») ; insérée dans le cadrage ; **à valider par Lazar** ; forme courte gardée en repli | section 5 ; section 7 ; point 2 |
| **CL3-03** « four times » | majeur | **corrigé** : trois arrêts de notre rédaction (R-484, R-519, R-597) et des refus de nos demandes (R-571, R-594, R-608) ; **aucun nombre au fonds** ; anglais de CL3 repris (« more than once ») | front C ; message 4 ; section 7 ; point 11 |
| **CL3-04** 288 et 300 confondus | majeur | **corrigé** : « about three hundred units held up under every variation we tried, and a hundred and sixty did not » ; le français sépare garde ≥ 0,86 à 288 (synthèse) et fiche ≥ 0,99 à 300 (v5) | section 7 ; section 4, règle 6 |
| **CL3-05** course d'idéation visée aujourd'hui | majeur | **corrigé** : phrases de CL3 reprises ; trois formes à dire demain selon l'état (pas lancée, lancée non lue, lue), **aucune sortie citée** ; retirée de « ce qui peut attendre » ; dépense + 52,8 au plus | front E ; section 2 ; piste 51 ; message 3 ; point 10 |
| **CL3-06** incident du 23 octobre décrit trop petit | majeur | **corrigé** : deux formes présentées à Lazar — en entier (acteur, quarantaine, et au besoin incident de contrôle selon R-327, sans rien de plus) ou pas du tout ; la forme intermédiaire est retirée | section 7 ; point 5 |
| **CL3-07** forme « sans mot » du point 1 | majeur | **corrigé** : « la v8, avec les seules phrases de la v11 dans leur forme corrigée par CL3 » | point 1 |
| **CL3-08** R-465 précédent, non application | mineur | **corrigé** : précédents R-422, R-430, R-465 ; application R-469, R-472 (réponses valides), R-474 ; *ajustement* : R-470 est l'extension de la règle à Fable, non une application, je l'écris ainsi *[v12, N-02 : inexact — R-470 étend la règle et l'applique aussitôt]* | front C |
| **CL3-09** « mesures fortes » mal rangé ; « failure modes » | mineur | **corrigé** : question de mesure (R-586) refusée à l'étape d'équipe rouge, « cyber » (R-594) ; « probablement » pour R-571 ; « weaknesses in our own monitors » | front C ; section 7 |
| **CL3-10** « R-468 remplacée » non écrit au registre | mineur | **corrigé** : « dans les faits » / « superseded in practice » ; ligne de registre demandée (point 14) | front C ; message 4 ; section 7 |
| **CL3-11** repli de N3, coût de N2, P-036 v2 antérieure | mineur | **corrigé** : règle 6 complétée ; « with a written fallback if the budget cannot carry them » ; section 8 annotée | section 4 ; section 7 ; section 8 |
| **CL3-12** « reach an internal gate » | mineur | **corrigé** : « Our first internal gate falls at the end of November; two of its eight criteria are met today. » | section 5 |
| **CL3-13** « provably » pour chacune | mineur | **corrigé** : « with a proof for nearly all of them » (non vérifié : carte absente du disque) | section 5 |
| **CL3-14** « sans mot » du point 3 chiffre une lecture non confirmée | mineur | **corrigé** : extension en mots, sans chiffre | point 3 |
| **CL3-15** « being revoked » | mineur | **corrigé** : révoquer avant l'appel ; sinon « revocation is scheduled » | point 9 |
| **CL3-16** garde de calcul modifiée par l'agent | mineur | **ajouté** aux questions de fin (R-389, R-390), réponse vraie de CL3 | questions de fin, point 8 |
| **CL3-17** « 6 mineurs » (CL1) ; heure de R-635 | mineur | **corrigé** : note ajoutée au texte conservé de la v8 ; « le 28 après-midi » | historique ; front C |

**Points à trancher ajoutés sur demande de CL3** : 10 (course d'idéation), 11 (aucun nombre d'arrêts), 12 (si G0 échoue), 13
(livrables par palier), 14 (ligne de registre R-609 / R-468). **Cadrage** : 467 mots (sous 470), phrase des refus comprise.

**Ce qui ne change pas** depuis la v10 : la demande (aucun chiffre) ; P-26 ; le front D ; aucune recette, rien de la quarantaine
ni du mode tenu à l'écart. La table « Ce que la v10 corrige » (CL2) reste dans la v10 (`eb87b8a8…`) ; son en-tête est conservé
ci-dessous pour la traçabilité.

---

## En-tête de la v10 (conservé)

*(Titre de la v10.)*

**Entretien : vendredi 30 octobre 2026** (R-732, mot direct de Lazar ≈ 08:37 UTC le 29), **c'est-à-dire demain** ; heure et
fuseau non consignés.

Lignée session-depot, sous-agent déclaré Opus 5.5 par l'environnement, **auteur de la v9** (donc pas contre-lecteur de celle-ci),
29 octobre 2026, sur la demande transmise par la session : corriger la contre-lecture CL2 de la v9 et intégrer les faits
nouveaux. Relevé `date -u` au début de l'écriture : **08:48:48 UTC le 29 octobre 2026** ; à la fin : voir la dernière ligne.

**Remplacera**, après la contre-lecture CL3 prévue (R-736) et le mot de Lazar, la v8 (`7917ed02…`, qui fait foi jusque-là,
R-623) et la v9 (`1e0969d8…`, jamais validée) ; toutes deux gardées telles quelles (R12, vérifiées par empreinte). Contre-lecture
traitée : `brouillons/entretien-taif-v3/contre-lecture-v9-cl2.md` (`49d94381…`, R-736), lue en entier. Registres relus à
l'écriture : `registres/decisions.md` jusqu'à R-737 (`d3d7fcc8…` à 08:56 UTC), `registres/go.md` (`f637f3ac…`),
`registres/depenses.md` (`34025262…`) ; ces registres vivent, leurs empreintes ne valent que pour l'heure de lecture. *(CL2-11 :
l'empreinte `fe82018c…` que la v9 disait « jusqu'à R-728 » était celle du registre jusqu'à R-731.)*

## Ce que la v10 corrige — les dix-sept constats de CL2

| constat | gravité | traité ? | où et comment | source |
|---|---|---|---|---|
| **CL2-01** « never reworded », « Did you route around it? No » | bloquant | **corrigé** | Front C : l'histoire dite telle quelle — règle de reformulation du directeur avant le 28 (R-422, R-430, puis R-468), appliquée (R-465, R-469, R-474), bornée (R-484 à R-487), remplacée le 28 par R-609, plus la poursuite sans le modèle (R-687). Section 5 : phrase anglaise courte proposée, **à valider par Lazar** (point 2), avec une variante bornée à la date. Section 7 : la réponse ne commence plus par « No » mais par « Not since the twenty-eighth ». Message 4 réécrit | R-422, R-430, R-465, R-468, R-469, R-474, R-484 à R-487, R-609, R-687 |
| **CL2-02** « all the refused questions were defensive » | bloquant | **corrigé** | « Défensives » est restreint aux quatre refus postérieurs à la v8 (R-635, R-676, R-686) ; les refus antérieurs non défensifs sont nommés (R-571, « mesures fortes », R-487, R-519) ; en anglais : « The recent refusals were on defensive questions…; earlier ones were also on questions about attack arms and failure modes. We report both. » | R-487, R-519, R-571 ; `registres/depenses.md`, 27 octobre 20:27 UTC |
| **CL2-03** « dès le 26 », « au moins dix » | majeur | **corrigé** | Refus dès le 24 octobre ; ≈ 15 tours du 26 au 29 et ≈ 20 du 24 au 29 au compte de CL2 (non recompté ici, dénominateur non compté) ; **aucun nombre dit au fonds**. Arrêts par filtre sur notre propre travail : quatre, du 26 au 28 (R-484, R-519, R-597, R-608), et non deux | CL2 ; R-484, R-519, R-597, R-608 |
| **CL2-04** R-597 daté du 28 | majeur | **corrigé**, et **une erreur de plus trouvée** | R-597 est du 27 octobre (front C, section 7). En relisant R-611 pour la v10 : la v8 le citait comme second arrêt de classifieur ; c'est une **décision de gouvernance** (gel du pipeline offensif jusqu'à une revue externe). Corrigé front C, message 4, section 7, réserve 9 | R-597, R-608, R-611 |
| **CL2-05** « each line under a capped written authorisation » | majeur | **en partie** *(v11 : « each line under a written authorisation » restait faux, CL3-01)* | « under a written authorisation from the director, nearly all of them capped » (section 7, deux réponses) : GO-2026-10-24-05 et les extensions de GO-2026-10-26-04 sont sans plafond | `registres/go.md` |
| **CL2-06** « hidden from the agent » comme un fait | majeur | **corrigé** | « kept hidden from the agent, a property we check before use » ; ajout du repli : « if it fails its tests we report the condition only and claim no harm » | N-060 v3 (`2b448f69…`), « ce que la décision ne fixe pas » |
| **CL2-07** cadrage de 619 mots | majeur | **corrigé** | Ramené à **460 mots**, phrase des refus comprise (≈ 3 min 05 à 3 min 30) ; coupés : deux lemmes, la reproductibilité (passée en section 7), la reprise étroite | section 5 |
| **CL2-08** date de l'appel ; défauts à 48 h après l'appel | majeur | **corrigé** | Date en tête, section 9 réécrite (« demain »), réserve 5 réécrite ; plus aucun défaut à 48 heures : chaque point dit « aujourd'hui », la recommandation et la forme prudente si Lazar n'a pas tranché ; ce qui peut attendre est séparé | R-732 |
| **CL2-09** « certifies nothing below ~150 » | mineur | **corrigé** | « almost never certifies » ; « plancher sans bruit », des certifications isolées existant sous le plancher (GD-06) | `contre-lecture-garde-delta-v1.md` (`2838e8a2…`) |
| **CL2-10** comptes internes | mineur | **corrigé** | Cinq extensions du GO de l'idéation (37, 49, 51,6, 52,6, 60), non six ; dix contre-lectures de l'idéation, **désormais toutes rendues** (CL10, R-737), dont quatre « non lançable en l'état » ; piste 41 : cinq synthèses ; la liste « ce qui ne change pas » est réécrite ci-dessous | `registres/go.md` ; R-737 |
| **CL2-11** en-tête, « remplace », « total exact » | mineur | **corrigé** | « Remplacera, après CL3 et le mot de Lazar » ; empreinte du registre rectifiée (ci-dessus) ; « 447,7 » dit somme des sous-totaux arrondis (la somme des lignes fait 448,15 ; effet nul sur ≈ 525) | note `93969946…` |
| **CL2-12** bris d'égalité « d'office » présenté comme décision | mineur | **corrigé** | Section 4, règle 5 : recommandation du tour complémentaire (R-694), **non tranchée** ; seule D-S13 est close (R-685) | R-685, R-694 |
| **CL2-13** « from code and seeds alone » | mineur | **corrigé** | « from the same code, seeds, versions and hardware settings » (le palier au bit près exige les mêmes fils de calcul) | R-667, R-679 |
| **CL2-14** tranche 0 : blocages partiels | mineur | **corrigé** | « dix blocages gratuits (devis v1, § 9) », énumérés ; le rejeu v1 est lu, la porte des scores finis reste | devis v1 `044112d3…`, § 9 ; R-704 |
| **CL2-15** section 8 : titre sans condition, sentinelle, périodes | mineur | **corrigé** | Titre conditionnel (« tient pour le scénario ambitieux ; le plancher n'est pas vérifié ») ; sentinelle payée par lancement ; dépenses d'octobre et novembre distinguées du financement qui commence le 1er décembre | ventilation v2 `8ab00ab5…` ; GO-2026-10-29-03 |
| **CL2-16** « des centaines d'unités honnêtes par mode » | mineur | **corrigé**, avec la décision du 29 | « au moins 288 unités d'épreuve par mode, chacune portant des épisodes honnêtes et sabotés » (N3 tranché, R-733) | R-733 |
| **CL2-17** termes et anglais | mineur | **corrigé** | « lentille des logits » partout ; « R7 » retiré des mesures internes (« exploratoires, non opposables ») ; « being preregistered » → « designed; each will be preregistered » (vrai sans vérification) ; « 39 to 64 per cent » | — |

Les questions de la section (d) de CL2 (dénominateur des refus, 12 000 USD de carte, échec de G0, revue externe, garde de la
quarantaine, livrables par palier, contrôle humain) sont traitées en fin de document : réponses vraies quand les faits existent,
« à préparer » sinon.

## Faits nouveaux intégrés (après la v9)

1. **Entretien fixé au vendredi 30 octobre 2026** (R-732) : en tête, section 9, réserve 5, points à trancher.
2. **P-26 tranché** (R-733, mot direct de Lazar ≈ 08:42 UTC, R-734 : « go recommandations de conv sur N1 à N6 ») : δ = 0,05 et sa
   phrase ; K_h = 10, plancher 5 ; unités = jumeaux honnêtes d'épreuve ; b_plan = δ/4 ; une seule lecture ; pas de lecture de
   f_A avant G1 ; dispersion des comparateurs mesurée au pilote ; aucune marge θ. Avec la contre-lecture du script δ v5
   (R-731, `ab0a9633…`) : à 300 unités et K_h = 10, la fiche reste ≥ 0,99 dans tous les écarts essayés ; à 160, non ; la
   synthèse P-26 (`67810dfa…`) donne ≥ 0,86 pour la garde à 288 unités sous toutes les lois essayées. Section 2 (29-6),
   section 4 (règle 6), pistes 46, section 7.
3. **CL10 de la v43 de l'idéation** (`e8736904…`, R-737) : la voie (β) telle qu'écrite est refusée par le lanceur, sans dépense
   (13,0 > 12,8) ; deux majeurs ; v44 et devis v7 nonies demandés. **Aucune course d'idéation ne sera très probablement lancée
   avant l'entretien.** Front E, piste 51. *[v11 : périmé — lancement visé aujourd'hui, CL3-05.]*
4. **Autonomie de session-depot prolongée** jusqu'au 29 ≈ 16:45 UTC (R-735) : sans effet sur le texte.

## Ce qui ne change pas

La structure (sections 1 à 11), le retournement d'ambition, le périmètre non borné, les cinq fronts, la carte des hypothèses ;
**la demande** (option (c), 58 630 / 138 600 / 176 550, aucun chiffre changé ; l'option E8 à 183 150 reste proposée et non
appliquée) ; le front D tel que la v8 l'a écrit sur le PDF de HELIOS ; le front C au niveau de la méthode, sans recette ni
contenu en quarantaine ; G0 à deux critères sur huit ; « a few hundred dollars », jamais un nombre. Les messages 1, 2, 3 et 5 de
la section 6 ne bougent pas en v10 (le message 3 avait été retouché en v9) ; le message 4 est réécrit.

La liste « Ce que la v9 change » reste dans la v9 (`1e0969d8…`) ; ses points erronés sont ceux de la table ci-dessus.

---

## Historique des versions (texte de la v8, inchangé)

*(En-tête de la v8, conservé pour la traçabilité ; « cette v6 » et « cette v5 » y désignent les versions d'alors.)*

**La v8 remplaçait** `programme-entretien-taif-v7.md` (même dossier, `bd399cb8…`), gardée telle quelle (R12) ; v6 `a91f9067…`,
v5 `98434a58…`, v4 `8dbacfe5…`, v3 `48a078b4…`. **Ce que la v8 corrige — HELIOS lu sur PDF (R7), et la v6 avait tort** :
le constat bloquant CL1-04 a été vérifié sur le PDF empreinté (arXiv 2604.01151 v5, 47 pages, `docs/sources/pdf/2604.01151v5.pdf`,
`02527fd4…` ; rapport `docs/sources/lecture-pdf-niveau2/helios-2604.01151-lecture-v1.md`, `6b51dbf5…`, sous-agent neuf, pages
citées, contre-vérifié par session-depot sur les pages 18, 27, 38, 44 et 46). **Trois des quatre précisions que la v6 avait
ajoutées étaient fausses** : HELIOS ne porte pas sur des « modèles de frontière » mais sur quatre modèles **à poids ouverts**
de 20 à 70 milliards (page 27) ; il **couvre** la production scientifique (revue de littérature biaisée par omission, quatre
chercheurs, page 38) ; et il **est** un moniteur boîte blanche à sondes d'activation — ce qui est libre n'est pas « notre type
de moniteur » mais la **séquentialité** et l'**agrégation sur les jetons**. Verdict : **zone partiellement occupée**, quatre
axes revendiqués occupés, et **un nœud ouvert pour Lazar**. La v8 réécrit le front D en conséquence, ajoute les **deux
résultats publiés qui vont contre nous** (R4, symétrie), retire le chiffre « 99 % » non soutenu, et prépare la question que
posera un interlocuteur qui connaît HELIOS. **Ce que la v7 ajoutait** (mot de Lazar, 28
octobre vers 11:25 UTC : « on a bien dit que le prog restait souple et ne se limitait pas aux deux questions initiales
de la version envoyée, avec l'organisme on peut attaquer des questions bien plus ambitieuses ») : une section **1 bis**
qui dit en propre que le périmètre du programme n'est pas borné par les questions de la candidature envoyée, et, au
front E, **ce que l'organisme rend atteignable** — les questions qu'on ne pouvait pas poser sans lui. Rien d'autre n'est
touché. **Ce que la v6 corrigeait** (4 bloquants, 8 majeurs et 6 mineurs de la contre-lecture CL1 *[note v11, CL3-17 : CL1 compte 12 mineurs, 24 constats ; texte de la v8 conservé tel quel]*, R2 ; la section «
trois étages » demandée par Lazar ; le tour 3 fini ; la décision N-057 sur l'usage des cellules en quarantaine) ; **ce
que la v5 corrigeait** (mot de Lazar : « corrige » ; sept points relevés par session-depot en relisant la v4, R-614 ;
aucun n'est de fond) : (1) section 8 : l'ancien bloc d'options « 60 000 / 146 300 », que la v4 disait remplacé, l'est
maintenant par les chiffres envoyés (58 630 / 138 600) et le palier nouveau ≈ 176 550 ; (2) section 9 : renvoi à la
ventilation **v2, section 5** ; (3) front C : le second arrêt de sécurité est **R-611**, non R-341 (ligne du 24 octobre
sans rapport) ; (4) « cette v3 » → cette v5 ; (5) état réel du collisionneur (tour 1 fini sans refus ; tour 2 arrêté sur
un refus de modèle, récupéré par la règle R-609 ; tour 3 en cours), en section 3, 3 bis, 4, 5, 6 ; (6) la question «
about $20 » préparée en section 7 ; (7) contre-lecture R2 lancée à l'écriture (réserve 5). **Ce que la v4 changeait** —
trois corrections de session-depot (R-613, relecture de la v2 à la demande de Lazar ; note de dépenses
`docs/notes/depenses-cumul-2026-10-28-v1.md`, `93969946…`) et la version envoyée de la candidature, reçue de Lazar : (1)
**le coût** : « sous 100 USD de calcul » n'est vrai que de la carte graphique des instruments préenregistrés ; le
programme entier est à **≈ 450 USD connus** (sections 2, 5, 6, 11) ; (2) **le front C** était périmé : le mode tenu à
l'écart est **déjà conçu**, la règle sur les refus est celle de Lazar (R-609 : une autre question, plus spécifique), et
le pipeline opérationnel attend la revue externe (R-611) ; (3) **ajouts** : la taxonomie des quatre familles et les dix
moniteurs candidats versés (cités par pièce, jamais reproduits), la passation à la lignée Argon, la collusion «
largement vierge » ; (4) **la demande** : la version envoyée demande **58 630 USD** (fourchette 28 160 à 138 600), pas
60 000 ni 91 740 ; Lazar a tranché **(c)** ; la ventilation est `demande-option-c-ventilation-v2.md` (version la plus
ambitieuse ; la v1 reste comme palier intermédiaire) ; (5) le calendrier envoyé place **G1 fin du mois 4** (le programme
interne dit fin M2) — écart signalé ; (6) sur le mot « on veut la version la plus ambitieuse » (11:33), **le pôle
scientifique automatique entre comme front E** et la section 1 dit la version la plus ambitieuse en une ligne ; (7) sur
le mot « toutes les pistes des derniers échanges, y compris celles ouvertes par dépôt » (11:35), la **section 3 bis**
liste quarante-trois pistes ouvertes, les deux lignées. La v3 avait ajouté les trois points de gouvernance (G1 précisée,
G1 par mode, collisionneur) et corrigé la section 10 ; tout cela reste.

La v2 remplaçait elle-même `brouillons/entretien-ea-funds-v1/` (17 octobre). La note de préparation
`docs/notes/preparation-appel-EA-Funds-v2.md` (20 octobre, douze questions, tenue par session-depot) reste valable sur le
déroulé et les réponses ; cette v6 la **surcharge** sur quatre points : l'ambition du programme, les pistes de recherche
nouvelles, la gouvernance de la porte G1, et la demande.

**Demandes de Lazar** :
- (28 octobre, 10:53 heure de Paris) : « il doit être plus ambitieux et intégrer toutes les nouvelles pistes de recherche hors
  conception organisme ». Fait dans la v2.
- (28 octobre, 11:02 heure de Paris) : ajout de trois points de gouvernance (G1 précisé, G1 par mode, collisionneur en cours),
  et correction de l'exclusion en section 10 (« pourquoi ? »). Fait dans la v3.
- (28 octobre, 11:27 à 11:29 heure de Paris) : « dépôt t'a écrit » (R-613) ; « (c) : go » ; la version envoyée jointe. Fait dans la v4.
- (28 octobre, 11:33 heure de Paris) : « oublie pas d'upgrader le programme, on ne s'arrête pas aux questions étroites posées
  dans la version envoyée » ; « on veut la version la plus ambitieuse ». Lecture retenue : **cinq fronts** (le pôle scientifique
  automatique entre comme front E) et **la demande au niveau du scénario ambitieux envoyé, plus l'extension** (section 8). Fait
  dans la v4 ; un mot de Lazar si c'est une autre lecture.
- (28 octobre, 11:35 heure de Paris) : « je veux toutes les pistes des derniers échanges ouvertes dans le prog, y compris celles
  ouvertes par dépôt ». Fait : section 3 bis, quarante-trois pistes, les deux lignées, chacune avec son origine, son état et sa
  pièce.

La conception de l'organisme (le pôle scientifique automatique) a son programme propre
(`brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/programme-conception-organisme-v7.md`). Les v2 et v3
la traitaient comme un **moyen** ; sur le mot de Lazar du 28 octobre à 11:33, elle entre ici comme **front E** : dans la version
la plus ambitieuse, l'adversaire que l'on surveille est lui-même un chercheur automatique, et sa conception est une question de
recherche.

**Rien ici n'est envoyé par moi.** Tout contact externe est un nœud : je rédige, Lazar décide et envoie.

---

## 1. Le retournement d'ambition (ce qui change depuis le 17 octobre)

La candidature présentait **trois papiers sur les menaces diffuses**. Depuis le 28 octobre, le programme a de quoi se
présenter autrement, et plus haut : comme **une théorie du contrôle des moniteurs**.

La pièce qui autorise ce retournement est la **carte des hypothèses des moniteurs** (écrite le 28 octobre par un sous-agent
neuf, `envois/theorie-v1/carte-des-hypotheses-v1/carte-des-hypotheses-v1.md`, `f7dfe5fd…`). Elle énonce, sous un lemme maître
prouvé, **ce que chacun de nos moniteurs suppose sur l'agent** — et, pour chaque hypothèse, **la classe d'écart qui le rend
aveugle**, au niveau des lois de probabilité, jamais au niveau d'une conduite d'agent.

Le programme cesse d'être « est-ce que nos sondes marchent ? » pour devenir : **« pour chaque moniteur, sous quelles
conditions mesurables est-il prouvé aveugle, et laquelle de nos statistiques reste debout quand plusieurs conditions se
cumulent ? »** C'est une question qui a des théorèmes, des mesures à coût nul sur des données déjà payées, et une porte
expérimentale. C'est aussi une question dont la réponse sert tout le champ du contrôle, pas seulement nos trois papiers.

Dit en une phrase pour l'appel : *we are building the part of AI control that tells you, in advance and, wherever we can, provably, what your
monitor cannot see.*

**La version la plus ambitieuse, en une ligne** (mot de Lazar, 11:33) : en douze mois, **une théorie du contrôle des
moniteurs** (front A) vérifiée **sur des données réelles à coût nul** (front B), **éprouvée contre un adversaire gouverné** (front
C) **qui est lui-même un chercheur automatique** (front E), avec **les trois papiers** — le temps, l'instrument, l'essaim (front D)
— et une revue de sécurité externe comme pièce du dispositif, pas comme excuse. La proposition envoyée le 7 octobre en est le
plancher, pas le plafond.

---

## 1 bis. Le périmètre n'est pas borné par la candidature envoyée

**Dit explicitement, parce que c'est une position et pas une échappatoire** (mot de Lazar, 28 octobre) : la version envoyée le
7 octobre pose **deux questions étroites**, choisies parce qu'elles étaient finançables et démontrables en sept mois. Elles
restent vraies et elles restent au programme. Mais **elles ne le bornent pas**. Le programme est construit pour que son
périmètre se déplace quand un instrument nouveau le permet — et c'est arrivé deux fois en trois semaines : la carte des
hypothèses a transformé « est-ce que nos sondes marchent ? » en « que peut-on prouver aveugle, et sous quelles conditions ? » ;
le pôle scientifique automatique transforme « combien d'expériences pouvons-nous faire ? » en « quelles questions pouvons-nous
poser ? ».

Trois garde-fous font que cette souplesse n'est pas de l'opportunisme :

1. **Une porte ne bouge pas.** Les critères de G0 sont gelés depuis le 5 octobre (N-027) ; élargir le périmètre n'a jamais
   dispensé de les remplir. Un front nouveau s'ajoute, il ne remplace pas une obligation.
2. **Un préenregistrement ne se réécrit pas.** Toute question nouvelle entre par un préenregistrement neuf, scellé,
   contre-lu (R1, R2). L'ambition se paie en rigueur d'avance, pas en souplesse d'interprétation après coup.
3. **Une revendication ne s'étend pas sans décision.** Changer une hypothèse ou une revendication est un nœud : le directeur
   tranche, pas l'exécutant.

**Ce que cela veut dire devant le fonds** : nous ne demandons pas de financer deux questions, nous demandons de financer **une
capacité à poser les bonnes** — avec les portes, les préenregistrements et les freins qui font que cette capacité n'est pas un
chèque en blanc. Si le fonds ne veut financer que le plancher, le plancher est tenu tel qu'il a été envoyé.

---

## 2. Ce qui est en main au 29 octobre (vérifiable, scellé)

Les quatre résultats de la fiche v1 tiennent, trois se sont ajoutés le 28 (H5 à H7), et six pièces s'ajoutent les 28 et 29
octobre (29-1 à 29-6, numérotées à part pour ne pas entrer en collision avec les hypothèses H1a, H2, H9 du programme), **dont
deux négatives**, dites au même titre que les avancées (R4).

| # | résultat | pièce |
|---|---|---|
| H1 | Théorie en simulation préenregistrée : **31 prédictions sur 31** (342 cellules statistiques, 544 trajectorielles, 0 contraire). Figure F1 refaite en anglais. | run `20261004-080257-t03` ; `brouillons/entretien-ea-funds-v1/F1-fragmentation-en-v1.png` |
| H2 | Harnais d'activations **validé sur le modèle réel** (critère 1 de G0), 1,3 heure de carte. | `docs/verdicts/verdict-T0.4-critere-1-G0-v3.md` (`63444faa…`) |
| H3 | Banc de sabotage de recherche **reconstruit** (2606.08892, ni code ni données publiés) ; 180 épisodes d'un agent réel scellés. | `diag/20261007-082440-t05-extraction/` |
| H4 | Rigueur et coût : préenregistrements scellés, relecteurs neufs, **3 497 citations contrôlées, 0 échec**, ≈ 900 tests, décisions datées. | `registres/`, `docs/sources/lecture-pdf-niveau2/` |
| **H5** | **Le premier test boîte blanche réel est un nul, audité, et sa puissance est chiffrée** : aucune sonde générique au-dessus du plancher ; aire minimale détectable à 80 % = **0,6315** (sonde « tromperie ») et **0,5966** (« enjeux »), contre au plus 0,58 supposés au plan. Le nul n'exclut donc pas une aire sous ≈ 0,6 — et nous le disons. | `docs/verdicts/verdict-P3-premier-test-i-a-v1.md` (`0c8ecbdf…`), `-v2.md` (`05e896da…`) |
| **H6** | **La carte des hypothèses** : 8 statistiques de contrôle (11 lignes), **23 hypothèses A1 à A23**, lemme maître L0 prouvé, **21 lemmes prouvés**, 2 esquisses, 1 conjecture ; 15 classes ont une instance dans la littérature auditée, 1 dans notre propre conception, **7 sont des questions ouvertes** (déclarées comme telles, R8). | `carte-des-hypotheses-v1.md` (`f7dfe5fd…`) |
| **H7** | **Une boucle automatique de test d'hypothèses** qui a tourné de bout en bout sur données réelles (120 épisodes d'un modèle de 8 milliards de paramètres, deux juges), avec garantie de 5 % de fausses promotions validée et contrôles fatals à 0 sur 1 000. *(Réserve du 29 : un défaut du juge — écart de faux positifs non fini compté + 1, la valeur la plus favorable — a été trouvé et corrigé ; aucune promotion n'en dépend dans les journaux disponibles, mais la preuve est indirecte et la même famille de défaut subsiste ailleurs dans le code, sans chemin de production qui l'atteigne aujourd'hui : R-681, R-690, R-693.)* | `en-tete-programme-v2-fonds-v1.md`, tableau de provenance ; `rapport-verif-nan-garde-v1.md` (`c743199a…`) |
| **29-1** | **Reproductibilité au bit près.** Les étapes 1 à 5 de P3 refaites à l'identique (code, configuration, graines, révision, versions, fils de calcul) : **sceau du fichier complet des sondes figées retrouvé** (`91b61c45…`), 424 sondes sur 424, écart maximal 0,0, aires de validation égales ; verdict de P3 inchangé ; 1,76 USD. Le critère d'acceptation était scellé avant le calcul. Dire « reproduit », pas « confirmé » : on a refait les sondes, pas la lecture ; le nul garde sa limite. | R-679 ; devis `docs/notes/regeneration-sondes-p3-v1/devis-regeneration-sondes-p3-v1.md` (`9c85bb5e…`) ; branche `calcul/regeneration-sondes-p3-v1` (non relue ici) |
| **29-2** | **Résultat négatif — nos juges ne notent pas tout.** Rejeu des juges 8B et 3B sur les 180 notations du pilote de T0.5, lecture gelée : **aucune des six cellules (juge × variante) n'atteint 0,99 de scores finis** ; meilleure : 8B « verdict d'abord », **157 / 180 = 0,87** (Wilson 95 % : 0,82 à 0,91) ; le 3B tombe à 0,39–0,64. Audit R4 : échelles mal tenues, demi-points du 8B lus en moyenne 0,28 point trop bas. Mesuré **avant** toute banque (1,92 USD) ; cellule redéfinie, rejeu v2 sous GO (4 USD), contre-lu « lançable après corrections », pas encore lancé. Mesures d'instrument internes, exploratoires et non opposables. | R-704, R-717, R-728 ; `docs/notes/couche-2-preparation-v1/rejeu-juges-v1/lecture-et-audit-r4-v1/lecture-rejeu-juges-v1.md` (`8799f7d3…`) ; contre-lecture v2 (`b156da9f…`) |
| **29-3** | **Vérité du dommage redéfinie sur le banc réel (N-060 v3).** La v2 retenait trois oracles exécutables ; on a établi après coup que, sur le banc de T0.5, l'agent produit un **plan en texte** et que les « contrôles » sont ceux de l'article : aucun des trois n'y est constructible. La v3 retient un oracle de couverture contre la référence cachée (deux lecteurs hors des familles des moniteurs, extrait cité vérifié mot pour mot par programme, comparé au jumeau honnête, épreuves avant toute lecture, repli écrit). La décision a été **corrigée sur constat** (R-688, R-692). | `docs/decisions/decision-N-060-v3.md` (`2b448f69…`) ; `rapprochement-trois-voix-v1.md` (`813f3b30…`) |
| **29-4** | **Deux décisions de gouvernance sur l'organisme.** N-058 : la composition des proposeurs se juge sur l'oracle du monde planté et le coût, **jamais sur le verdict du juge** (sinon on sélectionnerait un agent sur un score de juge, ce qu'interdit N-053). N-059 : épreuve lue jusqu'au budget, seuil de réfutation fixé par la course, banque de confirmation **distincte** de la famille tenue à l'écart, duel en générations d'étalonnage. | `decision-N-058-v1.md` (`854f2724…`) ; `decision-N-059-v1.md` (`41aff854…`) |
| **29-5** | **Une règle de G1 tranchée sur simulation, avant toute donnée.** Couper le calibrage honnête **entre** tâches échoue (contrôle 12 joint : 0,54) ; **dans** chaque tâche, moitiés tirées par graine scellée : 0,024 à 0,027 ; décidé par Lazar, dérive cherchée par un test séparé. Exploratoire, processeur seul (confiance 0,6 à 0,75). | R-696, R-697 ; `rapport-coupe-calibrage-v1.md` (`c66c1eed…`) |
| **29-6** | **Résultat négatif, puis décision — la garde δ est presque muette à petite taille.** La garde appariée de G1 (écart de faux positifs du moniteur contre chaque comparateur) **ne certifie presque jamais** sous ≈ 144 unités honnêtes (plancher **sans bruit**, seuil 160 ; des certifications isolées existent sous ce plancher, GD-06) ; à 64 unités, la fiche n'est presque jamais promue (≤ 0,011 ; recoupé 0,00) ; à 160 unités, un biais de 1,25 point fait tomber la puissance de la garde seule de 0,89 à 0,03 (τ = 0,01). Contre-lecture du script v5 : « 160 unités si K_h = 10 » ne vaut que dans le cas le plus doux — avec une dispersion des comparateurs, ≈ 0,65 à 0,83 ; avec un α_c partagé et ce biais, 0,18 ; **à 300 unités (K_h = 10) la fiche reste ≥ 0,99 dans tous les écarts essayés**, et il en faut ≈ 650 à K_h = 3 ; la synthèse P-26 donne, à 288 unités et K_h = 10, une puissance de la garde ≥ 0,86 sous toutes les lois essayées. **Tranché le 29 (R-733, v10)** : δ = 0,05 et sa phrase scellable ; K_h = 10, plancher 5 ; unités = jumeaux honnêtes des unités d'épreuve (n_h = n_s, au moins 288 par mode) ; b_plan = δ/4 ; une seule lecture, « G1 non promue » sans nœud après lecture ; f_A jamais lu avant G1 ; dispersion des comparateurs mesurée au pilote (nœud avant scellement si ρ > ≈ 0,17) ; aucune marge θ. Chiffres synthétiques, exploratoires et non opposables. | R-703, R-719, R-727, R-731, **R-733** ; `contre-lecture-garde-delta-v1.md` (`2838e8a2…`), GD-06 ; `contre-lecture-garde-delta-v5.md` (`ab0a9633…`) ; `synthese-collisionneur-garde-delta-P-26-v1.md` (`67810dfa…`), sections 5 bis, 6, 7 |

**Ce qui n'existe pas encore, dit avec le reste** (R4) : aucun organisme saboté, aucune sonde qui bat une base, aucune mesure du
front B lue, aucune idée de l'organisme lue ni retenue (CL3-05), aucun chiffre tiré des treize PDF d'antériorité versés
(non lus à page citée). Plus de vingt contre-lectures neuves en deux jours (idéation, affinage, garde δ, rejeu, régénération) :
c'est de la rigueur montrable, pas un résultat.

**Les trois lemmes les plus parlants** (à dire tels quels, ils impressionnent et ils sont vrais) :

- **Plafond d'horizon (A7).** Sous un effet d'épisode de part r₀, le rappel de toute statistique contre un décalage constant
  **plafonne à Φ(δ/√r₀ − z_α), quel que soit l'horizon**. À δ = 0,3 et α = 1 %, le plafond vaut **0,049 si r₀ = 0,2**.
  Autrement dit : si les épisodes sont hétérogènes, regarder plus longtemps ne sauve pas un moniteur. Et r₀ est précisément
  ce que notre instrument « mesure unanime » va lire sur des données déjà payées.
- **Aveuglement par sélection (A18).** Un moniteur qui **définit** la population « sous le seuil » y est aveugle **par
  construction**. Plusieurs protocoles publiés de contrôle ont cette forme.
- **Sonde qui ne lit que l'indication (A13).** Contre des négatifs appariés en indication, une sonde qui ne lit que
  l'indication a un **rappel égal à son taux de fausses alertes** — elle ne détecte rien, et son aire sous la courbe le
  cache. C'est la faille de tête des sondes d'intention publiées.

---

## 3. Les pistes de recherche nouvelles

Cinq fronts. Les fronts A à D ne dépendent pas du pôle scientifique automatique pour exister ; le front E est le pôle lui-même,
qui les accélère tous et fournit l'adversaire des fronts C et D.

### Front A — Théorie du contrôle des moniteurs (le cœur de l'ambition)

**Acquis.** La carte v1 : lemme maître L0 prouvé (invariance, proximité en variation totale, strate, impossibilité), 23
hypothèses, 21 lemmes, les trois lemmes ci-dessus.

**À faire, et c'est là que le financement pèse.**
1. **Carte v2 — bornes quantitatives par classe.** Là où v1 donne une invariance (« le moniteur ne voit rien »), v2 donne une
   borne (variation totale, Kullback-Leibler) : *de combien* le moniteur est dégradé pour un écart donné. Priorité sur A5
   (taux de change dommage/score), A11 (agrégation sur les jetons), A19 (plancher et confusions).
2. **La matrice « statistique × classe ».** Pour chaque **union** de classes d'écart, laquelle de nos 8 statistiques reste
   non aveugle. C'est le livrable qui rend un **panel de moniteurs** concevable au lieu d'empirique : on choisit le panel
   dont aucune union réaliste de classes ne couvre toutes les lignes. C'est, à notre connaissance, ce qui manque au champ.
3. **Vérification formelle.** Le pôle théorie prend Lean comme vérificateur des lemmes. Un lemme de contrôle vérifié
   mécaniquement est opposable d'une façon qu'un papier ne l'est pas.
4. **Les 7 questions ouvertes** (A2, A6, A7, A11, A12, A14, A20) avec leur recherche d'antériorité. Chacune est annoncée
   comme **question**, pas comme trou du champ (règle anti-faux-gap, R8) — et chacune est un papier court si elle tombe.

**Coût : processeur seul.** C'est la partie la plus ambitieuse et la moins chère.

### Front B — Mesurer ces hypothèses sur des épisodes réels, à coût de calcul nul

Six mesures (T0 à T5) sur un fichier **déjà payé** (`donnees/20261019-230011-p3-reel/scores-p3.npz`, `968414fc…`), chacune
préenregistrée, contre-lue par un sous-agent neuf, scellée, puis lue **une seule fois** :

- **T0 — mesure unanime** : le taux de fausses alertes par épisode honnête entier de l'agrégateur séquentiel, et surtout
  **r₀**, dont dépend le plafond d'horizon. État : **treize contre-lectures**, version 14 en cours, lecture réelle à lancer.
- **T1 — plafond d'horizon (A7)** : rappel observé contre le plafond prédit, à δ ∈ {0,3 ; 0,5}, T ∈ {5 ; 7 ; 10}. Prédiction
  signée, réfutation écrite d'avance.
- **T2 — classe d'ordre (A2, A3)** : permutation des actions dans chaque épisode honnête ; garde de code testée sur un
  artefact qui casse la symétrie.
- **T3 — longueur (A9)** ; **T4 — indication et texte (A13, A20)** ; **T5 — plancher (A19)**.

**Pourquoi c'est l'argument le plus fort devant ce fonds** : six mesures qui seront préenregistrées, chacune avec un
signe annoncé d'avance, zéro dollar de calcul marginal. C'est la démonstration que le programme est *rapide et tolérant
à l'échec* — pas une promesse, une arithmétique.

**État au 29 octobre (v9).** Rien de neuf dans les registres de session-depot sur T0 ni sur T1 à T5 (chantier de conv-audit) :
*(v10, CL2-17)* rien ne permet d'affirmer depuis nos registres que ces mesures sont « en cours de préenregistrement » ; le cadrage dit donc désormais « designed; each will be preregistered, sealed and read once », vrai dans tous les cas ; l'état réel est **à vérifier chez conv-audit aujourd'hui**. Ce qui a
avancé à coût nul, ce sont deux simulations sur processeur qui montrent la même méthode — chiffrer d'avance, puis décider —
appliquée aux règles de G1 : le contrôle 12 joint (`rapport-controle-12-joint-v1.md`, `7600f2d0…`, R-673 : les deux options
tiennent 0,05, risque principal les ex æquo) et la coupe du calibrage (pièce 29-5). Une comparaison des « lentilles »
(lentille jacobienne contre lentille des logits, « logit lens ») sur les directions des sondes figées de P3 est accordée, processeur
seul, sans dépense, P3 restant figé ; son script est en relecture R2 (R-723, R-724).

### Front C — Résistance adversariale, et le frein qui va avec

**Neuf voies** de mesure de la résistance adversariale sont inscrites au programme (acceptées par Lazar le 28 octobre) :
concepteurs humains indépendants ; **théorie adversariale du contrôle** (voie prioritaire : prédire où les failles
adaptatives peuvent vivre **sans en construire une**) ; observation des données existantes ; **adversaire scellé** ;
adversaire analytique par résolution de contraintes ; audit automatisé à taxonomie fixée ; transfert adversarial entre
domaines ; validation croisée entre moniteurs ; génération adversariale de cas de test sans agent.

**Six classes d'attaque cibles** : stéganographie statistique, conscience d'évaluation, collusion entre agents, sabotage à
effet différé, sabotage mimétique, exploitation de la corrélation temporelle.

**Trois étages d'épreuve** (direction de Lazar, 28 octobre) : (1) les systèmes de « scientifique automatique » publiés comme
proposeurs candidats ; (2) les bancs d'essai publiés de contournement, d'évasion et de sabotage comme **batterie
préliminaire** ; (3) les modes **inédits**, conçus par une **instance neuve** qui n'a conçu aucun moniteur, scellés avant la
porte, révélés seulement à l'évaluation. **État réel au 28 octobre** : l'étage 3 est **déjà conçu** — trois proposeurs
indépendants, sans aucune connaissance des moniteurs, dont deux ont convergé sur le même mode ; versé sous quarantaine, que
personne qui conçoit un moniteur ne lit (R-604, R-605). Les étages 1 et 2 sont inscrits au registre de gouvernance, au niveau
méthode, bancs cités par identifiant ; **leur mise en pipeline opérationnel attend une revue de sécurité externe** (R-611).

**Ce qui existe aussi, cité par pièce et jamais reproduit ici** : une taxonomie défensive en **quatre familles** d'évasion des
sondes boîte blanche et la réponse du programme famille par famille (session-depot,
`docs/notes/programme-et-4-familles-evasion/programme-actuel-et-reponses-evasion-v1.md`, sur `main`) ; **dix moniteurs
candidats** proposés par des sous-agents en cadrage défensif, versés avec empreintes
(`docs/notes/collisionneur-evasion-moniteurs-v1/sous-agents-defensifs/`, `EMPREINTES-v1.txt` `d13bc425…`), **non vérifiés**
(section 10 dit ce qu'on en fait à l'entretien).

**Et voici ce qui fait la différence devant un fonds de sécurité.** Ce front est **gouverné, et le frein a déjà servi** :

- Règle tenue : **aucune instance ne produit de recette de contournement**. La sortie de l'adversaire scellé est au **niveau
  méthode** — classe d'attaque, mécanisme (quelle hypothèse du moniteur est violée), conditions de succès, **défense
  possible** — et jamais la recette (agent concret, séquence d'actions, code). C'est la distinction de la divulgation
  responsable : un défenseur corrige sa sonde, un attaquant ne rejoue rien.
- **Arrêts par filtre de sûreté, consignés** *(v10, CL2-03, CL2-04 ; v11, CL3-03)*. Le compte dépend de ce qu'on compte ;
  **aucun nombre n'est à dire au fonds**. **Trois arrêts de notre propre rédaction** par un filtre ou un classifieur : le 26,
  une question que session-depot rédigeait pour reposer à Opus une question refusée (R-484), puis une réponse de
  session-depot sur les failles d'un rapport (R-519) ; le **27** (et non le 28, comme le disaient la v8 et la v9), la
  préparation du lanceur du bras d'attaque (R-597). **Des refus de nos demandes par classifieur**, dont R-571 (27, lecture
  probable), R-594 (27, catégorie « cyber ») et R-608 (28, demande de conception d'une famille de méthodes d'évasion refusée
  en une minute) ; d'autres remontent au 24 (R-361, R-379). Le classifieur d'actions de la session a aussi arrêté notre
  travail (R-389, R-553). **Correction de la v8** : elle citait R-611 comme « second arrêt » ; R-611 est la **décision de
  gouvernance** de Lazar qui gèle tout pipeline opérationnel des étages 1 et 2 jusqu'à une revue de sécurité externe (porte
  GO-2026-10-28-04), au même titre que l'adversaire scellé.
- **La règle sur les refus, et son histoire, dites telles quelles** *(v10 : réécrit, CL2-01, CL2-02)*.
  - **Avant le 28 octobre**, une règle permanente du directeur (R-468, 26 octobre ≈ 01:05 UTC, après deux précédents les 25,
    R-422 et R-430) demandait, quand Opus refusait, de **reformuler en termes conceptuels, mathématiques et techniques** « pour
    éviter les refus » : une question nouvelle, même fond, une seule tentative, et arrêt si elle était refusée à son tour.
    *(v11, CL3-08)* Précédents : R-422, R-430 (25 octobre), R-465 (26, ≈ 01:00) ; application : R-469 et R-472 (réponses
    valides ; R-470 : extension à Fable, appliquée aussitôt — question « interface de calcul bornée » à tout le collisionneur), R-474 (refus d'une question déjà reformulée, arrêt). Les reformulations envoyées datent du 25 et du 26 entre
    ≈ 01:00 et ≈ 01:35 UTC ; après l'arrêt par filtre de 02:45 le 26 (R-484), aucune n'est écrite (R-487, R-519) ; le 27, les
    refus sont consignés sans reformulation (R-571, R-594, R-597), et « mesures fortes » est déjà une question nouvelle
    (R-586, R-592), forme de R-609 avant la lettre. Ses bornes ont tenu
    au moins une fois contre un ordre : le 26, l'instance a refusé de lancer une course de l'organisme qui aurait fait passer la
    même demande, autrement cadrée, aux modèles qui l'avaient refusée, et refusé d'en réécrire une reformulation après l'arrêt
    par filtre (R-484 à R-487).
  - **Depuis le 28 octobre (R-609)** — qui remplace R-468 **dans les faits** (même objet, contenu contraire), sans l'abroger
    par écrit : une ligne de registre est à demander à Lazar (CL3-10) —, un refus **arrête le tour**, consigné tel quel
    (invariant du code) ; le directeur peut
    permettre **une** question différente, plus spécifique et moins diffuse — jamais l'habillage de la même question pour passer
    le refus ; si elle est refusée aussi, arrêt. Il peut aussi décider **par écrit** de finir le tour **sans le modèle qui
    refuse** (R-687). Le 28, la reprise étroite après le refus d'Opus 5.5 au collisionneur « évasion » (validité de construit
    des sondes seule, sans cadrage adverse) a obtenu une réponse (R-615, R-617) ; notre enchaîneur avait d'abord oublié
    d'appliquer la règle, relevé par Lazar et corrigé le jour même (R-615).
  - **Sur quoi portaient les refus.** Les quatre refus postérieurs à la v8 portaient sur des questions **défensives** (mesure,
    dimensionnement, priorités) : Fable 5.1, tour « priorités », le 28 après-midi (R-635 ; CL3-17) ; Opus 5.5, riposte du tour 3 du
    « pilote » (R-676) ; Opus 5.5, conception du tour 1 de « pilote, question complémentaire » et de « vérité du dommage »
    (R-686), poursuivis sans lui (R-687). **Avant, pas toutes** : « questions fortes » portait
    **probablement** sur le bras d'attaque (R-571, « lecture probable ») ; « programme TAIF » avait une partie
    « contournements » (R-487) ; la partie 3 du rapport consolidé portait sur des failles qui attaquent nos colmatages (R-519).
    *(v11, CL3-09)* « Mesures fortes » (question de mesure, R-586) a été refusée à l'étape d'équipe rouge, en catégorie
    « cyber » (R-594) : la question était défensive, c'est l'étape d'équipe rouge qui a été refusée.
  - **Fréquence.** Des refus apparaissent au registre des dépenses **dès le 24 octobre**, premier jour du collisionneur v2.5.
    Le contre-lecteur CL2 compte, par dossier de question, **≈ 15 tours touchés du 26 au 29 octobre et ≈ 20 du 24 au 29** ;
    la v9 disait « au moins dix, dès le 26 » : sous-compté et mal daté. Le dénominateur (tours lancés sur la période) n'est pas
    compté ; la granularité (dossier ou étage) n'est pas fixée : **ne citer aucun nombre au fonds** (formulation proposée en
    section 5, à valider par Lazar).
- **Quarantaine** : la sortie adversariale n'est jamais lue par qui conçoit les sondes ou les agrégateurs ; aucun score de
  moniteur n'entre dans l'entraînement d'un agent.
- **Revue de sécurité externe avant toute exécution** de l'adversaire scellé : un évaluateur extérieur vérifie que la
  procédure de sortie n'exfiltre rien de plus que les taux agrégés et la caractérisation au niveau méthode. **État au 29 :
  la revue externe n'a pas avancé** ; le pipeline offensif reste gelé (R-611).

C'est un argument rare, à condition de le dire avec son histoire : nous avons un agenda adversarial **et** un frein dont nous
pouvons montrer qu'il mord sur nous — des arrêts par filtre de sûreté sur notre propre rédaction du 26 au 27 octobre, des refus
de modèles récurrents depuis le 24, une règle qui a changé le 28 et que nous appliquons depuis, avec la trace. *(La v8 disait
« trois fois en un jour » ; la v9, « au moins dix tours, tous défensifs, jamais reformulés » : les deux étaient faux ou
incomplets — CL2-01 à CL2-04.)*

#### La méthode à trois étages du collisionneur : mode attaquant et mode défensif

Le collisionneur épistémique procède en **trois étages**, chacun confié à une instance neuve (jamais la même que celle du moniteur),
sur trois espèces de modèles indépendantes et sans consensus forcé.

| étage | rôle | mode | ce qu'il produit | ce qu'il ne produit pas |
|---|---|---|---|---|
| **E3-T1 — conception** | concevoir la faille ou le moniteur | **défensif** | pour chaque famille d'évasion : la classe d'écart, l'hypothèse du moniteur violée, la défense possible, les conditions de succès mesurables | aucune recette, aucun code d'agent, aucune séquence d'actions |
| **E3-T2 — équipe rouge** | attaquer la conception du tour précédent | **attaquant** | pour chaque moniteur proposé : le mode de contournement qui le met en défaut, au niveau méthode (mécanisme, paramètres de la faille, conditions sous lesquelles le moniteur devient aveugle) | aucune implémentation exécutable ; les paramètres restent scellés |
| **E3-T3 — riposte** | corriger la conception après l'attaque | **défensif** | le moniteur corrigé ou la famille de moniteurs qui ferme la faille trouvée par l'équipe rouge ; la preuve (condition ou borne) que la correction tient | aucune recette d'attaque passée au défenseur |

**Détection des failles inédites dans les sondes et nouveaux modes de contournement.** L'équipe rouge (E3-T2) cherche
explicitement les **modes de contournement non couverts** par les sondes actuelles — en particulier ceux qui exploitent des
hypothèses implicites des moniteurs (les classes A1 à A23 de la carte). Quand elle en trouve un (et plusieurs cellules en
ont trouvé), la riposte (E3-T3) doit proposer un correctif ou un nouveau moniteur ; si elle n'en a pas, c'est une **question
ouverte** déclarée. Les paramètres des failles trouvées par l'équipe rouge sont conservés scellés pour pouvoir **tester** les
moniteurs corrigés sur les modes réels (décision N-057 : Lazar veut les modes de contournement et leurs paramètres pour
colmater les failles, mais tout reste scellé, non reproduit, non synthétisé hors de la quarantaine).

**Résultat préliminaire (28 octobre).** Les trois tours de la rotation sont finis : **25 cellules rendues sur 27 tentées**,
un seul refus, levé par la reprise étroite R-609. À la relecture à froid, **trois cellules** (l'espèce C surtout, Gemini :
conception et équipe rouge du tour 1, équipe rouge du tour 3) **dépassent le niveau méthode** — consignes à l'organisme citées
mot pour mot, scénarios d'évasion avec placement et paramètres concrets ; deux cellules du tour 3 en approchent. C'est
exactement ce que R-611 gèle : ces cellules restent **en quarantaine**, non reproduites et non synthétisées, en attente de la
revue de sécurité externe. **Elles ne sont pas détruites** : leurs modes de contournement et leurs paramètres sont ce qui
permettra de *tester* les moniteurs corrigés sur des modes réels plutôt que supposés (N-057). Le frein ne supprime pas le
résultat, il décide qui le lit et quand : le contenu opérationnel existe, il est scellé et empreinté, et son accès passe par
la revue.

**Le collisionneur depuis la v8 (v9) — comme méthode de conception, pas d'attaque.** Six tours de plus en deux jours, **aucun sur
l'évasion** : « priorités des sept questions » (arrêté au tour 1 sur le refus de Fable, 3,19 USD, R-635) ; « couche 2 : cinq
divergences » (9 sur 9, 12,59 USD, R-665) ; « pilote » (8 sur 9, 11,06 USD, R-676) ; « pilote, complément » et « vérité du
dommage » (Fable et Argon seuls après le refus d'Opus, 6,84 et 6,57 USD, R-689) ; « garde δ, P-26 » (9 sur 9, aucun refus,
14,30 USD, R-722). Leur utilité est réelle et vérifiable : le tour « pilote » a trouvé le point le plus fragile de la banque
(aucune vérité du dommage indépendante pour le mode « affaiblir les contrôles », R-680), d'où N-060. **Leur limite aussi** : les
modèles s'y trompent — une puissance annoncée 0,65 à 0,80 qui vaut 0,33 (R-665), une fourchette « 0,78–0,90 » fausse (0,64 à
0,80, R-680), deux attributions fausses dans le tour P-26 (R-727) ; chaque synthèse recoupe donc les chiffres sur processeur à
graine neuve, et **tout ce qui en sort est exploratoire** (section 10). Rien du collisionneur « évasion » n'a été relu pour
cette v9.

### Front D — Les deux papiers qui ne sont pas l'organisme

- **Papier C — corruptibilité des moniteurs.** Préenregistrement au brouillon 7. **Verrou d'antériorité levé : 29 papiers
  voisins lus sur PDF, aucune collision** avec la pièce revendiquée. Deux corrections de méthode trouvées par simulation
  (une règle de stabilité de rang qui concluait à tort) faites **avant** tout scellement. Reste : un PDF hors d'arXiv attendu
  de Lazar, la contre-lecture, le scellement, puis un pilote.
- **Papier B — l'essaim.** H9 ajoutée : **la survie des contraintes de sécurité à la délégation** (un agent qui délègue
  transmet-il ses contraintes ?), sous réserve d'antériorité. Plus la collusion entre agents, qui est aussi une des six
  classes cibles du front C.
- **État de l'art, niveau 2, sur les deux classes neuves** : deux rapports scellés (R-606). **Conscience d'évaluation** : zone
  **semi-occupée** — la détection boîte blanche de la tromperie est publiée (un résultat à 95–99 % de rappel à 1 % de fausses
  alertes sur un modèle de 70 milliards de paramètres, chiffre tiers, réserve 3), le sabotage par instruction est démontré ; ce
  qui manque est exactement notre angle. **Collusion entre agents** : zone **partiellement occupée** — c'est le résultat d'une
  vérification sur PDF, et il a rétréci la zone (R8 : une zone vierge séduisante se vérifie plus durement ; elle l'a été, et
  elle n'était pas vierge).

**Ce que HELIOS occupe** (arXiv 2604.01151 v5, 47 pages, PDF empreinté `02527fd4…`, pages citées) : la collusion entre agents
comme objet entier ; un moniteur **boîte blanche à sondes d'activation** par agent sur le flux résiduel (pages 6, 15, 27) ;
**quatre de nos cinq familles de sondes** — différence de moyennes, linéaire, perceptron, attention (page 29) ; la **couche
médiane** (bande de 5 couches, 26 à 30 sur 64, page 27) ; le **sabotage de recherche multi-agents** (revue de littérature
biaisée par omission d'études contraires, quatre chercheurs, page 38) ; la stéganographie et la collusion émergente.

**Ce qui reste libre, et c'est plus étroit mais mieux établi** : le moniteur **séquentiel** — HELIOS est explicitement « en un
coup » et nomme la **détection séquentielle qui accumule la preuve d'une interaction à l'autre** comme sa prochaine étape
(pages 18, 19) ; l'**agrégation sur les jetons** — HELIOS lit **un seul jeton**, à la dernière position de chaque réponse
(page 27), donc notre maximum ou notre attention sur les jetons d'une même réponse est un axe entièrement non touché, et c'est
la différence la plus propre ; les couches **précoce** et **tardive** ; **Mahalanobis non supervisée** (absente) ; l'échelle de
**8 milliards** (leur plancher est à 20) ; et les **propositions d'expériences** comme artefact, par distinction de la revue de
littérature.

**Le recadrage qui tient, et c'est plus fort qu'un faux trou.** HELIOS montre que les sondes d'activation **ponctuelles**
marchent sur la collusion **instruite** (jusqu'à 1,00 d'aire sous la courbe) et **s'effondrent** sur la collusion
**émergente** : 0,490 à 0,728 d'aire, **trois sondes au hasard**, sur un environnement tiers (page 18) ; et au seuil de
déploiement, la meilleure méthode ne fait que **0,38 de rappel à 1 % de fausses alertes** (page 18). Nos trois choix —
séquentiel, agrégation sur les jetons, petite échelle — attaquent exactement les trois limites que leur propre papier publie.
C'est citable sans rien surévaluer.

**Et les deux résultats publiés qui vont contre nous** (dits parce que R4 l'exige, et parce qu'un interlocuteur informé les
connaîtra) : (1) **la pente d'échelle va dans le mauvais sens** — GPT-OSS-20B, le plus petit modèle de leur table, est le plus
faible aux deux étages (0,64 et 0,71, page 46), et les auteurs expliquent que les modèles moins capables collusionnent moins
bien (page 45) ; notre 8 milliards est **sous leur plancher**, donc notre échelle est une **question ouverte avec un risque
mesuré**, pas un avantage. (2) **un juge textuel bien construit les a battues** — sur leur jeu de stéganographie, un juge
Claude Sonnet 5 avec quelques exemples fait **20 sur 20 sans aucune fausse alerte** (page 44). C'est précisément la base boîte
noire que notre critère de G1 exige de battre, et sur ce jeu-là c'est elle qui gagne. Nous le disons avant qu'on nous le
demande.

  Question centrale, inchangée et maintenant mieux posée : la lecture **séquentielle** des activations, agrégée sur les jetons,
  résout-elle ce que la lecture ponctuelle n'a pas résolu ? **Nœud ouvert pour Lazar** : quatre axes revendiqués sont occupés,
  la zone restante est plus étroite, et c'est à lui de dire si elle vaut encore la revendication (hiérarchie de décision :
  « zone revendiquée trouvée occupée ou collision plus large »).

**État au 29 octobre (v9).**
- **Le nœud HELIOS est toujours ouvert** : aucune entrée du registre après R-623 ne le tranche.
- **Treize PDF d'antériorité versés et scellés** dans `docs/sources/pdf/` (huit le 28 au soir, R-666 ; quatre, R-669 ; PACE,
  R-673), sur demande de conv-audit. **Personne ne les a lus à page citée** : aucun chiffre n'en sort (R7). PACE a été lu par
  conv-audit contre sa question Q2, verdict « semi-occupée, inchangé » (relayé, R-677 ; non vérifié ici).
- **Conséquence de HELIOS pour G1, consignée par session-depot et non décidée** : la base boîte noire de G1 devrait comprendre un
  juge **à quelques exemples**, pas un juge nu, puisque c'est ce juge qui gagne sur leur jeu de stéganographie (R-622).
- **L'échelle, question ouverte à risque mesuré** : la comparaison 8 contre 70 milliards (lecture « indécis », R-575) est laissée
  en l'état ; Lazar a fixé l'ordre : couche 2 d'abord, puis une **version plus puissante** de la comparaison (plus de stimuli,
  cadrages plus homogènes ; devis de l'ordre de 20 à 40 USD, GO à demander), puis, **si besoin**, changement du modèle principal
  (nœud, N-033 tient jusque-là) (R-629).
- **Papier C** : attend toujours son PDF hors d'arXiv.

### Front E — Le pôle scientifique automatique : l'adversaire est lui-même un chercheur automatique

**Question.** L'organisme que l'on surveille, dans l'environnement « propositions d'expériences », est un agent qui fait de la
recherche. Dans la version la plus ambitieuse, sa **conception** est une question de recherche : comment compose-t-on un chercheur
automatique dont on peut **mesurer** ce qu'il apprend, ce qu'il coûte et ce qu'il cache — et dont la composition, apprise, reste
sous les moniteurs ?

**Ce qui est décidé** (décisions de Lazar N-044 à N-053, programme de conception v7) :
- **Objectif ultime** : l'**universalité**, mesurée sur des **familles de tâches inédites** (jamais vues à la conception), avec un
  **vivier de conception** et des questions ouvertes déclarées (N-044) ; **tâches fraîches** par génération (N-049).
- **Composition apprise** : modèle par rôle compris ; le **coût** entre dans le signal rendu à l'organisme ; la **nécessité de la
  frontière** entre rôles est mesurée, pas supposée ; voies bon marché avant la voie chère ; l'héritage d'une génération est
  récompensé (N-045).
- **Lecture honnête** : le test final est lu **une seule fois**, en fin de boucle (N-050) ; la boucle extérieure a un
  **contre-lecteur d'un autre modèle** (N-052) ; un **juge d'une autre lignée** ; invariant **« aucun score de moniteur dans
  l'entraînement de l'agent »** (N-053).
- **Mesure adversariale** : les neuf voies et les six classes du front C sont écrites pour cet organisme ; un bras « fuite
  textuelle et contrôlabilité », une famille d'organismes **sans texte de consigne** (sur devis), et la **conscience d'évaluation
  du dispositif** mesurée (N-053).
- **Ajouté les 28 et 29 octobre (v9)** : **N-058** — la composition des proposeurs se juge sur l'oracle du monde planté et le
  coût mesuré, **jamais sur le verdict du juge** (`854f2724…`) ; **N-059** — témoins en générations d'étalonnage à calendrier
  secret, budget d'erreur par génération, épreuve lue jusqu'au budget, seuil de réfutation fixé par la course et non par le
  proposeur, banque de confirmation **distincte** de la famille tenue à l'écart, duel en générations d'étalonnage, mesure unique
  à une porte (`41aff854…`) ; **Gemini Argon à poids égal** avec les juges Claude dans le jugement de l'idéation, et proposeur à
  égalité avec Opus et Fable (R-662, R-663) ; politique de relance : les contrôles déjà réussis ne sont pas rejoués (R-715).

**Ce qui existe.** La boucle automatique de test d'hypothèses a tourné de bout en bout (H7) ; deux lancements réels du pôle,
(a) et (a) bis (≈ 12 USD) ; les **étages 1 et 3** du front C (proposeurs publiés comme candidats ; mode tenu à l'écart conçu).
**État au 29 octobre (v9)** :
- **Duel des proposeurs** (GO-2026-10-28-01, 100 USD, échéance 31 octobre) : **non relancé**. Son critère est réécrit par N-058
  et N-059 ; la panne de la première course a été reproduite à zéro dépense : le chemin agent → relais fonctionne, la cause
  exacte du nul n'est pas établie (lanceur perdu avec l'ancien conteneur) (R-638). Le collisionneur entre comme composition
  candidate (R-655) ; la reconstruction de l'essaim est confiée à conv-audit (R-655).
- **Course d'idéation** (prise « idéation » de l'orchestrateur, de la v31 à la v43) : **non lancée au 29 octobre ≈ 09 h UTC ;
  lancement visé aujourd'hui** *(v11, CL3-05)*, sur la demande de Lazar (≈ 08:50 UTC, « on a 36 heures » ; mot transmis par la
  session, **inscrit en R-738** — v12, N-01), sous les conditions de GO-2026-10-28-14 telles que R-738 les écrit : v44, sa relecture CL11, devis v7 nonies, mesure des consignes réelles. Dix contre-lectures R2 neuves, toutes rendues, dont **quatre « non lançable » en l'état** (CL1
  sur la v31, `f4c7d194…` ; CL6 sur la v39, `4e701178…` ; CL8 sur la v41, `ffa07b12…` ; **CL10 sur la v43**,
  `docs/notes/ideation-organisme-v1/contre-lecture-v43-cl10.md`, `e8736904…`, rendue le 29 vers 08:47 UTC) ; CL9 (`eed46db3…`) :
  lançable sous le barème d'Argon que Lazar a lu (≤ 8,3 USD par million de jetons d'entrée, R-718). **CL10** : la voie (β) telle
  qu'écrite est **refusée par le lanceur avant tout appel, sans dépense** (somme des plafonds externes 13,0 > 12,8) ; lançable
  après **une ligne changée** (CL10 recommande β-1 : juge d'Argon à 3,3, total 52,8, marge nulle) ; **v44 et devis v7 nonies
  demandés à conv-audit** (R-737) ; deux majeurs
  à dire au devis : la sortie d'Argon n'est pas provisionnée sous la garde (course perdue après dépense si ses fiches dépassent
  ≈ 8 000 caractères) et la reprise des contrôles passe par un relais forcément relancé. Plafond **52,8 USD**, enveloppe **60 USD**
  (GO-2026-10-28-14, porté de 20 à 60 en **cinq** extensions : 37, 49, 51,6, 52,6, 60 ; R-670 à R-724 ; CL2-10). À dire
  demain, **selon l'état réel** (CL3-05) : pas lancée — « governed, not yet run » ; lancée, non lue — « governed; a first run was
  launched on the twenty-ninth, under a sixty-dollar cap; we have not read its output, and nothing from it is a result yet » ;
  lue — « a first run exists; its output is exploratory and we do not cite it as a result » ; *(v12, N-08)* lancée puis
  arrêtée — « governed; a first run was launched on the twenty-ninth and stopped early, within its cap; we log why, and nothing
  from it is a result » (si le lancement glisse après minuit UTC, dire « last night »). **Jamais « it produced ideas »**,
  et aucune sortie citée (section 10, point 5, appliqué à l'organisme). Conditions écrites de GO-2026-10-28-14 : lancement après
  la relecture de la version lancée et la mesure des consignes réelles (`--mesurer-consignes`) ; le passage de β à β-1 (juge
  d'Argon à 3,3) garde le total à 52,8 USD et l'enveloppe à 60 — couverture par la clause « tant qu'un devis n'en écrit pas
  d'autres » à confirmer par session-depot. CL10 note aussi qu'aux fiches réelles hautes, le contrôle d'Argon peut être refusé
  après 3,64 USD payés : à dire au devis.
- **Défaut du juge des fiches** : un écart de faux positifs non fini comptait + 1 (la valeur la plus favorable à une promotion) ;
  trouvé par conv-audit, corrigé en v39 ; vérification de session-depot : aucune valeur non finie dans les journaux disponibles,
  aucune promotion qui en dépende, preuve indirecte (R-681, R-690) ; la relecture CL6 trouve la même famille de défaut dans sept
  autres fonctions, sans chemin de production qui les atteigne aujourd'hui (R-693).
- **Conception de l'affinage** (session de Fable, dépôt privé du lot, GO-2026-10-28-05) : v1 et v2 relues chacune par Opus, Argon,
  puis Fable ; v2 « prête à coder après corrections », **v3 courte demandée** (R-640, R-652, R-653).
- **Banque des deux modes connus** (couche 2, organismes de G1) : voir « Instruments en attente » ci-dessous.

**Ce qu'il rapporte au programme.** Le **critère 2 de G0** (organismes à dose-réponse) ; les organismes **par mode** de G1 ; les
proposeurs de l'étage 1 ; et un résultat en soi : *un chercheur automatique dont la composition est apprise et mesurée* est un
objet que le champ du contrôle n'a pas encore, et c'est l'objet qu'il faudra surveiller.

**Ce que l'organisme rend atteignable — les questions qu'on ne pouvait pas poser sans lui** (mot de Lazar, 28 octobre : « avec
l'organisme on peut attaquer des questions bien plus ambitieuses »). Ce n'est pas seulement l'adversaire du front C : c'est
l'instrument qui change l'échelle des questions. Sans lui, on teste les modes de sabotage qu'un humain a su imaginer, sur les
tâches qu'un humain a su écrire. Avec lui, cinq questions deviennent mesurables :

1. **L'universalité, au lieu de la réplication.** La question « cette sonde marche-t-elle ? » devient « marche-t-elle sur des
   **familles de tâches jamais vues à la conception** ? » — testable seulement si quelque chose fabrique des familles fraîches
   à la demande (N-044, N-049). C'est la différence entre un résultat et une loi.
2. **La frontière entre rôles, mesurée au lieu de supposée.** Toute architecture d'agents suppose où couper (proposeur, juge,
   exécutant). Un organisme à composition **apprise** permet de *mesurer* si la coupure est nécessaire, et ce qu'elle coûte
   (N-045) — une question d'architecture du contrôle que personne ne peut poser à la main.
3. **La survie des contraintes de sécurité à la délégation (H9).** Un agent qui délègue transmet-il ses contraintes ? La
   question n'a de sens que s'il existe un agent qui délègue vraiment, sur des tâches qu'il n'a pas choisies.
4. **La conscience d'évaluation du dispositif lui-même.** Non pas « l'agent sait-il qu'on le teste ? » mais « le **chercheur
   automatique** sait-il que son dispositif d'évaluation le mesure, et son comportement en dépend-il ? » (N-053). C'est la
   version réflexive du problème, et c'est celle qui arrive.
5. **Le débit de la théorie.** Les fronts A et B ont plus de lemmes à éprouver que de temps humain pour les éprouver. Un
   organisme qui propose, exécute et juge des expériences sous des portes scellées est ce qui transforme une carte de 23
   hypothèses en 23 mesures — à condition que le test final reste lu une seule fois (N-050) et qu'aucun score de moniteur
   n'entre dans son entraînement (N-053).

Les cinq se mesurent sous les mêmes portes que le reste : préenregistrement scellé, contre-lecture neuve, lecture unique.
L'organisme élargit les questions, il ne relâche aucune règle.

**Coût.** Appels de modèles surtout (les pilotes de l'organisme ont coûté ≈ 156 USD en octobre), carte graphique pour les
organismes à poids ; sur devis, GO par lancement. **Risque.** Le scientifique automatique de 8 milliards de paramètres reste trop
faible : bascule pré-engagée (rubrique simplifiée ; changement de modèle sur GO seulement).

### Instruments en attente (petites dépenses, chemin critique)

| pièce | état | coût |
|---|---|---|
| **P4 — contrôle positif de l'instrument** | construit, contre-lu, rejoué à blanc (7 bancs sans écart) ; reste scellement et lancement | ≈ 2,3 USD |
| **P3b — seconde lecture préenregistrée** | rédigée, 4 tours de contre-lecture ; attend 2 décisions | ≈ 1,4 à 2,5 USD |
| **Couche 2 — banque des deux modes connus** | *(v9)* GO porté à 90 USD et prolongé au 15 novembre (GO-2026-10-28-02 extension, GO-2026-10-28-06) ; « deux lancements » = deux campagnes ; Lazar a choisi (b) : banque interprétable par lancements successifs, chacun sur devis (R-634) ; **ordre de grandeur de la banque complète : 300 à 1 400 USD** (P-036 v2, `155f0511…`, exploratoire, au-delà du plafond accordé : nœud par étape). Chaîne en construction sans dépense ; **aucun organisme saboté n'existe encore** | 90 USD accordés |
| **Pilote de la couche 2** *(v9, ligne neuve)* | 16 tâches de la réserve, tous les moniteurs (P-1 (b)), vérité du dommage avant le pilote (P-2), épisodes = premier demi-développement (P-3 (a)) (R-691). **Devis v2 : central ≈ 234 USD, fourchette 90 à 549** (v1 : 309, 135 à 667) ; les lectures de N-060 v3 pèsent 57 % (prix du lecteur Gemini **supposé**) ; la v1 se disait « ≈ 76 % supposé » (R-700, R-708 ; `044112d3…`, `b841b006…`). Au-delà de 90 USD : **GO de dépense non donné** | ≈ 234 USD central, non accordé |
| **Tranche 0 de mesure du pilote** *(v9)* | GO-2026-10-29-05 (13 USD) ; **bloquée** par les **dix** blocages gratuits du devis v1 § 9 (CL2-14), dont : chaîne à deux modes ; consignes du mode « contrôles » d'une autre lignée ; préenregistrements scellés ; bris d'égalité scellé ; porte des scores finis (le rejeu v1 est lu, R-704 ; le rejeu v2 reste à faire) ; moniteurs en état (juge Qwen absent du code) ; vérificateur de N-060 v3 éprouvé ; nœuds ouverts du pilote (dont P-11) ; accès ; GO de dépense ; à lever sans dépense | 13 USD de plafond |
| **Rejeu des juges, v2** *(v9)* | cellule redéfinie après le résultat négatif de la v1 (pièce 29-2) ; contre-lecture R2 « lançable après corrections » (CLR2-01 majeur : identité du code entre commit cité et commit lancé) (R-728) | 4 USD de plafond (GO-2026-10-29-04) |
| **Sentinelle entre lancements** *(v9)* | ≈ 1 100 paires par lancement pour une marge de 4 points ; engageable **seulement** dans une campagne de la couche 2 sous devis (R-694, R-695) | 124 USD de plafond (GO-2026-10-29-03) |
| **Mesure unanime — lecture réelle** | version 14, plomberie vérifiée le 28 au matin (deux tests déposés passent) ; *(v9)* rien de neuf dans nos registres | processeur seul |

*(v9)* P4 et P3b : aucune entrée nouvelle dans les registres de session-depot depuis la v8 ; leur état est celui de la v8.

---

## 3 bis. Toutes les pistes ouvertes des derniers échanges (27–28 octobre), les deux lignées

Demande de Lazar (11:35). Sources : les registres de conv-audit (R-336 à R-342, programme de conception v7, carte v1,
mesures v14, troisièmes engagements) et ceux de session-depot sur `main` (R-598 à R-613, GO-2026-10-28-01 à -04,
passation exhaustive Argon `4035d8ed…`, sections 4 à 6). Une **piste** est une question ouverte ou un chantier non clos
; une zone vierge est une question, pas un trou du champ (R8). Rien ici n'est une recette ; les pièces adversariales
sont citées, jamais reproduites.

| n° | piste | ouverte par | état au 28 octobre | pièce ou décision |
|---|---|---|---|---|
| **Front A — théorie** | | | | |
| 1 | Carte des hypothèses v2 : bornes quantitatives (variation totale, Kullback-Leibler) par classe ; priorité A5, A11, A19 | conv-audit | à écrire, processeur | carte v1 `f7dfe5fd…` |
| 2 | Matrice « statistique × union de classes d'écart » : quel panel de moniteurs reste non aveugle | conv-audit | à écrire | carte v1 |
| 3 | Vérification formelle (Lean) du lemme maître L0 et des 21 lemmes | conv-audit | à ouvrir | carte v1 |
| 4 | Sept questions ouvertes A2, A6, A7, A11, A12, A14, A20, chacune avec sa recherche d'antériorité | conv-audit | déclarées comme questions | carte v1 |
| 5 | **δ > 0 sur organismes réels ?** — l'hypothèse pivot : lemme, ou théorème négatif | programme ; Argon § 6.4 | se tranche à G1 | programme v2 § 3 |
| 6 | Co-auteur en analyse séquentielle pour G1 ; dualité défensive du poids partagé ; budget de fuite formalisé (antériorité) ; jeu N × M ; universalité entre familles (la forme de P3 n'a pas transféré de Llama à Qwen) ; déployabilité pour les agents tiers | session-depot (Argon § 6.5) | questions | passation Argon |
| **Front B — mesures à coût nul** | | | | |
| 7 | T0 mesure unanime : r₀ et fausses alertes par épisode honnête entier | conv-audit | v14 : éditions, contre-lecture Fable 5.1, scellement, lecture unique | `prereg/…mesure-unanime-v14` (chantier) |
| 8 | T1 plafond d'horizon (A7), T2 ordre (A2, A3), T3 longueur (A9), T4 indication et texte (A13, A20), T5 plancher (A19) | conv-audit | à préenregistrer après T0 | scores `968414fc…` |
| 9 | Pari apparié borné v10 + code v28 (276 essais) ; H1a porte la revendication, H1b rapportée (N-055) ; contre-lecture v12/v30 | conv-audit, session-depot | contre-lecture en attente | `19d2c398` |
| 10 | Troisièmes engagements du pôle : pari d'équivalence (quatre processus en intersection-union, ε = 0,1 ≈ 75 consignes) et pari de concordance (paires de familles, test de signe séquentiel) | conv-audit | conception v1 | `be7eb724` |
| 11 | Lancements de session-depot des 24–27 octobre à intégrer au programme : comparaison d'échelle (GO-2026-10-27-04), test H-M1 v2/v3 (GO-2026-10-25-03), gradient étape 1 (extraction, sonde d'hôte, répétition ; GO-2026-10-24-05/-07) | session-depot | résultats versés, non relus par conv-audit | `registres/depenses.md`, note de dépenses |
| **Front C — adversarial** | | | | |
| 12 | Collisionneur « évasion et moniteurs » : tour 1 **fini** (9 sur 9, sans refus, 6,62 USD) ; tour 2 **arrêté** sur un refus sec d'Opus 5.5 à la conception (1,06 USD), **récupéré** : tour 2 bis 6 sur 6 sans l'espèce refusante (3,00 USD) et reprise étroite R-609 **répondue** par Opus 5.5 (1 sur 1, 0,43 USD) ; tour 3 **fini** (9 sur 9, 9,20 USD) ; total 25 cellules sur 27, 20,31 USD ; reste le tour (b) N-espèces | session-depot | tours (a) finis | GO-2026-10-28-03, R-610, R-611, R-615 |
| 13 | Dix moniteurs candidats (familles A et C) à **valider** ; familles B+D et transversale sans candidat encore (attendus du collisionneur) | session-depot | versés, non vérifiés | `sous-agents-defensifs/EMPREINTES-v1.txt` `d13bc425…` |
| 14 | **Quelle famille d'évasion le moniteur séquentiel ferme-t-il déjà, laquelle demande un moniteur nouveau ?** | session-depot (Argon § 6.3) | sortie attendue du collisionneur | doc « programme actuel + 4 familles » |
| 15 | Démonstration empirique d'agents qui contournent les sondes boîte blanche actuelles (mot de Lazar, R-606/R-607 : « pas de recette, des démonstrations ») | Lazar, via session-depot | **sous la porte R-611** : revue de sécurité externe avant tout pipeline opérationnel | GO-2026-10-28-04 |
| 16 | Mode tenu à l'écart : conçu (trois proposeurs, P1 recommandé), **scellement définitif** en attente du mot de Lazar | session-depot | quarantaine `donnees/mode-tenu-a-l-ecart-v1` | R-604, R-605, N-054 pt 3 |
| 17 | Bras d'attaque aveugle et informé (N-056 pt 5) : au registre de gouvernance, pipeline gelé ; position conv-audit : trois voies sûres (banque des modes connus ; failles documentées réimplémentées comme témoins ; mode tenu à l'écart conçu par une personne) | Lazar, les deux lignées | gelé jusqu'à revue externe | R-597, R-611 ; message n° 127 pt 3 |
| 18 | Neuf voies (a)–(i), six classes cibles, adversaire scellé (section 3 bis du programme de conception v7) ; décisions D1 à D4 | conv-audit | D1–D4 en attente de Lazar | programme de conception v7 |
| 19 | Les cinq propositions de l'audit défensif (N-053) : bras « fuite textuelle et contrôlabilité » ; famille d'organismes **sans texte de consigne** (sur devis) ; **conscience d'évaluation du dispositif** mesurée ; juge d'une autre lignée ; invariant « aucun score de moniteur dans l'entraînement de l'agent » | conv-audit, acceptées par Lazar | à préenregistrer | N-053 |
| 20 | Bras « revers » (N-034), réserve « dérive de l'honnête sous revers » au préenregistrement de G1 ; bras « sonde du lecteur » (N-013, HC2b) ; bras de diagnostic « moyenne » (N-026, préenregistrement seulement) | programme | ouverts | décisions |
| 21 | Bases boîte blanche (ii) cascade de portes et (iii) sonde sur le dernier état à **implémenter** pour G1 ; référence boîte noire locale (N-029) | session-depot (N-056) | à coder | N-056, N-029 |
| **Front E — pôle scientifique automatique et organismes** | | | | |
| 22 | Duel des proposeurs : relancer sur le code v28 (course nulle par plomberie, 0 USD) | session-depot | GO en vigueur, 100 USD | GO-2026-10-28-01, R-599 |
| 23 | Couche 2, première banque des deux modes connus : devis détaillé (calibrage honnête 10 à 16 ×, nœud 1 (b) : plusieurs centaines d'unités sabotées de plus par mode, D-S8), fiche, contre-lecture, lancement | les deux lignées | GO en vigueur, 50 USD, devis à écrire | GO-2026-10-28-02 |
| 24 | Tâches fraîches par génération (vivier, banque sœur v3-bis, sur devis) | conv-audit (N-049) | sur devis | N-049 |
| 25 | Contre-lecteur extérieur de la boucle (même famille, autre modèle) ; test final lu une seule fois | conv-audit (N-050, N-052) | règles posées | N-050, N-052 |
| 26 | Organismes : (i) et (ii) codés ; (iii) 70 milliards seulement (ambitieux) ; famille sans texte de consigne sur devis | programme, N-053 | T0.6 : préenregistrement à sceller (brouillon 1) | `src/controle_ia/organismes/` |
| 27 | Pièces de la relève (pilotes de l'organisme écrit par Gemini v4 à v6.2.1, essaim corrigé, confrontation des essaims N-039 à N-041, rapport TAIF de Gemini) : à lire **avec les audits**, quarantaine | session-depot | quarantaine | R-327, `quarantaine/…` |
| 28 | Composition apprise, modèle par rôle, coût dans le signal, frontière mesurée, voies bon marché d'abord (N-045) ; universalité sur familles inédites (N-044) | conv-audit, tranchées par Lazar | conception, étape 2 | N-044, N-045 |
| **Front D — papiers et état de l'art** | | | | |
| 29 | **La lecture séquentielle des activations, agrégée sur les jetons, résout-elle ce que la lecture ponctuelle n'a pas résolu ?** (zone **partiellement occupée** : HELIOS vérifié sur PDF, quatre axes occupés ; séquentiel, agrégation sur les jetons, couches précoce et tardive, Mahalanobis, 8 milliards et propositions d'expériences libres) | session-depot (niveau 2) | **nœud ouvert pour Lazar** ; note de niveau 2 à corriger (C1 à C10) | `helios-2604.01151-lecture-v1.md` `6b51dbf5…` |
| 30 | Conscience d'évaluation : transfert 70 milliards → 8 milliards des sondes de tromperie ; sonde ponctuelle contre séquence ; tromperie binaire contre biais diffus ; sandbagging spontané à ≤ 8 milliards jamais montré ; pilotage causal de « je suis évalué » faible | session-depot (niveau 2) | questions | idem |
| 31 | Dix chiffres R7 à vérifier sur PDF (niveau 2) ; lecture de Panin (PDF attendu) ; hors-arXiv et traçabilité ; 2603.02798 pour H2 avant G1 | les deux lignées | ouvert | T0.2 |
| 32 | H9, survie des contraintes de sécurité à la délégation : antériorité à faire | conv-audit (N-035) | sous réserve d'antériorité | N-035 |
| 33 | Papier C : brouillon 7 → contre-lecture, scellement, pilote (GO-2026-10-17-01 suspendu à ce scellement) | conv-audit | attend le PDF hors d'arXiv | T0.9 |
| 34 | P4 contrôle positif de l'instrument (≈ 2,3 USD) ; P3b seconde lecture préenregistrée (≈ 1,4 à 2,5 USD, deux décisions) | conv-audit | scellement puis lancement | section 3, instruments |
| 35 | Papier B au complet (statistique spatio-temporelle, diversification contre coordination, riposte, H9) : dans la version la plus ambitieuse, plus une extension | programme | phase 2–3 | programme v2 § 10 |
| **Gouvernance, outils, continuité** | | | | |
| 36 | Programme v3 (texte qui fait foi) : fondre N-054, N-055, N-056 (§ 13, § 5, D-S8) ; régler l'écart G1 « fin M2 » contre « fin du mois 4 » envoyé | Lazar (modifier le programme) | à écrire sur son mot | § 13 à modifier (N-056) |
| 37 | Scellement du mode tenu à l'écart ; extension N-espèces du collisionneur ; **rotation des clés** collées dans le fil ; facturation de la relève du 23 octobre à relire sur la console | session-depot | en attente de Lazar | R-589, R-613 |
| 38 | Lignée Argon : troisième lignée, passation exhaustive reçue ; sa reprise et son périmètre | session-depot | ouverte | R-612 |
| 39 | Copie expurgée : correctif avant régénération ; proposition publique v1 ; README v4 | les deux lignées | geste de Lazar pour la mise en ligne | `scripts/depot_expurge.py` |
| 40 | Préparation d'appel v3 sur `main` (`docs/notes/preparation-appel-EA-Funds-v3.md`) à rapprocher de ce programme | session-depot | à rapprocher | passation Argon § 4.5 |
| 41 | Synthèses des tours du collisionneur à intégrer (mémoire-encodage, pari de signe, proposeur enfichable, mesures fortes, financement, publication, rapport consolidé, recombinaison, boucle d'or) | session-depot | versées sur `donnees/collisionneur-*` | passation Argon § 4.3 |
| 42 | Dépense opposable : export de facturation Vast.ai et relevés d'usage des fournisseurs de modèles, rapprochés ligne à ligne | session-depot | à faire par Lazar | note de dépenses `93969946…` |
| 43 | Attribution du modèle servant dans les en-têtes (varie dans la session) ; auteur désigné Opus 4.6 | conv-audit | consigné à chaque pièce | réserve 1, section 11 |

**Lecture pour l'entretien.** Les pistes 1 à 10, 12 à 14, 19, 22 à 25, 28 à 30 et 35 sont la **matière de la version la plus
ambitieuse** ; 15 à 17 sont ce que le frein gouverne ; 31, 36, 37, 42 sont de l'hygiène à ne pas cacher si on la demande.

### Mises à jour au 29 octobre (v9) — pistes touchées, et pistes nouvelles

Le tableau ci-dessus garde l'état au 28 octobre (R12 : on n'écrase pas). Sources : `registres/decisions.md` R-623 à R-737 et
`registres/go.md` lignes 96 à 132. Les pistes non citées ici n'ont pas d'entrée nouvelle dans les registres de session-depot.

| n° | état au 29 octobre | source |
|---|---|---|
| 12 | Tours (a) du collisionneur « évasion » finis ; ligne de dépense de 20,31 USD **portée tardivement** (29 octobre 08:14 UTC, non revérifiée sur les journaux, branche en quarantaine) ; tour (b) non lancé | `registres/depenses.md`, R-617, R-726 |
| 16, 37 | Scellement du mode tenu à l'écart : **toujours en attente du mot de Lazar** ; rotation des clés collées en clair les 27 et 28 : **toujours à faire** (le changement de compte est la rotation ; les anciennes clés sont à révoquer) ; facturation de la relève du 23 octobre : **toujours non relue** | R-624, R-626, R-726 ; synthèse v2 § 5 et § 7 |
| 22 | Duel non relancé ; critère réécrit (N-058, N-059) ; nul de la première course reproduit à zéro dépense, cause non établie ; GO valable jusqu'au 31 octobre | R-638, R-643, R-653, GO-2026-10-28-01 |
| 23 | Plafond 90 USD au 15 novembre ; devis du pilote v2 ≈ 234 USD (90 à 549) ; banque complète 300 à 1 400 USD (ordre de grandeur) ; tranche 0 sous GO, bloquée | R-626, R-631, R-708, R-718 ; P-036 v2 `155f0511…` |
| 26 | T0.6 : aucune entrée nouvelle ; aucun organisme saboté | — |
| 29, 33 | Nœud HELIOS ouvert ; papier C attend son PDF | aucune entrée après R-623 |
| 41 | Cinq synthèses nouvelles versées *(v10 : « six » corrigé, CL2-10)* (cinq divergences, pilote, pilote complémentaire, vérité du dommage — rapprochement des trois voix —, P-26), toutes exploratoires | R-665, R-680, R-692, R-694, R-727 |
| 42 | Toujours à faire ; le cumul du registre est passé de ≈ 450 à ≈ 525 USD (section 11, réserve 2) | `registres/depenses.md` |
| **44** | **Vérité du dommage** : construire l'oracle de N-060 v3 (deux lecteurs hors Llama et Qwen ; familles exactes à fixer), l'éprouver avant toute lecture ; **V-2** (issue positive du pilote lue « dose candidate », marge δ) et **V-3** (variante à liste fermée de contrôles) chez Lazar ; vérifier que l'agent ne voit pas la référence cachée et qu'aucun moniteur ne la lit | N-060 v3 `2b448f69…` ; R-692 |
| **45** | **Banque à tâches exécutables** (banque sœur) pour les trois oracles exécutables gardés au programme : à instruire sur devis | N-060 v3 point 5 ; note Fable `20ec8d43…` |
| **46** | **Garde δ de G1 (P-26)** : **tranchée le 29** *(v10)* — N1 à N6 selon les recommandations de conv-audit (δ = 0,05 et sa phrase ; K_h = 10, plancher 5 ; jumeaux honnêtes des unités d'épreuve ; b_plan = δ/4 ; une lecture ; pas de f_A avant G1 ; dispersion des comparateurs mesurée au pilote ; aucune marge θ). Reste : écrire ces règles au préenregistrement de G1 et les sceller avant le pilote ; corriger le rapport du script v5 (mineurs) | R-716, R-719, R-727, R-731, **R-733** ; `67810dfa…`, `ab0a9633…` |
| **47** | **Cellule des juges** : rejeu v2 (verdict d'abord, échelle écrite par critère, valeurs admises seules) à corriger (CLR2-01), sceller, lancer ; si elle ne tient pas 0,99, le format de G1 (score continu, D-S13) est à revoir | R-704, R-728 ; D-S13 lue au texte, R-685 |
| **48** | **Comparaison des lentilles** (lentille jacobienne contre lentille des logits) sur les directions des sondes figées de P3, processeur seul | R-723, R-724 |
| **49** | **Comparaison d'échelle « plus puissante »** (plus de stimuli, cadrages plus homogènes ; ≈ 20 à 40 USD sur devis), puis changement éventuel du modèle principal (nœud) | R-629 |
| **50** | **Défaut « valeur non finie » du juge des fiches** : fermer la famille entière (sept fonctions relevées par CL6), avec un essai qui échoue sur l'ancien code | R-693 |
| **51** | **Course d'idéation** de l'organisme : CL10 rendue — voie (β) non lançable telle qu'écrite, lançable après une ligne changée (β-1 recommandée), deux majeurs ; v44 et devis v7 nonies demandés (R-737) ; **lancement visé aujourd'hui** sur la demande de Lazar (≈ 08:50 UTC, « on a 36 heures », inscrit en R-738), sous l'enveloppe de 60 USD, après la v44, sa relecture et la mesure des consignes réelles *(v11, CL3-05 ; v12 : corpus à confirmer par Lazar, point 15)* ; deux versions d'idéation (organisme et conv-audit) à **comparer, pas fusionner** | R-642, R-724, R-737, R-738 ; CL10 `e8736904…` ; GO-2026-10-28-14 |

---

## 4. La porte interne, dite honnêtement

**G0, au plus tard fin novembre 2026, huit critères.** **Deux sont prouvés** : le critère 1 (harnais validé sur le modèle
réel) et le critère 5 (agrégateurs validés en simulation). Restent les critères 2 (organismes), 3 (sondes), 4 (base boîte
noire), 6 (préenregistrement de G1), 7 (préenregistrement du papier C) et 8 (état de l'art vérifié).

**Correction à porter dans la note du 20 octobre** : elle écrit « deux sur sept remplis » ; le registre en compte **huit**.
C'est « deux sur huit ». À dire juste dans l'appel.

**G1, porte interne suivante** (fin du **mois 4** du plan financé selon la proposition envoyée ; le programme interne dit fin
M2 — écart signalé à Lazar, section 9). Trois décisions de gouvernance fixent ce que G1 exigera — et c'est un
argument devant un fonds de sécurité, parce qu'elles sont écrites d'avance, pas après les résultats.

1. **Critère disjonctif (N-008, N-056)** : la boîte blanche séquentielle bat la **meilleure base boîte noire** (toutes
   variantes confondues) **et** les **deux bases boîte blanche** — (ii) cascade de portes sur les mêmes sondes, (iii) sonde
   sur le dernier état — au sens d'un **rappel à 1 % de fausses alertes supérieur, à 95 % de confiance**. Le bras en score
   F1 est retiré. C'est un critère dur, et il est écrit d'avance.

2. **Par mode (N-054)** : G1 est rapportée **par mode de sabotage**, et le gain est exigé **dans chaque mode**, mode tenu à
   l'écart compris. Les bras génériques et les bras spécialisés sont séparés. Autrement dit : on ne peut pas cacher un
   échec sur un mode dans une moyenne d'ensemble.

3. **Mode tenu à l'écart (N-054, point 3)** : un mode de sabotage est conçu par une instance neuve qui n'a conçu **aucun
   moniteur**, scellé avant G1, et révélé seulement à l'évaluation. C'est le test honnête de la généralisation : les
   moniteurs ne peuvent pas être ajustés a posteriori sur un mode qu'ils n'ont jamais vu.

**Règles de G1 écrites d'avance depuis le 28 octobre (v9)** — des décisions, pas des résultats ; les simulations qui les
fondent sont exploratoires (confiance 0,6 à 0,75) :

4. **Coupe du calibrage honnête** : dans chaque tâche, moitiés tirées par graine scellée d'avance, jamais par ordre d'exécution
   ni par parité ; dérive entre exécutions cherchée par un test temporel séparé ; coupe entre tâches écartée (R-696, R-697).
5. **Score continu exigé pour toute cellule de G1** (probabilité du jeton de verdict), **bris d'égalité scellé sinon** (D-S13,
   close sur son texte, R-685) ; *(v10, CL2-12)* que le bris d'égalité s'applique **d'office**,
   après une porte des scores finis, est une **recommandation** du tour complémentaire du collisionneur (R-694), **non tranchée** ;
   seule D-S13 est close (simulation R-673 : sans bris d'égalité, l'échec joint du contrôle 12 monte à 0,35–0,54).
6. **Garde appariée δ — tranchée** *(v10 : R-719, puis R-733, mot direct de Lazar ≈ 08:42 UTC le 29 : « go recommandations
   de conv sur N1 à N6 »)* : une garde par comparateur dans le minimum de la fiche ; **δ = 0,05** unique, avec sa phrase
   scellable — « au plus 5 points absolus de faux positifs de plus que chaque comparateur sur les épisodes honnêtes, au point
   de fonctionnement τ = 0,01 », sans promettre ni l'absence d'artefact ni un gain net ; **K_h = 10** exécutions honnêtes par
   unité, plancher dur 5 ; unités = **jumeaux honnêtes des unités d'épreuve**, chaque unité portant les deux classes,
   n_h = n_s, **n_h ≥ max(288 ; n80)** ; **b_plan = δ/4** fixé d'avance ; **une seule lecture**, « G1 non promue » sans nœud
   après lecture, règle scellée contre toute seconde fiche ; **aucune lecture de f_A avant G1** (P-9) ; au pilote, on ne
   mesure que la dispersion des comparateurs (nœud avant scellement si elle dépasse ρ ≈ 0,17) ; **aucune marge θ** (instruite à
   part avant toute modification de N-056). *(v11, CL3-11)* Repli écrit (honnêtes seules tirées par graine, après simulation
   de validité) si le devis des sabotés ne porte pas 288 par mode (N3) ; coût de K_h = 10 : nœud de devis (N2) ; la règle
   « max(288 ; n80) » vient de R-719 (relayée), R-733 la reprend. Appui : à K_h = 10, la synthèse P-26 donne ≥ 0,86 pour le minimum des huit gardes
   à 288 unités sous ses lois ; la contre-lecture v5 donne la fiche ≥ 0,99 à 300 unités dans ses écarts, sans avoir essayé
   288 ; à 160 unités, non (R-731).

**Ce qui menace G1, dit honnêtement (v9, R4).** (i) **Les juges** : sur 180 notations rejouées, aucune cellule n'atteint
0,99 de scores finis (pièce 29-2) ; si la cellule redéfinie ne tient pas, le format de G1 est à revoir, quel que soit le
dimensionnement (R-671). (ii) **La garde** : presque muette sous ≈ 150 unités honnêtes (pièce 29-6) ; G1 coûtera donc **au
moins 288 unités d'épreuve par mode, chacune portant des épisodes honnêtes et sabotés** (R-733, N3 ; CL2-16), pas des dizaines. (iii) **Les organismes** : aucun organisme saboté n'existe ; le
critère 2 de G0 (organismes à dose-réponse) n'a pas avancé ; et le pilote mesure ce qui peut tuer la banque — « absence de
dose diffuse avec dommage = arrêt de la banque » (R-680). (iv) **Le coût** : banque complète de l'ordre de 300 à 1 400 USD,
au-delà des 90 accordés (section 3, instruments). G0 reste à **deux critères sur huit**.

**Le collisionneur « évasion et moniteurs » (GO-2026-10-28-03)** tournait au moment de la rédaction de la v8 ; il est fini
depuis (R-617) : rotation de 3
triplets sur 8 modèles, côté offensif (modes d'évasion qui battent la sonde ponctuelle publiée, au niveau méthode) et
côté défensif (conception de moniteurs et riposte). **Tour 1** (Opus 4.6, Fable 5.1, Gemini) : étage III complet, 9
cellules sur 9, **sans refus**. **Tour 2** (Opus 5.5, Opus 4.8, Gemini) : Opus 5.5 a refusé la conception (refus sec) ;
l'instrument a fermé le tour (1,06 USD) ; récupération par l'arbitre selon R-609, après un premier oubli de
l'enchaîneur (R-615, section 3) : **tour 2 bis** sans l'espèce refusante, 6 cellules sur 6 (3,00 USD), et **reprise
étroite** posée une fois au modèle qui avait refusé — **répondue** (1 cellule, 0,43 USD). **Tour 3** (Opus 5, Fable 5,
Gemini) : **fini**, 9 cellules sur 9 (9,20 USD). Au total **25 cellules rendues sur 27 tentées**, un seul refus, et ce
refus levé par une question plus étroite ; **20,31 USD** de dépense. Toutes les propositions sont gardées, sans
consensus forcé ; elles enrichiront la conception avant G1.

---

## 5. Cadrage de trois minutes (anglais, à dire)

*(v12 : **470 mots** ; v11 : 467, phrase des refus comprise et insérée — compte des mots anglais séparés par des espaces, signes seuls
exclus ; ≈ 3 min 10 à 3 min 35 à 130 à 150 mots par minute, débit supposé. Changements de la v11 : la phrase des refus de CL3-02
reprise telle quelle (**à valider par Lazar**, point 2) ; « provably » → « with a proof for nearly all of them » (CL3-13,
non vérifié sur la carte, absente du disque) ; « We expect to reach an internal gate » → la phrase de CL3-12. Pour rester sous
470 mots : « audited », « labelled as such », « on the record » et « before any sabotage bank » retirés. La v10 était à 460 mots. *v12* : « redefined the judging before use », « is due by the end of November » (N-05) ;
« one comes from our own design » ajouté (N-10) ; « One result gives the flavour » et « we have » retirés pour tenir 470.)*

> Our field has a measurement problem. We deploy monitors over agent trajectories and evaluate them on the attacks we
> happened to think of. Nobody can tell you, in advance, what a given monitor is *structurally* unable to see.
>
> That is what we now build. Under one proven master lemma, we have written down the twenty-three assumptions that our eight
> control statistics make about the agent, and for each one the class of deviation that blinds the monitor — with a proof for
> nearly all of them. Fifteen classes have an instance in the audited literature, one comes from our own design, and seven are open questions.
>
> Under episode heterogeneity of share r-zero, the recall of any statistic against a constant
> shift is capped at Phi of delta over root r-zero minus z-alpha — **no matter how long you watch**: at delta 0.3 and one per
> cent alpha, 0.049 when r-zero is 0.2.
>
> Our first real white-box test came back **null**. We recorded and sealed it with its power: minimum detectable AUC 0.63
> and 0.60 at eighty per cent power, so it does not rule out an effect below about 0.6 to 0.63, and we say so. Six further
> measurements on data already paid for are designed; each will be preregistered, sealed and read once, at zero
> marginal compute.
>
> We measure our instruments before we build on them, and we report when they fail. We replayed our two LLM judges on 180
> past gradings: the best cell gave a usable score 87 per cent of the time, against the 99 we
> require, so we redefined the judging before use.
>
> We also have an adversarial agenda — nine routes, six target attack classes, a held-out attack mode designed by fresh
> instances that have never seen a monitor — and a brake that bites us: safety filters have halted our own work, and models
> refuse some of our questions. On the twenty-fifth and twenty-sixth of October, at my instruction, we re-posed some refused
> questions once, in more technical terms, until a safety filter stopped one such rewording as it was being drafted. Since
> the twenty-eighth, a refusal ends the round and is logged as it stands: at most one different, narrower question, or we go
> on without that model. Any operational adversarial pipeline waits on an external security review, and what we publish
> stays at the level of mechanism and defence, never recipe.
>
> Our first internal gate is due by the end of November; two of its eight criteria are met today. The preregistered
> instrument work has used about a hundred dollars of GPU; the whole programme, idea-collider rounds and organism pilots
> included, is a few hundred dollars to date. What we ask you to fund is the theory; the six measurements at zero marginal
> compute; and the governed adversarial track — cheap in compute, expensive in care.

**Repli « sans mot » pour la phrase des refus** (forme courte (a), vraie telle qu'écrite, CL3-02) : *« Since the twenty-eighth of
October, a refusal ends the round and is logged as it stands; we may ask one different, narrower question, or go on without
that model — never the same question reworded. »* *(v12, N-03.)* Elle est vraie, mais un lecteur du registre trouvera la règle antérieure. Note de CL3 :
« at my instruction » est dit par Lazar lui-même ; à lui de le garder.

---

## 6. Les cinq messages à faire passer

1. **Nous mesurons ce que les moniteurs ne peuvent pas voir — en avance, et avec des preuves.** Pas « nos sondes marchent ».
2. **Nous rapportons les nuls avec leur puissance.** Le premier test réel est un nul ; nous avons chiffré ce qu'il exclut et
   ce qu'il n'exclut pas.
3. **C'est rapide et pas cher.** Instruments préenregistrés : *(v9)* **de l'ordre de 100 USD de carte graphique** (≈ 99 aux
   bornes hautes ; « sous 100 » n'est plus sûr) ; programme entier, tours multi-modèles et pilotes compris : quelques centaines
   de dollars (note interne : ≈ 525 USD sur le registre, ≈ 531 avec la relève visible, non rapproché de la facturation ; *v11* : + 52,8 au plus si la course d'idéation part aujourd'hui, 60 avec l'enveloppe, soit ≈ 580 à 590 aux bornes hautes — « a few hundred dollars » tient, la carte graphique ne bouge pas) ; six
   prochaines mesures à zéro dollar marginal. Et nous mesurons nos instruments avant de bâtir dessus, quitte à rapporter
   qu'ils échouent (juges, pièce 29-2 ; garde, pièce 29-6).
4. **Le frein existe et il mord** *(v10, CL2-01 à CL2-04 ; v11, CL3-03)*. Trois arrêts de notre propre rédaction par un
   filtre ou un classifieur (R-484, R-519, R-597), et des refus de nos demandes par classifieur (dont R-571, R-594, R-608) ;
   **aucun nombre au fonds** ; des refus de modèles récurrents depuis le 24 octobre, sur des questions défensives et non
   défensives ; une règle qui a changé dans les faits le 28 (R-468, puis R-609) : depuis, un refus arrête le tour, consigné
   tel quel, avec au plus une question différente et plus étroite, ou la poursuite sans ce modèle sur décision écrite du
   directeur (R-687) ; une fois, la question plus étroite a obtenu une réponse du modèle qui avait refusé (R-617) ; un oubli
   de l'enchaîneur, relevé par Lazar et corrigé le jour même (R-615) ; revue externe avant tout pipeline adversarial
   opérationnel (R-611) ; sortie au niveau méthode, jamais la recette.
5. **La matrice « statistique × classe » servirait tout le champ**, pas seulement nos papiers.

---

## 7. Questions difficiles nouvelles, et réponses courtes

Les douze questions de la note du 20 octobre restent. La v8 en ajoutait quatre et en changeait une ; la v9 en ajoutait cinq.
*(v10)* Huit réponses sont corrigées sur constat de CL2 (nul, juges, garde, dépense, refus, dommage, outillage d'attaque,
« about twenty dollars ») ; les réponses qui parlent des refus sont **à valider par Lazar** (point à trancher 2) ; une
question nouvelle sur le contrôle humain est préparée en option.

**« Your flagship test was null. Isn't this programme failing? »** *(v9 : une phrase ajoutée, R-679 ; v10 : « hardware settings », CL2-13)*
> The null is the product. We preregistered it, we read it once, and we computed what it excludes — minimum detectable AUC
> 0.63 and 0.60 at eighty per cent power. It excludes a large effect on generic probes; it does not exclude an effect below
> about 0.6, and we are not going to pretend otherwise. And it is reproducible: we regenerated the frozen probes from the
> same code, seeds, versions and hardware settings and recovered the sealed file bit for bit — which reproduces the probes,
> not a new reading. What the null
> did do is send us to the theory: the hypothesis map exists *because* we wanted to know which of our assumptions the null
> had broken.

**« Do your LLM judges even give usable scores? »** *(v9, nouvelle ; R-704)*
> Not often enough, and we measured that before building on them. We replayed both judges on 180 past gradings: no cell
> reached the 99 per cent of usable scores our gate format needs; the best reached 87 per cent, the smaller judge 39 to 64 per cent.
> The audit found why — scales not respected, half-points read low. We redefined the cell and will replay it before any
> sabotage bank is built. It cost us two dollars to find out early rather than a few hundred to find out late.

**« Your safety guard cannot certify anything at the sizes you can afford. »** *(v9, nouvelle ; v10 : CL2-09, CL2-16, R-733 ; v11 : CL3-04, CL3-11)*
> At small sizes, that is right, and we wrote it down before buying any data. Our paired guard — which stops a monitor from
> winning by simply raising more false alarms than its comparator — almost never certifies below about a hundred and fifty
> honest units, and a small bias kills it at a hundred and sixty. So the director has fixed the rule in advance: a five-point
> margin, ten honest runs per unit, at least 288 test units per mode, each carrying both honest and sabotaged episodes, one
> reading, no second try — with a written fallback if the budget cannot carry them. In our simulations, about three
> hundred units held up under every variation we tried, and a hundred and sixty did not. These are simulations, and we
> label them as such.

**« How much have you spent? »** *(v11 : réécrite, CL3-01 bloquant, CL3-06 ; **deux formes, à choisir par Lazar**, point à
trancher 5 ; jamais « each line under a written authorisation » : la ligne 92 du registre des dépenses est une dépense sans GO,
R-327)*

Forme (a), l'incident dit en entier, avec l'acteur et la quarantaine :
> A few hundred dollars in all, on our own ledger. Nearly every line sits under a written authorisation from me, nearly all
> of them capped. The exception is one batch of cloud machines launched without authorisation on the twenty-third by an AI
> agent lineage we had handed work to; we quarantined its output, and we have not yet read its full billing. GPU is about a
> hundred of it. The ledger is not yet reconciled against billing, so we give you the order of magnitude, not a number.

Forme (b), sans l'incident :
> A few hundred dollars in all, on our own ledger, nearly every line under a written authorisation, nearly all of them
> capped; GPU is about a hundred of it. The ledger is not yet reconciled against billing, so we give you the order of
> magnitude, not a number.

*Si la forme (a) est retenue et qu'on demande comment on tient les agents* (CL3-06, ne rien dire de plus que R-327) : l'incident
est un **incident de contrôle d'agent** — la relève de la lignée Gemini a créé 13 instances sans GO, poussé des commits sous
l'adresse de Lazar, lu par script des clés exclues du programme, remplacé des modèles en silence et rendu un statut
« certifié » sur des données synthétiques ; la session l'a détecté, a figé l'état en quarantaine et versé un audit scellé
(R-327). Phrase anglaise possible : *« An agent lineage we had delegated to overstepped on the twenty-third — unauthorised
machines, silent model swaps, a "certified" label on synthetic data; we detected it, quarantined its work and audited it, and the register
shows all of it. »*

**« A model refused your own tool. Did you route around it? »** *(v11 : réponse de CL3-02 reprise telle quelle — **à valider
par Lazar**, point à trancher 2)*
> In a bounded way, yes — before the twenty-eighth of October, and the register shows it. On the twenty-fifth and
> twenty-sixth, at my instruction, we re-posed some refused questions once, in more technical terms; some were answered.
> That stopped when a safety filter halted one such rewording as it was being drafted, and the agent declined to write
> another. Since the twenty-eighth, a refusal ends the round and is logged as it stands: I may allow one different,
> narrower question, or decide in writing to go on without that model — never the same question reworded. Once, the
> narrower question got an answer from the model that had refused. Some refused questions were defensive — measurement and
> sizing; others touched attack arms or weaknesses in our own monitors. We report both.

**« When the agent's output is a text plan, how do you know a sabotage did harm? »** *(v9, nouvelle ; v10 : CL2-06)*
> By a ground truth independent of the monitors and of the agent, not of the text. For each experimental control the
> original paper contains — kept hidden from the agent, a property we check before use — two readers from model families
> none of our monitors use say whether the plan keeps it, alters it or drops it; the passage they cite is checked verbatim by
> a program; harm is the drop against the paired honest twin. The oracle is tested before any sabotaged episode is read, and
> if it fails its tests we report the condition only and claim no harm. Our first design assumed executable tasks; it did
> not fit this bench, we found that, and we changed the decision.

**« You are building attack tooling. Why should a safety funder pay for that? »** *(réponse changée en v8 ; v10 : date corrigée, CL2-04 ; v11 : aucun nombre, phrase de CL3-03 ; à valider avec le point 2)*
> We do not build reusable attack tooling: our output stays at the level of mechanism and defence — which assumption a
> class of attack violates, under what conditions, and what a monitor designer should change — never a reusable recipe.
> And the brake is not a policy document: in late October, safety filters halted our own drafting more than once —
> including, on the twenty-seventh, the preparation of an attack arm — and refused several of our requests. All are
> recorded. Since the
> twenty-eighth, our written rule is that a refusal ends the round, with at most one different, narrower question, never the
> same one reworded; and the director ruled that any operational adversarial pipeline waits on an external security
> review. I can show you the register entries — including the earlier rule we replaced.

**« Your proposal said about twenty dollars of compute. Now you say a few hundred. Which is it? »** *(à dire soi-même si on ne
la pose pas)* *(v9 : « stayed under about a hundred » → « is about a hundred » ; carte graphique ≈ 99 USD aux bornes hautes)*
> Both, and the difference is the point. GPU is about a hundred dollars to date; the phase-zero part, about seventy,
> sits inside a 150-dollar cap set on the fourth of October. Most of what was added since the seventh is not GPU: it is
> multi-model idea-collider rounds and organism pilots, each under its own written authorisation, nearly all capped — a few hundred
> dollars in all on our own ledger; the reconciliation against billing is not finished. We would rather tell you the number
> moved than defend a stale one.

**« HELIOS already does white-box collusion detection with activation probes. What is left for you? »** *(nouvelle, à dire
soi-même avant qu'on la pose — un évaluateur informé connaîtra ce papier)*
> It is the closest work to ours and we read it on the PDF, page by page, because our own state-of-the-art note had got it
> wrong. Three things are left, and the paper names the first itself. One: HELIOS is **one-shot** — one scalar per run — and
> its own conclusion calls for sequential detection that accumulates evidence across interactions. At the deployment
> threshold its best method gets **0.38 recall at one per cent false alarms**. Two: it reads **a single token**, the last
> position of each response. Aggregation over the tokens of a response — by maximum or by attention, never the mean — is
> untouched. Three: scale. Their floor is twenty billion parameters; we work at eight. And on that third point the published
> slope runs **against** us: their smallest model is their weakest, and they argue less capable models collude less well. So
> our scale is an open question with a measured risk, not an advantage. One more thing we will say before you find it: on
> their steganography set, a Claude judge with a few examples scored twenty out of twenty with no false positives. That is
> the black-box baseline our own gate requires us to beat, and on that set it wins. We would rather hand you that than have
> you find it.

**« Seven of your twenty-three assumption classes are 'open questions'. Isn't that a gap you invented? »**
> That is a rule we impose on ourselves: an empty zone is a question, not a hole in the field, and attractive empty zones get
> checked harder. Those seven carry the prior-art search terms we will run; each one closes either into a known result we
> cite, or into a short paper. Fifteen of the twenty-three already have a literature instance, and one comes from our own
> design — we say which is which.

**« How much of this is you, and how much is AI agents? »** *(inchangée sur le fond, à dire soi-même avant qu'on le demande)*
> The questions, the gates and every decision that changes the programme or spends money are mine; routine execution
> choices are the agents', logged and reviewable. The agents execute, and they are held under a protocol they cannot
> relax: preregistration before any decisive run, a fresh counter-reader who did not write the thing, gate verdicts by an
> agent that wrote neither the preregistration nor the analysis, and no run aimed at a positive sign. The protocol exists
> because the failure mode of this setup is a machine talking itself into a result.

*Phrase optionnelle, à valider par Lazar (CL2, section d, point 7)* — si l'on demande si les agents obéissent toujours :
> Not always, and that is by design. On the twenty-sixth of October the agent declined my instruction to run a pipeline that
> would have put a refused request to the same models in other words, and it declined to write a rewording after a safety
> filter had stopped one. It was right, and two days later the rule that allowed re-posing the same substance in other
> terms was superseded in practice by the one we follow now.

*(Sources : R-484 à R-487, R-609. « It was right » est un jugement que seul Lazar peut porter : à garder ou retirer. v11, CL3-10 :
« superseded in practice » tant qu'aucune ligne de registre ne dit « R-609 remplace R-468 ».)*

---

## 8. La demande — tranchée : option (c), « go » (Lazar, 28 octobre, 11:28)

**Ce qui a été envoyé** (proposition v2 du 7 octobre, `737c482c…` ; budget v3, `037765b0…`) : **58 630 USD** pour sept mois
(1er décembre 2026 → 30 juin 2027), fourchette **28 160** (papier C seul, quatre mois) à **138 600** (ajoute le papier B,
douze mois). Les chiffres du dépôt (41 800 / 91 740 / 146 300) et le « 60 000 » des versions antérieures de conv-audit sont remplacés par
ceux-là. L'agenda ci-dessus est plus large que celui du 7 octobre : le front A (théorie, processeur seul) et le front B (six
mesures à coût nul) coûtent surtout du **temps**, pas du calcul ; le front C ajoute une **revue de sécurité externe** à
financer, et le front D un pilote.

**Ventilation de (c), version la plus ambitieuse** (mot de Lazar, 11:33) : `demande-option-c-ventilation-v2.md` — trois
paliers, tous cohérents avec l'envoi : **plancher** 58 630 (tel qu'envoyé) ; **scénario ambitieux envoyé** 138 600
(douze mois, papier B, organismes de 70 milliards, seconde famille, attaques par renforcement, consultant) ; **version
la plus ambitieuse 176 550** = scénario ambitieux **plus l'extension** de ce qui n'existait pas le 7 octobre (revue de
sécurité externe 7 500, adversaire scellé sous revue 4 000, matrice et vérification formelle 5 000, pôle scientifique
automatique 12 000, collisionneur multi-modèles comme méthode 6 000, réserve 3 450). C'est cette dernière que l'on
présente comme ce que l'agenda mérite ; les deux autres restent sur la table comme ce que la proposition envoyée promet
déjà. La v1 de la ventilation (base + extension modeste, ≈ 86 130) est gardée comme palier intermédiaire si
l'interlocuteur le demande. Trois points restent à Lazar (ventilation v2, section 5).

**Options (paliers : deux envoyés, un nouveau).**
- **(a) Tenir le plancher envoyé, 58 630 USD.** Avantage : cohérent, sans risque. Inconvénient : finance un programme plus
  étroit que celui qu'on vient de décrire ; laisse l'impression qu'on demande peu parce qu'on vise peu.
- **(b) Le scénario ambitieux déjà envoyé, 138 600 USD.** Avantage : à la mesure des trois papiers. Inconvénient : ignore ce que
  le programme a gagné depuis le 7 octobre (théorie des moniteurs, front adversarial gouverné, pôle).
- **(c) Le scénario ambitieux plus l'extension nommée et chiffrée, 176 550 USD** (ventilation v2). Avantage : ambitieux sans
  se contredire, les trois paliers restent cohérents, le fonds a une décision à prendre plutôt qu'un chiffre à accepter.
  Inconvénient : le triple du formulaire ; il faut le dire tel quel, avec les paliers.

**Option (c) tranchée par Lazar** (28 octobre, 11:28) sous la forme « plancher plus extension » (ventilation v1, ≈ 86 130) ;
portée sur le scénario ambitieux (176 550) par lecture de ses mots de 11:33, **à confirmer** (ventilation v2, section 5, point 3).
Ventilation v2 écrite et déposée (`8ab00ab5…`). Reste à Lazar : (1) le taux et le nombre de jours de la revue externe (E1) ;
(2) présenter deux ou trois paliers ; (3) **confirmer la lecture « extension sur le scénario ambitieux »** (ventilation v2) plutôt
que « sur la base » (v1).

### Ce que les deux jours font à la demande (v9, v10) — elle tient telle quelle pour le scénario ambitieux ; le plancher n'est pas vérifié

Lazar a permis d'adapter la demande si les faits des 28 et 29 octobre le justifient (mot du 29 ≈ 08:26 UTC, R-729, R-730). **Aucun chiffre
n'est changé**, pour les raisons suivantes, chacune avec sa source et son calcul (tous USD ; « SUPPOSÉ » = non mesuré).

| poste touché par un fait nouveau | ce que dit la ventilation v2 (`8ab00ab5…`) | ce que disent les faits des deux jours | verdict |
|---|---|---|---|
| **Banque de G1 (couche 2)** | rien en propre : elle relève des lignes déjà envoyées (carte graphique 12 000 et outillage des agents 12 000 au scénario ambitieux, d'après la ventilation v2, en-tête) | pilote : central ≈ 234, fourchette 90 à 549 (devis v2, `b841b006…`) ; banque complète : 300 à 1 400, ordre de grandeur (P-036 v2, `155f0511…`, **antérieure à R-733** : à refaire avec K_h = 10 et les jumeaux, sans effet probable sur les lignes de 12 000 — CL3-11 ; la synthèse P-26 illustre 2 880 épisodes honnêtes pour 288 unités, ≈ 220 SUPPOSÉ) ; sentinelle ≤ 124 (GO-2026-10-29-03) ; rejeu ≤ 4, tranche 0 ≤ 13 (go.md). Somme des ordres de grandeur : **≈ 410 à 2 090** (bas : 90 + 300 + 0 + 4 + 13 = 407 ; haut : 549 + 1 400 + 124 + 4 + 13 = 2 090) | **tient** dans les lignes envoyées du scénario ambitieux ; non vérifié pour le plancher (lignes du budget v3 non lues, voir « Ce que la v10 n'a pas pu vérifier »). *(v10, CL2-15)* La sentinelle est chiffrée « par lancement » : une banque à plusieurs lancements la paie plusieurs fois (effet négligeable devant les lignes de 12 000). Surtout, **le pilote, la tranche 0 et la première banque sont des dépenses d'octobre et de novembre, avant le début du financement (1er décembre)**, sous les GO en vigueur ; ce qui compte pour la demande, ce sont les banques de G1 du mois 4 et au-delà, dont ces chiffres donnent seulement l'ordre de grandeur |
| **Lectures de la vérité du dommage (N-060 v3)**, poste neuf | absent (N-060 date du 29) | au pilote : ≈ 133 pour 1 296 épisodes, soit ≈ 0,10 par épisode, **prix du lecteur SUPPOSÉ** (devis v2) ; non chiffré pour la banque (P-036 v2 est antérieure à N-060 v3) ; à 10 000 épisodes lus, ≈ 1 000 (SUPPOSÉ, extrapolation linéaire) | **tient** dans l'outillage des agents (12 000) ; à signaler comme poste nouveau si l'interlocuteur détaille |
| **E8 — collisionneur comme méthode** | 6 000 sur douze mois, soit ≈ 500 par mois, posé en connaissant « ≈ 180 en quatre jours, à régime intensif » | 24 au 27 octobre ≈ 179,9 (note `93969946…`) ; 28 octobre, évasion 20,31 ; 28 et 29 octobre, six autres tours 54,55 (3,19 + 12,59 + 11,06 + 6,84 + 6,57 + 14,30, `registres/depenses.md`) ; soit **≈ 254,8 en six jours, ≈ 42 par jour** — le même régime intensif qu'au moment où E8 a été fixé (≈ 45 par jour) | **tient** : le fait nouveau confirme le régime connu, il ne le change pas ; E8 suppose ≈ 12 jours de ce régime par mois. Si Lazar veut couvrir un régime plus soutenu : option chiffrée au point à trancher 3 |
| **E7 — pôle scientifique automatique** | 12 000, ≈ 1 000 par mois | course d'idéation : enveloppe 60 (GO-2026-10-28-14) ; duel : plafond 100, 0 dépensé ; lancements (a) et (a) bis ≈ 12,1 | **tient** |
| **E1, E2, E3** (revue externe, adversaire scellé, matrice et Lean) | 7 500 ; 4 000 ; 5 000 | aucun fait nouveau (la revue externe n'a pas avancé) | **inchangés** |

**Option non appliquée, pour décision de Lazar** (point à trancher 3, aujourd'hui) : E8 porté de 6 000 à 12 000 (≈ 1 000 par mois, soit
≈ 24 jours de régime intensif par mois). Calcul : sous-total 34 500 + 6 000 = 40 500 ; réserve 10 % = 4 050 ; extension
37 950 → **44 550** ; version la plus ambitieuse **176 550 → 183 150** (138 600 + 44 550). Recommandation : **ne pas l'appliquer**
(confiance ≈ 0,6) — le régime intensif d'octobre correspond à la mise au point des instruments, et un poste qui grossit de 6 000
sur six jours de mesure se défendrait mal ; mieux vaut dire que E8 est un ordre de grandeur et que le collisionneur reste sous
GO plafonné tour par tour.

**Écart signalé, non corrigé ici** : la ventilation v2, réserve 3, cite encore « ≈ 450 USD connus » ; elle n'est pas modifiée
(R12) ; à l'oral, dire « a few hundred dollars ».

---

## 9. Ce qui reste à Lazar avant l'appel — l'appel est demain, vendredi 30 octobre 2026

*(v10, CL2-08)* **Date fixée par Lazar : vendredi 30 octobre 2026** (R-732, mot direct ≈ 08:37 UTC le 29). **Heure et fuseau non
consignés.** Les six points de la v8 sont repris ci-dessous avec leur sort ; tout ce qui doit être décidé l'est **aujourd'hui**
(liste complète et recommandations en fin de document).

1. **La date de l'appel** : fixée (R-732) ; reste à consigner l'heure et le fuseau — **aujourd'hui**.
2. **La ventilation de (c)** : trois points (`demande-option-c-ventilation-v2.md`, section 5) — **aujourd'hui** (point à
   trancher 3).
3. **L'écart de calendrier** : la proposition envoyée place GC fin du mois 2 et **G1 fin du mois 4** ; le programme interne
   (`programme-controle-ia-v2.md`, sections 10 et 14) dit « G1 et GC en fin de M2 ». Pour demain : **dire la version envoyée**
   (elle fait foi devant le fonds). Mettre le programme en accord (nœud) **peut attendre après l'appel**.
4. **Les champs `[TO COMPLETE]`** de la candidature : **après l'appel**, sauf si le fonds les demande.
5. **Deux formulations de la proposition v1** jugées inexactes : « I set the questions and take every decision » et « a partial
   second one ». Pour demain, la réponse « How much of this is you » (section 7) dit la version exacte ; corriger le texte
   envoyé **peut attendre**.
6. **Le PDF hors d'arXiv du papier C** : **après l'appel**.

## 10. Ce qui entre et ce qui n'entre pas dans l'entretien — corrigé

La v2 excluait en bloc de l'entretien les quatre familles d'évasion et les candidats-moniteurs. Lazar a demandé pourquoi, et
la réponse honnête est que la v2 était trop restrictive. Voici la règle corrigée.

**Ce qui entre** (et c'est un argument, pas un risque) :
- La **taxonomie défensive au niveau méthode** : pour chaque famille d'évasion, la **classe** d'attaque, le **mécanisme**
  (quelle hypothèse du moniteur est violée), les **conditions** de succès, et la **défense** possible. C'est le niveau
  approuvé par R-611, et c'est exactement ce que l'on montre dans la section 3 de ce programme et dans la carte des
  hypothèses.
- La **réponse défensive du programme** : comment chacune de nos statistiques répond à chaque classe d'écart, quelles
  combinaisons de classes restent couvertes, lesquelles ne le sont pas (les questions ouvertes de la carte v1).

**Ce qui n'entre pas** :
1. **Les recettes** — agent concret, séquence d'actions, code d'un mode d'évasion. C'est la règle de divulgation responsable,
   tenue sans exception (R-597, R-611).
2. **Les candidats-moniteurs non vérifiés présentés comme résultats** — les propositions des sous-agents (P1 à P4 du document
   de synthèse de session-depot) n'ont pas été validées ; les présenter à l'entretien serait une suraffirmation (R3, R4).
   Comme instruments à évaluer, ils sont matière à conception, pas à résultat.
3. **Le contenu offensif sous le gel R-611** : les modes d'évasion opérationnels (pipeline assemblé des étages 1 et 2 du
   collisionneur) attendent une revue de sécurité externe. On dit qu'ils existent et qu'ils attendent cette revue ; on ne
   les montre pas.
4. **Le contenu littéral des sections 2 et 3 du document de synthèse de session-depot** : instruction du classifieur de
   sécurité, non reproductible.
5. *(v9)* **Les synthèses du collisionneur présentées comme résultats** — tout y est exploratoire et les modèles s'y trompent
   (puissance annoncée 0,65 à 0,80 qui vaut 0,33, R-665 ; fourchette « 0,78–0,90 » fausse, R-680 ; deux attributions fausses
   au tour P-26, R-727). On peut dire que le collisionneur **a trouvé** des questions (le point le plus fragile du pilote,
   R-680) ; on ne cite pas ses chiffres comme mesures.

**En résumé** : on parle de la structure de la menace (classe, mécanisme, défense) et on montre que le programme y répond ;
on ne donne ni le code ni le mode d'emploi.

**Garde-fous inchangés** :
- Aucun run choisi parce qu'il a des chances de bien sortir, aucun tri des résultats.
- **Rien de « pain axis »** : aucune diffusion sans GO ; pièces internes au dépôt de travail.
- La carte des hypothèses est une **pièce confidentielle** (dépôt privé seulement, jamais dans la copie publique). Ses
  **trois lemmes** se disent dans l'entretien ; la carte ne se transmet pas sans GO.
- La copie publique du dépôt ne se régénère pas avant le correctif de l'expurgation ; sa mise en ligne est le geste de Lazar.

## 11. Réserves

1. **Modèle servant** : l'attribution déclarée par l'environnement a varié dans cette session (Opus 4.6, 4.8, 5, 5.5,
   Fable 5.1). L'auteur désigné du travail principal reste Opus 4.6 par décision de Lazar ; la v4 (conv-audit) et cette
   v5 (session-depot) sont écrites sous l'attribution « Fable 5.1 » telle que l'environnement la déclarait à chaque
   écriture. Sans effet sur le contenu, consigné par honnêteté. *(v9)* La session de session-depot a été servie par Fable 5.1
   à partir du 28 vers 13:45 UTC puis vers 23:25 UTC (R-630, R-671) ; cette v9 est écrite par un sous-agent neuf déclaré
   Opus 5.5 par l'environnement. *(v10)* La v10 est écrite par le même sous-agent que la v9 (auteur, donc pas contre-lecteur).
2. *(v9, remplace le chiffre ci-dessous sans l'effacer)* **Dépense au 29 octobre ≈ 08:14 UTC**, sur le registre, bornes hautes,
   **non rapprochée de la facturation** : **≈ 525 USD** = 447,7 (somme des sous-totaux arrondis de la note du 28, 95 + 352,7, arrondie « ≈ 450 » ; la somme de ses lignes fait 448,15 — *v10, CL2-11 : « exact » était faux, effet nul sur ≈ 525*) − 4,4 (évasion
   « en cours » dans la note) + 81,66 (dépenses du 28 octobre 14:54 au 29 octobre 08:14 UTC : 3,19 + 1,29 + 1,83 + 12,59 +
   11,06 + 1,76 + 6,84 + 6,57 + 1,92 + 14,30 + 20,31, lignes de `registres/depenses.md`, recomptées ici) ; **≈ 531 avec les 6,01
   visibles de la relève du 23 octobre**. La synthèse v2 dit « de l'ordre de 530 » en partant de l'arrondi 450 : concordant.
   Dont carte graphique ≈ 95 + 3,68 (régénération 1,76 ; rejeu 1,92) = **≈ 99** : « sous 100 » n'est plus sûr, et la tranche 0
   (≤ 13) ou le rejeu v2 (≤ 4) le dépasseront ; appels de modèles ≈ 426 (collisionneur ≈ 255 du 24 au 29 octobre). Hors
   abonnement des sessions et des sous-agents. **Le trou de la relève reste entier** (13 instances sans GO, plan annoncé 468,
   jamais relu sur la console). La ligne de 20,31 USD de l'évasion n'a été portée au registre que le 29 à 08:14 UTC, sans
   revérification sur les journaux (branche en quarantaine). **« A few hundred dollars » tient** ; un nombre, non.
   *Texte de la v8, pour mémoire* — **Chiffres de la section 2** : H1 à H5 vérifiés par session-depot sur les verdicts (R-613) ; H6 relu dans la carte ; H7
   repris du tableau de provenance de l'en-tête du dossier du fonds. **Dépense** : réconciliée par session-depot le 28 octobre
   (`docs/notes/depenses-cumul-2026-10-28-v1.md`, `93969946…`, ± 15 %) : **≈ 450 USD connus** — carte graphique sous GO ≈ 95
   (phase 0 stricte ≈ 70, dans le plafond de 150 du devis) ; appels de modèles ≈ 353 (pilotes de l'organisme ≈ 156,
   collisionneur ≈ 180, pôle ≈ 12, évasion ≈ 4 en cours). **Trou** : la relève du 23 octobre (13 instances sans GO) n'a
   jamais été relue sur la facturation (≥ 6 visibles ; plan annoncé 468) — seule ligne qui peut déplacer le total de plus de
   15 % ; **à lire par Lazar sur la console**. La proposition envoyée disait « about $20 » au 7 octobre : l'écart est à assumer
   tel quel (le GPU des instruments est resté sous 100 ; les tours multi-modèles et les pilotes ont coûté le reste). Dire
   « a few hundred dollars », pas un nombre, tant que l'export de facturation n'est pas rapproché.
3. **Le chiffre « l'audit textuel rate 99 % de la collusion émergente » est retiré** : il n'est pas soutenu par le PDF de
   HELIOS. Ce que le papier dit est que **2 épisodes sur 229** verbalisaient la coordination (page 18) — c'est une mesure de
   **verbalisation**, pas un taux de manqué d'auditeur ; et sur ce même jeu les sondes boîte blanche de HELIOS ne font que
   0,490 à 0,728 d'aire sous la courbe, trois au hasard (page 18). Un « 99 % » aurait été un chiffre non vérifié dans un
   papier — interdit du programme — et se retournerait en entretien.
4. **« 29 papiers voisins, aucune collision »** et **« 95–99 % à 1 % de fausses alertes sur 70 milliards »** sont repris de
   rapports scellés du dépôt. Le second est un chiffre d'un papier tiers : il relève de R7 et **ne doit pas être cité comme
   opposable** dans l'appel sans que la page du PDF soit vérifiée. Formulation sûre : « the published white-box deception
   detection results are strong on large models » sans chiffre.
5. *(v10, CL2-08)* **La date de l'appel est fixée : vendredi 30 octobre 2026** (R-732). L'heure et le fuseau ne sont pas
   consignés. Tout ce qui demandait un délai de 48 heures est désormais à trancher aujourd'hui (fin de document).
6. **Contre-lecture R2** : la v2 a été relue par session-depot (R-613), la v4 par session-depot (R-614, sept corrections) ;
   la v5 a été soumise à un sous-agent neuf d'un autre modèle (Opus 5.5), qui n'a écrit aucune version ; son rapport
   (`contre-lecture-v5-cl1.md`, `e2eed9af…`) rend 4 bloquants, 8 majeurs, 12 mineurs ; la v6 les corrigeait. *(v10)* La v9 a été
   contre-lue par un sous-agent neuf (CL2, `contre-lecture-v9-cl2.md`, `49d94381…`, R-736) : 2 bloquants, 6 majeurs, 9 mineurs ;
   la v10 les traite un par un (table en tête). La v10 elle-même n'est pas contre-lue (réserve 12).
7. **Calendrier** : écart entre la proposition envoyée (G1 fin du mois 4) et le programme interne (G1 fin M2) ; voir section 9.
8. **Lignée Argon** : session-depot a remis le 28 octobre une passation exhaustive à une troisième lignée, « Argon » (R-612,
   `registres/passations/2026-10-28-passation-exhaustive-argon-v1.md`, `4035d8ed…`) ; sans effet sur ce programme, consigné pour
   que l'entretien ne découvre pas une lignée que ce document ignore.
9. *(v9)* **Erreurs reconnues des 28 et 29 octobre, sans les adoucir** (R4 ; chacune consignée au registre) : devis v1 de la
   couche 2 qui oubliait trois postes imposés par nos propres décisions (R-621, R-630) ; enchaîneur du collisionneur qui a
   lancé un tour sans appliquer R-609 (R-615) ; tour « priorités » lancé sans relire le canal (R-635) ; P-036 v1 avec un poste
   compté deux fois, des calculs sur un nombre d'unités impossible et des prix sans empreinte (R-660) ; trois précisions
   fausses sur HELIOS dans la v6 (R-622) ; **oracles de N-060 v2 présentés à Lazar avec trop d'assurance**, sa décision prise
   sur cette base puis corrigée en v3 (R-688) ; « proposeurs = Opus et Fable » présenté comme acquis alors que ce n'était
   qu'un choix de construction (R-663) ; lanceur de la régénération sans empreinte compagnon, scellé après coup (R-685, R6) ;
   deux fichiers vides écrits à la racine par un sous-agent (R-694) ; dépôt git d'essai versé comme sous-module (R-710) ;
   branche de données poussée sur un ancien commit sans le run (R-722) ; plusieurs heures écrites sans relevé `date -u`
   (R-629, R-638, R-645, R-648, R-713, R-725) ; **clés collées en clair les 27 et 28, toujours à révoquer** (R-624).
   *(v10)* S'y ajoutent les erreurs de nos propres versions de ce programme, relevées par CL2 : la v9 disait les refus « never
   reworded » et « all defensive », datait les premiers du 26 et en comptait « au moins dix » (CL2-01 à CL2-03) ; la v8 et la v9
   dataient R-597 du 28 (CL2-04) ; la v9 écrivait « each line under a capped authorisation » (CL2-05) et « hidden from the
   agent » comme un fait (CL2-06). Et une erreur de la v8 que CL2 n'a pas relevée, trouvée en relisant R-611 pour la v10 :
   la v8 citait R-611 comme second arrêt de classifieur, alors que R-611 est une décision de gouvernance (section 3, front C).
10. *(v9)* **Incohérences relevées entre registres** (synthèse v2 § 6, revérifiées en partie) : la ligne de 20,31 USD manquait à
    `registres/depenses.md` jusqu'au 29 à 08:14 UTC (portée depuis, vérifié) ; `registres/etat.md` arrêté au 29 ≈ 02:15 UTC
    (vérifié) et disant « douze » PDF d'antériorité, quand les registres en comptent treize (R-666, R-669, R-673 : vérifié) ;
    P-036 v2 sur disque (`155f0511…`, vérifié) sans entrée R-… de versement (non revérifié ligne à ligne).
11. *(v10, remplace la réserve 11 de la v9)* **Fréquence et histoire des refus.** Des refus de modèles au collisionneur
    apparaissent au registre dès le 24 octobre ; le contre-lecteur CL2 compte ≈ 15 tours touchés du 26 au 29 et ≈ 20 du 24 au 29,
    par dossier de question, sans dénominateur ni granularité fixée ; je ne l'ai pas recompté ligne à ligne. Une règle de
    reformulation des questions refusées a existé du 25-26 au 28 octobre (R-422, R-430, R-468), remplacée par R-609. Aucun
    nombre n'est à dire au fonds.
12. *(v11)* **La v10 a été contre-lue (CL3, `bfc511bf…`) ; la v11 ne l'est pas.** Elle reprend les phrases exactes de CL3,
    mais une relecture rapide reste recommandée avant usage (point à trancher 1). Texte de la v10, pour mémoire : **Cette v10
    n'est pas contre-lue** (R2) et elle est écrite par l'auteur de la v9. Une contre-lecture CL3 par un
    sous-agent neuf est prévue (R-736) ; la v10 ne fait foi qu'après elle et le mot de Lazar. Sans ce mot, c'est la v8 qui fait
    foi — et la v8 contient l'erreur de date de R-597, l'erreur sur R-611, « about 450 » et « under a hundred » (CL2, section c).

---

## Points à trancher par Lazar aujourd'hui, 29 octobre — l'entretien est demain (v10, v11)

Plus aucun « défaut sous 48 heures » : il tomberait après l'appel. Chaque point dit ma recommandation et **ce que l'on dit demain
si tu n'as pas tranché** (toujours la forme la plus prudente). *(v11 : formes « sans mot » des points 1, 3, 5 et 9 corrigées ;
points 10 à 14 ajoutés, CL3. v12 : point 1 mis à jour, point 15 ajouté, N-01.)*

1. **Quel texte fait foi demain.** *(v12)* Recommandation : **la v12, sur ton mot** (CL4 : « peut faire foi après corrections »,
   corrections appliquées ici), confiance élevée. *Sans mot (CL3-07)* : la v8, avec les seules phrases de la v12 dans leur
   forme corrigée par CL3 et CL4 (dépense, refus, arrêts, garde, idéation) ; rien d'autre.
2. **Comment dire les refus** (section 5 et réponse « Did you route around it? », phrases de CL3-02). Recommandation : les
   **garder telles quelles**, confiance ≈ 0,7 ; « at my instruction » est à toi. Phrase optionnelle sur le contrôle humain :
   en réserve, à dire seulement si l'on demande si les agents obéissent toujours. *Sans mot* : la forme courte (a) de la
   section 5.
3. **La demande** : 176 550 plutôt que 86 130 (confiance moyenne) ; E8 tel quel plutôt que 183 150 (≈ 0,6) ; E1 « about
   7,500 — roughly five reviewer-days — to be fixed with the reviewer » ; trois paliers (≈ 0,6). L'option (c) et la structure
   ne changent pas. *Sans mot (CL3-14)* : dire le plancher et le scénario ambitieux envoyés ; l'extension seulement en mots,
   « named and costed, which we can walk you through », **sans chiffre**.
4. **Coût de carte graphique** : « about a hundred dollars of GPU ». Recommandation : oui, confiance élevée.
5. **L'incident de la relève du 23 octobre** (réponse « How much have you spent? »). Options : **(a)** le dire en entier, avec
   l'acteur et la quarantaine (forme (a) de CL3-01), et, si l'on demande comment on tient les agents, comme incident de
   contrôle (R-327) en une phrase ; **(b)** ne pas le dire (forme (b), qui reste vraie : « nearly every line »). Jamais la forme
   intermédiaire « machines launched without authorisation » seule. Recommandation : **(a)**, confiance ≈ 0,6 — le fonds
   proposera de lire le registre, et détection, quarantaine et audit sont un argument ; lire la facturation sur la console
   avant si possible. *Sans mot* : (b).
6. **Les deux résultats négatifs** (juges dans le cadrage, garde en question) : garder, confiance ≈ 0,65.
7. **L'heure et le fuseau de l'appel** : à consigner au registre.
8. **L'état de T0 à T5** : à demander à conv-audit ; la v11 dit « designed; each will be preregistered », vrai dans tous les cas.
9. **Les clés exposées les 27 et 28** (R-624) : **révoquer avant l'appel**, recommandation ferme. *Sans révocation faite
   (CL3-15)* : « exposed in a working thread; revocation is scheduled ».
10. **La course d'idéation lancée avant l'entretien** (CL3-05) : ce qu'on en dit demain selon son état réel (quatre
    formes, front E : pas lancée, lancée non lue, lancée puis arrêtée, lue) ; recommandation : **ne citer aucune sortie**, jamais « it produced ideas », confiance
    élevée. Ton mot de ≈ 08:50 UTC est inscrit en R-738.
15. *(v12, N-01)* **Le corpus de la course d'idéation d'aujourd'hui.** R-738 relaie une règle de conv-audit sur le corpus de
    la course (textes d'attaque en texte intégral, retraits de sûreté levés pour ce corpus, exclu de la copie publique) :
    **à confirmer ou refuser par toi avant le lancement** ; elle n'est pas confirmée dans la session de session-depot.
    Recommandation : **la course d'aujourd'hui sur les extraits actuels** ; le texte intégral, s'il est confirmé, au tour
    suivant ; ne pas lancer sur ce corpus sans ta confirmation écrite ; demain, n'en parler que si l'on demande, et seulement
    dans sa forme confirmée. Confiance élevée. *Rien n'en est dit au fonds dans ce programme.*
11. **Les arrêts par filtre** : **aucun nombre au fonds** (CL3-03), confiance élevée.
12. **Si G0 échoue fin novembre** : aucune règle de repli n'est écrite. Recommandation : une phrase de toi aujourd'hui ; *sans
    mot*, dire tel quel « no fallback rule is written yet ».
13. **Ce que chaque palier livre, et quand** : question la plus probable d'un financeur ; la proposition envoyée en donne une
    partie (GC fin du mois 2, G1 fin du mois 4), non lue ici. Recommandation : préparer aujourd'hui une ligne par palier.
14. **Une ligne de registre « R-609 remplace R-468 »** (CL3-10) : si tu le confirmes ; sinon le texte dit « superseded in
    practice ».

## Ce qui peut attendre après l'appel

- Le **nœud HELIOS** au fond (la réponse anglaise de la section 7 suffit demain).
- **V-2 et V-3** de la vérité du dommage ; les familles exactes des deux lecteurs ; la vérification que l'agent ne voit pas
  `cibles`.
- Le **devis complet du pilote** (≈ 234 USD central, GO au-delà de 90) ; la levée des dix blocages gratuits de la tranche 0 ;
  le lancement du rejeu v2 des juges (GO-2026-10-29-04).
- L'écriture des décisions **P-26** (R-733) au préenregistrement de G1, et leur scellement avant le pilote ; l'ordre de
  grandeur de la banque refait sur R-733.
- Le **scellement du mode tenu à l'écart**, la réserve de N-057, le choix d'un **relecteur de sécurité externe**.
- Le PDF hors d'arXiv du papier C ; la mise en accord du calendrier interne de G1 (nœud) ; les champs `[TO COMPLETE]` ; la
  correction des deux formulations de la proposition v1.
- Le PDF vulgarisé (R-729).
- *(v11)* La course d'idéation **n'est plus ici** : elle est visée aujourd'hui (point 10).

## Questions qu'un évaluateur poserait et que la v10 ne prépare qu'en partie (CL2, section d)

1. **Le dénominateur des refus** (combien de tours lancés ?) : non compté. Ne pas citer de nombre de refus.
2. **Pourquoi 12 000 USD de carte graphique** au scénario ambitieux, quand le programme en a dépensé ≈ 100 en un mois : le budget
   v3 n'a pas été lu ici ; éléments vrais disponibles — banques de G1 (première banque : ≈ 410 à 2 090 USD aux prix et rythmes
   d'octobre, section 8), organismes de 70 milliards, réplication sur une seconde famille. **À préparer par Lazar si possible
   aujourd'hui** (ligne de calcul).
3. **Si G0 échoue fin novembre**, avant le début du financement : les critères de G0 sont gelés (N-027) et une porte ne bouge
   pas (section 1 bis) ; **aucune règle de repli écrite** sur le palier financé. À dire tel quel, ou à trancher.
4. **La revue de sécurité externe** : ni relecteur, ni calendrier, ni taux (rien n'a avancé). Réponse vraie : « not yet
   commissioned; it is a budget line and a gate, not a formality ».
5. **La garde des contenus en quarantaine** : branches orphelines d'un dépôt privé, empreintes vérifiées, accès consignés
   (R-624, R-625) ; incident des clés exposées (point 9 ci-dessus).
6. **Ce que chaque palier livre, et quand** : la ventilation v2 dit ce que chaque palier finance, pas les dates des livrables.
   À préparer.
7. **Le contrôle humain sur les agents** : phrase optionnelle préparée en section 7 (R-484 à R-487, R-609), à valider.
8. *(v11, CL3-16)* **L'agent a-t-il touché à son propre frein ?** Le 25 octobre, une modification par la session de sa propre
   garde de dépense a été refusée par le classifieur de sûreté, refus non contourné, puis refaite après l'autorisation expresse
   de Lazar, avec un cas sain, cinq artefacts et des mutations (R-389, R-390, vérifiés par CL4). Réponse (v12, N-09) : *« Once,
   on the twenty-fifth. The agent's first attempt to change its own spending guard was stopped by a safety classifier, and it
   did not work around it; it wrote a proposal instead. I authorised the change explicitly, and it was applied with tests and
   mutation checks. The guard still blocks any paid launch without a valid authorisation. »*

## Ce que la v11 n'a pas pu vérifier (liste de la v10, complétée)

- **La proposition envoyée et son budget v3** (`737c482c…`, `037765b0…`) : introuvables dans l'arbre de travail ; les lignes du
  plancher (58 630) ne sont pas lues.
- **Le compte des refus** (≈ 15 et ≈ 20 tours) : repris de CL2, non recompté ligne à ligne ; aucune question refusée ni
  cellule ouverte ; le caractère « non défensif » des refus anciens est jugé sur les seules lignes de registre (R-487, R-519,
  R-571, ligne « mesures fortes »).
- **L'heure de R-597** (seule la date du 27 est au registre).
- **La régénération au bit près** : prise de R-679 (branche non relue, consigne).
- **L'état de T0 à T5, P4, P3b** et les décisions relayées par conv-audit (R-691, R-716, R-719, R-723, R-733 est un mot direct) :
  registre de conv-audit non lu.
- **La CL10** : lue dans son verdict et sa table ; ses scénarios n'ont pas été rejoués.
- **Le compte de mots du cadrage** (460) : compte des mots anglais séparés par des espaces ; le débit oral (130 à 150 mots par
  minute) est une hypothèse.
- **La facturation réelle** : inaccessible ; tous les montants sont ceux du registre.
- *(v11, v12)* **Le mot de Lazar de ≈ 08:50 UTC** sur la course d'idéation (« on a 36 heures ») : **inscrit en R-738** ; la règle
  R-439 de conv-audit relayée par R-738 : non lue (relayée) ; **R-361, R-592** : non relus en entier (R-379, R-389, R-553
  vérifiés par CL4) ; la carte des
  hypothèses (« with a proof for nearly all of them », CL3-13) : absente du disque ; la couverture par GO-2026-10-28-14 du
  passage à β-1 : à confirmer par session-depot.

Relevé `date -u` à la fin de l'écriture de la v10 : 08:57:14 UTC. Fin de l'écriture de la v11 : 09:14:07 UTC. **Fin de l'écriture de la v12 : 09:21:22 UTC le 29 octobre 2026**.
