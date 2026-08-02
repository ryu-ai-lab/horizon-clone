---
layout: default
title: "Horizon Summary: 2026-08-03"
date: 2026-08-03
lang: ko
---

> 42개의 콘텐츠 중 4개의 중요한 정보가 선별되었습니다.

---

1. [Karpathy Introduces 'Pelican on a Bicycle' AI Benchmark](#item-1) ⭐️ 8.0/10
2. [Kakehashi Project Enables macOS CLI Binaries on Linux ARM](#item-2) ⭐️ 8.0/10
3. [F*: A Proof-Oriented Language for Formal Verification](#item-3) ⭐️ 7.0/10
4. [RISC OS Open Celebrates 20 Years of OS Development and Preservation](#item-4) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Karpathy Introduces 'Pelican on a Bicycle' AI Benchmark](https://twitter.com/karpathy/status/2083749667410727319) ⭐️ 8.0/10

A tweet by prominent AI figure Karpathy introduced the 'Pelican on a bicycle' as a novel benchmark for evaluating AI models' understanding of the physical world and their ability to generate complex visual scenes. This benchmark, originally created by Simon Willison, challenges models to produce an SVG of a pelican riding a bicycle, moving beyond traditional text-only evaluations. This benchmark signifies a shift in AI evaluation, moving beyond language comprehension to assess models' grasp of physical coherence and visual generation, which is crucial for developing more capable and grounded AI systems. It highlights the growing need for benchmarks that test AI's ability to interact with and understand the physical world, rather than just processing text. The 'Pelican on a bicycle' benchmark specifically tests a model's capacity to generate valid, visually coherent Scalable Vector Graphics (SVG) code depicting a physically impossible scene. Unlike traditional benchmarks such as MMLU, HellaSwag, and GSM8K, which focus on text-based reasoning and knowledge recall, this benchmark aims to measure progress in visual and 3D graphics generation.

hackernews · delichon · 8월2일 04:05 · [커뮤니티 토론](https://news.ycombinator.com/item?id=49140998)

**배경 지식**: Traditional AI benchmarks like MMLU, HellaSwag, and GSM8K primarily evaluate Large Language Models (LLMs) through text-based tasks such as multiple-choice questions, short-answer responses, or mathematical problem-solving. These benchmarks focus on assessing knowledge recall, commonsense inference, and linguistic capabilities. In contrast, the 'Pelican on a bicycle' benchmark is designed to push AI models beyond text, evaluating their ability to understand and represent physical concepts visually, often involving code generation for graphics.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://grokipedia.com/page/Pelican_on_a_bicycle_AI_benchmark">Pelican on a bicycle (AI benchmark) - Grokipedia</a></li>
<li><a href="https://ai.miraheze.org/wiki/Pelican_Bicycle_Benchmark">Pelican Bicycle Benchmark - Learn AI</a></li>

</ul>
</details>

**커뮤니티 토론**: The community discussion shows mixed reactions, with some users acknowledging the benchmark's value for measuring future AI progress in physical world understanding despite current imperfect outputs. However, others express concern that such benchmarks might lower quality expectations for AI or suggest that models could be specifically trained for certain code generation tasks, making the benchmark less indicative of general AI capabilities.

**태그**: `#AI Evaluation`, `#AI Benchmarks`, `#Large Language Models`, `#AI Capabilities`, `#3D Graphics`

---

<a id="item-2"></a>
## [Kakehashi Project Enables macOS CLI Binaries on Linux ARM](https://github.com/wie-project/kakehashi) ⭐️ 8.0/10

Kakehashi is an experimental userspace project that aims to run macOS CLI binaries natively on Linux ARM machines. It has successfully demonstrated working prototypes for 7-Zip, curl, and Xcode Tools Git, with 7-Zip showing promising but early performance results. This project is significant as it addresses a complex cross-platform compatibility challenge, potentially allowing developers and users to leverage macOS command-line tools on Linux ARM devices. It could bridge a crucial gap for those working with Apple Silicon-based Macs and Linux environments. Kakehashi operates as a userspace macOS ARM64 to Linux aarch64 translation layer, focusing on CLI applications without a JIT compiler. While 7-Zip is currently ~5.2x slower than native Linux execution, the developer has outlined a clear optimization plan to improve performance.

hackernews · vlad_kalinkin · 8월2일 16:26 · [커뮤니티 토론](https://news.ycombinator.com/item?id=49145937)

**배경 지식**: Userspace refers to the memory area where user applications run, separate from the kernelspace where the operating system's core components reside. Binary compatibility, in this context, means enabling an executable compiled for one operating system and architecture (e.g., macOS ARM) to run on another (e.g., Linux ARM) by translating system calls and library dependencies.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://github.com/wie-project/kakehashi">GitHub - wie- project / kakehashi : Userspace macOS translation layer...</a></li>
<li><a href="https://blogs.oracle.com/linux/userspace-vs-kernelspace-understanding-the-divide">Userspace vs Kernelspace: Understanding the Divide | linux</a></li>
<li><a href="https://linuxcommandlibrary.com/man/darling">darling linux command man page: Run macOS software on Linux</a></li>

</ul>
</details>

**커뮤니티 토론**: The community expresses strong interest and excitement for Kakehashi, drawing parallels to successful projects like WINE/Proton for Windows applications. There's also discussion about its relationship with the existing Darling project for macOS compatibility on Linux and inquiries about the project's long-term development and potential for running graphical applications.

**태그**: `#Cross-platform`, `#macOS`, `#Linux`, `#ARM`, `#Binary compatibility`

---

<a id="item-3"></a>
## [F*: A Proof-Oriented Language for Formal Verification](https://fstar-lang.org/) ⭐️ 7.0/10

F* is a general-purpose, proof-oriented programming language designed for formal verification, generating significant community interest regarding its practical applications and potential for industry adoption. While not a new major release, the discussion highlights its technical merits and real-world applicability. F* is significant because it allows developers to write programs with machine-checked proofs of their properties, enhancing software assurance for critical systems where correctness and security are paramount. Its potential for industry adoption could lead to more reliable and secure software across various domains. F* features a sophisticated type system including dependent types, monadic effects, and refinement types, enabling precise program specifications and verification using SMT solving and manual proofs. Programs can be translated to OCaml, F#, C, or WebAssembly for execution, and users are actively seeking more practical code examples and industry use cases.

hackernews · ducktective · 8월2일 12:31 · [커뮤니티 토론](https://news.ycombinator.com/item?id=49143925)

**배경 지식**: Formal verification is a technique used in software engineering to prove the correctness and robustness of software and hardware systems using mathematical methods. A proof-oriented programming language, like F*, integrates executable code, formal specifications, and correctness proofs into a unified development process, often utilizing advanced type systems and automated theorem proving to provide mathematical guarantees about program behavior.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://fstar-lang.org/">F*: A Proof-Oriented Programming Language</a></li>
<li><a href="https://en.wikipedia.org/wiki/F*_(programming_language)">F* (programming language) - Wikipedia</a></li>
<li><a href="https://github.com/FStarLang/FStar">GitHub - FStarLang/FStar: A Proof-oriented Programming Language F* (programming language) - Wikipedia Proof-oriented Programming in F* — Proof-Oriented Programming ... Proof-Oriented Programming Languages - emergentmind.com F* – general-purpose, proof-oriented programming language FStarLang · GitHub</a></li>

</ul>
</details>

**커뮤니티 토론**: The community expresses strong interest in F*'s practical applications and industry adoption, with users sharing positive experiences migrating C codebases. There's a clear demand for more accessible code examples and tutorials to better understand its syntax and use cases, alongside questions about its current industrial deployment.

**태그**: `#Formal Verification`, `#Programming Languages`, `#Software Engineering`, `#Functional Programming`, `#Systems Research`

---

<a id="item-4"></a>
## [RISC OS Open Celebrates 20 Years of OS Development and Preservation](https://www.riscosopen.org/news/articles/2026/06/20/twenty-years-of-risc-os-open) ⭐️ 6.0/10

RISC OS Open is celebrating its 20th anniversary, marking two decades of dedicated effort in the continued development and preservation of the historically significant RISC OS operating system. This milestone highlights the project's commitment to an OS known for its origins with Acorn computers and ARM architecture. This anniversary is significant as it underscores the enduring dedication of a community to a niche, historical operating system, demonstrating the long-term viability and passion for open-source projects focused on preserving computing heritage. It also highlights the unique technical characteristics of RISC OS that continue to attract interest, such as its efficiency on modern hardware like the Raspberry Pi. Community members recall developing applications like "!Director" entirely in ARM assembler and note the impressive boot speed of RISC OS on Raspberry Pi devices. The famous music notation program Sibelius also originated on Acorn Archimedes under RISC OS, showcasing its historical impact on software development.

hackernews · AlexeyBrin · 8월2일 12:36 · [커뮤니티 토론](https://news.ycombinator.com/item?id=49143967)

**배경 지식**: RISC OS is an operating system designed in 1987 by Acorn Computers in England, specifically for their new ARM-based Archimedes personal computers. It is an open-source OS that runs on ARM architecture, which stands for Reduced Instruction Set Computer (RISC) architecture, known for its simplified instruction sets. Acorn Computers was a British company established in 1978, famous for producing popular computers in the 1980s and playing a pivotal role in the development of the ARM processor.

<details><summary>참고 링크</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RISC_OS">RISC OS - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Acorn_Archimedes">Acorn Archimedes - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Acorn_Computers">Acorn Computers - Wikipedia</a></li>

</ul>
</details>

**커뮤니티 토론**: The community discussion reflects a strong sense of nostalgia and appreciation for RISC OS, with users sharing personal anecdotes about developing software in ARM assembler and its surprisingly fast boot times on modern Raspberry Pi hardware. There's also recognition of its historical significance, including its role in the origin of professional applications like Sibelius, highlighting the unique challenges and dedication involved in maintaining such a niche OS.

**태그**: `#Operating Systems`, `#History of Computing`, `#RISC OS`, `#Open Source`, `#ARM Architecture`

---