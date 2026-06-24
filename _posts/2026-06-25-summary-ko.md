---
layout: default
title: "Horizon Summary: 2026-06-25"
date: 2026-06-25
lang: ko
---

> 53개의 콘텐츠 중 9개의 중요한 정보가 선별되었습니다.

---

1. [OpenAI Unveils Broadcom-Built Custom AI Inference Chip](#item-1) ⭐️ 9.0/10
2. [Krea 2: SOTA open-weights 12B image model](#item-2) ⭐️ 9.0/10
3. [Bunny.net Makes Bunny DNS Service Completely Free for Up to 500 Domains](#item-3) ⭐️ 8.0/10
4. [John Carmack Reflects on Early id Software Leadership Mistakes](#item-4) ⭐️ 8.0/10
5. [RubyLLM: A Unified Ruby Framework for Major AI Providers](#item-5) ⭐️ 8.0/10
6. [Stealing Is a Skill](#item-6) ⭐️ 8.0/10
7. [PR spam today looks like email spam in the early 2000s](#item-7) ⭐️ 8.0/10
8. [Gemini 3.5 Flash Gains 'Computer Use,' Faces User Criticism](#item-8) ⭐️ 8.0/10
9. [astral-sh/uv released 0.11.24](#item-9) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [OpenAI Unveils Broadcom-Built Custom AI Inference Chip](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/) ⭐️ 9.0/10

OpenAI has unveiled its first custom AI inference chip, codenamed "Jalapeno," developed in partnership with Broadcom, which reportedly offers significant cost savings of approximately 50% compared to typical AI GPUs. This marks OpenAI's strategic entry into custom hardware, moving beyond reliance on off-the-shelf solutions. This development is significant as it could drastically reduce the operational costs of running large AI models, potentially democratizing access to advanced AI and challenging the dominance of existing GPU manufacturers. It signals a broader industry trend towards vertical integration and specialized hardware for AI workloads. The "Jalapeno" chip, an Application-Specific Integrated Circuit (ASIC), was reportedly developed from design to production in nine months, with manufacturing handled by TSMC. Broadcom CEO Hock Tan stated the accelerator shows roughly 50% cost savings compared to typical AI GPUs for inference tasks.

hackernews · jamdesk · 6월24일 17:47 · [커뮤니티 토론](https://news.ycombinator.com/item?id=48663324)

**배경 지식**: An AI inference chip is a specialized semiconductor designed to efficiently run trained artificial intelligence models, focusing on deploying AI rather than training it, often prioritizing low latency and high throughput at minimal cost. These chips are a type of Application-Specific Integrated Circuit (ASIC), which are integrated circuits custom-designed for a particular application, offering superior performance and efficiency for their intended task compared to general-purpose processors.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://aws.amazon.com/ai/machine-learning/inferentia/">AI Chip - Amazon Inferentia - AWS</a></li>
<li><a href="https://grokipedia.com/page/Application-specific_integrated_circuit">Application-specific integrated circuit (ASIC)</a></li>

</ul>
</details>

**커뮤니티 토론**: The community highlighted the reported 50% cost savings as a significant market disruptor, while also questioning the extent to which OpenAI's models truly accelerated the chip's design process. There was also discussion about the chip's manufacturer (TSMC) and the potential for older chip technologies (like 28nm) to still be viable for inference tasks.

**태그**: `#AI Hardware`, `#Custom Chips`, `#OpenAI`, `#Broadcom`, `#AI Inference`

---

<a id="item-2"></a>
## [Krea 2: SOTA open-weights 12B image model](https://www.krea.ai/blog/krea-2-technical-report) ⭐️ 9.0/10

Krea has released Krea 2, a state-of-the-art 12B open-weights text-to-image model, accompanied by a detailed technical report on its training, data infrastructure, and architecture, offering impressive performance and speed for locally hostable models.

hackernews · mattnewton · 6월23일 15:31 · [커뮤니티 토론](https://news.ycombinator.com/item?id=48646659)

**태그**: `#Generative AI`, `#Text-to-Image`, `#Machine Learning Models`, `#Open Source`, `#AI Infrastructure`

---

<a id="item-3"></a>
## [Bunny.net Makes Bunny DNS Service Completely Free for Up to 500 Domains](https://bunny.net/blog/were-making-bunny-dns-free/) ⭐️ 8.0/10

Bunny.net has announced that its Bunny DNS service is now completely free, eliminating all DNS query fees and offering free DNS hosting for up to 500 domains per account, which includes advanced features like smart records and health monitoring. This move significantly alters Bunny.net's service offering and intensifies competition within the DNS service market, potentially attracting users seeking cost-effective and feature-rich web infrastructure solutions, especially those looking for EU-based alternatives. The free offering includes no query limits, no per-request billing, and all critical features such as smart records and health monitoring are available without being hidden behind enterprise plans, applying to both DNS resolution and hosting for up to 500 domains.

hackernews · dabinat · 6월24일 08:50 · [커뮤니티 토론](https://news.ycombinator.com/item?id=48657030)

**배경 지식**: DNS (Domain Name System) is a foundational component of the internet, acting like a phonebook that translates human-readable domain names (e.g., example.com) into machine-readable IP addresses (e.g., 192.0.2.1). DNS services are crucial for directing web traffic, ensuring websites load correctly, and providing features like load balancing and security.

**커뮤니티 토론**: Community members praised Bunny.net for offering a competitive EU-based alternative to US cloud providers, noting their organic growth strategy. There was some initial confusion about whether the free offering applied to DNS hosting or resolution, which was clarified to include both, but concerns were raised about potential unexpected charges for other Bunny.net products due to varying billing policies across their services.

**태그**: `#DNS`, `#Cloud Services`, `#Web Infrastructure`, `#Pricing Model`, `#Bunny.net`

---

<a id="item-4"></a>
## [John Carmack Reflects on Early id Software Leadership Mistakes](https://twitter.com/ID_AA_Carmack/status/2069799283369345247) ⭐️ 8.0/10

John Carmack, co-founder of id Software, recently reflected on his early career mistakes, specifically admitting to pushing employees too hard and failing to adapt to the needs of a maturing company. This personal reflection highlights the challenges of maintaining startup intensity as a company grows. This reflection from an influential figure like Carmack offers valuable lessons on leadership, company culture, and the human cost of intense development, impacting software engineering and game development communities. It underscores the importance of employee well-being and sustainable growth over relentless pressure. Carmack specifically mentioned pushing everyone too hard and not appreciating that maturing companies require more slack than startups, leading to burnout. The discussion also touches upon the legacy of Quake and its impact on id Software's internal dynamics and future releases.

hackernews · shadowtree · 6월24일 15:56 · [커뮤니티 토론](https://news.ycombinator.com/item?id=48661825)

**배경 지식**: John Carmack is a legendary programmer and co-founder of id Software, known for pioneering 3D graphics technologies and creating iconic games like Doom and Quake. id Software was famous for its intense development cycles, often referred to as "crunch time," which pushed the boundaries of game technology but sometimes at a high personal cost to employees.

**커뮤니티 토론**: The community discussion largely agrees with Carmack's sentiment, with some pointing to specific interviews from former employees like Sandy Petersen that corroborate the intense work environment. There's a debate on whether the success of Quake justified the human cost, with some arguing its iconic status made it "worth it" despite the company's internal struggles, while others note a decline in id Software's "industry pushing energy" in later titles like Doom 3.

**태그**: `#Software Engineering`, `#Game Development`, `#Leadership`, `#Company Culture`, `#Burnout`

---

<a id="item-5"></a>
## [RubyLLM: A Unified Ruby Framework for Major AI Providers](https://rubyllm.com/) ⭐️ 8.0/10

RubyLLM has emerged as a highly-regarded Ruby framework that unifies and simplifies integration with major AI providers like GPT, Claude, and Ollama, offering a consistent interface for developers. This framework aims to provide a balance of out-of-the-box usability and flexibility for various AI tasks. This framework significantly lowers the barrier for Ruby developers to integrate large language models into their applications, fostering innovation and expanding the use of AI within the Ruby ecosystem. By providing a productive and opinionated approach similar to Rails, RubyLLM makes AI integration more accessible and efficient for the community. RubyLLM aims to balance out-of-the-box functionality with flexibility, though users have noted challenges with cache consistency for certain providers like xAI and difficulties with true trace observability. However, the responses API, which was a point of frustration, is now reportedly natively supported, addressing a key community concern.

hackernews · doener · 6월24일 14:41 · [커뮤니티 토론](https://news.ycombinator.com/item?id=48660711)

**배경 지식**: Large Language Models (LLMs) are advanced AI models capable of understanding and generating human-like text, but integrating them into applications often requires dealing with diverse APIs from different providers. Ruby is a popular, developer-friendly programming language known for its elegance and productivity, widely used for web development, especially with the Ruby on Rails framework.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://rubyllm.com/">RubyLLM | One beautiful Ruby framework for all major AI providers.</a></li>
<li><a href="https://github.com/crmne/ruby_llm">GitHub - crmne/ ruby _ llm : One delightful Ruby framework for every...</a></li>

</ul>
</details>

**커뮤니티 토론**: The community generally praises RubyLLM for its usability and ease of integration, with many finding it surprisingly good and easy to use. However, some users raised concerns about cache inconsistencies for specific providers like xAI, challenges with true trace observability, and initial lack of native support for the responses API, though this has reportedly been addressed.

**태그**: `#Ruby`, `#LLM Frameworks`, `#AI Integration`, `#Developer Tools`, `#Software Engineering`

---

<a id="item-6"></a>
## [Stealing Is a Skill](https://ben-mini.com/2026/stealing-is-a-skill) ⭐️ 8.0/10

The article's provocative title "Stealing Is a Skill" ignited a robust community discussion on the fine line between inspiration and plagiarism in design, critiquing modern web design trends and debating the true value of imitation versus original creation.

hackernews · bewal416 · 6월24일 13:08 · [커뮤니티 토론](https://news.ycombinator.com/item?id=48659165)

**태그**: `#Design Ethics`, `#Web Design`, `#Creativity`, `#Intellectual Property`, `#Product Development`

---

<a id="item-7"></a>
## [PR spam today looks like email spam in the early 2000s](https://www.greptile.com/blog/prs-on-openclaw) ⭐️ 8.0/10

The content highlights the increasing issue of pull request (PR) spam in open-source projects, comparing it to email spam from the early 2000s, and features a robust community discussion on its implications and potential solutions.

hackernews · dakshgupta · 6월24일 14:32 · [커뮤니티 토론](https://news.ycombinator.com/item?id=48660579)

**태그**: `#Open Source`, `#Software Engineering`, `#Community Management`, `#Spam`, `#GitHub`

---

<a id="item-8"></a>
## [Gemini 3.5 Flash Gains 'Computer Use,' Faces User Criticism](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/) ⭐️ 8.0/10

Google has introduced new 'computer use' capabilities for its Gemini 3.5 Flash model, aiming to enable the AI to interact with external applications and systems. This capability is a significant step towards more autonomous AI agents, but community feedback highlights substantial limitations, reliability issues, and potential overstatements in its performance, raising questions about its immediate practical utility and user trust. Users reported that the 'computer use' feature struggles with complex tasks, such as extracting data from PDFs, often giving up or inventing information, and also noted a lack of support for specific application features like MCP within the Gemini app.

hackernews · swolpers · 6월24일 17:21 · [커뮤니티 토론](https://news.ycombinator.com/item?id=48662999)

**배경 지식**: In the context of large language models (LLMs), 'computer use' refers to the AI's ability to interact with and control external software, tools, or operating system functions, extending its capabilities beyond text generation to perform actions in the digital environment. This allows the AI to execute tasks like browsing the web, using specific applications, or manipulating data in a structured way, often through API calls or simulated user interfaces.

**커뮤니티 토론**: The community expressed significant disappointment, citing the model's inability to complete simple data extraction tasks, lack of support for useful features, overly aggressive guardrails leading to frequent refusals, and concerns about the security and efficiency of the 'computer use' concept itself. Some users also pointed out discrepancies between Google's performance graphs and their actual real-world experience.

**태그**: `#AI/ML`, `#Large Language Models`, `#Gemini`, `#AI Capabilities`, `#User Experience`

---

<a id="item-9"></a>
## [astral-sh/uv released 0.11.24](https://github.com/astral-sh/uv/releases/tag/0.11.24) ⭐️ 7.0/10

The `uv` 0.11.24 release introduces support for CPython 3.15.0b3, enables relocatable project environments as a preview feature, and includes performance improvements and several bug fixes.

github · github-actions[bot] · 6월23일 21:16

**태그**: `#Python`, `#Package Management`, `#Dependency Management`, `#Tooling`, `#Release Notes`

---