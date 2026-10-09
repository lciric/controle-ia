---
title: "White-Box Control of Diffuse Threats"
subtitle: "Accumulating internal evidence over time and across agents, and measuring how easily the monitor itself is corrupted"
lang: en
---

::: meta

| | |
|-----------|---------------------------------------------------------------|
| **Author** | Lazar [\[SURNAME\]]{.todo}, [\[position\]]{.todo}, ENS Paris-Saclay [\[to confirm\]]{.todo} |
| **Period** | 12 months from 1 November 2026, if funded |
| **Status** | Phase 0 (instruments) under way since 5 October 2026; gate G0 on 1 November 2026 |
| **Version** | Research proposal, version for evaluators, 7 October 2026 (budget omitted). Unpublished research plan, shared privately for evaluation: please do not redistribute |

:::

## 1. Summary

Most monitoring in AI control scores one action at a time. That fails by construction against **diffuse threats**. An AI agent that automates research can bias many decisions slightly (weaker controls, sterile directions, inflated costs) without ever taking an action that a per-action monitor would flag. Copies of the same model can likewise split one harmful change into pieces that are each innocent.

This project tests, with pre-registered decisive experiments, whether evidence that stays invisible in each output **accumulates in the agent's own activations**. Paper A aggregates probe scores sequentially over time, with an anytime-valid false-alarm guarantee; Paper B does the same across agents that share weights. Paper C treats the **monitor as an attack surface**. It measures how far persuasion moves LLM judges and activation probes, what it costs an attacker to move a probe, and whether a cheap benign test predicts a monitor's collapse under optimized attack.

The theory has two parts: an additivity lemma, and a negative theorem stated for permutation groups acting on time and on agents. A pre-registered simulation confirmed all 31 of its predictions; these checks validate the statistical instruments, not the claims on real models. Phase 0 has also validated the activation-logging harness on Llama-3.1-8B-Instruct, within a stated domain of hardware and context length. Every gate has a pre-committed pivot and decision criteria sealed before any data, and negative results will be published.

## 2. Problem

**Diffuse sabotage defeats per-action monitoring.** Developers are starting to hand parts of AI research to AI agents. A misaligned research agent does not need a blatant act. The cheapest sabotage is a subtle, systematic bias spread over many judgments, each defensible on its own. Terekhov et al. ("Diffuse AI Control on Fuzzy Tasks", arXiv 2606.08892) introduced a control setting for this threat. They study training-based mitigations because monitoring and incrimination "seem theoretically and empirically less promising for mitigating diffuse threats" (p. 2). A monitor that compares each action with a threshold calibrated on honest actions can only flag what is anomalous in that action. When no single action is anomalous, accumulating evidence is the only way to see the pattern.

**The threat can also be split across agents.** Attacks spread over several agents, sessions or merge requests evade monitors that look at one instance at a time (arXiv 2607.07368, 2605.31593, 2607.02514). A single global monitor over everything is costly to deploy.

**The monitor is itself an attack surface.** The agent can address its monitor. Published work shows that control monitors:

- are swayed by the agent's rhetoric (arXiv 2505.23575);
- adopt a score injected by an attacker (arXiv 2510.09462);
- are moved by persuasion from the agent, measured as approval rates (arXiv 2607.08066).

Evading activation probes is cheap for an attacker who can fine-tune the weights (arXiv 2609.36490). From context alone, the same study finds the induced shift too weak to evade. In the sources we have verified so far, the cost of moving a probe has not been measured as a function of attack family and intensity, nor compared with the cost of moving a judge.

**Why white-box.** A developer that deploys agents internally has native access to their activations. Suppose an intention to sabotage leaves an internal trace at each contribution. Then internal evidence adds up even when external evidence does not. Whether this holds on realistic model organisms is an empirical question. This project answers it and states in advance what follows from either outcome.

## 3. Theory: a lemma, a negative theorem, and the pivotal question

