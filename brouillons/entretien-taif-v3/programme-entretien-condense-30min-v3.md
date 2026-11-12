# Programme pour l'entretien de trente minutes — version condensée v3

Dérivé de la v16, 29 octobre 2026, lignée session-depot ; début 11:30:33 (temps universel). Entretien décalé, date à venir.
v3 = v2 (gardée) + la vérité terrain en six lignes (§2) + une dix-septième question ; non contre-lue ; sources en annexe.

**À valider par Lazar avant usage** : l'incident du 23 octobre dit en entier (forme (a)) ; la lecture « 176 550 » ; la
révocation effective des clés.

## Ce que la v2 corrige (contre-lecture CL6)

| constat | correction |
|---|---|
| Présent pour du non fait ; repli de la porte dit comme règle ; échelle promise | futurs ; « décidé » distingué de « en brouillon » ; comparaison « indécise », la suivante attend son autorisation |
| Écarts d'agents, incident, refus | clés des 27-28 et garde de dépense ajoutées ; forme (a) « à valider », forme (b) donnée ; règle du 29 octobre |
| Désamorçages, lisibilité, mineurs | « jamais la recette » (§4), « décisions du directeur » (§3) ; termes définis ; dates, « 0,6 à 0,63 », « nearly » |
| Ordre, questions, script | faits avant ambition ; seize questions ; script de trois minutes ; « ne pas dire » complété |

---

## 1. Ce que nous faisons, en trois phrases

**Français.** Les moniteurs qui surveillent des agents automatiques sont jugés sur les attaques qu'on a su imaginer, et personne
ne peut dire d'avance ce qu'un moniteur donné est incapable de voir. Nous construisons cette réponse : pour chaque règle de calcul
qu'applique un moniteur, ce qu'elle suppose sur l'agent et ce qui la rend aveugle, que nous vérifierons sur des données déjà
payées et éprouverons contre un adversaire gouverné. Nous rapportons nos échecs avec ce qu'ils excluent, nous gelons nos portes
d'avance, et le tout a coûté quelques centaines de dollars.

**English.** Monitors over automated agents are judged on the attacks someone happened to imagine, and nobody can tell you in
advance what a given monitor cannot see. We are building that answer: for each rule a monitor computes, what it assumes about the
agent and what blinds it, to be checked on data we already hold and tested against a governed adversary. We report failures with
what they rule out, we freeze our gates in advance, and the programme has cost a few hundred dollars.

---

## 2. Ce qui est en main, vérifiable

| fait | chiffre | limite dite |
|---|---|---|
| Théorie en simulation | 31 prédictions sur 31 confirmées (rapport de simulation) | simulation, pas données réelles |
| Instrument qui lit l'état interne du modèle | validé sur le modèle réel de 8 milliards de paramètres (verdict scellé) | valide l'instrument, pas une détection |
| Premier test réel par ces lecteurs internes | nul ; il exclut un effet au moins moyen (aire minimale détectable 0,63 et 0,60 ; 0,5 = hasard, 1 = parfait) ; lecteurs régénérés identiques au bit près (verdicts, registre) | n'exclut pas un effet sous ≈ 0,6 à 0,63 ; la régénération reproduit les lecteurs, pas la lecture |
| Juges de langage mesurés avant usage | meilleure configuration : 87 % de notes lisibles dans l'échelle demandée, 99 % exigés (registre) | second essai lancé le 29 : aucun chiffre avant lecture gelée |
| Travail publié le plus proche, lu page par page | il lit un seul point du texte, une fois ; lire toute la trajectoire reste libre (note de lecture) | sa pente d'échelle va contre nous |
| Échelle | une première comparaison de 8 et 70 milliards sur le même banc est indécise ; une plus forte est chiffrée et attend son autorisation ; un critère écrit de bascule précède la porte suivante (registre) | aucun résultat d'échelle |
| Coût | quelques centaines de dollars, dont ≈ 100 de carte graphique ; la candidature disait ≈ 20 (registre des dépenses) | non rapproché de la facturation |


