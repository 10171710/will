import glob
import re

files = sorted(glob.glob('*.html'))
for f in files:
    content = open(f, 'r', encoding='utf-8').read()
    hero_match = re.search(r'class="[^"]*hero-media[^"]*"[^>]*style="([^"]*)"', content)
    theme_btn = re.search(r'<button[^>]*id="theme-toggle"[^>]*>([\s\S]*?)</button>', content)
    dir_btn = re.search(r'<button[^>]*id="dir-toggle"[^>]*>([\s\S]*?)</button>', content)
    print("=" * 60)
    print(f"FILE: {f}")
    print(f"  Hero Style: {hero_match.group(1) if hero_match else 'NO HERO-MEDIA'}")
    if theme_btn:
        print(f"  Theme Toggle: {theme_btn.group(0)}")
    else:
        print("  Theme Toggle: NOT FOUND")
    if dir_btn:
        print(f"  Dir Toggle: {dir_btn.group(0)}")
    else:
        print("  Dir Toggle: NOT FOUND")
