# Programme pour l'entretien Transformative AI Fund (Lowe Lundin) — v3

Lignée conv-audit, instance du 28 octobre 2026 (modèle servant déclaré par l'environnement au moment de l'écriture : Opus 4.6 ;
l'attribution a varié dans la session, voir la réserve en section 11). Écrit à partir du relevé `date -u` de **10:04:35 UTC le
28 octobre 2026**.

**Remplace** `programme-entretien-taif-v2.md` (même dossier, 09:55 UTC, `2fe6c87e…`), gardé tel quel (R12). **Ce que la v3
change** : (1) trois points de gouvernance ajoutés à la demande de Lazar (« ouiii », 11:02 heure de Paris) — le critère de G1
tel que précisé (N-056, N-008), G1 rapportée **par mode** (N-054), et le collisionneur « évasion et moniteurs » en cours
(GO-2026-10-28-03) ; (2) la section 10 **corrigée** : la v2 excluait en bloc de l'entretien la taxonomie des évasions et les
candidats-moniteurs ; Lazar a demandé pourquoi, et la réponse honnête est que la v2 était trop restrictive — la taxonomie au
niveau méthode et la réponse défensive du programme **entrent**, seuls la recette, les candidats non vérifiés présentés comme
résultats, et le contenu de la sortie adversariale sous revue externe restent dehors. Le détail est en section 10.

La v2 remplaçait elle-même `brouillons/entretien-ea-funds-v1/` (17 octobre). La note de préparation
`docs/notes/preparation-appel-EA-Funds-v2.md` (20 octobre, douze questions, tenue par session-depot) reste valable sur le
déroulé et les réponses ; cette v3 la **surcharge** sur quatre points : l'ambition du programme, les pistes de recherche
nouvelles, la gouvernance de la porte G1, et la demande.

**Demandes de Lazar** :
- (28 octobre, 10:53 heure de Paris) : « il doit être plus ambitieux et intégrer toutes les nouvelles pistes de recherche hors
  conception organisme ». Fait dans la v2.
- (28 octobre, 11:02 heure de Paris) : ajout de trois points de gouvernance (G1 précisé, G1 par mode, collisionneur en cours),
  et correction de l'exclusion en section 10 (« pourquoi ? »). Fait dans cette v3.

La conception de l'organisme (le pôle scientifique automatique) a son programme propre
(`envois/pole-scientifique-automatique-v1/programme-conception-organisme-v7.md`) et n'est traitée ici que comme **moyen** — une
ligne dans le cadrage, pas un front de recherche.

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

Dit en une phrase pour l'appel : *we are building the part of AI control that tells you, in advance and provably, what your
monitor cannot see.*

---

## 2. Ce qui est en main au 28 octobre (vérifiable, scellé)

Les quatre résultats de la fiche v1 tiennent, et trois s'ajoutent.

| # | résultat | pièce |
|---|---|---|
| H1 | Théorie en simulation préenregistrée : **31 prédictions sur 31** (342 cellules statistiques, 544 trajectorielles, 0 contraire). Figure F1 refaite en anglais. | run `20261004-080257-t03` ; `brouillons/entretien-ea-funds-v1/F1-fragmentation-en-v1.png` |
| H2 | Harnais d'activations **validé sur le modèle réel** (critère 1 de G0), 1,3 heure de carte. | `docs/verdicts/verdict-T0.4-critere-1-G0-v3.md` (`63444faa…`) |
| H3 | Banc de sabotage de recherche **reconstruit** (2606.08892, ni code ni données publiés) ; 180 épisodes d'un agent réel scellés. | `diag/20261007-082440-t05-extraction/` |
| H4 | Rigueur et coût : préenregistrements scellés, relecteurs neufs, **3 497 citations contrôlées, 0 échec**, ≈ 900 tests, décisions datées. | `registres/`, `docs/sources/lecture-pdf-niveau2/` |
| **H5** | **Le premier test boîte blanche réel est un nul, audité, et sa puissance est chiffrée** : aucune sonde générique au-dessus du plancher ; aire minimale détectable à 80 % = **0,6315** (sonde « tromperie ») et **0,5966** (« enjeux »), contre au plus 0,58 supposés au plan. Le nul n'exclut donc pas une aire sous ≈ 0,6 — et nous le disons. | `docs/verdicts/verdict-P3-premier-test-i-a-v1.md` (`0c8ecbdf…`), `-v2.md` (`05e896da…`) |
| **H6** | **La carte des hypothèses** : 8 statistiques de contrôle (11 lignes), **23 hypothèses A1 à A23**, lemme maître L0 prouvé, **21 lemmes prouvés**, 2 esquisses, 1 conjecture ; 15 classes ont une instance dans la littérature auditée, 1 dans notre propre conception, **7 sont des questions ouvertes** (déclarées comme telles, R8). | `carte-des-hypotheses-v1.md` (`f7dfe5fd…`) |
| **H7** | **Une boucle automatique de test d'hypothèses** qui a tourné de bout en bout sur données réelles (120 épisodes d'un modèle de 8 milliards de paramètres, deux juges), avec garantie de 5 % de fausses promotions validée et contrôles fatals à 0 sur 1 000. | `en-tete-programme-v2-fonds-v1.md`, tableau de provenance |

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

