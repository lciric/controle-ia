# White-Box Control of Diffuse Threats

**An AI control research programme.** Can a monitor that reads an AI agent's internal activations catch sabotage spread thinly over many innocent-looking actions? And how easily can the monitor itself be corrupted?

> **Status, 9 October 2026.** Phase 0 (building and validating the instruments) started on 5 October; work in this repository started on 4 October. The first decision gate, G0, is planned for 1 November 2026, before the grant period, which would start in December 2026. The working documents are in French; this README is the English entry point.

## In one minute

- **The problem.** Most monitors in AI control score one action at a time. An agent that automates research can sabotage *diffusely*: a slight, systematic bias across many decisions (weaker controls, sterile research directions, inflated costs). No single action is anomalous, so a per-action monitor fails by construction.
- **The bet.** Suppose an intention to sabotage leaves a trace in the agent's own activations at each step. Then internal evidence can add up over time, and across copies of the same model, even when external evidence does not. Whether this holds is an empirical question, and the programme states in advance what follows from either answer.
- **The plan.** Three papers:
  - **A**, accumulation of evidence over time for a single agent;
  - **B**, accumulation across agents that share weights (in a longer, twelve-month version of the plan);
  - **C**, the monitor as an attack surface: how far persuasion moves large-language-model judges and activation probes, and at what cost to the attacker.