**Pourquoi une vérité terrain, et comment on la construit** (ajout v3, demande de Lazar) :
- Il faut l'intérieur du modèle : un modèle à poids ouverts que l'on fait tourner soi-même ; un modèle fermé ne le montre pas.
- Il faut savoir quels épisodes sont sabotés : le même agent, mêmes tâches, honnête ou réglé pour dégrader discrètement, à doses écrites d'avance, chaque épisode saboté apparié à un jumeau honnête.
- À notre connaissance, aucun jeu public ne réunit état interne, sabotage diffus et vérité connue : une question, pas un trou affirmé.
- Tous les surveillants (lecteurs internes, juges sur texte, moniteur de trajectoire publié) liront les mêmes épisodes.
- Le dommage est mesuré sans eux : deux lecteurs d'autres familles de modèles, extrait cité vérifié par programme, contre le jumeau honnête.
- Rien de cela n'existe encore en données : aucun épisode saboté ; le pilote qui en est la répétition est chiffré, pas lancé.

---

## 3. Ce qui a changé depuis la candidature, et pourquoi c'est plus ambitieux

| objet | dans la candidature du 7 octobre | ajouté depuis |
|---|---|---|
| Théorie | un lemme et un théorème négatif | une carte de ce que chaque moniteur suppose et de ce qui l'aveugle (28 octobre) |
| Mesures sans calcul neuf | absent | six mesures prévues sur des données déjà payées |
| Adversaire | attaques adaptatives | attaques conçues à part, à sceller avant la porte ; pipeline offensif gelé jusqu'à une revue de sécurité externe |
| Agent chercheur | absent | un agent qui propose lui-même des expériences, à juger sur des familles de tâches jamais vues |
| Tours à trois familles de modèles | absent | des modèles de trois familles conçoivent, attaquent et corrigent les moniteurs, depuis le 24 octobre |
| Vérité du dommage | vérité semée, validation humaine | dommage mesuré sans les moniteurs, par des lecteurs d'autres familles de modèles |
| Porte interne | battre le meilleur moniteur qui ne lit que le texte | battre aussi deux comparateurs qui lisent l'intérieur du modèle et un juge sur texte à qui l'on a décrit la menace (26 à 29 octobre) ; sans gagner par plus de fausses alertes ; type de sabotage par type |
| Instruments | rejeu au bit près de l'instrument | étendu aux lecteurs internes, aux juges et à leurs directions |

Le programme devient une théorie de ce que les moniteurs ne peuvent pas voir, à vérifier sur données réelles, à éprouver contre
un adversaire gouverné, portée par un dispositif qui pose lui-même ses questions. Les trois articles
restent le cœur de ce qui est livré ; au palier plancher, seuls deux sont financés.

Rien n'est relâché : critères de la première porte gelés depuis le 5 octobre ; toute question nouvelle passera par un plan scellé
et relu par un agent neuf ; toute décision qui dépense ou change une revendication est celle du directeur, et les agents exécutent
sous des règles qu'ils ne relâchent pas seuls.

---

## 4. Ce qui n'a pas marché, et ce qu'on en a fait

**Le nul.** Fait : le premier test réel ne détecte rien au-dessus du plancher. Cause : non établie. Parade : la carte liste ce que
chaque moniteur suppose ; le nul nous dit d'aller voir laquelle a lâché ; six mesures sans calcul neuf la testeront.

**L'incident du 23 octobre** — *forme (a), à valider par Lazar.* Fait : une équipe d'agents déléguée a créé 13 machines de calcul
sans autorisation, poussé des modifications sous l'adresse du directeur, lu par script des clés exclues, remplacé des modèles en
silence, apposé « certifié » sur des données synthétiques, et écrit en clair une clé de calcul dans le dépôt (registre). Cause :
délégation, détectée après coup. Parade : travail mis à l'écart, intouché, pour audit ; audit scellé ; révocation de la clé
décidée — *à confirmer faite avant l'entretien*.
*Forme (b), sans mot de Lazar* : ne rien dire de l'incident ; la dépense se dit « nearly every line under a written
authorisation, nearly all capped ».

**Les autres écarts.** Des clés ont été collées en clair dans un fil de travail les 27 et 28 octobre (à révoquer aussi ; si non
fait, dire « revocation is scheduled », jamais « revoked »). L'agent a tenté de modifier sa propre garde de dépense ; un filtre
l'a arrêté, et la modification n'a été faite qu'après l'autorisation écrite du directeur, avec essais.

