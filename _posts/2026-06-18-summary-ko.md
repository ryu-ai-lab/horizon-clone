---
layout: default
title: "Horizon Summary: 2026-06-18"
date: 2026-06-18
lang: ko
---

> 50개의 콘텐츠 중 8개의 중요한 정보가 선별되었습니다.

---

1. [Researcher Uncovers 10,000 GitHub Repositories Distributing Trojan Malware](#item-1) ⭐️ 9.0/10
2. [CS 6120: Advanced Compilers: The Self-Guided Online Course (2020)](#item-2) ⭐️ 8.0/10
3. [Hospitals and universities repurposing drugs at lower cost](#item-3) ⭐️ 8.0/10
4. [Noam Shazeer, Transformer Co-Author and Gemini Co-Lead, Reportedly Joins OpenAI](#item-4) ⭐️ 8.0/10
5. [Ubiquiti Launches Enterprise NAS with ZFS](#item-5) ⭐️ 8.0/10
6. [Swiss Parliament Lifts Ban on New Nuclear Power Plants](#item-6) ⭐️ 7.0/10
7. [Snap’s Specs look good on nobody](#item-7) ⭐️ 6.0/10
8. [This robotic self-driving toilet comes to you](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Researcher Uncovers 10,000 GitHub Repositories Distributing Trojan Malware](https://orchidfiles.com/github-repositories-distributing-malware/) ⭐️ 9.0/10

A researcher has identified approximately 10,000 GitHub repositories actively distributing Trojan malware, posing a significant and widespread supply chain security threat to developers and organizations. These malicious repositories often clone legitimate projects and inject harmful code, making them difficult to distinguish from genuine sources. This discovery highlights a critical vulnerability in the software supply chain, as developers unknowingly incorporating these compromised dependencies could introduce malware into their projects and, subsequently, into their users' systems. The sheer scale of 10,000 repositories indicates a sophisticated and pervasive attack vector that could lead to widespread infections and data breaches. The attackers primarily target new repositories rather than highly popular ones, frequently deleting and pushing new commits every few hours to appear high in "Last Updated" searches and evade detection. This strategy is designed to target automated agents that add dependencies, aiming to initiate new infection clusters through a fraction of searches.

hackernews · theorchid · 6월18일 11:45 · [커뮤니티 토론](https://news.ycombinator.com/item?id=48583928)

**배경 지식**: Trojan malware is a type of malicious software that disguises itself as legitimate software, tricking users into installing it and allowing attackers to gain unauthorized access or control over their systems. A software supply chain attack exploits vulnerabilities in the development or distribution process of software components, allowing attackers to inject malicious code into a widely used dependency, which then propagates to all applications that incorporate it.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Supply_chain_attack">Supply chain attack - Wikipedia</a></li>
<li><a href="https://www.cloudflare.com/learning/security/what-is-a-supply-chain-attack/">What is a supply chain attack?</a></li>

</ul>
</details>

**커뮤니티 토론**: Community members confirmed experiencing similar malicious activities, with their legitimate repositories being cloned or used to distribute malware. Discussions provided insights into attacker tactics, suggesting they target new repositories and frequently update commits to appear in automated dependency searches rather than human review. One user also shared an anecdote about an engineer unknowingly downloading a malicious AI tool from GitHub, highlighting the real-world impact of such supply chain attacks.

**태그**: `#Malware`, `#GitHub`, `#Supply Chain Security`, `#Cybersecurity`, `#Open Source`

---

<a id="item-2"></a>
## [CS 6120: Advanced Compilers: The Self-Guided Online Course (2020)](https://www.cs.cornell.edu/courses/cs6120/2025fa/self-guided/) ⭐️ 8.0/10

Cornell University offers a free, self-guided online course on advanced compilers (CS 6120) that covers fundamental and advanced topics in compiler design, available for public access.

hackernews · ibobev · 6월18일 11:04 · [커뮤니티 토론](https://news.ycombinator.com/item?id=48583606)

**태그**: `#Compilers`, `#Computer Science Education`, `#Online Course`, `#Systems Programming`, `#Programming Languages`

---

<a id="item-3"></a>
## [Hospitals and universities repurposing drugs at lower cost](https://www.kcl.ac.uk/news/hospitals-and-universities-repurposing-drugs-at-90-lower-cost) ⭐️ 8.0/10

Hospitals and universities are successfully repurposing existing drugs for new treatments at significantly lower costs, addressing issues like high drug prices and lack of pharmaceutical incentive for rare diseases, as highlighted by community discussions on systemic industry problems.

hackernews · giuliomagnifico · 6월18일 10:33 · [커뮤니티 토론](https://news.ycombinator.com/item?id=48583386)

**태그**: `#Drug Repurposing`, `#Healthcare Economics`, `#Pharmaceutical Policy`, `#Medical Innovation`

---

<a id="item-4"></a>
## [Noam Shazeer, Transformer Co-Author and Gemini Co-Lead, Reportedly Joins OpenAI](https://twitter.com/NoamShazeer/status/2067400851438932297) ⭐️ 8.0/10

Noam Shazeer, a key figure in AI research known for co-authoring the seminal 'Attention Is All You Need' paper and previously serving as a co-lead for Google's Gemini project, is reportedly joining OpenAI. This move represents a significant talent shift in the highly competitive AI industry, potentially strengthening OpenAI's research capabilities and influencing the future direction of large language model development. Shazeer's career includes a long tenure at Google, co-founding Character.AI, a brief return to Google as a Gemini co-lead, and his foundational work on the Transformer architecture, which underpins most modern large language models.

hackernews · lukasgross · 6월18일 00:26 · [커뮤니티 토론](https://news.ycombinator.com/item?id=48578913)

**배경 지식**: The 'Attention Is All You Need' paper, published in 2017, introduced the Transformer architecture, a novel neural network design that revolutionized sequence-to-sequence tasks, particularly in natural language processing. This architecture, which relies heavily on a mechanism called 'self-attention,' became the foundation for large language models (LLMs) like GPT-3 and Gemini, enabling their advanced capabilities in understanding and generating human-like text.

**커뮤니티 토론**: The community views this as a major event, comparing AI hiring to sports free agency due to the high-profile movement of key researchers like Shazeer. Discussions highlight his extensive career trajectory, from his foundational work on the 'Attention Is All You Need' paper to his recent role as a Gemini co-lead, and note his significant contributions to the field.

**태그**: `#AI Research`, `#Large Language Models`, `#Talent Mobility`, `#OpenAI`, `#Google`

---

<a id="item-5"></a>
## [Ubiquiti Launches Enterprise NAS with ZFS](https://blog.ui.com/article/introducing-enterprise-nas) ⭐️ 8.0/10

Ubiquiti has introduced a new Enterprise Network Attached Storage (NAS) solution, which is notably built upon the ZFS file system. This new offering aims to provide robust storage capabilities for enterprise environments. This launch is significant as it brings a ZFS-powered NAS to the enterprise market from a company known for its networking infrastructure, potentially offering a cost-effective alternative to existing solutions. However, the community's critical evaluation of Ubiquiti's software quality and security record raises concerns about its true suitability for enterprise deployments. The new Enterprise NAS features ZFS, a file system known for its data integrity and advanced features, and includes dual 25 Gigabit SFP28 ports and redundant power supplies for resilience. A key selling point for Ubiquiti products, including this NAS, is its no monthly recurring cost (MRR) model.

hackernews · ksec · 6월18일 14:24 · [커뮤니티 토론](https://news.ycombinator.com/item?id=48585866)

**배경 지식**: ZFS is an advanced file system and logical volume manager known for its data integrity features like checksumming, snapshotting, and copy-on-write. It is widely regarded for its robustness and scalability in storage solutions. NAS (Network Attached Storage) refers to a dedicated file storage device connected to a network, allowing multiple users and client devices to retrieve data from centralized disk capacity.

**커뮤니티 토론**: The community expresses significant concerns regarding Ubiquiti's historical software quality, security vulnerabilities (e.g., AWS root key access, misrepresentation of encryption, camera feed access issues), and overall suitability for enterprise environments, despite appreciating the no-MRR model and the technical merits of ZFS. Some users also question the ability of spinning drives to saturate 25 Gigabit links, even with ZFS optimizations.

**태그**: `#Enterprise Storage`, `#ZFS`, `#Ubiquiti`, `#Network Infrastructure`, `#Software Security`

---

<a id="item-6"></a>
## [Swiss Parliament Lifts Ban on New Nuclear Power Plants](https://www.bluewin.ch/en/news/switzerland/parliament-lifts-ban-on-new-nuclear-power-plants-3257535.html) ⭐️ 7.0/10

The Swiss parliament has voted to lift the ban on new nuclear power plants, a significant policy shift that still requires approval through a public referendum. This decision reopens the possibility for Switzerland to consider nuclear energy as part of its future power generation strategy. This move is significant as it could fundamentally alter Switzerland's energy landscape, potentially addressing its seasonal energy supply issues and contributing to decarbonization goals. It also reignites a global debate on the role of nuclear power in achieving energy security and climate targets amidst rising energy demands. While the parliament has approved the lifting of the ban, the decision is not final and must pass a public referendum, where significant opposition from left-leaning and green parties is expected. The debate highlights ongoing challenges in achieving informed public discourse on complex energy topics, including the economics and waste management of nuclear power.

hackernews · leonidasrup · 6월18일 14:17 · [커뮤니티 토론](https://news.ycombinator.com/item?id=48585746)

**배경 지식**: Switzerland previously decided to phase out nuclear power following the Fukushima disaster in 2011, with a ban on new plants enacted in 2017. The country faces a "summer/winter energy problem," with abundant hydropower in spring/summer but less energy production in winter, leading to reliance on imports.

**커뮤니티 토론**: The community discussion reveals a polarized debate, with some emphasizing the necessity of a public referendum and expressing skepticism about informed discourse, while others champion nuclear energy, especially Small Modular Reactors (SMRs), as the future. There's also frustration over perceived misinformation regarding nuclear costs and waste, with some arguing that nuclear power is unfairly deemed expensive and its waste problems exaggerated.

**태그**: `#Nuclear Energy`, `#Energy Policy`, `#Switzerland`, `#Sustainability`, `#Public Debate`

---

<a id="item-7"></a>
## [Snap’s Specs look good on nobody](https://www.theverge.com/podcast/952126/snap-specs-ar-glasses-vergecast) ⭐️ 6.0/10

Snap has released new, technically impressive AR smart glasses that are compact and feature-rich, but come with a high price tag and potential aesthetic drawbacks.

rss · The Verge Tech · 6월18일 19:15

**태그**: `#Augmented Reality`, `#Smart Glasses`, `#Wearable Technology`, `#Consumer Electronics`, `#Snap`

---

<a id="item-8"></a>
## [This robotic self-driving toilet comes to you](https://www.theverge.com/tech/952441/yueban-xiaoban-self-driving-autonomous-toilet) ⭐️ 6.0/10

A Chinese company has unveiled an autonomous, self-driving toilet designed to improve accessibility for individuals with mobility issues, allowing the toilet to come to the user.

rss · The Verge Tech · 6월18일 18:08

**태그**: `#Robotics`, `#Assistive Technology`, `#Elderly Care`, `#Autonomous Systems`, `#Product Innovation`

---