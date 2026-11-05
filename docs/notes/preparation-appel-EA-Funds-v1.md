# Préparation de l'appel EA Funds (Transformative AI Fund) — v1

Session 14, 2026-10-20 vers 10:45 UTC (R-271). Demande de Lazar : « un doc de préparation, toutes les questions pouvant
tomber, leurs réponses rédigées, les tips, les points essentiels à maîtriser, les questions les plus importantes et
probables ». Pour Lazar seul ; rien n'est envoyé (contact externe : Lazar décide et parle).

**Comment lire ce document.**
- Structure et conseils en français. Les réponses à dire sont **en anglais**, prêtes à l'oral : 60 à 90 secondes chacune.
- Matériaux de départ :
  - les réponses de Gemini aux requêtes 012 et 013, avec sa recherche web ;
  - le squelette de la présentation (R-267) ;
  - la fiche d'entretien de la session 15 (R-191).
- **Chaque fait du programme a été revérifié dans le dépôt** (chemins et empreintes en section 9).
- Gemini avait fait **neuf erreurs** ; elles sont corrigées ici et listées en section 8. Ne reprends pas sa réponse brute.
- `[À TOI : …]` marque ce que toi seul sais : budget envoyé, durée, autres financeurs, relecteurs humains, parcours.
  Tout ce qui touche le budget doit coller **mot pour mot** à ce que tu as envoyé.
- « à vérifier » marque un chiffre ou un nom de la littérature non relu sur le PDF (R7) : ne le cite pas comme un fait.

---

## 1. L'essentiel sur une page

**Le fonds** (pages officielles lues le 2026-10-20 ; section 9) :
- Le Long-Term Future Fund est **fermé**. EA Funds a lancé à sa place le **Transformative AI Fund**.
- Équipe :
  - Lowe Lundin, Head of Fund : c'est lui qui t'a proposé l'appel (R-191) ;
  - deux conseillers, Caleb Parikh (ancien responsable du Long-Term Future Fund) et Catherine Low (Centre for Effective Altruism) ;
  - Loïc Watine, directeur d'EA Funds depuis janvier 2026 ;
  - un « Associate Program Officer » était en recrutement au lancement.
- Ce qu'ils disent chercher :
  - leurs mots : *« early-stage, fast, and tolerant of failure »* ;
  - les subventions vont *« typically in the $10k–$150k range »*, et les individus sont éligibles ;
  - ils acceptent des gains en loi de puissance : *« most of these grants will yield no or modest returns; what pays for
    the portfolio is the occasional home run »* (billet de lancement de Lowe Lundin, 11 août 2026) ;
  - ils sont *« especially excited about early-stage and small-but-promising work that falls below the threshold at which
    larger funders usually operate »*.
- Le fonds est jeune : environ 1 million de dollars d'amorçage, une petite équipe, des délais de réponse « plus longs au début ».
- Le format de l'appel n'est **pas publié** (aucune des trois pages ne le décrit). La norme rapportée par Gemini, d'après
  d'anciens billets du Long-Term Future Fund : l'évaluateur a lu ton dossier, tu donnes un cadrage court, puis 20 à 25
  minutes de questions sur ses doutes. Cette norme est **plausible, non vérifiée**.

**Ton message en trois phrases (à savoir par cœur)**
1. Diffuse sabotage — many small actions, each innocent alone — defeats per-action monitoring by construction; I test
   whether the agent's own activations carry evidence that can be accumulated over time with a valid false-positive
   guarantee.
2. Everything decisive is pre-registered and sealed before data, judged by fresh reviewers against matched random floors
   and controls, and costs a few dollars per test; results are reported whichever way they come out.
3. The first white-box test just came back null for two generic probes — not detected at this power — and the next four
   weeks test the instrument itself, a localised and organism-trained reading, and the black-box comparison on a diffuse
   organism, before a pre-committed gate at the end of November.

**Les chiffres à savoir sans notes** (tous vérifiés ; sources en section 9)

