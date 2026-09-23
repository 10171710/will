# Willbridge — Will &amp; Estate Planning HTML Template

A complete, production-ready multipurpose HTML template for service-based businesses, built
around a will &amp; estate planning practice. Fourteen hand-written pages, no build step, no
dependencies to install — open `index.html` and it runs.

Suitable for ThemeForest / TemplateMonster listings or direct client projects.

---

## What is in the box

```
willbridge-estate-template/
├── index.html              Home 1 — classic advisory landing page
├── home-2.html             Home 2 — niche, product-led (online will platform)
├── about.html              Team, mission, values, history, testimonials
├── services.html           Filterable / searchable grid of nine services
├── service-details.html    ★ The complete guide — see below
├── blog.html               Journal index, searchable + category filters
├── blog-details.html       Article: Who Can Witness Your Will
├── blog-probate-timeline.html  Article: Realistic Probate Timeline
├── blog-family-trust.html  Article: When a Family Trust is Worth It
├── blog-parent-conversation.html Article: How to Raise the Subject with Parents
├── blog-nominee-heir.html  Article: A Nominee Is Not an Heir
├── blog-executor-checklist.html Article: Executor's 30-Day Checklist
├── blog-special-needs-care.html Article: Providing for a Special Needs Child
├── blog-digital-estate.html Article: Your Digital Estate & Passwords
├── blog-contest-proof-will.html Article: Six Things to Make a Will Harder to Contest
├── contact.html            Confidential consultation booking form + map
├── pricing.html            Packages, comparison table, add-ons, fee FAQ
├── login.html              Split-screen client sign-in
├── register.html           Split-screen account creation
├── 404.html                Not-found page with search and quick links
├── coming-soon.html        Launch page with live countdown
├── maintenance.html        Scheduled-maintenance holding page
├── assets/
│   ├── css/style.css       ~330 lines of hand-written CSS on top of Tailwind
│   ├── js/main.js          ~430 lines of vanilla JS — no jQuery, no framework
│   └── images/             High-resolution professional photography
├── docs/index.html         Developer documentation (open in a browser)
└── README.md
```

### ★ service-details.html — Estate Guide (3 core sections)

Rather than scattering thin pages across the menu, the in-depth estate planning and probate content lives on a spacious, full-width landing page with three core sections:

| Section id | Section Title | Content & Features |
| --- | --- | --- |
| `#probate-assistance` | **Probate Assistance** | 4-stage court process pipeline, executor documentation checklists, what Willbridge handles vs client responsibilities, and caution advisories |
| `#why-plan-early` | **Why Plan Early** | Comprehensive side-by-side comparison matrix (planning ahead vs dying intestate), life-stage triggers (parents, property, business, NRIs), and impact stats |
| `#faq` | **Frequently Asked Questions** | 20 searchable and filterable legal questions with category pills (Probate, Wills, Trusts, Fees), expand/collapse controls, and help contact callout |

Anything in the site can deep-link straight to a section, e.g.
`service-details.html#probate-assistance`, `service-details.html#why-plan-early`, or `service-details.html#faq`.

---

## Navigation
 
The primary menu is clean and structured — five main entries with intuitive dropdowns:

```
Home ▾     →  Home 1 — Legacy Practice   (index.html)
              Home 2 — Online Will Platform (home-2.html)
About             (about.html)
Services          (services.html)
Estate Guide      (service-details.html)
Blog              (blog.html)
Contact           (contact.html)
```

Probate Assistance, Why Plan Early, and the FAQ Knowledge Hub are unified together under **one comprehensive page (`service-details.html`)** accessible via the dedicated **Estate Guide** navbar heading, while **Services** is a direct link to `services.html`.

To change the menu, edit the `<nav aria-label="Primary">` block and the matching
`#mobile-menu` block in the header. Both appear in every page with site chrome — the header
markup is byte-identical across pages, so a find-and-replace across all `*.html` is safe.
Mark the current page by adding `nav-active` to its link.

---

## Design system

