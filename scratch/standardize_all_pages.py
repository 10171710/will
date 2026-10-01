import glob
import re
import os

# 1. Inspect and standardize header buttons
# 2. Inspect and ensure clean hero-media background styles
# 3. Ensure no duplicates and all files exist

HERO_MAP = {
    'index.html': 'assets/images/estate-property-hero.jpg',
    'home-2.html': 'assets/images/service-business-succession.jpg',
    'about.html': 'assets/images/about-consulting-room.jpg',
    'services.html': 'assets/images/service-will-drafting.jpg',
    'service-details.html': 'assets/images/service-trust-creation.jpg',
    'blog.html': 'assets/images/organised-family-folder.jpg',
    'blog-details.html': 'assets/images/blog-witnessing-will.jpg',
    'blog-contest-proof-will.html': 'assets/images/blog-contest-proof-will.jpg',
    'blog-digital-estate.html': 'assets/images/blog-digital-estate.jpg',
    'blog-executor-checklist.html': 'assets/images/blog-executor-checklist.jpg',
    'blog-family-trust.html': 'assets/images/blog-family-trust.jpg',
    'blog-nominee-heir.html': 'assets/images/blog-nominee-heir.jpg',
    'blog-parent-conversation.html': 'assets/images/blog-parent-conversation.jpg',
    'blog-probate-timeline.html': 'assets/images/blog-probate-timeline.jpg',
    'blog-special-needs-care.html': 'assets/images/blog-special-needs-care.jpg',
    'contact.html': 'assets/images/estate-consultation.jpg',
    'pricing.html': 'assets/images/estate-investment.jpg',
    'login.html': 'assets/images/hero-quiet-conversation.jpg',
    'register.html': 'assets/images/service-power-attorney.jpg',
    '404.html': 'assets/images/service-estate-review.jpg',
    'coming-soon.html': 'assets/images/service-property-deeds.jpg',
    'maintenance.html': 'assets/images/property-inspection.jpg',
}

# Verify uniqueness
used_images = set()
for page, img in HERO_MAP.items():
    if not os.path.exists(img):
        print(f"ERROR: Image {img} for {page} does not exist!")
    if img in used_images:
        print(f"ERROR: Duplicate image {img} in {page}!")
    used_images.add(img)

print(f"Verified {len(HERO_MAP)} unique existing hero images.")

# Header buttons template for dark headers (standard across 20 pages + header partial)
DARK_HEADER_BTNS = '''        <button id="dir-toggle" title="Toggle RTL / LTR" aria-label="Toggle text direction" aria-pressed="false" class="header-icon-btn w-9 h-9 sm:w-10 sm:h-10 inline-flex items-center justify-center rounded-xl bg-white/10 hover:bg-white/20 active:bg-white/25 text-white border border-white/20 hover:border-white/30 shadow-xs transition duration-200 shrink-0">
          <i class="ri-arrow-left-right-line text-base sm:text-lg"></i>
        </button>
        <button id="theme-toggle" title="Toggle dark / light mode" aria-label="Toggle dark or light mode" aria-pressed="false" class="header-icon-btn w-9 h-9 sm:w-10 sm:h-10 inline-flex items-center justify-center rounded-xl bg-white/10 hover:bg-white/20 active:bg-white/25 text-white border border-white/20 hover:border-white/30 shadow-xs transition duration-200 shrink-0">
          <i class="ri-moon-line text-base sm:text-lg"></i>
        </button>'''

LIGHT_HEADER_BTNS = '''        <button id="dir-toggle" title="Toggle RTL / LTR" aria-label="Toggle text direction" aria-pressed="false" class="header-icon-btn header-icon-btn--light w-9 h-9 sm:w-10 sm:h-10 inline-flex items-center justify-center rounded-xl bg-ink-100 dark:bg-white/10 hover:bg-ink-200 dark:hover:bg-white/20 text-ink-800 dark:text-white border border-ink-300/80 dark:border-white/20 shadow-xs transition duration-200 shrink-0">
          <i class="ri-arrow-left-right-line text-base sm:text-lg"></i>
        </button>
        <button id="theme-toggle" title="Toggle dark / light mode" aria-label="Toggle dark or light mode" aria-pressed="false" class="header-icon-btn header-icon-btn--light w-9 h-9 sm:w-10 sm:h-10 inline-flex items-center justify-center rounded-xl bg-ink-100 dark:bg-white/10 hover:bg-ink-200 dark:hover:bg-white/20 text-ink-800 dark:text-white border border-ink-300/80 dark:border-white/20 shadow-xs transition duration-200 shrink-0">
          <i class="ri-moon-line text-base sm:text-lg"></i>
        </button>'''

pages = sorted(glob.glob('*.html'))
for p in pages:
    content = open(p, 'r', encoding='utf-8').read()
    
    # Update hero media style
    if p in HERO_MAP:
        img_path = HERO_MAP[p]
        # Replace hero-media div
        if p in ['login.html', 'register.html']:
            hero_media_tag = f'<div class="hero-media hero-media--panel" style="background-image: url(\'{img_path}\');" aria-hidden="true"></div>'
            content = re.sub(r'<div class="hero-media[^"]*"[^>]*aria-hidden="true"></div>', hero_media_tag, content)
        else:
            hero_media_tag = f'<div class="hero-media" style="background-image: url(\'{img_path}\');" aria-hidden="true"></div>'
            content = re.sub(r'<div class="hero-media[^"]*"[^>]*aria-hidden="true"></div>', hero_media_tag, content)
    
    # Update header buttons
    # Pattern to match both buttons
    btn_pattern = re.compile(r'<button id="dir-toggle"[\s\S]*?</button>\s*<button id="theme-toggle"[\s\S]*?</button>')
    alt_btn_pattern = re.compile(r'<button id="theme-toggle"[\s\S]*?</button>\s*<button id="dir-toggle"[\s\S]*?</button>')
    
    target_btns = LIGHT_HEADER_BTNS if p in ['login.html', 'register.html'] else DARK_HEADER_BTNS
    
    if btn_pattern.search(content):
        content = btn_pattern.sub(target_btns.strip(), content)
    elif alt_btn_pattern.search(content):
        content = alt_btn_pattern.sub(target_btns.strip(), content)
    else:
        print(f"WARNING: Buttons not matched in {p}")
        
    open(p, 'w', encoding='utf-8').write(content)
    print(f"Updated {p}")

# Also update docs/partials/header.html
partial_path = 'docs/partials/header.html'
if os.path.exists(partial_path):
    c = open(partial_path, 'r', encoding='utf-8').read()
    btn_pattern = re.compile(r'<button id="dir-toggle"[\s\S]*?</button>\s*<button id="theme-toggle"[\s\S]*?</button>')
    if btn_pattern.search(c):
        c = btn_pattern.sub(DARK_HEADER_BTNS.strip(), c)
        open(partial_path, 'w', encoding='utf-8').write(c)
        print("Updated docs/partials/header.html")

print("All standardization complete.")
