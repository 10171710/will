# Willbridge — Design System &amp; Build Rules

Read this once before adding or editing a page. The template is a **Will &amp; Estate
Planning Service** business site called **Willbridge Legacy Planning**. Every page,
heading, card, testimonial, FAQ and statistic must be about estate planning: wills,
trusts, succession certificates, probate, executors, beneficiaries, guardianship, safe
custody of documents. No generic "digital agency", SaaS or e-commerce copy anywhere —
including on Home 2, which is the *online will platform* variant of the same practice.

---

## 1. Tone of voice (strict — this is the whole brief)

The brief asked for a **calm, respectful** layout. That constrains the copy as much as
the CSS.

- **Never use fear or urgency as a sales lever.** No "Don't leave your family destitute!",
  no scarcity timers on service pages, no "Act now". The motivating emotion is *relief and
  care*, not panic. (The countdown on `coming-soon.html` is a launch date, not a threat.)
- Plain language over legalese. Where a legal term is unavoidable — *intestate*, *probate*,
  *executor*, *residuary* — gloss it in the same sentence.
- Short, unhurried sentences. Reassure about **confidentiality** often.
- Acknowledge that people arrive here at hard moments (a bereavement, a diagnosis). The
  bereavement-adjacent sections — probate, succession certificates — get the gentlest copy
  on the site.
- Be honest about cost and duration. "Nine to fourteen months" beats a comfortable number
  the reader will resent later. Honesty *is* the brand.
- Motion is subtle: soft fades, no bounces, no parallax. All animation is suppressed under
  `prefers-reduced-motion` (already handled in `style.css` and `main.js`).
- **No legal advice.** Copy describes a *service*; it never asserts what the law is in a
  way a reader could act on. The footer disclaimer is mandatory on every page with chrome.

---

## 2. Stack constraints (non-negotiable)

- **No build step.** Tailwind via the CDN script (`https://cdn.tailwindcss.com`) — never
  npm/postcss. Every page must open directly over `file://` and work.
- Vanilla JS only (`assets/js/main.js`, already written). Read its markup contracts before
  adding interactive markup, and reuse its hooks rather than writing inline scripts.
- Semantic HTML5: `<header>`, `<nav aria-label>`, `<main id="main">`, `<section>`,
  `<article>`, `<footer>`; exactly one `<h1>` per page; no skipped heading levels.
- Mobile-first responsive, dark **and** light mode, RTL-ready.
- SEO: unique `<title>` and meta description per page, canonical link, OG/Twitter tags.
  JSON-LD (`LegalService`) on `index.html` only.
- Accessibility: the skip link lives in the header partial, so **every page needs
  `<main id="main">`**. Icon-only buttons need `aria-label`.

---

## 3. Brand

- Name: **Willbridge Legacy Planning** ("Willbridge" in running copy).
- Logo: `ri-quill-pen-line` in an evergreen rounded square, wordmark `Will` + `bridge`
  with `bridge` in sand, and a small `LEGACY PLANNING` line beneath at `sm:` and up.
  Taken from `docs/partials/header.html` — reuse verbatim, never redesign it.
- **Primary/brand colour:** `primary-600` (`#2d5f56`, evergreen).
  **Accent:** `sand-500` (`#c08a4b`) — eyebrows, icons, rules, hover states, the footer
  newsletter button. Neutral scale: `ink-*` (warm greys). Page background: `paper`
  (`#fbfaf8`) in light mode, `ink-950` in dark.
- Fonts: **Lora** for headings (`.font-serif`), **Plus Jakarta Sans** for body.

### Colour scales

| Scale | 600 / key value | Purpose |
| --- | --- | --- |
| `primary` | `#2d5f56` | Buttons, headings, brand, dark panels (`primary-900/950`) |
| `sand` | `#c08a4b` | Accent only — never a large background in light mode |
| `ink` | `#5c5c56` (600) | Body copy, borders (`ink-200`), muted text (`ink-400`) |
| `paper` | `#fbfaf8` | Light-mode page background |

### Shadows and radii

`shadow-soft` for raised brand elements, `shadow-card` for resting cards, `shadow-glow`
for sand CTAs on dark panels. Cards are `rounded-2xl`; large panels `rounded-3xl`.

---

## 4. Page inventory

| File | Nav entry | Purpose |
| --- | --- | --- |
| `index.html` | Home ▾ → Home 1 | Classic advisory landing page |
| `home-2.html` | Home ▾ → Home 2 | Niche, product-led online will platform |
| `about.html` | About | Team, mission, values, history, testimonials |
| `services.html` | Services | Filterable grid of nine services |
| `service-details.html` | — (linked from Services) | **The complete guide**, see §5 |
| `blog.html` | Blog | Journal index, searchable |
| `blog-details.html` | — | Article with sticky sidebar and comments |
| `contact.html` | Contact | Consultation booking form and map |
| `pricing.html` | — (footer) | Packages, comparison, add-ons, fee FAQ |
| `login.html` / `register.html` | — (footer) | Split-screen auth, no chrome |
| `404.html` | — | Not found, minimal chrome |
| `coming-soon.html` | — | Countdown launch page, no chrome |
| `maintenance.html` | — | Holding page, minimal chrome |

**There is no admin dashboard in this template**, by design.

### Menu rule

The primary menu has exactly five main entries with dropdown navigation for Home and Services:

```
Home ▾ (Home 1, Home 2) · About · Services ▾ (All Services, The Complete Guide [Probate, Why Plan Early, FAQ]) · Blog · Contact
```

Do not add separate top-level pages in the navbar for individual sub-topics. Probate assistance, "Why Plan Early" and the FAQ
are **consolidated under one unified guide page (`service-details.html`)**, accessible directly via the Services dropdown and internal anchor links.

---

