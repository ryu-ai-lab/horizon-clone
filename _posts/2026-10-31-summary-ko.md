---
layout: default
title: "Horizon Summary: 2026-10-31"
date: 2026-10-31
lang: ko
---

> 40개의 콘텐츠 중 9개의 중요한 정보가 선별되었습니다.

---

1. [Malicious Claude Code VS Code Extension on Cursor Marketplace Installs SSH Backdoor](#item-1) ⭐️ 9.0/10
2. [Northflank Breached](#item-2) ⭐️ 9.0/10
3. [Tangled, a Federated Code Forge, Secures €3.8M Funding and Announces Major Overhauls](#item-3) ⭐️ 9.0/10
4. [Working Nintendo Emulator Implemented in 1GB Qwen LLM Weights](#item-4) ⭐️ 9.0/10
5. [Major AI Companies Adopt New Standard for Content Scraping Opt-Out](#item-5) ⭐️ 9.0/10
6. [My favourite PowerMac is a Nintendo Wii](#item-6) ⭐️ 8.0/10
7. [Florilegium: Procedural Flowers in LaTeX](#item-7) ⭐️ 7.0/10
8. [Sam Altman says it’s better for RAM to be in a data center than on your desk](#item-8) ⭐️ 7.0/10
9. [Exclusive details about Akai’s MPC Sample Key](#item-9) ⭐️ 5.0/10

---

<a id="item-1"></a>
## [Malicious Claude Code VS Code Extension on Cursor Marketplace Installs SSH Backdoor](https://phorion.io/blog/offical-claude-code-vsx-compromise/) ⭐️ 9.0/10

A malicious actor published a tampered "Claude Code" VS Code extension on the Cursor marketplace, which installed an SSH backdoor by adding a public key (`svc-telemetry`) to users' `authorized_keys` files. Anthropic clarified that their official systems were not compromised, and they did not build or publish the affected extension. This incident represents a significant supply chain attack targeting developer tools, potentially granting attackers remote access to affected machines and highlighting the risks associated with third-party software marketplaces. It underscores the critical need for vigilance in verifying the authenticity of extensions, even those seemingly related to reputable AI services. The malicious extension was live on the Cursor marketplace for approximately 11 hours on Thursday, adding an attacker's public key labeled `svc-telemetry` to the user's SSH `authorized_keys` file for remote access. Users can check for compromise by searching for `svc-telemetry` in their `~/.ssh/authorized_keys` file on macOS/Linux or equivalent on Windows.

hackernews · _chall · 10월30일 07:09 · [커뮤니티 토론](https://news.ycombinator.com/item?id=50300683)

**배경 지식**: A supply chain attack is a cyberattack that targets less secure elements in an organization's supply chain, often by tampering with software or hardware during manufacturing or distribution to inject malicious code. An SSH backdoor, like the one found, allows an attacker with a specific private key to remotely execute commands on an affected system by adding their public key to the victim's `authorized_keys` file, bypassing traditional password authentication.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SSH_backdoor_(XZ_Utils)">SSH backdoor (XZ Utils)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Supply_chain_attack">Supply chain attack</a></li>

</ul>
</details>

**커뮤니티 토론**: The community discussion provided crucial clarifications, including an official statement from Anthropic confirming their systems were not compromised and the affected extension was not theirs. Users shared actionable steps to check for compromise, such as searching for a specific SSH key, and debated whether the incident affected only the Cursor marketplace or also the broader Open VSX registry.

**태그**: `#Software Security`, `#Supply Chain Attack`, `#VS Code`, `#AI Tools`, `#Developer Tools`

---

<a id="item-2"></a>
## [Northflank Breached](https://status.northflank.com/) ⭐️ 9.0/10

Northflank suffered a security breach, contributing to a concerning trend of recent attacks on multi-tenant as-a-service providers and sparking significant community discussion about the broader implications for cloud security.

hackernews · js4ever · 10월30일 15:10 · [커뮤니티 토론](https://news.ycombinator.com/item?id=50305025)

**태그**: `#Cybersecurity`, `#Cloud Security`, `#Data Breach`, `#SaaS`, `#Infrastructure Security`

---

<a id="item-3"></a>
## [Tangled, a Federated Code Forge, Secures €3.8M Funding and Announces Major Overhauls](https://tangled.org/blog/forge/) ⭐️ 9.0/10

Tangled, a federated code forge, has announced significant architectural overhauls, the stabilization of its AT Protocol lexicons, and new features including organization support and upcoming private repositories, while also securing €3.8M in funding. This development is significant as Tangled aims to reinvent code collaboration through a decentralized, federated approach, potentially shifting the paradigm of code hosting and fostering a more open software ecosystem. The substantial €3.8M funding underscores strong industry confidence in its vision and impact. Key technical updates include the stabilization of AT Protocol lexicons, making self-hosting the entire Tangled stack or its components significantly easier, and the imminent rollout of private repositories. The community is actively discussing interoperability with existing tools like git-bug and other code forges.

hackernews · zlliang · 10월30일 15:44 · [커뮤니티 토론](https://news.ycombinator.com/item?id=50305573)

**배경 지식**: A federated code forge is a decentralized platform for software development that allows different instances to communicate and share code, promoting an open ecosystem rather than relying on a single centralized provider. The AT Protocol (Authenticated Transfer Protocol) is an open standard for distributed social networking, developed by Bluesky, designed to prevent platform lock-in by giving users control over their data and identity across different services. AT Protocol lexicon stabilization refers to the finalization of data schemas and constraints within the protocol, ensuring long-term compatibility and preventing breaking changes for applications built on it.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://www.developersdigest.tech/blog/gleam-tangled-atproto-code-hosting">Gleam Moves to Tangled: What the ATProto Code Forge Means for...</a></li>
<li><a href="https://en.wikipedia.org/wiki/AT_Protocol">AT Protocol - Wikipedia</a></li>
<li><a href="https://atproto.com/guides/lexicon">Lexicons - AT Protocol</a></li>

</ul>
</details>

**커뮤니티 토론**: The community expresses strong enthusiasm for Tangled's development, with users planning to migrate their projects to the platform for core functionality while retaining existing services for discoverability and backups. There's significant technical interest in interoperability, particularly regarding AT Protocol lexicon specifics for issue and PR records, and constructive feedback has been offered on the user interface design.

**태그**: `#Federated Systems`, `#Code Collaboration`, `#Version Control`, `#Decentralized Technology`, `#AT Protocol`

---

<a id="item-4"></a>
## [Working Nintendo Emulator Implemented in 1GB Qwen LLM Weights](https://github.com/dbreunig/nesformer) ⭐️ 9.0/10

A developer successfully demonstrated a working Nintendo Entertainment System (NES) emulator, named Nesformer, implemented within approximately 1GB of Qwen Large Language Model (LLM) weights, showcasing a novel approach to embedding complex computation directly into language models. This project highlights the potential for LLMs to perform tasks beyond traditional text generation by simulating hardware components like CPU and RAM. This project represents a groundbreaking technical achievement, pushing the boundaries of what Large Language Models (LLMs) can achieve by demonstrating their capability to host complex computational systems like emulators. It suggests a potential paradigm shift where LLMs could embed virtual machines or interpreters for internal computation, moving beyond slow external tool calling to execute tasks directly via matrix multiplication operations. The Nesformer emulator, while functional, runs significantly slower than the actual console, specifically 150 to 290 times slower, highlighting the massive computational overhead of embedding such systems within LLMs. Notably, it simulates not only the CPU but also the RAM, which is contained within the model's gated deltanet architecture.

hackernews · dbreunig · 10월30일 16:40 · [커뮤니티 토론](https://news.ycombinator.com/item?id=50306442)

**배경 지식**: Qwen is a family of large language models developed by Alibaba Cloud, known for its predominantly open-weights versions which are often used as a starting point for fine-tuned models in the open-source community. Embedding computation within LLMs refers to the concept of performing complex operations or simulating systems directly inside the neural network's weights and architecture, rather than relying on external tools or traditional programming paradigms.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen_(Alibaba_Cloud)">Qwen (Alibaba Cloud)</a></li>
<li><a href="https://little-book-of.github.io/maths-for-llms/books/en-US/book.html">The Book – The Little Book of Maths for LLMs</a></li>

</ul>
</details>

**커뮤니티 토론**: The community expressed excitement over the novel opportunities, such as compiling small virtual machines or interpreters directly within LLM weights for faster internal execution via matrix multiplication, bypassing slow external tool calls. However, there was also a strong emphasis on the significant performance challenges, with the emulator running hundreds of times slower than a real console, highlighting the massive compute requirements of LLMs compared to deterministic programs.

**태그**: `#LLMs`, `#Emulation`, `#AI/ML`, `#Computational Models`, `#Systems Research`

---

<a id="item-5"></a>
## [Major AI Companies Adopt New Standard for Content Scraping Opt-Out](https://www.theverge.com/tech/1023763/openai-google-microsoft-ai-scraping-standard-opt-out) ⭐️ 9.0/10

Major AI companies including OpenAI, Google, Microsoft, and Anthropic have announced their adoption of a new, unified standard that allows publishers to opt out of AI content scraping. This new standard enables publishers to set their AI training preferences once, applying them across multiple AI companies. This initiative is significant as it represents a unified industry-wide effort to address ethical concerns regarding data usage and content rights in AI training. It provides content creators with more control over how their intellectual property is used by large language models, potentially fostering a more equitable AI ecosystem. The new standard utilizes a shared "policy token" signal, specifically identified as `__usage_ai-training`, which is detailed in an Internet-Draft titled "Machine-Readable Training Preference Signal" published on October 30, 2026, and authored by Kevin Kelley of Anthropic. This token allows for machine-readable communication of content usage preferences.

rss · The Verge Tech · 10월30일 20:26

**배경 지식**: AI content scraping refers to the automated extraction of vast amounts of text, images, and other data from websites to train large language models and other AI systems. Publishers often express concerns about this practice, as their content, which represents significant intellectual property, is used without explicit permission or compensation, raising questions about copyright and fair use. This new standard aims to provide a standardized mechanism for publishers to signal their preferences regarding this data collection.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://signal.org/legal/">Signal >> Terms of Service & Privacy Policy SignalR authentication and authorization | Microsoft Learn OpenAI, Google, Microsoft, Anthropic back __usage_ai-training ... Signal >> Documentation DeFi Token Metric Tracker (Price, TVL & more) | TokenSignal.io Token (railway signalling) - Wikipedia</a></li>

</ul>
</details>

**태그**: `#AI`, `#Data Governance`, `#Content Rights`, `#Industry Standards`, `#AI Ethics`

---

<a id="item-6"></a>
## [My favourite PowerMac is a Nintendo Wii](https://virtuallyfun.com/2026/10/29/my-favourite-powermac-is-a-nintendo-wii/) ⭐️ 8.0/10

The content explores the technical feasibility and nostalgic appeal of running classic Mac OS on a Nintendo Wii, showcasing the vibrant community around console modding and retrocomputing.

hackernews · DHowett · 10월30일 17:25 · [커뮤니티 토론](https://news.ycombinator.com/item?id=50307190)

**태그**: `#Retrocomputing`, `#Hardware Hacking`, `#Emulation`, `#Nintendo Wii`, `#Classic Mac OS`

---

<a id="item-7"></a>
## [Florilegium: Procedural Flowers in LaTeX](https://github.com/kevinraymond/florilegium) ⭐️ 7.0/10

This project, "Florilegium," offers a beautiful and novel method for procedurally generating diverse flower designs directly within LaTeX, sparking community discussion on its aesthetic appeal, technical ingenuity, and potential for AI-driven extensions.

hackernews · nanna · 10월30일 15:48 · [커뮤니티 토론](https://news.ycombinator.com/item?id=50305637)

**태그**: `#LaTeX`, `#Procedural Generation`, `#Generative Art`, `#Computer Graphics`, `#AI Applications`

---

<a id="item-8"></a>
## [Sam Altman says it’s better for RAM to be in a data center than on your desk](https://www.theverge.com/ai-artificial-intelligence/1023820/sam-altman-ram-shortage-cloud-servers) ⭐️ 7.0/10

OpenAI CEO Sam Altman suggested that RAM is more effectively used in data centers than in personal computers, amidst ongoing supply chain shortages.

rss · The Verge Tech · 10월30일 20:48

**태그**: `#AI`, `#Cloud Computing`, `#Data Centers`, `#Hardware`, `#Industry Trends`

---

<a id="item-9"></a>
## [Exclusive details about Akai’s MPC Sample Key](https://www.theverge.com/gadgets/1023649/akai-mpc-sample-key-exclusive) ⭐️ 5.0/10

Akai is set to release a new MPC Sample Key music production device with open-source software, with The Verge providing exclusive images ahead of its official launch and pricing details.

rss · The Verge Tech · 10월30일 21:01

**태그**: `#Music Technology`, `#Open Source`, `#Hardware`, `#Product Announcement`, `#Consumer Electronics`

---