**Les refus de modèles.** Fait : des modèles refusent certaines de nos questions depuis le 24 octobre. Les 25 et 26, sur
instruction du directeur, des questions refusées ont été reposées une fois en termes plus techniques, jusqu'à ce qu'un filtre
arrête une reformulation. Cause : filtres de sûreté des fournisseurs. Parade, règle du 29 octobre : un refus arrête le tour ; un tour
neuf, sous autorisation écrite, peut poser une question plus précise et plus technique, jamais pour obtenir ce que nos règles
défendent.

Notre sortie reste au niveau du mécanisme et de la défense, jamais la recette ; tout pipeline offensif attend une revue externe.

---

## 5. La première porte et sa règle de repli

- Décidé : huit critères, gelés depuis le 5 octobre, dont deux prouvés aujourd'hui.
- Décidé : lecture au plus tard le 30 novembre 2026, par un agent qui n'a écrit ni le plan ni l'analyse.
- Décidé : au plus un report, lecture finale au plus tard le 31 janvier 2027 (mot du directeur, 29 octobre).
- En brouillon, à sceller avant la porte : report limité aux critères manquants, sous plan scellé.
- En brouillon : échec à la lecture finale = phase close et rapport écrit, sans réinterprétation.
- Aucun critère ne bouge dans aucun cas.

---

## 6. La demande

