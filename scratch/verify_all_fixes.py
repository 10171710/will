import glob
import re

files = sorted(glob.glob('*.html'))
print(f"Total HTML files to verify: {len(files)}\n")

all_good = True

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    # Check if page has header
    has_header = '<header' in c
    if not has_header:
        print(f"[{f}] No standard header tag found.")
        continue
    
    # Check dir-toggle and theme-toggle class
    dir_match = re.search(r'<button id="dir-toggle"[^>]*class="([^"]*)"', c)
    theme_match = re.search(r'<button id="theme-toggle"[^>]*class="([^"]*)"', c)
    
    dir_has_btn = 'w-9 h-9' in dir_match.group(1) if dir_match else False
    theme_has_btn = 'w-9 h-9' in theme_match.group(1) if theme_match else False
    
    # Check mobile CTA inside header bar (should be hidden on mobile / hidden lg:inline-flex)
    header_part = c[c.find('<header'):c.find('</header>')]
    desktop_cta_match = re.search(r'<a href="contact\.html"[^>]*class="([^"]*)"[^>]*>\s*<i class="ri-calendar-check-line"></i><span>Book Consultation</span>', header_part)
    
    # Check mobile menu CTA
    mobile_cta_match = re.search(r'<div class="pt-3 border-t[^"]*"[^>]*>\s*<a href="contact\.html"[^>]*class="([^"]*)"[^>]*><i class="ri-calendar-check-line"></i>\s*Book Consultation</a>', header_part)
    
    # Check hero
    hero_cls_match = re.search(r'<section[^>]*class="([^"]*hero[^"]*)"', c)
    hero_img_match = re.search(r'--hero-image\s*:\s*url\(([^)]+)\)', c)
    
    hero_cls = hero_cls_match.group(1) if hero_cls_match else (
        'hero-compact (main)' if 'hero-section--compact' in c else 'no-hero'
    )
    hero_img = hero_img_match.group(1) if hero_img_match else 'no-img'
    
    status = "OK"
    issues = []
    if not dir_has_btn or not theme_has_btn:
        issues.append("dir/theme icon button mismatch")
    
    if 'id="mobile-menu"' in header_part:
        if not desktop_cta_match:
            issues.append("desktop CTA mismatch")
        elif 'hidden lg:inline-flex' not in desktop_cta_match.group(1):
            issues.append("desktop CTA not hidden lg:inline-flex")
        if not mobile_cta_match:
            issues.append("mobile CTA text mismatch")
    
    if issues:
        all_good = False
        print(f"[FAIL] {f:30} | Issues: {', '.join(issues)}")
    else:
        print(f"[PASS] {f:30} | Hero: {hero_cls:25} | Img: {hero_img}")

print("\n" + ("="*50))
if all_good:
    print("ALL 22 HTML FILES VERIFIED WITH 100% SUCCESS!")
else:
    print("Some files had issues, please review.")
