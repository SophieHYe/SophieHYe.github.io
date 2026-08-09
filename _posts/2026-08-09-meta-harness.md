---
title: 'Meta-Harness: End-to-End Optimization of Model Harnesses'
date: 2026-08-09
permalink: /posts/2026/08/meta-harness/
meta: "[arXiv 2603.28052](https://arxiv.org/abs/2603.28052) · Yoonho Lee, Roshen Nair, Qizheng Zhang, Kangwook Lee, Omar Khattab, Chelsea Finn (Mar 2026)"
summary: "Turns harness engineering into an executable code search, driven by a coding agent that reasons over the full raw history of prior attempts."
tags:
  - RSI
  - paper-notes
  - harness
---

**Takeaway**
- Full trajectories, not summaries
- A coding agent does the evolving
- It's a search problem; the hard part is credit assignment
- Code-as-representation is a free regularizer

**Remaining work**
- Credit assignment stays qualitative (no per-component score), and no guarantee each round improves.
- Large, open-ended search space explored under a tight budget — running each candidate on the frozen model is the compute bottleneck.
- Generalizes across datasets and models, but not across task types.
