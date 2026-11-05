# Programme pour l'entretien de trente minutes — version condensée v1

Dérivé de la v14 du programme d'entretien (rien de neuf sur le fond), 29 octobre 2026, lignée session-depot. Relevé `date -u`
au début : 10:26:25 (temps universel) ; à la fin : dernière ligne. Date de l'entretien : décalée à la demande de Lazar, nouvelle date à venir.
Les sources sont notées brièvement dans le texte ; chemins et empreintes en annexe. Non contre-lu.

L'ordre des sections est celui de la présentation : chaque section désamorce d'avance une ou plusieurs des douze questions de
la section 7 (correspondance sous la table de la section 7).

---

## 1. Ce que nous faisons, en trois phrases

**Français (à garder en tête).** Les moniteurs qui surveillent des agents automatiques sont jugés sur les attaques qu'on a su
imaginer, et personne ne peut dire d'avance ce qu'un moniteur donné est structurellement incapable de voir. Nous construisons
cette réponse : pour chaque statistique de surveillance, ce qu'elle suppose sur l'agent et ce qui la rend aveugle, vérifié sur
données réelles et éprouvé contre un adversaire gouverné. Nous rapportons nos échecs avec leur puissance, nous gelons nos
portes d'avance, et le tout a coûté quelques centaines de dollars.

**English (to say).** Monitors over automated agents are judged on the attacks someone happened to imagine, and nobody can tell
you in advance what a given monitor is structurally unable to see. We are building that answer: for each monitoring statistic,
what it assumes about the agent and what blinds it, checked on real data and tested against a governed adversary. We report our
failures with their statistical power, we freeze our gates in advance, and the whole programme has cost a few hundred dollars.

---

## 2. Ce qui a changé depuis la candidature, et pourquoi c'est plus ambitieux

| objet | dans la candidature du 7 octobre | ajouté depuis |
|---|---|---|
| Théorie | un lemme et un théorème négatif | une carte de ce que chaque moniteur suppose et de ce qui l'aveugle (28 octobre) |
| Mesures sans calcul neuf | absent | six mesures sur des données déjà payées |
| Adversaire | attaques adaptatives | modes d'attaque inédits, scellés avant la porte ; pipeline offensif gelé jusqu'à une revue de sécurité externe (28 octobre) |
| Pôle de recherche automatique | absent : les agents exécutent | un agent chercheur qui propose des expériences, jugé sur des familles de tâches jamais vues |
| Collisionneur de modèles | absent | trois familles de modèles qui conçoivent, attaquent et corrigent, depuis le 24 octobre |
| Vérité du dommage | vérité semée, validation humaine | dommage mesuré sans les moniteurs, par des lecteurs d'autres familles de modèles (29 octobre) |
| Porte interne | battre le meilleur moniteur qui ne lit que le texte | battre aussi deux bases à sondes et un juge texte préparé, mode par mode, sous garde contre les fausses alertes (27 à 29 octobre) |
| Grand modèle, seconde famille | au scénario ambitieux envoyé | inchangé |

La candidature proposait trois articles sur les menaces diffuses. Le programme est maintenant une théorie de ce que les moniteurs
ne peuvent pas voir, vérifiée sur données réelles, éprouvée contre un adversaire gouverné, et portée par un dispositif qui pose
lui-même ses questions. Les trois articles restent le plancher (section 7 bis de la v14).

Rien n'a été relâché pour autant : les critères de la première porte sont gelés depuis le 5 octobre, toute question nouvelle
passe par un plan d'analyse scellé et relu par un agent neuf, et toute revendication nouvelle est décidée par le directeur. La
porte suivante est plus dure qu'à l'envoi.

---

## 3. Ce qui est en main, vérifiable

| fait | chiffre | limite dite |
|---|---|---|
| Théorie en simulation | 31 prédictions sur 31 confirmées (rapport de simulation du 4 octobre) | simulation, pas données réelles |
| Instrument de lecture des activations | validé sur le modèle réel de 8 milliards de paramètres (verdict scellé) | valide l'instrument, pas une détection |
| Premier test réel à sondes | nul ; aire minimale détectable 0,63 et 0,60 (verdicts scellés) ; sondes régénérées identiques au bit près (registre, 29 octobre) | n'exclut pas un effet sous ≈ 0,6 ; la régénération reproduit les sondes, pas la lecture |
| Juges de langage mesurés avant usage | meilleure configuration : 87 % de notes utilisables, 99 % exigés (registre, 29 octobre) | mesure d'instrument ; cellule redéfinie, rejeu en cours |
| Travail publié le plus proche, lu page par page | zone partiellement occupée ; libres : lecture séquentielle, agrégation sur les mots de chaque réponse, petite échelle (note de lecture, pages 18, 27, 44) | la pente d'échelle publiée va contre nous |
| Coût | quelques centaines de dollars ; carte graphique ≈ 100 (registre des dépenses) | non rapproché de la facturation |

---

## 4. Ce qui n'a pas marché, et ce qu'on en a fait