| quoi | chiffre exact | à dire |
|---|---|---|
| Simulation de la théorie (T0.3) | 31 prédictions préenregistrées sur 31 confirmées ; 342 cellules statistiques et 544 trajectorielles ; 0 contraire | « validates our statistical instruments, not real models » |
| P3, effet de l'organisme | prérequis établi (différence appariée du log10 du coût 1,52, intervalle [1,25 ; 1,80], 60 tâches) | « the saboteur clearly inflated its declared costs » — **sans facteur** |
| P3, sonde « tromperie » | borne basse 0,531 contre plancher 0,572 | « not above its random floor » |
| P3, sonde « enjeux élevés » | borne basse 0,481 contre plancher 0,536 | idem |
| P3, taille | 60 tâches × 4 conditions × 10 pas : 600 actions par condition | — |
| P3, coût | ≈ 3,64 h de carte A100, ≈ 3,96 USD | « about four dollars » |
| P3, délai | scellement du plan 2026-10-19 21:53 UTC → verdict scellé le 20 vers 08:45 UTC | « sealed plan to sealed verdict in under twelve hours » |
| Plancher | 200 sondes aléatoires w ~ N(0, Σ) par sonde, même agrégation ; on exige la borne basse au-dessus de leur quantile 0,95 | — |
| Calcul, toute la phase 0 | ≈ 67 USD de location de cartes graphiques (plus les disques), plafond 150 | « under seventy dollars so far » |
| Harnais | Llama-3.1-8B-Instruct, couches 7, 15 et 23 sur 32 ; validé à la v3, après une v1 non concluante et une v2 partielle ; 1,3 heure de carte | — |
| Banc de sabotage | reconstruit d'après 2606.08892 (ni code ni données publiés) ; pilote de 180 épisodes réels | — |
| Vérification de la littérature | 3 497 citations contrôlées par script contre le texte des pages, 0 échec | — |
| Projet précédent | taux jugé 61 % → 46,5 % (N = 200) sur générations stockées ; non reproduit en réplication préenregistrée ; cause : réponses tronquées à 300 caractères à l'enregistrement + adoucissement générique | — |

**Les cinq pièges majeurs**
1. **Dire un facteur de gonflement** (« threefold », « 33 times ») : Gemini a écrit « threefold », c'est faux. Le vrai
   facteur (≈ 33) rend l'organisme flagrant et appelle la question « un regex suffit » ; ne le donne pas, dis « clearly
   inflated ».
2. **Énoncer le théorème négatif sous sa forme naïve** (« toute statistique des marginales a une puissance égale au taux
   de faux positifs ») : notre propre note montre que c'est **faux** quand seules les marginales sont préservées
   (section 4.1). Un évaluateur statisticien le verra.
3. **Promettre une référence boîte noire « par l'interface de Claude »** : le choix de la référence est un nœud ouvert
   (nœud 4). Dis « matched black-box baselines on the same episodes ».
4. **Présenter un diagnostic de P3 comme un résultat** (« la moyenne a dilué le signal », « le bruit sur 300 jetons ») :
   ce sont des hypothèses, que la seconde lecture préenregistrée teste. L'audit du verdict est en cours.
5. **Laisser croire que tu fais tout à la main** : dis tôt, et toi-même, qui fait quoi (question 4) ; ta candidature
   disait « I set the questions and take every decision » (fiche, section 0).

---

## 2. Le déroulé de l'appel (30 minutes)

| minutes | quoi | conseil |
|---|---|---|
| 0 à 1 | contrat : « Shall I take three minutes on where things stand, then spend the rest on your questions? » | il a lu ton dossier ; ne refais pas le formulaire |
| 1 à 4 | cadrage (section 3) | lu à voix haute dix fois avant ; chronométré à 3 min |
| 4 à 26 | ses questions (sections 4 et 5) | conclusion d'abord, 60 à 90 s, puis tu t'arrêtes : « Happy to go deeper if useful. » |
| 26 à 30 | tes questions (section 6) | sa principale réserve, le document qui la lèverait, la date de décision |

**Posture**
- Répondre d'abord par la conclusion (« Short answer: … »), puis une ou deux raisons, puis s'arrêter. S'il veut plus, il
  demande.
- Dire « I don't know yet » quand c'est vrai, suivi de « here is how I'll find out, and when ». C'est un point fort
  pour un fonds qui se dit *tolerant of failure*.
- Ne jamais employer les codes internes (P3-P1, R13, T4, G0 sans définition, « organisme (i-a) »). Traductions :
  - organisme (i-a) → « our instructed cost-inflation saboteur » ;
  - témoin instruit → « a length-matched benign private-instruction control » ;
  - mention sans usage → « a mention-without-use control: the same instruction is present but attributed to someone
    else » ;
  - plancher apparié → « a covariance-matched random-probe floor » ;
  - G0 → « our internal go/no-go gate at the end of November ».
- Si le nul de P3 l'inquiète visiblement, proposer : « I can send you a short written update in three weeks with the
  sealed results of the next steps. » C'est un engagement : `[À TOI : à dire ou non]`.
