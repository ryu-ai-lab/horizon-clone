(function () {
  'use strict';

  /** Replace ⭐️ N/10 with a colored badge in h2, h3, and li elements */
  function processScoreBadges() {
    var scoreRe = /⭐️\s*(\d+(?:\.\d+)?)\/10/;
    var targets = document.querySelectorAll('.main-content h2, .main-content h3, .main-content li');
    targets.forEach(function (el) {
      var m = el.innerHTML.match(scoreRe);
      if (!m) return;
      var score = parseFloat(m[1]);
      var tier;
      if (score >= 9) tier = 'high';
      else if (score >= 7) tier = 'good';
      else if (score >= 5) tier = 'mid';
      else tier = 'low';
      el.innerHTML = el.innerHTML.replace(
        scoreRe,
        '<span class="score-badge" data-tier="' + tier + '">' + m[1] + '</span>'
      );
    });
  }

  /** Add semantic classes to tag lines, source lines, and background paragraphs */
  function markSemanticElements() {
    var paragraphs = document.querySelectorAll('.main-content p');
    paragraphs.forEach(function (p) {
      var text = p.textContent.trim();

      // Tag line: starts with Tags or 标签 (bold prefix rendered by Markdown)
      if (/^(Tags|标签)\s*:/.test(text)) {
        p.classList.add('tag-line');
        return;
      }

      // Source line: pattern like "source · site · date"
      if (/^(rss|reddit|github|hackernews|hn|telegram)\s*·/i.test(text)) {
        p.classList.add('source-line');
        return;
      }
    });
  }

  /** Set up EN/한국어 language toggle as a page-level control */
  function setupLanguageToggle() {
    // Create toggle buttons
    var toggle = document.createElement('div');
    toggle.className = 'lang-toggle';

    var btnEn = document.createElement('button');
    btnEn.textContent = 'EN';
    btnEn.type = 'button';

    var btnKo = document.createElement('button');
    btnKo.textContent = '한국어';
    btnKo.type = 'button';

    toggle.appendChild(btnEn);
    toggle.appendChild(btnKo);

    // Insert at top of body
    document.body.insertBefore(toggle, document.body.firstChild);

    // Read saved preference, default to ko
    var saved = null;
    try { saved = localStorage.getItem('horizon-lang'); } catch (e) { /* noop */ }
    var currentLang = saved === 'en' ? 'en' : 'ko';

    function updateButtons(lang) {
      if (lang === 'en') {
        btnEn.classList.add('active');
        btnKo.classList.remove('active');
      } else {
        btnKo.classList.add('active');
        btnEn.classList.remove('active');
      }
    }

    // Index page: toggle lang-section visibility
    var koSection = document.getElementById('lang-ko');
    var enSection = document.getElementById('lang-en');

    function showSection(lang) {
      if (!koSection || !enSection) return;
      if (lang === 'en') {
        enSection.classList.remove('hidden');
        koSection.classList.add('hidden');
      } else {
        koSection.classList.remove('hidden');
        enSection.classList.add('hidden');
      }
    }

    // Article page: redirect to the other language version
    function switchArticleLang(lang, rollback) {
      var path = window.location.pathname;
      var target = null;
      if (lang === 'en' && /-ko(?:\.html)?$/.test(path.replace(/\/$/, ''))) {
        target = path.replace(/-ko(\.html)?$/, '-en$1').replace(/-ko\/$/, '-en/');
      } else if (lang === 'ko' && /-en(?:\.html)?$/.test(path.replace(/\/$/, ''))) {
        target = path.replace(/-en(\.html)?$/, '-ko$1').replace(/-en\/$/, '-ko/');
      }
      if (target) {
        fetch(target, { method: 'HEAD' })
          .then(function (res) {
            if (res.ok) {
              window.location.href = target;
            } else {
              alert(lang === 'en' ? 'English version is not available for this post.' : '한국어 버전이 존재하지 않는 게시글입니다.');
              if (rollback) rollback();
            }
          })
          .catch(function () {
            // Fallback for environments where fetch fails (e.g. CORS or file://)
            window.location.href = target;
          });
      }
    }

    function setLang(lang) {
      var prevLang = currentLang;
      currentLang = lang;
      updateButtons(lang);
      try { localStorage.setItem('horizon-lang', lang); } catch (e) { /* noop */ }
      if (koSection && enSection) {
        showSection(lang);
      } else {
        switchArticleLang(lang, function () {
          currentLang = prevLang;
          updateButtons(prevLang);
          try { localStorage.setItem('horizon-lang', prevLang); } catch (e) { /* noop */ }
        });
      }
    }

    btnEn.addEventListener('click', function () { setLang('en'); });
    btnKo.addEventListener('click', function () { setLang('ko'); });

    // Initialize
    updateButtons(currentLang);
    if (koSection && enSection) {
      showSection(currentLang);
    }
  }

  document.addEventListener('DOMContentLoaded', function () {
    processScoreBadges();
    markSemanticElements();
    setupLanguageToggle();
  });
})();
