---
layout: default
title: "Horizon Summary: 2026-11-28"
date: 2026-11-28
lang: ko
---

> 22개의 콘텐츠 중 7개의 중요한 정보가 선별되었습니다.

---

1. [Credit card skimming scripts using WebRTC found on popular shopping sites](#item-1) ⭐️ 9.0/10
2. [Google's DeepCrossAttention achieves comparable model quality up to 3x faster](#item-2) ⭐️ 9.0/10
3. [Bouncemarket: A Live Prediction Market Game for a Deterministic Bouncing Ball](#item-3) ⭐️ 8.0/10
4. [Convex Plugin Implicitly Sends User App Ideas to Remote Server](#item-4) ⭐️ 8.0/10
5. [Citroën's Integrated Hydraulic System: Innovation and Challenges](#item-5) ⭐️ 7.0/10
6. [datasette-charts 0.4a0 Improves API and Launches New Website](#item-6) ⭐️ 7.0/10
7. [Akai MPC Sample Opens to Custom Firmware and Mods](#item-7) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Credit card skimming scripts using WebRTC found on popular shopping sites](https://www.infohawk.com/news/2026-11-27-black-friday-webrtc-skimmer) ⭐️ 9.0/10

Credit card skimming scripts have been identified on popular shopping websites, exploiting WebRTC as an unmonitored channel to exfiltrate sensitive user payment data.

hackernews · scanr · 11월27일 15:40 · [커뮤니티 토론](https://news.ycombinator.com/item?id=50668145)

**태그**: `#Web Security`, `#E-commerce`, `#WebRTC`, `#Cybercrime`, `#Data Breaches`

---

<a id="item-2"></a>
## [Google's DeepCrossAttention achieves comparable model quality up to 3x faster](https://research.google/blog/supercharging-transformer-residual-connections/) ⭐️ 9.0/10

Google's DeepCrossAttention introduces a novel method for transformer residual connections that achieves up to 3x faster model inference while maintaining comparable quality, promising significant efficiency gains for AI models.

hackernews · ComputedCamp995 · 11월27일 23:06 · [커뮤니티 토론](https://news.ycombinator.com/item?id=50672565)

**태그**: `#AI/ML`, `#Transformers`, `#Deep Learning`, `#Model Optimization`, `#Google Research`

---

<a id="item-3"></a>
## [Bouncemarket: A Live Prediction Market Game for a Deterministic Bouncing Ball](https://bouncemarket.minhanhday.com/) ⭐️ 8.0/10

Bouncemarket is a newly launched live prediction market game where users bet on the landing spot of a server-simulated bouncing ball, utilizing deterministic physics, server-sent events for real-time streaming, and featuring AI traders to maintain market activity. This game is significant as it demonstrates a novel application of real-time simulation and prediction market mechanics, sparking community interest in how deterministic yet chaotic systems can be 'solved' by advanced AI bots and exploring the broader implications for prediction markets on seemingly random events. The game's core technicality lies in its server-side deterministic physics simulation, allowing exact replays for analysis, though minute initial position variations can drastically alter outcomes; AI traders with simple rules participate to ensure market liquidity but withdraw when more than five human players are present.

hackernews · mday404 · 11월27일 15:01 · [커뮤니티 토론](https://news.ycombinator.com/item?id=50667726)

**배경 지식**: A prediction market is an exchange where participants trade contracts whose payoffs are tied to the outcome of future events, with market prices reflecting aggregated beliefs. Server-Sent Events (SSE) is a web technology allowing servers to push real-time updates to clients over a persistent HTTP connection. A deterministic physics simulation ensures that, given the same initial conditions, the simulation will always produce the exact same results, making it reproducible for analysis.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Server-sent_events">Server-sent events</a></li>
<li><a href="https://en.wikipedia.org/wiki/Prediction_market">Prediction market</a></li>
<li><a href="https://inferensys.com/glossary/sim-to-real-transfer-learning/physics-simulation-engines/deterministic-simulation">Deterministic Simulation: Definition & Importance | Inference ...</a></li>

</ul>
</details>

**커뮤니티 토론**: The community generally found the game fun and engaging, with discussions ranging from practical gameplay strategies like buying cheap shares regardless of the ball's path, to suggestions for slower ball drops due to rapid odds changes. There was also significant interest in the potential for advanced AI bots to 'solve' the deterministic system and the broader implications for real-money prediction markets on purely random events.

**태그**: `#Prediction Markets`, `#Game Development`, `#Real-time Systems`, `#AI Strategy`, `#Simulation`

---

<a id="item-4"></a>
## [Convex Plugin Implicitly Sends User App Ideas to Remote Server](https://github.com/convex/convex-backend-skill/issues/64) ⭐️ 8.0/10

A GitHub issue and Hacker News discussion highlighted concerns that a Convex plugin was implicitly sending user application ideas (prompts) to a remote server without explicit consent, prompting Convex's CEO to clarify that this functionality powers a 'quickstart' feature. This incident is significant as it raises critical privacy and trust concerns regarding data handling in AI-integrated developer tools, emphasizing the need for transparent data practices in cloud platforms. The prompt upload feature is intended for Convex's 'quickstart' functionality, described by the CEO as the "spiritual successor" to the recently shut down "Convex Chef" vibe-coding product.

hackernews · MickyTheMouse · 11월27일 18:02 · [커뮤니티 토론](https://news.ycombinator.com/item?id=50669765)

**배경 지식**: Convex is a reactive backend-as-a-service (BaaS) platform designed for TypeScript, offering a custom database with ACID transactions and an integrated execution environment. It aims to simplify application development by bundling functionalities that typically require multiple separate services.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://saikat.com.bd/blog/convex-realtime-reactive-backend">What Is Convex ? The Reactive Backend Platform Explained</a></li>
<li><a href="https://www.youtube.com/watch?v=UVvd7BF99-4">Intro to Convex - YouTube</a></li>

</ul>
</details>

**커뮤니티 토론**: The community discussion included Convex's CEO clarifying the feature's purpose for a 'quickstart' and mentioning the shutdown of a related project, while some users advocated for self-hosted open-weight models and others discussed prompt injection or dismissed the value of ideas.

**태그**: `#Privacy`, `#Developer Tools`, `#AI Ethics`, `#Data Security`, `#Cloud Platforms`

---

<a id="item-5"></a>
## [Citroën's Integrated Hydraulic System: Innovation and Challenges](https://www.citroenet.org.uk/miscellaneous/hydraulics/hydraulics-1.html) ⭐️ 7.0/10

This news item provides a detailed exploration of Citroën's distinctive hydraulic system, which historically unified suspension, braking, and steering functions within a single, complex architecture. This system is significant for its pioneering integration of multiple vehicle functions, showcasing a bold engineering approach that influenced automotive design and offered a unique driving experience, despite its maintenance complexities. A key technical aspect was the system's reliance on a single hydraulic fluid to power suspension, braking, and steering, which, while innovative, meant that a single leak could compromise multiple critical vehicle functions and required specialized maintenance.

hackernews · o4c · 11월27일 03:10 · [커뮤니티 토론](https://news.ycombinator.com/item?id=50662313)

**배경 지식**: Citroën's hydraulic system, specifically its hydropneumatic suspension, was a revolutionary automotive technology developed by Paul Magès. Unlike conventional systems, it used a single high-pressure hydraulic circuit to manage not only suspension but also braking and steering, providing a self-leveling ride and variable ground clearance.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hydropneumatic_suspension">Hydropneumatic suspension - Wikipedia</a></li>
<li><a href="https://www.citroenet.org.uk/miscellaneous/hydraulics/hydraulics-16.html">Citroën high pressure hydraulic system explained using ...</a></li>

</ul>
</details>

**커뮤니티 토론**: The community discussion reflects a mix of nostalgia and appreciation for Citroën's unique hydraulic system, highlighting its smooth ride and innovative integration of functions, while also acknowledging its significant maintenance demands and the potential for critical failures due to leaks.

**태그**: `#Automotive Engineering`, `#Hydraulic Systems`, `#Engineering History`, `#Mechanical Design`, `#Vehicle Technology`

---

<a id="item-6"></a>
## [datasette-charts 0.4a0 Improves API and Launches New Website](https://simonwillison.net/2026/Nov/27/datasette-charts/) ⭐️ 7.0/10

The `datasette-charts` 0.4a0 release significantly improves the plugin's API for defining custom chart types, making development more ergonomic based on friction points identified by LLM-assisted testing. Additionally, a new website, `charts.datasette.io`, has been launched, featuring tutorials for plugin authors and an interactive chart gallery with Datasette Lite demos. This update is significant as it greatly enhances the usability and extensibility of the `datasette-charts` plugin, making it easier for developers to create custom chart types. The new website and improved API will foster a more vibrant Datasette ecosystem by simplifying data visualization and plugin development. The API improvements specifically target the plugin hook for defining new chart types, making it more ergonomic for developers. Notably, an LLM, Claude Opus 5.5, was utilized to identify design friction points, and the new website offers interactive demos on Datasette Lite for all core charts and annotations.

rss · Simon Willison · 11월27일 23:57

**배경 지식**: Datasette is an open-source tool designed for exploring and publishing structured data, often from SQLite databases, and it supports a rich ecosystem of plugins to extend its capabilities, including data visualization. LLM-assisted testing utilizes large language models to enhance software quality assurance by helping teams create, refine, and manage tests with contextual intelligence.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://www.accelq.com/blog/llm-software-testing/">LLM Software Testing for Enterprises | Next-Gen QA Strategy</a></li>

</ul>
</details>

**태그**: `#Datasette`, `#Plugin Development`, `#Data Visualization`, `#API Design`, `#LLM Applications`

---

<a id="item-7"></a>
## [Akai MPC Sample Opens to Custom Firmware and Mods](https://www.theverge.com/gadgets/1044485/mpc-sample-firmware-sdk) ⭐️ 7.0/10

Akai has released the MPC Sample 1.4 firmware update, officially opening its affordable beat maker to custom firmware and mods and embracing its existing modding community. This move is significant as it represents a rare embrace of user-driven innovation by a hardware manufacturer, potentially fostering greater customization and creativity within the music production and embedded systems communities. The 1.4 firmware update specifically enables support for "vibe-coded" custom firmwares and various modifications, indicating Akai's strategic shift from resisting to actively supporting its user base's creative endeavors.

rss · The Verge Tech · 11월27일 20:48

**배경 지식**: The Akai MPC Sample is a popular and affordable hardware sampler and beat maker used by musicians for creating and performing music. Firmware refers to the embedded software that controls the device's basic functions, and "modding" involves users creating custom versions of this software or hardware to add new features or alter existing ones.

**태그**: `#Music Technology`, `#Hardware Modding`, `#Firmware Development`, `#Developer Ecosystems`, `#Embedded Systems`

---