## 5. service-details.html — the one detailed page

A sticky rail (`aside` at `lg` and up) plus a horizontally scrolling pill bar on mobile,
both driven by `[data-spy-link]` scroll-spy. Section ids, in order:

`#overview` → `#will-drafting` → `#trust-creation` → `#succession-certificates` →
`#probate-assistance` → `#process` → `#why-plan-early` → `#fees` → `#faq`

Rules for this page:

- Every section is `scroll-mt-32` so the fixed header never covers its heading.
- Adding a section means adding it to **both** navs (rail and pills) with matching
  `data-spy-link`.
- `#fees` uses the generic tab hooks; the two panels are `[data-tab-panel="individual"]`
  and `[data-tab-panel="couple"]`.
- `#faq` is a `[data-filter-root]` with twenty `[data-filter-item]` accordions. Each needs
  `data-category` (one or more of `wills trusts succession probate fees`) and a
  `data-title` containing every word the search box should match.

---

## 6. Layout conventions

- Page container: `max-w-7xl mx-auto px-4 sm:px-6 lg:px-8`.
- Section rhythm: `py-20 sm:py-24` for major sections, `py-16 sm:py-20` for secondary ones.
- Alternating section backgrounds: transparent (`paper`) then
  `bg-white dark:bg-primary-950/30 border-y border-ink-200 dark:border-white/10`.
- Every page with chrome opens `<main id="main" class="pt-[78px]">` — the header is fixed
  at `h-[78px]`.
- Section heading block: `.eyebrow` → `h2` in `font-serif` → `<hr class="rule-sand">` →
  lead paragraph.
- Cards: `rounded-2xl bg-white dark:bg-primary-900/40 border border-ink-200
  dark:border-white/10 p-7 shadow-card`, plus `card-hover` when the whole card is a link.
- Dark CTA panels: `bg-gradient-to-br from-primary-700 to-primary-950` with a `.blob-bg`
  wash and a `sand-500` primary button.

---

## 7. RTL contract

The whole template mirrors by flipping `<html dir>`. That only keeps working if new markup
obeys the contract:

| Never use | Use instead |
| --- | --- |
| `ml-*` / `mr-*` | `ms-*` / `me-*` |
| `pl-*` / `pr-*` | `ps-*` / `pe-*` |
| `left-*` / `right-*` | `start-*` / `end-*` |
| `text-left` / `text-right` | `text-start` / `text-end` |
| `border-l` / `border-r` | `border-s` / `border-e` |
| `rounded-l-*` / `rounded-r-*` | `rounded-s-*` / `rounded-e-*` |

`inset-x-*` and symmetric spacing are fine. In CSS use logical properties
(`inset-inline-start`, `padding-inline-start`, `border-inline-start`).

Things CSS cannot mirror on its own are already handled under `[dir="rtl"]` in
`style.css` — gradient rules, marquee direction, the pull-quote glyph, the centred pricing
badge — plus two conventions you must follow yourself:

1. **Any arrow that points "forwards" gets `.rtl-flip`.** For example
   `<i class="ri-arrow-right-line rtl-flip"></i>`.
2. **Anything that scrolls horizontally in JS must negate its delta in RTL.** The
   testimonial carousel in `main.js` shows the pattern (`isRTL()`).

Test by clicking `#dir-toggle` and confirming the page has no horizontal scrollbar
(`document.documentElement.scrollWidth === clientWidth`) at 1440px and at 375px.

---

## 8. Dark mode contract

Class-based. The pre-paint script in `docs/partials/head-public.html` applies `.dark`
before first paint, so **every new page must include that script** or it will flash.

Pairings used throughout — keep to them:

| Light | Dark |
| --- | --- |
| `bg-paper` | `dark:bg-ink-950` |
| `bg-white` | `dark:bg-primary-900/40` |
| `border-ink-200` | `dark:border-white/10` |
| `text-primary-800` (headings) | `dark:text-white` |
| `text-ink-500` (body) | `dark:text-ink-400` |
| `text-primary-600` (links) | `dark:text-sand-300` |

Never leave a colour defined only for one mode.

---

## 9. Partials

`docs/partials/` holds the three blocks that must stay byte-identical across pages:

- `head-public.html` — everything from `<!DOCTYPE html>` to `<body …>`, with
  `{{PAGE_TITLE}}`, `{{PAGE_DESCRIPTION}}`, `{{PAGE_FILENAME}}`, `{{OG_IMAGE}}` and
  `{{OPTIONAL_JSON_LD}}` placeholders.
- `header.html` — skip link + fixed header + mobile menu. After pasting, add `nav-active`
  to the current page's link in **both** the desktop nav and the mobile nav.
- `footer.html` — footer, disclaimer, back-to-top button and the two script tags, through
  to `</html>`.

Because the chrome is identical everywhere, a find-and-replace across all `*.html` is a
safe way to change the menu or the footer.

---

## 10. Accessibility checklist for a new page

- [ ] `<main id="main">` present (the skip link targets it)
- [ ] Exactly one `<h1>`, no skipped heading levels
- [ ] Every `<nav>` has an `aria-label`
- [ ] Icon-only buttons have `aria-label`; decorative icons are `aria-hidden` or in a
      wrapper with an accessible name
- [ ] Every input has a real `<label for>`; required inputs have a
      `<p id="<fieldId>-error" class="hidden">`
- [ ] Tables have `<caption class="sr-only">`, `scope="col"` and `scope="row"`
- [ ] Decorative images use `alt=""`; meaningful ones describe the content
- [ ] `width`/`height` on every `<img>` to prevent layout shift
- [ ] Nothing conveys meaning by colour alone
- [ ] The page still reads correctly with JavaScript disabled (the AOS safety net at the
      bottom of `style.css` guarantees this — do not delete it)