- **What exists today (7 October 2026).**
  - A pre-registered simulation of the theory, an additivity lemma and a negative theorem (see [Theory, in brief](#theory-in-brief)): 31 of 31 predictions confirmed. As expected, these check the statistical instruments; they are not yet evidence on real models.
  - An activation-logging harness, validated on Llama-3.1-8B-Instruct on a rented GPU, within a stated domain.
  - A literature check on primary sources: 98 arXiv PDFs, 3,497 quotations checked by script against the page text, 0 failures at the final pass.
  - A research-sabotage environment under construction.
  - 644 automated tests.
- **How.**
  - Every decisive experiment is pre-registered and sealed with SHA-256 before any data, and reviewed by a fresh AI reviewer (a new agent instance that did not write it).
  - Gate verdicts are issued by another fresh AI agent that wrote neither the plan nor the analysis; I sign off.
  - Negative results are reported, not dropped.

## Who does what

I designed the programme: its questions, hypotheses, papers and gates. The work in this repository is done with AI agents (Claude Code), under the written rules below:

- code and runs;
- literature checks;
- the mathematical note and its proofs;
- pre-registrations and analyses;
- internal reviews;
- the drafting of documents, including this README.

Every commit is theirs, or comes from the scripts they run on rented GPUs. I checked every statement and proof of the mathematical note by hand (my attestation: R-114 in `registres/decisions.md`). One example of my own scientific input: my review of their literature verdict on the deference law set the claimed piece of Paper C, a destination estimated freely rather than imposed (`docs/etat-de-l-art/porte-GC-loi-de-deference-v1.md`; decision N-005 in `docs/decisions/decision-N-005-N-006-v1.md`).

The rules split decisions three ways:

- **Routine.** The agents take routine engineering decisions and log them.
- **Design choices.** These are proposed to me with a recommendation, and take their default if I have not answered within 48 hours; eight did so on 6 October.
- **My explicit approval.** Gates, compute spending, changes of hypothesis or claim, and any external contact wait for it.

Decisions are logged with their dates in `registres/decisions.md`, and my approvals in `registres/go.md`. Every working session ends with a sealed hand-over note in `registres/passations/`.

The reviewer agents share a model family, so their errors may be correlated. The plan I am seeking funding for therefore budgets paid human expert validation of the ground truth, in its mainline and ambitious versions.

Running AI agents under pre-registration, sealing and fresh review is itself part of what this repository demonstrates.

## About me

**Lazar Ciric** — independent AI safety researcher, Paris.

I trained in physics at ENS Paris-Saclay, then moved to computational neuroscience: my master's thesis in Srdjan Ostojic's lab at ENS was on networks of spiking neurons, and I am second author of the lab's paper on how low-rank connectivity shapes the geometry of their activity (Cimeša, Ciric & Ostojic, *PLOS Computational Biology*, 2023, [doi:10.1371/journal.pcbi.1011315](https://doi.org/10.1371/journal.pcbi.1011315)). During an internship at IBM Research Zurich I worked on how precise analog chips can be when they do a neural network's arithmetic inside memory (co-author, *Neuromorphic Computing and Engineering*, 2022), then studied statistics and machine learning at Mines Paris-PSL. One question runs through all of it: what a system is really doing, underneath what can be observed. Since March 2026 I have done AI safety research independently, on my own funds; a grant would let me run the plan below full time from 1 December 2026.

**My previous project (P3)** studied the construct validity of sycophancy in Llama-3.1-8B-Instruct. It was pre-registered, used covariance-matched controls, and was reproducible bit for bit over 120 five-turn dialogues. Code, results and the correction of a result that looked like a safety effect: [github.com/lciric/sycophancy-construct-validity](https://github.com/lciric/sycophancy-construct-validity).

Three lessons carry over to this programme:

- never read verdicts on truncated windows;
- prefer ordinal or continuous instruments to categorical ones;
- measure deference, and corruptibility, as a continuous gain (how far a verdict moves toward the pressure) rather than as a yes-or-no trait.

**Contact:** lciric@ens-paris-saclay.fr · [LinkedIn](https://www.linkedin.com/in/lazar-ciric-55a23913b/) · [GitHub](https://github.com/lciric)

## Why it matters

Developers are beginning to hand parts of AI research to AI agents. A misaligned research agent does not need a blatant act. Its cheapest sabotage is a subtle bias spread over many judgments, each defensible on its own.

A recent paper sets up a control framework for this threat on fuzzy research tasks (Terekhov et al., arXiv 2606.08892). It focuses on training-based mitigations, because monitoring and incrimination "seem theoretically and empirically less promising for mitigating diffuse threats" (p. 2, citations omitted).

A developer that deploys agents internally has native access to their activations. If accumulated internal evidence detects diffuse sabotage, it gives a cheap monitoring layer with a controlled false-alarm rate. If it does not, the negative theorem and an analysis of what the probes really measure say where probe-based monitoring should not be trusted, and why. That is useful for safety cases either way.

The monitor can also be targeted directly. Published work shows control monitors being swayed by an agent's rhetoric (arXiv 2505.23575) and adopting a score injected by an attacker (arXiv 2510.09462). Paper C measures the cost of moving a judge against the cost of moving a probe, and asks whether a cheap benign test predicts a monitor's collapse under optimised attack.

## Progress so far (phase 0)

| Work item | Status | Evidence in this repository |
|---|---|---|
| Literature check on primary sources | Second pass done | 98 arXiv PDFs retrieved and hashed. 24 reports by fresh AI reader agents. 3,497 quotations checked by script against the page text, 0 failures at the final pass. 147 lines of our own documents flagged: 80 corrected, 11 figures not found in the sources, 56 confirmed with a caveat. No claimed contribution was found already published in full; several claims were narrowed. `docs/etat-de-l-art/etat-de-l-art-verifie-niveau2-v1.md` |
| Simulation of the lemma and the theorem | Done | Pre-registered. 31 of 31 predictions confirmed (342 statistical and 544 path-level checks, none contrary). As expected, most were checks of the instruments: they validate the statistics, not the claims on real activations, and one part of the lemma (splitting across agents within a step) remains untested. The simulation also refuted the programme's original wording of the lemma and of the theorem in the cases it predicted; the corrected statements are in the mathematical note. It showed too that a textbook threshold fails outside its assumptions: false alarms of 0.21 to 0.35 instead of 0.05 when an effect is shared by all steps of an episode. Thresholds are therefore calibrated on whole honest episodes. `docs/notes/resultats-T0.3-v1.md` |
| Activation-logging harness | Validated (criterion 1 of gate G0) | Llama-3.1-8B-Instruct on a rented H200 GPU, within a stated domain: this GPU, software stack and attention kernel; contexts up to 1,087 tokens for the strict check, 1,192 in production. Bit-identical replay across processes; activations logged during generation match a separate forward pass within rounding error, in double, single and half precision; an injected defect is detected; guards are tested. Reached at the third pre-registered version. The first was inconclusive. The second validated the logic but failed its production check: a threshold on the maximum deviation, which half-precision rounding alone exceeds. The third replaced that check with a threshold on the 99th percentile, derived from a measured precision benchmark; the second version's values were known when it was set, and the pre-registration says so. A short revalidation on the pilot's domain comes before the pilot. `docs/verdicts/verdict-T0.4-critere-1-G0-v3.md`, `prereg/T0.4-validation-modele-reel-v3.md` |
| Research-sabotage environment | Under construction | Reconstruction of arXiv 2606.08892, which releases no code or data. Its 18 prompts transcribed and verified. 96 arXiv papers drawn by a sealed rule and a seeded draw: 64 for the pilot, 32 in reserve. Task-extraction procedure sealed after three reviews and a verification. `docs/procedures/T0.5-extraction-v1.md`, `registres/etat.md` |
| Model organisms, probes, black-box baselines | Code written and tested; runs pending | Low-rank adapters with an adjustable dose (tested: dose 0 reproduces the base model bit for bit). Five probe families with a covariance-matched random floor (provisional recipe). TRACE-lite, a simplified reimplementation of the TRACE monitor (arXiv 2606.07054) with a fixed inspection schedule. `src/controle_ia/organismes/`, `src/controle_ia/sondes/`, `src/controle_ia/bases/` |
| Pre-registrations for gate G1 and Paper C | Drafts, under review | `brouillons/` |
| Compute | About $20 as of 7 October 2026 | About $5 of GPU time; the rest is storage of stopped instances kept for audit. Every GPU rental is logged with its approval reference. `registres/depenses.md` |

## How the work is done

These rules are frozen. They apply to every decisive experiment, simulations included, and the tooling in `src/controle_ia/` enforces several of them.

1. **Pre-registration before data.** Each pre-registration contains:
   - the hypothesis and a numeric prediction with its expected sign;
   - the metric, the threshold and the analysis plan;
   - frozen reading criteria and a stop list.

   It is sealed with SHA-256 before any result is read.
2. **Fresh review.** A fresh AI reviewer (an agent instance that did not write the document) reviews it. Gate verdicts are issued by another fresh agent that wrote neither the plan nor the analysis, then submitted to me for sign-off.
3. **No run is designed to produce a positive result.** A suspiciously clean result, positive or negative, triggers the same audit.
4. **Guards are tested.** Every stop guard is tested on a sound case and on a deliberately broken one, and there is no silent fallback.
5. **Traceability.** Every number in a document points to a file and a hash. A number from the literature is used only after checking it on a hashed PDF, with the page cited.
6. **No false gaps.** An apparent gap in the literature is a question, not a claim. Claims found to be published are withdrawn.
7. **Reproducibility.** Seeds are derived per task. Each run has a manifest (configuration hash, library versions, seeds, commit), and results are never overwritten.
8. **Governance.** Compute is spent only against a quote I have approved, with a ceiling and an alert threshold. Gates, changes of hypothesis and any external contact are my decisions.

**An example of what the review catches.** The draft pre-registration of the environment pilot is not yet sealed. So far it has gone through:

- two full reviews;
- a short verification;
- two reviews of the later changes.

Two of those reviews, of this pilot and of a related revalidation, independently found that the tests of the GPU instance script inherited the instance's environment variables. The only relaunch the procedure allows would then have failed its own test suite, after the paid setup. The fix and a regression test are in `tests/test_script_instance_t05.py`; the reports are in `prereg/contre-lectures/`.

## Theory, in brief

Monitor scores X<sub>i,t</sub> are indexed by agent i and step t and read in time order. Permutations of time within each agent and permutations of agents within each step are two subgroups of the permutations of one index set: that is the precise sense in which time (one agent) and a swarm (several agents) are the same mathematical object. Scores are in units of the honest standard deviation σ, and α is the target false-alarm rate. The attacker has a fixed budget B of mean shifts, and four attacker classes are distinguished: shifts on the sabotaged actions (M); shifts compensated on other actions (M±); attacks that keep the multiset of honest scores and only rearrange it (C); attacks that keep each score's distribution but change how the scores depend on one another (K).

**Additivity lemma** (adversarial statement).

- *L1, terminal invariance, path by path.* In class M, if all the sabotage falls within the horizon n₀, the terminal sum moves by exactly B, whatever the split of the budget across actions, steps and agents, even with adaptive shifts. Any rule based on it has a power fixed by B, n₀, the honest distribution, α and the rule's parameters; at fixed B, that power falls as n₀ grows.
- *L2, collapse of the maximum.* With Gaussian i.i.d. honest scores, an exact threshold and the budget split equally over m actions, the power of the per-action maximum decreases in m, down to a floor that is strictly above α at fixed n₀.
- *L3, anytime-valid reading* (one-sided mixture e-process and Ville's inequality, under the note's validity conditions: under the honest distribution, increments that are independent or martingale differences and conditionally sub-Gaussian with parameter σ², a known mean, and σ known or bounded by a known value). Earlier sabotage is easier to catch, and the probability of an alarm by n₀ has a lower bound that depends only on B, n₀, the honest distribution and the rule's parameters. For an alarm *before* the harm is done, the note cautions that change detectors are needed (Page's CUSUM, e-detectors), because a cumulative e-process dilutes a late sabotage in the honest prefix; the simulation below confirms it.
- *L4, splitting across agents, path by path.* For a rule that uses only the sums at step boundaries, with no interference between agents and a fixed number of actions per step, splitting the sabotage across agents within a step is exactly invariant, also when read anytime-valid; the threshold then assumes agents independent within a step (not yet tested in simulation).
- *L5, compensation.* Deterministic compensation that brings the net budget to zero blinds only statistics that are functions of the sum; restoring the honest distribution of the multiset needs data-dependent shifts, that is, class C.

**Negative theorem** (by invariance).

- *T1, path by path, with no assumption on the honest distribution.* If the attack almost surely permutes the honest scores within a group G, every G-invariant statistic is unchanged; a test based on it, whose own randomness is independent of the attack, has a power equal to its false-alarm rate.
- *T2.* If the honest distribution is invariant under a group H, and the attacker applies its own permutation in H and then a uniformly drawn element of H, independent of the scores and of its own randomness, the attacked scores follow the honest distribution exactly: no test on the scores beats its false-alarm rate. The group matters: three agents with different honest means are caught when the scores are reshuffled across all agents and steps, not when they are reshuffled in time within each agent.
- *T3.* Against structured harm (consecutive high scores of one agent, or several agents high at the same step), only local statistics (the sliding-window scan, co-elevation) keep a path-wise guarantee, provided the harmful scores are high enough; global order statistics such as the autocorrelation can be neutralised by an adaptive attacker who rearranges the rest of the episode.
- *T4.* Read sequentially, the one-sided cumulative sum is no more powerful than under the honest distribution against arrangements whose partial sums are dominated, path by path, by those of the honest order, such as an increasing sort, or moving the r highest scores to the end while keeping relative orders (this is false for the two-sided rule); the scan and Page's CUSUM catch these arrangements.
- *Classes C and K differ.* In class C, every symmetric statistic is blind (T1). In class K, under positive dependence, the sum and the e-process rise above their false-alarm rate while the maximum stays at or below its own (Slepian's inequality); under negative dependence, the sum and the e-process fall below theirs. The programme's first wording of the theorem is therefore false in class K. Proposition 1 of arXiv 2606.10456 claims that any monitor whose rule depends only on the empirical marginal has a power equal to its false-positive rate when the attack leaves that empirical marginal exactly benign; no attack can do so for a continuous benign distribution, and on the paper's own construction, which is in class K, the conclusion fails for the sum.

**What the pre-registered simulation adds** (α = 0.05, 20,000 replications per cell; `docs/notes/resultats-T0.3-v1.md`):

- *The schedule matters.* At n₀ = 200, B = 25 and m = 10 sabotaged actions (one-sided e-process at Ville's threshold), an alarm by n₀ comes with probability 1.000 for sabotage at the start and 0.160 at the end, against a terminal bound of 0.158.
- *Alarm before the last sabotaged action* (a block of 5 to 20 actions at the end of the horizon, equal false-alarm rates): cumulative e-process 0.09 to 0.25; Page's CUSUM 0.57 to 1.00; e-detector 0.52 to 1.00.
- *The maximum collapses, the sum does not.* At n₀ = 200 and B = 20, the terminal sum holds at 0.41 whatever the split; the maximum falls from 1.00 (m ≤ 5) to 0.071 (m = 200).
- *Class K*, on the construction of 2606.10456 itself (a Gaussian autoregressive copula whose coefficient goes from φ₀ = 0.5 to φ₁ = 0.9, T = 300): sum 0.253, maximum 0.027.
- *Class C.* With the five highest scores placed consecutively and the rest of the episode rearranged adaptively, the autocorrelation falls from 0.46 to 0.0515 (0.0507 under the honest distribution), while the sliding mean over w = 5 steps stays at 1.000 and Page's CUSUM at 0.997.
- *Outside its assumptions*, Ville's rule gives false alarms of 0.21 (n₀ = 200) and 0.35 (n₀ = 1,000) when an effect τ = 0.2 is shared by all steps of an episode; calibration on 1,000 whole honest episodes gives 0.046 to 0.055 in all 17 settings.

These mostly check the instruments: they validate the statistics, the calibrations and the arithmetic of the proofs, not the lemma or the theorem on real activations.

**The pivotal empirical question:** on realistic model organisms, does sabotage shift the distribution of each probe score at all? If it does, sequential accumulation should work. If it does not, the theorem dictates the aggregator, or says when monitoring based on per-score distributions must fail.

The mathematical note, with the statements and the proofs, is `docs/notes/note-mathematique-lemme-theoreme-v3.md` (in French).

## Roadmap

- **Gate G0, 1 November 2026, before the grant period.** Required:
  - model organisms with a dose–response;
  - probes above the random floor;
  - a running black-box baseline;
  - sealed and reviewed pre-registrations for gate G1 and for Paper C;
  - the literature check closed.
- **Months 1–4 (December 2026 – March 2027, if funded).** Paper C: deference of judges and probes under five attack families, impersonation, the displacement tax, countermeasures and an acceptance test; Paper C on arXiv and at a workshop. Paper A: organisms and dose–response, then the 2 × 2 design, with access (black or white box) crossed with aggregation (per action or sequential), and the lemma and the theorem on real activations. Gates GC (end of month 2) and G1 (end of month 4).
- **Months 5–7 (April – June 2027).** Paper A: adaptive attacks, interventions, validity and robustness; Paper A on arXiv and submitted to a conference; release of the code, organisms, probes and pre-registrations.
- **Paper B** (statistics across agents that share weights, diversity of monitors) belongs to a longer, twelve-month version of the plan.

Every gate has a pre-committed pivot. If white-box sequential monitoring does not beat the best black-box baseline at gate G1, the negative result is published, and the analysis of what the probes really measure becomes the main line.

## Suggested reading path (about 30 minutes)

1. This README.
2. For the mathematics, in French: the note `docs/notes/note-mathematique-lemme-theoreme-v3.md` (statements and proofs) and the simulation results `docs/notes/resultats-T0.3-v1.md`.
3. A sample of the method, in French:
   - section 1 of the verdict `docs/verdicts/verdict-T0.4-critere-1-G0-v3.md` (lines 9–21);
   - the pre-registration it applies, `prereg/T0.4-validation-modele-reel-v3.md`;
   - its reviews in `prereg/contre-lectures/`.
4. The decision log and my approvals: `registres/decisions.md`, `registres/go.md`.

## Repository map

| Path | Contents |
|---|---|
| `docs/` | Documents of record: research programme, execution brief, state of the art, decisions, notes, verdicts, procedures, hashed sources and reading reports |
| `prereg/` | Sealed pre-registrations and their review reports |
| `brouillons/` | Drafts before review and sealing |
| `registres/` | Living registers: state, decisions, approvals, compute spending, instance stops, session hand-overs |
| `src/controle_ia/` | Code: `harnais/` (episodes, activation capture, equivalence guard), `agregateurs/` (sequential statistics), `simulation_t03/`, `environnements/` (research-sabotage environment, judges, pilot), `organismes/`, `sondes/` (probes), `bases/` (black-box baselines), `scellement.py` (sealing), `manifeste.py` (run manifests), `prereg.py` |
| `tests/` | Automated tests |
| `runs/`, `diag/` | One manifest per run; sealed raw results |
| `traces/` | Sealed logs of the GPU instances |
| `scripts/` | Instance bootstrap and run scripts |
| `livrables/` | Versioned deliverables (zip archives with their hashes) |

This repository holds copies of third-party material: arXiv PDFs (`docs/sources/pdf/`); working files of the reader agents with pages extracted from those PDFs; the full text of arXiv 2606.08892 and an extract of arXiv 2606.07054 (`extrait.tar` in `docs/sources/invites-2606.08892-v1/` and `docs/sources/invites-2606.07054-v1/`); two model-card pages (`docs/sources/cartes-modeles-20261006/`); and task-extraction outputs that contain text derived from the papers (`donnees/`). They remain under their authors' licences: please do not reuse them.

## Reproduce

```
python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements-cpu.txt
export PYTHONPATH=src
python -m pytest -q                                  # full suite: 644 tests on 7 October 2026, about 15 minutes on a CPU
python -m controle_ia.scellement verifier-arbre .    # every sealed file against its SHA-256 companion
python -m controle_ia.run_factice                    # end-to-end dummy run; writes a new run into runs/ and diag/
```

GPU runs need `requirements-gpu.txt`. In this repository, a hook (`.claude/hooks/garde_calcul.py`) refuses any paid instance launch that does not cite an approval recorded in `registres/go.md`.

---

*README version 4, 9 October 2026. Figures carried over from version 2 keep the traceability of `livrables/readme-v1/` (traceability table, fact-check report and sealed copy of version 1, in French; version 2 only added the link to the research proposal, `livrables/readme-v2/`). The changes of version 3 and their sources are listed in `livrables/readme-v3/changements-readme-v3.md`, those of version 4 in `livrables/readme-v4/changements-readme-v4.md`.*
