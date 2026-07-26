---
permalink: /
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<style>
body {
  font-size: 0.9em;
}
.funding {
  background: #fdeaea;
  border-left: 4px solid #c0392b;
  padding: 10px 14px;
  border-radius: 6px;
  margin: 1.2em 0;
}
.funding p { margin: 0; }
.news { font-size: 0.9em; }
.project {
  display: flex;
  gap: 18px;
  align-items: flex-start;
  margin: 1.2em 0;
}
.project__fig { flex: 0 0 44%; max-width: 44%; }
.project__fig img { width: 100%; border: 1px solid #e6e6e6; border-radius: 6px; }
.project__title { font-weight: 700; }
.project__authors { font-size: 0.9em; margin-top: 3px; }
.project__venue { font-style: italic; font-size: 0.9em; margin-top: 2px; }
.project__badges { display: flex; flex-wrap: wrap; gap: 7px; margin-top: 10px; }
.badge {
  display: inline-flex;
  font-size: 0.72em;
  line-height: 1.7;
  border-radius: 4px;
  overflow: hidden;
  text-decoration: none !important;
}
.badge .k { background: #4a4a4a; color: #fff; padding: 2px 7px; }
.badge .v { color: #fff; padding: 2px 7px; font-weight: 600; }
.v-arxiv { background: #b31b1b; }
.v-gh    { background: #2b2b2b; }
.v-hf    { background: #ffcc4d; color: #222; }
.v-web   { background: #1a7bd4; }
.v-cite  { background: #007ec6; }
@media (max-width: 700px) {
  .project { flex-direction: column; }
  .project__fig { max-width: 100%; flex-basis: auto; }
}
@media (prefers-color-scheme: dark) {
  .funding { background: #2b1a1a; border-left-color: #e06666; }
}
</style>

This is Ye, welcome to my page.
I am a Lecturer (aka. Assistant Professor) in the Department of Computer Science at University College London.
My research builds the next generation of **coding agents** that work like software engineers inside a real command-line environment, reasoning across an entire codebase and its tools to tackle tasks such as issue resolution, agent failure repair, and more. My group focuses on CLI coding agents: we design the agent harnesses they operate in, train them in realistic terminal-world environments, and study why they fail and how they can repair themselves. What I care about most is making these agents **secure and cost-efficient**, so that they are actually affordable in practice. We also maintain [Awesome Code Agents](https://github.com/EuniAI/awesome-code-agents), a curated list of cutting-edge coding-agent projects and research.

Prior to joining UCL, I worked as a Postdoctoral Researcher at Carnegie Mellon University with Prof. Claire Le Goues.
I obtained my PhD from KTH Royal Institute of Technology, where I was fortunate to be supervised by Prof. Martin Monperrus and Prof. Benoit Baudry. I received my bachelor's degree from Sichuan University.

**Let's connect:** I'm always happy to talk research, swap ideas, or just say hi — whether we share interests or come from very different fields. Reach me at [he.ye@ucl.ac.uk](mailto:he.ye@ucl.ac.uk).

<div class="funding" markdown="1">
**Funding:** We greatly appreciate that our research is supported by Google, AWS, Mistral AI, and Delysium (Jerry Zhang) through computing credits and gift funding.
</div>

## News

<div class="news" markdown="1">
- **2026.07**: 🤗 TerminalWorld dataset exceeded <span style="color:#9b1c1c;font-weight:600">10,000</span> downloads on HuggingFace!
- **2026.06**: Organizing the 7th APR workshop at ASE — welcome to submit to [APR@ASE 2026](https://conf.researchr.org/home/ase-2026/apr-2026)!
- **2026.06**: Happy to receive the FSE 2026 Distinguished Reviewer Award.
- **2026.06**: Our paper "Agent-based Automated Remediation for Vulnerabilities in Maven Projects" is accepted to OOPSLA 2026. Congrats to Lyuye!
- **2026.06**: 🎙️ TerminalWorld was featured on [Last Week in AI](https://lastweekin.ai/p/lwiai-podcast-246-gemini-35-omni) (ep. #246), a newsletter and podcast with 181k+ listeners.
- **2026.03**: Our paper [ExecVerify](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=K6V2VzsAAAAJ&cstart=20&pagesize=80&citation_for_view=K6V2VzsAAAAJ:Wp0gIr-vW9MC) is accepted to ACL 2026 (main). Congrats to Lingxiao!
- **2025.11**: Our scaffold Prometheus achieved TOP 1 🏆 by resolving 33.77% of issues on the AWS [SWE-PolyBench leaderboard](https://amazon-science.github.io/SWE-PolyBench/#verified). Check out our [experiment results](https://github.com/EuniAI/Polybench-experiment).
- **2025.10**: Our scaffold Prometheus achieved TOP 5 overall on the [SWE-bench Verified leaderboard](https://www.swebench.com/) 🎉! Check out our [project repository](https://github.com/EuniAI/Prometheus).
</div>

## Projects

<div class="project">
  <div class="project__fig">
    <a href="https://terminalworld.ai" target="_blank" rel="noopener noreferrer"><img src="{{ '/images/terminalworld.png' | relative_url }}" alt="TerminalWorld overview" /></a>
  </div>
  <div class="project__body">
    <div class="project__title">TerminalWorld: Benchmarking Agents on Real-World Terminal Tasks.</div>
    <div class="project__authors"><a href="https://zhaoyang-chu.github.io/" target="_blank" rel="noopener noreferrer">Zhaoyang Chu</a>, Jiarui Hu*, Xingyu Jiang*, Pengyu Zou*, Han Li, Chao Peng, Peter O&rsquo;Hearn, Earl T. Barr, Mark Harman, Federica Sarro, <strong style="color:#9b1c1c">He Ye</strong>&dagger;.</div>
    <div class="project__venue">Preprint.</div>
    <div class="project__badges">
      <a class="badge" href="https://arxiv.org/abs/2605.22535" target="_blank" rel="noopener noreferrer"><span class="k">arXiv</span><span class="v v-arxiv">2605.22535</span></a>
      <a class="badge" href="https://github.com/EuniAI/TerminalWorld" target="_blank" rel="noopener noreferrer"><span class="k">GitHub</span><span class="v v-gh">36</span></a>
      <a class="badge" href="https://huggingface.co/datasets/EuniAI/TerminalWorld" target="_blank" rel="noopener noreferrer"><span class="k">HuggingFace</span><span class="v v-hf">10438</span></a>
      <a class="badge" href="https://terminalworld.ai" target="_blank" rel="noopener noreferrer"><span class="k">Website</span><span class="v v-web">terminalworld.ai</span></a>
    </div>
  </div>
</div>