| Token | Value | Used for |
| --- | --- | --- |
| `primary-600` | `#2d5f56` | Evergreen — buttons, headings, brand |
| `sand-500` | `#c08a4b` | Warm sand accent — rules, icons, highlights |
| `ink-*` | warm greys | Body copy, borders, muted text |
| `paper` | `#fbfaf8` | Page background in light mode |

Fonts: **Lora** for headings (`.font-serif`), **Plus Jakarta Sans** for everything else.
Both load from Google Fonts; swap the `<link>` and the `tailwind.config` block in each
page's `<head>` to rebrand.

Tailwind is loaded from the Play CDN so the template runs from the filesystem with no
tooling. For production, install Tailwind and compile a minified stylesheet — the class
names need no changes.

---

## Dark mode

Class-based (`darkMode: 'class'`). A tiny pre-paint script in every `<head>` reads
`localStorage['wb-theme']` and applies `.dark` **before first paint**, so there is no flash
of the wrong theme. The toggle is `#theme-toggle`; the default is light.

## RTL support

The whole template mirrors by flipping one attribute — `<html dir="rtl">`. The
`#dir-toggle` button does this and persists the choice in `localStorage['wb-dir']`; the
same pre-paint script restores it and sets `lang="ar"`.

This works because **no physical-direction utility is used anywhere in the markup**:

| Never used | Used instead |
| --- | --- |
| `ml-*` / `mr-*` | `ms-*` / `me-*` |
| `pl-*` / `pr-*` | `ps-*` / `pe-*` |
| `left-*` / `right-*` | `start-*` / `end-*` |
| `text-left` / `text-right` | `text-start` / `text-end` |
| `border-l` / `border-r` | `border-s` / `border-e` |

The stylesheet does the same with logical properties (`inset-inline-start`,
`padding-inline-start`, `border-inline-start`) and mirrors the handful of things CSS cannot
flip on its own, all under `[dir="rtl"]`:

* gradient rules (`.rule-sand`, `.timeline-line-h`) reverse direction,
* the marquee reverses its animation,
* the pull-quote glyph switches from `"` to `"`,
* the centred pricing badge flips its translate,
* directional arrows carry `.rtl-flip` (`transform: scaleX(-1)`),
* the testimonial carousel negates its scroll delta in JS.

**When adding markup, keep to the logical utilities and add `.rtl-flip` to any arrow that
points "forwards".** That is the whole contract.

---

## JavaScript hooks

`assets/js/main.js` is one IIFE with no dependencies (AOS is optional). Everything is
driven by data attributes, so new markup needs no new script:

| Hook | What it does |
| --- | --- |
| `#theme-toggle` / `#dir-toggle` | Dark mode and RTL, both persisted |
| `#mobile-menu-btn` + `#mobile-menu` | Mobile navigation |
| `[data-mobile-toggle="id"]` | Mobile accordion sub-menu |
| `nav .group` + `button` | Click-based desktop dropdown (touch friendly) |
| `[data-counter="98"] [data-suffix="%"]` | Count-up animation on scroll into view |
| `[data-filter-root]` | Filter/search engine — see below |
| `[data-tabs]`, `[data-tab]`, `[data-tab-panel]` | Generic tabs |
| `[data-faq-expand]` / `[data-faq-collapse]` | Expand or collapse a `details` group |
| `[data-carousel]` + `.snap-row` | Prev/next carousel, direction aware |
| `[data-spy-link="#id"]` | Scroll-spy for the in-page rail |
| `[data-price-switch]` + `[data-price-standard]` | Pricing billing switch |
| `[data-toggle-password="#id"]` | Password reveal |
| `[data-countdown="ISO date"]` + `[data-cd="days"]` | Countdown timer |
| `form[data-validate][data-success="#el"]` | Client-side validation |

### The filter engine

```html
<div data-filter-root>
  <input data-filter-search>
  <button data-filter-btn="all" class="is-active">All</button>
  <button data-filter-btn="probate">Probate</button>
  <span data-filter-count>9</span>

  <article data-filter-item
           data-category="probate guides"
           data-title="words the search box should match">…</article>

  <p data-filter-empty class="hidden">No results</p>
</div>
```