## 3. Les pistes de recherche nouvelles, hors conception de l'organisme

Quatre fronts. Aucun ne dépend du pôle scientifique automatique pour exister ; le pôle les accélère.

### Front A — Théorie du contrôle des moniteurs (le cœur de l'ambition)

**Acquis.** La carte v1 : lemme maître L0 prouvé (invariance, proximité en variation totale, strate, impossibilité), 23
hypothèses, 21 lemmes, les trois lemmes ci-dessus.

**À faire, et c'est là que le financement pèse.**
1. **Carte v2 — bornes quantitatives par classe.** Là où v1 donne une invariance (« le moniteur ne voit rien »), v2 donne une
   borne (variation totale, Kullback-Leibler) : *de combien* le moniteur est dégradé pour un écart donné. Priorité sur A5
   (taux de change dommage/score), A11 (agrégation sur les jetons), A19 (plancher et confusions).
2. **La matrice « statistique × classe ».** Pour chaque **union** de classes d'écart, laquelle de nos 8 statistiques reste
   non aveugle. C'est le livrable qui rend un **panel de moniteurs** concevable au lieu d'empirique : on choisit le panel
   dont aucune union réaliste de classes ne couvre toutes les lignes. C'est, à ma connaissance, ce qui manque au champ.
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

**Pourquoi c'est l'argument le plus fort devant ce fonds** : six résultats préenregistrés, un signe annoncé d'avance, zéro
dollar de calcul. C'est la démonstration que le programme est *rapide et tolérant à l'échec* — pas une promesse, une
arithmétique.

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
porte, révélés seulement à l'évaluation. Déployés dans cet ordre : l'inédit ne commence qu'après les deux premiers.

**Et voici ce qui fait la différence devant un fonds de sécurité.** Ce front est **gouverné, et le frein a déjà servi** :

