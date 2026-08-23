---
layout: archive
permalink: /blog/interface/queue/
title: "Agent-Native Interfaces — Paper Queue"
author_profile: true
---

Reading / writing queue for the [Agent-Native Interfaces](/blog/interface/) series.
Grouped by **where the stable semantic interface comes from** (L0 → L3), plus the evaluation axis.

Workflow: pick one → `cp _drafts/paper-note-template.md _posts/YYYY-MM-DD-slug.md` → add `series: interface` to the front matter → fill it in → check it off here.

Suggested order: **0 → 2 → 6 → 1 → 5 → 3+4+7 → 8 → 9 → 10**.

---

## 0. Framing (write first)

- [ ] **Why GUI pixels are not agent-native** — the series intro. GUI is a lossy, vision-only encoding of a contract that already exists inside the application; the agent has to decode it back into that contract on every single invocation. Four things it re-derives each time: control discovery, visual grounding, state inference, context maintenance. Concrete anchor: deleting one file takes 3 CLI steps vs 7 GUI steps ([Beyond the GUI Paradigm](https://arxiv.org/abs/2606.19388), Fig. 1).

## The evaluation axis (the backbone of the series)

- [ ] **OSWorld-MCP** — Jia, Liao, Zhang, Xu, Xie et al. (PKU + Tongyi Lab), Oct 2025 · [arxiv](https://arxiv.org/abs/2510.24563) · the first attempt at a *fair* GUI-vs-tools comparison; 158 curated MCP tools on top of OSWorld; introduces TIR (tool invocation rate) and ACS (avg completion steps). Finding: tools help almost everyone, but Claude-4-Sonnet's TIR is still only 36.3%, and performance degrades as the tool catalog grows.
- [ ] **WeaveBench** — Li, Zhou, Yu, Xu, Yang, Li, Shan (MSRA + Tsinghua), Jun 2026 · [arxiv](https://arxiv.org/abs/2606.09426) · 114 long-horizon tasks that *require* both channels (median 76 tool calls, 16 GUI↔CLI switches). Single-channel ≤3.5% vs hybrid 35.1% (+31.6pp, against +3–4pp on prior hybrid benchmarks). Trajectory-aware judge drops GPT-5.5 from 53.5% to 33.3%; reward hacking is 35% of all failures.
- [ ] **GUI vs. CLI: Execution Bottlenecks** — Zhou, Zhang, Zhao, Wei, Song, Cohan, Zhao (NYU Shanghai + Yale + NTU), Jun 2026 · [arxiv](https://arxiv.org/abs/2606.24551) · **the cleanest controlled experiment**: 440 tasks, 18 apps, identical goals/states/verifiers, modality-native action spaces. GUI 59.1% vs CLI 48.2%; only 37.6% of verifier checkpoints reachable through the skill layer; verifier-guided patching → 69.3%. Complementary failure taxonomies: GUI = grounding + long workflows, CLI = skill coverage + implicit-default reconstruction + unobservable semantics.

## L0 · The contract is already there

- [ ] **Terminal Agents Suffice for Enterprise Automation** — Bechard, Marquez Ayala, Chen, Skelton, Davasam, Sunkara, Yadav, Rajeswar (ServiceNow), Apr 2026 · [arxiv](https://arxiv.org/abs/2604.00073) · 729 tasks on ServiceNow / GitLab / ERPNext. Terminal 73–79% vs web 69–80% vs MCP 33–39%, at 2–9× lower cost. A single generic `api_call` tool recovers most of MCP's deficit → the problem is catalog granularity, not the protocol. Self-written skills cut ServiceNow cost 43.7%.
- [ ] **Beyond the GUI Paradigm: Do Mobile Agents Need the Phone Screen?** — Gu, Jiang, Guo, Chi, Wang, Liu, Yu, Chen, Wang (Mila/Concordia + Toronto + McMaster), Jun 2026 · [arxiv](https://arxiv.org/abs/2606.19388) · off-the-shelf coding agents driving Android through ADB alone beat GUI models post-trained on mobile data (71.8% vs 69.3/68.1/57.8 on AndroidWorld). Introduces the CLI-Advantage Suite (45 tasks GUI benchmarks structurally cannot sample). 3 harnesses × 4 model APIs: **generic tools only help weak models** (Codex +14.3pp, Opus 0.0pp). Oracle ceiling 88.8% / 86.3%.

## L1 · Lifted by hand (or by an agent, one app at a time)

- [ ] **CLI-Anything: Towards Agent-Native Computer Use** — Yang, Fan, Huang (HKU), Jun 2026 · [arxiv](https://arxiv.org/abs/2606.03854) · [code](https://github.com/HKUDS/CLI-Anything) · the manifesto. A 7-step harness-lift SOP and a contract `H = (S, C, I, R, V, D)`. Two growth modes: Blender (the backend already exists — lower JSON scene state into `bpy`) vs *Slay the Spire II* (the backend must be *created* by an in-process bridge). Key slogan: **if an artifact can be checked by code, it can usually be built by code**. 83 CLIs / 32 categories; 87.8% of CLI-Hub calls come from agents.
- [ ] **OpenCLI** (system, not a paper) — jackwener, 2026 · [github](https://github.com/jackwener/OpenCLI) · 179 sites / 1332 commands / Chrome Browser-Bridge reusing your logged-in session. The pieces the papers don't have: a **degradation ladder** (adapter → sitemap-guided browser → raw primitives) with a promotion path back up; **trace-based online self-repair** whose oracle is re-running the command itself; machine-readable failure contracts (sysexits); and the only public **decay measurement** I know of — fixes/adapter-year by strategy (PUBLIC_API 1.18, COOKIE 2.01, UI_SELECTOR 1.92, PAGE_FETCH 8.41, INTERCEPT 8.69). The line is *contract vs no contract*, not *API vs DOM*.

## L2 · Compiled from traces (run once, replay many)

- [ ] **SkillDroid: Compile Once, Reuse Forever** — Chen, Bellucci, Sun, Jacucci (Helsinki + UC3M + Shenzhen), Apr 2026 · [arxiv](https://arxiv.org/abs/2604.14872) · compiles LLM-guided mobile trajectories into parameterized skills replayed with **zero LLM calls**; 85.3% vs 62% baseline, −49% LLM calls, 100% over 79 replay rounds. Best line to steal: stateless agents are **non-convergent** — the baseline decays 80% → 44% over 150 rounds while SkillDroid climbs 87% → 91%.
- [ ] **AutoRPA: GUI Automation through LLM-Driven Code Synthesis from Interactions** — Chen, Hu, Yu, Yin (Hangzhou Dianzi Univ), ICML 2026 · [arxiv](https://arxiv.org/abs/2605.21082) · translator + builder agents distill ReAct trajectories into robust RPA functions; hybrid repair resumes ReAct from the breakpoint. −82~96% tokens, and the synthesized code **beats its own teacher** (no sampling noise at test time).
- [ ] **AppAgent-Claw: CLI Is All You Need for GUI Automation** — Song, Zhang, Song, Zhang (Westlake AGI Lab), Jun 2026 · [arxiv](https://arxiv.org/abs/2606.05171) · record-once / annotate-once / replay-many when there is no backend to lift. Three-layer localization (anchor → context → monitor-relative) with post-action validation. Under dark mode, layer-1 hit rate collapses 74.4% → **0%** yet end-to-end stays 100% — *reliability comes from managing failure, not eliminating it*.

## L3 · Learning to route between the two

- [ ] **ToolCUA: Optimal GUI-Tool Path Orchestration** — Hu, Zhang, Xu, Qiao, Yang et al. (Tongyi Lab + Fudan + Shanghai AI Lab), May 2026 · [arxiv](https://arxiv.org/abs/2605.12481) · [code](https://github.com/X-PLUG/ToolCUA) · **the table that should be in every talk**: handing frontier models a hybrid action space *hurts* (Claude-4.5-Sonnet 61.9 → 48.4; EvoCUA-32B 52.6 → 40.5). Fix: synthesize interleaved GUI-Tool trajectories from existing GUI corpora, then online RL with a tool-appropriateness + path-length reward. 8B model → 46.85% on OSWorld-MCP with the lowest step count of any model.

## Closing (original angle, write last)

- [ ] **The skill layer rots** — no paper measures this, because benchmark environments are frozen snapshots and OpenCLI's sites are not. Argue that contract *strength* (who pays the maintenance bill) predicts decay better than contract *level* (API vs DOM), and that the open question left by GUI-vs-CLI — can coverage be synthesized without peeking at the verifier? — is really a question about where a first-party, CI-maintained specification of an app's behavior can be found.

---

## Prior art / adjacent (for related-work, not for the daily log)

Nearest neighbours found in an arXiv sweep — none of them occupies the "app's own test suite → agent interface" cell.

- **UIFormer: From User Interface to Agent Interface** — Dec 2025 · [arxiv](https://arxiv.org/abs/2512.13438) · synthesizes DSL programs that compress UI representations for agents (−48.7~55.8% tokens). Frames **"the lack of Boolean oracles"** as the fundamental obstacle to synthesizing agent interfaces from GUIs. Optimizes the *observation*, not the *action contract*.
- **TDAD: Test-Driven AI Agent Definition** — Mar 2026 · [arxiv](https://arxiv.org/abs/2603.08806) · compiles agent *prompts* from behavioral specs turned into executable tests. Its anti-specification-gaming protocol (visible/hidden test split, semantic mutation testing, spec-evolution regression) is the reusable part.
- **SkillFab: An Agent-Native Skill Production Platform** — Jul 2026 · [arxiv](https://arxiv.org/abs/2607.03780) · demand-first lifecycle: unmet capability → skill → review → registry. The plumbing around skill production, not a method for deriving the contract.
- **GUI Test Migration via Abstraction and Concretization (MACdroid)** — Sep 2024 · [arxiv](https://arxiv.org/abs/2409.05028) · abstracts general *test logic* from source tests, then re-concretizes it for a target app. Exactly the lift needed to turn a hard-coded test into a parameterized verb — but the output is another test.
- **ReuseDroid** — Apr 2025 · [arxiv](https://arxiv.org/abs/2504.02357) · VLM-based UI test migration with active feedback.
- **NL2Test: LLM-Based Test Case Carving and Assertion Generation** — Jul 2026 · [arxiv](https://arxiv.org/abs/2607.24000) · carves replayable API regression tests from captured traffic; deterministic guardrails for dependency binding and assertion-path validation. Industrial deployment, 3,196 tests, 85.4% adoption.
- **TestGen at Meta (observation-based unit test generation)** — Feb 2024 · [arxiv](https://arxiv.org/abs/2402.06111) · test carving from serialized runtime observations, at scale.
- **"Modern web test suites rot"** — May 2026 · [arxiv](https://arxiv.org/abs/2605.15281) · counter-evidence to keep honest: UI refactors break locators and teams abandon suites within weeks. Any claim that "CI keeps test selectors stable" has to be measured, not assumed.
- **CLI task/environment synthesis cluster** — CLI-Universe [2606.22883](https://arxiv.org/abs/2606.22883), SETA [2607.10891](https://arxiv.org/abs/2607.10891), Terminal-World [2605.20876](https://arxiv.org/abs/2605.20876). Keyword-adjacent but orthogonal: they synthesize *tasks and environments for training*, not *interfaces for acting*.
