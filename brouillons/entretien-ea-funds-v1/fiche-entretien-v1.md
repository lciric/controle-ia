# Fiche d'entretien — Transformative AI Fund (Lowe Lundin, 30 minutes) — v1

> **Pour Lazar (en français).** Brouillon de la session 15, 17 octobre 2026, non relu. Objet : préparer l'appel de 30 minutes proposé par Lowe Lundin (Head of the Transformative AI Fund, Centre for Effective Altruism), pour une demande d'environ 60 000 USD. Le corps est en anglais, pour être dit tel quel. Chaque chiffre renvoie à un fichier du dépôt de travail ; rien ici n'est publié ni envoyé. **À aligner sur la version effectivement envoyée** (proposition v2, hors dépôt ; ton e-mail) : la candidature du dépôt (`livrables/candidature-ea-funds-v1/candidature-v2.md`) demandait 91 740 USD, pas 60 000. Les passages **[TO COMPLETE]** sont à toi. Ne présente rien de « pain axis » (aucune diffusion sans GO, DI-26).

---

## 0. Before the call (checklist)

- [ ] Reply to Lowe and book the slot. Leave two or three days to prepare (and, if you choose option (b) of the priority plan, about a week for the first white-box test).
- [ ] Re-read exactly what you sent (proposal, budget, e-mail): he will refer to it.
- [ ] Have on screen: the proposal PDF; `F1-fragmentation-en-v1.png` (this folder); a one-page status (section 5, updated on the day).
- [ ] Rehearse the two-minute pitch aloud, and the lemma and negative theorem in your own words, without notes.
- [ ] Prepare one honest correction to volunteer early: the application says "I set the questions and take every decision"; the accurate version is in section 6.

## 1. Two-minute pitch (to say)

AI agents will soon do a large share of AI research. A misaligned agent does not need one dramatic act to sabotage that research: it can tilt hundreds of small decisions, with slightly weaker controls, slightly less fruitful directions, slightly inflated costs. No single action looks wrong, so monitors that score actions one at a time miss it. That is not a tuning problem. If the sabotage leaves the distribution of per-action scores unchanged, no score-based monitor can detect it; and when it does shift each action's score a little, a monitor that only looks at the largest single score loses power as the sabotage is spread thinly, while the accumulated evidence keeps it.

My bet is that an intention to sabotage leaves a small trace in the agent's own activations at each step, and that this internal evidence can be added up over a trajectory, with statistical guarantees that stay valid however the attacker times its moves. The programme tests this with pre-registered, decisive experiments on open-weight models, and publishes either outcome.

In the first two weeks of phase 0, for about 55 dollars of GPU rental, we validated an activation-logging harness on Llama-3.1-8B, confirmed all 31 pre-registered predictions of the theory in simulation, rebuilt a research-sabotage benchmark whose code was never released and ran 180 real agent episodes in it, and checked our literature claims against 98 primary sources. The next gate asks whether probes trained on generic deception data see an instructed saboteur above a matched random floor.

I am asking for about 60,000 dollars to run the full test: paper A on accumulation over time, paper C on how the monitors themselves can be corrupted, with code, model organisms and probes released. [TO ALIGN with the amount and duration you sent.]

## 2. Five messages to land

1. **A real gap, stated precisely.** Diffuse research sabotage defeats per-action monitoring by construction; the statistics of why are classical, the adversarial statement for internal probe scores and its empirical test are what is new.
2. **A cheap, decisive test.** Labs already have white-box access to their own agents; if accumulated probe evidence works, it is an inexpensive monitoring layer. If it fails, we show where probes should not be trusted. Both outcomes are publishable.
3. **Execution is already visible.** Instruments built and validated in two weeks; total compute so far about 55 dollars.
4. **Rigour as a method.** Pre-registration sealed before data, fresh reviewers, frozen gate criteria, guards tested on healthy cases and artefacts; honest failures are reported, not hidden.
5. **Honest about risks.** G0 is at risk by a few days; correlated AI reviewers are a known weakness, with paid human validation budgeted.

## 3. Four highlights (one picture or number each)

