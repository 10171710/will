import glob
import re
import os

pages = sorted(glob.glob('*.html'))
print(f"Checking {len(pages)} HTML pages...")

all_imgs = []
errors = []

for p in pages:
    c = open(p, 'r', encoding='utf-8').read()
    
    # Check Theme Toggle
    theme_match = re.search(r'<button[^>]*id="theme-toggle"[^>]*>([\s\S]*?)</button>', c)
    if not theme_match:
        errors.append(f"{p}: Missing #theme-toggle")
    else:
        if 'ri-moon-line' not in theme_match.group(1):
            errors.append(f"{p}: #theme-toggle missing ri-moon-line")
        if 'header-icon-btn' not in theme_match.group(0):
            errors.append(f"{p}: #theme-toggle missing header-icon-btn class")
            
    # Check Dir Toggle
    dir_match = re.search(r'<button[^>]*id="dir-toggle"[^>]*>([\s\S]*?)</button>', c)
    if not dir_match:
        errors.append(f"{p}: Missing #dir-toggle")
    else:
        if 'ri-arrow-left-right-line' not in dir_match.group(1):
            errors.append(f"{p}: #dir-toggle missing ri-arrow-left-right-line")
        if 'header-icon-btn' not in dir_match.group(0):
            errors.append(f"{p}: #dir-toggle missing header-icon-btn class")
            
    # Check Hero Media
    hero_match = re.search(r'<div class="hero-media[^"]*"[^>]*style="([^"]*)"', c)
    if not hero_match:
        errors.append(f"{p}: Missing .hero-media or inline style")
    else:
        style_content = hero_match.group(1)
        img_match = re.search(r'background-image:\s*url\([\'"]?([^\'"\)]+)[\'"]?\)', style_content)
        if not img_match:
            errors.append(f"{p}: Invalid background-image format in hero-media: {style_content}")
        else:
            img_path = img_match.group(1)
            if not os.path.exists(img_path):
                errors.append(f"{p}: Hero image file does not exist: {img_path}")
            all_imgs.append((p, img_path))

# Check duplicates
img_counts = {}
for p, img in all_imgs:
    img_counts[img] = img_counts.get(img, 0) + 1

for img, count in img_counts.items():
    if count > 1:
        dup_pages = [p for p, i in all_imgs if i == img]
        errors.append(f"Duplicate image '{img}' used in: {dup_pages}")

# Check CSS
css_content = open('assets/css/style.css', 'r', encoding='utf-8').read()
if 'var(--hero-image)' in css_content:
    errors.append("assets/css/style.css still contains var(--hero-image)")
if '.header-icon-btn' not in css_content:
    errors.append("assets/css/style.css missing .header-icon-btn")

if errors:
    print("ERRORS FOUND:")
    for e in errors:
        print(f"  - {e}")
else:
    print(f"ALL CHECKS PASSED PERFECTLY across all {len(pages)} pages!")
    print("\nSummary of hero image mappings:")
    for p, img in all_imgs:
        print(f"  {p:<30} -> {img}")