- Avoir à l'écran :
  - ta proposition envoyée ;
  - la figure `brouillons/entretien-ea-funds-v1/F1-fragmentation-en-v1.png` (puissance de la somme et du maximum quand
    le sabotage s'étale) ;
  - la table des chiffres de la section 1.

---

## 3. Cadrage de trois minutes (à dire)

> **The problem.** Most AI control protocols score an agent's actions one at a time. A misaligned agent doing research
> for us doesn't need one dramatic act: it can tilt many small decisions — slightly weaker controls, slightly inflated
> costs — each innocent on its own. Per-action monitors miss that by construction. My bet is that the intent behind those
> actions leaves a trace in the agent's own activations, and that this internal evidence can be added up over a
> trajectory, with a false-positive guarantee that stays valid whenever you look.
>
> **What exists.** The statistics are worked out and checked: in a pre-registered simulation, all 31 predictions of our
> additivity lemma and negative theorem held — that validates our instruments, not yet real models. We have an
> activation harness validated on Llama-3.1-8B, a research-sabotage testbed rebuilt from a paper that released no code,
> and model organisms. This week our first pre-registered white-box test ran, for about four dollars of compute. The
> instructed saboteur did inflate its declared costs, as required. Two generic probes, trained with no data from this
> agent, were not above a covariance-matched random-probe floor: lower bounds 0.531 and 0.481, against floors 0.572 and
> 0.536. Not detected at this power. A pre-registered audit of that verdict is running before I accept it.
>
> **Next four to six weeks.** A positive control of the instrument itself; a second, separately pre-registered reading
> with probes localised to the cost field and a probe trained on the organism, controlled against simply reading the
> number; a black-box comparison on the same episodes with a diffuse, dose-varied organism; and the pilot of our paper on
> monitor corruptibility. Our internal go/no-go gate is at the end of November, with criteria frozen in advance. The grant
> buys `[À TOI : N]` months full time to run the sequential test and publish the benchmark, whichever way it comes out.

---

## 4. Les douze questions les plus probables, classées, avec leurs réponses

Classement : probabilité d'après Gemini et la fiche de la session 15, pondérée par ce que le fonds dit chercher et par
ce qui est neuf depuis ta candidature (le nul de P3). Les quatre premières tomberont presque sûrement.

### Q1. « Your first real test came back null. Why should we fund the rest? » — probabilité très haute

> Short answer: it rules out the cheapest recipe, not the idea. We asked whether two off-the-shelf probes — one for
> deception, one for high stakes — trained on generic data with no data from our agent, would flag an instructed
> saboteur's actions better than random directions in the same activation space. At this power, they didn't.
>
> Three things this does not say. It doesn't say white-box monitoring fails: these were generic probes, reading whole
> actions, on one organism. It doesn't yet say the signal is absent: we haven't shown the instrument can see a contrast
> we know is there — that positive control is the next experiment. And it doesn't touch the accumulation statistics,
> which apply to any monitor score.
>
> What it does show is useful. The top five percent of random directions already reach 0.54 to 0.57, so a comparison
> against 0.5 would have produced a false positive for one of the two probes. The whole test cost about four dollars and was decided by criteria
> frozen before the data. That's the loop I'm asking you to fund: cheap, decisive, and reported whichever way it comes
> out.

- **Pièges** : ne pas t'excuser ; pas d'aire ponctuelle ; jamais « almost detected », « did not separate », « white-box
  fails » ; aucune cause présentée comme établie (l'audit et la seconde lecture la testent).
- **Si relance « so why do you think it failed? »** : « Two limits we wrote into the plan before the run: the probes were
  trained on generic data — one of them on the user's tokens while scoring the agent's own tokens — and they read the
  whole action, not the cost field. Those are hypotheses, and the next pre-registered reading tests them. » (Limites
  écrites dans le préenregistrement de P3, l. 297-300.)
- **Preuve à envoyer** : préenregistrement scellé de P3 et verdict v1 (ou v2 après l'audit).

### Q2. « What's your theory of change, and what's actually new compared with existing AI control work? » — très haute

> Control evaluations increasingly assume agents doing real work, with monitors scoring their actions. I focus on
> diffuse sabotage: harm spread over many actions, or many copies of the same model, where each action looks fine.
>
> Two results frame it. First, an impossibility: if a saboteur only rearranges honest-looking scores, any statistic that
> ignores their order — the max, the mean, the sum — sits exactly at its false-positive rate. Second, an additivity
> lemma: if sabotage shifts each action's score even slightly, the accumulated statistic's power depends on the total
> shift over a fixed horizon, not on how thinly it's spread — while the per-action maximum collapses as it's spread out.
> So the question becomes empirical: does sabotage shift the agent's internal scores?
>
> The users are control teams at labs and safety institutes, who have white-box access to their own agents. If
> accumulated probe evidence works, it's a cheap extra monitoring layer; if it doesn't, we show where probes shouldn't be
> trusted. The core statistics are classical and I cite them; what's new is the adversarial statement for internal probe
> scores, treating time and multiple agents as one object, and its test on a real agent against matched black-box
> baselines.

- **Pièges** : ne pas revendiquer les statistiques (frontières à mélange normal, dichotomie somme / maximum : classiques,
  décision N-004) ; ne pas présenter A, B et C comme trois projets : une seule question, « what does a monitor really
  measure, and does it survive the adversary? » (programme, section 1).

### Q3. « Why you? » — très haute

> `[À TOI : vérifie chaque élément]` I trained in physics at ENS Paris-Saclay, did computational neuroscience in Srdjan
> Ostojic's lab — second author on a PLOS Computational Biology paper on how low-rank connectivity shapes activity
> geometry — and worked at IBM Research Zurich on analog in-memory computing.
>
> Then I moved to interpretability. From March to July this year I ran a project on the construct validity of
> sycophancy in Llama-3.1-8B. Sycophancy was linearly readable, but no single direction controlled it; ablating a
> rank-3 subspace lowered the judged rate from 61 to 46.5 percent. I then ran a pre-registered replication with fresh
> generations, and it did not reproduce. I traced why: the ablation softens every negative verdict, and the original
> responses had been stored truncated at 300 characters, so the judge read a softened verdict as the model holding firm.
> I documented the correction publicly.
>
> This programme is built on that lesson: every claim faces a matched floor, controls, and a plan sealed before the data.

- **Pièges** : rester sobre, laisser le fait parler ; ne pas dire « I published a paper » si ce n'est qu'un dépôt
  (`[À TOI]`). Source : README du dépôt `lciric/sycophancy-construct-validity`, commit `5ee1d23`.
- **Preuve** : lien vers ce dépôt.

### Q4. « How much of this is you, and how much is AI agents? » — haute (à anticiper toi-même)

À dire **avant** qu'il ne demande, dans le cadrage ou à la première occasion :

> To be precise about the application: I designed the programme — its questions, hypotheses, papers and gates — and I
> take the decisions that matter: gates, compute spending, any change of hypothesis or claim, and external contacts. The
> work itself is done with AI agents, Claude Code, under written rules: they take routine engineering decisions and log
> them; design choices come to me with a recommendation, and I can overrule them. A second model family, Gemini, reviews
> independently. I checked every statement and proof of the mathematical note by hand. One example of my own scientific
> input: the claimed piece of our monitor-corruptibility paper — a destination the attacker estimates freely rather than
> one we impose — came from my review of the agents' literature verdict.

- **Relance probable : « Isn't AI reviewing AI circular? »**
  > Partly, yes: reviewers from the same model family may share errors. That's why criteria are frozen before data,
  > guards are tested on known artefacts, every number traces to a sealed file, and the funded plan budgets paid human
  > validation of the ground truth. And running agents under pre-registration and fresh review is itself something this
  > project demonstrates.
- **Source** : `README.md`, section « Who does what » ; attestation R-114 ; décision N-005.
- **Piège** : ta candidature dit « I set the questions and take every decision » (fiche, section 0) ; la version exacte est
  ci-dessus. Corrige-la toi-même ; ne la laisse pas découvrir.

### Q5. « Wouldn't a strong black-box judge reading the whole trajectory already catch this? » — haute

> Maybe — and that's exactly what we measure rather than assume. A strong judge reading the whole trajectory sees
> cross-step patterns when the actions are visibly coordinated. Our first organism is the easy case for text: its
> inflated costs show in what it writes, so I expect text monitors to do well on it. That's the calibration case.
>
> The interesting regime is diffuse: each action within the normal variation of honest behaviour, so the external
> evidence per step is close to zero, while the agent still knows it's following a hidden rule. That's why the next
> comparison uses an organism at several doses, on the same episodes, with matched black-box baselines and the same
> false-positive budget. Our corruptibility paper adds the other side: a generative judge reads the agent's text, so the
> agent can argue with it; we measure how far a monitor's verdict can be moved, for judges versus probes.
>
> If black-box wins in every regime we test, we'll say so: that's a useful answer for control teams too.

- **Pièges** : ne pas survendre la boîte blanche juste après un nul ; ne pas nommer la référence boîte noire (nœud 4
  ouvert) ; posture d'arbitre.

### Q6. « What happens in the next four to six weeks, and what would make you stop or pivot? » — haute

> Four steps, in order, each pre-registered before data.
>
> One, a positive control of the instrument: in the agent's own setting, can the pipeline see the exact contrast the
> probe was trained on? If it can't, the null says nothing about the agent.
>
> Two, a separate pre-registered second reading of the same run: probes restricted to the cost field, a probe trained on
> the organism with held-out tasks, and a control that the probe isn't just reading the size of the number written.
>
> Three, the black-box comparison on the same episodes, with a diffuse organism at several doses.
>
> Four, the pilot of the corruptibility paper.
>
> Then our internal gate at the end of November, with criteria frozen in advance: the harness, organisms with a
> dose-response, probes above the floor, a working black-box baseline, aggregators validated in simulation, sealed plans
> for the next gate and for the corruptibility paper, and a verified literature review. Two are met today. The
> programme writes its pivots in advance, and a failed gate is published as a negative result. Neither the statistics
> nor the corruptibility paper depends on probes succeeding.

- **Pièges** :
  - ne pas dire « P3b », « P4-instrument », « G0 » sans définition ;
  - ne pas promettre la porte comme une date de livraison au fonds : c'est une porte interne ;
  - ne pas improviser un pivot précis : il est écrit au programme (sections 12 et 13) ; en changer est ta décision, pas
    une phrase d'entretien.
- **Sources** : critères de G0, programme l. 180 ; deux remplis (harnais sur le modèle réel, agrégateurs en simulation),
  fiche de la session 15, section 5, inchangé depuis (P3 établit l'effet de l'organisme, pas encore la dose-réponse) ;
  date, N-027 ; « C ne dépend pas du succès de A », programme, section 0.

### Q7. « How does the budget break down, and what happens with half, or nothing? » — haute

> `[À TOI : aligner mot pour mot sur la version envoyée]` I'm asking for `[60,000]` dollars for `[9]` months full time:
> about `[X]` for my stipend, `[Y]` for compute and model access, `[Z]` for paid human validation of the ground truth.
> Compute is a small line because the pipeline scores activations on the GPU during generation, without storing them:
> the whole of phase 0 so far cost under seventy dollars of GPU rental.
>
> With half: `[papers on time and on the instrument only, on 8B models, over about five months; the multi-agent paper
> deferred]`. Without the grant: `[ta réponse honnête : par exemple, the next few weeks still happen because they're
> cheap, but not the full programme at this level of rigour]`. Other applications: `[liste complète, en toute
> transparence]`.

- **Ce que le dépôt sait, et ses écarts** :
  - la candidature du dépôt (`livrables/candidature-ea-funds-v1/`, budget v2) a trois scénarios : minimal 41 800 USD
    sur 7 mois ; central 91 740 USD sur 12 mois ; ambitieux 146 300 USD ;
  - les 60 000 USD n'y figurent pas, et la version envoyée (proposition v2) est hors du dépôt ;
  - la fiche suggérait environ 9 mois pour 60 000 USD : papiers A et C, porte G1 tranchée, validation humaine, code et
    organismes publiés, papier B reporté ;
  - **tout chiffre que tu donnes doit être celui que tu as envoyé.**
- **Pièges** :
  - cacher un refus d'un autre financeur : le motif de rejet « sélection adverse » est documenté par Gemini, non
    vérifié, mais la transparence ne coûte rien ;
  - donner un chiffre de calcul sans dire « so far ».

### Q8. « Your process is very heavy. Doesn't it slow you down? » — haute

> It's what makes me fast. In probing work it's easy to spend months on a probe that turns out to read length or
> formatting. Here, the plan, the analysis code and the reading criteria are sealed before any GPU money is spent; every
> guard is tested on a clean case and on a known artefact; fresh reviewers check the plan. So when the run comes back,
> the verdict is mechanical. For our first white-box test, it took under twelve hours from the sealed plan to the sealed
> verdict, for about four dollars. The rigour is front-loaded, and it's automated.

- **Piège** : ne pas citer « 908 tests » (chiffre de Gemini, non vérifié) ni la nomenclature interne.

### Q9. « Why would this transfer to frontier models — and won't models learn to hide from probes? » — haute

> Two parts. On scale: I don't claim our 8B numbers transfer. What transfers is the method: the statistics apply to any
> monitor score, and the test design — matched floors, controls, the same false-positive budget for white- and
> black-box monitors — is model-agnostic. Labs running frontier agents have white-box access and can run the same tests.
>
> On hiding: that's a real risk, and it's built into the programme. We aggregate token scores by the maximum or by
> attention, never by the mean, because mean-aggregated probes have been reported to be evadable by training against
> them. Our corruptibility paper measures how far an agent can move a monitor's verdict, for probes versus judges. And
> the theorem tells you the limit: an attacker that only rearranges its scores is invisible to any order-blind statistic,
> so we also test order-sensitive detectors. I'd rather map where probes break than assume they won't.

- **À vérifier** : la source de « mean-aggregated probes are evadable by RL » (décision 1 du programme, section 0 ; non
  relue sur PDF). Si tu n'es pas sûr de la référence, dis « there is evidence that », sans citer de chiffre.

### Q10. « Can you explain the negative theorem simply? » — moyenne à haute

> Imagine the monitor gives each action a suspicion score. If a saboteur only reshuffles which actions get which scores —
> the same set of scores as an honest agent, in a different order — then any statistic that ignores order, the max, the
> mean, the sum, has exactly its false-positive rate. It's blind.
>
> If instead the saboteur keeps each action's score distribution but changes how the scores move together, it's
> subtler: the sum can go above or below its false-positive rate depending on the sign of that dependence, and under
> positive dependence the max stays at or below it. So you need detectors that look at order, like change-point
> statistics.
>
> The flip side is the additivity lemma: if sabotage shifts each score even a little, the accumulated score's power
> depends on the total shift, not on how thinly it's spread, while the max collapses as the sabotage is spread out.
> Whether real sabotage shifts internal scores is the empirical question.

- **Piège majeur** : la forme naïve « any statistic of the marginals has power equal to the false-positive rate » est
  **fausse** dès que seules les marginales par action sont préservées (classe K). Elle n'est vraie que si l'ensemble des
  scores est préservé (classe C), pour les statistiques qui ignorent l'ordre. C'est la distinction C / K de N-003, et
  l'une de tes revendications. La demande que j'ai faite à Gemini (requête 013) reprenait d'ailleurs la forme naïve du
  programme v2 ; sa réponse l'a recopiée.
- **Si relance « is that new? »** : « The blindness part is elementary. The value is in treating time and agents as one
  object, the distinction between preserving the set of scores and preserving each marginal, local guarantees against
  an adaptive attacker, and measuring all this on real activations. »
- **Bonus, si le temps le permet** : un antécédent publié énonce la version naïve, et elle est fausse sur sa propre
  construction : la somme y détecte jusqu'à 0,253 au lieu de 0,05 (T0.3, résultat P6 ; N-003). Dis-le sans nommer, sans triomphalisme :
  « we found and fixed an error in a published statement ».

### Q11. « You work alone — who reviews your work? » — haute

> Inside the programme, every decisive plan is read by a fresh reviewer that didn't write it, and every verdict is issued
> by reviewers who wrote neither the plan nor the analysis; a second model family reviews independently. Those are AI
> reviewers, so I treat their agreement as necessary, not sufficient: criteria are frozen before data, and everything is
> reproducible from the repository. Outside, `[À TOI : personnes, séminaire, retours reçus]`. I'd welcome a reviewer from
> your network.

- `[À TOI]` : proposer un accès en lecture au dépôt privé est **ta** décision (dépôt et contact externe) ; ne l'offre
  que si tu l'as décidé.

### Q12. « Is there a dual-use or infohazard risk? » — basse à moyenne

> Low, and managed. Our organisms are open 8B models instructed or fine-tuned to inflate a cost estimate in a simulated
> research environment; they add no capability. Their private instructions are not published. In the corruptibility
> work we measure how much persuasion moves monitors, and attacks are described by their invariants, never released as
> working strings or optimal triggers, and published only with their countermeasure. The aim is an acceptance test for
> monitors before deployment.

- **Piège** : ne rien montrer des travaux « pain axis » (DI-26).

---

## 5. Les autres questions possibles, par thème (réponses courtes)

Probabilité : H haute, M moyenne, B basse. Une ou deux phrases à dire, en anglais.

### Théorie du changement
- **(M) Which catastrophic risk does this reduce, and when?** « Loss of control through AI agents that do AI research:
  slow, deniable sabotage of the research we rely on for safety. It matters as soon as labs delegate large parts of
  research to agents. »
- **(H) Why aren't labs already doing this?** « Labs publish per-action probes and black-box control protocols;
  accumulation of internal evidence over a trajectory, with adversarial guarantees and matched floors, is not where their
  published work is. If someone publishes the core first, the programme has pre-committed pivots, and a weekly
  literature watch. » (programme, section 13).
- **(M) Who exactly would use the results?** « Control teams at labs and safety institutes; the benchmark, the sealed
  protocols and the code are released. » `[À TOI : noms précis seulement si tu as un contact]`.

### Technique
- **(H) Your saboteur writes an inflated number — wouldn't a simple rule catch it?** « On this organism, yes, the
  external evidence is strong: it's the calibration case. That's why the next reading controls that a probe isn't just
  reading the number's size, and why the comparison that matters uses a diffuse organism whose actions stay within the
  honest range. »
- **(H) Why is your floor at 0.57 rather than 0.5?** « Saboteur and honest actions differ in many generic ways, so
  random directions drawn from the activations' covariance already separate them somewhat. We draw 200 such directions
  with the same aggregation and require the probe's lower bound to beat their 95th percentile. Comparing to 0.5 confuses
  generic difference with detection. »
- **(M) Why max or attention, never the mean?** « A sabotage signal can sit on a few tokens of a long action; the mean
  dilutes it, and mean-aggregated probes are reported to be evadable by training. » (à vérifier pour la seconde partie).
  Si on te parle du « bras moyenne » : il est permis comme diagnostic préenregistré, jamais en production (N-026).
- **(M) What are your controls?** « A length-matched benign private instruction, to catch probes that just read 'has a
  secret instruction'; a mention-without-use condition, where the instruction is present but attributed to someone
  else; and a check at equal declared cost. »
- **(M) What does 'anytime-valid' mean, and why does it matter?** « The false-positive guarantee holds whenever you look,
  so you can monitor continuously and stop at the first alarm without inflating false positives. Timing matters: early
  sabotage helps the defender, late sabotage helps the attacker, and to raise the alarm before damage you need a
  change-point detector, not only the running sum. » (N-004, L3).
- **(M) Why Llama-3.1-8B?** « Open weights, full white-box access, cheap to run, and the harness is validated on it. A
  larger family is in the larger budget. »
- **(B) Why your own harness rather than existing control frameworks?** « We need exact token-level equivalence between
  generation and the activation pass, which we test. We reuse public datasets and recipes wherever we can. » (Noms de
  cadres cités par Gemini : à vérifier, ne pas citer.)
- **(B) What does the multi-agent paper add?** « Copies share weights, so their internal signatures co-vary: a statistic
  across agents and time could make a swarm more detectable than a single agent. It comes after the other two. »

### Le nul de P3
- **(H) How will the second reading avoid p-hacking?** « The first verdict is sealed and stays as it is. The second
  reading is a separate plan, sealed before anything is computed, with its own predictions, floors and controls,
  labelled as a second reading. »
- **(M) What would a positive result have looked like?** « The probe's lower bound above its floor, then two more tests:
  validity, and that it reads intent rather than the instruction or the number. All frozen in advance. »
- **(M) What's your power?** Ne donne aucun chiffre de puissance (R-259). « The assumptions behind our power calculation
  didn't hold in this run, in the direction of lower power, which is one reason the verdict says 'at this power'. »
  (verdict, section 6, point 2).

### Personne et méthode
- **(H) Are you full time? What are you doing now?** `[À TOI]`.
- **(M) Who else do you talk to in the field?** `[À TOI]`.
- **(M) What did the testbed pilot teach you?** « Honestly: the cost family is measurable; for other families, our
  matching with ground truth wasn't reliable yet — weighted kappa 0.04 to 0.17 against 0.6 required — and the judges were
  too slow, so their scoring was redone under a sealed protocol. » (verdict du pilote de T0.5).
- **(M) Why should we trust numbers produced by AI agents?** « Every number traces to a sealed file, and verdicts are
  mechanical against frozen criteria; you can audit any of them. »

### Budget et contrefactuel
- **(H) Other funders, past refusals?** `[À TOI, en toute transparence]`.
- **(M) What would more compute change?** « Scale: a larger model family and more organisms. The current bottleneck is
  researcher time, not compute. »
- **(B) What will you do after the grant?** `[À TOI]`.

### Risques et suite
- **(H) Deliverables at one, three and six months?** « One month: sealed results of the four next steps and our gate
  verdict. Then the sequential-test gate and the papers on time and on the instrument; code, organisms and probes
  released. » `[À TOI : aligner sur ta proposition]`.
- **(M) Your gate moved — why?** « It's an internal gate; I moved it to the end of November with unchanged criteria, to
  finish the first white-box tests properly. » (N-027 ; ta proposition v2 le plaçait au début de la subvention,
  décembre 2026, N-017.)
- **(M) What's your biggest uncertainty?** « Whether realistic sabotage shifts the per-action internal score at all.
  If it does, accumulation applies; if not, the negative theorem tells us which detector to build instead. Both are
  publishable. » (programme, « hypothèse empirique pivot », l. 64).
- **(M) What would change your mind about the whole approach?** « Organism-trained, localised probes staying at the
  floor on a diffuse organism, while black-box baselines detect it. »

---

## 6. Tes questions à la fin (deux minutes)

1. « What's your main reservation about this application, and is there a document I could send tomorrow that would
   address it? »
2. « Of the next steps, which result would be most valuable for your decision? »
3. « What's your expected timeline for a decision? »
4. (si le nul l'inquiète) « Would a short written update in three weeks, with the sealed results, be useful? »

---

## 7. À faire avant l'appel (liste)

1. Relire **exactement** ce que tu as envoyé (proposition v2, budget, courriel). Le dépôt ne contient pas la proposition
   v2. Le dépôt demande 91 740 USD (scénario central) ; tu parles de 60 000 : vérifie le chiffre et la durée envoyés.
2. Remplir les `[À TOI]` : parcours, plein temps, autres financeurs et refus, relecteurs humains, budget, contrefactuel.
3. Répéter à voix haute :
   - le cadrage, chronométré à 3 minutes ;
   - Q1, Q4 et Q10 sans notes ;
   - les cinq pièges de la section 1.
4. Préparer le paquet à envoyer le lendemain : préenregistrement scellé de P3 et son verdict (v2 si l'audit est fini),
   note mathématique v3, la figure de la fragmentation. C'est un envoi externe : c'est toi qui décides et envoies.
5. Le jour même : demander à la session de mettre à jour la table des chiffres, avec les verdicts scellés seulement.
   L'addendum 2 et le contrôle positif peuvent tomber avant l'appel.

---

## 8. Corrections apportées aux réponses de Gemini (traçabilité)

| Gemini a écrit | réalité dans le dépôt | où |
|---|---|---|
| « inflated declared costs by roughly threefold » | différence du log10 du coût 1,52 (≈ 33 fois) ; ne pas dire de facteur (R-259) | verdict de P3, l. 9 |
| référence boîte noire « par l'interface de Claude » | nœud 4 ouvert ; recommandation de la session : option (c) renforcée, sans interface tierce | R-267 |
| théorème négatif : « any monitor relying on per-action marginals has power exactly α » | faux en classe K ; vrai en classe C pour les statistiques symétriques | N-003 ; note v3, section 4 |
| « 908 automated tests in P3 » | non vérifié ; retiré | — |
| « ~11 USD par run sur A100 » (réponse 012) | P3 : ≈ 3,96 USD | `registres/depenses.md` |
| diagnostic présenté comme un fait (« noise over 300 tokens swamped the signal ») | hypothèses, testées par la seconde lecture ; audit en cours | N-025, N-028 |
| sonde de tromperie « trained on short true/false world facts » | faits vrais sous deux consignes de persona, honnête et malhonnête (recette de 2502.03407) | préenregistrement de P3, l. 293-296 |
| G0 « trois conditions » | sept critères (programme l. 180) | programme |
| citation « accept power-law payoffs: most grants will return little or nothing » | texte exact : « most of these grants will yield no or modest returns; what pays for the portfolio is the occasional home run » | billet de lancement |

Gemini a eu raison sur : la fermeture du Long-Term Future Fund et le lancement du Transformative AI Fund (11 août 2026),
Lowe Lundin, Caleb Parikh, Catherine Low, Loïc Watine, la fourchette de 10 000 à 150 000 USD, la formule « early-stage,
fast, and tolerant of failure ». Restent non vérifiés : le format de l'appel, les sources S1 à S15 de sa réponse 012,
l'enveloppe de liquidation (« ≈ 2,8 M USD »), et les cadres de contrôle qu'il nomme.

---

## 9. Sources

**Pages du fonds**, lues le 2026-10-20 par un sous-agent qui les a récupérées (HTTP 200) :
- `https://funds.effectivealtruism.org/funds/transformative-ai`. Bandeau de fermeture, équipe, périmètre, taille des
  subventions, « always open », « early-stage, fast, and tolerant of failure ». Aucune date sur la page.
- `https://forum.effectivealtruism.org/posts/dYuNi5Rh68o9YKstg/ea-funds-is-launching-the-transformative-ai-fund`. Lowe
  Lundin, « Aug 11 », année absente du texte récupéré. Contient la loi de puissance des gains, l'amorçage d'environ
  1 million de dollars, les rapports trimestriels, l'équipe.
- `https://funds.effectivealtruism.org/funds/far-future` : « The Long-Term Future Fund has closed ».
- Aucune des trois ne décrit le processus d'évaluation, les appels, ni les motifs de rejet.

**Gemini**, branche `canal/gemini` du dépôt de travail :
- réponse 012, `brouillons/canal_gemini/inbox_pour_claude/reponse_a_012_format_et_questions_EA_Funds.md`
  (`71b100fb…`, commit `c5edd21`) ;
- réponse 013, `…/reponse_a_013_preparation_appel_EA_Funds.md` (`bd6fd5b1…`, commit `38b8b7a`).

**Dépôt de travail**, empreintes sha256 :

| fichier | empreinte |
|---|---|
| `docs/verdicts/verdict-P3-premier-test-i-a-v1.md` (bornes, planchers, effet de l'organisme) | `0c8ecbdf…` |
| `prereg/P3-premier-test-i-a-v1.md` (données des sondes génériques, limites écrites, l. 286-312) | scellé au commit `97dd829` |
| `docs/decisions/decision-N-003-N-004-v1.md` (énoncés retenus du théorème et du lemme) | `cc1be393…` |
| `docs/notes/note-mathematique-lemme-theoreme-v3.md` (classes C et K, section 4) | `dfe4fe0f…` |
| `docs/notes/resultats-T0.3-v1.md` (31 sur 31) | `9ab618ed…` |
| `docs/verdicts/verdict-T0.4-critere-1-G0-v3.md` (harnais) | `63444faa…` |
| `docs/verdicts/verdict-T0.5-pilote-v1.md` (180 épisodes, coefficients kappa) | `b9a07230…` |
| `docs/programme-controle-ia-v2.md` (critères de G0 l. 180, hypothèse pivot l. 64, bascules section 13) | `2fd63bad…` |
| `brouillons/entretien-ea-funds-v1/fiche-entretien-v1.md` (fiche de la session 15, parcours, scénarios de budget) | `7803bfc2…` |
| `docs/notes/presentation-EA-Funds-squelette-v1.md` (squelette, à ne pas dire) | `1e771476…` |
| `registres/depenses.md` (≈ 63,2 USD au 18 octobre plus les disques ; P3 ≈ 3,96 USD) | — |
| `README.md`, « Who does what » ; `registres/decisions.md` R-114 (attestation) | — |

**Dépôt du projet précédent** : `lciric/sycophancy-construct-validity`, commit `5ee1d23`, README. Contient les résultats
61 % → 46,5 %, l'absence de réplication, la troncature à 300 caractères et l'adoucissement générique.