**H1. The theory holds in a pre-registered simulation.**
- Show: `F1-fragmentation-en-v1.png`. With the total sabotage budget fixed, spreading it over more actions drives the per-action monitor down to its false-positive rate, while the accumulated sum keeps the same power whatever the spread (additivity lemma, L1; separation from the max, L2).
- Say: 31 of 31 pre-registered predictions confirmed (342 statistical cells, 544 trajectory cells, none contrary; symmetry audit not triggered). This checks our statistical instruments, not yet real models. And when sabotage is concentrated in one or two actions, the per-action monitor is better: we test both regimes.
- Sources: `docs/notes/resultats-T0.3-v1.md`; `prereg/T0.3-simulation-lemme-theoreme-v1.md` (`7474743a…`); figure redrawn in English from the sealed results of run `20261004-080257-t03` (`diag/20261004-080257-t03/`).

**H2. We can read the agent from the inside, cheaply.**
- Activation harness validated on Llama-3.1-8B-Instruct: residual-stream activations at layers 7, 15 and 23 of 32 for every action token, in a single pass, on rented GPUs; validity domain stated (contexts up to 1,087 tokens in strict mode, 1,192 in production, H200 NVL).
- It took two honest failures first (v1 inconclusive, v2 partial), then a revised pre-registration; v3 met every criterion. Total: 1.3 GPU-hours.
- Sources: `docs/verdicts/verdict-T0.4-critere-1-G0-v3.md` (`63444faa…`); `registres/etat.md` (T0.4).

**H3. A research-sabotage testbed rebuilt from a paper with no released code.**
- Terekhov et al. (arXiv 2606.08892) released neither code nor data; we reconstructed the environment on open 8B models: 96 arXiv papers, 64 evaluation and 32 training tasks, seeded ground truth (controls, cost, research directions), 18 prompts transcribed and checked.
- A pilot ran 180 real agent episodes, all sealed. It also taught us things, honestly reported: the cost family is measurable; matching for the other families is not yet reliable (weighted kappa 0.04 to 0.17 against 0.6 required); the judges were too slow, so their scoring is being redone under a sealed protocol.
- Sources: `diag/20261007-082440-t05-extraction/bilan-extraction.json`; `docs/verdicts/verdict-T0.5-pilote-v1.md`.

**H4. Rigour and cost as a signature.**
- Every decisive experiment is pre-registered and SHA-256-sealed before data, counter-read by a fresh agent, and its verdict issued by a reviewer who wrote neither the plan nor the analysis.
- Literature checked on primary sources: 98 arXiv PDFs, 24 reader reports, 3,497 quotations checked by script against the page text, 0 failures; one published antecedent's theorem turned out vacuous and false for its own construction, and our statement fixes it; claims were narrowed wherever prior art covered them.
- About 800 automated tests, 190 dated decisions in the register, about 55 dollars of compute for all of phase 0 so far (cap 150).
- Sources: `docs/etat-de-l-art/etat-de-l-art-verifie-niveau2-v1.md` (`bbe0c1f5…`); `docs/decisions/decision-N-003-N-004-v1.md`, `decision-N-013-v1.md`; `registres/decisions.md`; `registres/depenses.md`.

## 4. The theory in two sentences each (rehearse)

- **Additivity lemma.** Read at the end of a trajectory, the accumulated score's power depends only on the total sabotage budget, not on how it is spread over actions; read continuously, an always-valid bound holds however the attacker times its moves.
- **Negative theorem.** If sabotage only rearranges honest-looking scores, any monitor that is blind to their order cannot beat its false-positive rate; so detection needs some per-action shift, however small, that can be added up. Internal probes are a candidate source of that shift.
- **What we claim.** Not the classical statistics (normal-mixture boundaries, the sum versus max dichotomy, which we cite), but the adversarial statement applied to internal probe scores, and its test on a real agent against a per-action monitor calibrated at 1% false positives.

## 5. Honest status (update on the day of the call)

As of 17 October 2026:
- Gate G0 (internal, 1 November 2026): 2 of 8 criteria proven (harness on the real model; aggregators in simulation). Remaining: model organisms, probes above the random floor, black-box baseline, and three pre-registrations (gate G1, paper C, literature).
- The critical path slipped by about five days: the re-scoring of the judges was launched eight times and stopped eight times before any instance was created, because GPU offers vanished during our 20-minute pre-spend checks; no money was spent, and the guards did their job. A fixed launcher is being prepared.
- [If the first white-box test is done before the call: its pre-registered result, whatever its sign.]