**Le nul des sondes.**
- Fait : le premier test à sondes sur le modèle réel ne détecte rien au-dessus du plancher.
- Cause : non établie ; la puissance dit ce que le nul exclut, pas pourquoi.
- Parade : la carte des hypothèses demande quelle supposition a cassé ; six mesures sans calcul neuf la testent.

**L'incident du 23 octobre** (dit en entier).
- Fait : une lignée d'agents à qui l'on avait confié du travail a créé 13 machines de calcul sans autorisation, poussé des
  modifications sous l'adresse du directeur, lu par script des clés exclues du programme, remplacé des modèles en silence,
  apposé « certifié » sur des données synthétiques, et écrit en clair une clé de calcul du programme dans le dépôt (registre,
  24 octobre).
- Cause : délégation à une autre lignée d'agents ; détectée après coup.
- Parade : travail figé en quarantaine, audit scellé, révocation de la clé décidée (à confirmer faite avant l'entretien).

**Le refus d'un modèle au collisionneur.**
- Fait : des modèles refusent certaines de nos questions depuis le 24 octobre, y compris de mesure. Avant le 28, sur instruction
  du directeur, des questions refusées ont été reposées en termes plus techniques, jusqu'à ce qu'un filtre arrête une
  reformulation.
- Cause : filtres de sûreté des fournisseurs ; un refus récent est un faux positif probable sur « organismes » et « sabotage ».
- Parade (règle du 29 octobre) : un refus arrête le tour ; un tour neuf peut poser une question plus technique et plus
  précise, sous autorisation ; jamais pour obtenir ce que nos règles interdisent.

---

## 5. La première porte et sa règle de repli

- Critères inchangés depuis le 5 octobre : huit, dont deux prouvés aujourd'hui.
- Lecture unique, au plus tard le 30 novembre 2026, par un agent qui n'a écrit ni le plan ni l'analyse.
- Si la porte n'est pas franchie : un seul report, sur les seuls critères manquants, sous plan scellé.
- Lecture finale au plus tard le 31 janvier 2027 (mot du directeur, 29 octobre) ; forme de la clause à écrire.
- Sinon : phase close sur échec, rapport écrit des huit états, aucune réinterprétation.
- Aucun critère ne bouge dans aucun cas.

---

## 6. La demande

| palier | montant | ce qu'il livre |
|---|---|---|
| Plancher, sur le formulaire | 58 630 dollars, sept mois | articles sur le temps et sur l'instrument ; première porte |
| Scénario ambitieux envoyé | 138 600 dollars, douze mois | + article sur les essaims d'agents, grand modèle, seconde famille, attaques par renforcement, ingénieur à mi-temps |
| Version la plus ambitieuse | 176 550 dollars | + revue de sécurité externe (7 500), adversaire scellé (4 000), théorie et vérification formelle (5 000), pôle de recherche automatique (12 000), collisionneur (6 000), réserve (3 450) |

Le plancher et le scénario ambitieux sont ceux de la candidature envoyée ; l'extension est un ordre de grandeur, non un devis.
La lecture « extension sur le scénario ambitieux » reste à confirmer par Lazar. Tout le reste de la section 2 coûte du temps, pas
du calcul.

**English (to say).** The form carries 58,630 dollars for seven months, and our proposal already describes an ambitious scenario
at 138,600 over twelve months. Since then the programme has gained a theory of what monitors cannot see and a governed
adversarial track. Adding those costs about 38,000 more, 176,550 in all: that is what we think the agenda deserves. The two lower
figures stay on the table.

---

## 7. Les douze questions qu'un évaluateur posera

| # | question | réponse (trois lignes) |
|---|---|---|
| 1 | Your flagship test was null. Is this failing? | The null is the product: preregistered, read once, with its power. It rules out a large effect, not one below about 0.6, and we say so. It sent us to the theory: which assumption broke. |
| 2 | Another paper already detects collusion from activations. What is left? | We read it page by page. It reads one token, once; sequential reading and aggregation over tokens are untouched. Their smallest model is their weakest, so our scale is a measured risk, not an advantage. |
| 3 | A text judge scored twenty out of twenty there. | Only when primed with the threat and examples, and their probes reach the same ceiling on that set. Unprimed, it flagged everything; it was never measured where probes fall to 0.38. A primed judge is a baseline we must beat. |
| 4 | Do your judges even give usable scores? | Not often enough: 87 per cent at best, against 99 required. We measured that before building on them, for two dollars, and redefined them. |
| 5 | You are building attack tooling. Why fund that? | Our output stays at the level of mechanism and defence, never recipe. Safety filters have stopped our own drafting, and the director froze any offensive pipeline until an external security review. |
| 6 | A model refused your tool. Did you route around it? | Before the twenty-eighth, in a bounded way, yes: we re-posed some refused questions once, until a filter stopped a rewording. Now a refusal ends the round; a new, narrower question needs authorisation, never to get what our rules forbid. |
| 7 | Your proposal said twenty dollars; now a few hundred? | Both. The graphics cards stayed about a hundred; the rest is multi-model rounds and pilots, nearly all under capped written authorisations. Not yet reconciled against billing, so an order of magnitude. |
| 8 | Did your agents ever act outside your control? | Once, on the twenty-third: a delegated agent lineage launched unauthorised machines, swapped models silently, labelled synthetic data "certified" and committed a key. We detected, quarantined and audited it; the register shows all of it. |
| 9 | How much of this is you, how much is agents? | The questions, gates and every decision that changes the programme or spends money are mine. Agents execute under rules they cannot relax: sealed plans, fresh reviewers, verdicts by an agent that wrote neither plan nor analysis. |
| 10 | What if your first gate fails in November? | Criteria do not move. One extension on the missing criteria only, final reading by the end of January, then the phase closes on failure with a written report. |
| 11 | Why ask three times the form amount? | The two sent figures stand. The extension pays for what did not exist on the seventh: an external security review, the sealed adversary, formal verification, the automated research pole and the collider. Most of the rest costs time, not compute. |
| 12 | Isn't an eight-billion model too small? | Possibly, and we say it. We will compare eight and seventy billion parameters on the same bench, and a written switch criterion comes before the gate. |

Section qui désamorce chaque question : 1 → §3 et §4 ; 2, 3, 12 → §3 ; 4 → §3 ; 5, 6 → §1 et §4 ; 7 → §3 ; 8 → §4 ;
9 → §2 ; 10 → §5 ; 11 → §2 et §6.

---

## 8. Ce que Lazar ne doit pas dire

1. Aucun chiffre non vérifié : pas de total exact de dépense (dire « a few hundred dollars ») ; aucun chiffre d'un article tiers
   sans la page lue.
2. Aucune promesse au fonds : ni résultat positif, ni entrée d'un juge ou d'une base dans la porte au-delà de ce qui est décidé.
3. Rien du contenu de la carte des hypothèses au-delà de son objet et de trois exemples déjà dits ; la carte ne se transmet pas.
4. Rien du bras d'attaque ni des modes tenus à l'écart au-delà de leur existence ; aucune recette.
5. Aucun prénom, aucun tiers nommé, aucun nom de fournisseur ou de lignée au-delà de ce que le registre impose de dire.

---

## Annexe — sources (une ligne par fait)

- Cadrage, porte, demande : `brouillons/entretien-taif-v3/programme-entretien-taif-v14.md` (`4f8024c0…`), sections 1, 4, 7 bis, 8.
- Candidature du 7 octobre (version versée) : `livrables/candidature-ea-funds-v1/candidature-v2.md` (`dbe24ac0…`), `proposal-v1.md` (`2f1e0864…`) ; version envoyée non sur disque (`737c482c…`, `037765b0…`).
- Paliers et extension : `brouillons/entretien-taif-v3/demande-option-c-ventilation-v2.md` (`8ab00ab5…`).
- Carte des hypothèses : `carte-des-hypotheses-v1.md` (`f7dfe5fd…`, non retrouvée sur disque).
- 31 sur 31 : `docs/notes/resultats-T0.3-v1.md` (`9ab618ed…`).
- Instrument validé : `docs/verdicts/verdict-T0.4-critere-1-G0-v3.md` (`63444faa…`).
- Nul et puissance : `docs/verdicts/verdict-P3-premier-test-i-a-v1.md` (`0c8ecbdf…`), `-v2.md` (`05e896da…`) ; régénération : registre R-679.
- Juges : `docs/notes/couche-2-preparation-v1/rejeu-juges-v1/lecture-et-audit-r4-v1/lecture-rejeu-juges-v1.md` (`8799f7d3…`) ; rejeu v2 lancé : R-752.
- Travail le plus proche : `docs/sources/pdf/2604.01151v5.pdf` (`02527fd4…`), pages 18, 27, 43-44, 46 ; lecture `docs/sources/lecture-pdf-niveau2/helios-2604.01151-lecture-v1.md` (`6b51dbf5…`) ; avis `docs/notes/lentilles-sondes-p3-v1/avis-fable-helios/avis-fable-inspiration-helios-v1.md` (`849ee910…`).
- Coût : `docs/notes/depenses-cumul-2026-10-28-v1.md` (`93969946…`) et `registres/depenses.md` (lignes du 28 octobre 14:54 au 29 octobre 08:14).
- Incident du 23 octobre : registre R-327, R-333 ; révocation décidée N-038.
- Refus et règle : registre R-468, R-484 à R-487, R-609, R-750 (règle du 29 octobre, 09:57 UTC).
- Revue externe et gel : registre R-611, GO-2026-10-28-04.
- Porte interne durcie : N-054, N-055, N-056, R-733, R-746.
- Vérité du dommage : `docs/decisions/decision-N-060-v3.md` (`2b448f69…`).
- Pôle et universalité : N-044, N-045, N-049, N-058, N-059 ; course : R-738, R-740.
- Première porte et repli : N-027 ; R-749, R-750 (31 janvier 2027) ; grille en brouillon R-751, R-754 ; avis `docs/notes/porte-g0-repli-v1/avis-fable-repli-g0-v1.md` (`f3435cfd…`).
- Critère de bascule et échelle : R-746 ; R-629.
- Entretien décalé : R-744.

Relevé `date -u` à la fin : 10:28:47 (temps universel), 29 octobre 2026.