Used by the services grid, the blog index and the twenty-question FAQ.

### Form validation

```html
<form data-validate data-success="#thanks" novalidate>
  <label for="email">Email</label>
  <input id="email" type="email" required>
  <p id="email-error" class="hidden">Please enter a valid email address.</p>
</form>
<p id="thanks" class="hidden">Thank you.</p>
```

Every `[required]` field needs a sibling `<p id="<fieldId>-error" class="hidden">`. Add
`data-match="#otherField"` to cross-check two fields (used for password confirmation). On
success the form is hidden and the `data-success` panel is revealed and focused.

**There is no backend.** Wire the `submit` handler in `main.js` to your own endpoint.

---

## Accessibility

* Skip link on every page, visible on focus.
* One `<h1>` per page and a sane heading order beneath it.
* Landmarks throughout: `header`, `nav[aria-label]`, `main`, `aside`, `footer`.
* Visible focus rings on every interactive element (`:focus-visible`).
* Real `<label for>` on every input; errors are announced by `aria-invalid`.
* Data tables use `<caption class="sr-only">`, `scope="col"` and `scope="row"`.
* Decorative icons and images are `aria-hidden` or carry an empty `alt`.
* `prefers-reduced-motion` disables AOS, the marquee, card lifts and smooth scrolling.

### The AOS safety net — please do not delete

AOS ships `[data-aos^="fade"][data-aos^="fade"] { opacity: 0 }`, a deliberately doubled
selector that outranks a plain fallback. If the AOS script never runs — JavaScript
disabled, CDN blocked by a corporate proxy, an earlier script error — every animated
section would stay invisible to readers and crawlers alike. `style.css` therefore ends with:

```css
[data-aos]:not(.aos-init) { opacity: 1 !important; transform: none !important; }
```

AOS adds `.aos-init` the instant it initialises, so this reveals everything when AOS is
absent and steps aside completely when it is present.

---

## SEO

Each page carries a unique `<title>` and meta description, a canonical URL, full Open Graph
and Twitter card tags, and semantic sectioning. `index.html` includes `LegalService`
JSON-LD structured data — update the name, address, telephone and rating, or swap
`@type` for whatever your client actually is.

Utility pages (`login`, `register`, `404`, `coming-soon`, `maintenance`) are marked
`noindex, follow`.

---

## Browser support

Current Chrome, Edge, Firefox and Safari, plus iOS and Android. Layout relies on CSS grid,
flexbox and logical properties; there is no IE support and none is planned.

---

## Customising checklist

1. **Brand name** — search for `Willbridge` across `*.html`.
2. **Colours** — edit the `tailwind.config` block in each `<head>`, plus the hard-coded
   hex values in `assets/css/style.css` (`#2d5f56`, `#c08a4b`).
3. **Fonts** — swap the Google Fonts `<link>` and the `fontFamily` config.
4. **Contact details** — `+91 80 4555 0142`, `hello@willbridge.example`,
   `27 Richmond Row`, and the JSON-LD block in `index.html`.
5. **Images** — every image is a `placehold.co` or `i.pravatar.cc` placeholder. Replace the
   `src` values; the `width`/`height` attributes are already set to prevent layout shift.
6. **Map** — `contact.html` embeds OpenStreetMap. Swap the `<iframe src>` for your provider.
7. **Forms** — point `main.js` at your endpoint.
8. **Fees** — the figures throughout are illustrative placeholders.

---

## Content note

The estate-planning copy in this template is illustrative placeholder text written for
demonstration. It is **not legal advice**, and the fees, timelines and procedural details
are indicative only — succession law varies by jurisdiction. Replace it with copy reviewed
by the practitioner who will actually be using the site.

---

## Licence

Sold as a standard HTML template. Third-party assets used via CDN keep their own licences:
Tailwind CSS (MIT), Remix Icon (Apache 2.0), AOS (MIT), Google Fonts (OFL).
