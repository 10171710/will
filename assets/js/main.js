/* ==========================================================================
   Willbridge — main.js
   Shared behaviour for every page: theme toggle, RTL toggle, mobile nav,
   dropdowns, sticky header, back-to-top, AOS init, animated counters,
   a generic filterable/searchable grid engine (services, blog, FAQ),
   generic tabs, in-page scroll-spy for the Service Details rail,
   testimonial carousel, FAQ expand/collapse helpers, password reveal,
   pricing billing switch, lazy-image fade-in and form validation.

   Read the markup contracts in the comments before adding new interactive
   markup — reuse these hooks instead of writing per-page inline scripts.
   ========================================================================== */
(function () {
  'use strict';

  var prefersReducedMotion = window.matchMedia &&
    window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function isRTL() {
    return document.documentElement.getAttribute('dir') === 'rtl';
  }

  /* ---------------- Theme toggle ----------------
     Default theme is LIGHT for this brand (applied by the pre-paint script
     in each page's <head>). Persisted under 'wb-theme'. */
  var themeBtn = document.getElementById('theme-toggle');
  if (themeBtn) {
    themeBtn.addEventListener('click', function () {
      var isDark = document.documentElement.classList.toggle('dark');
      localStorage.setItem('wb-theme', isDark ? 'dark' : 'light');
      themeBtn.setAttribute('aria-pressed', isDark ? 'true' : 'false');
    });
  }

  /* ---------------- RTL / LTR toggle (LTR in normal, RTL in other side) ----------------
     Flips <html dir> and lang so the entire layout mirrors. All spacing in
     the markup uses logical utilities (ms-/me-/ps-/pe-/start-/end-), so
     nothing else has to change. Persisted under 'wb-dir'. */
  var dirBtn = document.getElementById('dir-toggle');
  if (dirBtn) {
    var updateDirState = function (isRtl) {
      dirBtn.setAttribute('aria-pressed', isRtl ? 'true' : 'false');
      dirBtn.setAttribute('title', isRtl ? 'RTL layout (Click for LTR)' : 'LTR layout (Click for RTL)');
      dirBtn.setAttribute('aria-label', isRtl ? 'RTL layout active. Click to switch to LTR' : 'LTR layout active. Click to switch to RTL');
    };
    var isRtlInit = document.documentElement.getAttribute('dir') === 'rtl';
    updateDirState(isRtlInit);

    dirBtn.addEventListener('click', function () {
      var html = document.documentElement;
      var next = html.getAttribute('dir') === 'rtl' ? 'ltr' : 'rtl';
      html.setAttribute('dir', next);
      html.setAttribute('lang', next === 'rtl' ? 'ar' : 'en');
      localStorage.setItem('wb-dir', next);
      updateDirState(next === 'rtl');
      if (window.AOS && typeof window.AOS.refresh === 'function') {
        window.AOS.refresh();
      }
    });
  }

  /* ---------------- Mobile menu ---------------- */
  var mobileBtn = document.getElementById('mobile-menu-btn');
  var mobileMenu = document.getElementById('mobile-menu');
  if (mobileBtn && mobileMenu) {
    mobileBtn.addEventListener('click', function () {
      mobileMenu.classList.toggle('hidden');
      var open = !mobileMenu.classList.contains('hidden');
      var icon = mobileBtn.querySelector('i');
      if (icon) icon.className = open ? 'ri-close-line text-2xl' : 'ri-menu-3-line text-2xl';
      mobileBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
      mobileBtn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    });

    /* Mobile accordion sub-menus (Home 1 / Home 2) */
    mobileMenu.querySelectorAll('[data-mobile-toggle]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var panel = document.getElementById(btn.getAttribute('data-mobile-toggle'));
        if (!panel) return;
        var open = panel.classList.toggle('hidden') === false;
        btn.setAttribute('aria-expanded', open ? 'true' : 'false');
        var icon = btn.querySelector('i.ri-arrow-down-s-line');
        if (icon) icon.classList.toggle('rotate-180', open);
      });
    });
  }

  /* ---------------- Desktop dropdowns (click-based, touch friendly) -------- */
  var groups = document.querySelectorAll('nav .group');
  groups.forEach(function (g) {
    var btn = g.querySelector('button');
    if (!btn) return;
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var wasOpen = g.classList.contains('open');
      groups.forEach(function (o) {
        o.classList.remove('open');
        var ob = o.querySelector('button');
        if (ob) ob.setAttribute('aria-expanded', 'false');
      });
      if (!wasOpen) g.classList.add('open');
      btn.setAttribute('aria-expanded', !wasOpen ? 'true' : 'false');
    });
  });
  document.addEventListener('click', function () {
    groups.forEach(function (g) { g.classList.remove('open'); });
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') groups.forEach(function (g) { g.classList.remove('open'); });
  });

  /* ---------------- Sticky header shadow + back-to-top -------------------- */
  var header = document.getElementById('site-header');
  var backToTop = document.getElementById('back-to-top');
  window.addEventListener('scroll', function () {
    var scrolled = window.scrollY > 20;
    if (header) header.classList.toggle('is-scrolled', scrolled);
    if (backToTop) backToTop.classList.toggle('show', window.scrollY > 500);
  }, { passive: true });
  if (backToTop) {
    backToTop.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: prefersReducedMotion ? 'auto' : 'smooth' });
    });
  }

  /* ---------------- Footer year ---------------- */
  var yearEl = document.getElementById('footer-year');
  if (yearEl) yearEl.textContent = String(new Date().getFullYear());

  /* ---------------- AOS scroll animations ----------------
     Skipped entirely for visitors who prefer reduced motion. */
  if (window.AOS) {
    if (prefersReducedMotion) {
      AOS.init({ disable: true });
    } else {
      AOS.init({ duration: 700, once: true, offset: 60, easing: 'ease-out-cubic' });
    }
  }

  /* ---------------- Animated stat counters ----------------
     Markup: <span data-counter="98" data-suffix="%">0</span> */
  var counters = document.querySelectorAll('[data-counter]');
  if (counters.length && 'IntersectionObserver' in window) {
    var counterObs = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        var raw = el.getAttribute('data-counter');
        var target = parseFloat(raw);
        var suffix = el.getAttribute('data-suffix') || '';
        var decimals = (raw.split('.')[1] || '').length;
        if (prefersReducedMotion) {
          el.textContent = target.toFixed(decimals) + suffix;
          counterObs.unobserve(el);
          return;
        }
        var duration = 1400;
        var startTime = null;
        function step(ts) {
          if (!startTime) startTime = ts;
          var progress = Math.min((ts - startTime) / duration, 1);
          var eased = 1 - Math.pow(1 - progress, 3);
          el.textContent = (target * eased).toFixed(decimals) + suffix;
          if (progress < 1) requestAnimationFrame(step);
        }
        requestAnimationFrame(step);
        counterObs.unobserve(el);
      });
    }, { threshold: 0.4 });
    counters.forEach(function (c) { counterObs.observe(c); });
  }

  /* ---------------- Generic filterable / searchable grid ------------------
     Used by Services, Blog and the FAQ block on Service Details.
     Markup contract:
       [data-filter-root]            wraps search box, filter buttons, list
       [data-filter-search]          optional text input
       [data-filter-btn]="category"  pill button; "all" shows everything
       [data-filter-item]            each card/row, with
                                       data-category="cat1 cat2"
                                       data-title="text the search matches"
       [data-filter-empty]           optional "no results" element
       [data-filter-count]           optional element showing visible count
  ------------------------------------------------------------------------- */
  document.querySelectorAll('[data-filter-root]').forEach(function (root) {
    var search = root.querySelector('[data-filter-search]');
    var buttons = root.querySelectorAll('[data-filter-btn]');
    var items = root.querySelectorAll('[data-filter-item]');
    var empty = root.querySelector('[data-filter-empty]');
    var countEl = root.querySelector('[data-filter-count]');
    var headingEl = root.querySelector('[data-filter-heading]');
    var active = 'all';

    function normalize(cat) {
      if (!cat) return '';
      var c = String(cat).trim().toLowerCase().replace(/[\s_]+/g, '-');
      if (c === 'all' || c === 'all-articles' || c === 'all-services' || c === 'all-questions') return 'all';
      if (c === 'family-conversations' || c === 'family-conversation' || c === 'family_conversations' || c === 'family') return 'family';
      if (c === 'wills' || c === 'will' || c === 'wills-testament' || c === 'wills-drafting') return 'wills';
      if (c === 'trusts' || c === 'trust' || c === 'trusts-settlements' || c === 'trusts-estates' || c === 'trusts-family') return 'trusts';
      if (c === 'probate' || c === 'probates' || c === 'probate-court') return 'probate';
      if (c === 'guides' || c === 'guide' || c === 'guides-checklists') return 'guides';
      if (c === 'digital' || c === 'digital-estate' || c === 'digital-assets') return 'digital';
      if (c === 'nominee' || c === 'nominees' || c === 'nominee-heirs' || c === 'nominee-vs-heirs') return 'nominee';
      if (c === 'disputes' || c === 'dispute' || c === 'dispute-prevention' || c === 'contest') return 'disputes';
      if (c === 'special-needs' || c === 'special-needs-care' || c === 'special-needs-trust') return 'special-needs';
      if (c === 'planning' || c === 'planning-ahead') return 'planning';
      if (c === 'after' || c === 'after-a-death') return 'after';
      if (c === 'business' || c === 'business-property') return 'business';
      if (c === 'fees' || c === 'fees-privacy') return 'fees';
      return c;
    }

    function apply() {
      var q = ((search && search.value) || '').trim().toLowerCase();
      var normActive = normalize(active);
      var visible = 0;

      items.forEach(function (item) {
        var rawCats = (item.getAttribute('data-category') || '').toLowerCase().split(/[\s,]+/);
        var cats = rawCats.map(normalize).filter(Boolean);
        var title = (item.getAttribute('data-title') || '').toLowerCase();
        var fullText = (item.textContent || '').toLowerCase();

        var matchesCategory = normActive === 'all' || normActive === '' || cats.indexOf(normActive) !== -1;
        var matchesSearch = !q || title.indexOf(q) !== -1 || fullText.indexOf(q) !== -1;
        var show = matchesCategory && matchesSearch;

        item.classList.toggle('hidden', !show);
        if (show) {
          visible++;
          item.classList.add('aos-animate');
        }
      });

      if (empty) empty.classList.toggle('hidden', visible !== 0);
      if (countEl) countEl.textContent = String(visible);

      // Dynamic heading update
      if (headingEl) {
        var activeBtn = root.querySelector('[data-filter-btn].is-active');
        if (activeBtn) {
          var btnText = activeBtn.textContent.trim();
          if (normActive === 'all') {
            headingEl.textContent = 'All articles';
          } else {
            headingEl.textContent = btnText;
          }
        }
      }

      // Refresh AOS animations so newly shown items animate smoothly
      if (window.AOS && typeof window.AOS.refresh === 'function') {
        window.AOS.refresh();
      }
    }

    function setActive(newCat, updateUrl) {
      var targetNorm = normalize(newCat);
      var foundBtn = false;

      buttons.forEach(function (b) {
        var bCat = normalize(b.getAttribute('data-filter-btn'));
        var isMatch = bCat === targetNorm || (targetNorm === 'all' && bCat === 'all');
        if (isMatch) {
          foundBtn = true;
          active = b.getAttribute('data-filter-btn');
          b.classList.add('is-active');
          b.setAttribute('aria-pressed', 'true');
        } else {
          b.classList.remove('is-active');
          b.setAttribute('aria-pressed', 'false');
        }
      });

      if (!foundBtn && targetNorm) {
        active = newCat;
      }

      apply();

      if (updateUrl && window.history && window.history.replaceState) {
        try {
          var url = new URL(window.location.href);
          if (active === 'all') {
            url.searchParams.delete('category');
            url.searchParams.delete('filter');
            url.searchParams.delete('cat');
          } else {
            url.searchParams.set('category', active);
          }
          window.history.replaceState(null, '', url.pathname + url.search + url.hash);
        } catch (e) {
          /* ignore */
        }
      }
    }

    if (search) search.addEventListener('input', apply);

    buttons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        setActive(btn.getAttribute('data-filter-btn'), true);
      });
    });

    // Check URL query parameters or hash to activate category directly on load
    try {
      var urlParams = new URLSearchParams(window.location.search);
      var urlCat = urlParams.get('category') || urlParams.get('filter') || urlParams.get('cat') || window.location.hash.replace('#', '');
      if (urlCat) {
        setActive(urlCat, false);
      } else {
        apply();
      }
    } catch (e) {
      apply();
    }
  });

  /* ---------------- FAQ expand-all / collapse-all -------------------------
     Markup: <button data-faq-expand="#faq-list"> / data-faq-collapse="#faq-list" */
  document.querySelectorAll('[data-faq-expand]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var scope = document.querySelector(btn.getAttribute('data-faq-expand'));
      if (!scope) return;
      scope.querySelectorAll('details.faq-item').forEach(function (d) { d.open = true; });
    });
  });
  document.querySelectorAll('[data-faq-collapse]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var scope = document.querySelector(btn.getAttribute('data-faq-collapse'));
      if (!scope) return;
      scope.querySelectorAll('details.faq-item').forEach(function (d) { d.open = false; });
    });
  });

  /* ---------------- Generic tabs ------------------------------------------
     Markup: [data-tabs] wrapper, [data-tab="key"] buttons,
             [data-tab-panel="key"] panels. */
  document.querySelectorAll('[data-tabs]').forEach(function (group) {
    var btns = group.querySelectorAll('[data-tab]');
    var panels = group.querySelectorAll('[data-tab-panel]');
    btns.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var key = btn.getAttribute('data-tab');
        btns.forEach(function (b) {
          var on = b === btn;
          b.classList.toggle('is-active', on);
          b.setAttribute('aria-selected', on ? 'true' : 'false');
        });
        panels.forEach(function (p) {
          p.classList.toggle('hidden', p.getAttribute('data-tab-panel') !== key);
        });
      });
    });
  });

  /* ---------------- Pricing billing switch --------------------------------
     Markup: [data-price-switch] checkbox; prices carry
             data-price-standard / data-price-instalment. */
  var priceSwitch = document.querySelector('[data-price-switch]');
  if (priceSwitch) {
    var priceEls = document.querySelectorAll('[data-price-standard]');
    priceSwitch.addEventListener('change', function () {
      var instalment = priceSwitch.checked;
      priceEls.forEach(function (el) {
        el.textContent = instalment
          ? el.getAttribute('data-price-instalment')
          : el.getAttribute('data-price-standard');
      });
      document.querySelectorAll('[data-price-note]').forEach(function (n) {
        n.textContent = instalment ? n.getAttribute('data-note-instalment') : n.getAttribute('data-note-standard');
      });
    });
  }

  /* ---------------- Scroll-spy for the in-page rail -----------------------
     Markup: [data-spy-link="#section-id"] links; sections are the targets.
     Adds .is-current to the link whose section is nearest the top. */
  var spyLinks = document.querySelectorAll('[data-spy-link]');
  if (spyLinks.length) {
    var spyTargets = [];
    spyLinks.forEach(function (link) {
      var el = document.querySelector(link.getAttribute('data-spy-link'));
      if (el) spyTargets.push({ link: link, el: el });
    });

    var markCurrent = function () {
      var offset = 140;
      var current = spyTargets[0];
      spyTargets.forEach(function (t) {
        if (t.el.getBoundingClientRect().top - offset <= 0) current = t;
      });
      spyLinks.forEach(function (l) { l.classList.remove('is-current'); });
      if (current) current.link.classList.add('is-current');
    };

    window.addEventListener('scroll', markCurrent, { passive: true });
    markCurrent();
  }

  /* ---------------- Simple prev/next carousel (testimonials) --------------
     Direction-aware: scrollBy is mirrored when the page is in RTL. */
  document.querySelectorAll('[data-carousel]').forEach(function (carousel) {
    var track = carousel.querySelector('.snap-row');
    if (!track) return;
    var prev = carousel.querySelector('[data-carousel-prev]');
    var next = carousel.querySelector('[data-carousel-next]');
    function scrollByCard(dir) {
      var card = track.querySelector(':scope > *');
      var amount = card ? card.getBoundingClientRect().width + 24 : 340;
      track.scrollBy({
        left: dir * amount * (isRTL() ? -1 : 1),
        behavior: prefersReducedMotion ? 'auto' : 'smooth'
      });
    }
    if (prev) prev.addEventListener('click', function () { scrollByCard(-1); });
    if (next) next.addEventListener('click', function () { scrollByCard(1); });
  });

  /* ---------------- Password reveal (Login / Register) --------------------
     Markup: <button data-toggle-password="#password-field-id"> */
  document.querySelectorAll('[data-toggle-password]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var field = document.querySelector(btn.getAttribute('data-toggle-password'));
      if (!field) return;
      var reveal = field.type === 'password';
      field.type = reveal ? 'text' : 'password';
      btn.setAttribute('aria-label', reveal ? 'Hide password' : 'Show password');
      var icon = btn.querySelector('i');
      if (icon) icon.className = reveal ? 'ri-eye-off-line' : 'ri-eye-line';
    });
  });

  /* ---------------- Coming soon / maintenance countdown -------------------
     Markup: [data-countdown="2026-12-01T09:00:00"] wrapping
             [data-cd="days|hours|minutes|seconds"] elements. */
  var countdown = document.querySelector('[data-countdown]');
  if (countdown) {
    var deadline = new Date(countdown.getAttribute('data-countdown')).getTime();
    var out = {
      days: countdown.querySelector('[data-cd="days"]'),
      hours: countdown.querySelector('[data-cd="hours"]'),
      minutes: countdown.querySelector('[data-cd="minutes"]'),
      seconds: countdown.querySelector('[data-cd="seconds"]')
    };
    var pad = function (n) { return String(n).padStart(2, '0'); };
    var tick = function () {
      var diff = Math.max(deadline - Date.now(), 0);
      var s = Math.floor(diff / 1000);
      if (out.days) out.days.textContent = pad(Math.floor(s / 86400));
      if (out.hours) out.hours.textContent = pad(Math.floor((s % 86400) / 3600));
      if (out.minutes) out.minutes.textContent = pad(Math.floor((s % 3600) / 60));
      if (out.seconds) out.seconds.textContent = pad(s % 60);
    };
    tick();
    setInterval(tick, 1000);
  }

  /* ---------------- Lazy-image fade-in ---------------- */
  document.querySelectorAll('img[loading="lazy"]').forEach(function (img) {
    if (img.complete) return;
    img.classList.add('img-lazy');
    img.addEventListener('load', function () { img.classList.remove('img-lazy'); }, { once: true });
  });

  /* ---------------- Password strength meter & recommendations -------------
     Evaluates password strength in real-time and updates recommendations & visual bars. */
  var passwordInputs = document.querySelectorAll('[data-password-strength], #reg-password');
  passwordInputs.forEach(function (pwdInput) {
    var labelEl = document.getElementById('password-strength-label');
    var seg1 = document.getElementById('pwd-seg-1');
    var seg2 = document.getElementById('pwd-seg-2');
    var seg3 = document.getElementById('pwd-seg-3');
    var seg4 = document.getElementById('pwd-seg-4');
    var segments = [seg1, seg2, seg3, seg4].filter(Boolean);

    var ruleLength = document.getElementById('pwd-rule-length');
    var ruleCases = document.getElementById('pwd-rule-cases');
    var ruleNumSym = document.getElementById('pwd-rule-num-sym');

    function updateRule(ruleEl, isPass) {
      if (!ruleEl) return;
      var icon = ruleEl.querySelector('i');
      if (isPass) {
        if (icon) icon.className = 'ri-checkbox-circle-fill text-emerald-500 text-xs shrink-0';
        ruleEl.classList.remove('text-ink-400');
        ruleEl.classList.add('text-emerald-700', 'dark:text-emerald-400', 'font-medium');
      } else {
        if (icon) icon.className = 'ri-checkbox-blank-circle-line text-ink-300 dark:text-ink-600 text-xs shrink-0';
        ruleEl.classList.remove('text-emerald-700', 'dark:text-emerald-400', 'font-medium');
        ruleEl.classList.add('text-ink-400');
      }
    }

    function checkStrength() {
      var val = pwdInput.value || '';
      if (!val) {
        if (labelEl) {
          labelEl.textContent = '—';
          labelEl.className = 'font-semibold text-ink-400';
        }
        segments.forEach(function (seg) {
          seg.className = 'h-full rounded-full bg-ink-200 dark:bg-white/10 transition-all duration-300';
        });
        updateRule(ruleLength, false);
        updateRule(ruleCases, false);
        updateRule(ruleNumSym, false);
        return;
      }

      var passLength = val.length >= 8;
      var passCases = /[a-z]/.test(val) && /[A-Z]/.test(val);
      var passNumSym = /[0-9!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?`~]/.test(val);

      updateRule(ruleLength, passLength);
      updateRule(ruleCases, passCases);
      updateRule(ruleNumSym, passNumSym);

      var score = 0;
      if (val.length >= 6) score++;
      if (passLength) score++;
      if (passCases) score++;
      if (passNumSym) score++;

      var level = 1;
      if (score === 3) {
        level = 2;
      } else if (score >= 4) {
        if (val.length >= 10 || (/[0-9]/.test(val) && /[^a-zA-Z0-9]/.test(val))) {
          level = 4;
        } else {
          level = 3;
        }
      }
      var colors = {
        1: { bg: 'bg-red-500', text: 'text-red-500', label: 'Weak' },
        2: { bg: 'bg-amber-500', text: 'text-amber-500', label: 'Fair' },
        3: { bg: 'bg-primary-500', text: 'text-primary-600 dark:text-sand-400', label: 'Good' },
        4: { bg: 'bg-emerald-500', text: 'text-emerald-600 dark:text-emerald-400', label: 'Strong' }
      };

      var active = colors[level];
      if (labelEl) {
        labelEl.textContent = active.label;
        labelEl.className = 'font-semibold ' + active.text;
      }

      segments.forEach(function (seg, idx) {
        if (idx < level) {
          seg.className = 'h-full rounded-full ' + active.bg + ' transition-all duration-300';
        } else {
          seg.className = 'h-full rounded-full bg-ink-200 dark:bg-white/10 transition-all duration-300';
        }
      });
    }

    pwdInput.addEventListener('input', checkStrength);
    pwdInput.addEventListener('focus', checkStrength);
  });

  /* ---------------- Form validation ----------------
     Markup contract: <form data-validate data-success="#success-el" novalidate>
       - every [required] field needs a real <label for> and a sibling
         element with id="<fieldId>-error" that starts hidden
       - data-match="#otherFieldId" cross-checks two fields (password confirm)
     There is no backend in this template: on success the form is hidden and
     the data-success panel is revealed and focused.
  --------------------------------------------------- */
  function validateForm(form) {
    var valid = true;
    form.querySelectorAll('[required]').forEach(function (field) {
      var errorEl = field.id ? document.getElementById(field.id + '-error') : null;
      var fieldValid = field.checkValidity();

      /* Name field validation: must be at least 2 characters, reject single letters or invalid names */
      var isNameField = field.name === 'name' || field.name === 'first' || field.name === 'last' ||
                        field.id === 'c-name' || field.id === 'reg-first' || field.id === 'reg-last' ||
                        field.id === 'start-name' || field.id === 'comment-name' ||
                        field.autocomplete === 'name' || field.autocomplete === 'given-name' || field.autocomplete === 'family-name';

      if (fieldValid && isNameField) {
        var nameVal = (field.value || '').trim();
        var nameRegex = /^[a-zA-ZÀ-ÿ\u0600-\u06FF\u0750-\u077F\u0900-\u097F\s'.\-]{2,}$/;
        if (nameVal.length < 2 || !nameRegex.test(nameVal)) {
          fieldValid = false;
        }
      }

      /* Strict lowercase domain email validation (e.g. gmail.com only, rejecting uppercase domain like GMAIL) */
      if (fieldValid && (field.type === 'email' || field.getAttribute('type') === 'email')) {
        var emailVal = (field.value || '').trim();
        var emailRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?(?:\.[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?)+$/;
        if (!emailRegex.test(emailVal)) {
          fieldValid = false;
        }
      }

      /* Registration password recommendation validation: length >= 8, mixed cases, number or symbol */
      if (fieldValid && (field.id === 'reg-password' || (field.name === 'password' && field.autocomplete === 'new-password'))) {
        var pwdVal = field.value || '';
        var passLength = pwdVal.length >= 8;
        var passCases = /[a-z]/.test(pwdVal) && /[A-Z]/.test(pwdVal);
        var passNumSym = /[0-9!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?`~]/.test(pwdVal);
        if (!passLength || !passCases || !passNumSym) {
          fieldValid = false;
        }
      }

      if (fieldValid && field.hasAttribute('data-match')) {
        var other = document.querySelector(field.getAttribute('data-match'));
        if (other && field.value !== other.value) fieldValid = false;
      }
      field.classList.toggle('field-invalid', !fieldValid);
      field.setAttribute('aria-invalid', fieldValid ? 'false' : 'true');
      if (errorEl) errorEl.classList.toggle('hidden', fieldValid);
      if (!fieldValid) valid = false;
    });
    return valid;
  }

  document.querySelectorAll('form[data-validate]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!validateForm(form)) {
        var firstInvalid = form.querySelector('.field-invalid');
        if (firstInvalid) firstInvalid.focus();
        return;
      }
      var successSelector = form.getAttribute('data-success');
      var successEl = successSelector ? document.querySelector(successSelector) : null;
      if (successEl) {
        form.classList.add('hidden');
        successEl.classList.remove('hidden');
        successEl.setAttribute('tabindex', '-1');
        successEl.focus();
      }
      form.reset();
    });

    /* Clear the invalid state as soon as the visitor fixes a field */
    form.querySelectorAll('[required]').forEach(function (field) {
      ['input', 'change', 'blur'].forEach(function (evtName) {
        field.addEventListener(evtName, function () {
          if (field.classList.contains('field-invalid')) validateForm(form);
        });
      });
    });
  });

  /* ---------------- Interactive info modal popup ---------------------------
     Shows an informative popup when placeholder/legal/info links are clicked
     instead of jumping to '#' or breaking navigation. */
  var modalEl = null;

  function createInfoModal() {
    if (modalEl) return modalEl;
    modalEl = document.createElement('div');
    modalEl.id = 'info-modal';
    modalEl.className = 'fixed inset-0 z-50 flex items-center justify-center p-4 bg-ink-950/70 backdrop-blur-sm opacity-0 pointer-events-none transition-opacity duration-300';
    modalEl.setAttribute('role', 'dialog');
    modalEl.setAttribute('aria-modal', 'true');
    modalEl.setAttribute('aria-labelledby', 'info-modal-title');
    modalEl.innerHTML = 
      '<div class="relative w-full max-w-lg rounded-2xl bg-white dark:bg-primary-900 border border-ink-200 dark:border-white/10 p-6 sm:p-8 shadow-2xl transform scale-95 transition-transform duration-300 max-h-[90vh] overflow-y-auto text-start">' +
        '<button type="button" id="info-modal-close" aria-label="Close dialog" class="absolute top-4 end-4 w-9 h-9 rounded-xl flex items-center justify-center text-ink-400 hover:text-primary-600 hover:bg-ink-100 dark:hover:bg-white/10 transition">' +
          '<i class="ri-close-line text-xl"></i>' +
        '</button>' +
        '<div class="flex items-center gap-3.5 mb-4">' +
          '<span class="w-11 h-11 rounded-xl bg-primary-50 dark:bg-white/10 text-primary-600 dark:text-sand-300 flex items-center justify-center shrink-0">' +
            '<i id="info-modal-icon" class="ri-information-line text-2xl"></i>' +
          '</span>' +
          '<div>' +
            '<span class="text-xs uppercase tracking-wider font-semibold text-sand-500">Willbridge Legal Notice</span>' +
            '<h3 id="info-modal-title" class="font-serif text-xl font-bold text-primary-900 dark:text-white"></h3>' +
          '</div>' +
        '</div>' +
        '<div id="info-modal-body" class="text-sm leading-relaxed text-ink-600 dark:text-ink-300 space-y-3"></div>' +
        '<div class="mt-6 pt-5 border-t border-ink-100 dark:border-white/10 flex justify-end gap-3">' +
          '<button type="button" id="info-modal-ok" class="px-5 py-2.5 rounded-xl bg-primary-600 hover:bg-primary-700 text-white text-sm font-semibold shadow-soft transition">Understood</button>' +
        '</div>' +
      '</div>';

    document.body.appendChild(modalEl);

    function closeModal() {
      modalEl.classList.remove('opacity-100', 'pointer-events-auto');
      modalEl.classList.add('opacity-0', 'pointer-events-none');
      var inner = modalEl.querySelector('div');
      if (inner) {
        inner.classList.remove('scale-100');
        inner.classList.add('scale-95');
      }
    }

    modalEl.querySelector('#info-modal-close').addEventListener('click', closeModal);
    modalEl.querySelector('#info-modal-ok').addEventListener('click', closeModal);
    modalEl.addEventListener('click', function (e) {
      if (e.target === modalEl) closeModal();
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && modalEl.classList.contains('opacity-100')) {
        closeModal();
      }
    });

    return modalEl;
  }

  function showInfoModal(title, contentHtml, iconClass) {
    var modal = createInfoModal();
    var titleEl = modal.querySelector('#info-modal-title');
    var bodyEl = modal.querySelector('#info-modal-body');
    var iconEl = modal.querySelector('#info-modal-icon');

    if (titleEl) titleEl.textContent = title;
    if (bodyEl) bodyEl.innerHTML = contentHtml;
    if (iconEl) iconEl.className = (iconClass || 'ri-information-line') + ' text-2xl';

    modal.classList.remove('opacity-0', 'pointer-events-none');
    modal.classList.add('opacity-100', 'pointer-events-auto');
    var inner = modal.querySelector('div');
    if (inner) {
      inner.classList.remove('scale-95');
      inner.classList.add('scale-100');
    }
    var okBtn = modal.querySelector('#info-modal-ok');
    if (okBtn) okBtn.focus();
  }

  /* Listen for clicks on footer/info links and other placeholder links */
  document.addEventListener('click', function (e) {
    var link = e.target.closest('a[href="#"]');
    if (!link) return;
    e.preventDefault();

    var text = (link.textContent || '').trim();
    var label = link.getAttribute('aria-label') || '';

    if (text === 'Privacy Policy') {
      showInfoModal(
        'Privacy Policy',
        '<p>At Willbridge Legacy Planning, we handle delicate family testamentary and estate data with strict confidentiality. All records are stored with end-to-end encryption at rest and access is strictly audited.</p><p class="text-xs text-ink-400 dark:text-ink-400">Personal information submitted through consultation requests is never sold, leased, or transmitted to third parties without your explicit written instruction.</p>',
        'ri-shield-check-line'
      );
    } else if (text === 'Terms of Service') {
      showInfoModal(
        'Terms of Service',
        '<p>Our advisory and estate-planning legal services operate on transparent, upfront fixed-fee arrangements agreed in writing before work commences.</p><p class="text-xs text-ink-400 dark:text-ink-400">No client–solicitor relationship is created merely by browsing this website or submitting general inquiries until formal engagement terms are executed.</p>',
        'ri-file-text-line'
      );
    } else if (text === 'Client Confidentiality') {
      showInfoModal(
        'Client Confidentiality',
        '<p>Client privilege and uncompromised discretion are the foundations of our practice. Nothing discussed during consultations or drafting sessions is ever shared with family members, financial institutions, or external parties without written mandate.</p>',
        'ri-lock-2-line'
      );
    } else if (label.indexOf('Facebook') !== -1 || label.indexOf('X') !== -1 || label.indexOf('LinkedIn') !== -1 || label.indexOf('WhatsApp') !== -1) {
      showInfoModal(
        'Connect with Willbridge',
        '<p>Our official channels and social advisory pages are maintained for informative updates on succession and probate law. For direct inquiries, please contact our Bengaluru practice at <strong class="text-primary-700 dark:text-sand-300">hello@willbridge.example</strong>.</p>',
        'ri-share-forward-line'
      );
    } else {
      showInfoModal(
        text || 'Notice',
        '<p>This section is part of the Willbridge Estate & Succession advisory framework. Full documentation and detailed schedules are available upon consultation request.</p>',
        'ri-information-line'
      );
    }
  });

})();