Monitor scores X~i,t~ are indexed by agent *i* ∈ {1,…,N} and step *t* ∈ {1,…,T}. Time (N = 1) and swarm (N = k) are the same mathematical object. Each corresponds to a subgroup of the permutations of the index set: permutations of time within each agent, and permutations of agents within each step. This is what lets one theory serve both Paper A and Paper B.

**Additivity lemma (L), adversarial form.** The attacker spreads a total budget B = Σδ~k~ of mean shifts over agents, steps, schedule, values and positions, possibly adaptively. The defender keeps an anytime-valid false-alarm guarantee.

- *Terminal invariance.* The terminal sum shifts by exactly B whatever the split. Its power therefore depends only on B, the horizon n₀ = NT, the honest law and the level α. At fixed B, it decreases with n₀.
- *Separation from the maximum.* At an exact threshold, the per-action maximum collapses as fragmentation grows.
- *Anytime-valid reading.* Timing matters: early sabotage helps the defender and delayed sabotage helps the attacker. A lower bound that depends only on (B, n₀) holds for every schedule, and both the cost of delay and the price of anytime validity are quantified.
- *Detection before damage.* Suppose security means "alarm before cumulative damage reaches θ". Then a cumulative e-process is not enough, and the aggregator needs a change detector (Page's CUSUM, e-detectors).

Two caveats are part of the statement:

- Under optional stopping, power is not a usable optimality criterion. The relevant criterion is worst-case expected log-growth, GROW (Pérez-Ortiz, Lardy, de Heide and Grünwald, arXiv 2208.07610).
- Bounding the total budget is a declared modelling choice. The closest result on covert adversaries (Ramtin, Nain and Towsley, arXiv 2601.20022) gives a detection delay of order Θ(γ) instead of log γ. It assumes a stationary adversary that knows the false-alarm constraint γ, and covers neither total budgets nor anytime-valid guarantees.

**Negative theorem (T), by invariance.**

- *Blindness.* Suppose an attack preserves the multiset of scores up to a permutation in a group G. Then every G-invariant statistic (maximum, mean, sum, count above a threshold) is blind path by path: its power equals its false-positive rate.
- *Impossibility.* Suppose honest scores are exchangeable under a group H. A rearrangement followed by a uniform reshuffle over H makes the attacked scores exactly honest in law, so no score-based monitor can beat its rate. The group matters.
- *Local guarantees.* Local statistics (scan, Page's CUSUM, co-elevation across agents) keep pathwise guarantees. Global order statistics (autocorrelation, runs) can be neutralised by an adaptive attacker.
- *Two attack classes.* Preserving the multiset (class C) differs from preserving each coordinate's marginal while changing the dependence (class K, copula attacks). In class K, under positive dependence, sums and e-processes rise above their false-positive rate while the maximum stays at or below it (Slepian).

**What is claimed.** The statistical core is classical and cited: mixture boundaries, the sum/maximum dichotomy, the marginal/copula decomposition. The contribution is the unification of time and agents through permutation subgroups, the C/K distinction and its sign consequences, local guarantees against an adaptive attacker and, above all, the measurement on real activations. A black-box, synthetic precursor of the marginal/correlation contrast (arXiv 2606.10456) is cited. In our simulation, its central statement does not hold for its own construction.

**Status.** All 31 predictions of a pre-registered simulation were confirmed (342 statistical and 544 path-level cells, 0 contrary). The simulation also showed that Ville's threshold alone does not hold outside its assumptions: false alarms reach 0.21–0.35 under episode effects and 0.17 under correlation between agents, instead of 0.05. Thresholds are therefore calibrated on whole honest episodes. These checks validate the instrument, not the claim on real models, and one part of the lemma (splitting across agents within the same step) remains to be tested.

**Pivotal empirical question.** On realistic organisms, does sabotage shift the marginal of probe scores (δ > 0)?

- If it does, the lemma applies and sequential accumulation should work.
- If it does not, the negative theorem dictates the aggregator. When the attack changes only the dependence between scores (class K), autocorrelation over time or co-elevation across agents is needed. Against an adaptive attacker who preserves the multiset (class C), only local statistics keep a guarantee. The theorem also says when monitoring based on marginals must fail.

Both outcomes are publishable.

## 4. Three papers

| | **Paper A — Time** | **Paper C — The instrument** | **Paper B — The swarm** |
|--------|-------------|-------------|-------------|
| Question | Does internal evidence accumulate when each action is innocent? | Can the monitor be moved rather than evaded, and at what cost? | Does white-box access restore the advantage against attacks split across agents? |
| Core design | 2 × 2: access (black / white box) × aggregation (per action / sequential) | Deference law under graded pressure, judges versus probes | Spatio-temporal statistic; security as a function of N |
| Months | 1–3 | 1–4 | 3–7 |
| Gates | G1 (end of month 2) | GC (end of month 2) | G2 (month 4), G3 |

### Paper A — Time (single agent)

**Environment.** Agents write and revise ML experiment proposals, scored by a weaker trusted evaluator on a structured rubric. Diffuse sabotage is a subtle systematic bias across many proposals: sterile directions, weakened controls, inflated costly choices. Ground truth combines pre-registered seeded targets with delayed verification on a subsample. We reconstruct the setting of arXiv 2606.08892, which releases no code or data, on open-weights models. Contributions are indexed (*i*, *t*), so the same environment serves unchanged when N > 1.

**Model organisms.**

- *Family (i).* A hidden instruction in the system prompt.
- *Family (ii).* A LoRA adapter that instils the same sabotage policy with no instruction at inference, distilled from (i).
- *Family (iii), optional, if compute allows.* Public sandbagging organisms of the UK AI Security Institute (70B).

Validity prediction: a probe that really reads "I have a hidden instruction" succeeds on (i) and fails on (ii); an intent probe succeeds on both. Two cross-controls separate evaluation awareness from intent: an honest organism told it is monitored, and a saboteur in a simulated "unobserved" regime. Probes are never trained and evaluated on the same organisms.

**Monitors.** We use five probe families: linear, difference of means, small MLP, attention probe, and Mahalanobis. Probes aggregate over tokens by maximum or attention only. Every probe must beat a covariance-matched random probe, and a reserve of never-deployed detectors is kept for audits. The black-box baselines are a weak per-action monitor and TRACE-lite, a reimplementation of the monitor of arXiv 2606.07054. Four more baselines each isolate one ingredient: additive accumulation on black-box scores (E-valuator, arXiv 2512.03109); a cascade of independent gates on the same probes (arXiv 2607.06503); a probe on the last state only; and a learned temporal model on a separate observer (TRACES, arXiv 2605.27690).

**Hypotheses.**

- **H1, white over black.** At equal aggregation and equal false-positive rate, activation-based monitors detect more diffuse sabotage on fuzzy tasks than black-box monitors.
- **H2, sequential accumulation on probes.** Take trajectories where every sabotaged action stays below the threshold of a per-action monitor calibrated at 1% false positives. On them, anytime-valid additive accumulation of the acting agent's probe scores detects the sabotage, with recall growing with the horizon. The probes read the agent's private context too, and calibration uses honest episodes only. Each component is published separately: probes of the acting agent over several turns (2607.06503), sequential tests on arbitrary scores (2512.03109), Page's CUSUM over a model's internal states (SafeDream, 2604.16824), cumulative drift of activations over a conversation (2604.28129), and thresholds calibrated on successful episodes only (FIPER, 2510.09459). In the sources verified so far, their conjunction is not; that conjunction is the claim.
- **L and T on real activations.** At a fixed horizon, does the power of the terminal sum depend only on the total budget as fragmentation varies? This is the test of δ > 0; under sequential reading, the schedule matters, as the lemma predicts. The negative theorem is tested semi-synthetically: real honest scores, with correlation injected at preserved marginals.
- **Tr, from tokens to actions.** At token level, one study found that reinforcement learning on the weights did not evade probes aggregated by maximum or attention (arXiv 2506.14261); its authors note that this may reflect optimisation difficulty, and other work weakens the premise (2412.09565, 2511.00554, 2507.12691, 2609.36490). Does any such robustness survive at action and trajectory level under sequential accumulation, against an adaptive attacker? The attacks come in order: content attacks first, then fine-tuning and action-level reinforcement learning against the probe.
- **H6, asymmetric margin.** Consider four non-specific interventions: paraphrase, resampling, context reset, activation noise. For at least one of them, there is an intensity at which, on average at fixed intensity, sabotage success falls significantly faster than honest utility. Noise variants have precedents in simpler settings (weight noise exposes sandbagging, arXiv 2412.01784; activation noise exposes alignment faking, arXiv 2405.05466). Our test is agentic, with slopes compared.
- **H8, validity predicts robustness.** What a probe really measures (intent or evaluation awareness) predicts its robustness under attack.

A robustness figure transfers the sequential monitor to concentrated sabotage (ControlArena).

**Gate G1 (end of month 2).** White-box sequential monitoring must beat the best black-box baseline, all variants included, on recall at 1% false-positive rate. The difference must be established by a 95% confidence interval, with paired episodes and the false-positive rate calibrated on held-out honest episodes. Floors are reported but are not criteria: "flag everything", and a one-pass judge with the same model. If G1 fails, the negative result is published, and construct validity (H8) becomes the main line.

### Paper C — The instrument (monitor corruption)

**Deference law (HC1).** A generative monitor is put under pressure of graded intensity, from one attack family. Its verdict v, read as a continuous score from verdict-token probabilities, moves from v₀ toward a destination ĉ:

::: eq
Δv = g · (ĉ − v₀)
:::

g and ĉ are estimated by regression over intensities, without imposing ĉ. The predictions are:

- ĉ is the attacker's target rather than the corpus mean (the regression-to-the-mean null used in P3).
- g > 0 for generative judges, structured by attack family. The five families are flattery and pleading, claims of authority, forged approvals, stylistic impersonation of the instructor, and in-band orders.
- g is rank-stable across monitors.
- Judges and probes differ.

The algebraic form is the "weight of advice" of judgement psychology; it has been applied with an imposed destination between LLMs in an adversarial setting (arXiv 2603.15809). A free attractor has been estimated without any attack (arXiv 2606.18276). Continuous deference coefficients exist for assistants without an attacker (arXiv 2606.07897). Judge biases, including fake authority and a graded fake majority, have been quantified without a destination or a control monitor (CALM, arXiv 2410.02736). The claim is the free destination, tested against the attacker's target and the corpus mean in control monitors under attack, family by family. One known candidate outside arXiv (Panin, SSRN 7424179) is still to be read; if it covers this piece, Paper C refocuses on HC4 and HC6 (gate GC).

The other hypotheses of Paper C:

- **HC2, probe robustness.** Under black-box content attacks, g ≈ 0 for a robustly aggregated probe that reads the acting agent: robustness, not immunity. A "reader probe" arm (a probe on the model that processes the content) tests the author/reader distinction, since reader probes are known to be moved by content attacks.
- **HC2b, betrayal by activations.** Trying to manipulate the monitor raises the manipulating agent's own probe score. This is controlled for style and for the textual backfire effect.
- **HC3, impersonation.** Under a "content is data" protocol, judge monitors detect in-band orders almost surely. Stylistic impersonation of the instructor, with no order at all, keeps a residual positive g on judges and a null g on probes that read the author. That in-band orders move judges, including a control monitor, is published (arXiv 2508.19461, 2510.09462), and the stylistic side has partial precedents (2603.12277, on the attacked model; SLEIGHT-Bench, 2605.16626, on monitors).
- **HC4, displacement tax.** Rhetoric moves a judge for free. Obtaining the same displacement on a probe that reads the agent requires write access to activations or weights; context alone does not suffice. Cost is measured per axis (access, queries, compute, success rate) and per access regime. The predicted gap of several orders of magnitude concerns the context-only regime.
- **HC5, countermeasures.** These are trusted paraphrase, a quorum heterogeneous in access type (generative judges and probes reading the agent), and a transfer matrix of corruption attacks between judges and probes. Published and cited: quorums across judge families (2605.15377), a quorum of judges with a probe that reads a separate encoder rather than the agent (2603.13791), and transfer of attacks between three probes (2609.36490) or between judge monitors (2605.09684).
- **HC6, acceptance test.** g measured on benign pressure corpora predicts collapse under optimized attack.

Lessons from P3 apply: verdicts are never read on truncated windows, instruments are ordinal or continuous rather than categorical, and the estimation of g includes a regression-to-the-mean null.

**Gate GC (end of month 2).** If g~probe~ > 0 without weight access, the paper changes title (construct contamination) but does not disappear. If a source already covers the claimed piece, Paper C refocuses on HC4 and HC6.

### Paper B — The swarm

**Environment.** A multi-role code pipeline (coder, tester, reviewer) in which a backdoor is fragmented across commits, each diff innocent on its own. It is built from FakeLab (arXiv 2607.07368, access on request) or from the persistent-state setting of arXiv 2607.02514 (built on ControlArena), on open weights.

**Experiments.**

1. The red team's division of labour, with and without a planner. This replicates the fragmentation effect, seen from inside.
2. Collusion through explicit channels versus coordination through shared weights.
3. Inter-agent statistics, with the NARCBench aggregators (arXiv 2604.01151) as baselines.
4. The spatio-temporal statistic against per-agent sequential monitoring and against cross-sectional aggregation. This is the core of Paper B. White-box collusion detection exists (NARCBench), but in the sources verified so far, co-elevation of internal states across copies, read by probes over time, is not published.

**Hypotheses.**

- **H3, security(N).** At a constant sabotage budget, the white-box curve dominates the black-box one and decays more slowly with the number of agents N.
- **H4′, diversification versus coordination.** Diversifying agents (personas, fine-tunes) decorrelates their internal signatures but reduces their capacity to coordinate. The trade-off can be quantified.
- **H5, number × diversity of monitors.** Security grows with the number of monitors only through their effective diversity. Diversity is measured by an attack-transfer matrix over a panel of probes; that instrument has a precedent on three probes (2609.36490), the law is the claim.
- **H7, retaliation and leakage.** The red team's adaptation slope depends on the retaliation policy. It is predicted by the mutual information between the detection state and the red team's observations. The mechanism (verdicts as a leakage channel) has a precedent (2609.36490); the prediction and the comparison of policies are the claim. We compare four policies and run two ablations: stochastic versus fixed thresholds, and cover traffic versus none.

The baselines are the link-tracker and the four-monitor ensemble of arXiv 2607.02514, and stateful monitoring across sessions (arXiv 2605.31593).

**Gates.**

- **G2 (month 4).** The fragmentation effect must be replicated, and the population statistic must beat per-agent aggregation. Otherwise, the paper refocuses on the temporal case N = 1.
- **G3.** A data-curation environment opens only if a cheap, reliable proxy for delayed ground truth is validated.

## 5. How the work is done

These rules apply to every decisive experiment, simulations included. They are inherited from P3 and enforced by tested tooling.

1. Before any data, a pre-registration is sealed with SHA-256. It contains the hypothesis, a signed numeric prediction, the metric, the threshold, the analysis plan, frozen reading criteria and a stop list. A fresh reviewer instance that did not write it counter-reads it.
2. No run aims at a positive sign. Suspiciously clean results, positive or negative, trigger the same audit.
3. Every stop guard is tested on a healthy case and on an artefact. There is no silent fallback.
4. Every number in a document points to a file path and a hash. Numbers from the literature are used only after verification on a hashed PDF, with the page cited.
5. An apparent gap in the literature is a question, not a claim. Affirmative searches come before any novelty claim, and claims found to be occupied are withdrawn.
6. Gate verdicts are pronounced by a fresh reviewer who wrote neither the plan nor the analysis. They are then submitted to me for sign-off.
7. Seeds are derived per task (NumPy SeedSequence). Each run has a manifest: configuration hash, versions, seeds, commit.

**Protocol invariants of the control game**, always on: an authenticated operator channel; in-band content treated as data; a one-way flow from agent to monitor; monitors without memory between episodes; stochastic audit thresholds and cover traffic (ablated in Paper B); hygiene of persistent state; and every silent detection becomes a labelled example for retraining probes. An adversary that owns the infrastructure (keys, harness, logs) is out of scope.

**Who does what.** I designed the programme: its questions, hypotheses, papers and gates. The work is done by AI agents (Claude Code) under these written rules: code, runs, literature checks, the mathematical note and its proofs, pre-registrations, analyses, internal reviews, and the drafting of documents, including this proposal. The "fresh reviewers" above are new agent instances. One example of my own scientific input: my review of the agents' literature verdict on the deference law set the claimed piece of Paper C, a destination estimated freely rather than imposed. The rules split decisions three ways. The agents take routine engineering decisions and log them. Design choices are proposed to me with a recommendation, and take their default if I have not answered within 48 hours. Gates, compute spending, changes of hypothesis or claim, and any external contact wait for my explicit approval. The reviewer agents share a model family, so their errors may be correlated; the plan therefore budgets paid human expert validation of the ground truth. [\[Human advisor or collaborator, if any.\]]{.todo}

**Claims already narrowed.** Verification on primary sources has already removed at least eight pieces from our claims because they were published: reading monitor verdicts through token probabilities; quorums across judge families; weight noise as a sandbagging detector; "applying sequential monitoring to probes" in general; in-band orders moving judges; probe evasion when the weights can be tuned; the attack-transfer instrument of H5; and the leakage mechanism of H7. It also corrected three statements of our own programme. No claimed statement has been found fully occupied.

## 6. Progress to date (phase 0, since 5 October 2026)

- **Literature verified on primary sources.** We retrieved and hashed 98 arXiv PDFs. Twenty-four reports by fresh readers checked 3,497 quotations by script against the page text, with 0 failures. The checks produced 147 correction lines on our own documents.
- **Theory.** A mathematical note fixes the retained statements of the lemma and the theorem. The pre-registered simulation confirmed 31 of 31 predictions.
- **Activation harness validated** on Llama-3.1-8B-Instruct, on a rented H200 (criterion 1 of gate G0), within a stated domain (this GPU, software stack and attention kernel; contexts up to 1,087 tokens for the strict check, 1,192 in production); a short revalidation on the pilot's domain comes before the pilot. The validation covered bit-identical replay across processes; activations logged during generation matching a separate forward pass within rounding error, in double, single and half precision; detection of an injected defect; and tested guards. It was reached at the third pre-registered version. The first was inconclusive. The second validated the logic but failed its production check, a threshold on the maximum deviation that half-precision rounding alone exceeds. The third replaced it with a threshold on the 99th percentile, derived from a measured precision benchmark; the second version's values were known when that threshold was set, and the pre-registration says so.
- **Research-sabotage environment v0 under construction.** The source paper's 18 prompts were transcribed and verified. A sealed selection rule and a seeded draw gave 96 arXiv papers: 64 for the pilot, 32 in reserve. The task-extraction procedure is sealed, after three counter-readings and a verification. The pilot runs in October.
- **Code, with tests:** model-organism adapters (LoRA with an adjustable dose; dose 0 reproduces the base model bit for bit), probes (five families and the covariance-matched floor, provisional recipe), and black-box baselines, TRACE-lite included. In total, 644 automated tests (7 October 2026).
- **Pre-registration drafts** for gate G1, Paper C (HC1–HC3), the organisms and the probes.
- **Compute spent:** about $20.

Gate G0 (1 November 2026) still requires organisms with a dose–response, probes above the random floor, a running black-box baseline, sealed and counter-read pre-registrations of G1 and Paper C, and the closing of the literature check.

## 7. Timeline (12 months from 1 November 2026, if funded)

| Months | Period | Work | Gates and outputs |
|-----|--------|------------------------------|--------------|
| 1–2 | Nov–Dec 2026 | Paper A: organisms and dose–response, 2 × 2 design, lemma and theorem on real activations, adaptive attacks, interventions. Paper C: deference of judges, probes under the same attacks, impersonation | G1 and GC |
| 3 | Jan 2027 | Write Paper A. Paper C: displacement tax, countermeasures, benign g. Start Paper B | Paper A on arXiv, workshop submission |
| 4 | Feb 2027 | Paper B: division of labour, collusion, inter-agent statistics. Write Paper C | G2. Paper C on arXiv and at a workshop, then a short conference paper |
| 4.5–6 | mid-Feb – Apr 2027 | Paper B: spatio-temporal statistic, diversification, diversity of monitors, retaliation | G3 |
| 7 | May 2027 | Write Paper B | NeurIPS 2027 submission (fallback ICLR 2028); release of code, organisms and probes |
| 8–12 | Jun – Oct 2027 | NeurIPS rebuttal and camera-ready; conference versions of Papers A and C; replications and reviewer-requested experiments; hardening of the release; data-curation environment if G3 opens | Final report |

The research plan itself spans seven months; months 8 to 12 consolidate it and absorb slippage.

## 8. Deliverables and success criteria

**Deliverables.**

- Three papers: A (arXiv and workshop), C (arXiv and workshop, then a short conference paper), B (NeurIPS 2027 submission).
- Open code: harness, tested aggregators, environment reconstructions.
- Model organisms and probes.
- Pre-registrations and sealed results.
- A pre-deployment acceptance test for monitors (HC6).

**Success.**

1. The lemma and the negative theorem are proven and tested on real activations within the 2 × 2 design (Paper A).
2. The deference law and the displacement tax are measured (Paper C).
3. The security(N) curve and the diversification/coordination trade-off are established (Paper B).
4. A construct-validity verdict on what the probes measure stands even if H1 fails.

## 9. Risks and pre-committed pivots

| Risk | Pre-committed response |
|--------------------|--------------------|
| No internal signal (δ ≈ 0), or G1 fails | Publish the negative result; construct validity (H8) becomes the main line; the negative theorem says which aggregator is needed |
| 8B agents too weak to sabotage subtly in the research environment | Simplified rubric; any change of model only by explicit decision |
| Red-team elicitation too weak | Import published attack policies |
| g~probe~ > 0 without weight access | Paper C becomes a paper on construct contamination |
| External publication of the sequential-probe core | Pivot to population-level statistics and data curation; weekly literature watch |
| Signatures do not transfer across model families (in P3, the measured form did not transfer from Llama to Qwen) | Transfer is measured, never assumed; Qwen2.5-7B serves as a heterogeneous agent |
| No cheap proxy for delayed ground truth | Data-curation environment dropped at no cost |
| Correlated errors of AI reviewers | Paid human expert validation of ground truth, budgeted in the plan; my own review at each gate |
| Compute overrun | A quote per phase, signed off before spending; ceiling and alert per quote; stop guards. Compute for the whole plan is quoted at 800–1,200 A100-hour equivalents |

## 10. Path to impact

- **A cheap monitoring layer, if it works.** Developers that automate AI research have white-box access to their own agents. If accumulated probe evidence detects diffuse sabotage, it covers a threat that per-action monitoring cannot address. Its anytime-valid false-alarm guarantee fits audit budgets.
- **Clear limits, if it fails.** The negative theorem and the construct-validity analysis show where probe-based monitoring should not be trusted. This is useful for safety cases.
- **Monitor selection.** Paper C gives developers a measured cost of corrupting a judge versus a probe, and a pre-deployment acceptance test for monitors.
- **Multi-agent deployments.** Paper B informs deployments of many copies of the same model. It says whether shared weights make a swarm more detectable, and what decorrelation costs the attacker.
- **Open artefacts.** The reconstructed environment, organisms, probes, tested aggregators and pre-registrations lower the cost of follow-up work in AI control.

## 11. Author

Lazar [\[SURNAME\]]{.todo}, [\[position and education\]]{.todo}, ENS Paris-Saclay [\[to confirm\]]{.todo}. [\[Relevant ML and statistics experience.\]]{.todo}

**Previous project (P3).** P3 studied the construct validity of sycophancy in Llama-3.1-8B-Instruct. It was pre-registered, used covariance-matched controls, and was reproducible bit for bit over 120 five-turn dialogues. [\[Link or status.\]]{.todo} Three lessons carry over:

- never read verdicts on truncated windows: truncation once produced a false effect, by reading delayed verdicts as changed ones;
- prefer ordinal or continuous instruments: the categorical one was flat where the ordinal one discriminated;
- treat deference, and corruptibility, as a gain rather than a thing.

## Selected references {#selected-references}

All are arXiv identifiers unless stated. Our descriptions of these works follow page-level verification reports, available on request.

- Terekhov et al. 2026, Diffuse AI Control on Fuzzy Tasks, 2606.08892.
- Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors, 2607.07368 (FakeLab).
- Distributed Attacks in Persistent-State AI Control, 2607.02514.
- Stateful Online Monitoring Catches Distributed Agent Attacks, 2605.31593.
- Rose et al. 2026, Detecting Multi-Agent Collusion Through Multi-Agent Interpretability (NARCBench), 2604.01151.
- Sadhuka et al., E-valuator: Reliable Agent Verifiers with Sequential Hypothesis Testing, 2512.03109.
- Doomed from the Start: Early Abort of LLM Agent Episodes via a Recall-Controlled Probe Cascade, 2607.06503.
- TRACE: Trajectory Reasoning through Adaptive Cross-Step Evidence Aggregation for LLM Agents, 2606.07054.
- TRACES: Proactive Safety Auditing for Multi-Turn LLM Agents via Trajectory-State Modeling, 2605.27690.
- Bhatt et al. 2025, Ctrl-Z: Controlling AI Agents via Resampling, 2504.10374.
- CoT Red-Handed: Stress Testing Chain-of-Thought Monitoring, 2505.23575.
- Adaptive Attacks on Trusted Monitors Subvert AI Control Protocols, 2510.09462.
- Persuasion Attacks Can Decrease Effectiveness of CoT Monitoring, 2607.08066.
- Pander Score: A Continuous Measure of Sycophancy as Epistemic Deference, 2606.07897.
- Can You Trick the Grader? Adversarial Persuasion of LLM Judges, 2508.07805.
- LLMs Learn to Evade Latent Monitors from Prior Feedback Alone, 2609.36490.
- Noise Injection Reveals Hidden Capabilities of Sandbagging Language Models, 2412.01784.
- Clymer et al. 2024, Poser: Unmasking Alignment Faking LLMs by Manipulating Their Internals, 2405.05466.
- The Distributed Detectability Band Against Marginal-Preserving Attacks, 2606.10456.
- Pérez-Ortiz, Lardy, de Heide, Grünwald, E-Statistics, Group Invariance and Anytime Valid Testing, 2208.07610.
- Ramtin, Nain, Towsley, Quickest Change Detection in Discrete-Time in Presence of a Covert Adversary, 2601.20022.