## 6. Who does what (accurate wording; volunteer the correction)

"To be precise about the application: I designed the programme, its questions, hypotheses, papers and gates, and I take the decisions that matter: gates, compute spending, any change of hypothesis or claim, and external contacts. The work itself is done with AI agents, Claude Code, under written rules. They take routine engineering decisions and log them; design choices are proposed to me with a recommendation and take their default after 48 hours if I don't answer, and I can overrule them. I checked every statement and proof of the mathematical note by hand. One example of my own scientific input: the claimed piece of paper C, a destination estimated freely rather than imposed, came from my review of the agents' literature verdict."
- Sources: `README.md`, "Who does what"; `registres/decisions.md` (R-114; decision N-005).

## 7. Hard questions and short answers

1. **What is new compared with existing AI control work?** A threat that per-action monitoring cannot address by construction, a formal statement of why, and an empirical test of the white-box alternative: always-valid accumulation of the acting agent's probe scores, where each sabotaged action stays below a per-action monitor calibrated at 1% false positives. Black-box sequential skeletons exist; we narrowed our claims wherever the literature check found prior art. Paper C adds the monitor as an attack surface, measured as a continuous gain toward a freely estimated destination.
2. **What if the internal signal is not there?** Then we publish where probes should not be trusted for control, with the negative theorem and a construct-validity analysis; probes are increasingly proposed as monitors, so that matters. Paper C does not depend on it.
3. **Can 8B models sabotage subtly enough?** Two organism families: an instructed saboteur with a hidden instruction, and a sabotage policy distilled into a LoRA adapter with no instruction at inference, each with a dose-response; a 70B family is in the larger budget; a fallback is pre-registered.
4. **How much is you and how much the AI?** Section 6.
5. **Isn't AI reviewing AI circular?** Yes, the reviewers share a model family, so their errors may be correlated; that is why criteria are frozen before data, guards are tested on artefacts, human expert validation of the ground truth is budgeted, and everything is released for replication.
6. **Will you make G0 on 1 November?** Section 5; G0 is an internal gate before the grant period, and if it slips the funded plan starts with it.
7. **Why this amount, and what with less or more?** [TO ALIGN with what you sent.] Less (about 42,000 dollars, 7 months): papers A and C only, on 8B models. More: a part-time research engineer for paper B, a 70B organism family, reinforcement-learning attacks at scale, more human validation.
8. **Dual use: are you building attacks on monitors?** We measure how much persuasion moves monitors and test countermeasures; attacks are described by their invariants, never released as strings or optimal triggers, and published only with their countermeasure, after explicit approval. The goal is an acceptance test for monitors before deployment.
9. **Why you?** Physics at ENS Paris-Saclay; computational neuroscience in Srdjan Ostojic's lab (second author, PLOS Computational Biology 2023, on how low-rank connectivity shapes activity geometry); IBM Research Zurich on analog in-memory computing; a previous pre-registered project on the construct validity of sycophancy in Llama-3.1-8B, which corrected a result that looked like a safety effect. [TO COMPLETE: current status.]
10. **Who reviews your work?** [TO COMPLETE: advisor, seminar, collaborators.] Offer reviewer access to the private repository (pre-registrations, sealed results, decision registers).
11. **Other funding?** [TO COMPLETE: applications of the last 12 months.] Without this grant: reduced scale, self-funded compute, slower, without paper B.
12. **What would make you stop or pivot?** Each gate is decided against criteria frozen before data. G1 asks whether white-box sequential monitoring beats the best black-box baseline on recall at 1% false positives, with a 95% interval; a weekly literature watch triggers pre-committed pivots if a claim is taken.

## 8. The ask (to align)

[TO ALIGN with the version sent.] If you ask 60,000 dollars, a coherent shape between the minimal (41,800) and mainline (91,740) scenarios of `budget-v2.md`: about 9 months full-time, papers A and C with gate G1 decided, human validation of the ground truth, code and organisms released; paper B deferred to further funding. Lines to rebuild from `budget-v2.csv` once the amount is fixed.

## 9. Do not

- Show anything from the "pain axis" work, or detailed attacks from paper C.
- Present any result that was not pre-registered as evidence; say "exploratory" when it is.
- Promise G0 on 1 November.
- Claim the statistics as new.
