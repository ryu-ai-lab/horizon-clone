---
layout: default
title: "Horizon Summary: 2026-06-17 (KO)"
date: 2026-06-17
lang: ko
---

> 64개의 콘텐츠 중 8개의 중요한 정보가 선별되었습니다.

---

1. [Lore: Open-Source Version Control System for Game Development](#item-1) ⭐️ 9.0/10
2. [GLM-5.2 is the new leading open weights model on Artificial Analysis](#item-2) ⭐️ 9.0/10
3. [U.S. science is in chaos](#item-3) ⭐️ 9.0/10
4. [RFC 10008 Proposes New HTTP QUERY Method for Idempotent, Cacheable Requests with Body](#item-4) ⭐️ 9.0/10
5. [Volkswagen Blocks GrapheneOS Users and Non-Play Protect Devices from Car Apps](#item-5) ⭐️ 8.0/10
6. [US Delays Blacklisting DeepSeek Amid Security Concerns for Over 100 Firms](#item-6) ⭐️ 8.0/10
7. [Apple to Raise Product Prices Due to "Unsustainable" RAM Expenses](#item-7) ⭐️ 8.0/10
8. [VSCO launches Studio Pro mobile photo editing app and plans $500 per year subscription](#item-8) ⭐️ 5.0/10

---

<a id="item-1"></a>
## [Lore: Open-Source Version Control System for Game Development](https://lore.org/) ⭐️ 9.0/10

Lore, previously known as Unreal Revision Control and used in UEFN, has been open-sourced by Epic Games under an MIT license. This new version control system is specifically designed for game development and managing large binary assets, aiming to provide a scalable alternative to proprietary solutions like Perforce where Git falls short. This is significant because it offers a much-needed open-source challenger in the game development industry, which heavily relies on proprietary systems like Perforce due to Git's limitations with large binary files and asset management. Its availability could foster innovation and reduce reliance on costly commercial tools for managing complex game projects. Lore, formerly Unreal Revision Control, was the built-in version control system for UEFN (Unreal Editor for Fortnite) and is seeing progressive adoption by internal Epic teams. It is designed with features like file locking, permissions, and large project support, which are crucial for game development, and is released under an MIT license.

hackernews · regnerba · 6월17일 14:30 · [커뮤니티 토론](https://news.ycombinator.com/item?id=48571081)

**배경 지식**: Version control systems (VCS) track changes to files over time, allowing multiple users to collaborate and revert to previous versions. While Git excels with text-based code, it struggles with large binary files (like game textures or 3D models) due to its distributed nature and how it handles diffs, leading to performance issues and large repository sizes. Perforce (Helix Core) is a centralized VCS widely adopted in game development for its robust handling of large files, granular permissions, and exclusive file locking, which are critical for managing game assets.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://epicgames.github.io/lore/explanation/system-design/">The Lore Version Control System - Lore Developer Documentation</a></li>
<li><a href="https://github.com/EpicGames/lore">GitHub - EpicGames/ lore : Lore is a next-generation, open source...</a></li>
<li><a href="https://www.phoronix.com/news/Epic-Games-Lore-VCS">Epic Games Announces Lore Open-Source Version Control System</a></li>
<li><a href="https://www.perforce.com/products/helix-core">Perforce P4: Version Control that Scales With Your Team</a></li>

</ul>
</details>

**커뮤니티 토론**: The community emphasizes that Lore is a Perforce competitor for game development, not a general Git replacement, highlighting Git's inadequacy for binary assets and Perforce's strengths like file locking. Some noted Git's user-unfriendly UI, while others pointed out that Lore isn't entirely new but an open-sourced version of Unreal Revision Control, making it particularly promising for Unreal game development.

**태그**: `#Version Control`, `#Game Development`, `#Open Source`, `#Scalability`, `#Asset Management`

---

<a id="item-2"></a>
## [GLM-5.2 is the new leading open weights model on Artificial Analysis](https://artificialanalysis.ai/articles/glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index) ⭐️ 9.0/10

GLM-5.2 has emerged as the top-performing open-weights model on Artificial Analysis, offering performance comparable to leading proprietary models like Opus at a fraction of the cost, potentially disrupting the AI market.

hackernews · himata4113 · 6월17일 09:12 · [커뮤니티 토론](https://news.ycombinator.com/item?id=48567759)

**태그**: `#Large Language Models`, `#Open Source AI`, `#AI Benchmarking`, `#AI Economics`, `#Machine Learning`

---

<a id="item-3"></a>
## [U.S. science is in chaos](https://www.scientificamerican.com/article/americas-compact-between-science-and-politics-is-broken/) ⭐️ 9.0/10

The article and community discussion reveal a severe crisis in U.S. scientific research, characterized by funding shortages, visa restrictions, and a significant exodus of talent, signaling a broken compact between science and politics.

hackernews · presspot · 6월17일 09:54 · [커뮤니티 토론](https://news.ycombinator.com/item?id=48568058)

**태그**: `#Science Policy`, `#Research Funding`, `#Academia`, `#Brain Drain`, `#US Politics`

---

<a id="item-4"></a>
## [RFC 10008 Proposes New HTTP QUERY Method for Idempotent, Cacheable Requests with Body](https://www.rfc-editor.org/info/rfc10008/) ⭐️ 9.0/10

RFC 10008 introduces the new HTTP QUERY method, which is specifically designed to handle idempotent and cacheable requests that necessitate a request body. This proposal represents a significant architectural addition to HTTP, potentially changing how complex, idempotent, and cacheable requests with bodies are managed across the web. The QUERY method is specifically designed to be idempotent and cacheable while allowing a request body, a functionality previously considered for GET but rejected due to interoperability issues and HTTP architectural principles.

hackernews · schappim · 6월17일 10:51 · [커뮤니티 토론](https://news.ycombinator.com/item?id=48568502)

**배경 지식**: HTTP methods like GET and POST define how clients interact with web resources; GET is typically used for retrieving data, is idempotent and cacheable, but traditionally lacks a request body, while POST sends data with a body but is neither idempotent nor cacheable by default. The new QUERY method addresses the gap for requests that need both a body for complex queries and the benefits of idempotency and caching.

**커뮤니티 토론**: The community discussion highlights concerns regarding the practical implications of QUERY, particularly how caching would work with potentially large and complex request bodies, and the challenge of defining a general caching strategy. There's also curiosity about its potential integration with HTML forms to leverage its idempotent nature and avoid resubmission warnings, alongside observations on the historical context of GET requests with bodies.

**태그**: `#HTTP`, `#Web Standards`, `#Networking`, `#Protocol Design`, `#RFC`

---

<a id="item-5"></a>
## [Volkswagen Blocks GrapheneOS Users and Non-Play Protect Devices from Car Apps](https://discuss.grapheneos.org/d/35949-volkswagen-app?page=3) ⭐️ 8.0/10

Volkswagen has reportedly begun blocking users of the privacy-focused GrapheneOS from accessing its car applications and has implemented a broader API lockdown for all non-Play Protect certified devices. This move effectively disables existing community-driven integrations and limits user control over their vehicle data. This action signifies a growing trend of vendor lock-in in the automotive industry, restricting user choice and privacy by limiting access to essential car functionalities to specific, certified device ecosystems. It could stifle innovation from third-party developers and reduce consumer control over their own vehicle data and smart home integrations. The blocking extends beyond GrapheneOS to encompass any device not certified by Google Play Protect, effectively shutting down all community-driven projects that previously offered enhanced functionality. Users report that Volkswagen's official app is feature-poor and heavily laden with advertisements, making the loss of third-party integrations particularly impactful.

hackernews · microtonal · 6월17일 15:04 · [커뮤니티 토론](https://news.ycombinator.com/item?id=48571526)

**배경 지식**: GrapheneOS is a privacy and security-hardened open-source mobile operating system based on Android, designed to enhance user privacy and security by minimizing Google's influence and offering robust protections. Google Play Protect certified devices, on the other hand, are Android devices that have passed Google's compatibility tests and are licensed to include Google's proprietary apps, ensuring a baseline level of security and compatibility with the Google Play ecosystem. Volkswagen's new policy restricts its car app access only to these certified devices.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://www.android.com/certified/">Android – Certified</a></li>
<li><a href="https://support.google.com/googleplay/answer/7165974?hl=en">Check & fix Play Protect certification status - Google Play Help</a></li>

</ul>
</details>

**커뮤니티 토론**: The community expresses strong disappointment and frustration with Volkswagen's decision, viewing it as a significant step backward for user freedom and privacy. Many users, including potential car buyers, are reconsidering Volkswagen purchases due to the loss of valuable community-driven integrations like Home Assistant, which they found superior to the official, ad-heavy app. There's a broader concern about vendor lock-in and the increasing lack of control over personal vehicles and data.

**태그**: `#Privacy`, `#Mobile Security`, `#Vendor Lock-in`, `#Automotive Tech`, `#API Policy`

---

<a id="item-6"></a>
## [US Delays Blacklisting DeepSeek Amid Security Concerns for Over 100 Firms](https://www.reuters.com/world/china/us-holds-off-blacklisting-chinas-deepseek-more-than-100-firms-deemed-security-2026-06-17/) ⭐️ 8.0/10

The U.S. has temporarily decided not to add Chinese AI company DeepSeek to its trade blacklist, even as it identified over 100 other firms as posing security risks. This decision highlights the complex geopolitical considerations in the global AI sector. This decision is significant as it reflects the ongoing geopolitical tensions and economic competition between the U.S. and China in the critical AI sector, potentially influencing global AI market dynamics and supply chain strategies. It also underscores the U.S.'s nuanced approach to managing security risks while navigating economic implications. DeepSeek is notable for its aggressive pricing, charging significantly less per million output tokens compared to competitors like Fable and GPT-5.5, which raises questions about its business model and market impact. While the U.S. held off on blacklisting DeepSeek, other Chinese AI firms like Z.ai (maker of GLM 5.2) have already been on the Entity List, which primarily restricts U.S. companies from selling goods and services to them.

hackernews · giuliomagnifico · 6월17일 03:55 · [커뮤니티 토론](https://news.ycombinator.com/item?id=48565498)

**배경 지식**: The U.S. government uses various tools, such as the Entity List, to restrict trade with foreign companies deemed to pose national security risks or be involved in activities contrary to U.S. foreign policy interests. Inclusion on this list typically means American firms need a license to export certain technologies or goods to the listed entity, a measure frequently employed in the ongoing technological and economic rivalry between the U.S. and China, particularly concerning advanced sectors like artificial intelligence.

**커뮤니티 토론**: The community discussion reveals a mix of perspectives, with some users highlighting the existing Entity List restrictions on other Chinese AI firms like Z.ai and questioning the effectiveness of such measures given China's limited reliance on U.S. goods beyond restricted GPUs. Others express concern about the geopolitical implications of Chinese LLMs, suggesting they could be used to influence Western opinions and promote the use of Chinese servers, while also noting DeepSeek's remarkably low pricing as a significant competitive factor.

**태그**: `#AI Policy`, `#Geopolitics`, `#US-China Tech Rivalry`, `#AI Ethics & Security`, `#Large Language Models`

---

<a id="item-7"></a>
## [Apple to Raise Product Prices Due to "Unsustainable" RAM Expenses](https://www.theverge.com/tech/951948/apple-tim-cook-price-increases-ram) ⭐️ 8.0/10

Apple CEO Tim Cook announced that the company will raise product prices, stating that "price increases are unavoidable" due to the ongoing memory shortage and "unsustainable" RAM expenses. Apple is attempting to mitigate the significant cost increases passed on to them and shield customers. This announcement from a major tech company CEO signals a direct impact on consumers through higher product costs and reflects broader industry trends of component shortages and inflationary pressures affecting the global supply chain. It could set a precedent for other manufacturers facing similar challenges. Tim Cook explicitly stated in an interview with The Wall Street Journal that "price increases are unavoidable," indicating that Apple has exhausted its options to absorb the rising costs of RAM. The company has been trying to shield customers from these increases but can no longer do so fully.

rss · The Verge Tech · 6월17일 21:42

**배경 지식**: RAM (Random Access Memory) is a crucial component in computers and mobile devices, providing temporary storage for data that the CPU actively uses, enabling multitasking and faster performance. A "memory shortage" refers to a situation where the supply of these essential components cannot meet the global demand, often leading to increased prices and production delays across the electronics industry.

**태그**: `#Apple`, `#Price Increase`, `#Supply Chain`, `#Memory Shortage`, `#Consumer Electronics`

---

<a id="item-8"></a>
## [VSCO launches Studio Pro mobile photo editing app and plans $500 per year subscription](https://www.theverge.com/tech/951863/vsco-studio-pro-vsco-one-subscription) ⭐️ 5.0/10

VSCO has launched Studio Pro, a new mobile photo editing app for iOS (with macOS planned) featuring batch editing and style matching, aiming to compete with Adobe with a high annual subscription.

rss · The Verge Tech · 6월17일 20:43

**태그**: `#Photo Editing`, `#Mobile Apps`, `#Creative Tools`, `#Software Industry`, `#Subscription Model`

---