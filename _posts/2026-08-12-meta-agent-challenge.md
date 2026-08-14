---
title: 'The Meta-Agent Challenge: Are Current Agents Capable of Autonomous Agent Development?'
date: 2026-08-12
permalink: /posts/2026/08/meta-agent-challenge/
meta: "[arXiv 2606.04455](https://arxiv.org/abs/2606.04455) · Xinyu Lu, Tianshu Wang, Pengbo Wang, Zujie Wen, Zhiqiang Zhang, Jun Zhou, Boxi Cao, Yaojie Lu, Hongyu Lin, Xianpei Han, Le Sun (ISCAS + Ant Group, Jun 2026)"
summary: "A benchmark that grades a model not on solving the task but on writing the agent that solves it — with the anti-reward-hacking plumbing that makes such a score believable."
tags:
  - RSI
  - paper-notes
  - benchmark
  - harness
---

**Takeaway**
- A code agent gets a sandbox, a hidden test split, and 12–24 hours to write the agent that solves the task; across five domains, meta-agents rarely beat human-engineered scaffolds and the design process is brittle.

**Remaining work**
- Grading is rule-based. Under an LLM judge, how fast does the meta-agent optimize the judge instead of the answer?
- The executor is weak (Qwen3-8B). What changes with a strong one — or when designer and executor are the same model?
- This and [Meta-Harness](/posts/2026/08/meta-harness/) are both single-domain RSI. What does cross-domain RSI look like?