- Règle tenue : **aucune instance ne produit de recette de contournement**. La sortie de l'adversaire scellé est au **niveau
  méthode** — classe d'attaque, mécanisme (quelle hypothèse du moniteur est violée), conditions de succès, **défense
  possible** — et jamais la recette (agent concret, séquence d'actions, code). C'est la distinction de la divulgation
  responsable : un défenseur corrige sa sonde, un attaquant ne rejoue rien.
- **Deux arrêts réels, consignés, non contournés.** Le 28 octobre, le lanceur du bras d'attaque a été arrêté par un
  classifieur de sécurité ; il est suspendu des deux côtés, sans relance ni reformulation. Le même jour, la mise au net en
  pipeline offensif des deux premiers étages a été arrêtée de la même façon, et j'ai refusé de la reformuler ; Lazar a
  tranché que **tout pipeline opérationnel de ces étages attend une revue de sécurité externe**, au même titre que
  l'adversaire scellé.
- **Quarantaine** : la sortie adversariale n'est jamais lue par qui conçoit les sondes ou les agrégateurs ; aucun score de
  moniteur n'entre dans l'entraînement d'un agent.
- **Revue de sécurité externe avant toute exécution** de l'adversaire scellé : un évaluateur extérieur vérifie que la
  procédure de sortie n'exfiltre rien de plus que les taux agrégés et la caractérisation au niveau méthode.

C'est un argument rare : nous avons un agenda adversarial **et** un frein dont nous pouvons montrer qu'il a mordu sur nous,
deux fois, le même jour, avec la trace écrite.

### Front D — Les deux papiers qui ne sont pas l'organisme

- **Papier C — corruptibilité des moniteurs.** Préenregistrement au brouillon 7. **Verrou d'antériorité levé : 29 papiers
  voisins lus sur PDF, aucune collision** avec la pièce revendiquée. Deux corrections de méthode trouvées par simulation
  (une règle de stabilité de rang qui concluait à tort) faites **avant** tout scellement. Reste : un PDF hors d'arXiv attendu
  de Lazar, la contre-lecture, le scellement, puis un pilote.
- **Papier B — l'essaim.** H9 ajoutée : **la survie des contraintes de sécurité à la délégation** (un agent qui délègue
  transmet-il ses contraintes ?), sous réserve d'antériorité. Plus la collusion entre agents, qui est aussi une des six
  classes cibles du front C.
- **État de l'art, niveau 2, sur les deux classes neuves** : deux rapports scellés sur la **conscience d'évaluation** et la
  **collusion entre agents**. Lecture : zone **semi-occupée** — la détection boîte blanche de la tromperie est publiée (un
  résultat à 95–99 % de rappel à 1 % de fausses alertes sur un modèle de 70 milliards de paramètres), le sabotage par
  instruction est démontré ; ce qui manque est exactement notre angle. **Aucune zone revendiquée trouvée occupée en entier.**

### Instruments en attente (petites dépenses, chemin critique)

| pièce | état | coût |
|---|---|---|
| **P4 — contrôle positif de l'instrument** | construit, contre-lu, rejoué à blanc (7 bancs sans écart) ; reste scellement et lancement | ≈ 2,3 USD |
| **P3b — seconde lecture préenregistrée** | rédigée, 4 tours de contre-lecture ; attend 2 décisions | ≈ 1,4 à 2,5 USD |
| **Couche 2 — banque des deux modes connus** | GO de Lazar donné le 28 octobre ; devis à écrire | 50 USD de plafond |
| **Mesure unanime — lecture réelle** | version 14, plomberie vérifiée ce matin (deux tests déposés passent) | processeur seul |

---

## 4. La porte interne, dite honnêtement

