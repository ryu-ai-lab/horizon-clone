---
layout: default
title: "Horizon Summary: 2026-11-06"
date: 2026-11-06
lang: ko
---

> 47개의 콘텐츠 중 7개의 중요한 정보가 선별되었습니다.

---

1. [Sshole Vulnerability Allows OpenSSH Authentication Bypass via `crypt()` Function Flaw](#item-1) ⭐️ 9.0/10
2. [Claude Code Leaks User Email Addresses via User-Agent Headers](#item-2) ⭐️ 9.0/10
3. [MS Paint Remote Code Execution Vulnerability Discovered](#item-3) ⭐️ 9.0/10
4. [Motorola Signature 27 Announced with Potential GrapheneOS Support](#item-4) ⭐️ 8.0/10
5. [Airbnb to Launch AI Travel Agent by H1 2027](#item-5) ⭐️ 8.0/10
6. [Search for everyone](#item-6) ⭐️ 7.0/10
7. [Goodbye from Salon](#item-7) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Sshole Vulnerability Allows OpenSSH Authentication Bypass via `crypt()` Function Flaw](https://sshhole.com/) ⭐️ 9.0/10

A new vulnerability, dubbed 'sshole', has been identified in OpenSSH, allowing authentication bypass by exploiting how the `crypt()` function in C libraries like musl libc handles special characters such as `*` or `!` in password hashes. This flaw enables unauthorized access on affected systems, particularly those using musl libc without proper workarounds. This vulnerability is critical because it allows attackers to bypass authentication in OpenSSH, a fundamental tool for secure remote access, potentially leading to unauthorized control over affected Linux systems. Its impact is significant for environments utilizing C libraries like musl libc, which are common in lightweight distributions such as Alpine Linux. The core technical detail is that the `crypt()` function, particularly in musl libc, returns a `*` character for both accounts with disabled passwords and when password hashing fails (e.g., due to an oversized input), leading OpenSSH to incorrectly validate an attacker's login attempt. This "in-band signaling" issue means that an attacker can submit a specially crafted (e.g., oversized) password to trigger a hashing failure, causing `crypt()` to return `*`, which then matches a stored `*` for accounts intended to be un-loggable.

hackernews · josemrb · 11월5일 12:19 · [커뮤니티 토론](https://news.ycombinator.com/item?id=50378228)

**배경 지식**: OpenSSH is a widely used suite of tools that provides secure encrypted communication over computer networks, commonly used for remote login and file transfers. The `crypt()` function is a standard C library function used for hashing passwords, converting a plaintext password into a one-way encrypted string for storage and verification. Libc, or the C standard library, is a collection of functions that provide basic services for C programs, such as input/output, memory management, and cryptographic operations like password hashing, with musl libc being a lightweight alternative to glibc.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/">Security advisory: openssh-server password ... | Alpine Linux</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/openssh-flaw-lets-attackers-log-into-password-disabled-linux-accounts/">OpenSSH flaw lets attackers log into password -disabled Linux accounts</a></li>
<li><a href="https://en.wikipedia.org/wiki/C_standard_library">C standard library - Wikipedia</a></li>

</ul>
</details>

**커뮤니티 토론**: The community discussion provides deep technical analysis, pinpointing "in-band signaling" as the core issue where special characters like `*` are overloaded for both "no password" and "hashing failure" states. Commenters explain how this allows attackers to bypass authentication by submitting oversized passwords, and some express disappointment with musl libc developers for not fully addressing known vulnerabilities or for making "convenient" changes without sufficient auditing. There's a general consensus that "magic strings" for signaling should be avoided in favor of more robust error handling mechanisms.

**태그**: `#Cybersecurity`, `#Authentication Bypass`, `#OpenSSH`, `#Vulnerability`, `#Libc`

---

<a id="item-2"></a>
## [Claude Code Leaks User Email Addresses via User-Agent Headers](https://github.com/anthropics/claude-code/issues/107757) ⭐️ 9.0/10

A critical privacy vulnerability was discovered in Anthropic's Claude Code, which inadvertently leaked users' email addresses and other Personally Identifiable Information (PII) to websites through User-Agent HTTP headers. Anthropic has since released an official fix, version 2.1.317 or later, which includes a `cc-plugin-privacy` mod to block this behavior. This vulnerability is highly significant as it erodes user trust in AI development tools and poses a serious risk to data privacy, potentially leading to increased spam and targeted attacks. It highlights the critical need for robust security measures in AI agents that interact with external services. The vulnerability specifically involved Claude Code's subagents embedding user identifiers, including names, company details, and even email addresses, into the User-Agent header of outgoing `curl` requests. This occurred even when using a private Claude account, and some users speculated that Anthropic's servers might also be involved in adding user details to queries.

hackernews · motoroco · 11월5일 22:17 · [커뮤니티 토론](https://news.ycombinator.com/item?id=50385272)

**배경 지식**: Claude Code is Anthropic's agentic coding tool that helps developers by understanding codebases, editing files, and running commands within their terminal or IDE. The User-Agent header is an HTTP request header that identifies the application, operating system, and version of the client making a web request, typically used by servers to tailor responses or gather analytics.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://code.claude.com/">Claude Code by Anthropic | AI coding agent and assistant</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/User-Agent">User-Agent header - HTTP | MDN - MDN Web Docs</a></li>

</ul>
</details>

**커뮤니티 토론**: The community expressed significant concern, with many users reporting a surge in personalized spam emails since using Claude Code, attributing it directly to this vulnerability. Users provided technical examples of how personal identifiers were embedded in User-Agent headers and questioned Anthropic's server-side handling of requests, while Anthropic confirmed awareness and the release of a fix in version 2.1.317.

**태그**: `#AI`, `#Privacy`, `#Security`, `#Developer Tools`, `#Claude Code`

---

<a id="item-3"></a>
## [MS Paint Remote Code Execution Vulnerability Discovered](https://www.cve.org/CVERecord?id=CVE-2026-83844) ⭐️ 9.0/10

A critical remote code execution (RCE) vulnerability, identified as CVE-2026-83844, has been discovered in MS Paint, allowing unauthenticated attackers to exploit it by sending specially crafted network packets. This vulnerability is highly significant due to its severity as a Remote Code Execution flaw in a ubiquitous and seemingly innocuous application like MS Paint, posing a substantial risk of arbitrary code execution on affected systems. The vulnerability specifically impacts MS Paint versions from 11.0.0.0 up to, but not including, 11.2605.91.0, and can be exploited by sending a specially crafted network packet to an affected service. Users may need to update their application through the Microsoft Store if Windows Update does not immediately provide the patch.

hackernews · kuberwastaken · 11월5일 20:43 · [커뮤니티 토론](https://news.ycombinator.com/item?id=50384233)

**배경 지식**: Remote Code Execution (RCE) is a critical cybersecurity vulnerability that enables an attacker to execute arbitrary commands or code on a remote computer. This type of exploit often allows attackers to gain full control over a compromised system without requiring physical access or local user privileges, making it one of the most severe threats in IT security.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://cyberphinix.de/en/blog/remote-code-execution-explained/">Remote code execution explained : How hackers take... | Cyberphinix</a></li>
<li><a href="https://www.n-able.com/blog/remote-code-execution">RCE: Remote Code Execution Explained - N-able</a></li>

</ul>
</details>

**커뮤니티 토론**: The community expressed widespread surprise and disbelief regarding a Remote Code Execution vulnerability in MS Paint, particularly questioning why such a basic application would possess network capabilities exploitable by crafted packets. Discussions also touched upon the specific affected versions and the potential need to update via the Microsoft Store rather than Windows Update.

**태그**: `#Cybersecurity`, `#Vulnerability`, `#Remote Code Execution`, `#Microsoft`, `#Software Security`

---

<a id="item-4"></a>
## [Motorola Signature 27 Announced with Potential GrapheneOS Support](https://motorolanews.com/motorola-signature-27-2/) ⭐️ 8.0/10

Motorola has announced a new high-end smartphone, the Signature 27, which is expected to offer support for the privacy-focused GrapheneOS, starting at an MSRP of $1,599. This development is significant as it could expand GrapheneOS availability beyond Google Pixel devices, potentially offering more hardware choices for privacy-conscious users, but it also sparks debate about trusting a privacy-focused OS on hardware from a manufacturer with a complex security track record. The Motorola Signature 27 is priced at a starting MSRP of $1,599, and community discussions immediately raised concerns about Motorola's ownership by a Chinese company and its history of modifying firmware components like the bootloader and BSP, which could impact the integrity of GrapheneOS.

hackernews · monneyboi · 11월5일 16:01 · [커뮤니티 토론](https://news.ycombinator.com/item?id=50380810)

**배경 지식**: GrapheneOS is an open-source mobile operating system built on the Android Open Source Project (AOSP), specifically designed for enhanced security and privacy. It focuses on improving Android's sandboxing, exploit mitigations, and permission model, and has historically been available primarily for Google Pixel devices. The project aims to provide users with a more secure and private mobile experience by minimizing Google services and hardening the OS.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GrapheneOS">GrapheneOS - Wikipedia</a></li>
<li><a href="https://grapheneos.org/">GrapheneOS: the private and secure mobile OS</a></li>

</ul>
</details>

**커뮤니티 토론**: The community expresses significant skepticism regarding the Motorola Signature 27's high price point and raises substantial trust concerns about running GrapheneOS on Motorola hardware, citing the company's Chinese ownership and historical firmware modifications. While some hope for GrapheneOS support to extend to more affordable Motorola models, others question the overall security integrity and the odd pairing of GrapheneOS with Google Gemini promotion.

**태그**: `#Mobile Security`, `#Privacy`, `#GrapheneOS`, `#Hardware Trust`, `#Android`

---

<a id="item-5"></a>
## [Airbnb to Launch AI Travel Agent by H1 2027](https://www.theverge.com/tech/1028412/airbnb-ai-travel-agent-q3-2026-earnings) ⭐️ 8.0/10

Airbnb announced its plan to roll out an AI agent by the first half of 2027, which will help users plan and book their travel. This strategic move was revealed in the company's Q3 2026 earnings shareholder letter. This announcement signifies a major strategic shift for Airbnb, leveraging advanced AI to potentially disrupt the travel industry by automating complex planning and booking tasks. It could transform how users interact with travel platforms, moving beyond simple transactions to comprehensive AI-guided experiences. Airbnb explicitly noted that while current AI agents excel at simple tasks, their upcoming agent aims to handle more complex travel planning and booking functionalities. The company has set a target rollout date for this AI agent in the first half of 2027.

rss · The Verge Tech · 11월6일 00:06

**배경 지식**: An AI agent is an artificial intelligence program designed to autonomously perceive its environment, make decisions, pursue specific goals, and take actions. Unlike simpler AI tools that perform narrow, specific tasks, AI agents can design workflows and interact with external environments to accomplish complex objectives with a degree of independence.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/ai-agents">What are AI agents? - IBM</a></li>

</ul>
</details>

**태그**: `#AI Agents`, `#Travel Technology`, `#Product Strategy`, `#Industry News`, `#Artificial Intelligence`

---

<a id="item-6"></a>
## [Search for everyone](https://kagi.com/changelog#11820) ⭐️ 7.0/10

Kagi has removed the account requirement for its search engine, a strategic move aimed at broader accessibility, which has sparked extensive community discussion about its impact, user experience, and feature gaps like enforced SafeSearch.

hackernews · elashri · 11월5일 20:03 · [커뮤니티 토론](https://news.ycombinator.com/item?id=50383740)

**태그**: `#Search Engines`, `#Product Strategy`, `#Privacy`, `#User Experience`, `#Web Services`

---

<a id="item-7"></a>
## [Goodbye from Salon](https://www.salon.com/2026/11/05/goodbye-from-salon/) ⭐️ 7.0/10

An old article reflecting on the past of Salon.com sparked a robust discussion about the decline of traditional journalism and the ongoing challenges faced by online publications in the digital age.

hackernews · mkeeter · 11월5일 20:03 · [커뮤니티 토론](https://news.ycombinator.com/item?id=50383739)

**태그**: `#Media Industry`, `#Online Publishing`, `#Journalism`, `#Business Models`, `#Digital Media History`

---