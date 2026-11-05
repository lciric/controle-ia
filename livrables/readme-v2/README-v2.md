# White-Box Control of Diffuse Threats

**An AI control research programme.** Can a monitor that reads an AI agent's internal activations catch sabotage spread thinly over many innocent-looking actions? And how easily can the monitor itself be corrupted?

> **Status, 7 October 2026.** Phase 0 (building and validating the instruments) runs from 5 October to the first decision gate, G0, on 1 November 2026; work in this repository started on 4 October. This repository is private and shared for evaluation only: please do not redistribute it. Its working documents are in French; this README is the English entry point.

## In one minute

- **The problem.** Most monitors in AI control score one action at a time. An agent that automates research can sabotage *diffusely*: a slight, systematic bias across many decisions (weaker controls, sterile research directions, inflated costs). No single action is anomalous, so a per-action monitor fails by construction.
- **The bet.** Suppose an intention to sabotage leaves a trace in the agent's own activations at each step. Then internal evidence can add up over time, and across copies of the same model, even when external evidence does not. Whether this holds is an empirical question, and the programme states in advance what follows from either answer.
- **The plan.** Three papers:
  - **A**, accumulation of evidence over time for a single agent;
  - **B**, accumulation across agents that share weights;
  - **C**, the monitor as an attack surface: how far persuasion moves large-language-model judges and activation probes, and at what cost to the attacker.
- **What exists today (7 October 2026).**
  - A pre-registered simulation of the theory: 31 of 31 predictions confirmed. As expected, these check the statistical instruments; they are not yet evidence on real models.
  - An activation-logging harness, validated on Llama-3.1-8B-Instruct on a rented GPU, within a stated domain.
  - A literature check on primary sources: 98 arXiv PDFs, 3,497 quotations checked by script against the page text, 0 failures at the final pass.
  - A research-sabotage environment under construction.
  - 644 automated tests.
- **How.**
  - Every decisive experiment is pre-registered and sealed with SHA-256 before any data, and reviewed by a fresh AI reviewer (a new agent instance that did not write it).
  - Gate verdicts are issued by another fresh AI agent that wrote neither the plan nor the analysis; I sign off.
  - Negative results are reported, not dropped.

## Who does what

I designed the programme: its questions, hypotheses, papers and gates. The work in this repository is done by AI agents (Claude Code) under the written rules below:

- code and runs;
- literature checks;
- the mathematical note and its proofs;
- pre-registrations and analyses;
- internal reviews;
- the drafting of documents, including this README.

Every commit is theirs, or comes from the scripts they run on rented GPUs. One example of my own scientific input: my review of their literature verdict on the deference law set the claimed piece of Paper C, a destination estimated freely rather than imposed (`docs/etat-de-l-art/porte-GC-loi-de-deference-v1.md`; decision N-005 in `docs/decisions/decision-N-005-N-006-v1.md`).

The rules split decisions three ways:

- **Routine.** The agents take routine engineering decisions and log them.
- **Design choices.** These are proposed to me with a recommendation, and take their default if I have not answered within 48 hours; eight did so on 6 October.
- **My explicit approval.** Gates, compute spending, changes of hypothesis or claim, and any external contact wait for it.

Decisions are logged with their dates in `registres/decisions.md`, and my approvals in `registres/go.md`. Every working session ends with a sealed hand-over note in `registres/passations/`.

The reviewer agents share a model family, so their errors may be correlated. The plan I am seeking funding for therefore budgets paid human expert validation of the ground truth, in its mainline and ambitious versions.

Running AI agents under pre-registration, sealing and fresh review is itself part of what this repository demonstrates.

## About me

**Lazar [TO COMPLETE: surname]** — [TO COMPLETE: current position and education].

[TO COMPLETE: two or three sentences on the career transition into AI safety: background, motivation, and what the grant would enable.]

**My previous project (P3)** studied the construct validity of sycophancy in Llama-3.1-8B-Instruct. It was pre-registered, used covariance-matched controls, and was reproducible bit for bit over 120 five-turn dialogues. [TO COMPLETE: link or status; and whether P3 was also carried out with AI agents.]

Three lessons carry over to this programme:

- never read verdicts on truncated windows;
- prefer ordinal or continuous instruments to categorical ones;
- measure deference, and corruptibility, as a continuous gain (how far a verdict moves toward the pressure) rather than as a yes-or-no trait.

**Contact:** [TO COMPLETE: email, LinkedIn or website]

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

- Monitor scores are indexed by agent and by step, so time (one agent) and a swarm (several agents) are the same mathematical object.
- An **additivity lemma** says what a sequential test with an anytime-valid false-alarm guarantee can achieve against an attacker who splits a fixed sabotage budget.
- A **negative theorem**, stated through permutation groups, shows which statistics an adaptive attacker can blind. It also separates attacks that only reorder the scores from attacks that keep each score's distribution but change how the scores depend on one another.
- **The pivotal empirical question:** on realistic model organisms, does sabotage shift the distribution of each probe score at all? If it does, sequential accumulation should work. If it does not, the theorem dictates the aggregator, or says when monitoring based on per-score distributions must fail.

The mathematical note is `docs/notes/note-mathematique-lemme-theoreme-v3.md` (in French).

## Roadmap

- **Gate G0, 1 November 2026.** Required:
  - model organisms with a dose–response;
  - probes above the random floor;
  - a running black-box baseline;
  - sealed and reviewed pre-registrations for gate G1 and for Paper C;
  - the literature check closed.
- **Months 1–2 (November–December 2026, if funded).** Paper A core experiments, with access (black or white box) crossed with aggregation (per action or sequential). Paper C: deference of judges and probes under graded pressure. Gates G1 and GC.
- **Months 3–7 (January–May 2027).** Write Paper A; Paper C (displacement cost, countermeasures, acceptance test); Paper B (swarm statistics, diversity of monitors).

Every gate has a pre-committed pivot. If white-box sequential monitoring does not beat the best black-box baseline at gate G1, the negative result is published, and the analysis of what the probes really measure becomes the main line.

## Suggested reading path (about 30 minutes)

1. This README.
2. The research proposal, in English (8 pages): `livrables/proposition-publique-v1/proposal-public-v1.pdf`.
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

This private repository holds copies of third-party arXiv PDFs (`docs/sources/pdf/`) and extraction outputs that contain text derived from those papers (`donnees/`). They are kept for verification only, are not redistributable, and will be removed before any publication. Please do not copy them.

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

*README version 2, 7 October 2026. Every figure is traced to its source in `livrables/readme-v1/` (traceability table, fact-check report and sealed copy of version 1, in French); version 2 only adds the link to the research proposal (`livrables/readme-v2/`).*