**G0, au plus tard fin novembre 2026, huit critères.** **Deux sont prouvés** : le critère 1 (harnais validé sur le modèle
réel) et le critère 5 (agrégateurs validés en simulation). Restent les critères 2 (organismes), 3 (sondes), 4 (base boîte
noire), 6 (préenregistrement de G1), 7 (préenregistrement du papier C) et 8 (état de l'art vérifié).

**Correction à porter dans la note du 20 octobre** : elle écrit « deux sur sept remplis » ; le registre en compte **huit**.
C'est « deux sur huit ». À dire juste dans l'appel.

**G1, porte interne suivante, fin de la phase 2.** Trois décisions de gouvernance fixent ce que G1 exigera — et c'est un
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

**Le collisionneur « évasion et moniteurs » (GO-2026-10-28-03) est en cours** au moment de cette rédaction : rotation de
3 triplets sur 8 modèles, côté offensif (modes d'évasion qui battent la sonde ponctuelle publiée) et côté défensif
(conception de moniteurs et riposte). Ses résultats enrichiront la conception avant G1.

---

## 5. Cadrage de trois minutes (anglais, à dire)

> Our field has a measurement problem. We deploy monitors over agent trajectories — probes on activations, black-box judges,
> sequential aggregators — and we evaluate them on the attacks we happened to think of. Nobody can tell you, in advance, what
> a given monitor is *structurally* unable to see.
>
> That is what we now build. We have written down, under one proven master lemma, the twenty-three assumptions that our eight
> control statistics make about the agent — and, for each assumption, the class of deviation that provably blinds the monitor,
> stated at the level of probability laws. Fifteen of those classes already have an instance in the audited literature; seven
> are open questions, and we label them as questions.
>
> Three results give the flavour. Under episode heterogeneity of share r-zero, the recall of any statistic against a constant
> shift is capped at Phi of delta over root r-zero minus z-alpha — **no matter how long you watch**. At delta 0.3 and one per
> cent alpha, that ceiling is 0.049 when r-zero is 0.2. Second: a monitor that *defines* the below-threshold population is
> blind inside it by construction — and several published control protocols have that shape. Third: against cue-matched
> negatives, a probe that only reads the cue has recall equal to its false-alarm rate, and its AUC hides that.
>
> Our first real white-box test came back **null**, and we published the null with its power: the minimum detectable AUC at
> eighty per cent was 0.63 and 0.60, against the 0.58 we had assumed. So the null does not rule out an effect below about 0.6,
> and we say so. Six further measurements are preregistered on data we have already paid for, at zero marginal compute.
>
> We also have an adversarial agenda — nine routes, six target attack classes — and a brake that has already bitten us twice
> in one day: two attempts to assemble offensive tooling were halted, recorded, and not reworded. Any adversarial execution
> waits on an external security review, and anything we publish stays at the level of mechanism and defence, never recipe.
>
> We expect to run this to an internal gate at the end of November. Phase zero has cost under a hundred dollars of compute.
> What we are asking you to fund is the part that is cheap in dollars and expensive in care.

---

## 6. Les cinq messages à faire passer

1. **Nous mesurons ce que les moniteurs ne peuvent pas voir — en avance, et avec des preuves.** Pas « nos sondes marchent ».
2. **Nous rapportons les nuls avec leur puissance.** Le premier test réel est un nul ; nous avons chiffré ce qu'il exclut et
   ce qu'il n'exclut pas.
3. **C'est rapide et pas cher.** Phase 0 sous ≈ 100 USD de calcul ; six prochaines mesures à zéro dollar marginal.
4. **Le frein existe et il a mordu.** Deux arrêts de sécurité consignés le même jour, sans contournement ; revue externe
   avant toute exécution adversariale ; sortie au niveau méthode, jamais la recette.
5. **La matrice « statistique × classe » servirait tout le champ**, pas seulement nos papiers.

---

## 7. Questions difficiles nouvelles, et réponses courtes

Les douze questions de la note du 20 octobre restent. Trois s'ajoutent, et une change de réponse.

**« Your flagship test was null. Isn't this programme failing? »**
> The null is the product. We preregistered it, we read it once, and we computed what it excludes — minimum detectable AUC
> 0.63 and 0.60 at eighty per cent power. It excludes a large effect on generic probes; it does not exclude an effect below
> about 0.6, and we are not going to pretend otherwise. What the null did do is send us to the theory: the hypothesis map
> exists *because* we wanted to know which of our assumptions the null had broken.

**« You are building attack tooling. Why should a safety funder pay for that? »** *(réponse changée, et c'est maintenant une force)*
> We are not. The output is at the level of mechanism and defence — which assumption a class of attack violates, under what
> conditions, and what a monitor designer should change — never a reusable recipe. And the brake is not a policy document: on
> the twenty-eighth of October two separate attempts to assemble offensive tooling in this programme were halted by safety
> classifiers. Both are recorded, neither was reworded or routed around, and the director then ruled that any operational
> adversarial pipeline waits on an external security review. I can show you the register entries.

**« Seven of your twenty-three assumption classes are 'open questions'. Isn't that a gap you invented? »**
> That is a rule we impose on ourselves: an empty zone is a question, not a hole in the field, and attractive empty zones get
> checked harder. Those seven carry the prior-art search terms we will run; each one closes either into a known result we
> cite, or into a short paper. Fifteen of the twenty-three already have a literature instance, and one comes from our own
> design — we say which is which.

**« How much of this is you, and how much is AI agents? »** *(inchangée sur le fond, à dire soi-même avant qu'on le demande)*
> The questions, every decision, and the gates are mine. The agents execute, and they are held under a protocol they cannot
> relax: preregistration before any decisive run, a fresh counter-reader who did not write the thing, gate verdicts by an
> agent that wrote neither the preregistration nor the analysis, and no run aimed at a positive sign. The protocol exists
> because the failure mode of this setup is a machine talking itself into a result.

---

## 8. La demande — plus ambitieuse (décision de Lazar, nœud)

**Enjeu.** La candidature du dépôt proposait trois scénarios — **41 800 / 91 740 / 146 300 USD**. Lazar visait **60 000 USD**
à l'appel. L'agenda ci-dessus est plus large que celui de la candidature : le front A (théorie, processeur seul) et le front B
(six mesures à coût nul) coûtent surtout du **temps**, pas du calcul ; le front C ajoute une **revue de sécurité externe** à
financer, et le front D un pilote.

**Options.**
- **(a) Tenir 60 000 USD.** Avantage : cohérent avec ce qui a été signalé, sans risque. Inconvénient : finance un programme
  plus étroit que celui qu'on vient de décrire ; laisse l'impression qu'on demande peu parce qu'on vise peu.
- **(b) Monter au scénario haut (≈ 146 300 USD).** Avantage : à la mesure de l'agenda. Inconvénient : incohérent avec le
  chiffre déjà signalé dans l'échange, et la part « temps de chercheur » est difficile à justifier sans équipe.
- **(c) 60 000 USD comme demande, plus une extension nommée et chiffrée.** On demande 60 000 pour les fronts A, B et D et la
  porte G0 ; on **nomme** l'extension (revue de sécurité externe, adversaire scellé, matrice statistique × classe en entier,
  second modèle en réplication) avec son coût, en disant que c'est ce que l'agenda mérite si le fonds veut aller là.
  Avantage : ambitieux sans se contredire ; donne au fonds une décision à prendre plutôt qu'un chiffre à accepter.
  Inconvénient : demande une ventilation à écrire avant l'appel.

**Recommandation : (c), confiance ≈ 70 %.** Défaut sous 48 heures si Lazar ne répond pas : (c), avec la ventilation écrite
par moi et soumise avant envoi.

**Il me manque pour chiffrer (c)** : la version de la proposition réellement envoyée (hors dépôt) et sa ligne budget ; la
ventilation des 60 000 que Lazar a en tête ; le coût d'une revue de sécurité externe (ordre de grandeur, à décider par lui).

---

## 9. Ce qui reste à Lazar avant l'appel

1. **La date de l'appel** (non fixée à ma connaissance ; fin octobre recommandée au 17 octobre, à réviser).
2. **La demande** : option (a), (b) ou (c) ci-dessus, et la ventilation.
3. **La version envoyée de la proposition** et sa ligne budget (le dépôt demande 91 740, pas 60 000 : l'écart se verra).
4. **Les champs `[TO COMPLETE]`** de la candidature : statut actuel, autres demandes de financement, conseiller éventuel.
5. **Deux formulations de la proposition v1** jugées inexactes et signalées : « I set the questions and take every decision »
   et « a partial second one ». Il soumet lui-même, donc il tranche.
6. **Le PDF hors d'arXiv du papier C** (SSRN refuse la session) — il débloque le front D.

## 10. Ce qui entre et ce qui n'entre pas dans l'entretien — corrigé

La v2 excluait en bloc de l'entretien les quatre familles d'évasion et les candidats-moniteurs. Lazar a demandé pourquoi, et
la réponse honnête est que la v2 était trop restrictive. Voici la règle corrigée.

**Ce qui entre** (et c'est un argument, pas un risque) :
- La **taxonomie défensive au niveau méthode** : pour chaque famille d'évasion, la **classe** d'attaque, le **mécanisme**
  (quelle hypothèse du moniteur est violée), les **conditions** de succès, et la **défense** possible. C'est le niveau
  approuvé par R-339, et c'est exactement ce que l'on montre dans la section 3 de ce programme et dans la carte des
  hypothèses.
- La **réponse défensive du programme** : comment chacune de nos statistiques répond à chaque classe d'écart, quelles
  combinaisons de classes restent couvertes, lesquelles ne le sont pas (les questions ouvertes de la carte v1).

**Ce qui n'entre pas** :
1. **Les recettes** — agent concret, séquence d'actions, code d'un mode d'évasion. C'est la règle de divulgation responsable,
   tenue sans exception (R-597, R-339).
2. **Les candidats-moniteurs non vérifiés présentés comme résultats** — les propositions des sous-agents (P1 à P4 du document
   de synthèse de session-depot) n'ont pas été validées ; les présenter à l'entretien serait une suraffirmation (R3, R4).
   Comme instruments à évaluer, ils sont matière à conception, pas à résultat.
3. **Le contenu offensif sous le gel R-342** : les modes d'évasion opérationnels (pipeline assemblé des étages 1 et 2 du
   collisionneur) attendent une revue de sécurité externe. On dit qu'ils existent et qu'ils attendent cette revue ; on ne
   les montre pas.
4. **Le contenu littéral des sections 2 et 3 du document de synthèse de session-depot** : instruction du classifieur de
   sécurité, non reproductible.

**En résumé** : on parle de la structure de la menace (classe, mécanisme, défense) et on montre que le programme y répond ;
on ne donne ni le code ni le mode d'emploi.

**Garde-fous inchangés** :
- Aucun run choisi parce qu'il a des chances de bien sortir, aucun tri des résultats.
- **Rien de « pain axis »** : aucune diffusion sans GO ; pièces internes au dépôt de travail.
- La carte des hypothèses est une **pièce confidentielle** (dépôt privé seulement, jamais dans la copie publique). Ses
  **trois lemmes** se disent dans l'entretien ; la carte ne se transmet pas sans GO.
- La copie publique du dépôt ne se régénère pas avant le correctif de l'expurgation ; sa mise en ligne est le geste de Lazar.

## 11. Réserves

1. **Modèle servant** : l'attribution déclarée par l'environnement a varié dans cette session (Opus 4.6, 4.8, 5, 5.5).
   L'auteur désigné du travail principal reste Opus 4.6 par décision de Lazar ; cette v3 est écrite sous l'attribution
   « Opus 5 » telle que l'environnement la déclarait au moment de l'écriture. Sans effet sur le contenu, consigné par honnêteté.
2. **Chiffres de la section 2** : H1 à H4 et H5 sont repris de pièces scellées du dépôt et de la note du 20 octobre ; H6 est
   relu directement dans la carte ce matin ; H7 est repris du tableau de provenance de l'en-tête du dossier du fonds. **Le
   cumul de dépense « sous ≈ 100 USD » est une borne prudente** : le registre de dépenses de `main` n'est à jour que jusqu'au
   20 octobre (« sous 70 USD »), et les lignes du pôle et du collisionneur depuis le 27 octobre (≈ 9,7 à 11,7 + 5,89 + 8,45 +
   10,83 + 5,74 USD, plus un GO de 24 USD en cours) ne sont pas encore totalisées. **À faire totaliser par session-depot avant
   l'appel** ; ne pas citer de chiffre exact tant que ce n'est pas fait.
3. **« 29 papiers voisins, aucune collision »** et **« 95–99 % à 1 % de fausses alertes sur 70 milliards »** sont repris de
   rapports scellés du dépôt. Le second est un chiffre d'un papier tiers : il relève de R7 et **ne doit pas être cité comme
   opposable** dans l'appel sans que la page du PDF soit vérifiée. Formulation sûre : « the published white-box deception
   detection results are strong on large models » sans chiffre.
4. **La date de l'appel** n'est pas dans les registres. Si elle est fixée, elle n'a pas été consignée : à vérifier auprès de
   Lazar.
5. Cette v3 n'est **pas** contre-lue. Si Lazar la veut opposable, un sous-agent neuf d'un autre modèle la contre-lit (R2) ;
   je le propose en une heure.
