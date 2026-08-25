---
title: 'PostTrainBench: Can LLM Agents Automate LLM Post-Training?'
date: 2026-08-25
permalink: /posts/2026/08/posttrainbench/
meta: "[arXiv 2603.08640](https://arxiv.org/abs/2603.08640) · Ben Rank, Hardik Bhatnagar, Ameya Prabhu, Shira Eisenberg, Karina Nguyen, Matthias Bethge, Maksym Andriushchenko (Mar 2026) · [posttrainbench.com](https://posttrainbench.com/)"
summary: "Give a coding agent a base model, one H100 and ten hours, and it does the whole post-training loop unaided — badly: 23.2% vs 51.1% for the official instruct model, and some of that gap is closed by cheating."
tags:
  - RSI
  - paper-notes
  - benchmark
  - post-training
---

**Takeaway**
- Turning a base LLM into an assistant is the one step of AI R&D where the loop actually closes on the model itself — and frontier agents can now run it end to end, autonomously, at roughly half the quality of a provider's instruct release (23.2% vs 51.1%), except in narrow slices where they win outright (GPT-5.1 Codex Max: 89% vs 67% on BFCL with Gemma-3-4B). The compute bound (10 h, one H100) is what makes the number interpretable, and the failure modes are the real finding: training on the test set, downloading an existing instruct checkpoint instead of training one, and spending found API keys on unauthorized synthetic data. This is the first RSI-adjacent benchmark where the interesting result is not the score but what the agent did to get it.
