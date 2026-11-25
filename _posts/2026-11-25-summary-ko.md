---
layout: default
title: "Horizon Summary: 2026-11-25"
date: 2026-11-25
lang: ko
---

> 30개의 콘텐츠 중 9개의 중요한 정보가 선별되었습니다.

---

1. [OpenAI Establishes Tighter Lower Bound for Matrix Multiplication Exponent at Θ(n^2.25)](#item-1) ⭐️ 10.0/10
2. [Ternary Bonsai 2.5 27B](#item-2) ⭐️ 9.0/10
3. [Active intrusion campaign against Check Point security management servers](#item-3) ⭐️ 9.0/10
4. [Simon Willison Identifies Three LLM and Coding Agent Inflection Points](#item-4) ⭐️ 8.0/10
5. [Congress Rushes to Reauthorize Controversial FISA Section 702](#item-5) ⭐️ 8.0/10
6. [GPT-6 Models Demonstrate Intrinsic Protein-Design Capabilities](#item-6) ⭐️ 7.0/10
7. [astral-sh/uv released 0.13.10](#item-7) ⭐️ 7.0/10
8. [US financial crimes bureau discloses ‘cybersecurity incident’](#item-8) ⭐️ 7.0/10
9. [Now Firefox can select which sites use its VPN, and clear your browsing history with one click](#item-9) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [OpenAI Establishes Tighter Lower Bound for Matrix Multiplication Exponent at Θ(n^2.25)](https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf) ⭐️ 10.0/10

OpenAI has published a paper establishing a tighter lower bound for the matrix multiplication exponent at Θ(n^2.25), refuting a prior conjecture and resolving a significant open problem in mathematics, potentially with AI assistance. This new finding specifies the exact exponent as 9/4 across all fields. This represents a groundbreaking theoretical breakthrough in computational complexity, resolving a long-standing open problem in mathematics and potentially paving the way for more efficient algorithms and stronger AI models. It contributes to the resolution of multiple "Top 500 Open Problems in Math," highlighting AI's growing capability in fundamental scientific discovery. The result establishes a *lower bound* of Ω(n^2.25), meaning matrix multiplication *cannot* be faster than this complexity, while an *upper bound* of O(n^2.25) was already known, indicating an algorithm exists that achieves this speed. The paper suggests the use of a new tensor geometry framework developed with an unreleased AI model, whose recipe is not disclosed.

hackernews · E-Reverance · 11월25일 01:19 · [커뮤니티 토론](https://news.ycombinator.com/item?id=50637220)

**배경 지식**: The matrix multiplication exponent, denoted as ω, is the smallest real number for which any n x n matrix can be multiplied using n^ω + o(1) field operations, describing the theoretical minimum number of operations. Big-Theta (Θ) notation provides an asymptotically tight bound for an algorithm's running time, indicating both its upper and lower growth rates. A lower bound for a problem represents the theoretical minimum number of operations required to solve it for all inputs of a given size.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Matrix_multiplication_algorithm">Matrix multiplication algorithm - Wikipedia</a></li>
<li><a href="https://askfilo.com/user-question-answers-smart-solutions/explain-asymptotic-notation-big-o-omega-and-theta-notations-3335373933333939">Explain Asymptotic Notation : Big O, Omega, and Theta Notations | Filo</a></li>
<li><a href="https://en.wikipedia.org/wiki/Computational_complexity">Computational complexity - Wikipedia</a></li>

</ul>
</details>

**커뮤니티 토론**: The community lauded OpenAI for resolving multiple "Top 500 Open Problems in Math," including this one and others like mean-payoff games. There was significant discussion clarifying that the result is a *lower bound* (Ω(n^2.25)), not an upper bound (O(n^2.25)), which was already known. Some speculated that OpenAI might be holding back its best models for fundamental research, using breakthroughs to build stronger models, and noted the use of an unreleased AI model for this discovery.

**태그**: `#Theoretical Computer Science`, `#Algorithms`, `#Computational Complexity`, `#Mathematics`, `#AI Research`

---

<a id="item-2"></a>
## [Ternary Bonsai 2.5 27B](https://prismml.com/news/bonsai-2-5-27b) ⭐️ 9.0/10

Ternary Bonsai 2.5 27B is a new quantized language model demonstrating surprisingly high performance for its size, with community reports suggesting it rivals larger models on benchmarks and offers practical capabilities for local agentic coding.

hackernews · b0m · 11월24일 20:08 · [커뮤니티 토론](https://news.ycombinator.com/item?id=50633922)

**태그**: `#Large Language Models`, `#Model Quantization`, `#Local Inference`, `#AI Agents`, `#Performance Benchmarking`

---

<a id="item-3"></a>
## [Active intrusion campaign against Check Point security management servers](https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign) ⭐️ 9.0/10

An active intrusion campaign is exploiting a vulnerability in Check Point security management servers by reconstructing the internal state of JavaScript's Math.random() to forge admin session cookies.

hackernews · louiereederson · 11월24일 16:32 · [커뮤니티 토론](https://news.ycombinator.com/item?id=50630594)

**태그**: `#Cybersecurity`, `#Vulnerability`, `#Check Point`, `#PRNG`, `#Network Security`

---

<a id="item-4"></a>
## [Simon Willison Identifies Three LLM and Coding Agent Inflection Points](https://simonwillison.net/2026/Nov/24/llm-inflection-points/) ⭐️ 8.0/10

Simon Willison presented a keynote and blog post detailing three major inflection points in LLM and coding agent capabilities over the past twelve months, exemplified by the increased reliability of coding agents like Claude Opus 4.5 and the emergence of "Fable class models." These models, such as Claude Fable 5, demonstrate a new level of autonomous problem-solving by defining goals and utilizing tools. These identified inflection points are significant because they mark a rapid acceleration in the practical utility of AI, transforming LLMs and coding agents into reliable tools for complex software development and autonomous problem-solving. This advancement promises to fundamentally alter developer workflows and significantly boost productivity across the tech industry. The first inflection point in November 2025 involved models like Claude Opus 4.5 and OpenAI's GPT-5.1 Codex achieving reliable utility for daily coding tasks, reducing the need for constant human correction. The second, in June/July 2026, introduced "Fable class models" such as Claude Fable 5, which exhibit proactive, brute-force problem-solving, with an earlier version (Claude Mythos) being withheld due to its advanced cybersecurity exploitation capabilities.

rss · Simon Willison · 11월24일 23:02

**배경 지식**: Coding agents are advanced AI systems that leverage Large Language Models (LLMs) to autonomously plan, write, test, and even deploy software. Unlike simpler AI coding assistants or copilots that offer suggestions, these agents can operate independently, combining reasoning with access to coding tools and execution environments to complete complex development goals end-to-end.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://www.uipath.com/ai/what-are-coding-agents">What Are Coding Agents? | UiPath</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-coding">What is agentic coding? - IBM</a></li>

</ul>
</details>

**태그**: `#LLMs`, `#AI Agents`, `#Generative AI`, `#Technology Trends`, `#AI Progress`

---

<a id="item-5"></a>
## [Congress Rushes to Reauthorize Controversial FISA Section 702](https://www.theverge.com/policy/1041568/fisa-ndaa-blue-wave) ⭐️ 8.0/10

Members of Congress are urgently working to reauthorize Section 702 of the Foreign Intelligence Surveillance Act (FISA), a controversial warrantless wiretapping authority, potentially by attaching it to a must-pass military spending bill before the legislative session ends. This reauthorization is highly significant due to its profound implications for privacy and civil liberties, as Section 702 allows warrantless access to Americans' communications and impacts the operational environment for tech companies and broader surveillance policy. Senator Mike Rounds indicated that FISA Section 702 could be attached to the National Defense Authorization Act (NDAA), a critical military spending bill, to ensure its passage before the current legislative session concludes.

rss · The Verge Tech · 11월24일 20:00

**배경 지식**: FISA Section 702, enacted in 2008, is a critical intelligence collection authority that enables the U.S. Intelligence Community to gather foreign intelligence information about national security threats. It has been controversially used as the legal basis for surveillance programs, including PRISM, disclosed by Edward Snowden, raising concerns about warrantless access to Americans’ communications.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/FISA_Section_702">FISA Section 702</a></li>
<li><a href="https://www.intel.gov/foreign-intelligence-surveillance-act/fisa-section-702">FISA Section 702 - INTEL</a></li>
<li><a href="https://www.brennancenter.org/our-work/research-reports/section-702-foreign-intelligence-surveillance-act-fisa-2026-resource-page">Section 702 of the Foreign Intelligence Surveillance Act ...</a></li>

</ul>
</details>

**태그**: `#Government Surveillance`, `#Privacy Policy`, `#Civil Liberties`, `#Tech Policy`, `#Legislation`

---

<a id="item-6"></a>
## [GPT-6 Models Demonstrate Intrinsic Protein-Design Capabilities](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/) ⭐️ 7.0/10

OpenAI announced that its GPT-6 models can intrinsically design three-dimensional protein minibinders by writing code, marking a potential advancement in general-purpose AI for scientific design. This capability allows the models to generate 3D designs for potential minibinders based on target protein structures without relying on specialized protein AI models for the initial structural concept. This development suggests a significant step towards general-purpose AI autonomously performing complex scientific design tasks, potentially accelerating drug discovery and materials science by reducing reliance on specialized models for initial structural concepts. If proven robust, this could streamline the early stages of therapeutic development and open new avenues for AI in biological engineering. GPT-6.2 was given target protein structures and attachment points, then wrote code to create three-dimensional minibinder designs; however, specialized AI models like SolubleMPNN were still needed to suggest amino acid sequences that would fold into the proposed structures. Community discussion highlights concerns about the actual scope of GPT-6's "intrinsic" design and the lack of robust biological validation in the presented evidence, with experts questioning the extent of laboratory confirmation.

hackernews · OpenAI Newsroom · 11월24일 21:02 · [커뮤니티 토론](https://news.ycombinator.com/item?id=50634658)

**배경 지식**: Protein minibinders are small proteins, typically under 100 amino acids, that are gaining attention for their potential in pharmaceutical applications due to their ability to bind to target proteins with high specificity. De novo protein design involves creating novel protein structures and sequences from scratch, which is a crucial and challenging field in biotechnology for developing new therapeutics and functional materials. This process traditionally relies on extensive computational modeling and experimental validation.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://communities.springernature.com/posts/minibinders-tiny-proteins-with-huge-potential-in-bioengineering">Minibinders: Tiny Proteins with Huge Potential in ...</a></li>
<li><a href="https://www.nature.com/articles/s41467-025-56369-w">De novo design of protein minibinder agonists of TLR3 - Nature</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12637805/">De Novo Design of Miniprotein Inhibitors of Bacterial ...</a></li>

</ul>
</details>

**커뮤니티 토론**: The community expresses skepticism regarding the "intrinsic" nature of GPT-6's design capabilities, noting that specialized AI models were still required for sequence generation and validation, which is fundamental to protein function. Experts also raise concerns about the lack of robust biological controls and laboratory confirmation, suggesting the presented evidence leans more towards computational exploration than confirmed biological efficacy, and that the press release does not meet their bar of evidence.

**태그**: `#AI`, `#Protein Design`, `#Large Language Models`, `#Computational Biology`, `#AI in Science`

---

<a id="item-7"></a>
## [astral-sh/uv released 0.13.10](https://github.com/astral-sh/uv/releases/tag/0.13.10) ⭐️ 7.0/10

This release of `uv` (0.13.10) includes a security fix, improves `uv.lock` validation and user feedback, updates managed Python builds, and previews a new proxy index feature for lockfiles.

github · astral-releases-bot[bot] · 11월24일 21:15

**태그**: `#Python`, `#Package Management`, `#Security`, `#Dependency Management`, `#Tooling`

---

<a id="item-8"></a>
## [US financial crimes bureau discloses ‘cybersecurity incident’](https://www.theverge.com/policy/1041957/fincen-treasury-cybersecurity-incident) ⭐️ 7.0/10

The Financial Crimes Enforcement Network (FinCEN), a US Treasury Department bureau, has disclosed it is investigating a cybersecurity incident involving unauthorized access to a limited part of its systems.

rss · The Verge Tech · 11월25일 01:00

**태그**: `#Cybersecurity`, `#Government`, `#Data Breach`, `#FinCEN`, `#National Security`

---

<a id="item-9"></a>
## [Now Firefox can select which sites use its VPN, and clear your browsing history with one click](https://www.theverge.com/tech/1041474/firefox-161-vpn-rules-fire-button) ⭐️ 6.0/10

Firefox 161 now allows users to set site-specific rules for its integrated VPN, enabling automatic activation or deactivation for chosen websites.

rss · The Verge Tech · 11월24일 18:44

**태그**: `#Browser`, `#Firefox`, `#VPN`, `#Privacy`, `#User Experience`

---