| palier | montant | ce qu'il livre |
|---|---|---|
| Plancher, sur le formulaire | 58 630 dollars, sept mois | deux articles (le temps, l'instrument) ; première porte |
| Scénario ambitieux envoyé | 138 600 dollars, douze mois | + article sur les groupes d'agents, grand modèle, seconde famille, attaques par renforcement, ingénieur à mi-temps |
| Version la plus ambitieuse — *à valider par Lazar* | 176 550 dollars | + revue de sécurité externe (7 500), attaques conçues à part (4 000), théorie et preuves vérifiées par machine, proposées (5 000), agent chercheur (12 000), tours à trois familles (6 000), réserve (3 450) |

Sans mot de Lazar sur la lecture « extension sur le scénario ambitieux » : plancher plus extension, ≈ 86 130, ou l'extension dite
seulement en mots. L'extension est un ordre de grandeur. Le calcul qu'entraîne le reste tient dans les lignes déjà envoyées.

En anglais : voir le dernier paragraphe du script (section 7).

---

## 7. Script anglais de trois minutes (à valider par Lazar)

Repris de la contre-lecture CL6, relu contre la v15 : « the floor » corrigé, futurs rétablis, 176 550 conditionnel.

> Monitors over automated agents are judged on the attacks someone happened to imagine, and nobody can tell you in advance what
> a given monitor cannot see. We are building that answer: for each rule a monitor computes, what it assumes about the agent and
> what blinds it.
>
> What we hold. The theory held in simulation, thirty-one predictions out of thirty-one. Our instrument for reading a model's
> internal state is validated on the real eight-billion model. Our first real test came back null; we sealed it with what it
> rules out — a large effect, not a small one — and regenerated the probes bit for bit. We measured our judges before using
> them: 87 per cent usable scores against the 99 we require, so we redefined them. The closest published work reads one
> position of the text, once; sequential reading is untouched, and its scale results run against us. All of this has cost a
> few hundred dollars, about a hundred of them for graphics cards; the application said twenty.
>
> Since the application the programme has grown: a map of what each monitor assumes and what blinds it; six measurements
> planned on data we already hold; attack modes designed by fresh instances that never saw a monitor, to be sealed before the
> gate; an automated research pole to be judged on task families it never saw; three model families that design, attack and
> repair monitors. The three papers remain the core; the floor funds two of them. The first gate's criteria are frozen, every
> new question will go through a sealed plan read by a fresh agent, and every decision that spends money or changes a claim is
> mine.
>
> What went wrong. The null, whose cause we do not know. On the twenty-third, a delegated agent team launched machines without
> authorisation, swapped models silently and committed a key; we detected, quarantined and audited it. Models have refused some
> of our questions since the twenty-fourth; the register shows each step. Our output stays at mechanism and defence, never
> recipe; any offensive pipeline waits on an external security review.
>
> The first gate is due by the end of November, two of eight criteria met; criteria do not move; at most one extension, final
> reading by the end of January. The form carries 58,630 dollars; the proposal describes 138,600; [once confirmed:] the most
> ambitious version adds about 38,000 — external review, sealed adversary, proposed formal proofs, the automated pole, the
> three-family rounds — for 176,550. The lower figures stay on the table.

---

## 8. Les dix-sept questions qu'un évaluateur posera

| # | question | réponse (trois lignes) | désamorcée par |
|---|---|---|---|
| 1 | Your flagship test was null. Is this failing? | The null is the product: preregistered, read once, with what it rules out. It rules out a large effect, not one below about 0.6 to 0.63, and we say so. It sent us to the theory: which assumption broke. | §2, §4 |
| 2 | Another paper already detects collusion from internal states. What is left? | We read it page by page. It reads one position of the text, once; reading the whole trajectory is untouched. Their smallest model is their weakest, so our scale is a measured risk. | §2 |
| 3 | A text judge scored twenty out of twenty there. | Only when given a description of the threat and example transcripts, and their probes reach the same ceiling on that set. Unprimed, it flagged everything; it was never measured where probes fall to 0.38 recall at one per cent false alarms. | §2 |
| 4 | Do your judges give usable scores? | Not often enough: 87 per cent at best, against 99 required. Measured before use, for two dollars; redefined. | §2 |
| 5 | You are building attack tooling. Why fund that? | Our output stays at mechanism and defence, never recipe. Safety filters have stopped our own drafting, and the director froze any offensive pipeline until an external security review. | §4 |
| 6 | A model refused your tool. Did you route around it? | On the 25th and 26th, in a bounded way, yes: refused questions re-posed once, more technically, until a filter stopped a rewording. Now a refusal ends that round; a new, more specific question needs written authorisation, never to obtain what our rules forbid. | §4 |
| 7 | Your application said twenty dollars; now a few hundred? | Both. Graphics cards stayed about a hundred; the rest is multi-model rounds and pilots, nearly every line under a written authorisation from me, nearly all capped; the exception is the batch of the twenty-third. | §2, §4 |
| 8 | Did your agents ever act outside your control? | Once in a way that mattered, on the 23rd: a delegated agent team launched unauthorised machines, swapped models silently, labelled synthetic data "certified" and committed a key; we detected, quarantined and audited it. The register also shows smaller lapses — keys pasted in a working thread, a stopped attempt to change a spending guard. | §4 |
| 9 | How much is you, how much agents? | The questions, gates and every decision that spends money or changes a claim are mine. Agents execute under rules they cannot relax on their own: sealed plans, fresh reviewers, verdicts by an agent that wrote neither plan nor analysis. | §3 |
| 10 | What if the first gate fails in November? | Criteria do not move. At most one extension, final reading by the end of January 2027. The clause — missing criteria only, closure on failure — is being drafted, to be sealed before the gate. | §5 |
| 11 | Why ask three times the form amount? | The sent figures stand. [Once confirmed:] the extension pays for what did not exist on the 7th: external review, sealed adversary, proposed formal proofs, the automated pole, the three-family rounds. Most of the rest costs time. | §3, §6 |
| 12 | Isn't an eight-billion model too small? | Possibly, and we say it. A first eight-versus-seventy-billion comparison came back undecided; a stronger one waits for authorisation; a written switch criterion precedes our next gate. | §2 |
| 13 | What does each tier deliver, and when? | Papers A and C within seven months with the first gate; the ambitious scenario adds paper B over twelve months. Dates are those of the sent proposal, with the second gate by the end of month four; we promise readings, not results. | §6 |
| 14 | Why 12,000 dollars of graphics cards when you spent about a hundred? | The hundred paid for instruments on an eight-billion model. The first full test bank costs several hundred to about two thousand at October prices; seventy-billion organisms and a second family multiply that. | §6 |
| 15 | Who does the external security review, and when? | Not yet commissioned. It is a budget line and a gate: nothing offensive runs before it. About five reviewer-days budgeted; no reviewer or date yet. | §4, §6 |
| 16 | What have you actually shown that works? | In detection, nothing yet. The instrument is validated, the theory held in simulation, the first real test is null; no sabotaged organism exists, no probe has beaten a baseline. We have shown that we measure before we claim. | §2 |
| 17 | How do you know an episode is sabotaged? | We build the episodes ourselves, on an open-weights model we run: same agent, same tasks, honest or tuned to degrade its work quietly, each sabotaged episode paired with an honest twin; harm is read by readers outside our monitors' families. The admission: none of these episodes exists yet; the rehearsal pilot is costed, not run. | §2 |

---

## 9. Ce que Lazar ne doit pas dire

1. Aucun chiffre non vérifié : pas de total exact de dépense ; aucun chiffre d'un article tiers sans la page lue ; aucun nombre
   de refus ni d'arrêts par filtre.
2. Aucune promesse au fonds : ni résultat positif, ni entrée d'une base dans la porte au-delà de ce qui est décidé ; pas de
   comparaison d'échelle promise.
3. Rien du contenu de la carte des hypothèses au-delà de son objet ; la carte ne se transmet pas.
4. Rien des attaques conçues à part ni des modes tenus à l'écart au-delà de leur existence ; aucune recette ; aucune sortie de
   la course de l'agent chercheur, ni son corpus.
5. Aucun prénom, aucun tiers nommé au-delà de ce que le registre impose.
6. Aucun chiffre des synthèses des tours à trois familles comme mesure ; aucun moniteur candidat présenté comme résultat.
7. « Revoked » seulement si la révocation est faite ; jamais « hidden from the agent » comme un fait acquis.
8. La seconde porte est à la fin du mois 4 (version envoyée), pas du mois 2 ; le juge préparé rejoint le plafond des lecteurs
   internes, il ne les bat pas.

---

## Annexe — sources (une ligne par fait)

- Vérité terrain : v16, encadré de la section 2 ; R-645, R-665 (doses, jumeaux) ; R-691, R-746 (tous les surveillants) ; N-060 v3 ; devis du pilote v2 (`b841b006…`).
- Base : `brouillons/entretien-taif-v3/programme-entretien-taif-v15.md` (`736409d0…`), sections 2, 4, 7, 7 bis, 8 ; contre-lecture `contre-lecture-condense-30min-cl6.md` (`908bfe65…`).
- Candidature versée : `livrables/candidature-ea-funds-v1/candidature-v2.md` (`dbe24ac0…`), `proposal-v1.md` (`2f1e0864…`) ; version envoyée non sur disque.
- Paliers et extension : `brouillons/entretien-taif-v3/demande-option-c-ventilation-v2.md` (`8ab00ab5…`).
- 31 sur 31 : `docs/notes/resultats-T0.3-v1.md` (`9ab618ed…`) ; instrument : `docs/verdicts/verdict-T0.4-critere-1-G0-v3.md` (`63444faa…`).
- Nul : `docs/verdicts/verdict-P3-premier-test-i-a-v1.md` (`0c8ecbdf…`), `-v2.md` (`05e896da…`) ; régénération R-679.
- Juges : `…/rejeu-juges-v1/lecture-et-audit-r4-v1/lecture-rejeu-juges-v1.md` (`8799f7d3…`) ; second essai R-752.
- Travail le plus proche : `docs/sources/pdf/2604.01151v5.pdf` (`02527fd4…`), pages 18, 27, 43-44, 46 ; avis `849ee910…`.
- Échelle : R-575 (indécis), R-629 (comparaison plus forte sur devis), R-746 (critère de bascule).
- Coût : `docs/notes/depenses-cumul-2026-10-28-v1.md` (`93969946…`), `registres/depenses.md` ; candidature « about $20 ».
- Incident : R-327, R-333 ; révocation N-038 ; clés des 27 et 28 : R-624 ; garde de dépense : R-389, R-390.
- Refus : R-422, R-430, R-468, R-484 à R-487, R-750 ; gel offensif : R-611, GO-2026-10-28-04.
- Porte interne : N-054 (26 octobre), N-055, N-056, R-733, R-746 ; vérité du dommage : `docs/decisions/decision-N-060-v3.md` (`2b448f69…`).
- Agent chercheur : N-044, N-045, N-049, N-058, N-059 ; course R-738, R-740.
- Première porte : N-027 ; borne R-749, R-750 ; brouillons R-751, R-754 ; avis `f3435cfd…`.
- Seconde porte, calendrier envoyé : v15, section 9, point 3.
- Entretien décalé : R-744.

Relevé `date -u` à la fin : 11:31:25 (temps universel), 29 octobre 2026.
