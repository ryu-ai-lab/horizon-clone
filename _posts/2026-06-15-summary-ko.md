---
layout: default
title: "Horizon Summary: 2026-06-15 (KO)"
date: 2026-06-15
lang: ko
---

> 15개의 콘텐츠 중 4개의 중요한 정보가 선별되었습니다.

---

1. [Pyodide 314.0, PEP 783 통해 WASM 휠 PyPI 직접 게시 가능](#item-1) ⭐️ 9.0/10
2. [Your ePub Is fine](#item-2) ⭐️ 8.0/10
3. [Why AI hasn’t replaced software engineers, and won’t](#item-3) ⭐️ 8.0/10
4. [Show HN: Kage – Shadow any website to a single binary for offline viewing](#item-4) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Pyodide 314.0, PEP 783 통해 WASM 휠 PyPI 직접 게시 가능](https://simonwillison.net/2026/Jun/13/publishing-wasm-wheels/#atom-everything) ⭐️ 9.0/10

Pyodide 314.0 릴리스는 이제 PEP 783 에 정의된 PyEmscripten 플랫폼을 활용하여 WebAssembly(WASM)용으로 빌드된 Python 패키지를 PyPI 에 직접 게시할 수 있도록 합니다. 4 월 21 일에 PyPI PR 을 통해 지원된 이 중요한 업데이트는 관리자가 Pyodide 휠을 네이티브 휠처럼 배포할 수 있게 합니다. 이 변화는 Pyodide 개발자의 유지보수 부담을 크게 줄이고 커뮤니티의 주요 병목 현상을 해소하여, 웹 브라우저에서 C/Rust 확장 기능을 포함한 Python 패키지를 훨씬 쉽게 배포하고 설치할 수 있게 합니다. 이는 WebAssembly 환경에서 Python 개발 및 채택을 간소화하여 더욱 강력한 생태계를 조성합니다. 핵심 기술적 가능성은 WASM 용 Python 패키지가 빌드되고 사용되는 방식을 표준화하는 PEP 783 에 정의된 PyEmscripten 플랫폼입니다. 작성자는 C++ 프로젝트를 WASM 으로 컴파일한 `luau-wasm`을 성공적으로 패키징하고 해당 `pyemscripten_2026_0_wasm32.whl` 파일을 PyPI 에 직접 게시하여 `micropip`을 통해 설치할 수 있음을 시연했습니다.

rss · Simon Willison · 6월13일 23:55

**배경 지식**: Pyodide 는 웹 브라우저에서 Python 을 실행할 수 있게 하는 프로젝트로, 웹에서 고성능 애플리케이션을 가능하게 하는 저수준 바이트코드 형식인 WebAssembly(WASM)를 사용합니다. PyPI(Python Package Index)는 Python 패키지의 주요 저장소이며, "휠(wheels)"은 미리 빌드된 Python 패키지의 표준 배포 형식으로 설치를 간소화합니다.

**태그**: `#Python`, `#WebAssembly`, `#Pyodide`, `#PyPI`, `#Package Management`

---

<a id="item-2"></a>
## [Your ePub Is fine](https://andreklein.net/your-epub-is-fine-kobo-disagrees-blame-adobe/) ⭐️ 8.0/10

The article and its extensive discussion highlight how Kobo e-readers' reliance on Adobe's poorly supported and licensed Reader Mobile SDK leads to significant compatibility issues for valid ePub files, underscoring Adobe's historical patterns of problematic software partnerships and offering community-driven workarounds.

hackernews · sohkamyung · 6월14일 22:54 · [커뮤니티 토론](https://news.ycombinator.com/item?id=48533848)

**태그**: `#e-readers`, `#ePub`, `#Adobe`, `#Software Engineering`, `#Digital Publishing`

---

<a id="item-3"></a>
## [Why AI hasn’t replaced software engineers, and won’t](https://simonwillison.net/2026/Jun/14/why-ai-hasnt-replaced-software-engineers/#atom-everything) ⭐️ 8.0/10

An analysis by Arvind Narayanan and Sayash Kappor, curated by Simon Willison, argues that current evidence does not support the narrative of AI causing mass layoffs in software engineering or other professions, citing early data from WARN Act filings.

rss · Simon Willison · 6월14일 23:54

**태그**: `#AI Impact`, `#Future of Work`, `#Software Engineering`, `#Job Market`

---

<a id="item-4"></a>
## [Show HN: Kage – Shadow any website to a single binary for offline viewing](https://github.com/tamnd/kage) ⭐️ 7.0/10

Kage is a new command-line tool that archives websites into a single executable binary for convenient offline viewing.

hackernews · tamnd · 6월14일 17:25 · [커뮤니티 토론](https://news.ycombinator.com/item?id=48529990)

**태그**: `#Web Archiving`, `#Offline Browsing`, `#Developer Tools`, `#CLI`, `#Web Utilities`

---