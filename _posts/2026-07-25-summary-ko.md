---
layout: default
title: "Horizon Summary: 2026-07-25"
date: 2026-07-25
lang: ko
---

> 43개의 콘텐츠 중 6개의 중요한 정보가 선별되었습니다.

---

1. [Anthropic Releases Claude Opus 5 with Enhanced Performance and No Data Retention](#item-1) ⭐️ 9.0/10
2. [Security Camera Shipped with GitHub Admin Token and US DoD IPs](#item-2) ⭐️ 9.0/10
3. [Nvidia, Microsoft, Meta warn against overregulating open-weight models](#item-3) ⭐️ 9.0/10
4. [If coding has been solved, why does software keep getting worse?](#item-4) ⭐️ 9.0/10
5. [Half-Life 2 Runs Natively on HaikuOS](#item-5) ⭐️ 8.0/10
6. [Midjourney Acquires Astrology App Co-Star](#item-6) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Anthropic Releases Claude Opus 5 with Enhanced Performance and No Data Retention](https://www.anthropic.com/news/claude-opus-5) ⭐️ 9.0/10

Anthropic has launched Claude Opus 5, a significant update to its AI model, demonstrating improved performance in tasks such as image-to-HTML conversion and implementing a critical policy of no data retention for general access. This new version aims to enhance its appeal, particularly for enterprise use cases. This release is significant as Claude Opus is a leading AI model, and its performance improvements, especially in specialized tasks, combined with a no-data-retention policy, make it highly attractive for enterprise adoption where data privacy is paramount. It addresses a key concern for businesses looking to integrate advanced AI without compromising sensitive information. Claude Opus 5 shows superior accuracy in image-to-HTML conversion compared to previous top models like Fable and Gemini 3.1 Pro, better adhering to design source truth. Crucially, it maintains a no-data-retention policy for general access, a key differentiator for enterprise clients concerned about data privacy.

hackernews · alvis · 7월24일 16:57 · [커뮤니티 토론](https://news.ycombinator.com/item?id=49038433)

**배경 지식**: Image-to-HTML conversion is the process of using AI to generate HTML and CSS code from an image, such as a screenshot or design mock-up. This technology aims to automate the front-end development process, allowing designers and developers to quickly convert visual designs into functional web pages. AI models recognize UI patterns, elements, and layouts within an image to produce clean, responsive code.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://fronty.com/">Image to HTML CSS converter . Convert image to HTML CSS with...</a></li>
<li><a href="https://ui2code.ai/image-to-html">Image to HTML - Convert Images to Responsive... | UI2CODE. AI</a></li>

</ul>
</details>

**커뮤니티 토론**: The community largely praises Claude Opus 5, particularly highlighting its superior image-to-HTML conversion capabilities and, most importantly, its no-data-retention policy for general access, which is seen as a critical advantage for enterprise adoption over competitors like Fable. Some users also discuss the broader challenges of assessing AI intelligence beyond simple tasks and the increasing complexity of managing diverse LLM offerings.

**태그**: `#AI`, `#Large Language Models`, `#Anthropic`, `#Machine Learning`, `#Enterprise AI`

---

<a id="item-2"></a>
## [Security Camera Shipped with GitHub Admin Token and US DoD IPs](https://hhh.hn/hanwha-github-token/) ⭐️ 9.0/10

A security researcher discovered a GitHub admin token embedded in the login page JavaScript of a Hanwha Wisenet XNP-9300RW security camera. Community discussion further revealed the presence of US Department of War IP addresses hardcoded into the camera's firmware, indicating a severe supply chain vulnerability. This incident exposes critical supply chain security flaws in widely adopted IoT devices, raising significant concerns about potential espionage or severe negligence in product development. The presence of such sensitive credentials and IP addresses could grant unauthorized access to critical systems or facilitate surveillance, impacting national security and user privacy. The GitHub admin token was found within client-side JavaScript on the camera's login page, while the US Department of War IP addresses were discovered directly baked into the device's firmware. This dual discovery suggests either extreme developer oversight or a deliberate, potentially malicious, inclusion, posing significant national security and data integrity risks.

hackernews · hhh · 7월24일 11:54 · [커뮤니티 토론](https://news.ycombinator.com/item?id=49034292)

**배경 지식**: A GitHub token is a credential used for authenticating to GitHub's API or command line, often for automation in workflows. An "admin token" typically implies broad permissions, and its compromise could grant an attacker extensive control over an organization's repositories and data. IoT devices, such as security cameras, often contain embedded firmware that can hold critical configuration data, and vulnerabilities in this firmware can expose sensitive information or create backdoors.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://daily.dev/posts/my-security-camera-shipped-a-github-admin-token-in-its-login-page-hpbnugrql">My security camera shipped a GitHub admin token in its...</a></li>
<li><a href="https://docs.github.com/en/actions/concepts/security/github_token">GITHUB_TOKEN - GitHub Docs</a></li>

</ul>
</details>

**커뮤니티 토론**: The community expressed strong concerns, particularly regarding the US Department of War IP addresses, with some commenters suggesting avoiding security products from the manufacturer's country. Discussions also highlighted the widespread poor security practices among IoT vendors, the desire for open firmware options, and practical advice like isolating cameras on separate VLANs without internet access.

**태그**: `#Cybersecurity`, `#IoT Security`, `#Supply Chain Security`, `#Vulnerability`

---

<a id="item-3"></a>
## [Nvidia, Microsoft, Meta warn against overregulating open-weight models](https://www.cnbc.com/2026/07/24/nvidia-microsoft-meta-open-weight-ai-models.html) ⭐️ 9.0/10

Nvidia, Microsoft, and Meta have issued a joint letter warning against overregulation of open-weight AI models, taking a public stance in the ongoing industry debate about AI governance and open-source development.

hackernews · louiereederson · 7월24일 13:32 · [커뮤니티 토론](https://news.ycombinator.com/item?id=49035303)

**태그**: `#AI Policy`, `#Open Source AI`, `#AI Regulation`, `#Tech Industry`, `#Large Language Models`

---

<a id="item-4"></a>
## [If coding has been solved, why does software keep getting worse?](https://ptrchm.com/posts/nothing-works-and-everyone-is-euphoric/) ⭐️ 9.0/10

The content explores the paradox of declining software quality despite advancements in coding, prompting a community discussion on user frustration with updates, the impact of AI on development speed versus correctness, and fundamental issues in system design and user experience.

hackernews · pchm · 7월24일 09:08 · [커뮤니티 토론](https://news.ycombinator.com/item?id=49033004)

**태그**: `#Software Quality`, `#Software Engineering`, `#User Experience`, `#AI in Development`, `#Industry Trends`

---

<a id="item-5"></a>
## [Half-Life 2 Runs Natively on HaikuOS](https://discuss.haiku-os.org/t/haiku-nvidia-porting-nvidia-driver-for-turing-gpus/16520?page=18) ⭐️ 8.0/10

Half-Life 2 has been successfully ported to run natively on HaikuOS, demonstrating the operating system's progress in graphics and application compatibility. This achievement highlights the dedicated efforts of the Haiku community in advancing the OS's capabilities. This port is a significant technical milestone for HaikuOS, a niche operating system, as it showcases its growing capabilities in handling demanding applications and advanced graphics. It underscores the vitality and technical prowess of its dedicated open-source community. The port appears to be based on the nillerusr Source engine, which itself is derived from a 2020 leak of the Source engine's source code. Community member X512 is highlighted as a key contributor, having also worked on NVIDIA, AMD Vulkan drivers, and ARM platform ports for HaikuOS.

hackernews · m0do1 · 7월24일 12:53 · [커뮤니티 토론](https://news.ycombinator.com/item?id=49034868)

**배경 지식**: HaikuOS is a free and open-source operating system for personal computers, serving as a community-driven continuation and reimplementation of the defunct BeOS. It aims for binary compatibility with BeOS while developing its own modern components. Its development is largely fueled by a dedicated volunteer community focused on creating a fast, efficient, and user-friendly system.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Haiku_(operating_system)">Haiku (operating system) - Wikipedia</a></li>
<li><a href="https://www.haiku-os.org/about/">What is Haiku? | Haiku Project</a></li>

</ul>
</details>

**커뮤니티 토론**: The community expresses strong appreciation for developer X512's extensive contributions to HaikuOS, including graphics drivers and ARM platform support. Discussions also reveal that the port likely utilizes the nillerusr Source engine, based on a 2020 leak, and some users acknowledge Haiku's technical prowess while noting concerns about its user experience compared to other operating systems.

**태그**: `#HaikuOS`, `#Game Porting`, `#Operating Systems`, `#Systems Programming`, `#Graphics Drivers`

---

<a id="item-6"></a>
## [Midjourney Acquires Astrology App Co-Star](https://www.theverge.com/ai-artificial-intelligence/970894/midjourney-co-star-acquisition) ⭐️ 7.0/10

Midjourney, a prominent AI image generation company, announced its acquisition of Co-Star, a personalized astrology app, on Thursday. This move signals a potential expansion beyond its core AI image generation capabilities into new application areas. This acquisition is significant as it indicates Midjourney's potential strategic shift and expansion into new, perhaps unexpected, application areas for AI beyond image generation. It could pave the way for innovative uses of AI in personalized content or lifestyle services, impacting the broader AI industry's direction. Co-Star is a free app known for offering daily horoscopes and personalized astrology readings, while Midjourney has evolved from generating AI cat images to more complex tasks like full-body ultrasound scans. The acquisition was first reported by Bloomberg before Midjourney's official announcement.

rss · The Verge Tech · 7월24일 19:06

**태그**: `#AI`, `#Acquisitions`, `#Industry News`, `#Business Strategy`, `#Midjourney`

---